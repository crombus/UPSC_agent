# CSAT 05 — Revision 3: worked answers (original items)

Every key is verified by computation (see `AUDIT.md`). Time targets assume the 72-second budget per item.

**R3-Q01 — D.** Solving for integers gives y = 2, 5, 8 with x = 12, 7, 2. Only y = 2 satisfies x > 2y, so x = 12.

- A. 7 satisfies the equation with y = 5, but x > 2y fails (7 is not greater than 10).
- B. 2 is the value from y = 8, which fails x > 2y since 2 is not greater than 16.
- C. 10 gives no integer y: 46 - 30 = 16 is not divisible by 5.
- D. (key) 12

- Trap: A second condition (x > 2y) is what removes the extra integer solutions of a linear Diophantine equation.
- Shortcut and time target: List y by its residue, compute x for each, then apply the inequality. Target 100 s.

**R3-Q02 — A.** Left side = x/3 + x/6 = x/2. The equation becomes x/2 = 1 + x/2, which reduces to 0 = 1. No value works.

- A. (key) No value of x satisfies it
- B. x = 0 gives 0 = 1, which is false.
- C. x = 6 gives 3 on the left and 4 on the right.
- D. x = 3 gives 1.5 on the left and 2.5 on the right.

- Trap: Combine the fractions before solving: a linear equation whose x-terms cancel may have no solution.
- Shortcut and time target: Combine the left side first; if the variable cancels to a false constant, there is no solution. Target 75 s.

**R3-Q03 — D.** Both statements leave many multiples of 2 or 4 that are not multiples of 3; the pair does not decide. I alone: not unique (2 values, e.g. no, yes); II alone: not unique (2 values, e.g. no, yes); together: not unique (2 values, e.g. no, yes).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: The answer is 'neither suffices' because 4 and 6 differ in prime factors.
- Shortcut and time target: A divisor by an unrelated number does not force divisibility by 3. Target 70 s.

**R3-Q04 — B.** x + y + z = 36, so (y + 6) + y + (y - 6) = 36, giving 3y = 36 and y = 12.

- A. 10 is (36 - 6)/3, which applies the offset only once.
- B. (key) 12
- C. 14 is (36 + 6)/3, which adds the offset instead of cancelling it.
- D. 18 is y + 6, the value of x rather than y.

- Trap: Offsets of +6 and -6 cancel in the sum, so the sum gives 3y directly.
- Shortcut and time target: Add the three expressions; the offsets cancel, so divide the total by 3. Target 75 s.

**R3-Q05 — A.** The square statement holds for every integer, so it says nothing; the cube statement forces m >= 0. I alone: not unique (2 values, e.g. no, yes); II alone: unique value yes; together: unique value yes.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: The cube keeps the sign of its base, so only the cube statement decides the question.
- Shortcut and time target: A statement true for every value in the set is not a filter. Target 70 s.

**R3-Q06 — D.** P = 40 + 52 + 48 = 140. Q = (45 + 50 + 47) - (38 + 60 + 44) = 142 - 142 = 0. So P is greater than Q.

- A. P is 140 and Q is 0, so P is not less than Q.
- B. P is 140 and Q is 0, so they are not equal.
- C. The table gives every mark, so the relation is fixed.
- D. (key) P is greater than Q

- Trap: Each quantity is a sum from the table; read the tables carefully before subtracting the two totals.
- Shortcut and time target: Add each row, then compare P with the difference Q. Target 85 s.

**R3-Q07 — A.** p^2 = q^2 means |p| = |q|, so p = q or p = -q.

- A. (key) p = q or p = -q
- B. p = q alone is not forced: p = 2 and q = -2 satisfy p^2 = q^2.
- C. Both positive is not forced: p = 2 and q = -2 give a negative q.
- D. p + q = 0 is not forced: p = q = 1 satisfies p^2 = q^2 with a non-zero sum.

- Trap: A squared equality allows a sign choice; state both branches before deciding.
- Shortcut and time target: Rewrite as p^2 - q^2 = 0, factor to (p - q)(p + q) = 0, then read the two branches. Target 80 s.

**R3-Q08 — A.** Pay = 500(30 - a) - 150a = 15000 - 650a. Setting this to 12400 gives a = 4.

