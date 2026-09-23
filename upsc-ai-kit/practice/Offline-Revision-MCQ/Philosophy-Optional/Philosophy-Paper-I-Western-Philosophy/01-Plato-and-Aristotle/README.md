# 01 Plato and Aristotle — Offline Revision and MCQ Pilot

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

`ANSWER-WRITING-TOOLKIT.md` is the topic's solved Mains/PYQ workbook: all 14 routed PYQs from
2018–2026 include complete independent model answers.

PDFs are in [pdf/](pdf/). Canonical depth sources and graphical assets are linked from the Revision Guide. Markdown is the editable source of truth.

## Formal-session reconciliation and validation

The authoritative completed session and workbook were reconciled block by block under locked rule
10:

- `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Western-Philosophy\01-Plato-and-Aristotle\Learning-Session.md`
- `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final\Philosophy-Optional\Philosophy-Paper-I-—-Western-Philosophy\01-Plato-and-Aristotle\Solved-Practice-Workbook.md`

The machine-readable audit records every formal block, its classification and exact package
destinations. Learner-v2 g7 is derivative/reference material only and does not define formal
coverage. No substantive in-scope omission remained after comparison with the canonical owner; the
existing 40-question coverage-sized bank and all 14 owned PYQs were therefore retained rather than
mechanically expanded.

Run `python validate_package.py --regenerate --mode development` while repairing. This can produce
`DEVELOPMENT_PASS`, which validates content and generated artifacts but is explicitly not a release
claim. After the parent stages every intended file, run `python validate_package.py --mode
precommit`; only `RELEASE_PASS` verifies that all required current files, including the audit,
validator, validation record and PDFs, are in the Git index. Mechanical checks do not prove
philosophical truth or semantic completeness.

**PDF tracking and staging:** these four package PDFs are currently tracked. Before release, inspect
any applicable ignore rule with `git check-ignore -v pdf/Revision-Guide.pdf`; stage tracked
regenerations normally, and use `git add -f pdf/*.pdf` only if an ignore rule applies to a
replacement or newly added PDF when a commit is actually requested.
