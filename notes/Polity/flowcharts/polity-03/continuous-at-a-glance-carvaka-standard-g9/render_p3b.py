"""Polity 03 bespoke visual grammars — part 2 of 2.

Part 2: pyramid · triad · vs3 · bus · constel · switch · tension · web
"""
from __future__ import annotations

import render_lib as R
from render_lib import (
    BG, CARD_TITLE, RULE, WHITE, DIM, YELLOW, MAGENTA, GREEN, RED, CYAN, TEAL,
    col, line_h, text_w, rrect, wrap_runs, parse_runs, draw_runs_line,
    arrow_right, arrow_down,
)
from render_p3 import _rich, _blk, _blk_h


# ================================================================ pyramid ====
def _pyr_geom(ctx, b, width):
    railw = width * 0.34
    g = 44
    tw = width - railw - g
    n = len(b["tiers"])
    widths = [tw * (1.0 - 0.20 * (n - 1 - i)) for i in range(n)]
    hs = [_blk_h(ctx, widths[i], t["t"], t.get("s", ""), pad=15) for i, t in enumerate(b["tiers"])]
    step = 30
    th = sum(hs) + step * (n - 1)
    rh = 18 + line_h(ctx.f.head) + 12
    rh += R._bullet_items_h(ctx, b["rail"]["items"], railw - 44, font=ctx.f.small, tag="rail")
    rh += 18
    return railw, g, tw, widths, hs, step, max(th, rh)


def _pyr_h(ctx, b, width):
    return _pyr_geom(ctx, b, width)[6]


def _pyr_draw(ctx, d, b, x, y, width):
    railw, g, tw, widths, hs, step, tot = _pyr_geom(ctx, b, width)
    cy = y
    for i, t in enumerate(b["tiers"]):
        bx = x + (tw - widths[i]) / 2
        c = col(t.get("c", "cyan"))
        _blk(ctx, d, bx, cy, widths[i], t["t"], t.get("s", ""), c, "pyr", pad=15, radius=14, bw=4)
        if i < len(b["tiers"]) - 1:
            arrow_down(d, x + tw / 2, cy + hs[i] + 4, cy + hs[i] + step - 2, c, thick=5, head=16)
        cy += hs[i] + step
    rx = x + tw + g
    rc = col(b["rail"].get("c", "magenta"))
    rrect(d, [rx, y, rx + railw, y + tot], radius=16, fill=(34, 30, 48), outline=rc, width=3)
    hb = line_h(ctx.f.head) + 14
    rrect(d, [rx, y, rx + railw, y + hb], radius=16, fill=rc)
    d.rectangle([rx, y + hb - 16, rx + railw, y + hb], fill=rc)
    d.text((rx + 20, y + 6), b["rail"]["h"], font=ctx.f.head, fill=BG)
    R._draw_bullets(ctx, d, rx + 22, y + hb + 16, railw - 44, b["rail"]["items"], rc,
                    font=ctx.f.small, tag="rail")
    return tot


# ================================================================== triad ====
def _triad_colh(ctx, c, cw):
    h = 16 + line_h(ctx.f.head) + 10
    h += line_h(ctx.f.smallb) + 22
    h += R._bullet_items_h(ctx, c["items"], cw - 44, font=ctx.f.small, tag=c["h"])
    return h + 18


def _triad_geom(ctx, b, width):
    n = len(b["cols"])
    g = 30
    cw = (width - g * (n - 1)) / n
    ch = max(_triad_colh(ctx, c, cw) for c in b["cols"])
    fl = _rich(ctx, b["foot"]["text"], ctx.f.band, ctx.f.bandb, WHITE, YELLOW,
               width - text_w(ctx.f.bandb, b["foot"]["label"]) - 74, "triadfoot")
    fh = len(fl) * (line_h(ctx.f.band) + 5) + 24
    return g, cw, ch, fl, fh


def _triad_h(ctx, b, width):
    g, cw, ch, fl, fh = _triad_geom(ctx, b, width)
    return ch + 22 + fh


