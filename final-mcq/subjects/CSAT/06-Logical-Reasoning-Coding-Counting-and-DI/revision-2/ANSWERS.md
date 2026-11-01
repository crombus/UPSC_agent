# CSAT 06 — Revision 2: worked answers

Every key was checked by the method recorded in `AUDIT.md`. Each entry gives the reason for the key, the error behind each distractor, the examiner trap, and a shortcut with a time target.

**R2-Q01 — C.** II follows: a panel member is a graduate (statement 1), and no graduate is a retired officer (statement 3). I fails: statement 2 places some interns among panel members, and nothing forces those interns to be retired officers. III fails: a case in which the intern who is a panel member is also a graduate satisfies all three statements.

- A: Accepts I. Nothing forces an intern to be a retired officer; statement 3 only forbids graduates from being retired officers.
- B: Accepts I and III. III needs an intern who is not a graduate, which the statements do not force; I is the same unsupported claim as before.
- D: Accepts I and III, and so also accepts an unsupported intern-graduate claim.
- C (key): correct, for the reason given above.

Trap: Chaining panel member -> graduate, then assuming the intern-panel overlap is a retired-officer overlap.

Shortcut: Chain panel -> graduate -> not retired; test each existential conclusion with one intern who is a panel member and a graduate. Time target: 100 seconds.

**R2-Q02 — C.** I follows: the managers who are auditors cannot be trainees (statement 2), and at least one manager is an auditor (statement 1). II fails: a manager who is not an auditor may be a trainee. III fails: a case with managers who are auditors and trainees who are not managers satisfies both statements.

- A: Accepts II. Statement 2 is about auditors only; it says nothing about managers who are not auditors.
- B: Accepts II alongside I. The universal claim about all managers is not supported.
- D: Accepts II and III. III converts a claim about auditors into a claim about trainees who are managers, which the statements do not give.
- C (key): correct, for the reason given above.

Trap: Widening a claim about the auditor managers to all managers; this is the most common CSAT error with 'some'.

Shortcut: Restrict to the managers who are auditors, test 'no manager' with an outside manager, and test III with a trainee who is not a manager. Time target: 85 seconds.

**R2-Q03 — D.** From (d) and (a), the sponsor was not found. From (c), the hall is booked. Statement (b) then allows the talk but does not require it, so the talk is not forced. The only must-true option is that the sponsor was not found.

- A: Contradicts the result of (a) and (d) together.
- B: Not forced: (b) allows a scheduled talk when the hall is booked, but nothing requires it.
- C: Contradicts (c), because exactly one of the hall and the sponsor holds and the sponsor was not found.
- D (key): correct, for the reason given above.

Trap: Reading 'exactly one' as 'at least one', which would drop the link that forces the hall to be booked.

Shortcut: Start from the fact given directly (funds not released), contrapose (a), then use the exactly-one condition in (c). Time target: 110 seconds.

**R2-Q04 — B.** 'Approved only if quorum and signature' means approval implies both a quorum and a signature. Since the proposal was approved, a quorum was present.

- A: Contradicts the condition: approval requires the chair to sign.
- C: Not forced: a committee may approve a proposal in a meeting; the statements do not say the committee did not meet.
- D: Contradicts the condition: approval requires a quorum.
- B (key): correct, for the reason given above.

Trap: Reading 'only if' as 'if', which would make the conditions sufficient rather than necessary.

Shortcut: 'Approved only if X' means approved -> X; the stated fact is approval, so X holds. Time target: 60 seconds.

**R2-Q05 — B.** From (d) and (c), B is not the case. From (a), A is not the case. So A is false. (Statement (b) then forces C to be true, which is not among the options.)

- A: Not possible: statement (b) forces C to be true, so C is false cannot hold in every valid case.
- C: Contradicts (c) and (d): B is not the case.
- D: Contradicts (d) directly.
- B (key): correct, for the reason given above.

Trap: Stopping after the first forced fact (B false) and not following the contrapositive of (a) to A.

Shortcut: Work backwards: D false -> B false (from c) -> A false (from a). Time target: 90 seconds.

**R2-Q06 — C.** B moves by 1 to C; O moves by 2 to Q; A moves by 3 to D; T moves by 4 to X. The code is CQDX.

- A: Moves every letter by 1, ignoring the position numbers: B to C, O to P, A to B, T to U.
- B: Moves the last letter by 3 instead of 4: T to W.
- D: Moves each letter by its position minus one: B stays B, O moves 1 to P, A moves 2 to C, T moves 3 to W.
- C (key): correct, for the reason given above.

Trap: Using the example only as a shift check and then applying a uniform shift.

Shortcut: Write the move for each position (1, 2, 3, 4) and apply it to the matching letter. Time target: 90 seconds.

**R2-Q07 — D.** CHAIR: C 3, H 8, A 1, I 9, R 18. Odd places: C, A, R = 3 + 1 + 18 = 22. Even places: H, I = 8 + 9 = 17. Code = 22 - 17 = 5.

