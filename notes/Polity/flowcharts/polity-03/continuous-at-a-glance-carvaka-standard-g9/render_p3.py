"""Polity 03 bespoke visual grammars — part 1 of 2.

These primitives exist only for Salient Features of the Indian Constitution.
None of them is used by the Polity 01 g9 or Polity 02 g8 packages.

Part 1: wheel · fan · srcmap · spectrum · quadrant · loop · balance · overlap · triangle
"""
from __future__ import annotations

import math

import render_lib as R
from render_lib import (
    BG, CARD_TITLE, RULE, WHITE, DIM, YELLOW, MAGENTA,
    col, line_h, text_w, rrect, wrap_runs, parse_runs, draw_runs_line,
    arrow_right, arrow_down,
)


def _rich(ctx, s, font, boldf, colour, bold_colour, w, tag):
    return wrap_runs(parse_runs(s, font, boldf, colour, bold_colour), w, tag)


def _kv_item_runs(ctx, it, f):
    """Extension of the engine's bullet builder: rich-parse the `v` field of
    keyed bullets so that **bold** inside WRONG:/CORRECT: lines is honoured."""
    fb = ctx.f.bodyb if f is ctx.f.body else ctx.f.smallb
    if isinstance(it, dict):
        runs = [(it["k"], fb, col(it.get("kc", "white")))]
        if it.get("v"):
            base = DIM if it.get("dim") else WHITE
            runs.extend(parse_runs(" " + it["v"], f, fb, base, WHITE))
        return runs
    return parse_runs(it, f, fb, WHITE, WHITE)


R._item_runs = _kv_item_runs


def _blk(ctx, d, x, y, w, title, sub, c, tag, pad=15, radius=13, fill=CARD_TITLE, bw=3):
    """Draw a titled mini-card and return its height."""
    tl = wrap_runs([(title, ctx.f.chain, c)], w - 2 * pad - 4, tag) if title else []
    sl = _rich(ctx, sub, ctx.f.small, ctx.f.smallb, DIM, WHITE, w - 2 * pad - 4, tag) if sub else []
    h = pad + len(tl) * (line_h(ctx.f.chain) + 4) + len(sl) * (line_h(ctx.f.small) + 4) + pad
    if d is not None:
        rrect(d, [x, y, x + w, y + h], radius=radius, fill=fill, outline=c, width=bw)
        ty = y + pad - 2
        for ln in tl:
            draw_runs_line(d, x + pad, ty, ln)
            ty += line_h(ctx.f.chain) + 4
        for ln in sl:
            draw_runs_line(d, x + pad, ty, ln)
            ty += line_h(ctx.f.small) + 4
    return h


def _blk_h(ctx, w, title, sub, pad=15):
    tl = wrap_runs([(title, ctx.f.chain, WHITE)], w - 2 * pad - 4, "m") if title else []
    sl = _rich(ctx, sub, ctx.f.small, ctx.f.smallb, DIM, WHITE, w - 2 * pad - 4, "m") if sub else []
    return pad + len(tl) * (line_h(ctx.f.chain) + 4) + len(sl) * (line_h(ctx.f.small) + 4) + pad


# ================================================================== wheel ====
def _wheel_geom(ctx, b, width):
    hubw = width * b.get("hub_w", 0.30)
    gap = 54
    nw = (width - hubw - 2 * gap) / 2
    nh = max(_blk_h(ctx, nw, n["t"], n.get("s", "")) for n in b["nodes"])
    vgap = 52
    hub_t = wrap_runs([(b["centre"]["t"], ctx.f.head, WHITE)], hubw * 0.74, "wheel")
    hub_s = _rich(ctx, b["centre"].get("s", ""), ctx.f.small, ctx.f.smallb, WHITE, YELLOW,
                  hubw * 0.74, "wheel")
    hub_h = len(hub_t) * (line_h(ctx.f.head) + 4) + len(hub_s) * (line_h(ctx.f.small) + 4) + 34
    total = max(2 * nh + vgap, hub_h / 0.60)
    return hubw, gap, nw, nh, vgap, total, hub_t, hub_s


