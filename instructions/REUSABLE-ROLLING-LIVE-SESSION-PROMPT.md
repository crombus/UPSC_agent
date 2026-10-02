# Reusable Rolling Live-Session Prompt

## Purpose

Use this file to start or resume a complete subject live-session programme in a new
Copilot terminal without relying on conversation memory.

This file is an operational entry point, not a competing rulebook. The following files
remain authoritative and must be read in full before work begins and before every
generation, repair, independent review and release pass:

1. `live_sessions\LIVE-SESSION-GENERATION-RULES.md`
2. `instructions\GENERATION-OPTIMIZATION-AND-INTEGRITY.md`
3. `instructions\LIVE-SESSION-VALIDATION-AND-RELEASE.md`
4. `instructions\README.md`

If this prompt conflicts with an authoritative file, the authoritative file wins.

## Durable User Decisions

Apply these decisions throughout the programme:

1. No syllabus topic, Basic/Core unit, Advanced unit, book-supported explanation, PYQ,
   criticism, reply, qualification, practice item or remediation unit may be skipped,
   compressed or replaced by a summary.
2. Full syllabus coverage and learner-first depth are required even when time is short.
3. Use dynamic lesson counts based on learning dependencies. Do not force a fixed number
   of lessons.
4. Once a roadmap passes audit, freeze it automatically under standing approval.
5. Do not ask for routine roadmap approval. Ask only when:
   - a substantive syllabus-boundary change is required;
   - a genuine ambiguity cannot be resolved from the approved sources; or
   - the proposed action would deviate from the governing rules.
6. Continue the rolling pipeline automatically. Do not stop after a status report,
   review result, repair completion or release when the next permitted action is known.
7. Earlier-topic repairs take priority over later-topic drafting.
8. A writer's claim that an artifact was independently reviewed is never sufficient.
   Use a separate read-only reviewer on the exact frozen hash.
9. Any substantive edit invalidates the previous review. Recompute the hash, rerun the
   hostile self-audit and mechanical validator, and obtain a new independent review.
10. Release every topic separately and in strict authoritative catalogue order.
11. Apply the consolidated-review optimization on every pass:
    - run mechanical and process-leak scans before semantic review;
    - require the first reviewer to produce one exhaustive blocker-and-advisory ledger;
    - repair all blockers and compatible safe advisories together;
    - use a direct surgical micro-fix for fewer than five isolated defects;
    - retain full exact-hash regression review after every edit.
12. Enforce the strict bounded-repair execution lock:
    - treat the supplied blocker ledger as the complete repair scope;
    - reread mandatory rules and benchmarks once, without reopening settled research;
    - prohibit broad searches, optional enrichment and repeated audits during repair;
    - edit the blockers and their directly dependent locations, run the hostile
      regression sweep and authoritative validator, freeze the new hash and stop;
    - leave fresh full semantic certification to the separate read-only reviewer;
    - controller intervention is mandatory when elapsed time or tool calls become
      disproportionate to the enumerated defects.

## Mandatory Teaching Standard

Before every generation or repair pass, read the learner-facing opening and at least one
complete lesson from each mandatory benchmark:

```text
live_sessions\Philosophy-Optional\01-Nyaya-Vaisesika\Learning-Session-Live-Edition.md
live_sessions\Philosophy-Optional\06-Yoga\Learning-Session-Live-Edition.md
live_sessions\Philosophy-Optional\07-Mimamsa\Learning-Session-Live-Edition.md
```

The pass instruction must explicitly state:

> Preserve or improve the accepted learner-first teaching standard: dependency-led
> sequencing, visual-first explanation, plain-language intuition before terminology,
> full doctrine and argument, examples with limits, strongest objection and reply,
> UPSC application, misconception-driven practice and remediation. Do not skip,
> compress or replace teaching with summaries or source metadata.

Learner-facing lessons must not expose source ownership, repositories, OCR operations,
generation quotas, validation machinery, package assembly, answer-key handling or
internal linkage budgets. Such provenance belongs only in final coverage and source
ledgers where required.

## Source Order and Exclusions

Use the source order defined by the authoritative rules:

1. complete canonical Basic/Core and Advanced Markdown owners;
2. relevant cross-topic canonical owners;
3. verified PYQ ledgers and official papers through 2026;
4. OCR-searchable local books and source PDFs;
5. official live sources where current status genuinely matters;
6. Qdrant only as an optional fallback.

Permanent exclusions for live-session work:

```text
notes\Final-Learning-Packages\
upsc-ai-kit\knowledge\Learner-v2-Refreshed\
```

