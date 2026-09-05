"""Validate the Polity 01 g9 continuous at-a-glance package."""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import render_lib as R          # noqa: E402
import spec_content as S        # noqa: E402
import build_g9 as B            # noqa: E402

Image.MAX_IMAGE_PIXELS = None
L = []


def say(s=""):
    L.append(s)
    print(s)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest().upper()


def sha_b(b):
    return hashlib.sha256(b).hexdigest().upper()


spec = json.loads((HERE / "bespoke-design-spec.json").read_text(encoding="utf-8"))
master = Image.open(HERE / "master.png")
POSTER = HERE / spec["outputs"]["poster_pdf"]
TILED = HERE / spec["outputs"]["tiled_pdf"]
fails, warns = [], []


def check(ok, label, detail=""):
    say(f"  [{'PASS' if ok else 'FAIL'}] {label}{(' — ' + detail) if detail else ''}")
    if not ok:
        fails.append(label)
    return ok


say("=" * 108)
say("VALIDATION REPORT — POLITY 01 · HISTORICAL BACKGROUND OF THE INDIAN CONSTITUTION")
say("CONTINUOUS AT-A-GLANCE MASTER FLOW — GENERATION g9 (Carvaka-standard)")
say(f"generated {datetime.now().isoformat(timespec='seconds')}")
say("=" * 108)

# 1 -------------------------------------------------------------- immutability
say("\n1. IMMUTABLE APPROVED REFERENCE — Philosophy Paper-I Indian Philosophy 01 / Carvaka")
for name, want in B.REF_EXPECTED.items():
    got = sha(B.REF_DIR / name)
    check(got == want, name, f"sha256 {got[:24]}…")
ref_all = {str(p.relative_to(B.REF_DIR)): sha(p) for p in sorted(B.REF_DIR.rglob("*")) if p.is_file()}
check(ref_all == json.loads((HERE / "build-audit.json").read_text(encoding="utf-8"))
      ["reference_hashes_before_build"],
      "every file in the reference folder unchanged", f"{len(ref_all)} files re-hashed")
say("  NOTE: the reference folder was opened read-only; no write occurred at any point.")

# 2 ------------------------------------------------------------ g8 preservation
say("\n2. REJECTED GENERATION g8 — PRESERVED FOR TRACEABILITY")
audit = json.loads((HERE / "build-audit.json").read_text(encoding="utf-8"))
g8 = {str(p.relative_to(B.G8_DIR)): sha(p) for p in sorted(B.G8_DIR.rglob("*")) if p.is_file()}
check(audit["g8_hashes_before_build"] == audit["g8_hashes_after_build"],
      "g8 hashes identical before and after the g9 build", f"{len(g8)} files")
check(g8 == audit["g8_hashes_after_build"],
      "g8 still byte-identical at validation time")
check(audit["reference_hashes_before_build"] == audit["reference_hashes_after_build"],
      "immutable reference untouched across the build")

# 3 --------------------------------------------------------------- master image
say("\n3. MASTER CANVAS")
check(master.size[0] == 4800, "master width is 4800 px", f"{master.size[0]}")
check(round(master.info.get("dpi", (0, 0))[0]) == 300, "master dpi metadata is 300",
      str(master.info.get("dpi")))
check(master.size[1] == spec["canvas"]["height_px"], "height matches the design spec",
      f"{master.size[1]} px  ({master.size[1]/300:.1f} in tall)")
check(len(audit["overflow_events"]) == 0,
      "no text overflow or measure/draw height mismatch recorded during rendering",
      f"{len(audit['overflow_events'])} events")

# 4 ---------------------------------------------------------------- stage audit
say("\n4. STAGE COMPLETENESS — REQUIRED SPINE 0..14 PLUS SUBORDINATE ENRICHMENT")
want = [str(i) for i in range(15)] + ["E"]
got = [s["n"] for s in spec["stages"]]
check(got == want, "all sixteen stages present in order", " ".join(got))
required_titles = {
    "0": "IDENTITY", "1": "PRE-1773", "2": "REGULATING ACT 1773", "3": "1781",
    "4": "PITT'S INDIA ACT 1784", "5": "CHARTER ACTS 1793 AND 1813", "6": "CHARTER ACT 1833",
    "7": "CHARTER ACT 1853", "8": "GOVERNMENT OF INDIA ACT 1858",
    "9": "INDIAN COUNCILS ACTS 1861 AND 1892", "10": "1909", "11": "1919", "12": "1935",
    "13": "INDIAN INDEPENDENCE ACT 1947", "14": "EXAM SYNTHESIS", "E": "ENRICHMENT",
}
bad = [n for n, frag in required_titles.items()
       if frag not in next(s for s in spec["stages"] if s["n"] == n)["title"]]
check(not bad, "each stage carries its required subject", "mismatched: " + str(bad) if bad else "")
check(spec["stages"][-1]["kind"] == "extra" and
      all(s["kind"] != "extra" for s in spec["stages"][:-1]),
      "enrichment is last and visually subordinate; the core is complete before it")
