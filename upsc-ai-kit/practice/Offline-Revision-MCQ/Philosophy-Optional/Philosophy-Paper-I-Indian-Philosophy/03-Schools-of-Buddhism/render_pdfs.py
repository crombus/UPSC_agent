from __future__ import annotations

import hashlib
import re
from html import escape
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / "pdf"
SURFACES = {
    "REVISION-GUIDE.md": "Schools-of-Buddhism-Revision-Guide.pdf",
    "MCQ-QUESTIONS.md": "Schools-of-Buddhism-MCQ-Questions.pdf",
    "MCQ-SOLUTIONS.md": "Schools-of-Buddhism-MCQ-Solutions.pdf",
    "ANSWER-WRITING-TOOLKIT.md": "Schools-of-Buddhism-Answer-Writing-Toolkit.pdf",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_inline(text: str) -> str:
    text = re.sub(r'<a id="[^"]+"></a>', "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    return escape(text, quote=False).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>").replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")


def render(src: Path, dest: Path) -> dict:
    source_hash = sha(src)
    font = "Helvetica"
    bold = "Helvetica-Bold"
    for candidate in (Path(r"C:\Windows\Fonts\arial.ttf"), Path(r"C:\Windows\Fonts\segoeui.ttf")):
        if candidate.exists():
            pdfmetrics.registerFont(TTFont("PackageUnicode", str(candidate)))
            font = "PackageUnicode"
            bold = "PackageUnicode"
            break
    styles = getSampleStyleSheet()
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName=font, fontSize=8.4, leading=11.2, spaceAfter=3)
    quote = ParagraphStyle("Quote", parent=body, leftIndent=8 * mm, borderColor=colors.HexColor("#3a6ea5"), borderWidth=1, borderPadding=5, backColor=colors.HexColor("#eef5fb"))
    code = ParagraphStyle("Code", parent=body, fontName=font, fontSize=7.4, leading=9.2, leftIndent=4 * mm, backColor=colors.HexColor("#f3f4f6"))
    hs = {
        1: ParagraphStyle("H1", parent=styles["Heading1"], fontName=bold, fontSize=18, leading=22, alignment=TA_CENTER, textColor=colors.HexColor("#102a43"), spaceAfter=12),
        2: ParagraphStyle("H2", parent=styles["Heading2"], fontName=bold, fontSize=13, leading=16, textColor=colors.HexColor("#174a7e"), spaceBefore=10, spaceAfter=6),
        3: ParagraphStyle("H3", parent=styles["Heading3"], fontName=bold, fontSize=10.5, leading=13, textColor=colors.HexColor("#245b8f"), spaceBefore=7, spaceAfter=4),
        4: ParagraphStyle("H4", parent=body, fontName=bold, fontSize=9.2, leading=11.5, textColor=colors.HexColor("#333333"), spaceBefore=5),
    }

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont(font, 7)
        canvas.setFillColor(colors.HexColor("#667788"))
        canvas.drawString(18 * mm, 10 * mm, "Schools of Buddhism · Offline Revision MCQ System")
        canvas.drawRightString(192 * mm, 10 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(dest), pagesize=A4, rightMargin=16 * mm, leftMargin=16 * mm,
                            topMargin=15 * mm, bottomMargin=16 * mm, title=src.stem,
                            author="UPSC AI Kit", subject=f"source-sha256:{source_hash}",
                            creator="package-local deterministic renderer", invariant=1)
    story = []
    in_code = False
    code_lines = []
    for raw in src.read_text(encoding="utf-8").splitlines():
        if raw.startswith("```"):
            if in_code:
                story.append(Paragraph("<br/>".join(escape(x) or " " for x in code_lines), code))
                code_lines = []
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(raw)
            continue
        if re.fullmatch(r'<a id="[^"]+"></a>', raw.strip()) or not raw.strip():
            if not raw.strip():
                story.append(Spacer(1, 1.5 * mm))
            continue
        hm = re.match(r"^(#{1,4})\s+(.+)", raw)
        if hm:
            story.append(Paragraph(clean_inline(hm.group(2)), hs[len(hm.group(1))]))
        elif raw.startswith(">"):
            story.append(Paragraph(clean_inline(raw.lstrip("> ")), quote))
        elif raw.startswith("|"):
            story.append(Paragraph(clean_inline(raw), code))
        elif re.match(r"^\s*[-*]\s+", raw):
            story.append(Paragraph("• " + clean_inline(re.sub(r"^\s*[-*]\s+", "", raw)), body))
        else:
            story.append(Paragraph(clean_inline(raw), body))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    reader = PdfReader(str(dest))
    return {"file": str(dest.relative_to(ROOT)), "source": src.name, "source_sha256": source_hash,
            "pdf_sha256": sha(dest), "pages": len(reader.pages), "bytes": dest.stat().st_size}


def main() -> None:
    PDF_DIR.mkdir(exist_ok=True)
    rows = [render(ROOT / src, PDF_DIR / pdf) for src, pdf in SURFACES.items()]
    (ROOT / "PDF-MANIFEST.json").write_text(__import__("json").dumps({"schema_version": 1, "artifacts": rows}, indent=2) + "\n", encoding="utf-8")
    print(__import__("json").dumps(rows, indent=2))


if __name__ == "__main__":
    main()
