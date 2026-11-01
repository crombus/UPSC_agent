# csat-06 — Logical Reasoning, Coding, Counting and Data Interpretation: coverage ledger

**Status: in_progress.** All three sets are authored (60, 60 and 62 original items) and recorded in [`AUDIT.md`](AUDIT.md) (sections 1 to 6 for revision-1 and revision-2; section 7 for the pass-2 re-verification of revision-3; section 8 for the original revision-3 record, merged from the former `AUDIT-revision-3.md`). Revision-3 was reconciled with this ledger in pass 2 (2026-11-01): the column R3 below maps every owner row, five items were revised (R3-Q05, R3-Q08, R3-Q23 ANSWERS, R3-Q56, R3-Q57), and every key was recomputed by an independent check. The topic is **not** `complete`, for the reasons in section 5 of this file: the 25% length band is not met for 22, 27 and 19 items in the three sets; the uniquely-longest exceptions in R1 and R2 were not rebalanced; interpretive items still await a second-person review; and the owner gaps in section 4 remain.

## Sources

- **Basic owner (B):** `upsc-ai-kit/knowledge/CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`, sections 1–11 and the generated 2026, 2024–2025 and 2018–2023 PYQ integration blocks.
- **Advanced owner (A):** `upsc-ai-kit/knowledge/CSAT/advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md`, sections 1–13 and its historical PYQ block.
- **Scope boundary:** communication, negotiation and questionnaire items belong to Topic 07 (`basic/07`, `advanced/07`). The 2026 owner routes six communication items there; they are not tested in this bank by design.
- **PYQ provenance:** the 2024 and 2025 CSAT Set-A keys are supplied local scans whose official status is not certified; the 2026 key is marked provisional; the 2018–2023 keys are not held locally. Under `final-mcq/INSTRUCTIONS.md`, no exact PYQ is reproduced or keyed here. PYQ families are listed only by demand type in section 3.

## 1. Set inventory

| Set | Items | File status | Verification record | Notes |
|---|---|---|---|---|
| revision-1 | 60 | QUESTIONS.md and ANSWERS.md written; computed key check passed for all 60 | `AUDIT.md` (this pass) | Full coverage of the owner rows in section 2 |
| revision-2 | 60 | QUESTIONS.md and ANSWERS.md written; computed key check passed for all 60 | `AUDIT.md` (this pass) | Cross-links, multi-step traps and close distractors |
| revision-3 | 62 | QUESTIONS.md and ANSWERS.md present; reconciled and re-verified in pass 2 (5 items revised) | `AUDIT.md` section 7 (pass 2) and section 8 (original record, merged from `AUDIT-revision-3.md`) | Text-only; no cube-figure or net items; two Topic 07 communication items removed in pass 2 and replaced by on-scope items |

## 2. Owner-row ledger

Each row names the owner section, the technique or trap, and the question IDs in revision-1 (R1) and revision-2 (R2) that test it. Revision-3 coverage is stated by its own record and is not repeated here.

