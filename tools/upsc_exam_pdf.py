"""
UPSC Exam Paper PDF Generator
Generates clean, print-ready question paper PDFs from structured data.

Usage:
    python tools/upsc_exam_pdf.py <data_module.py> [output.pdf]
"""

import sys, re, importlib.util
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY

W, H = A4
USABLE = W - 4 * cm

# ── Print-friendly palette ─────────────────────────────────────────────────────
NAVY   = HexColor("#1a1a2e")
BLUE   = HexColor("#0f3460")
GREY   = HexColor("#666666")
LGREY  = HexColor("#f5f5f5")
BORDER = HexColor("#999999")
TEXT   = black

# ── Styles ─────────────────────────────────────────────────────────────────────
def S(name="", **kw):
    base = dict(fontName="Helvetica", fontSize=10, textColor=TEXT,
                leading=14, spaceAfter=2, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name or f"_s{id(kw)}", **base)

EXAM_TITLE_S   = S("ET",  fontName="Helvetica-Bold", fontSize=16, textColor=white,
                   alignment=TA_CENTER, leading=20)
EXAM_SUB_S     = S("ES",  fontSize=9,  textColor=HexColor("#cccccc"),
                   alignment=TA_CENTER, leading=12)
SEC_HEAD_S     = S("SH",  fontName="Helvetica-Bold", fontSize=11, textColor=white,
                   alignment=TA_CENTER, leading=15)
PART_HEAD_S    = S("PH",  fontName="Helvetica-Bold", fontSize=9.5, textColor=BLUE,
                   spaceBefore=4, spaceAfter=3)
INSTR_S        = S("IN",  fontSize=9,  textColor=GREY, leading=13)
Q_NUM_S        = S("QN",  fontName="Helvetica-Bold", fontSize=10, textColor=NAVY,
                   leading=14)
Q_TEXT_S       = S("QT",  fontSize=10, leading=14, alignment=TA_JUSTIFY)
STMT_S         = S("ST",  fontSize=9.5, leading=13, leftIndent=12)
OPT_S          = S("OP",  fontSize=9.5, leading=13)
MAINS_Q_S      = S("MQ",  fontSize=10, leading=14, alignment=TA_JUSTIFY)
MAINS_META_S   = S("MM",  fontSize=8.5, textColor=GREY, fontName="Helvetica-Oblique",
                   leading=12, spaceAfter=8)
FOOTER_S       = S("FT",  fontSize=7.5, textColor=GREY, alignment=TA_CENTER)

def sp(h=0.2):
    return Spacer(1, h * cm)

def hr(thick=0.5, color=BORDER):
    return HRFlowable(width="100%", thickness=thick, color=color, spaceAfter=4, spaceBefore=4)

def p(text, style=None):
    s = style or Q_TEXT_S
    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', str(text).replace("&", "&amp;"))
    return Paragraph(txt, s)


# ── Section banner ─────────────────────────────────────────────────────────────
def section_banner(text, marks_text=""):
    content = f"{text}   <font size='9'>({marks_text})</font>" if marks_text else text
    banner = Table([[p(content, SEC_HEAD_S)]], colWidths=[USABLE])
    banner.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), NAVY),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ]))
    return banner

def part_banner(text):
    return p(f"▶  {text}", PART_HEAD_S)


# ── MCQ question builder ───────────────────────────────────────────────────────
def build_mcq(q):
    """Build one MCQ block: question stem + 4 options (A/B left, C/D right layout)."""
    elems = []
    qno   = q.get("no", "")

    # Question stem (may have multiple statements)
    stem_rows = [[p(f"Q{qno}.", Q_NUM_S), p(q["text"], Q_TEXT_S)]]
    if q.get("statements"):
        for stmt in q["statements"]:
            stem_rows.append([p(""), p(stmt, STMT_S)])
    if q.get("stem_tail"):
        stem_rows.append([p(""), p(q["stem_tail"], Q_TEXT_S)])
    # Inline data table (for DI questions)
    if q.get("table"):
        tbl_data = [q["table"]["headers"]] + q["table"]["rows"]
        ncols = len(tbl_data[0])
        cw    = [(USABLE - 1.5*cm) / ncols] * ncols
        dtbl  = Table([[Paragraph(str(c), OPT_S) for c in row] for row in tbl_data],
                      colWidths=cw)
        dtbl.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), LGREY),
            ("GRID",       (0,0), (-1,-1), 0.4, BORDER),
            ("FONTNAME",   (0,0), (-1,0),  "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("LEFTPADDING",   (0,0), (-1,-1), 5),
            ("RIGHTPADDING",  (0,0), (-1,-1), 5),
        ]))
        stem_rows.append([p(""), dtbl])
        if q.get("table_tail"):
            stem_rows.append([p(""), p(q["table_tail"], Q_TEXT_S)])

    stem_tbl = Table(stem_rows, colWidths=[1.0*cm, USABLE - 1.0*cm])
    stem_tbl.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
    ]))

    # Options: A/C left, B/D right (2×2 grid)
    opts = q.get("options", [])
    lw   = (USABLE - 1.0*cm) * 0.5
    o    = [p(o, OPT_S) for o in opts]
    while len(o) < 4:
        o.append(p(""))

    opts_tbl = Table(
        [[o[0], o[1]], [o[2], o[3]]],
        colWidths=[lw, lw]
    )
    opts_tbl.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (-1,-1), 4),
        ("RIGHTPADDING",  (0,0), (-1,-1), 4),
    ]))

    # Wrap stem + options in a light-background row
    outer = Table(
        [[stem_tbl], [opts_tbl]],
        colWidths=[USABLE]
    )
    outer.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), white),
        ("BOX",           (0,0), (-1,-1), 0.4, BORDER),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("ROWBACKGROUNDS",(0,0), (-1,-1), [white, LGREY]),
    ]))
    elems.append(KeepTogether([outer, sp(0.15)]))
    return elems


