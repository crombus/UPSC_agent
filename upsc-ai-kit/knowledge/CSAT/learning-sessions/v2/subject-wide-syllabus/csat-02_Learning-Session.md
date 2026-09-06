---
title: "Number-Systems-and-Number-Sense — CSAT Learner-v2 Semantic Successor"
topic_key: csat-02
---

# Number-Systems-and-Number-Sense — Complete CSAT Learning Session

**Identity:** `csat-02:learner-v2:g1`  
**Generation date:** 2026-09-06  
**Approval:** false  
**Official syllabus anchor:** Basic numeracy: numbers and their relations, orders of magnitude, etc. (Class X level).

| Source | SHA-256 at generation |
|---|---|
| `upsc-ai-kit\knowledge\CSAT\basic\02_Number-Systems-and-Number-Sense.md` | `64de1f8f4fe9b969548c14d41372fb5efa793daf3dc844837fc666778de243f3` |
| `upsc-ai-kit\knowledge\CSAT\advanced\02_Number-Systems-and-Number-Sense.md` | `342b0aa16f9297edcccf9d706c859c05d6fe44e261801bc27a2844e278028d3e` |
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
| PANEL 01 — NUMBER UNIVERSE                                                       |
| Natural, whole, integer, rational, irrational and real numbers.                  |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 02 — DIVISIBILITY                                                          |
| Use prime-factor and digit tests only within their valid base-ten                |
| conditions.                                                                      |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 03 — PRIMES AND FACTORS                                                    |
| Factorise before counting divisors or comparing powers.                          |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 04 — HCF AND LCM                                                           |
| Use gcd-lcm relations with integer and positivity checks.                        |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 05 — REMAINDERS                                                            |
| Reduce early and preserve the modulus.                                           |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 06 — UNIT DIGITS                                                           |
| Use cyclicity and treat exponent-zero cases separately.                          |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 07 — DIGITS AND PLACE VALUE                                                |
| Translate reversal and digit count into base-ten equations.                      |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 08 — POWERS AND FACTORIALS                                                 |
| Use repeated division for prime exponents and trailing zeros.                    |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 09 — FRACTIONS AND DECIMALS                                                |
| Convert recurring forms through algebra, not memorised guesses.                  |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 10 — SERIES                                                                |
| Test differences, ratios, alternation and position rules.                        |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 11 — MAGNITUDE AND ESTIMATION                                              |
| Bound before calculating exactly.                                                |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 12 — VERIFICATION                                                          |
| Plug back, check parity, digit count, remainder and order of magnitude.          |
+----------------------------------------------------------------------------------+
```

### Canonical Basic owner

### Number Systems and Number Sense - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy / general mental ability.
> **Core skill:** solve by a **number property** (divisibility, unit digit, remainder, factor count)
> instead of heavy calculation.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). All drills below are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example (not a UPSC item).
> *Companion: [Advanced Drill](../advanced/02_Number-Systems-and-Number-Sense.md).*

---

### 1. Visual foundation

```text
A NUMBER PROBLEM
      |
   ask: do I need the VALUE, or just a PROPERTY?
      |
   +----------------+------------------+
   |                |                  |
 DIVISIBILITY     UNIT DIGIT        REMAINDER / FACTORS
 rules 2..11      cyclicity 4       mod arithmetic / prime powers
      |                |                  |
   answer WITHOUT full multiplication whenever possible
