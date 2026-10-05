# CSAT 02 — Revision 3: worked answers (original items)

**Sources:** B = `upsc-ai-kit/knowledge/CSAT/basic/02_Number-Systems-and-Number-Sense.md`; A = corresponding `advanced/02_Number-Systems-and-Number-Sense.md`. Neutral PYQ demand routes in B do not verify exact official answers. Provisional bank.

**R3-Q01 — B.** A: 1 has one divisor and is not prime; B: 2 has only 1,2 as divisors and every other even integer >2 is composite; C: 0 is not composite; D: −2=−2/1 is rational. Source: B semantic closure, number universe.

**R3-Q02 — D.** Divisibility by 6 requires 2 and 3; to reach 12 one additionally needs 4 (3 and 4 coprime). A: 24 passes 12; B: 36 passes 12; C: 48 passes 12; D: 54 is even and 3-divisible but last two digits 54 are not divisible by 4. Source: B §§2,7–8.

**R3-Q03 — B.** Alternating sum `(3+1)−(x+6)=−(x+2)` is divisible by 11 only for digit x=9, yielding `3916` and a negative alternating difference of −11. Its final two digits 16 are divisible by 4 and final digit 6 rules out 5. A: ending 6 fails 5; B: 4 holds and 5 fails; C: ending 6 fails 5; D: 3916 is divisible by 4 as well as 2. Source: B §§2,5.3.

**R3-Q04 — C.** `144=2⁴·3²` has 15 divisors. Its multiples 144, 288 (`2⁵·3²`) and 432 (`2⁴·3³`) have 15, 18 and 20 divisors respectively; the next multiple, 576=`2⁶·3²`, has `(6+1)(2+1)=21`. Thus 4 is the least eligible m. A: m=2 gives 18 divisors; B: m=3 gives 20; C: m=4 gives 21; D: m=5 introduces a third prime and gives `(5)(3)(2)=30`. Source: B §§2,7.

**R3-Q05 — B.** `12=2²·3`, `18=2·3²`, `20=2²·5`; lcm `2²·3²·5=180`. The first multiple above 250 is 360, and `360 mod 16=8`. A: 180 is below the bound; B: 360 meets all conditions and is least; C: 720 is divisible by 16; D: 540 meets the divisibility tests but is larger than 360. Three-number HCF×LCM is not their product. Source: B §§2,4; A §5.

**R3-Q06 — A.** Subtract fixed remainder 4: gcd(90,120,150)=30, and `4<30`. A: 30 gives quotient 3,4,5 and remainder 4; B: 20 fails 90; C: 25 fails 90; D: 15 works but smaller. Source: B §4; historical divisor-remainder route.

**R3-Q07 — A.** Numbers ≡2 mod5 are 52,57,62,67… above 50; 52≡3 mod7. A: 52 satisfies both; B: 57≡1 mod7; C: 63≡0 mod7 and 3 mod5; D: 67≡4 mod7. The smallest positive solution is 17, but it is outside the asked range. Source: B §4; 2025 simultaneous-remainder neutral route.

**R3-Q08 — B.** Any nonzero base to exponent 0 is 1; 4^17 ends in 4 (odd exponent in 4,6 cycle), so last digit 5. A: 3 arises by treating `8⁰` as −1; B: 5 exact; C: 7 would require units 3 or 6; D: 9 treats `8⁰` as 5. Source: B §§2,7.

**R3-Q09 — A.** Though gcd(2,6)>1, residues alternate 2,4 from exponent 1; 51 is odd so remainder 2. A: 2 is odd-power residue; B: 1 is not in the eventual cycle; C: 0 is never reached; D: 4 is even-power residue. Noncoprime does **not** always imply stabilization. Source: A §§2–5.

**R3-Q10 — D.** Mod12: `2¹≡2`, `2²≡4`, `2³≡8`, `2⁴≡4` and then 8/4 alternate. `3^10` is odd and ≥3, hence remainder 8. A: exponent-1 residue ignores pre-period; B: even exponent only; C: never in residue list; D: correct eventual odd exponent. Source: A §§1–5.

