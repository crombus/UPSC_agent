# CSAT 05 — Revision 2: worked answers (original items)

Every key is verified by computation (see `AUDIT.md`). Time targets assume the 72-second budget per item.

**R2-Q01 — B.** Let the number be 10t + u. Then 10t + u = 4(t + u) gives u = 2t, and reversal gives 9(u - t) = 36, so u - t = 4. Thus t = 4, u = 8: 48.

- A. 24 satisfies the first condition (4 x 6 = 24) but reversal gives 42, an increase of 18, not 36.
- B. (key) 48
- C. 36 satisfies the first condition (4 x 9 = 36) but reversal gives 63, an increase of 27.
- D. 84 is the reversal of 48, which is smaller than the original when reversed; the increase condition fails.

- Trap: Two linear relations (from the 4-times rule and from the reversal increase) must hold together.
- Shortcut and time target: Form both equations, substitute u = 2t, then check against the reversal increase. Target 95 s.

**R2-Q02 — B.** Digits t and u with t - u = 2 and tu = 15 give t = 5 and u = 3. The number is 53.

- A. 35 has the same digit product, but its tens digit is smaller, so the difference condition fails.
- B. (key) 53
- C. 75 has tens digit exceeding units by 2 but the product is 35, not 15.
- D. 97 fails both conditions: the product is 63.

- Trap: Two conditions on the digits (difference and product) should be checked together.
- Shortcut and time target: Write t and u from the product list (3 x 5 = 15), then test the difference. Target 80 s.

**R2-Q03 — C.** Each relation alone allows several ratios; together x = 7 and y = 3 give the unique ratio 7/3. I alone: not unique (9 values, e.g. 1, 1/4, 1/9, 2/3); II alone: not unique (16 values, e.g. 11/7, 13/9, 15/11, 17/13); together: unique value 7/3.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: A ratio is determined only when both unknowns are determined.
- Shortcut and time target: Two relations are needed for two unknowns; the ratio is then a single fraction. Target 85 s.

**R2-Q04 — C.** Boys = 36 and girls = 24 at first. After 6 boys leave: boys = 30 and girls = 24. Girls to boys = 24:30 = 4:5.

- A. 5:4 inverts the boys-to-girls order, reporting boys to girls after the change (30 to 24).
- B. 2:3 repeats the original girls to boys ratio, ignoring the departure.
- C. (key) 4:5
- D. 6:5 divides 30 to 24 wrongly as 6 to 5, using 25 for the girls.

- Trap: Ratios are order-sensitive: the question asks girls to boys, the inverse of the starting ratio.
- Shortcut and time target: Compute the counts before and after the change, then write the requested order and reduce. Target 75 s.

**R2-Q05 — C.** Subtracting y <= -1 (that is, -y >= 1) from x >= 2 gives x - y >= 3, which must hold.

- A. x + y >= 1 fails for x = 2 and y = -5, which gives -3.
- B. xy >= -2 fails for x = 2 and y = -5, which gives -10.
- C. (key) x - y >= 3
- D. x - y <= 1 fails for x = 2 and y = -1, which gives 3.

- Trap: Sign reasoning on x - y: -y adds at least 1 because y is bounded above by -1.
- Shortcut and time target: Add the bound on x to the bound on -y; check each false option with one counterexample. Target 85 s.

**R2-Q06 — D.** |A| = 15, |B| = 10, |A and B| = |multiples of 12| = 5. So |A or B| = 15 + 10 - 5 = 20.

- A. 25 adds the sizes of A and B (15 + 10) without subtracting the 5 common multiples of 12.
- B. 15 counts only the multiples of 4 in A, ignoring B.
- C. 5 counts only the common multiples of 12, which is the intersection.
- D. (key) 20

- Trap: A common multiple of 4 and 6 is a multiple of 12; the overlap must be removed once.
- Shortcut and time target: Count each set, count the common multiples of the LCM (12), then subtract the overlap. Target 80 s.

**R2-Q07 — B.** Dividing by x > 0 gives x < 10, so the positive integers 1 to 9 work: nine values.

- A. 10 counts 0 through 9, but 0 is not a positive integer.
- B. (key) 9
- C. 8 omits x = 1, which satisfies 1 < 10.
- D. 4 derives x < 5 by halving the bound, which gives the wrong endpoint.

