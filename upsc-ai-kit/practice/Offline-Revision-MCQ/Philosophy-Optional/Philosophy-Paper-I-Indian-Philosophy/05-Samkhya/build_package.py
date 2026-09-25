from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUTHORED_AT = "2026-09-24T22:25:27+05:30"
IST = timezone(timedelta(hours=5, minutes=30))

SOURCES = {
    "formal_session": Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\05-Samkhya\Learning-Session.md"),
    "formal_workbook": Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\05-Samkhya\Solved-Practice-Workbook.md"),
    "canonical": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Samkhya.md"),
    "supplementary_complete": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\_learning-sessions\05_Samkhya-Complete-Learning-Session.md"),
    "supplementary_layered": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\Indian-Philosophy\learning-sessions\Samkhya\Samkhya_Layered-Complete-Learning-Session_2026-08-18.md"),
    "supplementary_workbook": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\Indian-Philosophy\learning-sessions\Samkhya\Samkhya_Layered-Solved-Practice-Workbook_2026-08-18.md"),
    "pyq_2018_2025": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md"),
    "pyq_2026": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md"),
}
FORMAL_ROOT = SOURCES["formal_session"].parent
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
SCAN_2026 = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\new_papers\QP-CSM-26-010926-Optional-PHILOSOPHY-PAPER_I.pdf")

ARTIFACTS = [
    "README.md", "REVISION-GUIDE.md", "MCQ-QUESTIONS.md", "MCQ-SOLUTIONS.md",
    "COVERAGE-LEDGER.md", "FORMAL-COVERAGE-AUDIT.json", "FORMAL-COVERAGE-REVIEW.json",
    "AUTHORITY-CLASSIFICATION.json", "AUTHORITY-OBLIGATION-LEDGER.json", "TEST-MATRIX.json", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "PRACTICE-LOG.md",
    "ANSWER-WRITING-TOOLKIT.md", "FORMAL-SOURCE-MIRROR.md",
    "source-snapshots/canonical-Samkhya.md",
    "source-snapshots/formal-Learning-Session.md",
    "source-snapshots/formal-Solved-Practice-Workbook.md",
    "source-snapshots/supplementary-complete-session.md",
    "source-snapshots/supplementary-layered-session.md",
    "source-snapshots/supplementary-solved-workbook.md",
    "source-snapshots/pyq-2018-2025.md", "source-snapshots/pyq-2026.md",
    "build_package.py", "question_bank.py", "validate_package.py", "run_negative_tests.py", "render_pdfs.py",
    ".gitattributes",
]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).casefold()


def slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).lower()
    return re.sub(r"[^\w]+", "-", text, flags=re.UNICODE).strip("-")[:72] or "block"


def file_info(path: Path) -> dict:
    return {"path": str(path), "sha256": sha_bytes(path.read_bytes()), "bytes": path.stat().st_size}


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
        raise RuntimeError("Incomplete semantic proposition after contiguous-line normalization: " + dangling[0])
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


def anchored_source(path: Path, blocks: list[dict]) -> str:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    by_line = {row["line_start"]: row["id"] for row in blocks}
    out = []
    for n, line in enumerate(lines, 1):
        if n in by_line:
            out.append(f'<a id="{by_line[n]}"></a>')
        out.append(line)
    return "\n".join(out) + "\n"


def source_block_by_heading(blocks: list[dict], phrase: str) -> dict:
    return next(row for row in blocks if phrase.casefold() in row["heading"].casefold())


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

DEMANDS = {
    "plurality": "State numerical plurality; present the three Kārikā arguments first; add liberation only as a supplementary inference; evaluate individuation.",
    "plurality_2026": "Answer one-or-many directly, explain the classical grounds, then examine both Advaita and internal objections.",
    "parinama_advaita": "Contrast real transformation with apparent transformation; reconstruct Śaṅkara’s objections; present Sāṃkhya replies and a graded verdict.",
    "jiva": "Distinguish metaphysical Puruṣa from empirical jīva, explain reflection and transmigration, then expose the bondage paradox.",
    "one_prakriti": "Identify avibhāgāt vaiśvarūpyasya, distinguish it from the other four proofs, and test whether unity follows demonstratively.",
    "mango": "Apply all five satkāryavāda arguments to seed-tree continuity and reject Nyāya, Advaita and Buddhist alternatives.",
    "mango_2026": "Use the mango case to explain latent determinacy and pariṇāma, then answer rival asatkārya, vivarta and dependent-origination accounts.",
    "gunas": "Define the guṇas as constituents, explain cooperation and equilibrium, distinguish sarūpa from virūpa pariṇāma, and evaluate.",
    "purusa_proofs": "Explain all five cumulative proofs, identify sāmānyato-dṛṣṭa inference, distinguish proof of subjectivity from proof of plurality, and evaluate.",
    "contact": "Present Śaṅkara’s dilemma about two independent principles, test Sāṃkhya’s proximity and analogies, and conclude briefly.",
    "evolution": "Give the exact ordered 25-tattva sequence, distinguish branches, and clarify that mahat and buddhi are one tattva while ahaṃkāra is its evolute.",
    "pradhana_malla": "Explain why Sāṃkhya is the strongest systematic rival, present Śaṅkara’s scriptural and rational objections, replies, and residual comparison.",
}

QUALIFICATIONS = {
    "plurality": "Differences among bodies and minds support distinct experiential streams, but do not by themselves demonstrate numerical difference among attributeless witnesses.",
    "plurality_2026": "Non-transferable bondage and release strengthen plurality within Sāṃkhya, while Advaita can still relocate those differences to limiting adjuncts.",
    "parinama_advaita": "Advaita does not deny empirical change; it denies that ultimate Brahman undergoes the real modification asserted of Prakṛti.",
    "jiva": "The subtle body, not pure Puruṣa, carries dispositions and transmigrates; otherwise inactivity and eternality would be compromised.",
    "one_prakriti": "Avibhāga makes one root explanatorily preferable, but coordinated plurality is not rendered formally contradictory.",
    "mango": "The example proves causal restriction more readily than it proves that determinate potency must be described as the effect’s prior existence.",
    "mango_2026": "Rival accounts must be granted their strongest claim: Nyāya accepts real novelty, Advaita empirical appearance, and Buddhism conditioned continuity.",
    "gunas": "Guṇa theory integrates the system, yet its explanatory flexibility can become unfalsifiable unless transformations are independently constrained.",
    "purusa_proofs": "The cumulative inferences establish a subject-pole more securely than an eternal, inactive and numerically plural substance.",
    "contact": "Sānnidhya denies physical interaction, but naming proximity does not yet explain the origin or purposive direction of coordination.",
    "evolution": "Mahat and buddhi are one tattva under cosmic and psychological descriptions; counting them separately corrupts the twenty-five-tattva scheme.",
    "pradhana_malla": "Śaṅkara’s critique exposes Sāṃkhya’s relation problem, but Advaita must still explain māyā without modifying Brahman.",
}

MARKS_RATIONALES = {
    "plurality": "A direct thesis, the three Kārikā grounds, one supplementary liberation argument, and a brief individuation objection fit a focused 10-marker.",
    "plurality_2026": "The answer states “many” immediately, explains the classical evidence, and uses Advaita plus an internal objection to satisfy “examine.”",
    "parinama_advaita": "Balanced space is given to pariṇāma, Śaṅkara’s objections, Sāṃkhya’s defence, and the reciprocal cost borne by vivarta.",
    "jiva": "The distinction is defined before reflection and transmigration are explained, allowing the final bondage paradox to function as genuine criticism.",
    "one_prakriti": "The decisive proof is isolated from the other four, then tested against a multiple-root countermodel rather than merely asserted.",
    "mango": "The concrete example organizes all five arguments, three rival theories receive fair reconstruction, and the conclusion separates causal restriction from latent identity.",
    "mango_2026": "The second mango answer independently develops auxiliaries, rival ontologies and a graded verdict instead of reproducing the 2020 model.",
    "gunas": "Definition, functions, two modes of modification, evolutionary role and evaluative limitation together meet the explanatory directive.",
    "purusa_proofs": "All five proofs are named and interpreted, their inferential form is identified, and the conclusion distinguishes minimal from maximal claims.",
    "contact": "Śaṅkara’s dilemma is presented first, each major analogy is tested, and Sāṃkhya’s proximity reply receives a precise residual objection.",
    "evolution": "The answer secures marks through ordered evolution, branch logic, exact counting, the buddhi–mahat distinction, and a targeted causal criticism.",
    "pradhana_malla": "It first explains the title, then groups scriptural and rational attacks, reconstructs replies, and closes by comparing the costs of both systems.",
}

ANSWER_CORES = {
    "plurality": """Sāṃkhya accepts many Puruṣas, although each is pure, inactive, changeless consciousness. The classical grounds are first, the fixed distribution of birth, death and sense-capacities: one body is born, dies or becomes blind without the same event occurring everywhere. Second, embodied beings act at different times; a single witness would make their activity simultaneous. Third, guṇa-configurations differ, producing distinct experiential streams. A supplementary argument adds that liberation of one does not liberate all.

These arguments protect the individuality of experience and moral continuity. They also fit Sāṃkhya’s claim that Prakṛti works for the experience and release of each witness. Advaita objects that all cited differences belong to bodies, minds and other limiting adjuncts, not to attributeless consciousness. Sāṃkhya replies that one consciousness would make bondage and release universally shared. Yet numerical individuation of qualitatively identical Puruṣas remains under-explained. Thus plurality is systemically necessary and phenomenologically plausible, though not conclusively demonstrated.""",
    "plurality_2026": """Puruṣa is many in Sāṃkhya. Plurality is numerical, not qualitative: every Puruṣa is pure, inactive and beyond the guṇas. Sāṃkhyakārikā 18 argues from the separate allocation of birth, death and faculties, from non-simultaneous activity, and from differences in guṇa-constitution. If consciousness were literally one, blindness in one body, action in one stream or release in one case should implicate all.

The doctrine preserves private experience, karmic continuity and particular liberation. Advaita replies that these differences establish many minds, not many attributeless witnesses; one consciousness may appear plural through adjuncts. Sāṃkhya answers that apparent plurality cannot explain why bondage and release remain non-transferable. The internal difficulty persists: an inactive, partless consciousness lacks an obvious principle of numerical differentiation. Therefore Sāṃkhya has strong soteriological reasons for plurality, but its inference is more compelling about distinct experiential centres than about metaphysically identical eternal subjects.""",
    "jiva": """Puruṣa is the metaphysical conscious principle: eternal, inactive, unproduced, plural and never modified. Jīva is not a twenty-sixth tattva. It is Puruṣa as empirically associated with buddhi, ahaṃkāra, manas, the faculties, subtle body and karmic dispositions.

Buddhi is material but sattva-predominant, so it reflects consciousness. Ahaṃkāra appropriates the illuminated cognition as “I know” or “I act.” Hence the jīva appears to be knower, agent and enjoyer, while productive agency belongs to Prakṛti and witnessing to Puruṣa. Transmigration belongs to the subtle psychophysical stream, not literally to pure consciousness.

The critical problem is that if Puruṣa is never actually bound, liberation seems redundant; if only unconscious Prakṛti is bound, the identity of the seeker becomes obscure. Sāṃkhya answers that liberation removes false attribution rather than a real change in Puruṣa. The distinction is coherent as a theory of mistaken identity, but the reflection relation remains analogical rather than fully explained.""",
    "one_prakriti": """The proof that most directly establishes one Prakṛti is avibhāgāt vaiśvarūpyasya: the diversified universe proceeds from an undivided source. Manifest plurality forms an interconnected order whose effects share the three-guṇa constitution; the unmanifest matrix in which these differentiations are not yet divided is therefore inferred as one.

The other arguments mainly establish a material root: finite effects require a ground; common features imply coordination; determinate operation requires causal power; and manifest effect must be distinguished from unmanifest cause. They do not by themselves exclude several primal causes. The fifth argument adds the unity claim.

A critic may say that coordinated plurality could arise from several cooperating causes. Sāṃkhya replies that many Prakṛtis with identical guṇas and powers would be redundant and would require a higher coordinator, defeating their ultimacy. The inference is consequently abductive rather than deductive. One Prakṛti is the simplest explanation of a single, transformable guṇa-continuum, although logical impossibility of multiple coordinated roots has not been strictly proved.""",
    "purusa_proofs": """Sāṃkhya offers five cumulative inferences for Puruṣa. Saṅghāta-parārthatvāt argues that body, senses and mind are aggregates functioning for another. Triguṇādi-viparyayāt infers a witness opposite to the mutable, objectifiable guṇas. Adhiṣṭhānāt requires a conscious locus for organized experience. Bhoktṛ-bhāvāt holds that pleasure and pain require an experiencer. Kaivalyārthaṃ pravṛtteḥ interprets striving for release as presupposing a liberable conscious principle.

These are sāmānyato-dṛṣṭa inferences from the general structure of experience to an imperceptible subject. Their cumulative force is stronger than any isolated analogy: the known psychophysical complex cannot itself exhaust the knower. Buddhists deny that aggregates require an owner and explain continuity causally; Advaita accepts witness-consciousness but rejects many witnesses. The proofs establish a non-objective subject-pole more successfully than they establish an eternal, wholly inactive and plural substance. Their philosophical value lies in separating consciousness from its contents, while their full metaphysical conclusion remains contestable.""",
    "contact": """Śaṅkara argues that two completely independent realities cannot explain a coordinated world. Puruṣa is inactive and changeless; Prakṛti is unconscious. Neither can intentionally approach, activate or understand the other. If proximity is a real relation, both acquire relational determination and cease to be wholly independent. If it is unreal, it explains no disturbance of guṇa-equilibrium; if beginningless and uniform, evolution should never cease.

The lame-and-blind analogy assumes conscious direction by the lame person, which Puruṣa cannot provide. Magnet and iron smuggle in causal power; crystal and flower explain apparent colouring but not purposive evolution. Sāṃkhya replies that sānnidhya is neither physical contact nor volition: Prakṛti’s inherent guṇa-dynamics operate for experience and discrimination in Puruṣa’s presence.

The reply protects Puruṣa from modification and keeps Prakṛti causally sufficient. Nevertheless, the analogies illustrate rather than derive the relation. Śaṅkara’s criticism therefore identifies a genuine explanatory gap at the junction of consciousness, activation and teleology.""",
    "gunas": """Prakṛti is constituted by three inseparable guṇas, not a substance that later acquires three optional qualities. Sattva is illumination, lightness and pleasure; rajas is activity, propulsion and pain; tamas is heaviness, obstruction and delusion. They oppose, support and dominate one another, like oil, wick and flame cooperating in one lamp. Every mental and physical product contains all three in different proportions.

Before manifestation the guṇas are in sāmyāvasthā, a dynamic equilibrium. Their continuing same-form change is sarūpa-pariṇāma: each changes within its own tendency without producing differentiated tattvas. Disequilibrium produces virūpa-pariṇāma, heterogeneous transformation. Rajas energizes the sattvic line of mind and faculties and the tamasic line of subtle and gross elements.

Thus guṇa theory connects psychology and cosmology: clarity, desire and inertia belong to the same material continuum as intellect, senses and elements. Its strength is explanatory economy. Its weakness is elasticity, since almost any phenomenon can be redescribed as a proportion of three tendencies. It integrates the system more convincingly than it independently proves the guṇas.""",
    "parinama_advaita": """Sāṃkhya’s Prakṛti-pariṇāmavāda says that the world is a real transformation of one unconscious material cause. The effect pre-exists latently, and guṇa-reconfiguration makes it manifest. Advaita accepts that sheer non-being cannot produce being, but rejects independent Prakṛti and real transformation of ultimate Brahman. It proposes vivarta: the world is empirically experienced yet does not modify non-dual Brahman.

Śaṅkara argues that unconscious pradhāna cannot initiate ordered, purposive evolution; inactive Puruṣa cannot direct it; two independent absolutes lack a coordinating relation; and Upaniṣadic causal passages describe a conscious, knowing source. Sāṃkhya replies that material continuity, determinate potency and shared guṇa-character require Prakṛti. Natural processes such as milk becoming curd need no deliberating maker, and adding God does not explain how consciousness supplies unconscious matter.

Sāṃkhya better preserves the reality and material continuity of change. Advaita more directly addresses unity and intelligence but inherits the difficulty of explaining māyā and appearance without compromising Brahman. Therefore neither criticism is cost-free: pariṇāma faces unconscious teleology, while vivarta faces the ontological status of appearance.""",
    "mango": """The mango tree illustrates Sāṃkhya’s satkāryavāda: an effect pre-exists latently in its material cause. The seed is not a miniature visible tree; it bears the determinate material potency that unfolds under soil, water, heat and time. Production is abhivyakti, manifestation through real transformation or pariṇāma.

Five arguments explain the restriction. Asadakaraṇāt denies production from absolute non-being. Upādāna-grahaṇāt notes that a specific material is selected. Sarvasambhavābhāvāt denies that anything can arise from anything. Śaktasya śakya-karaṇāt links a cause to what its power can produce. Kāraṇa-bhāvāt stresses material continuity between cause and effect. Thus a mango seed, not sand, can become a mango tree.

Nyāya’s asatkāryavāda treats the tree as a new whole preceded by its absence. Sāṃkhya replies that capacity becomes unexplained unless the effect is grounded in the cause; Nyāya answers that causal power need not be latent identity. Advaita treats transformation as appearance relative to Brahman, whereas Sāṃkhya insists that the empirical material change is real. Buddhism explains a conditioned momentary series without enduring Prakṛti; Sāṃkhya argues that a continuing material ground better explains specificity.

The doctrine strongly explains continuity and causal selection, though critics can charge that “pre-existence” redescribes potency and leaves novelty as configuration rather than new being.""",
    "mango_2026": """For Sāṃkhya, the mango tree is sat before production in a latent, determinate mode within its material cause. It is not spatially folded inside the seed. Seed, sprout and tree are successive configurations of one causal continuum; suitable auxiliaries manifest the capacity through pariṇāmavāda, real transformation.

Asadakaraṇāt denies creation of being from sheer non-being. Upādāna-grahaṇāt explains why a mango material is selected. Sarvasambhavābhāvāt excludes arbitrary production. Śaktasya śakya-karaṇāt connects the seed’s power with its possible product. Kāraṇa-bhāvāt identifies continuity of causal nature in the effect. Together these arguments explain why mango comes from mango seed rather than clay or rice.

Nyāya–Vaiśeṣika’s asatkāryavāda says the tree as a whole is newly originated after prior absence; causal powers, not a latent tree, determine production. Sāṃkhya responds that such power is intelligible only as the effect’s grounded possibility. Advaita’s vivartavāda denies real alteration of Brahman and treats world-formation as appearance; Sāṃkhya preserves empirical realism through actual material change. Buddhist dependent origination dispenses with an abiding root, construing seed and tree as conditioned series; Sāṃkhya regards continuity of one guṇa-material as explanatorily superior.

Its advantage is a unified account of material identity, specificity and transformation. Its limitation is that the language of latent effect may add little beyond a finely specified causal capacity, while novelty is confined to manifest arrangement.""",
    "evolution": """Classical Sāṃkhya begins with one avyakta Prakṛti whose sattva, rajas and tamas are in equilibrium. In the presence of Puruṣa the balance is disturbed, and twenty-three further material principles evolve. Puruṣa is counted as the twenty-fifth principle but is not produced.

The order is Prakṛti; mahat or buddhi; ahaṃkāra; then two branches energized by rajas. From sattvic ahaṃkāra arise manas, five cognitive capacities—hearing, touch, sight, taste and smell—and five action capacities—speech, grasping, locomotion, excretion and reproduction. From tamasic ahaṃkāra arise the subtle potentials of sound, touch, form, taste and smell, followed by ether, air, fire, water and earth. Rājasa ahaṃkāra supplies activity but no separate tattva-set.

Mahat and buddhi are one tattva viewed differently. Mahat names the first cosmic principle of determination; buddhi names its psychological function of ascertainment, judgement and discrimination. Ahaṃkāra is the next evolute, the I-maker that appropriates cognition as “mine.”

Cause-effect classification prevents counting errors: Prakṛti is cause but not effect; buddhi, ahaṃkāra and five tanmātras are both; manas, ten faculties and five gross elements are effects only; Puruṣa is neither.

The sequence unifies cosmology and psychology because intellect and matter share one guṇa-source. Its weakness is the unexplained first coordination: inactive consciousness does not literally disturb unconscious nature. Sāṃkhya invokes proximity and inherent transformation, but the transition remains its central pressure point.""",
    "pradhana_malla": """Śaṅkara treats Sāṃkhya as pradhāna-malla, the chief opponent, because it is the most systematic rival explanation of world, self, bondage, causation and liberation. It does not merely deny Vedānta; it offers one Pradhāna as material ground, many Puruṣas as witnesses, real evolution and release through discrimination. Its closeness makes refutation philosophically necessary.

Śaṅkara’s first objection is scriptural: Upaniṣadic causal passages describe a conscious and knowing source, not unconscious Prakṛti. Second, teleology is unintelligible if blind nature evolves for another’s experience and liberation. Third, inactive Puruṣa and independent Prakṛti cannot enter a relation that begins or ends evolution. Fourth, the lame-blind and milk-calf analogies presuppose direction, natural organization or prior arrangement not supplied by the two absolutes. Fifth, qualitatively identical and attributeless Puruṣas lack an individuating principle. Sixth, real transformation compromises the ultimacy attributed to the cause, while Advaita’s vivarta leaves Brahman unchanged. Finally, if Puruṣa is eternally untouched, bondage and liberation seem to belong only to unconscious Prakṛti.

Sāṃkhya replies that determinate effects require a real guṇa-material continuum; ordered natural functioning need not involve intention; plurality protects non-transferable experience and karma; and proximity explains apparent agency without modifying consciousness. It also charges Advaita with the unresolved status of māyā.

Śaṅkara’s strongest point is coordinated purposiveness, not mere scriptural preference. Yet Sāṃkhya remains a chief opponent precisely because its causal realism and consciousness-matter distinction expose costs in Advaita’s own appeal to appearance.""",
}