def _wheel_h(ctx, b, width):
    return _wheel_geom(ctx, b, width)[5]


def _wheel_draw(ctx, d, b, x, y, width):
    hubw, gap, nw, nh, vgap, total, hub_t, hub_s = _wheel_geom(ctx, b, width)
    cx, cy = x + width / 2, y + total / 2
    rx, ry = hubw / 2, total / 2 - 4
    cc = col(b["centre"].get("c", "yellow"))
    cols_x = [x, x + nw + hubw + 2 * gap]
    rows_y = [y + (total - (2 * nh + vgap)) / 2]
    rows_y.append(rows_y[0] + nh + vgap)
    for i, n in enumerate(b["nodes"][:4]):
        bx = cols_x[i % 2]
        by = rows_y[i // 2]
        px = bx + nw if i % 2 == 0 else bx
        py = by + nh / 2
        dx, dy = cx - px, cy - py
        t = 1.0 / math.sqrt((dx / rx) ** 2 + (dy / ry) ** 2)
        d.line([(px, py), (cx - t * dx, cy - t * dy)], fill=col(n.get("c", "cyan")), width=4)
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=col(n.get("c", "cyan")))
        _blk(ctx, d, bx, by + (nh - _blk_h(ctx, nw, n["t"], n.get("s", ""))) / 2, nw,
             n["t"], n.get("s", ""), col(n.get("c", "cyan")), "wheel")
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=(18, 44, 64), outline=cc, width=6)
    hy = cy - (len(hub_t) * (line_h(ctx.f.head) + 4) + len(hub_s) * (line_h(ctx.f.small) + 4)) / 2
    for ln in hub_t:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, cx - lw / 2, hy, ln)
        hy += line_h(ctx.f.head) + 4
    for ln in hub_s:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, cx - lw / 2, hy, ln)
        hy += line_h(ctx.f.small) + 4
    return total


# ==================================================================== fan ====
def _fan_geom(ctx, b, width):
    nc, ne = len(b["causes"]), len(b["effects"])
    g = 26
    cw = (width - g * (nc - 1)) / nc
    ew = (width - g * (ne - 1)) / ne
    ch = max(_blk_h(ctx, cw, c["t"], c.get("s", ""), pad=13) for c in b["causes"])
    eh = max(_blk_h(ctx, ew, e["t"], e.get("s", ""), pad=13) for e in b["effects"])
    corew = width * 0.72
    coreh = _blk_h(ctx, corew, b["core"]["t"], b["core"].get("s", ""), pad=19)
    link = 58
    return cw, ew, ch, eh, corew, coreh, link, g


def _fan_h(ctx, b, width):
    cw, ew, ch, eh, corew, coreh, link, g = _fan_geom(ctx, b, width)
    return ch + link + coreh + link + eh


def _fan_draw(ctx, d, b, x, y, width):
    cw, ew, ch, eh, corew, coreh, link, g = _fan_geom(ctx, b, width)
    corex = x + (width - corew) / 2
    cy0 = y + ch
    for i, c in enumerate(b["causes"]):
        bx = x + i * (cw + g)
        _blk(ctx, d, bx, y, cw, c["t"], c.get("s", ""), col(c.get("c", "amber")), "fan", pad=13)
        d.line([(bx + cw / 2, cy0 + 4), (corex + corew / 2, cy0 + link - 12)],
               fill=col(c.get("c", "amber")), width=3)
    arrow_down(d, corex + corew / 2, cy0 + link - 24, cy0 + link, YELLOW, thick=6, head=18)
    _blk(ctx, d, corex, cy0 + link, corew, b["core"]["t"], b["core"].get("s", ""),
         col(b["core"].get("c", "yellow")), "fan", pad=19, radius=16, fill=(24, 46, 62), bw=5)
    ey = cy0 + link + coreh + link
    for i, e in enumerate(b["effects"]):
        bx = x + i * (ew + g)
        d.line([(corex + corew / 2, ey - link + 12), (bx + ew / 2, ey - 16)],
               fill=col(e.get("c", "teal")), width=3)
        arrow_down(d, bx + ew / 2, ey - 20, ey, col(e.get("c", "teal")), thick=4, head=14)
        _blk(ctx, d, bx, ey, ew, e["t"], e.get("s", ""), col(e.get("c", "teal")), "fan", pad=13)
    return _fan_h(ctx, b, width)


