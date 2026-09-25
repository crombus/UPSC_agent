from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ARTIFACTS = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "COVERAGE-LEDGER.md", "FORMAL-COVERAGE-AUDIT.json", "FORMAL-COVERAGE-REVIEW.json",
    "AUTHORITY-CLASSIFICATION.json", "AUTHORITY-OBLIGATION-LEDGER.json", "TEST-MATRIX.json", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "PRACTICE-LOG.md", "ANSWER-WRITING-TOOLKIT.md", "FORMAL-SOURCE-MIRROR.md",
    "source-snapshots/canonical-Samkhya.md", "source-snapshots/formal-Learning-Session.md",
    "source-snapshots/formal-Solved-Practice-Workbook.md", "source-snapshots/supplementary-complete-session.md",
    "source-snapshots/supplementary-layered-session.md", "source-snapshots/supplementary-solved-workbook.md",
    "source-snapshots/pyq-2018-2025.md", "source-snapshots/pyq-2026.md",
    "build_package.py", "question_bank.py", "validate_package.py", "run_negative_tests.py", "render_pdfs.py", ".gitattributes",
]
SOURCES = {}
FORMAL_ROOT = None
DECLARED_SOURCES = {
    "formal_session": r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\05-Samkhya\Learning-Session.md",
    "formal_workbook": r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\05-Samkhya\Solved-Practice-Workbook.md",
    "canonical": r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Samkhya.md",
    "supplementary_complete": r"C:\up\upsc-ai-kit\knowledge\Philosophy\_learning-sessions\05_Samkhya-Complete-Learning-Session.md",
    "supplementary_layered": r"C:\up\upsc-ai-kit\knowledge\Philosophy\Indian-Philosophy\learning-sessions\Samkhya\Samkhya_Layered-Complete-Learning-Session_2026-08-18.md",
    "supplementary_workbook": r"C:\up\upsc-ai-kit\knowledge\Philosophy\Indian-Philosophy\learning-sessions\Samkhya\Samkhya_Layered-Solved-Practice-Workbook_2026-08-18.md",
    "pyq_2018_2025": r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md",
    "pyq_2026": r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md",
}
FORMAL_EXPECTED = {
    "formal_session": {
        "name": "Learning-Session.md",
        "sha256": "f847272fd032151fda3be9aa36267134ab32b51743792111ca1e8e8cfa66928c",
        "lines": 5194,
        "title": "Sāṃkhya — Complete Learning Session",
    },
    "formal_workbook": {
        "name": "Solved-Practice-Workbook.md",
        "sha256": "9bb5a8b8ce3951946af54d2d86ad10538e3009ba2528a9a83bd98c0117a3d482",
        "lines": 1356,
        "title": "Sāṃkhya — Solved Practice Workbook",
    },
}

def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha_text(text: str) -> str:
    return sha_bytes(text.replace("\r\n", "\n").encode("utf-8"))

def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()

def slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^\w]+", "-", text, flags=re.UNICODE).strip("-")[:72] or "block"

def heading_blocks(path: Path, prefix: str) -> list[dict]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    heads: list[tuple[int, int, str]] = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    rows = []
    for idx, (start, level, heading) in enumerate(heads):
        own_end = heads[idx + 1][0] if idx + 1 < len(heads) else len(lines)
        subtree_end = len(lines)
        for later_start, later_level, _ in heads[idx + 1:]:
            if later_level <= level:
                subtree_end = later_start
                break
        payload = "\n".join(lines[start:own_end]).strip() + "\n"
        subtree = "\n".join(lines[start:subtree_end]).strip() + "\n"
        ident = f"{prefix}-{idx + 1:03d}-{slug(heading)}-{sha_text(payload)[:10]}"
        rows.append({
            "id": ident, "source": prefix, "ordinal": idx + 1, "level": level,
            "heading": heading, "line_start": start + 1, "line_end": own_end,
            "own_payload_sha256": sha_text(payload), "subtree_sha256": sha_text(subtree),
            "own_chars": len(payload), "_payload": payload,
        })
    for row in rows:
        children = []
        for candidate in rows[row["ordinal"]:]:
            if candidate["level"] <= row["level"]:
                break
            if candidate["level"] == row["level"] + 1:
                children.append(candidate["id"])
        row["direct_children"] = children
        child_hashes = [next(x["own_payload_sha256"] for x in rows if x["id"] == cid) for cid in children]
        row["child_union_sha256"] = sha_text("\n".join(child_hashes))
        segments = []
        if len(row["_payload"]) > 2200:
            for number, offset in enumerate(range(0, len(row["_payload"]), 1600), 1):
                chunk = row["_payload"][offset:offset + 1600]
                segments.append({
                    "index": number, "start_char": offset,
                    "end_char_exclusive": offset + len(chunk), "chars": len(chunk),
                    "payload_sha256": sha_text(chunk),
                })
        row["large_leaf_segments"] = segments
    return rows

def structural_reason(unit: str) -> str | None:
    plain = re.sub(r"[*_`>#]", "", unit.strip()).strip()
    if not plain:
        return "blank_or_fence"
    if re.fullmatch(r"BOUNDARY WITH YOGA\s*\(bounded comparison,\s*never a source\)", plain, re.I):
        return "boundary_caption_coordinate"
    if re.fullmatch(r"(?:MASTER\s+)?PANEL(?:\s+\d+(?:/\d+)?|\s+[A-Z])?(?:\s*[:—-].*)?", plain, re.I):
        return "panel_label_coordinate"
    if re.fullmatch(
        r"(?:ASCII\s+)?(?:MASTER\s+)?(?:DIAGRAM|FLOW(?:CHART)?|MAP|SCHEMA|VISUAL)"
        r"(?:\s+\d+|\s+[A-Z])?(?:\s*[:—-].*)?",
        plain,
        re.I,
    ):
        return "diagram_heading_coordinate"
    if (
        re.fullmatch(r"\([^()\n]+\)", plain)
        and re.search(r"\b(?:route|routing|owned|owner|boundary|cross-link|comparison|topic\s+0?6|yoga)\b",
                      plain, re.I)
    ):
        return "parenthetical_routing_instruction"
    package_count_labels = (
        "teaching sessions", "diagnostic multiple-choice questions", "total diagnostics",
        "solved previous-year questions", "original solved mains models",
        "consolidated register parts", "package practice counts",
    )
    if (
        any(label in plain.casefold() for label in package_count_labels)
        and (
            "|" in plain
            or re.search(r"\b(?:count|counts|items?\s+\d+|questions?\s+\d+|\d+\s+core|\d+\s+remedial)\b",
                         plain, re.I)
        )
    ) or re.match(r"^(?:composition|package composition)\s*:", plain, re.I) or re.search(
        r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d+)\s+"
        r"(?:items?|questions?|sessions?|diagnostics?)\s+(?:target|cover|are\s+(?:primary|routed)|in\s+the)\b",
        plain, re.I,
    ):
        return "package_composition_metadata"
    if re.match(r"^#{1,6}\s+", unit.strip()) and "|" not in unit:
        return "heading_coordinate"
    if plain in {"---", "___"}:
        return "yaml_or_separator"
    if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?", plain):
        return "table_separator"
    if re.fullmatch(r"[│┌┐└┘├┤┬┴┼─═╔╗╚╝╠╣╦╩╬+\-\s]+", plain):
        return "diagram_border"
    if re.match(r"^(?:[-*]\s*)?(?:\*\*)?[A-D][.:](?:\*\*)?\s+", plain):
        return "mcq_option_coordinate"
    if re.match(r"^(?:\*\*)?(?:answer|correct answer|key|option-by-option explanation|examiner trap)(?:\*\*)?\s*:?", plain, re.I):
        return "answer_key_coordinate"
    if re.match(r"^-\s*\*\*[A-D]:\*\*", unit.strip()):
        return "option_explanation_coordinate"
    if re.fullmatch(r"(?:model solution|why this earns marks|question|examiner trap|demand decoded)\s*:?", plain, re.I):
        return "answer_or_explanation_coordinate"
    claim_markers = re.compile(
        r"(?:=|→|⇒|↔|∴|\b(?:is|are|was|were|be|being|becomes?|remains?|means?|"
        r"entails?|implies?|explains?|produces?|causes?|requires?|depends?|argues?|"
        r"delivers?|supports?|asserts?|grounds?|constitutes?|reveals?|shows?|"
        r"distinguishes?|preserves?|creates?|begins?|stops?|knows?|migrates?)\b)",
        re.I,
    )
    columns = [c.strip() for c in re.split(r"\s*\|\s*|\s{2,}", plain) if c.strip()]
    if len(columns) >= 2 and all(len(c.split()) <= 7 for c in columns):
        letters = "".join(re.findall(r"[^\W\d_]", plain, re.UNICODE))
        upper_ratio = sum(ch.isupper() for ch in letters) / max(1, sum(ch.isalpha() for ch in letters))
        if upper_ratio >= 0.72 and not re.search(r"(?:=|→|⇒|↔|∴)", plain):
            return "diagram_column_header"
    words_only = re.findall(r"[^\W\d_]+", plain, re.UNICODE)
    letters = "".join(words_only)
    upper_ratio = sum(ch.isupper() for ch in letters) / max(1, sum(ch.isalpha() for ch in letters))
    if (
        1 <= len(words_only) <= 12
        and upper_ratio >= 0.72
        and not claim_markers.search(plain)
        and not re.search(r"[.!?][”'\"]?$", plain)
    ):
        return "visual_label_coordinate"
    if len(re.sub(r"[\W_]+", "", plain, flags=re.UNICODE)) < 3:
        return "symbol_fragment"
    return None

def deterministic_sample_candidate(unit: str) -> bool:
    plain = re.sub(r"[*_`>#]", "", unit.strip()).strip()
    if structural_reason(unit):
        return False
    first_alpha = next((ch for ch in plain if ch.isalpha()), "")
    if first_alpha and first_alpha.islower():
        return False
    if re.match(r"^(?:consider|which|what|why|how|attempt|choose|select|question)\b", plain, re.I):
        return False
    if "|" in plain or "?" in plain or re.match(r"^\d+[.)]\s+", plain):
        return False
    if re.search(
        r"\b(?:correct answer|examiner trap|option [A-D]|items?\s+\d+[-–]\d+|"
        r"teaching order|basic block|advanced block|workbook|diagnostic|wording discipline|"
        r"demand decoded|printed question|model answer|previous-year question)\b",
        plain, re.I,
    ):
        return False
    claim = re.search(
        r"(?:=|→|⇒|↔|\b(?:is|are|was|were|becomes?|remains?|means?|entails?|implies?|"
        r"explains?|produces?|causes?|requires?|depends?|supports?|asserts?|grounds?|"
        r"constitutes?|reveals?|shows?|distinguishes?|preserves?|creates?)\b)",
        plain, re.I,
    )
    return bool(claim and len(re.findall(r"[^\W\d_]+", plain, re.UNICODE)) >= 5)

TARGETED_CONTIGUOUS_JOIN_HASHES = {
    "01c66f1a4aba86775ad7e9cc2b16bb3d45080b3f158c0eb531d87a5e54a7404e",
    "db2b035c9963e1be312de56a07d45e754f419644898157df64339fe7355df87a",
    "539f9c01d36a6fa56ab8b0fb581c53c2f78ac28dae7b389a1a35c67fa232473b",
    "7487f792c198253860ba22c64a1de7a28cc85174712691bcf07dc9bc12f0d772",
    "89e2d1b23a4f02f3c18c576f7c8b08b800c4205d0c727dd8850c24755ae64e45",
    "a076eb6a556a396f88217a9cd8a0d222bbbe0a3173a94d15c9f66cf25a7d664d",
    "ed334f2a17d5ddb91067051179e0ca58a0376df20a3c36d0bc542f10615b9fa1",
    "132302d47b4a8ba52ecf669c9d0596f90f010ba0c34a068dd55cf69c35bd36e9",
}

def incomplete_syntax_reason(payload: str) -> str | None:
    plain = re.sub(r"[*_`>#]", "", payload.strip()).strip()
    if not plain:
        return None
    if plain.count("(") > plain.count(")"):
        return "unmatched_open_parenthesis"
    if re.search(r"\bwould not be\s*$", plain, re.I):
        return "dangling_copular_negation"
    if re.search(r"\b(?:a|an|the|and|or|but)\s*$", plain, re.I):
        return "dangling_function_word"
    if re.search(r"\bchanging(?:\s+unconscious)?\s*$", plain, re.I):
        return "dangling_attributive_phrase"
    if re.search(r"\boperate\s*$", plain, re.I):
        return "wrapped_prepositional_continuation"
    if plain.endswith(";") and re.match(r"^(?:\d+\s+)?if\b", plain, re.I):
        return "suspended_conditional_pair"
    return None

def incomplete_clause(payload: str) -> bool:
    plain = re.sub(r"[*_`>#]", "", payload.strip()).strip()
    return bool(plain and re.search(r"\bwould not be\s*$", plain, re.I))

