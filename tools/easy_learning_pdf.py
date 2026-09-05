"""Render calm, learner-first Markdown editions without changing legacy renderers.

Usage:
    python tools/easy_learning_pdf.py source.md output.pdf
    python tools/easy_learning_pdf.py source.md output.pdf --contact-dir output\validation
"""

from __future__ import annotations

import argparse
import html
import json
import math
from functools import partial
from pathlib import Path

import fitz
from PIL import Image as PILImage, ImageDraw
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Spacer,
    Table,
    TableStyle,
)

import markdown_learning_pdf as base


PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 1.95 * cm
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN

NAVY = HexColor("#18324A")
BLUE = HexColor("#2D6A9F")
TEAL = HexColor("#2B7A78")
GREEN = HexColor("#3B7D5B")
AMBER = HexColor("#C9852D")
RED = HexColor("#B85252")
TEXT = HexColor("#263847")
SUBTEXT = HexColor("#657684")
BORDER = HexColor("#D5DEE5")
LIGHT = HexColor("#F5F8FA")
BLUE_BG = HexColor("#EEF6FC")
TEAL_BG = HexColor("#EDF8F6")
GREEN_BG = HexColor("#EEF8F1")
AMBER_BG = HexColor("#FFF7E7")
RED_BG = HexColor("#FFF1F0")

_BASE_PARAGRAPH = base.paragraph
_BASE_PREFORMATTED = base.Preformatted


def style(name: str, **overrides) -> ParagraphStyle:
    values = {
        "fontName": base.FONT,
        "fontSize": 10.6,
        "leading": 16.0,
        "textColor": TEXT,
        "spaceAfter": 7,
    }
    values.update(overrides)
    return ParagraphStyle(name, **values)


STYLES = {
    "body": style("easy-body"),
    "cover_title": style(
        "easy-cover-title",
        fontName=base.FONT_BOLD,
        fontSize=25,
        leading=31,
        textColor=white,
        alignment=TA_LEFT,
        spaceAfter=0,
    ),
    "cover_subtitle": style(
        "easy-cover-subtitle",
        fontName=base.FONT_BOLD,
        fontSize=11.5,
        leading=16,
        textColor=HexColor("#FFD98C"),
        alignment=TA_LEFT,
    ),
    "h1": style(
        "easy-h1",
        fontName=base.FONT_BOLD,
        fontSize=18,
        leading=23,
        textColor=NAVY,
        spaceBefore=9,
        spaceAfter=11,
        keepWithNext=True,
    ),
    "h2": style(
        "easy-h2",
        fontName=base.FONT_BOLD,
        fontSize=15,
        leading=20,
        textColor=white,
        backColor=BLUE,
        borderPadding=10,
        spaceBefore=13,
        spaceAfter=10,
        keepWithNext=True,
    ),
    "vault_h2": style(
        "easy-vault-h2",
        fontName=base.FONT_BOLD,
        fontSize=15,
        leading=20,
        textColor=white,
        backColor=GREEN,
        borderColor=AMBER,
        borderWidth=1.2,
        borderPadding=10,
        spaceBefore=13,
        spaceAfter=10,
        keepWithNext=True,
    ),
    "h3": style(
        "easy-h3",
        fontName=base.FONT_BOLD,
        fontSize=11.4,
        leading=15,
        textColor=TEAL,
        spaceBefore=9,
        spaceAfter=5,
        keepWithNext=True,
    ),
    "session": style(
        "easy-session",
        fontName=base.FONT_BOLD,
        fontSize=14.4,
        leading=19,
        textColor=white,
        backColor=TEAL,
        borderPadding=9,
        spaceBefore=11,
        spaceAfter=8,
        keepWithNext=True,
    ),
    "h4": style(
        "easy-h4",
        fontName=base.FONT_BOLD,
        fontSize=10.4,
        leading=14.2,
        textColor=AMBER,
        spaceBefore=7,
        spaceAfter=4,
        keepWithNext=True,
    ),
    "bullet": style(
        "easy-bullet",
        leftIndent=17,
        firstLineIndent=-9,
        bulletIndent=5,
        spaceAfter=4,
    ),
    "answer": style(
        "easy-answer",
        fontName=base.FONT_BOLD,
        textColor=GREEN,
        backColor=GREEN_BG,
        borderColor=GREEN,
        borderWidth=0.7,
        borderPadding=7,
        spaceBefore=5,
        spaceAfter=7,
    ),
    "model": style(
        "easy-model",
        fontName=base.FONT_BOLD,
        fontSize=10.8,
        leading=15,
        textColor=NAVY,
        backColor=AMBER_BG,
        borderColor=AMBER,
        borderWidth=0.7,
        borderPadding=8,
        spaceBefore=7,
        spaceAfter=7,
    ),
    "caption": style(
        "easy-caption",
        fontName=base.FONT_ITALIC,
        fontSize=8.4,
        leading=11,
        textColor=SUBTEXT,
        alignment=TA_CENTER,
    ),
    "footer": style(
        "easy-footer",
        fontSize=7.6,
        leading=9,
        textColor=SUBTEXT,
        alignment=TA_CENTER,
    ),
    "contents_title": style(
        "easy-contents-title",
        fontName=base.FONT_BOLD,
        fontSize=18,
        leading=23,
        textColor=white,
        backColor=NAVY,
        borderPadding=10,
        spaceAfter=9,
    ),
    "contents_intro": style(
        "easy-contents-intro",
        fontSize=9.3,
        leading=13.5,
        textColor=SUBTEXT,
        spaceAfter=12,
    ),
}


