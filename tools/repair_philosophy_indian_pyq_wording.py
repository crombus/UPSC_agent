"""Restore exact verified PYQ wording in the five active Indian packages."""

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
LEDGER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-1"
    / "_PYQ-Indian-Philosophy-2018-2025.md"
)
AUDIT_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "philosophy-indian-pyq-wording-repair-2026-08-25.json"
)
OWNER_BASENAMES = {
    "philosophy-paper-i-indian-philosophy-01": "Carvaka.md",
    "philosophy-paper-i-indian-philosophy-02": "Jainism.md",
    "philosophy-paper-i-indian-philosophy-03": "Buddhism.md",
    "philosophy-paper-i-indian-philosophy-04": "Nyaya-Vaisesika.md",
    "philosophy-paper-i-indian-philosophy-05": "Samkhya.md",
}
PRACTICE_RE = re.compile(
    r"(?ims)(^##\s+PYQS AND ANSWER PRACTICE\s*$)(?P<body>.*?)(?=^##\s+OPTIONAL ADVANCED DEPTH)"
)
SOURCE_QUESTION_RE = re.compile(
    r"(?ms)(^####\s+(?P<year>20\d{2})\s+·\s+"
    r"(?P<q>Q\d+\([a-z]\))\s+·[^\n]*\n+"
    r"\*\*Question:\*\*\s*)(?P<question>[^\n]+)"
)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json_atomic(path: Path, data: object) -> None:
    temporary = path.with_suffix(path.suffix + ".pyq-pending")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    temporary = path.with_suffix(path.suffix + ".pyq-pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def ledger_questions(owner: str) -> dict[tuple[str, str], str]:
    year = ""
    questions: dict[tuple[str, str], str] = {}
    owner_pattern = re.compile(
        rf"^-\s+\*\*(?P<q>Q\d+\([a-z]\))\s+·[^:]+"
        rf"\]\(\./indian/{re.escape(owner)}\):\*\*\s+(?P<question>.+)$"
    )
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^##\s+(20\d{2})\b", line)
        if heading:
            year = heading.group(1)
            continue
        match = owner_pattern.match(line)
        if not match:
            continue
        question = match.group("question").split("📝", 1)[0].strip()
        questions[(year, match.group("q").casefold())] = question
    return questions


def repair_source(
    text: str,
    expected: dict[tuple[str, str], str],
) -> tuple[str, list[dict[str, str]]]:
    practice = PRACTICE_RE.search(text)
    if not practice:
        raise ValueError("Missing PYQS AND ANSWER PRACTICE section.")
    changes: list[dict[str, str]] = []
    found: set[tuple[str, str]] = set()

    def replace(match: re.Match[str]) -> str:
        identity = (match.group("year"), match.group("q").casefold())
        if identity not in expected:
            return match.group(0)
        found.add(identity)
        before = match.group("question").strip()
        after = expected[identity]
        if before != after:
            changes.append(
                {
                    "year": identity[0],
                    "question": match.group("q"),
                    "before": before,
                    "after": after,
                }
            )
        return match.group(1) + after

    body = SOURCE_QUESTION_RE.sub(replace, practice.group("body"))
    missing = sorted(set(expected) - found)
    if missing:
        raise ValueError(f"Verified PYQs missing from solved practice: {missing}")
    repaired = (
        text[: practice.start()]
        + practice.group(1)
        + body
        + text[practice.end() :]
    )
    return repaired, changes


def render(record: dict[str, Any]) -> None:
    source = repair.repo_path(str(record["markdown"]))
    for mode, field in (("main", "main_pdf"), ("workbook", "workbook")):
        output = repair.repo_path(str(record[field]))
        backup = (
            ROOT / ".agent-scratch"
            / f"{record['topic_key']}-{mode}-pre-pyq-repair.pdf"
        )
        shutil.copy2(output, backup)
        try:
            markdown_learning_pdf.build_pdf(
                source,
                output,
                mode=mode,
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
    audit = {"schema_version": 1, "topics": []}
    for topic_key, owner in OWNER_BASENAMES.items():
        record = records[topic_key]
        path = repair.repo_path(str(record["markdown"]))
        expected = ledger_questions(owner)
        repaired, changes = repair_source(
            path.read_text(encoding="utf-8"),
            expected,
        )
        write_text_atomic(path, repaired)
        render(record)
        record.setdefault("provenance", {}).setdefault(
            "deep_quality_repair",
            {},
        )["verified_pyq_wording"] = {
            "ledger": repair.relative(LEDGER),
            "questions_checked": len(expected),
            "questions_restored": len(changes),
            "audit": repair.relative(AUDIT_PATH),
        }
        audit["topics"].append(
            {
                "topic_key": topic_key,
                "owner": owner,
                "verified_questions": len(expected),
                "questions_restored": len(changes),
                "changes": changes,
            }
        )
    write_json_atomic(AUDIT_PATH, audit)
    write_json_atomic(repair.STATUS_PATH, status)
    print(
        f"topics={len(audit['topics'])} verified="
        f"{sum(item['verified_questions'] for item in audit['topics'])} "
        f"restored={sum(item['questions_restored'] for item in audit['topics'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
