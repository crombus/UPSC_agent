"""Build the self-contained Notions of God continuous at-a-glance g6 package."""
from __future__ import annotations

import hashlib
import io
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))

import content_spec as S  # noqa: E402
import render_lib as R  # noqa: E402

Image.MAX_IMAGE_PIXELS = None

W = 4800
DPI = 300
MARGIN = 110
RAIL_X = 250
CARD_X0 = 520
CARD_X1 = 4690
CARD_W = CARD_X1 - CARD_X0
PAD = 44
INNER_X = CARD_X0 + PAD
INNER_W = CARD_W - 2 * PAD
STAGE_GAP = 58
TOP = 42

MASTER = HERE / "Notions-of-God_Continuous-At-a-Glance_g6_Master.png"
POSTER = HERE / (
    "Notions-of-God_Continuous-At-a-Glance_g6_Poster_2026-08-22.pdf"
)
TILED = HERE / (
    "Notions-of-God_Continuous-At-a-Glance_g6_Tiled_2026-08-22.pdf"
)
PREVIEWS = HERE / "previews"
DESIGN_SPEC = HERE / "design-spec.json"
BUILD_AUDIT = HERE / "build-audit.json"
HASH_BEFORE = HERE / "preservation-hashes-before.json"
HASH_AFTER = HERE / "preservation-hashes-after.json"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def collect_preservation():
    groups = {}
    src = {}
    for rel in S.SOURCES:
        p = ROOT / rel
        src[rel] = {
            "sha256": sha256(p),
            "bytes": p.stat().st_size,
        }
    groups["canonical_sources"] = src
    for group, rel in S.REFERENCE_FOLDERS:
        base = ROOT / rel
        items = {}
        for p in sorted(base.rglob("*")):
            if p.is_file():
                key = str(p.relative_to(ROOT))
                items[key] = {
                    "sha256": sha256(p),
                    "bytes": p.stat().st_size,
                }
        groups[group] = items
    return groups


