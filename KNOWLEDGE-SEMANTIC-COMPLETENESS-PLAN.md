# Knowledge Semantic-Completeness Review Plan

> **Goal:** No gaps, no missing data, no missing topic, and no missing subject. Every catalogue topic must pass a hostile semantic-completeness review.
>
> Authoritative state: `upsc-ai-kit\manifests\reviews\knowledge-semantic-completeness-status.json`
>
> Human tracker: `KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`

## Non-negotiable execution policy

1. Review exactly one subject at a time.
2. Within that subject, review exactly one topic at a time in tracker order.
3. Do not open the next topic until the current topic is passed or explicitly blocked.
4. Do not open the next subject until every topic in the current subject is passed.
5. Existing audit, export or PDF validation is evidence only; it is never proof of semantic completeness.
6. Repair the canonical knowledge owner before regenerating any dependent learning session, workbook, flowchart or PDF.
7. Preserve unrelated working-tree changes and commit only explicitly requested scopes.

## Completeness model

Every topic must be checked against four independently constructed ledgers:

1. **Literal syllabus ledger** — every noun, qualifier, relationship and directive in the official syllabus.
2. **Implied-prerequisite ledger** — concepts without which the printed syllabus cannot be understood or answered.
3. **Textbook-taxonomy ledger** — standard subtopics, classifications, debates, exceptions and terminology from local OCR-searchable books.
4. **PYQ-demand ledger** — every verified Prelims, Mains, CSAT or Philosophy Optional demand routed to the topic.

The hostile review must then search for what is absent rather than merely confirming what is present.

## Ten mandatory topic checks

| Check | Pass requirement |
|---|---|
| Literal syllabus | Every printed term and relationship is substantively taught |
| Implied prerequisites | No indispensable bridge doctrine or background mechanism is absent |
| Textbook taxonomy | Standard classifications, stages, schools, thinkers and exceptions are represented |
| PYQ demands | Every routed demand can be answered from the canonical owner |
| Hostile absence search | Synonyms and likely missing families were actively searched |
| Canonical owner | Basic/Core file contains all marks-essential material |
| Cross-owner boundaries | Cross-owned material has an explicit owner and usable link |
| Answer architecture | Definition, mechanism, evidence, objections, replies and verdict are executable |
| Factual verification | Changeable claims are current, sourced and correctly qualified |
| Dependent artifacts | Sessions, workbooks, diagrams and exports agree with the repaired owner |

## Topic workflow

```text
Freeze current state
        ↓
Read syllabus and owner
        ↓
Build four ledgers independently
        ↓
Run hostile absence search
        ↓
Record confirmed gaps and ownership conflicts
        ↓
Repair canonical Basic/Core owner
        ↓
Revalidate PYQs, arguments, facts and answer architecture
        ↓
Regenerate dependent artifacts only if required
        ↓
Update JSON state and regenerate tracker
        ↓
Pass topic → unlock next topic
```

## Subject completion gate

A subject passes only when:

- its topic count exactly matches the catalogue;
- every topic has passed all ten checks;
- no unresolved syllabus term, prerequisite, textbook family or PYQ remains;
- no marks-essential material exists only in Advanced;
- all cross-owned material has a named owner;
- factual-risk and gap ledgers contain no unhandled item;
- changed dependent artifacts have been regenerated and validated;
- the subject report lists all reviewed topics, findings and changed files.

## Crash recovery

1. Start Copilot in the repository root.
2. Send:

   `Resume semantic-completeness review from KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`

3. The agent must read the Markdown tracker and machine-readable JSON before taking action.
4. The first non-passed topic in JSON is the only permitted next topic.
5. After every topic status change, run:

   `python tools\generate_semantic_completeness_tracker.py`

6. Never reconstruct progress from conversation memory alone.

## State meanings

| Status | Meaning |
|---|---|
| `pending` | Not yet reviewed under this semantic standard |
| `in_progress` | Four-ledger and hostile review is active |
| `changes_required` | Confirmed gaps exist |
| `repair_in_progress` | Canonical owner is being repaired |
| `revalidation_pending` | Repair complete; gates not yet rerun |
| `passed` | All ten checks passed and findings resolved |
| `blocked` | Verification cannot continue; reason must be recorded |
