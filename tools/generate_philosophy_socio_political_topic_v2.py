"""Generate one adapter-defined Socio-Political Philosophy learner-v2 topic.

The module supports all ten official Socio-Political Philosophy topics.
It preserves retained layered sessions when available, can inherit a validated
learner-v2 generation into a new immutable successor, and otherwise assembles a
source-complete package from the canonical owner plus authored adapter practice
data. Shared publication state changes only when ``--finalize`` is supplied.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from types import ModuleType
from typing import Any, Iterable, Sequence

import fitz
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
import regenerate_philosophy_indian_v2 as philosophy_v2
from generate_philosophy_western_rationalism_v2 import (
    render_ascii_pdf_safe as _base_render_ascii_pdf,
)
from generate_v2_section_indexes import (
    load_manifest,
    load_tracker,
    resolve_topic_states,
)
from validate_v2_export import (
    V2_VARIANT,
    deep_content_quality_audit_text,
    extract_mcq_answer_keys,
    extract_v2_workbook_markdown,
    legacy_progress_navigation_lines,
    mcq_answer_text_errors,
    strip_legacy_progress_navigation,
    validate_ascii_master_text,
    validate_pdf,
    validate_pdf_layout,
    validate_refreshed_markdown_text,
    validate_tracker_record,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SECTION_KEY = "paper-ii-socio-political-philosophy"
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-socio-political-philosophy.json"
)
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
GLOBAL_EXPORT_INDEX = ROOT / "EXPORT-PDF-COMMAND-INDEX.md"
V2_COMMAND_INDEX = ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md"
PHILOSOPHY_COMMAND_INDEX = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "LEARNING-SESSION-COMMAND-INDEX.md"
)
MASTER_LEARNING_INDEX = (
    ROOT / "upsc-ai-kit" / "knowledge" / "LEARNING-SESSION-COMMAND-INDEX.md"
)
TOPIC_CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
EXPORT_MANIFEST_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
CONTENT_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / f"philosophy--{SECTION_KEY}-content-specs"
)
GRAPHICAL_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / f"philosophy--{SECTION_KEY}-graphical-specs"
)
KNOWLEDGE_OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
)
NOTES_OUTPUT = ROOT / "notes" / "Philosophy" / "learning-session-v2" / SECTION_KEY
FLOW_ROOT = ROOT / "notes" / "Philosophy" / "flowcharts"
OFFICIAL_SYLLABUS = (
    "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md"
)
PHILOSOPHY_README = "upsc-ai-kit\\knowledge\\Philosophy\\README.md"

REQUIRED_SESSION_FIELDS = {
    "title",
    "plain",
    "technical",
    "answer",
    "keywords",
    "usage",
    "mechanism",
    "consequence",
    "trap",
    "objection",
    "reply",
    "limit",
    "exam",
    "revision",
    "visuals",
}


@dataclass(frozen=True)
class LegacyTopic:
    key: str
    title: str


@dataclass(frozen=True)
class TopicAdapter:
    module_name: str
    module: ModuleType
    topic_key: str
    title: str
    number: int
    generation_date: str
    section_key: str
    official_clause: str
    slug: str
    asset_slug: str
    header_kicker: str
    canonical_owner: str
    advanced_dossier: str
    pyq_ledger: str
    retained_session: str | None
    retained_workbook: str | None
    successor_markdown: str | None
    immutable_generation_paths: bool
    session_specs: tuple[dict[str, Any], ...]
    ascii_panels: tuple[dict[str, Any], ...]
    required_terms: tuple[str, ...]
    advanced_session_titles: tuple[str, ...]
    owner_session_ranges: dict[int, tuple[str, ...]]
    current_anchor: dict[str, str] | None
    pyq_solutions: tuple[dict[str, Any], ...]
    mcqs: tuple[dict[str, Any], ...]
    original_mains: tuple[dict[str, Any], ...]

    @property
    def uses_retained_package(self) -> bool:
        return bool(
            self.retained_session
            and self.retained_workbook
            and repo_path(self.retained_session).is_file()
            and repo_path(self.retained_workbook).is_file()
        )

    @property
    def uses_successor_package(self) -> bool:
        return bool(
            self.successor_markdown
            and repo_path(self.successor_markdown).is_file()
        )


def repo_path(value: str | Path) -> Path:
    path = Path(str(value).replace("\\", os.sep).replace("/", os.sep))
    return path if path.is_absolute() else ROOT / path


def relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")
    except ValueError:
        return str(path.resolve()).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize_pdf_metadata(
    path: Path,
    *,
    title: str,
    adapter: TopicAdapter,
) -> None:
    compact_date = adapter.generation_date.replace("-", "")
    if not re.fullmatch(r"\d{8}", compact_date):
        raise ValueError(f"Invalid generation date for PDF metadata: {adapter.generation_date}")
    # Use a deterministic date-only timestamp at the start of the generation
    # day in the workspace timezone, rather than ReportLab's invariant 2000 date.
    pdf_date = f"D:{compact_date}000000+05'30'"
    temporary = path.with_suffix(path.suffix + ".metadata.pdf")
    with fitz.open(path) as document:
        current = dict(document.metadata or {})
        metadata = {
            "title": title,
            "author": "UPSC Agent / Copilot CLI",
            "subject": (
                "Philosophy Optional, Paper II, Socio-Political Philosophy, "
                f"Topic {adapter.number:02d}"
            ),
            "keywords": (
                f"{adapter.topic_key}; learner-v2; philosophy optional; "
                "socio-political philosophy"
            ),
            "creator": Path(__file__).name,
            "producer": current.get("producer") or "PyMuPDF",
            "creationDate": pdf_date,
            "modDate": pdf_date,
            "trapped": current.get("trapped") or "",
        }
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, path)


def pdf_metadata_errors(
    path: Path,
    *,
    expected_title: str,
    adapter: TopicAdapter,
) -> list[str]:
    expected_date = adapter.generation_date.replace("-", "")
    with fitz.open(path) as document:
        metadata = dict(document.metadata or {})
    errors: list[str] = []
    title = str(metadata.get("title") or "")
    if title != expected_title:
        errors.append(f"{path.name}: PDF title differs: {title!r}.")
    if "\ufffd" in " ".join(str(value) for value in metadata.values()):
        errors.append(f"{path.name}: PDF metadata contains a replacement glyph.")
    for key in ("creationDate", "modDate"):
        if expected_date not in str(metadata.get(key) or ""):
            errors.append(
                f"{path.name}: {key} does not match {adapter.generation_date}."
            )
    return errors


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".pending")
    pending.write_text(text, encoding="utf-8")
    os.replace(pending, path)


def write_json(path: Path, data: object) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def deliverable_hashes(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def _dict(module: ModuleType, name: str) -> dict[str, Any]:
    value = getattr(module, name, {})
    return dict(value) if isinstance(value, dict) else {}


def _first(*values: Any) -> Any:
    for value in values:
        if value is not None and value != "":
            return value
    return None


def _metadata_value(
    module: ModuleType,
    metadata: dict[str, Any],
    paths: dict[str, Any],
    sources: dict[str, Any],
    names: Sequence[str],
) -> Any:
    for name in names:
        if hasattr(module, name):
            value = getattr(module, name)
            if value is not None and value != "":
                return value
        for mapping in (metadata, paths, sources):
            for key in (name, name.casefold(), name.lower()):
                if key in mapping and mapping[key] not in (None, ""):
                    return mapping[key]
    return None


def _load_module(module_name: str) -> ModuleType:
    normalized = module_name.strip()
    if normalized.endswith(".py"):
        normalized = Path(normalized).stem
    if normalized.startswith("tools."):
        normalized = normalized.split(".", 1)[1]
    importlib.invalidate_caches()
    return importlib.import_module(normalized)


def _manifest_topic(
    module: ModuleType,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    topics = [item for item in manifest.get("topics", []) if isinstance(item, dict)]
    key = _first(getattr(module, "TOPIC_KEY", None), metadata.get("topic_key"), metadata.get("key"))
    if key:
        match = next((item for item in topics if item.get("topic_key") == key), None)
        if match:
            return match
    number = _first(
        getattr(module, "TOPIC_NUMBER", None),
        metadata.get("topic_number"),
        metadata.get("number"),
    )
    if number is None:
        header = str(getattr(module, "HEADER_KICKER", ""))
        match = re.search(r"\bTOPIC\s*0*(\d+)\b", header, re.I)
        number = int(match.group(1)) if match else None
    if number is None:
        match = re.search(r"(?:^|_)(08|09|10)(?:_|$)", module.__name__)
        number = int(match.group(1)) if match else None
    if number is not None:
        suffix = f"-{int(number):02d}"
        match = next(
            (item for item in topics if str(item.get("topic_key", "")).endswith(suffix)),
            None,
        )
        if match:
            return match
    raise ValueError(
        f"{module.__name__}: topic metadata cannot be reconciled with {relative(MANIFEST)}."
    )


def _official_clause(topic: dict[str, Any], module: ModuleType, metadata: dict[str, Any]) -> str:
    explicit = _first(
        getattr(module, "OFFICIAL_SYLLABUS_VERBATIM", None),
        getattr(module, "OFFICIAL_CLAUSE", None),
        metadata.get("official_syllabus_verbatim"),
        metadata.get("official_clause"),
        metadata.get("syllabus"),
    )
    if explicit:
        return str(explicit).strip()
    mapping = str(topic.get("syllabus_mapping") or "")
    match = re.search(r"\btopic\s+\d+\s*:\s*(.+)$", mapping, re.I)
    return (match.group(1) if match else mapping).strip()


def _tuple_of_dicts(value: Any) -> tuple[dict[str, Any], ...]:
    if value is None:
        return ()
    if not isinstance(value, (list, tuple)):
        raise ValueError("Expected a list/tuple of authored dictionaries.")
    if not all(isinstance(item, dict) for item in value):
        raise ValueError("Every authored specification item must be a dictionary.")
    return tuple(dict(item) for item in value)


def load_topic_adapter(module_name: str) -> TopicAdapter:
    module = _load_module(module_name)
    metadata = _dict(module, "TOPIC_METADATA")
    paths = _dict(module, "PATHS")
    sources = _dict(module, "SOURCE_METADATA")
    topic = _manifest_topic(module, metadata)

    topic_key = str(
        _first(
            getattr(module, "TOPIC_KEY", None),
            metadata.get("topic_key"),
            metadata.get("key"),
            topic.get("topic_key"),
        )
    )
    number_value = _first(
        getattr(module, "TOPIC_NUMBER", None),
        metadata.get("topic_number"),
        metadata.get("number"),
        re.search(r"-(\d+)$", topic_key).group(1)
        if re.search(r"-(\d+)$", topic_key)
        else None,
    )
    number = int(number_value)
    if number not in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
        raise ValueError(
            f"{module.__name__}: only official topics 01-10 are supported."
        )
    title = str(
        _first(
            getattr(module, "TOPIC_TITLE", None),
            metadata.get("topic_title"),
            metadata.get("title"),
            topic.get("display_title"),
        )
    ).strip()
    generation_date = str(
        _first(
            getattr(module, "GENERATION_DATE", None),
            metadata.get("generation_date"),
            metadata.get("date"),
            date.today().isoformat(),
        )
    )
    section_key = str(
        _first(
            getattr(module, "SECTION_KEY", None),
            metadata.get("section_key"),
            SECTION_KEY,
        )
    )
    slug = str(
        _first(
            getattr(module, "TOPIC_SLUG", None),
            metadata.get("topic_slug"),
            metadata.get("slug"),
            re.sub(r"^philosophy-paper-ii-socio-political-philosophy-\d+-?", "", topic_key),
            module.__name__.removeprefix("philosophy_socio_political_").removesuffix("_v2_spec"),
        )
    ).strip("-_ ")
    if not slug:
        slug = re.sub(r"[^a-z0-9]+", "-", title.casefold()).strip("-")
    slug = re.sub(r"[^a-z0-9]+", "-", slug.casefold()).strip("-")
    asset_slug = str(
        _first(
            getattr(module, "ASSET_SLUG", None),
            metadata.get("asset_slug"),
            slug,
        )
    ).strip("-_ ")
    asset_slug = re.sub(r"[^a-z0-9]+", "-", asset_slug.casefold()).strip("-")

    canonical_owner = str(
        _first(
            _metadata_value(
                module,
                metadata,
                paths,
                sources,
                ("CANONICAL_OWNER", "SOURCE_CANONICAL", "SOURCE_BASIC"),
            ),
            topic.get("source_canonical"),
            topic.get("source_basic"),
        )
    )
    advanced_dossier = str(
        _first(
            _metadata_value(
                module,
                metadata,
                paths,
                sources,
                ("ADVANCED_DOSSIER", "SOURCE_ADVANCED"),
            ),
            topic.get("source_advanced"),
        )
    )
    verified = topic.get("verified_pyq_sources")
    manifest_ledger = verified[0] if isinstance(verified, list) and verified else None
    pyq_ledger = str(
        _first(
            _metadata_value(
                module,
                metadata,
                paths,
                sources,
                ("PYQ_LEDGER", "VERIFIED_PYQ_LEDGER"),
            ),
            manifest_ledger,
        )
    )
    retained_session = _first(
        _metadata_value(
            module,
            metadata,
            paths,
            sources,
            ("RETAINED_SESSION", "RETAINED_LEARNING_SESSION"),
        ),
        topic.get("retained_learning_session"),
    )
    retained_workbook = _first(
        _metadata_value(
            module,
            metadata,
            paths,
            sources,
            ("RETAINED_WORKBOOK",),
        ),
        topic.get("retained_workbook"),
    )
    successor_markdown = _first(
        _metadata_value(
            module,
            metadata,
            paths,
            sources,
            ("SUCCESSOR_MARKDOWN", "BASE_GENERATION_MARKDOWN"),
        )
    )
    ranges_value = getattr(module, "OWNER_SESSION_RANGES", {})
    if isinstance(ranges_value, dict):
        owner_ranges = {
            int(key): tuple(str(item) for item in value)
            for key, value in ranges_value.items()
        }
    elif isinstance(ranges_value, (list, tuple)):
        owner_ranges = {
            int(item["session"]): tuple(
                f"§{section}" for section in item.get("owner_sections", ())
            )
            for item in ranges_value
            if isinstance(item, dict) and item.get("session") is not None
        }
    else:
        owner_ranges = {}

    adapter = TopicAdapter(
        module_name=module.__name__,
        module=module,
        topic_key=topic_key,
        title=title,
        number=number,
        generation_date=generation_date,
        section_key=section_key,
        official_clause=_official_clause(topic, module, metadata),
        slug=slug,
        asset_slug=asset_slug,
        header_kicker=str(
            _first(
                getattr(module, "HEADER_KICKER", None),
                metadata.get("header_kicker"),
                f"PHILOSOPHY OPTIONAL | PAPER II | SOCIO-POLITICAL PHILOSOPHY | TOPIC {number:02d}",
            )
        ),
        canonical_owner=canonical_owner,
        advanced_dossier=advanced_dossier,
        pyq_ledger=pyq_ledger,
        retained_session=str(retained_session) if retained_session else None,
        retained_workbook=str(retained_workbook) if retained_workbook else None,
        successor_markdown=(
            str(successor_markdown) if successor_markdown else None
        ),
        immutable_generation_paths=bool(
            _first(
                getattr(module, "IMMUTABLE_GENERATION_PATHS", None),
                metadata.get("immutable_generation_paths"),
                False,
            )
        ),
        session_specs=_tuple_of_dicts(getattr(module, "SESSION_SPECS", None)),
        ascii_panels=_tuple_of_dicts(getattr(module, "ASCII_PANELS", None)),
        required_terms=tuple(
            str(item)
            for item in _first(
                getattr(module, "REQUIRED_TERMS", None),
                getattr(module, "REQUIRED_CORE_TERMS", None),
                (),
            )
        ),
        advanced_session_titles=tuple(
            str(item)
            for item in getattr(module, "ADVANCED_SESSION_TITLES", ())
        ),
        owner_session_ranges=owner_ranges,
        current_anchor=(
            dict(getattr(module, "CURRENT_ANCHOR"))
            if isinstance(getattr(module, "CURRENT_ANCHOR", None), dict)
            else None
        ),
        pyq_solutions=_tuple_of_dicts(getattr(module, "PYQ_SOLUTIONS", ())),
        mcqs=_tuple_of_dicts(getattr(module, "MCQS", ())),
        original_mains=_tuple_of_dicts(getattr(module, "ORIGINAL_MAINS", ())),
    )
    validate_adapter(adapter)
    return adapter


def validate_adapter(adapter: TopicAdapter) -> None:
    if len(adapter.session_specs) != 10:
        raise ValueError(
            f"{adapter.module_name}: expected 10 SESSION_SPECS, found "
            f"{len(adapter.session_specs)}."
        )
    missing = [
        f"session {index}: {sorted(REQUIRED_SESSION_FIELDS - set(spec))}"
        for index, spec in enumerate(adapter.session_specs, 1)
        if REQUIRED_SESSION_FIELDS - set(spec)
    ]
    if missing:
        raise ValueError("Incomplete SESSION_SPECS: " + "; ".join(missing))
    if len(adapter.ascii_panels) != 12:
        raise ValueError(
            f"{adapter.module_name}: expected 12 ASCII_PANELS, found "
            f"{len(adapter.ascii_panels)}."
        )
    for index, panel in enumerate(adapter.ascii_panels, 1):
        if not {"title", "structural_type", "sessions", "lines"} <= set(panel):
            raise ValueError(f"ASCII panel {index} is missing required fields.")
        if not isinstance(panel["lines"], (list, tuple)) or not panel["lines"]:
            raise ValueError(f"ASCII panel {index} has no authored lines.")
    if not adapter.required_terms:
        raise ValueError(f"{adapter.module_name}: REQUIRED_TERMS is empty.")
    if not adapter.advanced_session_titles:
        raise ValueError(
            f"{adapter.module_name}: ADVANCED_SESSION_TITLES is empty."
        )
    for value, label in (
        (adapter.topic_key, "topic key"),
        (adapter.title, "title"),
        (adapter.official_clause, "official syllabus"),
        (adapter.canonical_owner, "canonical owner"),
        (adapter.advanced_dossier, "advanced dossier"),
        (adapter.pyq_ledger, "PYQ ledger"),
        (adapter.header_kicker, "header kicker"),
    ):
        if not str(value).strip():
            raise ValueError(f"{adapter.module_name}: missing {label}.")
    if not adapter.uses_retained_package and not adapter.uses_successor_package:
        if set(adapter.owner_session_ranges) != set(range(1, 11)):
            raise ValueError(
                f"{adapter.module_name}: canonical fallback requires "
                "OWNER_SESSION_RANGES for sessions 1-10."
            )
        if not adapter.pyq_solutions or not adapter.mcqs or not adapter.original_mains:
            raise ValueError(
                f"{adapter.module_name}: canonical fallback requires "
                "PYQ_SOLUTIONS, MCQS and ORIGINAL_MAINS."
            )
    if adapter.mcqs:
        keys = [str(item.get("answer", "")).upper() for item in adapter.mcqs]
        expected = ["ABCD"[index % 4] for index in range(len(keys))]
        if keys != expected:
            raise ValueError("Authored MCQs must follow strict A-B-C-D rotation.")
        for index, item in enumerate(adapter.mcqs, 1):
            options = item.get("options")
            if not isinstance(options, (list, tuple)) or len(options) != 4:
                raise ValueError(f"MCQ {index} must supply four options.")


def latest_identity(
    tracker: dict[str, Any],
    topic_key: str,
) -> tuple[int, str, str | None]:
    records = [
        record
        for record in tracker.get("exports", [])
        if isinstance(record, dict) and record.get("topic_key") == topic_key
    ]
    learners = [record for record in records if record.get("variant") == V2_VARIANT]
    legacy = [record for record in records if record.get("variant") == "legacy-v1"]
    legacy_id = (
        str(max(legacy, key=lambda item: int(item.get("generation") or 1))["record_id"])
        if legacy
        else None
    )
    if learners:
        current = max(learners, key=lambda item: int(item.get("generation") or 1))
        return int(current["generation"]) + 1, str(current["record_id"]), legacy_id
    return 2, legacy_id or f"{topic_key}:legacy-v1:g1", legacy_id


def owner_pyqs(adapter: TopicAdapter, ledger: str) -> list[str]:
    owner_name = Path(adapter.canonical_owner.replace("\\", "/")).name.casefold()
    questions: list[str] = []
    for line in ledger.splitlines():
        if not line.lstrip().startswith("- (") or "Primary owner" not in line:
            continue
        link = re.search(r"\[[^\]]+\]\(([^)]+)\)", line)
        if not link or Path(link.group(1).replace("\\", "/")).name.casefold() != owner_name:
            continue
        match = re.search(r"^-\s*(.+?)\s*\*\*\[[^\]]+\]\*\*\s*—", line)
        if match:
            questions.append(
                re.sub(r"^\([a-z]\)\s*", "", match.group(1)).strip()
            )
    return questions


def _normalize_question(value: str) -> str:
    normalized = re.sub(r"\s+", " ", value).strip()
    return re.sub(r"\s+([?!.,;:])", r"\1", normalized)


def validate_spec_pyqs(adapter: TopicAdapter, source_pyqs: Sequence[str]) -> None:
    if not adapter.pyq_solutions:
        return
    authored = [_normalize_question(str(item.get("question", ""))) for item in adapter.pyq_solutions]
    source = [_normalize_question(item) for item in source_pyqs]
    if len(authored) != len(source) or set(authored) != set(source):
        missing = [item for item in source if item not in authored]
        extra = [item for item in authored if item not in source]
        raise ValueError(
            "PYQ_SOLUTIONS must reproduce the controlling ledger exactly. "
            f"Missing={missing[:2]}; extra={extra[:2]}."
        )


def _session_visuals(spec: dict[str, Any]) -> str:
    blocks: list[str] = []
    for visual in spec.get("visuals", []):
        if not isinstance(visual, dict):
            continue
        lines = visual.get("lines", [])
        if isinstance(lines, str):
            lines = lines.splitlines()
        blocks.extend(
            [
                f"#### VISUAL — {visual.get('title', spec['title'])}",
                "```text",
                *(str(line) for line in lines),
                "```",
                f"*{visual.get('caption', 'This visual fixes the session logic in recall order.')}*",
            ]
        )
    return "\n\n".join(blocks)


def contract_block(spec: dict[str, Any]) -> str:
    keywords = "\n".join(f"- **{item}**" for item in spec["keywords"])
    revision = "\n".join(f"- {item}" for item in spec["revision"])
    return "\n\n".join(
        [
            "#### DEFINITION / WHAT THIS IS CALLED",
            (
                f"**Plain-language definition:** {spec['plain']}\n\n"
                f"**Technical definition:** {spec['technical']}"
            ),
            _session_visuals(spec),
            "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM",
            f"> {spec['answer']}",
            "#### MUST-WRITE KEYWORDS",
            f"{keywords}\n\n**How to use them:** {spec['usage']}",
            "#### CORE OBJECTION, REPLY AND RESIDUAL LIMIT",
            (
                f"**Objection:** {spec['objection']}\n\n"
                f"**Best reply:** {spec['reply']}\n\n"
                f"**Residual limit:** {spec['limit']}"
            ),
            "#### EXAM USE AND CONCISE REVISION",
            f"**Answer architecture:** {spec['exam']}\n\n{revision}",
        ]
    )


def closure_block(spec: dict[str, Any]) -> str:
    authored_closure = spec.get("closure_keywords")
    if authored_closure:
        closure_keywords = [str(item).strip() for item in authored_closure]
    else:
        concise_keywords: list[str] = []
        for raw in spec["keywords"]:
            value = re.split(
                r"\s+and\s+|[,;:/]|\s+\(",
                str(raw),
                maxsplit=1,
                flags=re.IGNORECASE,
            )[0].strip()
            words = value.split()
            if len(value) > 24 and len(words) > 2:
                value = " ".join(words[:2])
            if value and value.casefold() not in {
                item.casefold() for item in concise_keywords
            }:
                concise_keywords.append(value)
        closure_keywords = sorted(
            concise_keywords,
            key=lambda item: (len(item), item.casefold()),
        )[:4]
    return "\n".join(
        [
            f"#### CLOSING RECALL FLOW — {spec['title']}",
            "",
            "```closure-flow",
            f"SUBTOPIC: {spec['title']}",
            f"STARTING CONCEPT: {spec['title']}",
            "KEY TERMS / DEFINITIONS: " + " | ".join(closure_keywords),
            f"MECHANISM / ARGUMENT: {spec['mechanism']}",
            f"CONSEQUENCE / CONTRAST: {spec['consequence']}",
            f"UPSC TRAP / ANSWER-USE: {spec['trap']}",
            f"ANSWER-GRABBING FORMULATION: {spec['answer']}",
            "```",
        ]
    )


@dataclass(frozen=True)
class OwnerPiece:
    start: int
    section_id: str | None
    major: str | None
    text: str
    is_intro: bool


def _heading_id(title: str) -> str | None:
    match = re.match(r"\s*(\d+[A-Za-z]?(?:\.\d+)?)\b", title)
    return match.group(1).upper() if match else None


def _major(section_id: str | None) -> str | None:
    return section_id.split(".", 1)[0] if section_id else None


def _owner_pieces(owner_text: str) -> list[OwnerPiece]:
    _, body = philosophy_v2.strip_frontmatter(owner_text)
    body = re.sub(r"(?m)^#(?!#)\s+.*\n?", "", body, count=1)
    h2s = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", body))
    pieces: list[OwnerPiece] = []
    if not h2s:
        return [OwnerPiece(0, None, None, body.strip(), True)]
    pre = body[: h2s[0].start()].strip()
    if pre:
        pieces.append(OwnerPiece(0, None, None, pre, True))
    for index, heading in enumerate(h2s):
        end = h2s[index + 1].start() if index + 1 < len(h2s) else len(body)
        section = body[heading.start() : end]
        section_id = _heading_id(heading.group(1))
        h3s = list(re.finditer(r"(?m)^###\s+(.+?)\s*$", section))
        if not h3s:
            pieces.append(
                OwnerPiece(heading.start(), section_id, _major(section_id), section.strip(), True)
            )
            continue
        intro = section[: h3s[0].start()].strip()
        if intro:
            pieces.append(
                OwnerPiece(heading.start(), section_id, _major(section_id), intro, True)
            )
        for sub_index, subheading in enumerate(h3s):
            sub_end = (
                h3s[sub_index + 1].start()
                if sub_index + 1 < len(h3s)
                else len(section)
            )
            sub_id = _heading_id(subheading.group(1))
            pieces.append(
                OwnerPiece(
                    heading.start() + subheading.start(),
                    sub_id,
                    _major(sub_id) or _major(section_id),
                    section[subheading.start() : sub_end].strip(),
                    False,
                )
            )
    return [piece for piece in pieces if piece.text.strip()]


def _section_key(value: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)([A-Z]?)(?:\.(\d+))?", value.upper())
    if not match:
        return (10_000, 0, 0)
    return (
        int(match.group(1)),
        ord(match.group(2)) - 64 if match.group(2) else 0,
        int(match.group(3)) if match.group(3) else -1,
    )


def _range_tokens(references: Sequence[str]) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    for reference in references:
        scope = reference.split(":", 1)[0]
        for match in re.finditer(
            r"§\s*(\d+[A-Za-z]?(?:\.\d+)?)"
            r"(?:\s*[-–—]\s*§?\s*(\d+[A-Za-z]?(?:\.\d+)?))?",
            scope,
        ):
            tokens.append((match.group(1).upper(), (match.group(2) or match.group(1)).upper()))
    return tokens


def _piece_matches(piece: OwnerPiece, start: str, end: str) -> bool:
    if not piece.section_id:
        return False
    start_key, end_key = _section_key(start), _section_key(end)
    piece_key = _section_key(piece.section_id)
    if "." not in start and "." not in end:
        major_key = _section_key(piece.major or piece.section_id)
        return start_key[:2] <= major_key[:2] <= end_key[:2]
    return start_key <= piece_key <= end_key


def split_owner_by_session(
    adapter: TopicAdapter,
    owner_text: str,
) -> tuple[str, ...]:
    pieces = _owner_pieces(owner_text)
    ranges = {
        session: _range_tokens(adapter.owner_session_ranges[session])
        for session in range(1, 11)
    }
    assignments: dict[int, int] = {}
    for piece_index, piece in enumerate(pieces):
        if piece.is_intro and piece.section_id is None:
            continue
        for session in range(1, 11):
            if any(_piece_matches(piece, start, end) for start, end in ranges[session]):
                assignments[piece_index] = session
                break

    major_sessions: dict[str, list[int]] = {}
    for piece_index, session in assignments.items():
        major = pieces[piece_index].major
        if major:
            major_sessions.setdefault(major, []).append(session)
    for piece_index, piece in enumerate(pieces):
        if piece_index in assignments:
            continue
        if piece.major and major_sessions.get(piece.major):
            assignments[piece_index] = min(major_sessions[piece.major])
            continue
        if piece.start == 0:
            assignments[piece_index] = 1
            continue
        numeric_major = _section_key(piece.major or "")[0]
        candidates: list[tuple[int, int]] = []
        for major, sessions in major_sessions.items():
            candidates.append((abs(_section_key(major)[0] - numeric_major), min(sessions)))
        assignments[piece_index] = min(candidates)[1] if candidates else 10

    grouped: list[list[OwnerPiece]] = [[] for _ in range(10)]
    for piece_index, piece in enumerate(pieces):
        grouped[assignments[piece_index] - 1].append(piece)
    if sum(len(group) for group in grouped) != len(pieces):
        raise ValueError("Canonical-owner splitting lost source material.")
    return tuple(
        "\n\n".join(
            philosophy_v2.demote(piece.text, 4).strip()
            for piece in sorted(group, key=lambda item: item.start)
        )
        for group in grouped
    )


def _advanced_dossier_fragment(adapter: TopicAdapter, dossier: str) -> str:
    headings = list(re.finditer(r"(?m)^##\s+(\d+)\.\s+(.+?)\s*$", dossier))
    for index, heading in enumerate(headings):
        if int(heading.group(1)) != adapter.number:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(dossier)
        return dossier[heading.end() : end].strip()
    raise ValueError(
        f"{adapter.title}: matching advanced dossier section {adapter.number} was not found."
    )


def _advanced_sessions(adapter: TopicAdapter, fragment: str) -> str:
    titles = adapter.advanced_session_titles or (f"{adapter.title}: optional refinements",)
    lines = fragment.splitlines()
    table_start = next(
        (index for index, line in enumerate(lines) if line.lstrip().startswith("|")),
        None,
    )
    table_end = table_start
    if table_start is not None:
        while table_end is not None and table_end < len(lines) and lines[table_end].lstrip().startswith("|"):
            table_end += 1
    buckets: list[list[str]] = [[] for _ in titles]
    if table_start is not None and table_end is not None:
        pre = "\n".join(lines[:table_start]).strip()
        table = lines[table_start:table_end]
        post = "\n".join(lines[table_end:]).strip()
        header = table[:2]
        rows = table[2:]
        if pre:
            buckets[0].append(pre)
        for index, row in enumerate(rows):
            buckets[min(index, len(buckets) - 1)].append("\n".join([*header, row]))
        post_blocks = [item.strip() for item in re.split(r"\n\s*\n", post) if item.strip()]
        for index, block in enumerate(post_blocks):
            buckets[index % len(buckets)].append(block)
    else:
        blocks = [item.strip() for item in re.split(r"\n\s*\n", fragment) if item.strip()]
        for index, block in enumerate(blocks):
            buckets[index % len(buckets)].append(block)
    nonempty = [(title, bucket) for title, bucket in zip(titles, buckets) if bucket]
    return "\n\n".join(
        f"### ADVANCED SESSION {index} — {title}\n\n"
        + philosophy_v2.demote("\n\n".join(bucket), 4)
        for index, (title, bucket) in enumerate(nonempty, 1)
    )


def _current_anchor(adapter: TopicAdapter) -> str:
    anchor = adapter.current_anchor
    if not anchor:
        return ""
    title = _first(anchor.get("title"), anchor.get("case_name"), adapter.title)
    fact = _first(anchor.get("fact"), anchor.get("holding_summary"), "")
    if anchor.get("citation") or anchor.get("neutral_citation") or anchor.get("decided"):
        identity = " · ".join(
            str(value)
            for value in (
                anchor.get("citation"),
                anchor.get("neutral_citation"),
                anchor.get("decided"),
            )
            if value
        )
        fact = f"{identity}. {fact}".strip()
    use = _first(anchor.get("use"), anchor.get("scope_note"), "")
    fields = [
        f"### CURRENT ILLUSTRATION — {title}",
        "",
        f"**Fact:** {fact}",
        "",
        f"**Exam use:** {use}",
    ]
    if anchor.get("source_url"):
        fields.extend(["", f"**Source:** {anchor['source_url']}"])
    return "\n".join(fields).strip()


def _render_mcqs(adapter: TopicAdapter) -> str:
    blocks = ["### AUTHORED MCQ AND REMEDIATION BANK"]
    for index, item in enumerate(adapter.mcqs, 1):
        options = [str(option) for option in item["options"]]
        answer = str(item["answer"]).upper()
        answer_text = options["ABCD".index(answer)]
        question = _first(item.get("text"), item.get("question"), "")
        trap = _first(item.get("trap"), item.get("trap_remediation"), "")
        blocks.extend(
            [
                f"#### Q{index}. {question}",
                "",
                *[f"{letter}. {option}" for letter, option in zip("ABCD", options)],
                "",
                f"**Answer: {answer}. {answer_text}**",
                "",
                f"**Explanation:** {item.get('explanation', '')}",
                "",
                f"**Trap/remediation:** {trap}",
            ]
        )
    return "\n\n".join(blocks)


def _model_parts(item: dict[str, Any]) -> tuple[str, list[str], str]:
    model = item.get("model_answer")
    if isinstance(model, dict):
        thesis = str(
            _first(
                model.get("thesis"),
                model.get("intro"),
                item.get("thesis"),
                "",
            )
        )
        structure = _first(
            model.get("structure"),
            [
                value
                for value in (
                    model.get("body"),
                    model.get("objection_reply"),
                )
                if value
            ],
            item.get("structure"),
            [],
        )
        conclusion = str(
            _first(
                model.get("conclusion"),
                model.get("verdict"),
                item.get("conclusion"),
                "",
            )
        )
    else:
        thesis = str(_first(item.get("thesis"), model if isinstance(model, str) else "", ""))
        structure = item.get("structure", [])
        conclusion = str(item.get("conclusion", ""))
    if isinstance(structure, str):
        structure = [structure]
    return thesis, [str(value) for value in structure], conclusion


def _render_pyqs(
    adapter: TopicAdapter,
    source_pyqs: Sequence[str] = (),
) -> str:
    exact_by_normalized = {
        _normalize_question(question): question for question in source_pyqs
    }
    blocks = ["### VERIFIED PYQS WITH MODEL SOLUTIONS"]
    for index, item in enumerate(adapter.pyq_solutions, 1):
        thesis, structure, conclusion = _model_parts(item)
        authored_question = str(item["question"])
        question = exact_by_normalized.get(
            _normalize_question(authored_question),
            authored_question,
        )
        identity = " · ".join(
            str(value)
            for value in (
                item.get("year"),
                _first(item.get("number"), item.get("question_number")),
            )
            if value not in (None, "")
        )
        marks = f"{item['marks']} marks" if item.get("marks") is not None else "verified demand"
        blocks.extend(
            [
                f"#### PYQ {index} — {identity} ({marks})",
                "",
                f"**Question:** {question}",
                "",
                f"**Thesis / opening:** {thesis}",
                "",
                "**Model answer structure:**",
                *[f"- {point}" for point in structure],
                "",
                f"**Conclusion:** {conclusion}",
                "",
                (
                    "**Why this earns marks:** It answers the exact demand through a "
                    "clear claim, named doctrine or evidence, analysis, qualification "
                    "and a direct concluding verdict."
                ),
            ]
        )
    return "\n\n".join(blocks)


def _render_original_mains(adapter: TopicAdapter) -> str:
    blocks = ["### ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS"]
    for index, item in enumerate(adapter.original_mains, 1):
        solution = item.get("model_solution", item.get("solution", []))
        if isinstance(solution, dict):
            solution = [
                value
                for value in (
                    solution.get("intro"),
                    solution.get("body"),
                    solution.get("objection_reply"),
                    solution.get("verdict"),
                )
                if value
            ]
        if isinstance(solution, str):
            solution = [solution]
        marks = item.get("marks")
        word_limit = item.get("word_limit")
        meta = f"{marks} marks"
        if word_limit:
            meta += f" · {word_limit} words"
        question = _first(item.get("question"), item.get("prompt"), "")
        blocks.extend(
            [
                f"#### Original Mains {index} — {meta}",
                "",
                f"**Question:** {question}",
                "",
                "**Model solution:**",
                *[f"- {point}" for point in solution],
            ]
        )
    return "\n\n".join(blocks)


def _register_notes(adapter: TopicAdapter) -> str:
    blocks: list[str] = []
    for index, spec in enumerate(adapter.session_specs, 1):
        blocks.extend(
            [
                f"### {index}. {spec['title']}",
                "",
                f"**Answer line:** {spec['answer']}",
                "",
                "**Keywords:** " + " · ".join(str(item) for item in spec["keywords"]),
                "",
                "**Rapid revision:**",
                *[f"- {item}" for item in spec["revision"]],
                "",
                f"**Mechanism:** {spec['mechanism']}",
                "",
                f"**Consequence / contrast:** {spec['consequence']}",
                "",
                f"**Exam trap:** {spec['trap']}",
                "",
                f"**Answer route:** {spec['exam']}",
            ]
        )
    return "\n".join(blocks).strip()


def assemble_canonical_fallback(
    adapter: TopicAdapter,
    owner_text: str,
    dossier_text: str,
    ledger_text: str,
) -> str:
    source_pyqs = owner_pyqs(adapter, ledger_text)
    validate_spec_pyqs(adapter, source_pyqs)
    owner_sessions = split_owner_by_session(adapter, owner_text)
    basic: list[str] = []
    anchor = _current_anchor(adapter)
    if anchor:
        basic.append(anchor)
    for index, (spec, owner_fragment) in enumerate(
        zip(adapter.session_specs, owner_sessions),
        1,
    ):
        basic.append(
            "\n\n".join(
                [
                    f"### SESSION {index} — {spec['title']}",
                    contract_block(spec),
                    "#### CANONICAL OWNER COVERAGE",
                    owner_fragment,
                    closure_block(spec),
                ]
            )
        )
    advanced = _advanced_sessions(
        adapter,
        _advanced_dossier_fragment(adapter, dossier_text),
    )
    frontmatter = "\n".join(
        [
            "---",
            f'title: "{adapter.title} — Learner-v2"',
            f"topic_key: {adapter.topic_key}",
            "variant: learner-v2",
            "generation: 0",
            f"generation_date: {adapter.generation_date}",
            "---",
        ]
    )
    return "\n\n".join(
        [
            frontmatter,
            f"# {adapter.title} — Learner-v2 Source-Complete Learning Session",
            (
                f"> **Syllabus (verbatim):** {adapter.official_clause}\n>\n"
                "> **Evidence discipline:** The complete canonical owner is split "
                "across ten numbered Core sessions; exact verified PYQs and authored "
                "practice come from the controlling adapter; only the matching "
                "advanced dossier section is optional."
            ),
            "## BASIC LEARNING SESSION",
            *basic,
            "## BASIC MCQS / REMEDIATION",
            _render_mcqs(adapter),
            "## PYQS AND ANSWER PRACTICE",
            _render_pyqs(adapter, source_pyqs),
            _render_original_mains(adapter),
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            advanced,
            "## CONSOLIDATED REGISTER NOTES",
            _register_notes(adapter),
        ]
    ).strip() + "\n"


def _enrich_retained_sessions(adapter: TopicAdapter, text: str) -> str:
    start = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", text)
    end = re.search(r"(?m)^##\s+BASIC MCQS / REMEDIATION\s*$", text)
    if not start or not end:
        raise ValueError("Retained assembly lacks canonical Basic boundaries.")
    basic = text[start.end() : end.start()]
    matches = list(
        re.finditer(r"(?m)^###\s+SESSION\s+(\d+)\s*[—-]\s*(.+?)\s*$", basic)
    )
    if len(matches) != len(adapter.session_specs):
        raise ValueError(
            f"Retained assembly has {len(matches)} sessions; expected "
            f"{len(adapter.session_specs)}."
        )
    chunks = [basic[: matches[0].start()]]
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(basic)
        block = basic[match.end() : block_end].strip()
        block = re.sub(
            r"(?ims)^####\s+SUBTOPIC CLOSURE FLOW\s*\n+```(?:text)?\s*\n.*?\n```\s*$",
            "",
            block,
        ).strip()
        spec = adapter.session_specs[index]
        chunks.append(
            f"### SESSION {index + 1} — {spec['title']}\n\n"
            f"{contract_block(spec)}\n\n{block}\n\n{closure_block(spec)}\n\n"
        )
    return text[: start.end()] + "".join(chunks) + text[end.start() :]


def _insert_retained_advanced(
    adapter: TopicAdapter,
    text: str,
    dossier_text: str,
) -> str:
    text = re.sub(
        r"(?m)^###\s+OPTIONAL DEPTH\s+(\d+)\s*[—-]\s*(.+?)\s*$",
        lambda match: (
            f"### ADVANCED SESSION {match.group(1)} — "
            f"{adapter.advanced_session_titles[int(match.group(1)) - 1]}"
            if int(match.group(1)) <= len(adapter.advanced_session_titles)
            else f"### ADVANCED SESSION {match.group(1)} — {match.group(2)}"
        ),
        text,
    )
    marker = re.search(r"(?m)^##\s+CONSOLIDATED REGISTER NOTES\s*$", text)
    if not marker:
        raise ValueError("Retained assembly lacks final register notes.")
    fragment = philosophy_v2.demote(
        _advanced_dossier_fragment(adapter, dossier_text),
        4,
    )
    block = (
        "### ADVANCED DOSSIER REFINEMENTS — USE SELECTIVELY\n\n"
        "> **Classification: OPTIONAL ADVANCED.** This matching dossier section "
        "is unnecessary for a competent Core answer and must be used only after "
        "the complete Basic owner has been secured.\n\n"
        + fragment.strip()
        + "\n\n"
    )
    return text[: marker.start()] + block + text[marker.start() :]


def assemble_retained(
    adapter: TopicAdapter,
    retained_main: str,
    retained_workbook: str,
    dossier_text: str,
) -> str:
    assembled = philosophy_v2.assemble_legacy(
        LegacyTopic(adapter.topic_key, adapter.title),
        retained_main,
        retained_workbook,
    )
    assembled = _insert_retained_advanced(adapter, assembled, dossier_text)
    assembled = _enrich_retained_sessions(adapter, assembled)
    return strip_legacy_progress_navigation(assembled)


def _update_frontmatter(
    adapter: TopicAdapter,
    text: str,
    generation: int,
    concept_visual: Path,
    markdown_path: Path,
) -> str:
    _, body = philosophy_v2.strip_frontmatter(text)
    body = re.sub(
        r"(?m)^#\s+.+$",
        f"# {adapter.title} — Learner-v2 Source-Complete Learning Session",
        body,
        count=1,
    )
    lines = body.splitlines()
    h1_index = next(
        (index for index, line in enumerate(lines) if re.match(r"^#(?!#)\s+", line)),
        None,
    )
    if h1_index is None:
        raise ValueError("Assembled Markdown has no topic H1.")
    cursor = h1_index + 1
    while cursor < len(lines) and (
        not lines[cursor].strip() or lines[cursor].lstrip().startswith(">")
    ):
        cursor += 1
    body = "\n".join([*lines[: h1_index + 1], "", *lines[cursor:]]).lstrip()
    cover = os.path.relpath(concept_visual, markdown_path.parent).replace("\\", "/")
    frontmatter = "\n".join(
        [
            "---",
            f'title: "{adapter.title} — Learner-v2"',
            f"topic_key: {adapter.topic_key}",
            f"cover_image: {cover}",
            "variant: learner-v2",
            f"generation: {generation}",
            f"generation_date: {adapter.generation_date}",
            "---",
            "",
        ]
    )
    h1_end = body.find("\n")
    evidence = (
        f"\n\n> **Syllabus (verbatim):** {adapter.official_clause}\n>\n"
        f"> **Generation:** g{generation}, {adapter.generation_date} · "
        "**Approval:** false pending explicit topic approval\n>\n"
        "> **Evidence key:** ✅ canonical doctrine · ⚠️ analytical synthesis "
        "(for exam use) · ❓ contested/empirical claim\n>\n"
        "> **Evidence discipline:** Core follows the canonical owner and exact "
        "verified ledger; the matching advanced dossier section remains optional."
    )
    body = body[:h1_end] + evidence + body[h1_end:]
    return frontmatter + body.lstrip()


def _font(name: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    path = Path(r"C:\Windows\Fonts") / name
    return ImageFont.truetype(str(path), size) if path.is_file() else ImageFont.load_default()


def make_concept_visual(adapter: TopicAdapter, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1920, 1400
    image = Image.new("RGB", (width, height), "#09131D")
    draw = ImageDraw.Draw(image)
    title_font = _font("segoeuib.ttf", 42)
    kicker_font = _font("segoeui.ttf", 22)
    panel_font = _font("segoeuib.ttf", 23)
    body_font = _font("segoeui.ttf", 18)
    draw.text((80, 46), adapter.title.upper(), font=title_font, fill="#F2F7FB")
    draw.text((82, 108), adapter.header_kicker, font=kicker_font, fill="#72D7C2")
    colors = ("#6EC8E5", "#75D6A4", "#F0C36D", "#D69DEB")
    columns, rows = 3, 4
    gap, left, top = 24, 70, 160
    card_w = (width - left * 2 - gap * (columns - 1)) // columns
    card_h = (height - top - 60 - gap * (rows - 1)) // rows
    for index, panel in enumerate(adapter.ascii_panels):
        column, row = index % columns, index // columns
        x = left + column * (card_w + gap)
        y = top + row * (card_h + gap)
        accent = colors[index % len(colors)]
        draw.rounded_rectangle(
            (x, y, x + card_w, y + card_h),
            18,
            fill="#142330",
            outline=accent,
            width=3,
        )
        draw.text((x + 20, y + 16), f"{index:02d}", font=panel_font, fill=accent)
        title_lines = textwrap.wrap(str(panel["title"]), width=35)[:2]
        draw.multiline_text(
            (x + 72, y + 16),
            "\n".join(title_lines),
            font=panel_font,
            fill="#FFFFFF",
            spacing=4,
        )
        body_lines: list[str] = []
        for raw in panel["lines"]:
            clean = re.sub(r"\s+", " ", str(raw)).strip(" |")
            if clean:
                body_lines.extend(textwrap.wrap(clean, width=55))
            if len(body_lines) >= 6:
                break
        draw.multiline_text(
            (x + 20, y + 86),
            "\n".join(body_lines[:6]),
            font=body_font,
            fill="#D8E4EC",
            spacing=5,
        )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def _insert_concept_visual(
    adapter: TopicAdapter,
    text: str,
    concept_visual: Path,
    markdown_path: Path,
) -> str:
    marker = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", text)
    if not marker:
        raise ValueError("BASIC LEARNING SESSION is missing.")
    path = os.path.relpath(concept_visual, markdown_path.parent).replace("\\", "/")
    first = adapter.ascii_panels[0]
    block = (
        f"\n\n![{adapter.title} concept map]({path})\n\n"
        f"*Concept map: {first['title']}. The twelve authored stages preserve "
        "the topic-specific learning rail used by both master-flow formats.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def make_ascii_spec(
    adapter: TopicAdapter,
    markdown: Path,
    generation: int,
) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            f"Cārvāka-standard continuous master with the manually authored "
            f"{adapter.title} twelve-panel atlas"
        ),
        "generated_on": adapter.generation_date,
        "scope": (
            f"Philosophy Optional Paper II Socio-Political Philosophy topic "
            f"{adapter.number:02d} only"
        ),
        "constraints": {
            "panel_count_per_topic": len(adapter.ascii_panels),
            "max_line_width": 100,
            "manual_topic_specific": True,
            "english_first": True,
            "approved": False,
        },
        "topics": [
            {
                "topic_key": adapter.topic_key,
                "title": adapter.title,
                "source_markdown": relative(markdown),
                "source_record": f"{adapter.topic_key}:{V2_VARIANT}:g{generation}",
                "approved_master_reference": str(
                    carvaka_flowchart.REFERENCE_FOLDER
                    / "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ).replace("/", "\\"),
                "benchmark_preservation": (
                    "The approved design reference, all prior topic artifacts, "
                    "canonical owners and retained packages remain immutable."
                ),
                "panels": [
                    {
                        "panel_title": panel["title"],
                        "structural_type": panel["structural_type"],
                        "source_references": {"sessions": panel["sessions"]},
                        "lines": panel["lines"],
                    }
                    for panel in adapter.ascii_panels
                ],
            }
        ],
    }


def render_ascii_pdf(
    adapter: TopicAdapter,
    text: str,
    output_path: Path,
) -> dict[str, Any]:
    metrics = _base_render_ascii_pdf(text, output_path)
    temporary = output_path.with_suffix(".metadata.pdf")
    with fitz.open(output_path) as document:
        metadata = dict(document.metadata or {})
        metadata["title"] = f"{adapter.title} ASCII Master Flowchart"
        metadata["creator"] = Path(__file__).name
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError(f"{adapter.title} ASCII PDF validation failed.")
    return {**metrics, **validation}


def generation_paths(
    adapter: TopicAdapter,
    generation: int,
    output_dir: Path | None = None,
) -> dict[str, Path]:
    stem = (
        f"{adapter.topic_key}-{V2_VARIANT}-g{generation}-"
        f"{adapter.generation_date}"
    )
    ascii_spec_name = (
        f"philosophy--{adapter.section_key}-{adapter.number:02d}-ascii-"
        + (
            f"{adapter.generation_date}.json"
            if generation == 2
            else f"g{generation}-{adapter.generation_date}.json"
        )
    )
    if output_dir is None and adapter.immutable_generation_paths:
        topic_folder = f"topic-{adapter.number:02d}"
        knowledge_root = (
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Learner-v2-Refreshed"
            / "Philosophy"
            / "Socio-Political"
            / "learning-sessions"
            / topic_folder
            / f"g{generation}"
        )
        notes_root = (
            ROOT
            / "notes"
            / "Learner-v2-Refreshed"
            / "Philosophy"
            / "Socio-Political"
            / "learning-sessions"
            / topic_folder
            / f"g{generation}"
        )
        flow_root = (
            ROOT
            / "notes"
            / "Learner-v2-Refreshed"
            / "Philosophy"
            / "Socio-Political"
            / "flowcharts"
            / topic_folder
            / f"carvaka-g{generation}"
        )
        validation_root = notes_root / "validation"
        return {
            "markdown": (
                knowledge_root
                / f"{topic_folder}_Complete-Learning-Session_{adapter.generation_date}.md"
            ),
            "workbook_markdown": (
                knowledge_root
                / f"{topic_folder}_Solved-Practice-Workbook_{adapter.generation_date}.md"
            ),
            "concept_visual": (
                knowledge_root
                / "assets"
                / adapter.topic_key
                / f"{adapter.asset_slug}-map.png"
            ),
            "main_pdf": (
                notes_root
                / f"{topic_folder}_Complete-Learning-Session_{adapter.generation_date}.pdf"
            ),
            "workbook_pdf": (
                notes_root
                / f"{topic_folder}_Solved-Practice-Workbook_{adapter.generation_date}.pdf"
            ),
            "validation_root": validation_root,
            "main_visual_map": validation_root / "main-visual-audit-map.json",
            "workbook_visual_map": validation_root / "workbook-visual-audit-map.json",
            "inspection_root": validation_root / "rendered-inspection",
            "source_audit": validation_root / "source-audit.json",
            "flow_root": flow_root,
            "ascii_pdf": flow_root / "ascii-master.pdf",
            "ascii_spec": (
                ROOT
                / "upsc-ai-kit"
                / "manifests"
                / "retrofits"
                / "ascii-panel-specs"
                / ascii_spec_name
            ),
            "content_spec": CONTENT_SPEC_DIR / f"{adapter.topic_key}-g{generation}.json",
            "graphical_spec": GRAPHICAL_SPEC_DIR / f"{adapter.topic_key}-g{generation}.json",
            "record": EXPORT_MANIFEST_DIR / f"{stem}-record.json",
            "validation": EXPORT_MANIFEST_DIR / f"{stem}-validation.json",
            "changed": EXPORT_MANIFEST_DIR / f"{stem}-changed-files.txt",
        }
    if output_dir is not None:
        root = output_dir.resolve()
        knowledge_root = (
            root
            / "upsc-ai-kit"
            / "knowledge"
            / "Philosophy"
            / "learning-sessions"
            / "v2"
            / adapter.section_key
        )
        notes_root = (
            root
            / "notes"
            / "Philosophy"
            / "learning-session-v2"
            / adapter.section_key
        )
        flow_root = (
            root
            / "notes"
            / "Philosophy"
            / "flowcharts"
            / adapter.topic_key
            / f"continuous-at-a-glance-english-first-g{generation}"
        )
        validation_root = notes_root / "validation" / adapter.topic_key / f"g{generation}"
        return {
            "markdown": knowledge_root / f"{adapter.topic_key}_Learning-Session.md",
            "workbook_markdown": knowledge_root / f"{adapter.topic_key}_Solved-Workbook.md",
            "concept_visual": (
                knowledge_root
                / "assets"
                / adapter.topic_key
                / f"{adapter.asset_slug}-map.png"
            ),
            "main_pdf": (
                notes_root
                / "notes"
                / f"{adapter.topic_key}_Learning-Session_{adapter.generation_date}.pdf"
            ),
            "workbook_pdf": (
                notes_root
                / "workbooks"
                / f"{adapter.topic_key}_Solved-Workbook_{adapter.generation_date}.pdf"
            ),
            "validation_root": validation_root,
            "main_visual_map": validation_root / "main-visual-audit-map.json",
            "workbook_visual_map": validation_root / "workbook-visual-audit-map.json",
            "inspection_root": validation_root / "rendered-inspection",
            "source_audit": validation_root / "source-audit.json",
            "flow_root": flow_root,
            "ascii_pdf": flow_root / "ascii-master.pdf",
            "ascii_spec": (
                root
                / "upsc-ai-kit"
                / "manifests"
                / "retrofits"
                / "ascii-panel-specs"
                / ascii_spec_name
            ),
            "content_spec": (
                root
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / f"philosophy--{adapter.section_key}-content-specs"
                / f"{adapter.topic_key}-g{generation}.json"
            ),
            "graphical_spec": (
                root
                / "upsc-ai-kit"
                / "manifests"
                / "v2"
                / f"philosophy--{adapter.section_key}-graphical-specs"
                / f"{adapter.topic_key}-g{generation}.json"
            ),
            "record": (
                root / "upsc-ai-kit" / "manifests" / "exports" / f"{stem}-record.json"
            ),
            "validation": (
                root
                / "upsc-ai-kit"
                / "manifests"
                / "exports"
                / f"{stem}-validation.json"
            ),
            "changed": (
                root
                / "upsc-ai-kit"
                / "manifests"
                / "exports"
                / f"{stem}-changed-files.txt"
            ),
        }
    flow_root = (
        FLOW_ROOT
        / adapter.topic_key
        / f"continuous-at-a-glance-english-first-g{generation}"
    )
    validation_root = NOTES_OUTPUT / "validation" / adapter.topic_key / f"g{generation}"
    return {
        "markdown": KNOWLEDGE_OUTPUT / f"{adapter.topic_key}_Learning-Session.md",
        "workbook_markdown": KNOWLEDGE_OUTPUT / f"{adapter.topic_key}_Solved-Workbook.md",
        "concept_visual": (
            KNOWLEDGE_OUTPUT / "assets" / adapter.topic_key / f"{adapter.asset_slug}-map.png"
        ),
        "main_pdf": (
            NOTES_OUTPUT
            / "notes"
            / f"{adapter.topic_key}_Learning-Session_{adapter.generation_date}.pdf"
        ),
        "workbook_pdf": (
            NOTES_OUTPUT
            / "workbooks"
            / f"{adapter.topic_key}_Solved-Workbook_{adapter.generation_date}.pdf"
        ),
        "validation_root": validation_root,
        "main_visual_map": validation_root / "main-visual-audit-map.json",
        "workbook_visual_map": validation_root / "workbook-visual-audit-map.json",
        "inspection_root": validation_root / "rendered-inspection",
        "source_audit": validation_root / "source-audit.json",
        "flow_root": flow_root,
        "ascii_pdf": flow_root / "ascii-master.pdf",
        "ascii_spec": (
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "retrofits"
            / "ascii-panel-specs"
            / ascii_spec_name
        ),
        "content_spec": CONTENT_SPEC_DIR / f"{adapter.topic_key}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPEC_DIR / f"{adapter.topic_key}-g{generation}.json",
        "record": EXPORT_MANIFEST_DIR / f"{stem}-record.json",
        "validation": EXPORT_MANIFEST_DIR / f"{stem}-validation.json",
        "changed": EXPORT_MANIFEST_DIR / f"{stem}-changed-files.txt",
    }


def _canonical_planned_paths(adapter: TopicAdapter, generation: int) -> dict[str, str]:
    canonical = generation_paths(adapter, generation)
    return {
        "assembled_markdown": relative(canonical["markdown"]),
        "workbook_markdown": relative(canonical["workbook_markdown"]),
        "notes_pdf": relative(canonical["main_pdf"]),
        "workbook_pdf": relative(canonical["workbook_pdf"]),
        "graphical_flowchart_folder": relative(canonical["flow_root"]),
    }


def build_manifest(
    adapter: TopicAdapter,
    tracker: dict[str, Any],
    generation: int,
    ascii_spec: Path,
) -> dict[str, Any]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    topic = next(
        item for item in manifest["topics"] if item.get("topic_key") == adapter.topic_key
    )
    _, _, legacy_id = latest_identity(tracker, adapter.topic_key)
    planned = _canonical_planned_paths(adapter, generation)
    topic.update(
        {
            "display_title": adapter.title,
            "syllabus_mapping": (
                "Philosophy Optional, Paper II, Socio-Political Philosophy topic "
                f"{adapter.number}: {adapter.official_clause}"
            ),
            "source_basic": adapter.canonical_owner,
            "source_canonical": adapter.canonical_owner,
            "source_advanced": adapter.advanced_dossier,
            "cross_topic_sources": [PHILOSOPHY_README, OFFICIAL_SYLLABUS],
            "verified_pyq_sources": [adapter.pyq_ledger],
            "ascii_master_spec": relative(ascii_spec),
            "superseded_v1": legacy_id,
            **planned,
            "status": "generated_unapproved",
            "generation": generation,
            "record_id": f"{adapter.topic_key}:{V2_VARIANT}:g{generation}",
            "approved": False,
            "markdown": planned["assembled_markdown"],
            "main_pdf": planned["notes_pdf"],
            "workbook_pdf": planned["workbook_pdf"],
        }
    )
    if adapter.retained_session:
        topic["retained_learning_session"] = adapter.retained_session
    else:
        topic.pop("retained_learning_session", None)
    if adapter.retained_workbook:
        topic["retained_workbook"] = adapter.retained_workbook
    else:
        topic.pop("retained_workbook", None)
    return manifest


def _workbook_pyqs(workbook: str) -> list[str]:
    match = re.search(
        r"(?is)^###\s+(?:VERIFIED PYQS WITH MODEL SOLUTIONS|SOLVED PYQ BANK[^\n]*)"
        r"\s*(.*?)"
        r"(?=^###\s+ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS)",
        workbook,
        re.MULTILINE,
    )
    section = match.group(1) if match else workbook
    return [
        value.strip()
        for value in re.findall(r"(?m)^\*\*Question:\*\*\s*(.+?)\s*$", section)
    ]


def _owner_coverage_errors(owner: str, assembled: str) -> list[str]:
    missing: list[str] = []
    for line in owner.splitlines():
        clean = line.strip()
        if (
            len(clean) < 24
            or clean.startswith("# ")
            or re.fullmatch(r"[-|:\s]+", clean)
        ):
            continue
        if clean not in assembled:
            missing.append(clean)
    return (
        ["Canonical fallback omitted owner lines: " + " | ".join(missing[:3])]
        if missing
        else []
    )


def validate_content(
    adapter: TopicAdapter,
    assembled: str,
    workbook: str,
    standalone_ascii: str,
    source_pyqs: Sequence[str],
    ascii_spec: Path,
    owner_text: str | None = None,
) -> tuple[list[str], dict[str, Any]]:
    errors = validate_refreshed_markdown_text(
        assembled,
        topic_key=adapter.topic_key,
        ascii_spec_path=ascii_spec,
    )
    h2s = re.findall(r"(?m)^##\s+(.+?)\s*$", assembled)
    required_h2s = [
        "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION",
        "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "CONSOLIDATED REGISTER NOTES",
    ]
    if h2s != required_h2s:
        errors.append(f"Required five-H2 contract differs: {h2s}.")
    core_match = re.search(
        r"(?is)^##\s+BASIC LEARNING SESSION\s*(.*?)^##\s+BASIC MCQS / REMEDIATION",
        assembled,
        re.MULTILINE,
    )
    advanced_match = re.search(
        r"(?is)^##\s+OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\s*"
        r"(.*?)^##\s+CONSOLIDATED REGISTER NOTES",
        assembled,
        re.MULTILINE,
    )
    core = core_match.group(1) if core_match else ""
    advanced = advanced_match.group(1) if advanced_match else ""
    if adapter.official_clause not in assembled:
        errors.append("Exact official syllabus wording is missing.")
    for term in adapter.required_terms:
        if term.casefold() not in core.casefold():
            errors.append(f"Required Core term is missing: {term}")
    sessions = re.findall(r"(?m)^###\s+SESSION\s+\d+\s*[—-]", core)
    if len(sessions) != 10:
        errors.append(f"Expected 10 Core sessions, found {len(sessions)}.")
    if "ADVANCED" not in advanced.upper():
        errors.append("Matching optional Advanced material is missing.")
    progress = legacy_progress_navigation_lines(assembled)
    if progress:
        errors.append("Obsolete Progress X/Y navigation survives.")
    answers = [
        re.sub(r"\s+", " ", value).strip().casefold()
        for value in re.findall(
            r"(?ims)^####\s+ANSWER-GRABBING OPENING[^\n]*\n+>\s*(.+?)\s*$",
            core,
        )
    ]
    expected_answers = [
        re.sub(r"\s+", " ", str(spec["answer"])).strip().casefold()
        for spec in adapter.session_specs
    ]
    if answers != expected_answers:
        errors.append("Core Answer-Grabbing Lines differ from SESSION_SPECS.")
    workbook_questions = _workbook_pyqs(workbook)
    exact_source = [value.strip() for value in source_pyqs]
    missing_pyqs = [value for value in exact_source if value not in workbook_questions]
    if (
        missing_pyqs
        or len(workbook_questions) != len(exact_source)
        or set(workbook_questions) != set(exact_source)
    ):
        errors.append("Workbook PYQ wording/count differs from the controlling ledger.")
    keys = extract_mcq_answer_keys(assembled)
    expected_count = len(adapter.mcqs) if adapter.mcqs else 48
    expected_keys = ["ABCD"[index % 4] for index in range(expected_count)]
    if keys != expected_keys:
        errors.append(
            f"Expected {expected_count} MCQs in strict A-B-C-D rotation; found {len(keys)}."
        )
    errors.extend(mcq_answer_text_errors(assembled))
    if len(re.findall(r"(?m)^####\s+Original Mains\s+\d+", workbook)) < 3:
        errors.append("Workbook lacks original 10/15/20-mark Mains practice.")
    if re.search(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", assembled, re.I):
        errors.append("Placeholder text is present.")
    if owner_text is not None:
        errors.extend(_owner_coverage_errors(owner_text, assembled))
    ascii_match = re.search(
        r"(?is)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
        assembled,
        re.MULTILINE,
    )
    if not ascii_match:
        errors.append("Complete topic ASCII master is missing.")
    else:
        errors.extend(
            validate_ascii_master_text(
                ascii_match.group(1),
                topic_key=adapter.topic_key,
                ascii_spec_path=ascii_spec,
                standalone_text=standalone_ascii,
            )
        )
    audit = deep_content_quality_audit_text(assembled, topic_key=adapter.topic_key)
    return errors, {
        "core_session_count": len(sessions),
        "advanced_session_count": len(
            re.findall(r"(?m)^###\s+ADVANCED SESSION\s+\d+", advanced)
        ),
        "answer_grabbing_line_count": len(answers),
        "verified_pyq_count": len(exact_source),
        "mcq_count": len(keys),
        "original_mains_practice_count": len(
            re.findall(r"(?m)^####\s+Original Mains\s+\d+", workbook)
        ),
        "deep_quality_status": audit["status"],
        "deep_quality_severity_counts": audit["severity_counts"],
    }


def _content_spec(
    adapter: TopicAdapter,
    generation: int,
    markdown: Path,
    source_pyq_count: int,
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_on": adapter.generation_date,
        "topic_key": adapter.topic_key,
        "variant": V2_VARIANT,
        "generation": generation,
        "approval": False,
        "official_syllabus_verbatim": adapter.official_clause,
        "source_markdown": relative(markdown),
        "source_provenance": {
            "canonical_owner": adapter.canonical_owner,
            "advanced_dossier": adapter.advanced_dossier,
            "verified_pyq_ledger": adapter.pyq_ledger,
            "retained_learning_session": adapter.retained_session,
            "retained_workbook": adapter.retained_workbook,
            "successor_source_markdown": adapter.successor_markdown,
            "assembly_mode": (
                "immutable-successor-from-latest-validated-learner-v2"
                if adapter.uses_successor_package
                else (
                    "retained-legacy-via-regenerate_philosophy_indian_v2.assemble_legacy"
                    if adapter.uses_retained_package
                    else "source-complete-canonical-owner-fallback"
                )
            ),
        },
        "core_sessions": list(adapter.session_specs),
        "owner_session_ranges": {
            str(key): list(value) for key, value in adapter.owner_session_ranges.items()
        },
        "advanced_session_titles": list(adapter.advanced_session_titles),
        "ascii_panels": list(adapter.ascii_panels),
        "verified_pyq_count": source_pyq_count,
        "required_core_terms": list(adapter.required_terms),
    }


def pdf_metrics(path: Path) -> dict[str, Any]:
    with fitz.open(path) as document:
        text = "\n".join(page.get_text("text") for page in document)
        return {
            "pages": document.page_count,
            "bookmarks": len(document.get_toc(simple=True)),
            "replacement_glyphs": text.count("\ufffd"),
            "blank_pages": [
                number
                for number, page in enumerate(document, 1)
                if len(page.get_text("text").strip()) < 20
            ],
        }


def _source_paths(adapter: TopicAdapter) -> list[Path]:
    values = [
        adapter.canonical_owner,
        adapter.advanced_dossier,
        adapter.pyq_ledger,
        OFFICIAL_SYLLABUS,
        PHILOSOPHY_README,
    ]
    if adapter.retained_session:
        values.append(adapter.retained_session)
    if adapter.retained_workbook:
        values.append(adapter.retained_workbook)
    if adapter.successor_markdown:
        values.append(adapter.successor_markdown)
    return [repo_path(value) for value in values]


def _record(
    adapter: TopicAdapter,
    generation: int,
    supersedes: str,
    legacy_id: str | None,
    paths: dict[str, Path],
    flow_metadata: dict[str, Any],
    source_hashes: dict[str, str],
    outputs: Iterable[Path],
) -> dict[str, Any]:
    record_id = f"{adapter.topic_key}:{V2_VARIANT}:g{generation}"
    flow_metadata["ascii_master_source"] = (
        f"manual-authored-{adapter.asset_slug}-twelve-panel-spec"
    )
    return {
        "record_id": record_id,
        "topic_key": adapter.topic_key,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper II "
            f"— Socio-Political Philosophy — {adapter.title}"
        ),
        "main_pdf": relative(paths["main_pdf"]),
        "workbook": relative(paths["workbook_pdf"]),
        "markdown": relative(paths["markdown"]),
        "approved": False,
        "provenance": {
            "workflow": "learner-first-v2-philosophy-socio-political-topic-adapter",
            "topic_adapter": f"tools\\{adapter.module_name}.py",
            "source_basic": adapter.canonical_owner,
            "source_canonical": adapter.canonical_owner,
            "source_advanced": adapter.advanced_dossier,
            "legacy_v1_source_package": adapter.retained_session,
            "legacy_v1_workbook": adapter.retained_workbook,
            "successor_source_markdown": adapter.successor_markdown,
            "assembly_mode": (
                "immutable-successor-from-latest-validated-learner-v2"
                if adapter.uses_successor_package
                else (
                    "retained-legacy-via-regenerate_philosophy_indian_v2.assemble_legacy"
                    if adapter.uses_retained_package
                    else "source-complete-canonical-owner-fallback"
                )
            ),
            "pyq_corpus": adapter.pyq_ledger,
            "official_syllabus": OFFICIAL_SYLLABUS,
            "official_syllabus_verbatim": adapter.official_clause,
            "philosophy_readme": PHILOSOPHY_README,
            "assembled_markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "content_spec": relative(paths["content_spec"]),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": "2.1 learner-v2 indexed renderer",
            },
            "generation_date": adapter.generation_date,
            "superseded_v1": legacy_id,
            "english_first": True,
            "source_hashes": source_hashes,
            "deliverable_hashes": deliverable_hashes(outputs),
            "concept_visual": relative(paths["concept_visual"]),
            "main_visual_audit_map": relative(paths["main_visual_map"]),
            "workbook_visual_audit_map": relative(paths["workbook_visual_map"]),
            "ascii_master_pdf": relative(paths["ascii_pdf"]),
            "graphical_renderer": {
                "name": carvaka_flowchart.RENDERER_NAME,
                "version": carvaka_flowchart.RENDERER_VERSION,
            },
        },
        "approval": {"approved": False, "approved_on": None, "scope": record_id},
        "validation": {
            "state": "passed",
            "validated_on": adapter.generation_date,
            "validator": (
                "tools/generate_philosophy_socio_political_topic_v2.py + "
                "tools/validate_v2_export.py"
            ),
        },
        "generated_on": adapter.generation_date,
        "continuous_core_first": flow_metadata,
    }


def _run_command(command: list[str], description: str) -> dict[str, Any]:
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    output = (completed.stdout + "\n" + completed.stderr).strip()
    result = {
        "description": description,
        "command": subprocess.list2cmdline(command),
        "returncode": completed.returncode,
        "output_tail": output.splitlines()[-30:],
    }
    if completed.returncode:
        raise RuntimeError(f"{description} failed:\n{output}")
    return result


def _shared_files() -> list[Path]:
    index_root = NOTES_OUTPUT / "indexes"
    return [
        MANIFEST,
        TRACKER,
        GLOBAL_EXPORT_INDEX,
        V2_COMMAND_INDEX,
        PHILOSOPHY_COMMAND_INDEX,
        MASTER_LEARNING_INDEX,
        TOPIC_CATALOG,
        index_root / "TOPIC-COVERAGE-INDEX.md",
        index_root / "NOTES-PDF-INDEX.md",
        index_root / "WORKBOOK-PDF-INDEX.md",
    ]


def _snapshot(paths: Iterable[Path]) -> dict[Path, bytes | None]:
    return {path: path.read_bytes() if path.is_file() else None for path in paths}


def _restore(snapshot: dict[Path, bytes | None]) -> None:
    for path, content in snapshot.items():
        if content is None:
            if path.exists():
                path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)


def verify_final_state(
    adapter: TopicAdapter,
    generation: int,
) -> dict[str, Any]:
    errors = validate_tracker_record(
        TRACKER,
        adapter.topic_key,
        V2_VARIANT,
        generation,
        repository_root=ROOT,
        check_paths=True,
    )
    if errors:
        raise ValueError("Tracker validation failed:\n- " + "\n- ".join(errors))
    states = resolve_topic_states(ROOT, load_manifest(MANIFEST), load_tracker(TRACKER))
    if len(states) != 10:
        raise ValueError(f"Expected ten section states, found {len(states)}.")
    current = states[adapter.number - 1]
    if current.package_state != "generated":
        raise ValueError(
            f"{adapter.topic_key} state is {current.package_state!r}, expected generated."
        )
    earlier = states[: adapter.number - 1]
    if any(state.package_state != "generated" for state in earlier):
        raise ValueError("Sequential generation requires all earlier topics to be generated.")
    later = states[adapter.number :]
    if any(state.package_state not in {"planned", "generated"} for state in later):
        raise ValueError("Later topics have an invalid publication state.")
    catalog = json.loads(TOPIC_CATALOG.read_text(encoding="utf-8"))
    catalog_blob = json.dumps(catalog, ensure_ascii=False)
    if adapter.topic_key not in catalog_blob:
        raise ValueError("Topic catalogue publication omitted the topic key.")
    command = (
        "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper II — "
        f"Socio-Political Philosophy — {adapter.title} — Regenerate"
    )
    if command not in V2_COMMAND_INDEX.read_text(encoding="utf-8"):
        raise ValueError("Generation-aware topic command is missing from the guide.")
    return {
        "manifest_topic_count": len(states),
        "topic_number": adapter.number,
        "topic_state": current.package_state,
        "approval": current.approval_state,
        "validation": current.validation_state,
        "earlier_states": [state.package_state for state in earlier],
        "later_states": [state.package_state for state in later],
        "catalog_consistent": True,
        "command_index_consistent": True,
    }


def _publish(
    adapter: TopicAdapter,
    tracker: dict[str, Any],
    generation: int,
    paths: dict[str, Path],
) -> tuple[list[dict[str, Any]], dict[str, Any], set[str]]:
    shared = _shared_files()
    before = _snapshot(shared)
    try:
        write_json(
            MANIFEST,
            build_manifest(adapter, tracker, generation, paths["ascii_spec"]),
        )
        commands = [
            _run_command(
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
            ),
            _run_command(
                [
                    sys.executable,
                    str(TOOLS / "generate_v2_topic_command_catalog.py"),
                    "--repository-root",
                    str(ROOT),
                    "--guide",
                ],
                "Refresh topic catalogue and V2 command guide",
            ),
            _run_command(
                [
                    sys.executable,
                    str(TOOLS / "generate_learning_session_command_indexes.py"),
                ],
                "Refresh Philosophy and master learning-session indexes",
            ),
        ]
        state = verify_final_state(adapter, generation)
    except Exception:
        _restore(before)
        raise
    changed = {
        relative(path)
        for path, old in before.items()
        if (path.read_bytes() if path.is_file() else None) != old
    }
    return commands, state, changed


def _render_inspection(
    inspection_root: Path,
    targets: dict[str, Path],
    generated_on: str,
) -> dict[str, Any]:
    inspection_root.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, Any] = {"generated_on": generated_on, "sheets": []}
    for label, path in targets.items():
        with fitz.open(path) as document:
            for sheet_index, start in enumerate(range(0, document.page_count, 6), 1):
                pages = list(range(start, min(start + 6, document.page_count)))
                thumbs = []
                for number in pages:
                    pixmap = document[number].get_pixmap(dpi=52)
                    thumbs.append(
                        Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
                    )
                columns = 3
                rows = (len(thumbs) + columns - 1) // columns
                cell_w = max(image.width for image in thumbs) + 12
                cell_h = max(image.height for image in thumbs) + 12
                sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "#20262C")
                for position, thumb in enumerate(thumbs):
                    sheet.paste(
                        thumb,
                        (
                            (position % columns) * cell_w + 6,
                            (position // columns) * cell_h + 6,
                        ),
                    )
                output = inspection_root / f"{label}-contact-{sheet_index:02d}.png"
                sheet.save(output, "PNG")
                manifest["sheets"].append(
                    {
                        "label": label,
                        "sheet": sheet_index,
                        "source": relative(path),
                        "pages": [number + 1 for number in pages],
                        "image": relative(output),
                    }
                )
                for thumb in thumbs:
                    thumb.close()
                sheet.close()
    write_json(inspection_root / "inspection-manifest.json", manifest)
    return manifest


def run(
    topic_spec: str,
    *,
    finalize: bool = False,
    allow_supersede_learner_v2: bool = False,
    output_dir: Path | None = None,
) -> int:
    adapter = load_topic_adapter(topic_spec)
    if finalize and output_dir is not None:
        raise ValueError("--finalize cannot be combined with --output-dir.")
    if output_dir is not None:
        try:
            output_dir.resolve().relative_to(ROOT.resolve())
        except ValueError as exc:
            raise ValueError("--output-dir must remain inside the repository.") from exc
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    if tracker.get("schema_version") != 2 or not isinstance(tracker.get("exports"), list):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
    generation, supersedes, legacy_id = latest_identity(tracker, adapter.topic_key)
    existing_learner = supersedes.endswith(tuple(f":g{value}" for value in range(2, generation)))
    if existing_learner and not allow_supersede_learner_v2:
        raise ValueError(
            "A learner-v2 generation already exists; pass "
            "--allow-supersede-learner-v2 to create the next generation."
        )
    paths = generation_paths(adapter, generation, output_dir)
    immutable_targets = [
        paths["flow_root"],
        paths["ascii_spec"],
        paths["content_spec"],
        paths["graphical_spec"],
        paths["record"],
        paths["validation"],
        paths["changed"],
        paths["validation_root"],
    ]
    mutable_targets = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["concept_visual"],
        paths["main_pdf"],
        paths["workbook_pdf"],
    ]
    existing = [path for path in immutable_targets if path.exists()]
    if existing:
        raise ValueError(
            "Refusing to overwrite generation-identity targets:\n- "
            + "\n- ".join(relative(path) for path in existing)
        )
    if not allow_supersede_learner_v2:
        existing.extend(path for path in mutable_targets if path.exists())
        if existing:
            raise ValueError(
                "Refusing to overwrite learner-v2 targets:\n- "
                + "\n- ".join(relative(path) for path in existing)
            )

    owner_text = repo_path(adapter.canonical_owner).read_text(encoding="utf-8")
    dossier_text = repo_path(adapter.advanced_dossier).read_text(encoding="utf-8")
    ledger_text = repo_path(adapter.pyq_ledger).read_text(encoding="utf-8")
    source_pyqs = owner_pyqs(adapter, ledger_text)
    validate_spec_pyqs(adapter, source_pyqs)
    if adapter.uses_successor_package:
        assembled = repo_path(adapter.successor_markdown or "").read_text(
            encoding="utf-8"
        )
        fallback_owner = None
    elif adapter.uses_retained_package:
        assembled = assemble_retained(
            adapter,
            repo_path(adapter.retained_session or "").read_text(encoding="utf-8"),
            repo_path(adapter.retained_workbook or "").read_text(encoding="utf-8"),
            dossier_text,
        )
        fallback_owner = None
    else:
        assembled = assemble_canonical_fallback(
            adapter,
            owner_text,
            dossier_text,
            ledger_text,
        )
        fallback_owner = owner_text

    transform = getattr(adapter.module, "transform_assembled", None)
    if callable(transform):
        assembled = transform(
            assembled,
            owner_text=owner_text,
            generation=generation,
        )

    make_concept_visual(adapter, paths["concept_visual"])
    assembled = _update_frontmatter(
        adapter,
        assembled,
        generation,
        paths["concept_visual"],
        paths["markdown"],
    )
    assembled = _insert_concept_visual(
        adapter,
        assembled,
        paths["concept_visual"],
        paths["markdown"],
    )
    write_json(paths["ascii_spec"], make_ascii_spec(adapter, paths["markdown"], generation))
    manual = ascii_master.normalize_manual_spec_file(paths["ascii_spec"])[adapter.topic_key]
    ascii_fragment = ascii_master.build_manual_fragment(manual)
    standalone_ascii = ascii_master.standalone_panel_text(ascii_fragment)
    assembled = philosophy_v2.replace_ascii_master(assembled, ascii_fragment)
    if adapter.uses_retained_package and not adapter.uses_successor_package:
        assembled, _ = philosophy_v2.rotate_mcqs(assembled)
        assembled = re.sub(
            r"\*\*Correct answer:\s*([A-D])\.\s*(.+?)\*\*",
            r"**Answer: \1. \2**",
            assembled,
        )
    if adapter.uses_successor_package:
        assembled = re.sub(
            r"(?m)^\*\*Correct answer:\s*([A-D])\*\*\s*[—-]\s*(.+?)\s*$",
            r"**Answer: \1. \2**",
            assembled,
        )
    assembled = philosophy_v2.wrap_code_fences(assembled)
    assembled = re.sub(r"(?m)^#{5,6}\s+", "#### ", assembled)
    write_text(paths["markdown"], assembled)
    workbook = extract_v2_workbook_markdown(assembled)
    write_text(paths["workbook_markdown"], workbook)
    write_json(
        paths["content_spec"],
        _content_spec(adapter, generation, paths["markdown"], len(source_pyqs)),
    )

    content_errors, content_metrics = validate_content(
        adapter,
        assembled,
        workbook,
        standalone_ascii,
        source_pyqs,
        paths["ascii_spec"],
        fallback_owner,
    )
    if content_errors:
        raise ValueError("Content validation failed:\n- " + "\n- ".join(content_errors))

    render_root = output_dir.resolve() if output_dir is not None else ROOT
    markdown_learning_pdf.build_pdf(
        paths["markdown"],
        paths["main_pdf"],
        mode="main",
        variant=V2_VARIANT,
        topic_key=adapter.topic_key,
        repository_root=render_root,
        visual_audit_path=paths["main_visual_map"],
    )
    markdown_learning_pdf.build_pdf(
        paths["workbook_markdown"],
        paths["workbook_pdf"],
        mode="workbook",
        image_path=paths["concept_visual"],
        variant=V2_VARIANT,
        topic_key=adapter.topic_key,
        repository_root=render_root,
        visual_audit_path=paths["workbook_visual_map"],
        standalone_workbook=True,
    )
    pdf_titles = {
        paths["main_pdf"]: f"{adapter.title} - Learning Session",
        paths["workbook_pdf"]: f"{adapter.title} - Solved Practice Workbook",
        paths["flow_root"] / "poster.pdf": f"{adapter.title} - poster",
        paths["flow_root"] / "tiled.pdf": f"{adapter.title} - tiled",
        paths["ascii_pdf"]: f"{adapter.title} - ASCII Master Flowchart",
    }
    normalize_pdf_metadata(
        paths["main_pdf"],
        title=pdf_titles[paths["main_pdf"]],
        adapter=adapter,
    )
    normalize_pdf_metadata(
        paths["workbook_pdf"],
        title=pdf_titles[paths["workbook_pdf"]],
        adapter=adapter,
    )

    source_paths = _source_paths(adapter)
    source_hashes = deliverable_hashes(source_paths)
    write_json(
        paths["source_audit"],
        {
            "generated_on": adapter.generation_date,
            "topic_key": adapter.topic_key,
            "topic_title": adapter.title,
            "official_syllabus_verbatim": adapter.official_clause,
            "assembly_mode": (
                "immutable-successor-from-latest-validated-learner-v2"
                if adapter.uses_successor_package
                else (
                    "retained-legacy-via-regenerate_philosophy_indian_v2.assemble_legacy"
                    if adapter.uses_retained_package
                    else "source-complete-canonical-owner-fallback"
                )
            ),
            "source_order": [
                "Markdown canonical owner and any retained layered package",
                "OCR/PDF evidence already reconciled in source owners",
                "Live web not used for static doctrine or exact PYQ wording",
                "Qdrant not required",
            ],
            "verified_pyq_count": len(source_pyqs),
            "verified_pyqs": source_pyqs,
            "hashes": source_hashes,
        },
    )
    preservation_before = deliverable_hashes(
        [
            *source_paths,
            *[
                ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
                for name in carvaka_flowchart.REFERENCE_HASHES
            ],
        ]
    )
    graphical_panels = [
        {
            "title": panel.title,
            "structural_type": panel.structural_type,
            "body": panel.body,
            "source_references": [
                f"SESSION {number}" for number in raw["sessions"]
            ],
        }
        for panel, raw in zip(manual.panels, adapter.ascii_panels)
    ]
    graphical_data = carvaka_flowchart.author_topic_spec(
        topic_key=adapter.topic_key,
        subject="Philosophy",
        title=adapter.title,
        source_markdown=assembled.replace("...", " — ").replace("…", " — "),
        source_markdown_path=relative(paths["markdown"]),
        ascii_spec_path=relative(paths["ascii_spec"]),
        ascii_spec_sha256=sha256(paths["ascii_spec"]),
        panels=graphical_panels,
        source_generation=generation,
    )
    write_json(paths["graphical_spec"], graphical_data)
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_root"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    for flow_pdf in (paths["flow_root"] / "poster.pdf", paths["flow_root"] / "tiled.pdf"):
        normalize_pdf_metadata(
            flow_pdf,
            title=pdf_titles[flow_pdf],
            adapter=adapter,
        )
    flow_metadata["approval"] = False
    flow_metadata["ascii_master_spec"] = relative(paths["ascii_spec"])
    flow_metadata["ascii_master_spec_sha256"] = sha256(paths["ascii_spec"])
    ascii_pdf_metrics = render_ascii_pdf(adapter, standalone_ascii, paths["ascii_pdf"])
    normalize_pdf_metadata(
        paths["ascii_pdf"],
        title=pdf_titles[paths["ascii_pdf"]],
        adapter=adapter,
    )
    flow_metadata["ascii_master_pdf"] = relative(paths["ascii_pdf"])

    pdf_errors: list[str] = []
    for mode, pdf in (("main", paths["main_pdf"]), ("workbook", paths["workbook_pdf"])):
        if output_dir is None:
            pdf_errors.extend(
                validate_v2_paths(ROOT, paths["markdown"], pdf, adapter.topic_key, mode)
            )
        pdf_errors.extend(validate_pdf(pdf, variant=V2_VARIANT, mode=mode))
    main_layout_errors, main_layout = validate_pdf_layout(paths["main_pdf"])
    workbook_layout_errors, workbook_layout = validate_pdf_layout(paths["workbook_pdf"])
    pdf_errors.extend(f"main layout: {error}" for error in main_layout_errors)
    pdf_errors.extend(f"workbook layout: {error}" for error in workbook_layout_errors)
    pdf_errors.extend(
        f"graphical package: {error}" for error in render_result.validation_errors
    )
    for pdf, expected_title in pdf_titles.items():
        pdf_errors.extend(
            f"metadata: {error}"
            for error in pdf_metadata_errors(
                pdf,
                expected_title=expected_title,
                adapter=adapter,
            )
        )
    if pdf_errors:
        raise ValueError("Rendered validation failed:\n- " + "\n- ".join(pdf_errors))
    main_metrics = pdf_metrics(paths["main_pdf"])
    workbook_metrics = pdf_metrics(paths["workbook_pdf"])
    if (
        main_metrics["replacement_glyphs"]
        or workbook_metrics["replacement_glyphs"]
        or main_metrics["blank_pages"]
        or workbook_metrics["blank_pages"]
        or not main_metrics["bookmarks"]
        or not workbook_metrics["bookmarks"]
    ):
        raise ValueError("PDF metrics contain blank pages, glyph defects or missing bookmarks.")

    inspection = _render_inspection(
        paths["inspection_root"],
        {
            "main": paths["main_pdf"],
            "workbook": paths["workbook_pdf"],
            "ascii": paths["ascii_pdf"],
            "graphical": paths["flow_root"] / "tiled.pdf",
        },
        adapter.generation_date,
    )
    outputs = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["concept_visual"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["main_visual_map"],
        paths["workbook_visual_map"],
        paths["source_audit"],
        paths["ascii_pdf"],
        paths["ascii_spec"],
        paths["content_spec"],
        paths["graphical_spec"],
        *[path for path in paths["flow_root"].rglob("*") if path.is_file()],
        *[path for path in paths["inspection_root"].rglob("*") if path.is_file()],
    ]
    record = _record(
        adapter,
        generation,
        supersedes,
        legacy_id,
        paths,
        flow_metadata,
        source_hashes,
        outputs,
    )
    write_json(paths["record"], record)
    write_json(
        paths["validation"],
        {
            "schema_version": 1,
            "topic_key": adapter.topic_key,
            "generation": generation,
            "identity": record["record_id"],
            "published": False,
        },
    )

    publication_commands: list[dict[str, Any]] = []
    final_state: dict[str, Any] | None = None
    shared_changes: set[str] = set()
    if finalize:
        publication_commands, final_state, shared_changes = _publish(
            adapter,
            tracker,
            generation,
            paths,
        )

    report = {
        "schema_version": 1,
        "generated_on": adapter.generation_date,
        "identity": record["record_id"],
        "published": finalize,
        "record_id": record["record_id"],
        "topic_key": adapter.topic_key,
        "topic_title": adapter.title,
        "variant": V2_VARIANT,
        "generation": generation,
        "approval": False,
        "canonical_sequence_number": adapter.number,
        "official_syllabus_verbatim": adapter.official_clause,
        "topic_adapter": f"tools\\{adapter.module_name}.py",
        "sources": {
            "hashes": source_hashes,
            "verified_pyq_owner_count": len(source_pyqs),
            "source_audit": relative(paths["source_audit"]),
        },
        "content_validation": {
            **content_metrics,
            "required_h2_order": [
                "BASIC LEARNING SESSION",
                "BASIC MCQS / REMEDIATION",
                "PYQS AND ANSWER PRACTICE",
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                "CONSOLIDATED REGISTER NOTES",
            ],
            "register_notes_last": True,
            "session_navigation": "SESSION N only; no Progress X/Y labels",
            "core_syllabus_complete_without_advanced": True,
            "advanced_optional_and_separated": True,
            "verified_pyq_wording": "passed",
            "mcq_rotation": "A->B->C->D",
            "mcq_answer_text_key_consistency": "passed",
            "workbook_distinct": True,
            "english_first": True,
        },
        "deliverables": {
            "markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "main_pdf": relative(paths["main_pdf"]),
            "workbook_pdf": relative(paths["workbook_pdf"]),
            "concept_visual": relative(paths["concept_visual"]),
            "ascii_spec": relative(paths["ascii_spec"]),
            "content_spec": relative(paths["content_spec"]),
            "graphical_spec": relative(paths["graphical_spec"]),
            "flowchart_folder": relative(paths["flow_root"]),
            "ascii_pdf": relative(paths["ascii_pdf"]),
            "hashes": deliverable_hashes(outputs),
        },
        "pdf_validation": {
            "main": main_metrics,
            "workbook": workbook_metrics,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
        },
        "master_flow_validation": {
            "ascii_panel_count": len(manual.panels),
            "embedded_spec_equality": "passed",
            "standalone_spec_equality": "passed",
            "ascii_pdf": ascii_pdf_metrics,
            "graphical_metadata": flow_metadata,
            "graphical_validation_errors": render_result.validation_errors,
        },
        "rendered_visual_inspection": {
            "state": "generated and inspected",
            "contact_sheets": inspection["sheets"],
            "graphical_tiled_pages": render_result.audit.get("tiles", []),
        },
        "publication": {
            "requested": finalize,
            "commands": publication_commands,
            "state_verification": final_state,
        },
        "changed_files_manifest": relative(paths["changed"]),
    }
    write_json(paths["validation"], report)
    changed = {
        relative(Path(__file__)),
        f"tools\\{adapter.module_name}.py",
        relative(paths["record"]),
        relative(paths["validation"]),
        relative(paths["changed"]),
        *[relative(path) for path in outputs if path.is_file()],
        *shared_changes,
    }
    write_text(paths["changed"], "\n".join(sorted(changed, key=str.casefold)) + "\n")
    print(
        f"COMPLETE: {record['record_id']}; publication="
        f"{'finalized' if finalize else 'not requested'}; changed-file inventory: "
        f"{relative(paths['changed'])}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--topic-spec",
        required=True,
        help="Importable topic adapter/spec module name.",
    )
    parser.add_argument(
        "--finalize",
        action="store_true",
        help="Publish the validated record to tracker, manifests, catalog and indexes.",
    )
    parser.add_argument(
        "--allow-supersede-learner-v2",
        action="store_true",
        help="Allow creation of the next learner-v2 generation when one already exists.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Generate an isolated, non-publishable package under this directory.",
    )
    args = parser.parse_args()
    try:
        return run(
            args.topic_spec,
            finalize=args.finalize,
            allow_supersede_learner_v2=args.allow_supersede_learner_v2,
            output_dir=args.output_dir,
        )
    except (
        OSError,
        ValueError,
        RuntimeError,
        json.JSONDecodeError,
        carvaka_flowchart.CarvakaError,
    ) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
