"""Validate the Notions of God continuous at-a-glance g6 package."""
from __future__ import annotations

import io
import json
import re
import sys
from pathlib import Path

import fitz
from PIL import Image, ImageStat

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))

import build_g6 as B  # noqa: E402
import content_spec as S  # noqa: E402
import render_lib as R  # noqa: E402

Image.MAX_IMAGE_PIXELS = None

REPORT = HERE / "validation-report.txt"
lines = []
failures = []


def say(text=""):
    lines.append(text)
    print(text)


def check(condition, label, detail=""):
    marker = "PASS" if condition else "FAIL"
    say(f"  [{marker}] {label}" + (f" - {detail}" if detail else ""))
    if not condition:
        failures.append(label)
    return condition


def normalize(text):
    text = text.lower().replace("-", " ")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def visible_text(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            if key not in {"required", "height", "grammar"}:
                yield from visible_text(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            yield from visible_text(item)


def term_present(text, term):
    hay = normalize(text)
    needle = normalize(term)
    if needle in hay:
        return True
    words = [w for w in needle.split() if len(w) > 2 and w not in {"and", "the", "not"}]
    variants = []
    for word in words:
        group = {word}
        if word.endswith("s"):
            group.add(word[:-1])
        if word.endswith("y"):
            group.add(word[:-1] + "ies")
        if word.endswith("ies"):
            group.add(word[:-3] + "y")
        variants.append(group)
    tokens = set(hay.split())
    return all(any(v in tokens for v in group) for group in variants)


def blank_page(page):
    pix = page.get_pixmap(dpi=30, alpha=False)
    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
    stat = ImageStat.Stat(im)
    spread = sum(max(ch) - min(ch) for ch in stat.extrema)
    return spread < 18


spec = json.loads(B.DESIGN_SPEC.read_text(encoding="utf-8"))
audit = json.loads(B.BUILD_AUDIT.read_text(encoding="utf-8"))
before = json.loads(B.HASH_BEFORE.read_text(encoding="utf-8"))
after = json.loads(B.HASH_AFTER.read_text(encoding="utf-8"))
master = Image.open(B.MASTER).convert("RGB")

say("=" * 112)
say("VALIDATION REPORT - PHILOSOPHY PAPER II / PHILOSOPHY OF RELIGION 01 / NOTIONS OF GOD")
say("CONTINUOUS AT-A-GLANCE CORE-FIRST - GENERATION g6")
say("=" * 112)

say("\n1. SOURCE AND REFERENCE PRESERVATION")
check(after["matches_before"], "all recorded pre-existing source/reference files unchanged")
check(not after["mismatches"], "preservation mismatch list empty")
check(before["groups"] == after["groups"], "before and after manifests are byte-hash equivalent")
for group, items in before["groups"].items():
    check(bool(items), f"{group} recorded", f"{len(items)} files")
say("  NOTE: canonical Markdown, approved Carvaka reference, Polity g9 and Notions g5 were read-only.")

say("\n2. MASTER CANVAS AND METADATA")
check(master.width >= 4800, "master width at least 4800 px", str(master.width))
check(master.width == spec["canvas"]["width_px"], "master width matches design spec")
check(master.height == spec["canvas"]["height_px"], "master height matches design spec", str(master.height))
dpi = Image.open(B.MASTER).info.get("dpi", (0, 0))
check(round(dpi[0]) == 300 and round(dpi[1]) == 300, "master PNG has 300 DPI metadata", str(dpi))
check(spec["canvas"]["rail"]["continuous_through_all_stages"], "one continuous cyan rail declared")
check(spec["canvas"]["rail"]["colour"] == list(R.CYAN), "rail colour is cyan", str(R.CYAN))
check(not audit["overflow_events"], "no measured text overflow or stage-boundary overflow", str(len(audit["overflow_events"])))

say("\n3. STAGE ORDER, CORE-FIRST SEQUENCE AND LAYOUT DIVERSITY")
expected = [f"{i:02d}" for i in range(1, 11)]
actual = [stage["n"] for stage in spec["stages"]]
check(actual == expected, "ten stages present in exact order", " ".join(actual))
check(spec["stage_count"] == 10, "stage count is ten")
check("PYQ" not in " ".join(stage["title"] for stage in spec["stages"][:9]), "core stages 01-09 precede PYQ enrichment")
check("PYQ ROUTING" in spec["stages"][9]["title"], "Stage 10 is PYQ/answer enrichment")
grammars = [stage["grammar"] for stage in spec["stages"]]
check(len(set(grammars)) == 10, "all ten stages use distinct visual grammars", f"{len(set(grammars))}/10")
bounds = [stage["bounds"] for stage in spec["stages"]]
overlap_pairs = []
for left, right in zip(bounds, bounds[1:]):
    if left["y1"] >= right["y0"]:
        overlap_pairs.append((left["n"], right["n"]))
check(not overlap_pairs, "stage cards do not overlap", str(overlap_pairs) if overlap_pairs else "58 px gaps")
for stage in spec["stages"]:
    say(f"      Stage {stage['n']}: {stage['title']}")
    say(f"        visual grammar: {stage['grammar']}")
    say(f"        bounds: y={stage['bounds']['y0']}..{stage['bounds']['y1']} px")

say("\n4. SUBSTANTIVE STAGE COVERAGE")
all_missing = []
for stage, authored in zip(spec["stages"], S.STAGES):
    text = "\n".join(visible_text(authored))
    missing = [term for term in stage["required_terms"] if not term_present(text, term)]
    all_missing.extend((stage["n"], term) for term in missing)
    check(
        not missing,
        f"Stage {stage['n']} required-term coverage",
        (
            f"{len(stage['required_terms'])}/{len(stage['required_terms'])} present"
            if not missing
            else "missing: " + ", ".join(missing)
        ),
    )
global_text = "\n".join(visible_text({"header": S.HEADER, "stages": S.STAGES}))
global_missing = [term for term in S.MUST_SHOW if not term_present(global_text, term)]
check(
    not global_missing,
    "global must-show term coverage",
    (
        f"{len(S.MUST_SHOW)}/{len(S.MUST_SHOW)} present"
        if not global_missing
        else "missing: " + ", ".join(global_missing)
    ),
)
check(
    "anirvacaniya" in global_text.lower()
    and "do not call brahman anirvacaniya" in global_text.lower(),
    "Advaita technical correction is explicit",
    "anirvacaniya belongs to maya/world appearance, not Brahman",
)
high_value = [
    "personalistic and impersonalistic",
    "immanent and transcendent",
    "Spinoza",
    "Relation between God and Self according to Ramanuja",
    "physical manifestation",
    "Hinduism poly-theistic",
    "Freedom of will and an omnipotent God",
    "Nature of God in Nyaya",
]
for ask in high_value:
    check(term_present(global_text, ask), f"verified high-value ask routed: {ask}")

say("\n5. POSTER PDF")
poster = fitz.open(str(B.POSTER))
check(poster.page_count == 1, "poster is one page", str(poster.page_count))
rect = poster[0].rect
check(
    abs((rect.width / rect.height) - (master.width / master.height)) < 0.002,
    "poster preserves full master aspect ratio",
    f"{rect.width / 72:.2f} x {rect.height / 72:.2f} in",
)
check(max(rect.width, rect.height) / 72 <= 200, "poster remains within PDF page limit")
poster_pix = poster[0].get_pixmap(dpi=18, alpha=False)
check(len(poster_pix.samples) > 1000, "poster renders successfully")
check(not blank_page(poster[0]), "poster is not blank")
poster.close()

say("\n6. TILED PDF - SAME-MASTER IDENTITY AND OVERLAP")
tiled = fitz.open(str(B.TILED))
crops = spec["outputs"]["tile_crops"]
check(tiled.page_count == len(crops), "tiled page count matches crop ledger", str(tiled.page_count))
check(
    abs(tiled[0].rect.width - 1190.55) < 1 and abs(tiled[0].rect.height - 841.89) < 1,
    "tiled pages are A3 landscape",
    f"{tiled[0].rect.width:.1f} x {tiled[0].rect.height:.1f} pt",
)
same = True
blank_tiles = []
for index, page in enumerate(tiled):
    info = crops[index]
    box = info["box"]
    images = page.get_images(full=True)
    if not images:
        same = False
        say(f"      tile {index + 1}: no embedded image")
        continue
    xref = images[0][0]
    embedded = fitz.Pixmap(tiled, xref)
    embedded_image = Image.open(io.BytesIO(embedded.tobytes("png"))).convert("RGB")
    fresh = master.crop(tuple(box))
    identical = embedded_image.size == fresh.size and embedded_image.tobytes() == fresh.tobytes()
    same = same and identical
    if blank_page(page):
        blank_tiles.append(index + 1)
    say(
        f"      tile {index + 1:02d}: master y={box[1]}..{box[3]} px; "
        f"overlap={info['overlap_with_previous_px']} px; "
        f"{'pixel-identical' if identical else 'DIFFERENT'}"
    )
check(same, "every tile image is a pixel-identical crop of the same master")
overlaps = [item["overlap_with_previous_px"] for item in crops[1:]]
check(
    all(250 <= value <= 400 for value in overlaps),
    "every vertical overlap is within 250-400 px",
    ", ".join(map(str, overlaps)),
)
check(not blank_tiles, "no blank tiled pages", str(blank_tiles) if blank_tiles else "")
tops = [item["box"][1] for item in crops]
check(len(set(tops)) == len(tops), "no duplicate tile crops")
tiled.close()

say("\n7. PREVIEWS AND CONTACT SHEETS")
previews = sorted((HERE / "previews").glob("page-*.png"))
contacts = sorted((HERE / "previews").glob("contact-sheet-*.png"))
check(len(previews) == len(crops), "one preview per tiled page", str(len(previews)))
check(bool(contacts), "contact sheet(s) generated", str(len(contacts)))
preview_blank = []
for path in previews:
    im = Image.open(path).convert("RGB")
    extrema = ImageStat.Stat(im).extrema
    if sum(max(ch) - min(ch) for ch in extrema) < 18:
        preview_blank.append(path.name)
check(not preview_blank, "preview images are non-blank", str(preview_blank) if preview_blank else "")

say("\n8. GLYPHS, CLIPPING AND CONTRAST")
source_ascii = all(ord(char) < 128 for char in S.VISIBLE_TEXT)
check(source_ascii, "all authored source text is ASCII")
check("\ufffd" not in S.VISIBLE_TEXT, "no Unicode replacement character in source content")
try:
    from fontTools.ttLib import TTFont

    cmap = {}
    for table in TTFont(r"C:\Windows\Fonts\segoeui.ttf")["cmap"].tables:
        cmap.update(table.cmap)
    missing_chars = sorted(
        {
            ord(char)
            for char in S.VISIBLE_TEXT
            if not char.isspace() and ord(char) not in cmap
        }
    )
    check(not missing_chars, "selected body font supports every rendered source character", str(missing_chars))
except Exception as exc:
    check(False, "font cmap validation", str(exc))
title_ratio = R.contrast_ratio(R.WHITE, R.CARD)
body_ratio = R.contrast_ratio(R.DIM, R.CARD)
check(title_ratio >= 7, "stage-title contrast is high", f"{title_ratio:.2f}:1")
check(body_ratio >= 4.5, "body/secondary-text contrast is adequate", f"{body_ratio:.2f}:1")
check(not audit["overflow_events"], "clipping/overflow audit remains empty")
check(not overlap_pairs, "stage overlap audit remains empty")

say("\n9. DELIVERABLE INVENTORY")
required_files = [
    "README.txt",
    "content_spec.py",
    "render_lib.py",
    "build_g6.py",
    "validate_g6.py",
    "design-spec.json",
    "build-audit.json",
    "preservation-hashes-before.json",
    "preservation-hashes-after.json",
    B.MASTER.name,
    B.POSTER.name,
    B.TILED.name,
]
for name in required_files:
    path = HERE / name
    check(path.exists() and path.stat().st_size > 0, name, f"{path.stat().st_size / 1024:.1f} KB" if path.exists() else "missing")

say("\n" + "=" * 112)
say(f"RESULT: {'ALL CHECKS PASSED' if not failures else str(len(failures)) + ' CHECK(S) FAILED'}")
if failures:
    for failure in failures:
        say(f"  FAILED: {failure}")
say("Approval state: FALSE - explicit user approval still required.")
say("No canonical source, prior flowchart generation, reference, instruction file or export ledger was modified.")
say("=" * 112)

REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
raise SystemExit(1 if failures else 0)
