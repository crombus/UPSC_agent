# CSAT 02 — Revision 1: worked answers (original items)

**Sources:** B = `upsc-ai-kit/knowledge/CSAT/basic/02_Number-Systems-and-Number-Sense.md`; A = its `advanced/` counterpart. Year/Q identifiers in the source ledgers indicate *neutral demand routes*, not verified exact PYQs. Every explanation is independent of a supplied or provisional official key. This set remains provisional.

**R1-Q01 — C.** `(√49)/2=7/2`, rational and nonintegral. A: `(√81)/3=9/3=3`, integer; B: `−18/6=−3`, integer; C: `7/2` satisfies both conditions; D: `√11` is irrational. Trap: a quotient involving a square root can be rational when the radicand is a square. Source: B semantic closure, number universe.

**R1-Q02 — C.** Odd positions of `4x728` sum to `4+7+8=19`; even positions sum to `x+2`. Difference `17−x` must be a multiple of 11, so `x=6`. A: 3 gives 14; B: 7 gives 10; C: 6 gives 11; D: 9 gives 8. Negative alternating differences would also qualify if their magnitude were 11; not here. Source: B §2.

**R1-Q03 — B.** For 8, terminal 3 digits `x24` require `100x+24≡4x (mod 8)`, so `x` even; for 9, digit sum is `19+x`, hence `x=8`, and 824 is divisible by 8. A: 4 gives sum 23; B: 8 gives sum 27 and terminal 824; C: 1 gives 20; D: 6 gives 25. Source: B §§2,5.3.

**R1-Q04 — A.** Differences 60, 84, 144 have gcd 12. Their residues mod 12 are 5,5,5; 5<12. A: 12 works and is greatest; B: 24 does not divide 60; C: 60 does not divide 84; D: 4 works but is smaller. Source: B §4; 2024 Q18 neutral route.

**R1-Q05 — C.** `gcd(84,126)=42`; 84/42=2, 126/42=3. A: 21 works but smaller; B: 28 fails for 126; C: 42 is greatest; D: 63 fails for 84. Trap: box size is gcd, not lcm. Source: B §4; 2024 Q19 route.

**R1-Q06 — A.** Divisibility by 12 = `2^2·3`; choose powers of 2 in {2,3,4} (3), of 3 in {1,2} (2), of 7 in {0,1} (2): **12**. A: `3·2·2` is exact; B: 16 assumes a fourth permissible 2 exponent; C: 18 assumes a third permissible 3 exponent; D: 24 overcounts both the 2 and 3 choices (all divisors total 30). Source: B §2.

**R1-Q07 — D.** `⌊130/5⌋+⌊130/25⌋+⌊130/125⌋=26+5+1=32`. A: 30 omits some repeated fives; B: 31 omits 125; C: 33 adds a nonexistent higher term; D: 32 counts all three floors. Source: B §2; A §2.

**R1-Q08 — A.** `58≡2 (mod 4)`, so 7^58 ends 9; 9^41 ends 9; sum ends 8. A: 8 follows 9+9; B: 0 would require last digits summing to 10; C: 6 and D: 2 require other cycles. Source: B §2.

**R1-Q09 — A.** `6^2≡4, 6^3≡8, 6^4≡0 (mod 16)`, hence every exponent ≥4 yields 0. A: stabilized remainder; B: residue only at exponent 2; C: residue only at exponent 3; D: not a residue. Trap: no exponent-1 period may be assumed. Source: A §§2–5.

**R1-Q10 — B.** With `x=0.3272727…`, `1000x−10x=327.2727…−3.2727…=324`, so `x=324/990=18/55`. A: `3/11=0.2727…` loses the prefix; B: 18/55 is the lowest-term fraction; C: 327/990 omits the required prefix subtraction; D: 327/999 gives `0.(327)`, repeating all three digits instead of only 27. None of the three wrong choices has the same value as the answer. Source: B §5.1.

**R1-Q11 — B.** 87–99: 13×2=26; 100–213: 114×3=342; total 368. A: 365 omits the three digits of final page 213; B: 368 is exact; C: 366 omits the two digits of initial page 87; D: 363 omits both boundary pages. Count both endpoints. Source: B §5.2.

