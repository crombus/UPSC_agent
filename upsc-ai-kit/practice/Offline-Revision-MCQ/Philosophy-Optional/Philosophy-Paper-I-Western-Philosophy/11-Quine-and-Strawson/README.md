# 11 Quine and Strawson — Offline Revision and MCQ Package

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

The package contains **61 coverage-derived MCQs** and fully solves **10 directly owned verified PYQs through 2026**, plus original solved 10-, 15- and 20-mark practice. It keeps Quinean holism/naturalism distinct from Strawsonian descriptive metaphysics and reconciles ownership against Topics 06–10.

The canonical owner file is substantially retained where already final; source cells were reconciled, adapted and mapped, repeated apparatus was consolidated, and the validator records real hashes, witnesses and overlap measures. Mechanical validation does not prove semantic completeness, philosophical truth or an examiner score.

Run `python validate_package.py --regenerate` here. A run without `--regenerate` is deliberately non-release and fails the freshness gate.

PDFs are globally ignored. Before release staging, confirm the active ignore rule with `git check-ignore -v pdf/Revision-Guide.pdf` and the other three files, then stage regenerated binaries explicitly with `git add -f pdf/*.pdf`. Do not change `.gitignore`; force-adding release PDFs is intentional.
