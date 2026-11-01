# CSAT 05 — Revision 1: worked answers (original items)

Every key is verified by computation (see `AUDIT.md`). Time targets assume the 72-second budget per item.

**R1-Q01 — D.** The net coefficient is 3/5 - 2/7 = 11/35, so (11/35)x = 22 and x = 70. Check: 42 - 20 = 22.

- A. 35 is half of the correct value and does not satisfy 3/5 - 2/7 = 22/35 times the number.
- B. 77 results from dividing 22 by 2/7 instead of by the net coefficient (3/5 - 2/7).
- C. 110 results from dividing 22 by 1/5, a fraction misread from the 3/5 term.
- D. (key) 70

- Trap: Combine the two fractions of the same number first; dividing by a single fraction is wrong.
- Shortcut and time target: Net coefficient = 3/5 - 2/7 = 11/35; then x = 22 x 35/11 = 70. Target 80 s.

**R1-Q02 — C.** n^2 < 30 gives -5 <= n <= 5 (since 5^2 = 25 < 30 and 6^2 = 36). With n > -4, the integers are -3 to 5, which is nine integers.

- A. 8 uses |n| < 5 instead of |n| <= 5, so 5 is dropped even though 5 squared is 25 < 30; the -4 cut is then applied.
- B. 10 keeps -4 by reading the second condition as n >= -4.
- C. (key) 9
- D. 11 ignores the second condition and counts -5 to 5.

- Trap: Only -4 and -5 are excluded by n > -4; the bounds of the square condition must be taken from the square root.
- Shortcut and time target: Find the integer range from the square root (|n| <= 5), then apply the strict lower bound. Target 80 s.

**R1-Q03 — C.** Let the box be b and the bag g. Then b = 2 + g/2 and g = b + 4. Substituting: g = 2 + g/2 + 4, so g = 12 and b = 8.

- A. 8 is the box's weight, not the bag's.
- B. 6 is half the bag's weight, which is the quantity the 2 kg offset was added to.
- C. (key) 12
- D. 16 reverses the difference: it treats the bag as 4 kg heavier than the box.

- Trap: The first clue links the box to the bag through a half, so the substitution must keep the half.
- Shortcut and time target: Substitute one equation into the other and solve for the bag directly. Target 85 s.

**R1-Q04 — D.** The square gives 3 and -3; the upper bound keeps both, so the pair does not fix x. I alone: not unique (2 values, e.g. -3, 3); II alone: not unique (60 values, e.g. -1, -10, -11, -12); together: not unique (2 values, e.g. -3, 3).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: The second statement leaves both roots; a bound must exclude one of them to help.
- Shortcut and time target: Write both roots of the square and test them against the bound. Target 60 s.

**R1-Q05 — C.** The second statement leaves 16, 17 and 18; the first leaves many multiples of 6; together only 18 survives. I alone: not unique (33 values, e.g. 102, 108, 114, 12); II alone: not unique (3 values, e.g. 16, 17, 18); together: unique value 18.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement is necessary but not enough alone; only the pair fixes n.
- Shortcut and time target: Compare the narrow set with the multiples-of-6 test. Target 75 s.

**R1-Q06 — B.** The integers are 4 and 5. Their squares add to 16 + 25 = 41, which equals (x+y)^2 - 2xy = 81 - 40.

- A. 81 is the square of the sum alone; the 2xy term was ignored.
- B. (key) 41
- C. 49 subtracts 2 times 16, treating 16 as the product rather than 20.
- D. 121 adds the product to the square of the sum instead of subtracting twice it.

- Trap: The identity x^2 + y^2 = (x+y)^2 - 2xy avoids finding the integers at all.
- Shortcut and time target: Use (sum)^2 - 2 x product; check with the integers 4 and 5. Target 70 s.

**R1-Q07 — D.** Multiples of 15 in range and two-digit numbers with digit product 6 do not overlap. I alone: not unique (6 values, e.g. 15, 30, 45, 60); II alone: not unique (4 values, e.g. 16, 23, 32, 61); together: no admissible value satisfies it.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: Neither alone is unique and together no number fits, so the pair cannot determine N.
- Shortcut and time target: List the multiples of 15 and test each for a digit product of 6. Target 80 s.

**R1-Q08 — A.** 9^7 = 3^14, 27^5 = 3^15, 81^3 = 3^12 and 3^13 remain as they are; the largest exponent of base 3 is 15.

