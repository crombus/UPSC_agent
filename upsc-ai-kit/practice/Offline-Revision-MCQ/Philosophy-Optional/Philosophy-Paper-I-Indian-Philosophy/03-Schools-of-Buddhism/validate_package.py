from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.dont_write_bytecode = True

from pypdf import PdfReader

from mcq_bank import (
    CELL_MATRIX,
    EXTRA_PROBES,
    EXTRA_PROBE_RATIONALES,
    NEW_QUESTIONS,
    OLD_QUESTION_PRIMARY,
    RETAINED_ADAPTATIONS,
    REDUNDANT_REMOVED,
)

HERE = Path(__file__).resolve().parent
IST = timezone(timedelta(hours=5, minutes=30))
REQUIRED = [
    "README.md", "REVISION-GUIDE.md", "COVERAGE-LEDGER.md", "MCQ-QUESTIONS.md",
    "MCQ-SOLUTIONS.md", "ANSWER-WRITING-TOOLKIT.md", "PRACTICE-LOG.md",
    "FORMAL-COVERAGE-REVIEW.json", "FORMAL-COVERAGE-AUDIT.json", "MCQ-AUDIT.json",
    "PYQ-DEMAND-AUDIT.json", "PDF-MANIFEST.json", "validate_package.py", "build_package.py",
    "render_pdfs.py", "run_negative_tests.py", "FORMAL-SOURCE-MIRROR.md", "VALIDATION.json",
    "CANONICAL-SOURCE-MIRROR.md", ".gitattributes",
    "mcq_bank.py",
    "source-snapshots/formal-session.md", "source-snapshots/formal-workbook.md",
    "source-snapshots/canonical-owner.md", "source-snapshots/pyq-2018-2025.md",
    "source-snapshots/pyq-2026.md",
    "pdf/Schools-of-Buddhism-Revision-Guide.pdf", "pdf/Schools-of-Buddhism-MCQ-Questions.pdf",
    "pdf/Schools-of-Buddhism-MCQ-Solutions.pdf", "pdf/Schools-of-Buddhism-Answer-Writing-Toolkit.pdf",
]
EXPECTED_HASHES = {
    "formal_session": "9a0e5593fcba75966b2c3a57fe64402b4a6c0854dfeb3dce3463dc11e5ac5483",
    "formal_workbook": "1d99dabae0aa18be505764b1e72171cd2e2d6547a5da617889d4b493d3bf4fd1",
    "canonical": "0f405f2bcdcae0228194be9219a05946f38b151af5f457b887208e5a6dae7d12",
    "pyq_2018_2025": "c7b556c7b4b750943b7b5f0ac94273664a46c6c75f1c444ae2d953fd77d34eec",
    "pyq_2026": "1e3b86dbf301bf929851ecc39f1b8585485707cd19fc7a2168861bbb142a8806",
}
EXPECTED_ORIGINAL_PATHS = {
    "formal_session": r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\03-Schools-of-Buddhism\Learning-Session.md",
    "formal_workbook": r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Indian-Philosophy\03-Schools-of-Buddhism\Solved-Practice-Workbook.md",
    "canonical": r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\indian\Buddhism.md",
    "pyq_2018_2025": r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2018-2025.md",
    "pyq_2026": r"C:\up\upsc-ai-kit\knowledge\Philosophy\paper-1\_PYQ-Indian-Philosophy-2026.md",
}
EXPECTED_BYTES = {
    "formal_session": 371530,
    "formal_workbook": 104595,
    "canonical": 88150,
    "pyq_2018_2025": 25796,
    "pyq_2026": 8502,
}
SNAPSHOTS = {
    "formal_session": "source-snapshots/formal-session.md",
    "formal_workbook": "source-snapshots/formal-workbook.md",
    "canonical": "source-snapshots/canonical-owner.md",
    "pyq_2018_2025": "source-snapshots/pyq-2018-2025.md",
    "pyq_2026": "source-snapshots/pyq-2026.md",
}
MAX_PANEL_SEMANTIC_UNIT_CHARS = 512
EXPECTED_SUPPORTING_PYQS = [
    {
        "year": 2018, "question_no": "Q5(d)", "marks": 10,
        "text": "How do the Buddhists and the Nyāya philosophers explain our knowledge of 'the absence of the jar on the table'? Answer in detail.",
        "ownership": "Nyāya–Vaiśeṣika-primary/Buddhism-supporting",
        "status": "fully_solved_outside_primary_numbering", "supporting_id": "S1",
    },
    {
        "year": 2024, "question_no": "Q6(a)", "marks": 20,
        "text": "Differentiate between the Cārvākas’ refutation of self as a transcendental category and the Buddhist rejection of ātmā.",
        "ownership": "Cārvāka-primary/Buddhism-supporting",
        "status": "fully_solved_outside_primary_numbering", "supporting_id": "S2",
    },
    {
        "year": 2025, "question_no": "Q5(b)", "marks": 10,
        "text": "Present an exposition of the debate between Naiyāyikas and Buddhists with reference to the notion of Pramāṇa and Pramāṇaphala.",
        "ownership": "Nyāya–Vaiśeṣika-primary/Buddhism-supporting",
        "status": "fully_solved_outside_primary_numbering", "supporting_id": "S3",
    },
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text_sha(text: str) -> str:
    return hashlib.sha256(text.replace("\r\n", "\n").encode("utf-8")).hexdigest()


for _row in EXPECTED_SUPPORTING_PYQS:
    _row["text_sha256"] = text_sha(_row["text"])


def normalize_proposition(text: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text)).strip()


FINGERPRINT_STOPWORDS = {
    "a", "an", "and", "as", "at", "best", "by", "for", "from", "how", "in", "is",
    "it", "of", "on", "or", "that", "the", "this", "to", "what", "which", "why", "with",
    "answer", "claim", "demand", "question", "statement",
}


def inference_basis(stem: str, correct: str) -> str:
    clean = normalize_proposition(f"{stem} || {correct}").lower()
    clean = re.sub(r"\b(?:19|20)\d{2}\b", " ", clean)
    clean = re.sub(r"\b(?:mcq|pyq|cell)\s*[-:#]?\s*\d+\b", " ", clean)
    clean = re.sub(r"[^\wāīūṛṝḷṅñṭḍṇśṣṃḥ]+", " ", clean, flags=re.UNICODE)
    return normalize_proposition(clean)


def inference_tokens(text: str) -> set[str]:
    return {
        token for token in inference_basis(text, "").split()
        if len(token) > 2 and token not in FINGERPRINT_STOPWORDS
    }


def reconstruct_primary_pyqs(*snapshot_texts: str) -> list[dict]:
    rows = []
    for text in snapshot_texts:
        year = None
        for line in text.splitlines():
            year_match = re.match(r"## (20\d\d)", line)
            if year_match:
                year = int(year_match.group(1))
            match = re.match(
                r"- \*\*((Q\d+\([a-e]\)) · (\d+) marks(?:[^·]*)? · \[Buddhism\]\([^)]+\)):\*\* (.+)",
                line,
            )
            if match:
                wording = match.group(4).split(" 📝 **Printed wording:**", 1)[0].strip()
                rows.append({
                    "year": year,
                    "question_no": match.group(2),
                    "marks": int(match.group(3)),
                    "text": wording,
                    "text_sha256": text_sha(wording),
                    "ownership": "Buddhism-primary",
                    "status": "fully_solved",
                })
    return rows


