# CSAT 02 — Revision 2: worked answers (original items)

**Sources:** B = `upsc-ai-kit/knowledge/CSAT/basic/02_Number-Systems-and-Number-Sense.md`; A = corresponding `advanced/02_Number-Systems-and-Number-Sense.md`. This is original practice, not official PYQ text. Provisional bank.

**R2-Q01 — C.** Correct: C. (√2)² = 2, so the value is 2/4 = 1/2, rational, non-negative and not whole. A is the negative of the same value; B equals 2 − 1 = 1 and D equals 6, both whole numbers. Trap: squaring a root returns the radicand, and a rational number need not be whole. Time target: 60 seconds.

**R2-Q02 — B.** Alternating digit sums for `53x19` differ by `(5+x+9)−(3+1)=10+x`; divisibility by 11 requires x=1. Its digit sum `18+x=19` is not divisible by 3. A: x=7 gives alternating difference 17 and digit sum 25; C: x=5 gives difference 15 and digit sum 23; D: x=3 gives difference 13 and digit sum 21 (divisible by 3); B: x=1 passes both stated conditions. Source: B §2.

**R2-Q03 — C.** Correct: C. Divisibility by 8 depends on the last three digits x16 = 100x + 16, which is divisible by 8 exactly when x is even: x ∈ {0, 2, 4, 6, 8}. The digit sum 16 + x is a multiple of 9 only for x = 2 (63216 = 9 × 7024), which is excluded. Four digits remain: 0, 4, 6, 8. A treats 0 as an invalid digit; B ignores the 9-exclusion; D applies only the 4-test, which every digit passes. Trap: the 8-test uses three digits, not two. Time target: 90 seconds.

**R2-Q04 — D.** Correct: D. The pair (40, 24) has HCF 8, LCM 120, difference 16, and 40 × 24 = 960 = 8 × 120. A is the smaller integer; B (56) has HCF 8 with 24 only if the LCM were 168, so it fails the LCM; C is the LCM. Trap: the product rule fixes ab = 960, and the difference fixes the pair. Time target: 75 seconds.

**R2-Q05 — B.** Pairwise differences are 48, 96 and 144, so a common-remainder divisor must divide 48. Below 40, the eligible divisors with remainders greater than 10 are 16 and 24 (each gives remainder 13); 24 is greatest. A: 16 also works but is smaller; B: 24 is greatest under the bound; C: 48 leaves 13 but violates the strict upper bound; D: 12 leaves remainder 1, violating the lower bound. Source: B §4.

**R2-Q06 — B.** A square divisor uses even exponents: 2 has choices 0,2,4,6 (4); 3 has 0,2,4 (3); 5 has 0,2 (2); total 24. A: 12 omits one of the 5-exponent choices; B: 24 counts all (including 1 and N); C: 30 counts an inadmissible odd exponent; D: 18 treats 2's four exponent choices as three. Source: B §§2,7.

**R2-Q07 — D.** Between 125! and 249!, the additional factors of 5 are `(⌊249/5⌋−⌊125/5⌋)+(⌊249/25⌋−⌊125/25⌋)+(⌊249/125⌋−⌊125/125⌋)=(49−25)+(9−5)+(1−1)=28`. Both factorials contain far more factors of 2, so this is also the difference in trailing zero counts. D: 28 counts all of them; A: 27 omits one additional factor; B: 29 double-counts one factor; C: 30 double-counts two. Source: B §2; A §§2,5.

**R2-Q08 — B.** `2^71` ends 8 (exponent ≡3 mod 4), `3^66` ends 9 (exponent ≡2), product 72 ends 2. A: 4 requires different cycle positions; C: 6 does not match 8×9; B: 2 correct; D: 8 is just the first factor's digit. Source: B §2.