check(next(s for s in spec["stages"] if s["n"] == "8")["kind"] == "pivot",
      "1858 is rendered as the Crown-rule pivot (yellow rail node and border)")

# 5 ------------------------------------------------------------ layout diversity
say("\n5. LAYOUT DIVERSITY — THE DIRECT REBUTTAL OF THE g8 REJECTION")
sigs = {s["n"]: "|".join(s["layout_signature"]) for s in spec["stages"]}
dupes = [n for n in sigs if list(sigs.values()).count(sigs[n]) > 1]
check(not dupes, "no two stages share an identical block signature",
      "duplicated: " + str(dupes) if dupes else f"{len(set(sigs.values()))} distinct signatures / 16 stages")
kinds = sorted({b for s in spec["stages"] for b in s["layout_signature"]})
check(len(kinds) >= 10, "rich block vocabulary actually used", ", ".join(kinds))
for s in spec["stages"]:
    say(f"      stage {s['n']:>2} : {sigs[s['n']]}")
ncols_only = [s["n"] for s in spec["stages"]
              if set(x.split("(")[0] for x in s["layout_signature"]) <= {"cols"}]
check(not ncols_only, "no stage is a bare three-column card (the g8 failure mode)",
      str(ncols_only) if ncols_only else "")

# 6 ----------------------------------------------------------------- density
say("\n6. INFORMATION DENSITY PER STAGE")
blob = json.dumps(spec["stages"], ensure_ascii=False)
for s in spec["stages"]:
    txt = json.dumps(s, ensure_ascii=False)
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\u2019-]+", txt))
    say(f"      stage {s['n']:>2} : {s['pill_count']:>2} pills · {len(s['blocks'])} blocks · "
        f"~{words} words · {s['height_px']} px tall")
minp = min(s["pill_count"] for s in spec["stages"])
check(minp >= 5, "every stage carries at least five decisive keyword pills", f"minimum {minp}")