def write_before_manifest():
    current = collect_preservation()
    if not HASH_BEFORE.exists():
        HASH_BEFORE.write_text(
            json.dumps(
                {
                    "generation": S.GENERATION,
                    "snapshot": "before g6 artifact build",
                    "root": str(ROOT),
                    "groups": current,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return json.loads(HASH_BEFORE.read_text(encoding="utf-8"))["groups"]


def write_after_manifest(before):
    after = collect_preservation()
    mismatches = []
    for group, items in before.items():
        now = after.get(group, {})
        for path, meta in items.items():
            if path not in now:
                mismatches.append({"path": path, "status": "missing_after"})
            elif now[path]["sha256"] != meta["sha256"]:
                mismatches.append(
                    {
                        "path": path,
                        "status": "hash_changed",
                        "before": meta["sha256"],
                        "after": now[path]["sha256"],
                    }
                )
        for path in now:
            if path not in items:
                mismatches.append({"path": path, "status": "new_in_reference"})
    payload = {
        "generation": S.GENERATION,
        "snapshot": "after g6 artifact build",
        "root": str(ROOT),
        "groups": after,
        "matches_before": not mismatches,
        "mismatches": mismatches,
    }
    HASH_AFTER.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return after, mismatches


def stage_header_height(stage):
    title_font = R.F.stage
    available = INNER_W - 210
    if R.text_w(title_font, stage["title"]) > available * 1.7:
        title_font = R.F.stage_small
    title_h = R.measure_text(stage["title"], title_font, available, 4, "stage-title")
    pills_h = len(R.pill_rows(stage["pills"], INNER_W)) * (
        R.line_h(R.F.pill, 0) + 24
    )
    return max(68, title_h) + pills_h + 44, title_font


def draw_header(draw, y):
    x0, x1 = MARGIN, W - MARGIN
    h = 560
    R.rounded(draw, (x0, y, x1, y + h), 28, fill=R.HEADER, outline=R.CYAN, width=4)
    x = x0 + 42
    cy = y + 34
    cy = R.draw_text(
        draw,
        (x, cy),
        S.HEADER["title"],
        R.F.title,
        R.WHITE,
        x1 - x0 - 84,
        5,
        "header-title",
        y + h,
    )
    cy += 8
    cy = R.draw_text(
        draw,
        (x, cy),
        S.HEADER["subtitle"],
        R.F.subtitle,
        R.CYAN,
        x1 - x0 - 84,
        5,
        "header-subtitle",
        y + h,
    )
    cy += 14
    cy = R.draw_text(
        draw,
        (x, cy),
        S.HEADER["note"],
        R.F.note,
        R.DIM,
        x1 - x0 - 84,
        5,
        "header-note",
        y + h,
    )
    cy += 22
    legend_w = x1 - x0 - 84
    cx = x
    row_y = cy
    for cname, label in S.HEADER["legend"]:
        c = {
            "CYAN": R.CYAN,
            "AMBER": R.AMBER,
            "TEAL": R.TEAL,
            "RED": R.RED,
            "MAGENTA": R.MAGENTA,
        }[cname]
        text = f"{cname}: {label}"
        pw = R.text_w(R.F.small_bold, text) + 48
        if cx + pw > x + legend_w:
            cx = x
            row_y += 58
        R.rounded(
            draw,
            (cx, row_y, cx + pw, row_y + 48),
            24,
            fill=None,
            outline=c,
            width=3,
        )
        draw.ellipse((cx + 14, row_y + 15, cx + 32, row_y + 33), fill=c)
        draw.text((cx + 40, row_y + 8), text, font=R.F.small_bold, fill=c)
        cx += pw + 14
    cy = row_y + 68
    source_text = (
        "CANONICAL OWNERS: Notions-of-God.md + Uncompressed Complete Learning Session "
        "+ Solved Practice Workbook (all dated/identified in design-spec.json)"
    )
    R.band(
        draw,
        (x, cy, x1 - 42, cy + 72),
        "SOURCE CONTROL",
        source_text,
        R.TEAL,
        (8, 38, 48),
        R.F.small,
        "source-control",
    )
    cy += 88
    approval = S.HEADER["approval"]
    draw.text((x, cy), approval, font=R.F.note, fill=R.YELLOW)
    draw.text(
        (x1 - 42 - R.text_w(R.F.note, "CORE FIRST | PYQ ENRICHMENT LAST"), cy),
        "CORE FIRST | PYQ ENRICHMENT LAST",
        font=R.F.note,
        fill=R.DIM,
    )
    R.record_box("header", (x0, y, x1, y + h), "HEADER")
    return h


def draw_stage_shell(draw, stage, y, next_title):
    h = stage["height"]
    x0, x1 = CARD_X0, CARD_X1
    R.rounded(draw, (x0, y, x1, y + h), 25, fill=R.CARD, outline=R.CYAN, width=4)
    sh, title_font = stage_header_height(stage)
    x = x0 + PAD
    cy = y + 24
    badge = f"STAGE {stage['n']}"
    bh = 48
    bw = R.text_w(R.F.badge, badge) + 36
    R.rounded(draw, (x, cy, x + bw, cy + bh), bh // 2, fill=R.CYAN)
    draw.text((x + 18, cy + 7), badge, font=R.F.badge, fill=R.BG)
    title_y = cy - 2
    R.draw_text(
        draw,
        (x + bw + 24, title_y),
        stage["title"],
        title_font,
        R.WHITE,
        INNER_W - bw - 24,
        4,
        f"stage-{stage['n']}-title",
        y + sh,
    )
    cy = y + max(72, R.measure_text(stage["title"], title_font, INNER_W - bw - 24, 4)) + 34
    cy = R.draw_pills(draw, x, cy, INNER_W, stage["pills"])

    trap_y = y + h - 330
    answer_y = y + h - 214
    bridge_y = y + h - 98
    body_bottom = trap_y - 18
    R.trap_band(
        draw,
        (x, trap_y, x + INNER_W, trap_y + 98),
        stage["trap"],
        f"stage-{stage['n']}-trap",
    )
    R.answer_band(
        draw,
        (x, answer_y, x + INNER_W, answer_y + 98),
        stage["answer"],
        f"stage-{stage['n']}-answer",
    )
    bridge_text = (
        f"NEXT -> {next_title}"
        if next_title
        else "END OF MASTER -> Use Stage 10 to route the exact printed demand."
    )
    R.bridge_band(
        draw,
        (x, bridge_y, x + INNER_W, bridge_y + 72),
        bridge_text,
        f"stage-{stage['n']}-bridge",
    )
    R.record_box(f"stage-{stage['n']}", (x0, y, x1, y + h), stage["n"])
    return cy + 6, body_bottom


def draw_axis_arrow(draw, x0, x1, y, left, middle, right, caption):
    R.arrow(draw, (x0 + 110, y + 58), (x1 - 110, y + 58), R.CYAN, 5, 18)
    draw.text((x0 + 12, y + 5), left, font=R.F.small_bold, fill=R.AMBER)
    draw.text(
        (x1 - 12 - R.text_w(R.F.small_bold, right), y + 5),
        right,
        font=R.F.small_bold,
        fill=R.TEAL,
    )
    draw.text(
        ((x0 + x1 - R.text_w(R.F.small_bold, middle)) / 2, y + 5),
        middle,
        font=R.F.small_bold,
        fill=R.YELLOW,
    )
    R.draw_text(
        draw,
        (x0 + 12, y + 84),
        caption,
        R.F.small,
        R.DIM,
        x1 - x0 - 24,
        3,
        "spectrum",
    )


def draw_stage_01(draw, st, top, bottom):
    left_w = 2460
    gap = 26
    right_w = INNER_W - left_w - gap
    qx0, qy0 = INNER_X, top
    qx1, qy1 = qx0 + left_w, top + 770
    R.rounded(draw, (qx0, qy0, qx1, qy1), 18, fill=R.CARD_ALT, outline=R.RULE)
    cx, cy = (qx0 + qx1) / 2, (qy0 + qy1) / 2
    draw.line((cx, qy0 + 70, cx, qy1 - 34), fill=R.CYAN, width=5)
    draw.line((qx0 + 38, cy, qx1 - 38, cy), fill=R.CYAN, width=5)
    draw.text(
        (qx0 + 28, qy0 + 18),
        "2 x 2 AXES - ANALYTICAL PLACEMENTS, NOT COMPLETE DEFINITIONS",
        font=R.F.h2,
        fill=R.CYAN,
    )
    labels = [
        (qx0 + 40, qy0 + 80, st["quadrants"][0], R.AMBER),
        (cx + 30, qy0 + 80, st["quadrants"][1], R.TEAL),
        (qx0 + 40, cy + 24, st["quadrants"][2], R.MAGENTA),
        (cx + 30, cy + 24, st["quadrants"][3], R.YELLOW),
    ]
    qw = left_w / 2 - 76
    for x, y, item, c in labels:
        draw.text((x, y), item["title"], font=R.F.h2, fill=c)
        draw.text((x, y + 46), item["model"], font=R.F.small_bold, fill=R.WHITE)
        R.draw_text(
            draw,
            (x, y + 86),
            item["text"],
            R.F.body,
            R.WHITE,
            qw,
            5,
            "stage01-quadrant",
            qy1 - 28,
        )
    rx0 = qx1 + gap
    rx1 = INNER_X + INNER_W
    R.rounded(draw, (rx0, top, rx1, top + 770), 18, fill=R.DEEP, outline=R.RULE)
    draw.text((rx0 + 22, top + 18), "TWO SPECTRA", font=R.F.h1, fill=R.AMBER)
    draw_axis_arrow(
        draw,
        rx0 + 18,
        rx1 - 18,
        top + 88,
        **st["spectra"][0],
    )
    draw_axis_arrow(
        draw,
        rx0 + 18,
        rx1 - 18,
        top + 270,
        **st["spectra"][1],
    )
    rules = [
        "Personal: intellect, will and purposive relation - never a finite human body.",
        "Impersonal: not a deliberating person - never inert matter by definition.",
        "Transcendence: ontological independence - never spatial distance.",
        "Immanence: presence, sustaining or indwelling - never automatic identity.",
    ]
    draw.text((rx0 + 22, top + 464), "CLOSE-OPTION REPAIR", font=R.F.h2, fill=R.RED)
    R.draw_bullets(
        draw,
        rx0 + 22,
        top + 510,
        right_w - 44,
        rules,
        R.RED,
        R.F.small,
        6,
        "stage01-rules",
        top + 744,
    )
    lc_y = top + 796
    w = (INNER_W - 2 * gap) / 3
    for i, item in enumerate(st["language_control"]):
        x0 = INNER_X + i * (w + gap)
        x1 = x0 + w
        c = [R.AMBER, R.TEAL, R.YELLOW][i]
        px, py, pw = R.panel(
            draw,
            (x0, lc_y, x1, body_bottom := bottom),
            item["title"],
            c,
            R.CARD_ALT,
            c,
        )
        R.draw_text(
            draw,
            (px, py),
            item["text"],
            R.F.body,
            R.WHITE,
            pw,
            5,
            "stage01-language",
            body_bottom - 18,
        )


def draw_model_symbol(draw, box, kind):
    x0, y0, x1, y1 = box
    cx = (x0 + x1) / 2
    top = y0 + 8
    bot = y1 - 8
    if kind == "distinct":
        draw.ellipse((cx - 32, top, cx + 32, top + 64), outline=R.AMBER, width=5)
        draw.rectangle((cx - 80, bot - 48, cx + 80, bot), outline=R.TEAL, width=5)
        R.arrow(draw, (cx, top + 68), (cx, bot - 52), R.CYAN, 4, 14)
    elif kind == "withdrawn":
        draw.ellipse((x0 + 25, top, x0 + 89, top + 64), outline=R.AMBER, width=5)
        draw.rectangle((x1 - 180, bot - 48, x1 - 20, bot), outline=R.TEAL, width=5)
        draw.line((x0 + 96, top + 32, x1 - 190, bot - 24), fill=R.GREY, width=4)
        draw.line((cx - 8, (top + bot) / 2 - 12, cx + 8, (top + bot) / 2 + 12), fill=R.RED, width=5)
        draw.line((cx - 8, (top + bot) / 2 + 12, cx + 8, (top + bot) / 2 - 12), fill=R.RED, width=5)
    elif kind == "identity":
        R.rounded(draw, (cx - 115, top, cx + 115, bot), 26, fill=None, outline=R.MAGENTA, width=5)
        draw.text((cx - 73, top + 16), "GOD", font=R.F.small_bold, fill=R.MAGENTA)
        draw.text((cx - 92, bot - 42), "WORLD", font=R.F.small_bold, fill=R.TEAL)
    elif kind == "inclusion":
        R.rounded(draw, (cx - 130, top, cx + 130, bot), 28, fill=None, outline=R.AMBER, width=5)
        R.rounded(draw, (cx - 78, top + 44, cx + 78, bot - 28), 20, fill=None, outline=R.TEAL, width=5)
        draw.text((cx - 38, top + 8), "GOD", font=R.F.small_bold, fill=R.AMBER)
        draw.text((cx - 54, top + 72), "WORLD", font=R.F.tiny_bold, fill=R.TEAL)
    else:
        draw.ellipse((cx - 115, top, cx + 15, bot), outline=R.AMBER, width=5)
        draw.ellipse((cx - 15, top, cx + 115, bot), outline=R.TEAL, width=5)
        draw.text((cx - 94, top + 18), "POSS.", font=R.F.tiny_bold, fill=R.AMBER)
        draw.text((cx + 20, top + 18), "WORLD", font=R.F.tiny_bold, fill=R.TEAL)


def draw_stage_02(draw, st, top, bottom):
    gap = 18
    box_w = (INNER_W - 4 * gap) / 5
    box_h = 920
    for i, model in enumerate(st["models"]):
        x0 = INNER_X + i * (box_w + gap)
        x1 = x0 + box_w
        R.rounded(
            draw,
            (x0, top, x1, top + box_h),
            18,
            fill=R.CARD_ALT if i % 2 == 0 else R.DEEP,
            outline=[R.CYAN, R.AMBER, R.MAGENTA, R.TEAL, R.YELLOW][i],
            width=3,
        )
        c = [R.CYAN, R.AMBER, R.MAGENTA, R.TEAL, R.YELLOW][i]
        R.draw_text(
            draw,
            (x0 + 18, top + 16),
            model["name"],
            R.F.h2,
            c,
            box_w - 36,
            3,
            "stage02-name",
            top + 92,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 18, top + 82),
            model["formula"],
            R.F.small_bold,
            R.WHITE,
            box_w - 36,
            3,
            "stage02-formula",
            top + 145,
            "center",
        )
        draw_model_symbol(draw, (x0 + 180, top + 150, x1 - 180, top + 288), model["diagram"])
        cy = top + 312
        for label, text, tc in [
            ("WORLD", model["world"], R.TEAL),
            ("HUMAN", model["human"], R.CYAN),
            ("STRENGTH", model["strength"], R.GREEN),
            ("PRESSURE", model["pressure"], R.RED),
        ]:
            draw.text((x0 + 18, cy), label, font=R.F.tiny_bold, fill=tc)
            cy += 30
            cy = R.draw_text(
                draw,
                (x0 + 18, cy),
                text,
                R.F.tiny,
                R.WHITE,
                box_w - 36,
                3,
                f"stage02-{label}",
                top + box_h - 14,
            )
            cy += 8
    terms_y = top + box_h + 26
    cell_w = (INNER_W - 4 * gap) / 5
    draw.text(
        (INNER_X, terms_y),
        "DECISIVE RELATION TERMS",
        font=R.F.h2,
        fill=R.AMBER,
    )
    terms_y += 48
    for i, term in enumerate(st["relation_terms"]):
        x0 = INNER_X + i * (cell_w + gap)
        R.rounded(
            draw,
            (x0, terms_y, x0 + cell_w, terms_y + 90),
            14,
            fill=(9, 42, 55),
            outline=R.CYAN,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 12, terms_y + 17),
            term,
            R.F.small_bold,
            R.WHITE,
            cell_w - 24,
            3,
            "stage02-relations",
            terms_y + 82,
            "center",
        )
    compare_y = terms_y + 110
    R.band(
        draw,
        (INNER_X, compare_y, INNER_X + INNER_W, bottom),
        "COMPARISON RULE",
        "Always state: definition -> exact God-world formula -> relation to persons -> religious function -> strongest pressure.",
        R.YELLOW,
        R.CARD_ALT,
        R.F.body_bold,
        "stage02-compare",
    )


def draw_stage_03(draw, st, top, bottom):
    wheel_h = 630
    center_x = INNER_X + INNER_W / 2
    center_y = top + wheel_h / 2
    positions = [
        (INNER_X, top + 18),
        (INNER_X + 1040, top),
        (INNER_X + 2080, top),
        (INNER_X + 3120, top + 18),
        (INNER_X + 420, top + 350),
        (INNER_X + 1680, top + 365),
        (INNER_X + 2940, top + 350),
    ]
    node_w = 900
    node_h = 225
    draw.ellipse(
        (center_x - 205, center_y - 95, center_x + 205, center_y + 95),
        fill=(16, 52, 69),
        outline=R.CYAN,
        width=6,
    )
    R.draw_text(
        draw,
        (center_x - 175, center_y - 47),
        "PERFECT-BEING PACKAGE",
        R.F.h2,
        R.WHITE,
        350,
        3,
        "stage03-center",
        center_y + 65,
        "center",
    )
    for (x, y), item, c in zip(
        positions,
        st["attributes"],
        [R.AMBER, R.CYAN, R.TEAL, R.GREEN, R.YELLOW, R.MAGENTA, R.RED],
    ):
        nx = x
        if nx + node_w > INNER_X + INNER_W:
            nx = INNER_X + INNER_W - node_w
        R.rounded(
            draw,
            (nx, y, nx + node_w, y + node_h),
            18,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        R.arrow(
            draw,
            (center_x, center_y),
            (nx + node_w / 2, y + node_h / 2),
            R.RULE,
            3,
            12,
        )
        draw.text((nx + 18, y + 14), item["name"], font=R.F.h2, fill=c)
        R.draw_text(
            draw,
            (nx + 18, y + 58),
            item["text"],
            R.F.small,
            R.WHITE,
            node_w - 36,
            4,
            "stage03-attribute",
            y + node_h - 12,
        )
    matrix_y = top + wheel_h + 26
    matrix_end = R.matrix(
        draw,
        INNER_X,
        matrix_y,
        INNER_W,
        ["TENSION", "PHILOSOPHICAL PROBLEM", "STRONGEST REPLY", "RESIDUAL / TRAP"],
        st["coherence_rows"],
        [0.16, 0.27, 0.34, 0.23],
        R.F.tiny,
        R.F.tiny_bold,
        9,
        "stage03-matrix",
    )
    logic_y = matrix_end + 16
    col_w = (INNER_W - 20) / 4
    for i, line in enumerate(st["freedom_logic"]):
        x0 = INNER_X + i * (col_w + (20 / 3 if i else 0))
        if i:
            x0 = INNER_X + i * (col_w + 20 / 3)
        R.rounded(
            draw,
            (x0, logic_y, x0 + col_w, bottom),
            14,
            fill=R.DEEP,
            outline=R.YELLOW if i < 3 else R.RED,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 14, logic_y + 14),
            line,
            R.F.small,
            R.WHITE,
            col_w - 28,
            3,
            "stage03-logic",
            bottom - 10,
        )


def draw_stage_04(draw, st, top, bottom):
    tree = st["tree"]
    root_w = 1950
    root_x = INNER_X + (INNER_W - root_w) / 2
    R.rounded(
        draw,
        (root_x, top, root_x + root_w, top + 170),
        24,
        fill=(24, 48, 70),
        outline=R.MAGENTA,
        width=5,
    )
    R.draw_text(
        draw,
        (root_x + 20, top + 18),
        tree["root"],
        R.F.h1,
        R.WHITE,
        root_w - 40,
        4,
        "stage04-root",
        top + 88,
        "center",
    )
    R.draw_text(
        draw,
        (root_x + 24, top + 100),
        tree["root_note"],
        R.F.small,
        R.DIM,
        root_w - 48,
        3,
        "stage04-root-note",
        top + 158,
        "center",
    )
    attr_y = top + 250
    gap = 120
    box_w = (INNER_W - gap) / 2
    for i, (name, text, mode) in enumerate(tree["attributes"]):
        x0 = INNER_X + i * (box_w + gap)
        R.arrow(draw, (root_x + root_w / 2, top + 174), (x0 + box_w / 2, attr_y - 8), R.CYAN, 5, 18)
        R.rounded(
            draw,
            (x0, attr_y, x0 + box_w, attr_y + 370),
            20,
            fill=R.CARD_ALT,
            outline=R.CYAN if i == 0 else R.TEAL,
            width=4,
        )
        draw.text((x0 + 24, attr_y + 20), name, font=R.F.h1, fill=R.CYAN if i == 0 else R.TEAL)
        R.draw_text(
            draw,
            (x0 + 24, attr_y + 76),
            text,
            R.F.body,
            R.WHITE,
            box_w - 48,
            5,
            "stage04-attribute",
            attr_y + 235,
        )
        R.rounded(
            draw,
            (x0 + 24, attr_y + 255, x0 + box_w - 24, attr_y + 342),
            14,
            fill=(10, 52, 62),
            outline=R.YELLOW,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 38, attr_y + 276),
            mode,
            R.F.small_bold,
            R.WHITE,
            box_w - 76,
            3,
            "stage04-mode",
            attr_y + 332,
            "center",
        )
    qual_y = attr_y + 390
    R.band(
        draw,
        (INNER_X, qual_y, INNER_X + INNER_W, qual_y + 112),
        "SUBSTANCE TREE RULE",
        tree["qualification"],
        R.YELLOW,
        R.DEEP,
        R.F.small,
        "stage04-qualification",
    )
    natura_y = qual_y + 132
    gap2 = 30
    nw = (INNER_W - 2 * gap2) / 3
    for i, item in enumerate(st["natura"]):
        x0 = INNER_X + i * (nw + gap2)
        c = [R.AMBER, R.CYAN, R.TEAL][i]
        R.rounded(
            draw,
            (x0, natura_y, x0 + nw, natura_y + 235),
            18,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 18, natura_y + 16),
            item["name"],
            R.F.h2,
            c,
            nw - 36,
            3,
            "stage04-natura-name",
            natura_y + 68,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 18, natura_y + 82),
            item["text"],
            R.F.small,
            R.WHITE,
            nw - 36,
            4,
            "stage04-natura",
            natura_y + 222,
        )
        if i < 2:
            R.arrow(
                draw,
                (x0 + nw + 5, natura_y + 118),
                (x0 + nw + gap2 - 5, natura_y + 118),
                R.CYAN,
                4,
                13,
            )
    dia_y = natura_y + 255
    dw = (INNER_W - 2 * gap2) / 3
    for i, row in enumerate(st["dialectic"]):
        x0 = INNER_X + i * (dw + gap2)
        R.rounded(
            draw,
            (x0, dia_y, x0 + dw, bottom),
            16,
            fill=(44, 29, 40),
            outline=R.RED,
            width=2,
        )
        cy = dia_y + 14
        for j, text in enumerate(row):
            c = [R.RED, R.TEAL, R.YELLOW][j]
            cy = R.draw_text(
                draw,
                (x0 + 16, cy),
                text,
                R.F.tiny_bold if j != 1 else R.F.tiny,
                c if j != 1 else R.WHITE,
                dw - 32,
                3,
                "stage04-dialectic",
                bottom - 8,
            )
            cy += 6


