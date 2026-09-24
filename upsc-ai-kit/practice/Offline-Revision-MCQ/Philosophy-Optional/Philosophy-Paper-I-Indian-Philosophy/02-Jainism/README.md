# Jainism — Offline Revision and MCQ Package

This self-contained package reconciles the complete formal learning session and workbook against the canonical Jainism owner and verified 2018–2026 PYQ ledgers.

Markdown is the canonical package format. Existing PDFs are legacy optional artifacts and are
generated or refreshed only on explicit request with `python build_package.py --with-pdfs` or
`python render_pdfs.py`; default builds and validation do not update or require them.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. Record attempts in `PRACTICE-LOG.md`

`FORMAL-SOURCE-MIRROR.md` preserves the immutable 2018–2025 formal session/workbook snapshot for audit; its legacy nine-primary-plus-one-supporting numbering does not control the reconciled learner sequence.

`FORMAL-COVERAGE-REVIEW.json` is the authored/frozen formal-evidence ledger. `TEST-MATRIX.json`
contains the frozen 94-cell MCQ scope, and `MCQ-BANK.json` is its topic-local authored bank.
`FORMAL-COVERAGE-AUDIT.json`, `MCQ-AUDIT.json`, `PYQ-DEMAND-AUDIT.json`, and `VALIDATION.json`
are machine-auditable controls.
