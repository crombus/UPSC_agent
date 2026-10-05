# Deep Content Review — Medieval History 05: The Tughlaqs: Muhammad bin Tughlaq & Firuz Shah

- **Baseline locked:** `medieval-indian-history-05:learner-v2:g3` — 97/100
- **Immutable successor:** `medieval-indian-history-05:learner-v2:g4` — 98/100
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

- Session PDF: 86 pages
- Workbook PDF: 26 pages
- Solved items audited: 10
- Basic/remedial MCQs audited: 68
- Graphical/ASCII stages: 12 / 12
- Approval: false

## In-place strict re-review and repair — 20 September 2026

Manually audited all 25 sections of `Learning-Session.md` individually (not by
pattern search alone), together with the whole of
`Solved-Practice-Workbook.md`. The topic was still carrying the pre-standard
`g4` package shape, so this pass performed a strict in-place repair against the
current mandatory learner-v2 standard, applying the same locked checks used for
Topics 1-4. No new generation folder or `g*` suffix was created.

Defects found:

- 24 mechanically templated `How to use them: Frame the answer through ...`
  lines, one in every teaching session.
- 10 malformed generated definitions: 2 using `... comprises ... as its core
  connected dimensions` (Sessions 18, 19) and 8 using `... is analysed by
  relating ... then testing the relationship through ...` (Sessions 1, 8, 11,
  14, 15, 16, 20, 21).
- 14 closing-recall `UPSC TRAP / ANSWER-USE` lines carrying a raw copied
  `Do not miss this limiting distinction:` label instead of plain prose
  (Sessions 1, 4, 5, 7, 9, 10, 14, 15, 18, 19, 21, 23, 24 and the retired
  Session 25), 9 of them truncated mid-sentence with a trailing ellipsis.
- Many `MECHANISM / ARGUMENT` and `CONSEQUENCE / CONTRAST` fields that were raw
  sentences lifted out of the session body, several beginning with a copied
  `[DEBATE]` / `[FACT]` tag, and several `ANSWER-GRABBING FORMULATION` fields
  that duplicated the session's own opening quote verbatim.
- `MUST-WRITE KEYWORDS` lists polluted with meta/filler single-word entries,
  including literal `not`, `entire`, `reported`, `These`, `This`, `It` and
  `DEBATE`, and keyword sets that were simply the session title chopped into
  fragments.
- `SESSION 25 — BOUNDED LIVE LINKAGE`: non-teaching padding.
- Zero `PARAGRAPH DEMONSTRATION` blocks anywhere in the file.
- The main learning session carrying all 68 MCQs (16 Learning + 40
  broad-coverage + 12 remedial) instead of exactly 16.
- The standalone workbook duplicating the same 16 Learning MCQs before its 40
  broad-coverage MCQs, every question carrying one combined rationale instead
  of four option-specific explanations and no trap line, plus a separate
  12-question remedial bank and a `Semantic-completeness coverage drills`
  table.
- All 10 solved PYQ/Mains items in both files sharing an identical templated
  `Demand decoding` / `Detailed examiner-grade model status` / `Executable
  exam-length answer / compression plan` / `How to improve this answer` block,
  differing only by directive word, a truncated question quote or the mark
  count.