def _triad_draw(ctx, d, b, x, y, width):
    g, cw, ch, fl, fh = _triad_geom(ctx, b, width)
    for i, c in enumerate(b["cols"]):
        cx = x + i * (cw + g)
        cc = col(c.get("c", "cyan"))
        rrect(d, [cx, y, cx + cw, y + ch], radius=16, fill=CARD_TITLE, outline=cc, width=3)
        hb = line_h(ctx.f.head) + 12
        rrect(d, [cx, y, cx + cw, y + hb], radius=16, fill=cc)
        d.rectangle([cx, y + hb - 16, cx + cw, y + hb], fill=cc)
        d.text((cx + 18, y + 5), c["h"], font=ctx.f.head, fill=BG)
        sy = y + hb + 12
        sw = text_w(ctx.f.smallb, c["status"]) + 34
        sh = line_h(ctx.f.smallb) + 8
        rrect(d, [cx + 18, sy, cx + 18 + sw, sy + sh], radius=sh / 2, fill=None,
              outline=col(c.get("sc", "yellow")), width=3)
        d.text((cx + 35, sy + 3), c["status"], font=ctx.f.smallb, fill=col(c.get("sc", "yellow")))
        R._draw_bullets(ctx, d, cx + 20, sy + sh + 14, cw - 44, c["items"], cc,
                        font=ctx.f.small, tag=c["h"])
    fy = y + ch + 22
    rrect(d, [x, fy, x + width, fy + fh], radius=12, fill=(30, 40, 34), outline=GREEN, width=3)
    d.text((x + 22, fy + 11), b["foot"]["label"], font=ctx.f.bandb, fill=GREEN)
    off = text_w(ctx.f.bandb, b["foot"]["label"]) + 40
    ty = fy + 11
    for ln in fl:
        draw_runs_line(d, x + off, ty, ln)
        ty += line_h(ctx.f.band) + 5
    return _triad_h(ctx, b, width)


# ==================================================================== vs3 ====
def _vs3_geom(ctx, b, width):
    lw = width * b.get("labw", 0.19)
    cw = (width - lw) / 3
    hh = line_h(ctx.f.smallb) + 20
    rhs = []
    for r in b["rows"]:
        h = 0
        for k, cell in enumerate(r["v"]):
            n = len(_rich(ctx, cell, ctx.f.small, ctx.f.smallb, WHITE, WHITE, cw - 32, "vs3"))
            h = max(h, n * (line_h(ctx.f.small) + 5))
        n = len(wrap_runs([(r["l"], ctx.f.smallb, WHITE)], lw - 28, "vs3"))
        h = max(h, n * (line_h(ctx.f.smallb) + 5))
        rhs.append(h + 20)
    return lw, cw, hh, rhs


def _vs3_h(ctx, b, width):
    lw, cw, hh, rhs = _vs3_geom(ctx, b, width)
    return hh + sum(rhs)


def _vs3_draw(ctx, d, b, x, y, width):
    lw, cw, hh, rhs = _vs3_geom(ctx, b, width)
    tot = hh + sum(rhs)
    hx = x + lw + cw
    d.rectangle([hx, y, hx + cw, y + tot], fill=(20, 46, 40))
    for i, hd in enumerate(b["heads"]):
        cx = x + lw + i * cw
        c = col(hd.get("c", "dim"))
        d.rectangle([cx + 3, y, cx + cw - 3, y + hh], fill=c)
        tw = text_w(ctx.f.smallb, hd["t"])
        d.text((cx + (cw - tw) / 2, y + 9), hd["t"], font=ctx.f.smallb, fill=BG)
    cy = y + hh
    for j, r in enumerate(b["rows"]):
        rh = rhs[j]
        if j % 2 == 0:
            d.rectangle([x, cy, x + lw, cy + rh], fill=(13, 34, 52))
        ty = cy + 9
        for ln in wrap_runs([(r["l"], ctx.f.smallb, col(b.get("c", "cyan")))], lw - 28, "vs3"):
            draw_runs_line(d, x + 12, ty, ln)
            ty += line_h(ctx.f.smallb) + 5
        for k, cell in enumerate(r["v"]):
            cx = x + lw + k * cw
            hi = (k == 1)
            ty = cy + 9
            for ln in _rich(ctx, cell, ctx.f.small, ctx.f.smallb,
                            WHITE if hi else DIM, TEAL if hi else YELLOW, cw - 32, "vs3"):
                draw_runs_line(d, cx + 16, ty, ln)
                ty += line_h(ctx.f.small) + 5
            d.line([(cx, cy), (cx, cy + rh)], fill=RULE, width=1)
        d.line([(x, cy + rh), (x + width, cy + rh)], fill=RULE, width=1)
        cy += rh
    d.rectangle([hx, y, hx + cw, y + tot], fill=None, outline=TEAL, width=4)
    return tot


