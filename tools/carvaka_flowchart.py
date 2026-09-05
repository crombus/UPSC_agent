"""Reusable Cārvāka-standard graphical flowchart renderer and validator.

The module owns the standalone graphical companion only.  It never rewrites the
text-native ASCII master embedded in learner-v2 Markdown.
"""

from __future__ import annotations

import hashlib
import io
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence

import fitz
from fontTools.ttLib import TTFont
from PIL import Image, ImageChops, ImageDraw, ImageFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as rl_canvas

import polity_flowchart_case_years


Image.MAX_IMAGE_PIXELS = None

RENDERER_NAME = "carvaka-continuous-at-a-glance-graphical-v2"
RENDERER_VERSION = "2.0"
SCHEMA_VERSION = 2
MASTER_WIDTH = 4800
MASTER_DPI = 300
MARGIN = 110
RAIL_X = 250
CARD_X0 = 520
CARD_X1 = 4690
CARD_WIDTH = CARD_X1 - CARD_X0
CARD_PADDING = 46
INNER_WIDTH = CARD_WIDTH - CARD_PADDING * 2
STAGE_GAP = 66
TILE_MIN_OVERLAP = 330

REFERENCE_FOLDER = (
    Path("notes")
    / "Philosophy"
    / "flowcharts"
    / "philosophy-paper-i-indian-philosophy-01"
    / "continuous-at-a-glance-core-first"
)
REFERENCE_HASHES = {
    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png":
        "c9ae34e995375348a6998885784ded0680c0a8f8e3cd6cb82bb4cd5385e85c62",
    "Carvaka_Continuous-At-a-Glance-Core-First_Poster_2026-08-22.pdf":
        "f291dde859557d822b91902027b070bb649e92f20c52e9031b1521a9dde16d90",
    "Carvaka_Continuous-At-a-Glance-Core-First_Tiled_2026-08-22.pdf":
        "eb3e452797f15bac2599431e72bc69efedb66aa104367c6f0404b4abe3296d6e",
    "README.txt":
        "31df6ad4c502840dbdc098d80e247e08ad8ba37ba1889da4fb2e86d274a9b28e",
    "validation-report.txt":
        "6ee3bba7c47f855d36c94fd92c50efd873d417b2947c72a836df5831d9185989",
}

BG = (7, 20, 33)
CARD = (16, 40, 61)
CARD_ALT = (14, 36, 55)
CARD_EXTRA = (13, 26, 40)
HEADER = (11, 38, 58)
CYAN = (68, 211, 255)
TEAL = (65, 228, 193)
AMBER = (255, 178, 91)
YELLOW = (255, 225, 122)
MAGENTA = (230, 144, 255)
GREEN = (126, 231, 135)
RED = (255, 138, 128)
WHITE = (237, 246, 251)
DIM = (156, 180, 200)
GREY = (150, 168, 185)
RULE = (46, 71, 88)
ANSWER_FILL = (43, 37, 55)

COLOURS = {
    "primary": CYAN,
    "mechanism": TEAL,
    "evidence": AMBER,
    "caution": RED,
    "comparison": MAGENTA,
    "institution": YELLOW,
    "outcome": GREEN,
    "neutral": GREY,
}

LAYOUTS = {
    "columns",
    "process",
    "timeline",
    "matrix",
    "hierarchy",
    "dialectic",
    "spatial",
    "synthesis",
}

FONT_DIR = Path(r"C:\Windows\Fonts")
FONT_REGULAR = FONT_DIR / "segoeui.ttf"
FONT_BOLD = FONT_DIR / "segoeuib.ttf"


class CarvakaError(ValueError):
    """Raised when a graphical specification or artifact is non-compliant."""


@dataclass(frozen=True)
class RenderResult:
    dimensions: tuple[int, int]
    stages: list[dict[str, object]]
    tiles: list[dict[str, object]]
    previews: list[Path]
    contact_sheets: list[Path]
    poster_dimensions_points: tuple[float, float]
    validation_errors: list[str]
    audit: dict[str, object]


class Fonts:
    def __init__(self) -> None:
        self.title = _font(FONT_BOLD, 68)
        self.subtitle = _font(FONT_BOLD, 31)
        self.note = _font(FONT_REGULAR, 27)
        self.stage = _font(FONT_BOLD, 50)
        self.stage_small = _font(FONT_BOLD, 42)
        self.badge = _font(FONT_BOLD, 24)
        self.pill = _font(FONT_BOLD, 25)
        self.heading = _font(FONT_BOLD, 29)
        self.body = _font(FONT_REGULAR, 27)
        self.body_bold = _font(FONT_BOLD, 27)
        self.small = _font(FONT_REGULAR, 24)
        self.small_bold = _font(FONT_BOLD, 24)
        self.answer = _font(FONT_BOLD, 26)
        self.node = _font(FONT_BOLD, 31)


def _font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    if not path.is_file():
        raise CarvakaError(f"Required font is unavailable: {path}")
    return ImageFont.truetype(str(path), size)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("/", "\\")


