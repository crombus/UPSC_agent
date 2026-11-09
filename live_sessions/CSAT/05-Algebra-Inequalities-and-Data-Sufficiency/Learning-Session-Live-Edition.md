# Algebra, Inequalities and Data Sufficiency - Learning Session Live Edition

**Paper:** CSAT (Civil Services Preliminary Examination, Paper II) | **Format:** four-option objective items only; there is no Mains component in this paper | **Practice in this session:** multiple choice, answered in a separate block after each item

This session teaches the algebra that the paper uses in two different ways. In some items you must find a value: translate a sentence, solve the relation, and choose the number. In others you must decide whether information is enough: a data-sufficiency item asks whether a question is pinned down, not what the value is. Both skills rest on the same discipline. Name the unknown, state the domain, respect every sign and denominator, and check the answer by a second route before you choose an option.

Work through the lessons in order. Each lesson builds on the one before it, and each ends with a few original items that test the method and its common failure rather than the memory of a term. Attempt each item before you open its explanation.

Your personal target is a learning goal, not an official cut-off. The timed-set section explains how to use it.

## Roadmap

| # | Lesson | Stage | Depends on | Practice items |
|---:|---|---|---|---:|
| 1 | Words to equations: variables, domains, ages, digits, consecutive integers, sum-difference and marking schemes | Foundation | Basic arithmetic of signs and fractions | 3 |
| 2 | Simultaneous equations: independent, dependent and inconsistent systems | Foundation to Core | Lesson 1 | 4 |
| 3 | Inequalities: sign flips, denominators, chains, coded inequalities and ranges | Core | Lessons 1 and 2 | 2 |
| 4 | Absolute value, squares and surds: two branches and the unique-root test | Core, with Advanced Parts C and D | Lesson 1 (solving one unknown) | 3 |
| 5 | Quantitative comparison: equal forms, powers, surds, ratios, fractions and percentages | Core, with Advanced Part C | Lessons 3 and 4 | 4 |
| 6 | Bounds and optimisation: AM-GM, integer optima and interval corners | Core and Advanced | Lessons 3 and 5 | 2 |
| 7 | The data-sufficiency format: printed options, verdicts and necessary versus sufficient | Core | Lessons 2 and 3 | 3 |
| 8 | The data-sufficiency procedure: testing the question, each statement and both together | Core, with Advanced Parts C and D | Lessons 2, 4 and 7 | 4 |
| 9 | Data-sufficiency families: digits, ages, primes, factor counts, parity, shares and set membership | Core and Advanced | Lessons 1, 2 and 8 | 3 |

After the nine lessons come six cumulative items, four of which join methods from two or more lessons, followed by the timed-set routine, remediation, the master method maps, the consolidated register notes, the coverage matrix and the source ledger.

---

## Lesson 1 - Words to equations: variables, domains, ages, digits, consecutive integers, sum-difference and marking schemes

Progress: 1/9 | Stage: Foundation | Subtopic: Words to equations

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the translation pipeline

```text
SENTENCE            NAME               DOMAIN               RELATION            SOLVE       CHECK IN WORDS
"a number,    ->  x = the number  ->  x is a positive  ->  x + 7 = 4(x - 2)  ->  x = 5  ->  5 + 7 = 12 and
 increased by      (unit stated)      integer?             one clause,                     4 x (5 - 2) = 12
 7, equals..."                                             one line
```

Read the pipeline from left to right, and do not skip a box. Most errors in this family are translation errors. The algebra after the relation is usually routine. The three boxes before it, the name, the domain and the relation, decide whether the algebra answers the question that was asked.

A small table holds the phrases that carry the arithmetic.

```text
PHRASE                    SYMBOL            CAREFUL READING
"is" / "equals"           =                 the two sides balance
"more than" / "increased" +                 order matters: "x is 3 more than y" is x = y + 3
"less than" / "decreased" -                 order reverses: "7 less than x" is x - 7, not 7 - x
"times" / "of"            x                 "four times (x - 2)" needs brackets around x - 2
"per" / "each"            rate or unit      keep the unit with the variable
```

### Plain intuition

A word problem is a sentence written in ordinary language that the arithmetic cannot yet read. The job is to translate it. You do not start by guessing the answer or by moving numbers about. You start by deciding what the unknown stands for, because every later line depends on that choice.

Think of the variable as a labelled box. If you write "x" without saying that it means the number of marks, or the age of the son in years, then a later step may quietly change what the box holds. A clear label is cheap insurance.

### Doctrine: three rules before any algebra

- **Define the unknown.** Write one sentence: "Let x be the son's age in years." The unit and the subject are part of the definition.
- **State the domain.** Whole numbers, positive integers, even integers, two-digit numbers, and non-zero denominators are constraints that the answer must satisfy. A root that is a fraction is wrong when the question counts people or pages.
- **Count the relations.** One unknown needs one independent relation. Two unknowns need two independent relations, and finding and checking such a pair is a skill of its own. For now, make sure every sentence in the problem has been turned into exactly one relation, and that the relation uses the same unit throughout.

### Step-by-step method

1. Name the unknown in a full sentence, with its unit.
2. Write the domain: integer, positive, even, digit, or non-zero.
3. Translate each clause into one line, keeping the order of "more than" and "less than" exact.
4. Solve the single relation, keeping the domain in view.
5. Check the answer in the original words, not only in the equation.

### Worked example before the shortcuts: the single linear relation

Solve 3x + 5 = 20 first: subtract 5, so 3x = 15, and divide by 3, so x = 5. Check: 3 x 5 + 5 = 20. A second example with a negative constant: solve 4x - 7 = 9. Add 7 to both sides: 4x = 16. Divide by 4, a positive number: x = 4. Check: 4 x 4 - 7 = 9. The one domain condition is that the coefficient of x is not zero. With 0x + 5 = 9 there is no solution, and with 0x + 9 = 9 every value works, so a zero coefficient changes the kind of answer, not only its value.

Now a sentence with a bracket. A number decreased by 4 equals twice the number increased by 2. Let x be the number: x - 4 = 2(x + 2). Expand: x - 4 = 2x + 4, so x = -8. Check: -8 - 4 = -12, and 2(-8 + 2) = -12. Dropping the bracket gives x - 4 = 2x + 2, and then x = -6, which fails the sentence: -6 - 4 = -10, while twice (-6 + 2) is -8.

### Shortcut 1: a linear word relation

- **Rule.** Translate the whole sentence before solving. A number increased by 7 equal to four times the number decreased by 2 becomes x + 7 = 4(x - 2).
- **Worked example.** Expand the bracket: x + 7 = 4x - 8, so 3x = 15 and x = 5. Check in words: 5 increased by 7 is 12; 5 decreased by 2 is 3; four times 3 is 12. The two sides agree.
- **Failure condition.** The method fails when the brackets are dropped. Writing "four times x minus 2" as 4x - 2 changes the equation, and in this example gives x = 3, which does not satisfy the original sentence: 3 + 7 = 10, while 4 x 1 = 4.

### Shortcut 2: reversed order in "less than"

- **Rule.** "A is 7 less than B" means A = B - 7. The phrase "less than" names the number that is subtracted, and it comes after the amount it is subtracted from.
- **Worked example.** "A number is 7 less than 19" gives x = 19 - 7 = 12. "Seven less than a number is 12" gives x - 7 = 12, so x = 19. The same two numbers are used, and the order of the words decides the equation.
- **Failure condition.** Reversing the order produces 7 - x = 12, which gives x = -5. The sign of the answer is an early warning that the order was reversed.

### Shortcut 3: ages with a shift in time

- **Rule.** Write each person's age now, and then write both ages after the same number of years. The shift in time applies to both people.
- **Worked example.** A father is four times as old as his son. In 12 years the father will be twice as old as the son. Let the son's age be s. Then 4s + 12 = 2(s + 12), so 4s + 12 = 2s + 24, 2s = 12, and s = 6. The father is 24. Check: in 12 years the son is 18 and the father is 36, and 36 = 2 x 18.
- **Failure condition.** The method fails when the shift is added to only one person, or when the future and present ages are mixed. Write the time shift as a separate line so that both ages receive it.

### Shortcut 4: digits and place value

- **Rule.** A two-digit number with tens digit t and units digit u is 10t + u, not the product tu. The reversed number is 10u + t.
- **Worked example.** The digits of a two-digit number sum to 11, and the tens digit exceeds the units digit by 3. Then t + u = 11 and t - u = 3, so t = 7 and u = 4. The number is 74. Check: 7 + 4 = 11, and 7 - 4 = 3.
- **Reversal identity.** The original number minus its reversal is (10t + u) - (10u + t) = 9(t - u). A reversal that changes the number by 27 therefore means t - u = 3. This identity is often faster than writing both numbers out.
- **Failure condition.** The digits must be whole numbers from 0 to 9, and the tens digit of a two-digit number cannot be 0. An algebraic answer such as t = 7.5 is not a digit, and the problem must be solved again with the domain stated.

### Undoing a chain of steps

Some problems apply the same step several times and ask for the start. Work backwards: undo the last step first, then the one before it. A pile is halved and then 4 more are added, and the final pile is 22. Undo the last step: before adding 4 there were 18. Undo the halving: before halving there were 36. Check forwards: 36 halved is 18, plus 4 is 22.

- **Failure condition.** Undoing in the wrong order, or undoing an addition by adding it again, gives a wrong start. The undo of halving is doubling, and the undo of adding 4 is subtracting 4.
- **Limit.** The method needs each step to be reversible; a step that discards information, such as rounding down, cannot be undone uniquely.

### Shortcut 5: consecutive integers

- **Rule.** Consecutive integers differ by 1: n, n + 1, n + 2. Consecutive even or odd integers differ by 2: n, n + 2, n + 4.
- **Worked example.** Three consecutive even integers have sum 54. Then n + (n + 2) + (n + 4) = 54, so 3n + 6 = 54, n = 16, and the integers are 16, 18 and 20. Check: 16 + 18 + 20 = 54.
- **Failure condition.** Using a step of 1 for even integers produces an odd sequence and a wrong sum. The step is part of the definition, so state it before writing the equation.

### Shortcut 6: sum and difference

- **Rule.** If two numbers have sum S and difference D, with the larger number first, then they are (S + D)/2 and (S - D)/2.
- **Worked example.** Sum 30 and difference 8 give (30 + 8)/2 = 19 and (30 - 8)/2 = 11. Check: 19 + 11 = 30 and 19 - 11 = 8.
- **Failure condition.** For integer answers, S and D must have the same parity, that is, both even or both odd. Sum 30 and difference 9 give 39/2 = 19.5 and 21/2 = 10.5. No pair of integers has that sum and difference, so the problem has no integer solution, even though the formula produces numbers.

### Shortcut 7: two prices and a fixed count

- **Rule.** Let a be the number of one kind of item and b the number of the other, with a + b fixed. The total is the sum of the two products, so write it as a relation in one unknown. A marking scheme is the same bookkeeping: attempted = correct + wrong, and the score is the marks per correct answer times the correct count, minus the penalty per wrong answer times the wrong count.
- **Worked example.** A bill of 550 rupees is paid by 7 people. Adults pay 150 rupees each and children pay 50 each. Let a be the number of adults, so the number of children is 7 - a. Then 150a + 50(7 - a) = 550, so 100a = 200 and a = 2. Check: 2 x 150 + 5 x 50 = 550.
- **Failure condition.** The number of people is not the number of adults. Using 7 as the count of adults, or reading the total as the price of one person, is the usual slip. The number of children is still 7 - a, and a non-whole answer means a price or the total was misread.

### The strongest wrong method and the reply

The tempting wrong method in this lesson is to read "x is 3 more than y" as y = x + 3. The sentence is about x, so x is the quantity that is 3 more than something, and x = y + 3. The reply is to read the subject of the sentence first, and then decide which side of the equation it belongs on.

A second wrong method is to solve the words by guessing values and stopping when one fits. Testing a value against every clause is a valid check: it confirms a candidate, but it does not replace writing the relation first. As a substitute for the relation, however, a guess can hide a wrong reading of the sentence. The reply is to write the relation first, and then use a test value only to confirm it.

### UPSC application

Items in this family ask you to translate a short story into one relation, and to keep the domain of the answer. The common families are ages, digits, consecutive integers, sums and differences, and marking schemes. In each case the work has three parts: define the unknown, write the relation in the stated order, and check the answer against the domain. A marking-scheme item is solved in the same way as an age item, with c and w as the two unknowns and the total score as the stated relation.

### Revision points

- Name the unknown in a sentence, with its unit, before writing any equation.
- Translate "more than" and "less than" with the order of the words, not the order of the numbers.
- Brackets are needed around "four times (x - 2)"; dropping them changes the equation.
- In an age problem, apply a time shift to both people.
- A two-digit number is 10t + u, and its reversal changes it by 9(t - u).
- Consecutive even or odd integers differ by 2; state the step before writing the sum.
- Sum S and difference D give (S + D)/2 and (S - D)/2, which are integers only when S and D have the same parity.
- A marking scheme uses attempted = correct + wrong, not the total number of questions.
- Check every answer in the original sentence, not only in the equation.
- A root that is not a whole number, a digit, or a count is not a valid answer to a counting question.

Two relations linked to the same two unknowns may pin a single answer, leave a whole family of answers, or contradict each other. Deciding which case you are in is the job that follows.

### Practice

**MCQ 1**

A number reduced by 5 is equal to three times the number increased by 1. What is the number?

- A. x = -4
- B. x = 1
- C. x = -3
- D. x = 8

**MCQ 1 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The relation is x - 5 = 3(x + 1), so x - 5 = 3x + 3, -8 = 2x and x = -4. Check: -4 - 5 = -9 and 3(-4 + 1) = -9.
- **B — Incorrect:** Reads "reduced" as "increased", giving x + 5 = 3(x + 1), which yields x = 1. The direction of the change is part of the sentence.
- **C — Incorrect:** Drops the bracket and reads three times the number, plus 1: x - 5 = 3x + 1, which gives x = -3. The 1 must be multiplied by 3 along with the number.
- **D — Incorrect:** Reverses the sentence, so the increased number equals three times the reduced number: x + 1 = 3(x - 5), which gives x = 8.

**MCQ 2**

The digits of a two-digit number add up to 12. When its digits are reversed, the new number is 18 more than the original. What is the original number?

- A. 75 (tens digit 7)
- B. 57 (tens digit 5)
- C. 84 (tens digit 8)
- D. 48 (tens digit 4)

**MCQ 2 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Reports 75, the reversal of the correct answer. Its digits do add to 12, but reversing 75 gives 57, which is less than 75. The condition that the reversal is 18 more than the original fails.
- **B — Correct:** Let the tens digit be t and the units digit u. Then t + u = 12 and (10u + t) - (10t + u) = 18, so 9(u - t) = 18 and u - t = 2. Solving gives t = 5 and u = 7. The number is 57, and its reversal 75 is 18 more.
- **C — Incorrect:** Takes 84, whose digits also add to 12. Its reversal, 48, is 36 less than 84, so the reversal is not 18 more. Reading the condition as a difference of 36 doubles the 18 and produces this value.
- **D — Incorrect:** Takes 48, the reversal of 84. Reversing 48 gives 84, which is 36 more than 48, not 18 more, so the condition fails in the other direction.

**MCQ 3**

A tank is empty at the start. A tap fills it at 6 litres per minute, and a leak empties it at 2 litres per minute. After how many minutes does the tank hold 48 litres?

- A. 24 minutes
- B. 8 minutes
- C. 12 minutes
- D. 6 minutes

**MCQ 3 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Ignores the leak and divides 48 by the leak rate, 48 / 2 = 24. The leak removes water, so the net filling rate is smaller than the tap rate alone.
- **B — Incorrect:** Ignores the leak and divides 48 by the tap rate, 48 / 6 = 8. The leak still runs while the tank fills, so the tap alone does not give the time.
- **C — Correct:** The net rate is 6 - 2 = 4 litres per minute. Then 4m = 48, so m = 12. Check: 6 x 12 - 2 x 12 = 72 - 24 = 48.
- **D — Incorrect:** Adds the two rates, 6 + 2 = 8, and divides 48 by 8 to get 6. The leak drains the tank, so its rate is subtracted, not added.

---

## Lesson 2 - Simultaneous equations: independent, dependent and inconsistent systems

Progress: 2/9 | Stage: Foundation to Core | Subtopic: Simultaneous equations

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: three ways two relations can behave

```text
TWO LINEAR RELATIONS:   a1 x + b1 y = c1          a2 x + b2 y = c2

                      compare the ratios  a1/a2 , b1/b2 , c1/c2
                                   |
        +--------------------------+---------------------------+
        |                          |                           |
  a1/a2 != b1/b2            a1/a2 = b1/b2 != c1/c2      a1/a2 = b1/b2 = c1/c2
  UNIQUE solution           INCONSISTENT                 DEPENDENT
  the lines cross once      the lines are parallel      the two relations are
                            no common point, so          one relation written
                            no solution                  twice: infinitely many
```

Read the diagram from the top. The three ratios decide the case. When the x and y coefficients are not in the same ratio, the lines cross once. When they are in the same ratio but the constants are not, the lines are parallel. When all three ratios agree, the second relation is a scaled copy of the first.

### Plain intuition

Each linear equation in two unknowns is a straight line of possible pairs. Every pair (x, y) on the line satisfies that one sentence and no other. Two sentences together describe the points that lie on both lines. Usually that is one point. Sometimes the lines never meet. Sometimes they are the same line, and every point on it works.

This is why a system can have a unique answer, no answer, or infinitely many answers. The question is not whether the algebra is hard. The question is how the two relations are related to each other.

### Doctrine: the three cases

- **Independent (unique solution).** The two relations contain different information. The ratio of the x-coefficients differs from the ratio of the y-coefficients. The pair fixes one point.
- **Inconsistent (no solution).** The coefficients are in the same ratio, but the constants are not. The left sides are scalar multiples, and the right sides disagree. No pair can satisfy both.
- **Dependent (infinitely many solutions).** All three ratios agree. One relation is a scalar multiple of the other, and it adds nothing new.

### Method 1: elimination

- **Rule.** Multiply one or both equations by constants so that one unknown has the same coefficient in both. Add or subtract to remove it. Solve for the other unknown, then substitute back.
- **Worked example.** A shop sells notebooks at n each and pens at p each. Three notebooks and two pens cost 26, and one notebook and four pens cost 22. Then 3n + 2p = 26 and n + 4p = 22. Multiply the second equation by 3: 3n + 12p = 66. Subtract the first: 10p = 40, so p = 4. Substitute: n + 16 = 22, so n = 6. Check: 3 x 6 + 2 x 4 = 26 and 6 + 4 x 4 = 22.
- **Failure condition.** Elimination fails only in the sense that it exposes the three cases. If, after elimination, the unknown disappears and a false statement remains, such as 0 = 4, the system is inconsistent. If both unknowns disappear and 0 = 0 remains, the system is dependent.

### Method 2: substitution

- **Rule.** Solve one equation for one unknown and insert the result into the other equation.
- **Worked example.** From x + y = 10, y = 10 - x. Substitute into x - y = 4: x - (10 - x) = 4, so 2x = 14, x = 7 and y = 3. Check: 7 + 3 = 10 and 7 - 3 = 4.
- **Failure condition.** Substitution creates fractions quickly when a coefficient is not 1. Choose the variable with the simplest coefficient, and keep the fractions until the final step.

### Method 3: option testing

- **Rule.** When the answer is given as a set of options, substitute each option into both equations. An option is correct only if it satisfies every equation.
- **Worked example.** For x + y = 10 and x - y = 4, the pair (7, 3) satisfies both equations, but (6, 4) satisfies the sum only, because 6 - 4 = 2.
- **Failure condition.** Testing only the first equation is the most common error. A pair that satisfies one equation but not the other is an attractive distractor, and it must be rejected. Option testing confirms a candidate; it does not prove that no other pair works. For a count of solutions, use the ratio test or elimination.

### Worked example: an inconsistent system

Take 3x + y = 11 and 6x + 2y = 20. The ratios of the x and y coefficients are 3/6 = 1/2 and 1/2, and the ratio of the constants is 11/20. The first two agree but the constants do not, so the system is inconsistent. Elimination confirms it: multiply the first equation by 2 to get 6x + 2y = 22, and that cannot equal 20. There is no pair that satisfies both.