- A. (key) 4
- B. 3 days absent gives 500 x 27 - 150 x 3 = Rs 13,050.
- C. 5 days absent gives 500 x 25 - 150 x 5 = Rs 11,750.
- D. 6 days absent gives 500 x 24 - 150 x 6 = Rs 11,100.

- Trap: A worked day and an absent day move the total in opposite directions; the net effect per day is what matters.
- Shortcut and time target: Write pay as 15000 minus 650 for each absence, then solve. Target 90 s.

**R3-Q09 — B.** Total of four = 100; total of three = 66; removed number = 100 - 66 = 34.

- A. 22 is the average of the remaining three, not the removed number.
- B. (key) 34
- C. 25 is the original average of the four numbers; it does not answer the removal question.
- D. 28 comes from 100 - 72, where 72 is a slip for 3 times 24.

- Trap: Convert averages to totals before removing a value; averages do not subtract directly.
- Shortcut and time target: Multiply both averages by their counts, then subtract. Target 70 s.

**R3-Q10 — D.** The product statement leaves 0 and 1; the upper bound keeps both. The pair does not fix x. I alone: not unique (2 values, e.g. 0, 1); II alone: not unique (26 values, e.g. -1, -10, -11, -12); together: not unique (2 values, e.g. 0, 1).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: The 'at most' bound is satisfied by both roots, so it does not decide the case.
- Shortcut and time target: A bound that does not exclude any root of the other statement cannot break a tie. Target 70 s.

**R3-Q11 — B.** Net factor = 0.8 x 1.5 = 1.2. So the original is 480 / 1.2 = 400.

- A. 320 divides 480 by 1.5 and ignores the 20 per cent cut, which must also be undone.
- B. (key) 400
- C. 384 applies the 20 per cent cut to the final price instead of the original.
- D. 576 multiplies 480 by 1.2, applying the net change to the final price in the wrong direction.

- Trap: A sequence of percentage changes multiplies; undo the changes in reverse order and divide by the net factor.
- Shortcut and time target: Multiply the factors (0.8 x 1.5) and divide the final price by the product. Target 90 s.

**R3-Q12 — A.** 1.5n is an integer only for even n; n + 2 is a multiple of 5 means n = 3, 8, 13, ... Intersecting gives 8, 18, ...; the least is 8.

- A. (key) 8
- B. 3 fails: 1.5 times 3 = 4.5 is not an integer.
- C. 13 fails: 1.5 times 13 = 19.5 is not an integer.
- D. 18 satisfies both conditions but is not the least such integer.

- Trap: Turn each condition into a residue class and find the first common value.
- Shortcut and time target: List residues: even n, and n congruent to 3 mod 5; take the first common value. Target 90 s.

**R3-Q13 — D.** Statement II (n + 8 a multiple of 10) means n leaves remainder 2 on division by 10, which already implies Statement I. The pair adds nothing. I alone: not unique (20 values, e.g. 12, 17, 2, 22); II alone: not unique (10 values, e.g. 12, 2, 22, 32); together: not unique (10 values, e.g. 12, 2, 22, 32).

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. Wrong: the pair does not fix a unique value.
- D. (key) Correct verdict: even the pair leaves the target open.

- Trap: A statement that is a special case of the other is dependent, even when its wording differs.
- Shortcut and time target: Test whether one statement logically implies the other before combining them. Target 85 s.

**R3-Q14 — C.** Multiples of 15 and multiples of 4 below 80 overlap only at 60. I alone: not unique (13 values, e.g. 105, 120, 135, 15); II alone: not unique (19 values, e.g. 12, 16, 20, 24); together: unique value 60.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: The common multiples of 4 and 15 are spaced by 60; only one falls below 80.
- Shortcut and time target: Find the common multiple: multiples of 15 and 4 are multiples of 60. Target 90 s.

**R3-Q15 — B.** 5k - 7 < 3k + 9 gives 2k < 16, so k < 8. 2k + 1 > -3 gives k > -2. The largest integer is 7.

- A. 8 reads the strict bound k < 8 as k <= 8, admitting the boundary value.
- B. (key) 7
- C. 9 comes from moving 7 to the wrong side of the first inequality.
- D. 6 is a boundary slip: it stops one integer below the strict upper bound.

