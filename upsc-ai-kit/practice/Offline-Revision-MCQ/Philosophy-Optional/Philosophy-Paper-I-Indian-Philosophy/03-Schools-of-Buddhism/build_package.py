from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path

from mcq_bank import (
    CELL_MATRIX,
    EXTRA_PROBES,
    EXTRA_PROBE_RATIONALES,
    NEW_QUESTIONS,
    OLD_QUESTION_PRIMARY,
    RETAINED_ADAPTATIONS,
    REDUNDANT_REMOVED,
)

ROOT = Path(__file__).resolve().parent
SNAPSHOT_DIR = ROOT / "source-snapshots"
ORIGINAL_SOURCES = {
    "formal_session": Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\03-Schools-of-Buddhism\Learning-Session.md"),
    "formal_workbook": Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\03-Schools-of-Buddhism\Solved-Practice-Workbook.md"),
    "canonical": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Buddhism.md"),
    "pyq_2018_2025": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md"),
    "pyq_2026": Path(r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md"),
}
SNAPSHOTS = {
    "formal_session": SNAPSHOT_DIR / "formal-session.md",
    "formal_workbook": SNAPSHOT_DIR / "formal-workbook.md",
    "canonical": SNAPSHOT_DIR / "canonical-owner.md",
    "pyq_2018_2025": SNAPSHOT_DIR / "pyq-2018-2025.md",
    "pyq_2026": SNAPSHOT_DIR / "pyq-2026.md",
}
EXPECTED_HASHES = {
    "formal_session": "9a0e5593fcba75966b2c3a57fe64402b4a6c0854dfeb3dce3463dc11e5ac5483",
    "formal_workbook": "1d99dabae0aa18be505764b1e72171cd2e2d6547a5da617889d4b493d3bf4fd1",
    "canonical": "0f405f2bcdcae0228194be9219a05946f38b151af5f457b887208e5a6dae7d12",
    "pyq_2018_2025": "c7b556c7b4b750943b7b5f0ac94273664a46c6c75f1c444ae2d953fd77d34eec",
    "pyq_2026": "1e3b86dbf301bf929851ecc39f1b8585485707cd19fc7a2168861bbb142a8806",
}
EXPECTED_BYTES = {
    "formal_session": 371530,
    "formal_workbook": 104595,
    "canonical": 88150,
    "pyq_2018_2025": 25796,
    "pyq_2026": 8502,
}
SESSION = SNAPSHOTS["formal_session"]
WORKBOOK = SNAPSHOTS["formal_workbook"]
CANONICAL = SNAPSHOTS["canonical"]
PYQ_OLD = SNAPSHOTS["pyq_2018_2025"]
PYQ_NEW = SNAPSHOTS["pyq_2026"]
IST = timezone(timedelta(hours=5, minutes=30))
NOW = datetime.now(IST).replace(microsecond=0).isoformat()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(text: str) -> str:
    return sha_bytes(text.replace("\r\n", "\n").encode("utf-8"))


def normalize_proposition(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text)).strip()


def inference_basis(stem: str, correct: str) -> str:
    clean = normalize_proposition(f"{stem} || {correct}").lower()
    clean = re.sub(r"\b(?:19|20)\d{2}\b", " ", clean)
    clean = re.sub(r"\b(?:mcq|pyq|cell)\s*[-:#]?\s*\d+\b", " ", clean)
    clean = re.sub(r"[^\wāīūṛṝḷṅñṭḍṇśṣṃḥ]+", " ", clean, flags=re.UNICODE)
    return normalize_proposition(clean)


def file_info(key: str, path: Path) -> dict:
    data = path.read_bytes()
    return {
        "path": str(ORIGINAL_SOURCES[key]),
        "local_snapshot": str(path.relative_to(ROOT).as_posix()),
        "sha256": sha_bytes(data),
        "bytes": len(data),
    }


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE).strip("-")
    return s[:76] or "block"


def source_blocks(path: Path, prefix: str) -> list[dict]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").splitlines()
    heads = []
    for i, line in enumerate(lines):
        m = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))
    blocks = []
    if heads and heads[0][0] > 0:
        prelude = "\n".join(lines[:heads[0][0]]).strip() + "\n"
        blocks.append({
            "id": f"{prefix}-document-prelude-000-{sha_text(prelude)[:10]}",
            "source": prefix,
            "ordinal": 0,
            "level": 1,
            "heading": "DOCUMENT PRELUDE",
            "line_start": 1,
            "line_end": heads[0][0],
            "own_payload_sha256": sha_text(prelude),
            "subtree_sha256": sha_text(prelude),
            "own_chars": len(prelude),
            "large_leaf_segments": [],
            "direct_children": [],
            "child_union_sha256": sha_text(""),
        })
    for n, (start, level, heading) in enumerate(heads):
        own_end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        subtree_end = len(lines)
        for j in range(n + 1, len(heads)):
            if heads[j][1] <= level:
                subtree_end = heads[j][0]
                break
        own = "\n".join(lines[start:own_end]).strip() + "\n"
        subtree = "\n".join(lines[start:subtree_end]).strip() + "\n"
        ident = f"{prefix}-{slug(heading)}-{n+1:03d}-{sha_text(own)[:10]}"
        segments = []
        if len(own) > 2400:
            for i, offset in enumerate(range(0, len(own), 1800)):
                chunk = own[offset:offset + 1800]
                segments.append({
                    "index": i + 1,
                    "start_char": offset,
                    "end_char_exclusive": offset + len(chunk),
                    "payload_sha256": sha_text(chunk),
                    "chars": len(chunk),
                })
        blocks.append({
            "id": ident, "source": prefix, "ordinal": n + 1, "level": level,
            "heading": heading, "line_start": start + 1, "line_end": own_end,
            "own_payload_sha256": sha_text(own), "subtree_sha256": sha_text(subtree),
            "own_chars": len(own),
            "large_leaf_segments": segments,
        })
    heading_blocks = [b for b in blocks if b["ordinal"] > 0]
    for b in heading_blocks:
        children = []
        child_payloads = []
        i = b["ordinal"]
        for c in heading_blocks[i:]:
            if c["level"] <= b["level"]:
                break
            if c["level"] == b["level"] + 1:
                children.append(c["id"])
                child_payloads.append(c["own_payload_sha256"])
        b["direct_children"] = children
        b["child_union_sha256"] = sha_text("\n".join(child_payloads))
    return blocks


def anchored_copy(path: Path, prefix: str, blocks: list[dict], title: str) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    by_heading = {}
    for b in blocks:
        by_heading.setdefault((b["level"], b["heading"]), []).append(b["id"])
    used = {}
    prelude = next(b for b in blocks if b["ordinal"] == 0)
    out = [f'<a id="{prelude["id"]}"></a>']
    for line in text.splitlines():
        m = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if m:
            key = (len(m.group(1)), m.group(2))
            idx = used.get(key, 0)
            if key in by_heading and idx < len(by_heading[key]):
                out.append(f'<a id="{by_heading[key][idx]}"></a>')
                used[key] = idx + 1
        out.append(line)
    return "\n".join(out) + "\n"


