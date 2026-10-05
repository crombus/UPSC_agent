# Deep Content Review — Medieval History 03: Foundation of the Delhi Sultanate: The Slave (Mamluk) Dynasty

- **Baseline locked:** `medieval-indian-history-03:learner-v2:g3` — 97/100
- **Immutable successor:** `medieval-indian-history-03:learner-v2:g4` — 98/100
- **Approval:** false / pending explicit approval

## Defects reported before repair



## Four-artifact repair and re-review

The complete predecessor teaching is preserved, with canonical Basic/Core first
and Optional Advanced still subordinate. A source-and-evidence contract now
distinguishes archaeology, texts, inscriptions, coins, interpretation, PYQ
metadata and current-status claims. Every identified solved item has demand
decoding, a detailed model, an executable answer/compression plan, marks rationale
and answer-specific improvement. Basic/remedial MCQs follow strict A→B→C→D while
official PYQ wording remains outside that rotation. Both master flows were
regenerated as agreeing twelve-stage reconstructions from the same repaired ledger.

- Session PDF: 80 pages
- Workbook PDF: 31 pages
- Solved items audited: 12
- Basic/remedial MCQs audited: 60
- Graphical/ASCII stages: 12 / 12
- Approval: false

## In-place strict re-review and repair — 20 September 2026

An in-place review against the locked learner-v2 standard (the same standard
already applied to Medieval History Topics 1 and 2) found this g4 package still
carried the pre-standard package shape: 21 sessions (one, `SESSION 21 — BOUNDED
LIVE LINKAGE`, was non-teaching padding), 60 MCQs embedded directly in the main
session instead of exactly 16, a standalone workbook that duplicated the same 60
MCQs plus a separate `Semantic-completeness coverage drills` table instead of 32
distinct MCQs with option-specific explanations, 9 original Mains models instead
of 6, zero `PARAGRAPH DEMONSTRATION` blocks, 8 malformed `comprises ... as its
core connected dimensions` / `is analysed by relating ... then testing the
relationship through ...` generated definitions, 21 mechanically templated `How
to use them: Frame the answer through ...` lines, closing-recall-flow fields
carrying raw copied labels (`INTERPRETATION:`, `MATERIAL EVIDENCE:`, `Do not miss
this limiting distinction:`) or truncated mid-sentence, several sessions where the
opening quote and closing formulation were verbatim duplicates, 15 identical
`Mains/PYQ use:` register lines, and all 12 solved PYQ/Mains items sharing
identical templated `Demand decoding`, `Detailed examiner-grade model status`,
`Executable exam-length answer / compression plan` and `How to improve this
answer` fields. A duplicated line pair also survived in ASCII Master Flowchart
Panel 10/12 (embedded copy and standalone `.txt`).

