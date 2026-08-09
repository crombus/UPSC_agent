# Logical Reasoning, Coding, Counting and Data Interpretation - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Logical reasoning / decision-making / data interpretation.
> **Core skill:** multi-constraint arrangements, syllogism validity, coding rules, dice/counting
> probability, inclusion-exclusion, and multi-step data interpretation.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/06_Logical-Reasoning-Coding-Counting-and-DI.md).*

---

## 1. Architecture

```text
   MULTI-CONSTRAINT REASONING ITEM
        |
   build the STRUCTURE (grid / tree / compass / Venn / table)
        |
   enter constraints STRONGEST-FIRST; prune impossibilities
        |
   +----------------+-----------------+
   |                |                 |
 UNIQUE placement  VALID conclusion  EXACT count/prob
 (arrangement)     (holds in ALL     (order? overlap?)
                    diagrams)
```

**Analytical claim:** a hard reasoning item is won by **ordering the constraints** (most restrictive
first) and by asking, for logic, "does it hold in **every** consistent diagram?".

## 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Constraint ordering** | Place the clue that fixes the most first; each fix prunes the tree. | Recheck every earlier clue after each placement. |
| ✅ **Syllogism validity** | A conclusion is valid only if true in **all** consistent Venn diagrams. | One counter-diagram disproves it. |
| ✅ **Implication chaining** | `A -> B` and `B -> C` give `A -> C`; each arrow also gives its contrapositive. | The **converse** and the **inverse** are never free. |
| ✅ **Coding rule extraction** | Derive the transformation (shift/reverse/position) from the given pair. | Confirm the rule on **every** given letter before applying. |
| ✅ **Dice/coin counting** | Enumerate the sample space (`6^k`, `2^k`); count favourable. | Outcomes must be equally likely. |
| ✅ **Drawing without replacement** | Use `C(n,r)` on the whole draw, not repeated single-draw fractions. | Fractions multiply only if the draw is **with** replacement. |
| ✅ **Inclusion-exclusion** | `\|A∪B\| = \|A\| + \|B\| - \|A∩B\|`; for three sets, subtract the three pairwise overlaps and **add back** the triple. | Overlaps are counted via `lcm`, not the product, unless coprime. |
| ✅ **Polygon diagonals** | `n(n-3)/2`. | Convex polygon. |

## 3. Harder methods (worked)

### 📝 Method 1 - multi-constraint seating

**Five people P, Q, R, S, T sit in seats 1-5 (left to right).** Clues: R is in the middle (seat 3); P
is at the extreme left; Q is immediately right of P; T is **not** at an extreme end. Then P=1, Q=2,
R=3; T cannot be seat 5, so T=4 and S=5. **Unique order: P, Q, R, T, S.** *(Each clue checks out; the
solution is forced.)*

### 📝 Method 2 - coding rule

**If EARTH is coded GCTVJ (each letter shifted +2), how is MARS coded?** `M->O, A->C, R->T, S->U` ->
**OCTU.** *(Verified by letter positions 13->15, 1->3, 18->20, 19->21.)*

### 📝 Method 3 - dice probability

**Two fair dice; `P(sum = 7)`?** Favourable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 of 36 ->
**1/6.** *(Verified.)*

### 📝 Method 4 - conditional chains: solve them backwards

⚠️ A statement-logic item gives several "if ... then ..." links and asks which claims follow. Do
**not** try to assign truth values by trial. Instead:

```text
1. Write every link as an arrow:            A -> B
2. Write the contrapositive beside it:      not B -> not A
3. To test "if P then Q", ASSUME P and not Q, then chain to a contradiction.
4. To test "it is not necessary that Q", find ONE consistent case with Q false.
```

**Worked example (original).** Four claims W, X, Y, Z satisfy: *(i)* if X is false then Z is false;
*(ii)* if Y is false then W is true; *(iii)* if W is true then X is false.

- **Does "X true -> Y true" hold?** Assume X true and Y false. By (ii), W is true. By (iii), X is
  false - contradicting the assumption. So **Y must be true**: the claim **holds**.
