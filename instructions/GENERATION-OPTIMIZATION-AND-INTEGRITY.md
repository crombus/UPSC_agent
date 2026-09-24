# Generation Optimization and Integrity Instructions

## Purpose

Apply this policy to every new UPSC generation workflow.

## Optimization monitoring

Proactively monitor each generation batch for safe ways to improve:

- source discovery and preflight efficiency;
- independent read-only research and bounded parallelism;
- reuse of verified validators and generation tooling;
- defect detection before expensive generation or release work;
- controller review, staging, indexing and release sequencing;
- token, tool-call and elapsed-time efficiency.

Report worthwhile optimization opportunities to the user. Distinguish between:

1. **safe operational optimization**, which changes scheduling, tooling or validation
   efficiency without changing the required result; and
2. **requirement-affecting change**, which could alter coverage, depth, pedagogy,
   practice, evidence, validation or delivery and therefore requires explicit user
   approval before implementation.

## Non-compromise lock

Optimization must never skip, compress, merge, weaken or silently reinterpret any
approved rule. It must not reduce:

- syllabus, canonical, advanced, book, PYQ or current-affairs coverage;
- lesson-level depth or learner-first teaching quality;
- roadmap fidelity or required practice;
- semantic review of MCQ keys, distractors and explanations;
- independent validation, integrity hard stops or release gates;
- required files, indexes, commits, pushes or delivery order.

If an optimization creates uncertainty about equivalence with the approved workflow,
do not apply it. Keep the established workflow, report the proposed change and seek
approval when necessary.

## Integrity response

- Quarantine a topic when the problem is confined to that topic.
- Stop all affected generation lanes when a systemic problem threatens more than one
  topic or any shared authority.
- Resume only after correcting the cause and repeating the required validation.
- Prefer a slower verified result over a faster result that weakens any governing
  requirement.
