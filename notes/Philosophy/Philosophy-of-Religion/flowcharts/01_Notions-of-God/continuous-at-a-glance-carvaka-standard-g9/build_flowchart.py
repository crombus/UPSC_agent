from __future__ import annotations

import io
import json
import math
import sys
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import render_lib as R
from render_lib import (
    BG, CARD, CARD_EXTRA, CARD_TITLE, CYAN, DIM, GREY, RULE, WHITE, YELLOW,
    Ctx, Fonts, arrow_right, blocks_draw, blocks_h, col, line_h, rrect, text_w,
    wrap_runs,
)
import spec_content as S


Image.MAX_IMAGE_PIXELS = None
W, DPI = 4800, 300
MARGIN, RAIL_X = 110, 250
CARD_X0, CARD_X1 = 520, 4690
CARD_W, PAD = CARD_X1 - CARD_X0, 46
INNER_W, STAGE_GAP = CARD_W - 2 * PAD, 64

DATESTAMP = "2026-08-22"
MASTER = HERE / "NotionsOfGod_Continuous-At-a-Glance_Carvaka-g9_Master.png"
POSTER = HERE / f"NotionsOfGod_Continuous-At-a-Glance_Carvaka-g9_Poster_{DATESTAMP}.pdf"
TILED = HERE / f"NotionsOfGod_Continuous-At-a-Glance_Carvaka-g9_Tiled_{DATESTAMP}.pdf"
PREVIEWS = HERE / "previews"
PREVIEWS.mkdir(parents=True, exist_ok=True)


def header_h(ctx):
    h = 34
    for text, f in (
        (S.HEADER["title"], ctx.f.title),
        (S.HEADER["subtitle"], ctx.f.subtitle),
        (S.HEADER["note"], ctx.f.note),
    ):
        h += len(wrap_runs([(text, f, WHITE)], W - 2 * MARGIN - 80, "header")) * (line_h(f) + 6) + 10
    h += 20 + line_h(ctx.f.pill) + 16
    h += 14 + len(wrap_runs([(S.HEADER["key"], ctx.f.note, WHITE)], W - 2 * MARGIN - 80, "key")) * (line_h(ctx.f.note) + 6)
    h += line_h(ctx.f.note) + 34
    return h


def stage_title_font(ctx, stage):
    badge_w = text_w(ctx.f.badge, "STAGE " + stage["n"]) + 36
    available = INNER_W - badge_w - 26
    f = ctx.f.stage if text_w(ctx.f.stage, stage["title"]) <= available * 2 else ctx.f.stage_sm
    return f, badge_w, available


def stage_head_h(ctx, stage):
    f, badge_w, available = stage_title_font(ctx, stage)
    lines = wrap_runs([(stage["title"], f, WHITE)], available, "stage-title")
    return max(line_h(ctx.f.badge) + 14, len(lines) * (line_h(f) + 4)), f, badge_w, lines


def stage_h(ctx, stage):
    hh, *_ = stage_head_h(ctx, stage)
    return (
        26 + hh + 18
        + R._pills_h(ctx, {"pills": stage["pills"]}, INNER_W) + 24
        + blocks_h(ctx, stage["blocks"], INNER_W) + 34
    )


def draw_header(ctx, draw, y):
    h = header_h(ctx)
    rrect(draw, (MARGIN, y, W - MARGIN, y + h), 26, CARD_TITLE, CYAN, 4)
    x, cy = MARGIN + 40, y + 34
    for text, f, colour in (
        (S.HEADER["title"], ctx.f.title, WHITE),
        (S.HEADER["subtitle"], ctx.f.subtitle, CYAN),
        (S.HEADER["note"], ctx.f.note, DIM),
    ):
        for line in wrap_runs([(text, f, colour)], W - 2 * MARGIN - 80, "header"):
            R.draw_runs_line(draw, x, cy, line)
            cy += line_h(f) + 6
        cy += 10
    cy += 10
    ph = line_h(ctx.f.pill) + 16
    cx = x
    for chip in S.HEADER["legend"]:
        colour = col(chip["c"])
        width = text_w(ctx.f.pill, chip["t"]) + 54
        rrect(draw, (cx, cy, cx + width, cy + ph), ph / 2, None, colour, 3)
        draw.ellipse((cx + 16, cy + ph / 2 - 8, cx + 32, cy + ph / 2 + 8), fill=colour)
        draw.text((cx + 42, cy + 6), chip["t"], font=ctx.f.pill, fill=colour)
        cx += width + 20
    approval = S.HEADER["approval"]
    draw.text((W - MARGIN - 40 - text_w(ctx.f.note, approval), cy + 8), approval, font=ctx.f.note, fill=DIM)
    cy += ph + 14
    for line in wrap_runs([(S.HEADER["key"], ctx.f.note, WHITE)], W - 2 * MARGIN - 80, "key"):
        R.draw_runs_line(draw, x, cy, line)
        cy += line_h(ctx.f.note) + 6
    return h


