# CSAT (Prelims Paper II) - Knowledge Base Index

> **Subject:** CSAT - Civil Services Aptitude Test | **Paper:** UPSC Prelims General Studies Paper II.
> **Spine:** Audited UPSC CSAT PYQ sets 2024, 2025 and 2026 (GS Paper II, Set A) + official answer
> keys (2024, 2025 final; 2026 provisional) + the printed instruction page of the papers.
> **Start here:** `00_Master-Framework.md`, then work `basic/01` -> `basic/06`, then the `advanced/` drills.

---

## 1. What CSAT is and why the strategy differs

- ✅ CSAT is **Paper II** of the UPSC Civil Services (Preliminary) Examination.
- ✅ **Structure (from the printed instruction page of the 2025 Set A paper):** **80 items**,
  **maximum marks 200**, **time allowed two hours**, all items carry equal marks, each item printed
  in Hindi and English with four alternatives.
- ✅ **Marks per item (derived):** `200 / 80 = 2.5` marks per correct answer.
- ✅ **Negative marking (from the printed instructions):** for a wrong answer, **one-third of the
  marks assigned to that question is deducted** -> `2.5 / 3 = 0.833...` marks per wrong answer.
  Marking more than one option counts as wrong; a blank carries **no penalty**.
- ⚠️ **Qualifying nature:** UPSC's Prelims scheme treats Paper II as **qualifying**, with a minimum
  standard commonly stated as **33% (i.e., 66 of 200 marks)**; only Paper I (GS-I) marks decide the
  Prelims merit/cut-off. **Confirm the exact threshold against the current year's official
  notification before relying on it** - this module does not invent policy.

> 🔑 **Consequence for study:** the goal is **safe, reliable qualification**, not a top rank. A
> module built for CSAT therefore optimises **accuracy, selection and time control**, not exhaustive
> coverage of every exotic sum. This is why the files below emphasise elimination, verification and
> "leave-it" discipline as much as formulas.

## 2. Safe-score strategy (method, not a guarantee)

- ⚠️ Because only ~**66/200** is needed to clear the qualifying bar, a candidate does **not** need
  all 80 items. A disciplined plan is to **lock a strong-family core** (usually Reading
  Comprehension + one or two comfortable reasoning/quant families), **secure those with high
  accuracy**, and **attempt the rest selectively**.
- ⚠️ **Negative-marking logic:** at 2.5 correct / 0.833 wrong, a **blind 4-option guess** has
  expected value `(0.25 x 2.5) - (0.75 x 0.833) = 0` - it is break-even, not free. Guessing pays
  **only after genuine elimination** raises the success probability above one-in-four (see
  `00_Master-Framework.md`, error and risk sections).
- ⚠️ These are **planning heuristics derived from the marking scheme**, not official targets. Treat
  any number here as adaptable, and re-derive it if the paper pattern or notification changes.

## 3. The six-topic map (evidence-based)

The topics were locked **after classifying all 240 questions** of the 2024-2026 Set A papers into
six skill families (see `00_Master-Framework.md` for the full method, counts and limitations). The
six families are **exhaustive and non-overlapping** and together cover the official CSAT syllabus:
comprehension; interpersonal/communication and decision-making; logical reasoning and analytical
ability; general mental ability; basic numeracy; and data interpretation.

| # | Topic file | Skill family covered | Syllabus anchor |
|---|---|---|---|
| 01 | `Reading-Comprehension` | Passage-only comprehension: central idea, inference, assumption, tone/scope, elimination | Comprehension |
| 02 | `Number-Systems-and-Number-Sense` | Divisibility, remainders, factors, digits, HCF/LCM, powers/units, number series | Basic numeracy; general mental ability |
| 03 | `Arithmetic-and-Commercial-Math` | Ratio/proportion, percentages, averages, mixtures/alligation, profit-loss, interest, partnership, ages | Basic numeracy |
| 04 | `Rates-Motion-Time-and-Geometry` | Time-work, pipes/cisterns, speed-distance, trains/boats/races, clocks, calendars, geometry/mensuration | Basic numeracy; general mental ability |
| 05 | `Algebra-Inequalities-and-Data-Sufficiency` | Equations, inequalities, quantitative comparison, and the two-statement data-sufficiency format | Analytical ability; decision-making |
| 06 | `Logical-Reasoning-Coding-Counting-and-DI` | Arrangements, blood relations, directions, coding, syllogism, counting/probability, data interpretation, decision-making | Logical reasoning; decision-making; data interpretation |

