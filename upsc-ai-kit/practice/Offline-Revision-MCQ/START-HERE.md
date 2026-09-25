# Offline Revision and MCQ System

This directory is the portable, Agency-independent study and practice system.
It must remain fully usable from the repository in Markdown form. PDFs are optional derived
artifacts generated only when the user explicitly requests them.

For AI/Copilot execution of package generation, reconciliation, review, validation, release, or
scheduled continuation, first read `C:\up\OFFLINE-PACKAGE-AGENT-INSTRUCTIONS.md`. That file contains
agent-only workflow mechanics. It does not apply to interactive Guided Tutor or other live learning
sessions.

## Recall and continuation commands

- `Recall Offline Revision System`
  - Read this file and `STATUS.json`.
  - Report the saved rules, completed subjects, current subject, and next pending action.
  - Do not generate or modify content unless the user separately asks to continue.
- `Resume Offline Revision System`
  - Read this file and `STATUS.json`.
  - Continue from the exact next pending subject or topic.
  - Preserve all completed files, attempts, logs, and validation records.

## Locked requirements

1. Work only on branch `feature/offline-revision-mcq-system` in the isolated worktree.
2. Process one subject completely before beginning the next subject.
3. Subject order:
   1. Philosophy
   2. Art and Culture
   3. Economy
   4. Polity
   5. Political Theory
4. Never modify or delete the canonical learning packages, source knowledge files, existing
   all-topic MCQ atlas, existing practice logs, or learner attempts.
5. Read canonical source material in this order:
   1. Final Markdown learning session.
   2. Final solved-practice workbook.
   3. Existing quick-glance, flowchart, and graphical revision material.
   4. Verified PYQs and current-affairs material where relevant.
6. **Latest-paper rule (locked):**
   - Include every verified available PYQ through the latest year present in the repository;
     the current latest repository year is **2026**.
   - Never hard-code a stopping year. Recheck the repository's verified PYQ sources whenever a
     topic is generated, repaired, or validated.
   - Verify exact wording and marks against an official paper scan/OCR export or an explicitly
     verified repository ledger.
   - Assign each question-part to exactly one primary topic and add cross-links for genuinely
     shared demands; cross-links must not inflate ownership counts.
   - Do not invent, reconstruct, or imply questions that are not available in verified evidence.
7. **Solved-PYQ rule (locked):**
   - Every verified PYQ routed to a topic must appear in that topic's
     `ANSWER-WRITING-TOOLKIT.md`, which is also the topic's solved Mains/PYQ workbook.
   - A question-only listing, answer spine, or brief hint does not count as solved.
   - Every PYQ requires its year, question number, marks, exact verified wording, demand decoding,
     complete independent model answer, important qualification or criticism, and an explanation
     of why the structure earns marks.
   - Clearly state that model answers are independent learner practice and are not official UPSC
     answer keys.
8. No skipping:
   - Cover every canonical topic and every substantive subtopic in the selected subject.
   - Cover definitions, classifications, mechanisms, chronology, institutions, laws, exceptions,
     comparisons, criticisms, examples, current linkages, PYQ demands, and application.
9. No compression:
   - Do not replace complete teaching or revision material with a generic short summary.
   - Preserve all substantive reasoning, distinctions, examples, diagrams, flow logic, traps,
     qualifications, and answer-writing value.
   - Remove only true duplication, chat noise, tool output, and navigation prompts.