INDEX_STYLES = [
    style(
        "easy-index-0",
        fontName=base.FONT_BOLD,
        fontSize=10.5,
        leading=14,
        textColor=NAVY,
        spaceBefore=3,
        spaceAfter=3,
    ),
    style(
        "easy-index-1",
        fontName=base.FONT_BOLD,
        fontSize=9.6,
        leading=13,
        leftIndent=14,
        firstLineIndent=-5,
        textColor=BLUE,
        spaceBefore=2,
        spaceAfter=2,
    ),
    style(
        "easy-index-2",
        fontSize=8.8,
        leading=11.8,
        leftIndent=28,
        firstLineIndent=-5,
        textColor=TEXT,
        spaceBefore=1,
        spaceAfter=1,
    ),
]


def easy_paragraph(text: str, paragraph_style=None):
    if (
        paragraph_style is STYLES["h2"]
        and base.plain(text).upper().startswith("COMPLETE DATA VAULT")
    ):
        paragraph_style = STYLES["vault_h2"]
    return _BASE_PARAGRAPH(text, paragraph_style)


def easy_preformatted(text: str, paragraph_style, *args, **kwargs):
    if getattr(paragraph_style, "fontSize", 0) < 7.5:
        paragraph_style = ParagraphStyle(
            f"{paragraph_style.name}-readable",
            parent=paragraph_style,
            fontSize=7.5,
            leading=max(9.2, getattr(paragraph_style, "leading", 0)),
        )
    return _BASE_PREFORMATTED(text, paragraph_style, *args, **kwargs)


def configure_base() -> None:
    base.MARGIN = MARGIN
    base.USABLE_WIDTH = USABLE_WIDTH
    base.STYLES = STYLES
    base.INDEX_LEVEL_STYLES = INDEX_STYLES
    base.NAVY = NAVY
    base.BLUE = BLUE
    base.TEAL = TEAL
    base.GREEN = GREEN
    base.AMBER = AMBER
    base.RED = RED
    base.TEXT = TEXT
    base.SUBTEXT = SUBTEXT
    base.BORDER = BORDER
    base.LIGHT = LIGHT
    base.BLUE_BG = BLUE_BG
    base.GREEN_BG = GREEN_BG
    base.AMBER_BG = AMBER_BG
    base.RED_BG = RED_BG
    base.should_index_heading = lambda level, _text: level <= 2
    base.callout = easy_callout
    base.parse_table = easy_parse_table
    base.paragraph = easy_paragraph
    base.Preformatted = easy_preformatted


