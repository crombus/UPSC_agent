# UPSC Agent — Saved Instructions & Memory

> **Portable single source of truth** for all rules, preferences, workflows, and verified
> facts that @pulkitkundra has asked the agent to "save".
> Whenever the user says **"save"**, the agent does BOTH: (1) stores a Copilot memory, and
> (2) appends/updates the rule here so it survives across sessions, machines, and other apps.
>
> _Last updated: 2026-08-23_

---

## 0. How "save" works (meta-rule)

- When the user says **"save" / "save instructions" / "remember"**, persist the rule in **two** places:
  1. **Copilot memory** (`store_memory`, user scope).
  2. **This file** (`AGENT_MEMORY.md`) under the correct section, so it is portable and reusable
     in future sessions or other applications.
- Keep entries concise, grouped by topic, and dated when material changes.

---

## 1. Core principles (highest priority)

- **Verify before stating.** Never present unverified training-knowledge facts as ground truth.
  Use `web_search` for CA/recent facts; use Qdrant for book facts. If uncertain, say so.
  Wrong data in UPSC prep is worse than no data — this rule overrides convenience.
- **No fabrication.** Never guess %, ₹, years, targets, counts, or scheme names.
- **Tag everything:** ✅ Fact = directly from fetched/retrieved source · ⚠️ Inference = analytical.
- **Learning-session source priority:** (1) Markdown knowledge files →
  (2) OCR-searchable PDFs for deeper book evidence → (3) live current affairs →
  (4) Qdrant only as an optional fallback.
- **India-centric examples** always.

---

## 2. Static grounding and Qdrant fallback

- For learning sessions, use the authored Markdown knowledge files first and the OCR-searchable
  PDFs second for deeper source evidence.
- Add live current affairs after establishing the static foundation.
- Qdrant is optional and must not block a learning session. Use it only when the Markdown and OCR
  sources are insufficient and Qdrant is available at a practical response time.
- Optional Qdrant query:
  ```
  python tools/query_books.py "<topic>" --subject "<Subject>" --limit 5
  ```
  `--subject` is an **exact-match** filter — the string must match the stored tag precisely.
- If Qdrant is unavailable, empty, or slow, continue with Markdown + OCR PDFs + live current
  affairs without delaying the session.

### Subject tags (exact strings)
Indian Polity · Economy · History · Geography · Ethics · International Relations ·
Internal Security · Disaster Management · Current Affairs
**PYQ tags:** `Prelims PYQ` · `CSAT PYQ` · `Mains PYQ` · `Philosophy PYQ`

---

## 3. Exam generation

### Format v2 (current, locked)
- **Paper 1 — 100 MCQs:**
  - 80 GS = **48 Current Affairs** + **32 Static**
  - 20 **CSAT (Hard)** — calibrated to real UPSC PYQ difficulty (query `--subject "CSAT PYQ"`).
- **Paper 2:** 2 × 10-mark + 2 × 20-mark Mains (user attempts 1 of each pair) + **Essay (1 of 3)**.
- Philosophy essay: optional / random — not every paper.
- Difficulty will scale up slowly over time.

### Sourcing rules
- **Book/static questions come from Qdrant** (genuine book content) — never hallucinated.
- **For CA sections, also `web_search`** around the user's given topics — they may have missed items.
- **Recency weighting 40:60** → 40% older/static (> 1 week), 60% past-week content.
- Reserve a portion for **static topics** even in CA-heavy papers.
- Generate the exam for **whatever topics the user gives**, even if some overlap.

### MCQ verification step (run BEFORE finalizing every MCQ)
1. Does the question text or options accidentally give away the answer? (Fix if so.)
2. Chronological-ordering questions: **strip all years/dates** from option text — use event/conflict
   names only.
3. Statement-based questions: verify **each statement independently** before marking correct/incorrect.
- Keep all options comparable in length, specificity, grammar, and detail. Never let the correct
  answer become identifiable because it is consistently the longest or most elaborated option.
- Preserve clear, concept-rich teaching and MCQ lines from successful interactive sessions for
  later notes, workbooks, and topic exports; do not replace them with weaker generic paraphrases.
- **Anti-bias:** rotate the correct option A→B→C→D; never repeat the same option consecutively.
- CA MCQs must test **concept + geography + institution + data** — NOT ceremony details
  (signing dates, venues, who represented whom). Concept-level facts = higher UPSC probability.
- When a topic was covered in the current session's CA analysis, use **session-verified CA data first**;
  training knowledge is fallback only.
- **Marking:** MCQ = +2.00 correct / −0.66 wrong / 0 skipped.

### PDF workflow
- Build data `.py` → `python tools/upsc_exam_pdf.py <data.py> <out.pdf>` → delete the data `.py`.
- Papers → `exams/papers/..._QP.pdf` · Answer keys → `exams/answer-keys/..._AK.pdf`.
- **Set matching:** prelims QPs are **Set A only**; `Ans-*` files hold all sets → map Set A → Set A column.

### Interactive topic-specific MCQ test protocol (saved 23 August 2026)

**Trigger:** when the user asks for an `MCQ test`, `MCQ practice`, `test me`, or equivalent and
specifies one or more topics, execute this protocol by default unless the user requests another
format.

1. Resolve the complete Core/Basic Markdown owners for every specified topic and build an internal
   coverage ledger before asking questions. Use OCR PDFs only for deeper evidence and live web
   sources for current facts; Qdrant remains optional.
2. Ask **one MCQ at a time**. Do not show the answer before the learner responds.
3. Rotate topics fairly and rotate correct options strictly **A → B → C → D**, continuing the
   sequence across the whole test.
4. Begin with foundation/medium questions, then progress to hard UPSC-style statement,
   close-option, chronology, matching and conceptual-comparison questions once the foundation is
   covered.
5. After each learner response:
   - state `Correct` or `Incorrect` and give the correct option;
   - analyse every statement or option independently;
   - define every relevant technical term and abbreviation;
   - add the relevant timeline, wider context and at least one concrete example;
   - explain the exact trap that makes the wrong choice fail;
   - answer any doubt raised by the learner;
   - immediately present the next MCQ unless coverage is complete or the learner asks to stop.
