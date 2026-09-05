"""Build the Polity 01 continuous at-a-glance master flow, generation g9."""
from __future__ import annotations

import hashlib
import io
import json
import math
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import render_lib as R           # noqa: E402
from render_lib import (         # noqa: E402
    BG, CARD, CARD_TITLE, CARD_EXTRA, CYAN, YELLOW, GREY, WHITE, DIM, RULE,
    Fonts, Ctx, blocks_h, blocks_draw, col, line_h, text_w, rrect, wrap_runs,
    arrow_right, measure, render,
)
import spec_content as S         # noqa: E402

Image.MAX_IMAGE_PIXELS = None

ROOT = HERE.parents[4]
REF_DIR = ROOT / "notes" / "Philosophy" / "flowcharts" / \
    "philosophy-paper-i-indian-philosophy-01" / "continuous-at-a-glance-core-first"
G8_DIR = HERE.parent / "continuous-at-a-glance-carvaka-standard-g8"
PREV = HERE / "previews"
PREV.mkdir(parents=True, exist_ok=True)

REF_EXPECTED = {
    "Carvaka_Continuous-At-a-Glance-Core-First_Poster_2026-08-22.pdf":
        "F291DDE859557D822B91902027B070BB649E92F20C52E9031B1521A9DDE16D90",
    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png":
        "C9AE34E995375348A6998885784DED0680C0A8F8E3CD6CB82BB4CD5385E85C62",
    "Carvaka_Continuous-At-a-Glance-Core-First_Tiled_2026-08-22.pdf":
        "EB3E452797F15BAC2599431E72BC69EFEDB66AA104367C6F0404B4ABE3296D6E",
}

# ---------------------------------------------------------------- metrics ----
W = 4800
DPI = 300
MARGIN = 110
RAIL_X = 250
CARD_X0 = 520
CARD_X1 = 4690
CARD_W = CARD_X1 - CARD_X0
PAD = 46
INNER_W = CARD_W - 2 * PAD
STAGE_GAP = 64

DATESTAMP = date.today().isoformat()
MASTER = HERE / "master.png"
POSTER = HERE / f"Polity01_Continuous-At-a-Glance_g9_Poster_{DATESTAMP}.pdf"
TILED = HERE / f"Polity01_Continuous-At-a-Glance_g9_Tiled_{DATESTAMP}.pdf"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest().upper()


# ------------------------------------------------------------ measurement ----
def header_h(ctx):
    h = 34
    h += len(wrap_runs([(S.HEADER["title"], ctx.f.title, WHITE)], W - 2 * MARGIN - 80, "title")) * (line_h(ctx.f.title) + 6)
    h += 10
    h += len(wrap_runs([(S.HEADER["subtitle"], ctx.f.subtitle, CYAN)], W - 2 * MARGIN - 80, "subtitle")) * (line_h(ctx.f.subtitle) + 6)
    h += 12
    h += len(wrap_runs([(S.HEADER["note"], ctx.f.note, DIM)], W - 2 * MARGIN - 80, "note")) * (line_h(ctx.f.note) + 6)
    h += 22
    h += line_h(ctx.f.pill) + 16          # legend chips
    h += 14
    h += len(wrap_runs([(S.HEADER["key"], ctx.f.note, WHITE)], W - 2 * MARGIN - 80, "key")) * (line_h(ctx.f.note) + 6)
    h += 6
    h += line_h(ctx.f.note) + 6           # approval
    return h + 34


def stage_title_font(ctx, st):
    f = ctx.f.stage
    badge_w = text_w(ctx.f.badge, "STAGE " + st["n"]) + 36
    avail = INNER_W - badge_w - 26
    if text_w(f, st["title"]) > avail * 2.0:
        f = ctx.f.stage_sm
    return f, badge_w, avail


def stage_head_h(ctx, st):
    f, badge_w, avail = stage_title_font(ctx, st)
    lines = wrap_runs([(st["title"], f, WHITE)], avail, "stage-title")
    return max(line_h(ctx.f.badge) + 14, len(lines) * (line_h(f) + 4)), f, badge_w, avail, lines


def stage_h(ctx, st):
    hh, *_ = stage_head_h(ctx, st)
    h = 26 + hh + 18
    h += R._pills_h(ctx, {"pills": st["pills"]}, INNER_W) + 24
    h += blocks_h(ctx, st["blocks"], INNER_W)
    return h + 34


