"""
UPSC Register PDF Builder
Generates premium, register-style revision PDFs from structured topic data.

Each topic renders as a card:
  - Header: relevance badge + title + GS paper
  - News Trigger box (full width)
  - Intro & Origin  |  Timeline (flat two-column table, no nesting)
  - Key Data Table (full width)
  - Static Theory (full width)
  - Must-Know Facts  |  UPSC Traps (flat two-column table)
  - Mains Angle  |  Static Study Link (flat two-column table)

Usage:
    python tools/upsc_register_pdf.py <data_module.py> [output.pdf]
"""

import sys, re, importlib.util
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

W, H = A4
USABLE = W - 4*cm   # usable width between margins

# ── Palette ───────────────────────────────────────────────────────────────────
P = {
    "navy":     HexColor("#1a1a2e"),
    "blue":     HexColor("#0f3460"),
    "red":      HexColor("#c0392b"),
    "red_bg":   HexColor("#fdf2f2"),
    "amber":    HexColor("#d68910"),
    "amber_bg": HexColor("#fef9e7"),
    "green":    HexColor("#1e8449"),
    "green_bg": HexColor("#eafaf1"),
    "grey":     HexColor("#7f8c8d"),
    "border":   HexColor("#d5d8dc"),
    "alt_row":  HexColor("#f2f3f4"),
    "light":    HexColor("#f8f9fa"),
    "news_bg":  HexColor("#eaf4fb"),
    "news_bdr": HexColor("#2980b9"),
    "text":     HexColor("#2c3e50"),
    "subtext":  HexColor("#566573"),
}

# ── Style factory ─────────────────────────────────────────────────────────────
def S(name="", **kw):
    defaults = dict(fontName="Helvetica", fontSize=9, textColor=P["text"],
                    leading=13, spaceAfter=2, spaceBefore=0)
    defaults.update(kw)
    return ParagraphStyle(name or f"_s{id(kw)}", **defaults)

TITLE_S  = S("T",  fontName="Helvetica-Bold", fontSize=20, textColor=white, alignment=TA_CENTER, leading=24)
SUB_S    = S("SB", fontName="Helvetica", fontSize=10, textColor=HexColor("#aab7c4"), alignment=TA_CENTER)
BODY_S   = S("B",  fontSize=9, leading=13)
FOOTER_S = S("FT", fontSize=7, textColor=P["grey"], alignment=TA_CENTER)

# ── Paragraph helper ──────────────────────────────────────────────────────────
def p(text, style=None, **kw):
    """Create a Paragraph, converting **bold** and *italic* markers."""
    if style is None:
        style = S(**kw) if kw else BODY_S
    txt = str(text)
    # escape & first, then restore intentional tags
    txt = txt.replace("&", "&amp;")
    txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', txt)
    txt = re.sub(r'\*(.+?)\*',     r'<i>\1</i>', txt)
    return Paragraph(txt, style)

def spacer(h=0.2):
    return Spacer(1, h * cm)

def sec_label(emoji, title, color):
    return p(f"{emoji} {title.upper()}",
             S(fontName="Helvetica-Bold", fontSize=8.5, textColor=color,
               spaceBefore=2, spaceAfter=1))

# ── Table builders ────────────────────────────────────────────────────────────

def _ts(*cmds):
    return TableStyle(list(cmds))

_PAD = [
    ("TOPPADDING",    (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ("RIGHTPADDING",  (0,0), (-1,-1), 6),
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
]

def full_box(rows, bg, border, cw=None):
    """Single-column boxed block — NO nested tables inside cells."""
    t = Table(rows, colWidths=cw or [USABLE])
    t.setStyle(TableStyle(_PAD + [
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX",        (0,0), (-1,-1), 1.0, border),
    ]))
    return t

def data_table(headers, rows):
    """Key-data table with header row."""
    def cell(txt, bold=False):
        txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', str(txt))
        s = S(fontName="Helvetica-Bold" if bold else "Helvetica",
              fontSize=8, textColor=white if bold else P["text"], leading=11)
        return Paragraph(txt, s)

    data = [[cell(h, bold=True) for h in headers]]
    for row in rows:
        data.append([cell(c) for c in row])

    ncols = len(headers)
    cw = [USABLE / ncols] * ncols
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle(_PAD + [
        ("BACKGROUND",    (0,0), (-1,0),  P["blue"]),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [white, P["alt_row"]]),
        ("GRID",          (0,0), (-1,-1), 0.3, P["border"]),
    ]))
    return t