**R3-Q11 — A.** `v5(125!)=⌊125/5⌋+⌊125/25⌋+⌊125/125⌋=25+5+1=31`. A: 31 exact; B: 30 misses the extra factor from 125; C: 29 misses two extra factors; D: 26 counts 25 base factors and the extra 125 factor but omits all five extra factors supplied by multiples of 25. Source: A §§2,5.

**R3-Q12 — A.** Factor the sum as `(30!/20!)·(1+70!/30!)`. The first factor has `v5=(6+1)−4=3` with more than three factors of 2, hence exactly three trailing zeroes. The second factor is one plus a multiple of 10 and so has no factor of 2 or 5. A: 3 is exact; B: 9 subtracts the two summands' trailing-zero counts (12−3); C: 12 counts only the first summand; D: 15 adds the counts (12+3) as if the summands were multiplied. Source: B §2; A §§2,5.

**R3-Q13 — C.** Between 1–99, 7 occupies the unit place 10 times and tens place 10 times (77 counted twice, as required). In 100–150, units 7 occurs 107,117,127,137,147: five times. A: 20 omits the last range; B: 24 omits one 7; C: 25 exact; D: 30 overcounts. Source: B §5.2; historical digit-frequency route.

**R3-Q14 — D.** `x=45/990=1/22` because one zero precedes the repeating pair; `y=45/99=5/11`, so `x+y=1/22+10/22=1/2`. A: 9/22 undercounts y by 2/22; B: 5/11 keeps only y; C: 11/20 uses an incorrect tenths denominator; D: 1/2 equals the sum. Source: B §5.1.

**R3-Q15 — D.** Multiples of 4 =60, of 6 =40, of lcm(4,6)=12 =20; union=60+40−20=80. A: 120 adds overlap instead of removing it; B: 100 double-counts common multiples; C: 60 counts just multiples of 4; D: 80 exact. Source: B §5.4; A §5.

**R3-Q16 — B.** Successive terms 1,2,3,5,8,13,21. A: 18 mis-adds the last pair; B: 21 is seventh; C: 26 doubles 13; D: 34 is eighth. Specified recurrence, not extrapolation from three ambiguous terms. Source: B closure; 2026 recurrence neutral route (cross-owned with Topic 08).

**R3-Q17 — C.** `x²=9` permits x=−3 or x=3; the greater real solution is 3. A: −9 squares to 81; B: −3 is a root but smaller; C: 3 is the larger root; D: 9 squares to 81. Never discard the negative root before comparing. Source: B §5.3, closure.

**R3-Q18 — A.** Each of 1,2,3 appears twice in each of hundreds, tens and units places: `2(1+2+3)(100+10+1)=1332`. A: 1332 exact; B: 1233 undercounts hundreds; C: 1323 swaps a tens and units contribution; D: 1221 loses one place-weight unit. Source: B §5.2; historical digit-permutation neutral route.

**R3-Q19 — B.** `9^10≡01 (mod 100)`, hence `9^21≡09`; also `7^4=2401≡01 (mod 100)`. Subtract to get `09−01=08`, retaining the leading zero. A: 06 subtracts too much; B: 08 is exact; C: 09 omits the second term; D: 81 is the residue of a much smaller power of 9. Source: A §§2,5.

**R3-Q20 — B.** `⌊220/7⌋−⌊99/7⌋=31−14=17`, from 105 to 217. A: 16 omits one endpoint; B: 17 exact; C: 18 includes 98; D: 19 includes 98 and 224. Source: B §5.4.

**R3-Q21 — C.** Expand the sum: `3n²+6n+5 ≡2 (mod 3)` for every integer n. A: zero is impossible since 5≡2; B: one does not follow from the expansion; C: two is invariant; D: n cancels modulo 3, so no dependence remains. Check n=0 → 5, n=1 →14, both leave 2. Source: B §§3–4,7; historical consecutive-integer route.

**R3-Q22 — D.** `n²+n=n(n+1)` is even for every integer because one of the consecutive factors is even; adding 1 gives an odd result. A: n odd also works; B: n even also works; C: n=0 yields 1, an odd counterexample; D: correct for all integers. Source: B §7, consecutive-integer/parity methods.

