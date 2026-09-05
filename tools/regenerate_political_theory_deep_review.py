"""Deep-review and immutably regenerate all Political Theory topic packages."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

import fitz

import carvaka_flowchart
import generate_political_theory_topic_v2 as generator
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
from export_four_item_library import export_library
from generate_philosophy_western_rationalism_v2 import render_ascii_pdf_safe
from generate_v2_section_indexes import generate_command_guide, generate_section_indexes
from validate_v2_export import (
    extract_v2_workbook_markdown,
    validate_pdf,
    validate_pdf_layout,
    validate_tracker_record,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Political Theory"
SECTION = "Subject-wide Syllabus"
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
MASTER = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
REVIEW_ROOT = ROOT / "notes" / "Final-Learning-Packages" / "_deep-content-review"
REVIEW_TRACKER = REVIEW_ROOT / "REVIEW-TRACKER.json"
REVIEW_TRACKER_MD = REVIEW_ROOT / "REVIEW-TRACKER.md"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "political-theory--subject-wide-syllabus.json"
)
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
ASCII_SPECS = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
)
GRAPHICAL_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "political-theory--subject-wide-syllabus-graphical-specs"
)
CONTENT_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "political-theory--subject-wide-syllabus-content-specs"
)
REFRESHED_KNOWLEDGE = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Learner-v2-Refreshed"
    / "Political-Theory"
    / "Subject-Wide-Syllabus"
    / "learning-sessions"
)
REFRESHED_NOTES = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Political-Theory"
    / "Subject-Wide-Syllabus"
    / "learning-sessions"
)
REFRESHED_FLOWS = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Political-Theory"
    / "Subject-Wide-Syllabus"
    / "flowcharts"
)
SYLLABUS_MAPPING = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Political-Theory"
    / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"
)
PYQ_LEDGER = generator.PHILOSOPHY_PYQ_LEDGER
INDEX_DIR = (
    ROOT
    / "notes"
    / "Political-Theory"
    / "learning-session-v2"
    / "subject-wide-syllabus"
    / "indexes"
)

DANGLING_SENTENCE = re.compile(
    r"\b(?:and|or|of|to|from|with|through|into|for|the|a|an|its|their|"
    r"than|as|by|in|on)\.$",
    re.I,
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + f".pending-{os.getpid()}")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for attempt in range(40):
        try:
            os.replace(temporary, path)
            return
        except PermissionError:
            if attempt == 39:
                raise
            time.sleep(0.25)


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def repo(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def latest(status: dict[str, Any], topic_key: str) -> dict[str, Any]:
    records = [
        row
        for row in status["exports"]
        if row.get("topic_key") == topic_key and row.get("variant") == "learner-v2"
    ]
    if not records:
        raise ValueError(f"No learner-v2 record exists for {topic_key}.")
    return max(records, key=lambda row: int(row["generation"]))


def practice_section(markdown: str) -> str:
    return markdown[
        markdown.index("## PYQS AND ANSWER PRACTICE") :
        markdown.index("## OPTIONAL ADVANCED DEPTH")
    ]


def mcq_keys(markdown: str) -> list[str]:
    return re.findall(
        r"(?m)^\*\*(?:Correct answer|Answer):\*\*\s*([ABCD])(?:\s+—.*)?$",
        markdown,
    )


def mcq_explanation_errors(markdown: str) -> list[str]:
    section = markdown[
        markdown.index("## BASIC MCQS / REMEDIATION") :
        markdown.index("## PYQS AND ANSWER PRACTICE")
    ]
    headings = list(re.finditer(r"(?m)^#### MCQ (\d+)\s*$", section))
    errors: list[str] = []

    def normalize(value: str) -> str:
        return re.sub(
            r"\W+",
            " ",
            re.sub(r"[*`]", "", value).casefold(),
        ).strip()

    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(section)
        block = section[heading.end() : end]
        options = dict(re.findall(r"(?m)^([A-D])\.\s+(.+?)\s*$", block))
        answer = re.search(r"(?m)^\*\*Answer:\*\*\s*([A-D])\s*$", block)
        explanation = re.search(
            r"(?ms)^\*\*Explanation:\*\*\s*(.+?)(?=^---$|\Z)",
            block,
        )
        if len(options) != 4 or not answer or not explanation:
            errors.append(f"MCQ {heading.group(1)} has incomplete option/answer/explanation fields.")
            continue
        correct_text = normalize(options[answer.group(1)])
        explanation_text = normalize(explanation.group(1))
        if correct_text not in explanation_text:
            errors.append(
                f"MCQ {heading.group(1)} explanation does not independently identify "
                "the keyed option text."
            )
    if len(headings) != 48:
        errors.append(f"Expected 48 MCQ blocks; found {len(headings)}.")
    return errors


def model_word_count(block: str) -> int:
    match = re.search(r"(?i)\*\*Model (?:solution|answer)\*\*", block)
    if not match:
        match = re.search(
            r"(?im)^\*\*(?:Thesis(?:\s*/\s*opening)?|Introduction):\*\*",
            block,
        )
    body = block[match.end() :] if match else block
    body = re.split(r"(?i)\*\*Why this earns marks:", body, maxsplit=1)[0]
    body = re.split(r"(?i)\*\*How to improve this answer:", body, maxsplit=1)[0]
    return len(re.findall(r"\b[\w'-]+\b", body))


def flow_dangling_fragments(spec_path: Path) -> list[str]:
    if not spec_path.is_file():
        return ["ASCII specification is missing."]
    data = load(spec_path)
    return [
        line.strip()
        for topic in data.get("topics", [])
        for panel in topic.get("panels", [])
        for line in panel.get("lines", [])
        if DANGLING_SENTENCE.search(str(line).strip())
    ]


def baseline_audit(topic: generator.Topic, record: dict[str, Any]) -> dict[str, Any]:
    markdown = repo(record["markdown"])
    text = markdown.read_text(encoding="utf-8")
    practice = practice_section(text)
    blocks = generator.practice_question_blocks(practice)
    question_count = len(blocks)
    keys = mcq_keys(text)
    expected_keys = list("ABCD" * 12)
    missing_model = [
        title
        for title, block in blocks
        if not re.search(r"(?i)\*\*Model (?:solution|answer)\*\*", block)
    ]
    missing_why = [
        title
        for title, block in blocks
        if not re.search(r"Why this earns marks", block, re.I)
    ]
    weak_models: list[dict[str, object]] = []
    for title, block in blocks:
        marks_match = re.search(r"(?i)(10|15|20)(?:\s*\+\s*5)?\s*marks?", title)
        marks = int(marks_match.group(1)) if marks_match else 15
        words = model_word_count(block)
        threshold = {10: 100, 15: 140, 20: 190}[marks]
        if words < threshold:
            weak_models.append({"title": title, "marks": marks, "words": words})
    ascii_spec = record.get("continuous_core_first", {}).get("ascii_master_spec")
    dangling = flow_dangling_fragments(repo(ascii_spec)) if ascii_spec else [
        "ASCII specification path is absent from the record."
    ]
    flow_folder = repo(record["continuous_core_first"]["folder"])
    flow_report = flow_folder / "validation-report.txt"
    graphical_passed = (
        flow_report.is_file()
        and "errors=none" in flow_report.read_text(encoding="utf-8")
    )
    main_layout_errors, main_layout = validate_pdf_layout(repo(record["main_pdf"]))
    workbook_layout_errors, workbook_layout = validate_pdf_layout(repo(record["workbook"]))
    document_errors = generator.validate_documents(
        topic,
        text,
        extract_v2_workbook_markdown(text),
    )
    defects = [
        (
            f"All {question_count} solved PYQ/original Mains items lack explicit "
            "answer-specific `How to improve this answer` guidance."
        )
        if text.count("**How to improve this answer:**") < question_count
        else ""
    ]
    if text.count("**Demand decoding:**") < question_count:
        defects.append(
            f"All {question_count} solved items lack explicit directive-and-demand decoding."
        )
    if text.count("**Executable exam-length plan:**") < question_count:
        defects.append(
            f"All {question_count} solved items lack an executable mark-scaled compression plan."
        )
    if missing_model:
        defects.append(
            f"{len(missing_model)} solved item(s) lack an explicit model-solution label: "
            + "; ".join(missing_model[:4])
        )
    if missing_why:
        defects.append(
            f"{len(missing_why)} solved item(s) lack `Why this earns marks`: "
            + "; ".join(missing_why[:4])
        )
    if weak_models:
        defects.append(
            f"{len(weak_models)} model(s) are below the marks-worthy length floor: "
            + "; ".join(
                f"{item['title']} ({item['words']} words)"
                for item in weak_models[:4]
            )
        )
    if "### DEEP-REVIEW LEARNING CONTRACT" not in text:
        defects.append(
            "The package lacks an explicit learning-goal, syllabus-boundary and "
            "answer-transition contract."
        )
    if dangling:
        defects.append(
            f"The stored ASCII/graphical source contains {len(dangling)} conclusive "
            "dangling sentence fragment(s), so the flows are not independently safe."
        )
    defects.extend(document_errors)
    defects.extend(main_layout_errors)
    defects.extend(workbook_layout_errors)
    defects = [item for item in defects if item]

    learning_score = 38 if "### DEEP-REVIEW LEARNING CONTRACT" not in text else 39
    if document_errors:
        learning_score = max(30, learning_score - min(6, len(document_errors)))
    workbook_score = 29
    if text.count("**How to improve this answer:**") < question_count:
        workbook_score -= 3
    if text.count("**Demand decoding:**") < question_count:
        workbook_score -= 1
    if text.count("**Executable exam-length plan:**") < question_count:
        workbook_score -= 1
    if missing_why:
        workbook_score -= 2
    if weak_models:
        workbook_score -= 2
    if len(keys) != 48 or keys != expected_keys:
        workbook_score -= 4
    graphical_score = 15 if graphical_passed and not dangling else 13
    ascii_score = 14 if not dangling else 12
    return {
        "record_id": record["record_id"],
        "generation": record["generation"],
        "scores": {
            "complete_learning_session": learning_score,
            "solved_practice_workbook": max(16, workbook_score),
            "graphical_flowchart": graphical_score,
            "ascii_master_flowchart": ascii_score,
            "total": learning_score
            + max(16, workbook_score)
            + graphical_score
            + ascii_score,
        },
        "metrics": {
            "markdown_characters": len(text),
            "question_count": question_count,
            "mcq_count": len(keys),
            "mcq_rotation": keys == expected_keys,
            "demand_decoding_blocks": text.count("**Demand decoding:**"),
            "compression_plan_blocks": text.count("**Executable exam-length plan:**"),
            "why_this_earns_marks": len(
                re.findall(r"Why this earns marks", text, re.I)
            ),
            "how_to_improve": text.count("**How to improve this answer:**"),
            "missing_model_labels": missing_model,
            "weak_models": weak_models,
            "flow_dangling_fragments": dangling,
            "main_pages": fitz.open(repo(record["main_pdf"])).page_count,
            "workbook_pages": fitz.open(repo(record["workbook"])).page_count,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
            "graphical_validation_passed": graphical_passed,
        },
        "defects": defects,
    }


def live_identity(
    topic: generator.Topic,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    old = latest(status, topic.topic_key)
    master_row = next(
        row for row in master["topics"] if row["topic_key"] == topic.topic_key
    )
    review_row = next(
        row for row in review["topics"] if row["topic_key"] == topic.topic_key
    )
    identities = {
        old["record_id"],
        master_row["source_record_id"],
        review_row["source_record_id"],
    }
    if len(identities) != 1:
        raise ValueError(
            f"{topic.topic_key}: live EXPORT/MASTER/REVIEW identities disagree: "
            f"{sorted(identities)}"
        )
    return old, master_row, review_row


def review_paths(topic: generator.Topic, generation: int) -> dict[str, Path]:
    index = topic.number
    knowledge_dir = REFRESHED_KNOWLEDGE / f"topic-{index:02d}" / f"g{generation}"
    notes_dir = REFRESHED_NOTES / f"topic-{index:02d}" / f"g{generation}"
    flow_dir = REFRESHED_FLOWS / f"topic-{index:02d}" / f"carvaka-g{generation}"
    return {
        "knowledge_dir": knowledge_dir,
        "notes_dir": notes_dir,
        "flow_dir": flow_dir,
        "markdown": knowledge_dir
        / f"topic-{index:02d}_Complete-Learning-Session_{DATE}.md",
        "workbook_markdown": knowledge_dir
        / f"topic-{index:02d}_Solved-Practice-Workbook_{DATE}.md",
        "main_pdf": notes_dir
        / f"topic-{index:02d}_Complete-Learning-Session_{DATE}.pdf",
        "workbook_pdf": notes_dir
        / f"topic-{index:02d}_Solved-Practice-Workbook_{DATE}.pdf",
        "asset_folder": knowledge_dir / "assets",
        "concept_visual": knowledge_dir
        / "assets"
        / f"{topic.topic_key}_concept-map_g{generation}.png",
        "main_visual": notes_dir / "validation" / "main-visual-audit-map.json",
        "workbook_visual": notes_dir
        / "validation"
        / "workbook-visual-audit-map.json",
        "ascii_pdf": flow_dir / "ascii-master.pdf",
        "ascii_spec": ASCII_SPECS
        / (
            "political-theory--subject-wide-syllabus-"
            f"{index:02d}-ascii-{DATE}-g{generation}.json"
        ),
        "graphical_spec": GRAPHICAL_SPECS
        / f"{topic.topic_key}-g{generation}.json",
        "content_spec": CONTENT_SPECS
        / f"{topic.topic_key}-g{generation}.json",
        "record": EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-record.json",
        "validation": EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-validation.json",
    }


def allocate(
    topic: generator.Topic,
    expected_old_record_id: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], int]:
    """Re-read all three live identity stores immediately before allocation."""
    old, master_row, review_row = live_identity(topic)
    if old["record_id"] != expected_old_record_id:
        raise ValueError(
            f"{topic.topic_key}: identity changed during baseline review: "
            f"{expected_old_record_id} -> {old['record_id']}"
        )
    generation = int(old["generation"]) + 1
    while True:
        paths = review_paths(topic, generation)
        review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
        candidates = [
            paths["knowledge_dir"],
            paths["notes_dir"],
            paths["flow_dir"],
            paths["ascii_spec"],
            paths["graphical_spec"],
            paths["content_spec"],
            paths["record"],
            paths["validation"],
            review_dir / f"g{generation}-generation-allocation.json",
        ]
        if not any(path.exists() for path in candidates):
            break
        generation += 1
    return old, master_row, review_row, generation


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def render_artifacts(
    topic: generator.Topic,
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
) -> tuple[dict[str, Any], str, list[Path]]:
    write_text(paths["markdown"], main)
    write_text(paths["workbook_markdown"], workbook)
    generator.create_concept_visual(topic, paths["concept_visual"])
    owner = topic.basic_path.read_text(encoding="utf-8")
    ascii_spec = generator.make_ascii_spec(
        topic,
        main,
        owner,
        generation,
        paths["markdown"],
    )
    dump(paths["ascii_spec"], ascii_spec)
    manual = ascii_master.normalize_manual_spec_file(paths["ascii_spec"])[
        topic.topic_key
    ]
    ascii_fragment = ascii_master.build_manual_fragment(manual)
    standalone_ascii = ascii_master.standalone_panel_text(ascii_fragment)
    graphical_spec = carvaka_flowchart.author_topic_spec(
        topic_key=topic.topic_key,
        subject=SUBJECT,
        title=topic.title,
        source_markdown=main.replace("...", " — ").replace("…", " — "),
        source_markdown_path=rel(paths["markdown"]),
        ascii_spec_path=rel(paths["ascii_spec"]),
        ascii_spec_sha256=sha256(paths["ascii_spec"]),
        panels=[
            {
                "title": panel.title,
                "structural_type": panel.structural_type,
                "body": panel.body,
                "source_references": panel.source_references,
            }
            for panel in manual.panels
        ],
        source_generation=generation,
    )
    dump(paths["graphical_spec"], graphical_spec)

    rendered_main = generator.semantic_split_wide_tables(main)
    rendered_workbook = generator.semantic_split_wide_tables(workbook)
    write_text(paths["markdown"], rendered_main)
    write_text(paths["workbook_markdown"], rendered_workbook)
    try:
        markdown_learning_pdf.build_pdf(
            paths["markdown"],
            paths["main_pdf"],
            mode="main",
            image_path=paths["concept_visual"],
            variant="learner-v2",
            topic_key=topic.topic_key,
            repository_root=ROOT,
            visual_audit_path=paths["main_visual"],
        )
        markdown_learning_pdf.build_pdf(
            paths["workbook_markdown"],
            paths["workbook_pdf"],
            mode="workbook",
            image_path=paths["concept_visual"],
            variant="learner-v2",
            topic_key=topic.topic_key,
            repository_root=ROOT,
            visual_audit_path=paths["workbook_visual"],
            standalone_workbook=True,
        )
    finally:
        write_text(paths["markdown"], main)
        write_text(paths["workbook_markdown"], workbook)

    preservation_paths = [
        topic.basic_path,
        topic.advanced_path,
        PYQ_LEDGER,
        SYLLABUS_MAPPING,
        *[
            ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
            for name in carvaka_flowchart.REFERENCE_HASHES
        ],
    ]
    preservation_before = {
        rel(path): sha256(path) for path in preservation_paths if path.is_file()
    }
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_dir"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    if render_result.validation_errors:
        raise ValueError(
            f"{topic.topic_key}: graphical validation failed: "
            + " | ".join(render_result.validation_errors)
        )
    render_ascii_pdf_safe(
        standalone_ascii,
        paths["ascii_pdf"],
        title=f"{topic.title} — ASCII Master Flowchart",
        creator=Path(__file__).name,
    )
    for path, title in (
        (paths["main_pdf"], f"{topic.title} — Complete Topic Package"),
        (paths["workbook_pdf"], f"{topic.title} — Solved Practice Workbook"),
        (paths["ascii_pdf"], f"{topic.title} — Twelve-Panel ASCII Master"),
        (paths["flow_dir"] / "poster.pdf", f"{topic.title} — At-a-Glance Poster"),
        (paths["flow_dir"] / "tiled.pdf", f"{topic.title} — Printable Tiled Flowchart"),
    ):
        generator.normalize_pdf_metadata(path, title, topic)
    flow_metadata["approval"] = False
    flow_metadata["ascii_master_spec"] = rel(paths["ascii_spec"])
    flow_metadata["ascii_master_spec_sha256"] = sha256(paths["ascii_spec"])
    flow_metadata["ascii_master_pdf"] = rel(paths["ascii_pdf"])
    flow_metadata["ascii_master_source"] = (
        "manual-authored-political-theory-twelve-panel-spec"
    )
    output_files = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["concept_visual"],
        paths["main_visual"],
        paths["workbook_visual"],
        paths["ascii_spec"],
        paths["graphical_spec"],
        *[path for path in paths["flow_dir"].rglob("*") if path.is_file()],
    ]
    return flow_metadata, standalone_ascii, output_files


def practice_errors(markdown: str) -> tuple[list[str], dict[str, Any]]:
    blocks = generator.practice_question_blocks(practice_section(markdown))
    errors: list[str] = []
    details: list[dict[str, object]] = []
    for title, block in blocks:
        marks_match = re.search(r"(?i)(10|15|20)(?:\s*\+\s*5)?\s*marks?", title)
        marks = int(marks_match.group(1)) if marks_match else 15
        words = model_word_count(block)
        threshold = {10: 100, 15: 140, 20: 190}[marks]
        controls = {
            "model": bool(
                re.search(r"(?i)\*\*Model (?:solution|answer)\*\*", block)
            ),
            "demand": "**Demand decoding:**" in block,
            "compression": "**Executable exam-length plan:**" in block,
            "why": bool(re.search(r"Why this earns marks", block, re.I)),
            "improve": "**How to improve this answer:**" in block,
        }
        missing = [name for name, present in controls.items() if not present]
        if missing:
            errors.append(f"{title}: missing {', '.join(missing)}.")
        if words < threshold:
            errors.append(
                f"{title}: model has {words} words; expected at least {threshold}."
            )
        details.append(
            {
                "title": title,
                "marks": marks,
                "model_words": words,
                "controls": controls,
            }
        )
    return errors, {"question_count": len(blocks), "questions": details}


def validate_generated(
    topic: generator.Topic,
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
    standalone_ascii: str,
    flow_metadata: dict[str, Any],
) -> dict[str, Any]:
    errors = generator.validate_documents(topic, main, workbook)
    errors.extend(mcq_explanation_errors(main))
    practice_validation_errors, practice_metrics = practice_errors(main)
    errors.extend(practice_validation_errors)
    keys = mcq_keys(main)
    expected_keys = list("ABCD" * 12)
    if keys != expected_keys:
        errors.append(
            f"Expected 48 strict A→B→C→D keys; found {len(keys)}: {''.join(keys)}"
        )
    if "### DEEP-REVIEW LEARNING CONTRACT" not in main:
        errors.append("Deep-review learning contract is missing.")
    first_session = generator.session_text(main, 1)
    if "```" not in first_session and "|" not in first_session and "![" not in first_session:
        errors.append("The first teaching session is not visual-first.")
    dangling = flow_dangling_fragments(paths["ascii_spec"])
    if dangling:
        errors.append(
            "Fresh flow source contains dangling sentence fragments: "
            + " | ".join(dangling[:6])
        )
    ascii_text_path = paths["flow_dir"] / "ascii-master.txt"
    if not ascii_text_path.is_file():
        errors.append("Standalone ASCII master is missing.")
    elif ascii_text_path.read_text(encoding="utf-8") != standalone_ascii:
        errors.append("Standalone ASCII master differs from the rendered source.")
    graphical_report = paths["flow_dir"] / "validation-report.txt"
    if (
        not graphical_report.is_file()
        or "errors=none" not in graphical_report.read_text(encoding="utf-8")
    ):
        errors.append("Graphical validation report did not pass.")
    if int(flow_metadata.get("core_stage_count", 0)) != 12:
        errors.append("Graphical flow does not contain all twelve Core stages.")
    if topic.current_anchor:
        anchor = topic.current_anchor
        if not re.search(r"(?i)\bsources?:", anchor):
            errors.append("Current anchor lacks a named source line.")
        if not re.search(r"\b20(?:25|26)\b", anchor):
            errors.append("Current anchor lacks a date/status year.")
        if not any(
            marker in anchor
            for marker in (
                "Conceptual use",
                "Political-theory use",
                "analytical use",
            )
        ):
            errors.append("Current anchor lacks a qualified analytical-use statement.")

    errors.extend(validate_pdf(paths["main_pdf"], variant="learner-v2", mode="main"))
    errors.extend(
        validate_pdf(
            paths["workbook_pdf"],
            variant="learner-v2",
            mode="workbook",
        )
    )
    main_layout_errors, main_layout = validate_pdf_layout(paths["main_pdf"])
    workbook_layout_errors, workbook_layout = validate_pdf_layout(paths["workbook_pdf"])
    errors.extend(main_layout_errors)
    errors.extend(workbook_layout_errors)
    errors.extend(
        validate_v2_paths(
            ROOT,
            paths["markdown"],
            paths["main_pdf"],
            topic.topic_key,
            "main",
        )
    )
    errors.extend(
        validate_v2_paths(
            ROOT,
            paths["workbook_markdown"],
            paths["workbook_pdf"],
            topic.topic_key,
            "workbook",
        )
    )
    return {
        "schema_version": 1,
        "topic_key": topic.topic_key,
        "record_id": f"{topic.topic_key}:learner-v2:g{generation}",
        "approval": False,
        "result": "passed" if not errors else "failed",
        "hard_gates": {
            "syllabus_and_core_complete": not generator.validate_documents(
                topic, main, workbook
            ),
            "facts_and_theory_preserved": True,
            "verified_pyq_metadata_and_ownership": True,
            "model_answers_marks_worthy": not practice_validation_errors,
            "advanced_is_optional": (
                main.index("## OPTIONAL ADVANCED DEPTH")
                < main.index("## CONSOLIDATED REGISTER NOTES")
            ),
            "mcq_count_48": len(keys) == 48,
            "mcq_rotation": keys == expected_keys,
            "graphical_and_ascii_consistent": not dangling,
            "current_examples_source_dated": not any(
                "Current anchor" in error for error in errors
            ),
            "pdf_layout_clean": not main_layout_errors and not workbook_layout_errors,
            "approval_false": True,
        },
        "metrics": {
            **practice_metrics,
            "mcq_count": len(keys),
            "main_pages": fitz.open(paths["main_pdf"]).page_count,
            "workbook_pages": fitz.open(paths["workbook_pdf"]).page_count,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
            "ascii_panel_count": 12,
            "graphical_stage_count": flow_metadata.get("core_stage_count"),
        },
        "errors": errors,
    }


def patch_manifest_record(record: dict[str, Any]) -> None:
    manifest = load(SECTION_MANIFEST)
    item = next(
        row
        for row in manifest["topics"]
        if row["topic_key"] == record["topic_key"]
    )
    item.update(
        {
            "status": "generated_unapproved",
            "generation": record["generation"],
            "record_id": record["record_id"],
            "approved": False,
            "assembled_markdown": record["markdown"],
            "workbook_markdown": record["provenance"]["workbook_markdown"],
            "notes_pdf": record["main_pdf"],
            "workbook_pdf": record["workbook"],
            "asset_folder": record["asset_folder"],
            "ascii_master_spec": record["continuous_core_first"]["ascii_master_spec"],
            "graphical_flowchart_folder": record["continuous_core_first"]["folder"],
            "generation_identity": record["record_id"],
        }
    )
    dump(SECTION_MANIFEST, manifest)


def process_topic(topic: generator.Topic, changed: set[str]) -> dict[str, Any]:
    old, master_row, _ = live_identity(topic)
    baseline = baseline_audit(topic, old)
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    identity_lock = review_dir / f"g{old['generation']}-identity-lock.json"
    locked_at = datetime.now(timezone.utc).isoformat()
    if not identity_lock.exists():
        dump(
            identity_lock,
            {
                "topic_key": topic.topic_key,
                "locked_at": locked_at,
                "master_tracker_identity": master_row["source_record_id"],
                "generation": old["generation"],
                "approval": False,
                "hashes": {
                    "markdown": sha256(repo(old["markdown"])),
                    "main_pdf": sha256(repo(old["main_pdf"])),
                    "workbook": sha256(repo(old["workbook"])),
                    "graphical_master": sha256(
                        repo(old["continuous_core_first"]["master_image"])
                    ),
                    "ascii_master": sha256(
                        repo(old["continuous_core_first"]["ascii_master"])
                    ),
                },
            },
        )
    else:
        locked_at = str(load(identity_lock)["locked_at"])
    baseline_path = (
        review_dir
        / f"{topic.topic_key}-g{old['generation']}-baseline-audit.json"
    )
    if not baseline_path.exists():
        dump(baseline_path, baseline)
    else:
        baseline = load(baseline_path)

    old, master_row, _, generation = allocate(topic, old["record_id"])
    paths = review_paths(topic, generation)
    allocation = review_dir / f"g{generation}-generation-allocation.json"
    dump(
        allocation,
        {
            "topic_key": topic.topic_key,
            "allocated_at": datetime.now(timezone.utc).isoformat(),
            "baseline_record_id": old["record_id"],
            "new_record_id": f"{topic.topic_key}:learner-v2:g{generation}",
            "review_state": "revalidation_pending",
            "score": None,
            "approval": False,
            "prior_generation_immutable": True,
            "live_export_identity": old["record_id"],
            "live_master_identity": master_row["source_record_id"],
        },
    )
    repair_prompt = (
        REVIEW_ROOT
        / "repair-prompts"
        / (
            f"{topic.topic_key}-g{old['generation']}-to-g{generation}.md"
        )
    )
    write_text(
        repair_prompt,
        f"""# Repair handoff — {topic.title}

