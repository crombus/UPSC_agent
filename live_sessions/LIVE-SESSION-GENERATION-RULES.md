# Live-Session Generation Rules

## Purpose

Generate complete learner-first Markdown sessions that preserve the depth of the
canonical knowledge package while using the clarity, sequencing and visual teaching
style of an interactive live session.

These sessions are not short notes, revision summaries or compressed substitutes for
the source material. They are complete teaching editions.

## Single Source of Truth

This file is the **only authoritative workflow and presentation contract** for every
UPSC live learning session in this repository:

```text
live_sessions\LIVE-SESSION-GENERATION-RULES.md
```

The repository-wide optimization and integrity policy is stored at:

```text
instructions\GENERATION-OPTIMIZATION-AND-INTEGRITY.md
```

It governs execution efficiency around this contract but cannot replace, reduce or
override any requirement in this file.

Canonical knowledge files, books, PYQ ledgers, previous live editions, layered
packages, solved workbooks, checkpoints and conversation summaries supply content,
evidence or continuity only. They must never introduce, replace or override the
workflow, lesson structure, interaction pattern, roadmap rules or practice sequence
defined here.

Mandatory use:

1. Read this entire file before auditing or proposing the roadmap for every new topic.
2. Read it again after any context reset, summary handoff or resumed session.
3. Before responding to `Start` or `Next`, verify the response against the Start,
   Generation and Navigation Lock, Structural Format Lock and Required Lesson Structure
   in this file.
4. Derive the roadmap from the audited learning dependencies, not from the lesson or
   layer count of an existing package.
5. If any other artifact conflicts with this file, this file wins. Do not blend the two
   workflows or improvise a hybrid structure.
6. If a needed rule is missing or ambiguous, update this file first, then continue.
7. Record newly approved durable instructions in the central `instructions\` registry
   and update this file whenever they affect live-session behaviour.
8. After every generation or repair pass, reread `instructions\README.md`,
   `instructions\GENERATION-OPTIMIZATION-AND-INTEGRITY.md` and this entire file before
   beginning the independent validation or release gate. Do not rely on retained
   context, summaries or an agent's reported validation as a substitute.
9. Before every generation or repair pass, explicitly restate the learner-first lock
   in the pass instruction: preserve or improve learner sequencing, visual-first
   explanation, plain-language intuition, technical depth, examples, objections,
   replies, practice and remediation. Do not rely on a generic "follow the rules"
   reference.
10. Use `tools\validate_live_session.py` before every generation-lane handoff and again
    during independent controller validation. Use
    `tools\release_live_session.py` only after semantic review and index preparation.
    Mechanical automation never replaces semantic review.
11. Before every generation or repair pass, read the learner-facing opening and at
    least one complete lesson from both:
    `live_sessions\Philosophy-Optional\01-Nyaya-Vaisesika\Learning-Session-Live-Edition.md`
    and
    `live_sessions\Philosophy-Optional\07-Mimamsa\Learning-Session-Live-Edition.md`.
    Use their integrated terminal-teaching flow as the primary style check:
    roadmap-led sequencing, pre-teach checklist, visible progress, visual-first
    intuition, numbered explanation, comparison or distinction, qualification, exam
    linkage, mini recap, revision notes and adaptive misconception-driven mastery
    practice. This check is mandatory for every subject and every pass, including
    History. It does not permit copying Nyaya-Vaisesika or Mimamsa doctrine, wording
    or fixed lesson length into another topic.

## Nyaya-Vaisesika, Mimamsa, Vedanta and Economy Reference-Session Fidelity Lock

The required learner-facing standard is the teaching architecture demonstrated by:

```text
live_sessions\Philosophy-Optional\01-Nyaya-Vaisesika\Learning-Session-Live-Edition.md
live_sessions\Philosophy-Optional\07-Mimamsa\Learning-Session-Live-Edition.md
live_sessions\Philosophy-Optional\08-Vedanta\Learning-Session-Live-Edition.md
live_sessions\Economy\<completed topic>\Learning-Session-Live-Edition.md
```

These files are structural and pedagogical benchmarks, not independent rulebooks.
This file remains the single source of truth. Nyaya-Vaisesika and Mimamsa are the
mandatory primary style references before every pass; Vedanta and the completed
Economy sessions provide additional subject-specific calibration. When a future
session does not feel like these learner-first sessions, repair the rules here before
repairing the topic.

The defining benchmark is **content-led progression**. The learner's question and the
topic's internal logic must control the lesson:

```text
learner's problem
  -> visual or intuitive model
  -> plain-language explanation
  -> exact doctrine or mechanism
  -> complete derivation or process
  -> example
  -> rival view, near-neighbour or predictable confusion
  -> criticism, limitation or trap
  -> reply, resolution or qualified verdict
  -> UPSC use
  -> revision
  -> misconception-driven practice