# ================================================================= srcmap ====
def _srcmap_geom(ctx, b, width):
    sw = width * 0.18
    g = 22
    rest = width - sw - 2 * g
    aw = rest * 0.52
    rw = rest - aw
    return sw, aw, rw, g


def _srcmap_rowh(ctx, b, r, aw, rw):
    a = _rich(ctx, r["adopt"], ctx.f.small, ctx.f.smallb, WHITE, WHITE, aw - 32, "srcmap")
    j = _rich(ctx, r["reject"], ctx.f.small, ctx.f.smallb, DIM, WHITE, rw - 32, "srcmap")
    return max(len(a), len(j)) * (line_h(ctx.f.small) + 5) + 26


def _srcmap_h(ctx, b, width):
    sw, aw, rw, g = _srcmap_geom(ctx, b, width)
    h = line_h(ctx.f.smallb) + 16
    for r in b["rows"]:
        h += _srcmap_rowh(ctx, b, r, aw, rw) + 12
    return h - 12


def _srcmap_draw(ctx, d, b, x, y, width):
    sw, aw, rw, g = _srcmap_geom(ctx, b, width)
    hh = line_h(ctx.f.smallb) + 16
    d.text((x + 6, y + 4), b.get("h_src", "SOURCE"), font=ctx.f.smallb, fill=R.CYAN)
    d.text((x + sw + g + 6, y + 4), b["h_adopt"], font=ctx.f.smallb, fill=R.GREEN)
    d.text((x + sw + aw + 2 * g + 6, y + 4), b["h_reject"], font=ctx.f.smallb, fill=R.RED)
    cy = y + hh
    for r in b["rows"]:
        rh = _srcmap_rowh(ctx, b, r, aw, rw)
        c = col(r.get("c", "cyan"))
        rrect(d, [x, cy, x + sw, cy + rh], radius=11, fill=c)
        sl = wrap_runs([(r["src"], ctx.f.smallb, BG)], sw - 26, "srcmap")
        ty = cy + (rh - len(sl) * (line_h(ctx.f.smallb) + 4)) / 2
        for ln in sl:
            draw_runs_line(d, x + 13, ty, ln)
            ty += line_h(ctx.f.smallb) + 4
        ax = x + sw + g
        rrect(d, [ax, cy, ax + aw, cy + rh], radius=11, fill=(13, 38, 48), outline=R.GREEN, width=2)
        ty = cy + 12
        for ln in _rich(ctx, r["adopt"], ctx.f.small, ctx.f.smallb, WHITE, R.GREEN, aw - 32, "srcmap"):
            draw_runs_line(d, ax + 16, ty, ln)
            ty += line_h(ctx.f.small) + 5
        jx = ax + aw + g
        rrect(d, [jx, cy, jx + rw, cy + rh], radius=11, fill=(38, 22, 26), outline=R.RED, width=2)
        ty = cy + 12
        for ln in _rich(ctx, r["reject"], ctx.f.small, ctx.f.smallb, DIM, R.RED, rw - 32, "srcmap"):
            draw_runs_line(d, jx + 16, ty, ln)
            ty += line_h(ctx.f.small) + 5
        cy += rh + 12
    return _srcmap_h(ctx, b, width)


# =============================================================== spectrum ====
def _spec_geom(ctx, b, width):
    n = len(b["stops"])
    g = 22
    cw = (width - g * (n - 1)) / n
    ch = max(_blk_h(ctx, cw, s["t"], s.get("s", ""), pad=13) for s in b["stops"])
    endh = line_h(ctx.f.smallb) + 10
    ceil_lines = wrap_runs([(b["ceiling"], ctx.f.smallb, MAGENTA)], width - 60, "spec")
    ceilh = len(ceil_lines) * (line_h(ctx.f.smallb) + 4) + 20
    return n, g, cw, ch, endh, ceilh, ceil_lines


