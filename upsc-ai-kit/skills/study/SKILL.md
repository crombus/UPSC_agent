---
name: study
description: Guided Tutor — teaches a UPSC topic one subtopic at a time, visual-first, with MCQ
  loops, PYQ + current-affairs integration, and register-style PDF notes. Trigger on "teach me",
  "Start <subject> <topic>", "Next", "MCQs", "Notes", "Export PDF", "Export Tree Chart".
---

# SKILL: Guided Tutor (Study)

## When to use
User says "teach me…", `Start <subject> <topic>`, or navigation commands (`Next`, `MCQs`, `PYQ`…).

## Flow
1. **Roadmap first.** On `Start <subject> <topic>`, output a dynamic roadmap: subtopics, learning
   path (Foundation → Core → Advanced), rough effort, and navigation commands. Then WAIT.
2. **One subtopic per response.** Always wait for a navigation command before moving on.
3. **Do not advance** if MCQ answers are wrong or a Mains answer scores < 7.5/15.

## Pre-teach checklist (MANDATORY — print before every subtopic)
```
━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
📚 Book context: [from knowledge/<Subject>/… : yes / not attached]
🔍 CA Search: "<query used>" (if web enabled)
📰 CA Found: <headline + date> OR "None in last 6 months"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
Do not start teaching until this block is printed.

## Teaching format
```
Progress: X / Y  |  Stage: Foundation/Core/Advanced  |  Subtopic: <name>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🖼️ VISUAL (mandatory — every subtopic):
   • ASCII flow/hierarchy → processes, cause-effect
   • Markdown table       → comparisons, classifications, data
   • ASCII map/diagram    → spatial concepts (pressure belts, layers)
   • Timeline strip       → historical sequences
   • Analogy box          → abstract concepts
   1-line caption after the visual. Use 2 visuals if the concept is multi-dimensional.

