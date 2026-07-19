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
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import Color, HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import (
    Circle, Drawing, Line, Polygon, Rect, String,
)
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    CondPageBreak, HRFlowable, KeepTogether, PageBreak,
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

W, H = A4
USABLE = W - 4*cm   # usable width between margins

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"
FONT_BOLD_ITALIC = "Helvetica-BoldOblique"

_font_sets = [
    (
        Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\arialbd.ttf"),
        Path(r"C:\Windows\Fonts\ariali.ttf"),
        Path(r"C:\Windows\Fonts\arialbi.ttf"),
    ),
    (
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf"),
    ),
]

for regular, bold, italic, bold_italic in _font_sets:
    if all(path.exists() for path in (regular, bold, italic, bold_italic)):
        pdfmetrics.registerFont(TTFont("NotesSans", str(regular)))
        pdfmetrics.registerFont(TTFont("NotesSans-Bold", str(bold)))
        pdfmetrics.registerFont(TTFont("NotesSans-Italic", str(italic)))
        pdfmetrics.registerFont(TTFont("NotesSans-BoldItalic", str(bold_italic)))
        pdfmetrics.registerFontFamily(
            "NotesSans",
            normal="NotesSans",
            bold="NotesSans-Bold",
            italic="NotesSans-Italic",
            boldItalic="NotesSans-BoldItalic",
        )
        FONT_REGULAR = "NotesSans"
        FONT_BOLD = "NotesSans-Bold"
        FONT_ITALIC = "NotesSans-Italic"
        FONT_BOLD_ITALIC = "NotesSans-BoldItalic"
        break

# ── Palette ───────────────────────────────────────────────────────────────────
P = {
    "navy":      HexColor("#17233C"),
    "navy_2":    HexColor("#22345A"),
    "blue":      HexColor("#245B91"),
    "red":       HexColor("#C94B50"),
    "red_bg":    HexColor("#FFF4F3"),
    "amber":     HexColor("#D28B21"),
    "amber_bg":  HexColor("#FFF8E8"),
    "green":     HexColor("#24815D"),
    "green_bg":  HexColor("#EEF9F3"),
    "grey":      HexColor("#7A8494"),
    "border":    HexColor("#DCE2EA"),
    "border_2":  HexColor("#C7D0DC"),
    "alt_row":   HexColor("#F5F7FA"),
    "light":     HexColor("#F8FAFC"),
    "paper":     HexColor("#FCFDFE"),
    "news_bg":   HexColor("#EEF6FD"),
    "news_bdr":  HexColor("#3B82B8"),
    "purple":    HexColor("#76549A"),
    "purple_bg": HexColor("#F6F1FA"),
    "teal":      HexColor("#168373"),
    "teal_bg":   HexColor("#ECF8F5"),
    "text":      HexColor("#26364A"),
    "subtext":   HexColor("#5F6F82"),
}

# ── Style factory ─────────────────────────────────────────────────────────────
def S(name="", **kw):
    defaults = dict(fontName=FONT_REGULAR, fontSize=9.25, textColor=P["text"],
                    leading=13.5, spaceAfter=2, spaceBefore=0)
    defaults.update(kw)
    return ParagraphStyle(name or f"_s{id(kw)}", **defaults)

TITLE_S  = S("T",  fontName=FONT_BOLD, fontSize=23, textColor=white, alignment=TA_LEFT, leading=28)
SUB_S    = S("SB", fontName=FONT_REGULAR, fontSize=10, textColor=P["subtext"], alignment=TA_CENTER)
BODY_S   = S("B",  fontSize=9.25, leading=13.5)
FOOTER_S = S("FT", fontSize=7.5, textColor=P["grey"], alignment=TA_CENTER)

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
    return p(title.upper(),
             S(fontName=FONT_BOLD, fontSize=9.25, textColor=color,
               leading=11.5, spaceBefore=2, spaceAfter=2))

# ── Table builders ────────────────────────────────────────────────────────────

def _ts(*cmds):
    return TableStyle(list(cmds))

_PAD = [
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
]

def full_box(rows, bg, border, cw=None, treatment="rail"):
    """Single-column panel with editorial rather than worksheet-style borders."""
    t = Table(rows, colWidths=cw or [USABLE])
    commands = _PAD + [("BACKGROUND", (0,0), (-1,-1), bg)]
    if treatment == "outline":
        commands.append(("BOX", (0,0), (-1,-1), 0.75, border))
    elif treatment == "rail":
        commands.extend([
            ("LINEBEFORE", (0,0), (0,-1), 3.0, border),
            ("LINEABOVE", (0,0), (-1,0), 0.35, P["border"]),
            ("LINEBELOW", (0,-1), (-1,-1), 0.35, P["border"]),
        ])
    t.setStyle(TableStyle(commands))
    return KeepTogether([t])