Do not read, search, cite or derive findings from those paths during roadmap audit,
generation, repair, semantic review, validation or release.

`learning_package_final\` is optional, bounded and non-authoritative. It must never
replace canonical evidence or block progress.

For History, follow the bounded-research rule: complete Basic and Advanced owners plus
one core OCR history source form the substantive base. External research is limited to
exact PYQ verification, a short predeclared material-fact list and one genuine current
linkage where relevant. Do not conduct extensive decorative research.

## Artifact Contract

For the current forward live-session format:

1. Generate one complete
   `live_sessions\<Subject>\<Topic>\Learning-Session-Live-Edition.md`.
2. Generate the entire frozen roadmap in one pass, not one lesson at a time.
3. Each lesson requires:
   - progress line;
   - truthful pre-teach checklist;
   - at least one concept-appropriate visual;
   - intuition before terminology;
   - complete doctrine, mechanism or argument;
   - examples and their limits;
   - relevant comparison;
   - strongest objection, reply and qualified residual;
   - UPSC application;
   - 8-15 revision points;
   - exactly one concept check, concise model answer and misconception note;
   - one original Mains question, complete model and unique quantified rubric.
4. Do not include a compiled four-option MCQ corpus.
5. Include distinct final original 10-, 15- and 20-mark Mains questions, models and
   quantified rubrics.
6. Keep 10-mark models within 150 words and 15/20-mark models within 250 words.
7. Displayed PYQs must remain answer-neutral: no answer letter, truth marking,
   elimination cue, corrective mapping or language that identifies the unique answer.
8. Do not include solved PYQ model answers or generate a replacement solved-PYQ workbook.
9. Preserve exact verified wording, directive, marks and printed or instruction-derived
   word-limit provenance.
10. Use exactly one genuine file-level current linkage unless the governing roadmap
    explicitly establishes otherwise. Static docket verification does not become a
    second linkage, but it must be accurately labelled and sourced.
11. Consolidated register notes must be the final teaching section before the coverage
    matrix and source ledger.
12. Preserve the exact final H1 arc required by the authoritative rules.
13. Include the complete `## SOURCE-MANIFEST GATE`.
14. Use UTF-8, LF-only line endings, balanced fences and exactly one final newline.

## Rolling Continuous Pipeline

Maintain three logical blocks:

```text
Topic N     -> independent review, repair and sequential release
Topic N+1   -> source audit or bounded repair
Topic N+2   -> complete bounded draft from a frozen roadmap
```

Operational rules:

1. Use at most two concurrent generation or repair writers.
2. Read-only source audits and exact-hash semantic reviewers may overlap with writers.
3. One topic file has one writer at a time.
4. Shared index edits, staging, commits, pushes and releases are strictly sequential.
5. Later topics may be drafted or reviewed, but cannot release before every earlier
   catalogue topic.
6. When a writer slot opens:
   - first assign the earliest unreleased repair;
   - otherwise assign the next frozen roadmap;
   - keep future roadmap audits ready so writer lanes do not sit idle.
7. Do not stop merely to ask whether the pipeline should continue.

## Roadmap and Generation Sequence

For each topic:

1. Read all governing instructions and mandatory benchmark lessons.
2. Identify the matching Basic/Core and Advanced owners.
3. Audit syllabus, canonical owners, relevant cross-topic owners, books and PYQs.
4. Create a complete gap ledger and dependency-led roadmap.
5. Freeze an audit-passed roadmap automatically.
6. Generate the complete topic file.
7. Reread all rules.
8. Freeze the SHA-256.
9. Run the mandatory hostile self-audit.
10. Run the consolidated pre-review mechanical and semantic scans defined in
    `instructions\GENERATION-OPTIMIZATION-AND-INTEGRITY.md`.
11. Run:

```powershell
python tools\validate_live_session.py "<topic-file>"
```

12. Give a separate read-only reviewer the full exact hash and require one exhaustive
    blocker-and-safe-advisory ledger across every review dimension.
13. If the review fails, provide that complete consolidated ledger to the repair writer
    and repair all compatible items together under the strict bounded-repair execution
    lock. Do not reopen generation, broad source research or the completed review.
14. For fewer than five isolated mechanical or textual defects, prefer one direct
    surgical micro-fix over another long research cycle.
15. After every repair, stop the writer after its hostile regression sweep, validator,
    new hash and scoped-change report; then repeat steps 7-12 through a separate
    independent reviewer on the new hash.
16. Only an independently passed exact hash may enter release.

## Independent Review Contract

The reviewer must:

1. compute the SHA-256 before reading and halt on mismatch;
2. remain read-only;
3. reread all authoritative instructions and benchmark lessons;
4. inspect the complete canonical owners and actual permitted evidence;
5. review the whole file for regressions, not only the supplied blockers;
6. verify every substantive coverage claim and every displayed PYQ;
7. verify current legal or policy status through the stated review date;
8. verify learner-facing prose contains no internal process language;
9. rerun the validator and formatting gates;
10. report `PASS` only when the exact hash is releasable, or `FAIL` with numbered,
    precise, release-blocking defects and required corrections.

The first review must be exhaustive and include every safe source-supported advisory
that should be repaired in the same pass. A rereview remains a full regression review
and may still block a genuinely new critical defect, but it must not manufacture new
cycles from settled stylistic preferences.

## Sequential Release

After exact-hash independent PASS:

1. Add exactly one verified row to `live_sessions\INDEX.md` containing:
   - subject and topic;
   - lesson count;
   - current word count;
   - first 12 characters of the passed SHA-256;
   - correct relative link.
2. Confirm the Git staging area is empty.
3. Run dry preflight:

```powershell
python tools\release_live_session.py "<topic-file>" `
  --commit-title "<topic commit title>"
```

4. If preflight passes, execute:

```powershell
python tools\release_live_session.py "<topic-file>" `
  --commit-title "<topic commit title>" `
  --execute
```

5. Require remote parity `0/0`.
6. Record the passed hash and commit.
7. Immediately continue to the next pipeline action.

## Multiple-Terminal Safety

Do not run several writing terminals against the same workspace and branch.

For parallel subject programmes:

1. create a separate Git worktree and branch for each subject;
2. give each terminal exclusive ownership of one subject/worktree;
3. keep the two-writer limit inside each coordinated subject pipeline;
4. designate one coordinator terminal to merge subjects;
5. only the coordinator edits the shared `live_sessions\INDEX.md` on the integration
   branch and performs final sequential releases;
6. never allow two terminals to edit rules, the same topic, the index or Git history
   concurrently;
7. before merging, independently review the exact branch artifact and recheck conflicts,
   hashes, index data and release order.

Multiple terminals improve drafting throughput but do not remove semantic-review or
release bottlenecks.

## Resume Discovery

Never trust a stale handoff as the sole status source. On every new terminal:

1. read this file and all authoritative files;
2. inspect `live_sessions\INDEX.md` to identify the last released topic;
3. inspect the authoritative Basic/Core and Advanced catalogue counts;
4. inspect `git status`, but do not revert unrelated user changes;
5. locate unreleased topic files and compute their hashes;
6. retrieve any existing review or blocker records;
7. reconstruct the three pipeline blocks;
8. resume automatically from the earliest unreleased topic.

## Copy-Paste Startup Prompt

Replace the bracketed values and paste this into a new isolated terminal:

```text
Run the complete rolling continuous live-session pipeline for [SUBJECT] in:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent

First read in full:
- instructions\REUSABLE-ROLLING-LIVE-SESSION-PROMPT.md
- instructions\README.md
- live_sessions\LIVE-SESSION-GENERATION-RULES.md
- instructions\GENERATION-OPTIMIZATION-AND-INTEGRITY.md
- instructions\LIVE-SESSION-VALIDATION-AND-RELEASE.md

Then read the mandatory Nyaya-Vaisesika, Yoga and Mimamsa benchmark opening plus at
least one complete lesson from each.

Discover the authoritative [SUBJECT] Basic/Core and Advanced catalogues, inspect
live_sessions\INDEX.md and Git state, and identify the earliest unreleased topic.

Follow all rules with no skipping, no compression and full syllabus coverage. Use the
rolling three-block pipeline, at most two isolated writers, independent exact-hash
semantic review, surgical repair and strictly sequential release. Audit-passed roadmaps
freeze automatically. Do not ask for routine approvals and do not stop when the next
permitted pipeline action is known.

Apply the mandatory consolidated-review optimization on every pass: front-load
mechanical and process-leak scans, require one exhaustive first-review ledger, repair
blockers and safe advisories together, and use direct micro-fixes for fewer than five
isolated defects while preserving fresh hashes and independent rereview.

Never use notes\Final-Learning-Packages or learner-v2 artifacts. Preserve learner-first
teaching and keep all generation, source-routing and validation machinery out of
learner-facing lessons.

If this terminal is one of several parallel subject terminals, work only in its assigned
Git worktree and branch. Do not edit the shared integration INDEX or release from the
integration branch; leave merging and final release to the coordinator.
```