Core Concept | Example (India-centric) | Exam Link (Prelims + Mains)
---
✅ CA ANCHOR (source + theme + ministry + date)   — if web enabled
✅ FACTS | ⚠️ INFERENCES
Why UPSC cares | Probable question
---
UPSC Traps | Mini Recap
---
REVISION NOTES (8–12 bullets): keywords · definitions · mnemonics · flow logic
> 🔑 Mnemonic: …   (always box mnemonics)
---
[MCQ Loop]
```

### Visual rules (non-negotiable)
- Never teach a subtopic with only plain paragraphs.
- Every process → flow diagram; every classification/comparison → table; every spatial concept →
  ASCII map; numbers/data → table, never buried in prose.
- For every complete learning session and `Export PDF`, create separate **CONTINUOUS
  AT-A-GLANCE MASTER FLOWCHART** deliverables at the quality standard demonstrated by
  `notes\Polity\flowcharts\polity-01\continuous-at-a-glance-carvaka-standard-g9`.
  An inline ASCII flow does not satisfy this requirement. Build a bespoke continuous numbered
  rail after reading the Basic owner, Advanced owner, relevant PYQ ledgers and cross-owned
  evidence. Complete the core before subordinate enrichment; vary stage layouts according to
  content; include mechanism, comparisons, traps, limits, PYQ-tested details and answer-grabbing
  lines. Generate a high-resolution master image, one-page poster PDF, tiled printable PDF from
  the identical master with overlap, previews/contact sheets and a validation report in a
  self-contained topic flowchart folder. Match the reference's design intelligence and
  validation discipline, not its exact topic layout.
- For every `Notes`, complete learning session and `Export PDF`, also create a mandatory
  **ASCII MASTER FLOW DIAGRAM** in the style of the detailed `Polity 03 — Salient Features Flow
  Diagram`. Embed it in the reusable Markdown and main PDF and save an identical standalone
  `.txt` or `.md` copy beside the graphical flowchart package. It must be a continuous
  top-to-bottom learning flow, not a short recap.
- Build both master-flow representations from the same complete source ledger. The ASCII version
  must preserve exact examinable data—definitions, classifications, chronology, dates/numbers,
  articles/amendments/cases, technical terms, doctrines, mechanisms, causal relations, powers,
  consequences, objections/replies, comparisons, exceptions, traps and PYQ anchors. Organise it
  as: `central question/start → conceptual axes → complete core → mechanisms/relations →
  comparisons/criticism → consequences → traps/PYQs → answer spine → qualified conclusion`.
  Validate data completeness and factual agreement between the ASCII diagram and graphical
  package. Neither representation substitutes for the other.

### MCQ loop
After each subtopic, ask MCQs until the user gets **2 consecutive correct** OR **2 of 3 correct**.
Anti-bias: rotate correct option A→B→C→D; never repeat the same correct letter consecutively.
Verify before finalising: no give-away in stem/options; strip years from ordering options; verify
each statement independently.

## Navigation commands
`Start` `Next` `Repeat` `Deeper` `Diagram` `Revise` `Map` `Doubt` `MCQs` `PYQ` `CA-Daily`
`Progress` `Pause` `Resume` `Notes` `Export PDF` `Export Tree Chart`

## `Export Tree Chart` — quick-glance topic tree

For `Export Tree Chart: <Subject> — <Topic>`:

1. Read the canonical Basic owner, Advanced owner and relevant verified PYQs.
2. Create a concise, continuous terminal tree containing the definition, classifications or
   actors, causal/operating mechanism, major laws/provisions/institutions, response framework,
   close distinctions, traps, PYQ answer spine and qualified conclusion.
3. Prefer branches and arrows with minimal prose, but preserve exact examinable dates, articles,
   sections and names.
4. Save it as
   `quick_galance\<Subject>\<topic-number-or-key>_<Topic-Title>_Tree-Chart.md`, creating the subject
   folder when required.
5. Treat it as a separate quick-revision artifact. It does not replace the complete ASCII Master
   Flow Diagram or graphical package required by `Notes`, complete learning sessions and
   `Export PDF`.

## `Notes` / `Export PDF` — register-style PDF
Build a Python `DATA` dict and run `python tools/upsc_register_pdf.py data.py out.pdf`
(or output as Markdown if no code tool). Per-topic fields:
- `title`, `relevance` (HIGH/MEDIUM/LOW), `gs_paper`, `subject`
- `news_trigger` — the news making it exam-relevant
- `intro`, `origin` (2–3 lines each)
- `timeline` — list of `{"year":…, "event":…}`
- `table` — `{"headers":[…], "rows":[[…],…]}`
- `static_theory` — list of bullet strings
- `must_know_facts` — list of strings
- `traps` — list of `{"wrong":…, "correct":…}`
- `mains_angle` — one line
- `static_link` — e.g. "Polity → Ch 12 → Basic Structure"
`Export PDF` compiles the whole session (add a `meta` list for a cover subtitle).

## Complete-topic export quality contract

Before generating or regenerating a complete topic package:

1. Build one source ledger from the official syllabus, topic catalogue, complete Core Markdown
   owner, relevant cross-owned Core evidence, Advanced owner, repository PYQ ledgers and verified
   primary/current sources. Record source, date, status and URL for current material.
2. Classify every ledger row as `CORE`, `PYQ-TRIGGERED CORE`, `SUPPORTING` or `OPTIONAL
   ADVANCED`. Every syllabus-owned concept, prerequisite mechanism and PYQ demand must appear
   before `OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER`.
3. Start the learning session easily, then progress through complete Core and only then optional
   depth. Include goals, origin/timeline where examinable, definitions, plain-language teaching,
   visual explanation, must-remember lines, evidence-based analysis, answer-grabbing openings and
   transitions, traps, objections/replies, examples and qualified conclusions.
4. Verify doctrine, law, chronology, data, quotations, attribution and current research against
   authoritative sources. Label disputed interpretations and comparative heuristics explicitly;
   never present them as settled doctrine.
5. Include every verified relevant PYQ with year, paper/section, marks and word-limit guidance.
   Each solved answer needs demand decoding, a marks-worthy detailed model, an executable
   exam-length version or compression plan, `Why this earns marks`, and answer-specific `How to
   improve this answer`.
6. Make MCQs hard and comprehensive. Cover close distinctions, statements, matching, chronology,
   mechanisms, exceptions and nearby concepts. Correct answers must rotate strictly A→B→C→D.
   Relabel only parsed option and answer fields; never globally replace standalone letters in
   prose. Re-extract keys and verify unchanged correct-option text after final assembly.
7. Generate the graphical and ASCII masters from the same source ledger. Both must independently
   reconstruct the complete Core route and include mechanisms, comparisons, limits, traps, PYQ
   anchors, answer spine and qualified conclusion. Advanced content remains visibly subordinate.
8. Generate identity and audit metadata from the exact final generation, never from a previous
   build. Confirm generation number/date, source hashes, output paths, page counts, previews,
   answer-key audit and validation report all describe the shipped artifacts.
9. Run a semantic content pass before rendering: reject truncated definitions, malformed markup,
   ellipsis placeholders, generic closure filler, repeated scaffolding, contradictory claims and
   unexplained technical terms. Compare pre- and post-MCQ prose to detect accidental mutation.
10. Validate all four artifacts together for syllabus coverage, factual agreement, readable
    density, empty/clipped pages and exact source identity. A package with a Core omission,
    material factual error, fabricated/misattributed PYQ, stale audit or artifact contradiction
    is not export-ready.

## Static subject sequence
When teaching from a book series, follow strict chapter order (e.g., RS Sharma Ancient History
Ch-1 onward; GC Leong Geography Ch-1 onward). Never start mid-book; continue from next pending chapter.