def data_table(headers, rows):
    """Key-data table with header row."""
    def cell(txt, bold=False):
        txt = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', str(txt))
        s = S(fontName=FONT_BOLD if bold else FONT_REGULAR,
              fontSize=8.6, textColor=white if bold else P["text"], leading=11.5)
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
        ("LINEBELOW",     (0,0), (-1,-1), 0.35, P["border"]),
        ("LINEABOVE",     (0,0), (-1,0), 0.7, P["blue"]),
        ("BOTTOMPADDING", (0,0), (-1,0), 6),
        ("TOPPADDING",    (0,0), (-1,0), 6),
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
        ("BOX",        (0,0), (-1,-1), 0.65, P["border_2"]),
        ("LINEBEFORE", (0,0), (0,-1), 3.0, left_bdr),
        ("LINEBEFORE", (1,0), (1,-1), 3.0, right_bdr),
        ("LINEAFTER",  (0,0), (0,-1), 0.5, P["border_2"]),
        ("LEFTPADDING",(1,0), (1,-1), 10),
    ]
    t.setStyle(TableStyle(cmds))
    return KeepTogether([t])


def concept_map(spec):
    """Two-level visual mind map with a central idea and linked branches."""
    center = spec.get("center", "")
    branches = spec.get("branches", [])
    story = [sec_label("🧠", spec.get("title", "Concept Map"), P["purple"])]

    center_box = Table(
        [[p(f"<b>{center}</b>",
            S(fontName=FONT_BOLD, fontSize=10, textColor=white,
              alignment=TA_CENTER, leading=14))]],
        colWidths=[USABLE * 0.62],
        hAlign="CENTER",
    )
    center_box.setStyle(TableStyle(_PAD + [
        ("BACKGROUND", (0,0), (-1,-1), P["purple"]),
        ("BOX",        (0,0), (-1,-1), 0.6, P["purple"]),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    story.extend([center_box, p("↓", S(fontSize=15, textColor=P["purple"],
                                       alignment=TA_CENTER, leading=16))])

    cells = []
    for branch in branches:
        if isinstance(branch, dict):
            title = branch.get("title", "")
            text = branch.get("text", "")
            cells.append(p(f"<b>{title}</b><br/>{text}",
                           S(fontSize=8.2, leading=11, alignment=TA_CENTER)))
        else:
            cells.append(p(str(branch), S(fontSize=8.2, leading=11,
                                          alignment=TA_CENTER)))

    if len(cells) % 2:
        cells.append(p(""))
    rows = [cells[i:i+2] for i in range(0, len(cells), 2)]
    if rows:
        branches_table = Table(rows, colWidths=[USABLE / 2] * 2)
        branches_table.setStyle(TableStyle(_PAD + [
            ("BACKGROUND",    (0,0), (-1,-1), P["purple_bg"]),
            ("BOX",           (0,0), (-1,-1), 0.6, P["border_2"]),
            ("INNERGRID",     (0,0), (-1,-1), 0.35, P["border"]),
            ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING",    (0,0), (-1,-1), 7),
            ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ]))
        story.append(branches_table)
    return [KeepTogether(story)]


def flow_diagram(spec):
    """Vertical process diagram for causal chains and answer logic."""
    steps = spec.get("steps", [])
    story = [sec_label("🔄", spec.get("title", "Flow Diagram"), P["teal"])]
    for i, step in enumerate(steps, 1):
        if isinstance(step, dict):
            title = step.get("title", f"Step {i}")
            text = step.get("text", "")
            content = f"<b>{i}. {title}</b><br/>{text}"
        else:
            content = f"<b>{i}.</b> {step}"

        box = Table(
            [[p(content, S(fontSize=8.5, leading=12, alignment=TA_CENTER))]],
            colWidths=[USABLE * 0.78],
            hAlign="CENTER",
        )
        box.setStyle(TableStyle(_PAD + [
            ("BACKGROUND", (0,0), (-1,-1), P["teal_bg"]),
            ("BOX",        (0,0), (-1,-1), 0.6, P["border_2"]),
            ("LINEBEFORE", (0,0), (0,-1), 3.0, P["teal"]),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ]))
        story.append(box)
        if i < len(steps):
            story.append(p("↓", S(fontSize=13, textColor=P["teal"],
                                  alignment=TA_CENTER, leading=14)))
    return [KeepTogether(story)]


def link_map(spec):
    """Show how a topic connects to other doctrines and answer uses."""
    rows = spec.get("rows", [])
    if not rows:
        return []
    return [KeepTogether([
        sec_label("🔗", spec.get("title", "Concept Links"), P["amber"]),
        data_table(
            spec.get("headers", ["Core Concept", "Linked Concept", "Why It Matters"]),
            rows,
        ),
    ])]


def _draw_lines(drawing, lines, x, y, width, color, font_size=7.3,
                align="start", leading=10, bold_first=False):
    """Draw short wrapped lines inside a vector visual."""
    wrapped = []
    for line in lines:
        words = str(line).split()
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            font_name = FONT_BOLD if bold_first and not wrapped else FONT_REGULAR
            if pdfmetrics.stringWidth(candidate, font_name, font_size) <= width:
                current = candidate
            else:
                if current:
                    wrapped.append(current)
                current = word
        if current:
            wrapped.append(current)

    anchor = {"start": "start", "middle": "middle", "end": "end"}[align]
    for index, line in enumerate(wrapped):
        drawing.add(String(
            x, y - index * leading, line,
            fontName=FONT_BOLD if bold_first and index == 0 else FONT_REGULAR,
            fontSize=font_size, fillColor=color, textAnchor=anchor,
        ))


def venn_diagram(spec):
    """Comparison lens with bounded detail cards for content-safe text."""
    width, height = USABLE, 174
    drawing = Drawing(width, height)
    left_x, right_x, cy, radius = width * 0.39, width * 0.61, 80, 68
    drawing.add(Circle(
        left_x, cy, radius,
        fillColor=Color(0.46, 0.33, 0.60, alpha=0.16),
        strokeColor=P["purple"], strokeWidth=1.35,
    ))
    drawing.add(Circle(
        right_x, cy, radius,
        fillColor=Color(0.09, 0.51, 0.45, alpha=0.15),
        strokeColor=P["teal"], strokeWidth=1.35,
    ))
    drawing.add(String(
        left_x - 60, 159, spec.get("left_title", "Position A"),
        fontName=FONT_BOLD, fontSize=10.5, fillColor=P["purple"],
        textAnchor="middle",
    ))
    drawing.add(String(
        right_x + 60, 159, spec.get("right_title", "Position B"),
        fontName=FONT_BOLD, fontSize=10.5, fillColor=P["teal"],
        textAnchor="middle",
    ))
    drawing.add(String(
        width / 2, 151, spec.get("shared_title", "SHARED"),
        fontName=FONT_BOLD, fontSize=8.5, fillColor=P["blue"],
        textAnchor="middle",
    ))
    drawing.add(String(
        left_x - 34, 78, "DISTINCT",
        fontName=FONT_BOLD, fontSize=8, fillColor=P["purple"],
        textAnchor="middle",
    ))
    drawing.add(String(
        width / 2, 78, "OVERLAP",
        fontName=FONT_BOLD, fontSize=8, fillColor=P["blue"],
        textAnchor="middle",
    ))
    drawing.add(String(
        right_x + 34, 78, "DISTINCT",
        fontName=FONT_BOLD, fontSize=8, fillColor=P["teal"],
        textAnchor="middle",
    ))

    def detail_cell(title, items, color):
        cell = [p(title, S(fontName=FONT_BOLD, fontSize=8.5,
                           textColor=color, alignment=TA_CENTER, leading=11))]
        cell.extend(
            p(f"• {item}", S(fontSize=8, leading=10.5, alignment=TA_LEFT))
            for item in items
        )
        return cell

    details = Table([[
        detail_cell(spec.get("left_title", "Position A"), spec.get("left", []), P["purple"]),
        detail_cell(spec.get("shared_title", "Shared"), spec.get("shared", []), P["blue"]),
        detail_cell(spec.get("right_title", "Position B"), spec.get("right", []), P["teal"]),
    ]], colWidths=[USABLE * 0.34, USABLE * 0.32, USABLE * 0.34])
    details.setStyle(TableStyle(_PAD + [
        ("BACKGROUND", (0,0), (0,0), P["purple_bg"]),
        ("BACKGROUND", (1,0), (1,0), P["news_bg"]),
        ("BACKGROUND", (2,0), (2,0), P["teal_bg"]),
        ("BOX", (0,0), (-1,-1), 0.65, P["border_2"]),
        ("LINEAFTER", (0,0), (1,0), 0.45, P["border_2"]),
        ("LINEBEFORE", (0,0), (0,0), 3.0, P["purple"]),
        ("LINEBEFORE", (1,0), (1,0), 3.0, P["blue"]),
        ("LINEBEFORE", (2,0), (2,0), 3.0, P["teal"]),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    return [KeepTogether([
        sec_label("", spec.get("title", "Venn Comparison"), P["purple"]),
        drawing,
        details,
        p(spec.get("caption", ""),
          S(fontSize=7.5, textColor=P["subtext"], alignment=TA_CENTER,
            fontName=FONT_ITALIC)),
    ])]


def visual_timeline(spec):
    """Horizontal timeline with alternating labels."""
    events = spec.get("events", [])
    width, height = USABLE, 194
    drawing = Drawing(width, height)
    margin = 48
    y = 94
    drawing.add(Line(margin, y, width - margin, y,
                     strokeColor=P["blue"], strokeWidth=2))
    count = max(len(events), 1)
    for index, event in enumerate(events):
        x = margin + index * ((width - 2 * margin) / max(count - 1, 1))
        drawing.add(Circle(x, y, 7, fillColor=P["amber"],
                           strokeColor=white, strokeWidth=2))
        above = index % 2 == 0
        end_y = 145 if above else 38
        drawing.add(Line(x, y + (6 if above else -6), x,
                         end_y - (8 if above else -8),
                         strokeColor=P["border"], strokeWidth=1))
        label_y = 174 if above else 32
        drawing.add(String(
            x, label_y, str(event.get("period", "")),
            fontName=FONT_BOLD, fontSize=8.5, fillColor=P["blue"],
            textAnchor="middle",
        ))
        _draw_lines(
            drawing, [event.get("event", "")], x,
            label_y - 13, 92, P["text"], font_size=7.5,
            align="middle", leading=9,
        )
    return [KeepTogether([
        sec_label("", spec.get("title", "Timeline"), P["blue"]),
        drawing,
    ])]


def philosopher_illustration(spec):
    """Stylised vector medallions; illustrative, not claimed likenesses."""
    people = spec.get("people", [])[:2]
    width, height = USABLE, 218
    drawing = Drawing(width, height)
    panel_w = width / max(len(people), 1)
    for index, person in enumerate(people):
        x0 = index * panel_w + 8
        cx = x0 + panel_w / 2 - 8
        color = P["purple"] if index == 0 else P["teal"]
        bg = P["purple_bg"] if index == 0 else P["teal_bg"]
        drawing.add(Rect(
            x0, 10, panel_w - 16, 194, rx=12, ry=12,
            fillColor=bg, strokeColor=P["border_2"], strokeWidth=0.75,
        ))
        drawing.add(Rect(x0, 194, panel_w - 16, 10, rx=12, ry=12,
                         fillColor=color, strokeColor=color))
        drawing.add(Circle(cx, 128, 36, fillColor=Color(0.85, 0.76, 0.62),
                           strokeColor=color, strokeWidth=1.5))
        drawing.add(Polygon(
            [cx - 58, 50, cx - 34, 92, cx, 101,
             cx + 34, 92, cx + 58, 50],
            fillColor=Color(0.82, 0.84, 0.88),
            strokeColor=color, strokeWidth=1,
        ))
        drawing.add(Line(cx - 16, 132, cx - 5, 132,
                         strokeColor=P["navy"], strokeWidth=1))
        drawing.add(Line(cx + 5, 132, cx + 16, 132,
                         strokeColor=P["navy"], strokeWidth=1))
        drawing.add(Line(cx - 8, 116, cx + 8, 116,
                         strokeColor=P["navy"], strokeWidth=1))
        drawing.add(String(
            cx, 175, person.get("name", ""),
            fontName=FONT_BOLD, fontSize=11, fillColor=color,
            textAnchor="middle",
        ))
        drawing.add(String(
            cx, 24, person.get("label", "Illustrative profile"),
            fontName=FONT_ITALIC, fontSize=7.5, fillColor=P["subtext"],
            textAnchor="middle",
        ))
    return [KeepTogether([
        sec_label("", spec.get("title", "Illustrative Profiles"), P["amber"]),
        drawing,
        p("Stylised study illustrations, not historical likenesses.",
          S(fontSize=7, textColor=P["grey"], alignment=TA_CENTER,
            fontName=FONT_ITALIC)),
    ])]


def argument_tree(spec):
    """Root claim with branching objections or consequences."""
    branches = spec.get("branches", [])[:4]
    width, height = USABLE, 248
    drawing = Drawing(width, height)
    root_x, root_y, root_w, root_h = width / 2 - 112, 190, 224, 46
    drawing.add(Rect(root_x, root_y, root_w, root_h, rx=7, ry=7,
                     fillColor=P["purple"], strokeColor=P["purple"]))
    _draw_lines(drawing, [spec.get("root", "Root claim")], width / 2,
                root_y + 27, root_w - 20, white, font_size=8.2,
                align="middle", leading=10, bold_first=True)
    child_w = (width - 30) / max(len(branches), 1) - 8
    for index, branch in enumerate(branches):
        x = 15 + index * ((width - 30) / max(len(branches), 1))
        cx = x + child_w / 2
        drawing.add(Line(width / 2, root_y, cx, 122,
                         strokeColor=P["border_2"], strokeWidth=1.2))
        drawing.add(Rect(x, 28, child_w, 92, rx=8, ry=8,
                         fillColor=P["light"], strokeColor=P["border_2"],
                         strokeWidth=0.75))
        drawing.add(Rect(x, 112, child_w, 8, rx=8, ry=8,
                         fillColor=P["blue"], strokeColor=P["blue"]))
        _draw_lines(
            drawing,
            [branch.get("title", ""), branch.get("text", "")],
            cx, 101, child_w - 14, P["text"], font_size=7.6,
            align="middle", leading=9, bold_first=True,
        )
    return [KeepTogether([
        sec_label("", spec.get("title", "Argument Tree"), P["purple"]),
        drawing,
    ])]


def bar_chart(spec):
    """Simple labelled horizontal bar chart."""
    items = spec.get("items", [])
    width = USABLE
    height = max(135, 48 + len(items) * 32)
    drawing = Drawing(width, height)
    max_value = max([item.get("value", 0) for item in items] or [1])
    label_w = 145
    bar_w = width - label_w - 52
    for index, item in enumerate(items):
        y = height - 40 - index * 32
        value = item.get("value", 0)
        fill_w = bar_w * value / max_value if max_value else 0
        drawing.add(String(
            6, y + 4, item.get("label", ""),
            fontName=FONT_BOLD, fontSize=8, fillColor=P["text"],
        ))
        drawing.add(Rect(label_w, y, bar_w, 15, rx=7, ry=7,
                         fillColor=P["alt_row"], strokeColor=P["border"]))
        drawing.add(Rect(label_w, y, fill_w, 15, rx=7, ry=7,
                         fillColor=P["teal"], strokeColor=P["teal"]))
        drawing.add(String(
            label_w + fill_w + 6, y + 3, str(value),
            fontName=FONT_BOLD, fontSize=8, fillColor=P["blue"],
        ))
    return [KeepTogether([
        sec_label("", spec.get("title", "Chart"), P["teal"]),
        drawing,
        p(spec.get("caption", ""),
          S(fontSize=7.5, textColor=P["subtext"], alignment=TA_CENTER,
            fontName=FONT_ITALIC)),
    ])]


def labeled_diagram(spec):
    """Central object with four labelled explanatory dimensions."""
    nodes = spec.get("nodes", [])[:4]
    width, height = USABLE, 245
    drawing = Drawing(width, height)
    cx, cy = width / 2, 120
    drawing.add(Circle(cx, cy, 48, fillColor=P["amber_bg"],
                       strokeColor=P["amber"], strokeWidth=1.35))
    _draw_lines(drawing, [spec.get("center", "Object")], cx, cy + 8, 76,
                P["amber"], font_size=8.5, align="middle",
                leading=10, bold_first=True)
    positions = [
        (18, 166), (width - 168, 166), (18, 20), (width - 168, 20),
    ]
    for node, (x, y) in zip(nodes, positions):
        box_w, box_h = 150, 58
        target_x = x + box_w / 2
        target_y = y + box_h / 2
        drawing.add(Line(cx, cy, target_x, target_y,
                         strokeColor=P["border"], strokeWidth=1.2))
        drawing.add(Rect(x, y, box_w, box_h, rx=8, ry=8,
                         fillColor=P["light"], strokeColor=P["border_2"],
                         strokeWidth=0.75))
        drawing.add(Rect(x, y + box_h - 7, box_w, 7, rx=8, ry=8,
                         fillColor=P["blue"], strokeColor=P["blue"]))
        _draw_lines(
            drawing,
            [node.get("title", ""), node.get("text", "")],
            target_x, y + 42, box_w - 14, P["text"], font_size=7.7,
            align="middle", leading=9, bold_first=True,
        )
    return [KeepTogether([
        sec_label("", spec.get("title", "Labelled Diagram"), P["amber"]),
        drawing,
    ])]


def cover_concept_visual(title):
    """Topic-led visual metaphor that turns cover whitespace into a recall map."""
    width, height = USABLE, 260
    drawing = Drawing(width, height)
    cx, cy = width / 2, 130
    words = [
        word.strip("—–-,:;()[]")
        for word in str(title).split()
        if len(word.strip("—–-,:;()[]")) > 3
    ][:3] or ["PHILOSOPHY"]

    drawing.add(Circle(cx, cy, 56, fillColor=P["navy"],
                       strokeColor=P["amber"], strokeWidth=2))
    _draw_lines(drawing, words, cx, cy + 15, 88, white,
                font_size=10, align="middle", leading=13, bold_first=True)

    nodes = [
        ("CONCEPT", "What is being claimed?", 26, 174, P["purple"], P["purple_bg"]),
        ("ARGUMENT", "Why should it be accepted?", width - 176, 174, P["teal"], P["teal_bg"]),
        ("CRITIQUE", "Where does it fail?", 26, 35, P["red"], P["red_bg"]),
        ("JUDGEMENT", "What should the answer conclude?", width - 176, 35, P["amber"], P["amber_bg"]),
    ]
    for label, prompt, x, y, color, bg in nodes:
        box_w, box_h = 150, 58
        tx, ty = x + box_w / 2, y + box_h / 2
        drawing.add(Line(cx, cy, tx, ty, strokeColor=P["border_2"], strokeWidth=1.1))
        drawing.add(Rect(x, y, box_w, box_h, rx=10, ry=10,
                         fillColor=bg, strokeColor=P["border_2"], strokeWidth=0.7))
        drawing.add(Rect(x, y + box_h - 7, box_w, 7, rx=10, ry=10,
                         fillColor=color, strokeColor=color))
        drawing.add(String(tx, y + 34, label, fontName=FONT_BOLD,
                           fontSize=8.5, fillColor=color, textAnchor="middle"))
        _draw_lines(drawing, [prompt], tx, y + 20, box_w - 18,
                    P["subtext"], font_size=7.4, align="middle", leading=9)
    return drawing


# ── Topic Card Builder ────────────────────────────────────────────────────────

RELEVANCE_COLOR = {"HIGH": P["red"], "MEDIUM": P["amber"], "LOW": P["grey"]}
RELEVANCE_BG    = {"HIGH": P["red_bg"], "MEDIUM": P["amber_bg"], "LOW": P["light"]}

def build_topic_card(topic):
    """Return a list of ReportLab flowables for one topic."""
    rel   = topic.get("relevance", "MEDIUM").upper()
    color = RELEVANCE_COLOR.get(rel, P["grey"])
    story = []
    story.append(CondPageBreak(5.6 * cm))

    # ── 1. HEADER ─────────────────────────────────────────────────────────────
    badge = p(f"{rel}",
              S(fontName=FONT_BOLD, fontSize=8, textColor=white,
                alignment=TA_CENTER, leading=11))
    title = p(f"<b>{topic['title']}</b>",
              S(fontName=FONT_BOLD, fontSize=13, textColor=white, leading=16))
    gs    = p(f"<b>{topic.get('gs_paper','')}</b>  {topic.get('subject','')}",
              S(fontSize=8, textColor=HexColor("#cdd8e0"), alignment=TA_RIGHT, leading=12))

    header = Table([[badge, title, gs]],
                   colWidths=[1.9*cm, USABLE - 4.6*cm, 2.7*cm])
    header.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), P["navy"]),
        ("BACKGROUND",    (0,0), (0,-1), color),
        ("LINEBELOW",     (0,0), (-1,-1), 2.2, color),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 9),
        ("BOTTOMPADDING", (0,0), (-1,-1), 9),
        ("LEFTPADDING",   (0,0), (0,-1),  7),
        ("RIGHTPADDING",  (0,0), (0,-1),  7),
        ("LEFTPADDING",   (1,0), (1,-1),  11),
        ("RIGHTPADDING",  (2,0), (2,-1),  8),
    ]))
    story.append(header)

    # ── 2. NEWS TRIGGER ───────────────────────────────────────────────────────
    if topic.get("news_trigger"):
        story.append(spacer(0.12))
        story.append(full_box([
            [sec_label("📰", "News Trigger", P["news_bdr"])],
            [p(topic["news_trigger"], S(fontSize=9, leading=13))],
        ], P["news_bg"], P["news_bdr"], treatment="rail"))

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
                                 fontName=FONT_ITALIC, leading=12)))

        if has_timeline:
            right_rows = [sec_label("🕐", "Timeline", P["blue"])]
            for item in topic["timeline"]:
                yr = item.get("year", "")
                ev = item.get("event", "")
                right_rows.append(p(f"<b>{yr}</b> — {ev}", S(fontSize=8, leading=12)))
            story.append(flat_two_col(left_rows, right_rows, 0.55))
        else:
            story.append(full_box([[r] for r in left_rows], P["light"], P["blue"]))

    # ── 4. CONCEPT MAP ────────────────────────────────────────────────────────
    if topic.get("concept_map"):
        story.append(spacer(0.12))
        story.extend(concept_map(topic["concept_map"]))

    if topic.get("illustration"):
        story.append(spacer(0.12))
        story.extend(philosopher_illustration(topic["illustration"]))

    if topic.get("visual_timeline"):
        story.append(spacer(0.12))
        story.extend(visual_timeline(topic["visual_timeline"]))

    if topic.get("venn_diagram"):
        story.append(spacer(0.12))
        story.extend(venn_diagram(topic["venn_diagram"]))

    if topic.get("labeled_diagram"):
        story.append(spacer(0.12))
        story.extend(labeled_diagram(topic["labeled_diagram"]))

    if topic.get("argument_tree"):
        story.append(spacer(0.12))
        story.extend(argument_tree(topic["argument_tree"]))

    if topic.get("chart"):
        story.append(spacer(0.12))
        story.extend(bar_chart(topic["chart"]))

    # ── 5. KEY DATA TABLE ─────────────────────────────────────────────────────
    if topic.get("table"):
        tbl = topic["table"]
        story.append(spacer(0.12))
        story.append(KeepTogether([
            sec_label("📊", "Key Data", P["blue"]),
            data_table(tbl["headers"], tbl["rows"]),
        ]))

    # ── 6. FLOW DIAGRAM ───────────────────────────────────────────────────────
    if topic.get("flow_diagram"):
        story.append(spacer(0.12))
        story.extend(flow_diagram(topic["flow_diagram"]))

    # ── 7. STATIC THEORY ──────────────────────────────────────────────────────
    if topic.get("static_theory"):
        story.append(spacer(0.12))
        rows = [[sec_label("📚", "Static Theory", P["blue"])]]
        for pt in topic["static_theory"]:
            rows.append([p(f"• {pt}", S(fontSize=8.5, leading=13))])
        story.append(full_box(rows, P["light"], P["blue"]))

    # ── 8. MEMORY HOOK ────────────────────────────────────────────────────────
    if topic.get("memory_hook"):
        story.append(spacer(0.12))
        story.append(full_box([
            [sec_label("🔑", "Memory Hook", P["purple"])],
            [p(topic["memory_hook"],
               S(fontName=FONT_BOLD, fontSize=9, textColor=P["purple"],
                 leading=13, alignment=TA_CENTER))],
        ], P["purple_bg"], P["purple"], treatment="outline"))

    # ── 9. MUST-KNOW FACTS  |  UPSC TRAPS  (flat two-column) ─────────────────
    facts = topic.get("must_know_facts", [])
    traps = topic.get("traps", [])

    if facts or traps:
        story.append(CondPageBreak(6.5 * cm))
        story.append(spacer(0.12))

        left_rows = [sec_label("✅", "Must-Know Facts", P["green"])]
        for i, f in enumerate(facts, 1):
            left_rows.append(p(f"<b>{i}.</b> {f}",
                               S(fontSize=8.5, textColor=P["green"], leading=13)))

        right_rows = [sec_label("⚠️ ", "UPSC Traps", P["red"])]
        for tr in traps:
            w = tr.get("wrong", "")
            c = tr.get("correct", "")
            right_rows.append(p(f"<b>WRONG:</b> {w}",
                               S(fontSize=8, textColor=P["red"], leading=12)))
            right_rows.append(p(f"<b>CORRECT:</b> {c}",
                               S(fontSize=8, textColor=P["green"], leading=12,
                                 spaceAfter=3)))

        if facts and traps:
            panel = Table([[left_rows, right_rows]],
                          colWidths=[USABLE * 0.55, USABLE * 0.45])
            panel.setStyle(TableStyle(_PAD + [
                ("BACKGROUND", (0,0), (0,0), P["green_bg"]),
                ("BACKGROUND", (1,0), (1,0), P["red_bg"]),
                ("BOX", (0,0), (-1,-1), 0.65, P["border_2"]),
                ("LINEBEFORE", (0,0), (0,0), 3.0, P["green"]),
                ("LINEBEFORE", (1,0), (1,0), 3.0, P["red"]),
                ("LINEAFTER", (0,0), (0,0), 0.5, P["border_2"]),
                ("LEFTPADDING", (1,0), (1,0), 10),
            ]))
            story.append(KeepTogether([panel]))
        elif facts:
            story.append(full_box(
                [[row] for row in left_rows], P["green_bg"], P["green"]))
        else:
            story.append(full_box(
                [[row] for row in right_rows], P["red_bg"], P["red"]))

    # ── 10. CONCEPT LINKS ────────────────────────────────────────────────────
    if topic.get("link_map"):
        story.append(spacer(0.12))
        story.extend(link_map(topic["link_map"]))

    # ── 11. MAINS ANGLE  |  STATIC STUDY LINK  (flat two-column) ─────────────
    mains = topic.get("mains_angle", "")
    link  = topic.get("static_link", "")

    if mains or link:
        story.append(spacer(0.12))
        left_cell = [
            sec_label("📝", "Mains Angle", P["navy"]),
            p(mains, S(fontSize=8.5, leading=13, fontName=FONT_ITALIC)),
        ]
        right_cell = [
            sec_label("🔗", "Study Link", P["amber"]),
            p(link, S(fontSize=8.5, textColor=P["amber"], leading=13)),
        ]
        panel = Table([[left_cell, right_cell]],
                      colWidths=[USABLE * 0.60, USABLE * 0.40])
        panel.setStyle(TableStyle(_PAD + [
            ("BACKGROUND", (0,0), (0,0), P["light"]),
            ("BACKGROUND", (1,0), (1,0), P["amber_bg"]),
            ("BOX", (0,0), (-1,-1), 0.65, P["border_2"]),
            ("LINEBEFORE", (0,0), (0,0), 3.0, P["navy"]),
            ("LINEBEFORE", (1,0), (1,0), 3.0, P["amber"]),
            ("LINEAFTER", (0,0), (0,0), 0.5, P["border_2"]),
            ("LEFTPADDING", (1,0), (1,0), 10),
        ]))
        story.append(KeepTogether([panel]))

    story.append(spacer(0.4))
    story.append(HRFlowable(width="100%", thickness=0.5, color=P["border"], spaceAfter=2))
    return story


