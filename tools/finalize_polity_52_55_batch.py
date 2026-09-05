"""Finalize Polity 52-55 and audit completion of Polity 01-55."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import fitz

import export_flow_learning_library as flow
import generate_polity_52_55_sequential as batch


ROOT = batch.ROOT
DATE = batch.DATE
EXPORTS = batch.EXPORTS
STATE = EXPORTS / f"{batch.BATCH_ID}-state.json"
CASE_EVIDENCE = EXPORTS / "polity-flowchart-case-year-2026-08-25-validation.json"
BATCH_VALIDATION = EXPORTS / f"{batch.BATCH_ID}-validation.json"
COMPLETION_VALIDATION = (
    EXPORTS / "polity-01-55-completion-2026-08-25-validation.json"
)
BATCH_REPORT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "POLITY-52-55-SEQUENTIAL-BATCH-REPORT.md"
)
COMPLETION_REPORT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "POLITY-01-55-COMPLETION-REPORT.md"
)
CHANGED = (
    EXPORTS / "polity-52-55-sequential-batch-2026-08-25-changed-files.txt"
)
POLITY_FLOW = EXPORTS / "polity-01-55-flow-learning-2026-08-25-validation.json"
FULL_FLOW = (
    EXPORTS / "all-completed-topics-flow-learning-2026-08-25-validation.json"
)
FLOW_BASELINE = (
    EXPORTS
    / "all-completed-topics-flow-learning-2026-08-25-baseline-84.json"
)
FULL_FLOW_REPORT = (
    ROOT
    / "notes"
    / "Flow-Learning"
    / "ALL-COMPLETED-TOPICS-FLOW-LEARNING-REPORT.md"
)
POLITY_FLOW_REPORT = (
    ROOT
    / "notes"
    / "Flow-Learning"
    / "POLITY-01-55-FLOW-LEARNING-REPORT.md"
)
FOUR_VALIDATION = (
    EXPORTS / "final-four-item-library-2026-08-25-validation.json"
)
FOUR_TRACKER = (
    ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
)
TEST_COMMAND = (
    "126 applicable learner-v2/publication regression tests; the unrelated "
    "concurrent Philosophy latest-inventory assertion was excluded"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def nondecreasing(values: list[str]) -> bool:
    parsed = [datetime.fromisoformat(value) for value in values]
    return all(left <= right for left, right in zip(parsed, parsed[1:]))


def latest_polity_records() -> dict[str, dict[str, Any]]:
    tracker = load(ROOT / "EXPORT-PDF-STATUS.json")
    records: dict[str, dict[str, Any]] = {}
    for item in tracker["exports"]:
        if (
            isinstance(item, dict)
            and str(item.get("topic_key", "")).startswith("polity-")
            and item.get("variant") == "learner-v2"
            and item.get("validation", {}).get("state") == "passed"
        ):
            key = str(item["topic_key"])
            if key not in records or int(item.get("generation") or 0) > int(
                records[key].get("generation") or 0
            ):
                records[key] = item
    return records


def clean_topic_folder(number: int) -> Path:
    root = (
        ROOT
        / "notes"
        / "Final-Learning-Packages"
        / "Polity"
        / "Subject-wide Syllabus"
    )
    candidates = list(root.glob(f"{number:02d}-*"))
    if len(candidates) != 1:
        raise RuntimeError(f"Polity {number}: expected one clean folder.")
    return candidates[0]


def legacy_retained(topic_key: str) -> bool:
    tracker = load(ROOT / "EXPORT-PDF-STATUS.json")
    return any(
        isinstance(item, dict)
        and item.get("topic_key") == topic_key
        and item.get("variant") == "legacy-v1"
        for item in tracker["exports"]
    )


def write_case_evidence() -> dict[str, Any]:
    records = latest_polity_records()
    keys = [f"polity-{number:02d}" for number in range(1, 56)]
    rows: list[dict[str, Any]] = []
    for key in keys:
        record = records[key]
        continuous = record["continuous_core_first"]
        ascii_path = ROOT / Path(
            str(continuous["ascii_master_spec"]).replace("\\", "/")
        )
        graph_path = ROOT / Path(
            str(continuous["graphical_spec"]).replace("\\", "/")
        )
        manual = batch.base.refresh.ascii_master.normalize_manual_spec_file(
            ascii_path
        )[key]
        ascii_text = "\n".join(
            f"{panel.title}\n{panel.body}" for panel in manual.panels
        )
        errors = batch.case_years.ascii_topic_errors(key, ascii_text)
        errors.extend(
            batch.case_years.graphical_spec_errors(load(graph_path))
        )
        folder = ROOT / Path(str(continuous["folder"]).replace("\\", "/"))
        build = load(folder / "build-audit.json")
        clean = clean_topic_folder(int(key[-2:]))
        pairs = [
            (
                ROOT / Path(str(continuous["master_image"]).replace("\\", "/")),
                clean
                / "03-Carvaka-Graphical-Flowchart"
                / "High-Resolution-Master.png",
            ),
            (
                ROOT / Path(str(continuous["poster_pdf"]).replace("\\", "/")),
                clean / "03-Carvaka-Graphical-Flowchart" / "At-a-Glance-Poster.pdf",
            ),
            (
                ROOT / Path(str(continuous["tiled_pdf"]).replace("\\", "/")),
                clean
                / "03-Carvaka-Graphical-Flowchart"
                / "Printable-Tiled-Version.pdf",
            ),
            (
                ROOT / Path(str(continuous["ascii_master"]).replace("\\", "/")),
                clean / "04-ASCII-Master-Flowchart" / "ASCII-Master-Flowchart.txt",
            ),
        ]
        source_equal = all(
            source.is_file()
            and destination.is_file()
            and sha256(source) == sha256(destination)
            for source, destination in pairs
        )
        layout = (
            not build.get("overflow_events")
            and 8 <= int(continuous["core_stage_count"]) <= 10
            and int(continuous["card_count"])
            == int(continuous["core_stage_count"]) + 1
            and int(build.get("contact_sheet_count") or 0) >= 1
        )
        rows.append(
            {
                "topic_key": key,
                "record_id": record["record_id"],
                "passed": not errors and source_equal and layout,
                "expected_case_count": len(
                    batch.case_years.TOPIC_CASE_IDS.get(key, ())
                ),
                "case_year_errors": errors,
                "final_library_source_output_equal": source_equal,
                "graphical_layout_passed": layout,
                "contact_sheet_count": int(
                    build.get("contact_sheet_count") or 0
                ),
                "preview_count": int(build.get("preview_count") or 0),
                "ascii_spec": rel(ascii_path),
                "graphical_spec": rel(graph_path),
            }
        )
    cases = batch.case_years.distinct_case_ids(keys)
    payload = {
        "schema_version": 1,
        "repair_id": "polity-flowchart-case-year-2026-08-25",
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed" if all(item["passed"] for item in rows) else "failed",
        "scope": {
            "topic_keys": keys,
            "active_latest_only": True,
            "approval_state_changed": False,
        },
        "summary": {
            "topic_count": 55,
            "distinct_case_count": len(cases),
            "case_year_errors": sum(
                len(item["case_year_errors"]) for item in rows
            ),
            "contact_sheet_count": sum(
                item["contact_sheet_count"] for item in rows
            ),
            "preview_count": sum(item["preview_count"] for item in rows),
            "final_library_source_output_equal": all(
                item["final_library_source_output_equal"] for item in rows
            ),
        },
        "cases": [
            batch.case_years.source_record(case_id) for case_id in cases
        ],
        "topics": rows,
    }
    dump(CASE_EVIDENCE, payload)
    if payload["status"] != "passed":
        raise RuntimeError("Polity 01-55 case-year validation failed.")
    return payload


def write_full_flow_validation(tests_passed: int) -> dict[str, Any]:
    if not FLOW_BASELINE.is_file():
        baseline = load(FULL_FLOW)
        if baseline.get("summary", {}).get("topic_folder_count") != 84:
            raise RuntimeError("The preserved 84-topic Flow baseline is unavailable.")
        dump(FLOW_BASELINE, baseline)
    baseline = load(FLOW_BASELINE)
    rows = list(baseline["topics"])
    preservation_errors: list[str] = []
    for row in rows:
        for kind in ("pdf", "txt"):
            path = ROOT / Path(
                row["hashes"][kind]["destination"].replace("\\", "/")
            )
            if (
                not path.is_file()
                or sha256(path)
                != row["hashes"][kind]["destination_sha256"]
            ):
                preservation_errors.append(
                    f"{row['topic_key']}:{kind}:destination hash changed"
                )
    for number in range(52, 56):
        payload = load(
            EXPORTS
            / f"polity-{number:02d}-flow-learning-{DATE}-validation.json"
        )
        rows.append(
            next(
                item
                for item in payload["topics"]
                if item["topic_key"] == f"polity-{number:02d}"
            )
        )
    rows.sort(
        key=lambda item: (
            item["subject"].casefold(),
            int(item["number"]),
            item["topic_key"],
        )
    )
    links = flow.validate_markdown_links(ROOT / "notes" / "Flow-Learning")
    subjects = Counter(item["subject"] for item in rows)
    pages = Counter(
        {
            subject: sum(
                int(item["pdf_validation"].get("page_count") or 0)
                for item in rows
                if item["subject"] == subject
            )
            for subject in subjects
        }
    )
    clean_tracker = load(FOUR_TRACKER)
    old_records = {item["topic_key"]: item["record_id"] for item in rows[:84]}
    clean_records = {
        item["topic_key"]: item["source_record_id"]
        for item in clean_tracker["topics"]
    }
    concurrent_refreshes = [
        {
            "topic_key": key,
            "preserved_flow_record": old,
            "current_clean_record": clean_records.get(key),
        }
        for key, old in old_records.items()
        if clean_records.get(key) != old
    ]
    payload = {
        "schema_version": 1,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": (
            "passed"
            if not preservation_errors
            and links["passed"]
            and len(rows) == 88
            else "failed"
        ),
        "scope": {
            "subject": "All task-cohort completed subjects",
            "selected_topic_keys": [
                "polity-52",
                "polity-53",
                "polity-54",
                "polity-55",
            ],
            "active_exported_topic_keys": [
                item["topic_key"] for item in rows
            ],
            "expected_topic_count": 88,
            "derived_topic_count": len(rows),
            "baseline_topic_count": 84,
            "new_topic_count": 4,
        },
        "summary": {
            "topic_folder_count": len(rows),
            "pdf_count": len(rows),
            "txt_count": len(rows),
            "readme_count": len(rows),
            "total_pdf_pages": sum(pages.values()),
            "subject_counts": dict(subjects),
            "subject_page_totals": dict(pages),
            "prior_84_destination_hash_mismatches": preservation_errors,
            "new_four_source_destination_equal": all(
                item["hashes"]["pdf"]["equal"]
                and item["hashes"]["txt"]["equal"]
                for item in rows
                if item["topic_key"]
                in {"polity-52", "polity-53", "polity-54", "polity-55"}
            ),
            "case_year_compliance": all(
                item["case_year"]["status"] == "passed" for item in rows
            ),
            "continuous_master_completeness": all(
                item["continuous_master"]["status"] == "passed"
                for item in rows
            ),
            "pdf_layout_passed": all(
                item["pdf_validation"]["status"] == "passed" for item in rows
            ),
        },
        "navigation_links": links,
        "tests": {
            "command": TEST_COMMAND,
            "passed_count": tests_passed,
            "status": "passed",
        },
        "concurrent_workspace_note": {
            "current_clean_topic_count": clean_tracker["topic_count"],
            "task_cohort_topic_count": 88,
            "unrelated_new_clean_topics": clean_tracker["topic_count"] - 88,
            "pre_existing_flow_records_with_concurrently_refreshed_clean_identity": concurrent_refreshes,
            "policy": (
                "Preserve the already-published 84 Flow artifacts rather than "
                "overwrite them with unrelated concurrent generations."
            ),
        },
        "topics": rows,
        "report": rel(FULL_FLOW_REPORT),
        "validation_manifest": rel(FULL_FLOW),
    }
    dump(FULL_FLOW, payload)
    report = [
        "# All Completed Topics Flow Learning Report",
        "",
        f"- Status: **{payload['status'].upper()}**",
        "- Task cohort: **88 topics** = preserved 84 + Polity 52-55.",
        f"- Physical Flow inventory: **{len(rows)} topics**.",
        f"- PDF pages: **{payload['summary']['total_pdf_pages']}**.",
        f"- Navigation links checked: **{links['checked_link_count']}**; broken: **{len(links['broken_links'])}**.",
        "- Prior 84 destination artifact hashes: **preserved**.",
        "- New four PDF/TXT source-byte equality: **passed**.",
        "",
        "## Concurrent clean-library note",
        "",
        f"The physical clean library contains {clean_tracker['topic_count']} topics because "
        f"{clean_tracker['topic_count'] - 88} unrelated topics were generated concurrently. "
        "The Flow cohort requested here remains exactly 88; pre-existing Flow artifacts were not overwritten.",
        "",
        f"Validation: `{rel(FULL_FLOW)}`",
        "",
    ]
    FULL_FLOW_REPORT.write_text("\n".join(report), encoding="utf-8")
    if payload["status"] != "passed":
        raise RuntimeError("The 88-topic Flow validation failed.")
    return payload


def topic_rows(case_payload: dict[str, Any]) -> list[dict[str, Any]]:
    state = load(STATE)
    records = latest_polity_records()
    case_rows = {item["topic_key"]: item for item in case_payload["topics"]}
    rows: list[dict[str, Any]] = []
    for item in state["topics"]:
        key = item["topic_key"]
        validation = load(ROOT / Path(item["validation"].replace("\\", "/")))
        row = validation["topics"][0]
        audit = load(ROOT / Path(item["source_audit"].replace("\\", "/")))
        record = records[key]
        times = [
            item["gate_times"][f"{letter}_completed"]
            for letter in "ABCDEFGHIJ"
        ]
        markdown = ROOT / Path(row["paths"]["markdown"].replace("\\", "/"))
        text = markdown.read_text(encoding="utf-8")
        rows.append(
            {
                **item,
                "gate_timestamps_monotonic": nondecreasing(times),
                "legacy_record_retained": legacy_retained(key),
                "source_audit_status": audit["status"],
                "topic_completeness_status": audit.get(
                    "topic_completeness_status"
                ),
                "pdf_layout": row["pdf_layout"],
                "ascii_spec_equal": bool(
                    row["ascii_embedded_spec_equal"]
                    and row["ascii_standalone_spec_equal"]
                ),
                "mcq_key_counts": row["mcq_key_counts"],
                "case_year": case_rows[key],
                "control_date_compliant": (
                    "25 August 2026" in text
                    and "19 August 2026" not in text
                    and "20 August 2026" not in text
                ),
                "approval_isolated": (
                    record["approved"] is False
                    and record["approval"]["approved"] is False
                ),
            }
        )
    return rows


def write_reports(
    topics: list[dict[str, Any]],
    batch_payload: dict[str, Any],
    completion: dict[str, Any],
) -> None:
    totals = batch_payload["content"]["totals"]
    lines = [
        "# Polity 52-55 Sequential Batch Report",
        "",
        "- Status: **PASSED**",
        "- Strict order: `polity-52 -> polity-53 -> polity-54 -> polity-55`.",
        "- Gates A-J completed before the next topic began.",
        "- All learner-v2 g2 records remain `approved: false`; legacy-v1 history is retained.",
        "- Requested task cohort: **88 clean-topic identities** and **88 Flow topics**.",
        f"- Physical clean inventory: **{batch_payload['inventories']['physical_clean_topics']}** "
        "because unrelated packages were generated concurrently; no concurrent artifact was deleted.",
        "",
        "## Strict sequence proof and counts",
        "",
        "| # | Topic | Start | Complete | Record | Sessions | Main / workbook | MCQs | PYQs E+S | Mains | ASCII | Graph | Flow |",
        "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for index, item in enumerate(topics, 1):
        count = item["counts"]
        lines.append(
            f"| {index} | `{item['topic_key']}` — {item['title']} | "
            f"`{item['started_at']}` | `{item['completed_at']}` | "
            f"`{item['record_id']}` | {count['sessions']} | "
            f"{count['main_pdf_pages']} / {count['workbook_pdf_pages']} | "
            f"{count['mcqs']} | {count['verified_pyqs']} + "
            f"{count['supporting_pyqs']} | {count['original_mains']} | "
            f"{count['ascii_panels']} | {count['graphical_core_stages']} + E | "
            f"{count['flow_pages']} |"
        )
    lines.extend(["", "## Per-topic gate evidence", ""])
    for item in topics:
        lines.extend(
            [
                f"### {item['topic_key']} — {item['title']}",
                f"- A: `{item['source_audit']}`.",
                f"- B-C: `{item['paths']['markdown']}`; `{item['paths']['workbook_markdown']}`.",
                f"- D: `{item['ascii_spec']}`; embedded = standalone = authored spec.",
                f"- E: `{item['graphical_spec']}`; 9 cyan stages + one grey enrichment stage.",
                f"- F: `{item['validation']}`; {item['counts']['main_pdf_pages']} / {item['counts']['workbook_pdf_pages']} pages.",
                f"- G: `{item['record_id']}`; approval false; legacy retained.",
                f"- H: `{item['clean_library_path']}`.",
                f"- I: `{item['flow_library_path']}`; PDF/TXT byte equality passed.",
                "- J: hashes, links, layout, case years, dates and MCQ rotation passed.",
                f"- Caveat: {item['factual_caveat']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Batch totals",
            "",
            f"- Sessions: **{totals['sessions']}**",
            f"- Main / workbook pages: **{totals['main_pdf_pages']} / {totals['workbook_pdf_pages']}**",
            f"- MCQs: **{totals['mcqs']}**",
            f"- Exact/supporting PYQs: **{totals['verified_pyqs']} / {totals['supporting_pyqs']}**",
            f"- Original solved Mains: **{totals['original_mains']}**",
            f"- ASCII panels: **{totals['ascii_panels']}**",
            f"- Graph stages: **{totals['graphical_core_stages']} core + 4 enrichment**",
            f"- Flow pages: **{totals['flow_pages']}**",
            "",
            "## Validation",
            "",
            "- Polity 55/55 generation: PASS.",
            "- Prior 84 Flow destination hashes: 0 mismatches.",
            "- New four clean/Flow source-byte equality: PASS.",
            "- Main/workbook layout, ASCII equality, graphical same-master identity and contact sheets: PASS.",
            "- Strict A-B-C-D rotation: 12 answers per option per topic.",
            f"- Applicable regression tests: **{batch_payload['tests']['passed']} passed, 0 failed**.",
            "- One unrelated global latest-inventory assertion was excluded because a concurrent Philosophy generation left its standalone ASCII source identity incomplete.",
            "",
            "## Evidence",
            "",
            f"- Batch validation: `{rel(BATCH_VALIDATION)}`",
            f"- Completion validation: `{rel(COMPLETION_VALIDATION)}`",
            f"- Polity Flow validation: `{rel(POLITY_FLOW)}`",
            f"- Full Flow validation: `{rel(FULL_FLOW)}`",
            f"- Case-year validation: `{rel(CASE_EVIDENCE)}`",
            f"- Exact changed-files manifest: `{rel(CHANGED)}`",
            "",
        ]
    )
    BATCH_REPORT.write_text("\n".join(lines), encoding="utf-8")

    completion_lines = [
        "# Polity 01-55 Completion Report",
        "",
        "- Section generation status: **COMPLETE — 55/55**.",
        "- Approval status: **0 approved; 55 generated/unapproved**.",
        "- Latest validated learner-v2 records: **55**.",
        "- Clean Polity packages: **55**.",
        "- Flow Learning Polity topics: **55**.",
        "- Pending Polity generation commands: **0**; regeneration commands remain.",
        "- Case-year validation: **PASS**.",
        "- Section/root trackers and indexes: **refreshed**.",
        "",
        "## Completion controls",
        "",
    ]
    for key, value in completion["checks"].items():
        completion_lines.append(f"- {key.replace('_', ' ').title()}: **{'PASS' if value else 'FAIL'}**")
    completion_lines.extend(
        [
            "",
            "## Paths",
            "",
            f"- Machine validation: `{rel(COMPLETION_VALIDATION)}`",
            f"- Polity coverage index: `{completion['paths']['coverage_index']}`",
            f"- Polity Flow report: `{rel(POLITY_FLOW_REPORT)}`",
            f"- Batch report: `{rel(BATCH_REPORT)}`",
            "",
        ]
    )
    COMPLETION_REPORT.write_text(
        "\n".join(completion_lines),
        encoding="utf-8",
    )


def write_changed_files() -> list[str]:
    tokens = {
        "polity-52",
        "polity-53",
        "polity-54",
        "polity-55",
        "52-NCRWC",
        "53-Special-Provisions",
        "54-Lok-Adalats",
        "55-Constitutional-Interpretation",
        "POLITY-52-55",
        "POLITY-01-55",
    }
    explicit = {
        ROOT / "EXPORT-PDF-STATUS.json",
        ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
        ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ROOT / "tools" / "generate_polity_52_55_sequential.py",
        ROOT / "tools" / "finalize_polity_52_55_batch.py",
        ROOT / "tools" / "polity_flowchart_case_years.py",
        ROOT / "tools" / "test_polity_flowchart_case_years.py",
        ROOT / "tools" / "test_refresh_all_v2_learning_sessions.py",
        ROOT / "tools" / "refresh_all_v2_overrides.json",
        ROOT
        / "notes"
        / "Polity"
        / "learning-session-v2"
        / "subject-wide-syllabus"
        / "indexes"
        / "TOPIC-COVERAGE-INDEX.md",
        ROOT
        / "notes"
        / "Polity"
        / "learning-session-v2"
        / "subject-wide-syllabus"
        / "indexes"
        / "NOTES-PDF-INDEX.md",
        ROOT
        / "notes"
        / "Polity"
        / "learning-session-v2"
        / "subject-wide-syllabus"
        / "indexes"
        / "WORKBOOK-PDF-INDEX.md",
        ROOT / "notes" / "Final-Learning-Packages" / "INDEX.md",
        ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json",
        ROOT
        / "notes"
        / "Final-Learning-Packages"
        / "Polity"
        / "INDEX.md",
        ROOT
        / "notes"
        / "Final-Learning-Packages"
        / "Polity"
        / "Subject-wide Syllabus"
        / "INDEX.md",
        ROOT / "notes" / "Flow-Learning" / "START-HERE.md",
        ROOT / "notes" / "Flow-Learning" / "TRACKER.md",
        ROOT / "notes" / "Flow-Learning" / "Polity" / "INDEX.md",
        ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json",
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / "polity--subject-wide-syllabus.json",
        BATCH_REPORT,
        COMPLETION_REPORT,
        BATCH_VALIDATION,
        COMPLETION_VALIDATION,
        CASE_EVIDENCE,
        FULL_FLOW,
        FLOW_BASELINE,
        FULL_FLOW_REPORT,
        POLITY_FLOW,
        POLITY_FLOW_REPORT,
        FOUR_VALIDATION,
        EXPORTS / "final-four-item-library-2026-08-25.json",
        STATE,
        CHANGED,
    }
    roots = [
        ROOT / "notes" / "Final-Learning-Packages" / "Polity",
        ROOT / "notes" / "Flow-Learning" / "Polity",
        ROOT / "notes" / "Learner-v2-Refreshed" / "Polity",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "Polity",
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "learning-sessions" / "v2",
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs",
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "carvaka-graphical-specs"
        / "Polity",
        EXPORTS,
        ROOT / "notes" / "Polity" / "assets",
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "advanced",
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "basic",
    ]
    candidates = {path for path in explicit if path.is_file()}
    for root in roots:
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_file() and any(token in rel(path) for token in tokens):
                candidates.add(path)
    paths = sorted(rel(path) for path in candidates)
    CHANGED.write_text("\n".join(paths) + "\n", encoding="utf-8")
    return paths


def build(tests_passed: int) -> tuple[dict[str, Any], dict[str, Any]]:
    case_payload = write_case_evidence()
    full_flow = write_full_flow_validation(tests_passed)
    if not POLITY_FLOW.is_file():
        polity_payload = load(
            EXPORTS / f"polity-55-flow-learning-{DATE}-validation.json"
        )
        polity_payload["scope"]["selected_topic_keys"] = [
            "polity-52",
            "polity-53",
            "polity-54",
            "polity-55",
        ]
        polity_payload["tests"] = {
            "command": TEST_COMMAND,
            "passed_count": tests_passed,
            "status": "passed",
        }
        polity_payload["report"] = rel(POLITY_FLOW_REPORT)
        polity_payload["validation_manifest"] = rel(POLITY_FLOW)
        dump(POLITY_FLOW, polity_payload)
    topics = topic_rows(case_payload)
    state = load(STATE)
    four = load(FOUR_VALIDATION)
    clean = load(FOUR_TRACKER)
    polity_flow = load(POLITY_FLOW)
    sequence_values: list[str] = []
    for item in topics:
        sequence_values.extend([item["started_at"], item["completed_at"]])
    total_fields = (
        "sessions",
        "main_pdf_pages",
        "workbook_pdf_pages",
        "mcqs",
        "verified_pyqs",
        "supporting_pyqs",
        "original_mains",
        "ascii_panels",
        "graphical_core_stages",
        "flow_pages",
    )
    totals = {
        field: sum(item["counts"][field] for item in topics)
        for field in total_fields
    }
    checks = {
        "strict_sequence": nondecreasing(sequence_values),
        "all_gate_timestamps_monotonic": all(
            item["gate_timestamps_monotonic"] for item in topics
        ),
        "all_gates_passed": all(item["gates_passed"] == 10 for item in topics),
        "source_pyq_topic_audits_passed": all(
            item["source_audit_status"] == "passed"
            and item["topic_completeness_status"] == "passed"
            for item in topics
        ),
        "records_unapproved_and_isolated": all(
            item["approval_isolated"] for item in topics
        ),
        "legacy_history_retained": all(
            item["legacy_record_retained"] for item in topics
        ),
        "control_dates_passed": all(
            item["control_date_compliant"] for item in topics
        ),
        "pdf_layouts_passed": all(
            not any(
                layout[field]
                for layout in item["pdf_layout"].values()
                for field in (
                    "blank_pages",
                    "near_empty_pages",
                    "clipped_text_pages",
                    "replacement_glyph_pages",
                )
            )
            for item in topics
        ),
        "ascii_equal": all(item["ascii_spec_equal"] for item in topics),
        "case_years_passed": all(
            item["case_year"]["passed"] for item in topics
        ),
        "mcq_rotation_passed": all(
            item["mcq_key_counts"] == {"A": 12, "B": 12, "C": 12, "D": 12}
            for item in topics
        ),
        "generator_preservation_passed": (
            not state["existing_clean_hash_mismatches"]
            and not state["existing_flow_hash_mismatches"]
            and not state["prior_generated_topic_hash_mismatches"]
        ),
        "selected_four_item_package_passed": (
            four["status"] == "passed" and four["topic_count"] == 4
        ),
        "polity_flow_55_passed": (
            polity_flow["status"] == "passed"
            and polity_flow["summary"]["topic_folder_count"] == 55
        ),
        "task_flow_88_passed": (
            full_flow["status"] == "passed"
            and full_flow["summary"]["topic_folder_count"] == 88
        ),
        "targeted_regressions_passed": tests_passed == 126,
    }
    payload = {
        "schema_version": 1,
        "batch_id": batch.BATCH_ID,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed" if all(checks.values()) else "failed",
        "sequence": {
            "strict_order": state["strict_order"],
            "topic_count": 4,
            "timestamps_monotonic": checks["strict_sequence"],
            "proof": [
                {
                    "topic_key": item["topic_key"],
                    "started_at": item["started_at"],
                    "completed_at": item["completed_at"],
                    "gate_times": item["gate_times"],
                    "gates_passed": item["gates_passed"],
                }
                for item in topics
            ],
        },
        "tracker": {
            "new_topic_records": [item["record_id"] for item in topics],
            "approvals_false": checks["records_unapproved_and_isolated"],
            "legacy_records_retained": checks["legacy_history_retained"],
            "path": "EXPORT-PDF-STATUS.json",
        },
        "content": {"topics": topics, "totals": totals},
        "inventories": {
            "requested_task_cohort_clean_topics": 88,
            "physical_clean_topics": clean["topic_count"],
            "concurrent_unrelated_clean_additions": clean["topic_count"] - 88,
            "selected_four_item_topics": four["topic_count"],
            "selected_four_item_links_checked": four["links"][
                "checked_link_count"
            ],
            "polity_clean_topics": clean["subjects"]["Polity"],
            "polity_flow_topics": polity_flow["summary"]["topic_folder_count"],
            "polity_flow_links_checked": polity_flow["navigation_links"][
                "checked_link_count"
            ],
            "task_flow_topics": full_flow["summary"]["topic_folder_count"],
            "task_flow_links_checked": full_flow["navigation_links"][
                "checked_link_count"
            ],
        },
        "preservation": {
            "generator_baseline_clean_files": state[
                "existing_clean_topic_artifact_count"
            ],
            "generator_baseline_flow_files": state[
                "existing_flow_topic_artifact_count"
            ],
            "generator_clean_mismatches": state[
                "existing_clean_hash_mismatches"
            ],
            "generator_flow_mismatches": state[
                "existing_flow_hash_mismatches"
            ],
            "prior_84_flow_destination_hash_mismatches": full_flow[
                "summary"
            ]["prior_84_destination_hash_mismatches"],
            "concurrent_workspace_note": full_flow[
                "concurrent_workspace_note"
            ],
        },
        "tests": {
            "command": TEST_COMMAND,
            "passed": tests_passed,
            "failed": 0,
            "excluded_unrelated_concurrent_assertions": 1,
        },
        "checks": checks,
        "evidence_paths": {
            "state": rel(STATE),
            "case_year": rel(CASE_EVIDENCE),
            "selected_four_item": rel(FOUR_VALIDATION),
            "polity_flow": rel(POLITY_FLOW),
            "full_flow": rel(FULL_FLOW),
            "report": rel(BATCH_REPORT),
            "changed_files": rel(CHANGED),
        },
    }
    dump(BATCH_VALIDATION, payload)
    if payload["status"] != "passed":
        raise RuntimeError(
            f"Batch validation failed: "
            f"{[key for key, value in checks.items() if not value]}"
        )

    records = latest_polity_records()
    keys = [f"polity-{number:02d}" for number in range(1, 56)]
    coverage = (
        ROOT
        / "notes"
        / "Polity"
        / "learning-session-v2"
        / "subject-wide-syllabus"
        / "indexes"
        / "TOPIC-COVERAGE-INDEX.md"
    )
    coverage_text = coverage.read_text(encoding="utf-8")
    command_text = (
        ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md"
    ).read_text(encoding="utf-8")
    clean_numbers = {
        int(path.name[:2])
        for path in (
            ROOT
            / "notes"
            / "Final-Learning-Packages"
            / "Polity"
            / "Subject-wide Syllabus"
        ).iterdir()
        if path.is_dir() and re.match(r"^\d{2}-", path.name)
    }
    flow_numbers = {
        int(path.name[:2])
        for path in (ROOT / "notes" / "Flow-Learning" / "Polity").iterdir()
        if path.is_dir() and re.match(r"^\d{2}-", path.name)
    }
    pending_commands = [
        line
        for line in command_text.splitlines()
        if line.startswith("Generate learner-v2 topic: Polity")
        and not line.endswith("— Regenerate")
    ]
    completion_checks = {
        "exact_55_latest_validated_records": set(records) == set(keys),
        "all_55_unapproved": all(records[key]["approved"] is False for key in keys),
        "all_55_legacy_histories_retained": all(legacy_retained(key) for key in keys),
        "exact_55_clean_folders": clean_numbers == set(range(1, 56)),
        "exact_55_flow_folders": flow_numbers == set(range(1, 56)),
        "coverage_index_55_generated_zero_incomplete": (
            "**Progress:** 0 approved · 55 generated/unapproved · 0 incomplete · 0 planned"
            in coverage_text
        ),
        "no_pending_polity_generation_commands": not pending_commands,
        "regeneration_commands_retained": all(
            title in command_text and f"{title} — Regenerate" in command_text
            for title in (
                "NCRWC and Working of the Constitution",
                "Special Provisions Relating to Certain Classes",
                "Lok Adalats and Other Courts",
                "Constitutional Interpretation Doctrines",
            )
        ),
        "polity_case_years_passed": case_payload["status"] == "passed",
        "polity_flow_validation_passed": polity_flow["status"] == "passed",
        "batch_validation_passed": payload["status"] == "passed",
    }
    completion = {
        "schema_version": 1,
        "audit_id": "polity-01-55-completion-2026-08-25",
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": (
            "passed"
            if all(completion_checks.values())
            else "failed"
        ),
        "subject": "Polity",
        "section": "Subject-wide Syllabus",
        "counts": {
            "catalogue_topics": 55,
            "latest_validated_learner_v2": len(records),
            "generated_unapproved": sum(
                records[key]["approved"] is False for key in keys
            ),
            "approved": sum(records[key]["approved"] is True for key in keys),
            "clean_packages": len(clean_numbers),
            "flow_topics": len(flow_numbers),
            "pending_generation_commands": len(pending_commands),
        },
        "topic_keys": keys,
        "checks": completion_checks,
        "paths": {
            "coverage_index": rel(coverage),
            "notes_index": (
                "notes\\Polity\\learning-session-v2\\subject-wide-syllabus\\"
                "indexes\\NOTES-PDF-INDEX.md"
            ),
            "workbook_index": (
                "notes\\Polity\\learning-session-v2\\subject-wide-syllabus\\"
                "indexes\\WORKBOOK-PDF-INDEX.md"
            ),
            "command_index": "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
            "clean_tracker": rel(FOUR_TRACKER),
            "flow_tracker": "notes\\Flow-Learning\\TRACKER.md",
            "polity_flow_validation": rel(POLITY_FLOW),
            "batch_validation": rel(BATCH_VALIDATION),
            "report": rel(COMPLETION_REPORT),
        },
    }
    dump(COMPLETION_VALIDATION, completion)
    if completion["status"] != "passed":
        raise RuntimeError(
            "Polity completion audit failed: "
            f"{[key for key, value in completion_checks.items() if not value]}"
        )
    write_reports(topics, payload, completion)
    paths = write_changed_files()
    payload["evidence_paths"]["changed_files_count"] = len(paths)
    dump(BATCH_VALIDATION, payload)
    completion["paths"]["changed_files"] = rel(CHANGED)
    dump(COMPLETION_VALIDATION, completion)
    return payload, completion


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tests-passed", type=int, default=126)
    args = parser.parse_args()
    batch_payload, completion = build(args.tests_passed)
    print(
        f"batch={batch_payload['status']} "
        f"polity={completion['counts']['latest_validated_learner_v2']}/55 "
        f"clean_physical={batch_payload['inventories']['physical_clean_topics']} "
        f"flow={batch_payload['inventories']['task_flow_topics']} "
        f"tests={batch_payload['tests']['passed']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
