"""Validate and inventory the completed Environment and Ecology semantic review."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


DATE = "2026-09-06"
ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
SEMANTIC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
REPORT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "environment-and-ecology"
    / f"Environment-and-Ecology-Subject-Semantic-Completion-{DATE}.md"
)
VALIDATION = (
    EXPORTS
    / f"environment-and-ecology-01-28-semantic-completeness-{DATE}-validation.json"
)
INVENTORY = (
    EXPORTS
    / f"environment-and-ecology-01-28-semantic-completeness-{DATE}-changed-files.txt"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def latest(status: dict[str, Any], key: str) -> dict[str, Any]:
    rows = [
        row
        for row in status["exports"]
        if row.get("topic_key") == key and row.get("variant") == "learner-v2"
    ]
    return max(rows, key=lambda row: int(row.get("generation", 0)))


def run_tests() -> tuple[int, list[str]]:
    modules = [
        "test_run_environment_and_ecology_semantic_topic",
        *[
            f"test_generate_environment_and_ecology_{number:02d}_sequential"
            for number in range(1, 25)
        ],
        "test_generate_environment_and_ecology_25_28_sequential",
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    errors: list[str] = []
    count = 0
    for module in modules:
        result = subprocess.run(
            [sys.executable, "-m", "unittest", module],
            cwd=ROOT / "tools",
            capture_output=True,
            text=True,
        )
        count += int(result.stdout.count("\n")) or 1
        if result.returncode:
            errors.append(f"{module}: {result.stderr[-2000:]}")
    return count, errors


def main() -> int:
    semantic = load(SEMANTIC)
    export_status = load(STATUS)
    expected = [f"environment-and-ecology-{number:02d}" for number in range(1, 29)]
    rows = [
        row
        for row in semantic["topics"]
        if row["topic_key"].startswith("environment-and-ecology-")
    ]
    errors: list[str] = []
    if [row["topic_key"] for row in rows] != expected:
        errors.append("Environment catalogue/order mismatch.")
    if any(row["status"] != "passed" for row in rows):
        errors.append("Not every Environment topic passed.")
    if semantic["next_topic"]["topic_key"] != "science-and-technology-01":
        errors.append("Global queue did not advance to science-and-technology-01.")

    tracker_text = (
        ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md"
    ).read_text(encoding="utf-8")
    if "| 14 | Environment and Ecology | 28 | 28 | passed | Complete |" not in tracker_text:
        errors.append("Human tracker does not record Environment 28/28 passed.")

    inventory: set[str] = {
        "EXPORT-PDF-COMMAND-INDEX.md",
        "EXPORT-PDF-STATUS.json",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        "notes\\Final-Learning-Packages\\CATALOGUE.md",
        "notes\\Final-Learning-Packages\\MASTER-TRACKER.json",
        "notes\\Final-Learning-Packages\\MASTER-TRACKER.md",
        "notes\\Final-Learning-Packages\\START-HERE.md",
        "tools\\environment_semantic_runtime.py",
        "tools\\finalize_environment_and_ecology_semantic_review.py",
        "tools\\run_environment_and_ecology_semantic_topic.py",
        "tools\\test_run_environment_and_ecology_semantic_topic.py",
        rel(SEMANTIC),
        rel(REPORT),
        rel(VALIDATION),
        rel(INVENTORY),
    }
    topics: list[dict[str, Any]] = []
    approval_false = True
    h2_order_ok = True
    hash_errors: dict[str, str] = {}
    headings = [
        "## BASIC LEARNING SESSION",
        "## BASIC MCQS / REMEDIATION",
        "## PYQS AND ANSWER PRACTICE",
        "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "## CONSOLIDATED REGISTER NOTES",
    ]

    for key in expected:
        validation_path = EXPORTS / f"{key}-semantic-validation-{DATE}.json"
        item_inventory = (
            EXPORTS / f"{key}-semantic-completeness-{DATE}-changed-files.txt"
        )
        validation = load(validation_path)
        record = latest(export_status, key)
        approval_false &= all(
            row.get("approved") is False
            for row in export_status["exports"]
            if row.get("topic_key") == key and row.get("variant") == "learner-v2"
        )
        main_text = (ROOT / record["markdown"]).read_text(encoding="utf-8")
        positions = [main_text.find(heading) for heading in headings]
        h2_order_ok &= (
            all(position >= 0 for position in positions)
            and positions == sorted(positions)
            and main_text.rstrip().rfind(headings[-1]) == positions[-1]
        )
        for path_text, digest in validation["deliverable_hashes"].items():
            path = ROOT / path_text
            if not path.is_file():
                hash_errors[path_text] = "missing"
            elif sha256(path) != digest:
                hash_errors[path_text] = "sha256 mismatch"
        inventory.update(
            line.strip()
            for line in item_inventory.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
        metrics = validation["metrics"]
        topics.append(
            {
                "topic_key": key,
                "title": next(row["title"] for row in rows if row["topic_key"] == key),
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record["approved"],
                "main_pages": metrics["main_pages"],
                "workbook_pages": metrics["workbook_pages"],
                "solved_blocks": metrics["question_count"],
                "mcqs": metrics["mcq_count"],
                "ascii_panels": metrics["ascii_panel_count"],
                "graphical_stages": metrics["graphical_stage_count"],
                "tests": metrics["targeted_tests"],
                "validation": rel(validation_path),
                "inventory": rel(item_inventory),
            }
        )

    if not approval_false:
        errors.append("At least one Environment learner identity is approved.")
    if not h2_order_ok:
        errors.append("Five-H2 order or final register-note placement failed.")
    if hash_errors:
        errors.append("Deliverable hash validation failed.")
    test_count, test_errors = run_tests()
    errors.extend(test_errors)

    payload = {
        "schema_version": 1,
        "subject": "Environment and Ecology",
        "date": DATE,
        "result": "failed" if errors else "passed",
        "topic_count": 28,
        "passed": sum(row["status"] == "passed" for row in rows),
        "next_topic_key": semantic["next_topic"]["topic_key"],
        "next_subject": semantic["next_topic"]["subject"],
        "next_topic": semantic["next_topic"]["title"],
        "checks": {
            "catalogue_order": [row["topic_key"] for row in rows] == expected,
            "all_topics_passed": all(row["status"] == "passed" for row in rows),
            "all_learner_identities_approval_false": approval_false,
            "five_h2_order_and_register_notes_last": h2_order_ok,
            "deliverable_hashes": not hash_errors,
            "status_tracker_agreement": (
                "| 14 | Environment and Ecology | 28 | 28 | passed | Complete |"
                in tracker_text
            ),
            "targeted_regression": not test_errors,
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
        "errors": errors,
    }
    VALIDATION.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    rows_md = "\n".join(
        f"| {row['topic_key']} | `{row['record_id']}` | {row['main_pages']} | "
        f"{row['workbook_pages']} | {row['solved_blocks']} | {row['mcqs']} | "
        f"{row['ascii_panels']}/{row['graphical_stages']} | {row['tests']} |"
        for row in topics
    )
    REPORT.write_text(
        f"""# Environment and Ecology Subject Semantic Completion

**Date:** 6 September 2026  
**Result:** {'PASSED' if not errors else 'FAILED'}  
**Coverage:** {payload['passed']}/28  
**Next global queue item:** `{payload['next_topic_key']}` — {payload['next_topic']}

| Topic | Identity | Main pages | Workbook pages | Solved | MCQs | ASCII/graphical | Tests |
|---|---|---:|---:|---:|---:|---:|---:|
{rows_md}

Combined validation: `{rel(VALIDATION)}`  
Combined inventory: `{rel(INVENTORY)}`
""",
        encoding="utf-8",
    )
    INVENTORY.write_text(
        "\n".join(sorted(inventory, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
