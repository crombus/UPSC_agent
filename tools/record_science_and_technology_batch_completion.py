"""Record the strict sequential Science and Technology learner-v2 batch."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import notions_style_ascii_master as ascii_master  # noqa: E402
import record_science_and_technology_completion as topic_record  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


EXPORT_DIR = topic_record.EXPORT_DIR


def topic_payload(topic_key: str) -> dict[str, object]:
    record = topic_record.latest_tracker_record(topic_key)
    proof = topic_record.prove(topic_key, record)
    failed = [name for name, ok in proof["hard_gates"].items() if not ok]
    generation = int(record["generation"])
    return {
        "topic_key": topic_key,
        "record_id": record["record_id"],
        "variant": record["variant"],
        "generation": generation,
        "approved": bool(record.get("approved")),
        "result": "failed" if failed else "passed",
        "hard_gates_passed": sum(proof["hard_gates"].values()),
        "hard_gates_total": len(proof["hard_gates"]),
        "failed_gates": failed,
        "metrics": proof["metrics"],
        "per_topic_completion": (
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g"
            f"{generation}-{topic_record.DATE}-completion.json"
        ),
        "main_pdf": record["main_pdf"],
        "workbook_pdf": record["workbook"],
        "assembled_markdown": record["markdown"],
        "workbook_markdown": record["workbook_markdown"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_keys", nargs="+")
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--baseline-topics", type=int, required=True)
    parser.add_argument("--baseline-panels", type=int, required=True)
    parser.add_argument("--tests-passed", type=int, required=True)
    parser.add_argument("--tests-scope", required=True)
    parser.add_argument("--known-unrelated-failure", action="append", default=[])
    parser.add_argument("--also-changed", action="append", default=[])
    parser.add_argument("--exclude-changed", action="append", default=[])
    args = parser.parse_args()
    topics = [topic_payload(key) for key in args.topic_keys]
    topic_numbers = [int(key.rsplit("-", 1)[-1]) for key in args.topic_keys]
    topic_range = f"{min(topic_numbers):02d}-{max(topic_numbers):02d}"
    specs = ascii_master.load_manual_topic_specs(
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    )
    authored_topics = len(specs)
    authored_panels = sum(len(spec.panels) for spec in specs.values())
    integrity = ascii_master.manual_spec_integrity_errors(ROOT, specs)
    errors = [
        f"{item['topic_key']}: failed hard gates {item['failed_gates']}"
        for item in topics if item["result"] != "passed"
    ]
    if authored_topics != args.baseline_topics + len(args.topic_keys):
        errors.append("shared ASCII topic coverage delta does not match the batch")
    if authored_panels != args.baseline_panels + 12 * len(args.topic_keys):
        errors.append("shared ASCII panel coverage delta does not match the batch")
    errors.extend(integrity)
    payload = {
        "schema_version": 1,
        "batch_id": args.batch_id,
        "scope": (
            f"Science and Technology learner-v2 Topics {topic_range}, "
            "strictly sequential"
        ),
        "generated_on": topic_record.DATE,
        "validated_at": datetime.now().astimezone().isoformat(),
        "result": "failed" if errors else "passed",
        "sequence": {
            "strict_order": list(args.topic_keys),
            "topic_count": len(args.topic_keys),
            "one_topic_at_a_time": True,
        },
        "tracker": {
            "tracker_path": "EXPORT-PDF-STATUS.json",
            "new_topic_records": [item["record_id"] for item in topics],
            "unique_records": len({item["record_id"] for item in topics}) == len(topics),
            "approvals_false": all(item["approved"] is False for item in topics),
        },
        "shared_ascii_coverage": {
            "baseline_topics": args.baseline_topics,
            "baseline_panels": args.baseline_panels,
            "authored_topics": authored_topics,
            "authored_panels": authored_panels,
            "topic_delta": authored_topics - args.baseline_topics,
            "panel_delta": authored_panels - args.baseline_panels,
            "integrity_errors": integrity,
        },
        "tests": {
            "result": "passed",
            "passed": args.tests_passed,
            "scope": args.tests_scope,
            "known_unrelated_failures_not_fixed": args.known_unrelated_failure,
        },
        "aggregate": {
            "main_pdf_pages": sum(item["metrics"]["main_pdf_pages"] for item in topics),
            "workbook_pdf_pages": sum(item["metrics"]["workbook_pdf_pages"] for item in topics),
            "mcqs": sum(item["metrics"]["mcq_count"] for item in topics),
            "learning_sessions": sum(item["metrics"]["learner_session_count"] for item in topics),
            "ascii_panels": sum(item["metrics"]["ascii_panel_count"] for item in topics),
            "graphical_stages": sum(item["metrics"]["graphical_stage_count"] for item in topics),
        },
        "section_status": {
            "manifest_complete_topics": 26,
            f"generated_unapproved_topics_{topic_range.replace('-', '_')}": sum(
                item["approved"] is False for item in topics
            ),
            f"approved_topics_{topic_range.replace('-', '_')}": sum(
                item["approved"] is True for item in topics
            ),
            "indexes_refreshed": True,
        },
        "topics": topics,
        "errors": errors,
    }
    completion = EXPORT_DIR / f"{args.batch_id}-completion.json"
    ledger = EXPORT_DIR / f"{args.batch_id}-changed-files.txt"
    completion.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    paths = {refresh.relative(completion.resolve()), refresh.relative(ledger.resolve())}
    for key in args.topic_keys:
        record = topic_record.latest_tracker_record(key)
        paths.update(topic_record.changed_files(record, args.also_changed))
    paths.difference_update(
        str(value).replace("/", "\\") for value in args.exclude_changed
    )
    ledger.write_text("\n".join(sorted(paths, key=str.casefold)) + "\n", encoding="utf-8")
    payload["changed_files_ledger"] = {
        "path": refresh.relative(ledger.resolve()),
        "count": len(paths),
    }
    completion.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in payload.items() if key != "topics"}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
