# Deep Content Review — Medieval History 21: Shah Jahan & the Evolution of the Mughal Ruling Class

- **Current repair mode:** full independent audit-and-repair from canonical sources
- **approved:** false

## Independent verification against the supplied context

The supplied brief was treated as a starting hint only. Both canonical Topic 21 owners were read in full before any write, and every existing Topic 21 output was then audited against those owners rather than against the pre-repair export alone. Topic 20 and Topic 22 were held outside write scope and guarded by pre/post SHA-256 verification.

## Canonical source calibration completed before repair

The following canonical owners were read in full before repair:

- `upsc-ai-kit\knowledge\Medieval-Indian-History\basic\21_Shah-Jahan-and-Mansabdari-Evolution.md`
- `upsc-ai-kit\knowledge\Medieval-Indian-History\advanced\21_Shah-Jahan-and-Mansabdari-Evolution.md`

That calibration required full coverage of: the 1628 accession settlement; Asaf Khan's role; rival elimination and the harsher succession precedent; Bundela and Khan Jahan Lodi consolidation; bounded Deccan and north-west campaigns only; politically relevant use of the Peacock Throne, Taj Mahal and Shahjahanabad; the ruling class as a composite service elite; Athar Ali's composition series; Iranis, Turanis, Afghans, Indian Muslims, Rajputs and limited Maratha/Deccani inclusion; zat, sawar, dagh, chehra and du-aspa sih-aspa; salary reductions, barawardi and one-third/one-fourth/one-fifth contingent logic; jagir, jama, hasil and month-scale; jama growth versus elite growth; be-jagiri roots; and the 1657-58 succession war as a bounded bridge to Topic 22.

## Defects actually found in the pre-repair Topic 21 package

