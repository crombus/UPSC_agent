---
title: "Algebra-Inequalities-and-Data-Sufficiency — CSAT Learner-v2 Semantic Successor"
topic_key: csat-05
---

# Algebra-Inequalities-and-Data-Sufficiency — Complete CSAT Learning Session

**Identity:** `csat-05:learner-v2:g1`  
**Generation date:** 2026-09-06  
**Approval:** false  
**Official syllabus anchor:** Logical reasoning, analytical ability, decision making and Class X data sufficiency.

| Source | SHA-256 at generation |
|---|---|
| `upsc-ai-kit\knowledge\CSAT\basic\05_Algebra-Inequalities-and-Data-Sufficiency.md` | `9ce4e37a3ee79503180acc8881d913abb73caecd4ba2a6d6937349f975a86f3d` |
| `upsc-ai-kit\knowledge\CSAT\advanced\05_Algebra-Inequalities-and-Data-Sufficiency.md` | `68f22171fab10d649d8d81d357aca87bb870af467a52f29e8de02c3cfbc10882` |
| `upsc-ai-kit\knowledge\CSAT\00_Master-Framework.md` | `aaa2016904629d268db79a5798150ef8b9a1386fd1edb2ec737062f2cc9e3fcf` |
| `upsc-ai-kit\knowledge\CSAT\OFFICIAL-UPSC-SYLLABUS-MAPPING.md` | `80dd81eb9ccd7e977570eb86cac69418178dc665d981094c6438a95ca4b8b8a8` |
| `upsc-ai-kit\knowledge\CSAT\00_Question-Audit-Ledger.md` | `fbecba6a750ae88aba541dd1ef1379e6e73841ac7a4285b99bec8fd59bea7e6f` |

The canonical Basic owner is taught first. Optional Advanced material is isolated after practice.
All official-PYQ references preserve the repository's supplied/provisional key labels; no unavailable
wording, official explanation or official key is invented.

## BASIC LEARNING SESSION

### Twelve-panel ASCII master flow

```text
+----------------------------------------------------------------------------------+
| PANEL 01 — EXPRESSION DISCIPLINE                                                 |
| Track signs, brackets, domains and denominators.                                 |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 02 — LINEAR EQUATIONS                                                      |
| Preserve equality through reversible operations.                                 |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 03 — SIMULTANEOUS EQUATIONS                                                |
| Use elimination, substitution or option testing.                                 |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 04 — INEQUALITIES                                                          |
| Reverse the sign only when multiplying or dividing by a negative.                |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 05 — ABSOLUTE VALUE AND SURDS                                              |
| Split valid cases and respect non-negative roots.                                |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 06 — WORD TRANSLATION                                                      |
| Define variables and constraints before manipulating.                            |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 07 — QUANTITATIVE COMPARISON                                               |
| Compare ranges, not one sample.                                                  |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 08 — DS FORMAT                                                             |
| Read the printed verdict options before solving.                                 |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 09 — NECESSARY AND SUFFICIENT                                              |
| Test each statement alone, then together.                                        |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 10 — COUNTEREXAMPLE SEARCH                                                 |
| One second valid value disproves uniqueness.                                     |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 11 — BOUNDS AND OPTIMISATION                                               |
| Check endpoints, integrality and attainability.                                  |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 12 — VERIFICATION                                                          |
| Substitute, test domains and separate answer value from sufficiency.             |
+----------------------------------------------------------------------------------+
```

### Canonical Basic owner

### Algebra, Inequalities and Data Sufficiency - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Analytical ability / decision-making.
> **Core skill:** translate words to equations, handle inequalities and quantitative comparison, and
> master the UPSC two-statement **data-sufficiency** decision.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md).*

---

### 1. Visual foundation

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

### 2. The UPSC data-sufficiency format (read it, do not recall it)

✅ A CSAT data-sufficiency item gives a **Question** followed by two **Statements I and II**. The
first three options are stable across the audited papers; **the fourth is not**.

| Option | Meaning (stable across 2024, 2025 and 2026 Set A) |
|---|---|
| **(a)** | Answerable using **one** statement alone, but **not** the other alone. |
| **(b)** | Answerable using **either** statement alone. |
| **(c)** | Answerable using **both** statements **together**, but not either alone. |
| **(d)** | ⚠️ **Varies - read it.** See the table below. |

#### ⚠️ The fourth option is not a fixed template

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

#### Necessary vs sufficient (the distinction the format is built on)

| Term | Test | In a DS item |
|---|---|---|
| ✅ **Sufficient** | Having it **settles** the question. | A statement is "sufficient" only if it forces **exactly one** answer. |
| ✅ **Necessary** | The conclusion **cannot hold without** it. | A statement can be necessary yet insufficient - it narrows without pinning. |