**R1-Q12 — A.** If digits a>b, a−b=5 and a+b=11, hence a=8,b=3 and original 83. A: gap 45, sum 11; B: sum 11 but gap 27; C: sum 11 but gap 63; D: sum 11 but original smaller than reversal. Source: B §5.2.

**R1-Q13 — A.** Multiples 6:30, 9:20, both 18:10. Exactly one =30+20−2·10=30. A: 30 exact; B: 40 subtracts overlap once (either); C: 20 counts just multiples of 9; D: 50 double-counts intersection. Source: B §5.4; A §5.

**R1-Q14 — D.** For 0<a<1, `a^4<a^3<a^2`, and `a^−2=1/a²>1/a=a^−1`. A: `a⁴` is smaller, not larger; B: the second inverse power is larger; C: `a³` is smaller than `a²`; D: correct reciprocal ordering. Source: B §5.3.

**R1-Q15 — C.** `10^8 < √(10^17) < 10^9`, so the integer part has 9 digits. A: 8 ignores the lower bound `10^8`; B: 10 exceeds the upper bound; C: 9 is correct; D: 17 counts the exponent instead. Source: B §5.2, closure.

**R1-Q16 — B.** The differences are 3,5,7,9 and continue as 11,13, so the sixth term is 37 and the seventh 50 (`a_n=n²+1` fits). A: 37 is the sixth term; B: 50 correct; C: 49 omits the constant 1 from the inferred formula; D: 65 is the eighth term. Source: B §10, closure; number-property pattern, not an exact PYQ.

**R1-Q17 — B.** `v3(80!)=⌊80/3⌋+⌊80/9⌋+⌊80/27⌋=26+8+2=36`. A: 34 omits the two multiples of 27; B: 36 is exact; C: 38 counts multiples of 27 twice at the final floor; D: 35 misses one of the two multiples of 27. Source: A §§2–3.

**R1-Q18 — A.** Powers of 5 mod 13: `5,12,8,1` period 4; `3^20≡1 (mod 4)`, hence residue 5. A: 5 correct; B: 8 is cycle term 3; C: 1 is cycle term 4; D: 12 is cycle term 2. Source: A §§1–3.

**R1-Q19 — C.** A repunit of length k has digit sum k, so 9 divides it exactly when `9|k`. Its alternating digit sum is 0 for even k and 1 for odd k, so 11 divides it exactly when k is even. The least even multiple of 9 is 18. A: 9 passes 9 but fails 11 (odd length); B: 11 passes neither test; C: 18 passes both; D: 22 passes 11 but its digit sum fails 9. Source: B §§2,5.2; historical repunit route.

**R1-Q20 — D.** `3^20≡01 (mod 100)` so `3^101=(3^20)^5·3≡03 (mod 100)`. A: 01 omits final factor 3; B: 09 squares the last factor; C: 27 cubes it; D: 03 retains the required leading zero. Source: A §§2–5.

**R1-Q21 — C.** Among any three consecutive integers one is divisible by 3 and at least one is even, so the product is divisible by 6; 1·2·3=6 bounds the greatest universal divisor by 6. A: 2 is universal but not greatest; B: 3 likewise; C: 6 works and is maximal; D: 12 fails already for 1·2·3. Source: B §7; historical consecutive-integer neutral route.

**R1-Q22 — D.** With natural numbers starting at 1, zero belongs to whole numbers but not natural numbers; √2 is irrational since 2 is not a rational square. A: both classifications fail; B: zero classification fails; C: radical classification fails; D: both hold. Source: B semantic closure, number universe.

**R1-Q23 — B.** The last digit 0 certifies 2, 5 and 10; the digit sum `1+1+2+5+0=9` certifies 9; the last two digits 50 are not divisible by 4. A: 4 fails and 9 holds; B: all listed assertions hold; C: 4 fails, while 5 and 10 hold; D: 2 and 10 hold, contrary to the proposed exclusions. Each option describes a logically possible combination of tests for *some* integers, so the actual numeral must be checked. Source: B §§2,7.

**R1-Q24 — B.** `18=2·3²`, `24=2³·3`, `30=2·3·5`, hence lcm `2³·3²·5=360`; least multiple above 500 is 720. A: 540 fails 8; B: 720 passes all; C: 900 fails 8; D: 1080 is a larger common multiple. Source: B §4; 2026 LCM-range neutral route.