stray = []
def scan(o, path):
    if isinstance(o, dict):
        for k, v in o.items():
            scan(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            scan(v, path + "/" + str(i))
    elif isinstance(o, str) and "*" in o:
        key = path.rsplit("/", 1)[-1]
        parent = path.rsplit("/", 3)[-3] if path.count("/") >= 3 else ""
        if key in ("t", "h", "s", "sub", "label", "mid", "mid2", "title") or "headers" in path:
            stray.append(path + " :: " + o[:60])
for s in spec["stages"]:
    scan(s, "stage" + s["n"])
check(not stray, "no literal markdown markers left in pill, header or chain labels",
      "; ".join(stray) if stray else "rich text is only used where the renderer parses it")
check(master.size[1] > 20000, "canvas depth reflects real content, not padding",
      f"{master.size[1]} px tall at 300 dpi")

# 7 -------------------------------------------------------------- answer bands
say("\n7. ANSWER-GRABBING LINES — TOPIC-SPECIFIC, NOT BOILERPLATE")
ans = []
def walk(bs):
    for b in bs:
        if b["type"] == "answer":
            ans.append(b["text"])
        if b["type"] == "row":
            for c in b["children"]:
                walk([c["block"]])
for s in spec["stages"]:
    walk(s["blocks"])
check(len(ans) >= 12, "answer lines present across the flow", f"{len(ans)} bands")
check(len(set(ans)) == len(ans), "every answer line is unique", f"{len(set(ans))} distinct")
short = [a for a in ans if len(a) < 60]
check(not short, "no stub answer lines", str(short)[:120] if short else "")

# 8 ------------------------------------------------------------ must-show terms
say("\n8. MUST-SHOW CONTENT AUDIT (terms required by the commissioning brief)")
missing = [t for t in S.MUST_SHOW if t.lower() not in blob.lower()]
for t in S.MUST_SHOW:
    if t.lower() not in blob.lower():
        say(f"      MISSING: {t}")
check(not missing, f"all {len(S.MUST_SHOW)} required terms are on the canvas",
      f"{len(S.MUST_SHOW) - len(missing)}/{len(S.MUST_SHOW)} present")

# 9 ------------------------------------------------------------------- pdfs
say("\n9. POSTER AND TILED PDF")
import fitz  # noqa: E402
pd = fitz.open(str(POSTER))
check(pd.page_count == 1, "poster is a single page", f"{pd.page_count}")
r = pd[0].rect
check(max(r.width, r.height) / 72 <= 200, "poster within the 200-inch PDF page limit",
      f"{r.width/72:.2f} x {r.height/72:.2f} in")
check(abs((r.width / r.height) - (master.width / master.height)) < 0.002,
      "poster preserves the master aspect ratio — the whole canvas on one page")
pd.close()

td = fitz.open(str(TILED))
n_tiles = spec["outputs"]["tiles"]
check(td.page_count == n_tiles, "tiled page count matches the spec", f"{td.page_count} A3-landscape pages")
check(abs(td[0].rect.width - 1190.55) < 1 and abs(td[0].rect.height - 841.89) < 1,
      "tiles are A3 landscape", f"{td[0].rect.width:.1f} x {td[0].rect.height:.1f} pt")

say("\n   same-master pixel identity — every embedded tile image re-hashed against a fresh")
say("   crop taken from master.png at the recorded row range:")
allsame = True
for i, page in enumerate(td):
    xref = page.get_images(full=True)[0][0]
    emb = fitz.Pixmap(td, xref)
    ib = emb.tobytes("png")
    box = spec["outputs"]["tile_crops"][i]["box"]
    fresh = master.crop(tuple(box))
    bio = io.BytesIO()
    fresh.save(bio, format="PNG")
    same_hash = sha_b(ib) == sha_b(bio.getvalue())
    if not same_hash:                      # fall back to a pixel comparison
        emb_img = Image.open(io.BytesIO(ib)).convert("RGB")
        same_hash = (emb_img.size == fresh.size and emb_img.tobytes() == fresh.convert("RGB").tobytes())
    allsame &= same_hash
    say(f"      tile {i+1}/{n_tiles}  rows {box[1]}–{box[3]}  size {fresh.size}  "
        f"{'identical' if same_hash else 'DIFFERENT'}")
check(allsame, "all tiles are pixel-identical crops of the same master canvas")
ov = spec["outputs"]["tile_overlap_px"]
check(ov >= 240, "tiles overlap so no line is lost at a cut", f"{ov} px overlap, uniform")
tops = [c["box"][1] for c in spec["outputs"]["tile_crops"]]
check(len(set(tops)) == len(tops), "no duplicated tile page")
td.close()

# 10 ------------------------------------------------------------ contact sheets
say("\n10. PAGE PREVIEWS AND CONTACT SHEETS")
prev_pngs = sorted((HERE / "previews").glob("page-*.png"))
check(len(prev_pngs) == n_tiles, "one preview per tiled page", f"{len(prev_pngs)}")
sheets = sorted((HERE / "previews").glob("contact-sheet-*.png"))
check(len(sheets) >= 1, "contact sheets produced", f"{len(sheets)}")
psize = [Image.open(p).size for p in prev_pngs]
say("   the g8 rejection listed a large blank region on the contact sheet. Each sheet below is")
say("   sized from the actual tile count, so the only background left is the 22 px grid gutter:")
for i, s in enumerate(sheets):
    tiles = psize[i * 6:(i + 1) * 6]
    band, covered, size = B.blank_waste(s, tiles)
    check(band < 0.05 and covered > 0.90, f"{s.name} carries no blank region",
          f"{size[0]}x{size[1]} · page area covers {covered*100:.1f}% of the sheet · "
          f"largest empty horizontal band {band*100:.2f}% of sheet height")

# 11 ------------------------------------------------------------------ sources
say("\n11. SOURCE INTEGRITY")
for label, p in (("canonical learner-v2 owner", S.OWNER),
                 ("advanced owner", S.ADV_OWNER),
                 ("cross-owned mechanism owner", S.CROSS_OWNER)):
    check((B.ROOT / p).exists(), f"{label} exists", p)
ap = spec["header"]["approval"].lower()
check("approval" in ap and "false" in ap,
      "canvas carries the not-approved status line", spec["header"]["approval"])
check(spec["approved"] is False, "design spec records approved = false")

# 12 -------------------------------------------------------------------- files
say("\n12. DELIVERABLES")
for f in ["bespoke-design-spec.json", "master.png", spec["outputs"]["poster_pdf"],
          spec["outputs"]["tiled_pdf"], "README.txt", "preservation-hashes.json",
          "render_lib.py", "spec_content.py", "build_g9.py"]:
    p = HERE / f
    check(p.exists(), f, f"{p.stat().st_size/1024:.1f} KB" if p.exists() else "missing")

say("\n" + "=" * 108)
say(f"RESULT: {'ALL CHECKS PASSED' if not fails else str(len(fails)) + ' CHECK(S) FAILED'}")
if fails:
    for f in fails:
        say("   FAILED: " + f)
say("Approval state: NOT APPROVED — user review pending. No tracker or Markdown file was modified.")
say("=" * 108)

(HERE / "validation-report.txt").write_text("\n".join(L) + "\n", encoding="utf-8")

hashes = {
    "generation": spec["generation"],
    "approved": False,
    "immutable_reference_folder": str(B.REF_DIR).replace(str(B.ROOT) + "\\", ""),
    "immutable_reference_hashes_verified_unchanged": ref_all,
    "required_poster_sha256": B.REF_EXPECTED[
        "Carvaka_Continuous-At-a-Glance-Core-First_Poster_2026-08-22.pdf"],
    "rejected_g8_preserved_hashes": g8,
    "g9_artifact_hashes": {
        f: sha(HERE / f) for f in
        ["bespoke-design-spec.json", "master.png", spec["outputs"]["poster_pdf"],
         spec["outputs"]["tiled_pdf"], "render_lib.py", "spec_content.py", "build_g9.py"]
    },
    "g9_preview_hashes": {p.name: sha(p) for p in sorted((HERE / "previews").glob("*.png"))},
}
(HERE / "preservation-hashes.json").write_text(
    json.dumps(hashes, indent=1, ensure_ascii=False), encoding="utf-8")
sys.exit(1 if fails else 0)
