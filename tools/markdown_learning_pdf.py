"""
Render a complete UPSC learning-session Markdown file as an explanatory PDF.

Unlike the register-card compiler, this renderer preserves continuous
explanations, worked examples, Markdown tables, ASCII diagrams, questions,
solutions and final revision notes.

Usage:
    python tools/markdown_learning_pdf.py source.md output.pdf
    python tools/markdown_learning_pdf.py source.md workbook.pdf --mode workbook
    python tools/markdown_learning_pdf.py source.md output.pdf --image illustration.png
    python tools/markdown_learning_pdf.py source.md output.pdf --variant learner-v2 --topic-key <key>

Optional Markdown frontmatter:
    ---
    cover_image: relative/or/absolute/path.png
    ---
"""

from __future__ import annotations

import argparse
import html
import json
import re
from functools import partial
from pathlib import Path

from reportlab.graphics.shapes import Circle, Drawing, Line, Rect, String
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    CondPageBreak,
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)
from reportlab.platypus.tableofcontents import TableOfContents

from validate_v2_export import (
    V2_VARIANT,
    extract_v2_workbook_markdown,
    validate_pdf,
    validate_v2_markdown_text,
    validate_v2_paths,
)


PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 1.65 * cm
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN

NAVY = HexColor("#17233C")
BLUE = HexColor("#245B91")
TEAL = HexColor("#168373")
AMBER = HexColor("#D28B21")
RED = HexColor("#B84348")
GREEN = HexColor("#24815D")
TEXT = HexColor("#26364A")
SUBTEXT = HexColor("#5F6F82")
BORDER = HexColor("#D7DEE8")
LIGHT = HexColor("#F6F8FB")
BLUE_BG = HexColor("#EDF5FC")
AMBER_BG = HexColor("#FFF7E5")
GREEN_BG = HexColor("#EDF8F2")
RED_BG = HexColor("#FFF2F1")
CYAN = HexColor("#00A9C6")

FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"
MONO_FONT = "Courier"

RENDERER_NAME = "tools/markdown_learning_pdf.py"
RENDERER_VERSION = "2.5"
LEGACY_VARIANT = "legacy-v1"

for regular, bold, italic in (
    (
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\arialbd.ttf"),
        Path(r"C:\Windows\Fonts\ariali.ttf"),
    ),
    (
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"),
    ),
):
    if all(path.exists() for path in (regular, bold, italic)):
        pdfmetrics.registerFont(TTFont("LearningSans", str(regular)))
        pdfmetrics.registerFont(TTFont("LearningSans-Bold", str(bold)))
        pdfmetrics.registerFont(TTFont("LearningSans-Italic", str(italic)))
        pdfmetrics.registerFontFamily(
            "LearningSans",
            normal="LearningSans",
            bold="LearningSans-Bold",
            italic="LearningSans-Italic",
            boldItalic="LearningSans-Bold",
        )
        FONT = "LearningSans"
        FONT_BOLD = "LearningSans-Bold"
        FONT_ITALIC = "LearningSans-Italic"
        break

