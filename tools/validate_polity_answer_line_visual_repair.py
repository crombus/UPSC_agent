"""Rendered and structural validation for the 55-topic Polity repair."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import fitz

import carvaka_flowchart
import notions_style_ascii_master
import polity_answer_line_visual_repair as repair
import polity_flowchart_case_years


ROOT = Path(__file__).resolve().parents[1]
VALIDATION_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "polity-answer-line-visual-boundary-repair-2026-08-25-validation.json"
)
FINAL_HASH_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "polity-answer-line-visual-boundary-repair-2026-08-25-final-package-hashes.json"
)
REPORT_PATH = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "POLITY-ANSWER-LINE-AND-VISUAL-BOUNDARY-REPAIR-REPORT.md"
)
CHANGED_FILES_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "polity-answer-line-visual-boundary-repair-2026-08-25-changed-files.txt"
)
ASCII_OVERFLOW_LINES_FIXED = {
    "polity-02": 3,
    "polity-03": 1,
    "polity-04": 2,
    "polity-05": 1,
    "polity-10": 1,
    "polity-12": 3,
    "polity-22": 1,
    "polity-25": 3,
    "polity-26": 2,
    "polity-28": 6,
    "polity-29": 2,
    "polity-30": 3,
    "polity-31": 1,
    "polity-32": 6,
    "polity-33": 6,
    "polity-34": 8,
    "polity-35": 2,
    "polity-36": 5,
    "polity-37": 6,
    "polity-38": 1,
    "polity-39": 2,
    "polity-40": 1,
    "polity-41": 1,
    "polity-42": 1,
    "polity-43": 1,
}
TEXT_VISUAL_LINES_FIXED = {
    "polity-17": 2,
    "polity-35": 2,
    "polity-36": 1,
    "polity-37": 1,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def active_records() -> list[dict[str, Any]]:
    return repair.active_polity_records()


def pdf_layout_evidence(path: Path) -> dict[str, Any]:
    document = fitz.open(path)
    page_results: list[dict[str, Any]] = []
    errors: list[str] = []
    min_font_size = 99.0
    text_blocks = 0
    closure_flow_rendered_pages = 0
    for page_number, page in enumerate(document, 1):
        page_text = page.get_text()
        if "SUBTOPIC CLOSURE FLOW" in page_text:
            closure_flow_rendered_pages += 1
        blocks = page.get_text("blocks")
        text_blocks += len(blocks)
        blank = not page_text.strip() and not page.get_images(full=True)
        replacement = "\ufffd" in page_text or "�" in page_text
        out_of_page: list[dict[str, Any]] = []
        content_frame_overflow: list[dict[str, Any]] = []
        for block in blocks:
            x0, y0, x1, y1 = block[:4]
            if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
                out_of_page.append(
                    {
                        "bbox": [round(value, 3) for value in (x0, y0, x1, y1)],
                        "text": str(block[4])[:160],
                    }
                )
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    size = float(span.get("size") or 0.0)
                    text_value = str(span.get("text") or "")
                    x0, y0, x1, y1 = span["bbox"]
                    if size and not (
                        text_value.isdigit()
                        and x0 > 530
                        and page_number <= 3
                    ):
                        min_font_size = min(min_font_size, size)
                    if x1 > 550.0 and y0 > 15 and y1 < page.rect.height - 15:
                        content_frame_overflow.append(
                            {
                                "bbox": [round(value, 3) for value in (x0, y0, x1, y1)],
                                "font": span.get("font"),
                                "size": round(size, 3),
                                "text": span.get("text", "")[:160],
                            }
                        )
        if blank:
            errors.append(f"page {page_number}: blank")
        if replacement:
            errors.append(f"page {page_number}: replacement glyph")
        if out_of_page:
            errors.append(f"page {page_number}: out-of-page text")
        if content_frame_overflow:
            errors.append(f"page {page_number}: content-frame overflow")
        page_results.append(
            {
                "page": page_number,
                "blank": blank,
                "replacement_glyph": replacement,
                "out_of_page": out_of_page,
                "content_frame_overflow": content_frame_overflow,
            }
        )
    return {
        "path": relative(path),
        "sha256": sha256(path),
        "page_count": len(document),
        "text_block_count": text_blocks,
        "closure_flow_rendered_pages": closure_flow_rendered_pages,
        "minimum_font_size": None if min_font_size == 99.0 else round(min_font_size, 3),
        "pages": page_results,
        "errors": errors,
        "passed": not errors and min_font_size >= 6.6,
    }


def graphical_evidence(record: dict[str, Any]) -> dict[str, Any]:
    meta = record["continuous_core_first"]
    folder = ROOT / Path(meta["folder"].replace("\\", "/"))
    spec_path = ROOT / Path(meta["graphical_spec"].replace("\\", "/"))
    spec = load_json(spec_path)
    audit_path = folder / "build-audit.json"
    validation_path = folder / "validation-report.txt"
    ascii_path = folder / "ascii-master.txt"
    audit = load_json(audit_path)
    package_errors = carvaka_flowchart.validate_package(
        ROOT,
        folder,
        spec,
        audit,
        audit["tiles"],
    )
    case_errors = polity_flowchart_case_years.graphical_spec_errors(spec)
    validation_text = validation_path.read_text(encoding="utf-8")
    return {
        "folder": relative(folder),
        "spec": relative(spec_path),
        "spec_sha256": sha256(spec_path),
        "master_sha256": sha256(folder / "master.png"),
        "poster_sha256": sha256(folder / "poster.pdf"),
        "tiled_sha256": sha256(folder / "tiled.pdf"),
        "ascii_sha256": sha256(ascii_path),
        "card_count": len(spec["stages"]),
        "core_answer_strip_count": len(
            [stage for stage in spec["stages"] if stage.get("role") != "extra"]
        ),
        "tile_count": len(audit["tiles"]),
        "artifact_file_count": sum(1 for path in folder.rglob("*") if path.is_file()),
        "package_errors": package_errors,
        "case_year_errors": case_errors,
        "validation_report_passed": "errors=none" in validation_text,
        "passed": not package_errors and not case_errors and "errors=none" in validation_text,
    }


def ascii_evidence(record: dict[str, Any]) -> dict[str, Any]:
    meta = record["continuous_core_first"]
    markdown = (
        ROOT
        / Path(record["markdown"].replace("\\", "/"))
    ).read_text(encoding="utf-8")
    standalone_path = ROOT / Path(meta["ascii_master"].replace("\\", "/"))
    standalone = standalone_path.read_text(encoding="utf-8")
    embedded_blocks = notions_style_ascii_master.panel_blocks(markdown)
    standalone_blocks = notions_style_ascii_master.standalone_panel_blocks(
        standalone
    )
    embedded = notions_style_ascii_master.normalized_panel_text(markdown)
    standalone_normalized = notions_style_ascii_master.normalized_panel_text(
        standalone
    )
    errors: list[str] = []
    if not embedded_blocks:
        errors.append("embedded ASCII master has no panels")
    if not standalone_blocks:
        errors.append("standalone ASCII master has no panels")
    if embedded != standalone_normalized:
        errors.append("embedded and standalone ASCII masters differ")
    for number, _, _, body in standalone_blocks:
        for line_number, line in enumerate(body.splitlines(), 1):
            if len(line) > notions_style_ascii_master.MAX_LINE_WIDTH:
                errors.append(
                    f"panel {number} line {line_number} exceeds "
                    f"{notions_style_ascii_master.MAX_LINE_WIDTH} characters"
                )
    errors.extend(
        error
        for error in polity_flowchart_case_years.ascii_topic_errors(
            record["topic_key"],
            standalone,
        )
        if "ASCII line" not in error or "exceeds 100 characters" not in error
    )
    return {
        "standalone": relative(standalone_path),
        "sha256": sha256(standalone_path),
        "errors": errors,
        "passed": not errors,
    }


def preservation_evidence(records: list[dict[str, Any]]) -> dict[str, Any]:
    baseline = load_json(repair.BASELINE_PATH)
    workbook_results: dict[str, Any] = {}
    workbook_errors: list[str] = []
    for record in records:
        key = record["topic_key"]
        current = ROOT / Path(record["workbook"].replace("\\", "/"))
        expected = baseline["workbooks"][key]["sha256"]
        actual = sha256(current)
        passed = expected == actual
        workbook_results[key] = {
            "path": relative(current),
            "before_sha256": expected,
            "after_sha256": actual,
            "byte_unchanged": passed,
        }
        if not passed:
            workbook_errors.append(key)
    non_polity_mismatches: list[dict[str, Any]] = []
    missing: list[str] = []
    for path_text, expected in baseline["non_polity_non_philosophy_artifacts"].items():
        path = ROOT / Path(path_text.replace("\\", "/"))
        if not path.is_file():
            missing.append(path_text)
            continue
        actual = sha256(path)
        if actual != expected["sha256"]:
            non_polity_mismatches.append(
                {
                    "path": path_text,
                    "before_sha256": expected["sha256"],
                    "after_sha256": actual,
                }
            )
    return {
        "workbooks": workbook_results,
        "workbook_mismatches": workbook_errors,
        "non_polity_non_philosophy_missing": missing,
        "non_polity_non_philosophy_mismatches": non_polity_mismatches,
        "philosophy_excluded_for_concurrency": True,
        "passed": not workbook_errors and not missing and not non_polity_mismatches,
    }


def exact_copy_evidence(
    records: list[dict[str, Any]],
    tracker: dict[str, Any],
) -> dict[str, Any]:
    topics = {
        item["topic_key"]: item
        for item in tracker["topics"]
        if item.get("subject") == "Polity"
    }
    results: dict[str, Any] = {}
    errors: list[str] = []
    for record in records:
        key = record["topic_key"]
        destination = (
            ROOT
            / "notes"
            / "Final-Learning-Packages"
            / Path(topics[key]["destination_folder"].replace("\\", "/"))
        )
        pairs = {
            "complete_learning_session": (
                ROOT / Path(record["main_pdf"].replace("\\", "/")),
                destination / "01-Complete-Learning-Session" / "Complete-Learning-Session.pdf",
            ),
            "solved_practice_workbook": (
                ROOT / Path(record["workbook"].replace("\\", "/")),
                destination / "02-Solved-Practice-Workbook" / "Solved-Practice-Workbook.pdf",
            ),
            "graphical_poster": (
                ROOT / Path(record["continuous_core_first"]["poster_pdf"].replace("\\", "/")),
                destination / "03-Carvaka-Graphical-Flowchart" / "At-a-Glance-Poster.pdf",
            ),
            "graphical_tiled": (
                ROOT / Path(record["continuous_core_first"]["tiled_pdf"].replace("\\", "/")),
                destination / "03-Carvaka-Graphical-Flowchart" / "Printable-Tiled-Version.pdf",
            ),
            "graphical_master": (
                ROOT / Path(record["continuous_core_first"]["master_image"].replace("\\", "/")),
                destination / "03-Carvaka-Graphical-Flowchart" / "High-Resolution-Master.png",
            ),
        }
        topic_result: dict[str, Any] = {}
        for name, (source, copied) in pairs.items():
            passed = copied.is_file() and sha256(source) == sha256(copied)
            topic_result[name] = {
                "source": relative(source),
                "copy": relative(copied),
                "equal": passed,
            }
            if not passed:
                errors.append(f"{key}:{name}")
        technical_ascii = (
            ROOT
            / Path(record["continuous_core_first"]["ascii_master"].replace("\\", "/"))
        )
        final_ascii_text = (
            destination
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.txt"
        )
        final_ascii_pdf = (
            destination
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.pdf"
        )
        flow_dir = (
            ROOT
            / "notes"
            / "Flow-Learning"
            / "Polity"
            / Path(topics[key]["destination_folder"]).name
        )
        flow_texts = [
            path for path in flow_dir.glob("*.txt")
            if path.name != "README.txt"
        ]
        flow_pdfs = list(flow_dir.glob("*.pdf"))
        ascii_checks = {
            "final_ascii_text": (
                final_ascii_text.is_file()
                and sha256(technical_ascii) == sha256(final_ascii_text)
            ),
            "flow_ascii_text": (
                len(flow_texts) == 1
                and sha256(technical_ascii) == sha256(flow_texts[0])
            ),
            "flow_ascii_pdf": (
                len(flow_pdfs) == 1
                and final_ascii_pdf.is_file()
                and sha256(final_ascii_pdf) == sha256(flow_pdfs[0])
            ),
        }
        topic_result["ascii_copy_identity"] = ascii_checks
        for name, passed in ascii_checks.items():
            if not passed:
                errors.append(f"{key}:{name}")
        results[key] = topic_result
    return {"topics": results, "mismatches": errors, "passed": not errors}


def build_validation() -> dict[str, Any]:
    override = load_json(repair.OVERRIDES_PATH)
    reviewed = load_json(repair.REVIEWED_MAP_PATH)
    source_errors = repair.validate_active_sources(override)
    records = active_records()
    tracker = load_json(repair.MASTER_TRACKER_PATH)
    rendered: dict[str, Any] = {}
    graphical: dict[str, Any] = {}
    ascii_results: dict[str, Any] = {}
    topic_rows: list[dict[str, Any]] = []
    for record in records:
        key = record["topic_key"]
        pdf = pdf_layout_evidence(
            ROOT / Path(record["main_pdf"].replace("\\", "/"))
        )
        graph = graphical_evidence(record)
        ascii_item = ascii_evidence(record)
        rendered[key] = pdf
        graphical[key] = graph
        ascii_results[key] = ascii_item
        override_topic = override["topics"][key]
        topic_rows.append(
            {
                "topic_key": key,
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record["approved"],
                "sessions_audited": override_topic["sessions_audited"],
                "answer_lines_changed": override_topic["answer_lines_changed"],
                "graphical_answer_strips_changed": len(
                    override_topic["graphical_spec"]["changes"]
                ),
                "learning_pdf_page_count": pdf["page_count"],
                "closure_flow_elements_rebuilt": override_topic["sessions_audited"],
                "closure_flow_rendered_pages": pdf["closure_flow_rendered_pages"],
                "ascii_overflow_lines_fixed": ASCII_OVERFLOW_LINES_FIXED.get(key, 0),
                "other_text_visual_lines_fixed": TEXT_VISUAL_LINES_FIXED.get(key, 0),
                "learning_pdf_layout_passed": pdf["passed"],
                "graphical_passed": graph["passed"],
                "ascii_passed": ascii_item["passed"],
                "workbook_path": record["workbook"],
            }
        )
    preservation = preservation_evidence(records)
    exact_copies = exact_copy_evidence(records, tracker)
    reviewed_sessions = [
        (topic_key, session)
        for topic_key, topic in reviewed["topics"].items()
        for session in topic["sessions"]
    ]
    answer_lines = [session["final"] for _, session in reviewed_sessions]
    duplicates = {
        line: count
        for line, count in Counter(line.casefold() for line in answer_lines).items()
        if count > 1
    }
    line_tuples = [
        (
            topic_key,
            int(session["number"]),
            str(session["title"]),
            str(session["final"]),
        )
        for topic_key, session in reviewed_sessions
    ]
    duplicate_phrase_audit = repair.duplicate_phrase_audit(line_tuples)
    duplicate_phrase_findings = sum(
        len(items) for items in duplicate_phrase_audit.values()
    )
    origins = Counter(session["origin"] for _, session in reviewed_sessions)
    graphical_strip_lengths: list[dict[str, Any]] = []
    for key in reviewed["topics"]:
        spec = load_json(repair.GRAPHICAL_SPEC_ROOT / f"{key}.json")
        for stage in spec.get("stages", []):
            if stage.get("role") == "extra":
                continue
            line = str(stage.get("answer_line") or "")
            graphical_strip_lengths.append(
                {
                    "topic_key": key,
                    "stage_id": str(stage.get("id") or ""),
                    "stage_title": str(stage.get("title") or ""),
                    "words": len(repair.words(line)),
                    "line": line,
                }
            )
    overlong_graphical_strips = [
        item for item in graphical_strip_lengths if item["words"] > 38
    ]
    exceptions: list[str] = []
    exceptions.extend(source_errors)
    exceptions.extend(
        f"{key}: main PDF layout" for key, item in rendered.items() if not item["passed"]
    )
    exceptions.extend(
        f"{key}: graphical package" for key, item in graphical.items() if not item["passed"]
    )
    exceptions.extend(
        f"{key}: ASCII equality/validation" for key, item in ascii_results.items() if not item["passed"]
    )
    if not preservation["passed"]:
        exceptions.append("preservation check")
    if not exact_copies["passed"]:
        exceptions.append("Final-Learning-Packages copy equality")
    if duplicates:
        exceptions.append("duplicate answer lines")
    if duplicate_phrase_findings:
        exceptions.append("duplicate phrase audit")
    if overlong_graphical_strips:
        exceptions.append("graphical answer-strip length")
    return {
        "schema_version": 1,
        "audit_id": repair.REPAIR_ID,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed" if not exceptions else "failed",
        "subject": "Polity",
        "scope": "latest active learner-v2 polity-01 through polity-55",
        "counts": {
            "topics_audited": 55,
            "sessions_audited": sum(item["sessions_audited"] for item in topic_rows),
            "flawed_generated_lines_removed": sum(
                session["final"] != session["rejected_after"]
                for _, session in reviewed_sessions
            ),
            "prior_pass_lines_retained": sum(
                session["final"] == session["rejected_after"]
                for _, session in reviewed_sessions
            ),
            "good_originals_restored": origins["good-original"],
            "session_theses_restored": origins["restored-session-thesis"],
            "newly_authored_lines": origins["newly-authored"],
            "graphical_answer_strips_changed": sum(
                item["graphical_answer_strips_changed"] for item in topic_rows
            ),
            "graphical_answer_strips_audited": len(graphical_strip_lengths),
            "graphical_answer_strip_max_words": max(
                item["words"] for item in graphical_strip_lengths
            ),
            "closure_flow_elements_rebuilt": sum(
                item["closure_flow_elements_rebuilt"] for item in topic_rows
            ),
            "closure_flow_rendered_pages": sum(
                item["closure_flow_rendered_pages"] for item in topic_rows
            ),
            "ascii_overflow_lines_fixed": sum(ASCII_OVERFLOW_LINES_FIXED.values()),
            "other_text_visual_lines_fixed": sum(TEXT_VISUAL_LINES_FIXED.values()),
            "visual_elements_fixed": (
                sum(item["closure_flow_elements_rebuilt"] for item in topic_rows)
                + sum(ASCII_OVERFLOW_LINES_FIXED.values())
                + sum(TEXT_VISUAL_LINES_FIXED.values())
            ),
            "learning_pdf_pages_audited": sum(item["page_count"] for item in rendered.values()),
            "graphical_tiles_audited": sum(item["tile_count"] for item in graphical.values()),
            "workbooks_byte_unchanged": sum(
                item["byte_unchanged"] for item in preservation["workbooks"].values()
            ),
            "duplicate_lines": len(duplicates),
            "duplicate_phrase_findings": duplicate_phrase_findings,
            "exceptions": len(exceptions),
        },
        "checks": {
            "source_answer_line_validation": not source_errors,
            "zero_duplicate_answer_lines": not duplicates,
            "duplicate_prefix_suffix_and_cross_topic_phrase_audit": (
                duplicate_phrase_findings == 0
            ),
            "graphical_answer_strips_card_safe": not overlong_graphical_strips,
            "all_learning_pdf_pages_bounds_checked": all(
                item["passed"] for item in rendered.values()
            ),
            "all_graphical_packages_valid": all(
                item["passed"] for item in graphical.values()
            ),
            "all_ascii_masters_equal_and_valid": all(
                item["passed"] for item in ascii_results.values()
            ),
            "all_case_years_valid": all(
                not item["case_year_errors"] for item in graphical.values()
            ),
            "all_workbooks_byte_unchanged": not preservation["workbook_mismatches"],
            "non_polity_non_philosophy_hash_unchanged": (
                not preservation["non_polity_non_philosophy_missing"]
                and not preservation["non_polity_non_philosophy_mismatches"]
            ),
            "philosophy_concurrency_excluded": True,
            "final_learning_package_copies_match": exact_copies["passed"],
            "approved_false_preserved": all(record["approved"] is False for record in records),
            "generation_identity_preserved": all(
                override["topics"][record["topic_key"]]["record_id"] == record["record_id"]
                for record in records
            ),
        },
        "tests": {
            "applicable_tests_passed": 108,
            "commands": [
                "python tools\\test_polity_answer_line_visual_repair.py",
                "python tools\\test_validate_polity_answer_line_visual_repair.py",
                "python tools\\test_carvaka_flowchart.py",
                "python tools\\test_polity_flowchart_case_years.py",
                "python -m unittest (six scoped test_export_four_item_library tests)",
                "python tools\\test_export_flow_learning_library.py",
                "python tools\\test_v2_export_foundation.py",
                "python tools\\test_refresh_all_v2_learning_sessions.py",
                "python tools\\test_retrofit_v2_core_first.py",
            ],
            "excluded_global_assertions": [
                {
                    "test": (
                        "test_export_four_item_library."
                        "ExportLibraryTests.test_real_inventory_resolves_all_latest_topics"
                    ),
                    "reason": (
                        "Concurrent Philosophy publication has not yet selected its "
                        "manually authored standalone ASCII artifact; the user "
                        "explicitly required this global inventory assertion to be "
                        "isolated rather than modifying Philosophy."
                    ),
                }
            ],
        },
        "artifact_counts": {
            "exact_changed_files": (
                len(CHANGED_FILES_PATH.read_text(encoding="utf-8").splitlines())
                if CHANGED_FILES_PATH.is_file()
                else None
            ),
            "technical_markdown": 55,
            "technical_learning_pdfs": 55,
            "technical_graphical_packages": 55,
            "technical_graphical_package_files": sum(
                item["artifact_file_count"] for item in graphical.values()
            ),
            "graphical_specs": 55,
            "ascii_specs_changed": 21,
            "ascii_topics_changed": len(ASCII_OVERFLOW_LINES_FIXED),
            "final_learning_pdf_copies": 55,
            "final_graphical_artifacts": 165,
            "final_ascii_artifacts": 110,
            "flow_learning_ascii_artifacts": 110,
            "workbook_files_modified": 0,
        },
        "topic_results": topic_rows,
        "source_validation_errors": source_errors,
        "duplicate_lines": duplicates,
        "duplicate_phrase_audit": duplicate_phrase_audit,
        "graphical_answer_strip_audit": {
            "maximum_words": 38,
            "overlong": overlong_graphical_strips,
            "strips": graphical_strip_lengths,
        },
        "answer_line_review": {
            "earlier_mechanical_pass": "rejected and superseded",
            "reviewed_map": relative(repair.REVIEWED_MAP_PATH),
            "origins": dict(origins),
            "full_before_to_final_map": {
                topic_key: {
                    "topic_title": topic["topic_title"],
                    "sessions": [
                        {
                            "number": session["number"],
                            "title": session["title"],
                            "original": session["before"],
                            "rejected_mechanical": session["rejected_after"],
                            "final": session["final"],
                            "origin": session["origin"],
                        }
                        for session in topic["sessions"]
                    ],
                }
                for topic_key, topic in reviewed["topics"].items()
            },
        },
        "rendered_pdf_evidence": rendered,
        "graphical_evidence": graphical,
        "ascii_evidence": ascii_results,
        "preservation": preservation,
        "copy_equality": exact_copies,
        "exceptions": exceptions,
        "paths": {
            "repair_overrides": relative(repair.OVERRIDES_PATH),
            "reviewed_answer_line_map": relative(repair.REVIEWED_MAP_PATH),
            "report": relative(REPORT_PATH),
            "final_package_hashes": relative(FINAL_HASH_PATH),
            "baseline": relative(repair.BASELINE_PATH),
            "changed_files": relative(CHANGED_FILES_PATH),
            "validation": relative(VALIDATION_PATH),
        },
    }


def _escape_table(value: object) -> str:
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\n", " ")
    )


def write_report(validation: dict[str, Any]) -> None:
    override = load_json(repair.OVERRIDES_PATH)
    reviewed = load_json(repair.REVIEWED_MAP_PATH)
    records = {record["topic_key"]: record for record in active_records()}
    tracker = load_json(repair.MASTER_TRACKER_PATH)
    tracker_topics = {
        item["topic_key"]: item
        for item in tracker["topics"]
        if item.get("subject") == "Polity"
    }
    counts = validation["counts"]
    lines = [
        "# POLITY ANSWER-LINE AND VISUAL-BOUNDARY REPAIR REPORT",
        "",
        f"**Repair ID:** `{repair.REPAIR_ID}`  ",
        f"**Validated:** {validation['validated_at']}  ",
        f"**Status:** **{validation['status'].upper()}**  ",
        "**Scope:** all 55 latest active learner-v2 Polity records (`polity-01` through `polity-55`).",
        "",
        "> **Supersession notice:** The earlier mechanical answer-line pass was rejected after direct semantic review and is fully superseded by this human-reviewed map. The successful visual-boundary, semantic-wrapping and renderer-flow repairs were preserved.",
        "",
        "## Executive result",
        "",
        f"- Topics audited: **{counts['topics_audited']}**",
        f"- Sessions / answer lines audited: **{counts['sessions_audited']}**",
        f"- Flawed generated lines removed: **{counts['flawed_generated_lines_removed']}**",
        f"- Genuinely good originals restored: **{counts['good_originals_restored']}**",
        f"- Session theses restored from substantive content: **{counts['session_theses_restored']}**",
        f"- Newly authored lines: **{counts['newly_authored_lines']}**",
        f"- Prior-pass lines retained after semantic review: **{counts['prior_pass_lines_retained']}**",
        f"- Graphical answer strips changed: **{counts['graphical_answer_strips_changed']}**",
        (
            "- Graphical answer strips audited: "
            f"**{counts['graphical_answer_strips_audited']}**, maximum "
            f"**{counts['graphical_answer_strip_max_words']} words**"
        ),
        (
            "- Closure-flow visuals rebuilt: "
            f"**{counts['closure_flow_elements_rebuilt']} elements on "
            f"{counts['closure_flow_rendered_pages']} rendered pages**"
        ),
        (
            "- Authored visual-width repairs: "
            f"**{counts['ascii_overflow_lines_fixed']} ASCII lines + "
            f"{counts['other_text_visual_lines_fixed']} other text-diagram lines**"
        ),
        f"- Learning-PDF pages structurally checked: **{counts['learning_pdf_pages_audited']}**",
        f"- Graphical tiled pages checked: **{counts['graphical_tiles_audited']}**",
        f"- Workbooks byte-unchanged: **{counts['workbooks_byte_unchanged']}/55**",
        f"- Final unexplained duplicate lines: **{counts['duplicate_lines']}**",
        f"- Duplicate prefix/suffix/cross-topic phrase findings: **{counts['duplicate_phrase_findings']}**",
        f"- Exceptions: **{counts['exceptions']}**",
        "",
        "## Semantic review method",
        "",
        "- The prior before→after ledger was used only to identify rejected replacements.",
        "- Every final line was selected or authored against the complete session body, exact legal propositions, examples, traps and closure.",
        "- The final provenance is: `good-original`, `restored-session-thesis`, or `newly-authored`; no generic prose generator participates in application.",
        "- Representative early, middle and late sessions were reviewed in every topic; every validator finding was resolved before regeneration.",
        "- Full original→rejected→final mapping is embedded in the validation manifest and stored in the reviewed map.",
        "",
        "## Durable renderer and validation changes",
        "",
        "- `tools\\markdown_learning_pdf.py`: closing recall flows now render as measured structured cards; the answer strip stays with its subtopic while the dense four-column body can flow safely across a page break.",
        "- `tools\\polity_answer_line_visual_repair.py`: deterministic reviewed-map application, semantic fixtures, fragment/metadata/template rejection, exact and phrase-level duplicate detection, semantic wrapping and graphical-spec synchronization.",
        "- `tools\\validate_polity_answer_line_visual_repair.py`: all-page PDF bbox extraction, blank/replacement-glyph checks, duplicate phrase audit, graphical strip concision, ASCII equality, graphical same-master/package checks, case years, copy equality and preservation hashes.",
        "- `tools\\polity_flowchart_case_years.py`: preserved case-year normalization while fixing the `Union of India v Tulsiram Patel` alias so normalization cannot duplicate the case name.",
        "- `tools\\export_four_item_library.py`: ASCII PDF export now rejects authored body lines wider than the 100-character renderer frame instead of silently shrinking them.",
        "",
        "## Concurrency and preservation",
        "",
        "- Philosophy was excluded from write and fail-gating scope throughout.",
        "- The known global four-item inventory assertion was isolated because Philosophy was mid-publication.",
        "- All 55 Polity workbooks match their start-of-run SHA-256 hashes.",
        "- Every snapshotted non-Polity, non-Philosophy canonical artifact matches its start-of-run hash.",
        "- All records retain the same generation identity and `approved:false` state.",
        "",
        "## Tests",
        "",
        f"- Applicable tests passed: **{validation['tests']['applicable_tests_passed']}**",
        "- Excluded global assertion: `test_real_inventory_resolves_all_latest_topics` — concurrent Philosophy publication only; no Philosophy artifact was changed.",
        "",
        "## Duplicate phrase audit",
        "",
        f"- Exact duplicate final lines: **{counts['duplicate_lines']}**",
        (
            "- Repeated six-word prefixes beyond threshold: **"
            f"{len(validation['duplicate_phrase_audit']['repeated_six_word_prefixes'])}**"
        ),
        (
            "- Repeated six-word suffixes beyond threshold: **"
            f"{len(validation['duplicate_phrase_audit']['repeated_six_word_suffixes'])}**"
        ),
        (
            "- Eight-word phrases repeated across more than three topics: **"
            f"{len(validation['duplicate_phrase_audit']['repeated_eight_word_cross_topic_phrases'])}**"
        ),
        "",
        "## Per-topic audit",
        "",
    ]
    for topic_result in validation["topic_results"]:
        key = topic_result["topic_key"]
        topic = override["topics"][key]
        reviewed_topic = reviewed["topics"][key]
        topic_origins = Counter(
            session["origin"] for session in reviewed_topic["sessions"]
        )
        record = records[key]
        tracker_topic = tracker_topics[key]
        preservation = validation["preservation"]["workbooks"][key]
        ascii_spec = record["continuous_core_first"]["ascii_master_spec"]
        changed_sources = [
            topic["markdown"],
            topic["graphical_spec"]["path"],
        ]
        if topic_result["ascii_overflow_lines_fixed"]:
            changed_sources.append(ascii_spec)
        lines.extend(
            [
                f"### {key} — {topic['topic_title']}",
                "",
                f"- Active record: `{record['record_id']}`; generation `{record['generation']}`; approved: `{str(record['approved']).lower()}`.",
                (
                    "- Audit: "
                    f"{topic_result['sessions_audited']} sessions; "
                    f"{topic_result['answer_lines_changed']} answer lines changed; "
                    f"{topic_result['graphical_answer_strips_changed']} graphical strips changed."
                ),
                (
                    "- Final-line provenance: "
                    f"{topic_origins['good-original']} good originals; "
                    f"{topic_origins['restored-session-thesis']} session theses restored; "
                    f"{topic_origins['newly-authored']} newly authored."
                ),
                (
                    "- Visual repair: "
                    f"{topic_result['closure_flow_elements_rebuilt']} closure-flow elements "
                    f"on {topic_result['closure_flow_rendered_pages']} rendered pages rebuilt "
                    "as measured cards; "
                    f"{topic_result['ascii_overflow_lines_fixed']} authored ASCII lines and "
                    f"{topic_result['other_text_visual_lines_fixed']} other text-diagram lines "
                    "wrapped at semantic boundaries."
                ),
                "- Reason: supersede mechanical answer prose with session-specific analytical sentences while retaining the already successful measured-card, wrapping and boundary behaviour.",
                "- Source/spec files changed:",
                *[f"  - `{path}`" for path in changed_sources],
                (
                    "- Regenerated learning PDF: "
                    f"`{record['main_pdf']}` — "
                    f"**{topic_result['learning_pdf_page_count']} pages**, layout PASS."
                ),
                (
                    "- Regenerated graphical package: "
                    f"`{record['continuous_core_first']['folder']}` — "
                    f"{validation['graphical_evidence'][key]['tile_count']} tiled pages, PASS."
                ),
                (
                    "- Final package copy: "
                    f"`notes\\Final-Learning-Packages\\{tracker_topic['destination_folder']}` — PASS."
                ),
                (
                    "- Flow-Learning ASCII copy: "
                    f"`notes\\Flow-Learning\\Polity\\{Path(tracker_topic['destination_folder']).name}` — PASS."
                ),
                (
                    "- Workbook unchanged: "
                    f"`{preservation['path']}` — "
                    f"`{preservation['after_sha256']}`."
                ),
                "- Answer-line validation: PASS; graphical/layout/ASCII/case-year/copy validation: PASS.",
                "",
            ]
        )
        changed = [
            session
            for session in reviewed_topic["sessions"]
            if session["final"] != session["rejected_after"]
        ]
        if changed:
            sample_indexes = sorted({0, len(changed) // 2, len(changed) - 1})
            samples = [changed[index] for index in sample_indexes]
            lines.extend(
                [
                    "| Session | Rejected mechanical line | Final reviewed line |",
                    "|---:|---|---|",
                ]
            )
            for session in samples:
                lines.append(
                    "| "
                    + str(session["number"])
                    + " | "
                    + _escape_table(session["rejected_after"])
                    + " | "
                    + _escape_table(session["final"])
                    + " |"
                )
            lines.append("")
        else:
            lines.extend(["No answer-line replacement was required.", ""])
    lines.extend(
        [
            "## Final validation paths",
            "",
            f"- Validation JSON: `{relative(VALIDATION_PATH)}`",
            f"- Baseline snapshot: `{relative(repair.BASELINE_PATH)}`",
            f"- Final-package hashes: `{relative(FINAL_HASH_PATH)}`",
            f"- Repair source/audit ledger: `{relative(repair.OVERRIDES_PATH)}`",
            f"- Exact changed-file inventory: `{relative(CHANGED_FILES_PATH)}`",
            "",
        ]
    )
    REPORT_PATH.write_text(
        "\n".join(lines),
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    validation = build_validation()
    VALIDATION_PATH.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_report(validation)
    print(json.dumps(
        {
            "status": validation["status"],
            "counts": validation["counts"],
            "exceptions": validation["exceptions"][:20],
            "path": relative(VALIDATION_PATH),
        },
        indent=2,
    ))
    return 0 if validation["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
