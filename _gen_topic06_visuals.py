# -*- coding: utf-8 -*-
"""Deterministic visual generator for Modern History Topic 06.
Temporary working script -- deleted after PNG generation per task cleanup rules.
Style mirrors Topic 04/05 asset conventions (dark navy header, orange rule,
light content background, teal/white cards, orange arrows, red trap callouts).
"""
import os
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
from matplotlib.lines import Line2D

OUT = r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\notes\Modern-Indian-History\assets\06_Constitutional-Development-1757-1858"
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- palette --
NAVY = "#0e1c36"
ORANGE = "#e0982a"
TEAL = "#1f8a70"
RED = "#c0455a"
BLUE = "#2f5f8a"
BG_LIGHT = "#eef1f7"
WHITE = "#ffffff"
INK = "#1c2430"
GRAY_TXT = "#5a6472"
CARD_BORDER = "#c9d0dc"
CALLOUT_BG = "#e6e9f0"
TRAP_BG = "#fdecef"
TRAP_BORDER = "#c0455a"
GOOD_BG = "#e8f5f0"
GOOD_BORDER = "#1f8a70"

FONT = "DejaVu Sans"
plt.rcParams["font.family"] = FONT

W, H = 1600, 950
COVER_H = 900


def _fig(h=H):
    fig = plt.figure(figsize=(16, h / 100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, h)
    ax.invert_yaxis()
    ax.axis("off")
    return fig, ax


def _wrap(text, width):
    out = []
    for para in text.split("\n"):
        if para.strip() == "":
            out.append("")
        else:
            out.extend(textwrap.wrap(para, width=width) or [""])
    return "\n".join(out)


def chars_for(width_px, fontsize):
    """Empirically-calibrated chars-per-line for DejaVu Sans at 100 dpi on a
    1600-data-unit-wide, 16-inch figure (1 data unit = 0.72 pt)."""
    return max(6, int(width_px / (fontsize * 0.82)))


def wtext(ax, x, y, text, width_px, fontsize, **kw):
    wrapped = _wrap(text, chars_for(width_px, fontsize))
    ax.text(x, y, wrapped, fontsize=fontsize, **kw)
    return wrapped


def text_block_h(text, width_px, fontsize, linespacing=1.4):
    """Pixel height needed to render (possibly multi-paragraph) wrapped text at
    fontsize/linespacing, matching matplotlib's rendering metrics closely enough
    for safe box-sizing decisions."""
    wrapped = _wrap(text, chars_for(width_px, fontsize))
    n_lines = wrapped.count("\n") + 1 if text else 0
    return n_lines * fontsize * linespacing * 1.39


def head_band_h(head, w, head_fs):
    """Pixel height of a card()'s colored head band, accounting for multi-line
    wrapped head text (a 1-line head keeps the classic fixed 40px band)."""
    wrapped = _wrap(head, chars_for(w - 36, head_fs))
    n_lines = wrapped.count("\n") + 1 if head else 1
    return max(40, 12 + n_lines * head_fs * 1.15 * 1.39)


def card_h_needed(head, body, w, body_fs=14.5, head_fs=15.5, top_pad=16, bottom_pad=16, min_h=90):
    """Minimum card height so a card()'s wrapped head/body text never overflows the box."""
    hh = head_band_h(head, w, head_fs)
    body_h = text_block_h(body, w - 36, body_fs) if body else 0
    return max(min_h, hh + top_pad + body_h + bottom_pad)


def header(ax, title, badge=None, h=H, title_size=27):
    ax.add_patch(Rectangle((0, 0), W, 165, facecolor=NAVY, edgecolor="none", zorder=1))
    ax.add_patch(Rectangle((0, 165), W, 6, facecolor=ORANGE, edgecolor="none", zorder=1))
    wrapped = _wrap(title, chars_for(W - 320 if badge else W - 80, title_size))
    ax.text(40, 82, wrapped, color=WHITE, fontsize=title_size, fontweight="bold",
             va="center", ha="left", zorder=2, linespacing=1.15)
    if badge:
        bw = 18 * len(badge) + 60
        bx = W - 40 - bw
        ax.add_patch(FancyBboxPatch((bx, 34), bw, 46, boxstyle="round,pad=0,rounding_size=23",
                                     facecolor=NAVY, edgecolor=WHITE, linewidth=1.6, zorder=2))
        ax.text(bx + bw / 2, 57, badge, color=WHITE, fontsize=15, fontweight="bold",
                ha="center", va="center", zorder=3)


def footer(ax, caption, h=H):
    ax.text(40, h - 22, caption, color=GRAY_TXT, fontsize=12.5, style="italic",
            va="center", ha="left")


def note_box(ax, x, y, w, h, text, bg=CALLOUT_BG, fg=INK, fontsize=16.5, border=None):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=10",
                          facecolor=bg, edgecolor=border or "none",
                          linewidth=1.4 if border else 0, zorder=2)
    ax.add_patch(box)
    wrapped = _wrap(text, chars_for(w - 48, fontsize))
    ax.text(x + 24, y + h / 2, wrapped, color=fg, fontsize=fontsize, va="center",
            ha="left", linespacing=1.35, zorder=3)


def place_note(ax, content_bottom, text, x=40, w=None, bg=CALLOUT_BG, fg=INK, border=None,
                floor_y=None, ceiling=None):
    """Places a note_box directly below content_bottom, auto-shrinking fontsize/height
    so it never collides with the footer caption, regardless of note text length or
    how far down the content above it already runs."""
    w = (W - 80) if w is None else w
    ceiling = (H - 34) if ceiling is None else ceiling  # keep clear of footer text
    top = content_bottom + 14 if floor_y is None else max(content_bottom + 14, floor_y)
    for fs, ls in ((16.5, 1.35), (15, 1.32), (13.5, 1.3), (12, 1.28), (11, 1.25)):
        h = max(56, text_block_h(text, w - 48, fs, linespacing=ls) + 28)
        if top + h <= ceiling:
            note_box(ax, x, top, w, h, text, bg=bg, fg=fg, fontsize=fs, border=border)
            return top, h
    # last resort: smallest size, clipped to available space (should not occur in practice)
    h = max(40, ceiling - top)
    note_box(ax, x, top, w, h, text, bg=bg, fg=fg, fontsize=11, border=border)
    return top, h


def card(ax, x, y, w, h, head, body, head_color=TEAL, body_fs=14.5, head_fs=15.5, wrap_w=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=6",
                                 facecolor=WHITE, edgecolor=CARD_BORDER, linewidth=1.2, zorder=2))
    hh = head_band_h(head, w, head_fs)
    ax.add_patch(FancyBboxPatch((x, y), w, hh, boxstyle="round,pad=0,rounding_size=6",
                                 facecolor=head_color, edgecolor=head_color, linewidth=0, zorder=3))
    ax.add_patch(Rectangle((x, y + hh - 8), w, 8, facecolor=head_color, edgecolor="none", zorder=3))
    ax.text(x + 18, y + hh / 2, _wrap(head, chars_for(w - 36, head_fs)), color=WHITE, fontsize=head_fs,
            fontweight="bold", va="center", ha="left", zorder=4, linespacing=1.15)
    ww = chars_for(w - 36, body_fs) if wrap_w is None else wrap_w
    if body:
        ax.text(x + 18, y + hh + 16, _wrap(body, ww), color=INK, fontsize=body_fs, va="top",
                ha="left", zorder=4, linespacing=1.4)


def arrow(ax, x1, y1, x2, y2, color=ORANGE, lw=3.4, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=22,
                                  color=color, linewidth=lw, zorder=5))


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, facecolor=BG_LIGHT if False else fig.get_facecolor())
    plt.close(fig)
    print("saved", name)