**R2-Q09 — D.** Modulo 45 the remainders at exponents n=1,2,3,4,5,6 are respectively `12,9,18,36,27,9`. From n=2 onward the last four residues repeat, since multiplication by 12 takes `9→18→36→27→9`; the initial 12 is not in that cycle. Thus five different residues occur. A: 3 omits two valid residues; B: 4 overlooks the initial, nonperiodic 12; D: 5 includes all four periodic residues and the initial one; C: 6 counts the return to 9 as a new residue. Source: A §§1–3,5 (noncoprime pre-period and eventual cycle).

**R2-Q10 — A.** Modulo 17, `7²≡−2`, `7⁴≡4`, `7⁸≡−1`, and `7^16≡1`; since `7⁸≠1` and 16 is the first power-of-two exponent producing 1, `2^n` must first reach 16 at n=4. B: n=1 gives residue 15; C: n=2 gives 4; D: n=3 gives 16; A: n=4 gives 1 for the first time. Source: A §§1–3 (tower exponent mapping and order).

**R2-Q11 — A.** Correct: A. x = 36/99 = 4/11, so x/(1 − x) = (4/11)/(7/11) = 4/7. B returns x itself and drops the denominator; C treats 0.(36) as the terminating 0.36, giving 0.36/0.64 = 9/16; D inverts the quotient. Trap: a repeating decimal must be converted before any algebra. Time target: 75 seconds.

**R2-Q12 — A.** One-digit block uses 9 digits, two-digit block uses 180: first 189 digits. The 200th is digit 11 of the three-digit block: numbers 100,101,102 take nine; digits 10–12 are 103, hence second digit is 0. B: 1 is first digit of 103; C: 3 is third; D: 2 is final digit of previous number 102; A: 0 is second digit of 103. Source: B §5.2; 2025 concatenation neutral route.

**R2-Q13 — D.** The difference `9(a−b)=27` requires tens digit a to exceed units digit b by 3. Divisibility by 9 requires `a+b` to be 9 or 18; the feasible pairs with gap 3 include (6,3), giving 63, whose reverse 36 passes the last-two-digit test for 4. A: 72 is 9-divisible, but its reverse 27 fails 4 and its difference is 45; D: 63 passes all tests; B: 54 is 9-divisible but differs from 45 by 9; C: 81 is 9-divisible but differs from 18 by 63. Source: B §§2,5.2.

**R2-Q14 — A.** Multiples of 4, 6 and 9 up to 180 number 45, 30 and 20. Their pairwise LCM counts are 15 (12), 5 (36) and 10 (18); the triple LCM count is 5 (36). The union has `45+30+20−15−5−10+5=70`, leaving `180−70=110` in none. B: 120 ignores exclusion of 9; C: 115 forgets to restore the five triple-overlap cases; D: 105 subtracts five additional cases already excluded; A: 110 is the correct complement. Source: B §5.4; A §5 (three-set inclusion–exclusion).

**R2-Q15 — D.** `(2/1)^−3=1/8`, `√(9/1)=3`, `(1/2)^−2=4`, and `(5/2)^1=5/2`. A: 1/8 is the reciprocal of 8; B: 3 is below 4; D: 4 alone is greatest; C: 5/2 is below 4 even though the base exceeds 2. Source: B §5.3; historical magnitude route.

**R2-Q16 — D.** Sixteen full periods sum to 16(3−1+2)=64, with 2 remaining terms 3−1=2: total 66. D: 66 correct; A: 64 omits remainder; B: 68 adds entire extra period; C: 70 treats last two as 3+3. Source: B §10, closure; 2024 periodic-sum neutral route.

**R2-Q17 — A.** The central factorial quotient is an integer. The full floor sums give `v₂(64!)=32+16+8+4+2+1=63` and `v₂(32!)=16+8+4+2+1=31`. Thus `v₂(64!/(32!)²)=63−2·31=1`: it is divisible by 2, not by 4. B: 0 overlooks the one surviving factor; A: 1 is exact; C: 2 incorrectly leaves a second factor; D: 3 incorrectly leaves two extra factors. Source: B §2; A §§2–3,5 (factorial valuations and cancellation).

