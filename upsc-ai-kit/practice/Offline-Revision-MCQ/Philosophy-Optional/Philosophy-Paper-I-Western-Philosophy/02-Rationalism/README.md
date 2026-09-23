# 02 Rationalism — Offline Revision and MCQ Package

**Subject:** Philosophy Optional  
**Section:** Philosophy Paper I — Western Philosophy  
**Status:** Formal-session reconciled; development validation passed; release gate pending staging

Verified directly owned UPSC Philosophy Paper I PYQs are included through **2026**.

## Use in order

1. [Revision Guide](REVISION-GUIDE.md)
2. [MCQ Questions](MCQ-QUESTIONS.md)
3. [MCQ Solutions](MCQ-SOLUTIONS.md)
4. [Solved Answer-Writing Workbook and Toolkit](ANSWER-WRITING-TOOLKIT.md)
5. [Coverage Ledger](COVERAGE-LEDGER.md)
6. [Formal Coverage Audit](FORMAL-COVERAGE-AUDIT.json)
7. [Practice Log](PRACTICE-LOG.md)

`ANSWER-WRITING-TOOLKIT.md` fully solves all 15 directly owned verified PYQs from 2018–2026.
The 2026 Aristotle–Leibniz entelechy comparison is cross-linked to its single primary owner,
Topic 01. PDFs are in [pdf/](pdf/); Markdown remains the editable source of truth.

## Formal-session reconciliation and validation

The completed formal learning session and solved workbook were reconciled block by block against
the canonical Rationalism owner and both verified Western Philosophy PYQ ledgers:

- `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Western-Philosophy\02-Rationalism\Learning-Session.md`
- `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Western-Philosophy\02-Rationalism\Solved-Practice-Workbook.md`

`FORMAL-COVERAGE-AUDIT.json` records every formal block, stable source identity, body-derived
signature, substantive witnesses, classification and destination evidence. The reconciliation
found no unresolved formal block and no genuine in-scope omission requiring new teaching or a
larger MCQ bank. The existing 40-question total remains coverage-derived: Q1–32 preserve the
formal source bank and Q33–40 close the eight independently recorded test gaps.

Run `python validate_package.py --regenerate --mode development` while repairing. This may produce
`DEVELOPMENT_PASS`, which validates current content and generated artifacts but is not a release
claim. A later `python validate_package.py --mode precommit` can produce `RELEASE_PASS` only when
every required current file is in the Git index. Mechanical checks do not prove philosophical
truth or semantic completeness.

**PDF tracking and staging:** all four package PDFs are currently tracked. Before any future
release, inspect applicable ignore rules with `git check-ignore -v pdf/Revision-Guide.pdf`; stage
tracked regenerations normally, and use `git add -f pdf/*.pdf` only if an ignore rule applies when
a commit is actually requested.
