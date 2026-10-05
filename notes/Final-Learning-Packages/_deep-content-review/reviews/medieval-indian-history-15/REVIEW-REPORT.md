# Deep Content Review — Medieval History 15: Akbar: Consolidation & Expansion of the Empire

- **Current repair mode:** full strict in-place audit-and-repair after independent canonical-scope reconstruction
- **approved:** false

## Canonical scope reconstructed before editing

The package was repaired only after fully reading the canonical Basic and Advanced owners for Topic 15. The resulting scope ledger required coverage of: Kalanaur accession and the 1556 crisis; Hemu and Panipat II; Bairam Khan's regency and its end; household faction and the Adham Khan / Atka Khan episode; Uzbek and old-noble challenge through 1567; Malwa and Garh-Katanga as expansion with coercive cost; Rajput policy as alliance, honour, office and service; Chittor 1568, Ranthambhor 1569 and the Mewar exception through Haldighati; Gujarat 1572-73 as western commercial-strategic conquest; Bihar-Bengal through Daud Khan Karrani, Tukaroi and Rajmahal; Odisha and the wider frontier arc of Kabul, Kashmir, Sindh and Qandahar; the late Deccan opening through Ahmadnagar, Chand Bibi, Berar, Khandesh and Asirgarh; capitals and mobile camp; source criticism through Abul Fazl and Badauni; and the final verdict of a durable but uneven empire.

## Defects confirmed in the pre-repair Topic 15 package

1. `Learning-Session.md` had the correct five locked H2 headings but failed the paragraph-demonstration rule completely: **17** `### SESSION` headings and **0** explicit `#### PARAGRAPH DEMONSTRATION` headings.
2. The learning owner also contained circular filler, degraded answer-guidance lines and generic scaffolding that no longer met the Topic 14 clean-pass standard.
3. `Solved-Practice-Workbook.md` was not in the locked workbook format. It had mixed banks rather than validator-readable `#### Workbook MCQ` blocks, so the required 32-question / 128-explanation audit could not be performed cleanly.
4. The workbook owner also contained banned-pattern risk, including the synthetic-marker family and under-disciplined explanation scaffolding.
5. The owner path had no normal local `assets\` directory.
6. The final-package notes tree carried the cross-subject contamination the contaminated old graphical-flowchart name, and `README.txt` repeated the same contamination.
7. The pre-existing review paperwork was stale and did not disclose the paragraph-heading failure, workbook-structure failure, or folder-name contamination.

## Repair actions completed

- Rewrote `Learning-Session.md` in place around the independently rebuilt canonical scope.
- Preserved the exact learner-v2 five-H2 order and reduced the teaching core to **15** substantive sessions.
- Added **15** explicit `#### PARAGRAPH DEMONSTRATION` headings with one claim -> named evidence/example -> analysis -> qualification paragraph per session.
- Rebuilt the learning-practice section to the locked counts: **16** learning MCQs, **4** routed/adjacent support items, **6** original Mains models and support-field families **10 / 10 / 10 / 10**.
- Rebuilt `Solved-Practice-Workbook.md` to the locked standalone format with exactly **32** workbook MCQs, strict answer rotation `ABCDABCDABCDABCDABCDABCDABCDABCD`, **128** option-wise explanations and **32** unique examiner traps.
- Manually rewrote every workbook option explanation so each distractor is corrected through its own actor/date/place/institution/mechanism error rather than through a mail-merge sentence skeleton.
- Created a normal local owner `assets\` directory and added a topic-specific cover image; post-fix verification shows a normal directory (`is_dir = True`, `is_symlink = False`).
- Renamed the final-package graphical folder to `03-Graphical-Flowchart`, rewrote `README.txt`, rewrote the ASCII master-flow text and reconciled the quick-glance chart to the repaired scope and honest 2026 outcome.
- Re-rendered both learner-v2 PDFs in place while bypassing only `validate_v2_paths`; content validation and PDF validation were not bypassed.

## 2026 verification outcome

The mandated 2026 search was completed across these local roots:

- `books\mains6\`
- `knowledge-export\Mains PYQ\`
- `knowledge-export\Prelims PYQ\`
- `exams\papers\`
- `new_papers\`
- `upsc-ai-kit\knowledge\_PYQ-GS1-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-GS1-GS3-Static-2026.md`
- `upsc-ai-kit\knowledge\_PYQ-ROUTING-PRELIMS-2026.md`
- `upsc-ai-kit\knowledge\PYQ-INTEGRATION-AUDIT-2026.md`
- `upsc-ai-kit\knowledge\PYQ-MAINS-COVERAGE-AUDIT-2026.md`

Result: **no Topic 15-owned 2026 prelims or mains item** on Akbar's consolidation, Rajput policy, Gujarat, Bengal or frontier expansion was verified locally. Only transparent older adjacent or routed support items were retained.

## Final verification results

### Counts preserved

- `Learning-Session.md`: **15** sessions, **15** paragraph-demonstration headings, **16** learning MCQs, **4** routed/adjacent support items, **6** original Mains models and support-field families **10 / 10 / 10 / 10**.
- `Solved-Practice-Workbook.md`: **32** workbook MCQs, **128** option explanations, **32** unique trap lines, **4** routed/adjacent support items, **6** original Mains models and support-field families **10 / 10 / 10 / 10**.

### PDF validation after rerender

- Learning PDF: **31 pages / 97,763 extracted characters / 57 bookmarks**.
- Workbook PDF: **17 pages / 54,252 extracted characters / 15 bookmarks**.
- `validate_pdf`: **0** errors for both.
- `validate_pdf_layout`: **0** errors for both, with **0** blank, near-empty, clipped or replacement-glyph pages in either output.
- `validate_v2_markdown_text` on `Learning-Session.md`: **0** errors.

### Hard gates

- The banned synthetic-marker gate returned **zero** matches across both owner files after repair.
- The banned mail-merge/circular-template gate returned **zero** matches across both owner files after repair.
- Paragraph-heading parity passed exactly: **15** `### SESSION` headings and **15** `#### PARAGRAPH DEMONSTRATION` headings, with **0** inline `**Paragraph demonstration:**` residues.
- Cross-subject naming passed after the rename: no contaminated cross-subject naming remains in the Topic 15 final-package tree, `README.txt` or this review report.

### Manual semantic gate

The full **32-question workbook** was manually reread after the rewrite, not sampled. All **128** option explanations were checked against their own stems and options to verify that the reasoning is specific to the actual distractor error rather than a repeated English sentence skeleton.

### Supplementary similarity check

- max `difflib.SequenceMatcher` across the **128** workbook explanations: **0.7313**
- max token-Jaccard overlap across the same set: **0.5000**

These metrics were used only as warning signals. The binding pass/fail gate remained the zero-match phrase sweeps plus the full manual reread.

## Approval status

This package remains **not approved**.

- `approved: false`
- The repair pass does not self-approve the topic.


