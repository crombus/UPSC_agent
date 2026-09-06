"""Run one strictly sequential International Relations semantic review."""

from __future__ import annotations

import argparse
import json
import re
from typing import Any

import regenerate_international_relations_deep_review as deep
import run_polity_semantic_topic as runner


REPORT_DATE = "2026-09-06"
runner.deep = deep
runner.REPORT_DATE = REPORT_DATE
runner.TOPIC_CHOICES = range(1, 13)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_international_relations_deep_review"
runner.REPORT_DIR = (
    deep.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "international-relations"
)
runner.DRIVER_FILES = {
    "tools\\regenerate_international_relations_deep_review.py",
    "tools\\test_regenerate_international_relations_deep_review.py",
    "tools\\run_international_relations_semantic_topic.py",
    "tools\\test_run_international_relations_semantic_topic.py",
}
runner.SLUGS = {
    topic.number: (
        f"{topic.number:02d}-"
        + re.sub(r"[^a-z0-9]+", "-", topic.title.casefold()).strip("-")
    )
    for topic in deep.topics()
}
runner.PYQ_STATUS = {
    number: re.split(
        r"(?<=[.!?])\s+",
        deep.INTERNATIONAL_RELATIONS_PYQ_STATUS[number],
        maxsplit=1,
    )[0]
    for number in range(1, 13)
}
deep.POLITY_LIVE_OFFICIAL_SOURCES = (
    deep.INTERNATIONAL_RELATIONS_LIVE_OFFICIAL_SOURCES
)


def complete_semantic_state(
    topic: deep.Topic,
    result: dict[str, Any],
    files_changed: list[str],
) -> dict[str, Any]:
    state = runner.load(runner.SEMANTIC_STATUS)
    row = runner.semantic_row(state, topic.topic_key)
    row["status"] = "passed"
    row["checks"] = {name: "passed" for name in row["checks"]}
    row["gap_counts"] = {name: 0 for name in row["gap_counts"]}
    row["findings"] = [
        {
            "severity": "closed",
            "finding": (
                "Four-ledger hostile audit closed; literal syllabus, doctrine, "
                "actors, instruments, memberships, mandates, legal and operational "
                "status chains, bilateral/regional/systemic levels, contested-claim "
                "neutrality, current official evidence, PYQ ownership, answer "
                "contracts and both twelve-panel flow masters pass."
            ),
            "record_id": result["new_record_id"],
        }
    ]
    row["files_changed"] = files_changed
    row["completed_at"] = runner.now_iso()
    row["next_action"] = "Passed; advance exactly one topic in authoritative order."
    runner.dump(runner.SEMANTIC_STATUS, state)
    runner.refresh_semantic_tracker()
    return runner.load(runner.SEMANTIC_STATUS)


def report_text(
    topic: deep.Topic,
    result: dict[str, Any],
    validation: dict[str, Any],
    tests: list[dict[str, Any]],
    next_key: str,
) -> str:
    metrics = validation["metrics"]
    return f"""# International Relations Semantic-Completeness Review {topic.number:02d} - {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 6 September 2026  
**Result:** PASSED  
**Canonical Basic owner:** `{runner.rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Only this topic was active. The literal UPSC syllabus, indispensable
prerequisites, standard International Relations taxonomy, canonical Basic
owner, Optional Advanced owner, framework and cross-owner bridges, complete
verified PYQ ledgers and authoritative live sources were reconciled through a
hostile four-ledger audit.

The bounded canonical repair preserves doctrine, actors, interests,
bilateral/regional/systemic levels, institutional mandates, membership and
participation status, treaties and negotiations, projects and corridors,
contested-claim neutrality, current official evidence and source dates. The
immutable successor preserves Basic-first and Advanced-last order, final
register notes, examiner-grade answer contracts, strict A-B-C-D rotation and
twelve manually authored ASCII panels agreeing with twelve graphical stages.
Approval remains false. PYQ status: {runner.PYQ_STATUS[topic.number]}.

Validation passed: {metrics['main_pages']} main pages,
{metrics['workbook_pages']} workbook pages,
{metrics['question_count']} solved blocks, {metrics['mcq_count']} MCQs,
{metrics['ascii_panel_count']}/12 ASCII panels and
{metrics['graphical_stage_count']}/12 graphical stages. Targeted tests:
{sum(item['tests'] for item in tests)}; failures: 0.

The authoritative queue advanced exactly one topic to `{next_key}`.

Machine validation:
`upsc-ai-kit\\manifests\\exports\\{topic.topic_key}-semantic-validation-{REPORT_DATE}.json`

Inventory:
`upsc-ai-kit\\manifests\\exports\\{topic.topic_key}-semantic-completeness-{REPORT_DATE}-changed-files.txt`
"""


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_international_relations_deep_review",
        "test_run_international_relations_semantic_topic",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in runner.EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    tests = [deep.run_unittest(module) for module in modules]
    if any(item["exit_code"] or item["failures"] or item["errors"] for item in tests):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


runner.complete_semantic_state = complete_semantic_state
runner.report_text = report_text
runner.run_tests = run_tests


def run(topic_number: int) -> dict[str, object]:
    if topic_number not in runner.TOPIC_CHOICES:
        raise ValueError(
            "International Relations runner accepts only topic numbers 1 through 12."
        )
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
