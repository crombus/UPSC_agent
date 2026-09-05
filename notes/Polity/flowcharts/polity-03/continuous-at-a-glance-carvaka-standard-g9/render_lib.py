"""Bespoke rendering primitives for the Polity 01 continuous at-a-glance master flow.

These are reusable primitives only. Every stage's internal layout is authored by hand in
build_g9.py; nothing here imposes a fixed card schema.
"""
from __future__ import annotations

import re
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = r"C:\Windows\Fonts"

# ---------------------------------------------------------------- palette ----
BG = (7, 20, 33)
CARD = (16, 40, 61)
CARD_TITLE = (11, 38, 58)
CARD_EXTRA = (13, 26, 40)
CYAN = (68, 211, 255)
TEAL = (65, 228, 193)
AMBER = (255, 178, 91)
YELLOW = (255, 225, 122)
MAGENTA = (230, 144, 255)
GREEN = (126, 231, 135)
RED = (255, 138, 128)
WHITE = (237, 246, 251)
DIM = (156, 180, 200)
ANSWER_FILL = (43, 37, 55)
GREY = (150, 168, 185)
RULE = (46, 71, 88)

COLOURS = {
    "cyan": CYAN, "teal": TEAL, "amber": AMBER, "yellow": YELLOW,
    "magenta": MAGENTA, "green": GREEN, "red": RED, "white": WHITE,
    "dim": DIM, "grey": GREY,
}


def col(name):
    return COLOURS.get(name, CYAN)


# ------------------------------------------------------------------ fonts ----
def _f(name, size):
    return ImageFont.truetype(FONT_DIR + "\\" + name, size)


class Fonts:
    def __init__(self, scale=1.0):
        s = lambda v: max(8, int(round(v * scale)))
        self.title = _f("segoeuib.ttf", s(72))
        self.subtitle = _f("segoeuib.ttf", s(31))
        self.note = _f("segoeui.ttf", s(27))
        self.stage = _f("segoeuib.ttf", s(55))
        self.stage_sm = _f("segoeuib.ttf", s(45))
        self.badge = _f("segoeuib.ttf", s(25))
        self.pill = _f("segoeuib.ttf", s(29))
        self.head = _f("segoeuib.ttf", s(34))
        self.body = _f("segoeui.ttf", s(30))
        self.bodyb = _f("segoeuib.ttf", s(30))
        self.small = _f("segoeui.ttf", s(27))
        self.smallb = _f("segoeuib.ttf", s(27))
        self.band = _f("segoeui.ttf", s(30))
        self.bandb = _f("segoeuib.ttf", s(30))
        self.chain = _f("segoeuib.ttf", s(29))
        self.chain_sub = _f("segoeui.ttf", s(26))
        self.rail = _f("segoeuib.ttf", s(34))
        self.big = _f("segoeuib.ttf", s(78))
        self.num = _f("segoeuib.ttf", s(52))


# ------------------------------------------------------------ text engine ----
OVERFLOWS = []


def text_w(font, s):
    return font.getlength(s)


def line_h(font):
    a, d = font.getmetrics()
    return a + d


def parse_runs(s, font, bold_font, colour, bold_colour=None):
    """Split '**bold**' markers into styled runs."""
    runs = []
    for i, part in enumerate(re.split(r"\*\*", s)):
        if not part:
            continue
        if i % 2 == 1:
            runs.append((part, bold_font, bold_colour or colour))
        else:
            runs.append((part, font, colour))
    return runs


def wrap_runs(runs, width, tag=""):
    """Greedy wrap of styled runs into lines: list[list[(text, font, colour)]]."""
    lines = [[]]
    cur = 0.0
    for text, font, colour in runs:
        tokens = re.split(r"(\s+)", text)
        for tok in tokens:
            if tok == "":
                continue
            w = text_w(font, tok)
            if tok.strip() == "":
                if cur > 0:
                    lines[-1].append((tok, font, colour))
                    cur += w
                continue
            if cur + w > width and cur > 0:
                lines.append([])
                cur = 0.0
            if w > width:
                OVERFLOWS.append((tag, tok[:40], round(w), round(width)))
            lines[-1].append((tok, font, colour))
            cur += w
    return [ln for ln in lines if ln]


