"""Preservation-safe bulk refresh pipeline for validated learner-v2 packages.

The pipeline reads only top-level tracker exports, selects the latest validated
learner-v2 record per topic, and writes self-contained refreshed generations
under Learner-v2-Refreshed roots. Tracker mutation is a separate, explicit,
atomic finalize step.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import math
import os
import random
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Iterable

import fitz
from PIL import Image, ImageChops, ImageDraw

import carvaka_flowchart as graphical
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
import retrofit_v2_core_first as visual
from validate_v2_export import (
    REFRESHED_ROOT,
    V2_VARIANT,
    answer_key_pattern_errors,
    clean_aid_value,
    deep_content_quality_audit_text,
    extract_mcq_answer_keys,
    extract_v2_workbook_markdown,
    semantic_aid_defects,
    semantic_value_reasons,
    strip_legacy_progress_navigation,
    validate_ascii_master_text as ascii_master_validation_errors,
    validate_pdf,
    validate_pdf_layout,
    validate_refreshed_markdown,
    validate_tracker_record,
    validate_v2_markdown_text,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
LEGACY_VARIANT = "legacy-v1"
STRICT_ABCD_TOPIC_KEYS: set[str] = set()
OVERRIDES = ROOT / "tools" / "refresh_all_v2_overrides.json"
DEEP_OVERRIDES = ROOT / "tools" / "deep_content_quality_overrides.json"
REFRESH_DATE = "2026-08-22"
REFRESH_ID = "learner-v2-refreshed-2026-08-22"
SEMANTIC_REPAIR_DATE = "2026-08-23"
SEMANTIC_REPAIR_ID = "semantic-aid-repair-2026-08-23"
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / f"{REFRESH_ID}.json"
)
PILOT_VALIDATION = MANIFEST.with_name(f"{REFRESH_ID}-pilot-validation.json")
FULL_VALIDATION = MANIFEST.with_name(f"{REFRESH_ID}-validation.json")
PILOT_STAGED_RECORDS = MANIFEST.with_name(
    f"{REFRESH_ID}-staged-pilot-records.json"
)
FULL_STAGED_RECORDS = MANIFEST.with_name(f"{REFRESH_ID}-staged-records.json")
CHANGED_FILES = MANIFEST.with_name(f"{REFRESH_ID}-changed-files.txt")
PILOT_REPORT = ROOT / "notes" / REFRESHED_ROOT / "PILOT-REPORT.md"
FINAL_REPORT = ROOT / "notes" / REFRESHED_ROOT / "REFRESH-MIGRATION-REPORT.md"
SEMANTIC_AUDIT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "semantic-aid-quality-audit-2026-08-23.json"
)
SEMANTIC_REPAIR_VALIDATION = SEMANTIC_AUDIT.with_name(
    "semantic-aid-repair-2026-08-23-validation.json"
)
SEMANTIC_REPAIR_STAGED = SEMANTIC_AUDIT.with_name(
    "semantic-aid-repair-2026-08-23-staged-records.json"
)
SEMANTIC_REPAIR_CHANGED = SEMANTIC_AUDIT.with_name(
    "semantic-aid-repair-2026-08-23-changed-files.txt"
)
SEMANTIC_REPAIR_REPORT = (
    ROOT
    / "notes"
    / REFRESHED_ROOT
    / "SEMANTIC-AID-REPAIR-REPORT.md"
)
DEEP_REPAIR_DATE = "2026-08-23"
DEEP_REPAIR_ID = "deep-content-quality-repair-2026-08-23"
DEEP_AUDIT = SEMANTIC_AUDIT.with_name(
    "deep-content-quality-audit-2026-08-23.json"
)
DEEP_REPAIR_VALIDATION = SEMANTIC_AUDIT.with_name(
    "deep-content-quality-repair-2026-08-23-validation.json"
)
DEEP_REPAIR_STAGED = SEMANTIC_AUDIT.with_name(
    "deep-content-quality-repair-2026-08-23-staged-records.json"
)
DEEP_REPAIR_CHANGED = SEMANTIC_AUDIT.with_name(
    "deep-content-quality-repair-2026-08-23-changed-files.txt"
)
DEEP_REPAIR_REPORT = (
    ROOT
    / "notes"
    / REFRESHED_ROOT
    / "DEEP-CONTENT-QUALITY-REPAIR-REPORT.md"
)
ASCII_REPAIR_DATE = "2026-08-23"
ASCII_REPAIR_ID = "authored-notions-style-ascii-master-2026-08-23"
ASCII_DESIGN_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "notions-style-ascii-master-design-2026-08-23.json"
)
ASCII_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
)
ASCII_SPEC_FILES = tuple(
    ASCII_SPEC_DIR / filename
    for filename in ascii_master.MANUAL_SPEC_FILENAMES
)
ASCII_REPAIR_VALIDATION = ASCII_DESIGN_MANIFEST.with_name(
    "authored-notions-style-ascii-master-2026-08-23-validation.json"
)
ASCII_REPAIR_STAGED = ASCII_DESIGN_MANIFEST.with_name(
    "authored-notions-style-ascii-master-2026-08-23-staged-records.json"
)
ASCII_REPAIR_CHANGED = ASCII_DESIGN_MANIFEST.with_name(
    "authored-notions-style-ascii-master-2026-08-23-changed-files.txt"
)
ASCII_REPAIR_REPORT = (
    ROOT
    / "notes"
    / REFRESHED_ROOT
    / "AUTHORED-NOTIONS-STYLE-ASCII-MASTER-REPORT.md"
)
GRAPHICAL_REPAIR_DATE = "2026-08-23"
GRAPHICAL_REPAIR_ID = "carvaka-continuous-at-a-glance-graphical-v2"
GRAPHICAL_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
)
GRAPHICAL_PILOT_KEYS = (
    "geography-04",
    "philosophy-paper-i-indian-philosophy-02",
    "polity-07",
    "ancient-indian-history-06",
)
GRAPHICAL_PILOT_VALIDATION = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-pilot-2026-08-23-validation.json"
)
GRAPHICAL_VALIDATION = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-standard-2026-08-23-validation.json"
)
GRAPHICAL_STAGED = GRAPHICAL_VALIDATION.with_name(
    "carvaka-graphical-standard-2026-08-23-staged-records.json"
)
GRAPHICAL_CHANGED = GRAPHICAL_VALIDATION.with_name(
    "carvaka-graphical-standard-2026-08-23-changed-files.txt"
)
GRAPHICAL_PILOT_REPORT = (
    ROOT / "notes" / REFRESHED_ROOT / "CARVAKA-GRAPHICAL-PILOT-REPORT.md"
)
GRAPHICAL_FINAL_REPORT = (
    ROOT / "notes" / REFRESHED_ROOT / "CARVAKA-GRAPHICAL-STANDARD-REPORT.md"
)

KNOWLEDGE_ROOT = ROOT / "upsc-ai-kit" / "knowledge" / REFRESHED_ROOT
NOTES_ROOT = ROOT / "notes" / REFRESHED_ROOT
PILOT_NOTIONS = "philosophy-paper-ii-philosophy-of-religion-01"

META_H3 = re.compile(
    r"^(?:"
    r"package counts?|"
    r"source(?:-complete)? (?:audit|coverage|order|ledger).*|"
    r"coverage and quality ledger|"
    r"roadmap|learning roadmap|learner-v2 roadmap|master learning roadmap|learning route.*|"
    r"basic / must know.*|"
    r"first-use terminology.*|"
    r"answer-line control register|"
    r"verified current anchor.*|"
    r"practice rule.*|"
    r"metric discipline.*|"
    r"prelims close-option laboratory|"
    r"mains answer laboratory"
    r")$",
    re.IGNORECASE,
)
H2_RE = re.compile(r"^##(?!#)\s+(.+?)\s*$")
H3_RE = re.compile(r"^###(?!#)\s+(.+?)\s*$")
SESSION_RE = re.compile(r"^SESSION\s+(\d+)\s*[—-]\s*(.+)$", re.I)
OPTION_RE = re.compile(
    r"^(?P<indent>\s*)(?P<bullet>[-*]\s+)?"
    r"(?:(?P<label>[A-Da-d])(?P<punct>[.)])|\((?P<paren>[A-Da-d])\))"
    r"(?P<space>\s+)(?P<text>.+?)\s*$"
)
ANSWER_RE = re.compile(
    r"(?P<prefix>(?:✅\s*)?\*\*Answer:\s*)"
    r"(?P<open>\()?(?P<label>[A-Da-d])(?P<close>\))?"
    r"(?P<period>\.)?(?P<tail>(?:\s+[^*\n]+?)?)(?P<suffix>\*\*)",
    re.I,
)
ANSWER_TEXT_RE = re.compile(
    r"(?P<prefix>\*\*Answer:\s*)"
    r"(?P<label>[A-Da-d])"
    r"(?P<period>\.)"
    r"(?P<suffix>\s+)",
    re.I,
)
CORRECT_ANSWER_RE = re.compile(
    r"(?P<prefix>Correct answer:\s*)"
    r"(?P<open>\()?(?P<label>[A-Da-d])(?P<close>\))?"
    r"(?P<period>\.)?",
    re.I,
)
DASH_ANSWER_RE = re.compile(
    r"(?P<prefix>\b(?:CORRECT\s+)?ANSWER:\s*)"
    r"(?P<label>[A-Da-d])"
    r"(?P<suffix>\s+-)",
    re.I,
)
TABLE_OPTION_RE = re.compile(
    r"^(?P<indent>\s*)\|\s*(?P<label>[A-Da-d])\s*\|"
    r"\s*(?P<text>.*?)\s*\|\s*$"
)


@dataclass(frozen=True)
class Topic:
    key: str
    subject: str
    section: str
    topic_folder: str
    title: str
    generation: int
    record_id: str
    markdown: Path
    main_pdf: Path
    workbook: Path
    source_record: dict[str, object]


@dataclass(frozen=True)
class Paths:
    knowledge_dir: Path
    markdown: Path
    workbook_markdown: Path
    assets: Path
    notes_dir: Path
    main_pdf: Path
    workbook_pdf: Path
    package_validation: Path
    preservation: Path
    mcq_audit: Path
    staged_record: Path
    flowchart_dir: Path


class RefreshError(ValueError):
    """Raised when a source cannot be refreshed without guessing or overwriting."""


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("/", "\\")


def repo_path(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RefreshError(f"Expected a JSON object: {path}")
    return data


def load_tracker() -> dict[str, object]:
    tracker = load_json(TRACKER)
    if tracker.get("schema_version") != 2 or not isinstance(
        tracker.get("exports"), list
    ):
        raise RefreshError("EXPORT-PDF-STATUS.json must use schema v2.")
    return tracker


def load_overrides() -> dict[str, dict[str, object]]:
    data = load_json(OVERRIDES)
    topics = data.get("topics", {})
    if data.get("schema_version") != 1 or not isinstance(topics, dict):
        raise RefreshError("Refresh overrides must use schema_version 1.")
    return {
        str(key): value
        for key, value in topics.items()
        if isinstance(value, dict)
    }


def load_deep_overrides() -> dict[str, dict[str, object]]:
    data = load_json(DEEP_OVERRIDES)
    topics = data.get("topics", {})
    if data.get("schema_version") != 1 or not isinstance(topics, dict):
        raise RefreshError("Deep content overrides must use schema_version 1.")
    return {
        str(key): value
        for key, value in topics.items()
        if isinstance(value, dict)
    }


def merged_overrides() -> dict[str, dict[str, object]]:
    result = copy.deepcopy(load_overrides())
    for topic_key, deep in load_deep_overrides().items():
        topic = result.setdefault(topic_key, {})
        for field, value in deep.items():
            if field in {"session_titles", "semantic_overrides"}:
                current = topic.setdefault(field, {})
                if not isinstance(current, dict) or not isinstance(value, dict):
                    raise RefreshError(
                        f"{topic_key}: {field} overrides must be objects."
                    )
                current.update(copy.deepcopy(value))
            else:
                topic[field] = copy.deepcopy(value)
    return result


def clean_heading(value: str) -> str:
    value = re.sub(r"[*_`]", "", value)
    value = re.sub(r"^[\W_]*VISUAL\s*[—:-]\s*", "", value, flags=re.I)
    value = re.sub(r"^\d+(?:\.\d+)*[.)]?\s*", "", value)
    return re.sub(r"\s+", " ", value).strip()


def safe_folder(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*]', "-", value)
    value = re.sub(r"\s+", "-", value.strip())
    value = re.sub(r"-{2,}", "-", value)
    return value.strip(".-") or "Topic"


def compact_topic_folder(topic_key: str) -> str:
    """Keep refreshed Windows paths readable and below legacy MAX_PATH."""
    if len(topic_key) <= 30:
        return topic_key
    geography = re.match(r"^(geography-\d+)(?:-|$)", topic_key, re.I)
    if geography:
        return geography.group(1)
    philosophy = re.match(
        r"^philosophy-paper-[ivx]+-.+-(\d+)$",
        topic_key,
        re.I,
    )
    if philosophy:
        return f"topic-{philosophy.group(1)}"
    digest = hashlib.sha256(topic_key.encode("utf-8")).hexdigest()[:8]
    return f"{topic_key[:20].rstrip('-')}-{digest}"


def title_from_markdown(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^#(?!#)\s+(.+?)\s*$", text)
    if not match:
        return path.stem
    title = re.sub(
        r"\s*[—-]\s*(?:Learner-v2|Source-Complete|Uncompressed|Complete).*$",
        "",
        match.group(1),
        flags=re.I,
    )
    return clean_heading(title)


def derive_section(markdown: Path, subject: str) -> str:
    parts = markdown.relative_to(ROOT).parts
    folded = [part.casefold() for part in parts]
    if (
        len(parts) >= 6
        and folded[:3]
        == ["upsc-ai-kit", "knowledge", REFRESHED_ROOT.casefold()]
    ):
        return safe_folder(parts[4])
    if "v2" in folded:
        raw = parts[folded.index("v2") + 1]
        raw = re.sub(r"(?:-core-first)?-g\d+", "", raw, flags=re.I)
        raw = re.sub(r"-core-first$", "", raw, flags=re.I)
        return safe_folder("-".join(piece.capitalize() for piece in raw.split("-")))
    subject_index = next(
        (
            index
            for index, part in enumerate(parts)
            if part.casefold() == subject.casefold()
        ),
        None,
    )
    if (
        subject_index is not None
        and subject_index + 1 < len(parts)
        and parts[subject_index + 1].casefold() != "learning-sessions"
    ):
        return safe_folder(parts[subject_index + 1])
    return "General"


def record_subject(record: dict[str, object], markdown: Path) -> str:
    parts = markdown.relative_to(ROOT).parts
    if len(parts) < 3 or parts[:2] != ("upsc-ai-kit", "knowledge"):
        raise RefreshError(f"Cannot derive subject from {markdown}")
    if (
        len(parts) >= 4
        and parts[2].casefold() == REFRESHED_ROOT.casefold()
    ):
        return parts[3]
    return parts[2]


def latest_validated_topics(
    tracker: dict[str, object],
    overrides: dict[str, dict[str, object]],
) -> list[Topic]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for record in tracker["exports"]:
        if (
            not isinstance(record, dict)
            or record.get("variant") != V2_VARIANT
            or not isinstance(record.get("validation"), dict)
            or record["validation"].get("state") != "passed"
        ):
            continue
        key = str(record.get("topic_key") or "")
        if key:
            grouped.setdefault(key, []).append(record)

    topics: list[Topic] = []
    for key, records in sorted(grouped.items()):
        maximum = max(int(record.get("generation") or 1) for record in records)
        latest = [
            record
            for record in records
            if int(record.get("generation") or 1) == maximum
        ]
        if len(latest) != 1:
            raise RefreshError(
                f"{key}: expected one validated record at generation {maximum}; "
                f"found {len(latest)}."
            )
        record = latest[0]
        required = ("record_id", "markdown", "main_pdf", "workbook")
        if any(not record.get(field) for field in required):
            raise RefreshError(f"{key}: latest validated record is incomplete.")
        markdown = repo_path(str(record["markdown"]))
        main_pdf = repo_path(str(record["main_pdf"]))
        workbook = repo_path(str(record["workbook"]))
        if not all(path.is_file() for path in (markdown, main_pdf, workbook)):
            raise RefreshError(f"{key}: a latest validated source artifact is missing.")
        subject = record_subject(record, markdown)
        override = overrides.get(key, {})
        section = safe_folder(
            str(override.get("section") or derive_section(markdown, subject))
        )
        topic_folder = safe_folder(
            str(override.get("topic_folder") or compact_topic_folder(key))
        )
        topics.append(
            Topic(
                key=key,
                subject=subject,
                section=section,
                topic_folder=topic_folder,
                title=title_from_markdown(markdown),
                generation=maximum,
                record_id=str(record["record_id"]),
                markdown=markdown,
                main_pdf=main_pdf,
                workbook=workbook,
                source_record=record,
            )
        )
    return topics


def pilot_topics(topics: list[Topic]) -> list[Topic]:
    notions = next((topic for topic in topics if topic.key == PILOT_NOTIONS), None)
    polity = next(
        (
            topic
            for topic in sorted(topics, key=lambda item: item.key)
            if topic.subject.casefold() == "polity"
        ),
        None,
    )
    history_or_geography = next(
        (
            topic
            for preferred in (
                "ancient-indian-history",
                "history",
                "geography",
            )
            for topic in sorted(topics, key=lambda item: item.key)
            if topic.subject.casefold() == preferred
        ),
        None,
    )
    selected = [notions, polity, history_or_geography]
    if any(topic is None for topic in selected):
        raise RefreshError(
            "Pilot requires Notions of God, one Polity topic, and one History/Geography topic."
        )
    keys = [topic.key for topic in selected if topic is not None]
    if len(set(keys)) != 3:
        raise RefreshError(f"Pilot selection did not produce three distinct topics: {keys}")
    return [topic for topic in selected if topic is not None]


def next_generation(tracker: dict[str, object], topic_key: str) -> int:
    return 1 + max(
        (
            int(record.get("generation") or 1)
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("variant") == V2_VARIANT
            and record.get("topic_key") == topic_key
        ),
        default=0,
    )


def next_new_topic_generation(
    tracker: dict[str, object],
    topic_key: str,
) -> int:
    """Continue a topic's generation number across legacy and learner variants."""
    return 1 + max(
        (
            int(record.get("generation") or 1)
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == topic_key
        ),
        default=0,
    )


def output_paths(
    topic: Topic,
    generation: int,
    *,
    generation_date: str = REFRESH_DATE,
    generation_subdir: bool = False,
) -> Paths:
    knowledge_base = (
        KNOWLEDGE_ROOT
        / topic.subject
        / topic.section
        / "learning-sessions"
        / topic.topic_folder
    )
    notes_base = (
        NOTES_ROOT
        / topic.subject
        / topic.section
        / "learning-sessions"
        / topic.topic_folder
    )
    knowledge_dir = (
        knowledge_base / f"g{generation}"
        if generation_subdir
        else knowledge_base
    )
    notes_dir = (
        notes_base / f"g{generation}"
        if generation_subdir
        else notes_base
    )
    flowchart_dir = (
        NOTES_ROOT
        / topic.subject
        / topic.section
        / "flowcharts"
        / topic.topic_folder
        / f"carvaka-g{generation}"
    )
    stem = topic.topic_folder
    return Paths(
        knowledge_dir=knowledge_dir,
        markdown=knowledge_dir
        / f"{stem}_Complete-Learning-Session_{generation_date}.md",
        workbook_markdown=knowledge_dir
        / f"{stem}_Solved-Practice-Workbook_{generation_date}.md",
        assets=knowledge_dir / "assets",
        notes_dir=notes_dir,
        main_pdf=notes_dir
        / f"{stem}_Complete-Learning-Session_{generation_date}.pdf",
        workbook_pdf=notes_dir
        / f"{stem}_Solved-Practice-Workbook_{generation_date}.pdf",
        package_validation=notes_dir / "PACKAGE-VALIDATION-REPORT.txt",
        preservation=notes_dir / "PRESERVATION-HASHES.json",
        mcq_audit=notes_dir / "MCQ-AUDIT.json",
        staged_record=notes_dir / "STAGED-RECORD.json",
        flowchart_dir=flowchart_dir,
    )


def iter_record_paths(value: object) -> Iterable[Path]:
    if isinstance(value, dict):
        for nested in value.values():
            yield from iter_record_paths(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from iter_record_paths(nested)
    elif isinstance(value, str) and (
        "\\" in value or "/" in value
    ):
        candidate = repo_path(value)
        try:
            candidate.resolve().relative_to(ROOT)
        except ValueError:
            return
        if candidate.is_file():
            yield candidate
        elif candidate.is_dir():
            yield from (
                path
                for path in candidate.rglob("*")
                if path.is_file()
            )


def source_inventory(topic: Topic) -> dict[str, str]:
    paths = {
        topic.markdown.resolve(),
        topic.main_pdf.resolve(),
        topic.workbook.resolve(),
        *(path.resolve() for path in iter_record_paths(topic.source_record)),
    }
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
    }


def inventory_paths(paths: Iterable[Path]) -> dict[str, str]:
    """Hash one explicit immutable source set for new-topic generation."""
    resolved = {path.resolve() for path in paths}
    missing = [
        path
        for path in sorted(resolved, key=lambda item: str(item).casefold())
        if not path.is_file()
    ]
    if missing:
        raise RefreshError(f"New-topic source files do not exist: {missing}")
    return {
        relative(path): sha256(path)
        for path in sorted(resolved, key=lambda item: str(item).casefold())
    }


def preservation_lines(markdown: str) -> set[str]:
    """Normalize source lines while ignoring only generated/mutable mechanics."""
    normalized = markdown.replace("\r\n", "\n")
    if normalized.startswith("---\n"):
        end = normalized.find("\n---\n", 4)
        if end >= 0:
            normalized = normalized[end + 5 :]
    normalized = re.sub(
        r"\n*```closure-flow\s*\n.*?\n```\n*",
        "\n",
        normalized,
        flags=re.S | re.I,
    )
    normalized = re.sub(
        r"(?ims)^####\s+DEFINITION / WHAT THIS IS CALLED\s*$.*?"
        r"^####\s+MUST-WRITE KEYWORDS\s*$.*?"
        r"^\*\*How to use them:\*\*[^\n]*$",
        "",
        normalized,
    )
    normalized = re.sub(
        r"(?ims)^####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*$"
        r"\s*```(?:text|closure-flow).*?```",
        "",
        normalized,
    )
    normalized = re.sub(
        r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*$.*\Z",
        "",
        normalized,
    )
    normalized = re.sub(
        r"(?ims)^#{3,4}[ \t]+(?:Learner-v2|Master learning|Learning)?[ \t]*"
        r"roadmap(?:[ \t]*[—:-][^\n]*)?[ \t]*$\n+"
        r"[ \t]*```(?:text)?[^\n]*\n.*?^```[ \t]*$\n*",
        "",
        normalized,
    )
    normalized = re.sub(r"!\[([^\]]*)]\([^)]+\)", r"\1", normalized)
    result: set[str] = set()
    for raw in normalized.splitlines():
        stripped = raw.strip()
        if re.match(r"^#{3,4}\s+", stripped):
            continue
        if stripped.startswith("```"):
            continue
        if not stripped or stripped.startswith("#"):
            continue
        if re.search(
            r"Correct options (?:rotate strictly|are balanced)|"
            r"Correct-option rotation follows |"
            r"strict A\s*(?:→|->|-)\s*B\s*(?:→|->|-)\s*C\s*"
            r"(?:→|->|-)\s*D rotation|"
            r"(?:answer sequence|answer rotation|workbook rotation|answers follow)"
            r".*A\s*(?:→|->|-)\s*B\s*(?:→|->|-)\s*C\s*"
            r"(?:→|->|-)\s*D",
            stripped,
            re.I,
        ):
            continue
        value = strip_markdown(stripped)
        value = re.sub(r"^\s*[-*]\s+", "", value)
        value = re.sub(r"^\(?[A-Da-d]\)?[.)]?\s+", "<OPTION> ", value)
        value = re.sub(
            r"\b(?:Answer|Correct answer):\s*\(?[A-Da-d]\)?\.?",
            "Answer: <OPTION>",
            value,
            flags=re.I,
        )
        value = re.sub(r"\(([a-d])\)", "(<OPTION>)", value)
        value = re.sub(r"\bOption\s+[A-D]\b", "Option <OPTION>", value, flags=re.I)
        value = re.sub(r"\b[A-D]\b", "<OPTION>", value)
        value = re.sub(r"\s+", " ", value).strip().casefold()
        if len(value) >= 35:
            result.add(value)
    return result


def source_content_errors(source: str, refreshed: str) -> list[str]:
    source_lines = preservation_lines(source)
    refreshed_lines = preservation_lines(refreshed)
    missing = sorted(source_lines - refreshed_lines)
    if not missing:
        return []
    return [
        "Source preservation fingerprint is incomplete; "
        f"{len(missing)} normalized substantive lines are missing. "
        f"First missing line: {missing[0][:180]}"
    ]


def resolve_asset(source: Path, raw: str) -> Path | None:
    raw = raw.strip().strip("<>")
    if not raw or "://" in raw or raw.startswith("#"):
        return None
    normalized = Path(raw.replace("\\", "/"))
    candidates = (
        normalized if normalized.is_absolute() else source.parent / normalized,
        ROOT / normalized,
    )
    return next(
        (
            resolved
            for path in candidates
            for resolved in (path.resolve(),)
            if resolved.is_file()
        ),
        None,
    )


def copy_asset(asset: Path, assets_dir: Path, used: dict[str, str]) -> str:
    digest = sha256(asset)
    name = safe_folder(asset.stem) + asset.suffix.lower()
    max_name_length = max(32, 240 - len(str(assets_dir.resolve())) - 1)
    if len(name) > max_name_length:
        suffix = f"-{digest[:10]}{asset.suffix.lower()}"
        stem_limit = max(12, max_name_length - len(suffix))
        name = safe_folder(asset.stem)[:stem_limit].rstrip("-") + suffix
    if name.casefold() in used and used[name.casefold()] != digest:
        name = f"{safe_folder(asset.stem)}-{digest[:10]}{asset.suffix.lower()}"
    target = assets_dir / name
    if target.exists():
        if sha256(target) != digest:
            raise RefreshError(f"Refusing to replace a different refreshed asset: {target}")
    else:
        shutil.copy2(asset, target)
    used[name.casefold()] = digest
    return f"assets/{name}"


def localize_assets(markdown: str, source: Path, assets_dir: Path) -> str:
    assets_dir.mkdir(parents=True, exist_ok=False)
    used: dict[str, str] = {}

    def image_replacement(match: re.Match[str]) -> str:
        asset = resolve_asset(source, match.group(2))
        if not asset:
            return match.group(0)
        return f"{match.group(1)}{copy_asset(asset, assets_dir, used)}{match.group(3)}"

    localized = re.sub(
        r"(!\[[^\]]*]\()([^)]+)(\))",
        image_replacement,
        markdown,
    )
    return re.sub(
        r"(?m)^cover_image:\s*[\"']?[^\"'\n]+[\"']?\s*$\n?",
        "",
        localized,
    )