- A: Adds all five positions and ignores the subtraction: 3 + 8 + 1 + 9 + 18 = 39.
- B: Keeps only the even-place sum, 17, and omits the odd-place part.
- C: Reverses the subtraction, giving 17 - 22 = -5.
- D (key): correct, for the reason given above.

Trap: Reversing the subtraction, or counting places from zero.

Shortcut: Fill two columns: odd places and even places; subtract the even sum from the odd sum. Time target: 80 seconds.

**R2-Q08 — C.** 4 @ 3 = 12 - 7 = 5. 2 @ 1 = 2 - 3 = -1. Then 5 # (-1) = 5 + 2 x (-1) = 3.

- A: Uses a # b = 2a + b, reversing the roles of a and b: 2 x 5 + (-1) = 9.
- B: Stops after the first operation: 4 @ 3 = 5, with the outer operation omitted.
- D: Takes only the second inner result as the answer: 2 @ 1 = -1.
- C (key): correct, for the reason given above.

Trap: Applying # to the raw numbers instead of to the results of the inner @ operations.

Shortcut: Evaluate both inner @ results first, then apply # with the first result in the first place. Time target: 90 seconds.

**R2-Q09 — B.** Reverse values: M = 14, O = 12, T = 7, R = 9. Odd places: M, T, R = 14 + 7 + 9 = 30. Even places: O, O = 12 + 12 = 24. Code = 30 - 24 = 6.

- A: Keeps only the odd-place sum, 30, and omits the subtraction.
- C: Keeps only the even-place sum, 24.
- D: Adds all five reverse values: 14 + 12 + 7 + 12 + 9 = 54.
- B (key): correct, for the reason given above.

Trap: Converting letters to ordinary positions instead of reverse positions (M is 13 in ordinary order, 14 in reverse).

Shortcut: Convert each letter to its reverse value first, then compute odd minus even. Time target: 90 seconds.

**R2-Q10 — C.** TOP reversed is POT. Moving each letter back three places: P to M, O to L, T to Q. The code is MLQ. Check on MAP: reversed PAM; P to M, A to X, M to J gives MXJ.

- A: Moves the letters back by three without reversing the word: TOP becomes QLM.
- B: Reverses the word without moving the letters: POT.
- D: Moves the letters forward by three without reversing them: TOP becomes WRS.
- C (key): correct, for the reason given above.

Trap: Applying the two steps in the wrong order, or testing the rule on one letter only.

Shortcut: Reverse first, then shift back by three; check the example MAP -> MXJ before using the rule. Time target: 100 seconds.

**R2-Q11 — B.** The terms are n(n + 1) for n = 1 to 5: 1 x 2, 2 x 3, 3 x 4, 4 x 5, 5 x 6. The next term is 6 x 7 = 42. Equivalently, the differences are 4, 6, 8, 10, 12.

- A: Repeats the last difference (10): 30 + 10 = 40.
- C: Takes 6 squared, 36, which breaks the pattern of consecutive products.
- D: Adds 14 instead of 12 to the last term: 30 + 14 = 44.
- B (key): correct, for the reason given above.

Trap: Recognising consecutive products but mis-stepping the difference.

Shortcut: Write the differences: 4, 6, 8, 10; the next is 12. Time target: 60 seconds.

**R2-Q12 — A.** The first letter moves forward one place each step (A, B, C, D, E). The second letter moves back one place each step (Z, Y, X, W, V). The next pair is EV.

- B: Moves the second letter back two places (W to U): EU.
- C: Moves the first letter forward two places (D to F): FV.
- D: Moves both letters by two places: FU.
- A (key): correct, for the reason given above.

Trap: Reading the second letter as moving forward (it moves back), or using a step of two.

Shortcut: Track each letter in its own column: first letter +1, second letter -1. Time target: 60 seconds.

**R2-Q13 — D.** The steps alternate: +1, x3, +1, x3, +1, x3. So 39 to 40 is +1, and the next step is x3: 40 x 3 = 120.

- A: Adds 1 to the last term: 41. This treats the series as all +1 steps.
- B: Adds 1 to 120 to give 121: the pattern needs x3 at this position, not +1.
- C: Multiplies the term two places back (39) by 3: 117, which skips the +1 step.
- D (key): correct, for the reason given above.

Trap: Assuming one operation for the whole series, instead of two alternating operations.

Shortcut: Pair the terms as (3,4), (12,13), (39,40); each pair is one x3 and one +1. Time target: 80 seconds.

**R2-Q14 — B.** Each term is a cube plus one: 1 cubed + 1 = 2, 2 cubed + 1 = 9, 3 cubed + 1 = 28, 4 cubed + 1 = 65. The next term is 5 cubed + 1 = 126.

- A: Gives the cube without the +1 offset: 125.
- C: Adds 2 to the cube instead of 1: 127.
- D: 130 is not reached by any consistent rule; the cube-plus-one pattern gives 126.
- B (key): correct, for the reason given above.

