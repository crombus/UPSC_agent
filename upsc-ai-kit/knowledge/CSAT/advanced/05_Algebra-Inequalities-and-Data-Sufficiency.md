# Algebra, Inequalities and Data Sufficiency - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Analytical ability / decision-making.
> **Core skill:** unique-root traps, dependent-statement data sufficiency, quantitative comparison of
> surds/powers, and inequality ranges under constraints.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/05_Algebra-Inequalities-and-Data-Sufficiency.md).*

---

## 1. Architecture

```text
   DECISION / RELATION PROBLEM
        |
   +------------------+---------------------+
   |                  |                     |
 SUFFICIENCY        COMPARISON           CONSTRAINT
 unique answer?     equalise form        range/optimum
 (I / II / both)    (surd, power, ratio) (min/max under bounds)
        |
   answer the QUESTION ASKED (enough? / bigger? / range?), not the value by reflex
```

**Analytical claim:** the advanced trap is **false uniqueness** - a statement that looks sufficient but
allows two values (e.g., `n^2 = 49` -> `n = ±7`), or two statements that are secretly the same.

## 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Unique-root test** | Over the reals, `x^2 = k` gives two roots for `k > 0`, one for `k = 0`, and none for `k < 0`; `x^3 = k` gives one. | A squared/absolute constraint alone is often **in**sufficient; a cubic or odd-power one usually is not. |
| ✅ **Dependent statements** | If II is a multiple/rearrangement of I - or is **logically implied** by I - it adds nothing. | Two unknowns need two **independent** relations. Nesting can be hidden behind different-looking wording. |
| ✅ **Necessary vs sufficient** | In `A -> B`, A is sufficient for B, B is necessary for A. | Two individually **necessary** statements can be jointly **sufficient** - that is exactly the (c) verdict. |
| ✅ **Surd comparison** | Compare `sqrt a + sqrt b` vs `sqrt c` by squaring (both sides positive). | Squaring preserves order only for non-negative quantities. |
| ✅ **AM-GM / bounded optimum** | For non-negative real parts with fixed sum, the product is maximised at equal parts. | AM-GM itself needs non-negative terms; for integer parts choose the nearest permitted integers, and respect any positive/distinct bounds. |
| ✅ **Interval arithmetic** | For `a < x < b`, `c < y < d`: `a+c < x+y < b+d`. | For a product on a rectangular interval, compare all four endpoint products; retain open/closed endpoints. Division additionally requires the divisor interval to exclude zero. |

## 3. Harder methods (worked)

### 📝 Method 1 - false uniqueness in DS

**Question:** What is the integer n? **I:** `n^2 = 49`. **II:** `n^3 = 343`.
I alone -> `n = 7` or `n = -7` (**not** unique). II alone -> `n = 7` only (unique). So one statement (II)
alone answers it but the other does not. **Answer: (a).** *(Verified: `(-7)^2 = 49` but `(-7)^3 =
-343`.)*

### 📝 Method 2 - dependent statements

**Question:** What is `x + y`? **I:** `x + 2y = 10`. **II:** `2x + 4y = 20`.
II is exactly `2 x` I, so it adds no information. Two unknowns, one independent equation -> `x + y` is
not determined. **Answer: (d).** *(Verified: e.g. (10,0) and (8,1) both satisfy, giving x+y = 10 and 9.)*

### 📝 Method 3 - surd comparison

**Which is larger, `sqrt50 + sqrt72` or `sqrt200`?** `sqrt50 + sqrt72 ≈ 7.07 + 8.49 = 15.56`;
`sqrt200 ≈ 14.14`. So **`sqrt50 + sqrt72` is larger.** *(Verified.)* (Note `sqrt50 + sqrt72 = 5 sqrt2 +
6 sqrt2 = 11 sqrt2 ≈ 15.56`, while `sqrt200 = 10 sqrt2`.)

### 📝 Method 4 - verdict first, letter second (the escalation this paper punishes)

⚠️ Advanced DS is a **two-stage** decision. Stage 1 produces a **verdict**; stage 2 maps it to a
**printed letter**. The audited papers do not use one fixed mapping (see
[basic/05](../basic/05_Algebra-Inequalities-and-Data-Sufficiency.md), Section 2), so never fuse the stages.

```text
STAGE 1 - VERDICT (pure logic, no letters)
  Q alone pins it?  -----------------------------> SELF-SUFFICIENT
  else I alone pins it?  and II alone pins it?
        both  -> EITHER ALONE
        one   -> EXACTLY ONE ALONE
        none  -> do they pin it TOGETHER?
                    yes -> BOTH NEEDED
                    no  -> NEITHER SUFFICES
STAGE 2 - MAP to whatever (a)/(b)/(c)/(d) actually say on this paper
```