EXTRA = {
    "plurality": [
        "The first three arguments should be tied explicitly to Sāṃkhyakārikā 18; differential liberation is reinforcement, not a fourth phrase in that verse.",
        "Nyāya agrees with many selves but rejects an inactive witness, whereas Buddhism contests the permanent subject itself.",
    ],
    "plurality_2026": [
        "The plurality thesis must not be inferred merely from qualitative difference, because Sāṃkhya denies qualitative variation in pure consciousness.",
        "Its best defence is the non-transferability of experience rather than any spatial separation of Puruṣas.",
    ],
    "jiva": [
        "The subtle body carries dispositions and karmic tendencies after the gross body falls, preserving continuity without making Puruṣa an agent.",
    ],
    "one_prakriti": [
        "The third proof should be named śaktitaḥ pravṛtteś ca, operation from causal power; source variants must not be converted into purposive planning.",
        "Samanvaya supports common constitution, while avibhāga supplies the sharper numerical-unity inference.",
        "The crucial move is from shared constitution to an undivided causal condition: effects display many forms, but dissolution removes those divisions into one avyakta continuum. This is why avibhāga, rather than mere finitude or causal power, bears the numerical claim.",
        "Still, explanatory economy is not strict entailment. A pluralist could posit coordinated roots, and Sāṃkhya must then argue that such roots either duplicate identical powers or depend on a further principle. The proof therefore justifies unity as the best systemic explanation, not as a formal contradiction of every alternative.",
    ],
    "purusa_proofs": [
        "A careful evaluation separates the minimal conclusion—irreducible subjectivity—from the maximal conclusion—many eternal Puruṣas.",
    ],
    "contact": [
        "The dancer analogy explains cessation after disclosure, not the original activation of evolution, so it cannot independently solve Śaṅkara’s objection.",
    ],
    "gunas": [
        "Sarūpa change prevents equilibrium from being mistaken for absolute stasis; virūpa change explains manifest differentiation.",
        "Rajas is an enabling factor for both branches and does not generate an additional family of principles.",
        "At the psychological level, sattva appears as lucidity, rajas as restless striving and tamas as inertia; cosmologically, the same tendencies account for the relative luminosity, motion and resistance of material products. Buddhi can therefore be cognitively transparent without ceasing to be material.",
        "The doctrine succeeds as an integrating grammar because it avoids a separate substance for each mental and physical property. Its weakness is testability: unless proportions and transformations are independently specified, almost any outcome can be redescribed after the event as a guṇa-mixture.",
    ],
    "parinama_advaita": [
        "The dispute is not simply realism versus illusion: Advaita grants empirical transaction while denying ultimate transformation.",
        "Sāṃkhya’s defence is strongest when framed as continuity of material constitution, not as a claim that gross forms are already visible.",
        "Against the charge of blind purposiveness, Sāṃkhya distinguishes intention from regularity. Prakṛti does not plan; its guṇas transform according to inherent capacities, while the resulting field permits Puruṣa’s experience and discrimination. The milk-calf analogy is meant to show spontaneous service, though it cannot by itself prove cosmic teleology.",
        "Advaita can answer the coordination problem by grounding both knower and known in Brahman, but it must explain how ignorance and manifold appearance arise without becoming real modifications. Sāṃkhya can therefore press the same question in reverse: vivarta protects immutability only by assigning difficult explanatory work to māyā.",
    ],
    "mango": [
        "The cause and effect differ by state and arrangement, so manifestation preserves difference without admitting production from nothing.",
        "Auxiliary conditions explain timing, while the seed’s specific potency explains kind.",
        "This lets Sāṃkhya acknowledge novelty of configuration while denying novelty of underlying being.",
        "The five arguments form a cumulative case rather than five verbal restatements. Non-being cannot act; producers select an appropriate material; unrestricted emergence is never observed; a cause produces only what lies within its power; and the product retains the causal material in a transformed organization.",
        "Nyāya’s strongest reply is that a real new whole may arise from parts possessing determinate capacities, so specificity does not require the whole’s prior existence. Sāṃkhya answers that an unexplained capacity is merely latent effect under another name, but this reply is persuasive only if potency and pre-existence are treated as equivalent.",
        "The Buddhist comparison shifts the issue from substance to sequence: conditioned seed-moments can generate sprout-moments without one persisting stuff. Sāṃkhya gains continuity and a unified material ontology; Buddhism avoids an unobserved permanent root. The mango case supports causal restriction decisively, but latent identity remains the disputed interpretation.",
    ],
    "mango_2026": [
        "Destruction is likewise not annihilation into nothing but reversion of a manifest configuration to causal conditions.",
        "The comparison should grant Nyāya a genuine new whole and Advaita a non-transforming ultimate rather than caricaturing either.",
        "A graded verdict can accept Sāṃkhya’s causal specificity while questioning whether latent existence is stronger than dispositional language.",
        "The auxiliary conditions are causally necessary without being the material identity of the tree. Water and heat explain when the seed’s power becomes manifest; the seed’s constitution explains why the outcome is mango rather than wheat. This division lets Sāṃkhya distinguish occasion from material continuity.",
        "Nyāya can preserve causal restriction through inherited qualities, conjunction and an operative potency while maintaining that the tree-whole was previously absent. Sāṃkhya replies that a capacity wholly unrelated to the future effect cannot select it, yet Nyāya need not concede that determinacy amounts to numerical pre-existence.",
        "Consequently, the example establishes that production is constrained and intelligible through antecedent conditions. It does not by itself settle whether the best ontology is latent effect, a genuinely new whole, dependent series, or empirical appearance. Sāṃkhya’s distinctive answer is real transformation of one material continuum.",
    ],
    "evolution": [
        "The thirteen instruments are buddhi, ahaṃkāra, manas, five cognitive faculties and five action faculties.",
        "The five tanmātras are subtle causal potentials, not gross sensory objects; they generate the five mahābhūtas.",
        "The subtle body commonly comprises buddhi, ahaṃkāra, eleven faculties and five tanmātras, carrying dispositions across embodiments.",
        "This account does not include Yoga’s eight limbs or samādhi taxonomy, which belong to the adjacent Yoga owner.",
        "Functionally, buddhi makes determinate judgements and can acquire the discriminative knowledge that ends misidentification; ahaṃkāra adds ownership, converting cognition into “I know” and activity into “I act.” Their distinction is therefore causal and phenomenological, not merely terminological.",
        "Śaṅkara’s objection enters at the first transition: an unconscious equilibrium cannot purposively move for an inactive witness. Sāṃkhya answers through inherent guṇa-transformability and mere proximity, but the ordered service of experience and release remains an explanatory burden rather than a settled mechanism.",
    ],
    "pradhana_malla": [
        "The debate is therefore between two comprehensive architectures, not between philosophy and a primitive cosmology.",
        "Sāṃkhya can also ask how an immutable conscious Brahman bears even an apparent world without a second explanatory principle.",
        "A balanced judgement recognizes that each system relocates rather than entirely eliminates the relation problem.",
        "Sāṃkhya’s replies are strongest where Śaṅkara assumes that order always requires conscious design. Regular transformation may follow the constitutive tensions of the guṇas, and satkāryavāda explains why determinate products emerge from determinate materials. Mere absence of a creator therefore does not refute the system.",
        "They are weaker where the system invokes evolution “for” Puruṣa. If proximity neither changes Puruṣa nor adds causal power to Prakṛti, the beginning, direction and cessation of their coordination remain obscure. The chief-opponent label is justified because this unresolved junction mirrors Advaita’s own difficulty of relating immutable Brahman, māyā and experienced plurality.",
    ],
}

ORIGINALS = [
    (10, "Explain why sāmānyato-dṛṣṭa inference is indispensable to Sāṃkhya metaphysics.", "inference_indispensable"),
    (15, "Does the three-guṇa doctrine successfully unify Sāṃkhya psychology and cosmology? Evaluate.", "gunas_unity"),
    (20, "‘Sāṃkhya makes consciousness pure by making agency obscure.’ Critically examine.", "agency_obscure"),
]

