# CSAT 02 — Revision 2: worked answers (original items)

**Sources:** B = `upsc-ai-kit/knowledge/CSAT/basic/02_Number-Systems-and-Number-Sense.md`; A = corresponding `advanced/02_Number-Systems-and-Number-Sense.md`. This is original practice, not official PYQ text. Provisional bank.

**R2-Q01 — B.** Zero is an integer and 0/1 is rational; the whole numbers include zero. A: zero is not prime; B: both classifications hold; C: negative integers (e.g. −2=−2/1) are rational; D: √2 is a nonzero irrational real. Source: B semantic closure, number universe.

**R2-Q02 — D.** Alternating digit sums for `53x19` differ by `(5+x+9)−(3+1)=10+x`; divisibility by 11 requires x=1. Its digit sum `18+x=19` is not divisible by 3. A: x=7 gives alternating difference 17 and digit sum 25; B: x=5 gives difference 15 and digit sum 23; C: x=3 gives difference 13 and digit sum 21 (divisible by 3); D: x=1 passes both stated conditions. Source: B §2.

**R2-Q03 — B.** Test the final three digits for 8 and the sum of all digits for 9. A: 216 is 8-divisible, but 63216 has digit sum 18 and is also 9-divisible; B: 416 is divisible by 8, while 63416 has digit sum 20, so it fails 9; C: 516 is not divisible by 8 (remainder 4); D: 916 is not divisible by 8 (remainder 4). Source: B §§2,5.3.

**R2-Q04 — C.** Other = `(8×120)/24=40`; `gcd(24,40)=8`, `lcm=120`. A: 32 gives gcd8 but lcm96; B: 48 gives gcd24; C: 40 fits both; D: 64 gives lcm192. The product identity applies only to two positive integers. Source: B §§2,4.

**R2-Q05 — B.** Pairwise differences are 48, 96 and 144, so a common-remainder divisor must divide 48. Below 40, the eligible divisors with remainders greater than 10 are 16 and 24 (each gives remainder 13); 24 is greatest. A: 16 also works but is smaller; B: 24 is greatest under the bound; C: 48 leaves 13 but violates the strict upper bound; D: 12 leaves remainder 1, violating the lower bound. Source: B §4.

**R2-Q06 — B.** A square divisor uses even exponents: 2 has choices 0,2,4,6 (4); 3 has 0,2,4 (3); 5 has 0,2 (2); total 24. A: 12 omits one of the 5-exponent choices; B: 24 counts all (including 1 and N); C: 30 counts an inadmissible odd exponent; D: 18 treats 2's four exponent choices as three. Source: B §§2,7.

**R2-Q07 — A.** Between 125! and 249!, the additional factors of 5 are `(⌊249/5⌋−⌊125/5⌋)+(⌊249/25⌋−⌊125/25⌋)+(⌊249/125⌋−⌊125/125⌋)=(49−25)+(9−5)+(1−1)=28`. Both factorials contain far more factors of 2, so this is also the difference in trailing zero counts. A: 28 counts all of them; B: 27 omits one additional factor; C: 29 double-counts one factor; D: 30 double-counts two. Source: B §2; A §§2,5.

**R2-Q08 — C.** `2^71` ends 8 (exponent ≡3 mod 4), `3^66` ends 9 (exponent ≡2), product 72 ends 2. A: 4 requires different cycle positions; B: 6 does not match 8×9; C: 2 correct; D: 8 is just the first factor's digit. Source: B §2.

**R2-Q09 — C.** Modulo 45 the remainders at exponents n=1,2,3,4,5,6 are respectively `12,9,18,36,27,9`. From n=2 onward the last four residues repeat, since multiplication by 12 takes `9→18→36→27→9`; the initial 12 is not in that cycle. Thus five different residues occur. A: 3 omits two valid residues; B: 4 overlooks the initial, nonperiodic 12; C: 5 includes all four periodic residues and the initial one; D: 6 counts the return to 9 as a new residue. Source: A §§1–3,5 (noncoprime pre-period and eventual cycle).

**R2-Q10 — D.** Modulo 17, `7²≡−2`, `7⁴≡4`, `7⁸≡−1`, and `7^16≡1`; since `7⁸≠1` and 16 is the first power-of-two exponent producing 1, `2^n` must first reach 16 at n=4. A: n=1 gives residue 15; B: n=2 gives 4; C: n=3 gives 16; D: n=4 gives 1 for the first time. Source: A §§1–3 (tower exponent mapping and order).

