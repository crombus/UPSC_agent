"""Roll back one Internal Security learner-v2 generation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import refresh_all_v2_learning_sessions as refresh  # noqa: E402


SECTION = "Subject-Wide-Syllabus"
DATE = os.environ.get("INTERNAL_SECURITY_TOPIC_DATE", "2026-09-04")


def rollback(topic_key: str) -> dict[str, object]:
    tracker = refresh.load_tracker()
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == topic_key
        and record.get("variant") == refresh.V2_VARIANT
    ]
    removed_dirs: list[str] = []
    for record in records:
        generation = int(record.get("generation") or 1)
        topic = refresh.Topic(
            key=topic_key,
            subject="Internal-Security",
            section=SECTION,
            topic_folder=topic_key,
            title=str(record.get("topic_key")),
            generation=generation,
            record_id=str(record.get("record_id") or ""),
            markdown=refresh.repo_path(str(record["markdown"])),
            main_pdf=refresh.repo_path(str(record["main_pdf"])),
            workbook=refresh.repo_path(str(record["workbook"])),
            source_record={},
        )
        paths = refresh.output_paths(topic, generation, generation_date=DATE)
        for directory in (paths.knowledge_dir, paths.notes_dir, paths.flowchart_dir):
            if directory.is_dir():
                shutil.rmtree(directory)
                removed_dirs.append(refresh.relative(directory))

    tracker["exports"] = [
        record
        for record in tracker["exports"]
        if not (
            isinstance(record, dict)
            and record.get("topic_key") == topic_key
            and record.get("variant") == refresh.V2_VARIANT
        )
    ]
    refresh.TRACKER.write_text(
        json.dumps(tracker, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return {
        "topic_key": topic_key,
        "removed_records": [str(record.get("record_id")) for record in records],
        "removed_directories": removed_dirs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    args = parser.parse_args()
    print(json.dumps(rollback(args.topic_key), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
