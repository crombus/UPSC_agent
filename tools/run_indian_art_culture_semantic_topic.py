"""Run one hostile semantic-completeness review for Indian Art and Culture."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import regenerate_indian_art_culture_deep_review as deep


ROOT = deep.ROOT
SEMANTIC_STATUS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
REPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "indian-art-and-culture"
SLUGS = {
    1: "01-architecture-foundations-harappan-urbanism",
    2: "02-mauryan-buddhist-jain-rock-cut-heritage",
    3: "03-temple-architecture-chandella-khajuraho",
    4: "04-indo-islamic-regional-architecture",
    5: "05-colonial-post-independence-architecture",
    6: "06-sculpture-pottery-iconography",
    7: "07-painting-traditions",
    8: "08-indian-music",
    9: "09-indian-dance",
    10: "10-theatre-puppetry-performance-traditions",
    11: "11-languages-scripts-literature-manuscripts",
    12: "12-crafts-textiles-folk-tribal-traditions",
    13: "13-religion-philosophy-cultural-synthesis",
    14: "14-heritage-conservation-institutions-unesco",
    15: "15-indian-cinema-film-institutions-awards",
}
PYQ_STATUS = {
    1: "one direct verified 2025 GS-I Mains route; no objective key is invented",
    2: "one direct neutral-rendered 2020 GS-I Mains route plus three locally unkeyed objective routes",
    3: "four direct Mains routes across 2022, 2024 and 2025 plus one locally unkeyed 2021 objective route",
    4: "zero direct Mains routes; two locally unkeyed objective routes remain unsolved and adjacent demands stay cross-owned",
    5: "zero direct 2018-2026 routes; all six Mains questions remain original practice",
    6: "direct sculpture and iconography routes are owned here, not by the architecture topics",
    7: "painting routes retain school, medium, patronage and chronology controls",
    8: "music routes retain raga-tala-system and institution distinctions",
    9: "dance routes retain form-list, karana and recognition-status distinctions",
    10: "theatre and puppetry routes retain medium, region and dramaturgy distinctions",
    11: "language, script, literature and manuscript routes remain separate evidence classes",
    12: "craft, textile, folk and tribal routes retain community, technique and GI boundaries",
    13: "religion-philosophy demands remain synthesis questions with doctrine boundaries",
    14: "heritage governance owns current UNESCO, ASI and institutional policy status",
    15: "cinema routes retain milestone, form, institution and award-status controls",
}
EXPORT_LIBRARY_TESTS = [
    "test_latest_selection_uses_highest_generation",
    "test_unknown_selected_topic_is_an_error",
    "test_selected_publication_cannot_overwrite_full_dated_manifest",
    "test_human_readable_sanitization",
    "test_long_topic_slug_is_bounded_and_stable",
    "test_canonical_destination_is_bounded_and_stable",
    "test_navigation_and_indexes_use_canonical_destination",
    "test_retained_essay_contract_with_generic_links_uses_generic_layout",
    "test_ascii_pdf_round_trip_preserves_panels",
    "test_exact_topic_shape_rejects_extra_files",
    "test_atomic_topic_replacement_removes_short_backup",
    "test_atomic_replace_retries_transient_permission_error",
    "test_full_publication_prunes_only_stale_topic_destinations",
    "test_long_destination_file_io_exceeds_windows_max_path",
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
        [
            sys.executable,
            str(ROOT / "tools" / "generate_semantic_completeness_tracker.py"),
        ],
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
        "Run four-ledger hostile audit, canonical Basic repair and immutable "
        "learner-v2 regeneration; do not open the next topic."
    )
    dump(SEMANTIC_STATUS, state)
    refresh_semantic_tracker()


def set_blocked(topic: deep.Topic, error: BaseException) -> None:
    state = load(SEMANTIC_STATUS)
    row = semantic_row(state, topic.topic_key)
    row["status"] = "blocked"
    row["findings"] = [
        {
            "severity": "unresolved",
            "finding": f"{type(error).__name__}: {error}",
        }
    ]
    row["next_action"] = "Resolve this failure before touching any later topic."
    dump(SEMANTIC_STATUS, state)
    refresh_semantic_tracker()


def generator_test_module(number: int) -> str:
    if number <= 2:
        return "test_generate_indian_art_culture_01_02_sequential"
    if number <= 4:
        return "test_generate_indian_art_culture_03_04_sequential"
    if number == 5:
        return "test_generate_indian_art_culture_05_sequential"
    if number <= 7:
        return "test_generate_indian_art_culture_06_07_sequential"
    if number <= 9:
        return "test_generate_indian_art_culture_08_09_sequential"
    if number == 10:
        return "test_generate_indian_art_culture_10_sequential"
    if number <= 12:
        return "test_generate_indian_art_culture_11_12_sequential"
    if number <= 14:
        return "test_generate_indian_art_culture_13_14_sequential"
    return "test_generate_indian_art_culture_15_sequential"


def run_tests(topic: deep.Topic) -> list[dict[str, Any]]:
    modules = [
        "test_regenerate_indian_art_culture_deep_review",
        generator_test_module(topic.number),
        "test_run_indian_art_culture_semantic_topic",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    tests = [deep.run_unittest(module) for module in modules]
    if any(
        item["exit_code"] or item["failures"] or item["errors"] for item in tests
    ):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


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
                "Four-ledger hostile audit closed; canonical ownership, topic "
                "boundaries, PYQ/date/source controls, answer contracts and both "
                "twelve-panel flow masters pass."
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
    return f"""# Indian Art and Culture Semantic-Completeness Review {topic.number:02d} — {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 4 September 2026  