def draw_stage_05(draw, st, top, bottom):
    gap = 30
    sw = (INNER_W - gap) / 2
    top_h = 570
    for i, item in enumerate(st["standpoints"]):
        x0 = INNER_X + i * (sw + gap)
        c = R.AMBER if i == 0 else R.TEAL
        R.rounded(
            draw,
            (x0, top, x0 + sw, top + top_h),
            22,
            fill=R.CARD_ALT,
            outline=c,
            width=4,
        )
        R.draw_text(
            draw,
            (x0 + 22, top + 18),
            item["level"],
            R.F.h2,
            c,
            sw - 44,
            3,
            "stage05-level",
            top + 70,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 22, top + 83),
            item["name"],
            R.F.h1,
            R.WHITE,
            sw - 44,
            3,
            "stage05-name",
            top + 135,
            "center",
        )
        R.draw_bullets(
            draw,
            x0 + 24,
            top + 160,
            sw - 48,
            item["items"],
            c,
            R.F.body,
            8,
            "stage05-items",
            top + top_h - 18,
        )
    R.band(
        draw,
        (INNER_X + sw - 460, top + top_h - 54, INNER_X + sw + gap + 460, top + top_h + 34),
        "ONE REALITY",
        "Same Brahman under two epistemic standpoints - not two independent Brahmans.",
        R.CYAN,
        (10, 43, 57),
        R.F.tiny_bold,
        "stage05-one",
    )
    mid_y = top + top_h + 62
    left_w = 1500
    right_x = INNER_X + left_w + gap
    right_w = INNER_W - left_w - gap
    R.rounded(
        draw,
        (INNER_X, mid_y, INNER_X + left_w, mid_y + 485),
        18,
        fill=R.DEEP,
        outline=R.AMBER,
        width=3,
    )
    draw.text((INNER_X + 22, mid_y + 18), "THREE LEVELS OF REALITY", font=R.F.h1, fill=R.AMBER)
    cy = mid_y + 82
    for i, (name, text) in enumerate(st["levels"]):
        c = [R.AMBER, R.CYAN, R.MAGENTA][i]
        R.rounded(
            draw,
            (INNER_X + 40 + i * 75, cy, INNER_X + left_w - 40, cy + 105),
            14,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        draw.text((INNER_X + 58 + i * 75, cy + 13), name, font=R.F.small_bold, fill=c)
        R.draw_text(
            draw,
            (INNER_X + 58 + i * 75, cy + 48),
            text,
            R.F.small,
            R.WHITE,
            left_w - 135 - i * 75,
            3,
            "stage05-levels",
            cy + 98,
        )
        cy += 120
    R.rounded(
        draw,
        (right_x, mid_y, right_x + right_w, mid_y + 485),
        18,
        fill=R.DEEP,
        outline=R.TEAL,
        width=3,
    )
    draw.text((right_x + 22, mid_y + 18), "MAYA / ADHYASA / VIVARTA FLOW", font=R.F.h1, fill=R.TEAL)
    cy = mid_y + 90
    for i, text in enumerate(st["vivarta"]):
        c = R.YELLOW if i in (0, 2) else R.GREEN
        R.rounded(
            draw,
            (right_x + 26, cy, right_x + right_w - 26, cy + 78),
            13,
            fill=R.CARD_ALT,
            outline=c,
            width=2,
        )
        R.draw_text(
            draw,
            (right_x + 40, cy + 17),
            text,
            R.F.small_bold,
            R.WHITE,
            right_w - 80,
            3,
            "stage05-vivarta",
            cy + 70,
            "center",
        )
        cy += 91
    precision_y = mid_y + 510
    R.band(
        draw,
        (INNER_X, precision_y, INNER_X + INNER_W, precision_y + 130),
        "TECHNICAL CORRECTION",
        st["precision"],
        R.RED,
        (47, 28, 39),
        R.F.small_bold,
        "stage05-precision",
    )
    dia_y = precision_y + 150
    dw = (INNER_W - 2 * gap) / 3
    for i, text in enumerate(st["dialectic"]):
        x0 = INNER_X + i * (dw + gap)
        c = [R.RED, R.TEAL, R.YELLOW][i]
        R.rounded(
            draw,
            (x0, dia_y, x0 + dw, bottom),
            16,
            fill=R.CARD_ALT,
            outline=c,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 18, dia_y + 18),
            text,
            R.F.small,
            R.WHITE,
            dw - 36,
            4,
            "stage05-dialectic",
            bottom - 10,
        )


