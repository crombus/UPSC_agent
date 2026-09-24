from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
IST = timezone(timedelta(hours=5, minutes=30))
REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md", "COVERAGE-LEDGER.md",
    "FORMAL-SOURCE-MIRROR.md", "FORMAL-COVERAGE-REVIEW.json",
    "FORMAL-COVERAGE-AUDIT.json", "MCQ-AUDIT.json", "PYQ-DEMAND-AUDIT.json",
    "TEST-MATRIX.json", "SOURCE-ARTIFACT-AUDIT.json",
    "VALIDATION.json", "build_package.py", "render_pdfs.py",
    "validate_package.py", "run_negative_tests.py", ".gitattributes",
]
SOURCE_ARTIFACTS = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md", "COVERAGE-LEDGER.md",
    "FORMAL-SOURCE-MIRROR.md", "FORMAL-COVERAGE-REVIEW.json",
    "FORMAL-COVERAGE-AUDIT.json", "MCQ-AUDIT.json", "PYQ-DEMAND-AUDIT.json",
    "TEST-MATRIX.json", "build_package.py", "render_pdfs.py",
    "validate_package.py", "run_negative_tests.py", ".gitattributes",
]
PDF_REQUIRED = [
    "PDF-MANIFEST.json",
    "pdf/Nyaya-Vaisesika-Revision-Guide.pdf",
    "pdf/Nyaya-Vaisesika-MCQ-Questions.pdf",
    "pdf/Nyaya-Vaisesika-MCQ-Solutions.pdf",
    "pdf/Nyaya-Vaisesika-Answer-Writing-Toolkit.pdf",
]
EXPECTED_HASHES = {
    "formal_session": "dcb90b36fa7751b381176eb8fe61c22fc066033c72cdad21d27e27099630b12c",
    "formal_workbook": "68851473752eee993413d76727ed170d806c5cd943ebec9129342ef0ec10b412",
    "canonical": "8a2c28afbbdff202af26df5c0a2f7cb4453945b0f2691dc37b4cc76f42d8fffa",
    "pyq_2018_2025": "c7b556c7b4b750943b7b5f0ac94273664a46c6c75f1c444ae2d953fd77d34eec",
    "pyq_2026": "1e3b86dbf301bf929851ecc39f1b8585485707cd19fc7a2168861bbb142a8806",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha(text: str) -> str:
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()


def fail(errors: list[dict], code: str, detail: str) -> None:
    errors.append({"code": code, "detail": detail})


def classify_semantic_unit(unit: str) -> str | None:
    compact = re.sub(r"\s+", " ", unit.strip())
    plain = re.sub(r"[*_`>#]", "", compact).strip()
    if re.match(r"^[A-D]\.\s+", plain):
        return "mcq_option_coordinate"
    if re.match(r"^-\s*[A-D]:\s+", plain):
        return "option_explanation_coordinate"
    if re.fullmatch(r"Answer:\s*[A-D]\.?", plain, re.I):
        return "answer_key_coordinate"
    if re.fullmatch(r"(?:\d+\s*(?:(?:,|and)\s*\d+\s*)+(?:only)?|\d+\s+only)", plain, re.I):
        return "bare_numeric_combination"
    if re.fullmatch(
        r"(?:option explanations?|examiner traps?|demand decoded|why this earns marks|"
        r"model answer(?:\s*\([^)]*\))?|answer placement|core diagnostics|remedial drills)"
        r"[\s:.\-–—]*",
        plain,
        re.I,
    ):
        return "isolated_structural_label"
    if len(re.sub(r"[\W_]+", "", plain, flags=re.UNICODE)) < 3:
        return "nonsemantic_symbol_fragment"
    return None


def semantic_units(payload: str) -> tuple[list[str], list[dict]]:
    lines = payload.strip().splitlines()
    if lines and re.match(r"^#{2,5}\s+", lines[0]):
        lines = lines[1:]
    units, current, mode = [], [], None

    def flush() -> None:
        nonlocal current, mode
        value = "\n".join(current).strip()
        if value:
            units.append(value)
        current, mode = [], None

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if mode == "code":
                current.append(line)
                flush()
            else:
                flush()
                mode, current = "code", [line]
            continue
        if mode == "code":
            current.append(line)
            continue
        if stripped.startswith("|"):
            if mode not in (None, "table"):
                flush()
            mode = "table"
            current.append(line)
            continue
        if mode == "table" and not stripped.startswith("|"):
            flush()
        if not stripped:
            flush()
            continue
        if re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line):
            flush()
            units.append(line.strip())
            continue
        if mode not in (None, "paragraph"):
            flush()
        mode = "paragraph"
        current.append(line)
    flush()
    meaningful, excluded = [], []
    for source_ordinal, unit in enumerate(units, 1):
        reason = classify_semantic_unit(unit)
        if reason:
            excluded.append({
                "source_ordinal": source_ordinal,
                "reason": reason,
                "exact_payload_sha256": text_sha(unit),
                "exact_payload": unit,
            })
        else:
            meaningful.append(unit)
    return meaningful, excluded


def anchor_payload(text: str, anchor: str) -> str | None:
    token = f'<a id="{anchor}"></a>'
    start = text.find(token)
    if start < 0:
        return None
    start = text.find("\n", start) + 1
    next_anchor = text.find("\n<a id=", start)
    end = len(text) if next_anchor < 0 else next_anchor
    return text[start:end].strip() + "\n"


