# General Mental Ability - INTEGRATED CORE MAP

> **Subject:** CSAT | **Tier:** Core integration spine | **Paper:** Prelims Paper II.
> **Official clause:** "General mental ability."
> **Purpose:** Join the distributed number, arithmetic, rate, algebra, data and logical-reasoning
> owners into one complete decision map. Specialist formulas and drills remain in Topics 02-06.
> **Companion:** `../advanced/08_Mixed-General-Mental-Ability-and-Strategy.md`

---

## 1. What General Mental Ability means in this architecture

General Mental Ability is an umbrella ability to:

```text
UNDERSTAND information
        -> REPRESENT it as number / relation / diagram / table / condition
        -> SELECT a valid method
        -> REASON or COMPUTE
        -> CHECK sufficiency, consistency and magnitude
        -> DECIDE under time and negative marking
```

It is broader than arithmetic and narrower than the whole CSAT paper. Reading comprehension has its
own official clause and Topic 01, while communication has its own clause and Topic 07; both still
support mental performance.

---

## 2. Complete ownership map

| GMA capability | Primary Core owner | Typical forms |
|---|---|---|
| Number properties and pattern sense | [Topic 02](02_Number-Systems-and-Number-Sense.md) | Divisibility, remainders, digits, factors, HCF/LCM, powers, series |
| Quantitative proportional reasoning | [Topic 03](03_Arithmetic-and-Commercial-Math.md) | Ratio, percentage, average, mixture, profit-loss, interest, ages |
| Rate, space and time reasoning | [Topic 04](04_Rates-Motion-Time-and-Geometry.md) | Work, pipes, speed, trains, boats, clocks, calendars, geometry |
| Algebraic and sufficiency judgement | [Topic 05](05_Algebra-Inequalities-and-Data-Sufficiency.md) | Equations, inequalities, comparison, data sufficiency |
| Relational, spatial and symbolic reasoning | [Topic 06](06_Logical-Reasoning-Coding-Counting-and-DI.md) | Arrangement, relations, directions, coding, deduction, counting, DI |
| Communication judgement | [Topic 07](07_Interpersonal-and-Communication-Skills.md) | Barriers, feedback, conflict, channel, questionnaire, scenario choice |

No question becomes ownerless merely because UPSC labels it broadly. Route it by the mechanism
actually required.

---

## 3. First-read classification tree

```text
Does the stem depend on a passage?
  YES -> Topic 01
  NO
   |
   +-- asks about communication/conflict/channel? -> Topic 07
   +-- asks whether statements are sufficient?    -> Topic 05
   +-- arrangement/relation/direction/code/table? -> Topic 06
   +-- divisibility/digits/remainder/pattern?      -> Topic 02
   +-- ratio/%/average/money/age?                  -> Topic 03
   +-- work/speed/time/calendar/shape?             -> Topic 04
   +-- equation/inequality/comparison?             -> Topic 05
```

Some questions cross mechanisms. Select the dominant method first and use a second owner only when
it contributes a distinct necessary step.

---

## 4. Universal GMA workflow

1. **Classify:** identify the mechanism, not the story.
2. **Extract:** write only the relevant quantities, conditions and relation words.
3. **Represent:** equation, ratio, table, set, grid, tree, compass or diagram.
4. **Choose least work:** property, elimination, estimation, substitution or full solution.
5. **Solve:** keep units and conditions visible.
6. **Verify:** magnitude, sign, parity, boundary, plug-back or counterexample.
7. **Decide:** mark, revisit or leave according to confidence and time.

> **Core rule:** Externalise structure. Mental juggling creates avoidable working-memory errors.

### Fully worked mixed-mechanism example

**Question.** Group A has 40 observations with mean 70. Group B has 60 observations with mean 40.
Every Group B observation rises by 25%. Is the combined mean now above 55?

**Classify -> extract -> represent:** this is Topic 03 weighted-average reasoning plus a percentage
change; it is **not** a simple-average question. Write totals, not a long list: `A total = 40 x 70 =
2800`; `new B mean = 40 x 1.25 = 50`; `new B total = 60 x 50 = 3000`.

**Method selection and rejection:** compare totals with the required threshold without dividing:
`55 x (40 + 60) = 5500`; actual total is `5800`, so the combined mean is above 55. Reject `(70 +
50)/2 = 60`: that shortcut is unsafe because the groups have unequal sizes. Scaling B by `1.25` is
safe only because the same percentage applies to **every** B observation.

**Verification:** 2800 + 3000 = 5800 over 100 observations, so the exact mean is 58; it agrees with
the inequality result. **Diagnosis:** a 60 answer is a representation error (unweighted mean), while
an incorrect B total is an execution error. Log the stage separately.

---

## 5. Cross-cutting reasoning distinctions

| Distinction | Correct test |
|---|---|
| **Necessary vs sufficient** | In `A -> B`, A is sufficient and B is necessary |
| **Implication vs converse** | `A -> B` permits `not B -> not A`, not `B -> A` |
| **Possible vs certain** | One valid case proves possibility; every valid case is needed for certainty |
| **Correlation vs causation** | Association alone does not establish the causal mechanism |
| **Absolute vs relative change** | Difference in units/points versus change relative to the original base |
| **Average vs weighted average** | Unequal groups require weights |
| **Permutation vs combination** | Order matters versus order does not |
| **Distance vs displacement** | Path length versus net positional change |
| **Data sufficiency vs calculation** | Prove uniqueness/sufficiency; do not solve more than required |
| **Exact value vs estimation** | Estimation is valid only when option separation makes it decisive |

---

## 6. Representation toolkit

