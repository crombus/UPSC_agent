# Solved PYQs: Permanent Working Instructions

## 1. Objective

Build a paper-wise, examiner-grade solved PYQ library inside this folder with two coverage tiers:

- Complete corpus, 2019-2026: all eleven instructed paper families.
- Historical merit expansion, 2013-2018: Prelims GS-I, CSAT, Essay, GS-I to GS-IV, and
  Philosophy Optional Papers I and II.

The library must support both:

- Paper-wise study: year -> stage -> paper -> question -> solution.
- Topic-wise study: subject -> topic -> subtopic -> every linked PYQ across years and papers.

All navigation must use repository-relative GitHub Markdown links. Every paper question must link
to its topic route, and every topic catalogue must link back to the exact solved question.

## 2. Included Papers

The complete 2019-2026 corpus covers:

- Prelims General Studies Paper I.
- Prelims CSAT Paper II.
- Mains Qualifying Indian Language: Hindi.
- Mains Qualifying English.
- Mains Essay.
- Mains General Studies I.
- Mains General Studies II.
- Mains General Studies III.
- Mains General Studies IV.
- Philosophy Optional Paper I.
- Philosophy Optional Paper II.

The 2013-2018 historical expansion covers the same list except Mains Qualifying Hindi and
English. This creates nine merit paper families per historical year.

Never invent a missing paper or silently substitute a mock paper for an official PYQ. Reuse held
verified sources instead of downloading duplicates. Record direct official, archived-official,
and fallback-mirror provenance distinctly.

## 3. Source Priority and Fidelity

Use sources in this order:

1. Official or repository-held question papers and answer keys.
2. Existing verified PYQ ledgers and routing files.
3. Existing premium solved workbooks and canonical knowledge Markdown.
4. OCR-searchable local books for deeper static evidence.
5. Authoritative government, constitutional, judicial, institutional, or primary sources.
6. Reputable secondary sources only when primary material does not settle the issue.

Preserve the official question number, wording, marks, word limit, section, and paper order.
Clearly flag uncertain OCR instead of silently repairing it. Record the source file used for each
paper. Never fabricate an official answer key, fact, quotation, case, scholar, date, statistic,
translation, or source.

## 4. Folder and File Design

The final structure should follow this pattern:

```text
solved_pyqs/
  README.md
  AGENTS.md
  INSTRUCTIONS.md
  STATUS.md
  REVIEW-LOG.md
  catalogue/
    PAPERWISE-INDEX.md
    SUBJECT-INDEX.md
    TOPIC-INDEX.md
    YEARS-INDEX.md
  papers/
    <year>/
      prelims-gs1.md
      prelims-csat.md
      mains-hindi.md
      mains-english.md
      mains-essay.md
      mains-gs1.md
      mains-gs2.md
      mains-gs3.md
      mains-gs4.md
      philosophy-paper-1.md
      philosophy-paper-2.md
  topics/
    <subject>/
      <topic>.md
```

Create only files supported by available papers. Keep filenames stable, lowercase, descriptive,
and GitHub-safe. Do not duplicate the same full solution in topic files: topic catalogues should
contain concise question metadata and links to the canonical paper-wise solution.

## 5. Stable Question Identity and Linking

Assign every question a stable ID:

```text
<year>-<paper-key>-q<question-number>
```

Examples:

- `2025-prelims-gs1-q17`
- `2024-mains-gs2-q08`
- `2023-philosophy-p1-q3a`

Use that ID as the Markdown heading anchor or an explicit HTML anchor when GitHub's generated
anchor may be unstable. Each solved question must display:

- Year, stage, paper, section, and official question number.
- Marks and word limit where applicable.
- Primary subject, topic, and subtopic.
- Secondary or interdisciplinary topic links where genuinely relevant.
- Difficulty and question-demand tags.
- Relative links to all applicable topic catalogue pages.
- A backlink to the paper-wise catalogue.

Topic pages must link directly to the exact question anchor, not merely to the top of a paper.

## 6. Common Solution Standard

Every solution must be independently useful, accurate, and exam-oriented. It must include:

1. Exact question or verified transcription.
2. Demand decoding: directive, scope, hidden dimensions, and likely traps.
3. Correct answer or defensible thesis.
4. Step-by-step reasoning appropriate to the paper.
5. Named evidence: constitutional provisions, cases, committees, reports, thinkers, texts,
   examples, data, maps, calculations, or official concepts as relevant.
6. Analysis and qualification, not a list of generic points.
7. A concise examiner takeaway explaining why the answer earns marks.
8. Subject -> topic -> subtopic classification.

For Mains and Philosophy, follow:

```text
claim -> named evidence/example -> analysis -> qualification
```

Respect the directive and word limit. Prefer a focused, balanced, complete answer over decorative
language. Introductions and conclusions must answer the specific demand rather than repeat a
memorised template.

## 7. Paper-Specific Standards

### Prelims GS I

- State the correct option and its verification status.
- Evaluate every statement and, where useful, every option.
- Explain why the correct choice is correct and why close alternatives fail.
- Add elimination logic, but never use an unreliable trick as proof.
- Identify factual, conceptual, current-affairs, and close-option traps.
- Link each question to the most precise static topic possible.

### CSAT

- Show the complete reasoning or calculation.
- Provide the shortest safe exam method after the full method.
- State assumptions, units, intermediate values, and option checks.
- For comprehension, justify the answer strictly from the passage.
- For reasoning, explain why competing options fail.
- Flag questions affected by ambiguous wording or multiple interpretations.

