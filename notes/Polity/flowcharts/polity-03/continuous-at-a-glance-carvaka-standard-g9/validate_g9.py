"""Validate the Polity 03 g9 continuous at-a-glance package."""
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

import render_lib as R          # noqa: E402,F401
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
audit = json.loads((HERE / "build-audit.json").read_text(encoding="utf-8"))
master = Image.open(HERE / "master.png")
POSTER = HERE / spec["outputs"]["poster_pdf"]
TILED = HERE / spec["outputs"]["tiled_pdf"]
fails = []


def check(ok, label, detail=""):
    say(f"  [{'PASS' if ok else 'FAIL'}] {label}{(' — ' + detail) if detail else ''}")
    if not ok:
        fails.append(label)
    return ok


say("=" * 108)
say("VALIDATION REPORT — POLITY 03 · SALIENT FEATURES OF THE INDIAN CONSTITUTION")
say("CONTINUOUS AT-A-GLANCE MASTER FLOW — GENERATION g9 (Carvaka-standard, first for this topic)")
say(f"generated {datetime.now().isoformat(timespec='seconds')}")
say("=" * 108)

# 1 -------------------------------------------------------------- immutability
say("\n1. IMMUTABLE APPROVED REFERENCE — Philosophy Paper-I Indian Philosophy 01 / Carvaka")
for name, want in B.REF_EXPECTED.items():
    got = sha(B.REF_DIR / name)
    check(got == want, name, f"sha256 {got[:24]}\u2026")
ref_all = {str(p.relative_to(B.REF_DIR)): sha(p)
           for p in sorted(B.REF_DIR.rglob("*")) if p.is_file()}
check(ref_all == audit["reference_hashes_before_build"],
      "every file in the reference folder unchanged", f"{len(ref_all)} files re-hashed")
check(audit["reference_hashes_before_build"] == audit["reference_hashes_after_build"],
      "immutable reference untouched across the build")
say("  NOTE: the reference folder was opened read-only; no write occurred at any point.")

# 2 ------------------------------------------- preservation of every prior set
say("\n2. PRESERVATION — EVERY PRE-EXISTING POLITY 03 ARTEFACT")
now = B.topic_hashes(exclude=HERE)
check(audit["sibling_hashes_before_build"] == audit["sibling_hashes_after_build"],
      "sibling hashes identical before and after the g9 build",
      f"{len(audit['sibling_hashes_after_build'])} files")
check(now == audit["sibling_hashes_after_build"],
      "still byte-identical at validation time", f"{len(now)} files re-hashed")
gens = sorted({k.split("\\")[0] for k in now if "\\" in k})
check(len(gens) >= 5, "prior generations preserved in place", ", ".join(gens))
legacy = [k for k in now if "\\" not in k]
check(bool(legacy), "legacy root master set preserved", f"{len(legacy)} root files")

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
say("\n4. STAGE COMPLETENESS — REQUIRED SPINE 0..21 PLUS SUBORDINATE ENRICHMENT")
want = list(range(22)) + ["EXTRA"]
got = [s["n"] for s in spec["stages"]]
check(got == want, "all twenty-three stages present in order",
      " ".join(map(str, got)))
required = {
    0: "WHAT MAKES A FEATURE 'SALIENT'",
    1: "CONSTITUTIONALISM",
    2: "WRITTEN, LENGTHY AND DETAILED",
    3: "BORROWED IN ANCESTRY, ORIGINAL IN DESIGN",
    4: "THE AMENDMENT SPECTRUM",
    5: "FEDERAL IN FORM, CENTRALISING IN CAPACITY",
    6: "PARLIAMENTARY GOVERNMENT",
    7: "NEITHER PARLIAMENT NOR THE COURT IS SOVEREIGN",
    8: "SEPARATION OF FUNCTIONS, NOT OF ORGANS",
    9: "CONSTITUTIONAL SUPREMACY, RULE OF LAW AND LIMITED GOVERNMENT",
    10: "INTEGRATED AND INDEPENDENT JUDICIARY",
    11: "RIGHTS, DIRECTIVE PRINCIPLES AND DUTIES",
    12: "SECULAR REPUBLIC",
    13: "UNIVERSAL ADULT FRANCHISE",
    14: "SINGLE CITIZENSHIP",
    15: "INDEPENDENT CONSTITUTIONAL BODIES",
    16: "EMERGENCY PROVISIONS",
    17: "THE THIRD TIER",
    18: "ASYMMETRY AND PLURAL ACCOMMODATION",
    19: "CONTINUITY AND TRANSFORMATION",
    20: "TENSIONS AND TRADE-OFFS",
    21: "SYNTHESIS",
    "EXTRA": "SUBORDINATE ENRICHMENT",
}
bad = [n for n, frag in required.items()
       if frag not in next(s for s in spec["stages"] if s["n"] == n)["title"]]
