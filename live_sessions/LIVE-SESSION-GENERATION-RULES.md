# Live-Session Generation Rules

## Purpose

Generate complete learner-first Markdown sessions that preserve the depth of the
canonical knowledge package while using the clarity, sequencing and visual teaching
style of an interactive live session.

These sessions are not short notes, revision summaries or compressed substitutes for
the source material. They are complete teaching editions.

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
2. Verified UPSC PYQ ledgers and question papers through 2026.
3. OCR-searchable local books and source PDFs.
4. Official or otherwise reliable live sources where current linkage is relevant.
5. Existing generated package as a completeness cross-check, not as the sole source.
6. Qdrant only as an optional fallback.

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

## No-Skipping and No-Compression Rules

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
    - solved relevant PYQs.

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
6. Include a complete model answer for every directly owned PYQ.
7. Include cross-school PYQs where the topic forms a necessary part of the answer.

## Practice Rules

- The interactive two-consecutive-correct feedback loop is **not required** in the
  pre-generated Markdown edition.
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

1. complete consolidated register notes;
2. master comparison tables;
3. master argument and criticism map;
4. all solved PYQs through 2026;
5. original MCQ practice with explanations;
6. original Mains practice with model answers;
7. common-error remediation set;
8. final coverage matrix;
9. source and verification ledger.

Consolidated register notes must appear last among the teaching and practice content,
immediately before the coverage and source ledgers.

## Validation Checklist

Before declaring a live session complete, verify:

- every canonical heading is represented;
- every relevant PYQ through 2026 is mapped and solved;
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
