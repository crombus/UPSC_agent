TOPIC-LOCAL FACTUAL VALIDATION LEDGER
======================================
Topic: Modern History — Subject-wide Syllabus — 02 Indian States & Society in the
18th Century (Marathas, Sikhs, successor states)

Scope of this ledger: EXECUTOR SELF-CHECK ONLY, produced against a single
exhaustive preflight audit that identified and froze ten defects (D1-D10)
before any repair began, all fixed in one repair pass as instructed, plus
three additional defects (D11, asset provenance; D12, a stale self-declared
practice-counts table; D13, an unsupported-glyph PDF rendering defect)
surfaced and fixed during post-repair full-contract self-validation passes.
This document is the repairing agent's own recorded evidence. It is NOT an
independent reviewer's acceptance or sign-off, and it does not substitute
for one.

**approved:false**

1. FROZEN DEFECTS AND FIXES
---------------------------------------------------------------
- D1 — Learning-Session.md's "BASIC MCQS / REMEDIATION" section held 80
  questions instead of the required 16. Fixed: replaced with 16 curated,
  distinct questions (Q1-Q16), clean question-as-header format matching
  Topic 01's convention, unique per-question trap-logic lines, exact ABCD
  x4 answer-key rotation preserved from the source pool.
- D2 — Solved-Practice-Workbook.md's MCQ section was 100% duplicated from
  Learning-Session.md's original 80-question pool (specifically its Q17-
  Q48 slice) and used single-line explanations, not distinct
  question-plus-option-level explanations. Fixed: replaced with 32 wholly
  distinct questions (Q1-Q32, none overlapping the 16 kept in
  Learning-Session.md), each carrying a 4-bullet "Explanation by option"
  block (one bullet per option, addressing why it is right or wrong) and
  its own unique trap-logic line; exact ABCD x8 rotation confirmed.
- D3 — Solved-Practice-Workbook.md contained an extraneous "Semantic-
  completeness coverage drills" table with no equivalent in the required
  deliverable structure. Fixed: removed in full as part of the MCQ-section
  rewrite; re-grepped this pass, zero remaining occurrences of that phrase
  in either owner Markdown file.
- D4 — Learning-Session.md's "PART IV - ORIGINAL SOLVED MAINS PRACTICE"
  held 9 original Mains answers instead of exactly 6, and several answers
  exceeded their word ceilings. Fixed: curated down to exactly 6 originals
  (10M-1, 10M-2, 15M-1, 15M-2, 20M-1, 20M-2 — renumbering the two kept
  from the old "-3" slots), trimmed/rewritten to 150, 148, 248, 233, 245
  and 242 words respectively (all within the 150-word ceiling for 10-mark
  and 250-word ceiling for 15/20-mark answers), preserving the file's
  existing Demand-decoding / examiner-grade-model-status / executable-
  answer / how-to-improve boilerplate format per answer. A new "PART IV
  coverage conclusion" paragraph explains the 3 removed originals.
- D5 — Solved-Practice-Workbook.md's Mains section was a separate,
  independently drifted 9-original copy. Fixed: replaced in full with the
  exact byte-identical 6-original block now in Learning-Session.md
  (verified via direct string comparison: 17,827 characters, identical).
- D6 — `VALIDATION-LEDGER.md` did not exist for this topic. Fixed: this
  file, created with `approved:false`.
- D7 — `README.txt` was stale (referenced the removed Carvaka Graphical
  Flowchart as a retained deliverable, said "Approval pending" instead of
  the standard `approved:false` phrasing, and did not carry the graphical-
  flowchart-omission sentence or the companion-assets/quick-glance links
  used by Topic 01). Fixed: rewritten in Topic 01's concise format, see
  Section 3 below.
- D8 — A `03-Carvaka-Graphical-Flowchart` folder (poster PDF, tiled PDF,
  high-resolution PNG) was wrongly present in the final package. Fixed:
  deleted in full (3 files removed); README's deliverable list and
  omission sentence updated to match.
