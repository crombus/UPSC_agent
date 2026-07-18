# Logical Reasoning, Coding, Counting and Data Interpretation - ADVANCED

> **Subject:** CSAT | **Tier:** Advanced Drill | **Family:** Logical reasoning / decision-making / data interpretation.
> **Core skill:** multi-constraint arrangements, syllogism validity, coding rules, dice/counting
> probability, inclusion-exclusion, and multi-step data interpretation.
> **Grounded in:** audited UPSC CSAT PYQ sets 2024-2026 (Set A). Drills are **computationally verified**.
> ✅ = rule/fact | ⚠️ = guidance | 📝 = original example.
> *Companion: `basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`.*

---

## 1. Architecture

```text
   MULTI-CONSTRAINT REASONING ITEM
        |
   build the STRUCTURE (grid / tree / compass / Venn / table)
        |
   enter constraints STRONGEST-FIRST; prune impossibilities
        |
   +----------------+-----------------+
   |                |                 |
 UNIQUE placement  VALID conclusion  EXACT count/prob
 (arrangement)     (holds in ALL     (order? overlap?)
                    diagrams)
```

**Analytical claim:** a hard reasoning item is won by **ordering the constraints** (most restrictive
first) and by asking, for logic, "does it hold in **every** consistent diagram?".

## 2. Advanced tools with conditions

| Tool | Statement | Condition |
|---|---|---|
| ✅ **Constraint ordering** | Place the clue that fixes the most first; each fix prunes the tree. | Recheck every earlier clue after each placement. |
| ✅ **Syllogism validity** | A conclusion is valid only if true in **all** consistent Venn diagrams. | One counter-diagram disproves it. |
| ✅ **Coding rule extraction** | Derive the transformation (shift/reverse/position) from the given pair. | Confirm the rule on **every** given letter before applying. |
| ✅ **Dice/coin counting** | Enumerate the sample space (`6^k`, `2^k`); count favourable. | Outcomes must be equally likely. |
| ✅ **Inclusion-exclusion** | `|A∪B| = |A| + |B| - |A∩B|`. | Subtract the overlap once. |
| ✅ **Polygon diagonals** | `n(n-3)/2`. | Convex polygon. |

## 3. Harder methods (worked)

### 📝 Method 1 - multi-constraint seating

**Five people P, Q, R, S, T sit in seats 1-5 (left to right).** Clues: R is in the middle (seat 3); P
is at the extreme left; Q is immediately right of P; T is **not** at an extreme end. Then P=1, Q=2,
R=3; T cannot be seat 5, so T=4 and S=5. **Unique order: P, Q, R, T, S.** *(Each clue checks out; the
solution is forced.)*

### 📝 Method 2 - coding rule

**If EARTH is coded GCTVJ (each letter shifted +2), how is MARS coded?** `M->O, A->C, R->T, S->U` ->
**OCTU.** *(Verified by letter positions 13->15, 1->3, 18->20, 19->21.)*

### 📝 Method 3 - dice probability

**Two fair dice; `P(sum = 7)`?** Favourable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 of 36 ->
**1/6.** *(Verified.)*

## 4. Time-saving techniques (safe conditions)

- ⚠️ **Strongest-constraint-first** placement. *Safe always; it minimises backtracking.*
- ⚠️ **Counter-diagram test** for syllogisms - try to build one case where the conclusion fails. *Safe
  always; if you can, the conclusion is invalid.*
- ⚠️ **Complement counting** `P(at least one) = 1 - P(none)`. *Safe for independent trials.*
- ⚠️ **Inclusion-exclusion** for "either/or" counts. *Safe; remember to subtract the overlap exactly
  once.*

## 5. Boundary cases

- ⚠️ An arrangement puzzle may have **multiple** valid solutions - then only facts common to **all**
  solutions are guaranteed.
- ⚠️ "Some A are B" does **not** give "some A are not B" - existential statements do not license their
  negatives.
- ⚠️ Probability requires **equally likely** outcomes; weighted or dependent events need the sample
  space rebuilt.

## 6. Advanced traps

- ❌ Reporting a placement true in **one** solution when the puzzle has several. -> Report only forced
  facts.
- ❌ Accepting a syllogism because it "sounds right". -> Find a counter-diagram.
- ❌ Applying a coding rule confirmed on only one letter. -> Verify on all given letters.
- ❌ Double-counting the overlap in "either/or". -> Subtract `|A∩B|` once.
- ❌ Adding probabilities of non-exclusive events. -> Use inclusion-exclusion or complements.

## 7. Error analysis

| Recurring miss | Master-Framework code | Fix |
|---|---|---|
| Over-claiming a unique seat | A | List all solutions; keep only common facts. |
| Invalid syllogism accepted | C | Always attempt a counter-diagram. |
| Wrong coding rule | R | Re-derive the rule on every letter. |
| Probability sample-space errors | X | Write `6^k`/`2^k` and count favourable explicitly. |

## 8. Advanced drill (with full solutions)

1. Five people P, Q, R, S, T sit in seats 1-5. R is in the middle; P is at the far left; Q is
   immediately right of P; T is not at an end. Give the full order.
2. In a code, EARTH -> GCTVJ. Encode MARS.
3. Two fair dice are rolled. Find `P(sum = 7)`.
4. A fair coin is tossed 3 times. Find `P(at least one head)`.
5. How many diagonals does a regular octagon have?
6. How many integers from 1 to 100 are divisible by **neither 2 nor 3**?

**Solutions.**

1. **P, Q, R, T, S.** Forced by the constraints (see Method 1). *(Verified consistent.)*
2. **OCTU.** Shift each letter +2. *(Verified.)*
3. **1/6.** 6 favourable of 36. *(Verified.)*
4. **7/8.** `1 - (1/2)^3 = 1 - 1/8`. *(Verified.)*
5. **20.** `8 x (8 - 3)/2 = 20`. *(Verified.)*
6. **33.** `100 - (50 + 33 - 16) = 33`. *(Verified.)*

## 9. Multi-step data interpretation (worked)

Read this revenue table (in crore):

| Year | Revenue |
|---|---:|
| 2022 | 400 |
| 2023 | 500 |
| 2024 | 450 |

- Growth 2022 -> 2023 `= (500 - 400)/400 =` **+25%.** *(Verified.)*
- Change 2023 -> 2024 `= (450 - 500)/500 =` **-10%.** *(Verified.)*
- ⚠️ **Trap:** a +25% then -10% does **not** return to 400 - it gives `400 x 1.25 x 0.90 = 450`, matching
  the table. Percentage changes are on **different bases**, so they do not cancel.

## 10. PYQ-pattern notes (2024-2026, Set A)

- ⚠️ This is **one of the largest CSAT families** (and, together with data sufficiency in Topic 05, the
  single biggest block of the paper - see `00_Master-Framework.md`).
- ⚠️ Recurring shapes: **seating/ordering arrangements**, **blood relations and directions**,
  **coding-decoding**, **syllogism/deduction**, **decision-making scenarios**, **counting/probability**,
  and **data interpretation** from tables/graphs.
- ⚠️ The papers reward candidates who **draw the structure** and **read the exact quantity asked**;
  they punish mental juggling and misread stems.

## 11. Study links

- ✅ Foundation companion: `basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`.
- ✅ `advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md` - data-sufficiency content overlaps
  this family.
- ✅ `advanced/02_Number-Systems-and-Number-Sense.md` - counting and inclusion-exclusion share methods.
