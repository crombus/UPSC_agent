# CSAT-06 Logical Reasoning, Coding, Counting and Data Interpretation: audit record (revision-1 and revision-2)

Date of verification: 2026-11-01. Scope: `revision-1/QUESTIONS.md`, `revision-1/ANSWERS.md`, `revision-2/QUESTIONS.md` and `revision-2/ANSWERS.md` (60 original items each, `R1-Q01` to `R1-Q60` and `R2-Q01` to `R2-Q60`). Revision-3 was authored by a second agent; its original record is section 8 of this file (merged from the former `AUDIT-revision-3.md`) and its pass-2 re-verification is section 7. No UPSC PYQ wording or option is reproduced, and no item is labelled as a PYQ.

## 1. Method

- Every key was recomputed independently of the authored text before the files were rendered. The build step (`build.py`) asserts, for every item, that the computed answer equals the keyed option and that no distractor duplicates it. No item failed.
- **Puzzle uniqueness.** Seating, ranking, scheduling, grid, rota, lecture-order and weight items were solved by enumerating every permutation or assignment in Python and filtering by the stated clues. Each item either has exactly one solution, or (where two solutions exist) the key is a fact that holds in every solution. The enumeration result is recorded in the table in section 3.
- **Syllogisms and conditional logic.** Statement-conclusion items were checked by bounded model search: all multisets of up to four individuals, each with every combination of attributes, keeping only those models that satisfy the premises; a conclusion "follows" only if it holds in every such model, and a counter-model is found for each rejected conclusion. Conditional items were checked by full truth tables over all atoms.
- **Counting and probability.** Formulae were checked against direct enumeration (for example all 120 ordered four-digit strings from the digits 0 to 4; all 32 on/off patterns of five lamps; all 125 unit cubes of a 5-cube; all 36 dice outcomes; all integers from 1 to 120). Worst-case draws were checked by enumerating every failing draw.
- **Data interpretation.** Each value was computed in exact arithmetic (`fractions.Fraction`) from the table values, including every intermediate share, percentage and weighted mean.
- **Blood relations.** These have no free numerical choice. Each key was derived from an explicit parent, sibling and spouse edge list recorded in section 3; it was not searched by brute force over family graphs.
- **Original-only check.** Every item was written for this bank; no official PYQ text, option or key was copied.
- The check scripts are kept outside the repository at `/tmp/mcq_audit/csat06/` (`common.py`, `r1_verify.py`, `r2_verify.py`, `r1_items.py`, `r2_items.py`, `build.py`). They are not added to the repository.

## 2. Balance and difficulty statistics

| Measure | Revision-1 | Revision-2 | Target |
|---|---|---|---|
| Questions | 60 | 60 | at least 60 |
| Correct-letter distribution A / B / C / D | 15 / 15 / 15 / 15 (25% each) | 15 / 15 / 15 / 15 (25% each) | each letter 20–30% |
| Correct option is the uniquely longest option | 2 of 60 (3.3%) | 5 of 60 (8.3%) | no more than about 25% |
| Correct option is the uniquely shortest option | 4 of 60 (6.7%) | 4 of 60 (6.7%) | recorded for information |
| All four options within 25% of the shortest by character count | 38 of 60 (63%) | 33 of 60 (55%) | target; not met for all |
| Items with a target of 75 seconds or more (multi-step) | 41 of 60 (68%) | 53 of 60 (88%) | at least 40% need two or more steps or a trap |
| Items with a named trap in the answer key | 60 of 60 | 60 of 60 | every item |

Notes on the length statistics. The 25% length band is not met by the items whose options are bare numbers or single short labels (for example "2", "8", "20", "Niece", "Ajay"), because a bare numeral or a one-word relation cannot be padded to the same length without adding content that is not part of the answer. Those items were kept rather than padded with filler. The correct option is the uniquely longest option in only 2 items of revision-1 and 5 items of revision-2 (listed in section 4), so the principal cue the rule targets is largely absent; the 25% band itself is not satisfied for every item, and this is stated as an open issue.

## 3. Per-item verification record

Columns: the key as published; the verification method (the function that recomputes it); and how determinacy was established.

### R1 item keys