- **Is it possible for Z to be true while Y is false?** (i) contraposed is "Z true -> X true", and we
  just showed X true forces Y true. So **no** - "Z true with Y false" is impossible, i.e. the claim
  "if Z is true it is *not necessary* that Y is true" is **false**.

*(Verified as a logical derivation; only chaining and contraposition were used.)* The audited 2026
Set-A paper contains a four-statement item of exactly this shape.

- 🔑 **Escalation rule:** two arrows plus one contradiction beat any truth table under exam time.

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Strongest-constraint-first** placement. *Safe always; it minimises backtracking.*
- ⚠️ **Counter-diagram test** for syllogisms - try to build one case where the conclusion fails. *Safe
  always; if you can, the conclusion is invalid.*
- ⚠️ **Complement counting** `P(at least one) = 1 - P(none)` is always valid. Independence is needed
  only when multiplying component probabilities to calculate `P(none)`.
- ⚠️ **Inclusion-exclusion** for "either/or" counts. *Safe; remember to subtract the overlap exactly
  once.*

## 5. Boundary cases

- ⚠️ An arrangement puzzle may have **multiple** valid solutions - then only facts common to **all**
  solutions are guaranteed.
- ⚠️ "Some A are B" does **not** give "some A are not B" - existential statements do not license their
  negatives.
- ⚠️ "It is **not necessary** that Q" is settled by **one** consistent counter-case; it does not mean
  Q is false.
- ⚠️ Probability requires **equally likely** outcomes; weighted or dependent events need the sample
  space rebuilt.
- ⚠️ "Possible" is a **yes/no** verdict, "probability" is a **number** - answer the one asked.

## 6. Advanced traps

- ❌ Reporting a placement true in **one** solution when the puzzle has several. -> Report only forced
  facts.
- ❌ Accepting a syllogism because it "sounds right". -> Find a counter-diagram.
- ❌ Reading `A -> B` as `B -> A` in a statement-chain item. -> Only contraposition is free.
- ❌ Applying a coding rule confirmed on only one letter. -> Verify on all given letters.
- ❌ Multiplying single-draw fractions for a without-replacement draw. -> Use combinations.
- ❌ Double-counting the overlap in "either/or"; forgetting to add back the triple overlap with three
  sets. -> Write the full inclusion-exclusion line.
- ❌ Adding probabilities of non-exclusive events. -> Use inclusion-exclusion or complements.
- ❌ Reporting a percentage-point move as a percent change in a DI item. -> Name the quantity first.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Over-claiming a unique seat | A | List all solutions; keep only common facts. |
| Invalid syllogism accepted | C | Always attempt a counter-diagram. |
| Converse used as if valid | C | Write the arrow and its contrapositive; nothing else. |
| Wrong coding rule | R | Re-derive the rule on every letter. |
| Probability sample-space errors | X | Write `6^k`/`2^k` or `C(n,r)` and count favourable explicitly. |
| DI quantity mismatch | R | Label level / share / change / points before computing. |

## 8. Advanced drill (with full solutions)

> ⚠️ These items are **new** - they do not repeat Methods 1-4 above or the Foundation file.

1. A fair coin is tossed 3 times. Find `P(at least one head)`.
2. How many diagonals does a regular decagon have?
3. How many distinct arrangements can be made of the letters of "SUCCESS"?
4. How many integers from 1 to 100 are divisible by **at least one** of 2, 3 and 5?
5. Two fair dice are rolled. Find `P(sum >= 10)`.
6. A bag holds 4 white and 6 black balls; two are drawn together. Find `P(at least one white)`.
7. Given "every diploma holder is a graduate" and "no graduate is under 18", which of these follow?
   (i) No diploma holder is under 18. (ii) Every graduate is a diploma holder.

**Solutions.**

1. **7/8.** Complement: `1 - P(no head) = 1 - (1/2)^3 = 1 - 1/8`. *(Verified.)* The complement is
   valid here because the tosses are independent.
2. **35.** `n(n-3)/2 = 10 x 7/2 = 35`. *(Verified.)*
3. **420.** "SUCCESS" has 7 letters with S x3 and C x2: `7!/(3! x 2!) = 5040/12 = 420`. *(Verified.)*
   ⚠️ Dividing by only one repeat factorial gives 840 - the standard slip.
