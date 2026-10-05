# Deep Content Review — Medieval History 11: Art, Architecture & Culture of the Sultanate

- **Baseline locked:** `medieval-indian-history-11:learner-v2:g3` — 97/100
- **Immutable successor reference:** `medieval-indian-history-11:learner-v2:g4` — 98/100
- **Current repair mode:** in-place deep review / repair within locked writable roots only
- **approved:** false

## Before-repair diagnosis

The owner files were content-rich but not Topic 09/10-compliant.

### Gaps found

1. `Learning-Session.md` was structurally non-compliant:
   - 34 H3 blocks including residue such as deep-review control scaffolding and legacy routing text
   - 18 learning MCQs plus 40 broad-coverage MCQs plus 12 remedial MCQs instead of the locked 16-MCQ notes section
   - 10 Mains items instead of the required 6 originals
   - missing per-session paragraph-demonstration blocks and template-heavy opening/keyword/recall scaffolds
2. `Solved-Practice-Workbook.md` was non-compliant:
   - only two broad legacy sections
   - no locked 32 `Workbook MCQ N` structure
   - no final 128 option-wise explanations / 32 unique traps format
   - answer rotation not locked to `ABCD` x 8
3. Topic-content tightening was required:
   - trabeate/arcuate continuity vs expansion needed a non-invention framing
   - materials, mortar, craft labour and regional ecology needed explicit analytical ownership
   - Sayyid-Lodi transition, Delhi's multiple-city landscape, language/literature/music, manuscript-performance caution and source method needed firmer integration
4. Owner-folder asset handling had to be checked from the writable Topic 11 path.
5. Mandatory 2026 verification had to be completed honestly from local papers / ledgers.

## Repair actions completed

### Owner files

- Rebuilt the Topic 11 learning session into the locked learner-v2 teaching spine:
  - exact five H2 order retained
  - 12 substantive sessions only; padding / residue removed
  - one paragraph-demonstration block per session
  - one validator-readable opening, keyword block and closure-flow per session
  - 16 learning MCQs with strict `ABCDABCDABCDABCD` rotation
- Rebuilt the standalone workbook into the locked format:
  - 32 workbook MCQs
  - strict `ABCDABCDABCDABCDABCDABCDABCDABCD` answer rotation
  - 128 option-wise explanations
  - 32 unique examiner traps
  - no duplicate remedial second bank
  - same 2 routed/adjacent solved items + 6 original Mains carried across with locked support fields
- All 8 solved items in both Markdown owners now carry:
  - `Demand decoding`
  - executable plan field (`Executable elimination plan` / `Executable answer/compression plan`)
  - marks-rationale field (`Why this route earns marks` / `Why this earns marks`)
  - item-specific improvement field (`How to strengthen this route` / `How to improve this answer`)

### Topic-content repairs enforced

- Preserved full source-owned coverage of rupture / adaptation / localisation, trabeate-arcuate vocabulary, true arch vs corbelled opening, dome transition, lime mortar and workshop labour.
- Strengthened named monument sequencing through Quwwat-ul-Islam, Adhai Din ka Jhonpra, Qutb Minar, Sultan Ghari, Iltutmish's tomb, Balban's tomb, Alai Darwaza, Siri, Alai Minar, Hauz-i-Alai, Tughlaqabad, Ghiyasuddin's tomb, Jahanpanah, Adilabad, Firoz Shah Kotla, Hauz Khas and Sikandar Lodi's tomb.
- Preserved bounded regional comparison for Bengal, Gujarat, Malwa/Mandu and Jaunpur, with only limited Deccan cross-reference and no Bahmani re-teaching.
- Rewrote ornament/function coverage around calligraphy, arabesque, geometry, jaali, bounded aniconism and building-type function.
- Rewrote language/literature/music coverage around Persian, Arabic, Sanskrit, Hindavi/regional growth, Amir Khusrau attribution caution, and uneven manuscript/performance survival.
- Added explicit source-method and conservation discipline, including honest 2026 absence handling and non-duplication of Topic 09's Vijayanagara-owned 2026 item.

