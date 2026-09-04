# Final Learning Packages — Deep Content Review Instructions

## Purpose

Certify that each final package is complete, easy to learn from, fact-safe, syllabus-compliant,
PYQ-ready and capable of producing high-quality UPSC answers. File presence and clean rendering are
necessary but are not evidence of content quality.

## Scope

Review all four artifacts for every topic:

1. `01-Complete-Learning-Session`
2. `02-Solved-Practice-Workbook`
3. `03-Carvaka-Graphical-Flowchart`
4. `04-ASCII-Master-Flowchart`

Use sources in this order:

1. Official syllabus and repository topic catalogue/manifest.
2. Complete Basic/Core Markdown owners and relevant cross-topic owners.
3. Advanced Markdown owners, kept optional and subordinate.
4. Repository PYQ ledgers and local verified PYQ material.
5. Official UPSC pages/question papers for missing PYQs.
6. Reliable primary/current sources for facts that can change.

Markdown is the source of truth and has already undergone repeated review. Do not edit source
Markdown during this review. Record precise repair suggestions in the tracker and issue ledger;
apply them only through a separate repair command.

## Required repair handoff

When a review ends as `changes_suggested`, the reviewer must create a topic-specific repair prompt
under `_deep-content-review\repair-prompts\`. The prompt must:

- identify the exact reviewed generation and require it to remain immutable;
- list every critical/high defect and all required medium/low corrections;
- name the canonical Markdown owners and generated artifacts affected;
- distinguish source corrections from generator/pipeline corrections;
- require a new generation rather than in-place replacement;
- require regeneration of all four artifacts and metadata from the same corrected source ledger;
- include exact acceptance criteria and revalidation commands;
- instruct the generator to mark the new generation `revalidation_pending`;
- prohibit carrying forward the old review score or approval state.

The reviewer may make safe shared-pipeline fixes that prevent recurrence, but topic content repairs
must be applied through the new generation so review history remains auditable.

## Hard gates

A topic cannot pass when any of these remains unresolved:

- a material syllabus/Core omission;
- a factual, legal, constitutional, chronological, geographical or doctrinal error;
- a fabricated or misattributed PYQ, year, marks allocation, official key, quotation or statistic;
- Basic understanding depends on material placed only in Optional Advanced;
- a model answer fails the directive or cannot support a credible UPSC answer;
- the four artifacts contradict each other on a material point;
- graphical or ASCII flow omits a major examinable mechanism, distinction, limit or PYQ route;
- current-affairs material lacks source/date/status discipline or is presented as timeless static fact.

## Artifact 1 — Complete Learning Session

Review for:

- explicit learning goals and syllabus boundary;
- an easy beginning that assumes only basic prior knowledge;
- visual-first explanation followed by plain-language reasoning and examples;
- complete Core coverage in a natural learning sequence;
- precise definitions, terminology and `must remember` lines;
- origin and timeline where they are genuinely examinable;
- claim → named evidence/example → analysis → qualification;
- answer-grabbing opening, transitions, analytical lines and qualified conclusion;
- UPSC traps, close distinctions, exceptions and common misconceptions;
- India-centric and topic-specific examples;
- verified current-affairs linkage where it improves the static topic;
- an Optional Advanced block that adds depth without becoming necessary for a core answer;
- complete consolidated register notes at the end without merely repeating the introduction.

## Artifact 2 — Solved Practice Workbook

Review for:

- every relevant verified PYQ available in the repository or found through official online search;
- exact or explicitly qualified PYQ wording, year, paper, marks and word limit;
- directive and demand decoding before the model answer;
- best-answer structure appropriate to 10-, 15- and 20-mark demands;
- model answers using claim → named evidence → analysis → qualification;
- counterarguments, limits and a reasoned conclusion where the directive requires them;
- `Why this earns marks` and concrete `How to improve this answer` guidance;
- original questions that test future-question readiness, not only known PYQs;
- hard MCQs covering the complete topic, nearby concepts, exceptions, chronology, matching,
  statements and close-option traps;
- independent verification of every MCQ statement and strict A → B → C → D key rotation.

## Artifact 3 — Cārvāka-Style Graphical Flowchart

Review for:

- one continuous end-to-end core learning rail;
- full syllabus/Core sequence before optional enrichment;
- definitions, mechanisms, chronology, evidence, comparisons, consequences and limitations;
- visible UPSC traps, PYQ-tested distinctions and answer-grabbing lines;
- bespoke stage grammar rather than repeated generic cards;
- readable labels and useful density at poster and tiled-print scales;
- subordinate Advanced content that never repairs a missing Core stage;
- same-master identity, correct overlap and factual agreement with the learning session.

## Artifact 4 — ASCII Master Flowchart

Review for:

- complete top-to-bottom logical continuity;
- exact terminology, dates, numbers, articles, amendments, cases, thinkers and evidence;
- complete mechanisms, comparisons, objections/replies, exceptions and consequences;
- examiner traps, PYQ anchors, answer spine and qualified conclusion;
- readable branches and panels without generic scaffolding or vague compression;
- exact factual agreement with the graphical flowchart, session and workbook.

## Review result

Use one of these states:

- `pending`
- `in_review`
- `changes_suggested`
- `revalidation_pending`
- `passed`
- `blocked`

Approval remains separate. A review pass does not set the package to approved.