def draw_stage_06(draw, st, top, bottom):
    nested_w = 2390
    right_x = INNER_X + nested_w + 30
    right_w = INNER_W - nested_w - 30
    R.rounded(
        draw,
        (INNER_X, top, INNER_X + nested_w, top + 800),
        24,
        fill=(11, 41, 58),
        outline=R.AMBER,
        width=5,
    )
    R.draw_text(
        draw,
        (INNER_X + 26, top + 18),
        st["nested"]["outer"],
        R.F.h1,
        R.AMBER,
        nested_w - 52,
        4,
        "stage06-outer",
        top + 80,
        "center",
    )
    R.rounded(
        draw,
        (INNER_X + 150, top + 102, INNER_X + nested_w - 150, top + 720),
        24,
        fill=R.CARD_ALT,
        outline=R.CYAN,
        width=4,
    )
    R.draw_text(
        draw,
        (INNER_X + 180, top + 124),
        st["nested"]["inner"],
        R.F.h2,
        R.CYAN,
        nested_w - 360,
        4,
        "stage06-inner",
        top + 186,
        "center",
    )
    body_gap = 26
    bw = (nested_w - 420 - body_gap) / 2
    for i, (name, text) in enumerate(st["nested"]["body"]):
        x0 = INNER_X + 190 + i * (bw + body_gap)
        c = R.TEAL if i == 0 else R.YELLOW
        R.rounded(
            draw,
            (x0, top + 220, x0 + bw, top + 500),
            18,
            fill=R.DEEP,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 18, top + 238),
            name,
            R.F.h2,
            c,
            bw - 36,
            3,
            "stage06-body-name",
            top + 300,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 18, top + 320),
            text,
            R.F.body,
            R.WHITE,
            bw - 36,
            5,
            "stage06-body",
            top + 480,
        )
    R.band(
        draw,
        (INNER_X + 185, top + 535, INNER_X + nested_w - 185, top + 695),
        "SARIRA-SARIRI",
        st["nested"]["definition"],
        R.MAGENTA,
        (42, 34, 54),
        R.F.small,
        "stage06-definition",
    )
    R.rounded(
        draw,
        (right_x, top, right_x + right_w, top + 800),
        22,
        fill=R.CARD_ALT,
        outline=R.TEAL,
        width=4,
    )
    draw.text((right_x + 22, top + 18), "CAUSE CYCLE", font=R.F.h1, fill=R.TEAL)
    cy = top + 86
    for i, (name, note) in enumerate(st["cause_cycle"]):
        c = [R.AMBER, R.CYAN, R.TEAL, R.MAGENTA][i]
        R.rounded(
            draw,
            (right_x + 36, cy, right_x + right_w - 36, cy + 120),
            15,
            fill=R.DEEP,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (right_x + 52, cy + 12),
            name,
            R.F.small_bold,
            c,
            right_w - 104,
            3,
            "stage06-cycle-name",
            cy + 52,
            "center",
        )
        R.draw_text(
            draw,
            (right_x + 52, cy + 57),
            note,
            R.F.small,
            R.WHITE,
            right_w - 104,
            3,
            "stage06-cycle-note",
            cy + 108,
            "center",
        )
        if i < len(st["cause_cycle"]) - 1:
            R.arrow(
                draw,
                (right_x + right_w / 2, cy + 122),
                (right_x + right_w / 2, cy + 143),
                R.CYAN,
                4,
                11,
            )
        cy += 145
    notes_y = top + 810
    col_gap = 30
    col_w = (INNER_W - col_gap) / 2
    R.rounded(
        draw,
        (INNER_X, notes_y, INNER_X + col_w, notes_y + 520),
        18,
        fill=R.DEEP,
        outline=R.YELLOW,
        width=3,
    )
    draw.text((INNER_X + 22, notes_y + 16), "APRTHAK-SIDDHI + CAUSATION", font=R.F.h1, fill=R.YELLOW)
    cy = notes_y + 80
    for text in st["inseparability"]:
        R.rounded(
            draw,
            (INNER_X + 28, cy, INNER_X + col_w - 28, cy + 60),
            12,
            fill=R.CARD_ALT,
            outline=R.CYAN,
            width=2,
        )
        R.draw_text(
            draw,
            (INNER_X + 42, cy + 10),
            text,
            R.F.small_bold,
            R.WHITE,
            col_w - 84,
            3,
            "stage06-inseparability",
            cy + 54,
            "center",
        )
        cy += 66
    cy += 4
    R.draw_bullets(
        draw,
        INNER_X + 24,
        cy,
        col_w - 48,
        st["cause_notes"],
        R.AMBER,
        R.F.tiny,
        2,
        "stage06-cause-notes",
        notes_y + 502,
    )
    rx = INNER_X + col_w + col_gap
    R.rounded(
        draw,
        (rx, notes_y, rx + col_w, notes_y + 520),
        18,
        fill=R.DEEP,
        outline=R.GREEN,
        width=3,
    )
    draw.text((rx + 22, notes_y + 16), "DEVOTION / GRACE PATH", font=R.F.h1, fill=R.GREEN)
    cy = notes_y + 90
    for i, text in enumerate(st["devotion"]):
        R.rounded(
            draw,
            (rx + 35, cy, rx + col_w - 35, cy + 80),
            14,
            fill=R.CARD_ALT,
            outline=[R.CYAN, R.TEAL, R.MAGENTA, R.YELLOW][i],
            width=2,
        )
        R.draw_text(
            draw,
            (rx + 50, cy + 18),
            text,
            R.F.small_bold,
            R.WHITE,
            col_w - 100,
            3,
            "stage06-devotion",
            cy + 72,
            "center",
        )
        if i < 3:
            R.arrow(
                draw,
                (rx + col_w / 2, cy + 82),
                (rx + col_w / 2, cy + 100),
                R.CYAN,
                3,
                10,
            )
        cy += 105
    dia_y = notes_y + 540
    dw = (INNER_W - 2 * 26) / 3
    for i, text in enumerate(st["dialectic"]):
        x0 = INNER_X + i * (dw + 26)
        c = [R.RED, R.TEAL, R.YELLOW][i]
        R.rounded(
            draw,
            (x0, dia_y, x0 + dw, bottom),
            15,
            fill=R.CARD_ALT,
            outline=c,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 17, dia_y + 17),
            text,
            R.F.small,
            R.WHITE,
            dw - 34,
            4,
            "stage06-dialectic",
            bottom - 9,
        )