### Workbook anti-template verification

- Independent explanation scan after the rewrite:
  - max `difflib.SequenceMatcher` similarity across the 128 explanations: **0.7273** (pass threshold `< 0.75`)
  - max 5-gram Jaccard overlap across the 128 explanations: **0.0714** (pass threshold `< 0.10`)
- Trap recount after the rewrite:
  - exactly **32** trap lines
  - exactly **32** unique trap strings

### Asset handling

- Topic 11 initially had **no owner-local `assets\` directory**.
- Created a normal local owner directory at `learning_package_final\Medieval-History\Subject-wide-Syllabus\11-Art,-Architecture-&-Culture-of-the-Sultanate\assets` and copied the canonical learner-v2 image set into it.
- Post-repair verification: `Attributes : Directory`, no `LinkType`, no `Target`, local file count **35**.
- Final `Learning-Session.md` asset audit: **16** `assets/` references, all resolving locally; no missing references.

## Mandatory 2026 PYQ verification

### Checked locally

- official 2026 Mains papers / transcriptions under `books\mains\2026\` and `knowledge-export\Mains PYQ\`
- 2026 route ledgers including:
  - `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md`
  - `upsc-ai-kit\knowledge\_PYQ-GS1-GS3-Static-2026.md`
  - `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2026.md`
  - `upsc-ai-kit\knowledge\PYQ-INTEGRATION-AUDIT-2026.md`
  - `upsc-ai-kit\knowledge\PYQ-MAINS-COVERAGE-AUDIT-2026.md`
- local OCR / owned-topic verification surfaces including `upsc-ai-kit\knowledge\Medieval-Indian-History\basic\11_Sultanate-Art-and-Architecture.md`

### Result

- **No Topic 11-owned 2026 prelims or mains item was verified locally.**
- The verified 2026 GS-I architecture item is on **Vijayanagara architecture** and remains Topic 09-owned; it was intentionally not duplicated here.
- The two solved routed items retained here are older adjacent items only:
  - 2018 GS-I Q1 on safeguarding Indian art heritage (primary Heritage Conservation owner)
  - CAPF 2017 Q50 on the first extant true arch (adjacent competitive-exam discriminator)

## Rendering and validation

### Rendering

Rendered both PDFs in place with `tools\markdown_learning_pdf.py` using learner-v2 mode. Only the owner-path gate `validate_v2_paths` was bypassed; content validation and PDF validation were not bypassed.

### Validation results

- `Learning-Session.md`
  - H2 count: **5**
  - sessions: **12**
  - learning MCQs: **16**
  - answer rotation: `ABCDABCDABCDABCD`
  - solved routed/adjacent items: **2**
  - original mains: **6**
  - support-field families: **8 / 8 / 8 / 8**
  - `validate_v2_markdown_text`: **0** errors
  - `deep_content_quality_errors`: **0** errors
  - `answer_key_pattern_errors`: **0** errors
- `Solved-Practice-Workbook.md`
  - workbook MCQs: **32**
  - answer rotation: `ABCD` repeated **8** times
  - option-wise explanations: **128**
  - unique examiner traps: **32**
  - solved routed/adjacent items: **2**
  - original mains: **6**
  - support-field families: **8 / 8 / 8 / 8**
  - `answer_key_pattern_errors`: **0** errors
- PDF integrity
  - learning PDF: **34 pages / 94,932 extracted characters / 27 bookmarks**
  - workbook PDF: **18 pages / 46,828 extracted characters / 6 bookmarks**
  - `validate_pdf`: **0** errors for both
  - `validate_pdf_layout`: **0** errors for both; blank / near-empty / clipped / replacement-glyph pages = **0** in both outputs

## Approval status

This package remains **not approved**.

- `approved: false`
- Any final approval must come from an explicit later approval step; this repair pass does not self-approve.


## Reopened correction — synthetic-marker integrity failure (20 September 2026)

- **approved:** false
- **Reason for reopening:** an independent audit found that the workbook's 128 option-wise explanations still contained generator debris such as `Q1B`, `B-choice removed`, `tag cpws`, `false-A route`, `option-text=` and similar synthetic routing labels.
- **Scope discipline:** only Topic 11 owner Markdown, Topic 11 final-package PDFs, the Topic 11 final-package `README.txt`, this review report and the review/repair ledger were edited. Topic 12 and every other topic remained outside the write scope.

### Representative before → after repairs

1. **Workbook MCQ 1, option B**  
   Before: `Q1B | B-choice removed | cpws marker | "All earlier Indian buildings were structurally identical.".`  
   After: `Incorrect. Pre-Sultanate Indian building traditions were never structurally identical; they already included multiple regional materials, forms and construction habits.`
2. **Workbook MCQ 2, option A**  
   Before: `Q2A | false-A route | "a dome springing directly from a square without transition." | tag trrh.`  
   After: `Incorrect. A dome springing from a square raises the transition problem between the chamber below and the dome above; it does not define a trabeate roof.`
3. **Workbook MCQ 4, option B**  
   Before: `Q4B | B-route cancelled | cue tag cuip | claim="a horizontal lintel set between two supports.".`  
   After: `Incorrect. A horizontal lintel between two supports is the classic trabeate solution, whereas corbelling works by inward projection of courses.`
4. **Workbook MCQ 9, option B**  
   Before: `Q9B | B-choice removed | quis marker | "proof that all Sultanate mosques reused identical temple fabric.".`  
   After: `Incorrect. The monument does not prove that every Sultanate mosque reused temple fabric in the same way; that would turn a site-specific case into an empire-wide rule.`
5. **Workbook MCQ 31, option C**  
   Before: synthetic routing prose rather than a human explanation.  
   After: `Correct. This is the source-grounded position: Khusrau's literary and cultural importance is strong, while sweeping claims about inventing specific instruments or genres are not securely established.`

