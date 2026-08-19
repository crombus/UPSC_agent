# Number Systems and Number Sense - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy / general mental ability.
> **Core skill:** solve by a **number property** (divisibility, unit digit, remainder, factor count)
> instead of heavy calculation.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). All drills below are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example (not a UPSC item).
> *Companion: [Advanced Drill](../advanced/02_Number-Systems-and-Number-Sense.md).*

---

## 1. Visual foundation

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

## 2. Essential rules

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

## 3. Method (property-first)

1. Decide whether the question wants the **exact value** or only a **property** (last digit, remainder,
   count, divisor).
2. Pick the matching tool from Section 2.
3. Reduce with **modular thinking**: replace big numbers by their remainders before combining.
4. Only compute the full value if nothing else works - and then **estimate first** to catch slips.

## 4. Formulas and conditions

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

## 5. Core number sense methods

### 5.1 Recurring decimals

| Form | Convert | Condition |
|---|---|---|
| `0.\overline{a}` | `a/9` | `a` is one recurring digit. |
| `0.\overline{ab}` | `ab/99` | `ab` is the two-digit repeating block. |
| `0.uv\overline{w}` | `(uvw - uv) / [10^2(10^1-1)]` | Subtract the non-repeating prefix; denominator has prefix zeros, then recurring-block 9s. |

**Worked example.** `x = 0.1\overline{6}`. Then `100x = 16.\overline6` and `10x =
1.\overline6`; subtract: `90x = 15`, so `x = 1/6`. Do not use the `a/9` shortcut when a
non-repeating prefix exists.

### 5.2 Place value, digit counts and reversal

- An `n`-digit positive integer lies from `10^(n-1)` to `10^n - 1`.
- Digits used from 1 to `N` are counted in blocks: 1–9 uses `9 x 1`; 10–99 uses `90 x 2`; then
  count the final partial block. For a range `L` to `U`, use `digits(1..U) - digits(1..L-1)`.
- A two-digit number with digits `a,b` is `10a+b`; its reversal is `10b+a`. Their difference is
  `9(a-b)` and their sum is `11(a+b)`. Here `a != 0`, and a reversed “two-digit number” also
  requires `b != 0`.

**Worked example.** Pages 1–250 use `9 + 90x2 + 151x3 =` **642 digits**. A number `10a+b`
minus its reversal is divisible by 9; this is a property, not proof that every multiple of 9 is a
digit reversal.

### 5.3 Unknown digits and exponents

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

### 5.4 Counting multiples in a range

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

## 6. Original solved examples

### 📝 Example A (unit digit)

**Find the unit digit of `3^35`.** Cycle of 3 is (3, 9, 7, 1), period 4. `35 mod 4 = 3` -> third term
-> **7**. *(Verified.)*

### 📝 Example B (remainder)

**Remainder when `2^50` is divided by 7.** `2^3 = 8 ≡ 1 (mod 7)`, period 3. `50 mod 3 = 2` -> `2^2 = 4`.
**Remainder = 4.** *(Verified.)*

### 📝 Example C (HCF-LCM)

**Two numbers have HCF 12 and LCM 180; one is 36. Find the other.** Other `= (HCF x LCM)/known =
(12 x 180)/36 =` **60.** *(Verified.)*

### 📝 Example D (trailing zeros)

**How many zeros end `25!`?** `floor(25/5) + floor(25/25) = 5 + 1 =` **6.** *(Verified.)*

### 📝 Example E (factor count)

**Number of factors of 360.** `360 = 2^3 x 3^2 x 5^1` -> `(3+1)(2+1)(1+1) =` **24.** *(Verified.)*

## 7. Must-Know facts

- ✅ A number is div by 6 iff div by **2 and 3**; by 12 iff div by **3 and 4**. (Both work because the
  pairs are **coprime** - "div by 2 and 6" would **not** give div by 12.)
- ✅ Product of two numbers = HCF x LCM (two numbers only).
- ✅ Even x anything = even; odd x odd = odd; even + odd = odd (parity is a fast eliminator).
- ✅ Unit digit of any power `a^n` with `n >= 1` depends only on the **base's unit digit** and
  `n mod 4` (taking a remainder of 0 as the 4th, last, cycle term).
- ✅ Trailing zeros of a factorial are governed by the count of **5s**, not 2s (2s are always more).
- ✅ A number has an **odd** number of factors exactly when it is a **perfect square**.

## 8. Common traps

- ❌ Counting 2s for trailing zeros of `n!`. -> Count **5s**; 2s are surplus.
- ❌ Using `HCF x LCM = product` for **three** numbers. -> Two numbers only.
- ❌ Taking `n mod 4 = 0` as "cycle position 0". -> Use the **4th (last)** term of the cycle.
- ❌ Forgetting the div-by-11 **alternating** sign. -> It is odd-place minus even-place.
- ❌ Splitting a divisor into non-coprime factors ("div by 2 and 6 => div by 12"). -> The factors
  must be **coprime**.
- ❌ Confusing "same remainder" with "exact division". -> Same remainder uses HCF of **differences**.

## 9. Quick checks

- ✅ Can you get a unit digit of any `a^n` in under 10 seconds via `n mod 4`?
- ✅ Can you state trailing zeros of `n!` without multiplying?
- ✅ Given `n = p^a q^b`, can you write the factor count immediately?

## 10. Mini-drill (with answers and explanations)

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

## 11. Timed Core drill, diagnosis and retry gate

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

## 12. Study links

- ✅ [Advanced companion](../advanced/02_Number-Systems-and-Number-Sense.md) - big-power remainders,
  highest prime powers, and inclusion-exclusion counting.
- ✅ [Arithmetic and Commercial Math](./03_Arithmetic-and-Commercial-Math.md) - ratio and percentage build on factor sense.
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - number properties power many DS items.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
## 2026 PYQ Integration

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

### What this owner must now support

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
## Recent PYQ Integration (2024-2025)

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

### What this owner must now support

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
## Historical PYQ Integration (2018-2023)

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

### What this owner must now support

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