- Trap: Divide by a positive quantity only; the division keeps the direction and gives the bound.
- Shortcut and time target: Divide by x (positive) and read the bound, then count from 1. Target 70 s.

**R2-Q08 — D.** The numbers are (21 + 5)/2 = 13 and (21 - 5)/2 = 8. Their product is 104.

- A. 105 is the sum times the difference (21 x 5), which has no meaning here.
- B. 98 is the pair 14 and 7: sum 21 but difference 7.
- C. 110 is the pair 11 and 10: sum 21 but difference 1.
- D. (key) 104

- Trap: The half-sum plus or minus half-difference rule gives the pair; any other split with the same sum fails the difference.
- Shortcut and time target: Use (S + D)/2 and (S - D)/2 and multiply. Target 70 s.

**R2-Q09 — A.** The sum statement allows (1,3), (2,2) and (3,1), all with products at most 4, so the answer is no. The equal-values statement leaves products from 1 to 100. I alone: unique value no; II alone: not unique (2 values, e.g. no, yes); together: unique value no.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A yes-or-no question is settled as soon as every admissible pair gives the same answer.
- Shortcut and time target: For a yes-or-no product question, check the largest possible product in each branch. Target 85 s.

**R2-Q10 — D.** Each statement alone leaves several values; together they leave 24 and 48. I alone: not unique (8 values, e.g. 12, 18, 24, 30); II alone: not unique (6 values, e.g. 16, 24, 32, 40); together: not unique (2 values, e.g. 24, 48).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: A common multiple of two numbers is spaced by their lcm; check the next one in range.
- Shortcut and time target: Find the common multiples of 6 and 8 in range; more than one is a failure to fix the value. Target 75 s.

**R2-Q11 — C.** The square statement alone allows x less than y (for example x = -5, y = 1). The positive-sum statement alone says nothing about squares. Together, x + y > 0 and x squared greater than y squared force x > y. I alone: not unique (2 values, e.g. no, yes); II alone: not unique (2 values, e.g. no, yes); together: unique value yes.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Neither statement alone settles the order; their product (x-y)(x+y) does.
- Shortcut and time target: Factor the difference of squares: (x - y)(x + y) > 0 with x + y > 0 gives x - y > 0. Target 95 s.

**R2-Q12 — C.** The second statement leaves 8, 16 and 24; the first keeps only 24 from that list. I alone: not unique (8 values, e.g. 12, 18, 24, 30); II alone: not unique (3 values, e.g. 16, 24, 8); together: unique value 24.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement alone leaves several values; the intersection fixes one.
- Shortcut and time target: Use the set with fewer members as the filter. Target 80 s.

**R2-Q13 — D.** On x >= 4 the sum is 2x - 2 = 8, so x = 5. On x <= -2 it is 2 - 2x = 8, so x = -3. Between -2 and 4 the sum is always 6. So two integers work.

- A. 1 finds only x = 5 on the branch x >= 4 and forgets the branch x <= -2, which gives x = -3.
- B. 3 adds x = 4 from the middle region, where the sum is 6 and not 8.
- C. 4 counts the endpoints -2 and 4 along with 5 and -3; the middle region sums to 6 and fails.
- D. (key) 2

- Trap: Three regions give three linear forms; only the outer two can reach 8.
- Shortcut and time target: Split at -2 and 4 and solve each branch; the middle branch is constant and is discarded at once. Target 100 s.

**R2-Q14 — A.** The second statement alone gives m = 3; the first allows many values. I alone: not unique (40 values, e.g. -1, -10, -11, -12); II alone: unique value 3; together: unique value 3.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A statement that is always true of a nonzero integer cannot settle the value.
- Shortcut and time target: A linear statement fixes a value; a square inequality rarely does. Target 60 s.

**R2-Q15 — D.** The perfect squares and perfect cubes both include 1 and 64, so the pair leaves two values. I alone: not unique (10 values, e.g. 1, 100, 16, 25); II alone: not unique (4 values, e.g. 1, 27, 64, 8); together: not unique (2 values, e.g. 1, 64).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: A common element is not the same as a unique element; the overlap here has two members.
- Shortcut and time target: Check the overlap of the two sets for every value they share. Target 75 s.

