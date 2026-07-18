# Number Systems and Number Sense - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy / general mental ability.
> **Core skill:** big-power remainders, highest prime powers in factorials, last-two-digit cycles,
> and inclusion-exclusion counting - all by property, at speed.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `basic/02_Number-Systems-and-Number-Sense.md`.*

---

## 1. Architecture

```text
   BIG NUMBER / BIG POWER
        |
   reduce mod m  (find the cycle length of a mod m)
        |
   tower of powers?  ->  reduce the EXPONENT mod (cycle length)
        |
   counting how many?  ->  floor-division + inclusion-exclusion
        |
   ANSWER without ever forming the giant number
```

**Analytical claim:** every "impossible-looking" number item collapses once you replace the base by
its remainder and the exponent by its residue modulo the cycle length.

## 2. Advanced tools with conditions

| Tool | Statement | Condition / caution |
|---|---|---|
| ✅ **Cyclic remainders** | `a^n mod m` repeats with some period `k`; reduce `n mod k`. | Find `k` by listing powers until the residue repeats. |
| ✅ **Power tower** | For `a^(b^c) mod m`, reduce the **exponent** `b^c` modulo the cycle length of `a mod m`. | Handle exponent `≡ 0` as the full cycle length, not 0. |
| ✅ **Highest power of prime p in n!** | `floor(n/p) + floor(n/p^2) + ...` | Trailing zeros = highest power of 5 (since 2s are more plentiful). |
| ✅ **Last two digits** | Track `mod 100`; many bases have short 2-digit cycles. | e.g., `7^4 ≡ 01 (mod 100)`. |
| ✅ **Inclusion-exclusion** | `|A∪B| = |A| + |B| - |A∩B|`. | For "divisible by neither", subtract the union from the range. |

## 3. Harder methods (worked)

### 📝 Method 1 - power tower remainder

**Remainder of `32^(32^32)` divided by 7.** `32 ≡ 4 (mod 7)`; powers of 4 mod 7 cycle
(4, 2, 1) with period **3**. Reduce exponent: `32 ≡ 2 (mod 3)`, so `32^32 ≡ 2^32 ≡ (-1)^32 ≡ 1
(mod 3)`. Hence `4^1 = 4`. **Remainder = 4.** *(Verified.)*

### 📝 Method 2 - highest prime power in a factorial

**Highest power of 3 dividing `100!`.** `floor(100/3) + floor(100/9) + floor(100/27) + floor(100/81)
= 33 + 11 + 3 + 1 =` **48.** *(Verified.)*

### 📝 Method 3 - last two digits

**Last two digits of `7^100`.** `7^4 = 2401 ≡ 01 (mod 100)`, so `7^100 = (7^4)^25 ≡ 01`. **Last two
digits = 01.** *(Verified.)*

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Negatives modulo m.** Replace a base by a small negative residue (e.g., `15 ≡ -1 mod 4`) to
  make powers trivial. *Safe always.*
- ⚠️ **Parity/last-digit elimination.** Kill options of the wrong parity or unit digit before any
  full solve. *Safe always.*
- ⚠️ **Count 5s for factorial zeros.** *Safe always* (2s dominate).
- ⚠️ **Exponent-reduction requires the correct cycle length**; verify the cycle by listing a few
  powers first. *Do not assume period 4 for every base mod m.*

## 5. Boundary cases

- ⚠️ When the reduced exponent is `0`, use the **full cycle length** (e.g., position 0 means the last
  term of the cycle), not "zero-th term".
- ⚠️ Inclusion-exclusion needs the **intersection** term (divisible by `lcm`), not the product of the
  two divisors, unless they are coprime.
- ⚠️ `HCF x LCM = product` **fails** for three or more numbers - use prime factorisation instead.

## 6. Advanced traps

- ❌ Reducing the exponent modulo `m` instead of modulo the **cycle length**. -> Reduce by the period.
- ❌ Counting trailing zeros of `n!` by 2s. -> Count 5s.
- ❌ In "divisible by neither 2 nor 3", subtracting `50 + 33` without adding back multiples of 6. ->
  Use inclusion-exclusion.
- ❌ Treating `a^0` inside a cycle as term 0. -> It is the last cycle term.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Wrong cycle length | C | List powers until repeat before reducing. |
| Off-by-one in floor sums | X | Re-add the floor terms; check the last non-zero term. |
| Forgetting intersection term | A | Write the inclusion-exclusion formula every time. |
| Slips on giant multiplications | X | Never form the giant number; stay in mod. |

## 8. Advanced drill (with full solutions)

1. Trailing zeros of `50!`.
2. How many integers from 1 to 1000 are divisible by **3 or 5**?
3. Remainder of `2^50` divided by 7.
4. How many integers from 1 to 100 are divisible by **neither 2 nor 3**?
5. Unit digit of `3^35`.

**Solutions.**

1. **12.** `floor(50/5) + floor(50/25) = 10 + 2 = 12`. *(Verified.)*
2. **467.** `floor(1000/3) + floor(1000/5) - floor(1000/15) = 333 + 200 - 66 = 467`. *(Verified.)*
3. **4.** `2^3 ≡ 1 (mod 7)`, `50 mod 3 = 2`, `2^2 = 4`. *(Verified.)*
4. **33.** Divisible by 2 or 3 = `50 + 33 - 16 = 67`; neither = `100 - 67 = 33`. *(Verified.)*
5. **7.** Cycle (3,9,7,1); `35 mod 4 = 3` -> 7. *(Verified.)*

## 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Number-system items are a **steady presence** (roughly a tenth of each paper) and reward the
  property-first habit far more than long division.
- ⚠️ Recurring shapes: **unit-digit / last-digit of a power**, **remainder of a large power**,
  **HCF/LCM word problems**, **trailing-zeros / factor-count**, and **number/letter series**.
- ⚠️ The papers reward candidates who **reduce before computing**; brute force here is the classic
  time sink flagged in `00_Master-Framework.md`.

## 10. Study links

- ✅ Foundation companion: `basic/02_Number-Systems-and-Number-Sense.md`.
- ✅ `advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md` - number properties decide many
  data-sufficiency items.
- ✅ `advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md` - counting/inclusion-exclusion overlap.
