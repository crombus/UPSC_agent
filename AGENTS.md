# UPSC Agent Repository Instructions

`AGENT_MEMORY.md` is the repository's authoritative saved workflow. Read and follow it before
teaching, generating exams, or creating PDFs. If another instruction conflicts with it, use the
newer rule in `AGENT_MEMORY.md`.

## Universal Completion Report

After **every completed user command**, the final response must list the exact repository-relative
path of every file created or modified while completing that command. If no files changed, state
`Files changed: none`. This applies to audits, knowledge edits, trackers, tools, exams, notes and
PDF work—not only exports.

## Quick-Glance Tree Charts

- Trigger: `Export Tree Chart: <Subject> — <Topic>` or a request to export/create a concise tree
  chart for a specific topic.
- Create a concise, continuous, terminal-friendly tree derived from the topic's canonical Basic
  owner, Advanced owner and relevant verified PYQs. This quick-glance artifact is distinct from
  the data-complete ASCII Master Flow Diagram and the graphical flowchart package.
- Preserve the topic's high-value definition, classifications/actors, causal or operating
  mechanism, major provisions/institutions, response framework, close-option distinctions,
  examiner traps, PYQ answer route and qualified conclusion. Prefer branches and arrows over
  explanatory paragraphs, while retaining exact examinable dates, articles, sections and names.
- Save it as Markdown under
  `quick_galance\<Subject>\<topic-number-or-key>_<Topic-Title>_Tree-Chart.md`, creating the subject
  folder when needed. Use the repository's established subject spelling.
- A quick-glance export does not satisfy or replace either mandatory master-flow representation
  required for `Notes`, a complete learning session or `Export PDF`.
- **Whole-knowledge-base atlas:** the active atlas covers every source-ready topic in
  `upsc-ai-kit\manifests\v2\topic-catalog.json` except Essay, CSAT, Qualifying English and
  Qualifying Hindi. Process topics strictly in catalogue order and finish one chart before
  starting the next.
- Do not batch-generate chart content, use a fast/generic template, compress source coverage or
  mark a topic complete from an outline. Read that topic's complete canonical Core/Basic owner,
  Advanced owner and relevant verified PYQs, author its topic-specific tree, save it, then refresh
  `quick_galance\TREE-CHART-INDEX.md` and `quick_galance\TREE-CHART-STATUS.json`.
- `tools\generate_quick_glance_index.py` may regenerate only the inventory and completion status;
  it must never generate chart content.
- `Continue Quick-Glance Atlas` resolves `next_pending` from
  `quick_galance\TREE-CHART-STATUS.json` and generates exactly that one topic. It must not skip
  ahead or generate multiple topics in one invocation.
- While the quick-glance atlas is active, the standalone command `Next` is an exact alias for
  `Continue Quick-Glance Atlas`: resolve and generate only the first pending topic.
- After every successfully completed atlas topic, include the exact next copy-ready
  `Export Tree Chart: ...` command in the final response. If no topic remains, state that the atlas
  is complete instead.
- Keep the copy-ready pending queue at `quick_galance\TREE-CHART-COMMAND-INDEX.md`; regenerate it
  together with the completion index after every completed chart.

## Compact Visual Layout

- Visuals are content-sized by default; never force a diagram to occupy a whole page merely for
  presentation.
- Prefer inline, half-page, two-column/paired, or visual-plus-explanation layouts.
- Use a full-page visual only when complexity or legibility genuinely requires it, such as a dense
  map, comprehensive concept map or large timeline, and do not leave excessive unused space.
- Generate and embed original topic-specific visual assets wherever they improve learning:
  labelled diagrams, schematic maps, timelines, causal/process flows, concept maps, comparison
  infographics, charts and process illustrations. Do not rely only on styled text boxes or tables.
- Match each visual to its learning purpose, keep labels readable, add a concise caption, and
  verify factual and geographical accuracy. Use externally sourced images only with appropriate
  attribution and licensing.
- Keep the related caption or explanation on the same page where possible.
- Validate page-space efficiency and reject isolated diagrams surrounded by avoidable blank areas.

## Final Register-Note Structure

- Final revision/register notes must use topic-specific headings rather than a fixed notes
  template.
- Do not force `Introduction` or `Origin` sections. Include origin/background only when it is an
  examinable dimension of the topic, and name it precisely—for example, `Transition to Food
  Production`, `Formation of the Persianate World`, or `Evidence Base and Dating`.
- Register notes are compressed revision notes, not a second repetition of the teaching
  introduction.
- They must still cover every subtopic, while prioritising definitions, chronology,
  evidence/examples, causal logic, comparisons, debates, traps, PYQ routes, answer frameworks and
  rapid-recall facts.
