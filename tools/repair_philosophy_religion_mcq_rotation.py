"""Rotate active Philosophy-of-Religion diagnostic keys strictly A→B→C→D.

The script moves complete option chunks, updates answer labels and remaps option
letters in explanations.  It never changes the correct proposition, question
wording, PYQs, model answers, generation identity or approval.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

import markdown_learning_pdf


ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "EXPORT-PDF-STATUS.json"
AUDIT_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "philosophy-religion-mcq-rotation-reviewed-map-2026-08-25.json"
)
TOPIC_KEYS = tuple(
    f"philosophy-paper-ii-philosophy-of-religion-{index:02d}"
    for index in range(1, 11)
)
SECTION_RE = re.compile(
    r"(?ims)(^##\s+BASIC MCQS / REMEDIATION\s*$)(?P<body>.*?)(?=^##\s+PYQS AND ANSWER PRACTICE\s*$)"
)
QUESTION_START_RE = re.compile(
    r"^(?:####\s+(?:(?:Remedial\s+)?MCQ\s+)?\d+\b.*|"
    r"####\s+Remedial\s+R\d+\b.*|"
    r"\*\*\d+\.\s+.+\*\*|"
    r"\d+\.\s+\S.+)$",
    re.I,
)
OPTION_RE = re.compile(r"^(?P<indent>\s*)(?P<label>[ABCD])\.\s+(?P<body>.*)$")
ANSWER_RE = re.compile(
    r"^\*\*(?P<prefix>Correct answer|Answer):\s*"
    r"(?P<label>[ABCD])(?P<tail>.*?)\*\*(?P<post>.*)$",
    re.I,
)


class RotationError(RuntimeError):
    """Raised when an objective item cannot be safely rotated."""


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def repo_path(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json_atomic(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".rotation-pending")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".rotation-pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def active_records(status: dict[str, Any]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for topic_key in TOPIC_KEYS:
        candidates = [
            record
            for record in status["exports"]
            if record.get("topic_key") == topic_key
            and record.get("variant") == "learner-v2"
        ]
        if not candidates:
            raise RotationError(f"Missing active record: {topic_key}")
        records.append(
            max(candidates, key=lambda item: int(item.get("generation") or 0))
        )
    return records


def workbook_source(markdown: Path) -> Path:
    candidates = sorted(markdown.parent.glob("*Solved*Workbook*.md"))
    if len(candidates) != 1:
        raise RotationError(
            f"Expected one active workbook Markdown beside {markdown}, found "
            f"{len(candidates)}."
        )
    return candidates[0]


def option_content_hash(block: str) -> str:
    lines = block.splitlines()
    chunks: list[str] = []
    positions = [
        index for index, line in enumerate(lines) if OPTION_RE.match(line)
    ]
    for offset, start in enumerate(positions):
        end = positions[offset + 1] if offset + 1 < len(positions) else len(lines)
        answer_positions = [
            index
            for index in range(start + 1, end)
            if ANSWER_RE.match(lines[index])
        ]
        if answer_positions:
            end = answer_positions[0]
        first = OPTION_RE.match(lines[start])
        assert first is not None
        content = [first.group("body"), *lines[start + 1 : end]]
        chunks.append("\n".join(content).strip())
    encoded = json.dumps(sorted(chunks), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def remap_explanation(text: str, mapping: dict[str, str]) -> str:
    placeholders = {
        old: f"__OPTION_LETTER_{index}__"
        for index, old in enumerate("ABCD")
    }
    for old, placeholder in placeholders.items():
        text = re.sub(rf"\b{old}\b", placeholder, text)
    for old, placeholder in placeholders.items():
        text = text.replace(placeholder, mapping[old])
    return text


def rotate_block(
    block: str,
    desired: str,
) -> tuple[str, dict[str, Any]]:
    lines = block.splitlines()
    option_positions = [
        index for index, line in enumerate(lines) if OPTION_RE.match(line)
    ]
    answer_positions = [
        index for index, line in enumerate(lines) if ANSWER_RE.match(line)
    ]
    if len(option_positions) != 4 or len(answer_positions) != 1:
        raise RotationError(
            f"Expected four options and one answer, found "
            f"{len(option_positions)} and {len(answer_positions)}."
        )
    answer_index = answer_positions[0]
    if option_positions[-1] >= answer_index:
        raise RotationError("Answer label appears before all options.")
    labels = [OPTION_RE.match(lines[index]).group("label") for index in option_positions]
    if labels != list("ABCD"):
        raise RotationError(f"Option labels are not A/B/C/D: {labels}")
    answer_match = ANSWER_RE.match(lines[answer_index])
    assert answer_match is not None
    old_answer = answer_match.group("label").upper()
    old_hash = option_content_hash(block)
    chunks: dict[str, list[str]] = {}
    for offset, start in enumerate(option_positions):
        end = (
            option_positions[offset + 1]
            if offset + 1 < len(option_positions)
            else answer_index
        )
        chunks[labels[offset]] = lines[start:end]
    desired_order = [old_answer, *[label for label in "ABCD" if label != old_answer]]
    target_index = "ABCD".index(desired)
    desired_order[0], desired_order[target_index] = (
        desired_order[target_index],
        desired_order[0],
    )
    mapping = {
        old_label: new_label
        for old_label, new_label in zip(desired_order, "ABCD")
    }
    rebuilt_options: list[str] = []
    for new_label, old_label in zip("ABCD", desired_order):
        chunk = list(chunks[old_label])
        match = OPTION_RE.match(chunk[0])
        assert match is not None
        chunk[0] = (
            f"{match.group('indent')}{new_label}. {match.group('body')}"
        )
        rebuilt_options.extend(chunk)
    before_options = lines[: option_positions[0]]
    after_answer = lines[answer_index + 1 :]
    remapped_after = remap_explanation("\n".join(after_answer), mapping).splitlines()
    answer_line = (
        f"**{answer_match.group('prefix')}: {desired}"
        f"{answer_match.group('tail')}**{answer_match.group('post')}"
    )
    rebuilt = "\n".join(
        [*before_options, *rebuilt_options, answer_line, *remapped_after]
    )
    new_hash = option_content_hash(rebuilt)
    if old_hash != new_hash:
        raise RotationError("Option proposition multiset changed during rotation.")
    return rebuilt, {
        "before_answer": old_answer,
        "after_answer": desired,
        "old_to_new_letter_map": mapping,
        "option_content_sha256": new_hash,
    }


def candidate_starts(lines: list[str]) -> list[int]:
    candidates: dict[str, list[int]] = {"heading": [], "bold": [], "plain": []}
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not QUESTION_START_RE.match(stripped):
            continue
        kind = (
            "heading"
            if stripped.startswith("####")
            else "bold"
            if stripped.startswith("**")
            else "plain"
        )
        candidates[kind].append(index)
    for kind in ("heading", "bold", "plain"):
        if candidates[kind]:
            return candidates[kind]
    return []


def rotate_basic_section(text: str) -> tuple[str, list[dict[str, Any]]]:
    match = SECTION_RE.search(text)
    if not match:
        raise RotationError("Missing BASIC MCQS / REMEDIATION section.")
    body = match.group("body")
    lines = body.splitlines()
    starts = candidate_starts(lines)
    if not starts:
        raise RotationError("No objective items were parsed.")
    chunks: list[str] = []
    cursor = 0
    audit: list[dict[str, Any]] = []
    for question_index, start in enumerate(starts):
        end = starts[question_index + 1] if question_index + 1 < len(starts) else len(lines)
        chunks.extend(lines[cursor:start])
        block = "\n".join(lines[start:end])
        desired = "ABCD"[question_index % 4]
        rotated, result = rotate_block(block, desired)
        result["question_number"] = question_index + 1
        audit.append(result)
        chunks.extend(rotated.splitlines())
        cursor = end
    chunks.extend(lines[cursor:])
    replacement = match.group(1) + "\n" + "\n".join(chunks) + "\n"
    return text[: match.start()] + replacement + text[match.end() :], audit


def render_with_backup(
    source: Path,
    output: Path,
    *,
    mode: str,
    topic_key: str,
) -> None:
    backup = ROOT / ".agent-scratch" / f"{topic_key}-{mode}-pre-rotation.pdf"
    backup.parent.mkdir(exist_ok=True)
    shutil.copy2(output, backup)
    try:
        markdown_learning_pdf.build_pdf(
            source,
            output,
            mode=mode,
            variant="learner-v2",
            topic_key=topic_key,
            repository_root=ROOT,
        )
    except Exception:
        shutil.copy2(backup, output)
        raise
    backup.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not args.apply:
        parser.error("Pass --apply.")
    status = load_json(STATUS_PATH)
    records = active_records(status)
    audit: dict[str, Any] = {
        "schema_version": 1,
        "audit_id": "philosophy-religion-mcq-rotation-2026-08-25",
        "policy": "Strict A→B→C→D across every active diagnostic sequence",
        "topics": [],
    }
    for record in records:
        topic_key = str(record["topic_key"])
        main_source = repo_path(str(record["markdown"]))
        workbook_md = workbook_source(main_source)
        main_before = main_source.read_text(encoding="utf-8")
        workbook_before = workbook_md.read_text(encoding="utf-8")
        main_after, main_audit = rotate_basic_section(main_before)
        workbook_after, workbook_audit = rotate_basic_section(workbook_before)
        if len(main_audit) != len(workbook_audit):
            raise RotationError(
                f"{topic_key}: main/workbook objective counts differ: "
                f"{len(main_audit)} != {len(workbook_audit)}."
            )
        write_text_atomic(main_source, main_after)
        write_text_atomic(workbook_md, workbook_after)
        render_with_backup(
            main_source,
            repo_path(str(record["main_pdf"])),
            mode="main",
            topic_key=topic_key,
        )
        render_with_backup(
            main_source,
            repo_path(str(record["workbook"])),
            mode="workbook",
            topic_key=topic_key,
        )
        record.setdefault("provenance", {}).setdefault(
            "deep_quality_repair",
            {},
        )["mcq_rotation"] = {
            "policy": "strict A→B→C→D",
            "workbook_source": relative(workbook_md),
            "questions_rotated": len(workbook_audit),
            "reviewed_map": relative(AUDIT_PATH),
        }
        audit["topics"].append(
            {
                "topic_key": topic_key,
                "record_id": record["record_id"],
                "workbook_source": relative(workbook_md),
                "question_count": len(workbook_audit),
                "before_sequence": "".join(
                    item["before_answer"] for item in workbook_audit
                ),
                "after_sequence": "".join(
                    item["after_answer"] for item in workbook_audit
                ),
                "questions": workbook_audit,
            }
        )
    write_json_atomic(AUDIT_PATH, audit)
    write_json_atomic(STATUS_PATH, status)
    print(
        f"rotated_topics={len(records)} "
        f"rotated_questions={sum(item['question_count'] for item in audit['topics'])}"
    )
    print(f"audit={relative(AUDIT_PATH)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
