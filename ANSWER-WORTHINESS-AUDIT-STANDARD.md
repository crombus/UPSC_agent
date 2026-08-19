# UPSC Knowledge Answer-Worthiness Audit Standard

> **Purpose:** Determine whether the knowledge Markdown can reliably generate
> credible, marks-worthy answers for both known PYQs and unfamiliar future
> questions.
>
> **Important:** Syllabus coverage, file count, PYQ routing and the presence of
> headings do **not** by themselves prove answer-worthiness. Each subject must be
> inspected topic-by-topic against the evidence and reasoning tests below.

---

## 1. The ten-point standard

| # | Criterion | What the knowledge must enable |
|---:|---|---|
| 1 | Demand fidelity | Decode directives, qualifiers and every subpart; distinguish `Discuss`, `Examine`, `Critically examine`, `Evaluate`, `Analyse`, `Comment`, comparison and causal demands. |
| 2 | Direct thesis | Form a clear, qualified position in the introduction instead of repeating the question. |
| 3 | Logical structure | Organise by chronology, dimensions, stakeholders, causal chain, mechanism, comparison or another question-appropriate architecture. |
| 4 | Evidence-led analysis | Build `claim -> named evidence/example -> significance -> limitation` rather than append examples decoratively. |
| 5 | Adequate examples | Supply a credible pool capable of roughly 2-3 examples for 10 marks, 4-6 for 15 marks and 5-8 for 20 marks, without repetition or padding. |
| 6 | Analysis over narration | Explain why, how, consequences, interaction and significance—not merely what happened or what a scheme contains. |
| 7 | Balance | Provide variation, criticism, counter-evidence, limits, trade-offs or alternative interpretations where the directive requires them. |
| 8 | Value addition | Supply usable terminology, diagrams, maps, flowcharts, scholars, committees, cases, reports, constitutional/legal anchors or verified data appropriate to the subject. |
| 9 | Reasoned conclusion | Enable a graded verdict that answers the precise question and follows from the analysis. |
| 10 | Factual discipline | Prevent fabricated data, quotations, cases, provisions, chronology or examples; preserve source, date and status distinctions. |

---

## 2. Evidence-unit test

A fact is not automatically useful evidence. A complete evidence unit contains:

```text
CLAIM
  -> NAMED EVIDENCE / EXAMPLE
  -> WHY IT SUPPORTS THE CLAIM
  -> LIMIT / VARIATION / STATUS CAUTION
```

### Example of weak storage

> "The Green Revolution increased food production."

### Example of answer-ready storage

> **Claim:** Technological intervention can overcome an immediate production
> constraint when backed by state capacity. **Evidence:** The Green Revolution
> combined high-yielding varieties with irrigation, inputs, procurement and
> extension. **Significance:** It strengthened food-grain availability and
> reduced import vulnerability. **Limitation:** Benefits were regionally uneven
> and created ecological and crop-diversity costs.

The audit must judge the second capability, not keyword presence.

---

## 3. Future-question readiness test

Every Core topic must support answers beyond questions already seen in the PYQ
corpus. Test at least these demand transformations:

1. **Definition -> application:** Can the concept be applied to a new case?
2. **Description -> causation:** Can the file explain why and how?
3. **Single dimension -> comparison:** Can it compare periods, regions,
   institutions, groups or theories?
4. **Achievement -> critical evaluation:** Can it state limits and
   counter-evidence?
5. **Static -> current linkage:** Can a current development be embedded without
   making static understanding dependent on it?
6. **Known PYQ -> unfamiliar wording:** Can the same knowledge answer a changed
   directive, scope or time period?
7. **Part question -> synthesis:** Can evidence from multiple owner files be
   combined without contradiction or duplication?

Passing PYQ coverage alone is insufficient.

---

## 4. File scope of each subject audit

Inspect:

- `README.md`;
- master framework/chronology;
- official syllabus mapping;
- revision chart;
- every `basic/` file;
- every `advanced/` companion;
- complete-topic-package Markdown where present;
- local PYQ routing/ledger files relevant to the subject;
- linked evidence owners when the subject intentionally delegates facts.

Do not score generated PDFs as substitutes for missing reusable Markdown.

---

## 5. Scoring scale

Score every criterion from 0 to 3:

