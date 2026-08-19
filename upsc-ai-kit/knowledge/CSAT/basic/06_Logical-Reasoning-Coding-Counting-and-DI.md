# Logical Reasoning, Coding, Counting and Data Interpretation - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Logical reasoning / decision-making / data interpretation.
> **Core skill:** arrangements, blood relations, directions, coding, series, basic counting/probability,
> data tables and scenario reasoning.
> **Boundary:** Topic 07 owns the complete official interpersonal/communication clause; Topic 08
> integrates this file into the General Mental Ability map.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md).*

---

## 1. Visual foundation

```text
   A REASONING ITEM
        |
   +----------+-----------+-----------+-----------+
   |          |           |           |           |
 ARRANGE    RELATE      CODE        COUNT       READ
 grid/row   family/dir  letter/num  arrange/    the table/
            map         shift/rule  choose      graph
        |
   draw the picture (grid, tree, map) - never hold it all in your head
```

**Core proposition:** reasoning items are solved by **externalising** the structure - a grid, a family
tree, a direction map - so the constraints do the work.

## 2. Essential tools

| Sub-skill | Method |
|---|---|
| ✅ **Linear/circular arrangement** | Draw seats; for a circle, fix one person as an anchor before placing the strongest clue. |
| ✅ **Blood relations** | Build a small family tree; resolve "only son/daughter" carefully. |
| ✅ **Directions** | Sketch N-E-S-W; each right turn is +90 clockwise. |
| ✅ **Coding-decoding** | Find the rule (shift, reverse, position-value) from the given pair, then apply. |
| ✅ **Series** | Test differences, ratios, and known sequences (squares, triangular, primes). |
| ✅ **Visual/figure reasoning** | Copy the figure; count by size/layer and track invariants (sides, regions, shading, orientation). For cube views, faces visible together are adjacent. |
| ✅ **Conditional/statement logic** | Rewrite every "if ... then ..." as `A -> B`; chain implications and use contrapositives; never the converse. |
| ✅ **Counting** | Permutations `P(n,r) = n!/(n-r)!`; combinations `C(n,r) = n!/(r!(n-r)!)`. |
| ✅ **Probability** | `P = favourable / total` for equally likely outcomes; for a sequence, multiply **conditional** probabilities. |
| ✅ **Data interpretation** | Read the title, unit, scale and both axes before computing totals, differences, percentages, shares or weighted values. |
| ✅ **Interpersonal/communication scenario** | Apply the dedicated [Topic 07](07_Interpersonal-and-Communication-Skills.md) decision engine; this file retains only the reasoning interface. |
| ✅ **Communication matching** | Distinguish relationship type, tool purpose, channel, feedback, and barrier from the function described. |
| ✅ **Questionnaire design** | Use clear, neutral, single-issue questions; avoid leading, double-barrelled, ambiguous, or intrusive wording. |

The provisional 2026 Set-A audit places six explicit interpersonal/communication items at Q72-Q77.
Their complete concepts now reside in Topic 07. This remains a year-specific observed block, not
evidence that every CSAT paper uses the same count.

> 🔑 **Arrangement rule:** always start from the clue that **fixes the most**; a single anchored
> position usually cascades to the full solution.

## 3. Method

1. Classify the sub-skill and **draw the structure** (row, circle, tree, compass, table).
2. Enter the **strongest constraint** first, then the next, checking consistency each time.
3. For counting/probability, decide **order matters?** (permutation) or **not** (combination) before
   computing.
4. For DI, answer the **exact** quantity asked (total / change / percent), not a nearby one.
5. For communication scenarios, identify the misunderstanding or conflict, reject coercive or
   deceptive options, and prefer a clear, fair response with follow-up.

## 4. Formulas and rules

- ✅ `P(n,r) = n!/(n-r)!` (arrangements, order matters). *Requires `0 <= r <= n`.*
- ✅ `C(n,r) = n!/(r!(n-r)!)` (selections, order does not matter). *Requires `0 <= r <= n`; note
  `C(n,r) = C(n, n-r)`.*
