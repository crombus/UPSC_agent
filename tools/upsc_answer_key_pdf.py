"""
UPSC Exam Answer Key PDF Generator
Produces a clean, print-ready Answer Key + Model Answer Frameworks.
Usage: python tools/upsc_answer_key_pdf.py <data_module.py> [out.pdf]
"""

import sys, re, importlib.util
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

W, H = A4
USABLE = W - 4 * cm

# ── Palette ────────────────────────────────────────────────────────────────────
NAVY    = HexColor("#1a1a2e")
BLUE    = HexColor("#0f3460")
GREEN   = HexColor("#1b5e20")
LGREEN  = HexColor("#e8f5e9")
RED     = HexColor("#b71c1c")
LRED    = HexColor("#ffebee")
AMBER   = HexColor("#e65100")
LAMBER  = HexColor("#fff3e0")
GREY    = HexColor("#555555")
LGREY   = HexColor("#f5f5f5")
BORDER  = HexColor("#bbbbbb")
DBORDER = HexColor("#0f3460")

def S(name="", **kw):
    base = dict(fontName="Helvetica", fontSize=10, textColor=black,
                leading=14, spaceAfter=2, spaceBefore=0)
    base.update(kw)
    return ParagraphStyle(name or f"_s{id(kw)}", **base)

COVER_TITLE_S  = S("CT", fontName="Helvetica-Bold", fontSize=16, textColor=white,
                   alignment=TA_CENTER, leading=22)
COVER_SUB_S    = S("CS", fontSize=9, textColor=HexColor("#cccccc"),
                   alignment=TA_CENTER, leading=13)
SEC_HEAD_S     = S("SH", fontName="Helvetica-Bold", fontSize=11, textColor=white,
                   alignment=TA_CENTER, leading=15)
GRID_HDR_S     = S("GH", fontName="Helvetica-Bold", fontSize=9, textColor=white,
                   alignment=TA_CENTER, leading=12)
GRID_ANS_S     = S("GA", fontName="Helvetica-Bold", fontSize=10, textColor=GREEN,
                   alignment=TA_CENTER, leading=13)
GRID_Q_S       = S("GQ", fontSize=9, textColor=GREY, alignment=TA_CENTER, leading=12)
Q_NUM_S        = S("QN", fontName="Helvetica-Bold", fontSize=10, textColor=NAVY, leading=14)
ANS_TAG_S      = S("AT", fontName="Helvetica-Bold", fontSize=9.5, textColor=GREEN, leading=13)
CORRECT_OPT_S  = S("CO", fontName="Helvetica-Bold", fontSize=9.5, textColor=GREEN,
                   leading=13, leftIndent=10)
WRONG_OPT_S    = S("WO", fontSize=9, textColor=GREY, leading=13, leftIndent=10)
EXP_HEAD_S     = S("EH", fontName="Helvetica-Bold", fontSize=9, textColor=BLUE, leading=13)
EXP_BODY_S     = S("EB", fontSize=9, textColor=black, leading=13, leftIndent=8)
SOURCE_S       = S("SR", fontSize=8, textColor=GREY, fontName="Helvetica-Oblique",
                   leading=11, leftIndent=8)
MAINS_HEAD_S   = S("MH", fontName="Helvetica-Bold", fontSize=10, textColor=NAVY, leading=14)
MAINS_META_S   = S("MM", fontSize=8.5, textColor=GREY, fontName="Helvetica-Oblique", leading=12)
BULLET_S       = S("BU", fontSize=9.5, leading=14, leftIndent=12)
FOOTER_S       = S("FT", fontSize=7.5, textColor=GREY, alignment=TA_CENTER)

def sp(h=0.2):  return Spacer(1, h * cm)
def hr(t=0.5, c=BORDER): return HRFlowable(width="100%", thickness=t, color=c,
                                            spaceAfter=4, spaceBefore=4)
def p(text, style=None):
    s = style or S()
    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>',
          re.sub(r'~~(.+?)~~',     r'<strike>\1</strike>',
          str(text).replace("&", "&amp;")))
    return Paragraph(txt, s)