def draw_stage_07(draw, st, top, bottom):
    ny_h = 770
    left_w = 2250
    gap = 30
    right_x = INNER_X + left_w + gap
    right_w = INNER_W - left_w - gap
    R.rounded(
        draw,
        (INNER_X, top, INNER_X + left_w, top + ny_h),
        20,
        fill=R.CARD_ALT,
        outline=R.CYAN,
        width=4,
    )
    draw.text((INNER_X + 22, top + 18), "NYAYA: GOD ORDERS; GOD DOES NOT BECOME MATTER", font=R.F.h1, fill=R.CYAN)
    half = (left_w - 74) / 2
    for i, (title, items, c) in enumerate(
        [
            ("ISVARA - EFFICIENT CAUSE", st["nyaya"]["god"], R.AMBER),
            ("ETERNAL REALITIES - MATERIAL SIDE", st["nyaya"]["matter"], R.TEAL),
        ]
    ):
        x0 = INNER_X + 24 + i * (half + 26)
        R.rounded(
            draw,
            (x0, top + 86, x0 + half, top + 440),
            16,
            fill=R.DEEP,
            outline=c,
            width=3,
        )
        draw.text((x0 + 17, top + 102), title, font=R.F.h2, fill=c)
        R.draw_bullets(
            draw,
            x0 + 18,
            top + 150,
            half - 36,
            items,
            c,
            R.F.small,
            6,
            "stage07-nyaya",
            top + 425,
        )
    R.band(
        draw,
        (INNER_X + 24, top + 464, INNER_X + left_w - 24, top + 742),
        "KARMA CIRCUIT",
        " -> ".join(st["nyaya"]["karma"]),
        R.YELLOW,
        (45, 38, 27),
        R.F.body_bold,
        "stage07-karma",
    )
    R.rounded(
        draw,
        (right_x, top, right_x + right_w, top + ny_h),
        20,
        fill=R.CARD_ALT,
        outline=R.AMBER,
        width=4,
    )
    draw.text((right_x + 22, top + 18), "NYAYA OBJECTION / REPLY", font=R.F.h1, fill=R.AMBER)
    R.draw_text(
        draw,
        (right_x + 26, top + 90),
        st["nyaya"]["objection"],
        R.F.body,
        R.WHITE,
        right_w - 52,
        6,
        "stage07-objection",
        top + 420,
    )
    R.band(
        draw,
        (right_x + 24, top + 448, right_x + right_w - 24, top + 624),
        "ANSWER ROUTE",
        "Pluralist realism -> Isvara as special self -> efficient cause -> eternal atoms as material cause -> adrista administration -> one objection.",
        R.TEAL,
        R.DEEP,
        R.F.small_bold,
        "stage07-route",
    )
    R.draw_text(
        draw,
        (right_x + 26, top + 650),
        "Do not answer the nature question by merely listing proofs such as karyat and ayojanat.",
        R.F.small_bold,
        R.RED,
        right_w - 52,
        4,
        "stage07-proof-trap",
        top + 744,
        "center",
    )
    tax_y = top + ny_h + 28
    draw.text((INNER_X, tax_y), "HINDU DIVINE PLURALITY - TAXONOMY LADDER", font=R.F.h1, fill=R.MAGENTA)
    tax_y += 62
    step_w = 735
    step_h = 315
    rise = 34
    for i, (name, text) in enumerate(st["taxonomy"]):
        x0 = INNER_X + i * (step_w + 20)
        y0 = tax_y + (4 - i) * rise
        c = [R.RED, R.AMBER, R.YELLOW, R.TEAL, R.CYAN][i]
        R.rounded(
            draw,
            (x0, y0, x0 + step_w, y0 + step_h),
            18,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 16, y0 + 16),
            name,
            R.F.h2,
            c,
            step_w - 32,
            3,
            "stage07-tax-name",
            y0 + 68,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 18, y0 + 88),
            text,
            R.F.small,
            R.WHITE,
            step_w - 36,
            4,
            "stage07-tax",
            y0 + step_h - 14,
        )
        if i < 4:
            R.arrow(
                draw,
                (x0 + step_w + 3, y0 + step_h / 2),
                (x0 + step_w + 17, y0 + step_h / 2 - rise),
                R.CYAN,
                3,
                9,
            )
    vedic_y = tax_y + step_h + 4 * rise + 24
    R.band(
        draw,
        (INNER_X, vedic_y, INNER_X + INNER_W, vedic_y + 118),
        "VEDIC ANCHOR",
        st["vedic"],
        R.AMBER,
        (43, 37, 27),
        R.F.small_bold,
        "stage07-vedic",
    )
    R.band(
        draw,
        (INNER_X, vedic_y + 136, INNER_X + INNER_W, bottom),
        "QUALIFIED VERDICT",
        st["verdict"],
        R.TEAL,
        (9, 42, 49),
        R.F.small_bold,
        "stage07-verdict",
    )