- D9 — Learning-Session.md referenced a cover image at
  `assets/modern-indian-history-02_Teaching-Navigation_2026-08-30.png`
  but the owner package had no local `assets\` folder, so the reference
  was broken for any owner-local render. Fixed: created an owner-local
  `assets\` folder and copied (not moved) the PNG into it from its
  canonical source under
  `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Modern-Indian-History\...`;
  the canonical knowledge-base copy was left untouched.
- D10 — Both final-package PDFs (`Complete-Learning-Session.pdf`,
  `Solved-Practice-Workbook.pdf`) were stale against the corrected
  Markdown. Fixed: regenerated, see Section 2 below.
- D11 (found and fixed in follow-up pass) — the owner-local
  `assets\modern-indian-history-02_Teaching-Navigation_2026-08-30.png`
  created to satisfy D9 had been copied from a canonical/historical
  Learner-v2 generation tree
  (`upsc-ai-kit\knowledge\Learner-v2-Refreshed\Modern\MH\learning-
  sessions\mhi-02\g3\...` / `g4\...` / and the parallel `Modern-Indian-
  History\Subject-Wide-Syllabus\learning-sessions\modern-indian-
  history-02\...` copy — all three confirmed byte-identical via SHA-256
  hash, so the exact single source folder cannot be distinguished, but
  all three sit inside the same prohibited `Learner-v2-Refreshed`
  historical-generation tree). This violated the requirement that owner
  assets be independently owned/authored rather than sourced from a
  historical/canonical generation tree. Fixed: the copied PNG was
  deleted; a new asset,
  `assets\Topic02-Owner-Navigation-Map.png`, was independently generated
  by a topic-local script using only Pillow drawing primitives and data
  already present in this topic's own `Learning-Session.md` (the five H2
  part names/descriptions and the 25 Basic-Learning-Session titles/
  numbers) — nothing was copied from any external file or image. Both the
  frontmatter `cover_image:` reference and the inline embedded image/
  caption (`Learning-Session.md`, formerly around line 49) were updated to
  point to the new asset and to drop a caption sentence that had wrongly
  implied the removed graphical flowchart still existed as a companion
  artifact. Both PDFs were then re-rendered against the corrected
  Markdown (see Section 2), producing identical page/bookmark counts to
  the prior render (66 pages/79 bookmarks; 21 pages/50 bookmarks),
  confirming the fix changed only the cover image, not content structure.
  The canonical `Learner-v2-Refreshed` copies themselves were left
  completely untouched (read-only hash comparison only; zero writes to
  that tree at any point in this repair).
- D12 (found and fixed during full-contract self-validation) —
  Learning-Session.md's own front-matter "Package practice counts" table
  (Source-audit block, near line 57) was stale: it still declared "Hard
  MCQs with explanations | 48" / "Remedial MCQs with explanations | 12"
  (a difficulty split that does not exist anywhere in the current MCQ
  section — no such tagging is present) and "Original solved 10-mark
  Mains | 3" / "15-mark Mains | 3" / "20-mark Mains | 3" (the pre-D4/D5
  count of 9, not the corrected 6). This table was not updated when the
  MCQ/Mains sections were rewritten earlier in this repair, so the package
  carried an internally inconsistent, untruthful self-declared count in
  its own body text/PDF. Fixed: the table now reads "Learning-Session
  MCQs with explanations | 16 (ABCD x4 rotation)", "Workbook MCQs with
  explanations | 32 distinct (ABCD x8 rotation; zero overlap with the 16
  Learning-Session stems; 128 option-level explanation bullets; 32
  trap-logic lines)", and "Original solved 10/15/20-mark Mains | 2" each
  (totalling exactly 6). `Solved-Practice-Workbook.md` was checked and
  carries no equivalent table (nothing to fix there).
  `Complete-Learning-Session.pdf` was re-rendered a third time against
  this corrected Markdown (metadata re-applied); page/bookmark/blank-page
  counts are unchanged (66 pages, 79 bookmarks, 0 blank pages, the same 2
  pre-existing unrelated NUL-glyph pages), confirming the fix changed only
  the stale counts-table text, not structure.
  `Solved-Practice-Workbook.pdf` was not re-rendered since its source
  Markdown was not touched by D12.
- D13 (found and fixed during a follow-up mandatory glyph-defect pass) —
  the previously-disclosed "out-of-scope" item was reclassified as
  in-scope per explicit instruction: a single unsupported "➕" (U+2795,
  HEAVY PLUS SIGN) character in the Advanced-section subheading
  `### ➕ Historiography note (PYQ-gap)` (Learning-Session.md, then line
  ~2785) was not renderable by the PDF font, producing a NUL/replacement-
  glyph artifact on 2 of 66 `Complete-Learning-Session.pdf` pages. Fixed:
  replaced with ASCII/renderer-safe wording,
  `### ADDITIONAL — Historiography note (PYQ-gap)`, preserving the
  heading's meaning and its em-dash (already used safely elsewhere
  throughout the file) without altering any surrounding body text. A full
  scan of every character above U+2000 in `Learning-Session.md` was run
  before and after the fix (arrows →, ✅, ⚠️, ❌, ≤, 💰, 🔑 all confirmed
  already renderer-safe and unrelated to the 2 flagged pages) to confirm
  U+2795 was the only unsupported glyph. `Complete-Learning-Session.pdf`
  was re-rendered a fourth time (metadata re-applied); page/bookmark
  counts unchanged (66 pages, 79 bookmarks), 0 blank pages, and — verified
  by a full per-page `fitz` text-extraction scan of all 66 pages — 0
  pages now contain any NUL (`\x00`) or Unicode replacement (`\ufffd`)
  character. `Solved-Practice-Workbook.pdf` was not re-rendered (it never
  contained the Advanced section or this heading).

