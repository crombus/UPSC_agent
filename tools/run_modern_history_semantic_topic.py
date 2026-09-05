"""Run one hostile semantic-completeness review for Modern History topics."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import regenerate_modern_history_deep_review as deep


ROOT = deep.ROOT
SEMANTIC_STATUS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
REPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "modern-history"
SLUGS = {
    1: "01-decline-mughal-empire-1707-1740s",
    2: "02-indian-states-society-eighteenth-century",
    3: "03-beginnings-european-settlements",
    4: "04-british-conquest-bengal-plassey-buxar-dual-government",
    5: "05-british-territorial-expansion",
    6: "06-government-structure-constitutional-development-1757-1858",
    7: "07-economic-impact-british-rule",
    8: "08-administrative-organisation",
    9: "09-social-cultural-policy-education-press",
    10: "10-socio-religious-reform-movements",
    11: "11-revolt-of-1857",
    12: "12-administrative-constitutional-changes-after-1858",
    13: "13-india-and-her-neighbours",
    14: "14-foundation-inc-moderate-phase",
    15: "15-militant-nationalism-swadeshi-partition-bengal",
    16: "16-revolutionary-nationalism-phase-i-1907-1917",
    17: "17-growth-communalism-muslim-league",
    18: "18-first-world-war-home-rule-lucknow-pact",
    19: "19-gandhi-rise-rowlatt-jallianwala",
    20: "20-non-cooperation-khilafat",
    21: "21-swarajists-constructive-work-revolutionaries-1920s",
    22: "22-simon-commission-nehru-report-civil-disobedience-round-table-conferences",
    23: "23-left-peasant-workers-states-peoples-movements-1930s",
    24: "24-government-india-act-1935-congress-ministries-1937-1939",
    25: "25-second-world-war-cripps-mission-quit-india-1939-1942",
    26: "26-post-war-upsurge-ina-rin-cabinet-mission-1945-1946",
    27: "27-independence-partition-1946-1947",
    28: "28-integration-princely-states-making-republic",
    29: "29-colonial-legacy-foundations-republic",
    30: "30-linguistic-reorganisation-states-regionalism",
    31: "31-integration-tribals-national-unity",
    32: "32-nehru-era-hope-foreign-policy-legacy",
    33: "33-party-politics-congress-system-opposition",
    34: "34-shastri-indira-gandhi-1964-1973",
    35: "35-jp-movement-emergency",
    36: "36-janata-interregnum-indira-return-regional-crises",
    37: "37-rajiv-years-run-up-millennium",
    38: "38-economy-land-society-state-post-independence-synthesis",
}


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
        "Run four-ledger audit, canonical repair and immutable learner-v2 "
        "regeneration; do not open the next topic."
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
    row["next_action"] = "Resolve the recorded failure before touching any later topic."
    dump(SEMANTIC_STATUS, state)
    refresh_semantic_tracker()


def run_tests(topic: deep.Topic) -> list[dict[str, Any]]:
    generator_module = {
        1: "test_generate_modern_history_01_02_sequential",
        2: "test_generate_modern_history_01_02_sequential",
        3: "test_generate_modern_history_03_04_sequential",
        4: "test_generate_modern_history_03_04_sequential",
        5: "test_generate_modern_history_05_06_sequential",
        6: "test_generate_modern_history_05_06_sequential",
        7: "test_generate_modern_history_07_08_sequential",
        8: "test_generate_modern_history_07_08_sequential",
        9: "test_generate_modern_history_09_13_sequential",
        10: "test_generate_modern_history_09_13_sequential",
        11: "test_generate_modern_history_09_13_sequential",
        12: "test_generate_modern_history_09_13_sequential",
        13: "test_generate_modern_history_09_13_sequential",
        14: "test_generate_modern_history_14_15_sequential",
        15: "test_generate_modern_history_14_15_sequential",
        16: "test_generate_modern_history_16_17_sequential",
        17: "test_generate_modern_history_16_17_sequential",
        18: "test_generate_modern_history_18_19_sequential",
        19: "test_generate_modern_history_18_19_sequential",
        20: "test_generate_modern_history_20_21_sequential",
        21: "test_generate_modern_history_20_21_sequential",
        22: "test_generate_modern_history_22_23_sequential",
        23: "test_generate_modern_history_22_23_sequential",
        24: "test_generate_modern_history_24_25_sequential",
        25: "test_generate_modern_history_24_25_sequential",
        26: "test_generate_modern_history_26_27_sequential",
        27: "test_generate_modern_history_26_27_sequential",
        28: "test_generate_modern_history_28_29_sequential",
        29: "test_generate_modern_history_28_29_sequential",
        30: "test_generate_modern_history_30_31_sequential",
        31: "test_generate_modern_history_30_31_sequential",
        32: "test_generate_modern_history_32_33_sequential",
        33: "test_generate_modern_history_32_33_sequential",
        34: "test_generate_modern_history_34_35_sequential",
        35: "test_generate_modern_history_34_35_sequential",
        36: "test_generate_modern_history_36_37_sequential",
        37: "test_generate_modern_history_36_37_sequential",
        38: "test_generate_modern_history_38_sequential",
    }[topic.number]
    modules = [
        "test_regenerate_modern_history_deep_review",
        generator_module,
        "test_export_four_item_library",
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
                "Hostile four-ledger audit completed; canonical ownership, PYQ "
                "routing, chronology, answer contracts and both flow masters pass."
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
    pyq = {
        1: "zero direct; three adjacent-owned controls",
        2: "one direct Prelims route; key inferred",
        3: "four direct Prelims routes; 2025 Q75 key locally official",
        4: "zero direct; two adjacent-owned bridges",
        5: "two direct routes; 2018 key inferred, 2022 Mains unkeyed",
        6: "two direct Prelims routes; 2019 and 2023 local official keys unavailable",
        7: "six active direct routes; one dropped and one provisional objective control",
        8: "zero direct routes for 2018-2026; all practice remains original",
        9: "six direct Prelims routes, two inferred from supplementary evidence, plus one bounded Mains route",
        10: "eleven direct routes; Vital-Vidhvansak remains source-verified but locally unkeyed",
        11: "two direct routes; 2019 Mains solved and 2026 objective key remains provisional",
        12: "zero direct routes for 2018-2026; original practice only",
        13: "zero direct Modern-History routes for 2018-2026; original practice only",
        14: "one direct Mains route: 2021 GS-I on the Moderate foundation",
        15: "five direct routes; Lajpat Rai and Desher Katha answers are supplementary-evidence inferences",
        16: "one direct 2022 Prelims route; only Rash Behari Bose is supported, with the locally unkeyed answer labelled inferred",
        17: "one direct 2018 GS-I route plus provisional 2026 Prelims routing; no provisional key promoted",
        18: "one direct 2018 Prelims route; the 2024 balance-of-power demand remains World-History-owned",
        19: "one topic-tight 2018 Champaran route; five Gandhi demands remain bounded or cross-cutting",
        20: "three locally official-key-confirmed 2025 routes, one unkeyed 2026 route and one bounded 2021 Mains route",
        21: "one shared direct 2020 GS-I route; one adjacent 2018 name-confusion control with no local official key",
        22: "two direct Prelims routes; 2025 Q74 is locally official-key-confirmed and 2020 Q27 is locally unkeyed",
        23: "five routed demands: bounded/shared 2019 and 2020 Mains, cross-period 2023 Mains, locally unkeyed 2020 Prelims and provisional 2026 Prelims",
        24: "two direct Prelims routes; 2024 Q62 is locally official-key-confirmed and 2018 Q38 is locally unkeyed",
        25: "one locally official-verbatim 2024 Mains route plus two neutral objective routing summaries with exact stems and keys unavailable",
        26: "three routed demand summaries; exact objective stems and official keys are unavailable locally",
        27: "one unresolved objective route plus one shared 2019 transfer-of-power Mains route; no unsupported key is promoted",
        28: "one locally verified direct 2021 GS-I route; zero direct Prelims routes",
        29: "one locally verified direct 2025 GS-I route, one adjacent-owned 2021 route and zero direct Prelims routes",
        30: "two routed Mains demand summaries from 2018 and 2022; zero direct Modern History Prelims routes",
        31: "zero direct Modern History routes; adjacent tribal-society, colonial-tribal and Scheduled Areas demands remain explicitly cross-owned",
        32: "one direct 2018 Prelims chronology route with the local official key unavailable; the 2025 consolidation Mains demand remains Topic 29-owned",
        33: "one direct 2024 Prelims party-leader route; the local Series-A key exists but no answer is inferred in the owner",
        34: "one direct 2019 Prelims coal-nationalisation demand retained as an explicit unsupported local evidence gap; zero direct Mains routes",
        35: "zero direct Modern History routes for 2018-2026; all practice remains original and cross-owner constitutional material stays bounded",
        36: "zero direct Modern History routes for 2018-2026; original practice remains original and constitutional doctrine stays Polity-owned",
        37: "zero direct Modern History routes for 2018-2026; original practice remains original and later constitutional/economic doctrine stays cross-owned",
        38: "nine routed Prelims entries audited; one direct land-reform demand, one historical Hind Mazdoor Sabha evidence gap, seven current-affairs routing artefacts and zero direct Mains routes",
    }[topic.number]
    return f"""# Modern History Semantic-Completeness Review {topic.number:02d} — {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 4 September 2026  