- ✅ `P(n,r) = C(n,r) x r!` - permutations are combinations **times** the orderings of the chosen set.
- ✅ Arrangements of a word with repeats: `total! / (product of repeat factorials)`.
- ✅ Circular arrangements of `n` distinct people, where rotations are identical, are `(n-1)!`: fix one
  person, then arrange the rest. Do **not** divide by 2 unless mirror images are explicitly identical.
- ✅ For an `r`-digit numeral using a digit set containing zero, choose the first digit from the
  non-zero digits; then fill the remaining positions under the repetition rule.
- ✅ `P(not E) = 1 - P(E)`; for equally likely outcomes, `P = favourable/total`. *Every probability
  lies in `[0, 1]`; an answer outside that range is a signal you counted the sample space wrongly.*
- ✅ Sequential probability uses `P(A and B) = P(A) x P(B | A)`. Without replacement, the second
  fraction changes; multiplication itself remains valid because it uses the **conditional** fraction.
- ✅ `|A ∪ B| = |A| + |B| - |A ∩ B|`. For a total of `N`, overlap lies between
  `max(0, |A|+|B|-N)` and `min(|A|,|B|)`.
- ✅ In a worst-case “minimum draws to ensure” question, first take as many as possible without the
  target, then add one. For a grid/figure count, list each size exactly once rather than scanning
  visually.
- ✅ Handshakes or pairwise segments among n objects/points = `C(n,2)`; these are distinct infinite
  lines only when no three points are collinear.

### 4.1 Probability vs possibility

| Term | Meaning | Typical stem |
|---|---|---|
| ✅ **Possible** | At least one favourable case **exists**; the probability is `> 0`. | "Can X happen?", "Is it possible that ...?" |
| ✅ **Certain** | Every case is favourable; the probability is `1`. | "Must X be true?" |
| ✅ **Probability** | The **measured fraction** `favourable/total`. | "What is the probability ...?" |

- ⚠️ "Possible" and "probable" are **not** interchangeable: an event of probability `1/1000` is fully
  possible and highly improbable. In statement-based items, "it is not necessary that Y is correct"
  means **Y can fail in some consistent case** - one counter-case is enough, no probability needed.

### 4.2 Conditional statements: implication vs equivalence

```text
   A -> B   ("if A then B")
      |
      +-- ALSO TRUE : not B -> not A        (contrapositive - always valid)
      +-- NOT GIVEN : B -> A                (converse - a classic trap)
      +-- NOT GIVEN : not A -> not B        (inverse - equally invalid)

   A <-> B  ("A if and only if B") = BOTH A -> B and B -> A
```

| Relation | Symbol | What you may deduce |
|---|---|---|
| ✅ **Implication** | `A -> B` | A is **sufficient** for B; B is **necessary** for A; use the contrapositive freely. |
| ✅ **Equivalence** | `A <-> B` | Both directions; A and B are interchangeable. |

- ⚠️ **Transitivity is valid for implications:** from "every red is blue", "every blue is green" and
  "every green is yellow" it follows that every red is green **and** every red is yellow. The audited
  2026 Set-A paper contains exactly this chain, and it also contains a four-statement conditional
  puzzle whose two claims are settled purely by chaining contrapositives.
- ⚠️ **Converse is never valid from a one-way statement:** "every red is yellow" does **not** give
  "every yellow is red".

## 5. Original solved examples

### 📝 Example A (series - letters)

**A, C, F, J, ?** Positions 1, 3, 6, 10, 15 (gaps +2, +3, +4, +5; triangular numbers). Next `= 15` ->
**O.** *(Verified sequence 1,3,6,10,15.)*

### 📝 Example B (blood relation)

**A male speaker says, "She is the daughter of my paternal grandfather's only son."** The paternal
grandfather's only son is the speaker's father; the named woman is therefore the speaker's
**sister**. **Answer: sister.**

### 📝 Example C (counting)

**How many 3-digit numbers with distinct digits can be formed from {1, 2, 3, 4}?** `P(4,3) = 4 x 3 x 2
=` **24.** *(Verified.)*

