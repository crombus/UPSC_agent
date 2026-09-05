"""Small deterministic Pillow rendering library for the Notions of God g6 master."""
from __future__ import annotations

import math
import textwrap
from pathlib import Path

from PIL import ImageDraw, ImageFont

FONT_DIR = Path(r"C:\Windows\Fonts")

BG = (7, 20, 33)
CARD = (14, 37, 57)
CARD_ALT = (13, 31, 48)
HEADER = (10, 35, 53)
CYAN = (68, 211, 255)
TEAL = (70, 226, 192)
AMBER = (255, 184, 92)
YELLOW = (255, 225, 122)
MAGENTA = (231, 147, 255)
GREEN = (127, 232, 141)
RED = (255, 137, 128)
WHITE = (238, 247, 252)
DIM = (164, 188, 207)
GREY = (145, 165, 182)
RULE = (48, 76, 95)
DEEP = (9, 27, 42)
ANSWER = (48, 37, 59)

COLOURS = {
    "cyan": CYAN,
    "teal": TEAL,
    "amber": AMBER,
    "yellow": YELLOW,
    "magenta": MAGENTA,
    "green": GREEN,
    "red": RED,
    "white": WHITE,
    "dim": DIM,
    "grey": GREY,
}


def colour(name):
    return COLOURS.get(name, CYAN)


def _font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


class Fonts:
    def __init__(self):
        self.title = _font("segoeuib.ttf", 72)
        self.subtitle = _font("segoeuib.ttf", 31)
        self.note = _font("segoeui.ttf", 27)
        self.stage = _font("segoeuib.ttf", 50)
        self.stage_small = _font("segoeuib.ttf", 43)
        self.badge = _font("segoeuib.ttf", 25)
        self.pill = _font("segoeuib.ttf", 27)
        self.h1 = _font("segoeuib.ttf", 35)
        self.h2 = _font("segoeuib.ttf", 30)
        self.body = _font("segoeui.ttf", 28)
        self.body_bold = _font("segoeuib.ttf", 28)
        self.small = _font("segoeui.ttf", 24)
        self.small_bold = _font("segoeuib.ttf", 24)
        self.tiny = _font("segoeui.ttf", 21)
        self.tiny_bold = _font("segoeuib.ttf", 21)
        self.matrix = _font("segoeui.ttf", 23)
        self.matrix_bold = _font("segoeuib.ttf", 23)
        self.rail = _font("segoeuib.ttf", 31)


F = Fonts()
OVERFLOWS = []
BOXES = []


def reset_audit():
    OVERFLOWS.clear()
    BOXES.clear()


def text_w(font, text):
    return font.getlength(str(text))


def line_h(font, leading=6):
    a, d = font.getmetrics()
    return a + d + leading


def rounded(draw, box, radius=18, fill=None, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw, p0, p1, fill=CYAN, width=5, head=16):
    x0, y0 = p0
    x1, y1 = p1
    draw.line((x0, y0, x1, y1), fill=fill, width=width)
    ang = math.atan2(y1 - y0, x1 - x0)
    pts = [
        (x1, y1),
        (
            x1 - head * math.cos(ang - math.pi / 6),
            y1 - head * math.sin(ang - math.pi / 6),
        ),
        (
            x1 - head * math.cos(ang + math.pi / 6),
            y1 - head * math.sin(ang + math.pi / 6),
        ),
    ]
    draw.polygon(pts, fill=fill)