```

For Indian and Western philosophy, preserve the Vedanta teaching rhythm:

```text
philosophical puzzle
  -> technical vocabulary
  -> doctrine
  -> supporting argument
  -> purvapaksa or strongest objection
  -> reply
  -> unresolved residual or balanced assessment
  -> wider philosophical consequence
  -> PYQ and answer-writing use
```

For Economy and other process-heavy subjects, preserve the Economy teaching rhythm:

```text
practical problem
  -> transaction, causal flow or mechanism
  -> technical classification
  -> numerical or India-centric example
  -> near-neighbour distinction
  -> limitation, risk or policy trade-off
  -> current-affairs anchor where genuine
  -> UPSC trap and application
```

Apply these rules exactly:

1. Begin each lesson with the actual learner-facing problem, not with source ownership,
   evidence classification, package status or validation metadata.
2. Let lesson form and length vary with the concept. Use internal Parts when a concept
   needs several dependent movements. Do not force every lesson into the same number of
   headings, visuals, questions or words.
3. Introduce technical terms only after establishing the idea they name. Translate and
   define each term on first use, then show what philosophical or practical work it
   performs.
4. Make examples carry the reasoning. After every analogy, numerical example or
   thought experiment, explain what it establishes and where it stops applying.
5. Build causal transitions between lessons. End by showing why the next problem
   arises from the present lesson; do not merely close one module and start another.
6. Treat comparisons as arguments. Explain why the thinkers, schools, institutions or
   instruments differ and which prior commitment produces the difference.
7. Make practice local and misconception-driven. Use the number and type of conceptual,
   applied and remedial questions required by the lesson; do not impose an identical
   question quota on every lesson.
8. Place exam coaching after understanding. Marks, directives, answer spines and PYQ
   routes must arise from the taught doctrine or mechanism, not dominate the teaching
   voice.
9. Preserve a teacherly prose cadence: short conceptual moves, genuine questions,
   direct explanations, contrast, qualification and retrieval prompts. Avoid
   encyclopedic blocks and production-report prose.
10. Use doubt or misconception blocks where they clarify a predictable learner error.
    In a compiled edition, do not fabricate a learner's actual answer; state the likely
    doubt and resolve it transparently.
11. Repeat a concept only when its function changes from first teaching to comparison,
    application, criticism or revision. Do not repeat the same doctrine at the same
    level merely because separate source dossiers contained it.
12. Keep internal generation and validation machinery invisible in learner-facing
    lessons.

The following expressions and artifacts are prohibited inside learner-facing teaching
unless the term itself is the subject being taught:

- `layered lesson`, `layered opening map` or `five-layer package`;
- `solved workbook MCQs` or other source-workbook references;
- `canonical section ownership`, `sole ownership`, `printed ownership` or
  `ownership firewall`;
- `evidence dossier`, `restored doctrine dossier` or `corpus signal`;
- `mechanical audit`, completion-count narration or validation-pass claims;
- source-routing instructions, generation notes or package assembly language;
- repeated statements about the roadmap being frozen;
- visible references to which source file supplied a particular learner-facing
  paragraph.

Verified PYQ year/question linkage, directive analysis, demand and answer approach
remain locally integrated in the lesson that teaches them. Do not include solved PYQ
model answers in the live-session file and do not create a new solved-PYQ workbook;
the learner already maintains a separate solved workbook. Internal provenance labels,
source-ownership mapping, coverage evidence and validation counts remain mandatory,
but they belong only in the final coverage/source ledgers or in internal generation
records. Convert any necessary boundary or attribution into ordinary teaching
language inside the lesson.

### Natural variation lock

Shared sequence does not mean identical shells:

- choose a flowchart only for a process or argument;
- choose a table only for a genuine classification or comparison;
- use a thought experiment when the doctrine depends on conceptual possibility;
- use a numerical example when quantities or incentives matter;
- use an objection-reply exchange when disagreement drives understanding;
- use internal Parts when one accepted lesson contains several dependent arguments;
- vary practice volume according to difficulty and predictable errors;
- omit decorative headings that add no learning function.

A file fails this lock if multiple lessons could exchange their internal headings,
question counts and transition sentences without any meaningful change. Structural
regularity must support retrieval, not reveal a generator template.

### Reference-style final arc

After the complete lesson sequence, consolidate in this learner-facing order:

```text
verified PYQ linkage and answer approaches
  -> original cumulative MCQs with explanations
  -> original 10-, 15- and 20-mark Mains practice with model answers
  -> common-error remediation
  -> master comparisons, causal chains or argument maps
  -> complete consolidated register notes
  -> final coverage matrix
  -> source and verification ledger
