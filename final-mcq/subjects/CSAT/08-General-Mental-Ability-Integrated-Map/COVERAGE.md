# csat-08 — General mental ability (integrated capstone): coverage ledger and strategy

**Status: complete** (three 40-item sets, this ledger and `AUDIT.md`; all automated key checks pass). Caveat: reading-based keys have no second independent reviewer, as stated in `AUDIT.md` section 6.

## 1. Sources read

- Brief and repository rules: `final-mcq/INSTRUCTIONS.md` (anti-giveaway standard, uniform format, CSAT practice mode).
- Format references: `final-mcq/subjects/CSAT/02-Number-Systems-and-Number-Sense/` (COVERAGE, AUDIT and revision files) and `01-Reading-Comprehension/` (revision files).
- Owner files, read fully: `upsc-ai-kit/knowledge/CSAT/basic/08_General-Mental-Ability-Integrated-Map.md` and `advanced/08_Mixed-General-Mental-Ability-and-Strategy.md`.
- Owner files 01–07, read by section: "Must-Know facts", "Common traps", "Mini-drill" and "Timed transfer" sections of the basic files, and the "Boundary cases" and "Advanced traps" sections of the advanced files. Advanced 07 was read at its heading level only (see gaps).

## 2. Paper shape and time budget

Each set has 40 items, in mixed order, with passage groups kept together. Per-set counts and the cluster time budget (48 minutes, about 72 seconds per question) are:

| Cluster | Items per set | Cluster budget | Coverage (owners) |
|---|---|---|---|
| Reading comprehension (RC) | 8 | 10 min | Owner 01 (basic and advanced) |
| Number sense (NS) | 4 | 5 min | Owner 02 (and 08 closure) |
| Arithmetic and commercial math (AR) | 4 | 5 min | Owner 03 |
| Rates, motion, time and geometry (RG) | 4 | 5 min | Owner 04 |
| Algebra, inequalities, data sufficiency (AL) | 4 | 4 min | Owner 05 |
| Logical reasoning, coding, seating, counting (LG) | 6 | 7 min | Owner 06 |
| Data interpretation (DI) | 6 | 7 min | Owner 06 (tables) |
| Decision-making and communication (DM) | 4 | 5 min | Owner 07 |

Budgets total 48 minutes: reading comprehension 10 (8 items, including passage reading), quantitative 19 (16 items), logical reasoning 7 (6 items), data interpretation 7 (6 items) and decision-making 5 (4 items). The reading comprehension budget of 10 minutes and the quantitative budget of 19 minutes include short passage reading and the first representation step.

**Proportions.** The mix is an authoring approximation to a realistic mixed paper: about 20 per cent reading comprehension, 40 per cent quantitative (number, arithmetic, rates and geometry, algebra and data sufficiency), 15 per cent logical reasoning, 15 per cent data interpretation, and 10 per cent decision-making and communication. These proportions are not an official UPSC blueprint.

**Item time targets.** The per-item targets in `ANSWERS.md` sum to about 51 minutes in R1, 52 in R2 and 50 in R3. That is 2–4 minutes more than the 48-minute block. The cluster budgets are binding: an item that exceeds its target is parked (see section 3), so the set is finished in the block with a few items left.

## 3. Strategy note: skip, attempt and pace

- **Scoring.** +2.5 for a correct answer, −0.83 for a wrong answer, 0 for a skipped item (one-third of 2.5, rounded to 0.83).
- **Break-even confidence.** An answer with probability p of being correct has expected value 2.5p − 0.83(1 − p). That is zero at p = 0.83 / 3.33 = 0.249, about one in four.
- **Blind guessing** on four options gives 2.5 × 0.25 − 0.83 × 0.75 = +0.0025, which is effectively zero. A blind guess is therefore not worth taking.
- **Attempt rule.** Answer when you can eliminate at least one option for a stated reason. With three options left, p is at least 1/3 and the expected value is about +0.28. With two left, the expected value is about +0.84.
- **Skip rule.** Skip when no option can be eliminated and no option is chosen with confidence. Mark the item and return to it only if time remains.
- **Pacing.** Within each cluster, first pass at the cluster target; park at the cap (target plus about 30 seconds) with a one-word reason (method, representation, arithmetic or live options).
- **Order.** Work in printed order, but do not spend more than the cap on one item. Use the last 4 minutes to revisit parked items with an elimination rule, and do not change an answer without a stated reason.
- **Data sufficiency.** State the verdict for each statement first, then the combined verdict, and only then match the printed option.

## 4. Owner ledger (question IDs by owner reference)