# ==================================================================== bus ====
def _bus_geom(ctx, b, width):
    n = len(b["devices"])
    g = 26
    dw = (width - g * (n - 1)) / n
    dh = 0
    for dv in b["devices"]:
        h = 14
        h += len(wrap_runs([(dv["t"], ctx.f.chain, WHITE)], dw - 32, "bus")) * (line_h(ctx.f.chain) + 4)
        h += 10
        for key, lab in (("fn", b["l_fn"]), ("tension", b["l_ten"])):
            off = text_w(ctx.f.smallb, lab) + 12
            h += max(1, len(_rich(ctx, dv[key], ctx.f.small, ctx.f.smallb, WHITE, YELLOW,
                                  dw - 32 - off, "bus"))) * (line_h(ctx.f.small) + 4) + 8
        dh = max(dh, h + 12)
    labh = line_h(ctx.f.smallb) + 16
    return g, dw, dh, labh


def _bus_h(ctx, b, width):
    g, dw, dh, labh = _bus_geom(ctx, b, width)
    return labh + 34 + dh


def _bus_draw(ctx, d, b, x, y, width):
    g, dw, dh, labh = _bus_geom(ctx, b, width)
    lw = text_w(ctx.f.smallb, b["label"]) + 48
    rrect(d, [x, y, x + lw, y + labh], radius=labh / 2, fill=YELLOW)
    d.text((x + 24, y + 7), b["label"], font=ctx.f.smallb, fill=BG)
    by = y + labh / 2
    d.line([(x + lw + 12, by), (x + width, by)], fill=YELLOW, width=7)
    dy = y + labh + 34
    for i, dv in enumerate(b["devices"]):
        bx = x + i * (dw + g)
        c = col(dv.get("c", "cyan"))
        d.line([(bx + dw / 2, by + 4), (bx + dw / 2, dy - 14)], fill=c, width=4)
        arrow_down(d, bx + dw / 2, dy - 20, dy, c, thick=4, head=13)
        rrect(d, [bx, dy, bx + dw, dy + dh], radius=14, fill=CARD_TITLE, outline=c, width=3)
        ty = dy + 12
        for ln in wrap_runs([(dv["t"], ctx.f.chain, c)], dw - 32, "bus"):
            draw_runs_line(d, bx + 16, ty, ln)
            ty += line_h(ctx.f.chain) + 4
        ty += 10
        for key, lab, lc in (("fn", b["l_fn"], TEAL), ("tension", b["l_ten"], RED)):
            d.text((bx + 16, ty), lab, font=ctx.f.smallb, fill=lc)
            off = text_w(ctx.f.smallb, lab) + 12
            for ln in _rich(ctx, dv[key], ctx.f.small, ctx.f.smallb, WHITE, YELLOW,
                            dw - 32 - off, "bus"):
                draw_runs_line(d, bx + 16 + off, ty, ln)
                ty += line_h(ctx.f.small) + 4
            ty += 8
    return _bus_h(ctx, b, width)


# ================================================================ constel ====
def _con_card_h(ctx, b, bd, cw):
    h = 14
    h += len(wrap_runs([(bd["t"], ctx.f.chain, WHITE)], cw - 34, "con")) * (line_h(ctx.f.chain) + 4)
    h += line_h(ctx.f.smallb) + 12
    for key, lab in (("fn", b["l_fn"]), ("ind", b["l_ind"])):
        off = text_w(ctx.f.smallb, lab) + 12
        h += len(_rich(ctx, bd[key], ctx.f.small, ctx.f.smallb, WHITE, YELLOW,
                       cw - 34 - off, "con")) * (line_h(ctx.f.small) + 4) + 8
    return h + 12


def _con_geom(ctx, b, width):
    corew = width * 0.24
    g = 34
    cw = (width - corew - 2 * g) / 2
    ch = max(_con_card_h(ctx, b, bd, cw) for bd in b["bodies"])
    vgap = 34
    ct = wrap_runs([(b["core"]["t"], ctx.f.head, BG)], corew - 196, "con")
    cs = _rich(ctx, b["core"].get("s", ""), ctx.f.small, ctx.f.smallb, BG, BG, corew - 196, "con")
    return corew, g, cw, ch, vgap, ct, cs


def _con_h(ctx, b, width):
    corew, g, cw, ch, vgap, ct, cs = _con_geom(ctx, b, width)
    return 2 * ch + vgap