def section_banner(text, sub=""):
    rows = [[p(text, SEC_HEAD_S)]]
    if sub:
        rows.append([p(sub, COVER_SUB_S)])
    tbl = Table(rows, colWidths=[USABLE])
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
    ]))
    return tbl


# ── Quick-answer grid ──────────────────────────────────────────────────────────
def build_answer_grid(mcq_answers: list):
    """
    mcq_answers: list of dicts {no, answer, topic}
    Renders a compact colour-coded grid: Q# | Ans | Topic
    """
    story = []
    story.append(section_banner("QUICK ANSWER KEY — SECTION A (MCQ)",
                                "Correct answers only. Full explanations follow."))
    story.append(sp(0.3))

    # Build rows of 5 per line
    COLS = 5
    col_w = USABLE / COLS

    hdr = [p(f"Q{a['no']}  →  {a['answer']}", GRID_ANS_S) for a in mcq_answers]
    rows = [hdr[i:i+COLS] for i in range(0, len(hdr), COLS)]
    # pad last row
    while len(rows[-1]) < COLS:
        rows[-1].append(p(""))

    grid = Table(rows, colWidths=[col_w]*COLS)
    grid.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LGREEN),
        ("GRID",          (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(grid)
    story.append(sp(0.3))

    # Marking scheme reminder
    mark_rows = [
        [p("Correct", S(fontName="Helvetica-Bold", fontSize=9, textColor=GREEN, alignment=TA_CENTER)),
         p("Wrong",   S(fontName="Helvetica-Bold", fontSize=9, textColor=RED, alignment=TA_CENTER)),
         p("Skipped", S(fontName="Helvetica-Bold", fontSize=9, textColor=GREY, alignment=TA_CENTER))],
        [p("+2.00", S(fontName="Helvetica-Bold", fontSize=11, textColor=GREEN, alignment=TA_CENTER)),
         p("−0.66", S(fontName="Helvetica-Bold", fontSize=11, textColor=RED,   alignment=TA_CENTER)),
         p("0",     S(fontSize=11, textColor=GREY,  alignment=TA_CENTER))],
    ]
    mark_tbl = Table(mark_rows, colWidths=[USABLE/3]*3)
    mark_tbl.setStyle(TableStyle([
        ("BOX",           (0, 0), (-1, -1), 0.8, DBORDER),
        ("GRID",          (0, 0), (-1, -1), 0.4, BORDER),
        ("BACKGROUND",    (0, 0), (-1, 0),  LGREY),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(mark_tbl)
    return story


# ── Per-question detailed explanation ─────────────────────────────────────────
def build_mcq_explanation(q: dict):
    elems = []
    no      = q["no"]
    ans     = q["answer"]
    topic   = q.get("topic", "")
    gs      = q.get("gs", "")
    opts    = q.get("options", [])
    exp     = q.get("explanation", "")
    trap    = q.get("trap", "")
    source  = q.get("source", "")

    # Header row
    hdr_data = [
        [p(f"Q{no}", Q_NUM_S),
         p(f"Answer: {ans}", ANS_TAG_S),
         p(topic, S(fontSize=9, textColor=BLUE, leading=13)),
         p(gs,    S(fontSize=8.5, textColor=GREY, fontName="Helvetica-Oblique", leading=12))],
    ]
    hdr_tbl = Table(hdr_data, colWidths=[1.0*cm, 2.2*cm, USABLE-5.5*cm, 2.3*cm])
    hdr_tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LGREY),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("BOX",           (0, 0), (-1, -1), 0.5, BLUE),
    ]))
    elems.append(hdr_tbl)

    inner = []

    # Options — highlight correct in green, rest in grey
    if opts:
        inner.append(p("Options:", EXP_HEAD_S))
        for opt in opts:
            letter = opt.strip()[1] if len(opt.strip()) > 1 else ""
            if letter == ans:
                inner.append(p(f"✔ {opt.strip()}", CORRECT_OPT_S))
            else:
                inner.append(p(f"   {opt.strip()}", WRONG_OPT_S))

    # Explanation
    if exp:
        inner.append(sp(0.1))
        inner.append(p("Explanation:", EXP_HEAD_S))
        for line in exp.strip().split("\n"):
            if line.strip():
                inner.append(p(f"  {line.strip()}", EXP_BODY_S))

    # UPSC trap
    if trap:
        inner.append(sp(0.1))
        trap_tbl = Table([[p(f"⚠ UPSC Trap: {trap}",
                              S(fontSize=8.5, textColor=AMBER,
                                fontName="Helvetica-Oblique", leading=12))]],
                         colWidths=[USABLE - 0.8*cm])
        trap_tbl.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (-1,-1), LAMBER),
            ("BOX",           (0,0), (-1,-1), 0.4, AMBER),
            ("TOPPADDING",    (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("LEFTPADDING",   (0,0), (-1,-1), 6),
            ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ]))
        inner.append(trap_tbl)

    # Source
    if source:
        inner.append(p(f"📚 Source: {source}", SOURCE_S))

    inner_tbl = Table([[item] for item in inner], colWidths=[USABLE - 0.8*cm])
    inner_tbl.setStyle(TableStyle([
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
    ]))

    outer = Table([[hdr_tbl], [inner_tbl]], colWidths=[USABLE])
    outer.setStyle(TableStyle([
        ("BOX",           (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
    ]))
    elems.append(KeepTogether([outer, sp(0.15)]))
    return elems


# ── Mains model answer ─────────────────────────────────────────────────────────
def build_mains_answer(q: dict):
    elems = []
    no    = q["no"]
    gs    = q.get("gs", "")
    marks = q.get("marks", "")
    text  = q.get("text", "")
    intro = q.get("intro", "")
    pts   = q.get("points", [])
    conc  = q.get("conclusion", "")
    score = q.get("scoring_rubric", [])

    # Question header
    hdr = Table([
        [p(f"Q{no}", Q_NUM_S), p(text, MAINS_HEAD_S)],
        [p(""),                p(f"{gs} | {marks}", MAINS_META_S)],
    ], colWidths=[1.0*cm, USABLE - 1.0*cm])
    hdr.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), LGREY),
        ("BOX",           (0, 0), (-1, -1), 0.8, BLUE),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
    ]))
    elems.append(hdr)
    elems.append(sp(0.1))

    inner = []

    if intro:
        inner.append(p("**Model Intro:**", EXP_HEAD_S))
        inner.append(p(intro, EXP_BODY_S))
        inner.append(sp(0.1))

    if pts:
        inner.append(p("**Key Points to Cover:**", EXP_HEAD_S))
        for pt in pts:
            inner.append(p(f"• {pt}", BULLET_S))
        inner.append(sp(0.1))

    if conc:
        inner.append(p("**Conclusion Direction:**", EXP_HEAD_S))
        inner.append(p(conc, EXP_BODY_S))
        inner.append(sp(0.1))

    if score:
        inner.append(p("**Scoring Rubric:**", EXP_HEAD_S))
        score_rows = [[
            p("Dimension", S(fontName="Helvetica-Bold", fontSize=8.5,
                             textColor=white, alignment=TA_CENTER)),
            p("Marks", S(fontName="Helvetica-Bold", fontSize=8.5,
                         textColor=white, alignment=TA_CENTER)),
            p("What Examiner Looks For", S(fontName="Helvetica-Bold", fontSize=8.5,
                                           textColor=white)),
        ]]
        for row in score:
            score_rows.append([
                p(row[0], S(fontSize=8.5, leading=12)),
                p(row[1], S(fontSize=8.5, leading=12, alignment=TA_CENTER)),
                p(row[2], S(fontSize=8.5, leading=12)),
            ])
        score_tbl = Table(score_rows, colWidths=[3.5*cm, 1.5*cm, USABLE - 5.0*cm - 0.8*cm])
        score_tbl.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0), BLUE),
            ("GRID",          (0, 0), (-1, -1), 0.4, BORDER),
            ("TOPPADDING",    (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("LEFTPADDING",   (0, 0), (-1, -1), 5),
            ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
            ("FONTSIZE",      (0, 1), (-1, -1), 8.5),
            ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ]))
        inner.append(score_tbl)

    for item in inner:
        elems.append(item)

    elems.append(hr())
    return elems