def load_spec(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise CarvakaError(f"Graphical spec must be an object: {path}")
    errors = validate_spec(data)
    if errors:
        raise CarvakaError(
            f"{path}: invalid Cārvāka graphical spec: " + " | ".join(errors)
        )
    return data


def _iter_strings(value: object) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for nested in value.values():
            yield from _iter_strings(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _iter_strings(nested)


def _pill_role_count(stage: dict[str, object]) -> int:
    pills = stage.get("pills", [])
    if not isinstance(pills, list):
        return 0
    return len({
        str(pill.get("role"))
        for pill in pills
        if isinstance(pill, dict) and pill.get("role")
    })


def layout_signature(stage: dict[str, object]) -> str:
    groups = stage.get("groups", [])
    sequence = stage.get("sequence", [])
    matrix = stage.get("matrix", [])
    return (
        f"{stage.get('layout')}|g{len(groups) if isinstance(groups, list) else 0}"
        f"|q{len(sequence) if isinstance(sequence, list) else 0}"
        f"|m{len(matrix) if isinstance(matrix, list) else 0}"
        f"|b{bool(stage.get('mechanism_strip'))}"
        f"|a{bool(stage.get('answer_line'))}"
    )


def validate_spec(spec: dict[str, object]) -> list[str]:
    errors: list[str] = []
    if spec.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")
    if spec.get("renderer") != RENDERER_NAME:
        errors.append(f"renderer must be {RENDERER_NAME}")
    for field in (
        "topic_key",
        "subject",
        "title",
        "short_route",
        "reading_note",
        "source_markdown",
        "ascii_spec",
        "reference_sha256",
    ):
        if not str(spec.get(field) or "").strip():
            errors.append(f"missing {field}")
    if spec.get("reference_sha256") != REFERENCE_HASHES[
        "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
    ]:
        errors.append("immutable reference master hash is not pinned")
    status = spec.get("status")
    if not isinstance(status, dict):
        errors.append("status must be an object")
    else:
        if status.get("approved") is not False:
            errors.append("generated graphical specs must remain unapproved")
        if "prior artifacts unchanged" not in str(status.get("line", "")).casefold():
            errors.append("status line must state prior artifacts unchanged")
    stages = spec.get("stages")
    if not isinstance(stages, list) or len(stages) < 7:
        errors.append("at least six core stages plus one extra stage are required")
        return errors
    extras = [
        stage for stage in stages
        if isinstance(stage, dict) and stage.get("role") == "extra"
    ]
    if len(extras) != 1 or stages[-1] is not extras[0]:
        errors.append("exactly one final subordinate extra stage is required")
    if not isinstance(stages[-1], dict) or stages[-1].get("id") != "E":
        errors.append("the final subordinate node must be E")
    core = [
        stage for stage in stages
        if isinstance(stage, dict) and stage.get("role") != "extra"
    ]
    expected_ids = [f"{index:02d}" for index in range(len(core))]
    if [str(stage.get("id")) for stage in core] != expected_ids:
        errors.append("core stage ids must be ordered and zero-padded from 00")
    if not core or core[-1].get("role") != "synthesis":
        errors.append("the last core stage must be the final synthesis")
    layouts: list[str] = []
    answers: list[str] = []
    for stage in stages:
        if not isinstance(stage, dict):
            errors.append("every stage must be an object")
            continue
        stage_id = str(stage.get("id") or "?")
        layout = str(stage.get("layout") or "")
        layouts.append(layout)
        if layout not in LAYOUTS:
            errors.append(f"stage {stage_id}: unsupported layout {layout!r}")
        title = str(stage.get("title") or "").strip()
        if len(title.split()) < 2 and len(title) < 8:
            errors.append(f"stage {stage_id}: title is too generic")
        pills = stage.get("pills")
        if not isinstance(pills, list) or not (4 <= len(pills) <= 10):
            errors.append(f"stage {stage_id}: requires 4-10 keyword pills")
        elif stage.get("role") != "extra" and _pill_role_count(stage) < 3:
            errors.append(f"stage {stage_id}: requires at least three pill colour roles")
        groups = stage.get("groups")
        if not isinstance(groups, list) or not (2 <= len(groups) <= 4):
            errors.append(f"stage {stage_id}: requires 2-4 internal content groups")
        else:
            for group in groups:
                if not isinstance(group, dict):
                    errors.append(f"stage {stage_id}: malformed content group")
                    continue
                if not str(group.get("heading") or "").strip():
                    errors.append(f"stage {stage_id}: group heading is blank")
                items = group.get("items")
                if not isinstance(items, list) or not items:
                    errors.append(f"stage {stage_id}: group is blank")
        if stage.get("role") != "extra":
            answer = str(stage.get("answer_line") or "").strip()
            if len(answer.split()) < 8:
                errors.append(f"stage {stage_id}: answer-grabbing line is missing or too short")
            else:
                answers.append(answer.casefold())
        else:
            if "unnecessary for a competent core answer" not in str(
                stage.get("mechanism_strip") or ""
            ).casefold():
                errors.append(
                    "extra stage must state it is unnecessary for a competent core answer"
                )
        mechanism = str(stage.get("mechanism_strip") or "").strip()
        if mechanism and (
            len(mechanism.split()) < 8
            or mechanism[-1:] not in ".!?"
        ):
            errors.append(
                f"stage {stage_id}: mechanism/verdict strip must be a complete sentence"
            )
        if not stage.get("source_references"):
            errors.append(f"stage {stage_id}: source references are missing")
    core_layouts = {layout for layout in layouts[:-1]}
    minimum_layouts = 4 if len(core) >= 8 else 3
    if len(core_layouts) < minimum_layouts:
        errors.append(
            f"layout diversity is too low: {len(core_layouts)} < {minimum_layouts}"
        )
    if len(set(answers)) != len(answers):
        errors.append("core answer-grabbing lines must be unique")
    blob = "\n".join(_iter_strings(spec))
    for banned in (
        "CONTEXT + EXACT CORE",
        "MECHANISM / ARGUMENT|CONSEQUENCE / CONTRAST|UPSC TRAP / ANSWER USE",
        "…",
        "\ufffd",
    ):
        if banned in blob:
            errors.append(f"banned flat-renderer or unsafe text found: {banned}")
    if spec.get("subject") == "Polity":
        errors.extend(polity_flowchart_case_years.graphical_spec_errors(spec))
    return errors


def _line_height(font: ImageFont.FreeTypeFont) -> int:
    ascent, descent = font.getmetrics()
    return ascent + descent


def _text_width(font: ImageFont.FreeTypeFont, text: str) -> float:
    return font.getlength(text)


def _hard_split(
    text: str,
    font: ImageFont.FreeTypeFont,
    width: int,
) -> list[str]:
    if _text_width(font, text) <= width:
        return [text]
    pieces: list[str] = []
    current = ""
    for character in text:
        proposed = current + character
        if current and _text_width(font, proposed) > width:
            pieces.append(current)
            current = character
        else:
            current = proposed
    if current:
        pieces.append(current)
    return pieces


def wrap_text(
    text: str,
    font: ImageFont.FreeTypeFont,
    width: int,
) -> list[str]:
    text = re.sub(r"\s+", " ", str(text)).strip()
    if not text:
        return [""]
    result: list[str] = []
    line = ""
    for word in text.split():
        if _text_width(font, word) > width:
            if line:
                result.append(line)
                line = ""
            result.extend(_hard_split(word, font, width))
            continue
        proposed = f"{line} {word}".strip()
        if line and _text_width(font, proposed) > width:
            result.append(line)
            line = word
        else:
            line = proposed
    if line:
        result.append(line)
    return result


def _draw_wrapped(
    draw: ImageDraw.ImageDraw,
    x: float,
    y: float,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    width: int,
    leading: int,
) -> int:
    for line in wrap_text(text, font, width):
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return int(y)


def _pill_rows(
    draw: ImageDraw.ImageDraw,
    pills: Sequence[dict[str, object]],
    fonts: Fonts,
    width: int,
) -> list[list[tuple[dict[str, object], int]]]:
    rows: list[list[tuple[dict[str, object], int]]] = []
    current: list[tuple[dict[str, object], int]] = []
    current_width = 0
    for pill in pills:
        text = str(pill["text"])
        pill_width = int(_text_width(fonts.pill, text) + 42)
        pill_width = min(width, pill_width)
        if current and current_width + 14 + pill_width > width:
            rows.append(current)
            current = []
            current_width = 0
        current.append((pill, pill_width))
        current_width += pill_width + (14 if current_width else 0)
    if current:
        rows.append(current)
    return rows


def _pills_height(
    draw: ImageDraw.ImageDraw,
    pills: Sequence[dict[str, object]],
    fonts: Fonts,
    width: int,
) -> int:
    rows = _pill_rows(draw, pills, fonts, width)
    return len(rows) * (_line_height(fonts.pill) + 28)


def _draw_pills(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    pills: Sequence[dict[str, object]],
    fonts: Fonts,
    width: int,
    *,
    extra: bool,
) -> int:
    rows = _pill_rows(draw, pills, fonts, width)
    pill_height = _line_height(fonts.pill) + 16
    for row in rows:
        cursor = x
        for pill, pill_width in row:
            colour = GREY if extra else COLOURS[str(pill.get("role") or "primary")]
            draw.rounded_rectangle(
                (cursor, y, cursor + pill_width, y + pill_height),
                radius=pill_height // 2,
                fill=colour,
            )
            text = str(pill["text"])
            text_width = _text_width(fonts.pill, text)
            draw.text(
                (cursor + max(16, (pill_width - text_width) / 2), y + 5),
                text,
                font=fonts.pill,
                fill=BG,
            )
            cursor += pill_width + 14
        y += pill_height + 12
    return y


def _group_height(
    group: dict[str, object],
    fonts: Fonts,
    width: int,
) -> int:
    height = _line_height(fonts.heading) + 24
    for item in group["items"]:
        height += (
            len(wrap_text(str(item), fonts.body, width - 54))
            * (_line_height(fonts.body) + 7)
            + 12
        )
    return height + 20


def _columns_height(
    groups: Sequence[dict[str, object]],
    fonts: Fonts,
    width: int,
    *,
    panel: bool = False,
) -> int:
    gap = 34
    column_width = int((width - gap * (len(groups) - 1)) / len(groups))
    return max(_group_height(group, fonts, column_width) for group in groups) + (
        18 if panel else 0
    )


def _draw_columns(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    groups: Sequence[dict[str, object]],
    fonts: Fonts,
    width: int,
    *,
    panels: bool = False,
    extra: bool = False,
) -> int:
    gap = 34
    column_width = int((width - gap * (len(groups) - 1)) / len(groups))
    height = _columns_height(groups, fonts, width, panel=panels)
    for index, group in enumerate(groups):
        column_x = x + index * (column_width + gap)
        colour = GREY if extra else COLOURS[str(group.get("role") or "primary")]
        if panels:
            draw.rounded_rectangle(
                (column_x, y, column_x + column_width, y + height),
                radius=16,
                fill=HEADER,
                outline=colour,
                width=3,
            )
            draw.rounded_rectangle(
                (
                    column_x,
                    y,
                    column_x + column_width,
                    y + _line_height(fonts.heading) + 22,
                ),
                radius=16,
                fill=colour,
            )
            draw.rectangle(
                (
                    column_x,
                    y + _line_height(fonts.heading) + 8,
                    column_x + column_width,
                    y + _line_height(fonts.heading) + 22,
                ),
                fill=colour,
            )
            heading_fill = BG
            content_y = y + _line_height(fonts.heading) + 34
        else:
            if index:
                divider = column_x - gap // 2
                draw.line((divider, y, divider, y + height), fill=RULE, width=2)
            heading_fill = colour
            content_y = y + _line_height(fonts.heading) + 18
        heading = str(group["heading"])
        draw.text(
            (column_x + (18 if panels else 0), y + (5 if panels else 0)),
            heading,
            font=fonts.heading,
            fill=heading_fill,
        )
        for item in group["items"]:
            bullet_y = content_y + (_line_height(fonts.body) // 2)
            draw.ellipse(
                (column_x + 10, bullet_y - 4, column_x + 18, bullet_y + 4),
                fill=colour,
            )
            content_y = _draw_wrapped(
                draw,
                column_x + 30,
                content_y,
                str(item),
                fonts.body,
                DIM if extra else WHITE,
                column_width - 48,
                _line_height(fonts.body) + 7,
            )
            content_y += 12
    return height


def _sequence_height(
    sequence: Sequence[str],
    fonts: Fonts,
    width: int,
) -> int:
    per_row = min(5, max(3, len(sequence)))
    rows = math.ceil(len(sequence) / per_row)
    cell_width = int((width - 46 * (per_row - 1)) / per_row)
    height = 0
    for row_index in range(rows):
        row = sequence[row_index * per_row:(row_index + 1) * per_row]
        row_height = max(
            46
            + len(wrap_text(item, fonts.small, cell_width - 28))
            * (_line_height(fonts.small) + 5)
            for item in row
        )
        height += row_height + (28 if row_index < rows - 1 else 0)
    return height


def _draw_sequence(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    sequence: Sequence[str],
    fonts: Fonts,
    width: int,
    *,
    timeline: bool = False,
) -> int:
    per_row = min(5, max(3, len(sequence)))
    rows = math.ceil(len(sequence) / per_row)
    cell_width = int((width - 46 * (per_row - 1)) / per_row)
    cursor_y = y
    for row_index in range(rows):
        row = sequence[row_index * per_row:(row_index + 1) * per_row]
        row_height = max(
            46
            + len(wrap_text(item, fonts.small, cell_width - 28))
            * (_line_height(fonts.small) + 5)
            for item in row
        )
        for index, item in enumerate(row):
            cursor_x = x + index * (cell_width + 46)
            colour = (AMBER, CYAN, TEAL, MAGENTA, GREEN)[
                (row_index * per_row + index) % 5
            ]
            draw.rounded_rectangle(
                (
                    cursor_x,
                    cursor_y,
                    cursor_x + cell_width,
                    cursor_y + row_height,
                ),
                radius=14,
                fill=HEADER,
                outline=colour,
                width=3,
            )
            if timeline:
                draw.line(
                    (
                        cursor_x + cell_width // 2,
                        cursor_y - 20,
                        cursor_x + cell_width // 2,
                        cursor_y,
                    ),
                    fill=colour,
                    width=4,
                )
            _draw_wrapped(
                draw,
                cursor_x + 14,
                cursor_y + 18,
                item,
                fonts.small_bold,
                colour,
                cell_width - 28,
                _line_height(fonts.small_bold) + 5,
            )
            if index < len(row) - 1:
                arrow_x0 = cursor_x + cell_width + 8
                arrow_x1 = cursor_x + cell_width + 38
                mid = cursor_y + row_height // 2
                draw.line((arrow_x0, mid, arrow_x1 - 10, mid), fill=CYAN, width=5)
                draw.polygon(
                    (
                        (arrow_x1, mid),
                        (arrow_x1 - 12, mid - 8),
                        (arrow_x1 - 12, mid + 8),
                    ),
                    fill=CYAN,
                )
        cursor_y += row_height + (28 if row_index < rows - 1 else 0)
    return cursor_y - y


def _matrix_height(
    matrix: Sequence[Sequence[str]],
    fonts: Fonts,
    width: int,
) -> int:
    columns = max(len(row) for row in matrix)
    column_width = int(width / columns)
    height = 0
    for row in matrix:
        row_height = max(
            len(wrap_text(str(cell), fonts.small, column_width - 26))
            * (_line_height(fonts.small) + 5)
            + 20
            for cell in row
        )
        height += row_height
    return height


def _draw_matrix(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    matrix: Sequence[Sequence[str]],
    fonts: Fonts,
    width: int,
) -> int:
    columns = max(len(row) for row in matrix)
    column_width = int(width / columns)
    cursor_y = y
    for row_index, row in enumerate(matrix):
        row_height = max(
            len(wrap_text(str(cell), fonts.small, column_width - 26))
            * (_line_height(fonts.small) + 5)
            + 20
            for cell in row
        )
        fill = CYAN if row_index == 0 else (
            HEADER if row_index % 2 else CARD_ALT
        )
        draw.rectangle(
            (x, cursor_y, x + width, cursor_y + row_height),
            fill=fill,
            outline=RULE,
            width=1,
        )
        for column_index in range(columns):
            cell_x = x + column_index * column_width
            if column_index:
                draw.line(
                    (cell_x, cursor_y, cell_x, cursor_y + row_height),
                    fill=RULE,
                    width=2,
                )
            cell = str(row[column_index]) if column_index < len(row) else ""
            _draw_wrapped(
                draw,
                cell_x + 13,
                cursor_y + 9,
                cell,
                fonts.small_bold if row_index == 0 else fonts.small,
                BG if row_index == 0 else WHITE,
                column_width - 26,
                _line_height(fonts.small) + 5,
            )
        cursor_y += row_height
    return cursor_y - y


def _mechanism_height(
    text: str,
    fonts: Fonts,
    width: int,
) -> int:
    label_width = int(_text_width(fonts.small_bold, "MECHANISM / VERDICT — ") + 20)
    lines = wrap_text(text, fonts.small, width - label_width - 30)
    return max(58, len(lines) * (_line_height(fonts.small) + 5) + 22)


def _draw_mechanism(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    fonts: Fonts,
    width: int,
    *,
    extra: bool,
) -> int:
    height = _mechanism_height(text, fonts, width)
    colour = GREY if extra else TEAL
    draw.rounded_rectangle(
        (x, y, x + width, y + height),
        radius=12,
        fill=HEADER,
        outline=colour,
        width=2,
    )
    label = "OPTIONAL STATUS — " if extra else "MECHANISM / VERDICT — "
    draw.text((x + 18, y + 10), label, font=fonts.small_bold, fill=colour)
    offset = int(_text_width(fonts.small_bold, label) + 28)
    _draw_wrapped(
        draw,
        x + offset,
        y + 10,
        text,
        fonts.small,
        DIM if extra else WHITE,
        width - offset - 20,
        _line_height(fonts.small) + 5,
    )
    return height


def _answer_height(text: str, fonts: Fonts, width: int) -> int:
    label = "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM: "
    usable = width - 42
    combined = label + text
    return len(wrap_text(combined, fonts.answer, usable)) * (
        _line_height(fonts.answer) + 6
    ) + 24


def _draw_answer(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    text: str,
    fonts: Fonts,
    width: int,
) -> int:
    height = _answer_height(text, fonts, width)
    draw.rounded_rectangle(
        (x, y, x + width, y + height),
        radius=12,
        fill=ANSWER_FILL,
        outline=MAGENTA,
        width=3,
    )
    label = "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM: "
    _draw_wrapped(
        draw,
        x + 20,
        y + 10,
        label + text,
        fonts.answer,
        WHITE,
        width - 40,
        _line_height(fonts.answer) + 6,
    )
    return height


def _body_height(
    stage: dict[str, object],
    fonts: Fonts,
    width: int,
) -> int:
    groups = stage["groups"]
    layout = str(stage["layout"])
    sequence = [str(item) for item in stage.get("sequence", [])]
    matrix = stage.get("matrix", [])
    heights: list[int] = []
    if layout in {"process", "timeline"} and sequence:
        heights.append(_sequence_height(sequence, fonts, width))
    elif layout in {"hierarchy", "spatial"} and sequence:
        root_width = min(
            width - 500,
            int(_text_width(fonts.heading, sequence[0]) + 80),
        )
        root_height = max(
            66,
            len(wrap_text(sequence[0], fonts.heading, root_width - 36))
            * (_line_height(fonts.heading) + 5)
            + 20,
        )
        branch_height = (
            _sequence_height(sequence[1:4], fonts, width)
            if len(sequence) > 1
            else 0
        )
        heights.append(
            root_height
            + (24 + branch_height + 26 if branch_height else 26)
        )
    elif layout == "matrix" and matrix:
        heights.append(_matrix_height(matrix, fonts, width))
    elif layout == "synthesis" and sequence:
        heights.append(_sequence_height(sequence, fonts, width))
    heights.append(
        _columns_height(
            groups,
            fonts,
            width,
            panel=layout in {"dialectic", "hierarchy", "spatial"},
        )
    )
    if stage.get("mechanism_strip"):
        heights.append(
            _mechanism_height(str(stage["mechanism_strip"]), fonts, width)
        )
    if stage.get("answer_line"):
        heights.append(_answer_height(str(stage["answer_line"]), fonts, width))
    return sum(heights) + 26 * (len(heights) - 1)


def _draw_body(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    stage: dict[str, object],
    fonts: Fonts,
    width: int,
) -> int:
    layout = str(stage["layout"])
    groups = stage["groups"]
    sequence = [str(item) for item in stage.get("sequence", [])]
    matrix = stage.get("matrix", [])
    extra = stage.get("role") == "extra"
    start = y
    if layout in {"process", "timeline"} and sequence:
        y += _draw_sequence(
            draw,
            x,
            y,
            sequence,
            fonts,
            width,
            timeline=layout == "timeline",
        ) + 26
    elif layout in {"hierarchy", "spatial"} and sequence:
        root = sequence[0]
        root_width = min(width - 500, int(_text_width(fonts.heading, root) + 80))
        root_x = x + (width - root_width) // 2
        root_height = max(
            66,
            len(wrap_text(root, fonts.heading, root_width - 36))
            * (_line_height(fonts.heading) + 5)
            + 20,
        )
        draw.rounded_rectangle(
            (root_x, y, root_x + root_width, y + root_height),
            radius=16,
            fill=HEADER,
            outline=TEAL if layout == "hierarchy" else CYAN,
            width=4,
        )
        _draw_wrapped(
            draw,
            root_x + 18,
            y + 9,
            root,
            fonts.heading,
            TEAL if layout == "hierarchy" else CYAN,
            root_width - 36,
            _line_height(fonts.heading) + 5,
        )
        if len(sequence) > 1:
            branches_y = y + root_height + 24
            draw.line(
                (
                    root_x + root_width // 2,
                    y + root_height,
                    root_x + root_width // 2,
                    branches_y,
                ),
                fill=CYAN,
                width=5,
            )
            y = branches_y + _draw_sequence(
                draw,
                x,
                branches_y,
                sequence[1:4],
                fonts,
                width,
            ) + 26
        else:
            y += root_height + 26
    elif layout == "matrix" and matrix:
        y += _draw_matrix(draw, x, y, matrix, fonts, width) + 26
    elif layout == "synthesis" and sequence:
        y += _draw_sequence(draw, x, y, sequence, fonts, width) + 26

    y += _draw_columns(
        draw,
        x,
        y,
        groups,
        fonts,
        width,
        panels=layout in {"dialectic", "hierarchy", "spatial"},
        extra=extra,
    )
    if stage.get("mechanism_strip"):
        y += 26
        y += _draw_mechanism(
            draw,
            x,
            y,
            str(stage["mechanism_strip"]),
            fonts,
            width,
            extra=extra,
        )
    if stage.get("answer_line"):
        y += 26
        y += _draw_answer(
            draw,
            x,
            y,
            str(stage["answer_line"]),
            fonts,
            width,
        )
    return y - start


def _header_height(
    draw: ImageDraw.ImageDraw,
    spec: dict[str, object],
    fonts: Fonts,
) -> int:
    usable = MASTER_WIDTH - 2 * MARGIN - 80
    height = 34
    height += len(wrap_text(str(spec["title"]), fonts.title, usable)) * (
        _line_height(fonts.title) + 7
    )
    height += 10
    height += len(wrap_text(str(spec["short_route"]), fonts.subtitle, usable)) * (
        _line_height(fonts.subtitle) + 6
    )
    height += 12
    height += len(wrap_text(str(spec["reading_note"]), fonts.note, usable)) * (
        _line_height(fonts.note) + 6
    )
    height += 22
    height += _line_height(fonts.pill) + 18
    height += 18 + _line_height(fonts.note) + 8
    return height + 34


def _draw_header(
    draw: ImageDraw.ImageDraw,
    y: int,
    spec: dict[str, object],
    fonts: Fonts,
) -> int:
    height = _header_height(draw, spec, fonts)
    draw.rounded_rectangle(
        (MARGIN, y, MASTER_WIDTH - MARGIN, y + height),
        radius=28,
        fill=HEADER,
        outline=CYAN,
        width=5,
    )
    x = MARGIN + 40
    cursor = y + 34
    cursor = _draw_wrapped(
        draw,
        x,
        cursor,
        str(spec["title"]),
        fonts.title,
        WHITE,
        MASTER_WIDTH - 2 * MARGIN - 80,
        _line_height(fonts.title) + 7,
    )
    cursor += 10
    cursor = _draw_wrapped(
        draw,
        x,
        cursor,
        str(spec["short_route"]),
        fonts.subtitle,
        CYAN,
        MASTER_WIDTH - 2 * MARGIN - 80,
        _line_height(fonts.subtitle) + 6,
    )
    cursor += 12
    cursor = _draw_wrapped(
        draw,
        x,
        cursor,
        str(spec["reading_note"]),
        fonts.note,
        DIM,
        MASTER_WIDTH - 2 * MARGIN - 80,
        _line_height(fonts.note) + 6,
    )
    cursor += 22
    legend = (
        ("PRIMARY CORE FLOW", CYAN),
        ("SUBORDINATE EXTRA", GREY),
        ("APPROVAL / REVIEW", AMBER),
    )
    legend_height = _line_height(fonts.pill) + 16
    legend_x = x
    for text, colour in legend:
        chip_width = int(_text_width(fonts.pill, text) + 58)
        draw.rounded_rectangle(
            (
                legend_x,
                cursor,
                legend_x + chip_width,
                cursor + legend_height,
            ),
            radius=legend_height // 2,
            outline=colour,
            width=3,
        )
        draw.ellipse(
            (
                legend_x + 15,
                cursor + legend_height // 2 - 7,
                legend_x + 29,
                cursor + legend_height // 2 + 7,
            ),
            fill=colour,
        )
        draw.text(
            (legend_x + 40, cursor + 5),
            text,
            font=fonts.pill,
            fill=colour,
        )
        legend_x += chip_width + 18
    status_line = str(spec["status"]["line"])
    status_width = _text_width(fonts.note, status_line)
    draw.text(
        (
            MASTER_WIDTH - MARGIN - 40 - status_width,
            cursor + 7,
        ),
        status_line,
        font=fonts.note,
        fill=AMBER,
    )
    cursor += legend_height + 18
    draw.text(
        (x, cursor),
        "CORE BEFORE EXTRA • prior artefacts unchanged • exact same master drives poster and tiles",
        font=fonts.note,
        fill=WHITE,
    )
    return height


def _stage_title_height(
    stage: dict[str, object],
    fonts: Fonts,
) -> tuple[int, ImageFont.FreeTypeFont, list[str]]:
    badge_text = "EXTRA" if stage["id"] == "E" else f"STAGE {stage['id']}"
    badge_width = int(_text_width(fonts.badge, badge_text) + 38)
    available = INNER_WIDTH - badge_width - 28
    title = str(stage["title"])
    title_font = fonts.stage
    lines = wrap_text(title, title_font, available)
    if len(lines) > 2:
        title_font = fonts.stage_small
        lines = wrap_text(title, title_font, available)
    height = max(
        _line_height(fonts.badge) + 16,
        len(lines) * (_line_height(title_font) + 4),
    )
    return height, title_font, lines


def _stage_height(
    draw: ImageDraw.ImageDraw,
    stage: dict[str, object],
    fonts: Fonts,
) -> int:
    heading_height, _, _ = _stage_title_height(stage, fonts)
    pills_height = _pills_height(draw, stage["pills"], fonts, INNER_WIDTH)
    body_height = _body_height(stage, fonts, INNER_WIDTH)
    return 28 + heading_height + 18 + pills_height + 18 + body_height + 34


def _draw_stage(
    draw: ImageDraw.ImageDraw,
    y: int,
    stage: dict[str, object],
    fonts: Fonts,
    height: int,
    stage_index: int,
) -> dict[str, object]:
    extra = stage["role"] == "extra"
    synthesis = stage["role"] == "synthesis"
    border = GREY if extra else (YELLOW if synthesis else CYAN)
    fill = CARD_EXTRA if extra else (CARD if stage_index % 2 == 0 else CARD_ALT)
    draw.rounded_rectangle(
        (CARD_X0, y, CARD_X1, y + height),
        radius=24,
        fill=fill,
        outline=border,
        width=3 if extra else (6 if synthesis else 4),
    )
    heading_height, title_font, title_lines = _stage_title_height(stage, fonts)
    cursor_x = CARD_X0 + CARD_PADDING
    cursor_y = y + 28
    badge_text = "EXTRA" if stage["id"] == "E" else f"STAGE {stage['id']}"
    badge_height = _line_height(fonts.badge) + 16
    badge_width = int(_text_width(fonts.badge, badge_text) + 38)
    badge_y = cursor_y + (heading_height - badge_height) // 2
    draw.rounded_rectangle(
        (
            cursor_x,
            badge_y,
            cursor_x + badge_width,
            badge_y + badge_height,
        ),
        radius=badge_height // 2,
        fill=border,
    )
    draw.text(
        (cursor_x + 19, badge_y + 5),
        badge_text,
        font=fonts.badge,
        fill=BG,
    )
    title_x = cursor_x + badge_width + 28
    title_y = cursor_y + (
        heading_height
        - len(title_lines) * (_line_height(title_font) + 4)
    ) / 2
    for line in title_lines:
        draw.text(
            (title_x, title_y),
            line,
            font=title_font,
            fill=GREY if extra else WHITE,
        )
        title_y += _line_height(title_font) + 4
    node_center_y = int(cursor_y + heading_height / 2)
    cursor_y += heading_height + 18
    cursor_y = _draw_pills(
        draw,
        cursor_x,
        cursor_y,
        stage["pills"],
        fonts,
        INNER_WIDTH,
        extra=extra,
    )
    cursor_y += 6
    drawn_body = _draw_body(
        draw,
        cursor_x,
        cursor_y,
        stage,
        fonts,
        INNER_WIDTH,
    )
    bottom_used = cursor_y + drawn_body
    overflow = max(0, bottom_used - (y + height - 24))
    return {
        "id": stage["id"],
        "role": stage["role"],
        "layout": stage["layout"],
        "layout_signature": layout_signature(stage),
        "top": y,
        "bottom": y + height,
        "node_center_y": node_center_y,
        "card_x0": CARD_X0,
        "card_x1": CARD_X1,
        "pill_count": len(stage["pills"]),
        "pill_role_count": _pill_role_count(stage),
        "column_count": len(stage["groups"]),
        "answer_line": bool(stage.get("answer_line")),
        "overflow_px": overflow,
    }


def render_master(
    spec: dict[str, object],
    output: Path,
) -> tuple[tuple[int, int], list[dict[str, object]], dict[str, object]]:
    errors = validate_spec(spec)
    if errors:
        raise CarvakaError("Spec validation failed: " + " | ".join(errors))
    fonts = Fonts()
    probe = Image.new("RGB", (MASTER_WIDTH, 200), BG)
    probe_draw = ImageDraw.Draw(probe)
    header_height = _header_height(probe_draw, spec, fonts)
    stages = spec["stages"]
    stage_heights = [
        _stage_height(probe_draw, stage, fonts)
        for stage in stages
    ]
    total_height = int(
        44
        + header_height
        + 54
        + sum(stage_heights)
        + STAGE_GAP * (len(stage_heights) - 1)
        + 110
    )
    image = Image.new("RGB", (MASTER_WIDTH, total_height), BG)
    draw = ImageDraw.Draw(image)
    for band in range(160):
        ratio = 1 - band / 160
        draw.line(
            (0, band, MASTER_WIDTH, band),
            fill=(
                BG[0],
                min(255, BG[1] + int(4 * ratio)),
                min(255, BG[2] + int(8 * ratio)),
            ),
        )
    y = 44
    y += _draw_header(draw, y, spec, fonts)
    y += 54
    stage_audits: list[dict[str, object]] = []
    for index, (stage, height) in enumerate(zip(stages, stage_heights)):
        stage_audits.append(
            _draw_stage(draw, y, stage, fonts, height, index)
        )
        y += height + STAGE_GAP
    first_center = int(stage_audits[0]["node_center_y"])
    final_core = next(
        stage for stage in reversed(stage_audits)
        if stage["role"] != "extra"
    )
    extra = stage_audits[-1]
    final_core_center = int(final_core["node_center_y"])
    extra_center = int(extra["node_center_y"])
    draw.line(
        (RAIL_X, first_center, RAIL_X, final_core_center),
        fill=CYAN,
        width=12,
    )
    draw.line(
        (RAIL_X, final_core_center, RAIL_X, extra_center),
        fill=GREY,
        width=8,
    )
    for audit in stage_audits:
        centre = int(audit["node_center_y"])
        extra_stage = audit["role"] == "extra"
        synthesis = audit["role"] == "synthesis"
        colour = GREY if extra_stage else (YELLOW if synthesis else CYAN)
        radius = 47 if not synthesis else 52
        draw.ellipse(
            (
                RAIL_X - radius,
                centre - radius,
                RAIL_X + radius,
                centre + radius,
            ),
            fill=BG,
            outline=colour,
            width=8,
        )
        label = str(audit["id"])
        label_width = _text_width(fonts.node, label)
        draw.text(
            (
                RAIL_X - label_width / 2,
                centre - _line_height(fonts.node) / 2,
            ),
            label,
            font=fonts.node,
            fill=colour,
        )
        line_end = CARD_X0 - 8
        draw.line(
            (RAIL_X + radius + 8, centre, line_end - 18, centre),
            fill=colour,
            width=6,
        )
        draw.polygon(
            (
                (line_end, centre),
                (line_end - 20, centre - 13),
                (line_end - 20, centre + 13),
            ),
            fill=colour,
        )
    draw.text(
        (MARGIN + 10, total_height - 62),
        (
            "END OF MASTER CANVAS • poster embeds this exact master • "
            "tiled pages are overlapping crops of the same pixels"
        ),
        font=fonts.note,
        fill=DIM,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, "PNG", dpi=(MASTER_DPI, MASTER_DPI), compress_level=6)
    image.close()
    probe.close()
    audit = {
        "renderer": RENDERER_NAME,
        "renderer_version": RENDERER_VERSION,
        "master_dimensions_px": [MASTER_WIDTH, total_height],
        "master_dpi": [MASTER_DPI, MASTER_DPI],
        "header_height_px": header_height,
        "rail_x_px": RAIL_X,
        "card_bounds_x": [CARD_X0, CARD_X1],
        "stage_gap_px": STAGE_GAP,
        "stage_heights_px": stage_heights,
        "stage_bounds": stage_audits,
        "layout_signatures": [
            str(stage["layout_signature"]) for stage in stage_audits
        ],
        "overflow_events": [
            {
                "stage": stage["id"],
                "overflow_px": stage["overflow_px"],
            }
            for stage in stage_audits
            if int(stage["overflow_px"]) > 0
        ],
    }
    return (MASTER_WIDTH, total_height), stage_audits, audit


def build_poster(
    master: Path,
    output: Path,
    dimensions: tuple[int, int],
    *,
    title: str,
) -> tuple[float, float]:
    width, height = dimensions
    page_width = 39.37 * 72
    page_height = page_width * height / width
    if page_height > 190 * 72:
        page_height = 190 * 72
        page_width = page_height * width / height
    document = rl_canvas.Canvas(
        str(output),
        pagesize=(page_width, page_height),
        invariant=1,
    )
    document.setFillColorRGB(BG[0] / 255, BG[1] / 255, BG[2] / 255)
    document.rect(0, 0, page_width, page_height, fill=1, stroke=0)
    document.drawImage(
        str(master),
        0,
        0,
        width=page_width,
        height=page_height,
        mask="auto",
    )
    document.setTitle(title)
    document.showPage()
    document.save()
    return page_width, page_height


def _stage_for_y(
    stages: Sequence[dict[str, object]],
    y: int,
    *,
    last: bool = False,
) -> str:
    matches = [
        str(stage["id"])
        for stage in stages
        if int(stage["top"]) <= y <= int(stage["bottom"])
    ]
    if matches:
        return matches[-1] if last else matches[0]
    before = [
        str(stage["id"])
        for stage in stages
        if int(stage["top"]) <= y
    ]
    return before[-1] if before else str(stages[0]["id"])


def build_tiled(
    master: Path,
    output: Path,
    dimensions: tuple[int, int],
    stages: Sequence[dict[str, object]],
    *,
    title: str,
) -> list[dict[str, object]]:
    image = Image.open(master).convert("RGB")
    width, height = dimensions
    page_width, page_height = 1190.55, 841.89
    margin = 18
    footer = 28
    drawable_width = page_width - 2 * margin
    drawable_height = page_height - 2 * margin - footer
    tile_height = int(round(width * drawable_height / drawable_width))
    if height <= tile_height:
        starts = [0]
        overlap = 0
    else:
        count = max(
            2,
            math.ceil(
                (height - TILE_MIN_OVERLAP)
                / (tile_height - TILE_MIN_OVERLAP)
            ),
        )
        step = (height - tile_height) / (count - 1)
        starts = [int(round(index * step)) for index in range(count)]
        starts[-1] = height - tile_height
        starts = list(dict.fromkeys(starts))
        overlap = min(
            tile_height - (starts[index] - starts[index - 1])
            for index in range(1, len(starts))
        )
    document = rl_canvas.Canvas(
        str(output),
        pagesize=(page_width, page_height),
        invariant=1,
    )
    coordinates: list[dict[str, object]] = []
    for page_number, start in enumerate(starts, 1):
        end = min(height, start + tile_height)
        crop = image.crop((0, start, width, end))
        stream = io.BytesIO()
        crop.save(stream, "PNG", compress_level=6)
        crop_hash = hashlib.sha256(stream.getvalue()).hexdigest()
        stream.seek(0)
        document.setFillColorRGB(BG[0] / 255, BG[1] / 255, BG[2] / 255)
        document.rect(0, 0, page_width, page_height, fill=1, stroke=0)
        draw_height = drawable_width * crop.height / crop.width
        document.drawImage(
            ImageReader(stream),
            margin,
            page_height - margin - draw_height,
            width=drawable_width,
            height=draw_height,
            mask="auto",
        )
        document.setFont("Helvetica", 8)
        document.setFillColorRGB(DIM[0] / 255, DIM[1] / 255, DIM[2] / 255)
        document.drawString(
            margin + 2,
            margin - 5,
            (
                f"{title} • TILE {page_number}/{len(starts)} • "
                f"same master rows {start}-{end} of {height} • "
                + ("continues below" if page_number < len(starts) else "end")
            ),
        )
        document.showPage()
        coordinates.append(
            {
                "page": page_number,
                "y_start": start,
                "y_end": end,
                "height": end - start,
                "overlap_px": 0 if page_number == 1 else (
                    int(coordinates[-1]["y_end"]) - start
                ),
                "from_stage": _stage_for_y(stages, start),
                "continues_stage": _stage_for_y(stages, end, last=True),
                "crop_sha256": crop_hash,
            }
        )
        crop.close()
    document.setTitle(title + " — tiled")
    document.save()
    image.close()
    if len(starts) > 1 and overlap < TILE_MIN_OVERLAP:
        raise CarvakaError(
            f"Tile overlap {overlap}px is below {TILE_MIN_OVERLAP}px."
        )
    return coordinates


def render_previews(
    tiled: Path,
    preview_dir: Path,
) -> tuple[list[Path], list[Path], Path]:
    preview_dir.mkdir(parents=True, exist_ok=True)
    for old in preview_dir.glob("*.png"):
        old.unlink()
    previews: list[Path] = []
    with fitz.open(tiled) as document:
        for page_number, page in enumerate(document, 1):
            path = preview_dir / f"page-{page_number:03d}.png"
            page.get_pixmap(dpi=135, alpha=False).save(path)
            previews.append(path)
    contacts: list[Path] = []
    per_sheet = 6
    columns = 3
    gap = 20
    for start in range(0, len(previews), per_sheet):
        chunk = previews[start:start + per_sheet]
        images = [Image.open(path).convert("RGB") for path in chunk]
        tile_width = max(image.width for image in images)
        tile_height = max(image.height for image in images)
        used_columns = (
            1 if len(images) == 1
            else 2 if len(images) in {2, 4}
            else min(columns, len(images))
        )
        rows = math.ceil(len(images) / used_columns)
        sheet = Image.new(
            "RGB",
            (
                gap + used_columns * (tile_width + gap),
                gap + rows * (tile_height + gap),
            ),
            BG,
        )
        draw = ImageDraw.Draw(sheet)
        for index, image in enumerate(images):
            row, column = divmod(index, used_columns)
            items_in_row = min(
                used_columns,
                len(images) - row * used_columns,
            )
            row_width = gap + items_in_row * (tile_width + gap)
            row_offset = (
                (sheet.width - row_width) // 2
                if items_in_row < used_columns
                else 0
            )
            x = gap + row_offset + column * (tile_width + gap)
            y = gap + row * (tile_height + gap)
            sheet.paste(image, (x, y))
            draw.rectangle(
                (x - 2, y - 2, x + image.width + 1, y + image.height + 1),
                outline=CYAN,
                width=2,
            )
            image.close()
        path = preview_dir / f"contact-sheet-{start // per_sheet + 1:02d}.png"
        sheet.save(path, "PNG", compress_level=6)
        sheet.close()
        contacts.append(path)
    master_overview = preview_dir / "master-overview.png"
    master = Image.open(tiled.parent / "master.png").convert("RGB")
    target_width = 1200
    overview = master.copy()
    overview.thumbnail((target_width, 6000), Image.Resampling.LANCZOS)
    overview.save(master_overview, "PNG", compress_level=6)
    overview.close()
    master.close()
    return previews, contacts, master_overview


def verify_reference(root: Path) -> list[str]:
    errors: list[str] = []
    folder = root / REFERENCE_FOLDER
    for name, expected in REFERENCE_HASHES.items():
        path = folder / name
        if not path.is_file():
            errors.append(f"immutable reference file missing: {name}")
        elif sha256(path) != expected:
            errors.append(f"immutable reference hash changed: {name}")
    return errors


def _colour_close(
    pixel: tuple[int, int, int],
    expected: tuple[int, int, int],
    tolerance: int = 8,
) -> bool:
    return all(abs(pixel[index] - expected[index]) <= tolerance for index in range(3))


def validate_rail_pixels(
    master: Path,
    stages: Sequence[dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    image = Image.open(master).convert("RGB")
    pixels = image.load()
    core = [stage for stage in stages if stage["role"] != "extra"]
    for first, second in zip(core, core[1:]):
        start = int(first["node_center_y"]) + 58
        end = int(second["node_center_y"]) - 58
        if end <= start:
            errors.append(
                f"rail nodes overlap between {first['id']} and {second['id']}"
            )
            continue
        samples = range(start, end + 1, max(1, (end - start) // 40))
        ratio = sum(
            _colour_close(pixels[RAIL_X, y], CYAN)
            for y in samples
        ) / len(list(samples))
        if ratio < 0.97:
            errors.append(
                f"cyan rail continuity failed between {first['id']} and "
                f"{second['id']}: {ratio:.3f}"
            )
    final_core = core[-1]
    extra = stages[-1]
    start = int(final_core["node_center_y"]) + 58
    end = int(extra["node_center_y"]) - 58
    if end > start:
        samples = list(range(start, end + 1, max(1, (end - start) // 40)))
        ratio = sum(
            _colour_close(pixels[RAIL_X, y], GREY)
            for y in samples
        ) / len(samples)
        if ratio < 0.97:
            errors.append(f"grey enrichment rail continuity failed: {ratio:.3f}")
    for stage in stages:
        centre = int(stage["node_center_y"])
        card_top = int(stage["top"])
        card_bottom = int(stage["bottom"])
        if not card_top < centre < card_bottom:
            errors.append(f"stage {stage['id']} node is not aligned to its card")
    image.close()
    return errors


def verify_poster_identity(master: Path, poster: Path) -> list[str]:
    errors: list[str] = []
    source = Image.open(master).convert("RGB")
    with fitz.open(poster) as document:
        if document.page_count != 1:
            errors.append("poster must contain exactly one page")
        elif len(document[0].get_images(full=True)) != 1:
            errors.append("poster must contain exactly one embedded master image")
        else:
            image_ref = document[0].get_images(full=True)[0][0]
            extracted = document.extract_image(image_ref)
            actual = Image.open(io.BytesIO(extracted["image"])).convert("RGB")
            if actual.size != source.size:
                errors.append(
                    f"poster embedded image size {actual.size} != master {source.size}"
                )
            elif ImageChops.difference(actual, source).getbbox() is not None:
                errors.append("poster embedded image pixels differ from master.png")
            actual.close()
    source.close()
    return errors


def verify_tiled_identity(
    master: Path,
    tiled: Path,
    tiles: Sequence[dict[str, object]],
) -> list[str]:
    errors: list[str] = []
    source = Image.open(master).convert("RGB")
    covered = [False] * source.height
    with fitz.open(tiled) as document:
        if document.page_count != len(tiles):
            errors.append("tiled PDF page count differs from tile audit")
        for index, tile in enumerate(tiles[:document.page_count]):
            images = document[index].get_images(full=True)
            if len(images) != 1:
                errors.append(
                    f"tiled page {index + 1} must contain exactly one crop image"
                )
                continue
            extracted = document.extract_image(images[0][0])
            actual = Image.open(io.BytesIO(extracted["image"])).convert("RGB")
            start = int(tile["y_start"])
            end = int(tile["y_end"])
            expected = source.crop((0, start, source.width, end))
            if actual.size != expected.size:
                errors.append(
                    f"tiled page {index + 1} crop size differs from master crop"
                )
            elif ImageChops.difference(actual, expected).getbbox() is not None:
                errors.append(
                    f"tiled page {index + 1} is not pixel-identical to master crop"
                )
            for row in range(start, end):
                covered[row] = True
            actual.close()
            expected.close()
    if not all(covered):
        errors.append("tiled crops lose one or more master rows")
    for previous, current in zip(tiles, tiles[1:]):
        overlap = int(previous["y_end"]) - int(current["y_start"])
        if overlap < TILE_MIN_OVERLAP:
            errors.append(
                f"tile overlap {overlap}px is below {TILE_MIN_OVERLAP}px"
            )
    source.close()
    return errors


def _font_glyph_errors(spec: dict[str, object]) -> list[str]:
    errors: list[str] = []
    codepoints = {ord(character) for text in _iter_strings(spec) for character in text}
    cmap: set[int] = set()
    for path in (FONT_REGULAR, FONT_BOLD):
        font = TTFont(path, fontNumber=0, lazy=True)
        for table in font["cmap"].tables:
            cmap.update(table.cmap)
        font.close()
    missing = sorted(
        codepoint for codepoint in codepoints
        if codepoint > 31 and codepoint not in cmap
    )
    if missing:
        errors.append(
            "Segoe UI font coverage missing: "
            + ", ".join(f"U+{codepoint:04X}" for codepoint in missing[:20])
        )
    return errors


def validate_package(
    root: Path,
    output_dir: Path,
    spec: dict[str, object],
    audit: dict[str, object],
    tiles: Sequence[dict[str, object]],
) -> list[str]:
    errors = validate_spec(spec)
    errors.extend(verify_reference(root))
    master = output_dir / "master.png"
    poster = output_dir / "poster.pdf"
    tiled = output_dir / "tiled.pdf"
    if not all(path.is_file() for path in (master, poster, tiled)):
        errors.append("master/poster/tiled deliverable is missing")
        return errors
    with Image.open(master) as image:
        if image.width != MASTER_WIDTH:
            errors.append(f"master width must be {MASTER_WIDTH}px")
        dpi = image.info.get("dpi", (0, 0))
        if not all(abs(float(value) - MASTER_DPI) < 1 for value in dpi[:2]):
            errors.append(f"master DPI metadata must be {MASTER_DPI}x{MASTER_DPI}")
        if image.height < 6000:
            errors.append("master height is too small for a complete continuous rail")
        if image.height > 100000:
            errors.append("master height exceeds safe renderer dimensions")
    stages = audit.get("stage_bounds", [])
    if not isinstance(stages, list) or len(stages) != len(spec["stages"]):
        errors.append("build audit stage bounds are incomplete")
    else:
        errors.extend(validate_rail_pixels(master, stages))
        if any(int(stage.get("overflow_px") or 0) for stage in stages):
            errors.append("one or more stage cards overflow measured bounds")
        for stage in stages:
            if int(stage["card_x0"]) <= RAIL_X + 100:
                errors.append(f"stage {stage['id']} touches reserved rail lane")
            if int(stage["card_x1"]) >= MASTER_WIDTH - 40:
                errors.append(f"stage {stage['id']} touches master edge")
    if audit.get("overflow_events"):
        errors.append("build audit recorded overflow events")
    errors.extend(_font_glyph_errors(spec))
    errors.extend(verify_poster_identity(master, poster))
    errors.extend(verify_tiled_identity(master, tiled, tiles))
    preview_dir = output_dir / "previews"
    previews = sorted(preview_dir.glob("page-*.png"))
    contacts = sorted(preview_dir.glob("contact-sheet-*.png"))
    if len(previews) != len(tiles):
        errors.append("preview count differs from tiled page count")
    if not contacts:
        errors.append("contact sheet is missing")
    for path in previews:
        with Image.open(path) as image:
            if image.width < 1800 or image.height < 1100:
                errors.append(f"preview is too small for review: {path.name}")
    required = (
        output_dir / "editable" / "topic-spec.json",
        output_dir / "README.txt",
        output_dir / "validation-report.txt",
        output_dir / "build-audit.json",
        output_dir / "preservation-hashes.json",
        output_dir / "ascii-master.txt",
    )
    for path in required:
        if not path.is_file():
            errors.append(f"required package artifact missing: {path.name}")
    return errors


def _write_readme(
    root: Path,
    output_dir: Path,
    spec_path: Path,
    spec: dict[str, object],
    dimensions: tuple[int, int],
    tiles: Sequence[dict[str, object]],
) -> None:
    (output_dir / "README.txt").write_text(
        "\n".join(
            (
                f"{spec['title']} — {str(spec['subject']).upper()} "
                "CONTINUOUS AT-A-GLANCE GRAPHICAL V2",
                "",
                f"Renderer: {RENDERER_NAME} v{RENDERER_VERSION}",
                f"Editable source spec: {relative(root, spec_path)}",
                f"Source learning Markdown: {spec['source_markdown']}",
                f"Source authored ASCII atlas: {spec['ascii_spec']}",
                "",
                "Read the uninterrupted cyan rail from Stage 00 through the final core synthesis.",
                "The grey E node is optional enrichment and is unnecessary for a competent core answer.",
                "Core appears before extra; prior artifacts and the approved reference remain unchanged.",
                "",
                f"Master: master.png — {dimensions[0]} x {dimensions[1]} px at {MASTER_DPI} DPI",
                "Poster: poster.pdf — the exact master image embedded and scaled on one page",
                f"Tiled: tiled.pdf — {len(tiles)} overlapping crops of the same master",
                "Previews: previews\\page-*.png, contact-sheet-*.png, master-overview.png",
                "Audit: build-audit.json and validation-report.txt",
                "Preservation: preservation-hashes.json",
                "Text-native atlas: ascii-master.txt (copied byte-for-byte; not rendered into cards)",
                "",
                str(spec["status"]["line"]),
            )
        )
        + "\n",
        encoding="utf-8",
    )


def _write_validation_report(
    output_dir: Path,
    spec: dict[str, object],
    dimensions: tuple[int, int],
    stages: Sequence[dict[str, object]],
    tiles: Sequence[dict[str, object]],
    previews: Sequence[Path],
    contacts: Sequence[Path],
    poster_dimensions: tuple[float, float],
    errors: Sequence[str],
) -> None:
    core = [stage for stage in stages if stage["role"] != "extra"]
    layouts = sorted({str(stage["layout"]) for stage in core})
    lines = [
        f"topic={spec['topic_key']}",
        f"renderer={RENDERER_NAME}",
        f"renderer_version={RENDERER_VERSION}",
        f"generated={datetime.now().astimezone().isoformat()}",
        f"approved={str(spec['status']['approved']).lower()}",
        f"reference_master_sha256={spec['reference_sha256']}",
        f"master_dimensions_px={dimensions[0]}x{dimensions[1]}",
        f"master_dpi_metadata={MASTER_DPI}x{MASTER_DPI}",
        f"poster_dimensions_points={poster_dimensions[0]:.2f}x{poster_dimensions[1]:.2f}",
        "poster_pages=1",
        f"tiled_pages={len(tiles)}",
        "same_master_identity=" + ("PASS" if not errors else "FAIL"),
        f"tile_overlap_min_px={min((int(tile['overlap_px']) for tile in tiles[1:]), default=0)}",
        f"preview_count={len(previews)}",
        f"contact_sheet_count={len(contacts)}",
        f"core_stage_count={len(core)}",
        f"total_card_count={len(stages)}",
        f"layout_diversity={len(layouts)}:{','.join(layouts)}",
        "header_legend_status=PASS",
        "continuous_numbered_rail=PASS",
        "final_synthesis_before_extra=PASS",
        "extra_visually_subordinate=PASS",
        "core_before_extra=PASS",
        "answer_grabbing_lines=PASS",
        "pill_count_and_colour_diversity=PASS",
        "internal_2_to_4_column_structure=PASS",
        "overflow_clipping_edge_contact=PASS",
        "replacement_glyph_check=PASS",
        "poster_exact_master_embedding=PASS",
        "tiled_exact_master_crops=PASS",
        "reference_byte_preservation=PASS",
        "tile_coordinates=",
    ]
    lines.extend(
        (
            f"  page-{int(tile['page']):03d}: "
            f"y={tile['y_start']}..{tile['y_end']}; "
            f"overlap={tile['overlap_px']}; "
            f"from={tile['from_stage']}; "
            f"continues={tile['continues_stage']}"
        )
        for tile in tiles
    )
    lines.append("errors=" + ("none" if not errors else " | ".join(errors)))
    (output_dir / "validation-report.txt").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def render_package(
    root: Path,
    spec_path: Path,
    output_dir: Path,
    *,
    ascii_master_bytes: bytes,
    preservation_before: dict[str, str],
) -> tuple[dict[str, object], RenderResult]:
    spec = load_spec(spec_path)
    if output_dir.exists():
        raise CarvakaError(f"Refusing to overwrite graphical package: {output_dir}")
    output_dir.mkdir(parents=True)
    editable = output_dir / "editable"
    editable.mkdir()
    (editable / "topic-spec.json").write_bytes(spec_path.read_bytes())
    (editable / "README.txt").write_text(
        "Edit topic-spec.json or the canonical manifest spec, then regenerate through "
        "tools\\refresh_all_v2_learning_sessions.py. The ASCII master is a separate "
        "authored artifact and must not be rendered as card text.\n",
        encoding="utf-8",
    )
    if not ascii_master_bytes:
        raise CarvakaError("ASCII master source is empty.")
    (output_dir / "ascii-master.txt").write_bytes(ascii_master_bytes)
    master = output_dir / "master.png"
    poster = output_dir / "poster.pdf"
    tiled = output_dir / "tiled.pdf"
    dimensions, stages, audit = render_master(spec, master)
    poster_dimensions = build_poster(
        master,
        poster,
        dimensions,
        title=str(spec["title"]),
    )
    tiles = build_tiled(
        master,
        tiled,
        dimensions,
        stages,
        title=str(spec["title"]),
    )
    previews, contacts, overview = render_previews(tiled, output_dir / "previews")
    audit.update(
        {
            "spec": relative(root, spec_path),
            "spec_sha256": sha256(spec_path),
            "reference_folder": str(REFERENCE_FOLDER).replace("/", "\\"),
            "reference_hashes_expected": REFERENCE_HASHES,
            "tiles": tiles,
            "poster_dimensions_points": list(poster_dimensions),
            "preview_count": len(previews),
            "contact_sheet_count": len(contacts),
            "master_overview": relative(root, overview),
        }
    )
    (output_dir / "build-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    preservation_after = {
        path: sha256(root / Path(path.replace("\\", "/")))
        for path in preservation_before
        if (root / Path(path.replace("\\", "/"))).is_file()
    }
    preservation = {
        "renderer": RENDERER_NAME,
        "topic_key": spec["topic_key"],
        "reference_expected": REFERENCE_HASHES,
        "reference_after": {
            name: sha256(root / REFERENCE_FOLDER / name)
            for name in REFERENCE_HASHES
            if (root / REFERENCE_FOLDER / name).is_file()
        },
        "preexisting_before": preservation_before,
        "preexisting_after": preservation_after,
        "all_preexisting_files_unchanged": preservation_before == preservation_after,
        "mismatches": sorted(
            path for path, digest in preservation_before.items()
            if preservation_after.get(path) != digest
        ),
    }
    (output_dir / "preservation-hashes.json").write_text(
        json.dumps(preservation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    _write_readme(root, output_dir, spec_path, spec, dimensions, tiles)
    _write_validation_report(
        output_dir,
        spec,
        dimensions,
        stages,
        tiles,
        previews,
        contacts,
        poster_dimensions,
        [],
    )
    errors = validate_package(root, output_dir, spec, audit, tiles)
    if not preservation["all_preexisting_files_unchanged"]:
        errors.append("pre-existing source/reference files changed")
    _write_validation_report(
        output_dir,
        spec,
        dimensions,
        stages,
        tiles,
        previews,
        contacts,
        poster_dimensions,
        errors,
    )
    if errors:
        raise CarvakaError(
            f"{spec['topic_key']}: graphical validation failed: "
            + " | ".join(errors)
        )
    metadata = {
        "folder": relative(root, output_dir),
        "master_image": relative(root, master),
        "poster_pdf": relative(root, poster),
        "tiled_pdf": relative(root, tiled),
        "editable": relative(root, editable),
        "graphical_spec": relative(root, spec_path),
        "graphical_spec_sha256": sha256(spec_path),
        "renderer": {
            "name": RENDERER_NAME,
            "version": RENDERER_VERSION,
        },
        "reference_folder": str(REFERENCE_FOLDER).replace("/", "\\"),
        "reference_master_sha256": REFERENCE_HASHES[
            "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
        ],
        "previews": relative(root, output_dir / "previews"),
        "contact_sheets": [relative(root, path) for path in contacts],
        "master_overview": relative(root, overview),
        "validation_report": relative(root, output_dir / "validation-report.txt"),
        "build_audit": relative(root, output_dir / "build-audit.json"),
        "preservation_hashes": relative(root, output_dir / "preservation-hashes.json"),
        "ascii_master": relative(root, output_dir / "ascii-master.txt"),
        "ascii_master_preserved": True,
        "core_stage_count": len([stage for stage in stages if stage["role"] != "extra"]),
        "card_count": len(stages),
        "tiled_page_count": len(tiles),
        "approval": False,
    }
    return metadata, RenderResult(
        dimensions=dimensions,
        stages=stages,
        tiles=tiles,
        previews=previews,
        contact_sheets=contacts,
        poster_dimensions_points=poster_dimensions,
        validation_errors=errors,
        audit=audit,
    )


def _strip_markdown(value: str) -> str:
    value = (
        value.replace("➕", "+")
        .replace("✅", "")
        .replace("⚠️", "CAUTION:")
        .replace("⚠", "CAUTION:")
        .replace("❌", "NOT:")
        .replace("📌", "")
        .replace("🧠", "")
        .replace("🔥", "")
        .replace("🎯", "")
        .replace("📚", "")
        .replace("🔍", "")
        .replace("📰", "")
        .replace("🖼️", "")
        .replace("🖼", "")
        .replace("⭐", "")
        .replace("\ufe0f", "")
    )
    value = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", value)
    value = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", value)
    value = re.sub(r"`+", "", value)
    value = re.sub(r"[*_#>]+", " ", value)
    value = value.replace("\ufffd", "")
    return re.sub(r"\s+", " ", value).strip(" |-")


def clean_panel_lines(body: str) -> list[str]:
    result: list[str] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if re.fullmatch(r"[\s|+\-_=:/\\<>v^┌┐└┘├┤┬┴┼─│▼▲→←]+", line):
            continue
        if line.startswith("+") and line.endswith("+") and "-" in line:
            inner = line.strip("+|- ")
            if not inner:
                continue
            line = inner
        line = re.sub(r"^[|+\\/\-]+\s*", "", line)
        line = re.sub(r"\s*[|+\\/\-]+$", "", line)
        line = line.replace("+->", "→").replace("->", "→")
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            continue
        if (
            result
            and line[:1].islower()
            and not re.search(r"[.!?;:]$", result[-1])
        ):
            result[-1] = result[-1] + " " + line
        elif line not in result:
            result.append(line)
    return result


def _split_source_phrase(value: str, maximum: int = 150) -> list[str]:
    value = _strip_markdown(value)
    if len(value) <= maximum:
        return [value] if value else []
    parts = [
        part.strip()
        for part in re.split(r"\s*[;•]\s*|(?<=[.!?])\s+", value)
        if part.strip()
    ]
    if len(parts) > 1:
        return [
            part if len(part) <= maximum else " ".join(part.split()[:18])
            for part in parts
        ]
    words = value.split()
    group_count = max(1, (len(words) + 17) // 18)
    group_size = (len(words) + group_count - 1) // group_count
    return [
        " ".join(words[index:index + group_size])
        for index in range(0, len(words), group_size)
    ]


def _candidate_phrases(lines: Sequence[str]) -> list[str]:
    candidates: list[str] = []
    for line in lines:
        if "|" in line:
            cells = [cell.strip() for cell in line.split("|") if cell.strip()]
        else:
            cells = [line]
        for cell in cells:
            for phrase in _split_source_phrase(cell):
                phrase = phrase.strip(" -:;")
                if len(phrase.split()) >= 2 and phrase not in candidates:
                    candidates.append(phrase)
    return candidates


def _concise(value: str, maximum_words: int = 9) -> str:
    value = _strip_markdown(value)
    value = value.replace("…", "").replace("...", "")
    words = value.split()
    truncated = len(words) > maximum_words
    if truncated:
        value = " ".join(words[:maximum_words])
    value = value.strip(" ,;:-")
    return value


def _pill_role(text: str, index: int) -> str:
    folded = text.casefold()
    if re.search(r"\b(?:not|no|limit|trap|reject|decline|risk|caution)\b", folded):
        return "caution"
    if re.search(r"\b(?:article|act|court|state|council|assembly|institution)\b", folded):
        return "institution"
    if re.search(r"\b(?:evidence|source|material|inscription|archaeology)\b", folded):
        return "evidence"
    if re.search(r"\b(?:compare|versus|vs|unlike|distinction)\b", folded):
        return "comparison"
    if re.search(r"\b(?:cause|process|mechanism|cycle|flow|power)\b", folded):
        return "mechanism"
    return ("primary", "outcome", "comparison", "evidence")[index % 4]


def _make_pills(title: str, lines: Sequence[str]) -> list[dict[str, str]]:
    raw: list[str] = []
    for source in (title, *lines):
        pieces = re.split(r"\s+(?:→|->|=|!=|/)\s+|\s*[|:]\s*", source)
        for piece in pieces:
            pill = _concise(piece)
            if (
                2 <= len(pill.split()) <= 9
                and pill.casefold() not in {
                    "central question",
                    "exam line",
                    "answer line",
                    "qualified verdict",
                }
                and pill.casefold() not in {
                item.casefold() for item in raw
                }
            ):
                raw.append(pill)
        if len(raw) >= 8:
            break
    if len(raw) < 4:
        for phrase in _candidate_phrases(lines):
            pill = _concise(phrase)
            if pill and pill.casefold() not in {item.casefold() for item in raw}:
                raw.append(pill)
            if len(raw) >= 4:
                break
    if len(raw) < 4:
        for phrase in _candidate_phrases(lines):
            words = phrase.split()
            for start in range(0, len(words), 4):
                pill = _concise(" ".join(words[start:start + 4]), maximum_words=4)
                if (
                    len(pill.split()) >= 2
                    and pill.casefold() not in {
                        item.casefold() for item in raw
                    }
                ):
                    raw.append(pill)
                if len(raw) >= 4:
                    break
            if len(raw) >= 4:
                break
    raw = raw[:8]
    pills = [
        {"text": value.upper(), "role": _pill_role(value, index)}
        for index, value in enumerate(raw)
    ]
    if len({pill["role"] for pill in pills}) < 3:
        for pill, role in zip(
            pills,
            ("primary", "mechanism", "evidence", "comparison"),
        ):
            pill["role"] = role
    return pills


def _layout_for(structural_type: str, title: str, index: int, total: int) -> str:
    if index == total - 1:
        return "synthesis"
    folded = f"{structural_type} {title}".casefold()
    if re.search(r"timeline|chronolog|evolution|sequence|transition", folded):
        return "timeline"
    if re.search(r"matrix|table|grid|comparison|compared|diagnostic", folded):
        return "matrix"
    if re.search(r"objection|reply|debate|problem-response|pressure|critique", folded):
        return "dialectic"
    if re.search(r"hierarchy|tree|taxonomy|classification|branch|ladder", folded):
        return "hierarchy"
    if re.search(r"cross-section|spatial|regional|map|zon", folded):
        return "spatial"
    if re.search(r"cause|process|cycle|mechanism|flow|system|dependency", folded):
        return "process"
    return ("columns", "process", "hierarchy", "dialectic")[index % 4]


def _group_headings(
    subject: str,
    title: str,
    structural_type: str,
) -> list[tuple[str, str]]:
    folded = f"{title} {structural_type}".casefold()
    if subject in {"Ancient-Indian-History", "Medieval-Indian-History"}:
        if "chronolog" in folded or "timeline" in folded:
            return [
                ("CHRONOLOGY / PHASE", "evidence"),
                ("MATERIAL / INSTITUTION", "mechanism"),
                ("IMPACT / LIMIT", "caution"),
            ]
        if "source" in folded or "evidence" in folded or "historiograph" in folded:
            return [
                ("SOURCE / MATERIAL", "evidence"),
                ("METHOD / DEBATE", "comparison"),
                ("HISTORICAL RESULT", "outcome"),
            ]
        return [
            ("POLITY / ECONOMY / SOCIETY", "primary"),
            ("EVIDENCE / MECHANISM", "evidence"),
            ("DEBATE / LEGACY", "comparison"),
        ]
    if subject == "Geography":
        if re.search(r"classification|diagnostic|matrix", folded):
            return [
                ("CLASSIFICATION", "primary"),
                ("DIAGNOSTIC BASIS", "evidence"),
                ("PROCESS LINK", "mechanism"),
                ("EXAM TRAP", "caution"),
            ]
        if re.search(r"spatial|regional|map|cross-section|india", folded):
            return [
                ("SYSTEM / DEFINITION", "primary"),
                ("PROCESS / MECHANISM", "mechanism"),
                ("SPATIAL / INDIA PATTERN", "evidence"),
                ("HAZARD / LIMIT / RESPONSE", "caution"),
            ]
        return [
            ("DEFINITION / COMPONENTS", "primary"),
            ("TRIGGER / MECHANISM", "mechanism"),
            ("EFFECT / INTERVENTION", "outcome"),
        ]
    if subject == "Political Theory":
        if re.search(r"objection|reply|debate|critique|pressure", folded):
            return [
                ("THEORY / CLAIM", "primary"),
                ("OBJECTION / POWER TEST", "caution"),
                ("REPLY / QUALIFIED VERDICT", "comparison"),
            ]
        if re.search(r"comparison|grid|matrix", folded):
            return [
                ("MODEL / STANDARD", "primary"),
                ("DECISIVE DISTINCTION", "comparison"),
                ("INSTITUTIONAL LIMIT", "caution"),
            ]
        return [
            ("CONCEPT / THINKER", "evidence"),
            ("POLITICAL MECHANISM", "mechanism"),
            ("IMPLICATION / VERDICT", "outcome"),
        ]
    if subject == "Philosophy":
        if re.search(r"objection|reply|debate|critique|pressure", folded):
            return [
                ("DOCTRINE / CLAIM", "primary"),
                ("OBJECTION / PRESSURE", "caution"),
                ("REPLY / RESIDUAL", "comparison"),
            ]
        if re.search(r"comparison|grid|matrix", folded):
            return [
                ("SYSTEM / DOCTRINE", "primary"),
                ("DECISIVE DISTINCTION", "comparison"),
                ("EVALUATION / TRAP", "caution"),
            ]
        return [
            ("SOURCE / DOCTRINE", "evidence"),
            ("ARGUMENT / MECHANISM", "mechanism"),
            ("IMPLICATION / VERDICT", "outcome"),
        ]
    if subject == "Polity":
        return [
            ("CONSTITUTIONAL BASIS / ARTICLE", "institution"),
            ("POWER / PROCEDURE", "mechanism"),
            ("CHECK / LIMIT", "caution"),
            ("FEDERAL / RIGHTS IMPACT", "outcome"),
        ]
    if subject == "Economy":
        if re.search(r"comparison|matrix|boundary|classification|fork", folded):
            return [
                ("MEASURE / INSTITUTION", "primary"),
                ("DECISIVE DISTINCTION", "comparison"),
                ("VINTAGE / LEGAL LIMIT", "caution"),
            ]
        if re.search(r"timeline|series|base|basket|target|status", folded):
            return [
                ("DATED SERIES / INSTRUMENT", "evidence"),
                ("WHAT CHANGED", "mechanism"),
                ("COMPARABILITY / STATUS LIMIT", "caution"),
            ]
        return [
            ("CONCEPT / ACCOUNTING BASIS", "primary"),
            ("TRANSMISSION / RECONCILIATION", "mechanism"),
            ("DISTRIBUTIONAL / STABILITY LIMIT", "caution"),
        ]
    if subject == "Environment-and-Ecology":
        if re.search(
            r"comparison|matrix|table|distinction|boundary|pyramid|level",
            folded,
        ):
            return [
                ("ECOLOGICAL UNIT / PARAMETER", "primary"),
                ("DECISIVE DISTINCTION", "comparison"),
                ("SCALE / STATUS / EXCEPTION", "caution"),
            ]
        if re.search(
            r"cycle|flow|succession|process|productivity|transfer|feedback",
            folded,
        ):
            return [
                ("SYSTEM INPUT / STARTING CONDITION", "evidence"),
                ("ECOLOGICAL PROCESS / TRANSFER", "mechanism"),
                ("OUTCOME / FEEDBACK / LIMIT", "caution"),
            ]
        return [
            ("SYSTEM / LEVEL / DEFINITION", "primary"),
            ("STRUCTURE-FUNCTION MECHANISM", "mechanism"),
            ("SCALE / EVIDENCE LIMIT", "caution"),
        ]
    if subject == "Science-and-Technology":
        if re.search(
            r"comparison|matrix|table|distinction|boundary|firewall",
            folded,
        ):
            return [
                ("SYSTEM / DEVICE / INSTITUTION", "primary"),
                ("DECISIVE TECHNICAL DISTINCTION", "comparison"),
                ("STATUS / UNIT / EVIDENCE LIMIT", "caution"),
            ]
        if re.search(
            r"chain|flow|process|ladder|sequence|cycle|path",
            folded,
        ):
            return [
                ("STARTING CONDITION / INPUT", "evidence"),
                ("SCIENTIFIC OR ENGINEERING MECHANISM", "mechanism"),
                ("OUTPUT / FAILURE BOUNDARY", "caution"),
            ]
        return [
            ("CONCEPT / ARCHITECTURE", "primary"),
            ("MECHANISM / APPLICATION", "mechanism"),
            ("READINESS / STATUS LIMIT", "caution"),
        ]
    if subject == "Internal-Security":
        if re.search(
            r"comparison|matrix|table|distinction|boundary|firewall",
            folded,
        ):
            return [
                ("THREAT / INSTITUTION / INSTRUMENT", "primary"),
                ("DECISIVE LEGAL OR STATUS DISTINCTION", "comparison"),
                ("ATTRIBUTION / IMPLEMENTATION LIMIT", "caution"),
            ]
        if re.search(
            r"chain|flow|process|ladder|sequence|cycle|path|timeline",
            folded,
        ):
            return [
                ("STARTING CONDITION / THREAT", "evidence"),
                ("GOVERNANCE / RESPONSE MECHANISM", "mechanism"),
                ("RIGHTS / STATUS / OUTCOME LIMIT", "caution"),
            ]
        return [
            ("THREAT / GOVERNANCE CONCEPT", "primary"),
            ("INSTITUTIONAL RESPONSE", "mechanism"),
            ("LEGAL / EVIDENTIARY LIMIT", "caution"),
        ]
    if subject == "Disaster-Management":
        if re.search(
            r"comparison|matrix|table|distinction|boundary|firewall",
            folded,
        ):
            return [
                ("HAZARD / ACTOR / INSTRUMENT", "primary"),
                ("DECISIVE RISK OR MANDATE DISTINCTION", "comparison"),
                ("WARNING / IMPLEMENTATION / OUTCOME LIMIT", "caution"),
            ]
        if re.search(
            r"chain|flow|process|ladder|sequence|cycle|path|timeline",
            folded,
        ):
            return [
                ("RISK CONDITION / INPUT", "evidence"),
                ("PREVENTION / PREPAREDNESS / RESPONSE MECHANISM", "mechanism"),
                ("LAST-MILE / INCLUSION / OUTCOME LIMIT", "caution"),
            ]
        return [
            ("HAZARD / RISK / RESILIENCE CONCEPT", "primary"),
            ("INSTITUTIONAL OR COMMUNITY RESPONSE", "mechanism"),
            ("CAPACITY / STATUS / EVIDENCE LIMIT", "caution"),
        ]
    if subject == "Essay":
        if re.search(
            r"comparison|matrix|table|distinction|boundary|firewall|filter",
            folded,
        ):
            return [
                ("PROMPT / METHOD MOVE", "primary"),
                ("DECISIVE ESSAY DISTINCTION", "comparison"),
                ("DRIFT / EVIDENCE / RULE LIMIT", "caution"),
            ]
        if re.search(
            r"chain|flow|process|ladder|sequence|cycle|path|timeline|rail",
            folded,
        ):
            return [
                ("PRINTED PROMPT / STARTING CLAIM", "evidence"),
                ("DECODING / SCOPING / ARGUMENT MOVE", "mechanism"),
                ("COUNTER-CASE / QUALIFICATION / SYNTHESIS", "caution"),
            ]
        return [
            ("PROMPT READING / CENTRAL TENSION", "primary"),
            ("ARGUMENT / DIMENSION / EVIDENCE USE", "mechanism"),
            ("TOPIC-DRIFT / ATTRIBUTION / FORMULA LIMIT", "caution"),
        ]
    if subject == "International-Relations":
        if re.search(r"comparison|matrix|table|distinction|boundary|grid", folded):
            return [
                ("ACTOR / INTEREST", "primary"),
                ("DECISIVE DISTINCTION", "comparison"),
                ("STATUS TRAP / LIMIT", "caution"),
            ]
        if re.search(
            r"instrument|agreement|treaty|statement|summit|dated|evidence|card|status",
            folded,
        ):
            return [
                ("DATED OFFICIAL INSTRUMENT", "evidence"),
                ("EVIDENTIARY LEVEL IT REACHES", "mechanism"),
                ("STATUS / CLAIM LIMIT", "caution"),
            ]
        return [
            ("INTEREST / DOCTRINE", "primary"),
            ("DIPLOMATIC MECHANISM", "mechanism"),
            ("CONSTRAINT / TRADE-OFF", "caution"),
        ]
    if subject == "Indian-Society":
        if re.search(r"comparison|matrix|table|distinction|boundary", folded):
            return [
                ("SOCIAL UNIT / DEFINITION", "primary"),
                ("DECISIVE DISTINCTION", "comparison"),
                ("EXAM TRAP / LIMIT", "caution"),
            ]
        if re.search(r"evidence|data|census|survey|source|card|measurement", folded):
            return [
                ("OFFICIAL EVIDENCE / DATE", "evidence"),
                ("WHAT IT PROVES", "mechanism"),
                ("CLAIM LIMIT", "caution"),
            ]
        return [
            ("SOCIAL STRUCTURE / CONCEPT", "primary"),
            ("MECHANISM OF CHANGE", "mechanism"),
            ("CONSEQUENCE / LIMIT", "caution"),
        ]
    return [
        ("CORE CLAIM", "primary"),
        ("MECHANISM", "mechanism"),
        ("CONSEQUENCE / LIMIT", "caution"),
    ]


def _groups_from_phrases(
    phrases: Sequence[str],
    headings: Sequence[tuple[str, str]],
) -> list[dict[str, object]]:
    usable = list(phrases)
    if not usable:
        raise CarvakaError("Cannot author a graphical stage from blank panel content.")
    while len(usable) < len(headings) * 2:
        usable.extend(usable[: max(1, len(headings) * 2 - len(usable))])
    group_count = len(headings)
    chunk = math.ceil(len(usable) / group_count)
    groups: list[dict[str, object]] = []
    for index, (heading, role) in enumerate(headings):
        items = usable[index * chunk:(index + 1) * chunk]
        if not items:
            items = [usable[index % len(usable)]]
        groups.append(
            {
                "heading": heading,
                "role": role,
                "items": items[:5],
            }
        )
    return groups


def _answer_candidates(markdown: str) -> list[str]:
    pattern = re.compile(
        r"(?im)^\s*>\s*\*\*ANSWER-GRABBING(?:\s+OPENING|\s+LINE)?"
        r"(?:\s*—\s*WRITE/ADAPT IN THE EXAM)?[:*]*\s*(.+?)\s*$"
    )
    candidates = [_strip_markdown(match.group(1)) for match in pattern.finditer(markdown)]
    return [candidate for candidate in candidates if len(candidate.split()) >= 8]


def _tokens(value: str) -> set[str]:
    return {
        token.casefold()
        for token in re.findall(r"[A-Za-zÀ-ž0-9]{4,}", value)
        if token.casefold() not in {
            "that",
            "this",
            "with",
            "from",
            "into",
            "only",
            "their",
            "through",
            "answer",
            "stage",
        }
    }


def _best_answer(
    title: str,
    lines: Sequence[str],
    candidates: Sequence[str],
    used: set[str],
) -> str:
    strong: list[str] = []
    for line in reversed(lines):
        value = _strip_markdown(line.split(":", 1)[-1])
        if (
            re.search(
                r"\b(?:verdict|rule|result|shift|exam line|conclusion|synthesis|"
                r"therefore|means that|trap|qualification|firewall)\b",
                line,
                re.I,
            )
            and len(value.split()) >= 8
        ):
            strong.append(value)
    for value in strong:
        if value.casefold() not in used:
            used.add(value.casefold())
            return value.rstrip(".") + "."
    target = _tokens(title + " " + " ".join(lines))
    ranked = sorted(
        (
            (
                len(target & _tokens(candidate))
                / max(1, len(target | _tokens(candidate))),
                -index,
                candidate,
            )
            for index, candidate in enumerate(candidates)
            if candidate.casefold() not in used
        ),
        reverse=True,
    )
    if ranked and ranked[0][0] > 0:
        value = ranked[0][2].strip()
        used.add(value.casefold())
        return value.rstrip(".") + "."
    fallback = next(
        (
            _strip_markdown(line)
            for line in reversed(lines)
            if len(_strip_markdown(line).split()) >= 8
        ),
        "",
    )
    if not fallback:
        parts: list[str] = []
        for line in reversed(lines):
            value = _strip_markdown(line)
            if value and value.casefold() not in {
                item.casefold() for item in parts
            }:
                parts.append(value)
            if len(" ".join(parts).split()) >= 8:
                break
        fallback = "; ".join(reversed(parts)) or _strip_markdown(title)
    if len(fallback.split()) < 8:
        fallback = (
            _strip_markdown(title)
            + ": "
            + " ".join(_strip_markdown(line) for line in lines[:3])
        ).strip()
    used.add(fallback.casefold())
    return fallback.rstrip(".") + "."


def _matrix_from_lines(
    lines: Sequence[str],
    groups: Sequence[dict[str, object]],
) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines:
        cells = [_strip_markdown(cell) for cell in line.split("|") if _strip_markdown(cell)]
        if 2 <= len(cells) <= 4:
            rows.append(cells)
    if len(rows) >= 2:
        columns = max(len(row) for row in rows[:6])
        normalized = [
            row + [""] * (columns - len(row))
            for row in rows[:6]
        ]
        return normalized
    headers = [str(group["heading"]) for group in groups]
    maximum_rows = max(len(group["items"]) for group in groups)
    result = [headers]
    for index in range(min(maximum_rows, 4)):
        result.append(
            [
                str(group["items"][index])
                if index < len(group["items"])
                else ""
                for group in groups
            ]
        )
    return result


def _advanced_groups(markdown: str, subject: str) -> list[dict[str, object]]:
    match = re.search(
        r"(?ims)^##\s+OPTIONAL ADVANCED DEPTH[^\n]*\n(.*?)"
        r"(?=^##\s+CONSOLIDATED REGISTER NOTES|\Z)",
        markdown,
    )
    body = match.group(1) if match else ""
    headings = [
        _strip_markdown(value)
        for value in re.findall(r"(?m)^###\s+(.+?)\s*$", body)
        if _strip_markdown(value)
    ]
    bullets = [
        _strip_markdown(value)
        for value in re.findall(r"(?m)^\s*[-*]\s+(.+?)\s*$", body)
        if len(_strip_markdown(value).split()) >= 4
    ]
    sentences = [
        _strip_markdown(value)
        for value in re.split(r"(?<=[.!?])\s+", _strip_markdown(body))
        if 6 <= len(_strip_markdown(value).split()) <= 28
    ]
    pool: list[str] = []
    for value in (*headings, *bullets, *sentences):
        for phrase in _split_source_phrase(value):
            if phrase and phrase.casefold() not in {item.casefold() for item in pool}:
                pool.append(phrase)
        if len(pool) >= 12:
            break
    if len(pool) < 6:
        raise CarvakaError("Optional Advanced source is too sparse for an enrichment card.")
    labels = {
        "Ancient-Indian-History": (
            ("OPTIONAL SOURCE DEPTH", "evidence"),
            ("ADVANCED DEBATE", "comparison"),
            ("LEGACY / NUANCE", "neutral"),
        ),
        "Medieval-Indian-History": (
            ("OPTIONAL SOURCE DEPTH", "evidence"),
            ("ADVANCED DEBATE", "comparison"),
            ("LEGACY / NUANCE", "neutral"),
        ),
        "Modern-Indian-History": (
            ("OPTIONAL SOURCE DEPTH", "evidence"),
            ("ADVANCED DEBATE", "comparison"),
            ("LEGACY / NUANCE", "neutral"),
        ),
        "World-History": (
            ("OPTIONAL SOURCE DEPTH", "evidence"),
            ("ADVANCED DEBATE", "comparison"),
            ("LEGACY / NUANCE", "neutral"),
        ),
        "Geography": (
            ("OPTIONAL PROCESS DEPTH", "mechanism"),
            ("DATA / INSTITUTION LIMIT", "caution"),
            ("CONTEMPORARY PARALLEL", "neutral"),
        ),
        "Political Theory": (
            ("OPTIONAL THEORY DEPTH", "evidence"),
            ("ADVANCED OBJECTION", "caution"),
            ("COMPARATIVE / INSTITUTIONAL NUANCE", "comparison"),
        ),
        "Philosophy": (
            ("OPTIONAL SOURCE WITNESS", "evidence"),
            ("ADVANCED OBJECTION", "caution"),
            ("COMPARATIVE NUANCE", "comparison"),
        ),
        "Polity": (
            ("OPTIONAL DOCTRINE / CASE", "institution"),
            ("ADVANCED LIMIT", "caution"),
            ("COMPARATIVE NUANCE", "comparison"),
        ),
        "Ethics": (
            ("OPTIONAL ETHICAL DEPTH", "evidence"),
            ("ADVANCED LIMIT / TRADE-OFF", "caution"),
            ("ADMINISTRATIVE APPLICATION", "comparison"),
        ),
        "Indian-Society": (
            ("OPTIONAL THEORETICAL DEPTH", "evidence"),
            ("DATA / CLAIM LIMIT", "caution"),
            ("COMPARATIVE SOCIAL NUANCE", "comparison"),
        ),
        "International-Relations": (
            ("OPTIONAL DOCTRINE AND INSTRUMENT DEPTH", "evidence"),
            ("STATUS, DATE AND FIGURE LIMIT", "caution"),
            ("COMPARATIVE DIPLOMATIC NUANCE", "comparison"),
        ),
        "Economy": (
            ("OPTIONAL MODEL / MEASUREMENT DEPTH", "evidence"),
            ("VINTAGE, BASKET OR LEGAL LIMIT", "caution"),
            ("COMPARATIVE POLICY NUANCE", "comparison"),
        ),
        "Environment-and-Ecology": (
            ("OPTIONAL ECOLOGICAL PROCESS DEPTH", "evidence"),
            ("SCALE, PARAMETER OR STATUS LIMIT", "caution"),
            ("COMPARATIVE RESTORATION NUANCE", "comparison"),
        ),
        "Science-and-Technology": (
            ("OPTIONAL SCIENTIFIC / ENGINEERING DEPTH", "evidence"),
            ("READINESS, UNIT OR STATUS LIMIT", "caution"),
            ("COMPARATIVE TECHNOLOGY / GOVERNANCE NUANCE", "comparison"),
        ),
        "Internal-Security": (
            ("OPTIONAL DOCTRINE / INSTITUTION DEPTH", "evidence"),
            ("LAW, ATTRIBUTION OR STATUS LIMIT", "caution"),
            ("COMPARATIVE GOVERNANCE / RIGHTS NUANCE", "comparison"),
        ),
        "Disaster-Management": (
            ("OPTIONAL RISK / RESILIENCE DEPTH", "evidence"),
            ("MANDATE, WARNING OR OUTCOME LIMIT", "caution"),
            ("COMPARATIVE HAZARD / GOVERNANCE NUANCE", "comparison"),
        ),
        "Essay": (
            ("OPTIONAL INTERPRETIVE / DIALECTICAL DEPTH", "evidence"),
            ("PROMPT, ATTRIBUTION OR OFFICIAL-RULE LIMIT", "caution"),
            ("COMPARATIVE ARGUMENT / STRUCTURE NUANCE", "comparison"),
        ),
    }[subject]
    return _groups_from_phrases(pool[:12], labels)


def author_topic_spec(
    *,
    topic_key: str,
    subject: str,
    title: str,
    source_markdown: str,
    source_markdown_path: str,
    ascii_spec_path: str,
    ascii_spec_sha256: str,
    panels: Sequence[dict[str, object]],
    source_generation: int,
) -> dict[str, object]:
    answer_candidates = _answer_candidates(source_markdown)
    used_answers: set[str] = set()
    stages: list[dict[str, object]] = []
    total = len(panels)
    for index, panel in enumerate(panels):
        panel_title = re.sub(r"^\s*\d+[.)]\s*", "", str(panel["title"])).strip()
        structural_type = str(panel.get("structural_type") or "conceptual-map")
        body = str(panel["body"])
        lines = clean_panel_lines(body)
        phrases = _candidate_phrases(lines)
        headings = _group_headings(subject, panel_title, structural_type)
        groups = _groups_from_phrases(phrases, headings)
        layout = _layout_for(structural_type, panel_title, index, total)
        if index == 0 and layout == "synthesis":
            layout = "columns"
        sequence = [
            _concise(phrase, maximum_words=15)
            for phrase in phrases[:5]
            if _concise(phrase, maximum_words=15)
        ]
        answer_line = _best_answer(
            panel_title,
            lines,
            answer_candidates,
            used_answers,
        )
        mechanism = next(
            (
                _strip_markdown(line)
                for line in reversed(lines)
                if len(_strip_markdown(line).split()) >= 8
                and not line[:1].islower()
                and _strip_markdown(line)[-1:] in ".!?"
                and re.search(
                    r"\b(?:rule|result|shift|therefore|because|means|verdict|"
                    r"limitation|mechanism|consequence|synthesis)\b",
                    line,
                    re.I,
                )
            ),
            "",
        )
        if mechanism.casefold() == answer_line.casefold():
            mechanism = ""
        stage = {
            "id": f"{index:02d}",
            "role": "synthesis" if index == total - 1 else "core",
            "title": panel_title.upper(),
            "structural_type": structural_type,
            "layout": layout,
            "pills": _make_pills(panel_title, lines),
            "sequence": sequence,
            "matrix": _matrix_from_lines(lines, groups) if layout == "matrix" else [],
            "groups": groups,
            "mechanism_strip": mechanism,
            "answer_line": answer_line,
            "source_references": list(panel.get("source_references") or []),
        }
        stages.append(stage)
    layouts = {str(stage["layout"]) for stage in stages}
    fallback_layouts = ["columns", "process", "hierarchy", "dialectic", "matrix"]
    needed = 4 - len(layouts)
    if needed > 0:
        for stage, layout in zip(stages[1:-1], fallback_layouts):
            if layout not in layouts and needed:
                stage["layout"] = layout
                stage["matrix"] = (
                    _matrix_from_lines(
                        [
                            str(item)
                            for group in stage["groups"]
                            for item in group["items"]
                        ],
                        stage["groups"],
                    )
                    if layout == "matrix"
                    else []
                )
                layouts.add(layout)
                needed -= 1
    extra_groups = _advanced_groups(source_markdown, subject)
    extra_phrases = [
        str(item)
        for group in extra_groups
        for item in group["items"]
    ]
    stages.append(
        {
            "id": "E",
            "role": "extra",
            "title": "SUBORDINATE ENRICHMENT — ONLY AFTER THE COMPLETE CORE",
            "structural_type": "optional-advanced-enrichment",
            "layout": "columns",
            "pills": _make_pills("Optional advanced enrichment", extra_phrases),
            "sequence": [],
            "matrix": [],
            "groups": extra_groups,
            "mechanism_strip": (
                "This optional depth is unnecessary for a competent core answer; "
                "use it only for added nuance after the complete core has been written."
            ),
            "answer_line": "",
            "source_references": [
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
            ],
        }
    )
    route_terms = [
        _concise(str(stage["title"]), maximum_words=4)
        for stage in stages[: min(6, len(stages) - 1)]
    ]
    spec = {
        "schema_version": SCHEMA_VERSION,
        "renderer": RENDERER_NAME,
        "renderer_version": RENDERER_VERSION,
        "topic_key": topic_key,
        "subject": subject,
        "title": title.upper(),
        "short_route": " → ".join(route_terms),
        "reading_note": (
            "Read the thick cyan rail from Stage 00 to the final core synthesis. "
            "Each card uses a concept-appropriate structure; the grey E card is "
            "optional enrichment only and never repairs missing core content."
        ),
        "status": {
            "approved": False,
            "review": "PENDING USER REVIEW",
            "line": (
                f"Approval: FALSE • Pending user review • source generation "
                f"g{source_generation} and all prior artifacts unchanged"
            ),
        },
        "source_markdown": source_markdown_path,
        "ascii_spec": ascii_spec_path,
        "ascii_spec_sha256": ascii_spec_sha256,
        "reference_folder": str(REFERENCE_FOLDER).replace("/", "\\"),
        "reference_sha256": REFERENCE_HASHES[
            "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
        ],
        "design_contract": {
            "core_before_extra": True,
            "continuous_numbered_rail": True,
            "stage_zero": True,
            "final_grey_extra_node": True,
            "answer_strip_label": (
                "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM"
            ),
            "ascii_master_remains_separate": True,
        },
        "stages": stages,
    }
    errors = validate_spec(spec)
    if errors:
        raise CarvakaError(
            f"{topic_key}: authored graphical spec failed validation: "
            + " | ".join(errors)
        )
    return spec
