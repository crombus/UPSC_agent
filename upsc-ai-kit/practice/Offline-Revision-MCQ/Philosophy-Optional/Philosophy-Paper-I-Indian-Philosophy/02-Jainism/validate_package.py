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

HERE = Path(__file__).resolve().parent
IST = timezone(timedelta(hours=5, minutes=30))
REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "COVERAGE-LEDGER.md", "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md", "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md",
    "FORMAL-COVERAGE-REVIEW.json", "FORMAL-COVERAGE-AUDIT.json", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "TEST-MATRIX.json", "MCQ-BANK.json",
    "validate_package.py", "build_package.py", "render_pdfs.py", "run_negative_tests.py",
    "FORMAL-SOURCE-MIRROR.md", "VALIDATION.json",
]
OPTIONAL_PDF_FILES = [
    "PDF-MANIFEST.json",
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
        stem_start = ch.find("\n") + 1
        first_option = re.search(r"^[A-D]\.\s+", ch, re.M)
        stem = ch[stem_start:first_option.start()].strip() if first_option else ""
        out[int(m.group(1))] = {
            "title": m.group(2).strip(), "stem": stem, "options": opts,
            "answer": ans.group(1) if ans else None, "explanations": exps,
        }
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


MCQ_CUE_POLICY = {
    "word_count_regex": r"\b[^\W_]+(?:['’\-][^\W_]+)*\b",
    "aggregate_correct_to_distractor_ratio_max": 1.20,
    "per_item_correct_to_average_distractor_ratio_max": 1.60,
    "per_item_correct_advantage_min_words": 3.0,
    "extreme_short_keyed_min_words": 6,
    "extreme_short_distractor_max_words": 2,
    "extreme_short_distractor_to_keyed_ratio_min": 0.40,
    "visible_spread_ratio_max": 2.25,
    "visible_spread_min_gap_words": 6,
    "grammatical_parallelism_checks": ["terminal_punctuation", "initial_letter_case"],
    "noncompetitive_patterns": [
        r"\ball of the above\b",
        r"\bnone of the above\b",
        r"\bboth [A-D] and [A-D]\b",
        r"\bcannot say\b",
        r"\b(?:wholly )?(?:irrelevant|unrelated)\b",
    ],
}


def option_word_count(text: str) -> int:
    return len(re.findall(MCQ_CUE_POLICY["word_count_regex"], text, re.UNICODE))


def recompute_cue_metrics(surface: dict[int, dict]) -> dict:
    records = []
    correct_lengths, distractor_lengths = [], []
    patterns = [re.compile(pattern, re.I) for pattern in MCQ_CUE_POLICY["noncompetitive_patterns"]]
    for number in sorted(surface):
        row = surface[number]
        letters = list("ABCD")
        options = [row["options"].get(letter, "") for letter in letters]
        answer = row["answer"]
        correct_index = letters.index(answer) if answer in letters else 0
        counts = [option_word_count(text) for text in options]
        correct = counts[correct_index]
        distractors = [count for index, count in enumerate(counts) if index != correct_index]
        distractor_mean = sum(distractors) / 3
        ratio = correct / distractor_mean
        spread = max(counts) / min(counts)
        flags = []
        if ratio > MCQ_CUE_POLICY["per_item_correct_to_average_distractor_ratio_max"] and (
            correct - distractor_mean >= MCQ_CUE_POLICY["per_item_correct_advantage_min_words"]
        ):
            flags.append("correct_length_advantage")
        if correct >= MCQ_CUE_POLICY["extreme_short_keyed_min_words"]:
            for index, count in enumerate(counts):
                if index == correct_index:
                    continue
                if count <= MCQ_CUE_POLICY["extreme_short_distractor_max_words"] or (
                    count / correct < MCQ_CUE_POLICY["extreme_short_distractor_to_keyed_ratio_min"]
                ):
                    flags.append(f"extreme_short_distractor_{letters[index]}")
        if spread > MCQ_CUE_POLICY["visible_spread_ratio_max"] and (
            max(counts) - min(counts) >= MCQ_CUE_POLICY["visible_spread_min_gap_words"]
        ):
            flags.append("excessive_visible_spread")
        for index, text in enumerate(options):
            if any(pattern.search(text) for pattern in patterns):
                flags.append(f"noncompetitive_phrase_{letters[index]}")
        terminal = [text.rstrip()[-1:] for text in options]
        if len(set(terminal)) != 1:
            flags.append("terminal_punctuation_mismatch")
        initial_case = []
        for text in options:
            first = next((char for char in text if char.isalpha()), "")
            initial_case.append("upper" if first.isupper() else "lower")
        if len(set(initial_case)) != 1:
            flags.append("initial_letter_case_mismatch")
        records.append({
            "question_id": f"Q{number:03d}",
            "keyed_letter": answer,
            "word_counts": {letter: count for letter, count in zip(letters, counts)},
            "correct_to_average_distractor_ratio": round(ratio, 4),
            "visible_spread_ratio": round(spread, 4),
            "visible_spread_words": max(counts) - min(counts),
            "flags": flags,
        })
        correct_lengths.append(correct)
        distractor_lengths.extend(distractors)
    mean_correct = sum(correct_lengths) / len(correct_lengths)
    mean_distractor = sum(distractor_lengths) / len(distractor_lengths)
    aggregate_ratio = mean_correct / mean_distractor
    outliers = [row for row in records if row["flags"]]
    material_length_outliers = [
        row for row in records
        if any(flag in {"correct_length_advantage", "excessive_visible_spread"}
               for flag in row["flags"])
    ]
    return {
        "policy": MCQ_CUE_POLICY,
        "mean_correct_words": round(mean_correct, 4),
        "mean_distractor_words": round(mean_distractor, 4),
        "aggregate_correct_to_distractor_ratio": round(aggregate_ratio, 4),
        "ratio_at_or_above_1_8_count": sum(
            row["correct_to_average_distractor_ratio"] >= 1.8 for row in records
        ),
        "material_length_outlier_count": len(material_length_outliers),
        "policy_outlier_count": len(outliers),
        "noncompetitive_distractor_count": sum(
            flag.startswith(("extreme_short_distractor_", "noncompetitive_phrase_"))
            for row in records for flag in row["flags"]
        ),
        "all_options_terminal_punctuation_consistent": all(
            "terminal_punctuation_mismatch" not in row["flags"] for row in records
        ),
        "all_options_initial_letter_case_consistent": all(
            "initial_letter_case_mismatch" not in row["flags"] for row in records
        ),
        "grammar_parallel_review": (
            "passed_computed_surface_checks" if not outliers else "failed_computed_surface_checks"
        ),
        "per_item_records": records,
    }


def run(root: Path, release: bool, validate_pdfs: bool = False) -> dict:
    errors, checks = [], {}
    required_files = REQUIRED + (OPTIONAL_PDF_FILES if validate_pdfs else [])
    for rel in required_files:
        if rel == "VALIDATION.json" and not release:
            continue
        p = root / rel
        if not p.is_file():
            fail(errors, "MISSING_REQUIRED_FILE", rel)
    checks["required_files"] = len(required_files)
    checks["markdown_canonical"] = True
    checks["pdf_validation"] = "opt_in_enabled" if validate_pdfs else "optional_not_checked"
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

    q_text = (root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8")
    s_text = (root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8")
    q_numbers = [int(x) for x in re.findall(r"^## MCQ (\d+)\.", q_text, re.M)]
    s_numbers = [int(x) for x in re.findall(r"^## MCQ (\d+)\.", s_text, re.M)]
    if len(q_numbers) != len(set(q_numbers)) or len(s_numbers) != len(set(s_numbers)):
        fail(errors, "MCQ_DUPLICATE_ID", f"questions={q_numbers} solutions={s_numbers}")
    q = parse_mcq_surface(q_text)
    s = parse_mcq_surface(s_text)
    ma = json.loads((root / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    matrix = json.loads((root / "TEST-MATRIX.json").read_text(encoding="utf-8"))
    bank = json.loads((root / "MCQ-BANK.json").read_text(encoding="utf-8"))
    cells = matrix.get("cells", [])
    mappings = matrix.get("question_mappings", {})
    expected_categories = {
        "foundations": {"total": 6, "adequate": 3, "partial": 0, "uncovered": 3},
        "ontology": {"total": 13, "adequate": 6, "partial": 6, "uncovered": 1},
        "epistemology": {"total": 10, "adequate": 4, "partial": 1, "uncovered": 5},
        "many-sided logic": {"total": 26, "adequate": 11, "partial": 2, "uncovered": 13},
        "criticism-comparison-pyq": {"total": 11, "adequate": 2, "partial": 3, "uncovered": 6},
        "karma-liberation-ethics": {"total": 22, "adequate": 11, "partial": 7, "uncovered": 4},
        "transfer": {"total": 6, "adequate": 1, "partial": 1, "uncovered": 4},
    }
    if len(cells) != 94:
        fail(errors, "TEST_MATRIX_CELL_COUNT", f"Expected frozen 94 cells, found {len(cells)}")
    cell_ids = [cell.get("id") for cell in cells]
    if len(set(cell_ids)) != len(cell_ids):
        fail(errors, "TEST_MATRIX_DUPLICATE_CELL", "Cell IDs must be unique")
    baseline = {status: sum(cell.get("baseline_status") == status for cell in cells)
                for status in ("adequate", "partial", "uncovered")}
    if baseline != {"adequate": 38, "partial": 20, "uncovered": 36}:
        fail(errors, "TEST_MATRIX_BASELINE_TOTALS", json.dumps(baseline, sort_keys=True))
    for category, expected in expected_categories.items():
        rows = [cell for cell in cells if cell.get("category") == category]
        actual = {"total": len(rows)}
        actual.update({status: sum(cell.get("baseline_status") == status for cell in rows)
                       for status in ("adequate", "partial", "uncovered")})
        if actual != expected:
            fail(errors, "TEST_MATRIX_CATEGORY_TOTALS", f"{category}: {actual}")
    if matrix.get("frozen_audit", {}).get("category_totals") != expected_categories:
        fail(errors, "TEST_MATRIX_DECLARED_TOTALS", "Frozen category totals differ")
    expected_count = len(cells)
    if len(q) != expected_count or len(s) != expected_count or ma.get("derivation", {}).get("question_count") != expected_count:
        fail(errors, "MCQ_COUNT_MISMATCH", f"questions={len(q)} solutions={len(s)}")
    expected_numbers = list(range(1, expected_count + 1))
    if sorted(q) != expected_numbers or sorted(s) != expected_numbers:
        fail(errors, "MCQ_NONCONTIGUOUS_NUMBERING", f"questions={sorted(q)} solutions={sorted(s)}")
    bank_questions = bank.get("questions", [])
    bank_ids = [row.get("id") for row in bank_questions]
    if len(bank_questions) != expected_count or len(set(bank_ids)) != len(bank_ids):
        fail(errors, "MCQ_BANK_STRUCTURE", "Bank count or IDs do not match the matrix-derived count")
    if ma.get("matrix_sha256") != sha(root / "TEST-MATRIX.json") or ma.get("bank_sha256") != sha(root / "MCQ-BANK.json"):
        fail(errors, "MCQ_AUDIT_STALE", "Matrix or bank hash differs from MCQ audit")
    mapped_cells = []
    for cell in cells:
        required = {
            "category", "baseline_status", "source_evidence", "primary_discriminator",
            "minimum_probes", "mapped_question", "semantic_assertions", "final_covered_status",
        }
        if not required.issubset(cell) or cell.get("final_covered_status") != "covered":
            fail(errors, "TEST_MATRIX_CELL_INCOMPLETE", cell.get("id", "unknown"))
        qid = cell.get("mapped_question")
        mapping = mappings.get(qid)
        if not mapping:
            fail(errors, "MCQ_FALSE_MAPPING", f"{cell.get('id')} -> {qid}")
            continue
        mapping_cells = mapping.get("cell_ids", [])
        mapped_cells.extend(mapping_cells)
        if mapping.get("mapping_type") != "primary_single_cell" or len(mapping_cells) != 1:
            fail(errors, "MCQ_OVERLOADED_MAPPING", qid)
        if mapping_cells != [cell.get("id")]:
            fail(errors, "MCQ_FALSE_MAPPING", f"{cell.get('id')} -> {qid}")
        try:
            number = int(qid[1:])
            row = s[number]
            correct = row["answer"]
            evidence = " ".join([
                row["title"], row["stem"], row["options"].get(correct, ""),
                row["explanations"].get(correct, ""),
            ]).casefold()
            for assertion in cell.get("semantic_assertions", []):
                if assertion.casefold() not in evidence:
                    fail(errors, "MCQ_PRIMARY_EVIDENCE_MISSING", f"{cell.get('id')}:{qid}")
        except Exception:
            fail(errors, "MCQ_FALSE_MAPPING", f"{cell.get('id')} -> {qid}")
    if len(mapped_cells) != len(set(mapped_cells)) or set(mapped_cells) != set(cell_ids):
        fail(errors, "MCQ_REDUNDANT_MAPPING", "Cells must be mapped exactly once")
    if set(mappings) != {f"Q{i:03d}" for i in expected_numbers}:
        fail(errors, "MCQ_UNMAPPED_QUESTION", "Every question must have exactly one matrix mapping")
    seq = []
    for num in sorted(q):
        if num not in s or q[num]["options"] != s[num]["options"]:
            fail(errors, "MCQ_SOLUTION_OPTIONS_MISMATCH", str(num))
            continue
        if set(s[num]["explanations"]) != set("ABCD"):
            fail(errors, "MCQ_EXPLANATION_SYNC", str(num))
        if s[num]["answer"] not in set("ABCD"):
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
    if max(actual_counts.values()) - min(actual_counts.values()) > 2:
        fail(errors, "MCQ_POSITION_IMBALANCE", json.dumps(actual_counts, sort_keys=True))
    longest = max((len(x.group(0)) for x in re.finditer(r"(.)\1*", "".join(seq))), default=0)
    if longest > 3 or len(set(seq)) < 4:
        fail(errors, "MCQ_RANDOMIZATION_CUE", f"longest_run={longest}")
    if longest > 2:
        fail(errors, "MCQ_POSITION_RUN", f"longest_run={longest}")
    cycle = has_predictable_cycle("".join(seq))
    if cycle or ma.get("position_policy", {}).get("predictable_cycle_detected") is not False:
        fail(errors, "MCQ_PREDICTABLE_CYCLE", "".join(seq))
    cue_metrics = recompute_cue_metrics(s)
    audited_cues = ma.get("cue_metrics", {})
    if cue_metrics != audited_cues:
        fail(errors, "MCQ_AUDIT_CUE_MISMATCH", "Rendered option metrics differ from MCQ-AUDIT.json")
    noncompetitive = [
        row for row in cue_metrics["per_item_records"]
        if any(flag.startswith(("extreme_short_distractor_", "noncompetitive_phrase_"))
               for flag in row["flags"])
    ]
    if noncompetitive:
        fail(errors, "MCQ_NONCOMPETITIVE_DISTRACTOR", json.dumps(noncompetitive, ensure_ascii=False))
    length_outliers = [
        row for row in cue_metrics["per_item_records"]
        if any(flag in {"correct_length_advantage", "excessive_visible_spread",
                        "terminal_punctuation_mismatch", "initial_letter_case_mismatch"}
               for flag in row["flags"])
    ]
    if length_outliers:
        fail(errors, "MCQ_OPTION_LENGTH_CUE", json.dumps(length_outliers, ensure_ascii=False))
    if (cue_metrics["aggregate_correct_to_distractor_ratio"]
            > MCQ_CUE_POLICY["aggregate_correct_to_distractor_ratio_max"]):
        fail(
            errors,
            "MCQ_OPTION_AGGREGATE_CUE",
            str(cue_metrics["aggregate_correct_to_distractor_ratio"]),
        )
    if cue_metrics["grammar_parallel_review"] != "passed_computed_surface_checks":
        fail(errors, "MCQ_GRAMMAR_PARALLEL_REVIEW", cue_metrics["grammar_parallel_review"])
    checks["mcq_cue_metrics"] = {
        key: value for key, value in cue_metrics.items() if key != "per_item_records"
    }
    checks["mcqs"] = len(q)
    checks["test_matrix_cells"] = len(cells)
    checks["baseline_cells"] = baseline
    checks["matrix_categories"] = expected_categories

    learner_contract_surfaces = {
        name: (root / name).read_text(encoding="utf-8")
        for name in ("README.md", "REVISION-GUIDE.md", "COVERAGE-LEDGER.md",
                     "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md")
    }
    legacy_pattern = re.compile(r"(?:exact(?:ly)?\s+32|16\s*(?:×|x)\s*2|24\s*(?:\+|core plus)\s*8)", re.I)
    for name, text in learner_contract_surfaces.items():
        offending = [
            line for line in text.splitlines()
            if legacy_pattern.search(line) and "historical" not in line.lower()
        ]
        if offending:
            fail(errors, "LEGACY_FIXED_COUNT_CONTRACT", f"{name}: {offending[0]}")

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

    if validate_pdfs:
        from pypdf import PdfReader

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
            package_path = relroot.as_posix()
            status = subprocess.check_output(
                [
                    "git", "-C", str(repo), "status", "--porcelain=v1",
                    "--untracked-files=all", "--", package_path,
                ],
                text=True,
            ).splitlines()
            pending = []
            for line in status:
                if len(line) < 4:
                    continue
                index_state, worktree_state = line[0], line[1]
                if index_state == "?" or worktree_state not in {" ", "!"}:
                    pending.append(line[3:])
            if pending:
                fail(
                    errors,
                    "GIT_PACKAGE_UNSTAGED",
                    json.dumps(sorted(pending), ensure_ascii=False),
                )
            for rel in required_files:
                rp = str((relroot / rel).as_posix())
                tracked = subprocess.run(
                    ["git", "-C", str(repo), "ls-files", "--error-unmatch", "--", rp],
                    text=True,
                    capture_output=True,
                )
                if tracked.returncode != 0:
                    fail(errors, "GIT_REQUIRED_NOT_TRACKED", rp)
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
            checks["git_required_tracked"] = len(required_files)
            checks["git_pending_unstaged_package_files"] = len(pending)
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
    ap.add_argument(
        "--validate-pdfs",
        action="store_true",
        help="Opt in to validating legacy PDF artifacts and PDF-MANIFEST.json.",
    )
    args = ap.parse_args()
    result = run(args.root.resolve(), args.release, args.validate_pdfs)
    if not args.release and not args.check_only:
        (args.root / "VALIDATION.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"].endswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
