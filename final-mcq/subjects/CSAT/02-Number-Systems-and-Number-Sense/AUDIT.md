# CSAT-02 original-bank item audit (2026-10-01)

Each entry `Qnn=independently obtained result` represents an individually checked question: the result was recomputed by elementary algebra, modular arithmetic, enumeration or a direct counterexample, then matched against all four choices and the corresponding A–D explanation in that revision's `ANSWERS.md`. ✓ means the keyed choice is unique, the stem is sufficiently determinate and its competitors received a qualitative pass. The keyed letter and source section remain in `ANSWERS.md` rather than this learner-adjacent ledger. This audit does **not** authenticate exact PYQs or by itself sign off the owner-source coverage rows.

## Revision 1 (65/65 checked; no item hold)

| IDs and independently established result | State |
|---|---|
| Q01=7/2 rational noninteger; Q02=x6; Q03=x8; Q04=d12; Q05=42; Q06=12; Q07=32; Q08=8; Q09=0; Q10=18/55 | ✓ each |
| Q11=368; Q12=83; Q13=30; Q14=a⁻²>a⁻¹; Q15=9; Q16=50; Q17=36; Q18=5; Q19=18; Q20=03 | ✓ each |
| Q21=6; Q22=zero whole/√2 irrational; Q23=2,5,9,10 but not 4; Q24=720; Q25=6; Q26=1001; Q27=37/300; Q28=84; Q29=3; Q30=0^(1/2) | ✓ each |
| Q31=6; Q32=x5; Q33=52; Q34=(9,5); Q35=4; Q36=42; Q37=(91,121); Q38=1; Q39=12⇒3 and 4; Q40=(45,square) | ✓ each |
| Q41=90; Q42=10; Q43=first triple only; Q44=19; Q45=9; Q46=45; Q47=41; Q48=1477; Q49=27/126=3/14; Q50=x>3⇒x²>9 | ✓ each |
| Q51=2; Q52=6; Q53=n4; Q54=10; Q55=3; Q56=9; Q57=47; Q58=5 | ✓ each |
| Q59=3375 (`(90/6)³`); Q60=5; Q61=second structure; Q62=1; Q63=14 | ✓ each; Q59 competitors now correspond to explicit prime-factor exponent errors |
| Q64=170 contributes digit 400; Q65=24 mod 40 | ✓ each; Q64 block `9+180+210` places 169's last digit at 399; Q65 periodic segment begins at n=3 and independently gives `24≡4 (mod 5)` with `8∣24` |

## Revision 2 (63/63 checked)

| IDs and independently established result | State |
|---|---|
| Q01=zero whole/rational; Q02=x1; Q03=63416; Q04=40; Q05=d24 under both bounds; Q06=24; Q07=28; Q08=2; Q09=5 distinct residues including transient; Q10=least n4 | ✓ each |
| Q11=4/11; Q12=0; Q13=63; Q14=110; Q15=4; Q16=66; Q17=1 surviving 2-adic factor; Q18=26 exponents; Q19=5; Q20=−4 integer/zero whole | ✓ each |
| Q21=4 digit choices; Q22=195; Q23=4 ordered pairs; Q24=3; Q25=9; Q26=n3; Q27=4; Q28=45; Q29=1/55; Q30=(0,9) | ✓ each |
| Q31=7; Q32=7 digit pairs; Q33=270; Q34=11; Q35=1; Q36=2; Q37=(nonreal, integer, irrational real); Q38=36; Q39=36; Q40=both odd | ✓ each |
| Q41=48; Q42=pairwise coprime; Q43=5; Q44=40 impossible; Q45=2; Q46=2 valid digits; Q47=8; Q48=11; Q49=999; Q50=4 | ✓ each |
| Q51=44; Q52=248; Q53=5; Q54=2; Q55=−15; Q56=1013; Q57=72; Q58=29; Q59=3; Q60=180 | ✓ each |
| Q61=4; Q62=(24,30) | ✓ each |
| Q63=54, witnessed by 93−39 | ✓; `a+b=12`, valid nonzero digits give maximum `a−b=6`; larger listed 72 requires invalid digit 10 |

## Revision 3 (63/63 checked)

| IDs and independently established result | State |
|---|---|
| Q01=2 only even prime; Q02=54; Q03=x9, 4 not 5; Q04=m4; Q05=360; Q06=d30; Q07=52; Q08=5; Q09=2; Q10=8 | ✓ each |
| Q11=31; Q12=3; Q13=25; Q14=1/2; Q15=80; Q16=21; Q17=3; Q18=1332; Q19=08; Q20=17 | ✓ each |
| Q21=2; Q22=always odd; Q23=5 rational/zero whole; Q24=990; Q25=84; Q26=6; Q27=(7,3) common; Q28=0; Q29=43; Q30=7 | ✓ each |
| Q31=11; Q32=236; Q33=2-and-5 but not 10 impossible; Q34=88; Q35=7/11; Q36=−7 integer/1 neither; Q37=2; Q38=2; Q39=24 impossible; Q40=(38,65) | ✓ each |
| Q41=81 impossible; Q42=15; Q43=756; Q44=(8,2); Q45=909; Q46=3; Q47=30; Q48=13; Q49=2716; Q50=5994 | ✓ each |
| Q51=133; Q52=n6; Q53=50; Q54=20; Q55=1206 impossible; Q56=4; Q57=1; Q58=216064; Q59=3; Q60=first structure | ✓ each |
| Q61=31320; Q62=4 unordered pairs | ✓ each |
| Q63=6 units digit | ✓; independent reductions give `8×7≡6 (mod 10)`; wrong alternatives correspond to first-bracket only, wrong 2-cycle, second-bracket only |

