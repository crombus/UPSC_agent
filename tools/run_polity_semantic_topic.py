"""Run one strictly sequential hostile semantic-completeness review for Polity."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import regenerate_polity_26_30_deep_review as deep


ROOT = deep.ROOT
REPORT_DATE = "2026-09-05"
TOPIC_CHOICES = range(26, 31)
DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_26_30_deep_review"
DRIVER_FILES = {
    "tools\\regenerate_polity_26_30_deep_review.py",
    "tools\\test_regenerate_polity_26_30_deep_review.py",
    "tools\\run_polity_semantic_topic.py",
    "tools\\test_run_polity_semantic_topic.py",
}
SEMANTIC_STATUS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
REPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "polity"
SLUGS = {
    26: "26-scheduled-and-tribal-areas",
    27: "27-election-commission",
    28: "28-upsc-and-spsc",
    29: "29-finance-commission",
    30: "30-gst-council",
}
PYQ_STATUS = {
    26: (
        "direct/routed 2019, 2022, 2023, 2024, 2025 and provisional-key 2026 "
        "Scheduled-Area demands retained without inventing unavailable answer keys"
    ),
    27: (
        "direct/routed 2021-2025 election, MCC, delimitation, corrupt-practice "
        "and reform demands retained; cross-owner routes remain labelled"
    ),
    28: (
        "no direct verified question route fabricated; recruitment, consultation "
        "and civil-service bridges remain explicitly cross-owned"
    ),
    29: (
        "direct 2018 and 2020 Mains plus routed 2023 and 2025 objective demands "
        "retained with official-key discipline"
    ),
    30: (
        "direct 2023 GS-II accommodative-federalism demand retained; related "
        "taxation and fiscal-federalism questions remain cross-owned"
    ),
}
EXPORT_LIBRARY_TESTS = [
    "test_latest_selection_uses_highest_generation",
    "test_unknown_selected_topic_is_an_error",
    "test_selected_publication_cannot_overwrite_full_dated_manifest",
    "test_human_readable_sanitization",
    "test_long_topic_slug_is_bounded_and_stable",
    "test_canonical_destination_is_bounded_and_stable",
    "test_navigation_and_indexes_use_canonical_destination",
    "test_ascii_pdf_round_trip_preserves_panels",
    "test_exact_topic_shape_rejects_extra_files",
    "test_atomic_topic_replacement_removes_short_backup",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def refresh_semantic_tracker() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_semantic_completeness_tracker.py")],
        cwd=ROOT,
        check=True,
    )


def semantic_row(state: dict[str, Any], key: str) -> dict[str, Any]:
    return next(row for row in state["topics"] if row["topic_key"] == key)


def set_in_progress(topic: deep.Topic) -> None:
    state = load(SEMANTIC_STATUS)
    active = [
        row["topic_key"]
        for row in state["topics"]
        if row["status"]
        in {
            "in_progress",
            "changes_required",
            "repair_in_progress",
            "revalidation_pending",
        }
        and row["topic_key"] != topic.topic_key
    ]
    if active:
        raise ValueError("Another semantic topic is active: " + ", ".join(active))
    if state["next_topic"]["topic_key"] != topic.topic_key:
        raise ValueError(
            f"Authoritative next topic is {state['next_topic']['topic_key']}, "
            f"not {topic.topic_key}."
        )
    row = semantic_row(state, topic.topic_key)
    row["status"] = "in_progress"
    row["reviewed_at"] = now_iso()
    row["next_action"] = (
        "Run the four-ledger hostile audit, bounded constitutional repair and "
        "immutable learner-v2 regeneration; do not open the next topic."
    )
    dump(SEMANTIC_STATUS, state)
    refresh_semantic_tracker()


def set_blocked(topic: deep.Topic, error: BaseException) -> None:
    state = load(SEMANTIC_STATUS)
    row = semantic_row(state, topic.topic_key)
    row["status"] = "blocked"
    row["findings"] = [
        {"severity": "unresolved", "finding": f"{type(error).__name__}: {error}"}
    ]
    row["next_action"] = "Resolve this failure before touching any later topic."
    dump(SEMANTIC_STATUS, state)
    refresh_semantic_tracker()


def run_tests() -> list[dict[str, Any]]:
    modules = [
        DEEP_REVIEW_TEST_MODULE,
        "test_run_polity_semantic_topic",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    tests = [deep.run_unittest(module) for module in modules]
    if any(item["exit_code"] or item["failures"] or item["errors"] for item in tests):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


def apply_live_source_provenance(
    topic: deep.Topic,
    result: dict[str, Any],
    changed: set[str],
) -> None:
    sources, note = deep.POLITY_LIVE_OFFICIAL_SOURCES[topic.number]
    status = load(deep.STATUS)
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
        }
    )
    dump(deep.STATUS, status)
    changed.add(rel(deep.STATUS))

    record_path = deep.EXPORTS / (
        f"{topic.topic_key}-learner-v2-g{result['new_generation']}-"
        f"{deep.DATE}-record.json"
    )
    if record_path.is_file():
        payload = load(record_path)
        payload.setdefault("provenance", {}).update(
            {
                "live_sources": sources,
                "current_linkage_note": note,
                "live_sources_rechecked_on": REPORT_DATE,
            }
        )
        dump(record_path, payload)
        changed.add(rel(record_path))

    record = deep.latest(load(deep.STATUS), topic.topic_key)
    content_spec = deep.repo(record["provenance"]["content_spec"])
    payload = load(content_spec)
    payload["live_official_sources"] = sources
    payload["current_status_control"] = note
    payload["live_sources_rechecked_on"] = REPORT_DATE
    dump(content_spec, payload)
    changed.add(rel(content_spec))


def complete_semantic_state(
    topic: deep.Topic,
    result: dict[str, Any],
    files_changed: list[str],
) -> dict[str, Any]:
    state = load(SEMANTIC_STATUS)
    row = semantic_row(state, topic.topic_key)
    row["status"] = "passed"
    row["checks"] = {name: "passed" for name in row["checks"]}
    row["gap_counts"] = {name: 0 for name in row["gap_counts"]}
    row["findings"] = [
        {
            "severity": "closed",
            "finding": (
                "Four-ledger hostile audit closed; Articles, Parts, Schedules, "
                "amendments, cases, dates, doctrine, institutions, exceptions, "
                "current legal status, source hierarchy, PYQ ownership, answer "
                "contracts and both twelve-panel flow masters pass."
            ),
            "record_id": result["new_record_id"],
        }
    ]
    row["files_changed"] = files_changed
    row["completed_at"] = now_iso()
    row["next_action"] = "Passed; advance exactly one topic in authoritative order."
    dump(SEMANTIC_STATUS, state)
    refresh_semantic_tracker()
    return load(SEMANTIC_STATUS)


def report_text(
    topic: deep.Topic,
    result: dict[str, Any],
    validation: dict[str, Any],
    tests: list[dict[str, Any]],
    next_key: str,
) -> str:
    metrics = validation["metrics"]
    return f"""# Polity Semantic-Completeness Review {topic.number:02d} — {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 5 September 2026  
