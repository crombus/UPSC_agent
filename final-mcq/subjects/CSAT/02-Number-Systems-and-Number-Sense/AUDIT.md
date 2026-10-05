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
