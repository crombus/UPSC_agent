# Number Systems and Number Sense - Learning Session Live Edition

**Paper:** CSAT (Civil Services Preliminary Examination, Paper II) | **Format:** 80 objective items, 200 marks, two hours | **Scoring:** equal marks for each item (200 / 80 = 2.5 marks), with a penalty for each wrong answer | **Qualifying bar:** 33 per cent of Paper II, which is 66 of 200 marks (the repository's Master Framework states this minimum; recheck the current examination notification before relying on it)

This session teaches the number-property skill that decides a large share of CSAT arithmetic items. It does not ask you to memorise long tables. Every lesson asks one question first: does this item want the exact value, or only a property such as a divisor, a remainder, a last digit, a factor count, a digit total or a size? Then it teaches the method that answers that property without forming the large number.

The syllabus clause is "Basic numeracy (numbers and their relations, orders of magnitude, etc.) (Class X level)". Divisibility, primes and factors, HCF and LCM, remainders and cycles, digits and digit constraints, number sequences and integer combinations are taught in Lessons 1 to 6 and 9. Large powers, factorial valuations and trailing zeros are taught in Lesson 7. Orders of magnitude, powers of ten, scientific notation, bounding, estimation, roots, surds and decimal place value are taught in full in Lesson 8. Letter, shape and coding series are not taught here. Lessons 5 and 6 teach the number-property parts of digit puzzles and numeric sequences only; the full puzzle mechanisms of letter, code and general series questions lie outside this session.

Practice is multiple-choice. Each lesson ends with two to four original items, set out so that you can attempt them before reading any explanation. The items and worked examples in this session are original: none reproduces a past-paper stem, option, number pattern or answer. Past questions are linked, not solved, in the linkage section.

## Roadmap

| # | Subtopic | Stage | Depends on | Lesson MCQs |
|---|---|---|---|---|
| 1 | Divisibility, digit tests and digit-based eliminations | Foundation | none | 3 (MCQ 1-3) |
| 2 | Primes, factor counts, factor sums, difference of squares and consecutive integers | Core | 1 | 4 (MCQ 4-7) |
| 3 | HCF, LCM, same-remainder and multiple counts, including one Advanced part on numbers divisible by neither | Core, with one Advanced part | 2 | 3 (MCQ 8-10) |
| 4 | Remainders, unit-digit cycles, composite moduli and repunits | Core | 2, 3 | 2 (MCQ 11-12) |
| 5 | Digits, place value, reversal, digit sums, permutations and digit constraints | Core | 1, 4 | 4 (MCQ 13-16) |
| 6 | Sequences, patterns, periodic sums, matrices and derived operators | Core | 4, 5 | 3 (MCQ 17-19) |
| 7 | Large powers, the coprimality gate, factorial and product valuations | Core and Advanced | 2, 4 | 4 (MCQ 20-23) |
| 8 | Magnitude, powers of ten, scientific notation, bounding, recurring decimals, roots and surds | Core | 2, 7 | 3 (MCQ 24-26) |
| 9 | Integer combinations, minimum counts and extremes | Core | 3, 6, 8 | 2 (MCQ 27-28) |

Cumulative items: 6 (MCQ 29-34), in the CUMULATIVE MCQS section after the linkage section. Each combines two or more lessons.

```text
  L1 Divisibility --> L2 Primes, factors, sums --> L3 HCF, LCM, multiples
                                                        |
                                                        v
  L5 Digits, reversal <-- L4 Remainders, cycles, repunits
        |
        v
  L6 Sequences, periodic sums, matrices --> L7 Large powers, valuations, gate
                                                        |
                                                        v
  L9 Combinations, extremes  <-- L8 Magnitude, roots, recurring decimals
```

The lessons are sequenced by dependency, as the roadmap shows. The visuals differ from lesson to lesson, because the shape of each concept decides the shape of its picture.

## Lesson 1 - Divisibility, and the tests that replace division

Progress: 1/9 | Stage: Foundation | Subtopic: Divisibility, digit tests and digit-based eliminations

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the question decides the tool

```text
  A NUMBER ITEM ASKS FOR ...

     the VALUE ----------------------------> compute (only when nothing else works)
        |
     a PROPERTY of its shape
        |
        +-- "divisible by d?" ----------> apply the test for d (last digits, digit sum, alternating sum)
        +-- "remainder on division?" ---> the remainder method, reducing first
        +-- "how many divisors?" -------> factorise first, then count

  Test table (base 10)
  divisor   test on the digits                            fails when
  2, 5, 10  last digit even / 0 or 5 / 0                   never; these read one digit only
  4, 8      last 2 digits divisible by 4; last 3 by 8      the number is shorter than the block
  3, 9      digit sum divisible by 3; by 9                 any base other than 10
  6         divisible by 2 AND by 3 (2 and 3 coprime)      the two halves share a factor (2 and 6 fail for 12)
  12        divisible by 3 AND by 4                        as for 6
  11        |(sum of odd places) - (sum of even places)| is 0 or 11k
  7         remove last digit d; subtract 2d from the rest; repeat
```

### The idea in plain words

Divisibility is about the shape of a number, not its size. A very large number can be a multiple of 9 while looking ordinary, and the last digit or the digit total often gives the shape away at once. Each test is a short calculation that answers "is there a remainder?" without carrying out the division. The skill is choosing the test that matches the divisor in the question.

### Number classes, in the order the exam uses them

Start with the classes. Each class contains the ones before it. Natural numbers are 1, 2, 3 and so on. Whole numbers add zero. Integers add the negatives. Rational numbers are fractions p/q with q not zero, which include every terminating and every recurring decimal. Irrational numbers, such as the square root of 2 or pi, neither terminate nor recur. Real numbers are the rational and irrational numbers together.

Three traps recur in questions. Zero is a whole number but not a natural number. The square root of 4 is 2, which is rational even though a root sign is written. Minus 2 is an integer but not a natural number. A stem that asks for "natural numbers" excludes zero and negatives, while one that asks for "integers" includes them.

### Divisibility as a relation

"a divides b" means that b = a x k for some integer k. It is a claim about an ordered pair, so the reverse claim, "b divides a", is a different claim. For positive integers, a divides b and b divides a both hold only when a = b. Two numbers such as 2 and 3 satisfy neither claim.

Implication and equivalence must be kept apart. "If 12 divides n, then 6 divides n" is true, because 12 = 6 x 2. Its converse, "if 6 divides n, then 12 divides n", is false: n = 6 is divisible by 6 but not by 12. The equivalence "6 divides n if and only if 2 divides n and 3 divides n" holds, because 2 and 3 are coprime (they share no factor other than 1). The same pattern fails for 12 when the two halves are not coprime: "2 divides n and 6 divides n" does not give "12 divides n", and n = 6 is the counterexample.

### The tests, with their conditions

**Divisors 2, 5 and 10.** Read the last digit. An even last digit gives divisibility by 2, a last digit of 0 or 5 gives 5, and a last digit of 0 gives 10. These tests read one digit, so they need no addition.

**Divisors 4 and 8.** Read the last two digits for 4 and the last three for 8. The test works because 100 and 1,000 are multiples of 4 and 8, so only the last two or three digits decide the remainder. For a number with fewer digits than the block, the test simply reads the whole number, so it adds nothing.

**Divisors 3 and 9.** A number is divisible by 3 when its digit sum is divisible by 3, and by 9 when the digit sum is divisible by 9. The rule depends on base 10, because the test uses 10 = 9 + 1 and 10 leaves remainder 1 on division by 9. In general a digit sum leaves the same remainder on division by 9 as the number itself, which is why the 9-test works. In base 8, the numeral 17 means 15, and its digit sum 8 is not divisible by 3 even though 15 is.

**Divisors 6 and 12.** Divisibility by 6 is divisibility by 2 and by 3, and divisibility by 12 is divisibility by 3 and by 4. Both work only because the two halves are coprime.

**Divisor 11.** Take the sum of the digits in odd places, counting from the right, and subtract the sum of the digits in even places. The number is divisible by 11 when this difference is 0 or a multiple of 11. The difference can be negative, so judge its value, not its sign. A two-digit number such as 77 gives 7 - 7 = 0.

**Divisor 7.** Remove the last digit d, subtract twice d from what remains, and repeat on the result. The original number is divisible by 7 exactly when the final number is. The doubling is the test, not a refinement. Subtracting d once gives a different and wrong test.

**Repeated blocks.** A two-digit block written three times, such as 141,414 (the block 14 written as 14, 14, 14), equals the block times 10,101 = 1 + 100 + 10,000, and 10,101 = 3 x 7 x 13 x 37. So any number formed by writing a two-digit block three times is divisible by 3, 7, 13 and 37, and by the block itself.

### Worked check: the 3-test against the 9-test

Is 3,702 divisible by 9? Its digit sum is 3 + 7 + 0 + 2 = 12. Twelve is divisible by 3 but not by 9, so 3,702 is divisible by 3 and not by 9. A check: 3,702 divided by 3 gives 1,234, and 3,702 divided by 9 leaves remainder 3.

### Worked check: the 11-test with a negative difference

Is 2,728 divisible by 11? The odd places from the right hold 8 and 7, a sum of 15. The even places hold 2 and 2, a sum of 4. The difference is 4 - 15 = -11, a multiple of 11, so the number is divisible by 11. Check: 2,728 divided by 11 is 248.

### Worked check: the 7-test

Is 3,941 divisible by 7? Remove the last digit 1, giving 394, and subtract 2 x 1, giving 392. Repeat: remove 2 from 392, giving 39, and subtract 2 x 2, giving 35. Thirty-five is 7 x 5, so 3,941 is divisible by 7. Check: 3,941 = 7 x 563.

### Parity and digit sums as eliminators

Parity answers one question: is the number even or odd? Even times anything is even. Odd times odd is odd. Even plus odd is odd. Parity removes options only when the stem fixes the parity of the whole expression. When the expression includes an unknown whose parity is not fixed, no option can be removed by parity alone.

A digit sum can eliminate a whole family at once. The digits 2, 4 and 9 sum to 15, which is a multiple of 3. Every arrangement of those three digits therefore has digit sum 15 and is divisible by 3, so none of the three-digit numbers they form can be prime. One test removes all of them.

### Missing digits and when a test gives a unique answer

When a digit x is unknown and the test is divisibility by 9, the digit sum must be a multiple of 9. The digit x is unique when the other digits leave a non-zero remainder on division by 9, because exactly one digit from 1 to 9 then works. When the other digits leave remainder 0, digits 0 and 9 both work. For example, 4x5 is divisible by 9 when 9 + x is a multiple of 9, so x = 0 and x = 9 both pass (405 and 495). The 3-test alone gives several candidates in every case, so a stem with a unique answer needs the 9-test or a second condition.

For a missing digit with the 7-test, the rule is applied to each candidate digit in turn, because the 7-test gives no direct formula for the missing digit. Count every candidate that passes; do not stop at the first one.

### A trap: the 3-test is not the 9-test

The tempting method is "the number is divisible by 3, so it is divisible by 9". Reply with the digit sum. Take 1,236: its digit sum is 12, so it is divisible by 3 but not by 9. The 3-test says nothing about 9 except through its own digit sum, so the stronger test has to be run separately.

### What the examiner asks

Divisibility items in Prelims ask for the missing digit that makes a number divisible, for the count of digits that satisfy a test, for a number that is divisible by one of several divisors, and for an implication about all numbers of a given form. The fastest route is the test for the property asked, followed by a check with one concrete number. For an implication, one counterexample is enough to reject a claim, and one example is never enough to accept it.

### Keep in mind

- Divisibility is a relation: a divides b means b = a x k, and it is not symmetric.
- For positive integers, a divides b and b divides a both hold only when a = b.
- Tests for 2, 4, 5, 8 and 10 read the last one, two or three digits.
- The 3- and 9-tests use the digit sum and work only in base 10.
- Divisibility by 6 needs 2 and 3; by 12 needs 3 and 4; the halves must be coprime.
- The 11-test uses an alternating difference that may be negative; judge its value.
- The 7-test removes the last digit, subtracts twice it, and repeats.
- A two-digit block written three times is the block times 10,101 = 3 x 7 x 13 x 37.
- A missing digit is unique by the 9-test only when the needed remainder is non-zero.
- Parity removes options only when the stem fixes the parity.

### Check yourself

1. Which two divisibility tests together give the test for 12, and why does the pair 2 and 6 fail? *Answer: 3 and 4 give 12; 2 and 6 share the factor 2, so n = 6 passes both tests and is not divisible by 12.*
2. What is the digit sum of 1,458, and what does it tell you about 3 and 9? *Answer: 18, so divisible by 9 and therefore by 3.*
3. Apply the 7-test to 2,093. *Answer: 209 - 6 = 203, then 20 - 6 = 14, a multiple of 7, so 2,093 is divisible by 7.*
4. Why does 4x5 not have a unique digit x that makes it divisible by 9? *Answer: the required sum 9 + x is a multiple of 9 for x = 0 and x = 9.*

### Next step

A test tells you whether a number is divisible by d, but a question that asks how many divisors a number has needs more than a yes-or-no answer. To count the divisors you must know which primes build the number and how many times each one appears. That is the next lesson.

### Practice

Attempt each item before reading its answer block.

**MCQ 1**

Which number is divisible by 3 but not by 9?

- A. 2,166
- B. 882
- C. 207
- D. 2,173

**MCQ 1 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** the digit sum is 15, a multiple of 3 but not of 9, so 2,166 passes the 3-test and fails the 9-test.
- **B — Incorrect:** 882 has digit sum 18, so it is divisible by 9 as well; choosing it drops the 'not by 9' condition.
- **C — Incorrect:** 207 has digit sum 9, so it is divisible by 9; reading a digit sum of 9 as 'not by 9' inverts the test.
- **D — Incorrect:** 2,173 has digit sum 13, so it fails even the 3-test; the named error is adding the digits as 12 and passing it.

**MCQ 2**

Which of these numbers is divisible by 11?

- A. 1,019
- B. 528
- C. 137
- D. 1,409

**MCQ 2 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 1,019 has odd-place sum 9 and even-place sum 2; adding them gives 11, which is the error of adding where the test subtracts, and the difference 7 is not a multiple of 11.
- **B — Correct:** odd places from the right give 8 + 5 = 13 and the even place gives 2; the difference is 11, so 528 = 11 x 48.
- **C — Incorrect:** 137 has digit sum 11, which is a digit-sum value and not the 11-test; 137 leaves remainder 5 on division by 11.
- **D — Incorrect:** 1,409 has odd-place sum 13 and even-place sum 1, a difference of 12; that is one away from a multiple of 11, so the error is a slip in the final subtraction.

**MCQ 3**

Which of these numbers is divisible by 7?

- A. 103
- B. 104
- C. 5,236
- D. 109

**MCQ 3 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 103 passes a version of the 7-test that subtracts the last digit once (10 - 3 = 7); the correct test subtracts twice it (10 - 6 = 4), so 103 is not a multiple of 7.
- **B — Incorrect:** 104 has digit sum 5, which says nothing about divisibility by 7; the error is treating a digit sum as a 7-test.
- **C — Correct:** remove the last digit 6 and subtract twice it: 523 - 12 = 511; repeat: 51 - 2 = 49 = 7 x 7.
- **D — Incorrect:** 109 passes a version that adds twice the last digit (10 + 18 = 28 = 7 x 4), but the correct test subtracts, and 109 leaves remainder 4 on division by 7.

## Lesson 2 - Primes, factors, factor sums and consecutive integers

Progress: 2/9 | Stage: Core | Subtopic: Primes, factor counts, factor sums, difference of squares and consecutive integers

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the factor pair ladder for 40

```text
  The divisors of 40 come in pairs (d, 40/d):

     d     1    2    4    5
     40/d 40   20   10    8        four pairs; each pair is one way to write 40 = d x e

  Difference of squares, a^2 - b^2 = (a - b)(a + b):
     write 40 = d x e with d < e
     a - b = d,  a + b = e   so a = (d + e)/2,  b = (e - d)/2
     both a and b are whole numbers only when d and e have the same parity:
       (1, 40) odd/even  x     (2, 20) even/even  yes -> (11, 9)
       (4, 10) even/even yes -> (7, 3)                  (5, 8)  odd/even  x
```

### Why factorise first

A prime is a number that cannot be built by multiplying two smaller whole numbers greater than 1. Every whole number greater than 1 is either prime or a product of primes in exactly one way, apart from order. That uniqueness is why a factor count is a counting problem: a number's prime pattern decides how many smaller numbers can be built from it. The first step in any factor question is therefore the prime factorisation.

### Primes, and how to test one

The primes up to 100 are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 and 97. There are twenty-five of them. The number 1 is not prime, and 2 is the only even prime.

To test a number n for primality, divide it by the primes up to its square root. If none divides it, n is prime. For example, 91 has square root about 9.5, and 7 divides it because 91 = 7 x 13, so 91 is not prime. The number 97 has square root about 9.8, and no prime from 2 to 7 divides it, so 97 is prime.

Primes give parity information. Two odd primes add to an even number, so a sum of three odd primes is odd. A sum that includes the prime 2 changes that parity.

### Factor count from the exponents

Write n as a product of distinct prime powers, n = p^a x q^b x r^c. The number of positive factors is (a + 1)(b + 1)(c + 1). The formula counts 1 and n, and it fails if the factorisation is incomplete or if one prime is repeated across the factors.

Take 360 = 2^3 x 3^2 x 5. The count is (3 + 1)(2 + 1)(1 + 1) = 4 x 3 x 2 = 24. A common error is to multiply the exponents themselves, giving 3 x 2 x 1 = 6, which counts the exponents rather than their choices. Each prime contributes exponent + 1 choices, namely 0, 1, ..., exponent.

### Odd factor counts and perfect squares

A positive integer has an odd number of factors exactly when it is a perfect square. Factors pair up as d and n/d, and an odd count needs a middle factor that pairs with itself, which happens only when d = n/d, that is, when n is a square. Thirty-six has nine factors (1, 2, 3, 4, 6, 9, 12, 18, 36), an odd count. Forty has eight, an even count, because 40 is not a square.

### Factor sums

The sum of all positive divisors of n is written sigma(n). It is multiplicative over prime powers: sigma(p^a) = 1 + p + ... + p^a, and sigma(n) is the product of these over the primes of n. For 12 = 2^2 x 3: sigma(12) = (1 + 2 + 4)(1 + 3) = 7 x 4 = 28. Check: the divisors 1, 2, 3, 4, 6 and 12 add to 28.

The product is essential. The two brackets 7 and 4 must be multiplied, because each divisor takes one term from each bracket. Adding the brackets gives 11, which is not a sum of divisors.

### Difference of squares

a^2 - b^2 = (a - b)(a + b). For a and b to be natural numbers with a greater than b, write the target N = d x e with d < e. Then a - b = d and a + b = e, so a = (d + e)/2 and b = (e - d)/2. Both are whole numbers only when d and e have the same parity.

Two consequences follow. Every odd N greater than 1 has the pair (1, N), which gives a = (N + 1)/2 and b = (N - 1)/2. For N = 15 this is (8, 7), and the pair (3, 5) gives a second representation, (4, 1). A number of the form 4k + 2 is never a difference of two squares, because its factorisation always contains exactly one factor of 2. For 40, the pairs (2, 20) and (4, 10) both have even partners, giving (11, 9) and (7, 3). The pairs (1, 40) and (5, 8) mix parities and give nothing.

### Consecutive integers and triangular numbers

The sum of k consecutive integers starting at a is k x a + k(k - 1)/2. Equivalently it is k times the mean. The mean of an odd number of consecutive integers is the middle term, so the sum of k consecutive integers with k odd is divisible by k. Five consecutive integers always sum to a multiple of 5, because the sum is 5 times the middle term.

For an even number of consecutive integers the mean is a half-integer, so the sum is a multiple of k/2 but not of k. Four consecutive integers such as 3, 4, 5, 6 sum to 18, which is not a multiple of 4.

The sum of the first n natural numbers is the triangular number n(n + 1)/2. The triangular numbers are 1, 3, 6, 10, 15, 21, 28, 36 and so on. Each triangular number is reached from the one before it by adding the next whole number, so the increments are 2, 3, 4 and so on.

Some stems place marks at distances from one end of a segment that are triangular numbers. The method is the same as for any list of positions. Write the first few distances, check the increments, and count the distances that fall inside the segment, measured from the stated end. The count of marks below a limit is therefore the count of triangular numbers below that limit. List a few distances before you count, so that the rule is checked on real positions.

**Torn leaf.** Pages 1 to n are printed, and a leaf carrying the consecutive pages p and p + 1 is torn out. Let S_n = n(n + 1)/2 be the sum of the pages 1 to n, and let R be the sum of the pages that remain. The removed pair sums to S_n - R, and this equals 2p + 1, which is always odd. Worked example: R = 1,000. For n = 45, S_45 = 1,035, so 2p + 1 = 35 and p = 17: the leaf is pages 17 and 18. The stem must fix n, because for n = 46 the same R gives S_46 = 1,081, so 2p + 1 = 81 and p = 40 is also a possible leaf. Check: 1,035 - 35 = 1,000.

### Odd and even consecutive integers

Consecutive odd integers, such as 5, 7, 9 and so on, differ by 2. Their mean is the middle term, and their sum is the number of terms times that middle term. The same method applies: the odd integers from 5 to 25 are eleven numbers, the sixth of them is 15, and their sum is 11 x 15 = 165.

### Unit-fraction solutions

To count the ways to write 1/4 as a sum of two unit fractions 1/p + 1/q with p <= q, use the bound on the smaller variable. Since 2/p is at least 1/4, p is at most 8; since 1/p is less than 1/4 when q is finite, p is greater than 4. Testing p = 5, 6, 7 and 8 gives 1/q = 1/20, 1/12, 3/28 and 1/8. The value 3/28 is not a unit fraction, so the solutions are (5, 20), (6, 12) and (8, 8). The bound on the smaller variable is what makes the list finite and complete.

### Primes in progressions and prime expressions

When a stem links primes by a fixed gap, write the relation as a progression and check parity first. Among odd primes the common difference must be even, because two odd primes differ by an even number. The prime 2 can enter only at one end, and only when the progression is short enough. Then list the candidates below the stated bound and check each one.

For a quadratic form such as n squared plus a constant, check parity first: an odd square plus an odd constant is even, so the form can be prime only when it equals 2 or when the square term is even. Parity alone often removes most candidates.

### A trap: calling 1 prime

The tempting method is to call 1 a prime, or to test primality by checking only 2, 3 and 5. Reply with 91. It has no factor 2, 3 or 5, and a test that stopped there would call it prime. Its factor 7 appears only when the test runs to the square root. A prime test must run to the square root, not to the last small prime that the candidate happens to pass.

### Exam signals

Factor-count items ask for the number of divisors, for the odd-count property, or for a statement about factor counts that holds for all numbers of a form. Factor-sum items use sigma with the multiplicative formula. Difference-of-squares items ask how many pairs satisfy a fixed difference. Consecutive-integer items ask for the sum, the mean or whether a sum is possible at all. Prime items ask whether a statement holds, which requires one counterexample or a parity argument.

### Summary of rules

- A prime has exactly two positive divisors; 1 is not prime; 2 is the only even prime.
- A primality test runs to the square root, not to the last small prime.
- Factor count is the product of (exponent + 1) over the distinct primes.
- An odd factor count means a perfect square, for positive integers.
- Factor sum is multiplicative: sigma(p^a) = 1 + p + ... + p^a, and sigma(n) is the product.
- a^2 - b^2 = (a - b)(a + b); the pair (d, e) works only when d and e share parity.
- The sum of k consecutive integers is k times the mean; odd k gives a multiple of k.
- The sum of the first n integers is n(n + 1)/2, the triangular numbers.
- Unit-fraction counts start from the bound p <= 3 for 1/p + 1/q + 1/r = 1.
- For p^2 + k, parity removes most candidates before any list is written.

### Quick checks

1. How many positive factors does 2^5 x 7 have? *Answer: (5 + 1)(1 + 1) = 12.*
2. Is 1,000 a difference of two squares? *Answer: yes. Take 1,000 = 4 x 250; both are even, so a = 127 and b = 123, and 127^2 - 123^2 = 1,000.*
3. What is the sum of 5 consecutive integers whose middle term is 11? *Answer: 5 x 11 = 55.*
4. How many pairs of unit fractions 1/p + 1/q with p <= q equal 1/4? *Answer: three pairs, (5, 20), (6, 12) and (8, 8).*

### Bridge to counting

Once a number is written as a product of primes, its factors and sums are counted without listing them. But a common question asks about two numbers at once: the largest piece that fits both, or the first moment they coincide. Those questions need the exponents of two factorisations compared prime by prime, which is the next lesson.

### Practice

Attempt each item before reading its answer block.

**MCQ 4**

How many positive factors does 900 have?

- A. 8
- B. 9
- C. 18
- D. 27

**MCQ 4 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 8 is 2 x 2 x 2, the product of the exponents themselves rather than of the exponents plus one; the error is omitting the +1.
- **B — Incorrect:** 9 is (2 + 1)(2 + 1), which drops the prime 5 altogether; the error is a missing prime factor.
- **C — Incorrect:** 18 is (2 + 1)(2 + 1)(1 + 1), which reads the exponent of 5 as 1 instead of 2; the error is a factorisation slip.
- **D — Correct:** 900 = 2^2 x 3^2 x 5^2, so the count is (2 + 1)(2 + 1)(2 + 1) = 27.

**MCQ 5**

What is the sum of all positive divisors of 20?

- A. 42
- B. 7
- C. 22
- D. 40

**MCQ 5 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** 20 = 2^2 x 5, so the sum is (1 + 2 + 4)(1 + 5) = 7 x 6 = 42, the same as adding 1, 2, 4, 5, 10 and 20.
- **B — Incorrect:** 7 is the bracket 1 + 2 + 4 alone; the error is dropping the bracket that carries the factor 5.
- **C — Incorrect:** 22 is the sum of the proper divisors, which leaves out 20 itself; the error is dropping the number from its own divisor list.
- **D — Incorrect:** 40 is twice 20; the error is assuming that the divisor sum always doubles the number.

**MCQ 6**

A square lawn of side a metres has an inner square of side b metres, with a greater than b, and the lawn's area minus the inner square's area is 360 square metres. What is the largest possible value of b, a whole number?

- A. 91
- B. 89
- C. 43
- D. 1

**MCQ 6 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 91 is the outer side a of the first pair (91, 89), not the inner side b; the error is reporting the outer side.
- **B — Correct:** a - b and a + b must share parity, so the factor pairs of 360 with both factors even give (a, b) = (91, 89), (47, 43), (33, 27), (23, 13), (21, 9) and (19, 1); the largest b is 89.
- **C — Incorrect:** 43 is the inner side of the second pair (47, 43); the error is skipping the first and largest factor pair.
- **D — Incorrect:** 1 is the inner side of the last pair (19, 1); the error is reporting the smallest b rather than the largest.

**MCQ 7**

Which of the following is a prime number?

- A. 77
- B. 57
- C. 89
- D. 119

**MCQ 7 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 77 = 7 x 11; its last digit is 7, so a check that looks only at the last digit lets it through.
- **B — Incorrect:** 57 = 3 x 19 has digit sum 12, so the 3-test rejects it; the error is ignoring the 3-test.
- **C — Correct:** 89 has no prime divisor up to its square root (about 9.4): 2, 3, 5 and 7 all fail.
- **D — Incorrect:** 119 = 7 x 17 passes the tests for 2, 3 and 5 and then stops; the trial must run to 7, because the square root of 119 is about 10.9.

## Lesson 3 - HCF, LCM, common multiples and counts of coincidence

Progress: 3/9 | Stage: Core, with one Advanced part (the complement count, labelled in the lesson) | Subtopic: HCF, LCM, same-remainder and multiple counts

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the prime-exponent table

```text
  A = 24 = 2^3 x 3^1          B = 90 = 2^1 x 3^2 x 5^1

  prime   exponent in A   exponent in B   HCF takes   LCM takes
  2            3               1            min = 1     max = 3
  3            1               2            min = 1     max = 2
  5            0               1            min = 0     max = 1

  HCF = 2^1 x 3^1 x 5^0 = 6          LCM = 2^3 x 3^2 x 5^1 = 360
  HCF x LCM = 2,160 = 24 x 90 (two numbers only)
```

### The question decides the operation

The HCF is the largest piece that fits exactly into every number. The LCM is the smallest length that every number fits into exactly. Most mistakes in this family come from swapping the two. "The greatest length that measures both" is an HCF question. "The first time both bells ring together" is an LCM question. The words "greatest" and "least" decide the operation before any arithmetic starts.

### Doctrine: HCF takes the smaller exponent, LCM the larger

For each prime, the HCF uses the smaller of the two exponents and the LCM uses the larger one. A prime missing from one number has exponent 0 in that number, so it contributes nothing to the HCF and its full power to the LCM. Once both numbers are factorised, both results are mechanical.

### Doctrine: the product identity, for two numbers only

For two positive numbers A and B, HCF x LCM = A x B. The identity holds only for two numbers. For three numbers, take 2, 3 and 4: their HCF is 1 and their LCM is 12, so the product of the HCF and the LCM is 12, while 2 x 3 x 4 = 24. Use the prime-exponent table for three or more numbers.

The identity gives a fast route to a missing number. If the HCF is 6, the LCM is 180, and one number is 36, the other is (6 x 180)/36 = 30. Check: HCF(36, 30) = 6 and LCM(36, 30) = 180.

### Doctrine: the LCM as a count of coincidences

If two events repeat every a and every b units, they coincide every lcm(a, b) units. Over N units, the number of coincidences that fall inside the range 1 to N is floor(N / lcm(a, b)). Three or more events work the same way with the LCM of all their periods. Read whether the stem counts the first coincidence (a "time" question) or every coincidence in a range (a "how many times" question). For "how many times do three events with periods 5, 6 and 8 days coincide within 250 days", the lcm is 120 and the count is floor(250 / 120) = 2.

### Doctrine: same remainder, and the HCF of differences

If several numbers leave the same remainder r on division by one divisor d, then d divides every pairwise difference, and the greatest such d is the HCF of the differences. The remainder must be smaller than d, because a remainder is always less than its divisor.

For 62, 137 and 237, the differences are 75, 100 and 175. Their HCF is 25. Each number leaves remainder 12 on division by 25, and 12 is less than 25. If the remainders are not equal, first subtract each remainder from its number and then take the HCF.

### Doctrine: the least number with a given remainder

If a number leaves remainder r on division by each of m1, m2, ..., then the numbers with that property are r + k x lcm(m1, m2, ...) for whole numbers k, provided r is smaller than every divisor. When each number falls short by the same amount d, the numbers have the form k x lcm - d, and it is the same shared-deficit idea in reverse.

Take the stem "the least number greater than 400 that leaves remainder 2 when divided by 3, 5 and 7". The lcm is 105, so the numbers are 2 + 105k. The value 2 + 105 x 3 = 317 is below 400, and 2 + 105 x 4 = 422 is the answer. A number that is a multiple of 105 leaves remainder 0, not 2, so it is never the answer.

### Doctrine: counting multiples in a range

The number of multiples of d between L and U inclusive is floor(U/d) - floor((L - 1)/d). For "divisible by a or b", add the two counts and subtract the multiples of lcm(a, b). For "divisible by exactly one of a and b", subtract the overlap twice: A + B - 2AB, where AB is the count of multiples of lcm(a, b).

Take 1 to 120, divisible by exactly one of 6 and 8. Multiples of 6 number 20, multiples of 8 number 15, and multiples of lcm(6, 8) = 24 number 5. So the answer is 20 + 15 - 2 x 5 = 25. Using the product 48 as the overlap would give 20 + 15 - 2 x 2 = 31, which is wrong, because 48 is not the common multiple that matters. The product equals the lcm only when the two numbers are coprime, so the lcm is the overlap to use in general.

### Advanced part: numbers divisible by neither

This part is enrichment for the complement count. The core answer uses the counts above; this part adds one step that the examiner also uses. "Divisible by neither a nor b" is the complement of "divisible by a or b" inside the range, so count the union first and subtract it from the total: neither = N - (A + B - AB), where AB is the count of multiples of lcm(a, b).

Worked example: 1 to 200, divisible by neither 6 nor 9. Multiples of 6 number 33, multiples of 9 number 22, and multiples of lcm(6, 9) = 18 number 11. The union is 33 + 22 - 11 = 44, so the answer is 200 - 44 = 156.

Failure condition: subtracting both single counts from the total, 200 - 33 - 22 = 145, removes the eleven multiples of 18 twice. A number divisible by both 6 and 9 must be subtracted once, so the overlap is added back once to the union before the complement is taken.

### Integer pairs with a fixed sum

To count pairs of positive integers (p, q) with p < q and p + q = k, write q = k - p. The condition p < q keeps p below k/2, so the pairs run from p = 1 up to the largest integer below k/2. The count is floor((k - 1)/2). For k = 12, the pairs are (1, 11), (2, 10), (3, 9), (4, 8) and (5, 7), so there are floor(11/2) = 5. A sum determines its pair only when the count is one. To find the smallest sum that leaves two or more pairs, list the counts floor((k - 1)/2) for k = 3, 4, 5 and so on, and stop at the first k whose count reaches two. The listing is the method: it applies to any sum-condition and does not depend on remembering a value.

### Doctrine: a divisor that leaves a given remainder

A divisor d of N leaves remainder r when N = qd + r with 0 <= r < d. So d must exceed r, and d must divide N - r exactly. Counting divisors of N - r above r gives the count of divisors of N that leave remainder r. This turns a remainder question into a divisor count of a smaller number.

### Doctrine: HCF of fractions and decimals

Decimals become integers when both numbers are scaled by the same power of ten. The HCF of 2.4 and 1.5 is found from 240 and 150: their HCF is 30, so the answer is 30/100 = 0.3. For fractions in lowest terms, the HCF is the HCF of the numerators divided by the LCM of the denominators. The HCF of 3/4 and 9/10 is HCF(3, 9)/LCM(4, 10) = 3/20. Check: (3/4)/(3/20) = 5 and (9/10)/(3/20) = 6, both whole numbers.

### Doctrine: distributions that share one common value

Some stems describe a chain of proportions, such as A = 2B = 3C = 4D. Every person's share is then the common value V divided by that person's multiplier, so V must be divisible by 2, 3 and 4 at once. The smallest total uses the smallest such V, which is the LCM of the multipliers. For multipliers 2, 3 and 4 the LCM is 12, so A = 12, B = 6, C = 4 and D = 3, and the total is 25. Any larger V is a multiple of 12.

### Doctrine: the triple count with fixed HCF and LCM

When a stem gives the HCF and the LCM of three numbers, assign each prime power of the LCM to the three numbers. With HCF 1, no prime is shared by all three numbers. With LCM 30 = 2 x 3 x 5, each prime must appear in at least one number and not in all three, so each prime is assigned to one or two of the three positions. That gives six choices per prime, 6^3 = 216 ordered triples. Stems that ask for "sets" count unordered triples, so state the convention before counting, and do not mix the two.

### Doctrine: a product equal to a cube

If the product of two numbers equals the cube of one of them, write both numbers as multiples of their HCF h: a = hx and b = hy with HCF(x, y) = 1. Then the LCM is hxy, the product is h^2 xy, and the cube condition says h^2 xy is a cube of a or b. Working through the exponents of x and y is faster than trial. For example, if a = b^2 with b a prime, the product a x b equals b^3, which is a cube of b.

### Comparison with a near neighbour: HCF versus LCM

An HCF question says "greatest number that divides", "greatest length that measures", "largest group size" or "greatest number of identical pieces". An LCM question says "least number that is divisible by", "first time they coincide", "smallest number leaving the same remainder" on division by each. These are opposite operations. When the stem asks for a count of coincidences, the LCM sets the period and floor division counts the occurrences.

### The shortcut that swaps HCF and LCM

The tempting method is to take the LCM of two lengths when the stem asks for the greatest length that measures both. Reply with numbers. A rod of 120 cm and a rod of 90 cm: the LCM is 360 cm, longer than either rod, so neither rod can be laid along it. The HCF, 30 cm, measures both rods exactly, and it is the answer to the stem.

### How items are phrased

Common-multiple items ask how many times events coincide, for the smallest number that leaves given remainders, and for the number of multiples in a range. Same-remainder items ask for the greatest divisor, which is the HCF of the differences. Divisor-with-remainder items ask for a count of divisors of N minus r. Distribution items ask for a total built from a common value. The arithmetic is the same whatever the story, so the first move is always to decide HCF or LCM from the wording.

### Rules to remember

- HCF takes the smaller exponent of each prime; LCM takes the larger.
- HCF x LCM = product, for two numbers only.
- A count of coincidences in a range is floor(range / lcm).
- Same remainder gives an HCF of differences; the divisor must exceed the remainder.
- A least number with remainder r is lcm + r; a shared deficit gives k x lcm - d.
- Multiples in a range count by floor values; the overlap uses the lcm, not the product.
- "Exactly one" subtracts the overlap twice; "either" subtracts it once.
- Numbers divisible by neither equal the range minus the union (Advanced part).
- A divisor of N that leaves remainder r divides N - r and exceeds r.
- Decimals become integers by scaling with a power of ten before HCF.
- Chains of proportions share one common value, and the least total uses the LCM of the multipliers.
- For three numbers with fixed HCF and LCM, assign each prime to positions and fix the ordering convention.

### Self-test

1. Which operation does "the greatest length that measures both" need? *Answer: HCF.*
2. Compute the HCF of 36 and 84 by exponents. *Answer: 36 = 2^2 x 3^2 and 84 = 2^2 x 3 x 7, so the HCF is 2^2 x 3 = 12.*
3. Why does HCF x LCM = product fail for 2, 3 and 4? *Answer: the identity is for two numbers; for 2, 3 and 4 the product of the HCF and LCM is 12, not 24.*
4. How many integers from 1 to 60 are divisible by 5 or by 6? *Answer: 12 + 10 - 2 = 20.*

### Looking ahead

The LCM answers "when do they coincide", and it assumes that every event is measured in whole units. Once the periods are known, the remainder each number leaves becomes the next question: which numbers leave the same remainder, and how do remainders combine when numbers are multiplied? That is the next lesson.

### Practice

Attempt each item before reading its answer block.

**MCQ 8**

What is the greatest number that divides 53, 109 and 157 and leaves the same remainder in each case?

- A. 5
- B. 56
- C. 104
- D. 8

**MCQ 8 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 5 is the common remainder, not the divisor; the error is reporting the remainder as the answer.
- **B — Incorrect:** 56 is the single difference 109 - 53; the error is using one pairwise difference instead of the HCF of all of them.
- **C — Incorrect:** 104 is the difference 157 - 53, a common divisor of one pair only; the error is the same single-difference slip.
- **D — Correct:** the differences 56, 48 and 104 have HCF 8, and each number leaves remainder 5 on division by 8.

**MCQ 9**

How many integers from 1 to 230 inclusive are divisible by exactly one of 4 and 10?

- A. 58
- B. 69
- C. 5
- D. 80

**MCQ 9 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** 57 multiples of 4, 23 multiples of 10 and 11 multiples of lcm 20 give 57 + 23 - 2 x 11 = 58.
- **B — Incorrect:** 69 is the 'either' count, 57 + 23 - 11, which keeps the overlap once; the error is reading 'exactly one' as 'either'.
- **C — Incorrect:** 5 counts only the multiples of the product 40; the error is reporting one of the counts alone.
- **D — Incorrect:** 80 is 57 + 23 with no overlap removed; the error is ignoring the intersection altogether.

**MCQ 10**

A bag holds fewer than 1,000 marbles. Counted in fours, sixes or sevens, it leaves 3 marbles over each time. What is the largest possible number of marbles in the bag?

- A. 843
- B. 927
- C. 924
- D. 84

**MCQ 10 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 843 = 3 + 84 x 10 is one count short of the largest; the error is stopping one step early.
- **B — Correct:** lcm(4, 6, 7) = 84, so the possible counts are 3 + 84k; the largest below 1,000 is k = 11, which gives 927.
- **C — Incorrect:** 924 = 84 x 11 leaves remainder 0, not 3; the error is forgetting to add the remainder to a multiple of 84.
- **D — Incorrect:** 84 is the lcm itself, which leaves remainder 0; the error is reporting the lcm instead of a count with remainder 3.

## Lesson 4 - Remainders, unit digits, cycles and repunits

Progress: 4/9 | Stage: Core | Subtopic: Remainders, residues, unit-digit cycles, composite moduli and repunits

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the cycle wheel of unit digits

```text
  Power base 2 (the number raised to a power; numerals are in base 10):
     2 -> 4 -> 8 -> 6 -> 2 ...    period 4   (positions 1, 2, 3, 4)
  Power base 3:   3 -> 9 -> 7 -> 1 -> 3 ...    period 4
  Power base 7:   7 -> 9 -> 3 -> 1 -> 7 ...    period 4
  Power base 4:   4 -> 6 -> 4 -> 6 ...         period 2
  Power base 9:   9 -> 1 -> 9 -> 1 ...         period 2
  Power bases 0, 1, 5, 6 keep their own digit (period 1)

  exponent n >= 1:  n mod 4 = 1, 2, 3, 0  ->  position 1, 2, 3, 4
  a zero remainder means the FOURTH term of the cycle, not the zeroth
```

### Residues: reduce first, calculate second

A unit digit depends only on the last digit of the base, so powers of a base repeat their last digit in a cycle. A remainder works the same way. Once each factor is reduced, the remainder of a product is the product of the remainders, reduced again. The large number is never formed. The skill is reducing first and calculating second.

### Residues combine, but do not divide

For addition, subtraction and multiplication, residues combine. The remainder of a + b, a - b or a x b on division by m equals the same operation applied to the remainders of a and b, reduced by m. Division does not combine in this way. The remainder of a quotient cannot be read from the remainders of its parts, so compute the quotient first when a division is involved.

Take 8 and 4 modulo 6. Their remainders are 2 and 4. Dividing the remainders gives 2/4, which is not a remainder of anything. The true quotient 8/4 = 2 is exact, so the remainder of the division is 0.

### Negative residues

Replace a base by a small negative residue when that is smaller in size. Since 49 = 45 + 4 = 5 x 9 + 4, 49 is 4 modulo 5, or -1. Then 49^3 is (-1)^3 = -1, which is 4 modulo 5. The negative residue changes sizes, not remainders, so it helps in modular work but never in comparing sizes.

### The unit-digit cycle and the fourth term

For a power a^n with n >= 1, the unit digit is set by the unit digit of a and by n mod 4, because every cycle in the wheel has a period that divides 4. If n mod 4 = r with r in {1, 2, 3}, the unit digit is the r-th term of the cycle. If n mod 4 = 0, use the fourth term. The rule is for n >= 1, because a^0 = 1 for any non-zero a, and a^4 need not be 1.

Take 3^2018. The cycle of 3 is 3, 9, 7, 1. Since 2018 mod 4 = 2, the unit digit is the second term, 9. Check: 3^4 = 81, so 3^2016 ends in 1, and 3^2018 = 3^2016 x 9 ends in 9.

The reason for the fourth term is that the zero remainder of n mod 4 means n is a multiple of 4, and the cycle has returned to its starting point only after completing its four terms. Mapping zero to position 1 gives the first term, which is a different power.

### Composite moduli

If a modulus m is a product of distinct primes p x q, a product is divisible by m when it is divisible by both p and q. This is the reason a product of consecutive integers can leave a remainder on division by a composite number that is not simply the product of its parts. Take 11 x 12 x 13 divided by 30. Since 30 = 2 x 3 x 5, and the product contains 12 = 2^2 x 3 but no factor 5, the product is divisible by 6 but not by 30. Its remainder is therefore a multiple of 6 that leaves remainder 1 on division by 5 (since 11 x 12 x 13 = 1,716 leaves remainder 1 on division by 5), namely 6. The remainder is 6.

### A list of residues for a small modulus

When the modulus is small, list the residues of the powers until one repeats. For 2^n modulo 6, the list is 2, 4, 2, 4, ..., with period 2 from exponent 1. For 4^n modulo 6, the list is 4, 4, 4, ... so the period is 1. The list is a finite check that replaces a formula, and it is the safest method when the modulus is small.

### Repunits

A repunit is a number written with the digit 1 alone. R_n = 11...1 (n ones) = (10^n - 1)/9. So 9 R_n = 10^n - 1, which is a number of n nines.

Two facts are often needed. First, R_3 = 111 = 3 x 37, so the smallest repunit divisible by 37 has three digits, and R_5 = 11,111 = 41 x 271, so the smallest repunit divisible by 41 has five digits. Second, 10^6 - 1 = 999,999 = 3^3 x 7 x 11 x 13 x 37, so 10^6 leaves remainder 1 on division by 7, 11, 13 and 37. Hence a number of the form 10^n - 1 has its residues on division by 7 or 13 determined by n mod 6.

For a repunit of n digits, if the digits are split into a block of six ones and a block of the remaining ones, the six-ones block is divisible by 7 and contributes nothing. This is the method for a repunit whose length is not a multiple of six: the leftover ones decide the remainder. For the eleven-digit repunit divided by 7, the last five ones, 11,111, leave remainder 2.

A square of a repunit with at most nine ones has no carries, so its digit sum is n^2. For example, 111^2 = 12,321, whose digits are 1, 2, 3, 2, 1 and whose digit sum is 9 = 3^2.

### The last digit of a sum and a product

Unit digits of sums and products follow the same reduction. The unit digit of a sum is the unit digit of the sum of unit digits, and the unit digit of a product is the unit digit of the product of unit digits. A product of two numbers with unit digits 9 and 7 has unit digit 63 -> 3. For a product of powers, take each power's unit digit by its own cycle, then multiply the results.

### Remainder against quotient

The remainder is what is left after division, and it is always smaller than the divisor. A question that asks for the quotient, or for the number of times a divisor fits, needs the floor value, not the remainder. Read the stem for the word "remainder" or "quotient" before you start. The same division can answer both questions, and only one of them is asked.

### Dividing residues: the wrong move

The tempting method is to divide the remainders: "8 leaves remainder 2 on division by 6 and 4 leaves remainder 4, so 8/4 leaves remainder 2/4." This is not valid. Reply with the arithmetic: 8/4 = 2 exactly, so the remainder is 0. Residues cannot be divided, so compute the exact quotient and then reduce.

### Typical exam demands

Unit-digit items ask for the last digit of a large power or of a product of powers. Remainder items ask for the residue of a product, a sum of powers or a repunit on a stated divisor. Weekday items are remainder items: a day count taken modulo 7 gives the weekday shift. Repunit items use the R_n identity or the period of 10 modulo the divisor. Every one of these starts with reduction, not with the calculation.

### Recall list

- Unit digits repeat in cycles of period 1, 2 or 4; use n mod 4 for n >= 1.
- A zero remainder of n mod 4 selects the fourth term; a^0 = 1 is a different case.
- Residues combine under addition, subtraction and multiplication, but not under division.
- Negative residues help in modular work and never in size comparisons.
- A composite modulus of distinct primes divides a product that contains each prime.
- R_n = (10^n - 1)/9; 9 R_n is a string of n nines.
- R_3 = 111 = 3 x 37; R_5 = 11,111 = 41 x 271; 10^6 - 1 = 999,999 = 3^3 x 7 x 11 x 13 x 37.
- A repunit square with at most nine ones has digit sum n^2.
- Unit digits of sums and products depend only on the unit digits of the parts.
- Use the remainder when the stem asks for a remainder, and the floor value when it asks for a quotient.

### Quick drill

1. Which cycle does the unit digit of 7^n follow, and what is its period? *Answer: 7, 9, 3, 1 with period 4.*
2. What is the unit digit of 4^5? *Answer: 4 is a period-2 base, and 5 is odd, so the unit digit is 4.*
3. Why does a zero remainder of n mod 4 not give a^0? *Answer: a^0 = 1, while a^4 need not be 1; a zero remainder means the fourth term of the cycle.*
4. What is the remainder when 99 x 98 is divided by 7? *Answer: 99 leaves 1 and 98 leaves 0 on division by 7, so the product leaves 0.*

### Where residues lead

Residues answer questions about the size of a large number. The next question is about many numbers at once: a sequence of terms that repeats, or a block of digits that repeats. Those need a rule for how a list behaves, and before that a rule for what the digits in a number are, which is the lesson after this one.

### Practice

Attempt each item before reading its answer block.

**MCQ 11**

How many of the numbers 2^1, 2^2, 2^3, ..., 2^30 end in the digit 6?

- A. 8
- B. 15
- C. 7
- D. 4

**MCQ 11 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 8 rounds 30 / 4 = 7.5 up; the error is counting a partial cycle at the end, since the 8th digit-6 power would be 2^32, which is not in the list.
- **B — Incorrect:** 15 counts every even exponent, as if every even power of 2 ended in 6; the even exponents alternate between ending in 4 (k = 2, 6, ...) and ending in 6 (k = 4, 8, ...).
- **C — Correct:** the unit digits of the powers of 2 cycle 2, 4, 8, 6, so 2^k ends in 6 exactly when k is a multiple of 4: k = 4, 8, 12, 16, 20, 24, 28, which is 7 exponents.
- **D — Incorrect:** 4 is the length of the cycle, not the number of times the digit 6 occurs in the list; the error is reporting the cycle length as the count.

**MCQ 12**

What is the remainder when the eight-digit number 11111111 is divided by 7?

- A. 0
- B. 1
- C. 2
- D. 4

**MCQ 12 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 0 assumes that a repunit with eight ones is a multiple of 7; the first six ones form a multiple of 7, but the last two ones do not.
- **B — Incorrect:** 1 is 8 reduced modulo 7; the error is reducing the number of digits instead of the leftover block of ones.
- **C — Incorrect:** 2 is the leftover digit count, 8 mod 6, read as the remainder without reducing the two-ones block 11 modulo 7.
- **D — Correct:** the six-ones block 111111 = 7 x 15873 contributes nothing; the last two ones form 11, and 11 leaves remainder 4 on division by 7.

## Lesson 5 - Digits, place value, reversal, digit sums and digit constraints

Progress: 5/9 | Stage: Core | Subtopic: Place value, digit counts, digit frequency, reversal, permutations and column constraints

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: a number is a column of place values

```text
  Number   2   0   4   7
  place    10^3  10^2  10^1  10^0
  digit     2    0    4    7

  N = 2 x 10^3 + 0 x 10^2 + 4 x 10 + 7

  Two-digit number with tens digit a and units digit b:   N = 10a + b
  Its reversal (units and tens swapped):                  R = 10b + a
  N - R = 9(a - b)          N + R = 11(a + b)

  Digit frequency in 1 to 100 (digit 7):
     units column: 7, 17, 27, ..., 97       -> 10 sevens
     tens column:  70, 71, ..., 79          -> 10 sevens (77 has one here and one above)
     total occurrences = 20, though only 19 numbers contain a 7
```

### The idea in plain words

A question about digits is a question about a column, a count of positions or a relation between two digits. Writing the number as digits times place values turns a vague question into an equation. Counting digit occurrences is different from counting numbers: the number 77 contributes two sevens, so a count of numbers and a count of digits give different answers. Read the stem for what is counted before you calculate.

### Counting digits in blocks

An n-digit positive integer lies between 10^(n-1) and 10^n - 1. The digits used by the integers from 1 to U are counted in blocks: 1 to 9 use 9 digits, 10 to 99 use 90 numbers of two digits (180 digits), and 100 onwards use three digits each. For a range from L to U, subtract the digits used up to L - 1 from the digits used up to U.

For pages 1 to 240, the count is 9 + 180 + 3 x 141 = 612. The 141 three-digit pages are 100 to 240 inclusive. Counting 240 numbers would answer a different question. Writing the three-digit pages as two-digit numbers gives 9 + 180 + 2 x 141 = 471, which is also wrong.

The count also runs backwards. A printer uses 252 digits in all: pages 1 to 99 use 189 digits, which leaves 63 digits, and 63 / 3 = 21 three-digit pages, namely 100 to 120. So the book has 120 pages. Check: 189 + 3 x 21 = 252.

### The digit at a given position

Write the numbers in order and count digits in blocks until the target position is passed. For the concatenation 1 2 3 ... 12 written without spaces, the numbers 1 to 9 occupy positions 1 to 9. Then 10 occupies positions 10 and 11, 11 occupies 12 and 13, and 12 occupies 14 and 15. So the 15th digit is the last digit of 12, which is 2. Count to the block, then read the digit inside the number that the position falls in.

### Digit frequency, column by column

To count how often a digit d appears in 1 to N, count each column separately and add. In 1 to 100, the digit 7 appears 10 times in the units column (7, 17, ..., 97) and 10 times in the tens column (70 to 79). The total is 20 occurrences, not 19 numbers.

Within two-digit numbers, the digit 5 appears in the units column of 15, 25, ..., 95 (nine numbers) and in the tens column of 50 to 59 (ten numbers). The total is 19 occurrences. Counting the two-digit numbers that contain a 5 gives 18, because 55 contains two fives and is counted once in that method. For occurrences, always add the columns.

### Reversal and the ratio of a number to its reversal

If a two-digit number and its reversal stand in a ratio, cross-multiply and keep the digits. For N : R = 3 : 8, write 8(10a + b) = 3(10b + a). This simplifies to 77a = 22b, so 7a = 2b. Since the digits are at most 9, the only solution is (a, b) = (2, 7). So N = 27 and R = 72, and 27 : 72 = 3 : 8. Check: 8 x 27 = 216 = 3 x 72.

### Sums of digits across a range

The digit sum of the integers 20 to 39 is found column by column. The units column holds each digit 0 to 9 twice (once in 20 to 29 and once in 30 to 39), so the units total is 2 x 45 = 90. The tens column holds 2 ten times (20 to 29) and 3 ten times (30 to 39), so the tens total is 10 x 2 + 10 x 3 = 50. The digit sum of 20 to 39 is 140. The same column method gives the digit sum of any range that is a whole number of decades.

### Two-digit algebra and reversal

For a two-digit number with tens digit a and units digit b, the reversal is 10b + a. The difference is N - R = 9(a - b) and the sum is N + R = 11(a + b). So a number exceeds its reversal by a multiple of 9, and a number and its reversal sum to a multiple of 11.

For 82 and 28: a - b = 6, and 82 - 28 = 54 = 9 x 6. The digit sum is 10, and with a - b = 6 that gives a = 8, b = 2. The identity holds even when b = 0. With b = 0, N = 10a and the reversal reads as the one-digit number a, so N - R = 10a - a = 9a = 9(a - 0). Only the stem's wording "two-digit reversal" fails when b = 0, because the reversal then has one digit.

Reversal items also ask for a product. If the product of a two-digit number and its reversal is fixed, list the two-digit divisors of the product, pair each with its reversal, and test the digits; guessing from the size of the product is not enough.

### Missing digits by a test

A missing digit is found by writing the test as an equation. For 4x2 to be divisible by 9, the digit sum 6 + x must be a multiple of 9, so x = 3. For 3-divisibility alone, 6 + x must be a multiple of 3, which allows x = 0, 3, 6 and 9. The stronger test is the one that makes the answer unique, and Lesson 1 showed that the 9-test fails to be unique when the needed residue is 0.

### Permutations of distinct digits

For three distinct non-zero digits a, b and c, the six three-digit numbers formed from them place each digit in each column exactly twice. So their sum is 2 x 111 x (a + b + c). Check with 2, 3 and 6: the six numbers are 236, 263, 326, 362, 623 and 632, whose sum is 2,442 = 2 x 111 x 11.

The same idea extends to k distinct non-zero digits. There are k! arrangements, and in each place every digit appears in (k - 1)! of them, because fixing that digit in that place leaves (k - 1)! orders for the others. So the sum of all k-digit numbers formed from the digits is (k - 1)! x (sum of the digits) x R_k, where R_k is the repunit of k ones. Worked check with the digits 2, 3 and 6: each digit appears 2! = 2 times in each place, so the sum is 2 x 11 x 111 = 2,442. The condition matters: if one of the digits is 0, the arrangements that put 0 first are not k-digit numbers, so the formula does not apply. The tempting error is to use k! in place of (k - 1)!, which counts the arrangements rather than the appearances of one digit in one place.

Cyclic rotations of one three-digit number are different: XYZ + YZX + ZXY = 111 (X + Y + Z). Three rotations sum to 111 times the digit sum, so the divisors of the total come from the factors of 111 and of the digit sum; factor both and compare. When a stem asks which divisor holds for every choice of digits, test the factor 111 and the digit sum against each candidate divisor, rather than the number of permutations.

### The largest remainder after reversal

For a two-digit number and its reversal, the remainder when the larger is divided by the smaller is always less than the smaller number. Test the pairs with the largest smaller member first, and check each division directly. For 83 and 38, the remainder of 83 divided by 38 is 7, and the check is direct rather than read from the digits.

### Divisibility inside a digit string

A string of digits with one unknown digit B, such as the digits of 3,518,27B, is divisible by 3 exactly when the digit sum 26 + B is a multiple of 3. So B must be 1, 4 or 7. The count of values of B is the count of digits that satisfy the condition, and the answer is three. The same method counts values of B for a 3-test or a 9-test: change the required multiple and recount.

### Column constraints in a cryptarithm

A cryptarithm is a puzzle in which each letter or unknown stands for one digit. This session teaches only the number-theoretic constraints of such puzzles: place values, carries, the 9-test and enumeration over a small digit set. The full mechanisms of letter-coded and general puzzle families lie outside this session. Write each column's equation and the carry it passes on. If a column has one unknown, check every digit from 0 to 9 against the equation.

Take the column equation x x 3 = 1x, where the product of x and 3 has tens digit 1 and units digit x. That is 3x = 10 + x, so 2x = 10 and x = 5. Enumeration confirms it: 5 x 3 = 15, and no other digit from 0 to 9 satisfies 3x = 10 + x. A unique answer needs a check, because a carry can give two solutions in a longer puzzle.

A two-column worked example shows the carry at work. Let the sum of a two-digit number x5 and the two-digit number 3y be 134, where x and y are unknown digits. The units column gives 5 + y, which must end in 4, so y = 9 and it carries 1 (5 + 9 = 14). The tens column then gives x + 3 + 1 = 13, so x = 9 and the tens column carries 1 into the hundreds, and the leading 1 is the carry. Check: 95 + 39 = 134. Work column by column from the units, carry each result, and then check the whole sum once.

### Digit-based eliminations

For numbers from 200 to 499 whose digits are strictly decreasing, the hundreds digit h must exceed the tens digit t, which must exceed the units digit u. Count by the hundreds digit: for h = 2 the pair (t, u) comes from 0 and 1, giving 1 number; for h = 3 it comes from 0, 1 and 2, giving 3; for h = 4 it comes from 0 to 3, giving 6. The total is 10. Counting the admissible pairs is a count of choices, not of numbers in the range.

### Digits versus numbers: the near neighbour

A digit question asks what a column contains or how many times a digit occurs. A number question asks for the whole value. The digit-count method and the reversal algebra both use place values, so a candidate that has the right total but the wrong column digit is still wrong. Counting numbers instead of digits is the most common single error in this family.

### Pages: digits or numbers?

The tempting method is to count the numbers in a page range instead of the digits. Reply with pages 1 to 200: there are 200 pages, but they use 9 + 180 + 3 x 101 = 492 digits, because each page uses as many digits as its numeral has. The page count and the digit count answer different questions.

### Digit items in the paper

Digit items ask for the digits used in a page range, the number of times a digit appears, the sum of digits across a range, the reversal of a two-digit number, the sum of permutations, and the value of a missing digit that satisfies a test. Cryptarithm items ask for one digit that satisfies a column equation. Each of these becomes a place-value equation or a column count, and the method is the same each time.

### Recall notes

- Write N as the sum of digit times place value before any algebra.
- Count digit occurrences column by column, not numbers that contain the digit.
- Count digits in blocks: 9 digits for 1 to 9, 180 for 10 to 99, three per number after that.
- Digit sum of 20 to 39 is 140, found column by column; 1 to 200 uses 492 digits.
- Reversal difference is 9(a - b); reversal sum is 11(a + b).
- Permutations of three distinct digits sum to 2 x 111 times their digit sum; for k digits, (k - 1)! times the digit sum times R_k.
- Three cyclic rotations sum to 111 times the digit sum.
- A missing digit is unique by the 9-test only when the needed residue is non-zero.
- For a column equation with one unknown, check every digit that the equation allows.
- Count strictly ordered digits by choosing them from the top place downwards.

### Quick questions

1. How many digits are used by pages 1 to 120? *Answer: 9 + 180 + 3 x 21 = 252.*
2. Which digit makes 3y5 divisible by 9? *Answer: 3 + y + 5 = 8 + y, so y = 1.*
3. A two-digit number exceeds its reversal by 18. What is a - b? *Answer: 9(a - b) = 18, so a - b = 2.*
4. Why does the 3-test alone not fix a missing digit uniquely? *Answer: it allows every digit that leaves the digit sum a multiple of 3, usually three or four candidates.*

### Next lesson's question

Digit counts and column sums describe a fixed list of numbers. Many stems instead describe a list that grows by a rule: each term is found from the terms before it, or the terms repeat in a block. To answer those, you need to find the rule, check it on a term you did not use, and then read off a position. That is the next lesson.

### Practice

Attempt each item before reading its answer block.

**MCQ 13**

How many of the pages numbered 1 to 330 have a three-digit numeral?

- A. 231
- B. 90
- C. 225
- D. 230

**MCQ 13 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** pages 100 to 330 are 231 pages, each with a three-digit numeral.
- **B — Incorrect:** 90 counts the two-digit pages 10 to 99; the error is counting the wrong group of pages.
- **C — Incorrect:** 225 stops at page 324 and misses the six pages 325 to 330; the error is a count short at the upper end.
- **D — Incorrect:** 230 misses only page 330; the error is an off-by-one at the upper end.

**MCQ 14**

How many of the integers from 1 to 500 contain at least one digit 0?

- A. 50
- B. 86
- C. 91
- D. 85

**MCQ 14 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 50 counts the multiples of 10 only; the error is missing numbers whose zero is in the tens place, such as 105.
- **B — Correct:** 500 minus the numbers with no zero (9 one-digit, 81 two-digit and 324 three-digit numbers from 100 to 499) leaves 86.
- **C — Incorrect:** 91 counts the zeros written, not the numbers that contain one; the error is counting digits instead of numbers.
- **D — Incorrect:** 85 is the count up to 499, leaving out 500, which contains zeros; the error is dropping the last number.

**MCQ 15**

Which two-digit number N satisfies N minus the number formed by reversing its digits = 36 and has digit sum 12?

- A. 48
- B. 39
- C. 84
- D. 93

**MCQ 15 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 48 has digit sum 12, but its reversal is 84 and 48 - 84 = -36, not 36; the error is reversing the order of the subtraction.
- **B — Incorrect:** 39 has digit sum 12, but its reversal is 93 and 39 - 93 = -54, not 36; the error is checking the digit sum alone.
- **C — Correct:** 84 - 48 = 36 and 8 + 4 = 12; with digits a and b, 9(a - b) = 36 gives a - b = 4, and a + b = 12 gives a = 8 and b = 4.
- **D — Incorrect:** 93 has digit sum 12, but 93 - 39 = 54, not 36; the error is again checking the digit sum alone.

**MCQ 16**

The digits 2, 3 and 7 are each used once to form every three-digit number possible in all six orders. How many of the six numbers are odd?

- A. 0
- B. 6
- C. 5
- D. 4

**MCQ 16 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 0 claims that the digit 2 makes every number even; the error is ignoring that the numbers ending in 3 or 7 are odd.
- **B — Incorrect:** 6 counts all six numbers; the error is ignoring the units digit.
- **C — Incorrect:** 5 counts the number 327 twice; the error is double-counting one of the odd permutations.
- **D — Correct:** a number is odd when its units digit is odd; the odd digits are 3 and 7, so the numbers ending in 3 or 7 are 237, 273, 327 and 723, and there are four.

## Lesson 6 - Sequences, patterns and rules that must be verified

Progress: 6/9 | Stage: Core | Subtopic: Arithmetic and geometric rules, difference tables, interleaved strands, recurrences, prime-step lists, periodic sums, number matrices and derived operators

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the difference table

```text
  Sequence:       2     5    11    20    32     X
  1st difference:   3     6     9    12    15
  2nd difference:     3     3     3     3       <- constant: quadratic rule

  Interleaved strands (positions 1, 3, 5, 7 and 2, 4, 6, 8):
  1,  4,  8,  9,  27,  16,  X
  odd positions:   1 = 1^3, 8 = 2^3, 27 = 3^3          -> next cube, 4^3 = 64
  even positions:  4 = 2^2, 9 = 3^2, 16 = 4^2            -> next square, 5^2 = 25 (position 8)
```

### The idea in plain words

A sequence rule is a rule of change. Find what changes from term to term: a constant amount, an amount that changes steadily, a constant multiple, a strand that alternates or a block that repeats. Then check the rule on at least one term that you did not use to find it. A rule that fits the first three terms is a guess until a further term confirms it.

### Arithmetic and geometric rules

An arithmetic progression has a constant difference d: the n-th term is a + (n - 1)d. A geometric progression has a constant ratio r: the n-th term is a r^(n-1). Check the constancy with a second difference or ratio before you use a formula. The sequence 3, 6, 9, 12 has constant difference 3, while 3, 6, 12, 24 has constant ratio 2. Both begin with 3 and 6, so the third term decides the type.

### Difference tables and polynomial rules

Write the first differences. If they are constant, the rule is linear. If they are not constant but the second differences are, the rule is quadratic. Keep differencing until a row is constant, then extend every row back up to find the next term. For 2, 5, 11, 20, 32, the first differences are 3, 6, 9, 12, and the second differences are 3, 3, 3, 3. The next first difference is 15, so X = 32 + 15 = 47.

A short sequence can fit more than one rule. Two rules that agree on the first four terms can differ on the fifth, so the rule must be tested on an extra term.

### Interleaved strands

Some sequences interleave two rules: odd positions follow one pattern and even positions follow another. Separate the strands before searching for a rule. A rule found on the combined list may be a coincidence, and the strands will show it.

In 1, 4, 8, 9, 27, 16, X, the odd positions give 1^3, 2^3, 3^3, so the odd strand is cubes, and the next odd-position term is 4^3 = 64. The even positions give 2^2, 3^2, 4^2, an ascending strand of squares, whose next term would be 5^2 = 25. Check the answer on a term you did not use: the strands explain every term.

### Linear recurrences and two-term recurrences

A linear recurrence defines each term as a multiple of the previous term plus a constant: a(n+1) = p a(n) + q. Two consecutive pairs fix p and q. For 3, 13, 53, 213, the pairs give 13 = 4 x 3 + 1 and 53 = 4 x 13 + 1, so p = 4 and q = 1. Check: 213 = 4 x 53 + 1. The next term is 4 x 213 + 1 = 853.

A two-term recurrence adds the two preceding terms: x(n) = x(n-1) + x(n-2), with two starting terms given. The rule holds only for the stated start and the stated number of preceding terms. For 3, 1, 4, 5, 9, each term is the sum of the two before it, so the next term is 14.

### Prime-step and prime-offset lists

Some sequences step by consecutive primes. In 40, 43, 48, 55, 66, X, the differences are 3, 5, 7 and 11, which are consecutive primes. The next prime is 13, so the next difference is 13 and X = 66 + 13 = 79.

Some lists become a list of primes after a fixed operation. In 18, 20, 24, 26, 30, subtracting 7 from each term gives 11, 13, 17, 19, 23, all prime. The next prime after 23 is 29, so the next term is 36. The method is to try the operation, test whether every term becomes prime, and then find the next prime and reverse the operation.

### Periodic blocks and periodic sums

A periodic block of length p repeats forever. The term at position n equals the block term at position r, where r is n mod p, with r = p when the remainder is zero. This is the same rule as the unit-digit cycle, and the zero remainder again selects the last term of the block.

A periodic sum uses the same idea. If a block of length p sums to S, the sum of the first n terms is q S + (the sum of the first r terms of the block), where q = floor(n/p) and r = n mod p. For the block 2, 7, 1, 8 (sum 18), the first 52 terms are 13 full blocks, with no leftover, so the sum is 13 x 18 = 234. The first 53 terms add the first term 2, giving 236.

### Number matrices and figure patterns

A grid of numbers or a figure with numbers in its parts usually obeys one rule for each row. Find the rule on the complete rows first, then apply it to the incomplete row. Three rules recur.

A difference rule: in a row where the third number is the first minus the second, the row 40, 9, 31 satisfies 31 = 40 - 9. Apply the same rule to the row 50, X, 17: 17 = 50 - X, so X = 33.

A cube rule: in a row where the middle number is a^3 + c^3 for the outer numbers a and c, the row 1, 9, 2 satisfies 9 = 1^3 + 2^3, and the row 2, 35, 3 satisfies 35 = 2^3 + 3^3 = 8 + 27. Apply the same rule to the row 4, X, 1: X = 4^3 + 1^3 = 65.

A column or position rule: check the rule on every complete row before you use it on the incomplete one. A rule that works on one row and fails on another is not the rule.

### Derived operators

Some stems define a new operation, such as a * b, by giving a few examples and asking for another value. The method is to propose a rule that fits every example and to reject any rule that fails one. Suppose 4 * 7 = 14 and 9 * 2 = 19. The rule 2a + b - 1 fits both pairs: 2 x 4 + 7 - 1 = 14 and 2 x 9 + 2 - 1 = 19. A rival rule, a + b + 3, fits the first pair (4 + 7 + 3 = 14) but gives 14 for the second pair, not 19, so it is rejected. Only a rule that fits every example can be used. Then check the chosen rule once more on a fresh input, here 5 * 6 = 2 x 5 + 6 - 1 = 15, before using it on the question's own inputs.

### Periodic positions in a repeated pattern

A string made from a repeated block is read by position. If the block has length p, the character at position n is the block character at n mod p, with the last character used for a zero remainder. The same method answers questions about the k-th character from the left or right of a long repeated string.

### Arithmetic, quadratic and geometric: the near neighbour

An arithmetic rule has constant first differences. A quadratic rule has constant second differences. A geometric rule has constant ratios. The three look alike for the first two or three terms. The quickest diagnostic is to compute the first and second differences, and then the ratios, before trusting any one of them.

### Guessing from three terms

The tempting method is to guess from the first three terms. Reply with the arithmetic: the rules "double each term" and "add 2, then 4, then 6" both fit 2, 4, 8, yet they give 16 and 14 as the next term. Only a further check of the rule, or a fourth term, separates them. A rule is accepted when it is tested on a term that the rule did not use to find it.

### Sequence items in the paper

Sequence items ask for a missing term, an incorrect term, the next term or the term at a stated position. Recurrence items supply the start and ask for a later term. Periodic items ask for a sum over a number of terms or for the character at a position. Matrix items ask for a missing entry that completes a row rule. Derived-operator items give examples and ask for a value. Each starts with the change, then the verification, then the position.

### Key rules

- Use a difference table: a constant row gives the rule, and the next term follows.
- Test any rule on a term you did not use before you accept it.
- Separate interleaved strands before searching for a rule.
- A linear recurrence a(n+1) = p a(n) + q needs two pairs to fix p and q.
- Prime-step differences follow consecutive primes; prime-offset lists need the operation tested on each term.
- A periodic block uses n mod p, with a zero remainder meaning the last term.
- A periodic sum is q S plus the partial block, with q = floor(n/p).
- Matrix rules are checked on every complete row before use.
- A derived operator is accepted only when it fits every example given.
- The quickest diagnostic for the family is the first difference, the second difference and the ratio, in that order.

### Quick tests

1. What is the next term in 5, 7, 11, 17, ? *Answer: differences 2, 4, 6, so the next difference is 8 and the term is 25.*
2. In the block 4, 1, 2 repeated, what is the 100th term? *Answer: 100 mod 3 = 1, so the first block term, 4.*
3. Why does a rule fitting three terms need a fourth check? *Answer: several rules can fit three terms and differ on the fourth.*
4. What is the next term in 1, 2, 3, 5, 8, ? *Answer: 13, because each term is the sum of the two before.*

### What comes next

A sequence rule gives a term at a stated position. Two of the most common questions combine that position with a size: whether the term is large, and how large a power of the position is. A list that repeats also raises the question of how large a power of a base becomes. Those questions need a rule for the residues of powers, which the lesson after this one develops.

### Practice

Attempt each item before reading its answer block.

**MCQ 17**

In the sequence 3, 4, 7, 12, 19, X, the first differences follow a simple pattern. What is X?

- A. 28
- B. 26
- C. 31
- D. 33

**MCQ 17 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** the differences 1, 3, 5, 7 rise by 2, so the next difference is 9 and X = 19 + 9 = 28.
- **B — Incorrect:** 26 = 19 + 7 repeats the last difference; the error is copying the previous step rather than extending the pattern.
- **C — Incorrect:** 31 = 19 + 12 uses a difference of 12, a rise of 5 where the pattern rises by 2.
- **D — Incorrect:** 33 = 19 + 14 doubles the last difference instead of extending the rise.

**MCQ 18**

In the sequence 3, 7, 15, 31, X, what is X?

- A. 61
- B. 63
- C. 62
- D. 126

**MCQ 18 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 61 = 2 x 31 - 1 is a sign slip in the recurrence; the rule adds one.
- **B — Correct:** each term is twice the previous term plus 1, so X = 2 x 31 + 1 = 63.
- **C — Incorrect:** 62 = 2 x 31 omits the +1; the error is doubling without the constant.
- **D — Incorrect:** 126 = 2 x 63 doubles the answer instead of the previous term; the error is doubling at the wrong step.

**MCQ 19**

A list repeats the block 5, 2, 9 without end. What is the sum of its first 50 terms?

- A. 240
- B. 256
- C. 263
- D. 272

**MCQ 19 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 240 counts only 15 full blocks, dropping a whole block from the count.
- **B — Incorrect:** 256 counts the 16 full blocks and drops the partial block of two terms, 5 and 2.
- **C — Correct:** 16 full blocks of three terms (48 terms) sum to 16 x 16 = 256; the last two terms are 5 and 2, adding 7, so the total is 263.
- **D — Incorrect:** 272 counts 17 blocks, adding a block the list does not reach; the error is rounding the block count up.

## Lesson 7 - Large powers, factorial and product valuations, and the coprimality gate

Progress: 7/9 | Stage: Core and Advanced (Part A is Core; Parts B to F are labelled Advanced) | Subtopic: Trailing zeros, prime exponents in factorials and products, residues of large powers, the coprimality gate, power towers and last digits

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: what makes a trailing zero

```text
  A trailing zero in base 10 is one factor of 10 = one factor of 2 x one factor of 5.

  n!     factors of 2 (v_2)   factors of 5 (v_5)   trailing zeros = min(v_2, v_5)
  10!           8                    2                        2
  25!          22                    6                        6
  40!          38                    9                        9

  The factors of 2 are always more plentiful, so the 5s set the count.
```

### The idea in plain words

A large power of a fixed base produces a residue pattern. Whether the pattern repeats from the start, or first settles and then repeats, depends on whether the base shares a factor with the modulus. Reducing an exponent is safe only after you know which case you are in. The gate is the check that makes the reduction legitimate. A factorial or a product works differently: it has a count of trailing zeros, which is decided by counting how many factors of 2 and 5 it contains, and that count is a valuation rather than a residue.

### Part A (Core): trailing zeros of a factorial and of a product

#### Doctrine: trailing zeros of a factorial and the base

A trailing zero is a factor of the base. In base 10 a zero needs a factor 2 and a factor 5, so the number of trailing zeros is min(v_2, v_5). Since factors of 2 are always more plentiful than factors of 5, the count is v_5(n!). For 40!, the count is floor(40/5) + floor(40/25) = 8 + 1 = 9.

This holds only in base 10. In base 6 a trailing zero needs a factor 6 = 2 x 3, so the count is min(v_2, v_3). For 40! that is min(38, 18) = 18, which is not 9. Always state the base before applying the count of 5s.

#### Doctrine: trailing zeros and exponents of a product

The same idea applies to a product that is not a factorial. The power of 10 that divides a product is the smaller of its 2-exponent and its 5-exponent, and each factor contributes its own prime powers. For the product 5 x 10 x 15 x ... x 40 (the multiples of 5 up to 40), the 5-exponent is 9: each of 5, 10, 15, 20, 30, 35 and 40 contributes 1, and 25 contributes 2. The 2-exponent is 7: 10 contributes 1, 20 contributes 2, 30 contributes 1 and 40 contributes 3. The smaller of 9 and 7 is 7, so the product has 7 trailing zeros, not 9.

A factor count can also decide an exponent. If 10^m x n = 2^12 x 5^9 x 7 and n is not divisible by 10, then m is the smaller exponent, 9, and n = 2^3 x 7 = 56 is not divisible by 10. The same logic gives the highest power of 35 in a product: the answer is the smaller of the 5-exponent and the 7-exponent of the whole product.

#### Doctrine: the last non-zero digit

The last non-zero digit is found in three moves: remove the factors of 10 (as many 2s and 5s as make tens), read the unit digit of what remains by the cycle method of Lesson 4, and carry no zeros forward. Worked example: 10! = 2^8 x 3^4 x 5^2 x 7. Remove two factors of 10, which leaves 2^6 x 3^4 x 7 = 36,288. The unit digits are 4 for 2^6 (the cycle 2, 4, 8, 6 at position 6 gives 4), 1 for 3^4, and 7, so 4 x 1 x 7 = 28, whose unit digit is 8. The last non-zero digit of 10! is 8, and 10! = 3,628,800 confirms it.

### Part B (Advanced): the coprimality gate and residues of powers

```text
  Base 3, modulus 10 (gcd = 1):           Base 6, modulus 8 (gcd = 2):
     n     1  2  3  4  5                     n     1  2  3  4  5
     3^n   3  9  7  1  3  ...                6^n   6  4  0  0  0  ...
     purely periodic from n = 1              pre-period, then stable at 0 from n = 3

  GATE: is gcd(base, modulus) = 1 ?
     yes -> periodic from n = 1; the exponent may be reduced modulo the period
     no  -> list the residues; find the pre-period, then the eventual cycle
```

#### Doctrine: the coprimality gate

If gcd(a, m) = 1, the residues of a^n modulo m are purely periodic from n = 1, and the period divides the totient of m. In that case the exponent may be reduced modulo the period, once the period has been verified on the list. For 3^100 modulo 10, gcd(3, 10) = 1 and the cycle is 3, 9, 7, 1 with period 4. Since 100 mod 4 = 0, the fourth term, 1, is the residue.

If gcd(a, m) > 1, the residues may have a pre-period. Take 6^25 modulo 8. Here gcd(6, 8) = 2, so the gate fails. The residues are 6, 4, 0, 0, 0, ..., and from exponent 3 onward every power is a multiple of 8, because 6^3 = 216 = 27 x 8. The residue is 0. The naive method reduces 25 modulo 2 and reads position 1 of the list 6, 4, which gives 6, and that answer is wrong.

#### Doctrine: reduction inside a verified segment

For a periodic segment with period k that occupies the exponents s to s + k - 1, an exponent n can be replaced by the exponent e in that range with e congruent to n modulo k, namely e = s + ((n - s) mod k). For s = 1 this selects the last cycle term whenever k divides n, because (n - 1) mod k = k - 1. For a pre-period, first locate where repetition begins, and reduce only inside the repeating part.

### Part C (Advanced): power towers

A power tower a^(b^c) modulo m asks for the power of a whose exponent is itself a large power. Reduce the top exponent first, modulo the period of a modulo m, after you have checked that a is coprime to m or that the pre-period is short enough. For 32^(32^32) modulo 7: 32 = 4 modulo 7, and the powers of 4 modulo 7 are 4, 2, 1 with period 3. The exponent 32^32 reduces modulo 3: 32 = 2 modulo 3, and 2^32 = (2^2)^16 = 1 modulo 3. So 32^(32^32) = 4^1 = 4 modulo 7. Check the steps one at a time, because each reduction uses only the period of the previous level.

### Part D (Advanced): the exponent of a prime in a factorial

For a prime p, the exponent of p in n! is v_p(n!) = floor(n/p) + floor(n/p^2) + floor(n/p^3) + ... The sum runs until a term is zero. For the prime 2 in 40!, the sum is 20 + 10 + 5 + 2 + 1 = 38, because floor(40/32) = 1 and floor(40/64) = 0. So 2^38 divides 40! and 2^39 does not.

Stopping early is the characteristic error. For the prime 5 in 120!, the sum is 24 + 4 = 28; the term floor(120/25) = 4 must be included, and floor(120/125) = 0 ends the sum.

### Part E (Advanced): last two digits

The last two digits of a number are its residue modulo 100. Keep the leading zero: the last two digits of 3^101 are 03 when the residue is 3. A product that contains at least two factors of 2 and at least two factors of 5 is divisible by 100, so its last two digits are 00. For example, 25 x 24 = 600 has factors 5^2 and 2^3, and its last two digits are 00.

Where the product is not divisible by 100, use the residue rule with modulus 100, reducing each factor first. The gate applies here too: a base sharing a factor with 100 needs the list of residues, not a cycle assumed from exponent 1.

### Part F (Advanced): digit sums, factored powers and sums of powers

A digit sum has the same remainder on division by 9 as the number itself. So when a question asks only for the digit sum modulo 9, the power can be reduced modulo 9 with the cycle method. A full digit sum needs the digits, so the residue is a check, not a substitute, when the exact digit sum is asked.

When two large powers of small primes are added or multiplied, factor out the smallest power first. For 5^6 + 5^4, write 5^6 = 5^4 x 25, so the sum is 5^4 (25 + 1) = 26 x 5^4 = 16,250. This is divisible by 2, by 13 and by 5^4, but not by 3. The factoring turns an unreadable number into a short list of prime factors.

The divisibility of 2^n + 3^n by 4 shows the gate in a short case. For n = 1 the sum is 5, which is not a multiple of 4. For n >= 2, 2^n is a multiple of 4, so the sum is a multiple of 4 only if 3^n is; but 3^n is odd for every n, so the sum is never a multiple of 4. A stem that asks whether a sum of powers is ever divisible by a number must check the small exponents separately from the large ones.

### Comparison with a near neighbour: gate pass versus gate fail

For gcd(a, m) = 1, a cycle exists, and it is safe to use once it is verified. For gcd(a, m) > 1, the sequence may stabilise. The same arithmetic sign, "reduce the exponent", is valid in one case and wrong in the other, so the gate is the first step in every large-power question.

### Reducing the exponent too early

The tempting method is to reduce the exponent modulo the modulus. Reply with 12^9 modulo 8. Reducing 9 modulo 8 gives 12^1 = 12, which is 4 modulo 8. The true residue is 0: 12 leaves remainder 4 modulo 8, and 4^2 = 16 = 2 x 8, so every later power is a multiple of 8. The modulus is not the period.

### Question types

Items ask for the residue of a large power, the highest power of a prime in a factorial, the number of trailing zeros of a product, the last digits of a power or the highest power of one number that divides a product. Each needs the gate or the valuation first, and then a check on a small case. For base questions, the base must be named before counting.

### Memory points

- Trailing zeros in base 10 equal the smaller of the 2-exponent and 5-exponent; for a factorial, the count of 5s.
- In another base, count the factors of the base, not the factors of 5.
- The last non-zero digit: remove the factors of 10, then read the unit digit of the rest by the Lesson 4 cycles.
- Pass the coprimality gate before any reduction of an exponent.
- Non-coprime bases can stabilise; list residues to find where repetition begins.
- Legendre's sum: add floor(n/p^k) until the term is zero.
- The reduced exponent of zero in a cycle that starts at exponent 1 is the last cycle term.
- A power tower is reduced from the top, one period at a time.
- Keep the leading zero in last-two-digit answers.
- A product with two 2s and two 5s ends in 00.
- Factor out the smallest power before adding or comparing large powers.

### Check your grasp

1. Does the gate pass for 4^n modulo 10? *Answer: no, since gcd(4, 10) = 2. Do not assume a cycle from exponent 1; list the residues 4, 6, 4, 6, which show period 2 here, but the period was found by listing, not by the gate.*
2. Compute v_3(30!). *Answer: floor(30/3) + floor(30/9) + floor(30/27) = 10 + 3 + 1 = 14.*
3. How many trailing zeros does 30! have in base 10? *Answer: floor(30/5) + floor(30/25) = 6 + 1 = 7.*
4. What are the last two digits of 3^5? *Answer: 243, so 43.*

### Lesson after this

Valuations and residues describe how a large number behaves when it is divided. The next question is about size: which of several large values is bigger, how many digits a number has, and how to estimate a value from its leading digits. Those questions need the powers of ten and the laws of exponents, which the next lesson covers.

### Practice

Attempt each item before reading its answer block.

**MCQ 20**

For how many whole numbers n from 1 to 25 does 2^n leave remainder 4 when divided by 20?

- A. 12
- B. 5
- C. 8
- D. 6

**MCQ 20 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 12 is the remainder that 2^5 leaves, reported as the count; the error is answering with a remainder.
- **B — Incorrect:** 5 drops the last value n = 22 from the list; the error is an off-by-one at the upper end.
- **C — Incorrect:** 8 is the remainder for n = 3, 7, 11 and so on, reported as the count; the error is confusing a remainder with a number of exponents.
- **D — Correct:** 2^n leaves 4 for n = 2 and then every fourth exponent: n = 2, 6, 10, 14, 18 and 22, so there are six values.

**MCQ 21**

How many trailing zeros does 45! have when written in base 6?

- A. 21
- B. 10
- C. 41
- D. 15

**MCQ 21 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** in base 6 a zero needs a factor 6 = 2 x 3, so the count is min(v_2, v_3) = min(41, 21) = 21.
- **B — Incorrect:** 10 is the count in base 10, where each zero needs a 2 and a 5; the error is using the wrong base.
- **C — Incorrect:** 41 is the exponent of 2 in 45!; the error is counting the 2s, which are not the limiting factor in base 6.
- **D — Incorrect:** 15 is floor(45/3), the first term of the count of 3s; the error is stopping after the first term.

**MCQ 22**

What is the exponent of 2 in 500! minus the exponent of 5 in 500!?

- A. 618
- B. 370
- C. 494
- D. 247

**MCQ 22 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 618 adds the two exponents; the error is adding instead of subtracting.
- **B — Correct:** the exponent of 2 in 500! is 494 and the exponent of 5 is 100 + 20 + 4, so the difference is 370.
- **C — Incorrect:** 494 is the exponent of 2 alone; the error is forgetting to subtract the exponent of 5.
- **D — Incorrect:** 247 is the exponent of 3 in 500!, which uses the wrong prime.

**MCQ 23**

If 10^m x n = 2^4 x 5^13 x 3, where n is not divisible by 10, what is the exponent of 5 in n?

- A. 17
- B. 0
- C. 9
- D. 4

**MCQ 23 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 17 adds the exponents 4 and 13; the error is combining them.
- **B — Incorrect:** 0 says that n has no factor 5; the error is treating every 5 of the product as used by the power of ten.
- **C — Correct:** m = min(4, 13) = 4 uses four 5s, so n keeps 5^(13 - 4) = 5^9, and n = 5^9 x 3 is not divisible by 10.
- **D — Incorrect:** 4 is the exponent of 2 in the product, which n does not keep; the error is reading the power of 2 as if it belonged to n.

## Lesson 8 - Magnitude, powers of ten, roots, surds and recurring decimals

Progress: 8/9 | Stage: Core | Subtopic: Orders of magnitude, powers of ten, scientific notation, bounding and estimation, recurring decimals, roots and surds

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the number line of powers of ten

```text
  ... 10^2 ... 10^3 ... 10^4 ... 10^5 ... 10^6 ... 10^7 ...
        100    1,000    10,000   100,000  1,000,000  10,000,000

  Scientific notation  a x 10^k  with  1 <= a < 10
     4.2 x 10^7 = 42,000,000   k = 7, digits = k + 1 = 8
     9 x 10^5  <  1.2 x 10^6   (the exponent decides first, then the leading factor)

  Square roots of a x 10^k (k even):  sqrt(a) x 10^(k/2),  with 1 <= sqrt(a) < 10
     so N has k/2 + 1 digits for every a in [1, 10)
```

### The idea in plain words

Magnitude is the question "how many digits" asked on a logarithmic scale. Two numbers whose exponents differ by one differ by a factor of about ten, whatever their leading digits. Estimation keeps only the leading digits and tracks the direction of each rounding, so that you know whether the true value lies above or below the estimate. An estimate can decide a question only when the gap between options is larger than the total rounding error.

### Powers and exponent laws

For a non-zero a and whole numbers m and n: a^m x a^n = a^(m+n), a^m / a^n = a^(m-n), and (a^m)^n = a^(mn). A negative exponent means a reciprocal: a^(-n) = 1/a^n, so (1/a)^(-n) = a^n. A fractional exponent needs a real-domain check: a^(1/2) is real only for a >= 0.

For a base between 0 and 1, larger exponents give smaller values, so (1/2)^5 < (1/2)^3. For a base greater than 1, larger exponents give larger values. To compare powers with different bases, rewrite each in a common base. Since 8 = 2^3, 8^12 = 2^36, which is smaller than 2^40, so 8^12 < 2^40. The same rewrite handles 4^9 = 2^18 and 2^19: the common base 2 is greater than 1, so 2^18 < 2^19 and 4^9 < 2^19. Check: in every such comparison, the larger exponent of the common base gives the larger value.

Do not square an inequality when one side may be negative. The statement -3 < 2 is true, but squaring gives (-3)^2 = 9, which is not less than 2^2 = 4. Squaring preserves the order only when both sides are non-negative.

### Digit count from scientific notation

A number a x 10^k with 1 <= a < 10 has k + 1 digits, because its leading digit sits at 10^k. The factor a must be normalised first. Without normalisation the count is wrong: 42 x 10^6 = 42,000,000 has eight digits, but k + 1 with k = 6 gives seven. After normalising, 42 x 10^6 = 4.2 x 10^7, and k + 1 = 8.

The square-root rule follows from the same idea. If N^2 = a x 10^k with k even and 1 <= a < 10, then N = sqrt(a) x 10^(k/2) with 1 <= sqrt(a) < sqrt(10) < 10. So N has k/2 + 1 digits for every such a, perfect square or not. For N^2 = 9 x 10^8, N = 3 x 10^4 = 30,000, which has five digits, matching k/2 + 1 = 5.

### Bounding and estimation

Bounding gives an interval that contains the true value. Estimation rounds each factor to one significant figure, and tracks the direction of each rounding. For 49 x 51, the estimate is 50 x 50 = 2,500. One factor is rounded up by 1 and the other down by 1, and the exact product is 2,499, one less than the estimate. The error is 1.

The estimate separates two options only when their gap exceeds the total rounding error. With options 2,490 and 2,500, the gap is 10 and the error is 1, so the estimate can choose 2,500. With options 2,499 and 2,500, the gap is 1 and the error is 1, so the estimate cannot decide, and the exact value must be computed.

### Fractions with a shift

To compare fractions after the same change is made to numerator and denominator, cross-multiply. Compare a/b with c/d through ad and bc, and keep the signs, because a shift that changes a sign reverses the comparison. Cross-multiplication is exact and avoids decimals.

### Recurring decimals

A repeating block of length k with no non-repeating prefix converts to a fraction with denominator 10^k - 1: 0.(a) = a/9 and 0.(ab) = ab/99. With a non-repeating prefix, subtract. For 0.1(6), let x = 0.1666...; then 10x = 1.666... and 100x = 16.666..., and 100x - 10x = 15, so x = 15/90 = 1/6. For 0.1(27), 1,000x - 10x = 127.27... - 1.27... = 126, so x = 126/990 = 7/55.

Do not use a/9 or ab/99 when a non-repeating prefix exists. The simple forms are valid only with no prefix. For 0.(36), the value is 36/99 = 4/11, and 4/11 = 0.363636...

### Decimal place value after the point

Place value after the decimal point runs 10^-1, 10^-2 and so on. In a product, the number of decimal places equals the total number of decimal places of the factors. For 0.07 x 0.3, the factors have two and one decimal places, so the product has three: 0.021.

### Roots and surds

The square root of a non-negative integer that is not a perfect square is irrational. To bound it, find the consecutive squares that enclose it. sqrt(50) lies between 7 and 8, because 49 < 50 < 64, and its value is about 7.07.

A surd is an irrational root left in exact form. Simplify by taking out the largest square factor: sqrt(50) = sqrt(25 x 2) = 5 sqrt(2). To compare two surds, square them or compare the numbers under the root after simplifying: sqrt(11) < 3.5, because 11 < 12.25 = 3.5^2. Surds do not combine by addition: sqrt(2) + sqrt(3) is not sqrt(5), since its value is about 3.15 while sqrt(5) is about 2.24. Only like surds combine, so 3 sqrt(2) + 5 sqrt(2) = 8 sqrt(2).

### Perfect powers

The least addition that makes a number N a perfect square is (ceil(sqrt N))^2 - N. For 500, sqrt(500) is about 22.4, so the next square is 23^2 = 529, and the addition is 29. Check that 22^2 = 484 is below 500, so no smaller square is available.

A perfect square that is also a perfect cube is a sixth power, because the exponent must be divisible by both 2 and 3. Between 50 and 500 only 2^6 = 64 qualifies, since 3^6 = 729 is too large. To answer questions about the next year in which an age is a perfect power, list the perfect powers of each kind in order and read off the gap between the two that match the stem. Do not guess; check each candidate against the condition.

### Number classes in use

Rational numbers include terminating and recurring decimals, and each can be written as a fraction. Irrational numbers, such as sqrt(2), neither terminate nor recur. A non-zero rational times a rational is rational; a rational plus an irrational is irrational. This classification decides whether a decimal can be converted by the recurring-decimal method.

### Comparing by the leading digit

The tempting method is to compare numbers by their leading digit. Reply with 8 x 10^4 and 1.1 x 10^5. The leading digit 8 looks larger than 1.1, but the exponent 5 exceeds 4, so 1.1 x 10^5 = 110,000 is the larger number. The same error appears with 9.5 x 10^4, which also looks larger than 1.1 but is still below 110,000. The exponent decides first; the leading factor breaks ties.

### Magnitude in questions

Items ask which option is closest in magnitude, how many digits a large number has, which of several powers is largest, whether a recurring decimal equals a fraction, the square-root digit count of a large square, and which of several surds is larger. Each has a routine that does not require the full value. The routine is exponent first, common base or cross-multiplication second, and a one-significant-figure estimate with its direction last.

### Memory list

- Compare by exponent first, then by the leading factor.
- A number a x 10^k with 1 <= a < 10 has k + 1 digits.
- For N^2 = a x 10^k with k even, N has k/2 + 1 digits.
- Compare powers by rewriting them in a common base.
- Estimate with one significant figure; track the direction of each rounding.
- An estimate separates options only when their gap exceeds the rounding error.
- Recurring decimals: a/9 and ab/99 only without a prefix; subtract to remove a prefix.
- Place values after the decimal point add across a product.
- Simplify a surd by its largest square factor; surds add only when they are alike.
- A square that is also a cube is a sixth power.

### Short checks

1. How many digits does 5.1 x 10^9 have? *Answer: k + 1 = 10.*
2. Which is larger, 4^9 or 2^19? *Answer: 4^9 = 2^18, which is smaller than 2^19.*
3. Estimate 61 x 39 and state the direction of the error. *Answer: 60 x 40 = 2,400; the exact product is 2,379, so the estimate is too high.*
4. What is 0.(45) as a fraction? *Answer: 45/99 = 5/11.*

### Connection forward

Magnitude tells you the order of a value, but many stems ask for the best or the smallest value under a condition. That is a question about combinations: how to choose items, counts or digits so that a total is as small or as large as possible. The next lesson turns those choices into a method.

### Practice

Attempt each item before reading its answer block.

**MCQ 24**

How many digits does 3.8 x 10^12 have?

- A. 2
- B. 14
- C. 11
- D. 13

**MCQ 24 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 2 counts the digits of the leading factor 3.8 alone, ignoring the power of ten.
- **B — Incorrect:** 14 adds the two characters of 3.8 to the exponent 12; the error is counting decimal characters as places.
- **C — Incorrect:** 11 is k - 1, which loses a digit by misreading the exponent as the place of the leading digit.
- **D — Correct:** with 1 <= a < 10 and exponent k = 12, the count is k + 1 = 12 + 1 = 13 digits.

**MCQ 25**

A square tank has an area of 81 x 10^8 square centimetres. What is the sum of the digits of the length of its side, in centimetres?

- A. 9
- B. 5
- C. 10
- D. 18

**MCQ 25 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** the side is 9 x 10^4 = 90,000 cm, whose digits sum to 9.
- **B — Incorrect:** 5 counts the digits of the side, which are five, instead of adding them.
- **C — Incorrect:** 10 is the number of digits of the area 81 x 10^8, not of the side; the error is answering for the area.
- **D — Incorrect:** 18 adds the digit sums of 81 and 9, the two factors of the area; the error is combining the factors.

**MCQ 26**

How many integers from 1,000 to 20,000 inclusive are both perfect squares and perfect cubes?

- A. 0
- B. 2
- C. 3
- D. 18

**MCQ 26 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 0 claims that no square is also a cube in this range; the error is missing 4^6 = 4,096 and 5^6 = 15,625, which are sixth powers.
- **B — Correct:** a square that is also a cube is a sixth power; 4,096 and 15,625 lie in the range, and 6^6 = 46,656 does not.
- **C — Incorrect:** 3 adds 3^6 = 729, which lies below 1,000; the error is ignoring the lower bound.
- **D — Incorrect:** 18 counts the cubes from 10^3 to 27^3, ignoring the square condition.

## Lesson 9 - Integer combinations, extremes and minimum counts

Progress: 9/9 | Stage: Core | Subtopic: Minimum counts of items, common-value distributions, extremes over distinct values and operator choices

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: a bounded search for coin combinations

```text
  Target 22 g from coins of 3, 5 and 9 g (unlimited): how many different combinations?

  Greedy:  9 + 9 = 18; the next coin is 3 g -> 21; 1 g is left, so greedy finds no way to pay 22.

  Enumeration by the count of 9 g coins:
     no 9 g coin : 3a + 5b = 22 has one solution, (a, b) = (4, 2)
     one 9 g coin: 3a + 5b = 13 has one solution, (a, b) = (1, 2)
     two 9 g coins: 4 g is left, which no combination of 3 g and 5 g pays

  Total combinations: 2
```

### The idea in plain words

Many CSAT questions ask for the fewest items, the greatest total, or the smallest value over several choices. A list of options is too long to check one by one, but the search can be bounded. Fix the counts of the largest items, because they dominate the total, and then fill the remainder with the smallest number of smaller items. The method is an organised search, not a guess.

### Minimum number of items: greedy versus enumeration

The greedy method takes the largest item first, then the next largest, and so on. It is correct when each denomination divides the next, which makes the set canonical. When the denominations do not form such a chain, greedy can fail. The coins 3, 5 and 9 are not a divisibility chain, since 3 does not divide 5. Greedy takes 9 and 9, which makes 18, then 3 g, which makes 21, and the remaining 1 g cannot be paid, so greedy needs a different approach.

The correct method enumerates the number of the largest coins that can be used, then counts the solutions of the smaller problem for the remainder. For 22 g the enumeration by the count of 9 g coins gives two combinations: four 3 g coins with two 5 g coins, and one 9 g coin with one 3 g coin and two 5 g coins. Greedy finds neither, because it commits to the 9 g coins first.

The same method answers a measuring question. With cylinders of 4, 7 and 10 litres and at most two pours, the largest amount of at most 15 litres that can be measured exactly is 14 litres, and two pairs give it: 7 + 7 and 4 + 10. Enumerate the pairs and read the total of each one, rather than assuming that the largest cylinder is always the right first pour.

### A common-value distribution

When shares are proportional to fixed multipliers, as in A = 2B = 5C, all shares are multiples of one common value V. Every share is V divided by its multiplier, so V must be a multiple of every multiplier: the least possible V is the LCM of 2 and 5, which is 10. Then A = 10, B = 5 and C = 2, and the total is 17. A larger V multiplies every share, so the least total uses the least V.

When the total is fixed rather than the least value, the same idea runs backwards. For A = 4B = 6C, the shares are V, V/4 and V/6, so the total is V(1 + 1/4 + 1/6) = 17V/12. A total of 170 gives V = 120, with B = 30 and C = 20. A total that does not give a whole V has no solution.

An extra condition on the shares, such as 'every share must be even', turns V into V = 10k and forces k. For A = 2B = 5C, write A = 10k, B = 5k and C = 2k for a whole number k. B = 5k is even only when k is even, so the least k is 2, giving A = 20, B = 10 and C = 4, with total 34. If the condition were 'every share must be odd', no solution would exist, because A = 10k is even for every k. Failure condition: taking the least V = 10 (k = 1) without checking the condition gives shares 10, 5 and 2, and B = 5 is odd and C = 2 is even, so the condition fails; test the condition on every share before accepting the total.



### A maximum of a product of two sums

For a fixed total T, the product of two sums s and T - s is largest when the sums are as close as possible. This is the balance of two numbers with a fixed sum. For distinct digits, choose the four digits so that the total of the two pairs is as large as possible, and then split them so that the two pair sums are as close as possible. For the digits 3, 4, 5 and 6, the total is 18. The splits give (6 + 3)(5 + 4) = 81, (6 + 4)(5 + 3) = 80 and (6 + 5)(4 + 3) = 77. The most balanced split is the largest product.

### Extremes over distinct values

For a sum of products, x1 y1 + x2 y2 + ... with distinct values in each list, the sum is largest when both lists are sorted in the same order and smallest when they are sorted in opposite orders. This is the rearrangement idea. For x = (1, 2, 3) and y = (4, 5, 6), the largest sum is 1 x 4 + 2 x 5 + 3 x 6 = 32 and the smallest is 1 x 6 + 2 x 5 + 3 x 4 = 28. Check the extreme by one swap: exchanging two partners can only move the sum toward the middle.

### The smallest ratio of a number to its digit sum

To minimise the ratio of a number to its digit sum, write the number by its digits. A two-digit number with tens digit a and units digit b has ratio (10a + b)/(a + b) = 1 + 9a/(a + b). The ratio falls when the tens digit a is small and the units digit b is large, because the fraction 9a/(a + b) shrinks. So the smallest ratio uses a = 1 and b = 9: the number 19 has ratio 19/10 = 1.9. Check one rival: 29 has ratio 29/11, about 2.64, and 10 has ratio 10/1 = 10. The smallest number is not the number with the smallest ratio: a small digit sum makes the ratio large. This pattern is for two-digit numbers. For more digits, do not assume every other digit should be 9: with four digits, 1099 has ratio 1099/19, about 57.8, which is smaller than 1999/28, about 71.4, so compare the few candidates that keep the leading digit at 1 instead of guessing. Failure condition: comparing numbers by size alone, or by digit sum alone, ignores that the ratio depends on both.

A search by a digit condition works in order. The first two-digit multiple of 7 whose digit sum is 10 is 28: list the candidates in increasing order and stop at the first one that satisfies the condition. Here the multiples of 7 are 14, 21, 28, with digit sums 5, 3 and 10; 14 and 21 fail, so 28 is the answer. Listing in order is what makes the answer the first that fits, not the first guess.

### Placing operators for an extreme value

In a chain 7 ? 3 ? 2, each blank takes one operation from +, - and x, and each operation may be used at most once. The six placements that use two different operations are 7 + 3 x 2 = 13, 7 x 3 + 2 = 23, 7 + 3 - 2 = 8, 7 - 3 + 2 = 6, 7 x 3 - 2 = 19 and 7 - 3 x 2 = 1. Enumerate every placement that respects the limit and compute each total, with precedence visible, before comparing; here the largest is 23.

### Comparison with a near neighbour: greedy versus enumeration

Greedy is fast and correct only for canonical denominations. Enumeration of the largest counts is slower but correct for any set. The difference is that greedy commits to the largest item before checking the remainder. Enumeration checks the remainder for each candidate count of the largest item before committing. When a stem gives an unfamiliar set of denominations, enumerate.

### Greedy: the tempting shortcut

The tempting method is greedy: take the largest coin first and stop when the total is reached. Reply with 22 g and the set 3, 5 and 9 g. Greedy takes 9 and 9, then can pay only 3 g more, and 1 g is left unpaid. Enumeration finds the two combinations that greedy never reaches.

### Extreme-value questions

Items ask for the fewest coins, pours or items, for a common total of shares, for the largest product of two sums, for the extreme of a sum of products, for the extreme value of a ratio and for the best placement of operators. Each reduces to an organised search: fix the largest counts, use the balance or the rearrangement idea where it applies, and compute the candidates rather than estimating.

### Points to recall

- Greedy is correct only for canonical denominations; test the remainder before accepting it.
- Enumerate the counts of the largest items, then solve the smaller remainder.
- A common-value distribution has least total at the LCM of the multipliers.
- For a fixed sum, a product of two parts is largest when the parts are closest.
- Sorted in the same order gives the largest sum of products; opposite order gives the smallest.
- The ratio N/S is smallest with a small hundreds digit and large lower digits; check candidates.
- Subtracting a product lowers the total; check the precedence of every placement before comparing totals.
- Check every candidate placement; do not estimate an extreme.
- Name the convention before counting ordered and unordered sets.
- The fewest items is an optimisation, so count the total for each candidate.

### Self-check questions

1. How many combinations of 3, 5 and 9 g coins total 22 g? *Answer: 2, namely four 3 g coins with two 5 g coins, and one 9 g coin with one 3 g coin and two 5 g coins.*
2. Which product of two sums of the digits 3, 4, 5 and 6 is largest? *Answer: (6 + 3)(5 + 4) = 81.*
3. Why does the common-value method give the smallest total when the value is the LCM? *Answer: each share is the value divided by its multiplier, so a smaller value gives every share less.*
4. Which two sums of x and y give the largest sum of products, sorted together or in opposite order? *Answer: sorted together.*

### Closing the chain

This lesson completes the chain. Each earlier lesson gave one tool for a property of numbers: a test, a count, a remainder, a cycle, a digit equation, a rule for a list, a valuation or a magnitude. Combination questions use several at once. The cumulative items that follow mix the lessons, so that each one must choose its own tool.

### Practice

Attempt each item before reading its answer block.

**MCQ 27**

In how many different ways can 44 g be totalled using coins of 4 g, 5 g and 9 g, with any number of each?

- A. 5
- B. 3
- C. 8
- D. 16

**MCQ 27 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 5 counts only the combinations that use at least one 9 g coin; the error is leaving out the combinations with no 9 g coin.
- **B — Incorrect:** 3 counts only the combinations with no 9 g coin; the error is refusing the largest denomination.
- **C — Correct:** counting by the number of 9 g coins, there are 3 combinations with none, 2 with one, and 1 each with two, three and four: 3 + 2 + 1 + 1 + 1 = 8.
- **D — Incorrect:** 16 is twice the count of 8, as if the order of the coins mattered; the error is counting arrangements rather than combinations.

**MCQ 28**

A rectangle's length and width are each the sum of two different digits chosen from 1 to 7, and the four digits used are all different. What is the smallest possible area of the rectangle?

- A. 24
- B. 25
- C. 30
- D. 21

**MCQ 28 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 24 = (1 + 3)(2 + 4) is the balanced split, which gives a larger area than the smallest; the error is choosing the most balanced split when the smallest is asked.
- **B — Incorrect:** 25 = (1 + 4)(2 + 3) is larger than 21; the error is choosing a split without comparing all three.
- **C — Incorrect:** 30 = (1 + 5)(2 + 3) uses 5 where a smaller digit fits, so it is not the smallest; the error is using the wrong digit set.
- **D — Correct:** (1 + 2)(3 + 4) = 3 x 7 = 21, the smallest of the three splits of the digits 1, 2, 3 and 4.

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

This section links every Prelims CSAT question from 2013 to 2026 whose method this session teaches: 133 linked questions, 24 from 2013 to 2017 and 109 from 2018 to 2026. Seven further questions share one step with this session, and they are listed separately with that step. Nothing in this section solves a question, gives an answer, or reproduces a stem.

**Status of the 2026 entries: provisional.** Every 2026 entry below is provisional and carries no answer.

Three points govern the lists.

1. **Lesson mapping.** Each linked item is taught in the lesson named beside it. Items that share a step are listed separately, with that step.
2. **Typing.** Each item is typed from its question text, in neutral words that name the method and not the answer.
3. **Approach.** Each lesson's approach names the first move and its failure condition. It never names an option.

## How the lessons add up

| Lesson | Items | Neutral types taught in that lesson |
|---|---:|---|
| 1 Divisibility and digit tests | 10 | divisibility tests, digit-based eliminations, parity, digit constraints from a divisibility condition |
| 2 Primes, factors and consecutive integers | 16 | primes, factor counts and sums, difference of squares, consecutive sums, unit-fraction counts, triangular positions, odd factor counts |
| 3 HCF, LCM and counts | 21 | HCF and LCM, coincidence counts, same-remainder and multiple counts, shared-remainder and triple counts, range counts with overlap |
| 4 Remainders, cycles and repunits | 11 | residues, unit-digit cycles, composite moduli, repunits |
| 5 Digits and reversal | 29 | digit counts, digit frequency, digit sums, reversal, permutation sums, cryptarithm constraints, digit strings with a divisibility condition |
| 6 Sequences and patterns | 21 | arithmetic, quadratic and recurrence rules, interleaved and prime-step lists, periodic sums, matrix rules, derived operators |
| 7 Large powers and valuations | 12 | residues of large powers, the gate, factorial and product valuations, last two digits, last non-zero digit |
| 8 Magnitude, roots and decimals | 8 | magnitude, digit counts from scientific notation, comparisons, recurring decimals, roots and perfect powers |
| 9 Combinations and extremes | 5 | minimum counts of items, common-value distributions, extremes over distinct values, ratio extremes |
| **Total** | **133** | |

## Items that share a step

These items share one step with this session, and their main method lies outside it. Each line names the step that this session teaches. No item here is solved in this file.

- [Q31](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q031) (2013): ratio of counts after a sharing condition. Step taught here: the ratio step is outside this session; read the sharing condition first.
- [Q60](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q060) (2013): ratio of counts after an addition. Step taught here: the ratio step is outside this session; read the addition condition first.
- [Q79](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q079) (2015): counts of coloured objects. Step taught here: the counting step is outside this session; the stem's counts must be read before any arithmetic.
- [Q40](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q040) (2016): true-false patterns under a constraint. Step taught here: the pattern step is outside this session; test each statement against the stated constraint.
- [Q26](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q26) (2023): maximum of a product of two pair sums. Step taught here: the balance idea of Lesson 9 applies to the sum-product step; the rest of the item lies outside this session.
- [Q40](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q40) (2023): prime-group odd one out. Step taught here: the primality test of Lesson 2 applies to each member; the group comparison lies outside this session.
- [Q69](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q69) (2023): coin purchase versus weighing. Step taught here: the enumeration of the largest counts in Lesson 9 applies; the weighing comparison lies outside this session.

## Per-year lists

Each entry gives the question number, the lesson that teaches its method, and a short neutral type. The link opens the question in the linked question file. Cross-links are listed after the linked items for the same year.

**2013 (4 linked; 2 sharing a step):** [Q28](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q028) L3, common meeting count of five periodic groups within a period; [Q48](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q048) L6, value at a marked position of a number matrix; [Q50](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q050) L6, figure pattern with a missing part; [Q61](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q061) L8, smallest addition that makes a square arrangement; [Q31](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q031) shares a step, ratio of counts after a sharing condition; [Q60](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q060) shares a step, ratio of counts after an addition.

**2014 (6 linked):** [Q06](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q006) L3, common firing times of several periodic events; [Q22](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q022) L2, triangular positions of marks counted from both ends of a segment; [Q42](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q042) L6, table with a constant row-sum rule; [Q46](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q046) L3, common ringing times of several bells; [Q61](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q061) L5, digit substitution puzzle with a column constraint; [Q76](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q076) L4, weekday after a day count, read as a remainder modulo 7.

**2015 (3 linked; 1 sharing a step):** [Q12](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q012) L6, number matrix with a row rule; [Q13](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q013) L6, missing term of a short series; [Q57](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q057) L5, multiplication cryptarithm; [Q79](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q079) shares a step, counts of coloured objects.

**2016 (4 linked; 1 sharing a step):** [Q13](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q013) L3, common meeting count of periodic events; [Q53](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q053) L2, odd count of factors and perfect squares; [Q62](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q062) L1, divisibility statement about a form of number; [Q63](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q063) L3, count in a range with inclusion-exclusion; [Q40](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q040) shares a step, true-false patterns under a constraint.

**2017 (7 linked):** [Q35](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q035) L2, mean of consecutive odd numbers; [Q49](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q049) L5, three-digit numbers with distinct digits, reversal and the 7-test; [Q51](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q051) L5, count of numbers with a fixed digit in the units place; [Q53](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q053) L8, ages that are squares and cubes in consecutive years; [Q73](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q073) L5, largest remainder after reversing a two-digit number; [Q79](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q079) L5, two-digit numbers and reversal difference; [Q80](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q080) L5, digit count of a page range.

**2018 (2 linked):** [Q03](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q03) L6, number pattern with a missing entry in a figure; [Q36](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q36) L5, count of numbers whose digits are strictly ordered.

**2019 (8 linked):** [Q09](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q09) L5, frequency of one digit across 1 to 1000; [Q15](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q15) L3, count with two divisibility conditions that overlap; [Q33](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q33) L5, two-digit numbers in a fixed reversal ratio; [Q48](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q48) L6, series with prime-step differences; [Q51](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q51) L6, interleaved square strands; [Q53](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q53) L5, page count from a total of digits; [Q60](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q60) L1, digit constraint from a divisibility condition; [Q75](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q75) L1, count of digit values that satisfy a 3-test.

**2020 (17 linked):** [Q07](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q07) L7, trailing zeros of a product of multiples of 5; [Q08](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q08) L5, divisibility of a cyclic sum of digits; [Q10](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q10) L1, primality of digit arrangements via the digit sum; [Q11](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q11) L5, digit symbol equation; [Q12](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q12) L3, HCF of decimal measurements; [Q13](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q13) L6, prime-offset sequence; [Q14](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q14) L2, torn-leaf page sum; [Q37](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q37) L5, digit and divisibility count; [Q50](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q50) L8, largest of several powers with negative exponents; [Q51](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q51) L3, HCF of two measurements; [Q53](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q53) L8, recurring decimal conversion; [Q54](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q54) L3, least number with a common remainder; [Q56](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q56) L7, remainder of a product modulo 100; [Q58](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q58) L7, digit sum of a large power; [Q75](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q75) L2, pairs of numbers whose squares differ by a fixed amount; [Q76](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q76) L8, comparison of fractions after a shift; [Q77](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q77) L1, divisibility condition on a digit.

**2021 (10 linked):** [Q05](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q05) L4, remainder of a large power on division by 10; [Q06](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q06) L1, missing digit by the 7-test; [Q26](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q26) L6, incorrect term in an interleaved sequence; [Q36](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q36) L5, sum of permutations of three digits and divisibility; [Q50](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q50) L6, missing term of a recurrence-type sequence; [Q59](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q59) L5, addition cryptarithm; [Q60](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q60) L5, multiplication cryptarithm; [Q67](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q67) L2, statements on sums of consecutive integers; [Q76](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q76) L5, digit interchange difference; [Q79](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q79) L4, smallest repunit multiple.

**2022 (11 linked):** [Q04](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q04) L6, term of a sequence; [Q05](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q05) L1, divisibility of a digit arrangement; [Q09](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q09) L8, magnitude comparison; [Q47](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q47) L9, common-value distribution with a parity condition; [Q54](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q54) L5, digit sums of permutations with bounds; [Q58](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q58) L4, product remainder with a composite modulus; [Q65](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q65) L3, least number above a bound with a common remainder; [Q66](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q66) L5, two-digit reversal product; [Q67](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q67) L2, prime and composite statements; [Q74](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q74) L7, exponent of a prime in a factorial; [Q75](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q75) L6, term of a sequence.

**2023 (17 linked; 3 sharing a step):** [Q07](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q07) L4, remainder of a product modulo a number; [Q08](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q08) L4, unit digit of a large power; [Q09](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q09) L5, addition cryptarithm with digit sums; [Q10](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q10) L9, minimum ratio of a three-digit number to its digit sum; [Q14](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q14) L2, parity of a set of integers; [Q15](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q15) L2, prime and composite statements; [Q16](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q16) L5, digit multiplication constraint; [Q17](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q17) L1, divisibility of a repeated block; [Q25](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q25) L2, count of divisors under a condition; [Q27](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q27) L4, remainder of a repunit-type number; [Q28](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q28) L4, digit sum of the square of a repunit; [Q29](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q29) L5, digit sum over a range; [Q45](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q45) L3, divisors of a number that leave a given remainder; [Q46](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q46) L5, digit sum with repeated digits; [Q47](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q47) L5, permuted-digit number sum over four digits; [Q74](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q74) L7, remainder of a large power; [Q76](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q76) L5, digit cryptarithm solved column by column; [Q26](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q26) shares a step, maximum of a product of two pair sums; [Q40](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q40) shares a step, prime-group odd one out; [Q69](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q69) shares a step, coin purchase versus weighing.

**2024 (13 linked):** [Q06](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q06) L9, operator placement with a minimum value; [Q09](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q09) L7, trailing zeros of a product; [Q10](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q10) L6, cumulative sequence of savings; [Q15](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q15) L7, divisibility of large powers; [Q17](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q17) L7, last non-zero digit of a product; [Q18](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q18) L3, divisor with a common remainder; [Q19](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q19) L3, container size by highest common divisor; [Q20](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q20) L4, unit digit of a sum of primes; [Q39](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q39) L1, parity of an expression; [Q46](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q46) L6, sum of a periodic sequence; [Q54](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q54) L7, divisibility of a sum of powers; [Q55](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q55) L3, count of integer pairs; [Q79](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q79) L6, term of a sequence.

**2025 (19 linked):** [Q05](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q05) L2, factor-sum enumeration; [Q06](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q06) L2, progressions of primes; [Q07](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q07) L2, unit-fraction solution count; [Q16](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q16) L6, derived operator from examples; [Q18](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q18) L3, smallest number with several remainders; [Q20](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q20) L4, unit digit of an odd product; [Q25](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q25) L3, count of numbers by exclusion of multiples; [Q27](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q27) L2, count of primes with a quadratic form; [Q28](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q28) L3, count of triples with fixed HCF and LCM; [Q35](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q35) L7, highest power of a factor in a product; [Q36](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q36) L6, number-series completion with products; [Q40](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q40) L8, digit count of a square root; [Q46](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q46) L7, distinct remainders of a sum of powers; [Q47](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q47) L3, HCF of a repdigit and a number; [Q48](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q48) L5, digit at a position of a concatenation; [Q60](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q60) L6, difference sequence; [Q64](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q64) L2, statements about factor counts; [Q67](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q67) L4, remainder of a power series; [Q80](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q80) L3, count of multiples between bounds.

**2026 (12 linked):** [Q10](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q10) L3, count of common multiples in a range (provisional 2026 item); [Q18](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q18) L6, periodic positional pattern (provisional 2026 item); [Q19](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q19) L7, exponent from a prime factorisation (provisional 2026 item); [Q22](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q22) L9, fewest measurements for a total (provisional 2026 item); [Q29](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q29) L9, extremes of an expression over distinct values (provisional 2026 item); [Q42](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q42) L4, unit digit of a product of powers (provisional 2026 item); [Q45](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q45) L8, count of powers of two by bounds (provisional 2026 item); [Q49](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q49) L5, frequency of a digit in two-digit numbers (provisional 2026 item); [Q57](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q57) L6, recurrence sequence (provisional 2026 item); [Q59](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q59) L3, HCF and LCM identity with a cube condition (provisional 2026 item); [Q60](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q60) L1, divisibility by 11 with a digit puzzle (provisional 2026 item); [Q66](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q66) L5, reversed-digit divisibility count (provisional 2026 item).

## Approach by lesson

- **Lesson 1, property and test items.** Decide whether the stem asks a yes-or-no property (apply the test for the divisor) or a count (factorise in Lesson 2). A test fails when the base is not 10, or when the two halves of a divisor are not coprime.
- **Lesson 2, factor and prime items.** Factorise first. Then read the stem for its operation: count the factors, sum them, test primality up to the square root, count factor pairs with equal parity, or sum consecutive integers as k times their mean. For a triangular-position stem, write the distances from the stated end, check the increments, and count the distances inside the segment. For a torn-leaf stem, the page count n must be fixed; the removed pair sums to S_n minus the remaining total.
- **Lesson 3, common-multiple and measure items.** Decide from "greatest" or "least" which operation applies. For a same-remainder stem, take the HCF of the differences and check that the remainder is smaller than the divisor. For a count of coincidences, use floor(range / lcm). For a distribution, take the LCM of the multipliers. For a stem about numbers divisible by neither of two divisors, subtract the union from the range, and count the overlap once.
- **Lesson 4, residue and unit-digit items.** Reduce each factor first. Use the unit-digit cycle with n mod 4 for n >= 1; for a composite modulus, use the prime factors; for a repunit, use the identity 9 R_n = 10^n - 1.
- **Lesson 5, digit items.** Write the place-value equation, count digit occurrences column by column, use the reversal identity for two-digit reversals, and enumerate the digits a column equation allows. For permutation sums of k distinct non-zero digits, multiply the digit sum by (k - 1)! and by the repunit R_k. For a two-column cryptarithm, solve the units column first, carry its result, and then solve the next column.
- **Lesson 6, sequence items.** Separate strands or blocks, find the difference or ratio, test the rule on a term you did not use, and count a periodic sum by full blocks plus the partial block. For a derived operator, accept only a rule that fits every example.
- **Lesson 7, large-power and factorial items.** Pass the coprimality gate before reducing an exponent, use the Legendre sum for a prime's exponent, and count trailing zeros by the smaller of the 2- and 5-exponents in base 10. For a last non-zero digit, remove the factors of 10 first. State the base before counting.
- **Lesson 8, magnitude and root items.** Compare by exponent first, rewrite powers in a common base, estimate with one significant figure while tracking the direction of each rounding, and normalise scientific notation before counting digits.
- **Lesson 9, minimum and extreme items.** Enumerate the counts of the largest items, check the remainder for each candidate, and use the balance or the rearrangement idea only where the stem's structure supports it.

# CUMULATIVE MCQS

These six items combine two or more lessons. They are numbered on from the last lesson item and do not repeat any lesson item. The lessons combined are: 29 (Lessons 1 and 5), 30 (Lessons 2 and 3), 31 (Lessons 4 and 6), 32 (Lessons 4 and 7), 33 (Lessons 2, 7 and 8) and 34 (Lessons 2 and 7). Attempt them under the timed routine in the next section, then check any error against the error codes.

**MCQ 29**

For which digit d is the four-digit number 1d04 divisible by 11?

- A. 8
- B. 3
- C. 6
- D. 5

**MCQ 29 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** counting places from the right, the digits 4 and d sit in the odd places and 0 and 1 in the even places, so (4 + d) - (0 + 1) = d + 3 must be a multiple of 11; d = 8 gives 11, and 1804 = 11 x 164.
- **B — Incorrect:** 3 compares the first two digits with the last two, (1 + 3) - (0 + 4) = 0; the error is pairing adjacent digits instead of alternate places.
- **C — Incorrect:** 6 adds all four digits, 1 + 6 + 0 + 4 = 11; the error is using the digit sum, which is the test for 3 and 9, not the alternating difference.
- **D — Incorrect:** 5 pairs the first digit with the last against the two middle digits, (1 + 4) - (5 + 0) = 0; the error is choosing the wrong places for the two groups.

**MCQ 30**

How many positive divisors does the least common multiple of 18 and 24 have?

- A. 4
- B. 12
- C. 8
- D. 9

**MCQ 30 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 4 is the number of divisors of 6, the HCF of 18 and 24; the error is using the HCF where the LCM is asked.
- **B — Correct:** the LCM is 2^3 x 3^2 = 72, with (3 + 1)(2 + 1) = 12 divisors.
- **C — Incorrect:** 8 is the number of divisors of 24 alone; the error is counting one number's divisors rather than the LCM's.
- **D — Incorrect:** 9 uses the exponent 3 of 2 as 3 rather than 3 + 1, which gives (3)(2 + 1); the error is an omitted +1.

**MCQ 31**

How many of the first 50 terms of the sequence 8^1, 8^2, 8^3, and so on have 4 as their unit digit?

- A. 12
- B. 25
- C. 13
- D. 50

**MCQ 31 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** 12 stops at the exponent 46 and misses 50, the last exponent of the list; the error is an off-by-one at the end.
- **B — Incorrect:** 25 counts all even exponents; the error is counting even exponents instead of those with the right remainder.
- **C — Correct:** 8^n has unit digit 4 when n mod 4 = 2 (the cycle 8, 4, 2, 6): the exponents 2, 6, ..., 50 give 13 terms.
- **D — Incorrect:** 50 counts every term; the error is ignoring that the unit digits cycle.

**MCQ 32**

What is the smallest positive integer n for which 18^n is divisible by 16?

- A. 2
- B. 8
- C. 16
- D. 4

**MCQ 32 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** 2 reads 18 as if it were divisible by 4; 18 = 2 x 9 has only one factor 2, so 18^2 = 324 is divisible by 4 but not by 16.
- **B — Incorrect:** 8 divides 16 by the prime 2, treating the modulus as a count of 2s rather than as 2^4; the error is not factorising 16.
- **C — Incorrect:** 16 uses the modulus itself as the exponent; the question asks for the least n, and a smaller power already works.
- **D — Correct:** 18^n = 2^n x 9^n, and the odd factor 9^n adds no factor 2, so 18^n has exactly n factors 2; 16 = 2^4 needs four of them, so n = 4.

**MCQ 33**

How many digits does 2^10 x 5^3 have when written out in full?

- A. 6
- B. 4
- C. 7
- D. 9

**MCQ 33 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** 2^10 x 5^3 = 2^7 x 10^3 = 128,000 = 1.28 x 10^5, so the count is k + 1 = 5 + 1 = 6 digits.
- **B — Incorrect:** 4 is k - 1 for 1.28 x 10^5; the error is losing a digit by misplacing the leading digit.
- **C — Incorrect:** 7 adds the digit counts of the two factors, 1,024 (four digits) and 125 (three digits); the error is counting the factors, not the product.
- **D — Incorrect:** 9 adds the digit count of 1,024 to the exponent 5 of the power of ten; the error is mixing a digit count with an exponent.

**MCQ 34**

How many trailing zeros does 16 x 81 x 35 have when written in base 6?

- A. 1
- B. 4
- C. 9
- D. 0

**MCQ 34 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** 1 is the count obtained with base 10, where the single factor 5 gives one zero; the error is using the wrong base.
- **B — Correct:** in base 6 a zero needs a factor 6 = 2 x 3, so the count is min(4, 4) = 4, since 16 = 2^4 and 81 = 3^4.
- **C — Incorrect:** 9 adds 4 + 4 + 1, the two exponents and the exponent of 5 in 35; the error is adding exponents instead of pairing the factors of 2 with the factors of 3.
- **D — Incorrect:** 0 claims that no factor 6 is present; the error is ignoring the factors of 16 and 81.

# TIMED-SET PRACTICE AND SCORING RUBRIC

This section turns the lessons into a timed routine for number-sense items. The budgets are this session's working plan, derived from the paper's structure of 80 equal-mark items in two hours (about 90 seconds on average). They are not official cut-offs.

## Time budgets by item type

| Item type | Budget per item | Why |
|---|---:|---|
| Divisibility test or parity (Lesson 1) | 30 seconds | the test answers it directly |
| Factor count, prime check or factor sum (Lesson 2) | 45 seconds | factorise, then apply the formula |
| HCF, LCM or same-remainder (Lesson 3) | 75 seconds | decide the operation first |
| Multiples count with overlap (Lesson 3) | 75 seconds | floor values and one overlap |
| Unit digit or remainder (Lesson 4) | 60 seconds | reduce, read the cycle |
| Repunit or composite modulus (Lesson 4) | 90 seconds | identity or prime factors first |
| Digit count, reversal or missing digit (Lesson 5) | 60 seconds | place-value equation |
| Cryptarithm or digit-sum over a range (Lesson 5) | 120 seconds | column equation, then enumerate the surviving digits |
| Sequence, periodic sum or matrix (Lesson 6) | 60 seconds | difference table or block count, then one check |
| Large power, factorial or product valuation (Lesson 7) | 90 seconds | gate or valuation first |
| Magnitude, estimate, root or recurring decimal (Lesson 8) | 45 seconds | exponent first, then one estimate |
| Minimum count or extreme over choices (Lesson 9) | 120 seconds | enumerate the largest counts, then check the remainder |

## Three-pass control routine

- **Pass 1 (first sweep).** Answer each item whose property is visible in about 20 seconds: a test, a unit digit, a magnitude comparison. Leave everything else with a mark.
- **Pass 2 (middle items).** Apply the budget above. Use the method the lesson names, and stop at the budget even if the item is not finished. Mark a provisional choice.
- **Pass 3 (return).** Return to marked items with the remaining time. Use elimination only when the stem's property rules out options. Do not guess a number that you have not checked.

## Practice set rule

Eight items in ten minutes, drawn from one lesson or from a mixture. The gate is seven of eight in ten minutes. It is the learner's own gate, not an official cut-off.

## Marks-per-minute rubric

Each item carries 2.5 marks (200 / 80). At a budget of b seconds, a correct answer earns 150 / b marks per minute of working time. At 60 seconds that is 2.5 marks per minute, and at 30 seconds it is 5 marks per minute. Use the rubric to decide where to save time: the 30-second tests earn the most per minute, and a 120-second enumeration is worth attempting only when the counts or the column constraints are already visible.

Gate before optional Advanced work: seven of eight items in ten minutes, and seven of eight on a fresh set after corrections. The qualifying bar is 33 per cent of Paper II, which is 66 of 200 marks; recheck the current examination notification.

## Error codes for post-test analysis

| Code | Meaning | Example from this session |
|---|---|---|
| C | Condition error: the rule was applied where it fails | the 3-test used for a unique missing digit; a cycle reduced without the gate; greedy used for non-canonical coins |
| X | Execution slip: method right, arithmetic wrong | an off-by-one in a digit block or in a valuation term |
| T | Tool selection: a long calculation used where a property worked | computing 8^12 instead of comparing powers of 2 |
| R | Reading error: wrong digit, bound or base read from the stem | reading the 7-test subtraction as addition; reading the base as 8 |
| A | Interpretation: "or" read as "exactly one", "greatest" read as "least" | counting multiples of either divisor when exactly one was asked |
| G | Unsupported guess: an option chosen without a checked property | a remembered rule not verified on a second term |

Record each miss with its code and lesson. A code C or G miss sends you back to the lesson's failure condition before any new timed set.

# REMEDIATION

Each miss has one repair. Do the repair before you attempt a new timed set.

| Error code | Repair | Return to |
|---|---|---|
| C, condition | Write the rule's failure condition on a card, then solve one case where it fails (for example 12^9 mod 8, 4x5 for the 9-test). | the lesson named in the miss |
| X, execution | Recheck the final two lines of the calculation; verify with a second route (digit sum, residue list, or enumeration). | Lessons 2 to 5 |
| T, tool | Label the property first on five easy items (test, cycle, factor count, digit count, magnitude). | the matching lesson |
| R, reading | Underline the divisor, the base, the modulus and the exponent before any work. | Lesson 1 (bases), Lesson 4 (modulus), Lesson 7 (exponent) |
| A, interpretation | Write the operation word ("greatest", "least", "either", "exactly one") in the margin before computing. | Lessons 3 and 9 |
| G, guess | Stop guessing: state the rule, then check it on one more term or one more number. | Lesson 6 |

After a repair, retest with a fresh set of eight items from the same lesson, then from a mixed set.

# MASTER METHOD MAPS

| Stem signal | First move | Gate or condition | Lesson |
|---|---|---|---|
| "divisible by" a single divisor | apply the test for that divisor | base 10 for the digit tests; coprime halves for 6 and 12 | 1 |
| "how many factors" or "sum of factors" | full prime factorisation | distinct primes; exponent + 1; multiply the bracket sums | 2 |
| "is it prime" | test up to the square root | none | 2 |
| "a^2 - b^2 = N" | factor pairs of N with equal parity | d and e share parity | 2 |
| "sum of consecutive integers" | k times the mean | odd k gives a multiple of k | 2 |
| "triangular" positions of marks from one end | write the distances, check the increments, count inside the segment | count from the stated end | 2 |
| "greatest ... measures" or "greatest ... leaves the same remainder" | HCF (of differences, if remainders are equal) | remainder smaller than divisor | 3 |
| "least ... divisible by" or "when do they coincide" | LCM; count with floor(range / lcm) | none | 3 |
| "either ... or ... divisible" / "exactly one" | floor counts with lcm overlap | lcm, not product | 3 |
| "neither ... nor ... divisible" (Advanced part) | range minus the union | the overlap counted once | 3 |
| "remainder when" a product or power is divided | reduce each factor first | composite moduli by prime factors | 4 |
| "unit digit" of a power or a product | cycle of the base, n mod 4 | n >= 1; zero remainder means the fourth term | 4 |
| "how many digits" in a page or a range | block count | count digits, not numbers | 5 |
| "how many times does digit d appear" | column count | count occurrences, not numbers containing d | 5 |
| "sum of all k-digit numbers" from distinct digits | digit sum times (k - 1)! times R_k | all digits non-zero | 5 |
| missing digit, reversal or column puzzle | place-value equation, then the 9-test or enumeration | unique solution check | 5 |
| "next term", "missing term", "incorrect term" | difference table, then check | rule verified on one more term | 6 |
| "sum of the first N terms" of a repeating list | q x block sum plus the partial block | n = qp + r | 6 |
| "a * b" defined by examples | candidate rule must fit every example | reject any rule that fails one example | 6 |
| "remainder" of a large power | gate, then the period | gcd(base, modulus) = 1 | 7 |
| "exponent of a prime in" a factorial, or "trailing zeros" | Legendre sum; count 5s | base 10 only | 7 |
| "last non-zero digit" | remove the factors of 10, then the cycle of the rest | the unit digit of the remainder | 7 |
| "which is closest" or "which is larger" | exponent first; common base; one-significant-figure estimate | option gap larger than rounding error | 8 |
| "recurring decimal" as a fraction | a/9 or ab/99, or subtract to remove a prefix | no prefix for the simple form | 8 |
| "fewest items" to reach a total | enumerate the largest counts, then the remainder | denominations form a divisibility chain for greedy | 9 |
| "greatest" or "least" over distinct values | balance (fixed sum) or rearrangement (sum of products) | enumerate candidates when in doubt | 9 |

# COMPLETE CONSOLIDATED REGISTER NOTES

## Divisibility tests and the 9-test's limit (Lesson 1)

- Tests: 2, 5, 10 read the last digit; 4 the last two; 8 the last three; 3 and 9 the digit sum; 6 needs 2 and 3; 12 needs 3 and 4; 11 the alternating difference; 7 removes the last digit and subtracts twice it.
- Divisibility is a relation: a|b and b|a both hold only when a = b for positive integers. Implication is not equivalence.
- The 9-test fixes a missing digit uniquely only when the needed residue is non-zero; with residue 0 both 0 and 9 pass.
- A two-digit block written three times is the block times 10,101 = 3 x 7 x 13 x 37.
- Parity removes options only when the stem fixes the parity.

## Primes, factors, sums and consecutive integers (Lesson 2)

- Primes to 100: 25 of them; test up to the square root; 1 is not prime; 2 is the only even prime.
- Factor count = product of (exponent + 1); an odd count means a perfect square.
- sigma is multiplicative: sigma(12) = 7 x 4 = 28.
- a^2 - b^2 = (a - b)(a + b); pairs need equal parity; numbers of the form 4k + 2 fail.
- Sum of k consecutive integers = k times the mean; for odd k, a multiple of k; the first n integers sum to n(n + 1)/2.
- Triangular positions of marks: the increments are 2, 3, 4 and so on; count from the stated end.
- Torn leaf: with S_n = n(n + 1)/2 and R the remaining total, the removed pair sums to S_n - R = 2p + 1; the stem must fix n.
- Two-term unit-fraction count for 1/4 with p <= q: (5, 20), (6, 12), (8, 8). Integer pairs with a fixed sum k and p < q: floor((k - 1)/2); the first sum with two pairs is found by listing the counts floor((k - 1)/2) in order.

## HCF, LCM, counts and the Advanced part on numbers divisible by neither (Lesson 3)

- HCF takes the minimum exponent; LCM the maximum. HCF x LCM = product for two numbers only.
- Same remainder: HCF of differences, divisor above the remainder. Least number with remainder r: lcm + r.
- Coincidence count in a range: floor(range / lcm).
- Multiples in a range: floor values; exactly one: A + B - 2AB with AB from the lcm.
- Advanced: numbers divisible by neither = range minus (A + B - AB); 1 to 200 gives 200 - 44 = 156 for neither 6 nor 9.
- Common-value distributions: least total at the LCM of the multipliers (A = 2B = 5C gives 10, 5, 2, total 17; the chain A = 2B = 3C = 4D gives 12, 6, 4, 3, total 25). With the extra condition that every share is even, A = 2B = 5C gives 20, 10, 4, total 34. With a fixed total of 170, A = 4B = 6C gives V = 120, with B = 30 and C = 20.

## Remainders, cycles and repunits (Lesson 4)

- Residues combine under +, -, x and not under division.
- Unit-digit cycles of period 4 (2, 3, 7, 8), period 2 (4, 9), period 1 (0, 1, 5, 6); n mod 4 with zero meaning the fourth term.
- A composite modulus of distinct primes is satisfied by a product containing each prime.
- R_n = (10^n - 1)/9; R_3 = 111 = 3 x 37; R_5 = 11,111 = 41 x 271; 10^6 - 1 = 3^3 x 7 x 11 x 13 x 37.

## Digits, reversal and constraints (Lesson 5)

- Digits used by 1 to N in blocks; digit frequency is a column count; digit sum of 20 to 39 is 140; pages 1 to 200 use 492 digits; 252 digits run out at page 120.
- Reversal: N - R = 9(a - b), N + R = 11(a + b); the identity holds with b = 0, but the reversal then has one digit.
- Permutations of three distinct digits sum to 2 x 111 times their digit sum; three cyclic rotations sum to 111 times it.
- Permutations of k distinct non-zero digits: each digit fills each place (k - 1)! times, so the sum is (k - 1)! x digit sum x R_k; the digits 2, 3 and 6 give 2,442.
- Column constraints are checked digit by digit; a carry links each column to the next.

## Sequences and patterns (Lesson 6)

- Difference table: constant row gives the rule; second differences constant gives a quadratic rule.
- Interleaved strands separate before any search; square strands are common.
- Linear recurrence a(n+1) = p a(n) + q needs two pairs; Fibonacci-type needs two starts.
- Prime-step differences follow consecutive primes; prime-offset lists are tested term by term.
- Periodic blocks: n mod p; periodic sums: q S plus the partial block.
- Matrix rules: constant row sum or a cube rule, checked on every complete row.
- Derived operators: a candidate rule is accepted only if it fits every example; 2a + b - 1 fits 4 * 7 = 14 and 9 * 2 = 19.

## Large powers, valuations and products (Lesson 7)

- The gate: gcd(base, modulus) = 1 before any exponent reduction; otherwise list residues for a pre-period.
- Power towers: reduce from the top, one period at a time.
- Legendre: v_p(n!) = sum of floor(n/p^k); 40! has 38 factors of 2 and 9 trailing zeros in base 10, but 18 in base 6 through min(v_2, v_3).
- Product trailing zeros: the smaller of the 2- and 5-exponents; in 5 x 10 x ... x 40 the 5-exponent is 9 and the 2-exponent is 7, so the product has 7 trailing zeros.
- Last non-zero digit: remove the factors of 10, then take the unit digit of the rest by the cycles; 10! ends in 8 before its zeros.
- Last two digits: a product with two 2s and two 5s ends in 00; keep the leading zero.
- Factor out the smallest power before adding or comparing large powers.

## Magnitude, powers and roots (Lesson 8)

- Compare by exponent first; rewrite in a common base; a x 10^k has k + 1 digits when 1 <= a < 10.
- Do not square an inequality unless both sides are non-negative.
- For N^2 = a x 10^k with k even, N has k/2 + 1 digits for every a in [1, 10).
- Estimates separate options only when their gap exceeds the rounding error.
- Recurring decimals: a/9, ab/99; with a prefix, subtract (0.1(6) = 1/6; 0.1(27) = 7/55).
- Surds: simplify by the largest square factor; add only like surds; sqrt(50) = 5 sqrt(2).
- A square that is a cube is a sixth power; 64 is the only one between 50 and 500.

## Integer combinations and extremes (Lesson 9)

- Greedy is correct only for canonical denominations; for 3, 5 and 9 g, the 22 g target has two combinations; greedy takes 9 and 9 and cannot pay the last gram.
- Measuring cylinders: enumerate the largest counts; at most two pours from 4, 7 and 10 litres measure 14 litres in two ways.
- For a fixed sum, the product of two parts is largest when the parts are closest.
- For x and y, the sum of products is largest when sorted together and smallest when sorted in opposite orders.
- The first two-digit multiple of 7 with digit sum 10 is 28, found by an ordered search over candidates.

# COVERAGE MATRIX

Every row names the lesson that teaches the unit. The Basic and Advanced owner units are listed by their section numbers in the owners.

| Syllabus clause or owned unit | Lesson | MCQs or other evidence |
|---|---|---|
| Numbers and their relations: number universe (natural, whole, integer, rational, irrational, real) | 1 | prose and retrieval prompt |
| Basic owner section 2: divisibility by 2, 4, 5, 8, 10 | 1 | prose and worked items |
| Basic owner section 2: divisibility by 3 and 9; base-10 condition | 1 | 1 |
| Basic owner section 2: divisibility by 6 and 12; coprime halves | 1 | retrieval prompt |
| Divisibility by 7 and by 11 | 1 | 2, 3 |
| Repeated two-digit blocks written three times, and 10,101 | 1 | prose and worked item |
| Divisibility as a relation; implication and equivalence | 1 | prose |
| Parity as an eliminator | 1 | prose |
| Missing digit by a test; uniqueness | 1, 5 | 29 (cumulative) |
| Primes, primality test, primes to 100 | 2 | 7 |
| Factor count and odd factor count | 2 | 4 |
| Factor sums (sigma) | 2 | 5 |
| Difference of squares | 2 | 6 |
| Consecutive integers, means and sums; triangular numbers; torn leaf (page-sum route) | 2 | prose and worked items; 2014 Q22 approach in the linkage section |
| Unit-fraction solutions; prime progressions and prime expressions | 2 | prose and retrieval prompt |
| Integer pairs with a fixed sum (a labelled Core part of Lesson 3) | 3 | prose and worked example (k = 12) |
| Basic owner section 5.4 and must-know: HCF, LCM and HCF x LCM for two numbers | 3 | prose and worked examples; 30 (cumulative) for the LCM count |
| Same remainder and the HCF of differences | 3 | 8 |
| Least number with remainders; shared deficit | 3 | 10 |
| Multiples counts, overlap, either and exactly one (Basic owner section 5.4) | 3 | 9 |
| Advanced owner section 2: inclusion-exclusion, numbers divisible by neither (Advanced part) | 3 | prose and worked example (1 to 200) |
| Divisors leaving a given remainder | 3 | prose |
| HCF of fractions and decimals | 3 | prose and worked item |
| Common-value distributions: a least total, a fixed total, and an extra condition on the shares | 9 | prose and worked examples (10, 17, 120 and the even-share case 34) |
| Triples with fixed HCF and LCM; cube identity | 3 | prose |
| Residues, remainders and their arithmetic (Basic owner section 4) | 4 | 11, 12 |
| Unit digits and cycles (n mod 4) (Basic owner section 2) | 4 | 11 |
| Negative residues | 4 | prose |
| Composite moduli by prime factors | 4 | prose and worked item |
| Repunits and the 10^6 - 1 identity | 4 | 12 |
| Digits, place value and digit counts in blocks (Basic owner section 5.2) | 5 | 13 |
| Digit frequency by column | 5 | 14 |
| Digit sums by place | 5 | prose and retrieval prompt |
| Reversal algebra and reversal products | 5 | 15 |
| Permutation sums and cyclic sums | 5 | 16; k-digit permutation sums in prose |
| Digit divisibility counts | 5 | prose and retrieval prompt |
| Column constraints in cryptarithms (scope stated in Lesson 5) | 5 | prose, including a worked two-column example |
| Arithmetic and geometric rules; difference tables | 6 | 17 |
| Interleaved strands | 6 | prose and worked item |
| Linear and two-term recurrences | 6 | 18 |
| Prime-step and prime-offset lists | 6 | prose and worked items |
| Periodic blocks and periodic sums | 6 | 19 |
| Number matrices and figure rules | 6 | prose and worked item |
| Derived operators | 6 | prose and worked item (complete example) |
| Basic owner section 5.3 and Advanced owner section 4: large powers, the gate and pre-periods | 7 | 20 |
| Advanced owner section 3, Method 1: power towers | 7 | prose and worked item (Part C) |
| Advanced owner section 3, Method 2: factorial valuations (Legendre) | 7 | 22 |
| Basic owner section 5.2 and section 7: trailing zeros in base 10 and other bases; product valuations | 7 | 21, 23, 34 (cumulative) |
| Last non-zero digit | 7 | prose and worked example (10!) |
| Advanced owner section 3, Method 3: last two digits | 7 | prose (Part E) |
| Advanced owner section 4: sums of powers modulo a small number; factored powers | 7 | prose (Part F) |
| Orders of magnitude; powers of ten; scientific notation | 8 | 24 |
| Digit count of a power (scientific notation) | 8 | 26 (sixth powers) and 33 (cumulative) |
| Exponent laws and comparison of powers | 8 | prose and worked item |
| Perfect squares and perfect cubes; sixth powers | 8 | 26 |
| Square-root digit count | 8 | 25 |
| Bounding and estimation | 8 | prose and worked item |
| Recurring decimals | 8 | prose and worked item |
| Decimal place value after the point | 8 | prose and worked item |
| Roots, surds and irrational numbers | 8 | prose and worked item |
| Integer combinations: minimum counts of items | 9 | 27 |
| Extremes of a product of sums with distinct digits | 9 | 28 |
| Extremes over distinct values; rearrangement | 9 | prose |
| Ratio extremes | 9 | prose |
| Operator placement extremes | 9 | prose |
| Basic owner complete learner route, item 12 (verification by plugging back, parity, digit count, remainder and order of magnitude) | all lessons | each lesson's quick self-checks and the answer blocks of the MCQs |
| Basic owner section 11 timed Core drill and its diagnosis codes | timed set | TIMED-SET PRACTICE AND SCORING RUBRIC and REMEDIATION |
| Advanced owner section 8 drill (trailing zeros of 50!, multiples in 1 to 1000, 2^100 mod 9, 3^101 last two digits, exactly-one counts, 10^30 mod 16) | 3, 7 | the methods are taught in Lessons 3 and 7; the drill items are not reproduced |
| Advanced owner section 9 (PYQ-pattern notes: unit digits, large-power remainders, HCF and LCM word problems, trailing zeros, factor counts, number series) | 2, 3, 4, 6, 7 | the linkage section and the PYQ reconciliation table |
| Cumulative combinations | cumulative | 29-34 |

PYQ type coverage: every one of the 133 linked items is assigned to one lesson in the linkage section, and the seven cross-linked items are named there with the neutral step this session teaches. The per-lesson counts are reported there.

# SOURCE LEDGER

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical markdown | checked | upsc-ai-kit/knowledge/CSAT/basic/02_Number-Systems-and-Number-Sense.md read in full (549 lines); upsc-ai-kit/knowledge/CSAT/advanced/02_Number-Systems-and-Number-Sense.md read in full (322 lines); upsc-ai-kit/knowledge/CSAT/00_Master-Framework.md read for the qualifying-bar and attempt rules |
| Final learner package | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule; no file in that category was opened, cited or compared |
| Layered/complete session | not available | No non-excluded layered or complete CSAT session for this topic exists in the live-session tree; none was opened |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule; the solved-question library was used only to count, check and link stems (recorded under PYQs through 2026) |
| Advanced dossier | checked | upsc-ai-kit/knowledge/CSAT/advanced/02_Number-Systems-and-Number-Sense.md read in full (322 lines), including the power-tower, factorial, last-two-digit, gate and inclusion-exclusion sections |
| OCR books | not available | books/ holds only previous-paper PDFs (books/previous_papers_2013_2018) and no OCR book on number systems; no OCR book reference was consulted for this topic, and the book context is recorded as not available in each lesson |
| PYQs through 2026 | checked | Ledgers upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2018-2023.md, _PYQ-ROUTING-CSAT-2024-2025.md and _PYQ-ROUTING-CSAT-2026.md read for family-02 rows; linked stems were extracted by script from solved_pyqs/papers/2013 to 2026 prelims-csat.md, keeping stem text only with solution, key and answer lines filtered out by line prefix; 2018 to 2023 official keys not held locally; 2024 and 2025 keys supplied locally but not recorded; 2026 keys provisional and not used. Incidental exposure, disclosed: while locating stems in an earlier pass, one printed excerpt displayed the final-answer line of 2023 Q17 and solution-section headings; none of that text is used in this file, its MCQs or this ledger |
| Official live sources | not relevant | Aptitude paper with no current-affairs component; syllabus clause taken from the repository syllabus transcription |

## Reading record

- In this pass the full live-session generation rules file (live_sessions/LIVE-SESSION-GENERATION-RULES.md, all 1,150 lines) and the three instruction files (instructions/GENERATION-OPTIMIZATION-AND-INTEGRITY.md, instructions/LIVE-SESSION-VALIDATION-AND-RELEASE.md and instructions/README.md) were read in full.
- live_sessions/LIVE-SESSION-GENERATION-RULES.md, instructions/README.md, instructions/GENERATION-OPTIMIZATION-AND-INTEGRITY.md and instructions/LIVE-SESSION-VALIDATION-AND-RELEASE.md: read in full before the repair.
- tools/validate_live_session.py: read in full, including the CSAT MCQ block pattern, the answer-neutral PYQ check, the final arc and the source-manifest parser.
- Owners: upsc-ai-kit/knowledge/CSAT/basic/02 and advanced/02, both in full.
- Master framework: upsc-ai-kit/knowledge/CSAT/00_Master-Framework.md, for the qualifying bar and the attempt rules.
- Structure reference only: live_sessions/CSAT/05-Algebra-Inequalities-and-Data-Sufficiency/Learning-Session-Live-Edition.md, its headings and its labelled Core and Advanced parts. No content was copied.
- Not opened: any artifact of the excluded learner-package families, any learning-sessions folder, and any final learner package.

## PYQ reconciliation

| Year | Library routes here | Ledger routes here | Linked in this session | Cross-linked |
|---|---:|---:|---:|---:|
| 2013 | 6 | not in ledger | 4 | 2 (Q31, Q60) |
| 2014 | 6 | not in ledger | 6 | 0 |
| 2015 | 4 | not in ledger | 3 | 1 (Q79) |
| 2016 | 5 | not in ledger | 4 | 1 (Q40) |
| 2017 | 7 | not in ledger | 7 | 0 |
| 2018 | 2 | 2 | 2 | 0 |
| 2019 | 8 | 8 | 8 | 0 |
| 2020 | 17 | 17 | 17 | 0 |
| 2021 | 10 | 10 | 10 | 0 |
| 2022 | 11 | 11 | 11 | 0 |
| 2023 | 18 | 17 | 17 | 3 (Q26, Q40, Q69) |
| 2024 | 13 | 13 | 13 | 0 |
| 2025 | 19 | 19 | 19 | 0 |
| 2026 | 12 | 12 | 12 | 0 |
| Total, 2013 to 2017 | 28 | not in ledger | 24 | 4 |
| Total, 2018 to 2026 | 110 | 109 | 109 | 3 |
| Total | 138 | 109 (2018 to 2026) | 133 | 7 |

The library count for 2018 to 2026 (110) and the ledger count (109) differ by the 2023 disagreement described below. The per-year totals reconcile to the library topic page and to the three ledgers, with that single difference.

## Ledger notes on routing disagreements

- **2023, library against the ledger, both directions.** The ledgers route Q47 (permuted-digit number sum) and Q76 (digit cryptarithm solved column by column) to this topic, family 02. The library routes Q47 and Q76 to the logical-reasoning family (topic 06). This session follows the ledger and teaches them: Q47 in Lesson 5 (k-digit permutation sums) and Q76 in Lesson 5 (column-by-column cryptarithm). The library's routing for these two items is disclosed here as a residual disagreement.
- **2023, the library routes Q26, Q40 and Q69 here; the ledgers route them elsewhere.** The ledger routes Q26 to the algebra family and Q40 and Q69 to the logical-reasoning family. These three items are cross-linked in the linkage section, with the neutral step this session teaches. They are not counted in the 133 linked items.
- **Owner tables against the ledger.** The basic owner's 2018 to 2023 table lists Q47 and Q76 under this topic, consistent with the ledger. The advanced owner routes 2023 Q76 to topic 06 as a cross-owner reference, and routes 2021 Q59 and Q60 to topic 06 as well. This session follows the ledger for these items and teaches only the number-property parts: digit constraints and column carries in Lesson 5.
- **Sequence items.** The advanced owner marks 2019 Q48 and Q51, 2021 Q26 and Q50, and 2022 Q4 and Q75 as cross-owner references to the sequence family. The ledgers route them to this topic. This session teaches the number-property parts (prime-step lists, square strands, difference tables and recurrences) in Lesson 6, and does not teach the wider sequence family.
- **Key status.** The 2018 to 2023 official keys are not held locally; the 2024 and 2025 keys are supplied locally but not recorded here; the 2026 keys are provisional. No key, answer letter or inferred answer for any linked item is recorded in this file.

## Owner defects and their fixes in this session

| Owner location | Defect or claim checked | Fix taught here |
|---|---|---|
| basic/02, divisibility rules section | "only one holds unless a = b" and "implication, not an equivalence" are not correct as stated | Lesson 1 states that a divides b and b divides a both hold only when a = b, and gives the implication and equivalence pair |
| basic/02 and advanced/02, trailing-zero rows | the trailing-zero rule is stated without the base-10 condition in places | Lesson 7 states base 10 at every use and gives a base-6 example |
| basic/02, parity rows | parity is treated as always safe as an eliminator | Lesson 1 limits parity to stems that fix the parity |
| basic/02, the 7-test | the owner does not state a 7-test rule in any section, although the 7-test is in the syllabus scope | Lesson 1 teaches the 7-test from its standard subtract-twice method, with a worked check |
| basic/02 and advanced/02, headers | "grounded in 2024 to 2026" omits the earlier years of the routed questions | the session cites 2013 to 2026 |
| basic/02, scope and boundary text | the boundary places sequences and cryptarithms outside the topic while the scope claims number series | Lessons 5 and 6 teach the number-property parts only; letter, shape and coding series are excluded and the scope is stated at the top of the session |
| basic/02, scope text | roots, surds and magnitude are claimed but not taught in the earlier session | Lesson 8 teaches roots, surds, magnitude and bounding |
| basic/02 and advanced/02, digit-count and reversal rows | the reversal identity is stated with a condition that is not needed for the identity itself | Lesson 5 states the identity and the single condition that matters, that the reversal of 10a is one digit when b = 0 |
| basic/02, complete learner route, item 11 (magnitude and estimation) | the owner's estimation point is a route item, not a worked doctrine | Lesson 8 teaches bounding and one-significant-figure estimation with its direction of error |
| advanced/02 has no estimation row | the earlier ledger cited an estimation row in advanced/02 that the owner does not contain | the citation is corrected to the basic owner's route item 11 |
| advanced/02 has no 9-test uniqueness row | the earlier ledger cited a 9-test uniqueness row in advanced/02 that the owner does not contain | the point is stated as a derived correction in Lessons 1 and 5: a missing digit fixed by the 9-test is unique only when the needed residue is non-zero |
| advanced/02, inclusion-exclusion | "divisible by neither" is listed as a trap but not taught as a method | Lesson 3 teaches it as a labelled Advanced part, with a worked example and its failure condition |

## Verification of the MCQs and worked items

- Every MCQ key, option and explanation was recomputed in Python from the same data that renders the file, and the rendered file was re-parsed line by line. Keys rotate A, B, C, D by MCQ number; the explanation tagged Correct is the key in all 34 items.
- No correct option is the arithmetic midpoint of two others; no four options form an arithmetic run; all 102 incorrect explanations are unique; every numeric option lies in the stem's domain, and a numeric option never contradicts the stem's stated premise (for example MCQ 10 now offers only counts below 1,000, as the stem says).
- Length metric. Word counts (whitespace tokens) are a letter-order artefact: every option is a single numeral, so all word counts tie, and the word rank is not reported as evidence. The non-space character rank is the metric. Thirteen items are tie-only (all options the same length: MCQ 11, 12, 14, 15, 16, 17, 19, 21, 22, 28, 31, 33 and 34); they are flagged and excluded from the statistics below.
- Among the 21 informative items the correct option's character rank is 1 in 3 items, 2 in 8, 3 in 6 and 4 in 4. No four consecutive informative items fall in one half; there is no run of three shortest or three longest correct options; there is no 1-4 or 4-1 alternation of length four or more. Key letter against rank among informative items: A gives ranks 3, 2, 2, 2, 1, 1; B gives 1, 3, 3, 2, 2, 4; C gives 4, 3, 2, 3; D gives 4, 2, 3, 4, 2. No letter is tied to one rank.
- Repeated blocks. Among the informative items short rank patterns recur (for example the pair 1, 4 at items 2 and 3 and again at 29 and 30, and the pair 2, 3 at items 5 and 6, 9 and 10, and 26 and 27). These repeats are short, are not a strict run or a period, and are reported here as a residual rather than removed.
- Magnitude rank of the correct option among informative items: 1 in 1 item, 2 in 6, 3 in 8 and 4 in 6. Middle ranks still hold 14 of 21; this is a residual.
- The correct explanation is the longest of the four in 7 of 34 items by non-space characters.
- Teaching examples kept as canonical textbook method forms, with parameters and answers that differ from the linked questions (kept deliberately, not overlooked): the page-count and printer examples, the digit sum over a range of numbers, the repunit square, five consecutive integers modulo 35, strictly decreasing digits in a range, the recurring decimal with a repeating block, the least addition to reach a square, trailing zeros of a product of multiples of 5, and the 10^m x n valuation example. Practice items were held to the stricter test: each practice item asks for a quantity that differs from the linked questions in its family.
- Worked items and claims were recomputed in Python for this pass: the repeated-block factorisations (141,414 = 14 x 10,101; 10,101 = 3 x 7 x 13 x 37), the digits 2, 4 and 9, the unit-fraction pairs for 1/4, 19 x 20 x 21 x 22 x 23 and 11 x 12 x 13 modulo 30, R_3 = 111 and R_5 = 11,111, 111^2 = 12,321, the 3:8 reversal pair (27, 72), the digit sums of 20 to 39, the page counts (1 to 200 = 492; 252 digits = 120 pages; 1 to 330 three-digit pages = 231), the digit-0 count (86 numbers containing a zero in 1 to 500; 91 zeros written), the strictly decreasing numbers from 200 to 499 (10), the common-value totals 17, 34 and 120 (and 25 for the multiplier chain), the coincidence count for periods 5, 6 and 8 (2 within 250 days), the least number above 400 with remainder 2 (422), numbers divisible by neither 6 nor 9 up to 200 (156), the interleaved strands (1, 4, 8, 9, 27, 16, next 64), the recurrences (3, 13, 53, 213, next 853; 3, 1, 4, 5, 9, next 14), the prime-step lists (next 79 and 72 for the stated lists; next 34 and 36 for the offset lists), the difference and constant rules, the derived operator rule 2a + b - 1, 4,608 and 16,250 factorisations, 120! (exponent of 5 is 28), 500! and the exponent difference 370, the MCQ values (89 as the largest inner side for area 360; 927 below 1,000; 2^n mod 20 counts; 3d54 divisibility counts; 8^n unit digits; 7^100 mod 100 = 1; odd permutations of 1, 4, 8; the 47 g coin combinations, 7 in all).
- No independent blind reader was used for the MCQs. The independent controller review remains required.

## What was not done

- No independent review is claimed for this session. The hostile self-audit and the validator result are reported in the handoff, not here.
- No owner file, index, rules file, tool or other session was edited. No git write was run.
- Tie-only items (13 of 34: items 12, 14, 15, 16, 17, 19, 21, 22, 28, 29, 31, 33, 34) are not fixed: for unit-digit, remainder and small-count items, a single-digit or same-length option set is the natural form, and varying lengths would need unnatural values. They are flagged in this ledger and excluded from the informative statistics, as the controller decision allows.
- Magnitude ranks remain middle-heavy among informative items (12 of 19 in ranks 2 and 3). Making more keys extreme would need named errors that are larger or smaller than the answer by construction; this was not forced.