Trap: Recognising a power but forgetting the constant offset.

Shortcut: Subtract 1 from each term and look for cubes: 1, 8, 27, 64. Time target: 60 seconds.

**R2-Q15 — A.** The differences are 2, 4, 6, 8, 10, rising by 2 each time. The next difference is 12, so 35 + 12 = 47.

- B: Repeats the last difference (10): 35 + 10 = 45.
- C: Uses an odd difference (11): 35 + 11 = 46.
- D: Uses a difference of 14: 35 + 14 = 49, which skips the next step.
- A (key): correct, for the reason given above.

Trap: Using the last difference (10) as the next step instead of the next even number.

Shortcut: Write the differences; they are consecutive even numbers. Time target: 75 seconds.

**R2-Q16 — D.** Q is R's parent, and T is Q's brother, so T is R's uncle. S is T's son, so S and R are children of two siblings: first cousins.

- A: A nephew is a sibling's son; S is the son of R's uncle, not of R's sibling.
- B: Brother requires a shared parent; S and R share no parent in the statements.
- C: An uncle is a parent's brother: T is R's uncle, but S is not.
- D (key): correct, for the reason given above.

Trap: Reading T as R's parent or sibling because T is linked to Q.

Shortcut: Find R's parents, then the parents' siblings, then their children. Time target: 75 seconds.

**R2-Q17 — A.** Y's father's brother is Y's uncle. His spouse is Y's aunt by marriage.

- B: A grandmother is a parent's parent; X is in the generation of Y's parent, not above it.
- C: The mother is Y's parent; X is Y's uncle's spouse, not Y's parent.
- D: A cousin is a child of a parent's sibling; X is the spouse of that sibling, one generation above Y.
- A (key): correct, for the reason given above.

Trap: Treating 'spouse of a relative' as a blood relation of the same kind.

Shortcut: Start from Y's father, move to his brother, then to that brother's spouse. Time target: 70 seconds.

**R2-Q18 — D.** Leela is Mohan's paternal grandmother, so Gita, her daughter, is Mohan's paternal aunt. Hari, Gita's husband, is therefore Mohan's uncle by marriage.

- A: Nitin, not Hari, is Mohan's cousin; Hari is one generation above Nitin.
- B: A father-in-law is a spouse's father; Hari is not related to Mohan through a spouse.
- C: A grandfather is two generations above Mohan; Hari is Mohan's uncle, one generation above Mohan.
- D (key): correct, for the reason given above.

Trap: Naming Nitin as the relation asked, or treating a son-in-law link as a father-in-law link.

Shortcut: Locate Gita as the paternal aunt first; her husband is the uncle by marriage. Time target: 90 seconds.

**R2-Q19 — D.** B and C are brothers, the sons of A. D is C's wife, so D is B's sister-in-law. E is B's son, so E is D's nephew by marriage.

- A: Son would make E the child of D; E is the child of B, D's brother-in-law.
- B: Grandson is a relation to A; E is A's grandson, but the question asks about D.
- C: Brother-in-law is a spouse's brother or a sister's husband; E is in the next generation below D.
- D (key): correct, for the reason given above.

Trap: Answering with the relation to A (the grandfather) rather than to the person named.

Shortcut: Place D by marriage into the sibling line, then count E one generation below. Time target: 90 seconds.

**R2-Q20 — B.** Facing south-east, a 45 degree clockwise turn gives south. He walks 12 m south: (0, -12). A 90 degree anticlockwise turn from south faces east; he walks 5 m east: (5, -12). Distance = square root of (5 squared + 12 squared) = 13 m.

- A: Adds the two legs (12 + 5); the legs are at right angles, so they do not add.
- C: Subtracts the legs (12 - 5); the eastward leg is at right angles to the southward leg.
- D: Counts only the 12 m leg, ignoring the eastward walk.
- B (key): correct, for the reason given above.

Trap: Forgetting that the second leg is at right angles to the first.

Shortcut: Track the heading: south-east + 45 clockwise = south, then east; use the 5-12-13 triple. Time target: 100 seconds.

**R2-Q21 — C.** Headings: north-west, then right to north-east, then right to south-east, then left to north-east. Adding the east and north components of each leg gives a final position about 7.8 km east and 7.8 km north of the start, a distance of 11 km to the north-east.

- A: Reverses the sign of the westward component: the final point lies north-west of the start.
- B: Adds all four legs (4 + 3 + 4 + 8 = 19) as if the path were a straight line.
- D: Keeps only the last two legs in the same direction, giving 7 km north-east.
- C (key): correct, for the reason given above.

Trap: Treating path length as displacement, or tracking the heading without the sign of each component.

Shortcut: Convert each leg to east and north components using the heading; add components before taking the distance. Time target: 150 seconds.

**R2-Q22 — B.** West 5 km: (-5, 0). Right turn faces north; 5 km: (-5, 5). Right turn faces east; 5 km: (0, 5). Left turn faces north; 10 km: (0, 15). She is 15 km north of the start.