def draw_runs_line(d, x, y, line):
    cx = x
    for text, font, colour in line:
        d.text((cx, y), text, font=font, fill=colour)
        cx += text_w(font, text)
    return cx


# ------------------------------------------------------------- shape utils ----
def rrect(d, box, radius, fill=None, outline=None, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow_right(d, x0, y, x1, colour, thick=5, head=16):
    d.line([(x0, y), (x1 - head, y)], fill=colour, width=thick)
    d.polygon([(x1, y), (x1 - head, y - head * 0.62), (x1 - head, y + head * 0.62)], fill=colour)


def arrow_down(d, x, y0, y1, colour, thick=5, head=16):
    d.line([(x, y0), (x, y1 - head)], fill=colour, width=thick)
    d.polygon([(x, y1), (x - head * 0.62, y1 - head), (x + head * 0.62, y1 - head)], fill=colour)


# ================================================================= blocks ====
class Ctx:
    def __init__(self, fonts):
        self.f = fonts


GAP = 26          # gap between blocks
BUL_IND = 30      # bullet hanging indent
LEAD = 9          # extra leading between wrapped lines
ITEM_GAP = 11     # gap between bullet items


def _bullet_items_h(ctx, items, width, font=None, tag=""):
    f = font or ctx.f.body
    h = 0
    for it in items:
        h += _one_item_h(ctx, it, width, f, tag)
    return max(0, h - ITEM_GAP)


def _item_runs(ctx, it, f):
    fb = ctx.f.bodyb if f is ctx.f.body else ctx.f.smallb
    if isinstance(it, dict):
        runs = [(it["k"], fb, col(it.get("kc", "white")))]
        if it.get("v"):
            runs.append((" " + it["v"], f, DIM if it.get("dim") else WHITE))
        return runs
    return parse_runs(it, f, ctx.f.bodyb if f is ctx.f.body else ctx.f.smallb, WHITE, WHITE)


def _one_item_h(ctx, it, width, f, tag):
    indent = BUL_IND
    lines = wrap_runs(_item_runs(ctx, it, f), width - indent, tag)
    return len(lines) * (line_h(f) + LEAD) + ITEM_GAP


def _draw_bullets(ctx, d, x, y, width, items, colour, font=None, tag=""):
    f = font or ctx.f.body
    lh = line_h(f) + LEAD
    cy = y
    for it in items:
        lines = wrap_runs(_item_runs(ctx, it, f), width - BUL_IND, tag)
        r = 4
        by = cy + lh * 0.42
        d.ellipse([x + 7 - r, by - r, x + 7 + r, by + r], fill=colour)
        for ln in lines:
            draw_runs_line(d, x + BUL_IND, cy, ln)
            cy += lh
        cy += ITEM_GAP
    return cy - ITEM_GAP - y


# ---- column block -----------------------------------------------------------
def _cols_h(ctx, b, width):
    n = len(b["cols"])
    gap = b.get("gap", 40)
    cw = (width - gap * (n - 1)) / n
    hs = []
    for c in b["cols"]:
        h = 0
        if c.get("h"):
            h += line_h(ctx.f.head) + 12
        h += _bullet_items_h(ctx, c["items"], cw, tag=c.get("h", ""))
        hs.append(h)
    return max(hs)


def _cols_draw(ctx, d, b, x, y, width):
    n = len(b["cols"])
    gap = b.get("gap", 40)
    cw = (width - gap * (n - 1)) / n
    total = _cols_h(ctx, b, width)
    for i, c in enumerate(b["cols"]):
        cx = x + i * (cw + gap)
        cy = y
        if i:
            d.line([(cx - gap / 2, y - 6), (cx - gap / 2, y + total + 6)], fill=RULE, width=2)
        if c.get("h"):
            d.text((cx, cy), c["h"], font=ctx.f.head, fill=col(c.get("c", "amber")))
            cy += line_h(ctx.f.head) + 12
        _draw_bullets(ctx, d, cx, cy, cw, c["items"], col(c.get("c", "amber")), tag=c.get("h", ""))
    return total


# ---- pills ------------------------------------------------------------------
def _pill_rows(ctx, pills, width):
    rows, cur, curw = [], [], 0.0
    for p in pills:
        w = text_w(ctx.f.pill, p["t"]) + 44
        if cur and curw + w + 14 > width:
            rows.append(cur)
            cur, curw = [], 0.0
        cur.append((p, w))
        curw += w + 14
    if cur:
        rows.append(cur)
    return rows


def _pills_h(ctx, b, width):
    rows = _pill_rows(ctx, b["pills"], width)
    ph = line_h(ctx.f.pill) + 16
    return len(rows) * (ph + 12) - 12


def _pills_draw(ctx, d, b, x, y, width):
    rows = _pill_rows(ctx, b["pills"], width)
    ph = line_h(ctx.f.pill) + 16
    cy = y
    for row in rows:
        cx = x
        for p, w in row:
            c = col(p.get("c", "cyan"))
            rrect(d, [cx, cy, cx + w, cy + ph], radius=ph / 2, fill=c)
            tw = text_w(ctx.f.pill, p["t"])
            d.text((cx + (w - tw) / 2, cy + 6), p["t"], font=ctx.f.pill, fill=BG)
            cx += w + 14
        cy += ph + 12
    return cy - 12 - y


# ---- chain ------------------------------------------------------------------
def _chain_geom(ctx, b, width):
    per = b.get("per_row", 5)
    items = b["items"]
    rows = [items[i:i + per] for i in range(0, len(items), per)]
    arrow = 46
    boxes = []
    for row in rows:
        n = len(row)
        bw = (width - arrow * (n - 1)) / max(n, 1)
        hs = []
        for it in row:
            h = 20
            h += len(wrap_runs([(it["t"], ctx.f.chain, WHITE)], bw - 28, "chain")) * (line_h(ctx.f.chain) + 4)
            if it.get("s"):
                h += len(wrap_runs([(it["s"], ctx.f.chain_sub, DIM)], bw - 28, "chain")) * (line_h(ctx.f.chain_sub) + 3)
            h += 20
            hs.append(h)
        boxes.append((row, bw, max(hs)))
    return boxes, arrow


def _chain_h(ctx, b, width):
    boxes, _ = _chain_geom(ctx, b, width)
    return sum(h for _, _, h in boxes) + 34 * (len(boxes) - 1)


def _chain_draw(ctx, d, b, x, y, width):
    boxes, arrow = _chain_geom(ctx, b, width)
    cy = y
    for row, bw, bh in boxes:
        cx = x
        for i, it in enumerate(row):
            c = col(it.get("c", "cyan"))
            rrect(d, [cx, cy, cx + bw, cy + bh], radius=14,
                  fill=it.get("fill") and col(it["fill"]) or CARD_TITLE, outline=c, width=3)
            ty = cy + 14
            for ln in wrap_runs([(it["t"], ctx.f.chain, c)], bw - 28, "chain"):
                draw_runs_line(d, cx + 14, ty, ln)
                ty += line_h(ctx.f.chain) + 4
            if it.get("s"):
                for ln in wrap_runs([(it["s"], ctx.f.chain_sub, DIM)], bw - 28, "chain"):
                    draw_runs_line(d, cx + 14, ty, ln)
                    ty += line_h(ctx.f.chain_sub) + 3
            if i < len(row) - 1:
                arrow_right(d, cx + bw + 8, cy + bh / 2, cx + bw + arrow - 8, CYAN)
            cx += bw + arrow
        cy += bh + 34
    return cy - 34 - y


# ---- panels (institution-versus-function split) -----------------------------
def _panels_geom(ctx, b, width):
    n = len(b["panels"])
    midw = 0
    if b.get("mid"):
        midw = 340
    gap = 34
    pw = (width - midw - gap * (n - 1 + (2 if midw else 0))) / n
    return pw, midw, gap


def _panel_h(ctx, p, pw):
    h = 18 + line_h(ctx.f.head) + 14
    if p.get("sub"):
        h += len(wrap_runs([(p["sub"], ctx.f.small, DIM)], pw - 44, "panel")) * (line_h(ctx.f.small) + 4) + 10
    h += _bullet_items_h(ctx, p["items"], pw - 44, tag=p.get("h", ""))
    return h + 20


def _mid_stack(ctx, b, midw):
    """Wrapped centre-label and caption geometry for a panels block."""
    lines = wrap_runs([(b["mid"], ctx.f.smallb, BG)], midw - 28, "mid-label")
    lh = line_h(ctx.f.smallb)
    bh = len(lines) * (lh + 4) + 12
    bw = min(midw, max(sum(text_w(f, t) for t, f, _ in ln) for ln in lines) + 28)
    caption = wrap_runs([(b["mid2"], ctx.f.small, MAGENTA)], midw - 10, "mid") if b.get("mid2") else []
    ch = len(caption) * (line_h(ctx.f.small) + 3)
    return lines, lh, bh, bw, caption, ch


def _panels_h(ctx, b, width):
    pw, midw, gap = _panels_geom(ctx, b, width)
    h = max(_panel_h(ctx, p, pw) for p in b["panels"])
    if midw:
        _, _, bh, _, _, ch = _mid_stack(ctx, b, midw)
        h = max(h, 2 * max(bh + 30, ch + 34) + 16)
    return h


def _panels_draw(ctx, d, b, x, y, width):
    pw, midw, gap = _panels_geom(ctx, b, width)
    total = _panels_h(ctx, b, width)
    cx = x
    for i, p in enumerate(b["panels"]):
        c = col(p.get("c", "cyan"))
        rrect(d, [cx, y, cx + pw, y + total], radius=16, fill=CARD_TITLE, outline=c, width=3)
        hb = line_h(ctx.f.head) + 16
        rrect(d, [cx, y, cx + pw, y + hb], radius=16, fill=c)
        d.rectangle([cx, y + hb - 16, cx + pw, y + hb], fill=c)
        d.text((cx + 20, y + 7), p["h"], font=ctx.f.head, fill=BG)
        ty = y + hb + 14
        if p.get("sub"):
            for ln in wrap_runs([(p["sub"], ctx.f.small, DIM)], pw - 44, "panel"):
                draw_runs_line(d, cx + 22, ty, ln)
                ty += line_h(ctx.f.small) + 4
            ty += 10
        _draw_bullets(ctx, d, cx + 22, ty, pw - 44, p["items"], c, tag=p.get("h", ""))
        if midw and i == 0:
            mx = cx + pw + gap
            lines, lh, bh, bw, caption, ch = _mid_stack(ctx, b, midw)
            arrow_right(d, mx + 6, y + total / 2, mx + midw / 2 - 8, MAGENTA)
            arrow_right(d, mx + midw - 6, y + total / 2, mx + midw / 2 + 8, MAGENTA)
            bx = mx + (midw - bw) / 2
            by = y + total / 2 - 26 - bh
            rrect(d, [bx, by, bx + bw, by + bh], radius=12, fill=MAGENTA)
            yy = by + 6
            for ln in lines:
                lw = sum(text_w(f, t) for t, f, _ in ln)
                draw_runs_line(d, mx + (midw - lw) / 2, yy, ln)
                yy += lh + 4
            yy = y + total / 2 + 26
            for ln in caption:
                lw = sum(text_w(f, t) for t, f, _ in ln)
                draw_runs_line(d, mx + (midw - lw) / 2, yy, ln)
                yy += line_h(ctx.f.small) + 3
            cx += pw + midw + gap * 2
        else:
            cx += pw + gap
    return total


# ---- replace (before / after institutional replacement) ---------------------
def _replace_side_h(ctx, side, w):
    h = 16 + line_h(ctx.f.head) + 14
    h += _bullet_items_h(ctx, side["items"], w - 44, tag=side.get("h", ""))
    return h + 18


def _replace_h(ctx, b, width):
    aw = 340
    sw = (width - aw) / 2
    h = max(_replace_side_h(ctx, b["before"], sw), _replace_side_h(ctx, b["after"], sw))
    if b.get("note"):
        h += 18 + line_h(ctx.f.band) + 26
        h += (len(wrap_runs(parse_runs(b["note"], ctx.f.band, ctx.f.bandb, WHITE), width - 250, "note")) - 1) * (line_h(ctx.f.band) + 5)
    return h


def _replace_draw(ctx, d, b, x, y, width):
    aw = 340
    sw = (width - aw) / 2
    body_h = max(_replace_side_h(ctx, b["before"], sw), _replace_side_h(ctx, b["after"], sw))
    for side, sx, c in ((b["before"], x, col(b["before"].get("c", "red"))),
                        (b["after"], x + sw + aw, col(b["after"].get("c", "green")))):
        rrect(d, [sx, y, sx + sw, y + body_h], radius=16, fill=CARD_TITLE, outline=c, width=3)
        hb = line_h(ctx.f.head) + 14
        rrect(d, [sx, y, sx + sw, y + hb], radius=16, fill=c)
        d.rectangle([sx, y + hb - 16, sx + sw, y + hb], fill=c)
        d.text((sx + 20, y + 6), side["h"], font=ctx.f.head, fill=BG)
        _draw_bullets(ctx, d, sx + 22, y + hb + 14, sw - 44, side["items"], c, tag=side.get("h", ""))
    mx = x + sw
    mid_y = y + body_h / 2
    arrow_right(d, mx + 26, mid_y, mx + aw - 26, YELLOW, thick=9, head=30)
    lab = b.get("arrow", "")
    if lab:
        lines = wrap_runs([(lab, ctx.f.smallb, YELLOW)], aw - 30, "arrowlab")
        yy = mid_y - 22 - len(lines) * (line_h(ctx.f.smallb) + 3)
        for ln in lines:
            lw = sum(text_w(f, t) for t, f, _ in ln)
            draw_runs_line(d, mx + (aw - lw) / 2, yy, ln)
            yy += line_h(ctx.f.smallb) + 3
    if b.get("note"):
        ny = y + body_h + 18
        nh = _replace_h(ctx, b, width) - body_h - 18
        rrect(d, [x, ny, x + width, ny + nh], radius=12, fill=(14, 34, 52), outline=RULE, width=2)
        lab = "CONTINUITY CAUTION"
        d.text((x + 20, ny + 12), lab, font=ctx.f.bandb, fill=YELLOW)
        off = text_w(ctx.f.bandb, lab) + 34
        yy = ny + 12
        for ln in wrap_runs(parse_runs(b["note"], ctx.f.band, ctx.f.bandb, WHITE), width - off - 30, "note"):
            draw_runs_line(d, x + off, yy, ln)
            yy += line_h(ctx.f.band) + 5
    return _replace_h(ctx, b, width)


# ---- matrix -----------------------------------------------------------------
def _matrix_geom(ctx, b, width):
    fr = b.get("widths") or [1.0 / len(b["headers"])] * len(b["headers"])
    tot = sum(fr)
    ws = [width * f / tot for f in fr]
    return ws


def _matrix_rowh(ctx, cells, ws, font, pad=16):
    h = 0
    for i, cell in enumerate(cells):
        runs = parse_runs(cell, font, ctx.f.smallb, WHITE, WHITE)
        n = len(wrap_runs(runs, ws[i] - 26, "matrix"))
        h = max(h, n * (line_h(font) + 5))
    return h + pad


def _matrix_h(ctx, b, width):
    ws = _matrix_geom(ctx, b, width)
    h = 0
    if b.get("title"):
        h += line_h(ctx.f.head) + 12
    h += _matrix_rowh(ctx, b["headers"], ws, ctx.f.smallb, 18)
    for r in b["rows"]:
        h += _matrix_rowh(ctx, r, ws, ctx.f.small)
    return h


def _matrix_draw(ctx, d, b, x, y, width):
    ws = _matrix_geom(ctx, b, width)
    accent = col(b.get("c", "cyan"))
    cy = y
    if b.get("title"):
        d.text((x, cy), b["title"], font=ctx.f.head, fill=accent)
        cy += line_h(ctx.f.head) + 12
    hh = _matrix_rowh(ctx, b["headers"], ws, ctx.f.smallb, 18)
    d.rectangle([x, cy, x + width, cy + hh], fill=accent)
    cx = x
    for i, cell in enumerate(b["headers"]):
        ty = cy + 9
        for ln in wrap_runs(parse_runs(cell, ctx.f.smallb, ctx.f.smallb, BG, BG), ws[i] - 26, "matrix"):
            draw_runs_line(d, cx + 13, ty, ln)
            ty += line_h(ctx.f.smallb) + 5
        cx += ws[i]
    cy += hh
    for j, r in enumerate(b["rows"]):
        rh = _matrix_rowh(ctx, r, ws, ctx.f.small)
        if j % 2 == 0:
            d.rectangle([x, cy, x + width, cy + rh], fill=(13, 34, 52))
        cx = x
        for i, cell in enumerate(r):
            fill = accent if i == 0 else WHITE
            bold = ctx.f.smallb if i == 0 else ctx.f.smallb
            ty = cy + 8
            runs = parse_runs(cell, ctx.f.smallb if i == 0 else ctx.f.small, bold, fill, YELLOW if i else fill)
            for ln in wrap_runs(runs, ws[i] - 26, "matrix"):
                draw_runs_line(d, cx + 13, ty, ln)
                ty += line_h(ctx.f.small) + 5
            if i:
                d.line([(cx, cy), (cx, cy + rh)], fill=RULE, width=1)
            cx += ws[i]
        d.line([(x, cy + rh), (x + width, cy + rh)], fill=RULE, width=1)
        cy += rh
    return cy - y


# ---- timeline ---------------------------------------------------------------
def _timeline_h(ctx, b, width):
    n = len(b["items"])
    cw = width / n
    top = line_h(ctx.f.smallb) + 8
    below = 0
    for it in b["items"]:
        below = max(below, len(wrap_runs([(it["t"], ctx.f.small, WHITE)], cw - 26, "tl")) * (line_h(ctx.f.small) + 4))
    return top + 34 + below + 8


def _timeline_draw(ctx, d, b, x, y, width):
    n = len(b["items"])
    cw = width / n
    accent = col(b.get("c", "yellow"))
    top = line_h(ctx.f.smallb) + 8
    axis_y = y + top + 16
    d.line([(x + cw / 2, axis_y), (x + width - cw / 2, axis_y)], fill=accent, width=4)
    for i, it in enumerate(b["items"]):
        cx = x + i * cw
        mid = cx + cw / 2
        dw = text_w(ctx.f.smallb, it["d"])
        d.text((mid - dw / 2, y), it["d"], font=ctx.f.smallb, fill=accent)
        d.ellipse([mid - 10, axis_y - 10, mid + 10, axis_y + 10], fill=BG, outline=accent, width=4)
        ty = axis_y + 20
        for ln in wrap_runs([(it["t"], ctx.f.small, WHITE)], cw - 26, "tl"):
            lw = sum(text_w(f, t) for t, f, _ in ln)
            draw_runs_line(d, mid - lw / 2, ty, ln)
            ty += line_h(ctx.f.small) + 4
    return _timeline_h(ctx, b, width)


# ---- band -------------------------------------------------------------------
def _band_h(ctx, b, width):
    lab = b.get("label", "")
    off = (text_w(ctx.f.bandb, lab) + 30) if lab else 14
    lines = wrap_runs(parse_runs(b["text"], ctx.f.band, ctx.f.bandb, WHITE, col(b.get("c", "cyan"))),
                      width - off - 30, lab)
    return len(lines) * (line_h(ctx.f.band) + 5) + 24


def _band_draw(ctx, d, b, x, y, width):
    h = _band_h(ctx, b, width)
    c = col(b.get("c", "cyan"))
    fill = b.get("fill")
    fillc = (14, 34, 52) if not fill else fill
    rrect(d, [x, y, x + width, y + h], radius=10, fill=fillc,
          outline=c if b.get("outline") else None, width=2)
    d.rectangle([x, y, x + 7, y + h], fill=c)
    lab = b.get("label", "")
    off = (text_w(ctx.f.bandb, lab) + 30) if lab else 14
    if lab:
        d.text((x + 20, y + 10), lab, font=ctx.f.bandb, fill=c)
    yy = y + 10
    for ln in wrap_runs(parse_runs(b["text"], ctx.f.band, ctx.f.bandb, WHITE, c), width - off - 30, lab):
        draw_runs_line(d, x + off + 6, yy, ln)
        yy += line_h(ctx.f.band) + 5
    return h


# ---- answer band ------------------------------------------------------------
def _answer_h(ctx, b, width):
    lab = b.get("label", "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM:")
    runs = [(lab + " ", ctx.f.bandb, WHITE)] + parse_runs(b["text"], ctx.f.band, ctx.f.bandb, WHITE, YELLOW)
    return len(wrap_runs(runs, width - 44, "answer")) * (line_h(ctx.f.band) + 5) + 26


def _answer_draw(ctx, d, b, x, y, width):
    h = _answer_h(ctx, b, width)
    rrect(d, [x, y, x + width, y + h], radius=10, fill=ANSWER_FILL, outline=MAGENTA, width=3)
    lab = b.get("label", "ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM:")
    runs = [(lab + " ", ctx.f.bandb, WHITE)] + parse_runs(b["text"], ctx.f.band, ctx.f.bandb, WHITE, YELLOW)
    yy = y + 11
    for ln in wrap_runs(runs, width - 44, "answer"):
        draw_runs_line(d, x + 22, yy, ln)
        yy += line_h(ctx.f.band) + 5
    return h


# ---- ladder (stepped vertical progression) ----------------------------------
def _ladder_h(ctx, b, width):
    n = len(b["steps"])
    step = b.get("indent", 74)
    h = 0
    for i, s in enumerate(b["steps"]):
        w = width - step * i - 60
        ih = 16 + len(wrap_runs([(s["t"], ctx.f.chain, WHITE)], w - 28, "ladder")) * (line_h(ctx.f.chain) + 4)
        if s.get("s"):
            ih += len(wrap_runs([(s["s"], ctx.f.chain_sub, DIM)], w - 28, "ladder")) * (line_h(ctx.f.chain_sub) + 3)
        h += ih + 16 + (16 if i < n - 1 else 0)
    return h


def _ladder_draw(ctx, d, b, x, y, width):
    step = b.get("indent", 74)
    cy = y
    for i, s in enumerate(b["steps"]):
        w = width - step * i - 60
        c = col(s.get("c", "cyan"))
        lines = wrap_runs([(s["t"], ctx.f.chain, c)], w - 28, "ladder")
        sub = wrap_runs([(s["s"], ctx.f.chain_sub, DIM)], w - 28, "ladder") if s.get("s") else []
        ih = 16 + len(lines) * (line_h(ctx.f.chain) + 4) + len(sub) * (line_h(ctx.f.chain_sub) + 3)
        bx = x + step * i
        rrect(d, [bx, cy, bx + w, cy + ih], radius=12, fill=CARD_TITLE, outline=c, width=3)
        ty = cy + 8
        for ln in lines:
            draw_runs_line(d, bx + 14, ty, ln)
            ty += line_h(ctx.f.chain) + 4
        for ln in sub:
            draw_runs_line(d, bx + 14, ty, ln)
            ty += line_h(ctx.f.chain_sub) + 3
        if i < len(b["steps"]) - 1:
            arrow_down(d, bx + step / 2, cy + ih + 2, cy + ih + 30, CYAN, thick=4, head=12)
        cy += ih + 16 + (16 if i < len(b["steps"]) - 1 else 0)
    return cy - y


# ---- row container ----------------------------------------------------------
def _row_h(ctx, b, width):
    gap = b.get("gap", 40)
    ws = [c["w"] for c in b["children"]]
    tot = sum(ws)
    avail = width - gap * (len(ws) - 1)
    return max(measure(ctx, c["block"], avail * w / tot) for c, w in zip(b["children"], ws))


def _row_draw(ctx, d, b, x, y, width):
    gap = b.get("gap", 40)
    ws = [c["w"] for c in b["children"]]
    tot = sum(ws)
    avail = width - gap * (len(ws) - 1)
    cx = x
    total = _row_h(ctx, b, width)
    for c, w in zip(b["children"], ws):
        cw = avail * w / tot
        render(ctx, d, c["block"], cx, y, cw)
        cx += cw + gap
    return total


# ---- headline strip ---------------------------------------------------------
def _strip_h(ctx, b, width):
    return line_h(ctx.f.head) + 14


def _strip_draw(ctx, d, b, x, y, width):
    c = col(b.get("c", "cyan"))
    h = _strip_h(ctx, b, width)
    d.text((x, y + 4), b["text"], font=ctx.f.head, fill=c)
    tw = text_w(ctx.f.head, b["text"])
    d.line([(x + tw + 20, y + h / 2 + 4), (x + width, y + h / 2 + 4)], fill=RULE, width=2)
    return h


BLOCKS = {
    "cols": (_cols_h, _cols_draw),
    "pills": (_pills_h, _pills_draw),
    "chain": (_chain_h, _chain_draw),
    "panels": (_panels_h, _panels_draw),
    "replace": (_replace_h, _replace_draw),
    "matrix": (_matrix_h, _matrix_draw),
    "timeline": (_timeline_h, _timeline_draw),
    "band": (_band_h, _band_draw),
    "answer": (_answer_h, _answer_draw),
    "ladder": (_ladder_h, _ladder_draw),
    "row": (_row_h, _row_draw),
    "strip": (_strip_h, _strip_draw),
}


def measure(ctx, b, width):
    return BLOCKS[b["type"]][0](ctx, b, width)


def render(ctx, d, b, x, y, width):
    return BLOCKS[b["type"]][1](ctx, d, b, x, y, width)


def blocks_h(ctx, blocks, width):
    return sum(measure(ctx, b, width) for b in blocks) + GAP * (len(blocks) - 1)


def blocks_draw(ctx, d, blocks, x, y, width):
    cy = y
    for b in blocks:
        h = measure(ctx, b, width)
        got = render(ctx, d, b, x, cy, width)
        if abs(got - h) > 1.5:
            OVERFLOWS.append(("height-mismatch", b["type"], round(h), round(got)))
        cy += h + GAP
    return cy - GAP - y