- Trap: The strict bound excludes its endpoint; the largest integer is the one just below it.
- Shortcut and time target: Solve each inequality, intersect, then take the largest integer below the strict bound. Target 75 s.

**R3-Q16 — A.** Let coffee be c, so tea is c + 18 and c + (c + 18) = 46. Then c = 14 and tea = 32.

- A. (key) 32
- B. 14 is the number who prefer coffee, not tea.
- C. 16 is coffee plus two; the difference of 18 was not applied to the coffee count.
- D. 18 is the difference between the two groups, not the tea count.

- Trap: The difference and the total give two equations in two groups; solve for the smaller group first.
- Shortcut and time target: Subtract the difference from the total, halve, and add the difference back. Target 75 s.

**R3-Q17 — C.** The first statement leaves 3, 8, 13, 18, 23, 28; odd and below 10 leaves 1, 3, 5, 7, 9. Together only 3 is left. I alone: not unique (6 values, e.g. 13, 18, 23, 28); II alone: not unique (5 values, e.g. 1, 3, 5, 7); together: unique value 3.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement is a list; the overlap is one number.
- Shortcut and time target: Intersect the list from the first statement with the short list from the second. Target 90 s.

**R3-Q18 — A.** The first statement is equivalent to x positive and settles it; the second allows both signs. I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A lower bound that is negative does not fix the sign.
- Shortcut and time target: Read each inequality for its sign implication. Target 60 s.

**R3-Q19 — A.** The linear statement gives s = 11 alone; the multiple-of-4 statement leaves many values. I alone: unique value 11; II alone: not unique (25 values, e.g. 100, 12, 16, 20); together: no admissible value satisfies it.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: A linear equation with one unknown is the most reliable sufficient statement.
- Shortcut and time target: Solve the linear statement first; a multiple condition rarely fixes a value. Target 60 s.

**R3-Q20 — B.** With m kg of mangoes: 12(14 - m) + 30m = 240, so 168 + 18m = 240 and m = 4.

- A. 6 kg of mangoes would leave 8 kg of apples and cost Rs 276, not Rs 240.
- B. (key) 4
- C. 8 kg of mangoes would leave 6 kg of apples and cost Rs 312.
- D. 10 kg of mangoes would leave 4 kg of apples and cost Rs 348.

- Trap: Express the total cost in one unknown using the total weight; the cost gap per kg is 18 rupees.
- Shortcut and time target: Replace apples with 14 - m and solve the single equation. Target 85 s.

**R3-Q21 — C.** The first statement alone gives several pairs; the second alone gives several pairs. Together a = 5 and b = 4, so the product is 20. I alone: not unique (6 values, e.g. 11, 15, 18, 20); II alone: not unique (10 values, e.g. 108, 140, 176, 20); together: unique value 20.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each linear statement alone leaves several pairs with different products.
- Shortcut and time target: Two independent linear relations fix both numbers; then compute the product. Target 90 s.

**R3-Q22 — D.** Subtract 0.4x from both sides: 0.2x - 0.2 = 0.6, so 0.2x = 0.8 and x = 4.

- A. 2 comes from 0.2x = 0.4, a slip in the constant on the right.
- B. 8 comes from 0.2x = 1.6, which doubles the constant 0.8 instead of using it once.
- C. 0.4 halves 0.8 by mistake instead of dividing it by the coefficient 0.2.
- D. (key) 4

- Trap: Collect the x-terms on one side and the constants on the other; then divide by the coefficient 0.2.
- Shortcut and time target: Multiply by 10 to clear decimals: 6x - 2 = 4x + 6. Target 70 s.

**R3-Q23 — A.** Equal cost: 300 + 40v = 900 + 25v, so 15v = 600 and v = 40. Check: both cost Rs 1,900.

- A. (key) 40
- B. 30 divides the fee difference 600 by 20, which is not the difference in per-visit charges (40 - 25 = 15).
- C. 60 divides the annual fee 900 by 15 and treats the result as a visit count; the fees are not compared directly.
- D. 25 is Plan Y's per-visit charge, not a break-even count.

- Trap: Compare the two cost lines: the fixed-fee gap is divided by the gap in per-visit charges.
- Shortcut and time target: Set the two cost expressions equal and divide the fee gap by the rate gap. Target 85 s.