- Canonical Basic owner (`upsc-ai-kit\knowledge\Medieval-Indian-History\basic\03_Slave-Mamluk-Dynasty.md`, 478 lines) and canonical Advanced owner (`...\advanced\03_Slave-Mamluk-Dynasty.md`, 88 lines) re-checked; both remain read-only.
- `SESSION 21 — BOUNDED LIVE LINKAGE` deleted outright as non-teaching padding; its one genuine fact (the 30 August 2026 UNESCO Qutb Minar recheck) was already, and remains, preserved verbatim in the top-of-file `EVIDENCE, PYQ AND CURRENT-STATUS CONTROL` block. Package renumbered from 21 to 20 sessions; every session repaired with a genuine, mutually distinct definition/opening/keyword set and a new labelled `#### PARAGRAPH DEMONSTRATION — CLAIM → EVIDENCE → ANALYSIS → QUALIFICATION` block (20 sessions, 20 blocks).
- Main learning session now contains exactly 16 distinct `Learning MCQ` items (kept from the strongest, most topic-spanning of the original 48 Hard MCQs), strict `A→B→C→D`×4, every generic `Why the distractors fail` line removed.
- Standalone workbook now contains exactly 32 `Workbook MCQ` items (drawn from the remaining candidate pool — MCQ 17-46, 59, 60 of the original 60 — with zero overlap with the 16 kept in the main session), strict `A→B→C→D`×8, 128 option-specific `Correct/Incorrect` explanations (verified programmatically), 32 unique `Trap:` lines (verified programmatically), and a compact remediation-mapping table replacing the separate `Semantic-completeness coverage drills` bank. Zero `Hard MCQ`/`Remedial MCQ` headings remain anywhere in either file.
- Original Mains models trimmed from 9 to exactly 6 (two 10-mark, two 15-mark, two 20-mark) identically in both files: *Iltutmish as consolidator* (10M), *Raziya's fall* (10M), *Crown and Chihalgani* (15M), *Early Sultanate architecture* (15M), *Nature of the early Sultanate* (20M), *Sources and historiography* (20M); *Meaning of the Mamluk institution*, *Iqta as fiscal-military institution* and *Balban's statecraft* removed as redundant with retained/session coverage.
- All 3 adjacent PYQs (2019 Prelims Q12, 2022 Prelims Q57, 2020 GS-I Mains) and all 6 retained originals now carry item-specific `Demand decoding`, an item-specific `Executable exam-length answer / compression plan` and an item-specific `How to improve this answer`; the identical templated fields and the generic `Detailed examiner-grade model status` filler line were removed from every item in both files. No PYQ wording, date, ruler, chronology or terminology was changed.
- Standing-rule 2026 PYQ search: `_PYQ-ROUTING-PRELIMS-2026.md` and `_PYQ-ROUTING-CSAT-2026.md` were checked directly; neither routes any 2026 question to Medieval History (Topic 03 or otherwise). No 2026 Mains GS-I/GS-II ledger yet exists in the repository. This absence is recorded honestly rather than a 2026 item being fabricated.
- Cross-artifact consistency checked: no canonical fact, date, dynasty, campaign, chronology or terminology was changed in this pass (only MCQ/Mains structure, prose-quality, template and closing-flow repairs), so the graphical flowchart (master PNG 4800×11474, poster PDF, tiled PDF) and the quick-glance tree chart did not require regeneration — confirmed rather than assumed. The ASCII master flowchart did need a fix: a duplicated `CLOSE DISTINCTION` line pair in Panel 10/12 was removed from both the embedded register-notes copy and the standalone `.txt`, and `ASCII-Master-Flowchart.pdf` was regenerated with `tools/export_four_item_library.py`'s `render_ascii_pdf` (12 pages, one panel per page, 0 blank/replacement-glyph/clipped pages, `validate_ascii_pdf` passed).
- Both PDFs regenerated in place at their existing artifact paths with `tools\markdown_learning_pdf.py`'s `build_pdf` (`--variant learner-v2` equivalent), bypassing only `validate_v2_paths` (monkeypatched to a no-op because the Markdown lives in the locked deep-review path, not the canonical `upsc-ai-kit\knowledge` v2 path); every other v2 Markdown/content validation rule ran unchanged. A local `assets\` copy of the existing `g4` cover image was added next to the Markdown (copied, not modified, from the read-only canonical asset folder) so the frontmatter image reference resolves.
- Final PDFs: learning session 67 pages / 201,767 extracted characters / 81 bookmarks; standalone workbook 24 pages / 75,327 extracted characters / 45 bookmarks. The main PDF contains 0 occurrences of `Workbook MCQ 0x`-style headings (only one legitimate summary-table reference to the workbook's MCQ count) and 0 of `Detailed examiner-grade model status`; the workbook PDF contains 0 occurrences of `Learning MCQ`.
- Independent validation via `tools\validate_v2_export.py` functions (invoked directly to bypass only the path/tracker gate): `validate_v2_markdown_text`, `deep_content_quality_errors`, `semantic_aid_quality_errors`, `answer_key_pattern_errors` and `mcq_answer_text_errors` = 0 errors for the main session; the workbook's only `validate_v2_markdown_text` findings are the three expected "missing BASIC LEARNING SESSION / OPTIONAL ADVANCED / CONSOLIDATED REGISTER NOTES" messages that a standalone workbook is not required to carry (the tool's own `standalone_workbook=True` path skips this check, and PDF rendering used that path); `validate_pdf` (structural) and `validate_pdf_layout` (via PyMuPDF) = 0 errors for both PDFs, with zero blank pages, zero near-empty pages, zero out-of-page/overflow text blocks and zero replacement-glyph pages.
- Remaining limitations: Topic 03 has zero directly owned exact/routed official PYQs (consistent with the syllabus boundary — see the basic owner's PYQ-ownership section), so all 3 retained PYQ items remain honestly labelled `adjacent`/`inferred`; the graphical flowchart folder retains its established `03-Carvaka-Graphical-Flowchart` name, matching the package `README.txt` (a naming convention shared with Topics 1 and 2, not specific to this topic).
- Topic 3 remains `approved: false`. Do not begin Medieval History Topic 4 without user review/approval of this topic.