def _spec_h(ctx, b, width):
    n, g, cw, ch, endh, ceilh, cl = _spec_geom(ctx, b, width)
    return ceilh + 20 + endh + 40 + ch


def _spec_draw(ctx, d, b, x, y, width):
    n, g, cw, ch, endh, ceilh, cl = _spec_geom(ctx, b, width)
    rrect(d, [x, y, x + width, y + ceilh], radius=10, fill=(40, 33, 52), outline=MAGENTA, width=3)
    ty = y + 10
    for ln in cl:
        draw_runs_line(d, x + 22, ty, ln)
        ty += line_h(ctx.f.smallb) + 4
    ey = y + ceilh + 20
    d.text((x, ey), b["left"], font=ctx.f.smallb, fill=R.GREEN)
    rwid = text_w(ctx.f.smallb, b["right"])
    d.text((x + width - rwid, ey), b["right"], font=ctx.f.smallb, fill=R.RED)
    ay = ey + endh + 16
    steps = 220
    for i in range(steps):
        t = i / (steps - 1)
        cc = tuple(int(R.GREEN[k] + (R.RED[k] - R.GREEN[k]) * t) for k in range(3))
        d.line([(x + width * i / steps, ay), (x + width * (i + 1) / steps, ay)], fill=cc, width=8)
    cy = ay + 24
    for i, s in enumerate(b["stops"]):
        bx = x + i * (cw + g)
        c = col(s.get("c", "cyan"))
        mid = bx + cw / 2
        d.ellipse([mid - 13, ay - 13, mid + 13, ay + 13], fill=BG, outline=c, width=5)
        d.line([(mid, ay + 13), (mid, cy)], fill=c, width=3)
        _blk(ctx, d, bx, cy, cw, s["t"], s.get("s", ""), c, "spec", pad=13)
    return _spec_h(ctx, b, width)


# =============================================================== quadrant ====
def _quad_geom(ctx, b, width):
    g = 78
    cw = (width - g) / 2
    hs = [_blk_h(ctx, cw, c["t"], c.get("s", ""), pad=17) for c in b["cells"]]
    rh = max(max(hs[0], hs[1]), max(hs[2], hs[3]))
    return g, cw, rh


def _quad_h(ctx, b, width):
    g, cw, rh = _quad_geom(ctx, b, width)
    return 2 * rh + g