def draw_stage(ctx, draw, stage, y):
    h = stage_h(ctx, stage)
    border = {"core": CYAN, "pivot": YELLOW, "extra": GREY}[stage["kind"]]
    fill = {"core": CARD, "pivot": (22, 44, 58), "extra": CARD_EXTRA}[stage["kind"]]
    rrect(draw, (CARD_X0, y, CARD_X1, y + h), 24, fill, border, 6 if stage["kind"] == "pivot" else 4)
    hh, f, _, lines = stage_head_h(ctx, stage)
    x, cy = CARD_X0 + PAD, y + 26
    label = "EXTRA" if stage["n"] == "E" else "STAGE " + stage["n"]
    badge_h = line_h(ctx.f.badge) + 14
    badge_w = text_w(ctx.f.badge, label) + 36
    rrect(draw, (x, cy + (hh - badge_h) / 2, x + badge_w, cy + (hh + badge_h) / 2),
          badge_h / 2, border)
    draw.text((x + 18, cy + (hh - badge_h) / 2 + 5), label, font=ctx.f.badge, fill=BG)
    tx = x + badge_w + 26
    ty = cy + (hh - len(lines) * (line_h(f) + 4)) / 2
    for line in lines:
        R.draw_runs_line(draw, tx, ty, line)
        ty += line_h(f) + 4
    cy += hh + 18
    cy += R._pills_draw(ctx, draw, {"pills": stage["pills"]}, x, cy, INNER_W) + 24
    blocks_draw(ctx, draw, stage["blocks"], x, cy, INNER_W)
    return h, y + 26 + hh / 2


def build_master():
    R.OVERFLOWS.clear()
    ctx = Ctx(Fonts())
    heights = [stage_h(ctx, stage) for stage in S.STAGES]
    total_h = int(math.ceil(44 + header_h(ctx) + 54 + sum(heights) + STAGE_GAP * (len(heights) - 1) + 130))
    image = Image.new("RGB", (W, total_h), BG)
    draw = ImageDraw.Draw(image)
    y = 44
    y += draw_header(ctx, draw, y) + 54
    rail_top = y - 20
    centres = []
    for stage, height in zip(S.STAGES, heights):
        _, centre = draw_stage(ctx, draw, stage, y)
        centres.append((centre, stage))
        y += height + STAGE_GAP
    y -= STAGE_GAP
    rail_bottom = centres[-1][0]
    draw.line((RAIL_X, rail_top, RAIL_X, rail_bottom), fill=CYAN, width=9)
    draw.line((RAIL_X, centres[-2][0], RAIL_X, rail_bottom), fill=GREY, width=9)
    for centre, stage in centres:
        colour = {"core": CYAN, "pivot": YELLOW, "extra": GREY}[stage["kind"]]
        radius = 54 if stage["kind"] == "pivot" else 46
        draw.ellipse((RAIL_X - radius, centre - radius, RAIL_X + radius, centre + radius),
                     fill=BG, outline=colour, width=8)
        label = stage["n"]
        draw.text((RAIL_X, centre), label, font=ctx.f.rail, fill=colour, anchor="mm")
        arrow_right(draw, RAIL_X + radius + 8, centre, CARD_X0 - 6, colour, 6, 20)
    draw.text((MARGIN + 10, y + 46), S.FOOTER, font=ctx.f.note, fill=DIM)
    image.save(MASTER, dpi=(DPI, DPI))
    return image


def build_poster(image):
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
    width_pt = 39.37 * 72
    height_pt = width_pt * image.height / image.width
    if height_pt > 190 * 72:
        height_pt = 190 * 72
        width_pt = height_pt * image.width / image.height
    pdf = canvas.Canvas(str(POSTER), pagesize=(width_pt, height_pt))
    pdf.drawImage(ImageReader(str(MASTER)), 0, 0, width_pt, height_pt)
    pdf.setTitle("Notions of God — Continuous At-a-Glance Carvaka-standard g9")
    pdf.showPage()
    pdf.save()