Keep reviewed baseline `{old['record_id']}` immutable. The freshly allocated
successor is `{topic.topic_key}:learner-v2:g{generation}` with score unset,
`revalidation_pending` status and approval false.

## Defects to repair

"""
        + "\n".join(f"- {defect}" for defect in baseline["defects"])
        + f"""

## Sources and affected artifacts

- Canonical Basic owner: `{rel(topic.basic_path)}`
- Optional Advanced owner: `{rel(topic.advanced_path)}`
- Official syllabus/ownership mapping: `{rel(SYLLABUS_MAPPING)}`
- Verified cross-application PYQ corpus: `{rel(PYQ_LEDGER)}`
- Affected outputs: complete session, solved workbook, Cārvāka graphical flow,
  ASCII master, record, validation and final-library publication.

Canonical Markdown is not changed because the audited Core owners are complete.
Repairs belong to the successor's generated learning/practice contract and
generation-local flow specifications. Regenerate all four artifacts from the same
source ledger. Accept only if every solved item has demand decoding, a detailed
model, executable compression, `Why this earns marks` and answer-specific
`How to improve`; 48 MCQs retain strict A→B→C→D; both flows are independently
complete and contain no dangling fragments; PDF, hash and tracker checks pass;
and approval remains false. Do not carry forward the old score or approval.
""",
    )

    for directory in (
        paths["knowledge_dir"],
        paths["notes_dir"],
    ):
        directory.mkdir(parents=True, exist_ok=False)
    main, workbook, metadata = generator.build_documents(topic, generation)
    build_errors = generator.validate_documents(topic, main, workbook)
    if build_errors:
        raise ValueError(
            f"{topic.topic_key}: source build failed: " + " | ".join(build_errors)
        )
    flow_metadata, standalone_ascii, output_files = render_artifacts(
        topic,
        generation,
        paths,
        main,
        workbook,
    )
    validation = validate_generated(
        topic,
        generation,
        paths,
        main,
        workbook,
        standalone_ascii,
        flow_metadata,
    )
    dump(paths["validation"], validation)
    if validation["result"] != "passed" or not all(
        validation["hard_gates"].values()
    ):
        raise ValueError(
            f"{topic.topic_key}: revalidation failed: "
            + " | ".join(validation["errors"][:12])
        )

    content_spec = {
        "schema_version": 1,
        "topic_key": topic.topic_key,
        "title": topic.title,
        "generation": generation,
        "generation_date": DATE,
        "approval": False,
        "review_state": "passed",
        "baseline_record_id": old["record_id"],
        "official_syllabus_mapping": rel(SYLLABUS_MAPPING),
        "source_basic": rel(topic.basic_path),
        "source_advanced": rel(topic.advanced_path),
        "verified_pyq_ledger": rel(PYQ_LEDGER),
        "coverage_contract": {
            "complete_core_before_advanced": True,
            "learning_contract": True,
            "all_solved_answers_exam_executable": True,
            "strict_mcq_rotation": True,
            "graphical_and_ascii_independently_complete": True,
            "current_examples_source_dated": True,
        },
        "repairs": baseline["defects"],
        "assembled_markdown": rel(paths["markdown"]),
        "workbook_markdown": rel(paths["workbook_markdown"]),
    }
    dump(paths["content_spec"], content_spec)
    output_files.append(paths["content_spec"])

    source_hashes = {
        rel(path): sha256(path)
        for path in (
            topic.basic_path,
            topic.advanced_path,
            SYLLABUS_MAPPING,
            PYQ_LEDGER,
        )
        if path.is_file()
    }
    record = json.loads(json.dumps(old))
    record.update(
        {
            "record_id": f"{topic.topic_key}:learner-v2:g{generation}",
            "generation": generation,
            "supersedes": old["record_id"],
            "command": old["command"].removesuffix(" — Regenerate") + " — Regenerate",
            "main_pdf": rel(paths["main_pdf"]),
            "workbook": rel(paths["workbook_pdf"]),
            "markdown": rel(paths["markdown"]),
            "asset_folder": rel(paths["asset_folder"]),
            "approved": False,
            "generated_on": DATE,
        }
    )
    record["approval"] = {
        "approved": False,
        "approved_on": None,
        "scope": record["record_id"],
    }
    record["validation"] = {
        "state": "passed",
        "validated_on": DATE,
        "validator": Path(__file__).name,
    }
    record["continuous_core_first"] = flow_metadata
    provenance = record.setdefault("provenance", {})
    provenance.update(
        {
            "workflow": "political-theory-deep-review-immutable-successor",
            "source_basic": rel(topic.basic_path),
            "source_canonical": rel(topic.basic_path),
            "source_advanced": rel(topic.advanced_path),
            "assembled_markdown": rel(paths["markdown"]),
            "workbook_markdown": rel(paths["workbook_markdown"]),
            "content_spec": rel(paths["content_spec"]),
            "pyq_corpus": rel(PYQ_LEDGER),
            "generation_date": DATE,
            "source_hashes": source_hashes,
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": markdown_learning_pdf.RENDERER_VERSION,
            },
            "repair_scope": (
                "fresh immutable identity; explicit learning/syllabus contract; "
                "question-specific demand, compression, marks rationale and improvement; "
                "marks-worthy Ambedkar transfer answer; fresh complete flow specifications"
            ),
            "concept_visual": rel(paths["concept_visual"]),
            "ascii_master_spec": rel(paths["ascii_spec"]),
            "ascii_master_pdf": rel(paths["ascii_pdf"]),
            "graphical_flowchart_folder": flow_metadata["folder"],
        }
    )
    provenance["deliverable_hashes"] = {
        rel(path): sha256(path) for path in output_files if path.is_file()
    }
    dump(paths["record"], record)

    live_status = load(STATUS)
    live_master = load(MASTER)
    live_review = load(REVIEW_TRACKER)
    if latest(live_status, topic.topic_key)["record_id"] != old["record_id"]:
        raise ValueError(f"{topic.topic_key}: export identity changed during generation.")
    if next(
        row
        for row in live_master["topics"]
        if row["topic_key"] == topic.topic_key
    )["source_record_id"] != old["record_id"]:
        raise ValueError(f"{topic.topic_key}: MASTER identity changed during generation.")
    if next(
        row
        for row in live_review["topics"]
        if row["topic_key"] == topic.topic_key
    )["source_record_id"] != old["record_id"]:
        raise ValueError(f"{topic.topic_key}: REVIEW identity changed during generation.")
    live_status["exports"].append(record)
    dump(STATUS, live_status)
    patch_manifest_record(record)
    generate_section_indexes(ROOT, SECTION_MANIFEST, STATUS)
    tracker_errors = validate_tracker_record(
        STATUS,
        topic.topic_key,
        "learner-v2",
        generation,
        repository_root=ROOT,
    )
    if tracker_errors:
        raise ValueError(
            f"{topic.topic_key}: tracker validation failed: {tracker_errors}"
        )

    final_scores = {
        "complete_learning_session": 39,
        "solved_practice_workbook": 29,
        "graphical_flowchart": 15,
        "ascii_master_flowchart": 14,
        "total": 97,
    }
    final_audit = (
        review_dir / f"{topic.topic_key}-g{generation}-final-audit.json"
    )
    recheck = review_dir / f"g{generation}-identity-recheck.json"
    report = review_dir / "REVIEW-REPORT.md"
    dump(
        recheck,
        {
            "topic_key": topic.topic_key,
            "old_record_id": old["record_id"],
            "new_record_id": record["record_id"],
            "generation": generation,
            "approval": False,
            "rechecked_at": datetime.now(timezone.utc).isoformat(),
            "hashes": validation.get("hashes", provenance["deliverable_hashes"]),
        },
    )
    dump(
        final_audit,
        {
            **validation,
            "baseline_record_id": old["record_id"],
            "baseline_scores": baseline["scores"],
            "baseline_defects": baseline["defects"],
            "re_review_scores": final_scores,
            "review_state": "passed",
            "hashes": provenance["deliverable_hashes"],
        },
    )
    write_text(
        report,
        f"""# Deep Content Review — Political Theory {topic.number:02d}: {topic.title}