### 📝 Example D (probability)

**A bag has 3 red and 2 blue balls; one is drawn. `P(red)`?** `3/(3+2) =` **3/5.** *(Verified.)*

### 📝 Example E (data interpretation)

Read this table:

| Month | Product X | Product Y |
|---|---:|---:|
| Jan | 200 | 150 |
| Feb | 250 | 180 |
| Mar | 300 | 120 |

- Total X `= 200 + 250 + 300 =` **750**; total Y `= 150 + 180 + 120 =` **450.**
- Percentage rise in X from Jan to Mar `= (300 - 200)/200 =` **50%.** *(Verified.)*

### 📝 Example F (communication - original)

**A colleague follows an outdated procedure after receiving two conflicting emails. What should a
team lead do first?** Clarify the current procedure privately, explain which instruction controls,
ask the colleague to restate it, and circulate one corrected instruction to the team. This addresses
the information failure without blame.

### 📝 Example G (implication chain - original)

> **Given.** Every scholarship holder is a hosteller. Every hosteller is a registered student.

**Which follow?**
(i) Every scholarship holder is a registered student. — **Follows** (transitivity of `->`).
(ii) Every registered student is a hosteller. — **Does not follow** (that is the converse).
(iii) Someone who is not a registered student is not a scholarship holder. — **Follows** (that is the
contrapositive of (i)).

**Answer: (i) and (iii) only.** *(Verified: the only valid moves from a one-way implication are
chaining and contraposition.)*

### 📝 Example H (circular arrangement)

**Five friends sit around a round table. In how many distinct seatings can they sit if rotations are
the same?** Fix A at the top to remove rotational duplicates. Arrange B, C, D and E in the remaining
seats: `4! =` **24**. A reflection is a different seating unless the stem says clockwise and
anticlockwise arrangements are identical. *(Verified.)*

### 📝 Example I (coding verification)

**If CAT becomes DBU and DOG becomes EPH, code SUN.** Each corresponding letter shifts `+1`:
`C->D, A->B, T->U` **and** `D->E, O->P, G->H`; the second pair verifies that the rule is not guessed
from one letter. Hence `S->T, U->V, N->O`: **TVO**.

### 📝 Example J (Venn/set range)

In a group of 50, 28 study A and 24 study B. The number studying both can be from
`max(0, 28+24-50) = 2` to `min(28,24) = 24`. Thus **2 to 24** are possible; choosing a single
overlap without further data is unjustified. *(Verified.)*

### 📝 Example K (constrained number with zero)

How many **five-digit** numbers can be made from 0, 1, 2, 3 and 4 without repetition? The first
place cannot be zero: 4 choices. The remaining four digits can be arranged in `4!` ways. Total:
`4 x 4! =` **96**. *(Verified.)*

### 📝 Example L (conditional probability without replacement)

A bag has 3 red and 2 blue balls. Given that the first draw is red and it is not replaced, the
probability that the second is red is `2/4 =` **1/2**. The probability of two reds in order is
`(3/5) x (2/4) = 3/10`: fractions do multiply, but the second is the **conditional** fraction.

### 📝 Example M (table, pie and dual-axis DI)

| Quarter | Output (thousand units) | Revenue (₹ lakh) | Product P share of revenue |
|---|---:|---:|---:|
| Q1 | 40 | 80 | 25% |
| Q2 | 50 | 90 | 30% |

- **Bar/table reading:** output rose by `10 thousand`, not 10%.
- **Dual-axis reading:** revenue per thousand units in Q2 is `90/50 = 1.8 lakh`, while Q1 is `2`;
  output rose but revenue per unit fell.
- **Pie/share reading:** P's Q2 revenue is `30% of 90 = 27 lakh`; its share rose by **5 percentage
  points**, or `5/25 = 20%` relatively. Name the requested measure before choosing an option.

### 📝 Example N (visual/cube and worst-case execution)

**Cube views.** A labelled cube shows faces `(1,2,3)` at one corner and `(1,4,5)` at another. Faces
2, 3, 4 and 5 are each adjacent to 1, so the remaining face **6 is opposite 1**. Do not infer an
opposite pair from a single view.