```

Merge or omit a separate final block when it merely repeats an immediately preceding
block. The final arc must change the learner's task from understanding to application
to retrieval; it must not reproduce the same teaching three times under different
package labels.

## Output Location

Save each generated live session under:

```text
live_sessions\<Subject>\<Topic>\
```

Recommended files:

```text
Learning-Session-Live-Edition.md
Coverage-Matrix.md
```

Do not overwrite an existing canonical knowledge file or generated learning package.

## Source Priority

Use sources in this order:

1. Canonical Markdown knowledge file for the topic.
2. The exact complete learning-session and solved-practice artifacts under
   `notes\Final-Learning-Packages\` for learner sequencing, visual teaching,
   completeness, practice and remediation.
3. Verified UPSC PYQ ledgers and question papers through 2026.
4. Relevant layered/complete sessions and advanced dossiers as bounded completeness
   checks.
5. OCR-searchable local books and source PDFs.
6. Official or otherwise reliable live sources where current linkage is relevant.
7. Qdrant only as an optional fallback.

Do not use learner-v2 artifacts for this live-session workflow. Final-Learning-Packages
is the learner-session and solved-workbook reference.

If sources disagree, preserve the canonical distinction, verify the disputed point and
state the qualification. Never silently choose a convenient formulation.

## Coverage Lock

Before drafting, create a concept inventory from all relevant sources.

Every substantive concept must be mapped to at least one of:

- dedicated lesson;
- lesson subsection;
- definition;
- visual or comparison;
- argument or derivation;
- example or analogy;
- criticism and reply;
- inter-school comparison;
- UPSC trap;
- PYQ application;
- revision note;
- MCQ or Mains practice question.

Nothing may disappear because it is difficult, technical, advanced, repetitive in
appearance or inconvenient for the planned lesson count.

The final document must include a coverage table identifying where every canonical
concept and every relevant PYQ appears.

It must also include the exact `## SOURCE-MANIFEST GATE` table defined in
`instructions\LIVE-SESSION-VALIDATION-AND-RELEASE.md`. Every required source category
must be marked `checked`, `not available` or `not relevant`, with concrete evidence or
a reason. A missing category blocks release.

## No-Skipping and No-Compression Rules

**Absolute lock:** no live-session generation, reconstruction, repair or batch rebuild
may skip, compress, weaken or replace any required teaching merely to reduce time,
document length, lesson count, context use or workload. This applies equally to basic
content, advanced refinements, technical arguments, examples, qualifications,
comparisons, criticisms, replies, unresolved residuals, PYQ linkages, traps, original
practice and remediation.

For every accepted learner-facing lesson, verify completeness independently. A complete
topic-level summary, a long final document or strong coverage in another lesson cannot
compensate for a compressed or incomplete lesson. When a concept is too large for one
continuous treatment, preserve the accepted lesson boundary and teach it through
internal Parts rather than summarising, postponing or deleting material.