for mono in (
    Path(r"C:\Windows\Fonts\consola.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
):
    if mono.exists():
        pdfmetrics.registerFont(TTFont("LearningMono", str(mono)))
        MONO_FONT = "LearningMono"
        break


def style(name: str, **overrides) -> ParagraphStyle:
    values = {
        "fontName": FONT,
        "fontSize": 9.4,
        "leading": 14.2,
        "textColor": TEXT,
        "spaceAfter": 5,
    }
    values.update(overrides)
    return ParagraphStyle(name, **values)


STYLES = {
    "body": style("body"),
    "mcq_stem": style("mcq_stem", keepWithNext=True),
    "cover_title": style(
        "cover_title", fontName=FONT_BOLD, fontSize=24, leading=29,
        textColor=white, alignment=TA_LEFT, spaceAfter=0,
    ),
    "cover_subtitle": style(
        "cover_subtitle", fontName=FONT_BOLD, fontSize=11, leading=15,
        textColor=AMBER, alignment=TA_LEFT,
    ),
    "h1": style(
        "h1", fontName=FONT_BOLD, fontSize=17, leading=21,
        textColor=white, backColor=NAVY, borderPadding=10,
        spaceBefore=7, spaceAfter=10, keepWithNext=True,
    ),
    "h2": style(
        "h2", fontName=FONT_BOLD, fontSize=13, leading=17,
        textColor=BLUE, spaceBefore=10, spaceAfter=6, keepWithNext=False,
    ),
    "h3": style(
        "h3", fontName=FONT_BOLD, fontSize=10.6, leading=14,
        textColor=TEAL, spaceBefore=7, spaceAfter=4, keepWithNext=False,
    ),
    "session": style(
        "session", fontName=FONT_BOLD, fontSize=15, leading=19,
        textColor=white, backColor=BLUE, borderColor=NAVY,
        borderWidth=0.8, borderPadding=9,
        spaceBefore=11, spaceAfter=8, keepWithNext=True,
    ),
    "h4": style(
        "h4", fontName=FONT_BOLD, fontSize=9.6, leading=13,
        textColor=AMBER, spaceBefore=6, spaceAfter=3, keepWithNext=True,
    ),
    "bullet": style(
        "bullet", leftIndent=15, firstLineIndent=-8, bulletIndent=5,
        spaceAfter=3,
    ),
    "answer": style(
        "answer", fontName=FONT_BOLD, textColor=GREEN, backColor=GREEN_BG,
        borderColor=GREEN, borderWidth=0.7, borderPadding=6,
        spaceBefore=4, spaceAfter=5,
    ),
    "model": style(
        "model", fontName=FONT_BOLD, fontSize=10.2, textColor=NAVY,
        backColor=AMBER_BG, borderColor=AMBER, borderWidth=0.7,
        borderPadding=7, spaceBefore=6, spaceAfter=6,
    ),
    "caption": style(
        "caption", fontName=FONT_ITALIC, fontSize=7.6, leading=10,
        textColor=SUBTEXT, alignment=TA_CENTER,
    ),
    "footer": style(
        "footer", fontSize=7.2, leading=9, textColor=SUBTEXT,
        alignment=TA_CENTER,
    ),
    "contents_title": style(
        "contents_title", fontName=FONT_BOLD, fontSize=17, leading=21,
        textColor=white, backColor=NAVY, borderPadding=10,
        spaceAfter=8,
    ),
    "contents_intro": style(
        "contents_intro", fontSize=8.2, leading=11.5, textColor=SUBTEXT,
        spaceAfter=10,
    ),
}


INDEX_LEVEL_STYLES = [
    style(
        "contents-level-0",
        fontName=FONT_BOLD,
        fontSize=10.2,
        leading=13.2,
        leftIndent=0,
        rightIndent=28,
        firstLineIndent=0,
        textColor=NAVY,
        spaceBefore=3,
        spaceAfter=3,
    ),
    style(
        "contents-level-1",
        fontName=FONT_BOLD,
        fontSize=9.1,
        leading=12,
        leftIndent=13,
        rightIndent=28,
        firstLineIndent=-5,
        textColor=BLUE,
        spaceBefore=2,
        spaceAfter=2,
    ),
    style(
        "contents-level-2",
        fontSize=8.2,
        leading=10.8,
        leftIndent=27,
        rightIndent=28,
        firstLineIndent=-5,
        textColor=TEXT,
        spaceBefore=1,
        spaceAfter=1,
    ),
]

DENSE_INDEX_LEVEL_STYLES = [
    ParagraphStyle(
        f"dense-{base.name}",
        parent=base,
        spaceBefore=max(float(base.spaceBefore) - 0.25, 0),
        spaceAfter=max(float(base.spaceAfter) - 0.25, 0),
    )
    for base in INDEX_LEVEL_STYLES
]


NON_INDEX_SUBTOPIC = re.compile(
    r"^(?:"
    r"answer|answer key|explanation|solution|model answer|model solution|"
    r"question(?:\s+\d+)?|worked answer|examiner comment|why this works|"
    r"visual gateway|visual|diagram|example|exam link|upsc traps?|mini recap|"
    r"revision notes?|rapid recall|facts?|inferences?|source note|"
    r"current affairs anchor|pre-teach checklist"
    r")\s*:?\s*$",
    re.IGNORECASE,
)


class IndexedDocTemplate(SimpleDocTemplate):
    """Simple document template that records heading destinations for TOC and outline."""

    def __init__(self, *args, enable_internal_index: bool = False, **kwargs):
        self.enable_internal_index = enable_internal_index
        self._last_outline_level = -1
        self.visual_audit_positions: dict[str, dict[str, dict[str, float | int]]] = {}
        super().__init__(*args, **kwargs)

    def beforeDocument(self) -> None:
        super().beforeDocument()
        self._last_outline_level = -1
        self.visual_audit_positions = {}

    def afterFlowable(self, flowable) -> None:
        visual_id = getattr(flowable, "_visual_audit_id", None)
        visual_edge = getattr(flowable, "_visual_audit_edge", None)
        if visual_id and visual_edge:
            frame_y = float(getattr(getattr(self, "frame", None), "_y", 0.0))
            self.visual_audit_positions.setdefault(visual_id, {})[visual_edge] = {
                "page": int(self.page),
                "frame_y": round(frame_y, 3),
            }
        if not self.enable_internal_index:
            return
        level = getattr(flowable, "_index_level", None)
        if level is None:
            return
        # ReportLab outlines cannot skip a hierarchy level. Markdown front matter
        # may legitimately place an H3 callout before the first H2, so clamp only
        # the bookmark/TOC hierarchy while preserving the rendered heading style.
        level = min(level, self._last_outline_level + 1)
        self._last_outline_level = level
        text = getattr(flowable, "_index_text")
        outline_title = getattr(flowable, "_outline_title")
        key = getattr(flowable, "_bookmark_key")
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(outline_title, key, level=level, closed=False)
        self.notify("TOCEntry", (level, text, self.page, key))


class VisualAuditMarker(Flowable):
    """Zero-height marker used to map authored visual blocks to rendered pages."""

    def __init__(self, visual_id: str, edge: str):
        super().__init__()
        self.width = 0
        self.height = 0
        self._visual_audit_id = visual_id
        self._visual_audit_edge = edge

    def wrap(self, avail_width, avail_height):
        return 0, 0

    def draw(self):
        return None

    def getKeepWithNext(self):
        return 0


TOKEN_REPLACEMENTS = {
    "✅": "FACT:",
    "⚠️": "ANALYSIS:",
    "⚠": "ANALYSIS:",
    "📰": "CURRENT:",
    "📚": "BOOK:",
    "🔍": "SEARCH:",
    "🖼️": "VISUAL:",
    "🖼": "VISUAL:",
    "🔗": "LINK:",
    "❓": "CAUTION:",
    "❌": "WRONG:",
    "🔑": "MEMORY:",
    "━": "-",
    "─": "-",
    "—": "-",
    "–": "-",
    "‑": "-",
    "│": "|",
    "├": "+",
    "└": "+",
    "→": "->",
    "←": "<-",
    "↔": "<->",
    "⇒": "=>",
    "₹": "Rs ",
}


def plain(text: str) -> str:
    for source, replacement in TOKEN_REPLACEMENTS.items():
        text = text.replace(source, replacement)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[*_`]", "", text).strip()


def inline(text: str) -> str:
    answer_label = "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM"
    if answer_label in text:
        text = text.replace("—", "@@EXACT_EM_DASH@@")
        text = text.replace("–", "@@EXACT_EN_DASH@@")
    for source, replacement in TOKEN_REPLACEMENTS.items():
        text = text.replace(source, replacement)
    text = text.replace("@@EXACT_EM_DASH@@", "—")
    text = text.replace("@@EXACT_EN_DASH@@", "–")
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # ReportLab does not accept crossing bold/italic tags produced by Markdown
    # such as **term *gloss***. Keep the bold emphasis and flatten the nested
    # italics before converting markers to XML-like tags.
    text = re.sub(
        r"\*\*([^\n]+?)\*\*",
        lambda match: f"**{match.group(1).replace('*', '')}**",
        text,
    )
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    return text


def paragraph(text: str, paragraph_style: ParagraphStyle | None = None) -> Paragraph:
    return Paragraph(inline(text), paragraph_style or STYLES["body"])


def split_frontmatter(markdown: str) -> tuple[dict[str, str], str]:
    if not markdown.startswith("---\n"):
        return {}, markdown
    end = markdown.find("\n---\n", 4)
    if end < 0:
        return {}, markdown
    block = markdown[4:end]
    body = markdown[end + 5:]
    metadata: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip().strip("\"'")
        if key and value:
            metadata[key] = value
    return metadata, body


def is_table_separator(line: str) -> bool:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def parse_table(lines: list[str], start: int) -> tuple[Table | None, int]:
    block: list[str] = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        block.append(lines[index].strip())
        index += 1
    if len(block) < 2 or not is_table_separator(block[1]):
        return None, start + 1

    raw_rows = [
        [cell.strip() for cell in row.strip("|").split("|")]
        for row in [block[0], *block[2:]]
    ]
    width = max(len(row) for row in raw_rows)
    raw_rows = [(row + [""] * width)[:width] for row in raw_rows]
    data = []
    for row_number, row in enumerate(raw_rows):
        table_font_size = 7.8 if width >= 4 else 8.3
        row_style = style(
            f"table-{row_number}",
            fontName=FONT_BOLD if row_number == 0 else FONT,
            fontSize=table_font_size,
            leading=10.5 if width >= 4 else 11.2,
            textColor=white if row_number == 0 else TEXT,
            spaceAfter=0,
            wordWrap="LTR",
        )
        data.append(
            [
                paragraph(
                    cell.replace("\\", "\\\u200b")
                    .replace("/", "/\u200b")
                    .replace("-", "-\u200b")
                    .replace("_", "_\u200b"),
                    row_style,
                )
                for cell in row
            ]
        )

    minimum_widths = []
    desired_widths = []
    for column in range(width):
        cells = [plain(row[column]) for row in raw_rows]
        word_widths = [
            max(
                pdfmetrics.stringWidth(word, FONT, table_font_size),
                pdfmetrics.stringWidth(word, FONT_BOLD, table_font_size),
            )
            for cell in cells
            for word in re.findall(r"[^\s/\\_-]+", cell)
        ]
        line_widths = [
            max(
                pdfmetrics.stringWidth(cell, FONT, table_font_size),
                pdfmetrics.stringWidth(cell, FONT_BOLD, table_font_size),
            )
            for cell in cells
        ]
        minimum_widths.append(max([24.0, *(width + 13 for width in word_widths)]))
        desired_widths.append(
            max(
                minimum_widths[-1],
                min(max(line_widths, default=0) + 13, 170.0),
            )
        )
    minimum_total = sum(minimum_widths)
    if minimum_total > USABLE_WIDTH + 0.1:
        raise ValueError(
            "Markdown table needs a semantic split because its unbreakable "
            f"column minima require {minimum_total:.1f}pt but only "
            f"{USABLE_WIDTH:.1f}pt are available: {raw_rows[0]}"
        )
    remaining = USABLE_WIDTH - minimum_total
    expansion = [
        max(0.0, desired - minimum)
        for desired, minimum in zip(desired_widths, minimum_widths)
    ]
    expansion_total = sum(expansion)
    col_widths = [
        minimum
        + (
            remaining * extra / expansion_total
            if expansion_total
            else remaining / width
        )
        for minimum, extra in zip(minimum_widths, expansion)
    ]
    table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table, index


def callout(text: str) -> Table:
    upper = plain(text).upper()
    if upper.startswith("WRONG:"):
        color, background = RED, RED_BG
    elif upper.startswith(("FACT:", "MEMORY:")):
        color, background = GREEN, GREEN_BG
    elif upper.startswith(("ANALYSIS:", "CURRENT:")):
        color, background = AMBER, AMBER_BG
    else:
        color, background = BLUE, BLUE_BG
    body = Table(
        [[paragraph(text)]],
        colWidths=[USABLE_WIDTH],
        hAlign="LEFT",
    )
    body.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("LINEBEFORE", (0, 0), (0, -1), 3, color),
        ("LINEABOVE", (0, 0), (-1, 0), 0.35, BORDER),
        ("LINEBELOW", (0, -1), (-1, -1), 0.35, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return body


CLOSURE_FIELD_ORDER = (
    ("KEY TERMS / DEFINITIONS", "terms", BLUE, BLUE_BG),
    ("MECHANISM / ARGUMENT", "mechanism", TEAL, GREEN_BG),
    ("CONSEQUENCE / CONTRAST", "consequence", AMBER, AMBER_BG),
    ("UPSC TRAP / ANSWER-USE", "trap", RED, RED_BG),
)


def parse_closure_flow(lines: list[str]) -> tuple[str, dict[str, str]]:
    """Parse the repository's explicit, source-derived closure-flow fence."""
    fields = {
        "terms": "",
        "mechanism": "",
        "consequence": "",
        "trap": "",
        "answer": "",
    }
    title = "SUBTOPIC CLOSURE FLOW"
    labels = {
        "SUBTOPIC": "title",
        "KEY TERMS / DEFINITIONS": "terms",
        "EXACT TERMS": "terms",
        "MECHANISM / ARGUMENT": "mechanism",
        "CONSEQUENCE / CONTRAST": "consequence",
        "UPSC TRAP / ANSWER-USE": "trap",
        "ANSWER-GRABBING FORMULATION": "answer",
    }
    for raw_line in lines:
        if ":" not in raw_line:
            continue
        label, value = raw_line.split(":", 1)
        destination = labels.get(label.strip().upper())
        if not destination:
            continue
        if destination == "title":
            title = value.strip() or title
        else:
            fields[destination] = value.strip()
    missing = [key for _, key, _, _ in CLOSURE_FIELD_ORDER if not fields[key]]
    if missing or not fields["answer"]:
        raise ValueError(
            "Closure flow is missing required source-derived fields: "
            + ", ".join([*missing, *([] if fields["answer"] else ["answer"])])
        )
    return title, fields


def closure_flow(title: str, fields: dict[str, str]) -> list:
    """Render a compact left-to-right closure diagram at a subtopic's actual end."""
    header = Table(
        [[
            paragraph(
                f"SUBTOPIC CLOSURE FLOW  |  {title}",
                style(
                    "closure-title",
                    fontName=FONT_BOLD,
                    fontSize=8.8,
                    leading=11.3,
                    textColor=white,
                    spaceAfter=0,
                ),
            )
        ]],
        colWidths=[USABLE_WIDTH],
        hAlign="LEFT",
    )
    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LINEBEFORE", (0, 0), (0, -1), 5, CYAN),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    cells = []
    for sequence, (label, field, color, _) in enumerate(CLOSURE_FIELD_ORDER, 1):
        cells.append([
            Paragraph(
                f'<font color="{color.hexval()}"><b>{sequence}. {inline(label)}</b></font>'
                f"<br/>{inline(fields[field])}",
                style(
                    f"closure-{field}",
                    fontSize=6.65,
                    leading=8.35,
                    textColor=TEXT,
                    spaceAfter=0,
                ),
            )
        ])
    body = Table(
        [[cell[0] for cell in cells]],
        colWidths=[USABLE_WIDTH / 4] * 4,
        hAlign="LEFT",
    )
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    for column, (_, _, color, background) in enumerate(CLOSURE_FIELD_ORDER):
        commands.extend([
            ("BACKGROUND", (column, 0), (column, 0), background),
            ("LINEABOVE", (column, 0), (column, 0), 3, color),
        ])
    body.setStyle(TableStyle(commands))
    answer = Table(
        [[
            paragraph(
                "**ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM:** "
                + fields["answer"],
                style(
                    "closure-answer",
                    fontName=FONT_BOLD,
                    fontSize=7.4,
                    leading=9.5,
                    textColor=GREEN,
                    spaceAfter=0,
                ),
            )
        ]],
        colWidths=[USABLE_WIDTH],
        hAlign="LEFT",
    )
    answer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_BG),
        ("BOX", (0, 0), (-1, -1), 0.65, GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    # Keep the answer strip with its subtopic, but allow the dense four-column
    # body to split before it instead of creating an oversized unbreakable block.
    return [header, body, KeepTogether([answer, Spacer(1, 0.14 * cm)])]


def economy_identity_visual() -> Drawing:
    drawing = Drawing(USABLE_WIDTH, 210)
    center_x, center_y = USABLE_WIDTH / 2, 108
    drawing.add(Circle(center_x, center_y, 49, fillColor=NAVY, strokeColor=AMBER, strokeWidth=2))
    drawing.add(String(
        center_x, center_y + 8, "NATIONAL",
        fontName=FONT_BOLD, fontSize=10, fillColor=white, textAnchor="middle",
    ))
    drawing.add(String(
        center_x, center_y - 8, "INCOME",
        fontName=FONT_BOLD, fontSize=10, fillColor=white, textAnchor="middle",
    ))
    nodes = [
        ("PRODUCTION", "GVA -> GDP", 20, 140, BLUE),
        ("INCOME", "Wages + surplus", USABLE_WIDTH - 170, 140, TEAL),
        ("EXPENDITURE", "C + I + G + NX", 20, 28, AMBER),
        ("WELFARE TEST", "Jobs + equity + ecology", USABLE_WIDTH - 170, 28, RED),
    ]
    for title, detail, x, y, color in nodes:
        drawing.add(Line(center_x, center_y, x + 75, y + 28, strokeColor=BORDER, strokeWidth=1.2))
        drawing.add(Rect(x, y, 150, 56, rx=8, ry=8, fillColor=LIGHT, strokeColor=BORDER))
        drawing.add(Rect(x, y + 49, 150, 7, rx=8, ry=8, fillColor=color, strokeColor=color))
        drawing.add(String(
            x + 75, y + 31, title, fontName=FONT_BOLD, fontSize=8.2,
            fillColor=color, textAnchor="middle",
        ))
        drawing.add(String(
            x + 75, y + 15, detail, fontName=FONT, fontSize=7.4,
            fillColor=TEXT, textAnchor="middle",
        ))
    return drawing


def learning_path_visual() -> Drawing:
    drawing = Drawing(USABLE_WIDTH, 155)
    drawing.add(String(
        USABLE_WIDTH / 2,
        137,
        "LEARNING PATH",
        fontName=FONT_BOLD,
        fontSize=10,
        fillColor=NAVY,
        textAnchor="middle",
    ))
    nodes = [
        ("CONCEPT", "Define precisely", BLUE),
        ("ARGUMENT", "Build the case", TEAL),
        ("CRITIQUE", "Test the limits", RED),
        ("APPLICATION", "Write the answer", AMBER),
    ]
    node_width = 112
    node_height = 64
    gap = (USABLE_WIDTH - node_width * len(nodes)) / (len(nodes) - 1)
    y = 42
    for index, (title, detail, color) in enumerate(nodes):
        x = index * (node_width + gap)
        if index:
            previous_right = x - gap
            drawing.add(Line(
                previous_right,
                y + node_height / 2,
                x,
                y + node_height / 2,
                strokeColor=BORDER,
                strokeWidth=1.5,
            ))
        drawing.add(Rect(
            x,
            y,
            node_width,
            node_height,
            rx=8,
            ry=8,
            fillColor=LIGHT,
            strokeColor=BORDER,
        ))
        drawing.add(Rect(
            x,
            y + node_height - 8,
            node_width,
            8,
            rx=8,
            ry=8,
            fillColor=color,
            strokeColor=color,
        ))
        drawing.add(String(
            x + node_width / 2,
            y + 35,
            title,
            fontName=FONT_BOLD,
            fontSize=8,
            fillColor=color,
            textAnchor="middle",
        ))
        drawing.add(String(
            x + node_width / 2,
            y + 18,
            detail,
            fontName=FONT,
            fontSize=7.2,
            fillColor=TEXT,
            textAnchor="middle",
        ))
    return drawing


def cover_story(title: str, mode: str, image_path: Path | None) -> list:
    subtitle = (
        "COMPLETE LEARNING SESSION"
        if mode == "main"
        else "SOLVED PRACTICE WORKBOOK"
    )
    title_box = Table(
        [[
            [
                paragraph(subtitle, STYLES["cover_subtitle"]),
                Spacer(1, 0.2 * cm),
                paragraph(title, STYLES["cover_title"]),
            ]
        ]],
        colWidths=[USABLE_WIDTH],
    )
    title_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LINEBEFORE", (0, 0), (0, 0), 7, AMBER),
        ("LEFTPADDING", (0, 0), (-1, -1), 22),
        ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ("TOPPADDING", (0, 0), (-1, -1), 26),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 26),
    ]))
    story = [
        Spacer(1, 1.1 * cm),
        title_box,
        Spacer(1, 0.4 * cm),
        paragraph(
            "UPSC complete learning session | Foundation to advanced | "
            "Concepts, evidence, practice and answer writing",
            style("cover-meta", fontSize=9, textColor=SUBTEXT, alignment=TA_CENTER),
        ),
        Spacer(1, 0.35 * cm),
    ]
    if image_path:
        image = Image(str(image_path))
        image._restrictSize(USABLE_WIDTH, 10.5 * cm)
        image.hAlign = "CENTER"
        story.extend([
            image,
            Spacer(1, 0.1 * cm),
            paragraph(
                "Original deterministic study visual; labels are explanatory, not textual quotations.",
                STYLES["caption"],
            ),
        ])
    else:
        story.extend([
            learning_path_visual(),
            paragraph(
                "Deterministic fallback visual: move from precise concepts through "
                "argument and critique to exam application.",
                STYLES["caption"],
            ),
        ])
    story.extend([
        Spacer(1, 0.35 * cm),
        HRFlowable(width="35%", thickness=3, color=AMBER, hAlign="LEFT"),
        Spacer(1, 0.12 * cm),
        paragraph(
            "Source order: repository knowledge -> official current linkage -> "
            "clearly marked analysis. No fabricated PYQs or statistics.",
            STYLES["footer"],
        ),
        PageBreak(),
    ])
    return story


def should_index_heading(level: int, text: str) -> bool:
    """Keep major parts and meaningful subtopics, not every utility heading."""
    if level <= 2:
        return True
    if level == 3:
        return not NON_INDEX_SUBTOPIC.fullmatch(plain(text))
    return False


def indexed_heading_count(markdown: str) -> int:
    return sum(
        1
        for line in markdown.splitlines()
        if (
            (match := re.match(r"^(#{1,3})\s+(.+?)\s*$", line))
            and should_index_heading(len(match.group(1)), match.group(2))
        )
    )


def contents_story(mode: str, entry_count: int) -> list:
    title = (
        "CONTENTS / SESSION INDEX"
        if mode == "main"
        else "CONTENTS / WORKBOOK INDEX"
    )
    description = (
        "Major learning parts and meaningful subtopics are listed in document order. "
        "Page numbers are generated from the final PDF layout; PDF bookmarks mirror "
        "the same hierarchy."
    )
    toc = TableOfContents()
    toc.levelStyles = (
        DENSE_INDEX_LEVEL_STYLES
        if entry_count >= 90
        else INDEX_LEVEL_STYLES
    )
    toc.dotsMinLevel = 0
    return [
        paragraph(title, STYLES["contents_title"]),
        paragraph(description, STYLES["contents_intro"]),
        toc,
        PageBreak(),
    ]


def select_markdown(
    markdown: str,
    mode: str,
    variant: str = LEGACY_VARIANT,
) -> str:
    if mode == "main":
        return markdown
    if variant == V2_VARIANT:
        return extract_v2_workbook_markdown(markdown)

    start_match = re.search(
        r"^##\s+.*(?:PYQ|previous-year|practice|workbook).*$",
        markdown,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if not start_match:
        start_match = re.search(
            r"^##\s+PART III.*$",
            markdown,
            flags=re.MULTILINE | re.IGNORECASE,
        )
    if not start_match:
        return markdown

    practice = markdown[start_match.start() :]
    end_match = re.search(
        r"^##\s+.*(?:consolidated|final).*register notes.*$",
        practice,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    if end_match:
        practice = practice[: end_match.start()]
    title = markdown.splitlines()[0]
    return f"{title}\n\n{practice}"


def markdown_story(
    markdown: str,
    source_dir: Path,
    *,
    internal_index: bool = False,
    visual_audit_records: list[dict[str, object]] | None = None,
) -> list:
    lines = markdown.replace("\r\n", "\n").splitlines()
    story: list = []
    paragraph_lines: list[str] = []
    index = 0
    first_h1 = True
    indexed_heading_number = 0
    visual_number = 0
    current_heading = ""
    pending_heading_for_heading = None
    pending_heading_for_table = None

    def begin_visual(
        kind: str,
        start_index: int,
        end_index: int,
        *,
        preview: str,
        metadata: dict[str, object] | None = None,
        append_marker: bool = True,
    ) -> str | None:
        nonlocal visual_number
        if visual_audit_records is None:
            return None
        visual_number += 1
        visual_id = f"visual-{visual_number:04d}"
        visual_audit_records.append(
            {
                "visual_id": visual_id,
                "kind": kind,
                "markdown_body_line_start": start_index + 1,
                "markdown_body_line_end": end_index + 1,
                "heading": current_heading,
                "preview": preview[:240],
                "metadata": metadata or {},
            }
        )
        if append_marker:
            story.append(VisualAuditMarker(visual_id, "start"))
        return visual_id

    def end_visual(visual_id: str | None) -> None:
        if visual_id:
            story.append(VisualAuditMarker(visual_id, "end"))

    def pop_keep_with_next_chain() -> list:
        chain: list = []
        while story and story[-1].getKeepWithNext():
            chain.insert(0, story.pop())
        return chain

    def flush_paragraph() -> None:
        if paragraph_lines:
            text = " ".join(line.strip() for line in paragraph_lines)
            if text.startswith("**Answer:"):
                story.append(paragraph(text, STYLES["answer"]))
            elif text == "**Model solution**":
                story.append(paragraph(text, STYLES["model"]))
            elif (
                re.match(r"^MCQ\s+\d+\b", current_heading, re.IGNORECASE)
                and not re.match(r"^(?:[A-D]\.|[*]{2}Explanation:)", text)
            ):
                story.append(paragraph(text, STYLES["mcq_stem"]))
            else:
                body_paragraph = paragraph(text)
                if text.startswith(("**Conclusion:**", "**Verdict.**", "**Verdict:**")):
                    body_paragraph.keepWithNext = 1
                story.append(body_paragraph)
            paragraph_lines.clear()

    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()

        if stripped.startswith("<!--"):
            flush_paragraph()
            while index < len(lines) and "-->" not in lines[index]:
                index += 1
            index += 1
            continue

        if stripped.lower().startswith("```closure-flow"):
            flush_paragraph()
            visual_start = index
            closure_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                closure_lines.append(lines[index].rstrip())
                index += 1
            title, fields = parse_closure_flow(closure_lines)
            visual_id = begin_visual(
                "closure-flow",
                visual_start,
                index,
                preview=title,
                metadata={"field_count": len(fields)},
            )
            story.extend(closure_flow(title, fields))
            end_visual(visual_id)
            index += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            visual_start = index
            fence_language = stripped[3:].strip().lower()
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index].rstrip())
                index += 1
            code_text = "\n".join(code_lines)
            is_ascii_master = fence_language == "ascii-master"
            if not is_ascii_master:
                for source, replacement in TOKEN_REPLACEMENTS.items():
                    code_text = code_text.replace(source, replacement)
            code = Preformatted(
                code_text,
                style(
                    f"code-{index}", fontName=MONO_FONT,
                    fontSize=8.2 if is_ascii_master else 7.5,
                    leading=10.2 if is_ascii_master else 10,
                    textColor=NAVY, backColor=LIGHT,
                    borderColor=BORDER, borderWidth=0.6, borderPadding=8,
                    spaceBefore=4, spaceAfter=7,
                ),
                maxLineLength=110 if is_ascii_master else 100,
            )
            visual_id = begin_visual(
                "fenced-preformatted",
                visual_start,
                index,
                preview=next((line.strip() for line in code_lines if line.strip()), ""),
                metadata={
                    "language": fence_language or "plain",
                    "line_count": len(code_lines),
                    "max_source_line_length": max(
                        (len(line) for line in code_lines),
                        default=0,
                    ),
                },
                append_marker=False,
            )
            code_block = (
                [
                    VisualAuditMarker(visual_id, "start"),
                    code,
                    VisualAuditMarker(visual_id, "end"),
                ]
                if visual_id
                else [code]
            )
            if story and (
                getattr(story[-1], "_keep_with_code_block", False)
                or story[-1].getKeepWithNext()
            ):
                code_block[0:0] = pop_keep_with_next_chain()
            leading = 10.2 if is_ascii_master else 10
            required_height = min(
                22.0 * cm,
                max(4.0 * cm, (len(code_lines) + 3) * leading + 24),
            )
            story.append(CondPageBreak(required_height))
            story.append(
                KeepTogether(code_block) if len(code_block) > 1 else code
            )
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", stripped)
        if heading:
            flush_paragraph()
            source_level = len(heading.group(1))
            level = min(source_level, 4)
            text = plain(heading.group(2))
            current_heading = text
            if level == 4 and text.startswith("ASCII MASTER FLOW - PANEL"):
                story.append(CondPageBreak(10.0 * cm))
            if level == 1:
                if not first_h1:
                    story.append(CondPageBreak(8.5 * cm))
                first_h1 = False
            elif level == 2:
                story.append(CondPageBreak(5.0 * cm))
            elif level == 3 and re.match(
                r"^ASCII PANEL\s+\d+/\d+\b",
                text,
                re.IGNORECASE,
            ):
                story.append(CondPageBreak(12.0 * cm))
            elif level == 4 and re.match(
                r"^ASCII PANEL\s+\d+/\d+\b",
                text,
                re.IGNORECASE,
            ):
                story.append(CondPageBreak(13.0 * cm))
            elif level == 3:
                story.append(CondPageBreak(5.0 * cm))
            elif level == 4 and re.match(r"^MCQ\s+\d+\b", text, re.IGNORECASE):
                # Keep the stem, four options, answer and explanation on one page
                # for the normal workbook-sized question blocks.
                story.append(CondPageBreak(10.5 * cm))
            elif level == 4 and re.match(
                r"^(?:Solved\s+)?PYQ\s+\d+\b|^Original Mains",
                text,
                re.IGNORECASE,
            ):
                # Avoid leaving a question orphaned at the foot of a page before
                # its model answer begins.
                story.append(CondPageBreak(12.0 * cm))
            elif level == 4 and re.match(
                r"^(?:VISUAL\b|Visual gateway\b)",
                text,
                re.IGNORECASE,
            ):
                story.append(CondPageBreak(10.0 * cm))
            elif level == 4 and re.match(
                r"^ASCII MASTER FLOW\s*[-—]\s*PANEL\b",
                text,
                re.IGNORECASE,
            ):
                story.append(CondPageBreak(4.2 * cm))
            heading_style = (
                STYLES["session"]
                if level == 3 and re.match(r"^SESSION\s+\d+\b", text, re.IGNORECASE)
                else STYLES[f"h{level}"]
            )
            heading_paragraph = paragraph(text, heading_style)
            if level == 4 and re.match(
                r"^ASCII PANEL\s+\d+/\d+\b",
                text,
                re.IGNORECASE,
            ):
                heading_paragraph._keep_with_code_block = True
            if internal_index and should_index_heading(level, text):
                indexed_heading_number += 1
                heading_paragraph._index_level = level - 1
                heading_paragraph._index_text = html.escape(text, quote=False)
                heading_paragraph._outline_title = text
                heading_paragraph._bookmark_key = (
                    f"learning-heading-{indexed_heading_number:04d}"
                )
            if pending_heading_for_heading is not None:
                story.append(
                    KeepTogether(
                        [pending_heading_for_heading, heading_paragraph]
                    )
                )
                pending_heading_for_heading = None
            elif text in {
                "BASIC MCQS / REMEDIATION",
                "ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS",
            }:
                pending_heading_for_heading = heading_paragraph
            elif (
                text.startswith("21.6 Populism vs popular/participatory democracy")
                or text == "ONE-PAGE CONCEPT GRID"
            ):
                pending_heading_for_table = heading_paragraph
            else:
                story.append(heading_paragraph)
            index += 1
            continue

        image_match = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", stripped)
        if image_match:
            flush_paragraph()
            visual_start = index
            caption, raw_path = image_match.groups()
            image_path = Path(raw_path.strip())
            if not image_path.is_absolute():
                source_relative = (source_dir / image_path).resolve()
                cwd_relative = image_path.resolve()
                image_path = source_relative if source_relative.is_file() else cwd_relative
            if not image_path.is_file():
                raise FileNotFoundError(image_path)
            image = Image(str(image_path))
            image._restrictSize(USABLE_WIDTH, 10.2 * cm)
            image.hAlign = "CENTER"
            story.append(CondPageBreak(4.0 * cm))
            visual_id = begin_visual(
                "embedded-image",
                visual_start,
                visual_start,
                preview=caption or image_path.name,
                metadata={"image_path": str(image_path)},
            )
            story.append(image)
            if caption:
                story.append(paragraph(caption, STYLES["caption"]))
            story.append(Spacer(1, 0.12 * cm))
            end_visual(visual_id)
            index += 1
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            visual_start = index
            table, next_index = parse_table(lines, index)
            if table:
                header_cells = [
                    cell.strip()
                    for cell in lines[index].strip().strip("|").split("|")
                ]
                _, estimated_table_height = table.wrap(USABLE_WIDTH, A4[1])
                visual_id = begin_visual(
                    "markdown-table",
                    visual_start,
                    next_index - 1,
                    preview=" | ".join(header_cells),
                    metadata={
                        "column_count": len(header_cells),
                        "row_count": max(0, next_index - index - 2),
                        "headers": header_cells,
                    },
                    append_marker=False,
                )
                table_block = [table, Spacer(1, 0.12 * cm)]
                heading_chain = (
                    pop_keep_with_next_chain()
                    if (
                        pending_heading_for_table is None
                        and story
                        and story[-1].getKeepWithNext()
                        and estimated_table_height <= 24.0 * cm
                    )
                    else []
                )
                if pending_heading_for_table is not None:
                    grouped_table = [pending_heading_for_table]
                    pending_heading_for_table = None
                    if visual_id:
                        grouped_table.append(
                            VisualAuditMarker(visual_id, "start")
                        )
                    grouped_table.extend(table_block)
                    if visual_id:
                        grouped_table.append(
                            VisualAuditMarker(visual_id, "end")
                        )
                    story.append(KeepTogether(grouped_table))
                elif heading_chain:
                    grouped_table = heading_chain
                    if visual_id:
                        grouped_table.append(
                            VisualAuditMarker(visual_id, "start")
                        )
                    grouped_table.extend(table_block)
                    if visual_id:
                        grouped_table.append(
                            VisualAuditMarker(visual_id, "end")
                        )
                    story.append(KeepTogether(grouped_table))
                elif visual_id and estimated_table_height <= 24.0 * cm:
                    story.append(
                        KeepTogether(
                            [
                                VisualAuditMarker(visual_id, "start"),
                                *table_block,
                                VisualAuditMarker(visual_id, "end"),
                            ]
                        )
                    )
                else:
                    if visual_id:
                        story.append(VisualAuditMarker(visual_id, "start"))
                    story.extend(table_block)
                    end_visual(visual_id)
                index = next_index
                continue

        if stripped.startswith(">"):
            flush_paragraph()
            visual_start = index
            quote_lines = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(re.sub(r"^>\s?", "", lines[index].strip()))
                index += 1
            quote_text = " ".join(quote_lines)
            visual_id = begin_visual(
                "recall-callout",
                visual_start,
                index - 1,
                preview=quote_text,
                metadata={"line_count": len(quote_lines)},
                append_marker=False,
            )
            callout_block = [callout(quote_text), Spacer(1, 0.08 * cm)]
            if story and story[-1].getKeepWithNext():
                callout_block.insert(0, story.pop())
            if visual_id:
                story.append(
                    KeepTogether(
                        [
                            VisualAuditMarker(visual_id, "start"),
                            *callout_block,
                            VisualAuditMarker(visual_id, "end"),
                        ]
                    )
                )
            else:
                story.append(KeepTogether(callout_block))
            continue

        bullet = re.match(r"^[-+*]\s+(.+)$", stripped)
        ordered = re.match(r"^(\d+)[.)]\s+(.+)$", stripped)
        if bullet or ordered:
            flush_paragraph()
            marker = "-" if bullet else f"{ordered.group(1)}."
            text = bullet.group(1) if bullet else ordered.group(2)
            story.append(Paragraph(
                inline(text),
                STYLES["bullet"],
                bulletText=marker,
            ))
            index += 1
            continue

        if not stripped or stripped == "---":
            flush_paragraph()
            if stripped == "---":
                story.append(HRFlowable(width="100%", thickness=0.5, color=BORDER))
            index += 1
            continue

        paragraph_lines.append(stripped)
        index += 1

    flush_paragraph()
    if pending_heading_for_heading is not None:
        story.append(pending_heading_for_heading)
    if pending_heading_for_table is not None:
        story.append(pending_heading_for_table)
    return story