# =====================================================================
# 1. COVER
# =====================================================================
def cover():
    fig, ax = _fig(COVER_H)
    fig.patch.set_facecolor(NAVY)
    ax.add_patch(Rectangle((0, 0), W, 10, facecolor=ORANGE, edgecolor="none"))
    ax.text(48, 74, "MODERN HISTORY - TOPIC 06", color=ORANGE, fontsize=23, fontweight="bold", va="center")
    ax.text(46, 150, "Structure of Government &", color=WHITE, fontsize=40, fontweight="bold", va="center")
    ax.text(46, 205, "Constitutional Development,", color=WHITE, fontsize=40, fontweight="bold", va="center")
    ax.text(46, 260, "1757-1858", color=WHITE, fontsize=40, fontweight="bold", va="center")
    ax.text(48, 305, "Regulating Act 1773 to the Government of India Act 1858 | GS-I Modern Indian History | Date: 2026-08-19",
            color="#c7cedd", fontsize=16.5, va="center")

    cards = [
        ("FOCUS", "1773-1858: Regulating Act, Supreme Court and jurisdiction, Act of Settlement 1781, Pitt's India Act 1784, Act of 1786, Charter Acts 1793/1813/1833/1853, and the Government of India Act 1858.", BLUE),
        ("EVIDENCE", "Repository basic/advanced Topic 06; Bipin Chandra's Modern India and Sekhar Bandyopadhyay's From Plassey to Partition; official 2019 and 2023 Prelims papers.", TEAL),
        ("EXAM MOVE", "Prelims: hold Governor-General of Bengal vs India vs Viceroy precisely. Mains: read this as parliamentary control over a corporation, not a liberal reform story.", ORANGE),
        ("CAUTION", "No invented statutory wording, no fabricated PYQ key, no borrowing of Topic 04/07/08/09/11/12 material -- boundaries are held throughout; both PYQs are labelled where unverified.", RED),
    ]
    x0, y0, gw, gh, gap = 48, 360, 752, 190, 24
    for i, (head, body, color) in enumerate(cards):
        cx = x0 + (i % 2) * (gw + gap)
        cy = y0 + (i // 2) * (gh + gap)
        ax.add_patch(Rectangle((cx, cy), gw, 42, facecolor=color, edgecolor="none"))
        ax.text(cx + 20, cy + 21, head, color=WHITE, fontsize=15.5, fontweight="bold", va="center", ha="left")
        ax.add_patch(Rectangle((cx, cy + 42), gw, gh - 42, facecolor="#152645", edgecolor="none"))
        wtext(ax, cx + 20, cy + 42 + (gh - 42) / 2, body, gw - 40, 14.5, color="#dfe4ee", va="center",
              ha="left", linespacing=1.5)

    ax.text(48, COVER_H - 30, "Original deterministic study visual - Modern History Topic 06", color="#7c869c",
            fontsize=12.5, style="italic", va="center")
    save(fig, "00_00_cover.png")


# =====================================================================
# Generic layout: TIMELINE
# =====================================================================
def timeline_chart(name, title, badge, events, note, cap, alt_offset=True):
    """events: list of dict(year, text). Alternates above/below a horizontal spine."""
    fig, ax = _fig()
    header(ax, title, badge)
    n = len(events)
    x0, x1 = 90, W - 90
    y_mid = 430
    ax.add_patch(FancyArrowPatch((x0, y_mid), (x1, y_mid), arrowstyle="-|>", mutation_scale=26,
                                  color=INK, linewidth=3.2, zorder=2))
    step = (x1 - x0) / max(1, n - 1) if n > 1 else 0
    box_w = min(230, step - 20) if n > 1 else 300
    for i, ev in enumerate(events):
        x = x0 + i * step
        above = (i % 2 == 0) if alt_offset else True
        ax.add_patch(Circle((x, y_mid), 9, facecolor=ORANGE, edgecolor=WHITE, linewidth=1.5, zorder=4))
        bh = 150
        by = y_mid - 55 - bh if above else y_mid + 55
        bx = x - box_w / 2
        ax.plot([x, x], [y_mid - 12 if above else y_mid + 12, by + (bh if above else 0)],
                color="#9aa4b5", linewidth=1.4, zorder=2)
        ax.add_patch(FancyBboxPatch((bx, by), box_w, 40, boxstyle="round,pad=0,rounding_size=6",
                                     facecolor=TEAL, edgecolor="none", zorder=3))
        ax.text(x, by + 20, str(ev["year"]), color=WHITE, fontsize=17, fontweight="bold",
                ha="center", va="center", zorder=4)
        ax.add_patch(FancyBboxPatch((bx, by + 40), box_w, bh - 40, boxstyle="round,pad=0,rounding_size=6",
                                     facecolor=WHITE, edgecolor=CARD_BORDER, linewidth=1.1, zorder=3))
        ax.text(x, by + 40 + (bh - 40) / 2, _wrap(ev["text"], chars_for(box_w - 20, 12.6)), color=INK, fontsize=12.6,
                ha="center", va="center", zorder=4, linespacing=1.25)
    place_note(ax, y_mid + 55 + 150, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: FLOW / CIRCUIT (numbered boxes + arrows)
# =====================================================================
def flow_chart(name, title, badge, boxes, arrows, note, cap, cols=2):
    """boxes: list of dict(head, body, color); positions auto in a grid of `cols`."""
    fig, ax = _fig()
    header(ax, title, badge)
    n = len(boxes)
    rows = (n + cols - 1) // cols
    x0, y0 = 60, 210
    gap_x, gap_y = 60, 60
    gw = (W - 2 * x0 - (cols - 1) * gap_x) / cols
    avail_h = (H - 150) - y0
    avail_per_row = (avail_h - (rows - 1) * gap_y) / rows
    bfs = 15.5
    for candidate in (15.5, 14, 13, 11.5, 10.5, 9.5):
        needed = max(card_h_needed(b["head"], b["body"], gw, body_fs=candidate, head_fs=17) for b in boxes)
        if needed <= avail_per_row:
            bfs = candidate
            break
    else:
        bfs = 9.5
    needed = max(card_h_needed(b["head"], b["body"], gw, body_fs=bfs, head_fs=17) for b in boxes)
    gh = max(needed, min(190, avail_per_row))
    gh = min(gh, avail_per_row)
    positions = []
    for i in range(n):
        r, c = divmod(i, cols)
        x = x0 + c * (gw + gap_x)
        y = y0 + r * (gh + gap_y)
        positions.append((x, y))
    for i, b in enumerate(boxes):
        x, y = positions[i]
        card(ax, x, y, gw, gh, b["head"], b["body"], head_color=b.get("color", TEAL), body_fs=bfs, head_fs=17)
    for (i, j) in arrows:
        x1, y1 = positions[i]
        x2, y2 = positions[j]
        if abs(y1 - y2) < 5:  # same row -> horizontal arrow
            if x1 < x2:
                arrow(ax, x1 + gw + 14, y1 + gh / 2, x2 - 14, y2 + gh / 2)
            else:
                arrow(ax, x1 - 14, y1 + gh / 2, x2 + gw + 14, y2 + gh / 2)
        else:  # vertical arrow
            if y1 < y2:
                arrow(ax, x1 + gw / 2, y1 + gh + 14, x2 + gw / 2, y2 - 14)
            else:
                arrow(ax, x1 + gw / 2, y1 - 14, x2 + gw / 2, y2 + gh + 14)
    content_bottom = y0 + rows * (gh + gap_y) - gap_y
    place_note(ax, content_bottom, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: MATRIX / TABLE
# =====================================================================
def matrix_table(name, title, badge, col_headers, rows, note, cap, col_widths=None, row_h=None,
                  first_col_w=300):
    fig, ax = _fig()
    header(ax, title, badge)
    x0, y0 = 44, 200
    table_w = W - 88
    ncols = len(col_headers)
    if col_widths is None:
        rest = table_w - first_col_w
        col_widths = [first_col_w] + [rest / (ncols - 1)] * (ncols - 1)
    nrows = len(rows)
    hdr_h = 62
    row_h_needed = 0
    for row in rows:
        h0 = text_block_h(row[0], col_widths[0] - 32, 14.5, linespacing=1.2) + 24
        for c in range(1, ncols):
            h0 = max(h0, text_block_h(row[c], col_widths[c] - 32, 13.4, linespacing=1.25) + 24)
        row_h_needed = max(row_h_needed, h0)
    if row_h is None:
        avail = H - 300 - y0
        row_h = max(row_h_needed, min(92, avail / nrows))
    # header row
    xs = [x0]
    for w in col_widths:
        xs.append(xs[-1] + w)
    ax.add_patch(Rectangle((x0, y0), col_widths[0], hdr_h, facecolor=NAVY, edgecolor=WHITE, linewidth=1))
    for c in range(1, ncols):
        ax.add_patch(Rectangle((xs[c], y0), col_widths[c], hdr_h, facecolor=BLUE, edgecolor=WHITE, linewidth=1))
        ax.text(xs[c] + col_widths[c] / 2, y0 + hdr_h / 2, _wrap(col_headers[c], chars_for(col_widths[c] - 24, 15.5)),
                color=WHITE, fontsize=15.5, fontweight="bold", ha="center", va="center", linespacing=1.2)
    for r, row in enumerate(rows):
        ry = y0 + hdr_h + r * row_h
        shade = "#f4f6fa" if r % 2 == 0 else WHITE
        ax.add_patch(Rectangle((x0, ry), col_widths[0], row_h, facecolor="#fbe9d0", edgecolor=CARD_BORDER, linewidth=0.8))
        ax.text(x0 + 16, ry + row_h / 2, _wrap(row[0], chars_for(col_widths[0] - 32, 14.5)), color=INK, fontsize=14.5,
                fontweight="bold", va="center", ha="left", linespacing=1.2)
        for c in range(1, ncols):
            ax.add_patch(Rectangle((xs[c], ry), col_widths[c], row_h, facecolor=shade, edgecolor=CARD_BORDER, linewidth=0.8))
            ax.text(xs[c] + 16, ry + row_h / 2, _wrap(row[c], chars_for(col_widths[c] - 32, 13.4)), color=INK, fontsize=13.4,
                    va="center", ha="left", linespacing=1.25)
    bottom_y = y0 + hdr_h + nrows * row_h
    place_note(ax, bottom_y + 10, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: STANDOFF (two opposing sides + centre label)
# =====================================================================
def standoff_chart(name, title, badge, left_head, left_items, right_head, right_items, center, note, cap,
                    left_color=BLUE, right_color=TEAL):
    fig, ax = _fig()
    header(ax, title, badge)
    cw = 620
    ly, ry = 210, 210
    lx, rx = 60, W - 60 - cw
    head_h = max(head_band_h(left_head, cw, 19), head_band_h(right_head, cw, 19), 60)
    n = max(len(left_items), len(right_items), 1)
    slot_h = min(76, (H - 150 - (ly + head_h + 10)) / n - 12)
    longest_needed = max([text_block_h(it, cw - 36, 13.6, linespacing=1.25) + 24
                          for it in (left_items + right_items)] or [slot_h])
    item_h = max(slot_h, longest_needed)
    gap_h = item_h + 12
    card(ax, lx, ly, cw, head_h, left_head, "", head_color=left_color, head_fs=19)
    card(ax, rx, ry, cw, head_h, right_head, "", head_color=right_color, head_fs=19)
    iy = ly + head_h + 10
    for it in left_items:
        ax.add_patch(FancyBboxPatch((lx, iy), cw, item_h, boxstyle="round,pad=0,rounding_size=5",
                                     facecolor=WHITE, edgecolor=CARD_BORDER, linewidth=1, zorder=2))
        ax.text(lx + 18, iy + item_h / 2, _wrap(it, chars_for(cw - 36, 13.6)), color=INK, fontsize=13.6, va="center", ha="left", linespacing=1.25, zorder=3)
        iy += gap_h
    iy = ry + head_h + 10
    for it in right_items:
        ax.add_patch(FancyBboxPatch((rx, iy), cw, item_h, boxstyle="round,pad=0,rounding_size=5",
                                     facecolor=WHITE, edgecolor=CARD_BORDER, linewidth=1, zorder=2))
        ax.text(rx + 18, iy + item_h / 2, _wrap(it, chars_for(cw - 36, 13.6)), color=INK, fontsize=13.6, va="center", ha="left", linespacing=1.25, zorder=3)
        iy += gap_h
    cxm = W / 2
    cym = ly + head_h + 10 + (n * gap_h) / 2
    ax.add_patch(Circle((cxm, cym), 78, facecolor=ORANGE, edgecolor=WHITE, linewidth=3, zorder=5))
    ax.text(cxm, cym, _wrap(center, chars_for(132, 14.5)), color=WHITE, fontsize=14.5, fontweight="bold", ha="center", va="center",
            zorder=6, linespacing=1.2)
    content_bottom = max(ly + head_h + 10 + len(left_items) * gap_h,
                          ry + head_h + 10 + len(right_items) * gap_h, cym + 78)
    place_note(ax, content_bottom, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: VENN OVERLAP
# =====================================================================
def venn_chart(name, title, badge, left_label, left_items, right_label, right_items, overlap_label,
               overlap_items, note, cap):
    fig, ax = _fig()
    header(ax, title, badge)
    cy = 430
    r = 260
    lx, rx = W / 2 - 190, W / 2 + 190
    ax.add_patch(Circle((lx, cy), r, facecolor=BLUE, alpha=0.32, edgecolor=BLUE, linewidth=2.4, zorder=2))
    ax.add_patch(Circle((rx, cy), r, facecolor=TEAL, alpha=0.32, edgecolor=TEAL, linewidth=2.4, zorder=2))
    ax.text(lx - 130, cy - r - 24, left_label, color=BLUE, fontsize=18, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(rx + 130, cy - r - 24, right_label, color=TEAL, fontsize=18, fontweight="bold", ha="center", va="center", zorder=4)
    ax.text(lx - 150, cy - 20, _wrap("\n".join(left_items), chars_for(230, 12.8)), color=INK, fontsize=12.8, ha="center", va="center",
            zorder=4, linespacing=1.6)
    ax.text(rx + 150, cy - 20, _wrap("\n".join(right_items), chars_for(230, 12.8)), color=INK, fontsize=12.8, ha="center", va="center",
            zorder=4, linespacing=1.6)
    ax.text(W / 2, cy - 20, _wrap(overlap_label + ":\n" + "\n".join(overlap_items), chars_for(150, 12.2)), color=WHITE,
            fontsize=12.2, fontweight="bold", ha="center", va="center", zorder=5, linespacing=1.5)
    place_note(ax, cy + r, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: ORG CHART (tree hierarchy)
# =====================================================================
def org_chart(name, title, badge, root, children, note, cap, grandchildren=None):
    """root: dict(head, body). children: list of dict(head, body, color).
    grandchildren: optional list-of-lists aligned with children, each item dict(head, body)."""
    fig, ax = _fig()
    header(ax, title, badge)
    rw = 460
    rh = card_h_needed(root["head"], root["body"], rw, body_fs=14, head_fs=17)
    rx = (W - rw) / 2
    ry = 190
    card(ax, rx, ry, rw, rh, root["head"], root["body"], head_color=NAVY, head_fs=17, body_fs=14)
    n = len(children)
    cw = 340
    gap = (W - 80 - n * cw) / (n - 1) if n > 1 else 0
    cx0 = 40
    ch = max([card_h_needed(c["head"], c["body"], cw, body_fs=13, head_fs=15) for c in children])
    trunk_y = ry + rh + 22
    cy = trunk_y + 50
    ax.plot([W / 2, W / 2], [ry + rh, trunk_y], color=INK, linewidth=2.6, zorder=2)
    centers = []
    for i in range(n):
        cx = cx0 + i * (cw + gap)
        centers.append(cx + cw / 2)
    ax.plot([min(centers), max(centers)], [trunk_y, trunk_y], color=INK, linewidth=2.6, zorder=2)
    content_bottom = cy + ch
    for i, ch_item in enumerate(children):
        cx = cx0 + i * (cw + gap)
        ax.plot([centers[i], centers[i]], [trunk_y, cy], color=INK, linewidth=2.6, zorder=2)
        card(ax, cx, cy, cw, ch, ch_item["head"], ch_item["body"], head_color=ch_item.get("color", TEAL),
             head_fs=15, body_fs=13)
        if grandchildren and grandchildren[i]:
            gy = cy + ch + 14
            for j, g in enumerate(grandchildren[i]):
                gbh = max(52, text_block_h(g, cw - 30, 12, linespacing=1.2) + 20)
                ax.plot([centers[i], centers[i]], [cy + ch, gy], color="#9aa4b5", linewidth=1.6, zorder=2)
                ax.add_patch(FancyBboxPatch((cx, gy), cw, gbh, boxstyle="round,pad=0,rounding_size=5",
                                             facecolor=CALLOUT_BG, edgecolor=CARD_BORDER, linewidth=1, zorder=3))
                ax.text(cx + cw / 2, gy + gbh / 2, _wrap(g, chars_for(cw - 30, 12)), color=INK, fontsize=12, ha="center", va="center",
                        zorder=4, linespacing=1.2)
                gy += gbh + 8
            content_bottom = max(content_bottom, gy - 8)
    place_note(ax, content_bottom, note)
    footer(ax, cap)
    save(fig, name)



# =====================================================================
# Generic layout: LADDER (ascending steps)
# =====================================================================
def ladder_chart(name, title, badge, steps, note, cap, horizontal=True):
    fig, ax = _fig()
    header(ax, title, badge)
    n = len(steps)
    if horizontal:
        x0, x1 = 90, W - 90
        step_w = (x1 - x0) / n
        base_y = 720
        max_rise = 380
        for i, st in enumerate(steps):
            bx = x0 + i * step_w + 14
            bw = step_w - 28
            bh_box = 145
            by = base_y - (i + 1) * (max_rise / n) - bh_box
            ax.add_patch(FancyBboxPatch((bx, by), bw, bh_box, boxstyle="round,pad=0,rounding_size=6",
                                         facecolor=TEAL if i % 2 == 0 else BLUE, edgecolor="none", zorder=3))
            ax.text(bx + bw / 2, by + 26, st["label"], color=WHITE, fontsize=15.5, fontweight="bold",
                    ha="center", va="center", zorder=4)
            ax.text(bx + bw / 2, by + 86, _wrap(st["text"], chars_for(bw - 16, 11.6)), color=WHITE, fontsize=11.6, ha="center",
                    va="center", zorder=4, linespacing=1.25)
            ax.add_patch(Rectangle((bx, by + bh_box), bw, base_y - (by + bh_box), facecolor="#c7cedd",
                                    edgecolor="none", zorder=1))
            if i < n - 1:
                nx = x0 + (i + 1) * step_w + 14
                nby = base_y - (i + 2) * (max_rise / n) - bh_box
                arrow(ax, bx + bw, by + bh_box / 2, nx, nby + bh_box / 2, lw=3)
        ax.plot([x0 - 10, x1 + 10], [base_y, base_y], color=INK, linewidth=2)
    place_note(ax, base_y, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: SPECTRUM (gradient bar with markers)
# =====================================================================
def spectrum_chart(name, title, badge, left_label, right_label, points, note, cap):
    """points: list of dict(x in 0..1, label, text, above bool)"""
    fig, ax = _fig()
    header(ax, title, badge)
    bar_y = 430
    bx0, bx1 = 140, W - 140
    n = 220
    for i in range(n):
        frac = i / n
        color = tuple(a + (b - a) * frac for a, b in zip((0xc0 / 255, 0x45 / 255, 0x5a / 255),
                                                           (0x1f / 255, 0x8a / 255, 0x70 / 255)))
        ax.add_patch(Rectangle((bx0 + frac * (bx1 - bx0), bar_y - 22), (bx1 - bx0) / n + 1, 44,
                                facecolor=color, edgecolor="none", zorder=2))
    ax.text(bx0, bar_y - 60, left_label, color=RED, fontsize=16, fontweight="bold", ha="left", va="center")
    ax.text(bx1, bar_y - 60, right_label, color=TEAL, fontsize=16, fontweight="bold", ha="right", va="center")
    content_bottom = bar_y + 30
    for p in points:
        x = bx0 + p["x"] * (bx1 - bx0)
        ax.plot([x, x], [bar_y - 30, bar_y + 30], color=INK, linewidth=2.2, zorder=3)
        above = p.get("above", True)
        bw = 300
        bh = max(145, 48 + text_block_h(p["text"], bw - 32, 11.6, linespacing=1.3) + 16)
        ty = bar_y - 90 if above else bar_y + 100
        by = ty - bh if above else ty
        bxx = min(max(x - bw / 2, 20), W - 20 - bw)
        ax.plot([x, x], [bar_y - 30 if above else bar_y + 30, by + (bh if above else 0)], color="#9aa4b5",
                linewidth=1.4, zorder=2)
        ax.add_patch(FancyBboxPatch((bxx, by), bw, bh, boxstyle="round,pad=0,rounding_size=6", facecolor=WHITE,
                                     edgecolor=CARD_BORDER, linewidth=1.1, zorder=3))
        ax.text(bxx + bw / 2, by + 26, p["label"], color=INK, fontsize=13.6, fontweight="bold", ha="center",
                va="center", zorder=4)
        ax.text(bxx + bw / 2, by + 26 + 22, _wrap(p["text"], chars_for(bw - 32, 11.6)), color=INK, fontsize=11.6, ha="center", va="top",
                zorder=4, linespacing=1.3)
        content_bottom = max(content_bottom, by + bh)
    place_note(ax, content_bottom, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: GRID CELLS (traps / rapid recall)
# =====================================================================
def grid_cells(name, title, badge, cells, note, cap, cols=3, wrong_right=False):
    fig, ax = _fig()
    header(ax, title, badge)
    n = len(cells)
    rows = (n + cols - 1) // cols
    gap = 24
    gx0, gy0 = 44, 200
    gw = (W - 88 - (cols - 1) * gap) / cols
    gh_avail = min(150, (H - 300 - (rows - 1) * gap) / rows)
    gh_needed = 0
    for c in cells:
        if wrong_right:
            wh = text_block_h("WRONG: " + c["wrong"], gw - 32, 11.6, linespacing=1.25)
            rh = text_block_h("RIGHT: " + c["right"], gw - 32, 11.6, linespacing=1.25)
            gh_needed = max(gh_needed, 24 + wh + 20 + rh + 20)
        else:
            bh_c = text_block_h(c["body"], gw - 28, 11.4, linespacing=1.25)
            gh_needed = max(gh_needed, 36 + bh_c + 24)
    gh = max(gh_avail, gh_needed)
    for i, c in enumerate(cells):
        r, cc = divmod(i, cols)
        x = gx0 + cc * (gw + gap)
        y = gy0 + r * (gh + gap)
        if wrong_right:
            ax.add_patch(FancyBboxPatch((x, y), gw, gh, boxstyle="round,pad=0,rounding_size=6",
                                         facecolor=TRAP_BG, edgecolor=TRAP_BORDER, linewidth=1.3, zorder=2))
            ax.text(x + 16, y + 24, _wrap("WRONG: " + c["wrong"], chars_for(gw - 32, 11.6)), color=RED, fontsize=11.6,
                    fontweight="bold", va="top", ha="left", zorder=3, linespacing=1.25)
            ax.text(x + 16, y + gh * 0.56, _wrap("RIGHT: " + c["right"], chars_for(gw - 32, 11.6)), color="#166a52",
                    fontsize=11.6, fontweight="bold", va="top", ha="left", zorder=3, linespacing=1.25)
        else:
            ax.add_patch(FancyBboxPatch((x, y), gw, 36, boxstyle="round,pad=0,rounding_size=5",
                                         facecolor=BLUE, edgecolor="none", zorder=2))
            ax.text(x + gw / 2, y + 18, c["head"], color=WHITE, fontsize=12.8, fontweight="bold", ha="center",
                    va="center", zorder=3)
            ax.add_patch(FancyBboxPatch((x, y + 36), gw, gh - 36, boxstyle="round,pad=0,rounding_size=5",
                                         facecolor=WHITE, edgecolor=CARD_BORDER, linewidth=1, zorder=2))
            ax.text(x + 14, y + 36 + (gh - 36) / 2, _wrap(c["body"], chars_for(gw - 28, 11.4)), color=INK, fontsize=11.4,
                    va="center", ha="left", zorder=3, linespacing=1.25)
    bottom = gy0 + rows * (gh + gap)
    place_note(ax, bottom - gap, note)
    footer(ax, cap)
    save(fig, name)


# =====================================================================
# Generic layout: ANSWER SPINE (vertical sequence of labelled steps)
# =====================================================================
def spine_chart(name, title, badge, steps, note, cap):
    fig, ax = _fig()
    header(ax, title, badge)
    n = len(steps)
    x0 = 300
    y0, y1 = 210, H - 150
    avail = y1 - y0
    bx = x0 + 50
    bw = W - bx - 60
    text_w = bw - 60

    # Auto-fit: find the largest font/gap combo whose stacked row heights
    # (each sized to its own label+body content) fit within the available
    # vertical band; fall back to a uniform shrink if even the smallest still overflows.
    candidates = [(14.5, 12.6, 14), (13.5, 11.8, 12), (12.5, 11, 10), (11.5, 10.2, 8), (10.5, 9.6, 6)]
    row_heights, label_fs, body_fs, gap_row, total = None, None, None, None, None
    for lfs, bfs, gr in candidates:
        heights = []
        for st in steps:
            head_h = text_block_h(st["label"], text_w, lfs, linespacing=1.15)
            body_h = text_block_h(st["text"], text_w, bfs, linespacing=1.28)
            heights.append(max(60, 14 + head_h + 6 + body_h + 14))
        t = sum(heights) + gr * (n - 1)
        if t <= avail or (lfs, bfs, gr) == candidates[-1]:
            row_heights, label_fs, body_fs, gap_row, total = heights, lfs, bfs, gr, t
            break
    if total > avail:
        scale = avail / total
        row_heights = [rh * scale for rh in row_heights]
        gap_row *= scale

    cursor = y0
    content_bottom = y0
    boxes = []
    for rh in row_heights:
        boxes.append((cursor, rh))
        cursor += rh + gap_row
        content_bottom = cursor - gap_row
    ax.plot([x0, x0], [boxes[0][0] + boxes[0][1] / 2, boxes[-1][0] + boxes[-1][1] / 2], color=INK, linewidth=3, zorder=2)
    for i, (st, (by, rh)) in enumerate(zip(steps, boxes)):
        cy = by + rh / 2
        ax.add_patch(Circle((x0, cy), 16, facecolor=ORANGE, edgecolor=WHITE, linewidth=2, zorder=4))
        ax.text(x0, cy, str(i + 1), color=WHITE, fontsize=13, fontweight="bold", ha="center", va="center", zorder=5)
        ax.add_patch(FancyBboxPatch((bx, by), bw, rh, boxstyle="round,pad=0,rounding_size=6", facecolor=WHITE,
                                     edgecolor=CARD_BORDER, linewidth=1.1, zorder=3))
        ax.add_patch(Rectangle((bx, by), 10, rh, facecolor=TEAL, edgecolor="none", zorder=4))
        head_h = text_block_h(st["label"], text_w, label_fs, linespacing=1.15)
        body_h = text_block_h(st["text"], text_w, body_fs, linespacing=1.28)
        label_cy = by + 14 + head_h / 2
        body_cy = by + 14 + head_h + 6 + body_h / 2
        ax.text(bx + 28, label_cy, st["label"], color=TEAL, fontsize=label_fs, fontweight="bold", va="center",
                ha="left", zorder=4)
        ax.text(bx + 28, body_cy, _wrap(st["text"], chars_for(text_w, body_fs)), color=INK, fontsize=body_fs, va="center",
                ha="left", zorder=4, linespacing=1.28)
    place_note(ax, content_bottom, note)
    footer(ax, cap)
    save(fig, name)


print("Visual library loaded.")


# =====================================================================
# CONTENT: 30 deliverable visuals for Topic 06
# =====================================================================
def gen_all():
    cover()

    timeline_chart(
        "01_01_master_timeline_1757_1858.png",
        "1757-1858: Constitutional Master Timeline", "MASTER",
        [
            {"year": 1757, "text": "Plassey (background)"},
            {"year": 1765, "text": "Diwani grant (Topic 04)"},
            {"year": 1773, "text": "Regulating Act"},
            {"year": 1774, "text": "Supreme Court starts"},
            {"year": 1781, "text": "Amending Act"},
            {"year": 1784, "text": "Pitt's India Act"},
            {"year": 1786, "text": "Act of 1786"},
            {"year": 1793, "text": "Charter Act, 20-yr"},
            {"year": 1813, "text": "Charter Act, trade"},
            {"year": 1833, "text": "Charter Act, GG-India"},
            {"year": 1853, "text": "Charter Act, no term"},
            {"year": 1858, "text": "1858 Act, Crown rule"},
        ],
        "Topic 06 owns constitutional structure from 1773 to the 1858 transfer. 1757/1765 shown only as background triggers -- full detail is Topic 04.",
        "Fig 1. Twelve-point constitutional spine, Regulating Act 1773 to the Government of India Act 1858. Not to scale.",
    )

    standoff_chart(
        "02_02_corporation_sovereignty_contradiction.png",
        "The Company's Contradiction, 1765-72", "SECTION A",
        "Company as Merchant",
        ["Chartered trading corporation, London HQ", "Court of Directors answerable to shareholders", "Purpose: profit from Asian trade"],
        "Company as Sovereign",
        ["Diwani revenue authority in Bengal (1765)", "Raises armies, makes war and peace", "Dispenses justice via Diwani/Nizamat courts"],
        "ONE BODY,\nTWO ROLES",
        "FACT: this structural contradiction, not humanitarian concern, forced Parliament to act after 1772 (Sekhar Bandyopadhyay; Bipin Chandra).",
        "Fig 2. A profit-seeking corporation exercising the powers of a territorial state.",
    )

    flow_chart(
        "03_03_crisis_to_regulation_causal_chain.png",
        "Crisis-to-Regulation Causal Chain, 1770-73", "SECTION A",
        [
            {"head": "1. Bengal revenue crisis, 1770", "body": "Famine and revenue mismanagement strain Company finances even as land-revenue demand stays high.", "color": RED},
            {"head": "2. Company's loan request, 1772", "body": "Company applies to the British government for a loan -- exposes financial mismanagement to Parliament.", "color": BLUE},
            {"head": "3. Select Committee, April 1772", "body": "Parliament inquires how to define Crown-Company relations and a single centre of Indian authority.", "color": TEAL},
            {"head": "4. Patronage anxiety in Britain", "body": "Returning 'Nabobs' wealth alarms English political society; Burke (1772): Parliament's duty 'to superintend the affairs of this Company.'", "color": ORANGE},
            {"head": "5. Regulating Act, 1773", "body": "First parliamentary constitutional intervention in Company rule -- a compromise, not a takeover.", "color": NAVY},
        ],
        [(0, 1), (1, 2), (2, 4), (3, 4)],
        "ANALYSIS: fiscal crisis and patronage anxiety -- not compassion for famine victims -- are the documented drivers of 1773.",
        "Fig 3. From revenue crisis to the Regulating Act: a causal chain, not a reform narrative.",
        cols=2,
    )

    org_chart(
        "04_04_1773_institutional_chart.png",
        "Regulating Act, 1773: Institutional Chart", "SECTION B",
        {"head": "Regulating Act, 1773", "body": "Parliament's first constitutional intervention: recognises a parliamentary right to oversee Company affairs."},
        [
            {"head": "Governor-General of Bengal + Council of 4", "body": "Warren Hastings, first holder. Legislative + executive power vested in GG-in-Council.", "color": TEAL},
            {"head": "Supreme Court at Calcutta", "body": "Provided for by the Act; constituted under the 1774 Charter; justice for Europeans, employees, Calcutta's citizens.", "color": BLUE},
            {"head": "Court of Directors", "body": "Obliged to lay all civil, military and revenue correspondence before the British Ministry.", "color": ORANGE},
        ],
        "TRAP: this creates a Governor-General of BENGAL, not of India -- the 1833 Act alone renames the office.",
        "Fig 4. The Regulating Act's three new institutions and their reporting lines.",
        grandchildren=[
            ["Superintends Bombay/Madras in war and peace, 'except in emergency situations' -- a loophole 1784 later closes"],
            ["Jurisdiction clashes with Company authority -- Nand Kumar, Patna, Cossijurah (Section C)"],
            ["Council could outvote the Governor-General 3-1 -- Hastings-Council deadlock (visual 5)"],
        ],
    )

    standoff_chart(
        "05_05_hastings_council_deadlock.png",
        "The Hastings-Council Deadlock, 1774-76", "SECTION B",
        "Warren Hastings (Governor-General)",
        ["One vote among four in Council", "Sought continuity of Bengal policy", "Executive authority, but no majority"],
        "Clavering, Monson, Francis (majority bloc)",
        ["Three votes could outvote the GG on any matter", "Opposed Hastings' Bengal policy repeatedly", "Deadlock through much of 1774-76"],
        "3 VOTES\nBEAT 1",
        "FACT: Monson's death (1776) restored Hastings' casting vote -- a chance event, not a statutory fix; the design flaw itself was only corrected by Pitt's India Act's 3-member council in 1784.",
        "Fig 5. Why 'Governor-General' meant little without a reliable Council majority.",
    )

    venn_chart(
        "06_06_supreme_court_jurisdiction_overlap.png",
        "Supreme Court vs Company Authority: Jurisdiction Overlap", "SECTION C",
        "Company Courts",
        ["Diwani/Nizamat Adalats", "Revenue and zamindari disputes", "Persian/Mughal-derived procedure"],
        "Supreme Court, Calcutta",
        ["Crown's charter court (from 1774)", "British subjects in Calcutta", "English common-law procedure"],
        "Disputed zone",
        ["Company servants' official acts", "Nand Kumar trial, 1775", "Patna case, 1777-79", "Cossijurah case, 1779-80"],
        "CAUTION: Nand Kumar/Patna/Cossijurah facts below are externally corroborated (not in the local OCR corpus) and presented source-critically, without sensationalising.",
        "Fig 6. Two legal orders with no settled boundary -- the problem the 1781 Amending Act tried to fix.",
    )

    matrix_table(
        "07_07_1781_corrections_map.png",
        "Amending Act (Act of Settlement), 1781: Corrections Map", "SECTION D",
        ["Area of confusion under 1773", "Correction made by the 1781 Act"],
        [
            ["Governor-General-in-Council's official acts", "Exempted from the Supreme Court's jurisdiction when done in an official/public capacity"],
            ["Revenue-collection matters", "Excluded from the Supreme Court; routed to the Company's own revenue courts and to appeal before the GG-in-Council"],
            ["Personal law of Hindus and Muslims", "Supreme Court directed to apply Hindu law to Hindus and Muslim law to Muslims in personal-law matters"],
            ["Appeals from provincial courts", "Directed to the Governor-General-in-Council / Sadar Diwani Adalat, not the Supreme Court"],
        ],
        "LIMIT: Sekhar Bandyopadhyay notes the 1781 Act 'defined more precisely the jurisdiction of the Supreme Court, but did not address the other anomalies' -- e.g. the Council-GG deadlock persisted till 1784/1786.",
        "Fig 7. What 1781 actually fixed -- jurisdiction only, not the Council deadlock or presidency ambiguity.",
        first_col_w=520,
    )

    matrix_table(
        "08_08_1773_vs_1784_matrix.png",
        "1773 vs 1784: What Actually Changed", "SECTION E",
        ["Feature", "Regulating Act, 1773", "Pitt's India Act, 1784"],
        [
            ["Bengal Council size", "Governor-General + 4 -- GG needed 2 allies to prevail", "Governor-General + 3 -- GG needed only 1 ally to prevail"],
            ["Crown oversight body", "None -- only a duty to report to the Ministry", "Board of Control: 6 members incl. a Secretary of State and the Chancellor of the Exchequer"],
            ["Presidency subordination", "War/peace only, 'except in emergency situations'", "Clearly extended to war, diplomacy AND revenue"],
            ["Urgent-orders channel", "Not provided", "Secret Committee of Directors carries Board's binding orders"],
            ["Company trade monopoly", "Untouched", "Untouched -- retained in exchange for administrative control"],
        ],
        "TRAP: Pitt's India Act did not end Company rule -- it created dual control (Board of Control + Court of Directors), the classic 'divided sovereignty' design.",
        "Fig 8. 1784 as a corrective repair of 1773's two design flaws: council deadlock and vague subordination.",
        first_col_w=340,
    )

    org_chart(
        "09_09_british_dual_control_diagram.png",
        "Dual Control in Britain, from 1784", "SECTION E",
        {"head": "Government of India (Governor-General-in-Council, Bengal)", "body": "Administers India under joint supervision from London."},
        [
            {"head": "Board of Control (Crown side)", "body": "6 Commissioners incl. a Secretary of State + Chancellor of the Exchequer + 4 Privy Councillors. 'Superintend, direct and control' civil, military and revenue affairs.", "color": BLUE},
            {"head": "Court of Directors (Company side)", "body": "Retains patronage: appointment/dismissal of Company officials in India; commercial administration.", "color": ORANGE},
        ],
        "TRAP: do not confuse this British 'dual control' (1784, London-based, Board vs Directors) with the Bengal 'Dual Government' (1765-72, Nawab's Nizamat vs Company's Diwani -- Topic 04).",
        "Fig 9. Two London bodies sharing supervision of one Indian government.",
        grandchildren=[
            ["Orders binding on the Court of Directors"],
            ["Urgent orders pass via a Secret Committee of Directors"],
        ],
    )

    flow_chart(
        "10_10_1786_executive_override.png",
        "The Act of 1786: Fixing the Executive Deadlock", "SECTION F",
        [
            {"head": "Before, 1773-84", "body": "Governor-General bound by Council's majority vote; Hastings-Council deadlock (1774-76) shows the risk.", "color": RED},
            {"head": "After, Act of 1786", "body": "Governor-General empowered to overrule the Council 'in matters of importance affecting safety, peace, or the interests of the Empire.' Cornwallis also holds Governor-General and Commander-in-Chief together.", "color": TEAL},
        ],
        [(0, 1)],
        "FACT: this is a precise, bounded power -- override in specified matters, not a general dictatorship; it answers the 1774-76 deadlock directly.",
        "Fig 10. From collective deadlock to a Governor-General who can act.",
        cols=2,
    )

    ladder_chart(
        "11_11_charter_act_ladder.png",
        "The Charter-Act Ladder, 1773-1858", "SECTION F-J",
        [
            {"label": "1773", "text": "Regulating Act"},
            {"label": "1784", "text": "Pitt's India Act"},
            {"label": "1793", "text": "Charter renewed, 20 yrs"},
            {"label": "1813", "text": "Trade opened, tea/China kept"},
            {"label": "1833", "text": "GG of India, Law Member"},
            {"label": "1853", "text": "No fixed term, exam opened"},
            {"label": "1858", "text": "Company rule ends"},
        ],
        "Each step both corrects the previous act's defect and adds a further layer of parliamentary/Crown control.",
        "Fig 11. Seven statutory steps, one direction of travel: control tightens, Company shrinks.",
    )

    matrix_table(
        "12_12_1813_monopoly_opening.png",
        "Charter Act, 1813: What Opened, What Stayed Shut", "SECTION G",
        ["Domain", "Charter Act, 1813 position"],
        [
            ["General trade with India", "Opened to all British subjects -- Company monopoly ended"],
            ["Tea trade / trade with China", "Remained exclusive to the Company"],
            ["Government and revenues of India", "Continued in the Company's hands -- NOT transferred to Parliament"],
            ["Crown sovereignty", "Act asserted the 'undoubted sovereignty of the Crown of the United Kingdom' over Company territories"],
            ["Missionaries", "Permitted entry into Company territories for the first time"],
            ["Education grant", "Rs 1 lakh/year sanctioned -- but not actually disbursed by the Company until 1823 (implementation gap; detail: Topic 09)"],
        ],
        "PYQ 2019 GS-I Q4 turns on exactly this row-by-row structure -- see Part X for the full solved audit.",
        "Fig 12. 1813 as a partial, not total, opening -- and a statute whose promise outran its practice.",
        first_col_w=460,
    )

    org_chart(
        "13_13_1833_all_india_centralisation.png",
        "Charter Act, 1833: All-India Centralisation", "SECTION H",
        {"head": "Government of India, 1833", "body": "Single legislating, all-India authority replaces separate presidency law-making."},
        [
            {"head": "Governor-General of India", "body": "William Bentinck, first holder -- the former Governor-General of Bengal is now GG of India.", "color": TEAL},
            {"head": "Central Legislative Council", "body": "Adds a Law Member (Macaulay, first holder) for the first time.", "color": BLUE},
            {"head": "Company, post-1833", "body": "Loses its remaining China/tea trade monopoly; becomes a purely administrative agency holding India 'in trust' for the Crown.", "color": ORANGE},
        ],
        "TRAP: Governor-General of BENGAL (1773) is not Governor-General of INDIA (1833) -- the single commonest error in this topic.",
        "Fig 13. Bentinck's title change is the constitutional marker of all-India centralisation.",
        grandchildren=[
            [],
            ["Law Commission provided for -- codification pipeline (visual 14)", "Non-discrimination clause (Section 87) -- promise vs practice (visual 15)"],
            [],
        ],
    )

    flow_chart(
        "14_14_codification_pipeline.png",
        "The Codification Pipeline, from 1833", "SECTION H",
        [
            {"head": "1. Charter Act, 1833", "body": "Provides for a Law Member and a Law Commission to prepare uniform codes for British India.", "color": NAVY},
            {"head": "2. First Law Commission, from 1834", "body": "Macaulay chairs the Commission as first Law Member; drafts begin.", "color": TEAL},
            {"head": "3. Draft codes prepared", "body": "E.g. a Penal Code draft is prepared under Macaulay's Commission.", "color": BLUE},
            {"head": "4. Enactment, post-1858", "body": "Codes such as the Indian Penal Code are enacted only in 1860 -- AFTER the Crown transfer; owned by later topics, not claimed here.", "color": ORANGE},
        ],
        [(0, 1), (1, 2), (2, 3)],
        "CAUTION: the pipeline originates in 1833, but actual code enactment falls after 1858 -- do not backdate the codes themselves into this topic's window.",
        "Fig 14. From a constitutional provision (1833) to codified law (enacted after 1858).",
        cols=2,
    )

    standoff_chart(
        "15_15_1833_promise_vs_practice.png",
        "Charter Act 1833: Non-Discrimination -- Promise vs Practice", "SECTION H",
        "1833 Promise (Section 87)",
        ["'No native...by reason only of his religion, place of birth, descent, colour...be disabled from holding any place, office, or employment'"],
        "1833-1853 Practice",
        ["Covenanted civil service stayed almost entirely European", "Recruitment/patronage channels remained in Britain", "Real access waited on the 1853 exam framework -- and even then, sat only in London"],
        "GAP",
        "FACT: Section 87's wording is a real statutory promise; ANALYSIS: the promise-practice gap is itself a standard UPSC theme, not a modern gloss.",
        "Fig 15. A formal equality clause with no matching change in recruitment practice.",
    )

    org_chart(
        "16_16_1853_legislative_executive_split.png",
        "Charter Act, 1853: Legislative-Executive Split", "SECTION I",
        {"head": "Governor-General's Council, pre-1853", "body": "One body handled both executive government and legislation together."},
        [
            {"head": "Executive Council, from 1853", "body": "Continues day-to-day government of India.", "color": TEAL},
            {"head": "Legislative Council, from 1853", "body": "Enlarged with additional legislative members sitting separately for law-making -- includes members associated with the presidencies/provinces (exact seat count not confirmed from local sources).", "color": BLUE},
        ],
        "CAUTION: presidency-representation composition is well corroborated externally, but is flagged here as not drawn from this repository's local OCR corpus -- treat seat-by-seat counts as indicative, not statutory quotation.",
        "Fig 16. Executive and legislative business formally separated for the first time.",
    )

    ladder_chart(
        "17_17_civil_service_reform_sequence.png",
        "Civil-Service Reform Sequence, 1833 to 1855", "SECTION I",
        [
            {"label": "1833", "text": "'Open' principle announced"},
            {"label": "1853", "text": "Act ends Directors' patronage monopoly"},
            {"label": "1854", "text": "Macaulay Committee designs exam"},
            {"label": "1855", "text": "First competitive exam actually held"},
        ],
        "TRAP: 1853 alone did not instantly operationalise competition -- the exam mechanism came from the 1854 Macaulay Committee, first sat in 1855; detailed service structure is routed to Topic 08.",
        "Fig 17. Four distinct steps compressed by careless answers into a single date.",
    )

    flow_chart(
        "18_18_1858_transfer_flow.png",
        "The 1858 Transfer of Authority", "SECTION J",
        [
            {"head": "Abolished", "body": "East India Company's rule; Board of Control; Court of Directors all cease.", "color": RED},
            {"head": "Created", "body": "Secretary of State for India (in the Cabinet) + a 15-member Council of India (7 from the former Directors).", "color": TEAL},
            {"head": "Renamed", "body": "Governor-General of India also becomes Viceroy -- Canning holds both titles at the transfer.", "color": BLUE},
            {"head": "Continued", "body": "Covenanted civil service and its 1853 exam framework; army and administrative personnel; day-to-day machinery of government.", "color": ORANGE},
        ],
        [(0, 1), (1, 2), (2, 3)],
        "FACT (Sekhar Bandyopadhyay): the 1858 Act 'meant more continuation than change' -- structure continued even as the sovereign changed.",
        "Fig 18. What ended, what began, and what simply carried on in 1858.",
        cols=2,
    )

    org_chart(
        "19_19_secretary_of_state_council_structure.png",
        "Secretary of State for India + Council of India, 1858", "SECTION J",
        {"head": "Secretary of State for India", "body": "Cabinet minister; 'in subordination to the cabinet, the fountain of authority as well as the director of policy in India' (Sekhar Bandyopadhyay)."},
        [
            {"head": "Council of India -- 15 members", "body": "7 selected from the former Court of Directors; remainder Crown-appointed. Advisory -- Secretary of State could override it in urgent/confidential matters.", "color": TEAL},
            {"head": "Governor-General / Viceroy, India", "body": "Retains his powers, but now answerable ONLY to the Secretary of State -- dual control (Board + Directors) ends.", "color": BLUE},
        ],
        "TRAP: do not call the Council of India a legislature -- it is a London-based advisory body to the Secretary of State, distinct from India's own legislative councils (Topic 12).",
        "Fig 19. One accountable minister replaces two competing London authorities.",
    )

    matrix_table(
        "20_20_company_to_crown_continuity_matrix.png",
        "Company to Crown, 1858: Continuity and Change", "SECTION J",
        ["Institution", "Changed in 1858?"],
        [
            ["Sovereign authority over India", "CHANGED -- Company to Crown"],
            ["Board of Control / Court of Directors", "CHANGED -- abolished, replaced by Secretary of State + Council of India"],
            ["Governor-General's executive powers", "CONTINUED -- retained, plus the new title 'Viceroy'"],
            ["Civil-service exam framework (1853/1855)", "CONTINUED -- carried on unchanged"],
            ["Army, administrative personnel", "CONTINUED -- structural and staff continuity"],
            ["Indian representation in government", "UNCHANGED -- still none in 1858 itself (Topic 12 covers later councils)"],
        ],
        "VERDICT: 1858 changed the sovereign's name and the London supervisory machinery; it did not rebuild the Indian executive from scratch.",
        "Fig 20. Six institutions, sorted by what 1858 actually altered.",
        first_col_w=520,
    )

    ladder_chart(
        "21_21_office_title_ladder.png",
        "Office-Title Ladder: One Chair, Four Names", "SECTION K",
        [
            {"label": "1773", "text": "Governor-General of Bengal (Hastings)"},
            {"label": "1784", "text": "Same title, 3-member Council (reform)"},
            {"label": "1833", "text": "Governor-General of India (Bentinck)"},
            {"label": "1858", "text": "Governor-General AND Viceroy (Canning)"},
        ],
        "PYQ 2023 GS-I Q50 turns on exactly this ladder -- see Part X for the full solved audit.",
        "Fig 21. Same office, evolving title and jurisdiction -- 1773 to 1858.",
    )

    spectrum_chart(
        "22_22_indian_exclusion_spectrum.png",
        "Indian Exclusion Spectrum, 1793-1858", "SECTION K",
        "Total exclusion",
        "Formal equality only",
        [
            {"x": 0.08, "label": "1793 rule", "text": "Posts over 500 pounds/year salary reserved for Englishmen -- explicit racial bar", "above": True},
            {"x": 0.38, "label": "1833 Sec. 87", "text": "'No native...disabled...by reason of religion, birth, descent, colour' -- formal promise", "above": False},
            {"x": 0.62, "label": "1853 exam", "text": "Competition opened in principle -- but examination sat only in London", "above": True},
            {"x": 0.92, "label": "1858 reality", "text": "Covenanted service still virtually all-European at the Crown transfer", "above": False},
        ],
        "ANALYSIS: formal statutory language moved steadily toward equality; administrative practice barely moved at all across the same six decades.",
        "Fig 22. The gap between statutory promise and administrative reality, plotted across four markers.",
    )

    matrix_table(
        "23_23_historiography_matrix.png",
        "Historiography of the Company-State, 1773-1858", "SECTION L",
        ["Reading", "Core claim"],
        [
            ["Nationalist / imperial-control", "Acts regulated a corporation for British fiscal and political benefit; Indian welfare was incidental, not the motive"],
            ["Administrative / rule-of-law", "Acts built genuine institutions -- courts, codes, an examined service -- that outlasted the Company itself"],
            ["Company-state / corporate sovereignty", "The East India Company was a hybrid, improvised sovereign; historians debate how deliberate vs ad hoc its state-building was"],
            ["Free-trade / industrial-capital transition", "1813 and 1833 dismantled chartered monopoly precisely when British industry needed an open Indian market"],
        ],
        "CAUTION: named-scholar attributions here are limited to what the local corpus supports -- e.g. Thomas Metcalf's phrase 'a new attitude of caution and conservatism' (quoted in Sekhar Bandyopadhyay) for the post-1857 mood.",
        "Fig 23. Four lenses on the same sixty years -- none of them mutually exclusive.",
        first_col_w=460,
    )

    grid_cells(
        "24_24_topic_boundary_bridge.png",
        "Topic Boundary Bridge: Who Owns What", "TOPIC MAP",
        [
            {"head": "04 -- Plassey/Buxar/Diwani", "body": "Dual Government of Bengal, 1765-72 -- referenced here only as Section A's trigger."},
            {"head": "05 -- Territorial expansion", "body": "Company's growing territory that made central control necessary."},
            {"head": "06 -- THIS TOPIC", "body": "Governance structure, parliamentary control, constitutional Acts through the 1858 transfer."},
            {"head": "07 -- Colonial economic impact", "body": "Full drain-of-wealth and de-industrialisation analysis -- only flagged here, not developed."},
            {"head": "08 -- Civil service/police/judiciary", "body": "Detailed service structure -- Topic 06 covers only the constitutional milestones (1853/1854/1855)."},
            {"head": "09 -- Education/press", "body": "1813 education grant's implementation -- detailed there; Topic 06 states only the statutory provision."},
            {"head": "11 -- The Revolt, 1857", "body": "Referenced only as 1858's occasion, not developed here."},
            {"head": "12 -- Post-1858 councils/Crown", "body": "Indian Councils Acts and representative development after the 1858 endpoint."},
        ],
        "Use this map before citing any adjacent-topic fact -- Topic 06 stops at the 1858 transfer of authority.",
        "Fig 24. Eight boundary statements, one per adjacent topic.",
        cols=4,
    )

    spine_chart(
        "25_25_answer_spine_10mark.png",
        "Answer Spine: 10-Mark ('Trace the constitutional ladder')", "PRACTICE",
        [
            {"label": "Thesis", "text": "Parliament regulated a corporation step by step; each act repaired the previous act's defect."},
            {"label": "Stage 1", "text": "1773 Regulating Act -- first oversight, but a weak Council and vague presidency control."},
            {"label": "Stage 2", "text": "1784 Pitt's India Act -- Board of Control, dual control, clearer subordination."},
            {"label": "Stage 3", "text": "1833/1853 -- all-India centralisation, codification, competitive recruitment."},
            {"label": "Verdict", "text": "By 1858 the Crown inherited a ready-made state; it did not have to build one."},
        ],
        "Use for a 10-mark 'trace' or 'trajectory' directive -- three acts as stages plus one structural verdict.",
        "Fig 25. Five-step spine for a 10-mark trace/trajectory demand.",
    )

    spine_chart(
        "26_26_answer_spine_15mark.png",
        "Answer Spine: 15-Mark ('Assess dual control, 1784-1858')", "PRACTICE",
        [
            {"label": "Thesis", "text": "Dual control let Britain supervise India without owning the Company's liabilities or ending its patronage."},
            {"label": "Design", "text": "Board of Control (Crown/political) vs Court of Directors (Company/commercial) -- divided sovereignty by design."},
            {"label": "Strength", "text": "Gave Parliament a real check without a costly, disruptive full annexation of administration."},
            {"label": "Contradiction", "text": "Two masters could still disagree; urgent matters needed the Secret Committee workaround."},
            {"label": "Outcome", "text": "Dual control persisted, in modified form, until 1858, when a single Secretary of State replaced both bodies."},
            {"label": "Qualification", "text": "Do not confuse this British dual control with Bengal's 1765-72 Dual Government (Topic 04) -- different institutions, different decades."},
        ],
        "Use for a 15-mark 'assess/evaluate an institution' directive -- design, strength, contradiction, outcome, qualification.",
        "Fig 26. Six-step spine for a 15-mark institutional-evaluation demand.",
    )

    spine_chart(
        "27_27_answer_spine_20mark.png",
        "Answer Spine: 20-Mark ('1858 as endpoint -- change or continuity?')", "PRACTICE",
        [
            {"label": "Thesis", "text": "1858 changed the sovereign and the London machinery; it did not rebuild the Indian state from scratch."},
            {"label": "Trigger", "text": "The Revolt of 1857 was the occasion, but pressure for Crown takeover predates 1857 -- traders' and settlers' complaints since 1833."},
            {"label": "Changed", "text": "Company rule, Board of Control and Court of Directors abolished; Secretary of State + Council of India created."},
            {"label": "Continued", "text": "Governor-General's powers (now also Viceroy); the 1853/1855 exam framework; army and administrative personnel."},
            {"label": "Distinguish", "text": "The Act itself is not the Queen's Proclamation (separate document, same year) and not the later representative Councils Acts (Topic 12)."},
            {"label": "Qualification", "text": "Continuity does not mean nothing changed -- direct Crown accountability and a single minister were genuine, durable shifts."},
            {"label": "Verdict", "text": "1858 is the constitutional capstone of a process begun in 1773, not a fresh start."},
        ],
        "Use for a 20-mark synthesis/endpoint directive -- thesis, trigger, changed, continued, distinguish, qualify, verdict.",
        "Fig 27. Seven-step spine for a 20-mark synthesis/endpoint demand.",
    )

    grid_cells(
        "28_28_upsc_traps_grid.png",
        "UPSC Traps Grid: Structure & Constitutional Development", "PRACTICE",
        [
            {"wrong": "Regulating Act made Hastings Governor-General of India.", "right": "It made him Governor-General of BENGAL; India comes only in 1833."},
            {"wrong": "Pitt's India Act ended Company rule.", "right": "It created dual control; Company rule continued to 1858."},
            {"wrong": "British 'dual control' (1784) is the same as Bengal's 'Dual Government'.", "right": "Different institutions, different decades -- 1765-72 Bengal vs 1784 Britain."},
            {"wrong": "Charter Act 1813 ended all Company monopoly.", "right": "Tea trade and the China trade stayed exclusive to the Company."},
            {"wrong": "Charter Act 1833 introduced the competitive civil-service exam.", "right": "It only announced the open-recruitment PRINCIPLE; the exam came via the 1853 Act (first sat 1855)."},
            {"wrong": "Charter Act 1853 instantly operationalised competitive recruitment.", "right": "The Macaulay Committee (1854) designed it; the first exam sat only in 1855."},
            {"wrong": "The Law Commission was created by the 1853 Act.", "right": "The first Law Commission followed the 1833 Act."},
            {"wrong": "The Government of India Act 1858 is the same as the Queen's Proclamation.", "right": "Two separate 1858 documents -- the Act restructures government; the Proclamation is Victoria's political statement."},
            {"wrong": "1858 introduced Indian representation in government.", "right": "No Indian representation existed in 1858 itself -- that begins only with later Councils Acts (Topic 12)."},
        ],
        "Nine of the topic's highest-frequency confusions, each with its precise correction.",
        "Fig 28. A trap grid built directly from this topic's named evidence units.",
        cols=3,
        wrong_right=True,
    )

    grid_cells(
        "29_29_rapid_recall_grid.png",
        "Rapid-Recall Grid: 1757-1858 in 12 Facts", "PRACTICE",
        [
            {"head": "1765", "body": "Diwani grant creates the revenue-authority trigger (Topic 04 detail)."},
            {"head": "1772", "body": "Select Committee (April) inquires into Company affairs after its loan request."},
            {"head": "1773", "body": "Regulating Act: GG of Bengal + Council of 4; Supreme Court framework."},
            {"head": "1774", "body": "Supreme Court at Calcutta begins functioning under the 1774 Charter."},
            {"head": "1781", "body": "Amending Act fixes Supreme Court jurisdiction only, not the Council deadlock."},
            {"head": "1784", "body": "Pitt's India Act: Board of Control (6) + 3-member Bengal Council."},
            {"head": "1786", "body": "GG (Cornwallis) can override Council in safety/peace/Empire matters."},
            {"head": "1793", "body": "Charter renewed 20 years; regulations codified and printed with translations."},
            {"head": "1813", "body": "Trade opened except tea/China; Crown sovereignty asserted; Rs 1 lakh education grant."},
            {"head": "1833", "body": "GG of INDIA (Bentinck); Law Member (Macaulay); Company purely administrative."},
            {"head": "1853", "body": "No fixed renewal term; legislative/executive split; exam principle opened."},
            {"head": "1858", "body": "Company, Board of Control, Directors abolished; Secretary of State + Viceroy (Canning)."},
        ],
        "Twelve dated facts for last-minute revision -- cross-check each against the full teaching text before an exam.",
        "Fig 29. The topic's chronology compressed to one fact per box.",
        cols=4,
    )

    print("All 30 visuals generated.")


if __name__ == "__main__":
    gen_all()