def build_tiled(image):
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas
    page_w, page_h = 1190.55, 841.89
    margin, footer = 18, 26
    area_w, area_h = page_w - 2 * margin, page_h - 2 * margin - footer
    tile_h = int(round(image.width * area_h / area_w))
    min_overlap = 300
    count = max(1, math.ceil((image.height - min_overlap) / (tile_h - min_overlap)))
    step = (image.height - tile_h) / (count - 1) if count > 1 else 0
    overlap = int(round(tile_h - step)) if count > 1 else 0
    pdf = canvas.Canvas(str(TILED), pagesize=(page_w, page_h))
    crops = []
    previews = []
    for i in range(count):
        top = int(round(i * step))
        bottom = min(top + tile_h, image.height)
        top = max(0, bottom - tile_h)
        crop = image.crop((0, top, image.width, bottom))
        buffer = io.BytesIO()
        crop.save(buffer, format="PNG")
        buffer.seek(0)
        pdf.drawImage(ImageReader(buffer), margin, margin + footer, area_w, area_h)
        pdf.setFont("Helvetica", 8)
        pdf.drawString(margin, margin + 8, f"Notions of God continuous flow — tile {i + 1}/{count} — master rows {top}–{bottom}")
        pdf.showPage()
        preview = crop.copy()
        preview.thumbnail((1800, 1300))
        path = PREVIEWS / f"page-{i + 1:02d}.png"
        preview.save(path)
        previews.append(path)
        crops.append({"tile": i + 1, "box": [0, top, image.width, bottom]})
    pdf.save()

    per_sheet = 6
    sheets = []
    for start in range(0, len(previews), per_sheet):
        batch = previews[start:start + per_sheet]
        thumbs = [Image.open(path).convert("RGB") for path in batch]
        cell_w = max(im.width for im in thumbs)
        cell_h = max(im.height for im in thumbs)
        cols = min(2, len(thumbs))
        rows = math.ceil(len(thumbs) / cols)
        sheet = Image.new("RGB", (cols * cell_w + (cols + 1) * 22, rows * cell_h + (rows + 1) * 22), BG)
        for j, thumb in enumerate(thumbs):
            x = 22 + (j % cols) * (cell_w + 22)
            y = 22 + (j // cols) * (cell_h + 22)
            sheet.paste(thumb, (x, y))
        sheet_path = PREVIEWS / f"contact-sheet-{start // per_sheet + 1:02d}.png"
        sheet.save(sheet_path)
        sheets.append(sheet_path.name)

    spec = {
        "approved": False,
        "generation": "continuous-at-a-glance-carvaka-standard-g9",
        "generated": DATESTAMP,
        "canvas": {"width_px": image.width, "height_px": image.height, "dpi": DPI},
        "sources": {"canonical": S.OWNER, "pyq": S.PYQ_OWNER, "learning_session": S.SESSION_OWNER},
        "stage_order": [stage["n"] for stage in S.STAGES],
        "layout_signatures": {stage["n"]: [block["type"] for block in stage["blocks"]] for stage in S.STAGES},
        "outputs": {
            "master_png": MASTER.name, "poster_pdf": POSTER.name, "tiled_pdf": TILED.name,
            "tile_count": count, "tile_height_px": tile_h, "tile_overlap_px": overlap,
            "tile_crops": crops, "contact_sheets": sheets,
        },
        "overflow_events": R.OVERFLOWS,
    }
    (HERE / "design-spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")


def write_readme(image):
    (HERE / "README.txt").write_text(
        "NOTIONS OF GOD — CONTINUOUS AT-A-GLANCE — CARVAKA-STANDARD g9\n"
        "================================================================\n\n"
        "Status: NOT APPROVED. Generated for explicit user review.\n\n"
        "Read the numbered cyan rail from Stage 0 through Stage 14. The complete Basic / Must-Know "
        "spine precedes the lighter EXTRA enrichment stage. The master PNG is 4800 px wide at "
        f"300 dpi metadata and {image.height} px high. The poster preserves the whole master on one "
        "page; the A3 tiled PDF is cropped from that exact master with overlap.\n\n"
        "Rebuild:\n  python build_flowchart.py\n  python validate_flowchart.py\n\n"
        "Source files:\n  spec_content.py — hand-authored doctrine/stage content\n"
        "  render_lib.py — deterministic measured rendering primitives\n"
        "  build_flowchart.py — master/poster/tile/preview builder\n"
        "  validate_flowchart.py — completeness, geometry and same-master checks\n",
        encoding="utf-8",
    )


def main():
    image = build_master()
    build_poster(image)
    build_tiled(image)
    write_readme(image)
    print(MASTER)
    print(POSTER)
    print(TILED)


if __name__ == "__main__":
    main()