- ⚠️ In `A -> B`: A is **sufficient** for B; B is **necessary** for A. They are not interchangeable,
  and a statement that is merely necessary is **not** enough to mark (a) or (b).

### 3. Essential algebra and inequality facts

| Tool | Rule | Edge condition |
|---|---|---|
| ✅ **Linear solve** | A linear equation in one unknown fixes it after isolation. | The variable coefficient must be non-zero; retain any stated integer/positive domain. |
| ✅ **Two unknowns** | Two independent **linear** equations can pin two unknowns; a multiple of one is not independent. | Non-linear systems can still have 0, 1, or many solutions; inconsistent pairs give no solution and dependent pairs give many. |
| ✅ **Inequality flip** | Multiplying/dividing by a **negative** reverses the sign. | Adding/subtracting **never** flips it. |
| ✅ **Dividing by a variable** | Only legal if you know it is non-zero. | If its **sign** is unknown, the inequality direction is unknown too - split into cases; division by zero is never legal. |
| ✅ **Cross-multiplication** | For `a/b < c/d`, multiply only after fixing `b` and `d` as non-zero and their signs. | With `bd > 0`, compare `ad` and `bc`; with `bd < 0`, reverse the inequality. |
| ✅ **Absolute value** | `|u| = k` means `u = k` **or** `u = -k` when `k >= 0`; for `k>0`, `|u|<k` means `-k<u<k` and `|u|>k` means `u<-k` or `u>k`. | If `k < 0`, no real solution; handle `k=0` separately. |
| ✅ **Squaring to compare** | `a > b >= 0  =>  a^2 > b^2`. | Fails if either side may be negative. |
| ✅ **Quantitative comparison** | Reduce both quantities to the **same base/form** before comparing. | `x^m` vs `x^n` reverses for `0 < x < 1`. |
| ✅ **Sum-difference** | Two numbers with sum `S`, difference `D`: they are `(S+D)/2` and `(S-D)/2`. | Integer answers need `S` and `D` of the same parity. |

### 4. Method

1. **Solve items:** translate each sentence to one equation; write the domain first (integer, digit,
   positive, non-zero); then count unknowns vs independent **linear** equations.
2. **Inequality/QC items:** rewrite both sides in a comparable form (same base, same power); watch the
   sign rule and any denominator.
3. **DS items - in this order:**
   1. **Read the four printed options**, especially (d).
   2. Ask whether the **question alone** already pins the answer (a live verdict in this paper).
   3. Test **I alone**, then **II alone**, then **both** - stopping at **uniqueness**, not the value.

### 5. Original solved examples

#### 📝 Example A (solve)

**Solve `3x + 5 = 20`.** `3x = 15` -> `x =` **5.** *(Verified.)*

#### 📝 Example B (sum-difference)

**Two numbers have sum 30 and difference 8.** They are `(30+8)/2 = 19` and `(30-8)/2 = 11`. **19 and
11.** *(Verified.)*

#### 📝 Example C (quantitative comparison)

**Which is larger, `2^30` or `3^20`?** `2^30 = 8^10`, `3^20 = 9^10` -> `9^10 > 8^10` -> **`3^20` is
larger.** *(Verified: 1073741824 < 3486784401.)*

#### 📝 Example C.1 (word translation, denominator and absolute value)

**A number increased by 5 is three times the number decreased by 1. Find it.** Translate the words
before calculating: `x + 5 = 3(x - 1)`, so `x + 5 = 3x - 3`, `2x = 8`, and **`x = 4`**.

**Solve `|2x - 1| = 5`.** Keep both branches: `2x - 1 = 5` gives `x = 3`; `2x - 1 = -5` gives
`x = -2`. **Both values work.** *(Verified.)*

**Compare `1/x` and `1/y` when `x > y > 0`.** Because `xy > 0`, cross-multiplication gives
`y < x`, hence **`1/x < 1/y`**. This conclusion is unsafe without the positive-domain condition.

#### 📝 Example D (data sufficiency, answer (c))

**Question:** What is the two-digit number N?
Statement I: N is divisible by 11.
Statement II: The tens digit of N is 3.

I alone -> 11, 22, ..., 99 (not unique). II alone -> 30-39 (not unique). Both -> divisible by 11 **and**
tens digit 3 -> **33** (unique). **Answer: (c).**

#### 📝 Example E (data sufficiency, answer (b))

**Question:** Is the integer n even?
Statement I: n^2 is even.
Statement II: n + 1 is odd.

I alone -> n^2 even forces n even (sufficient). II alone -> n+1 odd forces n even (sufficient). Each
works alone. **Answer: (b).**

