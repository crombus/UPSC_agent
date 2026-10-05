# Deep Content Review — Medieval History 09: Vijayanagara & the Bahmani Kingdom (Deccan)

- **Baseline locked:** `medieval-indian-history-09:learner-v2:g6` — 97/100
- **Immutable successor reference:** `medieval-indian-history-09:learner-v2:g7` — 98/100
- **Current repair mode:** in-place deep review / repair within locked writable roots only
- **approved:** false

## Before-repair diagnosis

The owner files were structurally close to learner-v2, but not compliant with the locked Topic 1–8 repair standard.

### Gaps found

1. `Learning-Session.md` contained the correct five-H2 order, but its internals were non-compliant:
   - 16 real sessions plus stray non-compliant residue (`### 18...`, `SESSION 17 — BOUNDED LIVE LINKAGE`)
   - no required `PARAGRAPH DEMONSTRATION — CLAIM → EVIDENCE → ANALYSIS → QUALIFICATION` blocks
   - recurring template language in framing / keyword-use guidance
   - weak filler keywords in several recall fields
   - extra workbook-like banks embedded inside the notes file
2. Notes package carried excess practice payload:
   - 16 learning MCQs
   - 40 broad-coverage MCQs
   - 12 remedial trap MCQs
   - 8 original mains models
   This violated the locked Topic 09 target of 16 learning MCQs and 6 original mains models in the session file.
3. `Solved-Practice-Workbook.md` was not aligned to the locked workbook standard:
   - duplicated objective-bank logic
   - not locked to exactly 32 MCQs
   - did not present the required 128 option-wise explanations / 32 unique traps in the final compliant format
4. Topic 09 continuity framing required correction:
   - Talikota had to reject the "instant end" myth explicitly
   - post-1565 Penukonda / Chandragiri continuation needed clearer emphasis
5. 2026 routing verification was mandatory and had to be handled honestly from a local official paper source.

## Repair actions completed

### Owner files

- Rebuilt the Topic 09 learning session into a clean locked learner-v2 spine:
  - exactly 16 visual-first sessions
  - distinct framing per session
  - one paragraph-demonstration block per session
  - 5–6 substantive keywords per session (audited to 6 each)
- Removed the stray comparative-residue section and the non-compliant `SESSION 17` block.
- Preserved the five required H2 headings in exact order:
  1. `BASIC LEARNING SESSION`
  2. `BASIC MCQS / REMEDIATION`
  3. `PYQS AND ANSWER PRACTICE`
  4. `OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER`
  5. `CONSOLIDATED REGISTER NOTES`
- Kept the notes file locked to:
  - 16 learning MCQs
  - 4 solved direct/routed PYQs
  - 6 original mains models (2x10, 2x15, 2x20)
- Rebuilt the workbook into the locked standalone format:
  - 32 workbook MCQs
  - strict answer rotation `A-B-C-D` repeated 8 times
  - 128 option-wise explanations
  - 32 unique examiner traps
  - no duplicate remedial second bank
  - same solved PYQ + six-mains support spine carried into workbook practice

### Topic-content repairs enforced

- Strengthened foundation-debate caution around the 1336 convention.
- Kept Harihara/Bukka, Sangama chronology, Deva Raya I / II, Krishnadevaraya, *Amuktamalyada*, Portuguese-horse-trade linkage, amaram/nayankara with ayagar caution, Hampi urbanism, travellers, women, multilingual court-culture, Bahmani foundation, Gulbarga-Bidar shift, taraf logic, Deccani-Afaqi conflict, Mahmud Gawan, Talikota and post-1565 continuity.
- Explicitly rejected the "1565 = instant end" myth and restored Penukonda/Chandragiri continuity framing.
- Kept successor sultanates bounded to contextual mention only.

### Reconciled package companions

- Updated the quick-glance tree chart with the verified 2026 routed architecture support note.
- Updated the package `README.txt` to reflect repaired locked counts and new PDF page counts.
- Reused the existing local owner-folder `assets` junction so learner-v2 rendering could resolve image references from the writable owner path.

## Mandatory 2026 PYQ verification

### Verified locally

- **Question:** `Vijayanagara architecture exemplifies the amalgamation of past traditions with contemporary practices. Elucidate with examples.`
- **Paper slot:** GS-I Q11
- **Marks / word limit:** 15 marks / 250 words
- **Verification path:**
  - official local paper: `books\mains\2026\QP-CSM-26-010926-GENERAL STUDIES PAPER - I.pdf`
  - readable OCR derivative used for exact wording: `knowledge-export\Mains PYQ\QP-CSM-26-010926-GENERAL STUDIES PAPER - I.pdf.md`
  - provenance metadata: `knowledge-export\Mains PYQ\QP-CSM-26-010926-GENERAL STUDIES PAPER - I.pdf.json`
- **Routing status:** `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md` routes this question primarily to Indian Art & Culture, so Topic 09 includes it honestly as a **routed architecture-support PYQ**, not as a falsely claimed primary-owner question.

### Other 2026 topic-relevant routing references checked

- Root 2026 routing / audit ledgers were searched for additional Topic 09-specific items.
- Result:
  - `verified-local`: GS-I Q11 architecture route
  - `not-found`: no additional clearly Topic-09-specific 2026 Bahmani / Talikota / Deva Raya / Mahmud Gawan routing item was verified locally from the repo's 2026 ledgers during this repair pass

