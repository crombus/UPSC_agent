"""Render, publish and record the combined Essay subject-wide package."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import markdown_learning_pdf  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


DATE = os.environ.get("ESSAY_TOPIC_DATE", "2026-09-04")
TOPIC_KEY = "essay-subject-wide-master"
SOURCE = (
    ROOT / "upsc-ai-kit" / "knowledge" / "Essay"
    / "subject-wide-syllabus" / "master"
)
PDF_DIR = ROOT / "notes" / "Essay" / "Subject-Wide-Syllabus" / "master"
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: path.read_bytes(), b""):
            digest.update(block)
            break
    return digest.hexdigest()


def render(source: Path, output: Path) -> tuple[int, int]:
    output.parent.mkdir(parents=True, exist_ok=True)
    markdown_learning_pdf.build_pdf(
        source,
        output,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
    )
    with fitz.open(output) as document:
        return document.page_count, len(document.get_toc())


def append_tracker(record: dict[str, object]) -> None:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    exports = tracker.get("exports")
    if tracker.get("schema_version") != 2 or not isinstance(exports, list):
        raise ValueError("Tracker must use schema v2.")
    identity = (
        record["topic_key"],
        record["variant"],
        int(record["generation"]),
    )
    if any(
        isinstance(item, dict)
        and (
            item.get("topic_key"),
            item.get("variant"),
            int(item.get("generation") or 1),
        )
        == identity
        for item in exports
    ):
        raise ValueError(f"Tracker already contains {identity}.")
    updated = dict(tracker)
    updated["exports"] = [*exports, record]
    temporary = TRACKER.with_suffix(".essay-master.pending.json")
    temporary.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, TRACKER)


def main() -> int:
    guide = SOURCE / "Essay_Complete-Subject-Guide-and-Solved-PYQs.md"
    workbook = SOURCE / "Essay_Subject-Wide-Practice-Workbook.md"
    solutions = SOURCE / "Essay_Subject-Wide-Practice-Solutions.md"
    for path in (guide, workbook, solutions):
        if not path.is_file():
            raise FileNotFoundError(path)
    guide_text = guide.read_text(encoding="utf-8")
    workbook_text = workbook.read_text(encoding="utf-8")
    solutions_text = solutions.read_text(encoding="utf-8")
    if guide_text.count("## TOPIC ") != 16:
        raise ValueError("Guide does not contain all 16 knowledge topics.")
    if guide_text.count("### 20") != 100:
        raise ValueError("Guide does not contain all 100 solved PYQs.")
    if workbook_text.count("### 20") != 100 or workbook_text.count("### P") != 32:
        raise ValueError("Workbook does not contain all 132 topics.")
    if solutions_text.count("### 20") != 100 or solutions_text.count("### P") != 32:
        raise ValueError("Solutions do not match all 132 workbook topics.")
    if re.search(
        r"(?im)^### SESSION \d+|^### Q\d+\.",
        guide_text + workbook_text + solutions_text,
    ):
        raise ValueError("Sessions or MCQs remain in the Essay master package.")
    tracker = refresh.load_tracker()
    generation = refresh.next_new_topic_generation(tracker, TOPIC_KEY)
    generation_dir = PDF_DIR / f"g{generation}"
    guide_pdf = generation_dir / f"Essay_Complete-Subject-Guide_{DATE}.pdf"
    workbook_pdf = generation_dir / f"Essay_Practice-Workbook_{DATE}.pdf"
    solutions_pdf = generation_dir / f"Essay_Practice-Solutions_{DATE}.pdf"
    guide_pages, guide_bookmarks = render(guide, guide_pdf)
    workbook_pages, workbook_bookmarks = render(workbook, workbook_pdf)
    solution_pages, solution_bookmarks = render(solutions, solutions_pdf)
    record = {
        "record_id": f"{TOPIC_KEY}:learner-v2:g{generation}",
        "topic_key": TOPIC_KEY,
        "subject": "Essay",
        "section": "Subject-Wide-Syllabus",
        "title": "Complete Essay Subject-Wide Guide, PYQs and Practice",
        "variant": "learner-v2",
        "generation": generation,
        "command": "Generate Essay subject-wide master package",
        "main_pdf": relative(guide_pdf),
        "workbook": relative(workbook_pdf),
        "solutions_pdf": relative(solutions_pdf),
        "markdown": relative(guide),
        "workbook_markdown": relative(workbook),
        "solutions_markdown": relative(solutions),
        "generated_on": DATE,
        "approved": False,
        "format": {
            "name": "essay-subject-wide-master-v1",
            "knowledge_topics": 16,
            "solved_pyqs": 100,
            "practice_topics": 132,
            "practice_solutions": 132,
            "learning_sessions": 0,
            "mcqs": 0,
            "guide_pages": guide_pages,
            "workbook_pages": workbook_pages,
            "solutions_pages": solution_pages,
            "guide_bookmarks": guide_bookmarks,
            "workbook_bookmarks": workbook_bookmarks,
            "solutions_bookmarks": solution_bookmarks,
        },
        "provenance": {
            "source_manifest": (
                "upsc-ai-kit\\manifests\\v2\\essay--subject-wide-syllabus.json"
            ),
            "pyq_corpus": "upsc-ai-kit\\knowledge\\Essay\\PYQ-Corpus-2013-2025.md",
            "source_hashes": {
                relative(path): sha256(path)
                for path in (guide, workbook, solutions)
            },
        },
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": f"{TOPIC_KEY}:learner-v2:g{generation}",
        },
        "validation": {
            "state": "passed",
            "validated_on": date.today().isoformat(),
            "validator": "tools/publish_essay_master_package.py",
        },
        "refresh_profile": "essay-subject-wide-master-v1",
    }
    record_path = (
        EXPORT_DIR
        / f"{TOPIC_KEY}-learner-v2-g{generation}-{DATE}-record.json"
    )
    record_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    append_tracker(record)
    index = ROOT / "notes" / "Essay" / "Subject-Wide-Syllabus" / "INDEX.md"
    index.write_text(
        "# Essay Subject-Wide Master Package\n\n"
        "The primary Essay output is one combined package covering all 16 "
        "knowledge topics.\n\n"
        f"- Knowledge guide with 100 solved PYQs: `{relative(guide_pdf)}`\n"
        f"- Question-only workbook with 132 topics: `{relative(workbook_pdf)}`\n"
        f"- Separate matching solutions: `{relative(solutions_pdf)}`\n"
        "- Learning sessions: 0\n"
        "- MCQs: 0\n"
        "- Approved: no\n",
        encoding="utf-8",
    )
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    completion = (
        EXPORT_DIR / f"essay-subject-wide-master-{DATE}-completion.json"
    )
    ledger = EXPORT_DIR / f"essay-subject-wide-master-{DATE}-changed-files.txt"
    changed = {
        "EXPORT-PDF-STATUS.json",
        "EXPORT-PDF-COMMAND-INDEX.md",
        "tools\\generate_essay_master_package.py",
        "tools\\publish_essay_master_package.py",
        "upsc-ai-kit\\knowledge\\Essay\\README.md",
        "upsc-ai-kit\\knowledge\\Essay\\LEARNING-SESSION-COMMAND-INDEX.md",
        relative(guide),
        relative(workbook),
        relative(solutions),
        relative(guide_pdf),
        relative(workbook_pdf),
        relative(solutions_pdf),
        relative(index),
        relative(record_path),
        relative(completion),
        relative(ledger),
    }
    payload = {
        "schema_version": 1,
        "batch_id": f"essay-subject-wide-master-{DATE}",
        "scope": "Essay only; all 16 existing knowledge topics",
        "generated_on": DATE,
        "validated_at": datetime.now().astimezone().isoformat(),
        "result": "passed",
        "record_id": record["record_id"],
        "approved": False,
        "metrics": record["format"],
        "changed_files_ledger": {
            "path": relative(ledger),
            "count": len(changed),
        },
        "errors": [],
    }
    ledger.write_text(
        "\n".join(sorted(changed, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    completion.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