Each item's owner references (`B` = basic owner, `A` = advanced owner, `B08` = integration owner) are listed. Rows are grouped by owner file. The tags are a row-level route, not a substitute for the checklist in each owner file.

| Owner | Title | R1 item numbers | R2 item numbers | R3 item numbers |
|---|---|---|---|---|
| A01 | Reading comprehension (advanced) | Q03, Q25, Q26 | Q01 | Q01, Q27 |
| A02 | Number systems (advanced) | Q14, Q21, Q33 | Q04, Q14, Q21, Q33 | Q21 |
| A03 | Arithmetic (advanced) | Q06, Q24, Q36 | Q03, Q06, Q15, Q27 | Q06, Q30, Q36 |
| A04 | Rates and geometry (advanced) | Q18, Q23, Q35 | Q10, Q18, Q23 | Q10, Q18 |
| A05 | Algebra and DS (advanced) | Q11, Q19, Q29, Q39 | Q19, Q29 | Q19, Q29, Q38 |
| A06 | Logical reasoning and DI (advanced) | Q05, Q13, Q28, Q30 | Q05, Q13, Q28 | Q07, Q13, Q28 |
| A07 | Interpersonal communication and negotiation (advanced) | — | — | — |
| A08 | Mixed GMA and strategy (advanced) | Q01, Q04, Q05, Q06, Q07, Q10, Q11, Q12 | Q01, Q04, Q05, Q06, Q07, Q10, Q11, Q12 | Q01, Q04, Q05, Q06, Q07, Q10, Q11, Q12 |
| B01 | Reading comprehension (basic) | Q01, Q02, Q03, Q16, Q25, Q27 | Q01, Q02, Q16, Q17, Q25, Q26 | Q01, Q02, Q03, Q16, Q25, Q26 |
| B02 | Number systems (basic) | Q04, Q14, Q21, Q33 | Q04, Q14, Q21, Q33 | Q04, Q14, Q21, Q33 |
| B03 | Arithmetic and commercial math (basic) | Q06, Q08, Q15, Q16, Q17, Q24, Q32, Q36 | Q03, Q06, Q07, Q08, Q09, Q15, Q24, Q27, Q30, Q31, Q32, Q36 | Q06, Q07, Q08, Q09, Q15, Q16, Q17, Q24, Q30, Q31, Q32, Q36 |
| B04 | Rates, motion, time, geometry (basic) | Q10, Q18, Q23, Q35 | Q10, Q18, Q23, Q35 | Q10, Q18, Q23, Q35 |
| B05 | Algebra and data sufficiency (basic) | Q11, Q19, Q29, Q39 | Q11, Q19, Q29, Q38 | Q11, Q19, Q29, Q38 |
| B06 | Logical reasoning, coding, counting and DI (basic) | Q05, Q07, Q08, Q09, Q13, Q17, Q20, Q25, Q26, Q27, Q28, Q30, Q31, Q32, Q34, Q40 | Q02, Q05, Q07, Q08, Q09, Q13, Q16, Q17, Q20, Q25, Q26, Q28, Q30, Q31, Q32, Q34, Q40 | Q01, Q02, Q05, Q07, Q08, Q09, Q13, Q20, Q22, Q25, Q26, Q27, Q28, Q30, Q31, Q32, Q34, Q37, Q40 |
| B07 | Interpersonal and communication (basic) | Q12, Q22, Q37, Q38 | Q12, Q22, Q37, Q39 | Q12, Q22, Q37, Q39 |
| B08 | Integrated map and workflow (basic) | Q01, Q04, Q05, Q06, Q07, Q10, Q11, Q12 | Q01, Q04, Q05, Q06, Q07, Q10, Q11, Q12 | Q01, Q04, Q05, Q06, Q07, Q10, Q11, Q12 |

**Owner rows not directly tested (gaps).** A07 (negotiation depth, stakeholder matrix, mediation, crisis communication) has no dedicated item; communication appears only through four decision items per set. Owner 01 advanced "two-passage compare sets" and owner 06 "pie and dual-axis" graphics are not represented (all DI here is table-based). Owner 02 digit-sum maxima and owner 05 interval-product endpoint arithmetic are only indirectly present. A08 (method hierarchy and cognitive load) is applied through the integration items, not tested as a separate skill.

## 5. Item-by-item owner references

