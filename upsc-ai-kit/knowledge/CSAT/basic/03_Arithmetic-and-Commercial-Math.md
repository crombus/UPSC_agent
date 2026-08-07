# Arithmetic and Commercial Math - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy.
> **Core skill:** ratio, percentage, average, mixture, profit-loss, interest, partnership and ages -
> solved by **scaling and multipliers**, not long working.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/03_Arithmetic-and-Commercial-Math.md).*

---

## 1. Visual foundation

```text
WORD PROBLEM
     |
 translate to ONE relation:
     |
   part/whole (ratio)  |  per-hundred (percentage)  |  total/count (average)
     |
 apply as a MULTIPLIER   (x1.2 for +20%, x0.8 for -20%)
     |
 combine multipliers for successive changes  ->  read the answer
```

**Core proposition:** ratios and percentages are **multipliers**; chaining multipliers replaces most
step-by-step arithmetic.

## 2. Essential formulas

| Concept | Exam-ready formula |
|---|---|
| ✅ **Percentage change** | New = Old x (1 ± r). Successive changes multiply, they do **not** add. |
| ✅ **Percentage point** | A change **between two percentages**: `50% - 40% = 10 percentage points`, which is a **25% relative** rise. Never write "10%" for it. |
| ✅ **Ratio split** | Divide total by the sum of ratio parts to get one "part". |
| ✅ **Average** | `Average = Sum / Count`; `Sum = Average x Count`. |
| ✅ **Weighted average** | `(w1 a1 + w2 a2 + ...) / (w1 + w2 + ...)`. Equals the plain mean **only** when all weights are equal. |
| ✅ **Alligation** | For `a < m < b`, mixing positive quantities at values a and b to get mean m gives ratio `(b - m) : (m - a)`. At an endpoint, one component has zero quantity; outside `[a,b]`, the target is infeasible. |
| ✅ **Profit / loss** | `SP = CP x (1 ± profit%/loss%)`; profit% is on **CP**. |
| ✅ **Simple interest** | `SI = P x R x T / 100` - interest on the **original principal** every period, so it grows **linearly**. |
| ✅ **Compound interest** | `A = P x (1 + R/100)^T`; `CI = A - P` - interest on the **running amount**, so it grows **geometrically**. |
| ✅ **Non-annual compounding** | For `k` compoundings a year use `A = P x (1 + R/(100k))^(kT)` - halve the rate and double the periods for half-yearly, quarter and quadruple for quarterly. |
| ✅ **Partnership** | Profit share ∝ `capital x time`. |

> 🔑 **Multiplier trap:** a +10% then -10% is **not** zero. `1.10 x 0.90 = 0.99` -> a **1% net fall**.

> 🔑 **Percentage-point trap:** "the pass rate rose from 40% to 50%" is **+10 percentage points** and
> **+25%** relative - two different true numbers for one change. Read which one the stem wants.

## 3. Method

1. Name the quantity asked and the relation type (ratio / percent / average / mixture / commercial).
2. Convert every change to a **multiplier** or a **part**.
3. Combine (multiply multipliers; add parts), then scale to the total.
4. Verify by **magnitude** (is a discount answer smaller than the price? is a share ≤ total?).

## 4. Conditions to respect

- ⚠️ Profit/loss and markup percentages are on **CP** unless a **markup on MP** or **discount on MP**
  is stated - read the base carefully.
- ⚠️ Successive percentages **compound**; only convert to a single number via the product of
  multipliers, never by adding the percentages.
- ⚠️ **A percentage change always needs its base named.** The same absolute move is a different
  percentage on a different base, which is why `+25%` then `-10%` does not return to the start.
- ⚠️ Averages hide distributions - an average is unchanged by swaps that keep the sum.
- ⚠️ `A = P (1 + R/100)^T` assumes **annual** compounding and a **constant** rate; use the `k`-period
  form otherwise, and split the calculation if the rate changes between years.
- ⚠️ `CI - SI = P (R/100)^2` holds **only** for exactly **2 years**, annual compounding, same rate.

## 5. Original solved examples

### 📝 Example A (ratio)

**Divide 3300 among A, B, C in the ratio 2 : 3 : 6.** Parts = 11; one part = `3300/11 = 300`. Shares =
**600, 900, 1800.** *(Verified.)*

### 📝 Example B (successive percentage)

**A population rises 10% then falls 10%. Net change?** `1.10 x 0.90 = 0.99` -> **1% decrease.**
*(Verified.)*

### 📝 Example C (average)

**The average of 5 numbers is 27. One number, 35, is removed. New average of the 4?** Sum `= 135`;
new sum `= 100`; average `= 100/4 =` **25.** *(Verified.)*

### 📝 Example D (alligation)

**In what ratio mix rice at 30 and 40 per kg to get 34 per kg?** `(40 - 34) : (34 - 30) = 6 : 4 =`
**3 : 2.** *(Verified.)*

### 📝 Example E (compound interest)

**CI on 10000 at 10% for 2 years.** `A = 10000 x 1.1^2 = 12100`; `CI = 12100 - 10000 =` **2100.**
*(Verified.)* Compare **SI** on the same terms: `10000 x 10 x 2 / 100 =` **2000.** The `100`
difference is exactly `P (R/100)^2 = 10000 x 0.01`. *(Verified.)*