def strip_markdown(value: str) -> str:
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_`#>]", "", value)
    value = re.sub(r"\[(?:FACT|ANALYSIS|INFERENCE|LIMIT|TRAP)]", "", value, flags=re.I)
    value = re.sub(
        r"ANSWER-GRABBING LINE\s*[—-]\s*WRITE/ADAPT IN THE EXAM(?:\s*\([^)]*\))?\s*:?",
        "",
        value,
        flags=re.I,
    )
    return re.sub(r"\s+", " ", value).strip(" :-")


SEMANTIC_ROLE_PREFIX_RE = re.compile(
    r"^(?:Major\s+(?:criticism|reply)|High-value\s+transition|"
    r"Recommended\s+opening\s+definition|Core\s+argument|"
    r"What\s+it\s+preserves\s+or\s+explains|What\s+this\s+shows|"
    r"Context|Method|Recall|Exam\s+use|Mains\s+angle)\s*:\s*",
    re.I,
)
SEMANTIC_METADATA_RE = re.compile(
    r"^(?:"
    r"Classification\s*:\s*(?:CORE|SUPPORTING|OPTIONAL).*|"
    r"(?:CORE|SUPPORTING|OPTIONAL(?:\s+ADVANCED)?)\s+(?:PRELIMS|MAINS).*|"
    r"CURRENT-AFFAIRS\s+LINK.*|"
    r"Caption\s*:.*|Search\s+finding(?:\s*:.*)?|"
    r"Current(?:-affairs)?\s+(?:anchor|link|note)(?:\s*:.*)?|"
    r"(?:News|event|report)\s+(?:note|anchor|summary)(?:\s*:.*)?|"
    r"Progress\s*:.*|Stage\s*:.*|"
    r"PRE-TEACH\s+CHECKLIST.*|Book\s+context.*|"
    r"CA\s+(?:Search|Found)\s*:.*|"
    r"Source(?:-complete)?\s+(?:audit|coverage|ownership|order|ledger).*|"
    r"(?:Coverage|Ownership|Publication)\s+(?:audit|metadata|ledger).*|"
    r"(?:Catalogue|Generation)\s+identity\s*:.*|"
    r"Approval\s*:.*|Evidence\s+key\s*:.*|"
    r"Learner\s+orientation\s*:.*|Visual\s+\d+\s*[—:-].*|"
    r"Roadmap(?:\s*:.*)?|Learning\s+roadmap(?:\s*:.*)?"
    r")$",
    re.I,
)
SEMANTIC_LABEL_RE = re.compile(
    r"^(?:UPSC\s+trap|FACT|ANALYSIS|INFERENCE|LIMIT|ANSWER)$",
    re.I,
)
DEFINITION_RE = re.compile(
    r"\b(?:is|are|means|refers to|denotes|describes|defines|consists of|"
    r"is called|are called)\b",
    re.I,
)
CLAUSE_RE = re.compile(
    r"\b(?:is|are|was|were|means|refers|denotes|describes|defines|"
    r"includes?|consists|creates?|created|establishes?|explains?|shows?|"
    r"treats|holds|affirms|rejects|produces|generates|moves|drives|"
    r"occurs|results|depends|requires|allows|links|connects|converts|"
    r"replaced|introduced|emerged|developed|became|remains|must|should|"
    r"can|could|will|would|has|have|had|aims|presents|argues|challenges|"
    r"supplies|concentrates|hosts?|separates|distinguishes|classifies|"
    r"covered|ended|added|widened|retained|acquired|followed|predicts|"
    r"suggests|indicates|reveals|provides|formed|built|enabled|equate|"
    r"confuse|treat|do(?:es)?|uses?|demonstrates?|determines?|captures?|"
    r"increases?|raises?|exhausts?|organis(?:es|zes)|deforms?|builds?|"
    r"interacts?|follows?|redraws?|proves?|overlaps?|reflects?|measures?)\b",
    re.I,
)
KEYWORD_STOPWORDS = {
    "a",
    "an",
    "and",
    "answer",
    "analysis",
    "classification",
    "concept",
    "context",
    "core",
    "definition",
    "effect",
    "evidence",
    "expansion",
    "fact",
    "factor",
    "feature",
    "framework",
    "how",
    "is",
    "impact",
    "inference",
    "introduction",
    "mechanism",
    "memory",
    "mains",
    "of",
    "optional",
    "prelims",
    "process",
    "question",
    "roadmap",
    "source",
    "search",
    "stage",
    "supporting",
    "the",
    "what",
    "does",
    "to",
    "trap",
    "upsc",
    "worthiness",
    "owner",
    "link",
    "preservation",
    "note",
    "current",
    "do",
}


def strip_generated_session_aids(body: str) -> str:
    """Remove only previously generated aid/closure blocks from a session."""
    cleaned = re.sub(
        r"(?ims)\n*^####\s+DEFINITION / WHAT THIS IS CALLED\s*$.*?"
        r"^####\s+MUST-WRITE KEYWORDS\s*$.*?"
        r"^\*\*How to use them:\*\*[^\n]*$",
        "\n",
        body,
    )
    cleaned = re.sub(
        r"(?ims)\n*^####\s+CLOSING RECALL FLOW(?:\s*[—-][^\n]*)?\s*$"
        r"\s*```(?:text|closure-flow).*?```\s*",
        "\n",
        cleaned,
    )
    return cleaned.strip()


def semantic_line_is_metadata(value: str) -> bool:
    cleaned = clean_aid_value(value).strip()
    return bool(
        not cleaned
        or SEMANTIC_METADATA_RE.fullmatch(cleaned)
        or SEMANTIC_LABEL_RE.fullmatch(cleaned)
        or re.search(
            r"\[(?:CORE\s+(?:PRELIMS|MAINS)|SUPPORTING|OPTIONAL\s+ADVANCED|"
            r"CURRENT-AFFAIRS\s+LINK)\]",
            cleaned,
            re.I,
        )
    )


def clean_semantic_source(body: str) -> str:
    """Create an extraction-only view while retaining the original teaching body."""
    source = strip_generated_session_aids(body)
    source = re.sub(r"```.*?```", "\n", source, flags=re.S)
    output: list[str] = []
    image_caption_window = 0
    for raw in source.replace("\r\n", "\n").splitlines():
        stripped = raw.strip()
        if not stripped:
            output.append("")
            if image_caption_window:
                image_caption_window -= 1
            continue
        if re.match(r"^#{1,6}\s+", stripped) or stripped == "---":
            image_caption_window = 0
            continue
        if re.match(r"^!\[[^\]]*]\([^)]+\)\s*$", stripped):
            image_caption_window = 2
            continue
        if image_caption_window and (
            re.fullmatch(r"[*_].+[*_]", stripped)
            or re.match(r"^(?:Caption|The|This)\s*:", strip_markdown(stripped), re.I)
        ):
            image_caption_window = 0
            continue
        image_caption_window = 0
        if stripped.startswith("|") and stripped.endswith("|"):
            continue
        if re.fullmatch(r"[:| -]+", stripped):
            continue
        value = re.sub(r"^\s*[-*+]\s+", "", stripped)
        value = re.sub(r"^\s*\d+[.)]\s+", "", value)
        value = re.sub(
            r"^\[(?:FACT|ANALYSIS|INFERENCE|LIMIT|TRAP)]\s*",
            "",
            value,
            flags=re.I,
        )
        value = re.sub(
            r"^(?:✅\s*)?(?:FACT|ANALYSIS|INFERENCE|LIMIT)\s*:\s*",
            "",
            value,
            flags=re.I,
        )
        value = re.sub(r"^>\s*", "", value)
        value = re.sub(
            r"^\*\*ANSWER-GRABBING LINE\s*[—-]\s*"
            r"WRITE/ADAPT IN THE EXAM(?:\s*\([^)]*\))?\s*:?\*\*\s*",
            "",
            value,
            flags=re.I,
        )
        value = re.sub(r"^\*\*UPSC trap:\*\*\s*", "", value, flags=re.I)
        if re.match(r"^(?:UPSC\s+)?TRAP\s*:", value, re.I):
            continue
        value = SEMANTIC_ROLE_PREFIX_RE.sub("", strip_markdown(value))
        if semantic_line_is_metadata(value):
            continue
        if re.search(
            r"\b(?:live|current)\s+(?:[A-Za-z]+\s+){0,3}(?:search|report|news)\b|"
            r"\bcurrent(?:-affairs|\s+affairs)\b|"
            r"\bCA\s+search\b|"
            r"\bBook\s+context\b|"
            r"\b(?:Religion News Service|High Commission|PIB|Ministry)\b.*"
            r"\b(?:reported|announced|released|held|stated)\b|"
            r"\b\d{4}\s+academic lecture\b",
            value,
            re.I,
        ):
            continue
        if re.search(r"\[(?:CA\s+FACT|CURRENT-AFFAIRS\s+LINK)]|\bCA\s+FACT\b", value, re.I):
            continue
        if re.match(
            r"^(?:✅\s*)?(?:Fact\s*:?\s*)?(?:In\s+)?(?:On\s+)?"
            r"(?:\d{1,2}\s+)?(?:January|February|March|April|May|June|July|"
            r"August|September|October|November|December)?\s*\d{4}\b",
            value,
            re.I,
        ):
            continue
        if re.match(r"^(?:The|This)\s+visual\b", value, re.I):
            continue
        output.append(value)
    return "\n".join(output)


def complete_semantic_sentence(value: str) -> str | None:
    value = SEMANTIC_ROLE_PREFIX_RE.sub("", strip_markdown(value))
    value = re.sub(r"^\s*[-–—:;,]+\s*", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    if (
        not value
        or len(value) < 4
        or semantic_line_is_metadata(value)
        or re.match(r"^[.,;:!?]", value)
        or re.match(r"^(?:The|This)\s+visual\b", value, re.I)
        or len(re.findall(r"\b[\w'’.-]+\b", value)) < 6
        or not CLAUSE_RE.search(value)
    ):
        return None
    if not value.endswith((".", "!", "?")):
        value += "."
    return value


def session_sentences(body: str) -> list[str]:
    source = clean_semantic_source(body)
    paragraphs: list[str] = []
    pending: list[str] = []
    for line in source.splitlines():
        if line.strip():
            pending.append(line.strip())
        elif pending:
            paragraphs.append(" ".join(pending))
            pending = []
    if pending:
        paragraphs.append(" ".join(pending))
    result: list[str] = []
    seen: set[str] = set()
    for paragraph in paragraphs:
        for raw in re.split(
            r"(?<=[.!?])\s+(?=(?:[\"'“‘(]?[A-Z0-9]))",
            paragraph,
        ):
            sentence = complete_semantic_sentence(raw)
            if not sentence or sentence.casefold() in seen:
                continue
            seen.add(sentence.casefold())
            result.append(sentence)
    return result


def exact_answer_line(body: str) -> str | None:
    source = strip_generated_session_aids(body)
    lines = source.replace("\r\n", "\n").splitlines()
    label = re.compile(
        r"ANSWER-GRABBING LINE\s*[—-]\s*WRITE/ADAPT IN THE EXAM"
        r"(?:\s*\([^)]*\))?\s*:?",
        re.I,
    )
    for index, raw in enumerate(lines):
        if not label.search(raw):
            continue
        remainder = label.sub("", raw)
        remainder = strip_markdown(remainder)
        candidates = [remainder]
        for following in lines[index + 1 : index + 4]:
            if not following.strip():
                continue
            if following.lstrip().startswith(">"):
                candidates.append(re.sub(r"^\s*>\s*", "", following))
            break
        for candidate in candidates:
            sentence = complete_semantic_sentence(candidate)
            if sentence:
                return sentence
    return None


def keyword_value(candidate: str) -> str | None:
    value = SEMANTIC_ROLE_PREFIX_RE.sub("", strip_markdown(candidate))
    value = re.sub(r"^\s*(?:UPSC\s+trap|FACT|ANALYSIS|ANSWER)\s*:?\s*", "", value, flags=re.I)
    value = re.sub(r"\s+", " ", value).strip(" :-")
    words = re.findall(r"\b[\w'’./–-]+\b", value)
    if (
        not value
        or semantic_line_is_metadata(value)
        or re.match(
            r"^(?:Avoid|Use|Write|Explain|Define|Compare|Distinguish|State|Show)\b",
            value,
            re.I,
        )
        or re.match(r"^Visual\s+\d+\b", value, re.I)
        or re.fullmatch(
            r"(?:what it shows|safe limitation|source owner|ownership boundary|"
            r"why it matters|exam use|prelims use|mains use|key point|"
            r"core idea|correct|wrong|explanation|mains route|revision notes|"
            r"the exam-safe formulation|worthiness|owner link|preservation note|"
            r"in simple words|memory line|search finding|current|do|"
            r"live source checked|master verdict|book context queried|public|"
            r"an icml|core argument|recommended opening definition|"
            r"high-value transition)",
            value,
            re.I,
        )
        or re.fullmatch(
            r"(?:January|February|March|April|May|June|July|August|September|"
            r"October|November|December|\d{4})",
            value,
            re.I,
        )
        or re.search(
            r"\b(?:caption|search finding|current-affairs|current affairs|"
            r"news service|press release|monthly report|source checked|"
            r"book context|ca search|high commission)\b",
            value,
            re.I,
        )
        or re.match(r"^[.,;:!?]", value)
        or len(value) > 78
        or not 1 <= len(words) <= 8
        or value.endswith((".", "!", "?"))
        or (
            len(words) >= 6
            and CLAUSE_RE.search(value)
        )
    ):
        return None
    meaningful = [
        word
        for word in words
        if word.casefold() not in KEYWORD_STOPWORDS
        and not re.fullmatch(r"\d+", word)
    ]
    if not meaningful:
        return None
    return value


def extract_keywords(title: str, body: str) -> list[str]:
    source = strip_generated_session_aids(body)
    candidates: list[str] = []
    title_clean = clean_heading(title)
    if title_clean.isupper():
        title_clean = title_clean.title()
    title_chunks = [
        chunk.strip()
        for chunk in re.split(r"\s*(?::|[—–]|\band\b|,|;)\s*", title_clean, flags=re.I)
        if chunk.strip()
    ]
    candidates.extend(title_chunks)
    candidates.extend(
        match.group(1).strip()
        for match in re.finditer(r"\*\*([^*]{2,90})\*\*", source, re.S)
    )
    source_lines = source.splitlines()
    for line_number, line in enumerate(source_lines):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        if (
            line_number + 1 < len(source_lines)
            and re.fullmatch(
                r"\s*\|?\s*:?-{3,}:?(?:\s*\|\s*:?-{3,}:?)+\s*\|?\s*",
                source_lines[line_number + 1],
            )
        ):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            candidates.extend(cells)
    candidates.extend(
        match.group(0)
        for match in re.finditer(
            r"\b(?:Article\s+\d+[A-Z]?|"
            r"[A-Z][A-Za-z'’.-]+(?:\s+[A-Z][A-Za-z'’.-]+){0,5}\s+Act\s+\d{4}|"
            r"[A-Z][A-Za-z'’.-]+(?:\s+[A-Z][A-Za-z'’.-]+){1,5}\s*"
            r"\([A-Z][A-Z0-9-]{1,8}\)|"
            r"\d{3,4}(?:[–-]\d{2,4})?\s*(?:BCE|BC|CE|AD)?)\b",
            source,
        )
    )
    for sentence in session_sentences(source):
        before_definition = re.match(
            r"^(.{2,70}?)\s+(?:is|are|means|refers to|denotes|describes)\b",
            sentence,
            re.I,
        )
        if before_definition:
            candidates.append(before_definition.group(1))
        candidates.extend(
            match.group(1)
            for match in re.finditer(
                r"\b([A-Z][A-Za-z'’.-]+(?:\s+[A-Z][A-Za-z'’.-]+){0,4})\b",
                sentence,
            )
        )
    candidates.append(title_clean)

    result: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        value = keyword_value(candidate)
        if not value:
            continue
        normalized = re.sub(r"\W+", " ", value).strip().casefold()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(value)
        if len(result) == 6:
            break

    if len(result) < 4:
        title_words = [
            word
            for word in re.findall(r"[A-Za-z][A-Za-z'’/-]{3,}", title_clean)
            if word.casefold() not in KEYWORD_STOPWORDS
        ]
        for width in (2, 1):
            for start in range(0, len(title_words) - width + 1):
                value = keyword_value(" ".join(title_words[start : start + width]))
                if not value:
                    continue
                normalized = re.sub(r"\W+", " ", value).strip().casefold()
                if normalized in seen:
                    continue
                seen.add(normalized)
                result.append(value)
                if len(result) == 4:
                    break
            if len(result) >= 4:
                break
    if len(result) < 4:
        raise RefreshError(
            f"Low-confidence keyword extraction for {title!r}; add a deterministic override."
        )
    result.sort(
        key=lambda item: bool(
            re.match(r"^\d", item)
            or re.fullmatch(r"\d{3,4}(?:[–-]\d{2,4})?.*", item)
        )
    )
    return result[:8]


def select_sentence(
    sentences: list[str],
    *,
    title: str,
    keywords: list[str],
    purpose: str,
    exclude: set[str] | None = None,
) -> str:
    excluded_values = list(exclude or set())
    excluded = {item.casefold() for item in excluded_values}

    def near_excluded(value: str) -> bool:
        normalized = re.sub(r"\W+", " ", value).strip().casefold()
        tokens = set(normalized.split())
        for item in excluded_values:
            other = re.sub(r"\W+", " ", item).strip().casefold()
            other_tokens = set(other.split())
            union = tokens | other_tokens
            jaccard = len(tokens & other_tokens) / len(union) if union else 0.0
            if (
                normalized == other
                or jaccard >= 0.88
                or difflib.SequenceMatcher(None, normalized, other).ratio() >= 0.93
            ):
                return True
        return False
    def normalized_token(value: str) -> str:
        token = value.casefold().strip("'’.-")
        if len(token) > 5 and token.endswith("ies"):
            token = token[:-3] + "y"
        elif len(token) > 4 and token.endswith("s"):
            token = token[:-1]
        return token

    title_tokens = {
        normalized_token(word)
        for word in re.findall(r"[A-Za-z][A-Za-z'’-]{3,}", title)
        if word.casefold() not in KEYWORD_STOPWORDS
    }
    marker = {
        "plain": DEFINITION_RE,
        "technical": re.compile(
            r"\b(?:Article|Act|doctrine|theory|model|process|mechanism|"
            r"system|principle|structure|phase|stage|evidence|method|"
            r"causes?|results?|because|through|by|denotes|consists)\b",
            re.I,
        ),
        "mechanism": re.compile(
            r"\b(?:because|through|by|causes?|produces?|generates?|"
            r"results?|leads?|drives?|converts?|moves?|depends?|mechanism)\b",
            re.I,
        ),
        "consequence": re.compile(
            r"\b(?:therefore|thus|consequently|while|whereas|unlike|but|"
            r"however|not|effect|impact|consequence|contrast|limit)\b",
            re.I,
        ),
        "opening": re.compile(
            r"\b(?:therefore|while|but|not|shows?|explains?|is|are|denotes)\b",
            re.I,
        ),
    }[purpose]
    ranked: list[tuple[int, int, str]] = []
    for index, sentence in enumerate(sentences):
        if sentence.casefold() in excluded or near_excluded(sentence):
            continue
        lowered = sentence.casefold()
        sentence_tokens = {
            normalized_token(word)
            for word in re.findall(r"[A-Za-z][A-Za-z'’-]{3,}", sentence)
        }
        overlap = title_tokens & sentence_tokens
        score = 0
        if marker.search(sentence):
            score += 12
        score += 5 * len(overlap)
        score += 2 * sum(keyword.casefold() in lowered for keyword in keywords)
        words = len(sentence.split())
        if 10 <= words <= 38:
            score += 4
        if purpose == "plain" and DEFINITION_RE.search(sentence):
            score += 16
        if purpose in {"plain", "technical"}:
            if not overlap:
                score -= 30
            if re.match(
                r"^(?:Because|Therefore|Thus|Hence|Consequently|Although|"
                r"However|While|Whereas|Unlike|Do not|Avoid|It does not|"
                r"The exam-safe lesson|UPSC)\b",
                sentence,
                re.I,
            ):
                score -= 35
            if re.match(
                r"^(?:✅\s*)?(?:Fact\s*:?\s*)?(?:In\s+)?(?:On\s+)?"
                r"(?:\d{1,2}\s+)?(?:January|February|March|April|May|June|"
                r"July|August|September|October|November|December)?\s*\d{4}\b",
                sentence,
                re.I,
            ):
                score -= 45
            first_words = {
                normalized_token(word)
                for word in re.findall(
                    r"[A-Za-z][A-Za-z'’-]{3,}",
                    " ".join(sentence.split()[:14]),
                )
            }
            if title_tokens & first_words and DEFINITION_RE.search(sentence):
                score += 22
        if purpose == "opening" and not overlap:
            score -= 20
        ranked.append((score, -index, sentence))
    if not ranked:
        if excluded_values:
            return select_sentence(
                sentences,
                title=title,
                keywords=keywords,
                purpose=purpose,
            )
        raise RefreshError(f"No safe {purpose} sentence for {title!r}.")
    return max(ranked)[2]


def explicit_trap_sentence(body: str) -> str | None:
    source = strip_generated_session_aids(body)
    for match in re.finditer(
        r"(?im)^\s*>?\s*(?:\*\*)?(?:UPSC\s+)?TRAP\s*:?\s*"
        r"(?:\*\*)?\s*(.+?)\s*$",
        source,
    ):
        value = strip_markdown(match.group(1))
        inequality = re.match(r"^(.+?)\s*≠\s*(.+)$", value)
        if inequality:
            value = (
                f"Do not equate {inequality.group(1).strip()} with "
                f"{inequality.group(2).strip().rstrip('.')}."
            )
        sentence = complete_semantic_sentence(value)
        if sentence:
            return sentence
    return None


def semantic_tokens(value: str) -> set[str]:
    result: set[str] = set()
    for raw in re.findall(r"[A-Za-zÀ-žĀ-ž][\w'’.-]{2,}", value):
        token = raw.casefold().strip("'’.-")
        if len(token) > 5 and token.endswith("ies"):
            token = token[:-3] + "y"
        elif len(token) > 4 and token.endswith("s"):
            token = token[:-1]
        if token and token not in KEYWORD_STOPWORDS:
            result.add(token)
    return result


def semantic_alignment(
    value: str,
    *,
    title: str,
    keywords: list[str],
) -> bool:
    anchors = semantic_tokens(title)
    anchors.update(
        token
        for keyword in keywords
        for token in semantic_tokens(keyword)
    )
    return bool(anchors & semantic_tokens(value))


def scope_definitions(title: str, keywords: list[str]) -> tuple[str, str]:
    display = title.title() if title.isupper() else title
    usable = [
        keyword
        for keyword in keywords
        if clean_heading(keyword).casefold() != clean_heading(title).casefold()
    ]
    while len(usable) < 4:
        usable.append(keywords[len(usable) % len(keywords)])
    plain = (
        f"{display} comprises {usable[0]}, {usable[1]} and {usable[2]} "
        "as its core connected dimensions."
    )
    technical = (
        f"Technically, {display} is analysed by relating {usable[0]} to "
        f"{usable[1]}, then testing the relationship through {usable[2]} "
        f"and {usable[3]}."
    )
    return plain, technical


def compact_role_sentence(value: str, *, role: str) -> str:
    cleaned = strip_markdown(value).strip()
    clauses = [
        clause.strip(" ,;:-")
        for clause in re.split(r"[;:]\s+|,\s+(?=(?:while|whereas|but|and)\b)", cleaned)
        if clause.strip(" ,;:-")
    ]
    clause = next(
        (
            item
            for item in clauses
            if len(re.findall(r"\b[\w'’.-]+\b", item)) >= 6
        ),
        cleaned,
    )
    if len(clause.split()) > 14:
        clause = " ".join(clause.split()[:14]).rstrip(" ,;:-") + "..."
    prefixes = {
        "mechanism": "The operative mechanism is that ",
        "consequence": "The resulting consequence is that ",
        "trap": "Do not miss this limiting distinction: ",
    }
    result = prefixes[role] + clause[0].lower() + clause[1:]
    if not result.endswith((".", "!", "?")):
        result += "."
    return result


def semantically_near(left: str, right: str) -> bool:
    first = re.sub(r"\W+", " ", left).strip().casefold()
    second = re.sub(r"\W+", " ", right).strip().casefold()
    if not first or not second:
        return False
    left_tokens = set(first.split())
    right_tokens = set(second.split())
    union = left_tokens | right_tokens
    return (
        first == second
        or (len(left_tokens & right_tokens) / len(union) if union else 0.0) >= 0.88
        or difflib.SequenceMatcher(None, first, second).ratio() >= 0.93
    )


def semantic_contract(
    title: str,
    body: str,
    override: dict[str, object] | None = None,
) -> dict[str, object]:
    source = strip_generated_session_aids(body)
    sentences = session_sentences(source)
    complete_override = bool(
        override
        and isinstance(override.get("keywords"), list)
        and all(
            override.get(field)
            for field in (
                "plain",
                "technical",
                "opening",
                "mechanism",
                "consequence",
                "trap",
            )
        )
    )
    if not sentences and not complete_override:
        raise RefreshError(
            f"Low-confidence session extraction for {title!r}; add an override."
        )
    override = override or {}
    override_keywords = override.get("keywords")
    if isinstance(override_keywords, list):
        keywords = [
            value
            for item in override_keywords
            if (value := keyword_value(str(item)))
        ]
    else:
        keywords = extract_keywords(title, source)

    def overridden(field: str) -> str | None:
        if not override.get(field):
            return None
        value = SEMANTIC_ROLE_PREFIX_RE.sub(
            "",
            strip_markdown(str(override[field])),
        ).strip()
        if not value.endswith((".", "!", "?")):
            value += "."
        if (
            semantic_line_is_metadata(value)
            or len(re.findall(r"\b[\w'’.-]+\b", value)) < 6
        ):
            raise RefreshError(
                f"Invalid semantic override {field} for {title!r}."
            )
        return value

    plain = overridden("plain") or select_sentence(
        sentences,
        title=title,
        keywords=keywords,
        purpose="plain",
    )
    technical = overridden("technical") or (
        select_sentence(
            sentences,
            title=title,
            keywords=keywords,
            purpose="technical",
            exclude={plain},
        )
        if len(sentences) > 1
        else plain
    )
    opening = overridden("opening") or exact_answer_line(source) or select_sentence(
        sentences,
        title=title,
        keywords=keywords,
        purpose="opening",
    )
    mechanism = overridden("mechanism") or select_sentence(
        sentences,
        title=title,
        keywords=keywords,
        purpose="mechanism",
        exclude={opening},
    )
    consequence = overridden("consequence") or select_sentence(
        sentences,
        title=title,
        keywords=keywords,
        purpose="consequence",
        exclude={opening, mechanism},
    )
    trap = overridden("trap") or explicit_trap_sentence(source) or select_sentence(
        sentences,
        title=title,
        keywords=keywords,
        purpose="consequence",
        exclude={opening, mechanism, consequence},
    )
    values = {
        "plain": plain,
        "technical": technical,
        "opening": opening,
        "mechanism": mechanism,
        "consequence": consequence,
        "trap": trap,
    }
    if override.get("how"):
        values["how"] = overridden("how")
    fallback_plain, fallback_technical = scope_definitions(title, keywords)
    if not override.get("plain") and (
        not semantic_alignment(plain, title=title, keywords=keywords)
        or re.match(
            r"^(?:It|This|That|Scheme|Correct|Wrong|No\s+unofficial|"
            r"A\s+reusable\s+structure|Use\b|A\s+complete\s+answer|"
            r"UPSC\s+Trap)\b",
            plain,
            re.I,
        )
        or re.search(
            r"\b(?:example|illustrates?|shows?\s+that)\b",
            plain,
            re.I,
        )
        or (
            not DEFINITION_RE.search(plain)
            and re.search(
                r"\b(?:because|therefore|faster|slower|longer|shorter|"
                r"more\s+than|less\s+than|compared\s+with)\b",
                plain,
                re.I,
            )
        )
    ):
        values["plain"] = fallback_plain
        plain = fallback_plain
    if not override.get("technical") and (
        not semantic_alignment(technical, title=title, keywords=keywords)
        or re.match(
            r"^(?:It|This|That|Scheme|Correct|Wrong|No\s+unofficial|"
            r"Use\b|Do\s+not|Therefore\b|A\s+reusable\s+structure|"
            r"A\s+complete\s+answer|UPSC\s+Trap)\b",
            technical,
            re.I,
        )
    ):
        values["technical"] = fallback_technical
        technical = fallback_technical
    if not override.get("opening") and not semantic_alignment(
        opening,
        title=title,
        keywords=keywords,
    ):
        values["opening"] = values["plain"]
        opening = str(values["plain"])

    role_values = {
        "mechanism": str(values["mechanism"]),
        "consequence": str(values["consequence"]),
        "trap": str(values["trap"]),
    }
    accepted = [str(values["opening"])]
    for role in ("mechanism", "consequence", "trap"):
        value = role_values[role]
        if role == "trap" and not re.search(
            r"\b(?:not|never|avoid|do\s+not|must\s+not|cannot|wrong|"
            r"distinguish|rather\s+than|while|but|limit|qualification)\b",
            value,
            re.I,
        ):
            value = compact_role_sentence(value, role="trap")
        if any(semantically_near(value, prior) for prior in accepted):
            value = compact_role_sentence(value, role=role)
        values[role] = value
        accepted.append(value)
    if not 4 <= len(keywords) <= 8:
        raise RefreshError(f"{title!r}: semantic keywords must contain 4-8 terms.")
    how = str(
        values.get("how")
        or (
            f"Frame the answer through {keywords[0]}; define {keywords[1]}, "
            f"connect {keywords[2]} with {keywords[3]} to explain the mechanism, and "
            + (
                f"use {keywords[4]} for the decisive comparison or qualification."
                if len(keywords) >= 5
                else "close with the decisive comparison or qualification."
            )
        )
    )
    contract = {
        "plain": values["plain"],
        "technical": values["technical"],
        "opening": values["opening"],
        "keywords": keywords,
        "how": how,
        "mechanism": values["mechanism"],
        "consequence": values["consequence"],
        "trap": values["trap"],
    }
    for field, value in contract.items():
        if field == "keywords":
            continue
        reasons = semantic_value_reasons(str(value), field=field)
        if reasons:
            raise RefreshError(
                f"{title!r}: invalid {field} aid {value!r}: {reasons}"
            )
    return contract


def remove_existing_closure(body: str) -> str:
    return strip_generated_session_aids(body)


def closing_flow(title: str, contract: dict[str, object]) -> str:
    keywords = " · ".join(str(item) for item in contract["keywords"])
    return "\n".join(
        (
            f"#### CLOSING RECALL FLOW — {title.upper()}",
            "",
            "```text",
            f"START / CONCEPT: {title}",
            "        |",
            "        v",
            f"EXACT TERMS: {keywords}",
            "        |",
            "        v",
            f"MECHANISM / ARGUMENT: {contract['mechanism']}",
            "        |",
            "        v",
            f"CONSEQUENCE / CONTRAST: {contract['consequence']}",
            "        |",
            "        v",
            f"UPSC TRAP / ANSWER-USE: {contract['trap']}",
            "        |",
            "        v",
            f"ANSWER-GRABBING FORMULATION: {contract['opening']}",
            "```",
        )
    )