def parse_pyq_surface(text: str, supporting: bool = False) -> list[dict]:
    if supporting:
        pattern = re.compile(
            r"^#### Supporting cross-topic PYQ (S[1-3]) · (20\d\d) · (Q\d+\([a-e]\)) · "
            r"(\d+) marks · ([^\n]+) · fully solved\n\n"
            r"> \*\*Question, exact verified wording:\*\* (.+)$",
            re.M,
        )
        return [{
            "supporting_id": sid, "year": int(year), "question_no": qno, "marks": int(marks),
            "ownership": ownership.replace(" / ", "/"), "text": wording,
            "status": "fully_solved_outside_primary_numbering", "text_sha256": text_sha(wording),
        } for sid, year, qno, marks, ownership, wording in pattern.findall(text)]
    pattern = re.compile(
        r"^#### Primary PYQ (\d+) · (20\d\d) · (Q\d+\([a-e]\)) · (\d+) marks · "
        r"Buddhism · fully solved\n\n"
        r"> \*\*Question, exact verified wording:\*\* (.+)$",
        re.M,
    )
    return [{
        "number": int(number), "year": int(year), "question_no": qno, "marks": int(marks),
        "text": wording, "text_sha256": text_sha(wording),
        "ownership": "Buddhism-primary", "status": "fully_solved",
    } for number, year, qno, marks, wording in pattern.findall(text)]


def slug(text: str) -> str:
    value = re.sub(r"<[^>]+>", "", text).lower()
    value = re.sub(r"[^\w]+", "-", value, flags=re.UNICODE).strip("-")
    return value[:76] or "block"