- A. (key) 27^5
- B. 9^7 = 3^14, which is less than 3^15.
- C. 81^3 = 3^12, which is smaller than 3^13.
- D. 3^13 is smaller than 3^15 once every base is written as a power of 3.

- Trap: Writing every base as the same prime power is the only clean comparison; comparing decimal estimates is slow and error-prone.
- Shortcut and time target: Rewrite each base as 3 raised to a power and compare exponents. Target 70 s.

**R1-Q09 — C.** The absolute value gives 5 and -1; the positivity statement removes -1. I alone: not unique (2 values, e.g. -1, 5); II alone: not unique (20 values, e.g. 1, 10, 11, 12); together: unique value 5.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: The second statement alone leaves many values; only the pair removes the negative root.
- Shortcut and time target: Write both branches, then apply the sign condition. Target 70 s.

**R1-Q10 — C.** Multiples of 5 and perfect squares overlap only at 25 within 1 to 60. I alone: not unique (12 values, e.g. 10, 15, 20, 25); II alone: not unique (7 values, e.g. 1, 16, 25, 36); together: unique value 25.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement alone leaves several values; the overlap is a single number.
- Shortcut and time target: List perfect squares up to 60 and test divisibility by 5. Target 75 s.

**R1-Q11 — B.** Make b equal: 3 and 4 become 12. Then a:b = 8:12 and b:c = 12:15, so a:c = 8:15.

- A. 6:15 multiplies the first and second terms of the two ratios directly without aligning b.
- B. (key) 8:15
- C. 2:5 uses the ratio of b and c as if it were a and c; b was never eliminated.
- D. 8:20 scales c by 4 without bringing b to a common value; the b-terms never match.

- Trap: The shared term must be equalised before the ratios can be chained.
- Shortcut and time target: Find the least common multiple of the two b-terms (12) and scale each ratio to it. Target 70 s.

**R1-Q12 — C.** Let the tens digit be t and the units digit u. Then t - u = 2 and t + u = 12, giving t = 7 and u = 5. The number is 75.

- A. 57 has the digits reversed: its units digit exceeds its tens digit.
- B. 84 has digits differing by 4, not 2, and sum to 12, so it fails the difference.
- C. (key) 75
- D. 66 has digits that differ by 0, so the difference condition fails.

- Trap: The word 'exceeds' fixes the order of the digits; reversing them is the main slip.
- Shortcut and time target: Solve the sum and difference of the digits, then check the order of the digits. Target 75 s.

**R1-Q13 — B.** Each statement alone gives n = 3: the linear equation is one-valued and the odd power of 3 is unique. I alone: unique value 3; II alone: unique value 3; together: unique value 3.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Two statements can both be sufficient; the item then rewards recognising uniqueness, not computing.
- Shortcut and time target: Solve the linear statement and check whether the cube statement is one-valued. Target 60 s.

**R1-Q14 — A.** Squares 1 to 40 are 1, 4, 9, 16, 25, 36. Those divisible by 3 are 9 and 36: two common elements.

- A. (key) 2
- B. 6 is the number of perfect squares in Q (1, 4, 9, 16, 25, 36), not the common count.
- C. 13 is the number of multiples of 3 in P (3 to 39), not the intersection.
- D. 0 assumes that no square is divisible by 3, which misses 9 and 36.

- Trap: A square divisible by 3 must have 3 as a factor of its root, so only squares of multiples of 3 qualify.
- Shortcut and time target: Check the squares only; a square is in P exactly when its root is a multiple of 3. Target 80 s.

**R1-Q15 — C.** The inequality splits into x >= 3 or x <= -5. Within [-10, 5] that gives 3, 4, 5 and -10 to -5, which is 3 + 6 = 9 integers.

- A. 3 counts only the branch x + 1 >= 4 (that is, 3, 4, 5) and ignores the negative branch.
- B. 6 counts only the negative branch -10 to -5 and ignores the positive branch.
- C. (key) 9
- D. 15 removes only x = -1 from the 16 integers, forgetting that the whole block from -4 to 2 is excluded.

- Trap: The absolute-value inequality with >= gives two disjoint branches; the middle block is excluded.
- Shortcut and time target: Count the two branches separately (3 and 6 values) and add them. Target 90 s.

**R1-Q16 — A.** Salt is conserved: 0.4 x 1 = 0.25 x (1 + w), so 1 + w = 1.6 and w = 0.6 litre.