2. PDF REGENERATION AND VALIDATION
---------------------------------------------------------------
Fix method (topic-local, no shared-tool edit): a temporary, topic-local
script (created inside this topic's own owner source folder, deleted
after use) imported `tools\markdown_learning_pdf.py` as a module,
unmodified, and called its existing public functions:
- Learning Session PDF: regenerated via the module's `build_pdf(...,
  mode="main", variant="legacy-v1", internal_index=True)` — unchanged
  content-selection path, with full auto-TOC/bookmarks enabled.
- Workbook PDF: regenerated via a hand-assembled call sequence using the
  same module's own `cover_story`, `contents_story`, `markdown_story`,
  `on_page`, `IndexedDocTemplate` functions directly, passing the *full,
  unsliced* workbook markdown body (bypassing the destructive
  `select_markdown` slicing that `--mode workbook` would otherwise apply
  for the legacy variant — its heading-based slice rule would have cut
  from the first PYQ-labelled heading onward, i.e. would have deleted this
  workbook's own 32-question Basic MCQ section), while setting
  `mode="workbook"` cosmetics (cover subtitle "SOLVED PRACTICE WORKBOOK",
  workbook-specific descriptor, footer label "UPSC Solved Practice
  Workbook") and `internal_index=True` for full TOC/bookmarks.
- Metadata (Title/Author/Subject/Creator) was then set on both output
  files via a `pypdf` post-process (`PdfWriter.append` + `add_metadata`,
  touching only the `/Info` dictionary; the outline/bookmark tree built by
  the renderer was left untouched and re-verified intact afterward).

Verified this pass (via `fitz` full-text extraction and `pypdf` metadata/
outline inspection) — NOTE: superseded by the D14 pass below, which
re-rendered both PDFs again with different page/bookmark counts and
neutral metadata; the counts in this section are retained only as a
historical record of the D1-D13 state:
- `Complete-Learning-Session.pdf`: 66 pages. 79 outline bookmarks, covering
  all 5 top-level H2 parts in order (Basic Learning Session incl. all 25
  sessions, Basic MCQs/Remediation with all 16 questions, PYQs and Answer
  Practice with all 3 PYQs and all 6 Mains questions, Optional Advanced
  Depth, Consolidated Register Notes placed last with the ASCII master
  flow diagram) — satisfying full-content TOC/bookmark coverage. 0 blank/
  near-blank pages (every page checked). 0 pages now contain any
  unsupported-glyph (NUL/replacement) character — the single "➕" (U+2795)
  character that previously produced this artifact on 2 of 66 pages was
  found and fixed as D13 (see Section 1); a full 66-page `fitz` text-scan
  after the D13 re-render confirms zero remaining NUL (`\x00`) or
  replacement (`\ufffd`) characters anywhere in the file. Metadata at that
  time: Author "UPSC Preparation Workspace - owner export", Creator
  "owner-local topic-scoped renderer" — both since replaced by neutral
  values in the D14 pass (see below) because this phrasing was flagged as
  a forbidden owner-export/local-renderer metadata defect.
- `Solved-Practice-Workbook.pdf`: 21 pages. 50 outline bookmarks, covering
  all 32 workbook MCQs, the PYQ section and all 6 Mains questions. 0
  blank/near-blank pages. 0 NUL-glyph pages (the workbook file does not
  contain the Advanced-section heading above). Cover subtitle/footer both
  read Workbook-specific text; zero Complete-Learning-Session identity
  leakage. Metadata: Title "... - Solved Practice Workbook", Author/
  Creator matching the Learning Session PDF's neutral values, Subject
  naming the workbook deliverable.
- `ASCII-Master-Flowchart.pdf`/`.txt` (a separate, non-listed-as-repaired
  deliverable) were not regenerated this pass, since neither their source
  content nor the embedded ASCII panels in Learning-Session.md changed;
  re-verified this pass that all 12 ASCII panels in the standalone `.txt`
  are byte-identical (panel body content) to the corresponding fenced
  blocks embedded in Learning-Session.md — confirming embedded/TXT/PDF
  consistency was not disturbed by this repair.
- The temporary regeneration and metadata/validation scripts created
  inside this topic's owner source folder were deleted after both PDFs
  were regenerated and verified; no other temp files were left on disk.

3. README.txt REWRITE
---------------------------------------------------------------
Rewritten in Topic 01's concise two-file convention: Approval line changed
to `approved:false`; deliverable list corrected to the 3 actually-retained
deliverables (Complete Learning Session PDF, Solved Practice Workbook PDF,
ASCII Master Flowchart PDF+text) with a parenthetical summary of counts
matching this ledger; the Carvaka Graphical Flowchart entry removed and
replaced with the sentence "Graphical flowchart intentionally omitted by
user export preference." (same wording as Topic 01's precedent); a
Companion-assets block added linking to the quick-glance tree chart at
`quick_galance\Modern-Indian-History\02_Indian-States-and-Society-18th-
Century_Tree-Chart.md` (unedited, only referenced) and to this ledger.
The "Source record ID"/"Source generation" lines (previously
`modern-indian-history-02:learner-v2:g4`, generation 4) were removed in
the D14 pass below: this production-process/generation-tracking language
is not learner-facing information and was flagged as forbidden
Learner-v2-style prose.

4. ITEMS EXPLICITLY NOT TOUCHED
---------------------------------------------------------------
Per this task's scope limit, the following were left unedited: all 25
Basic-Learning-Session teaching sessions and their visual-first framing,
named-evidence demonstrations and keyword lists; the Optional Advanced
Depth section's substantive content (only the single unsupported glyph
fixed as D13 was changed, wording/meaning preserved); the 3 verified/
routed PYQs and their solved explanations; the 16 ASCII master-flow
panels and their wording; the quick-glance tree chart; the owner-local
topic Markdown outside the MCQ/Mains/counts-table/glyph edits listed
above; `tools\markdown_learning_pdf.py` and every other shared tool;
`EXPORT-PDF-STATUS.json`, `KNOWLEDGE-SEMANTIC-COMPLETENESS-
TRACKER.md`, `MANIFEST.json` and every other governing ledger, tracker or
index (read for reference only, never written); every canonical/basic
source file; and Modern History Topic 01, Medieval History Topic 25 and
Modern History Topic 03 in full (Topic 03's own unfixed graphical-
flowchart folder and missing validation ledger were both explicitly left
alone, per instruction).

5. COUNTS SUMMARY
---------------------------------------------------------------
| Item | Before this pass | After this pass |
|---|---|---|
| Learning-Session.md Basic MCQs | 80 | 16 (ABCD x4 rotation exact) |
| Solved-Practice-Workbook.md MCQs | 80 (100% duplicate of LS pool) | 32 distinct (ABCD x8 rotation exact) |
| WB option-level explanation bullets | 0 (single-line explanations only) | 128 (4 per question x 32) |
| WB unique trap-logic lines | 0 | 32 |
| "Semantic-completeness coverage drills" table | present | 0 occurrences |
| Original Mains answers (Learning-Session.md) | 9 | 6 (10M-1, 10M-2, 15M-1, 15M-2, 20M-1, 20M-2) |
| Mains word-ceiling violations | present (some >150/>250) | 0 (150, 148, 248, 233, 245, 242 words) |
| LS/WB Mains section byte match | not verified / drifted (WB had own 9) | identical, 17,827 characters |
| `03-Carvaka-Graphical-Flowchart` folder | present (3 files) | removed (0 files) |
| Owner-local `assets\` folder | absent (broken cover-image reference) | present, 1 PNG, independently generated from owner Markdown (D9 fix then D11-corrected provenance) |
| Owner-asset provenance | (D11) copied from `Learner-v2-Refreshed` historical generation tree | independently generated by topic-local script from this topic's own H2/session data; zero copy from any external file |
| `VALIDATION-LEDGER.md` | absent | present, `approved:false` |
| `README.txt` | stale (wrong deliverable list, no omission note) | rewritten, accurate, omission note present |
| Complete-Learning-Session.pdf | stale vs. corrected Markdown | 66 pages, 79 bookmarks, 0 blank pages (re-rendered four times: after D1-D10, after the D11 asset swap, after the D12 counts-table fix, and after the D13 glyph fix; identical page/bookmark counts every time) |
| Solved-Practice-Workbook.pdf | stale vs. corrected Markdown | 21 pages, 50 bookmarks, 0 blank pages (re-rendered twice, identical counts both times; not touched by D12/D13) |
| Five H2 top-level order | intact | re-confirmed intact and unchanged |
| Register notes position | last | re-confirmed last |
| ASCII embedded vs. standalone TXT/PDF consistency | unchanged | re-confirmed: all 12 panels byte-identical |
| Learning-Session.md front-matter "Package practice counts" table | stale (48 "Hard"/12 "Remedial" MCQs — split unsupported by content; 3/3/3=9 Mains) | accurate: 16 LS MCQs, 32 WB MCQs, 2/2/2=6 Mains |
| Complete-Learning-Session.pdf unsupported-glyph (NUL/replacement) pages | 2 of 66 (traced to one "➕" U+2795 character) | 0 of 66 (full 66-page scan, zero NUL/replacement characters) |

Approval state: **approved:false**. This ledger is the executor's own
recorded evidence against the ten frozen defects named in the preflight
audit for this pass, plus the D11 asset-provenance defect, D12 stale-
counts-table defect, and D13 unsupported-glyph PDF rendering defect found
and fixed during follow-up full-contract self-validation passes, and is
not an independent acceptance. All previously-identified defects (D1-D13)
are now fixed; no known blockers remain.

6. D14 — SURGICAL REPAIR AFTER INDEPENDENT AUDIT FAILURE
---------------------------------------------------------------
An independent audit of the D1-D13 state failed. This section records a
subsequent 15-point surgical repair performed against a frozen defect
list. Authorized writes for this pass: the exact Topic 02 owner folder
under `learning_package_final`, the exact final package folder under
`notes\Final-Learning-Packages`, the matching Quick-Glance file, and the
matching reusable Markdown at
`upsc-ai-kit\knowledge\Modern-Indian-History\02_Indian-States-Society-18th-
Century_Complete-Topic-Package.md`. Basic/Advanced content and all
Learner-v2/v2/history/practice/shared/global/governing files remained
read-only/forbidden throughout.

- D14.1/D14.2 — All 25 Basic-Learning-Session sessions were rewritten:
  each session's existing table/ASCII visual was moved before its
  DEFINITION block (visual-first ordering); a new "#### NAMED EVIDENCE"
  H4 (3-5 sentences, synthesised only from facts already present in that
  session's own tables/bullets) was added before CLOSING RECALL FLOW;
  tautological/duplicated DEFINITION and OPENING text, meta-label or
  false-option-as-keyword MUST-WRITE KEYWORDS, and 24 identical "How to
  use them" guidance shells were rewritten to be direct, distinct and
  session-specific; all editorial bracket tags (`[FACT]`, `[METHOD]`,
  `[BOUNDARY]`, `[INTERPRETATION]`, `[LIMIT]`, `[ANALYSIS]`, `[VERDICT]`,
  `[SOURCE CAUTION]`, `[MATERIAL LINK]`, `[CONCEPT]`, `[THESIS]`) were
  stripped throughout the file; 4 truncation ellipses in CLOSING RECALL
  FLOW blocks were completed; each session's "EXACT TERMS" line was
  re-synced to its new keyword list.
- D14.4/D14.13 — The frontmatter (previously containing a "Learner-v2
  Refreshed" title, a regeneration date, an approval-state paragraph, a
  "DEEP-REVIEW LEARNING CONTRACT" table, a canonical-owner file-path
  table, a "Sources actually used" table naming "Repository knowledge" /
  "Repository bridge", and a closing Qdrant-mention paragraph) was
  replaced with a short, clean, learner-facing frontmatter (title, tag
  line, navigation image, accurate practice-counts table, bounded
  reference links). A duplicate "MODERN HISTORY DEEP-REVIEW CORE CONTROL"
  section was deleted (content duplicated the ASCII panels). `README.txt`
  had its "Source record ID: modern-indian-history-02:learner-v2:g4" and
  "Source generation: 4" lines removed as forbidden production-process
  language. A whole-document grep for
  `Learner-v2|Qdrant|repository|predecessor generation|prior draft|core
  control` across `Learning-Session.md`, `Solved-Practice-Workbook.md` and
  the reusable Markdown returned zero matches after this pass.
- D14.5/D14.6 — The 17 REGISTER modules (previously positioned before
  Session 1) and a mid-document "TOPIC 02 CLOSING REGIONAL-STATE-AND-
  SOCIETY LEDGER" were relocated into the CONSOLIDATED REGISTER NOTES H2
  (the last of the five top-level sections), immediately before the 12
  ASCII panels, and the ledger content was rewritten as a fuller "LEARNER
  BOUNDARY BLOCK" naming Topic 01 (imperial-decline causation), Topic 03
  and Topic 05 (adjacent European rivalry/conquest/later wars), and
  Medieval Topic 25 (pre-1761 continuity), plus an explicit PYQ-honesty
  statement and explicit 2026 Prelims/Mains no-route statements. Both
  PDFs were regenerated so their auto-TOC/bookmarks reflect the new
  register position.
- D14.8/D14.9 — PYQ section: PYQ01 (2021 Q48) and PYQ02 (2021 Q45)
  generic boilerplate was replaced with question-specific
  demand-decoding/compression-plan/improvement text; PYQ02 now carries an
  explicit routing note stating its direct owner is Medieval Topic 24 (in
  both `Learning-Session.md` and `Solved-Practice-Workbook.md`, the latter
  previously missing this note entirely); PYQ03 (2022 GS-I Mains Q2) was
  corrected from a wrongly-labelled "15-mark" framing to the correct
  10-mark framing with bespoke text; the "PYQ coverage conclusion"
  paragraph was rewritten in both files to remove stale "audited
  repository"/"2018-2025"/"2018-2026" language and state explicitly that
  the direct Topic-02 route count for both 2026 Prelims and 2026 GS-I
  Mains is zero. All 6 Mains items (10M-1, 10M-2, 15M-1, 15M-2, 20M-1,
  20M-2) had their generic 4-line boilerplate (which wrongly used "For a
  15-mark answer" framing on the 10-mark and 20-mark items) replaced with
  bespoke, mark-accurate, question-specific demand-decoding/compression-
  plan/improvement text in both `Learning-Session.md` and
  `Solved-Practice-Workbook.md`. A "prior draft" production-process phrase
  in the "PART IV coverage conclusion" of both files was also removed.
- D14.10 — In `Solved-Practice-Workbook.md`, 33 of the 128 option-level
  explanation bullets (29 flagged as generic "an/a unrelated ..." shells,
  plus 4 additional ultra-short bullets) were rewritten so every option
  names the actual distractor entity, its correct real-world association,
  and a precise contrast with the tested answer. Verified this pass: 0
  bare "unrelated"-only shell bullets remain; the word "unrelated" still
  appears 9 times, all inside fuller, specific sentences or trap-logic
  guidance lines (re-checked individually). LS16/WB32 stem sets remain
  100% non-overlapping (programmatically verified) and both rotations
  remain exactly ABCDx4 (LS16) and ABCDx8 (WB32).
- D14.11 — All 12 ASCII MASTER FLOW panels were reworked: 3 orphan "MUST
  REMEMBER"/"CLOSE DISTINCTION"/"EVIDENCE LIMIT" add-on lines (previously
  asymmetric, present on only 3 of 12 panels) were removed for uniformity;
  required named anchors were added — Panel 3: 1719 sanads, Palkhed
  (1728), Panipat (1761)/1771 recovery; Panel 4: Arcot's Hyderabad-derived
  genealogy and 1724/1717 dates; Panel 5: 1719 sanads; Panel 6: Khalsa
  1699, Banda 1709-15/1715-16; Panel 7: Haidar Ali 1755/1761, Sawai Jai
  Singh II/Jaipur 1727; Panel 8: Jagat Seth (Bengal treasurer c.1730);
  Panel 9: Tarabai/Ahilyabai Holkar; Panel 10: Jagat Seth-style credit;
  Panel 11: named regional cultural centres (Kangra, Lucknow, Hyderabad-
  Arcot, Travancore); Panel 12: the Topic01/03/05/Medieval24/25 boundary
  and the PYQ anchors (direct: 2021 Q48 only; adjacent: 2021 Q45, 2022
  Q2; 2026 Prelims/Mains: zero). The standalone `ASCII-Master-
  Flowchart.txt` was regenerated programmatically from the embedded
  panels (confirmed 12/12 panels extracted) and the standalone PDF was
  rebuilt from that TXT with a fresh, independent cover.
- D14.7 — The Quick-Glance tree chart
  (`quick_galance\Modern-Indian-History\02_Indian-States-and-Society-18th-
  Century_Tree-Chart.md`) was condensed from 1,261 to 797 lines (37%
  reduction) by mechanically removing 235 purely decorative `|`/`v`
  connector-line pairs (zero content loss — all substantive text
  retained); explicit "2026 PRELIMS NO-ROUTE" and "2026 GS-I MAINS
  NO-ROUTE" statements were added to its PYQ ownership/routing section,
  synced with the LS/WB wording.
- D14.14 — The reusable Markdown at
  `upsc-ai-kit\knowledge\Modern-Indian-History\02_Indian-States-Society-
  18th-Century_Complete-Topic-Package.md` (previously a stale, pre-D1
  edition: 2,223 lines, a "Hard MCQ 01-48"/"Remedial MCQ 49-60" structure,
  9 Mains items and "Repository knowledge"/"Repository bridge"/Qdrant
  frontmatter prose) was fully replaced with a synchronised current
  edition built from the repaired `Learning-Session.md` (five H2s in
  order, 25 sessions, 16 LS MCQs, routed PYQs, exactly 6 Mains, the
  Optional Advanced section, the 12-panel ASCII spine, all 17 final
  registers) with the Workbook's 32 MCQs (128 explanations) inserted into
  the Basic MCQs section. Verified: exactly 5 top-level H2 headings in
  the required order, 25 sessions, 48 total MCQs (16+32), 0 forbidden-term
  hits, 12/12 ASCII panels, 17/17 registers, 3 PYQs, 6 Mains items.
- D14.12 — Both `Complete-Learning-Session.pdf` and
  `Solved-Practice-Workbook.pdf` were rebuilt against all of the above
  content changes. Because `tools\markdown_learning_pdf.py`'s own
  `cover_story()` hard-codes "Original deterministic study visual..." and
  "Source order: repository knowledge -> official current linkage -> ..."
  with no parameter to suppress either phrase, a topic-local script
  defined its own clean cover (reusing the shared tool's
  `IndexedDocTemplate`/`contents_story`/`markdown_story`/`on_page`/style
  constants unmodified) instead of editing the shared tool file. Both
  PDFs' `/Author` and `/Creator` metadata (previously "UPSC Preparation
  Workspace - owner export" and "owner-local topic-scoped renderer") were
  replaced with neutral values ("UPSC Preparation Workspace" and
  ReportLab's own default), and `/Subject`/`/Keywords` were set to
  neutral, topic-descriptive text. `ASCII-Master-Flowchart.pdf` was
  independently rebuilt from the resynced TXT with its own clean cover and
  neutral metadata (previously its `/Creator` field named a shared-tool
  script file, `regenerate_modern_history_deep_review.py`, which has been
  removed). Verified this pass via `fitz` full-text extraction across all
  three PDFs: `Complete-Learning-Session.pdf` = 67 pages / 75 bookmarks;
  `Solved-Practice-Workbook.pdf` = 21 pages / 50 bookmarks;
  `ASCII-Master-Flowchart.pdf` = 13 pages (1 cover + 12 panels); 0
  blank/near-blank pages in any file; 0 NUL (`\x00`) or replacement
  (`\ufffd`) characters in any file; 0 occurrences of
  "deterministic"/"Source order"/"repository"/"Learner-v2"/"owner
  export"/"owner-local [...] renderer"/"prior draft"/"Qdrant" as
  production-process claims (the two literal hits of "deterministic" and
  "owner-local" found by an initial scan were manually confirmed to be
  legitimate content — an analytical sentence about avoiding a
  deterministic historical verdict, and the pre-existing factual image
  caption describing the navigation asset's own local origin — not
  forbidden renderer/export metadata language).
- D14.15 — All temporary scripts (`_d14_step1_temp.py` through
  `_d14_step14_temp.py`) and the `Learning-Session.md.bak` backup created
  during this pass were deleted after use; see Section 7 for the final
  file listing. LS16 (ABCDx4) and WB32 (ABCDx8) rotations and the six
  Mains models/word limits were preserved unchanged throughout this pass
  (re-verified programmatically, not merely re-asserted).

Approval state: **approved:false**. This D14 section is the executor's own
recorded evidence against the frozen 15-point defect list issued after the
independent audit failure. It is not an independent reviewer's acceptance
or sign-off, and it does not substitute for one. No further blockers are
known at the time of writing; any blockers discovered by a subsequent
independent audit should be added as a new dated section, not by editing
the sections above.
