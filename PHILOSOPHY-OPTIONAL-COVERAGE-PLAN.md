# Philosophy Optional: Syllabus-Linked Coverage Plan

> Saved: 28 September 2026. Status: coverage audit complete (40 of 40 clauses mapped); all ten Philosophy of Religion clauses, all nine Indian Philosophy clauses (Cārvāka, Jainism, Schools of Buddhism, Nyāya–Vaiśeṣika, Sāṃkhya, Yoga, Mīmāṃsā, Schools of Vedānta, Aurobindo), all ten Socio-Political clauses (Equality, Justice, Liberty; Sovereignty; Individual and State; Forms of Government; Political Ideologies; Humanism, Secularism, Multi-culturalism; Crime and Punishment; Development and Social Progress; Gender Discrimination; Caste Discrimination), and all eleven Western clauses (Plato and Aristotle; Rationalism; Empiricism; Kant; Hegel; Moore, Russell and Early Wittgenstein; Logical Positivism; Later Wittgenstein; Phenomenology (Husserl); Existentialism; Quine and Strawson) audited, with confirmed gaps repaired in affected Core owners. Audit completion is not a guarantee of future question coverage or a personal study-progress claim.
> Scope: all four sections (Western, Indian, Socio-Political, Philosophy of Religion).

## Aim and boundary

Prevent avoidable surprises in Philosophy Optional by tracking **concepts and question demands**,
not just names of philosophers. A topic may be weak even when a thinker is mentioned: the
specific argument, assumption, counterargument, reply, application or comparison may be absent.
Conversely, a concept can be examined without naming any philosopher.

The official syllabus in
`upsc-ai-kit\knowledge\Philosophy\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md` controls scope. The
40 canonical Core owners and the verified 2018-2026 PYQ banks provide the existing evidence.
The subject is already marked answer-ready in
`upsc-ai-kit\knowledge\Philosophy\ANSWER-WORTHINESS-AUDIT.md` and the broader semantic review;
those assessments are evidence, **not** a guarantee against unfamiliar future questions.

This project creates a **separate, learner-readable coverage and risk map**. It does not create
new syllabus owners, replace the existing audit or require bulk editing the Core notes. Keep
the map outside `upsc-ai-kit\knowledge\Philosophy\` in a root-level `philosophy-coverage\`
folder so the difference between navigation and teaching content is explicit.

## Revised plan after review

The original proposal for philosopher matrices and an immediate status JSON had two weaknesses:
it made *names* the unit of coverage, and it duplicated the existing Core/Advanced matrix and
semantic-completeness tracker. Instead:

1. Use **one row per examinable demand**: a concept, doctrine, argument, objection, relation,
   comparison, method, school-specific variant or thinker-specific position. A philosopher's
   name is an attribute of a demand, not the default row key.
2. Give each row an **exact syllabus clause**, one primary Core owner, any secondary cross-links
   and a source trail (verified PYQ, canonical text, textbook evidence or reasoned inference).
3. Distinguish **mention**, **substantive treatment**, **answer-ready** and **not verified**.
   A search hit does not establish depth. Do not invent completeness statistics or declare
   gaps merely because a name is absent from one file.
4. Use a priority classification, **not a prediction of UPSC probabilities**:
   - **Essential:** literal syllabus demands, indispensable prerequisites and verified PYQs.
   - **Supporting:** canonical critics, school variants and comparisons needed to answer
     essential demands under plausible rewording.
   - **Enrichment:** defensible extensions beyond Core answer sufficiency, clearly optional.
5. If a genuine marks-essential gap is confirmed, record its evidence and impact and repair
   the canonical Core owner; the user has authorized clause-by-clause Core remediation.
   Do **not** treat a separate map as a substitute for Core material.
6. Reuse the existing `paper-1\_themes\` comparisons and 2026 remediation ledgers; link to
   them rather than copying lengthy expositions into the map.

## Deliverables for the implementation phase

Create these **only as each section is actually audited**:

```text
philosophy-coverage\
|-- README.md                     # scope, method, status and navigation
|-- Philosophy-of-Religion.md     # clause-by-clause demand matrix
|-- Indian-Philosophy.md
|-- Socio-Political-Philosophy.md
`-- Western-Philosophy.md
```