def parse_mcqs(text: str) -> dict[int, dict]:
    output = {}
    for chunk in re.split(r"(?=^## MCQ \d+\.)", text, flags=re.M):
        head = re.match(r"## MCQ (\d+)\.\s*(.+)\n", chunk)
        if not head:
            continue
        options = {}
        for match in re.finditer(
            r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:|\n<a id=|\n## |\Z)",
            chunk, re.M | re.S,
        ):
            options[match.group(1)] = re.sub(r"\s+", " ", match.group(2).strip())
        answer = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
        stem = chunk[head.end():]
        option_start = re.search(r"^[A-D]\.\s+", stem, re.M)
        stem = stem[:option_start.start()].strip() if option_start else stem.strip()
        explanations = {
            match.group(1): match.group(2).strip()
            for match in re.finditer(r"^- \*\*([A-D]):\*\*\s*(.+)$", chunk, re.M)
        }
        trap = re.search(r"\*\*Examiner trap:\*\*\s*(.+)", chunk)
        output[int(head.group(1))] = {
            "title": head.group(2).strip(), "stem": stem,
            "options": options, "answer": answer.group(1) if answer else None,
            "explanations": explanations, "trap": trap.group(1).strip() if trap else "",
        }
    return output


def predictable_cycle(sequence: str) -> bool:
    for period in range(2, 5):
        for start in range(len(sequence) - period * 3 + 1):
            unit = sequence[start:start + period]
            if len(set(unit)) > 1 and sequence[start:start + period * 3] == unit * 3:
                return True
    return False