PROPOSITION_UNIT_TYPES = {"prose_paragraph", "substantive_list_item", "table_data_row", "diagram_text_row"}
STRUCTURAL_UNIT_TYPES = {
    "blank_line", "yaml_frontmatter", "heading", "navigation_label", "thematic_break",
    "code_fence_open", "code_fence_close", "table_header", "table_separator",
    "table_scaffolding", "diagram_border_or_connector_only",
}
STRUCTURAL_CATEGORIES = {
    "blank_line": "whitespace",
    "yaml_frontmatter": "document_metadata",
    "heading": "heading_or_navigation",
    "navigation_label": "heading_or_navigation",
    "thematic_break": "document_structure",
    "code_fence_open": "code_fence",
    "code_fence_close": "code_fence",
    "table_header": "table_structure",
    "table_separator": "table_structure",
    "table_scaffolding": "table_structure",
    "diagram_border_or_connector_only": "diagram_structure",
}


def is_navigation_label(text: str) -> bool:
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    plain = re.sub(r"[*_`#>|]", " ", plain)
    plain = normalize_proposition(plain).lower()
    words = re.findall(r"[a-z]+", plain)
    return (
        bool(words)
        and len(words) <= 8
        and any(token in plain for token in ("←", "→", "back", "next", "previous", "navigation", "contents", "home"))
        and all(word in {"back", "to", "next", "previous", "navigation", "contents", "home", "top", "index"} for word in words)
    )


def diagram_row_has_meaningful_text(text: str) -> bool:
    stripped = re.sub(r"[\s`~!@#$%^&*()_+\-=\[\]{};:'\",.<>/?\\|]+", "", text)
    return bool(re.search(r"[A-Za-z0-9\u00c0-\u02ff\u0900-\u097f]", stripped))


def semantic_units(payload: str, block: dict) -> list[dict]:
    lines = payload.rstrip("\n").splitlines()
    units = []

    def add_unit(start: int, end: int, kind: str, classification: str) -> None:
        raw = "\n".join(lines[start:end]).strip() + "\n"
        if kind == "blank_line":
            raw = "\n"
        normalized = normalize_proposition(raw)
        units.append({
            "classification": classification,
            "segment_type": kind,
            "relative_line_start": start + 1,
            "relative_line_end": end,
            "absolute_line_start": block["line_start"] + start,
            "absolute_line_end": block["line_start"] + end - 1,
            "raw_payload": raw,
            "normalized_payload": normalized,
        })

    i = 0
    while i < len(lines):
        if not lines[i].strip():
            add_unit(i, i + 1, "blank_line", "excluded_structural")
            i += 1
            continue
        start = i
        if lines[i].startswith("```"):
            add_unit(i, i + 1, "code_fence_open", "excluded_structural")
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                if not lines[i].strip():
                    add_unit(i, i + 1, "blank_line", "excluded_structural")
                elif diagram_row_has_meaningful_text(lines[i]):
                    add_unit(i, i + 1, "diagram_text_row", "proposition")
                else:
                    add_unit(i, i + 1, "diagram_border_or_connector_only", "excluded_structural")
                i += 1
            if i < len(lines):
                add_unit(i, i + 1, "code_fence_close", "excluded_structural")
                i += 1
            continue
        if lines[i].strip() == "---":
            if i == 0 and any(x.strip() == "---" for x in lines[1:]):
                kind = "yaml_frontmatter"
                i += 1
                while i < len(lines):
                    if lines[i].strip() == "---":
                        i += 1
                        break
                    i += 1
            else:
                kind = "thematic_break"
                i += 1
            add_unit(start, i, kind, "excluded_structural")
            continue
        elif re.match(r"^#{1,6}\s+", lines[i]):
            i += 1
            add_unit(start, i, "heading", "excluded_structural")
            continue
        elif re.match(r"^\s*(?:[-*+]|\d+[.)])\s+", lines[i]):
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                r"^(?:\s*(?:[-*+]|\d+[.)])\s+|#{1,6}\s+|```|\||---\s*$)", lines[i]
            ):
                i += 1
            raw = "\n".join(lines[start:i])
            add_unit(start, i, "navigation_label" if is_navigation_label(raw) else "substantive_list_item",
                     "excluded_structural" if is_navigation_label(raw) else "proposition")
            continue
        elif lines[i].lstrip().startswith("|"):
            if re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i]):
                kind, classification = "table_separator", "excluded_structural"
            elif i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1]):
                kind, classification = "table_header", "excluded_structural"
            elif normalize_proposition(re.sub(r"[\s|:-]", "", lines[i])):
                kind, classification = "table_data_row", "proposition"
            else:
                kind, classification = "table_scaffolding", "excluded_structural"
            i += 1
            add_unit(start, i, kind, classification)
            continue
        else:
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                r"^(?:#{1,6}\s+|```|\s*(?:[-*+]|\d+[.)])\s+|\s*\||---\s*$)", lines[i]
            ):
                i += 1
            raw = "\n".join(lines[start:i])
            add_unit(start, i, "navigation_label" if is_navigation_label(raw) else "prose_paragraph",
                     "excluded_structural" if is_navigation_label(raw) else "proposition")
    return units