**Grid count.** A `3 x 3` square grid has `9` unit squares, `4` squares of side 2, and `1` of side
3: **14** total. Count by size, not by visual impression.

**Worst case.** From red and blue balls, how many draws ensure three of one colour? Take 2 red and
2 blue without reaching three, then one more: **5**.

## 6. Must-Know facts

- ✅ Order matters -> permutation; order does not -> combination; `P(n,r) = C(n,r) x r!`.
- ✅ Each **right** turn is 90 degrees clockwise; two rights = a U-turn (180).
- ✅ "Only son/daughter" removes other children of the **same stated sex**, not all siblings; map the
  maternal/paternal side and the speaker's sex before concluding.
- ✅ For a valid syllogism, a conclusion must hold in **every** arrangement, not just one.
- ✅ From `A -> B` you may use the **contrapositive**; you may never use the **converse**.
- ✅ "Possible" only needs one favourable case; "necessary/certain" needs every case.
- ✅ In DI, label **level / change / percentage change / share / percentage-point change / weighted
  rate**; a graph axis may use a different unit or scale from the other axis.
- ✅ In circular seating, fix one anchor; in a digit-number count, forbid leading zero before using a
  permutation.
- ✅ Venn overlap has lower and upper bounds; do not invent an intersection from two set sizes.
- ✅ In interpersonal items, prefer listening, clarity, fairness, legality, proportionality, and
  confirmation over humiliation, threats, concealment, or impulsive escalation.

## 7. Common traps

- ❌ Using permutations when order does not matter (or vice versa). -> Decide first.
- ❌ Reading "some A are B" as "all A are B". -> "Some" is existential, not universal.
- ❌ Reading `A -> B` as `B -> A`. -> Only the contrapositive is free.
- ❌ Treating "possible" as "probable", or "not necessary" as "false". -> "Not necessary" only means
  **at least one** consistent case makes it fail.
- ❌ In directions, treating a left turn as +90 clockwise. -> Left is anticlockwise.
- ❌ In DI, computing a total when a **change** or **percentage** was asked. -> Re-read the stem.
- ❌ Treating a circular rotation as a new arrangement. -> Fix one anchor before counting.
- ❌ Allowing zero in the first place of a multi-digit number. -> Choose the first digit separately.
- ❌ Multiplying unchanged fractions without replacement. -> Multiply sequential **conditional**
  fractions, or use combinations for an unordered draw.
- ❌ Reading a graph without its axis unit/scale or treating points as percent change. -> Label both
  axes and the base before computing.
- ❌ Declaring cube faces opposite from one view or double-counting a grid figure. -> Use all views
  and count by size/layer.
- ❌ Accepting a syllogism conclusion true in one diagram only. -> It must hold in **all**.
- ❌ Treating a communication problem as a character flaw before clarifying facts. -> Diagnose the
  information/process failure first.
- ❌ Treating every communication failure as conflict. -> First classify the barrier: physical,
  semantic/language, psychological, organisational, or technological.

## 8. Quick checks

- ✅ Can you decide permutation vs combination from the stem in one read?
- ✅ Can you sketch a family tree from "only son/daughter" clues?
- ✅ Can you write the contrapositive of a given "if ... then ..." instantly?
- ✅ Can you convert a table row into a percentage change quickly?

## 9. Mini-drill (with answers and explanations)

1. Next term: 5, 11, 23, 47, ...
2. In how many ways can the letters of "LEVEL" be arranged?
3. A man walks 3 km North, turns right and walks 4 km, turns right and walks 3 km. How far is he from
   the start, and in which direction?
4. Ten people each shake hands once with every other. How many handshakes?
5. Using the Section 5 table, what is the total sales of Product Y over the three months?
6. A bag holds 3 red and 2 blue balls. Two are drawn together at random. Is it **possible** to draw
   two blue balls, and what is the **probability** of drawing two red ones?
7. Given "if a file is approved, then it is signed" and "this file is not signed", what follows about
   approval?