Batch scale never changes this standard. When several topics are rebuilt together,
perform the full source, syllabus, PYQ and lesson-level gap audit separately for every
topic. Never copy a generic completeness decision from one topic to another.

1. Do not replace a substantive explanation with a one-line summary.
2. Do not merge distinct doctrines merely to reduce document length.
3. Do not remove definitions, causal steps, qualifications, examples, objections,
   replies or rival positions.
4. Do not omit a concept because it belongs to an advanced or enrichment section.
5. Do not treat a diagram or table as a replacement for full teaching prose.
6. Do not reduce a comparison to labels without explaining the reason for each
   position.
7. Do not state a criticism without the strongest available reply.
8. Do not force a large concept into an overcrowded lesson. Split it into Part A and
   Part B where needed.
9. Remove only tool logs, navigation chatter, accidental duplication and repetition
   that contributes no additional understanding.
10. An updated edition must retain or improve the depth of the previous edition.

## Controlled Two-Lane Parallel Generation Protocol

Parallel execution is an additional scheduling mechanism, not a reduced workflow.
It must produce the same topic-level result as strict sequential generation. Every
coverage, roadmap, teaching, PYQ, practice, validation and no-compression requirement
in this file remains independently binding inside each lane.

Use at most **two concurrent topic-generation lanes**. Each lane must be isolated by:

1. one topic and its frozen learner-facing roadmap;
2. its own complete syllabus, canonical, advanced, book and PYQ preflight;
3. its own gap ledger and per-lesson evidence mapping;
4. its own whole-topic Markdown file;
5. its own lesson-level completeness, semantic-practice and structural validation;
6. a prohibition on editing this rules file, the shared index, another topic or Git
   history.

Read-only source research and preflight audits may run concurrently. Actual generation
may also run concurrently only under the two-lane isolation above. Never let a summary,
coverage decision, validator result or apparent completeness from one lane substitute
for evidence in the other lane.

### Sequential release gate

Parallel generation does not permit parallel release. Release topics strictly in
approved syllabus order:

```text
independent controller audit
  -> repair every frozen defect
  -> repeat the complete release gate
  -> update the shared index
  -> stage only the topic and index
  -> commit the topic separately
  -> push and verify remote parity
  -> release the next topic
```

A later topic may finish drafting while an earlier topic is under review, but it must
wait. It cannot update the index, be committed or be pushed before every earlier topic
in the approved order has passed its own release gate.

The independent controller must verify, for each topic:

- the frozen roadmap, progress markers and pre-teach checks;
- full syllabus, basic, advanced, book and PYQ coverage;
- natural lesson variation and learner-first teaching;
- exact links-only PYQ treatment without solved-answer leakage;
- every MCQ key semantically, every distractor and all option explanations;
- original Mains practice and complete model answers;
- the required final-section order, Markdown integrity and clean scoped diff;
- final word count, hash and index entry.

### Tiered integrity hard stop

Integrity takes priority over throughput.

**Topic-lane quarantine:** stop and reject the affected topic when a defect is confined
to that lane, including a missing concept, compressed lesson, incorrect PYQ, false or
ambiguous MCQ key, generic explanation, roadmap drift, package-language leak or failed
structural check. Freeze a defect ledger, repair the topic surgically and repeat the
full release gate. The other isolated lane may finish drafting, but strict syllabus
release order still applies.

**Global hard stop:** pause both lanes and start no new generation when any defect is
systemic, including:

- cross-topic content, roadmap or source contamination;
- concurrent editing of the shared index, rules or Git history;
- evidence that one lane reused another lane's coverage decision;
- an unreliable validator or a validation method that misses substantive defects;
- source conflicts that affect more than one topic;
- skipped, compressed or weakened content attributable to concurrency;
- any measurable decline from the accepted Vedanta-Economy reference standard.

Resume parallel generation only after the systemic cause is corrected and both active
topics are rechecked against this entire file. If the same systemic failure recurs,
disable parallel generation and return to strict sequential generation.

The first use of this protocol is a two-topic pilot. After both topics are separately
validated, committed and pushed, compare their defect rate and teaching integrity with
the accepted sequential rebuilds before applying the protocol to another pair.

