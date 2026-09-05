"""Render and publish Qualifying English and Hindi subject-wide packages."""

from __future__ import annotations

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
import unicode_markdown_pdf  # noqa: E402


DATE = os.environ.get("LANGUAGE_PACKAGE_DATE", "2026-09-04")
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"

CONFIGS = {
    "Qualifying-English": {
        "topic_key": "qualifying-english-subject-master",
        "title": "UPSC Qualifying English Complete Skills Package",
    },
    "Qualifying-Hindi": {
        "topic_key": "qualifying-hindi-subject-master",
        "title": "UPSC अनिवार्य हिन्दी सम्पूर्ण कौशल पैकेज",
    },
}


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def render(
    source: Path,
    output: Path,
    topic_key: str,
    *,
    unicode_heavy: bool = False,
    document_kind: str = "Complete Skills Guide",
) -> tuple[int, int, int]:
    output.parent.mkdir(parents=True, exist_ok=True)
    if unicode_heavy:
        unicode_markdown_pdf.build_pdf(
            source,
            output,
            internal_index=True,
            index_title=f"CONTENTS / {document_kind.upper()}",
            cover_descriptor=(
                f"UPSC qualifying-language subject package | {document_kind} | "
                "Official syllabus to timed remediation"
            ),
            footer_label=f"UPSC Qualifying Hindi | {document_kind}",
        )
    else:
        markdown_learning_pdf.build_pdf(
            source,
            output,
            topic_key=topic_key,
            repository_root=ROOT,
            internal_index=True,
            index_title=f"CONTENTS / {document_kind.upper()}",
            cover_descriptor=(
                f"UPSC qualifying-language subject package | {document_kind} | "
                "Official syllabus to timed remediation"
            ),
            footer_label=f"UPSC Qualifying Language | {document_kind}",
        )
    with fitz.open(output) as document:
        text_length = sum(len(page.get_text().strip()) for page in document)
        empty_pages = sum(not page.get_text().strip() for page in document)
        return document.page_count, text_length, empty_pages


def publish_subject(
    subject: str,
    config: dict[str, str],
    *,
    generation: int = 1,
    generated_on: str = DATE,
) -> dict[str, object]:
    topic_key = config["topic_key"]
    source_dir = (
        ROOT / "upsc-ai-kit" / "knowledge" / subject / "subject-wide-package"
    )
    guide = source_dir / f"{subject}_Complete-Skills-Guide.md"
    workbook = source_dir / f"{subject}_Practice-Workbook.md"
    solutions = source_dir / f"{subject}_Practice-Solutions.md"
    for path in (guide, workbook, solutions):
        if not path.is_file():
            raise FileNotFoundError(path)
    combined = "\n".join(
        path.read_text(encoding="utf-8") for path in (guide, workbook, solutions)
    )
    if re.search(r"(?im)^### SESSION \d+", combined):
        raise ValueError(f"{subject}: artificial learning sessions remain.")
    output_dir = (
        ROOT / "notes" / subject / "Subject-Wide-Package" / f"g{generation}"
    )
    guide_pdf = output_dir / f"{subject}_Complete-Skills-Guide_{generated_on}.pdf"
    workbook_pdf = output_dir / f"{subject}_Practice-Workbook_{generated_on}.pdf"
    solutions_pdf = output_dir / f"{subject}_Practice-Solutions_{generated_on}.pdf"
    unicode_heavy = subject == "Qualifying-Hindi"
    guide_metrics = render(
        guide,
        guide_pdf,
        topic_key,
        unicode_heavy=unicode_heavy,
        document_kind="Complete Skills Guide",
    )
    workbook_metrics = render(
        workbook,
        workbook_pdf,
        topic_key,
        unicode_heavy=unicode_heavy,
        document_kind="Question-Only Practice Workbook",
    )
    solutions_metrics = render(
        solutions,
        solutions_pdf,
        topic_key,
        unicode_heavy=unicode_heavy,
        document_kind="Practice Solutions",
    )
    for name, metrics in (
        ("guide", guide_metrics),
        ("workbook", workbook_metrics),
        ("solutions", solutions_metrics),
    ):
        if metrics[0] < 1 or metrics[1] < 1 or metrics[2] != 0:
            raise ValueError(f"{subject}: invalid {name} PDF metrics {metrics}.")
    record = {
        "record_id": f"{topic_key}:learner-v2:g{generation}",
        "topic_key": topic_key,
        "subject": subject,
        "section": "Subject-Wide-Package",
        "title": config["title"],
        "variant": "learner-v2",
        "generation": generation,
        "command": f"Generate {subject} subject-wide skills package",
        "main_pdf": relative(guide_pdf),
        "workbook": relative(workbook_pdf),
        "solutions_pdf": relative(solutions_pdf),
        "markdown": relative(guide),
        "workbook_markdown": relative(workbook),
        "solutions_markdown": relative(solutions),
        "generated_on": generated_on,
        "approved": False,
        "format": {
            "name": "qualifying-language-subject-package-v1",
            "learning_sessions": 0,
            "guide_source_sections": 12,
            "practice_papers": 3,
            "matching_solution_keys": 3,
            "guide_pages": guide_metrics[0],
            "workbook_pages": workbook_metrics[0],
            "solutions_pages": solutions_metrics[0],
            "empty_pdf_pages": 0,
        },
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": f"{topic_key}:learner-v2:g{generation}",
        },
        "validation": {
            "state": "passed",
            "validated_on": date.today().isoformat(),
            "validator": "tools/publish_language_master_packages.py",
        },
        "refresh_profile": "qualifying-language-subject-package-v1",
    }
    record_path = (
        EXPORT_DIR
        / f"{topic_key}-learner-v2-g{generation}-{generated_on}-record.json"
    )
    record_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    index = output_dir.parent / "INDEX.md"
    index.write_text(
        f"# {config['title']}\n\n"
        f"- Current immutable generation: `g{generation}` ({generated_on})\n"
        f"- Complete skills guide: `{relative(guide_pdf)}`\n"
        f"- Question-only workbook: `{relative(workbook_pdf)}`\n"
        f"- Separate solutions: `{relative(solutions_pdf)}`\n"
        f"- Pages: guide {guide_metrics[0]}, workbook {workbook_metrics[0]}, "
        f"solutions {solutions_metrics[0]}\n"
        "- Practice papers: 3\n"
        "- Learning sessions: 0\n"
        "- Package contract: `qualifying-language-subject-package-v1`\n"
        "- Approved: no\n",
        encoding="utf-8",
    )
    record["_record_path"] = relative(record_path)
    record["_index_path"] = relative(index)
    return record