**R3-Q23 — B.** `√50/√2=√25=5`, an integer and therefore rational; zero is whole but is excluded by the stated positive-natural convention. A: both wrong; B: both right; C: quotient class wrong; D: zero class wrong. Source: B semantic closure, number universe and roots.

**R3-Q24 — C.** For decimal 9-divisibility use the digit sum; for 4 use the last two digits. A: 900 has sum 9 and terminal 00, so passes both; B: 960 has digit sum 15, so fails 9; C: 990 has digit sum 18 and terminal 90 (not divisible by 4); D: 920 has digit sum 11, so fails 9. Source: B §2.

**R3-Q25 — D.** Positive divisors of 36 divisible by 3 are 3,6,9,12,18,36, totalling 84. A: 72 omits 12; B: 78 omits 6; C: 90 double-counts the eligible divisor 6; D: 84 includes each eligible divisor exactly once. Source: B §§2,7; 2025 constrained factor-sum neutral route.

**R3-Q26 — C.** `gcd(4,6,9)=1`, `lcm(4,6,9)=36`, and the product is 216; ratio `216/(1·36)=6`. A: 2 misses prime-exponent duplication; B: 3 misses the repeated 2; C: 6 exact; D: 12 doubles the actual ratio. Two-number `HCF·LCM=product` cannot be extended to three. Source: B §§2,4,8.

**R3-Q27 — D.** A common remainder requires the divisor to divide `73−38=35` as well as `38−r` and `73−r`, with `0≤r<d`. A: remainder 5 cannot equal divisor 5; B: `38 mod 6=2` and `73 mod 6=1`, not 3; C: `38 mod 8=6` and `73 mod 8=1`, not 7; D: `38=7·5+3` and `73=7·10+3`, so both give remainder 3. Source: B §4.

**R3-Q28 — B.** Reduce first: `49≡−1 (mod 10)`, `51≡1 (mod 10)`; odd exponent gives `−1+1=0`. A: 1 retains only one summand; B: 0 exact; C: 2 incorrectly treats −1 as +1; D: 9 retains only the first summand. Source: B §3; A §4.

**R3-Q29 — B.** `12^k=2^(2k)·3^k`. In 90!, `v2=45+22+11+5+2+1=86` and `v3=30+10+3+1=44`. Thus `k≤min(⌊86/2⌋,44)=43`: factors of 2, not 3, bind first. A: 41 is possible but not maximal; B: 43 uses 86 factors of 2 and 43 of the available 44 factors of 3; C: 44 needs 88 factors of 2, exceeding 86; D: 45 exceeds both valuation limits. Source: A §§2,5; 2025 highest-factor-power route.

**R3-Q30 — D.** If the original digits are a,b, reversal minus original =9(b−a)=18, so b=a+2. With both digits nonzero and ≤9, a runs 1..7: seven numbers. A: 5 wrongly restricts b≤7; B: 6 excludes one boundary case; C: 8 would allow b=10 for a=8; D: 7 includes 13 through 79 with digit gaps 2. Source: B §5.2; 2026 reversal-count neutral route.

**R3-Q31 — A.** `111111=1111·100+11`, so gcd(1111,111111)=gcd(1111,11)=11 since 1111=11·101. A: 11 exact; B: 1 ignores common factor 11; C: 101 divides 1111 but not 111111; D: 1111 does not divide the longer repunit (remainder 11). Source: B §5.2; 2025 repdigit-HCF neutral route.

**R3-Q32 — C.** Digits for 1..9:9; 10..99:180; remaining 600−189=411 digits, exactly 137 three-digit numbers (100 through `99+137=236`). A: 235 stops three digits early; B: 237 needs three more digits; C: 236 exact; D: 238 needs six more. Source: B §5.2; historical page-digit route.

