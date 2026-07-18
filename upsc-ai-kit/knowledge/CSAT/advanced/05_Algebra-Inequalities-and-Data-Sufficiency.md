# Algebra, Inequalities and Data Sufficiency - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Analytical ability / decision-making.
> **Core skill:** unique-root traps, dependent-statement data sufficiency, quantitative comparison of
> surds/powers, and inequality ranges under constraints.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`.*

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
| ✅ **Unique-root test** | `x^2 = k` gives **two** roots; `x^3 = k` gives **one**. | A squared/absolute constraint alone is often **in**sufficient. |
| ✅ **Dependent statements** | If II is a multiple/rearrangement of I, together they still give one equation. | Two unknowns need two **independent** relations. |
| ✅ **Surd comparison** | Compare `sqrt a + sqrt b` vs `sqrt c` by squaring (both sides positive). | Squaring preserves order only for non-negative quantities. |
| ✅ **AM-GM / bounded optimum** | For fixed sum, the product is maximised when the parts are equal. | State the domain (integers vs reals) - it changes the optimum. |
| ✅ **Interval arithmetic** | For `a < x < b`, `c < y < d`: `a+c < x+y < b+d`. | For products, check signs of the endpoints. |

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

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Stop at uniqueness** in DS; never fully solve. *Safe always - it is the whole skill.*
- ⚠️ **Spot dependence** by checking whether one statement is a scalar multiple of the other. *Safe
  always.*
- ⚠️ **Factor out common surds** (`11 sqrt2` vs `10 sqrt2`) to compare instantly. *Safe when a common
  radical exists.*
- ⚠️ **Equal-parts optimum** for fixed-sum products. *Safe for reals; for integers, use the nearest
  integers to the mean.*

## 5. Boundary cases

- ⚠️ A statement with a **square or absolute value** frequently permits **two** values - treat it as
  insufficient until proven unique.
- ⚠️ Two equations can be **inconsistent** (no solution) as well as dependent (many solutions) - both
  block a unique answer.
- ⚠️ Interval products can flip sign if endpoints straddle zero - check the extreme corners.

## 6. Advanced traps

- ❌ Calling `n^2 = 49` sufficient. -> It allows `n = ±7`.
- ❌ Adding a scaled duplicate equation as new information. -> It is dependent.
- ❌ Comparing surds by rough decimals when they are close. -> Square or factor the common radical.
- ❌ Reflexively computing a value in DS. -> Decide sufficiency and move on.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| False uniqueness | A | For squares/abs, ask "could it be negative too?". |
| Missed dependence | C | Check statement-II = k x statement-I. |
| Over-solving DS | T | Stop the instant uniqueness is clear. |
| Surd comparison slips | X | Factor the common radical before deciding. |

## 8. Advanced drill (with full solutions)

1. **DS.** Question: What is the integer n? I: `n^2 = 49`. II: `n^3 = 343`.
2. **DS.** Question: What is `x + y`? I: `x + 2y = 10`. II: `2x + 4y = 20`.
3. If `x + y = 10` with x, y positive integers, what is the maximum of `xy`?
4. Given `1 < x < 3` and `2 < y < 5`, state the range of `x + y` and of `xy`.
5. Which is larger, `sqrt50 + sqrt72` or `sqrt200`?

**Solutions.**

1. **(a).** II gives a unique `n = 7`; I gives `±7`. *(Verified.)*
2. **(d).** II duplicates I; `x + y` is not fixed. *(Verified.)*
3. **25.** Maximum at `x = y = 5` -> `xy = 25`. *(Verified.)*
4. **`x + y` in `(3, 8)`; `xy` in `(2, 15)`.** Endpoints from `1x2` up to `3x5`. *(Verified.)*
5. **`sqrt50 + sqrt72`** (`11 sqrt2 ≈ 15.56` vs `10 sqrt2 ≈ 14.14`). *(Verified.)*

## 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Read **Topic 05 and Topic 06 together**: the two-statement **data-sufficiency** format is a major,
  recurring block, and its content often overlaps with reasoning/coding (see the trend-table caveat in
  `00_Master-Framework.md`).
- ⚠️ Recurring shapes: **data sufficiency** (unique-answer decisions), **quantitative comparison** of
  powers/surds, **inequality/parity** reasoning, and short **equation word problems**.
- ⚠️ The paper repeatedly punishes **false uniqueness** and **over-solving** - the two habits this file
  drills hardest.

## 10. Study links

- ✅ Foundation companion: `basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`.
- ✅ `advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md` - DS content often overlaps reasoning.
- ✅ `advanced/02_Number-Systems-and-Number-Sense.md` - parity/factor facts settle many DS items.