```

**Core proposition:** most CSAT number items are decided by a **last digit, a remainder, or a
factor count** - computing the whole number is usually the slow, error-prone path.

### 2. Essential rules

| Tool | Rule (exam-ready) | Edge condition |
|---|---|---|
| ✅ **Div by 2 / 5 / 10** | Look at the last digit (even; 0 or 5; 0). | - |
| ✅ **Div by 4 / 8** | Last **2** digits div by 4; last **3** digits div by 8. | - |
| ✅ **Div by 3 / 9** | Digit sum div by 3 / by 9. | Works in base 10 only. |
| ✅ **Div by 11** | (Sum of odd-place digits) - (sum of even-place digits) is 0 or a multiple of 11. | The difference may be **negative**; judge its absolute value. |
| ✅ **Unit-digit cycles** | 2,3,7,8 repeat with period **4**; 4,9 with period **2**; 0,1,5,6 are constant. | Applies to exponents `n >= 1`; `a^0 = 1` for any `a != 0`. |
| ✅ **Trailing zeros of n!** | `floor(n/5) + floor(n/25) + floor(n/125) + ...` (count 5s). | Keep adding terms until one is 0. |
| ✅ **Number of factors** | For `n = p^a q^b r^c`, factor count `= (a+1)(b+1)(c+1)`. | `p, q, r` must be **distinct primes**; the count includes 1 and `n`. |
| ✅ **HCF x LCM** | For two numbers, `HCF x LCM = product of the numbers`. | **Two** numbers only, and both positive. |

> 🔑 **Unit-digit shortcut:** for a power `a^n`, take `n mod 4` (use 4 when it divides), then read the
> unit digit from a's cycle. Example: `7^100` -> `100 mod 4 = 0` -> last in cycle (7,9,3,1) -> **1**.

### 3. Method (property-first)

1. Decide whether the question wants the **exact value** or only a **property** (last digit, remainder,
   count, divisor).
2. Pick the matching tool from Section 2.
3. Reduce with **modular thinking**: replace big numbers by their remainders before combining.
4. Only compute the full value if nothing else works - and then **estimate first** to catch slips.

### 4. Formulas and conditions

- ✅ `Dividend = Divisor x Quotient + Remainder`, with `0 <= Remainder < Divisor`.
- ✅ **Same-remainder divisor:** the greatest number dividing several numbers leaving the **same
  remainder** = **HCF of their pairwise differences**.
- ✅ **Exact-division divisor:** greatest number dividing several numbers exactly = **HCF**; smallest
  number divisible by several = **LCM**.
- ⚠️ *Condition:* `HCF x LCM = product` holds for **two** numbers only, not three or more.
- ⚠️ *Condition:* a "remainder" is only well defined against a **stated divisor**, and it is always
  **less than** that divisor - an answer of "remainder 7 on division by 5" is arithmetically impossible.
- ⚠️ *Condition:* "`a` divides `b`" and "`b` divides `a`" are different claims; only one holds unless
  `a = b`. Divisibility is an **implication**, not an equivalence.

### 5. Core number sense methods

#### 5.1 Recurring decimals

| Form | Convert | Condition |
|---|---|---|
| `0.\overline{a}` | `a/9` | `a` is one recurring digit. |
| `0.\overline{ab}` | `ab/99` | `ab` is the two-digit repeating block. |
| `0.uv\overline{w}` | `(uvw - uv) / [10^2(10^1-1)]` | Subtract the non-repeating prefix; denominator has prefix zeros, then recurring-block 9s. |

**Worked example.** `x = 0.1\overline{6}`. Then `100x = 16.\overline6` and `10x =
1.\overline6`; subtract: `90x = 15`, so `x = 1/6`. Do not use the `a/9` shortcut when a
non-repeating prefix exists.

#### 5.2 Place value, digit counts and reversal

- An `n`-digit positive integer lies from `10^(n-1)` to `10^n - 1`.
- Digits used from 1 to `N` are counted in blocks: 1–9 uses `9 x 1`; 10–99 uses `90 x 2`; then
  count the final partial block. For a range `L` to `U`, use `digits(1..U) - digits(1..L-1)`.
- A two-digit number with digits `a,b` is `10a+b`; its reversal is `10b+a`. Their difference is
  `9(a-b)` and their sum is `11(a+b)`. Here `a != 0`, and a reversed “two-digit number” also
  requires `b != 0`.

**Worked example.** Pages 1–250 use `9 + 90x2 + 151x3 =` **642 digits**. A number `10a+b`
minus its reversal is divisible by 9; this is a property, not proof that every multiple of 9 is a
digit reversal.

#### 5.3 Unknown digits and exponents

- For an unknown digit, apply the relevant divisibility test before trial: e.g. `47x2` divisible by
  9 requires `4+7+x+2 = 13+x` divisible by 9, hence **`x=5`**.
- For non-zero `a`, `a^m a^n=a^(m+n)`, `a^m/a^n=a^(m-n)`, and `(a^m)^n=a^(mn)`. A negative
  exponent means reciprocal: `a^(-n)=1/a^n`. Fractional exponents need a real-domain check:
  `a^(1/2)` is real only for `a >= 0`.
- For positive bases, powers increase with exponent when `a>1` and decrease when `0<a<1`.
  Never raise an inequality to an even power or multiply it by an unknown-sign quantity without
  checking the direction and lost sign information.

**Worked example.** Compare `(1/2)^5` and `(1/2)^3`: because the base lies between 0 and 1,
the larger exponent gives the smaller value, so `(1/2)^5 < (1/2)^3`.

#### 5.4 Counting multiples in a range

The count of multiples of positive `d` in the inclusive range `[L,U]` is
`floor(U/d) - floor((L-1)/d)`. For “divisible by `a` or `b`”, add the two counts and subtract
multiples of `lcm(a,b)`; “exactly one” subtracts the overlap twice.

**Worked example.** From 100 to 500, multiples of 6 number `83-16=67`, multiples of 10 number
`50-9=41`, and multiples of 30 number `16-3=13`. Thus divisible by 6 **or** 10:
`67+41-13 =` **95**.

> **Routing boundary:** Topic 02 owns number properties, digit structure and arithmetic counting.
> Cryptarithmetic, code-language puzzles and general sequence inference are owned by Topic 06/08.
> Their appearances in appended PYQ ledgers are cross-owner demand references, not claims that this
> file independently teaches those separate mechanisms.

### 6. Original solved examples

#### 📝 Example A (unit digit)

**Find the unit digit of `3^35`.** Cycle of 3 is (3, 9, 7, 1), period 4. `35 mod 4 = 3` -> third term
-> **7**. *(Verified.)*

#### 📝 Example B (remainder)

**Remainder when `2^50` is divided by 7.** `2^3 = 8 ≡ 1 (mod 7)`, period 3. `50 mod 3 = 2` -> `2^2 = 4`.
**Remainder = 4.** *(Verified.)*

#### 📝 Example C (HCF-LCM)

**Two numbers have HCF 12 and LCM 180; one is 36. Find the other.** Other `= (HCF x LCM)/known =
(12 x 180)/36 =` **60.** *(Verified.)*

#### 📝 Example D (trailing zeros)

**How many zeros end `25!`?** `floor(25/5) + floor(25/25) = 5 + 1 =` **6.** *(Verified.)*

#### 📝 Example E (factor count)

**Number of factors of 360.** `360 = 2^3 x 3^2 x 5^1` -> `(3+1)(2+1)(1+1) =` **24.** *(Verified.)*

### 7. Must-Know facts

- ✅ A number is div by 6 iff div by **2 and 3**; by 12 iff div by **3 and 4**. (Both work because the
  pairs are **coprime** - "div by 2 and 6" would **not** give div by 12.)
- ✅ Product of two numbers = HCF x LCM (two numbers only).
- ✅ Even x anything = even; odd x odd = odd; even + odd = odd (parity is a fast eliminator).
- ✅ Unit digit of any power `a^n` with `n >= 1` depends only on the **base's unit digit** and
  `n mod 4` (taking a remainder of 0 as the 4th, last, cycle term).
- ✅ Trailing zeros of a factorial are governed by the count of **5s**, not 2s (2s are always more).
- ✅ A number has an **odd** number of factors exactly when it is a **perfect square**.

### 8. Common traps

- ❌ Counting 2s for trailing zeros of `n!`. -> Count **5s**; 2s are surplus.
- ❌ Using `HCF x LCM = product` for **three** numbers. -> Two numbers only.
- ❌ Taking `n mod 4 = 0` as "cycle position 0". -> Use the **4th (last)** term of the cycle.
- ❌ Forgetting the div-by-11 **alternating** sign. -> It is odd-place minus even-place.
- ❌ Splitting a divisor into non-coprime factors ("div by 2 and 6 => div by 12"). -> The factors
  must be **coprime**.
- ❌ Confusing "same remainder" with "exact division". -> Same remainder uses HCF of **differences**.

### 9. Quick checks

- ✅ Can you get a unit digit of any `a^n` in under 10 seconds via `n mod 4`?
- ✅ Can you state trailing zeros of `n!` without multiplying?
- ✅ Given `n = p^a q^b`, can you write the factor count immediately?

### 10. Mini-drill (with answers and explanations)

1. Unit digit of `7^100`.
2. Greatest number that divides 43, 91 and 183 leaving the **same** remainder.
3. Remainder when `15^23` is divided by 4.
4. Number of zeros at the end of `100!`.
5. Next term: 2, 6, 12, 20, 30, ...

**Answers.**

1. **1.** Cycle (7,9,3,1); `100 mod 4 = 0` -> last term -> 1. *(Verified.)*
2. **4.** Differences 48, 92, 140; `HCF(48, 92, 140) = 4`. *(Verified.)*
3. **3.** `15 ≡ 3 ≡ -1 (mod 4)`; `(-1)^23 = -1 ≡ 3`. *(Verified.)*
4. **24.** `floor(100/5) + floor(100/25) = 20 + 4 = 24`. *(Verified.)*
5. **42.** Differences 4, 6, 8, 10 -> next 12 -> `30 + 12 = 42` (these are `n(n+1)`). *(Verified.)*

### 11. Timed Core drill, diagnosis and retry gate

**Set rule:** attempt the eight items in **10 minutes** without a calculator. Before calculating,
write the chosen method beside each answer: `D` divisibility, `R` remainder/cycle, `F` factors,
`G` digits, `E` exponent, or `I` inclusion-exclusion.

1. Convert `0.2\overline7` to a fraction in lowest terms.  
2. How many digits are used to number pages 1 to 120?  
3. Find the missing digit in `53x4` if it is divisible by 9.  
4. How many multiples of 8 lie from 51 to 250 inclusive?  
5. What is the unit digit of `7^53`?  
6. How many numbers from 1 to 100 are divisible by exactly one of 4 and 6?  
7. Which is larger: `(1/3)^4` or `(1/3)^5`?  
8. How many positive factors does `2^4 x 3^2` have?

**Answers.** 1. `5/18` (`100x-10x=25`); 2. `9+180+63 = 252`; 3. `x=6`;
4. `floor(250/8)-floor(50/8)=31-6 = 25`; 5. **7**; 6. `25+16-2x8 = 25`;
7. `(1/3)^4`; 8. `(4+1)(2+1)=15`.

| Miss pattern | Diagnosis | Mandatory repair before a new timed set |
|---|---|---|
| Formula remembered but wrong base/block | **C** condition error | Rebuild one example from definitions, then solve three variants. |
| Correct method, arithmetic slip | **X** execution | Estimate/order-check and rework the final two lines. |
| Used a long calculation where a property worked | **T** tool selection | Label the property first on five easy items. |
| Wrong “or/exactly one” count | **A** interpretation | Draw the overlap and write the lcm before counting. |

| Date / set | Score / time | D | R | F | G | E | I | X / T | Next repair |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |  |  |  |

**Gate:** proceed to optional Advanced work only after **7/8 in 10 minutes** on this set and
**7/8 on a fresh set** after correcting misses. Otherwise repeat the failed method family; an
Advanced remainder trick is not a substitute for Core number fluency. Apply the Master Framework’s
attempt and qualifying-margin rules in full-paper practice.

### 12. Study links

- ✅ [Advanced companion](../advanced/02_Number-Systems-and-Number-Sense.md) - big-power remainders,
  highest prime powers, and inclusion-exclusion counting.
- ✅ [Arithmetic and Commercial Math](./03_Arithmetic-and-Commercial-Math.md) - ratio and percentage build on factor sense.
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - number properties power many DS items.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
### 2026 PYQ Integration

> **Status:** 2026 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2026.md`.
> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are **provisional**; no option or answer is recorded or inferred in this integration.

