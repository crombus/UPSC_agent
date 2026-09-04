# PDF Learning Session Standard

Use this standard whenever the user asks for a PDF learning session, topic package,
exported learning session, or complete visual revision package.

## Learner-v2 topic-command output contract

Every command in the form:

`Generate learner-v2 topic: <Subject> — <Section> — <Topic>`

must generate and integrate all four deliverables:

1. Complete reusable learning-session Markdown.
2. Complete indexed learning-session PDF.
3. Separate indexed solved-practice workbook.
4. Continuous at-a-glance core-first flowchart package using the approved
   Cārvāka reference design described below.

The flowchart package includes a high-resolution master image, a one-page
large-format poster PDF, and a print-readable tiled continuation PDF with page
previews and contact sheets. A topic command is incomplete if any of these four
deliverables is missing.

## Core principle

- A flowchart or learning visual may continue across multiple pages.
- Never omit major exam-relevant content merely to fit a fixed page count.
- Prefer readable continuation pages over one overcrowded poster.
- Begin with a master learning sequence and expand each stage in logical order.
- A user-approved flowchart is an immutable visual baseline. Future learner-v2
  generation may enrich its content only within the approved design language;
  it must not replace the approved layout, sequencing, page architecture or
  visual style without explicit user permission.
- If an alternative expanded rendering is generated, preserve it in a clearly
  named subfolder and keep the approved version at the canonical flowchart path.

## Canonical folder structure

Keep every learner-v2 topic inside its subject and syllabus-section hierarchy.
Do not place generated artifacts directly in a subject root when a section and
topic folder can be resolved.

```text
upsc-ai-kit\knowledge\<Subject>\<Section>\learning-sessions\<Topic>\
  <Topic>_Complete-Learning-Session_<date>.md
  <Topic>_Solved-Practice-Workbook_<date>.md
  assets\

notes\<Subject>\<Section>\learning-sessions\<Topic>\
  <Topic>_Complete-Learning-Session_<date>.pdf
  <Topic>_Solved-Practice-Workbook_<date>.pdf
  PACKAGE-VALIDATION-REPORT.txt

notes\<Subject>\<Section>\flowcharts\<NN_Topic>\
  continuous-at-a-glance-carvaka-standard-g<N>\
    master image
    poster PDF
    tiled PDF
    editable sources
    previews
    validation report
```

- Reuse the canonical topic folder for later generations. Distinguish revisions
  through tracker generations and dated filenames rather than competing trees.
- Store the embedded teaching-navigation diagram in the Markdown topic's
  `assets` folder.
- Store the standalone continuous Cārvāka-style flowchart only in the separate
  `flowcharts` hierarchy.
- Legacy/reference artifacts may remain, but new learner-v2 outputs must use
  this canonical structure.

## Mandatory source order

1. Repository Markdown knowledge owners.
2. OCR-searchable local books and source PDFs.
3. Live current-affairs sources where genuinely relevant.
4. Qdrant only as an optional fallback.

## Complete learning-session PDF

The main PDF must include:

1. Topic definition, scope, syllabus mapping and source caution.
2. A master roadmap or flowchart showing the complete learning sequence.
3. Detailed subtopic teaching in natural learner order.
4. Definitions, classifications, components and technical terminology.
5. Chronology, evolution, mechanisms and cause-effect chains where applicable.
6. Arguments, derivations, assumptions and philosophical or constitutional logic.
7. Objections, criticisms, replies and balanced evaluation.
8. Comparisons with related thinkers, schools, institutions or constitutional models.
9. India-centric examples and bounded current-affairs linkage where relevant.
10. Prelims facts, close-option distinctions, common traps and mnemonics.
11. Mains themes, answer structures, introductions, conclusions and verdicts.
12. Highlighted answer-grabbing lines for definitions, core arguments,
    criticisms and conclusions.
13. Verified solved PYQs.
14. Diagnostic MCQs and remedial practice with explanations.
15. Original 10-, 15- and 20-mark Mains questions with model solutions.
16. Complete consolidated register notes as the final section.
17. A **subtopic-closure flow diagram immediately after every completed
    teaching subtopic**, before the next subtopic begins.

### Named major-session navigation contract