## Cross-revision decision audit

- Shared owner methods intentionally recur, but the decisive condition changes: R1-Q04 equal-remainder gcd, R2-Q05 residue-and-divisor **two-bound** maximisation, R3-Q06 fixed-remainder gcd, R3-Q27 simultaneous Euclidean pair; R1-Q07 factorial zeroes, R2-Q07 *difference* of zero counts, R3-Q12 *sum* of two factorial quotients with minimum valuation.
- R1-Q17 single-prime valuation `80!` differs from revised R2-Q17's **cancellation of two `32!` valuations from `64!`** and R3-Q29 combined `90!` 2/3-valuation with the **2-threshold binding**. The earlier R2-Q17 simply substituted a new prime/factorial into R1's calculation; the factorial-quotient decision replaces it. R1-Q19 joint repunit 9/11 minimum length differs from R2-Q48 single 11-divisibility and R3-Q31 repunit gcd.
- R1-Q11 pages across two digit-length blocks, R2-Q52 torn-sheet count, R3-Q49 count across three length blocks; R1-Q05 box side, R2-Q43 combined rope piece count, R3-Q42 rectangular square-tile count; R1-Q56 count ordered unit-fraction solutions, R2-Q57 maximal denominator, R3-Q54 minimal denominator sum. R1-Q57 now infers **two** leaves linked by page spacing, rather than the former one-subtraction stem; R2-Q58 infers **one** leaf from a remainder, R3-Q55 tests physical odd/even leaf feasibility.
- R1-Q64 asks which integer **contributes** a fixed concatenation digit; R2-Q12 asks for the **digit** at an index; R3-Q32 asks for the **last completed integer** under a fixed digit budget. R2-Q63 maximises a reversal difference given a fixed **sum**; R1-Q63 finds the digit sum and R3-Q62 counts unordered digit pairs. R3-Q63 multiplies compound unit-digit residues, whereas R1-Q45 reduces a signed power product and R2-Q08 multiplies two power residues. R1-Q65 evaluates an eventual **nonconstant** cycle at a distant exponent, R2-Q26 locates cycle onset, and R3-Q10 handles a tower with a pre-period.
- This blind pass found that R1-Q09 and the former R2-Q09 were the **same high-power-to-zero decision** with different constants. R2-Q09 now counts four eventual residues **plus** the distinct pre-period residue (five), unlike R1-Q65's remote-position evaluation and R3-Q10's tower. Former R2-Q46's unconditional divisor 3 required no digit decision; it now selects digit values by exact 3-adic valuation of a repeated block, unlike R1-Q26's universal 1001 divisor and R3-Q45's reversal-difference factor.
- Further same-calculation traps exposed by question-only reading: R1-Q18 vs former R2-Q10 both evaluated a coprime tower remainder; R2-Q10 now finds the **least tower level** that reaches a specific residue. R1-Q20 vs former R2-Q18 both found the last two digits of one distant power; R2-Q18 now counts **all matching exponents** in a bounded interval. R1-Q28 vs former R2-Q14 both complemented a union of two divisor sets; R2-Q14 now uses **three-set** inclusion–exclusion. R1-Q13 vs former R2-Q28 both counted exactly-one of two sets; R2-Q28 now counts exactly-one of **three** sets with shared triple overlap.

## Source-owner checklist signoff (rows 19–34 in COVERAGE.md)

Each row below was reconciled against its cited B/A section and inspected for a **different keyed decision** in R1, R2 and R3; the affirmative question IDs and per-revision contrasts are written in the corresponding `COVERAGE.md` row. `✓` means owner-subdetail coverage, *not* released-bank difficulty certification.