10. **Formal-session reconciliation and repair rule (locked):**
    - Source locations are fixed:
      - completed formal learning sessions and solved workbooks live under
        `C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\learning_package_final`;
      - canonical topic knowledge and verified PYQ ledgers live under
        `C:\up\upsc-ai-kit\knowledge`, organized by subject.
      Learner-v2 or other regenerated outputs are derivative evidence unless explicitly promoted
      to formal authority.
    - Before repairing a generated topic package, treat the completed formal learning session,
      its roadmap, and its formal teaching blocks as required coverage evidence alongside the
      canonical owner and solved-practice workbook.
    - If no completed formal learning session exists, declare
      `canonical_without_formal_session` provenance. In that mode, every canonical heading/block
      is mandatory coverage, while learning sessions, workbooks, and regenerated material are
      supplementary evidence only. Use those references to deepen teaching, examples, visuals,
      traps, and practice, but do not duplicate their derivative headings as mandatory coverage
      rows or pretend they are formal-session authority.
    - Build a pre-edit mapping from every formal subtopic and teaching block to the package
      surfaces where it is taught, revised, tested, and transferred to answer writing.
    - Classify every unmatched concept as exactly one of:
      1. a genuine in-scope omission;
      2. correctly owned by the next or another canonical topic, with an explicit bounded
         cross-link and no duplicate primary ownership; or
      3. excluded doubt-only enrichment with no independent syllabus, textbook, or PYQ relevance.
      If a doubt introduced an independently relevant concept, reclassify it under 1 or 2; it
      cannot remain in category 3.
    - A concept routed under category 2 must create a machine-readable inbound obligation for its
      destination topic. Record the obligation identifier in both topics' coverage records, and
      make the destination topic's validation fail until it teaches, tests, or explicitly
      re-routes the obligation. Recording a cross-link alone does not close coverage.
    - The formal session is required evidence, not the sole authority. Canonical topic
      boundaries, canonical ownership, verified PYQs, and existing ownership rules remain
      controlling when sources disagree. The content read-order in rule 5 does not transfer
      ownership or override a verified canonical boundary.
    - Do not rewrite, shorten, or reorganize existing correct material merely for consistency.
      Surgical correction is allowed where accuracy or cross-surface consistency requires it,
      but depth and valid learner history must be preserved.
    - For each genuine omission, repair every affected canonical surface: substantive lesson and
      visual, revision/register notes, coverage ledger, MCQs and option-specific explanations,
      affected direct PYQ or original Mains models, solved workbook, metadata, and validators.
      Repair optional PDFs only when the user explicitly requested PDF generation for that pass.
      Any added MCQ must obey rules 16–21, and the package's coverage-sized total must be
      re-justified rather than merely incremented.
    - **Optimized execution workflow (locked):**
      1. Run one exhaustive preflight before editing: extract formal blocks, large leaves,
         panels, verified PYQs, routes, obligations, and affected package surfaces.
      2. Freeze the resulting coverage/defect ledger. Do not repeatedly rediscover scope or
         reopen already cleared surfaces unless a later change can affect them.
      3. Validate incrementally in this order: source and block identity; authored proposition
         quality; routes and ownership; MCQs and timed answers; generated artifacts.
      4. Use shared, already-tested validation mechanisms for common integrity gates. Keep
         topic-specific validators limited to source paths, counts, obligations, semantic
         assertions, and genuine topic exceptions.
      5. Stabilize and validate learner-visible Markdown as the complete canonical package. Do
         not generate, update, stage, or commit PDFs by default. If the user explicitly requests
         PDFs, generate them only after Markdown stabilizes; validator-only, metadata-only, or
         review-JSON-only changes must not trigger PDF regeneration.
      6. After the first complete independent review, use focused re-reviews only for the newly
         changed risk area. Do not re-audit unrelated surfaces that remain mechanically and
         semantically unaffected.
      7. Finish with one full development validation, one staged release validation, `git diff
         --check`, then commit and push. These optimizations reduce repetition only; they never
         waive coverage, semantic integrity, independent review, or release gates.
      8. Start every pass with `workflow\offline_workflow.py begin-pass`. The resulting
         `PASS-MANIFEST.json` must record fresh hashes of both controlling instruction files,
         the read timestamp, pass type, and explicit pre-pass attestations.
      9. Use a hash-bound `EVIDENCE-CACHE.json` to avoid reparsing unchanged sources. Any path,
         byte-count, or SHA-256 change invalidates the cache and requires a fresh parse.
      10. Use `RISK-REVIEW-PACKET.json` to constrain focused reviews to changed files, rejected
          findings, affected obligations, and frozen approved counts. Reopen frozen surfaces only
          when direct contradictory evidence requires it.
      11. Run shared semantic lint before full regeneration. It is an early gate for dangling
          propositions, generic-only semantic anchors, unsupported representation links, and
          option cues; it never replaces production validation.
      12. Enforce the validator-independence contract. Neutral parsing/hash helpers may be shared,
          but validators must independently derive expected truth and may not import builder
          expectations, question banks, renderer output, or source-provenance constants.
      13. Run focused negative-test cases for changed invariants during repair, then run the
          complete copied-package suite once at the final development gate.
      14. Record every approved formal, canonical, verified-PYQ, or user-approved primary source
          in the immutable source registry with exact hash, provenance, rights, authority role,
          and permitted scope. A registry entry never transfers or expands ownership.
    - **Mandatory pre-pass compliance gate (locked):**
      - Before every development, independent-review, focused-repair, optional PDF, or release pass,
        verify against the frozen ledger that the complete syllabus, canonical/formal
        obligations, relevant verified PYQs, traps, comparisons, criticisms, applications,
        visuals, and answer-writing transfer remain covered.
      - Confirm explicitly that no concept or required surface was skipped, compressed, merged
        away, weakened, or deferred.
      - Recompute MCQ sufficiency from an explicit topic-specific test-cell matrix. A familiar,
        equal, convenient, or template total is never evidence of completeness.
      - Optimize only duplicate work, repeated scans, unnecessary rebuilds, and idle
        serialization. Never optimize away a content, evidence, review, or integrity gate.
      - If any check fails, stop that pass, freeze the defect, repair it, and rerun only the
        affected focused checks before the final full gate.
    - **Safe parallelism rule (locked):**
      - Independent topics may be reconciled concurrently when they have isolated package
        directories, independent source ledgers, and no unresolved cross-topic ownership writes.
      - Every parallel topic keeps its own exhaustive preflight, frozen coverage ledger,
        substantive repairs, authored review, validators, independent review, staged release
        gate, commit, and push. Optional PDFs are handled only when explicitly requested.
        Parallel execution never combines or substitutes these per-topic requirements.
      - Never skip, summarize away, compress, weaken, or defer required teaching, visuals,
        revision notes, MCQs, explanations, PYQs, Mains models, obligations, metadata, or
        validation merely to increase throughput.
      - Cross-topic obligations and shared files are serialized: one designated owner edits and
        validates them, while dependent topics wait at their release gate. Commits and pushes are
        also serialized to prevent conflicting histories or incomplete releases.
      - Parallelism is a scheduling optimization only. Topic completeness and validity are judged
        by the same locked standards as sequential execution.
    - Interpret any request to `preserve answer rotation` as preserving a valid randomized,
      non-gameable answer distribution where possible. It never overrides the locked rule against
      predictable A→B→C→D rotation, answer runs, lexical cues, or length/punctuation cues.
    - Finish with `FORMAL-COVERAGE-AUDIT.json`, a machine-readable row for every formal block
      recording its source anchor, classification, destination surface or routed owner, evidence,
      inbound-obligation identifier where applicable, and validation result. A repair cannot pass
      while a formal block is unclassified or a due inbound obligation is unresolved.