**R2-Q11 — A.** `100x=36+x`, hence `x=36/99=4/11`. A: 4/11 exact; B: 3/11 equals 0.(27); C: 6/11 equals 0.(54); D: 9/22≈0.40909, not 0.(36). Source: B §5.1.

**R2-Q12 — D.** One-digit block uses 9 digits, two-digit block uses 180: first 189 digits. The 200th is digit 11 of the three-digit block: numbers 100,101,102 take nine; digits 10–12 are 103, hence second digit is 0. A: 1 is first digit of 103; B: 3 is third; C: 2 is final digit of previous number 102; D: 0 is second digit of 103. Source: B §5.2; 2025 concatenation neutral route.

**R2-Q13 — B.** The difference `9(a−b)=27` requires tens digit a to exceed units digit b by 3. Divisibility by 9 requires `a+b` to be 9 or 18; the feasible pairs with gap 3 include (6,3), giving 63, whose reverse 36 passes the last-two-digit test for 4. A: 72 is 9-divisible, but its reverse 27 fails 4 and its difference is 45; B: 63 passes all tests; C: 54 is 9-divisible but differs from 45 by 9; D: 81 is 9-divisible but differs from 18 by 63. Source: B §§2,5.2.

**R2-Q14 — D.** Multiples of 4, 6 and 9 up to 180 number 45, 30 and 20. Their pairwise LCM counts are 15 (12), 5 (36) and 10 (18); the triple LCM count is 5 (36). The union has `45+30+20−15−5−10+5=70`, leaving `180−70=110` in none. A: 120 ignores exclusion of 9; B: 115 forgets to restore the five triple-overlap cases; C: 105 subtracts five additional cases already excluded; D: 110 is the correct complement. Source: B §5.4; A §5 (three-set inclusion–exclusion).

**R2-Q15 — C.** `(2/1)^−3=1/8`, `√(9/1)=3`, `(1/2)^−2=4`, and `(5/2)^1=5/2`. A: 1/8 is the reciprocal of 8; B: 3 is below 4; C: 4 alone is greatest; D: 5/2 is below 4 even though the base exceeds 2. Source: B §5.3; historical magnitude route.

**R2-Q16 — A.** Sixteen full periods sum to 16(3−1+2)=64, with 2 remaining terms 3−1=2: total 66. A: 66 correct; B: 64 omits remainder; C: 68 adds entire extra period; D: 70 treats last two as 3+3. Source: B §10, closure; 2024 periodic-sum neutral route.

**R2-Q17 — B.** The central factorial quotient is an integer. The full floor sums give `v₂(64!)=32+16+8+4+2+1=63` and `v₂(32!)=16+8+4+2+1=31`. Thus `v₂(64!/(32!)²)=63−2·31=1`: it is divisible by 2, not by 4. A: 0 overlooks the one surviving factor; B: 1 is exact; C: 2 incorrectly leaves a second factor; D: 3 incorrectly leaves two extra factors. Source: B §2; A §§2–3,5 (factorial valuations and cancellation).

**R2-Q18 — B.** `7⁴≡01 (mod 100)` while `7,49,43,01` are the first four two-digit residues. The target 43 occurs exactly at `n≡3 (mod 4)`: n=3,7,...,103 gives `(103−3)/4+1=26` occurrences. A: 25 omits the inclusive last exponent 103; B: 26 counts all occurrences; C: 27 includes one beyond 103; D: 28 includes two beyond 103. Source: A §§2–5 (two-digit periodic residues and inclusive endpoints).

**R2-Q19 — C.** `72=2³·3²`. The first four terms 5·6·7·8 contain plenty of 2s, but only one factor of 3 (from 6); the fifth term 9 supplies two more factors of 3. Thus 5·6·7·8·9 first becomes divisible by 72. A: three terms cannot supply enough 2s or 3s; B: four have insufficient 3s; C: five meet both prime-exponent thresholds; D: a sixth term is unnecessary. Source: B §§2,7; A §2; consecutive-integer valuation route.

**R2-Q20 — C.** `−√16=−4` is an integer (also rational and real); zero is whole, while the stem's positive-natural convention excludes it. A: both classes fail; B: `−4` is not irrational; C: both hold; D: zero is not positive natural. Source: B semantic closure, number universe.

