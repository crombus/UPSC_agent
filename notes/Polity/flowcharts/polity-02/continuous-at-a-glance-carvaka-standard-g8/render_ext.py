"""Bespoke block primitives authored for Polity 02 — Making of the Constitution.

These are additions to the proven g9 engine, not replacements. They exist because the
Polity 02 argument needs shapes that the Polity 01 flow never required: a legitimacy
funnel, a seat-allocation diagram, an officer role map, a committee hierarchy, a
multi-reading pipeline, a metric dashboard and a source-adaptation map.
"""
from __future__ import annotations

import render_lib as R
from render_lib import (
    BG, CARD, CARD_TITLE, CYAN, TEAL, AMBER, YELLOW, MAGENTA, GREEN, RED,
    WHITE, DIM, GREY, RULE, col, line_h, text_w, rrect, wrap_runs, draw_runs_line,
    arrow_right, arrow_down, parse_runs,
)


# ---- dash : metric dashboard of big numbers ---------------------------------
def _dash_geom(ctx, b, width):
    per = b.get("per_row", 3)
    gap = 28
    cw = (width - gap * (per - 1)) / per
    return per, gap, cw


def _dash_cell_h(ctx, it, cw):
    h = 14 + line_h(ctx.f.big) + 6
    h += len(wrap_runs([(it["l"], ctx.f.smallb, WHITE)], cw - 36, "dash")) * (line_h(ctx.f.smallb) + 3)
    if it.get("s"):
        h += 6 + len(wrap_runs([(it["s"], ctx.f.small, DIM)], cw - 36, "dash")) * (line_h(ctx.f.small) + 3)
    return h + 16


def _dash_h(ctx, b, width):
    per, gap, cw = _dash_geom(ctx, b, width)
    rows = [b["items"][i:i + per] for i in range(0, len(b["items"]), per)]
    return sum(max(_dash_cell_h(ctx, it, cw) for it in r) for r in rows) + 24 * (len(rows) - 1)


def _dash_draw(ctx, d, b, x, y, width):
    per, gap, cw = _dash_geom(ctx, b, width)
    rows = [b["items"][i:i + per] for i in range(0, len(b["items"]), per)]
    cy = y
    for r in rows:
        rh = max(_dash_cell_h(ctx, it, cw) for it in r)
        for i, it in enumerate(r):
            c = col(it.get("c", "cyan"))
            cx = x + i * (cw + gap)
            rrect(d, [cx, cy, cx + cw, cy + rh], radius=16, fill=CARD_TITLE, outline=c, width=3)
            d.rectangle([cx, cy + rh - 7, cx + cw, cy + rh], fill=c)
            d.text((cx + 18, cy + 8), it["n"], font=ctx.f.big, fill=c)
            nx = cx + 18 + text_w(ctx.f.big, it["n"]) + 14
            ty = cy + 14 + line_h(ctx.f.big) + 6
            if it.get("u"):
                d.text((nx, cy + 8 + line_h(ctx.f.big) - line_h(ctx.f.smallb) - 8),
                       it["u"], font=ctx.f.smallb, fill=DIM)
            for ln in wrap_runs([(it["l"], ctx.f.smallb, WHITE)], cw - 36, "dash"):
                draw_runs_line(d, cx + 18, ty, ln)
                ty += line_h(ctx.f.smallb) + 3
            if it.get("s"):
                ty += 6
                for ln in wrap_runs([(it["s"], ctx.f.small, DIM)], cw - 36, "dash"):
                    draw_runs_line(d, cx + 18, ty, ln)
                    ty += line_h(ctx.f.small) + 3
        cy += rh + 24
    return cy - 24 - y


# ---- alloc : proportional seat-allocation diagram ---------------------------
def _alloc_geom(ctx, b, width):
    gap = 30
    tot = sum(p["w"] for p in b["parts"])
    avail = width - gap * (len(b["parts"]) - 1)
    return gap, [avail * p["w"] / tot for p in b["parts"]]


def _alloc_part_h(ctx, p, pw):
    h = 12 + line_h(ctx.f.num) + 4
    h += len(wrap_runs([(p["l"], ctx.f.smallb, WHITE)], pw - 32, "alloc")) * (line_h(ctx.f.smallb) + 3)
    for s in p.get("sub", []):
        h += 8 + len(wrap_runs(parse_runs(s, ctx.f.small, ctx.f.smallb, DIM, WHITE),
                               pw - 46, "alloc")) * (line_h(ctx.f.small) + 3)
    return h + 16


