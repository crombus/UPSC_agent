# Algebra, Inequalities and Data Sufficiency - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Analytical ability / decision-making.
> **Core skill:** translate words to equations, handle inequalities and quantitative comparison, and
> master the UPSC two-statement **data-sufficiency** decision.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md`.*

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

## 2. The UPSC data-sufficiency format (learn it exactly)

✅ A CSAT data-sufficiency item gives a **Question** followed by two **Statements I and II**, and asks
you to choose:

| Option | Meaning |
|---|---|
| **(a)** | Answerable using **one** statement alone, but **not** the other alone. |
| **(b)** | Answerable using **either** statement alone. |
| **(c)** | Answerable using **both** statements **together**, but not either alone. |
| **(d)** | **Cannot** be answered even using both statements together. |

> 🔑 **DS discipline:** test **Statement I alone**, then **Statement II alone**, and only then **both
> together**. Do the value-finding **only** far enough to see whether the answer is **unique**.

## 3. Essential algebra and inequality facts

| Tool | Rule |
|---|---|
| ✅ **Linear solve** | Isolate the variable; one equation fixes one unknown. |
| ✅ **Two unknowns** | Need **two independent** equations; a multiple of one is not independent. |
| ✅ **Inequality flip** | Multiplying/dividing by a **negative** reverses the inequality sign. |
| ✅ **Quantitative comparison** | Reduce both quantities to the **same base/form** before comparing. |
| ✅ **Sum-difference** | Two numbers with sum `S`, difference `D`: they are `(S+D)/2` and `(S-D)/2`. |

## 4. Method

1. **Solve items:** translate each sentence to one equation; count unknowns vs independent equations.
2. **Inequality/QC items:** rewrite both sides in a comparable form (same base, same power); watch the
   sign rule.
3. **DS items:** apply the four-option test - I alone, II alone, both - stopping at **uniqueness**, not
   the value.

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

## 6. Must-Know facts

- ✅ Two independent linear equations are needed to pin two unknowns; `2x + 4y = 20` adds **nothing** to
  `x + 2y = 10`.
- ✅ In DS, a statement is "sufficient" only if it yields a **single** answer.
- ✅ Reversing an inequality happens on multiply/divide by a negative - **not** on adding a negative.
- ✅ For QC, common tricks: equalise exponents, take roots, or compare ratios.

## 7. Common traps

- ❌ Computing the value in a DS item when you only need "is it unique?". -> Stop at uniqueness.
- ❌ Treating a scaled copy of an equation as new information. -> It is dependent.
- ❌ Forgetting to flip the inequality on a negative multiplier. -> Flip the sign.
- ❌ In DS, checking "both together" **before** testing each alone. -> Test each alone first (it may be
  (a) or (b)).
- ❌ Assuming "cannot be found" without trying **both together**. -> (d) requires both to fail.

## 8. Quick checks

- ✅ Can you recite the four DS options and their exact meanings?
- ✅ Do you test I alone and II alone **before** combining?
- ✅ Can you compare `a^m` and `b^n` by equalising exponents?

## 9. Mini-drill (with answers and explanations)

1. Solve the inequality `2x - 3 > 7`.
2. Compare `(0.5)^3` and `(0.5)^2`.
3. **DS.** Question: What is the two-digit number? I: The sum of its digits is 9. II: The difference of
   its digits is 9.
4. **DS.** Question: What is x? I: `3x = 12`. II: `x + 7 = 11`.
5. Two numbers have sum 30 and difference 8. Find them.

**Answers.**

1. **x > 5.** Add 3, divide by 2. *(Verified.)*
2. **`(0.5)^3 < (0.5)^2`** (0.125 < 0.25): for a base between 0 and 1, a higher power is smaller.
   *(Verified.)*
3. **(a).** I alone: 18, 27, 36, ..., 90 (many). II alone: digits differing by 9 -> only **90** (since
   9 and 0), unique. So one statement (II) alone answers it but not the other. *(Verified: only 90.)*
4. **(b).** I alone -> x = 4; II alone -> x = 4. Either works. *(Verified.)*
5. **19 and 11.** `(30±8)/2`. *(Verified.)*

## 10. Study links

- ✅ Advanced companion: `advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md` - dependent-
  statement DS, unique-root logic, and inequality ranges.
- ✅ `01_Reading-Comprehension.md` (basic) - "is it supported?" mirrors "is it sufficient?".
- ✅ `02_Number-Systems-and-Number-Sense.md` (basic) - number properties power many DS items.