**R2-Q18 — B.** `7⁴≡01 (mod 100)` while `7,49,43,01` are the first four two-digit residues. The target 43 occurs exactly at `n≡3 (mod 4)`: n=3,7,...,103 gives `(103−3)/4+1=26` occurrences. A: 25 omits the inclusive last exponent 103; B: 26 counts all occurrences; C: 27 includes one beyond 103; D: 28 includes two beyond 103. Source: A §§2–5 (two-digit periodic residues and inclusive endpoints).

**R2-Q19 — D.** `72=2³·3²`. The first four terms 5·6·7·8 contain plenty of 2s, but only one factor of 3 (from 6); the fifth term 9 supplies two more factors of 3. Thus 5·6·7·8·9 first becomes divisible by 72. A: three terms cannot supply enough 2s or 3s; B: four have insufficient 3s; D: five meet both prime-exponent thresholds; C: a sixth term is unnecessary. Source: B §§2,7; A §2; consecutive-integer valuation route.

**R2-Q20 — B.** Correct: B. −√16 = −4, an integer and negative, hence not whole. A is whole; C (4) is whole; D (−1/2) is not an integer. Trap: a root symbol can hide an integer, and negative integers are excluded from the whole numbers. Time target: 45 seconds.

**R2-Q21 — C.** The terminal three digits x20 are `100x+20≡4x+4 (mod 8)`, so divisibility by 8 requires an odd digit x: 1,3,5,7 or 9. Their full digit sum is 9+x; only x=9 passes 9 too, leaving four permissible digits. A: 3 misses one valid odd digit; C: 4 counts exactly 1,3,5,7; B: 5 includes the both-divisible x=9; D: 6 admits an invalid even digit. Source: B §§2,5.3.

**R2-Q22 — A.** Correct: A. The divisors not divisible by 6 are 1, 2, 3, 4, 5, 8, 9, 10, 15, 20, 40, 45, with sum 162. Shortcut: σ(360) = 1170 minus the sum of the divisors divisible by 6, which is 6 × σ(60) = 6 × 168 = 1008; 1170 − 1008 = 162. B drops the divisor 1; C (195) is σ(72), the divisor sum of a different number; D (1170) is σ(360) and ignores the exclusion. Trap: 'not divisible by 6' must be checked for both primes 2 and 3. Time target: 120 seconds.

**R2-Q23 — B.** Correct: B. Writing a = 12x and b = 12y gives gcd(x, y) = 1 and lcm(x, y) = 60 = 2² × 3 × 5. Each of the three prime powers 2², 3 and 5 goes wholly to a or to b, giving 2³ = 8 ordered pairs. A counts unordered pairs; C miscounts the splits; D treats 2² as two separate primes and counts 2⁴. Trap: ordered and unordered counts differ. Time target: 90 seconds.

**R2-Q24 — A.** Values congruent to 4 modulo 6 are 4,10,16,22,...; impose remainder 1 modulo 5 to get 16,46,76 in [1,100], three values (period lcm(5,6)=30). B: 2 misses 76; C: 4 includes 106 outside range; D: 5 includes further out-of-range values; A: 3 exact. Source: B §§4–5.4; 2025 simultaneous-remainder route.

**R2-Q25 — B.** The only zeroes from 1 through 99 are units in 10,20,...,90: nine. A: 8 omits one ten; B: 9 exact; C: 10 includes 100 outside range; D: 11 counts 100's two zeroes. Leading zeroes in 01..09 are never written. Source: B §5.2; historical digit-frequency route.

**R2-Q26 — B.** Powers modulo 24 are 2,4,8,16,8,16,...; the cycle 8,16 begins at n=3 (not n=1). A: at 1 the residue is 2; C: at 2 it is 4; B: at 3 it is 8 followed by 16 repeatedly; D: at 4 the cycle has begun already and starts there at 16, not 8. Source: A §§1–5 (pre-period).

