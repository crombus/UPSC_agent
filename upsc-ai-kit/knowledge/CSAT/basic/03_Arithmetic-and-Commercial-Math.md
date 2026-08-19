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
| ✅ **Percentage change** | For a change of `p%`, `New = Old x (1 ± p/100)`. Successive changes multiply, they do **not** add. |
| ✅ **Percentage point** | A change **between two percentages**: `50% - 40% = 10 percentage points`, which is a **25% relative** rise. Never write "10%" for it. |
| ✅ **Ratio split** | Divide total by the sum of ratio parts to get one "part". |
| ✅ **Average** | `Average = Sum / Count`; `Sum = Average x Count`. |
| ✅ **Weighted average** | `(w1 a1 + w2 a2 + ...) / (w1 + w2 + ...)`. Equals the plain mean **only** when all weights are equal. |
| ✅ **Alligation** | For `a < m < b`, quantity at value `a` : quantity at value `b` is `(b - m) : (m - a)`. At an endpoint, one component has zero quantity; outside `[a,b]`, the target is infeasible. |
| ✅ **Profit / loss** | `SP = CP x (1 ± profit%/loss%)`; profit% is on **CP**. |
| ✅ **Simple interest** | `SI = P x R x T / 100` - interest on the **original principal** every period, so it grows **linearly**. |
| ✅ **Compound interest** | `A = P x (1 + R/100)^T`; `CI = A - P` - interest on the **running amount**, so it grows **geometrically**. |
| ✅ **Non-annual compounding** | For `k` compoundings a year use `A = P x (1 + R/(100k))^(kT)` - halve the rate and double the periods for half-yearly, quarter and quadruple for quarterly. |
| ✅ **Partnership** | Profit share ∝ `capital x time`. |

> **Routing boundary:** conditional probability is owned by Topic 06. This file uses percentages
> and ratios that may be prerequisites, but does not treat a probability demand as Commercial Math.

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

## 5. Core commercial workflows

### 5.1 Direct and inverse variation

If `y ∝ x`, then `y/x` is constant: doubling `x` doubles `y`. If `y ∝ 1/x`, then `xy` is
constant: doubling `x` halves `y`. First name what is held fixed; do not call every changing pair
“inverse.”

**Worked example.** 8 workers make 240 units in the same time at the same rate. 12 workers make
`240 x 12/8 =` **360 units** (direct variation). If 8 identical workers finish a job in 15 days,
12 workers finish in `8x15/12 =` **10 days** (inverse variation, with equal productivity).

### 5.2 Marked-price and discount workflow

```text
CP --(markup, if given)--> MP --(each discount multiplier)--> SP
profit / loss percentage = (SP - CP) / CP x 100
```

**Worked example.** Cost price is 500, markup 20%, then discounts 10% and 5%. `MP=500x1.20=600`;
`SP=600x0.90x0.95=513`. Profit `=13`, hence profit percentage **2.6%** on CP. Do not subtract
discounts from CP or add successive discounts.

### 5.3 Correcting an average

If one recorded value `r` should have been `c` in a group of `n`, corrected average
`= old average + (c-r)/n`. For several errors, add every `(correct-recorded)` difference to the old
sum first.

**Worked example.** The average of 20 marks is recorded as 48 after 35 was entered instead of 53.
Correct average `=48+(53-35)/20 =` **48.9**.

### 5.4 Compound interest with a withdrawal or instalment

For a deposit, move chronologically: compound the current balance for one period, then add or
subtract the cash flow at the stated time. The usual `P(1+r)^T` formula applies only when no
intermediate cash flow changes principal.

**Worked example.** Deposit 10,000 at 10% compounded annually; withdraw 1,100 at the end of year 1.
After year 1: `11,000-1,100=9,900`; after year 2: `9,900x1.10 =` **10,890**. A withdrawal at the
*beginning* of a year would be subtracted before that year’s compounding.

## 6. Original solved examples

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

## 7. Must-Know facts

- ✅ `1/2 = 50%`, `1/3 ≈ 33.3%`, `1/4 = 25%`, `1/8 = 12.5%`, `1/20 = 5%` - memorise these for speed.
- ✅ Profit% and loss% are always on **cost price**.
- ✅ For 2 years, `CI - SI = P x (R/100)^2` (a fast check; 2 years only, annual compounding).
- ✅ **SI is linear in time, CI is geometric** - so CI and SI are equal after **one** period and CI is
  larger after that (for a positive rate).
- ✅ A **percentage point** is a gap between percentages; a **percent change** is relative to a base.
- ✅ In partnership, equal-time investors share in the **capital ratio**; equal-capital investors
  share in the **time ratio**.

## 8. Common traps

- ❌ Adding successive percentages (10% + 10% = 20%). -> Multiply multipliers (`1.1 x 1.1 = 1.21`).
- ❌ Taking profit% on selling price. -> It is on **cost price**.
- ❌ Assuming +x% then -x% returns to the start. -> It gives a net `x^2/100 %` fall.
- ❌ Saying "the rate rose 10%" when it rose from 40% to 50%. -> That is **10 percentage points**
  (and 25% relatively).
- ❌ Averaging two group averages by a plain mean when the **group sizes differ**. -> Weight by size.
- ❌ Averaging two speeds/prices by a plain mean when the **weights differ**. -> Weight by quantity.
- ❌ Reading a discount off cost price. -> Discount is off **marked price**.
- ❌ Using the annual CI formula when compounding is half-yearly/quarterly. -> Adjust `R` and `T`.

## 9. Quick checks

- ✅ Can you turn "increases by 25%" into "x1.25" instantly?
- ✅ Given a ratio and a total, can you get one part in one division?
- ✅ Can you write alligation ratio without a diagram?
- ✅ Can you say, for one stated change, both its percentage-point and its percent value?