| Row | Distinct decision cross-check and any gap exposed/repaired | Owner coverage |
|---|---|---|
| 19 | R1 classifies rational noninteger/zero and a triple-consecutive product; R2 classifies negative integer/zero and a 5-to-9 product; R3 classifies radical quotient and tests consecutive-square residues/parity. | ✓ all three |
| 20 | R1 solves 11-digit variables and a 12-implication; R2 selects an 8-not-9 numeral and distinguishes 3-and-4 from 8; R3 tests negative signed-11, 2-and-6 false converse and the least 8-and-9 numeral. | ✓ all three |
| 21 | R1 counts constrained divisors and a square's 45 divisors; R2 counts square divisors and sums divisors; R3 finds a least 21-divisor multiplier and counts square divisors with two prime factors. | ✓ all three |
| 22 | R1 applies HCF to inventory, LCM threshold and triple failure; R2 counts HCF/LCM pairs, rope pieces and impossible LCM; R3 checks prime powers, square-tile measurement and cube relation. | ✓ all three |
| 23 | R1 uses gcd of three differences/nonzero residues and invalid remainder; R2 enforces divisor and remainder **two bounds**; R3 proves a maximum fixed-residue divisor and combines two congruences. | ✓ all three |
| 24 | R1 uses period-four/two/one, negative and zero exponent and product; R2 tests a different power product and fixed-digit sum; R3 had **no product of unit-digit expressions** → Q63 now multiplies two bracket residues. | ✓ after R3-Q63 |
| 25 | R1 noncoprime stabilization, tower and two-digit leading zero; R2 detects a two-term cycle's actual start, counts a transient plus four cyclic residues (Q09), locates the least tower level (Q10) and counts two-digit cyclic hits (Q18); R3 handles noncoprime tower/pre-period. R1 lacked **nonconstant eventual-cycle offset** → Q65 now locates cycle start at n=3, then maps n=2026. | ✓ after R1-Q65 |
| 26 | R1 counts 130! zeros and 3-adic 80! valuation; R2 compares 249! and 125! zeroes and cancels twice the 2-adic 32! valuation from 64!; R3 5-adic 125! floor boundary and 2/3-adic 90! joint exponent; terminal nonzero decisions differ. | ✓ all three |
| 27 | R1 range-page digits, digit frequency/sum and repeats but **no concatenation-index decision** → Q64 identifies contributing integer 170; R2 resolves the 200th digit and revised Q46 counts exact-valuation repeated-block digit choices; R3 finds last completed integer at 600 digits. | ✓ after R1-Q64 |
| 28 | R1 asks reversal difference, digit sum via reversal sum, zero-aware permutations and repunit minimum; R2 tested reversal difference but **not sum/11** → Q63 now maximises digit difference under a reversal sum; R3 counts unordered reversal pairs and repunit gcd. | ✓ after R2-Q63 |
| 29 | Pure/mixed repeat conversion and denominator placement in all three; R1 includes zero inverse/real-root exclusion, R2 contrasts fractional and negative exponents, R3 contrasts complementary reciprocals and counts irrational real roots. | ✓ all three |
| 30 | R1 exactly-one/neither with noncoprime lcm and strict quotient filtering; R2 now counts **none** and **exactly one** of three divisor sets (Q14/Q28), plus three-way union and strict endpoints; R3 either/exactly-one/neither-primes plus bounded inclusive/strict intersections. | ✓ all three |
| 31 | R1 differences, term-divisibility ratio and universal recurrence factor; R2 difference HCF, signed ratio and periodic 50-term sum; R3 cubic-difference residue, factorial ratio, parity periodicity and recurrence. | ✓ all three |
| 32 | R1 bounds roots and powers, signed squaring counterexample; R2 checks competing inverse-root magnitudes and sign-aware quadratic interval; R3 tests two signed square roots, reciprocal magnitudes and constructive digit bound. | ✓ all three |
| 33 | R1 counts ordered unit-fraction solutions, recovers two linked torn leaves from their remaining page sum and filters strict odd quotients; R2 maximises denominator, infers one torn leaf and excludes forbidden interior multiples; R3 minimises denominator sum and excludes impossible odd/even torn-page total. | ✓ all three |
| 34 | R1 cube ratio, `n²+1` prime count and equal factor counts; R2 cube-root product, `2^n−1` prime count and nonidentical exponent patterns; R3 cube HCF+LCM, `n!+1` primes and nine-divisor exponent structures. | ✓ all three |

## Question-only blind qualitative pass — 2026-10-01

Read the **question and all four options** of each ID below in the listed bank order **without the corresponding answer file**; only then compared the existing result/answer audit. This is a human question-only screen for distractor plausibility, two-survivor potential, independent numerical decisions and CSAT difficulty mix—not a claim that a script proves semantic uniqueness or that every foundation checkpoint is a hard PYQ. IDs actually screened (no IDs inferred from a count):

| Bank | Question-only IDs inspected |
|---|---|
| R1, first block | Q01 Q02 Q03 Q04 Q05 Q06 Q07 Q08 Q09 Q10 Q11 Q12 Q13 Q14 Q15 Q16 Q17 Q18 Q19 Q20 Q21 Q22 Q23 Q24 Q25 Q26 Q27 Q28 Q29 Q30 Q31 Q32 |
| R1, second block | Q33 Q34 Q35 Q36 Q37 Q38 Q39 Q40 Q41 Q42 Q43 Q44 Q45 Q46 Q47 Q48 Q49 Q50 Q51 Q52 Q53 Q54 Q55 Q56 Q57 Q58 Q59 Q60 Q61 Q62 Q63 Q64 Q65 |
| R2, first block | Q01 Q02 Q03 Q04 Q05 Q06 Q07 Q08 Q09 Q10 Q11 Q12 Q13 Q14 Q15 Q16 Q17 Q18 Q19 Q20 Q21 Q22 Q23 Q24 Q25 Q26 Q27 Q28 Q29 Q30 Q31 Q32 |
| R2, second block | Q33 Q34 Q35 Q36 Q37 Q38 Q39 Q40 Q41 Q42 Q43 Q44 Q45 Q46 Q47 Q48 Q49 Q50 Q51 Q52 Q53 Q54 Q55 Q56 Q57 Q58 Q59 Q60 Q61 Q62 Q63 |
| R3, first block | Q01 Q02 Q03 Q04 Q05 Q06 Q07 Q08 Q09 Q10 Q11 Q12 Q13 Q14 Q15 Q16 Q17 Q18 Q19 Q20 Q21 Q22 Q23 Q24 Q25 Q26 Q27 Q28 Q29 Q30 Q31 Q32 |
| R3, second block | Q33 Q34 Q35 Q36 Q37 Q38 Q39 Q40 Q41 Q42 Q43 Q44 Q45 Q46 Q47 Q48 Q49 Q50 Q51 Q52 Q53 Q54 Q55 Q56 Q57 Q58 Q59 Q60 Q61 Q62 Q63 |