def draw_stage_08(draw, st, top, bottom):
    formula_y = top
    gap = 14
    fw = (INNER_W - 5 * gap) / 6
    for i, (name, formula) in enumerate(st["formulas"]):
        x0 = INNER_X + i * (fw + gap)
        c = [R.CYAN, R.AMBER, R.MAGENTA, R.YELLOW, R.TEAL, R.GREEN][i]
        R.rounded(
            draw,
            (x0, formula_y, x0 + fw, formula_y + 176),
            16,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 12, formula_y + 14),
            name,
            R.F.small_bold,
            c,
            fw - 24,
            3,
            "stage08-formula-name",
            formula_y + 63,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 12, formula_y + 76),
            formula,
            R.F.small,
            R.WHITE,
            fw - 24,
            3,
            "stage08-formula",
            formula_y + 164,
            "center",
        )
    matrix_y = formula_y + 198
    matrix_end = R.matrix(
        draw,
        INNER_X,
        matrix_y,
        INNER_W,
        st["matrix_headers"],
        st["matrix_rows"],
        [0.13, 0.18, 0.18, 0.18, 0.16, 0.17],
        R.F.tiny,
        R.F.tiny_bold,
        9,
        "stage08-matrix",
    )
    physical_y = matrix_end + 16
    R.band(
        draw,
        (INNER_X, physical_y, INNER_X + INNER_W, physical_y + 130),
        "PHYSICAL CAUSE TEST",
        st["physical"],
        R.YELLOW,
        (44, 37, 28),
        R.F.small_bold,
        "stage08-physical",
    )
    tests_y = physical_y + 150
    test_gap = 18
    test_w = (INNER_W - test_gap) / 2
    test_h = (bottom - tests_y - test_gap) / 2
    for i, (name, text) in enumerate(st["cross_tests"]):
        row, col = divmod(i, 2)
        x0 = INNER_X + col * (test_w + test_gap)
        y0 = tests_y + row * (test_h + test_gap)
        c = [R.CYAN, R.AMBER, R.TEAL, R.MAGENTA][i]
        R.rounded(
            draw,
            (x0, y0, x0 + test_w, y0 + test_h),
            16,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 18, y0 + 14),
            name,
            R.F.h2,
            c,
            test_w - 36,
            3,
            "stage08-test-name",
            y0 + 62,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 20, y0 + 80),
            text,
            R.F.body,
            R.WHITE,
            test_w - 40,
            5,
            "stage08-test",
            y0 + test_h - 12,
        )
    if tests_y + 2 * test_h + test_gap > bottom + 1:
        R.OVERFLOWS.append(
            {
                "type": "stage08_test_height",
                "actual": round(tests_y + 2 * test_h + test_gap),
                "limit": round(bottom),
            }
        )


def draw_stage_09(draw, st, top, bottom):
    gap = 26
    col_w = (INNER_W - gap) / 2
    box_h = 348
    for i, item in enumerate(st["dialectic"]):
        col = i % 2
        row = i // 2
        x0 = INNER_X + col * (col_w + gap)
        y0 = top + row * (box_h + 20)
        R.rounded(
            draw,
            (x0, y0, x0 + col_w, y0 + box_h),
            18,
            fill=R.CARD_ALT,
            outline=R.RED if col == 0 else R.AMBER,
            width=3,
        )
        draw.text((x0 + 18, y0 + 14), item["target"], font=R.F.h2, fill=R.RED)
        cy = y0 + 62
        for label, text, c in [
            ("OBJECTION", item["objection"], R.RED),
            ("STRONGEST REPLY", item["reply"], R.TEAL),
            ("RESIDUAL COST", item["residual"], R.YELLOW),
        ]:
            draw.text((x0 + 18, cy), label, font=R.F.tiny_bold, fill=c)
            cy += 28
            cy = R.draw_text(
                draw,
                (x0 + 18, cy),
                text,
                R.F.tiny,
                R.WHITE,
                col_w - 36,
                3,
                "stage09-dialectic",
                y0 + box_h - 12,
            )
            cy += 5
    manif_y = top + 3 * (box_h + 20) + 6
    mw = (INNER_W - 2 * gap) / 3
    for i, (label, text, c) in enumerate(
        [
            ("ARGUMENT FOR MANIFESTATION", st["manifestation"]["for"], R.AMBER),
            ("ARGUMENT AGAINST NECESSITY", st["manifestation"]["against"], R.TEAL),
            ("GRADED VERDICT", st["manifestation"]["verdict"], R.YELLOW),
        ]
    ):
        x0 = INNER_X + i * (mw + gap)
        R.rounded(
            draw,
            (x0, manif_y, x0 + mw, manif_y + 230),
            16,
            fill=R.DEEP,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 16, manif_y + 14),
            label,
            R.F.small_bold,
            c,
            mw - 32,
            3,
            "stage09-man-label",
            manif_y + 60,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 18, manif_y + 74),
            text,
            R.F.small,
            R.WHITE,
            mw - 36,
            4,
            "stage09-manifest",
            manif_y + 218,
        )
    traps_y = manif_y + 250
    draw.text((INNER_X, traps_y), "TEN EXAMINER TRAPS - READ ACROSS", font=R.F.h2, fill=R.MAGENTA)
    traps_y += 48
    tw = (INNER_W - 4 * 14) / 5
    th = (bottom - traps_y - 14) / 2
    for i, text in enumerate(st["traps"]):
        row, col = divmod(i, 5)
        x0 = INNER_X + col * (tw + 14)
        y0 = traps_y + row * (th + 14)
        R.rounded(
            draw,
            (x0, y0, x0 + tw, y0 + th),
            12,
            fill=R.CARD_ALT,
            outline=R.RED if row == 0 else R.YELLOW,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 12, y0 + 12),
            f"{i + 1}. {text}",
            R.F.tiny,
            R.WHITE,
            tw - 24,
            3,
            "stage09-traps",
            y0 + th - 8,
        )