def _quad_draw(ctx, d, b, x, y, width):
    g, cw, rh = _quad_geom(ctx, b, width)
    for i, c in enumerate(b["cells"]):
        bx = x + (i % 2) * (cw + g)
        by = y + (i // 2) * (rh + g)
        cc = col(c.get("c", "cyan"))
        rrect(d, [bx, by, bx + cw, by + rh], radius=16, fill=CARD_TITLE, outline=cc, width=3)
        tl = wrap_runs([(c["t"], ctx.f.head, cc)], cw - 40, "quad")
        sl = _rich(ctx, c.get("s", ""), ctx.f.small, ctx.f.smallb, WHITE, cc, cw - 40, "quad")
        ty = by + 17
        for ln in tl:
            draw_runs_line(d, bx + 20, ty, ln)
            ty += line_h(ctx.f.head) + 4
        for ln in sl:
            draw_runs_line(d, bx + 20, ty, ln)
            ty += line_h(ctx.f.small) + 4
    mx, my = x + width / 2, y + rh + g / 2
    lab = b.get("core", "")
    lw = text_w(ctx.f.smallb, lab) + 46
    lh = line_h(ctx.f.smallb) + 14
    d.polygon([(mx - lw / 2 - 16, my), (mx, my - lh / 2 - 12), (mx + lw / 2 + 16, my),
               (mx, my + lh / 2 + 12)], fill=YELLOW)
    d.text((mx - text_w(ctx.f.smallb, lab) / 2, my - line_h(ctx.f.smallb) / 2), lab,
           font=ctx.f.smallb, fill=BG)
    return _quad_h(ctx, b, width)


# =================================================================== loop ====
def _loop_geom(ctx, b, width):
    g = 96
    nw = (width - g) / 2
    nh = max(_blk_h(ctx, nw, n["t"], n.get("s", ""), pad=15) for n in b["nodes"][:4])
    lane = 96
    cw = width - 2 * lane - 60
    ct = wrap_runs([(b["centre"]["t"], ctx.f.head, YELLOW)], cw - 44, "loop")
    ci = []
    for it in b["centre"]["items"]:
        ci.append(_rich(ctx, it, ctx.f.small, ctx.f.smallb, WHITE, YELLOW, cw - 60, "loop"))
    ch = 20 + len(ct) * (line_h(ctx.f.head) + 4) + sum(len(l) for l in ci) * (line_h(ctx.f.small) + 4) \
        + 8 * len(ci) + 20
    mid = max(ch + 34, 150)
    return g, nw, nh, lane, cw, ct, ci, ch, mid


def _loop_h(ctx, b, width):
    g, nw, nh, lane, cw, ct, ci, ch, mid = _loop_geom(ctx, b, width)
    return 2 * nh + mid


def _loop_draw(ctx, d, b, x, y, width):
    g, nw, nh, lane, cw, ct, ci, ch, mid = _loop_geom(ctx, b, width)
    pos = [(x, y), (x + nw + g, y), (x, y + nh + mid), (x + nw + g, y + nh + mid)]
    order = [0, 1, 3, 2]
    for k, i in enumerate(order):
        n = b["nodes"][k]
        bx, by = pos[i]
        _blk(ctx, d, bx, by, nw, n["t"], n.get("s", ""), col(n.get("c", "cyan")), "loop", pad=15,
             radius=16, bw=4)
    arrow_right(d, x + nw + 10, y + nh / 2, x + nw + g - 10, R.CYAN, thick=6, head=20)
    ry = y + nh + mid / 2
    d.line([(x + width - lane / 2, y + nh + 8), (x + width - lane / 2, y + nh + mid - 8)],
           fill=R.CYAN, width=6)
    arrow_down(d, x + width - lane / 2, y + nh + mid - 40, y + nh + mid - 6, R.CYAN, thick=6, head=20)
    d.line([(x + lane / 2, y + nh + 8), (x + lane / 2, y + nh + mid - 8)], fill=R.TEAL, width=6)
    d.polygon([(x + lane / 2, y + nh + 6), (x + lane / 2 - 12, y + nh + 32),
               (x + lane / 2 + 12, y + nh + 32)], fill=R.TEAL)
    by2 = y + nh + mid + nh / 2
    d.line([(x + nw + g - 10, by2), (x + nw + 10, by2)], fill=R.TEAL, width=6)
    d.polygon([(x + nw + 6, by2), (x + nw + 32, by2 - 12), (x + nw + 32, by2 + 12)], fill=R.TEAL)
    bx = x + lane + 30
    byc = y + nh + (mid - ch) / 2
    rrect(d, [bx, byc, bx + cw, byc + ch], radius=14, fill=(36, 33, 20), outline=YELLOW, width=3)
    ty = byc + 14
    for ln in ct:
        draw_runs_line(d, bx + 22, ty, ln)
        ty += line_h(ctx.f.head) + 4
    for k, lines in enumerate(ci):
        _by = ty + (line_h(ctx.f.small) + 4) * 0.42
        d.ellipse([bx + 24, _by - 5, bx + 34, _by + 5], fill=YELLOW)
        for ln in lines:
            draw_runs_line(d, bx + 48, ty, ln)
            ty += line_h(ctx.f.small) + 4
        ty += 8
    return _loop_h(ctx, b, width)


# ================================================================ balance ====
def _bal_geom(ctx, b, width):
    fw = width * 0.24
    g = 30
    pw = (width - fw - 2 * g) / 2
    ph = 0
    for side in (b["left"], b["right"]):
        h = 16 + line_h(ctx.f.head) + 12
        h += R._bullet_items_h(ctx, side["items"], pw - 44, font=ctx.f.small, tag=side["h"])
        ph = max(ph, h + 18)
    ft = wrap_runs([(b["fulcrum"]["t"], ctx.f.head, BG)], fw - 40, "bal")
    fs = _rich(ctx, b["fulcrum"].get("s", ""), ctx.f.small, ctx.f.smallb, WHITE, YELLOW, fw - 20, "bal")
    fh = len(ft) * (line_h(ctx.f.head) + 4) + 20
    tot = max(ph, 50 + fh + 78 + len(fs) * (line_h(ctx.f.small) + 4) + 12)
    return fw, g, pw, ph, ft, fs, fh, tot


def _bal_h(ctx, b, width):
    return _bal_geom(ctx, b, width)[7]


def _bal_draw(ctx, d, b, x, y, width):
    fw, g, pw, ph, ft, fs, fh, tot = _bal_geom(ctx, b, width)
    for side, sx in ((b["left"], x), (b["right"], x + pw + fw + 2 * g)):
        c = col(side.get("c", "cyan"))
        rrect(d, [sx, y, sx + pw, y + tot], radius=16, fill=CARD_TITLE, outline=c, width=3)
        hb = line_h(ctx.f.head) + 14
        rrect(d, [sx, y, sx + pw, y + hb], radius=16, fill=c)
        d.rectangle([sx, y + hb - 16, sx + pw, y + hb], fill=c)
        d.text((sx + 20, y + 6), side["h"], font=ctx.f.head, fill=BG)
        R._draw_bullets(ctx, d, sx + 22, y + hb + 14, pw - 44, side["items"], c,
                        font=ctx.f.small, tag=side["h"])
    mx = x + pw + g + fw / 2
    beam_y = y + 40
    d.line([(x + pw + 4, beam_y), (x + pw + 2 * g + fw - 4, beam_y)], fill=YELLOW, width=7)
    px0, px1 = mx - fw / 2, mx + fw / 2
    pl_y = beam_y + 10
    rrect(d, [px0, pl_y, px1, pl_y + fh], radius=14, fill=YELLOW)
    ty = pl_y + 10
    for ln in ft:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, mx - lw / 2, ty, ln)
        ty += line_h(ctx.f.head) + 4
    piv = pl_y + fh
    d.polygon([(mx, piv + 60), (mx - 54, piv + 4), (mx + 54, piv + 4)], fill=YELLOW)
    ty = piv + 74
    for ln in fs:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, mx - lw / 2, ty, ln)
        ty += line_h(ctx.f.small) + 4
    return tot