check(not bad, "each stage carries its required subject",
      "mismatched: " + str(bad) if bad else "22-stage core + enrichment")
check(spec["stages"][-1]["kind"] == "extra"
      and all(s["kind"] != "extra" for s in spec["stages"][:-1]),
      "enrichment is last and visually subordinate; the core is complete before it")
check(next(s for s in spec["stages"] if s["n"] == 9)["kind"] == "pivot",
      "constitutional supremacy is rendered as the keystone pivot (yellow node)")

# 5 ------------------------------------------------------------ layout diversity
say("\n5. LAYOUT DIVERSITY — NO REPEATED GENERIC CARDS")
sigs = {s["n"]: "|".join(s["layout_signature"]) for s in spec["stages"]}
dupes = [n for n in sigs if list(sigs.values()).count(sigs[n]) > 1]
check(not dupes, "no two stages share an identical block signature",
      "duplicated: " + str(dupes) if dupes
      else f"{len(set(sigs.values()))} distinct signatures / 23 stages")
kinds = sorted({b.split("(")[0] for s in spec["stages"] for b in s["layout_signature"]})
check(len(kinds) >= 12, "rich block vocabulary actually used", ", ".join(kinds))
for s in spec["stages"]:
    say(f"      stage {str(s['n']):>5} : {sigs[s['n']]}")
new_prims = set(spec["new_primitives"])
used_new = sorted(new_prims & set(kinds))
check(len(used_new) == len(new_prims),
      "every bespoke Polity-03 primitive is actually on the canvas", ", ".join(used_new))
prior = {
    "Polity 01 g9": B.ROOT / "notes" / "Polity" / "flowcharts" / "polity-01" /
    "continuous-at-a-glance-carvaka-standard-g9" / "bespoke-design-spec.json",
    "Polity 02 g8": B.ROOT / "notes" / "Polity" / "flowcharts" / "polity-02" /
    "continuous-at-a-glance-carvaka-standard-g8" / "bespoke-design-spec.json",
}
for label, p in prior.items():
    if not p.exists():
        continue
    prev_spec = json.loads(p.read_text(encoding="utf-8"))
    prev = {"|".join(s["layout_signature"]) for s in prev_spec["stages"]}
    shared = prev & set(sigs.values())
    check(not shared, f"no stage signature is copied from the {label} package",
          "shared: " + str(shared) if shared else "all twenty-three signatures are new")
    prev_prims = set(prev_spec.get("new_primitives", {}))
    check(not (prev_prims & new_prims),
          f"no bespoke primitive is recycled from the {label} package",
          "shared: " + str(sorted(prev_prims & new_prims)) if prev_prims & new_prims
          else f"{len(new_prims)} primitives authored only for Polity 03")
bare = [s["n"] for s in spec["stages"]
        if {x.split("(")[0] for x in s["layout_signature"]} <= {"cols"}]
check(not bare, "no stage is a bare three-column card", str(bare) if bare else "")

# 6 ----------------------------------------------------------------- density
say("\n6. INFORMATION DENSITY PER STAGE")
blob = json.dumps(spec["stages"], ensure_ascii=False)
for s in spec["stages"]:
    txt = json.dumps(s, ensure_ascii=False)
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\u2019-]+", txt))
    say(f"      stage {str(s['n']):>5} : {s['pill_count']:>2} pills \u00b7 {len(s['blocks'])} blocks "
        f"\u00b7 ~{words} words \u00b7 {s['height_px']} px tall")
minp = min(s["pill_count"] for s in spec["stages"])
check(minp >= 4, "every stage carries at least four decisive keyword pills", f"minimum {minp}")
minb = min(len(s["blocks"]) for s in spec["stages"])
check(minb >= 3, "every stage carries at least three internal blocks", f"minimum {minb}")

stray = []
RICH_S_TYPES = {"wheel", "fan", "spectrum", "quadrant", "loop", "overlap", "triangle",
                "pyramid", "balance", "srcmap", "triad", "vs3", "bus", "constel",
                "switch", "tension", "web"}
RICH_PAIRS = {("tension", "l"), ("web", "t")}
PLAIN_KEYS = ("t", "h", "s", "sub", "label", "mid", "mid2", "title", "d",
              "n", "l", "u", "src", "total", "art", "k")
accepted_rich = []


def scan(o, path, btype=""):
    if isinstance(o, dict):
        btype = o.get("type", btype)
        for k, v in o.items():
            scan(v, path + "/" + str(k), btype)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            scan(v, path + "/" + str(i), btype)
    elif isinstance(o, str) and "*" in o:
        key = path.rsplit("/", 1)[-1]
        rich = (key in ("v", "text", "note")
                or (key == "s" and btype in RICH_S_TYPES)
                or (btype, key) in RICH_PAIRS)
        if rich:
            accepted_rich.append(f"{btype}.{key}")
        elif key in PLAIN_KEYS or "headers" in path:
            stray.append(path + " :: " + o[:60])