- A: Mis-tracks the initial heading, placing the final result on the west side of the start.
- C: Drops the first northward leg (5 km), keeping only the final 10 km north.
- D: Keeps only the middle leg (5 km north).
- B (key): correct, for the reason given above.

Trap: Forgetting that the final left turn points her back north from an eastward heading.

Shortcut: Track the heading after each turn; the three 5 km legs net to east 0 and north 5. Time target: 100 seconds.

**R2-Q23 — D.** Start at 135 degrees (south-east). 135 degrees anticlockwise gives 0 degrees (north). 225 degrees clockwise gives 225 degrees (south-west). 90 degrees anticlockwise gives 135 degrees (south-east).

- A: Applies the 135 degree turn clockwise instead of anticlockwise, which gives a different heading: north-east after all three turns.
- B: Stops after the second turn (225 degrees, south-west), ignoring the final anticlockwise 90 degrees.
- C: Stops after the first turn (0 degrees, north).
- D (key): correct, for the reason given above.

Trap: Reversing the direction of the first turn, or stopping before the last turn.

Shortcut: Keep a running heading in degrees; anticlockwise subtracts, clockwise adds. Time target: 80 seconds.

**R2-Q24 — B.** Exactly two seatings satisfy every condition: A, F, B, D, E, C and D, E, B, F, A, C. In both, C sits in seat 6.

- A: F sits in seat 2 or seat 4 in the valid seatings, never seat 6.
- C: E sits in seat 2 or seat 5 in the valid seatings, never seat 6.
- D: A sits in seat 1 or seat 5 in the valid seatings, never seat 6.
- B (key): correct, for the reason given above.

Trap: Fixing a clue-free person in an end seat before testing the end-seat constraint on C.

Shortcut: Fix B in seat 3, then place the D-E pair and test C at each end; the end-seat rule decides seat 6. Time target: 120 seconds.

**R2-Q25 — D.** Round arrangements with rotations identical: 6! = 720. Those with A next to B number 240, and those with C next to D also number 240. Those with both adjacent pairs number 96, so the arrangements with neither are 720 - 240 - 240 + 96 = 336.

- A: Counts the forbidden seatings (A next to B) rather than the permitted ones: 240.
- B: Drops the rule about C and D: 720 - 240 = 480.
- C: Ignores both rules and counts all 720 seatings.
- D (key): correct, for the reason given above.

Trap: Counting the forbidden seatings instead of subtracting them, or dropping one of the two rules.

Shortcut: Use inclusion-exclusion: 720 - 240 - 240 + 96 = 336. Time target: 150 seconds.

**R2-Q26 — C.** The only assignment is Dev on floor 1, Ajay on floor 2, Chetan on floor 3 and Bina on floor 4.

- A: Chetan lives on floor 3; floor 2 is excluded for Chetan by the condition.
- B: Dev lives on floor 1, the ground floor, in the only valid assignment.
- D: Bina lives on floor 4, which is more than one floor above Ajay.
- C (key): correct, for the reason given above.

Trap: Stopping at an assignment that satisfies most conditions; test every condition on the final assignment.

Shortcut: Use the ground-floor and top-floor exclusions to place Dev and Bina first; then Ajay and Chetan are fixed. Time target: 120 seconds.

**R2-Q27 — C.** The only ranking is K, M, N, O, L. Here N is third, with K first and M second.

- A: K is first in the only valid ranking, not third.
- B: O is fourth in the only valid ranking, not third.
- D: L is last (fifth) by condition, not third.
- C (key): correct, for the reason given above.

Trap: Placing the adjacent pairs incorrectly; the pair N-O and the pair K-M are both forced.

Shortcut: Fix L last; then place the two adjacent pairs (N, O) and (K, M) in the remaining places. Time target: 120 seconds.

**R2-Q28 — A.** P is in slot 1 (it must come before R in slot 4). Q is in slot 2 and S in slot 3; slot 5 is empty.

- B: S follows Q immediately, so S is in slot 3, not slot 2.
- C: R is in slot 4 by condition.
- D: P is in slot 1 in the only schedule, so P is not in slot 2.
- A (key): correct, for the reason given above.

Trap: Forgetting that one slot is empty, so the talks do not fill slots 1 to 4 by default.

Shortcut: Fix R in slot 4 and the Q-S pair next to each other; P must come before R and in slot 1. Time target: 120 seconds.

**R2-Q29 — C.** Green is below yellow, so green can never be on top, because yellow would have to be above it. Red, blue and yellow each appear on top in at least one valid stacking.

- A: Red is on top in some valid stacking, so red can be on top.
- B: Blue is on top in some valid stacking, so blue can be on top.
- D: Yellow is on top in some valid stacking, so yellow can be on top.
- C (key): correct, for the reason given above.

Trap: Checking only one valid stacking before deciding which box can be on top.