| Set | ID | Cluster | Owner references and technique |
|---|---|---|---|
| R1 | Q01 | RC | B01 inference, over-generalisation trap; B01 §4 ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q02 | RC | B01 tone and attitude; B01 §3 method |
| R1 | Q03 | RC | B01 §4 counter-evidence; A01 weakening |
| R1 | Q04 | NS | B02 §§2,6 divisor count; B02 §3 factor count ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q05 | LG | B06 §§4-5 syllogism; A06 existential trap ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q06 | AR | B03 §§2,4,8 successive percentages; A03 §6 base trap ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q07 | DI | B06 §5-M table DI; percentage vs base ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q08 | DI | B06 §5-M value vs units; B03 share |
| R1 | Q09 | DI | B06 §5-M share and percentage-point change |
| R1 | Q10 | RG | B04 §2 work and pipes; §7 net rate ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q11 | AL | B05 §2 data sufficiency format; §5 DS example; A05 M4 verdict first ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q12 | DM | B07 §9 CSAT scenario decision engine; §6 conflict and escalation ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R1 | Q13 | LG | B06 §4.1 probability; §5-D; A06 without replacement |
| R1 | Q14 | NS | B02 §§3,6 remainders; A02 §3 factorial residues |
| R1 | Q15 | AR | B03 §§2,5.3 averages and correction |
| R1 | Q16 | RC | B01 §5 assumption; B03 §5.2 share arithmetic |
| R1 | Q17 | RC | B03 §5.2 share and power arithmetic; B06 §5-D |
| R1 | Q18 | RG | B04 §2 circular track; §4 meet-at-start vs meet-anywhere; A04 M2 |
| R1 | Q19 | AL | B05 §3 simultaneous linear equations; A05 M1 dependence |
| R1 | Q20 | LG | B06 §5-H seating; §4 constraint chains |
| R1 | Q21 | NS | B02 §2 trailing zeros; A02 §§2-6 v_5 with 25 and 125 |
| R1 | Q22 | DM | B07 §4 barriers; B07 §3 listening |
| R1 | Q23 | RG | B04 §2 boats and streams; §7 average speed harmonic trap; A04 M5 |
| R1 | Q24 | AR | B03 §§2,5.4 compound interest, non-annual compounding; A03 M4 |
| R1 | Q25 | RC | B06 §4.2 correlation vs causation; B01 §4 flaw; A01 M2 |
| R1 | Q26 | RC | B06 §4.2 strengthening causal claims; A01 weakening/strengthening |
| R1 | Q27 | RC | B01 §3 inference from data; B06 §4.2 necessary-sufficient |
| R1 | Q28 | LG | B06 §5-E coding; A06 M2 coding rule verification |
| R1 | Q29 | AL | B05 §3 surds and comparison; A05 M3 surd comparison |
| R1 | Q30 | DI | B06 §5-M table; average of group totals; A06 M-DI |
| R1 | Q31 | DI | B06 §5-M ratio comparison; trap: absolute counts vs ratios |
| R1 | Q32 | DI | B06 §5-M mean of percentages vs pooled percentage; B03 §4 base |
| R1 | Q33 | NS | B02 §5.2 reversal and digit sums; A02 §5 |
| R1 | Q34 | LG | B06 §5-B blood relations |
| R1 | Q35 | RG | B04 §6-7 painted cubes (edge formula); A04 §5 layer counts |
| R1 | Q36 | AR | B03 §5-alligation and mixture ratio; A03 weighted average |
| R1 | Q37 | DM | B07 §6 negotiation: interests vs positions |
| R1 | Q38 | DM | B07 §8 questionnaires: leading, double-barrelled, neutral |
| R1 | Q39 | AL | B05 §3 absolute value and inequalities; A05 §6 strictness |
| R1 | Q40 | LG | B06 §5-C directions; §4.1 Pythagoras-based distance |
| R2 | Q01 | RC | B01 §3 inference; A01 §2 precise distinctions ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q02 | RC | B01 §5 assumption; B06 §4.2 substitution vs addition |
| R2 | Q03 | RC | B03 §5 simultaneous percentage changes; A03 §3 cross-base reasoning |
| R2 | Q04 | NS | B02 §§4-5 inclusion-exclusion with LCM; A02 §5 exactly-one trap ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q05 | LG | B06 §5 syllogism; A06 §5 existential and universal premises ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q06 | AR | B03 §§2,8 successive percentages multiply; A03 §5 successive discounts ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q07 | DI | B06 §5-M percentage change across quarters; B03 §4 base ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q08 | DI | B06 §5-M percentage change across rows; B03 §4 wrong base |
| R2 | Q09 | DI | B06 §5-M share of a total; B03 §5.1 percentage arithmetic |
| R2 | Q10 | RG | B04 §2 clock angle formula; §7 clock traps; A04 M-clock ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q11 | AL | B05 §2 data sufficiency; §6 single statement with two roots ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q12 | DM | B07 §6-9 ethics and escalation; §9 decision engine ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R2 | Q13 | LG | B06 §4.1-4.2 conditional probability; A06 §4 dice |
| R2 | Q14 | NS | B02 §§2,3,6 unit-digit cycles; A02 §4 cycle-zero position |
| R2 | Q15 | AR | B03 §5 mixtures with replacement; A03 §3 replacement formula |
| R2 | Q16 | RC | B06 §4 conditional logic and necessary conditions; B01 §4 flaw |
| R2 | Q17 | RC | B06 §4 contrapositive and necessary condition; B01 §3 |
| R2 | Q18 | RG | B04 §4 alternate-day work; A04 M1 and M4 |
| R2 | Q19 | AL | B05 §3 algebraic identities; A05 M5 extrema reading |
| R2 | Q20 | LG | B06 §5-H seating; §4 constraint chains |
| R2 | Q21 | NS | B02 §2 v_p(n!) full floor sum; A02 §3 M2 |
| R2 | Q22 | DM | B07 §4 barriers and remedy; §2 channels |
| R2 | Q23 | RG | B04 §7 calendar and leap-year span; A04 M6 |
| R2 | Q24 | AR | B03 §§2,5.4 compound and simple interest; §7 CI−SI formula |
| R2 | Q25 | RC | B01 §4 distortion and scope; B06 §4.2 causal design |
| R2 | Q26 | RC | B06 §4.2 controlled comparison; B01 §4 strengthening |
| R2 | Q27 | RC | B03 §5 percentage arithmetic with a base; A03 §4 base choice |
| R2 | Q28 | LG | B06 §5-E coding by letter value; A06 M2 rule verification |
| R2 | Q29 | AL | B05 §3 comparison of powers; A05 M3 surd comparison |
| R2 | Q30 | DI | B06 §5-M table comparisons; B03 §5.3 averages |
| R2 | Q31 | DI | B06 §5-M averages and percentage of an average; B03 §4 base |
| R2 | Q32 | DI | B06 §5-M percentage decline; B03 §4 base |
| R2 | Q33 | NS | B02 §§2,4 HCF × LCM for two numbers; A02 §5 two-number product |
| R2 | Q34 | LG | B06 §5-H ranking; §4 chains |
| R2 | Q35 | RG | B04 §2 average speed by total time; §7 harmonic trap |
| R2 | Q36 | AR | B03 §7 partnership: capital × time; §2 partnership share |
| R2 | Q37 | DM | B07 §9 decision under uncertainty; §6 risk and verification |
| R2 | Q38 | AL | B05 §2-§6 sign reasoning in DS; §6 sign-dependent products |
| R2 | Q39 | DM | B07 §9 decision engine; §11 time management |
| R2 | Q40 | LG | B06 §4 permutation; §5-J counting with restrictions |
| R3 | Q01 | RC | B01 §4 distortion; B06 §4.2 causal design; A01 weakening ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q02 | RC | B01 §3 inference with hedging; B06 §4.2 correlation |
| R3 | Q03 | RC | B01 §4 weakening with specific counter-evidence |
| R3 | Q04 | NS | B02 §4 LCM of periods; §5.4 counting multiples in a range ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q05 | LG | B06 §5-J Venn and inclusion-exclusion ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q06 | AR | B03 §§2,4 markup and discount on marked price; A03 M2 ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q07 | DI | B06 §5-M table; B03 §4 base; A06 M-DI ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q08 | DI | B06 §5-M column totals; B03 §5 comparison |
| R3 | Q09 | DI | B06 §5-M difference of totals; B03 §4 base |
| R3 | Q10 | RG | B04 §2 relative speed opposite direction; §4 unit conversion; A04 M3 ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q11 | AL | B05 §2 data sufficiency; §6 roots and primes ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q12 | DM | B07 §5 assertiveness and fairness; §6 conflict resolution ; B08 §§3-8 classify-represent-verify workflow ; A08 §§2-5 method hierarchy and cognitive load |
| R3 | Q13 | LG | B06 §4.2 conditional probability; A06 §4 coins |
| R3 | Q14 | NS | B02 §4 HCF for exact division; §2 HCF vs LCM |
| R3 | Q15 | AR | B03 §§2,5.3 averages with a new observation; weighted average |
| R3 | Q16 | RC | B01 §5 assumption; B03 §5 base and share arithmetic |
| R3 | Q17 | RC | B03 §5 share of a total; B03 §4 base |
| R3 | Q18 | RG | B04 §2 pipes; §7 net rate and phase change; A04 M-pipe |
| R3 | Q19 | AL | B05 §3 absolute value inequalities; A05 §5 boundary cases |
| R3 | Q20 | LG | B06 §5-H seating; §4 constraint chains |
| R3 | Q21 | NS | B02 §4 common remainders and simultaneous congruences; A02 §3 |
| R3 | Q22 | DM | B07 §9 decision engine; B06 §5 constraint elimination |
| R3 | Q23 | RG | B04 §6 mensuration; §4 composite area |
| R3 | Q24 | AR | B03 §§2,5.4 simple interest solved for rate, then compound interest |
| R3 | Q25 | RC | B06 §4.2 confounding; B01 §4 limitation |
| R3 | Q26 | RC | B01 §3 conclusion scope; B06 §4.2 association vs cause |
| R3 | Q27 | RC | B06 §4.2 strengthening with random assignment; A01 §4 design |
| R3 | Q28 | LG | B06 §5-E number coding; A06 M2 rule verification |
| R3 | Q29 | AL | B05 §3 identities for sum and sum of squares; A05 M1 |
| R3 | Q30 | DI | B06 §5-M budget arithmetic; B03 §5 successive changes; A03 M4 |
| R3 | Q31 | DI | B06 §5-M share of a changed total; B03 §4 base |
| R3 | Q32 | DI | B06 §5-M share of an increase; B03 §4 base |
| R3 | Q33 | NS | B02 §§2,5.2 digit counting via powers of ten |
| R3 | Q34 | LG | B06 §5-B blood relations and spouse inference |
| R3 | Q35 | RG | B04 §6 volume of cone and sphere; ratio of volumes |
| R3 | Q36 | AR | B03 §§2,8 successive percentage changes; A03 §4 reverse change |
| R3 | Q37 | DM | B07 §9 decision under uncertainty; B06 §4.1 expected value |
| R3 | Q38 | AL | B05 §3 surd comparison by rationalising; A05 M3 |
| R3 | Q39 | DM | B07 §3 feedback: specific, behaviour-focused, actionable |
| R3 | Q40 | LG | B06 §5-C directions; §4.1 displacement vs distance |

