# csat-08 — verification audit: General mental ability integrated capstone

**Scope.** Three independent mixed sets, `revision-1/`, `revision-2/`, `revision-3/`, each with 40 original items (8 reading comprehension, 16 quantitative, 6 logical reasoning, 6 data interpretation, 4 decision-making and communication). Checked on the date of authoring; no learner attempt data is used.

## 1. Method

- **Verifier.** A scratch Python checker (kept outside the repository at `/tmp/mcq_audit/csat08/build.py`) executes each item's own check code and compares the computed value with the printed key. It rejects any distractor that equals the computed value, and it asserts that the letter distribution is balanced. The check code is summarised in section 3, one row per item.
- **Check classes.** (a) *computed numeric*: the key is recomputed from the stem data with exact fractions or integers, and the key text must match the computed value while no distractor does. (b) *computed logical*: brute force over the finite structure (syllogism models over eight Venn cells; all permutations for seating, ordering and assignment; digit/letter codes; integer ranges for data-sufficiency statements, checked for uniqueness). (c) *aux*: the stem is fixed by reading, and assertions verify each numerical fact used in the explanation. (d) *manual*: reading-based reasoning checked against the passage or stem text and option-by-option reasons (reading comprehension, communication and decision items).
- **Uniqueness.** Seating, ordering and assignment items assert that exactly one arrangement survives. Data-sufficiency items enumerate integers in a bounded range and reason algebraically for the rest. Reading and decision items were checked by re-reading the stem and passage for a second defensible answer; none was found.

## 2. Per-set results

| Set | Items | Computed numeric/logical | Aux (assertions; key by reading) | Manual (reading) | Failed checks | Key letters A/B/C/D | Correct uniquely longest | Correct uniquely shortest | Mean option-length spread |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 40 | 28 | 1 | 11 | 0 | 10/10/10/10 | 1/40 = 2.5% | 1/40 = 2.5% | 0.11 |
| R2 | 40 | 31 | 0 | 9 | 0 | 10/10/10/10 | 7/40 = 17.5% | 1/40 = 2.5% | 0.16 |
| R3 | 40 | 28 | 3 | 9 | 0 | 10/10/10/10 | 7/40 = 17.5% | 6/40 = 15.0% | 0.20 |

Letter distribution is generated from a seeded plan that balances A–D at 10 each per set, so every letter holds 25 per cent (inside the 20–30 per cent band). The correct option is uniquely longest in 2.5 %, 17.5 % and 17.5 % of items (target: no more than about 25–30 %). The mean option-length spread is the mean of (longest − shortest)/longest; it is higher where numeric options are short (for example "2" against "14"), which cannot be equalised without changing the number of digits. Items whose spread exceeds 30 per cent are listed below. They are numeric, fraction, symbol or single-label sets, and the key is recorded as uniquely longest or shortest in the marked cases only.

- R1 items with spread above 30 per cent: R1-Q24 (0.33).
- R2 items with spread above 30 per cent: R2-Q04 (0.33), R2-Q05 (0.42), R2-Q13 (0.4), R2-Q17 (0.36), R2-Q23 (0.33), R2-Q24 (0.43 key uniquely shortest), R2-Q26 (0.31 key uniquely longest), R2-Q33 (0.6), R2-Q39 (0.31), R2-Q40 (0.33).
- R3 items with spread above 30 per cent: R3-Q05 (0.5), R3-Q07 (0.92 key uniquely shortest), R3-Q14 (0.5), R3-Q19 (0.44), R3-Q24 (0.33), R3-Q29 (0.5), R3-Q33 (0.5), R3-Q34 (0.33 key uniquely shortest), R3-Q35 (0.33 key uniquely shortest), R3-Q36 (0.5), R3-Q38 (0.33).

## 3. Item-level verification record