- Avoid repeating introductory prose already taught earlier in the package.

## Complete Topic Package

Triggers:

- `Create Topic Package: <Subject> — <Topic>`
- `Export PDF` for the current topic/session

For either trigger:

1. Use sources in this order: Markdown knowledge files, OCR-searchable PDFs, live current
   affairs, then Qdrant only as an optional fallback.
2. Build the complete easy-to-understand Guided Tutor learning session even if it was not
   previously taught interactively. Cover the `basic/` owner completely first in its natural
   teaching order, with visual -> simple explanation -> example -> exam link -> traps -> recap.
   Do not interleave Advanced material into the Basic session.
3. Create a mandatory separate **CONTINUOUS AT-A-GLANCE MASTER FLOWCHART** using this approved
   design-intelligence reference:
   `notes\Polity\flowcharts\polity-01\continuous-at-a-glance-carvaka-standard-g9`.
   This is not satisfied by an ASCII diagram embedded inside the notes PDF. For every topic:
   - build one continuous, numbered visual rail that maps the complete topic end to end;
   - include every major chronology stage, provision, institution, doctrine, process, mechanism,
     causal link, limitation, comparison and PYQ-tested close-option distinction;
   - complete the full Basic/core spine before a visually subordinate optional enrichment stage;
   - choose a bespoke internal layout for each stage—chains, matrices, timelines, replacement
     diagrams, ladders, panels or comparisons as the content demands. Never repeat a generic
     three-column card across all stages;
   - use dense decisive keyword pills, mechanism/bridge bands, traps/limits and unique
     answer-grabbing lines, while keeping the continuous rail readable;
   - study the Basic owner, Advanced owner, relevant PYQ ledgers and cross-owned evidence before
     authoring the flowchart. Do not omit a tested detail merely because it appears minor;
   - generate a high-resolution master canvas, a one-page poster PDF, and a tiled printable PDF
     cropped from that exact same master with overlap. Save previews/contact sheets and a
     validation report in a self-contained topic flowchart folder;
   - match the g9 reference's design intelligence and quality controls, not its Polity-01 content
     or stage template. The flowchart remains `approved: false` until explicitly approved.
   The graphical package is one of two mandatory master-flow representations. It does not replace
   the text-native representation defined below.
4. Add a mandatory **ASCII MASTER FLOW DIAGRAM** to the reusable Markdown and main notes/learning
   PDF. Also save the same diagram as a standalone `.txt` or `.md` artifact beside the graphical
   flowchart package. This is the terminal-friendly, data-complete format exemplified by
   `Polity 03 — Salient Features Flow Diagram`; it is distinct from the designed PNG/PDF package.
   For every topic:
   - construct one continuous top-to-bottom logical flow using branches, arrows, bounded panels,
     comparison tables, timelines or hierarchies as the topic requires;
   - preserve the complete examinable spine, not a compressed decorative summary: definitions,
     classifications, chronology, exact terminology, constitutional articles/amendments/cases,
     doctrines, philosophers, mechanisms, causal links, institutional powers, consequences,
     objections/replies, comparisons, limits, exceptions and PYQ-tested minor facts must appear
     whenever owned by the sources;
   - organise the flow in learning order: central question or starting condition -> conceptual
     axes/definitions -> complete core sequence -> mechanisms and relations -> comparisons and
     criticisms -> consequences -> examiner traps/PYQ anchors -> answer-writing spine and qualified
     conclusion;
   - use exact numbers, dates, article/part/schedule references, technical terms and named evidence
     where relevant. Do not replace them with vague labels merely to shorten the diagram;
   - keep related distinctions together so the reader can reconstruct the answer by following only
     the headings, arrows, branch labels and high-yield facts;
   - validate the ASCII diagram and graphical package independently against the same Basic,
     Advanced and PYQ coverage ledger. They must agree factually, but may use different visual
     grammars. Neither representation is a substitute for the other.
5. Create a detailed main PDF containing all teaching, innovative diagrams, terminology,
   examples, criticisms/replies, advanced refinements, solved PYQs, MCQ/remedial loops, and
   solved Mains practice.
6. Keep the established answer and practice sections unchanged. After the complete Basic session
   and its exam application, place all material from the `advanced/` owner in a separate final
   teaching block labelled **OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER**. Advanced
   content is enrichment, not a prerequisite for understanding or writing the core answer.
7. End the main PDF with complete consolidated register notes covering every subtopic while
   preserving the Basic/Optional-Advanced distinction.
8. Create a separate workbook with all relevant solved PYQs, MCQs covering nearly every
   subtopic, remedial MCQs, and original 10/15/20-mark Mains questions with model solutions.
   Every model answer must follow the examiner-grade standard in `AGENT_MEMORY.md`, including
   directive fidelity and the pattern **claim → named evidence/example → analysis → qualification**.