8. Six people sit around a round table. How many distinct arrangements are there if rotations are the
   same?
9. How many four-digit numbers can be formed from 0, 1, 2 and 3 without repetition?
10. Of 60 students, 35 take Hindi and 28 take Tamil. What is the least possible number taking both?
11. A bag has 4 white and 6 black balls. Two are drawn in sequence without replacement. Find
    `P(white then white)`.
12. A pie slice rises from 20% to 25%. State the percentage-point change and the relative percent
    change.
13. How many squares are present in a `2 x 2` square grid?
14. From three colours of balls, how many draws ensure two balls of one colour?

**Answers.**

1. **95.** Each term is `x2 + 1`: `47 x 2 + 1 = 95`. *(Verified.)*
2. **30.** `5!/(2! x 2!) = 120/4 = 30` (E and L repeat twice). *(Verified.)*
3. **4 km, due East.** The two 3 km legs (N then S) cancel; the 4 km East leg remains. *(Verified.)*
4. **45.** `C(10,2) = 45`. *(Verified.)*
5. **450.** `150 + 180 + 120 = 450`. *(Verified.)*
6. **Yes, possible; `P(two red) = 3/10`.** Two blue is possible - exactly one such pair exists, so its
   probability is `1/C(5,2) = 1/10`, small but non-zero. Two red: `C(3,2)/C(5,2) = 3/10`.
   *(Verified: `C(5,2) = 10`.)* ⚠️ "Possible" was a yes/no question; "probability" was a number.
7. **The file was not approved.** That is the **contrapositive** of "approved -> signed", which is
   always valid. It does **not** follow that a signed file was approved - that would be the converse.
   *(Verified as a logical form.)*
8. **120.** Fix one person and arrange the other five: `5! = 120`.
9. **18.** First digit: 3 non-zero choices; then `3!` arrangements: `3 x 6`.
10. **3.** The lower overlap bound is `35 + 28 - 60 = 3`.
11. **2/15.** `P(W₁) x P(W₂|W₁) = (4/10) x (3/9)`.
12. **+5 percentage points; +25% relative change.** The second uses `5/20`, not `5/25`.
13. **5.** Four unit squares plus one large square.
14. **4.** In the worst case, take one of each colour first, then one more.

## 10. Timed transfer, diagnosis and retry gate

Attempt items 8-12 plus one seating/coding/DI question of your choice in **nine minutes**. For each
miss, diagnose before checking the answer:

| Symptom | Code | Repair |
|---|---|---|
| Rotation or reflection double-counted | C/A | Anchor one seat; read whether reflections are distinct. |
| Leading zero or repetition rule lost | R | Write allowed first-place digits before any factorial. |
| One Venn intersection assumed | C | Write lower and upper overlap bounds. |
| Without-replacement fraction unchanged | A | Write `P(B|A)` explicitly. |
| Graph/share measure confused | R/X | Label level, share, points, and relative change before arithmetic. |

**Retry gate:** after a 20-minute gap, score **6/6 in nine minutes** with no C/R error. Otherwise
redo the matching worked example and retry fresh values. The Advanced companion is optional speed
depth, not a prerequisite for this gate.

## 11. Study links

- ✅ [Optional Advanced companion](../advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md) -
  multi-constraint seating, harder syllogisms, and speed depth. Core above independently covers the
  required arrangement, Venn, coding, counting, probability, and DI mechanisms.
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - decision-making shares the sufficiency
  mindset.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - counting rests on factor and number sense.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
## 2026 PYQ Integration

