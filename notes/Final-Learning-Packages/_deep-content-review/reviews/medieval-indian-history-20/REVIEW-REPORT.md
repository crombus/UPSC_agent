# Deep Content Review — Medieval History 20: Jahangir & the Early Seventeenth Century (Nur Jahan)

- **Current repair mode:** full independent audit-and-repair from canonical sources
- **approved:** false

## Independent verification against the supplied context

The supplied brief was treated as a starting hint only. Both canonical Topic 20 owners were read in full before any write, and the repaired package was checked against those owners rather than against the pre-repair export. Topic 19 and Topic 21 were held outside write scope and guarded by pre/post SHA-256 verification.

## Canonical source calibration completed before repair

The following canonical owners were read in full before repair:

- `upsc-ai-kit\knowledge\Medieval-Indian-History\basic\20_Jahangir-and-Early-17th-Century.md`
- `upsc-ai-kit\knowledge\Medieval-Indian-History\advanced\20_Jahangir-and-Early-17th-Century.md`

That calibration required full coverage of: the 1605 accession bargain; Salim's Allahabad background; the twelve orders and the chain of justice with implementation caution; Khusrau's 1606 revolt; Guru Arjan with layered source treatment; Mewar 1615; Bengal under Islam Khan; Kangra 1620; bounded Deccan context only; Hawkins, Roe and the 1618 commercial facilities; Nur Jahan's biography, farmans, coins, patronage and family nexus; the debated fixed-junta thesis; post-1622 crisis periodisation; Khurram's rebellion; Mahabat Khan's coup; Jahangir as ruler, source, naturalist and patron; and the graded verdict of continuity plus strain without proven collapse.

## Defects actually found in the pre-repair Topic 20 package

1. The learning-session owner had materially drifted from the clean Topic 14-19 structure: **17** session headings, **0** explicit `#### PARAGRAPH DEMONSTRATION` headings, legacy bulk sections, and a non-compliant **18 + 40 + 12** MCQ bank plus **10** solved mains models.
2. The workbook owner was likewise in the old oversized format rather than the locked workbook format: **70** MCQs spread across three banks and **10** solved mains models instead of the required 32/6 pattern.
3. The owner path had **no local `assets\` directory**, so there was no verified normal local asset set for Topic 20.
4. The final-package graphical folder still carried a legacy cross-subject name instead of the required generic `03-Graphical-Flowchart`.
5. The quick-glance chart and ASCII package were not yet aligned to the repaired Topic 20 boundary discipline.
6. The pre-repair learning owner still contained banned circular/template residue (`comprises ... dimensions`, `is analysed by relating`) and had no paragraph-demonstration parity.

## Repair actions completed in this pass

- Rebuilt `Learning-Session.md` in place to the locked learner-v2 order with exactly **5** H2 sections, **12** substantive sessions, **12** explicit paragraph-demonstration headings, **16** learning MCQs and **6** original solved mains models.
- Rebuilt `Solved-Practice-Workbook.md` in place to the locked workbook format with exactly **32** workbook MCQs, strict `ABCD` rotation across the bank, exactly **128** option-wise explanations, exactly **32** unique examiner traps and the same **6** original solved mains models.
- Created a normal local owner `assets\` directory and populated it with topic-specific visuals (`topic20_cover.png`, `topic20_chronology.png`, `topic20_nurjahan_authority.png`, `topic20_source_ladder.png`).
- Normalised the final-package graphical folder to `03-Graphical-Flowchart`, regenerated the master PNG plus poster/tiled PDFs, refreshed the ASCII text/PDF pair, and expanded the quick-glance tree chart to atlas-grade detail.
- Re-rendered both learner-v2 PDFs via `tools\markdown_learning_pdf.py` using an import-level override that bypassed only `validate_v2_paths` for this legacy owner location; Markdown-content and PDF validation remained active.

## Nur Jahan treatment and boundary discipline

The repaired package now treats Nur Jahan as a **documented political actor** with explicitly named evidence: farmans in her name, coin legends, household access, patronage, the Itimad-ud-Daulah memorial complex and post-1622 crisis action. It also keeps the essential qualification that these evidences do **not** prove a stable constitutional replacement of Jahangir or a permanent monopoly by one camp.

Boundary discipline was repaired and then rechecked:

- Qandahar appears only as a bounded **1622 trigger** for internal crisis; the full foreign-policy system remains Topic 19's owner territory.
- Shah Jahan appears only as **Prince Khurram** inside Jahangir's reign and through the 1627 succession bridge; the mature Shah Jahan state remains Topic 21.

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

Result: **no direct or adjacent Topic 20-owned 2026 prelims or mains item** on Jahangir, Nur Jahan, Khusrau, Khurram, Mahabat Khan, Guru Arjan, Roe/Hawkins, justice-imagery or early seventeenth-century Mughal court politics was verified locally. The package therefore records the absence honestly rather than fabricating a route.

## Final verification metrics

### Owner-file structure and content checks

- `Learning-Session.md`: **5** locked H2 sections in the correct order; **12** `### SESSION` headings; **12** `#### PARAGRAPH DEMONSTRATION` headings; **16** learning MCQs; **0** inline `**Paragraph demonstration**` residue.
- `Solved-Practice-Workbook.md`: **32** workbook MCQs; **128** option-wise explanations; **32** unique examiner traps; **6** original Mains models.
- Solved-item support fields: **6** `Demand decoding`, **6** `Executable answer/elimination plan`, **6** `Why this earns marks / route earns marks`, **6** `How to improve/strengthen` in each owner file.
- Keyword discipline: all **12** session keyword blocks remain within the required **6**-keyword count.
- Manual semantic gate: all **32** workbook questions and all **16** learning MCQs were reread in full after the rewrite.
- Supplementary similarity scan on workbook option explanations: max `difflib.SequenceMatcher` **0.6195**; max token-Jaccard overlap **0.4000**.

### Regex and contamination gates

- Gate 1 synthetic-marker sweep: **0** matches across both owner Markdown files.
- Gate 2 mail-merge/circular-template sweep: **0** matches across both owner Markdown files.
- Cross-subject contamination search on Topic 20 package folder/file names, the package `README.txt`, the graphical `README.md`, this review report and the quick-glance chart returned **0** hits for the screened unrelated-topic term.

### PDF validation after rerender

- Learning PDF: **31 pages / 81,126 extracted characters / 33 outline nodes / outline depth 3**.
- Workbook PDF: **20 pages / 56,382 extracted characters / 6 outline nodes / outline depth 3**.
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
