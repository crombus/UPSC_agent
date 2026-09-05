POLITY 03 — SALIENT FEATURES OF THE INDIAN CONSTITUTION
CONTINUOUS AT-A-GLANCE MASTER FLOW · GENERATION g9 · CARVAKA-STANDARD
================================================================================

STATUS: NOT APPROVED — user review pending. `approved` is false in
bespoke-design-spec.json and the canvas prints "APPROVAL: FALSE" in its header.

WHAT THIS IS
--------------------------------------------------------------------------------
One continuous, numbered, top-to-bottom master flow for the whole topic. It is a
single canvas, not a deck: every stage hangs off one vertical rail, and every
stage was authored individually. There is no repeated card schema. The design
target is the immutable approved reference poster:

  notes\Philosophy\flowcharts\philosophy-paper-i-indian-philosophy-01\
      continuous-at-a-glance-core-first\
      Carvaka_Continuous-At-a-Glance-Core-First_Master.png

That folder is read-only for this build. Its poster SHA-256 must remain
F291DDE859557D822B91902027B070BB649E92F20C52E9031B1521A9DDE16D90 and the
validator re-hashes every file in it before and after the build.

THE SPINE (23 stages: 0–21 core, then subordinate enrichment)
--------------------------------------------------------------------------------
   0  what makes a feature 'salient' — a system property, not a memorised list
   1  Constitution -> constitutional law -> constitutionalism
   2  written, lengthy and detailed — four causes, one accommodation device
   3  borrowed in ancestry, original in design — taken, adapted, rejected
   4  the amendment spectrum — graded flexibility under a basic-structure ceiling
   5  federal in form, centralising in capacity, cooperative and asymmetric
   6  parliamentary government — the unbroken accountability loop
   7  neither Parliament nor the Court is sovereign — the Indian synthesis
   8  separation of functions, not of organs — overlap plus reciprocal checks
   9  KEYSTONE PIVOT: constitutional supremacy, rule of law, limited government
  10  an integrated and independent judiciary — one hierarchy, two bodies of law
  11  rights, Directive Principles and duties — three legal statuses
  12  secular republic — principled state engagement between two rejected extremes
  13  universal adult franchise — equal political membership from commencement
  14  the integration bus — single citizenship and the devices that hold a plural federation
  15  independent constitutional bodies — integrity functions outside ordinary control
  16  emergency provisions — a constitutional switch between normal and exception
  17  the third tier and constitutionalised cooperatives
  18  asymmetry and plural accommodation
  19  continuity and transformation — colonial machinery, republican legitimacy
  20  tensions and trade-offs — six fault lines and the graded verdict
  21  synthesis — how the features interact, the answer spine, the PYQ routes
  EX  subordinate enrichment — 17-feature enumeration, dated snapshots, borrowing debate
      (visually muted, deliberately last, never the spine)

Stage 9 is the only pivot node: it is the feature that makes every other feature
binding, so it is rendered in the yellow pivot treatment.

VISUAL GRAMMAR — 17 PRIMITIVES AUTHORED ONLY FOR THIS TOPIC
--------------------------------------------------------------------------------
wheel · fan · srcmap · spectrum · quadrant · loop · balance · overlap · triangle
pyramid · triad · vs3 · bus · constel · switch · tension · web

None of them is used by the Polity 01 g9 or Polity 02 g8 packages, and the
validator proves that no stage signature and no primitive name is shared with
either. Each stage combines a bespoke primitive with matrices, columns, bridge
bands and one topic-specific purple answer line; no two stages share a signature.

SOURCE INTEGRITY
--------------------------------------------------------------------------------
Every fact, Article, amendment number, case name and date comes from the single
canonical owner:

  upsc-ai-kit\knowledge\Polity\learning-sessions\v2\
    subject-wide-syllabus-core-first-g3-...-g8\polity-03_Learning-Session.md

including its OPTIONAL ADVANCED DEPTH block and its consolidated register notes.
Where the owner records a dated position (the ~470-Article snapshot, the 106th
Amendment commencement, the Article 370 judgment, the status of Jammu and
Kashmir), the date is printed with the fact. Where an official PYQ key is not
held locally, the canvas says so instead of asserting a key. Nothing is
reconstructed from memory. The 24 verbatim answer-control lines of the owner
file are distributed one per stage and are reproduced word for word.

FILES
--------------------------------------------------------------------------------
  master.png                                     4800 x 38332 px, 300 dpi
  Polity03_...g9_Poster_2026-08-22.pdf           one page, whole canvas
  Polity03_...g9_Tiled_2026-08-22.pdf            13 A3-landscape tiles, 240 px overlap
  previews\page-001..013.png                     one preview per tile
  previews\contact-sheet-01..03.png              justified galleries, no blank waste
  bespoke-design-spec.json                       full authored spec, stage by stage
  build-audit.json                               overflow log + before/after hash sets
  validation-report.txt                          output of validate_g9.py
  preservation-hashes.json                       reference, sibling and artefact hashes
  render_lib.py                                  shared engine, unmodified
  render_p3.py / render_p3b.py                   the 17 bespoke primitives
  spec_header.py, spec_a..spec_i.py              authored stage content
  spec_content.py                                assembled stages + must-show vocabulary
  build_g9.py                                    reproducible build
  validate_g9.py                                 12-section validation

REBUILD
--------------------------------------------------------------------------------
  cd notes\Polity\flowcharts\polity-03\continuous-at-a-glance-carvaka-standard-g9
  python build_g9.py        (~3 minutes; prints canvas size, tiles, overflows)
  python validate_g9.py     (writes validation-report.txt + preservation-hashes.json)

The build is deterministic: same sources, same fonts, same output. It writes only
inside this folder. It never touches the Philosophy reference folder, any earlier
Polity 03 generation, the topic Markdown, the workbook, the notes PDFs or any
tracker.

PRESERVATION
--------------------------------------------------------------------------------
Every pre-existing artefact under notes\Polity\flowcharts\polity-03\ is hashed
before the build, after the build and again at validation time. All three sets
must be identical, which is what keeps the earlier core-first generations
(g3..g8) and the legacy root master set available for traceability.

HOW TO USE IT
--------------------------------------------------------------------------------
Read the poster top to bottom once for the argument. Then work stage by stage:
each stage gives you the visual, the exact constitutional terms, the trap it
answers and one line you can lift into an answer. Stage 21 carries the PYQ
routing table, the prelims discriminators, the four-sentence Mains template and
the "never write these" list. The enrichment stage at the end is recall support
only — never open a Mains answer with it.