# ================================================================ overlap ====
def _ov_geom(ctx, b, width):
    n = len(b["organs"])
    g = 40
    ow = (width - g * (n - 1)) / n
    oh = 0
    for o in b["organs"]:
        h = 16 + line_h(ctx.f.head) + 12
        h += R._bullet_items_h(ctx, o["items"], ow - 44, font=ctx.f.small, tag=o["h"])
        oh = max(oh, h + 18)
    nz = len(b["zones"])
    zg = 20
    zw = (width - 44 - zg * (nz - 1)) / nz
    zh = max(_blk_h(ctx, zw, z["t"], z.get("s", ""), pad=12) for z in b["zones"])
    bandh = zh + line_h(ctx.f.smallb) + 40
    return g, ow, oh, zg, zw, zh, bandh


def _ov_h(ctx, b, width):
    g, ow, oh, zg, zw, zh, bandh = _ov_geom(ctx, b, width)
    return oh + 44 + bandh


def _ov_draw(ctx, d, b, x, y, width):
    g, ow, oh, zg, zw, zh, bandh = _ov_geom(ctx, b, width)
    for i, o in enumerate(b["organs"]):
        ox = x + i * (ow + g)
        c = col(o.get("c", "cyan"))
        rrect(d, [ox, y, ox + ow, y + oh], radius=16, fill=CARD_TITLE, outline=c, width=3)
        hb = line_h(ctx.f.head) + 14
        rrect(d, [ox, y, ox + ow, y + hb], radius=16, fill=c)
        d.rectangle([ox, y + hb - 16, ox + ow, y + hb], fill=c)
        d.text((ox + 20, y + 6), o["h"], font=ctx.f.head, fill=BG)
        R._draw_bullets(ctx, d, ox + 22, y + hb + 14, ow - 44, o["items"], c,
                        font=ctx.f.small, tag=o["h"])
        if i:
            lx = ox - g / 2
            arrow_right(d, lx - 18, y + oh + 22, lx - 2, YELLOW, thick=5, head=14)
            d.line([(lx - 2, y + oh + 22), (lx + 2, y + oh + 22)], fill=YELLOW, width=5)
            d.polygon([(lx + 18, y + oh + 22), (lx + 2, y + oh + 13), (lx + 2, y + oh + 31)],
                      fill=YELLOW)
    by = y + oh + 44
    rrect(d, [x, by, x + width, by + bandh], radius=14, fill=(30, 30, 20), outline=YELLOW, width=3)
    d.text((x + 22, by + 12), b.get("zone_h", "CONSTITUTIONAL OVERLAP ZONES — LEGITIMATE ONLY WITH RECIPROCAL CHECKS"),
           font=ctx.f.smallb, fill=YELLOW)
    zy = by + line_h(ctx.f.smallb) + 26
    for i, z in enumerate(b["zones"]):
        zx = x + 22 + i * (zw + zg)
        _blk(ctx, d, zx, zy, zw, z["t"], z.get("s", ""), col(z.get("c", "amber")), "zone",
             pad=12, radius=10, fill=(20, 44, 60), bw=2)
    return _ov_h(ctx, b, width)


