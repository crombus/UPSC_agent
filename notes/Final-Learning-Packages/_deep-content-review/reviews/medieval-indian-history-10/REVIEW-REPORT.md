# Deep Content Review — Medieval History 10: The Bhakti & Sufi Movements

- **Baseline locked:** `medieval-indian-history-10:learner-v2:g5` — 97/100
- **Immutable successor reference:** `medieval-indian-history-10:learner-v2:g6` — 98/100
- **Current repair mode:** in-place deep review / repair within locked writable roots only
- **approved:** false

## Before-repair diagnosis

The owner files were content-rich but not compliant with the Topic 09 strict repair standard.

### Gaps found

1. `Learning-Session.md` was structurally non-compliant:
   - 15 sessions including a stray bounded-live-linkage residue
   - no required paragraph-demonstration support blocks
   - templated definition/opening/keyword scaffolding across multiple sessions
   - 68 objective-question headings instead of the locked 16-learning-MCQ notes format
2. `Solved-Practice-Workbook.md` was non-compliant:
   - duplicated broad/remedial-bank logic
   - not locked to exactly 32 workbook MCQs
   - no final 128 option-wise explanations / 32 unique examiner traps structure
   - solved-item support fields were generic and not item-specific
3. Topic-content tightening was required:
   - later Sufi order handling needed Qadiri + Shattari + Naqshbandi clarity
   - Bhakti literature / vernacularisation needed stronger named language-text-institution mapping
   - Bhakti-Sufi comparison and social-protest historiography needed bounded, source-owned phrasing
4. Owner-folder asset handling had to be checked from the writable Topic 10 path.
5. Mandatory 2026 verification had to be completed honestly from local papers / ledgers.

## Repair actions completed

### Owner files

- Rebuilt the Topic 10 learning session into the locked learner-v2 teaching spine:
  - exact five H2 order retained
  - 14 substantive sessions only; padding residue removed
  - one paragraph-demonstration block per session
  - one validator-readable opening, keyword block and closure-flow per session
  - 16 learning MCQs with strict `ABCD` × 4 rotation
- Rebuilt the standalone workbook into the locked format:
  - 32 workbook MCQs
  - strict `ABCD` × 8 answer rotation
  - 128 option-wise explanations
  - 32 unique examiner traps
  - no duplicate remedial second bank
  - same 4 routed PYQs + 6 original Mains carried across with locked support fields
- All 10 solved items in both Markdown owners now carry:
  - `Demand decoding`
  - executable plan field (`Executable elimination plan` / `Executable answer/compression plan`)
  - marks-rationale field (`Why this route earns marks` / `Why this earns marks`)
  - item-specific improvement field (`How to strengthen this route` / `How to improve this answer`)

### Topic-content repairs enforced

- Preserved full source-owned coverage of Alvar-Nayanar antecedents, Ramanuja / Nimbarka / Madhva / Vallabha, Namdev / Ramananda, Kabir, Guru Nanak, Chaitanya, Mirabai, Tulsidas, Surdas, Eknath, Tukaram, Narsinha Mehta and Shankaradeva.
- Kept the Sufi matrix bounded to the actual owned corpus: Chishti, Suhrawardi, Qadiri, Shattari and Naqshbandi, plus Muinuddin Chishti, Bakhtiyar Kaki, Baba Farid, Nizamuddin Auliya, Bahauddin Zakariya, Muhammad Ghawth, Baqi Billah and Ahmad Sirhindi.
- Strengthened doctrinal / institutional precision around fana, silsilah, pir-murid, khanqah, dargah, sama, ziyarat, wahdat al-wujud / wahdat al-shuhud, futuh-waqf, shrine formation and multi-causal conversion.
- Rewrote Bhakti-Sufi comparison into a source-owned symbiosis / parallel-exchange frame rather than merger or one-way borrowing.
- Rewrote historiography and social-protest coverage around hagiography, oral corpus, malfuzat, Janamsakhi, inscriptions, endowments and provenance caution.

### Workbook anti-template verification

- Independent explanation scan after the rewrite:
  - max `difflib.SequenceMatcher` similarity across the 128 option explanations: **0.7254** (pass threshold `< 0.75`)
  - max 5-gram Jaccard overlap across the 128 option explanations: **0.0500** (pass threshold `< 0.10`)
- Trap recount after the rewrite:
  - exactly **32** trap lines
  - exactly **32** unique trap strings

### Asset handling

- Topic 10 initially had **no owner-local `assets\` directory**.
- Created a normal local owner directory at `learning_package_final\Medieval-History\Subject-wide-Syllabus\10-The-Bhakti-&-Sufi-Movements\assets` and copied the canonical learner-v2 image set into it.
- Post-repair verification: `Attributes : Directory`, no `LinkType`, no `Target`, local file count **28**.
- Final `Learning-Session.md` asset audit: **26** `assets/` references, all resolving locally; no missing references.

## Mandatory 2026 PYQ verification

### Checked locally

- official 2026 Mains papers under `books\mains\2026\`
- 2026 route ledgers including:
  - `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md`
  - `upsc-ai-kit\knowledge\_PYQ-GS1-GS3-Static-2026.md`
  - `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2026.md`
  - `upsc-ai-kit\knowledge\PYQ-INTEGRATION-AUDIT-2026.md`
  - `upsc-ai-kit\knowledge\PYQ-MAINS-COVERAGE-AUDIT-2026.md`
- local OCR/export surfaces under `knowledge-export\Mains PYQ\` and prior text-derivative search roots used in Topic 09/10 routing verification

### Result

- **No clearly relevant 2026 Bhakti / Sufi / Kabir / Nanak / Chaitanya / Chishti / Suhrawardi / Bhakti-literature prelims or mains item was verified locally.**
- This absence is recorded honestly here; no 2026 wording or answer was fabricated.

## Rendering and validation

### Rendering

Rendered both PDFs in place with `tools\markdown_learning_pdf.py` using learner-v2 mode.
Only the owner-path gate `validate_v2_paths` was bypassed; content validation and PDF validation were not bypassed.

### Validation results

- `Learning-Session.md`
  - H2 count: **5**
  - sessions: **14**
  - learning MCQs: **16**
  - answer rotation: `ABCDABCDABCDABCD`
  - solved PYQs: **4**
  - original mains: **6**
  - support-field families: **10 / 10 / 10 / 10**
  - `validate_v2_markdown_text`: **0** errors
  - `deep_content_quality_errors`: **0** errors
  - `answer_key_pattern_errors`: **0** errors
- `Solved-Practice-Workbook.md`
  - workbook MCQs: **32**
  - answer rotation: `ABCD` repeated **8** times
  - option-wise explanations: **128**
  - unique examiner traps: **32**
  - solved PYQs: **4**
  - original mains: **6**
  - support-field families: **10 / 10 / 10 / 10**
  - `answer_key_pattern_errors`: **0** errors
  - standalone workbook note: `validate_v2_markdown_text` reports only the three expected missing canonical notes-only H2 headings
- PDF integrity
  - learning PDF: **42 pages / 96,174 extracted characters / 31 bookmarks**
  - workbook PDF: **19 pages / 50,302 extracted characters / 7 bookmarks**
  - `validate_pdf`: **0** errors for both
  - `validate_pdf_layout`: **0** errors for both; blank / near-empty / clipped / replacement-glyph pages = **0** in both outputs

## Approval status

This package remains **not approved**.

- `approved: false`
- Any final approval must come from an explicit later approval step; this repair pass does not self-approve.
