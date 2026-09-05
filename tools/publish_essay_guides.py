"""Publish Essay-specific knowledge guides, workbooks and solution PDFs."""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_essay_common as common  # noqa: E402
import markdown_learning_pdf  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


DATE = os.environ.get("ESSAY_TOPIC_DATE", common.DATE)
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
KNOWLEDGE_ROOT = (
    ROOT / "upsc-ai-kit" / "knowledge" / "Essay" / "subject-wide-syllabus"
)
PDF_ROOT = ROOT / "notes" / "Essay" / "Subject-Wide-Syllabus"
INDEX = PDF_ROOT / "INDEX.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_config(topic_key: str) -> dict[str, object]:
    match = re.fullmatch(r"essay-(\d{2})", topic_key)
    if not match:
        raise ValueError(f"Invalid Essay topic key: {topic_key}")
    number = int(match.group(1))
    module = importlib.import_module(f"essay_{number:02d}_data")
    return getattr(module, f"TOPIC_{number:02d}")


def authoring_paths(topic_key: str) -> tuple[Path, Path, Path]:
    folder = KNOWLEDGE_ROOT / topic_key
    return (
        folder / f"{topic_key}_Knowledge-Guide.md",
        folder / f"{topic_key}_Practice-Workbook.md",
        folder / f"{topic_key}_Practice-Solutions.md",
    )


def output_paths(topic_key: str, generation: int) -> tuple[Path, Path, Path]:
    base = PDF_ROOT / topic_key / f"g{generation}"
    return (
        base / f"{topic_key}_Knowledge-Guide_{DATE}.pdf",
        base / f"{topic_key}_Practice-Workbook_{DATE}.pdf",
        base / f"{topic_key}_Practice-Solutions_{DATE}.pdf",
    )


def validate_markdown(
    topic_key: str,
    guide: Path,
    workbook: Path,
    solutions: Path,
) -> dict[str, int]:
    texts = [path.read_text(encoding="utf-8") for path in (guide, workbook, solutions)]
    combined = "\n".join(texts)
    if re.search(r"(?im)^### SESSION \d+", combined):
        raise ValueError(f"{topic_key}: learning-session headings remain.")
    if re.search(r"(?im)^### Q\d+\.", combined):
        raise ValueError(f"{topic_key}: MCQs remain.")
    question_count = texts[1].count("## TOPIC ")
    solution_count = texts[2].count("## SOLUTION ")
    if question_count < 1 or question_count != solution_count:
        raise ValueError(
            f"{topic_key}: workbook/solution count mismatch "
            f"({question_count}/{solution_count})."
        )
    if "## COMPLETE BASIC KNOWLEDGE" not in texts[0]:
        raise ValueError(f"{topic_key}: complete Basic knowledge is missing.")
    if "## COMPLETE ADVANCED KNOWLEDGE" not in texts[0]:
        raise ValueError(f"{topic_key}: complete Advanced knowledge is missing.")
    return {
        "practice_topics": question_count,
        "practice_solutions": solution_count,
        "solved_upsc_questions": texts[0].count("## SOLUTION "),
        "method_drills_retained": texts[0].count("### METHOD DRILL "),
    }


def render_pdf(source: Path, output: Path, topic_key: str) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    markdown_learning_pdf.build_pdf(
        source,
        output,
        topic_key=topic_key,
        repository_root=ROOT,
    )
    with fitz.open(output) as document:
        if document.page_count < 1:
            raise ValueError(f"Empty PDF: {output}")
        return document.page_count


def upsert_tracker(record: dict[str, object]) -> None:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    exports = tracker.get("exports")
    if tracker.get("schema_version") != 2 or not isinstance(exports, list):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
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
    temporary = TRACKER.with_suffix(".essay-guides.pending.json")
    temporary.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, TRACKER)