def update_tracker(records: list[dict[str, object]]) -> None:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    exports = tracker.get("exports")
    if tracker.get("schema_version") != 2 or not isinstance(exports, list):
        raise ValueError("Tracker must use schema v2.")
    clean_records = [
        {key: value for key, value in record.items() if not key.startswith("_")}
        for record in records
    ]
    replacements = {
        (record["topic_key"], record["variant"], int(record["generation"])): record
        for record in clean_records
    }
    retained = [
        item
        for item in exports
        if not (
            isinstance(item, dict)
            and (
                item.get("topic_key"),
                item.get("variant"),
                int(item.get("generation") or 1),
            )
            in replacements
        )
    ]
    updated = dict(tracker)
    updated["exports"] = [*retained, *clean_records]
    temporary = TRACKER.with_suffix(".language-packages.pending.json")
    temporary.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, TRACKER)


def main() -> int:
    records = [
        publish_subject(subject, config)
        for subject, config in CONFIGS.items()
    ]
    update_tracker(records)
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    completion = (
        EXPORT_DIR / f"qualifying-english-hindi-master-{DATE}-completion.json"
    )
    ledger = (
        EXPORT_DIR / f"qualifying-english-hindi-master-{DATE}-changed-files.txt"
    )
    changed = {
        "EXPORT-PDF-STATUS.json",
        "EXPORT-PDF-COMMAND-INDEX.md",
        "tools\\generate_language_master_packages.py",
        "tools\\publish_language_master_packages.py",
        "tools\\unicode_markdown_pdf.py",
        relative(completion),
        relative(ledger),
    }
    for record in records:
        changed.update(
            str(record[field])
            for field in (
                "main_pdf",
                "workbook",
                "solutions_pdf",
                "markdown",
                "workbook_markdown",
                "solutions_markdown",
                "_record_path",
                "_index_path",
            )
        )
    payload = {
        "schema_version": 1,
        "batch_id": f"qualifying-english-hindi-master-{DATE}",
        "scope": "Qualifying English and Qualifying Hindi only",
        "generated_on": DATE,
        "validated_at": datetime.now().astimezone().isoformat(),
        "result": "passed",
        "records": [
            {
                "record_id": record["record_id"],
                "subject": record["subject"],
                "approved": record["approved"],
                "metrics": record["format"],
            }
            for record in records
        ],
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
