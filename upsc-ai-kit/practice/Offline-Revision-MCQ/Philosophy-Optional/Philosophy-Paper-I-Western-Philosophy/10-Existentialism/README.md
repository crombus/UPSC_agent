# 10 Existentialism — Offline Revision and MCQ Package

**Subject:** Philosophy Optional
**Section:** Philosophy Paper I — Western Philosophy
**Status:** `DEVELOPMENT_PASS`; release staging is intentionally deferred to the serialized parent workflow.

## Use in order

1. [Revision Guide](REVISION-GUIDE.md)
2. [MCQ Questions](MCQ-QUESTIONS.md)
3. [MCQ Solutions](MCQ-SOLUTIONS.md)
4. [Solved Answer-Writing Workbook and Toolkit](ANSWER-WRITING-TOOLKIT.md)
5. [Coverage Ledger](COVERAGE-LEDGER.md)
6. [Formal Coverage Review](FORMAL-COVERAGE-REVIEW.json)
7. [Formal Coverage Audit](FORMAL-COVERAGE-AUDIT.json)
8. [Practice Log](PRACTICE-LOG.md)

The package contains **74 coverage-derived MCQs**, fully solves **16 directly owned verified PYQs through 2026**, and provides **nine original solved Mains models**: the package's three retained transfer models plus all six distinct formal-session exercises. The Revision Guide restores the authoritative **53-panel ASCII master flow** with exact ordered panel and payload parity. Topic 10 owns both 2026 questions; the Sartre–Husserl comparison gives Topic 09 only a bounded cross-link. The validator parses proposition-level MCQ and PYQ demand manifests, audits source-cell lineage, checks formal-block, structural-umbrella, large-leaf and panel correspondence, runs duplicate and production-negative gates, checks cue and length rates, regenerates all four PDFs, and verifies text integrity for tracked and untracked files.

The authoritative formal sources are the completed `Learning-Session.md` and
`Solved-Practice-Workbook.md` under
`C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final`.
The derivative `C:\up\learning_package_final` tree must not be substituted.
Canonical ownership and exact verified PYQs remain under `C:\up\upsc-ai-kit\knowledge`.

Substantive source cells were reconciled, adapted and mapped; repeated apparatus was consolidated. Mechanical checks do not prove philosophical truth or semantic completeness, and they do not predict an examiner score.

Run `python validate_package.py --refresh-formal-audit --regenerate` once after
learner-visible Markdown stabilizes, then run `python validate_package.py` for the
final development gate. `DEVELOPMENT_PASS` validates content and generated
artifacts without requiring Git-index changes. `RELEASE_PASS` is a separate
precommit gate and is intentionally unavailable until a serialized parent stages
the current files. The report records source and review hashes, regenerated PDF
identity, heading parity and production-negative results.

## PDF tracking and staging

PDFs are globally ignored. Before release staging, confirm the active ignore rule
with `git check-ignore -v pdf/Revision-Guide.pdf` (and the other three PDFs), then
stage the regenerated binaries explicitly with `git add -f pdf/*.pdf`. The PDFs
are currently tracked release artifacts; do not change `.gitignore`.