- A. (key) 0.6
- B. 0.4 repeats the concentration of the original solution rather than the water added.
- C. 0.375 divides the concentration gap by 0.4 instead of working with total solution volume.
- D. 1.6 equates 0.4 with 0.25 times the water alone, forgetting the 1 litre of solution in the total.

- Trap: Balance the salt, not the volume; the final volume is the original litre plus the water.
- Shortcut and time target: Set salt before = salt after and solve for the final volume (1.6 litre), then subtract 1. Target 90 s.

**R1-Q17 — D.** Statement II is three times Statement I, so it adds nothing new; x is not fixed. I alone: not unique (14 values, e.g. -1, -2, -3, -4); II alone: not unique (14 values, e.g. -1, -2, -3, -4); together: not unique (14 values, e.g. -1, -2, -3, -4).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: Proportional equations contribute one constraint; two unknowns need two independent relations.
- Shortcut and time target: Check whether the second equation is a multiple of the first before solving. Target 60 s.

**R1-Q18 — B.** The two branches give 3x - 2 = 10 (x = 4) and 3x - 2 = -10 (x = -8/3). Their sum is 4 - 8/3 = 4/3.

- A. 4 keeps only the positive branch 3x - 2 = 10 and drops the negative branch.
- B. (key) 4/3
- C. 20/3 adds the magnitudes 4 and 8/3 of the two roots rather than their signed sum.
- D. 8/3 is the magnitude of the negative root alone, not the sum of the solutions.

- Trap: The absolute value gives two branches; both roots are real and must be added with their signs.
- Shortcut and time target: Write both branches and add the signed roots; the sum equals (10+2)/3 + (-10+2)/3 = 4/3. Target 75 s.

**R1-Q19 — B.** -9 < 2n - 7 < 9 gives -2 < 2n < 16, so -1 < n < 8. The integers are 0 through 7: eight of them.

- A. 7 counts 1 to 7 only, dropping 0 because the lower bound was misread as n > 0.
- B. (key) 8
- C. 9 treats the upper bound as closed (2n - 7 = 9 allowed), giving 0 to 8, so the lower bound -1 is the only excluded end.
- D. 16 counts the values of 2n between -2 and 16, not the integers n.

- Trap: Both inequalities are strict, so neither -1 nor 8 is admitted.
- Shortcut and time target: Solve the double inequality to an open interval, then count integers strictly between the ends. Target 75 s.

**R1-Q20 — A.** Statement I pins x = 5 uniquely; Statement II allows both 5 and -5. I alone: unique value 5; II alone: not unique (2 values, e.g. -5, 5); together: unique value 5.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A squared statement is usually two-valued until a sign condition is added.
- Shortcut and time target: Solve the linear statement; for the squared statement count both roots. Target 60 s.

**R1-Q21 — B.** Let the son be s and the father 3s. In 8 years: 3s+8 = 2(s+8), so 3s+8 = 2s+16 and s = 8. Check: 32 = 2 x 16.

- A. Shifting only the son's age: 3s = 2(s+8) gives 16, but the father's shift is ignored.
- B. (key) 8
- C. Son 6, father 18: in 8 years 26 versus 2 x 14 = 28, so it fails.
- D. Son 12, father 36: in 8 years 44 versus 2 x 20 = 40, so it fails.

- Trap: Both persons age by the same 8 years; adding 8 to only one side is the commonest slip.
- Shortcut and time target: Write both future ages as (present + 8) before equating; test the answer by substitution. Target 75 s.

**R1-Q22 — A.** Let c be correct, so wrong = 40 - c. Then 3c - (40 - c) = 72, which gives 4c = 112 and c = 28. Check: 84 - 12 = 72.

- A. (key) 28
- B. 24 ignores the penalty: 3c = 72 would apply only if wrong answers cost nothing.
- C. 32 equals 72 minus 40: the attempt count was subtracted from the score, which the marking scheme does not allow.
- D. 30 gives 3(30) - 10 = 80, not 72; the penalty count was miscounted.

- Trap: The penalty applies to attempted-but-wrong questions, so the count of wrong answers is 40 - c, not 40.
- Shortcut and time target: Use score = 4c - 40 (3c - (40-c)); solve 4c = 112 directly. Target 85 s.

**R1-Q23 — A.** (a + 1/a)^2 = a^2 + 2 + 1/a^2, so a^2 + 1/a^2 = 25 - 2 = 23.