def _alloc_h(ctx, b, width):
    gap, ws = _alloc_geom(ctx, b, width)
    top = 16 + line_h(ctx.f.num) + 8 + line_h(ctx.f.smallb) + 12
    return top + 54 + max(_alloc_part_h(ctx, p, w) for p, w in zip(b["parts"], ws))


def _alloc_draw(ctx, d, b, x, y, width):
    gap, ws = _alloc_geom(ctx, b, width)
    t = b["total"]
    tc = col(t.get("c", "yellow"))
    top_h = 16 + line_h(ctx.f.num) + 8 + line_h(ctx.f.smallb) + 12
    rrect(d, [x, y, x + width, y + top_h], radius=16, fill=CARD_TITLE, outline=tc, width=4)
    d.text((x + 24, y + 10), t["n"], font=ctx.f.num, fill=tc)
    lx = x + 24 + text_w(ctx.f.num, t["n"]) + 22
    d.text((lx, y + 10 + line_h(ctx.f.num) - line_h(ctx.f.head) - 6), t["l"], font=ctx.f.head, fill=WHITE)
    d.text((x + 24, y + 16 + line_h(ctx.f.num) + 4), t["s"], font=ctx.f.smallb, fill=DIM)

    bus = y + top_h + 26
    d.line([(x + width / 2, y + top_h), (x + width / 2, bus)], fill=tc, width=5)
    cxs = []
    cx = x
    for w in ws:
        cxs.append(cx + w / 2)
        cx += w + gap
    d.line([(min(cxs), bus), (max(cxs), bus)], fill=tc, width=5)

    ph = max(_alloc_part_h(ctx, p, w) for p, w in zip(b["parts"], ws))
    cx = x
    for p, w in zip(b["parts"], ws):
        c = col(p.get("c", "cyan"))
        py = bus + 28
        arrow_down(d, cx + w / 2, bus, py - 2, c, thick=5, head=14)
        rrect(d, [cx, py, cx + w, py + ph], radius=14, fill=CARD, outline=c, width=3)
        d.text((cx + 16, py + 8), p["n"], font=ctx.f.num, fill=c)
        ty = py + 12 + line_h(ctx.f.num) + 4
        for ln in wrap_runs([(p["l"], ctx.f.smallb, WHITE)], w - 32, "alloc"):
            draw_runs_line(d, cx + 16, ty, ln)
            ty += line_h(ctx.f.smallb) + 3
        for s in p.get("sub", []):
            ty += 8
            d.line([(cx + 16, ty + 6), (cx + 16, ty + 22)], fill=c, width=3)
            for ln in wrap_runs(parse_runs(s, ctx.f.small, ctx.f.smallb, DIM, WHITE), w - 46, "alloc"):
                draw_runs_line(d, cx + 30, ty, ln)
                ty += line_h(ctx.f.small) + 3
        cx += w + gap
    return bus + 28 + ph - y


# ---- funnel : narrowing selection funnel ------------------------------------
def _funnel_widths(b, width):
    n = len(b["steps"])
    end = b.get("end", 0.46)
    return [width * (1 - (1 - end) * i / max(1, n - 1)) for i in range(n)]


def _funnel_step_h(ctx, s, w):
    h = 12 + len(wrap_runs([(s["t"], ctx.f.chain, WHITE)], w - 34, "funnel")) * (line_h(ctx.f.chain) + 4)
    if s.get("s"):
        h += len(wrap_runs(parse_runs(s["s"], ctx.f.chain_sub, ctx.f.smallb, DIM, WHITE),
                           w - 34, "funnel")) * (line_h(ctx.f.chain_sub) + 3)
    return h + 12


def _funnel_h(ctx, b, width):
    ws = _funnel_widths(b, width)
    return sum(_funnel_step_h(ctx, s, w) for s, w in zip(b["steps"], ws)) + 46 * (len(b["steps"]) - 1)