Every major teaching unit must be a consistently numbered H3 heading:
`SESSION <N> — <THINKER / SCHOOL / CONCEPT>`. The renderer must display these
headings as prominent full-width session bands, and the heading text must make
the taught doctrine obvious both while scanning pages and through PDF search.

Immediately below every named session heading, include:

1. `DEFINITION / WHAT THIS IS CALLED` with a plain-language definition followed
   by a technically precise definition that explicitly names the doctrine/model.
2. `ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM` with one or two accurate,
   analytical sentences that directly answer the likely demand.
3. `MUST-WRITE KEYWORDS` with exact thinker/school terminology and a short
   `How to use them` instruction.
4. A compact closing recall flow at the actual end of the session, before the
   next numbered session begins:
   `starting concept -> exact terms -> mechanism/argument -> consequence ->
   criticism/trap -> answer-use`.

Number sessions continuously across the Basic teaching sequence. Do not hide a
major thinker inside generic labels such as `Part I`, `Module`, or `Visual`.

### Final complete-topic ASCII master flow

The reusable Markdown and main learning PDF must contain a text-native
`COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM` inside
`CONSOLIDATED REGISTER NOTES`, after the compressed registers, so consolidated
revision material remains the package's final section. It is additional to both
the early embedded navigation graphic and the separate continuous graphical
flowchart package.

- The mandatory visual/pedagogical topology reference is the approved
  **Notions of God** master beginning at the same heading in
  `upsc-ai-kit\knowledge\Philosophy\Philosophy-of-Religion\learning-sessions\Notions-of-God\Notions-of-God_Uncompressed-Complete-Learning-Session_2026-08-22.md`.
  Use its ten-panel conceptual-atlas logic as the design reference, not its
  Philosophy content.
- A compliant master normally contains **6–12 topic-designed panels**, each
  headed exactly:
  `#### ASCII MASTER FLOW — PANEL X/N: <specific title>`.
  Each heading owns one separate `ascii-master` fenced block.