6. Persist the test under
   `upsc-ai-kit\practice\<topic-set>-MCQ\<YYYY-MM-DD>\` with:
   - one `README.md` containing method, progress, coverage ledger, results and final audit;
   - one separate `MCQ-NNN.md` per question containing the question, learner answer, correct answer,
     result and full explanation;
   - learner doubts and clarifications appended to the relevant question file.
7. Avoid accidental duplication. Repeat a concept only for deliberate remediation, using a new
   angle or harder framing.
8. Continue until every major objective fact, distinction, exception, timeline and conceptual
   trap in the specified Core files has been tested. Then run a formal coverage audit and
   **automatically close the loop**; do not create another question merely to extend the count.
9. At closure, report total questions, correct/incorrect counts, accuracy, topic-wise performance,
   strongest areas and priority-revision areas. Record that no further question is pending.
10. If the user stops early, preserve the exact pending-question state so the same loop can resume
    later without losing answer rotation, topic rotation or coverage tracking.

---

## 4. Current Affairs analysis

- **Sources are for DISCOVERY only** (what news happened on a date). ALL UPSC analysis
  (relevance, dimension shift, traps, mains angle) must be the agent's own — never copied from
  coaching-site analysis.
- **Source fetch methods:**
  - Vision IAS — JS-rendered + paywalled → use `web_search "visionias topics YYYY-MM-DD"` (no direct fetch).
  - Vajiram — `vajiramandravi.com/current-affairs/upsc-prelims-current-affairs/YYYY/MM/DD/` (direct fetch OK).
  - MEA — JS-rendered → `web_search site:mea.gov.in "DD Month YYYY"` (no direct fetch).
  - PIB — `web_fetch pib.gov.in/indexd.aspx?reg=3&lang=1`.
  - GKToday `/current-affairs/june-DD-YYYY/` returns 404 — avoid.
- **Per-item deep-analysis order:** FACTS → **📘 FULL FORMS** (dedicated section, every abbreviation
  expanded, placed right after FACTS) → ORIGIN → … → traps → mains angle → static link.
- **After EVERY CA item:** include (1) **MCQ loop** (2–3 MCQs, anti-bias rotation) and
  (2) **Register Notes** (title, facts, timeline, traps, mains angle). Both mandatory per item.
- **Medium-item format:** Title + GS paper + news trigger + 4–5 key facts + 1 UPSC trap +
  Mains angle (1 line) + static link. Not just 2-line summaries.
- **Export PDF** must include ALL items: HIGH (full deep analysis), MEDIUM (expanded summary +
  GS angle + key facts + 1 trap), LOW (2–3 line note + GS paper). Never export only HIGH.
- **Never conflate distinct news items.** Each separate event = its **own card/section** in CA
  analysis, deep-dives, and Export/Notes PDFs. Never merge two stories into one card, and never
  phrase them so one event appears to **cause or be the subject of** another — even words like
  "separately"/"simultaneously" inside one shared card still mislead. One news item → one card.

---

## 5. Guided Tutor & Notes

- **Static notes follow strict chapter sequence** — never skip or start mid-book:
  - RS Sharma Ancient History from **Ch-1** onwards.
  - GC Leong / Geography from **Ch-1** onwards.
  - Track completed chapters; always continue from the next pending chapter.
- Teach **visually first** (≥1 diagram/table/flowchart per subtopic), text second.
- One subtopic per response; never auto-advance — wait for a navigation command.
- **Quick-glance tree-chart command (saved 3 September 2026):** `Export Tree Chart: <Subject> —
  <Topic>` creates a concise, continuous terminal tree for that specific topic and saves it at
  `quick_galance\<Subject>\<topic-number-or-key>_<Topic-Title>_Tree-Chart.md`. Derive it from the
  canonical Basic owner, Advanced owner and relevant verified PYQs. Retain the definition,
  classifications/actors, causal or operating mechanism, major laws/provisions/institutions,
  response architecture, high-yield distinctions, traps, PYQ answer spine and qualified
  conclusion. Use branches and arrows with minimal prose, but do not remove exact examinable
  dates, articles, sections or names. This quick-glance chart is a separate revision artifact and
  never replaces the complete ASCII Master Flow Diagram or graphical master-flow package.
- **Verbatim learning-session export (all subjects):** when exporting a completed interactive
  learning session, the notes Markdown and main notes PDF must preserve the teaching **word for
  word and in the original order**, including roadmap, pre-teach checklists, visuals, tables,
  explanations, traps, revision notes, MCQs, remedial feedback and completion messages. Do not
  summarize, compress, rewrite or reorganize the taught session. A separately requested workbook
  may remain structured for practice.
- **Universal Export PDF workflow (all subjects):** whenever the user asks to export a PDF for
  any topic, first create the complete Guided Tutor-style learning session in the approved format,
  even if that topic was not previously taught interactively. Then save the session Markdown and
  render that same session verbatim to the main PDF. Never substitute a condensed topic summary.
- **Mandatory continuous at-a-glance flowchart standard (saved 22 August 2026, clarified by
  user):** every topic learning-session PDF request must also produce separate flowchart
  deliverables matching the design intelligence and validation quality of
  `notes\Polity\flowcharts\polity-01\continuous-at-a-glance-carvaka-standard-g9`.
  An ASCII diagram inside the notes PDF is not sufficient. Build a bespoke continuous numbered
  rail from the complete Basic owner, Advanced owner, PYQ ledgers and cross-owned evidence.
  Finish the full core before subordinate enrichment; vary each stage's internal grammar
  (chains, matrices, timelines, comparisons, ladders, replacement diagrams and mechanism bands);
  include dense keyword pills, traps/limits and unique answer-grabbing lines. Produce a
  high-resolution master canvas, one-page poster PDF, tiled printable PDF from identical
  overlapping crops of the same master, previews/contact sheets and a validation report inside
  a self-contained topic flowchart folder. Validate source completeness, layout diversity,
  overflow, required terms, same-master identity and reference immutability. Match the g9
  quality standard, not its topic-specific content or exact stage template. Keep every generated
  flowchart unapproved until explicit topic-generation approval.
- **Mandatory dual master-flow rule (saved 22 August 2026, clarified at 21:25 IST):** every
  `Notes`, complete learning-session and `Export PDF` deliverable must include both:
  (1) the designed Carvaka-standard graphical package (master PNG, poster, same-master tiled PDF,
  previews and validation), and (2) a terminal-friendly **ASCII MASTER FLOW DIAGRAM** like
  `Polity 03 — Salient Features Flow Diagram`. Embed the ASCII version in the reusable Markdown
  and main notes PDF and save it as a standalone text/Markdown artifact beside the graphical
  package. Neither output replaces the other.
- **ASCII master-flow parameters:** derive it from the complete Basic owner, Advanced owner,
  audited PYQs and cross-owned evidence; use one continuous top-to-bottom flow with topic-specific
  branches, matrices, timelines, hierarchies and bounded panels. Preserve all examinable data:
  definitions, classifications, chronology, exact dates/numbers, articles/parts/schedules,
  amendments/cases, technical terms, philosophers/doctrines, mechanisms, powers, causal links,
  consequences, objections/replies, comparisons, limits, exceptions, traps and PYQ-tested minor
  facts. Follow learning order:
  `central question/start -> conceptual axes -> complete core -> mechanisms/relations ->
  comparisons/criticism -> consequences -> examiner traps/PYQ anchors -> answer spine ->
  qualified conclusion`. Keep connected distinctions together and never shorten away precise data
  for visual neatness. Independently reconcile both master flows against the same coverage ledger
  and require factual agreement between them.
- **Manually authored ASCII atlas standard (saved 23 August 2026):** finalized learner-v2
  packages require a manually authored, topic-specific panel atlas. For the active 40-topic set,
  the four specs under `upsc-ai-kit\manifests\retrofits\ascii-panel-specs\` are authoritative;
  preserve panel titles, order and lines exactly, with the approved Notions-of-God ten-panel
  master as reference. Generic/heuristic panels are development-only and cannot be finalized.
  Require exact embedded/spec and standalone/spec equality; reject generic central wording,
  placeholders, ellipses, repeated `KEY TERMS:` scaffolding, session dumps, over-width lines,
  missing sequence/topology and source-reference integrity failures.
- **Basic-first, advanced-last learning sequence (saved 20 August 2026):** the main notes PDF must
  read exactly like the easy-to-understand Guided Tutor learning session, not like dense reference
  notes. Teach every substantive point from the `basic/` owner first, in its natural subtopic order,
  using the normal visual -> simple explanation -> example -> exam link -> traps -> recap flow.
  Do not interleave advanced material into the Basic teaching. Keep the established solved-PYQ,
  MCQ/remedial and Mains-answer standards unchanged. After the complete Basic session and its exam
  application, add every substantive point from the `advanced/` owner as a separate final teaching
  block labelled **OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER**. Advanced content is
  for enrichment, qualification and higher-level depth; it must not make the core session harder
  to understand. The consolidated register notes may remain the final structural section, but must
  preserve the Basic/Optional-Advanced distinction.
- **Learner-first v2 export foundation (saved 20 August 2026):** v2 is Markdown-first. Assemble the
  complete learner-facing Markdown once, validate it, and render both the main PDF and any derived
  workbook from that Markdown with `tools\markdown_learning_pdf.py --variant learner-v2`. Never
  create the v2 main PDF from a separate compressed data summary. Its canonical H2 sequence is:
  `BASIC LEARNING SESSION` -> `BASIC MCQS / REMEDIATION` ->
  `PYQS AND ANSWER PRACTICE` ->
  `OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER` ->
  `CONSOLIDATED REGISTER NOTES`. Subtopics use H3 or lower; register notes are the last H2.
- **Learner-v2 is the approved default workflow (saved 20 August 2026):** use learner-v2 for every
  new export. This is approval of the workflow and format only. Topic output approval remains
  isolated to an exact `topic_key + variant + generation`; do not mark an existing pilot or future
  topic `approved: true` unless the user explicitly approves that specific topic generation.
- **Learner-v2 internal PDF indexes (saved 20 August 2026):** every learner-v2 notes PDF and every
  learner-v2 workbook PDF has its own internal contents/index directly after the cover/title/front
  matter and before teaching or questions. Generate it automatically from the final heading
  hierarchy with `tools\markdown_learning_pdf.py`; topic authors never maintain page numbers
  manually. Include meaningful parts/subtopics rather than every tiny utility heading. Page
  numbers must be accurate after insertion and within the final PDF range; prefer PDF bookmarks
  mirroring the same hierarchy. The notes index and workbook index are independently appropriate
  to their own contents.
- **Permanent subject/section workflow (saved 20 August 2026):** work subject-wise and
  section-wise. The user supplies a section. Before content generation, reconcile the official
  syllabus with repository topic owners, enumerate the complete section topic list, and
  create/update its machine-readable manifest and topic-coverage index. Record planned topics,
  syllabus mapping, Basic/canonical owner, Advanced owner, cross-topic/thematic sources, verified
  PYQ sources, current status and expected deliverables. Present this index before starting.
- **Sequential one-topic execution is the user-facing default:** after the manifest is accepted,
  present and follow the manifest-ordered topic queue in
  `V2-SUBJECT-SECTION-COMMAND-INDEX.md`. The recommended command is
  `Generate learner-v2 topic: <Subject> — <Section name or key> — <Topic display title>`.
  Run one topic command at a time; do not begin the next topic until the current command has
  generated, validated and finalised that topic and refreshed the tracker, global coverage,
  section coverage, notes-PDF and workbook-PDF indexes. A full-section command remains available
  for explicit batch requests, but it is not the recommended default.
- **Safe next-ten execution:** use the exact command
  `Generate next 10 learner-v2 topics: <Subject> — <Section name or key>`. Resolve the
  catalogue and manifest, select the next 10 planned or incomplete topics in manifest order, and
  exclude successfully generated and validated topics unless the command explicitly ends with
  `— Regenerate`. Process strictly one topic at a time. After each topic, validate it, finalise
  its tracker record, and refresh the global command index plus the section coverage, notes-PDF
  and workbook-PDF indexes before starting the next topic. Stop immediately on the first failure
  or ambiguity and do not generate or mark any later topic complete. If fewer than 10 eligible
  topics remain, process all remaining topics. Every newly generated topic remains
  `approved: false` until the user explicitly approves that exact topic generation.
- **Learner-v2 topic command controls:** append `— Regenerate` only when intentionally replacing
  an existing topic generation, `— Generate index only` when only index reconciliation is wanted,
  or `— Pause after generation before finalising` when the user wants a review checkpoint before
  validation/tracker/index finalisation. Keep these suffixes out of ordinary commands unless their
  stated behaviour is wanted.
- **Learner-v2 answer-worthiness and anti-padding standard (saved 20 August 2026):** Topic 01's
  learner-friendly explanatory style is the quality benchmark, but its page count is never a
  target. Before finalising every new or regenerated topic, visibly classify major content as
  **CORE PRELIMS**, **CORE MAINS**, **SUPPORTING**, or **OPTIONAL ADVANCED**. Preserve every
  substantive Basic-owner point and teach it progressively with visuals, examples, traps and
  answer use. Retain only supporting examples that improve Prelims elimination or Mains argument
  quality; compress repetition, exhaustive catalogues, duplicated cases, scholar lists and
  technical minutiae that do not earn marks. Teach substantial Advanced-owner depth separately
  after all Basic and practice, but make clear that it is enrichment and is unnecessary for a
  competent core answer. Audit official-syllabus ownership and verified PYQ frequency honestly:
  do not inflate direct Mains relevance when a topic is mainly contextual or supportive. Length
  must follow syllabus completeness, ease of learning and answer value—not similarity to another
  PDF's word or page count.
- **Single-writer rule for learner-v2 generation (saved 20 August 2026):** do not run two topic
  generation, regeneration, finalisation or index-refresh commands simultaneously from different
  terminals against the same repository/worktree. Topic content files may be distinct, but all
  runs update shared state such as `EXPORT-PDF-STATUS.json`, `EXPORT-PDF-COMMAND-INDEX.md`,
  `V2-SUBJECT-SECTION-COMMAND-INDEX.md`, global study/command indexes and section indexes. The
  current tools use staged/atomic replacement for some writes but no repository-wide
  cross-process lock, so concurrent runs can lose tracker records or overwrite indexes. Process
  commands sequentially. Parallel research or read-only inspection is safe; parallel generation
  is allowed only in isolated worktrees/branches with separate output/state files and a controlled
  merge followed by one final tracker/index refresh in the target worktree.
- **Section completeness rule:** Markdown is the primary content source, but no single Markdown
  file proves completeness. Reconcile (1) official syllabus, (2) Basic/canonical owner,
  (3) relevant cross-topic/thematic Markdown, (4) available verified PYQs, and (5) the Advanced
  owner last. OCR-searchable local PDFs and live sources supplement this chain; Qdrant remains an
  optional fallback.
- **Preferred section-wise v2 paths:** use
  `upsc-ai-kit\knowledge\<Subject>\learning-sessions\v2\<section-key>\<topic-key>_Learning-Session.md`,
  `notes\<Subject>\learning-session-v2\<section-key>\notes\<topic-key>_Learning-Session_<date>.pdf`,
  `notes\<Subject>\learning-session-v2\<section-key>\workbooks\<topic-key>_Solved-Workbook_<date>.pdf`,
  and three separate indexes under
  `notes\<Subject>\learning-session-v2\<section-key>\indexes\`: `TOPIC-COVERAGE-INDEX.md`,
  `NOTES-PDF-INDEX.md`, and `WORKBOOK-PDF-INDEX.md`. Notes and workbooks must never share an
  external index. These external indexes track coverage and deliverable files; they never replace
  either PDF's internal contents/index. Existing topic-folder learner-v2 pilots remain valid
  compatibility paths; do not move, copy, rename or overwrite them or any v1 PDF, asset or
  Markdown.
- **Section-generation command guide:** the authoritative user-facing file is
  `V2-SUBJECT-SECTION-COMMAND-INDEX.md`. Follow it when the user gives section-generation
  instructions. Its primary command catalogue comes from
  `upsc-ai-kit\manifests\v2\topic-catalog.json` and must cover every source-ready repository
  topic, not only topics already present in pilot section manifests. Group commands by the
  narrowest unambiguous repository syllabus section, keep one exact copy-paste command per topic
  in source order, and append `— Regenerate` only when a learner-v2 tracker generation already
  exists. Unresolved entries stay in a clearly separated appendix and do not receive ready
  commands. The guide may retain registered-pilot detail after the complete catalogue.
- **On-demand section materialisation:** a catalogue command remains valid when its section has no
  registered manifest. Resolve the exact catalogue entry, materialise the complete section
  manifest and its three external indexes from the catalogue, then generate only the requested
  topic. The user never has to create or edit JSON manually. Regenerate the catalogue and guide
  deterministically with `python tools\generate_v2_topic_command_catalog.py --guide`.
- **Section index refresh:** rerun `tools\generate_v2_section_indexes.py` after each topic changes
  state. The three indexes must classify planned, incomplete, generated/unapproved and approved
  independently from `EXPORT-PDF-STATUS.json` schema v2, remain deterministic, and never duplicate
  rows. Use `tools\finalize_v2_topic.py` only as the safe post-topic sequence: validate known
  outputs -> upsert the supplied tracker identity -> regenerate the global command index ->
  regenerate that section's indexes. It does not generate content.
- `learning-sessions\` is the canonical archive name. `Terminal-Learning-Sessions`,
  `learning-sessions-v2` and `_learning-sessions` are legacy compatibility aliases that indexers
  may read but new content must not use.
- **V2 tracker identity and rollback:** each `EXPORT-PDF-STATUS.json` record is independently keyed
  by `topic_key + variant + generation`, has a stable `record_id`, and records `supersedes`.
  Approval belongs only to that exact variant/generation; learner-first v2 never inherits a v1
  approval. V2 provenance must name the Basic owner, optional Advanced owner, assembled Markdown,
  renderer name/version, generation date and superseded v1 record/topic when one exists. Rollback
  means deleting only the v2 output folder/Markdown and its v2 tracker records; legacy v1 remains.
- **Philosophy learner-v2 ordering override (saved 20 August 2026):** the legacy Philosophy
  five-layer rule remains authoritative for legacy-v1 and must not be rewritten in place. For
  `learner-v2` only, preserve all five kinds of content but reorder them package-wide: all logical
  subtopics' `SIMPLE START` + `CORE UPSC` material forms the complete Basic session;
  `EXAM APPLICATION` + `RAPID REVISION` becomes diagnostic/PYQ/Mains practice; every `ADVANCED`
  point moves to the final optional teaching block labelled **OPTIONAL ADVANCED DEPTH — NOT
  REQUIRED FOR A CORE ANSWER**; consolidated register notes remain last. This is an ordering
  override, never permission to compress, delete or transfer approval from v1.
- **Export completion and approval tracking:** after creating a complete package, record its main
  PDF, solved workbook and reusable Markdown paths in `EXPORT-PDF-STATUS.json`, then run
  `python tools\generate_export_command_index.py`. A package is generated only when all three
  files exist. Set `approved: true` only after the user explicitly approves that topic package;
  this produces the permanent tick in `EXPORT-PDF-COMMAND-INDEX.md`.
- **Permanent export completion report (saved 12 August 2026):** after every export completes,
  the final response must list the exact path of every file created or modified by that export.
  Listing a file does not imply approval; every newly generated package remains
  `approved: false` until the user explicitly approves it.
- **Universal command completion report (saved 12 August 2026):** after every completed user
  command—not only PDF exports—the final response must list the exact repository-relative path of
  every file created or modified during that command. If no file changed, state
  `Files changed: none`.
- Store reusable interactive-session Markdown under
  `upsc-ai-kit/knowledge/<Subject>/learning-sessions/`. Create that dedicated folder for every
  subject; do not mix verbatim session transcripts into `basic/`, `advanced/` or canonical topic
  files.

### 5a. AI-kit knowledge files (output format & location — IMPORTANT)

- Subject study notes are authored as **Markdown `.md`**, saved under
  `upsc-ai-kit/knowledge/<Subject>/basic/` and `upsc-ai-kit/knowledge/<Subject>/advanced/`.
  **NOT** PDFs — these are portable knowledge for **Claude / Gemini / OpenAI**, consumed alongside
  `system-prompt.md` + `skills/` + `tools/`. (PDFs in `notes/` are a separate, optional deliverable.)
- Format = the Polity kit style: `#` title with `— MUST-DO`/`— ADVANCED`, blockquote header
  (Subject · Tier · GS Paper · "Grounded in" · ✅/⚠️/📰 legend · `*Companion:*`), numbered `##`
  sections, Markdown tables, `> 🔑 Trap:` callouts, **Must-Know Facts**, **UPSC Traps**,
  **📰 Current link**, **Mains angles**. File naming `NN_Topic-Name.md`.