**R2-Q16 — C.** Statement II leaves 5, 10 and 15; with the multiple-of-3 condition only 15 remains. I alone: not unique (33 values, e.g. 12, 15, 18, 21); II alone: not unique (3 values, e.g. 10, 15, 5); together: unique value 15.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: The stated range excludes 0; without the lower bound, 0 would also satisfy both statements.
- Shortcut and time target: Use the narrower statement first, then check it against the other. Target 80 s.

**R2-Q17 — D.** For x > 1: 1/x < 1 < sqrt(x) < x < x^2. The least is 1/x.

- A. x is not the least: x is larger than 1, while 1/x is less than 1.
- B. x^2 is greater than x when x > 1, so it is not the least.
- C. sqrt(x) is greater than 1 but smaller than x when x > 1, so it is not the least.
- D. (key) 1/x

- Trap: The reciprocal of a number above 1 lies below 1, the opposite of the intuition from larger powers.
- Shortcut and time target: Test x = 4: 0.25, 2, 4, 16; the reciprocal is the least. Target 70 s.

**R2-Q18 — B.** The total is 5 x 20 = 100, so the fifth number is 100 - 76 = 24.

- A. 19 is the mean of the four given numbers, not the missing fifth.
- B. (key) 24
- C. 16 subtracts 4 from 20 instead of using the total of 100.
- D. 20 repeats the mean; the fifth number is the total minus the four.

- Trap: A mean problem is a sum problem first; the mean itself is not the answer.
- Shortcut and time target: Multiply the mean by the count to get the total, then subtract the known four. Target 60 s.

**R2-Q19 — B.** x^2 < x gives x(x - 1) < 0, so 0 < x < 1 (x is nonzero).

- A. x > 1 is contradicted by x = 2: 4 < 2 is false.
- B. (key) 0 < x < 1
- C. x < 0 is contradicted by x = -1: 1 < -1 is false.
- D. x^2 > 1 is contradicted by x = 0.5: 0.25 is not greater than 1.

- Trap: Factor the inequality: the product of x and x - 1 is negative only between the roots.
- Shortcut and time target: Factor as x(x - 1) < 0 and read the interval between 0 and 1. Target 75 s.

**R2-Q20 — C.** The product alone allows several pairs; the difference alone allows several pairs; together a = 4 and b = 3. I alone: not unique (6 values, e.g. 1, 12, 2, 3); II alone: not unique (19 values, e.g. 10, 11, 12, 13); together: unique value 4.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each relation alone is consistent with several pairs; only the joint solution is unique.
- Shortcut and time target: A product and a difference together form a quadratic-free system; test pairs against both. Target 85 s.

**R2-Q21 — A.** A square divisible by 81 needs 3 to power 2 in n, so 9 divides n; the multiple-of-12 statement does not force 9. I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Divisibility of a square by 81 is a power condition; it is not the same as divisibility by 81 itself.
- Shortcut and time target: A power of a prime in a square halves the exponent in the root. Target 90 s.

**R2-Q22 — B.** 2^(x+2) - 2^x = 2^x(4 - 1) = 3 x 2^x. So 2^x = 32 and x = 5.

- A. 4 gives 2^6 - 2^4 = 64 - 16 = 48, which is half of 96.
- B. (key) 5
- C. 6 gives 2^8 - 2^6 = 192, which is double 96.
- D. 7 gives 2^9 - 2^7 = 384, which is four times 96.

- Trap: Factor out the smallest power before solving; a power shift is not a multiplicative factor on the whole sum.
- Shortcut and time target: Write 2^(x+2) as 4 x 2^x, factor out 2^x, then read the exponent. Target 80 s.

**R2-Q23 — C.** Write y = (12 - x)/2, so xy = x(12 - x)/2, maximised at x = 6, giving y = 3 and xy = 18. Check: 6 + 6 = 12.

- A. 36 solves as if x + y = 12 (the coefficient 2 is dropped), which gives x = y = 6 and product 36; that pair does not satisfy x + 2y = 12.
- B. 24 needs x = 12 and y = 0, which is not positive, so it is not attainable.
- C. (key) 18
- D. 16 (x = 4, y = 4) lies on the line but is not the maximum.

- Trap: The coefficient 2 on y must be carried into the substitution; the equal-parts rule applies to x and 2y, not to x and y.
- Shortcut and time target: Put the two terms x and 2y in equal parts: x = 6 and 2y = 6, then multiply by the remaining factor. Target 100 s.