### Mains GS I-IV

- Decode the directive and all dimensions before answering.
- Match depth and structure to marks and word limit.
- Use precise headings, arguments, named evidence, India-centric examples, and qualifications.
- Include diagrams, tables, stakeholder maps, ethical matrices, or flow structures only when
  they improve the answer.
- GS IV case studies must identify stakeholders, values, conflicts, options, consequences, and a
  justified course of action.

### Essay

- Treat every official topic as a separate PYQ.
- Explain topic interpretation, central thesis, and possible misreadings.
- Provide a coherent outline with logical transitions and multidimensional coverage.
- Provide an examiner-grade model essay or a complete model-answer treatment at the agreed depth.
- Use relevant examples without turning the essay into a GS fact list.
- Preserve philosophical depth, counter-view, synthesis, and a strong conclusion.

### Qualifying Hindi and English

- Follow the exact section type: comprehension, precis, grammar, vocabulary, translation, or
  essay.
- Preserve language correctness and the paper's requested format.
- For translation, retain meaning, tone, register, and technical sense rather than translating
  mechanically.
- For precis, state the compression logic and supply a suitable title.
- Clearly mark answers where more than one phrasing can be valid.

### Philosophy Optional Papers I and II

- Use English-first terminology followed by accurate Sanskrit or Pali IAST where relevant.
- Decode the philosophical problem, thesis, arguments, objections, replies, and evaluation.
- Attribute doctrines accurately to thinkers and primary texts where support exists.
- Distinguish exposition, comparison, criticism, and independent assessment.
- Avoid generic GS-style answers; show conceptual precision and philosophical argument.
- Connect each PYQ to the exact syllabus unit, school, thinker, doctrine, and subproblem.

## 8. Topic Taxonomy

Classify by the narrowest defensible route:

```text
Paper area -> Subject -> Topic -> Subtopic
```

Allow secondary tags for genuinely cross-cutting questions, but designate exactly one primary
route. Do not create near-duplicate topic names. Reuse the repository's canonical subject and
topic naming wherever available.

The catalogue must support concentration analysis, including:

- Number of questions by subject, topic, subtopic, year, and paper.
- Marks concentration for Mains and Philosophy.
- Question-count concentration for Prelims and CSAT.
- Recurring themes and gaps across the selected years.

Counts must be generated from completed question metadata, not estimated manually.

## 9. Pass-Based Workflow

Process work in explicit passes:

1. Inventory pass: locate papers, identify years, detect missing or duplicate sources.
2. Transcription pass: preserve official order and wording.
3. Classification pass: assign stable IDs and topic routes.
4. Solution pass: write paper-appropriate solutions.
5. Evidence pass: verify facts, keys, citations, calculations, and philosophical attribution.
6. Linking pass: create paper-wise and topic-wise bidirectional GitHub links.
7. Quality pass: apply the mandatory review below.
8. Release pass: update status, metrics, catalogues, and review log.

Do not mark a later pass complete when an earlier pass has unresolved defects.

## 10. Mandatory Review After Every Pass

After every pass, re-read this file and review the changed scope for:

- Completeness: every source question is present once and in official order.
- Accuracy: wording, answer, calculation, facts, dates, articles, cases, thinkers, and texts.
- Demand fidelity: the solution answers the exact directive and all parts.
- Depth: evidence and analysis are sufficient for examiner-grade quality.
- Proportionality: solution length and structure match the marks and paper type.
- Classification: primary and secondary routes are precise and consistent.
- Link integrity: forward links, backlinks, and exact question anchors work on GitHub.
- Duplication: one canonical solution exists; catalogues link rather than copy.
- Language quality: clear English or Hindi, correct terminology, no broken OCR residue.
- Integrity: no unsupported certainty, invented official key, or fabricated evidence.
- Coverage accounting: paper and topic counts reconcile exactly.

Fix detected defects in the same pass. Then update `REVIEW-LOG.md` with:

- Date.
- Pass type and scope.
- Files reviewed.
- Defects found and corrected.
- Remaining blockers.
- Reviewer conclusion: `PASS` or `BLOCKED`.

A pass cannot be recorded as `PASS` while a known material defect remains.

## 11. Completion Criteria

A paper is complete only when:

- All questions have verified transcriptions and stable IDs.
- All questions have high-quality solutions appropriate to the paper.
- All questions have primary topic routes.
- Paper-wise and topic-wise links are bidirectional and valid.
- Counts reconcile with the source paper.
- The mandatory review is recorded as `PASS`.

The overall library is complete only when all in-scope papers in both coverage tiers meet these
criteria and the catalogues permit reliable paper-wise, topic-wise, and concentration-based study.

## 12. Definitive Release Audit Baseline

The released 2013–2026 baseline is:

- 2019–2026: eleven papers per year, including qualifying Hindi and English.
- 2013–2018: nine merit papers per year; qualifying Hindi and English are intentionally not
  expected.
- 142 paper files, 142 paper reviews, 5,381 answerable units, 5,565 routed anchors, 6,046 explicit
  anchors, 357 canonical topic pages and 48,800 represented Mains/Philosophy marks.

Run `python solved_pyqs/build_release_catalogue.py --idempotence` for a definitive release audit.
It must finish `PASS`, report no second-pass changes, validate every relative Markdown file/anchor
link, and verify all 65 records in
`books/previous_papers_2013_2018/SOURCE-VALIDATION.json` against their local SHA-256 hashes.
Preserve the 2026 provisional keys and GS-I Q64 dropped (`X`) semantics until authenticated
official-final keys are available.