Shortcut: Any box that must sit below another cannot be on top; then confirm the other boxes can. Time target: 100 seconds.

**R2-Q30 — D.** Squares of side 1: 16; side 2: 9; side 3: 4; side 4: 1. Total 16 + 9 + 4 + 1 = 30.

- A: Counts only the unit squares: 16.
- B: Counts sizes 1 and 2 only, as 16 + 4 = 20.
- C: Counts the number of grid lines squared: 5 x 5 = 25.
- D (key): correct, for the reason given above.

Trap: Counting only the smallest squares, or squaring the number of lines.

Shortcut: Count by size: k x k squares number (5 - k) squared. Time target: 75 seconds.

**R2-Q31 — A.** A unit cube has no painted face when none of its coordinates is on the outer layer. The inner block is 4 x 4 x 4 = 64.

- B: Counts the cubes with exactly two painted faces: 12 edges x (6 - 2) = 48.
- C: Counts the cubes with exactly one painted face: 6 x 4 x 4 = 96.
- D: Counts all unit cubes, ignoring the painting.
- A (key): correct, for the reason given above.

Trap: Using side 6 minus 1, or confusing the inner block with the edge cubes.

Shortcut: Inner unit cubes form a cube of side n - 2 = 4. Time target: 75 seconds.

**R2-Q32 — A.** Faces that meet face 2 at a corner in either view are adjacent to it: faces 3, 4, 5 and 6. The only face left, face 1, is opposite face 2.

- B: Face 3 meets face 2 at a corner in the second view, so it is adjacent to face 2.
- C: Face 4 meets face 2 at a corner in the second view, so it is adjacent to face 2.
- D: Face 5 meets face 2 at a corner in the first view, so it is adjacent to face 2.
- A (key): correct, for the reason given above.

Trap: Reading one view as showing an opposite pair; faces that share a corner are adjacent, never opposite.

Shortcut: List the faces that touch face 2; the remaining face is opposite. Time target: 75 seconds.

**R2-Q33 — D.** Pairs of points: C(8, 2) = 28. The four collinear points give C(4, 2) = 6 pairs that define only one line, so subtract 6 and add 1 for that line: 28 - 6 + 1 = 23.

- A: Subtracts 6 without adding back the single shared line: 28 - 6 = 22.
- B: Subtracts 4 rather than the 6 pairs on the common line: 28 - 4 = 24.
- C: Ignores collinearity and counts every pair as a separate line: 28.
- D (key): correct, for the reason given above.

Trap: Counting pairs as lines when some pairs lie on the same line.

Shortcut: Count pairs, then merge the pairs on the shared line into one line. Time target: 90 seconds.

**R2-Q34 — A.** A rectangle is chosen by two of the three horizontal lines and two of the six vertical lines: C(3, 2) x C(6, 2) = 3 x 15 = 45.

- B: Counts only the pairs of vertical lines: C(6, 2) = 15.
- C: Multiplies rows by columns to get 10, then multiplies by 3: 30.
- D: Multiplies the line counts incorrectly as 3 x 4 x 5 = 60.
- A (key): correct, for the reason given above.

Trap: Counting rows and columns as lines, or using the number of lines in one direction only.

Shortcut: Choose two horizontal lines (3 pairs) and two vertical lines (15 pairs): 3 x 15. Time target: 90 seconds.

**R2-Q35 — D.** Exactly two: (A and B only) 30 - 10 = 20, (B and C only) 25 - 10 = 15, (A and C only) 20 - 10 = 10. Total 45.

- A: 145 is the number who like at least one product: 80 + 70 + 60 - 30 - 25 - 20 + 10.
- B: 5 is the number who like none (150 - 145).
- C: 10 is the number who like all three products.
- D (key): correct, for the reason given above.

Trap: Reading the pairwise totals as 'exactly two' without removing the triple overlap.

Shortcut: Subtract the triple overlap from each pairwise total, then add the three results. Time target: 120 seconds.

**R2-Q36 — A.** The union of the two games is at least the larger group, 110. So the number who play neither is at most 200 - 110 = 90. This maximum occurs when all football players also play cricket.

- B: 110 is the cricket count, not the number playing neither.
- C: 95 is the football count, not the number playing neither.
- D: 105 subtracts the football count from 200 instead of using the union, which is at least 110.
- A (key): correct, for the reason given above.

Trap: Using the number of cricket or football players rather than the complement of the union.

Shortcut: Neither = 200 - union; the union is smallest when the groups overlap fully, so its minimum is 110. Time target: 90 seconds.

**R2-Q37 — D.** The union of the two groups is at most 100%, so the overlap is at least 60% + 45% - 100% = 5%.

- A: 15% is the difference between the two shares (60 - 45); the difference is not an overlap.
- B: 25% is not implied by the shares; it treats the two groups as overlapping by a quarter.
- C: 0% ignores that 60% + 45% exceeds 100%, which forces an overlap.
- D (key): correct, for the reason given above.

