# Answer-Philosophy Alignment Review — Working Instructions

## Purpose and authority

Use this workflow to align the answer-writing approach in solved Mains papers with
[UPSC Mains Answer-Writing Philosophy](answer-writing-philosophy.md), then connect each solved
question to the relevant learning subtopic. This is a controlled, paper-by-paper process—not a
corpus-wide audit.

Apply the existing [Solved PYQ workspace instructions](INSTRUCTIONS.md) as well. If these
instructions and the workspace's source-fidelity, answer-quality, or review requirements appear to
conflict, preserve the official question and source integrity, follow the more restrictive scope
here, and record or raise the conflict rather than silently broadening work.

## User-controlled sequence

- Work **one year and one paper per pass**, in the exact year/paper the user selects.
- Do not start another year or paper, or continue a queue, until the user explicitly asks.
- If a paper or year is ambiguous, ask before reviewing it.
- A paper pass covers every answerable question and subpart in that one paper. Do not sample,
  skip, or mark the paper complete from a partial check.
- Do not launch a whole-year, whole-subject, or whole-corpus review.

## Files in scope

For a selected paper, edits may be made only to:

1. Its canonical paper file under `solved_pyqs/papers/<year>/`.
2. Directly relevant canonical knowledge `.md` owners under `upsc-ai-kit/knowledge/`, excluding
   all learning-session archive paths, including `learning-sessions/`, `learning-sessions/v2/`,
   `learning-session-v2/`, and migration aliases.
3. The directly relevant subtopic in the live-learning-session area (`live_sessions/`).
4. The required review entry in `solved_pyqs/REVIEW-LOG.md`.

The instruction file and `solved_pyqs/README.md` may be changed only to maintain or link this
workflow. Do not modify PDFs, generated exports, workbooks, unrelated papers, broad catalogues,
trackers, indexes, scripts, or other subjects/years. If an exact question-anchor or topic-route
change makes a catalogue/link update unavoidable, stop and ask before expanding scope.

## Procedure for each selected paper

### 1. Establish the paper and learning sources

- Read the paper file and account for every official question, selectable alternative, subpart,
  answer and stable anchor in its published order.
- Preserve the official wording, numbering, marks, word limit, section, paper order and source
  notes. Resolve wording or factual doubts against the paper's recorded primary source; do not
  guess or silently repair uncertain OCR.
- For each question, identify its narrowest existing canonical knowledge owner and the matching
  live-session lesson/subtopic. Read the relevant content before judging the answer.
- Search only within the allowed source locations. Do not use a similarly named archive or v2
  learning-session file as a substitute for the canonical owner or live session.
- If a required source, lesson or anchor cannot be located or verified, record the exact gap and
  ask for direction; do not invent, reconstruct, or mark the link complete.

### 2. Check every answer against the recommended philosophy

Use `answer-writing-philosophy.md` together with the actual question and paper instructions.
Assess each answer for:

- **Demand fidelity:** directive, scope, every clause, marks and word limit.
- **Paper fit:** the correct distinction between GS analysis, GS-IV ethical application, Philosophy
  Optional argument, essay development, or a language-paper task.
- **Direct response:** a clear thesis or action that answers the question rather than restating it.
- **Reasoning and evidence:** relevant, accurate named evidence/examples, with their significance
  explained. For analytical Mains and Philosophy answers, check the chain **claim → named
  evidence/example → analysis → qualification**, as appropriate to the demand.
- **Proportion and clarity:** coherent structure and concise expression without unsupported claims,
  padding, decorative name-dropping, forced balance, or generic formulae.
- **Conclusion or decision:** a close that resolves the demand; in case studies, a justified,
  implementable course of action with relevant safeguards.

Do not impose an identical structure on every paper or question. In particular, do not turn
Philosophy Optional answers into GS answers; do not require equal positive and negative arguments
where the prompt/evidence does not warrant them; and do not apply an essay structure to a bounded
language task.

### Current-affairs relevance

- First decide whether current affairs are part of the question's actual demand or materially
  strengthen its evidence. Do not force a dated policy/event update into a question that can be
  answered fully through its core concepts, mechanisms and constraints.
- If a current-affairs detail is incidental, unsupported or not needed to answer the demand, omit
  it rather than letting it distract from the core doctrine or block completion of the paper.
- Add a current-affairs example only when it is directly relevant, verified from a reliable source
  and accurately dated. Keep it subordinate to the core explanation; do not present it as
  foundational doctrine.

### 3. Make only necessary corrections

- Correct only a material mismatch with the recommended answer philosophy, a verified factual or
  attribution error, or a directly related clarity defect that prevents the answer from meeting the
  question's demand.
- Preserve sound substantive material, examples, terminology and argumentation. Do not compress,
  summarise, rewrite for style alone, remove repetition unless it is a concrete defect, or change
  correct answers merely to make them uniform.
- Never change the official question text to make the model answer easier to fit.
- If the recommended learning is absent from the relevant canonical owner or live-session
  subtopic, make **only the smallest edit needed to add that missing learning**. Preserve adjacent
  content and ordering. Do not create a new full learning session, restructure a session, add
  unrelated teaching, or regenerate its PDF/export.
- If learning already meets the recommendation, do not edit it. Link the solved question to the
  existing subtopic instead.

### 4. Link learning and solved answers

- Keep the existing paper-to-topic route and exact question anchor intact.
- Add a precise link from each relevant solved question to its existing canonical knowledge
  subtopic and the matching live-session subtopic, using repository-relative Markdown paths and a
  stable heading anchor where available.
- Add or correct the reciprocal link from the edited/linked learning subtopic to the exact solved
  paper question anchor, when that link is missing and can be added within the allowed source file.
- Link at subtopic/question level, not merely to a broad folder or the top of a paper.
- Do not duplicate the full solved answer in a learning file. Do not alter unrelated links or
  topic classifications.

### 5. Review, account and stop

- Re-read the applicable sections of `INSTRUCTIONS.md` after the pass and perform its mandatory
  post-pass review on the changed scope: completeness, source/answer accuracy, demand fidelity,
  depth, proportionality, classification, bidirectional link integrity, duplication, language and
  coverage accounting.
- Check that every answerable unit in the selected paper was reviewed exactly once and that all
  new local Markdown links and anchors resolve.
- Fix in-scope defects found by that review before recording completion. Do not broaden into
  unrelated issues.
- Add a dated `REVIEW-LOG.md` entry naming the selected year/paper, files reviewed and changed,
  per-paper coverage checked, corrections made, source/learning links checked, remaining blockers,
  and `PASS` or `BLOCKED`.
- Do not change global corpus counts or release status for answer-only improvements. Update a
  catalogue or coverage artifact only if a permitted, necessary route/count change actually
  affects it; if doing so would exceed the scope above, stop and ask first.
- Report the exact repository-relative paths changed and any unresolved point. Stop after that
  paper and wait for the user's next year/paper instruction.

## Explicit prohibitions

- No full review, batch processing, or automatic advancement to another paper.
- No skipping questions, optional alternatives, subparts, or weak answers in the selected paper.
- No compression, wholesale rewriting, generic templating, or stylistic homogenisation.
- No edits to learning-session archives, learner-v2 files, generated learning PDFs, or unrelated
  source material.
- No inferred wording, attribution, evidence, or source links presented as verified.