def _con_draw(ctx, d, b, x, y, width):
    corew, g, cw, ch, vgap, ct, cs = _con_geom(ctx, b, width)
    tot = 2 * ch + vgap
    mx, my = x + width / 2, y + tot / 2
    for i, bd in enumerate(b["bodies"][:4]):
        bx = x if i % 2 == 0 else x + cw + corew + 2 * g
        by = y + (i // 2) * (ch + vgap)
        c = col(bd.get("c", "cyan"))
        px = bx + cw if i % 2 == 0 else bx
        d.line([(px, by + ch / 2), (mx, my)], fill=c, width=3)
        rrect(d, [bx, by, bx + cw, by + ch], radius=14, fill=CARD_TITLE, outline=c, width=3)
        ty = by + 12
        for ln in wrap_runs([(bd["t"], ctx.f.chain, c)], cw - 34, "con"):
            draw_runs_line(d, bx + 17, ty, ln)
            ty += line_h(ctx.f.chain) + 4
        aw = text_w(ctx.f.smallb, bd["art"]) + 26
        ah = line_h(ctx.f.smallb) + 6
        rrect(d, [bx + 17, ty + 3, bx + 17 + aw, ty + 3 + ah], radius=ah / 2, fill=c)
        d.text((bx + 30, ty + 5), bd["art"], font=ctx.f.smallb, fill=BG)
        ty += line_h(ctx.f.smallb) + 12
        for key, lab, lc in (("fn", b["l_fn"], TEAL), ("ind", b["l_ind"], MAGENTA)):
            d.text((bx + 17, ty), lab, font=ctx.f.smallb, fill=lc)
            off = text_w(ctx.f.smallb, lab) + 12
            for ln in _rich(ctx, bd[key], ctx.f.small, ctx.f.smallb, WHITE, YELLOW,
                            cw - 34 - off, "con"):
                draw_runs_line(d, bx + 17 + off, ty, ln)
                ty += line_h(ctx.f.small) + 4
            ty += 8
    hw = corew / 2 + 10
    tblk = len(ct) * (line_h(ctx.f.head) + 4) + len(cs) * (line_h(ctx.f.small) + 4)
    hy = tblk / 2 + 26
    tp = 74
    d.polygon([(mx - hw, my), (mx - hw + tp, my - hy), (mx + hw - tp, my - hy),
               (mx + hw, my), (mx + hw - tp, my + hy), (mx - hw + tp, my + hy)],
              fill=YELLOW)
    ty = my - tblk / 2
    for ln in ct:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, mx - lw / 2, ty, ln)
        ty += line_h(ctx.f.head) + 4
    for ln in cs:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, mx - lw / 2, ty, ln)
        ty += line_h(ctx.f.small) + 4
    return tot


# ================================================================= switch ====
def _sw_geom(ctx, b, width):
    midw = width * 0.24
    g = 30
    pw = (width - midw - 2 * g) / 2
    ph = 0
    for side in (b["normal"], b["exception"]):
        h = 16 + line_h(ctx.f.head) + 12
        h += R._bullet_items_h(ctx, side["items"], pw - 44, font=ctx.f.small, tag=side["h"])
        ph = max(ph, h + 18)
    trig = []
    for t in b["triggers"]:
        trig.append(wrap_runs([(t, ctx.f.smallb, YELLOW)], midw - 20, "sw"))
    trigh = sum(len(l) for l in trig) * (line_h(ctx.f.smallb) + 4) + 8 * len(trig)
    ret = _rich(ctx, b["ret"], ctx.f.small, ctx.f.smallb, WHITE, TEAL, midw - 12, "sw")
    reth = len(ret) * (line_h(ctx.f.small) + 4)
    tot = max(ph, trigh + 96 + reth + 30)
    return midw, g, pw, ph, trig, trigh, ret, reth, tot


def _sw_h(ctx, b, width):
    return _sw_geom(ctx, b, width)[8]