**R3-Q24 — B.** A cube is positive exactly when its base is; so is a fifth power. Each statement alone settles the question. I alone: unique value yes; II alone: unique value yes; together: unique value yes.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement alone gives the same sign information, so either one is enough.
- Shortcut and time target: Odd powers keep the sign of the base; use that to test the statement quickly. Target 70 s.

**R3-Q25 — D.** 4n > 15 gives n > 3.75, so the smallest positive integer is 4.

- A. 3 gives 39 - 7 = 32 and 27 + 8 = 35, so the inequality fails.
- B. 5 satisfies the inequality but is not the smallest.
- C. 15 treats the bound 4n > 15 as the answer itself.
- D. (key) 4

- Trap: Divide by 4 and read the strict bound; the answer is the next integer above 3.75.
- Shortcut and time target: Collect n-terms, divide by 4, then take the next integer above the bound. Target 70 s.

**R3-Q26 — C.** The total-rate statement alone leaves several splits; the difference statement alone also leaves several. Together a = 6 and b = 8. I alone: not unique (13 values, e.g. 1, 10, 11, 12); II alone: not unique (15 values, e.g. 10, 11, 12, 13); together: unique value 6.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: A rate statement alone is a single linear relation; the two relations must be solved together.
- Shortcut and time target: Two rate relations are needed for two machine rates. Target 85 s.

**R3-Q27 — D.** (3/2)^3 = 27/8 = 3.375; (2/3)^(-2) = (3/2)^2 = 2.25; (2/3)^3 = 8/27. So (3/2)^3 is greatest.

- A. (2/3)^(-2) equals (3/2)^2 = 2.25, which is less than (3/2)^3 = 3.375.
- B. The values are different: 3.375 and 2.25 are not the same.
- C. (2/3)^3 = 8/27, about 0.30, which is the smallest of the four.
- D. (key) (3/2)^3

- Trap: A negative exponent turns the base into its reciprocal; apply that before comparing.
- Shortcut and time target: Rewrite the negative exponent as a reciprocal power, then compare numbers above and below 1. Target 85 s.

**R3-Q28 — C.** The value statement alone leaves c = 1, 3 or 5; the coin-count statement alone leaves 0 to 10. Together 3c = 9, so c = 3 and t = 8. I alone: not unique (3 values, e.g. 1, 3, 5); II alone: not unique (11 values, e.g. 0, 1, 10, 2); together: unique value 3.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement is a linear relation in two counts; the pair is needed because the coin counts are not otherwise linked.
- Shortcut and time target: Solve the two relations together; a single value relation has more than one solution. Target 90 s.

**R3-Q29 — B.** A square divisible by 25 has 5 as a factor of its root; a multiple of 10 has 5 as a factor. Each alone decides the question. I alone: unique value yes; II alone: unique value yes; together: unique value yes.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Either statement settles divisibility by 5 alone, so the answer is 'either alone suffices'.
- Shortcut and time target: Use the power-of-prime rule: a square divisible by p squared forces p to divide the root. Target 80 s.

**R3-Q30 — B.** The range is 21 to 29. The odd values are 21, 23, 25, 27, 29; the highest is 29.

- A. 28 is even and does not satisfy the odd-degree condition.
- B. (key) 29
- C. 27 is odd but not the highest odd value allowed; 29 is also allowed.
- D. 25 is the centre of the range, odd but not the highest.

- Trap: An absolute-value bound gives an interval; apply the parity condition to its ends.
- Shortcut and time target: Write the interval (21 to 29), then pick the largest odd value. Target 75 s.

**R3-Q31 — D.** Try the pairs with difference 5: 7 and 12 give 84, so the larger integer is 12.

- A. 14 would give 14 times 6 = 84 with difference 8, not 5.
- B. 7 is the smaller integer, the pair being 12 and 7.
- C. 17 gives a difference of 5 with the product 204, not 84.
- D. (key) 12

- Trap: A product and a difference determine a pair; check the candidate pair against both.
- Shortcut and time target: Start from the difference (5) and test the integer pairs that multiply to 84. Target 85 s.