# ── Page footer ────────────────────────────────────────────────────────────────
def on_page(canvas, doc, exam_title="Answer Key"):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, W, 0.8*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(white)
    canvas.drawString(2*cm, 0.26*cm, f"{exam_title} — CONFIDENTIAL")
    canvas.drawRightString(W - 2*cm, 0.26*cm, f"Page {doc.page}")
    canvas.restoreState()


# ── Main builder ───────────────────────────────────────────────────────────────
def build_answer_key_pdf(data: dict, out_path: str):
    title = data.get("title", "UPSC Answer Key")

    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.8*cm, bottomMargin=1.4*cm,
        title=title, author="UPSC Agent / Copilot CLI",
    )
    story = []

    # Cover
    cover = Table([
        [p(title, COVER_TITLE_S)],
        [p(f"Date: {data.get('date','')}   |   Total: {data.get('max_marks','')} Marks", COVER_SUB_S)],
        [p(f"Topics: {data.get('topics','')}", COVER_SUB_S)],
        [p("⚠  ANSWER KEY — FOR EVALUATION USE ONLY — DO NOT DISTRIBUTE WITH QUESTION PAPER", COVER_SUB_S)],
    ], colWidths=[USABLE])
    cover.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 12),
    ]))
    story.append(cover)
    story.append(sp(0.4))

    # Quick answer grid
    story.extend(build_answer_grid(data.get("mcq_answers", [])))
    story.append(sp(0.5))

    # Detailed MCQ explanations
    story.append(section_banner("SECTION A — DETAILED EXPLANATIONS",
                                "Correct answer highlighted in green · UPSC traps flagged in amber"))
    story.append(sp(0.3))

    for q in data.get("mcq_questions", []):
        story.extend(build_mcq_explanation(q))

    story.append(PageBreak())

    # Mains model answers
    if data.get("mains_questions"):
        story.append(section_banner("SECTIONS B & C — MODEL ANSWER FRAMEWORKS",
                                    "Key points, rubric, and scoring guide"))
        story.append(sp(0.3))
        for q in data["mains_questions"]:
            story.extend(build_mains_answer(q))
            story.append(sp(0.2))

    # Essay outlines
    if data.get("essay_outlines"):
        story.append(section_banner("SECTION D — ESSAY OUTLINES",
                                    "Structure, key arguments, and examiner expectations"))
        story.append(sp(0.3))
        for essay in data["essay_outlines"]:
            story.append(p(f"**{essay['title']}**", MAINS_HEAD_S))
            story.append(sp(0.1))
            for pt in essay.get("outline", []):
                story.append(p(f"• {pt}", BULLET_S))
            story.append(hr())
            story.append(sp(0.2))

    # End
    story.append(hr(t=1.5, c=NAVY))
    story.append(p("— END OF ANSWER KEY —", FOOTER_S))
    story.append(p(f"Total: {data.get('max_marks','')} Marks | UPSC Agent / Copilot CLI", FOOTER_S))

    doc.build(
        story,
        onFirstPage=lambda c, d: on_page(c, d, title),
        onLaterPages=lambda c, d: on_page(c, d, title),
    )
    print(f"Answer Key PDF saved: {out_path}")
    return out_path


# ── CLI ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/upsc_answer_key_pdf.py <data_module.py> [out.pdf]")
        sys.exit(1)
    data_path = sys.argv[1]
    out_path  = sys.argv[2] if len(sys.argv) > 2 else data_path.replace("_data.py", "_AK.pdf").replace(".py", "_AK.pdf")
    spec   = importlib.util.spec_from_file_location("data", data_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    build_answer_key_pdf(module.DATA, out_path)