| ID | Cluster | Key | Check | Result recorded by the checker |
|---|---|---|---|---|
| R1-Q01 | RC | D | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q02 | RC | D | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q03 | RC | C | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q04 | NS | A | ok | computed 36; key option '36' |
| R1-Q05 | LG | C | ok | string key 'Only conclusion I follows' |
| R1-Q06 | AR | A | ok | string key 'Loss of 10 per cent' |
| R1-Q07 | DI | B | ok | computed 15.6; key option '15.6%' |
| R1-Q08 | DI | C | ok | computed 25.7; key option '25.7%' |
| R1-Q09 | DI | B | ok | string key 'Product S' |
| R1-Q10 | RG | C | ok | computed 8; key option '8 hours' |
| R1-Q11 | AL | C | ok | string key 'Both together are sufficient, but neither alone is sufficient' |
| R1-Q12 | DM | B | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q13 | LG | C | ok | string key '2/15' |
| R1-Q14 | NS | A | ok | computed 5; key option '5' |
| R1-Q15 | AR | D | ok | computed 39.4; key option '39.4' |
| R1-Q16 | RC | C | aux | assertions passed; key established by exact reading of the stem |
| R1-Q17 | RC | A | ok | computed 30; key option '30 per cent' |
| R1-Q18 | RG | A | ok | computed 12; key option '12 minutes' |
| R1-Q19 | AL | B | ok | computed 5; key option '5' |
| R1-Q20 | LG | A | ok | string key 'R' |
| R1-Q21 | NS | B | ok | computed 62; key option '62' |
| R1-Q22 | DM | B | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q23 | RG | D | ok | computed 11.25; key option '11.25 km/h (total distance over total time)' |
| R1-Q24 | AR | D | ok | computed 2100; key option '₹2,100' |
| R1-Q25 | RC | A | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q26 | RC | B | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q27 | RC | B | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q28 | LG | A | ok | string key 'SPDO' |
| R1-Q29 | AL | D | ok | string key '3^(1/3)' |
| R1-Q30 | DI | A | ok | computed 82.5; key option '82.5' |
| R1-Q31 | DI | D | ok | string key 'School X' |
| R1-Q32 | DI | D | ok | computed 31.8; key option '31.8%' |
| R1-Q33 | NS | C | ok | computed 84; key option '84' |
| R1-Q34 | LG | C | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q35 | RG | A | ok | computed 24; key option '24' |
| R1-Q36 | AR | D | ok | computed 15; key option '15 litres' |
| R1-Q37 | DM | B | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q38 | DM | B | manual | verified by exact reading of the stem (non-numeric) |
| R1-Q39 | AL | D | ok | computed 4; key option '4' |
| R1-Q40 | LG | C | ok | string key '√109 km, from net east and north displacement' |
| R2-Q01 | RC | C | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q02 | RC | C | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q03 | RC | A | ok | computed 32; key option '32 per cent' |
| R2-Q04 | NS | D | ok | computed 225; key option '225' |
| R2-Q05 | LG | C | ok | string key 'Both I and II follow' |
| R2-Q06 | AR | B | ok | string key '+10 per cent' |
| R2-Q07 | DI | A | ok | string key 'Quarter 4' |
| R2-Q08 | DI | D | ok | computed 50; key option '50.0%' |
| R2-Q09 | DI | B | ok | computed 30.2; key option '30.2%' |
| R2-Q10 | RG | A | ok | string key '2:27 3/11' |
| R2-Q11 | AL | C | ok | string key 'Both together are sufficient, but neither alone is sufficient' |
| R2-Q12 | DM | B | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q13 | LG | A | ok | string key '7/10' |
| R2-Q14 | NS | D | ok | computed 2; key option '2' |
| R2-Q15 | AR | B | ok | string key '9 : 16' |
| R2-Q16 | RC | D | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q17 | RC | D | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q18 | RG | C | ok | computed 12; key option '12 days' |
| R2-Q19 | AL | B | ok | computed 23; key option '23' |
| R2-Q20 | LG | A | ok | string key 'Q' |
| R2-Q21 | NS | C | ok | string key '2^38' |
| R2-Q22 | DM | D | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q23 | RG | A | ok | string key 'Tuesday' |
| R2-Q24 | AR | C | ok | computed 180; key option '₹180' |
| R2-Q25 | RC | A | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q26 | RC | B | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q27 | RC | D | ok | computed 4.8; key option '4.8 tonnes per hectare' |
| R2-Q28 | LG | C | ok | string key 'FARM' |
| R2-Q29 | AL | B | ok | string key '3^(1/4)' |
| R2-Q30 | DI | B | ok | computed 2; key option '2' |
| R2-Q31 | DI | A | ok | computed 10.5; key option '10.5%' |
| R2-Q32 | DI | C | ok | computed 33.3; key option '33.3%' |
| R2-Q33 | NS | A | ok | computed 360; key option '360' |
| R2-Q34 | LG | B | ok | string key 'A' |
| R2-Q35 | RG | D | ok | computed 78; key option '78 km/h' |
| R2-Q36 | AR | D | ok | computed 15000; key option '₹15,000' |
| R2-Q37 | DM | C | manual | verified by exact reading of the stem (non-numeric) |
| R2-Q38 | AL | B | ok | string key 'I alone is sufficient, but II alone is not sufficient' |
| R2-Q39 | DM | A | ok | string key 'T1 and T3 together' |
| R2-Q40 | LG | D | ok | computed 120; key option '120' |
| R3-Q01 | RC | A | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q02 | RC | A | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q03 | RC | C | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q04 | NS | C | ok | computed 34; key option '34' |
| R3-Q05 | LG | A | ok | computed 15; key option '15' |
| R3-Q06 | AR | D | ok | computed 640; key option '₹640' |
| R3-Q07 | DI | B | ok | string key 'East' |
| R3-Q08 | DI | A | ok | string key 'Quarter 4' |
| R3-Q09 | DI | A | ok | computed 30; key option '30' |
| R3-Q10 | RG | D | ok | computed 14.4; key option '14.4 seconds' |
| R3-Q11 | AL | C | ok | string key 'Both together are still not sufficient to determine m' |
| R3-Q12 | DM | A | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q13 | LG | D | ok | string key '2/5' |
| R3-Q14 | NS | B | ok | computed 36; key option '36' |
| R3-Q15 | AR | B | ok | computed 13000; key option '₹13,000' |
| R3-Q16 | RC | A | aux | assertions passed; key established by exact reading of the stem |
| R3-Q17 | RC | B | ok | computed 24; key option '24 per cent' |
| R3-Q18 | RG | C | aux | assertions passed; key established by exact reading of the stem |
| R3-Q19 | AL | B | ok | string key 'x > 1' |
| R3-Q20 | LG | C | ok | string key 'X' |
| R3-Q21 | NS | D | ok | computed 33; key option '33' |
| R3-Q22 | DM | D | ok | string key 'A–X, B–Y, C–Z' |
| R3-Q23 | RG | B | ok | computed 30.96; key option '30.96 cm²' |
| R3-Q24 | AR | C | ok | computed 618; key option '₹618' |
| R3-Q25 | RC | A | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q26 | RC | A | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q27 | RC | D | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q28 | LG | D | ok | string key '146' |
| R3-Q29 | AL | B | ok | computed 10; key option '10' |
| R3-Q30 | DI | A | ok | computed 312; key option '312' |
| R3-Q31 | DI | C | ok | computed 33.4; key option '33.4%' |
| R3-Q32 | DI | B | ok | computed 17.5; key option '17.5%' |
| R3-Q33 | NS | C | aux | assertions passed; key established by exact reading of the stem |
| R3-Q34 | LG | D | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q35 | RG | D | ok | computed 75; key option '75' |
| R3-Q36 | AR | B | ok | computed 10; key option '10' |
| R3-Q37 | DM | D | ok | string key 'Offer Q, since its expected payment of ₹1.0 lakh beats the ₹0.92 lakh from P' |
| R3-Q38 | AL | B | ok | string key '√6 − √4 is greater than √7 − √5' |
| R3-Q39 | DM | C | manual | verified by exact reading of the stem (non-numeric) |
| R3-Q40 | LG | C | ok | string key '0 km' |

