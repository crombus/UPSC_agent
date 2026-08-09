# Number Systems and Number Sense - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy / general mental ability.
> **Core skill:** big-power remainders, highest prime powers in factorials, last-two-digit cycles,
> and inclusion-exclusion counting - all by property, at speed.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/02_Number-Systems-and-Number-Sense.md).*

---

## 1. Architecture

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

## 2. Advanced tools with conditions

| Tool | Statement | Condition / caution |
|---|---|---|
| ✅ **Cyclic remainders** | If the powers are periodic from the relevant exponent onward with period `k`, reduce the exponent within that periodic segment. | List powers first. When `gcd(a,m) != 1`, check for a pre-period or stabilization; e.g. `2^n mod 8` becomes 0 from `n = 3`. |
| ✅ **Power tower** | For `a^(b^c) mod m`, reduce the exponent modulo a verified period only after accounting for any pre-period. | If `gcd(a,m) = 1`, Euler/Carmichael-style periodicity is available; otherwise inspect the residue sequence directly. |
| ✅ **Exponent of prime p in n!** | `v_p(n!) = floor(n/p) + floor(n/p^2) + ...`; the highest power dividing `n!` is `p^v_p(n!)`. | Trailing zeros equal `v_5(n!)` (since 2s are more plentiful). |
| ✅ **Last two digits** | Track `mod 100`; many bases have short 2-digit cycles. | e.g., `7^4 ≡ 01 (mod 100)`. |
| ✅ **Inclusion-exclusion** | `\|A∪B\| = \|A\| + \|B\| - \|A∩B\|`. | For "divisible by neither", subtract the union from the range. |

## 3. Harder methods (worked)

### 📝 Method 1 - power tower remainder

**Remainder of `32^(32^32)` divided by 7.** `32 ≡ 4 (mod 7)`; powers of 4 mod 7 cycle
(4, 2, 1) with period **3**. Reduce exponent: `32 ≡ 2 (mod 3)`, so `32^32 ≡ 2^32 ≡ (-1)^32 ≡ 1
(mod 3)`. Hence `4^1 = 4`. **Remainder = 4.** *(Verified.)*

### 📝 Method 2 - exponent of a prime in a factorial

**Exponent of 3 in `100!`.** `floor(100/3) + floor(100/9) + floor(100/27) + floor(100/81)
= 33 + 11 + 3 + 1 =` **48**, so the highest power of 3 dividing `100!` is **`3^48`**. *(Verified.)*

### 📝 Method 3 - last two digits

**Last two digits of `7^100`.** `7^4 = 2401 ≡ 01 (mod 100)`, so `7^100 = (7^4)^25 ≡ 01`. **Last two
digits = 01.** *(Verified.)*

### 📝 Method 4 - when the base and modulus share a factor (no period at all)

⚠️ The "reduce the exponent modulo the cycle length" habit **fails** when `gcd(a, m) != 1`. List the
residues first:

| `n` | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `6^n mod 8` | 6 | 4 | **0** | 0 | 0 | 0 |
| `2^n mod 8` | 2 | 4 | **0** | 0 | 0 | 0 |

The sequence does not cycle - it **stabilises at 0** from `n = 3` onward, because `8 = 2^3` divides
every `6^n` and `2^n` with `n >= 3`. So `6^25 mod 8 =` **0**, and any attempt to "reduce 25 modulo a
period" is meaningless here. *(Verified.)*

- 🔑 **Escalation rule:** before reducing an exponent, ask **"is `gcd(base, modulus) = 1`?"** If yes,
  a genuine cycle exists and reduction is safe. If no, write out the first few residues and look for
  **stabilisation or a pre-period** instead.

## 4. Time-saving techniques (safe conditions)

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

## 5. Boundary cases

- ⚠️ Within a cycle that starts at exponent 1, a reduced exponent of `0` selects the **last cycle
  position**. If there is a pre-period, map the exponent relative to the cycle's actual start instead.
- ⚠️ A **stabilising** sequence (Method 4) has no cycle at all - the answer is simply the stable value
  once the exponent is large enough.
- ⚠️ "Divisible by **either**" (`|A| + |B| - |A∩B|`) and "divisible by **exactly one**"
  (`|A| + |B| - 2|A∩B|`) are different counts; read which is asked.
- ⚠️ Inclusion-exclusion needs the **intersection** term (divisible by `lcm`), not the product of the
  two divisors, unless they are coprime.
- ⚠️ `HCF x LCM = product` **fails** for three or more numbers - use prime factorisation instead.
- ⚠️ A "last two digits" answer below 10 keeps its **leading zero** (`3^101 -> 03`, not `3`).

## 6. Advanced traps

- ❌ Reducing the exponent modulo `m` instead of modulo the **cycle length**. -> Reduce by the period.
- ❌ Reducing modulo a period before checking non-coprime stabilization/pre-period. -> List residues
  and locate where repetition actually begins.
- ❌ Counting trailing zeros of `n!` by 2s. -> Count 5s.
- ❌ Stopping the `v_p(n!)` floor sum one term early. -> Continue until the term is 0.
- ❌ In "divisible by neither 2 nor 3", subtracting `50 + 33` without adding back multiples of 6. ->
  Use inclusion-exclusion.
- ❌ Answering the "either" count when "exactly one" was asked. -> Subtract the overlap **twice**.
- ❌ Treating `a^0` inside a cycle as term 0. -> It is the last cycle term.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Wrong cycle length | C | List powers until repeat before reducing. |
| Off-by-one in floor sums | X | Re-add the floor terms; check the last non-zero term. |
| Forgetting intersection term | A | Write the inclusion-exclusion formula every time. |
| Slips on giant multiplications | X | Never form the giant number; stay in mod. |

## 8. Advanced drill (with full solutions)

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

## 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Number-system items are a **substantial recurring block**: 13/80 in 2024, 19/80 in 2025, and
  a provisional 12/80 in 2026. They reward the property-first habit far more than long division.
- ⚠️ Recurring shapes: **unit-digit / last-digit of a power**, **remainder of a large power**,
  **HCF/LCM word problems**, **trailing-zeros / factor-count**, and **number/letter series**.
- ⚠️ The papers reward candidates who **reduce before computing**; brute force here is the classic
  time sink flagged in the [Master Framework](../00_Master-Framework.md).

## 10. Study links

- ✅ [Foundation companion](../basic/02_Number-Systems-and-Number-Sense.md).
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - number properties decide many
  data-sufficiency items.
- ✅ [Logical Reasoning, Coding, Counting and DI](./06_Logical-Reasoning-Coding-Counting-and-DI.md) - counting/inclusion-exclusion overlap.

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
| 2018 | CSAT | 3 | Number matrix pattern | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2020 | CSAT | 11 | Digit symbol equation | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 12 | HCF length measurement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 13 | Prime-offset sequence | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 14 | Page-sum torn leaf | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 37 | Digit and divisibility count | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 50 | Irrational number comparison | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2022 | CSAT | 9 | Number magnitude comparison | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 47 | LCM parity minimum | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 54 | Digit sum bound statements | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 58 | Product modular remainder | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 65 | LCM remainder threshold | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 66 | Digit reversal product | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 67 | Prime composite property | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 74 | Exponent maximum value | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 75 | Number sequence term | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 7 | Product remainder modulo | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 8 | Unit digit expansion | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
- Irrational number comparison
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