**Repair log, with independently recomputed A–D decisions:** R1-Q10 replaced an option *numerically equal* to the key with the distinct but close `0.(327)` error; R1-Q23 replaced three logically impossible distractors with internally possible, visibly balanced combinations whose actual divisibility must be checked; R1-Q57 replaced a supplied-total subtraction with the inverse **two-leaf** problem. R2-Q09/Q10/Q14/Q17/Q18/Q28/Q46 replaced respectively the constant-zero clone, tower-remainder clone, two-set-neither clone, direct-factorial-valuation clone, last-two-single-power clone, two-set-exclusive clone and unconditional 3-divisor checkpoint. The changed decisions are respectively **five residues, least tower level 4, none-of-three 110, quotient valuation 1, 26 cyclic hits, exactly-one-of-three 45, two admissible digits**. Direct enumeration verified the changed arithmetic, including exclusions for every option. Correct letters were obtained from each item independently, not rotated.

**Calibrated difficulty, not a mechanical signoff:** R1 intentionally introduces quick definitions and one-step residue checks (e.g. Q01/Q22/Q49), R2 adds constraints, finite cycles and multi-set exclusions (Q05/Q09/Q14/Q28/Q46), and R3 adds valuation, mixed digit/number properties and infeasibility (Q29/Q50/Q55/Q60). Low-load R2-Q35 (zero exponent) and R3-Q17 (signed roots) remain as *boundary checks*, not misrepresented as hard calculation items. Answer-free stems do not expose a keyed letter. Close competitors for revised items reflect specific errors (transient omitted, triple overlap counted, 27-adic excess, one leaf versus two), not changes of constants.

**Historical checkpoint before the independent adversarial pass below:** the question-only screen above did **not** by itself establish a second-reader difficulty/two-survivor signoff. Its next gate was R1-Q01 onward. The following section records that subsequent review and supersedes this checkpoint; exact PYQ authentication and reproduction permission remain separate holds.

## Independent adversarial second pass — 2026-10-01

**Order and per-item record:** Inspected again, starting at **R1-Q01**, the stem and *every A–D choice* for all IDs explicitly enumerated in the question-only table above: **R1-Q01–Q65 (65/65), R2-Q01–Q63 (63/63), R3-Q01–Q63 (63/63)**, with no skipped ID. Independently recomputed each stem's numerical/logic decision and excluded each remaining option; checked that all four options use the same type of unit/answer, reasonably comparable visual form, and a plausible mathematical misconception or near-miss rather than an answer-length cue. Reconciled the rederived result against the keyed A–D explanations; this pass did not treat the preceding ✓ column or a mechanical uniqueness check as its proof. Cross-bank matched-route contrasts remain in the earlier decision audit. **Held original-item IDs: none; individually reviewed original-item IDs: all 191 listed above.** Low-load questions are deliberate foundation/zero/sign/domain checkpoints, not labelled hard PYQs.

| New substantive challenge | Adversarial outcome |
|---|---|
| **R1-Q40** originally paired a 45-divisor nonsquare and a 30-divisor square, *both logically impossible*, making elimination independent of N. | Replaced those pairs: A `(27, yes)` (square with exponent-4 undercount), B `(36, no)` (possible nonsquare), C `(45, yes)` actual, D `(30, no)` (possible nonsquare). Examples establishing competitor **possibility** are `2²3²5²` (27/yes), `2³3²5²` (36/no), and `2⁴3²5¹` (30/no); none describes this N. Direct computation `(2+1)(4+1)(2+1)=45`, all exponents even. |
| **R1-Q49** was `11×0.(27)` with integer options 2,3,4,5: three arbitrary neighbours, answer after a single denominator cancellation. | Replaced with `x/(1+x)` for `x=0.(27)`. A `27/127` assumes termination at .27; B `27/126` uses the true recurring fraction; C `27/99` omits `1+x`; D `27/72` changes the plus to minus. Cross-multiplication gives unique B; all options are positive fractions of the same format. R2-Q11 instead *converts* a pure repeat; R3-Q35 *subtracts* two repeats. |
| **R1-Q45 rationale** attributed option A to the wrong fourth-cycle position and C to sign alone, which did not produce those respective answers. | Recomputed `(-3)^15≡3`, `(2^13+1)≡3 (mod 10)`; A `7×3≡1` drops sign, B `3` omits second factor, C `7` drops sign **and** omits second factor, D `3×3≡9` exact. Corrected A–D rationale, key unchanged. |

**Competitor/difficulty calibration:** Initial R1 classifications Q01/Q22/Q38 and inverse implication Q39 intentionally diagnose number-domain and prime-power mistakes. R1-Q40/Q49 no longer permit the visual/logic shortcuts found here; R1-Q45's explanations now actually derive its alternatives. R2-Q09/Q14/Q17/Q28/Q46 require transient counting, triple overlaps, binomial valuation, exclusive-set enumeration and 27-adic rejection respectively; R3-Q29/Q34/Q50/Q55/Q62/63 require distinct prime factors, terminal two-digit tracking, a constructive lower bound, a physical odd-page leaf, a constrained unordered count and signed compound residues. R2-Q35 and R3-Q17 remain openly identified basic **boundary** checks, not recast as difficult. A timed learner trial may later measure empirical discrimination, but a future learner attempt is *not* required to accept authored original banks.

**Original-only decision:** All **65/63/63** question–answer pairs pass this second question-by-question adversarial review of mathematical uniqueness, A–D rationale, visible option balance, meaningful misconceptions and differentiated method, alongside the earlier complete owner-row and computation audits. Accept the three *original-only* banks; do **not** call the entire CSAT-02 catalogue topic complete. **First remaining gate:** the *exact-PYQ* provenance/rights hold—obtain a complete official Series-A question image, independently authenticated published UPSC-hosted same-series non-provisional key with upstream URLs, match exact question/options, and separately document reproduction permission. No exact PYQ is included or solved in any bank.