#### 📝 Example F (the self-sufficient question - the 2025 fourth-option variant)

**Question:** What is the smallest **two-digit** number having exactly **three** distinct factors?
Statement I: the number is odd.
Statement II: the number is divisible by 5.

**Why the factor shortcut is safe here:** if `n = p₁^a p₂^b ...`, its number of positive factors is
`(a+1)(b+1)...`. Exactly three factors therefore forces one exponent 2 and no other prime: `n = p²`.
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

### 6. Must-Know facts

- ✅ Two independent linear equations are needed to pin two unknowns; `2x + 4y = 20` adds **nothing** to
  `x + 2y = 10`.
- ✅ In DS, a statement is "sufficient" only if it yields a **single** answer; a statement that merely
  narrows the field is **necessary at best**, never sufficient.
- ✅ **Sufficiency is about the answer, not about the arithmetic.** Never finish the calculation.
- ✅ Reversing an inequality happens on multiply/divide by a negative - **not** on adding a negative.
  Adding the same quantity to both sides never flips the sign.
- ✅ Squaring both sides preserves order **only when both sides are non-negative**.
- ✅ For QC, common tricks: equalise exponents, take roots, or compare ratios.
- ✅ Before cross-multiplying an inequality, state whether the denominator product is positive or
  negative; zero denominators are excluded.
- ✅ A number that is both a perfect square and cube has every prime exponent divisible by both 2 and
  3, hence by 6; this supports the self-sufficiency drill without a hidden prerequisite.

### 7. Common traps

- ❌ Computing the value in a DS item when you only need "is it unique?". -> Stop at uniqueness.
- ❌ **Marking (d) from memory.** -> The printed (d) differs between the audited years and even
  between items of the same 2025 paper; read it.
- ❌ Missing that the **question alone** may already be answerable. -> Check that first.
- ❌ Treating a scaled copy of an equation as new information. -> It is dependent.
- ❌ Confusing **necessary** with **sufficient** ("n is even" is necessary for "n is a multiple of 6",
  but nowhere near sufficient). -> Ask which direction the arrow points.
- ❌ Forgetting to flip the inequality on a negative multiplier. -> Flip the sign.
- ❌ Cross-multiplying before checking a denominator sign. -> State `bd > 0` or split cases.
- ❌ Keeping only one branch of an absolute-value equation. -> Write `u = k` and `u = -k`.
- ❌ In DS, checking "both together" **before** testing each alone. -> Test each alone first (it may be
  (a) or (b)).
- ❌ Assuming "cannot be found" without trying **both together**. -> That verdict requires both to fail.

### 8. Quick checks

- ✅ Can you state options (a), (b) and (c) - and did you just **read** (d) off the paper?
- ✅ Do you test I alone and II alone **before** combining?
- ✅ Can you say which of two conditions is necessary and which is sufficient?
- ✅ Can you compare `a^m` and `b^n` by equalising exponents?

### 9. Mini-drill (with answers and explanations)

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

### 10. Timed transfer, diagnosis and retry gate

**Set 90 seconds per item; do not look at a DS letter until the logical verdict is fixed.**

1. Solve `3(x - 2) = 2x + 7` for integer `x`.
2. Solve `|x + 4| = 2`.
3. Given `a > b > 0`, compare `a/b` and `b/a`.
4. **DS.** Is positive integer `n` divisible by 6? I: `n` is even. II: `n` is divisible by 3.
5. A two-digit number is `10t + u`. Its digits sum to 11 and its tens digit exceeds its units digit
   by 3. Find the number.

**Answers.** 1. **13**. 2. **-2 or -6**. 3. **`a/b > b/a`** because multiplying by `ab > 0` reduces
it to `a² > b²`. 4. **Both needed**. 5. `t+u=11`, `t-u=3`, so `t=7,u=4`: **74**.

| If you missed because... | Code | Repair before retry |
|---|---|---|
| You assumed two equations always give one answer | C | State “independent linear equations + domain”. |
| You lost a sign/denominator restriction | A | Write `x ≠ 0` and denominator signs first. |
| You kept one absolute-value branch | C | Draw the two branches before solving. |
| You mapped a DS verdict to a memorised letter | R | Re-read the printed option block. |
| You over-solved a DS item | T | Stop once uniqueness or a counterexample is proved. |

**Retry gate:** redo the five items after 20 minutes. Continue only at **5/5 within eight minutes**;
otherwise rebuild the failed relation and take five fresh items of that exact form.

### 11. Study links

- ✅ [Optional Advanced companion](../advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md) -
  dependent-statement DS, unique-root logic, and interval/optimisation depth. Core above remains
  sufficient for the paper's basic algebra and DS forms.
