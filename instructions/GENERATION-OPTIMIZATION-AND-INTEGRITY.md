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

## Mandatory defect-prevention pass

For every live-session generation or repair, optimize for fewer review cycles by
requiring a distinct hostile self-audit before independent handoff. The writer must
freeze the final hash, reread all governing instructions, and test the artifact as an
adversarial reviewer would.

At minimum, the self-audit must measure and inspect:

- complete lesson-level Basic/Core, Advanced, book and PYQ coverage;
- accidental omission, compression, merging or misclassification of Core material;
- repeated teaching shells and visuals that are not concept-appropriate;
- every MCQ stem, option, key and explanation;
- correct-option length-rank distribution and categorical or impossible distractors;
- duplicate stems, options, explanations and answer-shape cues;
- lesson-local dependency and forward references;
- lesson-local and final Mains model counts, word ceilings and unique scoring notes;
- exact PYQ wording, response choices, ownership and inferred-key labels;
- factual, chronological, numerical and source-path integrity;
- source exclusions, manifest statuses, encoding, formatting and scoped Git checks.

Only a clean self-audited hash may enter independent review. If the artifact changes,
repeat the self-audit on the new hash. This is a safe operational optimization because
it moves known checks earlier; it never reduces independent review, coverage, depth,
practice or release safeguards.

## Approved live-session optimizations

The following are approved safe operational optimizations:

1. Use `tools\validate_live_session.py` as the single authoritative mechanical
   validator for live-session Markdown.
2. Require the source-manifest gate defined in
   `instructions\LIVE-SESSION-VALIDATION-AND-RELEASE.md`.
3. Use `tools\release_live_session.py` for fail-fast release preflight and execution.
4. Give every generation or repair lane the same validator before handoff.

These tools consolidate repeatable checks. They do not replace the independent
controller's semantic review of learner sequencing, doctrine, source reliability,
PYQ ownership, MCQ keys, distractors, explanations, Mains answers or completeness.

## History bounded-research rule (approved 28 September 2026)

For History live-session generation and repair, do **not** conduct extensive
research. The substantive base is:

1. the complete `basic/` owner and the complete `advanced/` owner for the topic; and
2. one core OCR history source for that period.

External or live research is limited to exactly three purposes:

- **(a) PYQ verification and routing** - confirming exact wording, marks, directive,
  year, paper and ownership from verified ledgers or locally held official papers;
- **(b) one bounded material-fact pass** for either a genuinely disputed fact, date or
  statistic that affects teaching, or a short enumerated set of standard connecting
  names and dates whose omission would create a real syllabus gap; and
- **(c) one brief bounded current linkage**, only where a genuine linkage exists.

Do not chase optional sources, exhaustive corroboration across multiple books, or
decorative current affairs. Finish promptly from material already collected.

The material-fact pass is not a general research licence. Define the missing or
disputed items before searching, use the minimum reliable source set, stop when that
list is resolved, and record provenance in the final source ledger rather than in
learner-facing lesson labels. Do not repeat `material-fact pass`, source ownership or
generation-process language throughout the teaching.

This rule limits **source volume**, not teaching. Full syllabus coverage, the
no-skipping and no-compression locks, lesson-level completeness, practice,
remediation, Mains models and the hostile pre-handoff self-audit all remain
binding and unchanged. Where the bounded base and the single material-fact pass leave
a point unresolved, record it as open uncertainty rather than expanding research or
inventing evidence.

## Staged rolling pipeline

For long sequential subject programmes, use a continuous rolling pipeline without
weakening strict syllabus release order:

1. **Topic N — review and release lane**
   - freeze the exact artifact hash;
   - run controller mechanical validation;
   - conduct independent exact-hash semantic review;
   - repair every blocker and repeat review on the new hash;
   - update the shared index only after final PASS;
   - dry-run and execute the guarded release;
   - require remote parity `0/0`.
2. **Topic N+1 — audit or repair lane**
   - audit a frozen file read-only;
   - give every repair writer the complete blocker ledger;
   - permit only one writer to edit that topic;
   - require a fresh hash, hostile self-audit and controller validation after every
     repair.
3. **Topic N+2 — bounded draft lane**
   - generate complete learner-first teaching, Mains practice, sources and a strong
     initial assessment;
   - run one mechanical validation pass;
   - stop instead of spending an unbounded turn on repeated semantic or rank
     optimisation;
   - leave final assessment optimisation to the separate audit and repair stages.

Later topics may be drafted or audited while an earlier topic is being repaired or
released, provided every topic file has one isolated owner. Shared index updates,
commits, pushes and releases remain strictly sequential. No later topic may be
released before every earlier syllabus topic has passed.