4. **74.** Three-set inclusion-exclusion:
   `50 + 33 + 20 - 16 - 10 - 6 + 3 = 74`, where the pairwise terms use `lcm(2,3) = 6`,
   `lcm(2,5) = 10`, `lcm(3,5) = 15` and the triple term uses `lcm = 30`. *(Verified by enumeration.)*
   ⚠️ With three sets the triple overlap must be **added back**, not subtracted.
5. **1/6.** Sums of 10, 11 or 12 come from (4,6),(5,5),(6,4),(5,6),(6,5),(6,6) = 6 of 36.
   *(Verified.)* ⚠️ It happens to equal `P(sum = 7)` - a coincidence, not a rule.
6. **2/3.** `P(no white) = C(6,2)/C(10,2) = 15/45 = 1/3`, so `P(at least one white) = 2/3`.
   *(Verified.)* Draws are **without replacement**, so use combinations, not repeated `6/10`.
7. **(i) only.** From `diploma -> graduate` and `graduate -> not under 18`, chaining gives
   `diploma -> not under 18`, so (i) follows. (ii) is the **converse** of the first premise and does
   not follow. *(Verified as a logical form.)*

## 9. Multi-step data interpretation (worked)

Read this revenue table (in crore):

| Year | Product X | All products | X's share |
|---|---:|---:|---:|
| 2022 | 400 | 1000 | 40% |
| 2023 | 500 | 1250 | 40% |
| 2024 | 450 | 900 | 50% |

- Growth of X, 2022 -> 2023 `= (500 - 400)/400 =` **+25%.** *(Verified.)*
- Change in X, 2023 -> 2024 `= (450 - 500)/500 =` **-10%.** *(Verified.)*
- ⚠️ **Trap 1 - different bases.** A +25% then -10% does **not** return to 400: `400 x 1.25 x 0.90 =
  450`, matching the table. Percentage changes are on **different bases**, so they do not cancel.
- ⚠️ **Trap 2 - level vs share.** From 2023 to 2024 X's revenue **fell** (500 -> 450) while X's
  **share rose** (40% -> 50%), because the total fell faster. "X performed worse" and "X gained share"
  are both true.
- ⚠️ **Trap 3 - percentage point vs percent.** That share move is **+10 percentage points** and
  **+25%** in relative terms (`10/40`). *(Verified.)* Expect both numbers among the options.

> 🔑 **DI decision rule:** before computing, label the quantity asked as **level**, **share**,
> **change in level**, **change in share (points)**, or **relative change**. Five different numbers
> live in one table row.

## 10. Interpersonal and communication scenarios

The official CSAT syllabus separately names **interpersonal skills including communication skills**.
The provisional 2026 Set-A classification contains six explicit items in this area (Q72-Q77).
The 2024/2025 papers do not show a comparable block, so treat this as observed provisional 2026
coverage rather than a fixed annual frequency.

| Test | Better response pattern |
|---|---|
| Stakeholder listening | Identify interests and constraints before proposing action. |
| Clear communication | Use specific, neutral language; confirm shared understanding. |
| Conflict handling | De-escalate, separate people from the problem, and seek a fair process. |
| Ethical decision | Reject deception, coercion, discrimination, and avoidable harm. |
| Administrative feasibility | Prefer lawful, proportionate, documented action with follow-up. |
| Relationship/tool matching | Match sender-receiver roles and tools to purpose: inform, consult, persuade, record, or obtain feedback. |
| Communication barriers | Separate physical/noise, semantic/language, psychological, organisational, and technological barriers. |
| Questionnaire design | Prefer neutral, specific, single-issue questions with suitable response choices; reject leading or double-barrelled items. |

### 📝 Original scenario

A team member repeatedly misses a reporting format because the instructions were ambiguous. The
best first response is to clarify the format privately, ask them to restate the requirement, and
agree on a check-in. Public blame or silent correction may hide the communication failure rather
than resolve it.

### 📝 Original classification drill

1. "Was the training clear and useful?" is **double-barrelled** because it asks two judgements.
2. A technical acronym misunderstood by a citizen is a **semantic barrier**.
3. A post-meeting form used to learn whether instructions were understood is a **feedback tool**.