11. Do not overwrite existing learner history. Generation must be deterministic and resumable.
12. Validate each pilot topic before generating the full subject.
13. Commit and push each validated subject or other coherent milestone to the isolated branch.
    Keep every push comfortably below GitHub's 2-GiB limit.

## Directory architecture

```text
Offline-Revision-MCQ\
|-- START-HERE.md
|-- STATUS.json
|-- INDEX.md
|-- HOW-TO-STUDY-AND-PRACTISE.md
|-- ANSWER-WRITING-GUIDE.md
`-- <Subject>\
    |-- SUBJECT-GUIDE.md
    `-- <Section>\
        `-- <Topic>\
            |-- README.md
            |-- REVISION-GUIDE.md
            |-- MCQ-QUESTIONS.md
            |-- MCQ-SOLUTIONS.md
            |-- COVERAGE-LEDGER.md
            |-- FORMAL-COVERAGE-AUDIT.json
            |-- PRACTICE-LOG.md
            |-- ANSWER-WRITING-TOOLKIT.md
            |-- attempts\
            `-- pdf\                         # optional; created only on explicit request
```

## Study workflow

### Previously studied topic

```text
Closed-book diagnostic recall
        |
        v
Review quick-glance notes and reconstruct visuals
        |
        v
Revise only missing or uncertain sections
        |
        v
Attempt hard MCQs one at a time
        |
        v
Study detailed feedback and repair errors
        |
        v
Produce an oral or written answer outline
        |
        v
Complete delayed and interleaved retests
```

### New or severely forgotten topic

```text
Broad pretest
    |
    v
Complete learning session
    |
    v
Closed-book reconstruction
    |
    v
Quick-glance and visual review
    |
    v
Hard MCQs and detailed feedback
    |
    v
Answer-writing transfer and delayed retest
```

### Revision priority

1. Closed-book recall of the topic structure.
2. Quick-glance notes, keywords, provisions, institutions, chronology, exceptions, and traps.
3. Flowcharts, comparison tables, timelines, diagrams, and maps.
4. Detailed learning-session sections only where recall or understanding failed.
5. Hard MCQs without notes.
6. Answer-writing transfer.

## MCQ rules

