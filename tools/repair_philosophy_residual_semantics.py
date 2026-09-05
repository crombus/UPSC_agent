"""Repair residual non-session answer labels found by the deep validator."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

import markdown_learning_pdf
import philosophy_indian_religion_deep_quality_repair as repair


ROOT = Path(__file__).resolve().parents[1]
NOTIONS = "philosophy-paper-ii-philosophy-of-religion-01"
PROOFS = "philosophy-paper-ii-philosophy-of-religion-02"
EVIL = "philosophy-paper-ii-philosophy-of-religion-03"
EXTRA_CLOSURE_ANSWERS = {
    "Part I - Nyaya's notion of God":
        "Nyāya infers an omniscient efficient cause that orders eternal atoms and dispenses karmic fruits without becoming the world's material cause.",
    "Madhva, Śaiva and Śākta notions of God":
        "Madhva, Śaiva and Śākta models differ over divine-world relations, so comparison must track causation, world-status, soul-status and liberation.",
    "Part II - Is Hinduism polytheistic?":
        "Hindu divine plurality ranges from polytheism to henotheism and qualified unity, so deity-count alone cannot settle its philosophical structure.",
    "Comparative synthesis":
        "Comparison is strongest when the same axes—ultimate reality, causation, world, self and worship—are applied consistently across traditions.",
    "PYQ answer frameworks":
        "A high-scoring answer defines the model, compares it on common axes, tests one serious objection and ends with a qualified verdict.",
    "Model philosophical conclusion":
        "The notion of God is a family of competing metaphysical models whose adequacy depends on coherence, world-relation and religious function.",
    "UPSC ANSWER WRITING FOR NOTIONS OF GOD":
        "God is not a single universal concept but a family of metaphysical models differing over personality, causation, world-relation and human destiny.",
}
CLOSURE_RE = re.compile(r"(?ms)```closure-flow\s*\n(.*?)\n```")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json_atomic(path: Path, data: object) -> None:
    temporary = path.with_suffix(path.suffix + ".residual-pending")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".residual-pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def repair_notions_closures(text: str) -> tuple[str, list[dict[str, str]]]:
    changes: list[dict[str, str]] = []

    def replace(match: re.Match[str]) -> str:
        body = match.group(1)
        subtopic_match = re.search(r"(?m)^SUBTOPIC:\s*(.+?)\s*$", body)
        if not subtopic_match:
            return match.group(0)
        subtopic = subtopic_match.group(1).strip()
        if subtopic not in EXTRA_CLOSURE_ANSWERS:
            return match.group(0)
        answer_match = re.search(
            r"(?m)^ANSWER-GRABBING FORMULATION:\s*(.*?)\s*$",
            body,
        )
        if not answer_match:
            raise ValueError(f"Closure {subtopic!r} lacks answer field.")
        before = answer_match.group(1)
        after = EXTRA_CLOSURE_ANSWERS[subtopic]
        body = (
            body[: answer_match.start(1)]
            + after
            + body[answer_match.end(1) :]
        )
        changes.append(
            {"subtopic": subtopic, "before": before, "after": after}
        )
        return "```closure-flow\n" + body + "\n```"

    return CLOSURE_RE.sub(replace, text), changes


def demote_roadmap_label(text: str) -> tuple[str, int]:
    pattern = re.compile(
        r"(?m)^>\s*\*\*ANSWER-GRABBING LINE\s*[—-]\s*"
        r"WRITE/ADAPT IN THE EXAM\*\*\s*$"
    )
    return pattern.subn("> **EXAM ROUTE**", text)


def render(record: dict[str, Any]) -> None:
    source = repair.repo_path(str(record["markdown"]))
    output = repair.repo_path(str(record["main_pdf"]))
    backup = ROOT / ".agent-scratch" / f"{record['topic_key']}-pre-residual.pdf"
    shutil.copy2(output, backup)
    try:
        markdown_learning_pdf.build_pdf(
            source,
            output,
            mode="main",
            variant="learner-v2",
            topic_key=str(record["topic_key"]),
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
    status = load_json(repair.STATUS_PATH)
    records = {
        record["topic_key"]: record for record in repair.active_records(status)
    }
    reviewed_map = load_json(repair.REVIEWED_MAP_PATH)
    audit = []
    for topic_key in (NOTIONS, PROOFS, EVIL):
        record = records[topic_key]
        path = repair.repo_path(str(record["markdown"]))
        text = path.read_text(encoding="utf-8")
        topic_changes: dict[str, Any] = {"topic_key": topic_key}
        if topic_key == NOTIONS:
            text, closure_changes = repair_notions_closures(text)
            topic_changes["closure_answer_changes"] = closure_changes
        text, demoted = demote_roadmap_label(text)
        topic_changes["roadmap_labels_demoted"] = demoted
        write_text_atomic(path, text)
        render(record)
        record.setdefault("provenance", {}).setdefault(
            "deep_quality_repair",
            {},
        )["residual_semantic_audit"] = True
        audit.append(topic_changes)
    reviewed_map["residual_semantic_repairs"] = audit
    write_json_atomic(repair.REVIEWED_MAP_PATH, reviewed_map)
    write_json_atomic(repair.STATUS_PATH, status)
    print(
        f"topics={len(audit)} closure_changes="
        f"{sum(len(item.get('closure_answer_changes', [])) for item in audit)} "
        f"labels_demoted={sum(item['roadmap_labels_demoted'] for item in audit)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
