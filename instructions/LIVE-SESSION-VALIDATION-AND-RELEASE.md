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
| Final learner package | checked | Exact Final-Learning-Packages learning-session path |
| Layered/complete session | checked | Exact path, or why not available/relevant |
| Solved workbook | checked | Exact Final-Learning-Packages workbook path |
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

Do not use learner-v2 artifacts for this workflow. The learner-facing reference is the
complete learning session and solved workbook under `notes\Final-Learning-Packages\`.

## Authoritative mechanical validator

Run:

```powershell
python tools\validate_live_session.py <topic-markdown>
```

It checks:

- continuous `## Lesson N` headings;
- lesson-bounded progress lines, pre-teach checklists and visuals;
- 2-4 concept-sensitive local MCQs with no constant, alternating or short repeating
  count pattern;
- exact answer labels, continuous numbering and A-B-C-D rotation;
- one correct and three incorrect option explanations per MCQ;
- unique incorrect explanations;
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

## Fail-fast release

After independent semantic review and after adding the verified index row, run a dry
preflight:

```powershell
python tools\release_live_session.py <topic-markdown> `
  --commit-title "<topic commit title>"
```

If it passes, execute:

```powershell
python tools\release_live_session.py <topic-markdown> `
  --commit-title "<topic commit title>" `
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