### Worked example: a dependent system

Take 3x + y = 11 and 6x + 2y = 22. The second equation is twice the first. Every point on the first line satisfies the second. For instance, x = 3, y = 2 works in both, and so does x = 2, y = 5: 3(2) + 5 = 11 and 6(2) + 2(5) = 22. The system has infinitely many solutions, and the two relations describe the same line.

### Example with limits: a non-linear system

Take x + y = 7 and xy = 10. This is not a linear system, so the ratio test does not apply. Substituting y = 7 - x gives x(7 - x) = 10, which is x^2 - 7x + 10 = 0, with roots 2 and 5. The ordered pairs are (2, 5) and (5, 2), so there are two solutions, not one. When the question asks for a value that is the same for both pairs, such as x^2 + y^2 = (x + y)^2 - 2xy = 49 - 20 = 29, the pair need not be found. The limit is that the three-case rule is a rule for straight lines. A product in one relation can produce two valid answers, and both must be checked.

**A relation written in the middle integer.** When a question describes consecutive integers of one kind, call the middle one t and write the neighbours from the step. For three consecutive even integers the step is 2, so they are t - 2, t and t + 2. Take three consecutive even integers whose product equals 12 times the middle one. The product is (t - 2)t(t + 2) = t(t^2 - 4), so t(t^2 - 4) = 12t. Move everything to one side and factor out t: t(t^2 - 16) = 0. Either t = 0, giving -2, 0, 2, or t = 4, giving 2, 4, 6, or t = -4, giving -6, -4, -2. All three roots give even integers, so three triples fit. The limit is dividing by t: dividing both sides by t would silently drop the solution t = 0, so factor instead of dividing, and always test each root against the kind of integer the question names. Check: 2 x 4 x 6 = 48 = 12 x 4, (-2)(0)(2) = 0 = 12 x 0, and (-6)(-4)(-2) = -48 = 12 x (-4).

### The strongest wrong method and the reply

The tempting wrong method is to assume that two equations always fix two unknowns. It seems natural: two sentences, two unknowns, one answer. The reply is the ratio test. Two sentences fix a unique pair only if they carry different information. A scaled copy carries no new information, and a pair with the same left side but a different constant contradicts itself.

A second wrong method is to test the first equation only and stop. The reply is to read the stem for the phrase "both", "and", or "simultaneously", and to test every candidate in every equation. Many options satisfy a single relation; few satisfy the pair.

### UPSC application

Items in this family turn two short statements into two linear equations, then ask for the value of a quantity or the number of solutions. The relevant PYQ families include linear-cost validation, weight comparisons, and two-group relations. The method is always the same. Write both relations in the same form. Compare the ratios if the question asks whether a solution exists or is unique. Otherwise, eliminate or substitute, and check the answer in both equations.

### Revision points

- Two linear equations in two unknowns fix a unique pair only when their x and y coefficients are not in the same ratio.
- Equal coefficient ratios with unequal constants give no solution; all three ratios equal give infinitely many.
- Elimination exposes the three cases: a false constant means no solution, and 0 = 0 means dependence.
- Substitution is accurate when the simplest variable is isolated first.
- Option testing must check every equation, not only the first.
- A pair that satisfies one equation is a distractor, not an answer.
- Non-linear relations can produce two valid pairs, so the ratio test does not apply to them.
- Ordered pairs matter: (3, 4) and (4, 3) are different answers when x and y are named.
- Write both equations in the same form before comparing ratios.
- A scaled copy of an equation is not new information.

Not every relation fixes a value. The first question to ask of any relation is whether it pins a single answer.

### Practice

**MCQ 4**

Consider the system x - 2y = 3 and 3x - 6y = 10. Which statement is correct?

- A. It has the unique solution x = 4, y = 0.5.
- B. It has infinitely many solutions, because the coefficients are proportional.
- C. It has exactly two solutions, because the system has two equations.
- D. It has no solution, since the constants do not match the coefficient ratio.

**MCQ 4 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Solves the first equation for one pair, x = 4 and y = 0.5, and stops. That pair fits x - 2y = 3, but 3(4) - 6(0.5) = 9, not 10. A common solution must satisfy both equations.
- **B — Incorrect:** Notices that the coefficient ratios match, 1:3 and -2:-6, and concludes that the lines coincide. The constants 3 and 10 are not in that ratio, so the lines are parallel.
- **C — Incorrect:** Assumes that two equations must give two solutions, as a line and a circle can. Two parallel lines never meet, so the count is zero.
- **D — Correct:** The coefficient ratios are both 1:3, but the constant ratio is 3:10, which is not 1:3. The system is inconsistent: 3(x - 2y) = 9 while the second equation says 10.

**MCQ 5**

Given 3m - n = 7 and m + n = 9, what is m - n?

- A. -1
- B. 1
- C. 2
- D. 16

**MCQ 5 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Adding the two equations gives 4m = 16, so m = 4, and then n = 5. The difference is m - n = -1. Check: 3(4) - 5 = 7 and 4 + 5 = 9.
- **B — Incorrect:** Takes n - m, which reverses the sign of the answer. The question asks for m - n, and that value is -1.
- **C — Incorrect:** Subtracts the two constants, 9 - 7 = 2. The constants are not the difference of the unknowns, so the equations must be combined first.
- **D — Incorrect:** Adds the two constants, 7 + 9 = 16. That mixes the right-hand sides instead of combining the unknowns.

**MCQ 6**

Which ordered pair (x, y) satisfies both x + y = 9 and 2x - y = 0?

- A. (6, 3)
- B. (3, 6)
- C. (4, 5)
- D. (4.5, 4.5)

**MCQ 6 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Swaps the unknowns. 6 + 3 = 9 holds, but 2(6) - 3 = 9, not 0. The order of the unknowns is part of the answer.
- **B — Correct:** 3 + 6 = 9 and 2(3) - 6 = 0. Both equations hold, and no other option does.
- **C — Incorrect:** Checks the sum only. 4 + 5 = 9 holds, but 2(4) - 5 = 3, not 0.
- **D — Incorrect:** Splits the sum equally, giving 4.5 and 4.5. Then 2(4.5) - 4.5 = 4.5, not 0, so equal splitting ignores the second equation.

**MCQ 7**

How many ordered pairs of positive integers (x, y) satisfy x + y = 6 and make xy a multiple of 4?

- A. 1, counting {2, 4} once
- B. 4, counting orders twice
- C. 2, both orders counted once
- D. 5, ignoring the multiple condition

**MCQ 7 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Counts the unordered pair {2, 4} once and forgets that x and y are named. (2, 4) and (4, 2) are two different ordered pairs, and both satisfy the conditions.
- **B — Incorrect:** Counts each ordered pair twice, once for each order, so the two pairs become four.
- **C — Correct:** Listing x + y = 6 gives (1, 5), (2, 4), (3, 3), (4, 2) and (5, 1). Their products are 5, 8, 9, 8 and 5, and only 8 is a multiple of 4. So (2, 4) and (4, 2) are the two ordered pairs.
- **D — Incorrect:** Ignores the multiple condition and counts all five pairs with sum 6. The product condition removes three of them.

---

## Lesson 3 - Inequalities: sign flips, denominators, chains, coded inequalities and ranges

Progress: 3/9 | Stage: Core | Subtopic: Inequalities

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the sign of the multiplier decides the direction

```text
          start with an inequality   a < b
                      |
    what am I doing to both sides?
                      |
   +------------------+-----------------------+
   |                  |                       |
  ADD or SUBTRACT   MULTIPLY or DIVIDE     MULTIPLY or DIVIDE
  a constant        by a POSITIVE number   by a NEGATIVE number
   |                  |                       |
  direction KEPT    direction KEPT          direction REVERSED
  a + c < b + c     a/k < b/k (k > 0)       a/k > b/k (k < 0)
```

Read the diagram from the top. Only one operation can reverse an inequality: multiplying or dividing by a negative number. Adding a negative number does not reverse it. A multiplier of unknown sign is the case most likely to produce an error, so the next sections deal with it directly.

### Plain intuition

An inequality describes a region on the number line rather than a single point. The sign of a multiplier is the sign of the arrow. If you turn a number line around, by reflecting it through zero, every left-to-right order is reversed. Multiplying by a negative number is exactly that reflection. Adding a constant only slides the line, so the order is kept.

Think of the number line as a row of people standing in order of height. Adding 5 cm to everyone keeps the order. Multiplying every height by -1 turns the row round, so the tallest person is now the shortest.

### Doctrine: four facts that cover the family

- **Adding or subtracting** the same number to both sides never reverses the inequality.
- **Multiplying or dividing** both sides by a positive number keeps the direction.
- **Multiplying or dividing** both sides by a negative number reverses the direction.
- **Dividing** by an expression with a variable is legal only when its sign is known. If the sign is unknown, split the problem into cases. Division by zero is never legal.

### Part A: the sign flip in linear inequalities

**Example 1.** Solve 2x - 3 > 7. Add 3: 2x > 10. Divide by 2, a positive number: x > 5. Check: at x = 6, 2(6) - 3 = 9 > 7.

**Example 2.** Solve -2x > 6. Divide by -2, a negative number. The direction reverses: x < -3. Check: at x = -4, -2(-4) = 8 > 6, and at x = -2, -2(-2) = 4, which is not greater than 6, so the region starts below -3.

**Failure condition.** The error is not in the arithmetic but in the operation. Students often flip the sign whenever a negative number appears, even when they only add it. Ask first what you are doing to both sides.

### Part B: denominators and cross-multiplication

Cross-multiplication is a shortcut for comparing two fractions, but it works only when the signs of the denominators are known.

- **Sign cases for cross-multiplication.** Take the sign of the product bd. If bd > 0 (both denominators positive, or both negative), a/b < c/d is equivalent to ad < bc. If bd < 0 (one denominator negative), the same comparison is equivalent to ad > bc, because multiplying by the negative product bd reverses the inequality.
- **Unknown denominator sign.** The inequality 3/(x - 2) > 1 depends on whether x - 2 is positive or negative. Split the case.

**Example 3 (the case split).** Solve 3/(x - 2) > 1.

- If x - 2 > 0, multiply both sides by x - 2 without reversing: 3 > x - 2, so x < 5. Combined with x > 2, the solution is 2 < x < 5.
- If x - 2 < 0, multiply by x - 2 and reverse: 3 < x - 2, so x > 5. This contradicts x < 2, so there is no solution in this case.

The solution is 2 < x < 5. Check: at x = 3, 3/1 = 3 > 1. At x = 1, 3/(-1) = -3, which is not greater than 1. At x = 6, 3/4 is less than 1.

**Failure condition.** Cross-multiplying directly, 3 > x - 2 with no case split, gives the first case's answer and also includes values such as x = 1, where the denominator is negative and the inequality fails.

### Part C: chains and the two-sided bound

A chain such as -4 <= 3 - 2x < 7 is three inequalities at once. Apply the same operation to every part.

**Example 4.** Subtract 3 from each part: -7 <= -2x < 4. Divide each part by -2, which is negative, so both inequality signs reverse: 7/2 >= x > -2. Written in the usual order, -2 < x <= 3.5.

Check the endpoints. At x = 3.5, 3 - 2(3.5) = -4, which satisfies the left bound with equality, so 3.5 is included. At x = -2, 3 - 2(-2) = 7, which is not less than 7, so -2 is excluded. The open and closed endpoints come from the original signs, not from the number of steps.

**Failure condition.** Dividing the middle part only, or forgetting to reverse both signs when dividing the chain by a negative number, gives a wrong range.

### Part D: coded inequalities

A coded inequality defines a new operation and asks for a range. The method is to rewrite the coded expression in ordinary form before solving.

**Example 5.** If a @ b means a + 2b, and 5 @ x > 13, find the range of x. Rewrite as 5 + 2x > 13, so 2x > 8 and x > 4.

**Example 6.** If p * q means 2p - q, and 3 * x <= 4, find the range of x. Rewrite as 6 - x <= 4, so -x <= -2 and x >= 2. The variable is negative on the left, so dividing or multiplying by -1 reverses the inequality.

**Failure condition.** The code may hide a sign. Rewrite the code in full before deciding whether any division has a negative multiplier.

### Part E: ranges of an expression

If x is restricted to an interval, the range of 2x + 3 follows from the interval's endpoints, with the open and closed ends preserved.

**Example 7.** If -1 < x <= 5, then -2 < 2x <= 10, so 1 < 2x + 3 <= 13. The range is (1, 13]. The lower endpoint is open because x > -1 excludes x = -1, which would give 1; the upper endpoint is closed because x = 5 is included.

**Limit.** A linear expression with a positive coefficient preserves the order of the endpoints. A negative coefficient reverses them, and the smaller and larger values must be found from the transformed endpoints.

### The strongest wrong method and the reply

The tempting wrong method is to cross-multiply or multiply both sides by a variable without knowing its sign. For 1/x > 1/3, cross-multiplication gives 3 > x, which includes negative values such as x = -1. The reply is to split the case: if x is negative, the left side is negative and cannot exceed 1/3. The fraction must be treated as a difference, (3 - x)/(3x) > 0, and its sign examined.

A second wrong method is to reverse the sign whenever a negative number appears anywhere in the problem. The reply is to name the operation: adding a negative does not reverse the inequality, while multiplying or dividing by a negative does.

### UPSC application

Inequality items in this paper ask for a range, a chained validity check, or the set of values consistent with a coded rule. The method is to name each operation, record the sign of every multiplier and denominator, and state the endpoints with their open or closed status. Answers that look right can fail one endpoint, so test the endpoints as well as one interior value.

### Revision points

- Adding the same quantity to both sides never reverses an inequality.
- Multiplying or dividing by a positive number keeps the direction; by a negative number reverses it.
- A denominator of unknown sign requires a case split, never a direct cross-multiplication.
- Dividing a chain by a negative number reverses both signs at once.
- Open and closed endpoints come from the original signs, and they must be preserved through each step.
- A coded operation must be rewritten in ordinary form before the inequality is solved.
- A linear expression with a positive coefficient keeps the order of its interval endpoints; a negative coefficient reverses it.
- Test an endpoint and one interior value before accepting a range.
- Zero denominators are excluded from the domain.
- A reversed inequality can be correct for a different question, so read which inequality the item asks about.

Not every relation is simple. The same translation habit applies to harder relations, but each case must be checked before a conclusion is drawn.

### Practice

**MCQ 8**

For which values of x is 2/(x + 1) less than 1?

- A. x > 1 only, where x + 1 is positive
- B. -1 < x < 1, the reversed set
- C. x < -1 only, where x + 1 is negative
- D. x < -1 or x > 1

**MCQ 8 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Keeps only the case where x + 1 is positive and drops the negative-denominator case, where every value below -1 works.
- **B — Incorrect:** Reverses the inequality, giving the solution set of 2/(x + 1) greater than 1. At x = 0, 2/1 = 2 is greater than 1, so this band is the wrong set.
- **C — Incorrect:** Keeps only the negative-denominator case and drops x > 1. At x = 2, 2/3 is less than 1, so x > 1 must be kept.
- **D — Correct:** For x > -1, multiply by the positive x + 1 to get 2 < x + 1, so x > 1. For x < -1, multiply by the negative x + 1 and reverse: 2 > x + 1, which holds for every x < -1. Check: x = -2 gives -2 < 1, and x = 2 gives 2/3 < 1.

**MCQ 9**

Which integer satisfies both -3x > 6 and x > -4?

- A. x = -3
- B. x = -2
- C. x = -5
- D. x = 0

**MCQ 9 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Dividing -3x > 6 by -3 reverses the sign: x < -2. With x > -4, the only integer is -3. Check: -3(-3) = 9 is greater than 6, and -3 is greater than -4.
- **B — Incorrect:** Uses greater-than-or-equal where the stem has a strict inequality. At x = -2, -3(-2) = 6, which is not greater than 6, so -2 fails the first condition.
- **C — Incorrect:** Reverses the second inequality, reading x > -4 as x < -4. Then -5 fits the reversed reading, but -5 is not greater than -4, so it fails the stem.
- **D — Incorrect:** Divides without reversing the sign, which gives x > -2. The value 0 satisfies that wrong inequality and the second condition, but -3(0) = 0 is not greater than 6.

---

## Lesson 4 - Absolute value, squares and surds: two branches and the unique-root test

Progress: 4/9 | Stage: Core, with Advanced Parts C and D | Subtopic: Absolute value, squares and surds

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the absolute value is a distance from zero

```text
   ----|-----|-----|-----|-----|-----|-----|-----|----  number line
      -6    -4    -2     0     2     4     6     8
                    |<-- distance 2 -->|
   |u| = k    the points at distance k from zero:   u = k  OR  u = -k
   |u| < k    the points inside the band:           -k < u < k
   |u| > k    the points outside the band:          u < -k  OR  u > k
   |u| = k when k < 0   no point is at negative distance: NO SOLUTION
```

The bar on either side of zero is the key. An absolute value asks how far a number is from zero, not which sign it has. A distance equation has two branches, one on each side of the origin, unless the distance is zero, which gives one point, or negative, which gives none.

### Plain intuition

Read |u| as "the distance of u from zero". The distance from 0 to 3 is 3, and the distance from 0 to -3 is also 3. Both values are at the same distance, so both answer the equation |u| = 3. A square also hides two candidates: the squares of 3 and -3 are both 9. The surd sign, the square root symbol, is a convention that chooses the non-negative root, and it does not undo the two branches of the equation.

### Part A (Core): the two branches of an absolute value

- **Rule for equations.** If k > 0, then |u| = k gives u = k or u = -k. If k = 0, then u = 0 is the only solution. If k < 0, there is no solution.
- **Rule for inequalities.** If k > 0, then |u| < k gives -k < u < k, a single interval. Then |u| > k gives u < -k or u > k, which is two outward rays.
- **Worked example.** Solve |2x - 1| = 5. The inner expression is 5 or -5. From 2x - 1 = 5, x = 3. From 2x - 1 = -5, x = -2. Check: |2(3) - 1| = 5 and |2(-2) - 1| = |-5| = 5. The sum of the two solutions is 3 + (-2) = 1.
- **Worked example.** Solve |x - 3| < 2. The distance of x from 3 must be less than 2, so -2 < x - 3 < 2, which gives 1 < x < 5. Check: at x = 4 the distance is 1, which is less than 2; at x = 5 it is 2, which is not.
- **Worked example.** Solve |x + 4| > 2. Either x + 4 > 2, so x > -2, or x + 4 < -2, so x < -6. Check: at x = 0 the distance is 4 > 2; at x = -4 it is 0, which fails.
- **Failure condition.** The method fails when one branch is dropped, or when a negative k is treated as having solutions. An equation with a negative absolute value has no solution, and an equation with k = 0 has exactly one.

### Part B (Core): squares, roots and the sign of a comparison

- **Rule.** A squared expression has the same value for u and -u. So u^2 = 16 has the roots 4 and -4. The symbol sqrt(16) denotes the non-negative root, 4, and it does not give the equation's second solution.
- **Rule for comparison.** If a > b >= 0, then a^2 > b^2. This is the reason squaring is a safe way to compare two non-negative quantities.
- **Failure condition.** Squaring preserves order only when both sides are non-negative. The comparison -3 > -5 is true, but squaring gives 9 < 25, which reverses it. Check the signs before squaring.

### Part C (Advanced): the unique-root test

The unique-root test asks how many real solutions an equation has when the unknown appears as a power. Over the real numbers:

```text
  x^2 = k :   k > 0  -> TWO roots (+sqrt(k) and -sqrt(k))
              k = 0  -> ONE root  (x = 0)
              k < 0  -> NO real root
  x^3 = k :   ANY real k -> EXACTLY ONE real root (the sign of x matches the sign of k)
```

The reason is that an odd power keeps the order of the numbers on the real line, so it cannot send two different numbers to the same value. An even power does send a number and its negative to the same value.

- **Worked example (sign from an odd power).** Suppose x^3 > 0. A cube keeps the sign of its base, so x > 0. Now suppose only x^2 > 0. That rules out x = 0, but x = -4 satisfies it, since (-4)^2 = 16 > 0 while (-4)^3 = -64 < 0. So the cube statement settles the sign and the square statement does not.