No independent JSON state until a concrete need for automation is demonstrated. The
existing `KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md` remains the authority for the older
whole-repository review; this project records its **own audit progress in `README.md`**.
No changes to study-progress status: an audited topic is not a studied topic.

Recommended row fields (split large rows if one concept has several independently
examinable arguments):

| Field | Meaning |
|---|---|
| ID and demand | Stable clause-scoped identifier and examinable question, not just a name |
| Syllabus anchor | Paper, section, clause and exact controlling words |
| Thinker/school | Defender, critic or comparison partner where relevant; distinguish roles |
| Required logic | Thesis, inferential steps, objection/reply and conclusion to be written |
| Connection | Prerequisite, rival position, cross-clause comparison or application |
| Evidence | Verified PYQ citation, Core section, textbook reference or labelled inference |
| Priority | Essential / Supporting / Enrichment with a one-line justification |
| Coverage | Mention / Substantive / Answer-ready / Not verified; with exact file and heading |
| Gap and action | Specific missing demand or `none`; owner and proposed remedy if confirmed |

## Discovery and scope control

For each syllabus clause, read the official wording, its Core owner, any directly linked
comparison/theme file and relevant verified PYQ ledger. Build four lenses separately:

1. **Literal words:** each named term, qualifier, school and relation.
2. **Conceptual dependencies:** definitions, mechanisms and distinctions required to explain
   those words.
3. **Examined variants:** the specific thinker, textual argument, objection, application,
   dual-demand stem or cross-school comparison in verified PYQs.
4. **Bounded future variants:** a standard critic, rival account or school representative that
   can reasonably be used to test the same syllabus clause. Cite the rationale; do not list
   arbitrary additional philosophers.

Coverage cannot be inferred from a name appearing somewhere in the repository. Test whether
an answer can actually be constructed with the relevant assumptions, opposition and qualified
verdict. Label uncertain interpretations as uncertain; do not represent speculative
future-question examples as past questions.

## Implementation order and gates

Work **one clause at a time**, then finish its section before starting the next:

1. **Philosophy of Religion:** the syllabus names few thinkers; pilot the method on
   "Proofs for the Existence of God and their Critique". Include Indian and Western cases,
   critiques, religion without a creator as a boundary, and exact PYQ demands without
   claiming every critic is an atheist.
2. **Indian Philosophy:** school-internal variants and inter-school debates, including
   epistemology and non-Advaita Vedanta.
3. **Socio-Political Philosophy:** concept-first mapping (rights, liberty, equality,
   corruption, democracy, caste etc.), with named thinkers where necessary.
4. **Western Philosophy:** named thinkers, close textual distinctions, critics and
   cross-thinker comparisons.

At each clause gate, confirm: (a) every literal syllabus term has a row or a documented
reason for grouping; (b) all relevant verified 2018-2026 PYQ demands have an exact route;
(c) essential comparisons have both sides; (d) the map cites a real owner/section rather
than a generated workbook alone; (e) gaps are distinguished from "not yet checked"; and
(f) no claim of exhaustive future-proofing is made. Repair confirmed Core-owner gaps
before marking the clause audited.

After the four sections: sample unseen, syllabus-bounded rephrasings for each clause and
report unresolved demands explicitly. Regeneration of dependent PDFs, if needed, follows
the existing `AGENT_MEMORY.md` and semantic-completeness workflow; the coverage map itself
does not certify generated packages.

## Pilot acceptance criteria

The first Religion clause should produce a thorough, terminal-navigable map
of individually examinable demands, with precise links and **no unverified
"complete" labels**. Do not compress five separately examinable proofs into
one row with a checklist of names. It must be possible
to locate the ontological, cosmological, design, moral and Indian proof families; their
chief criticisms; at least one Indian non-creator counterposition; and the specific
2018-2026 PYQs without opening unrelated generated packages. Keep detailed
reasoning in the Core owner while retaining every distinct demand in the map.

## Inventory and remediation boundary

The clause maps and fresh coverage judgments are recorded separately in
`philosophy-coverage\`. Recording a gap there does **not** repair a canonical
owner or update the old semantic-completeness certification. The user has
authorized fixing confirmed gaps in original Core files during each clause audit;
this project does not silently update prior whole-repository certification.