| Information shape | Representation |
|---|---|
| Repeated proportional change | Multiplicative factors |
| Relative shares | Ratio or 100-unit base |
| Work/motion | Rate x time table |
| Family relation | Tree |
| Direction/turn | Compass sketch or coordinates |
| Seating/order | Slots or grid |
| Conditional statements | Arrows and contrapositives |
| Sets/overlap | Venn diagram or inclusion-exclusion |
| Data table/chart | Requested quantity, base and unit labelled first |
| Sufficiency | Separate Statement I, Statement II and combined tests |

The representation is part of the solution, not decorative working.

---

## 7. Verification toolkit

- **Unit check:** kilometres cannot directly answer hours.
- **Magnitude check:** reject impossible orders of magnitude before exact calculation.
- **Parity/unit digit:** fast check for integer expressions.
- **Range/boundary:** probability must lie from 0 to 1; percentages and counts must fit the stem.
- **Plug-back:** substitute the proposed value into every condition.
- **Counterexample:** one valid counter-case defeats a claim of necessity.
- **Independent method:** use options or estimation to confirm a long calculation.
- **Completeness:** ensure every stated condition was used or deliberately shown irrelevant.

---

## 8. Operational time and attempt control

| Stage | Hard operating rule |
|---|---|
| **Classify** | Spend **10-15 seconds** identifying the owner and representation. If neither is visible, circle/park. |
| **Pass 1 - Harvest** | Spend **at most 60 seconds** on direct properties, one-step arithmetic, obvious diagrams and short tables. Mark only when the method is complete. |
| **Pass 2 - Grind** | Spend **at most 120 seconds** on multi-step quant, arrangements, complex DI and sufficiency. Write a compact representation before computing. |
| **Park** | At either cap, mark the question number, reason (`method`, `representation`, `arithmetic`, or `live options`) and move on. No emotional re-start. |
| **Final review** | Reserve the final **10 minutes** for parked items, marked-option transcription and only elimination-backed decisions. |

The 90-second paper average is not an individual-item command. Record whether a miss arose at
classification, extraction, representation, execution, verification or decision; Topic 08 routes the
repair, while the specialist topic supplies the drill.

---

## 9. Audited-PYQ integration rule

- The directly auditable question-level evidence in this repository is the 2024-2026 Set-A table in
  [Question Audit Ledger](../00_Question-Audit-Ledger.md). It should not be represented as an
  unsupported 2018-2023 routing database.
- 2024-2025 questions route to Topics 01-06 by their dominant mechanism. In 2026, Q72-Q77 retain
  Family 06 as an exclusive **structural** count but carry Topic 07 as their **content** owner.
- Topic 08 is the syllabus and navigation owner, not a duplicate omnibus table. Frequency, drills
  and remediation are read from the specialist owner and the tracker.

This avoids leaving an official umbrella ownerless, duplicating questions, or confusing solving
format with syllabus content.

---

## 10. Readiness checklist

You are GMA-ready only if you can:

- classify a mixed question into the correct owner rapidly;
- translate words into a minimal representation;
- choose a property or shortcut only when its conditions hold;
- distinguish necessity, sufficiency, possibility and certainty;
- verify units, magnitude and conditions;
- abandon a time-expensive item without emotional attachment;
- diagnose the cause of each error and route revision to the correct topic.

> **Core firewall:** Skipping Advanced Topic 08 cannot remove any GMA ownership, classification,
> workflow, representation, verification, time-control or revision-routing mechanism.

---

## Semantic-completeness closure — 2026-09-06

### Literal syllabus and canonical ownership

- **Literal clause:** General mental ability.
- **Canonical scope:** Owns the integrated classify-extract-represent-execute-verify-decide workflow, cross-family routing, cognitive-load control, time triage and readiness diagnostics.
- **Cross-topic boundary:** It does not duplicate formulas or full drills owned by Topics 02-07; it links them and teaches method selection for mixed questions.

### Complete learner route

1. **Classify:** Identify the dominant tested mechanism before calculating.
2. **Extract:** Separate givens, unknowns, constraints and the requested output.
3. **Represent:** Choose equation, table, diagram, number line, grid or passage map.
4. **Select method:** Use the lightest valid method, not the most familiar one.
5. **Execute:** Keep units, domains, direction and assumptions visible.
6. **Verify:** Use plug-back, bounds, enumeration, reverse coding or passage support.
7. **Decide:** Answer, eliminate, park or leave according to evidence and time.
8. **Cross-family routing:** Send number, arithmetic, rate, algebra, logic and communication gaps to their owners.
9. **Mixed problems:** Decompose a question into ordered sub-mechanisms.
10. **Cognitive load:** Externalise information instead of holding it mentally.
11. **Time and risk:** Use three passes and positive-evidence elimination.
12. **Readiness loop:** Diagnose error type, remediate the owner and retest under time.

### Verification and hostile-query gate

A mixed solution must name the owning mechanism, use a fitting representation, execute only justified steps and finish with an independent verification or risk decision.

The hostile absence search explicitly tested these families and close-option terms:
**classify; extract; represent; execute; verify; decide; time control; error log**. A shortcut is usable only when its stated condition survives; otherwise return to
the first-principles representation. Every worked answer must finish with an independent check:
passage support, substitution, enumeration, units, bounds, reverse operation or option elimination.

### Difficulty and timed progression

1. Foundation: recognise the family and state the governing definition or relation.
2. Core: solve a direct item with a visible representation and one verification.
3. Advanced: combine two mechanisms, test edge cases and reject close distractors.
4. Timed: use classify → extract → represent → execute → verify → decide.
5. Remediation: log the error as concept, application, calculation, reading, passage, time or guess;
   return to the owning subtopic before retesting.