- **Worked example (false uniqueness).** Suppose n^2 = 49 is stated as a fact about an integer n. A reader may take n = 7 and stop. The equation has two roots, 7 and -7, and the statement alone does not decide between them.
- **Worked example (absolute value).** Suppose |n - 3| = 5. The branches give n = 8 and n = -2. A statement that gives only the absolute value is not enough to fix n.
- **Worked example (odd power).** Suppose n^3 = 343. The only real root is 7, because cubing is one-to-one on the real numbers.
- **Failure condition.** The unique-root test applies to one equation in one unknown. Two statements can jointly remove a branch, which is a question about information rather than about equations.

### Part D (Advanced): comparing surds by squaring and by common factors

Sums of surds cannot be compared by adding under a single root. Two methods are safe.

- **Method 1: squaring.** Compare (sqrt(18) + sqrt(8))^2 with 48. The square is 18 + 8 + 2 sqrt(18 x 8) = 26 + 2 sqrt(144) = 26 + 24 = 50. Since 50 > 48 and both sides are positive, sqrt(18) + sqrt(8) is larger than sqrt(48). Check: sqrt(18) + sqrt(8) is about 7.07, and sqrt(48) is about 6.93.
- **Method 2: common factor.** Write each root as a multiple of the same radical. sqrt(50) + sqrt(72) = 5 sqrt(2) + 6 sqrt(2) = 11 sqrt(2), which is about 15.56, and sqrt(200) = 10 sqrt(2), which is about 14.14. So the sum is larger.
- **Failure condition.** Decimal approximation is safe only when the difference is not close. For close values, square or factor the common radical. The common-factor method works only when the radicals reduce to one radical.

### Example with limits: the square root of a square

For every real x, sqrt(x^2) = |x|. This is the two-branch fact seen through the root symbol. For x = 4, sqrt(16) = 4, and for x = -4, sqrt(16) is again 4, not -4. Writing sqrt(x^2) = x is correct only when x >= 0. A learner who drops the absolute value when simplifying a root has made the same error as one who drops a branch of an absolute-value equation.

### The strongest wrong method and the reply

The tempting wrong method is to treat |x| < 2 as x < 2. It ignores the lower branch, and it admits every very negative number. The reply is the number line: the distance from zero must be less than 2, so x must lie in the band from -2 to 2. For this inequality, the band is the solution, not the half-line.

A second wrong method is to conclude that x^2 = 49 has one answer because the square root of 49 is 7. The reply is the unique-root test: an even power gives two roots when the constant is positive, and the principal square root is only one of them.

### UPSC application

Items that use an absolute value ask for the set of values at a fixed distance, or for the range of a distance. They are often phrased as "the difference between two numbers is at most k", and the two branches must both be included. Items that use squares or cubes are often data-sufficiency statements in which one squared statement is not enough. Items that compare surds ask which of two sums is larger, and the squaring or common-factor method is always available. The PYQ families that use these tools include range inequality deductions and expression comparisons, which are linked later in the session.

### Revision points

- |u| = k gives u = k or u = -k when k > 0; one solution when k = 0; none when k < 0.
- |u| < k is a band, -k < u < k; |u| > k is two outward rays.
- Keep both branches of every absolute-value equation until a condition removes one.
- A square root symbol gives the non-negative root; an equation u^2 = k keeps both roots.
- Squaring preserves order only when both sides are non-negative.
- x^2 = k has two real roots for k > 0, one for k = 0, none for k < 0.
- x^3 = k has exactly one real root for every real k.
- A squared statement such as n^2 = 49 is not unique until the sign is fixed.
- Compare sums of surds by squaring when both sides are positive, or by writing both as one radical times a number.
- Decimal approximation is safe only when the two values are clearly apart.

Not every question asks for a value; some ask how two quantities stand, and the method must change accordingly.

### Practice

**MCQ 10**

What is the product of the two solutions of |3x + 2| = 7?

- A. 5, taking the absolute values of the solutions
- B. -5, from the two signed solutions
- C. -4/3, from adding the two solutions
- D. -3, from the negative branch alone

**MCQ 10 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Takes the absolute values of the two solutions, 5/3 and 3, and multiplies them to get 5. That ignores the sign of -3, which the product must keep.
- **B — Correct:** 3x + 2 = 7 gives x = 5/3, and 3x + 2 = -7 gives x = -3. The product is (5/3) x (-3) = -5. Check: |3(5/3) + 2| = 7 and |3(-3) + 2| = 7.
- **C — Incorrect:** Adds the two solutions instead of multiplying them: 5/3 + (-3) = -4/3. A sum is not a product.
- **D — Incorrect:** Keeps only the negative branch, x = -3, and reports it as the product. A product of two solutions needs both of them.

**MCQ 11**

How many integers n satisfy |2n - 5| <= 3?

- A. 2
- B. 8
- C. 4
- D. 5

**MCQ 11 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Uses the strict inequality |2n - 5| < 3, which keeps only n = 2 and n = 3. The stem allows equality, so the endpoints n = 1 and n = 4 also count.
- **B — Incorrect:** Adds the constant 5 to the bound 3 and uses |2n - 5| <= 8. That gives -1.5 <= n <= 6.5, which is eight integers, from -1 to 6.
- **C — Correct:** -3 <= 2n - 5 <= 3 gives 2 <= 2n <= 8, so 1 <= n <= 4: the integers 1, 2, 3 and 4. Check: |2(1) - 5| = 3 and |2(4) - 5| = 3.
- **D — Incorrect:** Takes the lower end as n = 0 instead of n = 1, so it counts 0, 1, 2, 3 and 4. Zero fails the band, since |2(0) - 5| = 5 is greater than 3.

**MCQ 12**

Compare sqrt(5) + sqrt(10) with sqrt(24). Which statement is correct?

- A. sqrt(24) is larger, since squaring the two terms gives 5 + 10 = 15.
- B. They are equal, since sqrt(5) + sqrt(10) equals sqrt(15).
- C. They cannot be compared, since one side is a sum.
- D. The sum sqrt(5) + sqrt(10) is larger, since its square exceeds 24.

**MCQ 12 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Squares only the two terms and drops the cross term 2 x sqrt(5) x sqrt(10) = 10 sqrt(2). The square of a sum is not the sum of the squares.
- **B — Incorrect:** Adds the radicands under one root, which is false: sqrt(15) is about 3.87, while the sum is about 5.40.
- **C — Incorrect:** Refuses the comparison. Both sides are positive, so squaring preserves their order, and the comparison can be made.
- **D — Correct:** (sqrt(5) + sqrt(10))^2 = 5 + 10 + 2 sqrt(50) = 15 + 10 sqrt(2), about 29.14, which exceeds 24. Both sides are positive, so the sum is the larger one.

---

## Lesson 5 - Quantitative comparison: equal forms, powers, surds, ratios, fractions and percentages

Progress: 5/9 | Stage: Core, with Advanced Part C | Subtopic: Quantitative comparison

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: put both quantities on the same scale

```text
 QUANTITY A  ------>  REWRITE in the same form  ------>  COMPARE the forms  ------>  DECIDE
 e.g. 2^30           8^10 and 9^10                        same exponent, larger    3^20 is larger
      3^20           (bases differ, exponent same)        base wins                 for both positive
```

A comparison is a decision about order. You do not need the two values, only the rule that puts them in order. The most reliable route is to rewrite both quantities so that they share a feature: the same base, the same exponent, the same denominator, or the same reference point for a percentage. Once they share the feature, the comparison is usually a single line.

### Plain intuition

Imagine two runners who started from different points on a track. You cannot tell who is ahead by looking at their distances from their own starting lines. You must measure both from the same line. Quantitative comparison is measuring from the same line, and the common form is that line.

### Part A (Core): equal exponents, equal bases and the reversal for bases between 0 and 1

- **Rule.** If two positive powers have the same exponent, the larger base gives the larger power. If they have the same base greater than 1, the larger exponent gives the larger power.
- **Rule for 0 < x < 1.** A power with a larger exponent is smaller. Repeated multiplication by a fraction shrinks the value. So for 0 < x < 1 and m > n, x^m < x^n.
- **Worked example.** Compare 2^30 with 3^20. Rewrite 2^30 = (2^3)^10 = 8^10 and 3^20 = (3^2)^10 = 9^10. Equal exponents, so 9^10 is larger: 3^20 > 2^30.
- **Worked example.** Compare 7^15 with 5^21. Rewrite both with exponent 3: 7^15 = (7^5)^3 = 16807^3 and 5^21 = (5^7)^3 = 78125^3. Since 78125 > 16807, 5^21 is larger.
- **Worked example.** Compare (2/3)^4 with (2/3)^2. The base is between 0 and 1, so the higher power is smaller. Check: (2/3)^4 = 16/81, about 0.20, and (2/3)^2 = 4/9, about 0.44.
- **Worked example (decimal base).** Compare (0.5)^3 with (0.5)^2. Since 0.5^3 = 0.125 and 0.5^2 = 0.25, the higher power is the smaller one, as the rule for bases between 0 and 1 predicts.
- **Exponential models.** A quantity that multiplies by a fixed factor each period has the form start times factor raised to the number of periods. Example: a bacterial count of 20 that triples every 3 hours is N = 20 x 3^(t/3); after 6 hours N = 20 x 9 = 180. Limit: the model needs a constant factor per period; a count that grows by a fixed amount each period is linear, not exponential.
- **Taking roots.** For positive quantities, the order of two numbers is the order of their square roots, and of their cube roots. Example: sqrt 10 and 3 are both positive, and 10 is greater than 9, so sqrt 10 is greater than 3. Failure condition: roots preserve order only when the quantities are non-negative, or for odd roots of any sign; comparing a negative quantity with a positive one needs a separate check.
- **Failure condition.** Equal exponents are needed before comparing bases. Comparing 5^20 with 4^25 by the bases alone ignores the different exponents, and the power with the larger base can be smaller. Rewrite both with a common exponent first.

### Part B (Core): fractions, ratios, reciprocals and percentages

- **Rule for a ratio and its reciprocal.** If a > b > 0, then a/b > b/a, because multiplying by ab > 0 gives a^2 > b^2.
- **Rule for fractions.** For positive denominators, a/b < c/d is equivalent to ad < bc. Check the denominators first.
- **Rule for reciprocals.** If x > y > 0, then 1/x < 1/y. The positivity is essential: with x = 2 and y = -1, we have x > y but 1/2 > -1, so the order of the reciprocals is reversed.
- **Worked example.** Compare 7/9 with 5/6. Cross-multiply, since both denominators are positive: 7 x 6 = 42 and 5 x 9 = 45. So 7/9 < 5/6.
- **Percentages.** A is 25% more than B means A = 1.25B. Then B = A/1.25 = 0.8A, so B is 20% less than A. The percentage "more" and "less" use different bases, and they are not symmetric.
- **Percentage points versus percent change.** A rate that rises from 10% to 14% has risen by 4 percentage points. Relative to the old rate of 10%, the rise is 4/10 = 40 per cent. The two measures have different bases, and an item that mixes them produces a wrong option.
- **Failure condition.** Comparing a ratio with its reciprocal without a positivity check, or treating "percentage points" as "per cent" of the old value, produces errors that look reasonable.

### Part C (Advanced): common multiples of exponents for large powers

For large powers the exponents cannot be equalised with small bases, so the method uses a common exponent or an interval argument.

- **Worked example.** Compare 5^100 with 3^150. Write 5^100 = (5^2)^50 = 25^50 and 3^150 = (3^3)^50 = 27^50. Since 27 > 25, 3^150 is larger. Check the exponents: 2 x 50 = 100 and 3 x 50 = 150.
- **Worked example (surds).** Compare sqrt(50) + sqrt(72) with sqrt(200) by the common-factor method in Lesson 4, Part D. The left side is 11 sqrt(2) and the right side is 10 sqrt(2), so the left side is larger.
- **Failure condition.** A common exponent is found by the lowest common multiple of the exponents. Choosing an arbitrary multiple gives correct inequalities but may make the numbers unmanageable; choose the smallest common multiple.

### Example with limits: comparing without fixing the sign

Let x and y be real numbers with x > y. Is x^2 > y^2? Not always. If x = 1 and y = -3, then x > y and x^2 = 1 < 9 = y^2. Squaring a comparison is safe only when both sides are non-negative, as Lesson 4 showed. A comparison that depends on sign must be checked by cases.

### The strongest wrong method and the reply

The tempting wrong method is to compare the bases of two powers and conclude that the power with the larger base is larger. It ignores the exponents. The reply is to equalise the exponents, or the bases, before deciding.

A second wrong method is to apply the rule for bases above 1 to a base between 0 and 1. For x = 0.4, the power x^5 looks as if it should be larger than x^3, but 0.4^5 = 0.01024 is less than 0.4^3 = 0.064. The reply is to identify whether the base is above or below 1 before using the power rule.

### UPSC application

Quantitative comparison items present two expressions, often with powers, surds, ratios, fractions or percentages, and ask which is larger, whether they are equal, or whether the comparison cannot be decided. The method is always to rewrite both expressions in one form. The PYQ families include ratio comparisons, product comparisons and percentage comparisons, which are linked to this lesson in the PYQ section. In a data-sufficiency item, a comparison may be the question itself. Then the verdict is about whether the comparison is pinned, which is a question about information rather than value.

### Revision points

- Rewrite both quantities in one common form before comparing.
- Equal exponents: compare the bases. Equal bases above 1: compare the exponents.
- For 0 < x < 1, a larger exponent gives a smaller power.
- For a > b > 0, a/b > b/a.
- Cross-multiply fractions only when both denominators are positive.
- For x > y > 0, 1/x < 1/y; the positivity is essential.
- A is 25 per cent more than B means B is 20 per cent less than A.
- Percentage points use the difference of two percentages; percent change uses the old value as base.
- For large powers, use the lowest common multiple of the exponents.
- Squaring a comparison is safe only when both sides are non-negative.

Knowing an order is one kind of answer; a different kind of question asks for an extreme value.

### Practice

**MCQ 13**

Which is larger, 4^25 or 5^20?

- A. 4^25 is larger, after equal exponents are compared.
- B. 5^20 is larger, since its base is bigger.
- C. They are equal, since both are powers of small integers.
- D. The comparison cannot be decided without evaluating the powers.

**MCQ 13 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Write both with exponent 5: 4^25 = (4^5)^5 = 1024^5 and 5^20 = (5^4)^5 = 625^5. Since 1024 > 625, 4^25 is larger.
- **B — Incorrect:** Judges by the larger base, 5 > 4. A larger base does not guarantee a larger power when the exponents differ; here the exponent of 4 is larger, and that effect outweighs the base.
- **C — Incorrect:** Assumes the two powers are equal because both are powers of small integers. Equal values would need equal bases after rewriting, and 1024 and 625 are different.
- **D — Incorrect:** Refuses to compare, although equalising the exponents is available for positive bases. The comparison can be made without evaluating either power.

**MCQ 14**

If x and y are both negative and x < y, which statement is always true?

- A. x squared equals y squared.
- B. x squared is greater than y squared.
- C. x squared is less than y squared.
- D. The order of the squares depends on how far apart x and y are.

**MCQ 14 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Treats the squares as equal because both numbers are negative. Equal squares need |x| = |y|, and x < y excludes that; at x = -3 and y = -1 the squares are 9 and 1.
- **B — Correct:** For negative numbers, the number further from zero is the smaller one, so x < y gives |x| > |y| and x squared > y squared. Check: x = -3 and y = -1 give 9 > 1; x = -2 and y = -1.5 give 4 > 2.25.
- **C — Incorrect:** Reverses the comparison by reading the larger number y as the one with the larger square. For negative numbers the number closer to zero has the smaller square.
- **D — Incorrect:** Claims that the gap matters. The order of the squares follows from the order of the absolute values, and for negative numbers that order is fixed whatever the gap.

**MCQ 15**

Which is larger, 11/15 or 7/10?

- A. 7/10 is larger, since 10 is smaller than 15.
- B. They are equal, since both fractions are below 1.
- C. 11/15 is larger, since 110 exceeds 105.
- D. 11/15 is smaller, since 15 is greater than 10.

**MCQ 15 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Compares the denominators only and treats the smaller denominator as the larger fraction. Cross-multiplying gives 7 x 15 = 105, which is below 11 x 10 = 110.
- **B — Incorrect:** Assumes that fractions below 1 are equal. They are not: 11/15 is about 0.733 and 7/10 is 0.7.
- **C — Correct:** Cross-multiply with positive denominators: 11 x 10 = 110 and 7 x 15 = 105, so 11/15 is larger.
- **D — Incorrect:** Reverses the comparison by reading the larger denominator as the larger fraction. The cross-multiplication shows the opposite.

**MCQ 16**

Last year's pass rate was 45 per cent, and this year's is 54 per cent. Which statement is correct?

- A. The rate rises by 9 per cent, which is the same as 9 percentage points.
- B. The rate rises by 54 per cent, to the new level.
- C. The rise is 9 per cent of this year's rate, since the rise is 9 points.
- D. The rise is 20 per cent of last year's rate, and it is 9 percentage points.

**MCQ 16 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Reads the gap of 9 points as a per cent change. The gap is 9 points, but relative to last year's 45 per cent the change is 20 per cent, so the two measures differ.
- **B — Incorrect:** Reports the new level, 54, as the increase. The increase is 54 - 45 = 9 points.
- **C — Incorrect:** Reads the 9 points as a share of this year's rate. The share is 9/54 = 16.7 per cent, not 9 per cent.
- **D — Correct:** The gap is 54 - 45 = 9 percentage points. Relative to the old rate, 9/45 = 20 per cent. The two measures use different bases.

---

## Lesson 6 - Bounds and optimisation: AM-GM, integer optima and interval corners

Progress: 6/9 | Stage: Core and Advanced | Subtopic: Bounds and optimisation

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: a product with a fixed sum is largest in the middle

```text
   x + y = S (fixed)          the product x * y as x moves along the sum line

   x:   0    2    4    6    8   ...  S
   y:   S    S-2  S-4  S-6  S-8 ...  0
   xy:  0    ...  ...  MAX  ...  ... 0
                             ^
                     the parts are closest to S/2
```

Read the table from left to right. As one part grows, the other shrinks by the same amount. The product is zero at the two ends, where one part is zero, and largest near the middle, where the parts are closest to half the sum. This picture holds for any fixed sum of non-negative parts.

### Plain intuition

Suppose you have a fixed length of fencing and want the largest rectangular area. Making one side very long and the other very short gives a thin rectangle with small area. Making the sides equal gives the square. The sum is fixed, and the product is largest when the parts are balanced. Optimisation is the search for the balanced point, and the integer rules decide what "balanced" means when the parts must be whole numbers.

### Part A (Advanced): integer optimum and the nearest integers

- **Rule.** For positive integers x and y with x + y = S, the product xy is largest when x and y are as close as integers allow. If S is even, the best split is S/2 and S/2. If S is odd, the best split is (S - 1)/2 and (S + 1)/2.
- **Worked example.** Let x + y = 15. The nearest integers to 7.5 are 7 and 8, and 7 x 8 = 56. The neighbouring split 6 and 9 gives 54, which is smaller, so 56 is the maximum.
- **Worked example.** For a minimum with the same sum, take the most unequal split: 1 x 14 = 14 is the smallest product among positive integers with sum 15.
- **Failure condition.** The real bound (S/2)^2 = 56.25 for sum 15 is an upper bound for the reals, not an attainable integer product. Use it as a check, not as an answer. Also, choosing an equal split when S is odd, such as 7 and 7 for sum 15, violates the sum.

### Part B (Advanced): AM-GM for non-negative parts

The arithmetic mean-geometric mean inequality states that for non-negative numbers x and y, (x + y)/2 >= sqrt(xy). Squaring both sides, xy <= ((x + y)/2)^2, with equality only when x = y.

- **Worked example.** For x + y = 17 with positive integers, the bound is (17/2)^2 = 72.25. The integers 8 and 9 give 72, the largest attainable integer product, and they are the nearest integers to 8.5.
- **Failure condition.** AM-GM requires non-negative parts. For a sum with a negative part, the product can be large and negative or positive, and the bound does not apply. Always check the signs first.