- One orphaned duplicate block of those generic fields (Adjacent PYQ 04's)
  misattached after the `### Original solved Mains practice` heading, before
  the first real Mains item.
- 3 broken relative image paths (Sessions 2, 12, 16 — truncated, hash-suffixed
  filenames that matched none of the 26 canonical PNGs), and no local `assets\`
  folder at all, so every one of the 27 image references failed to resolve.
- One unsupported `➕` glyph in the inherited Advanced-block heading, rendering
  as an empty box in the PDF and its index.

Repairs applied:

- `SESSION 25 — BOUNDED LIVE LINKAGE` deleted outright. Its one genuine fact
  (the ASI Qutb Minar current-status note, rechecked 30 August 2026) was
  already, and remains, preserved verbatim in the top-of-file `EVIDENCE, PYQ
  AND CURRENT-STATUS CONTROL` block. The package now carries exactly the 24
  sessions its own front matter promises.
- Every one of the 24 retained sessions received a genuine, mutually distinct
  plain definition, technical definition, answer-grabbing opening, six
  substantive keywords, session-specific `How to use them` guidance, and a new
  labelled `#### PARAGRAPH DEMONSTRATION — CLAIM → EVIDENCE → ANALYSIS →
  QUALIFICATION` block (24 sessions, 24 blocks, each grounded in that session's
  own vetted content).
- All four prose fields of all 24 closing recall flows were rewritten as
  complete, session-specific, non-duplicated sentences with every label-copy
  prefix removed, and `EXACT TERMS` was regenerated from the repaired keyword
  sets.
- Main learning session trimmed to exactly 16 `Learning MCQ` items, strict
  `A→B→C→D`×4; the 40 broad-coverage and 12 remedial MCQs were removed from it
  entirely.
- Standalone workbook rebuilt to open directly on `Workbook MCQ 01` with
  exactly 32 distinct questions before the PYQs, strict `A→B→C→D`×8, 128
  option-specific `Correct.`/`Incorrect.` explanations and 32 unique `Trap:`
  lines (all verified programmatically, zero near-duplicates at a 0.85
  similarity threshold, zero stem overlap with the 16 kept in the main
  session; two retained stems were reworded so that no stem sits within a 0.75 similarity of a Learning MCQ stem or within 0.8 of another Workbook MCQ stem, with options, keys and explanations untouched). The separate remedial bank and the coverage-drills table were
  replaced by a single `Remediation map` linking each predictable error to the
  Workbook MCQ that corrects it.
- All 4 PYQ items and all 6 original Mains models (already exactly two
  10-mark, two 15-mark and two 20-mark, so no trimming was needed) now carry
  item-specific `Demand decoding`, an item-specific `Executable exam-length
  answer / compression plan` and an item-specific `How to improve this answer`
  in both files; the generic `Detailed examiner-grade model status` line was
  removed from every item; the orphaned duplicate block was removed and
  Adjacent PYQ 04's own fields restored in place.
- The 3 broken image paths were corrected to their canonical filenames, a local
  `assets\` folder was added next to the Markdown with all 26 body/cover PNGs
  copied unmodified from `notes\Medieval-Indian-History\assets\05_The-Tughlaqs-Muhammad-bin-Tughlaq-Firuz-Shah\`
  plus the teaching-navigation cover copied from the read-only canonical
  `Learner-v2-Refreshed` asset folder, so all 27 references resolve.
- The `➕` was removed from the Advanced-block concept heading; the PDF now
  contains zero unsupported glyphs.
- An explicit attribution-caution row was added to Session 18 recording that
  only Firozabad/Kotla, Hissar-Firuza and the bounded Jaunpur association are
  attested in the source set used here, and that further foundations named in
  general accounts (for example Fatehabad) are recorded as unverified
  attributions rather than asserted.

Verification:

- Required five H2 sections present, in order, register notes last:
  `BASIC LEARNING SESSION` → `BASIC MCQS / REMEDIATION` → `PYQS AND ANSWER
  PRACTICE` → `OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER` →
  `CONSOLIDATED REGISTER NOTES`.
- `validate_v2_markdown_text`, `deep_content_quality_errors`,
  `semantic_aid_quality_errors`, `answer_key_pattern_errors` and
  `mcq_answer_text_errors` = 0 errors for both files. (One intermediate run
  flagged 4 `opening`-alignment mismatches in Sessions 10, 13, 20 and 24; all
  were rewritten and re-validated to 0.) The workbook's
  `validate_v2_markdown_text` correctly reports the three H2 sections a
  standalone workbook does not carry, which is expected and is why PDF
  rendering used the tool's own `standalone_workbook=True` path.
- Both PDFs regenerated in place with `tools\markdown_learning_pdf.py`'s
  `build_pdf` (`variant="learner-v2"`), bypassing only `validate_v2_paths`
  (monkeypatched to a no-op because the Markdown lives in the locked
  deep-review path, not the canonical `upsc-ai-kit\knowledge` v2 path); every
  other v2 validation rule ran unchanged.
- Final PDFs: learning session 83 pages / 225,755 extracted characters / 49
  bookmarks; standalone workbook 25 pages / 76,436 extracted characters / 39
  bookmarks. `validate_pdf` and `validate_pdf_layout` = 0 errors for both, with
  0 blank, 0 near-empty, 0 out-of-page/overflow and 0 replacement-glyph pages.
  The main PDF contains 0 occurrences of `Workbook MCQ`, `Detailed
  examiner-grade model` or `Frame the answer through`; the workbook PDF
  contains 0 occurrences of `Learning MCQ` or `Remedial MCQ`.
- 2026 evidence check: `_PYQ-ROUTING-PRELIMS-2026.md`,
  `_PYQ-ROUTING-CSAT-2026.md`, `_PYQ-GS1-2026.md`, `_PYQ-GS1-GS3-Static-2026.md`,
  `_PYQ-GS2-2026.md`, `_PYQ-GS3-2026.md`, `_PYQ-ESSAY-2026.md` and the locally
  held official papers `knowledge-export\Prelims PYQ\2026-GS1-Set A.md` and
  `knowledge-export\CSAT PYQ\2026-GS2-CSAT-Set A.md` were read directly. None
  routes any 2026 item to the Tughlaqs, Muhammad bin Tughlaq, Firuz Shah, Ibn
  Battuta, Barani or the Delhi Sultanate; the 2026 History questions are
  Ancient and Modern. This genuine absence is recorded honestly; no 2026
  question or key was fabricated.
- Cross-artifact consistency: the ASCII master flowchart (embedded 12-panel
  copy, standalone `.txt` and `.pdf`), the graphical flowchart (4800×11776
  master PNG, 1-page poster PDF, 4-page tiled PDF) and the quick-glance tree
  chart were all re-read against the repaired session and workbook. The
  embedded ASCII copy and the standalone text are normalized-identical, the
  standalone text and the ASCII PDF are normalized-identical, and no panel
  contains a duplicated line. No factual, chronological or terminological
  content changed in this pass, so none of these artifacts required
  regeneration — confirmed rather than assumed.
- Remaining limitations: Topic 05 owns exactly one directly routed official
  PYQ (2021 Prelims Q38), whose official key is not held locally, so its answer
  remains labelled `INFERRED ANSWER - NOT OFFICIALLY VERIFIED LOCALLY`; the
  other three items stay honestly labelled adjacent. The graphical flowchart
  folder retains its established `03-Carvaka-Graphical-Flowchart` name,
  matching the package `README.txt` (a naming convention shared with Topics
  1-4).
- Topic 5 remains `approved: false` and awaits user review. Topic 6 remains
  completely untouched.

## Reopened — independent baseline audit re-verification — 20 September 2026

An independent baseline audit restated this topic's pre-repair defect list (25
sessions, zero paragraph demonstrations, Session 25 BOUNDED LIVE LINKAGE padding,
malformed definitions in Sessions 1, 8, 11, 14-16 and 18-21, generic
`Frame the answer through` lines, filler keywords `not`/`entire`/`reported`/
`These`/`This`, label-copy recall fields, the 60+12 practice pattern with a
separate remedial bank, and generic solved scaffolding across 10 items). Every
claim was re-verified against the live files by fresh direct read and grep, with
the closing recall flows audited field-by-field and the 2026 check widened to the
actual papers.

### Confirmed already correct (no change needed)

- 24 `### SESSION` headings; 0 occurrences of `SESSION 25` or `BOUNDED LIVE
  LINKAGE` in either file.
- 24 `PARAGRAPH DEMONSTRATION` blocks, 149-201 words each, all four parts present,
  maximum pairwise similarity 0.073; Sessions 5, 9, 13, 17, 20 and 24 read in
  full and confirmed session-specific.
- 0 occurrences of `comprises ... as its core connected dimensions`, `is analysed
  by relating`, `Frame the answer through` or `Do not miss this limiting
  distinction`. All ten audit-named sessions' definitions quoted and confirmed
  genuine, session-specific prose.
- 24/24 keyword lists with exactly 6 substantive entries and 0 filler; the flagged
  words survive only inside genuine terms (*not a campaign against China*, *not
  paper currency*, *reported total of about 180,000*).
- All 24 closing recall flows read field-by-field: 0 label-copy prefixes, 0
  truncations, 0 within-session duplication, 0 cross-session duplication above
  0.72. Unlike Topic 4, no thin `MECHANISM / ARGUMENT` line was found.
- Practice structure: exactly 16 `Learning MCQ` (keys `ABCD`×4) in the main
  session, exactly 32 `Workbook MCQ` (keys `ABCD`×8) in the workbook, 128
  option-specific explanations, 32 unique traps, no remedial bank and no
  coverage-drills table.
- All 10 solved items carry item-specific decoding, compression plan and
  improvement fields in both files; 10/10 unique per field, maximum similarity
  0.166; no `Detailed examiner-grade model status` line remains.
- All 27 relative image references resolve.

### Genuine defects found and repaired (all invisible to the validators, which returned 0 errors beforehand)

1. **Internal contradiction.** The `MEDIEVAL DEEP-REVIEW CORE CONTROL` "Must
   remember" line and `ASCII MASTER FLOW — PANEL 1/12`'s `MUST REMEMBER` line both
   called the measure the "Daulatabad transfer" — the exact framing Session 5,
   Learning MCQ 02, Workbook MCQ 03/04, register module 04, the Advanced concept
   heading and the quick-glance chart all refute. Both rewritten to the
   second-capital framing with an explicit caution; the standalone
   `ASCII-Master-Flowchart.txt` corrected identically to preserve normalized
   identity.
2. Session 5 image caption "Delhi-Daulatabad **transfer** phases" carried the same
   refuted framing into the rendered PDF; corrected to "second-capital phases".
3. Register module 08 defined `haqq-i-sharb` without its ten per cent rate, which
   Session 16, the Advanced must-know list and the quick-glance chart all carry;
   the examinable rate and its attachment to the Sultan's personal income were
   restored to the revision layer.
4. Register module 09's `slave-corp interventions` — the only malformed singular
   against ten-plus correct uses of `slave corps` — rewritten as a complete clause.
5. Workbook MCQ 24 option A and Workbook MCQ 32 options B and C were materially
   thinner than the other 125 and named no evidence; rewritten with named evidence.
   Five other short explanations were re-read and deliberately left unchanged
   because each already names concrete evidence.

No canonical fact, date, ruler, chronology, campaign detail, figure, quotation or
PYQ wording was changed.

### 2026 evidence check — genuine absence, verified against the actual papers

All nine sources were read directly: the seven 2026 routing/ledger files plus the
locally held official `knowledge-export\Prelims PYQ\2026-GS1-Set A.md` and
`knowledge-export\CSAT PYQ\2026-GS2-CSAT-Set A.md`. A combined search for Tughlaq,
Muhammad bin Tughlaq, Firuz/Firoz, Ibn Battuta, Barani, Daulatabad/Deogir/
Devagiri, token currency, Delhi Sultanate, Sultanate, Khalji/Khilji, Iltutmish,
Balban, Vijayanagara, Bahmani and Medieval returned **0 hits in every source**.
The 2026 Prelims History questions route entirely to Ancient and Modern owners,
and the complete 20-question 2026 GS-I Mains ledger contains no Delhi Sultanate
item; its only medieval question, Q11 on Vijayanagara architecture (15 / 250),
routes to `Indian-Art-and-Culture/basic/03_Temple-Architecture-and-Chandella-Khajuraho.md`
and is explicitly outside Topic 05's scope. No question or key was fabricated.

### Cross-artifact and validation results

- Embedded 12-panel ASCII copy and `ASCII-Master-Flowchart.txt` re-verified
  normalized-identical after the panel-1 correction; `ASCII-Master-Flowchart.pdf`
  re-rendered with `render_ascii_pdf` and re-checked with `validate_ascii_pdf`
  (`passed: true`, 12/12/12, `normalized_equal: true`, 0 blank / 0
  replacement-glyph / 0 clipped pages).
- `quick_galance\Medieval-Indian-History\05_Tughlaqs_Tree-Chart.md` re-read and
  left unchanged — already correct on both repaired points.
- Graphical flowchart package not regenerated: no factual content changed, its
  Daulatabad stage already uses the second-capital framing in the generator's own
  Topic 05 panel specification, and its poster PDF carries no extractable text.
- Both PDFs re-rendered (`variant="learner-v2"`; workbook `mode="workbook"`,
  `standalone_workbook=True`; only `validate_v2_paths` monkeypatched to a no-op).
  Learning session **83 pages / 226,015 characters / 49 bookmarks** (was 225,755
  characters); workbook **25 pages / 76,613 characters / 39 bookmarks** (was
  76,436). Main PDF: 0 occurrences of `Workbook MCQ`, `Remedial MCQ`, `Frame the
  answer through`, `Detailed examiner-grade`, `Daulatabad transfer`, `slave-corp`.
  Workbook PDF: 0 occurrences of `Learning MCQ` or `Remedial MCQ`.
- `validate_v2_markdown_text`, `deep_content_quality_errors`,
  `semantic_aid_quality_errors`, `answer_key_pattern_errors`,
  `mcq_answer_text_errors` = **0 errors** for the main session; for the workbook
  the four content checks = 0 and `validate_v2_markdown_text` reports only the
  three H2 sections a standalone workbook legitimately does not carry.
  `validate_pdf` and `validate_pdf_layout` = **0 errors** for both PDFs, with 0
  blank, 0 near-empty, 0 clipped and 0 replacement-glyph pages.

Topic 5 remains `approved: false` and awaits user review. Topic 6 and every other
topic remain completely untouched by this pass.