| ID | Key | How the key was verified (script function) | Determinacy |
|---|---|---|---|
| R1-Q01 | I and III only | model search, 4 attributes, up to 4 individuals | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R1-Q02 | I and II only | model search | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R1-Q03 | I only | model search | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R1-Q04 | The lift was not serviced | propositional truth table over 4 atoms | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R1-Q05 | The audit did not pass | truth table over 3 atoms | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R1-Q06 | IQF | 4 consistent rules in family, all give same code | Checked by enumeration or assertion |
| R1-Q07 | 57 | arithmetic | Checked by arithmetic or formula |
| R1-Q08 | 73.25 | Python eval with BODMAS | Checked by arithmetic or formula |
| R1-Q09 | 108 | arithmetic | Checked by arithmetic or formula |
| R1-Q10 | GRJ | unique shift k=3 consistent with both examples | Checked by enumeration or assertion |
| R1-Q11 | 65 | differences 1,2,4,8,16,32 double each step | Checked by arithmetic or formula |
| R1-Q12 | 11 | odd positions step +6 (5,11,17,23); even positions step +1 (8,9,10); 8th term is even-position | Checked by arithmetic or formula |
| R1-Q13 | T | gaps [3, 4, 5], next gap 6 | Checked by arithmetic or formula |
| R1-Q14 | 324 | ratio 3 | Checked by arithmetic or formula |
| R1-Q15 | 37 | n^2+1 form; differences 3,5,7,9 -> next +11 | Checked by arithmetic or formula |
| R1-Q16 | Niece | Hand chain (explicit edges): man M - wife H; H father F; F only son B (H brother); B daughter W -> W is M niece by marriage. | Determined by the stated relations (no free choice) |
| R1-Q17 | Paternal aunt | Hand chain (explicit edges): D father of A; C mother of A and B; E sister of D -> E is A paternal aunt. | Determined by the stated relations (no free choice) |
| R1-Q18 | Niece | Hand chain (explicit edges): Priya only daughter of Ravi father F -> Priya sister of Ravi and Sunil; Meera daughter of Sunil -> Meera niece of Priya. | Determined by the stated relations (no free choice) |
| R1-Q19 | Cousin | Hand chain (explicit edges): paternal grandmother G; her only daughter = Ananya paternal aunt; aunt son = man -> cousin. | Determined by the stated relations (no free choice) |
| R1-Q20 | 4 m, north | coordinates end at (0,4) | Checked by arithmetic or formula |
| R1-Q21 | North-east | heading arithmetic, N=0 clockwise | Checked by arithmetic or formula |
| R1-Q22 | 10 km | coordinates (-8, 6) | Checked by arithmetic or formula |
| R1-Q23 | 4 m east | end at (4,0) | Checked by arithmetic or formula |
| R1-Q24 | C | unique order AECDB | Checked by enumeration or assertion |
| R1-Q25 | 4 | brute force over 5! seatings with first person fixed | Checked by enumeration or assertion |
| R1-Q26 | Asha | 2 seatings; Meera opposite is fixed | Checked by enumeration or assertion |
| R1-Q27 | Chetan | 2 floor assignments; floor 3 fixed | Checked by enumeration or assertion |
| R1-Q28 | Y | 2 rankings; first place fixed | Checked by enumeration or assertion |
| R1-Q29 | P | unique schedule ('P', 'Q', 'S', 'R') | Checked by enumeration or assertion |
| R1-Q30 | Green is not at the top | 3 stackings; all satisfy the claim | Checked by enumeration or assertion |
| R1-Q31 | 6 | enumeration of 32 on/off patterns | Checked by arithmetic or formula |
| R1-Q32 | 60 | enumeration of grid-line pairs (4 horizontal, 5 vertical lines) | Checked by enumeration or assertion |
| R1-Q33 | 54 | enumeration of 125 cubes | Checked by arithmetic or formula |
| R1-Q34 | 10 | n(n-3)/2 = 35 | Checked by arithmetic or formula |
| R1-Q35 | 204 | sum of k^2, k=1..8 | Checked by arithmetic or formula |
| R1-Q36 | 6 | all opposite-pair structures with 1 adjacent to 2,3,4,5: only 6 remains | Checked by enumeration or assertion |
| R1-Q37 | 72 | enumeration 1..120 | Checked by arithmetic or formula |
| R1-Q38 | 9 and 47 | bounds: max(0, 52+47-90) to min(52,47) | Checked by arithmetic or formula |
| R1-Q39 | 120 | regions p=65,q=30,r=25,pq=30,qr=20,pr=15,t=10,none=5 | Checked by arithmetic or formula |
| R1-Q40 | Drawing the gold coin is possible, but its probability is 1/100. | P(gold) = 1/100: possible (>0) and not certain (<1) | Checked by arithmetic or formula |
| R1-Q41 | 60 | 6!/(3!2!) | Checked by arithmetic or formula |
| R1-Q42 | 5/14 | C(5,2)/C(8,2) | Checked by arithmetic or formula |
| R1-Q43 | 7 | pigeonhole worst case | Checked by arithmetic or formula |
| R1-Q44 | 43 | C(10,2) minus 2 excluded pairs | Checked by arithmetic or formula |
| R1-Q45 | 42.55% | Y 2023 / (X+Y) 2023 = 100/235 | Checked by arithmetic or formula |
| R1-Q46 | 16 | averages 58 and 42 | Checked by arithmetic or formula |
| R1-Q47 | 5.00 percentage points | shares 35.0% and 40.0% | Checked by arithmetic or formula |
| R1-Q48 | 180 | {'Tea': 360.0, 'Coffee': 540.0, 'Juice': 450.0, 'Water': 450.0} | Checked by arithmetic or formula |
| R1-Q49 | 72.20 | weighted mean | Checked by arithmetic or formula |
| R1-Q50 | 108.75% | 5220/4800 | Checked by arithmetic or formula |
| R1-Q51 | Tech, 20% | budget per staff then female share | Checked by arithmetic or formula |
| R1-Q52 | Bhanu | Farah > Chirag > Bhanu > Eshan > Asha > Divya | Checked by arithmetic or formula |
| R1-Q53 | 9 | unique grid [(8, 1, 6), (3, 5, 7), (4, 9, 2)] | Checked by enumeration or assertion |
| R1-Q54 | T | 2 timetables; 10 o'clock train fixed | Checked by enumeration or assertion |
| R1-Q55 | Gamma | Beta > Alpha > Gamma > Delta > Epsilon > Zeta | Checked by arithmetic or formula |
| R1-Q56 | 3 | ACD ; ADE ; BCD | Checked by arithmetic or formula |
| R1-Q57 | Pune | 2 schedules; Tuesday fixed | Checked by enumeration or assertion |
| R1-Q58 | 150 | optimum ('B', 'C', 'D') | Checked by arithmetic or formula |
| R1-Q59 | Jas works on night 1 | unique rota ('Jas', 'Ila', 'Kira') | Checked by enumeration or assertion |
| R1-Q60 | B | exactly one true statement only if culprit is B | Checked by enumeration or assertion |

### R2 item keys