When a drafting slot becomes free, begin the next bounded topic draft while the
review and repair lanes continue. This scheduling rule creates continuous flow; it
does not permit additional generation lanes beyond the concurrency limit in the
authoritative live-session rules.

## Assessment construction and audit stages

Do not combine source research, complete teaching generation, exhaustive assessment
optimisation, independent semantic review and repeated repair into one unbounded
agent turn. Use these bounded stages:

1. complete content, source, PYQ and Mains construction;
2. construct the lesson-local and cumulative concept checks with misconception
   remediation;
3. run controller mechanical checks;
4. run one complete independent exact-hash semantic review;
5. use a direct micro-fix for fewer than five isolated defects or a bounded repair
   lane for systemic defects;
6. repeat exact-hash review and release sequentially.

The split is an execution optimization only. The final artifact must still satisfy
all learner-first, no-skipping, no-compression, semantic-assessment, source, PYQ,
Mains, hostile-audit and release requirements.

## Consolidated-review optimization (approved 30 September 2026)

Apply this optimization during every generation, review and repair pass. Its purpose is
to reduce repeated review cycles by finding and fixing all discoverable defects together.
It does not reduce semantic review, exact-hash control or release standards.

1. **Front-load mechanical scans.** Before independent semantic review, run the
   authoritative validator and targeted scans for:
   - prohibited learner-facing process, source-routing and package language;
   - PYQ quotation, marks, word-limit and answer-neutrality defects;
   - missing coverage-matrix, register-note and source-ledger mappings;
   - stale status dates, unsupported source paths and manifest defects;
   - formatting, encoding, fence and whitespace failures.
2. **Require one exhaustive first review.** The first independent exact-hash reviewer
   must inspect the complete artifact across all review dimensions in one pass:
   Core/Advanced/book coverage, doctrine, examples, objections and replies, PYQs,
   current status, practice, register notes, coverage matrix, source ledger, process
   leakage and formatting. The reviewer must report one consolidated numbered ledger
   containing:
   - every release blocker;
   - every safe, source-supported advisory that can be repaired without changing the
     frozen roadmap or approved scope;
   - regression risks for each repair.
   Reviewers must not intentionally defer a discoverable defect to a later cycle.
3. **Repair blockers and safe advisories together.** Give the writer the complete
   consolidated ledger once. The writer must fix every blocker and all compatible safe
   advisories in the same bounded repair pass, then update all dependent lesson,
   revision, practice, register, coverage and source locations so no stale formulation
   remains.
4. **Use direct micro-fixes for isolated defects.** When a reviewed hash has fewer than
   five truly isolated textual defects and the correction is mechanically clear,
   perform one direct surgical micro-fix instead of opening another long research or
   generation cycle. The fixer must still reread the governing rules, preserve the
   learner-first lock, recompute the hash, rerun the hostile self-audit and validator,
   and obtain independent review of the new exact hash.
5. **Keep rereview complete but focused.** The rereviewer must verify every supplied
   correction and run a full regression sweep. A genuinely new critical defect still
   blocks release; speed never permits ignoring it. However, the rereviewer must not
   reopen settled stylistic preferences or promote a previously disclosed
   non-source-supported preference into a blocker.
6. **Maintain continuous capacity.** Keep two writer lanes occupied whenever eligible
   generation or repair work exists, keep read-only roadmap audits several topics ahead,
   and run independent read-only reviews in parallel where safe. Shared index, commit,
   push and release operations remain strictly sequential.

Every generation, repair and review prompt must explicitly invoke this consolidated-
review optimization. A generic instruction to "optimize" is insufficient.

## Strict bounded-repair execution lock (approved 2 October 2026)

When independent review returns a finite blocker ledger, the repair pass is strictly
limited to that ledger and its directly dependent locations. A repair writer must not
turn a bounded correction into another generation, source audit or independent review.

Apply all of the following:

1. Reread the mandatory governing files and benchmark lessons once at the start of the
   pass, as required. This reread is a compliance gate, not permission to reopen settled
   research or repeat the completed semantic audit.
2. Freeze the repair scope before editing: enumerate the supplied blockers, the exact
   lesson or section locations affected, and the dependent revision, register, coverage
   and source-ledger locations that must remain consistent.
3. For fewer than five isolated defects, use one direct surgical micro-fix. Use the
   evidence already identified by the reviewer and the minimum canonical or official
   source needed to resolve a stated uncertainty.
4. Do not perform broad repository searches, reread unrelated source units, pursue
   optional enhancements, add decorative material, reopen settled findings or conduct
   repeated hostile audits during the same repair pass.