def write_index(records: list[dict[str, object]]) -> None:
    lines = [
        "# Essay Subject-Wide Syllabus",
        "",
        "Essay uses an Essay-specific format: one complete knowledge guide, a "
        "question-only workbook, and a separate solutions PDF. It contains no "
        "MCQs and no artificial learning-session sequence.",
        "",
        "| Topic | Knowledge guide | Practice workbook | Solutions | Approved |",
        "|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record['topic_key']} — {record['title']} | "
            f"`{record['main_pdf']}` | `{record['workbook']}` | "
            f"`{record['solutions_pdf']}` | No |"
        )
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def publish(topic_key: str) -> dict[str, object]:
    config = load_config(topic_key)
    guide, workbook, solutions = authoring_paths(topic_key)
    for path in (guide, workbook, solutions):
        if not path.is_file():
            raise FileNotFoundError(path)
    metrics = validate_markdown(topic_key, guide, workbook, solutions)
    generation = refresh.next_new_topic_generation(
        refresh.load_tracker(), topic_key
    )
    guide_pdf, workbook_pdf, solutions_pdf = output_paths(topic_key, generation)
    metrics["guide_pages"] = render_pdf(guide, guide_pdf, topic_key)
    metrics["workbook_pages"] = render_pdf(workbook, workbook_pdf, topic_key)
    metrics["solutions_pages"] = render_pdf(solutions, solutions_pdf, topic_key)
    command = next(
        item["learner_v2_command"]
        for item in json.loads(common.CATALOG.read_text(encoding="utf-8"))["topics"]
        if item.get("topic_key") == topic_key
    )
    record = {
        "record_id": f"{topic_key}:learner-v2:g{generation}",
        "topic_key": topic_key,
        "subject": "Essay",
        "section": "Subject-Wide-Syllabus",
        "title": config["title"],
        "variant": "learner-v2",
        "generation": generation,
        "command": command,
        "main_pdf": str(guide_pdf.relative_to(ROOT)).replace("/", "\\"),
        "workbook": str(workbook_pdf.relative_to(ROOT)).replace("/", "\\"),
        "solutions_pdf": str(solutions_pdf.relative_to(ROOT)).replace("/", "\\"),
        "markdown": str(guide.relative_to(ROOT)).replace("/", "\\"),
        "workbook_markdown": str(workbook.relative_to(ROOT)).replace("/", "\\"),
        "solutions_markdown": str(solutions.relative_to(ROOT)).replace("/", "\\"),
        "generated_on": DATE,
        "approved": False,
        "format": {
            "name": "essay-specific-guide-v1",
            "learning_sessions": 0,
            "mcqs": 0,
            **metrics,
        },
        "provenance": {
            "source_basic": str(Path(config["basic"]).relative_to(ROOT)).replace("/", "\\"),
            "source_advanced": str(Path(config["advanced"]).relative_to(ROOT)).replace("/", "\\"),
            "source_hashes": {
                str(path.relative_to(ROOT)).replace("/", "\\"): sha256(path)
                for path in (
                    Path(config["basic"]),
                    Path(config["advanced"]),
                    guide,
                    workbook,
                    solutions,
                )
            },
            "practice_profile": (
                "Question-only Essay workbook with a separate solutions PDF; "
                "no MCQs and no learning sessions."
            ),
        },
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": f"{topic_key}:learner-v2:g{generation}",
        },
        "validation": {
            "state": "passed",
            "validated_on": date.today().isoformat(),
            "validator": "tools/publish_essay_guides.py",
        },
        "refresh_profile": "essay-specific-guide-v1",
    }
    record_path = (
        EXPORT_DIR
        / f"{topic_key}-learner-v2-g{generation}-{DATE}-essay-guide-record.json"
    )
    record_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    upsert_tracker(record)
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_keys", nargs="+")
    args = parser.parse_args()
    records = [publish(key) for key in args.topic_keys]
    current = [
        item
        for item in refresh.load_tracker()["exports"]
        if isinstance(item, dict)
        and item.get("subject") == "Essay"
        and item.get("refresh_profile") == "essay-specific-guide-v1"
    ]
    if not current:
        current = records
    write_index(current)
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    print(json.dumps(records, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