**R2-Q21 — B.** The terminal three digits x20 are `100x+20≡4x+4 (mod 8)`, so divisibility by 8 requires an odd digit x: 1,3,5,7 or 9. Their full digit sum is 9+x; only x=9 passes 9 too, leaving four permissible digits. A: 3 misses one valid odd digit; B: 4 counts exactly 1,3,5,7; C: 5 includes the both-divisible x=9; D: 6 admits an invalid even digit. Source: B §§2,5.3.

**R2-Q22 — B.** Divisors use independent 2-exponent choices 0..3 and 3-exponent choices 0..2. Their sum is `(1+2+4+8)(1+3+9)=15·13=195`. A: 180 is a near undercount; B: 195 correct; C: 204 overcounts 9; D: 216 is a multiple of 72 but not its divisor sum. Source: B §2; 2025 factor-sum neutral route.

**R2-Q23 — A.** Write `a=12x,b=12y` with gcd(x,y)=1; lcm(x,y)=180/12=15, hence xy=15. Both prime factors 3 and 5 must each be allocated wholly to one of x,y: `(1,15),(3,5),(5,3),(15,1)`, four ordered pairs. A: 4 exact; B: 2 ignores pair orientation; C: 6 wrongly includes non-coprime splits; D: 8 assumes three independent prime factors. Source: B §4; 2025 LCM-HCF count route.

**R2-Q24 — D.** Values congruent to 4 modulo 6 are 4,10,16,22,...; impose remainder 1 modulo 5 to get 16,46,76 in [1,100], three values (period lcm(5,6)=30). A: 2 misses 76; B: 4 includes 106 outside range; C: 5 includes further out-of-range values; D: 3 exact. Source: B §§4–5.4; 2025 simultaneous-remainder route.

**R2-Q25 — B.** The only zeroes from 1 through 99 are units in 10,20,...,90: nine. A: 8 omits one ten; B: 9 exact; C: 10 includes 100 outside range; D: 11 counts 100's two zeroes. Leading zeroes in 01..09 are never written. Source: B §5.2; historical digit-frequency route.

**R2-Q26 — C.** Powers modulo 24 are 2,4,8,16,8,16,...; the cycle 8,16 begins at n=3 (not n=1). A: at 1 the residue is 2; B: at 2 it is 4; C: at 3 it is 8 followed by 16 repeatedly; D: at 4 the cycle has begun already and starts there at 16, not 8. Source: A §§1–5 (pre-period).

**R2-Q27 — C.** The factorial quotient is the integer `6·7·8·9·10·11·12·13·14·15=10,897,286,400`; removing its two trailing zeroes gives `108,972,864`, ending in 4. Equivalently `v5(15!)−v5(5!)=3−1=2`, with enough 2s to pair. A: 2 loses contributions from the remaining odd factors; B: 8 is the last nonzero digit of 15! **without** division by 5!; C: 4 is exact; D: 6 treats the cancelled factors of 5 incorrectly. Source: B §2; A §2; historical terminal-digit neutral route.

**R2-Q28 — B.** In [51,250], counts of multiples of 6, 10 and 15 are 33, 20 and 13. Every pair and all three intersect at multiples of 30, of which there are `⌊250/30⌋−⌊50/30⌋=7`. The three exclusive-only counts are `33−7=26`, `20−7=13` and `13−7=6`, totalling 45. A: 39 counts exactly one of *only* 6 and 10 and omits the 15-only category; B: 45 includes all three exclusive categories; C: 52 counts their union and includes all seven triple-overlap cases; D: 66 counts each category without removing overlap. Source: B §5.4; A §§2,5–6.

**R2-Q29 — A.** With `x=0.0181818…`, `1000x−10x=18.1818…−0.1818…=18`, so `x=18/990=1/55`. A: exact; B: 1/50 is terminating 0.02; C: 2/55 is twice the required value; D: 1/45=0.0(2), not 0.0(18). Source: B §5.1.

**R2-Q30 — B.** On [−3,2], zero belongs to the interval, so min x²=0; greatest absolute value is 3, so max x²=9. A: min 4 ignores zero; B: (0,9) correct; C: max 4 incorrectly treats x=2 as largest absolute endpoint; D: misses both facts. Squaring does not preserve the order of negative endpoints. Source: B §5.3, closure.

**R2-Q31 — C.** Primes below 20 are `2+3+5+7+11+13+17+19=77`, hence units digit 7. A: 4 omits prime 3 (`77−3=74`); B: 5 omits prime 2 (`77−2=75`); C: 7 is exact; D: 6 incorrectly includes composite 9 (`77+9=86`). Source: B §§3,7; 2024 prime-sum unit-digit route.

