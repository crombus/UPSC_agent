"""Prove and record the batch completion manifest for one Indian Society run.

Reads the per-topic completion manifests, tracker records, ASCII panel specs and
graphical specs for a sequential Indian Society learner-v2 batch, re-proves every
hard gate from the live artifacts, and writes a batch completion manifest plus a
batch changed-files manifest. It is read-only with respect to
`EXPORT-PDF-STATUS.json` and every index.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import notions_style_ascii_master as ascii_master  # noqa: E402
import record_indian_society_completion as topic_record  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


DATE = topic_record.DATE
EXPORT_DIR = topic_record.EXPORT_DIR


def topic_payload(topic_key: str) -> dict[str, object]:
    records = topic_record.tracker_records(topic_key)
    if len(records) != 1:
        raise SystemExit(
            f"{topic_key}: expected exactly one learner-v2 tracker record, "
            f"found {len(records)}."
        )
    record = records[0]
    generation = int(record["generation"])
    completion_path = (
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-completion.json"
    )
    if not completion_path.is_file():
        raise SystemExit(f"{topic_key}: per-topic completion manifest is missing.")
    completion = json.loads(completion_path.read_text(encoding="utf-8"))
    proof = topic_record.prove(topic_key, record)
    failed = [name for name, ok in proof["hard_gates"].items() if not ok]
    return {
        "topic_key": topic_key,
        "record_id": record["record_id"],
        "variant": record["variant"],
        "generation": generation,
        "approved": bool(record.get("approved")),
        "result": "failed" if failed else "passed",
        "hard_gates_passed": sum(1 for ok in proof["hard_gates"].values() if ok),
        "hard_gates_total": len(proof["hard_gates"]),
        "failed_gates": failed,
        "metrics": proof["metrics"],
        "per_topic_completion": refresh.relative(completion_path.resolve()),
        "per_topic_changed_files": refresh.relative(
            (
                EXPORT_DIR
                / f"{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
            ).resolve()
        ),
        "per_topic_result_recorded": completion.get("result"),
        "main_pdf": record["main_pdf"],
        "workbook_pdf": record["workbook"],
        "assembled_markdown": record["markdown"],
        "workbook_markdown": record["workbook_markdown"],
    }


def batch_changed_files(
    topic_keys: list[str],
    batch_id: str,
    also_changed: list[str],
) -> list[str]:
    paths: set[str] = set()
    for topic_key in topic_keys:
        records = topic_record.tracker_records(topic_key)
        paths.update(
            topic_record.changed_files(records[0], also_changed=also_changed)
        )
    for name in (
        f"{batch_id}-completion.json",
        f"{batch_id}-changed-files.txt",
    ):
        paths.add(refresh.relative((EXPORT_DIR / name).resolve()))
    return sorted(paths, key=str.casefold)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_keys", nargs="+")
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--scope", default="")
    parser.add_argument(
        "--also-changed",
        action="append",
        default=[],
        help=(
            "Repository-relative path of an additional file this batch created "
            "or modified, such as an authoring tool or its regression test."
        ),
    )
    args = parser.parse_args()

    topics = [topic_payload(topic_key) for topic_key in args.topic_keys]
    failed = [item["topic_key"] for item in topics if item["result"] != "passed"]
    specs = ascii_master.load_manual_topic_specs(
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    )
    payload = {
        "schema_version": 1,
        "batch_id": args.batch_id,
        "scope": args.scope or args.batch_id,
        "generated_on": DATE,
        "validated_at": datetime.now().astimezone().isoformat(),
        "result": "failed" if failed else "passed",
        "sequence": {
            "strict_order": list(args.topic_keys),
            "topic_count": len(args.topic_keys),
            "one_topic_at_a_time": True,
        },
        "tracker": {
            "tracker_path": "EXPORT-PDF-STATUS.json",
            "new_topic_records": [item["record_id"] for item in topics],
            "unique_records": len({item["record_id"] for item in topics})
            == len(topics),
            "approvals_false": all(item["approved"] is False for item in topics),
        },
        "shared_ascii_coverage": {
            "authored_topics": len(specs),
            "authored_panels": sum(len(spec.panels) for spec in specs.values()),
            "integrity_errors": ascii_master.manual_spec_integrity_errors(ROOT, specs),
        },
        "aggregate": {
            "main_pdf_pages": sum(
                int(item["metrics"]["main_pdf_pages"]) for item in topics
            ),
            "workbook_pdf_pages": sum(
                int(item["metrics"]["workbook_pdf_pages"]) for item in topics
            ),
            "mcqs": sum(int(item["metrics"]["mcq_count"]) for item in topics),
            "learning_sessions": sum(
                int(item["metrics"]["learner_session_count"]) for item in topics
            ),
            "ascii_panels": sum(
                int(item["metrics"]["ascii_panel_count"]) for item in topics
            ),
            "graphical_stages": sum(
                int(item["metrics"]["graphical_stage_count"]) for item in topics
            ),
        },
        "topics": topics,
        "errors": [f"topic failed hard gates: {key}" for key in failed],
    }
    completion_path = EXPORT_DIR / f"{args.batch_id}-completion.json"
    changed_path = EXPORT_DIR / f"{args.batch_id}-changed-files.txt"
    completion_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    changed_path.write_text(
        "\n".join(
            batch_changed_files(
                list(args.topic_keys),
                args.batch_id,
                list(args.also_changed),
            )
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in payload.items()
                if key != "topics"
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
