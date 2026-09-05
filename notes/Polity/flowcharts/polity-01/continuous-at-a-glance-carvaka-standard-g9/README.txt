POLITY 01 — HISTORICAL BACKGROUND OF THE INDIAN CONSTITUTION
CONTINUOUS AT-A-GLANCE MASTER FLOW · GENERATION g9 (Carvaka standard)
=============================================================================================

STATUS
  NOT APPROVED. Generated for user review. No approval flag has been set anywhere, and no
  Markdown, learning-session PDF, workbook or tracker file was created or modified by this
  build. Everything in this folder is new and self-contained.

WHY g9 EXISTS
  Generation g8 (../continuous-at-a-glance-carvaka-standard-g8/) was rejected. Its faults were
  specific and structural, not cosmetic:
      - every stage used the identical three-column CONTROL / FUNCTION / CONSEQUENCE card;
      - too little content per stage;
      - no internal branching and no adjacent institutional contrasts;
      - superficial keyword pills;
      - insufficient mechanism detail;
      - a contact sheet with a large blank region.
  g8 has been left completely untouched for traceability and is hashed in
  preservation-hashes.json and build-audit.json before and after this build.

  g9 is not a re-colouring of g8. The stage structure was hand-authored from scratch, stage by
  stage, so that the internal layout of each stage is chosen to fit that stage's argument.

THE IMMUTABLE DESIGN REFERENCE
  notes\Philosophy\flowcharts\philosophy-paper-i-indian-philosophy-01\continuous-at-a-glance-core-first\
  This folder is read-only for every purpose. It was opened, hashed and studied; nothing in it
  was written. Its poster SHA-256 is re-verified on every validation run:
      F291DDE859557D822B91902027B070BB649E92F20C52E9031B1521A9DDE16D90

  What was matched from it — the design intelligence, not a template:
      4800 px wide master at 300 dpi; a strong title card with legend chips and a reading rule;
      a numbered continuous rail with a node and a connector per stage; a genuinely different
      internal layout inside each stage; dense rows of decisive keyword pills; multi-column
      branches and direct institutional comparisons; compact high-information bullets;
      mechanism and bridge bands; a magenta answer-grabbing line; a complete numbered core
      before a visually subordinate enrichment card; a final synthesis stage carrying the
      comparison matrix and the PYQ routes; a poster that keeps the whole canvas on one page
      and a tiled PDF that crops the very same canvas with overlap.

WHAT IS ON THE CANVAS
  Sixteen stages, each with its own layout grammar:

     0  identity and source caution ................ columns + terminology matrix + caution band
     1  pre-1773 corporate state ................... eight-node causal chain + three-way branch
     2  Regulating Act 1773 ........................ build-versus-defect panels + mechanism band
     3  Settlement Act 1781 ........................ four-row repair matrix + bridge band
     4  Pitt's India Act 1784 and the Act of 1786 .. Board of Control vs Court of Directors
                                                     institutional split + transmission chain
     5  Charter Acts 1793 and 1813 ................. 1793-versus-1813 comparison matrix
     6  Charter Act 1833 ........................... before/after replacement + PYQ band
     7  Charter Act 1853 ........................... five-step institutional ladder
     8  Government of India Act 1858 (PIVOT) ....... abolished/created replacement diagram +
                                                     six-node imperial accountability chain
     9  Councils Acts 1861 and 1892 ................ association-versus-scrutiny matrix
    10  Morley-Minto 1909 .......................... separate electorate vs reserved seat panels
    11  Government of India Act 1919 ............... reserved-versus-transferred panels +
                                                     Simon-to-1935 timeline bridge
    12  Government of India Act 1935 ............... commenced-versus-not-commenced matrix
    13  Indian Independence Act 1947 ............... dated timeline + ended/created/lapsed columns
    14  exam synthesis ............................. ten-node spine chain + four-question
                                                     comparison matrix + trap ledger + FIRSTS
     E  subordinate enrichment ..................... grey, last, explicitly optional

  Colour key used on the canvas:
      AMBER heading   = sourced statutory provision
      CYAN heading    = mechanism and analysis
      RED heading     = defect, limit or trap
      GREEN / TEAL    = what a statute created or conceded
      MAGENTA band    = answer-grabbing line, written to be copied into an answer
      YELLOW border   = the 1858 Crown-rule pivot
      GREY border     = subordinate enrichment

SOURCES — NOTHING IS INVENTED
  Primary owner (canonical learner-v2):
    upsc-ai-kit\knowledge\Polity\learning-sessions\v2\
      subject-wide-syllabus-core-first-g3-core-first-g4-core-first-g5-core-first-g6-core-first-g7\
      polity-01_Learning-Session.md
  Advanced owner:
    the Advanced Layer sections of the same learner-v2 document.
  Cross-owned mechanism detail (1773 council deadlock, the Supreme Court jurisdiction cases,
  the exact 1781 repairs, the wording of the Board of Control's power and the Secret Committee
  transmission channel):
    upsc-ai-kit\knowledge\Modern-Indian-History\
      06_Structure-of-Government-and-Constitutional-Development-1757-1858_Complete-Topic-Package.md
  Where the local corpus is silent or divided, the canvas says so on the card rather than
  filling the gap. See the source-caution bands in stages 0, 5, 12 and E.

FILES
  bespoke-design-spec.json .... the full hand-authored design and content spec: canvas metrics,
                               palette, block vocabulary, and every stage with its layout
                               signature, pills and blocks. This is the thing that is bespoke.
  master.png .................. 4800 px wide, 300 dpi master canvas.
  Polity01_..._Poster_*.pdf ... one page, the entire canvas, inside the 200-inch page limit.
  Polity01_..._Tiled_*.pdf .... A3 landscape tiles cropped from the very same master canvas
                               with a uniform overlap, each footed with its row range and a
                               continuation note. Validated as pixel-identical to the master.
  previews\page-*.png ......... one preview per tiled page.
  previews\contact-sheet-*.png  exact-fit grids of those previews. Sheet size is computed from
                               the actual number of tiles, so there is no blank region.
  validation-report.txt ....... the full check log, including the immutability re-verification.
  preservation-hashes.json .... reference hashes, preserved g8 hashes, and g9 artifact hashes.
  build-audit.json ............ before/after hashes captured by the build itself, plus the
                               renderer's overflow log.
  render_lib.py ............... reusable rendering primitives (text engine, pills, chains,
                               panels, replacement diagrams, matrices, timelines, ladders,
                               bands, answer lines, side-by-side rows).
  spec_content.py ............. the hand-authored Polity 01 stage content.
  build_g9.py / validate_g9.py  build and validation entry points.

HOW TO REBUILD
      python build_g9.py
      python validate_g9.py
  build_g9.py is deterministic: it re-measures every block, lays the canvas out in two passes
  and fails loudly through the overflow log if any text does not fit.

HOW TO READ IT
  Follow the thick cyan rail from stage 0 to stage 14 without skipping. The rail is the
  argument: Company trade -> parliamentary regulation -> dual control -> Crown rule ->
  association -> representation -> provincial responsibility -> federal and autonomy
  architecture -> sovereignty. Read the grey enrichment card only after the core is secure.