**R3-Q32 — C.** The residue statement leaves -12, -7, -2, 3 and 8; the positivity bound below 5 keeps only 3. I alone: not unique (5 values, e.g. -12, -2, -7, 3); II alone: not unique (4 values, e.g. 1, 2, 3, 4); together: unique value 3.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: A residue condition leaves a long list over a symmetric range; a one-sided bound is what makes the answer unique.
- Shortcut and time target: Write the residue class first, then apply the bound to the list it gives. Target 80 s.

**R3-Q33 — C.** Each relation alone allows several prices; together they give p = 7 and q = 8. I alone: not unique (14 values, e.g. 1, 10, 11, 12); II alone: not unique (15 values, e.g. 10, 11, 12, 13); together: unique value 7.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Two independent linear relations are needed; one relation leaves several splits.
- Shortcut and time target: Two linear relations are needed for two unknown prices; check that they are independent. Target 85 s.

**R3-Q34 — D.** sqrt(48) = 4 sqrt(3), sqrt(27) = 3 sqrt(3), sqrt(75) = 5 sqrt(3). Total = (4 + 3 - 5) sqrt(3) = 2 sqrt(3).

- A. 4 sqrt(3) is only sqrt(48); the other two radicals were not combined.
- B. sqrt(3) would need the terms to total 1 sqrt(3); the actual total is 4 + 3 - 5 = 2.
- C. 6 sqrt(3) comes from adding sqrt(48) and sqrt(27) and ignoring the subtraction of sqrt(75).
- D. (key) 2 sqrt(3)

- Trap: Write every radical as a multiple of the same square-free surd before combining.
- Shortcut and time target: Factor each radicand into a square times 3, then add the coefficients. Target 80 s.

**R3-Q35 — B.** Both statements alone give x = 5, so either suffices. I alone: unique value 5; II alone: unique value 5; together: unique value 5.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Two different statements can each fix the same value.
- Shortcut and time target: Compare the single values. Target 60 s.

**R3-Q36 — C.** 7 x 8 = 56 < 60 and 7 x 9 = 63 > 60, so P = 8. Since 8 < 9, P is less than Q.

- A. P is greater than Q: P is 8 and Q is 9, so the first is not larger.
- B. P is 8, not 9, so the two are not equal.
- C. (key) P is less than Q
- D. The strict bound fixes P at 8, so the relation is determined.

- Trap: Check the largest integer by multiplying the candidate, not by estimating the division.
- Shortcut and time target: Divide 60 by 7 (about 8.6) and take the integer part below the bound. Target 70 s.

**R3-Q37 — C.** Perfect squares above 10 up to 40 are 16, 25 and 36; the multiple-of-5 condition keeps only 25. I alone: not unique (8 values, e.g. 10, 15, 20, 25); II alone: not unique (3 values, e.g. 16, 25, 36); together: unique value 25.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Each statement alone leaves several values; the overlap is 25.
- Shortcut and time target: Restrict the list of squares first, then apply the divisibility condition. Target 85 s.

**R3-Q38 — C.** Multiples of 45 up to 200 are 45, 90, 135, 180; the second statement leaves 9 to 45. Only 45 is in both. I alone: not unique (4 values, e.g. 135, 180, 45, 90); II alone: not unique (5 values, e.g. 18, 27, 36, 45); together: unique value 45.

- A. Wrong: neither statement suffices alone, so 'exactly one' fails.
- B. Wrong: neither statement suffices alone.
- C. (key) Correct verdict: only the pair suffices.
- D. Wrong: the pair fixes a unique value.

- Trap: Both lists contain 45, but the first also contains 90, which the second excludes.
- Shortcut and time target: Find the overlap of the two lists rather than solving either list fully. Target 85 s.

**R3-Q39 — C.** Let the son be s, so the father is 60 - s. Then 60 - s - 5 = 9(s - 5), so 55 - s = 9s - 45, 10s = 100 and s = 10.

- A. 12 gives a father of 48; five years ago 43 is not 9 times 7 (63).
- B. 8 gives a father of 52; five years ago 47 is not 9 times 3 (27).
- C. (key) 10
- D. 15 gives a father of 45; five years ago 40 is not 9 times 10 (90).