**R2-Q32 — C.** The alternating difference of `2a19b` is `(2+1+b)−(a+9)=b−a−6`. For nonzero digits a,b, its range is −14..2, so it can equal 0 (`b−a=6`: three pairs (1,7),(2,8),(3,9)) or −11 (`a−b=5`: four pairs (6,1),(7,2),(8,3),(9,4)). Total seven pairs. A: 5 omits two pairs; B: 6 omits one; C: 7 includes both the zero and the negative-11 routes; D: 8 includes one invalid pair. Source: B §§2,5.3.

**R2-Q33 — C.** Divisibility by 2 and 5 together implies a final 0; additionally check the digit sum for 9 and the final two digits for 4. A: 360 is divisible by 4 (60 is a multiple of 4); B: 540 is divisible by 4 (40); C: 270 has digit sum 9 and ends in 0, but 70 is not divisible by 4; D: 920 ends in 0 and is divisible by 4, but has digit sum 11 and fails 9. Source: B §§2,5.3,7–8.

**R2-Q34 — C.** Division algorithm gives `n=12·7+r=84+r` with `0≤r<12`, so n lies in [84,95]. The only multiple of 5 in this interval strictly above 90 is 95, giving r=11. A: r=1 gives n=85, below the required bound; B: r=6 gives n=90, not strictly greater; C: r=11 gives n=95 and meets both conditions; D: r=12 is an inadmissible remainder (and would make n=96). Source: B §4; fixed-quotient and remainder-bound route.

**R2-Q35 — B.** `(-9)^0=1`, so multiplying by `(-9)^21` leaves its value unchanged; the odd negative power ends in −9, whose least nonnegative residue modulo 10 is 1. A: 0 mistakes a nonzero product for zero; B: 1 is correct; C: 8 is the magnitude of the incorrect difference `1−9=−8`, not the product's residue; D: 9 drops the negative sign. Source: B §§2–3; A §4.

**R2-Q36 — C.** Only 2 and 53 are prime: 1 is neither prime nor composite, 49 is `7²`, 51 is `3·17`, and 57 is `3·19`; test 53 with primes at most √53, namely 2,3,5,7. A: 1 omits one prime; B: 3 counts a composite or 1; C: 2 counts exactly 2 and 53; D: 4 counts at least two composites. Source: B §§6–7, closure.

**R2-Q37 — A.** `√(−4)` is nonreal (in the real-number setting); `−√25=−5` is a rational integer; `√3` is irrational and real. A: all three positions match; B: swaps the classifications of −5 and √3; C: wrongly labels √(−4) real; D: wrongly labels −5 irrational. Source: B §§5.3,7, closure.

**R2-Q38 — D.** Divisibility by 3 and 4 is sufficient for 12 because these divisors are coprime; it does not require divisibility by 8. A: 48 is divisible by 8; B: 72 is divisible by 8; C: 96 is divisible by 8; D: 36 is divisible by 3 and 4, but 36 is not divisible by 8. Source: B §§2,7–8.

**R2-Q39 — B.** Only perfect squares have an odd number of positive divisors: their square-root divisor is unpaired. A: `18=2·3²` has 6 divisors; B: `36=2²·3²` has 9; C: `72=2³·3²` has 12; D: `108=2²·3³` has 12. Source: B §§2,6–7.

**R2-Q40 — C.** Each input divides its LCM; if either input is even, the LCM must be even. A: one even input contradicts an odd LCM; B: an even HCF would also force even inputs and LCM; C: both inputs must be odd; D: primality is not necessary, as 9 and 15 have the odd LCM 45. Source: B §§2,4; A §5.

**R2-Q41 — C.** For remainder 2, d must divide `62−2=60` and `122−2=120`, and exceed 2. The divisors of gcd(60,120)=60 within [5,15] are 5,6,10,12,15; their sum is 48. A: 42 omits 6; B: 45 misadds the five eligible divisors; C: 48 includes all five; D: 50 incorrectly includes the remainder 2 as though it were a divisor. Source: B §§2,4,6–7; 2025 fixed-remainder neutral route.

**R2-Q42 — C.** If each pair has HCF1, a prime factor can occur in only one input, so the LCM is their product and the triple HCF is 1. A: (2,3,6) has common HCF1, but LCM6 differs from product36; B: (3,9,15) are all odd but not pairwise coprime; C: pairwise HCF1 suffices; D: (4,6,8) are composite but the identity fails. Source: B §§2,4; A §5.