- **Accuracy & completeness are paramount; never drop or fabricate facts. Must-Do tier is the
  priority and must be exhaustive.**
- **Geography tier mapping:** `basic/` (Must-Do) = **Majid Husain "Indian & World Geography" + GC
  Leong + CA anchor**; `advanced/` = **Dr. D.R. Khullar + Majid Husain India geography + extra
  distinct CA**. **Both tiers must carry a current-affairs anchor.** (Khullar = optional-level depth.)

### 5b. Philosophy Optional PDF creation

- **Topic-package trigger (all subjects):** `Create Topic Package: <Subject> — <Topic>` builds the
  complete package even when no interactive teaching session was previously run. `Export PDF`
  applies the same package standard to the current topic/session.
- **Philosophy-only layered command rule:** when the active subject is Philosophy, both `Notes`
  and `Export PDF` must use this five-stage sequence for every logical subtopic:
  **1. SIMPLE START** (plain-language visual gateway) -> **2. CORE UPSC** (terminology,
  doctrine, arguments and examples) -> **3. ADVANCED** (objections, replies, comparisons and
  refinements) -> **4. EXAM APPLICATION** (verified PYQs and answer structure) ->
  **5. RAPID REVISION** (traps, concise register notes and MCQs).
- **Philosophy-only English-first terminology rule:** retain every common all-subject package
  rule, but in Philosophy Optional notes make the English concept the main expression and place
  its standard Sanskrit or Pali term immediately afterward in parentheses, using accurate IAST.
  Write `dependent origination (pratītyasamutpāda)` and `Middle Path (madhyamā pratipad; Pali:
  majjhimā paṭipadā)`, not an unexplained Indic term followed later by an English gloss. Apply
  this to headings, prose, tables, diagrams, captions, revision notes, questions and model
  answers. Exceptions are verbatim syllabus/source quotations and passages specifically analysing
  the original term; even there, provide an immediate English gloss.
