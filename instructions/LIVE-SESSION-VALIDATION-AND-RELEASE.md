# Live-Session Validation and Release

## Purpose

Use one mechanical validator and one fail-fast release command for every new or
repaired live-session topic. These tools improve speed and consistency without
reducing any learner-first, coverage, source, semantic-review or release requirement.

The controller must still independently review:

- learner sequencing and teaching quality;
- canonical, advanced and book completeness;
- doctrine, examples, objections, replies and residuals;
- every MCQ key, distractor and explanation;
- every PYQ's wording, ownership, demand and approach;
- original Mains questions and model answers;
- source reliability and fact/inference typing.

Before independent review, the generation or repair writer must complete the
`Mandatory Pre-Handoff Hostile Self-Audit` defined in
`live_sessions\LIVE-SESSION-GENERATION-RULES.md`. The handoff is invalid without a
fresh exact hash and reported coverage, MCQ-cue, model-answer, PYQ, source and
formatting results. Any subsequent edit invalidates that self-audit and requires a new
one.

## Learner-first pass preamble

Every generation and repair instruction must explicitly state:

> Preserve or improve the accepted learner-first teaching standard: dependency-led
> sequencing, visual-first explanation, plain-language intuition before terminology,
> full doctrine and argument, examples with limits, strongest objection and reply,
> UPSC application, misconception-driven practice and remediation. Do not skip,
> compress or replace teaching with summaries or source metadata.

This preamble is mandatory even when the lane has already read the governing rules.

## Source-manifest gate

Every new or repaired topic must contain this H2 section inside its final
`# SOURCE LEDGER`:

```markdown
## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical Markdown | checked | Exact path and material audited |
| Final learner package | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule |
| Layered/complete session | checked | Exact path, or why not available/relevant |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule |
| Advanced dossier | checked | Exact path/section, or why not available/relevant |
| OCR books | checked | Exact book/pages, or why not available/relevant |
| PYQs through 2026 | checked | Exact ledger and official/provisional control |
| Official live sources | checked | Exact sources, or why not relevant |
```

Allowed statuses are exactly:

- `checked`
- `not available`
- `not relevant`

Every row requires concrete evidence or a reason. A missing row, unsupported status or
empty reason blocks release.

For all live-session work, do not read, search, cite, compare against or derive any
finding from any artifact under `notes\Final-Learning-Packages\`. This includes its
learning sessions, solved workbooks, ASCII and graphical flowcharts, package reviews,
indexes and validation artifacts. The exclusion applies during source discovery,
generation, repair, independent semantic review, validation and release. Existing
files remain untouched for possible future use under a separately approved workflow.

Do not use learner-v2 artifacts for this workflow either.

Relevant artifacts under `learning_package_final\` may be consulted only when needed
as optional bounded checks for completeness, learner sequencing, practice or
remediation. Their use is not required for validation or release, and they cannot
override canonical Markdown, verified PYQs, books or official evidence.

## Authoritative mechanical validator

Run:

```powershell
python tools\validate_live_session.py <topic-markdown>
```

It checks:

- continuous `## Lesson N` headings;
- lesson-bounded progress lines, pre-teach checklists and visuals;
- for every newly generated topic, exactly one concept check, model answer and
  misconception note in every lesson, with no compiled MCQ corpus;
- only for existing released or explicitly preserved pre-rule legacy artifacts, the
  existing local-MCQ count, numbering, answer and explanation checks;
- exact final H1 arc;
- prohibited wording and package-language leakage;
- balanced fences, trailing whitespace and final newline;
- the source-manifest gate;
- repository-standard word count, line count and SHA-256;
- scoped `git diff --check`.

For a legacy released file that predates the source manifest, audit only with:

```powershell
python tools\validate_live_session.py <topic-markdown> --allow-missing-source-manifest
```

That compatibility flag is forbidden for new or repaired releases.

For an already-generated live-session draft that predates the answer-separation rule
approved on 28 September 2026, retain its existing keyed MCQ headings only when the user
has explicitly chosen not to retrofit earlier History or Philosophy sessions:

```powershell
python tools\validate_live_session.py <topic-markdown> `
  --allow-legacy-keyed-mcq-headings
```

This exception applies only to explicitly preserved pre-rule artifacts. It must not be
used for any newly generated session, regardless of subject or topic number.

## Fail-fast release

After independent semantic review and after adding the verified index row, run a dry
preflight:

```powershell
python tools\release_live_session.py <topic-markdown> `
  --commit-title "<topic commit title>" `
  [--allow-legacy-keyed-mcq-headings]
```

If it passes, execute:

```powershell
python tools\release_live_session.py <topic-markdown> `
  --commit-title "<topic commit title>" `
  [--allow-legacy-keyed-mcq-headings] `
  --execute
```

The release command:

1. reruns the authoritative validator without the legacy exception;
2. verifies the index contains exactly one topic link, current word count and current
   12-character hash;
3. requires an empty staging area;
4. runs scoped whitespace checks;
5. stages exactly the topic and `live_sessions\INDEX.md`;
6. runs cached whitespace checks;
7. commits with the required trailers;
8. pushes the current branch;
9. fetches and requires remote parity `0/0`;
10. stops immediately on any failure.

The script does not create or alter the index row, decide semantic completeness, repair
content or bypass sequential syllabus release order.