Trap: Reading the minimum overlap as zero when the two shares exceed the total.

Shortcut: Minimum overlap = sum of shares - 100%. Time target: 60 seconds.

**R2-Q38 — C.** Men: 120 - 70 = 50. Men who are managers: 45 - 30 = 15. Men who are not managers: 50 - 15 = 35.

- A: 15 is the number of men who are managers, not the number of men who are not managers.
- B: 45 is the total number of managers, not the men among them.
- D: 50 is all men, which includes the men who are managers.
- C (key): correct, for the reason given above.

Trap: Using the total managers rather than the male managers in the cross-table.

Shortcut: Build the 2 x 2 table: men = 50; men managers = 45 - 30. Time target: 80 seconds.

**R2-Q39 — A.** The last digit must be 0, 2 or 4. Last digit 0: the first digit has 4 choices (1 to 4) and the two middle digits have 3 x 2 = 6 choices: 24. Last digit 2: the first digit has 3 choices (1, 3, 4) and the middle digits 3 x 2 = 6: 18. Last digit 4 likewise gives 18. Total 24 + 18 + 18 = 60.

- B: 72 allows zero as the first digit, which does not make a four-digit number.
- C: 96 applies only the first-digit rule and ignores the requirement that the number be even.
- D: 120 counts arrangements of all five digits, not four-digit numbers.
- A (key): correct, for the reason given above.

Trap: Choosing the first digit from all five digits, or ignoring the even condition.

Shortcut: Fix the last digit (0, 2 or 4) first, then the first digit (nonzero), then the middle digits. Time target: 120 seconds.

**R2-Q40 — D.** Prime sums: 2 (1 way), 3 (2 ways), 5 (4 ways), 7 (6 ways), 11 (2 ways). Favourable outcomes: 15 of 36, which is 5/12.

- A: 1/2 would need 18 favourable outcomes; the count is 15.
- B: 1/3 would need 12 favourable outcomes; the count is 15.
- C: 7/36 counts only the sum of 7, one of the five prime sums.
- D (key): correct, for the reason given above.

Trap: Counting only the most common prime (7) or miscounting the ways for 11.

Shortcut: List the prime sums and their ways: 1 + 2 + 4 + 6 + 2 = 15 of 36. Time target: 90 seconds.

**R2-Q41 — B.** The worst case takes 4 red, 1 blue and 5 green (10 balls), which has no second blue ball, or 1 red, 3 blue and 5 green (9 balls), which has no second red ball. The largest failing draw is 10, so the answer is 11.

- A: 10 is the largest failing draw; the guarantee needs one more ball.
- C: 9 is the other failing branch, with one red, three blue and five green, and is not the largest failure.
- D: 6 ignores the green balls, which can all be drawn without helping the target.
- B (key): correct, for the reason given above.

Trap: Stopping at the largest failing draw without adding one ball.

Shortcut: Find the largest draw that fails either target, then add one. Time target: 120 seconds.

**R2-Q42 — C.** P(first ace) = 4/52; then P(second ace) = 3/51. Product = 12/2652 = 1/221.

- A: 1/169 is (1/13) squared, which assumes replacement and ignores the card removed.
- B: 1/13 is the probability of an ace in one draw from 13 ranks, not two aces in sequence.
- D: 3/52 is the probability of three aces in one draw of 52 cards, not two aces in sequence.
- C (key): correct, for the reason given above.

Trap: Squaring the single-draw probability when the draws are without replacement.

Shortcut: Multiply the two conditional fractions: 4/52 x 3/51. Time target: 75 seconds.

**R2-Q43 — A.** After the discount: 92 x 0.90 = 82.80. Change from 80: 2.80, which is 2.80 / 80 = 3.5%.

- B: Treats the discount as a flat Rs 10 off the new price, giving 82 and a change of 2 / 80 = 2.5%.
- C: Ignores the discount and reports the rise to 92: 12 / 80 = 15%.
- D: Reports the absolute rise of Rs 12 as a percentage of 100 rather than of 80.
- A (key): correct, for the reason given above.

Trap: Applying the discount to the old price, or treating a flat amount as a percentage.

Shortcut: Apply the discount to the new price, then express the final change against the original Rs 80. Time target: 90 seconds.

**R2-Q44 — A.** Shares of B: Q1 100/220 = 45.45%; Q2 150/280 = 53.57%. The first quarter above 50% is Q2. Q3 and Q4 are also above 50%, but they are not first.

- B: Q1 has B's share at 45.45%, below 50%.
- C: Q3 is above 50% (56.25%), but Q2 comes first.
- D: Q4 is above 50% (53.12%), but Q2 comes first.
- A (key): correct, for the reason given above.

Trap: Comparing B's sales with A's sales in one quarter only, instead of computing each share in order.

Shortcut: Compute B / (A + B) for each quarter in order and stop at the first above 50%. Time target: 100 seconds.