def _sw_draw(ctx, d, b, x, y, width):
    midw, g, pw, ph, trig, trigh, ret, reth, tot = _sw_geom(ctx, b, width)
    for side, sx in ((b["normal"], x), (b["exception"], x + pw + midw + 2 * g)):
        c = col(side.get("c", "cyan"))
        rrect(d, [sx, y, sx + pw, y + tot], radius=16, fill=CARD_TITLE, outline=c, width=3)
        hb = line_h(ctx.f.head) + 14
        rrect(d, [sx, y, sx + pw, y + hb], radius=16, fill=c)
        d.rectangle([sx, y + hb - 16, sx + pw, y + hb], fill=c)
        d.text((sx + 20, y + 6), side["h"], font=ctx.f.head, fill=BG)
        R._draw_bullets(ctx, d, sx + 22, y + hb + 14, pw - 44, side["items"], c,
                        font=ctx.f.small, tag=side["h"])
    mx = x + pw + g + midw / 2
    ty = y + 4
    for lines in trig:
        for ln in lines:
            lw = sum(text_w(f, t) for t, f, _ in ln)
            draw_runs_line(d, mx - lw / 2, ty, ln)
            ty += line_h(ctx.f.smallb) + 4
        ty += 8
    sy = ty + 22
    d.ellipse([mx - midw * 0.30 - 11, sy - 11, mx - midw * 0.30 + 11, sy + 11], fill=YELLOW)
    d.ellipse([mx + midw * 0.30 - 11, sy - 11, mx + midw * 0.30 + 11, sy + 11], fill=YELLOW)
    d.line([(mx - midw * 0.30, sy), (mx + midw * 0.30, sy - 30)], fill=YELLOW, width=8)
    arrow_right(d, x + pw + 6, sy + 34, x + pw + 2 * g + midw - 6, YELLOW, thick=8, head=26)
    ry = sy + 58
    d.line([(mx + midw * 0.34, ry), (mx - midw * 0.34, ry)], fill=TEAL, width=6)
    d.polygon([(mx - midw * 0.34 - 18, ry), (mx - midw * 0.34, ry - 11),
               (mx - midw * 0.34, ry + 11)], fill=TEAL)
    ty = ry + 18
    for ln in ret:
        lw = sum(text_w(f, t) for t, f, _ in ln)
        draw_runs_line(d, mx - lw / 2, ty, ln)
        ty += line_h(ctx.f.small) + 4
    return tot


# ================================================================ tension ====
def _ten_geom(ctx, b, width):
    vw = width * 0.22
    g = 26
    sw = (width - vw - 2 * g) / 2
    rhs = []
    for r in b["rows"]:
        a = _rich(ctx, r["l"], ctx.f.small, ctx.f.smallb, WHITE, GREEN, sw - 32, "ten")
        c = _rich(ctx, r["r"], ctx.f.small, ctx.f.smallb, WHITE, RED, sw - 32, "ten")
        v = wrap_runs([(r["v"], ctx.f.smallb, BG)], vw - 26, "ten")
        rhs.append(max(len(a), len(c)) * (line_h(ctx.f.small) + 5) + 24)
        rhs[-1] = max(rhs[-1], len(v) * (line_h(ctx.f.smallb) + 4) + 20)
    hh = line_h(ctx.f.smallb) + 14
    return vw, g, sw, rhs, hh


def _ten_h(ctx, b, width):
    vw, g, sw, rhs, hh = _ten_geom(ctx, b, width)
    return hh + sum(rhs) + 14 * (len(rhs) - 1)


def _ten_draw(ctx, d, b, x, y, width):
    vw, g, sw, rhs, hh = _ten_geom(ctx, b, width)
    d.text((x + 6, y), b["h_l"], font=ctx.f.smallb, fill=GREEN)
    hw = text_w(ctx.f.smallb, b["h_v"])
    d.text((x + sw + g + (vw - hw) / 2, y), b["h_v"], font=ctx.f.smallb, fill=YELLOW)
    rw = text_w(ctx.f.smallb, b["h_r"])
    d.text((x + width - rw - 6, y), b["h_r"], font=ctx.f.smallb, fill=RED)
    cy = y + hh
    for j, r in enumerate(b["rows"]):
        rh = rhs[j]
        rrect(d, [x, cy, x + sw, cy + rh], radius=11, fill=(14, 38, 30), outline=GREEN, width=2)
        ty = cy + 11
        for ln in _rich(ctx, r["l"], ctx.f.small, ctx.f.smallb, WHITE, GREEN, sw - 32, "ten"):
            draw_runs_line(d, x + 16, ty, ln)
            ty += line_h(ctx.f.small) + 5
        rx = x + sw + g + vw + g
        rrect(d, [rx, cy, rx + sw, cy + rh], radius=11, fill=(40, 22, 26), outline=RED, width=2)
        ty = cy + 11
        for ln in _rich(ctx, r["r"], ctx.f.small, ctx.f.smallb, WHITE, RED, sw - 32, "ten"):
            draw_runs_line(d, rx + 16, ty, ln)
            ty += line_h(ctx.f.small) + 5
        vx = x + sw + g
        v = wrap_runs([(r["v"], ctx.f.smallb, BG)], vw - 26, "ten")
        vh = len(v) * (line_h(ctx.f.smallb) + 4) + 16
        vy = cy + (rh - vh) / 2
        rrect(d, [vx, vy, vx + vw, vy + vh], radius=10, fill=col(r.get("c", "yellow")))
        ty = vy + 7
        for ln in v:
            lw = sum(text_w(f, t) for t, f, _ in ln)
            draw_runs_line(d, vx + (vw - lw) / 2, ty, ln)
            ty += line_h(ctx.f.smallb) + 4
        arrow_right(d, x + sw + 4, cy + rh / 2, vx - 4, GREEN, thick=4, head=13)
        d.line([(rx - 4, cy + rh / 2), (vx + vw + 18, cy + rh / 2)], fill=RED, width=4)
        d.polygon([(vx + vw + 4, cy + rh / 2), (vx + vw + 18, cy + rh / 2 - 9),
                   (vx + vw + 18, cy + rh / 2 + 9)], fill=RED)
        cy += rh + 14
    return _ten_h(ctx, b, width)