### Part C (Advanced): interval corners and endpoints

For sums, the bounds add: if a < x < b and c < y < d, then a + c < x + y < b + d, with the same open or closed rule at each end. For products, the range of xy is found from the four corner products. Each corner is a pair of endpoints, and the extremes of the product are among these four values, provided each endpoint is included or can be approached.

- **Worked example.** Let -2 < x <= 3 and 1 <= y < 4. The four corner products are (-2)(1) = -2, (-2)(4) = -8, (3)(1) = 3 and (3)(4) = 12. The minimum -8 needs x = -2 and y = 4 together, and each of those ends is excluded. The maximum 12 needs x = 3 and y = 4 together, and y = 4 is excluded. So -8 < xy < 12. Every value between is reached as x and y vary continuously.
- **Worked example.** Let -1 <= x < 2 and 2 <= y <= 5. The corners are -2, -5, 4 and 10. The minimum -5 is attained at x = -1, y = 5, since both ends are closed. The maximum would be 10, which needs x = 2, excluded. So the range is [-5, 10).
- **Worked example (all-open ends).** Let -2 < x < 3 and 1 < y < 4. The corners are -2, -8, 3 and 12, but every end is now open. The minimum -8 needs x = -2 and y = 4 together, and both are excluded; the maximum 12 needs x = 3 and y = 4 together, and y = 4 is excluded. So -8 < xy < 12, with neither extreme attained. An interior check: x = 0 and y = 2 give 0, which lies inside the range.
- **Failure condition.** Multiplying the lower bounds to obtain the minimum is wrong when the intervals straddle zero. In the first example, the naive product of the lower bounds is (-2)(1) = -2, which is not the minimum; the minimum comes from a mixed corner, (-2)(4). Division through an interval containing zero is not allowed at all.

### The strongest wrong method and the reply

The tempting wrong method for a product range is to multiply the smallest values together and the largest values together. For -2 < x <= 3 and 1 <= y < 4, that gives -2 as the minimum and 12 as the maximum, which loses the true minimum -8. The reply is to test all four corners, because the sign of x changes the direction of the product.

A second wrong method is to treat the sum optimum as a real maximum for integers. For sum 17 the real bound 72.25 is never reached by integers. The reply is to test the integer splits near the middle.

### UPSC application

Optimisation items in this family ask for the largest or smallest value of a product, a sum or a cost subject to a constraint, often with integers and a stated range. The method is to write the objective as a function of one variable, use the constraint to eliminate the other, and test the admissible values or endpoints. Interval items ask for the range of an expression on a stated set, and the open or closed status of each end must be preserved. The PYQ families include rate-constraint optimisation and bounded-expression ratios, which are linked to this lesson.

### Revision points

- For a fixed sum of positive parts, the product is largest when the parts are as equal as integers allow.
- For x + y = S with S odd, the best integer split is (S - 1)/2 and (S + 1)/2.
- The real bound (S/2)^2 is an upper limit; attainable integer products can be smaller.
- AM-GM: xy <= ((x + y)/2)^2 for non-negative x and y.
- For intervals, the product's extremes are among the four corner products.
- Open and closed ends decide whether an extreme is attained.
- A minimum may come from a mixed corner, not from the two lower bounds.
- Never divide through an interval that contains zero.
- Check each candidate against the constraint before accepting it.
- The range of a product on a rectangle is an interval whose ends are corner values or approached values.

Values answer how much. The final kind of question asks something different.

### Practice

**MCQ 17**

Positive integers x and y satisfy xy = 36. What is the least possible value of x + y?

- A. 12
- B. 13
- C. 15
- D. 37

**MCQ 17 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The sum is smallest when the two factors are as close as integers allow: 6 and 6, with sum 12. Check: 6 x 6 = 36. For positive numbers with a fixed product, x + y is at least 2 times the square root of the product, which is 12, so no pair does better.
- **B — Incorrect:** Takes 4 and 9, which multiply to 36 and sum to 13. The pair is admissible but not least, because 6 and 6 give 12.
- **C — Incorrect:** Takes 3 and 12, which multiply to 36 and sum to 15. Again the pair is admissible but larger than the least sum.
- **D — Incorrect:** Takes 1 and 36, the most unequal split, which gives the largest sum, 37, rather than the least.

**MCQ 18**

If -2 <= x <= 1 and 3 < y <= 5, what is the range of the product xy?

- A. [-6, 5], with the minimum at -6
- B. [-10, 5], with both extremes attained
- C. (-10, 5], with the minimum open
- D. [-10, 3], with the maximum at 3

**MCQ 18 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Takes the corner (-2)(3) = -6 as the minimum, but y = 3 is excluded, so -6 is not attained. The true minimum is -10.
- **B — Correct:** The corners are (-2)(3) = -6 with y = 3 excluded; (-2)(5) = -10 with both ends included; (1)(3) = 3 with y = 3 excluded; and (1)(5) = 5 with both included. The minimum -10 and the maximum 5 are both attained, so the range is [-10, 5].
- **C — Incorrect:** Makes the minimum open, although x = -2 and y = 5 are both included, so -10 is attained.
- **D — Incorrect:** Takes the corner (1)(3) = 3 as the top, ignoring the attained corner (1)(5) = 5.

---

## Lesson 7 - The data-sufficiency format: printed options, verdicts and necessary versus sufficient

Progress: 7/9 | Stage: Core | Subtopic: The data-sufficiency format

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the anatomy of a data-sufficiency item

```text
  QUESTION  (asks for a value, a yes/no answer, or a comparison)
      |
  STATEMENT I   (one piece of information)
  STATEMENT II  (a second piece of information)
      |
  PRINTED OPTIONS
  (a)  One statement alone settles the question; the other alone does not.   STABLE
  (b)  Either statement alone settles the question.                  STABLE
  (c)  Both together settle it; neither alone does.                  STABLE
  (d)  READ IT: the wording differs between papers and items.        VARIES
```

Three of the four printed options have the same meaning in every audited paper. The fourth changes. Read the fourth option before you think about the question, because the letter you choose depends on what the fourth option actually says.

### Plain intuition

A data-sufficiency item is not a calculation. It is a question about information. You are a careful reader who has been told a question and two facts. Your job is to decide whether the facts close the question. Closing means that only one answer is possible. If two answers remain, the facts are not enough, however close they come.

The skill is to separate two questions. The first is "what is the value?" The second is "is the value fixed?" The format asks only the second. A solver who computes the value has done more work than the item requires, and that work can also hide a second possible value. The same test decides whether a passage supports a claim: the text must force the conclusion, not merely make it plausible.

### Visual: the three kinds of relation problem

```text
                    A RELATION PROBLEM
                           |
     +---------------------+----------------------+
     |                     |                      |
   SOLVE                COMPARE                DECIDE
   equations            inequality or           data sufficiency
   (find the value)     quantity comparison     (is the information enough?)
     |                     |                      |
   find x               which is larger?       can the value be fixed?
                                               ask "can it be found?", not "what is it?"
```

The three branches are the three questions this paper asks. Lessons 1 to 6 train the first two; Lessons 7 to 9 train the third, which does not ask for a value at all.

### Part A (Core): the printed options come first

The format rewards a reader who reads the printed options before the stem. Two items can have the same stem and a different fourth option, and a reader who recalls the wrong fourth option will mark a letter that means the opposite of the verdict.

- Read the four printed options. Note the exact meaning of (d) for this item.
- Then read the question and decide whether it is answerable with no statement at all.
- Only after that, test the statements.

This order matters because the question alone can be answerable. In that case, the verdict is the option that says so, and it is not one of the statement-based options.

### Part B (Core): three versions of the fourth option

The audited papers print three different meanings for option (d). They are described here in paraphrase, so that the reader can recognise the meaning in any wording.

```text
VERSION                 WHERE IT APPEARS                       MEANING OF (d)
---------------------   ------------------------------------   ----------------------------------------
W1: "neither works,     2024 items (each item prints           the question cannot be answered even
     even together"      its own options)                       with both statements together

W2: "neither works,     2025 (some items) and the 2026         the question cannot be answered using
     even any one"       block of five items                    any of the statements, alone or together

W3: "the question       2025 (other items)                     the question is answered even with no
     needs no statement" statement at all                       statement; the question alone settles it
```

The three versions show the danger of memory. A student who has learnt "(d) means nothing works" will mark a letter that says the opposite of W3. Under W3, the verdict "the question alone settles it" is exactly the option (d) means, so the correct letter is (d). Under W1 or W2, the same verdict has no matching option, and the reader must go back to the stem to see what the question actually asks.

Two layouts also differ. In 2024 and 2025, each item prints its own directions and its own four options. In 2026, a single directions block covers five items, and the reader must scroll back to find the wording of (d). Check the block header before marking.

### Part C (Core): verdict first, letter second

Every data-sufficiency item has two stages. Keep them separate.

```text
STAGE 1 - VERDICT (pure logic, no letters)
   Does the question alone settle the value?       -> SELF-SUFFICIENT
   Otherwise:
     Does I alone settle it?   Does II alone settle it?
       exactly one settles     -> EXACTLY ONE ALONE
       both settle             -> EITHER ALONE
       neither settles         -> do they settle it TOGETHER?
                                    yes -> BOTH TOGETHER ONLY
                                    no  -> NEITHER SUFFICES

STAGE 2 - LETTER, read from the printed options for THIS item
   EXACTLY ONE ALONE          -> (a)
   EITHER ALONE               -> (b)
   BOTH TOGETHER ONLY         -> (c)
   NEITHER SUFFICES           -> (d) if (d) reads as W1 or W2
   NEITHER SUFFICES, (d) = W3 -> no option fits; re-read the stem
   SELF-SUFFICIENT            -> (d) if (d) reads as W3
   SELF-SUFFICIENT, (d) = W1 or W2 -> no option fits; re-read the stem
```

BOTH TOGETHER ONLY maps to (c) under every printed version. The last line is a warning. If you have found that the question is self-sufficient but the printed (d) says it cannot be answered, you have almost certainly misread the stem. Return to the stem and read what it asks.

### Part D (Core and Advanced): necessary versus sufficient

The format is built on two relations between a condition and a conclusion. In A -> B, the condition A is sufficient for B, because A settles B. The conclusion B is necessary for A, because A cannot hold unless B does.

- **Sufficient.** A statement is sufficient if it forces exactly one answer. "n is a multiple of 12" is sufficient for "n is a multiple of 3".
- **Necessary.** A statement is necessary if the conclusion cannot hold without it. "n is a multiple of 3" is necessary for "n is a multiple of 12", but it is not sufficient, because 9 is a multiple of 3 and not of 12.

A necessary statement narrows the set of possible values without fixing them. Advanced point: two statements that are each necessary may be jointly sufficient, as the multiple-of-6 example shows.

**Worked example (multiple of 12).** Every multiple of 12 is even, so evenness is necessary for divisibility by 12. The number 14 is even and is not a multiple of 12, so evenness is not sufficient. The statement is necessary, not sufficient, which is the pattern the test in this part detects.

**Advanced worked example.** Is the positive integer n a multiple of 6? Statement I: n is a multiple of 3. Statement II: n is even. Statement I alone is not enough, because n = 3 fails and n = 6 passes. Statement II alone is not enough, because n = 2 fails and n = 6 passes. Together, n must be a multiple of 2 and of 3, so it is a multiple of 6. The verdict is "both together only", which is (c) in the printed options of every audited paper. Each statement is necessary; the pair is sufficient.

**Limit.** A reader who treats a necessary statement as sufficient marks (a) or (b) wrongly. Test whether the arrow points the right way. Write the claim as "if the statement holds, does the answer follow?", not "does the answer hold, so the statement follows?".

### The strongest wrong method and the reply

The tempting wrong method is to memorise a letter for each verdict and mark it without reading the printed option. It is fast, and it works on the paper that taught it. It fails on a paper that prints W3 in place of W1. The reply is the layout rule: read the printed (d) each time, and treat the letter as a label on a verdict, not as a fixed fact.

A second wrong method is to read "necessary" as "true of the answer" and therefore sufficient. The reply is the counterexample: find one value that satisfies the statement and fails the question. For the multiple-of-6 example, n = 3 is that counterexample for statement I alone.

### UPSC application

Data-sufficiency items are a major and recurring block in this paper, and they are often printed together. A wrong reading of the option set can cost several items at once. The practical routine is: read the printed options, state the verdict, then map the verdict to a letter. The PYQ families that use this format include integers, shares, class size, prime and factor questions, and two-statement comparisons. They are linked below, grouped by year. The test order for the question, each statement and both together is set out in its own routine.

### Revision points

- Three of the four printed options are stable; the fourth must be read each time.
- W1: (d) says the question cannot be answered even with both statements together.
- W2: (d) says the question cannot be answered using any of the statements, alone or together; nothing works.
- W3: (d) says the question can be answered without any statement.
- In 2026, the options are printed once above a block of five items.
- Stage 1 is the verdict; stage 2 is the letter read from the printed options for that item.
- A question that is settled by itself gives W3's (d) and no letter under W1 or W2.
- In A -> B, A is sufficient for B and B is necessary for A.
- A necessary statement narrows without fixing; it is never sufficient on its own.
- Two individually necessary statements can be jointly sufficient.
- A counterexample to a single statement shows that it is not sufficient.

The verdict tells you which letter to mark. The procedure tells you how to reach the verdict without doing more work than the format requires. The next routine turns that into a timed habit.

### Practice

**MCQ 19**

Some data-sufficiency items carry a fourth option that, in paraphrase, says the question needs no statement at all. Under which situation is that option the correct mark?

- A. Statement I alone settles the question, and statement II alone does not.
- B. Either statement alone settles the question, without the other.
- C. The question is settled by itself, before any statement is tested.
- D. Both are needed together, and neither settles it alone.

**MCQ 19 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Describes exactly one statement being decisive. That is the verdict of option (a), not of the self-sufficiency option.
- **B — Incorrect:** Describes either statement alone being decisive. That is the verdict of option (b).
- **C — Correct:** Under this wording, option (d) is the mark when no statement is needed and the question is settled by itself. The printed option states that situation, and no statement is tested.
- **D — Incorrect:** Describes the pair being necessary. That is the verdict of option (c).

**MCQ 20**

Statement P says that the integer n is a multiple of 5. The question asks whether n is a multiple of 15. Which description of P is correct?

- A. Sufficient: knowing P settles divisibility by 15.
- B. Necessary and sufficient: P is exactly equivalent to divisibility by 15.
- C. Sufficient only if n is also even: P plus evenness settles divisibility by 15.
- D. Necessary, not sufficient: every multiple of 15 satisfies P.

**MCQ 20 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Reads P as settling the question. A multiple of 5 may or may not be a multiple of 15; the number 5 is a counterexample.
- **B — Incorrect:** Treats P as equivalent to the question. The converse fails, since 5 satisfies P without being a multiple of 15.
- **C — Incorrect:** Adds evenness as a condition that seems to finish the job. The number 10 is even and satisfies P, yet it is not a multiple of 15, so P plus evenness still fails.
- **D — Correct:** Every multiple of 15 is a multiple of 5, so P is necessary. The number 5 satisfies P without being a multiple of 15, so P is not sufficient.

**MCQ 21**

Statement I: x cubed equals -8. Statement II: x squared equals 64. The question asks for x. Which verdict is correct?

- A. Statement I alone settles x, and statement II alone does not.
- B. Either statement alone settles x, since both fix its size.
- C. Both are needed together, because neither settles x alone.
- D. Neither settles x, since cube roots are not unique.

**MCQ 21 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** An odd power has exactly one real root, so x cubed = -8 gives x = -2. Statement II gives x = 8 or x = -8, which is not unique, so only statement I settles the value.
- **B — Incorrect:** Assumes that statement II fixes x. It fixes only the size, 8, so the sign stays open.
- **C — Incorrect:** Claims that the pair is needed. Statement I alone already gives x = -2, so statement II adds nothing.
- **D — Incorrect:** Claims that cube roots are not unique. Over the real numbers an odd power has exactly one root, so statement I settles x.

---

## Lesson 8 - The data-sufficiency procedure: testing the question, each statement and both together

Progress: 8/9 | Stage: Core, with Advanced Parts C and D | Subtopic: The data-sufficiency procedure

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the testing sequence stops at the first decision

```text
   START: read the printed options (Lesson 7)
      |
   1. Is the QUESTION alone settled?  ----yes----> stop: self-sufficient verdict
      | no
   2. Does STATEMENT I alone settle it? --yes---> test II alone:
                                                   II fails -> (a)
                                                   II also settles -> (b)
      | no
   3. Does STATEMENT II alone settle it? --yes--> verdict (a), because I alone failed
      | no
   4. Do I and II TOGETHER settle it? --yes----> verdict (c)
      | no
   5. Find a COUNTEREXAMPLE that survives both  -> verdict: NEITHER SUFFICES
```

The sequence has five steps. The procedure stops at the first decisive answer, because nothing after it can change the verdict. The arrows show the branches. Each "no" moves you to the next test. Each "yes" ends the search.

### Plain intuition

To decide whether information is enough, look for a second answer. If you can find two different values that both satisfy the statements and the question, then the information is not enough. If no second value exists, the information is enough. A counterexample is a fast way to find the second value, and it is much cheaper than solving the problem fully.

This is why the procedure stops at uniqueness. Once a second value is ruled out, the question is settled, and a full calculation of the value adds nothing to the verdict.

### Visual: the three questions an advanced item can ask (Advanced)

```text
   DECISION / RELATION PROBLEM
        |
   +------------------+---------------------+
   |                  |                     |
 SUFFICIENCY        COMPARISON           CONSTRAINT
 unique answer?     equalise form        range or optimum
 (I / II / both)    (surd, power, ratio) (min or max under bounds)
```

This is the advanced architecture of the whole session. Sufficiency is decided in this lesson, comparison in Lesson 5, and constraint in Lesson 6. Each branch asks a different question of the same information.

### Part A (Core): the testing order

- **Question first.** Check whether the question is settled without any statement. Under the W3 printed (d), this may be the verdict.
- **Statement I alone.** Test whether it forces one value. If it does, the verdict is (a) or (b), depending on whether II also works.
- **Statement II alone.** Same test for the second statement.
- **Both together.** Only when neither alone works, test whether the pair forces one value.
- **Stop at uniqueness.** Do not evaluate the value beyond what is needed to show that it is unique.

**Worked example.** What is the two-digit number N? Statement I: N is a multiple of 7. Statement II: N lies between 40 and 50. Statement I alone allows 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, which is not unique. Statement II alone allows 41 to 49, which is not unique. Together, the multiples of 7 between 40 and 50 are 42 and 49. Two values survive, so the pair does not settle N. The verdict is that neither suffices, which is (d) under W1 or W2. Check: 42 and 49 are both two-digit multiples of 7 between 40 and 50.

### Part B (Core): counterexamples

A counterexample is one valid value that breaks uniqueness. A single surviving second value is enough.

**Worked example.** What is the integer x? Statement I: x^2 = 25. Statement II: x > 0. Statement I alone gives x = 5 or x = -5, and a second value exists. Statement II alone allows every positive integer, so it fails. Together, x > 0 removes -5, leaving x = 5 only. The verdict is that both are needed, (c).

**Worked example (both statements work alone).** Is the integer n even? Statement I: n^2 is even. Statement II: n + 1 is odd. Statement I alone forces n to be even, because an odd number has an odd square. Statement II alone also forces n to be even, because n + 1 odd means n even. Each statement works alone, so the verdict is (b). No counterexample survives.

**Worked example (two conditions that pin one number).** What is the two-digit number N? Statement I: N is divisible by 11. Statement II: the tens digit of N is 4. Statement I alone gives 11, 22, ..., 99, which is not unique. Statement II alone gives 40 to 49, which is not unique. Together, the two-digit multiples of 11 with tens digit 4 are only 44. The verdict is (c). Limit: the test is uniqueness, so a pair that still leaves two values fails even when each statement narrows the field.

**Worked example (each statement alone).** What is x? Statement I: 3x = 12. Statement II: x + 7 = 11. Each statement alone gives x = 4, so the verdict is (b). Two statements that fix the same value are not a reason for (c).

