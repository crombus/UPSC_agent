# UPSC Agent Repository Instructions

`AGENT_MEMORY.md` is the repository's authoritative saved workflow. Read and follow it before
teaching, generating exams, or creating PDFs. If another instruction conflicts with it, use the
newer rule in `AGENT_MEMORY.md`.

## Universal Completion Report

After **every completed user command**, the final response must list the exact repository-relative
path of every file created or modified while completing that command. If no files changed, state
`Files changed: none`. This applies to audits, knowledge edits, trackers, tools, exams, notes and
PDF work—not only exports.

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
2. Build the complete multi-subtopic learning session even if it was not previously taught
   interactively.
3. Create a detailed main PDF containing all teaching, innovative diagrams, terminology,
   examples, criticisms/replies, advanced refinements, solved PYQs, MCQ/remedial loops, and
   solved Mains practice.
4. End the main PDF with complete consolidated register notes covering every subtopic.
5. Create a separate workbook with all relevant solved PYQs, MCQs covering nearly every
   subtopic, remedial MCQs, and original 10/15/20-mark Mains questions with model solutions.
   Every model answer must follow the examiner-grade standard in `AGENT_MEMORY.md`, including
   directive fidelity and the pattern **claim → named evidence/example → analysis → qualification**.
6. Rotate MCQ keys strictly A → B → C → D.
7. Save a cleaned reusable Markdown edition in the relevant
   `upsc-ai-kit\knowledge\<Subject>\` area.
8. Validate coverage, layout, glyphs, answers, rotation, and final register-note placement.
9. Record all three deliverable paths in `EXPORT-PDF-STATUS.json`, regenerate
   `EXPORT-PDF-COMMAND-INDEX.md`, and mark `approved: true` only after explicit user approval.
10. After every export completes, the final response must list the exact path of every file
    created or modified by that export. This reporting requirement does not change approval:
    generated packages remain `approved: false` until the user explicitly approves them.

Do not apply the quick `Notes` rule that excludes MCQs to a complete topic package or
`Export PDF`.

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
