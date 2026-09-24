from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

from mcq_bank import CELL_MATRIX, EXTRA_PROBES, NEW_QUESTIONS, OLD_QUESTION_PRIMARY

ROOT = Path(__file__).resolve().parent
VALIDATOR = ROOT / "validate_package.py"
MCQ_COUNT = len(OLD_QUESTION_PRIMARY) + len(NEW_QUESTIONS) + len(EXTRA_PROBES)
CASES = [
    ("missing-required", "README.md", None, "MISSING_REQUIRED_FILE"),
    ("destination-tamper", "FORMAL-SOURCE-MIRROR.md", ("anchor_append",), "DESTINATION_PAYLOAD_HASH_MISMATCH"),
    ("snapshot-tamper", "source-snapshots/formal-session.md", ("append", "\nsource tamper\n"), "SOURCE_SNAPSHOT_HASH_MISMATCH"),
    ("source-hash-tamper", "FORMAL-COVERAGE-REVIEW.json", ("replace", "9a0e5593fcba75966b2c3a57fe64402b4a6c0854dfeb3dce3463dc11e5ac5483", "0" * 64), "SOURCE_HASH_MISMATCH"),
    ("source-original-path-tamper", "FORMAL-COVERAGE-REVIEW.json", ("source_path",), "SOURCE_ORIGINAL_PATH_MISMATCH"),
    ("source-byte-count-tamper", "FORMAL-COVERAGE-REVIEW.json", ("source_bytes",), "SOURCE_BYTE_LENGTH_MISMATCH"),
    ("prelude-coverage-removal", "FORMAL-COVERAGE-REVIEW.json", ("remove_prelude",), "SOURCE_BLOCK_RECONSTRUCTION_SET"),
    ("hierarchy-coordinated-tamper", "FORMAL-COVERAGE-REVIEW.json", ("hierarchy_coordinated",), "SOURCE_STRUCTURE_RECONSTRUCTION_MISMATCH"),
    ("panel-coordinated-tamper", "FORMAL-COVERAGE-REVIEW.json", ("panel_coordinated",), "PANEL_RECONSTRUCTION_MISMATCH"),
    ("proposition-normalization-tamper", "FORMAL-COVERAGE-REVIEW.json", ("proposition_normalization",), "PROPOSITION_CATALOG_MISMATCH"),
    ("proposition-occurrence-tamper", "FORMAL-COVERAGE-REVIEW.json", ("proposition_occurrence",), "PROPOSITION_OCCURRENCE_MISMATCH"),
    ("panel-semantic-unit-merge", "FORMAL-COVERAGE-REVIEW.json", ("panel_semantic_merge",), "PANEL_SEMANTIC_UNIT_STRUCTURE"),
    ("structural-yaml-as-proposition", "FORMAL-COVERAGE-REVIEW.json", ("structural_as_proposition", "yaml_frontmatter"), "STRUCTURAL_UNIT_AS_PROPOSITION"),
    ("structural-legacy-mcq-heading-as-proposition", "FORMAL-COVERAGE-REVIEW.json", ("structural_as_proposition", "heading", "32 original MCQs"), "STRUCTURAL_UNIT_AS_PROPOSITION"),
    ("structural-code-fence-as-proposition", "FORMAL-COVERAGE-REVIEW.json", ("structural_as_proposition", "code_fence_open"), "STRUCTURAL_UNIT_AS_PROPOSITION"),
    ("structural-table-header-as-proposition", "FORMAL-COVERAGE-REVIEW.json", ("structural_as_proposition", "table_header"), "STRUCTURAL_UNIT_AS_PROPOSITION"),
    ("structural-diagram-border-as-proposition", "FORMAL-COVERAGE-REVIEW.json", ("structural_as_proposition", "diagram_border_or_connector_only"), "STRUCTURAL_UNIT_AS_PROPOSITION"),
    ("excluded-structural-omission", "FORMAL-COVERAGE-REVIEW.json", ("excluded_omission",), "EXCLUDED_STRUCTURAL_COUNT_MISMATCH"),
    ("excluded-structural-type-tamper", "FORMAL-COVERAGE-REVIEW.json", ("excluded_type",), "EXCLUDED_STRUCTURAL_TYPE_MISMATCH"),
    ("excluded-structural-hash-tamper", "FORMAL-COVERAGE-REVIEW.json", ("excluded_hash",), "EXCLUDED_STRUCTURAL_HASH_MISMATCH"),
    ("excluded-structural-accounting-tamper", "FORMAL-COVERAGE-REVIEW.json", ("excluded_accounting",), "EXCLUDED_STRUCTURAL_ACCOUNTING_MISMATCH"),
    ("meaningful-sample-tamper", "FORMAL-COVERAGE-REVIEW.json", ("meaningful_sample",), "MEANINGFUL_PROPOSITION_SAMPLE_MISMATCH"),
    ("decision-proposition-tamper", "FORMAL-COVERAGE-REVIEW.json", ("decision_proposition",), "DECISION_PROPOSITION_COVERAGE"),
    ("proposition-dedup-tamper", "FORMAL-COVERAGE-REVIEW.json", ("proposition_dedup",), "PROPOSITION_ACCOUNTING_MISMATCH"),
    ("child-union-tamper", "FORMAL-COVERAGE-REVIEW.json", ("child_union",), "SOURCE_STRUCTURE_RECONSTRUCTION_MISMATCH"),
    ("segment-hash-tamper", "FORMAL-COVERAGE-REVIEW.json", ("segment_hash",), "LARGE_LEAF_SEGMENT_HASH"),
    ("panel-parity-tamper", "FORMAL-COVERAGE-REVIEW.json", ("panel",), "PANEL_RECONSTRUCTION_MISMATCH"),
    ("mcq-mismatch", "MCQ-SOLUTIONS.md", ("replace", "## MCQ 1.", "## MCQ 1X."), "MCQ_SOLUTION_OPTIONS_MISMATCH"),
    ("mcq-severe-imbalance", "MCQ-SOLUTIONS.md", ("answer_sequence", "A" * MCQ_COUNT), "MCQ_POSITION_IMBALANCE"),
    ("mcq-predictable-cycle", "MCQ-SOLUTIONS.md", ("answer_sequence", ("ABCD" * ((MCQ_COUNT + 3) // 4))[:MCQ_COUNT]), "MCQ_PREDICTABLE_CYCLE"),
    ("mcq-uncovered-cell", "MCQ-AUDIT.json", ("uncovered_cell",), "MCQ_UNCOVERED_CELL"),
    ("mcq-unknown-cell-mapping", "MCQ-AUDIT.json", ("unknown_cell",), "MCQ_UNKNOWN_OR_SUPERFICIAL_MAPPING"),
    ("mcq-known-wrong-primary-mapping", "MCQ-AUDIT.json", ("wrong_primary",), "MCQ_MAPPING_INTEGRITY"),
    ("mcq-duplicate-primary-inference", "MCQ-AUDIT.json", ("duplicate_inference",), "MCQ_DUPLICATE_PRIMARY_INFERENCE"),
    ("mcq-duplicate-stem", "MCQ-QUESTIONS.md", ("duplicate_stem",), "MCQ_DUPLICATE_STEM"),
    ("mcq-paraphrase-duplicate-distinct-audit", "MCQ-QUESTIONS.md", ("paraphrase_duplicate",), "MCQ_NEAR_DUPLICATE_INFERENCE"),
    ("mcq-coordinated-question-audit-drift", "MCQ-QUESTIONS.md", ("coordinated_question_audit",), "MCQ_AUTHORED_RENDER_MISMATCH"),
    ("mcq-authored-correct-proposition-omitted", "mcq_bank.py", ("correct_proposition_omit",), "MCQ_CORRECT_PROPOSITION_CONTRACT"),
    ("mcq-authored-correct-proposition-substituted", "mcq_bank.py", ("correct_proposition_substitute",), "MCQ_CORRECT_PROPOSITION_CONTRACT"),
    ("mcq-per-item-length-cue", "MCQ-QUESTIONS.md", ("per_item_length",), "MCQ_ITEM_LENGTH_CUE"),
    ("mcq-audit-count-tamper", "MCQ-AUDIT.json", ("audit_count",), "MCQ_AUDIT_COUNT_TAMPER"),
    ("pyq-mutation", "ANSWER-WRITING-TOOLKIT.md", ("replace_all", "How do the Mādhyamika Buddhists apply the notion of Pratītyasamutpāda to establish their doctrine of Śūnyatā? Discuss.", "How do Mādhyamika Buddhists establish emptiness?"), "PYQ_SNAPSHOT_RECONSTRUCTION_MISMATCH"),
    ("pyq-coordinated-audit-surface-tamper", "PYQ-DEMAND-AUDIT.json", ("pyq_coordinated",), "PYQ_SNAPSHOT_RECONSTRUCTION_MISMATCH"),
    ("stale-primary-count-variant", "REVISION-GUIDE.md", ("append", "\nPrimary-owned PYQs total: thirteen.\n"), "LEARNER_PYQ_COUNT_STALE"),
    ("stale-pdf", "REVISION-GUIDE.md", ("append", "\nStale mutation.\n"), "STALE_PDF_OR_MANIFEST"),
]


def invoke(copy: Path, release: bool = False) -> tuple[int, dict]:
    cmd = [sys.executable, "-B", str(copy / "validate_package.py"), "--root", str(copy), "--check-only"]
    if release:
        cmd.append("--release")
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    p = subprocess.run(cmd, text=True, encoding="utf-8", errors="replace", capture_output=True, env=env)
    try:
        data = json.loads(p.stdout)
    except Exception:
        data = {"errors": [{"code": "UNPARSEABLE", "detail": (p.stdout or "") + (p.stderr or "")}]}
    return p.returncode, data


def invoke_normally(copy: Path) -> tuple[int, dict]:
    env = dict(os.environ)
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    env["PYTHONIOENCODING"] = "utf-8"
    p = subprocess.run(
        [sys.executable, str(copy / "validate_package.py"), "--root", str(copy), "--check-only"],
        text=True, encoding="utf-8", errors="replace", capture_output=True, env=env,
    )
    try:
        data = json.loads(p.stdout)
    except Exception:
        data = {"errors": [{"code": "UNPARSEABLE", "detail": (p.stdout or "") + (p.stderr or "")}]}
    return p.returncode, data


def prepare(copy: Path) -> None:
    shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".negative-tests-work", "__pycache__", "*.pyc"))
    validation = copy / "VALIDATION.json"
    if not validation.exists():
        validation.write_text('{"state":"DEVELOPMENT_PASS","release_ready":false}\n', encoding="utf-8")


def main() -> int:
    work = ROOT / ".negative-tests-work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    results = []
    try:
        copy = work / "ordinary-cache-free-acceptance"
        prepare(copy)
        rc, data = invoke_normally(copy)
        cache_artifacts = [
            str(path.relative_to(copy))
            for path in [*copy.rglob("__pycache__"), *copy.rglob("*.pyc")]
        ]
        results.append({
            "case": "ordinary-cache-free-acceptance",
            "expected": "DEVELOPMENT_PASS and no bytecode artifacts",
            "returncode": rc,
            "codes": [e.get("code") for e in data.get("errors", [])],
            "cache_artifacts": cache_artifacts,
            "passed": rc == 0 and data.get("state") == "DEVELOPMENT_PASS" and not cache_artifacts,
        })
        for name, rel, mutation, expected in CASES:
            copy = work / name
            prepare(copy)
            target = copy / rel
            if mutation is None:
                target.unlink()
            else:
                text = target.read_text(encoding="utf-8")
                if mutation[0] == "replace":
                    text = text.replace(mutation[1], mutation[2], 1)
                elif mutation[0] == "replace_all":
                    text = text.replace(mutation[1], mutation[2])
                elif mutation[0] == "source_path":
                    review = json.loads(text)
                    review["sources"]["formal_session"]["path"] += ".tampered"
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "source_bytes":
                    review = json.loads(text)
                    review["sources"]["formal_session"]["bytes"] += 1
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "anchor_append":
                    review = json.loads((copy / "FORMAL-COVERAGE-REVIEW.json").read_text(encoding="utf-8"))
                    anchor = review["decisions"][0]["destination"]["anchor"]
                    token = f'<a id="{anchor}"></a>'
                    text = text.replace(token, token + "\nTAMPERED PAYLOAD", 1)
                elif mutation[0] == "remove_prelude":
                    review = json.loads(text)
                    prelude = next(d for d in review["decisions"] if d["ordinal"] == 0)
                    review["decisions"] = [d for d in review["decisions"] if d["id"] != prelude["id"]]
                    review["raw_proposition_mappings"] = [
                        m for m in review["raw_proposition_mappings"] if m["source_block_id"] != prelude["id"]
                    ]
                    review["decision_count"] -= 1
                    review["classification_counts"]["covered_in_scope"] -= 1
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "hierarchy_coordinated":
                    review = json.loads(text)
                    parent = next(d for d in review["decisions"] if d["direct_children"])
                    parent["direct_children"] = []
                    parent["child_union_sha256"] = __import__("hashlib").sha256(b"").hexdigest()
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "panel_coordinated":
                    review = json.loads(text)
                    panel = next(d for d in review["decisions"] if "ASCII MASTER FLOW" in d["heading"])
                    panel["heading"] = panel["heading"].replace("ASCII MASTER FLOW", "MASTER FLOW", 1)
                    review["panel_parity"]["actual"] = 13
                    review["panel_parity"]["panel_ids"] = [
                        value for value in review["panel_parity"]["panel_ids"] if value != panel["id"]
                    ]
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "proposition_normalization":
                    review = json.loads(text)
                    prop = next(iter(review["proposition_catalog"].values()))
                    prop["normalized_semantic_payload"] += " tampered"
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "proposition_occurrence":
                    review = json.loads(text)
                    review["raw_proposition_mappings"][0]["raw_payload_sha256"] = "0" * 64
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "panel_semantic_merge":
                    review = json.loads(text)
                    rows = review["raw_proposition_mappings"]
                    first_index = next(
                        i for i, row in enumerate(rows[:-1])
                        if row["segment_type"] == "diagram_text_row"
                        and rows[i + 1]["segment_type"] == "diagram_text_row"
                        and rows[i + 1]["source_block_id"] == row["source_block_id"]
                    )
                    rows[first_index]["relative_line_end"] = rows[first_index + 1]["relative_line_end"]
                    rows[first_index]["absolute_line_end"] = rows[first_index + 1]["absolute_line_end"]
                    del rows[first_index + 1]
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "structural_as_proposition":
                    review = json.loads(text)
                    candidates = [
                        row for row in review["excluded_structural_coordinates"]
                        if row["structural_type"] == mutation[1]
                    ]
                    if len(mutation) > 2:
                        needle = mutation[2]
                        matching = []
                        for row in candidates:
                            snapshot_name = {
                                "formal_session": "formal-session.md",
                                "formal_workbook": "formal-workbook.md",
                            }[row["source_key"]]
                            candidate_lines = (copy / "source-snapshots" / snapshot_name).read_text(
                                encoding="utf-8"
                            ).replace("\r\n", "\n").splitlines()
                            candidate_raw = "\n".join(candidate_lines[
                                row["absolute_line_start"] - 1:row["absolute_line_end"]
                            ])
                            if needle in candidate_raw:
                                matching.append(row)
                        candidates = matching
                    structural = candidates[0]
                    snapshot_name = {
                        "formal_session": "formal-session.md",
                        "formal_workbook": "formal-workbook.md",
                    }[structural["source_key"]]
                    source_lines = (copy / "source-snapshots" / snapshot_name).read_text(
                        encoding="utf-8"
                    ).replace("\r\n", "\n").splitlines()
                    raw = "\n".join(source_lines[
                        structural["absolute_line_start"] - 1:structural["absolute_line_end"]
                    ]).strip() + "\n"
                    if structural["structural_type"] == "blank_line":
                        raw = "\n"
                    normalized = re.sub(r"\s+", " ", raw).strip()
                    digest = __import__("hashlib").sha256(normalized.encode("utf-8")).hexdigest()
                    proposition_id = f"prop-{digest[:20]}"
                    block_rows = [
                        row for row in review["raw_proposition_mappings"]
                        if row["source_block_id"] == structural["source_block_id"]
                    ]
                    occurrence_index = max((row["occurrence_index"] for row in block_rows), default=0) + 1
                    mapping = {
                        "mapping_id": f"map-{structural['source_block_id']}-{occurrence_index:03d}",
                        "source_block_id": structural["source_block_id"],
                        "source_key": structural["source_key"],
                        "occurrence_index": occurrence_index,
                        "segment_type": structural["structural_type"],
                        "relative_line_start": structural["relative_line_start"],
                        "relative_line_end": structural["relative_line_end"],
                        "absolute_line_start": structural["absolute_line_start"],
                        "absolute_line_end": structural["absolute_line_end"],
                        "raw_payload_sha256": structural["raw_payload_sha256"],
                        "proposition_id": proposition_id,
                        "normalized_payload_sha256": digest,
                    }
                    review["raw_proposition_mappings"].append(mapping)
                    review["proposition_catalog"][proposition_id] = {
                        "id": proposition_id,
                        "normalized_semantic_payload": normalized,
                        "normalized_payload_sha256": digest,
                        "normalization": "Unicode NFC plus whitespace collapse of one deterministic source-authored semantic unit",
                    }
                    decision = next(
                        row for row in review["decisions"] if row["id"] == structural["source_block_id"]
                    )
                    if proposition_id not in decision["proposition_ids"]:
                        decision["proposition_ids"].append(proposition_id)
                    catalog_hash = __import__("hashlib").sha256(
                        json.dumps(review["proposition_catalog"], ensure_ascii=False, sort_keys=True).encode("utf-8")
                    ).hexdigest()
                    mappings_hash = __import__("hashlib").sha256(
                        json.dumps(review["raw_proposition_mappings"], ensure_ascii=False, sort_keys=True).encode("utf-8")
                    ).hexdigest()
                    review["proposition_accounting"].update({
                        "raw_mapping_count": len(review["raw_proposition_mappings"]),
                        "unique_normalized_proposition_count": len(review["proposition_catalog"]),
                        "duplicate_raw_mapping_count": (
                            len(review["raw_proposition_mappings"]) - len(review["proposition_catalog"])
                        ),
                        "catalog_sha256": catalog_hash,
                        "raw_mappings_sha256": mappings_hash,
                    })
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                    audit_path = copy / "FORMAL-COVERAGE-AUDIT.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    audit.update({
                        "review_sha256": __import__("hashlib").sha256(text.encode("utf-8")).hexdigest(),
                        "raw_proposition_mappings": len(review["raw_proposition_mappings"]),
                        "unique_normalized_semantic_propositions": len(review["proposition_catalog"]),
                        "deduplicated_repetitions": (
                            len(review["raw_proposition_mappings"]) - len(review["proposition_catalog"])
                        ),
                        "proposition_catalog_sha256": catalog_hash,
                        "raw_mappings_sha256": mappings_hash,
                    })
                    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                elif mutation[0] == "excluded_omission":
                    review = json.loads(text)
                    del review["excluded_structural_coordinates"][0]
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "excluded_type":
                    review = json.loads(text)
                    review["excluded_structural_coordinates"][0]["structural_type"] = "thematic_break"
                    review["excluded_structural_coordinates"][0]["segment_type"] = "thematic_break"
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "excluded_hash":
                    review = json.loads(text)
                    review["excluded_structural_coordinates"][0]["raw_payload_sha256"] = "0" * 64
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "excluded_accounting":
                    review = json.loads(text)
                    review["excluded_structural_accounting"]["total_excluded"] += 1
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "meaningful_sample":
                    review = json.loads(text)
                    review["meaningful_proposition_verification"]["samples"][0]["proposition_id"] = "prop-" + "0" * 20
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "decision_proposition":
                    review = json.loads(text)
                    review["decisions"][0]["proposition_ids"] = []
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "proposition_dedup":
                    review = json.loads(text)
                    review["proposition_accounting"]["unique_normalized_proposition_count"] += 1
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "child_union":
                    review = json.loads(text)
                    parent = next(d for d in review["decisions"] if d["direct_children"])
                    parent["child_union_sha256"] = "0" * 64
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "segment_hash":
                    review = json.loads(text)
                    leaf = next(d for d in review["decisions"] if d["large_leaf_segments"])
                    leaf["large_leaf_segments"][0]["payload_sha256"] = "0" * 64
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "panel":
                    review = json.loads(text)
                    review["panel_parity"]["actual"] = 13
                    text = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "append":
                    text += mutation[1]
                elif mutation[0] == "answer_sequence":
                    answers = iter(mutation[1])
                    text = re.sub(
                        r"\*\*Answer:\s*[A-D]\.\*\*",
                        lambda _: f"**Answer: {next(answers)}.**",
                        text,
                    )
                    audit_path = copy / "MCQ-AUDIT.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    audit["answer_sequence"] = mutation[1]
                    audit["answer_counts"] = {letter: mutation[1].count(letter) for letter in "ABCD"}
                    audit["position_policy"]["predictable_cycle_detected"] = mutation[1].startswith("ABCDABCDABCD")
                    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                elif mutation[0] == "uncovered_cell":
                    audit = json.loads(text)
                    target_cell = audit["test_cells"][0]["id"]
                    audit["question_mapping"] = [
                        row for row in audit["question_mapping"] if row["primary_cell"] != target_cell
                    ]
                    text = json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "unknown_cell":
                    audit = json.loads(text)
                    audit["question_mapping"][0]["secondary_cells"] = ["UNKNOWN-999"]
                    text = json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "wrong_primary":
                    audit = json.loads(text)
                    audit["question_mapping"][0]["primary_cell"] = audit["test_cells"][1]["id"]
                    text = json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "duplicate_inference":
                    audit = json.loads(text)
                    audit["question_mapping"][1]["tested_inference"] = audit["question_mapping"][0]["tested_inference"]
                    text = json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "duplicate_stem":
                    chunks = re.split(r"(?=^## MCQ \d+\.)", text, flags=re.M)
                    first = next(chunk for chunk in chunks if chunk.startswith("## MCQ 1."))
                    second_index = next(i for i, chunk in enumerate(chunks) if chunk.startswith("## MCQ 2."))
                    first_stem = first.split("\n\nA.", 1)[0].split("\n", 1)[1].strip()
                    second = chunks[second_index]
                    option_start = second.index("\nA.")
                    header_end = second.index("\n")
                    chunks[second_index] = second[:header_end + 1] + "\n" + first_stem + second[option_start:]
                    text = "".join(chunks)
                    audit_path = copy / "MCQ-AUDIT.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    audit["question_mapping"][1]["stem_sha256"] = audit["question_mapping"][0]["stem_sha256"]
                    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                elif mutation[0] == "paraphrase_duplicate":
                    for surface_name, solution in (("MCQ-QUESTIONS.md", False), ("MCQ-SOLUTIONS.md", True)):
                        surface_path = copy / surface_name
                        surface = surface_path.read_text(encoding="utf-8")
                        suffix = "-solution" if solution else ""
                        source_match = re.search(
                            rf'<a id="mcq-001{suffix}"></a>.*?(?=\n<a id="mcq-002{suffix}"></a>)',
                            surface, re.S,
                        )
                        target_match = re.search(
                            rf'<a id="mcq-002{suffix}"></a>.*?(?=\n<a id="mcq-003{suffix}"></a>)',
                            surface, re.S,
                        )
                        duplicate = source_match.group(0)
                        duplicate = duplicate.replace(f"mcq-001{suffix}", f"mcq-002{suffix}", 1)
                        duplicate = duplicate.replace("## MCQ 1.", "## MCQ 2. Paraphrased", 1)
                        duplicate = duplicate.replace("Which of the following", "Select which of the following", 1)
                        surface = surface[:target_match.start()] + duplicate + surface[target_match.end():]
                        surface_path.write_text(surface, encoding="utf-8", newline="\n")
                    audit_path = copy / "MCQ-AUDIT.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    audit["question_mapping"][1]["tested_inference"] = "A manually distinct audit label that hides a paraphrase duplicate"
                    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    text = target.read_text(encoding="utf-8")
                elif mutation[0] == "coordinated_question_audit":
                    for surface_name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                        surface_path = copy / surface_name
                        surface = surface_path.read_text(encoding="utf-8")
                        first_end = surface.find('<a id="mcq-002')
                        head, tail = surface[:first_end], surface[first_end:]
                        head = re.sub(
                            r'(<a id="mcq-001(?:-solution)?"></a>\n## MCQ 1\..+?\n\n)(.+?)(\n\nA\.)',
                            lambda m: m.group(1) + m.group(2) + " This coordinated wording was not authored." + m.group(3),
                            head, count=1, flags=re.S,
                        )
                        surface_path.write_text(head + tail, encoding="utf-8", newline="\n")
                    audit_path = copy / "MCQ-AUDIT.json"
                    audit = json.loads(audit_path.read_text(encoding="utf-8"))
                    questions = (copy / "MCQ-QUESTIONS.md").read_text(encoding="utf-8")
                    block = re.search(r'## MCQ 1\..*?(?=\n<a id="mcq-002")', questions, re.S).group(0)
                    stem = block.split("\n\nA.", 1)[0].split("\n", 1)[1].strip()
                    row = audit["question_mapping"][0]
                    norm = re.sub(r"\s+", " ", stem).strip().lower()
                    row["stem_sha256"] = __import__("hashlib").sha256(norm.encode("utf-8")).hexdigest()
                    row["tested_inference"] = "Coordinated drift label distinct from the source-authored operation"
                    row["authored_evidence"]["tested_operation"] = stem
                    row["authored_evidence_sha256"] = __import__("hashlib").sha256(
                        json.dumps(row["authored_evidence"], ensure_ascii=False, sort_keys=True).encode("utf-8")
                    ).hexdigest()
                    audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                    text = target.read_text(encoding="utf-8")
                elif mutation[0] == "correct_proposition_omit":
                    text = text.replace(
                        '        "correct_proposition": correct_proposition,\n',
                        "",
                        1,
                    )
                elif mutation[0] == "correct_proposition_substitute":
                    text = text.replace(
                        '        "correct_proposition": correct_proposition,\n',
                        '        "correct_proposition": normalized_rationale,\n',
                        1,
                    )
                elif mutation[0] == "per_item_length":
                    solutions_path = copy / "MCQ-SOLUTIONS.md"
                    solutions = solutions_path.read_text(encoding="utf-8")
                    first_solution = re.search(
                        r'(<a id="mcq-001-solution"></a>.*?)(?=\n<a id="mcq-002-solution"></a>)',
                        solutions, re.S,
                    ).group(1)
                    answer = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", first_solution).group(1)
                    extra = " while uniquely adding an extended chain of qualifications that no competing option contains in comparable form"
                    for surface_name in ("MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md"):
                        surface_path = copy / surface_name
                        surface = surface_path.read_text(encoding="utf-8")
                        first_end = surface.find('<a id="mcq-002')
                        head, tail = surface[:first_end], surface[first_end:]
                        head = re.sub(rf"^{answer}\.\s+(.+)$", lambda m: f"{answer}. {m.group(1)}{extra}", head, count=1, flags=re.M)
                        surface_path.write_text(head + tail, encoding="utf-8", newline="\n")
                    text = target.read_text(encoding="utf-8")
                elif mutation[0] == "audit_count":
                    audit = json.loads(text)
                    audit["derivation"]["question_count"] += 1
                    text = json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
                elif mutation[0] == "pyq_coordinated":
                    audit = json.loads(text)
                    old = audit["questions"][-1]["text"]
                    new = "How does momentariness affect action and responsibility? Critically discuss."
                    audit["questions"][-1]["text"] = new
                    audit["questions"][-1]["text_sha256"] = __import__("hashlib").sha256(new.encode("utf-8")).hexdigest()
                    text = json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
                    for surface_name in ("REVISION-GUIDE.md", "ANSWER-WRITING-TOOLKIT.md"):
                        surface_path = copy / surface_name
                        surface_path.write_text(
                            surface_path.read_text(encoding="utf-8").replace(old, new),
                            encoding="utf-8", newline="\n",
                        )
                else:
                    text += mutation[1]
                target.write_text(text, encoding="utf-8", newline="\n")
            rc, data = invoke(copy)
            codes = [e.get("code") for e in data.get("errors", [])]
            ok = rc != 0 and expected in codes
            results.append({"case": name, "expected": expected, "returncode": rc, "codes": codes, "passed": ok})
        copy = work / "release-not-staged"
        prepare(copy)
        validation_hash_before = __import__("hashlib").sha256((copy / "VALIDATION.json").read_bytes()).hexdigest()
        rc, data = invoke(copy, release=True)
        validation_hash_after = __import__("hashlib").sha256((copy / "VALIDATION.json").read_bytes()).hexdigest()
        codes = [e.get("code") for e in data.get("errors", [])]
        results.append({"case": "release-not-staged", "expected": "GIT_RELEASE_NOT_STAGED", "returncode": rc,
                        "codes": codes, "non_mutating": validation_hash_before == validation_hash_after,
                        "passed": rc != 0 and "GIT_RELEASE_NOT_STAGED" in codes and validation_hash_before == validation_hash_after})
    finally:
        shutil.rmtree(work, ignore_errors=True)
    out = {"total": len(results), "passed": sum(x["passed"] for x in results), "results": results}
    print(json.dumps(out, indent=2))
    return 0 if all(x["passed"] for x in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
