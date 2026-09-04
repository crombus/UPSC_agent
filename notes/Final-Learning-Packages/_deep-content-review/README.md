# Final Learning Packages — Deep Content Review

This folder contains the content-first review system for all final learning packages.

## Start here

1. Read [`REVIEW-INSTRUCTIONS.md`](REVIEW-INSTRUCTIONS.md).
2. Follow [`REVIEW-PLAN.md`](REVIEW-PLAN.md).
3. Update [`REVIEW-TRACKER.json`](REVIEW-TRACKER.json) as the machine source of truth.
4. Regenerate or update [`REVIEW-TRACKER.md`](REVIEW-TRACKER.md) for human navigation.
5. Record verified claims in [`EVIDENCE-LEDGER.md`](EVIDENCE-LEDGER.md).
6. Record defects in [`ISSUE-LEDGER.md`](ISSUE-LEDGER.md).
7. Record proposed source repairs in [`MD-CHANGE-SUGGESTIONS.md`](MD-CHANGE-SUGGESTIONS.md).
8. Use [`ONGOING-EXPORT-GENERATOR-PROMPT.md`](ONGOING-EXPORT-GENERATOR-PROMPT.md) in terminals
   generating new or repaired packages.
9. For reviewed failures, use the exact topic handoff under [`repair-prompts`](repair-prompts).

## Baseline

- Topics: **483**
- Batch size: **5**
- Planned batches: **97**
- New tracker identities enter as `pending`; completed reviews retain their state
- Review approval and package approval are separate.

## Recommended command unit

Review one complete topic at a time:

```text
Review final package: <Subject> — <Section> — <Topic>
```

For bounded execution:

```text
Review next 5 final packages
```

Stop on the first critical factual, syllabus-ownership or artifact-identity ambiguity.