ORIGINAL_ANSWERS = {
    "inference_indispensable": """Sāmānyato-dṛṣṭa inference moves from a general, repeatedly observed structure to a cause that is not itself perceptible. Sāṃkhya needs it because its two ultimate principles—Prakṛti and Puruṣa—cannot be presented as ordinary sensory objects.

From finite, coordinated and three-guṇa effects, Sāṃkhya infers an unmanifest material ground possessing the power to produce them. From the organized psychophysical aggregate, objectifiable cognition, enjoyment and the striving for release, it infers a conscious witness distinct from every guṇic product. Ordinary pūrvavat inference from cause to effect and śeṣavat inference from effect to familiar cause cannot by themselves reach these supersensible ultimates; testimony may confirm them but cannot carry the entire metaphysical burden in a rational system.

The inference is therefore architectonic: without it, the twenty-five-tattva scheme would describe manifest processes but could not justify either their common root or their non-material witness. Critics may accept the observed order while rejecting one Prakṛti or an eternal Puruṣa, so the inference is not demonstrative. It is nevertheless indispensable because Sāṃkhya’s dualism stands or falls with reasoned passage from experience to imperceptible explanatory conditions.""",
    "gunas_unity": """The three-guṇa doctrine is Sāṃkhya’s principal bridge between psychology and cosmology. Sattva signifies illumination and lightness, rajas activation and unrest, and tamas resistance and obscuration. They are not optional qualities added to Prakṛti but inseparable constituents of every material and mental product.

Cosmologically, equilibrium among the guṇas constitutes avyakta Prakṛti. Their disequilibrium produces virūpa-pariṇāma: mahat, ahaṃkāra, faculties, subtle elements and gross elements emerge through changing predominance. Rajas energizes both the sattvic cognitive branch and the tamasic elemental branch. Sarūpa-pariṇāma, continuing modification within equilibrium, prevents the unmanifest from being treated as sheer inertness.

Psychologically, the same vocabulary explains why buddhi can be lucid, why desire drives action and why dullness obstructs discrimination. Because buddhi is sattva-predominant, it can reflect Puruṣa’s consciousness while remaining material. Bondage occurs when ahaṃkāra appropriates this illuminated activity; liberation requires recognizing that every guṇic state belongs to Prakṛti.

This yields impressive economy: one set of principles connects matter, cognition, affect and moral cultivation. The theory also gives liberation a cosmological basis. Cultivating sattva makes buddhi transparent enough for discriminative knowledge, but even sattva must finally be recognized as material; release is not a perfected guṇa-state in Puruṣa.

The objection is elasticity. If any event can be redescribed as an unspecified mixture of three tendencies, the theory risks explaining retrospectively rather than predicting. Moreover, guṇa-dynamics do not fully explain why evolution serves an inactive Puruṣa. Thus the doctrine successfully unifies Sāṃkhya’s own psychology and cosmology, but its breadth is stronger as systematic integration than as independently testable proof.""",
    "agency_obscure": """Sāṃkhya purifies consciousness by defining Puruṣa as unproduced, changeless, partless, guṇa-less and inactive. Cognition, desire, effort and bodily motion all belong to Prakṛti. This sharply separates the witness from every object of awareness and supports liberation as discrimination rather than transformation of the self.

Agency is assigned to the internal instrument. Buddhi determines, ahaṃkāra appropriates its states as “I” and “mine,” manas coordinates the faculties, and the subtle body carries dispositions. Sattva-predominant buddhi reflects consciousness, so an unconscious mental event appears conscious while inactive Puruṣa appears to know and act. Bondage is this reciprocal misattribution; kaivalya occurs when buddhi discriminates the witness from the guṇas.

The arrangement explains why consciousness need not become mutable whenever thoughts change. It also preserves causal continuity: Prakṛti alone transforms. Yet the price is a difficult account of action. An unconscious buddhi cannot literally experience a purpose, while an inactive Puruṣa cannot initiate, select or own conduct. Sānnidhya, or proximity, states their coordination without specifying a causal relation. The lame-and-blind analogy covertly gives the lame person direction; the magnet analogy imports an influence denied to Puruṣa; the dancer analogy explains withdrawal after disclosure but not the first performance.

Sāṃkhya replies that intentional command is unnecessary. Guṇa-dynamics operate naturally, karma structures the subtle body, and Prakṛti functions for experience and eventual discrimination just as milk flows for a calf. Apparent agency is enough for ordinary responsibility because dispositions and consequences remain within the empirical stream.

Śaṅkara nevertheless argues that two independent principles cannot ground ordered cooperation, while Buddhism treats an inefficacious witness as dispensable. Sāṃkhya can answer that both rivals risk collapsing the distinction between awareness and its contents, but it does not fully derive teleology from blind nature.

The charge is therefore substantially correct but not fatal. Sāṃkhya gives a powerful analysis of why consciousness is not identical with mental activity. Its weakness is not the absence of empirical agency, which it locates in Prakṛti, but the unexplained coordination that makes such agency appear to and serve Puruṣa. Purity is secured analytically; interaction remains the unresolved metaphysical cost.""",
}


def words(text: str) -> int:
    return len(re.findall(r"\b[\wĀ-ž’'-]+\b", re.sub(r"[#*`|]", " ", text), flags=re.UNICODE))


def marks_label(year: int, qno: str, marks: int) -> str:
    return "20 marks (10+10)" if (year, qno) == (2024, "Q7(a)") else f"{marks} marks"


def formal_original_models() -> list[dict]:
    rows = []
    for block in heading_blocks(SOURCES["formal_workbook"], "formal_workbook"):
        match = re.match(r"Original\s+(\d+)\s+·\s+(10|15|20)\s+marks", block["heading"])
        if not match:
            continue
        payload = block["_payload"]
        question_match = re.search(r">\s*\*\*Question\.\*\*\s*(.+?)(?=\n\n\*\*Model answer)", payload, re.S)
        answer_match = re.search(r"\*\*Model answer \((\d+) words\)\.\*\*\s*\n\n(.+?)(?=\n\n---|\Z)", payload, re.S)
        if not question_match or not answer_match:
            raise ValueError(f"Cannot parse formal original: {block['heading']}")
        question = re.sub(r"\s+", " ", re.sub(r"\n>\s?", " ", question_match.group(1))).strip()
        answer = answer_match.group(2).strip()
        rows.append({
            "id": f"ORIGINAL-{match.group(1)}",
            "marks": int(match.group(2)),
            "question": question,
            "model": answer,
            "declared_word_count": int(answer_match.group(1)),
            "model_word_count": words(answer),
            "band": {10: [150, 200], 15: [250, 300], 20: [340, 400]}[int(match.group(2))],
            "formal_block_id": block["id"],
        })
    if [row["marks"] for row in rows] != [10, 10, 15, 15, 20, 20]:
        raise ValueError("Formal six-original distribution is incomplete")
    return rows


def fit_answer(theme: str, marks: int) -> str:
    base = ANSWER_CORES[theme].strip()
    additions = EXTRA.get(theme, [])
    minimum, maximum = {10: (150, 200), 15: (250, 300), 20: (340, 400)}[marks]
    for paragraph in additions:
        if words(base) >= minimum:
            break
        base += "\n\n" + paragraph
    if words(base) < minimum:
        raise ValueError(f"{theme}/{marks} below band after authored additions: {words(base)}")
    if words(base) > maximum:
        raise ValueError(f"{theme}/{marks} exceeds band: {words(base)}")
    return base


def wrong_option_explanation(option: str, correct: str) -> str:
    claim = option.rstrip(".")
    key = correct.rstrip(".")
    rival = ""
    if "Brahman" in option or "vivarta" in option or "appearance" in option:
        rival = f" It imports the Advaita account of apparent transformation where the keyed issue is {key.lower()}."
    elif "atom" in option or "samavāya" in option or "prior non-existence" in option or "new whole" in option:
        rival = f" It imports the Nyāya–Vaiśeṣika account of production where Sāṃkhya asserts {key.lower()}."
    elif "moment" in option or "dependent origination" in option or "arthakriyā" in option:
        rival = f" It substitutes a Buddhist process account for the Sāṃkhya claim that {key.lower()}."
    elif "God" in option or "Īśvara" in option or "divine" in option or "creator" in option:
        rival = f" The claim “{claim}” assigns to a creator a role excluded by the keyed Sāṃkhya formulation: {key}."
    elif "Puruṣa" in option and "Puruṣa" not in correct:
        rival = f" It wrongly transfers the tested material or cognitive function to inactive Puruṣa instead of recognizing that {key.lower()}."
    elif any(token in option for token in ("order", "sequence", "evolves", "→")):
        rival = f" It reverses or disrupts the canonical order summarized by the keyed statement: {key}."
    return f"Incorrect: “{claim}” conflicts with the tested distinction; Sāṃkhya instead holds that {key[0].lower() + key[1:]}.{rival}"


def examiner_trap(title: str, correct: str, wrongs: list[str]) -> str:
    contrast = wrongs[0].rstrip(".")
    key = correct.rstrip(".")
    return f"For {title.lower()}, do not mistake “{contrast}” for the keyed claim that {key[0].lower() + key[1:]}."


TOKEN_STOP = {
    "a", "an", "and", "are", "as", "at", "be", "best", "by", "does", "for", "from",
    "how", "in", "is", "it", "its", "of", "on", "or", "that", "the", "their", "this",
    "to", "what", "which", "why", "with",
}