### Zero-match verification on owner Markdown

Final PowerShell sweep after the rewrite used `Select-String` against both owner files for these pattern families: `Q\d+[A-D]\b`, `\btag [a-z]+\b`, `\bmarker\b`, `false-[A-D] route`, `[A-D]-choice removed`, `[A-D]-option rejected`, `\bfilter removes\b`, `option-text=`, `exact text=`, `\bdistractor clashes\b`, `\bsurvives because\b`, `\b[a-z]{4}\b marker`, `\btag [a-z]{4}\b`, `cue[- ]tag`, `quoted option=`, `quoted-choice`, `signal=`, `memory-rule=`, `correct-line=`, `retained-[A-D] line`, `do-not-mark`, `claim=`, `text=`, `option=`, `cue=`, `filter=` and `verdict:`. The final sweep returned **0 matches** in both `Learning-Session.md` and `Solved-Practice-Workbook.md`.

### Validation after reopening

- Rewritten workbook explanations: **128 / 128** in natural prose; exact 32-question set, key rotation `ABCDABCDABCDABCDABCDABCDABCDABCD`, and 32 trap lines preserved.
- Secondary similarity check after the rewrite: max `difflib.SequenceMatcher` **0.6897**; max 5-gram Jaccard **0.0938**.
- `Learning-Session.md`: `validate_v2_markdown_text` **0**, `deep_content_quality_errors` **0**, `answer_key_pattern_errors` **0**.
- `Solved-Practice-Workbook.md`: `answer_key_pattern_errors` **0**.
- Re-rendered learner-v2 PDFs: learning PDF **34 pages / 93,311 extracted chars / 27 bookmarks**; workbook PDF **19 pages / 49,805 extracted chars / 6 bookmarks**.
- `validate_pdf`: **0** errors on both PDFs.
- `validate_pdf_layout`: **0** errors on both PDFs; blank / near-empty / clipped / replacement-glyph pages = **0** for both outputs.

### Unchanged-scope confirmation

Post-repair timestamp/hash verification was re-run on Topic 12's `Learning-Session.md` and `Solved-Practice-Workbook.md`; both remained unchanged from the pre-pass baseline. Topic 11 therefore remains the only content owner modified in this reopened correction, and it remains **approved: false** pending explicit user approval.