| ID | Key | How the key was verified (script function) | Determinacy |
|---|---|---|---|
| R2-Q01 | II only | model search, 4 attributes | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R2-Q02 | I only | model search | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R2-Q03 | The sponsor was not found | truth table over 4 atoms | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R2-Q04 | A quorum was present | truth table | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R2-Q05 | A is false | truth table over 4 atoms: not D -> not B -> not A; C or A forces C | Exhaustive model search (all models of up to 4 individuals, or all truth assignments) |
| R2-Q06 | CQDX | letter i shifted by its position i | Checked by arithmetic or formula |
| R2-Q07 | 5 | odd-place sum minus even-place sum: 22 - 17 | Checked by arithmetic or formula |
| R2-Q08 | 3 | 5 # (-1) = 5 + 2(-1) | Checked by arithmetic or formula |
| R2-Q09 | 6 | reverse values; odd places minus even places | Checked by arithmetic or formula |
| R2-Q10 | MLQ | 4 consistent rules, same output | Checked by enumeration or assertion |
| R2-Q11 | 42 | n(n+1) for n = 1..6 | Checked by arithmetic or formula |
| R2-Q12 | EV | first letter +1; second letter -1 (alphabet positions) | Checked by arithmetic or formula |
| R2-Q13 | 120 | alternating +1 and x3: 40 x 3 | Checked by arithmetic or formula |
| R2-Q14 | 126 | n^3 + 1, n = 5 | Checked by arithmetic or formula |
| R2-Q15 | 47 | differences 2,4,6,8,10,12 | Checked by arithmetic or formula |
| R2-Q16 | Cousin | Hand chain (explicit edges): P-Q spouses; R daughter of both; T brother of Q; S son of T -> S and R first cousins. | Determined by the stated relations (no free choice) |
| R2-Q17 | Aunt by marriage | Hand chain (explicit edges): Y father F; U brother of F (Y uncle); X spouse of U -> X aunt by marriage. | Determined by the stated relations (no free choice) |
| R2-Q18 | Uncle by marriage | Hand chain (explicit edges): Mohan father F; F mother Leela; Leela daughter Gita (paternal aunt); Hari spouse of Gita -> Hari uncle by marriage. | Determined by the stated relations (no free choice) |
| R2-Q19 | Nephew by marriage | Hand chain (explicit edges): A father of B and C; D wife of C; E son of B -> D is B sister-in-law; E is D nephew by marriage. | Determined by the stated relations (no free choice) |
| R2-Q20 | 13 m | end at (5,-12) | Checked by arithmetic or formula |
| R2-Q21 | 11 km, north-east | end (7.78,7.78) | Checked by arithmetic or formula |
| R2-Q22 | 15 km north | end (0,15) | Checked by arithmetic or formula |
| R2-Q23 | South-east | heading 135 degrees | Checked by arithmetic or formula |
| R2-Q24 | C | 2 seatings; seat 6 fixed | Checked by enumeration or assertion |
| R2-Q25 | 336 | brute force over 6! seatings, first person fixed | Checked by enumeration or assertion |
| R2-Q26 | Ajay | unique: {'Ajay': 2, 'Bina': 4, 'Chetan': 3, 'Dev': 1} | Checked by enumeration or assertion |
| R2-Q27 | N | unique ranking K M N O L | Checked by enumeration or assertion |
| R2-Q28 | Q | unique: {'P': 1, 'Q': 2, 'R': 4, 'S': 3} | Checked by enumeration or assertion |
| R2-Q29 | Green | 7 stackings; tops possible ['Blue', 'Red', 'Yellow'] | Checked by enumeration or assertion |
| R2-Q30 | 30 | sum of k^2 placements for 4x4 | Checked by arithmetic or formula |
| R2-Q31 | 64 | interior cubes (n-2)^3 | Checked by arithmetic or formula |
| R2-Q32 | 1 | opposite-pair structures with 2 adjacent to 3,4,5,6: only 1 remains | Checked by enumeration or assertion |
| R2-Q33 | 23 | C(8,2) pairs, collinear four give one line, not six | Checked by arithmetic or formula |
| R2-Q34 | 45 | C(3,2) x C(6,2) for 2 rows by 5 columns | Checked by arithmetic or formula |
| R2-Q35 | 45 | union 145, none 5, exactly two = pairwise minus triple each | Checked by arithmetic or formula |
| R2-Q36 | 90 | neither = 200 - /union/; union at least 110, so neither at most 90 | Checked by arithmetic or formula |
| R2-Q37 | 5% | min overlap = 60 + 45 - 100 | Checked by arithmetic or formula |
| R2-Q38 | 35 | men 50, men managers 15 | Checked by arithmetic or formula |
| R2-Q39 | 60 | brute force over ordered 4-digit strings from 0-4: last digit even, first digit nonzero | Checked by enumeration or assertion |
| R2-Q40 | 5/12 | prime sums: 15 of 36 outcomes | Checked by arithmetic or formula |
| R2-Q41 | 11 | worst case without 2 red and 2 blue is 10 | Checked by arithmetic or formula |
| R2-Q42 | 1/221 | 4/52 x 3/51 | Checked by arithmetic or formula |
| R2-Q43 | +3.5% | 92 x 0.9 = 82.8 vs 80 | Checked by arithmetic or formula |
| R2-Q44 | Q2 | Q1 45.45% ; Q2 53.57% ; Q3 56.25% ; Q4 53.12% | Checked by arithmetic or formula |
| R2-Q45 | +8% | 1.2 x 0.9 = 1.08 | Checked by arithmetic or formula |
| R2-Q46 | 66.67% | ratio 1.5 to 2.5 | Checked by arithmetic or formula |
| R2-Q47 | 80 | five x 72 minus four known 280 | Checked by arithmetic or formula |
| R2-Q48 | Unchanged at 300 | both years 300 | Checked by arithmetic or formula |
| R2-Q49 | 70 | weighted by staff: (2400 + 1800)/60 | Checked by arithmetic or formula |
| R2-Q50 | D | B > A > D > C > E | Checked by arithmetic or formula |
| R2-Q51 | 2 | unique grid [('A', 'B', 'C'), ('C', 'A', 'B'), ('B', 'C', 'A')]; C in rows 1-2 = 2 | Checked by enumeration or assertion |
| R2-Q52 | T | unique weights {'P': 3, 'Q': 2, 'R': 1, 'S': 4, 'T': 5} | Checked by enumeration or assertion |
| R2-Q53 | L1 | unique lecture order L1 L4 L2 L3 | Checked by enumeration or assertion |
| R2-Q54 | Bala | 2 rotas; day 2 fixed | Checked by enumeration or assertion |
| R2-Q55 | X | final counts W 33, X 34.2, Y 32.8 | Checked by arithmetic or formula |
| R2-Q56 | 75 | optimum pair ('A', 'B') | Checked by arithmetic or formula |
| R2-Q57 | A only | A knight, B and C knaves | Checked by arithmetic or formula |
| R2-Q58 | D | orders ADBC and ADCB: the second task is always D | Checked by enumeration or assertion |
| R2-Q59 | 2 | derangements of three: 2 | Checked by arithmetic or formula |
| R2-Q60 | Getting no head is possible, but its probability is only 1/8. | P(TTT) = 1/8: possible but improbable | Checked by arithmetic or formula |

## 4. Items revised during authoring, and cue exceptions

Revised before release (the first drafts were wrong or weak; the final text is the one in the folder):