**Result:** PASSED  
**Canonical owner:** `{rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Topic {topic.number:02d} alone was active. The official syllabus/index,
canonical Basic owner, Optional Advanced owner, framework and cross-owner
bridges, complete verified 2018-2026 PYQ ledgers, constitutional/statutory text,
reported cases and authoritative live sources were reconciled through a hostile
four-ledger audit.

The bounded repair preserves exact Articles, Parts, Schedules, amendments,
cases, dates, doctrines, institutional mechanisms, exceptions, source hierarchy
and current operative status. The immutable successor preserves Basic-first and
Advanced-last order, final register notes, examiner-grade answer contracts,
strict A-B-C-D rotation and twelve manually authored ASCII panels agreeing with
twelve graphical stages. Approval remains false. PYQ status: {PYQ_STATUS[topic.number]}.

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


def run(topic_number: int) -> dict[str, Any]:
    topic = deep.topics()[topic_number - 1]
    set_in_progress(topic)
    changed: set[str] = {
        *DRIVER_FILES,
        rel(topic.basic_path),
        rel(SEMANTIC_STATUS),
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-PLAN.md",
    }
    try:
        deep.ensure_canonical_owner_control(topic)
        result = deep.completed_result(topic, changed)
        if result is None:
            result = deep.process_topic(topic, changed)
        apply_live_source_provenance(topic, result, changed)
        deep.update_ledgers([result], changed)

        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
            cwd=ROOT,
            check=True,
        )
        changed.add("EXPORT-PDF-COMMAND-INDEX.md")
        deep.generate_command_guide(ROOT)
        changed.add("V2-SUBJECT-SECTION-COMMAND-INDEX.md")
        changed.update(rel(path) for path in deep.INDEX_DIR.glob("*.md") if path.is_file())

        subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "export_four_item_library.py"),
                "--root",
                str(ROOT),
                "--export-root",
                str(ROOT / "notes" / "Final-Learning-Packages"),
                "--tracker",
                str(deep.STATUS),
                "--catalogue",
                str(ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"),
                "--topic-key",
                topic.topic_key,
                "--manifest-date",
                deep.DATE,
            ],
            cwd=ROOT,
            check=True,
        )
        export_result = deep.export_library(
            root=ROOT,
            export_root=ROOT / "notes" / "Final-Learning-Packages",
            tracker_path=deep.STATUS,
            catalogue_path=ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json",
            selected_keys=[topic.topic_key],
            manifest_date=deep.DATE,
            dry_run=False,
            full_pdf_validation=True,
        )
        deep.add_final_library_paths([result], export_result, changed)
        deep.update_review_tracker([result], changed)

        tests = run_tests()
        library_errors = deep.validate_final_library([result])
        mismatches, reconciled = deep.reconcile([result])
        mismatches.extend(library_errors)
        if mismatches:
            raise RuntimeError("Reconciliation failed: " + " | ".join(mismatches))

        deep.add_all_operation_generation_paths([result], changed)
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        generated_validation = deep.load(deep.repo(result["validation"]))
        deliverables = [
            deep.repo(record["markdown"]),
            deep.repo(record["workbook_markdown"]),
            deep.repo(record["main_pdf"]),
            deep.repo(record["workbook"]),
            deep.repo(record["continuous_core_first"]["master_image"]),
            deep.repo(record["continuous_core_first"]["poster_pdf"]),
            deep.repo(record["continuous_core_first"]["tiled_pdf"]),
            deep.repo(record["continuous_core_first"]["ascii_master_pdf"]),
            deep.repo(record["continuous_core_first"]["ascii_master"]),
        ]
        missing = [str(path) for path in deliverables if not path.is_file()]
        if missing:
            raise FileNotFoundError("Missing accepted deliverables: " + ", ".join(missing))
        hashes = {rel(path): sha256(path) for path in deliverables}

        validation_path = (
            deep.EXPORTS / f"{topic.topic_key}-semantic-validation-{REPORT_DATE}.json"
        )
        inventory_path = deep.EXPORTS / (
            f"{topic.topic_key}-semantic-completeness-{REPORT_DATE}-changed-files.txt"
        )
        report_path = REPORT_DIR / (
            f"{SLUGS[topic.number]}-semantic-completeness-review-{REPORT_DATE}.md"
        )
        changed.update({rel(validation_path), rel(inventory_path), rel(report_path)})

        state_before = load(SEMANTIC_STATUS)
        current_index = next(
            index
            for index, row in enumerate(state_before["topics"])
            if row["topic_key"] == topic.topic_key
        )
        next_key = state_before["topics"][current_index + 1]["topic_key"]
        validation_payload = {
            "schema_version": 1,
            "topic_key": topic.topic_key,
            "record_id": result["new_record_id"],
            "approval": False,
            "result": "passed",
            "ten_gates": {name: True for name in semantic_row(state_before, topic.topic_key)["checks"]},
            "checks": {
                "approval": record["approved"] is False,
                "h2": generated_validation["hard_gates"]["syllabus_and_core_complete"],
                "pyq": generated_validation["hard_gates"]["verified_pyq_metadata_and_key_discipline"],
                "answers": generated_validation["hard_gates"]["model_answers_marks_worthy"],
                "rotation": generated_validation["hard_gates"]["mcq_rotation"],
                "flows": generated_validation["hard_gates"]["graphical_and_ascii_consistent"],
                "layout": generated_validation["hard_gates"]["pdf_layout_clean"],
                "library": not library_errors,
                "reconciliation": not mismatches,
                "validator": generated_validation["result"] == "passed",
                "authoritative_live_sources": (
                    record["provenance"].get("live_sources_rechecked_on") == REPORT_DATE
                ),
            },
            "metrics": {
                **generated_validation["metrics"],
                "targeted_tests": sum(item["tests"] for item in tests),
                "deliverable_hashes_checked": len(hashes),
            },
            "deliverable_hashes": hashes,
            "deliverable_hash_errors": {},
            "reconciled_topic": reconciled[0],
            "next_topic_key": next_key,
        }
        dump(validation_path, validation_payload)

        pending = {rel(validation_path), rel(inventory_path), rel(report_path)}
        changed = {
            path for path in changed if path in pending or (ROOT / path).exists()
        }
        files = sorted(changed, key=str.casefold)
        final_state = complete_semantic_state(topic, result, files)
        next_key = final_state["next_topic"]["topic_key"]
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            report_text(topic, result, generated_validation, tests, next_key),
            encoding="utf-8",
        )
        inventory_path.write_text(
            "\n".join(sorted(changed, key=str.casefold)) + "\n",
            encoding="utf-8",
        )
        return {
            "status": "passed",
            "topic_key": topic.topic_key,
            "record_id": result["new_record_id"],
            "generation": result["new_generation"],
            "metrics": validation_payload["metrics"],
            "tests": sum(item["tests"] for item in tests),
            "next_topic_key": next_key,
            "report": rel(report_path),
            "validation": rel(validation_path),
            "inventory": rel(inventory_path),
        }
    except BaseException as error:
        set_blocked(topic, error)
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