- Trap: Shift both ages by the same five years before forming the ratio equation.
- Shortcut and time target: Write both ages five years ago, equate the ratio, then use the total to check. Target 90 s.

**R3-Q40 — D.** Since 0 < a < b, b/a is greater than 1, while each of the other three is less than 1.

- A. a/b is less than 1 for a < b, so it cannot be the greatest.
- B. (a+1)/(b+1) is less than 1 because a + 1 is at most b, which is less than b + 1.
- C. a/(b+1) is less than 1 for the same reason.
- D. (key) b/a

- Trap: Adding the same positive number to numerator and denominator moves a fraction towards 1; it does not change which side of 1 it lies on.
- Shortcut and time target: Test a = 2, b = 5: values 2.5, 0.4, 0.5 and 0.29 give the answer at once. Target 80 s.

**R3-Q41 — A.** An odd square has an odd root, so t is odd; the multiple-of-3 statement allows odd and even values. I alone: unique value yes; II alone: not unique (2 values, e.g. no, yes); together: unique value yes.

- A. (key) Correct verdict: exactly one statement suffices.
- B. Wrong: only one statement suffices alone; the other does not.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Odd multiples of 3 and even multiples of 3 both exist, so the second statement is silent.
- Shortcut and time target: A square's parity equals the root's; a multiple of 3 is not parity-determined. Target 70 s.

**R3-Q42 — B.** 4x <= 16 gives x <= 4; x + 3 > 2 gives x > -1. So x in {0, 1, 2, 3, 4}: five integers.

- A. 4 drops x = 0, reading x + 3 > 2 as x > 0.
- B. (key) 5
- C. 6 includes x = -1, reading x + 3 > 2 as x + 3 >= 2.
- D. 3 truncates the first bound at x = 2, misreading 4x <= 16 as x < 2.

- Trap: Each inequality gives one bound; list the integers between the strict and non-strict ends.
- Shortcut and time target: Solve both bounds, then count integers between them. Target 80 s.

**R3-Q43 — B.** 9^(x-1) = 3^(2x-2) = 3^3, so 2x - 2 = 3 and x = 5/2.

- A. 2 equates the exponent 2x - 2 with 2, mistaking 27 for 3 squared.
- B. (key) 5/2
- C. 3 equates x - 1 with 3, ignoring that 9 is 3 squared.
- D. 3/2 equates 2x with 3 and drops the -2 from the exponent.

- Trap: Write both sides as powers of the same base before equating exponents.
- Shortcut and time target: Express 9 and 27 as powers of 3, equate the exponents, and solve. Target 80 s.

**R3-Q44 — B.** An even square needs an even root; so the first statement is sufficient. The second statement says x + 1 is odd, so x is even. I alone: unique value yes; II alone: unique value yes; together: unique value yes.

- A. Wrong: both statements suffice alone, so 'exactly one' fails.
- B. (key) Correct verdict: each statement suffices alone.
- C. Wrong: a single statement already suffices, so 'neither alone' fails.
- D. Wrong: the pair fixes a unique value.

- Trap: Both statements determine parity, so either one suffices.
- Shortcut and time target: Parity of a square equals parity of its root; parity of x + 1 flips to give parity of x. Target 70 s.

**R3-Q45 — A.** The two-digit multiples of 7 with odd tens digits are 14, 35, 56, 70, 77, 91 and 98: seven values.

- A. (key) 7
- B. 6 omits 14, whose tens digit 1 is odd.
- C. 5 omits both 14 and 98.
- D. 8 counts 84, whose tens digit 8 is even, or 63, whose tens digit 6 is even.

- Trap: Check the tens digit of each multiple; it is easy to skip the first (14) or the last (98).
- Shortcut and time target: List the multiples of 7 from 14 to 98 and tick odd tens digits. Target 90 s.

**R3-Q46 — D.** 2n + 3 divisible by 3 means 2n divisible by 3, so n is divisible by 3.

- A. n + 1 is a multiple of 3 is not forced: n = 3 gives n + 1 = 4.
- B. n - 1 is a multiple of 3 is not forced: n = 3 gives n - 1 = 2.
- C. 2n + 1 is a multiple of 3 is not forced: n = 3 gives 7.
- D. (key) n is a multiple of 3