# ── Page template ─────────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(P["paper"])
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.setFillColor(P["navy"])
    canvas.rect(0, H - 0.16*cm, W, 0.16*cm, fill=1, stroke=0)
    canvas.setStrokeColor(P["border"])
    canvas.setLineWidth(0.45)
    canvas.line(2*cm, H - 1.02*cm, W - 2*cm, H - 1.02*cm)
    canvas.setFont(FONT_BOLD, 7.2)
    canvas.setFillColor(P["subtext"])
    canvas.drawString(2*cm, H - 0.78*cm, "UPSC PHILOSOPHY OPTIONAL  •  VISUAL REGISTER NOTES")
    canvas.setFillColor(P["navy"])
    canvas.rect(0, 0, W, 0.62*cm, fill=1, stroke=0)
    canvas.setFont(FONT_REGULAR, 7)
    canvas.setFillColor(white)
    canvas.drawString(2*cm, 0.22*cm, "Concept • Critique • Comparison • Answer Writing")
    canvas.setFillColor(P["amber"])
    canvas.circle(W - 2.15*cm, 0.31*cm, 0.18*cm, fill=1, stroke=0)
    canvas.setFont(FONT_BOLD, 6.5)
    canvas.setFillColor(P["navy"])
    canvas.drawCentredString(W - 2.15*cm, 0.235*cm, str(doc.page))
    canvas.restoreState()


