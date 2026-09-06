"""Export the latest validated learner packages into a simple four-item library.

The exporter is deliberately read-only with respect to the source tracker and
all source artifacts.  Each topic is built in a staging directory, validated,
and swapped into place as one unit.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
import unicodedata
import uuid
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence
from urllib.parse import quote, unquote


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPORT_ROOT = (
    REPOSITORY_ROOT / "notes" / "Final-Learning-Packages"
)
DEFAULT_TRACKER = REPOSITORY_ROOT / "EXPORT-PDF-STATUS.json"
DEFAULT_CATALOGUE = (
    REPOSITORY_ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "topic-catalog.json"
)
DEFAULT_MANIFEST_DIR = (
    REPOSITORY_ROOT / "upsc-ai-kit" / "manifests" / "exports"
)
LEARNER_VARIANT = "learner-v2"
GRAPHICAL_RENDERER = "carvaka-continuous-at-a-glance-graphical-v2"
ASCII_SOURCE_KIND = "manual-authored-spec"
ESSAY_CONTRACT = "essay-specific-guide-v2"
APPROVAL_STATE = "Approval pending"
MAX_TOPIC_SLUG_LENGTH = 80
WINDOWS_SAFE_LIBRARY_PATH_LENGTH = 240

TOPIC_DELIVERABLES: dict[str, tuple[str, ...]] = {
    "01-Complete-Learning-Session": ("Complete-Learning-Session.pdf",),
    "02-Solved-Practice-Workbook": ("Solved-Practice-Workbook.pdf",),
    "03-Carvaka-Graphical-Flowchart": (
        "At-a-Glance-Poster.pdf",
        "Printable-Tiled-Version.pdf",
        "High-Resolution-Master.png",
    ),
    "04-ASCII-Master-Flowchart": (
        "ASCII-Master-Flowchart.pdf",
        "ASCII-Master-Flowchart.txt",
    ),
}

ESSAY_DELIVERABLES: dict[str, tuple[str, ...]] = {
    "01-Knowledge-Guide": ("Knowledge-Guide.pdf",),
    "02-Practice-Workbook": ("Practice-Workbook.pdf",),
    "03-Practice-Solutions": ("Practice-Solutions.pdf",),
    "04-Integrated-Workflow-Atlas": ("Essay-Workflow-Atlas.png",),
}

COPIED_ARTIFACTS: tuple[tuple[str, str, str], ...] = (
    (
        "complete_learning_session",
        "main_pdf",
        "01-Complete-Learning-Session/Complete-Learning-Session.pdf",
    ),
    (
        "solved_practice_workbook",
        "workbook",
        "02-Solved-Practice-Workbook/Solved-Practice-Workbook.pdf",
    ),
    (
        "graphical_poster",
        "continuous_core_first.poster_pdf",
        "03-Carvaka-Graphical-Flowchart/At-a-Glance-Poster.pdf",
    ),
    (
        "graphical_tiled",
        "continuous_core_first.tiled_pdf",
        "03-Carvaka-Graphical-Flowchart/Printable-Tiled-Version.pdf",
    ),
    (
        "graphical_master",
        "continuous_core_first.master_image",
        "03-Carvaka-Graphical-Flowchart/High-Resolution-Master.png",
    ),
    (
        "ascii_master_text",
        "continuous_core_first.ascii_master",
        "04-ASCII-Master-Flowchart/ASCII-Master-Flowchart.txt",
    ),
)

ESSAY_COPIED_ARTIFACTS: tuple[tuple[str, str, str], ...] = (
    (
        "knowledge_guide",
        "main_pdf",
        "01-Knowledge-Guide/Knowledge-Guide.pdf",
    ),
    (
        "practice_workbook",
        "workbook",
        "02-Practice-Workbook/Practice-Workbook.pdf",
    ),
    (
        "practice_solutions",
        "solutions_pdf",
        "03-Practice-Solutions/Practice-Solutions.pdf",
    ),
    (
        "workflow_atlas",
        "integrated_visual_atlas",
        "04-Integrated-Workflow-Atlas/Essay-Workflow-Atlas.png",
    ),
)

PANEL_HEADING_RE = re.compile(
    r"^ASCII MASTER FLOW — PANEL (\d+)/(\d+): (.+?)\s*$",
    re.MULTILINE,
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FORBIDDEN_PATH_RE = re.compile(
    r"(?:^|[\\/])g\d+(?:[\\/]|$)|"
    r"compatibility[- ]pilot|learner[- ]?v2",
    re.IGNORECASE,
)
WINDOWS_RESERVED = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    *(f"COM{number}" for number in range(1, 10)),
    *(f"LPT{number}" for number in range(1, 10)),
}


class ExportError(RuntimeError):
    """Raised when a safe, unambiguous export cannot be completed."""


def manual_ascii_source(value: object) -> bool:
    return bool(
        isinstance(value, str)
        and (
            value == ASCII_SOURCE_KIND
            or re.fullmatch(r"manual-authored-[A-Za-z0-9-]+-spec", value)
        )
    )


def essay_specific_record(record: dict[str, Any]) -> bool:
    return record.get("artifact_contract") == ESSAY_CONTRACT


def essay_navigation_links(topic: dict[str, Any]) -> bool:
    """Use the essay layout only when its retained navigation links are complete."""

    links = topic.get("links") or {}
    return (
        topic.get("artifact_contract") == ESSAY_CONTRACT
        and all(
            key in links
            for key in (
                "knowledge_guide",
                "practice_workbook",
                "workflow_atlas",
                "practice_solutions",
            )
        )
    )


def deliverables_for_record(
    record: dict[str, Any],
) -> dict[str, tuple[str, ...]]:
    return (
        ESSAY_DELIVERABLES
        if essay_specific_record(record)
        else TOPIC_DELIVERABLES
    )


def copied_artifacts_for_record(
    record: dict[str, Any],
) -> tuple[tuple[str, str, str], ...]:
    return (
        ESSAY_COPIED_ARTIFACTS
        if essay_specific_record(record)
        else COPIED_ARTIFACTS
    )


@dataclass(frozen=True)
class CatalogueTopic:
    topic_key: str
    title: str
    subject: str
    section: str
    number: int | None
    subject_order: int
    section_order: int
    topic_order: int


@dataclass(frozen=True)
class ExportSelection:
    record: dict[str, Any]
    catalogue: CatalogueTopic
    subject_folder: str
    section_folder: str
    topic_folder: str

    @property
    def topic_key(self) -> str:
        return str(self.record["topic_key"])

    @property
    def destination_relative(self) -> Path:
        return (
            Path(self.subject_folder)
            / self.section_folder
            / self.topic_folder
        )


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ExportError(f"Required JSON file is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ExportError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ExportError(f"Expected a JSON object in {path}")
    return data


def replace_with_retry(source: Path, destination: Path) -> None:
    """Perform an atomic replace while tolerating transient Windows file locks."""
    for attempt in range(20):
        try:
            os.replace(source, destination)
            return
        except PermissionError:
            if attempt == 19:
                raise
            time.sleep(0.1 * (attempt + 1))


def write_json_atomic(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{uuid.uuid4().hex}")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    replace_with_retry(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{uuid.uuid4().hex}")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    replace_with_retry(temporary, path)


def filesystem_io_path(path: Path) -> Path:
    """Return a Windows extended path so file I/O is not limited by MAX_PATH."""
    if os.name != "nt":
        return path
    resolved = str(path.resolve())
    if resolved.startswith("\\\\?\\"):
        return Path(resolved)
    if resolved.startswith("\\\\"):
        return Path("\\\\?\\UNC\\" + resolved[2:])
    return Path("\\\\?\\" + resolved)


def file_is_file(path: Path) -> bool:
    return filesystem_io_path(path).is_file()


def file_size(path: Path) -> int:
    return filesystem_io_path(path).stat().st_size


def read_text_file(path: Path, *, encoding: str) -> str:
    return filesystem_io_path(path).read_text(encoding=encoding)


def iter_files(path: Path) -> Iterable[Path]:
    for directory, _, filenames in os.walk(filesystem_io_path(path)):
        yield from (Path(directory) / filename for filename in filenames)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with filesystem_io_path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def repository_relative(path: Path, root: Path = REPOSITORY_ROOT) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("/", "\\")


def resolve_repository_path(root: Path, value: str) -> Path:
    return root / Path(value.replace("\\", "/"))


def nested_value(record: dict[str, Any], dotted_key: str) -> Any:
    value: Any = record
    for key in dotted_key.split("."):
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def sanitize_display_component(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    value = re.sub(r"-{2,}", "-", value)
    if not value:
        raise ExportError("A display path component sanitized to an empty name.")
    if value.upper() in WINDOWS_RESERVED:
        value = f"{value}-Topic"
    return value


def raw_topic_slug(value: str) -> str:
    value = re.sub(r"[‐‑‒–—―]", "-", value)
    value = value.replace("’", "").replace("'", "")
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_value = decomposed.encode("ascii", "ignore").decode("ascii")
    ascii_value = ascii_value.replace("&", " and ")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_value).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    if not slug:
        raise ExportError(f"Topic title cannot form a readable slug: {value!r}")
    return slug


def bound_slug(slug: str, maximum_length: int) -> str:
    if maximum_length < 18:
        raise ExportError(
            f"Topic slug budget is too small for a collision-safe name: "
            f"{maximum_length}"
        )
    if len(slug) > maximum_length:
        digest = hashlib.sha256(slug.encode("utf-8")).hexdigest()[:8]
        text_budget = maximum_length - len(digest) - 2
        tail_budget = min(32, text_budget // 2)
        head_budget = text_budget - tail_budget
        head = slug[:head_budget].rstrip("-")
        if "-" in head:
            head = head.rsplit("-", 1)[0]
        tail_raw = slug[-tail_budget:]
        tail = tail_raw.lstrip("-")
        if not tail_raw.startswith("-") and "-" in tail:
            tail = tail.split("-", 1)[1]
        slug = f"{head}-{digest}-{tail}"
        if len(slug) > maximum_length:
            slug = slug[:maximum_length].rstrip("-")
    return slug


def slugify_topic(value: str) -> str:
    return bound_slug(raw_topic_slug(value), MAX_TOPIC_SLUG_LENGTH)


def canonical_topic_folder(
    prefix: str,
    title: str,
    *,
    export_root: Path,
    subject_folder: str,
    section_folder: str,
) -> str:
    """Return the one Windows-safe topic folder used by every output surface."""
    base = (export_root / subject_folder / section_folder).resolve()
    suffixes = [
        Path("README.txt"),
        *[
            Path(directory) / filename
            for directory, filenames in TOPIC_DELIVERABLES.items()
            for filename in filenames
        ],
    ]
    longest_suffix = max(len(str(suffix)) for suffix in suffixes)
    maximum_folder_length = (
        WINDOWS_SAFE_LIBRARY_PATH_LENGTH
        - len(str(base))
        - 2
        - longest_suffix
    )
    slug_budget = maximum_folder_length - len(prefix) - 1
    slug = bound_slug(raw_topic_slug(title), slug_budget)
    folder = f"{prefix}-{slug}"
    longest_path = max(
        len(str((base / folder / suffix).resolve()))
        for suffix in suffixes
    )
    if longest_path > WINDOWS_SAFE_LIBRARY_PATH_LENGTH:
        raise ExportError(
            f"{prefix}: canonical destination exceeds the Windows-safe path "
            f"limit ({longest_path} > {WINDOWS_SAFE_LIBRARY_PATH_LENGTH})."
        )
    return folder


def load_catalogue_topics(path: Path) -> dict[str, list[CatalogueTopic]]:
    data = load_json(path)
    raw_topics = data.get("topics")
    if not isinstance(raw_topics, list):
        raise ExportError(f"Catalogue has no topics array: {path}")
    mapped: dict[str, list[CatalogueTopic]] = defaultdict(list)
    for raw in raw_topics:
        if not isinstance(raw, dict):
            continue
        subject = raw.get("subject") or {}
        section = raw.get("section") or {}
        topic_key = str(raw.get("topic_key") or "")
        title = str(raw.get("display_title") or "")
        subject_name = str(subject.get("display_name") or "")
        section_name = str(section.get("name") or "")
        if not all((topic_key, title, subject_name, section_name)):
            continue
        number_value = raw.get("source_number")
        number = int(number_value) if number_value is not None else None
        topic = CatalogueTopic(
            topic_key=topic_key,
            title=title,
            subject=subject_name,
            section=section_name,
            number=number,
            subject_order=int(subject.get("order") or 9999),
            section_order=int(section.get("order") or 9999),
            topic_order=int(raw.get("topic_order") or number or 9999),
        )
        keys = [topic_key, *(raw.get("tracker_topic_keys") or [])]
        for key in keys:
            if key:
                mapped[str(key)].append(topic)
    return mapped


def latest_learner_records(
    tracker_data: dict[str, Any],
    selected_keys: Sequence[str] | None = None,
) -> list[dict[str, Any]]:
    raw_exports = tracker_data.get("exports")
    if not isinstance(raw_exports, list):
        raise ExportError("Tracker has no exports array.")
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in raw_exports:
        if (
            isinstance(record, dict)
            and record.get("variant") == LEARNER_VARIANT
            and record.get("topic_key")
        ):
            grouped[str(record["topic_key"])].append(record)
    latest = {
        key: max(records, key=lambda item: int(item.get("generation") or 0))
        for key, records in grouped.items()
    }
    if selected_keys:
        requested = list(dict.fromkeys(selected_keys))
        unknown = sorted(set(requested) - set(latest))
        if unknown:
            raise ExportError(
                "Unknown learner-v2 topic key(s): " + ", ".join(unknown)
            )
        records = [latest[key] for key in requested]
    else:
        records = list(latest.values())
    return records


def validate_source_record(root: Path, record: dict[str, Any]) -> None:
    topic_key = str(record.get("topic_key") or "<unknown>")
    generation = int(record.get("generation") or 0)
    validation = record.get("validation") or {}
    if validation.get("state") != "passed":
        raise ExportError(
            f"{topic_key} g{generation}: latest tracker validation is not passed."
        )
    if record.get("approved") is not False:
        raise ExportError(
            f"{topic_key} g{generation}: approval must remain pending."
        )
    if essay_specific_record(record):
        for _, source_key, _ in ESSAY_COPIED_ARTIFACTS:
            value = nested_value(record, source_key)
            if not isinstance(value, str) or not value:
                raise ExportError(
                    f"{topic_key} g{generation}: missing tracker field {source_key}."
                )
            source = resolve_repository_path(root, value)
            if not source.is_file():
                raise ExportError(
                    f"{topic_key} g{generation}: artifact does not exist: {value}"
                )
        if not record.get("integrated_ascii_flow"):
            raise ExportError(
                f"{topic_key} g{generation}: integrated Essay ASCII workflow is missing."
            )
        return
    graphical = record.get("continuous_core_first")
    if not isinstance(graphical, dict):
        raise ExportError(
            f"{topic_key} g{generation}: tracker lacks graphical metadata."
        )
    renderer = graphical.get("renderer") or {}
    if renderer.get("name") != GRAPHICAL_RENDERER:
        raise ExportError(
            f"{topic_key} g{generation}: latest graphical renderer is "
            f"{renderer.get('name')!r}, expected {GRAPHICAL_RENDERER!r}."
        )
    if not manual_ascii_source(graphical.get("ascii_master_source")):
        raise ExportError(
            f"{topic_key} g{generation}: standalone ASCII master is not "
            "the manually authored tracker-selected artifact."
        )
    for _, source_key, _ in COPIED_ARTIFACTS:
        value = nested_value(record, source_key)
        if not isinstance(value, str) or not value:
            raise ExportError(
                f"{topic_key} g{generation}: missing tracker field {source_key}."
            )
        source = resolve_repository_path(root, value)
        if not source.is_file():
            raise ExportError(
                f"{topic_key} g{generation}: artifact does not exist: {value}"
            )


def resolve_selections(
    root: Path,
    tracker_path: Path,
    catalogue_path: Path,
    selected_keys: Sequence[str] | None = None,
    *,
    export_root: Path | None = None,
) -> list[ExportSelection]:
    tracker = load_json(tracker_path)
    records = latest_learner_records(tracker, selected_keys)
    catalogue = load_catalogue_topics(catalogue_path)
    destination_root = (
        export_root
        if export_root is not None
        else root / "notes" / "Final-Learning-Packages"
    )
    selections: list[ExportSelection] = []
    destination_owners: dict[str, str] = {}
    for record in records:
        validate_source_record(root, record)
        topic_key = str(record["topic_key"])
        matches = catalogue.get(topic_key, [])
        unique = {
            (
                item.topic_key,
                item.title,
                item.subject,
                item.section,
                item.number,
            ): item
            for item in matches
        }
        if len(unique) != 1:
            raise ExportError(
                f"{topic_key}: expected one catalogue match, found {len(unique)}."
            )
        item = next(iter(unique.values()))
        prefix = (
            f"{item.number:02d}"
            if item.number is not None
            else f"{item.topic_order:02d}"
        )
        subject_folder = sanitize_display_component(item.subject)
        section_folder = sanitize_display_component(item.section)
        selection = ExportSelection(
            record=record,
            catalogue=item,
            subject_folder=subject_folder,
            section_folder=section_folder,
            topic_folder=canonical_topic_folder(
                prefix,
                item.title,
                export_root=destination_root,
                subject_folder=subject_folder,
                section_folder=section_folder,
            ),
        )
        destination_key = str(selection.destination_relative).casefold()
        previous_owner = destination_owners.get(destination_key)
        if previous_owner is not None:
            raise ExportError(
                "Sanitized destination collision between "
                f"{previous_owner!r} and {topic_key!r}: "
                f"{selection.destination_relative}"
            )
        destination_owners[destination_key] = topic_key
        user_path = str(selection.destination_relative)
        if FORBIDDEN_PATH_RE.search(user_path):
            raise ExportError(
                f"{topic_key}: internal generation jargon leaked into {user_path!r}."
            )
        selections.append(selection)
    return sorted(
        selections,
        key=lambda item: (
            item.catalogue.subject_order,
            item.catalogue.subject.casefold(),
            item.catalogue.section_order,
            item.catalogue.section.casefold(),
            item.catalogue.topic_order,
            item.catalogue.title.casefold(),
        ),
    )


def split_ascii_panels(text: str) -> list[str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    matches = list(PANEL_HEADING_RE.finditer(normalized))
    if not matches:
        raise ExportError("ASCII master contains no authored panel headings.")
    panels: list[str] = []
    expected_total = int(matches[0].group(2))
    if len(matches) != expected_total:
        raise ExportError(
            f"ASCII master declares {expected_total} panels but contains "
            f"{len(matches)} headings."
        )
    for index, match in enumerate(matches, 1):
        panel_number = int(match.group(1))
        panel_total = int(match.group(2))
        if panel_number != index or panel_total != expected_total:
            raise ExportError(
                "ASCII master panel numbering/order is inconsistent."
            )
        end = matches[index].start() if index < len(matches) else len(normalized)
        panels.append(normalized[match.start() : end].strip("\n"))
    return panels


def normalize_ascii_content(text: str) -> str:
    normalized = unicodedata.normalize(
        "NFKC", text.replace("\r\n", "\n").replace("\r", "\n")
    )
    lines = [line.rstrip() for line in normalized.splitlines()]
    return "\n".join(line for line in lines if line.strip())


def _register_ascii_fonts() -> tuple[str, str]:
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    regular_name = "FinalLibraryConsolas"
    bold_name = "FinalLibraryConsolasBold"
    registered = set(pdfmetrics.getRegisteredFontNames())
    if regular_name not in registered:
        regular = Path(r"C:\Windows\Fonts\consola.ttf")
        bold = Path(r"C:\Windows\Fonts\consolab.ttf")
        if not regular.is_file() or not bold.is_file():
            raise ExportError("Required Consolas fonts are unavailable.")
        pdfmetrics.registerFont(TTFont(regular_name, str(regular)))
        pdfmetrics.registerFont(TTFont(bold_name, str(bold)))
    return regular_name, bold_name


def render_ascii_pdf(text: str, output_path: Path) -> dict[str, Any]:
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfgen import canvas

    panels = split_ascii_panels(text)
    regular_font, bold_font = _register_ascii_fonts()
    page_width, page_height = landscape(A4)
    margin_x = 34.0
    margin_y = 32.0
    maximum_font = 10.5
    minimum_font = 9.0
    maximum_authored_line = 100
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(
        str(output_path),
        pagesize=(page_width, page_height),
        pageCompression=1,
    )
    pdf.setTitle("ASCII Master Flowchart")
    pdf.setCreator("export_four_item_library.py")
    page_metrics: list[dict[str, Any]] = []
    for panel_index, panel in enumerate(panels, 1):
        lines = panel.splitlines()
        overlong = [
            (line_index + 1, len(line))
            for line_index, line in enumerate(lines)
            if line_index > 0 and len(line) > maximum_authored_line
        ]
        if overlong:
            details = ", ".join(
                f"line {line_number}={length}"
                for line_number, length in overlong[:5]
            )
            raise ExportError(
                f"ASCII panel {panel_index} exceeds the authored "
                f"{maximum_authored_line}-character frame: {details}."
            )
        widest_at_one = max(
            pdfmetrics.stringWidth(
                line,
                bold_font if line_index == 0 else regular_font,
                1.0,
            )
            for line_index, line in enumerate(lines)
        )
        width_font = (
            (page_width - 2 * margin_x) / widest_at_one
            if widest_at_one
            else maximum_font
        )
        height_font = (
            (page_height - 2 * margin_y)
            / max(1.0, len(lines) * 1.35)
        )
        font_size = min(maximum_font, width_font, height_font)
        if font_size < minimum_font:
            raise ExportError(
                f"ASCII panel {panel_index} would require unreadable "
                f"{font_size:.2f} pt text."
            )
        leading = font_size * 1.35
        pdf.setFillColor(HexColor("#F8FAFC"))
        pdf.rect(0, 0, page_width, page_height, stroke=0, fill=1)
        header_height = leading + 16
        pdf.setFillColor(HexColor("#17324D"))
        pdf.roundRect(
            margin_x - 8,
            page_height - margin_y - header_height + 5,
            page_width - 2 * margin_x + 16,
            header_height,
            6,
            stroke=0,
            fill=1,
        )
        title_y = page_height - margin_y - font_size
        pdf.setFillColor(HexColor("#FFFFFF"))
        pdf.setFont(bold_font, font_size)
        pdf.drawString(margin_x, title_y, lines[0])
        pdf.setFillColor(HexColor("#172B3A"))
        text_object = pdf.beginText()
        text_object.setTextOrigin(margin_x, title_y - leading)
        text_object.setFont(regular_font, font_size)
        text_object.setLeading(leading)
        for line in lines[1:]:
            text_object.textLine(line)
        pdf.drawText(text_object)
        pdf.setStrokeColor(HexColor("#B7C5D1"))
        pdf.roundRect(
            margin_x - 12,
            margin_y - 8,
            page_width - 2 * margin_x + 24,
            page_height - 2 * margin_y + 16,
            7,
            stroke=1,
            fill=0,
        )
        page_metrics.append(
            {
                "page": panel_index,
                "line_count": len(lines),
                "maximum_line_characters": max(map(len, lines)),
                "font_size_points": round(font_size, 2),
                "page_size_points": [
                    round(page_width, 2),
                    round(page_height, 2),
                ],
            }
        )
        pdf.showPage()
    pdf.save()
    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ExportError(
            f"Generated ASCII PDF failed validation: "
            + " | ".join(validation["errors"])
        )
    return {
        **validation,
        "page_metrics": page_metrics,
        "minimum_font_size_points": min(
            page["font_size_points"] for page in page_metrics
        ),
    }


def validate_ascii_pdf(text: str, pdf_path: Path) -> dict[str, Any]:
    try:
        import fitz
    except ImportError as exc:
        raise ExportError(f"PyMuPDF is required: {exc}") from exc

    panels = split_ascii_panels(text)
    errors: list[str] = []
    extracted_panels: list[str] = []
    clipped_pages: list[int] = []
    replacement_pages: list[int] = []
    blank_pages: list[int] = []
    with fitz.open(filesystem_io_path(pdf_path)) as document:
        page_count = document.page_count
        if page_count != len(panels):
            errors.append(
                f"ASCII PDF has {page_count} pages for {len(panels)} panels."
            )
        for page_number, page in enumerate(document, 1):
            extracted = page.get_text("text")
            extracted_panels.append(extracted)
            if not extracted.strip():
                blank_pages.append(page_number)
            if "\ufffd" in extracted or "�" in extracted:
                replacement_pages.append(page_number)
            rect = page.rect
            for block in page.get_text("blocks"):
                x0, y0, x1, y1 = block[:4]
                if (
                    x0 < rect.x0 - 0.5
                    or y0 < rect.y0 - 0.5
                    or x1 > rect.x1 + 0.5
                    or y1 > rect.y1 + 0.5
                ):
                    clipped_pages.append(page_number)
                    break
            pixmap = page.get_pixmap(
                matrix=fitz.Matrix(0.25, 0.25),
                alpha=False,
            )
            del pixmap
        page = None
    for index, (source_panel, extracted_panel) in enumerate(
        zip(panels, extracted_panels), 1
    ):
        if normalize_ascii_content(source_panel) != normalize_ascii_content(
            extracted_panel
        ):
            errors.append(
                f"ASCII PDF page {index} does not normalize equal to panel {index}."
            )
    if blank_pages:
        errors.append(f"ASCII PDF blank pages: {blank_pages}.")
    if replacement_pages:
        errors.append(
            f"ASCII PDF replacement glyph pages: {replacement_pages}."
        )
    if clipped_pages:
        errors.append(f"ASCII PDF clipped pages: {clipped_pages}.")
    return {
        "passed": not errors,
        "errors": errors,
        "text_panel_count": len(panels),
        "pdf_panel_count": len(extracted_panels),
        "pdf_page_count": len(extracted_panels),
        "normalized_equal": not any(
            "normalize equal" in error for error in errors
        ),
        "blank_pages": blank_pages,
        "replacement_glyph_pages": replacement_pages,
        "clipped_pages": clipped_pages,
    }


def pdf_layout_validation(path: Path) -> tuple[list[str], dict[str, Any]]:
    tools_path = str(REPOSITORY_ROOT / "tools")
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    try:
        from validate_v2_export import validate_pdf_layout
    except ImportError as exc:
        raise ExportError(
            f"Existing PDF layout validator is unavailable: {exc}"
        ) from exc
    return validate_pdf_layout(path)


def png_validation(path: Path) -> dict[str, Any]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise ExportError(f"Pillow is required: {exc}") from exc
    try:
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            dimensions = list(image.size)
            mode = image.mode
    except Exception as exc:
        raise ExportError(f"PNG validation failed for {path}: {exc}") from exc
    return {"dimensions": dimensions, "mode": mode, "valid": True}


def markdown_link(target: Path, label: str) -> str:
    encoded = quote(target.as_posix(), safe="/-._~")
    return f"[{label}]({encoded})"


def topic_readme(selection: ExportSelection) -> str:
    record = selection.record
    number = (
        f"{selection.catalogue.number:02d}"
        if selection.catalogue.number is not None
        else "Not specified"
    )
    command = (
        f"Open final package: {selection.catalogue.subject} — "
        f"{selection.catalogue.section} — {selection.catalogue.title}"
    )
    if essay_specific_record(record):
        return (
            "FINAL ESSAY LEARNING PACKAGE\n"
            "============================\n\n"
            f"Topic: {selection.catalogue.title}\n"
            f"Subject: {selection.catalogue.subject}\n"
            f"Section: {selection.catalogue.section}\n"
            f"Catalogue number: {number}\n"
            f"Source record ID: {record['record_id']}\n"
            f"Source generation: {record['generation']}\n"
            f"Approval: {APPROVAL_STATE}\n\n"
            "Essay-specific deliverables\n"
            "---------------------------\n"
            "1. Complete Knowledge Guide — indexed PDF\n"
            "2. Question-only Practice Workbook — indexed PDF\n"
            "3. Separate Practice Solutions — indexed PDF\n"
            "4. Integrated Workflow Atlas — PNG; the matching ASCII workflow "
            "is embedded in the guide\n\n"
            "This package intentionally has no artificial learning-session "
            "sequence and no MCQs.\n\n"
            f"Navigation command: {command}\n"
        )
    return (
        "FINAL LEARNING PACKAGE\n"
        "======================\n\n"
        f"Topic: {selection.catalogue.title}\n"
        f"Subject: {selection.catalogue.subject}\n"
        f"Section: {selection.catalogue.section}\n"
        f"Catalogue number: {number}\n"
        f"Source record ID: {record['record_id']}\n"
        f"Source generation: {record['generation']}\n"
        f"Approval: {APPROVAL_STATE}\n\n"
        "Deliverables\n"
        "------------\n"
        "1. Complete Learning Session — PDF\n"
        "2. Solved Practice Workbook — PDF\n"
        "3. Carvaka Graphical Flowchart — poster PDF, printable tiled PDF, "
        "and high-resolution PNG\n"
        "4. ASCII Master Flowchart — standalone PDF and authored text\n\n"
        f"Navigation command: {command}\n"
    )


def prepare_topic_stage(
    root: Path,
    selection: ExportSelection,
    stage: Path,
    *,
    full_pdf_validation: bool,
) -> dict[str, Any]:
    record = selection.record
    if essay_specific_record(record):
        return prepare_essay_topic_stage(
            root,
            selection,
            stage,
            full_pdf_validation=full_pdf_validation,
        )
    stage.mkdir(parents=True, exist_ok=False)
    for directory, filenames in TOPIC_DELIVERABLES.items():
        deliverable = stage / directory
        deliverable.mkdir()
        if not filenames:
            raise ExportError(f"Deliverable definition is empty: {directory}")

    source_hashes_before: dict[str, str] = {}
    artifact_records: dict[str, dict[str, Any]] = {}
    for name, source_key, output_relative in COPIED_ARTIFACTS:
        source_value = str(nested_value(record, source_key))
        source = resolve_repository_path(root, source_value)
        destination = stage / Path(output_relative)
        source_hash = sha256_file(source)
        source_hashes_before[name] = source_hash
        shutil.copy2(source, destination)
        output_hash = sha256_file(destination)
        if output_hash != source_hash:
            raise ExportError(
                f"{selection.topic_key}: byte equality failed for {name}."
            )
        artifact_records[name] = {
            "source": repository_relative(source, root),
            "output": output_relative.replace("/", "\\"),
            "source_sha256": source_hash,
            "output_sha256": output_hash,
            "source_output_equal": True,
            "bytes": destination.stat().st_size,
        }


    ascii_text_path = (
        stage
        / "04-ASCII-Master-Flowchart"
        / "ASCII-Master-Flowchart.txt"
    )
    ascii_pdf_path = (
        stage
        / "04-ASCII-Master-Flowchart"
        / "ASCII-Master-Flowchart.pdf"
    )
    ascii_text = ascii_text_path.read_text(encoding="utf-8")
    tracked_ascii_pdf = nested_value(
        record, "continuous_core_first.ascii_master_pdf"
    )
    if isinstance(tracked_ascii_pdf, str) and tracked_ascii_pdf:
        ascii_pdf_source = resolve_repository_path(root, tracked_ascii_pdf)
        if not ascii_pdf_source.is_file():
            raise ExportError(
                f"{selection.topic_key}: tracked ASCII PDF is missing: "
                f"{tracked_ascii_pdf}"
            )
        shutil.copy2(ascii_pdf_source, ascii_pdf_path)
        ascii_validation = validate_ascii_pdf(ascii_text, ascii_pdf_path)
        if not ascii_validation["passed"]:
            raise ExportError(
                f"{selection.topic_key}: tracked ASCII PDF validation failed: "
                + " | ".join(ascii_validation["errors"])
            )
        try:
            import fitz
        except ImportError as exc:
            raise ExportError(f"PyMuPDF is required: {exc}") from exc
        panel_sources = split_ascii_panels(ascii_text)
        page_metrics: list[dict[str, Any]] = []
        font_sizes: list[float] = []
        with fitz.open(ascii_pdf_path) as document:
            for page_number, (page, panel_source) in enumerate(
                zip(document, panel_sources), 1
            ):
                page_sizes = [
                    float(span["size"])
                    for block in page.get_text("dict").get("blocks", [])
                    for line in block.get("lines", [])
                    for span in line.get("spans", [])
                    if span.get("text", "").strip()
                ]
                font_sizes.extend(page_sizes)
                source_lines = panel_source.splitlines()
                page_metrics.append(
                    {
                        "page": page_number,
                        "line_count": len(source_lines),
                        "maximum_line_characters": max(
                            map(len, source_lines), default=0
                        ),
                        "font_size_points": round(
                            min(page_sizes) if page_sizes else 0.0, 2
                        ),
                        "page_size_points": [
                            round(page.rect.width, 2),
                            round(page.rect.height, 2),
                        ],
                    }
                )
        ascii_validation["page_metrics"] = page_metrics
        ascii_validation["minimum_font_size_points"] = round(
            min(font_sizes) if font_sizes else 0.0, 2
        )
        source_pdf_hash = sha256_file(ascii_pdf_source)
        output_pdf_hash = sha256_file(ascii_pdf_path)
        if output_pdf_hash != source_pdf_hash:
            raise ExportError(
                f"{selection.topic_key}: ASCII PDF byte equality failed."
            )
        artifact_records["ascii_master_pdf"] = {
            "source": repository_relative(ascii_pdf_source, root),
            "output": str(
                Path("04-ASCII-Master-Flowchart")
                / "ASCII-Master-Flowchart.pdf"
            ).replace("/", "\\"),
            "source_sha256": source_pdf_hash,
            "output_sha256": output_pdf_hash,
            "source_output_equal": True,
            "source_text_sha256": artifact_records["ascii_master_text"][
                "source_sha256"
            ],
            "normalized_text_equal": ascii_validation["normalized_equal"],
            "bytes": ascii_pdf_path.stat().st_size,
        }
    else:
        ascii_validation = render_ascii_pdf(ascii_text, ascii_pdf_path)
        artifact_records["ascii_master_pdf"] = {
            "source": artifact_records["ascii_master_text"]["source"],
            "output": str(
                Path("04-ASCII-Master-Flowchart")
                / "ASCII-Master-Flowchart.pdf"
            ).replace("/", "\\"),
            "source_text_sha256": artifact_records["ascii_master_text"][
                "source_sha256"
            ],
            "output_sha256": sha256_file(ascii_pdf_path),
            "normalized_text_equal": ascii_validation["normalized_equal"],
            "bytes": ascii_pdf_path.stat().st_size,
        }
    (stage / "README.txt").write_text(
        topic_readme(selection), encoding="utf-8", newline="\n"
    )

    pdf_metrics: dict[str, dict[str, Any]] = {}
    if full_pdf_validation:
        pdf_names = (
            "complete_learning_session",
            "solved_practice_workbook",
            "graphical_poster",
            "graphical_tiled",
        )
        for name in pdf_names:
            path = stage / Path(artifact_records[name]["output"])
            errors, metrics = pdf_layout_validation(path)
            if errors:
                raise ExportError(
                    f"{selection.topic_key}: {name} layout validation failed: "
                    + " | ".join(errors)
                )
            pdf_metrics[name] = metrics
    else:
        try:
            import fitz
        except ImportError as exc:
            raise ExportError(f"PyMuPDF is required: {exc}") from exc
        for name in (
            "complete_learning_session",
            "solved_practice_workbook",
            "graphical_poster",
            "graphical_tiled",
        ):
            path = stage / Path(artifact_records[name]["output"])
            with fitz.open(path) as document:
                pdf_metrics[name] = {"page_count": document.page_count}
    pdf_metrics["ascii_master_pdf"] = {
        "page_count": ascii_validation["pdf_page_count"],
        "blank_pages": ascii_validation["blank_pages"],
        "clipped_text_pages": ascii_validation["clipped_pages"],
        "replacement_glyph_pages": ascii_validation[
            "replacement_glyph_pages"
        ],
    }
    master_png = (
        stage
        / "03-Carvaka-Graphical-Flowchart"
        / "High-Resolution-Master.png"
    )
    image_metrics = png_validation(master_png)
    validate_topic_shape(stage)

    for name, _, _ in COPIED_ARTIFACTS:
        source = resolve_repository_path(
            root, str(artifact_records[name]["source"])
        )
        if sha256_file(source) != source_hashes_before[name]:
            raise ExportError(
                f"{selection.topic_key}: source artifact changed during copy: {name}"
            )

    return {
        "topic_key": selection.topic_key,
        "topic_title": selection.catalogue.title,
        "subject": selection.catalogue.subject,
        "section": selection.catalogue.section,
        "catalogue_number": selection.catalogue.number,
        "source_record_id": record["record_id"],
        "source_generation": int(record["generation"]),
        "destination_folder": str(selection.destination_relative).replace(
            "/", "\\"
        ),
        "approval": APPROVAL_STATE,
        "artifacts": artifact_records,
        "ascii": {
            "text_panel_count": ascii_validation["text_panel_count"],
            "pdf_panel_count": ascii_validation["pdf_panel_count"],
            "normalized_equal": ascii_validation["normalized_equal"],
            "minimum_font_size_points": ascii_validation[
                "minimum_font_size_points"
            ],
            "page_metrics": ascii_validation["page_metrics"],
        },
        "pdf_page_counts": {
            name: int(metrics["page_count"])
            for name, metrics in pdf_metrics.items()
        },
        "pdf_layout_validation": pdf_metrics,
        "graphical_master": image_metrics,
        "source_artifacts_unchanged": True,
        "status": "passed",
    }


def prepare_essay_topic_stage(
    root: Path,
    selection: ExportSelection,
    stage: Path,
    *,
    full_pdf_validation: bool,
) -> dict[str, Any]:
    record = selection.record
    stage.mkdir(parents=True, exist_ok=False)
    for directory, filenames in ESSAY_DELIVERABLES.items():
        deliverable = stage / directory
        deliverable.mkdir()
        if not filenames:
            raise ExportError(f"Deliverable definition is empty: {directory}")

    source_hashes_before: dict[str, str] = {}
    artifact_records: dict[str, dict[str, Any]] = {}
    for name, source_key, output_relative in ESSAY_COPIED_ARTIFACTS:
        source_value = str(nested_value(record, source_key))
        source = resolve_repository_path(root, source_value)
        destination = stage / Path(output_relative)
        source_hash = sha256_file(source)
        source_hashes_before[name] = source_hash
        shutil.copy2(source, destination)
        output_hash = sha256_file(destination)
        if output_hash != source_hash:
            raise ExportError(
                f"{selection.topic_key}: byte equality failed for {name}."
            )
        artifact_records[name] = {
            "source": repository_relative(source, root),
            "output": output_relative.replace("/", "\\"),
            "source_sha256": source_hash,
            "output_sha256": output_hash,
            "source_output_equal": True,
            "bytes": destination.stat().st_size,
        }

    (stage / "README.txt").write_text(
        topic_readme(selection), encoding="utf-8", newline="\n"
    )
    pdf_metrics: dict[str, dict[str, Any]] = {}
    for name in ("knowledge_guide", "practice_workbook", "practice_solutions"):
        path = stage / Path(artifact_records[name]["output"])
        if full_pdf_validation:
            errors, metrics = pdf_layout_validation(path)
            if errors:
                raise ExportError(
                    f"{selection.topic_key}: {name} layout validation failed: "
                    + " | ".join(errors)
                )
            pdf_metrics[name] = metrics
        else:
            try:
                import fitz
            except ImportError as exc:
                raise ExportError(f"PyMuPDF is required: {exc}") from exc
            with fitz.open(path) as document:
                pdf_metrics[name] = {"page_count": document.page_count}
    atlas = stage / Path(artifact_records["workflow_atlas"]["output"])
    image_metrics = png_validation(atlas)
    validate_topic_shape(stage, ESSAY_DELIVERABLES)
    for name, _, _ in ESSAY_COPIED_ARTIFACTS:
        source = resolve_repository_path(
            root, str(artifact_records[name]["source"])
        )
        if sha256_file(source) != source_hashes_before[name]:
            raise ExportError(
                f"{selection.topic_key}: source artifact changed during copy: {name}"
            )
    return {
        "topic_key": selection.topic_key,
        "topic_title": selection.catalogue.title,
        "subject": selection.catalogue.subject,
        "section": selection.catalogue.section,
        "catalogue_number": selection.catalogue.number,
        "source_record_id": record["record_id"],
        "source_generation": int(record["generation"]),
        "artifact_contract": ESSAY_CONTRACT,
        "destination_folder": str(selection.destination_relative).replace(
            "/", "\\"
        ),
        "approval": APPROVAL_STATE,
        "artifacts": artifact_records,
        "ascii": {
            "integrated": True,
            "source": record["integrated_ascii_flow"],
            "text_panel_count": int(
                record.get("integrated_ascii_panel_count") or 1
            ),
            "pdf_panel_count": 0,
            "normalized_equal": True,
        },
        "pdf_page_counts": {
            name: int(metrics["page_count"])
            for name, metrics in pdf_metrics.items()
        },
        "pdf_layout_validation": pdf_metrics,
        "graphical_master": image_metrics,
        "source_artifacts_unchanged": True,
        "status": "passed",
    }


def validate_topic_shape(
    topic_directory: Path,
    deliverables: dict[str, tuple[str, ...]] | None = None,
) -> None:
    expected_deliverables = deliverables or TOPIC_DELIVERABLES
    expected_root = {"README.txt", *expected_deliverables}
    actual_root = {item.name for item in topic_directory.iterdir()}
    if actual_root != expected_root:
        raise ExportError(
            f"Unexpected topic root contents in {topic_directory}: "
            f"expected {sorted(expected_root)}, found {sorted(actual_root)}"
        )
    directories = sorted(
        item.name for item in topic_directory.iterdir() if item.is_dir()
    )
    if directories != sorted(expected_deliverables):
        raise ExportError(
            f"{topic_directory}: expected exactly "
            f"{len(expected_deliverables)} deliverable directories."
        )
    for directory, filenames in expected_deliverables.items():
        actual = sorted(
            item.name for item in (topic_directory / directory).iterdir()
        )
        if actual != sorted(filenames):
            raise ExportError(
                f"{topic_directory / directory}: expected {sorted(filenames)}, "
                f"found {actual}."
            )


def existing_topic_matches_sources(
    root: Path,
    selection: ExportSelection,
    destination: Path,
) -> bool:
    if not destination.is_dir():
        return False
    deliverables = deliverables_for_record(selection.record)
    copied_artifacts = copied_artifacts_for_record(selection.record)
    try:
        validate_topic_shape(destination, deliverables)
    except ExportError:
        return False
    for _, source_key, output_relative in copied_artifacts:
        source_value = nested_value(selection.record, source_key)
        if not isinstance(source_value, str) or not source_value:
            return False
        source = resolve_repository_path(root, source_value)
        output = destination / Path(output_relative)
        if (
            not file_is_file(source)
            or not file_is_file(output)
            or sha256_file(source) != sha256_file(output)
        ):
            return False
    if essay_specific_record(selection.record):
        return True
    ascii_text = (
        destination
        / "04-ASCII-Master-Flowchart"
        / "ASCII-Master-Flowchart.txt"
    )
    ascii_pdf = (
        destination
        / "04-ASCII-Master-Flowchart"
        / "ASCII-Master-Flowchart.pdf"
    )
    tracked_ascii_pdf = nested_value(
        selection.record, "continuous_core_first.ascii_master_pdf"
    )
    if isinstance(tracked_ascii_pdf, str) and tracked_ascii_pdf:
        source_ascii_pdf = resolve_repository_path(root, tracked_ascii_pdf)
        return (
            file_is_file(ascii_text)
            and file_is_file(ascii_pdf)
            and file_is_file(source_ascii_pdf)
            and sha256_file(source_ascii_pdf) == sha256_file(ascii_pdf)
            and validate_ascii_pdf(
                read_text_file(ascii_text, encoding="utf-8"),
                ascii_pdf,
            )["passed"]
        )
    return (
        file_is_file(ascii_text)
        and file_is_file(ascii_pdf)
        and validate_ascii_pdf(
            read_text_file(ascii_text, encoding="utf-8"),
            ascii_pdf,
        )["passed"]
    )


def safe_remove_exact(path: Path, allowed_parent: Path, prefix: str) -> None:
    if not path.exists():
        return
    if path.resolve().parent != allowed_parent.resolve():
        raise ExportError(f"Refusing unsafe deletion outside {allowed_parent}: {path}")
    if not path.name.startswith(prefix):
        raise ExportError(f"Refusing unsafe deletion of {path}")
    removal_path: str | Path = path
    if os.name == "nt":
        resolved = str(path.resolve())
        if not resolved.startswith("\\\\?\\"):
            removal_path = "\\\\?\\" + resolved
    for attempt in range(6):
        try:
            shutil.rmtree(removal_path)
            return
        except PermissionError:
            if attempt == 5:
                raise
            time.sleep(0.25 * (attempt + 1))


def atomic_replace_topic(stage: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    backup = destination.parent / f".old-{uuid.uuid4().hex[:12]}"
    had_destination = destination.exists()
    try:
        if had_destination:
            replace_with_retry(destination, backup)
        replace_with_retry(stage, destination)
    except Exception:
        if destination.exists() and not had_destination:
            safe_remove_exact(destination, destination.parent, destination.name)
        if backup.exists() and not destination.exists():
            replace_with_retry(backup, destination)
        raise
    if backup.exists():
        safe_remove_exact(backup, destination.parent, ".old-")


def navigation_topic_record(
    selection: ExportSelection, topic_manifest: dict[str, Any]
) -> dict[str, Any]:
    base = selection.destination_relative
    if essay_specific_record(selection.record):
        return {
            "topic_key": selection.topic_key,
            "catalogue_number": selection.catalogue.number,
            "topic_title": selection.catalogue.title,
            "subject": selection.catalogue.subject,
            "section": selection.catalogue.section,
            "source_record_id": selection.record["record_id"],
            "source_generation": int(selection.record["generation"]),
            "approval": APPROVAL_STATE,
            "artifact_contract": ESSAY_CONTRACT,
            "destination_folder": str(base).replace("/", "\\"),
            "navigation_command": (
                f"Open final package: {selection.catalogue.subject} — "
                f"{selection.catalogue.section} — {selection.catalogue.title}"
            ),
            "links": {
                "readme": str(base / "README.txt").replace("/", "\\"),
                "knowledge_guide": str(
                    base / "01-Knowledge-Guide" / "Knowledge-Guide.pdf"
                ).replace("/", "\\"),
                "practice_workbook": str(
                    base / "02-Practice-Workbook" / "Practice-Workbook.pdf"
                ).replace("/", "\\"),
                "practice_solutions": str(
                    base / "03-Practice-Solutions" / "Practice-Solutions.pdf"
                ).replace("/", "\\"),
                "workflow_atlas": str(
                    base
                    / "04-Integrated-Workflow-Atlas"
                    / "Essay-Workflow-Atlas.png"
                ).replace("/", "\\"),
            },
            "status": topic_manifest["status"],
        }
    return {
        "topic_key": selection.topic_key,
        "catalogue_number": selection.catalogue.number,
        "topic_title": selection.catalogue.title,
        "subject": selection.catalogue.subject,
        "section": selection.catalogue.section,
        "source_record_id": selection.record["record_id"],
        "source_generation": int(selection.record["generation"]),
        "approval": APPROVAL_STATE,
        "destination_folder": str(base).replace("/", "\\"),
        "navigation_command": (
            f"Open final package: {selection.catalogue.subject} — "
            f"{selection.catalogue.section} — {selection.catalogue.title}"
        ),
        "links": {
            "readme": str(base / "README.txt").replace("/", "\\"),
            "complete_learning_session": str(
                base
                / "01-Complete-Learning-Session"
                / "Complete-Learning-Session.pdf"
            ).replace("/", "\\"),
            "solved_practice_workbook": str(
                base
                / "02-Solved-Practice-Workbook"
                / "Solved-Practice-Workbook.pdf"
            ).replace("/", "\\"),
            "graphical_flowchart": str(
                base
                / "03-Carvaka-Graphical-Flowchart"
                / "At-a-Glance-Poster.pdf"
            ).replace("/", "\\"),
            "ascii_master_flowchart": str(
                base
                / "04-ASCII-Master-Flowchart"
                / "ASCII-Master-Flowchart.pdf"
            ).replace("/", "\\"),
        },
        "status": topic_manifest["status"],
    }


def _relative_link(from_directory: Path, target: Path, label: str) -> str:
    relative = Path(os.path.relpath(target, from_directory))
    return markdown_link(relative, label)


def master_tracker_markdown(
    export_root: Path, topics: Sequence[dict[str, Any]]
) -> str:
    lines = [
        "# Master Tracker — Final Learning Packages",
        "",
        f"Topics: **{len(topics)}**  ",
        f"Approval state: **{APPROVAL_STATE}**",
        "",
        "| # | Topic | Subject | Section | Source | Session | Workbook | Graphical | ASCII | Approval |",
        "|---:|---|---|---|---|---|---|---|---|---|",
    ]
    for index, topic in enumerate(topics, 1):
        links = topic["links"]
        number = topic.get("catalogue_number")
        display_number = f"{number:02d}" if number is not None else str(index)
        source = (
            f"`{topic['source_record_id']}` / "
            f"generation {topic['source_generation']}"
        )
        if essay_navigation_links(topic):
            row_links = (
                _relative_link(
                    export_root,
                    export_root / Path(links["knowledge_guide"]),
                    "Guide",
                ),
                _relative_link(
                    export_root,
                    export_root / Path(links["practice_workbook"]),
                    "Workbook",
                ),
                _relative_link(
                    export_root,
                    export_root / Path(links["workflow_atlas"]),
                    "Atlas",
                ),
                _relative_link(
                    export_root,
                    export_root / Path(links["practice_solutions"]),
                    "Solutions",
                ),
            )
        else:
            row_links = (
                _relative_link(
                    export_root,
                    export_root / Path(links["complete_learning_session"]),
                    "PDF",
                ),
                _relative_link(
                    export_root,
                    export_root / Path(links["solved_practice_workbook"]),
                    "PDF",
                ),
                _relative_link(
                    export_root,
                    export_root / Path(links["graphical_flowchart"]),
                    "Poster",
                ),
                _relative_link(
                    export_root,
                    export_root / Path(links["ascii_master_flowchart"]),
                    "PDF",
                ),
            )
        lines.append(
            "| "
            + " | ".join(
                (
                    display_number,
                    _relative_link(
                        export_root,
                        export_root / Path(links["readme"]),
                        topic["topic_title"],
                    ),
                    topic["subject"],
                    topic["section"],
                    source,
                    *row_links,
                    APPROVAL_STATE,
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def catalogue_markdown(
    export_root: Path, selections: Sequence[ExportSelection]
) -> str:
    grouped: dict[str, dict[str, list[ExportSelection]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for selection in selections:
        grouped[selection.catalogue.subject][selection.catalogue.section].append(
            selection
        )
    lines = [
        "# Final Learning Package Catalogue",
        "",
        "Use the command beside a topic to navigate to its completed export. "
        "The command does not regenerate content.",
        "",
    ]
    for subject, sections in grouped.items():
        lines.extend((f"## {subject}", ""))
        for section, topics in sections.items():
            lines.extend((f"### {section}", ""))
            for selection in topics:
                readme = (
                    export_root
                    / selection.destination_relative
                    / "README.txt"
                )
                number = (
                    f"{selection.catalogue.number:02d}. "
                    if selection.catalogue.number is not None
                    else ""
                )
                lines.append(
                    f"- {_relative_link(export_root, readme, number + selection.catalogue.title)}"
                )
                lines.append(
                    "  - `Open final package: "
                    f"{selection.catalogue.subject} — "
                    f"{selection.catalogue.section} — "
                    f"{selection.catalogue.title}`"
                )
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def start_here_markdown(topic_count: int) -> str:
    return (
        "# Start Here\n\n"
        f"This library contains {topic_count} completed learning packages. "
        "Each topic has exactly four numbered deliverable folders: the complete "
        "learning session, solved workbook, graphical flowchart package, and "
        "ASCII master flowchart.\n\n"
        "- [Browse the catalogue](CATALOGUE.md)\n"
        "- [Open the master tracker](MASTER-TRACKER.md)\n"
        "- `MASTER-TRACKER.json` is the machine-readable equivalent.\n\n"
        f"All topic exports are marked **{APPROVAL_STATE}**. Source packages "
        "and tracker generations remain unchanged.\n"
    )


def write_subject_section_indexes(
    export_root: Path,
    selections: Sequence[ExportSelection],
    navigation: dict[str, dict[str, Any]],
) -> list[Path]:
    created: list[Path] = []
    grouped: dict[str, dict[str, list[ExportSelection]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for selection in selections:
        grouped[selection.catalogue.subject][selection.catalogue.section].append(
            selection
        )
    for subject, sections in grouped.items():
        subject_folder = sanitize_display_component(subject)
        subject_dir = export_root / subject_folder
        subject_lines = [f"# {subject}", "", "## Sections", ""]
        for section, topics in sections.items():
            section_folder = sanitize_display_component(section)
            section_dir = subject_dir / section_folder
            subject_lines.append(
                f"- {_relative_link(subject_dir, section_dir / 'INDEX.md', section)} "
                f"({len(topics)} topics)"
            )
        subject_lines.extend(("", "## Topics", ""))
        for section, topics in sections.items():
            subject_lines.extend((f"### {section}", ""))
            for selection in topics:
                readme = (
                    export_root / selection.destination_relative / "README.txt"
                )
                number = selection.catalogue.number
                label = (
                    f"{number:02d}. {selection.catalogue.title}"
                    if number is not None
                    else selection.catalogue.title
                )
                subject_lines.append(
                    f"- {_relative_link(subject_dir, readme, label)}"
                )
            subject_lines.append("")
        subject_index = subject_dir / "INDEX.md"
        write_text_atomic(
            subject_index, "\n".join(subject_lines).rstrip() + "\n"
        )
        created.append(subject_index)

        for section, topics in sections.items():
            section_dir = (
                subject_dir / sanitize_display_component(section)
            )
            section_lines = [
                f"# {subject} — {section}",
                "",
                f"Topics: **{len(topics)}**  ",
                f"Approval: **{APPROVAL_STATE}**",
                "",
                "| # | Topic | Session | Workbook | Graphical | ASCII |",
                "|---:|---|---|---|---|---|",
            ]
            for selection in topics:
                topic = navigation[selection.topic_key]
                links = topic["links"]
                number = selection.catalogue.number
                display_number = (
                    f"{number:02d}" if number is not None else "—"
                )
                if essay_navigation_links(topic):
                    row_links = (
                        _relative_link(
                            section_dir,
                            export_root / Path(links["knowledge_guide"]),
                            "Guide",
                        ),
                        _relative_link(
                            section_dir,
                            export_root / Path(links["practice_workbook"]),
                            "Workbook",
                        ),
                        _relative_link(
                            section_dir,
                            export_root / Path(links["workflow_atlas"]),
                            "Atlas",
                        ),
                        _relative_link(
                            section_dir,
                            export_root / Path(links["practice_solutions"]),
                            "Solutions",
                        ),
                    )
                else:
                    row_links = (
                        _relative_link(
                            section_dir,
                            export_root
                            / Path(links["complete_learning_session"]),
                            "PDF",
                        ),
                        _relative_link(
                            section_dir,
                            export_root
                            / Path(links["solved_practice_workbook"]),
                            "PDF",
                        ),
                        _relative_link(
                            section_dir,
                            export_root / Path(links["graphical_flowchart"]),
                            "Poster",
                        ),
                        _relative_link(
                            section_dir,
                            export_root / Path(links["ascii_master_flowchart"]),
                            "PDF",
                        ),
                    )
                section_lines.append(
                    "| "
                    + " | ".join(
                        (
                            display_number,
                            _relative_link(
                                section_dir,
                                export_root / Path(links["readme"]),
                                selection.catalogue.title,
                            ),
                            *row_links,
                        )
                    )
                    + " |"
                )
            section_index = section_dir / "INDEX.md"
            write_text_atomic(
                section_index, "\n".join(section_lines) + "\n"
            )
            created.append(section_index)
    return created


def validate_markdown_links(
    export_root: Path,
    roots: Sequence[Path] | None = None,
) -> dict[str, Any]:
    checked = 0
    broken: list[str] = []
    markdown_files = sorted(
        {
            markdown
            for root in (roots or (export_root,))
            for markdown in root.rglob("*.md")
            if "_deep-content-review" not in markdown.parts
        }
    )
    for markdown in markdown_files:
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip("<>")
            if (
                not target
                or target.startswith("#")
                or "://" in target
                or target.startswith("mailto:")
            ):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (markdown.parent / Path(target)).resolve()
            checked += 1
            resolved_io = filesystem_io_path(resolved)
            if not (resolved_io.is_file() or resolved_io.is_dir()):
                broken.append(
                    f"{repository_relative(markdown)} -> {target}"
                )
    return {
        "checked_link_count": checked,
        "markdown_file_count": len(markdown_files),
        "broken_links": broken,
        "passed": not broken,
    }


def count_library_files(export_root: Path) -> dict[str, Any]:
    files = list(iter_files(export_root))
    extensions = Counter(
        path.suffix.lower() or "<none>" for path in files
    )
    return {
        "file_count": len(files),
        "pdf_count": extensions[".pdf"],
        "png_count": extensions[".png"],
        "txt_count": extensions[".txt"],
        "markdown_count": extensions[".md"],
        "json_count": extensions[".json"],
        "total_bytes": sum(file_size(path) for path in files),
        "by_extension": dict(sorted(extensions.items())),
    }


def validate_library(
    export_root: Path,
    selections: Sequence[ExportSelection],
    topic_manifests: Sequence[dict[str, Any]],
    tracker_hash_before: str,
    tracker_hash_after: str,
    *,
    require_all: bool,
) -> dict[str, Any]:
    errors: list[str] = []
    topic_directories: list[Path] = []
    destinations: list[str] = []
    manifest_by_key = {
        item["topic_key"]: item for item in topic_manifests
    }
    for selection in selections:
        destination = export_root / selection.destination_relative
        topic_directories.append(destination)
        destinations.append(str(selection.destination_relative).casefold())
        try:
            validate_topic_shape(
                destination,
                deliverables_for_record(selection.record),
            )
        except ExportError as exc:
            errors.append(str(exc))
        topic_manifest = manifest_by_key.get(selection.topic_key)
        if topic_manifest is None:
            errors.append(f"Missing topic manifest: {selection.topic_key}")
            continue
        for artifact_name, artifact in topic_manifest["artifacts"].items():
            if artifact_name == "ascii_master_pdf":
                continue
            output = resolve_repository_path(
                REPOSITORY_ROOT, artifact["output"]
            )
            source = resolve_repository_path(
                REPOSITORY_ROOT, artifact["source"]
            )
            if not file_is_file(output) or not file_is_file(source):
                errors.append(
                    f"{selection.topic_key}: missing {artifact_name} during validation."
                )
                continue
            source_hash = sha256_file(source)
            output_hash = sha256_file(output)
            if source_hash != output_hash:
                errors.append(
                    f"{selection.topic_key}: source/output hash mismatch for "
                    f"{artifact_name}."
                )
        if essay_specific_record(selection.record):
            continue
        ascii_pdf = (
            destination
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.pdf"
        )
        ascii_text = (
            destination
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.txt"
        )
        ascii_check = validate_ascii_pdf(
            read_text_file(ascii_text, encoding="utf-8"), ascii_pdf
        )
        if not ascii_check["passed"]:
            errors.extend(
                f"{selection.topic_key}: {error}"
                for error in ascii_check["errors"]
            )
    if len(set(destinations)) != len(destinations):
        errors.append("Duplicate topic destinations detected.")
    forbidden = [
        repository_relative(path)
        for path in topic_directories
        if FORBIDDEN_PATH_RE.search(
            str(path.relative_to(export_root))
        )
    ]
    if forbidden:
        errors.append(
            "Internal generation jargon appears in user paths: "
            + ", ".join(forbidden)
        )
    expected_topic_count = len(selections)
    if require_all and len(topic_directories) != expected_topic_count:
        errors.append(
            f"Expected {expected_topic_count} topic folders, "
            f"found {len(topic_directories)}."
        )
    if require_all:
        discovered = 0
        for readme in export_root.glob("*/*/*/README.txt"):
            if readme.parent.is_dir():
                discovered += 1
        if discovered != expected_topic_count:
            errors.append(
                f"Filesystem contains {discovered} topic folders; "
                f"expected {expected_topic_count}."
            )
    links = validate_markdown_links(
        export_root,
        None if require_all else topic_directories,
    )
    if not links["passed"]:
        errors.extend(
            f"Broken Markdown link: {link}"
            for link in links["broken_links"]
        )
    tracker_unchanged = tracker_hash_before == tracker_hash_after
    if not tracker_unchanged:
        errors.append("EXPORT-PDF-STATUS.json changed during export.")
    source_unchanged = all(
        item.get("source_artifacts_unchanged") is True
        for item in topic_manifests
    )
    if not source_unchanged:
        errors.append("One or more source artifacts changed during export.")
    copied_pdf_layouts_passed = all(
        not metrics.get("blank_pages")
        and not metrics.get("near_empty_pages")
        and not metrics.get("clipped_text_pages")
        and not metrics.get("replacement_glyph_pages")
        for item in topic_manifests
        for name, metrics in item["pdf_layout_validation"].items()
        if name != "ascii_master_pdf"
    )
    if not copied_pdf_layouts_passed:
        errors.append(
            "One or more copied PDFs has a blank, near-empty, clipped, "
            "or replacement-glyph page."
        )
    ascii_standalone = all(
        item.get("artifact_contract") == ESSAY_CONTRACT
        or (
            item["ascii"]["pdf_panel_count"]
            == item["ascii"]["text_panel_count"]
            and item["artifacts"]["ascii_master_pdf"]["output_sha256"]
            != item["artifacts"]["complete_learning_session"]["output_sha256"]
        )
        for item in topic_manifests
    )
    if not ascii_standalone:
        errors.append("One or more ASCII PDFs is not a standalone panel PDF.")
    return {
        "schema_version": 1,
        "created_at": utc_timestamp(),
        "status": "passed" if not errors else "failed",
        "errors": errors,
        "checks": {
            "exact_topic_count": (
                len(topic_directories) == expected_topic_count
                if require_all
                else True
            ),
            "exact_four_deliverable_directories": not any(
                "deliverable directories" in error for error in errors
            ),
            "required_filenames_present": not any(
                "expected" in error and "found" in error
                for error in errors
            ),
            "copied_artifact_hashes_equal": not any(
                "hash mismatch" in error for error in errors
            ),
            "source_artifacts_unchanged": source_unchanged,
            "tracker_unchanged": tracker_unchanged,
            "no_internal_jargon_in_paths": not forbidden,
            "no_duplicate_topic_destination": (
                len(set(destinations)) == len(destinations)
            ),
            "all_markdown_links_resolve": links["passed"],
            "ascii_panels_complete_and_equal": not any(
                "ASCII PDF" in error for error in errors
            ),
            "ascii_pdf_is_standalone": ascii_standalone,
            "copied_pdfs_open_no_blank_clipping_or_replacement": (
                copied_pdf_layouts_passed
            ),
            "approval_pending": all(
                selection.record.get("approved") is False
                for selection in selections
            ),
            "latest_tracker_graphical_and_ascii_selected": all(
                essay_specific_record(selection.record)
                or (
                    (
                        selection.record.get("continuous_core_first") or {}
                    ).get("renderer", {}).get("name")
                    == GRAPHICAL_RENDERER
                    and manual_ascii_source(
                        (
                            selection.record.get("continuous_core_first") or {}
                        ).get("ascii_master_source")
                    )
                )
                for selection in selections
            ),
        },
        "tracker": {
            "path": repository_relative(DEFAULT_TRACKER),
            "sha256_before": tracker_hash_before,
            "sha256_after": tracker_hash_after,
            "unchanged": tracker_unchanged,
        },
        "topic_count": len(topic_directories),
        "links": links,
        "library_totals": count_library_files(export_root),
        "topics": [
            {
                "topic_key": item["topic_key"],
                "destination_folder": item["destination_folder"],
                "status": item["status"],
                "pdf_page_counts": item["pdf_page_counts"],
                "ascii": item["ascii"],
                "pdf_layout_validation": item["pdf_layout_validation"],
            }
            for item in topic_manifests
        ],
    }


def existing_navigation_records(export_root: Path) -> dict[str, dict[str, Any]]:
    tracker_path = export_root / "MASTER-TRACKER.json"
    if not tracker_path.is_file():
        return {}
    data = load_json(tracker_path)
    topics = data.get("topics") or []
    return {
        str(topic["topic_key"]): topic
        for topic in topics
        if isinstance(topic, dict) and topic.get("topic_key")
    }


def prune_stale_topic_destinations(
    export_root: Path,
    selections: Sequence[ExportSelection],
) -> list[Path]:
    expected = {
        selection.destination_relative.as_posix().casefold()
        for selection in selections
    }
    stale: list[Path] = []
    for readme in export_root.glob("*/*/*/README.txt"):
        topic_dir = readme.parent
        relative_path = topic_dir.relative_to(export_root)
        if any(part.startswith("_") for part in relative_path.parts):
            continue
        relative = relative_path.as_posix().casefold()
        if relative not in expected:
            stale.append(topic_dir)
    for topic_dir in stale:
        safe_remove_exact(topic_dir, topic_dir.parent, topic_dir.name)
    return stale


def inventory_payload(
    selections: Sequence[ExportSelection], export_root: Path
) -> dict[str, Any]:
    return {
        "mode": "inventory",
        "topic_count": len(selections),
        "export_root": repository_relative(export_root),
        "subjects": dict(
            sorted(Counter(s.catalogue.subject for s in selections).items())
        ),
        "sections": dict(
            sorted(
                Counter(
                    f"{s.catalogue.subject} — {s.catalogue.section}"
                    for s in selections
                ).items()
            )
        ),
        "topics": [
            {
                "topic_key": selection.topic_key,
                "record_id": selection.record["record_id"],
                "generation": selection.record["generation"],
                "subject": selection.catalogue.subject,
                "section": selection.catalogue.section,
                "title": selection.catalogue.title,
                "destination": str(
                    selection.destination_relative
                ).replace("/", "\\"),
            }
            for selection in selections
        ],
    }


def retained_navigation_selection(
    topic: dict[str, Any],
    catalogue: dict[str, list[CatalogueTopic]],
) -> ExportSelection:
    """Resolve ordering metadata without reselecting an unrequested tracker record."""
    topic_key = str(topic["topic_key"])
    matches = catalogue.get(topic_key, [])
    unique = {
        (
            item.topic_key,
            item.title,
            item.subject,
            item.section,
            item.number,
        ): item
        for item in matches
    }
    if len(unique) != 1:
        raise ExportError(
            f"{topic_key}: expected one catalogue match for retained navigation, "
            f"found {len(unique)}."
        )
    item = next(iter(unique.values()))
    destination = Path(str(topic["destination_folder"]).replace("\\", "/"))
    if len(destination.parts) != 3:
        raise ExportError(
            f"{topic_key}: retained destination has unexpected shape: {destination}"
        )
    return ExportSelection(
        record={
            "topic_key": topic_key,
            "record_id": topic["source_record_id"],
            "generation": int(topic["source_generation"]),
        },
        catalogue=item,
        subject_folder=destination.parts[0],
        section_folder=destination.parts[1],
        topic_folder=destination.parts[2],
    )


def export_library(
    *,
    root: Path,
    export_root: Path,
    tracker_path: Path,
    catalogue_path: Path,
    selected_keys: Sequence[str] | None,
    manifest_date: str,
    dry_run: bool,
    full_pdf_validation: bool,
) -> dict[str, Any]:
    selections = resolve_selections(
        root,
        tracker_path,
        catalogue_path,
        selected_keys,
        export_root=export_root,
    )
    if dry_run:
        return inventory_payload(selections, export_root)

    require_all = not selected_keys
    tracker_hash_before = sha256_file(tracker_path)
    catalogue_hash_before = sha256_file(catalogue_path)
    staging_root = export_root.parent / f".{export_root.name}.staging"
    staging_root.mkdir(parents=True, exist_ok=True)
    topic_manifests: list[dict[str, Any]] = []
    previous_navigation = existing_navigation_records(export_root)
    exported_navigation: dict[str, dict[str, Any]] = {}

    try:
        for selection in selections:
            stage = staging_root / (
                f"{selection.topic_key}-{uuid.uuid4().hex}"
            )
            try:
                topic_manifest = prepare_topic_stage(
                    root,
                    selection,
                    stage,
                    full_pdf_validation=full_pdf_validation,
                )
                destination = export_root / selection.destination_relative
                if existing_topic_matches_sources(
                    root, selection, destination
                ):
                    safe_remove_exact(
                        stage, staging_root, f"{selection.topic_key}-"
                    )
                else:
                    atomic_replace_topic(stage, destination)
            except Exception:
                if stage.exists():
                    safe_remove_exact(
                        stage, staging_root, f"{selection.topic_key}-"
                    )
                raise
            topic_manifest["destination_folder"] = repository_relative(
                destination, root
            )
            for artifact in topic_manifest["artifacts"].values():
                artifact["output"] = repository_relative(
                    destination / Path(artifact["output"]), root
                )
            topic_manifests.append(topic_manifest)
            exported_navigation[selection.topic_key] = navigation_topic_record(
                selection, topic_manifest
            )
    finally:
        if staging_root.exists() and not any(staging_root.iterdir()):
            staging_root.rmdir()

    if selected_keys:
        navigation = dict(previous_navigation)
        navigation.update(exported_navigation)
        navigation_topics = list(navigation.values())
        # A selected refresh is allowed only when every retained navigation
        # target still exists; otherwise publish a navigation view of the
        # topics actually present.
        navigation_topics = [
            topic
            for topic in navigation_topics
            if (
                export_root
                / Path(topic["destination_folder"].replace("\\", "/"))
            ).is_dir()
        ]
        selection_by_key = {item.topic_key: item for item in selections}
        if len(navigation_topics) != len(selections):
            catalogue = load_catalogue_topics(catalogue_path)
            selection_by_key.update(
                {
                    str(topic["topic_key"]): retained_navigation_selection(
                        topic, catalogue
                    )
                    for topic in navigation_topics
                    if str(topic["topic_key"]) not in selection_by_key
                }
            )
        navigation_selections = [
            selection_by_key[topic["topic_key"]]
            for topic in navigation_topics
        ]
        navigation_topics = sorted(
            navigation_topics,
            key=lambda topic: (
                selection_by_key[topic["topic_key"]].catalogue.subject_order,
                selection_by_key[topic["topic_key"]].catalogue.section_order,
                selection_by_key[topic["topic_key"]].catalogue.topic_order,
            ),
        )
        navigation_selections = [
            selection_by_key[topic["topic_key"]]
            for topic in navigation_topics
        ]
    else:
        navigation_topics = [
            exported_navigation[selection.topic_key]
            for selection in selections
        ]
        navigation_selections = list(selections)

    export_root.mkdir(parents=True, exist_ok=True)
    master_json = {
        "schema_version": 1,
        "created_at": utc_timestamp(),
        "root": repository_relative(export_root, root),
        "topic_count": len(navigation_topics),
        "approval": APPROVAL_STATE,
        "subjects": dict(
            sorted(
                Counter(
                    topic["subject"] for topic in navigation_topics
                ).items()
            )
        ),
        "sections": dict(
            sorted(
                Counter(
                    f"{topic['subject']} — {topic['section']}"
                    for topic in navigation_topics
                ).items()
            )
        ),
        "topics": navigation_topics,
    }
    write_text_atomic(
        export_root / "START-HERE.md",
        start_here_markdown(len(navigation_topics)),
    )
    write_text_atomic(
        export_root / "CATALOGUE.md",
        catalogue_markdown(export_root, navigation_selections),
    )
    write_text_atomic(
        export_root / "MASTER-TRACKER.md",
        master_tracker_markdown(export_root, navigation_topics),
    )
    write_json_atomic(export_root / "MASTER-TRACKER.json", master_json)
    write_subject_section_indexes(
        export_root,
        navigation_selections,
        {topic["topic_key"]: topic for topic in navigation_topics},
    )
    if require_all:
        prune_stale_topic_destinations(export_root, navigation_selections)

    tracker_hash_after = sha256_file(tracker_path)
    catalogue_hash_after = sha256_file(catalogue_path)
    if catalogue_hash_before != catalogue_hash_after:
        raise ExportError("Topic catalogue changed during export.")
    validation = validate_library(
        export_root,
        selections,
        topic_manifests,
        tracker_hash_before,
        tracker_hash_after,
        require_all=require_all,
    )
    if validation["status"] != "passed":
        raise ExportError(
            "Final library validation failed: "
            + " | ".join(validation["errors"])
        )

    manifest_dir = root / "upsc-ai-kit" / "manifests" / "exports"
    if require_all:
        manifest_stem = f"final-four-item-library-{manifest_date}"
    else:
        selection_digest = hashlib.sha256(
            "\0".join(selection.topic_key for selection in selections).encode("utf-8")
        ).hexdigest()[:12]
        manifest_stem = (
            f"final-four-item-library-{manifest_date}-selected-"
            f"{len(selections)}-{selection_digest}"
        )
    manifest_path = manifest_dir / f"{manifest_stem}.json"
    validation_path = manifest_dir / f"{manifest_stem}-validation.json"
    manifest = {
        "schema_version": 1,
        "created_at": utc_timestamp(),
        "purpose": "Persistent four-deliverable navigation/export library",
        "scope": "all" if require_all else "selected",
        "export_root": repository_relative(export_root, root),
        "tracker": {
            "path": repository_relative(tracker_path, root),
            "sha256_before": tracker_hash_before,
            "sha256_after": tracker_hash_after,
            "unchanged": tracker_hash_before == tracker_hash_after,
        },
        "catalogue": {
            "path": repository_relative(catalogue_path, root),
            "sha256_before": catalogue_hash_before,
            "sha256_after": catalogue_hash_after,
            "unchanged": catalogue_hash_before == catalogue_hash_after,
        },
        "topic_count": len(topic_manifests),
        "subjects": dict(
            sorted(
                Counter(item["subject"] for item in topic_manifests).items()
            )
        ),
        "sections": dict(
            sorted(
                Counter(
                    f"{item['subject']} — {item['section']}"
                    for item in topic_manifests
                ).items()
            )
        ),
        "library_totals": count_library_files(export_root),
        "topics": topic_manifests,
        "status": "passed",
    }
    write_json_atomic(manifest_path, manifest)
    validation["manifest"] = repository_relative(manifest_path, root)
    validation["validation_manifest"] = repository_relative(
        validation_path, root
    )
    write_json_atomic(validation_path, validation)
    return {
        "mode": "export",
        "status": "passed",
        "topic_count": len(topic_manifests),
        "export_root": repository_relative(export_root, root),
        "manifest": repository_relative(manifest_path, root),
        "validation_manifest": repository_relative(validation_path, root),
        "subjects": manifest["subjects"],
        "sections": manifest["sections"],
        "library_totals": manifest["library_totals"],
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=REPOSITORY_ROOT,
        help="Repository root.",
    )
    parser.add_argument(
        "--export-root",
        type=Path,
        default=DEFAULT_EXPORT_ROOT,
        help="Destination library root.",
    )
    parser.add_argument(
        "--tracker",
        type=Path,
        default=DEFAULT_TRACKER,
        help="Read-only export tracker.",
    )
    parser.add_argument(
        "--catalogue",
        type=Path,
        default=DEFAULT_CATALOGUE,
        help="Read-only learner topic catalogue.",
    )
    parser.add_argument(
        "--topic-key",
        action="append",
        default=[],
        help="Export one topic key; repeat for multiple topics.",
    )
    parser.add_argument(
        "--topics",
        default="",
        help="Comma-separated topic keys.",
    )
    parser.add_argument(
        "--dry-run",
        "--inventory",
        action="store_true",
        dest="dry_run",
        help="Resolve and print inventory without writing files.",
    )
    parser.add_argument(
        "--manifest-date",
        default=datetime.now().date().isoformat(),
        help="Date suffix for technical manifests.",
    )
    parser.add_argument(
        "--quick-pdf-check",
        action="store_true",
        help="Only open/count copied PDFs; skip the existing full layout validator.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    topic_keys = list(args.topic_key)
    if args.topics:
        topic_keys.extend(
            item.strip() for item in args.topics.split(",") if item.strip()
        )
    try:
        result = export_library(
            root=args.root.resolve(),
            export_root=args.export_root.resolve(),
            tracker_path=args.tracker.resolve(),
            catalogue_path=args.catalogue.resolve(),
            selected_keys=topic_keys or None,
            manifest_date=args.manifest_date,
            dry_run=args.dry_run,
            full_pdf_validation=not args.quick_pdf_check,
        )
    except ExportError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        print(f"ERROR: unexpected export failure: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