- A. (key) 23
- B. 25 is 5 squared; the cross term -2 was forgotten.
- C. 21 subtracts 4 where the cross term is 2, so the constant is read as the square of 2.
- D. 27 adds 2 to 25, which reverses the sign of the cross term.

- Trap: The identity (a + 1/a)^2 = a^2 + 2 + 1/a^2 is the only step; squaring the given expression is the route.
- Shortcut and time target: Square the given sum and subtract 2 (the cross term). Target 70 s.

**R1-Q24 — B.** sqrt45 + sqrt20 = 3 sqrt5 + 2 sqrt5 = 5 sqrt5, about 11.18; the others are about 8.94, 8.49 and 7.94.

- A. sqrt80 = 4 sqrt5, which is smaller than 5 sqrt5 for the first option.
- B. (key) sqrt45 + sqrt20
- C. sqrt98 - sqrt2 = 6 sqrt2, about 8.49; the two radicals were not combined correctly.
- D. sqrt28 + sqrt7 = 3 sqrt7, about 7.94.

- Trap: Factoring out the perfect square under each root converts every term to a multiple of the same radical.
- Shortcut and time target: Simplify each radical to a single surd multiple, then compare coefficients. Target 75 s.

**R1-Q25 — B.** 16 divides x squared only if the power of 2 in x is at least 2, so 4 divides x; 8 divides x also forces 4 to divide x. I alone: unique value yes; II alone: unique value yes; together: unique value yes.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Both statements give a yes answer, so either one settles the question.
- Shortcut and time target: Count the power of 2: a square divisible by 16 needs two factors of 2 in x. Target 80 s.

**R1-Q26 — C.** The sum alone gives several products; the difference alone gives several products; together a=8 and b=4 give 32. I alone: not unique (6 values, e.g. 11, 20, 27, 32); II alone: not unique (16 values, e.g. 117, 12, 140, 165); together: unique value 32.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Do not conclude from the sum or the difference alone that the product is fixed.
- Shortcut and time target: Check the product list for the sum statement; it is not constant. Target 85 s.

**R1-Q27 — C.** Numbers with exactly three positive factors are squares of primes (4, 9, 25, 49); the range statement leaves only 25. I alone: not unique (4 values, e.g. 25, 4, 49, 9); II alone: not unique (19 values, e.g. 11, 12, 13, 14); together: unique value 25.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Exactly three divisors means n is the square of a prime; check the numbers that qualify, not the factor arithmetic.
- Shortcut and time target: List the squares of primes up to 100, then apply the range. Target 85 s.

**R1-Q28 — D.** Collect terms: -6x > -12. Dividing by the negative number -6 reverses the sign, so x < 2. Check x = 0: 7 > -5 is true.

- A. Dividing -6x > -12 by -6 without reversing the sign gives x > 2.
- B. A sign slip in moving 7 and -5 across the inequality (12 = 6x read as -12 = 6x) gives x < -2.
- C. Mixing the sign of the 6x term with the constant gives x > -2.
- D. (key) x < 2

- Trap: The sign must be reversed when dividing by -6, and only then.
- Shortcut and time target: Move x-terms to one side and divide by the coefficient, flipping the sign when the coefficient is negative. Target 60 s.

**R1-Q29 — A.** Per-kilometre rate = (300 - 196)/8 = 13. Fixed charge = 196 - 12 x 13 = 40. Check: 20 x 13 + 40 = 300.

- A. (key) 40
- B. 13 is the charge per kilometre, not the fixed charge.
- C. 52 is 196 minus 12 times 12, which treats 12 as the rate.
- D. 60 is 300 minus 20 times 12, which reuses the 12 km rate in the second trip.

- Trap: Two trips give two equations; the difference cancels the fixed charge and reveals the rate.
- Shortcut and time target: Subtract the two bills and divide by the difference in kilometres to find the rate first. Target 85 s.

**R1-Q30 — C.** Let the middle integer be m. Then 3m = 81 and m = 27, so the integers are 25, 27 and 29; the largest is 29.

- A. 27 is the middle integer, not the largest.
- B. 31 is 27 plus 4, which treats the spacing as 4 rather than 2.
- C. (key) 29
- D. 25 is the smallest of the three integers, not the largest.

- Trap: The sum of three consecutive odd integers equals three times the middle one.
- Shortcut and time target: Divide the sum by 3 to get the middle integer, then add 2. Target 65 s.

**R1-Q31 — B.** From 4x - y = 7, y = 4x - 7. Substitute: 2x + 3(4x - 7) = 21, so 14x = 42, x = 3, y = 5. Then x + 2y = 3 + 10 = 13.