# ── Mains question builder ─────────────────────────────────────────────────────
def build_mains(q):
    qno  = q.get("no", "")
    meta = q.get("meta", "")
    rows = [
        [p(f"Q{qno}.", Q_NUM_S), p(q["text"], MAINS_Q_S)],
    ]
    if meta:
        rows.append([p(""), p(meta, MAINS_META_S)])

    tbl = Table(rows, colWidths=[1.0*cm, USABLE - 1.0*cm])
    tbl.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("BACKGROUND",    (0,0), (-1,-1), white),
        ("BOX",           (0,0), (-1,-1), 0.4, BORDER),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
    ]))
    return [KeepTogether([tbl, sp(0.18)])]


# ── Page header/footer ────────────────────────────────────────────────────────
def on_page(canvas, doc, exam_title="UPSC Practice Exam"):
    canvas.saveState()
    # Footer bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, W, 0.8*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(white)
    canvas.drawString(2*cm, 0.26*cm, exam_title)
    canvas.drawRightString(W - 2*cm, 0.26*cm, f"Page {doc.page}")
    canvas.restoreState()


# ── Main builder ──────────────────────────────────────────────────────────────
def build_pdf(data: dict, out_path: str):
    exam_title = data.get("title", "UPSC Practice Exam")

    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.8*cm, bottomMargin=1.4*cm,
        title=exam_title,
        author="UPSC Agent / Copilot CLI",
    )

    story = []

    # ── Cover header ──────────────────────────────────────────────────────────
    cover_rows = [
        [p(exam_title, EXAM_TITLE_S)],
        [p(f"Date: {data.get('date','')}   |   Maximum Marks: {data.get('max_marks','')}   |   Time: {data.get('time','')}", EXAM_SUB_S)],
    ]
    if data.get("topics"):
        cover_rows.append([p(f"Topics: {data['topics']}", EXAM_SUB_S)])
    cover = Table(cover_rows, colWidths=[USABLE])
    cover.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), NAVY),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ]))
    story.append(cover)
    story.append(sp(0.3))

    # Instructions box
    if data.get("instructions"):
        instr_rows = [[p("INSTRUCTIONS:", S(fontName="Helvetica-Bold", fontSize=9,
                                            textColor=BLUE, leading=13))]]
        for inst in data["instructions"]:
            instr_rows.append([p(f"• {inst}", INSTR_S)])
        instr_tbl = Table(instr_rows, colWidths=[USABLE])
        instr_tbl.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (-1,-1), LGREY),
            ("BOX",           (0,0), (-1,-1), 0.8, BLUE),
            ("TOPPADDING",    (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING",   (0,0), (-1,-1), 8),
            ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ]))
        story.append(instr_tbl)
        story.append(sp(0.4))

    # ── Sections ──────────────────────────────────────────────────────────────
    for section in data.get("sections", []):
        story.append(section_banner(section["name"], section.get("marks_text", "")))
        story.append(sp(0.2))

        if section.get("instruction"):
            story.append(p(section["instruction"], INSTR_S))
            story.append(sp(0.15))

        # Parts (e.g. Section A has Part 1, Part 2…)
        if section.get("parts"):
            for part in section["parts"]:
                story.append(part_banner(part["name"]))
                if part.get("instruction"):
                    story.append(p(part["instruction"], INSTR_S))
                story.append(sp(0.1))
                for q in part.get("questions", []):
                    story.extend(build_mcq(q))
                story.append(sp(0.2))

        # Direct questions (Mains / Essay)
        elif section.get("questions"):
            for q in section["questions"]:
                qtype = q.get("type", "mains")
                if qtype == "mcq":
                    story.extend(build_mcq(q))
                else:
                    story.extend(build_mains(q))

        story.append(sp(0.3))

    # End line
    story.append(hr(thick=1.5, color=NAVY))
    story.append(p("— END OF QUESTION PAPER —", FOOTER_S))
    story.append(sp(0.1))
    story.append(p(f"Total: {data.get('max_marks','')} Marks  |  UPSC Practice Paper  |  Copilot CLI UPSC Agent", FOOTER_S))

    doc.build(
        story,
        onFirstPage=lambda c, d: on_page(c, d, exam_title),
        onLaterPages=lambda c, d: on_page(c, d, exam_title),
    )
    print(f"PDF saved: {out_path}")
    return out_path


# ── CLI entry ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/upsc_exam_pdf.py <data_module.py> [out.pdf]")
        sys.exit(1)

    data_path = sys.argv[1]
    out_path  = (sys.argv[2] if len(sys.argv) > 2
                 else data_path.replace("_data.py", "_QP.pdf").replace(".py", "_QP.pdf"))

    spec   = importlib.util.spec_from_file_location("data", data_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    build_pdf(module.DATA, out_path)
