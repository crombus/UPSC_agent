# 10 Existentialism — Offline Revision and MCQ Package

**Subject:** Philosophy Optional
**Section:** Philosophy Paper I — Western Philosophy
**Status:** Release validation requires a fresh local `validate_package.py --regenerate` PASS.

## Use in order

1. [Revision Guide](REVISION-GUIDE.md)
2. [MCQ Questions](MCQ-QUESTIONS.md)
3. [MCQ Solutions](MCQ-SOLUTIONS.md)
4. [Solved Answer-Writing Workbook and Toolkit](ANSWER-WRITING-TOOLKIT.md)
5. [Coverage Ledger](COVERAGE-LEDGER.md)
6. [Practice Log](PRACTICE-LOG.md)

The package contains **74 coverage-derived MCQs** and fully solves **16 directly owned verified PYQs through 2026**. Topic 10 owns both 2026 questions; the Sartre–Husserl comparison gives Topic 09 only a bounded cross-link. The validator parses proposition-level MCQ and PYQ demand manifests, audits source-cell lineage, checks cue and length rates, regenerates all four PDFs, and verifies text integrity for tracked and untracked files.

Substantive source cells were reconciled, adapted and mapped; repeated apparatus was consolidated. Mechanical checks do not prove semantic completeness, philosophical truth or an examiner score.

Run `python validate_package.py --regenerate` here. A run without `--regenerate`
is deliberately non-release and fails the freshness gate. The report records each
Markdown source SHA-256 and timestamp, the regenerated PDF SHA-256 and timestamp,
and extracted heading parity.

PDFs are globally ignored. Before release staging, confirm the active ignore rule
with `git check-ignore -v pdf/Revision-Guide.pdf` (and the other three PDFs), then
stage the regenerated binaries explicitly with `git add -f pdf/*.pdf`. Do not
change `.gitignore`; force-adding release PDFs is intentional.