- **Philosophy-only conceptual-completeness rule:** the printed syllabus terms are the minimum
  coverage spine, not permission to omit indispensable background doctrines. Before finalising a
  Philosophy topic, audit the complete school/thinker framework needed to understand the listed
  doctrines and answer its PYQs. For Buddhism this expressly includes both senses of the
  **Middle Path (madhyamā pratipad; Pali: majjhimā paṭipadā)**: the practical path between
  sensual indulgence and self-mortification, concretised in the Noble Eightfold Path
  (āryāṣṭāṅgamārga), and the doctrinal avoidance of eternalism and annihilationism. A mere passing
  mention does not count as coverage; explain its structure, function, relation to the Four Noble
  Truths and dependent origination, and exam relevance.
- The explicit aliases `Philosophy Notes: <Topic>` and `Export Philosophy PDF: <Topic>` invoke
  the same Philosophy-only layered standard. A separate command is not required when the active
  learning session is already clearly identified as Philosophy.
- **Philosophy `Notes` deliverable:** create one complete layered notes PDF plus reusable layered
  Markdown. It is not the generic short register-card PDF. A separate solved workbook and export
  tracking are required only when the user asks for `Export PDF`, `Export Philosophy PDF`, or a
  complete topic package.
- **Philosophy `Export PDF` deliverables:** create the layered main learning-session PDF, a
  separate premium solved-practice workbook, and reusable layered Markdown; then update the
  export tracker and command index.