- R1-Q12: the first draft asked for the next term of an interleaved series and keyed 29; the odd and even subsequences were recomputed and the stem now asks for the 8th term, keyed 11.
- R1-Q25: the redundant constraint "R is not next to P" was dropped; the three remaining constraints give 4 seatings (two mirror pairs), and the distractors were recomputed (drop U rule: 8; drop S-T rule: 20; mirror pairs identified: 2).
- R1-Q26 and R1-Q28: the first constraint sets gave 0 and 28 solutions; they were replaced by sets that give 2 solutions each, with the asked fact fixed across both.
- R1-Q30: the first draft included "Red is above Yellow" as a stem condition, which made the keyed statement a restatement; replaced by a stem with three conditions and the keyed statement "green is not at the top", which holds in all three stackings.
- R1-Q36 (cube faces) and R1-Q40 (possible versus probable) replaced a triangle count and a two-set Venn count, to cover owner rows that had no item in this bank.
- R1-Q53: the grid was made unique by fixing the bottom-right cell at 2 (brute force gives one grid).
- R2-Q02 and R2-Q03: the first statement sets had no must-true option or a duplicate answer; both were redesigned and recomputed.
- R2-Q05: the premise "if C is not the case, then A" was first encoded as "if C then A"; the encoding was corrected and the key re-derived (A is false; C is forced true, which is not offered).
- R2-Q26, R2-Q27, R2-Q28, R2-Q52, R2-Q53: constraint sets were searched for a unique solution before the stems were fixed.
- R2-Q32 (cube faces), R2-Q39 (four-digit even numbers with no leading zero) and R2-Q60 (possible versus probable) replaced a triangle count, a restricted-string count and a panel count, for the same owner-coverage reason as R1-Q36 and R1-Q40.
- R2-Q57: the explanations of the three rejected options were rewritten so that each names the statement that fails for that option.

Cue exceptions, kept and disclosed: the correct option is the uniquely longest option in R1-Q04 and R1-Q27 and in R2-Q03, R2-Q17, R2-Q18, R2-Q19 and R2-Q46; it is the uniquely shortest option in R1-Q03, R1-Q41, R1-Q47, R1-Q57, R2-Q02, R2-Q07, R2-Q09 and R2-Q48. These are within the two-in-sixty and five-in-sixty ceilings in section 2, but they are the items most exposed to a length cue and should be rebalanced before the bank is used as a graded instrument.

Items whose stems carry an interpretive choice that a reader could contest, flagged for review: R1-Q08 (BODMAS convention is stated in the stem, but the decoded expression depends on reading "left to right" for equal ranks), R1-Q25 (round-table convention: mirror images counted as distinct, rotations identical; stated), R2-Q21 (path-versus-displacement reading; stated as "how far from the starting point"), R2-Q55 (ballot rule: the transfer and the "most votes after transfer" rule are stated but a real election has more rules, so the item is an abstraction).

## 5. Checks not passed or not yet performed

- Relation items (R1-Q16 to R1-Q19, R2-Q16 to R2-Q19) are verified by hand-derived edge chains, not by a brute-force family-graph search.
- The 25% length band (section 2) is not met for 22 items in revision-1 and 27 in revision-2.
- No second-person independent review has been recorded for this pass; the record above is a single-pass check.
- Exact UPSC PYQs are not reproduced or keyed in either set. The local 2024 and 2025 Set-A keys are supplied scans whose official status is not certified, and the 2026 key is provisional; the owner files state that no PYQ answer is inferred. Routes to those PYQ families are listed in `COVERAGE.md`.

## 6. Status

Revision-1 and revision-2 meet the computational and format checks in sections 1 to 3. Revision-3 was reconciled and re-verified in pass 2 (section 7). The folder is **not** marked complete: the 25% length band is not met for 22 (R1), 27 (R2) and 19 (R3) items, the cue exceptions in section 4 were not rebalanced, and interpretive items await second-person review (`COVERAGE.md` section 5).

## 7. Pass-2 reconciliation and re-verification of revision-3 (2026-11-01)

Scope: `revision-3/QUESTIONS.md` and `revision-3/ANSWERS.md` (62 items), reconciled with `COVERAGE.md`, plus the length and letter statistics for all three sets. Revision-1 and revision-2 keys were not re-derived in this pass; their statistics are recomputed in section 7.4.

### 7.1 Method

- An independent Python checker, separate from the first agent's engine, was written outside the repository at `/tmp/mcq_audit/csat06_r3_recheck/` (`parse.py`, `solve.py`, `solve2.py`, `solve3.py`, `design.py`). It parses the printed QUESTIONS and ANSWERS text, so it checks what a learner reads, not an internal data record.
- Each key was recomputed by brute force where the space allows: all permutations for seating and ranking (120 row orders, 5040 anchored circular orders), all 4-digit and 3-digit numbers, all integers 1 to 100 and 100 to 300, all 36 dice rolls, all 125 cube cells, and all Venn region sets for the syllogisms (for example 192 models for the four-class item R3-Q02). Exact `Fraction` arithmetic was used for probability and DI.
- Every checked item reports one true option equal to the printed key (`FAILED: []` in the last run of `solve2.py`; `solve3.py` for the replaced items).

### 7.2 Re-verification record (all 62 items)

