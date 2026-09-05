================================================================================================
POLITY 02 — MAKING OF THE CONSTITUTION
CONTINUOUS AT-A-GLANCE MASTER FLOW — GENERATION g8 (Carvaka-standard)
================================================================================================

STATUS
    approved = FALSE. Pending user review. Nothing in this folder has been registered as
    approved, and no tracker, Markdown, note-PDF or workbook file was created or modified.

WHY THE FOLDER IS CALLED g8
    g8 is simply the next free generation index inside notes/Polity/flowcharts/polity-02,
    which already held continuous-at-a-glance-core-first g3, g4, g5, g6 and g7 plus the
    2026-08-21 legacy master set. This is the FIRST Carvaka-standard generation for Polity 02.
    It has nothing to do with the rejected Polity 01 g8 — that was a different topic folder.
    Every pre-existing Polity 02 artefact is preserved byte-identically; the build hashes the
    whole topic tree before and after itself and the validator re-hashes it independently.

WHAT THIS PACKAGE IS
    One continuous poster. A single 4800 px wide, 300 dpi canvas carries a numbered rail from
    the prehistory of the demand in 1934 to the commencement of the Constitution on
    26 January 1950, followed by a visually subordinate enrichment band.

    Seventeen numbered core stages, then EXTRA:
        0   Identity and metric discipline — this is constituent authority, not a list of dates
        1   Prehistory of the demand, 1934-1946 — from radical proposal to accepted principle
        2   Cabinet Mission Plan 1946 — the legal design and the allocation arithmetic
        3   The selection chain — how a Constituent Assembly seat was actually filled
        4   Composition ledger — 389 planned to 299 after Partition, category logic intact
        5   Elections of July-August 1946 and the legitimacy nuance
        6   First sitting, 9 December 1946 — officers, secretariat and the production chain
        7   Objectives Resolution to Preamble — values fixed before the clauses
        8   PIVOT — Indian Independence Act 1947: the Assembly becomes sovereign
        9   Committee architecture — specialisation, reporting and Assembly control
        10  B.N. Rau versus the Drafting Committee — research is not drafting
        11  Drafts, public comment and the three readings — where the text was actually made
        12  Adoption, signing and commencement — three distinct constitutional events
        13  Time, sittings, cost, other functions and constitutional craft
        14  Representativeness — criticism versus evidence-led reply, with the residue kept
        15  Borrowed provisions as adaptation — source, feature, Indian transformation
        16  Synthesis — the answer spine, PYQ routes and the graded verdict
        E   Subordinate enrichment — optional advanced depth, only after the core is secure

HOW IT MEETS THE CARVAKA STANDARD
    The immutable approved reference is
        notes/Philosophy/flowcharts/philosophy-paper-i-indian-philosophy-01/
        continuous-at-a-glance-core-first/
    It was opened read-only. Its poster SHA-256 is still
        F291DDE859557D822B91902027B070BB649E92F20C52E9031B1521A9DDE16D90
    and every file in that folder is re-hashed by the validator.

    Matched properties: 4800 px / 300 dpi master; strong title card with legend chips and a
    reading instruction; numbered continuous rail with per-stage nodes and connectors; a layout
    chosen individually for each stage rather than one repeated card schema; dense decisive
    keyword pill rows; multi-column branches and direct institutional comparisons; compact
    high-information bullets; mechanism, bridge, caution and trap bands; a magenta
    answer-grabbing line unique to every stage; a complete numbered core before a visually
    subordinate enrichment band; a final synthesis stage with an answer spine, routed PYQs and
    a trap sweep; a poster that keeps the whole canvas and a tiled PDF that crops the same
    canvas with overlap.

    Reused from the approved Polity 01 g9 package: rendering primitives only (render_lib.py).
    No stage structure, no layout signature and no sentence of content was carried across.
    All eighteen block signatures here are new, and the validator proves that none of them
    matches a Polity 01 g9 signature.

BESPOKE PRIMITIVES WRITTEN FOR THIS TOPIC (render_ext.py)
    dash      big-number metric dashboard cells (389 / 296 / 211 / 299 / 284, and the
              time-cost-sittings dashboard)
    alloc     proportional seat-allocation diagram with a bus line and weighted parts
    funnel    narrowing legitimacy and selection funnel, adult population to seated member
    hub       central institution with left and right officer-role spokes
    tree      root-and-branch committee architecture with leaf cards
    pipeline  dated multi-stage drafting and reading pipeline
    adapt     three-column source-family / feature / Indian-adaptation map

SOURCES
    Every fact comes from locally owned material. The canonical owner is the Polity 02
    learner-v2 Markdown listed in bespoke-design-spec.json under "sources". Nothing was
    invented. Where a PYQ key is unavailable or provisional locally, the canvas says so, and
    the absence of a directly attributable Mains PYQ is stated rather than filled.

    Deliberate source limits shown on the canvas: the four Chief Commissioners' provinces are
    counted but never named; princely-state seats are described as filled by nomination, not by
    popular election; proposed and moved/disposed amendment counts are kept apart; criticism of
    the Assembly is paraphrased, never quoted from an unverified wording.

FILES
    master.png                                  4800 x 30422 px, 300 dpi
    Polity02_..._g8_Poster_<date>.pdf           one page, whole canvas, within the 200 in limit
    Polity02_..._g8_Tiled_<date>.pdf            11 A3-landscape pages, same master, 240 px overlap
    previews/page-001..011.png                  one preview per tiled page
    previews/contact-sheet-01..02.png           justified galleries, no empty grid cell
    bespoke-design-spec.json                    full design record: canvas, palette, typography,
                                                per-stage layout signature, pills and blocks
    build-audit.json                            overflow log and before/after preservation hashes
    validation-report.txt                       the validator's own output
    preservation-hashes.json                    reference, sibling and artefact hashes

REPRODUCING
    cd notes/Polity/flowcharts/polity-02/continuous-at-a-glance-carvaka-standard-g8
    set PYTHONIOENCODING=utf-8
    python build_g8.py         rebuilds master, poster, tiles, previews, contact sheets, spec
    python validate_g8.py      re-runs all twelve validation sections and rewrites the report

    Build inputs: render_lib.py (engine), render_ext.py (this topic's primitives),
    spec_header.py and spec_a.py .. spec_h.py (the authored content), spec_content.py
    (assembles the stages and the must-show term list).

================================================================================================
