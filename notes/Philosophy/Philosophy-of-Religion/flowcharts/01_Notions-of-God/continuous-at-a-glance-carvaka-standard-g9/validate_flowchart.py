from __future__ import annotations

import io
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import fitz
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import spec_content as S

Image.MAX_IMAGE_PIXELS = None
spec = json.loads((HERE / "design-spec.json").read_text(encoding="utf-8"))
master_path = HERE / spec["outputs"]["master_png"]
poster_path = HERE / spec["outputs"]["poster_pdf"]
tiled_path = HERE / spec["outputs"]["tiled_pdf"]
master = Image.open(master_path).convert("RGB")

lines: list[str] = []
failures: list[str] = []


def say(text=""):
    lines.append(text)
    print(text)


def check(condition, label, detail=""):
    say(f"[{'PASS' if condition else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))
    if not condition:
        failures.append(label)


say("VALIDATION REPORT — NOTIONS OF GOD — CONTINUOUS AT-A-GLANCE CARVAKA-STANDARD g9")
say(f"generated {datetime.now().isoformat(timespec='seconds')}")
say("=" * 100)

check(master.width == 4800, "master width", f"{master.width}px")
check(round(master.info.get("dpi", (0, 0))[0]) == 300, "master DPI metadata", str(master.info.get("dpi")))
check(master.height > 15000, "nontrivial continuous canvas height", f"{master.height}px")
check(not spec.get("overflow_events"), "no measured text overflow", str(spec.get("overflow_events")))

expected_order = [str(i) for i in range(15)] + ["E"]
check(spec["stage_order"] == expected_order, "stage order 0..14 plus enrichment", " ".join(spec["stage_order"]))
check(len(set("|".join(v) for v in spec["layout_signatures"].values())) >= 10,
      "layout diversity", f"{len(set('|'.join(v) for v in spec['layout_signatures'].values()))} signatures")

blob = json.dumps(S.STAGES, ensure_ascii=False).casefold()
missing = [term for term in S.MUST_SHOW if term.casefold() not in blob]
check(not missing, "all required doctrine terms present", ", ".join(missing) if missing else f"{len(S.MUST_SHOW)} terms")

with fitz.open(poster_path) as doc:
    check(doc.page_count == 1, "standalone poster is one page", str(doc.page_count))
    ratio_ok = abs((doc[0].rect.width / doc[0].rect.height) - (master.width / master.height)) < 0.002
    check(ratio_ok, "poster preserves master aspect ratio")

with fitz.open(tiled_path) as doc:
    check(doc.page_count == spec["outputs"]["tile_count"], "tiled page count", str(doc.page_count))
    same = True
    for index, page in enumerate(doc):
        images = page.get_images(full=True)
        if not images:
            same = False
            continue
        pix = fitz.Pixmap(doc, images[0][0])
        embedded = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
        box = spec["outputs"]["tile_crops"][index]["box"]
        fresh = master.crop(tuple(box))
        same &= embedded.size == fresh.size and embedded.tobytes() == fresh.tobytes()
    check(same, "all tiled images are pixel-identical master crops")
    check(spec["outputs"]["tile_overlap_px"] >= 240, "tile overlap", f"{spec['outputs']['tile_overlap_px']}px")

previews = sorted((HERE / "previews").glob("page-*.png"))
contacts = sorted((HERE / "previews").glob("contact-sheet-*.png"))
check(len(previews) == spec["outputs"]["tile_count"], "one preview per tile", str(len(previews)))
check(bool(contacts), "contact sheet created", str(len(contacts)))

replacement = False
for path in (poster_path, tiled_path):
    with fitz.open(path) as doc:
        replacement |= any("\ufffd" in page.get_text() for page in doc)
check(not replacement, "no replacement glyphs in PDF text layer")

check(master_path.stat().st_size > 500_000, "master PNG nontrivial size", f"{master_path.stat().st_size / 1024:.1f}KB")
check(poster_path.stat().st_size > 500_000, "poster PDF nontrivial size", f"{poster_path.stat().st_size / 1024:.1f}KB")

say("=" * 100)
say("RESULT: " + ("ALL CHECKS PASSED" if not failures else f"{len(failures)} CHECK(S) FAILED"))
say("Approval: FALSE — pending explicit user review.")
(HERE / "validation-report.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
sys.exit(1 if failures else 0)