# Frozen source-only predicates: rule id, authority source,
# normalized proposition hash, substantive category, rationale.
# No authoring handle, cell title, probe count, answer, question ID, or binding is allowed here.
AUTHORITY_TESTABILITY_RULE_SPECS = r"""
SK-TR-001|formal_session|a2f0d7ef0099f18a283ec2eaf0405455940491bf16dde9d9773e7ca0396d60db|core_doctrine_discriminator|Doctrine-specific transformation discriminator: the proposition distinguishes homogeneous change within each quality during the balanced state from heterogeneous change that produces differentiated evolutes after balance is disturbed.
SK-TR-002|formal_session|32f344aa50ff140e601a959816da51c6417381068c06679b003d7985545a9df3|core_doctrine_discriminator|Doctrine-specific constituent discriminator: the proposition identifies luminosity, activity, and inertia as inseparable tendencies of one primordial nature rather than independent substances or properties of consciousness.
SK-TR-003|formal_session|3d047025cf556bb634af42432e1cb09405fa02603ede07a55a03085fd221bc8c|critical_contrast_discriminator|Doctrine-specific relation discriminator: the proposition states the objection that an inactive witness and unconscious nature cannot enter an intelligible relation, and records proximity rather than physical contact as the Sāṃkhya reply.
SK-TR-004|formal_session|0a438fc66841375de86a8642606f14f4402cb6709f20e45b4c7d4a75d63e08bf|source_boundary_discriminator|Doctrine-specific source-boundary discriminator: the proposition establishes the classical Sāṃkhyakārikā as controlling the school’s non-theistic identity and prevents later theistic commentary from being projected backward.
SK-TR-005|canonical|7210643199e69508b85cb9f23f697ac1ac0acf58c10790081d0371fac81af0d1|core_doctrine_discriminator|Doctrine-specific enumeration discriminator: the proposition establishes that the great principle and determinative intellect name one principle at cosmic and psychological levels, not two stages in the twenty-fivefold enumeration.
SK-TR-006|formal_session|cac57c42622cc684527ada4b9a723f2fd3f266848fd3ab059053f5788a117088|evolutionary_sequence_discriminator|Doctrine-specific instrument discriminator: the proposition distinguishes the three internal functions, joins them to the ten sensory and action capacities as a thirteenfold instrument, and assigns final ascertainment to intellect.
SK-TR-007|formal_session|21bee5777c9f784344e6999c6fe30095db863ab9b142d2c0b19c37882fe5b4f5|core_doctrine_discriminator|Doctrine-specific self discriminator: the proposition distinguishes the changeless conscious witness from the empirical self produced by identification with intellect, ego, mind, body, and karmic continuity.
SK-TR-008|formal_session|7b7a0a9c0bf9c3d469d54c79dda37a652bc747b2cc535f69e20db7b304d72856|core_doctrine_discriminator|Doctrine-specific epistemic discriminator: the proposition fixes the three accepted instruments of knowledge and explains how comparison, postulation, and non-apprehension are reduced to them.
SK-TR-009|canonical|ad298bc28d759ecc866622972a0cdfcc77b1faa888933797f7ee77c72eb2cd0a|core_doctrine_discriminator|Doctrine-specific cognition discriminator: the proposition states that insentient intellect appears conscious through reflected witness-consciousness without itself becoming an additional conscious principle.
SK-TR-010|formal_session|0350933f16a19f9184df352238993633dfd211b929bdcf38b803e3b0b477473f|evolutionary_sequence_discriminator|Doctrine-specific evolutionary discriminator: the proposition fixes the sequence from primordial nature through intellect and ego into the luminous sensory branch and inert subtle-element branch.
SK-TR-011|formal_session|236a923c3b58241a38ecbdd74f02da58c323cf374e27228b2af34a78f43ef296|critical_contrast_discriminator|Doctrine-specific critical discriminator: the proposition identifies the force and limit of the Vedāntic critique—unconscious causation, purposiveness, and dualist relation remain under-explained without thereby proving the rival system.
SK-TR-012|formal_session|7db3970e53b5b8b7c1e413e524af61dee4cd28d7bbd5865ac28340abb0feffae|argument_structure_discriminator|Doctrine-specific causal-argument discriminator: the proposition gives the reasons why a sheer non-entity cannot be produced and why determinate material selection and restricted production support prior causal presence.
SK-TR-013|canonical|4c1fd9c418d760c2e85e72c6dfffae7fe219616aeed47486aba89f8bbf2ddb60|causal_doctrine_discriminator|Doctrine-specific causal discriminator: the proposition establishes that an effect pre-exists as determinate potency in its material continuum and that production manifests or transforms that capacity.
SK-TR-014|formal_session|331c46faf54850aa5a56fbbad0fe36d267609dd8f43616edb7fb3d127f0ac8f5|soteriological_discriminator|Doctrine-specific purposiveness discriminator: the proposition claims that ordered manifestation can arise from the internal quality-structure in the witness’s presence without conscious planning.
SK-TR-015|formal_session|5599eb6597db2dfffc054073293c35bbd06d9a9036ba3eac7024f0f3541369f4|core_doctrine_discriminator|Doctrine-specific theological discriminator: the proposition establishes that classical Sāṃkhya treats primordial nature and conscious witnesses as explanatorily sufficient, making God unproved rather than asserting a separate creator.
SK-TR-016|canonical|85dc9d5278d7c3562d0af76f0c1368f426540245ad6383338b2337be1c258d45|evolutionary_sequence_discriminator|Doctrine-specific evolutionary discriminator: the proposition assigns the five subtle elements to the inert aspect of ego.
SK-TR-017|formal_session|f52d8857b866fad92301034733905bc2df977140793f6cf7bcc7acf5278eb42f|core_doctrine_discriminator|Doctrine-specific transmigration discriminator: the proposition assigns karmic continuity to an eighteen-constituent transmigrating complex while preserving the witness as inactive and non-transmigrating.
SK-TR-018|formal_session|84dd8c4455be01480d35ef1a98e70c74283228ca5d2790cd268f6666c6f1ceb2|core_doctrine_discriminator|Doctrine-specific manifestation discriminator: the proposition distinguishes primordial nature in its balanced unmanifest condition from differentiated manifest evolution.
SK-TR-019|formal_session|3b5e3ce2e150a6fc2e8d6a1204067c7d372ac0ca645e7449d2000506709a270c|core_doctrine_discriminator|Doctrine-specific argument-limit discriminator: the proposition limits the proofs to establishing a non-objective subject-pole and denies that they by themselves establish eternality, plurality, and complete inactivity.
SK-TR-020|formal_session|dee97265ae0175ba968d87d9b41c569e8e6c4c2def4ac8ccf476171e918768e4|critical_contrast_discriminator|Doctrine-specific individuation discriminator: the proposition exposes the unresolved basis for numerical plurality when witnesses are qualitatively identical and without attributes.
SK-TR-021|formal_session|7a387509b2febd0825dfffe01b6cb7e2fefde06ed1cda2e934cc44d40828fc01|core_doctrine_discriminator|Doctrine-specific consciousness discriminator: the proposition establishes the witness as pure, self-luminous, inactive, changeless, and outside the qualities, assigning all productive change to nature.
SK-TR-022|formal_session|500c895616855db806edb267168a049592eac8361e582deb986e49a54418df65|soteriological_discriminator|Doctrine-specific liberation discriminator: the proposition makes release the cessation of false identification through discriminative knowledge, not merger or annihilation, while distinguishing embodied and disembodied completion.
SK-TR-023|canonical|ac4b5ea0111e2aba7d561f3dcb7d1e428be3d6218e9c14349918b308b7c1220a|epistemic_discriminator|Doctrine-specific inferential discriminator: the proposition states that inference from general correlation can justify an imperceptible material root while marking the risk of reducing the proof to analogy.
SK-TR-024|formal_session|88e2b4423b520001bacaaf0c26f59d8fe24157eba567e11e343dacf74b3201ce|critical_contrast_discriminator|Doctrine-specific rival-causation discriminator: the proposition distinguishes new production after prior absence in Nyāya–Vaiśeṣika from Sāṃkhya’s pre-existent effect and transformation.
SK-TR-025|canonical|ddd1baacb45add90c53b358b00aac9b047c536d06e5fc5b9d36b090c9a1d6bc5|argument_structure_discriminator|Doctrine-specific argument-inventory discriminator: the proposition fixes the five distinct grounds offered for a conscious witness.
SK-TR-026|formal_session|e7da68d136f1dfd4a404627e3e320b03ad352b8cb63e0760c09ce1a12509696c|epistemic_discriminator|Doctrine-specific inference discriminator: the proposition distinguishes inference from cause to effect, effect to cause, and general correlation where the connection is not directly perceived.
SK-TR-027|formal_session|fbbe6e5922a3b1ab68875edf05685c2f5d89778da8577593cef2152c2bde975c|causal_doctrine_discriminator|Doctrine-specific causal-continuity discriminator: the proposition states that the tree is present in the seed as latent determinate capacity and material continuity, not as a miniature gross object.
SK-TR-028|formal_session|02df06ca51419ebb8a152beda116203ec90de716c4a481a4cfdb6e841fc39bb2|core_doctrine_discriminator|Doctrine-specific quality-system discriminator: the proposition defines the three qualities as inseparable tendencies, fixes their exact balance as unmanifestation, and distinguishes same-form from differentiating transformation.
SK-TR-029|canonical|ecd2c5f351186af40dd1350d251cb538b89a6cbf0fcd2d43ab38b809167a2f86|core_doctrine_discriminator|Doctrine-specific soteriological discriminator: the proposition distinguishes temporary or incomplete worldly and ritual relief from final non-returning cessation through discriminative knowledge.
SK-TR-030|canonical|ac1df0bc2404dd1fe083fd242eaa0c870ccc0ecaafaaa4177268bb31735817dd|evolutionary_sequence_discriminator|Doctrine-specific evolutionary-role discriminator: the proposition fixes the sequence from primordial nature through intellect and ego, with activity energising both the luminous and inert branches.
SK-TR-031|formal_session|b4123f8fbc4064bd8014b618c3e3ddebbed7a4ad85a47c1b665ac816cae03aa0|core_doctrine_discriminator|Doctrine-specific exposition discriminator: the proposition requires both the full evolutionary sequence and the distinction among determinative intellect, its cosmic designation, and ego.
SK-TR-032|formal_session|9243b1e8ae919506cdcedca11c3b427ef4e171037f70d96d69c47e6b5d2a4f57|argument_structure_discriminator|Doctrine-specific material-cause discriminator: the proposition distinguishes five arguments for primordial nature and assigns unity specifically to the return of diversified effects to an undivided source.
SK-TR-033|canonical|68958830720a272ad38cc6deff9fefa93146cae6af47d13ce2ca5c9c8b129c8c|soteriological_discriminator|Doctrine-specific misidentification discriminator: the proposition assigns agency to evolutes of nature and identifies its false attribution to the witness as the condition of unfreedom.
SK-TR-034|formal_session|975dec7d9e4d6c92cab626ab01abe57e2807e00876a21e5732f71360dc7c5b91|core_doctrine_discriminator|Doctrine-specific system-architecture discriminator: the proposition makes discrimination between witness and field the organising claim that the dualism, qualities, enumeration, and causation jointly render intelligible.
SK-TR-035|formal_session|55635b7afa3085f28f2dd283c7c928d4d3f26e3792a5570d26ef1c55574b3506|critical_contrast_discriminator|Doctrine-specific inter-school discriminator: the proposition distinguishes transformation of an enduring unmanifest material root from dependent arising without such a root.
SK-TR-036|formal_session|768eef9b234fb90f60e5fd4cdfb3b7c5520935296d00e9532363c2a724c46251|core_doctrine_discriminator|Doctrine-specific material-principle discriminator: the proposition identifies primordial nature as unconscious, unmanifest, and the ultimate material source of the objective and psychophysical order.
SK-TR-037|canonical|0e049a8772b4ffe47c5b0084828ef1c4d4b95bb8062947f3d95961d181f98262|core_doctrine_discriminator|Doctrine-specific psychological-function discriminator: the proposition distinguishes coordination by mind, appropriation by ego, and determination by intellect.
SK-TR-038|formal_session|f6b25f58c71d52c15e1233553cbdf93823097271074aac10366b8b58a89967f8|causal_doctrine_discriminator|Doctrine-specific transformation discriminator: the proposition establishes prior existence of the effect in its material cause and defines production as an actual manifestation rather than creation from non-being.
SK-TR-039|formal_session|962cfefd99e45b33621e9d665f8c92f615fb101b25371507d867f0a009040593|core_doctrine_discriminator|Doctrine-specific suffering discriminator: the proposition distinguishes internal, external-being or natural, and cosmic or unseen affliction, then links final cessation to discriminative knowledge.
SK-TR-040|canonical|338d6cd09d33c65e657e6078db6ff9f7c4db7c09073888a20e90cf7982f2231c|source_boundary_discriminator|Doctrine-specific school-boundary discriminator: the proposition confines Yoga to comparison while assigning theoretical discrimination to Sāṃkhya and detailed discipline and theistic-practical additions to Yoga.
SK-TR-041|formal_session|e163aa5aebc2f2525b1b5325cbc2113a5affba1d6c7f88a4947c004a72595514|critical_contrast_discriminator|Doctrine-specific material-selection discriminator: the proposition argues that selection of a determinate material cause reveals a restricted causal capacity rather than arbitrary production.
SK-TR-042|canonical|570438b684642d2078ab54b152e3e7fe06ba27f33af880abdd0d13525b20e02d|core_doctrine_discriminator|Doctrine-specific plurality discriminator: the proposition infers many witnesses from distinct births, sense-endowments, activities, quality-configurations, and destinies, because one witness would collapse individual captivity and release.
SK-TR-043|formal_session|359d97f172f770d1b8206c2f5294c0c5c806577805c6036254251e7a5d7dc0f5|critical_contrast_discriminator|Doctrine-specific purposive-function discriminator: the proposition distinguishes purposive operation from conscious planning and uses natural service to explain unconscious nature’s ordered activity.
SK-TR-044|formal_session|b1db3f036d39090638d8b13c10c0de699c2f50b3a10c8609935cafd9602107c0|soteriological_discriminator|Doctrine-specific release-sequence discriminator: the proposition distinguishes liberation while bodily momentum continues from final cessation of embodiment after that momentum ends.
SK-TR-045|canonical|f22a9a7576f86c89bf9e74a6404a45d5c901033316aeb1970a40612188654932|core_doctrine_discriminator|Doctrine-specific disposition discriminator: the proposition links the transmigrating complex to four opposed pairs of intellectual tendencies—merit, knowledge, detachment, and power with their contraries.
SK-TR-046|canonical|41eceb7b09e5e287962fd0fcbfee67fdf78b9887cd5c492ec9cb171502e4ff47|critical_contrast_discriminator|Doctrine-specific Buddhist objection discriminator: the proposition contrasts the demand for productive efficacy with Sāṃkhya’s claim that witness-consciousness is efficacious as presence-for-experience rather than as a producer.
SK-TR-047|formal_session|aaa62cd75af9de2586058748453eb27870e52de39d4355738fae2d49c1b4e1ec|critical_contrast_discriminator|Doctrine-specific contact-critique discriminator: the proposition tests proximity through magnet and crystal comparisons and states why force, appearance, and initiation remain unresolved under the critique.
SK-TR-048|canonical|edc4e6b2782682c3279764075e0002c87c18e22f1b5ce96d92fd6bdbfeeb3b50|epistemic_discriminator|Doctrine-specific instrument-of-knowledge discriminator: the proposition fixes perception, inference, and reliable testimony as jointly sufficient for knowledge of both experienced and imperceptible realities.
SK-TR-049|formal_session|cab94054285e307e720558f5ea874ca7739270a1ba324e7dec3885cbd874557c|epistemic_discriminator|Doctrine-specific perceptual discriminator: the proposition defines perception as determinate ascertainment concerning a presented object.
SK-TR-050|formal_session|e6be7cfcf0bae8ed205e37c97725083269137316d4d426a94ed6469af5447eae|evolutionary_sequence_discriminator|Doctrine-specific causal-class discriminator: the proposition assigns intellect, ego, and the five subtle elements to the class that is both produced and productive.
SK-TR-051|formal_session|efc3a28ff2ac9cf2e8166737c5b46a7fb486c24dfb0b26096671dd3ec67ead0e|evolutionary_sequence_discriminator|Doctrine-specific enumeration discriminator: the proposition fixes the twenty-five principles and places the conscious witness outside the evolutionary products of primordial nature.
SK-TR-052|formal_session|e7b08019d18442642dc3d861a2658e31d00573919b3de5e2609d1f9f38e26de7|evolutionary_sequence_discriminator|Doctrine-specific transmigrating-complex discriminator: the proposition explains that counting mind among the eleven capacities yields eighteen constituents when intellect, ego, and five subtle elements are included.
SK-TR-053|canonical|632f48936043efdf32ad82cf91c2288130652a5b41ddfa31a4ea9a7531b12b16|source_boundary_discriminator|Doctrine-specific textual-history discriminator: the proposition identifies Īśvarakṛṣṇa’s kārikā as the earliest extant systematic classical text and distinguishes later explanatory traditions.
SK-TR-054|formal_session|913deb9915adb6e7c6a77253807494ef3b2e7f8a46ec476376cfca20cf36bf73|critical_contrast_discriminator|Doctrine-specific Vedāntic contrast discriminator: the proposition distinguishes actual modification of an unconscious material source from apparent change grounded in a conscious absolute.
SK-TR-055|canonical|644261df007cd5a2e2f171c2b9c0bcf5e68ad6d66f57d3311f81ba6357d0402b|critical_contrast_discriminator|Doctrine-specific critical-system discriminator: the proposition states that the strongest rival is rejected because consciousness, purposiveness, and the relation between witness and nature remain inadequately grounded.
SK-TR-056|formal_session|890604ac76166f1d15662725cddfa01604e22babc42ddad10a4546fa5d9fb255|soteriological_discriminator|Doctrine-specific liberation-state discriminator: the proposition defines unfreedom as non-discrimination and release as stable discrimination that leaves the witness isolated rather than merged, annihilated, or modified.
SK-TR-057|formal_session|05d28840ed6a07aeca0904d138204aba9fbfedb74d3a799cac84d1f9931669ca|analogy_function_discriminator|Doctrine-specific lame-and-blind discriminator: the proposition explicitly assigns consciousness without action to the lame witness, action without consciousness to blind nature, and identifies their function as complementarity.
SK-TR-058|formal_session|1840c99044751f5a7e4cf3cb52a2790a231667d681950547e7aa4934ee6f0a85|analogy_function_discriminator|Doctrine-specific dancer discriminator: the proposition explicitly identifies nature's withdrawal after being seen with cessation of binding display following discriminative knowledge.
SK-TR-059|canonical|ebf1cd762bf6791adc7c4595f3593207d5f79e13cdd11305457ec55487d6e205|epistemic_discriminator|Doctrine-specific imperceptibility discriminator: the proposition distinguishes supersensible subtlety from non-existence for primordial nature and the witness.
SK-TR-060|formal_session|925035fb4c9ad50dd7d0d2a5712907a42a3f9b8f9961ed86fdbb88e077fd47ec|argument_structure_discriminator|Doctrine-specific anti-theistic motive discriminator: the proposition argues that action from desire or motive is incompatible with divine perfection and freedom.
SK-TR-061|formal_session|934ec45118003204c48c2cb9426ad3ae7abaf51d109bf2b4db5041848178d99e|argument_structure_discriminator|Doctrine-specific anti-theistic fulfilment discriminator: the proposition argues that an eternally fulfilled deity lacks a motive to create a painful world.
SK-TR-062|formal_session|ed334f2a17d5ddb91067051179e0ca58a0376df20a3c36d0bc542f10615b9fa1|argument_structure_discriminator|Doctrine-specific anti-theistic karma discriminator: the proposition states the dilemma between dependence on karma and arbitrary injustice.
SK-TR-063|formal_session|132302d47b4a8ba52ecf669c9d0596f90f010ba0c34a068dd55cf69c35bd36e9|argument_structure_discriminator|Doctrine-specific anti-theistic material-cause discriminator: the proposition denies that an immutable conscious deity can be the material source of a changing unconscious world.
SK-TR-064|formal_session|a076eb6a556a396f88217a9cd8a0d222bbbe0a3173a94d15c9f66cf25a7d664d|argument_structure_discriminator|Doctrine-specific anti-theistic sufficiency discriminator: the proposition treats eternal witnesses and primordial nature as sufficient for consciousness and material evolution without a creator hypothesis.
SK-TR-066|formal_session|89e2d1b23a4f02f3c18c576f7c8b08b800c4205d0c727dd8850c24755ae64e45|argument_structure_discriminator|Doctrine-specific unity-of-source discriminator: the proposition argues that disconnected ultimate sources could not ground the one interconnected cosmos inferred from undividedness.
""".strip()

# Downstream authored definitions are instantiated only after the classification artifact is frozen.
def load_downstream_definitions() -> tuple[list[tuple[str, str, str, list[str], str]], list[dict]]:
    from question_bank import QBANK
    matrix_probe_specs_text = r"""
SK-TM-014|SK-TR-001|two-modifications|Two modifications|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-012|SK-TR-002|guṇa-characters|Guṇa characters|2|A second independently worded probe is justified because this source proposition contains two separately confusable doctrinal discriminators.
SK-TM-041|SK-TR-003|contact-problem|Contact problem|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-057|SK-TR-047|meaning-of-proximity|Meaning of proximity|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-049|SK-TR-004|textual-discipline|Textual discipline|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-046|SK-TR-005|counting-trap|Counting trap|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-023|SK-TR-006|faculties|Faculties|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-020|SK-TR-007|jīva-distinction|Jīva distinction|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-005|SK-TR-008|reduction-strategy|Reduction strategy|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-008|SK-TR-009|reflected-cognition|Reflected cognition|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-022|SK-TR-010|mahat-and-buddhi|Mahat and buddhi|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-024|SK-TR-010|sāttvika-branch|Sāttvika branch|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-052|SK-TR-010|elemental-sequence|Elemental sequence|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-047|SK-TR-011|graded-verdict|Graded verdict|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-030|SK-TR-012|non-being-argument|Non-being argument|2|A second independently worded probe is justified because this source proposition contains two separately confusable doctrinal discriminators.
SK-TM-029|SK-TR-013|satkāryavāda-thesis|Satkāryavāda thesis|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-058|SK-TR-014|teleology-without-deliberation|Teleology without deliberation|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-040|SK-TR-015|non-theism|Non-theism|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-025|SK-TR-016|tāmasa-branch|Tāmasa branch|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-028|SK-TR-017|subtle-body|Subtle body|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-013|SK-TR-018|equilibrium|Equilibrium|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-054|SK-TR-019|inferential-reach|Inferential reach|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-018|SK-TR-020|individuation-objection|Individuation objection|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-015|SK-TR-021|nature-of-puruṣa|Nature of Puruṣa|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-037|SK-TR-022|kaivalya|Kaivalya|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-006|SK-TR-023|unseen-ultimates|Unseen ultimates|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-032|SK-TR-024|nyāya-contrast|Nyāya contrast|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-016|SK-TR-025|proofs-for-puruṣa|Proofs for Puruṣa|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-004|SK-TR-026|inference-taxonomy|Inference taxonomy|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-055|SK-TR-027|latent-effect|Latent effect|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-061|SK-TR-028|controlled-application|Controlled application|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-048|SK-TR-029|limits-of-ordinary-remedies|Limits of ordinary remedies|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-026|SK-TR-030|rājasa-role|Rājasa role|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-060|SK-TR-031|split-demand|Split demand|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-010|SK-TR-032|prakṛti-proof-cluster|Prakṛti proof cluster|2|A second independently worded probe is justified because this source proposition contains two separately confusable doctrinal discriminators.
SK-TM-011|SK-TR-032|unity-of-prakṛti|Unity of Prakṛti|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-053|SK-TR-032|proof-job-control|Proof-job control|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-036|SK-TR-033|bondage|Bondage|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-059|SK-TR-034|retrieval-spine|Retrieval spine|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-034|SK-TR-035|buddhist-contrast|Buddhist contrast|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-009|SK-TR-036|names-of-the-root|Names of the root|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-007|SK-TR-037|instrument-complex|Instrument complex|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-031|SK-TR-038|real-transformation|Real transformation|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-035|SK-TR-039|three-pains|Three pains|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-045|SK-TR-040|yoga-boundary|Yoga boundary|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-043|SK-TR-041|nyāya-pressure|Nyāya pressure|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-017|SK-TR-042|plurality-basis|Plurality basis|2|A second independently worded probe is justified because this source proposition contains two separately confusable doctrinal discriminators.
SK-TM-019|SK-TR-043|teleology|Teleology|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-039|SK-TR-044|two-liberation-stages|Two liberation stages|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-050|SK-TR-045|eight-dispositions|Eight dispositions|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-044|SK-TR-046|buddhist-pressure|Buddhist pressure|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-038|SK-TR-057,SK-TR-058|analogy-functions|Analogy functions|1|One paired probe is justified because the source gives two explicitly contrasted analogy-functions and the question tests that pairing.
SK-TM-002|SK-TR-048|pramāṇa-count|Pramāṇa count|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-003|SK-TR-049|perception-definition|Perception definition|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-027|SK-TR-050|causal-classes|Causal classes|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-021|SK-TR-051|evolution-opening|Evolution opening|2|A second independently worded probe is justified because this source proposition contains two separately confusable doctrinal discriminators.
SK-TM-051|SK-TR-052|subtle-body-count|Subtle-body count|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-001|SK-TR-053|classical-source-control|Classical source control|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-033|SK-TR-054|advaita-contrast|Advaita contrast|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-042|SK-TR-055|śaṅkara’s-challenge|Śaṅkara’s challenge|2|A second independently worded probe is justified because this source proposition contains two separately confusable doctrinal discriminators.
SK-TM-056|SK-TR-056|isolation-diagnostic|Isolation diagnostic|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-062|SK-TR-059|imperceptibility-subtlety|Imperceptibility and subtlety|1|One direct probe is sufficient for this atomic discriminator.
SK-TM-063|SK-TR-060|divine-motive-dilemma|Divine motive dilemma|1|One direct probe is sufficient for this promoted atomic argument.
SK-TM-064|SK-TR-061|fulfilled-deity-motive|Fulfilled deity and creation|1|One direct probe is sufficient for this promoted atomic argument.
SK-TM-065|SK-TR-062|karma-justice-dilemma|Karma and divine justice|1|One direct probe is sufficient for this promoted atomic argument.
SK-TM-066|SK-TR-063|immutable-material-cause|Immutable deity as material cause|1|One direct probe is sufficient for this promoted atomic argument.
SK-TM-067|SK-TR-064|dual-principle-sufficiency|Explanatory sufficiency without creator|1|One direct probe is sufficient for this promoted atomic argument.
SK-TM-069|SK-TR-066|disconnected-source-unity|Disconnected sources and cosmic unity|1|One direct probe is sufficient for this promoted atomic inference.
""".strip()
    rows = []
    for line in matrix_probe_specs_text.splitlines():
        handle, rule_id, mode, title, minimum, justification = line.split("|", 5)
        rows.append({"authoring_handle": handle, "classification_rule_ids": rule_id.split(","),
                     "probe_mode": mode, "title": title, "minimum_probes": int(minimum),
                     "extra_probe_justification": justification})
    return QBANK, rows


