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
9. Before every pass, use `Offline-Revision-MCQ\workflow\offline_workflow.py begin-pass` to read
   and hash this file and `START-HERE.md`, record the timestamp and pass type, and attest the
   pre-pass gates in `PASS-MANIFEST.json`.
10. Freeze parsed source evidence in `EVIDENCE-CACHE.json`. Reuse it only when every source path,
    byte count, and SHA-256 hash is unchanged; otherwise invalidate and reparse it.
11. Create `RISK-REVIEW-PACKET.json` for focused reviews. Include changed files, rejected findings,
    affected obligation IDs, approved frozen counts, and frozen surfaces. Direct contradictory
    evidence may reopen a frozen surface; convenience may not.
12. Run the shared semantic lint before an expensive rebuild. Dangling fragments, generic-only
    anchors, unsupported representation links, and option cues must be repaired before the full
    development gate.
13. Enforce `VALIDATOR-INDEPENDENCE-CONTRACT.json`: validators may share neutral parsing/hash
    helpers, but may not import builder expectations, question banks, renderer truth, or source
    provenance constants.
14. During focused repair, run the negative tests selected for the changed invariants. The full
    copied-package negative suite remains mandatory at the final development gate.
15. Register approved sources in the immutable hash-bound source registry with provenance,
    rights, authority role, and permitted scope. Registration never broadens source authority.
16. Optimization means materially reducing elapsed time, not merely adding integrity records.
    Every pass must declare an elapsed-minute budget and a tool-call budget in its pass manifest.
    A focused repair or focused review should normally fit within 45 minutes and 30 tool calls;
    a complete development or boundary pass should normally fit within 90 minutes and 60 tool
    calls. Use a smaller budget when the remaining defect is narrower.
17. A budget is a hard stop, not a target. When either limit is reached, stop without starting
    another search, edit, rebuild, or validation cycle; preserve the worktree and report the
    verified state, exact blocker, commands already run, and remaining bounded action. Continuing
    requires a new explicit pass manifest rather than a silent extension.
18. Within one pass, run at most one expensive complete build and one complete copied-package
    negative suite. During editing use semantic lint, focused validators, and focused negative
    tests. Do not rerun a complete gate after it passes unless a later change can affect it.
19. After every pass, report elapsed time, tool-call use, number of complete builds/full negative
    suites, result, and any blocker. A pass that spends most of its budget rediscovering frozen
    scope or repeating successful checks is an optimization failure and must not continue.

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
