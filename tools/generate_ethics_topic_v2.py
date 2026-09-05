"""Generate source-complete learner-v2 Ethics topic packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from types import ModuleType
from typing import Sequence

import fitz

import carvaka_flowchart
import ethics_topic_01_data as topic01_data
import ethics_topic_02_data as topic02_data
import ethics_topic_03_data as topic03_data
import ethics_topic_04_data as topic04_data
import ethics_topic_05_data as topic05_data
import ethics_topic_06_data as topic06_data
import ethics_topic_07_data as topic07_data
import ethics_topic_08_data as topic08_data
import ethics_topic_09_data as topic09_data
import ethics_topic_10_data as topic10_data
import ethics_topic_11_data as topic11_data
import ethics_topic_12_data as topic12_data
import ethics_topic_13_data as topic13_data
import ethics_topic_14_data as topic14_data
import ethics_topic_15_data as topic15_data
import ethics_topic_16_data as topic16_data
import ethics_topic_17_data as topic17_data
import ethics_topic_18_data as topic18_data
import ethics_topic_19_data as topic19_data
import ethics_topic_20_data as topic20_data
import ethics_topic_21_data as topic21_data
import ethics_topic_22_data as topic22_data
import ethics_topic_23_data as topic23_data
import notions_style_ascii_master as ascii_master
from generate_philosophy_western_rationalism_v2 import render_ascii_pdf_safe
from generate_political_theory_topic_v2 import (
    ascii_panel_lines,
    create_concept_visual,
    demote_headings,
    semantic_split_wide_tables,
    source_preservation_errors,
)
from markdown_learning_pdf import RENDERER_VERSION, build_pdf
from validate_v2_export import (
    V2_VARIANT,
    validate_pdf,
    validate_tracker_record,
    validate_v2_markdown_text,
)


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Ethics"
LEARNING_ROOT = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
NOTES_ROOT = (
    ROOT
    / "notes"
    / "Ethics"
    / "learning-session-v2"
    / "subject-wide-syllabus"
)
FLOW_ROOT = ROOT / "notes" / "Ethics" / "flowcharts"
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "ethics--subject-wide-syllabus.json"
)
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
ASCII_SPECS = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
)
GRAPHICAL_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "ethics--subject-wide-syllabus-graphical-specs"
)
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
SYLLABUS_MAPPING = KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"
PYQ_SOURCES = (
    ROOT / "books" / "more_previous_papers" / "GENERAL-STUDIES-PAPER-IV.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM19-GeneralStudies-IV.pdf",
    ROOT / "books" / "more_previous_papers" / "Gen_St_P4.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf",
    ROOT / "books" / "mains" / "05 UPSC 2024 Paper-IV_Final 1.pdf",
    ROOT / "books" / "mains" / "UPSC Mains 2025 GS Paper 4.pdf",
)
LOCAL_REFERENCE_SOURCES = (
    ROOT / "books" / "ethics4.pdf",
)
GENERATION_DATE = date.today().isoformat()


@dataclass(frozen=True)
class Topic:
    number: int
    title: str
    source_slug: str
    data: ModuleType

    @property
    def topic_key(self) -> str:
        return f"ethics-{self.number:02d}"

    @property
    def session_titles(self) -> tuple[str, ...]:
        return tuple(self.data.SESSION_TITLES)

    @property
    def basic_path(self) -> Path:
        return KNOWLEDGE / "basic" / f"{self.number:02d}_{self.source_slug}.md"

    @property
    def advanced_path(self) -> Path:
        return KNOWLEDGE / "advanced" / f"{self.number:02d}_{self.source_slug}.md"


TOPICS = {
    1: Topic(
        1,
        "Ethics and Human Interface",
        "Ethics-and-Human-Interface",
        topic01_data,
    ),
    2: Topic(
        2,
        "Human Values and Lessons from Leaders",
        "Human-Values-and-Lessons-from-Leaders",
        topic02_data,
    ),
    3: Topic(
        3,
        "Attitude: Content, Structure and Persuasion",
        "Attitude-Content-Structure-and-Persuasion",
        topic03_data,
    ),
    4: Topic(
        4,
        "Aptitude and Foundational Values for Civil Service",
        "Aptitude-and-Foundational-Values-for-Civil-Service",
        topic04_data,
    ),
    5: Topic(
        5,
        "Emotional Intelligence in Administration",
        "Emotional-Intelligence-in-Administration",
        topic05_data,
    ),
    6: Topic(
        6,
        "Indian Moral Thinkers and Philosophers",
        "Indian-Moral-Thinkers-and-Philosophers",
        topic06_data,
    ),
    7: Topic(
        7,
        "Western Moral Philosophers and Thinkers",
        "Western-Moral-Philosophers-and-Thinkers",
        topic07_data,
    ),
    8: Topic(
        8,
        "Moral Theories: Deontology, Consequentialism, Virtue Ethics",
        "Moral-Theories-Deontology-Consequentialism-Virtue-Ethics",
        topic08_data,
    ),
    9: Topic(
        9,
        "Public Service Values, Status and Ethical Dilemmas",
        "Public-Service-Values-Status-and-Ethical-Dilemmas",
        topic09_data,
    ),
    10: Topic(
        10,
        "Sources of Ethical Guidance: Laws, Rules, Conscience",
        "Sources-of-Ethical-Guidance-Laws-Rules-Conscience",
        topic10_data,
    ),
    11: Topic(
        11,
        "Accountability and Ethical Governance",
        "Accountability-and-Ethical-Governance",
        topic11_data,
    ),
    12: Topic(
        12,
        "Corporate Governance and International Ethics",
        "Corporate-Governance-and-International-Ethics",
        topic12_data,
    ),
    13: Topic(
        13,
        "Emerging Ethics: Technology, AI and Environment",
        "Emerging-Ethics-Technology-AI-and-Environment",
        topic13_data,
    ),
    14: Topic(
        14,
        "Probity: Concept and Philosophical Basis of Governance",
        "Probity-Concept-and-Philosophical-Basis-of-Governance",
        topic14_data,
    ),
    15: Topic(
        15,
        "Transparency, RTI and Information Sharing",
        "Transparency-RTI-and-Information-Sharing",
        topic15_data,
    ),
    16: Topic(
        16,
        "Codes of Ethics and Codes of Conduct",
        "Codes-of-Ethics-and-Codes-of-Conduct",
        topic16_data,
    ),
    17: Topic(
        17,
        "Citizens' Charters, Work Culture and Service Delivery",
        "Citizens-Charters-Work-Culture-and-Service-Delivery",
        topic17_data,
    ),
    18: Topic(
        18,
        "Utilization of Public Funds and Challenges of Corruption",
        "Utilization-of-Public-Funds-and-Challenges-of-Corruption",
        topic18_data,
    ),
    19: Topic(
        19,
        "Corruption: Legal Framework",
        "Corruption-Legal-Framework",
        topic19_data,
    ),
    20: Topic(
        20,
        "Anti-Corruption Institutions",
        "Anti-Corruption-Institutions",
        topic20_data,
    ),
    21: Topic(
        21,
        "Protecting Honest Officials and Vigilance Administration",
        "Protecting-Honest-Officials-and-Vigilance-Administration",
        topic21_data,
    ),
    22: Topic(
        22,
        "Case Study Method and Answer Architecture",
        "Case-Study-Method-and-Answer-Architecture",
        topic22_data,
    ),
    23: Topic(
        23,
        "Comparative and Named Real Case Studies",
        "Comparative-and-Named-Real-Case-Studies",
        topic23_data,
    ),
}


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def latest_identity(topic_key: str) -> tuple[int, str | None, str | None]:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    records = [
        item
        for item in tracker.get("exports", [])
        if isinstance(item, dict) and item.get("topic_key") == topic_key
    ]
    learners = [item for item in records if item.get("variant") == V2_VARIANT]
    legacy = [item for item in records if item.get("variant") == "legacy-v1"]
    if learners:
        current = max(learners, key=lambda item: int(item.get("generation") or 1))
        legacy_id = next(
            (
                str(item["record_id"])
                for item in sorted(
                    legacy,
                    key=lambda value: int(value.get("generation") or 1),
                    reverse=True,
                )
            ),
            None,
        )
        return int(current["generation"]) + 1, str(current["record_id"]), legacy_id
    if legacy:
        current = max(legacy, key=lambda item: int(item.get("generation") or 1))
        record_id = str(current["record_id"])
        return int(current.get("generation") or 1) + 1, record_id, record_id
    return 1, None, None


def parse_h2_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    if not matches:
        raise ValueError("Basic owner has no H2 sections.")
    preamble = re.sub(
        r"(?m)^#\s+.+\n?",
        "",
        text[: matches[0].start()],
        count=1,
    ).strip()
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        title = match.group(1).strip()
        numbered = re.match(r"^(\d+(?:[a-z])?)\.\s+", title, re.IGNORECASE)
        key = numbered.group(1).casefold() if numbered else f"extra-{index + 1}"
        sections.append((key, text[match.start() : end].strip()))
    return preamble, sections


def build_core(topic: Topic, owner: str) -> str:
    preamble, ordered_sections = parse_h2_sections(owner)
    by_key = {key: value for key, value in ordered_sections}
    assigned: set[str] = set()
    rendered: list[str] = []
    groups = tuple(
        (str(group).casefold(),)
        if isinstance(group, str)
        else tuple(str(item).casefold() for item in group)
        for group in topic.data.SESSION_GROUPS
    )
    if len(topic.session_titles) != 10 or len(groups) != 10:
        raise ValueError(f"{topic.topic_key}: exactly ten session titles and groups are required.")
    for index, (title, group) in enumerate(zip(topic.session_titles, groups), start=1):
        parts: list[str] = []
        if index == 1 and preamble:
            parts.append(preamble)
        for key in group:
            if key not in by_key:
                raise ValueError(f"{topic.topic_key}: session group references missing section {key}.")
            if key in assigned:
                raise ValueError(f"{topic.topic_key}: section {key} is assigned more than once.")
            assigned.add(key)
            parts.append(by_key[key])
        if index == 10:
            parts.extend(
                value
                for key, value in ordered_sections
                if key not in assigned
            )
            assigned.update(key for key, _ in ordered_sections)
        body = demote_headings("\n\n".join(parts), 2)
        rendered.append(f"### SESSION {index} — {title}\n\n{body}")
    missing = [key for key, _ in ordered_sections if key not in assigned]
    if missing:
        raise ValueError(f"{topic.topic_key}: unassigned source sections: {missing}")
    return "\n\n---\n\n".join(rendered)


def item_groups(topic: Topic) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    for raw in topic.data.MCQ_ITEMS:
        item = {key: str(raw[key]).strip() for key in raw}
        grouped.setdefault(item["group"], []).append(item)
    return grouped


def rotated_options(
    correct: str,
    candidates: Sequence[str],
    position: int,
    seed: int,
) -> list[str]:
    unique = list(dict.fromkeys(value for value in candidates if value != correct))
    if len(unique) < 3:
        raise ValueError("Each MCQ family needs at least three distinct distractors.")
    rotated = unique[seed % len(unique) :] + unique[: seed % len(unique)]
    options = rotated[:3]
    options.insert(position, correct)
    return options


def build_mcqs(topic: Topic) -> str:
    groups = item_groups(topic)
    questions: list[tuple[str, str, list[str], str]] = []
    for item_index, raw in enumerate(topic.data.MCQ_ITEMS):
        item = {key: str(raw[key]).strip() for key in raw}
        family = groups[item["group"]]
        statements = [candidate["statement"] for candidate in family]
        for scenario_key in ("scenario_a", "scenario_b"):
            scenario = item[scenario_key]
            if not scenario.endswith(("?", ".", "!")):
                scenario += "."
            stem = (
                f"{scenario} Which source-grounded ethical principle most precisely "
                "explains the case?"
            )
            position = len(questions) % 4
            options = rotated_options(
                item["statement"],
                statements,
                position,
                item_index + len(questions),
            )
            questions.append((stem, item["statement"], options, item["label"]))
    rendered: list[str] = []
    letters = "ABCD"
    for number, (stem, correct, options, label) in enumerate(questions, start=1):
        position = (number - 1) % 4
        if options[position] != correct:
            raise AssertionError("MCQ rotation construction failed.")
        option_lines = "\n\n".join(
            f"{letters[index]}. {option}"
            for index, option in enumerate(options)
        )
        rendered.append(
            f"#### MCQ {number}\n\n{stem}\n\n{option_lines}\n\n"
            f"**Answer:** {letters[position]}\n\n"
            f"**Explanation:** **{label}** is the controlling principle. "
            f"{correct} The distractors are related propositions, but they do not "
            "identify the decisive mechanism in this case."
        )
    return "\n\n---\n\n".join(rendered)


def build_pyqs(topic: Topic) -> str:
    blocks: list[str] = []
    for number, item in enumerate(topic.data.PYQS, start=1):
        marks = int(item["marks"])
        blocks.append(
            f"#### Solved PYQ {number} — {item['year']} — {marks} marks\n\n"
            f"**Question:** {str(item['question']).strip()}\n\n"
            f"**Source / ownership:** {str(item['source_note']).strip()}\n\n"
            "**Model solution**\n\n"
            f"{str(item['answer']).strip()}\n\n"
            "**Why this earns marks:** It states the governing ethical idea, "
            "translates it into public administration, uses a concrete Indian "
            "illustration, acknowledges a limit, and ends with a reasoned verdict."
        )
    return "\n\n---\n\n".join(blocks)


def build_original_practice(topic: Topic) -> str:
    blocks: list[str] = []
    limits = {10: 150, 15: 200, 20: 250}
    for number, item in enumerate(topic.data.ORIGINAL_MAINS, start=1):
        marks = int(item["marks"])
        blocks.append(
            f"#### Original Mains Practice {number} — {marks} marks\n\n"
            f"**Question:** {str(item['question']).strip()} "
            f"Answer in about {limits[marks]} words.\n\n"
            "**Model solution**\n\n"
            f"{str(item['answer']).strip()}\n\n"
            "**Why this earns marks:** The response defines the issue, develops "
            "the relevant mechanism with India-centric evidence, tests a limitation, "
            "and gives a mark-scaled conclusion."
        )
    return "\n\n---\n\n".join(blocks)


def panel_lines(panel: dict[str, object]) -> list[str]:
    return ascii_panel_lines(
        str(panel["title"]),
        [str(value) for value in panel["nodes"]],
        (
            f"VERDICT -> {str(panel['verdict']).strip()}",
            f"ANSWER USE -> {str(panel['answer_use']).strip()}",
        ),
        max_lines=32,
        fact_width=94,
    )


def embedded_ascii_atlas(topic: Topic) -> str:
    chunks: list[str] = []
    for index, panel in enumerate(topic.data.ASCII_PANELS, start=1):
        chunks.append(
            f"#### ASCII PANEL {index}/12 — {panel['title']}\n\n"
            "```text\n"
            + "\n".join(panel_lines(panel))
            + "\n```"
        )
    return (
        "### EMBEDDED TWELVE-PANEL ASCII REVISION ATLAS\n\n"
        "The panels compress the learning route without replacing the complete "
        "teaching and solved practice above.\n\n"
        + "\n\n".join(chunks)
    )


def build_register_notes(topic: Topic) -> str:
    items = list(topic.data.MCQ_ITEMS)
    grid_rows = "\n".join(
        f"| {item['label']} | {item['statement']} |"
        for item in items[:12]
    )
    revision = "\n".join(
        f"- **{item['label']}:** {item['statement']}"
        for item in items[12:]
    )
    return (
        embedded_ascii_atlas(topic)
        + "\n\n### ONE-PAGE CONCEPT GRID\n\n"
        "| Concept / thinker | Exam-ready formulation |\n"
        "|---|---|\n"
        f"{grid_rows}\n\n"
        "### CORE REVISION SPINE\n\n"
        f"{revision}\n\n"
        "### SOURCE AND ATTRIBUTION DISCIPLINE\n\n"
        f"{topic.data.SOURCE_CAVEAT.strip()}\n\n"
        "### ANSWER SPINE\n\n"
        "1. Define the precise ethical concept or teaching.\n"
        "2. State a qualified thesis rather than a moral slogan.\n"
        "3. Explain the causal or decision-making mechanism.\n"
        "4. Add one specific Indian administrative illustration.\n"
        "5. Test the strongest limitation or attribution caveat.\n"
        "6. End with a practical, institution-aware verdict.\n\n"
        + demote_headings(topic.data.REGISTER_SUPPLEMENT.strip(), 1)
    )


def build_documents(
    topic: Topic,
    generation: int,
) -> tuple[str, str, dict[str, object]]:
    owner = topic.basic_path.read_text(encoding="utf-8")
    advanced = topic.advanced_path.read_text(encoding="utf-8")
    core = build_core(topic, owner)
    mcqs = build_mcqs(topic)
    pyqs = build_pyqs(topic)
    original = build_original_practice(topic)
    advanced_body = re.sub(r"(?m)^#\s+.+\n?", "", advanced, count=1).strip()
    advanced_body = demote_headings(advanced_body, 1)
    register = build_register_notes(topic)
    identity = f"{topic.topic_key}:{V2_VARIANT}:g{generation}"
    anchor = topic.data.CURRENT_ANCHOR
    if isinstance(anchor, dict):
        anchor_lines = [
            f"**{str(anchor.get('title') or 'Current linkage').strip()}**",
            "",
            *(
                f"- ✅ Fact: {str(item).strip()}"
                for item in anchor.get("verified_facts", ())
            ),
            "",
            f"**⚠️ Inference / administrative link:** "
            f"{str(anchor.get('administrative_link') or '').strip()}",
            "",
            f"**⚠️ Limit:** {str(anchor.get('limit') or '').strip()}",
        ]
        current_anchor = "\n".join(anchor_lines)
    else:
        current_anchor = str(anchor).strip()
    source_urls = "  \n".join(
        f"- {url}" for url in topic.data.CURRENT_SOURCE_URLS
    )
    header = (
        "---\n"
        f"topic_key: {topic.topic_key}\n"
        f"title: {topic.title} — Complete Topic Package\n"
        f"generation_identity: {identity}\n"
        f"generated_on: {GENERATION_DATE}\n"
        "---\n\n"
        f"# {topic.title} — Complete Topic Package\n\n"
        "**Subject:** Ethics  \n"
        "**Section:** Subject-wide Syllabus  \n"
        f"**Generation:** learner-v2:g{generation}  \n"
        "**Ownership:** GS-IV Ethics topic; recent official-paper questions retain "
        "their exact year, paper and source note.  \n"
        "**Source policy:** complete Basic owner first; solved practice before "
        "optional Advanced depth; consolidated register notes last.\n\n"
        "### CURRENT-AFFAIRS ANCHOR\n\n"
        f"{current_anchor}\n\n"
        f"**Official source links:**  \n{source_urls}\n\n"
        f"**Source caution:** {topic.data.SOURCE_CAVEAT.strip()}\n"
    )
    practice = (
        pyqs
        + "\n\n---\n\n### ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS\n\n"
        + original
    )
    main = (
        header
        + "\n## BASIC LEARNING SESSION\n\n"
        + core
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + advanced_body
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + register
    )
    workbook = (
        "---\n"
        f"topic_key: {topic.topic_key}\n"
        f"title: {topic.title} — Solved Practice Workbook\n"
        f"generation_identity: {identity}\n"
        f"generated_on: {GENERATION_DATE}\n"
        "---\n\n"
        f"# {topic.title} — Solved Practice Workbook\n\n"
        f"**Generation:** learner-v2:g{generation}  \n"
        "**PYQ ownership:** Questions labelled as official reproduce the locally "
        "held UPSC GS-IV papers; routed historical demands are explicitly neutral "
        "renderings rather than invented quotations.\n\n"
        "## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
    )
    metadata = {
        "identity": identity,
        "session_count": len(re.findall(r"(?m)^### SESSION \d+ ", main)),
        "mcq_count": len(re.findall(r"(?m)^#### MCQ \d+$", main)),
        "pyq_count": len(re.findall(r"(?m)^#### Solved PYQ \d+", main)),
        "source_basic_sha256": sha256(topic.basic_path),
        "source_advanced_sha256": sha256(topic.advanced_path),
    }
    return main, workbook, metadata


def answer_word_count(answer: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", answer))


def validate_data(topic: Topic) -> list[str]:
    errors: list[str] = []
    if len(topic.data.SESSION_TITLES) != 10:
        errors.append("Exactly ten session titles are required.")
    if len(topic.data.SESSION_GROUPS) != 10:
        errors.append("Exactly ten session groups are required.")
    items = list(topic.data.MCQ_ITEMS)
    if len(items) != 24:
        errors.append("Exactly 24 MCQ concept items are required.")
    grouped = item_groups(topic)
    if any(len(values) < 4 for values in grouped.values()):
        errors.append("Every MCQ family must contain at least four concepts.")
    for index, item in enumerate(items, start=1):
        missing = {"label", "statement", "scenario_a", "scenario_b", "group"} - set(item)
        if missing:
            errors.append(f"MCQ item {index} lacks fields: {sorted(missing)}.")
            continue
        count = answer_word_count(str(item["statement"]))
        if not 18 <= count <= 65:
            errors.append(f"MCQ item {index} statement has {count} words; expected 18-65.")
        if re.search(r"(?i)\b(section|file|metadata|owner)\b", str(item["statement"])):
            errors.append(f"MCQ item {index} leaks source-routing metadata.")
    expected_marks = [10, 10, 15, 15, 20, 20]
    actual_marks = [int(item["marks"]) for item in topic.data.ORIGINAL_MAINS]
    if actual_marks != expected_marks:
        errors.append(f"Original Mains marks must be {expected_marks}, found {actual_marks}.")
    ranges = {10: (120, 185), 15: (175, 255), 20: (230, 350)}
    for index, item in enumerate(topic.data.ORIGINAL_MAINS, start=1):
        count = answer_word_count(str(item["answer"]))
        low, high = ranges[int(item["marks"])]
        if not low <= count <= high:
            errors.append(
                f"Original Mains answer {index} has {count} words; expected {low}-{high}."
            )
    pyq_count = len(topic.data.PYQS)
    pyq_ranges = {
        1: (5, 7),
        2: (8, 12),
        3: (5, 8),
        4: (8, 12),
        5: (5, 8),
        6: (8, 12),
        7: (10, 12),
        8: (10, 12),
        9: (10, 12),
        10: (10, 12),
        11: (10, 12),
        12: (10, 12),
        13: (10, 12),
        14: (8, 12),
        15: (8, 12),
        16: (8, 12),
        17: (8, 12),
        18: (8, 12),
        19: (8, 12),
        20: (8, 12),
        21: (8, 12),
        22: (8, 12),
        23: (8, 12),
    }
    if topic.number in pyq_ranges:
        low, high = pyq_ranges[topic.number]
        if not low <= pyq_count <= high:
            errors.append(
                f"Topic {topic.number:02d} requires {low}-{high} solved PYQs."
            )
    panels = list(topic.data.ASCII_PANELS)
    if len(panels) != 12:
        errors.append("Exactly twelve authored ASCII panels are required.")
    for index, panel in enumerate(panels, start=1):
        if len(panel.get("nodes", ())) != 8:
            errors.append(f"ASCII panel {index} must contain exactly eight nodes.")
        if not panel.get("verdict") or not panel.get("answer_use"):
            errors.append(f"ASCII panel {index} needs verdict and answer-use text.")
    return errors


def validate_documents(topic: Topic, main: str, workbook: str) -> list[str]:
    errors = validate_data(topic)
    errors.extend(validate_v2_markdown_text(main))
    if len(re.findall(r"(?m)^### SESSION \d+ ", main)) != 10:
        errors.append("The Basic learning session must contain exactly ten sessions.")
    if len(re.findall(r"(?m)^#### MCQ \d+$", main)) != 48:
        errors.append("The main package must contain exactly 48 MCQs.")
    if len(re.findall(r"(?m)^#### MCQ \d+$", workbook)) != 48:
        errors.append("The standalone workbook must contain exactly 48 MCQs.")
    answers = re.findall(r"(?m)^\*\*Answer:\*\*\s*([ABCD])\s*$", main)
    expected = ["ABCD"[index % 4] for index in range(48)]
    if answers[:48] != expected:
        errors.append("MCQ answer rotation is not strict A -> B -> C -> D.")
    errors.extend(
        source_preservation_errors(
            topic.basic_path.read_text(encoding="utf-8"),
            main,
        )
    )
    errors.extend(
        source_preservation_errors(
            topic.advanced_path.read_text(encoding="utf-8"),
            main,
        )
    )
    if not main.rstrip().endswith(
        demote_headings(topic.data.REGISTER_SUPPLEMENT.strip(), 1)
    ):
        errors.append("Consolidated register notes are not the final substantive content.")
    return errors


def make_ascii_spec(
    topic: Topic,
    generation: int,
    markdown_path: Path,
) -> dict[str, object]:
    panels: list[dict[str, object]] = []
    for index, panel in enumerate(topic.data.ASCII_PANELS, start=1):
        references: object = (
            {"sessions": [index]}
            if index <= 10
            else [
                "BASIC MCQS / REMEDIATION"
                if index == 11
                else "PYQS AND ANSWER PRACTICE"
            ]
        )
        panels.append(
            {
                "panel_title": str(panel["title"]),
                "structural_type": str(panel["structural_type"]),
                "source_references": references,
                "lines": panel_lines(panel),
            }
        )
    return {
        "schema_version": 2,
        "benchmark": (
            "Carvaka-standard continuous master with a topic-specific Ethics "
            "twelve-panel atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": f"Ethics subject-wide syllabus topic {topic.number:02d}",
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "english_first": True,
            "approved": False,
        },
        "topics": [
            {
                "topic_key": topic.topic_key,
                "title": topic.title,
                "source_markdown": relative(markdown_path),
                "source_record": f"{topic.topic_key}:{V2_VARIANT}:g{generation}",
                "approved_master_reference": str(
                    carvaka_flowchart.REFERENCE_FOLDER
                    / "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ).replace("/", "\\"),
                "benchmark_preservation": (
                    "The approved design reference, prior artifacts and canonical "
                    "Ethics owners remain immutable."
                ),
                "panels": panels,
            }
        ],
    }


def normalize_pdf_metadata(path: Path, title: str, topic: Topic) -> None:
    compact = GENERATION_DATE.replace("-", "")
    pdf_date = f"D:{compact}000000+05'30'"
    temporary = path.with_suffix(path.suffix + ".metadata.pdf")
    with fitz.open(path) as document:
        current = dict(document.metadata or {})
        document.set_metadata(
            {
                "title": title,
                "author": "UPSC Agent / Copilot CLI",
                "subject": f"Ethics, Subject-wide Syllabus, Topic {topic.number:02d}",
                "keywords": f"{topic.topic_key}; learner-v2; ethics; GS-IV",
                "creator": Path(__file__).name,
                "producer": current.get("producer") or "PyMuPDF",
                "creationDate": pdf_date,
                "modDate": pdf_date,
                "trapped": current.get("trapped") or "",
            }
        )
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, path)


def paths_for(topic: Topic, generation: int) -> dict[str, Path]:
    flow_dir = (
        FLOW_ROOT
        / topic.topic_key
        / f"continuous-at-a-glance-english-first-g{generation}"
    )
    return {
        "markdown": LEARNING_ROOT / f"{topic.topic_key}_Learning-Session.md",
        "workbook_markdown": LEARNING_ROOT / f"{topic.topic_key}_Solved-Workbook.md",
        "main_pdf": NOTES_ROOT
        / "notes"
        / f"{topic.topic_key}_Learning-Session_{GENERATION_DATE}.pdf",
        "workbook_pdf": NOTES_ROOT
        / "workbooks"
        / f"{topic.topic_key}_Solved-Workbook_{GENERATION_DATE}.pdf",
        "asset_folder": NOTES_ROOT / "assets" / topic.topic_key,
        "concept_visual": NOTES_ROOT
        / "assets"
        / topic.topic_key
        / f"{topic.topic_key}_concept-map_g{generation}.png",
        "main_visual_audit": NOTES_ROOT
        / "assets"
        / topic.topic_key
        / f"{topic.topic_key}_main-visual-audit_g{generation}.json",
        "workbook_visual_audit": NOTES_ROOT
        / "assets"
        / topic.topic_key
        / f"{topic.topic_key}_workbook-visual-audit_g{generation}.json",
        "flow_dir": flow_dir,
        "ascii_markdown": FLOW_ROOT
        / topic.topic_key
        / f"{topic.topic_key}_Twelve-Panel-ASCII-Master_{GENERATION_DATE}-g{generation}.md",
        "ascii_pdf": flow_dir / "ascii-master.pdf",
        "ascii_spec": ASCII_SPECS
        / f"ethics--subject-wide-syllabus-{topic.number:02d}-ascii-{GENERATION_DATE}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPECS / f"{topic.topic_key}-g{generation}.json",
        "record": EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{GENERATION_DATE}-record.json",
        "validation": EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{GENERATION_DATE}-validation.json",
    }


def ensure_manifest() -> dict[str, object]:
    if MANIFEST.is_file():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = [
        item
        for item in catalog.get("topics", [])
        if item.get("subject", {}).get("key") == "Ethics"
        and item.get("section", {}).get("key") == "subject-wide-syllabus"
    ]
    entries.sort(key=lambda item: int(item["topic_order"]))
    topics = [
        {
            "topic_key": item["topic_key"],
            "display_title": item["display_title"],
            "syllabus_mapping": (
                "Direct GS-IV Ethics syllabus ownership under the subject-wide "
                "topic map; verified questions retain official or routed provenance."
            ),
            "source_basic": item["source_basic"],
            "source_canonical": item["source_canonical"],
            "source_advanced": item["source_advanced"],
            "cross_topic_sources": [
                "upsc-ai-kit\\knowledge\\Ethics\\00_Master-Framework.md",
                "upsc-ai-kit\\knowledge\\Ethics\\README.md",
                "upsc-ai-kit\\knowledge\\Ethics\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            ],
            "verified_pyq_sources": [relative(path) for path in PYQ_SOURCES],
        }
        for item in entries
    ]
    if len(topics) != 23:
        raise ValueError(f"Expected 23 Ethics topics, found {len(topics)}.")
    manifest = {
        "schema_version": 1,
        "variant": V2_VARIANT,
        "subject": {"key": "Ethics", "display_name": "Ethics"},
        "section": {
            "key": "subject-wide-syllabus",
            "name": "Subject-wide Syllabus",
            "scope": "official-section",
            "complete_syllabus_section": True,
            "syllabus_sources": [
                relative(SYLLABUS_MAPPING),
                "upsc-ai-kit\\knowledge\\Ethics\\README.md",
                "upsc-ai-kit\\knowledge\\Ethics\\LEARNING-SESSION-COMMAND-INDEX.md",
            ],
            "notes": (
                "Complete Ethics topic map in source order. Each Basic owner remains "
                "canonical and Advanced depth remains optional."
            ),
        },
        "topics": topics,
    }
    write_json(MANIFEST, manifest)
    return manifest


def update_manifest(
    manifest: dict[str, object],
    topic: Topic,
    generation: int,
    paths: dict[str, Path],
    legacy_id: str | None,
) -> None:
    item = next(
        value
        for value in manifest["topics"]
        if value.get("topic_key") == topic.topic_key
    )
    item.update(
        {
            "assembled_markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "notes_pdf": relative(paths["main_pdf"]),
            "workbook_pdf": relative(paths["workbook_pdf"]),
            "asset_folder": relative(paths["asset_folder"]),
            "ascii_master_spec": relative(paths["ascii_spec"]),
            "graphical_flowchart_folder": relative(paths["flow_dir"]),
            "generation_identity": f"{topic.topic_key}:{V2_VARIANT}:g{generation}",
            "approved": False,
            "superseded_v1": legacy_id,
        }
    )
    write_json(MANIFEST, manifest)


def build_record(
    topic: Topic,
    generation: int,
    supersedes: str | None,
    legacy_id: str | None,
    paths: dict[str, Path],
    flow_metadata: dict[str, object],
) -> dict[str, object]:
    flow_folder = ROOT / Path(str(flow_metadata["folder"]).replace("\\", "/"))
    outputs = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["concept_visual"],
        paths["ascii_markdown"],
        paths["ascii_pdf"],
        paths["ascii_spec"],
        paths["graphical_spec"],
        *[path for path in flow_folder.rglob("*") if path.is_file()],
    ]
    record_id = f"{topic.topic_key}:{V2_VARIANT}:g{generation}"
    source_paths = [
        topic.basic_path,
        topic.advanced_path,
        SYLLABUS_MAPPING,
        *LOCAL_REFERENCE_SOURCES,
        *PYQ_SOURCES,
    ]
    return {
        "record_id": record_id,
        "topic_key": topic.topic_key,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Ethics — Subject-wide Syllabus — "
            f"{topic.title}"
        ),
        "main_pdf": relative(paths["main_pdf"]),
        "workbook": relative(paths["workbook_pdf"]),
        "markdown": relative(paths["markdown"]),
        "asset_folder": relative(paths["asset_folder"]),
        "approved": False,
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": record_id,
        },
        "provenance": {
            "workflow": "learner-first-v2-ethics-topic-generator",
            "source_basic": relative(topic.basic_path),
            "source_canonical": relative(topic.basic_path),
            "source_advanced": relative(topic.advanced_path),
            "assembled_markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "pyq_corpus": [relative(path) for path in PYQ_SOURCES],
            "local_reference_sources": [
                relative(path) for path in LOCAL_REFERENCE_SOURCES
            ],
            "subject_boundary": (
                "This package directly owns its GS-IV syllabus clause. Exact recent "
                "questions are distinguished from neutral historical routing notes."
            ),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": RENDERER_VERSION,
            },
            "generation_date": GENERATION_DATE,
            "superseded_v1": legacy_id,
            "source_hashes": {
                relative(path): sha256(path)
                for path in source_paths
                if path.is_file()
            },
            "deliverable_hashes": {
                relative(path): sha256(path) for path in outputs
            },
            "concept_visual": relative(paths["concept_visual"]),
            "ascii_master_spec": relative(paths["ascii_spec"]),
            "ascii_master_pdf": relative(paths["ascii_pdf"]),
            "graphical_flowchart_folder": str(flow_metadata["folder"]),
        },
        "continuous_core_first": flow_metadata,
        "validation": {
            "state": "passed",
            "validated_on": GENERATION_DATE,
            "validator": (
                "tools/generate_ethics_topic_v2.py + "
                "tools/validate_v2_export.py"
            ),
        },
    }


def run(command: Sequence[str], description: str) -> dict[str, object]:
    completed = subprocess.run(
        list(command),
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (completed.stdout + "\n" + completed.stderr).strip()
    if completed.returncode:
        raise RuntimeError(f"{description} failed:\n{output}")
    return {
        "description": description,
        "command": subprocess.list2cmdline(list(command)),
        "output_tail": output.splitlines()[-20:],
    }


def generate(topic: Topic, publish: bool = True) -> dict[str, object]:
    generation, supersedes, legacy_id = latest_identity(topic.topic_key)
    paths = paths_for(topic, generation)
    main, workbook, metadata = build_documents(topic, generation)
    errors = validate_documents(topic, main, workbook)
    if errors:
        raise ValueError("\n- " + "\n- ".join(errors))

    write_text(paths["markdown"], main)
    write_text(paths["workbook_markdown"], workbook)
    create_concept_visual(topic, paths["concept_visual"])
    write_json(paths["ascii_spec"], make_ascii_spec(topic, generation, paths["markdown"]))
    manual = ascii_master.normalize_manual_spec_file(paths["ascii_spec"])[topic.topic_key]
    ascii_fragment = ascii_master.build_manual_fragment(manual)
    standalone_ascii = ascii_master.standalone_panel_text(ascii_fragment)
    write_text(
        paths["ascii_markdown"],
        f"# {topic.title} — Twelve-Panel ASCII Master\n\n{ascii_fragment}",
    )
    write_json(
        paths["graphical_spec"],
        carvaka_flowchart.author_topic_spec(
            topic_key=topic.topic_key,
            subject="Ethics",
            title=topic.title,
            source_markdown=main.replace("...", " — ").replace("…", " — "),
            source_markdown_path=relative(paths["markdown"]),
            ascii_spec_path=relative(paths["ascii_spec"]),
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
        ),
    )

    rendered_main = semantic_split_wide_tables(main)
    rendered_workbook = semantic_split_wide_tables(workbook)
    write_text(paths["markdown"], rendered_main)
    write_text(paths["workbook_markdown"], rendered_workbook)
    try:
        build_pdf(
            paths["markdown"],
            paths["main_pdf"],
            mode="main",
            image_path=paths["concept_visual"],
            variant=V2_VARIANT,
            topic_key=topic.topic_key,
            repository_root=ROOT,
            visual_audit_path=paths["main_visual_audit"],
        )
        build_pdf(
            paths["workbook_markdown"],
            paths["workbook_pdf"],
            mode="workbook",
            image_path=paths["concept_visual"],
            variant=V2_VARIANT,
            topic_key=topic.topic_key,
            repository_root=ROOT,
            visual_audit_path=paths["workbook_visual_audit"],
            standalone_workbook=True,
        )
    finally:
        write_text(paths["markdown"], main)
        write_text(paths["workbook_markdown"], workbook)

    preservation_paths = [
        topic.basic_path,
        topic.advanced_path,
        SYLLABUS_MAPPING,
        *LOCAL_REFERENCE_SOURCES,
        *PYQ_SOURCES,
        *[
            ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
            for name in carvaka_flowchart.REFERENCE_HASHES
        ],
    ]
    preservation_before = {
        relative(path): sha256(path)
        for path in preservation_paths
        if path.is_file()
    }
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_dir"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    render_ascii_pdf_safe(
        standalone_ascii,
        paths["ascii_pdf"],
        title=f"{topic.title} — ASCII Master Flowchart",
        creator=Path(__file__).name,
    )
    normalize_pdf_metadata(
        paths["main_pdf"],
        f"{topic.title} — Complete Topic Package",
        topic,
    )
    normalize_pdf_metadata(
        paths["workbook_pdf"],
        f"{topic.title} — Solved Practice Workbook",
        topic,
    )
    normalize_pdf_metadata(
        paths["ascii_pdf"],
        f"{topic.title} — Twelve-Panel ASCII Master",
        topic,
    )
    for flow_name, flow_title in (
        ("poster.pdf", f"{topic.title} — At-a-Glance Poster"),
        ("tiled.pdf", f"{topic.title} — Printable Tiled Flowchart"),
    ):
        normalize_pdf_metadata(paths["flow_dir"] / flow_name, flow_title, topic)

    pdf_errors = validate_pdf(paths["main_pdf"]) + validate_pdf(paths["workbook_pdf"])
    pdf_errors.extend(
        f"graphical package: {error}"
        for error in render_result.validation_errors
    )
    if pdf_errors:
        raise ValueError("\n- " + "\n- ".join(pdf_errors))

    flow_metadata["approval"] = False
    flow_metadata["ascii_master_spec"] = relative(paths["ascii_spec"])
    flow_metadata["ascii_master_spec_sha256"] = sha256(paths["ascii_spec"])
    flow_metadata["ascii_master_pdf"] = relative(paths["ascii_pdf"])
    flow_metadata["ascii_master_source"] = "manual-authored-ethics-twelve-panel-spec"
    manifest = ensure_manifest()
    update_manifest(manifest, topic, generation, paths, legacy_id)
    record = build_record(
        topic,
        generation,
        supersedes,
        legacy_id,
        paths,
        flow_metadata,
    )
    write_json(paths["record"], record)

    commands: list[dict[str, object]] = []
    validation = {
        "topic_key": topic.topic_key,
        "generation": generation,
        "identity": metadata["identity"],
        "approved": False,
        "session_count": metadata["session_count"],
        "mcq_count": metadata["mcq_count"],
        "pyq_count": metadata["pyq_count"],
        "source_preservation": "passed",
        "pdf_validation": "passed",
        "published": False,
        "commands": commands,
        "outputs": {key: relative(value) for key, value in paths.items()},
    }
    # The atomic finalizer validates this topic-scoped result before publishing.
    write_json(paths["validation"], validation)

    if publish:
        commands.append(
            run(
                [
                    sys.executable,
                    str(TOOLS / "finalize_v2_topic.py"),
                    "--repository-root",
                    str(ROOT),
                    "--manifest",
                    str(MANIFEST),
                    "--record-file",
                    str(paths["record"]),
                ],
                "Finalize learner-v2 topic",
            )
        )
        commands.append(
            run(
                [
                    sys.executable,
                    str(TOOLS / "generate_v2_topic_command_catalog.py"),
                    "--repository-root",
                    str(ROOT),
                    "--guide",
                ],
                "Refresh learner-v2 topic catalogue",
            )
        )
        commands.append(
            run(
                [
                    sys.executable,
                    str(TOOLS / "generate_learning_session_command_indexes.py"),
                ],
                "Refresh learning-session command indexes",
            )
        )
        tracker_errors = validate_tracker_record(
            TRACKER,
            topic.topic_key,
            V2_VARIANT,
            generation,
            repository_root=ROOT,
            check_paths=True,
        )
        if tracker_errors:
            raise ValueError("\n- " + "\n- ".join(tracker_errors))

    validation["published"] = publish
    write_json(paths["validation"], validation)
    return validation


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic", type=int, choices=sorted(TOPICS))
    parser.add_argument(
        "--no-publish",
        action="store_true",
        help="Generate and validate artifacts without updating shared trackers/indexes.",
    )
    args = parser.parse_args()
    result = generate(TOPICS[args.topic], publish=not args.no_publish)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