- **Year represented:** 2026
- **Paper(s):** CSAT
- **Routed question demands:** 12

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2026 | CSAT | 10 | LCM multiple count in range | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 18 | String-pattern position | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 19 | Exponent equation factorisation | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 22 | Measurement-combination optimisation | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 29 | Discrete-set expression extrema | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 42 | Unit digit of power product | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 45 | Count of powers of two | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 49 | Digit count in two-digit integers | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 57 | Fibonacci-like recurrence | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 59 | HCF-LCM cube relation | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 60 | Divisibility-by-eleven digit puzzle | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 66 | Reversed-digit divisibility count | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |

#### What this owner must now support

- LCM multiple count in range
- String-pattern position
- Exponent equation factorisation
- Measurement-combination optimisation
- Discrete-set expression extrema
- Unit digit of power product
- Count of powers of two
- Digit count in two-digit integers
- Fibonacci-like recurrence
- HCF-LCM cube relation
- Divisibility-by-eleven digit puzzle
- Reversed-digit divisibility count

> This block integrates the 2026 examinable demand and paper metadata. It is kept separate from the 2018-2023 and 2024-2025 blocks and does not convert a provisionally-keyed, answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2026 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
### Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2024-2025.md`.
> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded or inferred in this integration.

- **Years represented:** 2024, 2025
- **Paper(s):** CSAT
- **Routed question demands:** 32

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | CSAT | 6 | Operator-placement minimum | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 9 | Trailing-zero count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 10 | Cumulative savings sequence | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 15 | Divisibility test | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 17 | Terminal nonzero digit | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 18 | Common-divisor remainder | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 19 | HCF container sizing | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 20 | Prime-sum unit digit | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 39 | Expression parity | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 46 | Periodic-sequence sum | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 54 | Exponential divisibility | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 55 | Integer-pair uniqueness | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 79 | Number series | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 5 | Factor-sum enumeration | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 6 | Prime-progression sums | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 7 | Unit-fraction solution count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 16 | Derived-operator pattern | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 18 | Simultaneous remainder constraints | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 20 | Odd-product unit digit | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 25 | Divisibility-exclusion count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 27 | Prime-expression count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 28 | LCM-HCF triple count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 35 | Highest factor power | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 36 | Number-series completion | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 40 | Square-root digit count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 46 | Power-sum remainder | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 47 | Repdigit HCF | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 48 | Concatenated-sequence digit | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 60 | Number-series completion | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 64 | Factor-count invariance | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 67 | Power-series remainder | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 80 | Interior-multiples count | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |

#### What this owner must now support