def reconstruct_blocks(text: str, prefix: str) -> list[dict]:
    lines = text.splitlines()
    heads = []
    for i, line in enumerate(lines):
        match = re.match(r"^(#{2,5})\s+(.+?)\s*$", line)
        if match:
            heads.append((i, len(match.group(1)), match.group(2)))
    blocks = []
    if heads and heads[0][0] > 0:
        payload = "\n".join(lines[:heads[0][0]]).strip() + "\n"
        blocks.append({
            "id": f"{prefix}-document-prelude-000-{text_sha(payload)[:10]}",
            "source": prefix, "ordinal": 0, "level": 1, "heading": "DOCUMENT PRELUDE",
            "line_start": 1, "line_end": heads[0][0],
            "own_payload_sha256": text_sha(payload), "subtree_sha256": text_sha(payload),
            "own_chars": len(payload), "large_leaf_segments": [],
            "direct_children": [], "child_union_sha256": text_sha(""),
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
        segments = []
        if len(own) > 2400:
            for index, offset in enumerate(range(0, len(own), 1800), 1):
                chunk = own[offset:offset + 1800]
                segments.append({
                    "index": index, "start_char": offset,
                    "end_char_exclusive": offset + len(chunk),
                    "payload_sha256": text_sha(chunk), "chars": len(chunk),
                })
        blocks.append({
            "id": f"{prefix}-{slug(heading)}-{n + 1:03d}-{text_sha(own)[:10]}",
            "source": prefix, "ordinal": n + 1, "level": level, "heading": heading,
            "line_start": start + 1, "line_end": own_end,
            "own_payload_sha256": text_sha(own), "subtree_sha256": text_sha(subtree),
            "own_chars": len(own), "large_leaf_segments": segments,
        })
    headings = [block for block in blocks if block["ordinal"] > 0]
    for block in headings:
        children = []
        child_hashes = []
        for child in headings[block["ordinal"]:]:
            if child["level"] <= block["level"]:
                break
            if child["level"] == block["level"] + 1:
                children.append(child["id"])
                child_hashes.append(child["own_payload_sha256"])
        block["direct_children"] = children
        block["child_union_sha256"] = text_sha("\n".join(child_hashes))
    return blocks


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
            "raw_payload_sha256": text_sha(raw),
            "normalized_payload": normalized,
            "normalized_payload_sha256": text_sha(normalized),
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
            navigation = is_navigation_label(raw)
            add_unit(start, i, "navigation_label" if navigation else "substantive_list_item",
                     "excluded_structural" if navigation else "proposition")
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
            navigation = is_navigation_label(raw)
            add_unit(start, i, "navigation_label" if navigation else "prose_paragraph",
                     "excluded_structural" if navigation else "proposition")
    return units


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
        first_option = re.search(r"^[A-D]\.\s+", ch, re.M)
        stem = ch[m.end():first_option.start()].strip() if first_option else ""
        for om in re.finditer(r"^([A-D])\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:|\n<a id=|\n## |\Z)", ch, re.M | re.S):
            opts[om.group(1)] = re.sub(r"\s+", " ", om.group(2).strip())
        ans = re.search(r"\*\*Answer:\s*([A-D])\.\*\*", ch)
        trap = re.search(r"\*\*Examiner trap:\*\*\s*(.+)$", ch, re.M)
        exps = {}
        for em in re.finditer(r"^- \*\*([A-D]):\*\*\s*(.+)$", ch, re.M):
            exps[em.group(1)] = em.group(2).strip()
        out[int(m.group(1))] = {
            "title": m.group(2).strip(), "stem": re.sub(r"\s+", " ", stem),
            "options": opts, "answer": ans.group(1) if ans else None, "explanations": exps,
            "trap": trap.group(1).strip() if trap else "",
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
        expected_snapshot = SNAPSHOTS[key]
        declared_snapshot = source.get("local_snapshot", "")
        source_path = root / expected_snapshot
        if source.get("path") != EXPECTED_ORIGINAL_PATHS[key]:
            fail(errors, "SOURCE_ORIGINAL_PATH_MISMATCH", f"{key}: {source.get('path')!r}")
        if source.get("bytes") != EXPECTED_BYTES[key]:
            fail(errors, "SOURCE_BYTE_LENGTH_MISMATCH", f"{key}: declared {source.get('bytes')} != {EXPECTED_BYTES[key]}")
        if declared != expected:
            fail(errors, "SOURCE_HASH_MISMATCH", f"{key}: declared {declared} != {expected}")
        if declared_snapshot != expected_snapshot:
            fail(errors, "SOURCE_SNAPSHOT_PATH_MISMATCH", f"{key}: {declared_snapshot} != {expected_snapshot}")
        if not source_path.is_file():
            fail(errors, "SOURCE_SNAPSHOT_MISSING", f"{key}: {source_path}")
            continue
        actual = sha(source_path)
        if actual != expected:
            fail(errors, "SOURCE_SNAPSHOT_HASH_MISMATCH", f"{key}: actual {actual} != {expected}")
        if source_path.stat().st_size != EXPECTED_BYTES[key]:
            fail(errors, "SOURCE_SNAPSHOT_BYTE_LENGTH_MISMATCH",
                 f"{key}: actual {source_path.stat().st_size} != {EXPECTED_BYTES[key]}")
        source_texts[key] = source_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    decisions = review.get("decisions", [])
    catalog = review.get("proposition_catalog", {})
    raw_mappings = review.get("raw_proposition_mappings", [])
    excluded_coordinates = review.get("excluded_structural_coordinates", [])
    accounting = review.get("proposition_accounting", {})
    excluded_accounting = review.get("excluded_structural_accounting", {})
    if review.get("decision_count") != len(decisions) or review.get("unclassified_count") != 0:
        fail(errors, "FORMAL_MAPPING_COUNT", "Decision count or unclassified count is invalid")
    mappings_by_block = {}
    for mapping in raw_mappings:
        mappings_by_block.setdefault(mapping.get("source_block_id"), []).append(mapping)
    excluded_by_block = {}
    for coordinate in excluded_coordinates:
        excluded_by_block.setdefault(coordinate.get("source_block_id"), []).append(coordinate)
    decision_by_id = {d.get("id"): d for d in decisions}
    reconstructed_blocks = (
        reconstruct_blocks(source_texts.get("formal_session", ""), "session")
        + reconstruct_blocks(source_texts.get("formal_workbook", ""), "workbook")
    )
    reconstructed_by_id = {block["id"]: block for block in reconstructed_blocks}
    if len(decision_by_id) != len(decisions) or set(decision_by_id) != set(reconstructed_by_id):
        fail(errors, "SOURCE_BLOCK_RECONSTRUCTION_SET", "Ledger block IDs differ from independently reconstructed source blocks")
    if len(decisions) != len(reconstructed_blocks):
        fail(errors, "SOURCE_BLOCK_RECONSTRUCTION_COUNT", f"ledger={len(decisions)} reconstructed={len(reconstructed_blocks)}")
    destinations = {}
    reconstructed_structural_proposition_ids = set()
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
        rebuilt = reconstructed_by_id.get(d.get("id"))
        structural_fields = (
            "source", "ordinal", "level", "heading", "line_start", "line_end",
            "own_payload_sha256", "subtree_sha256", "own_chars",
            "large_leaf_segments", "direct_children", "child_union_sha256",
        )
        if rebuilt is not None:
            for field in structural_fields:
                if d.get(field) != rebuilt.get(field):
                    fail(errors, "SOURCE_STRUCTURE_RECONSTRUCTION_MISMATCH", f"{d.get('id')}:{field}")
        dest = d.get("destination", {})
        f = dest.get("file", "")
        if f not in destinations and (root / f).is_file():
            destinations[f] = (root / f).read_text(encoding="utf-8").replace("\r\n", "\n")
        payload = anchor_payload(destinations.get(f, ""), dest.get("anchor", ""))
        if payload is None:
            fail(errors, "DESTINATION_ANCHOR_MISSING", d.get("id", "unknown"))
        elif text_sha(payload) != dest.get("payload_sha256"):
            fail(errors, "DESTINATION_PAYLOAD_HASH_MISMATCH", d.get("id", "unknown"))
        reconstructed_units = semantic_units(source_payload, d)
        expected_units = [unit for unit in reconstructed_units if unit["classification"] == "proposition"]
        expected_structural = [unit for unit in reconstructed_units if unit["classification"] == "excluded_structural"]
        reconstructed_structural_proposition_ids.update(
            f"prop-{unit['normalized_payload_sha256'][:20]}" for unit in expected_structural
        )
        mappings = sorted(mappings_by_block.get(d.get("id"), []), key=lambda row: row.get("occurrence_index", 0))
        structural_rows = sorted(
            excluded_by_block.get(d.get("id"), []), key=lambda row: row.get("coordinate_index", 0)
        )
        expected_ids = []
        if "```" in source_payload:
            expected_panel_units = [
                unit for unit in expected_units
                if unit["segment_type"] == "diagram_text_row"
            ]
            mapped_panel_units = [
                mapping for mapping in mappings
                if mapping.get("segment_type") == "diagram_text_row"
            ]
            if (not expected_panel_units
                    or [(m.get("segment_type"), m.get("relative_line_start"), m.get("relative_line_end"))
                        for m in mapped_panel_units]
                    != [(u["segment_type"], u["relative_line_start"], u["relative_line_end"])
                        for u in expected_panel_units]):
                fail(errors, "PANEL_SEMANTIC_UNIT_STRUCTURE", d.get("id", "unknown"))
            for unit in expected_panel_units:
                if (unit["relative_line_start"] != unit["relative_line_end"]
                        or len(unit["normalized_payload"]) > MAX_PANEL_SEMANTIC_UNIT_CHARS):
                    fail(errors, "PANEL_SEMANTIC_UNIT_SIZE", d.get("id", "unknown"))
        structural_spans = {
            (unit["relative_line_start"], unit["relative_line_end"])
            for unit in expected_structural
        }
        if any(
            mapping.get("segment_type") in STRUCTURAL_UNIT_TYPES
            or (mapping.get("relative_line_start"), mapping.get("relative_line_end")) in structural_spans
            for mapping in mappings
        ):
            fail(errors, "STRUCTURAL_UNIT_AS_PROPOSITION", d.get("id", "unknown"))
        if len(mappings) != len(expected_units):
            fail(errors, "PROPOSITION_RAW_MAPPING_COUNT", f"{d.get('id')}: mappings={len(mappings)} units={len(expected_units)}")
        for index, unit in enumerate(expected_units, 1):
            expected_prop_id = f"prop-{unit['normalized_payload_sha256'][:20]}"
            if expected_prop_id not in expected_ids:
                expected_ids.append(expected_prop_id)
            if index > len(mappings):
                continue
            mapping = mappings[index - 1]
            expected_mapping = {
                "mapping_id": f"map-{d.get('id')}-{index:03d}",
                "source_block_id": d.get("id"),
                "source_key": source_key,
                "occurrence_index": index,
                "segment_type": unit["segment_type"],
                "relative_line_start": unit["relative_line_start"],
                "relative_line_end": unit["relative_line_end"],
                "absolute_line_start": unit["absolute_line_start"],
                "absolute_line_end": unit["absolute_line_end"],
                "raw_payload_sha256": unit["raw_payload_sha256"],
                "proposition_id": expected_prop_id,
                "normalized_payload_sha256": unit["normalized_payload_sha256"],
            }
            if mapping != expected_mapping:
                fail(errors, "PROPOSITION_OCCURRENCE_MISMATCH", expected_mapping["mapping_id"])
            proposition = catalog.get(expected_prop_id)
            if (not proposition
                    or proposition.get("id") != expected_prop_id
                    or proposition.get("normalized_semantic_payload") != unit["normalized_payload"]
                    or proposition.get("normalized_payload_sha256") != unit["normalized_payload_sha256"]):
                fail(errors, "PROPOSITION_CATALOG_MISMATCH", expected_mapping["mapping_id"])
        if d.get("proposition_ids") != expected_ids:
            fail(errors, "DECISION_PROPOSITION_COVERAGE", d.get("id", "unknown"))
        if d.get("semantic_basis") != "only_deterministic_source_authored_proposition_bearing_units_normalized_and_globally_deduplicated;structural_units_excluded_separately":
            fail(errors, "SEMANTIC_PROPOSITION_QUALITY", d.get("id", "unknown"))
        if len(structural_rows) != len(expected_structural):
            fail(errors, "EXCLUDED_STRUCTURAL_COUNT_MISMATCH",
                 f"{d.get('id')}: rows={len(structural_rows)} units={len(expected_structural)}")
        for index, unit in enumerate(expected_structural, 1):
            if index > len(structural_rows):
                continue
            structural_type = unit["segment_type"]
            coordinate_basis = (
                f"{d.get('id')}|{unit['relative_line_start']}|{unit['relative_line_end']}|"
                f"{structural_type}|{unit['raw_payload_sha256']}"
            )
            expected_row = {
                "coordinate_id": f"struct-{text_sha(coordinate_basis)[:24]}",
                "source_block_id": d.get("id"),
                "source_key": source_key,
                "coordinate_index": index,
                "segment_type": structural_type,
                "relative_line_start": unit["relative_line_start"],
                "relative_line_end": unit["relative_line_end"],
                "absolute_line_start": unit["absolute_line_start"],
                "absolute_line_end": unit["absolute_line_end"],
                "structural_category": STRUCTURAL_CATEGORIES[structural_type],
                "structural_type": structural_type,
                "raw_payload_sha256": unit["raw_payload_sha256"],
            }
            if structural_rows[index - 1] != expected_row:
                actual = structural_rows[index - 1]
                if actual.get("structural_type") != structural_type:
                    fail(errors, "EXCLUDED_STRUCTURAL_TYPE_MISMATCH", expected_row["coordinate_id"])
                elif actual.get("raw_payload_sha256") != unit["raw_payload_sha256"]:
                    fail(errors, "EXCLUDED_STRUCTURAL_HASH_MISMATCH", expected_row["coordinate_id"])
                else:
                    fail(errors, "EXCLUDED_STRUCTURAL_COORDINATE_MISMATCH", expected_row["coordinate_id"])
        classified_lines = []
        for row in [*mappings, *structural_rows]:
            start = row.get("relative_line_start")
            end = row.get("relative_line_end")
            if isinstance(start, int) and isinstance(end, int) and start <= end:
                classified_lines.extend(range(start, end + 1))
        expected_lines = list(range(1, len(source_payload.rstrip("\n").splitlines()) + 1))
        if sorted(classified_lines) != expected_lines or len(classified_lines) != len(set(classified_lines)):
            fail(errors, "SOURCE_COORDINATE_CLASSIFICATION_PARTITION", d.get("id", "unknown"))
        segments = d.get("large_leaf_segments", [])
        if d.get("own_chars") != len(source_payload):
            fail(errors, "SOURCE_BLOCK_LENGTH_MISMATCH", d.get("id", "unknown"))
        if len(source_payload) > 2400 and not segments:
            fail(errors, "LARGE_LEAF_UNSEGMENTED", d.get("id", "unknown"))
        if segments:
            reconstructed_chunks = []
            for segment in segments:
                start = segment.get("start_char")
                end = segment.get("end_char_exclusive")
                if not isinstance(start, int) or not isinstance(end, int) or not 0 <= start < end <= len(source_payload):
                    fail(errors, "LARGE_LEAF_SEGMENT_RANGE", d.get("id", "unknown"))
                    continue
                chunk = source_payload[start:end]
                reconstructed_chunks.append(chunk)
                if len(chunk) != segment.get("chars") or text_sha(chunk) != segment.get("payload_sha256"):
                    fail(errors, "LARGE_LEAF_SEGMENT_HASH", f"{d.get('id', 'unknown')}:{segment.get('index')}")
            if "".join(reconstructed_chunks) != source_payload:
                fail(errors, "LARGE_LEAF_SEGMENT_UNION", d.get("id", "unknown"))
    for source_key, prefix in (("formal_session", "session"), ("formal_workbook", "workbook")):
        source_decisions = sorted(
            (d for d in decisions if d.get("source") == prefix),
            key=lambda row: row.get("line_start", 0),
        )
        rebuilt_text = "\n".join(
            "\n".join(source_texts[source_key].splitlines()[d["line_start"] - 1:d["line_end"]])
            for d in source_decisions
        ).strip() + "\n"
        if rebuilt_text != source_texts[source_key].strip() + "\n":
            fail(errors, "SOURCE_BLOCK_UNION_INCOMPLETE", source_key)
        covered_lines = [line for d in source_decisions for line in range(d["line_start"], d["line_end"] + 1)]
        if covered_lines != list(range(1, len(source_texts[source_key].splitlines()) + 1)):
            fail(errors, "SOURCE_LINE_COVERAGE_GAP", source_key)
    if audit.get("review_sha256") != sha(root / "FORMAL-COVERAGE-REVIEW.json"):
        fail(errors, "DERIVED_AUDIT_STALE", "Review hash differs")
    if audit.get("decision_count") != len(decisions) or audit.get("unclassified") != 0:
        fail(errors, "DERIVED_AUDIT_COUNT", "Derived counts differ")
    unique_ids = {m.get("proposition_id") for m in raw_mappings}
    mapping_ids = [m.get("mapping_id") for m in raw_mappings]
    catalog_hash = text_sha(json.dumps(catalog, ensure_ascii=False, sort_keys=True))
    mappings_hash = text_sha(json.dumps(raw_mappings, ensure_ascii=False, sort_keys=True))
    if (accounting.get("raw_mapping_count") != len(raw_mappings)
            or accounting.get("unique_normalized_proposition_count") != len(unique_ids)
            or len(catalog) != len(unique_ids)
            or accounting.get("duplicate_raw_mapping_count") != len(raw_mappings) - len(unique_ids)):
        fail(errors, "PROPOSITION_ACCOUNTING_MISMATCH", "Raw and unique proposition counts are inconsistent")
    if set(catalog) != unique_ids or len(mapping_ids) != len(set(mapping_ids)):
        fail(errors, "PROPOSITION_CATALOG_OCCURRENCE_SET", "Catalog keys or occurrence IDs are inconsistent")
    if set(catalog) & reconstructed_structural_proposition_ids:
        fail(errors, "STRUCTURAL_UNIT_AS_PROPOSITION", "Catalog contains a reconstructed structural payload")
    for proposition_id, proposition in catalog.items():
        normalized = proposition.get("normalized_semantic_payload", "")
        normalized_hash = text_sha(normalized)
        if (proposition_id != f"prop-{normalized_hash[:20]}"
                or proposition.get("id") != proposition_id
                or proposition.get("normalized_payload_sha256") != normalized_hash):
            fail(errors, "PROPOSITION_CATALOG_HASH", proposition_id)
    if accounting.get("catalog_sha256") != catalog_hash or accounting.get("raw_mappings_sha256") != mappings_hash:
        fail(errors, "PROPOSITION_ACCOUNTING_HASH", "Catalog or raw mapping hash differs")
    if (audit.get("raw_proposition_mappings") != len(raw_mappings)
            or audit.get("unique_normalized_semantic_propositions") != len(unique_ids)
            or audit.get("proposition_catalog_sha256") != catalog_hash
            or audit.get("raw_mappings_sha256") != mappings_hash):
        fail(errors, "PROPOSITION_AUDIT_STALE", "Derived proposition accounting differs")
    structural_type_counts = {
        unit_type: sum(row.get("structural_type") == unit_type for row in excluded_coordinates)
        for unit_type in sorted(STRUCTURAL_UNIT_TYPES)
    }
    structural_category_counts = {
        category: sum(row.get("structural_category") == category for row in excluded_coordinates)
        for category in sorted(set(STRUCTURAL_CATEGORIES.values()))
    }
    excluded_hash = text_sha(json.dumps(excluded_coordinates, ensure_ascii=False, sort_keys=True))
    if (excluded_accounting.get("total_excluded") != len(excluded_coordinates)
            or excluded_accounting.get("per_category") != structural_category_counts
            or excluded_accounting.get("per_type") != structural_type_counts):
        fail(errors, "EXCLUDED_STRUCTURAL_ACCOUNTING_MISMATCH", "Excluded structural counts differ")
    if excluded_accounting.get("coordinates_sha256") != excluded_hash:
        fail(errors, "EXCLUDED_STRUCTURAL_ACCOUNTING_HASH", "Excluded structural coordinate hash differs")
    if (audit.get("excluded_structural_coordinates") != len(excluded_coordinates)
            or audit.get("excluded_structural_per_category") != structural_category_counts
            or audit.get("excluded_structural_per_type") != structural_type_counts
            or audit.get("excluded_structural_coordinates_sha256") != excluded_hash):
        fail(errors, "EXCLUDED_STRUCTURAL_AUDIT_STALE", "Derived excluded structural accounting differs")
    panels = []
    panel_numbers = []
    for block in reconstructed_blocks:
        match = re.search(r"ASCII MASTER FLOW — PANEL (\d+)/(\d+)", block.get("heading", ""))
        if match:
            panels.append(block)
            panel_numbers.append((int(match.group(1)), int(match.group(2))))
    expected_panel_ids = [panel["id"] for panel in panels]
    panel_parity = review.get("panel_parity", {})
    if (panel_numbers != [(i, 14) for i in range(1, 15)]
            or panel_parity.get("expected") != 14
            or panel_parity.get("actual") != 14
            or panel_parity.get("panel_ids") != expected_panel_ids):
        fail(errors, "PANEL_RECONSTRUCTION_MISMATCH", json.dumps(panel_numbers))
    mappings_by_id = {row.get("mapping_id"): row for row in raw_mappings}

    def sample(category: str, mapping: dict, target: str) -> dict:
        basis = f"{category}|{target}|{mapping['mapping_id']}|{mapping['proposition_id']}"
        return {
            "sample_id": f"sample-{text_sha(basis)[:24]}",
            "category": category,
            "target": target,
            "mapping_id": mapping["mapping_id"],
            "proposition_id": mapping["proposition_id"],
            "source_block_id": mapping["source_block_id"],
            "normalized_payload_sha256": mapping["normalized_payload_sha256"],
        }

    expected_samples = []
    if raw_mappings:
        for label, index in (("beginning", 0), ("middle", len(raw_mappings) // 2), ("end", -1)):
            expected_samples.append(sample("corpus_position", raw_mappings[index], label))
    for decision in decisions:
        block_mappings = sorted(
            mappings_by_block.get(decision.get("id"), []), key=lambda row: row.get("occurrence_index", 0)
        )
        if decision.get("direct_children") and block_mappings:
            expected_samples.append(sample("parent_block", block_mappings[0], decision["id"]))
        if decision.get("large_leaf_segments") and block_mappings:
            expected_samples.append(sample("large_leaf", block_mappings[len(block_mappings) // 2], decision["id"]))
    for panel in panels:
        panel_mappings = sorted(
            (
                row for row in mappings_by_block.get(panel["id"], [])
                if row.get("segment_type") == "diagram_text_row"
            ),
            key=lambda row: row.get("occurrence_index", 0),
        )
        if not panel_mappings:
            fail(errors, "MEANINGFUL_SAMPLE_PANEL_MISSING", panel["id"])
            continue
        expected_samples.append(sample("panel", panel_mappings[0], panel["id"]))
    sample_section = review.get("meaningful_proposition_verification", {})
    actual_samples = sample_section.get("samples", [])
    sample_counts = {
        category: sum(row["category"] == category for row in expected_samples)
        for category in ("corpus_position", "parent_block", "large_leaf", "panel")
    }
    samples_hash = text_sha(json.dumps(expected_samples, ensure_ascii=False, sort_keys=True))
    if actual_samples != expected_samples:
        fail(errors, "MEANINGFUL_PROPOSITION_SAMPLE_MISMATCH", "Samples differ from independent derivation")
    if (sample_section.get("sample_count") != len(expected_samples)
            or sample_section.get("per_category") != sample_counts
            or sample_section.get("samples_sha256") != samples_hash):
        fail(errors, "MEANINGFUL_PROPOSITION_SAMPLE_ACCOUNTING", "Sample count/category/hash differs")
    for row in actual_samples:
        mapping = mappings_by_id.get(row.get("mapping_id"))
        if (not mapping or mapping.get("proposition_id") != row.get("proposition_id")
                or mapping.get("segment_type") not in PROPOSITION_UNIT_TYPES
                or row.get("proposition_id") not in catalog):
            fail(errors, "MEANINGFUL_SAMPLE_NOT_PROPOSITION", row.get("sample_id", "unknown"))
    if (audit.get("meaningful_proposition_samples") != len(expected_samples)
            or audit.get("meaningful_sample_categories") != sample_counts
            or audit.get("meaningful_samples_sha256") != samples_hash
            or audit.get("meaningful_samples") != expected_samples):
        fail(errors, "MEANINGFUL_PROPOSITION_SAMPLE_AUDIT_STALE", "Derived sample evidence differs")
    canonical_mirror = (root / "CANONICAL-SOURCE-MIRROR.md").read_text(encoding="utf-8")
    canonical_payload = canonical_mirror.split("\n\n", 2)[-1]
    if canonical_payload.replace("\r\n", "\n").rstrip() + "\n" != source_texts.get("canonical", "").rstrip() + "\n":
        fail(errors, "CANONICAL_MIRROR_MISMATCH", "Canonical mirror does not exactly preserve the owner")
    checks["formal_blocks"] = len(decisions)
    checks["raw_proposition_mappings"] = len(raw_mappings)
    checks["unique_normalized_propositions"] = len(unique_ids)
    checks["deduplicated_repetitions"] = len(raw_mappings) - len(unique_ids)
    checks["excluded_structural_coordinates"] = len(excluded_coordinates)
    checks["excluded_structural_per_category"] = structural_category_counts
    checks["meaningful_proposition_samples"] = len(expected_samples)
    checks["meaningful_sample_categories"] = sample_counts
    checks["panels"] = len(panels)

    revision = (root / "REVISION-GUIDE.md").read_text(encoding="utf-8")
    toolkit = (root / "ANSWER-WRITING-TOOLKIT.md").read_text(encoding="utf-8")
    doctrine_terms = [
        ("Four Noble Truths", "DOCTRINE_FOUR_TRUTHS"), ("pratītyasamutpāda", "DOCTRINE_DEPENDENT_ORIGINATION"),
        ("kṣaṇikavāda", "DOCTRINE_MOMENTARINESS"), ("nairātmyavāda", "DOCTRINE_NO_SELF"),
        ("causal continuum", "DOCTRINE_CONTINUITY"), ("Vaibhāṣika", "DOCTRINE_VAIBHASIKA"),
        ("Sautrāntika", "DOCTRINE_SAUTRANTIKA"), ("Yogācāra", "DOCTRINE_YOGACARA"),
        ("Mādhyamika", "DOCTRINE_MADHYAMAKA"), ("two truths", "DOCTRINE_TWO_TRUTHS"),
        ("apoha", "DOCTRINE_APOHA"), ("nirvāṇa", "DOCTRINE_NIRVANA"),
        ("perception", "DOCTRINE_PRAMANA"), ("inference", "DOCTRINE_PRAMANA_INFERENCE"),
    ]
    low = revision.lower()
    for term, code in doctrine_terms:
        if term.lower() not in low:
            fail(errors, code, term)
    forbidden = [
        r"(?:śūnyatā|sunyata|emptiness) (?:is|means) (?:sheer )?(?:nothingness|nihilism|non-being)",
        r"(?:vijñaptimātra|vijnaptimatra|consciousness-only) (?:is|means) (?:private )?(?:fantasy|solipsism|subjective idealism)",
        r"dependent origination is (?:a )?simple linear causation",
        r"store-consciousness is (?:an|the) (?:eternal|permanent) self",
    ]
    for pat in forbidden:
        if re.search(pat, revision, re.I):
            fail(errors, "DOCTRINE_GUARDRAIL", pat)
    stale_primary_count = re.compile(
        r"(?im)^.{0,180}(?:(?:\b13\b|\bthirteen\b).{0,100}"
        r"(?:primary-owned|owned PYQs|primary PYQs|PYQs)|"
        r"(?:primary-owned|owned PYQs|primary PYQs).{0,100}"
        r"(?:\b13\b|\bthirteen\b)).{0,180}$"
    )
    for surface_name, surface in (("REVISION-GUIDE.md", revision), ("ANSWER-WRITING-TOOLKIT.md", toolkit)):
        for match in stale_primary_count.finditer(surface):
            fail(errors, "LEARNER_PYQ_COUNT_STALE", f"{surface_name}: {match.group(0).strip()}")
    if "| Directly owned verified PYQs solved in full | 14 |" not in revision:
        fail(errors, "LEARNER_PYQ_COUNT_STALE", "summary table does not state 14 primary PYQs")
    rail = re.search(r"^PYQ ANCHORS\s+.*?(?=^ROUTED\s+)", revision, re.M | re.S)
    if (not rail or "2026 Q5(b)" not in rail.group(0)
            or "[14 primary-owned]" not in rail.group(0)
            or "[13 primary-owned]" in rail.group(0)):
        fail(errors, "LEARNER_PYQ_RAIL_STALE", "Final PYQ rail must enumerate 2026 Q5(b) and state 14 primary-owned")
    checks["doctrine_guardrails"] = len(doctrine_terms)

    q = parse_mcq_surface((root / "MCQ-QUESTIONS.md").read_text(encoding="utf-8"))
    s = parse_mcq_surface((root / "MCQ-SOLUTIONS.md").read_text(encoding="utf-8"))
    ma = json.loads((root / "MCQ-AUDIT.json").read_text(encoding="utf-8"))
    from build_package import authored_mcqs, parse_mcqs
    authored_items = authored_mcqs(parse_mcqs(source_texts.get("formal_workbook", "")))
    expected_count = len(OLD_QUESTION_PRIMARY) + len(NEW_QUESTIONS) + len(EXTRA_PROBES)
    expected_ids = [f"BUD-MCQ-{number:03d}" for number in range(1, expected_count + 1)]
    expected_cells = {row["id"]: row for row in CELL_MATRIX}
    if len(q) != expected_count or len(s) != expected_count or ma.get("derivation", {}).get("question_count") != expected_count:
        fail(errors, "MCQ_COUNT_MISMATCH", f"questions={len(q)} solutions={len(s)}")
    if sorted(q) != list(range(1, expected_count + 1)) or sorted(s) != list(range(1, expected_count + 1)):
        fail(errors, "MCQ_NUMBERING", f"Expected contiguous questions 1-{expected_count}")
    seq = []
    correct_lengths, incorrect_lengths, normalized_traps, item_length_metrics = [], [], [], []
    for num in sorted(q):
        if num not in s or q[num]["options"] != s[num]["options"] or q[num]["stem"] != s[num]["stem"]:
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
            rendered_lengths = {letter: len(option.split()) for letter, option in s[num]["options"].items()}
            incorrect_item_lengths = [
                value for letter, value in rendered_lengths.items() if letter != s[num]["answer"]
            ]
            metric = {
                "question_id": f"BUD-MCQ-{num:03d}",
                "correct_words": rendered_lengths[s[num]["answer"]],
                "minimum_option_words": min(rendered_lengths.values()),
                "maximum_option_words": max(rendered_lengths.values()),
                "max_to_min_ratio": round(max(rendered_lengths.values()) / max(1, min(rendered_lengths.values())), 3),
                "correct_to_incorrect_mean_ratio": round(
                    rendered_lengths[s[num]["answer"]] / (sum(incorrect_item_lengths) / 3), 3
                ),
                "maximum_word_disparity": max(rendered_lengths.values()) - min(rendered_lengths.values()),
            }
            item_length_metrics.append(metric)
            if (
                metric["max_to_min_ratio"] > 1.8
                or metric["maximum_word_disparity"] > 12
                or metric["correct_to_incorrect_mean_ratio"] > 1.5
            ):
                fail(errors, "MCQ_ITEM_LENGTH_CUE", f"{num}: {json.dumps(metric, sort_keys=True)}")
            for letter, option in s[num]["options"].items():
                (correct_lengths if letter == s[num]["answer"] else incorrect_lengths).append(len(option.split()))
                explanation = s[num]["explanations"].get(letter, "")
                if letter != s[num]["answer"] and (
                    not explanation.startswith("Incorrect:") or len(explanation.split()) < 5
                ):
                    fail(errors, "MCQ_FALSE_PROPOSITION_EXPLANATION", f"{num}{letter}")
        if not s[num].get("trap"):
            fail(errors, "MCQ_TRAP_MISSING", str(num))
        normalized_traps.append(normalize_proposition(s[num].get("trap", "")).lower())
        endings = {bool(re.search(r"[.!?…][\"')\]]?$", option.strip())) for option in s[num]["options"].values()}
        if len(endings) > 1:
            fail(errors, "MCQ_PUNCTUATION_CUE", str(num))
    if "".join(seq) != ma.get("answer_sequence"):
        fail(errors, "MCQ_AUDIT_SEQUENCE_MISMATCH", "".join(seq))
    actual_counts = {letter: seq.count(letter) for letter in "ABCD"}
    if actual_counts != ma.get("answer_counts"):
        fail(errors, "MCQ_AUDIT_COUNTS_MISMATCH", json.dumps(actual_counts, sort_keys=True))
    if max(actual_counts.values()) - min(actual_counts.values()) > 1:
        fail(errors, "MCQ_POSITION_IMBALANCE", json.dumps(actual_counts, sort_keys=True))
    derivation = ma.get("derivation", {})
    if (
        derivation.get("test_cell_count") != len(CELL_MATRIX)
        or derivation.get("question_count") != expected_count
        or derivation.get("coverage_ratio_definition") != "final_mcq_count / test_cell_count"
        or derivation.get("coverage_ratio") != round(expected_count / len(CELL_MATRIX), 6)
        or derivation.get("uncovered") != 0
        or derivation.get("retained_count") != len(OLD_QUESTION_PRIMARY) - len(RETAINED_ADAPTATIONS)
        or derivation.get("adapted_count") != len(RETAINED_ADAPTATIONS)
        or derivation.get("new_question_count") != len(NEW_QUESTIONS) + len(EXTRA_PROBES)
        or derivation.get("redundant_removed_count") != len(REDUNDANT_REMOVED)
        or derivation.get("redundant_removed") != REDUNDANT_REMOVED
    ):
        fail(errors, "MCQ_AUDIT_COUNT_TAMPER", "MCQ derivation/count fields differ from authored sources")
    expected_category_counts = {
        category: sum(row["category"] == category for row in CELL_MATRIX)
        for category in ("doctrine", "school", "comparison", "criticism", "PYQ", "misconception", "transfer")
    }
    if ma.get("category_counts") != expected_category_counts:
        fail(errors, "MCQ_CATEGORY_COUNTS", "Category totals differ from the authored matrix")
    audit_cells = ma.get("test_cells", [])
    if [row.get("id") for row in audit_cells] != list(expected_cells):
        fail(errors, "MCQ_CELL_IDS", "Cell IDs/order differ from authored stable matrix")
    for row in audit_cells:
        expected = expected_cells.get(row.get("id"))
        if not expected or any(row.get(field) != expected.get(field) for field in ("category", "label")):
            fail(errors, "MCQ_CELL_DEFINITION", row.get("id", "unknown"))
    authored_questions = [{
        "question_id": item["question_id"], "primary_cell": item["primary_cell"],
        "secondary_cells": item.get("secondary_cells", []), "origin": item["origin"],
        **({"source_question": item["source_question"]} if "source_question" in item else {}),
    } for item in authored_items]
    mappings = ma.get("question_mapping", [])
    if [row.get("question_id") for row in mappings] != expected_ids or len(mappings) != expected_count:
        fail(errors, "MCQ_MAPPING_IDS", "Question mapping IDs are not stable and contiguous")
    primary_coverage = {cell_id: [] for cell_id in expected_cells}
    inference_keys, inference_fingerprints, fingerprint_token_sets, stem_hashes = [], [], [], []
    for number, (mapping, expected) in enumerate(zip(mappings, authored_questions), 1):
        authored_item = authored_items[number - 1]
        if (
            mapping.get("number") != number
            or mapping.get("question_id") != expected["question_id"]
            or mapping.get("primary_cell") != expected["primary_cell"]
            or mapping.get("secondary_cells") != expected["secondary_cells"]
            or mapping.get("origin") != expected["origin"]
            or ("source_question" in expected and mapping.get("source_question") != expected["source_question"])
        ):
            fail(errors, "MCQ_MAPPING_INTEGRITY", expected["question_id"])
        mapped_cells = [mapping.get("primary_cell"), *mapping.get("secondary_cells", [])]
        if len(mapped_cells) != len(set(mapped_cells)) or any(cell_id not in expected_cells for cell_id in mapped_cells):
            fail(errors, "MCQ_UNKNOWN_OR_SUPERFICIAL_MAPPING", mapping.get("question_id", "unknown"))
        primary_coverage[mapping.get("primary_cell")].append(mapping.get("question_id"))
        expected_stem_hash = text_sha(normalize_proposition(q.get(number, {}).get("stem", "")).lower())
        if mapping.get("stem_sha256") != expected_stem_hash:
            fail(errors, "MCQ_STEM_AUDIT_MISMATCH", mapping.get("question_id", "unknown"))
        inference_keys.append(normalize_proposition(mapping.get("tested_inference", "")).lower())
        correct_option = authored_item["options"][authored_item["correct_index"]]
        expected_basis = inference_basis(authored_item["stem"], correct_option)
        expected_fingerprint = text_sha(expected_basis)
        evidence = authored_item.get("authored_evidence", {})
        expected_evidence_hash = text_sha(json.dumps(evidence, ensure_ascii=False, sort_keys=True))
        expected_entry_hash = text_sha(json.dumps({
            "title": authored_item["title"], "stem": authored_item["stem"],
            "options": authored_item["options"], "correct_index": authored_item["correct_index"],
            "correct_proposition": authored_item.get("correct_proposition"),
            "rationale": authored_item.get("rationale"),
            "explanations": authored_item["explanations"], "trap": authored_item["trap"],
        }, ensure_ascii=False, sort_keys=True))
        authored_correct = authored_item.get("correct_proposition")
        authored_rationale = authored_item.get("rationale")
        expected_correct_hash = (
            text_sha(normalize_proposition(authored_correct))
            if isinstance(authored_correct, str) and authored_correct.strip() else None
        )
        expected_rationale_hash = (
            text_sha(normalize_proposition(authored_rationale))
            if isinstance(authored_rationale, str) and authored_rationale.strip() else None
        )
        if (
            not authored_correct
            or not authored_rationale
            or correct_option != authored_correct
            or normalize_proposition(authored_correct).lower()
            == normalize_proposition(authored_rationale).lower()
            or authored_item["explanations"][authored_item["correct_index"]]
            != f"Correct: {authored_rationale}"
        ):
            fail(errors, "MCQ_CORRECT_PROPOSITION_CONTRACT", mapping.get("question_id", "unknown"))
        if (
            mapping.get("fingerprint_basis") != expected_basis
            or mapping.get("inference_fingerprint") != expected_fingerprint
        ):
            fail(errors, "MCQ_INFERENCE_FINGERPRINT_MISMATCH", mapping.get("question_id", "unknown"))
        if (
            not evidence.get("tested_operation")
            or not evidence.get("required_option_distinction")
            or mapping.get("authored_evidence") != evidence
            or mapping.get("authored_evidence_sha256") != expected_evidence_hash
            or mapping.get("authored_correct_proposition") != authored_correct
            or mapping.get("authored_correct_proposition_sha256") != expected_correct_hash
            or mapping.get("authored_rationale") != authored_rationale
            or mapping.get("authored_rationale_sha256") != expected_rationale_hash
            or mapping.get("authored_entry_sha256") != expected_entry_hash
        ):
            fail(errors, "MCQ_MAPPING_EVIDENCE_MISMATCH", mapping.get("question_id", "unknown"))
        rendered_options = list(q.get(number, {}).get("options", {}).values())
        rendered_answer = s.get(number, {}).get("answer")
        rendered_correct = s.get(number, {}).get("options", {}).get(rendered_answer, "")
        if (
            q.get(number, {}).get("title") != authored_item["title"]
            or q.get(number, {}).get("stem") != normalize_proposition(authored_item["stem"])
            or sorted(rendered_options) != sorted(authored_item["options"])
            or rendered_correct != authored_correct
            or text_sha(normalize_proposition(rendered_correct)) != expected_correct_hash
            or s.get(number, {}).get("trap") != authored_item["trap"]
        ):
            fail(errors, "MCQ_AUTHORED_RENDER_MISMATCH", mapping.get("question_id", "unknown"))
        expected_explanations = {
            option: explanation
            for option, explanation in zip(authored_item["options"], authored_item["explanations"])
        }
        for letter, option in s.get(number, {}).get("options", {}).items():
            if s[number]["explanations"].get(letter) != expected_explanations.get(option):
                fail(errors, "MCQ_AUTHORED_EXPLANATION_MISMATCH", f"{number}{letter}")
        rendered_basis = inference_basis(
            q.get(number, {}).get("stem", ""),
            rendered_correct,
        )
        inference_fingerprints.append(text_sha(rendered_basis))
        fingerprint_token_sets.append(inference_tokens(rendered_basis))
        stem_hashes.append(mapping.get("stem_sha256"))
    uncovered = sorted(cell_id for cell_id, ids in primary_coverage.items() if not ids)
    if uncovered:
        fail(errors, "MCQ_UNCOVERED_CELL", ", ".join(uncovered))
    audit_cell_questions = {row.get("id"): row.get("linked_question_ids", []) for row in audit_cells}
    audit_primary_questions = {row.get("id"): row.get("primary_question_ids", []) for row in audit_cells}
    expected_cell_questions = {cell_id: [] for cell_id in expected_cells}
    for mapping in mappings:
        for cell_id in [mapping.get("primary_cell"), *mapping.get("secondary_cells", [])]:
            if cell_id in expected_cell_questions:
                expected_cell_questions[cell_id].append(mapping.get("question_id"))
    if audit_cell_questions != expected_cell_questions:
        fail(errors, "MCQ_CELL_QUESTION_MAP", "Per-cell question lists differ from question mappings")
    if audit_primary_questions != primary_coverage:
        fail(errors, "MCQ_PRIMARY_CELL_QUESTION_MAP", "Per-cell primary lists differ from mappings")
    if len(stem_hashes) != len(set(stem_hashes)):
        fail(errors, "MCQ_DUPLICATE_STEM", "Normalized MCQ stems are not unique")
    if len(inference_keys) != len(set(inference_keys)) or any(not key for key in inference_keys):
        fail(errors, "MCQ_DUPLICATE_PRIMARY_INFERENCE", "Tested-inference keys are empty or duplicated")
    if len(inference_fingerprints) != len(set(inference_fingerprints)):
        fail(errors, "MCQ_DUPLICATE_INFERENCE_FINGERPRINT", "Normalized stem-plus-answer fingerprints are duplicated")
    for left in range(len(fingerprint_token_sets)):
        for right in range(left + 1, len(fingerprint_token_sets)):
            a, b = fingerprint_token_sets[left], fingerprint_token_sets[right]
            union = a | b
            similarity = len(a & b) / len(union) if union else 1.0
            if len(a & b) >= 8 and similarity >= 0.82:
                fail(errors, "MCQ_NEAR_DUPLICATE_INFERENCE",
                     f"{left + 1}/{right + 1}: token_jaccard={similarity:.3f}")
    declared_extra = ma.get("extra_probes", [])
    expected_extra = [{
        "question_id": item["question_id"], "cell_id": item["primary_cell"],
        "risk_rationale": EXTRA_PROBE_RATIONALES[item["primary_cell"]],
    } for item in EXTRA_PROBES]
    if declared_extra != expected_extra:
        fail(errors, "MCQ_EXTRA_PROBE_DECLARATION", "Declared probes or rationales differ from authored source")
    if expected_count != len(CELL_MATRIX) + len(EXTRA_PROBES):
        fail(errors, "MCQ_COUNT_DERIVATION", "Question count does not equal cells plus declared extras")
    declared_extra_cells = set(EXTRA_PROBE_RATIONALES)
    for cell_id, primary_ids in primary_coverage.items():
        expected_multiplicity = 2 if cell_id in declared_extra_cells else 1
        if len(primary_ids) != expected_multiplicity:
            fail(errors, "MCQ_PRIMARY_MULTIPLICITY", f"{cell_id}: {len(primary_ids)}")
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
    if len(normalized_traps) != len(set(normalized_traps)) or any(not trap for trap in normalized_traps):
        fail(errors, "MCQ_TRAP_DUPLICATE", "Examiner traps must be non-empty and unique")
    mean_correct = round(sum(correct_lengths) / len(correct_lengths), 2)
    mean_incorrect = round(sum(incorrect_lengths) / len(incorrect_lengths), 2)
    cue_metrics = ma.get("cue_metrics", {})
    if (
        cue_metrics.get("mean_correct_words") != mean_correct
        or cue_metrics.get("mean_incorrect_words") != mean_incorrect
        or cue_metrics.get("all_options_terminal_punctuation_consistent") is not True
        or cue_metrics.get("unique_examiner_traps") is not True
        or cue_metrics.get("item_length_metrics") != item_length_metrics
        or cue_metrics.get("item_constraints") != {
            "maximum_option_to_minimum_option_ratio": 1.8,
            "maximum_word_disparity": 12,
            "maximum_correct_to_incorrect_mean_ratio": 1.5,
            "exceptions_allowed": False,
        }
    ):
        fail(errors, "MCQ_CUE_AUDIT_MISMATCH", f"correct={mean_correct} incorrect={mean_incorrect}")
    if mean_correct > mean_incorrect * 1.75 or mean_incorrect > mean_correct * 1.75:
        fail(errors, "MCQ_OPTION_LENGTH_CUE", f"correct={mean_correct} incorrect={mean_incorrect}")
    checks["mcqs"] = len(q)
    checks["mcq_test_cells"] = len(CELL_MATRIX)
    checks["mcq_coverage_ratio"] = round(expected_count / len(CELL_MATRIX), 6)

    pa = json.loads((root / "PYQ-DEMAND-AUDIT.json").read_text(encoding="utf-8"))
    reconstructed_primary = reconstruct_primary_pyqs(
        source_texts.get("pyq_2018_2025", ""),
        source_texts.get("pyq_2026", ""),
    )
    if len(reconstructed_primary) != 14:
        fail(errors, "PYQ_SNAPSHOT_RECONSTRUCTION_MISMATCH",
             f"Expected fourteen Buddhism-primary rows in immutable snapshots, found {len(reconstructed_primary)}")
    if pa.get("actual_total") != 14 or pa.get("expected_total") != 14 or len(pa.get("questions", [])) != 14:
        fail(errors, "PYQ_OMISSION", "Expected fourteen Buddhism-primary PYQs")
    if pa.get("questions", []) != reconstructed_primary:
        fail(errors, "PYQ_SNAPSHOT_RECONSTRUCTION_MISMATCH",
             "PYQ-DEMAND-AUDIT.json primary records differ from immutable ledger reconstruction")
    year_counts = {}
    for row in reconstructed_primary:
        year_counts[str(row["year"])] = year_counts.get(str(row["year"]), 0) + 1
    if year_counts != pa.get("expected_year_counts"):
        fail(errors, "PYQ_YEAR_COUNTS", json.dumps(year_counts, sort_keys=True))
    for key, audit_key in (("pyq_2018_2025", "2018_2025"), ("pyq_2026", "2026")):
        if pa.get("sources", {}).get(audit_key) != review.get("sources", {}).get(key):
            fail(errors, "PYQ_SOURCE_METADATA_MISMATCH", audit_key)
    workbook_snapshot = source_texts.get("formal_workbook", "")
    for index, row in enumerate(EXPECTED_SUPPORTING_PYQS, 14):
        owner = row["ownership"].split("-primary/", 1)[0] + " (supporting routed question)"
        expected_header = (
            f"#### PYQ {index} · {row['year']} · {row['question_no']} · "
            f"{row['marks']} marks · {owner}"
        )
        expected_wording = f"> **Question, as printed:** {row['text']}"
        if expected_header not in workbook_snapshot or expected_wording not in workbook_snapshot:
            fail(errors, "SUPPORTING_SOURCE_RECONSTRUCTION_MISMATCH", row["supporting_id"])
    if pa.get("supporting_total") != 3 or pa.get("supporting_questions", []) != EXPECTED_SUPPORTING_PYQS:
        fail(errors, "SUPPORTING_PYQ_AUDIT", "Frozen supporting records or ownerships differ")
    for surface_name, surface in (("REVISION-GUIDE.md", revision), ("ANSWER-WRITING-TOOLKIT.md", toolkit)):
        surface_primary = parse_pyq_surface(surface)
        if [row["number"] for row in surface_primary] != list(range(1, 15)):
            fail(errors, "PRIMARY_PYQ_NUMBERING", surface_name)
        comparable_primary = [{k: v for k, v in row.items() if k != "number"} for row in surface_primary]
        if comparable_primary != reconstructed_primary:
            fail(errors, "PYQ_SNAPSHOT_RECONSTRUCTION_MISMATCH",
                 f"{surface_name} primary records differ from immutable ledger reconstruction")
        surface_supporting = parse_pyq_surface(surface, supporting=True)
        if surface_supporting != EXPECTED_SUPPORTING_PYQS:
            fail(errors, "SUPPORTING_PYQ_CLASSIFICATION",
                 f"{surface_name} supporting records or exact ownerships differ")
    checks["pyqs"] = len(reconstructed_primary)
    checks["supporting_pyqs"] = len(EXPECTED_SUPPORTING_PYQS)

    bands = {10: (150, 200), 15: (250, 300), 20: (340, 400)}
    models = 0
    for m in re.finditer(r"\*\*Model answer \((10|15|20) marks,\s*(\d+)[–-](\d+) words\)\.\*\*\s*\n(.*?)(?=\n\*\*Why this earns marks|\n#### |\n## |\Z)", toolkit, re.S):
        marks = int(m.group(1))
        body = m.group(4)
        wc = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"[`*#>]", "", body), re.UNICODE))
        lo, hi = bands[marks]
        if (int(m.group(2)), int(m.group(3))) != (lo, hi) or not lo <= wc <= hi:
            fail(errors, "MAINS_WORD_BAND", f"{marks} marks: declared {m.group(2)}-{m.group(3)}, actual {wc}")
        models += 1
    if models != 23:
        fail(errors, "MAINS_MODEL_COUNT", f"Expected 23 timed models (14 primary + 3 supporting + 6 original), found {models}")
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
            extracted = (page.extract_text() or "").strip()
            if len(extracted) < 20:
                fail(errors, "PDF_EMPTY_PAGE", f"{row['file']}:{i+1}")
            if "\ufffd" in extracted:
                fail(errors, "PDF_GLYPH_INTEGRITY", f"{row['file']}:{i+1}")
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
