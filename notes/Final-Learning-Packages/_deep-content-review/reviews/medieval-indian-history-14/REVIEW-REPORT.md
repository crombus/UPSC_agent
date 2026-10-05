# Deep Content Review — Medieval History 14: Sher Shah Sur & the Sur Empire

- **Current repair mode:** full strict in-place audit-and-repair after independent canonical-scope reconstruction
- **approved:** false

## Canonical scope reconstructed before editing

The repaired package was rebuilt only after fully re-reading the canonical Basic and Advanced owners. The resulting scope ledger contained these mandatory Topic 14 dimensions: Farid/Sher Khan's eastern rise; the bounded Chausa-Kannauj threshold into sovereignty; Bengal-to-Indus extent with unequal control; Afghan kingship and central departments; sarkar-pargana-village administration; revenue measurement, rai and patta-qabuliyat; coinage and customs simplification; roads, sarais, wells and dak; army control, dagh-chehra and forts; justice, policing and the mediated countryside; Raisen/Puran Mal, religion and legitimacy; Sasaram/Purana Qila architecture; Islam Shah, succession crisis and fragmentation; and the qualified Sur-to-Akbar legacy debate.

## Defects confirmed in the pre-repair Topic 14 package

1. `Learning-Session.md` had the correct five H2 headings but had become bloated and structurally unsafe: **24** `### SESSION` headings and **0** explicit `#### PARAGRAPH DEMONSTRATION` headings. That failed the now-locked paragraph-demonstration convention.
2. The pre-repair learning file also carried degraded keyword and recall guidance, including generic session scaffolding and non-examiner-grade phrasing that no longer matched the Topic 9/11/12/13 repaired standard.
3. `Solved-Practice-Workbook.md` was not in the locked workbook format. It had **0** `#### Workbook MCQ` headings, **0** option-wise explanation blocks and **0** examiner-trap lines in the required structure. Instead it held mixed banks totalling **58** questions, which violated the locked 32-question workbook count and made the high-risk explanation audit impossible.
4. The owner path had **no local `assets\` directory**, so the learning Markdown pointed toward assets that were not present locally.
5. The final-package notes folder still carried the cross-subject contamination the contaminated graphical-flowchart folder name, and `README.txt` repeated the same contamination.
6. The pre-existing review paperwork was stale and incomplete; it did not disclose the paragraph-heading failure, workbook count failure or the folder-name contamination.

## Repair actions completed

- Rewrote `Learning-Session.md` in place around the independently rebuilt canonical scope instead of trusting the large existing file.
- Restored the exact learner-v2 five-H2 order and reduced the teaching core to **13** substantive sessions.
- Added **13** explicit `#### PARAGRAPH DEMONSTRATION` headings with one claim -> evidence -> analysis -> qualification paragraph per session.
- Rebuilt the learning-practice section to the locked counts: **16** learning MCQs, **4** adjacent/routed support items, **6** original Mains models and **10 / 10 / 10 / 10** support-field families.
- Rebuilt `Solved-Practice-Workbook.md` to the locked standalone format with exactly **32** workbook MCQs, strict `ABCDABCDABCDABCDABCDABCDABCDABCD` rotation, **128** option-wise explanations and **32** unique examiner traps.
- Manually rewrote every workbook option explanation so each distractor is corrected through its own actor/date/place/institution/mechanism error rather than through a recycled mail-merge sentence frame.
- Created a normal local owner `assets\` directory and added a topic-specific cover image.
- Renamed the final-package graphical folder to `03-Graphical-Flowchart`, rewrote `README.txt`, rewrote the ASCII master-flow text and regenerated the standalone ASCII PDF.
- Re-rendered both learner-v2 PDFs in place while bypassing only `validate_v2_paths`; content validation and PDF validation were not bypassed.

## 2026 verification outcome

The mandated 2026 search was completed across these local roots:

- `books\mains\2026\`
- `knowledge-export\Mains PYQ\`
- `exams\papers\`
- `new_papers\`
- `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-GS1-GS3-Static-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2026.md`
- `upsc-ai-kit\knowledge\PYQ-INTEGRATION-AUDIT-2026.md`
- `upsc-ai-kit\knowledge\PYQ-MAINS-COVERAGE-AUDIT-2026.md`

Result: **no Topic 14-owned 2026 prelims or mains item** on Sher Shah, the Sur empire, revenue, roads, currency, forts or army control was verified locally. No duplicate 2026 claim from another topic was imported.

## Final verification results

### Counts preserved

- `Learning-Session.md`: **13** sessions, **13** paragraph-demonstration headings, **16** learning MCQs, **4** routed/adjacent support items, **6** original Mains models, support-field families **10 / 10 / 10 / 10**.
- `Solved-Practice-Workbook.md`: **32** workbook MCQs, **128** option explanations, **32** unique trap lines, **4** routed/adjacent support items, **6** original Mains models, support-field families **10 / 10 / 10 / 10**.

### PDF validation after rerender

- Learning PDF: **32 pages / 94,078 extracted characters / 33 bookmarks**.
- Workbook PDF: **20 pages / 57,159 extracted characters / 7 bookmarks**.
- `validate_pdf_layout`: **0** errors for both, with **0** blank, near-empty, clipped or replacement-glyph pages in either PDF.
- `validate_v2_markdown_text` on `Learning-Session.md`: **0** errors.

### Hard gates

- The banned synthetic-marker gate returned **zero** matches across both owner files after repair.
- The banned mail-merge/circular-template gate returned **zero** matches across both owner files after repair.
- Paragraph-heading parity passed exactly: **13** `### SESSION` headings and **13** `#### PARAGRAPH DEMONSTRATION` headings, with **0** inline `**Paragraph demonstration:**` residues.
- Cross-subject naming passed after the rename: no contaminated folder name remains in the Topic 14 final-package tree, `README.txt` or this review report.

### Manual semantic gate

The full **32-question workbook** was manually reread after the rewrite, not sampled. All **128** option explanations were checked against their own stems and options to verify that the reasoning is specific to the actual distractor error rather than a repeated English sentence skeleton.

### Supplementary similarity check

- max `difflib.SequenceMatcher` across the **128** workbook explanations: **0.6789**
- max token-Jaccard overlap across the same set: **0.4400**

These metrics were used only as a secondary warning signal. The binding pass/fail gate remained the zero-match phrase sweeps plus the full manual reread.

## Topic-integrity confirmation

- Topic 15 `Learning-Session.md` SHA-256 baseline: `EE5037A5D8E315D79008A056082848FC1524072BB824147DA54426F7C57583F3`
- Topic 15 `Solved-Practice-Workbook.md` SHA-256 baseline: `34BAEB9736D378D8944324C4A330C016CA359D59452E14BFFFEED093D3740A1D`
- Final post-pass verification matched those baselines exactly.

## Approval status

This package remains **not approved**.

- `approved: false`
- The repair pass does not self-approve the topic.