**R2-Q43 — A.** The maximum common piece length is `gcd(144,216)=72` cm, giving `144/72+216/72=2+3=5` pieces. A: 5 counts both ropes completely; B: 4 loses a piece; C: 6 assumes the largest common length is shorter; D: 7 similarly overcuts. Source: B §4; A historical 2020 measurement route.

**R2-Q44 — D.** For each prime, the LCM uses the larger exponent of that prime in a or b. Here a=72 supplies 2³·3², but b must supply 2⁴ and 5. A: `b=80=2⁴·5` gives the stated LCM; B: `240=2⁴·3·5` also does; C: `720=2⁴·3²·5` does; D: `40=2³·5` gives LCM `2³·3²·5=360`, not 720. Source: B §§2,4; A §5.

**R2-Q45 — B.** Every positive power of 6 ends in 6, while even positive powers of 4 end in 6; `6+6=12` ends in 2. A: 0 wrongly treats the second summand as 4; B: 2 is correct; C: 4 simply repeats the second base rather than evaluating and adding both powers; D: 6 retains only one summand. Source: B §§2–3,7.

**R2-Q46 — A.** The repeated number equals `(407+10x)·1001001`. Since `1001001=3·333667` and `333667` is not divisible by 3 (digit sum 28), the multiplier contains precisely one factor of 3. For the product to be divisible by 9 but not 27, the block must contain precisely one factor of 3. Its digit sum is `11+x`, divisible by 3 for `x=1,4,7`; the sums are 12, 15 and 18 respectively. At `x=7`, `477=9·53`, so this value makes the product divisible by 27; `417=3·139` and `447=3·149` do not. A: 2 counts x=1 and 4 only; B: 1 mistakenly retains only one qualifying block; C: 3 includes x=7 despite its extra factor of 3; D: 0 wrongly treats every triple repetition as 27-divisible. Source: B §§2,5.2; A §5 (valuation); repeated-block neutral route.

**R2-Q47 — B.** Ordered digit pairs (a,b) with a+b=9 and a,b both nonzero are (1,8),…,(8,1): eight. The pair (9,0) gives 90 but reversal 09 is not two-digit. A: 7 omits a valid pair; B: 8 counts exactly the permissible pairs; C: 9 includes (9,0); D: 10 incorrectly includes a leading-zero original as well. Source: B §5.2; reversal boundary route.

**R2-Q48 — C.** An even-length repunit is divisible by 11: its alternating digit sums both equal 5. A: 3 fails because digit sum is 10; B: 7 does not divide the ten-one repunit (`1111111111 mod 7=5`); C: 11 divides by alternating sums; D: 37 does not divide (`1111111111 mod 37=1`). Source: B §§2,5.2; historical repunit route.

**R2-Q49 — C.** The distinct numbers are 225,252,522; each digit 2 occurs twice but the two copies must not generate duplicate arrangements. Their sum is `225+252+522=999`. A: 774 omits 225; B: 747 omits 252; C: 999 totals each distinct integer once; D: 1998 double-counts every arrangement by treating the two 2s as distinguishable. Source: B §5.2; historical digit-permutation route.

**R2-Q50 — B.** `(1/4)^(1/2)=1/2`, `(1/4)^(−1)=4`, `(1/4)^(−1/2)=2`, and any nonzero base to power zero is 1. A: 1/2 is smallest; B: 4 is greatest; C: 2 is below 4; D: 1 is below 4. Negative powers invert a positive base below one. Source: B §5.3; historical fractional-power/magnitude route.

**R2-Q51 — C.** Count the union of three sets: singles `30+20+12=62`; pair intersections for divisors 6,10,15 give `10+6+4=20`; restore multiples of 30 counted too few times, `2`. Thus `62−20+2=44`. A: 42 omits the triple intersection; B: 43 restores only one triple-overlap member; C: 44 is exact; D: 45 adds one extra member. Source: B §5.4; A §§2,5–6.

**R2-Q52 — A.** Pages 1..9 use 9 digits; pages 10..99 use `90·2=180`; pages 100..120 use `21·3=63`. The full count is 252; removing 53 and 54 takes away four digits, leaving 248. A: 248 is exact; B: 246 removes six digits; C: 250 removes only two; D: 252 forgets the torn sheet. Source: B §5.2; historical torn-leaf digit route.

