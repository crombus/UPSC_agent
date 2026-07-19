# Arithmetic and Commercial Math - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy.
> **Core skill:** multi-step commercial arithmetic - repeated replacement, markup-and-discount chains,
> equated-ages, expenditure-consumption trade-offs, and two-vessel mixtures.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/03_Arithmetic-and-Commercial-Math.md).*

---

## 1. Architecture

```text
   MULTI-STEP COMMERCIAL PROBLEM
        |
   express each step as a MULTIPLIER or a RATIO
        |
   +----------------+-------------------+
   |                |                   |
 REPEATED         MARKUP + DISCOUNT   MIXTURE / AGES
 replacement      chain               relation to solve
 (fraction)^n     m1 x m2 -> profit%  linear equation
        |
   combine, then VERIFY by magnitude
```

**Analytical claim:** hard arithmetic is a **chain of multipliers plus one linear equation** - never
a pile of separate computations.

## 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Repeated replacement** | After removing and replacing fraction each time, remaining pure part `= initial x (1 - removed/total)^n`. | Same amount removed and replaced each round. |
| ✅ **Markup-then-discount** | Net multiplier `= (1 + markup) x (1 - discount)`; profit% `= (net - 1) x 100`. | Markup on CP, discount on MP. |
| ✅ **Expenditure = price x quantity** | To hold expenditure constant when price rises by r, cut quantity by `r/(1+r)`. | Price and quantity vary inversely. |
| ✅ **Ages** | Set present ages as variables; write one equation per time reference. | Keep "years later/ago" consistent on both sides. |
| ✅ **Two-vessel mixture** | Combined fraction = weighted average of the two fractions by volume. | Weight by the volume actually taken. |

## 3. Harder methods (worked)

### 📝 Method 1 - repeated replacement

**From 40 L of milk, 8 L is removed and replaced with water; repeated 3 times. Milk left?**
`40 x (1 - 8/40)^3 = 40 x (4/5)^3 = 40 x 0.512 =` **20.48 L.** *(Verified.)*

### 📝 Method 2 - markup and discount

**Goods marked up 40% and sold at 25% discount. Profit%?** `1.40 x 0.75 = 1.05` -> **5% profit.**
*(Verified.)*

### 📝 Method 3 - equated ages

**A father is thrice his son's age now; in 12 years he will be twice.** Let son `= s`, father `= 3s`.
`3s + 12 = 2(s + 12)` -> `s = 12`, father `= 36`. **Son 12, father 36.** *(Verified.)*

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Multiplier chaining** for any sequence of percentage changes. *Safe always.*
- ⚠️ **Fraction-power formula** for replacement. *Safe only when the same quantity is removed and
  replaced each round.*
- ⚠️ **`r/(1+r)` shortcut** for the consumption cut that holds expenditure fixed. *Safe when price and
  quantity are the only variables.*
- ⚠️ **Smart-number base (take 100 or the LCM)** for percentage/ratio word problems. *Safe when the
  answer is a ratio or a percentage, not an absolute value.*

## 5. Boundary cases

- ⚠️ Markup and discount must use the **correct base** (markup on CP, discount on MP); mixing bases is
  the most common error.
- ⚠️ Replacement formula fails if the removed amount **changes** between rounds.
- ⚠️ A weighted average of two mixtures uses the **volumes taken**, not a plain average, unless the
  volumes are equal.

## 6. Advanced traps

- ❌ Cutting consumption by `r%` (not `r/(1+r)`) to offset an `r%` price rise. -> Use `r/(1+r)`.
- ❌ Applying discount on cost price. -> Discount is on marked price.
- ❌ Averaging two mixture ratios directly. -> Weight by volume.
- ❌ In ages, writing "+12" on one side only. -> Add the time to **both** ages.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Wrong base for %/discount | C | Label CP/MP/SP before writing a multiplier. |
| Adding percentages | A | Always chain multipliers. |
| Age-equation sign slips | A | Tabulate ages at each time point. |
| Mixture weighting | X | Use volume x fraction, then divide by total volume. |

## 8. Advanced drill (with full solutions)

1. To keep expenditure unchanged after a 25% price rise, by what % must consumption fall?
2. Vessel 1 has milk : water = 3 : 1; vessel 2 has 5 : 2. Equal volumes are mixed. Find the new milk :
   water ratio.
3. From 40 L milk, 8 L is drawn off and replaced with water three times. How much milk remains?
4. An item marked up 40% is sold at 25% discount. Find the profit percentage.
5. A father is thrice as old as his son now and twice as old in 12 years. Find their present ages.

**Solutions.**

1. **20%.** `25/(100 + 25) = 25/125 = 20%`. *(Verified.)*
2. **41 : 15.** Milk fraction `= (3/4 + 5/7)/2 = 41/56`; water `= 15/56`. *(Verified.)*
3. **20.48 L.** `40 x (4/5)^3 = 20.48`. *(Verified.)*
4. **5% profit.** `1.4 x 0.75 = 1.05`. *(Verified.)*
5. **Son 12, father 36.** From `3s + 12 = 2(s + 12)`. *(Verified.)*

## 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Pure commercial arithmetic is a **lighter** slice of CSAT than candidates fear (a small share of
  each paper), but it is **high-yield** because the methods are fast and the traps are predictable.
- ⚠️ Recurring shapes: **successive percentage change**, **partnership/profit sharing**,
  **mixtures/alligation** (including replacement), and **ages**.
- ⚠️ The paper rewards **multiplier fluency**; the classic mistake it punishes is adding percentages.

## 10. Study links

- ✅ [Foundation companion](../basic/03_Arithmetic-and-Commercial-Math.md).
- ✅ [Rates, Motion, Time and Geometry](./04_Rates-Motion-Time-and-Geometry.md) - averages/ratios extend to average speed and
  work rates.
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - ages/mixtures are equation setups.