- **Preservation rule for layering:** retain every existing substantive definition, derivation,
  distinction, example, criticism/reply, comparison, PYQ, answer framework, revision point and
  practice explanation. Layering may reorder this material and add simpler gateways, but must
  never compress or delete it. If the user explicitly asks for a verbatim or word-for-word
  transcript, preserve the original order instead and add the simple layer without moving the
  transcript.
- Follow `PHILOSOPHY_VISUAL_NOTES_AI_PLAYBOOK.md` for every topic-wise Philosophy PDF.
- Also follow `PHILOSOPHY_PDF_CONTENT_AND_VISUAL_STANDARD.md`. Content determines
  the design: never reduce substantive doctrine, criticisms, comparisons, PYQs
  or answer frameworks merely to shorten or beautify a PDF.
- Analyze available local Philosophy PDFs directly; do not replace direct source analysis with
  Qdrant/RAG summaries when the PDFs are available.
- Before each PDF, research current educational information-design patterns and
  choose visuals by learning purpose rather than defaulting to Venn diagrams.
- Each PDF must be visually learnable and include topic-specific mind maps, argument or causal
  flows, concept links, comparison tables, memory hooks, must-know facts, UPSC traps, PYQ routes,
  and 10/15/20-mark answer frameworks.
- **Complete-session export rule (all subjects):** the main topic PDF must preserve the full
  detailed learning session verbatim when an interactive session exists. Include every
  substantive definition, derivation, distinction, example, criticism/reply, technical term,
  advanced refinement, solved PYQ, MCQ loop and remedial practice item needed for understanding.
  Remove only tool noise; do not remove or rewrite taught repetition, feedback or navigation
  content when the user requests a word-for-word export. End with complete consolidated register
  notes covering every subtopic in the learning session, after all teaching and practice material.
  When no interactive session exists, internally construct that same learner-facing sequence:
  complete Basic teaching first, answer/practice application unchanged, and optional Advanced depth
  last. A thematically reorganised reference chapter is not an acceptable substitute.
