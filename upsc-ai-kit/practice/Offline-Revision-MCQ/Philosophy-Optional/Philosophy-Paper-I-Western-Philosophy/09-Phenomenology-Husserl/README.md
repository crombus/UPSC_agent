# 09 Phenomenology (Husserl) — Offline Revision and MCQ Package

**Subject:** Philosophy Optional
**Section:** Philosophy Paper I — Western Philosophy
**Status:** Validated locally after `validate_package.py --regenerate` passes

## Use in order

1. [Revision Guide](REVISION-GUIDE.md)
2. [MCQ Questions](MCQ-QUESTIONS.md)
3. [MCQ Solutions](MCQ-SOLUTIONS.md)
4. [Solved Answer-Writing Workbook and Toolkit](ANSWER-WRITING-TOOLKIT.md)
5. [Coverage Ledger](COVERAGE-LEDGER.md)
6. [Practice Log](PRACTICE-LOG.md)

The toolkit solves all **7 directly owned verified PYQs from 2019–2025** and records the 2026 Sartre comparison as a bounded Topic 10 cross-link. The bank contains **53 matrix-mapped MCQs**. Mechanical lineage validation records **43 adapted inferences, 13 unmapped g4 candidates and 10 new matrix-closing operations**. These figures verify declared links and witnesses, not semantic completeness. PDFs are in [pdf/](pdf/); Markdown remains canonical.

Substantive source cells were reconciled, adapted and mapped; repeated apparatus was consolidated. The package does not claim verbatim or passage-by-passage preservation of every canonical source cell.

The validator parses [MCQ-AUDIT.json](MCQ-AUDIT.json) to align every explicit stem, option, keyed truth value, false proposition and correction. Correct rationales must contain their declared item-specific doctrinal anchors; distractor explanations must quote the exact false proposition and correction, and their rationales must contain declared correction anchors. Generic negative controls, repeated normalized bodies and near-duplicate rationale bodies are rejected. It also parses [PYQ-DEMAND-AUDIT.json](PYQ-DEMAND-AUDIT.json) and checks that every declared demand-limb anchor occurs in the matching timed answer. These are strong consistency and coverage gates, but they cannot independently prove philosophical truth, interpretive completeness or an examiner score.

Run `python validate_package.py --regenerate` from this directory to regenerate all four PDFs and execute every gate recorded in `VALIDATION.json`.