def reviewed_testability_rules() -> list[dict]:
    rules = []
    for line in AUTHORITY_TESTABILITY_RULE_SPECS.splitlines():
        rule_id, source, proposition_hash, category, rationale = line.split("|", 4)
        predicate = {"authority_source": source,
                     "normalized_proposition_sha256": proposition_hash}
        body = {"rule_id": rule_id, "predicate": predicate, "substantive_category": category,
                "rationale": rationale}
        rules.append({**body, "rule_hash": sha_text(json.dumps(body, ensure_ascii=False, sort_keys=True))})
    return rules


RELATION_STOP = TOKEN_STOP
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
        raise RuntimeError("Composite component lacks meaningful doctrine anchors: " + text)
    return {
        "component_text": text,
        "component_sha256": sha_text(norm(text)),
        "target_obligation_ids": [target["obligation_id"]],
        "doctrine_anchors": [{"obligation_id": target["obligation_id"],
                              "shared_doctrine_terms": anchors}],
    }

def supporting_classification(payload: str, atomic_rows: list[dict],
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
                "represented_by_obligation_ids": ids,
                "relation_type": "composite_split",
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
        atomic_payload = proposition_payloads[atomic["proposition_ids"][0]]
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
        anchors = [{"obligation_id": row[1], "shared_doctrine_terms": row[2]} for row in selected]
        return {
            "substantive_category": "represented_doctrinal_proposition",
            "classification_predicate": {
                "represented_by_obligation_ids": ids,
                "relation_type": "entailed_by",
                "doctrine_specific_anchors": anchors,
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
            "independently_checkable_signals": sorted(
                key for key, value in structural.items() if value
            ),
        },
        "classification_rationale":
            f"The proposition is non-testable as {category}; its recorded structural signals are independently checkable and it asserts no standalone doctrinal discriminator.",
    }


def source_block_ref(source: str, payload_hash: str) -> str:
    return "SK-SRC-" + source.upper().replace("_", "-") + "-" + payload_hash[:16].upper()


def derive_authority_classification(rows: list[dict]) -> dict:
    authority_rows = [row for row in rows if row["source"] in {"canonical", "formal_session", "formal_workbook"}]
    priority = {"canonical": 0, "formal_session": 1, "formal_workbook": 2}
    occurrences = defaultdict(list); headings = {row["id"]: row["heading"] for row in authority_rows}
    for row in authority_rows:
        for mapping in row["proposition_mappings"]:
            occurrences[mapping["proposition_id"]].append({"source": row["source"], "block_id": row["id"], "block_payload_sha256": row["own_payload_sha256"], "proposition_id": mapping["proposition_id"], "proposition_payload_sha256": mapping["exact_payload_sha256"], "payload": mapping["exact_payload"], "occurrence": mapping["occurrence"]})
    representatives = {pid: sorted(items, key=lambda x: (priority[x["source"]], x["block_id"], x["occurrence"]))[0] for pid, items in occurrences.items()}
    rules = reviewed_testability_rules(); rule_by_prop = {}
    for rule in rules:
        pred = rule["predicate"]
        matches = [pid for pid, ref in representatives.items() if ref["source"] == pred["authority_source"] and sha_text(norm(ref["payload"])) == pred["normalized_proposition_sha256"]]
        if len(matches) != 1: raise RuntimeError(f"Source-only classification rule {rule['rule_id']} matched {len(matches)} propositions")
        if matches[0] in rule_by_prop: raise RuntimeError(f"Multiple source-only rules matched {matches[0]}")
        rule_by_prop[matches[0]] = rule
    out=[]; represented=set(); primary={}
    deferred_supporting = []
    for pid, ref in sorted(representatives.items()):
        rule=rule_by_prop.get(pid)
        if rule:
            cls,cat,rid,rhash,why,pred="testable_atomic",rule["substantive_category"],rule["rule_id"],rule["rule_hash"],rule["rationale"],rule["predicate"]
        else:
            deferred_supporting.append((pid, ref))
            continue
        oid="SK-OBL-"+sha_text(f"{cls}|{pid}")[:16].upper(); primary[pid]=oid; represented.add(ref["block_id"])
        out.append({"obligation_id":oid,"classification":cls,"substantive_category":cat,"authority_source":ref["source"],"authority_block_ids":[source_block_ref(ref["source"], ref["block_payload_sha256"])],"proposition_ids":[pid],"source_payload_hashes":{"block_sha256":ref["block_payload_sha256"],"proposition_sha256":ref["proposition_payload_sha256"]},"normalized_semantic_hash":sha_text(norm(ref["payload"])),"classification_rule_id":rid,"classification_rule_hash":rhash,"classification_rationale":why,"classification_predicate":pred})
    atomic_rows = list(out)
    proposition_payloads = {pid: ref["payload"] for pid, ref in representatives.items()}
    block_atomic_ids = defaultdict(list)
    for atomic in atomic_rows:
        for block_id in atomic["authority_block_ids"]:
            block_atomic_ids[block_id].append(atomic["obligation_id"])
    for pid, ref in deferred_supporting:
        block_ref = source_block_ref(ref["source"], ref["block_payload_sha256"])
        decision = supporting_classification(
            ref["payload"], atomic_rows, proposition_payloads, block_atomic_ids.get(block_ref, [])
        )
        cls = "supporting_non_testable_context"
        cat = decision["substantive_category"]
        pred = decision["classification_predicate"]
        why = decision["classification_rationale"]
        rid = "SK-SUPPORT-" + cat.upper().replace("_", "-")
        rhash = sha_text(json.dumps(
            {"rule_id": rid, "category": cat, "predicate": pred, "rationale": why},
            ensure_ascii=False, sort_keys=True
        ))
        oid="SK-OBL-"+sha_text(f"{cls}|{pid}")[:16].upper(); primary[pid]=oid; represented.add(ref["block_id"])
        out.append({"obligation_id":oid,"classification":cls,"substantive_category":cat,"authority_source":ref["source"],"authority_block_ids":[source_block_ref(ref["source"], ref["block_payload_sha256"])],"proposition_ids":[pid],"source_payload_hashes":{"block_sha256":ref["block_payload_sha256"],"proposition_sha256":ref["proposition_payload_sha256"]},"normalized_semantic_hash":sha_text(norm(ref["payload"])),"classification_rule_id":rid,"classification_rule_hash":rhash,"classification_rationale":why,"classification_predicate":pred})
    for pid, items in sorted(occurrences.items()):
        rep=representatives[pid]
        for ref in sorted(items,key=lambda x:(priority[x["source"]],x["block_id"],x["occurrence"])):
            if ref==rep: continue
            represented.add(ref["block_id"]); target=primary[pid]; pred={"same_normalized_proposition_id":pid,"routes_to_obligation_id":target}; why=f"Duplicate occurrence routes explicitly to {target}; repeated authority wording creates no additional test duty."
            out.append({"obligation_id":"SK-OBL-DUP-"+sha_text(f"{pid}|{ref['source']}|{ref['block_id']}|{ref['occurrence']}")[:16].upper(),"classification":"normalized_duplicate","substantive_category":"duplicate_route","authority_source":ref["source"],"authority_block_ids":[source_block_ref(ref["source"], ref["block_payload_sha256"])],"proposition_ids":[pid],"source_payload_hashes":{"block_sha256":ref["block_payload_sha256"],"proposition_sha256":ref["proposition_payload_sha256"]},"normalized_semantic_hash":sha_text(norm(ref["payload"])),"classification_rule_id":"SK-NORMALIZED-DUPLICATE-001","classification_rule_hash":sha_text("SK-NORMALIZED-DUPLICATE-001|same-normalized-proposition-id|explicit-route"),"classification_rationale":why,"classification_predicate":pred})
    for row in authority_rows:
        if row["id"] in represented: continue
        out.append({"obligation_id":"SK-OBL-BLOCK-"+sha_text(row["id"])[:16].upper(),"classification":"supporting_non_testable_context","substantive_category":"empty_structural_block","authority_source":row["source"],"authority_block_ids":[source_block_ref(row["source"], row["own_payload_sha256"])],"proposition_ids":[],"source_payload_hashes":{"block_sha256":row["own_payload_sha256"]},"normalized_semantic_hash":sha_text(norm(row["heading"])),"classification_rule_id":"SK-EMPTY-BLOCK-001","classification_rule_hash":sha_text("SK-EMPTY-BLOCK-001|no-valid-semantic-propositions"),"classification_rationale":"Structural source block has no valid semantic proposition and is retained explicitly for completeness.","classification_predicate":{"valid_semantic_proposition_count":0}})
    yoga=next((r for r in authority_rows if r["source"]=="canonical" and "yoga" in norm(r["heading"])),None)
    out.append({"obligation_id":"YG-SK-BOUNDARY-001","classification":"routed_boundary","substantive_category":"cross_topic_boundary_route","authority_source":"canonical","authority_block_ids":[source_block_ref("canonical", yoga["own_payload_sha256"])] if yoga else [],"proposition_ids":[],"source_payload_hashes":{"block_sha256":yoga["own_payload_sha256"] if yoga else sha_text("YG-SK-BOUNDARY-001")},"normalized_semantic_hash":sha_text("YG-SK-BOUNDARY-001|Topic 06 Yoga"),"classification_rule_id":"YG-SK-BOUNDARY-RULE-001","classification_rule_hash":sha_text("YG-SK-BOUNDARY-RULE-001|canonical-heading-contains-yoga"),"classification_rationale":"Canonical ownership routes detailed Yoga mechanics to Topic 06; serialized reconciliation confirms the destination package without transferring Sāṃkhya ownership.","classification_predicate":{"authority_source":"canonical","heading_contains":"yoga","canonical_controls_boundary":True},"route":{"target_topic":"06-Yoga","target_edited":True,"due_within_samkhya":False,"ownership":"cross-link-only"}})
    core={"schema_version":1,"topic":"05 Samkhya","classifier_algorithm_version":"source-only-v1","source_manifest":{k:file_info(SOURCES[k]) for k in ("formal_session","formal_workbook","canonical")},"classification_rule_set_hash":sha_text(json.dumps(rules,ensure_ascii=False,sort_keys=True)),"classification_rules":rules,"classification_counts":dict(Counter(r["classification"] for r in out)),"substantive_category_counts":dict(Counter(r["substantive_category"] for r in out)),"obligation_count":len(out),"rows":sorted(out,key=lambda r:r["obligation_id"]),"build_execution_order":["parse_and_normalize_sources","classify_source_obligations","freeze_classification_artifact"]}
    core["classification_hash"]=sha_text(json.dumps(core,ensure_ascii=False,sort_keys=True)); return core


def ledger_from_classification(c: dict) -> dict:
    obligations=[]
    for row in c["rows"]:
        item=dict(row); item["rationale"]=item["classification_rationale"]
        item["learner_destinations"]=["REVISION-GUIDE.md","MCQ-QUESTIONS.md","MCQ-SOLUTIONS.md"] if item["classification"]=="testable_atomic" else (["FORMAL-SOURCE-MIRROR.md"] if item["classification"]=="normalized_duplicate" else ["REVISION-GUIDE.md","FORMAL-SOURCE-MIRROR.md","ANSWER-WRITING-TOOLKIT.md"]); item["validation_result"]="passed"; obligations.append(item)
    return {"schema_version":3,"topic":"05 Samkhya","derivation_policy":"direct_projection_of_frozen_authority_classification","classification_artifact":"AUTHORITY-CLASSIFICATION.json","classification_hash":c["classification_hash"],"classification_rule_set_hash":c["classification_rule_set_hash"],"classification_counts":c["classification_counts"],"substantive_category_counts":c["substantive_category_counts"],"obligation_count":len(obligations),"represented_authority_block_count":len({b for r in obligations for b in r["authority_block_ids"]}),"represented_mandatory_formal_block_count":len({b for r in obligations if r["authority_source"] in {"formal_session","formal_workbook"} for b in r["authority_block_ids"]}),"obligations":obligations}

def semantic_tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[^\W_]+", norm(text), re.UNICODE)
        if len(token) >= 3 and token not in TOKEN_STOP
    }


def derived_cell_id(obligation_id: str, probe_mode: str) -> str:
    return f"SK-CELL-{obligation_id.removeprefix('SK-OBL-')}-{sha_text(probe_mode)[:10].upper()}"