---

## Repair pass — 2026-11-01: letter balance, difficulty replacement and option-length check

Scope: all 191 items (revision-1 65, revision-2 63, revision-3 63). Changed files: `revision-N/QUESTIONS.md` and `revision-N/ANSWERS.md` in each set, this section, and a repair note appended to `COVERAGE.md`. IDs are unchanged; no item was deleted or renumbered.

### Method

1. Replaced the 16 easiest items per set (about 25%) with harder multi-step items on the same owner rows: 48 replacements in total. Each new key was recomputed in Python (brute-force enumeration, modular or exact `Fraction` arithmetic) before any file was written; constant-value items were checked by exact hand computation as listed below.
2. Rebalanced letters: each set has a fixed target count per letter (revision-1 16/16/16/17; revision-2 and revision-3 16/16/16/15, that is 24–27% per letter), assigned by a seeded random shuffle. The correct option is moved to its target letter; the three distractors keep their relative order. Numeric ascending order is therefore broken in the moved items, as the brief allows.
3. Explanations: option labels (`A:`–`D:`) were remapped mechanically. Every unchanged entry was first confirmed to contain exactly four option labels. Replaced entries were written with placeholder tokens that were filled from the final mapping.
4. Verification of the staged output, then installation (byte-identical copies checked with `cmp`): for all 191 items, the option at the ANSWERS key equals the intended correct value (recomputed for new items; carried from the pre-repair key for unchanged items); the stem is unchanged for the 143 unchanged items; the option set is unchanged for the 143 unchanged items; the ANSWERS header letter equals the key; a filler and placeholder scan (`within the stated source framework`, `judged against the evidence`, TODO, TBD, placeholder, lorem, `???`) returns no hit.

### Letter distribution (correct key), before and after

| Set | Letter | Before | Before % | After | After % |
|---|---|---|---|---|---|
| revision-1 (n=65) | A | 13 | 20.0 | 16 | 24.6 |
| revision-1 (n=65) | B | 20 | 30.8 | 16 | 24.6 |
| revision-1 (n=65) | C | 19 | 29.2 | 16 | 24.6 |
| revision-1 (n=65) | D | 13 | 20.0 | 17 | 26.2 |
| revision-2 (n=63) | A | 11 | 17.5 | 16 | 25.4 |
| revision-2 (n=63) | B | 20 | 31.7 | 16 | 25.4 |
| revision-2 (n=63) | C | 22 | 34.9 | 16 | 25.4 |
| revision-2 (n=63) | D | 10 | 15.9 | 15 | 23.8 |
| revision-3 (n=63) | A | 14 | 22.2 | 16 | 25.4 |
| revision-3 (n=63) | B | 19 | 30.2 | 16 | 25.4 |
| revision-3 (n=63) | C | 15 | 23.8 | 16 | 25.4 |
| revision-3 (n=63) | D | 15 | 23.8 | 15 | 23.8 |

Target band 20–30% per letter: all letters now fall within it (lowest 23.8%, highest 26.2%).

### Option-length balance, before and after (character counts of the option text)

| Set | Measure | Before | After |
|---|---|---|---|
| revision-1 | Correct option uniquely longest | 1/65 (1.5%) | 2/65 (3.1%) |
| revision-1 | Longest option within 1.25× shortest | 47/65 (72.3%) | 45/65 (69.2%) |
| revision-1 | Median / max longest-to-shortest ratio | 1.0 / 3.0 | 1.0 / 2.0 |
| revision-2 | Correct option uniquely longest | 0/63 (0.0%) | 0/63 (0.0%) |
| revision-2 | Longest option within 1.25× shortest | 53/63 (84.1%) | 42/63 (66.7%) |
| revision-2 | Median / max longest-to-shortest ratio | 1.0 / 2.0 | 1.0 / 3.0 |
| revision-3 | Correct option uniquely longest | 1/63 (1.6%) | 2/63 (3.2%) |
| revision-3 | Longest option within 1.25× shortest | 49/63 (77.8%) | 47/63 (74.6%) |
| revision-3 | Median / max longest-to-shortest ratio | 1.0 / 4.0 | 1.0 / 4.0 |

Reading: the brief's cue rule (correct option uniquely longest in at most 25–30% of items) is met with margin in every set. The softer 1.25× length-band target is not met in roughly 25–35% of items; the residual is mostly numeric options with different digit counts (for example 1 against 1080) and short symbolic options set against sentence options. This is recorded as an open gap, not hidden.

### Replaced items (difficulty repair)

