# Final Learning Packages — Deep Content Review Plan

## Recommended operating model

Review one topic completely across all four artifacts before moving to the next topic. Process
topics in manifest order, in bounded batches of five, and stop a batch immediately when a critical
factual or ownership ambiguity requires a decision. This prevents four disconnected audit passes
from missing contradictions between artifacts.

## Phase 0 — Freeze the review baseline

1. Capture the current master-tracker timestamp, topic count, source record ID and generation.
2. Record hashes for the four final artifacts and their source Markdown/flowchart artifacts.
3. Mark a topic `blocked` if its tracker identity is ambiguous or changes during review.
4. Keep package approval pending throughout review.

## Phase 1 — Build the topic coverage ledger

For each topic:

1. Resolve the exact official syllabus clause.
2. Enumerate Basic/Core, cross-topic, Advanced and PYQ owners.
3. Convert the syllabus and owners into atomic review requirements.
4. Classify each requirement as `Core`, `Optional Advanced`, `PYQ`, `Current` or `Cross-owned`.
5. Identify facts requiring live verification because they are current, disputed or status-sensitive.

**Output:** a topic coverage ledger against which all four artifacts are checked.

## Phase 2 — Review the complete learning session

Read the PDF as a learner, not merely as extracted text:

1. Goals and boundary.
2. Easy conceptual gateway.
3. Complete Core teaching in learning order.
4. Must-remember lines and terminology.
5. Evidence-based answer material.
6. Answer-grabbing openings, transitions and conclusions.
7. UPSC traps, timelines/origins and comparisons.
8. Verified current-affairs linkage.
9. Optional Advanced depth after the complete Core.
10. Final register notes.

Attempt at least three answer skeletons using only the session:

- one direct/definition or descriptive demand;
- one analytical/causal or comparative demand;
- one critical/evaluative unfamiliar demand.

## Phase 3 — Review the solved workbook

1. Reconcile repository PYQs with official UPSC question papers.
2. Search official online sources when the repository lacks a relevant PYQ.
3. Verify year, wording, paper, marks and word limit.
4. Score every model answer using the answer-worthiness rubric.
5. Check evidence density appropriate to 10/15/20 marks.
6. Check directive fidelity, balance, qualification and conclusion.
7. Require `Why this earns marks` and better-answer guidance.
8. Map MCQs to every major Core subtopic and close-option neighbourhood.
9. Verify every statement and strict A → B → C → D rotation.

## Phase 4 — Review both master flowcharts

### Graphical

Check stage order, Core completeness, visual hierarchy, evidence, traps, PYQ distinctions,
answer lines, Advanced subordination, readability, poster integrity and tiled-print usability.

### ASCII

Check logical continuity, exact-data retention, mechanisms, comparisons, limits, evidence,
PYQ anchors, answer spine and readability.

### Reconciliation

Create a four-way contradiction table:

| Requirement/fact | Session | Workbook | Graphical | ASCII | Verdict |
|---|---|---|---|---|---|

Any material disagreement is a hard failure until resolved.

## Phase 5 — Factual and current-data verification

Prioritise verification of:

- constitutional articles, amendments, schedules, judgments and institutional powers;
- historical dates, texts, inscriptions, sites, scholars and interpretations;
- geographical processes, locations, classifications, maps and quantitative claims;
- philosophical terminology, thinker attribution, arguments, objections and translations;
- reports, schemes, statistics, office-holders and current legal/policy status;
- PYQ wording and official answer keys where an official key exists.

Record source URL/path, publication date, access date, claim status and any qualification. Prefer
primary sources. Do not upgrade an inference into a fact.

## Phase 6 — Suggest source Markdown changes

Do not edit knowledge owners during review. For each required change, record:

- exact owner file and heading;
- missing/incorrect text;
- why it affects the paper outcome;
- verified evidence;
- proposed Core or Optional-Advanced placement;
- all generated artifacts that must be regenerated;
- severity and dependency.

Group repeated issues into one systemic repair proposal instead of duplicating micro-fixes.

## Phase 7 — Finalise and revalidate

A topic passes only when:

- all atomic Core requirements are covered;
- all hard gates pass;
- session, workbook and both flows agree;
- model answers are marks-worthy;
- PYQs and MCQs are verified;
- suggested Markdown repairs are either completed and regenerated or explicitly accepted as
  bounded non-critical gaps;
- rendering validation remains clean after any regeneration.

## Scoring framework

| Area | Weight |
|---|---:|
| Complete learning session | 40 |
| Solved workbook | 30 |
| Graphical flowchart | 15 |
| ASCII flowchart | 15 |

Recommended thresholds:

- `90–100`: pass candidate, subject to all hard gates;
- `80–89`: changes suggested;
- `<80`: substantial strengthening required.

A high score never overrides a failed hard gate.

## Efficiency controls

- Review in batches of five topics, but close each topic end-to-end.
- Use tracker-generated ready queues instead of browsing folders manually.
- Reuse one atomic syllabus ledger across all four artifact checks.
- Verify repeated facts once in a shared evidence ledger and reference them by ID.
- Record systemic defects separately from topic-local defects.
- Run automated checks for extraction, headings, indexes, answer-key rotation and artifact hashes;
  reserve human review for teaching quality, factual nuance, answer quality and visual usefulness.
- Publish a batch report after every five topics and a subject report after each section.

## Suggested first execution order

1. One representative topic from each subject to calibrate scoring.
2. Resolve rubric disagreements and freeze examples of Pass / Changes Suggested / Fail.
3. Complete the smallest unfinished section first.
4. Continue subject-wise in master-tracker order.
5. Run a final cross-subject consistency and factual-risk sweep.