# =============================================================== triangle ====
def _tri_geom(ctx, b, width):
    aw = width * 0.66
    ah = _blk_h(ctx, aw, b["apex"]["t"], b["apex"].get("s", ""), pad=19)
    n = len(b["base"])
    g = 30
    bw = (width - g * (n - 1)) / n
    bh = max(_blk_h(ctx, bw, s["t"], s.get("s", ""), pad=15) for s in b["base"])
    link = 70
    return aw, ah, n, g, bw, bh, link


def _tri_h(ctx, b, width):
    aw, ah, n, g, bw, bh, link = _tri_geom(ctx, b, width)
    return ah + link + bh


def _tri_draw(ctx, d, b, x, y, width):
    aw, ah, n, g, bw, bh, link = _tri_geom(ctx, b, width)
    ax = x + (width - aw) / 2
    _blk(ctx, d, ax, y, aw, b["apex"]["t"], b["apex"].get("s", ""),
         col(b["apex"].get("c", "yellow")), "tri", pad=19, radius=18, fill=(30, 46, 40), bw=5)
    by = y + ah + link
    for i, s in enumerate(b["base"]):
        bx = x + i * (bw + g)
        c = col(s.get("c", "cyan"))
        d.line([(x + width / 2, y + ah + 6), (bx + bw / 2, by - 18)], fill=c, width=4)
        arrow_down(d, bx + bw / 2, by - 24, by, c, thick=4, head=14)
        _blk(ctx, d, bx, by, bw, s["t"], s.get("s", ""), c, "tri", pad=15)
    return _tri_h(ctx, b, width)


R.BLOCKS.update({
    "wheel": (_wheel_h, _wheel_draw),
    "fan": (_fan_h, _fan_draw),
    "srcmap": (_srcmap_h, _srcmap_draw),
    "spectrum": (_spec_h, _spec_draw),
    "quadrant": (_quad_h, _quad_draw),
    "loop": (_loop_h, _loop_draw),
    "balance": (_bal_h, _bal_draw),
    "overlap": (_ov_h, _ov_draw),
    "triangle": (_tri_h, _tri_draw),
})
