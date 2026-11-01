# CSAT 06 — Revision 3: worked answers

Sources: B = `upsc-ai-kit/knowledge/CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; A = `upsc-ai-kit/knowledge/CSAT/advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md`. Every key was checked by computation or explicit enumeration (see `../AUDIT.md`, section 7). Times are targets in seconds.

**R3-Q01 — A.**

- A (key). Asha and Chitra are both trained and cleared, so the only admissible pair is this one.
- B. Dev is cleared but not trained, so Rule 1 excludes him.
- C. Bilal is neither trained nor cleared, so Rule 2 and Rule 1 both exclude him.
- D. Dev is cleared but not trained, so Rule 1 excludes him.
- Trap: Reading 'Cleared' as sufficient for a posting and forgetting Rule 1 for Dev, who clears Rule 2 but not Rule 1.
- Shortcut: Eliminate any officer failing either rule first; only two trained and cleared officers remain, so the pair is forced.
- Time target: 80 seconds. Source: B §3, §4.2; A §3 (Method 4).

**R3-Q02 — B.**

- A. Premise 2 places tax consultants among graduates, but not among auditors; a model with a non-auditor tax-consultant graduate fails it.
- B (key). Some graduates are tax consultants (premise 2) and no tax consultant is salaried (premise 3), so those graduates are not salaried. Follows in every model.
- C. Auditors may all be unsalaried; nothing links auditors to salaried employees. Not forced.
- D. Salaried graduates may exist outside the tax-consultant group. Premises do not exclude them.
- Trap: Converting 'some graduates are tax consultants' into 'every graduate is a tax consultant', or reversing the auditor inclusion.
- Shortcut: Draw the graduate circle, place the tax-consultant overlap inside it, then mark that overlap as outside salaried; two sets suffice.
- Time target: 75 seconds. Source: B §4.2, §7; A §2 (syllogism validity).

**R3-Q03 — C.**

- A. Dismissed reviewers may be people who never attended and so never passed; the premises say nothing about them. Not forced.
- B. Only the attending reviewers are known to have passed; other reviewers may not have taken the test.
- C (key). The reviewers who attended are inside the attendee group; they passed (premise 2), so they were not dismissed (premise 3). Follows in every model.
- D. Premise 1 says only 'some' reviewers attended, so non-reviewers may attend too.
- Trap: Using 'some reviewers attended' to infer that all attendees are reviewers, or treating 'some' as 'all' for the passing step.
- Shortcut: Chain the universal premise (attend -> pass -> not dismissed) only over the existing reviewer-attendees.
- Time target: 75 seconds. Source: B §4.2, §7; A §2.

**R3-Q04 — D.**

- A. Premise 3 excludes instructors from the pilot group, so no pilot can be an instructor. Forced false.
- B. Premise 2 names only 'some' passers as instructors; instructors need not have taken the test.
- C. A model in which every test-passer is an instructor exists (for example, one with no licensed pilots), so the premises do not force this claim.
- D (key). The instructors who passed the medical test are not pilots (premise 3). Forced true in every model.
- Trap: Treating 'not necessary' as 'false', or assuming the 'some' premise makes the converse true.
- Shortcut: Locate the overlap named by the 'some' premise and see which exclusion it must respect; ignore the rest.
- Time target: 75 seconds. Source: B §4.1, §4.2; A §5.

**R3-Q05 — A.**

- A (key). Chaining (i) and (ii) gives approved -> met -> published; (iii) denies published, so approval is false. Forced true.
- B. (ii) and (iii) together force the committee not to have met, so 'the committee met' is false.
- C. Published minutes are denied by (iii), so the conjunction fails.
- D. The chain makes approval impossible under the premises, so 'approval remains possible' is false.
- Trap: using the converse of (ii) ('published -> met') or reading the stem's 'three statements' as a list of two.
- Shortcut: Write the chain approved -> met -> published, apply not-published, and read off not-approved in one line.
- Time target: 60 seconds. Source: B §4.2; A §3 (Method 4).

**R3-Q06 — B.**

- A. Conclusion I follows, so 'neither' is false.
- B (key). Pencils that are erasers are also sharpeners, so some pencils are sharpeners. II reverses the inclusion 'all erasers are sharpeners', which is not valid.
- C. Only II is wrong because I does follow; and II, the converse of the premise, is not forced: a model with extra sharpeners that are not erasers satisfies both premises.
- D. 'Both' fails because II, the converse of 'all erasers are sharpeners', is not forced.
- Trap: Accepting the converse II because the premises 'sound connected'.
- Shortcut: Draw erasers inside sharpeners, place the pencil-eraser overlap, then test each conclusion for a counter-diagram.
- Time target: 70 seconds. Source: B §4.2, §7; A §2.

**R3-Q07 — C.**

- A. 'Only two are gold' does not mean two cannot be drawn; two gold coins can be drawn in order, so the claim is false.
- B. 1/15 would follow from (2/10) x (1/3) and wrongly treats the second draw as 1 of 3 coins.
- C (key). P = (2/10) x (1/9) = 2/90 = 1/45, using the conditional fraction for the second draw. Correct.
- D. 1/5 is only the first-draw probability; the second draw must also be gold.
- Trap: Confusing 'possible' (probability > 0) with 'probable', and multiplying the unchanged first-draw fraction for the second draw.
- Shortcut: Possibility needs one favourable route; the number needs (2/10) x (1/9) with the changed denominator.
- Time target: 60 seconds. Source: B §4.1, §9 item 6; A §5.

**R3-Q08 — D.**

- A. 'Known to have passed' is not forced: sample 14 may never have been tested, and the facts do not say it passed.
- B. This contradicts the stated fact that sample 14 is from Batch B.
- C. This is the converse of the premise (rejected -> failed). Another rejected Batch B sample could have passed, so the claim is not forced.
- D (key). The premise is failed -> rejected. Sample 14 was not rejected, so by the contrapositive it did not fail. Forced true.
- Trap: reversing the conditional (option C), or treating 'not rejected' as 'passed' (option A).
- Shortcut: Contrapositive only: not rejected -> not failed.
- Time target: 60 seconds. Source: B §4.2, §4.1; A §5.

**R3-Q09 — A.**

- A (key). Gaps are 3, 4, 5, so the next gap is 6 and the position is 14 + 6 = 20, which is T.
- B. Position 19 (S) repeats the last gap of 5; the gaps are growing.
- C. Position 21 (U) uses a gap of 7, which skips the rule's next gap of 6.
- D. Position 22 (V) uses a gap of 8, two steps ahead of the rule.
- Trap: Adding the last gap again (5) or jumping by the next-but-one gap.
- Shortcut: Read the gaps first (3, 4, 5), add the next gap (6) to position 14.
- Time target: 55 seconds. Source: B §2 (series), §9 item 1.

**R3-Q10 — B.**

- A. 92 = 2 x 47 - 2 applies a constant of -2 instead of the rule's +1.
- B (key). Each term is twice the previous term plus 1: 2 x 47 + 1 = 95. Correct.
- C. 94 = 2 x 47 is a doubling without the added 1.
- D. 96 = 2 x 47 + 2 applies +2 instead of +1.
- Trap: Adding a fixed difference, or doubling without the constant.
- Shortcut: Check the ratio of successive differences: 3, 6, 12, 24 double each time, so next difference 48 and 47 + 48 = 95.
- Time target: 55 seconds. Source: B §2 (series); A §8.

**R3-Q11 — C.**

- A. HMLD applies the mirror step but omits the reversal.
- B. WONS is the reversal of SNOW alone, with no mirror step.
- C (key). Mirror: S->H, N->M, O->L, W->D gives HMLD; reversed gives DLMH. Correct.
- D. DLHM is the right reversal with its last two letters swapped (M and H).
- Trap: Applying only one of the two steps, or misreading the mirror step as a single shift.
- Shortcut: Mirror each letter (27 minus its position), then reverse. Check the rule on both examples before answering.
- Time target: 70 seconds. Source: B §2 (coding), §5 Example I, §7; A §2.

**R3-Q12 — D.**

- A. 12 stops after the multiplication (24 ÷ 6 × 3) and ignores the last two operations.
- B. 17 is the result before the final subtraction; the '− 2' is ignored.
- C. 19 is obtained by turning the final subtraction into addition.
- D (key). 24 ÷ 6 = 4, 4 × 3 = 12, 12 + 5 = 17, 17 − 2 = 15. Correct.
- Trap: Substituting the symbols but then evaluating + and − before × and ÷, or dropping the last operation.
- Shortcut: Rewrite the expression with normal symbols, then do left-to-right division and multiplication before the additions.
- Time target: 70 seconds. Source: B §2 (coding); A §2.

**R3-Q13 — A.**

- A (key). GAIN = 7 + 1 + 9 + 14 = 31. Correct.
- B. DAY = 4 + 1 + 25 = 30.
- C. MEN = 13 + 5 + 14 = 32.
- D. ROAD = 18 + 15 + 1 + 4 = 38.
- Trap: Adding one letter too few or too many, which lands on a neighbouring value (30 or 32).
- Shortcut: Sum each word's letter values; check the 3-letter words first, then the 4-letter words.
- Time target: 60 seconds. Source: B §2 (coding), §5 Example I.

**R3-Q14 — B.**

- A. 81 = 9 squared continues the odd-number pattern, but 9 is not prime.
- B (key). The terms are 2, 3, 5, 7 squared; the next prime is 11, so the next term is 121. Correct.
- C. 143 = 11 x 13 is a product, not a square.
- D. 169 = 13 squared skips the prime 11.
- Trap: Using consecutive odd numbers instead of consecutive primes.
- Shortcut: Recognise the squares of 2, 3, 5, 7; the next prime is 11.
- Time target: 55 seconds. Source: B §2 (series).

**R3-Q15 — C.**

- A. 27 = 14 + 13 adds the sixth and seventh terms, not the seventh and eighth.
- B. 30 = 14 + 16 adds the sixth and eighth terms.
- C (key). Odd positions 7, 9, 11, 13 and even positions 10, 12, 14, 16 each rise by 2. So t7 = 13 and t8 = 16; the sum is 29. Correct.
- D. 31 = 13 + 18 uses a wrong eighth term.
- Trap: Treating the series as a single alternating +3, -1 pattern and taking the wrong term positions.
- Shortcut: Split the series into odd and even positions; each subseries rises by 2.
- Time target: 70 seconds. Source: B §2 (series), §9 item 1.

**R3-Q16 — D.**

- A. 25-18-9-23 applies the letter values but omits the reversal.
- B. 23-18-9-25 reverses the word but swaps the middle two numbers.
- C. 2-9-18-4 uses the plain alphabet positions, with no 27-minus step and no reversal.
- D (key). B -> 25, I -> 18, R -> 9, D -> 23; reversed order gives 23-9-18-25. Correct.
- Trap: Reversing the word but forgetting the 27-minus step, or applying the 27-minus step but reading the letters in the wrong direction.
- Shortcut: Convert each letter to 27 minus its position, then write the numbers from last letter to first.
- Time target: 70 seconds. Source: B §2 (coding), §5 Example I; A §2.

**R3-Q17 — A.**

- A (key). Final position is (8, 0): the 9 km north and 9 km south legs cancel; the 5 km east and 3 km east legs add to 8 km east. Correct.
- B. 5 km due East ignores the last leg of 3 km east.
- C. 2 km due West reads the final left turn as a right turn, which would send the person west from (5, 0).
- D. 8 km due West reverses the direction of the displacement.
- Trap: Adding path lengths instead of tracking displacement, or reading the final left turn as a right turn.
- Shortcut: Cancel opposite legs first: the north-south legs net to zero, and the east legs remain.
- Time target: 75 seconds. Source: B §2 (directions), §6; B §9 item 3.

**R3-Q18 — B.**

- A. North would result if the two left turns were ignored after the three rights.
- B (key). East to South to West to North after three rights; then North to West to South after two lefts. Correct.
- C. East would need a net multiple of four quarter-turns; her net is one clockwise quarter-turn.
- D. West would need a net of two clockwise quarter-turns, but the stem gives one.
- Trap: Miscounting the net turns or using the wrong sign for a left turn.
- Shortcut: Net the quarter-turns: three rights and two lefts equal one right, so east turns clockwise once.
- Time target: 55 seconds. Source: B §2 (directions), §6.

**R3-Q19 — C.**

- A. A paternal grandfather is the father of S's father. R is the father of S's mother, so the line runs through the mother.
- B. A maternal uncle would be the brother of S's mother; R is S's grandfather, not S's uncle.
- C (key). S is a child of P, and R is P's father, so R is S's maternal grandfather. Correct.
- D. R is S's grandfather, not father; S's father is not named in the stem.
- Trap: Going up one generation too few, or labelling the line as paternal when the link runs through the mother.
- Shortcut: Draw P at the centre: R above P, Q and S below P; then name R's link to S through P.
- Time target: 65 seconds. Source: B §2 (blood relations), §5 Example B, §6.

**R3-Q20 — D.**

- A. 5 gives g = 2 and b = 3 from the first condition, but the second needs b = 2(g - 1) = 2; it fails.
- B. With 6 children, b - 1 = g makes b + g odd, so 6 cannot satisfy the first condition.
- C. With 8 children, b - 1 = g makes b + g odd, so 8 cannot satisfy the first condition.
- D (key). Ramu's brothers = b - 1 = g, and a sister's brothers = b = 2(g - 1), so b = 4 and g = 3; total 7. Correct.
- Trap: Counting Ramu's own sisters and brothers as if he were not part of the total, or doubling a single group.
- Shortcut: Write b - 1 = g and b = 2(g - 1), solve in two lines, then add b + g.
- Time target: 75 seconds. Source: B §2 (blood relations), §7; B §9 item 9.

**R3-Q21 — A.**

- A (key). Positions: (0,3), then (4,3), then (4,6), then (0,6). He is 6 km north of the start. Correct.
- B. 6 km south reverses the sign of the north displacement.
- C. 4 km west reads only the final leg as the answer.
- D. 14 km north adds all four path lengths in the wrong direction.
- Trap: Adding total distance walked instead of finding the net displacement.
- Shortcut: Track each position in turn; the east and west legs cancel, and the two north legs (3 km + 3 km) remain.
- Time target: 70 seconds. Source: B §2 (directions), §9 item 3.

**R3-Q22 — B.**

- A. T sits in seat 2, not seat 3; seat 3 is P's seat.
- B (key). Clue (c) puts Q in seat 1 or 5, and clue (e) (Q left of S) forces Q into seat 1. Clue (a) makes R = P + 1 and clue (d) puts T left of R; the only placements of P, R and T that survive are P in seat 3, R in seat 4 and T in seat 2, and clue (b) then rules out the alternative with T and S adjacent in seats 2 and 3. So S is in seat 5 and the seating is Q, T, P, R, S (checked by enumeration of all 120 orders). Correct.
- C. R is in seat 4, directly to the right of P in seat 3, not in seat 3 itself.
- D. S is in seat 5, not seat 3; seat 3 is P's seat.
- Trap: Placing R before P or ignoring clue (e), which fixes the far-right occupant.
- Shortcut: Start with the end-seat clue (c) and the Q-left-of-S clue (e): Q is in seat 1. Then place R = P + 1 with T left of R, and use clue (b) to eliminate the rest.
- Time target: 90 seconds. Source: B §2 (arrangements), §4; A §3 (Method 1).

**R3-Q23 — C.**

- A. D sits three seats anticlockwise of A (seat 5 when A is at seat 0), so D is not A's left-hand neighbour.
- B. G sits three seats clockwise of A (seat 3), so G is not adjacent to A.
- C (key). Anchor A at seat 0. Then B is at seat 4 (opposite), C at seat 2 (second clockwise), G at seat 3 (immediately clockwise of C), D at seat 5 (next to B), E at seat 6 (the only seat not next to A), H at seat 1 (not next to E), and F at seat 7. F is the seat immediately anticlockwise of A, so F is the left-hand neighbour. Correct.
- D. H sits at seat 1, immediately clockwise of A, so H is A's right-hand neighbour.
- Trap: reading 'second to the right' as second anticlockwise, or anchoring on the wrong person.
- Shortcut: Anchor A, place B opposite and C two steps clockwise, then fill the rest with the clue on E and H.
- Time target: 100 seconds. Source: B §2 (circular seating), §4; A §3 (Method 1).

**R3-Q24 — D.**

- A. P is in seat 1 in only four of the eight seatings; in others P sits in seat 2 or seat 4. Not forced.
- B. R sits in seat 2 in only two of the eight seatings; in the others R is in seat 1 or seat 4. Not forced.
- C. T is in seat 4 in only two of the eight seatings; in the others T is in seat 2 or seat 3. Not forced.
- D (key). Clue (c) forces this: R can never be in seat 3, because then S and T (adjacent, not at ends) would need seats 2 and 4, which are not adjacent. So Q is in seat 5 in every seating. Correct.
- Trap: Treating a single valid seating as the answer, or confusing 'some' seatings with 'every' seating.
- Shortcut: Check each statement against all seatings; eliminate any option that fails in one seating. Clue (c) forces the answer.
- Time target: 90 seconds. Source: B §2; A §5 (multiple solutions).

**R3-Q25 — A.**

- A (key). A is taller than B (1), and B is taller than C (3), so A is taller than C in every ordering. Correct.
- B. E sits between A and D, but its position relative to B varies; some orderings put B above E. Not forced.
- C. D is taller than C but may be shorter than B; the premises do not fix D against B. Not forced.
- D. A is above E by clue (4), so E can never be the tallest. Forced false.
- Trap: Trusting the nearest-looking comparison; several orderings satisfy the premises.
- Shortcut: Chain the given comparisons (A > B > C), then test each option against every ordering; one failure rules it out.
- Time target: 75 seconds. Source: B §3 (method), §2; A §2 (constraint ordering).

**R3-Q26 — B.**

- A. 26 adds only four codes: it leaves out one of the neighbour codes, so it cannot be the full sum.
- B (key). Seating: Hari, Gita, Kiran, Lata, Mohan. Codes: Hari 0 (seat 1); Gita 8 (left neighbour Hari, H = 8); Kiran 7 (left neighbour Gita, G = 7); Lata 11 (left neighbour Kiran, K = 11); Mohan 12 (left neighbour Lata, L = 12). Sum 38. Correct.
- C. 43 uses the right-hand neighbour's initial instead of the left-hand neighbour's.
- D. 46 gives Hari the code 8 (her own initial) instead of 0, because seat 1 has no one on the left.
- Trap: Reading 'left' as 'right' when assigning neighbours, or giving the seat-1 person a non-zero code.
- Shortcut: Seat the row from clue (a) and (b) first, then Lata and Mohan; the codes are just the neighbour initials on the left.
- Time target: 100 seconds. Source: B §2 (arrangements), §2 (coding); A §3 (Methods 1–2).

**R3-Q27 — C.**

- A. 24 = (6-2)! omits the factor 2 for the two ways the pair can face each other around the table.
- B. 72 counts the seatings in which A and B are not adjacent.
- C (key). Treat AB as one block: 2 internal orders x (5 - 1)! = 2 x 24 = 48 circular arrangements. Correct.
- D. 120 = 5! counts all seatings of the six people with A fixed, not only the adjacent ones.
- Trap: Dividing by 2 for reflections when the stem says mirror images are different, or forgetting that the pair has two internal orders.
- Shortcut: Fix A, then B has two seats next to it; the other four people fill the rest in 4! ways: 2 x 24 = 48.
- Time target: 80 seconds. Source: B §4 (circular (n-1)!), §5 Example H; A §4.

**R3-Q28 — D.**

- A. 1680 = 8! / (2! x 3! x 2): it divides out an extra factor of 2 that the word does not supply.
- B. 6720 = 8!/3! divides only for the three Ls and forgets the two As.
- C. 40320 = 8! ignores both repetitions.
- D (key). PARALLEL has 8 letters, with A twice and L three times: 8!/(2! x 3!) = 3360. Correct.
- Trap: Dividing by only one repeat factorial, or forgetting repeats altogether.
- Shortcut: Count letters with repeats (A twice, L three times), then divide 8! by 2! x 3!.
- Time target: 70 seconds. Source: B §4 (arrangements with repeats), §9 item 2.

**R3-Q29 — A.**

- A (key). Ending in 0: 5 x 4 x 3 = 60 (first digit from {1..5}). Ending in 5: first digit from {1, 2, 3, 4} (4 ways), then 4 x 3 for the middle digits = 48. Total 108. Correct.
- B. 60 counts only the numbers ending in 0.
- C. 96 = 60 + 36: for numbers ending in 5 it lets the first digit come only from {1, 2, 3}, losing the digit 4.
- D. 120 = 60 + 60: for numbers ending in 5 it allows zero as the first digit, a leading-zero error.
- Trap: Forgetting that the first digit cannot be zero when the number ends in 5; forgetting that the number ends in 0 or 5 for divisibility by 5.
- Shortcut: Split by the last digit (0 or 5), then count the first digit separately.
- Time target: 90 seconds. Source: B §4, §5 Example K, §7.

**R3-Q30 — B.**

- A. 179 subtracts the all-men and all-women groups twice, which double-counts the exclusions.
- B (key). Total C(10,4) = 210; subtract all-men C(6,4) = 15 and all-women C(4,4) = 1: 210 - 16 = 194. Correct.
- C. 195 subtracts only the all-men committees and forgets to exclude the all-women group.
- D. 210 is the unrestricted total; it includes the two excluded groups.
- Trap: Subtracting only one excluded group, or subtracting the same group twice.
- Shortcut: Count all committees, then remove the two single-gender groups: 210 - 15 - 1.
- Time target: 80 seconds. Source: B §4 (combinations), §9 item 13.

**R3-Q31 — C.**

- A. 7 assumes only three colours (two of each = 6, then one more), which ignores the yellow balls.
- B. 8 balls (two of each of the four colours) can be drawn with no colour appearing three times, so 8 is not enough.
- C (key). Take two of each of the four colours (8 balls, no triple), then one more: 9. Correct.
- D. 10 is one ball more than the worst case needs; the worst case is already forced at 9.
- Trap: Using only three colours in the worst case, or adding one ball too many because the worst case was counted wrongly.
- Shortcut: Worst case: take the maximum without a triple (2 each of four colours = 8), then add one.
- Time target: 70 seconds. Source: B §5 Example N (worst case), §9 item 14.

**R3-Q32 — D.**

- A. 16 counts only the unit squares.
- B. 25 is the number of unit squares in a 5 x 5 grid; the stem has only four rows and columns of cells.
- C. 36 = 6 x 6 counts squares as if the grid had six lines in each direction.
- D (key). Size 1: 16; size 2: 9; size 3: 4; size 4: 1. Total 30. Correct.
- Trap: Counting only the unit squares, or treating a 4 x 4 cell grid as having more lines.
- Shortcut: Count by side length: 4^2 + 3^2 + 2^2 + 1^2.
- Time target: 60 seconds. Source: B §5 Example N (grid count), §2 (visual).

**R3-Q33 — A.**

- A (key). Exactly two painted faces lie along the 12 edges, excluding corners: 12 x (5 - 2) = 36. Correct.
- B. 24 is the count for a side of 4 (12 x (4 - 2)), a wrong side length.
- C. 27 is the number of unit cubes with no painted face (interior), not two faces.
- D. 54 is the number with exactly one painted face: 6 x (5 - 2)^2.
- Trap: Mixing up the three categories: one painted face (face centres), two (edge cubes), three (corners).
- Shortcut: Edge cubes (exactly two faces) = 12 edges x (side - 2); corners are excluded.
- Time target: 80 seconds. Source: B §2 (visual/cube), §5 Example N.

**R3-Q34 — B.**

- A. 37 omits the triple overlap: 25 + 16 + 11 - 8 - 2 - 5 = 37, with the triple term never added back.
- B (key). Multiples: 4 gives 25, 6 gives 16, 9 gives 11; pairs use lcm: 12 gives 8, 36 gives 2, 18 gives 5; triple lcm 36 gives 2. 25 + 16 + 11 - 8 - 2 - 5 + 2 = 39. Correct.
- C. 43 uses 24 as lcm(4, 6), which is wrong: 24 yields 4 multiples, so the pairwise term is 4, not 8.
- D. 52 is the sum of single-set counts without any overlap removal.
- Trap: Using lcm(4,6) = 24 rather than 12, or forgetting to add the triple overlap back.
- Shortcut: Use the lcm of each pair and the triple: 12, 36, 18 for pairs and 36 for the triple.
- Time target: 95 seconds. Source: B §4 (inclusion–exclusion), §5 Example J; A §2.

**R3-Q35 — C.**

- A. 8 = 48 - 40 gives a difference of single-language counts, not an overlap bound.
- B. 35 = 75 - 40 subtracts only the English count from the total.
- C (key). Lower bound: 48 + 40 - 75 = 13; this is least because no more than 75 can be covered without overlap. Correct.
- D. 40 is the largest possible overlap, bounded by the smaller set, not the least.
- Trap: Reporting the upper bound (the smaller set) as the least, or subtracting the wrong set from the total.
- Shortcut: Least overlap = |A| + |B| - total, provided it is not negative.
- Time target: 60 seconds. Source: B §4, §5 Example J (Venn bounds).

**R3-Q36 — D.**

- A. 5 is the number who play none of the three games.
- B. 45 is the number who play exactly two games (20 + 15 + 10).
- C. 115 is the number who play at least one game.
- D (key). Exactly one = 70 + 60 + 50 - 2(30 + 25 + 20) + 3(10) = 60. Correct.
- Trap: Reporting the union, or the exactly-two count, instead of the exactly-one count.
- Shortcut: Exactly one = sum of singles, which you can build from the region counts: triple 10, then pair-only parts, then singles.
- Time target: 95 seconds. Source: B §4; A §2, §8 item 4.

**R3-Q37 — A.**

- A (key). Last digit must be even: 2 or 4 (2 ways). First digit: 4 remaining choices. Middle digit: 3 choices. 2 x 4 x 3 = 24. Correct.
- B. 12 counts with the last digit fixed to 2 only.
- C. 30 = 5 x 3 x 2 lets the first digit take any of the five digits and then restricts the last digit to two options, which is an inconsistent count.
- D. 60 = 5 x 4 x 3 ignores the parity condition.
- Trap: Choosing the first digit from all five digits before the even last digit is fixed.
- Shortcut: Fix the last digit first (even: 2 or 4), then the first and middle digits from what remains.
- Time target: 75 seconds. Source: B §4 (sets), §7; A §2.

**R3-Q38 — B.**

- A. 5/14 = 10/28 counts only the two-red outcomes.
- B (key). Same colour = two reds C(5,2) = 10 or two blues C(3,2) = 3, out of C(8,2) = 28 pairs: 13/28. Correct.
- C. 17/32 = (5/8)^2 + (3/8)^2 treats the draws as independent with replacement, which the stem rules out.
- D. 1/2 is a guessed-looking value that ignores the without-replacement structure.
- Trap: Using independent fractions for a draw without replacement.
- Shortcut: Count pairs with C(n,2): same-colour pairs over all pairs, 13/28.
- Time target: 70 seconds. Source: B §4, §5 Example L; A §2 (without replacement), §8 item 6.

**R3-Q39 — C.**

- A. 1/2 adds the three single-roll probabilities (3 x 1/6), which is invalid because the events overlap.
- B. 125/216 = (5/6)^3 is the probability of no six, the complement of the requested event.
- C (key). 1 - (5/6)^3 = 1 - 125/216 = 91/216. Correct.
- D. 1/216 = (1/6)^3 is the probability of three sixes, a single outcome of the sample space.
- Trap: Adding probabilities of overlapping events, or reporting the complement.
- Shortcut: At least one = 1 - P(no six in any roll) = 1 - (5/6)^3.
- Time target: 60 seconds. Source: B §4 (complement), §9 item 14; A §4.

**R3-Q40 — D.**

- A. 1/6 counts only the totals of at least 10 (6 outcomes) and ignores the equal-faces event.
- B. 1/3 = 12/36 adds 6 + 6 without subtracting the overlap of (5,5) and (6,6).
- C. 7/18 = 14/36 counts the overlap twice.
- D (key). Totals of 10 or more: 6 outcomes; equal faces: 6 outcomes; both: (5,5) and (6,6), so the union is 10/36 = 5/18. Correct.
- Trap: Adding the two events without removing their shared outcomes.
- Shortcut: Union = 6 + 6 - 2 = 10 out of 36.
- Time target: 75 seconds. Source: B §4 (union); A §8 item 5.

**R3-Q41 — A.**

- A (key). Restricting to the 16 Economics students, 10 are women: 10/16 = 5/8. Correct.
- B. 5/12 = 10/24 is the probability that an Economics student is a woman out of all women, which reverses the condition.
- C. 1/4 = 10/40 is the joint probability (woman and Economics) out of all students, not the conditional one.
- D. 2/5 = 16/40 is the probability of studying Economics, not of being a woman given Economics.
- Trap: Using the total population as the denominator when the stem conditions on Economics students.
- Shortcut: Shrink the sample space to the 16 Economics students, then count women among them.
- Time target: 70 seconds. Source: B §4 (conditional), §9 item 11; A §8 item 9.

**R3-Q42 — B.**

- A. 1/3 = 20/60 is the share of all employees who are in Operations, which ignores the training condition.
- B (key). Trained employees total 12 + 15 + 10 = 37; Operations trained are 15: 15/37. Correct.
- C. 3/4 = 15/20 is the probability of being trained given Operations, which reverses the condition.
- D. 1/4 = 15/60 is the joint probability of being trained and in Operations, out of all employees.
- Trap: Dividing by the full workforce instead of the trained subgroup, or swapping the conditioning event.
- Shortcut: Restrict to the trained column (37), then take the Operations entry (15).
- Time target: 85 seconds. Source: B §4, §5 Example L; A §2.

**R3-Q43 — C.**

- A. -7.1% divides the fall by the Year 2 value (2.8) instead of the Year 1 value (3.0), using the wrong base.
- B. -21.3% is the change in total revenue (182/150 - 1 = +21.3%) with the sign reversed; it is not a per-unit measure.
- C (key). Revenue per thousand units: 150/50 = 3.0 and 182/65 = 2.8. Change = (2.8 - 3.0)/3.0 = -6.7%. Correct.
- D. -30.0% reverses the sign of the output growth (65/50 - 1 = +30%); it measures output, not revenue per unit.
- Trap: Reporting the change in total revenue or output instead of revenue per unit, or dividing by the wrong year.
- Shortcut: Compute each year's per-unit value first, then the percentage change from Year 1.
- Time target: 90 seconds. Source: B §5 Example M, §7 (DI traps); A §10.

**R3-Q44 — D.**

- A. +8% relative confuses the point change with the relative change; the relative change needs the old base 22.
- B. +36.4 points mixes up the relative change with the point change; the point change is 8.
- C. +27% divides by the new share (30), not the old share (22).
- D (key). Share change = 30 - 22 = +8 points; relative change = 8/22 = +36.4%. Correct.
- Trap: Quoting the point change as the percentage change, or dividing by the wrong base.
- Shortcut: Points = new minus old; relative = points divided by the old share.
- Time target: 75 seconds. Source: B §5 Example M, §9 item 12; A §10 (trap 3).

**R3-Q45 — A.**

- A (key). C + D = 40 per cent of 480 = 192; B = 35 per cent = 168; difference 24. Correct.
- B. 12 is half the correct gap, which would arise from taking 5 per cent of 240 rather than of 480.
- C. 48 is 10 per cent of 480, the gap between B (35 per cent) and A (25 per cent), not between B and C plus D.
- D. 96 is C alone (20 per cent of 480), ignoring department D.
- Trap: Comparing B with a single department, or using a wrong base.
- Shortcut: Add the two shares (40 per cent), take 35 per cent from the same total, and subtract.
- Time target: 85 seconds. Source: B §5 Example M (pie reading), §2 (DI).

**R3-Q46 — B.**

- A. 160 is the price after the fall only; the subsequent rise is ignored.
- B (key). 200 x 0.8 = 160; 160 x 1.25 = 200. The two changes cancel exactly because 0.8 x 1.25 = 1. Correct.
- C. 192 = 200 x 0.8 x 1.2 applies 20 per cent as the rise, which is wrong because the rise is 25 per cent.
- D. 210 adds the percentages (-20 + 25 = +5 per cent) instead of compounding them.
- Trap: Adding percentage changes, or treating a fall and a rise of different percentages as cancelling on the same base.
- Shortcut: Multiply the factors: 0.8 x 1.25 = 1.00, so the price returns to 200.
- Time target: 75 seconds. Source: B §2 (DI); A §10 (trap 1: different bases).

**R3-Q47 — C.**

- A. Bilal has the highest simple average (80), but the weights are 40 and 60, giving 77.
- B. Chitra scores 70 under either weighting.
- C (key). Asha: 0.4 x 50 + 0.6 x 100 = 80, the highest final score. Correct.
- D. Dev scores 52 under the weights; the simple average is 50.
- Trap: Using a simple average instead of the stated 40-60 weights.
- Shortcut: Apply the weights to each candidate before comparing; the simple average is not the rule.
- Time target: 80 seconds. Source: B §2 (DI weighted values), §6.

**R3-Q48 — D.**

- A. +0.2 lakh reverses the direction: revenue per thousand units fell from 2.0 to 1.8 lakh.
- B. +15 lakh is the increase in total revenue, not per-unit revenue.
- C. -15 lakh reverses the sign of the rise in total revenue; it is not a per-unit measure.
- D (key). Year 1: 120/60 = 2.0 lakh per thousand units; Year 2: 135/75 = 1.8. Change = -0.2 lakh. Correct.
- Trap: Reading total revenue growth as per-unit revenue change; output rose while revenue per unit fell.
- Shortcut: Divide each year's revenue by its output before subtracting.
- Time target: 80 seconds. Source: B §5 Example M (dual-axis reading); A §10.

**R3-Q49 — A.**

- A (key). Revenue fell (500 to 450) and the share rose from 40 to 50 per cent, a 10-point rise. Correct.
- B. X's revenue fell from 500 to 450, so this is false.
- C. The relative rise in share is (50 - 40)/40 = 25 per cent, not 10 per cent.
- D. Total revenue fell from 1250 to 900.
- Trap: Reading a share rise as a rise in revenue, or quoting a point change as a percent change.
- Shortcut: Name the measure first: revenue level, share in points, or relative share change.
- Time target: 90 seconds. Source: B §5 Example M, §6 (DI labels); A §10 (trap 2).

**R3-Q50 — B.**

- A. 33.3 per cent uses 2023 (90) as the base, which is not the starting year of the comparison.
- B (key). (120 - 100)/100 = 20 per cent. Correct.
- C. 50 per cent uses 2021 (80) as the base, a period outside the comparison.
- D. -20 per cent reverses the subtraction and divides by the end value.
- Trap: Using a convenient base year instead of the starting year of the comparison.
- Shortcut: Base is the earlier of the two named years: (end - start)/start.
- Time target: 70 seconds. Source: B §7 (DI base); A §10.

**R3-Q51 — C.**

- A. 10 doubles the correct gap, which is a scaling slip.
- B. 15 = 140 - 125 takes the third value in the unsorted list as if it were the median.
- C (key). Sorted: 90, 120, 140, 150. Median = (120 + 140)/2 = 130; mean = 500/4 = 125; difference 5. Correct.
- D. 25 = 150 - 125 takes the largest value as the median.
- Trap: Reading the median from the unsorted list, or taking the mean of the middle pair incorrectly.
- Shortcut: Sort first; the median is the mean of the two middle values; then subtract the mean.
- Time target: 80 seconds. Source: B §2 (DI reading); median/mean is elementary arithmetic outside the owner.

**R3-Q52 — D.**

- A. 1260 results from using 120 degrees for the sector (420 x 360/120), a misreading of the angle.
- B. 1680 results from using 90 degrees for the sector (420 x 360/90), a misreading of the angle.
- C. 2100 results from using 72 degrees for the sector (420 x 360/72), a misreading of the angle.
- D (key). 420 x 360/84 = 1800. Correct.
- Trap: Reading the sector angle wrongly, or multiplying instead of dividing by the angle fraction.
- Shortcut: Full pie = 360 degrees; scale the sector value by 360/84.
- Time target: 75 seconds. Source: B §5 Example M (pie/share).

**R3-Q53 — A.**

- A (key). PLANT has one vowel, A. Fix A first, then choose 2 letters in order from the remaining 4: 4 x 3 = 12. Correct.
- B. 20 = 5 x 4 ignores the third position.
- C. 24 = 4 x 3 x 2 counts arrangements of consonants only, which the stem does not allow.
- D. 60 = 5 x 4 x 3 is the total without the vowel restriction.
- Trap: Forgetting that a restriction on the first position must be applied before the others.
- Shortcut: Vowel first: A is the only choice, then P(4,2) = 12.
- Time target: 75 seconds. Source: B §4 (permutations), §5 Example K, §7.

**R3-Q54 — B.**

- A. 2 km is the difference of the two legs, which is not a distance between perpendicular points.
- B (key). The legs are perpendicular: sqrt(6^2 + 8^2) = 10 km. Correct.
- C. 7 km is the average of the two legs, which has no geometric meaning here.
- D. 14 km is the total path length, not the straight-line distance.
- Trap: Adding path lengths instead of applying Pythagoras to perpendicular displacements.
- Shortcut: Perpendicular legs: use 6-8-10, the common triple.
- Time target: 60 seconds. Source: B §2 (directions); Pythagoras is elementary geometry outside the owner.

**R3-Q55 — C.**

- A. Q is eligible, but its interview score of 50 is below 60, so Q is not shortlisted.
- B. Q fails rule 2 (interview 50 is below 60), so Q cannot be shortlisted.
- C (key). P is eligible (70) with interview 60, meeting rule 2; R is eligible (65) with interview 75. Correct.
- D. S is rejected by rule 3 (interview 40), even though its written score is high.
- Trap: Applying the eligibility rule without the interview threshold, or ignoring rule 3 for a high written score.
- Shortcut: Apply rule 3 first (rejections), then rule 1 and rule 2 to the survivors.
- Time target: 100 seconds. Source: B §3 (method, item 4), closure route item 11; A §4.

**R3-Q56 — C.**

- A. 12 ignores rules (a) to (d): P and Q can take a consecutive pair of days in 6 ordered placements, and R and S fill the other two days in 2 ways, giving 12.
- B. 9 is the number of ways to give each person a day other than the forbidden one (rules a to d); it ignores rule (e).
- C (key). Of the 9 assignments that satisfy rules (a) to (d), exactly 6 give P and Q consecutive days. Correct.
- D. 3 is the complement: the assignments where P and Q are not on consecutive days. This reverses rule (e).
- Trap: reading 'consecutive' as 'not consecutive', or dropping the forbidden-day rules and counting every consecutive placement.
- Shortcut: Count the 9 derangements of four staff (rules a to d), then keep those where P and Q are adjacent in the day sequence.
- Time target: 90 seconds. Source: owner assignment route with forbidden placements (`../COVERAGE.md` row 28); permutations with restrictions (row 13).

**R3-Q57 — B.**

- A. If X tells the truth, then Y lies, so Z tells the truth (Y's claim that Z lies is false). Z's claim that X and Y are both truthful is then false because Y lies. Contradiction.
- B (key). X lies, so Y tells the truth. Y's claim makes Z a liar. Z's claim (that X and Y are both truthful) is false because X lies, which is consistent. Only Y tells the truth. Correct.
- C. If Z tells the truth, then X and Y are both truthful. But a truthful X means Y lies, which contradicts Y being truthful. Contradiction.
- D. If X tells the truth, Y lies. If Z tells the truth, X and Y are both truthful, so Y would be truthful. Y cannot both lie and be truthful. Contradiction.
- Trap: accepting a statement's plausibility without testing each truth-teller hypothesis as a full assignment.
- Shortcut: Test each single truth-teller and propagate the claims; only one hypothesis survives.
- Time target: 60 seconds. Source: owner truth-teller and knight-knave route (`../COVERAGE.md` row 27).

**R3-Q58 — B.**

- A. 16 = 2n, which is not the diagonal formula.
- B (key). n(n - 3)/2 = 8 x 5/2 = 20. Correct.
- C. 24 = 8 x 3 counts one-off products instead of pairs.
- D. 28 = C(8,2) counts all vertex pairs, including the eight sides.
- Trap: Using C(n,2) for diagonals, which also counts the sides.
- Shortcut: Each vertex has n - 3 diagonals; halve the product: 8 x 5/2.
- Time target: 45 seconds. Source: A §2 (polygon diagonals).

**R3-Q59 — C.**

- A. 10 is the number of multiples of 21 in the range, which are the excluded ones.
- B. 20 = 28 - 8 subtracts the wrong count of multiples of 21.
- C (key). Multiples of 7 from 100 to 300: 28; multiples of 21: 10; 28 - 10 = 18. Correct.
- D. 28 counts all multiples of 7 and ignores the exclusion.
- Trap: Excluding multiples of 3 by counting multiples of 3 rather than multiples of 21.
- Shortcut: Multiples of 7 minus multiples of 21.
- Time target: 60 seconds. Source: B §4 (counting), A §2 (inclusion–exclusion).

**R3-Q60 — D.**

- A. 12 = 3 x 2 x 2 forgets the arrangements of the three middle letters.
- B. 24 = 4! ignores the consonant-vowel condition.
- C. 48 uses 4 choices for the first letter, but only 3 consonants are available.
- D (key). Start: 3 consonants (T, R, N); end: 2 vowels (A, I); middle three letters in 3! = 6 ways: 3 x 2 x 6 = 36. Correct.
- Trap: Filling the middle positions before fixing the first and last letters, or forgetting the middle arrangements.
- Shortcut: Fix the two end letters first (3 then 2), then arrange the middle three (3!).
- Time target: 60 seconds. Source: B §4 (arrangements), §5 Example K.

**R3-Q61 — A.**

- A (key). 9 x 8 x 7 = 504: 9 choices for president, 8 for vice-president, 7 for treasurer. Correct.
- B. 252 = C(9,2) x 7 treats the president and vice-president as an unordered pair, but the posts are distinct.
- C. 336 = 8 x 7 x 6 excludes the president from the choices for the later posts, an error in the sequence.
- D. 648 = 9 x 8 x 9 lets the treasurer be chosen from all nine members, including those already in post.
- Trap: Treating distinct posts as an unordered group, or allowing one person to hold two posts.
- Shortcut: Distinct posts: multiply the shrinking pool, 9 x 8 x 7.
- Time target: 60 seconds. Source: B §4 (permutations), §9 item 8.

**R3-Q62 — B.**

- A. 3 is possible if the first three balls are one of each colour; that case has no repeat.
- B (key). Worst case: one of each colour (3 balls, no pair), then any fourth ball repeats a colour: 4. Correct.
- C. 5 adds a fourth colour that is not in the box.
- D. 6 corresponds to two balls of each colour, which guarantees a triple, not merely a pair.
- Trap: Using the worst-case count for a stronger condition (a triple) or for a non-existent fourth colour.
- Shortcut: Worst case = number of colours; add one.
- Time target: 50 seconds. Source: B §5 Example N (worst case), §9 item 14.