def _funnel_draw(ctx, d, b, x, y, width):
    ws = _funnel_widths(b, width)
    cy = y
    for i, (s, w) in enumerate(zip(b["steps"], ws)):
        c = col(s.get("c", "cyan"))
        h = _funnel_step_h(ctx, s, w)
        bx = x + (width - w) / 2
        rrect(d, [bx, cy, bx + w, cy + h], radius=14, fill=CARD_TITLE, outline=c, width=3)
        d.rectangle([bx, cy + 6, bx + 8, cy + h - 6], fill=c)
        ty = cy + 6
        for ln in wrap_runs([(s["t"], ctx.f.chain, c)], w - 34, "funnel"):
            draw_runs_line(d, bx + 22, ty, ln)
            ty += line_h(ctx.f.chain) + 4
        if s.get("s"):
            for ln in wrap_runs(parse_runs(s["s"], ctx.f.chain_sub, ctx.f.smallb, DIM, WHITE),
                                w - 34, "funnel"):
                draw_runs_line(d, bx + 22, ty, ln)
                ty += line_h(ctx.f.chain_sub) + 3
        if i < len(b["steps"]) - 1:
            arrow_down(d, x + width / 2, cy + h + 6, cy + h + 40, CYAN, thick=5, head=14)
            if s.get("note"):
                nt = s["note"]
                d.text((x + width / 2 + 24, cy + h + (46 - line_h(ctx.f.badge)) / 2),
                       nt, font=ctx.f.badge, fill=MAGENTA)
        cy += h + 46
    return cy - 46 - y


# ---- hub : officer / role map around a centre -------------------------------
def _hub_geom(ctx, b, width):
    gap = 34
    cw = width * b.get("centre_w", 0.30)
    sw = (width - cw - gap * 2) / 2
    return gap, cw, sw


def _hub_spoke_h(ctx, s, sw):
    h = 10 + line_h(ctx.f.smallb) + 2
    h += len(wrap_runs([(s["n"], ctx.f.chain, WHITE)], sw - 30, "hub")) * (line_h(ctx.f.chain) + 3)
    h += len(wrap_runs([(s["s"], ctx.f.small, DIM)], sw - 30, "hub")) * (line_h(ctx.f.small) + 3)
    return h + 12


def _hub_col_h(ctx, items, sw):
    return sum(_hub_spoke_h(ctx, s, sw) for s in items) + 18 * (len(items) - 1)


