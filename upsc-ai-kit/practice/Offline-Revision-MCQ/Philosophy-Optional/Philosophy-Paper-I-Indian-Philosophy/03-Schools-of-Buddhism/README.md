# Schools of Buddhism — Offline Revision and MCQ Package

This self-contained package reconciles the complete formal learning session and workbook against the canonical Schools of Buddhism owner and verified 2018–2026 PYQ ledgers.

## Study order

1. `REVISION-GUIDE.md`
2. `MCQ-QUESTIONS.md`
3. `MCQ-SOLUTIONS.md`
4. `ANSWER-WRITING-TOOLKIT.md`
5. Record attempts in `PRACTICE-LOG.md`

`source-snapshots/` contains exact immutable copies of the formal session, formal workbook, canonical owner, and both PYQ ledgers. Normal study, build, and validation use only these package-local files, so copied-package validation is self-contained. `FORMAL-SOURCE-MIRROR.md` preserves both formal snapshots in full with stable anchors; `CANONICAL-SOURCE-MIRROR.md` integrity-preserves the canonical owner.

`FORMAL-COVERAGE-REVIEW.json` is the authored/frozen evidence ledger. It separately reports genuine proposition mappings, unique normalized propositions, excluded structural coordinates by category/type, and deterministic meaningful-proposition samples. `FORMAL-COVERAGE-AUDIT.json`, `MCQ-AUDIT.json`, `PYQ-DEMAND-AUDIT.json`, and `VALIDATION.json` are machine-auditable controls.

## Refreshing frozen authorities

Normal development and release validation never require the original `C:\Users\pulkitkundra` or `C:\up\upsc-ai-kit\knowledge` authority paths. To deliberately refresh the local snapshots from those configured authorities, run `python -B build_package.py --refresh-sources`. Refresh is refused unless every original file still matches its frozen SHA-256; updating authority hashes is a separate reviewed change.