def draw_stage_10(draw, st, top, bottom):
    pyq_end = R.matrix(
        draw,
        INNER_X,
        top,
        INNER_W,
        st["pyq_headers"],
        st["pyqs"],
        [0.12, 0.31, 0.57],
        R.F.tiny,
        R.F.tiny_bold,
        8,
        "stage10-pyqs",
    )
    spine_y = pyq_end + 18
    gap = 24
    sw = (INNER_W - 2 * gap) / 3
    for i, (name, text) in enumerate(st["spines"]):
        x0 = INNER_X + i * (sw + gap)
        c = [R.CYAN, R.TEAL, R.YELLOW][i]
        R.rounded(
            draw,
            (x0, spine_y, x0 + sw, spine_y + 238),
            17,
            fill=R.CARD_ALT,
            outline=c,
            width=3,
        )
        R.draw_text(
            draw,
            (x0 + 16, spine_y + 14),
            name,
            R.F.h2,
            c,
            sw - 32,
            3,
            "stage10-spine-name",
            spine_y + 60,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 18, spine_y + 76),
            text,
            R.F.small,
            R.WHITE,
            sw - 36,
            4,
            "stage10-spine",
            spine_y + 224,
        )
    dir_y = spine_y + 258
    dw = (INNER_W - 3 * 16) / 4
    for i, (name, text) in enumerate(st["directives"]):
        x0 = INNER_X + i * (dw + 16)
        R.rounded(
            draw,
            (x0, dir_y, x0 + dw, dir_y + 150),
            14,
            fill=R.DEEP,
            outline=R.MAGENTA,
            width=2,
        )
        R.draw_text(
            draw,
            (x0 + 12, dir_y + 12),
            name,
            R.F.small_bold,
            R.MAGENTA,
            dw - 24,
            3,
            "stage10-directive-name",
            dir_y + 48,
            "center",
        )
        R.draw_text(
            draw,
            (x0 + 14, dir_y + 58),
            text,
            R.F.small,
            R.WHITE,
            dw - 28,
            3,
            "stage10-directive",
            dir_y + 140,
            "center",
        )
    conclusion_y = dir_y + 170
    R.band(
        draw,
        (INNER_X, conclusion_y, INNER_X + INNER_W, bottom),
        "MODEL PHILOSOPHICAL CONCLUSION",
        st["conclusion"],
        R.MAGENTA,
        R.ANSWER,
        R.F.body_bold,
        "stage10-conclusion",
    )


STAGE_DRAWERS = {
    "01": draw_stage_01,
    "02": draw_stage_02,
    "03": draw_stage_03,
    "04": draw_stage_04,
    "05": draw_stage_05,
    "06": draw_stage_06,
    "07": draw_stage_07,
    "08": draw_stage_08,
    "09": draw_stage_09,
    "10": draw_stage_10,
}


def build_master():
    R.reset_audit()
    header_h = 560
    total_h = (
        TOP
        + header_h
        + 50
        + sum(stage["height"] for stage in S.STAGES)
        + STAGE_GAP * (len(S.STAGES) - 1)
        + 85
    )
    image = Image.new("RGB", (W, total_h), R.BG)
    draw = ImageDraw.Draw(image)
    for yy in range(170):
        frac = 1 - yy / 170
        draw.line((0, yy, W, yy), fill=(7, 20 + int(5 * frac), 33 + int(9 * frac)))
    y = TOP
    y += draw_header(draw, y)
    y += 50
    stage_bounds = []
    centres = []
    for index, stage in enumerate(S.STAGES):
        next_title = S.STAGES[index + 1]["title"] if index + 1 < len(S.STAGES) else None
        body_top, body_bottom = draw_stage_shell(draw, stage, y, next_title)
        STAGE_DRAWERS[stage["n"]](draw, stage, body_top, body_bottom)
        stage_bounds.append(
            {
                "n": stage["n"],
                "title": stage["title"],
                "grammar": stage["grammar"],
                "y0": y,
                "y1": y + stage["height"],
                "body_top": body_top,
                "body_bottom": body_bottom,
            }
        )
        centres.append((y + 62, stage["n"]))
        y += stage["height"] + STAGE_GAP
    y -= STAGE_GAP
    rail_top = stage_bounds[0]["y0"] - 18
    rail_bottom = stage_bounds[-1]["y1"] - 48
    draw.line((RAIL_X, rail_top, RAIL_X, rail_bottom), fill=R.CYAN, width=10)
    for (cy, num), bounds in zip(centres, stage_bounds):
        r = 46
        draw.ellipse(
            (RAIL_X - r, cy - r, RAIL_X + r, cy + r),
            fill=R.BG,
            outline=R.CYAN,
            width=8,
        )
        tw = R.text_w(R.F.rail, num)
        draw.text(
            (RAIL_X - tw / 2, cy - R.line_h(R.F.rail, 0) / 2 - 2),
            num,
            font=R.F.rail,
            fill=R.CYAN,
        )
        R.arrow(draw, (RAIL_X + r + 8, cy), (CARD_X0 - 8, cy), R.CYAN, 6, 20)
    footer = (
        "NOTIONS OF GOD g6 | APPROVAL FALSE | ONE CYAN RAIL | CORE 01-09 BEFORE "
        "PYQ / ANSWER ENRICHMENT 10 | PRE-EXISTING SOURCES AND REFERENCES HASH-PRESERVED"
    )
    draw.text((MARGIN, y + 34), footer, font=R.F.note, fill=R.DIM)
    image.save(MASTER, dpi=(DPI, DPI), optimize=False)
    return image, stage_bounds


def build_poster(image):
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas

    width_pt = 39.37 * 72
    height_pt = width_pt * image.height / image.width
    if height_pt > 190 * 72:
        height_pt = 190 * 72
        width_pt = height_pt * image.width / image.height
    c = canvas.Canvas(str(POSTER), pagesize=(width_pt, height_pt), invariant=1)
    c.setTitle("Notions of God - Continuous At-a-Glance g6 Poster")
    c.drawImage(ImageReader(image), 0, 0, width=width_pt, height=height_pt)
    c.showPage()
    c.save()
    return [width_pt, height_pt]


def tile_geometry(image, max_tile_px, target_overlap=330):
    min_pages = max(1, math.ceil(image.height / max_tile_px))
    chosen = None
    for pages in range(min_pages, min_pages + 8):
        if pages == 1:
            tile_h = image.height
            overlap = 0
        else:
            tile_h = math.ceil((image.height + (pages - 1) * target_overlap) / pages)
            step = (image.height - tile_h) / (pages - 1)
            overlap = tile_h - step
        if tile_h <= max_tile_px and (pages == 1 or 250 <= overlap <= 400):
            chosen = (pages, tile_h)
            break
    if chosen is None:
        raise RuntimeError("Could not produce A3 tiles with 250-400 px overlap")
    pages, tile_h = chosen
    if pages == 1:
        tops = [0]
    else:
        step = (image.height - tile_h) / (pages - 1)
        tops = [round(i * step) for i in range(pages)]
    crops = []
    for i, top in enumerate(tops):
        bottom = min(top + tile_h, image.height)
        if i == pages - 1:
            top = image.height - tile_h
            bottom = image.height
        prev_bottom = crops[-1]["box"][3] if crops else top
        crops.append(
            {
                "tile": i + 1,
                "box": [0, int(top), image.width, int(bottom)],
                "overlap_with_previous_px": 0 if not crops else int(prev_bottom - top),
            }
        )
    return crops


def build_tiled(image):
    from reportlab.lib.utils import ImageReader
    from reportlab.pdfgen import canvas

    page_w, page_h = 1190.55, 841.89
    margin = 18
    footer = 30
    area_w = page_w - 2 * margin
    area_h = page_h - 2 * margin - footer
    max_tile_px = int(image.width * area_h / area_w)
    crops = tile_geometry(image, max_tile_px, 330)
    c = canvas.Canvas(str(TILED), pagesize=(page_w, page_h), invariant=1)
    for i, info in enumerate(crops):
        box = info["box"]
        crop = image.crop(tuple(box))
        raw = io.BytesIO()
        crop.save(raw, format="PNG")
        info["png_sha256"] = sha256_bytes(raw.getvalue())
        c.setFillColorRGB(*(v / 255 for v in R.BG))
        c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
        draw_h = area_w * crop.height / crop.width
        c.drawImage(
            ImageReader(crop),
            margin,
            page_h - margin - draw_h,
            width=area_w,
            height=draw_h,
        )
        c.setFont("Helvetica", 8.5)
        c.setFillColorRGB(*(v / 255 for v in R.DIM))
        footer_text = (
            f"NOTIONS OF GOD g6 | TILE {i + 1}/{len(crops)} | "
            f"SAME MASTER CROP y={box[1]}..{box[3]} of {image.height}px | "
            + ("FLOW CONTINUES" if i + 1 < len(crops) else "END OF MASTER")
        )
        c.drawString(margin + 2, 9, footer_text)
        c.showPage()
    c.setTitle("Notions of God - Continuous At-a-Glance g6 Tiled")
    c.save()
    return crops, [page_w, page_h]