- A. 8 is x + y, which is the wrong combination of the two unknowns.
- B. (key) 13
- C. 15 is x times y, a product rather than the requested linear expression.
- D. 21 is the right-hand side of the first equation, not an expression in x and y.

- Trap: The value asked is x + 2y, not x or y; solving for both first is the safe route.
- Shortcut and time target: Eliminate y using the second equation, then read the requested combination. Target 85 s.

**R1-Q32 — D.** The slope m = (-2 - 4)/(6 - 0) = -1 and the intercept c = 4, so m + c = 3.

- A. -1 is the slope m alone, not the sum m + c.
- B. 4 is only the intercept c, not the sum.
- C. 5 takes the slope as +1, misreading the sign of the rise between (0, 4) and (6, -2).
- D. (key) 3

- Trap: Find the slope from the two points, then use the y-intercept given by the point (0, 4).
- Shortcut and time target: Compute m = rise/run; the intercept is read off where x = 0. Target 75 s.

**R1-Q33 — A.** Let A=3k and B=5k. After the addition 3k+4000=5k, so 2k=4000, k=2000 and B=5k=10000.

- A. (key) 10000
- B. 6000 is A's original amount (3k with k = 2000), not B's.
- C. 14000 comes from adding the Rs 4,000 to B instead of A, which breaks the equal-amounts condition.
- D. 8000 is twice the added amount; the increase is not doubled anywhere in the equation.

- Trap: Writing the equation for equal amounts after the addition is the decisive step; the ratio alone does not give B.
- Shortcut and time target: Solve 2k = 4000 directly from the difference of the two parts. Target 80 s.

**R1-Q34 — A.** The product is largest when the parts are equal, so take the integers nearest to 19/2: 9 and 10, giving 90.

- A. (key) 90
- B. 88 is 8 times 11, a valid pair with sum 19, but not the largest product.
- C. 72 is 8 times 9, which has sum 17, not 19.
- D. 99 is 9 times 11, which has sum 20, not 19.

- Trap: Among integers with a fixed sum, the pair closest together gives the largest product.
- Shortcut and time target: Test the pair nearest the midpoint (9.5); each step away reduces the product by the square of the gap. Target 75 s.

**R1-Q35 — C.** Tens digit t and units u: t+u=11 and (10u+t)-(10t+u)=27, so u-t=3, giving u=7, t=4. Check: 74-47=27.

- A. Satisfies the digit sum, but reversal gives 83, which is 45 more, not 27.
- B. Its reversal is 65, which is 9 more, so the stated increase is wrong.
- C. (key) 47
- D. Reversal gives 65 for 56, a difference of 9; the tens digit was read as the larger one.

- Trap: Writing the reversal equation as 9(u-t)=27 is the step that fixes the digits; the sum alone does not.
- Shortcut and time target: Use the sum to list candidates (29,38,47,56,65,74,83,92), then test the difference of 27 on each. Target 70 s.

**R1-Q36 — C.** I alone leaves several multiples of 7; II alone leaves several digit-sum-5 values; together only 14 survives. I alone: not unique (13 values, e.g. 14, 21, 28, 35); II alone: not unique (5 values, e.g. 14, 23, 32, 41); together: unique value 14.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Judge uniqueness of the pair, not the arithmetic value.
- Shortcut and time target: List the multiples of 7 and test the digit sum; stop when one value survives. Target 85 s.

**R1-Q37 — A.** The square allows +9 and -9; the cube statement forces -9 alone. I alone: not unique (2 values, e.g. -9, 9); II alone: unique value -9; together: unique value -9.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A cube keeps the sign, so the second statement is decisive where the first is not.
- Shortcut and time target: Find the roots of the square, then see whether the cube selects one. Target 70 s.

**R1-Q38 — B.** The four corner products of the open rectangle are -6, 0, 0 and 3 with the corners excluded, so xy lies strictly between -6 and 3; xy > -6 always holds.

- A. Fails: x = 0.9 and y = 2.9 give xy = 2.61, which exceeds 2.
- B. (key) xy > -6 always holds
- C. Fails: x = 0.9 and y = 2.9 give x + y = 3.8, which exceeds 3.
- D. Fails: x = -1.9 and y = 2.9 give x - y = -4.8, which is below -3.

- Trap: A product of an interval with a sign-changing interval needs all four corners; the naive lower bound (-2 times 0 is not the minimum) is misleading here.
- Shortcut and time target: Test the four corner products, then check the one-sided claim against the nearest corner. Target 90 s.