1. Use hard UPSC-style MCQs by default.
2. Present one question at a time during interactive practice.
3. Withhold the answer until the learner responds.
4. Independently randomize the correct-option position for every delivered question.
5. Do not use predictable answer-key rotation.
6. Keep options comparable in visible length, grammar, specificity, and detail.
7. Never make the correct answer identifiable through wording, length, precision, or formatting.
8. Use plausible, syllabus-relevant distractors.
9. Ask the learner for an option, brief reasoning, and confidence level.
10. Treat a correct guess as not mastered.
11. Give the result and then analyse every statement or option.
12. Expand abbreviations and explain the objectives, functions, legal basis, and key timeline of
    relevant laws, schemes, institutions, and mechanisms.
13. Explain the exact trap behind each wrong option.
14. Save every question, answer, confidence level, result, explanation, doubt, and remediation.
15. Repeat concepts only for deliberate remediation using a different or harder angle.
16. Question totals are coverage-driven, never fixed in advance.
17. Never copy a previous topic's MCQ count or use a round/template count as a stopping rule.
18. Before writing questions, derive a topic-specific test matrix from the syllabus, revision
    guide, coverage ledger, verified PYQs, major comparisons, criticisms, applications, and likely
    misconceptions.
19. Assign enough questions to each matrix cell to test recognition, reasoning, elimination, and
    transfer where those are substantively distinct. One question may cover multiple cells only
    when it genuinely tests each of them.
20. Record the resulting justified total in the coverage ledger and validation report. Different
    topics are expected to have different totals; an identical total requires independent
    coverage-based justification, not consistency with earlier packages.
21. Audit for redundancy after coverage is complete. Do not inflate the bank with paraphrases
    merely to reach a target, and do not stop while a substantive cell remains weak or untested.

## Coverage-driven completion

A topic is not complete merely because a question target has been reached. Continue when:

- a substantive syllabus cell remains untested;
- a learner answer reveals a new misconception;
- an answer was correct only by guessing;
- a high-confidence error remains unresolved;
- success depends on recognizing familiar wording;
- no delayed retest has confirmed retention; or
- the learner cannot explain or apply the concept without options.

Initial intensive practice may close only when:

- every substantive coverage cell has been sampled;
- the coverage ledger maps each question to its tested cell or cells;
- major doctrines have both direct and discriminating/comparative tests where appropriate;
- verified PYQ themes and common conceptual traps have been independently tested;
- no major closed-book recall gap remains;
- a representative fresh hard-MCQ set is strong;
- all high-confidence errors have been repaired;
- at least one novel transfer or application task succeeds; and
- additional questions would be substantively redundant.

Mastery requires later confirmation without recent rereading.

## Error codes

| Code | Meaning |
|---|---|
| `K-GAP` | Concept was not learned |
| `K-DECAY` | Previously learned but not retrievable |
| `CONF` | Confused related concepts |
| `EXC` | Missed an exception or proviso |
| `TIME` | Chronology or timeline error |
| `SCOPE` | Overgeneralized or misjudged scope |
| `CA-LINK` | Missed static-current linkage |
| `MISREAD` | Missed a qualifier or the question demand |
| `REASON` | Faulty inference |
| `ELIM` | Poor elimination |
| `GUESS-C` | Correct by guess |
| `HCW` | High-confidence wrong |
| `SOURCE` | Source or answer-key conflict |
| `TRANSFER` | Failed novel application |
| `MAINS` | Recognized the idea but could not produce it |

## Spaced retest cycle

| Stage | Task |
|---|---|
| Day 0 | Diagnostic recall, targeted revision, and initial hard MCQs |
| Day 1-2 | Error-focused recall and fresh remedial MCQs |
| Day 7 | Unseen hard MCQs and a closed-book topic outline |
| Day 21 | Interleaved practice with neighbouring topics |
| Day 45 | Cumulative Prelims set and one Mains task |
| Monthly | Mixed revision and weak-area repair |

A recurring serious error returns to the Day 1-2 stage.

## Subject guide requirements

Every `SUBJECT-GUIDE.md` must include:

- complete topic inventory in canonical order;
- prerequisites and topic relationships;
- recommended learning sequence;
- high-priority, difficult, and high-PYQ topics;
- revision and retest schedule;
- subject-specific MCQ traps;
- subject-specific Mains strategy;
- topic status and direct links to every canonical Markdown file and any explicitly generated PDF.

## Revision guide requirements

Every `REVISION-GUIDE.md` must preserve:

- syllabus boundary and topic roadmap;
- definitions and technical vocabulary;
- complete conceptual and causal flow;
- classifications and comparisons;
- chronology and timelines;
- laws, provisions, institutions, schemes, and mechanisms;
- exceptions, limitations, criticisms, and counterarguments;
- important examples and India-centric applications;
- verified PYQ demands;
- static-current linkages;
- UPSC traps;
- quick-glance register notes;
- recall prompts;
- text-renderable diagrams, tables, maps, and flowcharts.

The revision guide is a high-efficiency retrieval and repair layer. It must not become a shallow
substitute for the complete learning session.

## Answer-writing requirements

The global `ANSWER-WRITING-GUIDE.md` must explain:

- directive words and the demand of the question;
- 10-, 15-, and 20-mark structures;
- introductions, body organization, conclusions, headings, underlining, and diagrams;
- time allocation and gradual handwriting-endurance development;
- self-evaluation and model-answer comparison.

Every topic's `ANSWER-WRITING-TOOLKIT.md` must include:

- every verified PYQ routed to the topic through the latest available year, fully solved;
- syllabus demand and recurring PYQ themes;
- multiple valid introduction approaches;
- topic-specific high-value analytical lines;
- exact keywords and technical terminology;
- diagrams, frameworks, timelines, and answer spines;
- arguments, counterarguments, limitations, and balanced judgements;
- India-centric evidence and current examples where verified;
- way-forward points and conclusion approaches;
- original 10-, 15-, and 20-mark questions;
- complete model answer structures or solutions.

For verified PYQs, use complete model answers rather than answer structures alone. Model
structures without a developed answer are acceptable only for additional original drills that
are explicitly labelled as outline practice.

High-value lines must add conceptual precision, causal reasoning, balance, evidence, or a qualified
judgement. Do not use decorative quotations, generic filler, or promise that a memorized phrase
will guarantee marks.

## Writing-endurance progression

Writing practice must increase gradually and remain pain-free:

1. Oral recall and answer planning.
2. Short handwritten introductions, conclusions, and diagrams.
3. Five-minute answer skeletons.
4. One complete 10-mark answer.
5. One complete 15-mark answer.
6. Timed mixed-answer blocks.

Do not encourage writing through increasing pain, numbness, tingling, swelling, or weakness.

## Markdown-first and optional PDF requirements

- Markdown is the complete canonical learning source and must contain all substantive material.
- Do not generate, update, stage, or commit PDFs by default.
- Existing committed PDFs remain untouched unless the user explicitly requests regeneration or
  removal.
- When the user explicitly requests PDFs, generate separate revision, question, solution, and
  answer-writing artifacts. Question PDFs must contain no answers, hints, explanations, or visual
  answer clues; solution PDFs must preserve complete explanations.
- For explicitly requested PDFs, validate page order, clipping, overlap, blank pages, unsupported
  glyphs, internal links, and separation of questions from answers.

## Branch and push policy

- All work belongs on `feature/offline-revision-mcq-system`.
- The original active worktree and its uncommitted files remain untouched.
- Every concurrently active terminal or agent session must use its own Git branch and its own
  worktree. Two sessions must never write through the same worktree.
- Never switch, reset, clean, stash, merge, or rebase a worktree that is being used by another
  session. A session may commit and push only its own scoped changes to its own branch.
- Existing sessions are not automatically moved when this rule is introduced. Before starting
  new work, verify the current worktree and branch, and create a separate pair when either is
  already owned by another active session.
- Treat `origin/upsc-complete-repair` as the upstream content branch for this system.
- Do not continuously rebase this published feature branch. Rebasing would rewrite commit IDs and
  require force-pushing while other work may depend on the branch.
- Synchronize through explicit merge checkpoints:
  1. before inventorying a new subject;
  2. after the repair branch publishes relevant source updates;
  3. before final validation of a completed subject.
- At a synchronization checkpoint, first commit or otherwise obtain a clean offline worktree,
  fetch `origin`, and merge `origin/upsc-complete-repair` into this feature branch. Resolve only
  genuine conflicts in this worktree, rerun validation for affected topics, then commit and push
  the merge.
- Uncommitted work in the repair worktree cannot be synchronized. It becomes available only after
  the other session commits and pushes it to `origin/upsc-complete-repair`.
- Commit after each validated pilot or completed subject-sized milestone.
- Push each commit or safe commit batch to `origin/feature/offline-revision-mcq-system`.
- Never rewrite published history.
- Never merge into another branch without explicit user instruction.
- Keep every push comfortably below 2 GiB.