## 6. PYQ-pattern notes (no UPSC wording reproduced)

The owner files describe demand routes from their PYQ ledgers. Those routes are used here only as skill patterns, and no UPSC passage, question text, or option is reproduced or labelled as a PYQ. The routes covered by original items:
- Reading comprehension: inference under hedging, author attitude, weakening and strengthening by specific evidence, assumptions behind a policy or argument, and confound-aware causal reasoning.
- Number sense and arithmetic: divisor counts by exponent parity, unit digits through cycles, factorial valuation, HCF and LCM use for equal groups, successive percentages with the correct base, averages with corrections, and compound interest by frequency.
- Rates and geometry: pipes with a phase change, relative speed in two directions, boat average speed as total over total, circular tracks (meet-at-start versus meet-anywhere), clock angle, calendar with a leap day, painted-cube edge counts, and volume ratios.
- Algebra and data sufficiency: two-root statements, sign-dependent products, sum-and-squares identities, absolute-value inequalities, power and surd comparisons by a common power, and integer range counts with strict and non-strict bounds.
- Logic: seating with anchors, letter and digit coding, blood relations through a sibling link, syllogisms with existential and universal premises, conditional and without-replacement probability, Venn counts, and direction displacement.
- Data interpretation: totals and percentage change with a named base, unit-share versus value-share, percentage-point shares, mean versus pooled percentage, and budget changes with head-specific growth rates.
- Decision-making and communication: escalation under conflicting instructions, barrier identification and remedy, feedback quality, questionnaire neutrality, negotiation through interests, and expected-value decisions.

## 7. Gaps and honest limits

- No second independent reviewer for reading-based keys.
- Passages are 60–110 words; real CSAT passages are longer. Reading difficulty is calibrated below a full RC block.
- The 10 per cent communication share is thin; A07 is untested directly.
- Item time targets are authoring estimates, not learner measurements. They sum to slightly more than the block.
- Option-length balance is strong for text options, but numeric and single-label options have intrinsic length differences (AUDIT section 2 lists them).
- No learner attempt has been used; score or attempt logs are out of scope.

## 8. Files

- `revision-1/QUESTIONS.md`, `revision-1/ANSWERS.md`
- `revision-2/QUESTIONS.md`, `revision-2/ANSWERS.md`
- `revision-3/QUESTIONS.md`, `revision-3/ANSWERS.md`
- `COVERAGE.md`, `AUDIT.md`