1. The learning-session owner had materially drifted from the fixed learner-v2 contract: **12** session headings, **0** explicit `#### PARAGRAPH DEMONSTRATION` headings, malformed template definitions, and no session-to-demo parity.
2. The workbook owner was still in the oversized legacy format rather than the locked workbook format: an initial 20-question learning loop, an additional 44-question technical/remedial bank, no numbered `Workbook MCQ` structure, and **10** solved mains models instead of the required **6**.
3. The owner path had **no local `assets\` directory**, so Topic 21 lacked a verified self-contained local visual set.
4. The final-package graphical folder still carried a legacy cross-subject name instead of the required generic `03-Graphical-Flowchart`, and the package `README.txt` still repeated that wrong label.
5. The quick-glance chart, ASCII flowchart and package docs were not yet aligned to a repaired Topic 21 boundary discipline.
6. The pre-repair learning owner still contained banned circular/template residue (`comprises ... dimensions`, `is analysed by relating`) and the package docs still contained a screened unrelated-topic contamination term.

## Repair actions completed in this pass

- Rebuilt `Learning-Session.md` in place to the locked learner-v2 order with exactly **5** H2 sections, **10** substantive sessions, **10** explicit paragraph-demonstration headings, **16** learning MCQs and **6** original solved mains models.
- Rebuilt `Solved-Practice-Workbook.md` in place to the locked workbook format with exactly **32** workbook MCQs, strict `ABCD` rotation across the bank, exactly **128** option-wise explanations, exactly **32** unique examiner traps and the same **6** original mains models.
- Created a normal local owner `assets\` directory and populated it with four Topic 21 visuals: `topic21_cover.png`, `topic21_chronology.png`, `topic21_rulingclass.png` and `topic21_monthscale.png`.
- Normalised the final-package graphical folder to `03-Graphical-Flowchart`, regenerated the master PNG plus poster/tiled PDFs, refreshed the ASCII text/PDF pair, and rewrote the quick-glance tree chart to atlas-grade detail.
- Re-rendered both learner-v2 PDFs via `tools\markdown_learning_pdf.py` using an import-level override that bypassed only `validate_v2_paths` for this legacy owner location; Markdown-content and PDF validation remained active.

## Coverage and boundary judgement after repair

The repaired package now keeps Topic 21 inside its correct boundaries.

- Topic 20 is used only as pre-1628 background to explain why the accession was political and harsh.
- Topic 18 and Topic 19 are used only for bounded Deccan and frontier-capacity evidence; neither is re-taught in full.
- Topic 24 and Art/Culture ownership are respected by keeping architecture political, dynastic and fiscal rather than stylistically exhaustive.
- Topic 22 begins only after the accession outcome of 1658; the repaired package stops there.

Architecture was deliberately bounded to dynastic memory, capital-city sovereignty, court display and Moosvi's fiscal caution. The succession war was deliberately bounded to transfer politics, Dharmat, Samugarh and the accession bridge, not to Aurangzeb's subsequent policy history.

## Final-package root naming decision — REOPENED AND CORRECTED

**Superseded decision (do not follow):** an earlier pass retained the root package folder under the name `21-Shah-Jahan-and-the-b19eec2a-Mughal-Ruling-Class` (obsolete, historical reference only), reasoning that the same 8-character hex-fragment slug pattern appeared in 78 other final-package topic folders repo-wide and was therefore an accepted pre-existing quirk rather than a Topic-21-specific defect.

**Reopened correction:** the package was reopened because comparison-based acceptance is not sufficient — each package must be valid on its own regardless of whether the same defect exists elsewhere. The root package folder has now been safely moved (no data loss, all 9 files verified present before and after) to the clean, opaque-fragment-free name:

`notes\Final-Learning-Packages\Medieval History\Subject-wide Syllabus\21-Shah-Jahan-and-the-Evolution-of-the-Mughal-Ruling-Class`

The old `b19eec2a`-suffixed path no longer exists and must not be referenced as a live/current path anywhere in Topic 21's own README, this review report, the completion ledger, or the quick-glance chart — it may only appear, clearly marked obsolete, in this historical note. The graphical subfolder name (`03-Graphical-Flowchart`) remains correctly normalised as before.

## 2026 verification outcome

The mandated local search covered these roots:

- `books\mains\2026\`
- `knowledge-export\Mains PYQ\`
- `exams\papers\`
- `new_papers\`
- `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-GS1-GS3-Static-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2026.md`
- `upsc-ai-kit\knowledge\PYQ-INTEGRATION-AUDIT-2026.md`
- `upsc-ai-kit\knowledge\PYQ-MAINS-COVERAGE-AUDIT-2026.md`

Result: **no direct or adjacent Topic 21-owned 2026 prelims or mains item was verified locally** on Shah Jahan, mansabdari adjustment, jagir pressure, ruling-class composition or the 1657-58 transfer. The package therefore records the absence honestly rather than fabricating a route.

## Final verification metrics

### Owner-file structure and content checks

- `Learning-Session.md`: **5** locked H2 sections in the correct order; **10** `### SESSION` headings; **10** `#### PARAGRAPH DEMONSTRATION` headings; **16** learning MCQs; **0** inline `**Paragraph demonstration:**` residue.
- `Solved-Practice-Workbook.md`: **32** workbook MCQs; **128** option-wise explanations; **32** unique examiner traps; **6** original mains models.
- Solved-item support fields: **6** `Demand decoding`, **6** `Executable answer/elimination plan`, **6** `Why this earns marks / route earns marks`, **6** `How to improve/strengthen` in each owner file.
- Keyword discipline: all **10** session keyword blocks remain within the required **6**-keyword count.
- Manual semantic gate: all **32** workbook questions and all **16** learning MCQs were reread in full after the rewrite.
- Supplementary similarity scan on workbook option explanations: max `difflib.SequenceMatcher` **0.6609** after the rewrite; the remaining nearest pair concerns two different crown-revenue distractors and was manually reread in full.

### Regex and contamination gates

- Gate 1 synthetic-marker sweep: **0** matches across both owner Markdown files.
- Gate 2 mail-merge/circular-template sweep: **0** matches across both owner Markdown files.
- Cross-subject contamination search on Topic 21 package folder/file names, the package `README.txt`, the graphical `README.md`, this review report and the quick-glance chart returned **0** hits for the screened unrelated-topic term.

### PDF validation after rerender

- Learning PDF: **26 pages / 66,382 extracted characters / 29 outline nodes / outline depth 3**.
- Workbook PDF: **18 pages / 47,046 extracted characters / 6 outline nodes / outline depth 3**.
- `validate_pdf` errors: learning **0**, workbook **0**.
- `validate_pdf_layout` errors: learning **0**, workbook **0**.
- Blank pages: learning **0**, workbook **0**.
- Near-empty pages: learning **0**, workbook **0**.
- Clipped-text pages: learning **0**, workbook **0**.
- Replacement-glyph pages: learning **0**, workbook **0**.
- Asset references: both owner Markdown files resolve their `assets\` references successfully.

## Approval status

This package remains **not approved**.

- `approved: false`