- **Separate practice-workbook rule (all subjects):** alongside the main topic PDF, create a
  second detailed PDF containing topic-complete solved PYQs plus MCQ and remedial practice with
  explanations. Include MCQs spanning nearly every subtopic and add original Mains practice
  questions with model solutions. Rotate correct MCQ options A -> B -> C -> D.
- **Exam-stage PYQ coverage rule:** for subjects or topics that overlap between UPSC Prelims
  and Mains, the solved workbook must include all relevant verified PYQs from both stages. For
  subjects or topics tested only in Prelims, include the relevant verified Prelims PYQs and
  objective-answer explanations; do not force unrelated Mains PYQs into the workbook.
- **Unavailable Prelims-key rule:** when the official answer key is unavailable or unreadable,
  do not omit the relevant PYQ. Infer the most defensible answer from authoritative subject
  knowledge, explain the elimination logic, state a confidence level, and label it prominently
  as **INFERRED ANSWER — NOT OFFICIALLY VERIFIED**. Never present an inferred key as official.
- **Premium solved-workbook standard (all subjects):** every solved PYQ must include an
  examiner-grade, highest-standard model answer appropriate to its marks and directive, followed
  by a specific explanation of what an outstanding answer for that question and subject must
  contain (structure, concepts, comparisons, criticisms, examples, terminology and verdict).
  After the solved PYQs, include a substantial set of hard MCQs covering almost every part of the
  learning session, with four plausible options, strict A -> B -> C -> D key rotation and detailed
  explanations. End with revision-oriented Mains practice questions across relevant mark levels,
  each solved to the same highest standard. Brief answer routes alone are not sufficient.
- **UPSC Mains model-answer quality standard (all subjects, saved 12 August 2026):** UPSC does
  not publish a fixed answer-level marking formula, so use the following as the repository's
  examiner-oriented working standard:
  1. **Demand fidelity:** decode every keyword, directive, scope, time period, mark allocation and
     word limit. Answer every part of the question and do not substitute a memorised adjacent
     topic.
  2. **Direct thesis:** begin with a short definition/context and a defensible answer to the
     question. The introduction must orient the examiner rather than merely repeat the stem.
  3. **Structured coverage:** organise the body into logical dimensions appropriate to the
     subject, using meaningful headings, chronology, comparison, causation or stakeholder lenses.
  4. **Evidence-linked analysis:** use the pattern **claim -> named evidence/example -> what it
     proves -> limitation/qualification**. Examples must support an argument, not appear as a
     decorative list.
  5. **Evidence density:** normally include at least 2-3 precise examples in a 10-marker, 4-6 in
     a 15-marker and 5-8 in a 20-marker, adjusted for the question. Use subject-appropriate named
     evidence: texts/authors/sites in History; Articles/cases/commissions in Polity; data/reports/
     schemes in Economy and Society; thinkers/arguments/quotations in Philosophy and Ethics;
     maps/processes/case studies in Geography and Environment.
  6. **Analysis over narration:** explain how, why, consequence, significance and interrelation.
     Avoid chronology or fact-dumping unless the directive specifically requires description.
  7. **Balance and source criticism:** include counter-evidence, limitations, regional/social
     variation, contested interpretation or implementation gaps wherever relevant. Do not force
     artificial balance when the evidence is one-sided.
  8. **Value addition:** use accurate terminology, a compact diagram/map/table where it improves
     comprehension, a relevant current or comparative linkage, and scholars only when their view
     directly advances the answer.
  9. **Reasoned conclusion:** deliver a graded verdict that answers the directive and follows from
     the body. Use a practical way forward only for questions that genuinely require one.
  10. **Factual and presentation discipline:** no fabricated names, dates, data or quotations;
      maintain readable paragraphs/bullets, visible hierarchy, concise language and word-limit
      proportionality.
- **Evidence is compulsory in every solved answer and framework (strengthened 12 August 2026):**
  every solved Mains PYQ, original 10/15/20-mark model answer, answer framework and essay model
  must use relevant named evidence linked to the argument. Use **claim -> named evidence/example
  -> what it proves -> limitation/qualification**; evidence must never be decorative or merely
  listed. History answers should draw, as appropriate, on precise texts/authors, inscriptions,
  coins, sites, excavations, material remains, travellers, archaeological/scientific findings,
  historians and regional comparisons. Each solved answer must end with a concise
  **“Why this earns marks”** note. Never invent a fact, quotation, date, site, text, scholar,
  report, datum or official answer key to satisfy this requirement.