def easy_callout(text: str):
    upper = base.plain(text).upper()
    if upper.startswith(("COMMON CONFUSION:", "WRONG:")):
        color, background = RED, RED_BG
    elif upper.startswith(("TEACHER EXPLAINS:", "FOUNDATION", "SIMPLE EXAMPLE")):
        color, background = TEAL, TEAL_BG
    elif upper.startswith(("NOW ADD THE EXACT LAW:", "EXACT CONSTITUTIONAL")):
        color, background = BLUE, BLUE_BG
    elif upper.startswith(("EXAM USE:", "EXAM APPLICATION")):
        color, background = AMBER, AMBER_BG
    elif upper.startswith(("WHAT MUST I REMEMBER:", "FACT:", "MEMORY:")):
        color, background = GREEN, GREEN_BG
    else:
        color, background = BLUE, BLUE_BG
    body = Table(
        [[base.paragraph(text)]],
        colWidths=[USABLE_WIDTH],
        hAlign="LEFT",
    )
    body.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("LINEBEFORE", (0, 0), (0, -1), 4, color),
                ("BOX", (0, 0), (-1, -1), 0.35, BORDER),
                ("LEFTPADDING", (0, 0), (-1, -1), 11),
                ("RIGHTPADDING", (0, 0), (-1, -1), 11),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    return body


def easy_parse_table(lines: list[str], start: int):
    block: list[str] = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        block.append(lines[index].strip())
        index += 1
    if len(block) < 2 or not base.is_table_separator(block[1]):
        return None, start + 1

    raw_rows = [
        [cell.strip() for cell in row.strip("|").split("|")]
        for row in [block[0], *block[2:]]
    ]
    width = max(len(row) for row in raw_rows)
    raw_rows = [(row + [""] * width)[:width] for row in raw_rows]
    data = []
    for row_number, row in enumerate(raw_rows):
        row_style = style(
            f"easy-table-{start}-{row_number}",
            fontName=base.FONT_BOLD if row_number == 0 else base.FONT,
            fontSize=8.3 if width >= 4 else 8.8,
            leading=11.3 if width >= 4 else 12.0,
            textColor=white if row_number == 0 else TEXT,
            spaceAfter=0,
        )
        data.append([base.paragraph(cell, row_style) for cell in row])

    weights = []
    for column in range(width):
        longest = max(len(base.plain(row[column])) for row in raw_rows)
        weights.append(max(8, min(longest, 38)))
    total = sum(weights)
    col_widths = [USABLE_WIDTH * weight / total for weight in weights]
    table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), BLUE),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, LIGHT]),
                ("GRID", (0, 0), (-1, -1), 0.45, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table, index


class EasyDocTemplate(base.IndexedDocTemplate):
    def __init__(self, *args, **kwargs):
        self.current_section = "Opening roadmap"
        super().__init__(*args, **kwargs)

    def afterFlowable(self, flowable) -> None:
        level = getattr(flowable, "_index_level", None)
        if level == 1:
            self.current_section = getattr(flowable, "_outline_title", self.current_section)
        index_text = getattr(flowable, "_index_text", None)
        if index_text:
            plain_text = base.plain(html.unescape(index_text))
            if len(plain_text) > 64:
                clipped = plain_text[:61].rsplit(" ", 1)[0].rstrip(" ,:;-")
                flowable._index_text = html.escape(clipped + "...", quote=False)
        super().afterFlowable(flowable)


def cover_story(title: str) -> list:
    title_box = Table(
        [
            [
                [
                    base.paragraph("EASY LEARNING / GUIDED LEARNING EDITION", STYLES["cover_subtitle"]),
                    Spacer(1, 0.22 * cm),
                    base.paragraph(title, STYLES["cover_title"]),
                ]
            ]
        ],
        colWidths=[USABLE_WIDTH],
    )
    title_box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("LINEBEFORE", (0, 0), (0, 0), 8, TEAL),
                ("LEFTPADDING", (0, 0), (-1, -1), 24),
                ("RIGHTPADDING", (0, 0), (-1, -1), 22),
                ("TOPPADDING", (0, 0), (-1, -1), 30),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 30),
            ]
        )
    )
    path_box = Table(
        [
            [
                base.paragraph("<b>1</b><br/>First Pass<br/><font size='8'>Understand simply</font>"),
                base.paragraph("<b>2</b><br/>Exact Law Pass<br/><font size='8'>Add text and doctrine</font>"),
                base.paragraph("<b>3</b><br/>Exam Pass<br/><font size='8'>Practise use</font>"),
                base.paragraph("<b>4</b><br/>Data Vault<br/><font size='8'>Retain every detail</font>"),
            ]
        ],
        colWidths=[USABLE_WIDTH / 4] * 4,
    )
    path_box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BLUE_BG),
                ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 11),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
            ]
        )
    )
    return [
        Spacer(1, 1.25 * cm),
        title_box,
        Spacer(1, 0.65 * cm),
        base.paragraph(
            "Slow explanation first. Exact constitutional and legal language second. "
            "Cases, exceptions and exam language third. Complete source data remains available "
            "in the final Data Vault.",
            style("easy-cover-note", fontSize=11, leading=17, alignment=TA_CENTER, textColor=SUBTEXT),
        ),
        Spacer(1, 0.55 * cm),
        path_box,
        Spacer(1, 0.65 * cm),
        HRFlowable(width="38%", thickness=3, color=TEAL, hAlign="LEFT"),
        Spacer(1, 0.18 * cm),
        base.paragraph(
            "Indian Polity | UPSC Prelims and GS-II | Additional teaching edition",
            STYLES["footer"],
        ),
        PageBreak(),
    ]