- Active packages require a **manually authored and reviewed topic-specific
  panel atlas**. The four dated specs under
  `upsc-ai-kit\manifests\retrofits\ascii-panel-specs\` are authoritative for
  the current 40-topic set; preserve their titles, order and authored lines
  exactly. The approved Notions-of-God ten-panel master remains the reference.
  Automatic session summaries or heuristic panels may be used only as
  unfinalized development drafts and must never become a latest tracker record
  without explicit manual review and approval.
- Begin with a central question/root concept and analytical axes. Continue
  through topic-appropriate classifications, chronology, process or argument
  trees, causal chains, spatial zones/cross-sections, institutional
  checks/balances, comparisons, objections/replies, problems/responses and
  applications. End with an integrated revision and answer-writing spine for
  the exact topic.
- Group related teaching sessions into conceptual panels. **Never** emit one
  panel or one repeated card per numbered teaching session.
- The following old topology is prohibited:
  `+-- SESSION NN -> definition -> mechanism -> consequence -> trap`.
  A vertical session-card summary is not a complete-topic master, even when it
  contains every session and passes a presence/count check.
- Use genuine branching and convergence with `┌ ┬ ┴ ┐ └ ─ │ ▼` or safe ASCII
  equivalents; employ side-by-side contrasts and matrices where they teach
  more clearly than a vertical chain.
- History panels must cover chronology, causation, institutions,
  society/economy/culture, debates, legacy and synthesis. Geography panels
  must use process systems, classifications, cross-sections, spatial zones,
  India comparisons, hazards/interventions and synthesis. Philosophy panels
  must map doctrines, arguments, objections/replies, comparisons and
  liberation/ethical paths. Polity panels must map constitutional evolution,
  hierarchy, Articles, procedures, checks/balances, doctrine/case-law and
  federal relations.
- Derive panel nodes from the final corrected learning-session Markdown,
  consolidated register notes, session titles, exact keywords, mechanisms,
  contrasts, traps, verified PYQ themes and answer frameworks. Do not invent
  facts or paste duplicated closure-card prose.
- Preserve the complete conceptual order and exact high-yield content.
- Keep every line within the renderer's readable monospaced width (normally
  at most 100 characters). Split complexity into another panel rather than
  shrinking or clipping it.
- Save the same uninterrupted ASCII master as a standalone `.txt` or `.md`
  beside the graphical flowchart package.
- Validate exact equality in both directions: embedded panels = authored spec
  and standalone plain text = authored spec. Reject generic central wording,
  placeholder axes/zones/conditions, truncation ellipses, repeated `KEY TERMS:`
  scaffolding, session dumps, over-width lines, missing topology, count/order
  gaps and missing source-reference integrity. The graphical teaching
  navigation and separate Cārvāka-style graphical package remain independent
  artifacts.

### Subtopic-closure flow diagram

- After finishing the teaching, examples, evidence, qualifications, traps and
  answer line for a subtopic, insert a compact flow diagram that closes that
  subtopic.
- Use this structure:
  `SUBTOPIC HEADING -> decisive terms/definitions -> mechanism or argument ->
  consequence/contrast -> UPSC trap or answer-use`.
- The diagram must contain the high-yield core in exact short wording; it is
  not a decorative recap and must not introduce an essential point omitted
  from the teaching.
- Include the subtopic's answer-grabbing line or its exact compact exam-use
  formulation inside the closure flow.
- If the subtopic spans several pages, place the closure flow at its actual end.
  Never collect all closure diagrams at the end of the PDF.
- Validate that every substantive teaching subtopic has one closure flow before
  the next teaching heading begins.

## Visual standard

- Use as many pages as necessary for clarity.
- Every major subtopic must receive an appropriate visual.
- Every Sanskrit, Pali, Prakrit or Hindi term must immediately include its
  English meaning in parentheses on first use.
- Visual boxes must never rely on untranslated terminology. For example:
  `pratyaksa (perception)`, `pramana (means of valid knowledge)`,
  `vyapti (invariable concomitance)` and `upadhi (hidden limiting condition)`.
- If a technical term has no exact English equivalent, give the closest
  exam-safe translation plus a one-line explanation.
- Check that definitions and English explanations are complete and not
  truncated by box size, clipping or line limits.
- Processes require arrows and flow diagrams.
- Chronological subjects require timelines.
- Classifications require tables or branch diagrams.
- Comparisons require side-by-side matrices.
- Spatial subjects require maps or labelled spatial diagrams.
- Arguments require premise-to-conclusion trees.
- Include continuation labels when a flow spans pages.
- A visual must teach the concept, not merely decorate the page.

## Answer-grabbing line standard

- Every major subtopic must contain at least one highlighted line labelled:
  `ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM`.
- The line must be a complete, accurate and compact sentence that can directly
  serve as a definition, argument, criticism, transition or conclusion.
- The same exam-ready line must appear in the reusable Markdown, the learning
  notes PDF and the corresponding flowchart stage.
- Definition stages must identify the recommended opening definition explicitly;
  do not leave the learner to infer which explanatory sentence should be written.
- Use answer-grabbing lines selectively: highlight high-value formulations, not
  every fact. They must remain readable and must never be clipped or truncated.
- The learner may adapt the line to the directive and word limit; it is an
  exam-ready formulation, not a substitute for answering the question asked.

## Separate solved-practice workbook

Create a second PDF containing:

1. Every relevant verified PYQ with an independent model solution.
2. Diagnostic MCQs covering nearly every subtopic.
3. Remedial MCQs targeting common errors.
4. Balanced but non-patterned correct-option placement. Do not use a strict
   A-B-C-D cycle or another predictable sequence. Verify every key against its
   question and avoid answer leakage through wording or option length.
5. Original 10-, 15- and 20-mark Mains practice with complete model answers.
6. Explanations showing why each answer earns marks.

## Reusable Markdown

Save a complete cleaned Markdown edition containing:

- All substantive teaching.
- Clearly labelled answer-grabbing lines for every major subtopic.
- Text-form diagrams and flowcharts.
- Solved PYQs.
- MCQs with explanations.
- Original Mains practice and solutions.
- Advanced refinements.
- Final consolidated register notes.

Exclude chat turns, navigation prompts and tool logs.

## Flowchart companion

Every learner-v2 topic must create:

1. A high-resolution master image containing one continuous logical diagram.
2. A one-page large-format poster PDF of that master.
3. A print-readable tiled continuation PDF cropped from the same master, with
   overlap and explicit continuation labels.
4. Page previews and contact sheets for visual inspection.
5. Highlighted answer-grabbing lines, including the recommended opening
   definition and final evaluative verdict.

The flowchart companion must preserve all major exam-relevant points and may be
multi-page.

### Approved visual reference design

- The user explicitly approved the Cārvāka continuous at-a-glance core-first
  design on 22 August 2026 as the reference design for future topic flowcharts.
- Reference folder:
  `notes\Philosophy\flowcharts\philosophy-paper-i-indian-philosophy-01\continuous-at-a-glance-core-first\`
- Preserve its visual language:
  - dark high-contrast background;
  - strong continuous cyan flow rail and numbered stages;
  - clearly coloured keyword pills for decisive terms;
  - large stage headings and readable compact explanations;
  - exact answer-grabbing lines in distinct highlighted bands;
  - primary core visually dominant;
  - subordinate enrichment lighter and placed only after the complete core;
  - overlapping tiled pages that remain crops of the same master diagram.
- Adapt colours where subject meaning benefits, but preserve the hierarchy,
  continuity, keyword prominence, readability and core-before-extra logic.
- Do not regress to disconnected cards, independent chapter posters, bare
  headings, or later pages that repair missing primary-node content.

### Reusable graphical-v2 renderer and specification contract

- The permanent standalone renderer is
  `tools\carvaka_flowchart.py`, identified in tracker provenance as
  `carvaka-continuous-at-a-glance-graphical-v2`.
- Every finalized topic requires an explicit editable JSON specification under
  `upsc-ai-kit\manifests\retrofits\carvaka-graphical-specs\<Subject>\`.
  The authored ASCII atlas is a conceptual/coverage source, but its text must
  not be pasted or rendered as a sequence of ASCII cards.
- The immutable visual reference is the approved Cārvāka master whose SHA-256
  is `c9ae34e995375348a6998885784ded0680c0a8f8e3cd6cb82bb4cd5385e85c62`.
  Validate this hash before and after every build.
- The master must be 4800 px wide with 300-DPI metadata and dynamic height. Its
  header must contain the exact topic title, a concise topic route, a
  read-the-rail instruction, PRIMARY CORE FLOW / SUBORDINATE EXTRA /
  APPROVAL-REVIEW legend pills, and an explicit statement that core precedes
  extra and prior artifacts remain unchanged.
- Number the uninterrupted cyan core rail from Stage `00` through the final
  synthesis. Add exactly one visually lighter grey `E` node after the complete
  core. The enrichment card must state that it is unnecessary for a competent
  core answer.
- Every core card requires 4–10 semantically coloured keyword pills, 2–4
  domain-appropriate internal groups, concise bullets, source references and
  an `ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM` strip. Use varied
  structures—process chains, timelines, matrices, hierarchies, spatial
  cross-sections, doctrine dialectics and synthesis ladders—instead of one
  repeated closure-card template.
- Subject vocabulary must remain native to the domain: chronology/evidence/
  institutions/economy/society/culture for Ancient History; process/spatial/
  India/hazard/intervention for Geography; doctrine/argument/objection/reply/
  liberation for Philosophy; and Articles/powers/procedure/checks/limits/
  federal-rights impact for Polity.
- The final cyan/yellow synthesis card must independently contain comparisons
  or traps, PYQ/answer routes and a balanced conclusion. No verified PYQ
  concept or core explanation may first appear in the grey enrichment card.
- Each package must contain `master.png`, `poster.pdf`, `tiled.pdf`,
  `editable\topic-spec.json`, `README.txt`, `build-audit.json`,
  `validation-report.txt`, `preservation-hashes.json`, page previews, contact
  sheets and the byte-preserved separate `ascii-master.txt`.
- Validate measured card bounds, rail continuity between every node, node/card
  alignment, pill count and colour diversity, 2–4 group structure, answer
  strips, final-synthesis order, grey-extra subordination, glyph coverage,
  clipping, edge contact and blank cards. The poster must embed the exact
  master image, and every tiled page must contain a pixel-identical overlapping
  crop whose union loses no master row.
- Bulk replacement follows gated execution: four specified pilots without
  tracker mutation; reference/contact-sheet review; all-topic staging; then one
  atomic tracker/index finalization only after automated and recorded manual
  visual review pass.

### Continuous at-a-glance flow rule

- Treat the complete flowchart as **one continuous diagram**, even when it
  continues across several pages. A new page is a continuation of the same
  logical flow, not a place to add important information that was absent from
  the first-stage node.
- Use this node pattern:
  `HEADING -> decisive short context -> exact important terms/details -> consequence or contrast`.
- Every heading node must be self-explanatory at a glance. Do not write only a
  broad label such as `rejects inference`, `Board of Control`, or `Crown rule`.
  Add the exact content needed to understand and recall the point.
- Include decisive qualifiers inside the relevant node:
  - what is accepted or rejected;
  - the exact type, scope or category;
  - named functions, powers or subjects;
  - the institutional or doctrinal contrast;
  - the direct consequence;
  - the operative date or Act where chronology matters.
- Examples of the required density:
  - `Carvaka -> accepts pratyaksa (perception) as the only pramana (means of
    valid knowledge) -> specify the accepted form/scope of perception; rejects
    anumana (inference) and sabda (testimony) as independent pramanas -> contrast
    with Nyaya, which accepts perception, inference, comparison and testimony.`
  - `Pitt's India Act, 1784 -> Board of Control supervises civil, military and
    revenue/political affairs -> Court of Directors retains commercial
    management -> creates dual control.`
  - `Government of India Act, 1858 -> Company rule ends -> Crown rule begins ->
    Secretary of State for India and Council replace Company control.`
- Important words must be visually prominent inside the flow itself through
  bold text, colour, underlining or a dedicated keyword line. A learner should
  not need to search another page to discover the decisive term.
- Additional pages may deepen examples, objections or applications, but they
  cannot repair an incomplete primary node. The first occurrence of a concept
  must already contain its answer-worthy core.
- **Core-before-extra priority:** extra information is allowed and encouraged
  where useful, but it must never displace, dilute or visually overshadow the
  most important points of the topic. Complete the high-yield conceptual spine
  first: definitions, accepted/rejected positions, exact functions or powers,
  mechanisms, dates, consequences, comparisons and UPSC traps. Add enrichment
  only after that spine is visibly complete.
- Allocate the clearest boxes, strongest emphasis and earliest flow positions
  to the topic's most exam-relevant points. Secondary examples, background and
  advanced refinements must be visually subordinate and may continue later.
- Before approval, perform an **at-a-glance test**: read only the headings,
  arrows and highlighted keywords. If the complete argument, distinction or
  institutional change cannot be reconstructed, the flowchart is incomplete
  and must be regenerated.

## Validation

Before completion, verify:

- Syllabus and subtopic coverage.
- No major source-owned point was omitted.
- Correct chronology and terminology.
- PYQ completeness.
- MCQ keys are correct, reasonably balanced and non-patterned.
- Register notes are last.
- No empty or sparse pages.
- No clipping, overlap or replacement glyphs.
- Readable fonts, boxes, arrows and continuation flow.
- Complete English translations for every non-English technical term.
- No incomplete sentence or truncated definition in any visual.
- Answer-grabbing lines are present and consistent across Markdown, notes and
  flowchart companions.
- The flowchart is one continuous diagram across pages, and every primary node
  contains the decisive terms, scope, contrast and consequence needed for
  at-a-glance revision.
- No important definition, accepted/rejected doctrine, named function, power,
  date or consequence is deferred to a later add-on page.
- Every learner-v2 topic command produced Markdown, learning PDF, workbook,
  master flow image, poster PDF and tiled continuous flowchart PDF.
- Every substantive teaching subtopic in the learning PDF ends with its own
  closure flow diagram before the next subtopic begins.
- Every major teaching unit has a numbered, searchable `SESSION` heading,
  plain and technical definitions, an answer-grabbing opening, must-write
  keywords with usage guidance, and a closing recall flow.
- The complete-topic ASCII master appears near the end inside consolidated
  register notes, remains in continuous conceptual order across any labelled
  panels, and matches its standalone text artifact.
- Main PDF, workbook and Markdown paths all exist.
