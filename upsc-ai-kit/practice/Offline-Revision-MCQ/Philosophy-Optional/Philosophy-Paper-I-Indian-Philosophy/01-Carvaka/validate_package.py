from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import fitz


TOPIC = Path(__file__).resolve().parent
REPO = Path(r"C:\up")
TOOLS = REPO / "tools"
FORMAL_ROOT = Path(
    r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent"
    r"\learning_package_final\Philosophy-Optional"
    r"\Philosophy-Paper-I-—-Indian-Philosophy\01-Carvaka"
)
FORMAL_SOURCES = {
    "session": FORMAL_ROOT / "Learning-Session.md",
    "workbook": FORMAL_ROOT / "Solved-Practice-Workbook.md",
}
CANONICAL = REPO / r"upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Carvaka.md"
PYQ_LEDGERS = (
    REPO / r"upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md",
    REPO / r"upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md",
)
VALIDATION = TOPIC / "VALIDATION.json"
WORD_BANDS = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
EXPECTED_FORMAL_BLOCKS = 436
EXPECTED_SESSION_BLOCKS = 336
EXPECTED_WORKBOOK_BLOCKS = 100
EXPECTED_MCQS = 32
EXPECTED_PANELS = 12
EXPECTED_PRIMARY_PYQS = 9
EXPECTED_SUPPORTING_PYQS = 1
EXPECTED_ORIGINALS = 6
PDF_SOURCES = {
    "Revision-Guide.pdf": "REVISION-GUIDE.md",
    "MCQ-Questions.pdf": "MCQ-QUESTIONS.md",
    "MCQ-Solutions.pdf": "MCQ-SOLUTIONS.md",
    "Answer-Writing-Toolkit.pdf": "ANSWER-WRITING-TOOLKIT.md",
}
PDF_DESCRIPTORS = {
    "Revision-Guide.pdf": "Philosophy Optional · Paper I · Indian Philosophy · Topic 01",
    "MCQ-Questions.pdf": "32-question closed-book bank · no answer key",
    "MCQ-Solutions.pdf": "Option-specific explanations and examiner traps",
    "Answer-Writing-Toolkit.pdf": "Nine owned PYQs, one routed mirror, six original models",
}
REQUIRED = [
    "README.md",
    "REVISION-GUIDE.md",
    "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md",
    "ANSWER-WRITING-TOOLKIT.md",
    "COVERAGE-LEDGER.md",
    "PRACTICE-LOG.md",
    "PREFLIGHT-LEDGER.json",
    "FORMAL-COVERAGE-REVIEW.json",
    "FORMAL-COVERAGE-AUDIT.json",
    "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json",
    "VALIDATION.json",
    "validate_package.py",
    *(f"pdf/{name}" for name in PDF_SOURCES),
]
TEXT_SUFFIXES = {".md", ".json", ".py"}


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.encode("utf-8"))