**R2-Q27 — D.** The factorial quotient is the integer `6·7·8·9·10·11·12·13·14·15=10,897,286,400`; removing its two trailing zeroes gives `108,972,864`, ending in 4. Equivalently `v5(15!)−v5(5!)=3−1=2`, with enough 2s to pair. A: 2 loses contributions from the remaining odd factors; B: 8 is the last nonzero digit of 15! **without** division by 5!; D: 4 is exact; C: 6 treats the cancelled factors of 5 incorrectly. Source: B §2; A §2; historical terminal-digit neutral route.

**R2-Q28 — B.** In [51,250], counts of multiples of 6, 10 and 15 are 33, 20 and 13. Every pair and all three intersect at multiples of 30, of which there are `⌊250/30⌋−⌊50/30⌋=7`. The three exclusive-only counts are `33−7=26`, `20−7=13` and `13−7=6`, totalling 45. A: 39 counts exactly one of *only* 6 and 10 and omits the 15-only category; B: 45 includes all three exclusive categories; C: 52 counts their union and includes all seven triple-overlap cases; D: 66 counts each category without removing overlap. Source: B §5.4; A §§2,5–6.

**R2-Q29 — D.** With `x=0.0181818…`, `1000x−10x=18.1818…−0.1818…=18`, so `x=18/990=1/55`. D: exact; A: 1/50 is terminating 0.02; B: 2/55 is twice the required value; C: 1/45=0.0(2), not 0.0(18). Source: B §5.1.

**R2-Q30 — C.** On [−3,2], zero belongs to the interval, so min x²=0; greatest absolute value is 3, so max x²=9. A: min 4 ignores zero; C: (0,9) correct; B: max 4 incorrectly treats x=2 as largest absolute endpoint; D: misses both facts. Squaring does not preserve the order of negative endpoints. Source: B §5.3, closure.

**R2-Q31 — C.** Primes below 20 are `2+3+5+7+11+13+17+19=77`, hence units digit 7. A: 4 omits prime 3 (`77−3=74`); B: 5 omits prime 2 (`77−2=75`); C: 7 is exact; D: 6 incorrectly includes composite 9 (`77+9=86`). Source: B §§3,7; 2024 prime-sum unit-digit route.

**R2-Q32 — A.** The alternating difference of `2a19b` is `(2+1+b)−(a+9)=b−a−6`. For nonzero digits a,b, its range is −14..2, so it can equal 0 (`b−a=6`: three pairs (1,7),(2,8),(3,9)) or −11 (`a−b=5`: four pairs (6,1),(7,2),(8,3),(9,4)). Total seven pairs. B: 5 omits two pairs; C: 6 omits one; A: 7 includes both the zero and the negative-11 routes; D: 8 includes one invalid pair. Source: B §§2,5.3.

**R2-Q33 — A.** Correct: A. 1800 = 2³ × 3² × 5². Divisibility by 10 needs the 2-exponent in {1, 2, 3} and the 5-exponent in {1, 2}; not divisible by 9 needs the 3-exponent in {0, 1}. Count = 3 × 2 × 2 = 12. B allows only the 3-exponent 0; C ignores the 9-exclusion (3 × 3 × 2 = 18); D counts 2-exponents 0–3 and 5-exponents 0–2, ignoring the 10-requirement (4 × 2 × 3 = 24). Trap: divisibility by 10 needs both 2 and 5. Time target: 90 seconds.

**R2-Q34 — A.** Correct: A. 101 = 8 × 12 + 5 = 5 × 18 + 11. Both congruences recur with period lcm(12, 18) = 36, so the solutions are 29, 65, 101, 137, and so on. B (29) is the least solution but lies below 100; C (65) also satisfies both congruences and still fails the bound; D (137) is the next solution after 101. Trap: the bound selects the first solution above 100, not the first solution overall. Time target: 90 seconds.

**R2-Q35 — C.** `(-9)^0=1`, so multiplying by `(-9)^21` leaves its value unchanged; the odd negative power ends in −9, whose least nonnegative residue modulo 10 is 1. A: 0 mistakes a nonzero product for zero; C: 1 is correct; B: 8 is the magnitude of the incorrect difference `1−9=−8`, not the product's residue; D: 9 drops the negative sign. Source: B §§2–3; A §4.

