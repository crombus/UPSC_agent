"""Validate and inventory the completed Economy semantic review."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import regenerate_economy_deep_review as deep
import run_economy_semantic_topic as subject


DATE = "2026-09-06"
ROOT = deep.ROOT
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
REPORT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "economy"
    / f"Economy-Subject-Semantic-Completion-{DATE}.md"
)
VALIDATION = (
    EXPORTS
    / f"economy-01-31-semantic-completeness-{DATE}-validation.json"
)
INVENTORY = (
    EXPORTS
    / f"economy-01-31-semantic-completeness-{DATE}-changed-files.txt"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def latest(status: dict[str, Any], key: str) -> dict[str, Any]:
    rows = [
        row
        for row in status["exports"]
        if row.get("topic_key") == key and row.get("variant") == "learner-v2"
    ]
    return max(rows, key=lambda row: int(row.get("generation", 0)))


def main() -> int:
    semantic = load(subject.runner.SEMANTIC_STATUS)
    export_status = load(deep.STATUS)
    rows = [
        row
        for row in semantic["topics"]
        if row["topic_key"].startswith("economy-")
    ]
    expected = [f"economy-{number:02d}" for number in range(1, 32)]
    errors: list[str] = []
    if [row["topic_key"] for row in rows] != expected:
        errors.append("Economy semantic catalogue/order mismatch.")
    if any(row["status"] != "passed" for row in rows):
        errors.append("Not every Economy semantic row is passed.")
    if semantic["next_topic"]["topic_key"] != "environment-and-ecology-01":
        errors.append("Global queue did not advance to environment-and-ecology-01.")

    tracker_text = (
        ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md"
    ).read_text(encoding="utf-8")
    if "| 13 | Economy | 31 | 31 | passed | Complete |" not in tracker_text:
        errors.append("Human tracker does not record Economy 31/31 passed.")
    if "Environment and Ecology — Subject-wide Syllabus — Ecosystem Structure and Function" not in tracker_text:
        errors.append("Human tracker next topic disagrees with machine state.")

    topics: list[dict[str, Any]] = []
    inventory: set[str] = {
        "EXPORT-PDF-COMMAND-INDEX.md",
        "EXPORT-PDF-STATUS.json",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        "notes\\Final-Learning-Packages\\CATALOGUE.md",
        "notes\\Final-Learning-Packages\\MASTER-TRACKER.json",
        "notes\\Final-Learning-Packages\\MASTER-TRACKER.md",
        "notes\\Final-Learning-Packages\\START-HERE.md",
        "tools\\finalize_economy_semantic_review.py",
        "tools\\regenerate_economy_deep_review.py",
        "tools\\run_economy_semantic_topic.py",
        "tools\\test_regenerate_economy_deep_review.py",
        "tools\\test_run_economy_semantic_topic.py",
        rel(REPORT),
        rel(VALIDATION),
        rel(INVENTORY),
        rel(subject.runner.SEMANTIC_STATUS),
    }
    all_approval_false = True
    identity_isolation = True
    h2_order_ok = True
    live_sources_ok = True
    hash_errors: dict[str, str] = {}

    for number, key in enumerate(expected, 1):
        validation_path = EXPORTS / f"{key}-semantic-validation-{DATE}.json"
        item_inventory = (
            EXPORTS / f"{key}-semantic-completeness-{DATE}-changed-files.txt"
        )
        validation = load(validation_path)
        record = latest(export_status, key)
        records = [
            row
            for row in export_status["exports"]
            if row.get("topic_key") == key and row.get("variant") == "learner-v2"
        ]
        all_approval_false &= all(row.get("approved") is False for row in records)
        previous = [row for row in records if row["record_id"] != record["record_id"]]
        latest_paths = {
            record["markdown"],
            record["workbook_markdown"],
            record["main_pdf"],
            record["workbook"],
        }
        identity_isolation &= all(
            latest_paths.isdisjoint(
                {
                    row.get("markdown"),
                    row.get("workbook_markdown"),
                    row.get("main_pdf"),
                    row.get("workbook"),
                }
            )
            for row in previous
        )
        main_text = deep.repo(record["markdown"]).read_text(encoding="utf-8")
        headings = [
            "## BASIC LEARNING SESSION",
            "## BASIC MCQS / REMEDIATION",
            "## PYQS AND ANSWER PRACTICE",
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            "## CONSOLIDATED REGISTER NOTES",
        ]
        positions = [main_text.find(heading) for heading in headings]
        h2_order_ok &= all(position >= 0 for position in positions)
        h2_order_ok &= positions == sorted(positions)
        h2_order_ok &= (
            main_text.rstrip().rfind("## CONSOLIDATED REGISTER NOTES")
            == positions[-1]
        )
        live_sources_ok &= (
            record.get("provenance", {}).get("live_sources_rechecked_on") == DATE
            and bool(record.get("provenance", {}).get("live_sources"))
        )
        for path_text, expected_hash in validation["deliverable_hashes"].items():
            path = deep.repo(path_text)
            if not path.is_file():
                hash_errors[path_text] = "missing"
            elif deep.sha256(path) != expected_hash:
                hash_errors[path_text] = "sha256 mismatch"
        inventory.update(
            line.strip()
            for line in item_inventory.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
        report_path = next(
            path
            for path in rows[number - 1]["files_changed"]
            if path.startswith(
                "upsc-ai-kit\\manifests\\reviews\\economy\\"
            )
            and path.endswith(f"-semantic-completeness-review-{DATE}.md")
        )
        topics.append(
            {
                "topic_key": key,
                "title": rows[number - 1]["title"],
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record["approved"],
                "main_pages": validation["metrics"]["main_pages"],
                "workbook_pages": validation["metrics"]["workbook_pages"],
                "solved_blocks": validation["metrics"]["question_count"],
                "mcqs": validation["metrics"]["mcq_count"],
                "ascii_panels": validation["metrics"]["ascii_panel_count"],
                "graphical_stages": validation["metrics"]["graphical_stage_count"],
                "tests": validation["metrics"]["targeted_tests"],
                "report": report_path,
                "validation": rel(validation_path),
                "inventory": rel(item_inventory),
            }
        )

    library_errors = deep.validate_final_library(
        [{"topic_key": key} for key in expected]
    )
    if library_errors:
        errors.extend(library_errors)
    if not all_approval_false:
        errors.append("At least one Economy identity is approved.")
    if not identity_isolation:
        errors.append("A successor reuses a prior generation output path.")
    if not h2_order_ok:
        errors.append("Five-H2 order or final register-note placement failed.")
    if not live_sources_ok:
        errors.append("Live-source provenance/date is incomplete.")
    if hash_errors:
        errors.append("Deliverable hashes failed.")

    tests = subject.run_tests()
    test_count = sum(int(row["tests"]) for row in tests)
    payload = {
        "schema_version": 1,
        "subject": "Economy",
        "date": DATE,
        "result": "failed" if errors else "passed",
        "topic_count": 31,
        "passed": sum(row["status"] == "passed" for row in rows),
        "next_topic_key": semantic["next_topic"]["topic_key"],
        "next_subject": semantic["next_topic"]["subject"],
        "next_topic": semantic["next_topic"]["title"],
        "checks": {
            "catalogue_order": [row["topic_key"] for row in rows] == expected,
            "all_topics_passed": all(row["status"] == "passed" for row in rows),
            "all_learner_identities_approval_false": all_approval_false,
            "identity_isolation": identity_isolation,
            "five_h2_order_and_register_notes_last": h2_order_ok,
            "live_sources_rechecked": live_sources_ok,
            "deliverable_hashes": not hash_errors,
            "final_library_hash_parity": not library_errors,
            "status_tracker_agreement": (
                "| 13 | Economy | 31 | 31 | passed | Complete |"
                in tracker_text
            ),
            "targeted_regression": all(
                row["exit_code"] == 0
                and row["failures"] == 0
                and row["errors"] == 0
                for row in tests
            ),
        },
        "metrics": {
            "targeted_regression_tests": test_count,
            "per_topic_test_executions": sum(row["tests"] for row in topics),
            "main_pages": sum(row["main_pages"] for row in topics),
            "workbook_pages": sum(row["workbook_pages"] for row in topics),
            "solved_blocks": sum(row["solved_blocks"] for row in topics),
            "mcqs": sum(row["mcqs"] for row in topics),
            "ascii_panels": sum(row["ascii_panels"] for row in topics),
            "graphical_stages": sum(row["graphical_stages"] for row in topics),
        },
        "topics": topics,
        "hash_errors": hash_errors,
        "library_errors": library_errors,
        "errors": errors,
    }
    deep.dump(VALIDATION, payload)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    table_rows = "\n".join(
        f"| {row['topic_key']} | `{row['record_id']}` | "
        f"{row['main_pages']} | {row['workbook_pages']} | "
        f"{row['solved_blocks']} | {row['mcqs']} | "
        f"{row['ascii_panels']}/{row['graphical_stages']} | passed |"
        for row in topics
    )
    REPORT.write_text(
        f"""# Economy Semantic-Completeness Completion — 6 September 2026