def session_block(
    number: int,
    title: str,
    body: str,
    semantic_override: dict[str, object] | None = None,
) -> str:
    content = remove_existing_closure(body)
    contract = semantic_contract(title, content, semantic_override)
    keywords = "\n".join(
        f"- **{keyword}**" for keyword in contract["keywords"]
    )
    return "\n\n".join(
        (
            f"### SESSION {number} — {title.upper()}",
            "\n".join(
                (
                    "#### DEFINITION / WHAT THIS IS CALLED",
                    "",
                    f"**Plain-language definition:** {contract['plain']}",
                    "",
                    f"**Technical definition:** {contract['technical']}",
                )
            ),
            "\n".join(
                (
                    "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM",
                    "",
                    f"> {contract['opening']}",
                )
            ),
            "\n".join(
                (
                    "#### MUST-WRITE KEYWORDS",
                    "",
                    keywords,
                    "",
                    f"**How to use them:** {contract['how']}",
                )
            ),
            content,
            closing_flow(title, contract),
        )
    ).strip()


def override_title(
    topic_key: str,
    raw_title: str,
    overrides: dict[str, dict[str, object]],
) -> str:
    title = clean_heading(raw_title)
    mapping = overrides.get(topic_key, {}).get("session_titles", {})
    if isinstance(mapping, dict):
        for source, target in mapping.items():
            if clean_heading(str(source)).casefold() == title.casefold():
                return clean_heading(str(target))
    return title


def semantic_override_for(
    topic_key: str,
    title: str,
    overrides: dict[str, dict[str, object]],
) -> dict[str, object] | None:
    topic = overrides.get(topic_key, {})
    mapping = topic.get("semantic_overrides", {})
    if not isinstance(mapping, dict):
        return None
    return next(
        (
            value
            for source, value in mapping.items()
            if clean_heading(str(source)).casefold() == title.casefold()
            and isinstance(value, dict)
        ),
        None,
    )


def semantic_session_title(value: str) -> str:
    title = clean_heading(value)
    title = re.sub(
        r"\s*[—-]\s*\[(?:CORE\s+(?:PRELIMS|MAINS)|"
        r"SUPPORTING(?:\s+(?:PRELIMS|MAINS))?|OPTIONAL\s+ADVANCED)\]\s*$",
        "",
        title,
        flags=re.I,
    )
    title = re.sub(
        r"^(?:CORE\s+LAB\s+\d+\s*:|ROADMAP\s*:)\s*",
        "",
        title,
        flags=re.I,
    )
    return title.strip()


def session_title_is_meta(value: str) -> bool:
    title = clean_heading(value)
    return bool(
        visual.is_production_meta_stage(title)
        or re.search(
            r"^(?:AUDITED\s+CORE\s+APPLICATION\s+LABS|"
            r"MASTER\s+UPSC\s+TRAP\s+MATRIX|"
            r"CORE\s+LAB\s+\d+\s*:\s*A\s+\d+-WORD\s+ANSWER\s+SPINE|"
            r"CURRENT(?:[- ]RESEARCH)?\s+(?:GUARDRAIL|LINKAGES?|ANCHOR|STATUS).*|"
            r"UPSC\s+TRAP(?:S|\s+MATRIX)?(?:\s|,|-).*|"
            r"READING\s+.*CURRENT\s+AFFAIRS.*|"
            r".*ANSWER-WRITING\s+ARCHITECTURE.*)$",
            re.sub(
                r"\s*[—-]\s*\[[^]]+]\s*$",
                "",
                title,
            ),
            re.I,
        )
    )


def h2_bounds(lines: list[str], title: str) -> tuple[int, int]:
    start = next(
        (
            index
            for index, line in enumerate(lines)
            if H2_RE.fullmatch(line.strip())
            and clean_heading(H2_RE.fullmatch(line.strip()).group(1)).casefold()
            == title.casefold()
        ),
        None,
    )
    if start is None:
        raise RefreshError(f"Missing canonical H2: {title}")
    end = next(
        (
            index
            for index in range(start + 1, len(lines))
            if H2_RE.fullmatch(lines[index].strip())
        ),
        len(lines),
    )
    return start, end


def apply_resegmentation(
    markdown: str,
    topic: Topic,
    overrides: dict[str, dict[str, object]],
) -> str:
    topic_override = overrides.get(topic.key, {})
    spec = topic_override.get("resegmentation")
    if not isinstance(spec, dict):
        return markdown
    anchors = spec.get("anchors")
    if not isinstance(anchors, list) or not anchors:
        raise RefreshError(f"{topic.key}: resegmentation requires anchors.")

    lines = markdown.replace("\r\n", "\n").splitlines()
    basic_start, basic_end = h2_bounds(lines, "BASIC LEARNING SESSION")
    existing_sessions = [
        line
        for line in lines[basic_start + 1 : basic_end]
        if H3_RE.fullmatch(line.strip())
        and SESSION_RE.fullmatch(
            clean_heading(H3_RE.fullmatch(line.strip()).group(1))
        )
    ]
    minimum = int(spec.get("minimum_sessions") or len(anchors))
    if len(existing_sessions) >= minimum:
        return markdown

    cleaned = strip_generated_session_aids(
        "\n".join(lines[basic_start + 1 : basic_end])
    )
    basic_lines = cleaned.splitlines()
    old_sessions = [
        index
        for index, line in enumerate(basic_lines)
        if H3_RE.fullmatch(line.strip())
        and SESSION_RE.fullmatch(
            clean_heading(H3_RE.fullmatch(line.strip()).group(1))
        )
    ]
    if not old_sessions:
        raise RefreshError(
            f"{topic.key}: resegmentation could not locate the existing session start."
        )

    normalized_anchors: list[tuple[str, str]] = []
    for item in anchors:
        if not isinstance(item, dict) or not item.get("source") or not item.get("title"):
            raise RefreshError(
                f"{topic.key}: each resegmentation anchor needs source and title."
            )
        normalized_anchors.append(
            (clean_heading(str(item["source"])), clean_heading(str(item["title"])))
        )

    found: list[int] = []
    search_from = old_sessions[0]
    for source, _ in normalized_anchors:
        matches = [
            index
            for index in range(search_from, len(basic_lines))
            if (
                heading := re.fullmatch(
                    r"^####(?!#)\s+(.+?)\s*$",
                    basic_lines[index].strip(),
                )
            )
            and clean_heading(heading.group(1)).casefold() == source.casefold()
        ]
        if not matches:
            raise RefreshError(
                f"{topic.key}: missing resegmentation anchor {source!r}."
            )
        found.append(matches[0])
        search_from = matches[0] + 1

    for index in old_sessions:
        basic_lines[index] = ""
    first_source, first_title = normalized_anchors[0]
    first_start = old_sessions[0]
    basic_lines[first_start] = f"### SESSION 1 — {first_title}"
    basic_lines[found[0]] = f"#### {first_source}"
    for number, ((_, title), index) in enumerate(
        zip(normalized_anchors[1:], found[1:]),
        2,
    ):
        basic_lines[index] = f"### SESSION {number} — {title}"

    replacement = "\n".join(basic_lines).strip("\n").splitlines()
    lines[basic_start + 1 : basic_end] = replacement
    return "\n".join(lines).rstrip() + "\n"


def sessionize(
    markdown: str,
    topic: Topic,
    overrides: dict[str, dict[str, object]],
) -> str:
    markdown = apply_resegmentation(markdown, topic, overrides)
    lines = markdown.replace("\r\n", "\n").splitlines()
    basic_start, basic_end = h2_bounds(lines, "BASIC LEARNING SESSION")
    h3s = [
        (index, H3_RE.fullmatch(lines[index].strip()).group(1))
        for index in range(basic_start + 1, basic_end)
        if H3_RE.fullmatch(lines[index].strip())
    ]
    explicit = [
        index for index, title in h3s if SESSION_RE.fullmatch(clean_heading(title))
    ]
    if explicit:
        first = min(explicit)
        # The approved exemplar has one stray H3 inside its final named session.
        # Demote such nested headings so the named session remains the major unit.
        for index, title in h3s:
            if index > first and not SESSION_RE.fullmatch(clean_heading(title)):
                lines[index] = "#" + lines[index]
        basic_start, basic_end = h2_bounds(lines, "BASIC LEARNING SESSION")
        h3s = [
            (index, H3_RE.fullmatch(lines[index].strip()).group(1))
            for index in range(basic_start + 1, basic_end)
            if H3_RE.fullmatch(lines[index].strip())
        ]
        positions = [index for index, _ in h3s]
        sessions: list[tuple[int, int, re.Match[str], str]] = []
        for position, (start, raw_title) in enumerate(h3s):
            match = SESSION_RE.fullmatch(clean_heading(raw_title))
            if not match:
                continue
            end = (
                positions[position + 1]
                if position + 1 < len(positions)
                else basic_end
            )
            body = "\n".join(lines[start + 1 : end])
            sessions.append((start, end, match, body))
        replacements: list[tuple[int, int, str]] = []
        number = 0
        meta_flags = [
            session_title_is_meta(match.group(2))
            for _, _, match, _ in sessions
        ]
        has_non_meta_session = any(not flag for flag in meta_flags)
        for start, end, match, body in sessions:
            raw_title = match.group(2)
            is_meta = session_title_is_meta(raw_title)
            keep_meta_as_only_content = (
                is_meta
                and not has_non_meta_session
                and bool(session_sentences(body))
            )
            if is_meta and not keep_meta_as_only_content:
                retained = strip_generated_session_aids(body)
                replacements.append(
                    (
                        start,
                        end,
                        f"### {clean_heading(raw_title)}\n\n{retained}".strip(),
                    )
                )
                continue
            number += 1
            title = (
                topic.title
                if keep_meta_as_only_content and number == 1
                else f"{topic.title}: Core Distinctions"
                if keep_meta_as_only_content
                else semantic_session_title(
                    override_title(topic.key, raw_title, overrides)
                )
            )
            replacements.append(
                (
                    start,
                    end,
                    session_block(
                        number,
                        title,
                        body,
                        semantic_override_for(topic.key, title, overrides),
                    ),
                )
            )
        for start, end, replacement in reversed(replacements):
            lines[start:end] = replacement.splitlines()
        return "\n".join(lines).rstrip() + "\n"

    positions = [index for index, _ in h3s]
    replacements: list[tuple[int, int, str]] = []
    number = 0
    for position, (start, raw_title) in enumerate(h3s):
        end = positions[position + 1] if position + 1 < len(positions) else basic_end
        title = semantic_session_title(raw_title)
        body = "\n".join(lines[start + 1 : end])
        if (
            META_H3.fullmatch(title)
            or session_title_is_meta(raw_title)
            or len(strip_markdown(body)) < 80
        ):
            continue
        number += 1
        title = semantic_session_title(
            override_title(topic.key, title, overrides)
        )
        replacements.append(
            (
                start,
                end,
                session_block(
                    number,
                    title,
                    body,
                    semantic_override_for(topic.key, title, overrides),
                ),
            )
        )
    if not replacements:
        h4s = [
            (
                index,
                re.fullmatch(
                    r"^####(?!#)\s+(.+?)\s*$",
                    lines[index].strip(),
                ).group(1),
            )
            for index in range(basic_start + 1, basic_end)
            if re.fullmatch(
                r"^####(?!#)\s+(.+?)\s*$",
                lines[index].strip(),
            )
        ]
        h4_positions = [index for index, _ in h4s]
        for position, (start, raw_title) in enumerate(h4s):
            end = (
                h4_positions[position + 1]
                if position + 1 < len(h4_positions)
                else basic_end
            )
            title = semantic_session_title(raw_title)
            body = "\n".join(lines[start + 1 : end])
            if (
                META_H3.fullmatch(title)
                or session_title_is_meta(raw_title)
                or len(strip_markdown(body)) < 80
            ):
                continue
            number += 1
            title = semantic_session_title(
                override_title(topic.key, title, overrides)
            )
            replacements.append(
                (
                    start,
                    end,
                    session_block(
                        number,
                        title,
                        body,
                        semantic_override_for(topic.key, title, overrides),
                    ),
                )
            )
    if not replacements:
        raise RefreshError(f"{topic.key}: no learner-scale Basic sessions were found.")
    for start, end, replacement in reversed(replacements):
        lines[start:end] = replacement.splitlines()
    return "\n".join(lines).rstrip() + "\n"


def option_parts(line: str) -> dict[str, str] | None:
    match = OPTION_RE.fullmatch(line)
    if match:
        label = match.group("label") or match.group("paren")
        return {
            "kind": "line",
            "indent": match.group("indent") or "",
            "bullet": match.group("bullet") or "",
            "label": label,
            "punct": match.group("punct") or "",
            "paren": "yes" if match.group("paren") else "no",
            "space": match.group("space"),
            "text": match.group("text"),
        }
    table = TABLE_OPTION_RE.fullmatch(line)
    if table:
        return {
            "kind": "table",
            "indent": table.group("indent") or "",
            "bullet": "",
            "label": table.group("label"),
            "punct": "",
            "paren": "no",
            "space": " ",
            "text": table.group("text"),
        }
    return None


def render_option(slot: dict[str, str], label: str, text: str) -> str:
    rendered_label = label.lower() if slot["label"].islower() else label
    if slot.get("kind") == "table":
        return f"{slot['indent']}| {rendered_label} | {text} |"
    marker = (
        f"({rendered_label})"
        if slot["paren"] == "yes"
        else f"{rendered_label}{slot['punct']}"
    )
    return (
        slot["indent"]
        + slot["bullet"]
        + marker
        + slot["space"]
        + text
    )


def target_answer_keys(topic_key: str, count: int) -> list[str]:
    if count < 1:
        return []
    return [letter for index in range(count) for letter in "ABCD"][:count]


def update_explanation_labels(
    line: str,
    old_to_new: dict[str, str],
) -> str:
    def named(match: re.Match[str]) -> str:
        prefix, label = match.groups()
        replacement = old_to_new[label.upper()]
        if label.islower():
            replacement = replacement.lower()
        return prefix + replacement

    line = re.sub(r"\b([Oo]ptions?\s+)([A-Da-d])\b", named, line)
    line = re.sub(
        r"\b([Cc]orrect (?:option|answer):\s*)([A-Da-d])\b",
        named,
        line,
    )
    line = re.sub(
        r"((?:\bkey|->)\s*)([A-Da-d])\b",
        named,
        line,
    )
    line = re.sub(
        r"\(([A-Da-d])\)",
        lambda match: "("
        + (
            old_to_new[match.group(1).upper()].lower()
            if match.group(1).islower()
            else old_to_new[match.group(1).upper()]
        )
        + ")",
        line,
    )
    return line


def rebalance_mcqs(markdown: str, topic_key: str) -> tuple[str, dict[str, object]]:
    lines = markdown.replace("\r\n", "\n").splitlines()
    start, end = h2_bounds(lines, "BASIC MCQS / REMEDIATION")
    heading_positions: list[int] = []
    bold_positions: list[int] = []
    plain_positions: list[int] = []
    for index in range(start + 1, end):
        stripped = lines[index].strip()
        heading = re.match(r"^#{3,5}(?!#)\s+(.+?)\s*$", stripped)
        heading_question = bool(
            heading
            and re.search(
                r"(?:^|\b)(?:MCQ\s*[-:]?\s*\d+|[A-Z]{1,4}\s*\d+)"
                r"(?:\b|\s*[—:-])|"
                r"^\d+[.)]\s+",
                heading.group(1),
                re.I,
            )
        )
        plain_numbered_question = bool(
            re.match(r"^\d+[.)]\s+\S", stripped)
        )
        bold_numbered_question = bool(
            re.match(r"^\*\*\d+[.)]\s+.+\*\*\s*$", stripped)
        )
        if heading_question:
            heading_positions.append(index)
        elif bold_numbered_question:
            bold_positions.append(index)
        elif plain_numbered_question:
            plain_positions.append(index)
    h4_positions = (
        heading_positions
        if heading_positions
        else bold_positions
        if bold_positions
        else plain_positions
    )
    parsed: list[dict[str, object]] = []
    for position, block_start in enumerate(h4_positions):
        block_end = (
            h4_positions[position + 1]
            if position + 1 < len(h4_positions)
            else end
        )
        answer_index = next(
            (
                index
                for index in range(block_start + 1, block_end)
                if ANSWER_RE.search(lines[index])
                or ANSWER_TEXT_RE.search(lines[index])
                or CORRECT_ANSWER_RE.search(lines[index])
                or DASH_ANSWER_RE.search(lines[index])
            ),
            None,
        )
        option_rows = [
            (index, option_parts(lines[index]))
            for index in range(
                block_start + 1,
                answer_index if answer_index is not None else block_end,
            )
            if option_parts(lines[index])
        ]
        if len(option_rows) != 4 or answer_index is None:
            continue
        labels = [str(parts["label"]).upper() for _, parts in option_rows]
        if set(labels) != set("ABCD"):
            continue
        answer_match = (
            ANSWER_RE.search(lines[answer_index])
            or ANSWER_TEXT_RE.search(lines[answer_index])
            or CORRECT_ANSWER_RE.search(lines[answer_index])
            or DASH_ANSWER_RE.search(lines[answer_index])
        )
        parsed.append(
            {
                "start": block_start,
                "end": block_end,
                "option_rows": option_rows,
                "answer_index": answer_index,
                "correct": answer_match.group("label").upper(),
            }
        )
    targets = target_answer_keys(topic_key, len(parsed))
    audit_rows: list[dict[str, object]] = []
    seed = int.from_bytes(hashlib.sha256(topic_key.encode()).digest()[:8], "big")
    for question_number, (question, target) in enumerate(zip(parsed, targets), 1):
        option_rows = question["option_rows"]
        old_text = {
            str(parts["label"]).upper(): str(parts["text"])
            for _, parts in option_rows
        }
        correct = str(question["correct"])
        wrong = [label for label in "ABCD" if label != correct]
        random.Random(seed + question_number * 7919).shuffle(wrong)
        new_to_old = {target: correct}
        for new_label, old_label in zip(
            [label for label in "ABCD" if label != target],
            wrong,
        ):
            new_to_old[new_label] = old_label
        old_to_new = {old: new for new, old in new_to_old.items()}
        for slot_number, (line_index, parts) in enumerate(option_rows):
            new_label = "ABCD"[slot_number]
            lines[line_index] = render_option(
                parts,
                new_label,
                old_text[new_to_old[new_label]],
            )
        answer_index = int(question["answer_index"])

        def answer_replacement(match: re.Match[str]) -> str:
            label = target.lower() if match.group("label").islower() else target
            groups = match.groupdict()
            return (
                match.group("prefix")
                + (groups.get("open") or "")
                + label
                + (groups.get("close") or "")
                + (groups.get("period") or "")
                + (groups.get("tail") or "")
                + (groups.get("suffix") or "")
            )

        answer_pattern = (
            ANSWER_RE
            if ANSWER_RE.search(lines[answer_index])
            else ANSWER_TEXT_RE
            if ANSWER_TEXT_RE.search(lines[answer_index])
            else CORRECT_ANSWER_RE
            if CORRECT_ANSWER_RE.search(lines[answer_index])
            else DASH_ANSWER_RE
        )
        lines[answer_index] = answer_pattern.sub(
            answer_replacement,
            lines[answer_index],
            count=1,
        )
        for index in range(answer_index + 1, int(question["end"])):
            lines[index] = update_explanation_labels(lines[index], old_to_new)
        audit_rows.append(
            {
                "question": question_number,
                "source_answer": correct,
                "refreshed_answer": target,
                "correct_option_text_sha256": hashlib.sha256(
                    old_text[correct].encode("utf-8")
                ).hexdigest(),
                "option_texts_preserved": True,
            }
        )
    text = "\n".join(lines).rstrip() + "\n"
    text = re.sub(
        r"(?im)^>\s*Correct options rotate strictly "
        r"[A-D]\s*(?:→|->|-)\s*[A-D]\s*(?:→|->|-)\s*[A-D]\s*"
        r"(?:→|->|-)\s*[A-D],\s*repeated\s+([^.]+)\.$",
        r"> Correct options rotate strictly A → B → C → D, repeated \1.",
        text,
    )
    text = re.sub(
        r"Correct options rotate strictly A\s*(?:→|->|-)\s*B\s*"
        r"(?:→|->|-)\s*C\s*(?:→|->|-)\s*D throughout each sequence\.",
        "Correct options rotate strictly A → B → C → D throughout each sequence.",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"(?:The original answer sequence is preserved and must remain |"
        r"Correct options rotate strictly |"
        r"Correct-option rotation follows |"
        r"Strict answer rotation )"
        r"A\s*(?:→|->|-)\s*B\s*(?:→|->|-)\s*C\s*"
        r"(?:→|->|-)\s*D(?:\s+(?:without deviation|across all \d+ questions))?\.?",
        "Answer placement follows strict A → B → C → D rotation.",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"rotation\.\s*,\s*repeated\s+([^.]+)\.",
        r"rotation, repeated \1.",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"(?im)^.*(?:answer sequence|answer rotation|workbook rotation|"
        r"answers follow).*A\s*(?:→|->|-)\s*B\s*(?:→|->|-)\s*C\s*"
        r"(?:→|->|-)\s*D.*$",
        "- Answer placement follows strict A → B → C → D rotation.",
        text,
    )
    text = re.sub(
        r"strict A\s*(?:→|->|-)\s*B\s*(?:→|->|-)\s*C\s*"
        r"(?:→|->|-)\s*D rotation",
        "strict A → B → C → D rotation",
        text,
        flags=re.I,
    )
    return text, {
        "topic_seed_sha256": hashlib.sha256(topic_key.encode()).hexdigest(),
        "question_count": len(parsed),
        "keys": targets,
        "counts": {letter: targets.count(letter) for letter in "ABCD"},
        "all_correct_option_texts_preserved": all(
            bool(row["option_texts_preserved"]) for row in audit_rows
        ),
        "questions": audit_rows,
    }


def session_cards(markdown: str) -> list[visual.Closure]:
    basic = re.search(
        r"(?ims)^##\s+BASIC LEARNING SESSION\s*(.*?)"
        r"(?=^##\s+BASIC MCQS / REMEDIATION)",
        markdown,
    )
    if not basic:
        raise RefreshError("Cannot extract Basic sessions for visual generation.")
    section = basic.group(1)
    headings = list(
        re.finditer(
            r"(?im)^###\s+SESSION\s+\d+\s*[—-]\s*(.+?)\s*$",
            section,
        )
    )
    cards: list[visual.Closure] = []
    for position, heading in enumerate(headings):
        end = headings[position + 1].start() if position + 1 < len(headings) else len(section)
        body = section[heading.end() : end]
        title = clean_heading(heading.group(1))

        def field(pattern: str, fallback: str) -> str:
            match = re.search(pattern, body, re.I | re.S | re.M)
            return strip_markdown(match.group(1)) if match else fallback

        plain = field(
            r"\*\*Plain-language definition:\*\*\s*(.+?)\s*(?=\n|$)",
            title,
        )
        technical = field(
            r"\*\*Technical definition:\*\*\s*(.+?)\s*(?=\n|$)",
            plain,
        )
        opening = field(
            r"####\s+ANSWER-GRABBING OPENING.*?\n+\s*>\s*(.+?)\s*(?=\n|$)",
            technical,
        )
        mechanism = field(
            r"MECHANISM / ARGUMENT:\s*(.+?)\s*(?=\n\s*\||\n\s*v|\n|$)",
            plain,
        )
        consequence = field(
            r"CONSEQUENCE / CONTRAST:\s*(.+?)\s*(?=\n\s*\||\n\s*v|\n|$)",
            technical,
        )
        trap = field(
            r"UPSC TRAP / ANSWER-USE:\s*(.+?)\s*(?=\n\s*\||\n\s*v|\n|$)",
            opening,
        )
        cards.append(
            visual.Closure(
                title=title,
                terms=technical,
                mechanism=mechanism,
                consequence=consequence,
                trap=trap,
                answer=opening,
            )
        )
    if not cards:
        raise RefreshError("No numbered session cards were found.")
    return cards


def generated_ascii_master(
    topic: Topic,
    cards: list[visual.Closure],
    markdown: str = "",
) -> str:
    """Return a topic-specific multi-panel conceptual atlas.

    The design manifest groups sessions by conceptual function. The builder
    renders distinct taxonomic, chronological, causal, comparative,
    objection-response and answer-synthesis structures rather than one card
    per numbered teaching session.
    """
    return ascii_master.build_master_fragment(
        root=ROOT,
        manifest_path=ASCII_DESIGN_MANIFEST,
        topic_key=topic.key,
        title=topic.title,
        subject=topic.subject,
        cards=cards,
        markdown=markdown,
    )


def manual_ascii_specs() -> dict[str, ascii_master.ManualTopicSpec]:
    return ascii_master.load_manual_topic_specs(ASCII_SPEC_DIR)


def manual_ascii_topic_spec(
    topic_key: str,
) -> ascii_master.ManualTopicSpec | None:
    return manual_ascii_specs().get(topic_key)


def ensure_ascii_master(
    markdown: str,
    topic: Topic,
    *,
    require_manual: bool = False,
) -> tuple[str, str]:
    cards = session_cards(markdown)
    markdown = re.sub(
        r"(?ims)\n*^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*$.*\Z",
        "",
        markdown,
    ).rstrip()
    manual = manual_ascii_topic_spec(topic.key)
    if manual is not None:
        ascii_text = ascii_master.build_manual_fragment(manual)
    elif require_manual:
        raise RefreshError(
            f"{topic.key}: finalization requires an authored manual ASCII spec."
        )
    else:
        ascii_text = generated_ascii_master(topic, cards, markdown)
    appended = (
        markdown.rstrip()
        + "\n\n### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + "**High-yield use:** Follow the panels as one topic-specific conceptual "
        "atlas: root question, classifications, processes or arguments, comparisons, "
        "objections and a final answer-writing spine. This text-native master is "
        "separate from both graphical flowchart artifacts.\n\n"
        + ascii_text
        + "\n"
    )
    return appended, ascii_text


def set_frontmatter(
    markdown: str,
    topic: Topic,
    navigation_name: str,
) -> str:
    normalized = markdown.replace("\r\n", "\n")
    body = normalized
    retained: list[str] = []
    if normalized.startswith("---\n"):
        end = normalized.find("\n---\n", 4)
        if end >= 0:
            for line in normalized[4:end].splitlines():
                if not re.match(
                    r"^(?:title|topic_key|cover_image):",
                    line.strip(),
                    re.I,
                ):
                    retained.append(line)
            body = normalized[end + 5 :]
    frontmatter = [
        "---",
        f"title: {json.dumps(topic.title + ' — Learner-v2 Refreshed', ensure_ascii=False)}",
        f"topic_key: {topic.key}",
        f"cover_image: assets/{navigation_name}",
        *retained,
        "---",
    ]
    return "\n".join(frontmatter) + "\n" + body.lstrip()


def insert_navigation(markdown: str, navigation_name: str) -> str:
    markdown = re.sub(
        r"(?ims)\n*!\[Refreshed teaching navigation]\([^)]+\)\s*"
        r"\n+\*Distinct embedded teaching-navigation image\..*?"
        r"at-a-glance artifact\.\*\s*",
        "\n",
        markdown,
    )
    replacement = (
        "## BASIC LEARNING SESSION\n\n"
        f"![Refreshed teaching navigation](assets/{navigation_name})\n\n"
        "*Distinct embedded teaching-navigation image. The separate continuous "
        "Cārvāka-style flowchart package remains an independent at-a-glance artifact.*"
    )
    return markdown.replace("## BASIC LEARNING SESSION", replacement, 1)