def semantic_units(payload: str, include_repairs: bool = False, apply_repairs: bool = True):
    lines = payload.replace("\r\n", "\n").splitlines()
    units: list[str] = []
    excluded: list[dict] = []
    paragraph: list[str] = []
    in_code = False

    def append_unit(value: str) -> None:
        value = value.strip()
        if not value:
            return
        units.append(value)

    def flush() -> None:
        if paragraph:
            append_unit(" ".join(x.strip() for x in paragraph).strip())
            paragraph.clear()

    def is_table_separator(line: str) -> bool:
        stripped = line.strip()
        if not stripped.startswith("|"):
            return False
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells)

    for line_index, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```"):
            flush()
            excluded.append({"exact_payload": line, "reason": "fence_coordinate"})
            in_code = not in_code
            continue
        if in_code:
            reason = structural_reason(line)
            if reason:
                excluded.append({"exact_payload": line, "reason": reason})
                if reason == "boundary_caption_coordinate":
                    parenthetical = re.search(r"\([^()]+\)", line)
                    if parenthetical:
                        excluded.append({
                            "exact_payload": parenthetical.group(0),
                            "reason": "parenthetical_routing_instruction",
                        })
                if reason == "diagram_heading_coordinate":
                    panel_label = re.search(r"PANEL\s+\d+/\d+\s*:[^\n]+", line, re.I)
                    if panel_label:
                        excluded.append({
                            "exact_payload": panel_label.group(0).strip(),
                            "reason": "panel_label_coordinate",
                        })
            else:
                append_unit(line.strip())
            continue
        if not s:
            flush()
            continue
        if re.match(r"^#{1,6}\s+", s):
            flush()
            excluded.append({"exact_payload": line, "reason": "heading_coordinate"})
            continue
        if s.startswith("|"):
            flush()
            cells = [c.strip() for c in s.strip("|").split("|")]
            joined = " | ".join(cells)
            if is_table_separator(line):
                excluded.append({"exact_payload": line, "reason": "table_separator"})
            elif line_index + 1 < len(lines) and is_table_separator(lines[line_index + 1]):
                excluded.append({"exact_payload": line, "reason": "table_header_scaffolding"})
            elif all(len(re.sub(r"\W+", "", c)) < 2 for c in cells):
                excluded.append({"exact_payload": line, "reason": "table_scaffolding"})
            elif structural_reason(joined):
                excluded.append({"exact_payload": joined, "reason": structural_reason(joined)})
            else:
                append_unit(joined)
            continue
        if re.match(r"^\s*(?:[-*+]|\d+\.)\s+", line):
            flush()
            reason = structural_reason(s)
            if reason:
                excluded.append({"exact_payload": s, "reason": reason})
            else:
                append_unit(s)
            continue
        if paragraph and structural_reason(s) == "answer_key_coordinate":
            flush()
            excluded.append({"exact_payload": s, "reason": "answer_key_coordinate"})
            continue
        if paragraph:
            paragraph.append(s)
            continue
        reason = structural_reason(s)
        if reason:
            flush()
            excluded.append({"exact_payload": s, "reason": reason})
        else:
            paragraph.append(s)
    flush()
    joined_units = []
    repairs = []
    index = 0
    while index < len(units):
        if index + 1 < len(units):
            left, right = units[index], units[index + 1]
            joined = f"{left} {right}".strip()
            joined_hash = sha_text(norm(joined))
            reason = incomplete_syntax_reason(left)
            if apply_repairs and joined_hash in TARGETED_CONTIGUOUS_JOIN_HASHES and reason:
                joined_units.append(joined)
                repairs.append({
                    "left_original_ordinal": index + 1,
                    "right_original_ordinal": index + 2,
                    "left_exact_payload": left,
                    "left_exact_payload_sha256": sha_text(left),
                    "right_exact_payload": right,
                    "right_exact_payload_sha256": sha_text(right),
                    "joined_payload": joined,
                    "joined_payload_sha256": sha_text(joined),
                    "joined_normalized_sha256": joined_hash,
                    "old_proposition_ids": [
                        "prop-" + sha_text(norm(left))[:20],
                        "prop-" + sha_text(norm(right))[:20],
                    ],
                    "new_proposition_id": "prop-" + joined_hash[:20],
                    "reason": reason,
                })
                index += 2
                continue
        joined_units.append(units[index])
        index += 1
    units = joined_units
    dangling = [unit for unit in units if incomplete_clause(unit)]
    if apply_repairs and dangling:
        raise ValueError("INCOMPLETE_SOURCE_PAYLOAD:" + dangling[0])
    excluded_rows = []
    for i, item in enumerate(excluded, 1):
        excluded_rows.append({
            "source_ordinal": i, "reason": item["reason"],
            "exact_payload_sha256": sha_text(item["exact_payload"]),
            "exact_payload": item["exact_payload"],
        })
    if include_repairs:
        return units, excluded_rows, repairs
    return units, excluded_rows

def extract_panels(path: Path, prefix: str) -> list[dict]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    panels = []
    for i, m in enumerate(re.finditer(r"```[^\n]*\n.*?\n```", text, re.S), 1):
        payload = m.group(0)
        panels.append({"id": f"{prefix}-diagram-{i:03d}-{sha_text(payload)[:10]}", "kind": "diagram",
                       "payload_sha256": sha_text(payload), "chars": len(payload), "_payload": payload})
    table_re = re.compile(r"(?m)(?:^\|.*\|\n){2,}")
    for i, m in enumerate(table_re.finditer(text), 1):
        payload = m.group(0).rstrip() + "\n"
        panels.append({"id": f"{prefix}-table-{i:03d}-{sha_text(payload)[:10]}", "kind": "table",
                       "payload_sha256": sha_text(payload), "chars": len(payload), "_payload": payload})
    return panels

PYQS = [
    (2018, "Q5(e)", 10, "Is Puruṣa one or many? Explain the Sāṃkhya position in this regard and give arguments in support of your answer.", "plurality"),
    (2018, "Q7(b)", 15, "How do the Advaita Vedāntins react to the Prakṛtipariṇāmavāda of the Sāṃkhya philosophy? How do the Sāṃkhyas defend their own position in this regard? Discuss.", "parinama_advaita"),
    (2019, "Q5(d)", 10, "Critically discuss the metaphysical status of a Jīva and a Puruṣa according to Sāṃkhya philosophy.", "jiva"),
    (2019, "Q8(c)", 15, "Which Sāṃkhya proof for the existence of Prakṛti actually shows that there can be only one Prakṛti? Justify your answer.", "one_prakriti"),
    (2020, "Q7(a)", 20, "“A mango tree is grown out of a mango seed.” How will Sāṃkhya system explain this process through their theory of causation by rejecting their rival perspectives?", "mango"),
    (2021, "Q6(b)", 15, "Explain the Sāṃkhya view on three guṇas (guṇa-traya) and their modifications.", "gunas"),
    (2022, "Q5(a)", 10, "Examine and evaluate the proofs given by Sāṃkhya philosophy to prove the existence of Puruṣa.", "purusa_proofs"),
    (2023, "Q5(b)", 10, "“If Puruṣa and Prakṛti are two completely independent realities, then no relation between the two is possible.” In the light of this statement make a brief presentation of Śaṅkara’s criticism of Sāṃkhya dualism.", "contact"),
    (2024, "Q7(a)", 20, "Present an account of evolution of Prakṛti as propounded in Sāṃkhyakārikā. In this context, also explain the difference between buddhi, mahat and ahaṃkāra.", "evolution"),
    (2025, "Q7(a)", 20, "Why does Śaṅkara consider Sāṃkhya Philosophy as his chief opponent (pradhāna malla)? Examine his arguments against Sāṃkhya Philosophy.", "pradhana_malla"),
    (2026, "Q5(c)", 10, "Is Purusa one or many? Explain and examine the Sankhya position in this context.", "plurality_2026"),
    (2026, "Q6(a)", 20, "\"A mango tree is grown out of a mango seed.\" How do the Sankhya philosophers explain this process through their theory of causation by rejecting their rival perspectives?", "mango_2026"),
]

SUPPORTING_PYQS = [
    (2021, "Q5(a)", 10, "Does the seed contain the tree? Discuss with reference to Nyāya-Vaiśeṣika Philosophy.", "Primary owner: Nyāya–Vaiśeṣika; Sāṃkhya supplies the satkāryavāda contrast only."),
    (2022, "Q5(e)", 10, "Do you agree with the view that ‘Vivartavāda is the logical development of Pariṇāmavāda’? Give reasons in support of your answer.", "Primary owner: Vedānta; Sāṃkhya supplies the pariṇāma comparison only."),
    (2023, "Q8(b)", 15, "Write a note on Nyāya notion of Prāgabhāva (prior non-existence). How does this notion help Naiyāyikas in defending their position on causation against the Sāṃkhya view of causation? Critically discuss.", "Primary owner: Nyāya–Vaiśeṣika; Sāṃkhya supplies the satkāryavāda comparison only."),
]

def words(text: str) -> int:
    return len(re.findall(r"\b[\wĀ-ž’'-]+\b", re.sub(r"[#*`|]", " ", text), flags=re.UNICODE))


IST = timezone(timedelta(hours=5, minutes=30))
ANSWER_DRAW_ALGORITHM_VERSION = "sha256-rejection-v1"
ANSWER_DRAW_SEED_POLICY = "sha256('samkhya-answer-position-v1|' + stable_question_id)"

RELATION_STOP = {
    "a", "an", "and", "are", "as", "at", "be", "best", "by", "does", "for", "from",
    "how", "in", "is", "it", "its", "of", "on", "or", "that", "the", "their", "this",
    "to", "what", "which", "why", "with",
}
GENERIC_RELATION_TERMS = {
    "also", "another", "because", "classical", "however", "into", "less", "more",
    "nature", "only", "other", "rather", "same", "samkhya", "sankhya", "such",
    "system", "than", "their", "them", "therefore", "these", "they", "those",
    "three", "through", "thus", "under", "upon", "when", "where", "while",
    "within", "without", "would",
}

def relation_tokens(payload: str) -> set[str]:
    return {
        token for token in re.findall(r"[^\W_]+", norm(payload), re.UNICODE)
        if len(token) >= 4 and token not in RELATION_STOP
    }

def relation_component(text: str, target: dict, proposition_payloads: dict[str, str]) -> dict:
    target_payload = proposition_payloads[target["proposition_ids"][0]]
    anchors = sorted((relation_tokens(text) & relation_tokens(target_payload)) - GENERIC_RELATION_TERMS,
                     key=lambda token: (-len(token), token))[:8]
    if len(anchors) < 2:
        raise ValueError("composite anchors")
    return {
        "component_text": text, "component_sha256": sha_text(norm(text)),
        "target_obligation_ids": [target["obligation_id"]],
        "doctrine_anchors": [{"obligation_id": target["obligation_id"],
                              "shared_doctrine_terms": anchors}],
    }