**R2-Q36 — C.** Correct: C. The qualifying primes are 61 (71), 73 (83), 79 (89) and 97 (107). A omits 97; B adds 71, whose partner 81 is composite; D also adds 89, whose partner 99 is composite. Trap: each candidate needs both p and p + 10 tested. Time target: 90 seconds.

**R2-Q37 — C.** Correct: C. √8 + √2 = 2√2 + √2 = 3√2, irrational. A = 0.5 + 4 = 4.5, rational; B = √9 = 3, rational; D = 2√2 ÷ 2√2 = 1, rational. Trap: a radical expression must be simplified before its nature is judged. Time target: 75 seconds.

**R2-Q38 — B.** Correct: B. 720 = 2⁴ × 3² × 5. Divisibility by 12 needs the 2-exponent ≥ 2 and the 3-exponent ≥ 1; not divisible by 8 needs the 2-exponent exactly 2. Choices: 2-exponent 2 (one option), 3-exponent 1 or 2 (two options), 5-exponent 0 or 1 (two options): 12, 36, 60, 180. A keeps only 12 and 36; C allows the 2-exponent 3 and so ignores the 8-exclusion; D counts all divisors divisible by 12 and ignores the 8-exclusion. Trap: 'not divisible by 8' restricts the 2-exponent to exactly 2. Time target: 90 seconds.

**R2-Q39 — C.** Only perfect squares have an odd number of positive divisors: their square-root divisor is unpaired. A: `18=2·3²` has 6 divisors; C: `36=2²·3²` has 9; B: `72=2³·3²` has 12; D: `108=2²·3³` has 12. Source: B §§2,6–7.

**R2-Q40 — B.** Correct: B. 315 = 3² × 5 × 7. For a prime power p^e, the ordered pairs of exponents with maximum e number 2e + 1, so the count is 5 × 3 × 3 = 45. A ignores the prime 5 (3 × 3 × 1 = 9); C treats 3² as 3¹ (27); D uses 4 choices for 3² (36), omitting one of the five exponent pairs. Trap: the LCM counts exponent pairs with the maximum exactly e, not the exponent itself. Time target: 90 seconds.

**R2-Q41 — D.** For remainder 2, d must divide `62−2=60` and `122−2=120`, and exceed 2. The divisors of gcd(60,120)=60 within [5,15] are 5,6,10,12,15; their sum is 48. A: 42 omits 6; B: 45 misadds the five eligible divisors; D: 48 includes all five; C: 50 incorrectly includes the remainder 2 as though it were a divisor. Source: B §§2,4,6–7; 2025 fixed-remainder neutral route.

**R2-Q42 — D.** If each pair has HCF1, a prime factor can occur in only one input, so the LCM is their product and the triple HCF is 1. A: (2,3,6) has common HCF1, but LCM6 differs from product36; B: (3,9,15) are all odd but not pairwise coprime; D: pairwise HCF1 suffices; C: (4,6,8) are composite but the identity fails. Source: B §§2,4; A §5.

**R2-Q43 — C.** Correct: C. The common piece length is HCF(144, 216, 360) = 72, giving 2 + 3 + 5 = 10 pieces. A uses only the first two ropes (2 + 3); B uses HCF 36 (4 + 6 + 10); D uses HCF 24 (6 + 9 + 15). Trap: the common piece length is the HCF over all the ropes, not a pairwise value. Time target: 90 seconds.

**R2-Q44 — A.** For each prime, the LCM uses the larger exponent of that prime in a or b. Here a=72 supplies 2³·3², but b must supply 2⁴ and 5. B: `b=80=2⁴·5` gives the stated LCM; C: `240=2⁴·3·5` also does; D: `720=2⁴·3²·5` does; A: `40=2³·5` gives LCM `2³·3²·5=360`, not 720. Source: B §§2,4; A §5.

