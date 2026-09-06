#!/usr/bin/env python3
"""Collect final learner Markdown packages into one browsable directory."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MASTER_TRACKER = REPO_ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
EXPORT_STATUS = REPO_ROOT / "EXPORT-PDF-STATUS.json"
DESTINATION = REPO_ROOT / "learning_package_final"

SPECIAL_PACKAGES = {
    "Essay": (
        REPO_ROOT / "upsc-ai-kit" / "knowledge" / "Essay" / "subject-wide-syllabus" / "master"
    ),
    "Qualifying English": (
        REPO_ROOT / "upsc-ai-kit" / "knowledge" / "Qualifying-English" / "subject-wide-package"
    ),
    "Qualifying Hindi": (
        REPO_ROOT / "upsc-ai-kit" / "knowledge" / "Qualifying-Hindi" / "subject-wide-package"
    ),
}


def slug(value: str, max_length: int = 80) -> str:
    value = re.sub(r'[<>:"/\\|?*]+', "-", value.strip())
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    value = value.strip("-.") or "untitled"
    return value[:max_length].rstrip("-.")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_workbook(record: dict, markdown: Path) -> Path:
    workbook = record.get("workbook_markdown")
    if workbook:
        return REPO_ROOT / workbook

    candidate = markdown.with_name(
        markdown.name.replace(
            "_Complete-Learning-Session_",
            "_Solved-Practice-Workbook_",
        )
    )
    return candidate


def copy_file(source: Path, destination: Path, records: list[dict], kind: str) -> None:
    if not source.is_file():
        raise FileNotFoundError(f"Missing {kind}: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    if sha256(source) != sha256(destination):
        raise RuntimeError(f"Hash mismatch after copying {source}")
    records.append(
        {
            "kind": kind,
            "destination": destination.relative_to(REPO_ROOT).as_posix(),
            "source": source.relative_to(REPO_ROOT).as_posix(),
            "sha256": sha256(destination),
            "bytes": destination.stat().st_size,
        }
    )


def main() -> None:
    if DESTINATION.exists():
        raise FileExistsError(
            f"{DESTINATION} already exists; remove or rename it before rebuilding."
        )

    master = json.loads(MASTER_TRACKER.read_text(encoding="utf-8"))
    status = json.loads(EXPORT_STATUS.read_text(encoding="utf-8"))
    exports = {record["record_id"]: record for record in status["exports"]}
    copied: list[dict] = []
    topic_rows: list[dict] = []

    for topic in master["topics"]:
        # Essay has a newer subject-wide guide/workbook/solutions package.
        if topic["subject"] == "Essay":
            continue

        record_id = topic["source_record_id"]
        if record_id not in exports:
            raise KeyError(f"Missing export record: {record_id}")
        record = exports[record_id]
        learning_source = REPO_ROOT / record["markdown"]
        workbook_source = resolve_workbook(record, learning_source)

        topic_folder = (
            DESTINATION
            / slug(topic["subject"])
            / slug(topic["section"])
            / f'{topic["catalogue_number"]:02d}-{slug(topic["topic_title"], 72)}'
        )
        learning_destination = topic_folder / "Learning-Session.md"
        workbook_destination = topic_folder / "Solved-Practice-Workbook.md"
        copy_file(learning_source, learning_destination, copied, "learning_session")
        copy_file(workbook_source, workbook_destination, copied, "solved_practice_workbook")
        topic_rows.append(
            {
                "subject": topic["subject"],
                "section": topic["section"],
                "catalogue_number": topic["catalogue_number"],
                "topic_key": topic["topic_key"],
                "topic_title": topic["topic_title"],
                "source_record_id": record_id,
                "folder": topic_folder.relative_to(DESTINATION).as_posix(),
            }
        )

    for subject, source_folder in SPECIAL_PACKAGES.items():
        destination_folder = DESTINATION / slug(subject) / "Subject-Wide-Package"
        special_files = sorted(source_folder.glob("*.md"))
        if not special_files:
            raise FileNotFoundError(f"No Markdown files found in {source_folder}")
        for source in special_files:
            copy_file(source, destination_folder / source.name, copied, "subject_wide_package")

    counts = Counter(row["subject"] for row in topic_rows)
    readme_lines = [
        "# Final Learning Packages",
        "",
        "This folder provides one browsable location for the final Markdown learning sessions",
        "and solved-practice workbooks selected by `notes/Final-Learning-Packages/MASTER-TRACKER.json`.",
        "The original source files remain unchanged in their canonical locations.",
        "",
        "Essay, Qualifying English, and Qualifying Hindi use their final subject-wide",
        "guide/workbook/solutions packages instead of artificial topic learning sessions.",
        "",
        "## Inventory",
        "",
        "| Subject | Final topics | Markdown files |",
        "|---|---:|---:|",
    ]
    for subject in sorted(counts):
        readme_lines.append(f"| {subject} | {counts[subject]} | {counts[subject] * 2} |")
    for subject, source_folder in SPECIAL_PACKAGES.items():
        file_count = len(list(source_folder.glob("*.md")))
        readme_lines.append(f"| {subject} | Subject-wide package | {file_count} |")
    readme_lines.extend(
        [
            "",
            f"Standard final topics: **{len(topic_rows)}**",
            f"Total copied Markdown files: **{len(copied)}**",
            "",
            "See `MANIFEST.json` for every destination, canonical source path, file size,",
            "and SHA-256 checksum.",
            "",
        ]
    )
    (DESTINATION / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")

    manifest = {
        "schema_version": 1,
        "purpose": "Consolidated copies of final learning-session and workbook Markdown files.",
        "selection_source": MASTER_TRACKER.relative_to(REPO_ROOT).as_posix(),
        "export_source": EXPORT_STATUS.relative_to(REPO_ROOT).as_posix(),
        "standard_topic_count": len(topic_rows),
        "copied_markdown_count": len(copied),
        "topics": topic_rows,
        "files": copied,
    }
    (DESTINATION / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    expected_files = len(copied) + 2
    actual_files = sum(1 for path in DESTINATION.rglob("*") if path.is_file())
    if actual_files != expected_files:
        raise RuntimeError(f"Expected {expected_files} files, found {actual_files}")

    print(f"Created {DESTINATION.relative_to(REPO_ROOT)}")
    print(f"Standard topics: {len(topic_rows)}")
    print(f"Copied Markdown files: {len(copied)}")
    print(f"Total files including index and manifest: {actual_files}")


if __name__ == "__main__":
    main()