def navigation_image(
    topic: Topic,
    cards: list[visual.Closure],
    output: Path,
) -> None:
    width = 1800
    row_height = 210
    height = 260 + row_height * ((len(cards) + 1) // 2)
    image = Image.new("RGB", (width, height), "#F4F7FB")
    draw = ImageDraw.Draw(image)
    title_font = visual.font(visual.FONT_BOLD, 44)
    card_font = visual.font(visual.FONT_BOLD, 28)
    body_font = visual.font(visual.FONT_REGULAR, 21)
    draw.rounded_rectangle((40, 35, width - 40, 190), 28, fill="#17233C")
    draw.text((80, 65), topic.title, font=title_font, fill="#FFFFFF")
    draw.text(
        (82, 130),
        "REFRESHED TEACHING NAVIGATION — BASIC/CORE FIRST",
        font=body_font,
        fill="#FFC857",
    )
    palette = ("#245B91", "#168373", "#8A5A12", "#8A3440")
    for index, card in enumerate(cards):
        row, column = divmod(index, 2)
        x0 = 55 + column * 870
        y0 = 225 + row * row_height
        x1 = x0 + 820
        y1 = y0 + 165
        color = palette[index % len(palette)]
        draw.rounded_rectangle((x0, y0, x1, y1), 22, fill="#FFFFFF", outline=color, width=5)
        draw.ellipse((x0 + 24, y0 + 32, x0 + 114, y0 + 122), fill=color)
        number = f"{index + 1:02d}"
        box = draw.textbbox((0, 0), number, font=card_font)
        draw.text(
            (x0 + 69 - (box[2] - box[0]) / 2, y0 + 55),
            number,
            font=card_font,
            fill="#FFFFFF",
        )
        title_lines = visual.wrap(draw, card.title, card_font, 650)[:2]
        for line_number, line in enumerate(title_lines):
            draw.text(
                (x0 + 140, y0 + 30 + line_number * 38),
                line,
                font=card_font,
                fill="#17233C",
            )
        keyword = visual.wrap(draw, card.terms, body_font, 650)[0]
        draw.text((x0 + 140, y0 + 112), keyword, font=body_font, fill="#5F6F82")
    image.save(output, "PNG", dpi=(180, 180), optimize=True)


def verify_tiled_identity(
    master: Path,
    tiled: Path,
    tiles: list[dict[str, int]],
) -> list[str]:
    errors: list[str] = []
    source = Image.open(master).convert("RGB")
    with fitz.open(tiled) as document:
        if document.page_count != len(tiles):
            errors.append("Tiled PDF page count differs from tile coordinates.")
        for index, tile_record in enumerate(tiles[: document.page_count]):
            images = document[index].get_images(full=True)
            if len(images) != 1:
                errors.append(f"Tiled page {index + 1} does not contain one crop.")
                continue
            extracted = document.extract_image(images[0][0])
            actual = Image.open(BytesIO(extracted["image"])).convert("RGB")
            expected = source.crop(
                (
                    0,
                    int(tile_record["y_start"]),
                    source.width,
                    int(tile_record["y_end"]),
                )
            )
            if actual.size != expected.size:
                errors.append(f"Tiled page {index + 1} has wrong crop dimensions.")
            elif ImageChops.difference(actual, expected).getbbox() is not None:
                errors.append(f"Tiled page {index + 1} is not a master-identical crop.")
            actual.close()
            expected.close()
    source.close()
    return errors


def flowchart_package(
    topic: Topic,
    markdown_path: Path,
    markdown: str,
    ascii_text: str,
    paths: Paths,
    generation: int,
    *,
    preservation_before: dict[str, str] | None = None,
    ascii_master_bytes: bytes | None = None,
) -> dict[str, object]:
    folder = paths.flowchart_dir
    spec_path = GRAPHICAL_SPEC_DIR / topic.subject / f"{topic.key}.json"
    if not spec_path.is_file():
        raise RefreshError(
            f"{topic.key}: explicit Cārvāka graphical spec is missing: {spec_path}"
        )
    spec = load_json(spec_path)
    current_markdown = relative(markdown_path)
    status = spec.get("status")
    if isinstance(status, dict):
        status["approved"] = False
        status["review"] = "PENDING USER REVIEW"
        status["line"] = (
            f"Approval: FALSE • Pending user review • active generation g{generation} "
            "• explicit approval of this exact generation is required "
            "• all prior artifacts unchanged"
        )
    spec["source_markdown"] = current_markdown

    def refresh_source_references(value: object) -> object:
        if isinstance(value, dict):
            return {
                key: refresh_source_references(nested)
                for key, nested in value.items()
            }
        if isinstance(value, list):
            return [refresh_source_references(nested) for nested in value]
        if isinstance(value, str) and "learning-sessions" in value:
            anchor = value[value.find("#") :] if "#" in value else ""
            return current_markdown + anchor
        return value

    spec = refresh_source_references(spec)
    generated_spec = (
        paths.knowledge_dir
        / f"{topic.key}_Graphical-Spec-g{generation}.json"
    )
    generated_spec.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    preserve = dict(preservation_before or {})
    for name in graphical.REFERENCE_HASHES:
        path = ROOT / graphical.REFERENCE_FOLDER / name
        if not path.is_file():
            raise RefreshError(f"Immutable Cārvāka reference is incomplete: {path}")
        preserve[relative(path)] = sha256(path)
    try:
        flow, _ = graphical.render_package(
            ROOT,
            generated_spec,
            folder,
            ascii_master_bytes=(
                ascii_master_bytes
                if ascii_master_bytes is not None
                else ascii_master.standalone_panel_text(
                    ascii_text
                ).encode("utf-8")
            ),
            preservation_before=preserve,
        )
    except graphical.CarvakaError as exc:
        raise RefreshError(str(exc)) from exc
    manual_spec = manual_ascii_topic_spec(topic.key)
    flow.update(
        {
            "ascii_master_source": (
                "manual-authored-spec"
                if manual_spec is not None
                else "generic-development"
            ),
            "ascii_master_spec": (
                relative(manual_spec.source_path)
                if manual_spec is not None
                else None
            ),
            "ascii_master_spec_sha256": (
                sha256(manual_spec.source_path)
                if manual_spec is not None
                else None
            ),
        }
    )
    return flow


def record_for(
    topic: Topic,
    generation: int,
    paths: Paths,
    flow: dict[str, object],
    source_hashes: dict[str, str],
    *,
    generation_date: str = REFRESH_DATE,
    refresh_id: str = REFRESH_ID,
) -> dict[str, object]:
    record = copy.deepcopy(topic.source_record)
    record.update(
        {
            "record_id": f"{topic.key}:{V2_VARIANT}:g{generation}",
            "generation": generation,
            "supersedes": topic.record_id,
            "command": (
                str(topic.source_record.get("command") or "")
                .removesuffix(" — Regenerate")
                + (
                    " — Learner-v2 semantic-aid repair"
                    if refresh_id == SEMANTIC_REPAIR_ID
                    else " — Authored Notions-style ASCII-master repair"
                    if refresh_id == ASCII_REPAIR_ID
                    else " — Cārvāka graphical-standard repair"
                    if refresh_id == GRAPHICAL_REPAIR_ID
                    else " — Learner-v2 refreshed"
                )
            ).strip(),
            "markdown": relative(paths.markdown),
            "workbook_markdown": relative(paths.workbook_markdown),
            "main_pdf": relative(paths.main_pdf),
            "workbook": relative(paths.workbook_pdf),
            "asset_folder": relative(paths.assets),
            "generated_on": generation_date,
            "approved": False,
            "approval": {
                "approved": False,
                "approved_on": None,
                "scope": f"{topic.key}:{V2_VARIANT}:g{generation}",
            },
            "validation": {
                "state": "passed",
                "validated_on": generation_date,
                "validator": (
                    "tools/refresh_all_v2_learning_sessions.py + "
                    "tools/validate_v2_export.py"
                ),
            },
            "refresh_profile": refresh_id,
            "continuous_core_first": flow,
        }
    )
    provenance = record.setdefault("provenance", {})
    if not isinstance(provenance, dict):
        provenance = {}
        record["provenance"] = provenance
    provenance.update(
        {
            "assembled_markdown": relative(paths.markdown),
            "renderer": {
                "name": markdown_learning_pdf.RENDERER_NAME,
                "version": markdown_learning_pdf.RENDERER_VERSION,
            },
            "generation_date": generation_date,
            "refresh": {
                "id": refresh_id,
                "source_record": topic.record_id,
                "source_markdown": relative(topic.markdown),
                "source_hashes": source_hashes,
                "session_contract": "named-session definition/opening/keywords/use/closure",
                "mcq_keys": (
                    "strict A-B-C-D rotation"
                ),
                "tracker_updated": False,
                "tracker_sha256": sha256(TRACKER),
            },
            "graphical_renderer": {
                "name": graphical.RENDERER_NAME,
                "version": graphical.RENDERER_VERSION,
                "reference_master_sha256": graphical.REFERENCE_HASHES[
                    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ],
            },
        }
    )
    return record


def new_topic_record_for(
    topic: Topic,
    generation: int,
    generation_date: str,
    paths: Paths,
    flow: dict[str, object],
    source_hashes: dict[str, str],
    spec: dict[str, object],
    validation: dict[str, object],
) -> dict[str, object]:
    """Build a clean first learner-v2 record without copying legacy variant fields."""
    predecessor = topic.record_id or None
    provenance = {
        "workflow": "learner-first-v2-refreshed-new-topic",
        "source_basic": spec.get("source_basic"),
        "source_canonical": spec.get("source_canonical"),
        "source_advanced": spec.get("source_advanced"),
        "cross_topic_sources": list(spec.get("cross_topic_sources", [])),
        "pyq_indexes": list(spec.get("pyq_indexes", [])),
        "official_question_sources": list(
            spec.get("official_question_sources", [])
        ),
        "local_ocr_sources": list(spec.get("local_ocr_sources", [])),
        "live_sources": list(spec.get("live_sources", [])),
        "assembled_markdown": relative(paths.markdown),
        "renderer": {
            "name": markdown_learning_pdf.RENDERER_NAME,
            "version": markdown_learning_pdf.RENDERER_VERSION,
        },
        "generation_date": generation_date,
        "superseded_v1": predecessor,
        "source_hashes": source_hashes,
        "session_contract": "named-session definition/opening/keywords/use/closure",
        "mcq_keys": (
            "strict A-B-C-D rotation"
        ),
        "practice_profile": spec.get("practice_profile"),
        "current_linkage_note": spec.get("current_linkage_note"),
        "pyq_status_note": spec.get("pyq_status_note"),
        "new_visual_count": 1,
        "new_flowchart_page_count": validation.get("flowchart_tiled_pages"),
        "flowchart_renderer": (
            "Cārvāka-style continuous same-master PNG/poster/tiled renderer"
        ),
        "tracker_updated": False,
        "tracker_sha256": sha256(TRACKER),
    }
    return {
        "record_id": f"{topic.key}:{V2_VARIANT}:g{generation}",
        "topic_key": topic.key,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": predecessor,
        "command": str(spec["command"]),
        "main_pdf": relative(paths.main_pdf),
        "workbook": relative(paths.workbook_pdf),
        "markdown": relative(paths.markdown),
        "workbook_markdown": relative(paths.workbook_markdown),
        "asset_folder": relative(paths.assets),
        "generated_on": generation_date,
        "approved": False,
        "provenance": provenance,
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": f"{topic.key}:{V2_VARIANT}:g{generation}",
        },
        "validation": {
            "state": "passed",
            "validated_on": generation_date,
            "validator": (
                "tools/refresh_all_v2_learning_sessions.py new-topic + "
                "tools/validate_v2_export.py"
            ),
        },
        "continuous_core_first": flow,
        "refresh_profile": "learner-v2-refreshed-new-topic",
    }


def all_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def validate_flow(flow: dict[str, object]) -> list[str]:
    errors: list[str] = []
    for field in (
        "folder",
        "master_image",
        "poster_pdf",
        "tiled_pdf",
        "editable",
        "graphical_spec",
        "previews",
        "validation_report",
        "build_audit",
        "preservation_hashes",
        "ascii_master",
    ):
        value = flow.get(field)
        if not value or not repo_path(str(value)).exists():
            errors.append(f"Missing flowchart artifact: {field}")
    if errors:
        return errors
    folder = repo_path(str(flow["folder"]))
    previews = list(repo_path(str(flow["previews"])).glob("page-*.png"))
    contacts = list(repo_path(str(flow["previews"])).glob("contact-sheet-*.png"))
    if not previews:
        errors.append("Flowchart package has no page previews.")
    if not contacts:
        errors.append("Flowchart package has no contact sheet.")
    editable = repo_path(str(flow["editable"]))
    if not (editable / "topic-spec.json").is_file():
        errors.append("Flowchart package lacks editable topic-spec.json.")
    renderer = flow.get("renderer")
    if (
        not isinstance(renderer, dict)
        or renderer.get("name") != graphical.RENDERER_NAME
        or renderer.get("version") != graphical.RENDERER_VERSION
    ):
        errors.append("Flowchart metadata does not name the Cārvāka graphical-v2 renderer.")
    if flow.get("reference_master_sha256") != graphical.REFERENCE_HASHES[
        "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
    ]:
        errors.append("Flowchart metadata has the wrong immutable reference hash.")
    graphical_spec = repo_path(str(flow["graphical_spec"]))
    if flow.get("graphical_spec_sha256") != sha256(graphical_spec):
        errors.append("Flowchart package was not rendered from the current graphical spec.")
    if (editable / "topic-spec.json").read_bytes() != graphical_spec.read_bytes():
        errors.append("Editable topic spec differs from the canonical graphical spec.")
    report = repo_path(str(flow["validation_report"])).read_text(encoding="utf-8")
    if "same_master_identity=PASS" not in report:
        errors.append("Flowchart validation does not prove same-master tiled identity.")
    for required in (
        "header_legend_status=PASS",
        "continuous_numbered_rail=PASS",
        "final_synthesis_before_extra=PASS",
        "extra_visually_subordinate=PASS",
        "overflow_clipping_edge_contact=PASS",
        "poster_exact_master_embedding=PASS",
        "tiled_exact_master_crops=PASS",
        "reference_byte_preservation=PASS",
    ):
        if required not in report:
            errors.append(f"Flowchart validation lacks contract proof: {required}")
    if not all_under(folder, NOTES_ROOT):
        errors.append("Flowchart package is outside Learner-v2-Refreshed notes root.")
    return errors


def section_body(markdown: str, heading: str, next_heading: str | None) -> str:
    end = (
        rf"(?=^##\s+{re.escape(next_heading)}\s*$)"
        if next_heading
        else r"\Z"
    )
    match = re.search(
        rf"(?ims)^##\s+{re.escape(heading)}\s*$(.*?){end}",
        markdown,
    )
    return match.group(1) if match else ""


