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

### 📝 Method 4 - three different "percentages" from one situation

⚠️ When a **rate** applied to a **changing base** moves, there are **three** true percentage answers.
The options will contain more than one of them.

**A scheme is approved by 30% of 2000 respondents in year 1 and by 36% of 2500 in year 2.**

| Question actually asked | Computation | Answer |
|---|---|---|
| Change in the **approval rate**, in percentage points | `36 - 30` | **6 percentage points** |
| **Percent change** in the approval rate | `(36 - 30)/30` | **20%** |
| **Percent change** in the **number** of approvers | `600 -> 900`, `(900 - 600)/600` | **50%** |

*(Verified: `0.30 x 2000 = 600`; `0.36 x 2500 = 900`.)*

- 🔑 **Escalation rule:** underline the noun the stem attaches "%" to - **rate** or **count** - before
  you compute anything. Then decide whether it wants a **gap** (percentage points) or a **ratio**
  (percent change).

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
- ⚠️ A percentage applied to a **moving base** yields several different true answers - name the base
  before computing (Method 4).
- ⚠️ Successive discounts multiply; two discounts of `d1` and `d2` are equivalent to a single
  `d1 + d2 - d1 d2/100`, never `d1 + d2`.

## 6. Advanced traps

- ❌ Cutting consumption by `r%` (not `r/(1+r)`) to offset an `r%` price rise. -> Use `r/(1+r)`.
- ❌ Applying discount on cost price. -> Discount is on marked price.
- ❌ Adding two successive discounts. -> Multiply the multipliers.
- ❌ Reporting a **percent change** when the stem asked for **percentage points**, or the reverse.
  -> Underline the noun before computing.
- ❌ Averaging two mixture ratios directly. -> Weight by volume.
- ❌ Averaging two group averages when the groups differ in size. -> Weight by group size.
- ❌ In ages, writing "+12" on one side only. -> Add the time to **both** ages.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Wrong base for %/discount | C | Label CP/MP/SP before writing a multiplier. |
| Adding percentages | A | Always chain multipliers. |
| Percentage point vs percent | R | Underline "rate" or "count" in the stem first. |
| Age-equation sign slips | A | Tabulate ages at each time point. |
| Mixture weighting | X | Use volume x fraction, then divide by total volume. |

## 8. Advanced drill (with full solutions)

> ⚠️ These items are **new** - they do not repeat Methods 1-4 above or the Foundation file.

1. To keep expenditure unchanged after a 25% price rise, by what % must consumption fall?
2. Vessel 1 has milk : water = 3 : 1; vessel 2 has 5 : 2. Equal volumes are mixed. Find the new milk :
   water ratio.
3. A trader marks goods 25% above cost and then allows two successive discounts of 10% and 4%. Find
   the profit percentage.
4. From 40 L of pure milk, 10 L is drawn off and replaced with water; this is done **twice**. How much
   milk remains?
5. A class of 50 averages 60 marks. The 30 boys average 56. Find the girls' average.
6. An article sold at a 20% loss would have yielded a 10% gain had the selling price been 300 higher.
   Find the cost price.

**Solutions.**

1. **20%.** `25/(100 + 25) = 25/125 = 20%`. *(Verified.)* ⚠️ Not 25% - the base changed.
2. **41 : 15.** Milk fraction `= (3/4 + 5/7)/2 = 41/56`; water `= 15/56`. *(Verified.)*
3. **8% profit.** Chain the multipliers on **CP**: `1.25 x 0.90 x 0.96 = 1.08`. *(Verified.)*
   ⚠️ The two discounts are **both on the marked price**, so they multiply (`0.90 x 0.96 = 0.864`);
   adding them to "14%" would give a wrong 7.5%.
4. **22.5 L.** `40 x (1 - 10/40)^2 = 40 x (3/4)^2 = 40 x 9/16 = 22.5`. *(Verified.)* The formula holds
   because the **same** 10 L is removed each round.
5. **66.** Total `= 50 x 60 = 3000`; boys `= 30 x 56 = 1680`; girls' total `= 1320` over 20 girls
   `= 66`. *(Verified.)* ⚠️ The plain mean of 56 and 60 is meaningless here - the groups differ in size.
6. **1000.** `0.8C + 300 = 1.1C` -> `0.3C = 300` -> `C = 1000`. *(Verified: SP at 20% loss = 800;
   800 + 300 = 1100 = 1.1 x 1000.)*

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

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 40

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 39 | Conditional probability | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 41 | Pass-fail percentage marks | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 57 | Symmetric profit-loss point | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 68 | Capacity proportion share | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2018 | CSAT | 69 | Compound interest installment | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 11 | Percentage weight reduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 17 | Percentage shortfall amount | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 19 | Unit price joint purchase | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 34 | Percentage marks difference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 39 | Discount from quantity change | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 40 | Mean error correction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2019 | CSAT | 55 | Average group weight | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 18 | Weighted group average | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 39 | Age group average | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 40 | Loss-percentage cost recovery | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 47 | Successive-discount comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 55 | Percentage ratio constraint | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 57 | Ratio share difference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 59 | Class average invariance | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 68 | Successive mixture replacement | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 69 | Innings average difference | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 70 | Price-hike quantity reduction | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2020 | CSAT | 78 | Volume-mass unit conversion | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 7 | Linear fuel-price crossover | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 9 | Percentage group overlap | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 30 | Proportional marks threshold | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 37 | Class average transfer effect | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 53 | Equal-cost price ratio | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 54 | Percentage marks comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 55 | Conditional money allocation | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 70 | Ratio-share inequality | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2021 | CSAT | 78 | Successive percentage change | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 8 | Denomination combination validity | Objective question; official key unavailable locally | Partial OCR; manual verification needed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 20 | Successive percentage change | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 26 | Equal interval spacing | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 45 | Word problem total cost | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 64 | Election vote percentage | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 69 | Mixture proportion comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2022 | CSAT | 80 | Average weight combination | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2023 | CSAT | 44 | Compound interest frequency comparison | Objective question; official key unavailable locally | Routed; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Conditional probability
- Pass-fail percentage marks
- Symmetric profit-loss point
- Capacity proportion share
- Compound interest installment
- Percentage weight reduction
- Percentage shortfall amount
- Unit price joint purchase
- Percentage marks difference
- Discount from quantity change
- Mean error correction
- Average group weight
- Weighted group average
- Age group average
- Loss-percentage cost recovery
- Successive-discount comparison
- Percentage ratio constraint
- Ratio share difference
- Class average invariance
- Successive mixture replacement
- Innings average difference
- Price-hike quantity reduction
- Volume-mass unit conversion
- Linear fuel-price crossover
- Percentage group overlap
- Proportional marks threshold
- Class average transfer effect
- Equal-cost price ratio
- Percentage marks comparison
- Conditional money allocation
- Ratio-share inequality
- Successive percentage change
- Denomination combination validity
- Equal interval spacing
- Word problem total cost
- Election vote percentage
- Mixture proportion comparison
- Average weight combination
- Compound interest frequency comparison

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
