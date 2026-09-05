"""Record completion of the Essay-only guide/workbook/solutions redesign."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
DATE = os.environ.get("ESSAY_TOPIC_DATE", "2026-09-04")
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
TOPIC_KEYS = [f"essay-{number:02d}" for number in range(1, 5)]
BATCH_ID = f"essay-01-04-guide-redesign-{DATE}"


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def latest_record(records: list[dict[str, object]], key: str) -> dict[str, object]:
    matches = [
        item
        for item in records
        if item.get("topic_key") == key
        and item.get("variant") == "learner-v2"
    ]
    return max(matches, key=lambda item: int(item.get("generation") or 1))


def pdf_pages(path: Path) -> int:
    with fitz.open(path) as document:
        return document.page_count


def main() -> int:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    records = [item for item in tracker["exports"] if isinstance(item, dict)]
    topics = []
    errors = []
    changed = {
        "EXPORT-PDF-STATUS.json",
        "EXPORT-PDF-COMMAND-INDEX.md",
        "tools\\generate_essay_common.py",
        "tools\\publish_essay_guides.py",
        "tools\\record_essay_redesign_completion.py",
        "upsc-ai-kit\\knowledge\\Essay\\README.md",
        "upsc-ai-kit\\knowledge\\Essay\\LEARNING-SESSION-COMMAND-INDEX.md",
        "notes\\Essay\\Subject-Wide-Syllabus\\INDEX.md",
    }
    for key in TOPIC_KEYS:
        record = latest_record(records, key)
        guide = ROOT / str(record["markdown"])
        workbook = ROOT / str(record["workbook_markdown"])
        solutions = ROOT / str(record["solutions_markdown"])
        paths = [
            guide,
            workbook,
            solutions,
            ROOT / str(record["main_pdf"]),
            ROOT / str(record["workbook"]),
            ROOT / str(record["solutions_pdf"]),
        ]
        missing = [relative(path) for path in paths if not path.is_file()]
        if missing:
            errors.append(f"{key}: missing {missing}")
            continue
        guide_text = guide.read_text(encoding="utf-8")
        workbook_text = workbook.read_text(encoding="utf-8")
        solutions_text = solutions.read_text(encoding="utf-8")
        session_count = len(re.findall(r"(?im)^### SESSION \d+", guide_text))
        mcq_count = len(
            re.findall(
                r"(?im)^### Q\d+\.",
                "\n".join((guide_text, workbook_text, solutions_text)),
            )
        )
        practice_topics = workbook_text.count("## TOPIC ")
        practice_solutions = solutions_text.count("## SOLUTION ")
        solved_upsc = guide_text.count("## SOLUTION ")
        method_drills = guide_text.count("### METHOD DRILL ")
        complete_owner_markers = (
            "## COMPLETE BASIC KNOWLEDGE" in guide_text
            and "## COMPLETE ADVANCED KNOWLEDGE" in guide_text
        )
        gates = {
            "essay_specific_format": record.get("refresh_profile")
            == "essay-specific-guide-v1",
            "single_complete_knowledge_guide": complete_owner_markers,
            "no_learning_sessions": session_count == 0,
            "no_mcqs": mcq_count == 0,
            "question_only_workbook": practice_topics >= 1
            and "## SOLUTION " not in workbook_text,
            "separate_matching_solutions": practice_topics == practice_solutions,
            "solved_upsc_questions_in_guide": solved_upsc == 3,
            "retained_method_material": method_drills == 6,
            "three_real_pdfs": all(pdf_pages(path) > 0 for path in paths[3:]),
            "approval_false": record.get("approved") is False,
        }
        failed = [name for name, passed in gates.items() if not passed]
        if failed:
            errors.append(f"{key}: failed {failed}")
        changed.update(relative(path) for path in paths)
        changed.add(
            f"upsc-ai-kit\\manifests\\exports\\{key}-essay-guide-{DATE}.json"
        )
        changed.add(
            "upsc-ai-kit\\manifests\\exports\\"
            f"{key}-learner-v2-g{record['generation']}-{DATE}-essay-guide-record.json"
        )
        topics.append(
            {
                "topic_key": key,
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record["approved"],
                "hard_gates": gates,
                "metrics": {
                    "learning_sessions": session_count,
                    "mcqs": mcq_count,
                    "practice_topics": practice_topics,
                    "practice_solutions": practice_solutions,
                    "solved_upsc_questions": solved_upsc,
                    "method_drills_retained": method_drills,
                    "guide_pages": pdf_pages(paths[3]),
                    "workbook_pages": pdf_pages(paths[4]),
                    "solutions_pages": pdf_pages(paths[5]),
                },
            }
        )
    completion = EXPORT_DIR / f"{BATCH_ID}-completion.json"
    ledger = EXPORT_DIR / f"{BATCH_ID}-changed-files.txt"
    changed.update((relative(completion), relative(ledger)))
    payload = {
        "schema_version": 1,
        "batch_id": BATCH_ID,
        "scope": "Essay topics 01-04 only",
        "generated_on": DATE,
        "validated_at": datetime.now().astimezone().isoformat(),
        "result": "failed" if errors else "passed",
        "format": {
            "knowledge_guides": 4,
            "question_only_workbooks": 4,
            "separate_solution_pdfs": 4,
            "learning_sessions": 0,
            "mcqs": 0,
        },
        "topics": topics,
        "errors": errors,
        "changed_files_ledger": {
            "path": relative(ledger),
            "count": len(changed),
        },
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
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