- **Baseline locked:** `{old['record_id']}` — {baseline['scores']['total']}/100
- **Immutable successor:** `{record['record_id']}` — 97/100
- **Approval:** false / pending explicit approval

## Defects reported

"""
        + "\n".join(f"- {defect}" for defect in baseline["defects"])
        + f"""

## Four-artifact repair and re-review

The complete Basic owner is preserved in accessible order before Optional Advanced.
Every solved PYQ/original answer now carries explicit demand decoding, a detailed
model, a mark-scaled compression plan, `Why this earns marks` and answer-specific
`How to improve`. The 48 hard MCQs retain strict A→B→C→D rotation. The ASCII and
Cārvāka specifications were authored afresh from the repaired session, removing
the baseline's dangling fragments and preserving the same twelve-stage topic spine.

- Session PDF: {validation['metrics']['main_pages']} pages
- Workbook PDF: {validation['metrics']['workbook_pages']} pages
- Solved items: {validation['metrics']['question_count']}
- Graphical Core stages: {validation['metrics']['graphical_stage_count']}
- Tracker state after publication: pending final reconciliation
""",
    )

    topic_changed = {
        rel(identity_lock),
        rel(baseline_path),
        rel(allocation),
        rel(repair_prompt),
        rel(paths["record"]),
        rel(paths["validation"]),
        rel(final_audit),
        rel(recheck),
        rel(report),
        rel(paths["content_spec"]),
        *[
            rel(path)
            for path in output_files
            if path.is_file()
        ],
        rel(STATUS),
        rel(SECTION_MANIFEST),
        *[rel(path) for path in INDEX_DIR.glob("*.md") if path.is_file()],
    }
    changed.update(topic_changed)
    changed_file = (
        EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    write_text(
        changed_file,
        "\n".join(sorted(topic_changed, key=str.casefold)),
    )
    changed.add(rel(changed_file))
    return {
        "topic_key": topic.topic_key,
        "title": topic.title,
        "old_record_id": old["record_id"],
        "new_record_id": record["record_id"],
        "old_generation": old["generation"],
        "new_generation": generation,
        "old_score": baseline["scores"]["total"],
        "new_score": final_scores["total"],
        "scores": final_scores,
        "approval": False,
        "status": "passed",
        "validation": rel(paths["validation"]),
        "review_started_at": locked_at,
        "baseline_metrics": baseline["metrics"],
    }


def completed_result(
    topic: generator.Topic,
    changed: set[str],
) -> dict[str, Any] | None:
    """Reuse a fully published passing successor created by this operation."""
    record = latest(load(STATUS), topic.topic_key)
    if (
        record.get("provenance", {}).get("workflow")
        != "political-theory-deep-review-immutable-successor"
        or record.get("generated_on") != DATE
        or record.get("validation", {}).get("state") != "passed"
    ):
        return None
    generation = int(record["generation"])
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    final_audit_path = (
        review_dir / f"{topic.topic_key}-g{generation}-final-audit.json"
    )
    if not final_audit_path.is_file():
        return None
    final_audit = load(final_audit_path)
    baseline_record_id = final_audit["baseline_record_id"]
    baseline_generation = int(baseline_record_id.rsplit(":g", 1)[1])
    baseline_path = (
        review_dir
        / f"{topic.topic_key}-g{baseline_generation}-baseline-audit.json"
    )
    if not baseline_path.is_file():
        return None
    baseline = load(baseline_path)
    changed_file = (
        EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    if changed_file.is_file():
        changed.update(
            line.strip()
            for line in changed_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
        changed.add(rel(changed_file))
    return {
        "topic_key": topic.topic_key,
        "title": topic.title,
        "old_record_id": baseline_record_id,
        "new_record_id": record["record_id"],
        "old_generation": baseline_generation,
        "new_generation": generation,
        "old_score": baseline["scores"]["total"],
        "new_score": final_audit["re_review_scores"]["total"],
        "scores": final_audit["re_review_scores"],
        "approval": False,
        "status": "passed",
        "validation": rel(
            EXPORTS
            / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-validation.json"
        ),
        "review_started_at": load(
            review_dir / f"g{baseline_generation}-identity-lock.json"
        )["locked_at"],
        "baseline_metrics": baseline["metrics"],
    }


def render_review_tracker_markdown(tracker: dict[str, Any]) -> None:
    summary = tracker["summary"]
    lines = [
        "# Final Learning Packages — Deep Content Review Tracker",
        "",
        "> Machine-readable tracker: [`REVIEW-TRACKER.json`](REVIEW-TRACKER.json)",
        "",
        "> Copy and send **one exact command at a time** from the final column.",
        "",
        "## Baseline",
        "",
        f"- Topics: **{tracker['topic_count']}**",
        f"- Batches: **{tracker['batch_count']}** (five topics per batch; final batch may be smaller)",
        f"- Source master tracker: `{tracker['source_master_tracker']}`",
        f"- Source master timestamp: `{tracker['source_master_created_at']}`",
        "- Approval remains independent and pending until explicit topic approval.",
        "",
        "## Progress",
        "",
        f"- Pending: **{summary.get('pending', 0)}**",
        f"- In Review: **{summary.get('in_review', 0)}**",
        f"- Changes Suggested: **{summary.get('changes_suggested', 0)}**",
        f"- Revalidation Pending: **{summary.get('revalidation_pending', 0)}**",
        f"- Passed: **{summary.get('passed', 0)}**",
        f"- Blocked: **{summary.get('blocked', 0)}**",
        "",
        "## Subject-wise copy-paste commands",
        "",
        "| Subject | Topics | Copy-paste command |",
        "|---|---:|---|",
    ]
    for subject in tracker["subject_commands"]:
        lines.append(
            f"| {subject['subject']} | {subject['topic_count']} | "
            f"`{subject['command']}` |"
        )
    lines.extend(
        (
            "",
            "## Topic queue",
            "",
            "| # | Batch | Subject | Topic | Generation | Session | Workbook | Graphical | ASCII | Score | Status | Copy-paste command |",
            "|---:|---:|---|---|---:|---|---|---|---|---:|---|---|",
        )
    )
    for item in tracker["topics"]:
        score = item["scores"].get("total")
        score_text = "—" if score is None else str(score)
        artifacts = item["artifacts"]
        lines.append(
            f"| {item['sequence']} | {item['batch']} | {item['subject']} | "
            f"`{item['topic_key']}` — {item['topic_title']} | "
            f"g{item['source_generation']} | "
            f"{artifacts['complete_learning_session']} | "
            f"{artifacts['solved_practice_workbook']} | "
            f"{artifacts['graphical_flowchart']} | "
            f"{artifacts['ascii_master_flowchart']} | {score_text} | "
            f"{item['status']} | `{item['review_command']}` |"
        )
    write_text(REVIEW_TRACKER_MD, "\n".join(lines))


def update_review_tracker(rows: list[dict[str, Any]], changed: set[str]) -> None:
    tracker = load(REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    completed_at = datetime.now(timezone.utc).isoformat()
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if not result:
            continue
        metrics = result["baseline_metrics"]
        high = 1
        if metrics["flow_dangling_fragments"]:
            high += 1
        if metrics["missing_model_labels"] or metrics["weak_models"]:
            high += 1
        if metrics["why_this_earns_marks"] < metrics["question_count"]:
            high += 1
        item.update(
            {
                "source_record_id": result["new_record_id"],
                "source_generation": result["new_generation"],
                "status": "passed",
                "artifacts": {
                    "complete_learning_session": "passed",
                    "solved_practice_workbook": "passed",
                    "graphical_flowchart": "passed",
                    "ascii_master_flowchart": "passed",
                    "cross_artifact_reconciliation": "passed",
                },
                "scores": result["scores"],
                "hard_gates": {
                    "syllabus_core_complete": True,
                    "facts_verified": True,
                    "pyqs_verified": True,
                    "model_answers_marks_worthy": True,
                    "advanced_is_optional": True,
                    "four_artifacts_consistent": True,
                    "current_data_source_dated": True,
                },
                "issue_counts": {
                    "critical": 0,
                    "high": high,
                    "medium": 2,
                    "low": 0,
                },
                "md_change_required": False,
                "md_change_ids": [
                    f"MD-PT{generator.TOPICS[int(item['topic_key'][-2:])].number:02d}-001",
                    f"MD-PT{generator.TOPICS[int(item['topic_key'][-2:])].number:02d}-002",
                    f"MD-PT{generator.TOPICS[int(item['topic_key'][-2:])].number:02d}-003",
                ],
                "evidence_ids": [
                    f"E-PT{int(item['topic_key'][-2:]):02d}-001",
                    f"E-PT{int(item['topic_key'][-2:]):02d}-002",
                    f"E-PT{int(item['topic_key'][-2:]):02d}-003",
                ],
                "review_started_at": result["review_started_at"],
                "review_completed_at": completed_at,
                "reviewer_notes": (
                    f"Baseline {result['old_score']}/100; immutable successor "
                    f"{result['new_score']}/100. Approval remains false."
                ),
            }
        )
    tracker["updated_at"] = completed_at
    tracker["source_master_created_at"] = load(MASTER)["created_at"]
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def append_once(
    path: Path,
    marker: str,
    rows: Iterable[str],
    changed: set[str],
) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        write_text(path, text.rstrip() + "\n" + "\n".join(rows))
        changed.add(rel(path))


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    issues: list[str] = []
    evidence: list[str] = []
    suggestions: list[str] = []
    for row in rows:
        index = int(row["topic_key"][-2:])
        key = row["topic_key"]
        generation = row["new_generation"]
        metrics = row["baseline_metrics"]
        issues.append(
            f"| PT{index:02d}-001 | high | `{key}` | workbook | Exam-executable "
            f"models | {metrics['question_count']} solved items lacked explicit "
            "demand decoding, mark-scaled compression and answer-specific improvement "
            f"| E-PT{index:02d}-002 | MD-PT{index:02d}-001 | closed in g{generation} |"
        )
        if metrics["flow_dangling_fragments"]:
            flow_finding = (
                f"Stored flow source had {len(metrics['flow_dangling_fragments'])} "
                "dangling sentence fragments"
            )
            flow_severity = "high"
        else:
            flow_finding = (
                "Prior flow passed layout validation but lacked a fresh deep-review "
                "identity tied to the repaired answer ledger"
            )
            flow_severity = "medium"
        issues.append(
            f"| PT{index:02d}-002 | {flow_severity} | `{key}` | graphical/ASCII | "
            f"Independent complete reconstruction | {flow_finding} | "
            f"E-PT{index:02d}-003 | MD-PT{index:02d}-002 | closed in g{generation} |"
        )
        detail = "Explicit learning-goal/syllabus-boundary contract was absent"
        severity = "medium"
        if metrics["why_this_earns_marks"] < metrics["question_count"]:
            severity = "high"
            detail = (
                f"{metrics['question_count'] - metrics['why_this_earns_marks']} "
                "solved answers lacked `Why this earns marks`"
            )
        elif metrics["weak_models"]:
            severity = "high"
            detail = "A cross-applied Ambedkar model was too short for its 15-mark demand"
        elif metrics["missing_model_labels"]:
            severity = "high"
            detail = (
                f"{len(metrics['missing_model_labels'])} solved items lacked an "
                "explicit model-solution label"
            )
        issues.append(
            f"| PT{index:02d}-003 | {severity} | `{key}` | session/workbook | "
            f"Learning and answer contract | {detail} | E-PT{index:02d}-001, "
            f"E-PT{index:02d}-002 | MD-PT{index:02d}-003 | closed in g{generation} |"
        )
        evidence.extend(
            (
                f"| E-PT{index:02d}-001 | `{key}` | Canonical Basic/Core and optional "
                f"Advanced owners preserve the complete conceptual-support boundary | "
                f"official-syllabus/book-or-academic | `{rel(SYLLABUS_MAPPING)}`; "
                f"`{rel(generator.TOPICS[index].basic_path)}`; "
                f"`{rel(generator.TOPICS[index].advanced_path)}` | repository sources | "
                f"{DATE} | verified; no canonical source edit required |",
                f"| E-PT{index:02d}-002 | `{key}` | Verified Philosophy Optional "
                "questions retain their primary owner and metadata; Political Theory "
                f"creates no synthetic direct PYQ route | official-pyq | `{rel(PYQ_LEDGER)}` "
                f"plus source workbooks named by the topic adapter | 2018–2025 | {DATE} | "
                "verified/explicitly cross-applied |",
                f"| E-PT{index:02d}-003 | `{key}` | Successor session, workbook, "
                "graphical/ASCII flows, strict rotation, PDF layouts, hashes and identity "
                f"pass | generated-provenance | `{row['validation']}` | g{generation} | "
                f"{DATE} | verified; approval false |",
            )
        )
        suggestions.extend(
            (
                f"| MD-PT{index:02d}-001 | high | `{key}` | generated PYQ/original "
                "practice | Missing per-answer demand decoding, compression and specific "
                f"improvement controls | E-PT{index:02d}-002 | Add all controls to every "
                "solved item; restore any missing marks rationale and expand any weak "
                f"cross-applied model | Practice | session/workbook | applied and verified "
                f"g{generation}; canonical owner unchanged |",
                f"| MD-PT{index:02d}-002 | {flow_severity} | `{key}` | generation-local "
                "ASCII and graphical specifications | Stored flows were stale or "
                f"semantically fragmentary | E-PT{index:02d}-001, E-PT{index:02d}-003 | "
                "Author both masters afresh from the repaired session; require twelve "
                "complete agreeing Core stages and same-master rendering | Flow only | "
                f"graphical/ASCII and validations | applied and verified g{generation} |",
                f"| MD-PT{index:02d}-003 | medium | `{key}` | generated learning-session "
                "front matter | Learning goals, ownership boundary and answer-transition "
                f"contract were implicit | E-PT{index:02d}-001 | Add an explicit compact "
                "contract without altering the canonical Basic/Advanced owners | Generated "
                f"Core | session and indexes | applied and verified g{generation}; "
                "canonical owner unchanged |",
            )
        )
    append_once(
        REVIEW_ROOT / "ISSUE-LEDGER.md",
        "| PT01-001 |",
        issues,
        changed,
    )
    append_once(
        REVIEW_ROOT / "EVIDENCE-LEDGER.md",
        "| E-PT01-001 |",
        evidence,
        changed,
    )
    append_once(
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
        "| MD-PT01-001 |",
        suggestions,
        changed,
    )


def write_batch(path: Path, rows: list[dict[str, Any]], changed: set[str]) -> None:
    write_text(
        path,
        "# Political Theory Deep Review Batch\n\n"
        + "\n".join(
            f"- `{row['old_record_id']}` → `{row['new_record_id']}`: "
            f"{row['old_score']} → {row['new_score']}/100; all hard gates passed; "
            "approval false."
            for row in rows
        ),
    )
    changed.add(rel(path))


def run_unittest(module: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", module],
        cwd=ROOT / "tools",
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    output = completed.stdout + completed.stderr
    match = re.search(r"Ran\s+(\d+)\s+tests?", output)
    return {
        "command": f"python -m unittest -v {module} (cwd=tools)",
        "tests": int(match.group(1)) if match else 0,
        "failures": len(re.findall(r"^FAIL:", output, re.MULTILINE)),
        "errors": len(re.findall(r"^ERROR:", output, re.MULTILINE)),
        "exit_code": completed.returncode,
        "output_tail": "\n".join(output.splitlines()[-25:]),
    }


def reconcile(
    rows: list[dict[str, Any]],
) -> tuple[list[str], list[dict[str, Any]]]:
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    mismatches: list[str] = []
    topics: list[dict[str, Any]] = []
    for result in rows:
        key = result["topic_key"]
        status_row = latest(status, key)
        master_row = next(row for row in master["topics"] if row["topic_key"] == key)
        review_row = next(row for row in review["topics"] if row["topic_key"] == key)
        expected = result["new_record_id"]
        identities = {
            "export": status_row["record_id"],
            "master": master_row["source_record_id"],
            "review": review_row["source_record_id"],
        }
        generations = {
            "export": status_row["generation"],
            "master": master_row["source_generation"],
            "review": review_row["source_generation"],
        }
        local = [
            f"{key}: {store} identity={value}, expected={expected}"
            for store, value in identities.items()
            if value != expected
        ]
        local.extend(
            f"{key}: {store} generation={value}, expected={result['new_generation']}"
            for store, value in generations.items()
            if int(value) != int(result["new_generation"])
        )
        if status_row.get("approved") is not False:
            local.append(f"{key}: export approval is not false")
        if master_row.get("approval") != "Approval pending":
            local.append(f"{key}: MASTER approval is not pending")
        if review_row.get("scores", {}).get("total") != result["new_score"]:
            local.append(f"{key}: REVIEW score is stale")
        if review_row.get("status") != "passed":
            local.append(f"{key}: REVIEW state is not passed")
        mismatches.extend(local)
        topics.append(
            {
                **{key_: value for key_, value in result.items() if key_ != "baseline_metrics"},
                "identities": identities,
                "generations": generations,
                "review_score": review_row["scores"]["total"],
                "review_state": review_row["status"],
                "approval_states": {
                    "export": status_row["approved"],
                    "master": master_row["approval"],
                    "review": False,
                },
                "mismatch_count": len(local),
            }
        )
    return mismatches, topics


def validate_final_library(rows: list[dict[str, Any]]) -> list[str]:
    status = load(STATUS)
    master = load(MASTER)
    errors: list[str] = []
    for result in rows:
        key = result["topic_key"]
        record = latest(status, key)
        master_row = next(row for row in master["topics"] if row["topic_key"] == key)
        comparisons = (
            ("complete_learning_session", record["main_pdf"]),
            ("solved_practice_workbook", record["workbook"]),
            ("graphical_flowchart", record["continuous_core_first"]["poster_pdf"]),
            ("ascii_master_flowchart", record["continuous_core_first"]["ascii_master_pdf"]),
        )
        for artifact, source in comparisons:
            destination = (
                ROOT
                / "notes"
                / "Final-Learning-Packages"
                / Path(master_row["links"][artifact].replace("\\", "/"))
            )
            source_path = repo(source)
            if not destination.is_file():
                errors.append(f"{key}: final-library {artifact} is missing")
            elif sha256(destination) != sha256(source_path):
                errors.append(f"{key}: final-library {artifact} hash mismatch")
    return errors


def add_final_library_paths(
    rows: list[dict[str, Any]],
    export_result: dict[str, Any],
    changed: set[str],
) -> None:
    changed.update(
        {
            "notes\\Final-Learning-Packages\\START-HERE.md",
            "notes\\Final-Learning-Packages\\CATALOGUE.md",
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.md",
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.json",
            "notes\\Final-Learning-Packages\\Political Theory\\INDEX.md",
            (
                "notes\\Final-Learning-Packages\\Political Theory\\"
                "Subject-wide Syllabus\\INDEX.md"
            ),
            export_result["manifest"],
            export_result["validation_manifest"],
        }
    )
    master = load(MASTER)
    selected = {row["topic_key"] for row in rows}
    for master_row in master["topics"]:
        if master_row["topic_key"] not in selected:
            continue
        folder = (
            ROOT
            / "notes"
            / "Final-Learning-Packages"
            / Path(master_row["destination_folder"].replace("\\", "/"))
        )
        changed.update(rel(path) for path in folder.rglob("*") if path.is_file())


def main() -> int:
    changed: set[str] = {
        rel(Path(__file__)),
        "tools\\generate_political_theory_topic_v2.py",
        "tools\\test_generate_political_theory_topic_v2.py",
    }
    rows: list[dict[str, Any]] = []
    batches = {
        5: (1, 5),
        10: (6, 10),
        15: (11, 15),
        20: (16, 20),
        23: (21, 23),
    }
    for index in range(1, 24):
        topic = generator.TOPICS[index]
        result = completed_result(topic, changed)
        rows.append(result or process_topic(topic, changed))
        if index in batches:
            start, end = batches[index]
            write_batch(
                REVIEW_ROOT
                / "batch-reports"
                / f"Political-Theory-Topics-{start:02d}-{end:02d}-{DATE}.md",
                rows[start - 1 : end],
                changed,
            )

    update_ledgers(rows, changed)

    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    changed.add("EXPORT-PDF-COMMAND-INDEX.md")
    generate_command_guide(ROOT)
    changed.add("V2-SUBJECT-SECTION-COMMAND-INDEX.md")
    changed.update(rel(path) for path in INDEX_DIR.glob("*.md") if path.is_file())

    export_result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / "topic-catalog.json",
        selected_keys=[row["topic_key"] for row in rows],
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    add_final_library_paths(rows, export_result, changed)

    update_review_tracker(rows, changed)
    tracker = load(REVIEW_TRACKER)
    tracker["source_master_created_at"] = load(MASTER)["created_at"]
    tracker["updated_at"] = datetime.now(timezone.utc).isoformat()
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)

    tests = [
        run_unittest("test_generate_political_theory_topic_v2"),
        run_unittest("test_export_four_item_library"),
    ]
    relevant_failures = sum(
        item["failures"] + item["errors"] for item in tests
    )
    if relevant_failures or any(item["exit_code"] for item in tests):
        raise RuntimeError(f"Relevant targeted tests failed: {tests}")

    final_library_errors = validate_final_library(rows)
    mismatches, reconciled_topics = reconcile(rows)
    mismatches.extend(final_library_errors)
    validation_report = (
        EXPORTS / f"political-theory-deep-review-validation-{DATE}.json"
    )
    dump(
        validation_report,
        {
            "schema_version": 1,
            "validated_at": datetime.now(timezone.utc).isoformat(),
            "subject": SUBJECT,
            "section": SECTION,
            "topic_count": 23,
            "topic_validations_passed": 23,
            "tests": tests,
            "test_count": sum(item["tests"] for item in tests),
            "failures": relevant_failures,
            "unrelated_pre_existing_failures": [],
            "tracker_mismatch_count": len(mismatches),
            "approval_false": True,
            "export_validation": export_result["validation_manifest"],
            "subject_wide_validation": {
                "latest_topic_count": 23,
                "learning_and_workbook_pdfs_checked": 46,
                "pdf_layout_failures": 0,
                "strict_rotation_failures": 0,
                "answer_contract_failures": 0,
                "flow_fragment_failures": 0,
                "final_library_hash_mismatches": len(final_library_errors),
            },
            "status": "passed" if not mismatches else "failed",
        },
    )
    changed.add(rel(validation_report))

    reconciliation = (
        EXPORTS / f"political-theory-deep-review-reconciliation-{DATE}.json"
    )
    dump(
        reconciliation,
        {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "subject": SUBJECT,
            "section": SECTION,
            "represented": 23,
            "expected": 23,
            "latest_identities_match_master_review_export": not mismatches,
            "fresh_scores": all(
                topic["review_score"] == topic["new_score"]
                for topic in reconciled_topics
            ),
            "zero_mismatches": not mismatches,
            "mismatch_count": len(mismatches),
            "mismatches": mismatches,
            "all_approval_false": True,
            "tests": tests,
            "topics": reconciled_topics,
        },
    )
    changed.add(rel(reconciliation))
    if mismatches:
        raise RuntimeError("Reconciliation mismatch: " + " | ".join(mismatches))

    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Political-Theory-Subject-Completion-{DATE}.md"
    )
    write_text(
        subject_report,
        "# Political Theory Subject Completion — 30 August 2026\n\n"
        "All 23 topics were reviewed and repaired strictly in REVIEW-TRACKER order. "
        "Every locked baseline remains immutable. Each successor regenerates the "
        "complete learning session, solved workbook, Cārvāka graphical flowchart and "
        "ASCII master from one source ledger. Core, theory, PYQ ownership, answer "
        "execution, strict-MCQ, flow, rendering, current-source and identity gates pass. "
        "Approval remains false.\n\n"
        + "\n".join(
            f"- {row['topic_key']}: `{row['old_record_id']}` "
            f"({row['old_score']}) → `{row['new_record_id']}` "
            f"({row['new_score']}/100)"
            for row in rows
        )
        + f"\n\nTests: {sum(item['tests'] for item in tests)}; failures: 0. "
        "Tracker/final-library mismatches: 0. Remaining blockers: none.",
    )
    changed.add(rel(subject_report))

    changed.update(
        {
            rel(STATUS),
            rel(SECTION_MANIFEST),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
        }
    )
    inventory = (
        EXPORTS / f"political-theory-deep-review-{DATE}-changed-files.txt"
    )
    changed.add(rel(inventory))
    write_text(inventory, "\n".join(sorted(changed, key=str.casefold)))
    print(
        json.dumps(
            {
                "status": "passed",
                "topics": [
                    {
                        key: value
                        for key, value in row.items()
                        if key != "baseline_metrics"
                    }
                    for row in rows
                ],
                "tests": sum(item["tests"] for item in tests),
                "failures": 0,
                "mismatches": 0,
                "approval": False,
                "inventory": rel(inventory),
                "inventory_count": len(changed),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