**R2-Q53 — B.** Each decimal digit is at most 9, so four digits have sum at most 36<44. Five digits suffice: the number 89999 has digit sum `8+9+9+9+9=44`. A: four digits cannot reach 44; B: five is attainable and minimal; C: six digits are possible but not minimal; D: seven are likewise unnecessary. Source: B §5.2; digit-sum bound route.

**R2-Q54 — D.** The first five terms are 2,6,12,20,30; successive differences are 4,6,8,10 and their HCF is 2. A: 1 divides but is not greatest; B: 4 fails to divide 6 and 10; C: 6 fails to divide 4; D: 2 divides all four differences. Source: B §§4,10; differences as number property rather than an open-ended series puzzle.

**R2-Q55 — A.** Terms are `3,−6,12,−24`, so `3−6+12−24=−15`. A: −15 is exact; B: −21 counts the second term with the wrong magnitude; C: −9 misses one negative contribution; D: 15 incorrectly reports the absolute value of the signed sum. Source: B §§7,10; ratio/alternating-sign sequence route.

**R2-Q56 — C.** Recurrence gives `0,1,0,1,…`; each two-term pair sums to 1. There are `2026/2=1013` pairs. A: 1012 drops one pair; B: 2025 counts positions rather than values; C: 1013 is exact; D: 2026 treats every term as 1. Source: B §§7,10; recurrence and finite periodic sum method.

**R2-Q57 — C.** Rearranging gives `(a−8)(b−8)=64`, with both factors positive. To maximize b, minimize `a−8` to 1, giving a=9 and b=8+64=72; this meets a≤b. A: 64 is smaller than the feasible maximum; B: 70 is not maximal; C: 72 is feasible and greatest; D: 80 would require `b−8=72`, not a divisor of 64. Source: B §6 and 2025 unit-fraction neutral route.

**R2-Q58 — D.** The missing pages sum to `3240−3181=59`. For consecutive pages p,p+1, `2p+1=59`, so p=29 and its partner30. A: (28,29) sum57; B: (31,32) sum63; C: (30,31) sum61; D: (29,30) sum59. Source: B §5.2 and historical torn-leaf page-sum neutral route.

**R2-Q59 — D.** The 6-and-5 condition gives multiples of lcm(6,5)=30: strictly inside the bounds these are 120,150,180,210,240,270. Among them 150,210,270 fail divisibility by 4, leaving three. A: 2 drops one valid multiple; B: 5 retains two multiples of 4; C: 4 retains one multiple of 4; D: 3 is exact. Source: B §5.4; A §§2,5; 2025 strict-interior route.

**R2-Q60 — B.** Cubing multiplies each prime exponent by 3, so `HCF(a,b)=∛216=6` and `LCM(a,b)=∛27000=30`. For two positive integers `ab=HCF(a,b)·LCM(a,b)=6·30=180`; the pair (6,30) realizes it. A: 150 violates the identity; B: 180 is exact; C: 210 violates it; D: 240 violates it. Source: B §§2,4 and 2026 cube-relation neutral route.

**R2-Q61 — A.** Values `2^n−1` for n=2..8 are 3,7,15,31,63,127,255. Exactly 3,7,31,127 are prime (for 127, check primes 2,3,5,7,11 ≤√127); the rest are composite. A: 4 counts all four; B: 3 misses one; C: 5 counts a composite; D: 6 counts two composites. Source: B §§6–7 and 2025 prime-expression count neutral route.

**R2-Q62 — C.** `24=2³·3` and `30=2·3·5` each have eight positive divisors, despite different exponent patterns. A: (30,36) gives (8,9); B: (24,36) gives (8,9); C: (24,30) gives (8,8); D: (36,40) gives (9,8), since `36=2²·3²` and `40=2³·5`. Source: B §§2,6; 2025 factor-count invariance neutral route.

**R2-Q63 — B.** Writing the original number as `10a+b` and its reversal as `10b+a`, their sum is `11(a+b)=132`, so `a+b=12`. For a positive difference `9(a−b)`, maximise `a−b` subject to nonzero digits at most 9: `a=9,b=3`, giving `93−39=54`. A: 18 comes from the feasible but nonmaximal pair (7,5); B: 54 is attained by (9,3); C: 36 is attained by (8,4) but is not greatest; D: 72 would require (10,2), which is not a pair of decimal digits. Source: B §5.2; reversal-sum bound, original application.