- **Model-answer review rubric:** internally review every answer for demand fulfilment (20%),
  accurate content and named evidence (30%), analysis and linkage (20%), structure and coherence
  (15%), balance and conclusion (10%), and presentation/value addition (5%). Revise any model
  answer that remains generic, lacks named examples, lists facts without inference, or fails to
  answer the directive. The final PDF/workbook should also state a short “Why this earns marks”
  note after each solved answer.
- **Compact visual-layout rule (saved 13 August 2026):** visuals are content-sized by default and
  must not be forced onto a whole page merely for presentation. Prefer inline, half-page,
  two-column/paired, or visual-plus-explanation layouts. A full-page visual is allowed only when
  complexity or legibility genuinely requires it (for example, a dense map, comprehensive concept
  map or large timeline), and it must not leave excessive unused space. Keep the related caption
  or explanation on the same page where possible. Validate page-space efficiency and reject
  isolated diagrams surrounded by avoidable blank areas.
- **Generated visual-asset rule (saved 14 August 2026):** complete topic packages must generate
  and embed original topic-specific visual assets wherever they materially improve understanding:
  labelled diagrams, schematic maps, timelines, causal/process flows, concept maps, comparison
  infographics, charts and process illustrations. Do not rely only on styled text boxes or
  tables. Select each visual by learning purpose, keep labels legible, add a concise caption,
  validate factual and geographical accuracy, and use externally sourced images only with
  appropriate attribution and licensing.
- **Continuous at-a-glance flowchart rule (saved 22 August 2026):** every topic flowchart is one
  continuous logical diagram even when it spills across pages. Each primary node must contain the
  heading, decisive short context, exact important terms/details, and the consequence or contrast.
  Never defer an essential qualifier to a later page. For example, state which pramanas
  (means of valid knowledge) Carvaka accepts/rejects and contrast Nyaya in the same doctrine flow;
  state the exact civil, military, revenue/political control associated with Pitt's India Act and
  the Court of Directors' commercial role; state that the 1858 Act ended Company rule and began
  Crown rule with the replacement institutional structure. Validate by reading only headings,
  arrows and highlighted keywords: if the full distinction cannot be reconstructed at a glance,
  regenerate the chart. Extra information is allowed, but the complete high-yield spine must come
  first and receive the strongest visual emphasis: definitions, accepted/rejected positions, exact
  functions or powers, mechanisms, dates, consequences, comparisons and UPSC traps. Enrichment
  must remain visually subordinate and cannot displace or repair a missing core point.
