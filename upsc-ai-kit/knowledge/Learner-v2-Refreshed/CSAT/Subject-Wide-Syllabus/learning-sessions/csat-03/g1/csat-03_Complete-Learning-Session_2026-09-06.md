---
title: "Arithmetic-and-Commercial-Math — CSAT Learner-v2 Semantic Successor"
topic_key: csat-03
---

# Arithmetic-and-Commercial-Math — Complete CSAT Learning Session

**Identity:** `csat-03:learner-v2:g1`  
**Generation date:** 2026-09-06  
**Approval:** false  
**Official syllabus anchor:** Basic numeracy at Class X level.

| Source | SHA-256 at generation |
|---|---|
| `upsc-ai-kit\knowledge\CSAT\basic\03_Arithmetic-and-Commercial-Math.md` | `9283043c44d58ac8207c7b9ab39d5729bb80481950297680a22fd88c292a5d54` |
| `upsc-ai-kit\knowledge\CSAT\advanced\03_Arithmetic-and-Commercial-Math.md` | `0bdebe411b5f61ec646b126510ffe7bfb9c9fcf3f6dd322902b2b9e3bfe99cc8` |
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
| PANEL 01 — RATIO LANGUAGE                                                        |
| Convert comparisons into common units and scalable parts.                        |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 02 — PROPORTION AND VARIATION                                              |
| Distinguish direct from inverse change.                                          |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 03 — PERCENT FOUNDATION                                                    |
| Percent means per hundred; identify the base before operating.                   |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 04 — SUCCESSIVE CHANGE                                                     |
| Multiply factors; do not add percentages blindly.                                |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 05 — AVERAGE                                                               |
| Use total divided by count and preserve group weights.                           |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 06 — PROFIT, LOSS AND DISCOUNT                                             |
| Keep CP, SP and MP bases distinct.                                               |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 07 — INTEREST                                                              |
| Derive SI from principal-rate-time and CI from repeated growth.                  |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 08 — MIXTURES                                                              |
| Use conservation of quantity or alligation with validity checks.                 |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 09 — PARTNERSHIP                                                           |
| Profit share follows capital multiplied by time.                                 |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 10 — AGES                                                                  |
| Translate one timeline consistently.                                             |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 11 — ESTIMATION AND OPTIONS                                                |
| Use smart numbers only when ratios remain invariant.                             |
+----------------------------------------------------------------------------------+
        |
        v