| ID | Pass-2 check | Computed result | Key |
|---|---|---|---|
| R3-Q01 | enumerate 6 pairs against both rules | only Asha and Chitra qualify | A |
| R3-Q02 | Venn, 4 classes, 192 models | only B holds in all models | B |
| R3-Q03 | Venn, 4 classes, 64 models | only C holds | C |
| R3-Q04 | Venn, 3 classes, 8 models | only D holds | D |
| R3-Q05 (revised) | 8 truth-worlds of (i) to (iii) | only A forced; B, C false; D (approval possible) false | A |
| R3-Q06 | Venn, 3 classes, 16 models | I forced, II not forced | B |
| R3-Q07 | Fraction: (2/10) x (1/9) | 1/45 | C |
| R3-Q08 (revised) | 4 truth-worlds; D forced; A not forced (sample may be untested) | only D forced; C is refuted by another rejected Batch B sample that passed | D |
| R3-Q09 | gaps 3, 4, 5, next gap 6, position 20 | T | A |
| R3-Q10 | x to 2x+1 on every term; next 95 | 95 | B |
| R3-Q11 | 27 minus position, then reverse; both given examples reproduced | DLMH | C |
| R3-Q12 | 24 / 6 x 3 + 5 - 2 | 15 | D |
| R3-Q13 | letter sums: GAIN 31; DAY 30; MEN 32; ROAD 38 | GAIN | A |
| R3-Q14 | squares of primes 2, 3, 5, 7; next 11 squared | 121 | B |
| R3-Q15 | t7 = 13, t8 = 16 | 29 | C |
| R3-Q16 | 27 minus position, reversed; CAT and BIRD reproduce | 23-9-18-25 | D |
| R3-Q17 | displacement: (0,9), (5,9), (5,0), (8,0) | 8 km East | A |
| R3-Q18 | three clockwise then two anticlockwise quarter turns from East | South | B |
| R3-Q19 | hand edge chain (R father of P, P mother of S) | maternal grandfather | C |
| R3-Q20 | search over boys and girls up to 30 | (4 boys, 3 girls), total 7 | D |
| R3-Q21 | displacement: (0,3), (4,3), (4,6), (0,6) | 6 km North | A |
| R3-Q22 | all 120 row orders; one solution Q, T, P, R, S | seat 3 = P | B |
| R3-Q23 | all 5040 anchored circular orders; one solution A, H, C, G, B, D, E, F | left of A = F | C |
| R3-Q24 | all 120 row orders; 8 seatings; P in seat 1 in 4, R in seat 2 in 2, T in seat 4 in 2 | only Q in seat 5 holds in every seating | D |
| R3-Q25 | all 120 orderings; 3 valid; A taller than C in all | only A holds | A |
| R3-Q26 | all 120 row orders; one seating (Hari, Gita, Kiran, Lata, Mohan) | codes sum to 38 | B |
| R3-Q27 | anchored circular count with A and B adjacent: 2 x 4! | 48 | C |
| R3-Q28 | 8! / (2! 3!) | 3360 | D |
| R3-Q29 | enumeration of 4-digit numbers from {0..5}, no repeat, ending 0 or 5 | 108 | A |
| R3-Q30 | C(10,4) - C(6,4) - C(4,4) | 194 | B |
| R3-Q31 | worst case: 2 of each of four colours, then one more | 9 | C |
| R3-Q32 | 4^2 + 3^2 + 2^2 + 1^2 | 30 | D |
| R3-Q33 | enumeration of the 5 x 5 x 5 cells with exactly two painted faces | 36 | A |
| R3-Q34 | enumeration of 1 to 100 | 39 | B |
| R3-Q35 | 48 + 40 - 75 | 13 | C |
| R3-Q36 | exactly one = 180 - 2(75) + 3(10); totals reconcile to 120 | 60 | D |
| R3-Q37 | enumeration of 3-digit even numbers from {1..5} | 24 | A |
| R3-Q38 | (C(5,2) + C(3,2)) / C(8,2) | 13/28 | B |
| R3-Q39 | 1 - (5/6)^3 | 91/216 | C |
| R3-Q40 | enumeration of 36 rolls: total at least 10 or equal faces | 10/36 = 5/18 | D |
| R3-Q41 | 10 women of 16 Economics students | 5/8 | A |
| R3-Q42 | 15 of 37 trained | 15/37 | B |
| R3-Q43 | revenue per thousand units 3.0 to 2.8 | -6.7% | C |
| R3-Q44 | 8 points; 8/22 relative | +36.4% relative | D |
| R3-Q45 | 40% minus 35% of 480 | 24 | A |
| R3-Q46 | 200 x 0.8 x 1.25 | 200 (no change) | B |
| R3-Q47 | 0.4 test + 0.6 interview: Asha 80, Bilal 77, Chitra 70, Dev 52 | Asha | C |
| R3-Q48 | revenue per thousand units 2.0 to 1.8 | -0.2 lakh | D |
| R3-Q49 | X's share 40% to 50%; X revenue 500 to 450; total 1250 to 900 | only A holds | A |
| R3-Q50 | (120 - 100) / 100 | 20% | B |
| R3-Q51 | sorted 90, 120, 140, 150: median 130, mean 125 | 5 | C |
| R3-Q52 | 420 x 360 / 84 | 1800 | D |
| R3-Q53 | enumeration of 3-letter arrangements of PLANT with a vowel first | 12 | A |
| R3-Q54 | hypotenuse of 6 and 8 | 10 km | B |
| R3-Q55 | rules applied to P, Q, R, S | P and R | C |
| R3-Q56 (replaced) | 24 day orders: 9 derangements; 6 with P and Q on consecutive days | 6 | C |
| R3-Q57 (replaced) | 8 truth-teller assignments | only Y truthful | B |
| R3-Q58 | n(n - 3) / 2 with n = 8 | 20 | B |
| R3-Q59 | multiples of 7 (28) minus multiples of 21 (10) | 18 | C |
| R3-Q60 | enumeration of 120 arrangements of TRAIN with consonant first and vowel last | 36 | D |
| R3-Q61 | 9 x 8 x 7 | 504 | A |
| R3-Q62 | worst case: one of each of three colours, then one more | 4 | B |

Items verified by definition and reasoning rather than search: R3-Q19 (relation chain), R3-Q14 (pattern), R3-Q18 and R3-Q21 (turn bookkeeping, also computed). No item has more than one true option under the computed truth.

### 7.3 Revisions made in pass 2

- **R3-Q05**: the stem said "Four statements" over three numbered statements (corrected to "Three statements"); options rewritten to the same length band (ratio 1.8 reduced to about 1.2). Key A unchanged.
- **R3-Q08**: the keyed option was a possibility claim ("could have passed and still been rejected") that a reader could contest under "necessarily true". The item now says "Sample 14 was not rejected" and asks which statement must be true; key D (did not fail) is the contrapositive. Key letter unchanged.
- **R3-Q22** (ANSWERS only): the explanation said S was forced into seat 5 by clue (e); the correct reason is elimination after Q is placed in seat 1. Key B unchanged.
- **R3-Q23** (ANSWERS only): the option-by-option explanation was attached to the wrong letters (the paragraph headed "C (key)" described option D). Rewritten against the printed options: A = D, B = G, C = F (key), D = H.
- **R3-Q56**: replaced. The original was a communication item (double-barrelled questionnaire) that belongs to Topic 07. The new item is a forbidden-day assignment with an adjacency rule (row 28), key C = 6, options 12, 9, 6, 3 (in descending order), with distractors named for each error (12 ignores the forbidden-day rules; 9 ignores the adjacency rule; 3 reverses the adjacency rule).
- **R3-Q57**: replaced. The original was a communication barrier item (Topic 07 boundary). The new item is a three-witness truth-teller puzzle (row 27), with a unique solution (only Y truthful), key B.

