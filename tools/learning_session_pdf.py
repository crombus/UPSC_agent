"""Render a Markdown learning-session transcript without rewriting its wording."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#17233C")
BLUE = colors.HexColor("#245B91")
AMBER = colors.HexColor("#D28B21")
TEXT = colors.HexColor("#26364A")
MUTED = colors.HexColor("#5F6F82")
LIGHT = colors.HexColor("#F5F7FA")
BORDER = colors.HexColor("#DCE2EA")
GREEN_BG = colors.HexColor("#EEF9F3")
DOCUMENT_HEADER = "UPSC LEARNING SESSION | VERBATIM NOTES"


def register_fonts() -> tuple[str, str, str, str, str, str]:
    candidates = [
        (
            Path(r"C:\Windows\Fonts\arial.ttf"),
            Path(r"C:\Windows\Fonts\arialbd.ttf"),
            Path(r"C:\Windows\Fonts\ariali.ttf"),
            Path(r"C:\Windows\Fonts\consola.ttf"),
        ),
    ]
    for regular, bold, italic, mono in candidates:
        if all(path.exists() for path in (regular, bold, italic, mono)):
            pdfmetrics.registerFont(TTFont("SessionSans", str(regular)))
            pdfmetrics.registerFont(TTFont("SessionSans-Bold", str(bold)))
            pdfmetrics.registerFont(TTFont("SessionSans-Italic", str(italic)))
            pdfmetrics.registerFont(TTFont("SessionMono", str(mono)))
            pdfmetrics.registerFont(
                TTFont("SessionSymbols", r"C:\Windows\Fonts\seguisym.ttf")
            )
            pdfmetrics.registerFont(
                TTFont("SessionEmoji", r"C:\Windows\Fonts\seguiemj.ttf")
            )
            bold_italic = Path(r"C:\Windows\Fonts\arialbi.ttf")
            if bold_italic.exists():
                pdfmetrics.registerFont(
                    TTFont("SessionSans-BoldItalic", str(bold_italic))
                )
            else:
                pdfmetrics.registerFont(TTFont("SessionSans-BoldItalic", str(bold)))
            pdfmetrics.registerFontFamily(
                "SessionSans",
                normal="SessionSans",
                bold="SessionSans-Bold",
                italic="SessionSans-Italic",
                boldItalic="SessionSans-BoldItalic",
            )
            return (
                "SessionSans",
                "SessionSans-Bold",
                "SessionSans-Italic",
                "SessionMono",
                "SessionSymbols",
                "SessionEmoji",
            )
    return (
        "Helvetica",
        "Helvetica-Bold",
        "Helvetica-Oblique",
        "Courier",
        "Helvetica",
        "Helvetica",
    )


FONT, BOLD, ITALIC, MONO, SYMBOLS, EMOJI = register_fonts()


def style(name: str, **kwargs) -> ParagraphStyle:
    defaults = {
        "fontName": FONT,
        "fontSize": 9.2,
        "leading": 13.2,
        "textColor": TEXT,
        "spaceAfter": 5,
        "alignment": TA_LEFT,
    }
    defaults.update(kwargs)
    return ParagraphStyle(name, **defaults)


BODY = style("Body")
QUOTE = style(
    "Quote",
    fontName=ITALIC,
    textColor=MUTED,
    leftIndent=12,
    borderColor=BLUE,
    borderWidth=2,
    borderPadding=7,
    backColor=LIGHT,
)
LIST = style("List", leftIndent=12, firstLineIndent=-8)
H1 = style("H1", fontName=BOLD, fontSize=20, leading=24, textColor=NAVY, spaceBefore=8, spaceAfter=12)
H2 = style("H2", fontName=BOLD, fontSize=14, leading=18, textColor=BLUE, spaceBefore=10, spaceAfter=7)
H3 = style("H3", fontName=BOLD, fontSize=11.5, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=5)


def markup(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<font name='SessionMono'>\1</font>", escaped)
    escaped = re.sub(r"\*\*\*([^*]+?)\*\*\*", r"<b><i>\1</i></b>", escaped)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", escaped)
    escaped = re.sub(
        r"([\u2190-\u2BFF]+)",
        rf"<font name='{SYMBOLS}'>\1</font>",
        escaped,
    )
    escaped = re.sub(
        r"([\uFE0F\U0001F000-\U0001FAFF]+)",
        rf"<font name='{EMOJI}'>\1</font>",
        escaped,
    )
    return escaped


def paragraph(text: str, paragraph_style: ParagraphStyle = BODY) -> Paragraph:
    return Paragraph(markup(text), paragraph_style)


def parse_table(lines: list[str], usable_width: float) -> Table:
    rows = []
    header_style = style("HeadCell", fontName=BOLD, fontSize=8.1, leading=10.8, textColor=colors.white)
    body_style = style("Cell", fontSize=8.1, leading=10.8)
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        cell_style = header_style if not rows else body_style
        rows.append([paragraph(cell, cell_style) for cell in cells])
    column_count = max(len(row) for row in rows)
    for row in rows:
        row.extend([paragraph("")] * (column_count - len(row)))
    table = Table(rows, colWidths=[usable_width / column_count] * column_count, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), BOLD),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.35, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def markdown_story(text: str, usable_width: float) -> list:
    story = []
    lines = text.splitlines()
    index = 0
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        if paragraph_lines:
            story.append(paragraph(" ".join(line.strip() for line in paragraph_lines)))
            paragraph_lines.clear()

    while index < len(lines):
        line = lines[index]

        if line.startswith("```"):
            flush_paragraph()
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            story.append(KeepTogether([
                Preformatted(
                    "\n".join(code_lines),
                    style(
                        "Code",
                        fontName=MONO,
                        fontSize=7.6,
                        leading=10,
                        backColor=LIGHT,
                        borderColor=BORDER,
                        borderWidth=0.7,
                        borderPadding=8,
                        spaceBefore=4,
                        spaceAfter=7,
                    ),
                )
            ]))
            index += 1
            continue

        if line.startswith("|") and index + 1 < len(lines) and lines[index + 1].startswith("|"):
            flush_paragraph()
            table_lines = []
            while index < len(lines) and lines[index].startswith("|"):
                table_lines.append(lines[index])
                index += 1
            story.append(parse_table(table_lines, usable_width))
            story.append(Spacer(1, 0.12 * cm))
            continue

        if re.fullmatch(r"\s*---+\s*", line):
            flush_paragraph()
            story.append(HRFlowable(width="100%", thickness=0.7, color=BORDER, spaceBefore=5, spaceAfter=7))
            index += 1
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            story.append(paragraph(heading.group(2), {1: H1, 2: H2, 3: H3}[level]))
            index += 1
            continue

        if line.strip() == ">":
            flush_paragraph()
            index += 1
            continue

        if line.startswith("> "):
            flush_paragraph()
            story.append(paragraph(line[2:], QUOTE))
            index += 1
            continue

        if re.match(r"^\((?:[a-d]|[A-D])\)\s+\S", line.strip()):
            flush_paragraph()
            story.append(paragraph(line.strip(), LIST))
            index += 1
            continue

        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line):
            flush_paragraph()
            item_text = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line)
            marker = re.match(r"^\s*(\d+\.|[-*])", line).group(1)
            story.append(paragraph(f"{marker} {item_text}", LIST))
            index += 1
            continue

        if not line.strip():
            flush_paragraph()
            story.append(Spacer(1, 0.05 * cm))
            index += 1
            continue

        paragraph_lines.append(line)
        index += 1

    flush_paragraph()
    return story


def on_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 0.18 * cm, PAGE_W, 0.18 * cm, fill=1, stroke=0)
    canvas.setStrokeColor(BORDER)
    canvas.line(1.7 * cm, PAGE_H - 0.9 * cm, PAGE_W - 1.7 * cm, PAGE_H - 0.9 * cm)
    canvas.setFont(BOLD, 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(1.7 * cm, PAGE_H - 0.68 * cm, DOCUMENT_HEADER)
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 0.55 * cm, fill=1, stroke=0)
    canvas.setFont(FONT, 7)
    canvas.setFillColor(colors.white)
    canvas.drawRightString(PAGE_W - 1.7 * cm, 0.19 * cm, f"Page {doc.page}")
    canvas.restoreState()


def build(
    markdown_path: Path,
    pdf_path: Path,
    *,
    document_header: str = "UPSC LEARNING SESSION | VERBATIM NOTES",
    document_title: str = "Notions of God - Verbatim Learning Session",
) -> None:
    global DOCUMENT_HEADER
    DOCUMENT_HEADER = document_header
    text = markdown_path.read_text(encoding="utf-8")
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.15 * cm,
        bottomMargin=1.0 * cm,
        title=document_title,
        author="UPSC Agent / Copilot CLI",
    )
    usable_width = PAGE_W - doc.leftMargin - doc.rightMargin
    doc.build(markdown_story(text, usable_width), onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF saved: {pdf_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("pdf", type=Path)
    parser.add_argument(
        "--header",
        default="UPSC LEARNING SESSION | VERBATIM NOTES",
    )
    parser.add_argument(
        "--title",
        default="Notions of God - Verbatim Learning Session",
    )
    args = parser.parse_args()
    build(
        args.markdown,
        args.pdf,
        document_header=args.header,
        document_title=args.title,
    )


if __name__ == "__main__":
    main()
