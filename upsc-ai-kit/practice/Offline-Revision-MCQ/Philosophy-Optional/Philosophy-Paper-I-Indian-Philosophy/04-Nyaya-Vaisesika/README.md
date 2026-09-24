# Nyāya–Vaiśeṣika — Offline Revision and MCQ Package

This isolated package reconciles all fifteen formal sessions, all formal practice, canonical doctrine and every verified primary PYQ through 2026.

The current MCQ bank has **66 questions** governed by **59 explicit test cells**. `TEST-MATRIX.json` is the machine-readable question-to-cell contract. Counts printed inside `FORMAL-SOURCE-MIRROR.md` are immutable historical text and do not define the current package.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. Record attempts in `PRACTICE-LOG.md`

`FORMAL-SOURCE-MIRROR.md` is immutable evidence, including legacy practice metrics or risky phrases. The learner surfaces apply documented canonical overrides. The formal audit records **1645 raw meaningful proposition mappings**, **1311 unique normalized propositions**, **696 excluded structural fragments**, and **334 acknowledged duplicate occurrences**. JSON audits bind source blocks, meaningful propositions, exclusions, the test matrix, MCQs, PYQs and canonical source artifacts.

## Build and validation policy

- Default canonical build: `python build_package.py`
- Default development validation: `python validate_package.py`
- Default release validation: `python validate_package.py --release --check-only`
- Optional PDF generation: `python render_pdfs.py`
- Optional PDF validation: `python validate_package.py --pdf`

Markdown and machine-readable audits are the current deliverables. PDFs and `PDF-MANIFEST.json` are optional derived artifacts and are not required for development or release.