# --------------------------------------------------------------- drawing -----
def draw_header(ctx, d, y):
    h = header_h(ctx)
    rrect(d, [MARGIN, y, W - MARGIN, y + h], radius=26, fill=CARD_TITLE, outline=CYAN, width=4)
    x = MARGIN + 40
    cy = y + 34
    for ln in wrap_runs([(S.HEADER["title"], ctx.f.title, WHITE)], W - 2 * MARGIN - 80, "title"):
        R.draw_runs_line(d, x, cy, ln)
        cy += line_h(ctx.f.title) + 6
    cy += 10
    for ln in wrap_runs([(S.HEADER["subtitle"], ctx.f.subtitle, CYAN)], W - 2 * MARGIN - 80, "subtitle"):
        R.draw_runs_line(d, x, cy, ln)
        cy += line_h(ctx.f.subtitle) + 6
    cy += 12
    for ln in wrap_runs([(S.HEADER["note"], ctx.f.note, DIM)], W - 2 * MARGIN - 80, "note"):
        R.draw_runs_line(d, x, cy, ln)
        cy += line_h(ctx.f.note) + 6
    cy += 22
    ph = line_h(ctx.f.pill) + 16
    cx = x
    for chip in S.HEADER["legend"]:
        c = col(chip["c"])
        cw = text_w(ctx.f.pill, chip["t"]) + 54
        rrect(d, [cx, cy, cx + cw, cy + ph], radius=ph / 2, fill=None, outline=c, width=3)
        d.ellipse([cx + 16, cy + ph / 2 - 8, cx + 32, cy + ph / 2 + 8], fill=c)
        d.text((cx + 42, cy + 6), chip["t"], font=ctx.f.pill, fill=c)
        cx += cw + 20
    ap = S.HEADER["approval"]
    d.text((W - MARGIN - 40 - text_w(ctx.f.note, ap), cy + 8), ap, font=ctx.f.note, fill=DIM)
    cy += ph + 14
    for ln in wrap_runs([(S.HEADER["key"], ctx.f.note, WHITE)], W - 2 * MARGIN - 80, "key"):
        R.draw_runs_line(d, x, cy, ln)
        cy += line_h(ctx.f.note) + 6
    return h


def draw_stage(ctx, d, st, y):
    h = stage_h(ctx, st)
    kind = st["kind"]
    border = {"core": CYAN, "pivot": YELLOW, "extra": GREY}[kind]
    fill = {"core": CARD, "pivot": (22, 44, 58), "extra": CARD_EXTRA}[kind]
    bw = {"core": 4, "pivot": 6, "extra": 3}[kind]
    rrect(d, [CARD_X0, y, CARD_X1, y + h], radius=24, fill=fill, outline=border, width=bw)

    hh, f, badge_w, avail, lines = stage_head_h(ctx, st)
    x = CARD_X0 + PAD
    cy = y + 26
    bh = line_h(ctx.f.badge) + 14
    badge_txt = "STAGE " + st["n"] if st["n"] != "E" else "EXTRA"
    bwid = text_w(ctx.f.badge, badge_txt) + 36
    rrect(d, [x, cy + (hh - bh) / 2, x + bwid, cy + (hh - bh) / 2 + bh], radius=bh / 2, fill=border)
    d.text((x + 18, cy + (hh - bh) / 2 + 5), badge_txt, font=ctx.f.badge, fill=BG)
    tx = x + bwid + 26
    ty = cy + (hh - len(lines) * (line_h(f) + 4)) / 2
    for ln in wrap_runs([(st["title"], f, WHITE if kind != "extra" else GREY)], INNER_W - bwid - 26, "stage-title"):
        R.draw_runs_line(d, tx, ty, ln)
        ty += line_h(f) + 4
    cy += hh + 18
    cy += R._pills_draw(ctx, d, {"pills": st["pills"]}, x, cy, INNER_W) + 24
    blocks_draw(ctx, d, st["blocks"], x, cy, INNER_W)
    return h, y + 26 + hh / 2