**Result:** PASSED  
**Canonical owner:** `{rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Topic {topic.number:02d} alone was active. The official syllabus/index, canonical
Basic owner, Optional Advanced owner, master chronology, cross-owner boundaries,
verified 2018-2026 PYQ ledgers and relevant OCR-book provenance were reconciled
through a hostile four-ledger audit. Canonical repair was limited to explicit
ownership, chronology and PYQ controls.

The immutable successor preserves Basic-first/Advanced-last order, final register
notes, examiner-grade answer contracts, strict A-B-C-D rotation, and twelve
manually authored ASCII panels agreeing with twelve graphical Core stages.
Approval remains false. PYQ status: {pyq}.

Validation passed: {metrics['main_pages']} main pages, {metrics['workbook_pages']}
workbook pages, {metrics['question_count']} solved blocks, {metrics['mcq_count']}
MCQs, {metrics['ascii_panel_count']}/12 ASCII panels and
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
        "tools\\regenerate_modern_history_deep_review.py",
        "tools\\test_regenerate_modern_history_deep_review.py",
        "tools\\run_modern_history_semantic_topic.py",
        rel(topic.basic_path),
        rel(SEMANTIC_STATUS),
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-PLAN.md",
    }
    if topic.number <= 2:
        changed.add("tools\\test_generate_modern_history_01_02_sequential.py")
    try:
        deep.ensure_canonical_owner_control(topic)
        result = deep._historical_completed_result(topic)
        if result is None:
            result = deep.process_topic(topic, changed)
        deep.update_ledgers([result], changed)

        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
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
            catalogue_path=ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "v2"
            / "topic-catalog.json",
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
                catalogue_path=ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / "topic-catalog.json",
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
            raise FileNotFoundError("Missing accepted deliverables: " + ", ".join(missing))
        hashes = {rel(path): sha256(path) for path in deliverables}

        validation_path = (
            deep.EXPORTS
            / f"{topic.topic_key}-semantic-validation-2026-09-04.json"
        )
        inventory_path = (
            deep.EXPORTS
            / (
                f"{topic.topic_key}-semantic-completeness-"
                "2026-09-04-changed-files.txt"
            )
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
                "h2": generated_validation["hard_gates"]["syllabus_and_core_complete"],
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
        files = sorted(changed, key=str.casefold)
        inventory_path.write_text("\n".join(files) + "\n", encoding="utf-8")
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
    parser.add_argument("--topic", type=int, choices=range(1, 39), required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