**R2-Q45 — C.** Multiply the two factors: 1.20 x 0.90 = 1.08. The net change is +8%.

- A: Adds the two percentage changes (20 - 10), ignoring that the bases differ.
- B: Reverses the sign of the net change: the revenue is higher, not lower, after the two years.
- D: Keeps only the first year's rise and ignores the 2023 fall.
- C (key): correct, for the reason given above.

Trap: Adding percentage changes that act on different bases.

Shortcut: Multiply the growth factors (1.2 and 0.9), then subtract one. Time target: 80 seconds.

**R2-Q46 — D.** The ratio rose from 120/80 = 1.5 to 150/60 = 2.5. The percentage change is (2.5 - 1.5) / 1.5 = 66.67%.

- A: 25% is the growth of X's own sales (120 to 150), not the change in the ratio.
- B: 40% divides the change of 1.0 by 2.5, using the new ratio as the base.
- C: 100% reports the absolute change in the ratio (1.0) as a percentage.
- D (key): correct, for the reason given above.

Trap: Using the new value as the base, or reporting a change in a ratio as if it were a change in a level.

Shortcut: Compute both ratios, then take the change over the 2023 ratio. Time target: 100 seconds.

**R2-Q47 — A.** Total of five subjects = 5 x 72 = 360. Fifth score = 360 - 280 = 80.

- B: 72 is the average itself, not the score in the fifth subject.
- C: 88 comes from a subtraction slip: 360 - 272.
- D: 92 is the average plus 20, with no basis in the totals.
- A (key): correct, for the reason given above.

Trap: Reporting the average as the missing value.

Shortcut: Find the five-subject total first, then subtract the known four. Time target: 60 seconds.

**R2-Q48 — D.** 2023: 90/360 x 1,200 = 300. 2024: 72/360 x 1,500 = 300. The number is unchanged at 300, although the angle and the total both changed.

- A: Uses the rise in the total respondents (1,200 to 1,500 is 25%) as if it applied to sector A.
- B: Uses the fall in the angle (72/90 = 0.8) as the fall in the number, ignoring the larger total.
- C: Subtracts the angles (90 - 72 = 18) and applies the old total: 18 / 360 x 1,200 = 60.
- D (key): correct, for the reason given above.

Trap: Reading a smaller angle as a smaller count when the total has grown.

Shortcut: Convert each angle to a count first (angle / 360 x total), then compare counts. Time target: 100 seconds.

**R2-Q49 — B.** Total score = 40 x 60 + 20 x 90 = 2,400 + 1,800 = 4,200. Average over 60 employees = 4,200 / 60 = 70.

- A: 75 is the simple average of the two branch averages, which ignores the different group sizes.
- C: 80 swaps the weights: (60 x 20 + 90 x 40) / 60 = 80.
- D: 90 reports only the higher branch average.
- B (key): correct, for the reason given above.

Trap: Averaging two averages without weighting them by the number of employees.

Shortcut: Total = sum of (group size x average); divide by the total group size. Time target: 90 seconds.

**R2-Q50 — B.** Totals: A 88, B 88, C 85, D 85, E 80. Order: B (88, interview 28), A (88, interview 20), D (85, interview 15), C (85, interview 10), E. Third is D.

- A: C is third only if the tie between C and D is broken in favour of the lower interview score, which reverses the rule.
- C: A is third only if candidates are ranked by written score alone (C 75, D 70, A 68).
- D: B is first in the correct order, not third.
- B (key): correct, for the reason given above.

Trap: Ranking by one component, or reversing the tie-break direction.

Shortcut: Compute totals, sort on total, then apply the interview tie-break to equal totals. Time target: 100 seconds.

**R2-Q51 — C.** The only grid is A B C / C A B / B C A. The top row contains one C, and the middle row contains one C, so the total is 2.

- A: Counts only one of the two rows.
- B: Counts three: the bottom row's C is outside the top and middle rows, and is wrongly added.
- D: Counts four, which would require two C's in each of the two rows.
- C (key): correct, for the reason given above.

Trap: Counting the whole grid, or including the bottom row.

Shortcut: Fill the grid from the top row and the bottom-right rule; then count C in the first two rows. Time target: 120 seconds.

**R2-Q52 — B.** The only valid weights are P 3 kg, Q 2 kg, R 1 kg, S 4 kg and T 5 kg. T is the heaviest.

- A: P is 3 kg, not the heaviest.
- C: R is the lightest box, at 1 kg.
- D: S is 4 kg; the condition that S is not the heaviest rules it out as the heaviest.
- B (key): correct, for the reason given above.

Trap: Assuming the box named in the clues is the heaviest rather than testing the remaining box.

Shortcut: Chain the three comparisons (R < Q < P < S), then place T in the remaining weight. Time target: 90 seconds.

**R2-Q53 — A.** The only order is L1, L4, L2, L3. L1 is in slot 1.

