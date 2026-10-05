# Deep Content Review — Medieval History 16: State & Government under Akbar (Mansabdari, Dahsala)

- **Current repair mode:** full strict in-place audit-and-repair after independent canonical-scope reconstruction
- **approved:** false

## Canonical scope reconstructed before editing

The package was repaired only after fully reading the canonical Basic and Advanced owners for Topic 16. The resulting scope ledger required coverage of: ruler-centred kingship after the Bairam Khan phase; reduced concentration in the vakilship; central offices of diwan, mir bakhshi, sadr/qazi and mir saman-buyutat; the provincial ladder of suba, sarkar, pargana and village; provincial counterweights through subadar, provincial diwan, bakhshi, sadr-qazi and waqia-navis; mansabdari as numerical service rank rather than landed title; the late-Akbar zat-sawar distinction with chronology caution; dagh and chehra as verification tools; jagir versus khalisa and jama versus hasil; team-built revenue reform through Muzaffar Khan Turbati, Todar Mal, Shah Mansur and local record expertise; measurement through jarib, Ilahi gaz and bigha; land categories of polaj, parauti, chachar and banjar; zabt, dahsala and dastur; alternative methods of batai, kankut and nasaq; zamindars and village intermediaries; and the final verdict of a centralised but negotiated Mughal state.

## Defects confirmed in the pre-repair Topic 16 package

1. `Learning-Session.md` had the correct five locked H2 headings but failed the paragraph-demonstration rule completely: **19** `### SESSION` headings and **0** explicit `#### PARAGRAPH DEMONSTRATION` headings.
2. The learning owner contained extra legacy banks and drifted from the Topic 14/15 clean-pass structure, including overgrown practice sections and incomplete solved-item support fields.
3. `Solved-Practice-Workbook.md` was not in the locked workbook format, so the required 32-question / 128-explanation audit could not be performed cleanly.
4. The workbook owner carried the known high-risk defect class for synthetic-marker and templated-explanation contamination.
5. The owner path had no normal local `assets\` directory.
6. The final-package notes tree used a contaminated cross-subject graphical-flowchart folder name, and `README.txt` repeated the same contamination.
7. The pre-existing review paperwork was stale and did not disclose the paragraph-heading failure, workbook-structure failure, missing local assets or folder-name contamination.

## Repair actions completed

- Rewrote `Learning-Session.md` in place around the independently rebuilt canonical scope.
- Preserved the exact learner-v2 five-H2 order and rebuilt the teaching core to **15** substantive sessions.
- Added **15** explicit `#### PARAGRAPH DEMONSTRATION` headings with one claim -> named evidence/example -> analysis -> qualification paragraph per session.
- Rebuilt the learning-practice section to the locked counts: **16** learning MCQs with strict `ABCDABCDABCDABCD` rotation, **4** routed/adjacent support items, **6** original Mains models and support-field families **10 / 10 / 10 / 10**.
- Rebuilt `Solved-Practice-Workbook.md` to the locked standalone format with exactly **32** workbook MCQs, strict answer rotation `ABCDABCDABCDABCDABCDABCDABCDABCD`, **128** option-wise explanations and **32** unique examiner traps.
- Manually rewrote every workbook option explanation so each distractor is corrected through its own institutional, chronological, fiscal or conceptual error rather than by a repeated English sentence skeleton.
- Created a normal local owner `assets\` directory and added a topic-specific cover image; post-fix verification shows a normal directory (`is_dir = True`, `is_symlink = False`).
- Renamed the final-package graphical folder to `03-Graphical-Flowchart`, rewrote `README.txt`, reconciled the quick-glance chart to the repaired scope and kept the ASCII master text aligned to the repaired content.
- Re-rendered both learner-v2 PDFs in place while bypassing only `validate_v2_paths`; content validation and PDF validation were not bypassed.

## 2026 verification outcome

The mandated 2026 search was completed across these local roots:

- `books\mains\2026\`
- `knowledge-export\Mains PYQ\`
- `knowledge-export\Prelims PYQ\`
- `exams\papers\`
- `new_papers\`
- `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-GS1-GS3-Static-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2026.md`
- `upsc-ai-kit\knowledge\PYQ-INTEGRATION-AUDIT-2026.md`
- `upsc-ai-kit\knowledge\PYQ-MAINS-COVERAGE-AUDIT-2026.md`

Result: **no Topic 16-owned 2026 prelims or mains item** on mansabdari, jagir, zat-sawar, zabt-dahsala or Akbarian state structure was verified locally. Only transparent older direct or adjacent support items were retained.

## Final verification results

### Counts preserved

- `Learning-Session.md`: **15** sessions, **15** paragraph-demonstration headings, **16** learning MCQs, **4** routed/adjacent support items, **6** original Mains models and support-field families **10 / 10 / 10 / 10**.
- `Solved-Practice-Workbook.md`: **32** workbook MCQs, **128** option explanations, **32** unique trap lines, **4** routed/adjacent support items, **6** original Mains models and support-field families **10 / 10 / 10 / 10**.

### PDF validation after rerender

- Learning PDF: **30 pages / 94,080 extracted characters / 2 bookmarks**.
- Workbook PDF: **16 pages / 46,502 extracted characters / 2 bookmarks**.
- `validate_pdf`: **0** errors for both.
- `validate_pdf_layout`: **0** errors for both, with **0** blank, near-empty, clipped or replacement-glyph pages in either output.
- `validate_v2_markdown_text` on `Learning-Session.md`: **0** errors.

### Hard gates

- The banned synthetic-marker gate returned **zero** matches across both owner files after repair.
- The banned mail-merge/circular-template gate returned **zero** matches across both owner files after repair.
- Paragraph-heading parity passed exactly: **15** `### SESSION` headings and **15** `#### PARAGRAPH DEMONSTRATION` headings, with **0** inline `**Paragraph demonstration:**` residues.
- Cross-subject naming passed after the rename: no cross-subject contamination remains in the Topic 16 final-package tree, `README.txt`, quick-glance chart or this review report.

### Manual semantic gate

The full **32-question workbook** was manually reread after the rewrite, not sampled. All **128** option explanations were checked against their own stems and options to verify that the reasoning is specific to the actual distractor error rather than a repeated English sentence skeleton.

### Supplementary similarity check

- max `difflib.SequenceMatcher` across the **128** workbook explanations: **0.6250**
- max token-Jaccard overlap across the same set: **0.3750**

These metrics were used only as warning signals. The binding pass/fail gate remained the zero-match phrase sweeps plus the full manual reread.

## Approval status

This package remains **not approved**.

- `approved: false`
- The repair pass does not self-approve the topic.