**R1-Q39 — D.** Each inequality alone leaves many integers, and together they leave 4 through 8. I alone: not unique (17 values, e.g. 10, 11, 12, 13); II alone: not unique (29 values, e.g. -1, -10, -11, -12); together: not unique (5 values, e.g. 4, 5, 6, 7).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: Combined bounds narrow the set but do not fix a value.
- Shortcut and time target: Intersect the two bounds and count what remains. Target 60 s.

**R1-Q40 — A.** Statement I allows both signs for nonzero x; Statement II forces x > 0 because cubes keep the sign of the base. I alone: not unique (2 values, e.g. no, yes); II alone: unique value yes; together: unique value yes.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: x squared greater than 0 only rules out x = 0; both signs remain.
- Shortcut and time target: Ask whether the statement fixes the sign; a cube does and a square does not. Target 70 s.

**R1-Q41 — D.** 7n - 5n > 19 + 3 gives 2n > 22, so n > 11. The least integer greater than 11 is 12.

- A. 11 is the boundary value of the inequality, which is excluded because the inequality is strict.
- B. 23 mis-solves 2n > 22 as n > 22 and then misreads the least integer.
- C. 14 comes from an arithmetic slip that gives 2n > 26, so n > 13 and the answer 14.
- D. (key) 12

- Trap: A strict inequality excludes its boundary, so the answer is the next integer, not the boundary.
- Shortcut and time target: Solve to a strict bound, then take the next integer above it. Target 70 s.

**R1-Q42 — B.** The corner products are -3, -15, 2 and 10. The minimum -15 needs x = -3, which is excluded, and the maximum 10 needs x = 2, also excluded; so the range is open at both ends.

- A. (-3, 10) applies the naive rule that multiplies the lower bounds together, missing the corner -3 times 5 = -15.
- B. (key) (-15, 10)
- C. (-15, 2) takes the largest product from the wrong corner and ignores 2 times 5 = 10.
- D. [-15, 10] closes both ends, but both extremes are approached only through an excluded endpoint (x = -3 and x = 2).

- Trap: Endpoint inclusion must be checked for each extreme; the extremes are not automatically attained.
- Shortcut and time target: Tabulate the four corners and mark the endpoint responsible for each extreme as open or closed. Target 100 s.

**R1-Q43 — D.** -3 < 2x-1 gives x > -1; 2x-1 <= 9 gives x <= 5. So x in {0,1,2,3,4,5}; removing x = 2 leaves 5 integers.

- A. 6 forgets the exclusion of x = 2 and counts 0 to 5 as six integers.
- B. 4 loses one admissible integer through a slip in the upper bound (2x <= 8 instead of 2x <= 10).
- C. 7 treats both bounds as closed and forgets the exclusion, counting -1 to 5.
- D. (key) 5

- Trap: The lower bound is strict (x > -1, so -1 is excluded); a closed bound at -1 gives a wrong count.
- Shortcut and time target: Find the integer interval first, count its members, then subtract any excluded integers that lie inside. Target 80 s.

**R1-Q44 — A.** Statement I forces n odd (an odd square has an odd root); Statement II allows odd and even multiples of 3. I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A multiple of 3 can be odd or even, so the second statement is silent on parity.
- Shortcut and time target: Recognise that the square's parity equals the root's parity; test one multiple of 3 of each parity. Target 60 s.

**R1-Q45 — D.** The numbers are (45+9)/2 = 27 and (45-9)/2 = 18; their product is 486.

- A. 405 is 45 times 9, the sum multiplied by the difference.
- B. 324 is 18 squared, the square of the smaller number, not the product.
- C. 540 is 30 times 18, a pair that does not have sum 45 and difference 9.
- D. (key) 486

- Trap: Half the sum plus half the difference gives the larger number, and the other is half the sum minus half the difference.
- Shortcut and time target: Use (S+D)/2 and (S-D)/2; check the sum and difference before multiplying. Target 70 s.

**R1-Q46 — B.** For 0 < t < 1, t^3 < t^2 < t < sqrt(t); the square root of a proper fraction exceeds the fraction itself.

- A. t is less than sqrt(t) when 0 < t < 1, since multiplying a fraction by itself makes it smaller but taking its root makes it larger.
- B. (key) sqrt(t)
- C. t^2 is less than t for 0 < t < 1.
- D. t^3 is the smallest of the four for 0 < t < 1.