## Rendering and validation

### Rendering

Rendered with `tools\markdown_learning_pdf.py` using learner-v2 mode.

Because the owner paths live under the deep-review repair tree rather than canonical v2 export paths, **only `validate_v2_paths` was bypassed** during rendering. Content validation and PDF validation were not bypassed.

### Validation results

- `Learning-Session.md`
  - H2 count: 5
  - sessions: 16
  - learning MCQs: 16
  - solved PYQs: 4
  - original mains: 6
  - keyword blocks: 16 / all audited to 6 keywords each
- `Solved-Practice-Workbook.md`
  - workbook MCQs: 32
  - option-wise explanations: 128
  - unique examiner traps: 32
  - solved PYQs: 4
  - original mains: 6
  - answer rotation: `ABCD` repeated 8 times
- PDF integrity
  - learning PDF: 41 pages, validator OK, readable via `pypdf`
  - workbook PDF: 22 pages, validator OK, readable via `pypdf`

## Approval status

This package remains **not approved**.

- `approved: false`
- Any final approval must come from an explicit later approval step; this repair pass does not self-approve.


## Reopened strict repair — 20 September 2026

- **Trigger:** independent audit reopened Topic 09 only and required five concrete fixes: cloned workbook option explanations, missing solved-item support fields, a junction-backed `assets\` owner, missing completion-record coverage, and a full post-repair recount/PDF re-validation.
- **Defect 1 fixed — workbook explanations rewritten completely:** all **128** option-wise explanations (32 MCQs × 4 options) were rewritten item-specifically while preserving the exact 32 stems, answer key `ABCD` × 8 and the existing 32 trap lines. The generic boilerplate family (`Not the best choice because it misses the question's decisive clue...`) is gone. Sample repair: Workbook MCQ 1 now rejects option B because the Kaveri/Punjab/Kabul set belongs to other agrarian/frontier theatres, rejects option C because Ganga-Yamuna/Kashmir/Bengal are non-Deccan regions, and rejects option D because Malwa-Gujarat-Mewar belongs to Topic 08's regional-state field. Independent scan result: max `SequenceMatcher` similarity **0.6751** (pass threshold `< 0.75`) and max 5-gram Jaccard overlap **0.0417** (pass threshold `< 0.10`).
- **Defect 2 fixed — all solved items now carry the locked support fields:** all **10** solved items in both `Learning-Session.md` and `Solved-Practice-Workbook.md` now contain `Demand decoding`, the appropriate executable plan field (`Executable elimination plan` for 3 objective PYQs; `Executable answer/compression plan` for the 2026 GS-I descriptive PYQ plus all 6 original Mains), the appropriate marks-rationale field (`Why this route earns marks` / `Why this earns marks`), and the appropriate improvement field (`How to strengthen this route` / `How to improve this answer`). The exact 2026 GS-I Q11 wording, **15 marks**, **250 words**, and verified-local routed-support status were preserved; only the four missing support fields were added around the existing model answer.
- **Defect 3 fixed — owner assets are now local, not a junction:** the Topic 09 `assets\` owner path was first audited against the canonical read-only target (`upsc-ai-kit\knowledge\Learner-v2-Refreshed\Medieval\MH\learning-sessions\mhi-09\g7\assets`) with **28** files present. The junction itself was then removed safely with `.Delete()` (non-recursive), the canonical target was re-checked and remained intact with the same 28 files, a normal local `assets\` directory was created at the owner path, and all 28 asset files were copied into it. Post-fix verification: owner `Attributes : Directory` with no `ReparsePoint`, local file count **28** matching the canonical target, and all **23** `assets/` references in `Learning-Session.md` resolve against the new local copy.
- **Defect 4 fixed — audit paperwork brought into sync:** this review report now records the reopened-audit defects and their verified closure, and `learning_package_final\REVIEW-AND-REPAIR-INSTRUCTIONS.md` now carries an honest Topic 09 completion record for this second repair pass. `approved: false` remains unchanged.
- **Defect 5 fixed — mechanical recount and PDF re-validation completed:** `Learning-Session.md` contains exactly **16** `Learning MCQ` items with rotation `ABCDABCDABCDABCD`; `Solved-Practice-Workbook.md` contains exactly **32** `Workbook MCQ` items with rotation `ABCDABCDABCDABCDABCDABCDABCDABCD`; the workbook now contains exactly **128** distinct option explanations and **32** unique trap strings; the solved section contains exactly **4** PYQs and **6** original Mains models; and all 10 solved items passed the support-field audit. Original Mains mark/word conventions are now verified mechanically as 10 marks = 150 words, 15 marks = 250 words, 20 marks = 250 words, with counted model-answer bodies of **127**, **128**, **226**, **209**, **234** and **215** words respectively.
- **PDF re-render / parse result:** both learner-v2 PDFs were regenerated in place through `tools\markdown_learning_pdf.py` with only `validate_v2_paths` bypassed. `pypdf` parsed both outputs cleanly: learning PDF **44 pages / 97,213 extracted characters / 28 bookmarks**; workbook PDF **23 pages / 62,663 extracted characters / 6 bookmarks**.
- **Scope discipline:** the targeted git-status check after repair listed Topic 09 paths only; Topic 10 does not appear in the changed-path set for this pass.