- B: L2 is in slot 3 in the only valid order.
- C: L3 is in slot 4 in the only valid order.
- D: L4 is in slot 2 in the only valid order, not slot 1.
- A (key): correct, for the reason given above.

Trap: Placing the immediately-before pair without checking the slot 4 exclusion for L1.

Shortcut: Place the pair L2-L3 as a block; then fix L4 and L1 with their exclusions. Time target: 100 seconds.

**R2-Q54 — C.** Day 1 must be Chitra: Anu cannot be on Day 1, Dinesh must be on Day 3 or 4, and Bala cannot come first because Chitra must come immediately before Bala. Bala is then on Day 2, and Anu and Dinesh take Days 3 and 4 in either order.

- A: Anu cannot be on Day 2 in every valid rota; Anu is on Day 3 or Day 4.
- B: Chitra is on Day 1 in every valid rota, not Day 2.
- D: Dinesh is on Day 3 or Day 4 by condition, not Day 2.
- C (key): correct, for the reason given above.

Trap: Testing one valid rota and stopping before checking that the answer holds in all of them.

Shortcut: Place Chitra and Bala as a block; Anu and Dinesh then fill the other two days. Time target: 120 seconds.

**R2-Q55 — A.** After the transfer: W 33%; X 27% + 7.2% = 34.2%; Y 22% + 10.8% = 32.8%. X has the most votes and wins.

- B: W led the first count but does not have the most votes after the transfer.
- C: Y gains the larger share of Z's votes but still finishes third at 32.8%.
- D: Z is eliminated before the final count and cannot win.
- A (key): correct, for the reason given above.

Trap: Judging by the first-count leader rather than recalculating after the transfer.

Shortcut: Add the transfer shares to each remaining candidate, then compare totals. Time target: 100 seconds.

**R2-Q56 — A.** A and B cost Rs 50 lakh and give a benefit of 75. Every other feasible pair gives less: C and D give 72, A and E give 70, and B and E give 65.

- B: C and D cost Rs 60 lakh and give 72; feasible, but A and B give more.
- C: A and E cost Rs 55 lakh and give 70; feasible, but not the maximum.
- D: B and E cost Rs 45 lakh and give 65; feasible, but not the maximum.
- A (key): correct, for the reason given above.

Trap: Choosing the single most valuable project and adding the next one within budget without checking all pairs.

Shortcut: List the pairs within budget and compare benefits; the largest single benefit is not always in the best pair. Time target: 120 seconds.

**R2-Q57 — B.** Only A is a knight. Then A's statement is true (B is a knave), B's statement is false (A and C are of different types, since C is a knave), and C's statement is false (B is a knave). Every statement matches the speaker's type, and no other assignment does.

- A: With B the only knight, C is a knave, so C's statement 'B is a knight' would be true, which a knave cannot say.
- C: With C the only knight, A and B are knaves, so A's statement 'B is a knave' would be true, which a knave cannot say.
- D: With B and C as knights, B's statement 'A and C are of the same type' is false, since A is a knave and C a knight, but a knight cannot say that.
- B (key): correct, for the reason given above.

Trap: Testing each person in isolation instead of checking all three statements together.

Shortcut: Assume one person's type, test the statements of the other two, and check for contradictions. Time target: 120 seconds.

**R2-Q58 — C.** The only valid orders are A, D, B, C and A, D, C, B. In both, D is second.

- A: A is always first in the valid orders, so it cannot be second.
- B: B is third in one valid order and fourth in the other, so it is never second.
- D: C is third or fourth in the valid orders, so it is never second.
- C (key): correct, for the reason given above.

Trap: Assuming that the task named first in a constraint is the one that must come second.

Shortcut: Treat A and D as a block with D after A; then check the remaining placements against the other two rules. Time target: 100 seconds.

**R2-Q59 — B.** Of the six possible assignments, the valid ones are (X in 2, Y in 3, Z in 1) and (X in 3, Y in 1, Z in 2). That makes 2.

- A: 1 treats one assignment as the only possibility, missing the second valid arrangement.
- C: 3 counts the assignments that break exactly one rule, not those that break none.
- D: 6 counts every assignment, ignoring the three exclusions.
- B (key): correct, for the reason given above.

Trap: Counting arrangements with a forbidden position without listing them, or assuming that the three exclusions cancel out.

Shortcut: List the six assignments and cross out any with a forbidden placement. Time target: 120 seconds.

**R2-Q60 — B.** Getting no head means TTT, which has probability 1/8. An event with probability above zero is possible, and 1/8 is far from certain, so 'possible but improbable' is correct.

- A: Three heads in a row has probability 1/8, so it is possible but not certain.
- C: No head has probability 1/8, which is above zero, so it is possible.
- D: No head has probability 1/8, so at least one head has probability 7/8: not certain.
- B (key): correct, for the reason given above.

Trap: Treating 'possible' as 'probable', or treating a small but non-zero probability as impossible.

Shortcut: Possible needs probability above zero; certain needs probability one; compute the one outcome asked. Time target: 75 seconds.