def contents_story() -> list:
    toc = base.TableOfContents()
    toc.levelStyles = INDEX_STYLES
    toc.dotsMinLevel = 0
    return [
        base.paragraph("CONTENTS / GUIDED MODULE INDEX", STYLES["contents_title"]),
        base.paragraph(
            "The index lists the opening roadmap, guided modules, understanding-check answers "
            "and the Complete Data Vault. Page numbers and PDF bookmarks are generated from the "
            "final layout.",
            STYLES["contents_intro"],
        ),
        toc,
        PageBreak(),
    ]


def on_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_WIDTH, 0.72 * cm, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, PAGE_HEIGHT - 0.13 * cm, PAGE_WIDTH, 0.13 * cm, fill=1, stroke=0)
    canvas.setFont(base.FONT, 7.4)
    canvas.setFillColor(white)
    section = getattr(doc, "current_section", "Guided Learning")
    if len(section) > 58:
        section = section[:55] + "..."
    canvas.drawString(MARGIN, 0.25 * cm, f"GUIDED PROGRESS | {section}")
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 0.25 * cm, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(source_path: str | Path, output_path: str | Path) -> Path:
    configure_base()
    source = Path(source_path)
    output = Path(output_path)
    if not source.is_file():
        raise FileNotFoundError(source)
    metadata, body = base.split_frontmatter(source.read_text(encoding="utf-8"))
    heading = next(
        (line.strip()[2:] for line in body.splitlines() if line.startswith("# ")),
        source.stem,
    )
    title = base.plain(metadata.get("title") or heading)
    output.parent.mkdir(parents=True, exist_ok=True)
    document = EasyDocTemplate(
        str(output),
        enable_internal_index=True,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.2 * cm,
        bottomMargin=1.25 * cm,
        title=title,
        author="UPSC Agent / Copilot CLI",
        invariant=1,
    )
    story = cover_story(title)
    story.extend(contents_story())
    story.extend(base.markdown_story(body, source.parent, internal_index=True))
    document.multiBuild(
        story,
        maxPasses=12,
        canvasmaker=partial(Canvas, invariant=1),
        onFirstPage=on_page,
        onLaterPages=on_page,
    )
    return output.resolve()


