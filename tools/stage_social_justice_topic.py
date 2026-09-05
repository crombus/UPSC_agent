"""Stage one Social Justice learner-v2 topic without touching the tracker.

Runs the shared new-topic generation path, then writes the standard staged-record
and validation manifests used by the atomic finalisation step. It never mutates
`EXPORT-PDF-STATUS.json` or any index.

The tracker guard below is deliberately scoped to the staged topic. A whole-file
hash comparison also fails when an unrelated process appends a record for a
different subject, which proves nothing about this topic and destroys a
completed render. `refresh.process_new_topic_spec` already applies the correct
rule internally, so this module applies the same one: after generation the live
tracker must still carry no learner-v2 record for this topic key, and the next
new-topic generation for that key must still be the generation that was just
staged.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import refresh_all_v2_learning_sessions as refresh  # noqa: E402


EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
DATE = "2026-09-02"


def assert_topic_tracker_untouched(topic_key: str, generation: int) -> None:
    """Fail when stage-only generation changed this topic's tracker state."""

    live = refresh.load_tracker()
    existing = [
        item
        for item in live["exports"]
        if isinstance(item, dict)
        and item.get("topic_key") == topic_key
        and item.get("variant") == refresh.V2_VARIANT
    ]
    if existing:
        raise refresh.RefreshError(
            f"{topic_key}: tracker gained a learner-v2 record during "
            "stage-only generation."
        )
    if refresh.next_new_topic_generation(live, topic_key) != generation:
        raise refresh.RefreshError(
            f"{topic_key}: tracker history for this topic changed during "
            "stage-only generation."
        )


def stage(topic_key: str, *, tests_passed: int, tests_scope: str) -> dict[str, object]:
    spec_path = EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json"
    if not spec_path.is_file():
        raise refresh.RefreshError(f"New-topic spec is missing: {spec_path}")
    tracker = refresh.load_tracker()
    row, record = refresh.process_new_topic_spec(spec_path, tracker)
    assert_topic_tracker_untouched(topic_key, int(record["generation"]))
    if not row.get("passed"):
        raise refresh.RefreshError(f"{topic_key}: validation failed: {row['errors']}")

    validation_path = EXPORT_DIR / f"{topic_key}-learner-v2-{DATE}-validation.json"
    staged_path = EXPORT_DIR / f"{topic_key}-learner-v2-{DATE}-staged-records.json"
    payload = {
        "schema_version": 1,
        "id": validation_path.stem,
        "validated_on": datetime.now().astimezone().isoformat(),
        "selection": topic_key,
        "topic_count": 1,
        "passed": True,
        "errors": [],
        "tests": {"passed": tests_passed, "scope": tests_scope},
        "topics": [row],
    }
    validation_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    refresh.write_staged_records(
        [record],
        staged_path,
        selection=topic_key,
        record_set_id=f"{topic_key}-learner-v2-{DATE}",
    )
    return {
        "topic_key": topic_key,
        "generation": record["generation"],
        "record_id": record["record_id"],
        "validation": str(validation_path.relative_to(ROOT)),
        "staged_records": str(staged_path.relative_to(ROOT)),
        "main_pdf": record["main_pdf"],
        "workbook": record["workbook"],
        "markdown": record["markdown"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    parser.add_argument("--tests-passed", type=int, default=0)
    parser.add_argument(
        "--tests-scope",
        default="Social Justice sequential generator suite and shared refresh suites",
    )
    args = parser.parse_args()
    result = stage(
        args.topic_key,
        tests_passed=args.tests_passed,
        tests_scope=args.tests_scope,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
