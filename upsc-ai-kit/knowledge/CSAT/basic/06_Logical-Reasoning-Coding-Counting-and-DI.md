# Logical Reasoning, Coding, Counting and Data Interpretation - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Logical reasoning / decision-making / data interpretation.
> **Core skill:** arrangements, blood relations, directions, coding, series, basic counting/probability,
> and reading data tables - a large, high-yield CSAT family.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md`.*

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
| ✅ **Counting** | Permutations `P(n,r) = n!/(n-r)!`; combinations `C(n,r) = n!/(r!(n-r)!)`. |
| ✅ **Probability** | `P = favourable / total` for equally likely outcomes. |
| ✅ **Data interpretation** | Read exactly what is asked; compute totals, differences, and percentages from the table. |

> 🔑 **Arrangement rule:** always start from the clue that **fixes the most**; a single anchored
> position usually cascades to the full solution.

## 3. Method

1. Classify the sub-skill and **draw the structure** (row, circle, tree, compass, table).
2. Enter the **strongest constraint** first, then the next, checking consistency each time.
3. For counting/probability, decide **order matters?** (permutation) or **not** (combination) before
   computing.
4. For DI, answer the **exact** quantity asked (total / change / percent), not a nearby one.

## 4. Formulas and rules

- ✅ `P(n,r) = n!/(n-r)!` (arrangements, order matters).
- ✅ `C(n,r) = n!/(r!(n-r)!)` (selections, order does not matter).
- ✅ Arrangements of a word with repeats: `total! / (product of repeat factorials)`.
- ✅ `P(not E) = 1 - P(E)`; for equally likely outcomes, `P = favourable/total`.
- ✅ Handshakes / lines among n points = `C(n,2)`.

## 5. Original solved examples

### 📝 Example A (series - letters)

**A, C, F, J, ?** Positions 1, 3, 6, 10, 15 (gaps +2, +3, +4, +5; triangular numbers). Next `= 15` ->
**O.** *(Verified sequence 1,3,6,10,15.)*

### 📝 Example B (blood relation)

**"She is the daughter of my grandfather's only son."** The grandfather's only son is the speaker's
**father**; his daughter is the speaker's **sister**. **Answer: sister.**

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

## 6. Must-Know facts

- ✅ Order matters -> permutation; order does not -> combination.
- ✅ Each **right** turn is 90 degrees clockwise; two rights = a U-turn (180).
- ✅ "Only son/daughter" is a strong clue - it removes siblings from the tree.
- ✅ For a valid syllogism, a conclusion must hold in **every** arrangement, not just one.
- ✅ In DI, watch whether the question wants an **absolute** number or a **percentage/ratio**.

## 7. Common traps

- ❌ Using permutations when order does not matter (or vice versa). -> Decide first.
- ❌ Reading "some A are B" as "all A are B". -> "Some" is existential, not universal.
- ❌ In directions, treating a left turn as +90 clockwise. -> Left is anticlockwise.
- ❌ In DI, computing a total when a **change** or **percentage** was asked. -> Re-read the stem.
- ❌ Accepting a syllogism conclusion true in one diagram only. -> It must hold in **all**.

## 8. Quick checks

- ✅ Can you decide permutation vs combination from the stem in one read?
- ✅ Can you sketch a family tree from "only son/daughter" clues?
- ✅ Can you convert a table row into a percentage change quickly?

## 9. Mini-drill (with answers and explanations)

1. Next term: 5, 11, 23, 47, ...
2. In how many ways can the letters of "LEVEL" be arranged?
3. A man walks 3 km North, turns right and walks 4 km, turns right and walks 3 km. How far is he from
   the start, and in which direction?
4. Ten people each shake hands once with every other. How many handshakes?
5. Using the Section 5 table, what is the total sales of Product Y over the three months?

**Answers.**

1. **95.** Each term is `x2 + 1`: `47 x 2 + 1 = 95`. *(Verified.)*
2. **30.** `5!/(2! x 2!) = 120/4 = 30` (E and L repeat twice). *(Verified.)*
3. **4 km, due East.** The two 3 km legs (N then S) cancel; the 4 km East leg remains. *(Verified.)*
4. **45.** `C(10,2) = 45`. *(Verified.)*
5. **450.** `150 + 180 + 120 = 450`. *(Verified.)*

## 10. Study links

- ✅ Advanced companion: `advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md` - multi-constraint
  seating, syllogisms, dice probability, and inclusion-exclusion counting.
- ✅ `05_Algebra-Inequalities-and-Data-Sufficiency.md` (basic) - decision-making shares the sufficiency
  mindset.
- ✅ `02_Number-Systems-and-Number-Sense.md` (basic) - counting rests on factor and number sense.