**R1-Q25 — C.** In 12!, prime exponents of 2 and 5 are 10 and 2, respectively; remove two factors of 10. The remaining factor modulo 10 is `2^8·3^5·7·11≡6·3·7·1≡6`. A: 2 ignores remaining odd factors; B: 4 miscounts a factor of 2; C: 6 exact; D: 8 is the unit digit of 10! after removing zeros, not of 12!. Source: B §2; A §2; 2024 terminal-nonzero-digit route.

**R1-Q26 — A.** Writing `abc` for an integer from 100 through 999, `abcabc =1000·abc+abc=1001·abc`. A: 1001 divides every result; B: 1011 need not divide 123123; C: 1101 need not divide 123123; D: 1111 need not divide 123123. Source: B §5.2; historical repeated-block route.

**R1-Q27 — C.** Let `x=0.123333…`; `1000x−100x=123.333…−12.333…=111`, giving `x=111/900=37/300`. A: denominator 330 uses the wrong nonrepeating-prefix length; B: 41/300 shifts the numerator; C: exact in lowest terms; D: 123/999 repeats all three digits rather than only 3. Source: B §5.1.

**R1-Q28 — B.** Multiples of 4:30, of 10:12, of lcm(4,10)=20:6; either=30+12−6=36, neither=120−36=84. A: 78 subtracts both sets without restoring their overlap; B: 84 exact; C: 90 ignores the 10-only multiples; D: 96 over-adds the overlap. Source: B §5.4; A §§2,5.

**R1-Q29 — D.** Powers satisfying the bounds are 64, 128 and 256 (2^6 through 2^8): three. A: 2 omits a boundary-valid power; B: 4 includes either 32 or 512; C: 5 includes both 32 and 512; D: 3 exact. Source: B §5.2, closure; 2026 powers-of-two neutral route.

**R1-Q30 — C.** A: `0^−1=1/0`, undefined; B: √(−9) is not real; C: √0=0, real; D: reciprocal of √(−9) is not real either. Trap: a negative exponent requires a nonzero base; a real square root requires a nonnegative radicand. Source: B §5.3.

**R1-Q31 — A.** Units of consecutive positive powers of 2 cycle 2,4,8,6, with cycle sum 20. As `2026=4·506+2`, the final two units contribute 2+4=6. A: 6 exact; B: 4 is only the second leftover term; C: 8 is the third cycle term; D: 2 is only the first leftover term. Source: B §2; A §§2–3; historical cyclic-sum route.

**R1-Q32 — C.** For `2x19` the signed alternating difference is `(2+1)−(x+9)=−x−6`. Its value can be −11 when `x=5`; `2519=11·229`. A: 7 gives −13; B: 9 gives −15; C: 5 gives −11; D: 4 gives −10. A negative multiple of 11 is as valid as a positive one. Source: B §§2,5.3.

**R1-Q33 — B.** Since `72=2³·3²`, the required divisors contain precisely `2²` and may contain `3⁰,3¹,3²`: 4,12,36, summing to 52. A: 48 omits 4; B: 52 counts all three; C: 40 omits 12; D: 60 wrongly includes 8, which is divisible by 8. Source: B §§2,6–7; 2025 constrained-divisor-sum neutral route.

**R1-Q34 — C.** The remainder must lie between zero and one less than its divisor, and `59=9·6+5`. A: 6 cannot be a remainder modulo 6; B: `59 mod 8=3`; C: `(9,5)` is valid; D: `59 mod 10=9`, not 5. Source: B §4.

**R1-Q35 — B.** A nonzero base raised to the zeroth power is 1, and `(-7)^0+(-7)^1=1−7=−6≡4 (mod 10)`. A: 2 does not represent −6; B: 4 is its least nonnegative remainder; C: 6 is the absolute value of −6, not its remainder; D: 8 is not congruent to −6 modulo 10. Source: B §§2–3; A §4.

**R1-Q36 — D.** Multiples of 4 or 6 in [1,150]: `⌊150/4⌋+⌊150/6⌋−⌊150/12⌋=37+25−12=50`. Among these, multiples of 9 are counted by `⌊150/36⌋+⌊150/18⌋−⌊150/36⌋=8`; exclude them to obtain 42. A: 50 does not exclude the multiples of 9; B: 38 subtracts the shared count 12 instead; C: 46 excludes only the four multiples of 36; D: 42 correctly excludes all eight. Source: B §5.4; A §§2,5–6.