def independent_supporting_classification(payload: str, atomic_rows: list[dict],
                                          proposition_payloads: dict[str, str],
                                          contextual_atomic_ids: list[str]) -> dict:
    text = norm(payload)
    by_rule = {row["classification_rule_id"]: row for row in atomic_rows}
    if "three-instrument scheme" in text and "five named reductions" in text:
        target = by_rule["SK-TR-008"]
        components = [
            relation_component("Perception, inference and reliable testimony are the three admitted pramāṇas.", target, proposition_payloads),
            relation_component("Comparison (upamāna) is reduced to inference or reliable testimony.", target, proposition_payloads),
            relation_component("Postulation (arthāpatti) is reduced to inference.", target, proposition_payloads),
            relation_component("Non-apprehension (anupalabdhi) is reduced to perception's failure-conditions.", target, proposition_payloads),
            relation_component("Inclusion or probability (sambhava) is reduced to inference.", target, proposition_payloads),
            relation_component("Traditional report (aitihya) is reduced to reliable testimony when trustworthy.", target, proposition_payloads),
        ]
        return {
            "substantive_category": "represented_doctrinal_proposition",
            "classification_predicate": {
                "represented_by_obligation_ids": [target["obligation_id"]],
                "relation_type": "composite_split",
                "source_component_contract": {"kind": "three_pramanas_plus_five_named_reductions",
                                              "expected_component_count": 6},
                "components": components,
            },
            "classification_rationale":
                f"The summary is split into the three-pramāṇa claim and all five named reductions, each covered by {target['obligation_id']}.",
        }
    if sha_text(text) == "db2b035c9963e1be312de56a07d45e754f419644898157df64339fe7355df87a":
        target = by_rule["SK-TR-039"]
        anchors = sorted(
            (relation_tokens(payload) & relation_tokens(
                proposition_payloads[target["proposition_ids"][0]]
            )) - GENERIC_RELATION_TERMS,
            key=lambda token: (-len(token), token),
        )[:8]
        return {
            "substantive_category": "represented_doctrinal_proposition",
            "classification_predicate": {
                "represented_by_obligation_ids": [target["obligation_id"]],
                "relation_type": "entailed_by",
                "doctrine_specific_anchors": [{
                    "obligation_id": target["obligation_id"],
                    "shared_doctrine_terms": anchors,
                }],
            },
            "classification_rationale":
                f"The ordinary-remedy proposition is entailed by {target['obligation_id']}'s doctrine of partial relief and final cessation.",
        }
    anti = re.findall(r"\((\d)\)\s*(.*?)(?=\s*\(\d\)|$)", payload)
    if "five non-theistic arguments" in text and len(anti) == 5:
        targets = [by_rule[f"SK-TR-{number:03d}"] for number in range(60, 65)]
        components = [relation_component(part.strip(" .;"), target, proposition_payloads)
                      for (_, part), target in zip(anti, targets)]
        ids = [target["obligation_id"] for target in targets]
        return {
            "substantive_category": "represented_doctrinal_proposition",
            "classification_predicate": {
                "represented_by_obligation_ids": ids, "relation_type": "composite_split",
                "source_component_contract": {"kind": "five_anti_theistic_arguments",
                                              "expected_component_count": 5},
                "components": components,
            },
            "classification_rationale":
                f"The five numbered anti-theistic arguments are split without omission and covered respectively by {', '.join(ids)}.",
        }
    source_terms = relation_tokens(payload)
    candidates = []
    weak_candidates = []
    for atomic in atomic_rows:
        atomic_payload = proposition_payloads.get(atomic["proposition_ids"][0])
        if atomic_payload is None:
            continue
        shared = source_terms & relation_tokens(atomic_payload)
        doctrine_anchors = sorted(shared - GENERIC_RELATION_TERMS,
                                  key=lambda x: (-len(x), x))
        if len(doctrine_anchors) >= 2:
            candidates.append((len(shared), atomic["obligation_id"], doctrine_anchors[:6]))
        elif doctrine_anchors:
            weak_candidates.append((atomic["obligation_id"], doctrine_anchors))
    candidates.sort(key=lambda x: (-x[0], x[1]))
    if candidates:
        best = candidates[0][0]
        selected = [row for row in candidates if row[0] >= max(2, best - 1)][:4]
        ids = [row[1] for row in selected]
        return {
            "substantive_category": "represented_doctrinal_proposition",
            "classification_predicate": {
                "represented_by_obligation_ids": ids,
                "relation_type": "entailed_by",
                "doctrine_specific_anchors": [
                    {"obligation_id": row[1], "shared_doctrine_terms": row[2]} for row in selected
                ],
            },
            "classification_rationale":
                f"The proposition is covered by {', '.join(ids)} through the recorded doctrine-specific anchors; it creates no separate test duty.",
        }
    structural = {
        "example_only": bool(re.search(r"\b(?:example|analogy|image|illustration)\b", text)),
        "source_attribution_or_citation_only": bool(re.search(
            r"\b(?:bibliography|reference|source control|citation|vol\.?|chapter|kārikā|karika|"
            r"kapila|īśvarakṛṣṇa|isvarakrsna|vācaspati|radhakrishnan|sharma)\b", text)),
        "answer_writing_or_meta": bool(re.search(
            r"\b(?:model answer|word limit|marks?|question|pyq|write|examiner|revision|"
            r"mnemonic|checklist|trap|body [abc]|introduction|conclusion|licence|supplementary|directive|judgement|end with|begin with|open with|conclude|paragraph|answer structure)\b", text))
            or bool(re.search(r"[┌┐└┘│├┤─►◄→⇒]|\.{4,}", payload)) or words(payload) <= 4 or bool(re.fullmatch(r"\s*\*\*[^*]{1,100}\*\*\s*", payload)) or bool(re.fullmatch(r"(?:\s*v){3,}\s*", payload, re.I)) or (len(re.findall(r"\b[A-ZĀ-Ž-]{4,}\b", payload)) >= 2 and bool(re.search(r"\s{3,}", payload))) or payload.strip().endswith("?"),
        "chronology_or_context_only": bool(re.search(
            r"\b(?:century|later phase|earlier|historical|tradition|modern|classical period|"
            r"development)\b|\b(?:18|19|20)\d{2}\b", text)),
    }
    matched = [category for category, yes in structural.items() if yes]
    if not matched and weak_candidates:
        selected = sorted(weak_candidates)[:2]
        ids = [row[0] for row in selected]
        return {
            "substantive_category": "qualification_dependent_on_atomic_claim",
            "classification_predicate": {
                "non_testability_category": "qualification_dependent_on_atomic_claim",
                "named_atomic_ids": ids,
                "context_terms": [{"obligation_id": oid, "shared_term": terms[0]}
                                  for oid, terms in selected],
            },
            "classification_rationale":
                f"The fragment qualifies {', '.join(ids)} through the recorded context terms and is not independently testable without those atomic claims.",
        }
    if not matched and contextual_atomic_ids:
        ids = sorted(set(contextual_atomic_ids))[:4]
        return {
            "substantive_category": "repeated_implication",
            "classification_predicate": {
                "non_testability_category": "repeated_implication",
                "named_atomic_ids": ids,
                "same_authority_block": True,
            },
            "classification_rationale":
                f"The proposition repeats an implication of {', '.join(ids)} in the same authority block and creates no independent discriminator.",
        }
    concept_rules = {
        "SK-TR-032": r"\b(?:continuity of constitution|dependence|disconnected ultimates|undivided source)\b",
        "SK-TR-015": r"\b(?:god|divine|creator|theistic)\b",
        "SK-TR-058": r"\b(?:dancer|stops performing|binding display)\b",
        "SK-TR-059": r"\b(?:imperceptib|subtlety|saukṣmya|supersensible)\b",
        "SK-TR-008": r"\b(?:upamāna|arthāpatti|anupalabdhi|sambhava|aitihya|pramāṇa|testimony|inference|perception)\b",
        "SK-TR-002": r"\b(?:sattva|rajas|tamas|guṇa|qualities|pleasure|pain|delusion)\b",
        "SK-TR-010": r"\b(?:mahat|buddhi|ahaṃkāra|tanmātra|evolution|evolute)\b",
        "SK-TR-021": r"\b(?:puruṣa|purusa|witness|consciousness|watches|watcher)\b",
        "SK-TR-036": r"\b(?:prakṛti|prakrti|pradhāna|avyakta|material root)\b",
        "SK-TR-013": r"\b(?:satkāryavāda|satkaryavada|pariṇāma|parinama|effect|cause)\b",
        "SK-TR-022": r"\b(?:kaivalya|liberation|release|viveka|discriminative knowledge)\b",
        "SK-TR-039": r"\b(?:duḥkha|duhkha|suffering|three pains)\b",
        "SK-TR-042": r"\b(?:plurality|many witnesses|birth|death|faculties)\b",
        "SK-TR-006": r"\b(?:dvāra|dvarin|dvārin|doors|doorkeeper|instrument|manas)\b",
    }
    rule_to_oid = {row["classification_rule_id"]: row["obligation_id"] for row in atomic_rows}
    ids = sorted(rule_to_oid[rid] for rid, pattern in concept_rules.items()
                 if rid in rule_to_oid and re.search(pattern, text))
    if not matched and ids:
        return {
            "substantive_category": "repeated_implication",
            "classification_predicate": {
                "non_testability_category": "repeated_implication",
                "named_atomic_ids": ids,
                "source_derived_concept_patterns": sorted(
                    rid for rid, pattern in concept_rules.items() if rid in rule_to_oid and re.search(pattern, text)
                ),
            },
            "classification_rationale":
                f"The proposition repeats a source-derived implication of {', '.join(ids)} and creates no independent discriminator.",
        }
    if not matched:
        return {
            "substantive_category": "non_atomic_context",
            "classification_predicate": {"non_testability_category": "non_atomic_context",
                                         "standalone_test_duty": False},
            "classification_rationale":
                "The proposition is contextual exposition, not an atomic discriminator and not a represented claim.",
        }
    category = sorted(matched)[0]
    return {
        "substantive_category": category,
        "classification_predicate": {
            "non_testability_category": category,
            "independently_checkable_signals": sorted(key for key, value in structural.items() if value),
        },
        "classification_rationale":
            f"The proposition is non-testable as {category}; its recorded structural signals are independently checkable and it asserts no standalone doctrinal discriminator.",
    }

def independent_draw(question_id: str, accepted: str) -> dict:
    seed=sha_text("samkhya-answer-position-v1|"+question_id); attempts=[]
    for attempt in range(100):
        digest=sha_text(f"{ANSWER_DRAW_ALGORITHM_VERSION}|{seed}|{attempt}"); letter="ABCD"[int(digest,16)%4]; candidate=accepted+letter; reasons=[]
        if len(candidate)>=3 and candidate[-3:]==letter*3: reasons.append("max_run_two")
        for period in range(2,5):
            if len(candidate)>=period*3 and candidate[-period*3:]==candidate[-period:]*3: reasons.append("reject_three_repeated_cycles_period_2_to_4"); break
        attempts.append({"attempt":attempt,"digest":digest,"draw_index":int(digest,16)%4,"draw_letter":letter,"rejected":bool(reasons),"rejection_reasons":reasons})
        if not reasons:
            evidence={"question_id":question_id,"algorithm_version":ANSWER_DRAW_ALGORITHM_VERSION,"seed_policy":ANSWER_DRAW_SEED_POLICY,"seed":seed,"raw_draw":attempts[0]["draw_letter"],"attempts":attempts,"rejection_log":[x for x in attempts if x["rejected"]],"final_placement":letter}; evidence["draw_hash"]=sha_text(json.dumps(evidence,ensure_ascii=False,sort_keys=True)); return evidence
    raise RuntimeError(question_id)

REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "COVERAGE-LEDGER.md", "FORMAL-COVERAGE-AUDIT.json", "FORMAL-COVERAGE-REVIEW.json",
    "AUTHORITY-CLASSIFICATION.json", "AUTHORITY-OBLIGATION-LEDGER.json", "TEST-MATRIX.json", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md", "FORMAL-SOURCE-MIRROR.md", "SOURCE-ARTIFACT-AUDIT.json",
    "source-snapshots/formal-Learning-Session.md", "source-snapshots/formal-Solved-Practice-Workbook.md",
    "source-snapshots/canonical-Samkhya.md", "source-snapshots/supplementary-complete-session.md",
    "source-snapshots/supplementary-layered-session.md", "source-snapshots/supplementary-solved-workbook.md",
    "source-snapshots/pyq-2018-2025.md", "source-snapshots/pyq-2026.md",
    "build_package.py", "question_bank.py", "validate_package.py", "run_negative_tests.py", "render_pdfs.py", ".gitattributes",
    "VALIDATION.json",
]


def fail(errors: list[dict], code: str, detail: str) -> None:
    errors.append({"code": code, "detail": detail})


def proposition_inflation_code(payload: str) -> str:
    reason = structural_reason(payload)
    return {
        "visual_label_coordinate": "VISUAL_LABEL_PROPOSITION_INFLATION",
        "diagram_column_header": "DIAGRAM_COLUMN_HEADER_INFLATION",
        "boundary_caption_coordinate": "BOUNDARY_CAPTION_STRUCTURAL_INFLATION",
        "panel_label_coordinate": "PANEL_LABEL_STRUCTURAL_INFLATION",
        "diagram_heading_coordinate": "DIAGRAM_HEADING_STRUCTURAL_INFLATION",
        "parenthetical_routing_instruction": "PARENTHETICAL_ROUTING_STRUCTURAL_INFLATION",
        "package_composition_metadata": "PACKAGE_COMPOSITION_PROPOSITION_INFLATION",
    }.get(reason, "NON_PROPOSITION_FRAGMENT_INCLUDED")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def anchor_payload(text: str, anchor: str) -> str | None:
    token = f'<a id="{anchor}"></a>'
    start = text.find(token)
    if start < 0:
        return None
    start = text.find("\n", start) + 1
    end = text.find("\n<a id=", start)
    if end < 0:
        end = len(text)
    return text[start:end].strip() + "\n"


def table_header_lines(payload: str) -> list[str]:
    lines = payload.replace("\r\n", "\n").splitlines()

    def separator(line: str) -> bool:
        stripped = line.strip()
        if not stripped.startswith("|"):
            return False
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)

    return [
        line for index, line in enumerate(lines[:-1])
        if line.strip().startswith("|") and separator(lines[index + 1])
    ]