**R2-Q24 — B.** (x + 1/x)^3 = x^3 + 1/x^3 + 3(x + 1/x), so x^3 + 1/x^3 = 27 - 9 = 18.

- A. 27 is the cube of the sum alone; the cubic identity subtracts 3 times the sum.
- B. (key) 18
- C. 24 subtracts 3 instead of 3 times the sum (9); the coefficient 3 was applied to the constant only.
- D. 9 keeps only 3(x + 1/x) and drops the cube term.

- Trap: The cube of a sum carries a middle term 3(sum); missing it is the common slip.
- Shortcut and time target: Use (s)^3 - 3s, where s is the given sum, and check with x = (3 + sqrt5)/2. Target 85 s.

**R2-Q25 — D.** Bina = b, Ankit = b + 3, so 2b + 3 = 35 and b = 16. In four years Bina is 20.

- A. 16 is Bina's present age, not her age in four years.
- B. 19 is Ankit's present age, not Bina's.
- C. 23 is Ankit's age in four years.
- D. (key) 20

- Trap: Relate both persons through the same unknown first; the future age is added after the present value is found.
- Shortcut and time target: Solve for the present age, then add the number of years. Target 75 s.

**R2-Q26 — A.** 7p + 4q = 100 needs p to be a multiple of 4 (since 7p = 100 - 4q). Of the feasible pairs p = 4, q = 18 gives the most items: 22.

- A. (key) 22
- B. 19 is the total for 8 pens and 11 pencils: feasible but not the greatest.
- C. 16 is the total for 12 pens and 4 pencils, which is feasible but fewer items than 22.
- D. 25 needs 3 pens' worth of money to vanish: 7p + 4q = 100 with p + q = 25 forces p = 0, which breaks the at-least-one rule.

- Trap: Maximising a count under a cost equality favours cheap items; the cheap item pencils get the larger count.
- Shortcut and time target: Solve the congruence 7p = 100 (mod 4) first, then compare the few feasible pairs. Target 110 s.

**R2-Q27 — B.** The nearest integers to 25/2 are 12 and 13, which both exceed 3 and sum to 25; 12 x 13 = 156.

- A. 150 is 10 times 15, a valid pair that is not the maximum: the product falls as the pair moves away from 12.5.
- B. (key) 156
- C. 144 is 12 times 12, but the sum is 24, not 25.
- D. 168 is 12 times 14, but the sum is 26, not 25.

- Trap: The lower bounds of 3 do not bind here; the integer pair nearest the midpoint still gives the maximum.
- Shortcut and time target: Choose the consecutive integers nearest half the sum, then check the lower bounds. Target 80 s.

**R2-Q28 — D.** sqrt(2) is about 1.414 and sqrt(3) about 1.732; 3/2 = 1.5 is rational and lies between them.

- A. 7/5 = 1.4 is below sqrt(2), about 1.414, so it lies outside the interval.
- B. 9/5 = 1.8 is above sqrt(3), about 1.732.
- C. sqrt(5) is about 2.24, which is above sqrt(3), and it is irrational.
- D. (key) 3/2

- Trap: Square both ends to test candidates: 2 < (3/2)^2 = 2.25 < 3.
- Shortcut and time target: Check the squares: 2 < r^2 < 3 for the rational candidate. Target 70 s.

**R2-Q29 — A.** The cube statement alone gives 2; the square statement allows 2 and -2, so only the first suffices. I alone: unique value 2; II alone: not unique (2 values, e.g. -2, 2); together: unique value 2.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A square of 4 keeps two roots; a cube of 8 keeps one.
- Shortcut and time target: Check whether the statement is one-valued before testing the other. Target 70 s.

**R2-Q30 — A.** Raise each option to the 30th power: 3^10 = 59049, 6^6 = 46656, 2^15 = 32768 and 5^5 = 3125. Since 59049 is largest, 3^(1/3) is the greatest.

- A. (key) 3^(1/3)
- B. 4^(1/4) = sqrt(2), about 1.414, which is smaller than 3^(1/3), about 1.442.
- C. 5^(1/6) is about 1.307; a smaller base with a larger root index does not offset the lower base.
- D. 6^(1/5) is about 1.431, just below 3^(1/3). Raise both to the 15th power: 6^3 = 216 against 3^5 = 243.