| ID | Old key → new key | Replacement item (new stem, abridged) | Verification |
|---|---|---|---|
| R1-Q01 | C → B | How many of the following are rational numbers that are **not** integers?  (i) √12.25 (ii) (√50 + √2)/√2 (iii) ∛0.125 (iv) (√7 × √7)/14 | Python |
| R1-Q02 | C → D | The six-digit numeral `1x0y80` is divisible by 99, where `x` and `y` are decimal digits. What is `x + y`? | Python |
| R1-Q05 | C → B | 84 red counters and 126 blue counters are packed into boxes. Every box holds the same number of counters, all of one colour, with no counter left over… | Python |
| R1-Q14 | D → D | Let a = 2/5. What is the value of a^(−2) − a^(−1) + a²? | Python |
| R1-Q22 | D → D | Natural numbers begin at 1. How many of the following are whole numbers that are **not** natural numbers?  (i) 6 − √36 (ii) 3⁰ (iii) (−1)³ + 1 (iv) √0… | Python |
| R1-Q23 | B → B | How many of the following numerals are divisible by 36?  (i) 46,512 (ii) 73,116 (iii) 81,214 (iv) 90,130 (v) 52,236 | Python |
| R1-Q24 | B → D | What is the smallest integer greater than 500 that is divisible by 18, 24 and 30 but **not** by 16? | Python |
| R1-Q29 | D → C | How many integers in the closed interval [40, 300] have exactly three positive divisors? | Python |
| R1-Q30 | C → C | For how many integers n with 0 ≤ n ≤ 10 is √((n − 3)(n − 7)) a real number? | Python |
| R1-Q34 | C → A | What is the least positive integer N that leaves remainder 5 when divided by 9 and remainder 3 when divided by 13? | Python |
| R1-Q37 | B → D | How many of the following are odd composite numbers?  (i) 91 (ii) 97 (iii) 121 (iv) 3⁴ − 2⁴ | Python |
| R1-Q38 | C → D | Which expression is irrational? | exact hand check |
| R1-Q41 | D → B | Two positive integers have HCF 6 and LCM 180. One of them is 36. What is the **sum** of the two integers? | exact hand check |
| R1-Q50 | B → C | Which statement is equivalent to /x − 2/ < 3 for real x? | exact hand check |
| R1-Q54 | C → B | For a_n = (−1)^n (n² − 1), what is a_1 + a_2 + a_3 + a_4 + a_5 + a_6? | Python |
| R1-Q63 | D → D | A two-digit number and its two-digit reversal sum to 154. The number exceeds its reversal by 36. What is the product of its two digits? | Python |
| R2-Q01 | B → C | Which of the following is a non-negative rational number that is **not** a whole number? | Python |
| R2-Q03 | B → C | For how many decimal digits `x` is the numeral `63x16` divisible by 8 but **not** by 9? | Python |
| R2-Q04 | C → D | Two positive integers have HCF 8 and LCM 120. The larger minus the smaller is 16. What is the larger integer? | Python |
| R2-Q11 | A → A | Let x = 0.(36), with the block 36 repeating from the first decimal place. What is x / (1 − x) in lowest terms? | Python |
| R2-Q20 | C → B | Which of the following numbers is an integer but **not** a whole number? | exact hand check |
| R2-Q22 | B → A | What is the sum of the positive divisors of 360 that are **not** divisible by 6? | Python |
| R2-Q23 | A → B | How many ordered pairs (a, b) of positive integers satisfy HCF(a, b) = 12 and LCM(a, b) = 720? | Python |
| R2-Q33 | C → A | How many positive divisors of 1800 are divisible by 10 but **not** by 9? | Python |
| R2-Q34 | C → A | A positive integer N leaves remainder 5 on division by 12 and remainder 11 on division by 18. What is the least such N greater than 100? | Python |
| R2-Q36 | C → C | How many primes p satisfy 50 ≤ p ≤ 100 and also have p + 10 prime? | Python |
| R2-Q37 | A → C | Which of the following is a real irrational number? | exact hand check |
| R2-Q38 | D → B | How many positive divisors of 720 are divisible by 12 but **not** by 8? | Python |
| R2-Q40 | C → B | How many ordered pairs (a, b) of positive integers satisfy LCM(a, b) = 315? | Python |
| R2-Q43 | A → C | Ropes of lengths 144 cm, 216 cm and 360 cm are each cut, without waste, into pieces of the greatest possible length common to all three ropes. How man… | Python |
| R2-Q50 | B → B | What is the value of (1/4)^(−3/2) × (1/8)^(2/3)? | exact hand check |
| R2-Q55 | A → A | If a_n = 3 × (−2)^(n−1) for n ≥ 1, what is a_3 + a_4 + a_5 + a_6 + a_7 + a_8? | Python |
| R3-Q01 | B → C | How many of the following expressions evaluate to a prime number?  (i) 2⁴ + 1 (ii) 3³ − 1 (iii) 5² − 6 (iv) 7 × 11 + 2 | Python |
| R3-Q02 | D → B | How many positive integers not exceeding 100 are divisible by 6, are **not** divisible by 12, and have an odd digit sum? | Python |
| R3-Q03 | B → A | The six-digit numeral `4x3y18` is divisible by 66, where `x` and `y` are decimal digits. What is `x + y`? | Python |
| R3-Q08 | B → B | What is the units digit of (2¹⁰⁰ + 3¹⁰¹) × 7²? | exact hand check |
| R3-Q16 | B → D | A sequence begins 1, 2, and each later term is the sum of the two preceding terms. What is the remainder when its 20th term is divided by 7? | exact hand check |
| R3-Q17 | C → B | How many integers n satisfy /n² − 5/ ≤ 4? | Python |
| R3-Q22 | D → D | What is the sum of all integers n in the interval [−5, 5] for which n³ + n² + 1 is divisible by 3? | Python |
| R3-Q23 | B → C | Natural numbers begin at 1. Which statement about the number −(√72 − 6√2)/√2 is correct? | exact hand check |
| R3-Q24 | C → D | What is the sum of all four-digit numerals of the form `4x6y` (with `x` and `y` decimal digits) that are divisible by 36? | Python |
| R3-Q26 | C → C | For the integers 4, 6 and 9, what is the sum of their three pairwise HCFs? | Python |
| R3-Q33 | A → A | How many positive divisors of 2⁴ × 3³ × 5 are both perfect squares and divisible by 6? | Python |
| R3-Q36 | D → B | How many of the following are rational numbers that are **not** integers?  (i) √0.49 (ii) −√49 (iii) 2√2 × √2 (iv) ∛0.001 | Python |
| R3-Q37 | C → B | How many real solutions does the equation x³ − 2x = 0 have? | exact hand check |
| R3-Q39 | D → C | How many unordered pairs of positive integers have HCF 4 and LCM 60? | Python |
| R3-Q43 | A → D | Two positive integers have HCF 6 and LCM 126. One of them is 18. What is the other integer? | exact hand check |
| R3-Q47 | A → C | How many integers from 1 through 120 are divisible by **exactly one** of 4 and 6? | Python |