5. After the bounded edits, run one complete hostile regression sweep using deterministic
   local checks where possible, run the authoritative validator once, compute the new
   exact hash and report immediately. If a check fails because of the repair, correct
   only that reported failure and rerun the failed check.
6. Stop the repair pass after the required report. Fresh full semantic certification of
   the new hash belongs to the separate independent reviewer, never to the repair writer.

Elapsed time and tool calls must remain proportionate to the enumerated repair scope.
Repeated scans or research without a newly identified release-blocking reason are a
pipeline defect and must be stopped by the controller. This execution lock improves
speed only; it does not weaken required rule rereads, no-skipping or no-compression,
whole-file regression safety, exact-hash review or release gates.

For existing released or explicitly preserved pre-rule legacy live sessions:

- preserve exact `A -> B -> C -> D` key rotation;
- show the complete question set before its answer and explanation block;
- use three plausible same-domain near-neighbour distractors;
- provide four clause-aligned explanations;
- make incorrect misconception families semantically distinct across the corpus;
- reject categorical, invented, caricatured, meta-key, grammatical and
  qualification-only cues;
- calculate correct-option word and non-space-character ranks with deterministic
  A-D tie-breaking;
- reject four-question common upper/lower-half windows, three-question strict
  shortest/longest runs and strict `1 <-> 4` alternations of length four or more;
- inspect global rank distribution, extreme clustering and key/rank association;
- rebalance semantically rather than padding option length.

For every newly generated live session, regardless of subject or topic number, do not
construct or audit a compiled MCQ corpus. Each lesson instead requires exactly one
answer-free concept check, one concise model answer and one misconception-to-avoid note.
Audit those three elements for conceptual correctness, lesson-local teachability,
source fidelity and duplication. Topic numbering alone never activates the legacy MCQ
contract. This forward-only trade-off removes option-balancing work from live sessions
without reducing teaching, PYQ, Mains, remediation or separate-workbook requirements.

This live-session policy does not create, copy or relocate an MCQ corpus into a
workbook during live-session generation. When a separate workbook is generated under
its own workflow, apply that workflow's key-placement rule: complete-topic package
workbooks retain strict `A -> B -> C -> D` rotation, while exam-generation and
interactive-test workflows retain independently randomized option placement. Do not
blend those workflow-specific rules.

Displayed unkeyed PYQ blocks must remain answer-neutral: no answer letter,
truth-value marking, option elimination, corrective mapping or wording that
effectively identifies the unique answer.

## Permanent live-session source exclusion

For every subject and every live-session generation, reconstruction, repair, audit,
validation and release pass, exclude the entire directory:

```text
notes\Final-Learning-Packages\
```

Do not read, search, cite or derive conclusions from its learning sessions, solved
workbooks, ASCII or graphical flowcharts, package reviews, indexes or any other
derived artifact. No defect finding, correction or release verdict may depend on
them. Keep the files unchanged so the user may reconsider their use in a future,
separately approved workflow.

This is a requirement-affecting rule explicitly approved by the user. It overrides
older live-session source-routing language that treated Final-Learning-Packages as a
reference. It does not alter separate workflows whose explicit task is to review,
repair or export Final-Learning-Packages themselves.

When genuinely needed, live-session work may consult relevant artifacts under:

```text
learning_package_final\
```

This permission is optional, not a mandatory source gate. Treat those artifacts only
as bounded completeness, learner-sequencing, practice or remediation checks. They
must not override canonical Markdown, verified PYQs, books or official evidence, and
must not replace an independent no-skipping and no-compression audit.

Every generation and repair pass must begin with an explicit learner-first preamble.
The pass instruction must state that the final result must preserve or improve the
accepted learner-facing teaching quality, sequencing, visuals, examples, objections,
replies, practice and remediation. A generic instruction to "follow the rules" is not
enough.

Before every generation or repair pass, read the opening and at least one complete
lesson from each of:

- `live_sessions\Philosophy-Optional\01-Nyaya-Vaisesika\Learning-Session-Live-Edition.md`
- `live_sessions\Philosophy-Optional\06-Yoga\Learning-Session-Live-Edition.md`
- `live_sessions\Philosophy-Optional\07-Mimamsa\Learning-Session-Live-Edition.md`

Treat their natural learner-facing terminal flow as the mandatory primary style
benchmark across subjects: roadmap-led sequencing, visible pre-teach context and
progress, visual-first intuition, numbered teaching, precise distinctions and
qualifications, exam linkage, mini recap, revision notes and adaptive
misconception-driven mastery practice. Reuse the integrated teaching architecture,
never either topic's doctrine, wording or a mechanically fixed lesson size.

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
