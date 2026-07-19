# CSAT - Master Framework

> **Purpose:** the single strategy layer to read before the six topic files. It fixes the attempt
> plan, the passage and quantitative workflows, the elimination and risk logic, an error taxonomy,
> a revision cycle, and the audited **2024-2026 PYQ trend table** that justifies the six-topic map.
> **Core question:** how do I reliably clear a **qualifying** aptitude paper with the fewest errors
> and the least wasted time?

---

## 1. The paper as a system

```text
   80 items, 200 marks, 2 hours              (from the printed instruction page)
            |
   2.5 marks correct  /  -5/6 wrong  /  0 blank
            |
     Goal = QUALIFY (minimum standard, commonly stated 33% = 66/200)
            |
   +--------+---------+---------+
   |        |         |         |
 SELECT   READ     COMPUTE   CONTROL
 easy Qs  slowly   carefully  the clock
 first    once     & verify   & risk
```

- ✅ **Facts (from the paper's own instruction page):** 80 items; 200 marks; two hours; equal marks
  (so 2.5 each); one-third penalty for a wrong answer (so `5/6 = 0.8333...`); multiple marks = wrong;
  blank = no penalty.
- ⚠️ **Qualifying standard:** commonly stated as 33% (66/200). **Verify against the current
  notification.** The strategy below assumes only that the bar is well below full marks - which is
  what makes **selective, high-accuracy attempting** the correct policy.

## 2. Attempt strategy (three-pass method)

CSAT rewards **selection**, not heroics. Use three passes over the 80 items.

| Pass | What you attempt | Mindset |
|---|---|---|
| **Pass 1 - Harvest** | Every item you can finish in about a minute with confidence: most passages, one-step arithmetic, direct coding/relations, easy series. | "Bank the certain marks first." |
| **Pass 2 - Grind** | Multi-step quant, data sufficiency, arrangements needing a grid, DI tables. | "Now spend the minutes I saved." |
| **Pass 3 - Decide** | Everything left: solve, **eliminate-then-guess**, or leave blank. | "Convert only positive-expectation guesses." |

> 🔑 **Rule:** never let one stubborn sum consume the time of three passage items. In a qualifying
> paper, **an item skipped costs 0; an item that eats 6 minutes costs the items you never reach.**

## 3. Passage workflow (Reading Comprehension - the largest family)

```text
READ QUESTION STEM FIRST (what is asked: idea / inference / assumption / tone?)
        |
READ PASSAGE ONCE, marking scope, contrast words, and the author's claim
        |
ANSWER FROM THE PASSAGE ONLY  -> ignore outside knowledge, however true
        |
ELIMINATE options that are: too broad, too narrow, unstated, or a distortion
        |
CHOOSE the option the passage can DEFEND, not the one that is merely true
```

- ⚠️ **Passage-only discipline** is the single highest-yield CSAT habit: the correct option is the
  one **entailed by the text**, not the factually correct real-world statement.
- ⚠️ Match the **question type** to a test (full method in
  [basic/01](basic/01_Reading-Comprehension.md)): central idea = "what does
  the whole passage support?"; inference = "what must also be true?"; assumption = "what does the
  argument silently rely on?"; tone = "what attitude does the wording reveal?".

## 4. Quantitative workflow

```text
CLASSIFY the family (number theory / arithmetic / rate-motion / algebra-DS)
        |
TRANSLATE words to one relation (rate x time, part/whole, ratio, equation)
        |
PICK the lightest tool: unit digit, remainder, ratio-scaling, smart numbers,
        options-substitution, or estimation  -- before full computation
        |
COMPUTE the minimum needed  ->  VERIFY (units, magnitude, plug-back)
        |
MATCH to an option; if two survive, test the boundary case
```

- ⚠️ **Least-work principle:** many CSAT quant items are solved by a **property** (unit digit,
  divisibility, parity, ratio) far faster than by full arithmetic. Each Topic 02-05 file teaches the
  property-first shortcut and states when it is safe.
- ⚠️ **Smart numbers / option-substitution** are legitimate when the answer is a pure ratio or when
  options are concrete values; they are unsafe when the question asks for an exact relationship among
  variables. Conditions are given per topic.

## 5. Option-elimination toolkit (works across families)

| Signal in an option | Usual verdict |
|---|---|
| Absolute words - "solely", "only", "always", "never", "cannot" | Often too strong for an inference passage; test hard. |
| A true real-world fact **not stated** in the passage | Wrong for passage-only items. |
| A number of the wrong **order of magnitude** | Eliminate before precise calculation. |
| Wrong **parity / unit digit / sign** | Eliminate by property, no full solve. |
| Two options that are logical opposites | The answer is often one of the two - focus there. |
| An option that restates the stem without adding the asked step | Usually a trap. |

## 6. Time allocation - adaptable, not prescriptive

> There is **no single correct timing**. Two hours for 80 items is on average ninety seconds each,
> but the right split depends on **your** strong families and the day's difficulty. Below are
> **templates to adapt**, not a rule to obey.

| Profile | Illustrative split (adapt freely) |
|---|---|
| Comprehension-strong | Bank all passages early and fast; spend the surplus on Pass-2 quant. |
| Quant-strong | Front-load one-step quant and series; keep passages for a calm middle block. |
| Balanced | Strict three-pass sweep; hard cap of about two minutes on any single item in Pass 2. |

- ⚠️ **The only firm timing rule:** set a **per-item ceiling** in Passes 1-2 and obey it; parking a
  hard item is a decision, not a failure.

## 7. Negative-marking and risk logic

At `2.5` correct and `5/6` wrong, the expected value of an attempt with success probability `p` is:

```text
EV(p) = p x 2.5  -  (1 - p) x 5/6
EV = 0  when  p = (5/6) / (2.5 + 5/6) = 1/4   (exactly a 1-in-4 blind guess)
```

| Situation after your work | p (roughly) | EV per item | Action |
|---|---|---|---|
| No idea, four live options | 0.25 | 0 | Break-even; skip unless you want variance. |
| One option eliminated (1 of 3) | 1/3 | +5/18 (~0.28) | Attempt. |
| Two eliminated (1 of 2) | 1/2 | +5/6 (~0.83) | Attempt. |
| Confident | 0.8-1.0 | +11/6 to +2.5 | Always attempt. |

- ⚠️ **Takeaway:** a blind guess is **not** free money - it is a coin with zero mean. **Every
  elimination** you can justify turns a guess positive. Guess **after** eliminating, not before.
- ⚠️ Because the paper only needs to be **qualified**, once your banked-plus-positive-EV total
  comfortably clears the bar, **stop taking marginal risks** - protect the lead.

## 8. Error taxonomy (log every mistake into one of these)

| Code | Error type | Typical fix |
|---|---|---|
| **C** | Concept gap (didn't know method/formula) | Re-study the topic file; add to weak-list. |
| **A** | Application slip (right idea, wrong step) | Slow the setup; write the relation before solving. |
| **X** | Calculation error (arithmetic slip) | Add a plug-back/estimation check. |
| **R** | Reading error (misread stem/option/passage) | Read the stem twice; underline "not/except/only". |
| **P** | Passage-only violation (used outside knowledge) | Force "which line proves this?" before choosing. |
| **T** | Time error (over-invested or rushed) | Enforce the per-item ceiling; use three passes. |
| **G** | Guess error (negative-EV guess) | Guess only after real elimination. |

> 🔑 Track the **mix** of codes, not just the count. A wall of **X** needs a verification habit; a
> wall of **P** needs passage discipline; a wall of **T** needs the three-pass clock.

## 9. Revision cycle (spaced)

```text
Day 0  learn topic (basic/NN)      ->  Day 1  redo missed drills
Day 3  advanced/NN drill set       ->  Day 7  timed mixed set (all 6 families)
Day 15 error-log-only revision     ->  Day 30 full timed 80-item mock
                (repeat the 7 -> 30 loop, always revising the error log first)
```

- ⚠️ Revise **the error log first, notes second**. The cheapest marks are the mistakes you already
  diagnosed once.

## 10. PYQ trend table (audited 2024-2026, Set A)

**Method:** every one of the **240 items** (80 per year x 3 years) in the Set A English text was
classified into exactly one of the six skill families that define Topics 01-06. Counts below are
that classification.

**Limitations (read before using the numbers):**

- ⚠️ These are **classification counts from OCR text**, not an official UPSC break-up. UPSC does not
  publish a per-item syllabus tag.
- ⚠️ The **Algebra/Data-Sufficiency (Topic 05)** and **Logical-Reasoning/DI (Topic 06)** boundary is
  genuinely fuzzy: a two-statement data-sufficiency item whose content is a coding puzzle can be read
  either way. Year-to-year swings between these two columns partly reflect that **judgement call on
  garbled OCR**, not only real paper drift. Read 05 and 06 **together** as "reasoning + sufficiency".
- ⚠️ The **2026** row is based on the paper text plus a **provisional, poorly-OCR'd** key; treat its
  counts as **provisional**.

| Topic | Skill family | 2024 | 2025 | 2026 (prov.) | 3-yr total | Share of 240 |
|---|---|---:|---:|---:|---:|---:|
| 01 | Reading Comprehension | 27 | 29 | 23 | 79 | ~33% |
| 02 | Number Systems | 13 | 19 | 12 | 44 | ~18% |
| 03 | Arithmetic (commercial math) | 8 | 3 | 7 | 18 | ~8% |
| 04 | Rates, Motion, Time & Geometry | 7 | 6 | 8 | 21 | ~9% |
| 05 | Algebra, Inequalities & Data Sufficiency | 13 | 11 | 9 | 33 | ~14% |
| 06 | Logical Reasoning, Coding, Counting & DI | 12 | 12 | 21 | 45 | ~19% |
| | **Total** | **80** | **80** | **80** | **240** | **100%** |

**What the audit reliably shows (robust to the fuzzy boundary):**

- ⚠️ **Reading Comprehension is the largest three-year family** and the largest family in each
  audited year, including the **provisional 2026 classification**.
- ⚠️ **Reasoning + Data Sufficiency together (Topics 05+06)** account for **78 of 240 (32.5%)**,
  almost the same as Reading Comprehension alone (79 of 240). Read Topics 05 and 06 together because
  their boundary is method-dependent.
- ⚠️ **Pure commercial arithmetic (Topic 03) is comparatively light** (about 8%), while **number
  systems (Topic 02)** form a substantial recurring block (about 18%).
- ⚠️ The paper's **weight shifts year to year** (notably Topic 06's rise in provisional 2026),
  which is exactly why the safe-score plan is **breadth of competence across all six families**, not
  betting on one.

## 11. Study sequence

1. Read this framework and the [README topic map](README.md).
2. **Foundation first, in order:** [basic/01](basic/01_Reading-Comprehension.md) through [basic/06](basic/06_Logical-Reasoning-Coding-Counting-and-DI.md).
3. **Then drill:** [advanced/01](advanced/01_Reading-Comprehension.md) through [advanced/06](advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md), one family at a time.
4. **Integrate:** timed mixed sets, logging every error by the Section 8 code.
5. **Audit the evidence:** use the [Question Audit Ledger](00_Question-Audit-Ledger.md) for the question-level map.
6. **Track progress:** use the internal self-diagnostics in the [Readiness Tracker](00_Readiness-Tracker.md).
