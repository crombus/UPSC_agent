from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
IST = timezone(timedelta(hours=5, minutes=30))
REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "COVERAGE-LEDGER.md", "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md", "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md",
    "FORMAL-COVERAGE-REVIEW.json", "FORMAL-COVERAGE-AUDIT.json", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "PDF-MANIFEST.json", "validate_package.py", "build_package.py",
    "render_pdfs.py", "run_negative_tests.py", "FORMAL-SOURCE-MIRROR.md", "VALIDATION.json",
    "pdf/Jainism-Revision-Guide.pdf", "pdf/Jainism-MCQ-Questions.pdf",
    "pdf/Jainism-MCQ-Solutions.pdf", "pdf/Jainism-Answer-Writing-Toolkit.pdf",
]
EXPECTED_HASHES = {
    "formal_session": "de8b2c8fde2819b60c7a7f6a983300651082394fd6a434b5c832d6af3c2b6c90",
    "formal_workbook": "b101222aa4f7d3098f59f1856e87f534d5a94d79fd18a4f2a493f4ca84762a54",
    "canonical": "cefb795a8623a2b4fda5f74fde0eb872261674779b8d36e3dc3f57ba6e0bf3c7",
    "pyq_2018_2025": "c7b556c7b4b750943b7b5f0ac94273664a46c6c75f1c444ae2d953fd77d34eec",
    "pyq_2026": "1e3b86dbf301bf929851ecc39f1b8585485707cd19fc7a2168861bbb142a8806",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha(text: str) -> str:
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def fail(errors: list[dict], code: str, detail: str) -> None:
    errors.append({"code": code, "detail": detail})


def anchor_payload(text: str, anchor: str) -> str | None:
    token = f'<a id="{anchor}"></a>'
    start = text.find(token)
    if start < 0:
        return None
    start = text.find("\n", start) + 1
    next_anchor = text.find("\n<a id=", start)
    end = len(text) if next_anchor < 0 else next_anchor
    return text[start:end].strip() + "\n"


def parse_mcq_surface(text: str) -> dict[int, dict]:
    out = {}
    chunks = re.split(r"(?=^## MCQ \d+\.)", text, flags=re.M)
    for ch in chunks:
        m = re.match(r"## MCQ (\d+)\.\s*(.+)\n", ch)
        if not m:
            continue
        opts = {}
        for om in re.finditer(r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:|\n<a id=|\n## |\Z)", ch, re.M | re.S):
            opts[om.group(1)] = re.sub(r"\s+", " ", om.group(2).strip())
        ans = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", ch)
        exps = {}
        for em in re.finditer(r"^- \*\*([A-D]):\*\*\s*(.+)$", ch, re.M):
            exps[em.group(1)] = em.group(2).strip()
        out[int(m.group(1))] = {"options": opts, "answer": ans.group(1) if ans else None, "explanations": exps}
    return out


def has_predictable_cycle(sequence: str) -> bool:
    for period in range(2, 5):
        width = period * 3
        for start in range(0, len(sequence) - width + 1):
            window = sequence[start:start + width]
            unit = window[:period]
            if len(set(unit)) > 1 and window == unit * 3:
                return True
    return False


def run(root: Path, release: bool) -> dict:
    errors, checks = [], {}
    for rel in REQUIRED:
        if rel == "VALIDATION.json" and not release:
            continue
        p = root / rel
        if not p.is_file():
            fail(errors, "MISSING_REQUIRED_FILE", rel)
    checks["required_files"] = len(REQUIRED)
    if errors:
        return report(root, release, checks, errors)

    review = json.loads((root / "FORMAL-COVERAGE-REVIEW.json").read_text(encoding="utf-8"))
    audit = json.loads((root / "FORMAL-COVERAGE-AUDIT.json").read_text(encoding="utf-8"))
    source_texts = {}
    for key, expected in EXPECTED_HASHES.items():
        source = review.get("sources", {}).get(key, {})
        declared = source.get("sha256", "").lower()
        source_path = Path(source.get("path", ""))
        if declared != expected:
            fail(errors, "SOURCE_HASH_MISMATCH", f"{key}: declared {declared} != {expected}")
        if not source_path.is_file():
            fail(errors, "SOURCE_FILE_MISSING", f"{key}: {source_path}")
            continue
        actual = sha(source_path)
        if actual != expected:
            fail(errors, "SOURCE_HASH_MISMATCH", f"{key}: actual {actual} != {expected}")
        source_texts[key] = source_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    decisions = review.get("decisions", [])
    if review.get("decision_count") != len(decisions) or review.get("unclassified_count") != 0:
        fail(errors, "FORMAL_MAPPING_COUNT", "Decision count or unclassified count is invalid")
    decision_by_id = {d.get("id"): d for d in decisions}
    destinations = {}
    for d in decisions:
        source_key = "formal_session" if d.get("source") == "session" else "formal_workbook"
        source_lines = source_texts.get(source_key, "").splitlines()
        line_start, line_end = d.get("line_start", 0), d.get("line_end", 0)
        source_payload = ""
        if 1 <= line_start <= line_end <= len(source_lines):
            source_payload = "\n".join(source_lines[line_start - 1:line_end]).strip() + "\n"
        else:
            fail(errors, "SOURCE_BLOCK_RANGE_INVALID", d.get("id", "unknown"))
        if text_sha(source_payload) != d.get("own_payload_sha256"):
            fail(errors, "SOURCE_BLOCK_PAYLOAD_MISMATCH", d.get("id", "unknown"))
        dest = d.get("destination", {})
        f = dest.get("file", "")
        if f not in destinations and (root / f).is_file():
            destinations[f] = (root / f).read_text(encoding="utf-8").replace("\r\n", "\n")
        payload = anchor_payload(destinations.get(f, ""), dest.get("anchor", ""))
        if payload is None:
            fail(errors, "DESTINATION_ANCHOR_MISSING", d.get("id", "unknown"))
        elif text_sha(payload) != dest.get("payload_sha256"):
            fail(errors, "DESTINATION_PAYLOAD_HASH_MISMATCH", d.get("id", "unknown"))
        props = d.get("semantic_propositions", [])
        if props != [source_payload.strip()] or d.get("semantic_basis") != "exact_complete_source_owned_payload_not_excerpt":
            fail(errors, "SEMANTIC_PROPOSITION_QUALITY", d.get("id", "unknown"))
        segments = d.get("large_leaf_segments", [])
        if d.get("own_chars") != len(source_payload):
            fail(errors, "SOURCE_BLOCK_LENGTH_MISMATCH", d.get("id", "unknown"))
        if len(source_payload) > 2400 and not segments:
            fail(errors, "LARGE_LEAF_UNSEGMENTED", d.get("id", "unknown"))
        if segments:
            reconstructed = []
            for segment in segments:
                start = segment.get("start_char")
                end = segment.get("end_char_exclusive")
                if not isinstance(start, int) or not isinstance(end, int) or not 0 <= start < end <= len(source_payload):
                    fail(errors, "LARGE_LEAF_SEGMENT_RANGE", d.get("id", "unknown"))
                    continue
                chunk = source_payload[start:end]
                reconstructed.append(chunk)
                if len(chunk) != segment.get("chars") or text_sha(chunk) != segment.get("payload_sha256"):
                    fail(errors, "LARGE_LEAF_SEGMENT_HASH", f"{d.get('id', 'unknown')}:{segment.get('index')}")
            if "".join(reconstructed) != source_payload:
                fail(errors, "LARGE_LEAF_SEGMENT_UNION", d.get("id", "unknown"))
        child_payload_hashes = []
        for child_id in d.get("direct_children", []):
            child = decision_by_id.get(child_id)
            if child is None:
                fail(errors, "CHILD_ID_MISSING", f"{d.get('id', 'unknown')} -> {child_id}")
            else:
                child_payload_hashes.append(child.get("own_payload_sha256", ""))
        child_hash = text_sha("\n".join(child_payload_hashes))
        if child_hash != d.get("child_union_sha256"):
            fail(errors, "CHILD_UNION_MISMATCH", d.get("id", "unknown"))
    if audit.get("review_sha256") != sha(root / "FORMAL-COVERAGE-REVIEW.json"):
        fail(errors, "DERIVED_AUDIT_STALE", "Review hash differs")
    if audit.get("decision_count") != len(decisions) or audit.get("unclassified") != 0:
        fail(errors, "DERIVED_AUDIT_COUNT", "Derived counts differ")
    panels = [d for d in decisions if "ASCII MASTER FLOW — PANEL" in d.get("heading", "")]
    if review.get("panel_parity", {}).get("actual") != len(panels):
        fail(errors, "PANEL_PARITY_MISMATCH", f"{len(panels)} actual panels")
    checks["formal_blocks"] = len(decisions)
    checks["panels"] = len(panels)

    revision = (root / "REVISION-GUIDE.md").read_text(encoding="utf-8")
    toolkit = (root / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    doctrine_terms = [
        ("jīva", "DOCTRINE_JIVA"), ("ajīva", "DOCTRINE_AJIVA"), ("six substances", "DOCTRINE_SIX_SUBSTANCES"),
        ("karma-pudgala", "DOCTRINE_MATERIAL_KARMA"), ("āsrava", "DOCTRINE_ASRAVA"), ("bandha", "DOCTRINE_BANDHA"),
        ("saṃvara", "DOCTRINE_SAMVARA"), ("nirjarā", "DOCTRINE_NIRJARA"), ("mokṣa", "DOCTRINE_MOKSHA"),
        ("bhāvabandha", "DOCTRINE_BHAVA_BANDHA"), ("dravyabandha", "DOCTRINE_DRAVYA_BANDHA"),
        ("anekāntavāda", "DOCTRINE_ANEKANTA"), ("nayavāda", "DOCTRINE_NAYA"),
        ("syādvāda", "DOCTRINE_SYAD"), ("saptabhaṅgī", "DOCTRINE_SAPTABHANGI"),
    ]
    low = revision.lower()
    for term, code in doctrine_terms:
        if term.lower() not in low:
            fail(errors, code, term)
    forbidden = [
        r"syādvāda (?:is|means|permits|endorses) (?:mere )?relativism",
        r"syādvāda (?:is|means|permits|endorses) [“\"]?anything goes",
        r"syāt means [“\"]?perhaps",
        r"contradictions are true",
    ]
    for pat in forbidden:
        if re.search(pat, revision, re.I):
            fail(errors, "DOCTRINE_GUARDRAIL", pat)
    checks["doctrine_guardrails"] = len(doctrine_terms)

    q = parse_mcq_surface((root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8"))
    s = parse_mcq_surface((root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"))
    ma = json.loads((root / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    if len(q) != 32 or len(s) != 32 or ma.get("derivation", {}).get("question_count") != 32:
        fail(errors, "MCQ_COUNT_MISMATCH", f"questions={len(q)} solutions={len(s)}")
    seq = []
    for num in sorted(q):
        if num not in s or q[num]["options"] != s[num]["options"]:
            fail(errors, "MCQ_SOLUTION_OPTIONS_MISMATCH", str(num))
            continue
        if set(s[num]["explanations"]) != set("ABCD"):
            fail(errors, "MCQ_EXPLANATION_SYNC", str(num))
        if s[num]["answer"] not in "ABCD":
            fail(errors, "MCQ_ANSWER_MISSING", str(num))
        else:
            correct_explanations = [
                letter for letter, explanation in s[num]["explanations"].items()
                if explanation.startswith("Correct:")
            ]
            if correct_explanations != [s[num]["answer"]]:
                fail(errors, "MCQ_CORRECTNESS_SYNC", f"{num}: {correct_explanations} != {s[num]['answer']}")
            seq.append(s[num]["answer"])
    if "".join(seq) != ma.get("answer_sequence"):
        fail(errors, "MCQ_AUDIT_SEQUENCE_MISMATCH", "".join(seq))
    actual_counts = {letter: seq.count(letter) for letter in "ABCD"}
    if actual_counts != ma.get("answer_counts"):
        fail(errors, "MCQ_AUDIT_COUNTS_MISMATCH", json.dumps(actual_counts, sort_keys=True))
    if any(count < 6 or count > 10 for count in actual_counts.values()):
        fail(errors, "MCQ_POSITION_IMBALANCE", json.dumps(actual_counts, sort_keys=True))
    longest = max((len(x.group(0)) for x in re.finditer(r"(.)\1*", "".join(seq))), default=0)
    if longest > 3 or len(set(seq)) < 4:
        fail(errors, "MCQ_RANDOMIZATION_CUE", f"longest_run={longest}")
    if longest > 2:
        fail(errors, "MCQ_POSITION_RUN", f"longest_run={longest}")
    cycle = has_predictable_cycle("".join(seq))
    if cycle or ma.get("position_policy", {}).get("predictable_cycle_detected") is not False:
        fail(errors, "MCQ_PREDICTABLE_CYCLE", "".join(seq))
    if ma.get("cue_metrics", {}).get("template_filler_count") != 0:
        fail(errors, "MCQ_TEMPLATE_CUE", "Template filler detected")
    checks["mcqs"] = len(q)

    pa = json.loads((root / "PYQ-DEMAND-AUDIT.json").read_text(encoding="utf-8"))
    if pa.get("actual_total") != 10 or len(pa.get("questions", [])) != 10:
        fail(errors, "PYQ_OMISSION", "Expected ten Jain-primary PYQs")
    year_counts = {}
    for row in pa.get("questions", []):
        year_counts[str(row["year"])] = year_counts.get(str(row["year"]), 0) + 1
        if row["text"] not in toolkit or text_sha(row["text"]) != row["text_sha256"]:
            fail(errors, "PYQ_TEXT_MUTATION", f"{row['year']}: {row['text'][:45]}")
    if year_counts != pa.get("expected_year_counts"):
        fail(errors, "PYQ_YEAR_COUNTS", json.dumps(year_counts, sort_keys=True))
    primary_pattern = re.compile(
        r"^#### Primary PYQ (\d+) · (20\d\d) · (Q\d+\([a-e]\)) · (\d+) marks · Jainism · fully solved$",
        re.M,
    )
    supporting_pattern = re.compile(
        r"^#### Supporting cross-topic PYQ S1 · 2020 · Q7\(c\) · 15 marks · Cārvāka-primary / Jainism-supporting · fully solved$",
        re.M,
    )
    for surface_name, surface in (("REVISION-GUIDE.md", revision), ("ANSWER-WRITING-TOOLKIT.md", toolkit)):
        primary = primary_pattern.findall(surface)
        if len(primary) != 10 or [int(x[0]) for x in primary] != list(range(1, 11)):
            fail(errors, "PRIMARY_PYQ_NUMBERING", f"{surface_name}: {primary}")
        actual_primary = [(int(year), qno, int(marks)) for _, year, qno, marks in primary]
        expected_primary = [(int(row["year"]), row["question_no"], int(row["marks"])) for row in pa.get("questions", [])]
        if actual_primary != expected_primary:
            fail(errors, "PRIMARY_PYQ_SEQUENCE", f"{surface_name}: {actual_primary}")
        if len(supporting_pattern.findall(surface)) != 1:
            fail(errors, "SUPPORTING_PYQ_CLASSIFICATION", surface_name)
        if "#### PYQ 10 · 2020 · Q7(c)" in surface:
            fail(errors, "LEGACY_SUPPORTING_PRIMARY_NUMBER", surface_name)
        for row in pa.get("questions", []):
            if surface.count(row["text"]) != 1:
                fail(errors, "PRIMARY_PYQ_WORDING_COUNT", f"{surface_name}:{row['year']}:{surface.count(row['text'])}")
    if pa.get("supporting_total") != 1 or pa.get("supporting_questions", [{}])[0].get("ownership") != "Carvaka-primary/Jainism-supporting":
        fail(errors, "SUPPORTING_PYQ_AUDIT", "Expected one separately owned supporting PYQ")
    checks["pyqs"] = len(pa.get("questions", []))
    checks["supporting_pyqs"] = pa.get("supporting_total", 0)

    bands = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
    models = 0
    for m in re.finditer(r"\*\*Model answer \((10|15|20) marks,\s*(\d+)[–-](\d+) words\)\.\*\*\s*\n(.*?)(?=\n#### |\n## |\Z)", toolkit, re.S):
        marks = int(m.group(1))
        body = m.group(4)
        wc = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"[`*#>]", "", body), re.UNICODE))
        lo, hi = bands[marks]
        if (int(m.group(2)), int(m.group(3))) != (lo, hi) or not lo <= wc <= hi:
            fail(errors, "MAINS_WORD_BAND", f"{marks} marks: declared {m.group(2)}-{m.group(3)}, actual {wc}")
        models += 1
    if models != 17:
        fail(errors, "MAINS_MODEL_COUNT", f"Expected 17 timed models (10 primary + 1 supporting + 6 original), found {models}")
    checks["timed_models_including_mirror"] = models

    manifest = json.loads((root / "PDF-MANIFEST.json").read_text(encoding="utf-8"))
    for row in manifest.get("artifacts", []):
        src, pdf = root / row["source"], root / row["file"]
        if not src.is_file() or not pdf.is_file():
            fail(errors, "PDF_MISSING", row.get("file", ""))
            continue
        reader = PdfReader(str(pdf))
        if sha(src) != row.get("source_sha256") or sha(pdf) != row.get("pdf_sha256"):
            fail(errors, "STALE_PDF_OR_MANIFEST", row["file"])
        if len(reader.pages) != row.get("pages") or len(reader.pages) < 1:
            fail(errors, "PDF_PAGE_COUNT", row["file"])
        meta = reader.metadata or {}
        if row["source_sha256"] not in str(meta.get("/Subject", "")):
            fail(errors, "PDF_SOURCE_METADATA", row["file"])
        for i, page in enumerate(reader.pages):
            box = page.mediabox
            if float(box.width) <= 0 or float(box.height) <= 0:
                fail(errors, "PDF_INVALID_PAGE", f"{row['file']}:{i+1}")
            if not (page.extract_text() or "").strip():
                fail(errors, "PDF_EMPTY_PAGE", f"{row['file']}:{i+1}")
    if len(manifest.get("artifacts", [])) != 4:
        fail(errors, "PDF_COUNT", str(len(manifest.get("artifacts", []))))
    checks["pdfs"] = len(manifest.get("artifacts", []))

    caches = list(root.rglob("__pycache__")) + list(root.rglob("*.pyc"))
    if caches:
        fail(errors, "BYTECODE_ARTIFACT", ", ".join(str(x) for x in caches))
    if release:
        try:
            repo = Path(subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True).strip())
            relroot = root.relative_to(repo)
            staged = set(subprocess.check_output(["git", "-C", str(repo), "diff", "--cached", "--name-only"], text=True).splitlines())
            missing = [str((relroot / rel).as_posix()) for rel in REQUIRED if str((relroot / rel).as_posix()) not in staged]
            if missing:
                fail(errors, "GIT_RELEASE_NOT_STAGED", f"{len(missing)} required artifacts are not staged")
            for rel in REQUIRED:
                rp = str((relroot / rel).as_posix())
                if rp not in staged:
                    continue
                staged_oid = subprocess.check_output(
                    ["git", "-C", str(repo), "rev-parse", f":{rp}"],
                    text=True,
                ).strip()
                working_oid = subprocess.check_output(
                    [
                        "git",
                        "-C",
                        str(repo),
                        "hash-object",
                        f"--path={rp}",
                        str(root / rel),
                    ],
                    text=True,
                ).strip()
                if staged_oid != working_oid:
                    fail(errors, "GIT_STAGED_CONTENT_STALE", rp)
        except Exception as exc:
            fail(errors, "GIT_RELEASE_CHECK_FAILED", str(exc))
    return report(root, release, checks, errors)


def report(root: Path, release: bool, checks: dict, errors: list[dict]) -> dict:
    state = "RELEASE_PASS" if release and not errors else ("DEVELOPMENT_PASS" if not release and not errors else "FAIL")
    return {"schema_version": 1, "validated_at": datetime.now(IST).replace(microsecond=0).isoformat(),
            "mode": "release" if release else "development", "state": state,
            "release_ready": bool(release and not errors), "checks": checks,
            "error_count": len(errors), "errors": errors}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=HERE)
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()
    result = run(args.root.resolve(), args.release)
    if not args.release and not args.check_only:
        (args.root / "VALIDATION.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"].endswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
