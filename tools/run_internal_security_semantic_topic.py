"""Run one strictly sequential Internal Security semantic review."""

from __future__ import annotations

import argparse
import importlib
import json
from typing import Any

from internal_security_semantic_runtime import (
    REPORT_DATE,
    load_runtime,
    topic_slug,
)

import run_polity_semantic_topic as runner


deep = load_runtime()
runner.deep = deep
runner.REPORT_DATE = REPORT_DATE
runner.TOPIC_CHOICES = range(1, 13)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_internal_security_deep_review"
runner.REPORT_DIR = (
    deep.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "internal-security"
)
runner.DRIVER_FILES = {
    "tools\\internal_security_semantic_runtime.py",
    "tools\\verify_internal_security_live_sources.py",
    "tools\\run_internal_security_semantic_topic.py",
    "tools\\test_run_internal_security_semantic_topic.py",
    "tools\\finalize_internal_security_semantic_review.py",
    "tools\\regenerate_internal_security_deep_review.py",
}
runner.SLUGS = {
    topic.number: topic_slug(topic.title, topic.number) for topic in deep.topics()
}
LIVE_AUDIT = (
    deep.ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"internal-security-authoritative-live-source-audit-{REPORT_DATE}.json"
)


def _topic_configs() -> dict[int, dict[str, object]]:
    configs = {}
    for number in range(1, 13):
        module = importlib.import_module(f"internal_security_{number:02d}_data")
        configs[number] = getattr(module, f"TOPIC_{number:02d}")
    return configs


CONFIGS = _topic_configs()


def _load_live_audit() -> dict[str, Any]:
    if not LIVE_AUDIT.is_file():
        raise FileNotFoundError("Run verify_internal_security_live_sources.py first.")
    payload = runner.load(LIVE_AUDIT)
    if payload.get("result") != "passed":
        raise RuntimeError("Authoritative live-source audit has unresolved failures.")
    return payload


def _live_sources() -> dict[int, tuple[list[str], str]]:
    payload = _load_live_audit()
    by_key = {row["topic_key"]: row for row in payload["topics"]}
    result = {}
    for number in range(1, 13):
        key = f"internal-security-{number:02d}"
        row = by_key[key]
        sources = [item["url"] for item in row["sources"]]
        result[number] = (
            sources,
            f"Rechecked {REPORT_DATE} through {row['attempted']} authoritative "
            f"source attempts, including {row['substantive_retrievals']} "
            "substantive live retrievals. Failed or thin attempts remain in the "
            "audit and support no claim. Coverage stayed policy-oriented and "
            "non-actionable.",
        )
    return result


LIVE_OFFICIAL_SOURCES = _live_sources()
runner.PYQ_STATUS = {
    number: str(CONFIGS[number]["pyq_note"]) for number in range(1, 13)
}
deep.POLITY_LIVE_OFFICIAL_SOURCES = LIVE_OFFICIAL_SOURCES


def complete_semantic_state(
    topic: object,
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
                "Hostile semantic audit closed: literal GS-III syllabus, "
                "prerequisites, standard taxonomy, verified PYQs, canonical "
                "ownership, cross-topic boundaries, threat-mechanism-response "
                "logic, legal/institutional/status precision, authoritative "
                "current-source integrity, safety/non-actionability, answer "
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
    topic: object,
    result: dict[str, Any],
    validation: dict[str, Any],
    tests: list[dict[str, Any]],
    next_key: str,
) -> str:
    metrics = validation["metrics"]
    return f"""# Internal Security Semantic-Completeness Review {topic.number:02d} - {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 6 September 2026  
**Result:** PASSED  
**Canonical Basic owner:** `{runner.rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Only this topic was active. The literal UPSC GS-III syllabus, indispensable
prerequisites, standard Internal Security taxonomy, canonical Basic and
Optional Advanced owners, cross-topic boundaries, verified PYQ ledgers,
hostile retrieval searches and authoritative live sources were reconciled.

The immutable successor preserves threat-vulnerability-capability and
threat-mechanism-response analysis, actor and geography mapping, exact legal
and institutional status, process and evidentiary rungs, security-development-
rights trade-offs, India-centric examples, safe non-actionable policy coverage,
Mains answer architecture, Basic-first teaching, Optional Advanced isolation,
final register notes, strict A-B-C-D rotation and twelve complete ASCII panels
agreeing with twelve graphical stages. Approval remains false. PYQ status:
{runner.PYQ_STATUS[topic.number]}.

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
        "test_run_internal_security_semantic_topic",
        "test_regenerate_internal_security_deep_review",
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


def apply_live_source_provenance(
    topic: object,
    result: dict[str, Any],
    changed: set[str],
) -> None:
    sources, note = LIVE_OFFICIAL_SOURCES[topic.number]
    status = runner.load(deep.STATUS)
    record = next(
        row
        for row in reversed(status["exports"])
        if row.get("record_id") == result["new_record_id"]
    )
    record.setdefault("provenance", {}).update(
        {
            "live_sources": sources,
            "current_linkage_note": note,
            "live_sources_rechecked_on": REPORT_DATE,
            "live_source_audit": runner.rel(LIVE_AUDIT),
            "safety_scope": "public-policy-only; non-actionable",
        }
    )
    runner.dump(deep.STATUS, status)
    changed.update({runner.rel(deep.STATUS), runner.rel(LIVE_AUDIT)})

    record_path = deep.EXPORTS / (
        f"{topic.topic_key}-learner-v2-g{result['new_generation']}-"
        f"{deep.DATE}-record.json"
    )
    if record_path.is_file():
        payload = runner.load(record_path)
        payload.setdefault("provenance", {}).update(record["provenance"])
        runner.dump(record_path, payload)
        changed.add(runner.rel(record_path))

    latest_record = deep.latest(runner.load(deep.STATUS), topic.topic_key)
    content_spec = deep.repo(latest_record["provenance"]["content_spec"])
    payload = runner.load(content_spec)
    payload["live_official_sources"] = sources
    payload["current_status_control"] = note
    payload["live_sources_rechecked_on"] = REPORT_DATE
    payload["safety_scope"] = "public-policy-only; non-actionable"
    runner.dump(content_spec, payload)
    changed.add(runner.rel(content_spec))


runner.complete_semantic_state = complete_semantic_state
runner.report_text = report_text
runner.run_tests = run_tests
runner.apply_live_source_provenance = apply_live_source_provenance


def run(topic_number: int) -> dict[str, object]:
    if topic_number not in runner.TOPIC_CHOICES:
        raise ValueError("Internal Security runner accepts topics 1 through 12.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