| Verdict from Stage 1 | Maps to, in the audited papers |
|---|---|
| Exactly one alone | **(a)** in all three years. |
| Either alone | **(b)** in all three years. |
| Both needed | **(c)** in all three years. |
| Neither suffices | **(d)** where (d) reads "cannot be answered ...". |
| Self-sufficient question | **(d)** only where (d) reads "can be answered even **without** ..."; otherwise **no option fits** and you must re-read the stem for what it really asks. |

- 🔑 **Escalation rule:** if your verdict is "self-sufficient" but (d) says "cannot be answered", you
  have almost certainly misread the question - go back to the stem, not to the statements.

### 📝 Method 5 - optimum and interval endpoints

**Integer optimum.** Positive integers `x,y` have `x+y=11`. Their product is largest at the nearest
integers to `11/2`: `x,y = 5,6`, so the maximum is **30**, not `11²/4 = 30.25` (which is the real,
not integer, bound). AM-GM applies because the parts are positive.

**Endpoint-aware interval.** If `-2 < x <= 3` and `1 <= y < 4`, the four limiting corner products
are `-2, -8, 3, 12`. Thus `-8 < xy < 12`: neither extreme is reached because the responsible
endpoint (`x=-2` for the minimum and `y=4` for the maximum) is excluded. Do not silently convert
open bounds into closed ones.

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Stop at uniqueness** in DS; never fully solve. *Safe always - it is the whole skill.*
- ⚠️ **Spot dependence** by checking whether one statement is a scalar multiple of the other. *Safe
  always.*
- ⚠️ **Factor out common surds** (`11 sqrt2` vs `10 sqrt2`) to compare instantly. *Safe when a common
  radical exists.*
- ⚠️ **Equal-parts optimum** for a fixed-sum product. *Use AM-GM only for non-negative parts; for
  integers use the nearest permitted integers to the mean, then check any bounds/distinctness rule.*

## 5. Boundary cases

- ⚠️ A statement with a **square or absolute value** frequently permits **two** values - treat it as
  insufficient until proven unique.
- ⚠️ Two equations can be **inconsistent** (no solution) as well as dependent (many solutions) - both
  block a unique answer.
- ⚠️ Interval products need all four corner products even when neither interval straddles zero; then
  preserve whether each extremal endpoint is open or closed. Interval division is unsafe if the
  divisor interval contains zero.

## 6. Advanced traps

- ❌ Calling `n^2 = 49` sufficient. -> It allows `n = ±7`. Same for `|n - 3| = 5`.
- ❌ Adding a scaled duplicate equation as new information. -> It is dependent.
- ❌ Missing **logical** (not algebraic) dependence - II may be implied by I without looking like it.
  -> Ask "does I already force II?".
- ❌ Treating a **necessary** condition as sufficient. -> "Divisible by 3" does not give "divisible
  by 6"; the pair does.
- ❌ Multiplying corresponding interval endpoints. -> Take all four corners and preserve endpoint
  inclusion; never divide through an interval containing zero.
- ❌ Comparing surds by rough decimals when they are close. -> Square or factor the common radical.
- ❌ Reflexively computing a value in DS. -> Decide sufficiency and move on.
- ❌ Choosing the DS letter before reading what that letter says on **this** paper. -> Verdict first,
  letter second (Method 4).

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| False uniqueness | A | For squares/absolute values, ask "could it be negative too?". |
| Missed dependence | C | Check both `II = k x I` **and** `I => II`. |
| Necessary treated as sufficient | C | Write the arrow, then read it in the right direction. |
| Over-solving DS | T | Stop the instant uniqueness is clear. |
| Interval-product sign errors | X | Tabulate the four corner products. |
| Surd comparison slips | X | Factor the common radical before deciding. |
| Right verdict, wrong letter | R | Re-read the printed option set before marking. |

## 8. Advanced drill (with full solutions)

> ⚠️ These items are **new** - they do not repeat Methods 1-4 above or the Foundation file. Give each
> a verdict **before** looking for a letter.

1. **DS.** Question: Is the real number `x` positive? I: `x^3 > 0`. II: `x^2 > 0`.
2. **DS.** Question: What is the two-digit number `N`? I: `N` is a multiple of 9 and `N < 30`.
   II: the digits of `N` sum to 9.
3. **DS.** Question: What is the integer `n`? I: `|n - 3| = 5`. II: `n > 0`.
4. **DS.** Question: Is the positive integer `n` divisible by 6? I: `n` is divisible by 3.
   II: `n` is even.
5. Given `-2 < x < 3` and `1 < y < 4`, state the range of `xy`.
6. Which is larger, `5^100` or `3^150`?
7. Positive integers `a` and `b` satisfy `a+b=17`. What is their maximum product?
8. Given `-1 <= x < 2` and `2 <= y <= 5`, state the range of `xy`.