## 10. Mini-drill (with answers and explanations)

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

## 11. Timed mixed practice, diagnosis and retry gate

**Set rule:** solve in **12 minutes** without a calculator. For every answer, label the governing
relationship first: `P` percentage multiplier, `V` variation, `W` weighted average, `M` marked-price
chain, `C` cash-flow compounding, or `R` ratio.

1. Price rises by 40%. By what percentage must consumption fall to keep expenditure unchanged?  
2. If 15 machines make 900 parts in 6 hours, how many parts do 10 identical machines make in 9 hours?  
3. A 25-member class has recorded average 60. One score 42 was actually 57. Find the corrected average.  
4. CP is 800; markup is 25%, followed by discounts 10% and 20%. Find profit/loss percentage.  
5. A deposit of 20,000 earns 5% annual CI. At the end of year 1, 1,000 is withdrawn. Find the balance
   at the end of year 2.  
6. Mix 20 kg at 30/kg and 30 kg at 45/kg. Find the mean price/kg.  
7. A:B capital ratio is 3:5; A invests 8 months and B 6 months. Divide profit 5,400.  
8. A pass rate rises from 48% to 60%. State the percentage-point and relative changes.

**Answers.** 1. `40/140 =` **28 4/7%** (`P`); 2. **900** (`V`, output ∝ machines x time);
3. `60+(57-42)/25 =` **60.6** (`W`); 4. `1.25x0.90x0.80=0.90`, **10% loss** (`M`);
5. `(20,000x1.05-1,000)x1.05 =` **21,000** (`C`); 6. `(600+1,350)/50 =` **39** (`W`);
7. time-weighted ratio `24:30=4:5`, shares **2,400 and 3,000** (`R`); 8. **12 percentage
points; 25% relative rise** (`P`).

| Miss pattern | Error code | Repair before retry |
|---|---|---|
| Added percentages or used the wrong base | **C** | Draw CP→MP→SP or write every multiplier. |
| Plain-averaged unequal groups / quantities | **W** | Rebuild totals as quantity × value. |
| Reversed direct and inverse variation | **V** | State the constant (`y/x` or `xy`) before numbers. |
| Compounded a withdrawn/deposited amount for the wrong period | **C** | Write a year-by-year balance line. |
| Accurate but too slow | **T** | Redo using fractions/smart numbers; park at the set ceiling. |

| Date / set | Score / time | P | V | W | M | C | R | T | Next repair |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |  |  |  |

**Gate:** score **7/8 within 12 minutes**, then **7/8 on a new mixed set** after any correction
before treating Advanced methods as optional enrichment. For full papers, use the Master Framework’s
qualifying-margin and negative-marking rules; never try to recover a weak Core score with blind
commercial-math attempts.

## 12. Study links

- ✅ [Advanced companion](../advanced/03_Arithmetic-and-Commercial-Math.md) - repeated replacement,
  markup-plus-discount, and equating-ages methods.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - ratio sense rests on factors.
- ✅ [Rates, Motion, Time and Geometry](./04_Rates-Motion-Time-and-Geometry.md) - averages and ratios extend to speed and work.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
## 2026 PYQ Integration

> **Status:** 2026 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2026.md`.
> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are **provisional**; no option or answer is recorded or inferred in this integration.

- **Year represented:** 2026
- **Paper(s):** CSAT
- **Routed question demands:** 7

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2026 | CSAT | 25 | Class-average correction | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 30 | Direct/inverse proportion | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 43 | Percentage savings change | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 58 | Company-worker ratio | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 65 | Alloy-mixture ratio | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 78 | Partnership capital-duration share | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2026 | CSAT | 79 | Repeated-replacement mixture | Objective question; provisional 2026 Set-A key present locally, answer not inferred | Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; key is provisional - no answer letter recorded or inferred here | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Class-average correction
- Direct/inverse proportion
- Percentage savings change
- Company-worker ratio
- Alloy-mixture ratio
- Partnership capital-duration share
- Repeated-replacement mixture

> This block integrates the 2026 examinable demand and paper metadata. It is kept separate from the 2018-2023 and 2024-2025 blocks and does not convert a provisionally-keyed, answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2026 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
## Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2024-2025.md`.
> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded or inferred in this integration.

- **Years represented:** 2024, 2025
- **Paper(s):** CSAT
- **Routed question demands:** 11

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2024 | CSAT | 16 | Mixture gain | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 25 | Partnership profit share | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 26 | Successive-percentage comparison | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 27 | Inverse-operation error | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 28 | Overlapping pass percentages | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 29 | Age ratio | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 36 | Proportional weights | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2024 | CSAT | 47 | Chained price ratios | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 10 | Successive-percentage cycle | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 17 | Fuel-cost distance adjustment | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |
| 2025 | CSAT | 78 | Average-balance relation | Objective question; official Set-A key available locally, answer not inferred | Key supplied locally (Set-A scan; recorded as supplied, not certified final); family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here | Practise this exact skill form under timed elimination; no answer is inferred here. |

### What this owner must now support

- Mixture gain
- Partnership profit share
- Successive-percentage comparison
- Inverse-operation error
- Overlapping pass percentages
- Age ratio
- Proportional weights
- Chained price ratios
- Successive-percentage cycle
- Fuel-cost distance adjustment
- Average-balance relation

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

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
| 2019 | CSAT | 19 | Unit price joint purchase | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
| 2022 | CSAT | 8 | Denomination combination validity | Objective question; official key unavailable locally | Stem verified against official scan; OCR artifact resolved; key unavailable locally | Practise this exact skill form under timed elimination; no answer is inferred here. |
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