### 📝 Example F (weighted average vs plain average)

**A class has 30 boys averaging 62 marks and 20 girls averaging 72.** Class average
`= (30 x 62 + 20 x 72) / 50 = (1860 + 1440)/50 = 3300/50 =` **66.**
The plain mean of 62 and 72 is **67** - wrong, because the groups are not the same size.
*(Verified.)*

### 📝 Example G (percentage point vs percent change)

**A district's literacy rate rises from 40% to 50%.** The rise is **10 percentage points**. As a
**relative** change it is `(50 - 40)/40 =` **25%**. Both are correct answers to **different**
questions - and the options will usually contain both. *(Verified.)*

## 6. Must-Know facts

- ✅ `1/2 = 50%`, `1/3 ≈ 33.3%`, `1/4 = 25%`, `1/8 = 12.5%`, `1/20 = 5%` - memorise these for speed.
- ✅ Profit% and loss% are always on **cost price**.
- ✅ For 2 years, `CI - SI = P x (R/100)^2` (a fast check; 2 years only, annual compounding).
- ✅ **SI is linear in time, CI is geometric** - so CI and SI are equal after **one** period and CI is
  larger after that (for a positive rate).
- ✅ A **percentage point** is a gap between percentages; a **percent change** is relative to a base.
- ✅ In partnership, equal-time investors share in the **capital ratio**; equal-capital investors
  share in the **time ratio**.

## 7. Common traps

- ❌ Adding successive percentages (10% + 10% = 20%). -> Multiply multipliers (`1.1 x 1.1 = 1.21`).
- ❌ Taking profit% on selling price. -> It is on **cost price**.
- ❌ Assuming +x% then -x% returns to the start. -> It gives a net `x^2/100 %` fall.
- ❌ Saying "the rate rose 10%" when it rose from 40% to 50%. -> That is **10 percentage points**
  (and 25% relatively).
- ❌ Averaging two group averages by a plain mean when the **group sizes differ**. -> Weight by size.
- ❌ Averaging two speeds/prices by a plain mean when the **weights differ**. -> Weight by quantity.
- ❌ Reading a discount off cost price. -> Discount is off **marked price**.
- ❌ Using the annual CI formula when compounding is half-yearly/quarterly. -> Adjust `R` and `T`.

## 8. Quick checks

- ✅ Can you turn "increases by 25%" into "x1.25" instantly?
- ✅ Given a ratio and a total, can you get one part in one division?
- ✅ Can you write alligation ratio without a diagram?
- ✅ Can you say, for one stated change, both its percentage-point and its percent value?

## 9. Mini-drill (with answers and explanations)

1. If A : B = 2 : 3 and B : C = 4 : 5, find A : B : C.
2. Two successive discounts of 20% and 10% equal what single discount?
3. The average age of 30 students is 12. Including the teacher, the average of 31 becomes 13. Find the
   teacher's age.
4. An article sold for 480 at a 20% loss. Find the cost price.
5. A invests 12000 for 6 months and B invests 8000 for 12 months; total profit is 4200. Find B's share.
6. A scheme's approval rating moves from 25% to 30%. State the change (i) in percentage points and
   (ii) as a percent change.
7. A shop sells 3 kg of rice at 40 per kg and 2 kg at 50 per kg. Find the average price per kg.
8. Find `CI - SI` on 8000 at 5% per annum for 2 years.

**Answers.**

1. **8 : 12 : 15.** Make B common (12): A : B = 8 : 12, B : C = 12 : 15.
2. **28%.** `1 - (0.8 x 0.9) = 0.28`. *(Verified.)*
3. **43.** Students' sum `= 360`; with teacher `= 31 x 13 = 403`; teacher `= 43`. *(Verified.)*
4. **600.** `CP = 480 / 0.8 = 600`. *(Verified.)*
5. **2400.** Capital x time = `72000 : 96000 = 3 : 4`; B = `4200 x 4/7 = 2400`. *(Verified.)*
6. **(i) 5 percentage points. (ii) 20%.** `30 - 25 = 5` points; `(30 - 25)/25 = 0.20`. Both are
   correct - for different questions. *(Verified.)*
7. **44.** Weighted: `(3 x 40 + 2 x 50)/5 = 220/5 = 44`. The plain mean of 40 and 50 is **45**, which
   is wrong because the quantities differ. *(Verified.)*
8. **20.** `CI = 8000 x 1.05^2 - 8000 = 820`; `SI = 8000 x 5 x 2/100 = 800`; difference `= 20`, which
   equals `P (R/100)^2 = 8000 x 0.0025`. *(Verified.)*

## 10. Study links

- ✅ [Advanced companion](../advanced/03_Arithmetic-and-Commercial-Math.md) - repeated replacement,
  markup-plus-discount, and equating-ages methods.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - ratio sense rests on factors.
- ✅ [Rates, Motion, Time and Geometry](./04_Rates-Motion-Time-and-Geometry.md) - averages and ratios extend to speed and work.