+----------------------------------------------------------------------------------+
| PANEL 12 — VERIFICATION                                                          |
| Reverse the change, recompute totals and inspect the percentage base.            |
+----------------------------------------------------------------------------------+
```

### Canonical Basic owner

### Arithmetic and Commercial Math - MUST-DO

> **Subject:** CSAT | **Tier:** Must-Do (foundation) | **Family:** Basic numeracy.
> **Core skill:** ratio, percentage, average, mixture, profit-loss, interest, partnership and ages -
> solved by **scaling and multipliers**, not long working.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Advanced Drill](../advanced/03_Arithmetic-and-Commercial-Math.md).*

---

### 1. Visual foundation

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

### 2. Essential formulas

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

### 3. Method

1. Name the quantity asked and the relation type (ratio / percent / average / mixture / commercial).
2. Convert every change to a **multiplier** or a **part**.
3. Combine (multiply multipliers; add parts), then scale to the total.
4. Verify by **magnitude** (is a discount answer smaller than the price? is a share ≤ total?).

### 4. Conditions to respect

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

### 5. Core commercial workflows

#### 5.1 Direct and inverse variation

If `y ∝ x`, then `y/x` is constant: doubling `x` doubles `y`. If `y ∝ 1/x`, then `xy` is
constant: doubling `x` halves `y`. First name what is held fixed; do not call every changing pair
“inverse.”

**Worked example.** 8 workers make 240 units in the same time at the same rate. 12 workers make
`240 x 12/8 =` **360 units** (direct variation). If 8 identical workers finish a job in 15 days,
12 workers finish in `8x15/12 =` **10 days** (inverse variation, with equal productivity).

#### 5.2 Marked-price and discount workflow

```text
CP --(markup, if given)--> MP --(each discount multiplier)--> SP
profit / loss percentage = (SP - CP) / CP x 100
```

**Worked example.** Cost price is 500, markup 20%, then discounts 10% and 5%. `MP=500x1.20=600`;
`SP=600x0.90x0.95=513`. Profit `=13`, hence profit percentage **2.6%** on CP. Do not subtract
discounts from CP or add successive discounts.

#### 5.3 Correcting an average

If one recorded value `r` should have been `c` in a group of `n`, corrected average
`= old average + (c-r)/n`. For several errors, add every `(correct-recorded)` difference to the old
sum first.

**Worked example.** The average of 20 marks is recorded as 48 after 35 was entered instead of 53.
Correct average `=48+(53-35)/20 =` **48.9**.

#### 5.4 Compound interest with a withdrawal or instalment

For a deposit, move chronologically: compound the current balance for one period, then add or
subtract the cash flow at the stated time. The usual `P(1+r)^T` formula applies only when no
intermediate cash flow changes principal.

**Worked example.** Deposit 10,000 at 10% compounded annually; withdraw 1,100 at the end of year 1.
After year 1: `11,000-1,100=9,900`; after year 2: `9,900x1.10 =` **10,890**. A withdrawal at the
*beginning* of a year would be subtracted before that year’s compounding.

### 6. Original solved examples

#### 📝 Example A (ratio)

**Divide 3300 among A, B, C in the ratio 2 : 3 : 6.** Parts = 11; one part = `3300/11 = 300`. Shares =
**600, 900, 1800.** *(Verified.)*

#### 📝 Example B (successive percentage)

**A population rises 10% then falls 10%. Net change?** `1.10 x 0.90 = 0.99` -> **1% decrease.**
*(Verified.)*

#### 📝 Example C (average)

**The average of 5 numbers is 27. One number, 35, is removed. New average of the 4?** Sum `= 135`;
new sum `= 100`; average `= 100/4 =` **25.** *(Verified.)*

#### 📝 Example D (alligation)

**In what ratio mix rice at 30 and 40 per kg to get 34 per kg?** `(40 - 34) : (34 - 30) = 6 : 4 =`
**3 : 2.** *(Verified.)*

#### 📝 Example E (compound interest)

**CI on 10000 at 10% for 2 years.** `A = 10000 x 1.1^2 = 12100`; `CI = 12100 - 10000 =` **2100.**
*(Verified.)* Compare **SI** on the same terms: `10000 x 10 x 2 / 100 =` **2000.** The `100`
difference is exactly `P (R/100)^2 = 10000 x 0.01`. *(Verified.)*

#### 📝 Example F (weighted average vs plain average)

**A class has 30 boys averaging 62 marks and 20 girls averaging 72.** Class average
`= (30 x 62 + 20 x 72) / 50 = (1860 + 1440)/50 = 3300/50 =` **66.**
The plain mean of 62 and 72 is **67** - wrong, because the groups are not the same size.
*(Verified.)*

#### 📝 Example G (percentage point vs percent change)

**A district's literacy rate rises from 40% to 50%.** The rise is **10 percentage points**. As a
**relative** change it is `(50 - 40)/40 =` **25%**. Both are correct answers to **different**
questions - and the options will usually contain both. *(Verified.)*

### 7. Must-Know facts

- ✅ `1/2 = 50%`, `1/3 ≈ 33.3%`, `1/4 = 25%`, `1/8 = 12.5%`, `1/20 = 5%` - memorise these for speed.
- ✅ Profit% and loss% are always on **cost price**.
- ✅ For 2 years, `CI - SI = P x (R/100)^2` (a fast check; 2 years only, annual compounding).
- ✅ **SI is linear in time, CI is geometric** - so CI and SI are equal after **one** period and CI is
  larger after that (for a positive rate).
- ✅ A **percentage point** is a gap between percentages; a **percent change** is relative to a base.
- ✅ In partnership, equal-time investors share in the **capital ratio**; equal-capital investors
  share in the **time ratio**.

### 8. Common traps

- ❌ Adding successive percentages (10% + 10% = 20%). -> Multiply multipliers (`1.1 x 1.1 = 1.21`).
- ❌ Taking profit% on selling price. -> It is on **cost price**.
- ❌ Assuming +x% then -x% returns to the start. -> It gives a net `x^2/100 %` fall.
- ❌ Saying "the rate rose 10%" when it rose from 40% to 50%. -> That is **10 percentage points**
  (and 25% relatively).
- ❌ Averaging two group averages by a plain mean when the **group sizes differ**. -> Weight by size.
- ❌ Averaging two speeds/prices by a plain mean when the **weights differ**. -> Weight by quantity.
- ❌ Reading a discount off cost price. -> Discount is off **marked price**.
- ❌ Using the annual CI formula when compounding is half-yearly/quarterly. -> Adjust `R` and `T`.

### 9. Quick checks

- ✅ Can you turn "increases by 25%" into "x1.25" instantly?
- ✅ Given a ratio and a total, can you get one part in one division?
- ✅ Can you write alligation ratio without a diagram?
- ✅ Can you say, for one stated change, both its percentage-point and its percent value?

### 10. Mini-drill (with answers and explanations)

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

### 11. Timed mixed practice, diagnosis and retry gate

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

### 12. Study links

- ✅ [Advanced companion](../advanced/03_Arithmetic-and-Commercial-Math.md) - repeated replacement,
  markup-plus-discount, and equating-ages methods.
- ✅ [Number Systems and Number Sense](./02_Number-Systems-and-Number-Sense.md) - ratio sense rests on factors.
- ✅ [Rates, Motion, Time and Geometry](./04_Rates-Motion-Time-and-Geometry.md) - averages and ratios extend to speed and work.
<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->
### 2026 PYQ Integration

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

#### What this owner must now support

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
### Recent PYQ Integration (2024-2025)

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

#### What this owner must now support

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
### Historical PYQ Integration (2018-2023)

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

#### What this owner must now support

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

---

### Semantic-completeness closure — 2026-09-06

#### Literal syllabus and canonical ownership

- **Literal clause:** Basic numeracy at Class X level.
- **Canonical scope:** Owns ratio, proportion, variation, percentages, averages, mixtures, profit-loss-discount, simple and compound interest, partnership and ages.
- **Cross-topic boundary:** Pure number properties belong to Topic 02; time-work and motion rates to Topic 04; equation sufficiency to Topic 05.

#### Complete learner route

1. **Ratio language:** Convert comparisons into common units and scalable parts.
2. **Proportion and variation:** Distinguish direct from inverse change.
3. **Percent foundation:** Percent means per hundred; identify the base before operating.
4. **Successive change:** Multiply factors; do not add percentages blindly.
5. **Average:** Use total divided by count and preserve group weights.
6. **Profit, loss and discount:** Keep CP, SP and MP bases distinct.
7. **Interest:** Derive SI from principal-rate-time and CI from repeated growth.
8. **Mixtures:** Use conservation of quantity or alligation with validity checks.
9. **Partnership:** Profit share follows capital multiplied by time.
10. **Ages:** Translate one timeline consistently.
11. **Estimation and options:** Use smart numbers only when ratios remain invariant.
12. **Verification:** Reverse the change, recompute totals and inspect the percentage base.

#### Verification and hostile-query gate

Every formula is derived from part/whole, multiplier, weighted-total or principal-time logic. Generated answers are recomputed with exact fractions before formatting.

The hostile absence search explicitly tested these families and close-option terms:
**ratio; percentage; weighted average; profit; discount; simple interest; compound interest; alligation**. A shortcut is usable only when its stated condition survives; otherwise return to
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

### Q1. Practice variant 1: What is 15% of 200?

A. 30
B. 31
C. 29
D. 32

**Correct answer: A.** Percent means per hundred: base x rate/100.


### Q2. Practice variant 1: A value of 1000 rises by 10% and then falls by 5%. What is the final value?

A. 1046
B. 1045
C. 1044
D. 1047

**Correct answer: B.** Successive changes multiply growth factors; they do not simply cancel.


### Q3. Practice variant 1: Groups of 20 and 30 have averages 40 and 60. What is their combined average, rounded to the nearest integer?

A. 53
B. 51
C. 52
D. 54

**Correct answer: C.** Combine totals, then divide by the combined count.


### Q4. Practice variant 1: An article costs Rs 500 and is sold at 20% profit. What is the selling price?

A. 601
B. 599
C. 602
D. 600

**Correct answer: D.** Profit percent uses cost price as the base.


### Q5. Practice variant 1: Find the simple interest on Rs 1000 at 5% per annum for 2 years.

A. 100
B. 101
C. 99
D. 102

**Correct answer: A.** SI = PRT/100, derived by adding the same annual interest on the original principal.


### Q6. Practice variant 1: Find the compound interest on Rs 1000 at 10% per annum for 2 years, compounded annually.

A. 211
B. 210
C. 209
D. 212

**Correct answer: B.** Amount = P(1+r/100)^n; subtract principal for compound interest.


### Q7. Practice variant 1: Rs 360 is divided in the ratio 2:3. What is the first share?

A. 145
B. 143
C. 144
D. 146

**Correct answer: C.** One share equals total divided by total ratio-parts.


### Q8. Practice variant 1: A invests Rs 1000 for 12 months and B invests Rs 1500 for 8 months. Out of profit Rs 1000, what is A's share, rounded to the nearest rupee?

A. 501
B. 499
C. 502
D. 500

**Correct answer: D.** Partnership shares are proportional to capital multiplied by time.


### Q9. Practice variant 2: What is 20% of 220?

A. 44
B. 45
C. 43
D. 46

**Correct answer: A.** Percent means per hundred: base x rate/100.


### Q10. Practice variant 2: A value of 1000 rises by 11% and then falls by 6%. What is the final value?

A. 1044
B. 1043
C. 1042
D. 1045

**Correct answer: B.** Successive changes multiply growth factors; they do not simply cancel.


### Q11. Practice variant 2: Groups of 21 and 31 have averages 41 and 61. What is their combined average, rounded to the nearest integer?

A. 54
B. 52
C. 53
D. 55

**Correct answer: C.** Combine totals, then divide by the combined count.


### Q12. Practice variant 2: An article costs Rs 550 and is sold at 20% profit. What is the selling price?

A. 661
B. 659
C. 662
D. 660

**Correct answer: D.** Profit percent uses cost price as the base.


### Q13. Practice variant 2: Find the simple interest on Rs 1200 at 6% per annum for 2 years.

A. 144
B. 145
C. 143
D. 146

**Correct answer: A.** SI = PRT/100, derived by adding the same annual interest on the original principal.


### Q14. Practice variant 2: Find the compound interest on Rs 1000 at 15% per annum for 2 years, compounded annually.

A. 323
B. 322
C. 321
D. 324

**Correct answer: B.** Amount = P(1+r/100)^n; subtract principal for compound interest.


### Q15. Practice variant 2: Rs 420 is divided in the ratio 3:3. What is the first share?

A. 211
B. 209
C. 210
D. 212

**Correct answer: C.** One share equals total divided by total ratio-parts.


### Q16. Practice variant 2: A invests Rs 1000 for 12 months and B invests Rs 1500 for 9 months. Out of profit Rs 1000, what is A's share, rounded to the nearest rupee?

A. 472
B. 470
C. 473
D. 471

**Correct answer: D.** Partnership shares are proportional to capital multiplied by time.


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
| 2024 | 16 | Mixture gain | A (supplied) | Conserve the amount of the active component. |
| 2024 | 25 | Partnership profit share | A (supplied) | Compare capital multiplied by time. |
| 2024 | 26 | Successive-percentage comparison | B (supplied) | Fix the base and multiply successive change factors. |
| 2024 | 27 | Inverse-operation error | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 28 | Overlapping pass percentages | B (supplied) | Fix the base and multiply successive change factors. |
| 2024 | 29 | Age ratio | A (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 36 | Proportional weights | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2024 | 47 | Chained price ratios | D (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 10 | Successive-percentage cycle | A (supplied) | Fix the base and multiply successive change factors. |
| 2025 | 17 | Fuel-cost distance adjustment | B (supplied) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2025 | 78 | Average-balance relation | A (supplied) | Rebuild the total before and after the change. |
| 2026 | 25 | Class-average correction | B (provisional) | Rebuild the total before and after the change. |
| 2026 | 30 | Direct/inverse proportion | B (provisional) | Classify the dominant mechanism, represent the givens, solve minimally and verify independently. |
| 2026 | 43 | Percentage savings change | B (provisional) | Fix the base and multiply successive change factors. |
| 2026 | 58 | Company-worker ratio | B (provisional) | Add rates and invert the net rate. |
| 2026 | 65 | Alloy-mixture ratio | A (provisional) | Conserve the amount of the active component. |
| 2026 | 78 | Partnership capital-duration share | A (provisional) | Compare capital multiplied by time. |
| 2026 | 79 | Repeated-replacement mixture | B (provisional) | Conserve the amount of the active component. |

> The table is a non-verbatim routing audit. It records the locally checked Set-A key letter and a
> valid solving route, but does not pretend that UPSC publishes model solutions. The separate
> workbook supplies original solved equivalents for every mechanism.

### Timed mixed transfer

### Q33. Practice variant 5: What is 20% of 280?

A. 56
B. 57
C. 55
D. 58

**Correct answer: A.** Percent means per hundred: base x rate/100.


### Q34. Practice variant 5: A value of 1000 rises by 14% and then falls by 9%. What is the final value?

A. 1038
B. 1037
C. 1036
D. 1039

**Correct answer: B.** Successive changes multiply growth factors; they do not simply cancel.


### Q35. Practice variant 5: Groups of 24 and 34 have averages 44 and 64. What is their combined average, rounded to the nearest integer?

A. 57
B. 55
C. 56
D. 58

**Correct answer: C.** Combine totals, then divide by the combined count.


### Q36. Practice variant 5: An article costs Rs 700 and is sold at 20% profit. What is the selling price?

A. 841
B. 839
C. 842
D. 840

**Correct answer: D.** Profit percent uses cost price as the base.


### Q37. Practice variant 5: Find the simple interest on Rs 1800 at 9% per annum for 2 years.

A. 324
B. 325
C. 323
D. 326

**Correct answer: A.** SI = PRT/100, derived by adding the same annual interest on the original principal.


### Q38. Practice variant 5: Find the compound interest on Rs 1000 at 10% per annum for 2 years, compounded annually.

A. 211
B. 210
C. 209
D. 212

**Correct answer: B.** Amount = P(1+r/100)^n; subtract principal for compound interest.


### Q39. Practice variant 5: Rs 600 is divided in the ratio 3:3. What is the first share?

A. 301
B. 299
C. 300
D. 302

**Correct answer: C.** One share equals total divided by total ratio-parts.


### Q40. Practice variant 5: A invests Rs 1000 for 12 months and B invests Rs 1500 for 9 months. Out of profit Rs 1000, what is A's share, rounded to the nearest rupee?

A. 472
B. 470
C. 473
D. 471

**Correct answer: D.** Partnership shares are proportional to capital multiplied by time.


## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Arithmetic and Commercial Math - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Basic numeracy.
> **Core skill:** multi-step commercial arithmetic - repeated replacement, markup-and-discount chains,
> equated-ages, expenditure-consumption trade-offs, and two-vessel mixtures.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: [Foundation](../basic/03_Arithmetic-and-Commercial-Math.md).*

---

### 1. Architecture

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

### 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Repeated replacement** | After removing and replacing fraction each time, remaining pure part `= initial x (1 - removed/total)^n`. | The vessel is thoroughly mixed, the same volume is removed and replaced each round, and total volume is restored after every round. |
| ✅ **Markup-then-discount** | Net multiplier `= (1 + markup) x (1 - discount)`; profit% `= (net - 1) x 100`. | Markup on CP, discount on MP. |
| ✅ **Expenditure = price x quantity** | To hold expenditure constant when price rises by r, cut quantity by `r/(1+r)`. | Price and quantity vary inversely. |
| ✅ **Ages** | Set present ages as variables; write one equation per time reference. | Keep "years later/ago" consistent on both sides. |
| ✅ **Two-vessel mixture** | Combined fraction = weighted average of the two fractions by volume. | Weight by the volume actually taken. |

### 3. Harder methods (worked)

#### 📝 Method 1 - repeated replacement

**From 40 L of milk, 8 L is removed and replaced with water; repeated 3 times. Milk left?**
`40 x (1 - 8/40)^3 = 40 x (4/5)^3 = 40 x 0.512 =` **20.48 L.** *(Verified.)*

#### 📝 Method 2 - markup and discount

**Goods marked up 40% and sold at 25% discount. Profit%?** `1.40 x 0.75 = 1.05` -> **5% profit.**
*(Verified.)*

#### 📝 Method 3 - equated ages

**A father is thrice his son's age now; in 12 years he will be twice.** Let son `= s`, father `= 3s`.
`3s + 12 = 2(s + 12)` -> `s = 12`, father `= 36`. **Son 12, father 36.** *(Verified.)*

#### 📝 Method 4 - three different "percentages" from one situation

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

### 4. Time-saving techniques (safe conditions)

- ⚠️ **Multiplier chaining** for any sequence of percentage changes. *Safe always.*
- ⚠️ **Fraction-power formula** for replacement. *Safe only when the vessel is mixed before every
  draw, the same quantity is removed and replaced, and the original total volume is restored each
  round.*
- ⚠️ **`r/(1+r)` shortcut** for the consumption cut that holds expenditure fixed. *Safe when price and
  quantity are the only variables.*
- ⚠️ **Smart-number base (take 100 or the LCM)** for percentage/ratio word problems. *Safe when the
  answer is a ratio or a percentage, not an absolute value.*

### 5. Boundary cases

- ⚠️ Markup and discount must use the **correct base** (markup on CP, discount on MP); mixing bases is
  the most common error.
- ⚠️ Replacement formula fails if the removed amount changes, the vessel is not mixed before a draw,
  or the total volume is not restored between rounds.
- ⚠️ A weighted average of two mixtures uses the **volumes taken**, not a plain average, unless the
  volumes are equal.
- ⚠️ A percentage applied to a **moving base** yields several different true answers - name the base
  before computing (Method 4).
- ⚠️ Successive discounts multiply; two discounts of `d1` and `d2` are equivalent to a single
  `d1 + d2 - d1 d2/100`, never `d1 + d2`.

### 6. Advanced traps

- ❌ Cutting consumption by `r%` (not `r/(1+r)`) to offset an `r%` price rise. -> Use `r/(1+r)`.
- ❌ Applying discount on cost price. -> Discount is on marked price.
- ❌ Adding two successive discounts. -> Multiply the multipliers.
- ❌ Reporting a **percent change** when the stem asked for **percentage points**, or the reverse.
  -> Underline the noun before computing.
- ❌ Averaging two mixture ratios directly. -> Weight by volume.
- ❌ Averaging two group averages when the groups differ in size. -> Weight by group size.
- ❌ In ages, writing "+12" on one side only. -> Add the time to **both** ages.

### 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Wrong base for %/discount | C | Label CP/MP/SP before writing a multiplier. |
| Adding percentages | A | Always chain multipliers. |
| Percentage point vs percent | R | Underline "rate" or "count" in the stem first. |
| Age-equation sign slips | A | Tabulate ages at each time point. |
| Mixture weighting | X | Use volume x fraction, then divide by total volume. |

### 8. Advanced drill (with full solutions)

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

### 9. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ Pure commercial arithmetic is a **lighter** slice of CSAT than candidates fear (a small share of
  each paper), but it is **high-yield** because the methods are fast and the traps are predictable.
- ⚠️ Recurring shapes: **successive percentage change**, **partnership/profit sharing**,
  **mixtures/alligation** (including replacement), and **ages**.
- ⚠️ The paper rewards **multiplier fluency**; the classic mistake it punishes is adding percentages.

### 10. Study links

- ✅ [Foundation companion](../basic/03_Arithmetic-and-Commercial-Math.md).
- ✅ [Rates, Motion, Time and Geometry](./04_Rates-Motion-Time-and-Geometry.md) - averages/ratios extend to average speed and
  work rates.
- ✅ [Algebra, Inequalities and Data Sufficiency](./05_Algebra-Inequalities-and-Data-Sufficiency.md) - ages/mixtures are equation setups.

> **Ownership note:** conditional-probability entries in an appended historical routing ledger are
> owned by Topic 06, not by this Arithmetic companion. This file may supply percentage/fraction
> prerequisites but must not be used as a probability substitute.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
### Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-CSAT-2018-2023.md`.
> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held locally; no option or answer has been inferred.