**Solutions.**

1. **(a).** I: a cube keeps the sign of its base, so `x^3 > 0` forces `x > 0` - **sufficient**.
   II: `x^2 > 0` only rules out `x = 0`; `x = -4` satisfies it - **insufficient**. Exactly one alone
   works. *(Verified: `(-4)^3 = -64 < 0` but `(-4)^2 = 16 > 0`.)*
2. **"Neither suffices" -> the "cannot be answered" verdict.** I alone -> {18, 27}. II alone ->
   {18, 27, 36, 45, 54, 63, 72, 81, 90}. **Together** -> still {18, 27}, because II adds nothing that
   I did not already imply: every multiple of 9 has digit sum 9 here. Two survivors, so no unique
   answer even jointly. *(Verified by enumeration.)* This is the **hidden-dependence** trap: two
   statements can look independent and be logically nested.
3. **(c).** I alone -> `n = 8` or `n = -2` (**false uniqueness** from an absolute value). II alone ->
   any positive integer. Together -> `n = 8` only. *(Verified: `|8-3| = |−2−3| = 5`.)*
4. **(c).** I alone: 9 is divisible by 3 but not by 6 - insufficient. II alone: 8 is even but not
   divisible by 6 - insufficient. Together: divisible by 2 **and** 3 forces divisibility by 6, since
   2 and 3 are coprime. *(Verified over 1-200.)* Each statement is **necessary**; only the pair is
   **sufficient** - the cleanest illustration of that distinction in the whole file.
5. **`xy` in `(-8, 12)`.** The interval for `x` **straddles zero**, so test all four corners:
   `(-2)(1) = -2`, `(-2)(4) = -8`, `(3)(1) = 3`, `(3)(4) = 12`. Minimum `-8`, maximum `12`.
   *(Verified.)* ⚠️ The naive `a·c < xy < b·d` rule would have given `(-2, 12)` and lost the true
   minimum - it is valid only when both intervals are positive.
6. **`3^150`.** Equalise the exponent: `5^100 = (5^2)^50 = 25^50` and `3^150 = (3^3)^50 = 27^50`, and
   `27 > 25`. *(Verified by exact integer comparison.)*
7. **72.** The nearest integers to `17/2` are 8 and 9, so `8 x 9 = 72`. The real equal-parts bound
   is `72.25`, but it is unavailable to integers. *(Verified.)*
8. **`[-5, 10)`.** The corner products are `-2, -5, 4, 10`; `-5` is attained at `x=-1,y=5`, whereas
   10 would require excluded `x=2`. *(Verified.)*

## 9. Timed transfer and retry gate

Attempt the eight drills in **12 minutes**, recording each miss as C, A, X, R, or T. A DS answer is
not complete until its printed option wording is checked. Retry the failed form after a 20-minute
gap. Advance only at **7/8 or better**, with no false-uniqueness, denominator, or endpoint error;
otherwise redo the corresponding method and take a fresh set.

## 10. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Read **Topic 05 and Topic 06 together**: the two-statement **data-sufficiency** format is a major,
  recurring block, and its content often overlaps with reasoning/coding (see the trend-table caveat in
  [Master Framework](../00_Master-Framework.md)).
- ⚠️ **The DS block is not printed the same way each year.** 2024 and 2025 attach the directions and
  the four options to **every item**; 2026 opens with a **single directions block covering five
  items**. The number of DS-format items in the audited Set-A papers is small but they arrive
  together, so a wrong reading of the option set costs several marks at once.
- ⚠️ **The fourth option changed meaning inside the 2025 paper itself** - some items offer "cannot be
  answered", others offer "can be answered even **without** using any of the Statements". Treat the
  option set as **data to be read**, not a template to be recalled.
- ⚠️ Recurring shapes: **data sufficiency** (unique-answer decisions), **quantitative comparison** of
  powers/surds, **inequality/parity** reasoning, and short **equation word problems**.
- ⚠️ The paper repeatedly punishes **false uniqueness** and **over-solving** - the two habits this file
  drills hardest.

## 11. Study links

- ✅ [Foundation companion](../basic/05_Algebra-Inequalities-and-Data-Sufficiency.md).
- ✅ [Logical Reasoning, Coding, Counting and DI](./06_Logical-Reasoning-Coding-Counting-and-DI.md) - DS content often overlaps reasoning.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - parity/factor facts settle many DS items.

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
| 2018 | CSAT | 2 | Series equation solving | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 23 | Range inequality deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 24 | Expression magnitude comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 34 | Digit-constraint algebra | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 37 | Inequality chain deduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 38 | Algebraic revenue expression | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2023 | CSAT | 59 | Two-statement digit-number sufficiency | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 60 | Two-statement age-sequence sufficiency | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |

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