**Failure condition.** A counterexample must satisfy every condition in the question and every condition in the statement under test. A value that breaks one condition is not a counterexample.

### Part C (Advanced): false uniqueness

A statement that looks as if it fixes a value may allow two values. Squares, absolute values and even powers produce this error. Lesson 4 gave the unique-root test; here it is applied inside the sufficiency procedure.

**Worked example.** What is the positive integer p? Statement I: p^3 = 8. Statement II: p is even. Statement I alone gives p = 2, which is unique over the reals, so it settles the value. Statement II alone allows 2, 4, 6, and so on, which is not unique. The verdict is that exactly one statement settles it, (a).

**Worked example (false uniqueness in a squared statement).** What is the integer m? Statement I: |m + 1| = 4. Statement II: m < 0. Statement I alone gives m = 3 or m = -5, so it is not unique. Statement II alone allows every negative integer, which is not unique. Together, m < 0 removes 3, leaving m = -5. The verdict is (c).

**Failure condition.** Reading |m + 1| = 4 as a single value because the right side is a single number is the false-uniqueness error. The unique-root test is the check.

### Part D (Advanced): hidden dependence

Two statements may look independent and yet be logically nested. The test is whether one statement is a scalar multiple of the other, or whether one statement already implies the other.

**Worked example.** What is x + y? Statement I: x + 2y = 8. Statement II: 3x + 6y = 24. Statement II is three times statement I, so it adds nothing. Two unknowns need two independent relations, and here there is one. The values (8, 0) and (6, 1) both satisfy both statements, and they give x + y = 8 and 7. Neither statement alone, nor both together, settles x + y. The verdict is (d) under W1 or W2.

**Worked example (hidden logical dependence).** What is the two-digit number N? Statement I: N is a multiple of 9 and N < 40. Statement II: the digits of N add to 9. The two-digit multiples of 9 below 40 are 18, 27 and 36, and each has digit sum 9. So statement II is already implied by statement I. Three values survive, and the pair does not settle N. The apparent second condition was a repetition.

**Failure condition.** Hidden dependence is found by asking whether the first statement already forces the second. Asking only whether the two statements look like the same equation misses dependence that is hidden in wording.

### Part E (Core): the self-sufficient question

Sometimes the question alone settles the value, and no statement is needed. Under W3, the verdict is the (d) option. The check is to solve the question as a stand-alone problem and see whether one value survives.

**Factor counts from exponents.** A positive integer with prime factorisation p^a q^b has (a + 1)(b + 1) positive factors. Exactly three factors therefore needs one prime with exponent 2, so the number is p squared. Exactly four factors comes from two patterns: a product of two distinct primes, p q, with exponents 1 and 1 giving 2 x 2 = 4; or a cube of a prime, p^3, with exponent 3 giving 3 + 1 = 4.

**Worked example (counting factors).** How many positive factors does 360 have? Write 360 = 2^3 x 3^2 x 5. The exponents are 3, 2 and 1, so the count is (3 + 1)(2 + 1)(1 + 1) = 4 x 3 x 2 = 24. The question alone settles it, so no statement is needed. A statement that happens to be true of 360 does not change the verdict. Under the printed option that says the question can be answered without any statement, that option is the mark. The method fails if a prime is missed or an exponent is read without adding 1: 3 x 2 x 1 = 6 counts the exponents, not the factors.

**Worked example.** What is the smallest positive integer that is divisible by both 4 and 6? The answer is 12, from the least common multiple of 4 and 6, and no statement is required. A statement that happens to be true of 12 does not change the verdict. The verdict is the self-sufficient option.

**Worked example (a number that is both a square and a cube).** What is the smallest integer greater than 1 that is both a perfect square and a perfect cube? A number that is a square has every prime exponent even, and a number that is a cube has every prime exponent divisible by 3. Both hold only when every exponent is divisible by 6, so the number is a sixth power. The smallest sixth power above 1 is 2^6 = 64. The question alone settles the value. Any statement that happens to be true of 64 leaves the verdict unchanged.

### The strongest wrong method and the reply

The tempting wrong method is to solve the question completely before testing the statements. That turns a decision into a calculation, and it can produce false confidence: a computed value looks like proof of uniqueness even when the method has ignored a second branch. The reply is the stop-at-uniqueness rule. Test for a second value, and stop when none survives.

A second wrong method is to test both statements together before testing each alone. A pair may look decisive when one statement alone is already decisive, and the verdict then should be (a) or (b). The reply is the printed order: I alone, II alone, both together.

### UPSC application

The procedure applies to every data-sufficiency item, whatever its family. In an exam, time is saved by stopping early. The common families, such as digits, ages, primes, factor counts, parity, shares and set membership, each reduce to a relation that the same procedure tests. The PYQ items linked to this lesson include many whose family is recorded only as a two-statement sufficiency item; they are practised with the same order of tests.

### Revision points

- Test the question alone first; it may already be settled.
- Test statement I alone, then statement II alone, then both together.
- Stop at uniqueness; computing the value beyond that is unnecessary.
- A counterexample that satisfies every condition breaks uniqueness.
- Squares and absolute values often allow two values; check the sign.
- An odd power has one real root; an even power has two for a positive constant.
- Hidden dependence: one statement may already imply the other, or be a multiple of it.
- A statement that holds for every value in a set does not settle a value in that set.
- Two statements can be jointly sufficient even when each is merely necessary.
- The verdict comes from the procedure, and the letter comes from the printed options.

The procedure does not depend on the family of the item. The families the paper repeats each reduce to a relation, and the same test then applies.

### Practice

**MCQ 22**

Statement I: 2x = 3y. Statement II: 4x - 6y = 0. The question asks for x. Which verdict is correct?

- A. Statement I alone settles x, since it is one linear relation in two unknowns.
- B. Neither statement settles x, even if both are taken together.
- C. Both together settle x, since they are two relations.
- D. Either statement alone settles x, since both are linear.

**MCQ 22 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Assumes that one relation fixes a value. 2x = 3y has many solutions, such as (3, 2) and (6, 4).
- **B — Correct:** Statement II is twice statement I, so the two relations describe the same line. Two unknowns need two independent relations, so x is not fixed.
- **C — Incorrect:** Assumes that two relations always fix two unknowns. The second relation is a multiple of the first, so the pair is dependent.
- **D — Incorrect:** Assumes that being linear fixes a value. Each relation alone leaves a whole line of solutions.

**MCQ 23**

Statement I: k squared minus 4 equals 5. Statement II: k is positive. The question asks for the integer k. Which verdict is correct?

- A. Statement I alone settles k, since the equation is quadratic with one root.
- B. Either statement alone settles k, since each is a single condition.
- C. Both together settle k, since statement II rules out the root -3.
- D. Both together still leave two values of k, since the sign is free.

**MCQ 23 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Treats the quadratic as having one root. k squared = 9 has two roots, 3 and -3, so statement I alone is not unique.
- **B — Incorrect:** Assumes that statement II alone works. It allows every positive integer, so it is not unique.
- **C — Correct:** Statement I gives k = 3 or k = -3. Statement II removes -3, leaving k = 3. Neither statement alone is unique, but the pair is.
- **D — Incorrect:** Claims that the sign condition leaves two values. Positivity removes -3, so the pair fixes k.

**MCQ 24**

What is the two-digit number N? Statement I: N is a multiple of 7 and N is less than 50. Statement II: the tens digit of N is 2 more than its units digit. Which verdict is correct?

- A. Statement I alone settles N, since it gives one multiple of 7 below 50.
- B. Statement II alone settles N, since the digit gap fixes the number.
- C. Neither statement settles N, even together, since several multiples remain.
- D. Both together settle N, though neither alone does.

**MCQ 24 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Miscounts the multiples of 7 below 50. There are six of them: 14, 21, 28, 35, 42 and 49.
- **B — Incorrect:** Treats the digit gap as fixing the number. A gap of 2 alone gives 20, 31, 42, 53, 64, 75, 86 and 97.
- **C — Incorrect:** Assumes that the pair leaves several candidates. Only one candidate survives both conditions, so the pair does not leave several.
- **D — Correct:** Among the multiples of 7 below 50, only 42 has a tens digit 2 more than its units digit (4 and 2). So both statements together settle N, while neither alone does.

**MCQ 25**

What is the two-digit number N? Statement I: N is even and a multiple of 9. Statement II: N is less than 50. Which verdict is correct?

- A. Both together still leave two values of N, namely 18 and 36.
- B. Statement I alone settles N, since it leaves one even multiple of 9.
- C. Statement II alone settles N, since it leaves a single two-digit number.
- D. Both together settle N, since a multiple of 18 below 50 is unique.

**MCQ 25 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** An even multiple of 9 is a multiple of 18. The two-digit ones below 50 are 18 and 36, so the two statements together leave two values, and the question is not settled.
- **B — Incorrect:** Reads an even multiple of 9 as a single value. The two-digit multiples of 18 are 18, 36, 54, 72 and 90: five candidates, not one.
- **C — Incorrect:** Treats the bound below 50 as settling the number. Statement II alone admits every two-digit number from 10 to 49, so many candidates remain.
- **D — Incorrect:** Claims a unique multiple of 18 below 50. Both 18 and 36 satisfy the two statements, so the pair is not unique.

---

## Lesson 9 - Data-sufficiency families: digits, ages, primes, factor counts, parity, shares and set membership

Progress: 9/9 | Stage: Core and Advanced | Subtopic: Data-sufficiency families

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Visual: the families and what each statement usually supplies

```text
FAMILY               WHAT THE STATEMENTS USUALLY SUPPLY            WHAT TO CHECK BEFORE CONCLUDING
-------------------  ---------------------------------------------  ------------------------------------------
DIGITS               sum, difference, place, or a multiple          digits 0-9; two-digit has tens >= 1
AGES                 a difference, a sum, or a ratio                 a time shift applies to both people
PRIMES               a square, a prime label, or a bound            positive integers; 1 is not prime
FACTOR COUNTS        the number of divisors                         the exponent pattern; p^2 has 3 factors
PARITY               even or odd, of one term or a sum              the parity of a sum or product
SHARES               a fraction of a total, or a total              the fractions must add to the whole
SET MEMBERSHIP       sizes of groups and of the union               inclusion-exclusion; the overlap
```

The table is a planning aid, not a template. Each family has its own traps. The first column names the family, and the second column says what a statement typically provides. The third column is the check that prevents a false uniqueness or an unnoticed domain restriction.

### Plain intuition

Every family asks one question: does this information fix a single value? The families differ only in the vocabulary of the statements. A digit statement is a statement about place value. An age statement is a statement about differences over time. A factor-count statement is a statement about the exponents of primes. The procedure from Lesson 8 applies to each family without change, once the vocabulary is translated into a relation.

### Part A: digits and place value

A digit statement becomes an equation in the tens digit t and the units digit u, with 0 <= t, u <= 9 and t >= 1 for a two-digit number.

**Worked example.** What is the two-digit number N? Statement I: its digits add to 12. Statement II: N is odd. Statement I alone allows 39, 48, 57, 66, 75, 84 and 93. Statement II alone allows every odd two-digit number. Together, 39, 57, 75 and 93 survive, all odd and with digit sum 12. Several values survive, so the verdict is (d) under W1 or W2.

**Worked example (single answer, with limits).** Which two-digit number has digits that sum to 9 and differ by 9? Digits that differ by 9 must be 0 and 9, since no other pair of digits is 9 apart. With the tens digit at least 1, the number is 90, and its digits do sum to 9. Limit: the difference is between the two digits, not between the number and its reversal, so the order of the digits matters.

**Trap.** Place-value errors appear when a digit statement is read as a product. The digits 3 and 9 give the number 39, not 27.

### Part B: ages

An age statement becomes an equation in the present ages. A difference of ages does not change over time, but a ratio does. The time shift must be applied to both people.

**Worked example.** How old is A? Statement I: A is 6 years older than B. Statement II: the sum of their ages is 30. Statement I alone allows any pair with a difference of 6. Statement II alone allows any pair with a sum of 30. Together, 2A = 36, so A = 18 and B = 12. The pair settles A.

**Trap.** Reading "older by 6" as a ratio, or applying the time shift to only one person, gives a wrong relation that may still look consistent.

### Part C: primes and the sign of an integer

Prime questions are about positive integers. The number 1 is not prime, and the square of a prime has exactly three positive factors. A statement that restricts an integer to a set of squares may settle a value once the sign is fixed.

**Worked example.** What is the positive integer p? Statement I: p^2 = 25. Statement II: p is prime. Statement I alone gives p = 5, because p is positive. Statement II alone allows every prime. So statement I alone settles p. The positivity condition is the decisive detail: without it, the square would give p = -5 as well.

**Trap.** Forgetting that a prime is positive and that 1 is not prime produces a wrong count of candidates.

### Part D: factor counts and exponent patterns

The number of positive factors of n = p^a x q^b is (a + 1)(b + 1), and it is the product of one more than each exponent. Statements about the number of factors are therefore statements about exponent patterns.

**Worked example.** What is the integer n? Statement I: n lies between 20 and 40 and has exactly four positive factors. Statement II: n is a perfect cube. Statement I alone allows 21, 22, 26, 27, 33, 34, 35, 38 and 39, since each is a product of two distinct primes or the cube of a prime. Statement II alone allows 1, 8, 27, 64 and every other cube. Together, the only cube between 20 and 40 is 27 = 3^3, which has (3 + 1) = 4 factors, so the pair settles n.

**Trap.** A pattern of exponents is not a single number. Listing the factor count of one example, such as 12, and concluding that every number with the same count is 12 is a false uniqueness error.

### Part E: parity

Parity is decided by even and odd rules. An even number plus an odd number is odd, and a sum or product of two numbers has a parity that depends on both. A parity question is often answerable with one statement and the rule for sums.

**Worked example.** Is m + n even? Statement I: m is even. Statement II: n is odd. Statement I alone leaves n unknown, so the parity of m + n is not fixed. Statement II alone leaves m unknown, so it is not fixed either. Together, an even number plus an odd number is odd, so m + n is always odd, and the answer is determined: "no". The two statements together settle the question.

**Trap.** A parity statement about one term is not enough for a sum. Check the parity of the whole expression, not of one of its parts.

### Part F: shares and fractions

A share statement fixes a part of a whole by a fraction. The fractions of a whole must add to one, and a total must be stated or implied before a value can be found.

**Worked example.** What is A's share of a sum? Statement I: A receives two-fifths of the total. Statement II: the total is 200. Statement I alone gives a fraction without a total. Statement II alone gives a total without a fraction. Together, A's share is 2/5 of 200, which is 80. The two statements together settle the share.

**Trap.** A fraction statement gives a ratio of the whole. Without the whole, no amount is determined.

### Part G: set membership

Set questions use the rule for the union of two groups: the size of the union equals the sum of the group sizes minus the overlap. A statement about the union and a statement about the group sizes together give the overlap.

**Worked example.** How many students belong to both groups? Statement I: 50 students belong to at least one group. Statement II: 30 belong to the first group and 25 to the second. Statement I alone gives the union but no group sizes. Statement II alone gives group sizes but no union. Together, the overlap is 30 + 25 - 50 = 5, so the two statements together settle it.

**Trap.** A group size is not the union. Check whether a statement describes one group, both groups, or the union before using it.

### Part H: five further families in their true formats

One family is a statement set, and the other four are single-answer items. The same habit serves all five: translate the vocabulary into a relation, check the domain, and then decide what the item asks.

- **Statement sets that fix a total.** Let a be the number of 4-run boundaries and b the number of 6-run boundaries, with a and b non-negative whole numbers. Question: how many 4-run boundaries were hit? Statement I: every run came from a 4 or a 6, and the total is 32 runs. Statement II: there were 7 boundaries in all. Statement I alone allows (a, b) = (8, 0), (5, 2) and (2, 4), which is not unique. Statement II alone is not unique either. Together, 4a + 6(7 - a) = 32 gives a = 5 and b = 2. Neither statement alone settles the count, but together they do. Limit: the counts must be non-negative whole numbers, which is what removes the other candidates.
- **Comparisons of real numbers (single answer).** Which is larger, the cube root of 9 or 2? Cube both sides: 9 against 2 cubed, which is 8. Since 9 is greater than 8, and cubing keeps the order of real numbers, the cube root of 9 is larger. Limit: cubing keeps order for every real number, but squaring does so only for non-negative numbers, so a squared comparison needs the signs checked first.
- **Bounded variables (single answer).** Which integers n satisfy both -3 < n <= 5 and n > 1? Intersect the two ranges and keep each end as given: the answer is 2, 3, 4 and 5, four integers. Limit: the open end -3 is excluded and the closed end 5 is included. A range is a set of values, so a question that asks for one integer must narrow the range further.
- **Optimising under linear limits (single answer).** What is the largest value of 2x + y for non-negative whole numbers with x + 3y at most 9? The points (9, 0), (6, 1), (3, 2) and (0, 3) give 18, 13, 8 and 3. No point can beat 18, because 2x + y is at most 2x + 6y, which is at most 2 times 9 = 18. The maximum is 18, at x = 9 and y = 0. Limit: the bound uses only y being non-negative, so it holds for every point in the region.
- **Fixed charge plus rate (single answer).** A phone plan charges a fixed 50 rupees plus 2 rupees per minute. A bill of 110 rupees shows how many minutes? Subtract the fixed charge first: 110 - 50 = 60, and 2m = 60 gives m = 30. Limit: dividing 110 by 2 gives 55, which ignores the fixed charge, so the fixed part must come out before the rate is divided.

### The strongest wrong method and the reply

The tempting wrong method is to treat each family as a different skill, with its own rule. The reply is that the families share one procedure. The vocabulary changes, but the question is always whether a second value survives. A learner who has memorised a rule for each family has memorised more than is needed and will miss a case that does not fit the rule.

A second wrong method is to assume that a family's typical statement always settles the value. A digit statement, an age statement or a factor count may or may not be enough. The reply is to test each statement with the procedure of Lesson 8, not to rely on the family name.

### UPSC application

Data-sufficiency items in past papers fall into the families above, and many of them are repeated in each year. The learner who can translate the vocabulary of a family into a relation can apply the same procedure to an unfamiliar item. Number-property facts from the number-systems topic, such as parity, divisibility and factor counts, do much of the work in these families, and the same sufficiency test applies to them. The routine is: name the family, translate each statement into a relation, check the domain, test each statement alone, test both, and stop at uniqueness. The PYQ section links each item to the family it belongs to, and it gives the answer approach, not the answer.

### Revision points

- Every family is a translation of statements into a relation, followed by the same procedure.
- Digits: check 0 to 9 and tens digit at least 1; a digit sum does not fix the number.
- Ages: a difference is fixed over time; a ratio is not; apply time shifts to both.
- Primes: positive integers, with 1 not prime; the square of a prime has three factors.
- Factor counts: use the exponent pattern; a count does not fix the number.
- Parity: check the parity of the whole sum or product.
- Shares: a fraction needs a total before an amount is determined.
- Set membership: union equals the sum of the groups minus the overlap.
- A typical statement in a family may still leave two values; test it.
- Stop at uniqueness in every family.

The lesson closes the teaching sequence. What remains is practice, remediation and a consolidated record of the methods. The learner should now be able to read the printed options, test the question and the statements in order, and translate any family into a relation.

### Practice

**MCQ 26**

What is the two-digit number N? Statement I: its digits sum to 9. Statement II: it is greater than 60. Which verdict is correct?

- A. Statement I alone settles N.
- B. Neither statement settles N, even together.
- C. Either statement alone settles N.
- D. Both together settle N, since the digit sum fixes it.

**MCQ 26 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Treats the digit sum as fixing the number. Nine two-digit numbers have digit sum 9, from 18 to 90.
- **B — Correct:** The digit sum gives nine candidates. Being greater than 60 leaves 63, 72, 81 and 90. Neither statement alone is unique, and together they still leave four values.
- **C — Incorrect:** Assumes that either condition alone is decisive. Each leaves several candidates.
- **D — Incorrect:** Assumes that the digit sum fixes the number once combined with the bound. Four candidates remain, so it does not.

**MCQ 27**

A sum of 240 rupees is divided between Asha and Bina in the ratio 3:5. How much does Bina receive?