- **Years represented:** 2018, 2019, 2020, 2021, 2022, 2023
- **Paper(s):** CSAT
- **Routed question demands:** 40

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2018 | CSAT | 39 | Conditional probability | Objective question; official key unavailable locally | Cross-owner reference; key unavailable locally | **Route to Topic 06** for method and timed practice; no Topic 03 coverage claim is made here. |
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

#### What this owner must now support

- Conditional probability — routed to Topic 06 (cross-owner reference)
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

## CONSOLIDATED REGISTER NOTES

### Complete revision spine

- **Ratio language:** Convert comparisons into common units and scalable parts.
- **Proportion and variation:** Distinguish direct from inverse change.
- **Percent foundation:** Percent means per hundred; identify the base before operating.
- **Successive change:** Multiply factors; do not add percentages blindly.
- **Average:** Use total divided by count and preserve group weights.
- **Profit, loss and discount:** Keep CP, SP and MP bases distinct.
- **Interest:** Derive SI from principal-rate-time and CI from repeated growth.
- **Mixtures:** Use conservation of quantity or alligation with validity checks.
- **Partnership:** Profit share follows capital multiplied by time.
- **Ages:** Translate one timeline consistently.
- **Estimation and options:** Use smart numbers only when ratios remain invariant.
- **Verification:** Reverse the change, recompute totals and inspect the percentage base.

### Ownership and close-option firewall

- **Own here:** Owns ratio, proportion, variation, percentages, averages, mixtures, profit-loss-discount, simple and compound interest, partnership and ages.
- **Do not duplicate:** Pure number properties belong to Topic 02; time-work and motion rates to Topic 04; equation sufficiency to Topic 05.
- **Verification:** Every formula is derived from part/whole, multiplier, weighted-total or principal-time logic. Generated answers are recomputed with exact fractions before formatting.

### Timed answer route

`CLASSIFY → EXTRACT → REPRESENT → EXECUTE → VERIFY → DECIDE`

- Use estimation or option elimination only after preserving the governing condition.
- A blank costs zero; a rushed unsupported answer also consumes time and may attract negative marks.
- For every error, record concept/application/calculation/reading/passage/time/guess, repair the
  owner, and retry a new item rather than memorising the old option.