| Score | Meaning |
|---:|---|
| 0 | Missing or materially unsafe |
| 1 | Present only sporadically; cannot support reliable novel answers |
| 2 | Generally sufficient, with identifiable topic-level gaps |
| 3 | Systematic, reusable and future-question ready |

### Critical criteria

Criteria **1, 2, 3, 4, 6 and 10** are critical. A subject cannot be marked
complete if any Core topic is materially deficient on one of them.

### Subject status

| Status | Meaning |
|---|---|
| ⬜ Pending | Not audited against this standard |
| 🔍 Auditing | Inspection in progress |
| 🟠 Strengthening required | Audit completed; material gaps remain |
| 🟡 Strengthened, validation pending | Files changed; final re-audit remains |
| ✅ Complete | All Core topics future-question ready; Advanced remains optional enrichment |
| ⛔ Blocked | Required source or owner file is unavailable |

No subject becomes ✅ merely from a high average score. Topic-level critical
gaps must be repaired.

---

## 6. Required per-subject audit output

Save:

`upsc-ai-kit/knowledge/<Subject>/ANSWER-WORTHINESS-AUDIT.md`

It must contain:

1. **Audit scope and inventory**
2. **Executive verdict**
3. **Ten-criterion scorecard**
4. **Topic-by-topic matrix**
5. **Future-question stress tests**
6. **Evidence-bank assessment**
7. **Factual-risk ledger**
8. **Core gaps that could reduce marks**
9. **Advanced-only improvements that are safely skippable**
10. **Files changed**
11. **Validation evidence**
12. **Final status and date**

### Topic matrix

| Topic | Demand/thesis | Structure/analysis | Evidence sufficiency | Balance/value | Fact safety | Action |
|---|---|---|---|---|---|---|
| NN Topic name | 0-3 | 0-3 | 0-3 | 0-3 | 0-3 | Keep / strengthen |

### Evidence-bank matrix

| Major demand family | Named examples available | Significance supplied? | Limit supplied? | 10/15/20-mark readiness |
|---|---:|---|---|---|

---

## 7. Mandatory audit method

1. Inventory all subject files and exact Core/Advanced pairs.
2. Read the framework, syllabus map and revision chart.
3. Inspect every Core file substantively; do not keyword-score.
4. Inspect every Advanced file for optional-only depth and Core leakage.
5. Sample or enumerate PYQ routes to identify repeated demand patterns.
6. Generate unfamiliar test questions across directives and timelines.
7. Attempt answer skeletons using only the stored knowledge.
8. Record evidence gaps, unsupported claims and factual-status risks.
9. Strengthen the Core files wherever paper outcome could otherwise suffer.
10. Keep optional nuance in Advanced; do not make Core dependent on it.
11. Re-run link, formatting and subject-specific validation.
12. Write the audit file and update the master tracker.

---

## 8. Non-negotiable repair rules

- Fix the knowledge files, not merely the audit report.
- Core must remain independently answer-complete.
- Do not inflate files with generic “way forward” lists.
- Evidence must perform an analytical function.
- Do not force every example count into every answer; ensure a sufficiently
  diverse pool from which the right examples can be selected.
- Reuse verified owner files instead of duplicating uncertain facts.
- Tag current and dynamic claims with date/status discipline.
- Do not invent quotations, scholars, cases, data or PYQs.
- Preserve subject boundaries while ensuring cross-links are usable.
- Do not mark complete until unfamiliar-question stress tests pass.

---

## 9. Adapted paper standards

### Essay

Audit against prompt fidelity, thesis, argument, counterargument, evidence,
coherence, exact expression and conclusion. Do not force GS-style headings or
example quotas into a continuous essay.

### Ethics

Apply the ten criteria to Section A. For Section B additionally require facts,
stakeholders, constraints, realistic options, ethical evaluation, decision,
implementation and residual-risk mitigation.

### Philosophy

Require doctrine, argument reconstruction, objections, replies, comparison and
direct response to the exact philosophical claim. Examples cannot substitute
for arguments.

### CSAT

The descriptive-answer rubric is not applicable. Audit instead for concept
completeness, method selection, conditions on shortcuts, worked examples,
trap-awareness, timed execution, error diagnosis and qualifying-margin safety.

### Qualifying English and Hindi

Audit for grammar/usage, comprehension, précis, essay/paragraph construction,
translation where applicable, worked practice, marking safety and timed
completion—not GS-style evidence density.