- ✅ [Reading Comprehension](./01_Reading-Comprehension.md) - "is it supported?" mirrors "is it sufficient?".
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - number properties power many DS items.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
### 2026 PYQ Integration

> **Status:** 2026 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2026.md`.
> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are **provisional**; no option or answer is recorded or inferred in this integration.

- **Year represented:** 2026
- **Paper(s):** CSAT
- **Routed question demands:** 9

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2026 | CSAT | 1 | Data sufficiency: coin denomination | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 2 | Data sufficiency: compare reals | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 3 | Data sufficiency: parity | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 4 | Data sufficiency: set-membership logic | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 5 | Data sufficiency: prime determination | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 8 | Weight equations comparison | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 21 | Inequality-range statements | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 38 | Linear marking-scheme equations | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 80 | Rate-constraint optimisation | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |

#### What this owner must now support

- Data sufficiency: coin denomination
- Data sufficiency: compare reals
- Data sufficiency: parity
- Data sufficiency: set-membership logic
- Data sufficiency: prime determination
- Weight equations comparison
- Inequality-range statements
- Linear marking-scheme equations
- Rate-constraint optimisation

> This block integrates the 2026 examinable demand and paper metadata. It is kept separate from the 2018-2023 and 2024-2025 blocks and does not convert a provisionally-keyed, answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2026 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
### Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2024-2025.md`.
> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded or inferred in this integration.

- **Years represented:** 2024, 2025
- **Paper(s):** CSAT
- **Routed question demands:** 24

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | CSAT | 35 | Reversed-digit equation | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 50 | Linear-cost validation | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 59 | Data sufficiency: integers | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 60 | Data sufficiency: transfer rate | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 64 | Data sufficiency: integer pair | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 65 | Data sufficiency: shares | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 66 | Data sufficiency: class size | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 67 | Data sufficiency: prime triple | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 68 | Data sufficiency: integrality | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 69 | Data sufficiency: article prices | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 70 | Data sufficiency: score comparison | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 73 | Data sufficiency: reversed ages | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 76 | Coded inequalities | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 19 | Chained-inequality validation | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 26 | Bounded-expression ratio | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 68 | Data sufficiency: factor count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 69 | Data sufficiency: digit product | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 70 | Data sufficiency: family relation | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 73 | Data sufficiency: match outcome | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 74 | Data sufficiency: positivity | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 75 | Quantitative comparison: ratio | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 76 | Quantitative comparison: product | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 77 | Quantitative comparison: set | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 79 | Unit-interval inequalities | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |

#### What this owner must now support

- Reversed-digit equation
- Linear-cost validation
- Data sufficiency: integers
- Data sufficiency: transfer rate
- Data sufficiency: integer pair
- Data sufficiency: shares
- Data sufficiency: class size
- Data sufficiency: prime triple
- Data sufficiency: integrality
- Data sufficiency: article prices
- Data sufficiency: score comparison
- Data sufficiency: reversed ages
- Coded inequalities
- Chained-inequality validation
- Bounded-expression ratio
- Data sufficiency: factor count
- Data sufficiency: digit product
- Data sufficiency: family relation
- Data sufficiency: match outcome
- Data sufficiency: positivity
- Quantitative comparison: ratio
- Quantitative comparison: product
- Quantitative comparison: set
- Unit-interval inequalities

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
### Historical PYQ Integration (2018-2023)

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

#### What this owner must now support

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

---

### Semantic-completeness closure — 2026-09-06

#### Literal syllabus and canonical ownership

- **Literal clause:** Logical reasoning, analytical ability, decision making and Class X data sufficiency.
- **Canonical scope:** Owns algebraic expressions, equations, inequalities, quantitative comparison and the two-statement data-sufficiency decision format.
- **Cross-topic boundary:** Arithmetic computation remains with Topic 03 and rate contexts with Topic 04 when no sufficiency judgement is tested; arrangements and coding belong to Topic 06.

#### Complete learner route

1. **Expression discipline:** Track signs, brackets, domains and denominators.
2. **Linear equations:** Preserve equality through reversible operations.
3. **Simultaneous equations:** Use elimination, substitution or option testing.
4. **Inequalities:** Reverse the sign only when multiplying or dividing by a negative.
5. **Absolute value and surds:** Split valid cases and respect non-negative roots.
6. **Word translation:** Define variables and constraints before manipulating.
7. **Quantitative comparison:** Compare ranges, not one sample.
8. **DS format:** Read the printed verdict options before solving.
9. **Necessary and sufficient:** Test each statement alone, then together.
10. **Counterexample search:** One second valid value disproves uniqueness.
11. **Bounds and optimisation:** Check endpoints, integrality and attainability.
12. **Verification:** Substitute, test domains and separate answer value from sufficiency.