def flat_two_col(left_rows, right_rows, left_w=0.55,
                 left_bg=P["light"], right_bg=P["light"],
                 left_bdr=P["border"], right_bdr=P["border"]):
    """
    True flat two-column layout: no nested tables.
    left_rows / right_rows are lists of Paragraph objects.
    Shorter side is padded with empty cells.
    """
    lw = USABLE * left_w
    rw = USABLE * (1 - left_w)

    n = max(len(left_rows), len(right_rows))
    empty = p("")
    data = []
    for i in range(n):
        l = left_rows[i]  if i < len(left_rows)  else empty
        r = right_rows[i] if i < len(right_rows) else empty
        data.append([l, r])

    t = Table(data, colWidths=[lw, rw])
    cmds = _PAD + [
        ("BACKGROUND", (0,0), (0,-1), left_bg),
        ("BACKGROUND", (1,0), (1,-1), right_bg),
        ("BOX",        (0,0), (0,-1), 1.0, left_bdr),
        ("BOX",        (1,0), (1,-1), 1.0, right_bdr),
        ("LINEAFTER",  (0,0), (0,-1), 0.5, P["border"]),
        ("LEFTPADDING",(1,0), (1,-1), 10),
    ]
    t.setStyle(TableStyle(cmds))
    return t


# ── Topic Card Builder ────────────────────────────────────────────────────────

RELEVANCE_COLOR = {"HIGH": P["red"], "MEDIUM": P["amber"], "LOW": P["grey"]}
RELEVANCE_BG    = {"HIGH": P["red_bg"], "MEDIUM": P["amber_bg"], "LOW": P["light"]}

def build_topic_card(topic):
    """Return a list of ReportLab flowables for one topic."""
    rel   = topic.get("relevance", "MEDIUM").upper()
    color = RELEVANCE_COLOR.get(rel, P["grey"])
    story = []

    # ── 1. HEADER ─────────────────────────────────────────────────────────────
    badge = p(f"  {rel}  ",
              S(fontName="Helvetica-Bold", fontSize=8, textColor=white,
                backColor=color, alignment=TA_CENTER, leading=11))
    title = p(f"<b>{topic['title']}</b>",
              S(fontName="Helvetica-Bold", fontSize=11, textColor=white, leading=14))
    gs    = p(f"<b>{topic.get('gs_paper','')}</b>  {topic.get('subject','')}",
              S(fontSize=8, textColor=HexColor("#cdd8e0"), alignment=TA_RIGHT, leading=12))

    header = Table([[badge, title, gs]],
                   colWidths=[1.9*cm, USABLE - 4.6*cm, 2.7*cm])
    header.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), P["navy"]),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING",   (0,0), (0,-1),  5),
        ("LEFTPADDING",   (1,0), (1,-1),  8),
        ("RIGHTPADDING",  (2,0), (2,-1),  6),
    ]))
    story.append(header)

    # ── 2. NEWS TRIGGER ───────────────────────────────────────────────────────
    if topic.get("news_trigger"):
        story.append(spacer(0.12))
        story.append(full_box([
            [sec_label("📰", "News Trigger", P["news_bdr"])],
            [p(topic["news_trigger"], S(fontSize=9, leading=13))],
        ], P["news_bg"], P["news_bdr"]))

    # ── 3. INTRO & ORIGIN  |  TIMELINE  (flat two-column) ────────────────────
    has_intro    = topic.get("intro") or topic.get("origin")
    has_timeline = bool(topic.get("timeline"))

    if has_intro or has_timeline:
        story.append(spacer(0.12))

        left_rows = [sec_label("📖", "Intro & Origin", P["blue"])]
        if topic.get("intro"):
            left_rows.append(p(topic["intro"], S(fontSize=8.5, leading=13)))
        if topic.get("origin"):
            left_rows.append(p(topic["origin"],
                               S(fontSize=8.5, textColor=P["subtext"],
                                 fontName="Helvetica-Oblique", leading=12)))

        if has_timeline:
            right_rows = [sec_label("🕐", "Timeline", P["blue"])]
            for item in topic["timeline"]:
                yr = item.get("year", "")
                ev = item.get("event", "")
                right_rows.append(p(f"<b>{yr}</b> — {ev}", S(fontSize=8, leading=12)))
            story.append(flat_two_col(left_rows, right_rows, 0.55))
        else:
            story.append(full_box([[r] for r in left_rows], P["light"], P["border"]))

    # ── 4. KEY DATA TABLE ─────────────────────────────────────────────────────
    if topic.get("table"):
        tbl = topic["table"]
        story.append(spacer(0.12))
        story.append(sec_label("📊", "Key Data", P["blue"]))
        story.append(data_table(tbl["headers"], tbl["rows"]))

    # ── 5. STATIC THEORY ──────────────────────────────────────────────────────
    if topic.get("static_theory"):
        story.append(spacer(0.12))
        rows = [[sec_label("📚", "Static Theory", P["blue"])]]
        for pt in topic["static_theory"]:
            rows.append([p(f"• {pt}", S(fontSize=8.5, leading=13))])
        story.append(full_box(rows, P["light"], P["border"]))

    # ── 6. MUST-KNOW FACTS  |  UPSC TRAPS  (flat two-column) ─────────────────
    facts = topic.get("must_know_facts", [])
    traps = topic.get("traps", [])

    if facts or traps:
        story.append(spacer(0.12))

        left_rows = [sec_label("✅", "Must-Know Facts", P["green"])]
        for i, f in enumerate(facts, 1):
            left_rows.append(p(f"<b>{i}.</b> {f}",
                               S(fontSize=8.5, textColor=P["green"], leading=13)))

        right_rows = [sec_label("⚠️ ", "UPSC Traps", P["red"])]
        for tr in traps:
            w = tr.get("wrong", "")
            c = tr.get("correct", "")
            right_rows.append(p(f"<b>✗</b> {w}",
                               S(fontSize=8, textColor=P["red"], leading=12)))
            right_rows.append(p(f"<b>✓</b> {c}",
                               S(fontSize=8, textColor=P["green"], leading=12,
                                 spaceAfter=3)))

        story.append(flat_two_col(
            left_rows, right_rows, 0.55,
            left_bg=P["green_bg"], right_bg=P["red_bg"],
            left_bdr=P["green"],   right_bdr=P["red"],
        ))

    # ── 7. MAINS ANGLE  |  STATIC STUDY LINK  (flat two-column) ─────────────
    mains = topic.get("mains_angle", "")
    link  = topic.get("static_link", "")

    if mains or link:
        story.append(spacer(0.12))
        left_rows  = [
            sec_label("📝", "Mains Angle", P["navy"]),
            p(mains, S(fontSize=8.5, leading=13, fontName="Helvetica-Oblique")),
        ]
        right_rows = [
            sec_label("🔗", "Study Link", P["amber"]),
            p(link, S(fontSize=8.5, textColor=P["amber"], leading=13)),
        ]
        story.append(flat_two_col(
            left_rows, right_rows, 0.60,
            left_bg=P["light"],     right_bg=P["amber_bg"],
            left_bdr=P["border"],   right_bdr=P["amber"],
        ))

    story.append(spacer(0.4))
    story.append(HRFlowable(width="100%", thickness=0.5, color=P["border"], spaceAfter=2))
    return story