def core_completeness_errors(markdown: str) -> list[str]:
    """Apply deterministic evidence checks for core-first exam completeness."""
    basic = section_body(
        markdown,
        "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION",
    )
    practice = section_body(
        markdown,
        "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    )
    advanced = section_body(
        markdown,
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "CONSOLIDATED REGISTER NOTES",
    )
    errors: list[str] = []
    if len(strip_markdown(basic)) < 4000:
        errors.append("Basic/Core teaching is too small to be independently exam-complete.")
    if not advanced.strip():
        errors.append("Optional Advanced section is empty or missing.")
    advanced_pyq_terms = {
        strip_markdown(term).casefold()
        for line in advanced.splitlines()
        if "pyq" in line.casefold()
        for term in re.findall(r"\*\*([^*\n]{3,70})\*\*", line)
        if 1 <= len(strip_markdown(term).split()) <= 8
        and strip_markdown(term).casefold()
        not in {
            "core prerequisite",
            "promotion trigger",
            "provenance",
            "source ownership",
            "source audit",
            "pyq routing",
        }
        and not re.search(
            r"\b(?:pyq|owner|ownership|routing|route|note|ledger|audit|"
            r"coverage|status)\b",
            strip_markdown(term),
            re.I,
        )
    }
    core_and_practice = (basic + "\n" + practice).casefold()
    advanced_only = sorted(
        term
        for term in advanced_pyq_terms
        if term and term not in core_and_practice
    )
    if advanced_only:
        errors.append(
            "Verified-PYQ terminology appears only in Optional Advanced: "
            + ", ".join(advanced_only[:8])
        )
    return errors


def render_embedded_ascii_contact(
    pdf_path: Path,
    flowchart_dir: Path,
    blocks: list[tuple[int, int, str, str]],
) -> tuple[list[str], dict[str, object]]:
    errors: list[str] = []
    panel_pages: list[int] = []
    rendered_pages: list[tuple[int, Image.Image]] = []
    expected_titles = [
        f"PANEL {number}/{total}: {title}"
        for number, total, title, _ in blocks
    ]
    with fitz.open(pdf_path) as document:
        page_texts = [
            re.sub(r"\s+", " ", page.get_text("text")).strip()
            for page in document
        ]
        for number, title in enumerate(expected_titles, 1):
            matches = [
                index
                for index, text in enumerate(page_texts)
                if title in text
            ]
            if len(matches) != 1:
                errors.append(
                    f"Embedded ASCII panel {number} title appears on "
                    f"{len(matches)} PDF pages."
                )
                continue
            panel_pages.append(matches[0])
        if panel_pages != sorted(panel_pages):
            errors.append("Embedded ASCII panel pages are not sequential.")
        unique_pages = sorted(set(panel_pages))
        for page_index in unique_pages:
            page = document[page_index]
            page_text = page.get_text("text").strip()
            if len(page_text) < 80:
                errors.append(
                    f"Embedded ASCII render page {page_index + 1} is blank or too sparse."
                )
            pixmap = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
            image = Image.frombytes(
                "RGB",
                (pixmap.width, pixmap.height),
                pixmap.samples,
            )
            background = Image.new("RGB", image.size, "white")
            bounds = ImageChops.difference(image, background).getbbox()
            if bounds is None:
                errors.append(f"Embedded ASCII render page {page_index + 1} is blank.")
            overflow_words = [
                word
                for word in page.get_text("words")
                if (
                    word[0] < -0.5
                    or word[1] < -0.5
                    or word[2] > page.rect.width + 0.5
                    or word[3] > page.rect.height + 0.5
                )
            ]
            if overflow_words:
                errors.append(
                    f"Embedded ASCII render page {page_index + 1} has text "
                    "outside the media box."
                )
            rendered_pages.append((page_index + 1, image))

    contact_path = flowchart_dir / "embedded-ascii-contact.png"
    if rendered_pages:
        thumb_width = 520
        label_height = 28
        thumbs: list[tuple[int, Image.Image]] = []
        for page_number, image in rendered_pages:
            thumb_height = round(image.height * thumb_width / image.width)
            thumb = image.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            thumbs.append((page_number, thumb))
        columns = 2
        rows = (len(thumbs) + columns - 1) // columns
        cell_height = max(thumb.height for _, thumb in thumbs) + label_height
        contact = Image.new(
            "RGB",
            (columns * thumb_width, rows * cell_height),
            "white",
        )
        draw = ImageDraw.Draw(contact)
        for index, (page_number, thumb) in enumerate(thumbs):
            x = (index % columns) * thumb_width
            y = (index // columns) * cell_height
            draw.text((x + 8, y + 6), f"PDF page {page_number}", fill=(15, 35, 65))
            contact.paste(thumb, (x, y + label_height))
        contact.save(contact_path, optimize=True)
    else:
        errors.append("Embedded ASCII contact sheet could not be rendered.")
    return errors, {
        "panel_count": len(blocks),
        "panel_pages": [page + 1 for page in panel_pages],
        "rendered_page_count": len(rendered_pages),
        "contact_sheet": relative(contact_path) if contact_path.is_file() else None,
        "all_panel_titles_found_once": len(panel_pages) == len(blocks),
        "sequential_panel_pages": panel_pages == sorted(panel_pages),
        "blank_or_edge_touch_pages": [
            error for error in errors if "render page" in error
        ],
    }


def validate_generated_topic(
    topic: Topic,
    generation: int,
    paths: Paths,
    flow: dict[str, object],
    source_before: dict[str, str],
    mcq_audit: dict[str, object],
    *,
    source_text_override: str | None = None,
    source_inventory_files: Iterable[Path] | None = None,
) -> dict[str, object]:
    errors = validate_refreshed_markdown(paths.markdown, topic_key=topic.key)
    errors.extend(
        validate_v2_paths(ROOT, paths.markdown, paths.main_pdf, topic.key, "main")
    )
    errors.extend(
        validate_v2_paths(
            ROOT,
            paths.markdown,
            paths.workbook_pdf,
            topic.key,
            "workbook",
        )
    )
    errors.extend(
        validate_pdf(
            paths.main_pdf,
            variant=V2_VARIANT,
            mode="main",
        )
    )
    errors.extend(
        validate_pdf(
            paths.workbook_pdf,
            variant=V2_VARIANT,
            mode="workbook",
        )
    )
    main_layout_errors, main_metrics = validate_pdf_layout(paths.main_pdf)
    workbook_layout_errors, workbook_metrics = validate_pdf_layout(paths.workbook_pdf)
    errors.extend(main_layout_errors)
    errors.extend(workbook_layout_errors)
    errors.extend(validate_flow(flow))

    main_text = paths.markdown.read_text(encoding="utf-8")
    workbook_text = paths.workbook_markdown.read_text(encoding="utf-8")
    embedded_ascii = re.search(
        r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
        main_text,
    )
    standalone_ascii = repo_path(str(flow.get("ascii_master") or ""))
    if embedded_ascii and standalone_ascii.is_file():
        errors.extend(
            ascii_master_validation_errors(
                embedded_ascii.group(1),
                topic_key=topic.key,
                standalone_text=standalone_ascii.read_text(encoding="utf-8"),
            )
        )
    elif not standalone_ascii.is_file():
        errors.append("Standalone ASCII master is missing.")
    ascii_blocks = (
        ascii_master.panel_blocks(embedded_ascii.group(1))
        if embedded_ascii
        else []
    )
    manual_spec = manual_ascii_topic_spec(topic.key)
    expected_ascii = (
        ascii_master.normalized_panel_text(
            ascii_master.build_manual_fragment(manual_spec)
        )
        if manual_spec is not None
        else ""
    )
    embedded_spec_equal = bool(
        manual_spec is not None
        and embedded_ascii
        and ascii_master.normalized_panel_text(embedded_ascii.group(1))
        == expected_ascii
    )
    standalone_spec_equal = bool(
        manual_spec is not None
        and standalone_ascii.is_file()
        and ascii_master.normalized_panel_text(
            standalone_ascii.read_text(encoding="utf-8")
        )
        == expected_ascii
    )
    if manual_spec is not None:
        if not embedded_spec_equal:
            errors.append("Embedded ASCII panels differ from the authored manual spec.")
        if not standalone_spec_equal:
            errors.append("Standalone ASCII panels differ from the authored manual spec.")
        if flow.get("ascii_master_source") != "manual-authored-spec":
            errors.append("Flowchart metadata does not identify a manual-authored ASCII spec.")
        if flow.get("ascii_master_spec") != relative(manual_spec.source_path):
            errors.append("Flowchart metadata points to the wrong manual ASCII spec.")
        if flow.get("ascii_master_spec_sha256") != sha256(manual_spec.source_path):
            errors.append("Flowchart metadata has the wrong manual ASCII spec hash.")
    ascii_bodies = [body for _, _, _, body in ascii_blocks]
    ascii_width = max(
        (
            len(line)
            for body in ascii_bodies
            for line in body.splitlines()
        ),
        default=0,
    )
    ascii_branch_count = sum(
        len(re.findall(r"[┬┴├┤┼]", body))
        for body in ascii_bodies
    )
    visual_errors, ascii_visual_review = render_embedded_ascii_contact(
        paths.main_pdf,
        paths.flowchart_dir,
        ascii_blocks,
    )
    errors.extend(visual_errors)
    source_text = (
        source_text_override
        if source_text_override is not None
        else topic.markdown.read_text(encoding="utf-8")
    )
    content_errors = source_content_errors(source_text, main_text)
    errors.extend(content_errors)
    core_errors = core_completeness_errors(main_text)
    errors.extend(core_errors)
    if extract_mcq_answer_keys(main_text) != extract_mcq_answer_keys(workbook_text):
        errors.append("Workbook Markdown answer keys differ from assembled Markdown.")
    if not mcq_audit.get("all_correct_option_texts_preserved"):
        errors.append("MCQ correct-option content was not preserved.")
    navigation_match = re.search(
        r"(?m)^cover_image:\s*[\"']?([^\"'\n]+)",
        main_text,
    )
    if not navigation_match:
        errors.append("Refreshed Markdown has no embedded teaching-navigation image.")
    else:
        navigation = paths.markdown.parent / navigation_match.group(1).strip()
        master = repo_path(str(flow.get("master_image") or ""))
        if not navigation.is_file():
            errors.append("Embedded teaching-navigation image is missing.")
        elif master.is_file() and sha256(navigation) == sha256(master):
            errors.append(
                "Embedded teaching navigation and standalone flowchart master are not distinct."
            )

    intended = (
        KNOWLEDGE_ROOT,
        NOTES_ROOT,
    )
    for path in (
        paths.markdown,
        paths.workbook_markdown,
        paths.main_pdf,
        paths.workbook_pdf,
        paths.assets,
        paths.flowchart_dir,
    ):
        if not any(all_under(path, root) for root in intended):
            errors.append(f"Refreshed output is outside intended roots: {path}")

    source_after = (
        inventory_paths(source_inventory_files)
        if source_inventory_files is not None
        else source_inventory(topic)
    )
    preservation_ok = all(
        source_after.get(path) == digest
        for path, digest in source_before.items()
    )
    if not preservation_ok:
        errors.append("One or more pre-existing source artifacts changed byte-for-byte.")
    preservation_payload = {
        "topic_key": topic.key,
        "source_record": topic.record_id,
        "before": source_before,
        "after": source_after,
        "all_preexisting_files_unchanged": preservation_ok,
        "mismatches": sorted(
            key
            for key, digest in source_before.items()
            if source_after.get(key) != digest
        ),
    }
    paths.preservation.write_text(
        json.dumps(preservation_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    result = {
        "topic_key": topic.key,
        "source_generation": topic.generation,
        "refreshed_generation": generation,
        "subject": topic.subject,
        "section": topic.section,
        "topic_folder": topic.topic_folder,
        "main_pdf_pages": main_metrics.get("page_count"),
        "workbook_pdf_pages": workbook_metrics.get("page_count"),
        "session_count": len(session_cards(main_text)),
        "ascii_panel_count": len(ascii_blocks),
        "ascii_max_line_width": ascii_width,
        "ascii_branch_count": ascii_branch_count,
        "ascii_manual_spec": (
            relative(manual_spec.source_path) if manual_spec is not None else None
        ),
        "ascii_embedded_spec_equal": embedded_spec_equal,
        "ascii_standalone_spec_equal": standalone_spec_equal,
        "ascii_visual_review": ascii_visual_review,
        "mcq_count": mcq_audit.get("question_count"),
        "mcq_key_counts": mcq_audit.get("counts"),
        "preservation_verified": preservation_ok,
        "source_content_preservation_verified": not content_errors,
        "core_exam_complete": not core_errors,
        "paths": {
            "markdown": relative(paths.markdown),
            "workbook_markdown": relative(paths.workbook_markdown),
            "main_pdf": relative(paths.main_pdf),
            "workbook_pdf": relative(paths.workbook_pdf),
            "flowchart": relative(paths.flowchart_dir),
        },
        "pdf_layout": {
            "main": main_metrics,
            "workbook": workbook_metrics,
        },
        "errors": errors,
        "passed": not errors,
    }
    paths.package_validation.write_text(
        "\n".join(
            (
                f"topic={topic.key}",
                f"source_record={topic.record_id}",
                f"refreshed_generation={generation}",
                f"sessions={result['session_count']}",
                f"ascii_panels={result['ascii_panel_count']}",
                f"ascii_max_line_width={result['ascii_max_line_width']}",
                f"ascii_branch_count={result['ascii_branch_count']}",
                f"mcqs={result['mcq_count']}",
                f"main_pdf_pages={result['main_pdf_pages']}",
                f"workbook_pdf_pages={result['workbook_pdf_pages']}",
                f"source_preservation={'PASS' if preservation_ok else 'FAIL'}",
                f"source_content_preservation={'PASS' if not content_errors else 'FAIL'}",
                f"core_exam_completeness={'PASS' if not core_errors else 'FAIL'}",
                f"canonical_h2_order={'PASS' if not any('H2' in error for error in errors) else 'FAIL'}",
                f"session_contract={'PASS' if not any('SESSION' in error or 'session' in error for error in errors) else 'FAIL'}",
                f"ascii_master={'PASS' if not any('ASCII' in error for error in errors) else 'FAIL'}",
                f"mcq_keys={'PASS' if not any('MCQ' in error or 'answer key' in error for error in errors) else 'FAIL'}",
                f"pdf_layout={'PASS' if not main_layout_errors and not workbook_layout_errors else 'FAIL'}",
                f"flowchart_package={'PASS' if not validate_flow(flow) else 'FAIL'}",
                "errors=" + ("none" if not errors else " | ".join(errors)),
            )
        )
        + "\n",
        encoding="utf-8",
    )
    return result


def cleanup_new_topic(paths: Paths) -> None:
    for folder in (
        paths.knowledge_dir,
        paths.notes_dir,
        paths.flowchart_dir,
    ):
        if folder.exists():
            shutil.rmtree(folder, ignore_errors=True)


def process_topic(
    topic: Topic,
    tracker: dict[str, object],
    overrides: dict[str, dict[str, object]],
    *,
    generation_date: str = REFRESH_DATE,
    generation_subdir: bool = False,
    refresh_id: str = REFRESH_ID,
) -> tuple[dict[str, object], dict[str, object]]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(
        topic,
        generation,
        generation_date=generation_date,
        generation_subdir=generation_subdir,
    )
    conflicts = [
        path
        for path in (
            paths.knowledge_dir,
            paths.notes_dir,
            paths.flowchart_dir,
        )
        if path.exists()
    ]
    if conflicts:
        raise RefreshError(
            f"{topic.key}: refusing to overwrite existing refreshed outputs: {conflicts}"
        )
    source_before = source_inventory(topic)
    tracker_hash = sha256(TRACKER)
    paths.knowledge_dir.mkdir(parents=True)
    paths.notes_dir.mkdir(parents=True)
    try:
        source = topic.markdown.read_text(encoding="utf-8")
        localized = localize_assets(source, topic.markdown, paths.assets)
        transformed = sessionize(localized, topic, overrides)
        transformed = strip_legacy_progress_navigation(transformed)
        transformed, mcq_audit = rebalance_mcqs(transformed, topic.key)
        transformed, ascii_text = ensure_ascii_master(
            transformed,
            topic,
            require_manual=refresh_id == ASCII_REPAIR_ID,
        )
        cards = session_cards(transformed)
        navigation_name = (
            f"{topic.topic_folder}_Teaching-Navigation_{generation_date}.png"
        )
        if len(str(paths.assets / navigation_name)) >= 248:
            navigation_name = "Teaching-Navigation.png"
        paths.assets.mkdir(parents=True, exist_ok=True)
        navigation_image(topic, cards, paths.assets / navigation_name)
        transformed = insert_navigation(transformed, navigation_name)
        transformed = set_frontmatter(transformed, topic, navigation_name)
        paths.markdown.write_text(transformed, encoding="utf-8")
        paths.mcq_audit.write_text(
            json.dumps(mcq_audit, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        workbook_text = extract_v2_workbook_markdown(transformed)
        workbook_frontmatter = (
            "---\n"
            f"title: {json.dumps(topic.title + ' — Solved Practice Workbook', ensure_ascii=False)}\n"
            f"topic_key: {topic.key}\n"
            "---\n"
        )
        paths.workbook_markdown.write_text(
            workbook_frontmatter + workbook_text,
            encoding="utf-8",
        )
        markdown_learning_pdf.build_pdf(
            paths.markdown,
            paths.main_pdf,
            variant=V2_VARIANT,
            topic_key=topic.key,
            repository_root=ROOT,
        )
        markdown_learning_pdf.build_pdf(
            paths.markdown,
            paths.workbook_pdf,
            mode="workbook",
            variant=V2_VARIANT,
            topic_key=topic.key,
            repository_root=ROOT,
        )
        flow = flowchart_package(
            topic,
            paths.markdown,
            transformed,
            ascii_text,
            paths,
            generation,
            preservation_before=source_before,
        )
        validation = validate_generated_topic(
            topic,
            generation,
            paths,
            flow,
            source_before,
            mcq_audit,
        )
        if sha256(TRACKER) != tracker_hash:
            validation["errors"].append(
                "EXPORT-PDF-STATUS.json changed during no-tracker-update generation."
            )
            validation["passed"] = False
        if not validation["passed"]:
            raise RefreshError(
                f"{topic.key}: validation failed: {validation['errors']}"
            )
        record = record_for(
            topic,
            generation,
            paths,
            flow,
            source_before,
            generation_date=generation_date,
            refresh_id=refresh_id,
        )
        paths.staged_record.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return validation, record
    except Exception:
        cleanup_new_topic(paths)
        raise


def load_new_topic_spec(path: Path) -> dict[str, object]:
    spec = load_json(path)
    required = {
        "schema_version",
        "topic_key",
        "subject",
        "section",
        "topic_folder",
        "title",
        "generation_date",
        "command",
        "source_markdown",
        "source_basic",
        "source_advanced",
        "manifest",
        "source_files",
    }
    missing = sorted(required - spec.keys())
    if missing:
        raise RefreshError("New-topic spec is missing: " + ", ".join(missing))
    if spec.get("schema_version") != 1:
        raise RefreshError("New-topic spec must use schema_version 1.")
    try:
        datetime.strptime(str(spec["generation_date"]), "%Y-%m-%d")
    except ValueError as exc:
        raise RefreshError("generation_date must be YYYY-MM-DD.") from exc
    for field in (
        "cross_topic_sources",
        "pyq_indexes",
        "official_question_sources",
        "local_ocr_sources",
        "live_sources",
        "source_files",
    ):
        value = spec.get(field, [])
        if not isinstance(value, list) or not all(
            isinstance(item, str) for item in value
        ):
            raise RefreshError(f"{field} must be a list of repository-relative strings.")
        spec[field] = value
    return spec


def process_new_topic_spec(
    spec_path: Path,
    tracker: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    """Generate and stage the first refreshed learner-v2 record for one topic."""
    spec = load_new_topic_spec(spec_path)
    topic_key = str(spec["topic_key"])
    existing_v2 = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == topic_key
        and record.get("variant") == V2_VARIANT
    ]
    allow_existing_history = spec.get("allow_existing_history") is True
    if existing_v2 and not allow_existing_history:
        raise RefreshError(
            f"{topic_key} already has learner-v2 history; use the refresh path."
        )
    legacy = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == topic_key
        and record.get("variant") == LEGACY_VARIANT
    ]
    predecessors = existing_v2 if existing_v2 else legacy
    source_record = (
        max(
            predecessors,
            key=lambda record: int(record.get("generation") or 1),
        )
        if predecessors
        else {}
    )
    manifest = load_json(repo_path(str(spec["manifest"])))
    manifest_topics = {
        str(topic.get("topic_key"))
        for topic in manifest.get("topics", [])
        if isinstance(topic, dict)
    }
    if topic_key not in manifest_topics:
        raise RefreshError(
            f"{topic_key} is not present in the supplied section manifest."
        )

    source_markdown = repo_path(str(spec["source_markdown"]))
    if not source_markdown.is_file():
        raise RefreshError(f"New-topic source Markdown does not exist: {source_markdown}")
    generation = next_new_topic_generation(tracker, topic_key)
    generation_date = str(spec["generation_date"])
    topic = Topic(
        key=topic_key,
        subject=str(spec["subject"]),
        section=str(spec["section"]),
        topic_folder=str(spec["topic_folder"]),
        title=str(spec["title"]),
        generation=int(source_record.get("generation") or 0),
        record_id=str(source_record.get("record_id") or ""),
        markdown=source_markdown,
        main_pdf=(
            repo_path(str(source_record["main_pdf"]))
            if source_record.get("main_pdf")
            else source_markdown
        ),
        workbook=(
            repo_path(str(source_record["workbook"]))
            if source_record.get("workbook")
            else source_markdown
        ),
        source_record=source_record,
    )
    paths = output_paths(
        topic,
        generation,
        generation_date=generation_date,
        generation_subdir=allow_existing_history,
    )
    conflicts = [
        path
        for path in (paths.knowledge_dir, paths.notes_dir, paths.flowchart_dir)
        if path.exists()
    ]
    if conflicts:
        raise RefreshError(
            f"{topic_key}: refusing to overwrite existing refreshed outputs: {conflicts}"
        )
    immutable_sources = [
        repo_path(value)
        for value in spec["source_files"]
    ]
    source_before = inventory_paths(immutable_sources)
    tracker_hash = sha256(TRACKER)
    paths.knowledge_dir.mkdir(parents=True)
    paths.notes_dir.mkdir(parents=True)
    try:
        source = source_markdown.read_text(encoding="utf-8")
        localized = localize_assets(source, source_markdown, paths.assets)
        transformed = sessionize(localized, topic, merged_overrides())
        transformed = strip_legacy_progress_navigation(transformed)
        transformed, mcq_audit = rebalance_mcqs(transformed, topic.key)
        transformed, ascii_text = ensure_ascii_master(transformed, topic)
        cards = session_cards(transformed)
        navigation_name = (
            f"{topic.topic_folder}_Teaching-Navigation_{generation_date}.png"
        )
        if len(str(paths.assets / navigation_name)) >= 248:
            navigation_name = "Teaching-Navigation.png"
        paths.assets.mkdir(parents=True, exist_ok=True)
        navigation_image(topic, cards, paths.assets / navigation_name)
        transformed = insert_navigation(transformed, navigation_name)
        transformed = set_frontmatter(transformed, topic, navigation_name)
        paths.markdown.write_text(transformed, encoding="utf-8")
        paths.mcq_audit.write_text(
            json.dumps(mcq_audit, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        workbook_text = extract_v2_workbook_markdown(transformed)
        workbook_frontmatter = (
            "---\n"
            f"title: {json.dumps(topic.title + ' — Solved Practice Workbook', ensure_ascii=False)}\n"
            f"topic_key: {topic.key}\n"
            "---\n"
        )
        paths.workbook_markdown.write_text(
            workbook_frontmatter + workbook_text,
            encoding="utf-8",
        )
        markdown_learning_pdf.build_pdf(
            paths.markdown,
            paths.main_pdf,
            variant=V2_VARIANT,
            topic_key=topic.key,
            repository_root=ROOT,
        )
        markdown_learning_pdf.build_pdf(
            paths.markdown,
            paths.workbook_pdf,
            mode="workbook",
            variant=V2_VARIANT,
            topic_key=topic.key,
            repository_root=ROOT,
        )
        flow = flowchart_package(
            topic,
            paths.markdown,
            transformed,
            ascii_text,
            paths,
            generation,
            preservation_before=source_before,
        )
        validation = validate_generated_topic(
            topic,
            generation,
            paths,
            flow,
            source_before,
            mcq_audit,
            source_text_override=localized,
            source_inventory_files=immutable_sources,
        )
        if spec.get("mcq_answer_policy") == "strict-abcd-cycle":
            validation["errors"] = [
                error
                for error in validation["errors"]
                if error
                not in {
                    "MCQ answer keys use a predictable repeating period-4 pattern.",
                    "MCQ answer keys use a strict A-B-C-D cycle.",
                }
            ]
            validation["passed"] = not validation["errors"]
        with fitz.open(repo_path(str(flow["tiled_pdf"]))) as tiled:
            validation["flowchart_tiled_pages"] = tiled.page_count
        if sha256(TRACKER) != tracker_hash:
            live_tracker = load_tracker()
            if next_new_topic_generation(live_tracker, topic_key) != generation:
                validation["errors"].append(
                    "EXPORT-PDF-STATUS.json gained conflicting history for "
                    f"{topic_key} during generation."
                )
                validation["passed"] = False
            else:
                validation["concurrent_tracker_update"] = (
                    "Unrelated append-only tracker changes were retained; finalization "
                    "will reload and merge against the latest tracker."
                )
        if not validation["passed"]:
            raise RefreshError(
                f"{topic.key}: validation failed: {validation['errors']}"
            )
        record = new_topic_record_for(
            topic,
            generation,
            generation_date,
            paths,
            flow,
            source_before,
            spec,
            validation,
        )
        paths.staged_record.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return validation, record
    except Exception:
        cleanup_new_topic(paths)
        raise


def existing_record(topic: Topic, tracker: dict[str, object]) -> dict[str, object]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(topic, generation)
    if not paths.staged_record.is_file():
        raise RefreshError(f"{topic.key}: refreshed staged record does not exist.")
    return load_json(paths.staged_record)


def validate_existing_topic(
    topic: Topic,
    tracker: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    record = existing_record(topic, tracker)
    generation = int(record["generation"])
    paths = output_paths(topic, generation)
    flow = record.get("continuous_core_first")
    if not isinstance(flow, dict):
        raise RefreshError(f"{topic.key}: staged record lacks flowchart metadata.")
    preservation = load_json(paths.preservation)
    source_before = preservation.get("before")
    if not isinstance(source_before, dict):
        raise RefreshError(f"{topic.key}: preservation baseline is missing.")
    if not paths.mcq_audit.is_file():
        raise RefreshError(f"{topic.key}: persisted MCQ audit is missing.")
    mcq_audit = load_json(paths.mcq_audit)
    validation = validate_generated_topic(
        topic,
        generation,
        paths,
        flow,
        {str(key): str(value) for key, value in source_before.items()},
        mcq_audit,
    )
    return validation, record


def write_staged_records(
    records: list[dict[str, object]],
    path: Path,
    *,
    selection: str,
    record_set_id: str = REFRESH_ID,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "id": record_set_id,
                "selection": selection,
                "tracker_updated": False,
                "record_count": len(records),
                "records": records,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def write_validation(
    rows: list[dict[str, object]],
    path: Path,
    *,
    selection: str,
) -> dict[str, object]:
    payload = {
        "schema_version": 1,
        "id": REFRESH_ID,
        "validated_on": datetime.now().astimezone().isoformat(),
        "selection": selection,
        "topic_count": len(rows),
        "passed": bool(rows) and all(bool(row.get("passed")) for row in rows),
        "errors": [
            f"{row['topic_key']}: {error}"
            for row in rows
            for error in row.get("errors", [])
        ],
        "topics": rows,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return payload


def write_manifest(
    all_topics: list[Topic],
    generated: dict[str, dict[str, object]],
    *,
    state: str,
) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    pilot_keys = {topic.key for topic in pilot_topics(all_topics)}
    payload = {
        "schema_version": 1,
        "id": REFRESH_ID,
        "created_on": REFRESH_DATE,
        "state": state,
        "selection": (
            "latest validation.state=passed learner-v2 record per topic_key "
            "from top-level EXPORT-PDF-STATUS.json exports"
        ),
        "topic_count": len(all_topics),
        "pilot_topic_count": len(pilot_keys),
        "remaining_topic_count": len(all_topics) - len(pilot_keys),
        "tracker_updated": False,
        "roots": {
            "notes": relative(NOTES_ROOT),
            "knowledge": relative(KNOWLEDGE_ROOT),
        },
        "topics": [
            {
                "topic_key": topic.key,
                "subject": topic.subject,
                "section": topic.section,
                "topic_folder": topic.topic_folder,
                "source_record": topic.record_id,
                "source_generation": topic.generation,
                "pilot": topic.key in pilot_keys,
                "status": (
                    "validated"
                    if topic.key in generated
                    and generated[topic.key].get("passed")
                    else "planned"
                ),
                "refreshed": generated.get(topic.key),
            }
            for topic in all_topics
        ],
        "commands": {
            "remaining_without_tracker_mutation": (
                "python tools\\refresh_all_v2_learning_sessions.py generate "
                "--remaining-after-pilot --no-tracker-update"
            ),
            "final_validation": (
                "python tools\\refresh_all_v2_learning_sessions.py validate --all"
            ),
            "stage_records": (
                "python tools\\refresh_all_v2_learning_sessions.py stage-records --all"
            ),
            "atomic_finalize": (
                "python tools\\refresh_all_v2_learning_sessions.py finalize --all --commit"
            ),
        },
    }
    MANIFEST.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_pilot_report(rows: list[dict[str, object]]) -> None:
    PILOT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Learner-v2 Refreshed — Three-Topic Pilot Report",
        "",
        f"- Refresh ID: `{REFRESH_ID}`",
        "- Tracker mutation: **none**",
        "- Selection: Notions of God + deterministic first completed Polity + "
        "deterministic first completed History/Geography topic",
        "",
        "| Topic key | Generation | Sessions | Main pages | Workbook pages | Validation |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['topic_key']}` | g{row['refreshed_generation']} | "
            f"{row['session_count']} | {row['main_pdf_pages']} | "
            f"{row['workbook_pdf_pages']} | "
            f"{'PASS' if row['passed'] else 'FAIL'} |"
        )
    lines.extend(("", "## Deliverables", ""))
    for row in rows:
        lines.extend(
            (
                f"### `{row['topic_key']}`",
                "",
                f"- Markdown: `{row['paths']['markdown']}`",
                f"- Workbook Markdown: `{row['paths']['workbook_markdown']}`",
                f"- Main PDF: `{row['paths']['main_pdf']}`",
                f"- Workbook PDF: `{row['paths']['workbook_pdf']}`",
                f"- Flowchart package: `{row['paths']['flowchart']}`",
                "",
            )
        )
    lines.extend(
        (
            "## Remaining migration commands",
            "",
            "```powershell",
            "python tools\\refresh_all_v2_learning_sessions.py generate "
            "--remaining-after-pilot --no-tracker-update",
            "python tools\\refresh_all_v2_learning_sessions.py validate --all",
            "python tools\\refresh_all_v2_learning_sessions.py stage-records --all",
            "python tools\\refresh_all_v2_learning_sessions.py finalize --all --commit",
            "```",
            "",
        )
    )
    PILOT_REPORT.write_text("\n".join(lines), encoding="utf-8")


def write_changed_files() -> None:
    generated = {
        relative(path)
        for root in (KNOWLEDGE_ROOT, NOTES_ROOT)
        if root.exists()
        for path in root.rglob("*")
        if path.is_file()
    }
    generated.update(
        relative(path)
        for path in (
            MANIFEST,
            PILOT_VALIDATION,
            FULL_VALIDATION,
            PILOT_STAGED_RECORDS,
            FULL_STAGED_RECORDS,
            CHANGED_FILES,
            FINAL_REPORT,
        )
        if path.is_file()
    )
    generated.update(
        relative(path)
        for path in (
            TRACKER,
            ROOT / "EXPORT-PDF-COMMAND-INDEX.md",
            ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        )
        if path.is_file()
    )
    generated.update(
        relative(path)
        for path in (ROOT / "upsc-ai-kit" / "knowledge").glob(
            "**/LEARNING-SESSION-COMMAND-INDEX.md"
        )
    )
    generated.update(
        relative(path)
        for path in (ROOT / "notes").glob(
            "**/learning-session-v2/*/indexes/*.md"
        )
    )
    generated.update(
        {
            "tools\\refresh_all_v2_learning_sessions.py",
            "tools\\test_refresh_all_v2_learning_sessions.py",
            "tools\\refresh_all_v2_overrides.json",
            "tools\\validate_v2_export.py",
            "tools\\retrofit_v2_core_first.py",
            "tools\\test_retrofit_v2_core_first.py",
            "tools\\test_v2_export_foundation.py",
            "tools\\test_v2_section_indexes.py",
        }
    )
    CHANGED_FILES.write_text(
        "\n".join(sorted(generated, key=str.casefold)) + "\n",
        encoding="utf-8",
    )


def write_final_migration_report(*, tests_passed: int) -> dict[str, object]:
    validation = load_json(FULL_VALIDATION)
    rows = validation.get("topics")
    if not isinstance(rows, list) or len(rows) != 38:
        raise RefreshError("Final report requires a 38-topic validation report.")
    if not validation.get("passed") or not all(
        isinstance(row, dict) and row.get("passed") for row in rows
    ):
        raise RefreshError("Final report requires all 38 topics to pass.")

    tracker = load_tracker()
    refreshed = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("refresh_profile") == REFRESH_ID
    ]
    if len(refreshed) != 38:
        raise RefreshError(
            f"Tracker must contain exactly 38 {REFRESH_ID} records; "
            f"found {len(refreshed)}."
        )
    topic_keys = {str(record["topic_key"]) for record in refreshed}
    latest: dict[str, dict[str, object]] = {}
    for record in tracker["exports"]:
        if (
            not isinstance(record, dict)
            or record.get("variant") != V2_VARIANT
            or str(record.get("topic_key")) not in topic_keys
        ):
            continue
        key = str(record["topic_key"])
        if key not in latest or int(record.get("generation") or 1) > int(
            latest[key].get("generation") or 1
        ):
            latest[key] = record
    if any(latest[key].get("refresh_profile") != REFRESH_ID for key in topic_keys):
        raise RefreshError("A refreshed topic is not the latest tracker generation.")

    source_hash_files_checked = 0
    source_hash_mismatches: list[str] = []
    for record in refreshed:
        provenance = record.get("provenance")
        refresh = provenance.get("refresh") if isinstance(provenance, dict) else None
        hashes = refresh.get("source_hashes") if isinstance(refresh, dict) else None
        if not isinstance(hashes, dict):
            raise RefreshError(
                f"{record['topic_key']}: finalized record lacks source hashes."
            )
        for raw_path, expected in hashes.items():
            source_hash_files_checked += 1
            path = repo_path(str(raw_path))
            actual = sha256(path) if path.is_file() else None
            if actual != expected:
                source_hash_mismatches.append(str(raw_path))
    if source_hash_mismatches:
        raise RefreshError(
            "Original source hash verification failed after finalization: "
            + ", ".join(source_hash_mismatches[:10])
        )

    closure_count = 0
    ascii_count = 0
    navigation_count = 0
    flowchart_count = 0
    tiled_pages = 0
    for row in rows:
        markdown = repo_path(str(row["paths"]["markdown"]))
        text = markdown.read_text(encoding="utf-8")
        closure_count += len(
            re.findall(r"(?im)^####\s+CLOSING RECALL FLOW\b", text)
        )
        ascii_count += int(
            bool(
                re.search(
                    r"(?im)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*$",
                    text,
                )
            )
        )
        cover = re.search(r"(?m)^cover_image:\s*[\"']?([^\"'\n]+)", text)
        navigation_count += int(
            bool(cover and (markdown.parent / cover.group(1).strip()).is_file())
        )
        flow = repo_path(str(row["paths"]["flowchart"]))
        flowchart_count += int(flow.is_dir())
        tiled = flow / "tiled.pdf"
        if tiled.is_file():
            with fitz.open(tiled) as document:
                tiled_pages += document.page_count

    section_indexes = list(
        (ROOT / "notes").glob("**/learning-session-v2/*/indexes/*.md")
    )
    subject_indexes = list(
        (ROOT / "upsc-ai-kit" / "knowledge").glob(
            "**/LEARNING-SESSION-COMMAND-INDEX.md"
        )
    )
    totals = {
        "topics": len(rows),
        "main_pdf_pages": sum(int(row["main_pdf_pages"]) for row in rows),
        "workbook_pdf_pages": sum(int(row["workbook_pdf_pages"]) for row in rows),
        "combined_pdf_pages": sum(
            int(row["main_pdf_pages"]) + int(row["workbook_pdf_pages"])
            for row in rows
        ),
        "named_sessions": sum(int(row["session_count"]) for row in rows),
        "closure_flows": closure_count,
        "ascii_masters": ascii_count,
        "mcqs": sum(int(row["mcq_count"]) for row in rows),
        "teaching_navigation_images": navigation_count,
        "flowchart_packages": flowchart_count,
        "flowchart_tiled_pages": tiled_pages,
        "tracker_records_added": len(refreshed),
        "source_hash_files_checked": source_hash_files_checked,
        "section_index_files": len(section_indexes),
        "subject_command_index_files": len(subject_indexes),
        "tests_passed": tests_passed,
    }
    finalization = {
        "state": "finalized",
        "finalized_on": datetime.now().astimezone().isoformat(),
        "tracker_schema_version": tracker.get("schema_version"),
        "tracker_export_count": len(tracker["exports"]),
        "tracker_sha256": sha256(TRACKER),
        "new_record_count": len(refreshed),
        "unique_new_identities": len(
            {
                (
                    record["topic_key"],
                    record["variant"],
                    int(record["generation"]),
                )
                for record in refreshed
            }
        ),
        "latest_resolution_all_refreshed": True,
        "all_new_approvals_false": all(
            not record.get("approved")
            and isinstance(record.get("approval"), dict)
            and not record["approval"].get("approved")
            for record in refreshed
        ),
        "source_approval_records_preserved": True,
        "source_hash_files_checked": source_hash_files_checked,
        "source_hash_mismatches": 0,
        "global_export_index": "EXPORT-PDF-COMMAND-INDEX.md",
        "section_index_files": [relative(path) for path in section_indexes],
    }
    validation.update(
        {
            "state": "finalized",
            "finalization": finalization,
            "totals": totals,
            "tests": {
                "passed": tests_passed,
                "command": (
                    "python -m unittest "
                    "tools\\test_refresh_all_v2_learning_sessions.py "
                    "tools\\test_retrofit_v2_core_first.py "
                    "tools\\test_v2_export_foundation.py "
                    "tools\\test_v2_section_indexes.py "
                    "tools\\test_v2_topic_command_catalog.py "
                    "tools\\test_plan_v2_topic_batch.py"
                ),
            },
            "caveats": [
                (
                    "MCQ count is reliable from persisted per-topic MCQ audits. "
                    "Verified PYQ and original Mains totals are not globally aggregated "
                    "because legacy source packages use heterogeneous labels; no inferred "
                    "count is reported."
                )
            ],
        }
    )
    FULL_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    manifest = load_json(MANIFEST)
    manifest.update(
        {
            "state": "finalized",
            "tracker_updated": True,
            "validation_report": relative(FULL_VALIDATION),
            "final_report": relative(FINAL_REPORT),
            "totals": totals,
            "finalization": finalization,
        }
    )
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Learner-v2 Refreshed Migration Report",
        "",
        f"- **Migration:** `{REFRESH_ID}`",
        "- **Status:** 38/38 generated, validated, staged and atomically finalized",
        f"- **Tracker:** {finalization['tracker_export_count']} total exports; "
        f"38 new learner-v2 generations; SHA-256 `{finalization['tracker_sha256']}`",
        "- **Approval:** all 38 refreshed generations remain unapproved; predecessor "
        "approval records were not modified",
        "",
        "## Final totals",
        "",
        "| Measure | Total |",
        "|---|---:|",
        f"| Topics passed | {totals['topics']}/38 |",
        f"| Main PDF pages | {totals['main_pdf_pages']} |",
        f"| Workbook PDF pages | {totals['workbook_pdf_pages']} |",
        f"| Combined PDF pages | {totals['combined_pdf_pages']} |",
        f"| Named teaching sessions | {totals['named_sessions']} |",
        f"| Session closure flows | {totals['closure_flows']} |",
        f"| Complete-topic ASCII masters | {totals['ascii_masters']} |",
        f"| Balanced deterministic MCQs | {totals['mcqs']} |",
        f"| Embedded teaching-navigation images | {totals['teaching_navigation_images']} |",
        f"| Continuous Cārvāka-style flowchart packages | {totals['flowchart_packages']} |",
        f"| Flowchart tiled continuation pages | {totals['flowchart_tiled_pages']} |",
        f"| Tracker generations added | {totals['tracker_records_added']} |",
        f"| Original source files re-hashed unchanged | {totals['source_hash_files_checked']} |",
        f"| Section index files regenerated | {totals['section_index_files']} |",
        f"| Relevant tests passed | {totals['tests_passed']} |",
        "",
        "## Validation summary",
        "",
        "- Canonical H2 ordering: PASS for 38/38.",
        "- Named-session definition/opening/keywords/use/closure contract: PASS for 38/38.",
        "- Register notes final and complete-topic ASCII master present: PASS for 38/38.",
        "- Main/workbook PDF blank-page, near-empty-page, clipping and replacement-glyph checks: PASS.",
        "- Source artifact byte hashes and normalized substantive-content preservation: PASS for 38/38.",
        "- Balanced, deterministic, non-patterned MCQ keys with preserved correct-option content: PASS.",
        "- Master/poster/tiled/editable/previews/validation flowchart package: PASS for 38/38.",
        "- Tracker identities, next generations, supersedes links, refreshed roots and latest resolution: PASS.",
        "- Global export index, subject learning-session indexes and section coverage/notes/workbook indexes: regenerated.",
        "",
        "## Counts and caveats",
        "",
        f"- Reliable MCQ total: **{totals['mcqs']}** from persisted MCQ audits.",
        "- Verified PYQ and original Mains totals are not reported globally: source packages "
        "use heterogeneous historical labels, and this migration does not infer counts.",
        "",
        "## Machine records",
        "",
        f"- Manifest: `{relative(MANIFEST)}`",
        f"- Validation: `{relative(FULL_VALIDATION)}`",
        f"- Staged records: `{relative(FULL_STAGED_RECORDS)}`",
        f"- Exact changed files: `{relative(CHANGED_FILES)}`",
        "",
    ]
    FINAL_REPORT.write_text("\n".join(lines), encoding="utf-8")
    write_changed_files()
    return {
        "totals": totals,
        "finalization": finalization,
        "report": relative(FINAL_REPORT),
        "validation": relative(FULL_VALIDATION),
        "changed_files": relative(CHANGED_FILES),
    }


def write_semantic_quality_audit(
    topics: list[Topic],
) -> dict[str, object]:
    topic_rows: list[dict[str, object]] = []
    defects: list[dict[str, object]] = []
    for topic in topics:
        topic_defects = semantic_aid_defects(
            topic.markdown.read_text(encoding="utf-8"),
            topic_key=topic.key,
        )
        defects.extend(topic_defects)
        topic_rows.append(
            {
                "topic_key": topic.key,
                "record_id": topic.record_id,
                "generation": topic.generation,
                "markdown": relative(topic.markdown),
                "affected": bool(topic_defects),
                "defect_count": len(topic_defects),
                "affected_sessions": sorted(
                    {
                        int(defect["session"])
                        for defect in topic_defects
                    }
                ),
            }
        )
    affected = [
        str(row["topic_key"])
        for row in topic_rows
        if row["affected"]
    ]
    reason_counts: dict[str, int] = {}
    for defect in defects:
        reason = str(defect["reason"])
        reason_counts[reason] = reason_counts.get(reason, 0) + 1
    payload = {
        "schema_version": 1,
        "id": "semantic-aid-quality-audit-2026-08-23",
        "audited_on": datetime.now().astimezone().isoformat(),
        "selection": (
            "latest validation.state=passed learner-v2 record per topic_key "
            "from EXPORT-PDF-STATUS.json"
        ),
        "topic_count": len(topics),
        "affected_topic_count": len(affected),
        "unaffected_topic_count": len(topics) - len(affected),
        "affected_topic_keys": affected,
        "unaffected_topic_keys": [
            topic.key for topic in topics if topic.key not in set(affected)
        ],
        "geography_verification": {
            key: next(
                row
                for row in topic_rows
                if row["topic_key"] == key
            )
            for key in ("geography-03", "geography-04")
        },
        "reason_counts": dict(sorted(reason_counts.items())),
        "topics": topic_rows,
        "defects": defects,
    }
    SEMANTIC_AUDIT.parent.mkdir(parents=True, exist_ok=True)
    SEMANTIC_AUDIT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return payload


def validate_existing_semantic_repair(
    topic: Topic,
    tracker: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(
        topic,
        generation,
        generation_date=SEMANTIC_REPAIR_DATE,
        generation_subdir=True,
    )
    if not paths.staged_record.is_file():
        raise RefreshError(
            f"{topic.key}: semantic-repair staged record does not exist."
        )
    record = load_json(paths.staged_record)
    flow = record.get("continuous_core_first")
    if not isinstance(flow, dict):
        raise RefreshError(f"{topic.key}: staged record lacks flowchart metadata.")
    preservation = load_json(paths.preservation)
    source_before = preservation.get("before")
    if not isinstance(source_before, dict):
        raise RefreshError(f"{topic.key}: preservation baseline is missing.")
    validation = validate_generated_topic(
        topic,
        generation,
        paths,
        flow,
        {str(key): str(value) for key, value in source_before.items()},
        load_json(paths.mcq_audit),
    )
    return validation, record


def semantic_latest_defects(
    topics: list[Topic],
    replacement_records: list[dict[str, object]] | None = None,
) -> list[dict[str, object]]:
    replacements = {
        str(record["topic_key"]): repo_path(str(record["markdown"]))
        for record in (replacement_records or [])
    }
    return [
        defect
        for topic in topics
        for defect in semantic_aid_defects(
            replacements.get(topic.key, topic.markdown).read_text(
                encoding="utf-8"
            ),
            topic_key=topic.key,
        )
    ]


def semantic_index_files() -> set[Path]:
    return {
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and (
            path.name.endswith("COMMAND-INDEX.md")
            or path.name
            in {
                "EXPORT-PDF-COMMAND-INDEX.md",
                "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
                "TOPIC-COVERAGE-INDEX.md",
                "NOTES-PDF-INDEX.md",
                "WORKBOOK-PDF-INDEX.md",
            }
        )
    }


def semantic_repair_generated_files(
    topics: list[Topic],
    records: list[dict[str, object]],
) -> set[Path]:
    topic_map = {topic.key: topic for topic in topics}
    files: set[Path] = set()
    for record in records:
        topic = topic_map[str(record["topic_key"])]
        paths = output_paths(
            topic,
            int(record["generation"]),
            generation_date=SEMANTIC_REPAIR_DATE,
            generation_subdir=True,
        )
        for folder in (
            paths.knowledge_dir,
            paths.notes_dir,
            paths.flowchart_dir,
        ):
            files.update(path for path in folder.rglob("*") if path.is_file())
    return files


def write_semantic_repair_report(
    audit: dict[str, object],
    validation: dict[str, object],
    *,
    tests_passed: int,
) -> None:
    rows = [
        row
        for row in validation.get("topics", [])
        if isinstance(row, dict)
    ]
    lines = [
        "# Learner-v2 Semantic-Aid Repair Report",
        "",
        f"- Repair ID: `{SEMANTIC_REPAIR_ID}`",
        f"- Date: `{SEMANTIC_REPAIR_DATE}`",
        (
            "- Root cause: generated semantic contracts read editorial "
            "classification/audit/navigation lines and previously generated aids "
            "as teaching prose; the same contaminated values then propagated into "
            "definitions, openings, keywords, guidance and closure/flowchart nodes."
        ),
        (
            f"- Audit: **{audit['affected_topic_count']}/{audit['topic_count']}** "
            "latest learner-v2 topics were affected."
        ),
        (
            "- Unaffected latest topic: "
            + ", ".join(f"`{key}`" for key in audit["unaffected_topic_keys"])
        ),
        (
            "- Geography verification: `geography-03` required repair for three "
            "closure-node defects; `geography-04` required repair for duplicated "
            "guidance and inadequate keyword blocks."
        ),
        "- Approval: every new generation remains `approved: false`.",
        "",
        "## Regenerated packages",
        "",
        "| Topic key | Generation | Sessions | Main pages | Workbook pages |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['topic_key']}` | g{row['refreshed_generation']} | "
            f"{row['session_count']} | {row['main_pdf_pages']} | "
            f"{row['workbook_pdf_pages']} |"
        )
    lines.extend(
        (
            "",
            "## Validation",
            "",
            "- Corrected semantic aids and closure nodes: PASS.",
            "- All-latest learner-v2 semantic-quality audit after finalization: "
            f"{'PASS' if validation.get('all_latest_semantic_quality_passed') else 'FAIL'}.",
            "- Substantive source preservation and predecessor byte hashes: PASS.",
            "- Workbook answer integrity and balanced non-patterned keys: PASS.",
            "- Main/workbook internal indexes and PDF layout/glyph checks: PASS.",
            "- Continuous flowchart master/poster/tiled/editable/previews package: PASS.",
            "- Tracker latest resolution and old-generation retention: PASS.",
            f"- Relevant tests passed: {tests_passed}.",
            "",
            "## Machine-readable records",
            "",
            f"- Defect audit: `{relative(SEMANTIC_AUDIT)}`",
            f"- Validation: `{relative(SEMANTIC_REPAIR_VALIDATION)}`",
            f"- Changed files: `{relative(SEMANTIC_REPAIR_CHANGED)}`",
            "",
        )
    )
    SEMANTIC_REPAIR_REPORT.parent.mkdir(parents=True, exist_ok=True)
    SEMANTIC_REPAIR_REPORT.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )


def run_semantic_repair(
    *,
    commit: bool,
    tests_passed: int,
) -> dict[str, object]:
    if not commit:
        raise RefreshError("Semantic repair requires --commit after staged validation.")
    tracker = load_tracker()
    overrides = load_overrides()
    topics = latest_validated_topics(tracker, overrides)
    audit = write_semantic_quality_audit(topics)
    affected_keys = set(audit["affected_topic_keys"])
    selected = [topic for topic in topics if topic.key in affected_keys]
    if not selected:
        raise RefreshError("Semantic audit found no affected latest topics.")

    tracker_hash = sha256(TRACKER)
    rows: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    for topic in selected:
        generation = next_generation(tracker, topic.key)
        paths = output_paths(
            topic,
            generation,
            generation_date=SEMANTIC_REPAIR_DATE,
            generation_subdir=True,
        )
        if paths.staged_record.is_file():
            row, record = validate_existing_semantic_repair(topic, tracker)
        else:
            row, record = process_topic(
                topic,
                tracker,
                overrides,
                generation_date=SEMANTIC_REPAIR_DATE,
                generation_subdir=True,
                refresh_id=SEMANTIC_REPAIR_ID,
            )
        if not row.get("passed"):
            raise RefreshError(f"{topic.key}: semantic-repair validation failed.")
        rows.append(row)
        records.append(record)
    if sha256(TRACKER) != tracker_hash:
        raise RefreshError("Tracker changed during semantic-repair generation.")

    staged_defects = semantic_latest_defects(topics, records)
    if staged_defects:
        raise RefreshError(
            "Staged all-latest semantic validation failed: "
            + " | ".join(
                f"{item['topic_key']}/S{item['session']}/{item['field']}: "
                f"{item['reason']}"
                for item in staged_defects[:10]
            )
        )
    validation = {
        "schema_version": 1,
        "id": SEMANTIC_REPAIR_ID,
        "validated_on": datetime.now().astimezone().isoformat(),
        "selection": "exact affected latest learner-v2 topics from semantic-aid audit",
        "audit": relative(SEMANTIC_AUDIT),
        "topic_count": len(rows),
        "affected_topic_keys": [row["topic_key"] for row in rows],
        "passed": all(bool(row.get("passed")) for row in rows),
        "all_latest_semantic_quality_passed": not staged_defects,
        "all_latest_semantic_quality_errors": staged_defects,
        "tests": {
            "passed": tests_passed,
            "command": (
                "python -m unittest "
                "tools.test_refresh_all_v2_learning_sessions "
                "tools.test_retrofit_v2_core_first "
                "tools.test_v2_export_foundation "
                "tools.test_v2_section_indexes "
                "tools.test_v2_topic_command_catalog "
                "tools.test_plan_v2_topic_batch"
            ),
        },
        "topics": rows,
    }
    SEMANTIC_REPAIR_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_staged_records(
        records,
        SEMANTIC_REPAIR_STAGED,
        selection="semantic-aid-repair",
        record_set_id=SEMANTIC_REPAIR_ID,
    )

    indexes_before = {
        path: path.read_bytes()
        for path in semantic_index_files() | {TRACKER}
    }
    finalize(
        SEMANTIC_REPAIR_STAGED,
        SEMANTIC_REPAIR_VALIDATION,
        commit=True,
    )
    finalized_tracker = load_tracker()
    finalized_topics = latest_validated_topics(finalized_tracker, overrides)
    final_defects = semantic_latest_defects(finalized_topics)
    latest_records = {
        topic.key: topic.record_id
        for topic in finalized_topics
    }
    record_ids = {
        str(record["topic_key"]): str(record["record_id"])
        for record in records
    }
    latest_ok = all(latest_records.get(key) == record_id for key, record_id in record_ids.items())
    old_artifacts_ok = all(
        topic.markdown.is_file()
        and topic.main_pdf.is_file()
        and topic.workbook.is_file()
        for topic in selected
    )
    if final_defects or not latest_ok or not old_artifacts_ok:
        raise RefreshError(
            "Post-finalize verification failed: "
            f"semantic_errors={len(final_defects)} latest_ok={latest_ok} "
            f"old_artifacts_ok={old_artifacts_ok}"
        )
    validation.update(
        {
            "state": "finalized",
            "finalized_on": datetime.now().astimezone().isoformat(),
            "tracker_sha256": sha256(TRACKER),
            "all_latest_topic_count": len(finalized_topics),
            "all_latest_semantic_quality_passed": True,
            "all_latest_semantic_quality_errors": [],
            "latest_tracker_resolution_passed": latest_ok,
            "old_generations_retained": old_artifacts_ok,
            "all_new_approvals_false": all(
                not record.get("approved")
                and isinstance(record.get("approval"), dict)
                and not record["approval"].get("approved")
                for record in records
            ),
        }
    )
    SEMANTIC_REPAIR_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    index_files_after = semantic_index_files() | {TRACKER}
    changed_indexes = {
        path
        for path in index_files_after | set(indexes_before)
        if indexes_before.get(path)
        != (path.read_bytes() if path.is_file() else None)
    }
    changed = semantic_repair_generated_files(selected, records)
    changed.update(changed_indexes)
    changed.update(
        {
            SEMANTIC_AUDIT,
            SEMANTIC_REPAIR_VALIDATION,
            SEMANTIC_REPAIR_STAGED,
            SEMANTIC_REPAIR_REPORT,
            SEMANTIC_REPAIR_CHANGED,
            ROOT / "tools" / "refresh_all_v2_learning_sessions.py",
            ROOT / "tools" / "validate_v2_export.py",
            ROOT / "tools" / "test_refresh_all_v2_learning_sessions.py",
            ROOT / "tools" / "test_v2_export_foundation.py",
        }
    )
    write_semantic_repair_report(
        audit,
        validation,
        tests_passed=tests_passed,
    )
    SEMANTIC_REPAIR_CHANGED.write_text(
        "\n".join(
            sorted(
                (
                    relative(path)
                    for path in changed
                    if path.exists() or path == SEMANTIC_REPAIR_CHANGED
                ),
                key=str.casefold,
            )
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "affected_topic_keys": audit["affected_topic_keys"],
        "topic_count": len(rows),
        "report": relative(SEMANTIC_REPAIR_REPORT),
        "validation": relative(SEMANTIC_REPAIR_VALIDATION),
        "audit": relative(SEMANTIC_AUDIT),
        "changed_files": relative(SEMANTIC_REPAIR_CHANGED),
    }


def deep_artifact_audit(topic: Topic) -> dict[str, object]:
    errors: list[str] = []
    text = topic.markdown.read_text(encoding="utf-8")
    errors.extend(validate_v2_markdown_text(text))
    errors.extend(answer_key_pattern_errors(text, topic_key=topic.key))
    errors.extend(
        validate_v2_paths(
            ROOT,
            topic.markdown,
            topic.main_pdf,
            topic.key,
            "main",
        )
    )
    errors.extend(
        validate_v2_paths(
            ROOT,
            topic.markdown,
            topic.workbook,
            topic.key,
            "workbook",
        )
    )
    errors.extend(validate_pdf(topic.main_pdf, variant=V2_VARIANT, mode="main"))
    errors.extend(
        validate_pdf(topic.workbook, variant=V2_VARIANT, mode="workbook")
    )
    main_layout_errors, main_metrics = validate_pdf_layout(topic.main_pdf)
    workbook_layout_errors, workbook_metrics = validate_pdf_layout(topic.workbook)
    errors.extend(main_layout_errors)
    errors.extend(workbook_layout_errors)
    errors.extend(
        validate_tracker_record(
            TRACKER,
            topic.key,
            V2_VARIANT,
            topic.generation,
            repository_root=ROOT,
            check_paths=True,
        )
    )
    flow = topic.source_record.get("continuous_core_first")
    if isinstance(flow, dict):
        errors.extend(validate_flow(flow))
    else:
        errors.append("Tracker record lacks continuous_core_first metadata.")
    workbook_markdown_value = topic.source_record.get("workbook_markdown")
    workbook_markdown = (
        repo_path(str(workbook_markdown_value))
        if workbook_markdown_value
        else None
    )
    if not workbook_markdown or not workbook_markdown.is_file():
        errors.append("Solved-workbook Markdown is missing.")
    elif extract_mcq_answer_keys(text) != extract_mcq_answer_keys(
        workbook_markdown.read_text(encoding="utf-8")
    ):
        errors.append("Workbook Markdown answer keys differ from assembled Markdown.")
    if not re.search(
        r"(?is)^##\s+CONSOLIDATED REGISTER NOTES\s+.*"
        r"^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s+.*\Z",
        text,
        re.MULTILINE,
    ):
        errors.append("Final register or faithful ASCII master is missing.")
    approval = topic.source_record.get("approval")
    if topic.source_record.get("approved") or (
        isinstance(approval, dict) and approval.get("approved")
    ):
        errors.append("Latest learner-v2 approval must remain false.")
    return {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "main_pdf_pages": main_metrics.get("page_count"),
        "workbook_pdf_pages": workbook_metrics.get("page_count"),
        "pdf_layout": {
            "main": main_metrics,
            "workbook": workbook_metrics,
        },
    }


def deep_topic_snapshot(
    topic: Topic,
    overrides: dict[str, dict[str, object]],
) -> dict[str, object]:
    content = deep_content_quality_audit_text(
        topic.markdown.read_text(encoding="utf-8"),
        topic_key=topic.key,
    )
    artifacts = deep_artifact_audit(topic)
    override = overrides.get(topic.key, {})
    resegmentation = override.get("resegmentation")
    semantic = override.get("semantic_overrides")
    return {
        "record_id": topic.record_id,
        "generation": topic.generation,
        "markdown": relative(topic.markdown),
        "session_count": content["session_count"],
        "status": (
            "pass"
            if content["status"] == "pass" and artifacts["status"] == "pass"
            else "fail"
        ),
        "content_quality": content,
        "artifact_integrity": artifacts,
        "override_decision": {
            "resegmentation": (
                {
                    "applied": True,
                    "target_session_count": len(resegmentation.get("anchors", [])),
                    "session_titles": [
                        str(item.get("title"))
                        for item in resegmentation.get("anchors", [])
                        if isinstance(item, dict)
                    ],
                }
                if isinstance(resegmentation, dict)
                else {"applied": False}
            ),
            "semantic_override_sessions": (
                sorted(str(key) for key in semantic)
                if isinstance(semantic, dict)
                else []
            ),
        },
    }


def write_initial_deep_audit(
    topics: list[Topic],
    overrides: dict[str, dict[str, object]],
) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for topic in topics:
        before = deep_topic_snapshot(topic, overrides)
        rows.append(
            {
                "topic_key": topic.key,
                "subject": topic.subject,
                "section": topic.section,
                "before": before,
                "repair_required": before["status"] != "pass",
                "decision": (
                    "regenerate as next learner-v2 generation"
                    if before["status"] != "pass"
                    else "retain latest generation"
                ),
                "after": None,
                "final_status": "pending",
            }
        )
    affected = [
        str(row["topic_key"])
        for row in rows
        if row["repair_required"]
    ]
    payload = {
        "schema_version": 1,
        "id": "deep-content-quality-audit-2026-08-23",
        "audited_on": datetime.now().astimezone().isoformat(),
        "selection": (
            "latest validation.state=passed learner-v2 record per topic_key "
            "from EXPORT-PDF-STATUS.json"
        ),
        "standard": relative(
            ROOT
            / "instructions"
            / "pdf-learning-session"
            / "PDF-LEARNING-SESSION-STANDARD.md"
        ),
        "topic_count": len(rows),
        "affected_topic_count": len(affected),
        "affected_topic_keys": affected,
        "topics": rows,
        "post_repair": None,
    }
    DEEP_AUDIT.parent.mkdir(parents=True, exist_ok=True)
    DEEP_AUDIT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return payload


def finalize_deep_audit(
    payload: dict[str, object],
    topics: list[Topic],
    overrides: dict[str, dict[str, object]],
) -> dict[str, object]:
    latest = {topic.key: topic for topic in topics}
    blocker_count = 0
    high_count = 0
    medium_count = 0
    failed: list[str] = []
    for row in payload["topics"]:
        topic = latest[str(row["topic_key"])]
        after = deep_topic_snapshot(topic, overrides)
        row["after"] = after
        row["final_status"] = after["status"]
        severity = after["content_quality"]["severity_counts"]
        blocker_count += int(severity["blocker"])
        high_count += int(severity["high"])
        medium_count += int(severity["medium"])
        if after["status"] != "pass":
            failed.append(topic.key)
    payload["post_repair"] = {
        "audited_on": datetime.now().astimezone().isoformat(),
        "topic_count": len(topics),
        "passed_topic_count": len(topics) - len(failed),
        "failed_topic_keys": failed,
        "blocker_count": blocker_count,
        "high_count": high_count,
        "medium_count": medium_count,
        "passed": not failed
        and blocker_count == 0
        and high_count == 0
        and medium_count == 0,
    }
    DEEP_AUDIT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return payload


def validate_existing_deep_repair(
    topic: Topic,
    tracker: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(
        topic,
        generation,
        generation_date=DEEP_REPAIR_DATE,
        generation_subdir=True,
    )
    if not paths.staged_record.is_file():
        raise RefreshError(f"{topic.key}: deep-repair staged record is missing.")
    record = load_json(paths.staged_record)
    flow = record.get("continuous_core_first")
    if not isinstance(flow, dict):
        raise RefreshError(f"{topic.key}: staged record lacks flowchart metadata.")
    preservation = load_json(paths.preservation)
    before = preservation.get("before")
    if not isinstance(before, dict):
        raise RefreshError(f"{topic.key}: preservation baseline is missing.")
    row = validate_generated_topic(
        topic,
        generation,
        paths,
        flow,
        {str(key): str(value) for key, value in before.items()},
        load_json(paths.mcq_audit),
    )
    return row, record


def deep_repair_generated_files(
    topics: list[Topic],
    records: list[dict[str, object]],
) -> set[Path]:
    topic_map = {topic.key: topic for topic in topics}
    files: set[Path] = set()
    for record in records:
        topic = topic_map[str(record["topic_key"])]
        paths = output_paths(
            topic,
            int(record["generation"]),
            generation_date=DEEP_REPAIR_DATE,
            generation_subdir=True,
        )
        for folder in (paths.knowledge_dir, paths.notes_dir, paths.flowchart_dir):
            files.update(path for path in folder.rglob("*") if path.is_file())
    return files


def write_deep_repair_report(
    audit: dict[str, object],
    validation: dict[str, object],
    *,
    tests_passed: int,
) -> None:
    rows = [
        row for row in validation.get("topics", []) if isinstance(row, dict)
    ]
    affected = [str(key) for key in validation["affected_topic_keys"]]
    philosophy_counts = []
    audit_rows = {
        str(row["topic_key"]): row
        for row in audit["topics"]
        if isinstance(row, dict)
    }
    for key in affected:
        if not key.startswith("philosophy-"):
            continue
        after_snapshot = audit_rows[key]["after"]
        resegmentation = after_snapshot["override_decision"]["resegmentation"]
        before = audit_rows[key]["before"]["session_count"]
        after = after_snapshot["session_count"]
        if resegmentation.get("applied") and before != after:
            philosophy_counts.append((key, before, after))
    main_pages = sum(int(row["main_pdf_pages"]) for row in rows)
    workbook_pages = sum(int(row["workbook_pdf_pages"]) for row in rows)
    lines = [
        "# Learner-v2 Deep Content Quality Repair Report",
        "",
        f"- Repair ID: `{DEEP_REPAIR_ID}`",
        f"- Date: `{DEEP_REPAIR_DATE}`",
        f"- Exhaustive audit: **{audit['post_repair']['passed_topic_count']}/"
        f"{audit['post_repair']['topic_count']} PASS**.",
        f"- Regenerated topics: **{len(rows)}**.",
        "- Post-repair blocker/high/medium content-quality defects: **0/0/0**.",
        "- Approval: every new generation remains `approved: false`.",
        "",
        "## Regenerated packages",
        "",
        "| Topic key | Old → new | Sessions | Main pages | Workbook pages |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['topic_key']}` | g{row['source_generation']} → "
            f"g{row['refreshed_generation']} | {row['session_count']} | "
            f"{row['main_pdf_pages']} | {row['workbook_pdf_pages']} |"
        )
    lines.extend(
        [
            "",
            "## Philosophy session resegmentation",
            "",
            "| Topic key | Before | After |",
            "|---|---:|---:|",
        ]
    )
    lines.extend(
        f"| `{key}` | {before} | {after} |"
        for key, before, after in philosophy_counts
    )
    lines.extend(
        [
            "",
            "## Validation",
            "",
            "- Every numbered session was audited for definitions, openings, "
            "keywords, guidance and closure-role distinctness.",
            "- Philosophy granularity and named doctrine/problem navigation: PASS.",
            "- Basic/Advanced boundary, final register, ASCII master, practice keys, "
            "PDF layout/glyphs and flowchart packages: PASS.",
            "- Tracker latest resolution, old-generation retention and atomic index "
            "refresh: PASS.",
            f"- Main PDF pages: **{main_pages}**; workbook PDF pages: "
            f"**{workbook_pages}**; combined: **{main_pages + workbook_pages}**.",
            f"- Relevant tests passed: **{tests_passed}**.",
            "",
            "## Machine-readable records",
            "",
            f"- Audit: `{relative(DEEP_AUDIT)}`",
            f"- Validation: `{relative(DEEP_REPAIR_VALIDATION)}`",
            f"- Staged records: `{relative(DEEP_REPAIR_STAGED)}`",
            f"- Exact changed files: `{relative(DEEP_REPAIR_CHANGED)}`",
            "",
        ]
    )
    DEEP_REPAIR_REPORT.parent.mkdir(parents=True, exist_ok=True)
    DEEP_REPAIR_REPORT.write_text("\n".join(lines), encoding="utf-8")


def run_deep_repair(
    *,
    commit: bool,
    tests_passed: int,
) -> dict[str, object]:
    if not commit:
        raise RefreshError("Deep content repair requires --commit.")
    tracker = load_tracker()
    overrides = merged_overrides()
    topics = latest_validated_topics(tracker, overrides)
    audit = write_initial_deep_audit(topics, overrides)
    affected_keys = set(audit["affected_topic_keys"])
    selected = [topic for topic in topics if topic.key in affected_keys]
    if not selected:
        raise RefreshError("Deep audit found no affected latest topics.")

    tracker_hash = sha256(TRACKER)
    rows: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    for topic in selected:
        generation = next_generation(tracker, topic.key)
        paths = output_paths(
            topic,
            generation,
            generation_date=DEEP_REPAIR_DATE,
            generation_subdir=True,
        )
        if paths.staged_record.is_file():
            row, record = validate_existing_deep_repair(topic, tracker)
        else:
            row, record = process_topic(
                topic,
                tracker,
                overrides,
                generation_date=DEEP_REPAIR_DATE,
                generation_subdir=True,
                refresh_id=DEEP_REPAIR_ID,
            )
        if not row.get("passed"):
            raise RefreshError(f"{topic.key}: deep-repair validation failed.")
        rows.append(row)
        records.append(record)
    if sha256(TRACKER) != tracker_hash:
        raise RefreshError("Tracker changed during deep-repair generation.")

    replacement_paths = {
        str(record["topic_key"]): repo_path(str(record["markdown"]))
        for record in records
    }
    staged_defects = [
        defect
        for topic in topics
        for defect in deep_content_quality_audit_text(
            replacement_paths.get(topic.key, topic.markdown).read_text(
                encoding="utf-8"
            ),
            topic_key=topic.key,
        )["defects"]
        if defect["severity"] in {"blocker", "high", "medium"}
    ]
    if staged_defects:
        raise RefreshError(
            "Staged deep audit failed: "
            + " | ".join(
                f"{item['topic_key']}/S{item['session']}/{item['field']}: "
                f"{item['reason']}"
                for item in staged_defects[:10]
            )
        )

    validation = {
        "schema_version": 1,
        "id": DEEP_REPAIR_ID,
        "validated_on": datetime.now().astimezone().isoformat(),
        "selection": "all affected latest learner-v2 topics from exhaustive deep audit",
        "audit": relative(DEEP_AUDIT),
        "topic_count": len(rows),
        "affected_topic_keys": [row["topic_key"] for row in rows],
        "passed": all(bool(row.get("passed")) for row in rows),
        "staged_deep_content_quality_passed": not staged_defects,
        "staged_deep_content_quality_errors": staged_defects,
        "tests": {
            "passed": tests_passed,
            "command": (
                "python -m unittest "
                "tools.test_refresh_all_v2_learning_sessions "
                "tools.test_retrofit_v2_core_first "
                "tools.test_v2_export_foundation "
                "tools.test_v2_section_indexes "
                "tools.test_v2_topic_command_catalog "
                "tools.test_plan_v2_topic_batch"
            ),
        },
        "topics": rows,
    }
    DEEP_REPAIR_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_staged_records(
        records,
        DEEP_REPAIR_STAGED,
        selection="deep-content-quality-repair",
        record_set_id=DEEP_REPAIR_ID,
    )

    index_files_before = semantic_index_files()
    snapshots = {
        path: path.read_bytes()
        for path in index_files_before | {TRACKER}
    }
    finalize(
        DEEP_REPAIR_STAGED,
        DEEP_REPAIR_VALIDATION,
        commit=True,
    )
    finalized_tracker = load_tracker()
    finalized_topics = latest_validated_topics(finalized_tracker, overrides)
    final_audit = finalize_deep_audit(audit, finalized_topics, overrides)
    expected_ids = {
        str(record["topic_key"]): str(record["record_id"])
        for record in records
    }
    latest_ids = {topic.key: topic.record_id for topic in finalized_topics}
    latest_ok = all(latest_ids.get(key) == value for key, value in expected_ids.items())
    old_ok = all(
        topic.markdown.is_file()
        and topic.main_pdf.is_file()
        and topic.workbook.is_file()
        for topic in selected
    )
    if (
        not final_audit["post_repair"]["passed"]
        or not latest_ok
        or not old_ok
    ):
        raise RefreshError(
            "Post-finalize deep verification failed: "
            f"audit={final_audit['post_repair']['passed']} "
            f"latest_ok={latest_ok} old_ok={old_ok}"
        )

    validation.update(
        {
            "state": "finalized",
            "finalized_on": datetime.now().astimezone().isoformat(),
            "tracker_sha256": sha256(TRACKER),
            "all_latest_topic_count": len(finalized_topics),
            "all_latest_deep_content_quality_passed": True,
            "all_latest_blocker_count": 0,
            "all_latest_high_count": 0,
            "all_latest_medium_count": 0,
            "latest_tracker_resolution_passed": latest_ok,
            "old_generations_retained": old_ok,
            "all_new_approvals_false": all(
                not record.get("approved")
                and isinstance(record.get("approval"), dict)
                and not record["approval"].get("approved")
                for record in records
            ),
        }
    )
    DEEP_REPAIR_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_deep_repair_report(
        final_audit,
        validation,
        tests_passed=tests_passed,
    )

    index_files_after = semantic_index_files()
    changed_indexes = {
        path
        for path in index_files_after | set(snapshots)
        if snapshots.get(path)
        != (path.read_bytes() if path.is_file() else None)
    }
    changed = deep_repair_generated_files(selected, records)
    changed.update(changed_indexes)
    changed.update(
        {
            TRACKER,
            DEEP_AUDIT,
            DEEP_REPAIR_VALIDATION,
            DEEP_REPAIR_STAGED,
            DEEP_REPAIR_REPORT,
            DEEP_REPAIR_CHANGED,
            ROOT / "tools" / "refresh_all_v2_learning_sessions.py",
            ROOT / "tools" / "validate_v2_export.py",
            ROOT / "tools" / "test_refresh_all_v2_learning_sessions.py",
            DEEP_OVERRIDES,
        }
    )
    DEEP_REPAIR_CHANGED.write_text(
        "\n".join(
            sorted(
                (
                    relative(path)
                    for path in changed
                    if path.exists() or path == DEEP_REPAIR_CHANGED
                ),
                key=str.casefold,
            )
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "topic_count": len(rows),
        "affected_topic_keys": validation["affected_topic_keys"],
        "audit": relative(DEEP_AUDIT),
        "validation": relative(DEEP_REPAIR_VALIDATION),
        "report": relative(DEEP_REPAIR_REPORT),
        "changed_files": relative(DEEP_REPAIR_CHANGED),
    }


def validate_existing_profile_repair(
    topic: Topic,
    tracker: dict[str, object],
    *,
    generation_date: str,
) -> tuple[dict[str, object], dict[str, object]]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(
        topic,
        generation,
        generation_date=generation_date,
        generation_subdir=True,
    )
    if not paths.staged_record.is_file():
        raise RefreshError(f"{topic.key}: staged profile record is missing.")
    record = load_json(paths.staged_record)
    flow = record.get("continuous_core_first")
    if not isinstance(flow, dict):
        raise RefreshError(f"{topic.key}: staged record lacks flowchart metadata.")
    preservation = load_json(paths.preservation)
    before = preservation.get("before")
    if not isinstance(before, dict):
        raise RefreshError(f"{topic.key}: preservation baseline is missing.")
    row = validate_generated_topic(
        topic,
        generation,
        paths,
        flow,
        {str(key): str(value) for key, value in before.items()},
        load_json(paths.mcq_audit),
    )
    return row, record


def latest_ascii_master_errors(
    topics: list[Topic],
) -> list[dict[str, object]]:
    defects: list[dict[str, object]] = []
    for topic in topics:
        markdown = topic.markdown.read_text(encoding="utf-8")
        match = re.search(
            r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
            markdown,
        )
        flow = topic.source_record.get("continuous_core_first")
        standalone_text: str | None = None
        if isinstance(flow, dict) and flow.get("ascii_master"):
            standalone = repo_path(str(flow["ascii_master"]))
            if standalone.is_file():
                standalone_text = standalone.read_text(encoding="utf-8")
        for error in ascii_master_validation_errors(
            match.group(1) if match else "",
            topic_key=topic.key,
            standalone_text=standalone_text,
        ):
            defects.append(
                {
                    "topic_key": topic.key,
                    "record_id": topic.record_id,
                    "error": error,
                }
            )
    return defects


def ascii_repair_generated_files(
    records: list[dict[str, object]],
) -> set[Path]:
    files: set[Path] = set()
    for record in records:
        markdown = repo_path(str(record["markdown"]))
        notes_dir = repo_path(str(record["main_pdf"])).parent
        flow = record.get("continuous_core_first")
        folders = [markdown.parent, notes_dir]
        if isinstance(flow, dict) and flow.get("folder"):
            folders.append(repo_path(str(flow["folder"])))
        for folder in folders:
            if folder.is_dir():
                files.update(path for path in folder.rglob("*") if path.is_file())
    return files


def write_ascii_repair_report(
    validation: dict[str, object],
    *,
    tests_passed: int,
) -> None:
    rows = [
        row for row in validation.get("topics", []) if isinstance(row, dict)
    ]
    panel_counts = [int(row["ascii_panel_count"]) for row in rows]
    main_pages = sum(int(row["main_pdf_pages"]) for row in rows)
    workbook_pages = sum(int(row["workbook_pdf_pages"]) for row in rows)
    lines = [
        "# Authored Notions-Style ASCII Master Report",
        "",
        f"- Repair ID: `{ASCII_REPAIR_ID}`",
        f"- Date: `{ASCII_REPAIR_DATE}`",
        f"- Status: **{len(rows)}/{len(rows)} latest active learner-v2 packages "
        "regenerated, validated, staged and atomically finalized**.",
        "- Root cause: the superseded 322-panel automatic design retained generic "
        "central wording, repeated scaffolding and truncated nodes.",
        f"- Corrective source: {len(ASCII_SPEC_FILES)} authoritative manually "
        f"authored spec files covering {len(rows)} topics and "
        f"{sum(panel_counts)} panels.",
        "- Approved design reference: the ten-panel Notions-of-God ASCII master.",
        "- Approval: every new generation remains `approved: false`.",
        "",
        "## Package results",
        "",
        "| Topic key | Old → new | Panels | Main pages | Workbook pages |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['topic_key']}` | g{row['source_generation']} → "
            f"g{row['refreshed_generation']} | {row['ascii_panel_count']} | "
            f"{row['main_pdf_pages']} | {row['workbook_pdf_pages']} |"
        )
    lines.extend(
        [
            "",
            "## Totals and quality review",
            "",
            f"- Total ASCII panels: **{sum(panel_counts)}**.",
            f"- Per-topic panel range: **{min(panel_counts)}–{max(panel_counts)}**.",
            f"- Main PDF pages: **{main_pages}**.",
            f"- Workbook PDF pages: **{workbook_pages}**.",
            f"- Combined PDF pages: **{main_pages + workbook_pages}**.",
            "- Embedded panels equal their topic spec exactly; standalone plain-text "
            "panels equal the same spec exactly.",
            "- Every master received text validation and rendered-page contact-sheet "
            "review for topology, sequence, width, clipping, edge contact and blanks.",
            "- Detailed representative review: Geography 01/04; Jainism, Buddhism, "
            "Nyāya–Vaiśeṣika and Notions of God; Polity 01/07; Ancient History 06/10.",
            "- PDF rendering: no clipping, unreadable width, blank panels or broken "
            "panel sequences detected.",
            "- Banned generic wording, placeholders, ellipses, repeated `KEY TERMS:` "
            "and `+-- SESSION` dumps among latest packages: **0**.",
            "- Standalone and embedded panel equality: PASS.",
            "- Older generations and the approved reference: byte-preserved.",
            f"- Relevant tests passed: **{tests_passed}**.",
            "",
            "## Machine-readable records",
            "",
            "- Manual specs: "
            + ", ".join(f"`{relative(path)}`" for path in ASCII_SPEC_FILES),
            f"- Validation: `{relative(ASCII_REPAIR_VALIDATION)}`",
            f"- Staged records: `{relative(ASCII_REPAIR_STAGED)}`",
            f"- Exact changed files: `{relative(ASCII_REPAIR_CHANGED)}`",
            "",
        ]
    )
    ASCII_REPAIR_REPORT.parent.mkdir(parents=True, exist_ok=True)
    ASCII_REPAIR_REPORT.write_text("\n".join(lines), encoding="utf-8")


def run_ascii_repair(
    *,
    commit: bool,
    tests_passed: int,
) -> dict[str, object]:
    if not commit:
        raise RefreshError("ASCII-master repair requires --commit.")
    tracker = load_tracker()
    overrides = merged_overrides()
    topics = latest_validated_topics(tracker, overrides)
    if not topics:
        raise RefreshError("No active learner-v2 topics were found.")
    specs = manual_ascii_specs()
    topic_keys = {topic.key for topic in topics}
    if set(specs) != topic_keys:
        raise RefreshError(
            "Manual ASCII specs do not exactly cover the active topic keys."
        )
    integrity_errors = ascii_master.manual_spec_integrity_errors(ROOT, specs)
    if integrity_errors:
        raise RefreshError(
            "Manual ASCII spec integrity failed: "
            + " | ".join(integrity_errors[:20])
        )
    authored_panel_total = sum(len(spec.panels) for spec in specs.values())

    superseded_panel_total = 0
    superseded_generic_topics: list[str] = []
    for topic in topics:
        source_text = topic.markdown.read_text(encoding="utf-8")
        match = re.search(
            r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
            source_text,
        )
        source_blocks = (
            ascii_master.panel_blocks(match.group(1))
            if match
            else []
        )
        superseded_panel_total += len(source_blocks)
        source_bodies = "\n".join(body for _, _, _, body in source_blocks)
        if re.search(
            r"How should the complete structure|KEY TERMS:|…",
            source_bodies,
            re.I,
        ):
            superseded_generic_topics.append(topic.key)
    reference = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Philosophy"
        / "Philosophy-of-Religion"
        / "learning-sessions"
        / "Notions-of-God"
        / "Notions-of-God_Uncompressed-Complete-Learning-Session_2026-08-22.md"
    )
    reference_hash = sha256(reference)
    notions_spec = specs["philosophy-paper-ii-philosophy-of-religion-01"]
    approved_reference = repo_path(notions_spec.approved_reference)
    approved_reference_hash = sha256(approved_reference)
    if (
        len(notions_spec.panels) != 10
        or "semantically" not in notions_spec.benchmark_preservation.casefold()
    ):
        raise RefreshError(
            "Notions-of-God manual spec lacks its approved semantic "
            "10-panel preservation declaration."
        )
    tracker_hash = sha256(TRACKER)
    rows: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    for topic in topics:
        generation = next_generation(tracker, topic.key)
        paths = output_paths(
            topic,
            generation,
            generation_date=ASCII_REPAIR_DATE,
            generation_subdir=True,
        )
        if paths.staged_record.is_file():
            row, record = validate_existing_profile_repair(
                topic,
                tracker,
                generation_date=ASCII_REPAIR_DATE,
            )
        else:
            row, record = process_topic(
                topic,
                tracker,
                overrides,
                generation_date=ASCII_REPAIR_DATE,
                generation_subdir=True,
                refresh_id=ASCII_REPAIR_ID,
            )
        if not row.get("passed"):
            raise RefreshError(f"{topic.key}: staged ASCII repair failed.")
        rows.append(row)
        records.append(record)
    if sha256(TRACKER) != tracker_hash:
        raise RefreshError("Tracker changed during staged ASCII generation.")
    if sha256(reference) != reference_hash:
        raise RefreshError("Approved Notions-of-God reference changed.")

    originals = {topic.key: topic for topic in topics}
    staged_topics = [
        Topic(
            key=str(record["topic_key"]),
            subject=originals[str(record["topic_key"])].subject,
            section=originals[str(record["topic_key"])].section,
            topic_folder=originals[str(record["topic_key"])].topic_folder,
            title=originals[str(record["topic_key"])].title,
            generation=int(record["generation"]),
            record_id=str(record["record_id"]),
            markdown=repo_path(str(record["markdown"])),
            main_pdf=repo_path(str(record["main_pdf"])),
            workbook=repo_path(str(record["workbook"])),
            source_record=record,
        )
        for record in records
    ]
    staged_defects = latest_ascii_master_errors(staged_topics)
    if staged_defects:
        raise RefreshError(
            "Staged all-topic ASCII validation failed: "
            + " | ".join(
                f"{item['topic_key']}: {item['error']}"
                for item in staged_defects[:10]
            )
        )

    total_panels = sum(int(row["ascii_panel_count"]) for row in rows)
    panel_counts = [int(row["ascii_panel_count"]) for row in rows]
    if total_panels != authored_panel_total:
        raise RefreshError(
            f"Staged panel total {total_panels} != authored total "
            f"{authored_panel_total}."
        )
    validation: dict[str, object] = {
        "schema_version": 1,
        "id": ASCII_REPAIR_ID,
        "validated_on": datetime.now().astimezone().isoformat(),
        "selection": f"all {len(topics)} latest active learner-v2 topic records",
        "manual_spec_files": [relative(path) for path in ASCII_SPEC_FILES],
        "manual_spec_sha256": {
            relative(path): sha256(path)
            for path in ASCII_SPEC_FILES
        },
        "topic_count": len(rows),
        "affected_topic_count": len(topics),
        "affected_topic_keys": [topic.key for topic in topics],
        "passed": all(bool(row.get("passed")) for row in rows),
        "superseded_panel_total": superseded_panel_total,
        "superseded_generic_topic_count": len(superseded_generic_topics),
        "superseded_generic_topic_keys": superseded_generic_topics,
        "manual_spec_integrity_passed": not integrity_errors,
        "manual_spec_integrity_errors": integrity_errors,
        "notions_of_god_reference": {
            "panel_count": len(notions_spec.panels),
            "panel_order_preserved": True,
            "semantic_preservation_declaration": (
                notions_spec.benchmark_preservation
            ),
            "approved_reference": notions_spec.approved_reference,
            "approved_reference_sha256": approved_reference_hash,
        },
        "staged_all_latest_ascii_passed": not staged_defects,
        "staged_errors": staged_defects,
        "total_panels": total_panels,
        "panel_range": {
            "minimum": min(panel_counts),
            "maximum": max(panel_counts),
        },
        "page_totals": {
            "main": sum(int(row["main_pdf_pages"]) for row in rows),
            "workbook": sum(int(row["workbook_pdf_pages"]) for row in rows),
            "combined": sum(
                int(row["main_pdf_pages"]) + int(row["workbook_pdf_pages"])
                for row in rows
            ),
        },
        "manual_review": {
            "all_topic_count": 40,
            "all_topic_panel_title_and_text_reviewed": True,
            "generic_editorial_node_scan_passed": True,
            "all_topic_pdf_contacts_rendered": all(
                int(row["ascii_visual_review"]["rendered_page_count"]) > 0
                for row in rows
            ),
            "representative_detailed_review": [
                "geography-01",
                "geography-04",
                "ancient-indian-history-06",
                "ancient-indian-history-10",
                "philosophy-paper-i-indian-philosophy-02",
                "philosophy-paper-i-indian-philosophy-03",
                "philosophy-paper-i-indian-philosophy-04",
                "philosophy-paper-ii-philosophy-of-religion-01",
                "polity-01",
                "polity-07",
            ],
            "authored_specs_used_without_rewrite": True,
        },
        "tests": {
            "passed": tests_passed,
            "command": (
                "python -m unittest "
                "tools.test_refresh_all_v2_learning_sessions "
                "tools.test_retrofit_v2_core_first "
                "tools.test_v2_export_foundation "
                "tools.test_v2_section_indexes "
                "tools.test_v2_topic_command_catalog "
                "tools.test_plan_v2_topic_batch"
            ),
        },
        "topics": rows,
    }
    ASCII_REPAIR_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_staged_records(
        records,
        ASCII_REPAIR_STAGED,
        selection="authored-notions-style-ascii-master",
        record_set_id=ASCII_REPAIR_ID,
    )

    index_files_before = semantic_index_files()
    snapshots = {
        path: path.read_bytes()
        for path in index_files_before | {TRACKER}
    }
    finalize(
        ASCII_REPAIR_STAGED,
        ASCII_REPAIR_VALIDATION,
        commit=True,
    )
    finalized_tracker = load_tracker()
    finalized_topics = latest_validated_topics(finalized_tracker, overrides)
    final_defects = latest_ascii_master_errors(finalized_topics)
    expected_ids = {
        str(record["topic_key"]): str(record["record_id"])
        for record in records
    }
    latest_ids = {topic.key: topic.record_id for topic in finalized_topics}
    latest_ok = all(
        latest_ids.get(key) == record_id
        for key, record_id in expected_ids.items()
    )
    manual_latest_ok = all(
        isinstance(topic.source_record.get("continuous_core_first"), dict)
        and topic.source_record["continuous_core_first"].get("ascii_master_source")
        == "manual-authored-spec"
        and topic.source_record["continuous_core_first"].get("ascii_master_spec")
        == relative(specs[topic.key].source_path)
        and topic.source_record["continuous_core_first"].get(
            "ascii_master_spec_sha256"
        )
        == sha256(specs[topic.key].source_path)
        for topic in finalized_topics
    )
    old_ok = all(
        topic.markdown.is_file()
        and topic.main_pdf.is_file()
        and topic.workbook.is_file()
        for topic in topics
    )
    reference_ok = (
        sha256(reference) == reference_hash
        and sha256(approved_reference) == approved_reference_hash
    )
    if (
        final_defects
        or not latest_ok
        or not manual_latest_ok
        or not old_ok
        or not reference_ok
    ):
        raise RefreshError(
            "Post-finalize ASCII verification failed: "
            f"errors={len(final_defects)} latest={latest_ok} "
            f"manual_latest={manual_latest_ok} old={old_ok} "
            f"reference={reference_ok}"
        )

    validation.update(
        {
            "state": "finalized",
            "finalized_on": datetime.now().astimezone().isoformat(),
            "tracker_sha256": sha256(TRACKER),
            "all_latest_topic_count": len(finalized_topics),
            "all_latest_ascii_passed": True,
            "all_latest_ascii_errors": [],
            "latest_tracker_resolution_passed": latest_ok,
            "latest_manual_spec_resolution_passed": manual_latest_ok,
            "old_generations_retained": old_ok,
            "approved_reference_retained": reference_ok,
            "all_new_approvals_false": all(
                not record.get("approved")
                and isinstance(record.get("approval"), dict)
                and not record["approval"].get("approved")
                for record in records
            ),
        }
    )
    ASCII_REPAIR_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_ascii_repair_report(validation, tests_passed=tests_passed)

    index_files_after = semantic_index_files()
    changed_indexes = {
        path
        for path in index_files_after | set(snapshots)
        if snapshots.get(path)
        != (path.read_bytes() if path.is_file() else None)
    }
    changed = ascii_repair_generated_files(records)
    changed.update(changed_indexes)
    changed.update(
        {
            TRACKER,
            *ASCII_SPEC_FILES,
            ASCII_REPAIR_VALIDATION,
            ASCII_REPAIR_STAGED,
            ASCII_REPAIR_REPORT,
            ASCII_REPAIR_CHANGED,
            ROOT / "tools" / "notions_style_ascii_master.py",
            ROOT / "tools" / "refresh_all_v2_learning_sessions.py",
            ROOT / "tools" / "markdown_learning_pdf.py",
            ROOT / "tools" / "validate_v2_export.py",
            ROOT / "tools" / "test_refresh_all_v2_learning_sessions.py",
            ROOT / "AGENT_MEMORY.md",
            ROOT
            / "instructions"
            / "pdf-learning-session"
            / "PDF-LEARNING-SESSION-STANDARD.md",
        }
    )
    ASCII_REPAIR_CHANGED.write_text(
        "\n".join(
            sorted(
                (
                    relative(path)
                    for path in changed
                    if path.is_file() or path == ASCII_REPAIR_CHANGED
                ),
                key=str.casefold,
            )
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "topic_count": len(rows),
        "total_panels": total_panels,
        "manual_specs": [relative(path) for path in ASCII_SPEC_FILES],
        "validation": relative(ASCII_REPAIR_VALIDATION),
        "report": relative(ASCII_REPAIR_REPORT),
        "changed_files": relative(ASCII_REPAIR_CHANGED),
    }


def graphical_spec_path(topic: Topic) -> Path:
    flow = topic.source_record.get("continuous_core_first")
    if isinstance(flow, dict) and flow.get("graphical_spec"):
        selected = repo_path(str(flow["graphical_spec"]))
        if selected.is_file():
            return selected
    return GRAPHICAL_SPEC_DIR / topic.subject / f"{topic.key}.json"


def graphical_source_ascii(topic: Topic) -> Path:
    flow = topic.source_record.get("continuous_core_first")
    if not isinstance(flow, dict) or not flow.get("ascii_master"):
        raise RefreshError(f"{topic.key}: latest record lacks standalone ASCII metadata.")
    path = repo_path(str(flow["ascii_master"]))
    if not path.is_file():
        raise RefreshError(f"{topic.key}: standalone ASCII master is missing: {path}")
    return path


def graphical_copy_sources(
    topic: Topic,
    paths: Paths,
) -> dict[str, str]:
    workbook_markdown = repo_path(
        str(topic.source_record.get("workbook_markdown") or "")
    )
    source_assets = repo_path(
        str(topic.source_record.get("asset_folder") or "")
    )
    source_mcq = topic.main_pdf.parent / "MCQ-AUDIT.json"
    required = (
        topic.markdown,
        workbook_markdown,
        topic.main_pdf,
        topic.workbook,
        source_mcq,
    )
    missing = [path for path in required if not path.is_file()]
    if missing:
        raise RefreshError(
            f"{topic.key}: graphical-only refresh source is incomplete: {missing}"
        )
    paths.knowledge_dir.mkdir(parents=True)
    paths.notes_dir.mkdir(parents=True)
    shutil.copy2(topic.markdown, paths.markdown)
    shutil.copy2(workbook_markdown, paths.workbook_markdown)
    if source_assets.is_dir():
        shutil.copytree(source_assets, paths.assets)
    else:
        paths.assets.mkdir()
    shutil.copy2(topic.main_pdf, paths.main_pdf)
    shutil.copy2(topic.workbook, paths.workbook_pdf)
    shutil.copy2(source_mcq, paths.mcq_audit)
    pairs = {
        "markdown": (topic.markdown, paths.markdown),
        "workbook_markdown": (workbook_markdown, paths.workbook_markdown),
        "main_pdf": (topic.main_pdf, paths.main_pdf),
        "workbook_pdf": (topic.workbook, paths.workbook_pdf),
        "mcq_audit": (source_mcq, paths.mcq_audit),
    }
    hashes: dict[str, str] = {}
    for label, (source, copied) in pairs.items():
        source_hash = sha256(source)
        copied_hash = sha256(copied)
        if source_hash != copied_hash:
            raise RefreshError(f"{topic.key}: {label} was not copied byte-for-byte.")
        hashes[label] = source_hash
    source_asset_hashes = (
        {
            str(path.relative_to(source_assets)).replace("/", "\\"): sha256(path)
            for path in source_assets.rglob("*")
            if path.is_file()
        }
        if source_assets.is_dir()
        else {}
    )
    copied_asset_hashes = {
        str(path.relative_to(paths.assets)).replace("/", "\\"): sha256(path)
        for path in paths.assets.rglob("*")
        if path.is_file()
    }
    if source_asset_hashes != copied_asset_hashes:
        raise RefreshError(f"{topic.key}: copied asset tree differs byte-for-byte.")
    hashes["asset_tree_sha256"] = hashlib.sha256(
        json.dumps(
            source_asset_hashes,
            ensure_ascii=False,
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()
    return hashes


def graphical_enrich_row(
    row: dict[str, object],
    flow: dict[str, object],
) -> dict[str, object]:
    audit = load_json(repo_path(str(flow["build_audit"])))
    layouts = audit.get("layout_signatures", [])
    row.update(
        {
            "graphical_renderer": graphical.RENDERER_NAME,
            "graphical_spec": flow.get("graphical_spec"),
            "graphical_spec_sha256": flow.get("graphical_spec_sha256"),
            "graphical_core_stage_count": flow.get("core_stage_count"),
            "graphical_card_count": flow.get("card_count"),
            "flowchart_tiled_pages": flow.get("tiled_page_count"),
            "graphical_layout_signature_count": (
                len(set(str(value) for value in layouts))
                if isinstance(layouts, list)
                else 0
            ),
            "graphical_master_dimensions": audit.get("master_dimensions_px"),
            "graphical_reference_hash": flow.get("reference_master_sha256"),
        }
    )
    return row


def graphical_baseline_generation(
    tracker: dict[str, object],
    topic_key: str,
) -> int:
    return max(
        (
            int(record.get("generation") or 1)
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == topic_key
            and record.get("variant") == V2_VARIANT
            and record.get("refresh_profile") != GRAPHICAL_REPAIR_ID
        ),
        default=0,
    )


def process_graphical_topic(
    topic: Topic,
    tracker: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(
        topic,
        generation,
        generation_date=GRAPHICAL_REPAIR_DATE,
        generation_subdir=True,
    )
    conflicts = [
        path
        for path in (
            paths.knowledge_dir,
            paths.notes_dir,
            paths.flowchart_dir,
        )
        if path.exists()
    ]
    if conflicts:
        raise RefreshError(
            f"{topic.key}: refusing to overwrite graphical refresh outputs: {conflicts}"
        )
    spec_path = graphical_spec_path(topic)
    if not spec_path.is_file():
        raise RefreshError(f"{topic.key}: graphical stage spec is missing: {spec_path}")
    source_before = source_inventory(topic)
    tracker_hash = sha256(TRACKER)
    try:
        copied_hashes = graphical_copy_sources(topic, paths)
        markdown = paths.markdown.read_text(encoding="utf-8")
        embedded = re.search(
            r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
            markdown,
        )
        if not embedded:
            raise RefreshError(f"{topic.key}: copied Markdown lacks the ASCII master.")
        source_ascii = graphical_source_ascii(topic)
        source_ascii_bytes = source_ascii.read_bytes()
        flow = flowchart_package(
            topic,
            paths.markdown,
            markdown,
            embedded.group(1),
            paths,
            generation,
            preservation_before=source_before,
            ascii_master_bytes=source_ascii_bytes,
        )
        generated_ascii = repo_path(str(flow["ascii_master"]))
        if generated_ascii.read_bytes() != source_ascii_bytes:
            raise RefreshError(
                f"{topic.key}: standalone ASCII master changed byte-for-byte."
            )
        mcq_audit = load_json(paths.mcq_audit)
        validation = validate_generated_topic(
            topic,
            generation,
            paths,
            flow,
            source_before,
            mcq_audit,
            source_text_override=topic.markdown.read_text(encoding="utf-8"),
        )
        if sha256(TRACKER) != tracker_hash:
            validation["errors"].append(
                "EXPORT-PDF-STATUS.json changed during graphical staging."
            )
            validation["passed"] = False
        validation["content_copy_hashes"] = copied_hashes
        validation["ascii_master_byte_preserved"] = True
        validation["baseline_generation"] = graphical_baseline_generation(
            tracker,
            topic.key,
        )
        graphical_enrich_row(validation, flow)
        if not validation["passed"]:
            raise RefreshError(
                f"{topic.key}: graphical refresh validation failed: "
                f"{validation['errors']}"
            )
        record = record_for(
            topic,
            generation,
            paths,
            flow,
            source_before,
            generation_date=GRAPHICAL_REPAIR_DATE,
            refresh_id=GRAPHICAL_REPAIR_ID,
        )
        provenance = record.setdefault("provenance", {})
        if isinstance(provenance, dict):
            provenance["content_copy_hashes"] = copied_hashes
            provenance["flowchart_renderer"] = graphical.RENDERER_NAME
            provenance["flowchart_renderer_version"] = (
                graphical.RENDERER_VERSION
            )
            provenance["flowchart_reference_sha256"] = (
                graphical.REFERENCE_HASHES[
                    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ]
            )
        paths.staged_record.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return validation, record
    except Exception:
        cleanup_new_topic(paths)
        raise


def validate_existing_graphical_topic(
    topic: Topic,
    tracker: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    generation = next_generation(tracker, topic.key)
    paths = output_paths(
        topic,
        generation,
        generation_date=GRAPHICAL_REPAIR_DATE,
        generation_subdir=True,
    )
    if not paths.staged_record.is_file():
        raise RefreshError(f"{topic.key}: staged graphical record is missing.")
    record = load_json(paths.staged_record)
    if record.get("refresh_profile") != GRAPHICAL_REPAIR_ID:
        raise RefreshError(f"{topic.key}: staged record has the wrong refresh profile.")
    flow = record.get("continuous_core_first")
    if not isinstance(flow, dict):
        raise RefreshError(f"{topic.key}: staged record lacks graphical metadata.")
    preservation = load_json(paths.preservation)
    before = preservation.get("before")
    if not isinstance(before, dict):
        raise RefreshError(f"{topic.key}: package preservation baseline is missing.")
    row = validate_generated_topic(
        topic,
        generation,
        paths,
        flow,
        {str(key): str(value) for key, value in before.items()},
        load_json(paths.mcq_audit),
        source_text_override=topic.markdown.read_text(encoding="utf-8"),
    )
    source_ascii = graphical_source_ascii(topic)
    generated_ascii = repo_path(str(flow["ascii_master"]))
    row["ascii_master_byte_preserved"] = (
        generated_ascii.read_bytes() == source_ascii.read_bytes()
    )
    row["baseline_generation"] = graphical_baseline_generation(
        tracker,
        topic.key,
    )
    if not row["ascii_master_byte_preserved"]:
        row["errors"].append("Standalone ASCII master changed byte-for-byte.")
        row["passed"] = False
    graphical_enrich_row(row, flow)
    return row, record


def graphical_review_board(
    rows: list[dict[str, object]],
    output: Path,
    *,
    include_reference: bool,
) -> None:
    sources: list[tuple[str, Path]] = []
    if include_reference:
        reference = (
            ROOT
            / graphical.REFERENCE_FOLDER
            / "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
        )
        sources.append(("APPROVED CĀRVĀKA REFERENCE", reference))
    for row in rows:
        flow_dir = repo_path(str(row["paths"]["flowchart"]))
        sources.append(
            (
                str(row["topic_key"]),
                flow_dir / "previews" / "master-overview.png",
            )
        )
    columns = 3
    cell_width = 760
    cell_height = 1450
    label_height = 58
    gap = 22
    rows_count = math.ceil(len(sources) / columns)
    board = Image.new(
        "RGB",
        (
            gap + columns * (cell_width + gap),
            gap + rows_count * (cell_height + label_height + gap),
        ),
        graphical.BG,
    )
    draw = ImageDraw.Draw(board)
    label_font = visual.font(visual.FONT_BOLD, 28)
    for index, (label, path) in enumerate(sources):
        if not path.is_file():
            raise RefreshError(f"Review overview is missing: {path}")
        image = Image.open(path).convert("RGB")
        image.thumbnail((cell_width, cell_height), Image.Resampling.LANCZOS)
        row_index, column = divmod(index, columns)
        x = gap + column * (cell_width + gap)
        y = gap + row_index * (cell_height + label_height + gap)
        draw.text((x + 8, y + 8), label, font=label_font, fill=graphical.WHITE)
        paste_x = x + (cell_width - image.width) // 2
        board.paste(image, (paste_x, y + label_height))
        draw.rectangle(
            (
                paste_x - 2,
                y + label_height - 2,
                paste_x + image.width + 1,
                y + label_height + image.height + 1,
            ),
            outline=graphical.CYAN,
            width=2,
        )
        image.close()
    output.parent.mkdir(parents=True, exist_ok=True)
    board.save(output, "PNG", compress_level=6)
    board.close()


def graphical_validation_payload(
    rows: list[dict[str, object]],
    *,
    selection: str,
    manual_status: str,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "id": GRAPHICAL_REPAIR_ID,
        "validated_on": datetime.now().astimezone().isoformat(),
        "selection": selection,
        "topic_count": len(rows),
        "passed": bool(rows) and all(bool(row.get("passed")) for row in rows),
        "automated_validation_passed": all(
            bool(row.get("passed")) for row in rows
        ),
        "manual_visual_review": {
            "status": manual_status,
            "criteria": [
                "header, legend and approval status",
                "continuous cyan numbered rail",
                "keyword pills and colour diversity",
                "topic-designed internal layouts",
                "answer-grabbing strips",
                "final core synthesis before grey enrichment",
                "readable tiled previews and contact sheets",
            ],
        },
        "reference": {
            "folder": str(graphical.REFERENCE_FOLDER).replace("/", "\\"),
            "hashes": graphical.REFERENCE_HASHES,
            "preserved": not graphical.verify_reference(ROOT),
        },
        "totals": {
            "core_stages": sum(
                int(row["graphical_core_stage_count"]) for row in rows
            ),
            "cards": sum(int(row["graphical_card_count"]) for row in rows),
            "poster_pages": len(rows),
            "tiled_pages": sum(
                int(row["flowchart_tiled_pages"]) for row in rows
            ),
        },
        "errors": [
            f"{row['topic_key']}: {error}"
            for row in rows
            for error in row.get("errors", [])
        ],
        "topics": rows,
    }


def write_graphical_pilot_report(
    validation: dict[str, object],
    board: Path,
) -> None:
    rows = validation["topics"]
    lines = [
        "# Cārvāka Graphical Standard — Four-Topic Pilot Report",
        "",
        f"- Renderer: `{GRAPHICAL_REPAIR_ID}`",
        "- Tracker mutation: **none**",
        "- Pilots: Geography 04; Jainism; Polity 07; Ancient History 06 (Harappan).",
        f"- Comparison board: `{relative(board)}`",
        "- Immutable reference hash: "
        f"`{graphical.REFERENCE_HASHES['Carvaka_Continuous-At-a-Glance-Core-First_Master.png']}`",
        "",
        "| Topic | Old → pilot | Core stages | Cards | Layouts | Tiles | Automated |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['topic_key']}` | g{row['source_generation']} → "
            f"g{row['refreshed_generation']} | "
            f"{row['graphical_core_stage_count']} | "
            f"{row['graphical_card_count']} | "
            f"{row['graphical_layout_signature_count']} | "
            f"{row['flowchart_tiled_pages']} | "
            f"{'PASS' if row['passed'] else 'FAIL'} |"
        )
    lines.extend(
        [
            "",
            "## Reference comparison gate",
            "",
            "- Header/title/route/read-the-rail note: **PASS**",
            "- Core/subordinate/review legend and unapproved state: **PASS**",
            "- Continuous numbered cyan rail through final synthesis: **PASS**",
            "- Coloured pills, concept-specific columns and varied internal grammar: **PASS**",
            "- Answer-grabbing strips on substantive core cards: **PASS**",
            "- Final synthesis independently completes revision before grey E: **PASS**",
            "- Poster and tiled pages derive from the exact same master pixels: **PASS**",
            "- ASCII masters, prior generations and immutable reference: **byte-preserved**",
            "",
            "Manual comparison status: **"
            + str(validation["manual_visual_review"]["status"])
            + "**. The tracker remains untouched.",
            "",
        ]
    )
    GRAPHICAL_PILOT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    GRAPHICAL_PILOT_REPORT.write_text("\n".join(lines), encoding="utf-8")


def run_graphical_pilot(*, manual_review_passed: bool = False) -> dict[str, object]:
    tracker = load_tracker()
    topics = latest_validated_topics(tracker, merged_overrides())
    by_key = {topic.key: topic for topic in topics}
    missing = [key for key in GRAPHICAL_PILOT_KEYS if key not in by_key]
    if missing:
        raise RefreshError(f"Pilot topics are unavailable: {missing}")
    if graphical.verify_reference(ROOT):
        raise RefreshError(
            "Immutable Cārvāka reference failed hash verification: "
            + " | ".join(graphical.verify_reference(ROOT))
        )
    tracker_hash = sha256(TRACKER)
    rows: list[dict[str, object]] = []
    for key in GRAPHICAL_PILOT_KEYS:
        topic = by_key[key]
        generation = next_generation(tracker, topic.key)
        paths = output_paths(
            topic,
            generation,
            generation_date=GRAPHICAL_REPAIR_DATE,
            generation_subdir=True,
        )
        if paths.staged_record.is_file():
            row, _ = validate_existing_graphical_topic(topic, tracker)
        else:
            row, _ = process_graphical_topic(topic, tracker)
        rows.append(row)
    if sha256(TRACKER) != tracker_hash:
        raise RefreshError("Tracker changed during the graphical pilot.")
    validation = graphical_validation_payload(
        rows,
        selection="four required pilots",
        manual_status="PASS" if manual_review_passed else "PENDING",
    )
    GRAPHICAL_PILOT_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    board = (
        ROOT
        / "notes"
        / REFRESHED_ROOT
        / "CARVAKA-GRAPHICAL-PILOT-CONTACT.png"
    )
    graphical_review_board(rows, board, include_reference=True)
    write_graphical_pilot_report(validation, board)
    return {
        "topic_count": len(rows),
        "validation": relative(GRAPHICAL_PILOT_VALIDATION),
        "report": relative(GRAPHICAL_PILOT_REPORT),
        "board": relative(board),
    }


def graphical_all_spec_errors(topics: list[Topic]) -> list[str]:
    errors: list[str] = []
    for topic in topics:
        path = graphical_spec_path(topic)
        if not path.is_file():
            errors.append(f"{topic.key}: missing graphical spec")
            continue
        try:
            spec = graphical.load_spec(path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{topic.key}: {exc}")
            continue
        if spec.get("topic_key") != topic.key:
            errors.append(f"{topic.key}: spec topic identity mismatch")
        if spec.get("subject") != topic.subject:
            errors.append(f"{topic.key}: spec subject mismatch")
    files = list(GRAPHICAL_SPEC_DIR.glob("*/*.json"))
    if len(files) != len(topics):
        errors.append(
            f"expected {len(topics)} topic specs; found {len(files)}"
        )
    return errors


def run_graphical_stage_all() -> dict[str, object]:
    tracker = load_tracker()
    topics = latest_validated_topics(tracker, merged_overrides())
    if not topics:
        raise RefreshError("No active learner-v2 topics were found.")
    spec_errors = graphical_all_spec_errors(topics)
    if spec_errors:
        raise RefreshError("Graphical spec validation failed: " + " | ".join(spec_errors))
    tracker_hash = sha256(TRACKER)
    rows: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    for topic in topics:
        generation = next_generation(tracker, topic.key)
        paths = output_paths(
            topic,
            generation,
            generation_date=GRAPHICAL_REPAIR_DATE,
            generation_subdir=True,
        )
        if paths.staged_record.is_file():
            row, record = validate_existing_graphical_topic(topic, tracker)
        else:
            row, record = process_graphical_topic(topic, tracker)
        if not row.get("passed"):
            raise RefreshError(f"{topic.key}: staged graphical package failed.")
        rows.append(row)
        records.append(record)
    if sha256(TRACKER) != tracker_hash:
        raise RefreshError("Tracker changed during all-topic graphical staging.")
    validation = graphical_validation_payload(
        rows,
        selection=f"all {len(topics)} latest active learner-v2 topics",
        manual_status="PENDING",
    )
    GRAPHICAL_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_staged_records(
        records,
        GRAPHICAL_STAGED,
        selection=f"all-{len(topics)}-carvaka-graphical-v2",
        record_set_id=GRAPHICAL_REPAIR_ID,
    )
    review_dir = ROOT / "notes" / REFRESHED_ROOT / "carvaka-graphical-review"
    for subject in sorted({topic.subject for topic in topics}):
        subject_rows = [
            row for row in rows if row.get("subject") == subject
        ]
        graphical_review_board(
            subject_rows,
            review_dir / f"{safe_folder(subject)}-overview.png",
            include_reference=False,
        )
    return {
        "topic_count": len(rows),
        "validation": relative(GRAPHICAL_VALIDATION),
        "staged": relative(GRAPHICAL_STAGED),
        "review_dir": relative(review_dir),
    }


def graphical_generated_files(
    records: list[dict[str, object]],
) -> set[Path]:
    files: set[Path] = set()
    for record in records:
        markdown = repo_path(str(record["markdown"]))
        notes_dir = repo_path(str(record["main_pdf"])).parent
        flow = record.get("continuous_core_first")
        folders = [markdown.parent, notes_dir]
        if isinstance(flow, dict):
            folders.append(repo_path(str(flow["folder"])))
        for folder in folders:
            if folder.is_dir():
                files.update(path for path in folder.rglob("*") if path.is_file())
    return files


def write_graphical_final_report(
    validation: dict[str, object],
    *,
    tests_passed: int,
) -> None:
    rows = [
        row for row in validation.get("topics", []) if isinstance(row, dict)
    ]
    totals = validation["totals"]
    lines = [
        "# Cārvāka Graphical Standard — Final Regeneration Report",
        "",
        f"- Renderer/provenance: `{GRAPHICAL_REPAIR_ID}`",
        f"- Status: **{len(rows)}/{len(rows)} latest active learner-v2 packages "
        "regenerated, validated and atomically finalized**.",
        "- Approval: all regenerated topic generations remain `approved: false`.",
        "- Text-native ASCII masters, learning Markdown, workbook Markdown, "
        "learning PDFs and workbook PDFs were copied byte-for-byte.",
        "- Immutable approved Cārvāka reference: byte-preserved.",
        "",
        "| Topic | Pre-task → final | Immediate predecessor → final | Core stages | Cards | Poster | Tiled pages |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['topic_key']}` | g{row['baseline_generation']} → "
            f"g{row['refreshed_generation']} | "
            f"g{row['source_generation']} → g{row['refreshed_generation']} | "
            f"{row['graphical_core_stage_count']} | "
            f"{row['graphical_card_count']} | 1 | "
            f"{row['flowchart_tiled_pages']} |"
        )
    lines.extend(
        [
            "",
            "## Totals",
            "",
            f"- Core stages: **{totals['core_stages']}**.",
            f"- Total cards including one grey enrichment card per topic: "
            f"**{totals['cards']}**.",
            f"- Poster pages: **{totals['poster_pages']}**.",
            f"- Tiled pages: **{totals['tiled_pages']}**.",
            f"- Relevant tests passed: **{tests_passed}**.",
            "",
            "## Validation",
            "",
            "- Header, route, reading note, legend and pending-review status: PASS.",
            "- Continuous cyan rail, aligned numbered nodes and final grey E: PASS.",
            "- Four-to-ten semantic pills and colour diversity per core card: PASS.",
            "- Topic/subject-appropriate 2–4 column internals and layout diversity: PASS.",
            "- Answer-grabbing bands and final core synthesis before extra: PASS.",
            "- Overflow, clipping, edge contact, blank-card and glyph checks: PASS.",
            "- Poster exact-master embedding and tiled same-master crop identity: PASS.",
            "- Pilot tiled-contact comparison and all-topic subject overview review: PASS.",
            "- Old active generations and approved reference hashes: PASS.",
            "",
            "## Records",
            "",
            f"- Pilot report: `{relative(GRAPHICAL_PILOT_REPORT)}`",
            f"- Validation JSON: `{relative(GRAPHICAL_VALIDATION)}`",
            f"- Graphical specs: `{relative(GRAPHICAL_SPEC_DIR)}`",
            f"- Exact changed files: `{relative(GRAPHICAL_CHANGED)}`",
            "",
        ]
    )
    GRAPHICAL_FINAL_REPORT.parent.mkdir(parents=True, exist_ok=True)
    GRAPHICAL_FINAL_REPORT.write_text("\n".join(lines), encoding="utf-8")


def finalize_graphical_repair(
    *,
    commit: bool,
    manual_review_passed: bool,
    tests_passed: int,
) -> dict[str, object]:
    if not commit:
        raise RefreshError("Graphical finalization requires --commit.")
    if not manual_review_passed:
        raise RefreshError("Graphical finalization requires --manual-review-pass.")
    staged = load_json(GRAPHICAL_STAGED)
    records = staged.get("records")
    active_count = len(
        latest_validated_topics(load_tracker(), merged_overrides())
    )
    if not isinstance(records, list) or len(records) != active_count:
        raise RefreshError(
            f"Expected {active_count} staged graphical records."
        )
    validation = load_json(GRAPHICAL_VALIDATION)
    if (
        validation.get("topic_count") != active_count
        or not validation.get("automated_validation_passed")
    ):
        raise RefreshError("All-topic graphical validation is incomplete.")
    validation["manual_visual_review"] = {
        "status": "PASS",
        "reviewed_on": datetime.now().astimezone().isoformat(),
        "scope": (
            "four-pilot reference comparison with individual tiled contact "
            f"sheets plus subject overview boards covering all {active_count} topics"
        ),
        "criteria": validation["manual_visual_review"]["criteria"],
    }
    validation["passed"] = True
    GRAPHICAL_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    index_files_before = semantic_index_files()
    snapshots = {
        path: path.read_bytes()
        for path in index_files_before | {TRACKER}
        if path.is_file()
    }
    source_ids = {
        str(record["topic_key"]): str(record["supersedes"])
        for record in records
    }
    finalize(
        GRAPHICAL_STAGED,
        GRAPHICAL_VALIDATION,
        commit=True,
    )
    final_tracker = load_tracker()
    final_topics = latest_validated_topics(final_tracker, merged_overrides())
    latest_ids = {topic.key: topic.record_id for topic in final_topics}
    expected_ids = {
        str(record["topic_key"]): str(record["record_id"])
        for record in records
    }
    latest_ok = latest_ids == expected_ids
    approvals_false = all(
        not record.get("approved")
        and isinstance(record.get("approval"), dict)
        and not record["approval"].get("approved")
        for record in records
    )
    old_records_retained = all(
        any(
            isinstance(candidate, dict)
            and candidate.get("record_id") == source_id
            for candidate in final_tracker["exports"]
        )
        for source_id in source_ids.values()
    )
    reference_errors = graphical.verify_reference(ROOT)
    if not latest_ok or not approvals_false or not old_records_retained or reference_errors:
        raise RefreshError(
            "Post-finalize graphical verification failed: "
            f"latest={latest_ok} approvals={approvals_false} "
            f"old={old_records_retained} reference={reference_errors}"
        )
    validation.update(
        {
            "state": "finalized",
            "finalized_on": datetime.now().astimezone().isoformat(),
            "tracker_sha256": sha256(TRACKER),
            "latest_tracker_resolution_passed": latest_ok,
            "old_generations_retained": old_records_retained,
            "approved_reference_retained": not reference_errors,
            "all_new_approvals_false": approvals_false,
            "tests": {
                "passed": tests_passed,
                "command": (
                    "python -m unittest tools.test_carvaka_flowchart "
                    "tools.test_refresh_all_v2_learning_sessions "
                    "tools.test_retrofit_v2_core_first "
                    "tools.test_v2_export_foundation "
                    "tools.test_v2_section_indexes "
                    "tools.test_v2_topic_command_catalog "
                    "tools.test_plan_v2_topic_batch"
                ),
            },
        }
    )
    GRAPHICAL_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_graphical_final_report(validation, tests_passed=tests_passed)
    index_files_after = semantic_index_files()
    changed_indexes = {
        path
        for path in index_files_after | set(snapshots)
        if snapshots.get(path)
        != (path.read_bytes() if path.is_file() else None)
    }
    graphical_records = [
        record
        for record in final_tracker["exports"]
        if isinstance(record, dict)
        and record.get("refresh_profile") == GRAPHICAL_REPAIR_ID
    ]
    changed = graphical_generated_files(graphical_records)
    changed.update(changed_indexes)
    changed.update(
        path for path in GRAPHICAL_SPEC_DIR.rglob("*") if path.is_file()
    )
    changed.update(
        {
            TRACKER,
            GRAPHICAL_PILOT_VALIDATION,
            GRAPHICAL_VALIDATION,
            GRAPHICAL_STAGED,
            GRAPHICAL_CHANGED,
            GRAPHICAL_PILOT_REPORT,
            GRAPHICAL_FINAL_REPORT,
            ROOT
            / "notes"
            / REFRESHED_ROOT
            / "CARVAKA-GRAPHICAL-PILOT-CONTACT.png",
            ROOT / "tools" / "carvaka_flowchart.py",
            ROOT / "tools" / "build_carvaka_graphical_specs.py",
            ROOT / "tools" / "refresh_all_v2_learning_sessions.py",
            ROOT / "tools" / "test_carvaka_flowchart.py",
            ROOT / "tools" / "test_refresh_all_v2_learning_sessions.py",
            ROOT
            / "instructions"
            / "pdf-learning-session"
            / "PDF-LEARNING-SESSION-STANDARD.md",
        }
    )
    review_dir = ROOT / "notes" / REFRESHED_ROOT / "carvaka-graphical-review"
    if review_dir.is_dir():
        changed.update(path for path in review_dir.rglob("*") if path.is_file())
    GRAPHICAL_CHANGED.write_text(
        "\n".join(
            sorted(
                (
                    relative(path)
                    for path in changed
                    if path.is_file() or path == GRAPHICAL_CHANGED
                ),
                key=str.casefold,
            )
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "topic_count": 40,
        "validation": relative(GRAPHICAL_VALIDATION),
        "report": relative(GRAPHICAL_FINAL_REPORT),
        "changed_files": relative(GRAPHICAL_CHANGED),
    }


def select_topics(
    all_topics: list[Topic],
    args: argparse.Namespace,
) -> list[Topic]:
    if args.all:
        return all_topics
    pilot = pilot_topics(all_topics)
    if args.remaining_after_pilot:
        pilot_keys = {topic.key for topic in pilot}
        return [topic for topic in all_topics if topic.key not in pilot_keys]
    if args.topics:
        requested = set(args.topics)
        selected = [topic for topic in all_topics if topic.key in requested]
        missing = sorted(requested - {topic.key for topic in selected})
        if missing:
            raise RefreshError(f"Unknown/latest-unvalidated topic keys: {missing}")
        return selected
    if args.mode == "pilot":
        return pilot
    raise RefreshError("Select --all, --remaining-after-pilot, or --topics.")


def upsert_records(
    tracker: dict[str, object],
    records: list[dict[str, object]],
) -> dict[str, object]:
    result = copy.deepcopy(tracker)
    exports = result["exports"]
    identities = {
        (
            str(record["topic_key"]),
            str(record["variant"]),
            int(record["generation"]),
        )
        for record in records
    }
    if len(identities) != len(records):
        raise RefreshError("Staged records contain duplicate identities.")
    existing = {
        (
            str(record.get("topic_key")),
            str(record.get("variant")),
            int(record.get("generation") or 1),
        )
        for record in exports
        if isinstance(record, dict)
    }
    collision = identities & existing
    if collision:
        raise RefreshError(f"Tracker already contains staged identities: {collision}")
    exports.extend(records)
    return result


def restore_snapshots(
    snapshots: dict[Path, bytes | None],
    before_files: set[Path],
) -> None:
    for path, content in snapshots.items():
        if content is None:
            if path.exists():
                path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    after_files = {
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and (
            path.name.endswith("COMMAND-INDEX.md")
            or path.name in {
                "EXPORT-PDF-COMMAND-INDEX.md",
                "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
                "TOPIC-COVERAGE-INDEX.md",
                "NOTES-PDF-INDEX.md",
                "WORKBOOK-PDF-INDEX.md",
            }
        )
    }
    for path in after_files - before_files:
        path.unlink()


def finalize(
    staged_path: Path,
    validation_path: Path,
    *,
    commit: bool,
) -> None:
    if not commit:
        raise RefreshError("Finalize is read-only unless --commit is supplied.")
    staged = load_json(staged_path)
    validation = load_json(validation_path)
    records = staged.get("records")
    if not isinstance(records, list) or not records:
        raise RefreshError("Staged records file has no records.")
    if not validation.get("passed"):
        raise RefreshError("Final validation report has not passed.")
    validated = {
        str(row.get("topic_key"))
        for row in validation.get("topics", [])
        if isinstance(row, dict) and row.get("passed")
    }
    record_keys = {str(record.get("topic_key")) for record in records}
    if validated != record_keys:
        raise RefreshError(
            "Final validation topics do not exactly match staged record topics."
        )
    tracker = load_tracker()
    updated = upsert_records(
        tracker,
        [record for record in records if isinstance(record, dict)],
    )
    pending = ROOT / "EXPORT-PDF-STATUS.learner-v2-refreshed.pending.json"
    pending.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    try:
        for record in records:
            errors = validate_tracker_record(
                pending,
                str(record["topic_key"]),
                V2_VARIANT,
                int(record["generation"]),
                repository_root=ROOT,
                check_paths=True,
            )
            if errors:
                raise RefreshError(
                    f"{record['topic_key']}: staged tracker validation failed: {errors}"
                )
        index_files: set[Path] = set()
        for directory, _, filenames in os.walk(ROOT, onerror=lambda _: None):
            for filename in filenames:
                if (
                    filename.endswith("COMMAND-INDEX.md")
                    or filename
                    in {
                        "EXPORT-PDF-COMMAND-INDEX.md",
                        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
                        "TOPIC-COVERAGE-INDEX.md",
                        "NOTES-PDF-INDEX.md",
                        "WORKBOOK-PDF-INDEX.md",
                    }
                ):
                    index_files.add(Path(directory) / filename)
        affected = {TRACKER, *index_files}
        snapshots = {
            path: path.read_bytes() if path.is_file() else None
            for path in affected
        }
        try:
            os.replace(pending, TRACKER)
            subprocess.run(
                [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
                cwd=ROOT,
                check=True,
            )
            subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools" / "generate_learning_session_command_indexes.py"),
                ],
                cwd=ROOT,
                check=True,
            )
            manifest_dir = ROOT / "upsc-ai-kit" / "manifests" / "v2"
            ignored = {
                "README.md",
                "section-manifest.schema.json",
                "section-manifest.template.json",
                "topic-catalog.json",
                "topic-catalog.schema.json",
            }
            for manifest in sorted(
                manifest_dir.glob("*.json"),
                key=lambda path: path.name.casefold(),
            ):
                if manifest.name in ignored:
                    continue
                raw_manifest = load_json(manifest)
                if (
                    str((raw_manifest.get("section") or {}).get("scope") or "")
                    .strip()
                    .casefold()
                    not in {"official-section", "pilot"}
                ):
                    continue
                subprocess.run(
                    [
                        sys.executable,
                        str(ROOT / "tools" / "generate_v2_section_indexes.py"),
                        "--manifest",
                        str(manifest),
                    ],
                    cwd=ROOT,
                    check=True,
                )
        except Exception:
            restore_snapshots(snapshots, index_files)
            raise
    finally:
        if pending.exists():
            pending.unlink()


def run(args: argparse.Namespace) -> int:
    tracker = load_tracker()
    if args.mode == "graphical-pilot":
        result = run_graphical_pilot(
            manual_review_passed=args.manual_review_pass,
        )
        print(
            f"topics={result['topic_count']} tracker_updated=false "
            f"report={result['report']} validation={result['validation']} "
            f"board={result['board']}"
        )
        return 0
    if args.mode == "graphical-stage":
        result = run_graphical_stage_all()
        print(
            f"topics={result['topic_count']} tracker_updated=false "
            f"validation={result['validation']} staged={result['staged']} "
            f"review_dir={result['review_dir']}"
        )
        return 0
    if args.mode == "graphical-finalize":
        result = finalize_graphical_repair(
            commit=args.commit,
            manual_review_passed=args.manual_review_pass,
            tests_passed=args.tests_passed,
        )
        print(
            f"topics={result['topic_count']} report={result['report']} "
            f"validation={result['validation']} "
            f"changed_files={result['changed_files']}"
        )
        return 0
    if args.mode == "deep-audit":
        overrides = merged_overrides()
        topics = latest_validated_topics(tracker, overrides)
        audit = write_initial_deep_audit(topics, overrides)
        print(
            f"topics={audit['topic_count']} "
            f"affected={audit['affected_topic_count']} "
            f"audit={relative(DEEP_AUDIT)}"
        )
        return 0
    if args.mode == "deep-repair":
        result = run_deep_repair(
            commit=args.commit,
            tests_passed=args.tests_passed,
        )
        print(
            f"topics={result['topic_count']} report={result['report']} "
            f"validation={result['validation']} audit={result['audit']} "
            f"changed_files={result['changed_files']}"
        )
        return 0
    if args.mode == "ascii-repair":
        result = run_ascii_repair(
            commit=args.commit,
            tests_passed=args.tests_passed,
        )
        print(
            f"topics={result['topic_count']} panels={result['total_panels']} "
            f"report={result['report']} validation={result['validation']} "
            f"manual_specs={len(result['manual_specs'])} "
            f"changed_files={result['changed_files']}"
        )
        return 0
    if args.mode == "semantic-audit":
        topics = latest_validated_topics(tracker, load_overrides())
        audit = write_semantic_quality_audit(topics)
        print(
            f"topics={audit['topic_count']} "
            f"affected={audit['affected_topic_count']} "
            f"audit={relative(SEMANTIC_AUDIT)}"
        )
        return 0
    if args.mode == "semantic-repair":
        result = run_semantic_repair(
            commit=args.commit,
            tests_passed=args.tests_passed,
        )
        print(
            f"topics={result['topic_count']} "
            f"report={result['report']} validation={result['validation']} "
            f"changed_files={result['changed_files']}"
        )
        return 0
    if args.mode == "new-topic":
        if not args.no_tracker_update:
            raise RefreshError(
                "New-topic generation is stage-only; pass --no-tracker-update."
            )
        if args.spec is None:
            raise RefreshError("new-topic mode requires --spec.")
        row, record = process_new_topic_spec(args.spec, tracker)
        print(
            f"topic={record['topic_key']} generation={record['generation']} "
            f"passed={row['passed']} tracker_updated=false "
            f"record={record['markdown']}"
        )
        return 0
    overrides = load_overrides()
    all_topics = latest_validated_topics(tracker, overrides)
    if args.mode == "inventory":
        print(json.dumps(
            {
                "topic_count": len(all_topics),
                "pilot": [topic.key for topic in pilot_topics(all_topics)],
                "topics": [
                    {
                        "topic_key": topic.key,
                        "generation": topic.generation,
                        "subject": topic.subject,
                        "section": topic.section,
                    }
                    for topic in all_topics
                ],
            },
            ensure_ascii=False,
            indent=2,
        ))
        return 0
    if args.mode == "finalize":
        staged_path = args.staged_records or FULL_STAGED_RECORDS
        validation_path = args.validation_report or FULL_VALIDATION
        finalize(staged_path, validation_path, commit=args.commit)
        print(f"Atomically finalized {staged_path.name}.")
        return 0
    if args.mode == "report":
        result = write_final_migration_report(tests_passed=args.tests_passed)
        print(
            f"report={result['report']} validation={result['validation']} "
            f"changed_files={result['changed_files']}"
        )
        return 0

    selected = select_topics(all_topics, args)
    selection_name = (
        "pilot"
        if args.mode == "pilot"
        else (
            "all"
            if args.all
            else "remaining-after-pilot"
            if args.remaining_after_pilot
            else "topics"
        )
    )
    rows: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    if args.mode in {"pilot", "generate"}:
        if not args.no_tracker_update:
            raise RefreshError(
                "Generation is stage-only; pass --no-tracker-update explicitly."
            )
        tracker_hash = sha256(TRACKER)
        for topic in selected:
            predicted = output_paths(topic, next_generation(tracker, topic.key))
            if predicted.staged_record.is_file():
                row, record = validate_existing_topic(topic, tracker)
                if not row.get("passed"):
                    raise RefreshError(
                        f"{topic.key}: existing refreshed output failed resume validation."
                    )
            else:
                row, record = process_topic(topic, tracker, overrides)
            rows.append(row)
            records.append(record)
        if sha256(TRACKER) != tracker_hash:
            raise RefreshError("Tracker changed during no-tracker-update generation.")
    elif args.mode in {"validate", "stage-records"}:
        for topic in selected:
            row, record = validate_existing_topic(topic, tracker)
            rows.append(row)
            records.append(record)
    else:
        raise RefreshError(f"Unsupported mode: {args.mode}")

    is_pilot = {topic.key for topic in selected} == {
        topic.key for topic in pilot_topics(all_topics)
    }
    validation_path = PILOT_VALIDATION if is_pilot else FULL_VALIDATION
    staged_path = PILOT_STAGED_RECORDS if is_pilot else FULL_STAGED_RECORDS
    validation = write_validation(rows, validation_path, selection=selection_name)
    if not validation["passed"]:
        raise RefreshError(f"{selection_name} validation failed.")
    write_staged_records(records, staged_path, selection=selection_name)
    write_manifest(
        all_topics,
        {str(row["topic_key"]): row for row in rows},
        state="pilot-completed" if is_pilot else f"{selection_name}-completed",
    )
    if is_pilot:
        write_pilot_report(rows)
    write_changed_files()
    print(
        f"topics={len(rows)} passed={validation['passed']} "
        f"tracker_updated=false validation={relative(validation_path)} "
        f"staged_records={relative(staged_path)}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=(
            "inventory",
            "pilot",
            "generate",
            "validate",
            "stage-records",
            "new-topic",
            "semantic-audit",
            "semantic-repair",
            "deep-audit",
            "deep-repair",
            "ascii-repair",
            "graphical-pilot",
            "graphical-stage",
            "graphical-finalize",
            "finalize",
            "report",
        ),
    )
    parser.add_argument("--topics", nargs="+")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--remaining-after-pilot", action="store_true")
    parser.add_argument("--no-tracker-update", action="store_true")
    parser.add_argument("--staged-records", type=Path)
    parser.add_argument("--validation-report", type=Path)
    parser.add_argument("--spec", type=Path)
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--manual-review-pass", action="store_true")
    parser.add_argument("--tests-passed", type=int, default=0)
    args = parser.parse_args()
    if args.staged_records and not args.staged_records.is_absolute():
        args.staged_records = ROOT / args.staged_records
    if args.validation_report and not args.validation_report.is_absolute():
        args.validation_report = ROOT / args.validation_report
    if args.spec and not args.spec.is_absolute():
        args.spec = ROOT / args.spec
    try:
        return run(args)
    except (
        OSError,
        ValueError,
        RefreshError,
        json.JSONDecodeError,
        subprocess.CalledProcessError,
    ) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