- A. 90 rupees
- B. 48 rupees
- C. 150 rupees
- D. 200 rupees

**MCQ 27 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Gives Asha's share, 240 x 3/8 = 90. The question asks for Bina's share, which is the part with the 5.
- **B — Incorrect:** Divides the total by the second ratio number alone, 240 / 5 = 48. A share must use the whole ratio total, 3 + 5 = 8, not one of its parts.
- **C — Correct:** The ratio total is 3 + 5 = 8, and Bina's part is 5/8. So Bina receives 240 x 5/8 = 150. Check: 90 + 150 = 240, and 90 : 150 is 3 : 5.
- **D — Incorrect:** Uses 6 as the ratio total, giving 240 x 5/6 = 200. The total of the ratio is 8, since 3 + 5 = 8, so the denominator is wrong.

**MCQ 28**

A group of 40 students is surveyed. 25 play cricket, 18 play football and 9 play both games. How many play neither game?

- A. 15 students
- B. 34 students
- C. 9 students
- D. 6 students

**MCQ 28 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Counts everyone who does not play cricket, 40 - 25 = 15. That group still includes the football players, who play a game and so are not in the neither group.
- **B — Incorrect:** Gives the union, 25 + 18 - 9 = 34, which is the number who play at least one game. The question asks for those who play neither, so the union must be subtracted from 40.
- **C — Incorrect:** Reports the overlap of 9, the students who play both games. That is a count inside the union and does not answer the neither question.
- **D — Correct:** The union is 25 + 18 - 9 = 34, because the 9 who play both are counted twice when the two groups are added. So neither = 40 - 34 = 6. Check: 34 + 6 = 40.

---

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

This section links the Prelims CSAT questions in algebra, inequalities and data sufficiency from 2013 to 2026. One item, 2023 Q26, is also a Number Systems question and is listed here for the method it shares with this topic. Each link opens the question-level entry of its year file. Nothing here reproduces a question, an option, a letter or a worked solution, and no answer key appears in this section.

Three points govern how to use the list.

1. **Demand before calculation.** The label in bold names the demand type of the question as its stem presents it. Identify that demand first; it tells you which lesson's method applies.
2. **Format and demand.** The format says whether the item is a single-answer question or a statement set. A statement set needs each statement tested alone before the verdict is read.
3. **The approach is a route, not a result.** It names the test to run. Run the test on the numbers in the stem and check the result by a second route.

The 2026 paper is provisional, so its entries record the method only and make no claim about any option. The 2013 to 2017 entries name the demand type of each item, and they are listed here because they test this topic's methods. The 2018 entries name the demand type of each item, and each approach line states the test to run.

## How the items add up

| Span | Items |
|---|---:|
| 2013 to 2017 | 9 |
| 2018 to 2026 | 74 |
| Total | 83 |

| Covered in | Items |
|---|---:|
| Lesson 1 | 13 |
| Lesson 2 | 9 |
| Lesson 3 | 6 |
| Lesson 4 | 0 |
| Lesson 5 | 8 |
| Lesson 6 | 6 |
| Lesson 7 | 0 |
| Lesson 8 | 23 |
| Lesson 9 | 18 |

Each item appears once. The 2013 paper has no item listed for this topic, so no 2013 heading appears below.

## 2014 — 1 item

- [Q65](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q065) — **Largest holding from linked totals**. Format: single-answer objective item. Demand and approach: Write each holding with one unknown, use the stated total and the comparisons, and test which holding is largest. Covered in: Lesson 2.

## 2015 — 1 item

- [Q51](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q051) — **Set relations from stated counts**. Format: single-answer objective item. Demand and approach: Write the counts of each region of the two sets, use the stated ratios, and test each conclusion against the derived counts. Covered in: Lesson 9.

## 2016 — 3 items

- [Q14](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q014) — **Flowers and bees from two landing rules**. Format: single-answer objective item. Demand and approach: Name the flowers and the bees, write the two landing conditions as linear relations, and solve. Covered in: Lesson 2.
- [Q29](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q029) — **Class size from a total contribution**. Format: single-answer objective item. Demand and approach: Let the class size be the unknown, write the total as the square of the size plus the extra amount, and solve for a whole number. Covered in: Lesson 1.
- [Q50](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q050) — **Maximum area under a fixed sum of sides**. Format: single-answer objective item. Demand and approach: Write the area as the product of the two sides, use the fixed sum, and find the largest product. Covered in: Lesson 6.

## 2017 — 4 items