The pre-repair text of each replaced item is not reproduced here. The pre-repair files are preserved outside the repository, and the 'Old key' column above gives the prior key.

### Open gaps (recorded, not hidden)

- **Shortcut and time target (CSAT rule 2):** the 48 replacement entries carry a shortcut and a time target in seconds. The 143 unchanged legacy ANSWERS entries do not; they were not rewritten in this pass and remain an open gap.
- **Length band:** the correct option is uniquely longest in only 0–3% of items. The 1.25× band is met in about 65–75% of items; the residual is mostly numeric options with different digit counts. Unchanged original items with extreme ratios: R3-Q31 (11 / 1 / 101 / 1111) and R2-Q50 (1/2 / 2 / 8 / 32 after the rebalance; ratio 3.0).
- **COVERAGE ledger:** matrix rows that cite replaced IDs are superseded by the repair note appended to COVERAGE.md.
- **Difficulty:** the 48 replacements are multi-step by design (count-of-items, digit-test intersections, modular or valuation chains). The share of two-step items in the 143 unchanged items was not re-measured in this pass.
- **Exact-PYQ hold and provisional status** from the earlier audit are unchanged; nothing in this pass reproduces UPSC wording or options.

### Changed-ID log (every ID in the three sets)

Action codes: **R** = replaced with a harder item; **M** = options reordered (key letter moved); **=** = letter and option order unchanged. Every ID is listed.


**revision-1**

| ID | Action | Old key | New key |
|---|---|---|---|
| R1-Q01 | R+M | C | B |
| R1-Q02 | R+M | C | D |
| R1-Q03 | M | B | A |
| R1-Q04 | = | A | A |
| R1-Q05 | R+M | C | B |
| R1-Q06 | M | A | D |
| R1-Q07 | = | D | D |
| R1-Q08 | M | A | C |
| R1-Q09 | M | A | C |
| R1-Q10 | M | B | C |
| R1-Q11 | M | B | C |
| R1-Q12 | M | A | C |
| R1-Q13 | M | A | B |
| R1-Q14 | R | D | D |
| R1-Q15 | = | C | C |
| R1-Q16 | = | B | B |
| R1-Q17 | M | B | D |
| R1-Q18 | M | A | C |
| R1-Q19 | M | C | B |
| R1-Q20 | M | D | B |
| R1-Q21 | M | C | D |
| R1-Q22 | R | D | D |
| R1-Q23 | R | B | B |
| R1-Q24 | R+M | B | D |
| R1-Q25 | M | C | A |
| R1-Q26 | = | A | A |
| R1-Q27 | M | C | B |
| R1-Q28 | M | B | C |
| R1-Q29 | R+M | D | C |
| R1-Q30 | R | C | C |
| R1-Q31 | = | A | A |
| R1-Q32 | M | C | B |
| R1-Q33 | M | B | C |
| R1-Q34 | R+M | C | A |
| R1-Q35 | M | B | D |
| R1-Q36 | M | D | C |
| R1-Q37 | R+M | B | D |
| R1-Q38 | R+M | C | D |
| R1-Q39 | M | A | D |
| R1-Q40 | M | C | A |
| R1-Q41 | R+M | D | B |
| R1-Q42 | M | C | D |
| R1-Q43 | = | A | A |
| R1-Q44 | = | B | B |
| R1-Q45 | M | D | A |
| R1-Q46 | M | D | C |
| R1-Q47 | M | B | D |
| R1-Q48 | M | C | A |
| R1-Q49 | = | B | B |
| R1-Q50 | R+M | B | C |
| R1-Q51 | M | A | B |
| R1-Q52 | M | B | A |
| R1-Q53 | M | D | A |
| R1-Q54 | R+M | C | B |
| R1-Q55 | M | A | B |
| R1-Q56 | M | B | D |
| R1-Q57 | = | C | C |
| R1-Q58 | M | B | D |
| R1-Q59 | M | C | A |
| R1-Q60 | M | D | C |
| R1-Q61 | M | B | A |
| R1-Q62 | = | B | B |
| R1-Q63 | R | D | D |
| R1-Q64 | M | C | A |
| R1-Q65 | M | D | A |

**revision-2**