# ── Page template ─────────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(P["navy"])
    canvas.rect(0, 0, W, 0.85*cm, fill=1, stroke=0)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(white)
    canvas.drawString(1.8*cm, 0.3*cm,
        "UPSC Register Notes  |  Copilot CLI UPSC Agent  |  For personal study only")
    canvas.drawRightString(W - 1.8*cm, 0.3*cm, f"Page {doc.page}")
    canvas.restoreState()


# ── Main PDF builder ──────────────────────────────────────────────────────────
def build_pdf(data: dict, out_path: str):
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.8*cm, bottomMargin=1.5*cm,
        title=data.get("title", "UPSC Register Notes"),
        author="UPSC Agent / Copilot CLI",
    )

    story = []

    # ── Cover page ────────────────────────────────────────────────────────────
    story.append(spacer(2.0))
    cover = Table([[p(data.get("title", "UPSC Register Notes"), TITLE_S)]],
                  colWidths=[USABLE])
    cover.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), P["navy"]),
        ("TOPPADDING",    (0,0), (-1,-1), 22),
        ("BOTTOMPADDING", (0,0), (-1,-1), 22),
        ("LEFTPADDING",   (0,0), (-1,-1), 12),
        ("RIGHTPADDING",  (0,0), (-1,-1), 12),
    ]))
    story.append(cover)
    story.append(spacer(0.4))
    for line in data.get("meta", []):
        story.append(p(line, SUB_S))
    story.append(spacer(0.8))
    story.append(HRFlowable(width="100%", thickness=2, color=P["red"], spaceAfter=8))
    story.append(p(
        "Facts from official sources  |  Inferences clearly marked  |  No fabricated data",
        FOOTER_S))
    story.append(PageBreak())

    # ── Topics by relevance group ─────────────────────────────────────────────
    for rel_group in ["HIGH", "MEDIUM", "LOW"]:
        topics = [t for t in data.get("topics", [])
                  if t.get("relevance", "MEDIUM").upper() == rel_group]
        if not topics:
            continue

        color = RELEVANCE_COLOR[rel_group]
        emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}[rel_group]
        banner_s = S(fontName="Helvetica-Bold", fontSize=12, textColor=white,
                     backColor=color, alignment=TA_CENTER, borderPad=6,
                     spaceBefore=8, spaceAfter=10)
        story.append(p(f"{emoji}  {rel_group} UPSC RELEVANCE", banner_s))

        for topic in topics:
            story.extend(build_topic_card(topic))

    story.append(spacer(0.8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=P["red"], spaceAfter=6))
    story.append(p("End of Register Notes — UPSC Agent / Copilot CLI", FOOTER_S))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF saved: {out_path}")
    return out_path


# ── CLI entry ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/upsc_register_pdf.py <data_module.py> [out.pdf]")
        sys.exit(1)

    data_path = sys.argv[1]
    out_path  = (sys.argv[2] if len(sys.argv) > 2
                 else data_path.replace("_data.py", ".pdf").replace(".py", ".pdf"))

    spec   = importlib.util.spec_from_file_location("data", data_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    build_pdf(module.DATA, out_path)