**R1-Q37 — B.** `91=7·13` and `121=11²` are odd composites. The only divisors to try for 97 beyond 1 are primes ≤√97: 2,3,5,7; none divides it. A: 97 is prime; B: both 91 and 121 are composite; C: 1 is neither prime nor composite; D: 97 is prime. Source: B §§6–7, closure.

**R1-Q38 — C.** `0` and `−√9=−3` are integers and hence rational; `0.(3)=1/3` is rational; only `√2` is real and irrational. A: 0 overlooks √2; B: 2 treats a rational as irrational; C: 1 counts exactly √2; D: 3 misclassifies two rationals. Source: B §§5.1,5.3,7, closure.

**R1-Q39 — A.** Since `12=3·4`, any multiple of 12 is divisible by 3 and 4; conversely 3 and 4 together imply 12 because they are coprime. A: always true; B: take n=6, which fails divisibility by 4; C: take n=6, which satisfies both conditions but fails 12; D: take n=6, which satisfies both conditions but fails 12. The redundant `2 | n` beside `6 | n` contributes no new factor of 2. Source: B §§2,7–8.

**R1-Q40 — C.** Its three prime exponents are 2,4,2, giving `(2+1)(4+1)(2+1)=45` divisors, including 1 and N. All exponents are even, so N is a square; equivalently its divisor count is odd. A: 27 would result from misreading the exponent 4 as 2, though the square classification would remain true; B: 36 miscounts an exponent and falsely calls N nonsquare; C: 45 and square are both correct; D: 30 miscounts divisors and wrongly calls N nonsquare. Each wrong pair is itself arithmetically possible for some other integer, rather than being eliminated by the odd-divisor-count theorem alone. Source: B §§2,6–7.

**R1-Q41 — D.** For two positive integers, HCF×LCM=product, so LCM=`270/3=90`; the example (6,45) has HCF 3 and LCM 90 and satisfies the parity condition. A: 45 is an odd LCM and cannot contain the even integer; B: 135 is likewise odd; C: 60 is even but violates the product identity; D: 90 satisfies the identity and parity. This product law does not extend unchanged to three integers. Source: B §§2,4; A §5.

**R1-Q42 — C.** A shared remainder forces `d` to divide each difference, 60 and 120; hence d must be a divisor of 60. There are `(2+1)(1+1)(1+1)=12` positive divisors of `60=2²·3·5`. The remainder vanishes precisely if d also divides 95; among these twelve, only 1 and 5 do, leaving ten eligible divisors. A: 8 excludes two additional valid divisors; B: 9 excludes one additional valid divisor; C: 10 counts them all; D: 11 forgets that 5 gives exact division. Source: B §§2,4,6–7.

**R1-Q43 — A.** For (4,9,25), pairwise coprimality gives HCF1, LCM900 and product900. For (4,6,15), HCF1, LCM60, but product360. A: exactly the first works; B: the second fails; C: the second fails; D: the first works. Three-number product equality cannot be presumed from the two-number identity. Source: B §§2,4; A §5.

**R1-Q44 — B.** Candidates from `n+1≡0 (mod 5)` are n=4,9,14,19,…; only n=19 first makes n+2=21 divisible by 7. A: n=14 gives n+2=16; B: n=19 passes both; C: n=24 gives n+2=26; D: n=29 gives n+2=31. Source: B §4; 2025 simultaneous-remainder neutral route.

**R1-Q45 — D.** Powers of 3 have units 3,9,7,1, so `(-3)^15≡−7≡3 (mod 10)`; `2^13` ends in 2, giving the bracket's remainder 3. Their product ends in `3·3=9`. A: 1 drops the negative sign of the first factor, multiplying 7 by 3; B: 3 omits the second factor; C: 7 drops the negative sign *and* omits the second factor; D: 9 combines both signed residues. Source: B §§2–3; A §§2,4.

**R1-Q46 — D.** The last digit contributes zero; each of the other five digits is at most 9, so their sum cannot exceed 45. `999990` attains 45, is six-digit and is 9-divisible. A: 36 is attainable but not maximal; B: 40 is not divisible by 9 and not maximal; C: 44 is neither 9-divisible nor maximal; D: 45 is the proven attainable maximum. Source: B §§2,5.2; 2025 digit-bound neutral route.