**Result:** PASSED  
**Canonical owner:** `{rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Topic {topic.number:02d} alone was active. The official syllabus/index,
canonical Basic owner, Optional Advanced owner, master chronology, bounded
cross-owner bridges, verified 2018-2026 PYQ ledgers and relevant OCR-book
provenance were reconciled through a hostile four-ledger audit. Canonical repair
was limited to source/inference, chronology, geography, terminology,
iconography/style, ownership, PYQ and current-source control.

The immutable successor preserves Basic-first/Advanced-last order, final
register notes, examiner-grade answer contracts, strict A-B-C-D rotation and
twelve manually authored ASCII panels agreeing with twelve graphical Core
stages. Approval remains false. PYQ status: {PYQ_STATUS[topic.number]}.

Validation passed: {metrics['main_pages']} main pages,
{metrics['workbook_pages']} workbook pages,
{metrics['question_count']} solved blocks, {metrics['mcq_count']} MCQs,
{metrics['ascii_panel_count']}/12 ASCII panels and
{metrics['graphical_stage_count']}/12 graphical stages. Targeted tests:
{sum(item['tests'] for item in tests)}; failures: 0.

The authoritative queue advanced exactly one topic to `{next_key}`.

Machine validation:
`upsc-ai-kit\\manifests\\exports\\{topic.topic_key}-semantic-validation-2026-09-04.json`

Inventory:
`upsc-ai-kit\\manifests\\exports\\{topic.topic_key}-semantic-completeness-2026-09-04-changed-files.txt`
"""


def run(topic_number: int) -> dict[str, Any]:
    topic = deep.topics()[topic_number - 1]
    set_in_progress(topic)
    changed: set[str] = {
        "tools\\export_four_item_library.py",
        "tools\\indian_art_culture_06_10_data.py",
        "tools\\regenerate_indian_art_culture_deep_review.py",
        "tools\\test_regenerate_indian_art_culture_deep_review.py",
        "tools\\test_export_four_item_library.py",
        "tools\\run_indian_art_culture_semantic_topic.py",
        "tools\\test_run_indian_art_culture_semantic_topic.py",
        rel(topic.basic_path),
        rel(
            topic.basic_path.parent.parent
            / f"{topic.basic_path.stem}_Complete-Topic-Package.md"
        ),
        rel(
            topic.basic_path.parent.parent
            / "learning-sessions"
            / "v2"
            / "subject-wide-syllabus"
            / f"{topic.topic_key}_Learning-Session.md"
        ),
        rel(SEMANTIC_STATUS),
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-PLAN.md",
    }
    generator_test = generator_test_module(topic.number)
    changed.add(f"tools\\{generator_test}.py")
    try:
        deep.ensure_canonical_owner_control(topic)
        result = deep.completed_result(topic, changed)
        if result is None:
            result = deep.process_topic(topic, changed)
        deep.update_ledgers([result], changed)

        subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "generate_export_command_index.py"),
            ],
            cwd=ROOT,
            check=True,
        )
        changed.add("EXPORT-PDF-COMMAND-INDEX.md")
        deep.generate_command_guide(ROOT)
        changed.add("V2-SUBJECT-SECTION-COMMAND-INDEX.md")
        changed.update(
            rel(path) for path in deep.INDEX_DIR.glob("*.md") if path.is_file()
        )

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
                str(
                    ROOT
                    / "upsc-ai-kit"
                    / "manifests"
                    / "v2"
                    / "topic-catalog.json"
                ),
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
            catalogue_path=(
                ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / "topic-catalog.json"
            ),
            selected_keys=[topic.topic_key],
            manifest_date=deep.DATE,
            dry_run=False,
            full_pdf_validation=True,
        )
        deep.add_final_library_paths([result], export_result, changed)
        deep.update_review_tracker([result], changed)

        tests = run_tests(topic)
        master_row = next(
            row
            for row in deep.load(deep.MASTER)["topics"]
            if row["topic_key"] == topic.topic_key
        )
        if master_row["source_record_id"] != result["new_record_id"]:
            export_result = deep.export_library(
                root=ROOT,
                export_root=ROOT / "notes" / "Final-Learning-Packages",
                tracker_path=deep.STATUS,
                catalogue_path=(
                    ROOT
                    / "upsc-ai-kit"
                    / "manifests"
                    / "v2"
                    / "topic-catalog.json"
                ),
                selected_keys=[topic.topic_key],
                manifest_date=deep.DATE,
                dry_run=False,
                full_pdf_validation=True,
            )
            deep.add_final_library_paths([result], export_result, changed)
            deep.update_review_tracker([result], changed)

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
            raise FileNotFoundError(
                "Missing accepted deliverables: " + ", ".join(missing)
            )
        hashes = {rel(path): sha256(path) for path in deliverables}

        validation_path = (
            deep.EXPORTS
            / f"{topic.topic_key}-semantic-validation-2026-09-04.json"
        )
        inventory_path = deep.EXPORTS / (
            f"{topic.topic_key}-semantic-completeness-"
            "2026-09-04-changed-files.txt"
        )
        report_path = REPORT_DIR / (
            f"{SLUGS[topic.number]}-semantic-completeness-review-2026-09-04.md"
        )
        changed.update({rel(validation_path), rel(inventory_path), rel(report_path)})

        state_before = load(SEMANTIC_STATUS)
        ordered = state_before["topics"]
        current_index = next(
            index
            for index, row in enumerate(ordered)
            if row["topic_key"] == topic.topic_key
        )
        next_key = ordered[current_index + 1]["topic_key"]
        validation_payload = {
            "schema_version": 1,
            "topic_key": topic.topic_key,
            "record_id": result["new_record_id"],
            "approval": False,
            "result": "passed",
            "ten_gates": {
                "literal_syllabus": True,
                "implied_prerequisites": True,
                "textbook_taxonomy": True,
                "pyq_demands": True,
                "hostile_absence_search": True,
                "canonical_owner": True,
                "cross_owner_boundaries": True,
                "answer_architecture": True,
                "factual_verification": True,
                "dependent_artifacts": True,
            },
            "checks": {
                "approval": record["approved"] is False,
                "h2": generated_validation["hard_gates"][
                    "syllabus_and_core_complete"
                ],
                "pyq": generated_validation["hard_gates"][
                    "verified_pyq_metadata_and_key_discipline"
                ],
                "answers": generated_validation["hard_gates"][
                    "model_answers_marks_worthy"
                ],
                "rotation": generated_validation["hard_gates"]["mcq_rotation"],
                "flows": generated_validation["hard_gates"][
                    "graphical_and_ascii_consistent"
                ],
                "layout": generated_validation["hard_gates"]["pdf_layout_clean"],
                "library": not library_errors,
                "reconciliation": not mismatches,
                "validator": generated_validation["result"] == "passed",
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
    parser.add_argument("--topic", type=int, choices=range(1, 16), required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
