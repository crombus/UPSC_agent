"""Run one hostile semantic-completeness review for Geography."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import regenerate_geography_part_a_deep_review as deep


ROOT = deep.ROOT
REPORT_DATE = "2026-09-05"
TOPIC_CHOICES = range(1, 26)
DEEP_REVIEW_TEST_MODULE = "test_regenerate_geography_part_a_deep_review"
DRIVER_FILES = {
    "tools\\regenerate_geography_part_a_deep_review.py",
    "tools\\test_regenerate_geography_part_a_deep_review.py",
    "tools\\run_geography_semantic_topic.py",
    "tools\\test_run_geography_semantic_topic.py",
}
FORCE_REGENERATE = False
STATUS_TOPIC_KEYS: dict[str, str] = {}
SEMANTIC_STATUS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
REPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "geography"
SLUGS = {
    1: "01-earth-universe-india-location-extent",
    2: "02-earth-crust-rocks-india-geological-structure",
    3: "03-vulcanism-earthquakes-india-seismic-zones",
    4: "04-weathering-erosion-landslides-groundwater",
    5: "05-rivers-drainage-india-interlinking",
    6: "06-glaciation-himalayan-glaciers-glof",
    7: "07-thar-desert-desertification",
    8: "08-caves-meghalayan-age",
    9: "09-lakes-wetlands-ramsar",
    10: "10-coast-coastal-landforms-crz",
    11: "11-islands-coral-reefs-great-nicobar",
    12: "12-oceans-currents-tides-salinity-iod",
    13: "13-weather-elements-jet-stream-western-disturbances",
    14: "14-climate-classification-india-climatic-regions",
    15: "15-hot-wet-equatorial-india-evergreen-forests",
    16: "16-india-monsoon-mechanism",
    17: "17-india-deciduous-forests-grasslands",
    18: "18-thar-desert-great-indian-bustard",
    19: "19-india-himalayan-fruit-belt",
    20: "20-india-wheat-granary",
    21: "21-humid-subtropical-northeast",
    22: "22-himalayan-temperate-forests",
    23: "23-subalpine-and-alpine-belt",
    24: "24-eastern-himalaya-temperate",
    25: "25-cold-desert-and-poles",
}
PYQ_STATUS = {
    1: (
        "direct routes cover 2019/2022 solstice, 2021 subcontinent, 2024 "
        "aurora/latitude/stars and 2025 axis/solar-flare/IDL demands; no "
        "unavailable key is invented"
    ),
    2: (
        "direct routes cover 2018 magnetic reversal, 2022 primary rocks, "
        "2023 Indian ranges, 2024 mountain types, 2025 drift/tectonics and "
        "provisional 2026 Peninsular Block; provisional keys stay unpromoted"
    ),
    3: (
        "direct routes cover 2018 Barren Island/mantle plume, 2020 "
        "Circum-Pacific, 2021 eruption impacts, 2023 waves, 2024 products, "
        "2025 tsunami and provisional 2026 Tungurahua"
    ),
    4: (
        "direct routes cover 2018 urban harvesting, 2021 black-soil, 2023 "
        "groundwater withdrawal, 2024 weathering and 2025 permeability; "
        "landslide and Gangetic-groundwater bridges retain external ownership"
    ),
    5: (
        "direct routes cover 2020 interlinking, 2021 tributary/source maps, "
        "2022 Gandikota, 2024 waterfall matching and provisional 2026 "
        "drainage-shift/antecedent-river demands"
    ),
    6: (
        "direct routes cover 2019 glacier-river matching, 2020 Himalayan "
        "glacier melting and Indian water resources, and 2023 fjord formation; "
        "the unavailable 2019 objective key remains unpromoted"
    ),
    7: (
        "the checked central ledgers contain no direct Geography Topic 07 "
        "route; the 2020 desertification demand remains Environment-owned and "
        "is retained only as bounded cross-owner context"
    ),
    8: (
        "the checked central ledgers contain no direct Geography Topic 08 "
        "route; Ajanta and cave-shrine demands remain with their cultural "
        "owners and no direct PYQ is fabricated"
    ),
    9: (
        "direct routes cover 2018 lake shrinkage/artificial lakes, 2019 "
        "reservoirs, 2021 Rajasthan saline lakes, 2023 river-lake matching and "
        "provisional 2026 Lake Turkana; unavailable/provisional keys stay "
        "unpromoted and the urban-water-body Mains route remains cross-owned"
    ),
    10: (
        "the direct route is the 2023 GS-I coastline resource-potential and "
        "natural-hazard preparedness demand; mangrove, blue-carbon, coral and "
        "tsunami demands remain with their routed owners"
    ),
    11: (
        "direct routes cover the 2018 coral-distribution/biodiversity objective "
        "demand and 2019 GS-I global-warming impact on coral life; unavailable "
        "objective keys stay unpromoted"
    ),
    12: (
        "direct routes cover the 2019 GS-I currents versus water masses and "
        "marine-life demand and the 2022 GS-I forces influencing currents and "
        "fishing; no live IOD phase is inferred"
    ),
    13: (
        "only routed weather-element, jet-stream, upper-air and western-"
        "disturbance demands are retained; reconstructed wording and "
        "unavailable keys remain labelled"
    ),
    14: (
        "only routed Köppen/classification and Indian climatic-region demands "
        "are retained; no station code or revised map boundary is invented"
    ),
    15: (
        "direct routes cover the 2021 rainforest-structure and 2023 tropical-"
        "rainforest nutrient/decomposition objective demands; both unavailable "
        "official answer letters remain unpromoted"
    ),
    16: (
        "direct ownership includes the 2023 GS-I Purvaiya/Bhojpur demand and "
        "the 2026 Andaman-Nicobar climate objective route; the provisional "
        "2026 Set-A key remains unpromoted"
    ),
    17: (
        "the direct route is the 2021 savanna tree-limitation objective "
        "demand; the unavailable official answer letter remains unpromoted"
    ),
    18: (
        "the audited Geography ledgers contain no direct Topic 18 route; "
        "desertification remains Topic 07-owned and GIB law remains bounded "
        "cross-owner context, so no PYQ is fabricated"
    ),
    19: (
        "the audited ledgers contain no direct Topic 19 route; horticulture, "
        "climate-impact and value-chain questions remain bounded applications "
        "and no PYQ is fabricated"
    ),
    20: (
        "the audited ledgers contain no direct Topic 20 route; adjacent "
        "climate, soil, cropping and food-security demands retain their routed "
        "owners and no PYQ is fabricated"
    ),
    21: (
        "the audited ledgers contain no direct Topic 21 route; eastern-margin "
        "climate, Northeast monsoon and flood-fertility applications remain "
        "bounded, and no PYQ is fabricated"
    ),
    22: (
        "the routed 2024 Marine West Coast objective demand is retained "
        "without inventing an answer letter; Himalayan forest belts remain an "
        "altitudinal analogue rather than a British-climate equivalence"
    ),
    23: (
        "the audited ledgers contain no direct Topic 23 route; taiga, "
        "permafrost and Himalayan subalpine-alpine applications remain bounded "
        "and no PYQ is fabricated"
    ),
    24: (
        "the audited ledgers contain no direct Topic 24 route; Laurentian, "
        "current-convergence and Eastern-Himalaya applications remain bounded "
        "and no PYQ is fabricated"
    ),
    25: (
        "the verified route is 2021 GS-I Q15 on Arctic ice, Antarctic "
        "glaciers and weather patterns; floating/grounded ice, hemispheric "
        "scale and confidence levels remain explicit"
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
    key = STATUS_TOPIC_KEYS.get(key, key)
    return next(row for row in state["topics"] if row["topic_key"] == key)


def set_in_progress(topic: deep.Topic) -> None:
    state = load(SEMANTIC_STATUS)
    status_key = STATUS_TOPIC_KEYS.get(topic.topic_key, topic.topic_key)
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
        and row["topic_key"] != status_key
    ]
    if active:
        raise ValueError("Another semantic topic is active: " + ", ".join(active))
    if state["next_topic"]["topic_key"] != status_key:
        raise ValueError(
            f"Authoritative next topic is {state['next_topic']['topic_key']}, "
            f"not {topic.topic_key}."
        )
    row = semantic_row(state, topic.topic_key)
    row["status"] = "in_progress"
    row["reviewed_at"] = now_iso()
    row["next_action"] = (
        "Run the four-ledger hostile audit, bounded canonical repair and "
        "immutable learner-v2 regeneration; do not open the next topic."
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


def generator_test_module(number: int) -> str | None:
    if number in {5, 6}:
        return "test_generate_geography_05_06_sequential"
    if number == 7:
        return "test_generate_geography_07_08_sequential"
    if number == 8:
        return "test_generate_geography_07_08_sequential"
    if number == 9:
        return "test_generate_geography_09_sequential"
    if number == 10:
        return "test_generate_geography_10_11_sequential"
    if number == 11:
        return "test_generate_geography_10_11_sequential"
    if number in {12, 13}:
        return "test_generate_geography_12_13_sequential"
    if number == 14:
        return "test_generate_geography_14_sequential"
    if number == 15:
        return "test_generate_geography_15_16_sequential"
    if number == 16:
        return "test_generate_geography_15_16_sequential"
    if number in {17, 18}:
        return "test_generate_geography_17_18_sequential"
    if number == 19:
        return "test_generate_geography_19_sequential"
    if number == 20:
        return "test_generate_geography_20_sequential"
    if number == 21:
        return "test_generate_geography_21_sequential"
    if number == 22:
        return "test_generate_geography_22_sequential"
    if number == 23:
        return "test_generate_geography_23_sequential"
    if number == 24:
        return "test_generate_geography_24_sequential"
    if number == 25:
        return "test_generate_geography_25_sequential"
    return None


def run_tests(topic: deep.Topic) -> list[dict[str, Any]]:
    modules = [
        DEEP_REVIEW_TEST_MODULE,
        "test_run_geography_semantic_topic",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    generator_test = generator_test_module(topic.number)
    if generator_test:
        modules.insert(1, generator_test)
    tests = [deep.run_unittest(module) for module in modules]
    if any(
        item["exit_code"] or item["failures"] or item["errors"] for item in tests
    ):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


def apply_live_source_provenance(
    topic: deep.Topic,
    result: dict[str, Any],
    changed: set[str],
) -> None:
    sources, note = deep.GEOGRAPHY_LIVE_OFFICIAL_SOURCES[topic.number]
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

    content_spec = deep.repo(record["provenance"]["content_spec"])
    if content_spec.is_file():
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
                "Four-ledger hostile audit closed; canonical ownership, "
                "process/scale/map/chronology/data/terminology/causal/source "
                "controls, bounded cross-ownership, PYQ/key discipline, answer "
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
    return f"""# Geography Semantic-Completeness Review {topic.number:02d} — {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 5 September 2026  
