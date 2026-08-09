# Algebra, Inequalities and Data Sufficiency - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Analytical ability / decision-making.
> **Core skill:** translate words to equations, handle inequalities and quantitative comparison, and
> master the UPSC two-statement **data-sufficiency** decision.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md).*

---

## 1. Visual foundation

```text
   A RELATION PROBLEM
        |
   +----------------+------------------+
   |                |                  |
 SOLVE            COMPARE           DECIDE
 equations        inequality/QC     data sufficiency
 (find value)     (which is bigger) (is info enough?)
        |
   for DS, ask NOT "what is the value" but "CAN it be found?"
```

**Core proposition:** data sufficiency tests a **decision** ("is the information enough?"), not a
computation - the fastest solvers often **never** find the value.

## 2. The UPSC data-sufficiency format (read it, do not recall it)

✅ A CSAT data-sufficiency item gives a **Question** followed by two **Statements I and II**. The
first three options are stable across the audited papers; **the fourth is not**.

| Option | Meaning (stable across 2024, 2025 and 2026 Set A) |
|---|---|
| **(a)** | Answerable using **one** statement alone, but **not** the other alone. |
| **(b)** | Answerable using **either** statement alone. |
| **(c)** | Answerable using **both** statements **together**, but not either alone. |
| **(d)** | ⚠️ **Varies - read it.** See the table below. |

### ⚠️ The fourth option is not a fixed template

| Audited paper | Printed wording of (d) | What it means |
|---|---|---|
| 2024 Set A (per item) | "The Question **cannot** be answered even by using both the Statements together" | Nothing works. |
| 2025 Set A (some items) | "The Question **cannot** be answered even using any of the Statements" | Nothing works. |
| 2025 Set A (other items) | "The Question **can** be answered even **without** using any of the Statements" | The **question alone is self-sufficient**. |
| 2026 Set A (shared block of 5) | "the question cannot be answered even using any of the statements" | Nothing works. |

- ✅ **Both 2025 variants appear in the same paper.** Two of the five audited 2025 data-sufficiency
  items print the "cannot" form and three print the "even without" form.
- 🔑 **Consequence:** a candidate who marks (d) from memory as "nothing works" will mark the exact
  opposite verdict on a "can be answered without any statement" item. **Always read (d) before
  deciding.**
- ✅ **Layout also differs:** 2024 and 2025 repeat the directions and all four options **inside every
  item**; 2026 prints them **once** above a block of five items. In 2026 you must scroll back to the
  block header to see what (d) says.

> 🔑 **DS discipline:** test **Statement I alone**, then **Statement II alone**, and only then **both
> together** - but before any of that, check whether the **question is already answerable on its own**,
> because in this paper that can be a live option. Do the value-finding **only** far enough to see
> whether the answer is **unique**.

### Necessary vs sufficient (the distinction the format is built on)

| Term | Test | In a DS item |
|---|---|---|
| ✅ **Sufficient** | Having it **settles** the question. | A statement is "sufficient" only if it forces **exactly one** answer. |
| ✅ **Necessary** | The conclusion **cannot hold without** it. | A statement can be necessary yet insufficient - it narrows without pinning. |

- ⚠️ In `A -> B`: A is **sufficient** for B; B is **necessary** for A. They are not interchangeable,
  and a statement that is merely necessary is **not** enough to mark (a) or (b).

## 3. Essential algebra and inequality facts

| Tool | Rule | Edge condition |
|---|---|---|
| ✅ **Linear solve** | Isolate the variable; one equation fixes one unknown. | Only if the coefficient is non-zero. |
| ✅ **Two unknowns** | Need **two independent** equations; a multiple of one is not independent. | Inconsistent pairs give **no** solution; dependent pairs give **many**. Both block a unique answer. |
| ✅ **Inequality flip** | Multiplying/dividing by a **negative** reverses the sign. | Adding/subtracting **never** flips it. |
| ✅ **Dividing by a variable** | Only legal if you know it is non-zero. | If its **sign** is unknown, the inequality direction is unknown too - split into cases. |
| ✅ **Squaring to compare** | `a > b >= 0  =>  a^2 > b^2`. | Fails if either side may be negative. |
| ✅ **Quantitative comparison** | Reduce both quantities to the **same base/form** before comparing. | `x^m` vs `x^n` reverses for `0 < x < 1`. |
| ✅ **Sum-difference** | Two numbers with sum `S`, difference `D`: they are `(S+D)/2` and `(S-D)/2`. | Integer answers need `S` and `D` of the same parity. |

## 4. Method