- Operator-placement minimum
- Trailing-zero count
- Cumulative savings sequence
- Divisibility test
- Terminal nonzero digit
- Common-divisor remainder
- HCF container sizing
- Prime-sum unit digit
- Expression parity
- Periodic-sequence sum
- Exponential divisibility
- Integer-pair uniqueness
- Number series
- Factor-sum enumeration
- Prime-progression sums
- Unit-fraction solution count
- Derived-operator pattern
- Simultaneous remainder constraints
- Odd-product unit digit
- Divisibility-exclusion count
- Prime-expression count
- LCM-HCF triple count
- Highest factor power
- Number-series completion
- Square-root digit count
- Power-sum remainder
- Repdigit HCF
- Concatenated-sequence digit
- Factor-count invariance
- Power-series remainder
- Interior-multiples count

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
### Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 65

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 3 | Number matrix pattern | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 36 | Digit-ordered number count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 9 | Digit frequency count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 15 | Divisibility set overlap | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 33 | Reversed-digit ratio pairs | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 48 | Number series pattern | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 51 | Number series pattern | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 53 | Page-digit range count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 60 | Multi-digit divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 75 | Digit sum divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 7 | Trailing-zero count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 8 | Cyclic-sum divisibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 10 | Digit-sum primality | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 11 | Digit symbol equation | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 12 | HCF length measurement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 13 | Prime-offset sequence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 14 | Page-sum torn leaf | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 37 | Digit and divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 50 | Largest value among fractional and negative-exponent powers | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 51 | HCF of measurements | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 53 | Recurring decimal conversion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 54 | LCM remainder constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 56 | Product remainder calculation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 58 | Digit sum of power | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 75 | Difference-of-squares factoring | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 76 | Fraction shift comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 77 | Divisibility condition digit | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 5 | Cyclic remainder pattern | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 6 | Divisibility digit value | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 26 | Sequence incorrect term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 36 | Digit-permutation sum divisibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 50 | Number sequence missing term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 59 | Cryptarithmetic digit addition | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 60 | Cryptarithmetic digit multiplication | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 67 | Consecutive-integer property | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 76 | Digit-interchange difference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 79 | Repunit smallest multiplier | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 4 | Number sequence term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 5 | Divisibility digit arrangement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 9 | Number magnitude comparison | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 47 | LCM parity minimum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 54 | Digit sum bound statements | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 58 | Product modular remainder | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 65 | LCM remainder threshold | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 66 | Digit reversal product | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 67 | Prime composite property | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 74 | Exponent maximum value | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 75 | Number sequence term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 7 | Product remainder modulo | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 8 | Unit digit expansion | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 9 | Digit-sum addition puzzle | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 10 | Digit-sum ratio minimum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 14 | Integer parity determination | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 15 | Prime-composite property check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 16 | Digit multiplication constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 17 | Repeated-block divisibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 25 | Conditional divisor count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 27 | Repunit remainder modulo | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 28 | Repunit square digit sum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 29 | Range digit-sum total | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 45 | Divisor-remainder bound count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 46 | Repeated-digit sum constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 47 | Permuted-digit number sum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 74 | Large power remainder | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 76 | Cryptarithmetic digit solve | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |

#### What this owner must now support

- Number matrix pattern
- Digit-ordered number count
- Digit frequency count
- Divisibility set overlap
- Reversed-digit ratio pairs
- Number series pattern
- Page-digit range count
- Multi-digit divisibility count
- Digit sum divisibility count
- Trailing-zero count
- Cyclic-sum divisibility
- Digit-sum primality
- Digit symbol equation
- HCF length measurement
- Prime-offset sequence
- Page-sum torn leaf
- Digit and divisibility count
- Largest value among fractional and negative-exponent powers
- HCF of measurements
- Recurring decimal conversion
- LCM remainder constraint
- Product remainder calculation
- Digit sum of power
- Difference-of-squares factoring
- Fraction shift comparison
- Divisibility condition digit
- Cyclic remainder pattern
- Divisibility digit value
- Sequence incorrect term
- Digit-permutation sum divisibility
- Number sequence missing term
- Cryptarithmetic digit addition
- Cryptarithmetic digit multiplication
- Consecutive-integer property
- Digit-interchange difference
- Repunit smallest multiplier
- Number sequence term
- Divisibility digit arrangement
- Number magnitude comparison
- LCM parity minimum
- Digit sum bound statements
- Product modular remainder
- LCM remainder threshold
- Digit reversal product
- Prime composite property
- Exponent maximum value
- Product remainder modulo
- Unit digit expansion
- Digit-sum addition puzzle
- Digit-sum ratio minimum
- Integer parity determination
- Prime-composite property check
- Digit multiplication constraint
- Repeated-block divisibility
- Conditional divisor count
- Repunit remainder modulo
- Repunit square digit sum
- Range digit-sum total
- Divisor-remainder bound count
- Repeated-digit sum constraint
- Permuted-digit number sum
- Large power remainder
- Cryptarithmetic digit solve

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->

---

### Semantic-completeness closure — 2026-09-06

#### Literal syllabus and canonical ownership

- **Literal clause:** Basic numeracy: numbers and their relations, orders of magnitude, etc. (Class X level).
- **Canonical scope:** Owns integer classes, divisibility, primes, factors, HCF/LCM, remainders, digits, powers, roots, factorial valuations, recurring decimals, magnitude and number series.
- **Cross-topic boundary:** Commercial percentages belong to Topic 03; rate contexts to Topic 04; algebraic unknowns and sufficiency to Topic 05; coding/counting structures to Topic 06.

#### Complete learner route

1. **Number universe:** Natural, whole, integer, rational, irrational and real numbers.
2. **Divisibility:** Use prime-factor and digit tests only within their valid base-ten conditions.
3. **Primes and factors:** Factorise before counting divisors or comparing powers.
4. **HCF and LCM:** Use gcd-lcm relations with integer and positivity checks.
5. **Remainders:** Reduce early and preserve the modulus.
6. **Unit digits:** Use cyclicity and treat exponent-zero cases separately.
7. **Digits and place value:** Translate reversal and digit count into base-ten equations.
8. **Powers and factorials:** Use repeated division for prime exponents and trailing zeros.
9. **Fractions and decimals:** Convert recurring forms through algebra, not memorised guesses.
10. **Series:** Test differences, ratios, alternation and position rules.
11. **Magnitude and estimation:** Bound before calculating exactly.
12. **Verification:** Plug back, check parity, digit count, remainder and order of magnitude.

#### Verification and hostile-query gate

Each shortcut is stated with its modulus, parity, cycle or factorisation condition. Deterministic checks recompute every generated answer by direct arithmetic or enumeration.

The hostile absence search explicitly tested these families and close-option terms:
**divisibility; prime; factor; HCF; LCM; remainder; unit digit; trailing zeros**. A shortcut is usable only when its stated condition survives; otherwise return to
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

### Q1. Practice variant 1: What is the unit digit of 2^11?

A. 8
B. 9
C. 7
D. 10

**Correct answer: A.** Reduce powers modulo 10 and use the complete unit-digit cycle.


### Q2. Practice variant 1: What is the remainder when 137 is divided by 7?

A. 5
B. 4
C. 3
D. 6

**Correct answer: B.** Division algorithm: n = mq + r with 0 <= r < m.


### Q3. Practice variant 1: What is the HCF of 12 and 18?

A. 7
B. 5
C. 6
D. 8