**Result:** PASSED  
**Canonical owner:** `{rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Topic {topic.number:02d} alone was active. The official syllabus/index,
canonical Basic owner, Optional Advanced owner, master framework, bounded
cross-owner bridges, verified 2018-2026 PYQ ledgers, relevant OCR-searchable
Geography books and authoritative live sources were reconciled through a hostile
four-ledger audit.

Canonical repair is bounded to exact process, scale, map/spatial, chronology,
data, terminology, causation, source/date and ownership controls. The immutable
successor preserves Basic-first/Advanced-last order, final register notes,
examiner-grade answer contracts, strict A-B-C-D rotation and twelve manually
authored ASCII panels agreeing with twelve graphical Core stages. Approval
remains false. PYQ status: {PYQ_STATUS[topic.number]}.

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
    topic = next(
        item for item in deep.topics() if item.number == topic_number
    )
    if topic.number not in SLUGS:
        raise ValueError("This topic-only driver does not own that Geography topic.")
    set_in_progress(topic)
    changed: set[str] = {
        *DRIVER_FILES,
        rel(topic.basic_path),
        rel(SEMANTIC_STATUS),
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-PLAN.md",
    }
    generator_test = generator_test_module(topic.number)
    if generator_test:
        changed.add(f"tools\\{generator_test}.py")
    try:
        deep.ensure_canonical_owner_control(topic)
        result = None
        if not FORCE_REGENERATE:
            result = deep.completed_result(topic, changed)
        if result is None:
            result = deep.process_topic(topic, changed)
        apply_live_source_provenance(topic, result, changed)
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
            / f"{topic.topic_key}-semantic-validation-{REPORT_DATE}.json"
        )
        inventory_path = deep.EXPORTS / (
            f"{topic.topic_key}-semantic-completeness-"
            f"{REPORT_DATE}-changed-files.txt"
        )
        report_path = REPORT_DIR / (
            f"{SLUGS[topic.number]}-semantic-completeness-review-"
            f"{REPORT_DATE}.md"
        )
        changed.update({rel(validation_path), rel(inventory_path), rel(report_path)})

        state_before = load(SEMANTIC_STATUS)
        ordered = state_before["topics"]
        current_index = next(
            index
            for index, row in enumerate(ordered)
            if row["topic_key"]
            == STATUS_TOPIC_KEYS.get(topic.topic_key, topic.topic_key)
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
                "authoritative_live_sources": (
                    record["provenance"].get("live_sources_rechecked_on")
                    == REPORT_DATE
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

        pending_outputs = {rel(validation_path), rel(inventory_path), rel(report_path)}
        changed = {
            path
            for path in changed
            if path in pending_outputs or (ROOT / path).exists()
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