Letter balance after pass 2: A 15 (24.2%), B 17 (27.4%), C 16 (25.8%), D 14 (22.6%).

### 7.4 Length and letter statistics, all three sets

Measured on the printed QUESTIONS and ANSWERS text (character count of each option; "uniquely longest" means the keyed option is strictly longer than the other three).

| Measure | Revision-1 | Revision-2 | Revision-3 (after pass 2) | Target |
|---|---|---|---|---|
| Correct option uniquely longest | 2 of 60 (3.3%) | 5 of 60 (8.3%) | 3 of 62 (4.8%) | about 25% or less: met in all sets |
| Longest option within 25% of shortest | 38 of 60 (63.3%) | 33 of 60 (55.0%) | 43 of 62 (69.4%) | target: not met for 22, 27 and 19 items |
| Letters A / B / C / D | 15 / 15 / 15 / 15 (25.0% each) | 15 / 15 / 15 / 15 (25.0% each) | 15 / 17 / 16 / 14 (24.2 / 27.4 / 25.8 / 22.6%) | each 20 to 30%: met |
| Items with a ratio above 1.5 | 14 | 15 | 10 | numeric and fraction outliers |

Revision-3 items above a ratio of 1.5 (all numeric, fraction or name options; the length follows digit count): R3-Q31, Q35, Q36, Q38, Q39, Q42, Q47, Q50, Q51 and Q56. R3-Q05 (ratio 1.8) is no longer an outlier.

### 7.5 Status after pass 2

Revision-3 passes the key, format, uniqueness, letter and uniquely-longest checks. The topic stays `in_progress` (reasons in `COVERAGE.md` section 5): the 25% length band is not met for 22, 27 and 19 items in the three sets; the R1 and R2 exceptions in section 4 were not rebalanced; interpretive items (section 4 above and `COVERAGE.md` section 4) await a second-person review; and owner gaps remain in `COVERAGE.md` section 4.

## 8. Original revision-3 record (merged from AUDIT-revision-3.md, first pass)

Recorded by the second agent before pass 2. Superseded where section 7 says so: the R3-Q05, R3-Q08, R3-Q23, R3-Q56 and R3-Q57 entries in sections 8.2 and 8.5 are replaced by section 7.3; the option-length counts in section 8.4 are replaced by section 7.4. The remaining entries stand.

Date of verification: 2026-11-01. Scope: `revision-3/QUESTIONS.md` and `revision-3/ANSWERS.md` only (62 original items, `R3-Q01` to `R3-Q62`). Revision 1, Revision 2, `COVERAGE.md` and `AUDIT.md` were not read for content and were not edited. No UPSC PYQ wording or option is reproduced, and no item is labelled as a PYQ.

### 8.1 Method

- Every item was written as a data record with four options, a keyed letter, and a truth function that evaluates **each of the four options** by computation (brute-force enumeration, exact `Fraction` arithmetic, or a closed-form count checked by enumeration). The build asserts, for all 62 items, that exactly one option is true and that it is the keyed option. The full build failed the first time on a wrong mirror-letter formula (Q11) and a direction-name mismatch (Q18); both were fixed and re-run.
- Puzzle uniqueness: arrangement and circular items (Q22 to Q27) were checked by enumerating every permutation and counting the solutions that satisfy the stated clues. Q22, Q23 and Q26 each have exactly one solution. Q24 has eight seatings and the keyed statement holds in all eight. Q25 has three orderings and the keyed statement holds in all three.
- Syllogisms and conclusion items (Q02 to Q06) were checked by enumerating every Venn region configuration for three or four classes (up to 2^16 region sets). "Follows" means true in every configuration satisfying the premises.
- Conditional and propositional items (Q05, Q08) were checked over all truth-value worlds.
- Counting items were checked by direct enumeration where the space is small (4-digit, 3-digit, 1 to 100, 100 to 300, 36 rolls, permutations of PLANT) and by formula otherwise, with the formula asserted against the enumerated value where feasible (for example Q28, Q34, Q29, Q37, Q59).
- Probability and DI items use `fractions.Fraction` or exact arithmetic, and each computed value is asserted against the key before rendering.
- Engine and build scripts are at `/tmp/mcq_audit/csat06_r3/` (`engine.py`, `items_a.py` to `items_d.py`, `build.py`, `render.py`). They are outside the repository and were not added to it.

### 8.2 Per-item verification table

Truth vector: the computed truth value of each option A to D, in displayed order. `T` marks a true option; the single `T` is the key.