def _hub_h(ctx, b, width):
    gap, cw, sw = _hub_geom(ctx, b, width)
    n = len(b["spokes"])
    left, right = b["spokes"][:(n + 1) // 2], b["spokes"][(n + 1) // 2:]
    c = b["centre"]
    ch = 18 + len(wrap_runs([(c["t"], ctx.f.head, WHITE)], cw - 36, "hub")) * (line_h(ctx.f.head) + 4)
    ch += 8 + len(wrap_runs(parse_runs(c["s"], ctx.f.small, ctx.f.smallb, DIM, WHITE),
                            cw - 36, "hub")) * (line_h(ctx.f.small) + 3) + 18
    return max(_hub_col_h(ctx, left, sw), _hub_col_h(ctx, right, sw), ch)


def _hub_draw(ctx, d, b, x, y, width):
    gap, cw, sw = _hub_geom(ctx, b, width)
    total = _hub_h(ctx, b, width)
    n = len(b["spokes"])
    left, right = b["spokes"][:(n + 1) // 2], b["spokes"][(n + 1) // 2:]
    cx0 = x + sw + gap
    cc = col(b["centre"].get("c", "yellow"))

    ch = 18 + len(wrap_runs([(b["centre"]["t"], ctx.f.head, WHITE)], cw - 36, "hub")) * (line_h(ctx.f.head) + 4)
    ch += 8 + len(wrap_runs(parse_runs(b["centre"]["s"], ctx.f.small, ctx.f.smallb, DIM, WHITE),
                            cw - 36, "hub")) * (line_h(ctx.f.small) + 3) + 18
    cy0 = y + (total - ch) / 2
    rrect(d, [cx0, cy0, cx0 + cw, cy0 + ch], radius=18, fill=(22, 44, 58), outline=cc, width=5)
    ty = cy0 + 14
    for ln in wrap_runs([(b["centre"]["t"], ctx.f.head, cc)], cw - 36, "hub"):
        draw_runs_line(d, cx0 + 18, ty, ln)
        ty += line_h(ctx.f.head) + 4
    ty += 8
    for ln in wrap_runs(parse_runs(b["centre"]["s"], ctx.f.small, ctx.f.smallb, DIM, WHITE),
                        cw - 36, "hub"):
        draw_runs_line(d, cx0 + 18, ty, ln)
        ty += line_h(ctx.f.small) + 3

    for side, items in (("L", left), ("R", right)):
        colh = _hub_col_h(ctx, items, sw)
        cy = y + (total - colh) / 2
        bx = x if side == "L" else cx0 + cw + gap
        for s in items:
            c = col(s.get("c", "cyan"))
            h = _hub_spoke_h(ctx, s, sw)
            rrect(d, [bx, cy, bx + sw, cy + h], radius=13, fill=CARD_TITLE, outline=c, width=3)
            d.text((bx + 16, cy + 6), s["h"], font=ctx.f.smallb, fill=c)
            ty = cy + 10 + line_h(ctx.f.smallb) + 2
            for ln in wrap_runs([(s["n"], ctx.f.chain, WHITE)], sw - 30, "hub"):
                draw_runs_line(d, bx + 16, ty, ln)
                ty += line_h(ctx.f.chain) + 3
            for ln in wrap_runs([(s["s"], ctx.f.small, DIM)], sw - 30, "hub"):
                draw_runs_line(d, bx + 16, ty, ln)
                ty += line_h(ctx.f.small) + 3
            my = cy + h / 2
            if side == "L":
                d.line([(bx + sw, my), (bx + sw + gap / 2, my)], fill=c, width=3)
                d.line([(bx + sw + gap / 2, my), (bx + sw + gap / 2, cy0 + ch / 2)], fill=c, width=3)
            else:
                d.line([(bx - gap / 2, my), (bx, my)], fill=c, width=3)
                d.line([(bx - gap / 2, my), (bx - gap / 2, cy0 + ch / 2)], fill=c, width=3)
            cy += h + 18
    return total


# ---- tree : committee hierarchy ---------------------------------------------
def _tree_geom(ctx, b, width):
    gap = 30
    n = len(b["branches"])
    return gap, (width - gap * (n - 1)) / n


def _tree_leaf_h(ctx, lf, bw):
    h = 10 + len(wrap_runs([(lf["t"], ctx.f.smallb, WHITE)], bw - 30, "tree")) * (line_h(ctx.f.smallb) + 3)
    h += len(wrap_runs([(lf["s"], ctx.f.small, DIM)], bw - 30, "tree")) * (line_h(ctx.f.small) + 3)
    return h + 10


def _tree_branch_h(ctx, br, bw):
    h = line_h(ctx.f.smallb) + 18 + 14
    h += sum(_tree_leaf_h(ctx, lf, bw) for lf in br["leaves"]) + 12 * (len(br["leaves"]) - 1)
    return h


def _tree_h(ctx, b, width):
    gap, bw = _tree_geom(ctx, b, width)
    root_h = 14 + line_h(ctx.f.head) + 6 + line_h(ctx.f.small) + 14
    return root_h + 50 + max(_tree_branch_h(ctx, br, bw) for br in b["branches"])


def _tree_draw(ctx, d, b, x, y, width):
    gap, bw = _tree_geom(ctx, b, width)
    rc = col(b["root"].get("c", "yellow"))
    root_h = 14 + line_h(ctx.f.head) + 6 + line_h(ctx.f.small) + 14
    rw = width * 0.44
    rx = x + (width - rw) / 2
    rrect(d, [rx, y, rx + rw, y + root_h], radius=16, fill=(22, 44, 58), outline=rc, width=4)
    d.text((rx + 20, y + 12), b["root"]["t"], font=ctx.f.head, fill=rc)
    d.text((rx + 20, y + 14 + line_h(ctx.f.head) + 6), b["root"]["s"], font=ctx.f.small, fill=DIM)

    bus = y + root_h + 24
    d.line([(x + width / 2, y + root_h), (x + width / 2, bus)], fill=rc, width=5)
    cxs = [x + i * (bw + gap) + bw / 2 for i in range(len(b["branches"]))]
    d.line([(min(cxs), bus), (max(cxs), bus)], fill=rc, width=5)

    for i, br in enumerate(b["branches"]):
        c = col(br.get("c", "cyan"))
        bx = x + i * (bw + gap)
        arrow_down(d, bx + bw / 2, bus, bus + 24, c, thick=4, head=12)
        cy = bus + 26
        hb = line_h(ctx.f.smallb) + 18
        rrect(d, [bx, cy, bx + bw, cy + hb], radius=12, fill=c)
        d.text((bx + 16, cy + 8), br["h"], font=ctx.f.smallb, fill=BG)
        cy += hb + 14
        for lf in br["leaves"]:
            h = _tree_leaf_h(ctx, lf, bw)
            rrect(d, [bx, cy, bx + bw, cy + h], radius=11, fill=CARD_TITLE, outline=c, width=2)
            ty = cy + 6
            for ln in wrap_runs([(lf["t"], ctx.f.smallb, WHITE)], bw - 30, "tree"):
                draw_runs_line(d, bx + 15, ty, ln)
                ty += line_h(ctx.f.smallb) + 3
            for ln in wrap_runs([(lf["s"], ctx.f.small, c)], bw - 30, "tree"):
                draw_runs_line(d, bx + 15, ty, ln)
                ty += line_h(ctx.f.small) + 3
            cy += h + 12
    return _tree_h(ctx, b, width)


# ---- pipeline : dated multi-reading process pipeline ------------------------
def _pipe_geom(ctx, b, width):
    per = b.get("per_row", 4)
    gap = 46
    return per, gap, (width - gap * (per - 1)) / per


def _pipe_cell_h(ctx, s, cw):
    h = line_h(ctx.f.smallb) + 14
    h += 10 + len(wrap_runs([(s["t"], ctx.f.chain, WHITE)], cw - 30, "pipe")) * (line_h(ctx.f.chain) + 4)
    h += len(wrap_runs(parse_runs(s["s"], ctx.f.chain_sub, ctx.f.smallb, DIM, WHITE),
                       cw - 30, "pipe")) * (line_h(ctx.f.chain_sub) + 3)
    return h + 12


def _pipe_h(ctx, b, width):
    per, gap, cw = _pipe_geom(ctx, b, width)
    rows = [b["stages"][i:i + per] for i in range(0, len(b["stages"]), per)]
    nr = len(rows)
    total = sum(max(_pipe_cell_h(ctx, s, cw) for s in r) for r in rows) + 26 * nr
    if nr > 1:
        total += 14 * (nr - 2)
    return total


def _pipe_draw(ctx, d, b, x, y, width):
    per, gap, cw = _pipe_geom(ctx, b, width)
    rows = [b["stages"][i:i + per] for i in range(0, len(b["stages"]), per)]
    cy = y
    for r_i, r in enumerate(rows):
        rh = max(_pipe_cell_h(ctx, s, cw) for s in r)
        for i, s in enumerate(r):
            c = col(s.get("c", "cyan"))
            cx = x + i * (cw + gap)
            rrect(d, [cx, cy, cx + cw, cy + rh], radius=14, fill=CARD_TITLE, outline=c, width=3)
            rb = line_h(ctx.f.smallb) + 14
            rrect(d, [cx, cy, cx + cw, cy + rb], radius=14, fill=c)
            d.rectangle([cx, cy + rb - 14, cx + cw, cy + rb], fill=c)
            d.text((cx + 15, cy + 6), s["d"], font=ctx.f.smallb, fill=BG)
            ty = cy + rb + 10
            for ln in wrap_runs([(s["t"], ctx.f.chain, c)], cw - 30, "pipe"):
                draw_runs_line(d, cx + 15, ty, ln)
                ty += line_h(ctx.f.chain) + 4
            for ln in wrap_runs(parse_runs(s["s"], ctx.f.chain_sub, ctx.f.smallb, DIM, WHITE),
                                cw - 30, "pipe"):
                draw_runs_line(d, cx + 15, ty, ln)
                ty += line_h(ctx.f.chain_sub) + 3
            if i < len(r) - 1:
                arrow_right(d, cx + cw + 8, cy + rh / 2, cx + cw + gap - 8, CYAN, thick=5, head=16)
        # progress rail beneath the row
        ry = cy + rh + 13
        d.line([(x, ry), (x + width, ry)], fill=RULE, width=3)
        for i in range(len(r)):
            tx = x + i * (cw + gap) + cw / 2
            d.ellipse([tx - 6, ry - 6, tx + 6, ry + 6], fill=col(r[i].get("c", "cyan")))
        if r_i < len(rows) - 1:
            arrow_down(d, x + 26, ry + 4, ry + 24, CYAN, thick=4, head=12)
        cy += rh + 26 + (14 if r_i < len(rows) - 1 else 0)
    return cy - (14 if len(rows) > 1 else 0) - y


# ---- adapt : source -> device -> Indian adaptation map ----------------------
def _adapt_geom(ctx, b, width):
    a = 30
    sw = width * 0.20
    rest = width - sw - a * 2
    return a, sw, rest * 0.40, rest * 0.60


def _adapt_row_h(ctx, r, dw, iw):
    hd = len(wrap_runs(parse_runs(r["dev"], ctx.f.small, ctx.f.smallb, WHITE, WHITE), dw - 30, "adapt"))
    hi = len(wrap_runs(parse_runs(r["ind"], ctx.f.small, ctx.f.smallb, WHITE, WHITE), iw - 30, "adapt"))
    return max(hd, hi) * (line_h(ctx.f.small) + 4) + 22


def _adapt_h(ctx, b, width):
    a, sw, dw, iw = _adapt_geom(ctx, b, width)
    head = line_h(ctx.f.smallb) + 16
    return head + sum(_adapt_row_h(ctx, r, dw, iw) for r in b["rows"]) + 14 * len(b["rows"])


def _adapt_draw(ctx, d, b, x, y, width):
    a, sw, dw, iw = _adapt_geom(ctx, b, width)
    head = line_h(ctx.f.smallb) + 16
    d.text((x + 6, y + 6), b.get("h1", "SOURCE FAMILY"), font=ctx.f.smallb, fill=AMBER)
    d.text((x + sw + a + 6, y + 6), b.get("h2", "OFTEN-ASSOCIATED FEATURE"), font=ctx.f.smallb, fill=CYAN)
    d.text((x + sw + a + dw + a + 6, y + 6), b.get("h3", "INDIAN ADAPTATION"), font=ctx.f.smallb, fill=TEAL)
    cy = y + head
    for r in b["rows"]:
        c = col(r.get("c", "cyan"))
        h = _adapt_row_h(ctx, r, dw, iw)
        rrect(d, [x, cy, x + sw, cy + h], radius=12, fill=c)
        for ln in wrap_runs([(r["src"], ctx.f.smallb, BG)], sw - 26, "adapt"):
            draw_runs_line(d, x + 14, cy + 9, ln)
        arrow_right(d, x + sw + 6, cy + h / 2, x + sw + a - 4, c, thick=4, head=12)
        bx = x + sw + a
        rrect(d, [bx, cy, bx + dw, cy + h], radius=12, fill=CARD_TITLE, outline=c, width=2)
        ty = cy + 9
        for ln in wrap_runs(parse_runs(r["dev"], ctx.f.small, ctx.f.smallb, WHITE, WHITE), dw - 30, "adapt"):
            draw_runs_line(d, bx + 15, ty, ln)
            ty += line_h(ctx.f.small) + 4
        arrow_right(d, bx + dw + 6, cy + h / 2, bx + dw + a - 4, TEAL, thick=4, head=12)
        ix = bx + dw + a
        rrect(d, [ix, cy, ix + iw, cy + h], radius=12, fill=CARD, outline=TEAL, width=2)
        ty = cy + 9
        for ln in wrap_runs(parse_runs(r["ind"], ctx.f.small, ctx.f.smallb, WHITE, WHITE), iw - 30, "adapt"):
            draw_runs_line(d, ix + 15, ty, ln)
            ty += line_h(ctx.f.small) + 4
        cy += h + 14
    return cy - y


R.BLOCKS.update({
    "dash": (_dash_h, _dash_draw),
    "alloc": (_alloc_h, _alloc_draw),
    "funnel": (_funnel_h, _funnel_draw),
    "hub": (_hub_h, _hub_draw),
    "tree": (_tree_h, _tree_draw),
    "pipeline": (_pipe_h, _pipe_draw),
    "adapt": (_adapt_h, _adapt_draw),
})

NEW_BLOCKS = ["dash", "alloc", "funnel", "hub", "tree", "pipeline", "adapt"]