**R3-Q33 — A.** Divisibility by both 2 and 5 entails a factor of 10, so the stated exception is impossible. A: no integer can satisfy it; B: 10 is divisible by 5 and 10 but not 4; C: 12 is divisible by 3 and 4 but not 5; D: 8 is divisible by 4 and 8 but not 9. Source: B §§2,5.3,7–8.

**R3-Q34 — B.** In `10!`, two factors of 5 pair with two factors of 2, so remove two terminal zeroes: `10!=3,628,800` becomes `36,288`, ending in 88. A: 28 reverses the final two digits; B: 88 is the actual pair; C: 08 drops the tens-place 8; D: 80 removes only one zero. Source: B §2; A §§2–3; historical terminal-nonzero-digit route.

**R3-Q35 — A.** Subtract blocks with the same period: `0.(81)−0.(18)=(81−18)/99=63/99=7/11`. A: 7/11 is the reduced difference; B: 9/11 keeps only the first repeating decimal; C: 7/10 falsely treats the difference as a terminating tenth; D: 63/100 uses a terminating-decimal denominator rather than 99. Source: B §5.1.

**R3-Q36 — D.** `−√49=−7` is an integer, rational and real, while 1 has only one positive divisor and is neither prime nor composite. A: −7 is not irrational and 1 is not prime; B: −7 is rational but 1 is not composite; C: both classifications are false; D: both are correct. Source: B §§5.3,6–7, closure.

**R3-Q37 — C.** `x²=2` has two real irrational roots, +√2 and −√2. `x²=0` has only the rational root 0; `x²=−2` has no real root. A: 1 omits one root of 2; B: 3 wrongly counts zero as irrational; C: 2 is exact; D: 4 incorrectly counts nonreal roots. Source: B §§5.3,7, closure.

**R3-Q38 — B.** A square divisor has even exponents, and exactly two distinct prime factors requires both exponents positive. The 2 exponent can be 2 or 4 and the 3 exponent must be 2; only 36 and 144 qualify. A: 1 omits one choice for 2; B: 2 counts both; C: 3 includes a nonsquare or a single-prime divisor; D: 4 counts a zero exponent even though that would leave only one distinct prime factor. Source: B §§2,6–7.

**R3-Q39 — D.** Each input must divide their LCM 60. A: 4 is possible with partner 60; B: 12 is possible with partner 20 (HCF4, LCM60); C: 20 is possible with partner 12; D: 24 does not divide 60, so cannot be an input regardless of its partner. Source: B §§2,4; A §5.

**R3-Q40 — A.** Reduce each entry modulo 9 and distinguish a shared nonzero residue from exact divisibility. A: 38 and 65 both leave 2; B: 36 and 54 both leave zero; C: 38 leaves 2 while 64 leaves 1; D: 45 leaves zero while 65 leaves 2. Source: B §§2,4.

**R3-Q41 — D.** Every input divides its LCM. Since one input is even (18), its LCM must be an even multiple of 18. A: 36 is possible, taking the second input as 36; B: 54 is possible with second input 54; C: 72 is possible with second input 72; D: 81 is odd and not divisible by 18, so impossible. Source: B §§2,4; A §5.

**R3-Q42 — C.** A square side must divide both 90 and 150; its largest possible length is `gcd(90,150)=30` cm. The rectangle has `90/30=3` tiles across and `150/30=5` down, or `3·5=15` tiles. A: 12 counts only four of the five rows; B: 8 adds the row and column counts instead of multiplying; C: 15 multiplies them; D: 16 counts one extra tile. Source: B §4; A historical 2020 measurement route.

**R3-Q43 — A.** For two positive integers, HCF×LCM=their product, so `6·126=756`; the pair (18,42) realizes the given HCF and LCM. A: 756 follows the two-number identity; B: 630 wrongly substitutes HCF 5 (`5·126`); C: 882 wrongly substitutes HCF 7 (`7·126`); D: 504 wrongly substitutes HCF 4 (`4·126`). This formula cannot automatically be applied to a triple. Source: B §§2,4; A §5.

