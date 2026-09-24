# 01 Cārvāka — Offline Revision and MCQ Package

**Subject:** Philosophy Optional

**Section:** Philosophy Paper I — Indian Philosophy

**Status:** `DEVELOPMENT_PASS` is the target; release staging is intentionally deferred.

## Use in order

1. [Revision Guide](REVISION-GUIDE.md)
2. [MCQ Questions](MCQ-QUESTIONS.md)
3. [MCQ Solutions](MCQ-SOLUTIONS.md)
4. [Answer-Writing Toolkit](ANSWER-WRITING-TOOLKIT.md)
5. [Coverage Ledger](COVERAGE-LEDGER.md)
6. [Practice Log](PRACTICE-LOG.md)
7. [Formal Authored Review](FORMAL-COVERAGE-REVIEW.json)
8. [Formal Derived Audit](FORMAL-COVERAGE-AUDIT.json)
9. [MCQ Audit](MCQ-AUDIT.json)
10. [PYQ Audit](PYQ-DEMAND-AUDIT.json)

The package preserves all formal teaching, visuals, practice, advanced depth and register
notes; contains **32 coverage-derived MCQs** with independently randomized correct positions;
fully solves **9 directly owned verified PYQs through 2026**; retains **1 supporting routed
Nyāya-owned question** with honest ownership; and includes **6 original solved Mains models**,
two each at 10, 15 and 20 marks.

Formal coverage contains **697 raw proposition mappings** across the 436 source-block
decisions and **522 unique normalized semantic propositions**. The remaining **175 duplicate
occurrences** are acknowledged repetitions, chiefly where the completed session and workbook
carry the same practice material; repeated source mappings share one unique proposition ID
and do not inflate substantive coverage.

The completed `learning_package_final` session and workbook are formal authority. The canonical
owner controls doctrine, boundaries and contested attributions. The verified ledgers control
PYQ wording and ownership. Cārvāka has no direct 2026 question.

Run `python -B validate_package.py --regenerate` only after Markdown stabilizes. Then run
`python -B validate_package.py` for the final development gate. `--mode release` is
non-mutating and succeeds only when every required current artifact is staged with
Git-normalized identity.