- Trap: Taking a root of a number between 0 and 1 moves it towards 1, which reverses the naive intuition.
- Shortcut and time target: Test a value such as t = 0.25: 0.25, 0.0625, 0.5 and 0.015625 give the answer at once. Target 70 s.

**R1-Q47 — D.** For -1 < a < 0, -a is in (0,1), and a^2 = (-a)^2 is smaller than -a; 1/a is negative and below -1.

- A. a is negative and so less than every positive option.
- B. a^2 is the square of a number less than 1 in size; it is smaller than -a.
- C. 1/a is less than -1 because the reciprocal of a negative proper fraction is a negative number of magnitude above 1.
- D. (key) -a

- Trap: A negative proper fraction is compared with its own magnitude; squaring makes it smaller, but the reciprocal is negative.
- Shortcut and time target: Pick a = -0.5: the values are -0.5, 0.25, -2 and 0.5, so -a is the greatest. Target 75 s.

**R1-Q48 — D.** 3m + 4 odd means 3m is odd, so m is odd. The other options are contradicted or unforced.

- A. Fails: m = 1 satisfies the premise (3 + 4 = 7 is odd), yet m is not even.
- B. Fails: m = 1 gives m + 1 = 2, which is even.
- C. Fails: 2m + 1 is always odd, so it is never even.
- D. (key) m is odd

- Trap: Subtract 4 (even) and divide by the odd coefficient 3: parity is preserved in both steps.
- Shortcut and time target: Track parity: odd minus even is odd, and an odd multiple of m is odd only when m is odd. Target 75 s.

**R1-Q49 — D.** The remainders fix the value by themselves. Numbers leaving remainder 3 on division by 7 are 3, 10, 17, ...; of these, 3 leaves remainder 3 on division by 5, 10 leaves 0, and 17 leaves 2. So the smallest such integer is 17, and the question is answered without either statement.

- A. Wrong: the question already fixes 17 before any statement is read, so the verdict "exactly one statement suffices" does not apply.
- B. Wrong: the same reason; neither statement is needed, so "each suffices alone" misreads the item.
- C. Wrong: the pair is not needed either; 17 comes from the stem alone.
- D. (key) The question can be answered without any statement: the first value leaving remainder 2 on division by 5 in the list 3, 10, 17 is 17.

- Trap: Reading the statements first and choosing a letter. In this form option D asks whether the stem alone pins a value, so check the stem before the statements.
- Shortcut and time target: Test the numbers that leave remainder 3 on division by 7 in increasing order until one leaves remainder 2 on division by 5. Target 60 s.

**R1-Q50 — A.** Statement I gives x^2 = 49. With x positive, x = 7 and the value is 3(49) - 35 = 112. Statement II alone leaves x between 1 and 9, and the value changes with x. The stem alone is not enough (x = 1 gives -2, x = 2 gives 2).

- A. (key) Correct verdict: Statement I alone gives 112; Statement II alone does not.
- B. Wrong: Statement II alone does not fix the value (x = 1 gives -2, x = 2 gives 2, x = 3 gives 12).
- C. Wrong: Statement I alone already suffices, so the pair is not needed.
- D. Wrong: the question alone does not fix x; the self-sufficiency option is false.

- Trap: Taking x = -7 from x^2 = 49. The "positive integer" condition removes it, and that restriction is what makes Statement I sufficient.
- Shortcut and time target: x^2 = 49 with x positive gives one root; test whether any statement leaves a range of x. Target 70 s.

**R1-Q51 — D.** The largest three-digit square is 31^2 = 961, since 32^2 = 1024 has four digits. Its digits sum to 9 + 6 + 1 = 16. The question alone determines the answer, so neither statement is needed.

- A. Wrong: the largest three-digit square is fixed by the stem; Statement I (odd) is true of 961 but is not needed, so "exactly one suffices" misreads the item.
- B. Wrong: the same reason; no statement is needed, so "each suffices alone" does not apply.
- C. Wrong: the pair is not needed; the stem gives 961.
- D. (key) The question can be answered without any statement: 961 is fixed by the stem.

- Trap: Treating 1024 as a three-digit square because 32^2 looks close to 1000. The three-digit limit is 999, and the square root of 999 is about 31.6.
- Shortcut and time target: Take the integer square root of 999 (31) and square it. Target 60 s.