def parse_mcqs(text: str) -> dict[int, dict]:
    result = {}
    for chunk in re.split(r"(?=^## MCQ \d+\.)", text, flags=re.M):
        head = re.match(r"## MCQ (\d+)\.\s*(.+)\n", chunk)
        if not head:
            continue
        options = {}
        for m in re.finditer(r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:|\n## |\Z)", chunk, re.M | re.S):
            options[m.group(1)] = re.sub(r"\s+", " ", m.group(2).strip())
        ans = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
        stem_part = chunk[head.end():]
        first_opt = re.search(r"^[A-D]\.\s+", stem_part, re.M)
        stem = stem_part[:first_opt.start()].strip() if first_opt else stem_part.strip()
        explanations = {m.group(1): re.sub(r"\s+", " ", m.group(2).strip())
                        for m in re.finditer(r"^- \*\*([A-D]):\*\*\s*(.+)$", chunk, re.M)}
        trap = re.search(r"^\*\*Examiner trap:\*\*\s*(.+)$", chunk, re.M)
        result[int(head.group(1))] = {
            "title": head.group(2).strip(), "stem": stem, "options": options,
            "answer": ans.group(1) if ans else None, "explanations": explanations,
            "trap": re.sub(r"\s+", " ", trap.group(1).strip()) if trap else None,
        }
    return result


def repeated_explanation_fragments(mcqs: dict[int, dict], threshold: int = 2) -> list[dict]:
    fragments = []
    for q in mcqs.values():
        for letter, explanation in q["explanations"].items():
            if letter == q["answer"]:
                continue
            for sentence in re.split(r"(?<=[.!?])\s+", explanation):
                cleaned = norm(sentence)
                if words(cleaned) >= 8:
                    fragments.append(cleaned)
    return [{"text": text, "count": count} for text, count in Counter(fragments).items() if count > threshold]


def parse_model_answers(text: str) -> list[dict]:
    models = []
    pattern = re.compile(
        r"^\*\*Model answer \((\d+) words\):\*\*\n\n(.*?)(?=\n\n\*\*(?:Qualification / criticism|Self-check):\*\*)",
        re.M | re.S,
    )
    for match in pattern.finditer(text):
        body = match.group(2).strip()
        models.append({"declared": int(match.group(1)), "actual": words(body), "body": body})
    return models


def predictable_cycles(sequence: str) -> list[tuple[int, int, str]]:
    hits = []
    for period in range(2, 5):
        for start in range(len(sequence) - period * 3 + 1):
            unit = sequence[start:start + period]
            if len(set(unit)) > 1 and sequence[start:start + period * 3] == unit * 3:
                hits.append((period, start, unit))
    return hits


def legacy_contract(value, path: str = "") -> list[str]:
    hits = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else key
            if key in {"fixed_question_count", "source_core", "source_remedial", "answers_per_letter", "balanced_exactly"}:
                hits.append(child_path)
            hits.extend(legacy_contract(child, child_path))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            hits.extend(legacy_contract(child, f"{path}[{i}]"))
    elif isinstance(value, str) and re.search(r"\b32 questions?\b|\b24\s*\+\s*8\b|\b24 core\b|fixed total", value, re.I):
        hits.append(path)
    return hits


def report(release: bool, checks: dict, errors: list[dict]) -> dict:
    state = "RELEASE_PASS" if release and not errors else "DEVELOPMENT_PASS" if not release and not errors else "FAIL"
    return {
        "schema_version": 3, "topic": "05 Samkhya",
        "validated_at": datetime.now(IST).isoformat(timespec="seconds"),
        "mode": "release" if release else "development", "state": state,
        "release_ready": bool(release and not errors), "pdf_validation": "not_requested",
        "release_blockers": [] if release and not errors else (
            [row["code"] for row in errors] if release
            else ["Package is intentionally unstaged; user prohibited staging, commit, and push."]
        ),
        "checks": checks, "errors": errors,
    }


def validate(root: Path, release: bool) -> dict:
    global SOURCES, FORMAL_ROOT
    snap = root / "source-snapshots"
    SOURCES = {
        "formal_session": snap / "formal-Learning-Session.md",
        "formal_workbook": snap / "formal-Solved-Practice-Workbook.md",
        "canonical": snap / "canonical-Samkhya.md",
        "supplementary_complete": snap / "supplementary-complete-session.md",
        "supplementary_layered": snap / "supplementary-layered-session.md",
        "supplementary_workbook": snap / "supplementary-solved-workbook.md",
        "pyq_2018_2025": snap / "pyq-2018-2025.md",
        "pyq_2026": snap / "pyq-2026.md",
    }
    FORMAL_ROOT = snap
    errors: list[dict] = []
    checks: dict = {}
    validator_tree = ast.parse((root / "validate_package.py").read_text(encoding="utf-8"))
    prohibited_imports = []
    for node in ast.walk(validator_tree):
        if isinstance(node, ast.ImportFrom) and node.module in {"build_package", "question_bank"}:
            prohibited_imports.extend(alias.name for alias in node.names)
        if isinstance(node, ast.Import):
            prohibited_imports.extend(alias.name for alias in node.names
                                      if alias.name in {"build_package", "question_bank"})
    if prohibited_imports:
        fail(errors, "VALIDATOR_BUILDER_COUPLING", ",".join(prohibited_imports))
    for rel in REQUIRED:
        if not (root / rel).is_file():
            fail(errors, "MISSING_REQUIRED_FILE", rel)
    if (root / "pdf").exists() or (root / "PDF-MANIFEST.json").exists() or list(root.rglob("*.pdf")):
        fail(errors, "PDF_ARTIFACT_FORBIDDEN", "PDFs, pdf/, and PDF-MANIFEST.json are prohibited")
    checks["required_files"] = len(REQUIRED)
    checks["pdf_validation"] = "not_requested"
    if errors:
        return report(release, checks, errors)

    source_audit = load(root / "SOURCE-ARTIFACT-AUDIT.json")
    rows = source_audit.get("artifacts", [])
    amap = {row.get("file"): row for row in rows}
    if source_audit.get("status") != "CANONICAL_SOURCE_ARTIFACTS_CURRENT" or set(amap) != set(ARTIFACTS):
        fail(errors, "SOURCE_ARTIFACT_AUDIT_SCHEMA", "Artifact inventory or status differs")
    for rel in ARTIFACTS:
        p = root / rel
        row = amap.get(rel, {})
        if not p.is_file() or row.get("sha256") != sha_bytes(p.read_bytes()) or row.get("bytes") != p.stat().st_size:
            fail(errors, "SOURCE_ARTIFACT_STALE", rel)
    checks["source_artifacts"] = len(ARTIFACTS)

    review = load(root / "FORMAL-COVERAGE-REVIEW.json")
    audit = load(root / "FORMAL-COVERAGE-AUDIT.json")
    if review.get("authority_mode") != "formal_session_and_workbook_present":
        fail(errors, "AUTHORITY_MODE_MISMATCH", str(review.get("authority_mode")))
    forbidden_claims = ("canonical_without_" + "formal_session", "completed_formal_" + "session_found", "formal session was " + "found")
    for rel in ARTIFACTS:
        if rel.endswith((".md", ".json", ".py")) and (root / rel).is_file():
            text = (root / rel).read_text(encoding="utf-8", errors="replace")
            if any(claim in text for claim in forbidden_claims):
                fail(errors, "STALE_FORMAL_ABSENCE_CLAIM", rel)

    source_texts = {}
    for key, declared in review.get("sources", {}).items():
        expected_path = SOURCES.get(key)
        if expected_path is None or declared.get("path") != DECLARED_SOURCES.get(key):
            fail(errors, "SOURCE_IDENTITY_MISMATCH", key)
            continue
        if not expected_path.is_file():
            fail(errors, "SOURCE_FILE_MISSING", str(expected_path))
            continue
        if declared.get("sha256") != sha_bytes(expected_path.read_bytes()) or declared.get("bytes") != expected_path.stat().st_size:
            fail(errors, "SOURCE_HASH_MISMATCH", key)
            fail(errors, "SOURCE_SNAPSHOT_STALE", key)
        source_texts[key] = expected_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    for key, expected in FORMAL_EXPECTED.items():
        path = SOURCES[key]
        actual_lines = len(path.read_text(encoding="utf-8").splitlines()) if path.is_file() else 0
        actual_title = next((line[2:].strip() for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("# ")), "") if path.is_file() else ""
        recorded = review.get("formal_authorities", {}).get(key, {})
        if recorded.get("path") != DECLARED_SOURCES[key]:
            fail(errors, "FORMAL_EXACT_PATH_MISMATCH", key)
        if not path.is_file():
            fail(errors, "FORMAL_FILE_MISSING", key)
        elif sha_bytes(path.read_bytes()) != expected["sha256"] or actual_lines != expected["lines"]:
            fail(errors, "FORMAL_HASH_OR_LINE_IDENTITY", key)
        if actual_title != expected["title"] or recorded.get("actual_title") != expected["title"]:
            fail(errors, "FORMAL_TITLE_IDENTITY", key)
    if any(not SOURCES[key].is_file() for key in ("formal_session", "formal_workbook")):
        return report(release, checks, errors)

    for key, path in SOURCES.items():
        if not path.is_file():
            fail(errors, "SOURCE_SNAPSHOT_STALE", key)
    checks["source_identities"] = len(SOURCES)

    expected_blocks = {
        "formal_session": heading_blocks(SOURCES["formal_session"], "formal_session"),
        "formal_workbook": heading_blocks(SOURCES["formal_workbook"], "formal_workbook"),
        "canonical": heading_blocks(SOURCES["canonical"], "canonical"),
    }
    decisions = review.get("decisions", [])
    for stored_row in decisions:
        for mapping in stored_row.get("proposition_mappings", []):
            if incomplete_clause(mapping.get("exact_payload", "")):
                fail(errors, "INCOMPLETE_SOURCE_PAYLOAD",
                     f"{stored_row.get('id', 'missing-id')}:{mapping.get('proposition_id', 'missing-proposition')}")
    by_id = {row.get("id"): row for row in decisions}
    if len(by_id) != len(decisions):
        fail(errors, "BLOCK_ID_DUPLICATE", "Duplicate source-bound block IDs")
    if review.get("decision_count") != len(decisions) or review.get("unclassified_count") != 0:
        fail(errors, "FORMAL_MAPPING_COUNT", "Decision/unclassified count differs")
    for row in decisions:
        if row.get("validation_result") != "passed":
            fail(errors, "DECISION_VALIDATION_STATUS", row.get("id", "missing-id"))
    for panel in review.get("panels", []):
        if panel.get("validation_result") != "passed":
            fail(errors, "PANEL_VALIDATION_STATUS", panel.get("id", "missing-id"))
    special_inventories = review.get("special_inventories", {})
    expected_inventory_names = {"advanced_modules", "register_sections", "diagnostics", "formal_pyqs", "originals"}
    if set(special_inventories) != expected_inventory_names:
        fail(errors, "SPECIAL_INVENTORY_VALIDATION_STATUS", "Missing or unexpected special inventory")
    for inventory_name in expected_inventory_names:
        for row in special_inventories.get(inventory_name, []):
            if row.get("validation_result") != "passed":
                fail(errors, "SPECIAL_INVENTORY_VALIDATION_STATUS", f"{inventory_name}:{row.get('id', 'missing-id')}")
    mirror = (root / "FORMAL-SOURCE-MIRROR.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    revision = (root / "REVISION-GUIDE.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    raw = 0
    unique = {}
    baseline_raw = 0
    baseline_occurrences = Counter()
    expected_repairs = []
    exclusions = []
    per_source = defaultdict(lambda: {
        "raw": 0, "unique": set(), "occurrences": Counter(),
        "excluded": 0, "excluded_reasons": Counter(), "samples": [],
    })
    proposition_occurrences = Counter()
    expected_ids = set()
    for source, blocks in expected_blocks.items():
        expected_count_key = source + "_block_count"
        if review.get(expected_count_key) != len(blocks):
            fail(errors, "SOURCE_BLOCK_COUNT", f"{source}: expected {len(blocks)}")
        for actual in blocks:
            expected_ids.add(actual["id"])
            row = by_id.get(actual["id"])
            if not row or row.get("source") != source:
                fail(errors, "SOURCE_BLOCK_MISSING", actual["id"])
                continue
            payload = actual["_payload"]
            if row.get("own_payload_sha256") != sha_text(payload) or row.get("own_chars") != len(payload):
                fail(errors, "BLOCK_IDENTITY_OR_HASH_MISMATCH", actual["id"])
            if row.get("direct_children") != actual["direct_children"] or row.get("child_union_sha256") != actual["child_union_sha256"]:
                fail(errors, "CHILD_UNION_MISMATCH", actual["id"])
            if row.get("large_leaf_segments") != actual["large_leaf_segments"]:
                fail(errors, "LARGE_LEAF_MISMATCH", actual["id"])
            mirrored = anchor_payload(mirror, actual["id"])
            if mirrored is None or sha_text(mirrored) != sha_text(payload):
                fail(errors, "DESTINATION_PAYLOAD_HASH_MISMATCH", actual["id"])
            if source in {"formal_session", "canonical"}:
                learned = anchor_payload(revision, actual["id"])
                if learned is None or sha_text(learned) != sha_text(payload):
                    fail(errors, "LEARNER_FORMAL_PAYLOAD_MISMATCH", actual["id"])
            try:
                units, excluded, repairs = semantic_units(payload, include_repairs=True)
                original_units, _ = semantic_units(payload, apply_repairs=False)
                baseline_raw += len(original_units)
                baseline_occurrences.update("prop-" + sha_text(norm(unit))[:20] for unit in original_units)
                expected_repairs.extend({"source": source, "block_id": actual["id"], **repair} for repair in repairs)
            except ValueError as exc:
                fail(errors, "INCOMPLETE_SOURCE_PAYLOAD", f"{actual['id']}:{exc}")
                units, excluded = [], []
            mappings = row.get("proposition_mappings", [])
            headers = set(table_header_lines(payload))
            if any(mapping.get("exact_payload") in headers for mapping in mappings):
                fail(errors, "TABLE_HEADER_STRUCTURAL_INFLATION", actual["id"])
            for mapping in mappings:
                if structural_reason(mapping.get("exact_payload", "")):
                    fail(errors, proposition_inflation_code(mapping.get("exact_payload", "")), actual["id"])
            if len(units) != len(mappings):
                fail(errors, "SEMANTIC_PROPOSITION_COUNT", actual["id"])
            expected_excluded = [{"source_block_id": actual["id"], **item} for item in excluded]
            if row.get("excluded_non_propositional_fragments") != expected_excluded:
                fail(errors, "EXCLUDED_FRAGMENT_ACCOUNTING_TAMPER", actual["id"])
            for item in row.get("excluded_non_propositional_fragments", []):
                if item.get("exact_payload_sha256") != sha_text(item.get("exact_payload", "")):
                    fail(errors, "EXCLUDED_FRAGMENT_HASH_MISMATCH", actual["id"])
            for header in headers:
                if not any(item["exact_payload"] == header and item["reason"] == "table_header_scaffolding"
                           for item in excluded):
                    fail(errors, "TABLE_HEADER_CLASSIFICATION_MISMATCH", actual["id"])
            exclusions.extend(expected_excluded)
            per_source[source]["excluded"] += len(expected_excluded)
            per_source[source]["excluded_reasons"].update(item["reason"] for item in expected_excluded)
            for i, (unit, mapping) in enumerate(zip(units, mappings), 1):
                pid = "prop-" + sha_text(norm(unit))[:20]
                if structural_reason(mapping.get("exact_payload", "")):
                    fail(errors, proposition_inflation_code(mapping.get("exact_payload", "")), actual["id"])
                if mapping.get("occurrence") != i or mapping.get("proposition_id") != pid or mapping.get("exact_payload") != unit:
                    fail(errors, "SEMANTIC_PROPOSITION_REFERENCE_TAMPER", f"{actual['id']}:{i}")
                raw += 1
                unique[pid] = unit
                proposition_occurrences[pid] += 1
                per_source[source]["raw"] += 1
                per_source[source]["unique"].add(pid)
                per_source[source]["occurrences"][pid] += 1
                if len(per_source[source]["samples"]) < 3 and deterministic_sample_candidate(unit):
                    per_source[source]["samples"].append({
                        "block_id": actual["id"], "proposition_id": pid,
                        "payload_sha256": sha_text(unit), "payload": unit,
                    })
    for row in decisions:
        if row.get("classification") != "supplementary_depth":
            continue
        expected_ids.add(row["id"])
        payload = anchor_payload(mirror, row["id"])
        if payload is None or sha_text(payload) != row.get("own_payload_sha256"):
            fail(errors, "SUPPLEMENTARY_PAYLOAD_MISMATCH", row["id"])
            continue
        try:
            units, excluded, repairs = semantic_units(payload, include_repairs=True)
            original_units, _ = semantic_units(payload, apply_repairs=False)
            baseline_raw += len(original_units)
            baseline_occurrences.update("prop-" + sha_text(norm(unit))[:20] for unit in original_units)
            expected_repairs.extend({"source": row["source"], "block_id": row["id"], **repair} for repair in repairs)
        except ValueError as exc:
            fail(errors, "INCOMPLETE_SOURCE_PAYLOAD", f"{row['id']}:{exc}")
            units, excluded = [], []
        mappings = row.get("proposition_mappings", [])
        headers = set(table_header_lines(payload))
        if any(mapping.get("exact_payload") in headers for mapping in mappings):
            fail(errors, "TABLE_HEADER_STRUCTURAL_INFLATION", row["id"])
        for mapping in mappings:
            if structural_reason(mapping.get("exact_payload", "")):
                fail(errors, proposition_inflation_code(mapping.get("exact_payload", "")), row["id"])
        if len(units) != len(mappings):
            fail(errors, "SEMANTIC_PROPOSITION_COUNT", row["id"])
        expected_excluded = [{"source_block_id": row["id"], **item} for item in excluded]
        if row.get("excluded_non_propositional_fragments") != expected_excluded:
            fail(errors, "EXCLUDED_FRAGMENT_ACCOUNTING_TAMPER", row["id"])
        for item in row.get("excluded_non_propositional_fragments", []):
            if item.get("exact_payload_sha256") != sha_text(item.get("exact_payload", "")):
                fail(errors, "EXCLUDED_FRAGMENT_HASH_MISMATCH", row["id"])
        for header in headers:
            if not any(item["exact_payload"] == header and item["reason"] == "table_header_scaffolding"
                       for item in excluded):
                fail(errors, "TABLE_HEADER_CLASSIFICATION_MISMATCH", row["id"])
        exclusions.extend(expected_excluded)
        per_source[row["source"]]["excluded"] += len(expected_excluded)
        per_source[row["source"]]["excluded_reasons"].update(item["reason"] for item in expected_excluded)
        for i, (unit, mapping) in enumerate(zip(units, mappings), 1):
            pid = "prop-" + sha_text(norm(unit))[:20]
            if structural_reason(mapping.get("exact_payload", "")):
                fail(errors, proposition_inflation_code(mapping.get("exact_payload", "")), row["id"])
            if mapping.get("occurrence") != i or mapping.get("proposition_id") != pid or mapping.get("exact_payload") != unit:
                fail(errors, "SEMANTIC_PROPOSITION_REFERENCE_TAMPER", f"{row['id']}:{i}")
            raw += 1
            unique[pid] = unit
            proposition_occurrences[pid] += 1
            per_source[row["source"]]["raw"] += 1
            per_source[row["source"]]["unique"].add(pid)
            per_source[row["source"]]["occurrences"][pid] += 1
            if len(per_source[row["source"]]["samples"]) < 3 and deterministic_sample_candidate(unit):
                per_source[row["source"]]["samples"].append({
                    "block_id": row["id"], "proposition_id": pid,
                    "payload_sha256": sha_text(unit), "payload": unit,
                })
    if set(by_id) != expected_ids:
        fail(errors, "SOURCE_BLOCK_SET_MISMATCH", "Unexpected or absent formal/canonical/supplementary rows")
    if raw != review.get("raw_proposition_mapping_count") or len(unique) != review.get("unique_normalized_proposition_count"):
        fail(errors, "SEMANTIC_TOTAL_MISMATCH", f"raw={raw}, unique={len(unique)}")
    if raw - len(unique) != review.get("duplicate_occurrences_deduplicated"):
        fail(errors, "DUPLICATE_ACCOUNTING_MISMATCH", "Duplicate occurrence count differs")
    if raw - review.get("duplicate_occurrences_deduplicated", -1) != len(unique):
        fail(errors, "DUPLICATE_ACCOUNTING_MISMATCH", "raw - duplicate_occurrences must equal unique")
    if sum(count > 1 for count in proposition_occurrences.values()) != review.get("duplicate_group_count"):
        fail(errors, "DUPLICATE_ACCOUNTING_MISMATCH", "Duplicate group count differs")
    recorded_repairs = review.get("normalization_repairs")
    if recorded_repairs != expected_repairs:
        fail(errors, "NORMALIZATION_REPAIR_BINDING_MISMATCH",
             "Recorded repairs do not match adjacent original units in their bound blocks")
    if {row.get("joined_normalized_sha256") for row in expected_repairs} != TARGETED_CONTIGUOUS_JOIN_HASHES:
        fail(errors, "NORMALIZATION_REPAIR_ALLOWLIST_MISMATCH", "Approved join hashes are missing or unused")
    for repair in expected_repairs:
        if repair["right_original_ordinal"] != repair["left_original_ordinal"] + 1:
            fail(errors, "NORMALIZATION_REPAIR_NONADJACENT", repair["block_id"])
        if incomplete_syntax_reason(repair["left_exact_payload"]) != repair["reason"]:
            fail(errors, "NORMALIZATION_REPAIR_SYNTAX_MISMATCH", repair["block_id"])
        if repair["joined_payload"] != f"{repair['left_exact_payload']} {repair['right_exact_payload']}".strip():
            fail(errors, "NORMALIZATION_REPAIR_PAYLOAD_MISMATCH", repair["block_id"])
        if repair["joined_payload_sha256"] != sha_text(repair["joined_payload"]):
            fail(errors, "NORMALIZATION_REPAIR_HASH_MISMATCH", repair["block_id"])
        if repair["joined_normalized_sha256"] != sha_text(norm(repair["joined_payload"])):
            fail(errors, "NORMALIZATION_REPAIR_HASH_MISMATCH", repair["block_id"])
        expected_old_ids = [
            "prop-" + sha_text(norm(repair["left_exact_payload"]))[:20],
            "prop-" + sha_text(norm(repair["right_exact_payload"]))[:20],
        ]
        if repair["old_proposition_ids"] != expected_old_ids:
            fail(errors, "NORMALIZATION_REPAIR_ID_MISMATCH", repair["block_id"])
        if repair["new_proposition_id"] != "prop-" + repair["joined_normalized_sha256"][:20]:
            fail(errors, "NORMALIZATION_REPAIR_ID_MISMATCH", repair["block_id"])
    baseline = {
        "raw_proposition_mapping_count": baseline_raw,
        "unique_normalized_proposition_count": len(baseline_occurrences),
        "duplicate_occurrences_deduplicated": baseline_raw - len(baseline_occurrences),
        "duplicate_group_count": sum(count > 1 for count in baseline_occurrences.values()),
        "excluded_fragment_count": len(exclusions),
    }
    cleared_baseline = {
        "raw_proposition_mapping_count": 2721,
        "unique_normalized_proposition_count": 2497,
        "duplicate_occurrences_deduplicated": 224,
        "duplicate_group_count": 222,
        "excluded_fragment_count": 1762,
    }
    if baseline != cleared_baseline or review.get("normalization_baseline") != baseline:
        fail(errors, "NORMALIZATION_BASELINE_DRIFT", str(baseline))
    semantic_delta = {
        "raw_proposition_mapping_count": raw - baseline_raw,
        "unique_normalized_proposition_count": len(unique) - len(baseline_occurrences),
        "duplicate_occurrences_deduplicated":
            (raw - len(unique)) - (baseline_raw - len(baseline_occurrences)),
        "duplicate_group_count":
            sum(count > 1 for count in proposition_occurrences.values())
            - sum(count > 1 for count in baseline_occurrences.values()),
        "excluded_fragment_count": len(exclusions) - baseline["excluded_fragment_count"],
    }
    if review.get("normalization_semantic_delta") != semantic_delta:
        fail(errors, "UNRECORDED_NORMALIZATION_DELTA", str(semantic_delta))
    if semantic_delta["raw_proposition_mapping_count"] != -len(expected_repairs):
        fail(errors, "UNRECORDED_NORMALIZATION_DELTA", "Raw delta is not exactly one per recorded join")
    if len(exclusions) != review.get("excluded_fragment_count"):
        fail(errors, "EXCLUDED_TOTAL_MISMATCH", str(len(exclusions)))
    actual_reason_counts = dict(Counter(item["reason"] for item in exclusions))
    expected_exclusion_reasons = {
        "heading_coordinate": 470, "table_header_scaffolding": 53, "table_separator": 53,
        "package_composition_metadata": 13, "fence_coordinate": 88, "diagram_border": 120,
        "diagram_column_header": 51, "symbol_fragment": 63, "visual_label_coordinate": 33,
        "blank_or_fence": 92, "answer_key_coordinate": 139, "mcq_option_coordinate": 520,
        "yaml_or_separator": 36, "diagram_heading_coordinate": 14, "panel_label_coordinate": 14,
        "boundary_caption_coordinate": 1, "parenthetical_routing_instruction": 1,
        "answer_or_explanation_coordinate": 1,
    }
    if actual_reason_counts != expected_exclusion_reasons:
        fail(errors, "STRUCTURAL_EXCLUSION_BASELINE_DRIFT", str(actual_reason_counts))
    if review.get("excluded_fragment_reason_counts") != actual_reason_counts:
        fail(errors, "EXCLUDED_REASON_COUNT_MISMATCH", "Excluded reason counts differ")
    breakdown = review.get("source_proposition_breakdown", {})
    if set(breakdown) != set(per_source):
        fail(errors, "SOURCE_GLOBAL_TOTAL_MISMATCH", "Source breakdown keys differ")
    if sum(row.get("raw_mappings", 0) for row in breakdown.values()) != review.get("raw_proposition_mapping_count"):
        fail(errors, "SOURCE_GLOBAL_TOTAL_MISMATCH", "Stored source raw totals do not sum to stored global raw")
    if sum(row.get("excluded_structural_coordinates", 0) for row in breakdown.values()) != review.get("excluded_fragment_count"):
        fail(errors, "SOURCE_GLOBAL_TOTAL_MISMATCH", "Stored source excluded totals do not sum to stored global excluded")
    for source, stats in per_source.items():
        row = breakdown.get(source, {})
        expected_source_accounting = (
            stats["raw"], len(stats["unique"]), stats["raw"] - len(stats["unique"]),
            sum(count > 1 for count in stats["occurrences"].values()),
            stats["excluded"], dict(stats["excluded_reasons"]),
        )
        recorded_source_accounting = (
            row.get("raw_mappings"), row.get("source_unique_normalized"),
            row.get("duplicate_occurrences"), row.get("duplicate_groups"),
            row.get("excluded_structural_coordinates"), row.get("excluded_reason_counts"),
        )
        if recorded_source_accounting != expected_source_accounting:
            fail(errors, "SOURCE_SPECIFIC_PROPOSITION_OMISSION", source)
        samples = row.get("deterministic_payload_samples", [])
        if samples != stats["samples"]:
            fail(errors, "SOURCE_PROPOSITION_SAMPLE_TAMPER", source)
    if sum(stats["raw"] for stats in per_source.values()) != raw:
        fail(errors, "SOURCE_GLOBAL_TOTAL_MISMATCH", "Source raw totals do not sum to global raw")
    if sum(stats["excluded"] for stats in per_source.values()) != len(exclusions):
        fail(errors, "SOURCE_GLOBAL_TOTAL_MISMATCH", "Source excluded totals do not sum to global excluded")

    expected_panels = []
    for source in ("formal_session", "formal_workbook", "canonical"):
        expected_panels.extend(extract_panels(SOURCES[source], source))
    for row in decisions:
        if row.get("classification") != "supplementary_depth":
            continue
        payload = anchor_payload(mirror, row["id"]) or ""
        for i, m in enumerate(re.finditer(r"```[^\n]*\n.*?\n```", payload, re.S), 1):
            panel = m.group(0); expected_panels.append({"id": f"{row['id']}-diagram-{i}", "payload_sha256": sha_text(panel), "chars": len(panel)})
        for i, m in enumerate(re.finditer(r"(?m)(?:^\|.*\|\n){2,}", payload), 1):
            panel = m.group(0).rstrip() + "\n"; expected_panels.append({"id": f"{row['id']}-table-{i}", "payload_sha256": sha_text(panel), "chars": len(panel)})
    recorded_panels = {x.get("id"): x for x in review.get("panels", [])}
    for panel in expected_panels:
        row = recorded_panels.get(panel["id"])
        if not row or row.get("payload_sha256") != panel["payload_sha256"] or row.get("chars") != panel["chars"]:
            fail(errors, "PANEL_PARITY_MISMATCH", panel["id"])
    if len(recorded_panels) != len(expected_panels):
        fail(errors, "PANEL_COUNT_MISMATCH", str(len(recorded_panels)))
    formal_session_blocks = expected_blocks["formal_session"]
    formal_workbook_blocks = expected_blocks["formal_workbook"]
    advanced = sum("ADVANCED MODULE" in row["heading"] for row in formal_session_blocks)
    registers = sum(bool(re.match(r"^[A-N]\.\s", row["heading"])) for row in formal_session_blocks)
    diagnostics = sum(bool(re.match(r"MCQ\s+\d+\.", row["heading"])) for row in formal_workbook_blocks)
    master_flows = sum("ASCII MASTER FLOW — PANEL" in row["heading"] for row in formal_session_blocks)
    if (advanced, registers, diagnostics, master_flows) != (3, 14, 32, 14):
        fail(errors, "FORMAL_STRUCTURAL_IDENTITY", f"advanced={advanced}, registers={registers}, diagnostics={diagnostics}, master={master_flows}")
    if (audit.get("advanced_modules"), audit.get("register_sections"), audit.get("workbook_diagnostics"),
        audit.get("master_flow_panels")) != (advanced, registers, diagnostics, master_flows):
        fail(errors, "FORMAL_STRUCTURAL_IDENTITY", "Stored structural metrics differ from bound sources")
    expected_special_ids = {
        "advanced_modules": [row["id"] for row in formal_session_blocks if "ADVANCED MODULE" in row["heading"]],
        "register_sections": [row["id"] for row in formal_session_blocks if re.match(r"^[A-N]\.\s", row["heading"])],
        "diagnostics": [row["id"] for row in formal_workbook_blocks if re.match(r"MCQ\s+\d+\.", row["heading"])],
    }
    for inventory_name, ids in expected_special_ids.items():
        if [row.get("id") for row in special_inventories.get(inventory_name, [])] != ids:
            fail(errors, "SPECIAL_INVENTORY_IDENTITY", inventory_name)
    checks.update({"formal_session_blocks": len(formal_session_blocks), "formal_workbook_blocks": len(formal_workbook_blocks),
                   "canonical_blocks": len(expected_blocks["canonical"]), "supplementary_units": review.get("supplementary_unit_count"),
                   "panels": len(expected_panels), "master_flow_panels": master_flows, "advanced_modules": advanced,
                   "register_sections": registers, "workbook_diagnostics": diagnostics,
                   "large_leaves": review.get("large_leaf_count"), "large_leaf_segments": review.get("large_leaf_segment_count"),
                   "raw_propositions": raw, "unique_propositions": len(unique),
                   "duplicate_occurrences": raw - len(unique), "duplicate_groups": review.get("duplicate_group_count"),
                   "excluded_coordinates": len(exclusions),
                   "source_proposition_breakdown": {
                       k: {
                           "raw": v["raw"], "unique": len(v["unique"]),
                           "duplicate_occurrences": v["raw"] - len(v["unique"]),
                           "duplicate_groups": sum(count > 1 for count in v["occurrences"].values()),
                           "excluded": v["excluded"], "excluded_reason_counts": dict(v["excluded_reasons"]),
                       }
                       for k, v in per_source.items()
                   }})

    derivation_rows = []
    for source in ("canonical", "formal_session", "formal_workbook"):
        for block in expected_blocks[source]:
            row = dict(block); units, excluded = semantic_units(row["_payload"])
            row["proposition_mappings"] = [{"source_block_id": row["id"], "occurrence": i,
                "proposition_id": "prop-" + sha_text(norm(unit))[:20],
                "exact_payload_sha256": sha_text(unit), "exact_payload": unit}
                for i, unit in enumerate(units, 1)]
            derivation_rows.append(row)

    classification = load(root / "AUTHORITY-CLASSIFICATION.json")
    forbidden_keys = {"authoring_handle", "authoring_key", "cell_id", "cell_title", "probe_count", "minimum_probes",
                      "answer", "answer_key", "question_id", "question_binding", "probe_mode", "probe_modes", "mapped_question_ids"}
    leaked = []
    def inspect_classification(value, path=""):
        if isinstance(value, dict):
            for key, child in value.items():
                if key in forbidden_keys: leaked.append(path + "." + key)
                inspect_classification(child, path + "." + key)
        elif isinstance(value, list):
            for i, child in enumerate(value): inspect_classification(child, f"{path}[{i}]")
        elif isinstance(value, str) and re.search(r"SK-TM-\d+", value): leaked.append(path + ":SK-TM")
    inspect_classification(classification)
    if leaked: fail(errors, "CLASSIFICATION_AUTHORING_HANDLE_LEAK", ",".join(leaked[:8]))
    core = {k: v for k, v in classification.items() if k != "classification_hash"}
    computed_classification_hash = sha_text(json.dumps(core, ensure_ascii=False, sort_keys=True))
    if classification.get("classification_hash") != computed_classification_hash:
        fail(errors, "CLASSIFICATION_HASH_DRIFT", "Frozen classification self-hash differs while source hashes remain fixed")
    if classification.get("build_execution_order") != ["parse_and_normalize_sources", "classify_source_obligations", "freeze_classification_artifact"]:
        fail(errors, "CLASSIFICATION_EXECUTION_ORDER", str(classification.get("build_execution_order")))
    for source in ("formal_session", "formal_workbook", "canonical"):
        manifest = classification.get("source_manifest", {}).get(source, {})
        path = SOURCES[source]
        if manifest.get("sha256") != sha_bytes(path.read_bytes()) or manifest.get("bytes") != path.stat().st_size:
            fail(errors, "CLASSIFICATION_SOURCE_HASH_DRIFT", source)
    rules = classification.get("classification_rules", [])
    if any(set(rule) - {"rule_id", "predicate", "substantive_category", "rationale", "rule_hash"} for rule in rules):
        fail(errors, "CLASSIFICATION_RULE_SCHEMA", "Classification rules contain non-source fields")
    if any("doctrine-specific" not in norm(rule.get("rationale", "")) for rule in rules):
        fail(errors, "CLASSIFICATION_GENERIC_FALLBACK", "Testable rules require doctrine-specific rationale")
    if classification.get("classification_rule_set_hash") != sha_text(json.dumps(rules, ensure_ascii=False, sort_keys=True)):
        fail(errors, "CLASSIFICATION_RULE_SET_HASH_DRIFT", "Rule-set hash differs")

    def source_block_ref(source: str, payload_hash: str) -> str:
        return "SK-SRC-" + source.upper().replace("_", "-") + "-" + payload_hash[:16].upper()

    valid_blocks = {source_block_ref(row["source"], row["own_payload_sha256"]): row for row in derivation_rows}
    occurrences = defaultdict(list)
    for row in derivation_rows:
        for mapping in row["proposition_mappings"]:
            occurrences[mapping["proposition_id"]].append((row, mapping))
    priority = {"canonical": 0, "formal_session": 1, "formal_workbook": 2}
    representatives = {pid: sorted(items, key=lambda x: (priority[x[0]["source"]], x[0]["id"], x[1]["occurrence"]))[0] for pid, items in occurrences.items()}
    rules_by_hash = {}
    for rule in rules:
        pred = rule.get("predicate", {}); ph = pred.get("normalized_proposition_sha256")
        matches = [(pid, row, mapping) for pid, (row, mapping) in representatives.items()
                   if row["source"] == pred.get("authority_source")
                   and sha_text(norm(mapping["exact_payload"])) == ph]
        if len(matches) != 1: fail(errors, "CLASSIFICATION_SOURCE_PREDICATE_MISMATCH", rule.get("rule_id", "missing")); continue
        if ph in rules_by_hash: fail(errors, "CLASSIFICATION_SOURCE_PREDICATE_MISMATCH", "duplicate testable proposition")
        body = {k: rule.get(k) for k in ("rule_id", "predicate", "substantive_category", "rationale")}
        if rule.get("rule_hash") != sha_text(json.dumps(body, ensure_ascii=False, sort_keys=True)):
            fail(errors, "CLASSIFICATION_RULE_HASH_DRIFT", rule.get("rule_id", "missing"))
        rules_by_hash[ph] = rule

    class_rows = classification.get("rows", [])
    by_oid = {row.get("obligation_id"): row for row in class_rows}
    if len(by_oid) != len(class_rows): fail(errors, "CLASSIFICATION_DUPLICATE_OBLIGATION", "Duplicate obligation IDs")
    proposition_payloads = {pid: mapping["exact_payload"] for pid, (_, mapping) in representatives.items()}
    atomic_rows = [row for row in class_rows if row.get("classification") == "testable_atomic"]
    block_atomic_ids = defaultdict(list)
    for atomic in atomic_rows:
        for block_id in atomic.get("authority_block_ids", []):
            block_atomic_ids[block_id].append(atomic["obligation_id"])
    category_counts = Counter(); class_counts = Counter(); primary_by_pid = {}
    for pid, (block, mapping) in representatives.items():
        ph = sha_text(norm(mapping["exact_payload"])); rule = rules_by_hash.get(ph)
        expected_class = "testable_atomic" if rule else "supporting_non_testable_context"
        oid = "SK-OBL-" + sha_text(f"{expected_class}|{pid}")[:16].upper(); primary_by_pid[pid] = oid
        row = by_oid.get(oid)
        if not row: fail(errors, "OBLIGATION_OMISSION", oid); continue
        if rule:
            expected = (rule["substantive_category"], rule["predicate"], rule["rationale"], rule["rule_id"], rule["rule_hash"])
        else:
            try:
                block_ref = source_block_ref(block["source"], block["own_payload_sha256"])
                decision = independent_supporting_classification(
                    mapping["exact_payload"], atomic_rows, proposition_payloads,
                    block_atomic_ids.get(block_ref, [])
                )
            except ValueError:
                fail(errors, "CLASSIFICATION_UNSUPPORTED_FALLBACK", oid)
                continue
            cat = decision["substantive_category"]; pred = decision["classification_predicate"]; why = decision["classification_rationale"]
            rid = "SK-SUPPORT-" + cat.upper().replace("_", "-")
            rhash = sha_text(json.dumps({"rule_id": rid, "category": cat, "predicate": pred, "rationale": why}, ensure_ascii=False, sort_keys=True))
            expected = (cat, pred, why, rid, rhash)
        actual = (row.get("substantive_category"), row.get("classification_predicate"), row.get("classification_rationale"), row.get("classification_rule_id"), row.get("classification_rule_hash"))
        if actual != expected: fail(errors, "CLASSIFICATION_SOURCE_ONLY_MISMATCH", oid)
        if row.get("classification") != expected_class: fail(errors, "OBLIGATION_CLASSIFICATION_INVALID", oid)
        if row.get("authority_block_ids") != [source_block_ref(block["source"], block["own_payload_sha256"])]: fail(errors, "OBLIGATION_AUTHORITY_BLOCK_REFERENCE_INVALID", oid)
        if row.get("source_payload_hashes") != {"block_sha256": block["own_payload_sha256"], "proposition_sha256": mapping["exact_payload_sha256"]}: fail(errors, "OBLIGATION_HASH_DRIFT", oid)
    represented_blocks = {block["id"] for block, _ in representatives.values()}
    for pid, items in occurrences.items():
        representative = representatives[pid]
        for block, mapping in sorted(items, key=lambda x: (priority[x[0]["source"]], x[0]["id"], x[1]["occurrence"])):
            if (block, mapping) == representative:
                continue
            represented_blocks.add(block["id"])
            oid = "SK-OBL-DUP-" + sha_text(
                f"{pid}|{block['source']}|{block['id']}|{mapping['occurrence']}"
            )[:16].upper()
            row = by_oid.get(oid)
            if not row:
                fail(errors, "OBLIGATION_OMISSION", oid)
                continue
            if row.get("classification") != "normalized_duplicate" or row.get("substantive_category") != "duplicate_route":
                fail(errors, "CLASSIFICATION_SOURCE_ONLY_MISMATCH", oid)
            if row.get("classification_predicate") != {
                "same_normalized_proposition_id": pid,
                "routes_to_obligation_id": primary_by_pid[pid],
            }:
                fail(errors, "DUPLICATE_ROUTE_MISMATCH", oid)
    for block in derivation_rows:
        if block["id"] in represented_blocks:
            continue
        oid = "SK-OBL-BLOCK-" + sha_text(block["id"])[:16].upper()
        row = by_oid.get(oid)
        if not row or row.get("substantive_category") != "empty_structural_block":
            fail(errors, "CLASSIFICATION_SOURCE_ONLY_MISMATCH", oid)
    for row in class_rows:
        class_counts[row.get("classification")] += 1; category_counts[row.get("substantive_category")] += 1
        if row.get("classification") == "supporting_non_testable_context" and row.get("substantive_category") in {None, "generic", "default", "supporting"}:
            fail(errors, "CLASSIFICATION_GENERIC_FALLBACK", row.get("obligation_id", "missing"))
        if row.get("classification") == "supporting_non_testable_context":
            if row.get("substantive_category") == "empty_structural_block":
                if row.get("proposition_ids") or row.get("classification_predicate") != {"valid_semantic_proposition_count": 0}:
                    fail(errors, "EMPTY_STRUCTURAL_EVIDENCE_INVALID", row.get("obligation_id", "missing"))
                continue
            pred = row.get("classification_predicate", {})
            represented = pred.get("represented_by_obligation_ids")
            non_testability = pred.get("non_testability_category")
            if bool(represented) == bool(non_testability):
                fail(errors, "SUPPORTING_STRUCTURE_INVALID", row.get("obligation_id", "missing"))
            if represented:
                relation_type = pred.get("relation_type")
                if relation_type not in {"entailed_by", "subsumed_by", "composite_split"}:
                    fail(errors, "SUPPORTING_RELATION_INVALID", row.get("obligation_id", "missing"))
                source_payload = proposition_payloads.get(row.get("proposition_ids", [""])[0], "")
                if relation_type == "composite_split":
                    contract = pred.get("source_component_contract", {})
                    components = pred.get("components", [])
                    expected_count = contract.get("expected_component_count")
                    expected_by_kind = {
                        "three_pramanas_plus_five_named_reductions": 6,
                        "five_anti_theistic_arguments": 5,
                    }
                    if (expected_by_kind.get(contract.get("kind")) != expected_count
                            or len(components) != expected_count):
                        fail(errors, "SUPPORTING_COMPOSITE_COMPONENT_MISSING", row.get("obligation_id", "missing"))
                    covered_ids = []
                    for component in components:
                        component_text = component.get("component_text", "")
                        if component.get("component_sha256") != sha_text(norm(component_text)):
                            fail(errors, "SUPPORTING_COMPOSITE_COMPONENT_INVALID", row.get("obligation_id", "missing"))
                        target_ids = component.get("target_obligation_ids", [])
                        anchors = component.get("doctrine_anchors", [])
                        if not target_ids or [x.get("obligation_id") for x in anchors] != target_ids:
                            fail(errors, "SUPPORTING_COMPOSITE_COMPONENT_INVALID", row.get("obligation_id", "missing"))
                        covered_ids.extend(target_ids)
                        for anchor in anchors:
                            target = by_oid.get(anchor.get("obligation_id"), {})
                            target_payload = proposition_payloads.get(target.get("proposition_ids", [""])[0], "")
                            terms = anchor.get("shared_doctrine_terms", [])
                            if target.get("classification") != "testable_atomic" or len(terms) < 2 or any(
                                term in RELATION_STOP or term in GENERIC_RELATION_TERMS
                                or term not in relation_tokens(component_text)
                                or term not in relation_tokens(target_payload) for term in terms
                            ):
                                fail(errors, "SUPPORTING_SEMANTIC_RELATION_INVALID", row.get("obligation_id", "missing"))
                    if sorted(set(covered_ids)) != sorted(set(represented)):
                        fail(errors, "SUPPORTING_COMPOSITE_COMPONENT_MISSING", row.get("obligation_id", "missing"))
                else:
                    anchors = pred.get("doctrine_specific_anchors", [])
                    if [x.get("obligation_id") for x in anchors] != represented:
                        fail(errors, "SUPPORTING_REPRESENTATION_INVALID", row.get("obligation_id", "missing"))
                    for anchor in anchors:
                        target = by_oid.get(anchor.get("obligation_id"), {})
                        terms = anchor.get("shared_doctrine_terms", [])
                        target_payload = proposition_payloads.get(target.get("proposition_ids", [""])[0], "")
                        if target.get("classification") != "testable_atomic" or len(terms) < 2 or any(
                            term in RELATION_STOP or term in GENERIC_RELATION_TERMS
                            or term not in relation_tokens(source_payload)
                            or term not in relation_tokens(target_payload) for term in terms
                        ):
                            fail(errors, "SUPPORTING_SEMANTIC_RELATION_INVALID", row.get("obligation_id", "missing"))
            elif non_testability not in {
                "example_only", "source_attribution_or_citation_only", "answer_writing_or_meta",
                "chronology_or_context_only", "qualification_dependent_on_atomic_claim",
                "non_atomic_composite", "repeated_implication", "non_atomic_context",
            }:
                fail(errors, "SUPPORTING_NON_TESTABILITY_INVALID", row.get("obligation_id", "missing"))
            elif non_testability in {
                "qualification_dependent_on_atomic_claim", "non_atomic_composite", "repeated_implication"
            }:
                named = pred.get("named_atomic_ids", [])
                if not named or any(by_oid.get(oid, {}).get("classification") != "testable_atomic" for oid in named):
                    fail(errors, "SUPPORTING_REPRESENTATION_INVALID", row.get("obligation_id", "missing"))
    if dict(class_counts) != classification.get("classification_counts") or dict(category_counts) != classification.get("substantive_category_counts"):
        fail(errors, "CLASSIFICATION_TOTAL_MISMATCH", "Stored classification/category totals differ")
    if len(category_counts) < 8: fail(errors, "CLASSIFICATION_GENERIC_FALLBACK", f"Only {len(category_counts)} substantive categories")

    obligation_ledger = load(root / "AUTHORITY-OBLIGATION-LEDGER.json")
    actual_obligations = {row.get("obligation_id"): row for row in obligation_ledger.get("obligations", [])}
    expected_obligations = by_oid
    if set(actual_obligations) != set(expected_obligations): fail(errors, "OBLIGATION_OMISSION", "Ledger/classification obligation sets differ")
    valid_props = {mapping["proposition_id"] for row in derivation_rows for mapping in row["proposition_mappings"]}
    for oid, source_row in expected_obligations.items():
        ledger_row = actual_obligations.get(oid, {})
        for block_id in ledger_row.get("authority_block_ids", []):
            if block_id not in valid_blocks:
                fail(errors, "OBLIGATION_AUTHORITY_BLOCK_REFERENCE_INVALID", f"{oid}:{block_id}")
        for proposition_id in ledger_row.get("proposition_ids", []):
            if proposition_id not in valid_props:
                fail(errors, "OBLIGATION_PROPOSITION_REFERENCE_INVALID", f"{oid}:{proposition_id}")
        for key, value in source_row.items():
            if ledger_row.get(key) != value:
                code = {
                    "source_payload_hashes": "OBLIGATION_HASH_DRIFT",
                    "classification_rule_id": "OBLIGATION_RULE_ID_DRIFT",
                    "classification_rule_hash": "OBLIGATION_RULE_HASH_DRIFT",
                    "classification_rationale": "OBLIGATION_RULE_RATIONALE_DRIFT",
                }.get(key, "OBLIGATION_LEDGER_MISMATCH")
                fail(errors, code, f"{oid}:{key}")
        if ledger_row.get("validation_result") != "passed": fail(errors, "OBLIGATION_VALIDATION_STATUS", oid)
    if obligation_ledger.get("classification_hash") != classification.get("classification_hash"):
        fail(errors, "CLASSIFICATION_HASH_DRIFT", "Ledger is not bound to frozen classification")
    if obligation_ledger.get("classification_counts") != classification.get("classification_counts") or obligation_ledger.get("substantive_category_counts") != classification.get("substantive_category_counts"):
        fail(errors, "OBLIGATION_LEDGER_MISMATCH", "Classification summaries differ")
    route = actual_obligations.get("YG-SK-BOUNDARY-001")
    if not route or route.get("classification") != "routed_boundary" or route.get("route") != {"target_topic":"06-Yoga","target_edited":True,"due_within_samkhya":False,"ownership":"cross-link-only"}:
        fail(errors, "YOGA_ROUTE_OBLIGATION_MISMATCH", "YG-SK-BOUNDARY-001")
    checks["classification_hash"] = classification.get("classification_hash")
    checks["obligation_count"] = obligation_ledger.get("obligation_count")
    checks["obligation_classifications"] = classification.get("classification_counts")
    checks["classification_categories"] = classification.get("substantive_category_counts")
    checks["authority_derivation_question_independent"] = not leaked
    checks["validator_builder_imports"] = []
    if obligation_ledger.get("represented_mandatory_formal_block_count") != 337:
        fail(errors, "MANDATORY_FORMAL_BLOCK_REPRESENTATION", str(obligation_ledger.get("represented_mandatory_formal_block_count")))
    checks["represented_mandatory_formal_blocks"] = obligation_ledger.get("represented_mandatory_formal_block_count")

    matrix = load(root / "TEST-MATRIX.json")
    qdoc = parse_mcqs((root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8"))
    sdoc = parse_mcqs((root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"))
    forbidden_titles = {
        norm(title) for title in
        [row.get("title", "") for row in matrix.get("cells", [])]
        + [row.get("title", "") for row in qdoc.values()]
        + [row.get("title", "") for row in sdoc.values()]
        if len(norm(title)) >= 5
    }
    prose = [
        rule.get("rationale", "") for rule in classification.get("classification_rules", [])
    ] + [
        row.get("classification_rationale", "") for row in classification.get("rows", [])
    ]
    title_leaks = sorted({
        title for title in forbidden_titles
        if any(re.search(r"(?<!\w)" + re.escape(title) + r"(?!\w)", norm(text)) for text in prose)
    })
    if title_leaks:
        fail(errors, "CLASSIFICATION_AUTHORING_TITLE_LEAK", ",".join(title_leaks[:8]))

    mcq_audit = load(root / "MCQ-AUDIT.json")
    matrix_legacy_hits = legacy_contract(matrix)
    quota_hits = legacy_contract(mcq_audit)
    quota_text = json.dumps({"matrix": matrix, "audit": mcq_audit}, ensure_ascii=False)
    if quota_hits or re.search(r"target_balance|(?<!quota_or_)target_distribution|distribution_quota|reasonably_balanced|answers_per_letter|balanced_exactly", quota_text, re.I):
        fail(errors, "ANSWER_QUOTA_CONTRACT", str(quota_hits[:8]))
    if matrix_legacy_hits or matrix.get("legacy_fixed_total") is not False:
        fail(errors, "LEGACY_FIXED_TOTAL", str(matrix_legacy_hits))
    if matrix.get("classification_hash") != classification.get("classification_hash"):
        fail(errors, "CLASSIFICATION_HASH_DRIFT", "Matrix is not bound to frozen classification")

    obligations_by_id = {
        row["obligation_id"]: row for row in expected_obligations.values()
        if row.get("classification") == "testable_atomic"
    }
    actual_cells = {row.get("cell_id"): row for row in matrix.get("cells", [])}
    if len(actual_cells) != len(matrix.get("cells", [])):
        fail(errors, "ORPHAN_CELL", "Duplicate or missing cell identifier")
    expected_cells = {}
    expected_q_cell = {}
    for cid, cell in actual_cells.items():
        oids = cell.get("obligation_ids", [])
        if not oids or len(oids) > 2 or any(oid not in obligations_by_id for oid in oids):
            fail(errors, "CELL_OBLIGATION_MISMATCH", str(cid))
            continue
        obligations = [obligations_by_id[oid] for oid in oids]
        joined = "+".join(oids)
        expected_cid = f"SK-CELL-{joined.removeprefix('SK-OBL-')}-{sha_text(cell.get('probe_mode',''))[:10].upper()}"
        if cid != expected_cid:
            fail(errors, "CELL_OBLIGATION_MISMATCH" if str(cid).startswith("SK-CELL-") else "ORPHAN_CELL", str(cid))
        refs = [{"authority_source": obligation["authority_source"], "authority_block_id": obligation["authority_block_ids"][0],
                 "proposition_id": obligation["proposition_ids"][0], "block_sha256": obligation["source_payload_hashes"]["block_sha256"],
                 "proposition_sha256": obligation["source_payload_hashes"]["proposition_sha256"]} for obligation in obligations]
        if cell.get("authority_refs") != refs:
            fail(errors, "QUESTION_AUTHORITY_MISMATCH", str(cid))
        mapped = cell.get("mapped_question_ids", [])
        minimum = cell.get("minimum_probes")
        if not isinstance(minimum, int) or minimum < 1 or len(mapped) != minimum:
            fail(errors, "TEST_MATRIX_DERIVATION_MISMATCH", str(cid))
        if cell.get("coverage_status") != "covered" or cell.get("derivation") != "post_classification_obligation_plus_probe_mode":
            fail(errors, "TEST_MATRIX_DERIVATION_MISMATCH", str(cid))
        expected_cells[cid] = cell
        for qid in mapped:
            if qid in expected_q_cell:
                fail(errors, "MCQ_MAPPING_OVERLOADED", qid)
            expected_q_cell[qid] = cid

    expected_question_count = len(qdoc)
    expected_qids = {f"Q{n}" for n in qdoc}
    if set(sdoc) != set(qdoc) or set(qdoc) != set(range(1, expected_question_count + 1)):
        fail(errors, "MCQ_DOCUMENT_COUNT", f"questions={len(qdoc)} solutions={len(sdoc)}")
    if matrix.get("cell_count") != len(actual_cells) or matrix.get("question_total") != expected_question_count:
        fail(errors, "MCQ_MATRIX_TOTAL_MISMATCH", "Matrix totals differ")
    if set(expected_q_cell) != expected_qids:
        fail(errors, "ORPHAN_QUESTION", "Cell question inventory differs from authored documents")

    mapping_rows = matrix.get("question_mappings", [])
    mapped_pairs = {(x.get("question_id"), x.get("cell_id")) for x in mapping_rows}
    if len(mapped_pairs) != len(mapping_rows):
        fail(errors, "MCQ_REDUNDANT_MAPPING", "Duplicate question-cell mapping")
    for row in mapping_rows:
        qid = row.get("question_id"); cid = row.get("cell_id")
        if qid not in expected_qids:
            fail(errors, "ORPHAN_QUESTION", str(qid)); continue
        if cid != expected_q_cell.get(qid):
            fail(errors, "QUESTION_OBLIGATION_MISMATCH", f"{qid}:{cid}"); continue
        cell = expected_cells[cid]
        for oid in row.get("obligation_ids", []):
            if actual_obligations.get(oid, {}).get("classification") != "testable_atomic":
                fail(errors, "NON_TESTABLE_OBLIGATION_MAPPED", f"{qid}:{oid}")
        if row.get("obligation_ids") != cell["obligation_ids"]:
            fail(errors, "QUESTION_OBLIGATION_MISMATCH", f"{qid}:{cid}")
        if row.get("authority_refs") != cell["authority_refs"]:
            fail(errors, "QUESTION_AUTHORITY_MISMATCH", f"{qid}:{cid}")
        n = int(qid[1:]); q = sdoc.get(n)
        if not q or len(q.get("options", {})) != 4 or len(q.get("explanations", {})) != 4:
            fail(errors, "MCQ_SOLUTION_STRUCTURE", qid); continue
        evidence = " ".join([q["title"], q["stem"], q["options"].get(q["answer"], ""), q["explanations"].get(q["answer"], "")])
        evidence_terms = relation_tokens(evidence)
        anchors = row.get("mapping_anchors", [])
        if [x.get("obligation_id") for x in anchors] != row.get("obligation_ids"):
            fail(errors, "MCQ_SEMANTIC_AUTHORITY_MISMATCH", f"{qid}->{cid}")
        for anchor in anchors:
            oid = anchor.get("obligation_id"); terms = anchor.get("doctrine_specific_terms", [])
            obligation = obligations_by_id.get(oid, {})
            authority_payload = proposition_payloads.get(obligation.get("proposition_ids", [""])[0], "")
            authority_terms = relation_tokens(authority_payload)
            if len(terms) < 2 or any(term in RELATION_STOP or term not in authority_terms or term not in evidence_terms for term in terms):
                fail(errors, "MCQ_SEMANTIC_AUTHORITY_MISMATCH", f"{qid}->{oid}")
        content_hash = sha_text(json.dumps({"title": q["title"], "stem": q["stem"], "correct": q["options"][q["answer"]],
            "distractors": sorted(v for k, v in q["options"].items() if k != q["answer"])}, ensure_ascii=False, sort_keys=True))
        if row.get("substantive_question_hash") != content_hash:
            fail(errors, "GENERATED_QUESTION_SET_TAMPER", qid)
    for qid in expected_qids:
        count = sum(row.get("question_id") == qid for row in mapping_rows)
        if count == 0: fail(errors, "ORPHAN_QUESTION", qid)
        if count > 1: fail(errors, "MCQ_MAPPING_OVERLOADED", qid)
    mapped_obligations = {oid for row in mapping_rows for oid in row.get("obligation_ids", [])}
    for oid, obligation in actual_obligations.items():
        if obligation.get("classification") == "testable_atomic" and oid not in mapped_obligations:
            fail(errors, "TESTABLE_OBLIGATION_REVERSE_COVERAGE_MISSING", oid)
        if obligation.get("classification") != "testable_atomic" and oid in mapped_obligations:
            fail(errors, "NON_TESTABLE_OBLIGATION_MAPPED", oid)
    for n in sorted(set(qdoc) | set(sdoc)):
        q, sq = qdoc.get(n), sdoc.get(n)
        if not q or not sq or q["title"] != sq["title"] or q["stem"] != sq["stem"] or q["options"] != sq["options"]:
            fail(errors, "MCQ_OPTION_SOLUTION_TAMPER", f"Q{n}")

    draws = mcq_audit.get("question_draws", []); draw_map = {x.get("question_id"): x for x in draws}
    if set(draw_map) != expected_qids or len(draw_map) != len(draws):
        fail(errors, "ANSWER_DRAW_INVENTORY", str(len(draws)))
    accepted = ""
    for qid in sorted(expected_qids, key=lambda x: int(x[1:])):
        expected_draw = independent_draw(qid, accepted); actual_draw = draw_map.get(qid)
        if actual_draw != expected_draw:
            if actual_draw and actual_draw.get("raw_draw") != expected_draw["raw_draw"]: code = "ANSWER_RAW_DRAW_TAMPER"
            elif actual_draw and actual_draw.get("final_placement") != expected_draw["final_placement"]: code = "ANSWER_FINAL_PLACEMENT_TAMPER"
            elif actual_draw and actual_draw.get("rejection_log") != expected_draw["rejection_log"]: code = "ANSWER_REJECTION_LOG_TAMPER"
            else: code = "ANSWER_DRAW_HASH_TAMPER"
            fail(errors, code, qid)
        final = expected_draw["final_placement"]; accepted += final
        n = int(qid[1:])
        if sdoc.get(n, {}).get("answer") != final:
            fail(errors, "ANSWER_FINAL_PLACEMENT_TAMPER", qid)
    sequence = accepted
    if mcq_audit.get("answer_sequence") != sequence: fail(errors, "ANSWER_FINAL_PLACEMENT_TAMPER", "answer_sequence")
    counts = {x: sequence.count(x) for x in "ABCD"}
    if mcq_audit.get("answer_counts") != counts: fail(errors, "ANSWER_OBSERVED_DISTRIBUTION_TAMPER", str(counts))
    max_run = max(len(m.group(0)) for m in re.finditer(r"(.)\1*", sequence)); cycles = predictable_cycles(sequence)
    if mcq_audit.get("max_answer_run") != max_run: fail(errors, "MCQ_ANSWER_RUN", str(max_run))
    if mcq_audit.get("short_cycles") != [{"period": p, "start": s + 1, "unit": u} for p, s, u in cycles]: fail(errors, "MCQ_SHORT_CYCLE", str(cycles))
    policy = mcq_audit.get("position_policy", {})
    if policy != {"algorithm_version": ANSWER_DRAW_ALGORITHM_VERSION, "seed_policy": ANSWER_DRAW_SEED_POLICY,
                  "safety_rejections_only": ["max_run_two", "reject_three_repeated_cycles_period_2_to_4"],
                  "quota_or_target_distribution": None, "predictable_cycle_detected": bool(cycles)}:
        fail(errors, "ANSWER_DRAW_POLICY_TAMPER", str(policy))
    stems = defaultdict(list)
    for n, q in sdoc.items():
        stems[norm(q["stem"])].append(n); lens = [words(v) for v in q["options"].values()]
        if max(lens) / max(1, min(lens)) > mcq_audit["option_cues"]["threshold"]: fail(errors, "MCQ_OPTION_LENGTH_CUE", f"Q{n}")
        if len(set(q["options"].values())) < 4: fail(errors, "MCQ_OPTION_FORMAT_CUE", f"Q{n}")
    repeated = [v for v in stems.values() if len(v) > 1]
    if repeated: fail(errors, "MCQ_REDUNDANT_STEM", str(repeated))
    boilerplate = repeated_explanation_fragments(sdoc)
    if boilerplate: fail(errors, "MCQ_WRONG_EXPLANATION_BOILERPLATE", str(boilerplate[:5]))
    traps = Counter(norm(q.get("trap") or "") for q in sdoc.values()); repeated_traps = [{"text": x, "count": n} for x, n in traps.items() if x and n > 2]
    if repeated_traps: fail(errors, "MCQ_EXAMINER_TRAP_BOILERPLATE", str(repeated_traps[:5]))
    cue = mcq_audit.get("option_cues", {})
    if cue.get("format_mismatches") != 0: fail(errors, "MCQ_OPTION_FORMAT_CUE", str(cue.get("format_mismatches")))
    if cue.get("specificity_flags") != 0: fail(errors, "MCQ_OPTION_SPECIFICITY_CUE", str(cue.get("specificity_flags")))
    if cue.get("lexical_key_flags") != 0: fail(errors, "MCQ_OPTION_LEXICAL_CUE", str(cue.get("lexical_key_flags")))
    checks.update({"matrix_cells": len(expected_cells), "mcq_total": expected_question_count, "answer_distribution": counts,
        "testable_obligations": classification["classification_counts"].get("testable_atomic", 0), "max_answer_run": max_run,
        "short_cycle_count": len(cycles), "answer_rejections": sum(len(x["rejection_log"]) for x in draws),
        "option_max_length_ratio": cue.get("maximum_word_length_ratio"), "option_format_flags": cue.get("format_mismatches"),
        "option_specificity_flags": cue.get("specificity_flags"), "option_lexical_flags": cue.get("lexical_key_flags"),
        "repeated_wrong_explanation_fragments": len(boilerplate), "repeated_examiner_traps": len(repeated_traps)})

    pyq = load(root / "PYQ-DEMAND-AUDIT.json")
    toolkit = (root / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    primary = pyq.get("primary", [])
    if pyq.get("formal_pre_2026_corpus") != {"primary_count": 10, "routed_count": 3, "total": 13}:
        fail(errors, "PYQ_FORMAL_CORPUS_OWNERSHIP", "Formal corpus must resolve as 10 primary plus 3 routed")
    if pyq.get("verified_ledger_additions_2026") != {"primary_count": 2, "questions": ["Q5(c)", "Q6(a)"]}:
        fail(errors, "PYQ_FORMAL_CORPUS_OWNERSHIP", "2026 ledger additions differ")
    if pyq.get("latest_repository_year") != 2026 or len(primary) != len(PYQS) or pyq.get("primary_count") != len(PYQS):
        fail(errors, "PYQ_PRIMARY_COUNT", "Primary PYQ corpus differs")
    for expected, row in zip(PYQS, primary):
        year, qno, marks, wording, _ = expected
        if (row.get("year"), row.get("question"), row.get("marks"), row.get("exact_wording")) != (year, qno, marks, wording):
            fail(errors, "PYQ_EXACT_WORDING_OR_MARKS", f"{year} {qno}")
        if row.get("validation_result") != "passed":
            fail(errors, "SPECIAL_INVENTORY_VALIDATION_STATUS", f"primary PYQ {year} {qno}")
        expected_display = "20 marks (10+10)" if (year, qno) == (2024, "Q7(a)") else f"{marks} marks"
        if row.get("marks_display") != expected_display:
            fail(errors, "PYQ_EXACT_WORDING_OR_MARKS", f"{year} {qno}: marks display")
        if wording not in toolkit:
            fail(errors, "PYQ_TOOLKIT_WORDING_MISSING", f"{year} {qno}")
        wc = row.get("model_word_count", 0)
        lo, hi = {10: (150, 200), 15: (250, 300), 20: (340, 400)}[marks]
        if not lo <= wc <= hi:
            fail(errors, "PYQ_WORD_BAND", f"{year} {qno}: {wc}")
        for field in ("demand_decoding", "qualification_present", "marks_rationale_present"):
            if not row.get(field):
                fail(errors, "PYQ_SOLUTION_COMPONENT_MISSING", f"{year} {qno}: {field}")
    supporting = pyq.get("supporting", [])
    if len(supporting) != 3 or pyq.get("supporting_count") != 3:
        fail(errors, "PYQ_ROUTED_OWNERSHIP", "Expected exactly three routed/supporting formal PYQs")
    for expected, row in zip(SUPPORTING_PYQS, supporting):
        year, qno, marks, wording, route = expected
        if (row.get("year"), row.get("question"), row.get("marks"), row.get("exact_wording"), row.get("route")) != (year, qno, marks, wording, route):
            fail(errors, "PYQ_ROUTED_OWNERSHIP", f"{year} {qno}")
        if row.get("primary_owner_is_samkhya") is not False:
            fail(errors, "PYQ_ROUTED_OWNERSHIP", f"{year} {qno}: falsely primary")
        if row.get("validation_result") != "passed":
            fail(errors, "SPECIAL_INVENTORY_VALIDATION_STATUS", f"routed PYQ {year} {qno}")
    originals = pyq.get("originals", [])
    if [x.get("marks") for x in originals] != [10, 10, 15, 15, 20, 20]:
        fail(errors, "ORIGINAL_TIMED_SET", "Expected formal 2x10, 2x15 and 2x20 originals")
    for row in originals:
        if row.get("validation_result") != "passed":
            fail(errors, "SPECIAL_INVENTORY_VALIDATION_STATUS", row.get("id", "original"))
        lo, hi = row["band"]
        if not lo <= row["model_word_count"] <= hi:
            fail(errors, "ORIGINAL_WORD_BAND", row["id"])
    expected_formal_pyq_ids = (
        [f"PYQ-{year}-{re.sub(r'[^a-z0-9]+', '-', qno.lower()).strip('-')}" for year, qno, *_ in PYQS] +
        [f"ROUTED-PYQ-{year}-{re.sub(r'[^a-z0-9]+', '-', qno.lower()).strip('-')}" for year, qno, *_ in SUPPORTING_PYQS]
    )
    if [row.get("id") for row in special_inventories.get("formal_pyqs", [])] != expected_formal_pyq_ids:
        fail(errors, "SPECIAL_INVENTORY_IDENTITY", "formal_pyqs")
    if [row.get("id") for row in special_inventories.get("originals", [])] != [row.get("id") for row in originals]:
        fail(errors, "SPECIAL_INVENTORY_IDENTITY", "originals")
    models = parse_model_answers(toolkit)
    expected_bands = ([{10: (150, 200), 15: (250, 300), 20: (340, 400)}[row[2]] for row in PYQS] +
                      [(150, 200), (150, 200), (250, 300), (250, 300), (340, 400), (340, 400)])
    if len(models) != len(expected_bands):
        fail(errors, "MODEL_ANSWER_COUNT", f"expected={len(expected_bands)} actual={len(models)}")
    for i, (model, band) in enumerate(zip(models, expected_bands), 1):
        if model["declared"] != model["actual"]:
            fail(errors, "MODEL_WORD_COUNT_MISMATCH", f"model={i} declared={model['declared']} actual={model['actual']}")
        if not band[0] <= model["actual"] <= band[1]:
            fail(errors, "MODEL_PROSE_WORD_BAND", f"model={i} words={model['actual']} band={band}")
    stock_phrases = (
        "this qualification avoids turning a system-specific explanation",
        "the exam value lies in connecting doctrine",
        "accordingly, the theory remains philosophically significant",
        "a high-quality answer must preserve the distinction",
        "the final judgement should therefore be conditional",
    )
    for phrase in stock_phrases:
        if phrase in norm(toolkit):
            fail(errors, "MODEL_STOCK_PADDING", phrase)
    wording_notes = pyq.get("wording_notes", {})
    if wording_notes.get("2026_Q5c") != "Ledger-normalized wording uses “Sankhya”; authenticated printed OCR/scan wording reads “Sarnkhya”.":
        fail(errors, "PYQ_PRINTED_WORDING_NOTE", "2026 Q5(c)")
    if "The authenticated ledger normalizes the school name as “Sankhya”; the official OCR/scan line reads “Sarnkhya”." not in toolkit:
        fail(errors, "PYQ_PRINTED_WORDING_NOTE", "2026 Q5(c) toolkit note")
    checks.update({"primary_pyqs": len(primary), "supporting_pyqs": pyq.get("supporting_count"),
                   "original_timed_models": len(originals),
                   "model_answers_independently_counted": len(models)})

    if release:
        try:
            repo = Path(subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True).strip())
            relroot = root.relative_to(repo)
            unstaged = []
            staged = 0
            for rel in REQUIRED + ["SOURCE-ARTIFACT-AUDIT.json"]:
                p = root / rel
                relpath = (relroot / rel).as_posix()
                work_oid = subprocess.check_output(["git", "-C", str(repo), "hash-object", "--path", relpath, str(p)], text=True).strip()
                staged_result = subprocess.run(["git", "-C", str(repo), "rev-parse", f":{relpath}"], text=True, capture_output=True)
                if staged_result.returncode != 0 or staged_result.stdout.strip() != work_oid:
                    unstaged.append(rel)
                else:
                    staged += 1
            if unstaged:
                fail(errors, "RELEASE_NOT_STAGED", f"{len(unstaged)} package files absent/different in index")
            checks["git_normalized_staged_files"] = staged
        except Exception as exc:
            fail(errors, "RELEASE_GIT_CHECK_FAILED", str(exc))

    return report(release, checks, errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    result = validate(args.root.resolve(), args.release)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not args.check_only:
        (args.root / "VALIDATION.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return 0 if result["state"] in {"DEVELOPMENT_PASS", "RELEASE_PASS"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