**R2-Q45 — C.** Every positive power of 6 ends in 6, while even positive powers of 4 end in 6; `6+6=12` ends in 2. A: 0 wrongly treats the second summand as 4; C: 2 is correct; B: 4 simply repeats the second base rather than evaluating and adding both powers; D: 6 retains only one summand. Source: B §§2–3,7.

**R2-Q46 — D.** The repeated number equals `(407+10x)·1001001`. Since `1001001=3·333667` and `333667` is not divisible by 3 (digit sum 28), the multiplier contains precisely one factor of 3. For the product to be divisible by 9 but not 27, the block must contain precisely one factor of 3. Its digit sum is `11+x`, divisible by 3 for `x=1,4,7`; the sums are 12, 15 and 18 respectively. At `x=7`, `477=9·53`, so this value makes the product divisible by 27; `417=3·139` and `447=3·149` do not. D: 2 counts x=1 and 4 only; A: 1 mistakenly retains only one qualifying block; B: 3 includes x=7 despite its extra factor of 3; C: 0 wrongly treats every triple repetition as 27-divisible. Source: B §§2,5.2; A §5 (valuation); repeated-block neutral route.

**R2-Q47 — B.** Ordered digit pairs (a,b) with a+b=9 and a,b both nonzero are (1,8),…,(8,1): eight. The pair (9,0) gives 90 but reversal 09 is not two-digit. A: 7 omits a valid pair; B: 8 counts exactly the permissible pairs; C: 9 includes (9,0); D: 10 incorrectly includes a leading-zero original as well. Source: B §5.2; reversal boundary route.

**R2-Q48 — C.** An even-length repunit is divisible by 11: its alternating digit sums both equal 5. A: 3 fails because digit sum is 10; B: 7 does not divide the ten-one repunit (`1111111111 mod 7=5`); C: 11 divides by alternating sums; D: 37 does not divide (`1111111111 mod 37=1`). Source: B §§2,5.2; historical repunit route.

**R2-Q49 — C.** The distinct numbers are 225,252,522; each digit 2 occurs twice but the two copies must not generate duplicate arrangements. Their sum is `225+252+522=999`. A: 774 omits 225; B: 747 omits 252; C: 999 totals each distinct integer once; D: 1998 double-counts every arrangement by treating the two 2s as distinguishable. Source: B §5.2; historical digit-permutation route.

**R2-Q50 — B.** Correct: B. (1/4)^(−3/2) = 4^(3/2) = 8 and (1/8)^(2/3) = 8^(−2/3) = 1/4, product 2. A reverses both exponent signs; C ignores the second factor; D inverts the second factor (8^(2/3) = 4, so 8 × 4 = 32). Trap: a negative fractional exponent takes a reciprocal and then a root. Time target: 90 seconds.

**R2-Q51 — D.** Count the union of three sets: singles `30+20+12=62`; pair intersections for divisors 6,10,15 give `10+6+4=20`; restore multiples of 30 counted too few times, `2`. Thus `62−20+2=44`. A: 42 omits the triple intersection; B: 43 restores only one triple-overlap member; D: 44 is exact; C: 45 adds one extra member. Source: B §5.4; A §§2,5–6.

**R2-Q52 — A.** Pages 1..9 use 9 digits; pages 10..99 use `90·2=180`; pages 100..120 use `21·3=63`. The full count is 252; removing 53 and 54 takes away four digits, leaving 248. A: 248 is exact; B: 246 removes six digits; C: 250 removes only two; D: 252 forgets the torn sheet. Source: B §5.2; historical torn-leaf digit route.

**R2-Q53 — D.** Each decimal digit is at most 9, so four digits have sum at most 36<44. Five digits suffice: the number 89999 has digit sum `8+9+9+9+9=44`. A: four digits cannot reach 44; D: five is attainable and minimal; B: six digits are possible but not minimal; C: seven are likewise unnecessary. Source: B §5.2; digit-sum bound route.

