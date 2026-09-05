"""Stage one Internal Security learner-v2 topic without publishing tracker state."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import refresh_all_v2_learning_sessions as refresh  # noqa: E402


EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
DATE = os.environ.get("INTERNAL_SECURITY_TOPIC_DATE", "2026-09-04")


def stage(topic_key: str, *, tests_passed: int, tests_scope: str) -> dict[str, object]:
    spec_path = EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json"
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    expected_generation = int(spec["expected_generation"])
    tracker = refresh.load_tracker()
    before = [
        item for item in tracker["exports"]
        if isinstance(item, dict)
        and item.get("topic_key") == topic_key
        and item.get("variant") == refresh.V2_VARIANT
    ]
    row, record = refresh.process_new_topic_spec(spec_path, tracker)
    if not row.get("passed"):
        raise refresh.RefreshError(f"{topic_key}: validation failed: {row['errors']}")
    if int(record["generation"]) != expected_generation:
        raise refresh.RefreshError(
            f"{topic_key}: staged generation {record['generation']} != {expected_generation}"
        )
    live = refresh.load_tracker()
    after = [
        item for item in live["exports"]
        if isinstance(item, dict)
        and item.get("topic_key") == topic_key
        and item.get("variant") == refresh.V2_VARIANT
    ]
    if [item.get("record_id") for item in after] != [item.get("record_id") for item in before]:
        raise refresh.RefreshError(f"{topic_key}: stage-only tracker guard failed.")

    validation_path = EXPORT_DIR / f"{topic_key}-learner-v2-{DATE}-validation.json"
    staged_path = EXPORT_DIR / f"{topic_key}-learner-v2-{DATE}-staged-records.json"
    record_path = EXPORT_DIR / f"{topic_key}-learner-v2-g{expected_generation}-{DATE}-record.json"
    result_path = record_path.with_name(
        record_path.name.removesuffix("-record.json") + "-validation.json"
    )
    validation_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "id": validation_path.stem,
                "validated_on": datetime.now().astimezone().isoformat(),
                "selection": topic_key,
                "topic_count": 1,
                "passed": True,
                "errors": [],
                "tests": {"passed": tests_passed, "scope": tests_scope},
                "topics": [row],
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    refresh.write_staged_records(
        [record],
        staged_path,
        selection=topic_key,
        record_set_id=f"{topic_key}-learner-v2-{DATE}",
    )
    record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result_path.write_text(
        json.dumps(
            {
                "topic_key": topic_key,
                "generation": expected_generation,
                "identity": record["record_id"],
                "approved": False,
                "source_validation": str(validation_path.relative_to(ROOT)),
                "published": False,
            },
            ensure_ascii=False,
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    return {
        "topic_key": topic_key,
        "generation": expected_generation,
        "record_id": record["record_id"],
        "validation": str(validation_path.relative_to(ROOT)),
        "staged_records": str(staged_path.relative_to(ROOT)),
        "record": str(record_path.relative_to(ROOT)),
        "main_pdf": record["main_pdf"],
        "workbook": record["workbook"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    parser.add_argument("--tests-passed", type=int, default=0)
    parser.add_argument(
        "--tests-scope",
        default="Internal Security topic generator and shared refresh/manual-flow suites",
    )
    args = parser.parse_args()
    print(json.dumps(stage(args.topic_key, tests_passed=args.tests_passed, tests_scope=args.tests_scope), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