**R1-Q52 — B.** The sum of three odd primes is odd, so the sum 40 requires the prime 2. Then q + r = 38 with 2 < q < r; the only pair of primes is (7, 31), so r = 31. Statement II: 62 = 2 x 31 with p < r, so p = 2 and r = 31 again. Each statement alone fixes r.

- A. Wrong: Statement II alone also fixes r = 31, so "exactly one" fails.
- B. (key) Each statement alone suffices: both give r = 31.
- C. Wrong: each statement suffices alone, so the pair is not needed.
- D. Wrong: the two statements together give r = 31; the pair is consistent and decisive.

- Trap: Forgetting the parity argument. Without it a solver may try prime sums that do not contain 2; with it the set collapses to one candidate pair.
- Shortcut and time target: Parity: 40 is even, so one prime is 2. Then check which prime pair sums to 38. Target 80 s.

**R1-Q53 — A.** Statement I: boys form 3/5 of the class, so N must be a multiple of 5 in the range 30 to 50: 30, 35, 40, 45 or 50. Statement II: more than 49 students in the range 30 to 50 means N = 50. Only Statement II fixes the number alone.

- A. (key) Exactly one suffices: Statement II alone gives 50; Statement I alone leaves five candidates.
- B. Wrong: Statement I alone does not fix N; the five multiples of 5 remain.
- C. Wrong: Statement II alone already suffices, so the pair is not needed.
- D. Wrong: the pair gives 50 as well; the question is answered.

- Trap: Treating the 3/5 fraction as if it fixed the class size. A fraction of N is a whole number for every multiple of 5, so the statement only narrows N.
- Shortcut and time target: For a fraction of the class to be whole, N must be a multiple of the denominator. Target 70 s.

**R1-Q54 — B.** x ∇ 3 = x^2 - 3 and 2 ∇ x = 4 - x. The inequality is x^2 + x - 7 > 0, whose larger root is (-1 + sqrt(29))/2, about 2.19. So x >= 3, and every integer from 3 to 30 satisfies it: 28 values.

- A. 27 counts only x = 4 to 30. It treats the root 2.19 as if x = 3 were excluded; but x = 3 gives 6 > 1.
- B. (key) 28. The inequality holds for x = 3 to 30.
- C. 29 counts x = 2 to 30. At x = 2 the left side is 1 and the right side is 2, so the inequality fails.
- D. 30 counts every integer in the range. The inequality removes x = 1 (-2 is not greater than 3) and x = 2.

- Trap: Reversing the roles in 2 ∇ x (writing it as 2^2 - 3x or as x^2 - 2). The first operand is always the number before the symbol.
- Shortcut and time target: Test x = 2 (fails) and x = 3 (passes); the inequality holds for all larger x. Target 90 s.

**R1-Q55 — C.** Each statement is necessary: a multiple of 12 is always a multiple of 4 and of 3. Neither is sufficient: m = 4 satisfies Statement I but not the question, while m = 12 satisfies both and gives yes. Together, m is a multiple of 4 and of 3, so it is a multiple of lcm(4, 3) = 12, and the answer is yes.

- A. Wrong: Statement I alone gives yes for 12 and no for 4, so it does not decide the question.
- B. Wrong: Statement II alone gives yes for 12 and no for 3, so neither statement suffices alone.
- C. (key) Both together are sufficient: the answer is always yes.
- D. Wrong: the pair decides the question; the answer is yes for every admissible m.

- Trap: Mistaking necessity for sufficiency. Each statement is necessary, but the pair is sufficient.
- Shortcut and time target: Use lcm(4, 3) = 12; the pair answers the question. Target 60 s.

**R1-Q56 — C.** Statement I: x is a factor of 36 and greater than 5, so x is 6, 9, 12 or 18. Statement II: x is a multiple of 4. Together, x must be a multiple of 4 from that list, which is 12 only (18 is not divisible by 4). Neither statement alone is decisive.

- A. Wrong: Statement I alone leaves 6, 9, 12 and 18; Statement II alone leaves 4, 8, 12, 16, 20, 24 and 28. Neither alone is decisive.
- B. Wrong: Statement II alone leaves seven candidates, so it cannot decide the question.
- C. (key) Both together are sufficient: their intersection is 12.
- D. Wrong: the pair fixes x = 12, so the value is determined.

- Trap: Including 18 because it divides 36 and exceeds 5, while forgetting that Statement II requires a multiple of 4. The intersection step removes it.
- Shortcut and time target: Intersect the two lists instead of testing each integer from 1 to 29. Target 75 s.