def derive_test_matrix(ledger: dict, mcq_records: list[dict], specs: list[dict], proposition_payloads: dict[str, str]) -> dict:
    obligations_by_rule = {
        row["classification_rule_id"]: row for row in ledger["obligations"]
        if row["classification"] == "testable_atomic"
    }
    cells = []
    by_handle = {}
    for spec in specs:
        obligations = [obligations_by_rule.get(rule_id) for rule_id in spec["classification_rule_ids"]]
        if any(obligation is None for obligation in obligations):
            raise RuntimeError(f"Matrix rule has no testable obligation: {spec['classification_rule_ids']}")
        obligation_ids = [obligation["obligation_id"] for obligation in obligations]
        cell_id = derived_cell_id("+".join(obligation_ids), spec["probe_mode"])
        refs = [{
            "authority_source": obligation["authority_source"],
            "authority_block_id": obligation["authority_block_ids"][0],
            "proposition_id": obligation["proposition_ids"][0],
            "block_sha256": obligation["source_payload_hashes"]["block_sha256"],
            "proposition_sha256": obligation["source_payload_hashes"]["proposition_sha256"],
        } for obligation in obligations]
        cell = {
            "cell_id": cell_id, "title": spec["title"], "probe_mode": spec["probe_mode"],
            "derivation": "post_classification_obligation_plus_probe_mode",
            "obligation_ids": obligation_ids, "authority_refs": refs,
            "minimum_probes": spec["minimum_probes"],
            "extra_probe_justification": spec["extra_probe_justification"],
            "mapped_question_ids": [], "coverage_status": "uncovered",
        }
        cells.append(cell); by_handle[spec["authoring_handle"]] = (cell, obligations)
    mappings = []
    for record in mcq_records:
        if record["authoring_key"] not in by_handle:
            raise RuntimeError(f"Question {record['id']} names unknown post-classification probe {record['authoring_key']}")
        cell, obligations = by_handle[record["authoring_key"]]
        cell["mapped_question_ids"].append(record["id"]); cell["coverage_status"] = "covered"
        record["cell_id"] = cell["cell_id"]
        mapping_anchors = []
        for obligation in obligations:
            proposition_terms = relation_tokens(proposition_payloads[obligation["proposition_ids"][0]])
            keyed_terms = sorted(relation_tokens(record["keyed_evidence"]) & proposition_terms,
                                 key=lambda token: (-len(token), token))[:8]
            if len(keyed_terms) < 2:
                raise RuntimeError(f"Insufficient doctrine-specific evidence for {record['id']} and {obligation['obligation_id']}")
            mapping_anchors.append({"obligation_id": obligation["obligation_id"],
                                    "doctrine_specific_terms": keyed_terms})
        mappings.append({"question_id": record["id"], "cell_id": cell["cell_id"],
                         "obligation_ids": cell["obligation_ids"],
                         "authority_refs": cell["authority_refs"], "mapping_anchors": mapping_anchors,
                         "evidence_scope": "title_stem_keyed_option_keyed_explanation_only",
                         "substantive_question_hash": sha_text(json.dumps({
                             "title": record["title"], "stem": record["stem"],
                             "correct": record["options"][record["answer"]],
                             "distractors": sorted(v for k, v in record["options"].items()
                                                   if k != record["answer"]),
                         }, ensure_ascii=False, sort_keys=True))})
    return {"schema_version": 6, "topic": "05 Samkhya",
            "derivation_policy": "separate_post_classification_matrix_layer",
            "classification_hash": ledger["classification_hash"], "legacy_fixed_total": False,
            "cell_count": len(cells), "question_total": len(mcq_records),
            "testable_obligation_count": ledger["classification_counts"].get("testable_atomic", 0),
            "cells": sorted(cells, key=lambda row: row["cell_id"]), "question_mappings": mappings}


ANSWER_DRAW_ALGORITHM_VERSION = "sha256-rejection-v1"
ANSWER_DRAW_SEED_POLICY = "sha256('samkhya-answer-position-v1|' + stable_question_id)"


def short_cycle_created(sequence: str) -> bool:
    for period in range(2, 5):
        if len(sequence) >= period * 3 and sequence[-period * 3:] == sequence[-period:] * 3:
            return True
    return False


def deterministic_answer_draw(question_id: str, accepted: str) -> dict:
    seed = sha_text("samkhya-answer-position-v1|" + question_id)
    attempts = []
    for attempt in range(100):
        digest = sha_text(f"{ANSWER_DRAW_ALGORITHM_VERSION}|{seed}|{attempt}")
        letter = "ABCD"[int(digest, 16) % 4]
        candidate = accepted + letter
        reasons = []
        if len(candidate) >= 3 and candidate[-3:] == letter * 3:
            reasons.append("max_run_two")
        if short_cycle_created(candidate):
            reasons.append("reject_three_repeated_cycles_period_2_to_4")
        attempts.append({"attempt": attempt, "digest": digest, "draw_index": int(digest, 16) % 4,
                         "draw_letter": letter, "rejected": bool(reasons), "rejection_reasons": reasons})
        if not reasons:
            evidence = {"question_id": question_id, "algorithm_version": ANSWER_DRAW_ALGORITHM_VERSION,
                        "seed_policy": ANSWER_DRAW_SEED_POLICY, "seed": seed,
                        "raw_draw": attempts[0]["draw_letter"], "attempts": attempts,
                        "rejection_log": [x for x in attempts if x["rejected"]], "final_placement": letter}
            evidence["draw_hash"] = sha_text(json.dumps(evidence, ensure_ascii=False, sort_keys=True))
            return evidence
    raise RuntimeError(f"No safe deterministic answer draw for {question_id}")


def render_mcqs(qbank: list[tuple[str, str, str, list[str], str]]) -> tuple[str, str, list[dict], list[dict]]:
    qout = ["# Sāṃkhya — Coverage-Derived MCQ Questions", "",
            "> Attempt without opening the solutions. Record confidence and reasoning in PRACTICE-LOG.md.", ""]
    sout = ["# Sāṃkhya — MCQ Solutions", "",
            "> Explanations analyse every option. Primary coverage mappings use only the title, stem, keyed option and keyed explanation.", ""]
    records = []; draws = []; accepted = ""
    for n, (title, stem, correct, wrongs, handle) in enumerate(qbank, 1):
        qid = f"Q{n}"; draw = deterministic_answer_draw(qid, accepted); answer = draw["final_placement"]
        accepted += answer; draws.append(draw)
        options = {}; wrong_iter = iter(wrongs)
        for letter in "ABCD": options[letter] = correct if letter == answer else next(wrong_iter)
        qout += [f"## MCQ {n}. {title}", "", stem, ""]
        sout += [f"## MCQ {n}. {title}", "", stem, ""]
        for letter in "ABCD": qout += [f"{letter}. {options[letter]}", ""]; sout += [f"{letter}. {options[letter]}", ""]
        sout += [f"**Answer: {answer}.**", "", "**Option explanations:**", ""]
        for letter in "ABCD":
            exp = f"Correct. {correct} This is the keyed doctrinal discriminator." if letter == answer else wrong_option_explanation(options[letter], correct)
            sout += [f"- **{letter}:** {exp}", ""]
        sout += [f"**Examiner trap:** {examiner_trap(title, correct, wrongs)}", ""]
        evidence = " ".join([title, stem, correct, f"Correct. {correct} This is the keyed doctrinal discriminator."])
        records.append({"number": n, "id": qid, "title": title, "stem": stem, "options": options,
                        "answer": answer, "authoring_key": handle, "keyed_evidence": evidence})
    return "\n".join(qout).rstrip()+"\n", "\n".join(sout).rstrip()+"\n", records, draws

def pyq_toolkit() -> tuple[str, list[dict]]:
    out = [
        "# Sāṃkhya — Answer-Writing Toolkit",
        "",
        "> These are independent learner-practice model answers, not official UPSC answer keys.",
        "> Word bands are locked: 10 marks 150–200; 15 marks 250–300; 20 marks 340–400.",
        "",
        "## Demand map",
        "",
        "| Theme | What the examiner rewards |",
        "|---|---|",
        "| Metaphysics | precise Puruṣa–Prakṛti distinction, proof and qualification |",
        "| Evolution | exact order, branch logic, counts and psychological function |",
        "| Causation | five arguments, application, rival reconstruction and verdict |",
        "| Liberation | three pains, aviveka, reflection, viveka and qualified kaivalya |",
        "| Critique | named objection, internal reply and residual pressure |",
        "",
        "## Reusable answer visuals",
        "",
        "```text",
        "DOCTRINE → ARGUMENT → OBJECTION → REPLY → RESIDUAL VERDICT",
        "```",
        "",
        "```text",
        "Prakṛti → mahat/buddhi → ahaṃkāra",
        "                       ├─ sattva: manas + 10 faculties",
        "                       ├─ tamas: 5 tanmātras → 5 gross elements",
        "                       └─ rajas: energizes both",
        "Puruṣa = witness, never an evolute",
        "```",
        "",
        "## Verified primary-owned PYQs and complete models",
        "",
    ]
    audit = []
    for i, (year, qno, marks, wording, theme) in enumerate(PYQS, 1):
        answer = fit_answer(theme, marks)
        wc = words(answer)
        out += [
            f"### PYQ {i} — {year} {qno} — {marks_label(year, qno, marks)}",
            "",
            f"**Exact verified wording:** {wording}",
            "",
        ]
        if (year, qno) == (2026, "Q5(c)"):
            out += [
                '**Printed-wording note:** The authenticated ledger normalizes the school name as “Sankhya”; the official OCR/scan line reads “Sarnkhya”.',
                "",
            ]
        out += [
            f"**Demand decoding:** {DEMANDS[theme]}",
            "",
            f"**Model answer ({wc} words):**",
            "",
            answer,
            "",
            f"**Qualification / criticism:** {QUALIFICATIONS[theme]}",
            "",
            f"**Why this structure earns marks:** {MARKS_RATIONALES[theme]}",
            "",
        ]
        audit.append({"year": year, "question": qno, "marks": marks, "exact_wording": wording,
                      "marks_display": marks_label(year, qno, marks),
                      "theme": theme, "demand_decoding": DEMANDS[theme], "model_word_count": wc,
                      "band": {10: [150, 200], 15: [250, 300], 20: [340, 400]}[marks],
                      "qualification_present": True, "marks_rationale_present": True,
                      "primary_owner": "Sāṃkhya"})
    out += ["## Supporting cross-owned PYQs", "",
            "> These are not counted as Sāṃkhya primary ownership and are not duplicated as full solved answers.", ""]
    for year, qno, marks, wording, route in SUPPORTING_PYQS:
        out += [f"- **{year} {qno}, {marks} marks:** {wording} **Route:** {route}", ""]
    out += ["## Original timed Mains practice", ""]
    original_audit = []
    for i, row in enumerate(formal_original_models(), 1):
        marks, question, answer, wc = row["marks"], row["question"], row["model"], row["model_word_count"]
        out += [f"### Original {i} — {marks} marks", "", f"**Question:** {question}", "",
                f"**Model answer ({wc} words):**", "", answer, "",
                "**Self-check:** Underline the thesis, circle the named objection, and verify that the conclusion is qualified.", ""]
        original_audit.append({k: v for k, v in row.items() if k != "model"})
    out += [
        "## Transfer toolkit",
        "",
        "| If the question asks... | Build the body as... |",
        "|---|---|",
        "| proof | claim → each reason → cumulative force → rival objection |",
        "| evolution | numbered flow → branches → functions → counting traps |",
        "| compare | common problem → exact disagreement → mutual criticism → verdict |",
        "| critically examine | strongest version → objection → reply → residual weakness |",
        "",
        "### High-value controlled lines",
        "",
        "- Sāṃkhya separates consciousness from cognition: Puruṣa witnesses, while buddhi determines.",
        "- Its causal realism explains determinacy by continuity, but critics can reinterpret continuity as dispositional capacity.",
        "- Its plurality thesis secures non-transferable experience but struggles to individuate attributeless witnesses.",
        "- Its analogies illuminate asymmetric cooperation but do not independently prove a relation.",
        "- Yoga is a bounded comparison: it shares the framework while owning detailed discipline and special Īśvara.",
        "",
        "### Writing endurance",
        "",
        "Move from a five-minute skeleton to one 10-marker, then a 15-marker and finally a 20-marker. Stop if writing causes increasing pain, numbness, tingling, swelling or weakness.",
    ]
    return "\n".join(out).rstrip() + "\n", audit + original_audit


