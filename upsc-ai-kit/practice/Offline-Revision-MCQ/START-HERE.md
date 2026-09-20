# Offline Revision and MCQ System

This directory is the portable, Agency-independent study and practice system.
It must remain usable from the repository alone in Markdown and PDF form.

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
6. No skipping:
   - Cover every canonical topic and every substantive subtopic in the selected subject.
   - Cover definitions, classifications, mechanisms, chronology, institutions, laws, exceptions,
     comparisons, criticisms, examples, current linkages, PYQ demands, and application.
7. No compression:
   - Do not replace complete teaching or revision material with a generic short summary.
   - Preserve all substantive reasoning, distinctions, examples, diagrams, flow logic, traps,
     qualifications, and answer-writing value.
   - Remove only true duplication, chat noise, tool output, and navigation prompts.
8. Do not overwrite existing learner history. Generation must be deterministic and resumable.
9. Validate each pilot topic before generating the full subject.
10. Commit and push each validated subject or other coherent milestone to the isolated branch.
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
            |-- PRACTICE-LOG.md
            |-- ANSWER-WRITING-TOOLKIT.md
            |-- attempts\
            `-- pdf\
                |-- Revision-Guide.pdf
                |-- MCQ-Questions.pdf
                |-- MCQ-Solutions.pdf
                `-- Answer-Writing-Toolkit.pdf
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
- topic status and direct links to every file and PDF.

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

## PDF and offline requirements

- Markdown is the canonical editable source.
- Generate separate PDFs for revision, questions, solutions, and answer writing.
- Question PDFs must contain no answers, hints, explanations, or visual answer clues.
- Solution PDFs must preserve complete explanations.
- Validate page order, clipping, overlap, blank pages, unsupported glyphs, internal links, and
  separation of questions from answers.

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