**R3-Q44 — C.** If n is odd, 2n is 2 modulo 4, so 7^(2n) and 3^(2n) each end in 9, and their sum in 8. If n is even, 2n is 0 modulo 4 and both powers end in 1, sum 2. A: misses the odd-n case; B: swaps the two cases; C: (8,2) matches both; D: misses the even-n case. Source: B §§2–3; A §§1–3.

**R3-Q45 — D.** With both digits a,b nonzero, `abab=1010a+101b` and `baba=1010b+101a`; their difference is `909(a−b)`. Taking (a,b)=(1,2) produces absolute difference exactly 909, so no greater universal divisor exists. A: 101 divides 909 but is not greatest; B: 303 also divides 909 but is not greatest; C: 1111 does not divide 909; D: 909 is the maximum. Source: B §5.2; repeated-block and reversal methods.

**R3-Q46 — C.** With a=2/3, the four values are A: `a²=4/9`; B: `a^(−2)=9/4`; C: `(1−a)^(−1)=(1/3)^(−1)=3`, greatest; D: `a^(−1)=3/2`. Do not assume that every reciprocal power of a is larger than the reciprocal of its complement. Source: B §5.3, closure.

**R3-Q47 — A.** A number divisible by both 4 and 6 is divisible by their LCM 12, while one divisible by exactly one must pass just one test. A: 30 passes 6 but not 4; B: 24 passes both; C: 22 passes neither test; D: 36 passes both. Source: B §5.4; A §5.

**R3-Q48 — B.** Primes through 50 are `2,3,5,7,11,13,17,19,23,29,31,37,41,43,47`: fifteen. Exactly two of these, 2 and 3, are divisible by 2 or 3, leaving thirteen. A: 12 excludes an additional prime; B: 13 is exact; C: 14 excludes only one of 2 and 3; D: 15 excludes neither. Source: B §§5.4,6–7; historical prime-classification route.

**R3-Q49 — C.** In the inclusive interval 98..1002 there are two two-digit numbers (4 digits), 900 three-digit numbers (2700 digits), and three four-digit numbers (12 digits). Total `4+2700+12=2716`. A: 2700 counts only the three-digit block; B: 2712 omits the two-digit pair; C: 2716 counts all three blocks; D: 2720 adds an extra four-digit number. Source: B §5.2; historical page-digit route.

**R3-Q50 — B.** The smallest multiple of 9 greater than 20 is 27, so the digit sum must be at least 27. With units digit 4, the first three digits must total 23; the smallest possible leading digit is 5, forcing the next two to be 9 each. Thus 5994 is minimal. A: 4994 has digit sum 26, failing 9; B: 5994 sums to 27 and is minimal; C: 6894 also sums to 27 but is larger; D: 7794 sums to 27 but is larger. Source: B §§2,5.2,11; 2025 digit-bound neutral route.

**R3-Q51 — D.** Units of 7^n repeat 7,9,3,1 in four-term blocks, each summing to 20. There are seven blocks through n=28; omit the fourth position (units 1) in each: `7·(20−1)=133`. A: 126 subtracts two units per block; B: 140 retains all positions; C: 147 adds an extra unit per block; D: 133 removes just the seven excluded units. Source: B §§2,3,10; A §§1–3.

**R3-Q52 — A.** The factorial ratio is `a_(n+1)/a_n=(n+1)!/n!=n+1`; the least positive n making it divisible by 7 is n=6. A: 6 produces the ratio 7; B: 5 produces 6; C: 7 produces 8; D: 8 produces 9. Source: B §§2,10; factorial/ratio number-property route.

**R3-Q53 — C.** `n(n+1)/2` is odd precisely for `n≡1 or 2 (mod 4)`; its parity repeats odd,odd,even,even. The first 100 indices form 25 full four-term blocks, with two odd terms per block: 50. A: 25 takes one per block; B: 75 takes three; C: 50 takes two; D: 100 treats all as odd. Source: B §§7,10; parity/alternate-position number-property route.

**R3-Q54 — B.** Multiplying through yields `(a−5)(b−5)=25`. Its unordered positive factor pairs are (1,25) and (5,5), giving `(a,b)=(6,30)` with sum36 or `(10,10)` with sum20. A: 18 is below the feasible minimum; B: 20 is attained at a=b=10; C: 24 has no qualifying factor pair; D: 36 is possible but not minimal. Source: B §6 and 2025 unit-fraction neutral route.