- Trap: A common exponent (here 30) puts all roots on one integer scale; check it exactly.
- Shortcut and time target: Raise every option to the common power 30, then compare integers. Target 110 s.

**R2-Q31 — B.** Substitute y = x - 2: 2x - 3x + 6 = 4, so -x = -2 and x = 2. Check: y = 0, and 4 - 0 = 4.

- A. 0 is the value of y at x = 2, not of x.
- B. (key) 2
- C. -2 is the value of y in the original relation at x = 0; it does not satisfy both equations.
- D. 6 comes from taking 2x - 3(x - 2) = 4 as 2x - 3x = 4 (the bracket dropped).

- Trap: Keep the bracket when substituting; a dropped constant is the typical error.
- Shortcut and time target: Substitute the relation into the first equation and keep the bracket. Target 70 s.

**R2-Q32 — C.** Rationalise each difference: sqrt(n+1) - sqrt(n) = 1/(sqrt(n+1) + sqrt(n)). The denominator for the first pair (sqrt98 + sqrt97) is smaller, so its difference is larger.

- A. sqrt(99) - sqrt(98) is smaller: rationalising gives 1/(sqrt99 + sqrt98), which is less than 1/(sqrt98 + sqrt97).
- B. The two differences are not equal; the gap between consecutive square roots shrinks as the numbers grow.
- C. (key) sqrt(98) - sqrt(97)
- D. The sum is about 19.7 while the difference is about 0.05; the sum is not a comparison of the same kind.

- Trap: Rationalising converts a difference of close radicals into a reciprocal that is easy to compare.
- Shortcut and time target: Rationalise both differences: the one with the smaller denominator is larger. Target 85 s.

**R2-Q33 — D.** The first statement leaves squares 0, 1, 4 and 9; the second leaves primes. Together they leave 2 and 3, with squares 4 and 9. I alone: not unique (4 values, e.g. 0, 1, 4, 9); II alone: not unique (8 values, e.g. 121, 169, 25, 289); together: not unique (2 values, e.g. 4, 9).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: Two possible values with different squares break uniqueness even when both statements are strong.
- Shortcut and time target: Overlap a bounded set with a prime set; a common prime is not a single prime. Target 80 s.

**R2-Q34 — B.** Each statement alone gives x = 6, so either one suffices. I alone: unique value 6; II alone: unique value 6; together: unique value 6.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Two statements can be sufficient alone and still look different; compare the values.
- Shortcut and time target: Compare the two single values once the sign is fixed. Target 65 s.

**R2-Q35 — C.** The product statement leaves 0 and -1; the non-negativity statement removes -1, so 0 is the unique survivor. I alone: not unique (2 values, e.g. -1, 0); II alone: not unique (21 values, e.g. 0, 1, 10, 11); together: unique value 0.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: A product of zero hides the answer -1 until the sign condition removes it.
- Shortcut and time target: Solve the product first, then apply the sign condition. Target 80 s.

**R2-Q36 — D.** The square statement allows -3 to -10 and 3 to 10; the negative statement keeps -3 to -10. Several values remain. I alone: not unique (16 values, e.g. -10, -3, -4, -5); II alone: not unique (10 values, e.g. -1, -10, -2, -3); together: not unique (8 values, e.g. -10, -3, -4, -5).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: Two conditions can narrow a set without fixing it.
- Shortcut and time target: A square bound and a sign bound together give an interval of negatives, not a point. Target 65 s.

**R2-Q37 — A.** The corner products are -15, -20, -6 and -8. The smallest is a = -5 with b = 4, but both those ends are excluded, so -20 is the infimum and is not attained.

- A. (key) -20
- B. -15 is a = -5 times b = 3; it is not the lowest corner, because -20 is smaller and needs the same excluded end a = -5.
- C. -8 is a = -2 times b = 4: an upper corner of a, not the lowest product.
- D. -6 is a = -2 times b = 3: a corner that is larger than -20.

- Trap: Infimum and minimum differ when the extreme endpoint is excluded; read the open or closed status before naming the bound.
- Shortcut and time target: Compare the four corners, then decide whether the extreme corner is attained. Target 100 s.

**R2-Q38 — A.** Over the rectangle, x/y is smallest as x tends to 0 and largest as x tends to 1 with y tends to 2; both extremes are approached but not reached, so the range is (0, 1/2).