#### Verification and hostile-query gate

Equations are plug-checked, inequality sign changes are explicit, and sufficiency verdicts require uniqueness across all allowed values rather than one convenient example.

The hostile absence search explicitly tested these families and close-option terms:
**equation; inequality; absolute value; quantitative comparison; data sufficiency; necessary; sufficient; counterexample**. A shortcut is usable only when its stated condition survives; otherwise return to
the first-principles representation. Every worked answer must finish with an independent check:
passage support, substitution, enumeration, units, bounds, reverse operation or option elimination.

#### Difficulty and timed progression

1. Foundation: recognise the family and state the governing definition or relation.
2. Core: solve a direct item with a visible representation and one verification.
3. Advanced: combine two mechanisms, test edge cases and reject close distractors.
4. Timed: use classify → extract → represent → execute → verify → decide.
5. Remediation: log the error as concept, application, calculation, reading, passage, time or guess;
   return to the owning subtopic before retesting.

## BASIC MCQS / REMEDIATION

### Diagnostic and core set

### Q1. Practice variant 1: Solve 3x + 2 = 11.

A. 3
B. 4
C. 2
D. 5

**Correct answer: A.** Subtract the constant, divide by 3, then substitute back.


### Q2. Practice variant 1: Two numbers have sum 20 and difference 4. What is the larger number?

A. 13
B. 12
C. 11
D. 14

**Correct answer: B.** Adding the equations gives twice the larger number.


### Q3. Practice variant 1: If -2x > 8, which statement is correct?

A. x > -4
B. x < 4
C. x < -4
D. x > 4

**Correct answer: C.** Dividing an inequality by a negative reverses its sign.


### Q4. Practice variant 1: How many real solutions does |x| = 4 have?

A. 0
B. 1
C. 4
D. 2

**Correct answer: D.** For a positive a, |x|=a gives x=a and x=-a.


### Q5. Practice variant 1: Compare Quantity I: 3^2 and Quantity II: 8.

A. Quantity I is greater
B. Quantity II is greater
C. They are equal
D. Cannot be determined

**Correct answer: A.** Their difference is exactly 1.


### Q6. Practice variant 1: What is x? Statement 1: x + 2 = 12. Statement 2: x is positive.

A. Statement 2 alone is sufficient
B. Statement 1 alone is sufficient
C. Both together are required
D. Even both are insufficient

**Correct answer: B.** Statement 1 fixes x uniquely; positivity alone does not.


### Q7. Practice variant 1: What is x? Statement 1: x^2 = 9. Statement 2: x > 0.

A. Statement 1 alone is sufficient
B. Statement 2 alone is sufficient
C. Both statements together are sufficient
D. Even both are insufficient

**Correct answer: C.** Statement 1 leaves plus/minus values; Statement 2 selects the positive one.


### Q8. Practice variant 1: For 0 <= y <= 5, what is the maximum of y(10-y)?

A. 26
B. 24
C. 27
D. 25

**Correct answer: D.** Complete the square: y(2n-y)=n^2-(y-n)^2, maximised at y=n.


### Q9. Practice variant 2: Solve 3x + 3 = 15.

A. 4
B. 5
C. 3
D. 6

**Correct answer: A.** Subtract the constant, divide by 3, then substitute back.


### Q10. Practice variant 2: Two numbers have sum 22 and difference 4. What is the larger number?

A. 14
B. 13
C. 12
D. 15

**Correct answer: B.** Adding the equations gives twice the larger number.


### Q11. Practice variant 2: If -2x > 8, which statement is correct?

A. x > -4
B. x < 4
C. x < -4
D. x > 4

**Correct answer: C.** Dividing an inequality by a negative reverses its sign.


### Q12. Practice variant 2: How many real solutions does |x| = 5 have?

A. 0
B. 1
C. 4
D. 2

**Correct answer: D.** For a positive a, |x|=a gives x=a and x=-a.


### Q13. Practice variant 2: Compare Quantity I: 4^2 and Quantity II: 15.

A. Quantity I is greater
B. Quantity II is greater
C. They are equal
D. Cannot be determined

**Correct answer: A.** Their difference is exactly 1.


### Q14. Practice variant 2: What is x? Statement 1: x + 2 = 13. Statement 2: x is positive.

A. Statement 2 alone is sufficient
B. Statement 1 alone is sufficient
C. Both together are required
D. Even both are insufficient

**Correct answer: B.** Statement 1 fixes x uniquely; positivity alone does not.