**Boundary notes (why the grouping is clean, not arbitrary):**

- **Topic 04 groups "rates, motion and shapes"** because time-work, pipes, speed-distance, clocks,
  calendars and mensuration all reduce to a **rate x quantity or a geometric-measure** template;
  keeping them together prevents overlap with the pure number theory of Topic 02.
- **Topic 05 owns the two-statement Data-Sufficiency format** even when the hidden content is
  arithmetic, because the tested skill is **"is the information sufficient?"** - a decision skill,
  not a computation skill. Topic 06 owns **decision-making word problems and DI tables** where the
  skill is reading a scenario/table, not judging sufficiency.
- **Reading Comprehension (01) is deliberately a single, large topic** because it is consistently
  the biggest single family in every year (see the trend table) and rewards one coherent method.

## 4. How Foundation vs Advanced Drill works

- **`basic/NN` = Foundation.** Builds the concept: visual, definitions/formulas with conditions,
  a stepwise method, **original solved examples**, common traps, quick checks, and a **mini-drill with
  full answers and explanations**. Read these first, in order 01 -> 06.
- **`advanced/NN` = Advanced Drill.** Assumes the Foundation. Adds **harder multi-step methods**,
  **UPSC-style traps**, **time-saving techniques with the conditions under which they are safe**, a
  larger **original drill set with full worked solutions**, an **error-analysis** section, and
  **PYQ-pattern notes** distilled from the 2024-2026 papers. Advanced files never simply repeat the
  Foundation.
- **Same number = same topic** across both tiers (`basic/03` pairs with `advanced/03`).

## 5. Source and PYQ methodology

- ✅ **Primary sources:** the OCR text of the 2024/2025/2026 GS Paper II (CSAT) Set A papers and
  their answer keys, plus the original PDFs under
  `books/prelima_question_paper_answers/`. These are also ingested in the Qdrant vector store under
  the subject tag **`CSAT PYQ`**.
- ⚠️ **OCR caveat:** the scanned papers are bilingual; the **Hindi (Devanagari) half is garbled**
  by OCR, so all analysis uses the **clean English half only**. Answer keys are mapped **Set A ->
  Set A column** only.
- ⚠️ **2026 caveat:** the 2026 answer key is **provisional** and its OCR quality is poor; any 2026
  count or answer is labelled **provisional** wherever used.
- **Copyright discipline:** this module **does not reproduce UPSC questions verbatim**. It
  **describes the PYQ patterns** and provides **original examples and drills** that train the same
  skills. Short identifying fragments appear only where needed to name a pattern.

## 6. Navigation order

1. `00_Master-Framework.md` - attempt strategy, workflows, error taxonomy, PYQ trend table.
2. `basic/01` -> `basic/06` - build every family's foundation in order.
3. `advanced/01` -> `advanced/06` - drill each family to exam intensity.
4. `00_Readiness-Tracker.md` - log timed sets, track accuracy/risk, run revision cycles, and check
   readiness gates before the exam.

## 7. Files in this module

| File | Purpose |
|---|---|
| `README.md` | This index. |
| `00_Master-Framework.md` | Strategy, workflows, error taxonomy, and the 2024-2026 PYQ trend table. |
| `00_Readiness-Tracker.md` | Reusable skill checklist, timed-set log, metrics, error log, revision plan, readiness gates. |
| `basic/01`..`basic/06` | Foundation files, six topics. |
| `advanced/01`..`advanced/06` | Advanced Drill files, six topics. |