> **Status:** 2026 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2026.md`.
> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are **provisional**; no option or answer is recorded or inferred in this integration.

- **Year represented:** 2026
- **Paper(s):** CSAT
- **Routed question demands:** 21

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2026 | CSAT | 9 | Constrained-word permutation count | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 14 | Circular-seating arrangement | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 15 | Painted-region pattern count | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 23 | Weighing-combination count | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 33 | Ranking-order logic | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 34 | Segment-matching puzzle | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 35 | Group-seating constraints | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 36 | Statement-implication logic | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 44 | Blood-relation tree | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 48 | Transitive-colour syllogism | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 51 | Odd-item weighing logic | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 56 | Direction turns and distance | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 67 | Letter-code decoding | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 70 | Weighted-score data table | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 71 | Statement-relationship logic | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 72 | Communication: relationship matching | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 73 | Communication: tool-purpose matching | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 74 | Communication: conflict scenario | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 75 | Communication: barrier-example matching | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 76 | Communication: questionnaire scenario | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 77 | Communication: statements | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Constrained-word permutation count
- Circular-seating arrangement
- Painted-region pattern count
- Weighing-combination count
- Ranking-order logic
- Segment-matching puzzle
- Group-seating constraints
- Statement-implication logic
- Blood-relation tree
- Transitive-colour syllogism
- Odd-item weighing logic
- Direction turns and distance
- Letter-code decoding
- Weighted-score data table
- Statement-relationship logic
- Communication: relationship matching
- Communication: tool-purpose matching
- Communication: conflict scenario
- Communication: barrier-example matching
- Communication: questionnaire scenario
- Communication: statements

> This block integrates the 2026 examinable demand and paper metadata. It is kept separate from the 2018-2023 and 2024-2025 blocks and does not convert a provisionally-keyed, answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2026 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
## Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2024-2025.md`.
> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded or inferred in this integration.

- **Years represented:** 2024, 2025
- **Paper(s):** CSAT
- **Routed question demands:** 24

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | CSAT | 24 | Sequence completion | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 45 | Digit-frequency counting | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 48 | Alphametic addition | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 49 | Constrained-triplet count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 56 | Multi-turn direction sense | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 57 | Rotational direction sense | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 58 | Conclusion validity | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 74 | Implication consistency | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 75 | Operator substitution | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 77 | Alphabetic-number coding | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 78 | Letter-rearrangement coding | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 80 | Coded-value constraints | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 8 | Month-pattern sequence | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 29 | Alphametic subtraction | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 30 | Letter-pattern completion | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 38 | Coded-operator arrangement | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 49 | Suspect-statement logic | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 50 | Tournament-score logic | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 55 | Family-relation deductions | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 56 | Multiplicative-letter code | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 57 | Letter-digit substitution | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 58 | Constrained-digit arrangement | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 65 | Direction-network distance | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 66 | Numeric-cube code | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Sequence completion
- Digit-frequency counting
- Alphametic addition
- Constrained-triplet count
- Multi-turn direction sense
- Rotational direction sense
- Conclusion validity
- Implication consistency
- Operator substitution
- Alphabetic-number coding
- Letter-rearrangement coding
- Coded-value constraints
- Month-pattern sequence
- Alphametic subtraction
- Letter-pattern completion
- Coded-operator arrangement
- Suspect-statement logic
- Tournament-score logic
- Family-relation deductions
- Multiplicative-letter code
- Letter-digit substitution
- Constrained-digit arrangement
- Direction-network distance
- Numeric-cube code

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

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
| 2018 | CSAT | 66 | Figural analogy completion | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 67 | Graph break-even reading | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 70 | Figural rotation series | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2020 | CSAT | 34 | Sequence pair counting | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2021 | CSAT | 27 | Matrix trend missing entry | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 28 | Dual-sequence missing entry | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 35 | Venn set overlap range | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 40 | Alphabet reversal position coding | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 45 | Table run-rate comparison | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2022 | CSAT | 79 | Form constraint number count | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 4 | Worst-case pair selection | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 5 | Score partition counting | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 6 | Derangement possibility check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 18 | Interior cube count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 19 | Position-constrained permutation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 24 | Symbol operation decode | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 30 | Collinearity-aware triangle count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 36 | Worst-case colour group draw | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 37 | Letter-shift cipher decode | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 38 | Statement-based age ranking | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 39 | Family-relation statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 40 | Prime-group odd-one-out | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 48 | Circular consecutive selection count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 54 | Circular pass-sequence return | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 55 | Sequence middle term | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