def build_master():
    fonts = Fonts()
    ctx = Ctx(fonts)
    hh = header_h(ctx)
    stage_heights = [stage_h(ctx, st) for st in S.STAGES]
    total = 44 + hh + 54 + sum(stage_heights) + STAGE_GAP * (len(S.STAGES) - 1) + 46 + line_h(fonts.note) + 60
    H = int(math.ceil(total))

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # subtle top glow band
    for i in range(160):
        t = i / 160
        c = tuple(int(BG[k] + (11 - BG[k]) * (1 - t) * 0.7 + (0 if k else 0)) for k in range(3))
        d.line([(0, i), (W, i)], fill=(c[0], c[1] + 2, c[2] + 4))

    y = 44
    y += draw_header(ctx, d, y)
    y += 54

    rail_top = y - 20
    centres = []
    for st, sh in zip(S.STAGES, stage_heights):
        _, cyc = draw_stage(ctx, d, st, y)
        centres.append((cyc, st))
        y += sh + STAGE_GAP
    y -= STAGE_GAP
    rail_bottom = centres[-1][0]

    # continuous rail behind the numbered nodes
    d.line([(RAIL_X, rail_top), (RAIL_X, rail_bottom)], fill=CYAN, width=9)
    d.line([(RAIL_X, centres[-2][0]), (RAIL_X, rail_bottom)], fill=GREY, width=9)
    for cyc, st in centres:
        c = {"core": CYAN, "pivot": YELLOW, "extra": GREY}[st["kind"]]
        r = 46 if st["kind"] != "pivot" else 54
        d.ellipse([RAIL_X - r, cyc - r, RAIL_X + r, cyc + r], fill=BG, outline=c, width=8)
        lab = st["n"]
        lw = text_w(fonts.rail, lab)
        d.text((RAIL_X - lw / 2, cyc - line_h(fonts.rail) / 2), lab, font=fonts.rail, fill=c)
        arrow_right(d, RAIL_X + r + 8, cyc, CARD_X0 - 6, c, thick=6, head=20)

    fy = y + 46
    d.text((MARGIN + 10, fy), S.FOOTER, font=fonts.note, fill=DIM)

    img.save(MASTER, dpi=(DPI, DPI))
    return img, H, stage_heights


# ------------------------------------------------------------------- pdfs ----
def build_poster(img):
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas as rl_canvas
    Wp = 39.37 * 72
    Hp = Wp * img.height / img.width
    if Hp > 190 * 72:
        Hp = 190 * 72
        Wp = Hp * img.width / img.height
    c = rl_canvas.Canvas(str(POSTER), pagesize=(Wp, Hp))
    c.setFillColorRGB(BG[0] / 255, BG[1] / 255, BG[2] / 255)
    c.rect(0, 0, Wp, Hp, fill=1, stroke=0)
    c.drawImage(ImageReader(img), 0, 0, width=Wp, height=Hp)
    c.setTitle("Polity 01 — Historical Background — Continuous At-a-Glance Master Flow (g9)")
    c.showPage()
    c.save()
    return Wp / 72, Hp / 72


def build_tiled(img):
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas as rl_canvas
    fonts = Fonts()
    PW, PH = 1190.55, 841.89          # A3 landscape, points
    M = 18
    foot = 26
    area_w = PW - 2 * M
    area_h = PH - 2 * M - foot
    tile_px = int(round(img.width * area_h / area_w))
    min_overlap = 240
    n = max(1, math.ceil((img.height - min_overlap) / (tile_px - min_overlap)))
    step = (img.height - tile_px) / (n - 1) if n > 1 else 0
    overlap = int(round(tile_px - step)) if n > 1 else 0
    c = rl_canvas.Canvas(str(TILED), pagesize=(PW, PH))
    crops = []
    for i in range(n):
        top = int(round(i * step))
        bot = min(top + tile_px, img.height)
        crop = img.crop((0, top, img.width, bot))
        buf = io.BytesIO()
        crop.save(buf, format="PNG")
        crops.append({"tile": i + 1, "box": [0, top, img.width, bot],
                      "sha256": sha256_bytes(buf.getvalue())})
        c.setFillColorRGB(BG[0] / 255, BG[1] / 255, BG[2] / 255)
        c.rect(0, 0, PW, PH, fill=1, stroke=0)
        dh = area_w * crop.height / crop.width
        c.drawImage(ImageReader(crop), M, PH - M - dh, width=area_w, height=dh)
        c.setFont("Helvetica", 9)
        c.setFillColorRGB(0.61, 0.71, 0.78)
        c.drawString(M + 2, M - 4,
                     f"POLITY 01 — CONTINUOUS AT-A-GLANCE MASTER FLOW (g9)  ·  TILE {i+1} OF {n}  ·  "
                     f"same master canvas, overlapping crop rows {top}–{bot} of {img.height}  ·  "
                     + ("continues below" if i < n - 1 else "end of master canvas"))
        c.showPage()
    c.setTitle("Polity 01 — Continuous At-a-Glance Master Flow (g9) — tiled")
    c.save()
    return n, tile_px, overlap, crops