- [Q14](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q014) — **Highest income from comparative sums**. Format: single-answer objective item. Demand and approach: Write each stated comparison as an inequality between sums, and test which income must exceed all others. Covered in: Lesson 1.
- [Q30](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q030) — **Comparison of two weighted mixtures**. Format: single-answer objective item. Demand and approach: Write P and Q as combinations of A and B with the stated weights, use A greater than B, and compare P with Q. Covered in: Lesson 5.
- [Q40](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q040) — **Highest marks from ordered comparisons (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write each stated comparison as an ordering, then test which person must be above all others. Covered in: Lesson 8.
- [Q74](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q074) — **Total income from ratios and savings**. Format: single-answer objective item. Demand and approach: Let incomes and expenses be multiples of the stated ratio terms, form each saving as income minus expense, and solve the two savings equations. Covered in: Lesson 2.

## 2018 — 7 items

- [Q2](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q02) — **Series with an unknown symbol**. Format: single-answer objective item. Demand and approach: Write the sum as one equation in the symbol, solve it, and check the result against the terms shown. Covered in: Lesson 1.
- [Q23](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q23) — **Range of a difference of squares**. Format: single-answer objective item. Demand and approach: Find the range of X squared and of Y squared from their intervals, then the range of their difference, and select the matching range. Covered in: Lesson 3.
- [Q24](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q24) — **Largest of candidate expressions**. Format: single-answer objective item. Demand and approach: Compare the candidate expressions for the largest value, using the order of X and Y and the restriction to natural numbers other than 1. Covered in: Lesson 5.
- [Q34](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q34) — **Digit values with a reversal condition**. Format: single-answer objective item. Demand and approach: Write the three digits as unknowns, use the digit sum and the middle digit, and solve the reversal condition for the difference of the outer digits. Covered in: Lesson 1.
- [Q37](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q37) — **Conclusion from three order relations**. Format: single-answer objective item. Demand and approach: Test which conclusion holds in every case the three order relations allow. Covered in: Lesson 3.
- [Q38](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q38) — **Total sale from quantities and prices**. Format: single-answer objective item. Demand and approach: Write the sale as a sum of products of quantity and price, and simplify. Covered in: Lesson 1.
- [Q77](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q77) — **Sign implications from a difference equation**. Format: single-answer objective item. Demand and approach: Test each numbered statement about signs with a counterexample; keep only those forced by the equation. Covered in: Lesson 2.

## 2019 — 6 items

- [Q18](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q18) — **Birth year from ages at two dates**. Format: single-answer objective item. Demand and approach: Write the two ages at each date as linear relations in the birth year, and solve. Covered in: Lesson 1.
- [Q37](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q37) — **Conclusion that holds at every bound**. Format: single-answer objective item. Demand and approach: Track the bounds of x and y through each candidate relation, and keep only the relations that hold throughout. Covered in: Lesson 3.
- [Q38](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q38) — **Age at marriage from a chain of ages**. Format: single-answer objective item. Demand and approach: Write each family member's age relative to Ena, convert the stated gaps into equations, and solve for the father's age at marriage. Covered in: Lesson 1.
- [Q50](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q50) — **Fraction after the same addition to both parts**. Format: single-answer objective item. Demand and approach: Compare the original fraction with the new one by cross-multiplying with positive quantities. Covered in: Lesson 5.
- [Q58](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q58) — **Parity of a product from two statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Test whether each statement, with the question, forces the parity of the product, using the primality conditions. Covered in: Lesson 8.
- [Q69](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q69) — **Piece lengths from relative lengths**. Format: single-answer objective item. Demand and approach: Name the three single-digit odd primes, write each piece as a relation to the others, and solve for the original length. Covered in: Lesson 1.

## 2020 — 7 items

- [Q9](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q09) — **Largest of four linked natural numbers**. Format: single-answer objective item. Demand and approach: Let the common value be t, write each of p, q, r and s in terms of t, and compare the four expressions. Covered in: Lesson 2.
- [Q16](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q16) — **Digit values from a four-digit sum**. Format: single-answer objective item. Demand and approach: Write each four-digit number in place-value form with unknown digits, use the column sums and the digit bounds, and test the candidates. Covered in: Lesson 9.
- [Q17](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q17) — **Count bound from two statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the largest and smallest totals each statement allows, and test whether the question's threshold is forced. Covered in: Lesson 8.
- [Q28](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q28) — **Largest of four from ordering statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write each statement as an ordering of P, Q, R and S, and test which number is forced to be the largest. Covered in: Lesson 8.
- [Q29](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q29) — **Unique natural number from prime and remainder statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Restrict the range, test each statement on the candidates, and check whether the question's value is forced. Covered in: Lesson 8.
- [Q30](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q30) — **Two numbers from a sum and a product (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the two statements as the sum and the product of the two numbers, and test whether the pair is forced. Covered in: Lesson 8.
- [Q79](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q79) — **Empty-vessel weight from two fill states**. Format: single-answer objective item. Demand and approach: Write the empty weight and the full weight, express the one-third filled weight as a relation, and solve the two linear equations. Covered in: Lesson 2.

## 2021 — 6 items

- [Q8](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q08) — **Exponential model from a doubling rule**. Format: single-answer objective item. Demand and approach: Write the population after n years as the starting value times the doubling factor raised to the number of doubling periods, and match the expression to the given form. Covered in: Lesson 5.
- [Q38](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q38) — **Rank from ordered positions (statement set)**. Format: statement set (data sufficiency). Demand and approach: Convert each position statement into a rank from the top or bottom of the class, and test whether the requested rank is forced. Covered in: Lesson 8.
- [Q39](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q39) — **Heaviest person from ordering statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write each weight comparison as an ordering, combine the two statements, and test whether one person is forced to be heaviest. Covered in: Lesson 8.
- [Q47](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q47) — **Day of the month from weekday statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Use the weekdays of the given days to fix the calendar, test each statement, and identify the requested day. Covered in: Lesson 8.
- [Q58](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q58) — **Wrong count from marks and attempts**. Format: single-answer objective item. Demand and approach: Let the correct count be c, write the total marks as a linear equation in c, solve it, and report the wrong count. Covered in: Lesson 1.
- [Q77](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q77) — **Age relations with two numbered statements**. Format: single-answer objective item. Demand and approach: Let the present ages be the unknowns, convert the birth-time statement into an equation, then test each numbered statement against the solution. Covered in: Lesson 1.

## 2022 — 9 items

- [Q19](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q19) — **Integer status from two statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Test whether each statement alone, and both together, force x to be an integer. Covered in: Lesson 8.
- [Q25](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q25) — **Family relation from two statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Place each person in the stated relations, and test whether the requested relation is forced. Covered in: Lesson 8.
- [Q28](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q28) — **Coins undone through repeated halving**. Format: single-answer objective item. Demand and approach: Undo each step in reverse: write the count before a step in terms of the count after it, using the rule that step states, and apply the undo once per step from the final count. Covered in: Lesson 1.
- [Q37](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q37) — **Distance from statements about three places (statement set)**. Format: statement set (data sufficiency). Demand and approach: Place the three places from the statements, and test whether the requested distance is forced. Covered in: Lesson 8.
- [Q48](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q48) — **Seating from equal spacing and statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Place the six persons at equal positions around the table, convert each statement into a position relation, and test who sits at the stated place. Covered in: Lesson 8.
- [Q49](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q49) — **Age of a person from two statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write each statement as a relation among the ages, and test whether the age of the named person is forced. Covered in: Lesson 8.
- [Q50](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q50) — **Lecture in a stated period (statement set)**. Format: statement set (data sufficiency). Demand and approach: Place the six lectures in the periods, convert each statement into an ordering, and test the requested period. Covered in: Lesson 8.
- [Q60](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q60) — **Percentage relations between three numbers**. Format: single-answer objective item. Demand and approach: Write each sum statement as a linear relation among x, y and z, and test whether the requested comparison is forced. Covered in: Lesson 5.
- [Q78](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q78) — **Consecutive integers with sum equal to product**. Format: single-answer objective item. Demand and approach: Let the middle integer be t, write the stated relation in t, factor rather than divide, and count the admissible integer solutions. Covered in: Lesson 2.

## 2023 — 6 items

- [Q26](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q26) — **Maximum product of two sums from four digits**. Format: single-answer objective item. Demand and approach: Write the product as a product of two sums with a fixed total, use the digit bounds, and test the digit choices near the balanced split. Covered in: Lesson 6.
- [Q56](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q56) — **Sign and square comparisons (statement set)**. Format: statement set (data sufficiency). Demand and approach: Test whether the sign of the product and the comparison of squares force the order of p and q, including cases where p and q have different signs. Covered in: Lesson 8.
- [Q57](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q57) — **Comparison of two expressions from sign statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Subtract the two expressions to get a difference in terms of p, q and r, and test whether the stated signs force its sign. Covered in: Lesson 8.
- [Q58](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q58) — **Set size from drink counts (statement set)**. Format: statement set (data sufficiency). Demand and approach: Apply the union rule to the groups described, and test whether the statements fix the total number of persons. Covered in: Lesson 9.
- [Q59](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q59) — **Three-digit number from digit statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the three digits as unknowns, use the digit-sum and divisibility conditions, and test whether the number is forced. Covered in: Lesson 9.
- [Q60](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q60) — **Youngest age from spacing and average (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the ages with the stated common step in terms of the youngest age, convert each statement into an equation, and test whether the youngest age is forced. Covered in: Lesson 9.

## 2024 — 13 items

- [Q35](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q35) — **Count of two-digit values from a reversal sum**. Format: single-answer objective item. Demand and approach: Write X and its reversal in place-value form, so their sum is eleven times the digit sum; find the digit sums that match the stated maximum, and count the values of X. Covered in: Lesson 1.
- [Q50](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q50) — **Linear cost relations and consistency**. Format: single-answer objective item. Demand and approach: Write each price relation as a linear equation, eliminate variables from the given relations, and test whether each statement follows. Covered in: Lesson 2.
- [Q59](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q59) — **Natural-number values from statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the stated relations for m and n, restrict them to natural numbers, and test whether the pair is forced. Covered in: Lesson 9.
- [Q60](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q60) — **Download time from a transfer rate (statement set)**. Format: statement set (data sufficiency). Demand and approach: Convert the file size and the transfer rate into a time relation, and test whether the statements fix the required quantity. Covered in: Lesson 8.
- [Q64](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q64) — **Unique distinct natural pair from two statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write each condition as an equation in x and y, restrict to distinct natural numbers, and test whether one pair is forced. Covered in: Lesson 9.
- [Q65](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q65) — **Least share from fractional statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Express each share as a fraction of the total, convert both statements to shares of one total, and test whether the least share is forced. Covered in: Lesson 9.
- [Q66](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q66) — **Class size from an average and extreme-mark statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the average as total marks over the number of students, and test whether the statements fix that number. Covered in: Lesson 9.
- [Q67](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q67) — **Three primes with a prime sum (statement set)**. Format: statement set (data sufficiency). Demand and approach: Restrict the three numbers to distinct primes, examine the parity of the sum, and test whether the statements fix the triple. Covered in: Lesson 9.
- [Q68](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q68) — **Integer status of a sum from two parts (statement set)**. Format: statement set (data sufficiency). Demand and approach: Test whether each statement, alone and together, forces the sum to be an integer; whole-number parts do not by themselves fix the sum. Covered in: Lesson 9.
- [Q69](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q69) — **Article price from a total and a minimum price (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the three prices as unknowns with their total and the stated minimum, and test whether the price of p is forced. Covered in: Lesson 8.
- [Q70](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q70) — **Comparison of scores from ordered statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write each statement as an ordering of the four scores, and test whether P's score is forced above Q's. Covered in: Lesson 8.
- [Q73](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q73) — **Ages from digit reversal and a difference (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the two ages in place-value form with reversed digits, convert each statement into a relation, and test whether the difference is forced. Covered in: Lesson 9.
- [Q76](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q76) — **Coded relations on symbols**. Format: single-answer objective item. Demand and approach: Translate each coded symbol into its ordinary relation, then test each stated consequence one by one. Covered in: Lesson 3.

## 2025 — 11 items

- [Q19](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q19) — **Chained comparisons and their consequences**. Format: single-answer objective item. Demand and approach: Expand each chain of comparisons into pairwise relations, and test whether the stated conclusion holds in every case the chain allows. Covered in: Lesson 3.
- [Q26](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q26) — **Ratio of extreme values of a sum and a difference**. Format: single-answer objective item. Demand and approach: Find the largest sum and the smallest difference from the stated bounds of x and y, then form their ratio. Covered in: Lesson 6.
- [Q68](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q68) — **Smallest one-digit number with four factors (statement set)**. Format: statement set (data sufficiency). Demand and approach: Test the one-digit numbers in order for exactly four factors, and check whether each statement fixes the first match. Covered in: Lesson 9.
- [Q69](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q69) — **Digit values from a two-digit product equation (statement set)**. Format: statement set (data sufficiency). Demand and approach: Write the two-digit products in place-value form, use the digit bounds, and test whether each statement fixes the digit Q. Covered in: Lesson 9.
- [Q70](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q70) — **Kinship relation from family statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Place each person in the family tree from the statements, and test whether the relation between P and Q is forced. Covered in: Lesson 8.
- [Q73](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q73) — **Match outcome from goal statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Compare the goal difference and the time left with the goals in each statement, and test whether the outcome is forced. Covered in: Lesson 8.
- [Q74](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q74) — **Sign of a quantity from order statements (statement set)**. Format: statement set (data sufficiency). Demand and approach: Rewrite the expression as a square of a difference or a product, and test whether each order statement fixes its sign. Covered in: Lesson 8.
- [Q75](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q75) — **Ratio of three runs in continued proportion**. Format: single-answer objective item. Demand and approach: Write the continued-proportion relation among X, Y and Z with the total, and compare the stated values. Covered in: Lesson 5.
- [Q76](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q76) — **Maxima of a product under two lower bounds**. Format: single-answer objective item. Demand and approach: Find the largest product under each set of bounds separately, and compare the two maxima. Covered in: Lesson 6.
- [Q77](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q77) — **Minimum average and product of consecutive integers**. Format: single-answer objective item. Demand and approach: Write the sets of consecutive integers allowed by each lower bound, find the minimum average and the minimum product, and compare them. Covered in: Lesson 6.
- [Q79](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q79) — **Powers and roots on the unit interval**. Format: single-answer objective item. Demand and approach: For a value between 0 and 1, compare each power or root with the value itself, and test each stated statement. Covered in: Lesson 5.

## 2026 — 9 items (provisional paper)

- [Q1](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q01) — **Denomination count from a received total**. Format: statement set (data sufficiency). Demand and approach: Write the total as a sum over the denominations, and test whether the stated amount forces the presence of the coin. Covered in: Lesson 9.
- [Q2](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q02) — **Comparison of two distinct real numbers**. Format: statement set (data sufficiency). Demand and approach: Compare the two numbers in a common form, and test whether the comparison is forced for every admissible pair. Covered in: Lesson 5.
- [Q3](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q03) — **Parity of a variable from integer relations**. Format: statement set (data sufficiency). Demand and approach: Write the relations among the integers, and test whether the stated conditions force the parity of x. Covered in: Lesson 9.
- [Q4](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q04) — **Membership of a combined collection**. Format: statement set (data sufficiency). Demand and approach: Write the membership conditions as set relations, and test whether every element of the combined collection is forced into one collection. Covered in: Lesson 9.
- [Q5](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q05) — **Primality from integer conditions**. Format: statement set (data sufficiency). Demand and approach: Test whether the stated integer conditions force x to have exactly two positive factors. Covered in: Lesson 9.
- [Q8](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q08) — **Weights from linear sums**. Format: single-answer objective item. Demand and approach: Write the stated sums as linear equations, eliminate unknowns, and compare the resulting weights. Covered in: Lesson 2.
- [Q21](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q21) — **Ordered inequalities on a bounded interval**. Format: single-answer objective item. Demand and approach: Test each statement at the endpoints of the interval and at a sample interior point, keeping only statements that hold throughout. Covered in: Lesson 3.
- [Q38](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q38) — **Marks under two marking schemes**. Format: single-answer objective item. Demand and approach: Let c be correct and w wrong; write the score under each scheme as a linear equation, and solve the two equations together. Covered in: Lesson 1.
- [Q80](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q80) — **Maximum earning under a distance cap**. Format: single-answer objective item. Demand and approach: Write the earnings as a linear function of deliveries and distance under the cap, and test the admissible corners. Covered in: Lesson 6.

## Reading the 2026 entries

The 2026 entries record the method only. The provisional paper has no confirmed key in this session, and no entry claims that any option is right or wrong. The approach column is the route to take; the learner checks the route on the printed stem.

---

# CUMULATIVE MCQS

Four of these six items join methods from more than one lesson (29, 30, 32 and 34). Items 31 and 33 apply one lesson's method in a new setting. They are numbered on from the last lesson item, and none of them repeats a lesson item. Attempt each before you open its explanation.

**MCQ 29**

Positive integers x and y satisfy x + 2y = 11 and y > x. Given also that x > 2, what is x?

- A. 3, with y = 4
- B. 1, with y = 5
- C. 7, with y = 2
- D. 4, the value of y

**MCQ 29 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** From x = 11 - 2y and x > 2, y is at most 4. From y > x, 3y > 11, so y is at least 4. Hence y = 4 and x = 3. Check: 3 + 8 = 11, 4 > 3 and 3 > 2.
- **B — Incorrect:** Takes y = 5, which gives x = 1. That value fails x > 2, so the branch is excluded.
- **C — Incorrect:** Takes x = 7, which gives y = 2 from x + 2y = 11. The pair satisfies the equation, but y > x fails, since 2 is less than 7.
- **D — Incorrect:** Reports y = 4, the value of y, as the answer. The question asks for x, and with y = 4 the value of x is 3.

**MCQ 30**

How many integers n satisfy |n - 1| < 4 and 3n - 2 >= 4?

- A. 9
- B. 3
- C. 2
- D. 5

**MCQ 30 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Ignores the second condition and uses the non-strict band |n - 1| <= 4, which runs from -3 to 5: nine integers.
- **B — Correct:** |n - 1| < 4 gives -3 < n < 5, so n runs from -2 to 4: seven integers. The condition 3n - 2 >= 4 means n >= 2, which leaves 2, 3 and 4: three integers. Check: 3(2) - 2 = 4 satisfies the condition, while 3(1) - 2 = 1 does not.
- **C — Incorrect:** Uses n > 2 instead of n >= 2, which drops n = 2. Check: 3(2) - 2 = 4 satisfies the condition, so 2 belongs in the count.
- **D — Incorrect:** Reverses the second condition to n <= 2, which within the band gives -2, -1, 0, 1 and 2: five integers.

**MCQ 31**

What is the largest integer n that satisfies 3 - 2n > -5 and n/2 >= -1?

- A. 4
- B. 6
- C. 3
- D. -2

**MCQ 31 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Reads the strict inequality as allowing n = 4. Dividing 3 - 2n > -5 by -2 gives n < 4, and n = 4 gives 3 - 8 = -5, which is not greater than -5.
- **B — Incorrect:** Counts the admissible integers instead of asking for the largest. They are -2, -1, 0, 1, 2 and 3: six integers, and six is a count, not a value of n.
- **C — Correct:** 3 - 2n > -5 gives n < 4, with the sign reversed on dividing by -2. The condition n/2 >= -1 gives n >= -2. The largest integer below 4 is 3. Check: 3 - 6 = -3 is greater than -5, and 3/2 >= -1.
- **D — Incorrect:** Takes the smallest admissible integer, -2, instead of the largest. The question asks for the upper end of the set.

**MCQ 32**

Statement I: 3x - y = 5. Statement II: x + 2y = 8, and y is non-negative. The question asks for x. Which verdict is correct?

- A. Statement I alone settles x, since it links x and y.
- B. Statement II alone settles x, since it has a positive coefficient.
- C. Neither settles x, even together.
- D. Both together settle x, since the two relations determine one value of x.

**MCQ 32 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Assumes that a relation linking x and y fixes x. 3x - y = 5 has many solutions, such as (2, 1) and (3, 4).
- **B — Incorrect:** Assumes that a positive coefficient fixes the value. Statement II alone allows x = 8 - 2y for every non-negative y.
- **C — Incorrect:** Assumes the two relations cannot be combined. Substituting y = 3x - 5 into the second gives x = 18/7.
- **D — Correct:** Substituting y = 3x - 5 from statement I into statement II gives x + 2(3x - 5) = 8, so 7x = 18. Each statement alone leaves a family of values.

**MCQ 33**

What is the largest value of |x - y| for 0 <= x <= 2 and -1 <= y <= 3?

- A. 3
- B. 1
- C. 0
- D. 2.5

**MCQ 33 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The distance |x - y| is largest at a corner where x and y are farthest apart. The four corners give 1, 3, 3 and 1, so the maximum is 3, at (0, 3) or (2, -1).
- **B — Incorrect:** Reports the distance at the corner (0, -1), which is 1. That corner is close together, not farthest apart, so it is not the maximum.
- **C — Incorrect:** Compares the midpoints of the two intervals, which are both 1, and reports 0. The midpoints give the centre of each range, not the largest separation of a point from another point.
- **D — Incorrect:** Averages the width of x, which is 2, and the largest value of y, which is 3, to get 2.5. An average of two numbers is not a distance between two points, and the largest distance is 3.

**MCQ 34**

A two-digit number has digits that add to 9. Twice its tens digit is 3 more than its units digit. What is the number?

- A. 81 (tens digit 8)
- B. 45 (tens digit 4)
- C. 27 (tens digit 2)
- D. 72 (tens digit 7)

**MCQ 34 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Satisfies the digit sum but fails the second condition. It is the candidate with the largest tens digit, chosen without testing the second condition. Twice the tens digit is 16, and the units digit plus 3 is 4, so the two sides differ.
- **B — Correct:** Let the tens digit be t and the units digit u. Then t + u = 9 and 2t = u + 3. So u = 2t - 3 and 3t = 12, which gives t = 4 and u = 5. Check: 4 + 5 = 9 and 2 x 4 = 5 + 3.
- **C — Incorrect:** Reverses the sign of the 3, so that twice the tens digit is 3 less than the units digit. That gives 27. Under the stem's condition, twice the tens digit is 4 and the units digit plus 3 is 10, so the second condition fails.
- **D — Incorrect:** Keeps the digit sum of 9, but twice the tens digit is 14 and the units digit plus 3 is 5, so the second condition fails.

---

# TIMED-SET PRACTICE AND SCORING RUBRIC

This section turns the lesson methods into a timed routine. The numbers in it are a practice frame. The personal target is a learning goal set by the learner, not an official cut-off, and no cut-off is stated here as a fact.

## Scoring frame

The CSAT framework records the paper's marking as 2.5 marks for each correct answer, a penalty for each wrong answer equal to one-third of the marks for a correct answer (5/6 of a mark), and no penalty for a blank. Confirm the current marking instructions before any real attempt. The expected value of an attempt with success probability p is:

```text
EV(p) = p x 2.5  -  (1 - p) x 5/6
EV = 0 when p = (5/6) / (2.5 + 5/6) = 1/4
```

| Situation after your work | Chance of being right (p) | Expected value per item | Action |
|---|---|---|---|
| No idea, four live options | about 0.25 | 0 | Break-even; skip it unless you accept variance. |
| One option eliminated, three remain | 1/3 | +5/18 | Attempt. |
| Two options eliminated, two remain | 1/2 | +5/6 | Attempt. |
| Confident in the method | 0.8 to 1.0 | +11/6 to +2.5 | Attempt. |

A blind guess has zero mean. Every elimination you can justify makes the guess positive, so eliminate first and guess second.

## Time budgets by item type

| Item type | Budget per item | Notes |
|---|---|---|
| One-step relation or direct substitution (Lessons 1 and 2) | about 60 seconds | Write the relation, solve, check once. |
| Word problem with two relations or a marking scheme (Lessons 1 and 2) | about 90 seconds | Name the unknowns and the domain first. |
| Inequality with a sign or denominator split (Lesson 3) | about 90 to 120 seconds | Split the case before solving. |
| Absolute value, surd or interval item (Lessons 4 to 6) | about 90 to 120 seconds | Keep both branches or all corners. |
| Data-sufficiency item (Lessons 7 to 9) | about 90 seconds | Stop at uniqueness; do not compute the value unless it is needed. |

Each item is budgeted at about ninety seconds, so a five-item set from one lesson should take about seven minutes. These are learning budgets. The per-item ceiling is what matters: if an item passes it, mark it, leave it, and return later.

## Three-pass control routine

- **Pass 1 - harvest.** Attempt every direct relation, one-step comparison and marking-scheme item that you can finish with confidence. Leave anything that needs a case split.
- **Pass 2 - grind.** Return to the inequality, interval and data-sufficiency items. Use the procedure of Lesson 8 and stop at uniqueness.
- **Pass 3 - decide.** Take the items you left. Eliminate what you can, apply the expected-value rule, and either guess among the survivors or leave the item blank.

## Practice-set pace and personal target

The basic retry gate is five of five items right within eight minutes, drawn from one lesson. Redo the five items after a 20-minute gap; continue only at 5/5 within eight minutes, otherwise rebuild the failed relation and take five fresh items of that exact form. The advanced retry gate is seven of any eight items right from Lessons 4 to 8 within twelve minutes, with no false-uniqueness, denominator or endpoint error, retried after a 20-minute gap; those lessons hold sixteen items. A personal target may sit above either gate, but it is a personal number and never an official standard.

## Error codes for post-test analysis

Record every missed item with one code.

| Code | Error type | First repair |
|---|---|---|
| C | Concept gap: the method was not known | Return to the lesson's rule and redo its worked example. |
| A | Application slip: the right idea, a wrong step | Write the relation before solving; name each operation. |
| X | Calculation error | Add a plug-back check to the answer. |
| R | Reading error: stem, option or direction misread | Read the printed options first; underline "alone", "together", "not", "only". |
| T | Time error: over-invested or rushed | Enforce the per-item ceiling and use the three passes. |
| G | Guess error: a negative-expected-value guess | Guess only after justified elimination. |

Track the mix of codes, not only the count. A run of A codes needs slower relation-writing; a run of R codes needs the printed-option routine; a run of T codes needs the pass structure.

## Scoring a practice set

- Count correct answers and wrong answers separately, and record the time used.
- Marks per minute = (2.5 x correct - (5/6) x wrong) / minutes. Use this as a personal rate for comparing sets of the same type.
- Compare each set with the set before it. A rising marks-per-minute rate on the same family is the sign of a method that is taking hold.

# REMEDIATION

The table pairs each lesson with the commonest miss and its repair. Each repair returns to the lesson's rule, not to a longer list of items.

## If you missed a lesson item

| Lesson | Typical miss | Repair |
|---|---|---|
| 1 | A bracket dropped, or "less than" read in the wrong order | Write the phrase as a symbol line, with brackets, before solving; check in the words. |
| 1 | Digits treated as a product, or the reversal ignored | Write 10t + u; apply the reversal identity 9(t - u). |
| 2 | Two relations assumed to fix a unique pair | Apply the ratio test to the x and y coefficients and the constants. |
| 2 | Option tested against one equation only | Substitute every option into every equation. |
| 3 | Inequality flipped on addition, or not flipped on division by a negative | Name the operation; reverse only for multiplication or division by a negative. |
| 3 | Denominator cross-multiplied without a sign check | Split the case by the sign of the denominator. |
| 4 | One branch of an absolute value kept | Write both branches before solving; check both in the original. |
| 4 | A squared statement treated as a single value | Apply the unique-root test and check the sign. |
| 5 | Powers compared by their bases alone | Equalise the exponents first, or the bases. |
| 5 | Percentage points and percent change mixed | Name the base of each measure before comparing. |
| 6 | Real bound used as an integer answer | Test the integer splits near the middle. |
| 6 | Interval minimum taken from the lower bounds | Test all four corners and keep open and closed ends. |
| 7 | Printed fourth option memorised rather than read | Read the printed (d) each time; map the verdict to the wording. |
| 7 | Necessary condition treated as sufficient | Write the arrow; find a counterexample to the sufficiency claim. |
| 8 | Value computed when only uniqueness was needed | Stop as soon as a second value is found or excluded. |
| 8 | Two statements treated as independent when one implies the other | Check whether one statement is a multiple of the other. |
| 9 | A family's typical statement assumed to settle the value | Test each statement with the Lesson 8 procedure. |
| 9 | A count or a total used without its domain | State the domain of each unknown first. |
| 9 | A range answered with one value, or a maximum found without the bound | Intersect ranges with their ends kept; for the linear-limit type, check the bound 2x + y at most 2(x + 3y) for non-negative x and y. |

## Cumulative items

The cumulative items mix two or more lessons. A miss on them is usually one of three things: a domain omitted (Lessons 1 and 6), a sign not checked (Lessons 3 and 5), or a fourth option misread (Lessons 7 and 8). Redo the lesson whose rule the miss breaks, then return to the cumulative item.

## Retry prompts

Work these in your own notes before you check the answers below each prompt. They are short prompts, not a second set of MCQs.

1. A number is 9 less than the sum of 4 and twice itself. Write the relation and solve. *Answer: x = (4 + 2x) - 9, so x = 2x - 5 and x = 5. Check: 4 + 10 = 14 and 14 - 9 = 5.*
2. Solve |3x - 2| = 4. *Answer: x = 2 and x = -2/3.*
3. Is the statement "n is even" sufficient for "n is a multiple of 6"? *Answer: no; n = 2 is even and not a multiple of 6.*
4. Compare 3^12 and 2^18 by a common exponent. *Answer: 3^12 = 9^6 and 2^18 = 8^6, so 3^12 is larger.*
5. For x + y = 10 with positive integers, what is the largest product? *Answer: 25, from 5 and 5.*

---

# MASTER METHOD MAPS

These maps join the lessons into a single routine. Each one starts from a question the learner can ask and ends at a method.

## Map 1: from a sentence to a relation

```text
SENTENCE
   |
NAME the unknown with unit      -> "Let x be the son's age in years."
   |
STATE the domain                -> integer / positive / digit / non-zero
   |
COUNT the relations             -> one unknown: one relation; two: two independent
   |
WRITE each clause in order      -> "more than", "less than", "times" keep their order
   |
SOLVE, respecting the domain
   |
CHECK in the original words
```

## Map 2: which kind of system?

```text
TWO LINEAR RELATIONS
   |
Compare a1/a2, b1/b2, c1/c2
   |
+------------------+----------------------+-------------------------+
|                  |                      |                         |
a1/a2 != b1/b2     a1/a2 = b1/b2 != c1/c2  a1/a2 = b1/b2 = c1/c2
UNIQUE             INCONSISTENT            DEPENDENT
(eliminate)        (no pair)               (one line written twice)
```

## Map 3: the sign of an inequality

```text
ADD or SUBTRACT a constant      -> direction kept
MULTIPLY or DIVIDE by k > 0     -> direction kept
MULTIPLY or DIVIDE by k < 0     -> direction REVERSED
DIVIDE by an unknown expression -> split into cases by its sign; never divide by zero
CROSS-MULTIPLY a/b vs c/d       -> only with b, d > 0 (or bd sign checked)
CHAINS                          -> apply the operation to every part
```

## Map 4: the branches of a distance or a root

```text
|u| = k
   |
k < 0 ----> no solution
k = 0 ----> u = 0
k > 0 ----> u = k  OR  u = -k

|u| < k ---> -k < u < k (a band)
|u| > k ---> u < -k  OR  u > k (two rays)

u^2 = k ----> k > 0: two roots; k = 0: one; k < 0: none
u^3 = k ----> exactly one real root
```

## Map 5: quantitative comparison routes

```text
TWO POWERS             -> equal exponents? compare bases; equal bases > 1? compare exponents
                          bases between 0 and 1: larger exponent gives the SMALLER power
TWO RATIOS             -> cross-multiply with positive denominators
RATIO vs RECIPROCAL    -> a/b vs b/a: for a > b > 0, a/b is larger
TWO PERCENTAGES        -> put both on the same base; separate percentage points from percent change
TWO SURDS              -> square both (if both positive); or write as one radical times a number
LARGE POWERS           -> common exponent (lowest common multiple)
```

## Map 6: optimisation and ranges

```text
FIXED SUM, INTEGER PARTS -> the most balanced integer split
FIXED SUM, REAL PARTS    -> product at most (sum/2)^2 for non-negative parts (AM-GM)
INTERVAL PRODUCT         -> test the FOUR corners
                            an extreme is attained only if its ends are closed
                            a minimum may come from a mixed corner
SUM OF INTERVALS         -> bounds add, with the same open or closed rule
```

## Map 7: the data-sufficiency decision

```text
READ the printed options (note the wording of (d): W1, W2 or W3)
   |
Does the QUESTION alone settle the value?
   | yes -> SELF-SUFFICIENT
   | no
Does I alone settle it?   Does II alone settle it?
   | exactly one -> (a)
   | both         -> (b)
   | neither
Do I and II together settle it? -> (c)
   | no -> NEITHER SUFFICES

LETTER:
  (a) exactly one alone      (b) either alone      (c) both together only
  (d) under W1/W2: neither suffices
  (d) under W3:    self-sufficient question
  self-sufficient with (d) = W1/W2: no option fits; re-read the stem
```

## Map 8: families of data-sufficiency items

```text
FAMILY        TRANSLATE INTO                    CHECK BEFORE CONCLUDING
digits        place value 10t + u, digit bounds  0 to 9; tens digit at least 1
ages          present ages, one time shift       the shift applies to both people
primes        positive integers                  1 is not prime
factor counts exponent pattern (a+1)(b+1)...     a count does not fix the number
parity        parity of the whole sum/product    not the parity of one term
shares        fraction of a total                needs the total
sets          union = sum of groups - overlap    which quantity a statement describes
```

---

# COMPLETE CONSOLIDATED REGISTER NOTES

These notes cover every subtopic of the session in compressed form. They prioritise definitions, rules, failure conditions, examples and the recall facts that the items test. They do not repeat the teaching prose.

## Words to equations (Lesson 1)

- Name the unknown with its unit; state the domain; write one relation per clause; check in words.
- "x is 3 more than y" means x = y + 3. "7 less than x" means x - 7.
- Brackets are required around "four times (x - 2)".
- Age problems: apply any time shift to both people.
- Two-digit numbers: 10t + u; reversal changes the number by 9(t - u).
- Consecutive even or odd integers differ by 2; consecutive integers differ by 1.
- Sum S and difference D give (S + D)/2 and (S - D)/2; integers need S and D of the same parity.
- Two prices and a fixed count: write the count of each kind, then the total as a sum of the two products; a marking scheme uses attempted = correct + wrong.

## Simultaneous equations (Lesson 2)

- Ratio test: a1/a2 vs b1/b2 vs c1/c2 gives unique, inconsistent or dependent.
- Elimination: multiply to match one coefficient, then add or subtract.
- Substitution: isolate the simplest variable first.
- Option testing: every option must satisfy every equation.
- Non-linear systems can give two ordered pairs; the ratio test does not apply to them.
- Sum S and product P: the pair is the roots of t^2 - St + P = 0; a symmetric value such as x^2 + y^2 = S^2 - 2P needs no pair.

## Inequalities (Lesson 3)

- Add or subtract: direction kept. Multiply or divide by a positive: kept. By a negative: reversed.
- Denominator of unknown sign: split the case; never cross-multiply blind.
- Cross-multiplication: when bd > 0, a/b < c/d is ad < bc; when bd < 0, it is ad > bc.
- Chains: apply the same operation to every part; reverse both signs when dividing by a negative.
- Coded inequalities: rewrite the code in ordinary form first.
- Ranges: a positive coefficient keeps the order of endpoints; a negative one reverses it.

## Absolute value, squares and surds (Lesson 4)

- |u| = k: u = k or u = -k for k > 0; one solution for k = 0; none for k < 0.
- |u| < k: band; |u| > k: two rays.
- sqrt(x^2) = |x|; the root symbol gives the non-negative root.
- Squaring preserves order only for non-negative quantities.
- x^2 = k: two roots for k > 0; one for k = 0; none for k < 0. x^3 = k: one real root.
- Odd power settles the sign (x^3 > 0 gives x > 0); even power does not (x^2 > 0 allows x = -4).
- Surds: square both sides when positive; or write both as one radical times a number.

## Quantitative comparison (Lesson 5)

- Equal exponents: compare bases. Equal bases above 1: compare exponents.
- For 0 < x < 1, the higher power is smaller.
- For a > b > 0: a/b > b/a.
- For x > y > 0: 1/x < 1/y. The positivity is essential.
- A is 25 per cent more than B: B is 20 per cent less than A.
- A rate from 10 to 14 per cent: 4 percentage points, which is 40 per cent of the old rate.
- Large powers: common exponent via the lowest common multiple.
- Squaring a comparison is safe only when both sides are non-negative.

## Bounds and optimisation (Lesson 6)

- Integer product with fixed sum: the most balanced integer split (for 15: 7 and 8, product 56).
- Fixed product: the least sum comes from the most balanced split (for 36: 6 and 6, sum 12).
- Real AM-GM: xy <= ((x + y)/2)^2 for non-negative x and y.
- Interval product: test all four corners; open and closed ends decide attainment.
- Minimum may come from a mixed corner, not from the two lower bounds.
- Sums of intervals: bounds add with the same open or closed rule.
- Never divide through an interval that contains zero.

## Data-sufficiency format (Lesson 7)

- Options (a), (b), (c) are stable. Option (d) varies: W1 "cannot, even with both"; W2 "cannot, using any statement alone or together"; W3 "answered with no statement". BOTH TOGETHER ONLY maps to (c).
- The 2024 items print their own options; the 2026 options are printed once above a block of five.
- Verdict first, letter second. Self-sufficient with W1/W2: no option fits; re-read the stem.
- Necessary: every case that satisfies the question satisfies the statement. Sufficient: the statement settles the question.
- Two individually necessary statements can be jointly sufficient.

## Data-sufficiency procedure (Lesson 8)

- Order: question alone; statement I alone; statement II alone; both together; counterexample.
- Stop at uniqueness. A counterexample that satisfies every condition breaks uniqueness.
- False uniqueness: squares, absolute values and even powers often allow two values.
- Hidden dependence: one statement a multiple of the other, or implied by it.
- Self-sufficiency: check the question alone first; a number that is both a square and a cube is a sixth power, and the smallest above 1 is 64.

## Data-sufficiency families (Lesson 9)

- Digits: place value and digit bounds; a digit sum does not fix the number.
- Ages: differences are fixed over time; ratios are not; shift both people.
- Primes: positive integers; 1 is not prime; the square of a prime has three factors.
- Factor counts: the exponent pattern; a count does not fix the number.
- Parity: the parity of the whole expression; an even plus an odd is odd.
- Shares: a fraction needs a total before an amount is determined.
- Sets: union equals the sum of groups minus the overlap.
- Statement sets that fix a total: counts are non-negative whole numbers; test uniqueness.
- Comparisons of real numbers: cube both sides for real numbers; squaring preserves order only for non-negative numbers.
- Bounded variables (single answer): intersect ranges and keep the open and closed ends; a range is a set, not a single value.
- Optimising under linear limits (single answer): bound the objective using non-negativity, then test the corner points.
- Fixed charge plus rate (single answer): subtract the fixed charge before dividing by the rate.

## Learner route in twelve steps

1. Name the unknown in a sentence, with its unit, and state its domain.
2. Translate each clause into one relation, keeping the order of "more than" and "less than".
3. Count the relations: one unknown needs one relation; two unknowns need two independent ones.
4. Solve, keeping every branch of an absolute value and every root of a square.
5. For an inequality, name each operation and track the sign of every multiplier and denominator.
6. Compare two quantities by rewriting both in one common form before any calculation.
7. For an optimum, test the admissible integer points or the interval corners, keeping open and closed ends.
8. For a data-sufficiency item, read the printed options first and note the wording of (d).
9. Test the question alone, then each statement alone, then both together, stopping at uniqueness.
10. Look for a second admissible value; a counterexample that meets every condition breaks uniqueness.
11. Translate the family's vocabulary (digits, ages, primes, factor counts, parity, shares, sets) into a relation.
12. Check the answer in the original words, and log any miss by its error code before the next set.

## Exam shortcut cheat-sheet with failure conditions

| Shortcut | Works when | Fails when |
|---|---|---|
| Ratio test for two linear relations | The relations are linear | A relation is non-linear |
| Option testing | Options are given | Only one equation is tested |
| Case split on a denominator | The denominator's sign is unknown | Fails only when a case boundary, such as the zero of the denominator, is omitted |
| Square to compare | Both sides are non-negative | A side can be negative |
| Common exponent | Bases are small powers of a common base | Exponents have no common multiple that helps |
| Corner test | The region is a rectangle of intervals | The region is not a rectangle |
| Stop at uniqueness | The question is a sufficiency item | The question asks for the value |

## Formula reference

- Two-digit number: 10t + u; reversal difference 9(t - u).
- Sum and difference: (S + D)/2 and (S - D)/2.
- Paper marking (Framework): 2.5c - (5/6)w; the rule is attempted = c + w.
- Absolute value: |u| = k gives u = k or u = -k for k > 0.
- Square root: sqrt(x^2) = |x|.
- AM-GM: xy <= ((x + y)/2)^2 for non-negative x and y.
- Expected value of an attempt: EV(p) = 2.5p - (5/6)(1 - p); break-even p = 1/4.
- Union: |A union B| = |A| + |B| - |A intersection B|.

---

# COVERAGE MATRIX

Each unit below is mapped to the lesson that teaches it. The practice column names an item only where that item tests the unit; otherwise the unit is covered by a worked check inside the lesson.

## Basic units

| Unit | Taught in | Practice |
|---|---|---|
| Visual foundation: solve, compare or decide | Lesson 7, visual "the three kinds of relation problem" | MCQ 19 (method) |
| Data-sufficiency format and the printed fourth-option variants | Lesson 7 Parts A and B | MCQ 19 |
| Necessary and sufficient | Lesson 7 Part D | MCQ 20 |
| Linear solve from a word relation | Lesson 1 worked examples | MCQ 1 |
| Example A (3x + 5 = 20) | Lesson 1 worked example | Worked check (no item) |
| Example C.1 (bracketed word relation) | Lesson 1 worked example | Worked check (no item) |
| Two independent linear relations, ratio test, option testing | Lesson 2 | MCQs 4, 5, 6 |
| Ordered pairs from a fixed sum and a product condition | Lesson 2 worked example | MCQ 7 |
| Inequality sign flip (multiply or divide by a negative) | Lesson 3 Part A | MCQ 9 |
| Division by an unknown-sign denominator, cross-multiplication | Lesson 3 Part B | MCQ 8 |
| Chains and coded inequalities | Lesson 3 Parts C and D | Worked check (no item) |
| Absolute value and its two branches | Lesson 4 Part A | MCQs 10, 11 |
| Squaring to compare non-negative quantities | Lesson 4 Part B | MCQ 12 |
| Equal exponents; bases between 0 and 1; bases above 1 | Lesson 5 Part A | MCQ 13 |
| Squares of negative numbers and the order of the squares | Lesson 4 Part B | MCQ 14 |
| Fraction comparison by cross-multiplication | Lesson 5 Part B | MCQ 15 |
| Ratio, reciprocal and the positivity check | Lesson 5 Part B | Worked check (no item) |
| Percentage versus percentage points | Lesson 5 Part B | MCQ 16 |
| Sum and difference with parity | Lesson 1 Shortcut 6 | Worked check (no item) |
| Example B (sum 30, difference 8) | Lesson 1 Shortcut 6 | Worked check (no item) |
| Example C (2^30 against 3^20) | Lesson 5 Part A | Worked check (no item) |
| Example D (two-digit number, divisible by 11, tens digit 4) | Lesson 8 Part B | Worked check (no item) |
| Example E (parity of n through n^2 and n + 1) | Lesson 8 Part B | Worked check (no item) |
| Example F (exponent pattern; the self-sufficient verdict) | Lesson 8 Part E | Worked check (no item) |
| Must-know: independent relations, sign rule, squaring, sufficiency about the answer | Lessons 2, 3, 4, 5, 8 | MCQs 4, 8, 14, 22 |
| Must-know: square and cube are a sixth power | Lesson 8 Part E | Worked check (no item) |
| Digits and place value: a digit sum with a bound | Lesson 9 Part A | MCQ 26 |
| Digits: tens digit against units digit, with a multiple | Lesson 1 Shortcut 4; Lesson 8 Part A | MCQ 24 |
| Shares and fractions with a total | Lesson 9 Part F | MCQ 27 |
| Set membership: union and overlap | Lesson 9 Part G | MCQ 28 |
| Ages, primes and parity | Lesson 9 Parts B, C and E | Worked check (no item) |
| Divisibility in a statement set (even multiples of 9) | Lesson 8 Parts A and B | MCQ 25 |
| Five further families: statement sets that fix a total, real comparison, bounded variables, linear limits, fixed charge plus rate | Lesson 9 Part H | Worked check (no item) |
| Common traps | Failure conditions and wrong-method sections of each lesson | Remediation table |
| Quick checks | Lesson 7 Part A and revision points | Timed-set routine |
| Mini-drill 1 (2x - 3 > 7) | Lesson 3 Part A | Worked check (no item) |
| Mini-drill 2 ((0.5)^3 against (0.5)^2) | Lesson 5 Part A | Worked check (no item) |
| Mini-drill 3 (digits 9 apart with sum 9) | Lesson 9 Part A | Worked check (no item) |
| Mini-drill 4 (3x = 12 and x + 7 = 11) | Lesson 8 Part B | Worked check (no item) |
| Mini-drill 5 (sum 30, difference 8) | Lesson 1 Shortcut 6 | Worked check (no item) |
| Mini-drill 6 (multiple of 12 and evenness) | Lesson 7 Part D | Worked check (no item) |
| Mini-drill 7 (smallest square and cube above 1) | Lesson 8 Part E | Worked check (no item) |
| Timed transfer, diagnosis and retry gates | Timed-set section | Retry prompts |
| Study links (reading comprehension; number systems) | Lesson 7 plain intuition; Lesson 9 application | Worked check (no item) |
| Learner route in twelve steps | Register notes | Worked check (no item) |

## Advanced units

| Unit | Taught in | Practice |
|---|---|---|
| Architecture: the sufficiency verdict | Lesson 8 visual; Lesson 7 | MCQs 19, 21 |
| Unique-root test (odd and even powers) | Lesson 4 Part C | MCQ 21 |
| Dependent statements | Lesson 8 Part D | MCQ 22 |
| Two individually necessary statements that are jointly sufficient | Lesson 7 Part D, Advanced point | Worked check (no item) |
| Surd comparison by squaring | Lesson 4 Parts B and D | MCQ 12 |
| Surd comparison by a common factor | Lesson 4 Part D | Worked check (no item) |
| AM-GM for non-negative parts (least sum for a fixed product) | Lesson 6 Part B | MCQ 17 |
| Integer optimum with a fixed sum | Lesson 6 Part A | Worked check (no item) |
| Interval corners | Lesson 6 Part C | MCQs 18, 33 |
| Method 1: false uniqueness | Lesson 4 Part C; Lesson 8 Part C | MCQ 23 |
| Method 2: dependent statements | Lesson 8 Part D | MCQ 22 |
| Method 3: surd comparison | Lesson 4 Parts B and D | MCQ 12 |
| Method 4: verdict first, letter second | Lesson 7 Part C | MCQ 19 |
| Method 5: optimum and endpoints | Lesson 6 Parts B and C | MCQs 17, 18 |
| Boundary cases: a square with a sign statement; an inconsistent pair | Lessons 2, 4 and 8 | MCQs 4, 23 |
| Advanced traps | Lessons 4, 6 and 8 | Remediation table |
| Error-analysis codes | Timed-set section | Retry routine |
| Advanced check 1 (sign of a cube against a square) | Lesson 4 Part C | Worked check (no item) |
| Advanced check 2 (multiple of 9 and digit sum 9) | Lesson 8 Part D | Worked check (no item) |
| Advanced check 3 (absolute value with a sign statement) | Lesson 8 Part C | Worked check (no item) |
| Advanced check 4 (divisibility by 6) | Lesson 7 Part D | Worked check (no item) |
| Advanced check 5 (product on intervals with open ends) | Lesson 6 Part C | Worked check (no item) |
| Advanced check 6 (5^100 against 3^150) | Lesson 5 Part C | Worked check (no item) |
| Advanced check 7 (maximum product with sum 17) | Lesson 6 Part B | Worked check (no item) |
| Advanced check 8 (range with closed and open ends) | Lesson 6 Part C | MCQ 18 |
| Advanced timed transfer and retry gate | Timed-set section | Retry routine |
| PYQ-pattern notes: format changes and false uniqueness | Lesson 7 Part B; Lesson 8 | MCQs 19, 21 |

## PYQ accounting

| Year | Items | Covered in (number of items in brackets where more than one) |
|---|---:|---|
| 2013 | 0 | No item listed for this topic. |
| 2014 | 1 | Lesson 2 |
| 2015 | 1 | Lesson 9 |
| 2016 | 3 | Lesson 1, Lesson 2, Lesson 6 |
| 2017 | 4 | Lesson 1, Lesson 2, Lesson 5, Lesson 8 |
| 2018 | 7 | Lesson 1 (3), Lesson 2, Lesson 3 (2), Lesson 5 |
| 2019 | 6 | Lesson 1 (3), Lesson 3, Lesson 5, Lesson 8 |
| 2020 | 7 | Lesson 2 (2), Lesson 8 (4), Lesson 9 |
| 2021 | 6 | Lesson 1 (2), Lesson 5, Lesson 8 (3) |
| 2022 | 9 | Lesson 1, Lesson 2, Lesson 5, Lesson 8 (6) |
| 2023 | 6 | Lesson 6, Lesson 8 (2), Lesson 9 (3) |
| 2024 | 13 | Lesson 1, Lesson 2, Lesson 3, Lesson 8 (3), Lesson 9 (7) |
| 2025 | 11 | Lesson 3, Lesson 5 (2), Lesson 6 (3), Lesson 8 (3), Lesson 9 (2) |
| 2026 | 9 | Lesson 1, Lesson 2, Lesson 3, Lesson 5, Lesson 6, Lesson 9 (4) |

The totals are 9 for 2013 to 2017 and 74 for 2018 to 2026. The counts by lesson appear in the PYQ linkage section above and match the year entries.

## Practice counts by lesson

| Lesson | MCQs | Numbers |
|---:|---:|---|
| 1 | 3 | 1 to 3 |
| 2 | 4 | 4 to 7 |
| 3 | 2 | 8 to 9 |
| 4 | 3 | 10 to 12 |
| 5 | 4 | 13 to 16 |
| 6 | 2 | 17 to 18 |
| 7 | 3 | 19 to 21 |
| 8 | 4 | 22 to 25 |
| 9 | 3 | 26 to 28 |
| Cumulative | 6 | 29 to 34 |

Thirty-four MCQs in all. Each has four options, four option explanations and an answer key, and the keys rotate A to B to C to D across the whole file.

---

# SOURCE LEDGER

## Sources used

- `upsc-ai-kit/knowledge/CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`: read in full, including the 2026, 2024 to 2025 and 2018 to 2023 PYQ integration blocks and the semantic-completeness closure.
- `upsc-ai-kit/knowledge/CSAT/advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md`: read in full, including the advanced drill and its solutions, and the PYQ integration blocks.
- `upsc-ai-kit/knowledge/CSAT/00_Master-Framework.md`: read for the paper's marking scheme, the expected-value rule and the error codes.
- `upsc-ai-kit/knowledge/CSAT/00_Question-Audit-Ledger.md`: used only for its family and neutral-type labels (the 2024, 2025 and 2026 rows) and its family definitions, to classify the demand labels of the PYQ entries; its answer-key columns and solution text were not read.
- `upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2018-2023.md`, `_PYQ-ROUTING-CSAT-2024-2025.md` and `_PYQ-ROUTING-CSAT-2026.md`: used to count and route the items, with neutral type labels only.
- `solved_pyqs/papers/2013` to `2026/prelims-csat.md`: the question stem and statement lines of each linked entry were read to classify demand and to correct approach lines. Solution, key and answer lines were not read or used, and stem wording is not reproduced. Link anchors were checked for all 83 entries.
- `live_sessions/CSAT/04-Rates-Motion-Time-and-Geometry/Learning-Session-Live-Edition.md` and `live_sessions/CSAT/01-Reading-Comprehension/Learning-Session-Live-Edition.md`: read for the CSAT structural pattern only; no content copied.
- `live_sessions/Philosophy-Optional/01-Nyaya-Vaisesika`, `06-Yoga` and `07-Mimamsa` Learning-Session-Live-Edition files: opening and a complete teaching segment read for the learner-first style only; no doctrine copied.
- `live_sessions/LIVE-SESSION-GENERATION-RULES.md`, `instructions/README.md`, `instructions/GENERATION-OPTIMIZATION-AND-INTEGRITY.md` and `instructions/LIVE-SESSION-VALIDATION-AND-RELEASE.md`: read in full in this pass, before the final matrix and wording edits; the rules text was not changed by those edits.
- `tools/validate_live_session.py`: read for the CSAT profile and the source-manifest rules.

Books: not consulted. Teaching content, worked examples, MCQs, retry prompts, the timed routine and the method maps were written for this session. The linked PYQ question stems were read (stem and statement lines only), and approach lines paraphrase their demand; no solution, key, answer line or printed option wording is reproduced. Official live sources: not consulted, because the paper is an aptitude paper whose keys are either supplied or provisional.

## Coverage counts

- 83 routed items accounted for: 9 from 2013 to 2017 and 74 from 2018 to 2026 (41 from 2018 to 2023, 24 from 2024 to 2025 and 9 from 2026).
- 34 original MCQs: 28 in lessons and 6 cumulative.

## Permanent exclusions

No artifact in the excluded final learning-package folder was read, searched, cited or compared against. No learner-v2 artifact was used.

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical Markdown | checked | `upsc-ai-kit/knowledge/CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md` and `upsc-ai-kit/knowledge/CSAT/advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md`, both read in full, with the CSAT master framework and the question audit ledger. |
| Final learner package | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule. |
| Layered/complete session | checked | CSAT 04 and CSAT 01 live editions and the Philosophy Optional opening and teaching segments were read for structure and style only; no content was copied. |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule. |
| Advanced dossier | checked | `upsc-ai-kit/knowledge/CSAT/advanced/05_Algebra-Inequalities-and-Data-Sufficiency.md`, all sections, including the advanced drill and its solutions. |
| OCR books | not relevant | No OCR book was consulted; the aptitude items are verified arithmetically and the owner files carry the full evidence. |
| PYQs through 2026 | checked | Routing ledgers `_PYQ-ROUTING-CSAT-2018-2023.md`, `_PYQ-ROUTING-CSAT-2024-2025.md` and `_PYQ-ROUTING-CSAT-2026.md`, plus the solved PYQ library used only for counting, routing and anchor verification; the 2026 paper is provisional and no 2026 key is inferred. |
| Official live sources | not relevant | Aptitude paper; no current-affairs or live linkage applies, and no live source was used. |

## Uncertainties

- The 2013 to 2017 entries use the family labels in the solved library; their format is recorded as single-answer except for the one item whose title names a data-sufficiency statement set.
- The 2018 to 2023 entries carry generic family labels in the routing ledger; their approach lines state the test to run, not a worked route for each question.
- The 2026 paper is provisional; its entries record the method only.
- 2023 Q26 is listed for this topic by the 2018 to 2023 routing ledger, but the solved library's own primary route for that item points to Number Systems (topic 02). It is counted here per the routing ledger, and the controller should reconcile the two.
- The routing ledger's 2018 to 2023 labels are generic family names, so their approach lines state the test to run, not a solved route.
