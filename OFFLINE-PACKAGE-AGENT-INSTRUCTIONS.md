# Offline Package Agent Instructions

## Scope

These are **agent-only execution instructions** for generating, reconciling, reviewing, repairing,
validating, releasing, scheduling, or resuming packages under:

`C:\up\upsc-ai-kit\practice\Offline-Revision-MCQ`

They do not govern interactive Guided Tutor turns, CA analysis, ordinary notes requests, exam
generation, or answer evaluation. Those workflows use their own instructions in `AGENT_MEMORY.md`
and the relevant guide.

## Mandatory source authority

1. Completed formal sessions and solved workbooks:
   `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final`
2. Canonical owners and verified PYQ ledgers:
   `C:\up\upsc-ai-kit\knowledge`
3. Regenerated Learner-v2 or other derivative material is reference-only unless explicitly
   promoted to formal authority.
4. If no completed formal session exists, record `canonical_without_formal_session`; require every
   canonical heading/block, while using reference sessions/workbooks only as supplementary depth.

## Pre-pass compliance gate

Before every development, independent-review, focused-repair, optional PDF, or release pass:

1. Verify the frozen ledger covers the complete syllabus and every canonical/formal obligation.
2. Verify all relevant authenticated PYQs through the latest repository year are included, owned
   honestly, and fully solved.
3. Verify teaching, visuals, comparisons, criticisms, traps, applications, and answer-writing
   transfer are complete.
4. Confirm nothing was skipped, compressed, merged away, weakened, or deferred.
5. Derive MCQ sufficiency from an explicit topic-specific test-cell matrix. Never use a familiar,
   equal, convenient, copied, or template question total as evidence of completeness.
6. Stop the pass immediately if any requirement fails; freeze the defect and repair it before
   progression.

## Optimized execution

1. Run one exhaustive preflight and freeze the defect/coverage ledger.
2. Validate incrementally: source identity, semantic propositions, hierarchy, routes, practice,
   learner-visible artifacts, then release integrity.
3. Report raw proposition mappings separately from unique normalized propositions and acknowledged
   duplicates. Exclude and separately count non-propositional coordinates or labels.
4. Freeze cleared surfaces. Do not repeatedly rediscover scope or reopen unaffected content.
5. Stabilize and validate learner-visible Markdown as the complete canonical package. Do not
   generate, update, stage, or commit PDFs by default. Generate PDFs only when the user explicitly
   requests them, and then regenerate only artifacts affected by a learner-visible source change.
6. After the first complete independent review, use focused re-reviews for changed risk areas.
7. Run one final development gate and one staged release gate, followed by `git diff --check`,
   commit, and push.
8. Optimization may remove duplicate work, repeated scans, unnecessary rebuilds, or idle
   serialization only. It may never remove a content, evidence, review, or integrity gate.

## Parallelism and release

1. Use at most two isolated topic build lanes unless the user explicitly changes concurrency.
2. Never allow parallel agents to edit the same package, shared file, route destination, index,
   commit, or branch history.
3. Serialize independent reviews, cross-topic obligations, staged release gates, commits, and
   pushes in syllabus order.
4. Each topic independently requires complete Markdown teaching, practice, authored evidence,
   negative tests, independent review, release validation, commit, and push. PDFs are optional
   derived artifacts and are not a completion or release requirement unless explicitly requested.

## Locked practice and integrity rules

1. Correct MCQ positions are independently randomized and reasonably balanced; never impose a
   predictable A-B-C-D cycle.
2. MCQ options must be naturally comparable and free from length, grammar, punctuation, lexical,
   or formatting cues.
3. Exact Mains answer bands are 150-200 words for 10 marks, 250-300 for 15 marks, and 340-400 for
   20 marks.
4. Use stable source IDs/hashes, meaningful source-specific propositions, precise destination
   anchors/payload hashes, parent-only bodies, child unions, large-leaf segmentation, and
   panel-specific parity.
5. Negative tests must mutate copied real packages and invoke the production validator entry
   point, returning nonzero with the expected diagnostic.
6. Release checks must use Git clean-filter-normalized staged equality and must not report
   `release_ready` unless the overall staged release result passes.
7. Never trust a builder or validator summary without independent inspection of the highest-risk
   evidence.

## Conflict rule

If another local note, generated template, agent report, speed target, or scheduling instruction
conflicts with this file for an offline package task, this file and
`Offline-Revision-MCQ\START-HERE.md` control. Stop and repair the conflict rather than silently
skipping, compressing, weakening, merging, or deferring a requirement.

## Topic completion reporting

After each topic passes independent review, staged release validation, commit, and push, provide a
concise completion summary containing:

1. Topic name and final release status.
2. Formal/canonical coverage counts, including raw versus unique semantic evidence where used.
3. Final coverage-derived MCQ count and answer-pattern integrity.
4. Primary/supporting verified PYQ counts through the latest repository year.
5. Original Mains-practice count and locked word-band status.
6. Markdown artifact and validation result; report PDF artifacts only when explicitly generated.
7. Commit hash and push status.
8. Any retrospective repair or unresolved dependency that remains.