- Trap: Subtract the multiple of 3 (3 itself) and divide by 2, which is coprime to 3.
- Shortcut and time target: Reduce modulo 3: 2n ≡ 0 mod 3 forces n ≡ 0 mod 3. Target 75 s.

**R3-Q47 — A.** x^2 > 50 needs x >= 8 (since 7^2 = 49). With x <= 9, the integers are 8 and 9: two values.

- A. (key) 2
- B. 1 counts only 9 and forgets that 8 squared (64) also exceeds 50.
- C. 3 adds 7, whose square 49 falls just short of 50.
- D. 9 counts all integers from 1 to 9 and ignores the square condition.

- Trap: Near a threshold, check the integer just below the bound (49 here) before deciding.
- Shortcut and time target: Find the smallest integer whose square exceeds 50, then count up to 9. Target 75 s.

**R3-Q48 — C.** Copper = 3/5 + 1/5 = 4/5 of the mass of one unit each, and tin = 2/5 + 4/5 = 6/5. So the ratio is 4:6 = 2:3.

- A. 3:2 is the ratio of alloy X alone; the mixture includes Y, which changes it.
- B. 1:1 assumes the two alloys balance each other, which the masses do not show.
- C. (key) 2:3
- D. 7:3 inverts Y's ratio, giving Y four parts of copper and one part of tin.

- Trap: Compute the copper and tin shares of each alloy separately, then add the shares; ratios are not added directly.
- Shortcut and time target: Use shares of each alloy (3/5 and 2/5 for X; 1/5 and 4/5 for Y) and add. Target 110 s.

**R3-Q49 — D.** Let Meena's age be m, so Ravi's is m + 4. Then m + (m + 4) = 28, so 2m = 24 and m = 12. The stem alone fixes the age; neither statement is needed.

- A. Wrong: the sum and difference already fix the age. Statement I (Ravi over 15) is true of 12 but is not needed, so "exactly one suffices" misreads the item.
- B. Wrong: no statement is needed, so "each suffices alone" does not apply.
- C. Wrong: the pair is not needed; the stem fixes m = 12.
- D. (key) The question can be answered without any statement.

- Trap: Treating 28 as Ravi's age, which gives Meena 24. The two ages sum to 28, so both must be expressed in terms of m.
- Shortcut and time target: Use 2m + 4 = 28. Target 70 s.

**R3-Q50 — A.** A positive whole number whose square is 144 is 12, since the negative root -12 is excluded. Statement I alone gives 12. Statement II alone leaves 4, 8, 12 and 16 (multiples of 4 below 20), so it is not decisive. The stem alone does not fix the count.

- A. (key) Exactly one suffices: Statement I alone gives 12; Statement II alone does not.
- B. Wrong: Statement II alone leaves four candidates.
- C. Wrong: Statement I alone already suffices, so the pair is not needed.
- D. Wrong: without a statement the number of pens is not fixed; Statement I fixes it, so the item is not self-sufficient.

- Trap: Taking -12 as a possible count because a square has two roots. The count is a positive whole number, so only 12 is admissible.
- Shortcut and time target: Take the positive square root of 144. Target 70 s.

**R3-Q51 — D.** The length is 2w, so the perimeter is 2(2w + w) = 6w = 36. Then w = 6 and the length is 12, so the area is 12 x 6 = 72 cm^2. The stem alone fixes the area; neither statement is needed.

- A. Wrong: the perimeter and length condition already fixes the area; Statement I is true of width 6 but is not needed, so "exactly one suffices" misreads the item.
- B. Wrong: no statement is needed.
- C. Wrong: the pair is not needed; the stem alone gives 72.
- D. (key) The question can be answered without any statement.

- Trap: Computing the area as (2w)(2w) = 144 by doubling the width in both factors. The area is length times width, and the width is 6.
- Shortcut and time target: From 6w = 36, w = 6 and the area is 2w^2 = 72. Target 75 s.

**R3-Q52 — A.** Three distinct primes with sum 20 must include 2, since three odd primes sum to an odd number. Then b + c = 18 with 2 < b < c. The possibilities are (5, 13) and (7, 11), so the question alone leaves c = 11 or 13. Statement I (b = 7) gives a + c = 13, so a = 2 and c = 11. Statement II (a = 2) leaves b = 5 or 7, so c is still 13 or 11.

