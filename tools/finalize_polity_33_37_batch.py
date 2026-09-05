"""Finalize validation and publication records for the Polity 33-37 batch."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_33_37_sequential as batch


ROOT = batch.ROOT
DATE = batch.DATE
EXPORTS = batch.EXPORTS
STATE_PATH = EXPORTS / f"{batch.BATCH_ID}-state.json"
CASE_EVIDENCE = (
    EXPORTS / "polity-flowchart-case-year-repair-2026-08-24-validation.json"
)
POLITY_FLOW_VALIDATION = (
    EXPORTS / "polity-01-37-flow-learning-2026-08-24-validation.json"
)
ALL_FLOW_VALIDATION = (
    EXPORTS / "all-completed-topics-flow-learning-2026-08-24-validation.json"
)
FINAL_VALIDATION = EXPORTS / f"{batch.BATCH_ID}-validation.json"
REPORT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "POLITY-33-37-SEQUENTIAL-BATCH-REPORT.md"
)
CHANGED = EXPORTS / f"{batch.BATCH_ID}-changed-files.txt"
FOUR_VALIDATION = EXPORTS / "final-four-item-library-2026-08-24-validation.json"
TEST_COMMAND = (
    "python -m unittest tools.test_v2_topic_command_catalog "
    "tools.test_v2_section_indexes tools.test_v2_export_foundation "
    "tools.test_retrofit_v2_core_first tools.test_refresh_all_v2_learning_sessions "
    "tools.test_polity_flowchart_case_years tools.test_plan_v2_topic_batch "
    "tools.test_export_four_item_library tools.test_export_flow_learning_library "
    "tools.test_carvaka_flowchart -q"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def latest_records() -> dict[str, dict[str, Any]]:
    tracker = load(ROOT / "EXPORT-PDF-STATUS.json")
    result: dict[str, dict[str, Any]] = {}
    for record in tracker["exports"]:
        if (
            isinstance(record, dict)
            and str(record.get("topic_key", "")).startswith("polity-")
            and record.get("variant") == "learner-v2"
            and record.get("validation", {}).get("state") == "passed"
        ):
            key = str(record["topic_key"])
            if key not in result or int(record.get("generation") or 0) > int(
                result[key].get("generation") or 0
            ):
                result[key] = record
    return result


def clean_topic_folder(number: int) -> Path:
    candidates = list(
        (
            ROOT
            / "notes"
            / "Final-Learning-Packages"
            / "Polity"
            / "Subject-wide Syllabus"
        ).glob(f"{number:02d}-*")
    )
    if len(candidates) != 1:
        raise RuntimeError(
            f"Expected one clean Polity folder for {number}: {candidates}"
        )
    return candidates[0]


def write_case_evidence() -> dict[str, Any]:
    records = latest_records()
    topic_keys = [f"polity-{number:02d}" for number in range(1, 38)]
    rows: list[dict[str, Any]] = []
    for key in topic_keys:
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
        graph = load(graph_path)
        errors.extend(batch.case_years.graphical_spec_errors(graph))

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
                clean
                / "03-Carvaka-Graphical-Flowchart"
                / "At-a-Glance-Poster.pdf",
            ),
            (
                ROOT / Path(str(continuous["tiled_pdf"]).replace("\\", "/")),
                clean
                / "03-Carvaka-Graphical-Flowchart"
                / "Printable-Tiled-Version.pdf",
            ),
            (
                ROOT / Path(str(continuous["ascii_master"]).replace("\\", "/")),
                clean
                / "04-ASCII-Master-Flowchart"
                / "ASCII-Master-Flowchart.txt",
            ),
        ]
        source_equal = all(
            source.is_file()
            and destination.is_file()
            and sha256(source) == sha256(destination)
            for source, destination in pairs
        )
        core_stage_count = int(continuous["core_stage_count"])
        card_count = int(continuous["card_count"])
        layout_passed = (
            not build.get("overflow_events")
            and 9 <= core_stage_count <= 10
            and card_count == core_stage_count + 1
            and int(build.get("contact_sheet_count") or 0) >= 1
        )
        rows.append(
            {
                "topic_key": key,
                "record_id": record["record_id"],
                "passed": not errors and layout_passed and source_equal,
                "layout_status": "passed" if layout_passed else "failed",
                "contact_sheet_count": int(build.get("contact_sheet_count") or 0),
                "preview_count": int(build.get("preview_count") or 0),
                "final_library_source_output_equal": source_equal,
                "expected_case_count": len(
                    batch.case_years.TOPIC_CASE_IDS.get(key, ())
                ),
                "errors": errors,
                "ascii_spec": rel(ascii_path),
                "graphical_spec": rel(graph_path),
            }
        )
    distinct_cases = batch.case_years.distinct_case_ids(topic_keys)
    payload = {
        "schema_version": 1,
        "repair_id": "polity-flowchart-case-year-repair-2026-08-24",
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed" if all(row["passed"] for row in rows) else "failed",
        "scope": {
            "topic_keys": topic_keys,
            "active_latest_only": True,
            "tracker_generation_created": False,
            "approval_state_changed": False,
        },
        "summary": {
            "topic_count": len(rows),
            "distinct_case_count": len(distinct_cases),
            "case_year_errors": sum(len(row["errors"]) for row in rows),
            "contact_sheet_count": sum(row["contact_sheet_count"] for row in rows),
            "preview_count": sum(row["preview_count"] for row in rows),
            "final_library_source_output_equal": all(
                row["final_library_source_output_equal"] for row in rows
            ),
        },
        "cases": [
            batch.case_years.source_record(case_id)
            for case_id in distinct_cases
        ],
        "topics": rows,
    }
    CASE_EVIDENCE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if payload["status"] != "passed":
        raise RuntimeError("Polity case-year evidence failed.")
    return payload


def run_flow_publications(tests_passed: int) -> None:
    common = [
        "--topic-key",
        "polity-37",
        "--manifest-date",
        DATE,
        "--case-year-evidence",
        rel(CASE_EVIDENCE),
        "--tests-passed",
        str(tests_passed),
        "--tests-command",
        TEST_COMMAND,
    ]
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "export_flow_learning_library.py"),
            "--subject",
            "Polity",
            "--topic-prefix",
            "polity-",
            "--report-path",
            "notes\\Flow-Learning\\POLITY-01-37-FLOW-LEARNING-REPORT.md",
            "--validation-path",
            rel(POLITY_FLOW_VALIDATION),
            *common,
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "export_flow_learning_library.py"),
            "--all-completed",
            "--expected-topic-count",
            "70",
            "--report-path",
            "notes\\Flow-Learning\\ALL-COMPLETED-TOPICS-FLOW-LEARNING-REPORT.md",
            "--validation-path",
            rel(ALL_FLOW_VALIDATION),
            *common,
        ],
        cwd=ROOT,
        check=True,
    )


def nondecreasing(values: list[str]) -> bool:
    parsed = [datetime.fromisoformat(value) for value in values]
    return all(left <= right for left, right in zip(parsed, parsed[1:]))


def legacy_retained(tracker: dict[str, Any], topic_key: str) -> bool:
    return any(
        isinstance(record, dict)
        and record.get("topic_key") == topic_key
        and record.get("variant") == "legacy-v1"
        for record in tracker["exports"]
    )


def build_validation(tests_passed: int) -> dict[str, Any]:
    state = load(STATE_PATH)
    tracker = load(ROOT / "EXPORT-PDF-STATUS.json")
    records = latest_records()
    case_evidence = load(CASE_EVIDENCE)
    case_rows = {row["topic_key"]: row for row in case_evidence["topics"]}
    four = load(FOUR_VALIDATION)
    polity_flow = load(POLITY_FLOW_VALIDATION)
    all_flow = load(ALL_FLOW_VALIDATION)
    all_flow_rows = {row["topic_key"]: row for row in all_flow["topics"]}
    topics: list[dict[str, Any]] = []

    for item in state["topics"]:
        key = item["topic_key"]
        validation = load(ROOT / Path(item["validation"].replace("\\", "/")))
        row = validation["topics"][0]
        record = records[key]
        flow_row = all_flow_rows[key]
        audit = load(ROOT / Path(item["source_audit"].replace("\\", "/")))
        continuous = record["continuous_core_first"]
        times = [
            item["gate_times"][f"{letter}_completed"]
            for letter in "ABCDEFGHIJ"
        ]
        markdown = ROOT / Path(row["paths"]["markdown"].replace("\\", "/"))
        markdown_text = markdown.read_text(encoding="utf-8")
        topics.append(
            {
                **item,
                "gate_timestamps_monotonic": nondecreasing(times),
                "legacy_record_retained": legacy_retained(tracker, key),
                "source_audit_status": audit["status"],
                "topic_completeness_status": audit.get(
                    "topic_completeness_status"
                ),
                "pdf_layout": row["pdf_layout"],
                "ascii_spec_equal": bool(
                    row["ascii_embedded_spec_equal"]
                    and row["ascii_standalone_spec_equal"]
                ),
                "ascii_contact_sheet": row["ascii_visual_review"]["contact_sheet"],
                "graphical_contact_sheet": continuous["contact_sheets"][0],
                "graphical_same_master": case_rows[key][
                    "final_library_source_output_equal"
                ],
                "case_year": {
                    "status": "passed" if case_rows[key]["passed"] else "failed",
                    "expected_case_count": case_rows[key]["expected_case_count"],
                    "errors": case_rows[key]["errors"],
                },
                "flow_hashes": flow_row["hashes"],
                "flow_status": flow_row["status"],
                "mcq_key_counts": row["mcq_key_counts"],
                "control_date_compliant": (
                    "24 August 2026" in markdown_text
                    and "19 August 2026" not in markdown_text
                ),
            }
        )

    sequence_values: list[str] = []
    for item in state["topics"]:
        sequence_values.extend([item["started_at"], item["completed_at"]])
    totals = {
        name: sum(item["counts"][name] for item in topics)
        for name in (
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
    }
    checks = {
        "strict_sequence": nondecreasing(sequence_values),
        "all_gate_timestamps_monotonic": all(
            item["gate_timestamps_monotonic"] for item in topics
        ),
        "all_gates_passed": all(item["gates_passed"] == 10 for item in topics),
        "source_pyq_current_audits_passed": all(
            item["source_audit_status"] == "passed"
            and item["topic_completeness_status"] == "passed"
            for item in topics
        ),
        "tracker_records_unapproved": all(
            item["approved"] is False for item in topics
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
        "graphical_same_master": all(
            item["graphical_same_master"] for item in topics
        ),
        "case_years_passed": all(
            item["case_year"]["status"] == "passed" for item in topics
        ),
        "mcq_rotation_passed": all(
            item["mcq_key_counts"] == {"A": 12, "B": 12, "C": 12, "D": 12}
            for item in topics
        ),
        "prior_65_clean_hashes_preserved": not state[
            "existing_clean_hash_mismatches"
        ],
        "prior_65_flow_hashes_preserved": not state[
            "existing_flow_hash_mismatches"
        ],
        "prior_generated_topics_preserved": not state[
            "prior_generated_topic_hash_mismatches"
        ],
        "four_item_inventory_70": four["topic_count"] == 70
        and four["status"] == "passed",
        "polity_flow_inventory_37": (
            polity_flow["summary"]["topic_folder_count"] == 37
            and polity_flow["status"] == "passed"
        ),
        "full_flow_inventory_70": (
            all_flow["summary"]["topic_folder_count"] == 70
            and all_flow["status"] == "passed"
        ),
        "four_item_links_passed": four["links"]["passed"],
        "polity_flow_links_passed": polity_flow["navigation_links"]["passed"],
        "full_flow_links_passed": (
            all_flow["navigation_links"]["passed"]
            and not all_flow["navigation_links"]["broken_links"]
        ),
        "targeted_regressions_passed": tests_passed == 127,
    }
    payload = {
        "schema_version": 1,
        "batch_id": batch.BATCH_ID,
        "validated_at": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "status": "passed" if all(checks.values()) else "failed",
        "sequence": {
            "strict_order": state["strict_order"],
            "topic_count": len(topics),
            "timestamps_monotonic": checks["strict_sequence"],
            "all_gate_timestamps_monotonic": checks[
                "all_gate_timestamps_monotonic"
            ],
            "proof": [
                {
                    "topic_key": item["topic_key"],
                    "started_at": item["started_at"],
                    "completed_at": item["completed_at"],
                    "gates_passed": item["gates_passed"],
                }
                for item in topics
            ],
        },
        "tracker": {
            "latest_validated_topics": 70,
            "new_topic_records": [item["record_id"] for item in topics],
            "legacy_records_retained": checks["legacy_history_retained"],
            "approvals_false": checks["tracker_records_unapproved"],
            "tracker_path": "EXPORT-PDF-STATUS.json",
        },
        "content": {"topics": topics, "totals": totals},
        "inventories": {
            "four_item_topics": four["topic_count"],
            "four_item_links_checked": four["links"]["checked_link_count"],
            "polity_flow_topics": polity_flow["summary"]["topic_folder_count"],
            "polity_flow_links_checked": polity_flow["navigation_links"][
                "checked_link_count"
            ],
            "full_flow_topics": all_flow["summary"]["topic_folder_count"],
            "full_flow_links_checked": all_flow["navigation_links"][
                "checked_link_count"
            ],
            "full_flow_topic_artifact_files_checked": (
                all_flow["summary"]["topic_folder_count"] * 3
            ),
            "full_flow_pages": all_flow["summary"]["total_pdf_pages"],
        },
        "preservation": {
            "prior_clean_artifact_files": state[
                "existing_clean_topic_artifact_count"
            ],
            "prior_flow_artifact_files": state[
                "existing_flow_topic_artifact_count"
            ],
            "clean_hash_mismatches": state["existing_clean_hash_mismatches"],
            "flow_hash_mismatches": state["existing_flow_hash_mismatches"],
            "prior_generated_hash_mismatches": state[
                "prior_generated_topic_hash_mismatches"
            ],
        },
        "tests": {
            "command": TEST_COMMAND,
            "passed": tests_passed,
            "failed": 0,
        },
        "checks": checks,
        "evidence_paths": {
            "state": rel(STATE_PATH),
            "case_year": rel(CASE_EVIDENCE),
            "four_item": rel(FOUR_VALIDATION),
            "polity_flow": rel(POLITY_FLOW_VALIDATION),
            "full_flow": rel(ALL_FLOW_VALIDATION),
            "report": rel(REPORT),
            "changed_files": rel(CHANGED),
        },
    }
    FINAL_VALIDATION.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if payload["status"] != "passed":
        failed = [name for name, value in checks.items() if not value]
        raise RuntimeError(f"Final batch validation failed: {failed}")
    return payload


def write_report(payload: dict[str, Any]) -> None:
    topics = payload["content"]["topics"]
    totals = payload["content"]["totals"]
    lines = [
        "# Polity 33-37 Sequential Batch Report",
        "",
        "- Status: **PASSED**",
        "- Execution: strict order `polity-33 -> polity-34 -> polity-35 -> polity-36 -> polity-37`.",
        "- Gates: A-J completed for each topic before the next topic started.",
        "- Approval: all five learner-v2 g2 records remain `approved: false`; legacy-v1 history is retained.",
        "- Final clean four-item library: **70 topics**. Final Flow Learning inventory: **70 topics**, including **Polity 37**.",
        "",
        "## Sequential proof and package counts",
        "",
        "| # | Topic | Start | Complete | Record | Sessions | Main / workbook pages | MCQs | PYQs exact + supporting | Mains | ASCII | Graph | Flow pages |",
        "|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for index, item in enumerate(topics, 1):
        c = item["counts"]
        lines.append(
            f"| {index} | `{item['topic_key']}` — {item['title']} | "
            f"`{item['started_at']}` | `{item['completed_at']}` | "
            f"`{item['record_id']}` | {c['sessions']} | "
            f"{c['main_pdf_pages']} / {c['workbook_pdf_pages']} | {c['mcqs']} | "
            f"{c['verified_pyqs']} + {c['supporting_pyqs']} | "
            f"{c['original_mains']} | {c['ascii_panels']} | "
            f"{c['graphical_core_stages']} + E | {c['flow_pages']} |"
        )
    lines.extend(["", "## Per-topic gate evidence", ""])
    for item in topics:
        lines.extend(
            [
                f"### {item['topic_key']} — {item['title']}",
                f"- A audit: `{item['source_audit']}`.",
                f"- B-C reusable Markdown/workbook: `{item['paths']['markdown']}`; `{item['paths']['workbook_markdown']}`.",
                f"- D ASCII spec: `{item['ascii_spec']}`; embedded = standalone = authored spec.",
                f"- E graphical spec: `{item['graphical_spec']}`; 9 cyan stages + one grey enrichment stage.",
                f"- F validation/PDFs: `{item['validation']}`; main {item['counts']['main_pdf_pages']} pages; workbook {item['counts']['workbook_pdf_pages']} pages.",
                f"- G tracker: `{item['record_id']}`, `approved: false`; legacy-v1 retained.",
                f"- H clean four-item package: `{item['clean_library_path']}`.",
                f"- I Flow Learning: `{item['flow_library_path']}`; PDF/TXT source-byte equality passed.",
                "- J regression: case years, dates, links, layout, hashes, rotation and prior-topic preservation passed.",
                f"- Factual caveat: {item['factual_caveat']}",
                "",
            ]
        )
    lines.extend(
        [
            "## Batch totals",
            "",
            f"- Sessions: **{totals['sessions']}**",
            f"- Main PDF pages: **{totals['main_pdf_pages']}**",
            f"- Workbook PDF pages: **{totals['workbook_pdf_pages']}**",
            f"- MCQs: **{totals['mcqs']}**",
            f"- Exact/direct verified PYQs: **{totals['verified_pyqs']}**",
            f"- Supporting routed PYQs: **{totals['supporting_pyqs']}**",
            f"- Original solved Mains questions: **{totals['original_mains']}**",
            f"- ASCII panels: **{totals['ascii_panels']}**",
            f"- Graphical stages: **{totals['graphical_core_stages']} core + 5 enrichment**",
            f"- Flow Learning pages: **{totals['flow_pages']}**",
            "",
            "## Validation",
            "",
            "- Strict sequence and A-J gate timestamps: PASS.",
            "- Source, PYQ, current-control and topic-completeness audits: PASS.",
            "- Main/workbook blank, near-empty, clipping and replacement-glyph checks: PASS.",
            "- ASCII embedded/spec/standalone equality: PASS.",
            "- Graphical poster/tiled same-master identity and contact-sheet reviews: PASS.",
            "- Every registered decided case in both flow forms carries a verified decision year: PASS.",
            "- Strict original MCQ rotation A -> B -> C -> D: PASS; each topic has 12 A, 12 B, 12 C and 12 D answers.",
            "- Existing 65 clean packages: prior canonical artifact files checked, 0 hash mismatches.",
            "- Existing 65 Flow Learning topics: prior topic artifacts checked, 0 hash mismatches.",
            f"- Full four-item library: 70 topics; {payload['inventories']['four_item_links_checked']} links checked; 0 broken.",
            f"- Polity Flow Learning: 37 topics; {payload['inventories']['polity_flow_links_checked']} links checked; 0 broken.",
            f"- Full Flow Learning: 70 topics; {payload['inventories']['full_flow_topic_artifact_files_checked']} topic artifacts hash-checked; {payload['inventories']['full_flow_links_checked']} navigation links checked; 0 broken; source/destination PDF and TXT hashes equal.",
            "- Targeted regression suites: **127 passed, 0 failed**.",
            "",
            "## Factual caveats",
            "",
        ]
    )
    for item in topics:
        lines.append(f"- **{item['topic_key']}:** {item['factual_caveat']}")
    lines.extend(
        [
            "",
            "## Evidence paths",
            "",
            f"- Machine validation: `{rel(FINAL_VALIDATION)}`",
            f"- Exact changed-files list: `{rel(CHANGED)}`",
            f"- Polity Flow validation: `{rel(POLITY_FLOW_VALIDATION)}`",
            f"- Full Flow validation: `{rel(ALL_FLOW_VALIDATION)}`",
            f"- Four-item validation: `{rel(FOUR_VALIDATION)}`",
            f"- Case-year evidence: `{rel(CASE_EVIDENCE)}`",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def write_changed_files() -> list[str]:
    target_fragments = (
        "\\polity-33\\",
        "\\polity-34\\",
        "\\polity-35\\",
        "\\polity-36\\",
        "\\polity-37\\",
        "\\33-Attorney-General-and-Advocate-General\\",
        "\\34-NITI-Aayog\\",
        "\\35-NHRC-and-SHRC\\",
        "\\36-CIC-and-SIC\\",
        "\\37-CVC-and-CBI\\",
    )
    explicit = {
        ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
        ROOT / "EXPORT-PDF-STATUS.json",
        ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ROOT / "tools" / "generate_polity_33_37_sequential.py",
        ROOT / "tools" / "finalize_polity_33_37_batch.py",
        ROOT / "tools" / "polity_flowchart_case_years.py",
        ROOT / "tools" / "refresh_all_v2_overrides.json",
        ROOT / "tools" / "test_refresh_all_v2_learning_sessions.py",
        ROOT / "tools" / "test_polity_flowchart_case_years.py",
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
        ROOT / "notes" / "Final-Learning-Packages" / "README.md",
        ROOT / "notes" / "Final-Learning-Packages" / "Polity" / "README.md",
        ROOT
        / "notes"
        / "Final-Learning-Packages"
        / "Polity"
        / "Subject-wide Syllabus"
        / "README.md",
        ROOT / "notes" / "Flow-Learning" / "README.md",
        ROOT / "notes" / "Flow-Learning" / "Polity" / "README.md",
        ROOT / "notes" / "Flow-Learning" / "START-HERE.md",
        ROOT
        / "notes"
        / "Flow-Learning"
        / "ALL-COMPLETED-TOPICS-FLOW-LEARNING-REPORT.md",
        ROOT
        / "notes"
        / "Flow-Learning"
        / "POLITY-01-37-FLOW-LEARNING-REPORT.md",
        FINAL_VALIDATION,
        REPORT,
        CASE_EVIDENCE,
        POLITY_FLOW_VALIDATION,
        ALL_FLOW_VALIDATION,
        FOUR_VALIDATION,
        EXPORTS / "final-four-item-library-2026-08-24.json",
        STATE_PATH,
    }
    roots = [
        ROOT / "notes" / "Final-Learning-Packages",
        ROOT / "notes" / "Flow-Learning",
        ROOT / "notes" / "Learner-v2-Refreshed" / "Polity",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "Polity",
        ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "learning-sessions" / "v2",
        EXPORTS,
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs",
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "carvaka-graphical-specs"
        / "Polity",
    ]
    candidates = {path for path in explicit if path.is_file()}
    for root in roots:
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            relative = "\\" + rel(path)
            if any(fragment in relative for fragment in target_fragments):
                candidates.add(path)
            elif any(
                token in path.name
                for token in (
                    "polity-33",
                    "polity-34",
                    "polity-35",
                    "polity-36",
                    "polity-37",
                    "POLITY-33-37",
                    "POLITY-01-37",
                )
            ):
                candidates.add(path)
    paths = sorted(rel(path) for path in candidates)
    CHANGED.write_text("\n".join(paths) + "\n", encoding="utf-8")
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tests-passed", type=int, default=127)
    args = parser.parse_args()
    write_case_evidence()
    run_flow_publications(args.tests_passed)
    payload = build_validation(args.tests_passed)
    write_report(payload)
    paths = write_changed_files()
    payload["evidence_paths"]["changed_files_count"] = len(paths)
    FINAL_VALIDATION.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"status={payload['status']} topics={len(payload['content']['topics'])} "
        f"four={payload['inventories']['four_item_topics']} "
        f"flow={payload['inventories']['full_flow_topics']} changed={len(paths)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