### Q15. Practice variant 2: What is x? Statement 1: x^2 = 16. Statement 2: x > 0.

A. Statement 1 alone is sufficient
B. Statement 2 alone is sufficient
C. Both statements together are sufficient
D. Even both are insufficient

**Correct answer: C.** Statement 1 leaves plus/minus values; Statement 2 selects the positive one.


### Q16. Practice variant 2: For 0 <= y <= 6, what is the maximum of y(12-y)?

A. 37
B. 35
C. 38
D. 36

**Correct answer: D.** Complete the square: y(2n-y)=n^2-(y-n)^2, maximised at y=n.


### Remediation protocol

1. Recompute without options.
2. Name the failed rule or passage phrase.
3. Reject every distractor for a specific reason.
4. Retry with altered numbers, wording or constraints.
5. Advance only after two consecutive correct answers under the time ceiling.

## PYQS AND ANSWER PRACTICE

### Verified 2024-2026 Set-A demand and key ledger

| Year | Q | Neutral verified demand | Key status | Solution architecture |
|---:|---:|---|---|---|
| 2024 | 35 | Reversed-digit equation | D (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2024 | 50 | Linear-cost validation | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 59 | Data sufficiency: integers | C (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 60 | Data sufficiency: transfer rate | C (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 64 | Data sufficiency: integer pair | C (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 65 | Data sufficiency: shares | C (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 66 | Data sufficiency: class size | D (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 67 | Data sufficiency: prime triple | A (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 68 | Data sufficiency: integrality | D (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 69 | Data sufficiency: article prices | C (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 70 | Data sufficiency: score comparison | D (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 73 | Data sufficiency: reversed ages | A (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2024 | 76 | Coded inequalities | D (supplied) | Translate signs and test the full allowed range. |
| 2025 | 19 | Chained-inequality validation | D (supplied) | Translate signs and test the full allowed range. |
| 2025 | 26 | Bounded-expression ratio | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 68 | Data sufficiency: factor count | D (supplied) | Prime-factorise, count exponents and verify divisibility. |
| 2025 | 69 | Data sufficiency: digit product | D (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2025 | 70 | Data sufficiency: family relation | D (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2025 | 73 | Data sufficiency: match outcome | D (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2025 | 74 | Data sufficiency: positivity | B (supplied) | Test each statement alone, then together, seeking uniqueness. |
| 2025 | 75 | Quantitative comparison: ratio | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 76 | Quantitative comparison: product | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 77 | Quantitative comparison: set | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 79 | Unit-interval inequalities | A (supplied) | Translate signs and test the full allowed range. |
| 2026 | 1 | Data sufficiency: coin denomination | A (provisional) | Test each statement alone, then together, seeking uniqueness. |
| 2026 | 2 | Data sufficiency: compare reals | D (provisional) | Test each statement alone, then together, seeking uniqueness. |
| 2026 | 3 | Data sufficiency: parity | C (provisional) | Test each statement alone, then together, seeking uniqueness. |
| 2026 | 4 | Data sufficiency: set-membership logic | D (provisional) | Test each statement alone, then together, seeking uniqueness. |
| 2026 | 5 | Data sufficiency: prime determination | A (provisional) | Test each statement alone, then together, seeking uniqueness. |
| 2026 | 8 | Weight equations comparison | B (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 21 | Inequality-range statements | B (provisional) | Translate signs and test the full allowed range. |
| 2026 | 38 | Linear marking-scheme equations | B (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 80 | Rate-constraint optimisation | D (provisional) | Use the total crossing length. |

> The table is a non-verbatim routing audit. It records the locally checked Set-A key letter and a
> valid solving route, but does not pretend that UPSC publishes model solutions. The separate
> workbook supplies original solved equivalents for every mechanism.

### Timed mixed transfer

### Q33. Practice variant 5: Solve 3x + 6 = 27.

A. 7
B. 8
C. 6
D. 9

**Correct answer: A.** Subtract the constant, divide by 3, then substitute back.


### Q34. Practice variant 5: Two numbers have sum 28 and difference 4. What is the larger number?

A. 17
B. 16
C. 15
D. 18

**Correct answer: B.** Adding the equations gives twice the larger number.


### Q35. Practice variant 5: If -2x > 8, which statement is correct?

A. x > -4
B. x < 4
C. x < -4
D. x > 4

**Correct answer: C.** Dividing an inequality by a negative reverses its sign.


### Q36. Practice variant 5: How many real solutions does |x| = 8 have?

A. 0
B. 1
C. 4
D. 2

**Correct answer: D.** For a positive a, |x|=a gives x=a and x=-a.


### Q37. Practice variant 5: Compare Quantity I: 7^2 and Quantity II: 48.

A. Quantity I is greater
B. Quantity II is greater
C. They are equal
D. Cannot be determined

**Correct answer: A.** Their difference is exactly 1.


### Q38. Practice variant 5: What is x? Statement 1: x + 2 = 16. Statement 2: x is positive.

A. Statement 2 alone is sufficient
B. Statement 1 alone is sufficient
C. Both together are required
D. Even both are insufficient

**Correct answer: B.** Statement 1 fixes x uniquely; positivity alone does not.


### Q39. Practice variant 5: What is x? Statement 1: x^2 = 49. Statement 2: x > 0.

A. Statement 1 alone is sufficient
B. Statement 2 alone is sufficient
C. Both statements together are sufficient
D. Even both are insufficient

**Correct answer: C.** Statement 1 leaves plus/minus values; Statement 2 selects the positive one.


### Q40. Practice variant 5: For 0 <= y <= 9, what is the maximum of y(18-y)?

A. 82
B. 80
C. 83
D. 81

**Correct answer: D.** Complete the square: y(2n-y)=n^2-(y-n)^2, maximised at y=n.


## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Algebra, Inequalities and Data Sufficiency - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Analytical ability / decision-making.
> **Core skill:** unique-root traps, dependent-statement data sufficiency, quantitative comparison of
> surds/powers, and inequality ranges under constraints.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/05_Algebra-Inequalities-and-Data-Sufficiency.md).*

---

### 1. Architecture

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

### 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Unique-root test** | Over the reals, `x^2 = k` gives two roots for `k > 0`, one for `k = 0`, and none for `k < 0`; `x^3 = k` gives one. | A squared/absolute constraint alone is often **in**sufficient; a cubic or odd-power one usually is not. |
| ✅ **Dependent statements** | If II is a multiple/rearrangement of I - or is **logically implied** by I - it adds nothing. | Two unknowns need two **independent** relations. Nesting can be hidden behind different-looking wording. |
| ✅ **Necessary vs sufficient** | In `A -> B`, A is sufficient for B, B is necessary for A. | Two individually **necessary** statements can be jointly **sufficient** - that is exactly the (c) verdict. |
| ✅ **Surd comparison** | Compare `sqrt a + sqrt b` vs `sqrt c` by squaring (both sides positive). | Squaring preserves order only for non-negative quantities. |
| ✅ **AM-GM / bounded optimum** | For non-negative real parts with fixed sum, the product is maximised at equal parts. | AM-GM itself needs non-negative terms; for integer parts choose the nearest permitted integers, and respect any positive/distinct bounds. |
| ✅ **Interval arithmetic** | For `a < x < b`, `c < y < d`: `a+c < x+y < b+d`. | For a product on a rectangular interval, compare all four endpoint products; retain open/closed endpoints. Division additionally requires the divisor interval to exclude zero. |

### 3. Harder methods (worked)

#### 📝 Method 1 - false uniqueness in DS

**Question:** What is the integer n? **I:** `n^2 = 49`. **II:** `n^3 = 343`.
I alone -> `n = 7` or `n = -7` (**not** unique). II alone -> `n = 7` only (unique). So one statement (II)
alone answers it but the other does not. **Answer: (a).** *(Verified: `(-7)^2 = 49` but `(-7)^3 =
-343`.)*

#### 📝 Method 2 - dependent statements

**Question:** What is `x + y`? **I:** `x + 2y = 10`. **II:** `2x + 4y = 20`.
II is exactly `2 x` I, so it adds no information. Two unknowns, one independent equation -> `x + y` is
not determined. **Answer: (d).** *(Verified: e.g. (10,0) and (8,1) both satisfy, giving x+y = 10 and 9.)*

#### 📝 Method 3 - surd comparison

**Which is larger, `sqrt50 + sqrt72` or `sqrt200`?** `sqrt50 + sqrt72 ≈ 7.07 + 8.49 = 15.56`;
`sqrt200 ≈ 14.14`. So **`sqrt50 + sqrt72` is larger.** *(Verified.)* (Note `sqrt50 + sqrt72 = 5 sqrt2 +
6 sqrt2 = 11 sqrt2 ≈ 15.56`, while `sqrt200 = 10 sqrt2`.)

#### 📝 Method 4 - verdict first, letter second (the escalation this paper punishes)

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

#### 📝 Method 5 - optimum and interval endpoints

**Integer optimum.** Positive integers `x,y` have `x+y=11`. Their product is largest at the nearest
integers to `11/2`: `x,y = 5,6`, so the maximum is **30**, not `11²/4 = 30.25` (which is the real,
not integer, bound). AM-GM applies because the parts are positive.

**Endpoint-aware interval.** If `-2 < x <= 3` and `1 <= y < 4`, the four limiting corner products
are `-2, -8, 3, 12`. Thus `-8 < xy < 12`: neither extreme is reached because the responsible
endpoint (`x=-2` for the minimum and `y=4` for the maximum) is excluded. Do not silently convert
open bounds into closed ones.

### 4. Time-saving techniques (safe conditions)

- ⚠️ **Stop at uniqueness** in DS; never fully solve. *Safe always - it is the whole skill.*
- ⚠️ **Spot dependence** by checking whether one statement is a scalar multiple of the other. *Safe
  always.*
- ⚠️ **Factor out common surds** (`11 sqrt2` vs `10 sqrt2`) to compare instantly. *Safe when a common
  radical exists.*
- ⚠️ **Equal-parts optimum** for a fixed-sum product. *Use AM-GM only for non-negative parts; for
  integers use the nearest permitted integers to the mean, then check any bounds/distinctness rule.*

### 5. Boundary cases

- ⚠️ A statement with a **square or absolute value** frequently permits **two** values - treat it as
  insufficient until proven unique.
- ⚠️ Two equations can be **inconsistent** (no solution) as well as dependent (many solutions) - both
  block a unique answer.
- ⚠️ Interval products need all four corner products even when neither interval straddles zero; then
  preserve whether each extremal endpoint is open or closed. Interval division is unsafe if the
  divisor interval contains zero.

### 6. Advanced traps

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

### 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| False uniqueness | A | For squares/absolute values, ask "could it be negative too?". |
| Missed dependence | C | Check both `II = k x I` **and** `I => II`. |
| Necessary treated as sufficient | C | Write the arrow, then read it in the right direction. |
| Over-solving DS | T | Stop the instant uniqueness is clear. |
| Interval-product sign errors | X | Tabulate the four corner products. |
| Surd comparison slips | X | Factor the common radical before deciding. |
| Right verdict, wrong letter | R | Re-read the printed option set before marking. |

### 8. Advanced drill (with full solutions)

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

### 9. Timed transfer and retry gate

Attempt the eight drills in **12 minutes**, recording each miss as C, A, X, R, or T. A DS answer is
not complete until its printed option wording is checked. Retry the failed form after a 20-minute
gap. Advance only at **7/8 or better**, with no false-uniqueness, denominator, or endpoint error;
otherwise redo the corresponding method and take a fresh set.

### 10. PYQ-pattern notes (2024-2026, Set A)

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

### 11. Study links

- ✅ [Foundation companion](../basic/05_Algebra-Inequalities-and-Data-Sufficiency.md).
- ✅ [Logical Reasoning, Coding, Counting and DI](./06_Logical-Reasoning-Coding-Counting-and-DI.md) - DS content often overlaps reasoning.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - parity/factor facts settle many DS items.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
### Historical PYQ Integration (2018-2023)

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

#### What this owner must now support

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

## CONSOLIDATED REGISTER NOTES

### Complete revision spine

- **Expression discipline:** Track signs, brackets, domains and denominators.
- **Linear equations:** Preserve equality through reversible operations.
- **Simultaneous equations:** Use elimination, substitution or option testing.
- **Inequalities:** Reverse the sign only when multiplying or dividing by a negative.
- **Absolute value and surds:** Split valid cases and respect non-negative roots.
- **Word translation:** Define variables and constraints before manipulating.
- **Quantitative comparison:** Compare ranges, not one sample.
- **DS format:** Read the printed verdict options before solving.
- **Necessary and sufficient:** Test each statement alone, then together.
- **Counterexample search:** One second valid value disproves uniqueness.
- **Bounds and optimisation:** Check endpoints, integrality and attainability.
- **Verification:** Substitute, test domains and separate answer value from sufficiency.

### Ownership and close-option firewall

- **Own here:** Owns algebraic expressions, equations, inequalities, quantitative comparison and the two-statement data-sufficiency decision format.
- **Do not duplicate:** Arithmetic computation remains with Topic 03 and rate contexts with Topic 04 when no sufficiency judgement is tested; arrangements and coding belong to Topic 06.
- **Verification:** Equations are plug-checked, inequality sign changes are explicit, and sufficiency verdicts require uniqueness across all allowed values rather than one convenient example.

### Timed answer route

`CLASSIFY → EXTRACT → REPRESENT → EXECUTE → VERIFY → DECIDE`

- Use estimation or option elimination only after preserving the governing condition.
- A blank costs zero; a rushed unsupported answer also consumes time and may attract negative marks.
- For every error, record concept/application/calculation/reading/passage/time/guess, repair the
  owner, and retry a new item rather than memorising the old option.