def normalized_text_bytes(data: bytes) -> bytes:
    text = data.decode("utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def normalize_payload(value: str) -> str:
    return value.replace("\r\n", "\n").replace("\r", "\n").strip("\n")


def word_count(value: str) -> int:
    value = re.sub(r"```.*?```", " ", value, flags=re.S)
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", " ", value)
    return len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", value))


def semantic_plain(value: str) -> str:
    value = re.sub(r"```.*?```", " ", value, flags=re.S)
    value = "\n".join(
        line for line in value.splitlines() if not line.lstrip().startswith("|")
    )
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[*_`>#]", "", value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_proposition_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    return re.sub(r"\s+", " ", value).strip().casefold()


def proposition_inventory_digest(inventory: list[dict]) -> str:
    encoded = json.dumps(
        inventory,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha_bytes(encoded)


def safe_json(path: Path, failures: list[str], code: str) -> dict:
    if not path.is_file():
        failures.append(f"{code}:missing:{path.name}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"{code}:invalid_json:{path.name}:{type(exc).__name__}")
        return {}
    if not isinstance(value, dict):
        failures.append(f"{code}:not_object:{path.name}")
        return {}
    return value


def source_meta(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": str(path), "sha256": sha_bytes(data), "bytes": len(data)}


def slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[*_`[\](){}:;,.!?\"'’“”|/\\]+", " ", value)
    value = re.sub(r"[^0-9A-Za-zĀ-ž]+", "-", value, flags=re.UNICODE)
    return value.strip("-").lower()[:64] or "block"


def parse_formal_blocks(path: Path, source_key: str) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^(#{2,5})\s+(.+?)\s*$", text))
    ordinals: defaultdict[str, int] = defaultdict(int)
    blocks = []
    for index, match in enumerate(matches):
        level = len(match.group(1))
        title = match.group(2).strip()
        ordinals[title] += 1
        next_heading = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        subtree_end = len(text)
        for later in matches[index + 1 :]:
            if len(later.group(1)) <= level:
                subtree_end = later.start()
                break
        body = normalize_payload(text[match.end() : next_heading])
        subtree = normalize_payload(text[match.end() : subtree_end])
        digest = sha_text(normalize_payload(match.group(0) + "\n" + subtree))
        blocks.append(
            {
                "id": f"{source_key}-{slug(title)}-{ordinals[title]:02d}-{digest[:10]}",
                "title": title,
                "level": level,
                "body": body,
                "body_sha256": sha_text(body),
                "subtree_end": subtree_end,
                "start": match.start(),
                "words": word_count(body),
            }
        )
    for block in blocks:
        block["child_ids"] = [
            candidate["id"]
            for candidate in blocks
            if candidate["start"] > block["start"]
            and candidate["start"] < block["subtree_end"]
            and candidate["level"] == block["level"] + 1
        ]
    return blocks


def payload_at_anchor(path: Path, anchor: str) -> str | None:
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(rf'(?m)^<a id="{re.escape(anchor)}"></a>\s*$', text)
    if not match:
        return None
    tail = text[match.end() :]
    heading = re.search(r"(?m)^#{2,5}\s+.+$", tail)
    if not heading:
        return None
    after_heading = tail[heading.end() :]
    following = re.search(r"(?m)^#{2,5}\s+.+$", after_heading)
    payload = after_heading[: following.start()] if following else after_heading
    return normalize_payload(re.sub(r'(?m)^<a id="[^"]+"></a>\s*$', "", payload))


def check_required(failures: list[str], allow_regeneration: bool = False) -> dict:
    rows = []
    for relative in REQUIRED:
        path = TOPIC / relative
        regeneratable = allow_regeneration and relative.startswith("pdf/")
        exists = path.is_file()
        rows.append({"path": relative, "exists": exists, "regeneratable": regeneratable})
        if not exists and not regeneratable:
            failures.append(f"REQUIRED_MISSING:{relative}")
    return {
        "files": rows,
        "pass": all(row["exists"] or row["regeneratable"] for row in rows),
    }


def check_source_integrity(review: dict, preflight: dict, failures: list[str]) -> dict:
    live = {
        "session": source_meta(FORMAL_SOURCES["session"]),
        "workbook": source_meta(FORMAL_SOURCES["workbook"]),
        "canonical": source_meta(CANONICAL),
        "pyq_2018_2025": source_meta(PYQ_LEDGERS[0]),
        "pyq_2026": source_meta(PYQ_LEDGERS[1]),
    }
    expected = preflight.get("source_hashes", {})
    mismatches = []
    for key, row in live.items():
        if expected.get(key, {}).get("sha256") != row["sha256"]:
            mismatches.append(key)
    if mismatches:
        failures.append("SOURCE_HASH_MISMATCH:" + ",".join(mismatches))
    review_sources = {
        **review.get("source_files", {}),
        "canonical": review.get("authority_files", {}).get("canonical", {}),
        "pyq_2018_2025": review.get("authority_files", {}).get("pyq_2018_2025", {}),
        "pyq_2026": review.get("authority_files", {}).get("pyq_2026", {}),
    }
    review_mismatches = [
        key
        for key, row in live.items()
        if review_sources.get(key, {}).get("sha256") != row["sha256"]
    ]
    if review_mismatches:
        failures.append("REVIEW_SOURCE_HASH_MISMATCH:" + ",".join(review_mismatches))
    return {
        "live": live,
        "preflight_mismatches": mismatches,
        "review_mismatches": review_mismatches,
        "pass": not mismatches and not review_mismatches,
    }


def check_formal(review: dict, audit: dict, failures: list[str]) -> dict:
    source_blocks = (
        parse_formal_blocks(FORMAL_SOURCES["session"], "session")
        + parse_formal_blocks(FORMAL_SOURCES["workbook"], "workbook")
    )
    source_by_id = {block["id"]: block for block in source_blocks}
    decisions = review.get("decisions", [])
    decision_by_id = {row.get("id"): row for row in decisions}
    errors = []
    if len(source_blocks) != EXPECTED_FORMAL_BLOCKS:
        errors.append(f"live_block_count:{len(source_blocks)}")
    if len(decisions) != EXPECTED_FORMAL_BLOCKS:
        errors.append(f"review_decision_count:{len(decisions)}")
    if len(decision_by_id) != len(decisions):
        errors.append("duplicate_decision_ids")
    missing = sorted(set(source_by_id) - set(decision_by_id))
    stale = sorted(set(decision_by_id) - set(source_by_id))
    if missing:
        errors.append(f"unreviewed:{len(missing)}")
    if stale:
        errors.append(f"stale:{len(stale)}")
    destination_failures = []
    proposition_failures = []
    proposition_accounting_failures = []
    raw_proposition_records = []
    child_failures = []
    segment_failures = []
    for block_id, source in source_by_id.items():
        decision = decision_by_id.get(block_id)
        if not decision:
            continue
        if decision.get("classification") != "covered_in_scope":
            errors.append(f"classification:{block_id}")
        recorded = decision.get("source", {})
        if recorded.get("direct_parent_body_sha256") != source["body_sha256"]:
            errors.append(f"source_body_hash:{block_id}")
        if recorded.get("source_heading") != source["title"]:
            errors.append(f"source_heading:{block_id}")
        child_union = decision.get("child_union", {})
        if bool(source["child_ids"]) != bool(child_union.get("required")):
            child_failures.append(f"child_required:{block_id}")
        if source["child_ids"] != child_union.get("direct_child_ids", []):
            child_failures.append(f"child_union:{block_id}")
        destination = decision.get("destination", {})
        destination_path = TOPIC / destination.get("file", "")
        payload = payload_at_anchor(destination_path, destination.get("anchor", ""))
        if payload is None:
            destination_failures.append(f"anchor:{block_id}")
            continue
        if sha_text(payload) != destination.get("payload_sha256"):
            destination_failures.append(f"payload:{block_id}")
        mode = destination.get("mapping_mode")
        if mode == "exact_normalized_payload" and sha_text(payload) != source["body_sha256"]:
            destination_failures.append(f"exact:{block_id}")
        if mode == "reviewed_option_rewrite_with_explanation_binding":
            number = re.match(r"MCQ (\d+)\.", source["title"])
            if not number or f"**Coverage cell:** {source['title'].split('. ', 1)[1]}" not in payload:
                destination_failures.append(f"mcq_cell:{block_id}")
        propositions = decision.get("source_specific_semantic_propositions", [])
        if not propositions:
            proposition_failures.append(f"missing:{block_id}")
        for proposition_index, proposition in enumerate(propositions, start=1):
            proposition_text = proposition.get("text")
            normalized_proposition = (
                normalize_proposition_text(proposition_text)
                if isinstance(proposition_text, str)
                else ""
            )
            if not normalized_proposition:
                proposition_accounting_failures.append(
                    f"empty_claim:{block_id}#{proposition_index}"
                )
            normalized_hash = sha_text(normalized_proposition)
            expected_unique_id = f"usp-{normalized_hash[:16]}"
            if proposition.get("normalized_text_sha256") != normalized_hash:
                proposition_accounting_failures.append(
                    f"normalized_hash:{block_id}#{proposition_index}"
                )
            if proposition.get("unique_proposition_id") != expected_unique_id:
                proposition_accounting_failures.append(
                    f"unique_id:{block_id}#{proposition_index}"
                )
            raw_proposition_records.append(
                {
                    "decision_id": block_id,
                    "mapping_index": proposition_index,
                    "mapping_ref": f"{block_id}#{proposition_index}",
                    "normalized_text": normalized_proposition,
                    "normalized_text_sha256": normalized_hash,
                    "unique_proposition_id": expected_unique_id,
                }
            )
            if not proposition.get("source_specific"):
                proposition_failures.append(f"generic:{block_id}")
            if proposition.get("type") == "verbatim_source_sentence":
                text = proposition.get("text", "")
                if text not in semantic_plain(source["body"]):
                    proposition_failures.append(f"not_source:{block_id}")
                if mode == "exact_normalized_payload" and text not in semantic_plain(payload):
                    proposition_failures.append(f"not_destination:{block_id}")
            elif proposition.get("type") == "verbatim_source_payload":
                text = proposition.get("text", "")
                if normalize_payload(text) != source["body"]:
                    proposition_failures.append(f"payload_not_source:{block_id}")
                if mode == "exact_normalized_payload" and normalize_payload(text) != payload:
                    proposition_failures.append(f"payload_not_destination:{block_id}")
            elif proposition.get("type") == "empty_source_heading_label":
                if proposition.get("text") != source["title"] or source["body"]:
                    proposition_failures.append(f"invalid_empty_heading_label:{block_id}")
            else:
                proposition_failures.append(f"unknown_type:{block_id}")
        for segment in decision.get("large_leaf_segments", []):
            start = segment.get("verbatim_start", "")
            end = segment.get("verbatim_end", "")
            compact_source = re.sub(r"\s+", " ", source["body"])
            compact_destination = re.sub(r"\s+", " ", payload)
            if start not in compact_source or end not in compact_source:
                segment_failures.append(f"source:{block_id}:{segment.get('segment')}")
            if mode == "exact_normalized_payload" and (
                start not in compact_destination or end not in compact_destination
            ):
                segment_failures.append(f"destination:{block_id}:{segment.get('segment')}")
    review_hash = sha_text((TOPIC / "FORMAL-COVERAGE-REVIEW.json").read_text(encoding="utf-8"))
    if audit.get("source_review", {}).get("sha256") != review_hash:
        errors.append("audit_review_hash")
    counts = audit.get("counts", {})
    proposition_groups: defaultdict[str, list[dict]] = defaultdict(list)
    for record in raw_proposition_records:
        proposition_groups[record["normalized_text_sha256"]].append(record)
    computed_raw_count = len(raw_proposition_records)
    computed_unique_count = len(proposition_groups)
    computed_duplicate_count = computed_raw_count - computed_unique_count
    accounting = review.get("proposition_accounting", {})
    if accounting.get("raw_mapping_count") != computed_raw_count:
        proposition_accounting_failures.append("raw_count")
    if accounting.get("unique_semantic_count") != computed_unique_count:
        proposition_accounting_failures.append("unique_count")
    if accounting.get("duplicate_occurrence_count") != computed_duplicate_count:
        proposition_accounting_failures.append("duplicate_count")
    if accounting.get("substantive_coverage_count") != computed_unique_count:
        proposition_accounting_failures.append("substantive_coverage_inflation")
    inventory = review.get("unique_semantic_proposition_inventory", [])
    inventory_by_hash = {
        row.get("normalized_text_sha256"): row
        for row in inventory
        if isinstance(row, dict)
    }
    if len(inventory) != computed_unique_count or len(inventory_by_hash) != len(inventory):
        proposition_accounting_failures.append("inventory_count")
    if set(inventory_by_hash) != set(proposition_groups):
        proposition_accounting_failures.append("inventory_hash_set")
    for normalized_hash, records in proposition_groups.items():
        row = inventory_by_hash.get(normalized_hash)
        if not row:
            continue
        expected_id = f"usp-{normalized_hash[:16]}"
        expected_refs = sorted(record["mapping_ref"] for record in records)
        expected_text = records[0]["normalized_text"]
        if row.get("id") != expected_id:
            proposition_accounting_failures.append(f"inventory_id:{expected_id}")
        if row.get("normalized_text") != expected_text:
            proposition_accounting_failures.append(f"inventory_text:{expected_id}")
        if row.get("raw_mapping_count") != len(records):
            proposition_accounting_failures.append(f"inventory_raw_count:{expected_id}")
        if sorted(row.get("mapping_refs", [])) != expected_refs:
            proposition_accounting_failures.append(f"inventory_refs:{expected_id}")
    if accounting.get("inventory_sha256") != proposition_inventory_digest(inventory):
        proposition_accounting_failures.append("inventory_digest")
    duplicate_policy = accounting.get("duplicate_policy", "")
    if "contributes once" not in duplicate_policy or "source-block mapping remains" not in duplicate_policy:
        proposition_accounting_failures.append("duplicate_policy")
    audit_accounting = audit.get("proposition_accounting", {})
    for key, expected in {
        "raw_mapping_count": computed_raw_count,
        "unique_semantic_count": computed_unique_count,
        "duplicate_occurrence_count": computed_duplicate_count,
        "substantive_coverage_count": computed_unique_count,
    }.items():
        if audit_accounting.get(key) != expected:
            proposition_accounting_failures.append(f"audit_{key}")
    published_surfaces = {
        "README.md": semantic_plain((TOPIC / "README.md").read_text(encoding="utf-8")),
        "COVERAGE-LEDGER.md": semantic_plain(
            (TOPIC / "COVERAGE-LEDGER.md").read_text(encoding="utf-8")
        ),
    }
    required_metric_phrases = (
        f"{computed_raw_count} raw proposition mappings",
        f"{computed_unique_count} unique normalized semantic propositions",
        f"{computed_duplicate_count} duplicate occurrences",
    )
    for file_name, published in published_surfaces.items():
        for phrase in required_metric_phrases:
            if phrase.casefold() not in published:
                proposition_accounting_failures.append(
                    f"published_metric:{file_name}:{phrase}"
                )
    expected_counts = {
        "session_blocks": EXPECTED_SESSION_BLOCKS,
        "workbook_blocks": EXPECTED_WORKBOOK_BLOCKS,
        "formal_blocks": EXPECTED_FORMAL_BLOCKS,
        "covered_in_scope": EXPECTED_FORMAL_BLOCKS,
        "unresolved": 0,
        "master_flow_panels": EXPECTED_PANELS,
        "raw_proposition_mappings": computed_raw_count,
        "unique_semantic_propositions": computed_unique_count,
        "duplicate_proposition_occurrences": computed_duplicate_count,
    }
    for key, expected in expected_counts.items():
        if counts.get(key) != expected:
            errors.append(f"audit_count:{key}")
    panels = review.get("panel_parity", {})
    if panels.get("expected") != EXPECTED_PANELS or panels.get("actual") != EXPECTED_PANELS:
        errors.append("panel_parity")
    all_errors = errors + destination_failures + proposition_failures + child_failures + segment_failures
    if all_errors:
        failures.append("FORMAL_DESTINATION:" + all_errors[0])
    if proposition_accounting_failures:
        failures.append("PROPOSITION_ACCOUNTING:" + proposition_accounting_failures[0])
    return {
        "live_block_count": len(source_blocks),
        "decision_count": len(decisions),
        "unreviewed": missing,
        "stale": stale,
        "destination_failures": destination_failures,
        "proposition_failures": proposition_failures,
        "raw_proposition_mapping_count": computed_raw_count,
        "unique_semantic_proposition_count": computed_unique_count,
        "duplicate_proposition_occurrence_count": computed_duplicate_count,
        "proposition_accounting_failures": proposition_accounting_failures,
        "child_union_failures": child_failures,
        "large_leaf_segment_failures": segment_failures,
        "panel_count": panels.get("actual"),
        "errors": errors,
        "pass": not all_errors and not proposition_accounting_failures,
    }


def parse_questions(text: str) -> list[dict]:
    blocks = re.split(r"(?m)(?=^## MCQ \d+$)", text)[1:]
    result = []
    for block in blocks:
        number_match = re.search(r"(?m)^## MCQ (\d+)$", block)
        options = {
            match.group(1): match.group(2).strip()
            for match in re.finditer(r"(?m)^([A-D])\. (.+)$", block)
        }
        result.append(
            {
                "number": int(number_match.group(1)) if number_match else -1,
                "options": options,
                "answer": (
                    re.search(r"(?m)^\*\*Answer: ([A-D])\.\*\*$", block).group(1)
                    if re.search(r"(?m)^\*\*Answer: ([A-D])\.\*\*$", block)
                    else None
                ),
                "explanations": {
                    match.group(1): match.group(2).strip()
                    for match in re.finditer(r"(?m)^- \*\*([A-D]):\*\* (.+)$", block)
                },
                "block": block,
            }
        )
    return result


def longest_run(key: str) -> int:
    best = run = 0
    previous = None
    for letter in key:
        run = run + 1 if letter == previous else 1
        previous = letter
        best = max(best, run)
    return best


def check_mcqs(audit: dict, failures: list[str]) -> dict:
    question_path = TOPIC / "MCQ-QUESTIONS.md"
    solution_path = TOPIC / "MCQ-SOLUTIONS.md"
    if not question_path.is_file() or not solution_path.is_file():
        failures.append("MCQ_SYNC:missing_surface")
        return {
            "question_count": 0,
            "solution_count": 0,
            "errors": ["missing_surface"],
            "pass": False,
        }
    questions_text = question_path.read_text(encoding="utf-8")
    solutions_text = solution_path.read_text(encoding="utf-8")
    questions = parse_questions(questions_text)
    solutions = parse_questions(solutions_text)
    errors = []
    expected_numbers = list(range(1, EXPECTED_MCQS + 1))
    if [row["number"] for row in questions] != expected_numbers:
        errors.append("question_numbering")
    if [row["number"] for row in solutions] != expected_numbers:
        errors.append("solution_numbering")
    if re.search(r"(?m)^\*\*Answer:", questions_text):
        errors.append("answer_leakage")
    key = ""
    correct_lengths, distractor_lengths = [], []
    unique_longest = 0
    correct_longest = 0
    cue_patterns = {
        "semicolon": r";",
        "colon": r":",
        "parentheses": r"[()]",
        "dash": r"[—–]",
        "contrast": r"\b(?:but|however|whereas|although|yet|though|despite)\b",
    }
    cue_counts = {name: {"correct": 0, "distractor": 0} for name in cue_patterns}
    generic_explanations = []
    normalized_explanations = []
    for question, solution in zip(questions, solutions):
        if set(question["options"]) != set("ABCD") or set(solution["options"]) != set("ABCD"):
            errors.append(f"option_count:{question['number']}")
            continue
        if question["options"] != solution["options"]:
            errors.append(f"MCQ_SYNC:options:{question['number']}")
        answer = solution["answer"]
        if answer not in "ABCD":
            errors.append(f"answer:{question['number']}")
            continue
        key += answer
        if set(solution["explanations"]) != set("ABCD"):
            errors.append(f"MCQ_SYNC:explanations:{question['number']}")
        lengths = {letter: word_count(text) for letter, text in question["options"].items()}
        correct_lengths.append(lengths[answer])
        distractor_lengths.extend(length for letter, length in lengths.items() if letter != answer)
        if lengths[answer] == max(lengths.values()):
            correct_longest += 1
        if lengths[answer] > max(length for letter, length in lengths.items() if letter != answer):
            unique_longest += 1
        for letter, text in question["options"].items():
            category = "correct" if letter == answer else "distractor"
            for name, pattern in cue_patterns.items():
                cue_counts[name][category] += bool(re.search(pattern, text, flags=re.I))
        for letter, explanation in solution["explanations"].items():
            if word_count(explanation) < 10:
                generic_explanations.append(f"{question['number']}{letter}:short")
            if not re.match(r"^(?:Correct|Incorrect):", explanation):
                generic_explanations.append(f"{question['number']}{letter}:no_verdict")
            normalized_explanations.append(
                re.sub(r"\s+", " ", explanation.casefold()).strip()
            )
    duplicate_explanations = [
        text for text, count in Counter(normalized_explanations).items() if count > 1
    ]
    if duplicate_explanations:
        generic_explanations.append("duplicate_rationales")
    if audit.get("question_count") != EXPECTED_MCQS:
        errors.append("audit_count")
    if audit.get("randomization", {}).get("answer_key") != key:
        errors.append("audit_key")
    if key == "ABCD" * 8:
        errors.append("fixed_rotation")
    if longest_run(key) > 2:
        errors.append("answer_run")
    correct_longest_rate = correct_longest / EXPECTED_MCQS
    unique_longest_rate = unique_longest / EXPECTED_MCQS
    if correct_longest_rate > 0.50:
        errors.append("correct_longest_rate")
    if unique_longest_rate > 0.35:
        errors.append("unique_longest_rate")
    for name, counts in cue_counts.items():
        if counts["correct"] >= 3 and counts["distractor"] == 0:
            errors.append(f"correct_only_cue:{name}")
    if generic_explanations:
        errors.append("generic_explanations")
    if errors:
        failures.append("MCQ_SYNC:" + errors[0])
    return {
        "question_count": len(questions),
        "solution_count": len(solutions),
        "answer_key": key,
        "distribution": dict(sorted(Counter(key).items())),
        "maximum_identical_run": longest_run(key),
        "correct_longest_rate": round(correct_longest_rate, 4),
        "unique_correct_longest_rate": round(unique_longest_rate, 4),
        "cue_counts": cue_counts,
        "generic_explanation_failures": generic_explanations,
        "errors": errors,
        "pass": not errors,
    }


def extract_timed_answers(text: str) -> list[dict]:
    entries = []
    pattern = re.compile(
        r"(?m)^#### ((?:20\d{2}\s+·\s+Q\d+\([a-z]\)|Original \d+)\s+·\s+"
        r"(10|15|20) marks(?:[^\n]*)?)\s*$"
    )
    matches = list(pattern.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end() : end]
        answer = re.search(
            r"(?ms)^##### (?:Independent model answer|Full independent model answer)\s*$"
            r"(.*?)(?=^\*\*Depth refinement|^##### Why this earns marks)",
            block,
        )
        if not answer:
            continue
        marks = int(match.group(2))
        count = word_count(answer.group(1))
        low, high = WORD_BANDS[marks]
        entries.append(
            {
                "id": match.group(1),
                "marks": marks,
                "words": count,
                "band": [low, high],
                "in_band": low <= count <= high,
            }
        )
    return entries


def check_pyqs(audit: dict, failures: list[str]) -> dict:
    path = TOPIC / "ANSWER-WRITING-TOOLKIT.md"
    if not path.is_file():
        failures.append("PYQ_INTEGRITY:missing_surface")
        return {
            "primary_owned_count": 0,
            "supporting_routed_count": 0,
            "original_count": 0,
            "errors": ["missing_surface"],
            "pass": False,
        }
    text = path.read_text(encoding="utf-8")
    expected = [
        "2018 · Q8(b)",
        "2019 · Q5(c)",
        "2019 · Q6(c)",
        "2020 · Q6(b)",
        "2020 · Q7(c)",
        "2021 · Q5(e)",
        "2024 · Q5(a)",
        "2024 · Q6(a)",
        "2025 · Q5(a)",
    ]
    missing = [item for item in expected if item not in text]
    supporting = "2022 · Q7(c)" in text and "primary owner Nyāya–Vaiśeṣika" in text
    direct_2026_absence = (
        audit.get("year_2026", {}).get("direct_owned_count") == 0
        and "No direct Cārvāka question" in text
    )
    answers = extract_timed_answers(text)
    originals = [row for row in answers if row["id"].startswith("Original")]
    direct = [
        row
        for row in answers
        if row["id"].startswith(("2018", "2019", "2020", "2021", "2024", "2025"))
    ]
    routed = [row for row in answers if row["id"].startswith("2022")]
    errors = []
    if missing:
        errors.append("missing_owned:" + ",".join(missing))
    if len(direct) != EXPECTED_PRIMARY_PYQS:
        errors.append(f"owned_count:{len(direct)}")
    if len(routed) != EXPECTED_SUPPORTING_PYQS or not supporting:
        errors.append("supporting_route")
    if len(originals) != EXPECTED_ORIGINALS:
        errors.append(f"original_count:{len(originals)}")
    if Counter(row["marks"] for row in originals) != Counter({10: 2, 15: 2, 20: 2}):
        errors.append("original_distribution")
    if any(not row["in_band"] for row in answers):
        errors.append("word_band")
    if not direct_2026_absence:
        errors.append("2026_absence")
    if errors:
        failures.append("PYQ_INTEGRITY:" + errors[0])
    return {
        "primary_owned_count": len(direct),
        "supporting_routed_count": len(routed),
        "original_count": len(originals),
        "timed_answers": answers,
        "missing": missing,
        "errors": errors,
        "pass": not errors,
    }


def check_markdown(failures: list[str]) -> dict:
    errors = []
    for path in TOPIC.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "\ufffd" in text:
            errors.append(f"replacement:{path.name}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if re.match(r"^[a-z]+://", target) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f"link:{path.name}:{target}")
    pycache = list(TOPIC.rglob("__pycache__"))
    if pycache:
        errors.extend(f"pycache:{path.relative_to(TOPIC)}" for path in pycache)
    if errors:
        failures.append("TEXT_INTEGRITY:" + errors[0])
    return {"errors": errors, "pass": not errors}


def stamp_pdf(path: Path, source_hash: str) -> None:
    document = fitz.open(path)
    metadata = dict(document.metadata or {})
    metadata["keywords"] = f"source-sha256={source_hash}"
    temporary = path.with_suffix(".stamped.pdf")
    document.set_metadata(metadata)
    document.save(temporary, garbage=4, deflate=True)
    document.close()
    os.replace(temporary, path)


def regenerate_pdfs() -> dict:
    sys.path.insert(0, str(TOOLS))
    from unicode_markdown_pdf import build_pdf

    output = {}
    for pdf_name, source_name in PDF_SOURCES.items():
        source = TOPIC / source_name
        target = TOPIC / "pdf" / pdf_name
        build_pdf(
            source,
            target,
            internal_index=True,
            index_title="CONTENTS",
            cover_descriptor=PDF_DESCRIPTORS[pdf_name],
            footer_label="Cārvāka",
        )
        source_hash = sha_bytes(normalized_text_bytes(source.read_bytes()))
        stamp_pdf(target, source_hash)
        output[pdf_name] = {"source": source_name, "source_sha256": source_hash}
    return output


def check_pdfs(failures: list[str]) -> dict:
    rows = {}
    errors = []
    for pdf_name, source_name in PDF_SOURCES.items():
        source = TOPIC / source_name
        pdf = TOPIC / "pdf" / pdf_name
        row = {
            "source": source_name,
            "source_exists": source.is_file(),
            "exists": pdf.is_file(),
        }
        if not source.is_file():
            errors.append(f"missing_source:{source_name}")
            rows[pdf_name] = row
            continue
        if not pdf.is_file():
            errors.append(f"missing:{pdf_name}")
            rows[pdf_name] = row
            continue
        source_hash = sha_bytes(normalized_text_bytes(source.read_bytes()))
        document = fitz.open(pdf)
        page_text = [page.get_text() for page in document]
        blank_pages = [index + 1 for index, text in enumerate(page_text) if len(text.strip()) < 20]
        replacement_pages = [
            index + 1 for index, text in enumerate(page_text) if "\ufffd" in text
        ]
        out_of_bounds = []
        for index, page in enumerate(document):
            rect = page.rect
            for block in page.get_text("blocks"):
                x0, y0, x1, y1 = block[:4]
                if x0 < -1 or y0 < -1 or x1 > rect.width + 1 or y1 > rect.height + 1:
                    out_of_bounds.append(index + 1)
                    break
        stamped = (document.metadata or {}).get("keywords", "")
        document.close()
        stale = stamped != f"source-sha256={source_hash}"
        if blank_pages:
            errors.append(f"blank:{pdf_name}")
        if replacement_pages:
            errors.append(f"replacement:{pdf_name}")
        if out_of_bounds:
            errors.append(f"bounds:{pdf_name}")
        if stale:
            errors.append(f"PDF_STALE:{pdf_name}")
        row.update(
            {
                "pages": len(page_text),
                "sha256": sha_bytes(pdf.read_bytes()),
                "source_sha256": source_hash,
                "stamped_source_sha256": stamped.removeprefix("source-sha256="),
                "blank_pages": blank_pages,
                "replacement_pages": replacement_pages,
                "out_of_bounds_pages": out_of_bounds,
                "stale": stale,
            }
        )
        rows[pdf_name] = row
    if errors:
        failures.append("PDF_INTEGRITY:" + errors[0])
    return {"files": rows, "errors": errors, "pass": not errors}


def git_path(relative: str) -> str:
    return (TOPIC / relative).relative_to(REPO).as_posix()


def git_run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(REPO), *args],
        capture_output=True,
        check=False,
    )


def check_release_integrity(failures: list[str], enforce: bool) -> dict:
    try:
        TOPIC.relative_to(REPO)
    except ValueError:
        if enforce:
            failures.append("RELEASE_NOT_STAGED:package_outside_repository")
        return {
            "required_count": len(REQUIRED),
            "included_count": 0,
            "missing_or_stale": list(REQUIRED),
            "pass": False,
            "enforced": enforce,
            "skipped_for_copied_package": True,
            "normalization": "Not evaluated for a copied-package development validation.",
        }
    rows = []
    missing = []
    for relative in REQUIRED:
        path = TOPIC / relative
        repository_path = git_path(relative)
        staged_result = git_run("show", f":{repository_path}")
        staged = staged_result.returncode == 0
        identical = False
        if staged and path.is_file():
            working = path.read_bytes()
            indexed = staged_result.stdout
            if path.suffix.lower() in TEXT_SUFFIXES:
                try:
                    identical = normalized_text_bytes(working) == normalized_text_bytes(indexed)
                except UnicodeDecodeError:
                    identical = False
            else:
                identical = working == indexed
        included = path.is_file() and staged and identical
        rows.append(
            {
                "path": relative,
                "staged": staged,
                "git_normalized_identity": identical,
                "release_included": included,
            }
        )
        if not included:
            missing.append(relative)
    if enforce and missing:
        failures.append("RELEASE_NOT_STAGED:" + missing[0])
    return {
        "required_count": len(REQUIRED),
        "included_count": len(REQUIRED) - len(missing),
        "missing_or_stale": missing,
        "pass": not missing,
        "enforced": enforce,
        "normalization": "UTF-8 text compares LF-normalized index/worktree bytes; PDFs compare exact bytes.",
    }


def run_child(package: Path) -> tuple[int, str]:
    process = subprocess.run(
        [
            sys.executable,
            "-B",
            str(package / "validate_package.py"),
            "--internal-negative",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return process.returncode, process.stdout + process.stderr


def corrupt_proposition_accounting(package: Path) -> None:
    path = package / "FORMAL-COVERAGE-REVIEW.json"
    review = json.loads(path.read_text(encoding="utf-8"))
    review["proposition_accounting"]["raw_mapping_count"] += 1
    path.write_text(
        json.dumps(review, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def run_negative_tests() -> dict:
    cases = []
    with tempfile.TemporaryDirectory(prefix="carvaka-validator-") as temporary:
        root = Path(temporary)
        base = root / "base"
        shutil.copytree(TOPIC, base, ignore=shutil.ignore_patterns("__pycache__"))
        mutations = [
            (
                "missing_required_file",
                "REQUIRED_MISSING",
                lambda package: (package / "MCQ-SOLUTIONS.md").unlink(),
            ),
            (
                "question_solution_divergence",
                "MCQ_SYNC",
                lambda package: (package / "MCQ-QUESTIONS.md").write_text(
                    (package / "MCQ-QUESTIONS.md")
                    .read_text(encoding="utf-8")
                    .replace("A. 2 and 3 only", "A. 1 and 2 only", 1),
                    encoding="utf-8",
                    newline="\n",
                ),
            ),
            (
                "formal_destination_mutation",
                "FORMAL_DESTINATION",
                lambda package: (package / "REVISION-GUIDE.md").write_text(
                    (package / "REVISION-GUIDE.md")
                    .read_text(encoding="utf-8")
                    .replace(
                        "Contemporary labels such as empiricism, naturalism, secularism or dissent",
                        "Contemporary labels such as empiricism, mutation, secularism or dissent",
                        1,
                    ),
                    encoding="utf-8",
                    newline="\n",
                ),
            ),
            (
                "stale_pdf_after_markdown_change",
                "PDF_STALE",
                lambda package: (package / "MCQ-QUESTIONS.md").write_text(
                    (package / "MCQ-QUESTIONS.md").read_text(encoding="utf-8")
                    + "\n<!-- stale mutation -->\n",
                    encoding="utf-8",
                    newline="\n",
                ),
            ),
            (
                "missing_validation_no_crash",
                "REQUIRED_MISSING",
                lambda package: (package / "VALIDATION.json").unlink(),
            ),
            (
                "corrupt_raw_unique_proposition_accounting",
                "PROPOSITION_ACCOUNTING:raw_count",
                corrupt_proposition_accounting,
            ),
        ]
        for name, expected, mutate in mutations:
            package = root / name
            shutil.copytree(base, package)
            mutate(package)
            code, output = run_child(package)
            cases.append(
                {
                    "name": name,
                    "expected_code": expected,
                    "exit_code": code,
                    "expected_code_observed": expected in output,
                    "rejected": code != 0,
                    "pass": code != 0 and expected in output,
                }
            )
    return {"cases": cases, "pass": all(case["pass"] for case in cases)}


def validate(args: argparse.Namespace) -> tuple[dict, int]:
    failures: list[str] = []
    required = check_required(failures, allow_regeneration=args.regenerate)
    review = safe_json(TOPIC / "FORMAL-COVERAGE-REVIEW.json", failures, "FORMAL_REVIEW")
    audit = safe_json(TOPIC / "FORMAL-COVERAGE-AUDIT.json", failures, "FORMAL_AUDIT")
    preflight = safe_json(TOPIC / "PREFLIGHT-LEDGER.json", failures, "PREFLIGHT")
    mcq_audit = safe_json(TOPIC / "MCQ-AUDIT.json", failures, "MCQ_AUDIT")
    pyq_audit = safe_json(TOPIC / "PYQ-DEMAND-AUDIT.json", failures, "PYQ_AUDIT")
    source_integrity = check_source_integrity(review, preflight, failures)
    formal = check_formal(review, audit, failures)
    mcqs = check_mcqs(mcq_audit, failures)
    pyqs = check_pyqs(pyq_audit, failures)
    markdown = check_markdown(failures)
    regeneration = regenerate_pdfs() if args.regenerate and not failures else {}
    pdfs = check_pdfs(failures)
    release = check_release_integrity(failures, args.mode == "release")
    negative = (
        {"skipped": True, "pass": True}
        if args.internal_negative
        else run_negative_tests()
    )
    if not negative.get("pass"):
        failures.append("NEGATIVE_TESTS")
    result = (
        "FAIL"
        if failures
        else ("RELEASE_PASS" if args.mode == "release" else "DEVELOPMENT_PASS")
    )
    payload = {
        "schema_version": 1,
        "topic": "01 Cārvāka",
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "validation_mode": args.mode,
        "result": result,
        "release_ready": release["pass"],
        "result_gate": (
            "DEVELOPMENT_PASS validates current package content and generated artifacts. "
            "RELEASE_PASS is non-mutating and additionally requires every required artifact "
            "to have Git-normalized identity with its staged index blob."
        ),
        "counts": {
            "formal_blocks": formal.get("live_block_count", 0),
            "raw_proposition_mappings": formal.get(
                "raw_proposition_mapping_count", 0
            ),
            "unique_semantic_propositions": formal.get(
                "unique_semantic_proposition_count", 0
            ),
            "duplicate_proposition_occurrences": formal.get(
                "duplicate_proposition_occurrence_count", 0
            ),
            "mcqs": mcqs.get("question_count", 0),
            "primary_owned_pyqs": pyqs.get("primary_owned_count", 0),
            "supporting_routed_pyqs": pyqs.get("supporting_routed_count", 0),
            "original_models": pyqs.get("original_count", 0),
        },
        "checks": {
            "required_files": required,
            "source_integrity": source_integrity,
            "formal_coverage": formal,
            "mcq_integrity": mcqs,
            "pyq_integrity": pyqs,
            "markdown_integrity": markdown,
            "pdf_generation": regeneration,
            "pdf_integrity": pdfs,
            "copied_package_full_entry_negative_tests": negative,
            "release_integrity": release,
        },
        "failures": failures,
        "mechanical_limits": (
            "The validator proves enumerated source identity, exact or reviewed destination "
            "binding, hierarchy and panel parity, MCQ/PYQ structure, visible cue metrics, "
            "word bands, PDF mechanics and staged-file identity. It does not substitute for "
            "philosophical judgement or an examiner's evaluation."
        ),
    }
    return payload, 0 if result in {"DEVELOPMENT_PASS", "RELEASE_PASS"} else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--regenerate", action="store_true")
    parser.add_argument("--mode", choices=("development", "release"), default="development")
    parser.add_argument("--internal-negative", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.mode == "development" and not args.internal_negative:
        VALIDATION.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "topic": "01 Cārvāka",
                    "result": "VALIDATION_IN_PROGRESS",
                    "release_ready": False,
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
    payload, code = validate(args)
    if args.mode == "development" and not args.internal_negative:
        VALIDATION.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    pages = payload["checks"]["pdf_integrity"].get("files", {})
    page_summary = ",".join(
        f"{name}:{row.get('pages', 0)}" for name, row in pages.items()
    )
    print(
        f"{payload['result']}: formal={payload['counts']['formal_blocks']} "
        f"mcqs={payload['counts']['mcqs']} pyqs={payload['counts']['primary_owned_pyqs']} "
        f"supporting={payload['counts']['supporting_routed_pyqs']} "
        f"originals={payload['counts']['original_models']} "
        f"pdfs={page_summary} "
        f"release_ready={payload['release_ready']}"
    )
    if payload["failures"]:
        print("Failures:")
        for failure in payload["failures"]:
            print(f"- {failure}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
