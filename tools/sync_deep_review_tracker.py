"""Synchronize the deep-review queue with the latest learner-v2 export library."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EXPORT_STATUS = ROOT / "EXPORT-PDF-STATUS.json"
MASTER = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
REVIEW_ROOT = ROOT / "notes" / "Final-Learning-Packages" / "_deep-content-review"
REVIEW_JSON = REVIEW_ROOT / "REVIEW-TRACKER.json"
REVIEW_MD = REVIEW_ROOT / "REVIEW-TRACKER.md"
README = REVIEW_ROOT / "README.md"
REPORT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "deep-review-tracker-sync-2026-08-31.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def pending_row(master_row: dict[str, Any]) -> dict[str, Any]:
    subject = master_row["subject"]
    section = master_row["section"]
    title = master_row["topic_title"]
    return {
        "sequence": 0,
        "batch": 0,
        "topic_key": master_row["topic_key"],
        "topic_title": title,
        "subject": subject,
        "section": section,
        "destination_folder": master_row["destination_folder"],
        "source_record_id": master_row["source_record_id"],
        "source_generation": master_row["source_generation"],
        "status": "pending",
        "artifacts": {
            "complete_learning_session": "pending",
            "solved_practice_workbook": "pending",
            "graphical_flowchart": "pending",
            "ascii_master_flowchart": "pending",
            "cross_artifact_reconciliation": "pending",
        },
        "scores": {
            "complete_learning_session": None,
            "solved_practice_workbook": None,
            "graphical_flowchart": None,
            "ascii_master_flowchart": None,
            "total": None,
        },
        "hard_gates": {
            "syllabus_core_complete": None,
            "facts_verified": None,
            "pyqs_verified": None,
            "model_answers_marks_worthy": None,
            "advanced_is_optional": None,
            "four_artifacts_consistent": None,
            "current_data_source_dated": None,
        },
        "issue_counts": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        "md_change_required": False,
        "md_change_ids": [],
        "evidence_ids": [],
        "review_started_at": None,
        "review_completed_at": None,
        "reviewer_notes": "",
        "review_command": (
            f"Review final package: {subject} — {section} — {title}"
        ),
    }


def latest_exports(status: dict[str, Any]) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for row in status["exports"]:
        if row.get("variant") != "learner-v2":
            continue
        current = latest.get(row["topic_key"])
        if current is None or int(row["generation"]) > int(current["generation"]):
            latest[row["topic_key"]] = row
    return latest


def subject_commands(topics: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter(row["subject"] for row in topics)
    return [
        {
            "subject": subject,
            "topic_count": count,
            "command": f"Review and repair final packages subject-wise: {subject}",
            "workflow": (
                "For each topic: review all four artifacts, report issues, fix "
                "sources and pipeline defects, create a new immutable generation, "
                "regenerate, validate, re-review, then continue."
            ),
        }
        for subject, count in sorted(counts.items())
    ]


def render_markdown(tracker: dict[str, Any]) -> str:
    summary = tracker["summary"]
    lines = [
        "# Final Learning Packages — Deep Content Review Tracker",
        "",
        "> Machine-readable tracker: [`REVIEW-TRACKER.json`](REVIEW-TRACKER.json)",
        "",
        "> Copy and send **one exact command at a time** from the final column.",
        "",
        "## Baseline",
        "",
        f"- Topics: **{tracker['topic_count']}**",
        (
            f"- Batches: **{tracker['batch_count']}** "
            "(five topics per batch; final batch may be smaller)"
        ),
        f"- Source master tracker: `{tracker['source_master_tracker']}`",
        f"- Source master timestamp: `{tracker['source_master_created_at']}`",
        "- Approval remains independent and pending until explicit topic approval.",
        "",
        "## Progress",
        "",
        f"- Pending: **{summary.get('pending', 0)}**",
        f"- In Review: **{summary.get('in_review', 0)}**",
        f"- Changes Suggested: **{summary.get('changes_suggested', 0)}**",
        f"- Revalidation Pending: **{summary.get('revalidation_pending', 0)}**",
        f"- Passed: **{summary.get('passed', 0)}**",
        f"- Blocked: **{summary.get('blocked', 0)}**",
        "",
        "## Subject-wise copy-paste commands",
        "",
        "| Subject | Topics | Copy-paste command |",
        "|---|---:|---|",
    ]
    for subject in tracker["subject_commands"]:
        lines.append(
            f"| {subject['subject']} | {subject['topic_count']} | "
            f"`{subject['command']}` |"
        )
    lines.extend(
        [
            "",
            "## Topic queue",
            "",
            (
                "| # | Batch | Subject | Topic | Generation | Session | Workbook | "
                "Graphical | ASCII | Score | Status | Copy-paste command |"
            ),
            "|---:|---:|---|---|---:|---|---|---|---|---:|---|---|",
        ]
    )
    for item in tracker["topics"]:
        artifacts = item["artifacts"]
        score = item["scores"].get("total")
        lines.append(
            f"| {item['sequence']} | {item['batch']} | {item['subject']} | "
            f"`{item['topic_key']}` — {item['topic_title']} | "
            f"g{item['source_generation']} | "
            f"{artifacts['complete_learning_session']} | "
            f"{artifacts['solved_practice_workbook']} | "
            f"{artifacts['graphical_flowchart']} | "
            f"{artifacts['ascii_master_flowchart']} | "
            f"{'—' if score is None else score} | {item['status']} | "
            f"`{item['review_command']}` |"
        )
    return "\n".join(lines) + "\n"


def update_readme(topic_count: int, batch_count: int) -> None:
    text = README.read_text(encoding="utf-8")
    text = re.sub(r"- Topics: \*\*\d+\*\*", f"- Topics: **{topic_count}**", text)
    text = re.sub(
        r"- Planned batches: \*\*\d+\*\*",
        f"- Planned batches: **{batch_count}**",
        text,
    )
    text = re.sub(
        r"- Initial state: every topic is `pending`",
        "- New tracker identities enter as `pending`; completed reviews retain their state",
        text,
    )
    README.write_text(text, encoding="utf-8")


def latest_exports_for_master(
    status: dict[str, Any],
    master_rows: list[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    """Scope synchronization to the already published MASTER catalogue."""
    latest_all = latest_exports(status)
    master_keys = {row["topic_key"] for row in master_rows}
    missing_latest = sorted(master_keys - set(latest_all))
    if missing_latest:
        raise ValueError(
            "MASTER topic keys are missing from latest learner-v2 exports: "
            + ", ".join(missing_latest)
        )
    return (
        {key: latest_all[key] for key in master_keys},
        sorted(set(latest_all) - master_keys),
    )


def sync() -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    status = load(EXPORT_STATUS)
    master = load(MASTER)
    review = load(REVIEW_JSON)
    master_rows = master["topics"]
    master_by_key = {row["topic_key"]: row for row in master_rows}
    latest, ignored_unpublished = latest_exports_for_master(status, master_rows)
    identity_errors = [
        key
        for key, row in master_by_key.items()
        if row["source_record_id"] != latest[key]["record_id"]
        or int(row["source_generation"]) != int(latest[key]["generation"])
    ]
    if identity_errors:
        raise ValueError(f"MASTER has stale identities: {identity_errors}")

    old_rows = {row["topic_key"]: row for row in review["topics"]}
    added: list[str] = []
    reset: list[str] = []
    rows: list[dict[str, Any]] = []
    for master_row in master_rows:
        key = master_row["topic_key"]
        old = old_rows.get(key)
        if old is None:
            row = pending_row(master_row)
            added.append(key)
        elif old["source_record_id"] != master_row["source_record_id"]:
            row = pending_row(master_row)
            reset.append(key)
        else:
            row = old
            row.update(
                {
                    "topic_title": master_row["topic_title"],
                    "subject": master_row["subject"],
                    "section": master_row["section"],
                    "destination_folder": master_row["destination_folder"],
                    "source_generation": master_row["source_generation"],
                }
            )
        rows.append(row)

    for sequence, row in enumerate(rows, 1):
        row["sequence"] = sequence
        row["batch"] = math.ceil(sequence / 5)

    subject_counts = dict(Counter(row["subject"] for row in master_rows))
    section_counts = dict(
        Counter(f"{row['subject']} — {row['section']}" for row in master_rows)
    )
    master.update(
        {
            "topic_count": len(master_rows),
            "subjects": subject_counts,
            "sections": section_counts,
            "updated_at": now,
        }
    )
    dump(MASTER, master)

    review.update(
        {
            "source_master_created_at": master.get("updated_at", master["created_at"]),
            "topic_count": len(rows),
            "batch_count": math.ceil(len(rows) / 5),
            "subject_commands": subject_commands(rows),
            "topics": rows,
            "summary": dict(Counter(row["status"] for row in rows)),
            "updated_at": now,
        }
    )
    dump(REVIEW_JSON, review)
    REVIEW_MD.write_text(render_markdown(review), encoding="utf-8")
    update_readme(review["topic_count"], review["batch_count"])

    report = {
        "schema_version": 1,
        "created_at": now,
        "latest_learner_v2_topics": len(latest),
        "master_topics": len(master_rows),
        "review_topics_before": len(old_rows),
        "review_topics_after": len(rows),
        "added_count": len(added),
        "added_topic_keys": added,
        "reset_count": len(reset),
        "reset_topic_keys": reset,
        "preserved_count": len(rows) - len(added) - len(reset),
        "summary": review["summary"],
        "subject_counts": subject_counts,
        "identity_mismatches": [],
        "ignored_unpublished_export_keys": ignored_unpublished,
        "approval_policy": review["approval_policy"],
        "result": "passed",
    }
    dump(REPORT, report)
    return report


def tracker_check_errors(
    status: dict[str, Any],
    master: dict[str, Any],
    review: dict[str, Any],
) -> tuple[list[str], dict[str, dict[str, Any]]]:
    latest = latest_exports(status)
    master_by_key = {row["topic_key"]: row for row in master["topics"]}
    review_by_key = {row["topic_key"]: row for row in review["topics"]}
    errors: list[str] = []
    if len(latest) != master["topic_count"]:
        errors.append("MASTER topic_count differs from latest exports.")
    if len(latest) != review["topic_count"]:
        errors.append("REVIEW topic_count differs from latest exports.")
    latest_keys = set(latest)
    master_keys = set(master_by_key)
    review_keys = set(review_by_key)
    for store, keys in (("MASTER", master_keys), ("REVIEW", review_keys)):
        missing = sorted(latest_keys - keys)
        unexpected = sorted(keys - latest_keys)
        if missing:
            errors.append(
                f"{store} is missing topic keys: {', '.join(missing)}."
            )
        if unexpected:
            errors.append(
                f"{store} has unexpected topic keys: {', '.join(unexpected)}."
            )
    for key, export in latest.items():
        master_row = master_by_key.get(key)
        review_row = review_by_key.get(key)
        if (
            master_row is not None
            and master_row["source_record_id"] != export["record_id"]
        ):
            errors.append(f"{key}: MASTER identity mismatch.")
        if (
            review_row is not None
            and review_row["source_record_id"] != export["record_id"]
        ):
            errors.append(f"{key}: REVIEW identity mismatch.")
    actual_summary = dict(Counter(row["status"] for row in review["topics"]))
    recorded_summary = {
        str(key): int(value)
        for key, value in (review.get("summary") or {}).items()
    }
    if actual_summary != recorded_summary:
        errors.append("REVIEW summary differs from topic states.")
    return errors, latest


def check() -> None:
    status = load(EXPORT_STATUS)
    master = load(MASTER)
    review = load(REVIEW_JSON)
    errors, latest = tracker_check_errors(status, master, review)
    if errors:
        raise SystemExit("\n".join(errors))
    print(
        f"PASS topics={len(latest)} pending={review['summary'].get('pending', 0)} "
        f"passed={review['summary'].get('passed', 0)}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        check()
    else:
        result = sync()
        print(
            f"Synced {result['review_topics_after']} topics; "
            f"added={result['added_count']} reset={result['reset_count']}."
        )


if __name__ == "__main__":
    main()