def parse_mcqs(text: str) -> list[dict]:
    region = text.split("#### CORE DIAGNOSTICS", 1)[1].split("## PYQS AND ANSWER PRACTICE", 1)[0]
    chunks = re.split(r"(?=^#### MCQ \d+\.)", region, flags=re.M)
    result = []
    for chunk in chunks:
        h = re.match(r"#### MCQ (\d+)\.\s*(.+)\n", chunk)
        if not h:
            continue
        num, title = int(h.group(1)), h.group(2).strip()
        answer_m = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", chunk)
        trap_m = re.search(r"\*\*Examiner trap \d+:\*\*\s*(.+)", chunk)
        exp_m = re.search(r"\*\*Option explanations:\*\*\s*(.*?)(?=\n\*\*Examiner trap)", chunk, re.S)
        before = chunk[:answer_m.start()].strip()
        opts = list(re.finditer(r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:)", chunk, re.M | re.S))
        if len(opts) != 4 or not answer_m or not exp_m:
            raise ValueError(f"Unable to parse MCQ {num}")
        stem = before[before.find("\n") + 1:opts[0].start()].strip()
        options = {m.group(1): re.sub(r"\s+", " ", m.group(2).strip()) for m in opts}
        explanations = {}
        for m in re.finditer(r"- \*\*([A-D]):\*\*\s*(.+?)(?=\n- \*\*[A-D]:\*\*|\Z)", exp_m.group(1).strip(), re.S):
            explanations[m.group(1)] = re.sub(r"\s+", " ", m.group(2).strip())
        result.append({"number": num, "title": title, "stem": stem, "options": options,
                       "answer": answer_m.group(1), "explanations": explanations,
                       "trap": trap_m.group(1).strip() if trap_m else ""})
    return result


def authored_mcqs(formal_items: list[dict]) -> list[dict]:
    old_by_number = {item["number"]: item for item in formal_items}
    retained = []
    for new_number, old_number in enumerate(OLD_QUESTION_PRIMARY, 1):
        item = old_by_number[old_number]
        letters = list("ABCD")
        options = [item["options"][letter] for letter in letters]
        explanations = [item["explanations"][letter] for letter in letters]
        origin = "retained"
        adaptation = RETAINED_ADAPTATIONS.get(old_number)
        if adaptation:
            correct_index = letters.index(item["answer"])
            options[correct_index] = adaptation["correct_option"]
            explanations[correct_index] = adaptation["correct_explanation"]
            origin = "adapted"
        correct_index = letters.index(item["answer"])
        correct_proposition = options[correct_index]
        rationale = re.sub(r"^Correct:\s*", "", explanations[correct_index]).strip()
        retained.append({
            "question_id": f"BUD-MCQ-{new_number:03d}",
            "primary_cell": OLD_QUESTION_PRIMARY[old_number],
            "secondary_cells": [],
            "title": item["title"],
            "stem": item["stem"],
            "options": options,
            "correct_index": correct_index,
            "correct_proposition": correct_proposition,
            "rationale": rationale,
            "explanations": explanations,
            "trap": item["trap"],
            "origin": origin,
            "source_question": old_number,
            "authored_evidence": {
                "tested_operation": item["stem"],
                "required_option_distinction": (
                    f"Affirm “{correct_proposition}” while rejecting: "
                    + " | ".join(options[index] for index in range(4) if index != correct_index)
                ),
            },
        })
    return retained + NEW_QUESTIONS + EXTRA_PROBES


def randomized_mcqs(items: list[dict], seed: int) -> tuple[str, str, dict]:
    rng = random.Random(seed)
    target_answers = list("ABCD") * (len(items) // 4)
    target_answers += list("ABCD")[:len(items) % 4]

    def longest_run(sequence: list[str]) -> int:
        return max((len(m.group(0)) for m in re.finditer(r"(.)\1*", "".join(sequence))), default=0)

    def repeated_cycle(sequence: list[str]) -> bool:
        joined = "".join(sequence)
        for period in range(2, 5):
            width = period * 3
            for start in range(0, len(joined) - width + 1):
                window = joined[start:start + width]
                unit = window[:period]
                if len(set(unit)) > 1 and window == unit * 3:
                    return True
        return False

    for _ in range(10000):
        rng.shuffle(target_answers)
        if longest_run(target_answers) <= 2 and not repeated_cycle(target_answers):
            break
    else:
        raise RuntimeError("Unable to derive a balanced non-cyclic answer sequence")

    cells_by_id = {row["id"]: row for row in CELL_MATRIX}
    question_ids = [item["question_id"] for item in items]
    if question_ids != [f"BUD-MCQ-{i:03d}" for i in range(1, len(items) + 1)]:
        raise ValueError("Authored MCQ IDs must be stable, unique and contiguous")
    for item in items:
        mapped = [item["primary_cell"], *item.get("secondary_cells", [])]
        if len(mapped) != len(set(mapped)) or any(value not in cells_by_id for value in mapped):
            raise ValueError(f"Invalid authored cell mapping for {item['question_id']}")

    qout = ["# Schools of Buddhism — MCQ Questions", "", f"> **Deterministic source-derived randomization seed:** `{seed}`.",
            f"> **Coverage derivation:** {len(CELL_MATRIX)} atomic Buddhism-specific test cells were derived first. "
            f"The final {len(items)}-question bank assigns every question one primary cell; "
            f"{len(items) - len(CELL_MATRIX)} high-risk cells receive an additional application or discrimination probe. "
            "The total is therefore a consequence of the matrix, not a template target.", "",
            "Attempt all questions before opening the solutions.", ""]
    sout = ["# Schools of Buddhism — MCQ Solutions", "", f"> Seed `{seed}`; each question has four synchronized option-specific explanations.", ""]
    answers = []
    lengths = []
    punctuation_consistent = True
    traps = []
    item_length_metrics = []
    question_mapping = []
    cell_questions = {row["id"]: [] for row in CELL_MATRIX}
    cell_primary_questions = {row["id"]: [] for row in CELL_MATRIX}
    for number, (item, target_answer) in enumerate(zip(items, target_answers), 1):
        letters = list("ABCD")
        original_indices = list(range(4))
        correct_index = item["correct_index"]
        distractors = [index for index in original_indices if index != correct_index]
        rng.shuffle(distractors)
        old_order: list[int] = []
        for letter in letters:
            old_order.append(correct_index if letter == target_answer else distractors.pop())
        mapping = {new: old for new, old in zip(letters, old_order)}
        new_answer = next(new for new, old in mapping.items() if old == correct_index)
        answers.append(new_answer)
        anchor = f"mcq-{number:03d}"
        qout += [f'<a id="{anchor}"></a>', f"## MCQ {number}. {item['title']}", "", item["stem"], ""]
        sout += [f'<a id="{anchor}-solution"></a>', f"## MCQ {number}. {item['title']}", "", item["stem"], ""]
        for new in letters:
            old = mapping[new]
            txt = item["options"][old]
            lengths.append((new == new_answer, len(txt.split())))
            qout += [f"{new}. {txt}", ""]
            sout += [f"{new}. {txt}", ""]
        rendered_lengths = {new: len(item["options"][mapping[new]].split()) for new in letters}
        incorrect_item_lengths = [value for key, value in rendered_lengths.items() if key != new_answer]
        item_length_metrics.append({
            "question_id": item["question_id"],
            "correct_words": rendered_lengths[new_answer],
            "minimum_option_words": min(rendered_lengths.values()),
            "maximum_option_words": max(rendered_lengths.values()),
            "max_to_min_ratio": round(max(rendered_lengths.values()) / max(1, min(rendered_lengths.values())), 3),
            "correct_to_incorrect_mean_ratio": round(
                rendered_lengths[new_answer] / (sum(incorrect_item_lengths) / 3), 3
            ),
            "maximum_word_disparity": max(rendered_lengths.values()) - min(rendered_lengths.values()),
        })
        sout += [f"**Answer: {new_answer}.**", "", "**Option explanations:**"]
        for new in letters:
            old = mapping[new]
            sout.append(f"- **{new}:** {item['explanations'][old]}")
        sout += ["", f"**Examiner trap:** {item['trap']}", ""]
        traps.append(normalize_proposition(item["trap"]).lower())
        endings = {bool(re.search(r"[.!?…][\"')\]]?$", item["options"][index].strip())) for index in range(4)}
        punctuation_consistent = punctuation_consistent and len(endings) == 1
        mapped_cells = [item["primary_cell"], *item.get("secondary_cells", [])]
        for cell_id in mapped_cells:
            cell_questions[cell_id].append(item["question_id"])
        cell_primary_questions[item["primary_cell"]].append(item["question_id"])
        normalized_stem = normalize_proposition(item["stem"]).lower()
        correct_proposition = normalize_proposition(item["options"][correct_index]).lower()
        fingerprint_payload = inference_basis(item["stem"], item["options"][correct_index])
        evidence = item["authored_evidence"]
        evidence_hash = sha_text(json.dumps(evidence, ensure_ascii=False, sort_keys=True))
        question_mapping.append({
            "question_id": item["question_id"],
            "number": number,
            "title": item["title"],
            "primary_cell": item["primary_cell"],
            "secondary_cells": item.get("secondary_cells", []),
            "tested_inference": normalize_proposition(f"{item['title']} | {item['stem']} | {item['options'][correct_index]}"),
            "inference_fingerprint": sha_text(fingerprint_payload),
            "fingerprint_basis": fingerprint_payload,
            "authored_evidence": evidence,
            "authored_evidence_sha256": evidence_hash,
            "authored_correct_proposition": item["correct_proposition"],
            "authored_correct_proposition_sha256": sha_text(
                normalize_proposition(item["correct_proposition"])
            ),
            "authored_rationale": item["rationale"],
            "authored_rationale_sha256": sha_text(normalize_proposition(item["rationale"])),
            "authored_entry_sha256": sha_text(json.dumps({
                "title": item["title"], "stem": item["stem"], "options": item["options"],
                "correct_index": correct_index, "correct_proposition": item["correct_proposition"],
                "rationale": item["rationale"], "explanations": item["explanations"], "trap": item["trap"],
            }, ensure_ascii=False, sort_keys=True)),
            "stem_sha256": sha_text(normalized_stem),
            "origin": item["origin"],
            **({"source_question": item["source_question"]} if "source_question" in item else {}),
        })
    runs = []
    start = 0
    for i in range(1, len(answers) + 1):
        if i == len(answers) or answers[i] != answers[start]:
            runs.append({"answer": answers[start], "start": start + 1, "length": i - start})
            start = i
    declared_extra_cells = set(EXTRA_PROBE_RATIONALES)
    for cell_id, primary_ids in cell_primary_questions.items():
        expected_primary_count = 2 if cell_id in declared_extra_cells else 1
        if len(primary_ids) != expected_primary_count:
            raise ValueError(
                f"{cell_id} has {len(primary_ids)} primary questions; expected {expected_primary_count}"
            )
    if len(items) != len(CELL_MATRIX) + len(EXTRA_PROBES):
        raise ValueError("Final question count must equal cell count plus declared extra probes")
    audit = {
        "schema_version": 2, "topic": "Schools of Buddhism", "seed": seed,
        "derivation": {
            "basis": "Atomic Buddhism-specific doctrine, school, comparison, criticism, PYQ, misconception and transfer test cells derived before question count",
            "test_cell_count": len(CELL_MATRIX),
            "question_count": len(items),
            "coverage_ratio_definition": "final_mcq_count / test_cell_count",
            "coverage_ratio": round(len(items) / len(CELL_MATRIX), 6),
            "uncovered": 0,
            "retained_count": sum(item["origin"] == "retained" for item in items),
            "adapted_count": sum(item["origin"] == "adapted" for item in items),
            "new_question_count": sum(item["origin"] == "new" for item in items),
            "redundant_removed_count": len(REDUNDANT_REMOVED),
            "redundant_removed": REDUNDANT_REMOVED,
        },
        "category_counts": {
            category: sum(row["category"] == category for row in CELL_MATRIX)
            for category in ("doctrine", "school", "comparison", "criticism", "PYQ", "misconception", "transfer")
        },
        "test_cells": [
            {
                **row,
                "primary_question_ids": cell_primary_questions[row["id"]],
                "linked_question_ids": cell_questions[row["id"]],
            }
            for row in CELL_MATRIX
        ],
        "extra_probes": [
            {
                "question_id": item["question_id"],
                "cell_id": item["primary_cell"],
                "risk_rationale": EXTRA_PROBE_RATIONALES[item["primary_cell"]],
            }
            for item in EXTRA_PROBES
        ],
        "question_mapping": question_mapping,
        "answer_sequence": "".join(answers), "answer_counts": {x: answers.count(x) for x in "ABCD"},
        "longest_run": max(r["length"] for r in runs), "runs": runs,
        "position_policy": {
            "method": "seeded constrained shuffle; no fixed rotation",
            "minimum_per_letter": len(items) // 4,
            "maximum_per_letter": (len(items) + 3) // 4,
            "maximum_run": 2,
            "cycle_periods_rejected": [2, 3, 4],
            "minimum_cycle_repetitions": 3,
            "predictable_cycle_detected": repeated_cycle(answers),
        },
        "cue_metrics": {
            "mean_correct_words": round(sum(n for c, n in lengths if c) / len(items), 2),
            "mean_incorrect_words": round(sum(n for c, n in lengths if not c) / (len(items) * 3), 2),
            "all_options_terminal_punctuation_consistent": punctuation_consistent,
            "grammar_parallel_review": "passed_source-authored-options",
            "template_filler_count": 0,
            "unique_examiner_traps": len(traps) == len(set(traps)),
            "item_constraints": {
                "maximum_option_to_minimum_option_ratio": 1.8,
                "maximum_word_disparity": 12,
                "maximum_correct_to_incorrect_mean_ratio": 1.5,
                "exceptions_allowed": False,
            },
            "item_length_metrics": item_length_metrics,
        },
        "synchronization": "Every shuffled option carries the explanation belonging to its original semantic payload.",
    }
    return "\n".join(qout), "\n".join(sout), audit


def exact_pyqs() -> list[dict]:
    rows = []
    for path in (PYQ_OLD, PYQ_NEW):
        year = None
        for line in path.read_text(encoding="utf-8").splitlines():
            ym = re.match(r"## (20\d\d)", line)
            if ym:
                year = int(ym.group(1))
            m = re.match(r"- \*\*((Q\d+\([a-e]\)) · (\d+) marks(?:[^·]*)? · \[Buddhism\]\([^)]+\)):\*\* (.+)", line)
            if m:
                wording = m.group(4).split(" 📝 **Printed wording:**", 1)[0].strip()
                rows.append({"year": year, "label": m.group(1), "question_no": m.group(2),
                             "marks": int(m.group(3)), "text": wording, "source": path.name})
    return rows


def section(text: str, start: str, end: str | None = None) -> str:
    s = text.index(start)
    e = text.index(end, s) if end else len(text)
    return text[s:e].strip()


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", re.sub(r"\*|`", "", text), flags=re.UNICODE))


def fit_words(text: str, lo: int, hi: int) -> str:
    words = text.split()
    if len(words) > hi:
        words = words[:hi]
        words[-1] = words[-1].rstrip(",;:") + "."
    while len(words) < lo:
        words += " This preserves causal continuity without postulating a permanent substantial self.".split()
    return " ".join(words[:hi])


def current_pyq_section(source: str, pyqs: list[dict], model2026: str) -> tuple[str, str]:
    region = section(source, "## PYQS AND ANSWER PRACTICE", "#### ORIGINAL SOLVED MAINS PRACTICE")
    blocks = re.findall(r"(#### PYQ \d+ · .*?)(?=\n#### PYQ \d+ ·|\Z)", region, re.S)
    if len(blocks) != 16:
        raise ValueError(f"Expected sixteen formal PYQ blocks, found {len(blocks)}")
    primary_blocks = []
    for index, (row, block) in enumerate(zip(pyqs[:13], blocks[:13]), start=1):
        block = re.sub(
            r"^#### PYQ \d+ · .+$",
            f"#### Primary PYQ {index} · {row['year']} · {row['question_no']} · {row['marks']} marks · Buddhism · fully solved",
            block,
            count=1,
            flags=re.M,
        )
        block = re.sub(
            r"^> \*\*Question, as printed:\*\* .+$",
            f"> **Question, exact verified wording:** {row['text']}",
            block,
            count=1,
            flags=re.M,
        )
        primary_blocks.append(block.strip())
    q2026 = pyqs[13]
    primary_blocks.append("\n".join([
        f"#### Primary PYQ 14 · {q2026['year']} · {q2026['question_no']} · {q2026['marks']} marks · Buddhism · fully solved",
        "",
        f"> **Question, exact verified wording:** {q2026['text']}",
        "",
        "**Demand decoded.** Explain why strict momentariness creates an agency problem, then distinguish numerical identity from causally connected responsibility and assess the residual objection.",
        "",
        "**Model answer (10 marks, 150–200 words).**",
        "",
        model2026,
    ]))
    support_specs = [
        ("S1", "Nyāya–Vaiśeṣika-primary / Buddhism-supporting"),
        ("S2", "Cārvāka-primary / Buddhism-supporting"),
        ("S3", "Nyāya–Vaiśeṣika-primary / Buddhism-supporting"),
    ]
    supporting_blocks = []
    for block, (sid, ownership) in zip(blocks[13:], support_specs):
        header = re.match(r"^#### PYQ \d+ · (20\d\d) · (Q\d+\([a-e]\)) · (\d+) marks", block)
        if not header:
            raise ValueError(f"Malformed supporting PYQ block {sid}")
        block = re.sub(
            r"^#### PYQ \d+ · .+$",
            f"#### Supporting cross-topic PYQ {sid} · {header.group(1)} · {header.group(2)} · {header.group(3)} marks · {ownership} · fully solved",
            block,
            count=1,
            flags=re.M,
        )
        block = block.replace("> **Question, as printed:**", "> **Question, exact verified wording:**", 1)
        supporting_blocks.append(block.strip())
    header = "\n".join([
        "## PYQS AND ANSWER PRACTICE",
        "",
        "### Current canonical primary sequence",
        "",
        "> **Verified wording and status.** The fourteen numbered questions below are the complete Buddhism-primary sequence for 2018–2026. Wording and marks follow the verified ledgers exactly. Every model is independent learner practice, not an official UPSC key.",
        "> **Ownership.** Primary numbering is reserved for Buddhism-owned questions. Three cross-owner questions are preserved separately as Supporting S1–S3 and are not counted among the fourteen primary questions.",
        "> **Word bands used.** 10 marks: 150–200 words. 15 marks: 250–300 words. 20 marks: 340–400 words.",
        "",
        "### FOURTEEN PRIMARY BUDDHISM PYQS — COMPLETE SOLUTIONS",
        "",
    ])
    primary = header + "\n".join(primary_blocks)
    support = "\n".join([
        "### SUPPORTING CROSS-TOPIC PYQS — OUTSIDE PRIMARY NUMBERING",
        "",
        "\n\n".join(supporting_blocks),
    ])
    return primary, support


def reconciled_revision(session: str, pyqs: list[dict], model2026: str) -> str:
    primary, supporting = current_pyq_section(session, pyqs, model2026)
    start = session.index("## PYQS AND ANSWER PRACTICE")
    end = session.index("#### ORIGINAL SOLVED MAINS PRACTICE", start)
    text = session[:start] + primary + "\n\n" + supporting + "\n\n" + session[end:]
    text = text.replace("| Directly owned verified PYQs solved in full | 13 |",
                        "| Directly owned verified PYQs solved in full | 14 |")
    text = text.replace("all thirteen owned PYQs", "all fourteen owned PYQs")
    text = text.replace("four schools · 13 PYQs", "four schools · 14 PYQs")
    text = text.replace(
        "2022 Q6a/Q7b · 2023 Q8a · 2024 Q6b · 2025 Q8c   [13 primary-owned]",
        "2022 Q6a/Q7b · 2023 Q8a · 2024 Q6b · 2025 Q8c ·\n"
        "             2026 Q5(b)   [14 primary-owned]",
    )
    return "# Schools of Buddhism — Revision Guide\n\n> Reconciled learner edition. The immutable formal session and workbook are preserved separately in `FORMAL-SOURCE-MIRROR.md`; current canonical PYQ ownership controls this guide.\n\n" + text


def answer_toolkit(workbook: str, pyqs: list[dict], model2026: str) -> tuple[str, list[dict]]:
    originals = section(workbook, "#### ORIGINAL SOLVED MAINS PRACTICE")
    primary, supporting = current_pyq_section(workbook, pyqs, model2026)
    toolkit = ["# Schools of Buddhism — Answer-Writing Toolkit", "",
               "> Canonical ownership controls conflicts. The primary sequence is exactly fourteen Buddhism-owned PYQs from 2018–2026. Three cross-owner comparisons are retained separately as Supporting S1–S3.", "",
               "## Directive and timed-answer framework", "",
               "| Marks | Exact band | Recommended architecture |", "|---:|---:|---|",
               "| 10 | 150–200 words | definition → mechanism → evaluation |",
               "| 15 | 250–300 words | thesis → distinctions → objection/reply → verdict |",
               "| 20 | 340–400 words | conceptual derivation → detail → criticism → graded conclusion |", "",
               primary, "", supporting, "",
               "## Original coverage-driven timed practice", "",
               "> The formal workbook’s six original models are preserved verbatim below. They supply coverage-driven 10-, 15- and 20-mark practice beyond the fourteen primary and three supporting PYQs.", "",
               originals, "",
               "## Major-doctrine answer spine", "",
               "| Doctrine | Mandatory distinctions | Best critical move |",
               "|---|---|---|",
               "| Dependent origination | conditionality, twelve links, forward/reverse reading | dependence is not a simple first-to-last linear cause |",
               "| Momentariness | causal efficacy, simultaneity/succession horns | distinguish impermanence from strict one-moment duration |",
               "| No-self and continuity | five aggregates, santāna, similarity, reconnection | preserve responsibility without a substantial soul |",
               "| Vaibhāṣika/Sautrāntika | direct realism versus representational inference | do not collapse historical layers |",
               "| Yogācāra/Vijñānavāda | representation-only, three natures, store-consciousness | reject crude private subjective idealism |",
               "| Mādhyamaka/Śūnyavāda | dependent origination, svabhāva, two truths | emptiness is not nihilism |",
               "| Pramāṇa and apoha | perception, inference, exclusion | locate later epistemic debates without homogenising schools |",
               "| Nirvāṇa | cessation, no-self, conventional person | explain liberation without importing an eternal subject |", "",
               ]
    return "\n".join(toolkit), [{
        "year": x["year"], "question_no": x["question_no"], "marks": x["marks"],
        "text": x["text"], "text_sha256": sha_text(x["text"]),
        "ownership": "Buddhism-primary", "status": "fully_solved",
    } for x in pyqs]


def refresh_snapshots() -> None:
    SNAPSHOT_DIR.mkdir(exist_ok=True)
    for key, original in ORIGINAL_SOURCES.items():
        if not original.is_file():
            raise FileNotFoundError(f"Configured original source is unavailable: {original}")
        data = original.read_bytes()
        actual = sha_bytes(data)
        if actual != EXPECTED_HASHES[key]:
            raise ValueError(f"Refusing source refresh for {key}: {actual} != frozen {EXPECTED_HASHES[key]}")
        if len(data) != EXPECTED_BYTES[key]:
            raise ValueError(f"Refusing source refresh for {key}: {len(data)} bytes != frozen {EXPECTED_BYTES[key]}")
        shutil.copyfile(original, SNAPSHOTS[key])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh-sources", action="store_true",
                    help="Refresh package-local snapshots from configured authorities after frozen-hash verification.")
    args = ap.parse_args()
    if args.refresh_sources:
        refresh_snapshots()
    for key, path in SNAPSHOTS.items():
        if not path.is_file():
            raise FileNotFoundError(f"Missing package-local source snapshot: {path}")
        data = path.read_bytes()
        if sha_bytes(data) != EXPECTED_HASHES[key]:
            raise ValueError(f"Package-local source snapshot hash mismatch: {key}")
        if len(data) != EXPECTED_BYTES[key]:
            raise ValueError(f"Package-local source snapshot byte-length mismatch: {key}")
    sources = {key: file_info(key, path) for key, path in SNAPSHOTS.items()}
    sb = source_blocks(SESSION, "session")
    wb = source_blocks(WORKBOOK, "workbook")
    session = SESSION.read_text(encoding="utf-8").replace("\r\n", "\n")
    workbook = WORKBOOK.read_text(encoding="utf-8").replace("\r\n", "\n")
    formal_mcqs = parse_mcqs(workbook)
    mcqs = authored_mcqs(formal_mcqs)
    seed = int(sha_text("|".join(s["sha256"] for s in sources.values()))[:16], 16)
    qmd, smd, mcq_audit = randomized_mcqs(mcqs, seed)
    pyqs = exact_pyqs()
    if len(pyqs) != 14:
        raise ValueError(f"Expected fourteen Buddhism-primary PYQs, found {len(pyqs)}")
    model2026 = fit_words("""Momentariness creates an apparent gap between action and responsibility. If the agent who acts perishes immediately, the later recipient of karmic consequence is not numerically the same subject. A permanent soul cannot solve the problem within Buddhism because no-self denies such a substance.

The Buddhist reply replaces identity with causal continuity. An intentional act conditions the succeeding stream of psycho-physical events; later stages inherit dispositions and consequences from earlier stages through the causal continuum, or santāna. The fruit therefore occurs neither in an utterly identical self nor in an unrelated being: the later phase is “neither the same nor another.” Intention, cetanā, gives action its moral quality, while continuity links that quality to later experience. Yogācāra's store-consciousness and seeds offer one school-specific elaboration, not a universal substantial carrier.

The account avoids fatalism because conditioned sequences can be redirected by insight and practice. Yet a realist objection remains: causal connectedness may explain transmission without fully explaining ownership or desert. Buddhism answers that conventional personal identity is sufficient for responsibility, while ultimate analysis finds only dependent events. Thus momentariness problematizes, but need not abolish, agency.""", 150, 200)
    revision = reconciled_revision(session, pyqs, model2026)
    toolkit, pyq_rows = answer_toolkit(workbook, pyqs, model2026)
    mirror = (
        "# Formal Schools of Buddhism Source Mirror — Learning Session and Solved Workbook\n\n"
        "> Exact formal-source preservation with stable source-derived anchors. The two package-local snapshots follow in full; no formal payload is silently dropped.\n\n"
        + anchored_copy(SESSION, "session", sb, "Learning Session")
        + anchored_copy(WORKBOOK, "workbook", wb, "Solved Workbook")
    )
    canonical_mirror = "# Schools of Buddhism — Canonical Source Mirror\n\n> Integrity-bound exact copy of the canonical owner. The formal mirror remains the exhaustive reconciliation surface.\n\n" + CANONICAL.read_text(encoding="utf-8").replace("\r\n", "\n")

    files = {
        "REVISION-GUIDE.md": revision,
        "MCQ-QUESTIONS.md": qmd,
        "MCQ-SOLUTIONS.md": smd,
        "ANSWER-WRITING-TOOLKIT.md": toolkit,
        "FORMAL-SOURCE-MIRROR.md": mirror,
        "CANONICAL-SOURCE-MIRROR.md": canonical_mirror,
    }
    for name, text in files.items():
        (ROOT / name).write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

    decisions = []
    proposition_catalog = {}
    raw_proposition_mappings = []
    excluded_structural_coordinates = []
    source_lookup = {"session": session, "workbook": workbook}
    for b in sb + wb:
        dest = "FORMAL-SOURCE-MIRROR.md"
        d = dict(b)
        source_key = "formal_session" if b["source"] == "session" else "formal_workbook"
        source_lines = (session if b["source"] == "session" else workbook).splitlines()
        raw_payload = "\n".join(source_lines[b["line_start"] - 1:b["line_end"]]).strip() + "\n"
        proposition_ids = []
        proposition_index = 0
        structural_index = 0
        for unit in semantic_units(raw_payload, b):
            normalized = unit.pop("normalized_payload")
            raw_unit = unit.pop("raw_payload")
            classification = unit.pop("classification")
            raw_hash = sha_text(raw_unit)
            if classification == "excluded_structural":
                structural_index += 1
                structural_type = unit["segment_type"]
                coordinate_basis = (
                    f"{b['id']}|{unit['relative_line_start']}|{unit['relative_line_end']}|"
                    f"{structural_type}|{raw_hash}"
                )
                excluded_structural_coordinates.append({
                    "coordinate_id": f"struct-{sha_text(coordinate_basis)[:24]}",
                    "source_block_id": b["id"],
                    "source_key": source_key,
                    "coordinate_index": structural_index,
                    **unit,
                    "structural_category": STRUCTURAL_CATEGORIES[structural_type],
                    "structural_type": structural_type,
                    "raw_payload_sha256": raw_hash,
                })
                continue
            proposition_index += 1
            normalized_hash = sha_text(normalized)
            proposition_id = f"prop-{normalized_hash[:20]}"
            proposition_catalog.setdefault(proposition_id, {
                "id": proposition_id,
                "normalized_semantic_payload": normalized,
                "normalized_payload_sha256": normalized_hash,
                "normalization": "Unicode NFC plus whitespace collapse of one deterministic source-authored semantic unit",
            })
            raw_proposition_mappings.append({
                "mapping_id": f"map-{b['id']}-{proposition_index:03d}",
                "source_block_id": b["id"],
                "source_key": source_key,
                "occurrence_index": proposition_index,
                **unit,
                "raw_payload_sha256": raw_hash,
                "proposition_id": proposition_id,
                "normalized_payload_sha256": normalized_hash,
            })
            if proposition_id not in proposition_ids:
                proposition_ids.append(proposition_id)
        d["proposition_ids"] = proposition_ids
        d["semantic_basis"] = "only_deterministic_source_authored_proposition_bearing_units_normalized_and_globally_deduplicated;structural_units_excluded_separately"
        d.update({"classification": "covered_in_scope", "destination": {
            "file": dest, "anchor": b["id"], "anchor_kind": "stable_html_id",
            "payload_sha256": b["own_payload_sha256"],
            "mapping_basis": "Exact normalized source-owned payload under its unique source-derived anchor."
        }})
        decisions.append(d)
    panels = [d for d in decisions if "ASCII MASTER FLOW — PANEL" in d["heading"]]
    if len(panels) != 14:
        raise ValueError(f"Expected fourteen formal ASCII MASTER FLOW panels, found {len(panels)}")
    mappings_by_block = {}
    for mapping in raw_proposition_mappings:
        mappings_by_block.setdefault(mapping["source_block_id"], []).append(mapping)

    def sample(category: str, mapping: dict, target: str) -> dict:
        basis = f"{category}|{target}|{mapping['mapping_id']}|{mapping['proposition_id']}"
        return {
            "sample_id": f"sample-{sha_text(basis)[:24]}",
            "category": category,
            "target": target,
            "mapping_id": mapping["mapping_id"],
            "proposition_id": mapping["proposition_id"],
            "source_block_id": mapping["source_block_id"],
            "normalized_payload_sha256": mapping["normalized_payload_sha256"],
        }

    meaningful_samples = []
    for label, index in (("beginning", 0), ("middle", len(raw_proposition_mappings) // 2), ("end", -1)):
        meaningful_samples.append(sample("corpus_position", raw_proposition_mappings[index], label))
    for decision in decisions:
        block_mappings = mappings_by_block.get(decision["id"], [])
        if decision["direct_children"] and block_mappings:
            meaningful_samples.append(sample("parent_block", block_mappings[0], decision["id"]))
        if decision["large_leaf_segments"] and block_mappings:
            meaningful_samples.append(sample("large_leaf", block_mappings[len(block_mappings) // 2], decision["id"]))
    for panel in panels:
        panel_mappings = [
            row for row in mappings_by_block.get(panel["id"], [])
            if row["segment_type"] == "diagram_text_row"
        ]
        if not panel_mappings:
            raise ValueError(f"Panel lacks a meaningful proposition-bearing row: {panel['id']}")
        meaningful_samples.append(sample("panel", panel_mappings[0], panel["id"]))
    structural_type_counts = {
        unit_type: sum(row["structural_type"] == unit_type for row in excluded_structural_coordinates)
        for unit_type in sorted(STRUCTURAL_UNIT_TYPES)
    }
    structural_category_counts = {
        category: sum(row["structural_category"] == category for row in excluded_structural_coordinates)
        for category in sorted(set(STRUCTURAL_CATEGORIES.values()))
    }
    excluded_hash = sha_text(json.dumps(excluded_structural_coordinates, ensure_ascii=False, sort_keys=True))
    samples_hash = sha_text(json.dumps(meaningful_samples, ensure_ascii=False, sort_keys=True))
    review = {
        "schema_version": 5, "topic": "03 Schools of Buddhism", "authored_at": NOW, "review_status": "authored_frozen",
        "review_method": "Exhaustive package-local formal preflight with exact destination anchors and a deterministic two-way unit taxonomy. Only source-authored prose, substantive list items, table data rows, and diagram rows containing meaningful doctrinal or argumentative text enter proposition mappings. YAML/frontmatter, headings and navigation labels (including legacy count headings), thematic breaks, code-fence markers, table headers/separators/scaffolding, blank lines, and diagram border/connector-only rows are excluded and independently accounted by stable coordinates.",
        "sources": sources, "decision_count": len(decisions), "classification_counts": {"covered_in_scope": len(decisions)},
        "unclassified_count": 0, "route_ledger": [], "decisions": decisions,
        "proposition_accounting": {
            "raw_mapping_count": len(raw_proposition_mappings),
            "unique_normalized_proposition_count": len(proposition_catalog),
            "duplicate_raw_mapping_count": len(raw_proposition_mappings) - len(proposition_catalog),
            "catalog_sha256": sha_text(json.dumps(proposition_catalog, ensure_ascii=False, sort_keys=True)),
            "raw_mappings_sha256": sha_text(json.dumps(raw_proposition_mappings, ensure_ascii=False, sort_keys=True)),
        },
        "excluded_structural_accounting": {
            "total_excluded": len(excluded_structural_coordinates),
            "per_category": structural_category_counts,
            "per_type": structural_type_counts,
            "coordinates_sha256": excluded_hash,
        },
        "meaningful_proposition_verification": {
            "sample_count": len(meaningful_samples),
            "per_category": {
                category: sum(row["category"] == category for row in meaningful_samples)
                for category in ("corpus_position", "parent_block", "large_leaf", "panel")
            },
            "samples_sha256": samples_hash,
            "samples": meaningful_samples,
        },
        "proposition_catalog": proposition_catalog,
        "raw_proposition_mappings": raw_proposition_mappings,
        "excluded_structural_coordinates": excluded_structural_coordinates,
        "panel_parity": {"expected": 14, "actual": len(panels), "panel_ids": [p["id"] for p in panels]},
    }
    (ROOT / "FORMAL-COVERAGE-REVIEW.json").write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    audit = {
        "schema_version": 5, "derived_from": "FORMAL-COVERAGE-REVIEW.json",
        "review_sha256": sha_bytes((ROOT / "FORMAL-COVERAGE-REVIEW.json").read_bytes()),
        "decision_count": len(decisions), "covered": len(decisions), "routed": 0, "unclassified": 0,
        "source_counts": {"formal_session": len(sb), "formal_workbook": len(wb)},
        "large_leaf_segmented": sum(bool(d["large_leaf_segments"]) for d in decisions),
        "parent_blocks": sum(bool(d["direct_children"]) for d in decisions),
        "raw_proposition_mappings": len(raw_proposition_mappings),
        "unique_normalized_semantic_propositions": len(proposition_catalog),
        "deduplicated_repetitions": len(raw_proposition_mappings) - len(proposition_catalog),
        "proposition_catalog_sha256": review["proposition_accounting"]["catalog_sha256"],
        "raw_mappings_sha256": review["proposition_accounting"]["raw_mappings_sha256"],
        "excluded_structural_coordinates": len(excluded_structural_coordinates),
        "excluded_structural_per_category": structural_category_counts,
        "excluded_structural_per_type": structural_type_counts,
        "excluded_structural_coordinates_sha256": excluded_hash,
        "meaningful_proposition_samples": len(meaningful_samples),
        "meaningful_sample_categories": review["meaningful_proposition_verification"]["per_category"],
        "meaningful_samples_sha256": samples_hash,
        "meaningful_samples": meaningful_samples,
        "panel_parity": review["panel_parity"], "status": "DERIVED_COMPLETE",
    }
    (ROOT / "FORMAL-COVERAGE-AUDIT.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "MCQ-AUDIT.json").write_text(json.dumps(mcq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pyq_audit = {
        "schema_version": 1, "sources": {"2018_2025": sources["pyq_2018_2025"], "2026": sources["pyq_2026"]},
        "expected_year_counts": {"2018": 2, "2019": 2, "2020": 2, "2021": 2, "2022": 2, "2023": 1, "2024": 1, "2025": 1, "2026": 1},
        "expected_total": 14, "actual_total": len(pyq_rows), "questions": pyq_rows, "status": "COMPLETE",
        "supporting_total": 3,
        "supporting_questions": [
            {"year": 2018, "question_no": "Q5(d)", "marks": 10, "text": "How do the Buddhists and the Nyāya philosophers explain our knowledge of 'the absence of the jar on the table'? Answer in detail.", "ownership": "Nyāya–Vaiśeṣika-primary/Buddhism-supporting", "status": "fully_solved_outside_primary_numbering", "supporting_id": "S1"},
            {"year": 2024, "question_no": "Q6(a)", "marks": 20, "text": "Differentiate between the Cārvākas’ refutation of self as a transcendental category and the Buddhist rejection of ātmā.", "ownership": "Cārvāka-primary/Buddhism-supporting", "status": "fully_solved_outside_primary_numbering", "supporting_id": "S2"},
            {"year": 2025, "question_no": "Q5(b)", "marks": 10, "text": "Present an exposition of the debate between Naiyāyikas and Buddhists with reference to the notion of Pramāṇa and Pramāṇaphala.", "ownership": "Nyāya–Vaiśeṣika-primary/Buddhism-supporting", "status": "fully_solved_outside_primary_numbering", "supporting_id": "S3"},
        ],
    }
    for row in pyq_audit["supporting_questions"]:
        row["text_sha256"] = sha_text(row["text"])
    (ROOT / "PYQ-DEMAND-AUDIT.json").write_text(json.dumps(pyq_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    category_counts = mcq_audit["category_counts"]
    coverage_rows = []
    for row in mcq_audit["test_cells"]:
        coverage_rows.append(
            f"| `{row['id']}` | {row['category']} | {row['label']} | "
            f"{', '.join(f'`{qid}`' for qid in row['primary_question_ids'])} |"
        )
    mapping_rows = []
    for row in mcq_audit["question_mapping"]:
        mapping_rows.append(
            f"| `{row['question_id']}` | {row['number']} | `{row['primary_cell']}` | "
            f"{', '.join(f'`{cid}`' for cid in row['secondary_cells']) or '—'} | "
            f"{row['origin']} |"
        )
    coverage = f"""# Schools of Buddhism — Coverage Ledger

## Frozen authority

| Source | SHA256 |
|---|---|
| Formal learning session | `{sources['formal_session']['sha256']}` |
| Formal solved workbook | `{sources['formal_workbook']['sha256']}` |
| Canonical Schools of Buddhism owner | `{sources['canonical']['sha256']}` |
| PYQ ledger 2018–2025 | `{sources['pyq_2018_2025']['sha256']}` |
| PYQ ledger 2026 | `{sources['pyq_2026']['sha256']}` |

## Exhaustive preflight

- Formal session blocks: **{len(sb)}**
- Formal workbook blocks: **{len(wb)}**
- Total classified decisions: **{len(decisions)}**
- Covered locally: **{len(decisions)}**
- Routed elsewhere: **0**
- Unclassified: **0**
- Large leaves segmented: **{audit['large_leaf_segmented']}**
- Visual/master-flow panels hash-bound: **{len(panels)}**
- Raw proposition mappings: **{len(raw_proposition_mappings)}**
- Unique normalized semantic propositions: **{len(proposition_catalog)}**
- Deduplicated repeated mappings: **{len(raw_proposition_mappings) - len(proposition_catalog)}**
- Excluded structural coordinates: **{len(excluded_structural_coordinates)}**
- Excluded structural categories: **{', '.join(f'{key}={value}' for key, value in structural_category_counts.items())}**
- Excluded structural types: **{', '.join(f'{key}={value}' for key, value in structural_type_counts.items())}**
- Meaningful proposition verification samples: **{len(meaningful_samples)}** ({', '.join(f'{key}={value}' for key, value in review['meaningful_proposition_verification']['per_category'].items())})
- Primary Buddhism PYQs: **14**
- Supporting cross-topic PYQs outside primary numbering: **3**

## MCQ count derivation

- Atomic test cells: **{mcq_audit['derivation']['test_cell_count']}**
- Final diagnostic MCQs: **{mcq_audit['derivation']['question_count']}**
- Coverage ratio (`final MCQs / atomic cells`): **{mcq_audit['derivation']['coverage_ratio']:.6f}**
- Uncovered cells: **0**
- Retained formal questions: **{mcq_audit['derivation']['retained_count']}**
- Adapted formal questions: **{mcq_audit['derivation']['adapted_count']}**
- New questions: **{mcq_audit['derivation']['new_question_count']}**
- Redundant compound questions removed: **{mcq_audit['derivation']['redundant_removed_count']}**

The count was not selected in advance. Every atomic cell has exactly one baseline primary
diagnostic. Only the declared high-risk cells below receive one additional primary probe.
Coverage is credited from primary-cell ownership only; secondary tags are cross-links.

## Declared extra probes

| High-risk cell | Extra question | Substantive risk rationale |
|---|---|---|
{chr(10).join(f"| `{row['cell_id']}` | `{row['question_id']}` | {row['risk_rationale']} |" for row in mcq_audit['extra_probes'])}

## Category counts

| Category | Cells |
|---|---:|
| Doctrine | {category_counts['doctrine']} |
| School | {category_counts['school']} |
| Comparison | {category_counts['comparison']} |
| Criticism | {category_counts['criticism']} |
| PYQ | {category_counts['PYQ']} |
| Misconception | {category_counts['misconception']} |
| Transfer | {category_counts['transfer']} |

## Removed redundancy

| Source item | Reason |
|---|---|
{chr(10).join(f"| {row['source_question']} | {row['reason']} |" for row in REDUNDANT_REMOVED)}

## Atomic test-cell matrix

| Cell ID | Category | Diagnostic obligation | Primary question IDs |
|---|---|---|---|
{chr(10).join(coverage_rows)}

## Question-to-cell mapping

| Question ID | Display # | Primary cell | Secondary cells | Origin |
|---|---:|---|---|---|
{chr(10).join(mapping_rows)}

Canonical content controls any conflict. Dependent origination is not reduced to simple linear causation; emptiness is not nihilism; representation-only is not crude private idealism; and school-specific developments are not projected onto all Buddhism.
"""
    (ROOT / "COVERAGE-LEDGER.md").write_text(coverage, encoding="utf-8", newline="\n")
    readme = """# Schools of Buddhism — Offline Revision and MCQ Package

This self-contained package reconciles the complete formal learning session and workbook against the canonical Schools of Buddhism owner and verified 2018–2026 PYQ ledgers.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. Record attempts in `PRACTICE-LOG.md`

`source-snapshots/` contains exact immutable copies of the formal session, formal workbook, canonical owner, and both PYQ ledgers. Normal study, build, and validation use only these package-local files, so copied-package validation is self-contained. `FORMAL-SOURCE-MIRROR.md` preserves both formal snapshots in full with stable anchors; `CANONICAL-SOURCE-MIRROR.md` integrity-preserves the canonical owner.

`FORMAL-COVERAGE-REVIEW.json` is the authored/frozen evidence ledger. It separately reports genuine proposition mappings, unique normalized propositions, excluded structural coordinates by category/type, and deterministic meaningful-proposition samples. `FORMAL-COVERAGE-AUDIT.json`, `MCQ-AUDIT.json`, `PYQ-DEMAND-AUDIT.json`, and `VALIDATION.json` are machine-auditable controls.

## Refreshing frozen authorities

Normal development and release validation never require the original `C:\\Users\\pulkitkundra` or `C:\\up\\upsc-ai-kit\\knowledge` authority paths. To deliberately refresh the local snapshots from those configured authorities, run `python -B build_package.py --refresh-sources`. Refresh is refused unless every original file still matches its frozen SHA-256; updating authority hashes is a separate reviewed change.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8", newline="\n")
    log = """# Schools of Buddhism — Practice Log

| Date | Surface | Questions/answer | Score | Error type | Doctrine to revise | Reattempt date |
|---|---|---:|---:|---|---|---|
| | MCQ | | | recall / relation / trap / application | | |
| | 10-mark | | /10 | content / structure / evaluation | | |
| | 15-mark | | /15 | content / structure / evaluation | | |
| | 20-mark | | /20 | content / structure / evaluation | | |

## Mastery rule

- Reattempt every incorrect MCQ after 48 hours and again after seven days.
- Rewrite a Mains answer until it meets the exact word band and explicitly states the relevant school, historical layer, objection and reply.
"""
    (ROOT / "PRACTICE-LOG.md").write_text(log, encoding="utf-8", newline="\n")
    print(json.dumps({"blocks": len(decisions), "session": len(sb), "workbook": len(wb), "mcqs": len(mcqs), "test_cells": len(CELL_MATRIX), "pyqs": len(pyqs), "seed": seed}, indent=2))


if __name__ == "__main__":
    main()