**R1-Q47 — B.** If original digits are a,b, original minus reverse is `9(a−b)=27`, so a−b=3. Both digits must be nonzero for both numerals to be two-digit: the least b is 1, giving a=4 and original 41. A: 30 would reverse to 03, which is not two-digit; B: 41 reverses to 14, a difference of 27; C: 52 works but is larger; D: 63 also works but is larger. Source: B §5.2; historical reversal boundary route.

**R1-Q48 — C.** With a leading zero excluded, the possible three-digit numbers are 205,250,502,520, with sum `455+1022=1477`. A: 1400 removes the 77 contributed by leading-zero strings from the correct sum, rather than from the sum of all six digit permutations (1554); B: 1457 undercounts by 20; C: 1477 counts each permissible number once; D: 1554 wrongly includes 025 and 052 as three-digit numbers (their values add 77). Source: B §5.2; historical digit-arrangement route.

**R1-Q49 — B.** Put `x=0.272727…`. Then `100x−x=27`, so `x=27/99` and `x/(1+x)=(27/99)/(126/99)=27/126=3/14`. A: 27/127 treats the recurring block as the terminating decimal 27/100, producing `(27/100)/(127/100)`; B: 27/126 is exact; C: 27/99 is x alone, omitting the `1+x` denominator; D: 27/72 would follow from substituting `1−x` for `1+x`. All four are positive fractions and B is unique after reduction (A≈0.2126, B≈0.2143, C≈0.2727, D=0.375). Source: B §5.1.

**R1-Q50 — B.** For real x>3, squaring positive numbers preserves order, so x²>9. A: x=−3 is a counterexample; B: always valid; C: x=−4 squares above 9 without exceeding 3; D: x=3 squares to 9 but is not negative. Source: B §5.3, closure.

**R1-Q51 — A.** Although gcd(4,14)>1, the successive residues 4,2,8,4,… repeat from exponent 1 with period 3. Since `101≡2 (mod 3)`, the answer is the second residue, 2. A: 2 matches the exponent's cycle position; B: 4 is the first; C: 6 never appears; D: 8 is the third. Coprimality is sufficient, not necessary, for immediate periodicity. Source: A §§1–5.

**R1-Q52 — B.** The even two-digit numbers with a tens-place 1 are 10,12,14,16,18: five occurrences; none can have a units-place 1. The final number 100 contributes one more occurrence, giving six. A: 5 omits 100; B: 6 counts all six; C: 7 counts one nonexistent odd units-place case; D: 8 overcounts two. Source: B §5.2; historical digit-frequency route.

**R1-Q53 — D.** Divisibility by `24=3·2³` first occurs when `n−1≥3`; n=4 gives term24. A: n=3 gives12; B: n=6 gives96 but is not least; C: n=5 gives48 but is not least; D: n=4 gives24. Source: B §§2,6,10; ratio and divisibility method.

**R1-Q54 — C.** For indices 1–4 the terms are −1,4,−9,16 and their sum is 10. A: −10 reverses all four signs; B: 6 results from treating the fourth square as 12 rather than 16; C: 10 is exact; D: 20 adds only the positive terms 4 and 16, omitting the two negative terms. Source: B §§7,10; alternating-index number-property route.

**R1-Q55 — A.** Let `b_n=a_n+1`; then `b_1=3` and `b_(n+1)=2b_n`, so `b_n=3·2^(n−1)` always has factor 3. Since the first b equals 3, a universal divisor cannot exceed 3. A: 3 is universal and greatest; B: 2 fails at n=1; C: 1 works but is not greatest; D: 6 fails at n=1. Source: B §§6,10; recurrence-to-divisibility route.

**R1-Q56 — B.** Multiplying by 6ab gives `(a−6)(b−6)=36`. Both shifted factors must be positive (a,b>6), and `36=2²·3²` has `(2+1)(2+1)=9` positive divisors. Each choice for the first factor fixes the second, giving nine ordered pairs. A: 8 omits a divisor pair; B: 9 is exact; C: 10 double-counts the symmetric middle pair; D: 11 includes invalid nonpositive factors. Source: B §6 and its 2025 unit-fraction solution-count neutral demand route.