# ==================================================================== web ====
def _web_geom(ctx, b, width):
    aw = width * 0.155
    g = 20
    xw = 44
    tw = width - 2 * aw - xw - 3 * g
    rhs = []
    for r in b["rows"]:
        a = wrap_runs([(r["a"], ctx.f.smallb, BG)], aw - 26, "web")
        bb = wrap_runs([(r["b"], ctx.f.smallb, BG)], aw - 26, "web")
        t = _rich(ctx, r["t"], ctx.f.small, ctx.f.smallb, WHITE, YELLOW, tw - 34, "web")
        h = max(len(a), len(bb)) * (line_h(ctx.f.smallb) + 4) + 20
        h = max(h, len(t) * (line_h(ctx.f.small) + 5) + 22)
        rhs.append(h)
    hh = line_h(ctx.f.smallb) + 14
    return aw, g, xw, tw, rhs, hh


def _web_h(ctx, b, width):
    aw, g, xw, tw, rhs, hh = _web_geom(ctx, b, width)
    return hh + sum(rhs) + 12 * (len(rhs) - 1)


def _web_draw(ctx, d, b, x, y, width):
    aw, g, xw, tw, rhs, hh = _web_geom(ctx, b, width)
    d.text((x + 6, y), b["h_pair"], font=ctx.f.smallb, fill=CYAN)
    d.text((x + 2 * aw + xw + 3 * g + 6, y), b["h_out"], font=ctx.f.smallb, fill=YELLOW)
    cy = y + hh
    for j, r in enumerate(b["rows"]):
        rh = rhs[j]
        c = col(r.get("c", "cyan"))
        for k, key in enumerate(("a", "b")):
            bx = x + k * (aw + g + xw + g if k else 0)
            lines = wrap_runs([(r[key], ctx.f.smallb, BG)], aw - 26, "web")
            lh = len(lines) * (line_h(ctx.f.smallb) + 4) + 16
            by = cy + (rh - lh) / 2
            rrect(d, [bx, by, bx + aw, by + lh], radius=10, fill=c)
            ty = by + 7
            for ln in lines:
                draw_runs_line(d, bx + 13, ty, ln)
                ty += line_h(ctx.f.smallb) + 4
        xx = x + aw + g + xw / 2
        d.text((xx - text_w(ctx.f.head, "\u00d7") / 2, cy + rh / 2 - line_h(ctx.f.head) / 2),
               "\u00d7", font=ctx.f.head, fill=YELLOW)
        tx = x + 2 * aw + xw + 3 * g
        arrow_right(d, tx - g - 6, cy + rh / 2, tx - 4, YELLOW, thick=4, head=14)
        rrect(d, [tx, cy, tx + tw, cy + rh], radius=11, fill=(28, 34, 46), outline=c, width=2)
        ty = cy + 11
        for ln in _rich(ctx, r["t"], ctx.f.small, ctx.f.smallb, WHITE, YELLOW, tw - 34, "web"):
            draw_runs_line(d, tx + 17, ty, ln)
            ty += line_h(ctx.f.small) + 5
        cy += rh + 12
    return _web_h(ctx, b, width)


R.BLOCKS.update({
    "pyramid": (_pyr_h, _pyr_draw),
    "triad": (_triad_h, _triad_draw),
    "vs3": (_vs3_h, _vs3_draw),
    "bus": (_bus_h, _bus_draw),
    "constel": (_con_h, _con_draw),
    "switch": (_sw_h, _sw_draw),
    "tension": (_ten_h, _ten_draw),
    "web": (_web_h, _web_draw),
})