| # | Owner row (source) | R1 | R2 | R3 | Coverage note |
|---|---|---|---|---|---|
| 1 | Externalise the structure: draw the seats, grid, tree, compass (B §1–3) | Q24, Q25, Q26, Q32, Q33 | Q24, Q25, Q26, Q30, Q34 | Q22, Q23, Q24, Q26, Q27 | Each arrangement is solved from the drawn structure |
| 2 | Linear arrangement, fixed clue first (B §2, §5 H, A §3 M1) | Q24 | Q24, Q27, Q28 | Q22, Q24, Q26 | Forced order in both sets |
| 3 | Circular arrangement, rotations identical, reflections distinct; `(n−1)!` (B §4, §5 H) | Q25 | Q25 | Q23, Q27 | Counted by enumeration against inclusion–exclusion |
| 4 | Two-row and multi-constraint seating (A §3 M1) | Q26 | Q24, Q26 | Q23 (multi-constraint only; no two-row seating in R3) | Solution sets checked; asked fact fixed in all solutions |
| 5 | Ranking and time-slot order with immediate-adjacency rules (owner demand routes) | Q27, Q28, Q29, Q30 | Q27, Q28 | Q25 (ranking only; no time-slot adjacency in R3) | Exact enumeration |
| 6 | Blood relations: only son/daughter, in-law and generation traps (B §2, §5 B, §6) | Q16, Q17, Q18, Q19 | Q16, Q17, Q18, Q19 | Q19, Q20 (generation and sibling counts; no in-law trap in R3) | Hand edge-chain check; see `AUDIT.md` section 5 |
| 7 | Directions: right turn = +90 clockwise; coordinate displacement; path versus displacement (B §2, §6, §7) | Q20, Q21, Q22, Q23 | Q20, Q21, Q22, Q23 | Q17, Q18, Q21, Q54 | Exact coordinates and headings |
| 8 | Coding by shift, reverse, position rule and symbol operations: verify on every letter (B §2, §5 I; A §3 M2) | Q06, Q07, Q08, Q09, Q10 | Q06, Q07, Q08, Q09, Q10 | Q11, Q12, Q13, Q16 | Rule families enumerated; one-output asserted |
| 9 | Series: differences, ratios, known forms, interleaved series, letter-position series (B §2, §5 A, §9.1) | Q11–Q15 | Q11–Q15 | Q09, Q10, Q14, Q15 | Patterns checked on every given term |
| 10 | Conditional logic: implication, contrapositive, converse, equivalence (B §4.2, §6, §7; A §3 M4) | Q01, Q04, Q05 | Q03, Q04, Q05 | Q01, Q05, Q08 | Truth tables; converse traps in distractors |
| 11 | Syllogisms: existential versus universal, counter-diagram test; "some" is not "all" (B §6, §7; A §2, §5) | Q01, Q02, Q03 | Q01, Q02 | Q02, Q03, Q04, Q06 | Bounded model search with counter-models |
| 12 | Possible versus probable versus certain (B §4.1, §9.6) | Q40 | Q60 | Q04, Q07, Q08 | Probability above zero versus one |
| 13 | Permutations `P(n,r)`, restricted first digit, leading zero (B §4, §5 C, §5 K, §9.9) | — | Q39 | Q37, Q53, Q60, Q61 | `P(n,r)` with a restriction; not repeated in R1 |
| 14 | Combinations `C(n,r)`; counting pairs and selections (B §4, §5 M) | Q31, Q44 | Q34 | Q30, Q38 | Pair counts and selection counts |
| 15 | Words with repeats: `total!/(product of repeat factorials)`; repeat-factorial slip (B §4, §9.2; A §8 #3) | Q41 | — | Q28 | Single item; R2 has none |
| 16 | Handshakes and segments `C(n,2)`, no three collinear (B §4, §9.4; A §8 #2) | Q44 | Q33 | Q58 (diagonals as segments; no handshake item in R3) | Lines and pairs with a collinear exception |
| 17 | Worst-case draws: take the maximum without the target, then one more (B §4, §5 N, §9.14) | Q43 | Q41 | Q31, Q62 | Enumerated failing draws |
| 18 | Probability: favourable over total; complement `1 − P(none)` (B §4, §9.6; A §4) | Q42 | Q40, Q60 | Q39, Q40, Q41 | Complement appears in the R2 answer rationale |
| 19 | Sequential probability without replacement: multiply conditional fractions (B §4, §5 L, §9.11; A §2, §8 #6, #9) | Q42 | Q42 | Q38, Q42 | Ordered and unordered routes both shown |
| 20 | Dice and coin probability (A §3 M3, §8 #1) | — | Q40, Q60 | Q40 (dice only; no coin item in R3) | Two-dice prime sum; three-coin possibility |
| 21 | Inclusion–exclusion for three sets, with a triple overlap added back; LCM-based multiples (A §2, §4, §8 #4) | Q37 | Q35 | Q34, Q36 | Full seven-term line in R1; exact-two count in R2 |
| 22 | Venn bounds and exact-region counts (B §4, §5 J, §6, §9.10) | Q38, Q39 | Q35, Q36, Q37 | Q35, Q36 | Lower and upper bounds; linear region solve |
| 23 | Figure counting by size: squares, rectangles, cube partitions, polygon diagonals (B §2, §5 N, §9.13) | Q32, Q33, Q34, Q35 | Q30, Q31, Q34 | Q32, Q33, Q58 (no rectangle count in R3) | Counted by size; formula checked by enumeration |
| 24 | Cube views: faces that share a corner are adjacent; the opposite face is the one left over (B §2, §5 N) | Q36 | Q32 | — (no cube-view item in R3) | Added to close an owner gap |
| 25 | Data arrangement: sorting by primary and tie-break keys; grid and rota placement (owner demand routes) | Q52, Q53, Q55 | Q50, Q51, Q52, Q53 | Q55 (rule-based shortlisting only; no grid or rota in R3) | Uniqueness asserted |
| 26 | Constraint-based selection with a budget (owner caselet routes) | Q58 | Q56 | Q55 (threshold selection only; no budget optimum in R3) | Optimum over all feasible sets |
| 27 | Truth-teller, knight-knave and exact-one-true puzzles (owner caselet routes) | Q60 | Q57 | Q57 (truth-teller; replaced in pass 2) | Assignments enumerated |
| 28 | Assignment with forbidden placements (owner caselet routes) | — | Q59 | Q56 (forbidden-day assignment; replaced in pass 2) | Derangement count |
| 29 | DI level versus share versus change in share (B §5 M; A §10 trap 2) | Q45, Q47 | Q44, Q46 | Q43, Q44, Q48, Q49 | Share and level kept separate |
| 30 | DI percentage points versus relative percentage (B §5 M; A §10 trap 3) | Q47 | Q46 | Q44, Q49 | Both forms in distractors |
| 31 | DI successive changes on different bases; no cancellation (A §10 trap 1) | — | Q45 | Q46, Q50 (base-year choice) | Multiplicative growth factors |
| 32 | DI pie-chart angle to count (owner demand routes) | Q48 | Q48 | Q45, Q52 | Angles converted exactly |
| 33 | DI weighted average; weighted versus simple average; missing value (owner demand routes) | Q49 | Q47, Q49 | Q47 (weighted; no missing-value item in R3) | Weights applied to each component |
| 34 | DI price-quantity expenditure and discount chains (owner demand routes) | Q50 | Q43 | Q46 (discount chain only; no price-quantity index in R3) | Aggregate versus unweighted index |
| 35 | DI two-table derived measure (owner demand routes) | Q51 | — | Q43, Q48 (derived per-unit measure; no two-table item in R3) | Derived per-staff and female share |
| 36 | Multiple solutions: only facts common to every solution are guaranteed (A §5) | Q26, Q27, Q28 | — | Q24, Q25 | Stated where a fact is forced |
| 37 | Complement and inclusion–exclusion as a time-saving method (A §4) | — | Q41 (worst-case complement) | Q34, Q39 (complement; no separate complement drill) | Partial; no separate complement drill |
| 38 | Interpersonal and communication items (boundary: Topic 07) | — | — | — (Topic 07 items removed from R3 in pass 2) | Excluded by design; see Sources |

## 3. PYQ-pattern notes (demand families only; no UPSC text reproduced)

The owner's 2024–2026 and 2018–2023 integration blocks name the demand families below. Each family is tested here by an original item, not by an exact PYQ. No answer letter is inferred from any local key.

| Demand family (neutral) | Years in owner routing | R1 items | R2 items | R3 items |
|---|---|---|---|---|
| Statement-conclusion and syllogism | 2018–2026 | Q01–Q03 | Q01, Q02 | Q02, Q03, Q04, Q06 |
| Implication consistency and conclusion validity | 2023–2024 | Q04, Q05 | Q03, Q04, Q05 | Q01, Q05, Q08 |
| Seating and placement deduction | 2018–2025 | Q24–Q28 | Q24–Q27 | Q22–Q27 |
| Blood relations and family-relation deduction | 2019–2025 | Q16–Q19 | Q16–Q19 | Q19, Q20 |
| Multi-turn direction and distance | 2024–2026 | Q20–Q23 | Q20–Q23 | Q17, Q18, Q21, Q54 |
| Letter, digit and symbol coding | 2018–2025 | Q06–Q10 | Q06–Q10 | Q11, Q12, Q13, Q16 |
| Series completion and pattern | 2019–2025 | Q11–Q15 | Q11–Q15 | Q09, Q10, Q14, Q15 |
| Figure counting (squares, cubes, polygons, diagonals) | 2018–2023 | Q32–Q35 | Q30–Q34 | Q32, Q33, Q58 |
| Venn and set overlap | 2018–2023 | Q37–Q39 | Q35–Q37 | Q34, Q35, Q36 |
| Constrained permutation, worst case and handshakes | 2020–2026 | Q31, Q41, Q43, Q44 | Q39, Q41 | Q28–Q31, Q37, Q53, Q56, Q60–Q62 |
| Probability over draws and selections | 2023 | Q42 | Q40, Q42, Q60 | Q38–Q42 |
| Data interpretation: tables, pie, share, level, change | 2018–2026 | Q45–Q51 | Q43–Q49 | Q43–Q52 |
| Data arrangement and ranking under constraints | 2018–2026 | Q52–Q55 | Q50–Q53 | Q25, Q55 |
| Caselet decision logic and budget selection | 2023–2026 | Q56–Q60 | Q54–Q59 | Q55, Q57 |

## 4. Open gaps (stated honestly)

- **Exact PYQs** are not in any set (provenance and reproduction-rights holds in `INSTRUCTIONS.md`). Coverage is by demand family only.
- **Complement counting** (A §4) has no stand-alone drill; it appears in the worst-case and possibility rationales and in R3-Q39 (at-least-one complement).
- **Dice sums of at least ten** and **two draws with at least one white** (A §8 #5, #6) are covered by R3-Q40, R2-Q40 and R1-Q42; no coin item exists in any set (owner row 20).
- **Cube faces** (row 24) are tested with two views only (R1-Q36, R2-Q32). No set has a cube-net or three-dimensional rotation item, and R3 has no cube-view item at all.
- **Relation items** (row 6): the in-law and generation traps are tested only in R1 and R2; R3-Q19 and R3-Q20 cover generation and sibling counting. Relation keys are checked by hand-derived edge chains, not by a family-graph search.
- **Row-level gaps in R3 only** (R1 or R2 covers them): two-row seating (row 4), time-slot adjacency (row 5), missing-value weighted average (row 33), price-quantity index (row 34), two-table derived measure (row 35), budget optimum (row 26), grid and rota (row 25), handshakes (row 16), coins (row 20), rectangles in figure counting (row 23).
- **Length balance:** the correct option is the uniquely longest in 2 items of revision-1 (3.3%), 5 of revision-2 (8.3%) and 3 of revision-3 (4.8%), so the ceiling of about 25% is met in all three sets. The 25% length band (longest within 25% of shortest) is **not** met for 22 items in revision-1 (63% met), 27 in revision-2 (55% met) and 19 in revision-3 (69% met); these are numeric, fraction and name options whose length follows digit or letter count (`AUDIT.md` sections 2, 4 and 7). The R1 and R2 exceptions listed in `AUDIT.md` section 4 (R1-Q04, R1-Q27, R2-Q03, R2-Q17, R2-Q18, R2-Q19, R2-Q46) were not rebalanced in pass 2.
- **Interpretive items flagged for review:** R1-Q08 (BODMAS convention stated), R1-Q25 (round-table convention stated), R2-Q21 (path versus displacement), R2-Q55 (abstracted ballot rules), R3-Q23 (clockwise-seat definition stated in the stem). R3-Q51 (median and mean) and R3-Q54 (Pythagoras) use arithmetic outside the owner rows and are flagged in `ANSWERS.md`.
- **Revision-3 reconciliation (pass 2, 2026-11-01):** the second agent's record is merged into `AUDIT.md` section 8; every row above now lists its R3 items. R3-Q08 (a modal keyed option), R3-Q05 (a 'four statements' stem over three statements, and option-length ratio 1.8), R3-Q23 (ANSWERS text misaligned with option letters), and R3-Q56 and R3-Q57 (Topic 07 communication items) were revised. R3-Q22's written explanation was corrected; its key is unchanged.

## 5. Next actions

1. Second-person or independent review of the interpretive items in section 4 and of `AUDIT.md` section 4 before the bank is used as a graded instrument.
2. Rebalance the length cues in the R1 and R2 items named in `AUDIT.md` section 4, and review the numeric and fraction outliers listed in `AUDIT.md` section 7.4.
3. Close the R3-only row gaps listed in section 4 (two-row seating, time-slot adjacency, missing-value average, budget optimum, cube views) or record them as accepted gaps, then set the topic status to `complete` only if all three sets, this file and `AUDIT.md` pass.