1. **Solve items:** translate each sentence to one equation; count unknowns vs independent equations.
2. **Inequality/QC items:** rewrite both sides in a comparable form (same base, same power); watch the
   sign rule.
3. **DS items - in this order:**
   1. **Read the four printed options**, especially (d).
   2. Ask whether the **question alone** already pins the answer (a live verdict in this paper).
   3. Test **I alone**, then **II alone**, then **both** - stopping at **uniqueness**, not the value.

## 5. Original solved examples

### 📝 Example A (solve)

**Solve `3x + 5 = 20`.** `3x = 15` -> `x =` **5.** *(Verified.)*

### 📝 Example B (sum-difference)

**Two numbers have sum 30 and difference 8.** They are `(30+8)/2 = 19` and `(30-8)/2 = 11`. **19 and
11.** *(Verified.)*

### 📝 Example C (quantitative comparison)

**Which is larger, `2^30` or `3^20`?** `2^30 = 8^10`, `3^20 = 9^10` -> `9^10 > 8^10` -> **`3^20` is
larger.** *(Verified: 1073741824 < 3486784401.)*

### 📝 Example D (data sufficiency, answer (c))

**Question:** What is the two-digit number N?
Statement I: N is divisible by 11.
Statement II: The tens digit of N is 3.

I alone -> 11, 22, ..., 99 (not unique). II alone -> 30-39 (not unique). Both -> divisible by 11 **and**
tens digit 3 -> **33** (unique). **Answer: (c).**

### 📝 Example E (data sufficiency, answer (b))

**Question:** Is the integer n even?
Statement I: n^2 is even.
Statement II: n + 1 is odd.

I alone -> n^2 even forces n even (sufficient). II alone -> n+1 odd forces n even (sufficient). Each
works alone. **Answer: (b).**

### 📝 Example F (the self-sufficient question - the 2025 fourth-option variant)

**Question:** What is the smallest **two-digit** number having exactly **three** distinct factors?
Statement I: the number is odd.
Statement II: the number is divisible by 5.

A number has exactly three distinct factors only if it is the **square of a prime** (`1, p, p^2`).
Two-digit prime squares are `25` and `49`, so the smallest is **25** - and that came from the
**question alone**. Statement I is true of 25 and Statement II is true of 25, but **neither was
needed**.

**Verdict:** the question is answerable **without** either statement. Under the 2025-style fourth
option ("The Question can be answered even **without** using any of the Statements") that is **(d)**.
Under a 2024-style fourth option ("cannot be answered even by using both together") the same
reasoning would make (d) **wrong** and the printed set would have to be re-read.
*(Verified: divisors of 25 = {1, 5, 25}; of 49 = {1, 7, 49}; no smaller two-digit number has exactly
three.)*

> 🔑 **This is the whole lesson of Section 2:** the same reasoning maps to different letters depending
> on what is printed. Solve the logic, then read the label.

## 6. Must-Know facts

- ✅ Two independent linear equations are needed to pin two unknowns; `2x + 4y = 20` adds **nothing** to
  `x + 2y = 10`.
- ✅ In DS, a statement is "sufficient" only if it yields a **single** answer; a statement that merely
  narrows the field is **necessary at best**, never sufficient.
- ✅ **Sufficiency is about the answer, not about the arithmetic.** Never finish the calculation.
- ✅ Reversing an inequality happens on multiply/divide by a negative - **not** on adding a negative.
  Adding the same quantity to both sides never flips the sign.
- ✅ Squaring both sides preserves order **only when both sides are non-negative**.
- ✅ For QC, common tricks: equalise exponents, take roots, or compare ratios.

## 7. Common traps

- ❌ Computing the value in a DS item when you only need "is it unique?". -> Stop at uniqueness.
- ❌ **Marking (d) from memory.** -> The printed (d) differs between the audited years and even
  between items of the same 2025 paper; read it.
- ❌ Missing that the **question alone** may already be answerable. -> Check that first.
- ❌ Treating a scaled copy of an equation as new information. -> It is dependent.
- ❌ Confusing **necessary** with **sufficient** ("n is even" is necessary for "n is a multiple of 6",
  but nowhere near sufficient). -> Ask which direction the arrow points.
- ❌ Forgetting to flip the inequality on a negative multiplier. -> Flip the sign.
- ❌ In DS, checking "both together" **before** testing each alone. -> Test each alone first (it may be
  (a) or (b)).
- ❌ Assuming "cannot be found" without trying **both together**. -> That verdict requires both to fail.

## 8. Quick checks