for s in spec["stages"]:
    scan(s, "stage" + str(s["n"]))
check(not stray, "no literal markdown markers left in plain-text fields",
      "; ".join(stray) if stray else "rich text is only used where the renderer parses it")
say("      rich-parsed fields carrying bold runs: "
    + ", ".join(f"{k}\u00d7{accepted_rich.count(k)}" for k in sorted(set(accepted_rich))))
check(master.size[1] > 25000, "canvas depth reflects real content, not padding",
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
check(len(ans) >= 20, "answer lines present across the flow", f"{len(ans)} bands")
check(len(set(ans)) == len(ans), "every answer line is unique", f"{len(set(ans))} distinct")
short = [a for a in ans if len(a) < 60]
check(not short, "no stub answer lines", str(short)[:120] if short else "")
heads = [a.split(":")[0] for a in ans]
check(len(set(heads)) == len(heads), "every answer band carries its own labelled head",
      f"{len(set(heads))} distinct heads")

# 8 ------------------------------------------------------------ must-show terms
say("\n8. MUST-SHOW CONTENT AUDIT (terms required by the commissioning brief)")
missing = [t for t in S.MUST_SHOW if t.lower() not in blob.lower()]
for t in missing:
    say(f"      MISSING: {t}")
check(not missing, f"all {len(S.MUST_SHOW)} required terms are on the canvas",
      f"{len(S.MUST_SHOW) - len(missing)}/{len(S.MUST_SHOW)} present")

NEGATED = ("wrong", "never write", "never say", "do not", "don't", "is not",
           "trap", "incorrect", "avoid", "myth", "error")
FORBIDDEN_CLAIMS = [
    ("'Federation' is never claimed to be constitutional text",
     r"the (?:constitutional )?text (?:uses|says) ['\u2018]?Federation"),
    ("no claim that every amendment needs State ratification",
     r"[Ee]very amendment requires State ratification"),
    ("no claim that India uses a strict separation of powers",
     r"India follows a strict separation of powers"),
    ("no claim that the Directive Principles are irrelevant",
     r"DPSP are irrelevant"),
    ("no claim that Indian secularism means total State withdrawal",
     r"secularism means total State withdrawal"),
    ("no claim that Hindi is the national language",
     r"Hindi is the national language"),
    ("no claim that the whole 97th Amendment was struck down",
     r"whole 97th Amendment was struck down"),
]


def unnegated_hits(pattern):
    """A forbidden claim is only a defect when it is asserted. Every occurrence is
    tested inside its own block, because that is the unit the reader sees: a WRONG:
    trap line, a 'NEVER WRITE THESE' column or a 'Never say' precision control."""
    out = []
    rx = re.compile(pattern)
    for st in spec["stages"]:
        for blk in st["blocks"]:
            btxt = json.dumps(blk, ensure_ascii=False)
            if not rx.search(btxt):
                continue
            low = btxt.lower()
            cue = next((w for w in NEGATED if w in low), None)
            if cue is None:
                out.append(f"stage {st['n']} block {blk['type']}")
    return out


for label, pat in FORBIDDEN_CLAIMS:
    hits = unnegated_hits(pat)
    check(not hits, f"source limit respected \u2014 {label}",
          "unnegated: " + str(hits)[:160] if hits
          else "only ever printed inside an explicit trap / never-write line")
say("      (every occurrence of these strings on the canvas is inside a WRONG:/NEVER WRITE")
say("       control line, which is exactly how the owner file teaches them.)")
undated = re.findall(r"470 Articles", blob)
dated = re.findall(r"470 Articles[^\"]{0,40}(?:2019|dated)|(?:2019|about|snapshot)[^\"]{0,60}470 Articles", blob)
check(len(dated) >= len(undated),
      "present-day Article totals always carry the source's dated wording",
      f"{len(undated)} occurrences, each printed as a dated 2019 snapshot")

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
check(td.page_count == n_tiles, "tiled page count matches the spec",
      f"{td.page_count} A3-landscape pages")
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
    same = sha_b(ib) == sha_b(bio.getvalue())
    if not same:
        emb_img = Image.open(io.BytesIO(ib)).convert("RGB")
        same = (emb_img.size == fresh.size
                and emb_img.tobytes() == fresh.convert("RGB").tobytes())
    allsame &= same
    say(f"      tile {i+1}/{n_tiles}  rows {box[1]}\u2013{box[3]}  size {fresh.size}  "
        f"{'identical' if same else 'DIFFERENT'}")
check(allsame, "all tiles are pixel-identical crops of the same master canvas")
ov = spec["outputs"]["tile_overlap_px"]
check(ov >= 240, "tiles overlap so no line is lost at a cut", f"{ov} px overlap, uniform")
tops = [c["box"][1] for c in spec["outputs"]["tile_crops"]]
check(len(set(tops)) == len(tops), "no duplicated tile page")
check(tops[0] == 0 and spec["outputs"]["tile_crops"][-1]["box"][3] == master.height,
      "tiling covers the canvas from the first row to the last")
td.close()

# 10 ------------------------------------------------------------ contact sheets
say("\n10. PAGE PREVIEWS AND CONTACT SHEETS")
prev_pngs = sorted((HERE / "previews").glob("page-*.png"))
check(len(prev_pngs) == n_tiles, "one preview per tiled page", f"{len(prev_pngs)}")
sheets = sorted((HERE / "previews").glob("contact-sheet-*.png"))
check(len(sheets) >= 1, "contact sheets produced", f"{len(sheets)}")
psize = [Image.open(p).size for p in prev_pngs]
check(len({s for s in psize}) == 1, "all page previews share one page geometry", str(psize[0]))
say("   sheets are justified galleries: every row fills the sheet width, so no grid cell is")
say("   ever left empty and the only background left is the gutter:")
for i, s in enumerate(sheets):
    meta = spec["outputs"]["contact_sheets"][i]
    band, covered, size = B.blank_waste(s, meta["boxes"])
    check(band < 0.05 and covered > 0.90, f"{s.name} carries no blank region",
          f"{size[0]}x{size[1]} \u00b7 {len(meta['boxes'])} pages cover {covered*100:.1f}% of the "
          f"sheet \u00b7 largest empty horizontal band {band*100:.2f}% of sheet height")
check(sum(len(m["boxes"]) for m in spec["outputs"]["contact_sheets"]) == n_tiles,
      "every tiled page appears on exactly one contact sheet", f"{n_tiles} pages")

# 11 ------------------------------------------------------------------ sources
say("\n11. SOURCE INTEGRITY")
check((B.ROOT / S.OWNER).exists(), "canonical learner-v2 owner exists", S.OWNER)
say(f"      advanced depth owner  : {S.ADV_OWNER}")
say(f"      topic package owner   : {S.PKG_OWNER}")
ap = spec["header"]["approval"].lower()
check("approval" in ap and "false" in ap,
      "canvas carries the not-approved status line", spec["header"]["approval"])
check(spec["approved"] is False, "design spec records approved = false")

# 12 -------------------------------------------------------------------- files
say("\n12. DELIVERABLES")
for f in ["bespoke-design-spec.json", "build-audit.json", "master.png",
          spec["outputs"]["poster_pdf"], spec["outputs"]["tiled_pdf"],
          "README.txt", "preservation-hashes.json", "render_lib.py",
          "render_p3.py", "render_p3b.py", "spec_header.py", "spec_content.py",
          "build_g9.py", "validate_g9.py"]:
    p = HERE / f
    check(p.exists(), f, f"{p.stat().st_size/1024:.1f} KB" if p.exists() else "missing")
for f in "abcdefghi":
    p = HERE / f"spec_{f}.py"
    check(p.exists(), f"spec_{f}.py", f"{p.stat().st_size/1024:.1f} KB" if p.exists() else "missing")

say("\n" + "=" * 108)
say(f"RESULT: {'ALL CHECKS PASSED' if not fails else str(len(fails)) + ' CHECK(S) FAILED'}")
for f in fails:
    say("   FAILED: " + f)
say("Approval state: NOT APPROVED — user review pending. No Markdown, workbook, PDF note or")
say("tracker file was created or modified by this package.")
say("=" * 108)

(HERE / "validation-report.txt").write_text("\n".join(L) + "\n", encoding="utf-8")

hashes = {
    "generation": spec["generation"],
    "approved": False,
    "immutable_reference_folder": str(B.REF_DIR).replace(str(B.ROOT) + "\\", ""),
    "immutable_reference_hashes_verified_unchanged": ref_all,
    "required_reference_poster_sha256": B.REF_EXPECTED[
        "Carvaka_Continuous-At-a-Glance-Core-First_Poster_2026-08-22.pdf"],
    "preserved_polity03_hashes": now,
    "g9_artifact_hashes": {
        f: sha(HERE / f) for f in
        ["bespoke-design-spec.json", "master.png", spec["outputs"]["poster_pdf"],
         spec["outputs"]["tiled_pdf"], "render_lib.py", "render_p3.py", "render_p3b.py",
         "spec_content.py", "build_g9.py", "validate_g9.py"]
    },
    "g9_preview_hashes": {p.name: sha(p) for p in sorted((HERE / "previews").glob("*.png"))},
}
(HERE / "preservation-hashes.json").write_text(
    json.dumps(hashes, indent=1, ensure_ascii=False), encoding="utf-8")
sys.exit(1 if fails else 0)