# ── Main PDF builder ──────────────────────────────────────────────────────────
def build_pdf(data: dict, out_path: str):
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.35*cm, bottomMargin=1.25*cm,
        title=data.get("title", "UPSC Register Notes"),
        author="UPSC Agent / Copilot CLI",
    )

    story = []

    # ── Cover page ────────────────────────────────────────────────────────────
    story.append(spacer(1.8))
    eyebrow = p("UPSC PHILOSOPHY OPTIONAL",
                S(fontName=FONT_BOLD, fontSize=9, textColor=P["amber"],
                  alignment=TA_LEFT, leading=12))
    cover = Table([[
        [eyebrow, spacer(0.18), p(data.get("title", "UPSC Register Notes"), TITLE_S)]
    ]], colWidths=[USABLE])
    cover.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), P["navy"]),
        ("LINEBEFORE",    (0,0), (0,0), 7, P["amber"]),
        ("TOPPADDING",    (0,0), (-1,-1), 28),
        ("BOTTOMPADDING", (0,0), (-1,-1), 28),
        ("LEFTPADDING",   (0,0), (-1,-1), 22),
        ("RIGHTPADDING",  (0,0), (-1,-1), 18),
    ]))
    story.append(cover)
    story.append(spacer(0.4))
    for line in data.get("meta", []):
        story.append(p(line, SUB_S))
    story.append(spacer(0.35))
    story.append(cover_concept_visual(data.get("title", "UPSC Register Notes")))
    story.append(spacer(0.18))
    story.append(HRFlowable(width="32%", thickness=3, color=P["amber"],
                            hAlign="LEFT", spaceAfter=10))
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
        banner_s = S(fontName=FONT_BOLD, fontSize=12, textColor=white,
                     backColor=color, alignment=TA_CENTER, borderPad=6,
                     spaceBefore=8, spaceAfter=10)
        story.append(p(f"{rel_group} UPSC RELEVANCE", banner_s))

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