def legacy_fixed_contract(value, path: str = "") -> list[str]:
    hits = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else key
            if key in {
                "fixed_question_count", "source_core", "source_remedial",
                "balanced_exactly", "answers_per_letter", "legacy_matrix_contract",
            }:
                hits.append(child_path)
            hits.extend(legacy_fixed_contract(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits.extend(legacy_fixed_contract(child, f"{path}[{index}]"))
    elif isinstance(value, str) and re.search(
        r"\bbank is 32\b|\b24 core (?:plus|\+) 8 remedial\b|\bexactly 8 (?:answers )?per letter\b|\bsixteen-cell matrix\b",
        value, re.I,
    ):
        hits.append(path)
    return hits


def validate(root: Path, release: bool, validate_pdfs: bool = False) -> dict:
    errors, checks = [], {}
    required = REQUIRED + (PDF_REQUIRED if validate_pdfs else [])
    for rel in required:
        if rel == "VALIDATION.json" and not release and not (root / rel).exists():
            continue
        if not (root / rel).is_file():
            fail(errors, "MISSING_REQUIRED_FILE", rel)
    checks["required_files"] = len(required)
    checks["pdf_validation"] = "enabled" if validate_pdfs else "not_requested"
    if errors:
        return report(release, checks, errors)

    source_artifact_audit = json.loads((root / "SOURCE-ARTIFACT-AUDIT.json").read_text(encoding="utf-8"))
    artifact_rows = source_artifact_audit.get("artifacts", [])
    artifact_map = {row.get("file"): row for row in artifact_rows}
    if (
        source_artifact_audit.get("policy")
        != "markdown_and_machine_readable_audits_are_canonical_pdfs_optional"
        or source_artifact_audit.get("status") != "CANONICAL_SOURCE_ARTIFACTS_CURRENT"
        or len(artifact_map) != len(artifact_rows)
        or set(artifact_map) != set(SOURCE_ARTIFACTS)
    ):
        fail(errors, "SOURCE_ARTIFACT_AUDIT_SCHEMA", "Canonical source-artifact inventory differs")
    for rel in SOURCE_ARTIFACTS:
        row = artifact_map.get(rel)
        path = root / rel
        if not row or row.get("sha256") != sha(path) or row.get("bytes") != path.stat().st_size:
            fail(errors, "SOURCE_ARTIFACT_STALE", rel)
    checks["canonical_source_artifacts"] = len(SOURCE_ARTIFACTS)

    review = json.loads((root / "FORMAL-COVERAGE-REVIEW.json").read_text(encoding="utf-8"))
    audit = json.loads((root / "FORMAL-COVERAGE-AUDIT.json").read_text(encoding="utf-8"))
    source_texts = {}
    for key, expected in EXPECTED_HASHES.items():
        source = review.get("sources", {}).get(key, {})
        path = Path(source.get("path", ""))
        if source.get("sha256", "").lower() != expected:
            fail(errors, "SOURCE_HASH_MISMATCH", f"{key}: declared hash")
        if not path.is_file():
            fail(errors, "SOURCE_FILE_MISSING", f"{key}: {path}")
            continue
        if sha(path) != expected:
            fail(errors, "SOURCE_HASH_MISMATCH", f"{key}: authoritative file")
        source_texts[key] = path.read_text(encoding="utf-8").replace("\r\n", "\n")

    decisions = review.get("decisions", [])
    if review.get("decision_count") != len(decisions) or review.get("unclassified_count") != 0:
        fail(errors, "FORMAL_MAPPING_COUNT", "Decision or unclassified count differs")
    by_id = {row.get("id"): row for row in decisions}
    if len(by_id) != len(decisions):
        fail(errors, "FORMAL_BLOCK_ID_DUPLICATE", "Block IDs are not unique")
    mirror = (root / "FORMAL-SOURCE-MIRROR.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    flattened, unique_seen, excluded_seen = [], {}, []
    for row in decisions:
        source_key = "formal_session" if row.get("source") == "session" else "formal_workbook"
        lines = source_texts.get(source_key, "").splitlines()
        start, end = row.get("line_start", 0), row.get("line_end", 0)
        if not 1 <= start <= end <= len(lines):
            fail(errors, "SOURCE_BLOCK_RANGE_INVALID", row.get("id", "unknown"))
            continue
        payload = "\n".join(lines[start - 1:end]).strip() + "\n"
        if text_sha(payload) != row.get("own_payload_sha256") or len(payload) != row.get("own_chars"):
            fail(errors, "SOURCE_BLOCK_PAYLOAD_MISMATCH", row.get("id", "unknown"))
        destination = row.get("destination", {})
        mirrored = anchor_payload(mirror, destination.get("anchor", ""))
        if mirrored is None:
            fail(errors, "DESTINATION_ANCHOR_MISSING", row.get("id", "unknown"))
        elif text_sha(mirrored) != destination.get("payload_sha256") or text_sha(mirrored) != text_sha(payload):
            fail(errors, "DESTINATION_PAYLOAD_HASH_MISMATCH", row.get("id", "unknown"))
        actual_units, actual_exclusions = semantic_units(payload)
        mappings = row.get("proposition_mappings", [])
        recorded_exclusions = row.get("excluded_non_propositional_fragments", [])
        excluded_payloads = {item["exact_payload"] for item in actual_exclusions}
        for mapping in mappings:
            if mapping.get("exact_payload") in excluded_payloads or classify_semantic_unit(mapping.get("exact_payload", "")):
                fail(errors, "NON_PROPOSITION_FRAGMENT_INCLUDED", row.get("id", "unknown"))
        if len(actual_units) != len(mappings):
            fail(errors, "SEMANTIC_PROPOSITION_COUNT", row.get("id", "unknown"))
        expected_exclusions = [
            {"source_block_id": row.get("id"), **item}
            for item in actual_exclusions
        ]
        if recorded_exclusions != expected_exclusions:
            fail(errors, "EXCLUDED_FRAGMENT_ACCOUNTING_TAMPER", row.get("id", "unknown"))
        excluded_seen.extend(recorded_exclusions)
        for number, (unit, mapping) in enumerate(zip(actual_units, mappings), 1):
            prop_id = "prop-" + text_sha(normalized(unit))[:20]
            if (
                mapping.get("occurrence") != number
                or mapping.get("source_block_id") != row.get("id")
                or mapping.get("exact_payload") != unit
                or mapping.get("exact_payload_sha256") != text_sha(unit)
                or mapping.get("proposition_id") != prop_id
            ):
                fail(errors, "SEMANTIC_PROPOSITION_REFERENCE_TAMPER", f"{row.get('id')}:{number}")
            flattened.append(mapping)
            unique_seen.setdefault(prop_id, unit)
        if row.get("semantic_basis") != "deterministically_filtered_exact_source_owned_independently_meaningful_payload":
            fail(errors, "SEMANTIC_PROPOSITION_QUALITY", row.get("id", "unknown"))
        if row.get("structural_parent_only") != (not mappings and bool(row.get("direct_children"))):
            fail(errors, "PARENT_ONLY_CLASSIFICATION", row.get("id", "unknown"))
        segments = row.get("large_leaf_segments", [])
        if len(payload) > 2400 and not segments:
            fail(errors, "LARGE_LEAF_UNSEGMENTED", row.get("id", "unknown"))
        if segments:
            chunks = []
            for segment in segments:
                first, last = segment.get("start_char"), segment.get("end_char_exclusive")
                if not isinstance(first, int) or not isinstance(last, int) or not 0 <= first < last <= len(payload):
                    fail(errors, "LARGE_LEAF_SEGMENT_RANGE", row.get("id", "unknown"))
                    continue
                chunk = payload[first:last]
                chunks.append(chunk)
                if text_sha(chunk) != segment.get("payload_sha256") or len(chunk) != segment.get("chars"):
                    fail(errors, "LARGE_LEAF_SEGMENT_HASH", f"{row.get('id')}:{segment.get('index')}")
            if "".join(chunks) != payload:
                fail(errors, "LARGE_LEAF_SEGMENT_UNION", row.get("id", "unknown"))
        child_hashes = []
        for child in row.get("direct_children", []):
            if child not in by_id:
                fail(errors, "CHILD_ID_MISSING", f"{row.get('id')}->{child}")
            else:
                child_hashes.append(by_id[child].get("own_payload_sha256", ""))
        if text_sha("\n".join(child_hashes)) != row.get("child_union_sha256"):
            fail(errors, "CHILD_UNION_MISMATCH", row.get("id", "unknown"))

    registry = review.get("proposition_registry", [])
    registry_map = {row.get("id"): row for row in registry}
    if len(registry_map) != len(registry):
        fail(errors, "SEMANTIC_REGISTRY_DUPLICATE_ID", "Registry IDs are not unique")
    for prop_id, unit in unique_seen.items():
        row = registry_map.get(prop_id)
        if not row:
            fail(errors, "SEMANTIC_REGISTRY_MISSING", prop_id)
        elif (
            row.get("normalized_sha256") != text_sha(normalized(unit))
            or row.get("representative_exact_payload") != unit
            or row.get("exact_payload_sha256") != text_sha(unit)
        ):
            fail(errors, "SEMANTIC_REGISTRY_TAMPER", prop_id)
    raw_count, unique_count = len(flattened), len(unique_seen)
    if review.get("raw_proposition_mapping_count") != raw_count:
        fail(errors, "RAW_PROPOSITION_COUNT", str(raw_count))
    if review.get("unique_normalized_proposition_count") != unique_count:
        fail(errors, "UNIQUE_PROPOSITION_COUNT", str(unique_count))
    if review.get("duplicate_occurrences_deduplicated") != raw_count - unique_count:
        fail(errors, "PROPOSITION_DEDUP_COUNT", str(raw_count - unique_count))
    reason_counts = {
        reason: sum(row.get("reason") == reason for row in excluded_seen)
        for reason in sorted({row.get("reason") for row in excluded_seen})
    }
    if review.get("excluded_fragment_count") != len(excluded_seen):
        fail(errors, "EXCLUDED_FRAGMENT_COUNT", str(len(excluded_seen)))
    if review.get("excluded_fragment_reason_counts") != reason_counts:
        fail(errors, "EXCLUDED_FRAGMENT_REASON_COUNTS", json.dumps(reason_counts, sort_keys=True))
    panels = [row for row in decisions if "ASCII MASTER FLOW — PANEL" in row.get("heading", "")]
    parity = review.get("panel_parity", {})
    if parity.get("expected") != 15 or parity.get("actual") != 15 or len(panels) != 15:
        fail(errors, "PANEL_PARITY_MISMATCH", f"found {len(panels)}")
    if audit.get("review_sha256") != sha(root / "FORMAL-COVERAGE-REVIEW.json"):
        fail(errors, "DERIVED_AUDIT_STALE", "Review hash changed")
    for key, value in {
        "decision_count": len(decisions), "raw_proposition_mapping_count": raw_count,
        "unique_normalized_proposition_count": unique_count,
        "duplicate_occurrences_deduplicated": raw_count - unique_count,
        "excluded_fragment_count": len(excluded_seen),
        "excluded_fragment_reason_counts": reason_counts,
        "parent_blocks": sum(bool(row.get("direct_children")) for row in decisions),
        "large_leaf_segmented": sum(bool(row.get("large_leaf_segments")) for row in decisions),
    }.items():
        if audit.get(key) != value:
            fail(errors, "DERIVED_AUDIT_COUNT", f"{key}: {audit.get(key)} != {value}")
    checks.update({
        "formal_blocks": len(decisions), "raw_proposition_mappings": raw_count,
        "unique_normalized_propositions": unique_count,
        "duplicates_deduplicated": raw_count - unique_count,
        "excluded_fragments": len(excluded_seen),
        "excluded_fragment_reasons": reason_counts,
        "panels": len(panels),
    })

    revision = (root / "REVISION-GUIDE.md").read_text(encoding="utf-8")
    toolkit = (root / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    positive = [
        "Nyāya accepts four pramāṇas", "classical Vaiśeṣika accepts perception and inference",
        "public epistemic/didactic demonstration", "vyāpti", "upādhi",
        "ordinary and extraordinary", "sentence cognition", "five marks of a valid reason",
        "adventitious qualities", "cognition-producing qualities", "seven categories",
        "Inherence is irreducible to conjunction", "asatkāryavāda/ārambhavāda", "Atomism",
        "not a bare correspondence slogan",
    ]
    for phrase in positive:
        if phrase.casefold() not in revision.casefold():
            fail(errors, "DOCTRINAL_PRECISION_MISSING", phrase)
    forbidden = [
        r"Nyāya (?:accepts|has) (?:only )?two pramāṇas",
        r"Vaiśeṣika (?:accepts|has) four pramāṇas",
        r"Nyāya(?:'s)? five-member(?:ed)? (?:demonstration|syllogism) is (?:the )?(?:same as|equivalent to) (?:the )?Aristotelian syllogism",
        r"Nyāya liberation is (?:an experience of )?(?:conscious )?bliss",
        r"the liberated Nyāya self (?:experiences|enjoys|retains) (?:consciousness|bliss)",
        r"truth is merely correspondence",
        r"samavāya is (?:a )?conjunction",
        r"Nyāya(?:–Vaiśeṣika)? holds that the effect pre-exists in (?:its|the) cause",
    ]
    for pattern in forbidden:
        if re.search(pattern, revision, re.I):
            fail(errors, "DOCTRINAL_PRECISION_VIOLATION", pattern)
    checks["doctrinal_guards"] = len(positive)

    questions = parse_mcqs((root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8"))
    solutions = parse_mcqs((root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"))
    mcq_audit = json.loads((root / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    matrix = json.loads((root / "TEST-MATRIX.json").read_text(encoding="utf-8"))
    question_headings = [int(number) for number in re.findall(r"^## MCQ (\d+)\.", (root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8"), re.M)]
    solution_headings = [int(number) for number in re.findall(r"^## MCQ (\d+)\.", (root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"), re.M)]
    if len(question_headings) != len(set(question_headings)) or len(solution_headings) != len(set(solution_headings)):
        fail(errors, "MCQ_DUPLICATE_QUESTION_ID", f"questions={question_headings}; solutions={solution_headings}")
    question_ids = sorted(questions)
    if question_ids != list(range(1, max(question_ids, default=0) + 1)) or sorted(solutions) != question_ids:
        fail(errors, "MCQ_COUNT_MISMATCH", f"{len(questions)}/{len(solutions)}")
    cells = matrix.get("cells", [])
    cell_ids = [cell.get("cell_id") for cell in cells]
    if len(cells) != 59 or len(set(cell_ids)) != len(cells) or any(not re.fullmatch(r"NV-TM-\d{3}", value or "") for value in cell_ids):
        fail(errors, "MCQ_TEST_MATRIX_SCHEMA", f"cells={len(cells)} unique={len(set(cell_ids))}")
    baseline = {status: sum(cell.get("baseline_status") == status for cell in cells) for status in ("adequate", "partial", "untested")}
    if baseline != {"adequate": 25, "partial": 30, "untested": 4}:
        fail(errors, "MCQ_TEST_MATRIX_BASELINE", json.dumps(baseline, sort_keys=True))
    known_questions = {f"Q{number}" for number in question_ids}
    known_cells = set(cell_ids)
    cells_by_id = {cell.get("cell_id"): cell for cell in cells}
    if "NV-TM-058" not in cells_by_id:
        fail(errors, "NV_FIVE_MOTIONS_CELL_MISSING", "NV-TM-058")
    if "NV-TM-059" not in cells_by_id:
        fail(errors, "NV_GRADED_EVALUATION_CELL_MISSING", "NV-TM-059")

    expected_primary_owners = {
        "NV-TM-006": ("Q6", "NV_MOTION_CAUSAL_ROLE_OWNERSHIP"),
        "NV-TM-016": ("Q19", "NV_DIRECTION_GRID_OWNERSHIP"),
        "NV-TM-019": ("Q23", "NV_SENTENCE_INTELLIGIBILITY_OWNERSHIP"),
        "NV-TM-033": ("Q40", "NV_THREE_GRID_FALSE_MAPPING"),
        "NV-TM-040": ("Q47", "NV_APTA_AUTHORITY_FALSE_MAPPING"),
        "NV-TM-057": ("Q64", "NV_Q64_COMPARISON_ONLY_REQUIRED"),
        "NV-TM-058": ("Q65", "NV_FIVE_MOTIONS_FALSE_MAPPING"),
        "NV-TM-059": ("Q66", "NV_GRADED_EVALUATION_REQUIRED"),
    }
    for cell_id, (question_id, code) in expected_primary_owners.items():
        cell = cells_by_id.get(cell_id)
        if cell is not None and cell.get("mapped_question_ids") != [question_id]:
            fail(errors, code, f"{cell_id} must be owned only by {question_id}")
    if "NV-TM-059" in cells_by_id and "Q64" in cells_by_id["NV-TM-059"].get("mapped_question_ids", []):
        fail(errors, "NV_Q64_GRADED_EVALUATION_FORBIDDEN", "Q64 is comparison-transfer only")
    added_question_ids = {
        qid
        for cell in cells if cell.get("baseline_status") in {"partial", "untested"}
        for qid in cell.get("mapped_question_ids", [])
    }
    explicit_mappings = matrix.get("question_mappings", [])
    explicit_pairs = []
    for mapping in explicit_mappings:
        qid, cell_id = mapping.get("question_id"), mapping.get("cell_id")
        if qid not in known_questions or cell_id not in known_cells:
            fail(errors, "MCQ_UNKNOWN_MAPPING", f"{qid}->{cell_id}")
            continue
        explicit_pairs.append((qid, cell_id))
        cell = cells[cell_ids.index(cell_id)]
        if mapping.get("primary_discriminator") != cell.get("primary_discriminator"):
            fail(errors, "MCQ_FALSE_MAPPING", f"{qid}->{cell_id}:discriminator")
    if len(explicit_pairs) != len(set(explicit_pairs)):
        fail(errors, "MCQ_DUPLICATE_MAPPING", str(explicit_pairs))
    mapping_counts = {qid: sum(pair[0] == qid for pair in explicit_pairs) for qid in known_questions}
    derived_minimum = 0
    for cell in cells:
        cell_id = cell.get("cell_id", "")
        mapped = cell.get("mapped_question_ids", [])
        minimum = cell.get("minimum_probes")
        if (
            not cell.get("description") or not cell.get("source_anchors_scope")
            or not cell.get("minimum_probe_justification") or not cell.get("primary_discriminator")
            or not cell.get("required_question_tokens") or not cell.get("semantic_assertions")
        ):
            fail(errors, "MCQ_TEST_MATRIX_SCHEMA", cell_id)
        if not isinstance(minimum, int) or minimum < 1:
            fail(errors, "MCQ_TEST_MATRIX_SCHEMA", f"{cell_id}:minimum")
            continue
        derived_minimum += minimum
        unknown = [qid for qid in mapped if qid not in known_questions]
        if unknown:
            fail(errors, "MCQ_UNKNOWN_MAPPING", f"{cell_id}:{','.join(unknown)}")
        valid_mapped = [qid for qid in mapped if qid in known_questions]
        for qid in valid_mapped:
            if not any(
                assertion.get("applies_to") is None or qid in assertion.get("applies_to", [])
                for assertion in cell.get("semantic_assertions", [])
            ):
                fail(errors, "MCQ_TEST_MATRIX_SCHEMA", f"{cell_id}:{qid}:no semantic assertion")
                fail(errors, "MCQ_FALSE_MAPPING", f"{qid}->{cell_id}:no applicable semantic assertion")
        explicit_for_cell = sorted(qid for qid, mapped_cell in explicit_pairs if mapped_cell == cell_id)
        if sorted(set(valid_mapped)) != explicit_for_cell:
            fail(errors, "MCQ_MATRIX_MAPPING_MISMATCH", cell_id)
        if len(set(valid_mapped)) < minimum or cell.get("coverage_status") != "covered":
            fail(errors, "MCQ_CELL_BELOW_MINIMUM", f"{cell_id}:{len(set(valid_mapped))}/{minimum}")
        for qid in set(valid_mapped):
            number = int(qid[1:])
            row = questions[number]
            solution = solutions.get(number, {})
            keyed_letter = solution.get("answer")
            keyed_option = solution.get("options", {}).get(keyed_letter, "")
            keyed_explanation = solution.get("explanations", {}).get(keyed_letter, "")
            keyed_searchable = normalized(
                " ".join([row["title"], row["stem"], keyed_option, keyed_explanation])
            )
            for assertion in cell.get("semantic_assertions", []):
                applies_to = assertion.get("applies_to")
                if applies_to is not None and qid not in applies_to:
                    continue
                groups = assertion.get("all_of", [])
                valid_groups = (
                    isinstance(groups, list) and bool(groups)
                    and all(isinstance(group, list) and bool(group) for group in groups)
                )
                if not valid_groups:
                    fail(errors, "MCQ_TEST_MATRIX_SCHEMA", f"{cell_id}:semantic_assertions")
                    continue
                if not all(any(normalized(term) in keyed_searchable for term in group) for group in groups):
                    special_codes = {
                        "NV-TM-006": "NV_MOTION_CAUSAL_ROLE_EVIDENCE_MISSING",
                        "NV-TM-016": "NV_DIRECTION_GRID_EVIDENCE_MISSING",
                        "NV-TM-019": "NV_SENTENCE_INTELLIGIBILITY_EVIDENCE_MISSING",
                        "NV-TM-033": "NV_THREE_GRID_COMPLETE_EVIDENCE_MISSING",
                        "NV-TM-040": "NV_APTA_COMPETENCE_SINCERITY_EVIDENCE_MISSING",
                        "NV-TM-058": "NV_FIVE_MOTIONS_COMPLETE_EVIDENCE_MISSING",
                        "NV-TM-059": "NV_GRADED_EVALUATION_EVIDENCE_MISSING",
                    }
                    fail(
                        errors,
                        special_codes.get(cell_id, "MCQ_SEMANTIC_ASSERTION_MISSING"),
                        f"{qid}->{cell_id}:{assertion.get('assertion', 'unnamed assertion')}",
                    )
                    fail(errors, "MCQ_FALSE_MAPPING", f"{qid}->{cell_id}")
            for assertion in cell.get("distractor_assertions", []):
                applies_to = assertion.get("applies_to")
                if applies_to is not None and qid not in applies_to:
                    continue
                option = assertion.get("option")
                groups = assertion.get("all_of", [])
                if (
                    option not in "ABCD"
                    or option == keyed_letter
                    or not isinstance(groups, list)
                    or not groups
                    or not all(isinstance(group, list) and group for group in groups)
                ):
                    fail(errors, "MCQ_DISTRACTOR_ASSERTION_SCHEMA", f"{cell_id}:{qid}")
                    continue
                distractor_searchable = normalized(
                    " ".join([
                        solution.get("options", {}).get(option, ""),
                        solution.get("explanations", {}).get(option, ""),
                    ])
                )
                if not all(
                    any(normalized(term) in distractor_searchable for term in group)
                    for group in groups
                ):
                    fail(
                        errors,
                        "MCQ_DISTRACTOR_CONTRAST_MISSING",
                        f"{qid}->{cell_id}:{option}:{assertion.get('assertion', 'unnamed assertion')}",
                    )
    uncovered = sorted(qid for qid, count in mapping_counts.items() if count == 0)
    if uncovered:
        fail(errors, "MCQ_UNMAPPED_QUESTION", ",".join(uncovered))
    maximum_mappings = matrix.get("mapping_policy", {}).get("maximum_cells_per_question")
    overloaded = sorted(qid for qid, count in mapping_counts.items() if not isinstance(maximum_mappings, int) or count > maximum_mappings)
    if overloaded:
        fail(errors, "MCQ_MAPPING_OVERLOADED", ",".join(overloaded))
    if len(question_ids) < derived_minimum:
        fail(errors, "MCQ_BANK_BELOW_DERIVED_MINIMUM", f"{len(question_ids)}/{derived_minimum}")
    derivation = mcq_audit.get("derivation", {})
    if (
        derivation.get("matrix_file") != "TEST-MATRIX.json"
        or derivation.get("matrix_cells") != len(cells)
        or derivation.get("derived_minimum_probes") != derived_minimum
        or derivation.get("mapped_unique_question_count") != len(question_ids)
        or derivation.get("all_question_ids_mapped") is not True
    ):
        fail(errors, "MCQ_MATRIX_AUDIT_MISMATCH", json.dumps(derivation, sort_keys=True))
    fixed_hits = legacy_fixed_contract(matrix) + legacy_fixed_contract(mcq_audit)
    if fixed_hits:
        fail(errors, "MCQ_LEGACY_FIXED_COUNT_CONTRACT", ",".join(fixed_hits))
    sequence, option_lengths = [], []
    for number in question_ids:
        qrow, srow = questions.get(number), solutions.get(number)
        if not qrow or not srow or qrow["options"] != srow["options"]:
            fail(errors, "MCQ_OPTION_SOLUTION_TAMPER", str(number))
            continue
        if set(qrow["options"]) != set("ABCD") or set(srow["explanations"]) != set("ABCD"):
            fail(errors, "MCQ_EXPLANATION_SYNC", str(number))
            continue
        answer = srow["answer"]
        correct = [letter for letter, text in srow["explanations"].items() if text.startswith("Correct:")]
        if answer not in "ABCD" or correct != [answer]:
            fail(errors, "MCQ_ANSWER_EXPLANATION_TAMPER", f"{number}:{answer}:{correct}")
            continue
        if f"Q{number}" in added_question_ids:
            for letter in "ABCD":
                if normalized(qrow["options"][letter]) not in normalized(srow["explanations"][letter]):
                    fail(errors, "MCQ_ANSWER_EXPLANATION_TAMPER", f"{number}:{letter}:option-specific")
            if not srow.get("trap"):
                fail(errors, "MCQ_EXAMINER_TRAP_MISSING", str(number))
        sequence.append(answer)
        option_lengths.extend((letter == answer, len(value.split())) for letter, value in qrow["options"].items())
    joined = "".join(sequence)
    counts = {letter: joined.count(letter) for letter in "ABCD"}
    longest = max((len(match.group(0)) for match in re.finditer(r"(.)\1*", joined)), default=0)
    if joined != mcq_audit.get("answer_sequence"):
        fail(errors, "MCQ_AUDIT_SEQUENCE_MISMATCH", joined)
    tolerance = mcq_audit.get("position_policy", {}).get("balance_tolerance_max_difference")
    if (
        counts != mcq_audit.get("answer_counts")
        or not isinstance(tolerance, int)
        or max(counts.values(), default=0) - min(counts.values(), default=0) > tolerance
    ):
        fail(errors, "MCQ_POSITION_IMBALANCE", json.dumps(counts, sort_keys=True))
    if longest > 2:
        fail(errors, "MCQ_POSITION_RUN", str(longest))
    audited_sequence = mcq_audit.get("answer_sequence", "")
    if (
        predictable_cycle(joined)
        or predictable_cycle(audited_sequence)
        or mcq_audit.get("position_policy", {}).get("predictable_cycle_detected") is not False
    ):
        fail(errors, "MCQ_PREDICTABLE_CYCLE", audited_sequence or joined)
    if joined == mcq_audit.get("source_answer_sequence"):
        fail(errors, "MCQ_SOURCE_SEQUENCE_PRESERVED", joined)
    correct_mean = sum(n for correct, n in option_lengths if correct) / len(question_ids)
    wrong_mean = sum(n for correct, n in option_lengths if not correct) / (len(question_ids) * 3)
    metrics = mcq_audit.get("cue_metrics", {})
    if (
        metrics.get("template_filler_count") != 0
        or metrics.get("mean_correct_words") != round(correct_mean, 2)
        or metrics.get("mean_incorrect_words") != round(wrong_mean, 2)
        or not 0.75 <= correct_mean / wrong_mean <= 1.25
    ):
        fail(errors, "MCQ_CUE_METRICS", json.dumps(metrics, sort_keys=True))
    checks.update({
        "matrix_cells": len(cells), "matrix_baseline": baseline,
        "derived_minimum_probes": derived_minimum, "mapped_questions": len(question_ids),
        "mcqs": len(questions), "answer_counts": counts, "answer_sequence": joined,
        "max_run": longest, "predictable_cycle": predictable_cycle(joined),
    })

    pyq_audit = json.loads((root / "PYQ-DEMAND-AUDIT.json").read_text(encoding="utf-8"))
    rows = pyq_audit.get("questions", [])
    if len(rows) != 26 or pyq_audit.get("actual_total") != 26 or pyq_audit.get("formal_preserved_total") != 22:
        fail(errors, "PYQ_OMISSION", f"{len(rows)} primary")
    primary_pattern = re.compile(
        r"^#### Primary PYQ (\d+) · (20\d\d) · (Q\d+\([a-e]\)) · (\d+) marks · Nyāya–Vaiśeṣika · fully solved$",
        re.M,
    )
    support_pattern = re.compile(
        r"^#### Supporting cross-topic PYQ S1 · 2026 · Q7\(a\) · 20 marks · Mīmāṃsā-primary / Nyāya–Vaiśeṣika-supporting · fully solved$",
        re.M,
    )
    expected = [(row["year"], row["question_no"], row["marks"]) for row in rows]
    for name, surface in (("REVISION-GUIDE.md", revision), ("ANSWER-WRITING-TOOLKIT.md", toolkit)):
        found = primary_pattern.findall(surface)
        actual = [(int(year), qno, int(marks)) for _, year, qno, marks in found]
        if [int(number) for number, *_ in found] != list(range(1, 27)) or actual != expected:
            fail(errors, "PYQ_NUMBERING_OR_OWNERSHIP", f"{name}:{actual}")
        if len(support_pattern.findall(surface)) != 1:
            fail(errors, "PYQ_SUPPORTING_OWNERSHIP", name)
        for row in rows:
            marker = f"> **Question, exact verified wording:** {row['text']}"
            if marker not in surface or text_sha(row["text"]) != row.get("text_sha256"):
                fail(errors, "PYQ_WORDING_TAMPER", f"{name}:{row['year']}:{row['question_no']}")
    support = pyq_audit.get("supporting_questions", [{}])[0]
    if (
        pyq_audit.get("supporting_total") != 1
        or support.get("question_no") != "Q7(a)"
        or support.get("ownership") != "Mimamsa-primary/Nyaya-Vaisesika-supporting"
        or text_sha(support.get("text", "")) != support.get("text_sha256")
    ):
        fail(errors, "PYQ_SUPPORTING_AUDIT", json.dumps(support, ensure_ascii=False))
    if pyq_audit.get("original_solved_total") != 6:
        fail(errors, "ORIGINAL_MODEL_COUNT", str(pyq_audit.get("original_solved_total")))
    bands = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
    model_count = 0
    for match in re.finditer(
        r"\*\*Model answer \((10|15|20) marks,\s*(\d+)[–-](\d+) words\)\.\*\*\s*\n"
        r"(.*?)(?=\n\*\*Why this earns marks|\n#### |\n## |\Z)",
        toolkit, re.S,
    ):
        marks = int(match.group(1))
        low, high = bands[marks]
        words = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"[`*#>]", "", match.group(4)), re.UNICODE))
        if (int(match.group(2)), int(match.group(3))) != (low, high) or not low <= words <= high:
            fail(errors, "MAINS_WORD_BAND", f"{model_count + 1}:{marks}:{words}")
        model_count += 1
    if model_count != 33:
        fail(errors, "MAINS_MODEL_COUNT", f"expected 33, found {model_count}")
    checks.update({"primary_pyqs": len(rows), "supporting_pyqs": 1, "originals": 6, "timed_models": model_count})

    if validate_pdfs:
        try:
            from pypdf import PdfReader
        except ImportError:
            fail(errors, "PDF_VALIDATOR_DEPENDENCY_MISSING", "pypdf")
        else:
            manifest = json.loads((root / "PDF-MANIFEST.json").read_text(encoding="utf-8"))
            artifacts = manifest.get("artifacts", [])
            if len(artifacts) != 4:
                fail(errors, "PDF_COUNT", str(len(artifacts)))
            pages = {}
            for row in artifacts:
                source, pdf = root / row.get("source", ""), root / row.get("file", "")
                if not source.is_file() or not pdf.is_file():
                    fail(errors, "PDF_MISSING", row.get("file", ""))
                    continue
                reader = PdfReader(str(pdf))
                if sha(source) != row.get("source_sha256") or sha(pdf) != row.get("pdf_sha256"):
                    fail(errors, "STALE_PDF_OR_MANIFEST", row.get("file", ""))
                if len(reader.pages) != row.get("pages") or not reader.pages:
                    fail(errors, "PDF_PAGE_COUNT", row.get("file", ""))
                metadata = reader.metadata or {}
                if row.get("source_sha256") not in str(metadata.get("/Subject", "")):
                    fail(errors, "PDF_SOURCE_METADATA", row.get("file", ""))
                for index, page in enumerate(reader.pages, 1):
                    width, height = float(page.mediabox.width), float(page.mediabox.height)
                    if not 590 <= width <= 600 or not 838 <= height <= 846:
                        fail(errors, "PDF_PAGE_DIMENSIONS", f"{row.get('file')}:{index}:{width}x{height}")
                    if not (page.extract_text() or "").strip():
                        fail(errors, "PDF_EMPTY_PAGE", f"{row.get('file')}:{index}")
                pages[row.get("file", "")] = len(reader.pages)
            checks["pdf_pages"] = pages

    caches = list(root.rglob("__pycache__")) + list(root.rglob("*.pyc"))
    if caches:
        fail(errors, "BYTECODE_ARTIFACT", ", ".join(str(path) for path in caches))
    if release:
        try:
            repo = Path(subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True).strip())
            relroot = root.relative_to(repo)
            staged = set(subprocess.check_output(["git", "-C", str(repo), "diff", "--cached", "--name-only"], text=True).splitlines())
            missing = [str((relroot / rel).as_posix()) for rel in required if str((relroot / rel).as_posix()) not in staged]
            if missing:
                fail(errors, "GIT_RELEASE_NOT_STAGED", f"{len(missing)} required artifacts not staged")
            for rel in required:
                repo_path = str((relroot / rel).as_posix())
                if repo_path not in staged:
                    continue
                staged_oid = subprocess.check_output(["git", "-C", str(repo), "rev-parse", f":{repo_path}"], text=True).strip()
                working_oid = subprocess.check_output(
                    ["git", "-C", str(repo), "hash-object", f"--path={repo_path}", str(root / rel)],
                    text=True,
                ).strip()
                if staged_oid != working_oid:
                    fail(errors, "GIT_STAGED_CONTENT_STALE", repo_path)
        except Exception as exc:
            fail(errors, "GIT_RELEASE_CHECK_FAILED", str(exc))
    return report(release, checks, errors)


def report(release: bool, checks: dict, errors: list[dict]) -> dict:
    state = "RELEASE_PASS" if release and not errors else ("DEVELOPMENT_PASS" if not release and not errors else "FAIL")
    return {
        "schema_version": 2,
        "validated_at": datetime.now(IST).replace(microsecond=0).isoformat(),
        "mode": "release" if release else "development",
        "state": state, "release_ready": bool(release and not errors),
        "checks": checks, "error_count": len(errors), "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=HERE)
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--pdf", action="store_true", help="Explicitly validate optional PDF artifacts and manifest")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.release, args.pdf)
    if not args.release and not args.check_only:
        (args.root / "VALIDATION.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0 if result["state"].endswith("PASS") else 1


if __name__ == "__main__":
    raise SystemExit(main())