**R3-Q55 — C.** Removing odd p and following even p+1 removes `2p+1≡3 (mod 4)`, so the surviving sum from 1275 must be divisible by 4. A: 1200 removes75, from pages37+38; B: 1204 removes71, from pages35+36; C: 1206 removes69, which would be pages34+35, starting even and therefore not the specified leaf; D: 1208 removes67, from pages33+34. Source: B §§5.2,7 and historical torn-leaf page-sum neutral route.

**R3-Q56 — B.** Write the number as 7k. Strict bounds give k=16..33; since `7k≡3k≡1 (mod 4)`, require `k≡3 (mod 4)`: k=19,23,27,31, or four values. A: 3 omits one quotient; B: 4 exact; C: 5 includes a boundary-ineligible quotient; D: 6 includes two. Source: B §§4,5.4; A §5; 2025 strict-interior neutral route.

**R3-Q57 — D.** `a_(n+1)−a_n=(n+1)³−n³=3n²+3n+1≡1 (mod 3)` for every positive n. A: zero misses the constant 1; B: the n-dependent terms vanish modulo 3; C: two contradicts the expansion; D: one is invariant. Source: B §§3,7,10; number-property difference method.

**R3-Q58 — B.** With a=12 and b=20, their HCF is 4 and LCM is 60. For cubes, HCF is `4³=64`, LCM is `60³=216000`, and the sum is 216064. A: 216000 omits the cubic HCF; B: 216064 is exact; C: 216400 adds 400 instead of 64; D: 216640 adds 640 instead of 64. Source: B §§2,4; 2026 cube-relation neutral route.

**R3-Q59 — D.** For n=1..5, `n!+1` yields 2,3,7,25,121; only the first three are prime, while `25=5²` and `121=11²`. A: 4 misclassifies one square; B: 5 misclassifies both; C: 2 omits a genuine prime; D: 3 exact. Source: B §§2,6–7 and 2025 prime-expression count neutral route.

**R3-Q60 — A.** The positive-divisor count of `p^a q^b` is `(a+1)(b+1)`; a missing prime has exponent zero. A: `p⁸` gives 9 and `p²q²` gives 3·3=9; B: both structures give 8; C: `p⁴q` gives 10 while `p²q` gives 6; D: both structures give 12. Source: B §§2,6–7 and 2025 factor-count invariance neutral route.

**R3-Q61 — B.** Terminal three digits x20 represent `100x+20≡4x+4 (mod 8)`, so x must be odd. The digit sum is `6+x`, divisible by 9 only for x=3 among 0..9; 31320 has final block 320, divisible by 8, and digit sum 9. A: 31120 passes 8 but has digit sum 7; B: 31320 passes both and is least; C: 31520 passes 8 but has digit sum 11; D: 31720 passes 8 but has digit sum 13. Source: B §§2,5.2–5.3; terminal-block and digit-sum route.

**R3-Q62 — B.** If digits a,b are nonzero, reversing gives sum `11(a+b)=121`, so a+b=11. Unordered choices within 1..9 are (2,9),(3,8),(4,7),(5,6): four. A: 3 omits one pair; B: 4 includes all four; C: 5 also counts (1,10), whose second member is not a digit; D: 6 counts (1,10) and (0,11), both invalid. Source: B §5.2; reversal-sum and digit-bound method.

**R3-Q63 — C.** Reduce each power before combining: `7^53` ends in 7 (53≡1 mod 4), `9^44` ends in 1, so the first bracket ends in 8. Likewise `3^18` ends in 9 and `2^17` ends in 2, so the second bracket ends in 7. The product ends in `8·7=56`, or 6. A: 8 keeps only the first bracket; B: 4 results from wrongly taking `2^17` to end in 6, giving `8·(9−6)=24`; C: 6 is the product's digit; D: 7 keeps only the second bracket. Source: B §§2–3,7; A §§2–3; original product-of-residues application.