def build_previews():
    import fitz
    doc = fitz.open(str(TILED))
    paths = []
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=110)
        p = PREV / f"page-{i+1:03d}.png"
        pix.save(str(p))
        paths.append(p)
    doc.close()
    return paths


def build_contact_sheets(paths, per_sheet=6, cols=3, gap=22):
    sheets = []
    for s in range(0, len(paths), per_sheet):
        chunk = paths[s:s + per_sheet]
        ims = [Image.open(p).convert("RGB") for p in chunk]
        tw = max(i.width for i in ims)
        th = max(i.height for i in ims)
        ncols = min(cols, len(chunk))
        nrows = math.ceil(len(chunk) / ncols)
        # last row may be short: crop the sheet width to the widest used row
        used_cols_last = len(chunk) - ncols * (nrows - 1)
        sheet_w = gap + ncols * (tw + gap)
        sheet_h = gap + nrows * (th + gap)
        sheet = Image.new("RGB", (sheet_w, sheet_h), (7, 20, 33))
        dd = ImageDraw.Draw(sheet)
        for k, im in enumerate(ims):
            r, cc = divmod(k, ncols)
            if r == nrows - 1 and used_cols_last < ncols:
                row_w = gap + used_cols_last * (tw + gap)
                x = gap + cc * (tw + gap) + (sheet_w - row_w) // 2
            else:
                x = gap + cc * (tw + gap)
            yy = gap + r * (th + gap)
            sheet.paste(im, (x, yy))
            dd.rectangle([x - 2, yy - 2, x + im.width + 1, yy + im.height + 1],
                         outline=(68, 211, 255), width=2)
        out = PREV / f"contact-sheet-{s // per_sheet + 1:02d}.png"
        sheet.save(out)
        sheets.append(out)
    return sheets


def blank_waste(path, tiles=None):
    """Uncovered-area fraction and the largest fully-background horizontal band."""
    im = Image.open(path).convert("RGB")
    px = im.load()
    bgc = (7, 20, 33)
    step = 5
    runs, cur = [], 0
    for y in range(im.height):
        if all(px[x, y] == bgc for x in range(0, im.width, step)):
            cur += 1
        else:
            runs.append(cur)
            cur = 0
    runs.append(cur)
    band = max(runs) / im.height
    covered = None
    if tiles:
        covered = sum(w * h for w, h in tiles) / (im.width * im.height)
    return band, covered, im.size


# ------------------------------------------------------------------- spec ----
def layout_signature(st):
    sig = []
    for b in st["blocks"]:
        if b["type"] == "row":
            sig.append("row(" + "+".join(c["block"]["type"] for c in b["children"]) + ")")
        elif b["type"] == "cols":
            sig.append(f"cols{len(b['cols'])}")
        elif b["type"] == "panels":
            sig.append(f"panels{len(b['panels'])}")
        else:
            sig.append(b["type"])
    return sig