def validate_pdf(pdf_path: str | Path) -> dict:
    path = Path(pdf_path)
    doc = fitz.open(path)
    blank_pages: list[int] = []
    near_empty_pages: list[int] = []
    replacement_glyph_pages: list[int] = []
    overflow_pages: list[int] = []
    tiny_font_pages: list[int] = []
    font_sizes: list[float] = []
    for number, page in enumerate(doc, 1):
        text = page.get_text("text").strip()
        images = page.get_images(full=True)
        if not text and not images:
            blank_pages.append(number)
        if len(text) < 90 and not images:
            near_empty_pages.append(number)
        if "\ufffd" in text or "�" in text:
            replacement_glyph_pages.append(number)
        page_rect = page.rect
        for block in page.get_text("dict").get("blocks", []):
            bbox = block.get("bbox")
            if bbox and (
                bbox[0] < -1
                or bbox[1] < -1
                or bbox[2] > page_rect.width + 1
                or bbox[3] > page_rect.height + 1
            ):
                overflow_pages.append(number)
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    y0 = span.get("bbox", [0, 0, 0, 0])[1]
                    if y0 < page_rect.height - 32:
                        size = round(float(span.get("size", 0)), 1)
                        font_sizes.append(size)
                        if size < 7.4:
                            tiny_font_pages.append(number)
    toc = doc.get_toc(simple=True)
    toc_invalid = [entry for entry in toc if entry[2] < 1 or entry[2] > len(doc)]
    result = {
        "status": "passed",
        "path": str(path),
        "page_count": len(doc),
        "bookmarks": len(toc),
        "toc_page_targets_valid": not toc_invalid,
        "blank_pages": blank_pages,
        "near_empty_pages": near_empty_pages,
        "replacement_glyph_pages": replacement_glyph_pages,
        "overflow_pages": sorted(set(overflow_pages)),
        "tiny_font_pages": sorted(set(tiny_font_pages)),
        "configured_body_font_pt": 10.6,
        "configured_body_leading_pt": 16.0,
        "configured_table_font_floor_pt": 8.3,
        "configured_ascii_font_pt": 7.5,
        "observed_min_non_footer_font_pt": min(font_sizes) if font_sizes else None,
        "observed_median_font_pt": sorted(font_sizes)[len(font_sizes) // 2] if font_sizes else None,
    }
    failures = (
        blank_pages
        or near_empty_pages
        or replacement_glyph_pages
        or overflow_pages
        or tiny_font_pages
        or toc_invalid
        or len(toc) == 0
    )
    if failures:
        result["status"] = "failed"
    doc.close()
    return result


def make_contact_sheets(
    pdf_path: str | Path,
    output_dir: str | Path,
    *,
    pages_per_sheet: int = 20,
) -> list[str]:
    pdf = fitz.open(pdf_path)
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    columns = 4
    rows = math.ceil(pages_per_sheet / columns)
    thumb_width = 285
    thumb_height = 403
    gap = 18
    header = 44
    paths: list[str] = []
    for sheet_index, start in enumerate(range(0, len(pdf), pages_per_sheet), 1):
        end = min(start + pages_per_sheet, len(pdf))
        canvas = PILImage.new(
            "RGB",
            (
                columns * thumb_width + (columns + 1) * gap,
                rows * thumb_height + (rows + 1) * gap + header,
            ),
            "white",
        )
        draw = ImageDraw.Draw(canvas)
        draw.text(
            (gap, 12),
            f"{Path(pdf_path).name} | pages {start + 1}-{end}",
            fill="#18324A",
        )
        for offset, page_number in enumerate(range(start, end)):
            page = pdf[page_number]
            pix = page.get_pixmap(matrix=fitz.Matrix(0.55, 0.55), alpha=False)
            image = PILImage.frombytes("RGB", [pix.width, pix.height], pix.samples)
            image.thumbnail((thumb_width, thumb_height - 18))
            row, column = divmod(offset, columns)
            x = gap + column * (thumb_width + gap)
            y = header + gap + row * (thumb_height + gap)
            canvas.paste(image, (x, y + 16))
            draw.text((x, y), f"p.{page_number + 1}", fill="#263847")
            draw.rectangle(
                (x, y + 16, x + image.width, y + 16 + image.height),
                outline="#D5DEE5",
                width=1,
            )
        target = output / f"contact-sheet-{sheet_index:02d}.png"
        canvas.save(target, optimize=True)
        paths.append(str(target))
    pdf.close()
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Guided Learning Edition PDF.")
    parser.add_argument("source")
    parser.add_argument("output")
    parser.add_argument("--contact-dir")
    parser.add_argument("--validation-json")
    args = parser.parse_args()
    output = build_pdf(args.source, args.output)
    validation = validate_pdf(output)
    if args.contact_dir:
        validation["contact_sheets"] = make_contact_sheets(output, args.contact_dir)
    if args.validation_json:
        target = Path(args.validation_json)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(validation, indent=2), encoding="utf-8")
    print(json.dumps(validation, indent=2))
    if validation["status"] != "passed":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