**Correct answer: C.** Prime factorisation or Euclid's algorithm gives the greatest common divisor.


### Q4. Practice variant 1: How many positive divisors does 60 have?

A. 13
B. 11
C. 14
D. 12

**Correct answer: D.** If n = product p_i^a_i, the divisor count is product (a_i + 1).


### Q5. Practice variant 1: How many trailing zeros are in 25! ?

A. 6
B. 7
C. 5
D. 8

**Correct answer: A.** Count factors of 5 by repeated division; factors of 2 are more abundant.


### Q6. Practice variant 1: How many multiples of 7 lie from 10 through 100, inclusive?

A. 14
B. 13
C. 12
D. 15

**Correct answer: B.** Use floor(high/d) - floor((low-1)/d).


### Q7. Practice variant 1: The sequence starts 3, 5, 7, ... . What is its 8th term?

A. 18
B. 16
C. 17
D. 19

**Correct answer: C.** This is an arithmetic progression: a_n = a + (n-1)d.


### Q8. Practice variant 1: How many decimal digits are in 137?

A. 4
B. 2
C. 5
D. 3

**Correct answer: D.** A positive integer n has floor(log10 n)+1 digits; direct place-value bounding gives the same answer.


### Q9. Practice variant 2: What is the unit digit of 3^12?

A. 1
B. 2
C. 0
D. 3

**Correct answer: A.** Reduce powers modulo 10 and use the complete unit-digit cycle.


### Q10. Practice variant 2: What is the remainder when 154 is divided by 8?

A. 3
B. 2
C. 1
D. 4

**Correct answer: B.** Division algorithm: n = mq + r with 0 <= r < m.


### Q11. Practice variant 2: What is the HCF of 14 and 21?

A. 8
B. 6
C. 7
D. 9

**Correct answer: C.** Prime factorisation or Euclid's algorithm gives the greatest common divisor.


### Q12. Practice variant 2: How many positive divisors does 72 have?

A. 13
B. 11
C. 14
D. 12

**Correct answer: D.** If n = product p_i^a_i, the divisor count is product (a_i + 1).


### Q13. Practice variant 2: How many trailing zeros are in 30! ?

A. 7
B. 8
C. 6
D. 9

**Correct answer: A.** Count factors of 5 by repeated division; factors of 2 are more abundant.


### Q14. Practice variant 2: How many multiples of 8 lie from 11 through 105, inclusive?

A. 13
B. 12
C. 11
D. 14

**Correct answer: B.** Use floor(high/d) - floor((low-1)/d).


### Q15. Practice variant 2: The sequence starts 4, 7, 10, ... . What is its 8th term?

A. 26
B. 24
C. 25
D. 27

**Correct answer: C.** This is an arithmetic progression: a_n = a + (n-1)d.


### Q16. Practice variant 2: How many decimal digits are in 1037?

A. 5
B. 3
C. 6
D. 4