## 4. Similarity and originality checks

- Against the other existing CSAT banks (01–03 revision files, stem plus options, difflib ratio): maximum 0.60 (R1 R1-Q04), 0.68 (R2 R2-Q14), 0.69 (R3 R3-Q21). Shared stems are standard templates (for example, data sufficiency wording), not copied items. No item was carried over from another bank.
- Across the three new sets: maximum R1–R2 0.12 (R1-Q01 / R2-Q01), R1–R3 0.20, R2–R3 0.67 (R2-Q11 / R3-Q11). Two near-duplicates were rewritten during authoring (R2 coding and radicals items) and one HCF–LCM item was reworded where it followed an existing bank template.
- No exact UPSC CSAT wording, passage, or option was reproduced. Pattern-level PYQ routes are recorded in `COVERAGE.md` only.

## 5. Items revised during authoring

These are corrections made by the checker or by re-reading before the release. None was a learner-facing revision.

- **R1-Q20 (seating):** the first constraint set had two solutions; P was anchored at the left end, which leaves one. Options re-ordered so that the key is the first option in the build, with reasons aligned.
- **R1-Q11, R1-Q18, R1-Q21, R1-Q22, R1-Q32, R1-Q35:** the key was not in the first position in the build, or a reason was attached to the wrong option. Reordered and re-aligned; the computed keys did not change.
- **R1-Q23, R1-Q34, R1-Q37, R1-Q40, R1-Q01–R1-Q03, R1-Q12, R1-Q16, R1-Q25–R1-Q27:** option lengths rebalanced so that the key was no longer uniquely the longest. Wording changed; keys unchanged.
- **R1-Q30:** numeric options given a uniform decimal form, removing a decimal-point cue.
- **R1 product-table passage:** an ambiguous sentence about the 2025 price applied to 2024 units was removed; the 26.6 % distractor is now a clear named error.
- **R2-Q06, R2-Q10, R2-Q21:** keys stated as exact strings, because a first-number parser misread a sign, a time and an exponent. R2-Q10 distractor angles corrected: at 2:21 9/11 the angle is 60°, not a coincidence (coincidence is at 4:21 9/11).
- **R2-Q15 (milk and water):** a distractor explanation corrected (the named error is replacing only the 4 litres of water removed).
- **R2-Q20 (circular seating):** the first constraint set had no solution because rotations were not anchored; redesigned with P in seat 1 (one solution, verified by enumeration).
- **R2-Q01, R2-Q12, R2-Q25, R2-Q26:** option lengths rebalanced (the key was uniquely longest); keys unchanged.
- **R2-Q39:** the short option "T2 alone" lengthened to "T2 alone, with no deadline" to reduce the length gap; key unchanged.
- **R2-Q28, R2-Q29, R2-Q33:** replaced or reworded because of similarity to R1 or to an existing bank template (see section 4).
- **R3-Q11 (data sufficiency):** key moved to the first position in the build; reasons re-aligned.
- **R3-Q33 (digit count):** the first draft said 9 digits; 80,000,000 has 8 digits (an eight followed by seven zeros). Corrected to 8 with the matching distractor explanations.
- **R3-Q36 (percentage up and down):** check used (1/100)² instead of (10/100)²; corrected.
- **R3-Q18 (pipes), R3-Q35 (cone), R3-Q16:** check code cleaned to exact assertions; the pipes options given a uniform "same day" form.
- **R3-Q23 (square and circle):** options and reasons simplified to a fixed π = 3.14 with exact arithmetic (30.96 cm²).
- **R3-Q37, R3-Q38, R3-Q39:** option lengths rebalanced; keys unchanged.

## 6. Limits of this verification

- Reading-based keys (manual checks, 29 items in total: 11 in R1, 9 in R2 and 9 in R3) have no second independent reviewer. The reasons were checked by the author against the passage text; they were not checked by a second reader.
- Assertions that check numbers used in explanations were recomputed in the checker, but the explanation prose itself was not machine-checked.
- Item time targets (seconds) are authoring estimates, not measurements from learners; the per-item targets sum to 49.7–52.4 minutes per set, against a 48-minute practice block (see `COVERAGE.md`).

## 7. Status

All 120 items pass the automated checks (0 failures). The status is recorded as complete in `COVERAGE.md`, with the reading-based limits above.