- ✅ Can you state options (a), (b) and (c) - and did you just **read** (d) off the paper?
- ✅ Do you test I alone and II alone **before** combining?
- ✅ Can you say which of two conditions is necessary and which is sufficient?
- ✅ Can you compare `a^m` and `b^n` by equalising exponents?

## 9. Mini-drill (with answers and explanations)

1. Solve the inequality `2x - 3 > 7`.
2. Compare `(0.5)^3` and `(0.5)^2`.
3. **DS.** Question: What is the two-digit number? I: The sum of its digits is 9. II: The difference of
   its digits is 9.
4. **DS.** Question: What is x? I: `3x = 12`. II: `x + 7 = 11`.
5. Two numbers have sum 30 and difference 8. Find them.
6. For the claim "`n` is a multiple of 12", is "`n` is even" **necessary**, **sufficient**, both, or
   neither?
7. **DS.** Question: What is the smallest integer greater than 1 that is both a perfect square and a
   perfect cube? I: it is even. II: it is less than 100.

**Answers.**

1. **x > 5.** Add 3, divide by 2. *(Verified.)*
2. **`(0.5)^3 < (0.5)^2`** (0.125 < 0.25): for a base between 0 and 1, a higher power is smaller.
   *(Verified.)*
3. **(a).** I alone: 18, 27, 36, ..., 90 (many). II alone: digits differing by 9 -> only **90** (since
   9 and 0), unique. So one statement (II) alone answers it but not the other. *(Verified: only 90.)*
4. **(b).** I alone -> x = 4; II alone -> x = 4. Either works. *(Verified.)*
5. **19 and 11.** `(30±8)/2`. *(Verified.)*
6. **Necessary but not sufficient.** Every multiple of 12 is even, so evenness cannot be dropped; but
   14 is even and not a multiple of 12, so evenness does not settle it. *(Verified counter-example.)*
7. **The question is self-sufficient.** A number that is both a square and a cube is a **6th power**;
   the smallest above 1 is `2^6 = 64`. Neither statement was used - both merely happen to be true of
   64. Under the 2025-style fourth option that is **(d)**; under a 2024-style fourth option it is not,
   so **read the printed options** before marking. *(Verified: `64 = 8^2 = 4^3`; next is `3^6 = 729`.)*

## 10. Study links

- ✅ [Advanced companion](../advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md) - dependent-
  statement DS, unique-root logic, and inequality ranges.
- ✅ [Reading Comprehension](./01_Reading-Comprehension.md) - "is it supported?" mirrors "is it sufficient?".
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - number properties power many DS items.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 41

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 2 | Series equation solving | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 23 | Range inequality deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 24 | Expression magnitude comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 34 | Digit-constraint algebra | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 37 | Inequality chain deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 38 | Algebraic revenue expression | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 77 | Equation implication deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 18 | Age ratio equations | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 37 | Bounded inequality range | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 38 | Age variable algebra | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 50 | Fraction comparison property | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 58 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 69 | Piece-length ratio algebra | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 9 | Equal-expression ordering | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 16 | Digit-constraint sum puzzle | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 17 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 28 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 29 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 30 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 79 | Vessel weight linear equation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 8 | Exponential model identification | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 38 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 39 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 47 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 58 | Two-variable score algebra | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 77 | Age-relation algebra | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 19 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 25 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 28 | Reverse chain equation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 37 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 48 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 49 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 50 | Two-statement sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 60 | Percentage inequality comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 78 | Consecutive integer equation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 26 | Two-group sum product maximum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 56 | Two-statement inequality sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 57 | Two-statement integer sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 58 | Two-statement set-size sufficiency | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 59 | Two-statement digit-number sufficiency | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 60 | Two-statement age-sequence sufficiency | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Series equation solving
- Range inequality deduction
- Expression magnitude comparison
- Digit-constraint algebra
- Inequality chain deduction
- Algebraic revenue expression
- Equation implication deduction
- Age ratio equations
- Bounded inequality range
- Age variable algebra
- Fraction comparison property
- Two-statement sufficiency
- Piece-length ratio algebra
- Equal-expression ordering
- Digit-constraint sum puzzle
- Vessel weight linear equation
- Exponential model identification
- Two-variable score algebra
- Age-relation algebra
- Reverse chain equation
- Percentage inequality comparison
- Consecutive integer equation
- Two-group sum product maximum
- Two-statement inequality sufficiency
- Two-statement integer sufficiency
- Two-statement set-size sufficiency
- Two-statement digit-number sufficiency
- Two-statement age-sequence sufficiency

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