- A. (key) (0, 1/2)
- B. (-1, 1/2) uses a negative corner, but x is positive in the stem; it does not describe the rectangle.
- C. (0, 1/4) takes 1/4 as the maximum and ignores the corner x near 1 with y near 2, which gives values near 1/2.
- D. [0, 1/2] closes both ends, but x = 0 and y = 2 are excluded, so neither extreme is attained.

- Trap: With positive intervals, the quotient's extremes come from opposite corners, and the open status of each endpoint decides the bracket.
- Shortcut and time target: Tabulate the corners and keep the open status of the endpoint responsible for each extreme. Target 100 s.

**R2-Q39 — B.** An odd power is one-to-one on the reals: x^3 = -343 gives x = -7 alone.

- A. x^2 = 49 has two real solutions, 7 and -7.
- B. (key) x^3 = -343
- C. x^2 = -16 has no real solution, since a square of a real number is not negative.
- D. The pair x^2 = 49 and x^2 = 16 requires one number with two different squares, so no real solution exists.

- Trap: Count real roots by power: an even power doubles the roots, an odd power keeps exactly one.
- Shortcut and time target: Decide the parity of the power first; odd powers of real numbers have a single real root. Target 75 s.

**R2-Q40 — C.** Need 3y even, so y in {0, 2, 4}, giving x = 6, 3, 0: the pairs (6,0), (3,2), (0,4). That is 3.

- A. 2 misses (6, 0) on the grounds that y = 0 is trivial; y = 0 is allowed here.
- B. 4 counts pairs whose 2x is not an integer multiple of 2; 2x = 12 - 3y needs 3y even, so y must be even.
- C. (key) 3
- D. 5 counts every y from 0 to 4 without checking that x is an integer.

- Trap: A parity constraint on y (from the coefficient 2 on x) filters the possible values before counting.
- Shortcut and time target: Find the allowed y values by parity, then compute x for each. Target 90 s.

**R2-Q41 — D.** The first statement is always true in this range, so it adds nothing; the second leaves 4, 10 and 16. I alone: not unique (21 values, e.g. 0, 1, 10, 11); II alone: not unique (3 values, e.g. 10, 16, 4); together: not unique (3 values, e.g. 10, 16, 4).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: A statement that holds for every value in the range is not a filter.
- Shortcut and time target: Test whether a statement is true for the whole range before using it as a filter. Target 60 s.

**R2-Q42 — A.** Both factors change sign at their roots (3 and -2). Positive quotient needs both factors of the same sign: x > 3 or x < -2.

- A. (key) x < -2 or x > 3
- B. Taking the two factors with the same sign only in the middle region reverses the sign of x + 2; the sign pattern is the opposite.
- C. Keeps only the positive branch of the sign chart and forgets that both numerator and denominator can be negative.
- D. A union of two conditions that each hold for some values in the interval; x = 0 gives -3/2, which is negative, so it fails.

- Trap: Cross-multiplying needs the sign of (x + 2) fixed first; without that the direction of the inequality is unknown.
- Shortcut and time target: Use a sign chart with the two critical points -2 and 3, then test one value in each interval. Target 90 s.

**R2-Q43 — A.** Statement II settles the question (x is positive, so not negative). Statement I allows x to be negative or positive. I alone: not unique (2 values, e.g. no, yes); II alone: unique value no; together: unique value no.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Only Statement II fixes the sign; a positive square says nothing about it.
- Shortcut and time target: Check the sign with the statement that uses an order relation, not the one that uses a square. Target 70 s.

**R2-Q44 — C.** Statement I leaves 7 and -7; the lower bound removes -7 and leaves 7 alone. I alone: not unique (2 values, e.g. -7, 7); II alone: not unique (45 values, e.g. -1, -2, -3, -4); together: unique value 7.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: A bound that removes one root of a square is the usual way a pair becomes decisive.
- Shortcut and time target: Apply each bound to the roots of the square before testing uniqueness. Target 75 s.

**R2-Q45 — A.** Points are 3 per win and 0 per loss, so 21 points means 7 wins alone; the second statement leaves 6 to 10. I alone: unique value 7; II alone: not unique (5 values, e.g. 10, 6, 7, 8); together: unique value 7.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A statement about the total points is a linear constraint; the second is an inequality that leaves several values.
- Shortcut and time target: Convert the points statement into wins before testing the second statement. Target 70 s.