**Correct answer: D.** A positive integer n has floor(log10 n)+1 digits; direct place-value bounding gives the same answer.


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
| 2024 | 6 | Operator-placement minimum | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 9 | Trailing-zero count | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 10 | Cumulative savings sequence | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 15 | Divisibility test | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 17 | Terminal nonzero digit | D (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2024 | 18 | Common-divisor remainder | C (supplied) | Translate to congruences and plug the result into every condition. |
| 2024 | 19 | HCF container sizing | B (supplied) | Use prime factors or Euclid; verify the common-divisor condition. |
| 2024 | 20 | Prime-sum unit digit | C (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2024 | 39 | Expression parity | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 46 | Periodic-sequence sum | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 54 | Exponential divisibility | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 55 | Integer-pair uniqueness | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 79 | Number series | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 5 | Factor-sum enumeration | C (supplied) | Prime-factorise, count exponents and verify divisibility. |
| 2025 | 6 | Prime-progression sums | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 7 | Unit-fraction solution count | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 16 | Derived-operator pattern | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 18 | Simultaneous remainder constraints | C (supplied) | Translate to congruences and plug the result into every condition. |
| 2025 | 20 | Odd-product unit digit | C (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2025 | 25 | Divisibility-exclusion count | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 27 | Prime-expression count | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 28 | LCM-HCF triple count | D (supplied) | Use prime factors or Euclid; verify the common-divisor condition. |
| 2025 | 35 | Highest factor power | B (supplied) | Prime-factorise, count exponents and verify divisibility. |
| 2025 | 36 | Number-series completion | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 40 | Square-root digit count | B (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2025 | 46 | Power-sum remainder | C (supplied) | Translate to congruences and plug the result into every condition. |
| 2025 | 47 | Repdigit HCF | C (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2025 | 48 | Concatenated-sequence digit | D (supplied) | Use place value, cyclicity or a constrained enumeration. |
| 2025 | 60 | Number-series completion | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 64 | Factor-count invariance | C (supplied) | Prime-factorise, count exponents and verify divisibility. |
| 2025 | 67 | Power-series remainder | A (supplied) | Translate to congruences and plug the result into every condition. |
| 2025 | 80 | Interior-multiples count | C (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 10 | LCM multiple count in range | D (provisional) | Use prime powers and range bounds. |
| 2026 | 18 | String-pattern position | D (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 19 | Exponent equation factorisation | B (provisional) | Prime-factorise, count exponents and verify divisibility. |
| 2026 | 22 | Measurement-combination optimisation | B (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 29 | Discrete-set expression extrema | C (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 42 | Unit digit of power product | C (provisional) | Use place value, cyclicity or a constrained enumeration. |
| 2026 | 45 | Count of powers of two | C (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 49 | Digit count in two-digit integers | B (provisional) | Use place value, cyclicity or a constrained enumeration. |
| 2026 | 57 | Fibonacci-like recurrence | D (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 59 | HCF-LCM cube relation | C (provisional) | Use prime factors or Euclid; verify the common-divisor condition. |
| 2026 | 60 | Divisibility-by-eleven digit puzzle | D (provisional) | Use place value, cyclicity or a constrained enumeration. |
| 2026 | 66 | Reversed-digit divisibility count | B (provisional) | Use place value, cyclicity or a constrained enumeration. |

> The table is a non-verbatim routing audit. It records the locally checked Set-A key letter and a
> valid solving route, but does not pretend that UPSC publishes model solutions. The separate
> workbook supplies original solved equivalents for every mechanism.

### Timed mixed transfer

### Q33. Practice variant 5: What is the unit digit of 6^15?

A. 6
B. 7
C. 5
D. 8

**Correct answer: A.** Reduce powers modulo 10 and use the complete unit-digit cycle.


### Q34. Practice variant 5: What is the remainder when 205 is divided by 11?

A. 8
B. 7
C. 6
D. 9

**Correct answer: B.** Division algorithm: n = mq + r with 0 <= r < m.


### Q35. Practice variant 5: What is the HCF of 20 and 30?

A. 11
B. 9
C. 10
D. 12

**Correct answer: C.** Prime factorisation or Euclid's algorithm gives the greatest common divisor.


### Q36. Practice variant 5: How many positive divisors does 108 have?

A. 13
B. 11
C. 14
D. 12

**Correct answer: D.** If n = product p_i^a_i, the divisor count is product (a_i + 1).


### Q37. Practice variant 5: How many trailing zeros are in 45! ?

A. 10
B. 11
C. 9
D. 12

**Correct answer: A.** Count factors of 5 by repeated division; factors of 2 are more abundant.


### Q38. Practice variant 5: How many multiples of 11 lie from 14 through 120, inclusive?

A. 10
B. 9
C. 8
D. 11

**Correct answer: B.** Use floor(high/d) - floor((low-1)/d).


### Q39. Practice variant 5: The sequence starts 7, 13, 19, ... . What is its 8th term?

A. 50
B. 48
C. 49
D. 51

**Correct answer: C.** This is an arithmetic progression: a_n = a + (n-1)d.


### Q40. Practice variant 5: How many decimal digits are in 1000037?

A. 8
B. 6
C. 9
D. 7

**Correct answer: D.** A positive integer n has floor(log10 n)+1 digits; direct place-value bounding gives the same answer.


## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Number Systems and Number Sense - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy / general mental ability.
> **Core skill:** big-power remainders, highest prime powers in factorials, last-two-digit cycles,
> and inclusion-exclusion counting - all by property, at speed.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/02_Number-Systems-and-Number-Sense.md).*

---

### 1. Architecture

```text
   BIG NUMBER / BIG POWER
        |
   list a^n mod m  (locate any pre-period, then the period)
        |
   tower?  ->  first prove exponent reaches periodic segment
               then map it within that segment; otherwise evaluate directly
        |
   counting how many?  ->  floor-division + inclusion-exclusion
        |
   ANSWER without ever forming the giant number
```

**Analytical claim:** large-power items become manageable after reducing the base modulo `m` and
then checking whether the residue sequence is periodic immediately, has a pre-period, or stabilizes.
Exponent reduction modulo a period is valid only from the point where that period actually applies.

### 2. Advanced tools with conditions

| Tool | Statement | Condition / caution |
|---|---|---|
| ✅ **Cyclic remainders** | If the powers are periodic from the relevant exponent onward with period `k`, reduce the exponent within that periodic segment. | List powers first. When `gcd(a,m) != 1`, check for a pre-period or stabilization; e.g. `2^n mod 8` becomes 0 from `n = 3`. |
| ✅ **Power tower** | For `a^(b^c) mod m`, reduce the exponent modulo a verified period only after accounting for any pre-period. | If `gcd(a,m) = 1`, Euler/Carmichael-style periodicity is available; otherwise inspect the residue sequence directly. |
| ✅ **Exponent of prime p in n!** | `v_p(n!) = floor(n/p) + floor(n/p^2) + ...`; the highest power dividing `n!` is `p^v_p(n!)`. | Trailing zeros equal `v_5(n!)` (since 2s are more plentiful). |
| ✅ **Last two digits** | Track `mod 100`; many bases have short 2-digit cycles. | e.g., `7^4 ≡ 01 (mod 100)`. |
| ✅ **Inclusion-exclusion** | `\|A∪B\| = \|A\| + \|B\| - \|A∩B\|`. | For "divisible by neither", subtract the union from the range. |

### 3. Harder methods (worked)

#### 📝 Method 1 - power tower remainder

**Remainder of `32^(32^32)` divided by 7.** `32 ≡ 4 (mod 7)`; powers of 4 mod 7 cycle
(4, 2, 1) with period **3**. Reduce exponent: `32 ≡ 2 (mod 3)`, so `32^32 ≡ 2^32 ≡ (-1)^32 ≡ 1
(mod 3)`. Hence `4^1 = 4`. **Remainder = 4.** *(Verified.)*

#### 📝 Method 2 - exponent of a prime in a factorial

**Exponent of 3 in `100!`.** `floor(100/3) + floor(100/9) + floor(100/27) + floor(100/81)
= 33 + 11 + 3 + 1 =` **48**, so the highest power of 3 dividing `100!` is **`3^48`**. *(Verified.)*

#### 📝 Method 3 - last two digits

**Last two digits of `7^100`.** `7^4 = 2401 ≡ 01 (mod 100)`, so `7^100 = (7^4)^25 ≡ 01`. **Last two
digits = 01.** *(Verified.)*

#### 📝 Method 4 - when the base and modulus share a factor (find the eventual period)

⚠️ The "reduce the exponent modulo the cycle length" habit **fails** when `gcd(a, m) != 1`. List the
residues first:

| `n` | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `6^n mod 8` | 6 | 4 | **0** | 0 | 0 | 0 |
| `2^n mod 8` | 2 | 4 | **0** | 0 | 0 | 0 |

The sequence has a **pre-period** and then stabilises at 0 from `n = 3` onward (an eventual period
of 1), because `8 = 2^3` divides every `6^n` and `2^n` with `n >= 3`. So `6^25 mod 8 =` **0**.
Reducing 25 by a cycle assumed to start at exponent 1 is unsafe; first locate the pre-period and
eventual period. *(Verified.)*

- 🔑 **Escalation rule:** before reducing an exponent, ask **"is `gcd(base, modulus) = 1`?"** If yes,
  powers are periodic from exponent 1; verify the cycle length before reducing. If no, write out
  residues and locate any **pre-period plus eventual cycle** (which may be a constant); non-coprime
  bases can still cycle immediately.

### 4. Time-saving techniques (safe conditions)

- ⚠️ **Coprimality gate - run this before any exponent reduction.** If `gcd(base, modulus) = 1`, a
  genuine cycle exists and reducing the exponent modulo its length is safe. If not, list residues and
  look for a **pre-period or stabilisation** instead (Method 4). *This single check prevents the most
  expensive error in the family.*
- ⚠️ **Negatives modulo m.** Replace a base by a small negative residue (e.g., `15 ≡ -1 mod 4`) to
  make powers trivial. *Safe always.*
- ⚠️ **Parity/last-digit elimination.** Kill options of the wrong parity or unit digit before any
  full solve. *Safe always.*
- ⚠️ **Count 5s for factorial zeros.** *Safe always* (2s dominate).
- ⚠️ **Exponent reduction requires a verified periodic segment**; list powers first. *Do not assume
  immediate periodicity or a universal period, especially when the base and modulus are non-coprime.*

### 5. Boundary cases

- ⚠️ Within a cycle that starts at exponent 1, a reduced exponent of `0` selects the **last cycle
  position**. If there is a pre-period, map the exponent relative to the cycle's actual start instead.
- ⚠️ A **stabilising** sequence has an eventual constant cycle (period 1). Do not apply a period
  assumed from exponent 1: first check that the exponent lies beyond its pre-period.
- ⚠️ "Divisible by **either**" (`|A| + |B| - |A∩B|`) and "divisible by **exactly one**"
  (`|A| + |B| - 2|A∩B|`) are different counts; read which is asked.
- ⚠️ Inclusion-exclusion needs the **intersection** term (divisible by `lcm`), not the product of the
  two divisors, unless they are coprime.
- ⚠️ `HCF x LCM = product` **fails** for three or more numbers - use prime factorisation instead.
- ⚠️ A "last two digits" answer below 10 keeps its **leading zero** (`3^101 -> 03`, not `3`).

### 6. Advanced traps

- ❌ Reducing the exponent modulo `m` instead of modulo the **cycle length**. -> Reduce by the period.
- ❌ Reducing modulo a period before checking non-coprime stabilization/pre-period. -> List residues
  and locate where repetition actually begins.
- ❌ Counting trailing zeros of `n!` by 2s. -> Count 5s.
- ❌ Stopping the `v_p(n!)` floor sum one term early. -> Continue until the term is 0.
- ❌ In "divisible by neither 2 nor 3", subtracting `50 + 33` without adding back multiples of 6. ->
  Use inclusion-exclusion.
- ❌ Answering the "either" count when "exactly one" was asked. -> Subtract the overlap **twice**.
- ❌ Treating `a^0` inside a cycle as term 0. -> It is the last cycle term.

### 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Wrong cycle length | C | List powers until repeat before reducing. |
| Off-by-one in floor sums | X | Re-add the floor terms; check the last non-zero term. |
| Forgetting intersection term | A | Write the inclusion-exclusion formula every time. |
| Slips on giant multiplications | X | Never form the giant number; stay in mod. |

### 8. Advanced drill (with full solutions)

> ⚠️ These items are **new** - none repeats Methods 1-4 above or an example in the Foundation file.

1. Trailing zeros of `50!`.
2. How many integers from 1 to 1000 are divisible by **3 or 5**?
3. Remainder when `2^100` is divided by 9.
4. What is the **highest power of 2** that divides `50!`?
5. Last two digits of `3^101`.
6. How many integers from 1 to 300 are divisible by **exactly one** of 4 and 6?
7. Remainder when `10^30` is divided by 16.

**Solutions.**

1. **12.** `floor(50/5) + floor(50/25) = 10 + 2 = 12`. *(Verified.)*
2. **467.** `floor(1000/3) + floor(1000/5) - floor(1000/15) = 333 + 200 - 66 = 467`. *(Verified.)*
3. **7.** `gcd(2, 9) = 1`, so a cycle exists: `2^6 = 64 ≡ 1 (mod 9)`, period **6**.
   `100 mod 6 = 4` -> `2^4 = 16 ≡ 7`. *(Verified.)*
4. **`2^47`.** `v_2(50!) = 25 + 12 + 6 + 3 + 1 = 47`. *(Verified - keep adding floors until the term
   is 0; the last non-zero term here is `floor(50/32) = 1`.)*
5. **03.** `3^20 ≡ 01 (mod 100)`, so `3^100 ≡ 01` and `3^101 ≡ 3`, i.e. the last two digits are
   **03** - write the leading zero. *(Verified.)*
6. **75.** `|A| = floor(300/4) = 75`, `|B| = floor(300/6) = 50`, `|A ∩ B| = floor(300/12) = 25`.
   "Exactly one" `= |A| + |B| - 2|A ∩ B| = 75 + 50 - 50 = 75`. *(Verified.)* ⚠️ Subtracting the
   overlap **once** (the "either" count) would give 100 - a different question.
7. **0.** `gcd(10, 16) = 2 != 1`, so there is **no cycle to reduce into** - apply the Method 4 gate.
   Listing residues gives `10, 4, 8, 0, 0, ...`: the sequence **stabilises** at 0 from `n = 4`, because
   `16 = 2^4` divides `10^n` once `n >= 4`. Since `30 >= 4`, the remainder is **0**. *(Verified.)*

### 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Number-system items are a **substantial recurring block**: 13/80 in 2024, 19/80 in 2025, and
  a provisional 12/80 in 2026. They reward the property-first habit far more than long division.
- ⚠️ Recurring shapes: **unit-digit / last-digit of a power**, **remainder of a large power**,
  **HCF/LCM word problems**, **trailing-zeros / factor-count**, and **number/letter series**.
- ⚠️ The papers reward candidates who **reduce before computing**; brute force here is the classic
  time sink flagged in the [Master Framework](../00_Master-Framework.md).

### 10. Study links

- ✅ [Foundation companion](../basic/02_Number-Systems-and-Number-Sense.md).
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - number properties decide many
  data-sufficiency items.
- ✅ [Logical Reasoning, Coding, Counting and DI](./06_Logical-Reasoning-Coding-Counting-and-DI.md) - counting/inclusion-exclusion overlap.

> **Ownership note:** appended historical ledgers may list cryptarithmetic or broad sequence demands
> beside number questions. Their mechanism is owned by Topic 06/08; this companion supplies only
> number-property prerequisites and must not be used to relabel those topics as Number Systems.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
### Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 65

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 3 | Number matrix pattern | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 36 | Digit-ordered number count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 9 | Digit frequency count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 15 | Divisibility set overlap | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 33 | Reversed-digit ratio pairs | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 48 | Number series pattern | Objective question; official key unavailable locally | Cross-owner reference; key unavailable locally | **Route to Topic 08** for sequence method; retain Topic 02 only for numeric properties. |
| 2019 | CSAT | 51 | Number series pattern | Objective question; official key unavailable locally | Cross-owner reference; key unavailable locally | **Route to Topic 08** for sequence method; retain Topic 02 only for numeric properties. |
| 2019 | CSAT | 53 | Page-digit range count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 60 | Multi-digit divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 75 | Digit sum divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 7 | Trailing-zero count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 8 | Cyclic-sum divisibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 10 | Digit-sum primality | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 11 | Digit symbol equation | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 12 | HCF length measurement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 13 | Prime-offset sequence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 14 | Page-sum torn leaf | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 37 | Digit and divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 50 | Largest value among fractional and negative-exponent powers | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 51 | HCF of measurements | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 53 | Recurring decimal conversion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 54 | LCM remainder constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 56 | Product remainder calculation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 58 | Digit sum of power | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 75 | Difference-of-squares factoring | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 76 | Fraction shift comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 77 | Divisibility condition digit | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 5 | Cyclic remainder pattern | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 6 | Divisibility digit value | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 26 | Sequence incorrect term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 36 | Digit-permutation sum divisibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 50 | Number sequence missing term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 59 | Cryptarithmetic digit addition | Objective question; official key unavailable locally | Cross-owner reference; key unavailable locally | **Route to Topic 06** for the puzzle mechanism; Topic 02 supplies digit constraints only. |
| 2021 | CSAT | 60 | Cryptarithmetic digit multiplication | Objective question; official key unavailable locally | Cross-owner reference; key unavailable locally | **Route to Topic 06** for the puzzle mechanism; Topic 02 supplies digit constraints only. |
| 2021 | CSAT | 67 | Consecutive-integer property | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 76 | Digit-interchange difference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 79 | Repunit smallest multiplier | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 4 | Number sequence term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 5 | Divisibility digit arrangement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 9 | Number magnitude comparison | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 47 | LCM parity minimum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 54 | Digit sum bound statements | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 58 | Product modular remainder | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 65 | LCM remainder threshold | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 66 | Digit reversal product | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 67 | Prime composite property | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 74 | Exponent maximum value | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 75 | Number sequence term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 7 | Product remainder modulo | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 8 | Unit digit expansion | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 9 | Digit-sum addition puzzle | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 10 | Digit-sum ratio minimum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 14 | Integer parity determination | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 15 | Prime-composite property check | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 16 | Digit multiplication constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 17 | Repeated-block divisibility | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 25 | Conditional divisor count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 27 | Repunit remainder modulo | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 28 | Repunit square digit sum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 29 | Range digit-sum total | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 45 | Divisor-remainder bound count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 46 | Repeated-digit sum constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 47 | Permuted-digit number sum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 74 | Large power remainder | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 76 | Cryptarithmetic digit solve | Objective question; official key unavailable locally | Cross-owner reference; key unavailable locally | **Route to Topic 06** for the puzzle mechanism; Topic 02 supplies digit constraints only. |

#### What this owner must now support

- Number matrix pattern
- Digit-ordered number count
- Digit frequency count
- Divisibility set overlap
- Reversed-digit ratio pairs
- Number series pattern — routed to Topic 08 (cross-owner reference)
- Page-digit range count
- Multi-digit divisibility count
- Digit sum divisibility count
- Trailing-zero count
- Cyclic-sum divisibility
- Digit-sum primality
- Digit symbol equation
- HCF length measurement
- Prime-offset sequence
- Page-sum torn leaf
- Digit and divisibility count
- Largest value among fractional and negative-exponent powers
- HCF of measurements
- Recurring decimal conversion
- LCM remainder constraint
- Product remainder calculation
- Digit sum of power
- Difference-of-squares factoring
- Fraction shift comparison
- Divisibility condition digit
- Cyclic remainder pattern
- Divisibility digit value
- Sequence incorrect term — routed to Topic 08 (cross-owner reference)
- Digit-permutation sum divisibility
- Number sequence missing term — routed to Topic 08 (cross-owner reference)
- Cryptarithmetic digit addition — routed to Topic 06 (cross-owner reference)
- Cryptarithmetic digit multiplication — routed to Topic 06 (cross-owner reference)
- Consecutive-integer property
- Digit-interchange difference
- Repunit smallest multiplier
- Number sequence term — routed to Topic 08 (cross-owner reference)
- Divisibility digit arrangement
- Number magnitude comparison
- LCM parity minimum
- Digit sum bound statements
- Product modular remainder
- LCM remainder threshold
- Digit reversal product
- Prime composite property
- Exponent maximum value
- Product remainder modulo
- Unit digit expansion
- Digit-sum addition puzzle
- Digit-sum ratio minimum
- Integer parity determination
- Prime-composite property check
- Digit multiplication constraint
- Repeated-block divisibility
- Conditional divisor count
- Repunit remainder modulo
- Repunit square digit sum
- Range digit-sum total
- Divisor-remainder bound count
- Repeated-digit sum constraint
- Permuted-digit number sum
- Large power remainder
- Cryptarithmetic digit solve — routed to Topic 06 (cross-owner reference)

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->

## CONSOLIDATED REGISTER NOTES

### Complete revision spine

- **Number universe:** Natural, whole, integer, rational, irrational and real numbers.
- **Divisibility:** Use prime-factor and digit tests only within their valid base-ten conditions.
- **Primes and factors:** Factorise before counting divisors or comparing powers.
- **HCF and LCM:** Use gcd-lcm relations with integer and positivity checks.
- **Remainders:** Reduce early and preserve the modulus.
- **Unit digits:** Use cyclicity and treat exponent-zero cases separately.
- **Digits and place value:** Translate reversal and digit count into base-ten equations.
- **Powers and factorials:** Use repeated division for prime exponents and trailing zeros.
- **Fractions and decimals:** Convert recurring forms through algebra, not memorised guesses.
- **Series:** Test differences, ratios, alternation and position rules.
- **Magnitude and estimation:** Bound before calculating exactly.
- **Verification:** Plug back, check parity, digit count, remainder and order of magnitude.

### Ownership and close-option firewall

- **Own here:** Owns integer classes, divisibility, primes, factors, HCF/LCM, remainders, digits, powers, roots, factorial valuations, recurring decimals, magnitude and number series.
- **Do not duplicate:** Commercial percentages belong to Topic 03; rate contexts to Topic 04; algebraic unknowns and sufficiency to Topic 05; coding/counting structures to Topic 06.
- **Verification:** Each shortcut is stated with its modulus, parity, cycle or factorisation condition. Deterministic checks recompute every generated answer by direct arithmetic or enumeration.

### Timed answer route

`CLASSIFY → EXTRACT → REPRESENT → EXECUTE → VERIFY → DECIDE`

- Use estimation or option elimination only after preserving the governing condition.
- A blank costs zero; a rushed unsupported answer also consumes time and may attract negative marks.
- For every error, record concept/application/calculation/reading/passage/time/guess, repair the
  owner, and retry a new item rather than memorising the old option.