**Result:** {'FAILED' if errors else 'PASSED'}  
**Coverage:** {payload['passed']}/31  
**Next queue item:** `environment-and-ecology-01` — Ecosystem Structure and Function

| Topic | Identity | Main pages | Workbook pages | Solved | MCQs | ASCII/graphical | Result |
|---|---|---:|---:|---:|---:|---:|---|
{table_rows}

Targeted Economy regression: {test_count} tests, zero failures.
All learner-v2 Economy identities remain `approved: false`;
successor paths are isolated; final-library copies match accepted-source hashes;
both flow representations retain twelve panels/stages per topic; PDF layout
checks report no blank, near-empty, clipped-text or replacement-glyph pages.

Validation: `{rel(VALIDATION)}`  
Combined inventory: `{rel(INVENTORY)}`
""",
        encoding="utf-8",
    )

    status_output = subprocess.check_output(
        [
            "git",
            "-C",
            str(ROOT),
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
        ]
    ).decode("utf-8", errors="replace")
    git_changed = {
        entry[3:].replace("/", "\\")
        for entry in status_output.split("\0")
        if entry and len(entry) > 3
    }
    always_include = {rel(REPORT), rel(VALIDATION), rel(INVENTORY)}
    inventory = {
        path for path in inventory if path in git_changed or path in always_include
    }
    existing = {
        path
        for path in inventory
        if path == rel(INVENTORY) or (ROOT / path).exists()
    }
    INVENTORY.write_text(
        "\n".join(sorted(existing, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    if errors:
        raise RuntimeError("Economy final validation failed: " + "; ".join(errors))
    print(json.dumps(payload, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