**R2-Q46 — D.** Each statement leaves several positive integers; together they leave 1, 2 and 3. I alone: not unique (5 values, e.g. 1, 2, 3, 4); II alone: not unique (3 values, e.g. 1, 2, 3); together: not unique (3 values, e.g. 1, 2, 3).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: Each statement alone is an upper bound; the intersection still contains three integers.
- Shortcut and time target: Both statements are upper bounds, so the pair's intersection is the smaller of the two sets. Target 75 s.

**R2-Q47 — B.** The coefficient determinant 1(-2) - 1(2) = -4 is nonzero, so the system has a single solution (x = 6, y = 2).

- A. The second equation is exactly twice the first, so the pair has infinitely many common solutions, not one.
- B. (key) x + 2y = 10 and x - 2y = 2
- C. The two left-hand sides are identical but the right-hand sides differ (5 and 6), so there is no common solution.
- D. The second equation has left side 2 times the first, but its right side 9 is not 14, so the system is inconsistent.

- Trap: Compare the ratio of coefficients with the ratio of constants: unequal coefficient ratios give a unique solution.
- Shortcut and time target: Compute the coefficient determinant of each pair; a nonzero value is sufficient for uniqueness. Target 85 s.

**R2-Q48 — A.** The four corners are -6, 3, -10 and 5. All endpoints are included, so the range is the closed interval from -10 to 5.

- A. (key) [-10, 5]
- B. [-6, 5] takes the lower corner 3 times -2 and the upper corner 5 times 1; it misses the corner 5 times -2 = -10.
- C. [-10, 3] takes the lowest corner correctly but drops the corner 5 times 1 = 5.
- D. [-6, 3] uses only the corners that involve x = 3, missing both x = 5 corners.

- Trap: A product range on a sign-changing rectangle takes all four corners; the endpoints here are included.
- Shortcut and time target: Tabulate the four corners and take their minimum and maximum. Target 90 s.

**R2-Q49 — D.** x^2 = 2x gives x(x - 2) = 0, so x = 0 or x = 2, and their sum is 2. The question alone fixes the sum; neither statement is needed.

- A. Wrong: Statement I (positive) alone would leave only x = 2, but the question is answered without it, so "exactly one suffices" misreads the item.
- B. Wrong: Statement II (integer) does not change the answer, and the question is already answered.
- C. Wrong: the pair is not needed; the sum 2 comes from the stem alone.
- D. (key) The question can be answered without any statement: the solutions are 0 and 2.

- Trap: Dividing both sides of x^2 = 2x by x. That loses the root x = 0 and gives a false "unique root" x = 2 with the wrong sum.
- Shortcut and time target: Factor the quadratic and add the distinct roots. Target 70 s.

**R2-Q50 — A.** Two-digit numbers with digit sum 11 are 29, 38, 47, 56, 65, 74, 83 and 92. Statement I (greater than 85) leaves 92 only. Statement II (even) leaves 38, 56, 74 and 92. The question alone leaves eight candidates.

- A. (key) Exactly one suffices: Statement I alone gives 92; Statement II alone does not.
- B. Wrong: Statement II alone leaves four even candidates, so it does not decide N.
- C. Wrong: Statement I alone already decides N, so the pair is not needed.
- D. Wrong: without a statement the question leaves eight candidates, so it is not self-sufficient.

- Trap: Assuming the digit-sum condition has one answer because 92 looks like the largest. Eight two-digit numbers satisfy it.
- Shortcut and time target: Consecutive numbers with digit sum 11 differ by 9 (29, 38, 47, ...). Target 70 s.

**R2-Q51 — B.** Statement I: t is positive and t^2 = 9, so t = 3. Statement II: t^3 = 27 has the single real root 3. Each statement alone fixes t.

- A. Wrong: Statement II alone also gives t = 3, so "exactly one" fails.
- B. (key) Each statement alone suffices.
- C. Wrong: each statement is decisive alone; the pair is not needed.
- D. Wrong: the question alone leaves t = 3 or t = -3, so it is not self-sufficient, and each statement decides t.

- Trap: Keeping t = -3 from t^2 = 9 without the positivity condition. The cube has a single real root, so Statement II avoids this issue.
- Shortcut and time target: An odd power keeps the sign of its base, so t^3 = 27 has one real solution. Target 70 s.

