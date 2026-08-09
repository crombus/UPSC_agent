"""
Render a complete UPSC learning-session Markdown file as an explanatory PDF.

Unlike the register-card compiler, this renderer preserves continuous
explanations, worked examples, Markdown tables, ASCII diagrams, questions,
solutions and final revision notes.

Usage:
    python tools/markdown_learning_pdf.py source.md output.pdf
    python tools/markdown_learning_pdf.py source.md workbook.pdf --mode workbook
    python tools/markdown_learning_pdf.py source.md output.pdf --image illustration.png
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.graphics.shapes import Circle, Drawing, Line, Rect, String
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
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

FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"

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
        textColor=BLUE, spaceBefore=10, spaceAfter=6, keepWithNext=True,
    ),
    "h3": style(
        "h3", fontName=FONT_BOLD, fontSize=10.6, leading=14,
        textColor=TEAL, spaceBefore=7, spaceAfter=4, keepWithNext=True,
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
}


TOKEN_REPLACEMENTS = {
    "✅": "FACT:",
    "⚠️": "ANALYSIS:",
    "⚠": "ANALYSIS:",
    "📰": "CURRENT:",
    "❌": "WRONG:",
    "🔑": "MEMORY:",
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
    for source, replacement in TOKEN_REPLACEMENTS.items():
        text = text.replace(source, replacement)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    return text


def paragraph(text: str, paragraph_style: ParagraphStyle | None = None) -> Paragraph:
    return Paragraph(inline(text), paragraph_style or STYLES["body"])


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
        row_style = style(
            f"table-{row_number}",
            fontName=FONT_BOLD if row_number == 0 else FONT,
            fontSize=7.8 if width >= 4 else 8.3,
            leading=10.5 if width >= 4 else 11.2,
            textColor=white if row_number == 0 else TEXT,
            spaceAfter=0,
        )
        data.append([paragraph(cell, row_style) for cell in row])

    weights = []
    for column in range(width):
        longest = max(len(plain(row[column])) for row in raw_rows)
        weights.append(max(8, min(longest, 35)))
    total = sum(weights)
    col_widths = [USABLE_WIDTH * weight / total for weight in weights]
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


def callout(text: str) -> KeepTogether:
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
    return KeepTogether([body])


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
            "Economy | GS-III and Prelims | Foundation to advanced | "
            "Concepts, worked examples, traps, current linkage and answer writing",
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
                "AI-generated conceptual illustration; not factual or quantitative evidence.",
                STYLES["caption"],
            ),
        ])
    else:
        story.extend([
            economy_identity_visual(),
            paragraph(
                "Deterministic fallback visual: national income viewed through production, "
                "income, expenditure and welfare lenses.",
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


def select_markdown(markdown: str, mode: str) -> str:
    if mode == "main":
        return markdown
    marker = "## Solved topic-specific MCQs"
    start = markdown.find(marker)
    if start < 0:
        raise ValueError("Workbook marker not found in source Markdown.")
    end_marker = "## Final consolidated register notes"
    end = markdown.find(end_marker, start)
    practice = markdown[start:] if end < 0 else markdown[start:end]
    title = markdown.splitlines()[0]
    return f"{title}\n\n{practice}"


def markdown_story(markdown: str) -> list:
    lines = markdown.replace("\r\n", "\n").splitlines()
    story: list = []
    paragraph_lines: list[str] = []
    index = 0
    first_h1 = True

    def flush_paragraph() -> None:
        if paragraph_lines:
            text = " ".join(line.strip() for line in paragraph_lines)
            if text.startswith("**Answer:"):
                story.append(paragraph(text, STYLES["answer"]))
            elif text == "**Model solution**":
                story.append(paragraph(text, STYLES["model"]))
            else:
                story.append(paragraph(text))
            paragraph_lines.clear()

    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index].rstrip())
                index += 1
            code_text = "\n".join(code_lines)
            code = Preformatted(
                code_text,
                style(
                    f"code-{index}", fontName="Courier", fontSize=7.5,
                    leading=10, textColor=NAVY, backColor=LIGHT,
                    borderColor=BORDER, borderWidth=0.6, borderPadding=8,
                    spaceBefore=4, spaceAfter=7,
                ),
                maxLineLength=100,
            )
            story.append(code)
            index += 1
            continue

        heading = re.match(r"^(#{1,4})\s+(.+?)\s*$", stripped)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = plain(heading.group(2))
            if level == 1:
                if not first_h1:
                    story.append(PageBreak())
                first_h1 = False
            elif level == 2:
                story.append(CondPageBreak(3.2 * cm))
            elif level == 3 and text.startswith("Q"):
                story.append(CondPageBreak(5.0 * cm))
            story.append(paragraph(text, STYLES[f"h{level}"]))
            index += 1
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            table, next_index = parse_table(lines, index)
            if table:
                story.extend([table, Spacer(1, 0.12 * cm)])
                index = next_index
                continue

        if stripped.startswith(">"):
            flush_paragraph()
            quote_lines = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(re.sub(r"^>\s?", "", lines[index].strip()))
                index += 1
            story.extend([callout(" ".join(quote_lines)), Spacer(1, 0.08 * cm)])
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
    return story


def on_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_WIDTH, 0.62 * cm, fill=1, stroke=0)
    canvas.setFillColor(AMBER)
    canvas.rect(0, PAGE_HEIGHT - 0.13 * cm, PAGE_WIDTH, 0.13 * cm, fill=1, stroke=0)
    canvas.setFont(FONT, 7)
    canvas.setFillColor(white)
    canvas.drawString(MARGIN, 0.22 * cm, "UPSC Economy Learning Session")
    canvas.drawRightString(PAGE_WIDTH - MARGIN, 0.22 * cm, f"Page {doc.page}")
    canvas.restoreState()


def build_pdf(
    source_path: str | Path,
    output_path: str | Path,
    *,
    mode: str = "main",
    image_path: str | Path | None = None,
) -> Path:
    source = Path(source_path)
    output = Path(output_path)
    if mode not in {"main", "workbook"}:
        raise ValueError("mode must be 'main' or 'workbook'.")
    if not source.is_file():
        raise FileNotFoundError(source)

    markdown = select_markdown(source.read_text(encoding="utf-8"), mode)
    title = plain(markdown.splitlines()[0].lstrip("# "))
    if mode == "workbook":
        title = re.sub(
            r"\s*-\s*Complete Topic Package\s*$",
            " - Solved Practice Workbook",
            title,
            flags=re.IGNORECASE,
        )
    illustration = Path(image_path) if image_path else None
    if illustration and not illustration.is_file():
        raise FileNotFoundError(illustration)

    output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=1.15 * cm,
        bottomMargin=1.1 * cm,
        title=title,
        author="UPSC Agent / Copilot CLI",
    )
    story = cover_story(title, mode, illustration)
    story.extend(markdown_story(markdown))
    story.extend([
        Spacer(1, 0.45 * cm),
        HRFlowable(width="100%", thickness=1.2, color=AMBER),
        Spacer(1, 0.12 * cm),
        paragraph("End of document", STYLES["footer"]),
    ])
    document.build(story, onFirstPage=on_page, onLaterPages=on_page)
    return output.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render explanatory UPSC learning Markdown as PDF."
    )
    parser.add_argument("source")
    parser.add_argument("output")
    parser.add_argument("--mode", choices=("main", "workbook"), default="main")
    parser.add_argument("--image")
    args = parser.parse_args()
    output = build_pdf(
        args.source,
        args.output,
        mode=args.mode,
        image_path=args.image,
    )
    print(f"PDF saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