These drills mirror the provisional 2026 categories without reproducing the source questions.

## 11. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ This is the **second-largest three-year family**. Together with data sufficiency in Topic 05,
  it accounts for 78 of 240 audited items (32.5%) - see the [Master Framework](../00_Master-Framework.md).
- ⚠️ Recurring shapes: **seating/ordering arrangements**, **blood relations and directions**,
  **coding-decoding**, **syllogism/deduction**, **decision-making scenarios**, **counting/probability**,
  and **data interpretation** from tables/graphs.
- ⚠️ The papers reward candidates who **draw the structure** and **read the exact quantity asked**;
  they punish mental juggling and misread stems.

## 12. Study links

- ✅ [Foundation companion](../basic/06_Logical-Reasoning-Coding-Counting-and-DI.md).
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - data-sufficiency content overlaps
  this family.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - counting and inclusion-exclusion share methods.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 127

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 1 | 3D shape counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 4 | Polygon diagonal count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 11 | Bar-chart data comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 12 | Bar-chart value calculation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 13 | Bar-chart ratio reading | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 14 | Cube rotation opposite face | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 15 | Cube rotation opposite face | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 16 | Cube rotation opposite face | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 21 | Letter substitution coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 22 | Letter-to-number coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 25 | Office seating deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 26 | Office seating deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 42 | Venn-diagram counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 43 | Placement logic deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 44 | Placement logic deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 45 | Placement logic deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 46 | Placement statement check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 47 | Placement statement check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 48 | Placement statement check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 61 | Progress graph comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 62 | Color arrangement counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 63 | Population graph inference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 64 | Graph statement validity | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 65 | Dual-scale graph comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 66 | Figural analogy completion | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 67 | Graph break-even reading | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 70 | Figural rotation series | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 71 | Population age-group graph | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 72 | Logical relation deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 73 | Policy rate graph inference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 74 | Table data inference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 75 | Table assumption validity | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 76 | Tax revenue graph inference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 10 | Cube partition cuts | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 13 | Syllogism conclusion check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 14 | Grid parallelogram count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 20 | Set overlap deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 29 | Statement sufficiency check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 31 | Venn diagram deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 32 | Logical chain elimination | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 52 | Venn-diagram counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 54 | Letter sequence fill | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 56 | Denomination combination count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 68 | Alphabet substitution coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 70 | Sequence conditional count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 71 | Blood-relation deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 72 | Cube face coloring count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 73 | Natural number partition count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 74 | Symbol substitution evaluation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 76 | Ranking order deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 77 | Ranking order deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 78 | Ranking order deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 79 | Weight inequality deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 80 | Weight inequality deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 15 | Letter sequence completion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 19 | Blood-relation deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 32 | Syllogism deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 33 | Syllogism deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 34 | Sequence pair counting | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 35 | Linear row position count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 36 | Age-ordering deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 48 | Letter-number coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 49 | Letter analogy series | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 52 | Table rate comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 60 | Denomination subset counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 67 | Constrained permutation count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 10 | Syllogism conclusion selection | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 15 | Syllogism conclusion selection | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 17 | Mirror-image consonant count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 19 | Digit-sum integer count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 25 | Multi-attribute classification | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 27 | Matrix trend missing entry | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 28 | Dual-sequence missing entry | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 35 | Venn set overlap range | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 40 | Alphabet reversal position coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 45 | Table run-rate comparison | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 46 | Fractional set deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 49 | Multi-conclusion syllogism | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 56 | Letter-substitution coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 64 | Chessboard diagonal count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 65 | Series blank-fill pattern | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 66 | Restricted digit arrangement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 69 | Non-consecutive selection count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 74 | Pie-chart sector angle | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 10 | Digit row arrangement count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 16 | Alphabet reversal coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 17 | Elimination match counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 18 | Odd digit counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 24 | Letter arrangement counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 27 | Route combination counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 29 | Letter series position | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 30 | Queue minimum size | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 36 | Blood relation deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 38 | Two-statement syllogism | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 39 | Three-statement syllogism | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 40 | Circular seating arrangement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 55 | Constrained PIN enumeration | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 56 | Circle inscribed triangle count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 70 | Pie chart percentage | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 76 | Constrained password count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 77 | Grid row arrangement count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 79 | Form constraint number count | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 4 | Worst-case pair selection | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 5 | Score partition counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 6 | Derangement possibility check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 18 | Interior cube count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 19 | Position-constrained permutation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 24 | Symbol operation decode | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 30 | Collinearity-aware triangle count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 36 | Worst-case colour group draw | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 37 | Letter-shift cipher decode | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 38 | Statement-based age ranking | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 39 | Family-relation statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 40 | Prime-group odd-one-out | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 48 | Circular consecutive selection count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 54 | Circular pass-sequence return | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 55 | Sequence middle term | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 65 | Integer-constraint solution count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 66 | Adjacent-colour stripe count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 68 | Constrained assignment count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 69 | Weighing-coin optimisation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 70 | Coded relational chain deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 75 | Repeating pattern gap fill | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 77 | True-false logic deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 78 | Conditional logic conclusion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 79 | Painted cuboid partition count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 80 | Reverse alphabetical position count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- 3D shape counting
- Polygon diagonal count
- Bar-chart data comparison
- Bar-chart value calculation
- Bar-chart ratio reading
- Cube rotation opposite face
- Letter substitution coding
- Letter-to-number coding
- Office seating deduction
- Venn-diagram counting
- Placement logic deduction
- Placement statement check
- Progress graph comparison
- Color arrangement counting
- Population graph inference
- Graph statement validity
- Dual-scale graph comparison
- Figural analogy completion
- Graph break-even reading
- Figural rotation series
- Population age-group graph
- Logical relation deduction
- Policy rate graph inference
- Table data inference
- Table assumption validity
- Tax revenue graph inference
- Cube partition cuts
- Syllogism conclusion check
- Grid parallelogram count
- Set overlap deduction
- Statement sufficiency check
- Venn diagram deduction
- Logical chain elimination
- Letter sequence fill
- Denomination combination count
- Alphabet substitution coding
- Sequence conditional count
- Blood-relation deduction
- Cube face coloring count
- Natural number partition count
- Symbol substitution evaluation
- Ranking order deduction
- Weight inequality deduction
- Letter sequence completion
- Syllogism deduction
- Sequence pair counting
- Linear row position count
- Age-ordering deduction
- Letter-number coding
- Letter analogy series
- Table rate comparison
- Denomination subset counting
- Constrained permutation count
- Syllogism conclusion selection
- Mirror-image consonant count
- Digit-sum integer count
- Multi-attribute classification
- Matrix trend missing entry
- Dual-sequence missing entry
- Venn set overlap range
- Alphabet reversal position coding
- Table run-rate comparison
- Fractional set deduction
- Multi-conclusion syllogism
- Letter-substitution coding
- Chessboard diagonal count
- Series blank-fill pattern
- Restricted digit arrangement
- Non-consecutive selection count
- Pie-chart sector angle
- Digit row arrangement count
- Alphabet reversal coding
- Elimination match counting
- Odd digit counting
- Letter arrangement counting
- Route combination counting
- Letter series position
- Queue minimum size
- Blood relation deduction
- Two-statement syllogism
- Three-statement syllogism
- Circular seating arrangement
- Constrained PIN enumeration
- Circle inscribed triangle count
- Pie chart percentage
- Constrained password count
- Grid row arrangement count
- Form constraint number count
- Worst-case pair selection
- Score partition counting
- Derangement possibility check
- Interior cube count
- Position-constrained permutation
- Symbol operation decode
- Collinearity-aware triangle count
- Worst-case colour group draw
- Letter-shift cipher decode
- Statement-based age ranking
- Family-relation statement sufficiency
- Prime-group odd-one-out
- Circular consecutive selection count
- Circular pass-sequence return
- Sequence middle term
- Integer-constraint solution count
- Adjacent-colour stripe count
- Constrained assignment count
- Weighing-coin optimisation
- Coded relational chain deduction
- Repeating pattern gap fill
- True-false logic deduction
- Conditional logic conclusion
- Painted cuboid partition count
- Reverse alphabetical position count

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
