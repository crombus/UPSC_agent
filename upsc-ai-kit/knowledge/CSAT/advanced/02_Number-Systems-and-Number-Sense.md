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
| ✅ **Inclusion-exclusion** | `|A∪B| = |A| + |B| - |A∩B|`. | For "divisible by neither", subtract the union from the range. |

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

## 4. Time-saving techniques (safe conditions)

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
- ⚠️ Inclusion-exclusion needs the **intersection** term (divisible by `lcm`), not the product of the
  two divisors, unless they are coprime.
- ⚠️ `HCF x LCM = product` **fails** for three or more numbers - use prime factorisation instead.

## 6. Advanced traps

- ❌ Reducing the exponent modulo `m` instead of modulo the **cycle length**. -> Reduce by the period.
- ❌ Reducing modulo a period before checking non-coprime stabilization/pre-period. -> List residues
  and locate where repetition actually begins.
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