def write_spec(H, stage_heights, tile_info):
    n, tile_px, overlap, crops = tile_info
    spec = {
        "artifact": "Polity 01 — Historical Background of the Indian Constitution — continuous at-a-glance master flow",
        "generation": "polity-01:flowchart:continuous-at-a-glance-carvaka-standard:g9",
        "supersedes": "continuous-at-a-glance-carvaka-standard-g8 (REJECTED — repeated identical three-column cards, thin content, no internal branching, superficial pills, blank contact-sheet region)",
        "approved": False,
        "generated": DATESTAMP,
        "design_reference": {
            "folder": str(REF_DIR).replace(str(ROOT) + "\\", ""),
            "status": "IMMUTABLE — read only, never modified",
            "matched_properties": [
                "4800 px wide master at 300 dpi metadata",
                "strong title card with legend chips and reading instruction",
                "numbered continuous rail with per-stage nodes and connectors",
                "per-stage individually chosen internal layout, not a fixed card schema",
                "dense decisive keyword pill rows",
                "multi-column branches and direct institutional comparisons",
                "compact high-information bullets",
                "mechanism / bridge / trap bands",
                "magenta answer-grabbing line",
                "complete numbered core before a visually subordinate enrichment band",
                "final synthesis stage with comparison matrix and PYQ routes",
                "poster preserves the whole canvas; tiled PDF crops the same canvas with overlap",
            ],
        },
        "sources": {
            "canonical_learner_v2_owner": S.OWNER,
            "advanced_owner": S.ADV_OWNER,
            "cross_owned_mechanism_owner": S.CROSS_OWNER,
            "fabrication_policy": "No fact is introduced that is not present in the owners above. Inferred PYQ keys are labelled inferred on the canvas.",
        },
        "canvas": {
            "width_px": W, "height_px": H, "dpi": DPI,
            "margin_px": MARGIN, "rail_x_px": RAIL_X,
            "card_x0_px": CARD_X0, "card_x1_px": CARD_X1,
            "card_padding_px": PAD, "stage_gap_px": STAGE_GAP,
        },
        "palette": {k: list(v) for k, v in R.COLOURS.items()} | {
            "background": list(BG), "card": list(CARD), "card_title": list(CARD_TITLE),
            "card_extra": list(CARD_EXTRA), "answer_fill": list(R.ANSWER_FILL),
        },
        "typography": {
            "family": "Segoe UI / Segoe UI Bold",
            "poster_title_px": 72, "stage_title_px": 55, "section_head_px": 34,
            "body_px": 30, "pill_px": 29, "matrix_px": 27,
        },
        "block_vocabulary": {
            "cols": "n-column branch with coloured section heads and compact bullets",
            "pills": "wrapped rows of decisive keyword chips",
            "chain": "horizontal causal chain of boxes with arrows",
            "panels": "institution-versus-function split with a centre relation label",
            "replace": "before/after institutional replacement with a large transfer arrow and continuity caution",
            "matrix": "comparison / repair / commenced-versus-not-commenced table",
            "timeline": "dated horizontal bridge strip",
            "ladder": "stepped vertical progression of a single institution",
            "band": "labelled mechanism, bridge, trap, source-caution or PYQ band",
            "answer": "magenta answer-grabbing line",
            "row": "side-by-side container for two heterogeneous blocks",
        },
        "outputs": {
            "master_png": MASTER.name,
            "poster_pdf": POSTER.name,
            "tiled_pdf": TILED.name,
            "tiles": n, "tile_height_px": tile_px, "tile_overlap_px": overlap,
            "tile_crops": crops,
        },
        "header": S.HEADER,
        "footer": S.FOOTER,
        "stages": [
            {
                "n": st["n"], "kind": st["kind"], "title": st["title"],
                "height_px": int(round(h)),
                "layout_signature": layout_signature(st),
                "pill_count": len(st["pills"]),
                "pills": [p["t"] for p in st["pills"]],
                "blocks": st["blocks"],
            }
            for st, h in zip(S.STAGES, stage_heights)
        ],
        "must_show_terms": S.MUST_SHOW,
    }
    (HERE / "bespoke-design-spec.json").write_text(
        json.dumps(spec, indent=1, ensure_ascii=False), encoding="utf-8")
    return spec


def spec_text_blob(spec):
    return json.dumps(spec["stages"], ensure_ascii=False)


# ------------------------------------------------------------------- main ----
def main():
    before = {str(p.relative_to(G8_DIR)): sha256(p) for p in sorted(G8_DIR.rglob("*")) if p.is_file()}
    ref_now = {str(p.relative_to(REF_DIR)): sha256(p) for p in sorted(REF_DIR.rglob("*")) if p.is_file()}

    img, H, stage_heights = build_master()
    poster_dims = build_poster(img)
    tile_info = build_tiled(img)
    previews = build_previews()
    sheets = build_contact_sheets(previews)
    spec = write_spec(H, stage_heights, tile_info)

    after = {str(p.relative_to(G8_DIR)): sha256(p) for p in sorted(G8_DIR.rglob("*")) if p.is_file()}
    ref_after = {str(p.relative_to(REF_DIR)): sha256(p) for p in sorted(REF_DIR.rglob("*")) if p.is_file()}

    json.dump({
        "built": DATESTAMP,
        "master_size": list(img.size),
        "overflow_events": [list(o) for o in R.OVERFLOWS],
        "g8_hashes_before_build": before,
        "g8_hashes_after_build": after,
        "reference_hashes_before_build": ref_now,
        "reference_hashes_after_build": ref_after,
    }, open(HERE / "build-audit.json", "w", encoding="utf-8"), indent=1)

    return {
        "img": img, "H": H, "poster_dims": poster_dims, "tile_info": tile_info,
        "previews": previews, "sheets": sheets, "spec": spec,
        "g8_before": before, "g8_after": after,
        "ref_before": ref_now, "ref_after": ref_after,
    }


if __name__ == "__main__":
    res = main()
    print("master", res["img"].size, "poster_in", res["poster_dims"],
          "tiles", res["tile_info"][0], "overflows", len(R.OVERFLOWS))
    for o in R.OVERFLOWS[:20]:
        print("  OVERFLOW", o)