**R1-Q57 — C.** The original page sum is `100·101/2=5050`, so the four missing pages total 210. If the smaller odd page is p, the leaves are `(p,p+1)` and `(p+10,p+11)`, whose sum is `4p+22`; hence `p=(210−22)/4=47`. The leaves `(47,48)` and `(57,58)` are physically valid and total 210. A: 45 removes 202, leaving 4848; B: 49 removes 218, leaving 4832; C: 47 leaves exactly 4840; D: 43 removes 194, leaving 4856. Source: B §5.2 and historical page-sum torn-leaf neutral route.

**R1-Q58 — B.** The strict inequality `90<12k<210` gives integer quotients k=8..17. The odd quotients are 9,11,13,15,17, five values. A: 4 omits one valid odd quotient; B: 5 counts all of them; C: 6 includes one even quotient; D: 7 includes two even quotients. Source: B §5.4 and 2025 strict-interior multiples neutral route.

**R1-Q59 — C.** For any prime, cubing multiplies each factor exponent by 3; thus the HCF and LCM of cubes are the cubes of the original HCF and LCM. Their ratio is `(90/6)³=(3·5)³=3³·5³=3375`. A: 1125=`3²·5³` omits one factor of 3; B: 675=`3³·5²` omits one factor of 5; C: 3375 has all three factors of each prime; D: 10125=`3⁴·5³` adds one factor of 3. Source: B §§2,4 and its 2026 HCF–LCM cube-relation neutral route.

**R1-Q60 — D.** For n=1..10 the values are 2,5,10,17,26,37,50,65,82,101. Exactly 2,5,17,37,101 are prime; 101 has no divisor among primes ≤√101 (2,3,5,7). A: 2 omits three primes; B: 3 omits two; C: 4 omits one; D: 5 is exact. Source: B §§6–7 and 2025 prime-expression count neutral route.

**R1-Q61 — B.** `N=2⁴·3²` has `(4+1)(2+1)=15` positive divisors. A: `2³·3³` has `4·4=16`; B: `5⁴·7²` has `5·3=15` despite changed primes; C: `2⁵·3²` has `6·3=18`; D: `2²·3²·5` has `3·3·2=18`. Source: B §§2,6 and 2025 factor-count invariance neutral route.

**R1-Q62 — B.** For positive exponents, powers of 5 always end in 5 and powers of 6 always end in 6. As n≥1, both exponents shown are positive, so their sum always ends in `5+6=11`, or 1. A: 0 mistakenly treats the sum as a product; B: 1 is invariant; C: 5 omits the second power; D: 6 omits the first. Source: B §§2–3,7; single-position unit-digit cycles.

**R1-Q63 — D.** If the digits are a,b, the number and reversal sum to `(10a+b)+(10b+a)=11(a+b)=154`. Hence a+b=14, attainable with nonzero digits (e.g. 59 and 95). A: 11 would make total121; B: 12 gives132; C: 13 gives143; D: 14 gives154. Source: B §5.2; reversal-sum divisibility method.

**R1-Q64 — C.** The one- and two-digit integers contribute `9+90·2=189` digits. Digit 400 is therefore the 211th digit of the three-digit integers. Since `210=70·3`, the next digit belongs to the 71st three-digit integer, `100+70=170` (its first digit). A: 169 ends at position 399; B: 171 starts at position 403; C: 170 spans positions 400–402; D: 172 begins at 406. Source: B §5.2; 2025 concatenated-sequence-digit neutral route (original stem).

**R1-Q65 — D.** The residues of `2^n` modulo 40 begin `2,4,8,16,32,24,8,...`: the four-term cycle `8,16,32,24` starts at exponent 3, not exponent 1. Because `2026−3=2023≡3 (mod 4)`, select the fourth term of that eventual cycle: 24. Independently, `2^2026` is divisible by 8 and congruent to `2^2026≡4 (mod 5)` (since 2026≡2 mod 4); of the residues 0,8,16,24,32 divisible by 8, only 24 is congruent to 4 mod 5. A: 4 wrongly applies exponent 2's pre-cycle residue; B: 8 uses the cycle's first term; C: 16 uses its second term; D: 24 respects the cycle offset. Source: A §§1–6,8; noncoprime eventual-cycle offset, original application.