9. Rotate MCQ keys strictly A → B → C → D.
10. Save a cleaned reusable Markdown edition in the relevant
   `upsc-ai-kit\knowledge\<Subject>\` area.
11. Validate both master-flow representations against the Basic owner, Advanced owner and PYQ
    ledgers. For the ASCII diagram, check logical continuity, exact-data retention, branch
    readability, complete core sequence, comparisons, traps, PYQ anchors and agreement with the
    graphical package. For the graphical package, check stage order/completeness, layout diversity,
    information density, required terms,
    overflow, poster integrity, tiled-PDF same-master pixel identity, overlap, previews/contact
    sheets and source/reference immutability. Then validate notes/workbook coverage, layout,
    glyphs, answers, rotation, and final register-note placement.
12. Record all deliverable paths in `EXPORT-PDF-STATUS.json`, regenerate
   `EXPORT-PDF-COMMAND-INDEX.md`, and mark `approved: true` only after explicit user approval.
13. After every export completes, the final response must list the exact path of every file
    created or modified by that export. This reporting requirement does not change approval:
    generated packages remain `approved: false` until the user explicitly approves them.

Do not apply the quick `Notes` rule that excludes MCQs to a complete topic package or
`Export PDF`.

## Learner-First V2 Export Convention

- Learner-v2 is the approved default for all new exports. This approves the workflow, not every
  topic output: an exact topic variant/generation remains unapproved until the user explicitly
  approves that topic.
- Build one assembled learner-facing Markdown and render v2 PDFs from it with
  `tools\markdown_learning_pdf.py --variant learner-v2`; do not render the main PDF from a
  separate compressed summary.
- Every learner-v2 notes PDF and every learner-v2 workbook PDF must generate its own internal
  contents/index directly after the cover/title/front matter and before teaching or questions.
  Derive it automatically from meaningful headings, use accurate final page numbers, and prefer
  matching PDF bookmarks. Do not make topic authors maintain page numbers or list every tiny
  utility heading. Notes and workbook indexes must reflect their own distinct contents.
- Use these H2 sections in order: `BASIC LEARNING SESSION`,
  `BASIC MCQS / REMEDIATION`, `PYQS AND ANSWER PRACTICE`,
  `OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER`, and
  `CONSOLIDATED REGISTER NOTES`. The last one must remain the final H2.
- Work subject-wise and section-wise. Before generating a user-supplied section, enumerate its
  complete topic list from the official syllabus and repository owners, create/update the section
  manifest, and present/record the coverage index with planned topics, source owners, status and
  deliverables.
- After the section plan is fixed, default user-facing execution is a manifest-ordered queue of
  one-topic commands, not a whole-section batch. Use the exact syntax
  `Generate learner-v2 topic: <Subject> — <Section name or key> — <Topic display title>`.
  Each command must generate, validate and finalise that topic and refresh the tracker, global
  coverage, section coverage, notes-PDF and workbook-PDF indexes before the next topic begins.
  The full-section command remains available for explicit batch requests, but is not recommended
  by default. Supported topic suffixes are `— Regenerate`, `— Generate index only`, and
  `— Pause after generation before finalising`; include one only when its stated behaviour is
  meaningful.
- For a bounded automatic queue, use the exact syntax
  `Generate next 10 learner-v2 topics: <Subject> — <Section name or key>`. Resolve the
  catalogue and manifest; select the next 10 planned or incomplete topics in manifest order;
  exclude successfully generated and validated topics unless the command explicitly ends with
  `— Regenerate`; and process strictly one topic at a time. After each topic, validate, finalise
  the tracker, and refresh the global command index plus section coverage, notes-PDF and
  workbook-PDF indexes. Stop immediately on the first failure or ambiguity without generating or
  marking later topics complete. If fewer than 10 remain, process all remaining topics. Topic
  approval stays false until explicit approval of that exact generation.
- Completeness must combine the official syllabus, Basic/canonical Markdown, relevant
  cross-topic/thematic Markdown, available verified PYQs and Advanced Markdown last. Markdown is
  the source of truth; OCR PDFs and live sources supplement it.
- Preferred new paths are
  `upsc-ai-kit\knowledge\<Subject>\learning-sessions\v2\<section-key>\<topic-key>_Learning-Session.md`,
  `notes\<Subject>\learning-session-v2\<section-key>\notes\`,
  `notes\<Subject>\learning-session-v2\<section-key>\workbooks\`, and
  `notes\<Subject>\learning-session-v2\<section-key>\indexes\`. The index folder contains separate
  `TOPIC-COVERAGE-INDEX.md`, `NOTES-PDF-INDEX.md`, and `WORKBOOK-PDF-INDEX.md` files. Existing
  topic-folder v2 pilots and all v1 paths remain immutable compatibility paths. These external
  section indexes track progress and deliverable files; they do not replace the internal index in
  either PDF.
- `V2-SUBJECT-SECTION-COMMAND-INDEX.md` is the authoritative human-facing guide for section
  requests. Its command catalogue is generated from
  `upsc-ai-kit\manifests\v2\topic-catalog.json` and covers every source-ready topic discovered
  from repository owners and syllabus/index mappings, not only registered pilots. It must group
  exact one-topic commands by subject and the narrowest unambiguous section, preserve source
  order, append `— Regenerate` only for an existing learner-v2 generation, and withhold unresolved
  topics in a separate appendix. Registered-manifest detail may follow the complete catalogue.
- A valid catalogue topic command does not require a pre-existing section manifest. Resolve the
  catalogue entry, materialise the complete section manifest and its coverage/notes/workbook
  indexes on demand, then generate only that requested topic. The user must never create JSON
  manually. Regenerate deterministically with
  `python tools\generate_v2_topic_command_catalog.py --guide`.
- Use `tools\generate_v2_section_indexes.py` to create/refresh section indexes. A safe post-topic
  operation may use `tools\finalize_v2_topic.py` to validate known outputs, upsert the supplied
  schema-v2 tracker record, regenerate the global command index and refresh section indexes. It
  must never fabricate or autonomously generate teaching content.
- `learning-sessions\` is canonical. `Terminal-Learning-Sessions`, `learning-sessions-v2` and
  `_learning-sessions` are read-only migration aliases.
- Tracker identity is `topic_key + variant + generation`; approval never crosses records.
  Record Basic/Advanced owners, assembled Markdown, renderer name/version, generation date,
  superseded v1 identity (when present), and `supersedes`. Deleting only v2 paths and records
  must restore the v1-only state.
- **Philosophy learner-v2 override:** preserve all five legacy content kinds, but reorder them
  across the package rather than interleaving them per subtopic. Put every `SIMPLE START` and
  `CORE UPSC` point for all logical subtopics in `BASIC LEARNING SESSION`; put `EXAM APPLICATION`
  and `RAPID REVISION` material in the two practice sections; put every `ADVANCED` point only in
  `OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER`; keep consolidated register notes
  last. This override applies only to `learner-v2`; legacy-v1 Philosophy files retain the
  five-layer-per-subtopic sequence and remain immutable.

## Philosophy-Only Layered Notes and Export

For Philosophy, the ordinary `Notes` and `Export PDF` commands use a mandatory five-layer
architecture for every logical subtopic:

1. **SIMPLE START** — plain-language explanation and a concept-appropriate visual.
2. **CORE UPSC** — complete terminology, doctrine, arguments, examples and source grounding.
3. **ADVANCED** — objections, replies, comparisons, interpretive issues and refinements.
4. **EXAM APPLICATION** — verified PYQs, demand decoding and 10/15/20-mark answer structure.
5. **RAPID REVISION** — traps, consolidated recall notes and MCQs with explanations.

`Philosophy Notes: <Topic>` is an explicit alias for a single layered notes PDF plus reusable
Markdown. `Export Philosophy PDF: <Topic>` is an explicit alias for the full three-deliverable
package: layered main PDF, separate solved workbook and reusable Markdown.

Preserve all existing substantive material when converting an older Philosophy session. Reorder
it into the layers and add simple visual gateways, but do not compress or delete it. An explicitly
requested verbatim transcript remains in its original order.

All common all-subject package, practice, visual, validation and register-note rules remain
binding. Philosophy adds these subject-only requirements:

- Use **English-first terminology** throughout notes, PDFs, Markdown, workbooks, diagrams and
  model answers. The English concept is the main expression; place the accurate Sanskrit or Pali
  IAST term immediately afterward in parentheses, for example `dependent origination
  (pratītyasamutpāda)` and `Middle Path (madhyamā pratipad; Pali: majjhimā paṭipadā)`.
- Do not lead with an unexplained Sanskrit/Pali term except in a verbatim quotation or explicit
  linguistic analysis; provide the English gloss immediately even in those exceptions.
- Treat the official syllabus as the minimum coverage spine. Include indispensable doctrines
  needed to understand the named terms and PYQs even when the doctrine is not separately printed
  in the syllabus clause.
- For Buddhism, substantial coverage must include the practical Middle Path between sensual
  indulgence and self-mortification through the Noble Eightfold Path (āryāṣṭāṅgamārga), as well
  as the doctrinal middle between eternalism and annihilationism. Connect both to the Four Noble
  Truths, dependent origination and liberation; a passing mention is insufficient.