- A. (key) Exactly one suffices: Statement I alone gives c = 11; Statement II alone does not.
- B. Wrong: Statement II alone leaves c = 11 or 13, so it does not decide the answer.
- C. Wrong: Statement I alone already decides c, so the pair is not needed.
- D. Wrong: the pair is consistent with (2, 7, 11), so both statements together do decide c = 11.

- Trap: Forgetting that the sum of three odd primes is odd. Without the parity argument, a solver may miss a = 2 altogether.
- Shortcut and time target: Parity forces a = 2; then the remaining sum is 18 and the candidate pairs are short to list. Target 85 s.

**R3-Q53 — C.** Statement I: with no students left over in rows of 7, the number is a multiple of 7 in the range 40 to 60, so it is 42, 49 or 56. Statement II: a remainder of exactly 2 on division by 8 gives 42, 50 or 58. Each statement alone leaves three candidates. Together only 42 fits both.

- A. Wrong: each statement alone leaves three candidates, so neither decides the number.
- B. Wrong: Statement II alone leaves 42, 50 and 58, so "each suffices" fails.
- C. (key) Both together are sufficient: 42 is the only common value.
- D. Wrong: the pair gives 42, so the number is determined.

- Trap: Reading "exactly 2 are left over" as "at least 2". The exact remainder removes 49 and 56 from the Statement II list.
- Shortcut and time target: List the multiples of 7 in range, then test the remainder 2 on division by 8; only 42 passes. Target 80 s.

**R3-Q54 — B.** x ★ 2 = x^2 - 6 and 2 ★ x = 4 - 3x. The inequality is x^2 + 3x - 10 >= 0, which factorises as (x + 5)(x - 2) >= 0, so x <= -5 or x >= 2. Within -4 to 4 the values are x = 2, 3 and 4: three integers.

- A. 2 counts only the strict inequality (x = 3 and 4). At x = 2 both sides equal -2, so the non-strict inequality holds.
- B. (key) 3. The integers 2, 3 and 4 satisfy the inequality.
- C. 4 counts x = -5, which is outside the stated range -4 to 4.
- D. 5 counts every integer from 0 to 4, which would follow from a sign error that drops the lower root.

- Trap: Swapping the roles in 2 ★ x. It equals 2^2 - 3x, not x^2 - 3 times 2.
- Shortcut and time target: Test x = 2 (equality holds), x = 1 (fails) and x = 4 (holds) to see the pattern. Target 100 s.

**R3-Q55 — A.** Statement I: x ∆ 3 = x + 6 and 2 ∆ x = 2 + 2x, so x + 6 = 2 + 2x and x = 4. Statement II: x ∆ 1 = x + 2 > 5 gives x > 3, which leaves 4 to 10 (seven values). So only Statement I fixes x.

- A. (key) Exactly one suffices: Statement I alone gives x = 4; Statement II alone does not.
- B. Wrong: Statement II alone leaves seven candidates, so "each suffices" fails.
- C. Wrong: Statement I alone already suffices, so the pair is not needed.
- D. Wrong: Statement I alone gives x = 4, so the value is determined.

- Trap: Swapping the operands of the first clause, which would give x ∆ 3 = 3 + 2x and x = 1. The first operand is always the number on the left.
- Shortcut and time target: Set both expressions equal and solve the linear equation. Target 80 s.

**R3-Q56 — C.** Statement I: the number of eggs is a multiple of 8, so it lies in 104, 112, ..., 200. Statement II: a multiple of 15, so it lies in 105, 120, ..., 195. Each leaves several candidates. Together, the number is a multiple of lcm(8, 15) = 120, and within 100 to 200 only 120 fits.

- A. Wrong: each statement alone leaves several candidates in the range.
- B. Wrong: Statement II alone leaves seven candidates, so it is not decisive.
- C. (key) Both together are sufficient: 120 is the only common multiple in the range.
- D. Wrong: the pair determines the number as 120.

- Trap: Treating a single multiple as sufficient because 120 is a multiple of 8 and of 15. Each statement is necessary; the pair is sufficient.
- Shortcut and time target: Use lcm(8, 15) = 120; the next multiple, 240, is out of range. Target 70 s.
