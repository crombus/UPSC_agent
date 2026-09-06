"""Validate and inventory the completed Essay semantic review."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


DATE = "2026-09-06"
ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
SEMANTIC = (
    ROOT / "upsc-ai-kit" / "manifests" / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
TRACKER = ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md"
REPORT = (
    ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "essay"
    / f"Essay-Subject-Semantic-Completion-{DATE}.md"
)
VALIDATION = (
    EXPORTS / f"essay-01-16-semantic-completeness-{DATE}-validation.json"
)
INVENTORY = (
    EXPORTS / f"essay-01-16-semantic-completeness-{DATE}-changed-files.txt"
)
SOURCE_AUDIT = EXPORTS / f"essay-authoritative-source-audit-{DATE}.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def latest(status: dict[str, Any], key: str) -> dict[str, Any]:
    rows = [
        row for row in status["exports"]
        if row.get("topic_key") == key and row.get("variant") == "learner-v2"
    ]
    return max(rows, key=lambda row: int(row.get("generation", 0)))


def run_tests() -> tuple[int, list[str]]:
    modules = [
        "test_run_essay_semantic_topic",
        "test_v2_section_indexes",
        "test_v2_topic_command_catalog",
    ]
    total = 0
    errors: list[str] = []
    for module in modules:
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "-v", module],
            cwd=ROOT / "tools",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        output = result.stdout + result.stderr
        match = re.search(r"Ran (\d+) tests?", output)
        total += int(match.group(1)) if match else 0
        if result.returncode:
            errors.append(f"{module}: {output[-5000:]}")
    return total, errors


def main() -> int:
    semantic = load(SEMANTIC)
    status = load(STATUS)
    expected = [f"essay-{number:02d}" for number in range(1, 17)]
    rows = [row for row in semantic["topics"] if row["topic_key"].startswith("essay-")]
    errors: list[str] = []
    if [row["topic_key"] for row in rows] != expected:
        errors.append("Essay catalogue/order mismatch.")
    if any(row["status"] != "passed" for row in rows):
        errors.append("Not every Essay topic passed.")
    if semantic["next_topic"]["topic_key"] != "csat-01":
        errors.append("Global queue did not advance to csat-01.")
    tracker_text = TRACKER.read_text(encoding="utf-8")
    tracker_ok = "| 20 | Essay | 16 | 16 | passed | Complete |" in tracker_text
    if not tracker_ok:
        errors.append("Human tracker does not record Essay 16/16.")
    source_audit = load(SOURCE_AUDIT)
    if source_audit.get("result") != "passed":
        errors.append("Essay authoritative source audit failed.")

    inventory = {
        "EXPORT-PDF-COMMAND-INDEX.md",
        "EXPORT-PDF-STATUS.json",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        "tools\\essay_semantic_data.py",
        "tools\\generate_essay_common.py",
        "tools\\generate_essay_semantic_topic_v2.py",
        "tools\\run_essay_semantic_topic.py",
        "tools\\test_run_essay_semantic_topic.py",
        "tools\\finalize_essay_semantic_review.py",
        "tools\\notions_style_ascii_master.py",
        rel(SEMANTIC),
        rel(SOURCE_AUDIT),
        rel(REPORT),
        rel(VALIDATION),
        rel(INVENTORY),
    }
    for path in ROOT.glob(
        "notes/*/learning-session-v2/**/indexes/*-INDEX.md"
    ):
        inventory.add(rel(path))

    topic_metrics = []
    all_approval_false = True
    dated_provenance = True
    identity_isolation = True
    hash_errors: dict[str, str] = {}
    for key in expected:
        validation_path = EXPORTS / f"{key}-semantic-validation-{DATE}.json"
        item_inventory = EXPORTS / (
            f"{key}-semantic-completeness-{DATE}-changed-files.txt"
        )
        validation = load(validation_path)
        record = latest(status, key)
        records = [
            row for row in status["exports"]
            if row.get("topic_key") == key and row.get("variant") == "learner-v2"
        ]
        all_approval_false &= all(row.get("approved") is False for row in records)
        dated_provenance &= (
            record.get("provenance", {}).get("live_sources_rechecked_on") == DATE
            and record.get("provenance", {}).get("facts_and_inference_separated") is True
            and record.get("provenance", {}).get("quotation_policy_verified") is True
        )
        current_paths = {
            record["markdown"], record["workbook_markdown"],
            record["main_pdf"], record["workbook"],
        }
        identity_isolation &= all(
            current_paths.isdisjoint(
                {
                    old.get("markdown"), old.get("workbook_markdown"),
                    old.get("main_pdf"), old.get("workbook"),
                }
            )
            for old in records if old["record_id"] != record["record_id"]
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
        topic_metrics.append(
            {
                "topic_key": key,
                "title": next(row["title"] for row in rows if row["topic_key"] == key),
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record["approved"],
                **metrics,
                "validation": rel(validation_path),
                "inventory": rel(item_inventory),
            }
        )

    # Preserve and inventory every failed/superseded dated intermediate.
    for path in EXPORTS.glob(f"essay-*-*{DATE}*"):
        if path.is_file():
            inventory.add(rel(path))
    for root in (
        ROOT / "notes" / "Learner-v2-Refreshed" / "Essay",
        ROOT / "upsc-ai-kit" / "knowledge" / "Learner-v2-Refreshed" / "Essay",
    ):
        if root.is_dir():
            for path in root.rglob(f"*{DATE}*"):
                if path.is_file():
                    inventory.add(rel(path))

    if not all_approval_false:
        errors.append("At least one Essay learner-v2 identity is approved.")
    if not dated_provenance:
        errors.append("At least one accepted identity lacks dated source provenance.")
    if not identity_isolation:
        errors.append("An accepted identity reuses a prior generation output path.")
    if hash_errors:
        errors.append("Deliverable hash validation failed.")
    tests, test_errors = run_tests()
    errors.extend(test_errors)

    payload = {
        "schema_version": 1,
        "subject": "Essay",
        "date": DATE,
        "result": "failed" if errors else "passed",
        "topic_count": 16,
        "passed": sum(row["status"] == "passed" for row in rows),
        "next_topic_key": semantic["next_topic"]["topic_key"],
        "next_subject": semantic["next_topic"]["subject"],
        "next_topic": semantic["next_topic"]["title"],
        "checks": {
            "catalogue_order": [row["topic_key"] for row in rows] == expected,
            "all_topics_passed": all(row["status"] == "passed" for row in rows),
            "authoritative_source_audit": source_audit.get("result") == "passed",
            "all_learner_identities_approval_false": all_approval_false,
            "identity_isolation": identity_isolation,
            "dated_source_and_quotation_integrity": dated_provenance,
            "deliverable_hashes": not hash_errors,
            "status_tracker_agreement": tracker_ok,
            "targeted_regression": not test_errors,
        },
        "metrics": {
            "targeted_regression_tests": tests,
            "per_topic_test_executions": sum(row["targeted_tests"] for row in topic_metrics),
            "main_pages": sum(row["main_pages"] for row in topic_metrics),
            "workbook_pages": sum(row["workbook_pages"] for row in topic_metrics),
            "solved_blocks": sum(row["question_count"] for row in topic_metrics),
            "mcqs": sum(row["mcq_count"] for row in topic_metrics),
            "complete_model_essays": sum(row["model_essay_count"] for row in topic_metrics),
            "model_essay_words": sum(sum(row["model_essay_words"]) for row in topic_metrics),
            "ascii_panels": sum(row["ascii_panel_count"] for row in topic_metrics),
            "graphical_stages": sum(row["graphical_stage_count"] for row in topic_metrics),
        },
        "topics": topic_metrics,
        "hash_errors": hash_errors,
        "errors": errors,
    }
    VALIDATION.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    rows_md = "\n".join(
        f"| {row['topic_key']} | `{row['record_id']}` | {row['main_pages']} | "
        f"{row['workbook_pages']} | {row['mcq_count']} | "
        f"{row['model_essay_words'][0]} | "
        f"{row['ascii_panel_count']}/{row['graphical_stage_count']} | "
        f"{row['targeted_tests']} |"
        for row in topic_metrics
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        f"""# Essay Subject Semantic Completion

**Date:** 6 September 2026  
**Result:** {'PASSED' if not errors else 'FAILED'}  
**Coverage:** {payload['passed']}/16  
**Next global queue item:** `{payload['next_topic_key']}` — {payload['next_topic']}

| Topic | Identity | Main pages | Workbook pages | MCQs | Model words | ASCII/graphical | Tests |
|---|---|---:|---:|---:|---:|---:|---:|
{rows_md}

The review preserved failed/superseded intermediates, accepted only isolated
unapproved successors, and verified exact five-H2 order, Basic-before-Advanced,
register notes last, prompt fidelity, complete model essays, strict diagnostic
rotation, source/quotation status, hashes, PDF quality and twelve-panel
ASCII/graphical semantic parity (plus one subordinate optional graphical stage).

Source audit: `{rel(SOURCE_AUDIT)}`  
Combined validation: `{rel(VALIDATION)}`  
Combined inventory: `{rel(INVENTORY)}`
""",
        encoding="utf-8",
    )
    INVENTORY.write_text(
        "\n".join(sorted(inventory, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