**R2-Q52 — D.** Statement I: p + r = 22 with p < q < r < 30. Statement II: q + r = 24. Together: r = 19 gives p = 3 and q = 5; r = 17 gives p = 5 and q = 7. Both are admissible, so q is 5 or 7.

- A. Wrong: Statement I alone leaves five possible values of q (5, 7, 11, 13, 17), so it is not decisive.
- B. Wrong: Statement II alone leaves q = 5, 7 or 11, so "each suffices" fails.
- C. Wrong: together they leave two values of q (5 and 7), so the pair is not decisive.
- D. (key) The question cannot be answered even using both together.

- Trap: Counting two equations as enough for three unknowns. Two integer equations in three prime unknowns can still have two solutions.
- Shortcut and time target: List the admissible r values from the second equation, then test p. Target 90 s.

**R2-Q53 — B.** Statement I: the multiples of 7 in the range 30 to 50 are 35, 42 and 49; "less than 36" leaves 35. Statement II: the whole numbers strictly between 34 and 37 are 35 and 36; only 35 is a multiple of 5. Each statement alone fixes the number at 35.

- A. Wrong: Statement II alone also fixes the number, so "exactly one" fails.
- B. (key) Each statement alone suffices; both give 35.
- C. Wrong: each statement suffices alone, so the pair is not needed.
- D. Wrong: both statements give 35, so the question is answered.

- Trap: Stopping at the multiples of 7 (35, 42, 49) and forgetting the upper bound. The bound "less than 36" is what removes 42 and 49.
- Shortcut and time target: List the multiples of 7 in the range and apply the bound at once. Target 70 s.

**R2-Q54 — C.** Statement I: x ◇ 2 = x^2 - 4 and 2 ◇ x = 4 - 2x, so x^2 + 2x - 8 = 0 and x = -4 or x = 2. Statement II: x^2 = 16 gives x = 4 or x = -4. Together, only x = -4 fits both.

- A. Wrong: Statement I alone leaves x = -4 or 2, so it is not decisive; Statement II alone leaves x = -4 or 4.
- B. Wrong: neither statement suffices alone.
- C. (key) Both together are sufficient: x = -4 satisfies both, and x = 2 and x = 4 each fail one.
- D. Wrong: the pair fixes x = -4.

- Trap: Swapping the roles in the operation, that is, writing 2 ◇ x as x^2 - 2·2. The second operand enters the formula as the subtracted term only.
- Shortcut and time target: Solve Statement I as a quadratic, then test its two roots in Statement II. Target 100 s.

**R2-Q55 — C.** Statement I: N is a multiple of 9, so N is one of 18, 27, 36, 45, 54, 63, 72, 81, 90 or 99. Statement II: the tens digit exceeds the units digit by 5, which gives 50, 61, 72, 83 and 94. Together only 72 fits, since 72 = 8 x 9 and 7 - 2 = 5.

- A. Wrong: Statement I alone leaves ten candidates, so it is not decisive.
- B. Wrong: Statement II alone leaves five candidates, so it is not decisive.
- C. (key) Both together are sufficient: 72 is the only common value.
- D. Wrong: the pair fixes N = 72.

- Trap: Reading "tens digit exceeds units digit by 5" as "digits add to 5". The difference condition is different from the digit sum.
- Shortcut and time target: Test the ten two-digit multiples of 9 against the difference 5; only 72 matches. Target 80 s.

**R2-Q56 — D.** n is a perfect square when n = 36k with k a perfect square. Statement I (divisible by 4) gives n = 4 (square) and n = 8 (not square). Statement II (divisible by 9) gives n = 9 (square) and n = 18 (not square). Together, n = 36 is a square but n = 72 is not, so the question is not decided.

- A. Wrong: neither statement alone decides the question.
- B. Wrong: neither statement alone decides the question, so "each suffices" fails.
- C. Wrong: the pair leaves both yes and no open (36 yes, 72 no).
- D. (key) The question cannot be answered even using both together.

- Trap: Assuming that divisibility by 4 and by 9 guarantees a square. Only the square part of the cofactor k matters, so 36 is a square but 72 is not.
- Shortcut and time target: Write n = 36k and check whether k is a square. Target 80 s.