def wrap_lines(text, font, width, tag=""):
    words = str(text).split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if text_w(font, trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            if text_w(font, word) > width:
                OVERFLOWS.append(
                    {"type": "token_width", "tag": tag, "text": word, "width": width}
                )
            cur = word
    if cur:
        lines.append(cur)
    return lines or [""]


def measure_text(text, font, width, leading=6, tag=""):
    return len(wrap_lines(text, font, width, tag)) * line_h(font, leading)


def draw_text(
    draw,
    xy,
    text,
    font,
    fill,
    width,
    leading=6,
    tag="",
    bottom=None,
    align="left",
):
    x, y = xy
    lines = wrap_lines(text, font, width, tag)
    lh = line_h(font, leading)
    for line in lines:
        lw = text_w(font, line)
        tx = x
        if align == "center":
            tx = x + (width - lw) / 2
        elif align == "right":
            tx = x + width - lw
        draw.text((tx, y), line, font=font, fill=fill)
        y += lh
    if bottom is not None and y > bottom + 1:
        OVERFLOWS.append(
            {"type": "bottom", "tag": tag, "actual": round(y), "limit": round(bottom)}
        )
    return y


def draw_bullets(
    draw,
    x,
    y,
    width,
    items,
    accent=CYAN,
    font=None,
    gap=8,
    tag="",
    bottom=None,
):
    font = font or F.body
    lh = line_h(font, 5)
    for index, item in enumerate(items):
        lines = wrap_lines(item, font, width - 34, f"{tag}:{index}")
        draw.ellipse((x + 4, y + 11, x + 13, y + 20), fill=accent)
        for line in lines:
            draw.text((x + 30, y), line, font=font, fill=WHITE)
            y += lh
        y += gap
    if bottom is not None and y > bottom + 1:
        OVERFLOWS.append(
            {"type": "bullets_bottom", "tag": tag, "actual": round(y), "limit": round(bottom)}
        )
    return y


def panel(draw, box, title, title_colour=AMBER, fill=CARD_ALT, outline=RULE, font=None):
    rounded(draw, box, 18, fill=fill, outline=outline, width=2)
    x0, y0, x1, _ = box
    font = font or F.h2
    draw.text((x0 + 22, y0 + 16), title, font=font, fill=title_colour)
    return x0 + 22, y0 + 16 + line_h(font, 4) + 7, x1 - x0 - 44


def pill_rows(pills, width):
    rows = []
    cur = []
    used = 0
    for i, pill in enumerate(pills):
        text = pill if isinstance(pill, str) else pill[0]
        pw = text_w(F.pill, text) + 42
        if cur and used + pw + 12 > width:
            rows.append(cur)
            cur = []
            used = 0
        cur.append((pill, pw))
        used += pw + 12
    if cur:
        rows.append(cur)
    return rows


def draw_pills(draw, x, y, width, pills):
    palette = ["amber", "cyan", "teal", "yellow", "magenta", "green", "red"]
    ph = line_h(F.pill, 0) + 14
    for row in pill_rows(pills, width):
        cx = x
        for i, (item, pw) in enumerate(row):
            if isinstance(item, tuple):
                text, cname = item
            else:
                text, cname = item, palette[i % len(palette)]
            c = colour(cname)
            rounded(draw, (cx, y, cx + pw, y + ph), ph // 2, fill=c)
            draw.text(
                (cx + (pw - text_w(F.pill, text)) / 2, y + 5),
                text,
                font=F.pill,
                fill=BG,
            )
            cx += pw + 12
        y += ph + 10
    return y


def band(draw, box, label, text, accent=CYAN, fill=DEEP, font=None, tag=""):
    font = font or F.small
    rounded(draw, box, 15, fill=fill, outline=accent, width=2)
    x0, y0, x1, y1 = box
    label_w = text_w(F.small_bold, label) + 30
    rounded(draw, (x0, y0, x0 + label_w, y1), 15, fill=accent)
    draw.text(
        (x0 + 15, y0 + (y1 - y0 - line_h(F.small_bold, 0)) / 2 - 1),
        label,
        font=F.small_bold,
        fill=BG,
    )
    draw_text(
        draw,
        (x0 + label_w + 18, y0 + 13),
        text,
        font,
        WHITE,
        x1 - x0 - label_w - 34,
        4,
        tag,
        y1 - 7,
    )


def answer_band(draw, box, text, tag="answer"):
    band(draw, box, "ANSWER LINE", text, MAGENTA, ANSWER, F.small_bold, tag)


def bridge_band(draw, box, text, tag="bridge"):
    band(draw, box, "BRIDGE", text, CYAN, (9, 39, 54), F.small, tag)


def trap_band(draw, box, text, tag="trap"):
    band(draw, box, "TRAP", text, RED, (49, 31, 40), F.small, tag)


def record_box(name, box, stage):
    BOXES.append({"name": name, "box": [round(v) for v in box], "stage": stage})


def matrix(
    draw,
    x,
    y,
    width,
    headers,
    rows,
    col_fracs,
    font=None,
    header_font=None,
    row_pad=12,
    tag="matrix",
    row_colours=None,
):
    font = font or F.matrix
    header_font = header_font or F.matrix_bold
    xs = [x]
    for frac in col_fracs:
        xs.append(xs[-1] + width * frac)
    header_h = max(
        measure_text(h, header_font, width * col_fracs[i] - 22, 3, tag)
        for i, h in enumerate(headers)
    ) + 2 * row_pad
    rounded(draw, (x, y, x + width, y + header_h), 10, fill=AMBER)
    for i, h in enumerate(headers):
        draw_text(
            draw,
            (xs[i] + 11, y + row_pad),
            h,
            header_font,
            BG,
            width * col_fracs[i] - 22,
            3,
            f"{tag}:head:{i}",
        )
    for xx in xs[1:-1]:
        draw.line((xx, y, xx, y + header_h), fill=BG, width=2)
    cy = y + header_h
    for r, row in enumerate(rows):
        heights = [
            measure_text(cell, font, width * col_fracs[i] - 22, 3, f"{tag}:{r}:{i}")
            for i, cell in enumerate(row)
        ]
        rh = max(heights) + 2 * row_pad
        fill = CARD_ALT if r % 2 == 0 else (17, 43, 62)
        if row_colours and r < len(row_colours):
            fill = row_colours[r]
        draw.rectangle((x, cy, x + width, cy + rh), fill=fill, outline=RULE, width=2)
        for i, cell in enumerate(row):
            ff = F.matrix_bold if i == 0 else font
            fc = colour(["cyan", "white", "white", "white", "white", "white"][min(i, 5)])
            draw_text(
                draw,
                (xs[i] + 11, cy + row_pad),
                cell,
                ff,
                fc,
                width * col_fracs[i] - 22,
                3,
                f"{tag}:{r}:{i}",
            )
            if i:
                draw.line((xs[i], cy, xs[i], cy + rh), fill=RULE, width=2)
        cy += rh
    return cy


def contrast_ratio(a, b):
    def lum(c):
        vals = []
        for v in c:
            x = v / 255
            vals.append(x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4)
        return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]

    l1, l2 = sorted((lum(a), lum(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)