- **User-approved Cārvāka reference design (approved 22 August 2026):** the flowchart under
  `notes\Philosophy\flowcharts\philosophy-paper-i-indian-philosophy-01\continuous-at-a-glance-core-first\`
  is the mandatory visual reference for future learner-v2 topic flowcharts. Preserve its dark
  high-contrast canvas, continuous cyan stage rail, numbered stages, coloured decisive-keyword
  pills, highlighted answer-line bands, primary-core dominance, subordinate enrichment and
  same-master overlapping tiled pages. Every `Generate learner-v2 topic: ...` command now produces
  four integrated outputs: reusable Markdown, indexed learning PDF, indexed solved workbook, and
  this continuous core-first flowchart package (master image + large poster + tiled PDF + previews).
- **Subtopic-closure flow rule (saved 22 August 2026):** immediately after every completed teaching
  subtopic in the learning-session PDF, insert a compact flow diagram:
  `heading -> exact key terms -> mechanism/argument -> consequence/contrast -> UPSC trap/answer-use`.
  It must include the subtopic's answer-grabbing formulation, appear before the next subtopic begins,
  and cannot be deferred to a consolidated section at the end.
- **Topic-specific final register-note rule (saved 13 August 2026):** final revision/register
  notes must use topic-specific headings rather than a fixed notes template. Do not force
  `Introduction` or `Origin` sections. Include origin/background only when it is an examinable
  dimension of the topic and name it precisely (for example, `Transition to Food Production`,
  `Formation of the Persianate World`, or `Evidence Base and Dating`). Register notes are
  compressed revision notes, not a second repetition of the teaching introduction. They must
  still cover every subtopic, but prioritise definitions, chronology, evidence/examples, causal
  logic, comparisons, debates, traps, PYQ routes, answer frameworks and rapid-recall facts.
  Avoid repeating introductory prose already taught earlier.
- **Reusable Markdown rule (all subjects):** retain a complete Markdown edition of an interactive
  learning session under `knowledge/<Subject>/learning-sessions/`. It must omit tool logs but keep
  the taught wording and ordering unchanged. Canonical synthesized topic files may remain in their
  existing syllabus folders.
- Never split tables, facts/traps panels, memory hooks, diagrams, Mains-angle
  panels or Study-link panels across pages. Keep all diagram text inside
  measured nodes or bounded detail cards.
- Use `tools/upsc_register_pdf.py` and its optional `concept_map`, `flow_diagram`, `memory_hook`,
  `link_map`, and `generated_image` fields.
- Use Azure GPT Image only for conceptual illustrations, historical ambience, and visual
  metaphors. Keep maps, constitutional structures, scientific diagrams, timelines, and
  quantitative charts deterministic. Every generated image must include a caption and the
  renderer's AI-generated/non-factual-evidence label.
- Generate images through `tools/azure_image_generator.py`; credentials must come only from
  ignored environment configuration and must never appear in source, prompts, logs, PDFs, or
  generated Markdown.
- Validate the final PDF for content coverage, empty pages, clipping, overlap, and unsupported
  glyphs. Delete the temporary `_data.py` module only after successful generation.
- Save Philosophy PDFs under the correct category folder inside `notes/Philosophy/`.

### Final-learning-package deep content review standard (saved 27 August 2026)

- Review work under `notes\Final-Learning-Packages\` must evaluate all four topic artifacts:
  the complete learning session, solved workbook, Cārvāka-style graphical flowchart, and ASCII
  master flowchart. A package cannot pass merely because files exist, open, or render cleanly.
- The complete learning session must be checked against the official syllabus, complete Basic/Core
  owners, relevant cross-topic owners, Advanced owners, verified PYQs, and current evidence where
  useful. It must provide a learner-friendly beginning, explicit goals, complete core teaching,
  must-remember lines, examinable origin/timelines where relevant, verified evidence units,
  answer-grabbing lines, UPSC traps, current-affairs integration with source/date/status discipline,
  and a clearly optional advanced block that is not required for a core answer.
- The solved workbook must be reviewed for complete verified PYQ coverage, directive fidelity,
  examiner-grade model answers, named evidence, analysis, qualification, better-answer guidance,
  and hard MCQs covering the topic and its close-option neighbourhood. If repository PYQ ledgers
  are incomplete, verify missing questions through official UPSC sources or reliable web evidence;
  never invent wording, year, marks, or an official key.
- Review both master-flow representations independently. The graphical flowchart must preserve the
  complete core spine, readable learning order, decisive evidence, traps, comparisons, PYQ-tested
  distinctions and visually subordinate advanced enrichment. The ASCII flowchart must preserve the
  same facts and complete examinable logic with exact terminology, dates, provisions, thinkers,
  evidence, limits and answer-writing routes. Reconcile factual agreement across the session,
  workbook, graphical flowchart and ASCII flowchart.
- Data verification is a hard gate. Record the source, date, status and uncertainty for current,
  legal, constitutional, historical, geographical, philosophical and quantitative claims. A
  material factual error, fabricated PYQ/key, unsupported quotation, or contradictory artifact
  prevents passage regardless of the aggregate score.
- Knowledge Markdown has already undergone repeated review. During package review, do not edit it
  automatically. Record any required Markdown repair as a precise suggestion with owner path,
  affected output, evidence and proposed change; apply it only under a separate repair command.
- Maintain the review instructions, plan and per-topic tracker in the dedicated folder
  `notes\Final-Learning-Packages\_deep-content-review\`.

---

## 6. Study tracking (dates & methods)

- **Start dates:** CA daily = **6 June 2026** · MCQ daily practice = **9 June 2026** ·
  Mains answer writing (1/day) = **9 June 2026** · Essay (1/week, Sunday) = **9 June 2026**.
- **Daily Mains (20 min):** 2 min read+directive, 2 min outline, 12 min write, 4 min self-evaluate on
  Content /3 · Structure /2 · Multidimensionality /3 · Language /2 = **/10**.
- **Essay (weekly, Sunday):** 3 stages — Deconstruct (5 min: hidden assumption, both sides, verdict) →
  Build Spine (10 min: narrative arc, not a point list) → Write with philosophy (optional edge:
  Rawls, Sen, biocentrism, etc.).

---

## 7. Ingestion (adding new PDFs)

- Drop PDF in the correct subfolder of `books/`; run `python ingestion/ingest.py`.
  Already-ingested files are skipped via checkpoint (`vectordb/static/checkpoint.json`).
- **Folder-aware subject tagging** (`ingest.py` → `infer_subject`):
  - `books/mains/` → `Mains PYQ`
  - `books/philosophy_optional*/` → `Philosophy PYQ`
  - `books/prelim*/` → `CSAT PYQ` if "csat" in filename, else `Prelims PYQ`
  - else → fall back to `SUBJECT_KEYWORDS` filename matching.
- **OCR caveat:** scanned bilingual PYQs are OCR'd **English-only** → Hindi/Devanagari comes out
  garbled. Use the clean English half; ignore garbled Hindi when querying these PYQs.

---

## 8. Verified facts & corrections

- **JPN Bird Sanctuary** = Jai Prakash Narayan Bird Sanctuary (a.k.a. **Surha Tal**), **Ballia district, UP**.
  India's **100th Ramsar site**, announced **5 June 2026** (World Environment Day).
  NOT Jagdishpur–Phulhar–Nawabganj.
- **Jagdishpur (Sultanpur), Phulhar (Bahraich), Nawabganj (Unnao)** are **three separate** Ramsar sites
  in UP — do **not** call them a single "JPN complex".
- **Misri vs First Secretary (The Hindu, 20 June 2026) — KEEP SEPARATE (two distinct stories):**
  1. **Parliamentary Standing Committee on External Affairs** (Chair: **Shashi Tharoor**) questioned
     **Foreign Secretary Vikram Misri** on the government's Pakistan **engagement** policy
     (people-to-people ties, SCO summit, Track-II) — trigger was **RSS advocacy** for keeping the
     window open; meeting was a pre-tour briefing before the panel's J&K/Ladakh study tour (Jun 22–25).
  2. **First Secretary Anupama Singh** (India's UN Permanent Mission) called Pakistan a
     **"Frankenstein state"** at the UN (rebutting Pakistan + OIC on J&K).
  The panel did **NOT** question Misri about the First Secretary's UN remark. Do not link them.

---

## 9. Knowledge semantic-completeness review

- **Goal:** no gaps, no missing data, no missing topic and no missing subject.
- The crash-resumable human tracker is
  `KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`; the authoritative machine state is
  `upsc-ai-kit\manifests\reviews\knowledge-semantic-completeness-status.json`.
- Review exactly one subject and one topic at a time. Philosophy Optional comes first because it
  has a confirmed Buddhism coverage gap; remaining subjects follow the authoritative topic
  catalogue order.
- Every topic requires four independently built ledgers: literal syllabus, indispensable
  prerequisites, standard textbook taxonomy and complete PYQ demands.
- Existing audits, keyword checks, exports and PDF validation are evidence only. A topic passes
  only after a hostile search for absent doctrines, thinkers, mechanisms, classifications,
  exceptions, comparisons, criticisms and demand families.
- Repair the canonical Basic/Core owner first. Regenerate dependent sessions, workbooks,
  flowcharts and PDFs only after the owner passes.
- After any status update, regenerate the human tracker with:
  `python tools\generate_semantic_completeness_tracker.py`.
- Universal recovery command:
  `Resume semantic-completeness review from KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md`.