## Learner-First Teaching Order

Teach in dependency order rather than merely copying source order:

```text
intuition
  -> plain-language definition
  -> visual model
  -> technical terminology
  -> full doctrine or mechanism
  -> argument and presuppositions
  -> examples
  -> comparison
  -> criticism and reply
  -> UPSC application
  -> revision
  -> practice
```

Do not introduce several unfamiliar technical terms before establishing the underlying
idea.

## Dynamic Lesson Count

The number of lessons or subtopics is never fixed at 12. Determine it separately for
each topic from:

- the complete UPSC syllabus demand;
- the number and dependency of distinct concepts;
- doctrine, argument, criticism and comparison requirements;
- relevant PYQs through 2026;
- the amount of practice and remediation needed for mastery.

Use as many lessons as necessary for complete, understandable coverage. A narrow topic
may need fewer lessons; a broad or technically dense topic may need substantially more.
Never merge, omit or compress content merely to meet a predetermined lesson count.
Finalize the roadmap only after completing the canonical coverage and PYQ audit.

## Roadmap Freeze and Coverage Integration

Dynamic lesson count applies only while the roadmap is being designed. Once a roadmap
has been presented and accepted, its learner-facing lesson count, order and boundaries
are frozen.

Keep these three structures distinct:

1. **Coverage units** — sections, doctrines, arguments and PYQs found in the sources.
2. **Learner-facing lessons** — the accepted roadmap used for progress tracking.
3. **Internal parts** — Part A, Part B or named subsections used when one accepted
   lesson contains substantial material.

There is no requirement that one coverage unit must become one lesson. Additional
coverage discovered during drafting must normally be integrated into the appropriate
accepted lesson as an internal part, without skipping or compression.

After roadmap acceptance, change the lesson count only when genuinely new material
cannot be placed coherently within the accepted structure. Before making such a change:

- explain why the existing roadmap is insufficient;
- show the old-to-new lesson mapping;
- identify the newly discovered independent learning dependency; and
- obtain explicit learner approval.

When reconstructing or exporting an existing live learning session, preserve its
original roadmap exactly. A source file's chapter or section count must never replace
the accepted live-session roadmap.

## Mandatory Gap Audit Before Drafting

Never assume that an existing learning package, canonical summary or generated session
is complete merely because it is long or labelled "complete."

Before drafting every live learning session, cross-check:

1. the verbatim UPSC syllabus terms;
2. all relevant basic and advanced canonical knowledge files;
3. existing complete, layered and solved-practice packages;
4. verified PYQs through the latest available year;
5. OCR-searchable local books for deeper evidence and standard formulations;
6. relevant inter-school or inter-topic comparisons, criticisms and replies.

Create a gap ledger identifying material that is absent, under-taught, misplaced or
outdated in any existing package. Restore every confirmed gap in the appropriate
accepted lesson or internal Part.

The final coverage-lock matrix must prove that every syllabus term, canonical doctrine,
advanced refinement, argument, criticism, reply and verified PYQ is present. Existing
packages are evidence sources and completeness checks, never unquestioned templates.

## Per-Subtopic Analysis Lock

Whole-topic generation in one run does **not** permit whole-topic summarisation. Before
drafting the Markdown, analyse every frozen learner-facing subtopic independently.

For each subtopic, create an internal evidence dossier containing:

1. the exact syllabus term or learning dependency it serves;
2. every relevant basic canonical heading and passage;
3. every relevant advanced, enrichment and technical passage;
4. relevant OCR-book evidence and standard formulations;
5. every directly owned or necessary cross-linked PYQ through 2026;
6. definitions and technical terminology;
7. the complete argument, including presuppositions and inferential steps;
8. examples, analogies and the limits of those examples;
9. comparisons with directly relevant thinkers or schools;
10. strongest criticisms, strongest replies and the unresolved residual;
11. UPSC traps, directive demands and answer-writing uses;
12. conceptual, applied and remedial practice requirements.

Only begin drafting after all frozen subtopics have a completed dossier and every
confirmed source item is mapped to a lesson or internal Part.

No-skipping and no-compression apply **inside every subtopic**, not merely to the topic
as a whole:

- never replace a full argument with its conclusion;
- never replace advanced content with a reference to another file;
- never move all criticism, PYQs or practice to the final synthesis;
- never merge distinct doctrines because they share vocabulary;
- never use a source summary as a substitute for reading its relevant full passage;
- never declare a subtopic complete because the overall document is long.

The final coverage matrix must include a lesson-level row for every dossier and prove
that its basic content, advanced content, arguments, criticisms, PYQs and practice were
actually taught. Any unexplained lesson-level gap blocks completion.

## Start, Generation and Navigation Lock

`Start` means: generate the **entire accepted topic** as one complete
`Learning-Session-Live-Edition.md` file in the same run. It never means generating only
the first subtopic, printing the lesson in the terminal, or starting an interactive
MCQ exchange.

Follow the original Indian Philosophy file-generation workflow:

1. Audit the complete topic and present the learner-facing roadmap.
2. Wait for `Start`; that acceptance freezes the roadmap.
3. Generate every frozen subtopic, internal Part, visual, doctrine, argument, example,
   criticism, reply, PYQ linkage and answer approach, MCQ, original Mains model answer
   and register-note section into the topic's `Learning-Session-Live-Edition.md` file
   in one uninterrupted generation run.
4. Every lesson inside the file must independently follow the Required Lesson
   Structure below and contain its own practice. Do not postpone all practice to the
   final lesson.
5. Include conceptual, applied and remedial MCQs, their answer key and an explanation
   of every option inside the Markdown. The learner is not required to answer them
   live unless test mode is explicitly requested.
6. Include every directly owned verified PYQ through 2026 as a year/question linkage
   with directive, demand and concise answer approach, mapped to the lesson where its
   concepts are taught. Do not include its solved model answer in the live-session file
   and do not generate a replacement solved-PYQ workbook.
7. Include original 10-, 15- and 20-mark Mains practice with complete model answers.
8. Use the terminal only to confirm the generated file, report concise validation
   status and accept navigation commands. Do not print the lesson prose or repeat the
   saved practice in the terminal.
9. `Next` after a successful generation means move to the **next syllabus topic**, not
   the next subtopic within the same file.
10. If generation or validation is incomplete, do not claim completion and do not move
    to the next topic.

The roadmap lists the doctrinal learning sequence. It must not imply that MCQs, PYQs,
remediation or Mains practice are postponed to a final lesson. Practice is embedded in
every subtopic, with cumulative practice added at major blocks and final synthesis.

The completed Markdown live edition preserves all teaching, MCQs, explanations,
remediation, PYQ linkage and answer approaches, original Mains practice and mastery
guidance while excluding navigation-only turns and tool logs.

## Structural Format Lock — Original Terminal Flow

Before generating or repairing any live learning session, read this rule and the full
**Required Lesson Structure** below. The learner-facing structure must reproduce the
integrated flow of the original terminal teaching sessions, not the visible scaffolding
of an existing layered source package.

Every lesson must flow directly as:

```text
Progress line
  -> Pre-teach checklist
  -> Visual
  -> Plain-language intuition
  -> Named or numbered doctrine sections
  -> Arguments and examples
  -> Comparisons, criticisms and replies
  -> UPSC application
  -> Revision notes
  -> Practice
```

The following repeated learner-facing wrapper headings are **prohibited**:

```text
LAYER 1 — SIMPLE START
LAYER 2 — CORE UPSC
LAYER 3 — ADVANCED
LAYER 4 — EXAM APPLICATION
LAYER 5 — RAPID REVISION
```

These are source-package assembly labels, not live-session teaching headings. Their
underlying content remains mandatory and must be integrated naturally into the lesson;
only the visible wrapper scaffolding is removed. Do not describe a live session as a
"five-layer session" or claim that each lesson carries five retained layers.

Existing layered packages may be used to audit completeness, recover missing doctrine
and verify practice coverage. They must never control the learner-facing structure.
The original terminal flow controls structure across Indian Philosophy, Western
Philosophy, Economy and every future subject.

**Pre-generation structural check:** before drafting the first lesson, confirm that the
planned template contains no `LAYER 1`–`LAYER 5` wrapper headings. **Final structural
check:** the completed file must contain zero such headings and zero five-layer-template
claims.