| ID | Action | Old key | New key |
|---|---|---|---|
| R2-Q01 | R+M | B | C |
| R2-Q02 | M | D | B |
| R2-Q03 | R+M | B | C |
| R2-Q04 | R+M | C | D |
| R2-Q05 | = | B | B |
| R2-Q06 | = | B | B |
| R2-Q07 | M | A | D |
| R2-Q08 | M | C | B |
| R2-Q09 | M | C | D |
| R2-Q10 | M | D | A |
| R2-Q11 | R | A | A |
| R2-Q12 | M | D | A |
| R2-Q13 | M | B | D |
| R2-Q14 | M | D | A |
| R2-Q15 | M | C | D |
| R2-Q16 | M | A | D |
| R2-Q17 | M | B | A |
| R2-Q18 | = | B | B |
| R2-Q19 | M | C | D |
| R2-Q20 | R+M | C | B |
| R2-Q21 | M | B | C |
| R2-Q22 | R+M | B | A |
| R2-Q23 | R+M | A | B |
| R2-Q24 | M | D | A |
| R2-Q25 | = | B | B |
| R2-Q26 | M | C | B |
| R2-Q27 | M | C | D |
| R2-Q28 | = | B | B |
| R2-Q29 | M | A | D |
| R2-Q30 | M | B | C |
| R2-Q31 | = | C | C |
| R2-Q32 | M | C | A |
| R2-Q33 | R+M | C | A |
| R2-Q34 | R+M | C | A |
| R2-Q35 | M | B | C |
| R2-Q36 | R | C | C |
| R2-Q37 | R+M | A | C |
| R2-Q38 | R+M | D | B |
| R2-Q39 | M | B | C |
| R2-Q40 | R+M | C | B |
| R2-Q41 | M | C | D |
| R2-Q42 | M | C | D |
| R2-Q43 | R+M | A | C |
| R2-Q44 | M | D | A |
| R2-Q45 | M | B | C |
| R2-Q46 | M | A | D |
| R2-Q47 | = | B | B |
| R2-Q48 | = | C | C |
| R2-Q49 | = | C | C |
| R2-Q50 | R | B | B |
| R2-Q51 | M | C | D |
| R2-Q52 | = | A | A |
| R2-Q53 | M | B | D |
| R2-Q54 | = | D | D |
| R2-Q55 | R | A | A |
| R2-Q56 | M | C | B |
| R2-Q57 | M | C | A |
| R2-Q58 | M | D | A |
| R2-Q59 | M | D | C |
| R2-Q60 | M | B | C |
| R2-Q61 | M | A | B |
| R2-Q62 | M | C | A |
| R2-Q63 | M | B | C |

**revision-3**

| ID | Action | Old key | New key |
|---|---|---|---|
| R3-Q01 | R+M | B | C |
| R3-Q02 | R+M | D | B |
| R3-Q03 | R+M | B | A |
| R3-Q04 | M | C | D |
| R3-Q05 | M | B | D |
| R3-Q06 | M | A | B |
| R3-Q07 | M | A | D |
| R3-Q08 | R | B | B |
| R3-Q09 | M | A | B |
| R3-Q10 | M | D | B |
| R3-Q11 | M | A | D |
| R3-Q12 | M | A | C |
| R3-Q13 | M | C | B |
| R3-Q14 | M | D | B |
| R3-Q15 | M | D | B |
| R3-Q16 | R+M | B | D |
| R3-Q17 | R+M | C | B |
| R3-Q18 | = | A | A |
| R3-Q19 | = | B | B |
| R3-Q20 | M | B | C |
| R3-Q21 | M | C | A |
| R3-Q22 | R | D | D |
| R3-Q23 | R+M | B | C |
| R3-Q24 | R+M | C | D |
| R3-Q25 | M | D | B |
| R3-Q26 | R | C | C |
| R3-Q27 | = | D | D |
| R3-Q28 | M | B | A |
| R3-Q29 | M | B | D |
| R3-Q30 | M | D | A |
| R3-Q31 | = | A | A |
| R3-Q32 | = | C | C |
| R3-Q33 | R | A | A |
| R3-Q34 | M | B | A |
| R3-Q35 | M | A | C |
| R3-Q36 | R+M | D | B |
| R3-Q37 | R+M | C | B |
| R3-Q38 | M | B | C |
| R3-Q39 | R+M | D | C |
| R3-Q40 | M | A | D |
| R3-Q41 | M | D | C |
| R3-Q42 | M | C | B |
| R3-Q43 | R+M | A | D |
| R3-Q44 | M | C | B |
| R3-Q45 | M | D | A |
| R3-Q46 | M | C | A |
| R3-Q47 | R+M | A | C |
| R3-Q48 | M | B | C |
| R3-Q49 | = | C | C |
| R3-Q50 | M | B | C |
| R3-Q51 | = | D | D |
| R3-Q52 | M | A | B |
| R3-Q53 | = | C | C |
| R3-Q54 | M | B | A |
| R3-Q55 | M | C | A |
| R3-Q56 | M | B | D |
| R3-Q57 | = | D | D |
| R3-Q58 | M | B | C |
| R3-Q59 | M | D | A |
| R3-Q60 | M | A | D |
| R3-Q61 | M | B | A |
| R3-Q62 | M | B | A |
| R3-Q63 | M | C | A |

IDs replaced: revision-1: R1-Q01, R1-Q02, R1-Q05, R1-Q14, R1-Q22, R1-Q23, R1-Q24, R1-Q29, R1-Q30, R1-Q34, R1-Q37, R1-Q38, R1-Q41, R1-Q50, R1-Q54, R1-Q63; revision-2: R2-Q01, R2-Q03, R2-Q04, R2-Q11, R2-Q20, R2-Q22, R2-Q23, R2-Q33, R2-Q34, R2-Q36, R2-Q37, R2-Q38, R2-Q40, R2-Q43, R2-Q50, R2-Q55; revision-3: R3-Q01, R3-Q02, R3-Q03, R3-Q08, R3-Q16, R3-Q17, R3-Q22, R3-Q23, R3-Q24, R3-Q26, R3-Q33, R3-Q36, R3-Q37, R3-Q39, R3-Q43, R3-Q47.