**R2-Q54 — D.** The first five terms are 2,6,12,20,30; successive differences are 4,6,8,10 and their HCF is 2. A: 1 divides but is not greatest; B: 4 fails to divide 6 and 10; C: 6 fails to divide 4; D: 2 divides all four differences. Source: B §§4,10; differences as number property rather than an open-ended series puzzle.

**R2-Q55 — A.** Correct: A. The terms a_3 to a_8 are 12, −24, 48, −96, 192, −384, summing to −252. Shortcut: geometric sum with first term 12 and ratio −2 over six terms: 12(1 − 64)/(1 + 2) = −252. B stops at a_7 (sum 132); C reverses the sign of the sum; D reports only a_8. Trap: a negative ratio alternates signs, and a miscounted number of terms shifts the sum. Time target: 90 seconds.

**R2-Q56 — B.** Recurrence gives `0,1,0,1,…`; each two-term pair sums to 1. There are `2026/2=1013` pairs. A: 1012 drops one pair; C: 2025 counts positions rather than values; B: 1013 is exact; D: 2026 treats every term as 1. Source: B §§7,10; recurrence and finite periodic sum method.

**R2-Q57 — A.** Rearranging gives `(a−8)(b−8)=64`, with both factors positive. To maximize b, minimize `a−8` to 1, giving a=9 and b=8+64=72; this meets a≤b. B: 64 is smaller than the feasible maximum; C: 70 is not maximal; A: 72 is feasible and greatest; D: 80 would require `b−8=72`, not a divisor of 64. Source: B §6 and 2025 unit-fraction neutral route.

**R2-Q58 — A.** The missing pages sum to `3240−3181=59`. For consecutive pages p,p+1, `2p+1=59`, so p=29 and its partner30. B: (28,29) sum57; C: (31,32) sum63; D: (30,31) sum61; A: (29,30) sum59. Source: B §5.2 and historical torn-leaf page-sum neutral route.

**R2-Q59 — C.** The 6-and-5 condition gives multiples of lcm(6,5)=30: strictly inside the bounds these are 120,150,180,210,240,270. Among them 150,210,270 fail divisibility by 4, leaving three. A: 2 drops one valid multiple; B: 5 retains two multiples of 4; D: 4 retains one multiple of 4; C: 3 is exact. Source: B §5.4; A §§2,5; 2025 strict-interior route.

**R2-Q60 — C.** Cubing multiplies each prime exponent by 3, so `HCF(a,b)=∛216=6` and `LCM(a,b)=∛27000=30`. For two positive integers `ab=HCF(a,b)·LCM(a,b)=6·30=180`; the pair (6,30) realizes it. A: 150 violates the identity; C: 180 is exact; B: 210 violates it; D: 240 violates it. Source: B §§2,4 and 2026 cube-relation neutral route.

**R2-Q61 — B.** Values `2^n−1` for n=2..8 are 3,7,15,31,63,127,255. Exactly 3,7,31,127 are prime (for 127, check primes 2,3,5,7,11 ≤√127); the rest are composite. B: 4 counts all four; A: 3 misses one; C: 5 counts a composite; D: 6 counts two composites. Source: B §§6–7 and 2025 prime-expression count neutral route.

**R2-Q62 — A.** `24=2³·3` and `30=2·3·5` each have eight positive divisors, despite different exponent patterns. B: (30,36) gives (8,9); C: (24,36) gives (8,9); A: (24,30) gives (8,8); D: (36,40) gives (9,8), since `36=2²·3²` and `40=2³·5`. Source: B §§2,6; 2025 factor-count invariance neutral route.

**R2-Q63 — C.** Writing the original number as `10a+b` and its reversal as `10b+a`, their sum is `11(a+b)=132`, so `a+b=12`. For a positive difference `9(a−b)`, maximise `a−b` subject to nonzero digits at most 9: `a=9,b=3`, giving `93−39=54`. A: 18 comes from the feasible but nonmaximal pair (7,5); C: 54 is attained by (9,3); B: 36 is attained by (8,4) but is not greatest; D: 72 would require (10,2), which is not a pair of decimal digits. Source: B §5.2; reversal-sum bound, original application.