| ID | Category | Method | Key | Truth vector A-D (keyed option) | Time target (s) |
|---|---|---|---|---|---|
| R3-Q01 | Logic + table + count | enumerate all 6 pairs against both rules | A | TFFF | 80 |
| R3-Q02 | Syllogism (Venn, four classes) | Venn models, 4 classes (2^16 region sets) | B | FTFF | 75 |
| R3-Q03 | Syllogism with existential premise | Venn models, 4 classes | C | FFTF | 75 |
| R3-Q04 | Syllogism + necessity test | Venn models, 3 classes | D | FFFT | 75 |
| R3-Q05 | Conditional chain | propositional worlds (8) | A | TFFF | 60 |
| R3-Q06 | Syllogism (two conclusions) | Venn models, 3 classes, both conclusions | B | FTFF | 70 |
| R3-Q07 | Probability vs possibility | Fraction arithmetic | C | FFTF | 60 |
| R3-Q08 | Necessity vs possibility | propositional worlds (4) | D | FFFT | 60 |
| R3-Q09 | Letter series (growing gaps) | exact arithmetic / closed form | A | TFFF | 55 |
| R3-Q10 | Numeric series (recurrence) | exact arithmetic / closed form | B | FTFF | 55 |
| R3-Q11 | Coding (mirror and reverse) | exact arithmetic / closed form | C | FFTF | 70 |
| R3-Q12 | Operator substitution | exact arithmetic / closed form | D | FFFT | 70 |
| R3-Q13 | Letter-value coding | exact arithmetic / closed form | A | TFFF | 60 |
| R3-Q14 | Series (squares of primes) | exact arithmetic / closed form | B | FTFF | 55 |
| R3-Q15 | Interleaved series | exact arithmetic / closed form | C | FFTF | 70 |
| R3-Q16 | Coding (value and reversal) | exact arithmetic / closed form | D | FFFT | 70 |
| R3-Q17 | Directions (displacement) | exact arithmetic / closed form | A | TFFF | 75 |
| R3-Q18 | Facing and turns | exact arithmetic / closed form | B | FTFF | 55 |
| R3-Q19 | Blood relation | definitional (no computation; see limitations) | C | FFTF | 65 |
| R3-Q20 | Relations (sibling counting) | search over boys/girls counts | D | FFFT | 75 |
| R3-Q21 | Directions (turns and distance) | exact arithmetic / closed form | A | TFFF | 70 |
| R3-Q22 | Linear arrangement (unique) | all 120 row orders | B | FTFF | 90 |
| R3-Q23 | Circular arrangement (anchored) | all 5040 anchored circular orders | C | FFTF | 100 |
| R3-Q24 | Row arrangement (must-be-true) | all row orders; 8 valid seatings | D | FFFT | 90 |
| R3-Q25 | Ranking (forced comparison) | all 120 orderings; 3 valid | A | TFFF | 75 |
| R3-Q26 | Arrangement with coding twist | all 120 row orders; 1 valid | B | FTFF | 100 |
| R3-Q27 | Circular count (adjacency) | all 120 anchored circular orders | C | FFTF | 80 |
| R3-Q28 | Arrangements with repeats | exact arithmetic / closed form | D | FFFT | 70 |
| R3-Q29 | Constrained numbers (leading zero) | all 4-digit numbers 1000-9999 | A | TFFF | 90 |
| R3-Q30 | Committee (complement with restriction) | exact arithmetic / closed form | B | FTFF | 80 |
| R3-Q31 | Worst-case draw | exact arithmetic / closed form | C | FFTF | 70 |
| R3-Q32 | Figure count (by size) | exact arithmetic / closed form | D | FFFT | 60 |
| R3-Q33 | Painted cube (layer count) | exact arithmetic / closed form | A | TFFF | 80 |
| R3-Q34 | Inclusion-exclusion (three sets) | all integers 1-100 | B | FTFF | 95 |
| R3-Q35 | Set overlap (minimum) | exact arithmetic / closed form | C | FFTF | 60 |
| R3-Q36 | Set counts (exactly one of three) | exact arithmetic / closed form | D | FFFT | 95 |
| R3-Q37 | Constrained numbers (parity) | all 3-digit numbers | A | TFFF | 75 |
| R3-Q38 | Probability (without replacement, same colour) | exact arithmetic / closed form | B | FTFF | 70 |
| R3-Q39 | Complement (at least one) | exact arithmetic / closed form | C | FFTF | 60 |
| R3-Q40 | Dice (union with overlap) | all 36 rolls | D | FFFT | 75 |
| R3-Q41 | Conditional probability (reverse trap) | exact arithmetic / closed form | A | TFFF | 70 |
| R3-Q42 | Table conditional probability | exact arithmetic / closed form | B | FTFF | 85 |
| R3-Q43 | DI (per-unit change in percent) | exact arithmetic / closed form | C | FFTF | 90 |
| R3-Q44 | DI (percentage points vs relative change) | exact arithmetic / closed form | D | FFFT | 75 |
| R3-Q45 | DI (pie shares in money) | exact arithmetic / closed form | A | TFFF | 85 |
| R3-Q46 | DI (successive percentage changes) | exact arithmetic / closed form | B | FTFF | 75 |
| R3-Q47 | DI (weighted score) | exact arithmetic / closed form | C | FFTF | 80 |
| R3-Q48 | DI (per-unit level, dual axis) | exact arithmetic / closed form | D | FFFT | 80 |
| R3-Q49 | DI (level vs share) | exact arithmetic / closed form | A | TFFF | 90 |
| R3-Q50 | DI (base year in percentage change) | exact arithmetic / closed form | B | FTFF | 70 |
| R3-Q51 | DI (median vs mean) | exact arithmetic / closed form | C | FFTF | 80 |
| R3-Q52 | DI (pie angle to total) | exact arithmetic / closed form | D | FFFT | 75 |
| R3-Q53 | Mixed: restricted words | all permutations of PLANT | A | TFFF | 75 |
| R3-Q54 | Mixed: directions and distance | exact arithmetic / closed form | B | FTFF | 60 |
| R3-Q55 | Mixed: table and conditional rules | rule evaluation on 4 candidates | C | FFTF | 100 |
| R3-Q56 | Communication: questionnaire design | definitional (no computation; see limitations) | D | FFFT | 60 |
| R3-Q57 | Communication: barrier identification | definitional (no computation; see limitations) | A | TFFF | 60 |
| R3-Q58 | Sprint: polygon diagonals | exact arithmetic / closed form | B | FTFF | 45 |
| R3-Q59 | Sprint: divisibility count | all integers 100-300 | C | FFTF | 60 |
| R3-Q60 | Sprint: arrangement with end conditions | exact arithmetic / closed form | D | FFFT | 60 |
| R3-Q61 | Sprint: ordered posts | exact arithmetic / closed form | A | TFFF | 60 |
| R3-Q62 | Sprint: worst-case draw (three colours) | exact arithmetic / closed form | B | FTFF | 50 |


### 8.3 Uniqueness and key checks (summary)

- Items with exactly one true option under computed truth: **62 of 62**.
- Keyed letters: A 16 (25.8%), B 16 (25.8%), C 15 (24.2%), D 15 (24.2%). Every letter sits inside the 20 to 30 per cent band.
- Items whose option-level truth was checked by a rule evaluation rather than a brute-force search: Q19, Q56, Q57 (see limitations).

### 8.4 Option-length and cue balance (this set)

| Measure | Result | Target |
|---|---|---|
| Correct option is the uniquely longest | 5 of 62 (8.1%) | at most about 25% |
| Longest option within 25% of the shortest (character count) | 41 of 62 (66.1%) | as many as possible |
| Items where the ratio exceeds 1.5 | Q05 (prose; 1.8); Q31, Q35, Q36, Q51 (numerals; 2.0 to 3.0); Q39 (fractions; 2.3); Q38, Q42, Q50 (fractions or percentages; 1.7); Q47 (names; 2.0) | numeric, fraction and name options may differ in length by digit or letter count |
| No "all of the above", "none of the above" options | 0 items | 0 |
| Qualifier-only correct options | None found after revision; Q49, Q55 and Q44 options were length-matched | none |

