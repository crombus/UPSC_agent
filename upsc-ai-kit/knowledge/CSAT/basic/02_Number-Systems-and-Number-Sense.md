# Number Systems and Number Sense - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy / general mental ability.
> **Core skill:** solve by a **number property** (divisibility, unit digit, remainder, factor count)
> instead of heavy calculation.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). All drills below are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example (not a UPSC item).
> *Companion: `advanced/02_Number-Systems-and-Number-Sense.md`.*

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

| Tool | Rule (exam-ready) |
|---|---|
| ✅ **Div by 2 / 5 / 10** | Look at the last digit (even; 0 or 5; 0). |
| ✅ **Div by 4 / 8** | Last **2** digits div by 4; last **3** digits div by 8. |
| ✅ **Div by 3 / 9** | Digit sum div by 3 / by 9. |
| ✅ **Div by 11** | (Sum of odd-place digits) - (sum of even-place digits) is 0 or a multiple of 11. |
| ✅ **Unit-digit cycles** | 2,3,7,8 repeat with period **4**; 4,9 with period **2**; 0,1,5,6 are constant. |
| ✅ **Trailing zeros of n!** | `floor(n/5) + floor(n/25) + floor(n/125) + ...` (count 5s). |
| ✅ **Number of factors** | For `n = p^a q^b r^c`, factor count `= (a+1)(b+1)(c+1)`. |
| ✅ **HCF x LCM** | For two numbers, `HCF x LCM = product of the numbers`. |

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

## 5. Original solved examples

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

## 6. Must-Know facts

- ✅ A number is div by 6 iff div by **2 and 3**; by 12 iff div by **3 and 4**.
- ✅ Product of two numbers = HCF x LCM (two numbers only).
- ✅ Even x anything = even; odd x odd = odd; even + odd = odd (parity is a fast eliminator).
- ✅ Unit digit of any power depends only on the **base's unit digit** and `n mod 4`.
- ✅ Trailing zeros of a factorial are governed by the count of **5s**, not 2s (2s are always more).

## 7. Common traps

- ❌ Counting 2s for trailing zeros of `n!`. -> Count **5s**; 2s are surplus.
- ❌ Using `HCF x LCM = product` for **three** numbers. -> Two numbers only.
- ❌ Taking `n mod 4 = 0` as "cycle position 0". -> Use the **4th (last)** term of the cycle.
- ❌ Forgetting the div-by-11 **alternating** sign. -> It is odd-place minus even-place.
- ❌ Confusing "same remainder" with "exact division". -> Same remainder uses HCF of **differences**.

## 8. Quick checks

- ✅ Can you get a unit digit of any `a^n` in under 10 seconds via `n mod 4`?
- ✅ Can you state trailing zeros of `n!` without multiplying?
- ✅ Given `n = p^a q^b`, can you write the factor count immediately?

## 9. Mini-drill (with answers and explanations)

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

## 10. Study links

- ✅ Advanced companion: `advanced/02_Number-Systems-and-Number-Sense.md` - big-power remainders,
  highest prime powers, and inclusion-exclusion counting.
- ✅ `03_Arithmetic-and-Commercial-Math.md` (basic) - ratio and percentage build on factor sense.
- ✅ `05_Algebra-Inequalities-and-Data-Sufficiency.md` (basic) - number properties power many DS items.
