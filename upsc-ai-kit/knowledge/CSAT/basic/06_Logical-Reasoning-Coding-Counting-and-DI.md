# Logical Reasoning, Coding, Counting and Data Interpretation - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Logical reasoning / decision-making / data interpretation.
> **Core skill:** arrangements, blood relations, directions, coding, series, basic counting/probability,
> data tables, and interpersonal/communication decision method.
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
| ✅ **Linear/circular arrangement** | Draw seats; place the most-constrained clue first. |
| ✅ **Blood relations** | Build a small family tree; resolve "only son/daughter" carefully. |
| ✅ **Directions** | Sketch N-E-S-W; each right turn is +90 clockwise. |
| ✅ **Coding-decoding** | Find the rule (shift, reverse, position-value) from the given pair, then apply. |
| ✅ **Series** | Test differences, ratios, and known sequences (squares, triangular, primes). |
| ✅ **Conditional/statement logic** | Rewrite every "if ... then ..." as `A -> B`; chain implications and use contrapositives; never the converse. |
| ✅ **Counting** | Permutations `P(n,r) = n!/(n-r)!`; combinations `C(n,r) = n!/(r!(n-r)!)`. |
| ✅ **Probability** | `P = favourable / total` for equally likely outcomes. |
| ✅ **Data interpretation** | Read exactly what is asked; compute totals, differences, and percentages from the table. |
| ✅ **Interpersonal/communication scenario** | Listen for interests, communicate neutrally, choose a lawful and proportionate response, and verify understanding. |
| ✅ **Communication matching** | Distinguish relationship type, tool purpose, channel, feedback, and barrier from the function described. |
| ✅ **Questionnaire design** | Use clear, neutral, single-issue questions; avoid leading, double-barrelled, ambiguous, or intrusive wording. |

The provisional 2026 Set-A audit places six explicit interpersonal/communication items at Q72-Q77.
This is a year-specific observed block, not evidence that every CSAT paper uses the same count.

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
- ✅ `P(not E) = 1 - P(E)`; for equally likely outcomes, `P = favourable/total`. *Every probability
  lies in `[0, 1]`; an answer outside that range is a signal you counted the sample space wrongly.*
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

## 6. Must-Know facts

- ✅ Order matters -> permutation; order does not -> combination; `P(n,r) = C(n,r) x r!`.
- ✅ Each **right** turn is 90 degrees clockwise; two rights = a U-turn (180).
- ✅ "Only son/daughter" removes other children of the **same stated sex**, not all siblings; map the
  maternal/paternal side and the speaker's sex before concluding.
- ✅ For a valid syllogism, a conclusion must hold in **every** arrangement, not just one.
- ✅ From `A -> B` you may use the **contrapositive**; you may never use the **converse**.
- ✅ "Possible" only needs one favourable case; "necessary/certain" needs every case.
- ✅ In DI, watch whether the question wants an **absolute** number or a **percentage/ratio**.
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

## 10. Study links

- ✅ [Advanced companion](../advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md) - multi-constraint
  seating, syllogisms, dice probability, and inclusion-exclusion counting.
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - decision-making shares the sufficiency
  mindset.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - counting rests on factor and number sense.