The longest-option outliers are numeric or fraction sets, where length follows digit count and cannot be equalised without changing the values. Q05 is the only prose item with a ratio above 1.5. Its wording is fixed by the logical forms (the two false options are short, and the forced one and the false "may still be approved" option cannot be lengthened without adding a claim the premises do not support).

### 8.5 Revisions made during the audit (all keys and stems re-verified afterwards)

- **Q11**: the first mirror-letter formula produced `KOZM` for PLAN, so the built-in example assertion failed; corrected to `155 - ord(letter)` and re-run.
- **Q18**: the direction list used letters while the truth list used names; corrected.
- **Q22**: the first clue set (a)-(d) left two solutions; clue (e) "Q sits to the left of S" added, giving one solution.
- **Q23**: the first clue set left two possible left neighbours (F and H); clue (f) "H is not next to E" added, giving one solution. The stem's 'right-hand neighbour when facing the centre' was wrong for a clockwise seat order and was replaced by an explicit definition ('to the right of' means the next clockwise seat).
- **Q24**: the first search found several forced facts; the chosen clue set makes "Q sits in seat 5" the only forced statement among the four options. Counts used in the explanation were recomputed (P in seat 1 in 4 of 8; R in seat 2 in 2 of 8; T in seat 4 in 2 of 8; R never in seat 3).
- **Q25**: the first version had two forced true options (A taller than C; C shortest), so the options were replaced.
- **Q26**: the first clue sets gave three or four solutions; clues (a) and (d) (Hari in seat 1; Lata in seat 4) make the order unique.
- **Q05**: a version with "if the minutes are published, the proposal was approved" was forced true by vacuous truth (minutes not published), so it was removed.
- **Q04**: the option "It is not necessary that ..." was reworded as "Not every medical-test passer must be an instructor" to match the other option lengths; the claim is unchanged.
- **Q08**: an option phrase "in the study" referred to a setting the stem never mentions; reworded.
- **Q33**: the stem said the cube was "made of 125 unit cubes" and was "cut into 125 unit cubes"; reworded to a side-5 cube cut into unit cubes.
- **Q36**: the first truth vector tested the wrong quantities; corrected to test each option against the exactly-one count (60).
- **Q24 explanation**, **Q29** (96 and 120 identified as the lost-digit and leading-zero errors), **Q37**, **Q31**: explanations rewritten where a distractor's error had been described loosely.
- **Option wording** changed for length balance only (Q03, Q04, Q06, Q08, Q19, Q25, Q49). No key changed in any of these edits.

### 8.6 Five hardest or most doubtful items

1. **Q23** (eight people, six clues, circular). Solvable in about 100 seconds, but a learner can misread the clockwise definition. The stem now defines it explicitly.
2. **Q24** (must-be-true over eight seatings). The keyed statement follows only from clue (c) (R cannot be in seat 3, so Q is in seat 5). A solver who checks only one seating may pick P in seat 1 or R in seat 2 by mistake.
3. **Q26** (coded arrangement with a sum of codes). Four steps: seat the row, then identify each left-hand neighbour, then map initials to positions. The distractor 43 is what the right-hand reading gives.
4. **Q08** (the keyed option is a possibility statement). Some readers take "necessarily true" to mean "true of sample 14", not "consistent with the facts". The explanation states the reading explicitly.
5. **Q05** (option-length outlier, ratio 1.8). The logic is clean (chain then contrapositive), but a test-taker may pick the longest option on length alone; the length balance is the weakest point of this item.

Also noted: Q55's rule (3) does not change the answer (S is excluded by rule 2 already). It is kept as a deliberate redundancy so that the rule set is complete, and it does not create a second correct answer.

### 8.7 Owner-row coverage in this set (for the coverage ledger)

| Owner technique (basic / advanced) | Revision 3 items |
|---|---|
| Implication, contrapositive, converse, equivalence | Q01, Q02, Q05, Q06 |
| Possible vs probable; "not necessary" | Q04, Q07, Q08 |
| Syllogism validity (conclusion in every diagram; existential "some") | Q02, Q03, Q04, Q06 |
| Series (differences, growing gaps, recurrence, interleaving, squares of primes) | Q09, Q10, Q14, Q15 |
| Coding: shift, mirror, reverse, position value, operator substitution, letter value | Q11, Q12, Q13, Q16 |
| Directions and turns (displacement, facing) | Q17, Q18, Q21 |
| Blood relations and sibling counting | Q19, Q20 |
| Linear and circular arrangement; forced vs multiple solutions; coded seating | Q22 to Q27 |
| Arrangements with repeats, leading zero, parity and digit constraints | Q28, Q29, Q37 |
| Permutation vs combination; committee with restriction; ordered posts | Q30, Q53, Q60, Q61 |
| Worst-case draws | Q31, Q62 |
| Figure counting by size; painted-cube layers | Q32, Q33 |
| Inclusion-exclusion; Venn bounds; exactly-one counts | Q34, Q35, Q36 |
| Probability: without replacement, complement, dice union, conditional, table conditional | Q38 to Q42 |
| DI: per-unit change, percentage points vs relative change, pie shares, successive changes, weighted values, dual axis, level vs share, base year, median vs mean, pie-to-total | Q43 to Q52 |
| Tables with conditional rules; directions and distance (mixed) | Q54, Q55 |
| Communication: questionnaire design (double-barrelled item); barrier identification | Q56, Q57 (boundary with Topic 07) |
| Polygon diagonals; divisibility-range count | Q58, Q59 |

Gaps in this set, stated honestly: no image-based figure or cube-net items (the set is text-only, so cube opposite-face inference from several views is not tested); no interpersonal decision scenarios beyond the two communication classification items (those belong to Topic 07); and no exact PYQ-pattern reproductions (none are permitted in this file).

### 8.8 Limitations

- **Q19, Q56, Q57** have keys verified by definition and explicit case reasoning, not by code. Q19 uses a three-person family chain that was checked by hand; Q56 and Q57 are classification items whose keys follow from the definitions in the owner.
- **Q51** (median vs mean) and **Q54** (Pythagoras) use elementary arithmetic and geometry that the owner does not state as rows. They are included as DI and distance arithmetic and are flagged in `ANSWERS.md` source notes.
- Keys are internally verified only. The set has not been checked against any official answer key, which is correct because none is reproduced here.
- Time targets (about 72 seconds per question, with block budgets adding to 75 minutes) are design targets, not measured learner times.