def build_previews():
    import fitz

    PREVIEWS.mkdir(parents=True, exist_ok=True)
    for old in PREVIEWS.glob("*.png"):
        old.unlink()
    doc = fitz.open(str(TILED))
    paths = []
    for index, page in enumerate(doc):
        pix = page.get_pixmap(dpi=125, alpha=False)
        path = PREVIEWS / f"page-{index + 1:03d}.png"
        pix.save(str(path))
        paths.append(path)
    doc.close()
    return paths


def build_contact_sheets(paths, per_sheet=6, columns=3, gap=20):
    outputs = []
    for start in range(0, len(paths), per_sheet):
        chunk = paths[start : start + per_sheet]
        images = [Image.open(path).convert("RGB") for path in chunk]
        cols = min(columns, len(images))
        rows = math.ceil(len(images) / cols)
        tw = max(img.width for img in images)
        th = max(img.height for img in images)
        sheet = Image.new(
            "RGB",
            (gap + cols * (tw + gap), gap + rows * (th + gap)),
            R.BG,
        )
        d = ImageDraw.Draw(sheet)
        for i, img in enumerate(images):
            row, col = divmod(i, cols)
            x = gap + col * (tw + gap)
            y = gap + row * (th + gap)
            sheet.paste(img, (x, y))
            d.rectangle((x - 2, y - 2, x + img.width + 1, y + img.height + 1), outline=R.CYAN, width=2)
        path = PREVIEWS / f"contact-sheet-{start // per_sheet + 1:02d}.png"
        sheet.save(path)
        outputs.append(path)
    return outputs


def write_design_spec(image, stage_bounds, poster_points, crops, tile_points):
    spec = {
        "artifact": "Notions of God - Philosophy Paper II - continuous at-a-glance master flow",
        "generation": S.GENERATION,
        "approved": False,
        "generated_date": S.GENERATED_DATE,
        "content_owners": S.SOURCES,
        "design_references_read_only": [
            {"name": name, "folder": rel} for name, rel in S.REFERENCE_FOLDERS
        ],
        "canvas": {
            "width_px": image.width,
            "height_px": image.height,
            "dpi": DPI,
            "rail": {
                "colour": list(R.CYAN),
                "x_px": RAIL_X,
                "continuous_through_all_stages": True,
            },
            "font_family": "Segoe UI / Segoe UI Bold",
            "source_text_encoding": "ASCII",
        },
        "stage_count": len(S.STAGES),
        "stages": [
            {
                "n": stage["n"],
                "title": stage["title"],
                "grammar": stage["grammar"],
                "height_px": stage["height"],
                "pills": stage["pills"],
                "required_terms": stage["required"],
                "bounds": bounds,
            }
            for stage, bounds in zip(S.STAGES, stage_bounds)
        ],
        "must_show_terms": S.MUST_SHOW,
        "outputs": {
            "master_png": MASTER.name,
            "poster_pdf": POSTER.name,
            "poster_points": poster_points,
            "poster_pages": 1,
            "tiled_pdf": TILED.name,
            "tile_page_points": tile_points,
            "tile_count": len(crops),
            "tile_crops": crops,
            "previews_folder": "previews",
        },
        "quality_intent": {
            "core_before_pyq": "Stages 01-09 are doctrine; Stage 10 is PYQ/answer enrichment.",
            "layout_diversity": [stage["grammar"] for stage in S.STAGES],
            "same_master_tiles": True,
            "target_overlap_px": "250-400",
            "answer_grabbing_lines": len(S.STAGES),
            "approval_state": "false until explicit user approval",
        },
    }
    DESIGN_SPEC.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    return spec


def write_readme(spec):
    crop_lines = "\n".join(
        (
            f"  page-{item['tile']:03d}: y={item['box'][1]}..{item['box'][3]} px; "
            f"overlap={item['overlap_with_previous_px']} px"
        )
        for item in spec["outputs"]["tile_crops"]
    )
    text = f"""NOTIONS OF GOD - CONTINUOUS AT-A-GLANCE CORE-FIRST - GENERATION g6

Approval: false - pending explicit user review.

This self-contained folder is a new Carvaka-standard revision package for Philosophy
Paper II, Philosophy of Religion, Topic 01: Notions of God. It does not replace or
modify any canonical Markdown, learning-session PDF, approved reference, prior g3/g4/g5
package, repository instruction file, skill file or export ledger.

PRIMARY OUTPUTS
  Master PNG: {MASTER.name}
  Master dimensions: {spec['canvas']['width_px']} x {spec['canvas']['height_px']} px
  Master metadata: {spec['canvas']['dpi']} DPI
  Poster PDF: {POSTER.name} (one page)
  Tiled PDF: {TILED.name} ({spec['outputs']['tile_count']} A3-landscape pages)

TILE CROPS - PIXEL-IDENTICAL REGIONS OF THE MASTER
{crop_lines}

STAGES
"""
    for stage in spec["stages"]:
        text += f"  {stage['n']}: {stage['title']} [{stage['grammar']}]\n"
    text += """

SOURCE / DESIGN CONTROL
  Exact owners and read-only design references are listed in design-spec.json.
  preservation-hashes-before.json and preservation-hashes-after.json prove that every
  recorded pre-existing source/reference file remained byte-identical.

REBUILD
  python build_g6.py

VALIDATE
  python validate_g6.py

The renderer is deterministic for the fixed source specification and uses only files
inside this folder for writes. All authored source text is ASCII; Segoe UI is used for
the rendered master and validated for the characters actually present.
"""
    (HERE / "README.txt").write_text(text, encoding="utf-8")


def write_audit(image, spec, before_mismatches, previews, contacts):
    artifacts = [
        MASTER,
        POSTER,
        TILED,
        DESIGN_SPEC,
        HERE / "README.txt",
        HERE / "content_spec.py",
        HERE / "render_lib.py",
        HERE / "build_g6.py",
        HERE / "validate_g6.py",
    ] + previews + contacts
    payload = {
        "generation": S.GENERATION,
        "master_size": list(image.size),
        "master_dpi": list(Image.open(MASTER).info.get("dpi", (0, 0))),
        "overflow_events": R.OVERFLOWS,
        "recorded_boxes": R.BOXES,
        "preservation_mismatches_after_build": before_mismatches,
        "artifact_hashes": {
            str(path.relative_to(HERE)): sha256(path)
            for path in artifacts
            if path.exists()
        },
        "tile_crops": spec["outputs"]["tile_crops"],
    }
    BUILD_AUDIT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main():
    before = write_before_manifest()
    image, stage_bounds = build_master()
    poster_points = build_poster(image)
    crops, tile_points = build_tiled(image)
    previews = build_previews()
    contacts = build_contact_sheets(previews)
    spec = write_design_spec(image, stage_bounds, poster_points, crops, tile_points)
    write_readme(spec)
    _, mismatches = write_after_manifest(before)
    write_audit(image, spec, mismatches, previews, contacts)
    print(
        json.dumps(
            {
                "master": list(image.size),
                "poster": POSTER.name,
                "tiles": len(crops),
                "overlaps": [
                    item["overlap_with_previous_px"] for item in crops[1:]
                ],
                "overflows": len(R.OVERFLOWS),
                "preservation_mismatches": len(mismatches),
            }
        )
    )
    if R.OVERFLOWS or mismatches:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
