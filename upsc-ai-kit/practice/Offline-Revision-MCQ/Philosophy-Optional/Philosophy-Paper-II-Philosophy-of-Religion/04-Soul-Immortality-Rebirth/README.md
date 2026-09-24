# 04 Soul, Immortality and Rebirth — Offline Revision and MCQ Package

**Subject:** Philosophy Optional
**Section:** Philosophy Paper II — Philosophy of Religion
**Authority mode:** `canonical_without_formal_session`
**Status:** Development validation is recorded in `VALIDATION.json`; release readiness is established by the non-mutating staged precommit gate.

## Use in order

1. [Source Provenance](SOURCE-PROVENANCE.json)
2. [Revision Guide](REVISION-GUIDE.md)
3. [MCQ Questions](MCQ-QUESTIONS.md)
4. [MCQ Solutions](MCQ-SOLUTIONS.md)
5. [Solved Answer-Writing Toolkit](ANSWER-WRITING-TOOLKIT.md)
6. [Coverage Ledger](COVERAGE-LEDGER.md)
7. [Canonical Coverage Review — 41 authoritative rows](CANONICAL-COVERAGE-REVIEW.json)
8. [Formal-Named Compatibility Audit](FORMAL-COVERAGE-AUDIT.json)
9. [Practice Log](PRACTICE-LOG.md)

This package contains 54 coverage-derived MCQs, all 17 exact verified primary-owned PYQs
from 2018-2025, the verified zero-owner result for 2026, and six original timed Mains models.
Every timed answer uses the locked 150-200 / 250-300 / 340-400 word bands with declared counts
computed from the rendered answer text.

`FORMAL-COVERAGE-AUDIT.json` exists only for repository compatibility. Its
`authority_mode` is unmistakably `canonical_without_formal_session`; it is generated from the
canonical review and must never be described as formal-session reconciliation.

The inbound obligation `T11-ROUTE-P2-SOUL` is closed across lesson, revision, MCQs and answer writing.
The Strawsonian comparison is bounded to public identification and re-identification conditions
for survival claims.

Run:

```powershell
$env:PYTHONDONTWRITEBYTECODE='1'
python -B validate_package.py --regenerate --mode development
```

The validator checks current source hashes, 41 authored canonical rows, supplementary-reference provenance,
inbound closure, MCQ randomization/cues/leakage, exact PYQ wording, timed bands, PDFs, temporary
files, production negative controls and package isolation. Mechanical validation does not prove
philosophical truth, examiner marks or formal-session reconciliation.

The release manifest requires `VALIDATION.json`; its embedded deterministic SHA-256 manifest covers every other required artifact and explicitly excludes only its own self-hash to avoid recursion.