## Required Lesson Structure

Each lesson must contain:

1. **Progress line**
   - lesson number and total;
   - stage: Foundation, Core or Advanced;
   - exact subtopic.

2. **Pre-teach checklist**

```text
━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: [queried / not available]
CA search: "[exact query, where relevant]"
CA found: [headline and date / none found]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Current affairs must not be forced into a timeless philosophical topic. Record
truthfully when no meaningful recent linkage exists.

3. **Visual-first explanation**
   - ASCII flowchart;
   - comparison table;
   - hierarchy;
   - timeline;
   - argument tree; or
   - another concept-appropriate visual.

4. **Simple intuition**
   - explain the problem in ordinary language;
   - use an analogy where it improves understanding;
   - identify the exact question the doctrine attempts to answer.

5. **Technical doctrine**
   - preserve the original technical term;
   - provide a precise English explanation;
   - distinguish definition from implication.

6. **Step-by-step argument**
   - presuppositions;
   - premises;
   - inferential movement;
   - conclusion;
   - philosophical cost or limitation.

7. **Examples**
   - at least one concrete example for every abstract central concept;
   - explain the limits of the analogy.

8. **Comparative treatment**
   - compare all directly relevant schools or thinkers;
   - explain why they disagree;
   - do not provide only a memorisation table.

9. **Criticism and reply**
   - present the strongest objection;
   - present the relevant defence;
   - provide a balanced assessment where appropriate.

10. **UPSC integration**
    - syllabus relevance;
    - verified PYQ linkage through 2026;
    - probable framing;
    - common traps;
    - answer-use guidance.

11. **Revision notes**
    - 8-15 complete recall points;
    - definitions, argument sequence and contrasts;
    - mnemonics only where they genuinely aid recall.

12. **Practice**
    - conceptual MCQs;
    - applied MCQs;
    - remedial MCQs for predictable errors;
    - Mains questions and model answers;
    - relevant PYQ year/question linkage, demand and answer approach without a solved
      model answer.

## Visual Quality Rules

- Every lesson must contain at least one meaningful visual.
- Processes and arguments require flows or argument trees.
- Classifications require tables.
- Comparisons require side-by-side treatment.
- Chronological development requires a timeline.
- The visual must be explained immediately afterward.
- Technical Sanskrit terms must remain readable and be translated on first use.
- Visuals must clarify reasoning rather than decorate the page.

## PYQ Boundary

1. Cover every relevant verified UPSC Philosophy Optional or General Studies PYQ from
   the available period through **2026**.
2. Verify 2026 questions from the official paper or clearly identified provisional
   source before treating them as final.
3. Preserve the exact directive, marks and wording where available.
4. Never fabricate or reconstruct a question from memory.
5. Map every PYQ to the lesson that teaches the concepts required to answer it.
6. State the year/question, directive, conceptual demand and a concise answer approach.
7. Do not include solved PYQ model answers in the live-session file.
8. Do not create a new solved-PYQ workbook; use the learner's existing separate solved
   workbook.
9. Include cross-school PYQ linkages where the topic forms a necessary part of the
   answer.

## Practice Rules

### Whole-topic Markdown generation

- Write conceptual, applied and remedial MCQs into every relevant lesson.
- Put answers after the question set, not beside each question.
- Explain why every option is right or wrong.
- Include mastery guidance and predictable-error remediation in the file.
- Do not ask the learner to answer live unless test mode is explicitly requested.
- Complete and validate the entire topic file before accepting `Next` to a new topic.

### Compiled or pre-generated Markdown edition

- A live two-consecutive-correct feedback loop is **not required** because no learner
  is answering in real time unless test mode was explicitly requested.
- Preserve the pedagogical purpose of the loop by including:
  - standard MCQs;
  - answers after the question set, not beside each question;
  - explanation of every option;
  - remedial MCQs targeting common misconceptions;
  - cumulative tests after major blocks.
- Rotate correct options strictly:

```text
A -> B -> C -> D -> repeat
```

- Never repeat the same correct option consecutively.
- Questions must test understanding, not merely terminology recognition.
- Mains practice must include 10-, 15- and 20-mark questions with complete model
  answers.

## Fact and Inference Control

Use:

- **Fact / canonical doctrine** for statements directly supported by the source.
- **Analytical inference** for interpretation, evaluation or synthesis.

Never:

- invent a doctrine, quotation, book title, date, school attribution or PYQ;
- present a contested interpretation as unanimously accepted;
- collapse distinct schools into a generic Indian-philosophy position;
- use a current-affairs claim without verification.

## Language Standard

- Start simple and become technical progressively.
- Prefer short, direct explanatory sentences during first exposure.
- Explain one conceptual move at a time.
- Avoid dense nominalised prose where a causal explanation is clearer.
- Preserve philosophical precision without assuming prior mastery.
- Define every technical term on first use.
- Repeat a central distinction when repetition aids learning, but do not duplicate
  entire passages.

## Philosophy-Specific Requirements

For every philosophical doctrine, identify:

1. the problem being addressed;
2. the doctrine's definition;
3. its metaphysical or epistemological presuppositions;
4. the argument supporting it;
5. a standard example;
6. its relation to liberation or practice where relevant;
7. rival-school criticism;
8. the school's reply;
9. a balanced evaluation;
10. its PYQ and answer-writing relevance.

Comparative topics must explain both similarities and differences. A comparison table
without argumentative explanation is incomplete.

## Vedanta Live-Edition Boundary

The complete Vedanta live edition must include, without omission:

- Vedanta, Uttara-Mimamsa and the prasthana-traya;
- the six major commentarial traditions;
- Brahman and its essential and relational definitions;
- Advaita's six pramanas and the special role of sabda;
- nirguna and saguna Brahman;
- Brahman as efficient and material cause;
- Isvara across Advaita, Visistadvaita and Dvaita;
- bimba-pratibimba-vada and competing individuation models;
- Atman, jiva, saksi and the three states;
- jagat, vivarta, parinama and levels of reality;
- maya, avidya, their powers and the locus problem;
- Ramanuja's seven objections to Mayavada and Advaita replies;
- adhyasa and anirvacaniya-khyati;
- tat tvam asi and bhaga-tyaga-laksana;
- moksa, jivanmukti, videhamukti, devotion, surrender, grace and service;
- aprthaksiddhi and the body-soul relation;
- pancavidhabheda and Madhva's hierarchy;
- Nimbarka, Vallabha and the Caitanya tradition;
- Sankara's criticism of Samkhya;
- inter-school criticisms, replies and graded evaluation;
- every relevant verified PYQ through 2026.

## Required Final Sections

The completed Markdown must end with:

1. verified PYQ linkage and answer-approach index through 2026, without solved model
   answers;
2. original cumulative MCQ practice with explanations;
3. original 10-, 15- and 20-mark Mains practice with model answers;
4. common-error remediation set;
5. master comparison tables, causal chains and argument or criticism maps;
6. complete consolidated register notes;
7. final coverage matrix;
8. source and verification ledger.

Consolidated register notes must appear last among the teaching and practice content,
immediately before the coverage and source ledgers.

## Validation Checklist

Before declaring a live session complete, verify:

- every canonical heading is represented;
- every relevant PYQ through 2026 is mapped with its demand and answer approach;
- every major doctrine has a plain-language explanation;
- every technical term is defined;
- every abstract central concept has an example or visual;
- every major criticism has a reply;
- cross-school comparisons are doctrinally consistent;
- no advanced section has been silently omitted;
- no teaching content has been replaced by revision bullets;
- MCQ answers follow the required rotation;
- MCQ explanations cover every option;
- no unsupported quotation, date or attribution appears;
- the final coverage matrix has no unexplained gaps;
- the original canonical and generated-package files remain unchanged.

## Completion Standard

The live edition is complete only when a learner can:

1. understand each doctrine progressively without consulting the dense source first;
2. reconstruct the principal arguments and comparisons;
3. answer all relevant PYQs through 2026;
4. identify standard UPSC traps;
5. write structured 10-, 15- and 20-mark answers; and
6. use the canonical package afterward for deeper revision rather than basic
   comprehension.