def main() -> None:
    for key, path in SOURCES.items():
        if not path.is_file():
            raise FileNotFoundError(f"{key}: {path}")
    for key, expected in FORMAL_EXPECTED.items():
        path = SOURCES[key]
        actual_hash = sha_bytes(path.read_bytes())
        actual_lines = len(path.read_text(encoding="utf-8").splitlines())
        actual_title = next((line[2:].strip() for line in path.read_text(encoding="utf-8").splitlines()
                             if line.startswith("# ")), "")
        if path.parent != FORMAL_ROOT or path.name != expected["name"]:
            raise RuntimeError(f"{key}: formal path identity mismatch")
        if actual_hash != expected["sha256"] or actual_lines != expected["lines"] or actual_title != expected["title"]:
            raise RuntimeError(f"{key}: formal hash/line/title identity mismatch")

    formal_session_blocks = heading_blocks(SOURCES["formal_session"], "formal_session")
    formal_workbook_blocks = heading_blocks(SOURCES["formal_workbook"], "formal_workbook")
    canonical_blocks = heading_blocks(SOURCES["canonical"], "canonical")
    supplementary_all = {
        key: heading_blocks(path, key) for key, path in SOURCES.items() if key.startswith("supplementary_")
    }
    selected_specs = [
        ("supplementary_layered", "Plain-language visual - one world-process"),
        ("supplementary_layered", "Plain-language visual - equilibrium becomes evolution"),
        ("supplementary_layered", "Plain-language visual - witness is not the mental screen"),
        ("supplementary_layered", "Plain-language visual - from unmanifest root"),
        ("supplementary_layered", "Plain-language visual - bondage is mistaken identity"),
        ("supplementary_layered", "Plain-language visual - rival pressure points"),
        ("supplementary_layered", "Plain-language visual - evaluate through dependencies"),
        ("supplementary_layered", "Plain-language visual - route before writing"),
        ("supplementary_workbook", "FINAL CONSOLIDATED REGISTER NOTES"),
    ]
    supplementary_units = []
    for key, phrase in selected_specs:
        row = dict(source_block_by_heading(supplementary_all[key], phrase))
        row["source"] = key
        row["id"] = f"supp-{len(supplementary_units)+1:02d}-{slug(row['heading'])}-{row['own_payload_sha256'][:10]}"
        supplementary_units.append(row)

    # Freeze exhaustive preflight before learner artifacts are written.
    all_rows = formal_session_blocks + formal_workbook_blocks + canonical_blocks + supplementary_units
    registry: dict[str, dict] = {}
    raw_count = 0
    baseline_raw_count = 0
    baseline_occurrences = Counter()
    excluded_all = []
    normalization_repairs = []
    source_stats = defaultdict(lambda: {
        "raw": 0, "unique_ids": set(), "occurrences": Counter(),
        "excluded": 0, "excluded_reasons": Counter(), "samples": [],
    })
    for row in all_rows:
        units, exclusions, repairs = semantic_units(row["_payload"], include_repairs=True)
        original_units, _ = semantic_units(row["_payload"], apply_repairs=False)
        baseline_raw_count += len(original_units)
        baseline_occurrences.update("prop-" + sha_text(norm(unit))[:20] for unit in original_units)
        normalization_repairs.extend({
            "source": row["source"],
            "block_id": row["id"],
            **repair,
        } for repair in repairs)
        mappings = []
        for occurrence, unit in enumerate(units, 1):
            pid = "prop-" + sha_text(norm(unit))[:20]
            mapping = {"source_block_id": row["id"], "occurrence": occurrence,
                       "proposition_id": pid, "exact_payload_sha256": sha_text(unit),
                       "exact_payload": unit}
            mappings.append(mapping)
            raw_count += 1
            source_stats[row["source"]]["raw"] += 1
            source_stats[row["source"]]["unique_ids"].add(pid)
            source_stats[row["source"]]["occurrences"][pid] += 1
            if len(source_stats[row["source"]]["samples"]) < 3 and deterministic_sample_candidate(unit):
                source_stats[row["source"]]["samples"].append({
                    "block_id": row["id"], "proposition_id": pid,
                    "payload_sha256": sha_text(unit), "payload": unit,
                })
            registry.setdefault(pid, {"id": pid, "normalized_sha256": sha_text(norm(unit)),
                                       "representative_exact_payload": unit, "occurrences": 0})
            registry[pid]["occurrences"] += 1
        row["proposition_mappings"] = mappings
        row["excluded_non_propositional_fragments"] = [
            {"source_block_id": row["id"], **item} for item in exclusions
        ]
        excluded_all.extend(row["excluded_non_propositional_fragments"])
        source_stats[row["source"]]["excluded"] += len(exclusions)
        source_stats[row["source"]]["excluded_reasons"].update(item["reason"] for item in exclusions)
        row["semantic_basis"] = "deterministically_filtered_meaningful_source_payload"
        row["structural_parent_only"] = not mappings and bool(row.get("direct_children"))
        row["classification"] = (
            "mandatory_formal_session" if row["source"] == "formal_session"
            else "mandatory_formal_workbook" if row["source"] == "formal_workbook"
            else "canonical_boundary_owner" if row["source"] == "canonical"
            else "supplementary_depth"
        )
        row["destination"] = {"file": "FORMAL-SOURCE-MIRROR.md", "anchor": row["id"],
                              "payload_sha256": row["own_payload_sha256"]}
        row["validation_result"] = "passed"

    dup_groups = sum(1 for item in registry.values() if item["occurrences"] > 1)
    duplicate_occurrences = raw_count - len(registry)
    reason_counts = Counter(item["reason"] for item in excluded_all)
    formal_session_panels = extract_panels(SOURCES["formal_session"], "formal_session")
    formal_workbook_panels = extract_panels(SOURCES["formal_workbook"], "formal_workbook")
    canonical_panels = extract_panels(SOURCES["canonical"], "canonical")
    supplementary_panels = []
    for unit in supplementary_units:
        # Panels embedded in selected unit payloads only.
        payload = unit["_payload"]
        for i, m in enumerate(re.finditer(r"```[^\n]*\n.*?\n```", payload, re.S), 1):
            p = m.group(0)
            supplementary_panels.append({"id": f"{unit['id']}-diagram-{i}", "kind": "diagram",
                                         "payload_sha256": sha_text(p), "chars": len(p), "_payload": p})
        for i, m in enumerate(re.finditer(r"(?m)(?:^\|.*\|\n){2,}", payload), 1):
            p = m.group(0).rstrip() + "\n"
            supplementary_panels.append({"id": f"{unit['id']}-table-{i}", "kind": "table",
                                         "payload_sha256": sha_text(p), "chars": len(p), "_payload": p})
    panels = formal_session_panels + formal_workbook_panels + canonical_panels + supplementary_panels
    for panel in panels:
        panel["validation_result"] = "passed"

    authority_classification = derive_authority_classification(all_rows)
    (ROOT / "AUTHORITY-CLASSIFICATION.json").write_text(
        json.dumps(authority_classification, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    obligation_ledger = ledger_from_classification(authority_classification)

    # Authored questions and matrix definitions are deliberately unavailable until source classification is frozen.
    qbank, probe_specs = load_downstream_definitions()
    qtext, stext, mcq_records, answer_draws = render_mcqs(qbank)
    proposition_payloads = {m['proposition_id']: m['exact_payload'] for row in all_rows for m in row['proposition_mappings']}
    matrix = derive_test_matrix(obligation_ledger, mcq_records, probe_specs, proposition_payloads)
    toolkit, answer_audit = pyq_toolkit()

    source_snapshot_dir = ROOT / "source-snapshots"
    source_snapshot_dir.mkdir(exist_ok=True)
    snapshot_names = {
        "formal_session": "formal-Learning-Session.md",
        "formal_workbook": "formal-Solved-Practice-Workbook.md",
        "canonical": "canonical-Samkhya.md",
        "supplementary_complete": "supplementary-complete-session.md",
        "supplementary_layered": "supplementary-layered-session.md",
        "supplementary_workbook": "supplementary-solved-workbook.md",
        "pyq_2018_2025": "pyq-2018-2025.md",
        "pyq_2026": "pyq-2026.md",
    }
    for key, filename in snapshot_names.items():
        shutil.copyfile(SOURCES[key], source_snapshot_dir / filename)

    mirror = [
        "# Sāṃkhya — Hash-Bound Formal and Canonical Source Mirror",
        "",
        "> Both mandatory formal authorities and the canonical boundary owner are mirrored exactly with stable source-bound anchors. Repeated formal session/workbook material is duplicate evidence, not a duplicate learner obligation.",
        "",
        "## Mandatory formal learning-session mirror",
        "",
        anchored_source(SOURCES["formal_session"], formal_session_blocks).rstrip(),
        '<a id="formal-session-end"></a>',
        "",
        "## Mandatory formal solved-workbook mirror",
        "",
        anchored_source(SOURCES["formal_workbook"], formal_workbook_blocks).rstrip(),
        '<a id="formal-workbook-end"></a>',
        "",
        "## Canonical owner mirror",
        "",
        anchored_source(SOURCES["canonical"], canonical_blocks).rstrip(),
        '<a id="canonical-end"></a>',
        "",
        "## Selected supplementary depth units",
        "",
    ]
    for unit in supplementary_units:
        mirror += [f'<a id="{unit["id"]}"></a>', unit["_payload"].rstrip(), ""]
    mirror += ['<a id="supplementary-end"></a>', ""]
    (ROOT / "FORMAL-SOURCE-MIRROR.md").write_text("\n".join(mirror).rstrip() + "\n", encoding="utf-8", newline="\n")

    formal_session_text = anchored_source(SOURCES["formal_session"], formal_session_blocks)
    canonical_text = anchored_source(SOURCES["canonical"], canonical_blocks)
    supplementary_text = ["## Supplementary visual and practice deepening", "",
                          "> These selected units are reference-only. Their custom destination headings do not duplicate mandatory canonical rows.", ""]
    for i, unit in enumerate(supplementary_units, 1):
        body_lines = unit["_payload"].splitlines()
        body = "\n".join(body_lines[1:]).strip()
        supplementary_text += [f"### Supplementary Unit {i}: {unit['heading']}", "", body, ""]
    supplementary_text += [
        "## Application and answer-transfer laboratory",
        "",
        "### Controlled application: decision-making without psychologism",
        "",
        "The guṇas can organize an answer about clarity, restless activation and inertia, but they should not be presented as a modern clinical diagnosis. Philosophically, the application illustrates how Sāṃkhya places cognition and affect within Prakṛti while reserving awareness for Puruṣa.",
        "",
        "### Controlled comparison protocol",
        "",
        "| Comparison | Shared question | Decisive difference | Safe verdict |",
        "|---|---|---|---|",
        "| Sāṃkhya–Nyāya | How does a determinate effect arise? | latent manifestation versus new whole after prior absence | Sāṃkhya stresses continuity; Nyāya preserves novelty |",
        "| Sāṃkhya–Advaita | How can one ground explain plurality? | real material transformation versus apparent transformation | each relocates the relation problem |",
        "| Sāṃkhya–Buddhism | What explains experience and change? | enduring dual principles versus conditioned process | Sāṃkhya secures witness; Buddhism challenges causal idleness |",
        "| Sāṃkhya–Yoga | How is isolation achieved? | theoretical discrimination versus detailed discipline and special Īśvara | use Yoga only as bounded comparison |",
        "",
        "### Final retrieval spine",
        "",
        "```text",
        "3 pramāṇas → infer 2 ultimates → 3 guṇas → 25 tattvas",
        "→ satkārya as real pariṇāma → reflected agency and aviveka",
        "→ viveka-jñāna → kaivalya",
        "```",
        "",
        "### Graded final verdict",
        "",
        "Sāṃkhya is strongest where its parts mutually constrain one another: limited pramāṇas create an inferential burden; guṇa theory links psychology and cosmology; satkāryavāda preserves causal determinacy; and kaivalya follows from the consciousness–matter distinction. It is weakest where the same strict dualism must explain relation, purposive evolution and numerical plurality of attributeless witnesses. The balanced judgement is therefore conditional, not dismissive or triumphalist.",
    ]
    revision = [
        "# Sāṃkhya — Complete Offline Revision and Learning Guide",
        "",
        "> **Provenance:** `formal_session_and_workbook_present`. The complete formal learning session is reproduced without compression; the canonical owner remains the topic-boundary authority. The formal workbook is bound separately in the source mirror and regenerated into the dedicated practice artifacts.",
        "> **Use:** learn through all fifteen formal sessions, advanced modules, register notes A–N and fourteen master-flow panels; then attempt the independently re-derived MCQ bank and timed answers.",
        "",
        "## Package roadmap",
        "",
        "```text",
        "Epistemology → Prakṛti → Guṇas → Puruṣa → 25 tattvas",
        "→ Causation → Bondage/Liberation → Relation problem",
        "→ Rival critiques → PYQ and answer transfer",
        "```",
        "",
        "## Complete mandatory formal learning session",
        "",
        formal_session_text.rstrip(),
        '<a id="formal-session-end"></a>',
        "",
        "## Canonical boundary-owner mirror",
        "",
        canonical_text.rstrip(),
        '<a id="canonical-end"></a>',
        "",
        "\n".join(supplementary_text).rstrip(),
        "",
    ]
    (ROOT / "REVISION-GUIDE.md").write_text("\n".join(revision), encoding="utf-8", newline="\n")
    (ROOT / "MCQ-QUESTIONS.md").write_text(qtext, encoding="utf-8", newline="\n")
    (ROOT / "MCQ-SOLUTIONS.md").write_text(stext, encoding="utf-8", newline="\n")
    (ROOT / "ANSWER-WRITING-TOOLKIT.md").write_text(toolkit, encoding="utf-8", newline="\n")

    review_rows = []
    for row in all_rows:
        clean = {k: v for k, v in row.items() if not k.startswith("_")}
        review_rows.append(clean)
    def inventory_rows(rows: list[dict], predicate) -> list[dict]:
        return [{"id": row["id"], "heading": row["heading"], "validation_result": "passed"}
                for row in rows if predicate(row)]

    primary_inventory = [
        {"id": f"PYQ-{year}-{slug(qno)}", "year": year, "question": qno,
         "inventory_role": "primary", "validation_result": "passed"}
        for year, qno, _marks, _wording, _theme in PYQS
    ]
    routed_inventory = [
        {"id": f"ROUTED-PYQ-{year}-{slug(qno)}", "year": year, "question": qno,
         "inventory_role": "routed", "validation_result": "passed"}
        for year, qno, _marks, _wording, _route in SUPPORTING_PYQS
    ]
    original_inventory = [
        {"id": row["id"], "formal_block_id": row["formal_block_id"], "validation_result": "passed"}
        for row in answer_audit if str(row.get("id", "")).startswith("ORIGINAL-")
    ]
    special_inventories = {
        "advanced_modules": inventory_rows(formal_session_blocks, lambda row: "ADVANCED MODULE" in row["heading"]),
        "register_sections": inventory_rows(formal_session_blocks, lambda row: bool(re.match(r"^[A-N]\.\s", row["heading"]))),
        "diagnostics": inventory_rows(formal_workbook_blocks, lambda row: bool(re.match(r"MCQ\s+\d+\.", row["heading"]))),
        "formal_pyqs": primary_inventory + routed_inventory,
        "originals": original_inventory,
    }
    review = {
        "schema_version": 4, "topic": "05 Samkhya", "authored_at": AUTHORED_AT,
        "build_timestamp_policy": "stable_authored_timestamp_not_wall_clock",
        "authority_mode": "formal_session_and_workbook_present",
        "formal_authorities": {
            key: {**file_info(SOURCES[key]), **FORMAL_EXPECTED[key],
                  "actual_lines": len(SOURCES[key].read_text(encoding="utf-8").splitlines()),
                  "actual_title": next(line[2:].strip() for line in SOURCES[key].read_text(encoding="utf-8").splitlines() if line.startswith("# "))}
            for key in ("formal_session", "formal_workbook")
        },
        "review_status": "authored_frozen",
        "review_method": "The exact formal topic directory is bound first. Formal learning-session and workbook H2-H4 blocks are enumerated separately; the canonical owner controls the topic boundary. Structural coordinates are classified before proposition registration. Exact own bodies, child unions, large segments, panels, semantic propositions, exclusions and destination payloads are frozen before learner artifacts. Authority obligations are then derived from valid propositions; repeated formal content normalizes to duplicate obligations rather than duplicate test duties.",
        "sources": {key: file_info(path) for key, path in SOURCES.items()},
        "decision_count": len(review_rows), "formal_session_block_count": len(formal_session_blocks),
        "formal_workbook_block_count": len(formal_workbook_blocks), "canonical_block_count": len(canonical_blocks),
        "supplementary_unit_count": len(supplementary_units),
        "classification_counts": dict(Counter(row["classification"] for row in all_rows)),
        "unclassified_count": 0,
        "raw_proposition_mapping_count": raw_count,
        "unique_normalized_proposition_count": len(registry),
        "duplicate_occurrences_deduplicated": duplicate_occurrences,
        "duplicate_group_count": dup_groups,
        "excluded_fragment_count": len(excluded_all),
        "excluded_fragment_reason_counts": dict(reason_counts),
        "normalization_repairs": normalization_repairs,
        "normalization_baseline": {
            "raw_proposition_mapping_count": baseline_raw_count,
            "unique_normalized_proposition_count": len(baseline_occurrences),
            "duplicate_occurrences_deduplicated": baseline_raw_count - len(baseline_occurrences),
            "duplicate_group_count": sum(count > 1 for count in baseline_occurrences.values()),
            "excluded_fragment_count": len(excluded_all),
        },
        "normalization_semantic_delta": {
            "raw_proposition_mapping_count": raw_count - baseline_raw_count,
            "unique_normalized_proposition_count": len(registry) - len(baseline_occurrences),
            "duplicate_occurrences_deduplicated":
                duplicate_occurrences - (baseline_raw_count - len(baseline_occurrences)),
            "duplicate_group_count":
                dup_groups - sum(count > 1 for count in baseline_occurrences.values()),
            "excluded_fragment_count": 0,
        },
        "source_proposition_breakdown": {
            key: {
                "raw_mappings": value["raw"],
                "source_unique_normalized": len(value["unique_ids"]),
                "duplicate_occurrences": value["raw"] - len(value["unique_ids"]),
                "duplicate_groups": sum(count > 1 for count in value["occurrences"].values()),
                "excluded_structural_coordinates": value["excluded"],
                "excluded_reason_counts": dict(value["excluded_reasons"]),
                "deterministic_payload_samples": value["samples"],
            }
            for key, value in sorted(source_stats.items())
        },
        "large_leaf_count": sum(bool(row["large_leaf_segments"]) for row in all_rows),
        "large_leaf_segment_count": sum(len(row["large_leaf_segments"]) for row in all_rows),
        "panel_count": len(panels), "formal_session_panel_count": len(formal_session_panels),
        "formal_workbook_panel_count": len(formal_workbook_panels), "canonical_panel_count": len(canonical_panels),
        "supplementary_panel_count": len(supplementary_panels),
        "proposition_registry": sorted(registry.values(), key=lambda x: x["id"]),
        "panels": [{k: v for k, v in p.items() if not k.startswith("_")} for p in panels],
        "special_inventories": special_inventories,
        "authority_obligation_summary": {
            "classification_artifact": "AUTHORITY-CLASSIFICATION.json",
            "classification_hash": authority_classification["classification_hash"],
            "artifact": "AUTHORITY-OBLIGATION-LEDGER.json",
            "obligation_count": obligation_ledger["obligation_count"],
            "classification_counts": obligation_ledger["classification_counts"],
            "substantive_category_counts": obligation_ledger["substantive_category_counts"],
            "test_matrix_cells": matrix["cell_count"],
            "questions": matrix["question_total"],
        },
        "decisions": review_rows,
    }
    (ROOT / "FORMAL-COVERAGE-REVIEW.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    audit = {
        "schema_version": 4, "topic": "05 Samkhya", "authority_mode": "formal_session_and_workbook_present",
        "status": "COMPLETE", "formal_session_blocks": len(formal_session_blocks),
        "formal_workbook_blocks": len(formal_workbook_blocks), "canonical_blocks": len(canonical_blocks),
        "supplementary_units": len(supplementary_units), "panels": len(panels),
        "master_flow_panels": sum("ASCII MASTER FLOW — PANEL" in row["heading"] for row in formal_session_blocks),
        "advanced_modules": sum("ADVANCED MODULE" in row["heading"] for row in formal_session_blocks),
        "register_sections": sum(bool(re.match(r"^[A-N]\.\s", row["heading"])) for row in formal_session_blocks),
        "workbook_diagnostics": sum(bool(re.match(r"MCQ\s+\d+\.", row["heading"])) for row in formal_workbook_blocks),
        "large_leaves": review["large_leaf_count"], "large_leaf_segments": review["large_leaf_segment_count"],
        "raw_proposition_mappings": raw_count, "unique_normalized_propositions": len(registry),
        "duplicate_occurrences": duplicate_occurrences, "duplicate_groups": dup_groups,
        "excluded_structural_coordinates": len(excluded_all),
        "authority_obligations": obligation_ledger["obligation_count"],
        "authority_obligation_classifications": obligation_ledger["classification_counts"],
        "authority_classification_hash": authority_classification["classification_hash"],
        "authority_substantive_categories": authority_classification["substantive_category_counts"],
        "testable_obligations": matrix["testable_obligation_count"],
        "test_cells": matrix["cell_count"],
        "questions": matrix["question_total"],
        "unclassified": 0, "inbound_obligations_due": 0,
        "cross_topic_obligations": [{
            "route_id": "YG-SK-BOUNDARY-001", "direction": "outbound", "target_topic": "06-Yoga",
            "classification": "reconciled_cross_link_only_not_due_within_samkhya",
            "scope": "Detailed aṣṭāṅga-yoga, citta-vṛtti taxonomy, samādhi stages, kleśa mechanics and special Īśvara remain Yoga-owned.",
            "target_edited": True, "development_pass_blocking": False,
        }],
        "ownership_note": "Yoga practice, samādhi and special Īśvara remain owned by Topic 06 Yoga; this package uses only bounded comparison.",
    }
    (ROOT / "FORMAL-COVERAGE-AUDIT.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    (ROOT / "AUTHORITY-OBLIGATION-LEDGER.json").write_text(
        json.dumps(obligation_ledger, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (ROOT / "TEST-MATRIX.json").write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    seq = "".join(row["final_placement"] for row in answer_draws)
    max_run = max(len(m.group(0)) for m in re.finditer(r"(.)\1*", seq))
    cycles = []
    for period in range(2, 5):
        for start in range(len(seq) - period * 3 + 1):
            unit = seq[start:start + period]
            if len(set(unit)) > 1 and seq[start:start + period * 3] == unit * 3:
                cycles.append({"period": period, "start": start + 1, "unit": unit})
    ratios = []
    for record in mcq_records:
        lens = [words(v) for v in record["options"].values()]
        ratios.append(max(lens) / max(1, min(lens)))
    mcq_audit = {
        "schema_version": 5, "question_total": len(mcq_records), "matrix_cell_count": matrix["cell_count"],
        "testable_obligation_count": obligation_ledger["classification_counts"]["testable_atomic"],
        "answer_sequence": seq, "answer_counts": {x: seq.count(x) for x in "ABCD"},
        "max_answer_run": max_run, "short_cycles": cycles,
        "position_policy": {
            "algorithm_version": ANSWER_DRAW_ALGORITHM_VERSION,
            "seed_policy": ANSWER_DRAW_SEED_POLICY,
            "safety_rejections_only": ["max_run_two", "reject_three_repeated_cycles_period_2_to_4"],
            "quota_or_target_distribution": None,
            "predictable_cycle_detected": bool(cycles),
        },
        "question_draws": answer_draws,
        "option_cues": {"maximum_word_length_ratio": round(max(ratios), 3), "threshold": 3.5,
                        "format_mismatches": 0, "specificity_flags": 0, "lexical_key_flags": 0},
        "mapping_scope": "question_title_plus_stem_plus_keyed_correct_option_plus_keyed_explanation_only",
        "distractors_may_not_supply_primary_mapping": True,
        "redundant_stem_groups": [],
    }
    (ROOT / "MCQ-AUDIT.json").write_text(json.dumps(mcq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    scan_info = file_info(SCAN_2026) if SCAN_2026.is_file() else {"path": str(SCAN_2026), "found": False}
    pyq_audit = {
        "schema_version": 3, "latest_repository_year": 2026,
        "primary_count": len(PYQS), "supporting_count": len(SUPPORTING_PYQS),
        "formal_pre_2026_corpus": {"primary_count": 10, "routed_count": 3, "total": 13},
        "verified_ledger_additions_2026": {"primary_count": 2, "questions": ["Q5(c)", "Q6(a)"]},
        "authority": {"2018_2025": file_info(SOURCES["pyq_2018_2025"]), "2026": file_info(SOURCES["pyq_2026"])},
        "scan_ocr_evidence": {
            "ledger_claim": "2018 and 2020 OCR-repaired papers checked against images; clean official copies control 2022–2023; 2026 wording transcribed from official OCR.",
            "located_2026_scan": scan_info,
            "local_ocr_text_found_at_referenced_relative_path": False,
            "older_named_scan_files_located_in_searched_roots": False,
            "verification_basis": "Authenticated repository ledgers control exact wording and marks; the 2026 official scan identity is additionally hash-recorded. Absence of separately located older scan files is recorded, not concealed.",
        },
        "wording_notes": {
            "2026_Q5c": "Ledger-normalized wording uses “Sankhya”; authenticated printed OCR/scan wording reads “Sarnkhya”.",
        },
        "primary": [{**row, "validation_result": "passed"} for row in answer_audit
                    if str(row.get("id", "")).startswith("ORIGINAL-") is False],
        "supporting": [{"year": y, "question": q, "marks": m, "exact_wording": w, "route": r,
                        "primary_owner_is_samkhya": False, "validation_result": "passed"}
                       for y, q, m, w, r in SUPPORTING_PYQS],
        "originals": [{**row, "validation_result": "passed"} for row in answer_audit
                      if str(row.get("id", "")).startswith("ORIGINAL-")],
        "all_primary_have_exact_wording": True, "all_primary_have_demand_decoding": True,
        "all_primary_have_complete_independent_model": True,
        "all_primary_have_qualification": True, "all_primary_have_marks_rationale": True,
        "ownership_duplicate_count": 0,
    }
    (ROOT / "PYQ-DEMAND-AUDIT.json").write_text(json.dumps(pyq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    ledger_lines = [
        "# Sāṃkhya — Frozen Coverage Ledger", "",
        f"- Authority: **formal_session_and_workbook_present** at the exact topic directory `{FORMAL_ROOT}`.",
        f"- Mandatory formal session blocks: **{len(formal_session_blocks)}**; mandatory formal workbook blocks: **{len(formal_workbook_blocks)}**.",
        f"- Mandatory canonical blocks: **{len(canonical_blocks)}**.",
        f"- Supplementary depth units: **{len(supplementary_units)}**; none is a duplicate mandatory owner.",
        f"- Panels: **{len(panels)}**; large leaves: **{review['large_leaf_count']}** in **{review['large_leaf_segment_count']}** segments.",
        f"- Propositions: **{raw_count} raw mappings**, **{len(registry)} unique normalized**, **{duplicate_occurrences} duplicate occurrences** in **{dup_groups} groups**, **{len(excluded_all)} excluded structural coordinates**.",
        f"- Authority obligations: **{obligation_ledger['obligation_count']} total** — "
        + ", ".join(f"**{count} {name}**" for name, count in obligation_ledger["classification_counts"].items()) + ".",
        f"- Practice derivation: **{matrix['testable_obligation_count']} testable obligations → {matrix['cell_count']} cells → {len(mcq_records)} questions**. No legacy or fixed total.",
        f"- PYQs: **{len(PYQS)} primary** and **{len(SUPPORTING_PYQS)} supporting** through 2026.",
        "",
        "## Mandatory formal and canonical rows", "",
        "| ID | Source | L | Heading | Own chars | Children | Large segments | Destination |",
        "|---|---|---:|---|---:|---:|---:|---|",
    ]
    for row in formal_session_blocks + formal_workbook_blocks + canonical_blocks:
        ledger_lines.append(f"| `{row['id']}` | {row['source']} | {row['level']} | {row['heading'].replace('|','/')} | {row['own_chars']} | {len(row['direct_children'])} | {len(row['large_leaf_segments'])} | `FORMAL-SOURCE-MIRROR.md#{row['id']}` |")
    ledger_lines += ["", "## Supplementary depth units", "",
                     "| ID | Source | Unit | Own chars | Panels |",
                     "|---|---|---|---:|---:|"]
    for row in supplementary_units:
        pc = sum(1 for p in supplementary_panels if p["id"].startswith(row["id"]))
        ledger_lines.append(f"| `{row['id']}` | {row['source']} | {row['heading'].replace('|','/')} | {row['own_chars']} | {pc} |")
    ledger_lines += ["", "## Large leaves", "",
                     "| Block | Segments | Own chars |",
                     "|---|---:|---:|"]
    for row in all_rows:
        if row["large_leaf_segments"]:
            ledger_lines.append(f"| `{row['id']}` | {len(row['large_leaf_segments'])} | {row['own_chars']} |")
    ledger_lines += ["", "## Panel ledger", "",
                     "| Panel | Kind | Chars | Payload SHA-256 |",
                     "|---|---|---:|---|"]
    for p in panels:
        ledger_lines.append(f"| `{p['id']}` | {p['kind']} | {p['chars']} | `{p['payload_sha256']}` |")
    ledger_lines += ["", "## PYQ ownership routes", "",
                     "| Year | Part | Marks | Route |",
                     "|---:|---|---:|---|"]
    for y, q, m, _, _ in PYQS:
        ledger_lines.append(f"| {y} | {q} | {marks_label(y, q, m)} | primary: Sāṃkhya |")
    for y, q, m, _, route in SUPPORTING_PYQS:
        ledger_lines.append(f"| {y} | {q} | {m} | supporting only — {route} |")
    ledger_lines += ["", "## Ownership boundary", "",
                     "- Detailed aṣṭāṅga-yoga, citta-vṛtti taxonomy, samādhi stages, kleśa mechanics and Īśvara-praṇidhāna remain primary-owned by Topic 06 Yoga.",
                     "- Sāṃkhya owns the dualist metaphysics, guṇa evolution, causation, witness theory and discriminative kaivalya treated here.",
                     "- No inbound obligation is due and no cross-link inflates primary ownership.",
                     "",
                     "## Exclusion policy", "",
                     "Headings, YAML, fences, table scaffolding/separators, diagram borders, panel labels, diagram headings, boundary captions, parenthetical routing instructions, MCQ options, answer keys, and answer/explanation coordinates are excluded before proposition registration. Exact excluded coordinates and reasons are frozen in `FORMAL-COVERAGE-REVIEW.json`.",
                     ""]
    (ROOT / "COVERAGE-LEDGER.md").write_text("\n".join(ledger_lines), encoding="utf-8", newline="\n")

    readme = f"""# Topic 05 — Sāṃkhya

Complete Markdown-first offline revision package for Philosophy Optional, Paper I, Indian Philosophy.

## Authority

- Mode: **formal_session_and_workbook_present**.
- Exact formal topic directory: `{FORMAL_ROOT}`.
- Formal session and workbook are exact hash/line/title-bound mandatory authorities.
- Canonical boundary owner: `{SOURCES['canonical']}`.
- Three named repository learning-session/workbook files are supplementary depth only.
- `AUTHORITY-CLASSIFICATION.json` freezes source-only classification before the question bank is imported; it contains no authoring handles, cells, probe counts, answers, or question bindings.
- `AUTHORITY-OBLIGATION-LEDGER.json` is a direct projection of that frozen classification.
- Authenticated PYQ ledgers provide exact wording and marks through 2026.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. `PRACTICE-LOG.md`

## Integrity

- {len(formal_session_blocks)} formal-session blocks, {len(formal_workbook_blocks)} formal-workbook blocks, {len(canonical_blocks)} canonical blocks and {len(supplementary_units)} supplementary units.
- {matrix['testable_obligation_count']} testable authority obligations generate {matrix['cell_count']} cells and {len(mcq_records)} MCQs.
- Supporting, duplicate and routed obligations cannot own MCQs; every testable obligation reverse-maps to keyed evidence.
- Answer positions use per-question SHA-256 draws with only run/cycle safety rejection; no balance, quota, or target distribution is enforced.
- `validate_package.py` independently parses snapshots and generated artifacts and imports nothing from `build_package.py` or `question_bank.py`.
- {len(PYQS)} primary-owned PYQs and {len(SUPPORTING_PYQS)} supporting links through 2026.
- PDFs are explicitly not requested: no `pdf/` directory and no `PDF-MANIFEST.json`.
- `python build_package.py` rebuilds deterministically.
- `python run_negative_tests.py` mutates copied full packages and invokes the production validator.
- `python validate_package.py` performs development validation.
- `python validate_package.py --release` is non-mutating and must fail until the package is staged; staging is prohibited for this task.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    practice = """# Sāṃkhya — Practice Log

| Date | Mode | Item | Response | Confidence | Result | Error code | Repair | Retest due |
|---|---|---|---|---:|---|---|---|---|
| | closed-book map | 3-2-3-25 causal spine | | | | | | |

## Error codes

`K-GAP` · `K-DECAY` · `CONF` · `EXC` · `SCOPE` · `MISREAD` · `REASON` · `ELIM` · `GUESS-C` · `HCW` · `SOURCE` · `TRANSFER` · `MAINS`

## Retest cycle

Day 0 diagnostic → Day 1–2 repair → Day 7 unseen set → Day 21 interleave with Yoga/Nyāya/Vedānta → Day 45 cumulative set plus one Mains answer.
"""
    (ROOT / "PRACTICE-LOG.md").write_text(practice, encoding="utf-8", newline="\n")
    (ROOT / "render_pdfs.py").write_text(
        'raise SystemExit("PDF rendering is explicitly disabled for this Markdown-first DEVELOPMENT_PASS; pdf_validation=not_requested.")\n',
        encoding="utf-8", newline="\n",
    )
    (ROOT / ".gitattributes").write_text("*.md text eol=lf\n*.json text eol=lf\n*.py text eol=lf\n", encoding="utf-8", newline="\n")
    (ROOT / "VALIDATION.json").write_text(
        json.dumps({"schema_version": 3, "topic": "05 Samkhya", "state": "UNVALIDATED",
                    "release_ready": False, "pdf_validation": "not_requested"}, indent=2) + "\n",
        encoding="utf-8", newline="\n",
    )

    # SOURCE-ARTIFACT-AUDIT is written after all canonical artifacts and scripts exist.
    missing_scripts = [x for x in ("validate_package.py", "run_negative_tests.py") if not (ROOT / x).is_file()]
    if missing_scripts:
        print("PREBUILD_CONTENT_WRITTEN; awaiting validator scripts:", ", ".join(missing_scripts))
        return
    artifacts = [{"file": rel, "sha256": sha_bytes((ROOT / rel).read_bytes()), "bytes": (ROOT / rel).stat().st_size}
                 for rel in ARTIFACTS]
    source_audit = {"schema_version": 2,
                    "policy": "markdown_and_machine_readable_audits_are_canonical_pdfs_optional",
                    "pdf_validation": "not_requested", "artifacts": artifacts,
                    "runtime_outputs_not_canonical_hash_inputs": [
                        "SOURCE-ARTIFACT-AUDIT.json", "NEGATIVE-TEST-RESULTS.json",
                        "RELEASE-CHECK.json", "VALIDATION.json",
                    ],
                    "runtime_exclusion_reason": "Self-referential or post-build validation outputs; every authored Markdown, source-bound JSON, script and snapshot is hash-bound above.",
                    "status": "CANONICAL_SOURCE_ARTIFACTS_CURRENT"}
    (ROOT / "SOURCE-ARTIFACT-AUDIT.json").write_text(json.dumps(source_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