def on_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_WIDTH, 0.62 * cm, fill=1, stroke=0)
    canvas.setFillColor(AMBER)
    canvas.rect(0, PAGE_HEIGHT - 0.13 * cm, PAGE_WIDTH, 0.13 * cm, fill=1, stroke=0)
    canvas.setFont(FONT, 7)
    canvas.setFillColor(white)
    canvas.drawString(MARGIN, 0.22 * cm, "UPSC Complete Learning Session")
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 0.22 * cm, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(
    source_path: str | Path,
    output_path: str | Path,
    *,
    mode: str = "main",
    image_path: str | Path | None = None,
    variant: str = LEGACY_VARIANT,
    topic_key: str | None = None,
    repository_root: str | Path | None = None,
    visual_audit_path: str | Path | None = None,
    standalone_workbook: bool = False,
) -> Path:
    source = Path(source_path)
    output = Path(output_path)
    if mode not in {"main", "workbook"}:
        raise ValueError("mode must be 'main' or 'workbook'.")
    if variant not in {LEGACY_VARIANT, V2_VARIANT}:
        raise ValueError(
            f"variant must be '{LEGACY_VARIANT}' or '{V2_VARIANT}'."
        )
    if not source.is_file():
        raise FileNotFoundError(source)
    if standalone_workbook and (mode != "workbook" or variant != V2_VARIANT):
        raise ValueError(
            "standalone_workbook requires mode='workbook' and variant='learner-v2'."
        )

    metadata, body = split_frontmatter(source.read_text(encoding="utf-8"))
    resolved_topic_key = topic_key or metadata.get("topic_key")
    root = (
        Path(repository_root).resolve()
        if repository_root
        else Path(__file__).resolve().parents[1]
    )
    if variant == V2_VARIANT:
        errors = [] if standalone_workbook else validate_v2_markdown_text(body)
        if standalone_workbook:
            if not re.search(
                r"(?im)^#\s+.+\bSolved Practice Workbook\b",
                body,
            ):
                errors.append(
                    "Standalone workbook Markdown needs a Solved Practice Workbook H1."
                )
            for heading in (
                "BASIC MCQS / REMEDIATION",
                "PYQS AND ANSWER PRACTICE",
            ):
                if not re.search(
                    rf"(?im)^##\s+{re.escape(heading)}\s*$",
                    body,
                ):
                    errors.append(
                        f"Standalone workbook Markdown is missing {heading}."
                    )
        if not resolved_topic_key:
            errors.append(
                "Learner-first v2 rendering requires --topic-key or topic_key frontmatter."
            )
        else:
            errors.extend(
                validate_v2_paths(
                    root,
                    source,
                    output,
                    resolved_topic_key,
                    mode,
                )
            )
        if errors:
            raise ValueError("V2 Markdown/path validation failed:\n- " + "\n- ".join(errors))

    markdown = body if standalone_workbook else select_markdown(body, mode, variant)
    heading = next(
        (
            line.strip()
            for line in markdown.splitlines()
            if re.match(r"^#\s+\S", line.strip())
        ),
        "",
    )
    title = plain(metadata.get("title") or heading.lstrip("# "))
    if mode == "workbook":
        title = re.sub(
            r"\s*[:-]\s*Complete Topic Package\s*$",
            " - Solved Practice Workbook",
            title,
            flags=re.IGNORECASE,
        )
    illustration = Path(image_path) if image_path else None
    if not illustration and metadata.get("cover_image"):
        illustration = Path(metadata["cover_image"])
        if not illustration.is_absolute():
            illustration = (source.parent / illustration).resolve()
    if illustration and not illustration.is_file():
        raise FileNotFoundError(illustration)

    output.parent.mkdir(parents=True, exist_ok=True)
    document = IndexedDocTemplate(
        str(output),
        enable_internal_index=variant == V2_VARIANT,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.15 * cm,
        bottomMargin=1.1 * cm,
        title=title,
        author="UPSC Agent / Copilot CLI",
        invariant=1 if variant == V2_VARIANT else None,
    )
    story = cover_story(title, mode, illustration)
    if variant == V2_VARIANT:
        story.extend(contents_story(mode, indexed_heading_count(markdown)))
    visual_audit_records: list[dict[str, object]] | None = (
        [] if visual_audit_path else None
    )
    story.extend(
        markdown_story(
            markdown,
            source.parent,
            internal_index=variant == V2_VARIANT,
            visual_audit_records=visual_audit_records,
        )
    )
    build_arguments = {
        "onFirstPage": on_page,
        "onLaterPages": on_page,
    }
    if variant == V2_VARIANT:
        document.multiBuild(
            story,
            maxPasses=10,
            canvasmaker=partial(Canvas, invariant=1),
            **build_arguments,
        )
    else:
        document.build(story, **build_arguments)
    if variant == V2_VARIANT:
        errors = validate_pdf(output, variant=variant, mode=mode)
        if errors:
            raise ValueError("Generated v2 PDF failed validation:\n- " + "\n- ".join(errors))
    if visual_audit_path and visual_audit_records is not None:
        audit_output = Path(visual_audit_path)
        audit_output.parent.mkdir(parents=True, exist_ok=True)
        for record in visual_audit_records:
            positions = document.visual_audit_positions.get(
                str(record["visual_id"]),
                {},
            )
            record["rendered_positions"] = positions
            start = positions.get("start", {})
            end = positions.get("end", start)
            start_page = int(start.get("page", 0))
            end_page = int(end.get("page", start_page))
            record["pdf_pages"] = (
                list(range(start_page, end_page + 1))
                if start_page and end_page >= start_page
                else []
            )
        audit_output.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "source": str(source.resolve()),
                    "output_pdf": str(output.resolve()),
                    "mode": mode,
                    "topic_key": resolved_topic_key,
                    "visual_blocks": visual_audit_records,
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return output.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render explanatory UPSC learning Markdown as PDF."
    )
    parser.add_argument("source")
    parser.add_argument("output")
    parser.add_argument("--mode", choices=("main", "workbook"), default="main")
    parser.add_argument("--image")
    parser.add_argument(
        "--variant",
        choices=(LEGACY_VARIANT, V2_VARIANT),
        default=LEGACY_VARIANT,
    )
    parser.add_argument("--topic-key")
    parser.add_argument("--repository-root")
    parser.add_argument("--visual-audit-map")
    parser.add_argument("--standalone-workbook", action="store_true")
    args = parser.parse_args()
    output = build_pdf(
        args.source,
        args.output,
        mode=args.mode,
        image_path=args.image,
        variant=args.variant,
        topic_key=args.topic_key,
        repository_root=args.repository_root,
        visual_audit_path=args.visual_audit_map,
        standalone_workbook=args.standalone_workbook,
    )
    print(f"PDF saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
