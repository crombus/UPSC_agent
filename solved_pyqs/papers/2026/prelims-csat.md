# UPSC Civil Services (Preliminary) Examination 2026 — CSAT Paper II, Set A

> **Key status:** **PROVISIONAL** throughout. The answer letters come from the locally held scan headed `CS (P) Exam 2026 [Prov. Ans. Key]`, Set A.  
> **Question source:** Official Set-A paper `books/prelima_question_paper_answers/2026-GS2-CSAT-Set A.pdf`, checked against `knowledge-export/CSAT PYQ/2026-GS2-CSAT-Set A.md` and the direct English-page exports.  
> **Routing source:** `upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2026.md`.  
> **Canonical owners:** CSAT Basic modules 01–06; Q72–Q77 additionally carry the Topic-07 communication-content overlay.  
> **Catalogue:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

## Shared directions for Q1–Q5

Each item contains a question followed by two statements. Choose:

- **(a)** Select this option if the question can be answered using one of these statements alone, but cannot be answered using other statement.
- **(b)** Select this option if the question can be answered using either statement alone.
- **(c)** Select this option if the question can be answered using both the statements together, but cannot be answered using either statement alone.
- **(d)** Select this option if the question cannot be answered even using any of the statements.

---

<a id="2026-prelims-csat-q01"></a>
## Q1. Coin denomination
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities/Data Sufficiency → Data sufficiency → finite-case enumeration · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

**Question:** X receives three coins of different denominations: 1, 2, 5, 10 and 20. If the total amount received by X is \(m\), does X receive a coin of denomination 5?  
**Statement I:** \(m\) is not a prime number.  
**Statement II:** The sum of the digits of \(m\) is greater than 5.

**Metadata:** Family 05 · Algebra/Inequalities/Data Sufficiency → Data sufficiency → finite-case enumeration · Proposed slug: `coin-denomination-data-sufficiency`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (a).**

**Reasoning:** The ten possible triples give totals \(8,13,23,16,26,31,17,27,32,35\). Statement I permits both triples containing 5 (for example \(1,2,5\to8\)) and not containing 5 (\(2,10,20\to32\)); it is insufficient. Under Statement II, the qualifying totals are \(8,16,26,17,27,35\), and every corresponding triple contains 5. Statement II alone is sufficient.  
**Shortest safe method:** list the ten triples once and mark “contains 5 / does not contain 5.”  
**Assumption:** exactly one coin is selected from each listed denomination; the three denominations are distinct.  
**Option check:** (b), (c) and (d) incorrectly treat Statement I as sufficient or Statement II as insufficient.

---

<a id="2026-prelims-csat-q02"></a>
## Q2. Comparing two distinct real numbers
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities/Data Sufficiency → Inequalities → counterexample testing · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

**Question:** For two distinct real numbers \(x\) and \(y\), which of them is bigger?  
**Statement I:** \(x^2<y<1\).  
**Statement II:** \(y<\sqrt{x}<1\).

**Metadata:** Family 05 · Algebra/Inequalities/Data Sufficiency → Inequalities → counterexample testing · Proposed slug: `compare-reals-data-sufficiency`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (d).**

**Reasoning:** I alone allows \(x=-1/2,y=1/2\) (\(y>x\)) and \(x=0.8,y=0.7\) (\(x>y\)). II alone also allows either order: \(x=0.25,y=0.1\) gives \(x>y\), while \(x=0.25,y=0.4\) gives \(y>x\). Both together remain ambiguous: \(x=0.25,y=0.4\) and \(x=0.8,y=0.7\) satisfy both but reverse the order.  
**Shortest safe method:** seek two valid counterexamples with opposite answers.  
**Assumption:** \(\sqrt{x}\) is the principal real square root.

---

<a id="2026-prelims-csat-q03"></a>
## Q3. Parity of \(x\)
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities/Data Sufficiency → Parity → combined sufficiency · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

**Question:** If \(x\) and \(y\) are integers, then is \(x\) even?  
**Statement I:** \(x^2y^2\) is even.  
**Statement II:** \(1+x^2+y^2\) is odd.

**Metadata:** Family 05 · Algebra/Inequalities/Data Sufficiency → Parity → combined sufficiency · Proposed slug: `parity-data-sufficiency`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (c).**

**Reasoning:** I says at least one of \(x,y\) is even, but not which. II says \(x^2+y^2\) is even, so \(x,y\) have the same parity. Together they must both be even; therefore \(x\) is even. Neither statement alone settles \(x\).  
**Shortest safe method:** square preserves parity; translate each statement into parity language.

---

<a id="2026-prelims-csat-q04"></a>
## Q4. Odd/even set membership
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities/Data Sufficiency → Set-membership logic → parity · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

**Question:** X is a collection of certain odd numbers whereas Y is a collection of certain even numbers. T consists of the numbers all of which are either from X or from Y. Is every number of T from Y?  
**Statement I:** The sum of any two numbers belonging to T is even.  
**Statement II:** If both \(p\) and \(q\) are picked from T, then \((p-1)q\) is even.

**Metadata:** Family 05 · Algebra/Inequalities/Data Sufficiency → Set-membership logic → parity · Proposed slug: `set-membership-parity-data-sufficiency`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (d).**

**Reasoning:** I only forces all members of T to have the same parity; T may be all odd or all even. II is true for an all-odd T because \(p-1\) is even, and for an all-even T because \(q\) is even. Even together, the statements do not decide whether T is drawn wholly from Y.  
**Shortest safe method:** test the two models “T all odd” and “T all even.”

---

<a id="2026-prelims-csat-q05"></a>
## Q5. Is \(x\) prime?
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities/Data Sufficiency → Factorisation → primality · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

**Question:** If \(x\), \(y\) and \(z\) are integers, each greater than 1, then is \(x\) a prime number?  
**Statement I:** \(xy^2=116\).  
**Statement II:** \(xz=261\).

**Metadata:** Family 05 · Algebra/Inequalities/Data Sufficiency → Factorisation → primality · Proposed slug: `prime-determination-data-sufficiency`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (a).**

**Reasoning:** \(116=2^2\cdot29\). Since \(y>1\) and \(y^2\mid116\), necessarily \(y=2,x=29\), so I alone proves prime. From \(261=3^2\cdot29\), II permits \(x=3,z=87\) and \(x=9,z=29\); it is insufficient.  
**Shortest safe method:** factor both constants and inspect allowable divisors.

---

## Shared passage for Q6–Q7

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

“Kalagram”, the cultural village set up at the Maha Kumbh Mela, unfolded as a mosaic of India’s diverse regions, each represented by seven meticulously crafted “Sanskriti Angans”—stepping through the grand portal was like entering another world. These thematic zones, inspired by iconic temples like the Dakshineshwar Kali Temple and the Brahma Mandir, were treasure troves of regional artistry. Bengal’s Pattachitra paintings, Assam’s bamboo crafts, Tamil Nadu’s Thanjavur paintings, and Madhya Pradesh’s tribal sculpture—all were showcased in these living galleries where 230 master artisans breathed life into them using age-old techniques, their hands shaping India’s ancient history into creations to behold.

<a id="2026-prelims-csat-q06"></a>
## Q6. Conclusions from the Kalagram passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Conclusions → scope control · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions are valid?

1. Seven Sanskriti Angans, representing different regions of India, had been showcased in Kalagram.
2. Regional artistry was recognised via the inspiration drawn from iconic temples.
3. India’s ancient history had been crafted by the contemporary craftsmanship of 230 artisans into creations to behold.
4. Art forms from all regions of India had been showcased in these living galleries.

**Options:** (a) 1 and 2 only · (b) 2, 3 and 4 · (c) 1, 2 and 4 · (d) 1 and 3

**Metadata:** Family 01 · Reading Comprehension → Conclusions → scope control · Proposed slug: `kalagram-passage-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (a).**

**Passage-only justification:** 1 is stated through the seven Angans representing diverse regions. 2 follows from the thematic zones being inspired by iconic temples and showcasing regional artistry. 3 turns a figurative phrase about artisans’ hands into a literal historical claim. 4 overreaches from named examples and “diverse regions” to **all** regions.  
**Competing options:** (b) and (c) retain unsupported 4; (d) retains the over-literal 3 and drops supported 2.  
**Ambiguity flag:** the opening syntax is awkward (“each represented by seven”), but the provisional key reads it as seven Angans collectively representing regions.

---

<a id="2026-prelims-csat-q07"></a>
## Q7. Incorrect statement from the Kalagram passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Incorrect statement → literal verification · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which one of the following statements is not correct?

**Options:**  
(a) Paintings from four States of India have been mentioned.  
(b) Stepping into Kalagram is likened to stepping into another world.  
(c) The Angans have been described as living galleries.  
(d) Kalagram is divided into thematic zones, inspired by well-known temples of India.

**Metadata:** Family 01 · Reading Comprehension → Incorrect statement → literal verification · Proposed slug: `kalagram-passage-incorrect-statement`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (a).**

**Passage-only justification:** Only Bengal’s Pattachitra and Tamil Nadu’s Thanjavur items are paintings; Assam contributes bamboo crafts and Madhya Pradesh tribal sculpture. Options (b)–(d) closely reproduce the passage.

---

<a id="2026-prelims-csat-q08"></a>
## Q8. Weight equations
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra → Simultaneous equations → comparison · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

The weight of X, in kg, is denoted by X. The weights of A, B, C, D, P, Q, R and S are measured. Given:

\[
A+B+C+D=17,\quad A+C=6,
\]
\[
P+Q+S+D=15,\quad P+Q+R+B=17,\quad P=R\text{ and }Q=S.
\]

Which one of the following statements is correct?

(a) B and D together weigh less than the total weight of P and Q.  
(b) P and Q together weigh more than the total weight of A and C.  
(c) P weighs more than Q.  
(d) Q weighs more than P.

**Metadata:** Family 05 · Algebra → Simultaneous equations → comparison · Proposed slug: `weight-equations-comparison`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (b).**

**Reasoning:** From the first pair, \(B+D=11\). With \(R=P,S=Q\), the other equations give \(P+2Q+D=15\) and \(2P+Q+B=17\). Adding: \(3(P+Q)+(B+D)=32\), so \(P+Q=7\). Since \(A+C=6\), option (b) follows. Nothing fixes the order of P and Q.  
**Shortest safe method:** add the two P–Q equations, then substitute \(B+D\).

---

<a id="2026-prelims-csat-q09"></a>
## Q9. QUEUE arrangements
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning/Counting → Permutations → block method · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

How many words can one form by shuffling the letters of the word QUEUE, if Q is always followed by U? The words thus formed need not necessarily have any meaning.

**Options:** (a) 6 · (b) 8 · (c) 10 · (d) 12

**Metadata:** Family 06 · Logical Reasoning/Counting → Permutations → block method · Proposed slug: `queue-constrained-permutations`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Treat QU as one block. Arrange \(\{QU,U,E,E\}\): \(4!/2!=12\).  
**Shortest safe method:** mandatory adjacency ⇒ block; divide for repeated E.

---

<a id="2026-prelims-csat-q10"></a>
## Q10. Common landing marks
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → LCM → counting terms in a range · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

X, Y and Z jump forward 4′, 6′ and 5′, respectively. At 8 AM, they all land on mark 199′. How many times will they all land on the same mark (need not be at the same moment) between mark 195′ and 1000′, if all of them cross mark 1000′ by 9 AM?

**Options:** (a) 11 · (b) 12 · (c) 13 · (d) 14

**Metadata:** Family 02 · Number Systems → LCM → counting terms in a range · Proposed slug: `common-jump-marks-lcm`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Common marks recur every \(\operatorname{LCM}(4,6,5)=60\) ft: \(199+60k\). For \(199+60k\le1000\), \(k=0,\ldots,13\), giving 14 marks.  
**Shortest safe method:** LCM, then floor count.  
**Assumption:** “between” includes the stated common mark 199; neither boundary 195 nor 1000 is common.

---

## Shared passage for Q11–Q12

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

Sport is not just about winning medals or getting jobs through a sports quota. Today’s generation is struggling with issues like depression and anxiety. Parents often say that their children are inactive and rarely leave the house. Sport can help tackle these problems. From sport you can learn time management, fitness, teamwork, coordination, and so much more. We need to develop a culture in which sport is seen as a way of life—a path to building a healthier, happier society.

<a id="2026-prelims-csat-q11"></a>
## Q11. Conclusions from the sport passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Conclusions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions are valid?

1. Sport is more than just games; it is a way of life.
2. Sport can help mitigate the problems of seclusion among the young.
3. Earning laurels in sport can help one secure a job on the basis of an assigned quota.
4. Standard corporate sector skills cannot be learnt through sport.

**Options:** (a) 1 and 3 only · (b) 2 and 4 only · (c) 1, 2 and 4 · (d) 1, 2 and 3

**Metadata:** Family 01 · Reading Comprehension → Conclusions · Proposed slug: `sport-way-of-life-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (d).**

**Passage-only justification:** 1 restates the closing recommendation. 2 follows from sport addressing inactivity and rarely leaving home. 3 is acknowledged in the opening, though the author says sport is **not just** about that. 4 contradicts the listed transferable skills such as teamwork and time management. Other options either include 4 or omit supported claims.

---

<a id="2026-prelims-csat-q12"></a>
## Q12. Statements from the sport passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. Parents are not encouraging enough when it comes to children playing sport.
2. Participation in sporting activities can help develop life skills.
3. Sport as a way of life can help evolve the very nature of society itself.

**Options:** (a) 1 and 3 · (b) 2 and 3 · (c) 2 only · (d) 3 only

**Metadata:** Family 01 · Reading Comprehension → Statements · Proposed slug: `sport-life-skills-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (b).**

**Passage-only justification:** 2 is explicit in the skills list; 3 follows from the envisaged healthier, happier society. The passage reports parents’ concern about inactivity, not lack of encouragement, so 1 is unsupported.

---

<a id="2026-prelims-csat-q13"></a>
## Q13. Forward and backward jumps
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Rates/Motion/Time/Geometry → Displacement → linear equations · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A toy T jumps forward or backward. In each forward jump, it moves 5′ forward whereas in each backward jump, it moves 2′ backward. If in 31 jumps, T moves exactly 15′ forward, then what is the difference of the number of forward and backward jumps?

**Options:** (a) 6 · (b) 7 · (c) 8 · (d) 9

**Metadata:** Family 04 · Rates/Motion/Time/Geometry → Displacement → linear equations · Proposed slug: `forward-backward-jumps`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Let forward and backward counts be \(f,b\). Then \(f+b=31\), \(5f-2b=15\). Substitution gives \(7f=77\), so \(f=11,b=20\), difference \(9\).  
**Shortest safe method:** add twice the count equation to the displacement equation.

---

<a id="2026-prelims-csat-q14"></a>
## Q14. Circular seating
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Circular seating → adjacency constraints · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Eight persons P, Q, R, S, T, U, V and W sit around a round table in eight different seats placed with equal distance between any two consecutive seats. Both P and R are adjacent to Q. Both T and R are adjacent to S. Both U and W are adjacent to V. S and W are on opposite chairs. If while going in the clockwise direction around the table from P, one meets R before T, then how many persons shall Q cross while moving in the clockwise direction around the table before meeting W?

**Options:** (a) 5 · (b) 4 · (c) 2 · (d) 1

**Metadata:** Family 06 · Logical Reasoning → Circular seating → adjacency constraints · Proposed slug: `circular-seating-adjacency`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Fix Q to remove rotational symmetry. Its neighbours must be P and R. Since R also neighbours S, the forced chain is \(P-Q-R-S-T\). W is opposite S; V must sit between U and W. The clockwise-order condition selects the mirror in which Q passes five persons before W.  
**Shortest safe method:** build the forced adjacency chain first, place the opposite pair next, and use the final direction condition only to choose the mirror.

---

<a id="2026-prelims-csat-q15"></a>
## Q15. Painted table-top patterns
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Counting/Spatial reasoning → Placements → symmetry on a fixed rectangle · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

The top of a table is rectangular and its dimensions are 6′ × 10′. Two rectangular portions of the table top are painted in blue colour; both these portions have dimensions 2.5′ × 8′ and each of them has exactly two sides common with two edges of the table top. If the table is fixed to the ground and the remaining portion of the table top is painted in white, how many different patterns are possible when observed from above?

**Options:** (a) 2 · (b) 4 · (c) 6 · (d) 8

**Metadata:** Family 06 · Counting/Spatial reasoning → Placements → symmetry on a fixed rectangle · Proposed slug: `painted-table-pattern-count`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Each blue rectangle must occupy a corner with its 8-ft side along a 10-ft edge and its 2.5-ft side along a 6-ft edge. Enumerating the two-corner placements and identifying identical unions on the fixed table yields four patterns.  
**Shortest safe method:** sketch the four corner placements and compare the union, not the order in which the two identical blue rectangles are chosen.  
**Assumption:** overlapping blue portions do not create a new colour.

---

## Shared passage for Q16–Q17

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

How is deflation done? Most countries use a method called “double deflation”, where input and output prices are deflated separately. Consider a manufacturer importing oil for use in production. If oil prices fall, output prices do not and quantities remain the same, real value added should not change. But if the same deflator is used for inputs and outputs, as in India, it would look as if the manufacturer had become more productive.

<a id="2026-prelims-csat-q16"></a>
## Q16. Statements on double deflation
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements → exact-term fidelity · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. Real value should not change in the instance of static output cost and unchanged quantities against falling oil prices.
2. Deflators are to be used separately for inputs and outputs, and this is a practice universally adopted by all economies.

**Options:** (a) 1 only · (b) 2 only · (c) Both 1 and 2 · (d) Neither 1 nor 2

**Metadata:** Family 01 · Reading Comprehension → Statements → exact-term fidelity · Proposed slug: `double-deflation-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (d).**

**Passage-only justification:** The passage says **real value added**, not undifferentiated “real value”; statement 1 drops the decisive term. Statement 2 changes “most countries” into “universally adopted by all economies,” directly contradicted by India’s stated practice.  
**Ambiguity flag:** statement 1 is close in ordinary language, but the provisional key treats the omission of “added” as material.

---

<a id="2026-prelims-csat-q17"></a>
## Q17. Assumptions on deflation
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Assumptions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following assumptions is/are valid?

1. Deflation strategies can be used to make manufacturers appear to be doing better than they actually are.
2. When input and output prices are both deflated against a single input price, it is referred to as “double deflation”.

**Options:** (a) 1 only · (b) 2 only · (c) Both 1 and 2 · (d) Neither 1 nor 2

**Metadata:** Family 01 · Reading Comprehension → Assumptions · Proposed slug: `double-deflation-assumptions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (a).**

**Passage-only justification:** 1 is the implication of the manufacturer appearing more productive under a common deflator. 2 reverses the definition: double deflation uses separate input and output deflators.

---

<a id="2026-prelims-csat-q18"></a>
## Q18. Repeated a–b pattern
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems/Sequences → Repeating pattern → positional decoding · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A pattern formed by characters \(a\) and \(b\) is repeated more than once in:

`× b × a × a × × a × a × b a b`

What is × × in the 7th and 8th positions from the left in the above string?

**Options:** (a) aa · (b) ab · (c) ba · (d) bb

**Metadata:** Family 02 · Number Systems/Sequences → Repeating pattern → positional decoding · Proposed slug: `repeated-string-position`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Testing the only possible character substitutions, \(×=b\) produces the repeated a–b structure required by the stem; positions 7 and 8 are therefore \(bb\).  
**Shortest safe method:** write indices above the string and test \(×=a\), then \(×=b\).  
**Ambiguity flag:** the scan uses a multiplication-like mark; it is a blank symbol, not multiplication.

---

<a id="2026-prelims-csat-q19"></a>
## Q19. Exponent factorisation
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Prime exponents → trailing tens · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

If
\[
10^m\times1000\times n=75^{25}\times25^{32}\times32^{75},
\]
where \(n\) is not divisible by 10, then the value of \(m\) is

**Options:** (a) 101 · (b) 111 · (c) 121 · (d) 131

**Metadata:** Family 02 · Number Systems → Prime exponents → trailing tens · Proposed slug: `exponent-factorisation-trailing-tens`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (b).**

**Reasoning:** RHS has \(2^{375}\) and \(5^{2(25)+2(32)}=5^{114}\), hence \(10^{114}\) can be extracted while the residue is not divisible by 10. Since \(1000=10^3\), \(m+3=114\), so \(m=111\).  
**Shortest safe method:** count only the smaller of the total powers of 2 and 5, then subtract 3.

---

<a id="2026-prelims-csat-q20"></a>
## Q20. Train crossing a person
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Rates/Motion/Time → Relative speed → crossing · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

The speed of a train T is 100 km per hour and the speed of a person P is 4 km per hour. T crosses P in 15 seconds, if P travels along the direction of motion of T. If P travels along the opposite direction of T, then in how much time does T cross P, in seconds, approximately?

**Options:** (a) 13.51 · (b) 13.65 · (c) 13.85 · (d) 14.05

**Metadata:** Family 04 · Rates/Motion/Time → Relative speed → crossing · Proposed slug: `train-person-relative-speed`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (c).**

**Reasoning:** Same-direction relative speed \(=96\) km/h, so train length \(=96(5/18)\times15=400\) m. Opposite-direction speed \(=104\) km/h \(=260/9\) m/s. Time \(=400/(260/9)=13.846\) s.  
**Shortest safe method:** time ratio \(t_2/t_1=(100-4)/(100+4)=96/104\); \(t_2=15(96/104)=13.85\) s.

---

<a id="2026-prelims-csat-q21"></a>
## Q21. Inequalities in \(1/3<x<y<2\)
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities → Monotonicity → interval testing · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

For \(\frac13<x<y<2\), which of the following statements is/are always correct?

I. \(x+\frac1x<y+\frac1y\)  
II. \(\frac{\sqrt{1+y^2}}{y}<\frac{\sqrt{1+x^2}}{x}\)

**Options:** (a) I only · (b) II only · (c) Both I and II · (d) Neither I nor II

**Metadata:** Family 05 · Algebra/Inequalities → Monotonicity → interval testing · Proposed slug: `unit-interval-inequality-functions`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (b).**

**Reasoning:** \(f(t)=t+1/t\) decreases on \((0,1)\) and increases on \((1,\infty)\), so I is not always true across the stated interval. But \(g(t)=\sqrt{1+t^2}/t=\sqrt{1+1/t^2}\) strictly decreases for \(t>0\); hence \(x<y\Rightarrow g(y)<g(x)\).  
**Shortest safe method:** rewrite II as \(\sqrt{1+1/t^2}\); disprove I with \(x,y<1\).

---

<a id="2026-prelims-csat-q22"></a>
## Q22. Measuring 298 litres
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Integer combinations → optimisation · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

What is the minimum number of times one needs to measure to get 298 litres of water from a tank, if the measuring cylinders have capacities 1 litre, 6 litres, 25 litres and 100 litres?

**Options:** (a) 4 · (b) 5 · (c) 9 · (d) 13

**Metadata:** Family 02 · Number Systems → Integer combinations → optimisation · Proposed slug: `measure-298-litres`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Measure \(100\) litres three times to get 300, then measure out 1 litre twice: five measurements. Four cannot work because no signed combination of four available capacities totals 298.  
**Shortest safe method:** target is \(300-2\), immediately suggesting \(3\times100-2\times1\).  
**Assumption:** measuring out/removing water counts as a measurement and signed use of a cylinder is permitted.

---

<a id="2026-prelims-csat-q23"></a>
## Q23. Ways to measure 20 kg
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Counting → Non-negative integer solutions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

There are four types of weights, namely 1 kg, 2 kg, 5 kg and 10 kg. What is the maximum number of different ways one can measure 20 kg, if at least eight but not more than eleven weights of 1 kg are to be used while measuring?

**Options:** (a) 7 · (b) 8 · (c) 9 · (d) 10

**Metadata:** Family 06 · Counting → Non-negative integer solutions · Proposed slug: `twenty-kilogram-weight-combinations`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Solve \(a+2b+5c+10d=20\) for \(a=8,9,10,11\). Counts are 3, 1, 3 and 1 respectively, totalling 8.  
**Shortest safe method:** fix the constrained 1-kg count and solve the small residual by inspection.  
**Assumption:** weights of each type are available in sufficient quantity.

---

<a id="2026-prelims-csat-q24"></a>
## Q24. Cuts of an unmoved cube
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Geometry → Plane cuts → piece-count bounds · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A cut on a solid object divides the object into two parts where the new surfaces thus produced are plane. On the other hand, one single cut can be used to cut more than one object at a time. In an experiment, the total number of pieces produced by applying \(n\) cuts is denoted by \(x_n\). The experiment is performed on a solid cube where pieces remain unmoved after each cut. In this experiment, if after the third cut, the pieces are identical, then which of the following is not a possible value for \(x_4\)?

**Options:** (a) 16 · (b) 12 · (c) 8 · (d) 5

**Metadata:** Family 04 · Geometry → Plane cuts → piece-count bounds · Proposed slug: `cube-fourth-cut-piece-count`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Three cuts can leave four identical slabs or eight identical sub-cubes. A fourth plane can produce 5 or 8 pieces from four slabs, or 12 from eight cubes by cutting four aligned cubes. It cannot double eight unmoved sub-cubes to 16 because one plane cannot intersect all eight separated cube cells.  
**Shortest safe method:** enumerate the identical-piece configurations after three cuts and count how many existing pieces one new plane can intersect.

---

<a id="2026-prelims-csat-q25"></a>
## Q25. Correcting a class average
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic/Commercial Math → Averages → correction of totals · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

The class average \(x\) in a test increases by 4 when the score of a student is rectified, whose corrected score is 100 instead of 0. Later, the score of another student was found to have been recorded as 81 in place of 56. If there are no other corrections and the final corrected average is \(y\), then \(y-x\) is

**Options:** (a) 2 · (b) 3 · (c) 5 · (d) 6

**Metadata:** Family 03 · Arithmetic/Commercial Math → Averages → correction of totals · Proposed slug: `class-average-corrections`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (b).**

**Reasoning:** A 100-point correction raises average by 4, so class size is \(100/4=25\). The second correction reduces total by 25, hence average by 1. Net change from original \(x\) is \(4-1=3\).  
**Shortest safe method:** correction ÷ average change gives class size.

---

## Shared passage for Q26–Q28

**Directions for the next 3 (three) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

When SARS-CoV-2 was first detected in 2019, it was a truly novel virus for the world. At that time, no one in the world had been exposed to SARS-CoV-2 or had specific immunity against it. In contrast, people across the world have been exposed to HMPV for decades and the virus is well-studied. HMPV and SARS-CoV-2 belong to two very different virus families with fundamentally different characteristics and epidemiology, with strong seasonality seen in HMPV, unlike SARS-CoV-2. Both viruses cause different severity of symptoms, particularly over the long term, and the affected population segments do not fully overlap. In general, HMPV causes milder illness with deaths being very rare and with no long-term post-viral symptoms.

<a id="2026-prelims-csat-q26"></a>
## Q26. Conclusions on HMPV and SARS-CoV-2
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Conclusions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions is/are valid?

1. Though SARS-CoV-2 and HMPV are similar viruses with somewhat different epidemiology, the former became a pandemic because it was novel and people had not been exposed to it.
2. The two viruses have fundamentally different impacts on human populations and should not therefore be dealt with in a similar manner.

**Options:** (a) 1 only · (b) 2 only · (c) Both 1 and 2 · (d) Neither 1 nor 2

**Metadata:** Family 01 · Reading Comprehension → Conclusions · Proposed slug: `hmpv-sars-cov2-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (b).**

**Passage-only justification:** 1 begins by calling the viruses similar, contrary to “two very different virus families.” 2 follows from their different characteristics, epidemiology, severity, long-term effects and affected groups.

---

<a id="2026-prelims-csat-q27"></a>
## Q27. Writer’s intent in the virus passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Writer’s intent · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following reflect the intent of the writer in the above passage?

1. To evolve methodologies for objective analysis of the two viruses.
2. To establish the epidemiological similarities and differences between the two viruses.
3. To offer a better understanding of HMPV remedies when analysed with SARS-CoV-2.

**Options:** (a) 1 and 2 · (b) 2 and 3 · (c) 1 and 3 · (d) None of the above

**Metadata:** Family 01 · Reading Comprehension → Writer’s intent · Proposed slug: `hmpv-sars-writer-intent`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (d).**

**Passage-only justification:** The author compares the viruses to prevent false equivalence. No methodology is developed, similarities are not the organising purpose, and remedies are not discussed. Each numbered intent adds an unsupported aim.

---

<a id="2026-prelims-csat-q28"></a>
## Q28. Inferences from the virus passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Inferences · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements reflect the logical and rational inferences that can be drawn from the passage?

1. HMPV has, historically, had longer documentation of studies when compared with SARS-CoV-2.
2. The two viruses are different from each other and this results in markedly different outcomes amongst those affected.
3. Long-term impacts of the two viruses are dissimilar and this is an important differentiator between them.
4. One of the common factors between the two viruses is seasonal specificity.

**Options:** (a) 1 and 2 only · (b) 1, 2 and 3 · (c) 3 and 4 · (d) 1 and 3 only

**Metadata:** Family 01 · Reading Comprehension → Inferences · Proposed slug: `hmpv-sars-inferences`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (b).**

**Passage-only justification:** 1 follows from HMPV’s decades of study versus SARS-CoV-2’s 2019 novelty. 2 and 3 restate explicit differences. 4 is false because strong seasonality is attributed to HMPV **unlike** SARS-CoV-2.

---

<a id="2026-prelims-csat-q29"></a>
## Q29. Extremes of \(xy+z\)
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Discrete optimisation · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Three variables \(x\), \(y\) and \(z\) take values 2, 3, 4 or 5 such that their values are always distinct. If M and N denote the largest possible value and the smallest possible value, respectively, for the expression \(\{(x\times y)+z\}\), then \(M-N\) is

**Options:** (a) 11 · (b) 12 · (c) 13 · (d) 14

**Metadata:** Family 02 · Number Systems → Discrete optimisation · Proposed slug: `distinct-values-expression-extrema`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (c).**

**Reasoning:** Maximum uses the two largest values in the product and the next value: \(5\cdot4+3=23\). Minimum uses the two smallest in the product and the next value: \(2\cdot3+4=10\). Difference \(=13\).  
**Shortest safe method:** because multiplication dominates, allocate extremes to \(xy\), then use the smallest available \(z\) for max and the smallest remaining \(z\) for min.

---

<a id="2026-prelims-csat-q30"></a>
## Q30. Direct and inverse proportion
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic → Proportion → combined direct/inverse relation · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Suppose \(x\), \(y\) and \(z\) are variables taking positive real numbers as their possible values. It is given that \(y\) is directly proportional to \(x^2\) and \(x\) is inversely proportional to \(z\). For \(z=7/25\), the values of \(x\) and \(y\) are 5 and 50, respectively. If \(y=98\), what is \(z\) equal to?

**Options:** (a) \(1/7\) · (b) \(1/5\) · (c) \(5/7\) · (d) 1

**Metadata:** Family 03 · Arithmetic → Proportion → combined direct/inverse relation · Proposed slug: `direct-inverse-proportion`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (b).**

**Reasoning:** \(y=kx^2\); \(50=25k\Rightarrow k=2\). Thus \(98=2x^2\Rightarrow x=7\). Also \(xz\) is constant: \(5(7/25)=7/5\). Hence \(z=(7/5)/7=1/5\).  
**Shortest safe method:** \(y\propto1/z^2\), so \(98/50=(z_1/z_2)^2\).

---

## Shared passage for Q31–Q32

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

India is starting to deploy AI for critical use cases such as weather forecasting, pest detection and control, and crop yield optimisation. However, penetration is limited to a small subset of tech-savvy farmers. In the US and in Europe, generative AI tools have started offering precision farming at scale, integrating large datasets to provide real-time agronomic insights. For at-scale integration and accessibility of AI tools in India, it would be helpful to develop Indian languages-based AI tools for smallholder farmers, partner with AgTechs to create affordable AI solutions, and disseminate AI-based advisory services through government programmes.

<a id="2026-prelims-csat-q31"></a>
## Q31. Assumptions in the agricultural-AI passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Assumptions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following assumptions is/are valid?

1. Agricultural productivity has marched ahead in the West because of the economies of scale facilitated by the adoption of AI tools.
2. Affordable AI tools rendered available in local languages can help AI-based solutions reach more and more small farmers.
3. Though penetration is as yet low, critical application areas deploying AI tools are already in use in India.

**Options:** (a) 1, 2 and 3 · (b) 2 only · (c) 1 and 3 only · (d) 2 and 3 only

**Metadata:** Family 01 · Reading Comprehension → Assumptions · Proposed slug: `agricultural-ai-assumptions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (d).**

**Passage-only justification:** 2 underlies the recommendation for affordable Indian-language tools; 3 is explicit. The passage says Western tools operate at scale, not that Western productivity advanced **because** of economies of scale, so 1 adds causation.

---

<a id="2026-prelims-csat-q32"></a>
## Q32. Incorrect statements in the agricultural-AI passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Incorrect statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are not correct?

1. Tech-savvy farmers will drive the AgTech companies of the future.
2. The development of advisory services by the government programmes for the use of AI tools in agriculture would be helpful.
3. In the US and Europe, AI tools have replaced traditional agricultural practices.
4. The integration of large datasets for use in real-time agronomic analysis is already a reality.

**Options:** (a) 1 and 3 only · (b) 1, 3 and 4 · (c) 2 and 4 · (d) 3 only

**Metadata:** Family 01 · Reading Comprehension → Incorrect statements · Proposed slug: `agricultural-ai-incorrect-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (a).**

**Passage-only justification:** 1 is speculative and absent; 3 exaggerates “started offering precision farming” into replacement. Statements 2 and 4 are directly supported.

---

<a id="2026-prelims-csat-q33"></a>
## Q33. Ranking five persons
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Ranking → conditional testing · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

P, Q, R, S and T are ranked 1 to 5 (not necessarily in that order). The rank of P is 4, the rank of Q is not 5, the rank of R is 1, the rank of S is not 2, the rank of T is not 3. Then which of the following is/are correct?

I. If the rank of S is 3, then that of T is 2.  
II. If the rank of Q is 3, then that of T is 5.

**Options:** (a) I only · (b) II only · (c) Both I and II · (d) Neither I nor II

**Metadata:** Family 06 · Logical Reasoning → Ranking → conditional testing · Proposed slug: `five-person-ranking-conditions`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (d).**

**Reasoning:** With P=4,R=1, remaining ranks are 2,3,5. If S=3, Q/T may be 2/5 in either allowed order, so I is not necessary. If Q=3, S/T may be 5/2 or 2/5 subject to S≠2, which actually forces S=5,T=2; thus II is false.  
**Shortest safe method:** reduce immediately to the three unused ranks.

---

<a id="2026-prelims-csat-q34"></a>
## Q34. Matching coloured rod segments
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Segment matching → constrained arrangements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Two identical straight rods are painted in five distinct colours so that each of them gets divided into five equal parts along the length. In one of them, the portions are marked P1, P2, P3, P4 and P5 (not necessarily in that order) whereas in the other, they are marked Q1, Q2, Q3, Q4 and Q5 (not necessarily in that order). When the rods are kept parallel to each other side by side, P1 and Q3 match, P4 matches Q1 or Q2, and Q4 matches P3 or P5. If Q3 and Q5 are adjacent, which of the following is/are possible?

I. Q3 is marked at the middle portion of the straight rod.  
II. P2 is marked at one of the extreme portions of the straight rod.

**Options:** (a) I only · (b) II only · (c) Both I and II · (d) Neither I nor II

**Metadata:** Family 06 · Logical Reasoning → Segment matching → constrained arrangements · Proposed slug: `coloured-rod-segment-matching`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (c).**

**Reasoning:** A short arrangement enumeration satisfying the three colour correspondences and Q3–Q5 adjacency produces at least one valid layout with Q3 central and at least one with P2 extreme. The question asks possibility, not necessity.  
**Shortest safe method:** fix Q3 successively at positions 2,3,4; place adjacent Q5; transfer matched P labels and test remaining slots.  
**Assumption:** “matches” means occupies the position of the same colour when rods are parallel.

---

<a id="2026-prelims-csat-q35"></a>
## Q35. Seven persons in three cars
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Group allocation · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Seven persons A, B, C, D, E, F and G travel by three cars X, Y, Z. A and another two of them travel by X. Only E travels with G, C travels by Z, but B does not travel by Y. Besides, A and B do not travel by the same car. Then which of the following are correct?

I. No one travels alone.  
II. Only D travels with F.  
III. Only C travels with B.

**Options:** (a) I and II only · (b) I and III only · (c) II and III only · (d) All three

**Metadata:** Family 06 · Logical Reasoning → Group allocation · Proposed slug: `three-car-group-allocation`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (b).**

**Reasoning:** B cannot be Y and cannot share X with A, so B is in Z with C; thus III. “Only E travels with G” makes the third car exactly E–G. The remaining D and F join A in X. Hence no one is alone, while F travels with both D and A, making II false.  
**Shortest safe method:** place the exclusive pair E–G, then force B with C.

---

<a id="2026-prelims-csat-q36"></a>
## Q36. Relations among four statements
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Implication → contraposition · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

There are four statements X, Y, Z and W. Their relations are as follows:

If X is incorrect, then so is Z; if Y is incorrect, then W is correct; if W is correct, then X is incorrect.

Which of the following is/are correct?

I. If X is correct, then so is Y.  
II. If Z is correct, then it is not necessary that Y is correct.

**Options:** (a) I only · (b) II only · (c) Both I and II · (d) Neither I nor II

**Metadata:** Family 06 · Logical Reasoning → Implication → contraposition · Proposed slug: `statement-implication-chain`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (a).**

**Reasoning:** \(W\to\neg X\) gives \(X\to\neg W\). \(\neg Y\to W\) gives \(\neg W\to Y\). Therefore \(X\to Y\): I is true. Also \(\neg X\to\neg Z\) gives \(Z\to X\to Y\), so II is false.  
**Shortest safe method:** write contrapositives and chain them.

---

<a id="2026-prelims-csat-q37"></a>
## Q37. Runners on a circular track
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Motion → Circular track → relative laps · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

X and Y are two runners who run for the same duration of time on the same circular track. They started running at the same time in the same direction with uniform speeds. When X completed 7 rounds, Y did exactly 5. After completing 5 rounds, Y changed his direction and started running in the opposite direction with speed which is double of his earlier speed. On the other hand, X continued to run with the same speed. They stopped running when X completed exactly 21 rounds. How many times did X and Y meet after they had started and before they finally stopped?

**Options:** (a) 35 · (b) 34 · (c) 31 · (d) 29

**Metadata:** Family 04 · Motion → Circular track → relative laps · Proposed slug: `circular-track-direction-change`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Phase 1 ends at X=7,Y=5; relative gain is 2 laps, so two meetings after the start, including the phase boundary. In phase 2, Y’s opposite speed is \(10/7\) of X’s speed. While X covers 14 more laps, relative distance is \(14(1+10/7)=34\) laps. Excluding the already-counted boundary and the final stopping instant leaves 33 new meetings. Total \(2+33=35\).  
**Shortest safe method:** count integer relative laps separately in the two phases and handle endpoints explicitly.

---

<a id="2026-prelims-csat-q38"></a>
## Q38. Two marking schemes
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra → Simultaneous linear equations → marks · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

In an objective type question paper, 5 marks are awarded for a correct answer and 2 marks are deducted for a wrong answer. A student attempted all the questions and got a score of 69. Had he been awarded 4 marks for a correct answer and 1 mark deducted for a wrong answer, he would have scored 84. How many questions were there in the question paper?

**Options:** (a) 99 · (b) 81 · (c) 84 · (d) 79

**Metadata:** Family 05 · Algebra → Simultaneous linear equations → marks · Proposed slug: `objective-marking-equations`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Let correct \(c\), wrong \(w\). \(5c-2w=69\), \(4c-w=84\). Thus \(w=4c-84\); substitution gives \(c=33,w=48\), total 81.  
**Shortest safe method:** eliminate \(w\) by doubling the second equation.

---

## Shared passage for Q39–Q40

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

The Juvenile Justice (Care and Protection of Children) Act, or the JJ Act, 2015 allows for the possibility for trying adolescents above 16 as adults if they are accused of committing a heinous offence. A heinous offence is one with a minimum punishment of seven years. Offences such as culpable homicide and causing death by negligence, which are common in drunken driving cases, are not heinous offences because they do not have a prescribed minimum punishment. The JJ Act, amended in 2021, now categorises an offence that has no minimum sentence, but has a maximum sentence of seven years or more as a serious offence which nonetheless, in the opinion of activists, does not merit the transfer of a case to the adult criminal justice system.

<a id="2026-prelims-csat-q39"></a>
## Q39. Conclusions from the JJ passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Conclusions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions is/are valid?

1. Only a serious offence as categorised by the revised JJ Act, justifies the transfer of a case to the adult judicial system.
2. The JJ Act, 2021, categorises an offence as a serious offence based on the maximum sentence it carries, rather than on the minimum sentence.

**Options:** (a) 1 only · (b) 2 only · (c) Both 1 and 2 · (d) Neither 1 nor 2

**Metadata:** Family 01 · Reading Comprehension → Conclusions · Proposed slug: `juvenile-justice-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (b).**

**Passage-only justification:** Transfer is associated with heinous offences, while activists oppose transfer for the newly defined serious category; 1 reverses this. Statement 2 accurately captures the no-minimum/maximum-seven-years rule.

---

<a id="2026-prelims-csat-q40"></a>
## Q40. Statements from the JJ passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. If an offence has no minimum prescribed punishment, it cannot be considered heinous as per the JJ Act, 2015.
2. As per the JJ Act, 2021, an offence for which there is a provision for a maximum sentence of seven years or more, but no minimum sentence, is to be considered a serious offence.

**Options:** (a) 1 only · (b) 2 only · (c) Both 1 and 2 · (d) Neither 1 nor 2

**Metadata:** Family 01 · Reading Comprehension → Statements · Proposed slug: `juvenile-justice-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (c).**

**Passage-only justification:** Both statements are direct restatements of the definitions supplied in the passage; the competing options omit one or both.

---

<a id="2026-prelims-csat-q41"></a>
## Q41. Explosion, sound and drones
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Rates/Motion/Time → Sound and travel time · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

An explosion takes place at a certain distance from an army camp. As soon as the sensor in the camp receives the sound of the explosion, a drone starts flying towards the spot of explosion. The drone clicks a picture from the spot and the camp receives it at the same time. Immediately another drone starts flying to the spot and it also sends a picture as soon as it reaches the spot. The two pictures were received at 5:02 PM and 5:05 PM, respectively. If the speed of the drones is 30 m/s, at what time did the explosion take place? Assume that the speed of sound is 300 m/s.

**Options:** (a) 4:59:00 PM · (b) 4:59:02 PM · (c) 4:58:42 PM · (d) 4:56:32 PM

**Metadata:** Family 04 · Rates/Motion/Time → Sound and travel time · Proposed slug: `explosion-sound-drone-time`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (c).**

**Reasoning:** The second drone takes 3 minutes, so distance \(=30\times180=5400\) m. The first drone also took 3 minutes, meaning sound reached camp at 4:59 PM. Sound travel time \(=5400/300=18\) s; explosion time \(=4{:}59{:}00-18\) s \(=4{:}58{:}42\) PM.  
**Shortest safe method:** obtain distance from the second drone, then subtract sound time from the first drone’s start.

---

<a id="2026-prelims-csat-q42"></a>
## Q42. Unit digit of \(6^{129}\times7^{307}\)
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Unit-digit cycles · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

The digit in the unit place of the number \(6^{129}\times7^{307}\) is

**Options:** (a) 2 · (b) 4 · (c) 8 · (d) 6

**Metadata:** Family 02 · Number Systems → Unit-digit cycles · Proposed slug: `unit-digit-power-product`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (c).**

**Reasoning:** \(6^n\) always ends in 6. Powers of 7 cycle \(7,9,3,1\); \(307\equiv3\pmod4\), so \(7^{307}\) ends in 3. Product ends in \(6\cdot3=18\), hence 8.  
**Shortest safe method:** use only unit-digit cycles.

---

<a id="2026-prelims-csat-q43"></a>
## Q43. Change in monthly saving
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic/Commercial Math → Percentages → base reconstruction · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A person saves 10% of his salary every month. If his salary increases by 12% and the expenditure increases by 10%, then what will be the change in his saving per month?

**Options:** (a) 20% increase · (b) 30% increase · (c) 3% decrease · (d) 2% decrease

**Metadata:** Family 03 · Arithmetic/Commercial Math → Percentages → base reconstruction · Proposed slug: `salary-expenditure-saving-change`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Take salary 100: saving 10, expenditure 90. New salary 112; new expenditure 99; new saving 13. Increase \(=3/10=30\%\).  
**Shortest safe method:** use a salary base of 100.

---

<a id="2026-prelims-csat-q44"></a>
## Q44. Blood relation
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Blood relations → family tree · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

P has a son and a daughter. S is the mother of T. S is R’s spouse. Q and R are children of P. Then how is Q related to S?

**Options:** (a) Q is a sister of S · (b) Q is a daughter of S · (c) Q is the mother of S · (d) Q is a sister of the husband of S

**Metadata:** Family 06 · Logical Reasoning → Blood relations → family tree · Proposed slug: `p-q-r-s-blood-relation`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (d).**

**Reasoning:** S is identified as mother, so R, her spouse and one of P’s two children, is the son. Q is therefore P’s daughter and R’s sister: the sister of S’s husband.  
**Shortest safe method:** draw P above siblings Q–R; attach S as R’s spouse.  
**Assumption:** “mother” and “spouse” are used in the conventional binary relation intended by the paper.

---

<a id="2026-prelims-csat-q45"></a>
## Q45. Three-digit powers of 2
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Exponents → bounded counting · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

How many three-digit numbers are integral powers of 2?

**Options:** (a) 1 · (b) 2 · (c) 3 · (d) 4

**Metadata:** Family 02 · Number Systems → Exponents → bounded counting · Proposed slug: `three-digit-powers-of-two`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (c).**

**Reasoning:** \(2^7=128,2^8=256,2^9=512\) are three-digit; \(2^{10}=1024\). Count 3.

---

## Shared passage for Q46–Q47

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

The key source of the battle for clean skies and clear lungs is the fuel we burn—from household Chulhas to the thermal power plants. In most cases, it is biomass or coal. The Supreme Court banned the use of pet coke—the dirtiest of such fuels. The Delhi Government banned the use of coal, which was later extended to the entire National Capital Region. It was also agreed that the thermal power plants would clean up or shut down. Action on this has been patchy to say the least. The lesson from the transition to CNG is that people need alternatives for a ban to be effective. When diesel buses were stopped, CNG supply had to be assured. It also had to be feasible in terms of cost. The Supreme Court agreed that fiscal measures were needed to keep clean fuel cheaper than dirty fuel. Now even as coal is banned, the price of natural gas makes industry uncompetitive.

<a id="2026-prelims-csat-q46"></a>
## Q46. Inferences from the clean-fuel passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Inferences · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following inferences is/are correct?

1. The source of the energy we consume is the key to the battle for cleaner air.
2. Bans are effective where the will is strong and the people are convinced that such bans are for the greater good of society.
3. There is judicial approval for a policy that intervenes fiscally to facilitate benevolent pricing for cleaner fuel.

**Options:** (a) 1 and 2 · (b) 2 and 3 · (c) 1 and 3 · (d) 1 only

**Metadata:** Family 01 · Reading Comprehension → Inferences · Proposed slug: `clean-fuel-policy-inferences`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (c).**

**Passage-only justification:** 1 and 3 are explicit. The passage conditions effectiveness on an available, affordable alternative—not merely will or public conviction—so 2 substitutes a different causal condition.

---

<a id="2026-prelims-csat-q47"></a>
## Q47. Statements from the clean-fuel passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. Thermal power stations in Delhi were required to summarily shut down.
2. CNG supplies had to be assured once diesel vehicles were prohibited from plying.
3. The Supreme Court banned the use of coal across the National Capital Region.

**Options:** (a) 1 and 2 · (b) 3 only · (c) 2 only · (d) 2 and 3

**Metadata:** Family 01 · Reading Comprehension → Statements · Proposed slug: `clean-fuel-policy-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (c).**

**Passage-only justification:** 1 omits the alternative “clean up”; 2 is explicit; 3 confuses the Delhi Government’s coal ban with the Court’s pet-coke ban.

---

<a id="2026-prelims-csat-q48"></a>
## Q48. Colour-set syllogism
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Syllogism → transitive set containment · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Consider the following statements:

Every red is blue. Every blue is green. Every green is yellow.

Which of the following statements denoted by P, Q and R are correct?

P. Every blue is yellow.  
Q. Every red is green.  
R. Every red is yellow.

**Options:** (a) P and Q only · (b) Q and R only · (c) P and R only · (d) P, Q and R

**Metadata:** Family 06 · Logical Reasoning → Syllogism → transitive set containment · Proposed slug: `colour-set-transitivity`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (d).**

**Reasoning:** \(R\subset B\subset G\subset Y\). Every listed conclusion follows by transitivity.  
**Shortest safe method:** draw nested sets.

---

<a id="2026-prelims-csat-q49"></a>
## Q49. Occurrences of digit 5
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Digit frequency · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

How many times does 5 appear in all two-digit positive integers?

**Options:** (a) 18 · (b) 19 · (c) 20 · (d) 21

**Metadata:** Family 02 · Number Systems → Digit frequency · Proposed slug: `digit-five-two-digit-integers`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Tens-place 5 occurs 10 times (50–59); units-place 5 occurs 9 times (15–95). The two appearances in 55 are correctly counted separately. Total 19.  
**Shortest safe method:** count by place value, not by numbers containing 5.

---

<a id="2026-prelims-csat-q50"></a>
## Q50. Two six-kilometre journeys
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Rates/Motion/Time → Segment times → speed comparison · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

X travels 6 km on a bicycle with average speeds of 5 km per hour, 10 km per hour and 4 km per hour during the first 1 km, the next 2 km and the remaining 3 km, respectively. Y travels the same distances with average speeds of 4 km per hour, 10 km per hour and 5 km per hour, respectively. How many minutes early will Y complete the journey if both X and Y start at the same time?

**Options:** (a) 3 · (b) 4 · (c) 5 · (d) 6

**Metadata:** Family 04 · Rates/Motion/Time → Segment times → speed comparison · Proposed slug: `multi-segment-speed-comparison`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (d).**

**Reasoning:** \(t_X=1/5+2/10+3/4=1.15\) h; \(t_Y=1/4+2/10+3/5=1.05\) h. Difference \(0.10\) h \(=6\) min.  
**Shortest safe method:** only the first and third segments differ; compare \(1/5+3/4\) with \(1/4+3/5\).

---

<a id="2026-prelims-csat-q51"></a>
## Q51. Lightest of seven cubes
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Balance weighing → ternary split · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Seven cubes are identical in shape. Out of these, the weight of each of the six cubes is equal and the weight of the remaining cube is less than the weight of any other cube. A balance is used to identify the lightest cube. What is the minimum number of attempts required to distinguish the odd cube with certainty?

**Options:** (a) 2 · (b) 3 · (c) 4 · (d) 1

**Metadata:** Family 06 · Logical Reasoning → Balance weighing → ternary split · Proposed slug: `seven-cubes-lightest-balance`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Weigh 3 against 3. If equal, the seventh is light; otherwise the lighter pan contains it. In the latter case weigh 1 against 1 from those three: imbalance identifies it, equality identifies the third. One weighing has only three outcomes and cannot distinguish seven possibilities.  
**Shortest safe method:** split \(7\) as \(3+3+1\).

---

## Shared passage for Q52–Q53

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

Previous waves of customer-service technology, including email and those pesky voice menus, stoked concerns of job losses, only for them to fail to materialise. AI could yet prove different. And if it does, its effects may be salutary. Human agents could be freed up to spend more time on creative and rewarding tasks, like using feedback to make products and services better—and thereby spend less time listening to irate customers!

<a id="2026-prelims-csat-q52"></a>
## Q52. Point of view on AI and customer service
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Point of view · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which one among the following statements most appropriately reflects the point of view of the given passage?

**Options:**  
(a) If AI were to take over customer service, there would be no work left for human subjects to do.  
(b) Irritating voice menus and email could not achieve human redundancy to the extent that AI might.  
(c) The value of human intervention in the workplace affected by AI might be enhanced through redirection towards more fulfilling tasks.  
(d) Unlike previous waves in customer-service technology, AI has raised the alarm of worker replacement.

**Metadata:** Family 01 · Reading Comprehension → Point of view · Proposed slug: `ai-customer-service-point-of-view`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (c).**

**Passage-only justification:** (c) captures the author’s qualified optimism. (a) is absolute; (b) focuses on redundancy rather than salutary task redirection; (d) is false because previous waves also raised fears.

---

<a id="2026-prelims-csat-q53"></a>
## Q53. Conclusions on customer-service technology
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Conclusions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions, made on the basis of the given passage, is/are correct?

1. The advent of new customer-service technology had invariably sparked fears about job losses.
2. Often it is found that instead of job losses, alternative channels for employee engagement are discovered while certain tasks are replaced by technology.
3. The advent of technology inevitably leads to stressful outcomes.

**Options:** (a) 1 and 3 · (b) 2 only · (c) 3 only · (d) 1 and 2

**Metadata:** Family 01 · Reading Comprehension → Conclusions · Proposed slug: `customer-service-technology-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (d).**

**Passage-only justification:** 1 is explicit and 2 is the author’s suggested beneficial redirection. “Inevitably” makes 3 contrary to the passage’s salutary possibility.

---

## Shared passage for Q54–Q55

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

Cattle from the nearby villages came to the common ground to graze, and there was still a cool freshness in the air. Hori took several deep breaths and thought of sitting down for a while, since he’d be dying of heat in the scorching “loo” wind the rest of the day. A number of farmers were eager to lease this bit of land and had offered a good price, but Rai Sahib—God bless him—had plainly told them it was reserved for grazing and would not be relinquished for any price. If he’d been one of those selfish Zamindars, he’d have said the cattle could go to hell, that there was no reason for him to miss the chance to make a little money. But the Rai Sahib still held to the old values, feeling that any landlord who didn’t look after his tenants was less than human.

<a id="2026-prelims-csat-q54"></a>
## Q54. Conclusions from the Rai Sahib passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Literary conclusions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions is/are correct?

1. All landlords essentially have some goodness trapped within them.
2. The common grazing grounds of a village are intended for use by the cattle of that village.
3. Landlords who believe in tradition tend to be more concerned about their tenants.
4. Winds later in the day tend to be cooler post the hot winds of the morning.

**Options:** (a) 1 and 3 · (b) 2 and 4 · (c) 3 only · (d) 2 only

**Metadata:** Family 01 · Reading Comprehension → Literary conclusions · Proposed slug: `rai-sahib-passage-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (c).**

**Passage-only justification:** 3 reflects the narrator’s explicit contrast. 1 universalises one character; 2 is contradicted by cattle from nearby villages; 4 reverses the cool-now/scorching-later sequence.

---

<a id="2026-prelims-csat-q55"></a>
## Q55. Incorrect statements from the Rai Sahib passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Literary incorrect statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements are not correct?

1. The landholdings of Rai Sahib were currently not being used for farming.
2. Temperamentally, Rai Sahib was as greedy as other landlords.
3. It cannot be ascertained that Rai Sahib could have made some money by leasing out the grazing land.
4. It may be asserted that Rai Sahib valued his tenants and wanted to protect their livelihood.

**Options:** (a) 1 and 2 only · (b) 1 and 3 only · (c) 3 and 4 · (d) 1, 2 and 3

**Metadata:** Family 01 · Reading Comprehension → Literary incorrect statements · Proposed slug: `rai-sahib-incorrect-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (d).**

**Passage-only justification:** 1 extrapolates from one grazing plot to all holdings; 2 contradicts the contrast with selfish zamindars; 3 contradicts the stated good lease offers. Statement 4 is supported.

---

<a id="2026-prelims-csat-q56"></a>
## Q56. Direction and displacement
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Direction sense → coordinates · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A person facing the East travels 4 km straight and then turns right and travels 3 km, then further turns left and travels 2 km and finally turns left and travels 3 km. The minimum distance between the final point and the initial point, and the direction in which the person is facing at the final point are, respectively

**Options:** (a) 12 km, East · (b) 6 km, East · (c) 8 km, North · (d) 6 km, North

**Metadata:** Family 06 · Logical Reasoning → Direction sense → coordinates · Proposed slug: `direction-turns-displacement`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Coordinates: \((0,0)\to(4,0)\to(4,-3)\to(6,-3)\to(6,0)\). Displacement is 6 km; final turn points north.  
**Shortest safe method:** use an x–y sketch.

---

<a id="2026-prelims-csat-q57"></a>
## Q57. Fibonacci-like sequence
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Recurrence sequence · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

In a sequence of numbers, each number other than the first two is the sum of the two immediately preceding numbers from it. If the first two numbers in the sequence are 4 and 7, then the sixth number is

**Options:** (a) 29 · (b) 37 · (c) 43 · (d) 47

**Metadata:** Family 02 · Number Systems → Recurrence sequence · Proposed slug: `four-seven-recurrence-sixth-term`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (d).**

**Reasoning:** \(4,7,11,18,29,47\).

---

<a id="2026-prelims-csat-q58"></a>
## Q58. Workers in two companies
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic → Ratios → common component · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

The ratio of male to female workers in two companies A and B is 13:10 and 7:5, respectively. If both the companies have the same number of female workers, then what is the ratio of the total number of workers in A to those in B?

**Options:** (a) 24:23 · (b) 23:24 · (c) 18:17 · (d) 27:18

**Metadata:** Family 03 · Arithmetic → Ratios → common component · Proposed slug: `company-workers-ratio`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Set each female count to 50. A has 65 males, total 115; B has 70 males, total 120. Ratio \(115:120=23:24\).  
**Shortest safe method:** equalise female-ratio parts using LCM 10.

---

<a id="2026-prelims-csat-q59"></a>
## Q59. HCF–LCM product as a cube
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → HCF/LCM identity · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

If the product of the HCF and LCM of two distinct numbers is the cube of one of the numbers, then which of the following statements is/are correct?

I. The difference of the numbers is an even number.  
II. One of the numbers is a perfect square.

**Options:** (a) I only · (b) II only · (c) Both I and II · (d) Neither I nor II

**Metadata:** Family 02 · Number Systems → HCF/LCM identity · Proposed slug: `hcf-lcm-cube-relation`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (c).**

**Reasoning:** \(\operatorname{HCF}(a,b)\operatorname{LCM}(a,b)=ab\). If \(ab=a^3\), then \(b=a^2\), or symmetrically \(a=b^2\). Thus one is a square. Their difference is \(n^2-n=n(n-1)\), always even.  
**Shortest safe method:** replace HCF×LCM by product of the numbers.

---

<a id="2026-prelims-csat-q60"></a>
## Q60. Divisibility by 11
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Divisibility by 11 → digit puzzle · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

If \(x\) and \(y\) are two digits and the number \(4x5y790\) is divisible by 11, then what is the remainder, if \(x+y\) is divided by 11?

**Options:** (a) 1 · (b) 3 · (c) 5 · (d) 7

**Metadata:** Family 02 · Number Systems → Divisibility by 11 → digit puzzle · Proposed slug: `divisibility-eleven-digit-sum`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Alternating-sum difference is \((4+5+7+0)-(x+y+9)=7-(x+y)\), a multiple of 11. Thus \(x+y=7\) or 18; either leaves remainder 7 modulo 11.  
**Shortest safe method:** apply the alternating-sum test directly.

---

## Shared passage for Q61–Q62

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

Was it the sun-dappled ambience, the strawberries and cream, the frustration of Flavio Cobolli’s unforced errors against Serbian Novak Djokovic on Centre Court or simply the crushing weight of being a 64-year-old man in the third act of a very public life? Whatever the reason, Hugh Grant, the actor, deserves empathy. There he was, in the Royal Box at Wimbledon, flanked by Britain’s well-dressed and well-rested spectators, watching the men’s singles quarterfinals, when the actor did something quietly radical: head at a tilt, eyes closed, utterly unbothered, he took a nap. So praise be to Grant for serving up an unexpected ace. In that small, delicious moment, he didn’t merely catch forty winks, he made an elegant case for surrender. Not to laziness, but to limits. To the body’s quiet wisdom over society’s relentless performance metrics. Wimbledon had its tennis. The perpetually sleep-deprived discovered a leading man, not of action, but of rest.

<a id="2026-prelims-csat-q61"></a>
## Q61. Statements from the Hugh Grant passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. Radical action can also be attributed to mild surrender where one acts against societal expectations.
2. Submitting to one’s limitations, given the effect of age and other factors, ought not to be conflated with laziness.
3. “Leading man” usually refers to one who plays the lead role in a movie; in this instance the implication is that Hugh Grant is performing the role of not an action hero, but that of a resting one!

**Options:** (a) 1 and 2 only · (b) 2 and 3 only · (c) 1, 2 and 3 · (d) 3 only

**Metadata:** Family 01 · Reading Comprehension → Statements · Proposed slug: `hugh-grant-rest-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (c).**

**Passage-only justification:** All three capture explicit wordplay and argument in the passage. The narrower alternatives arbitrarily omit supported statements.

---

<a id="2026-prelims-csat-q62"></a>
## Q62. Further statements from the Hugh Grant passage
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. Hugh Grant was watching, from the Royal Box, the men’s semifinal match on Centre Court between Flavio Cobolli and Novak Djokovic.
2. The phrase “unexpected ace” in the context uses a term from the game of tennis to highlight Hugh Grant’s somewhat uncharacteristic act of catching “forty winks”; an act that is viewed with opprobrium.
3. Grant subjects the demands of society to the wisdom of his body.

**Options:** (a) 1 and 2 · (b) 3 only · (c) 2 and 3 · (d) 2 only

**Metadata:** Family 01 · Reading Comprehension → Statements · Proposed slug: `hugh-grant-context-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (b).**

**Passage-only justification:** 1 changes quarterfinal to semifinal. Although “unexpected ace” is tennis wordplay, the passage praises rather than condemns the act, so 2 as a whole is false. Statement 3 restates the central contrast.

---

## Shared passage for Q63–Q64

**Directions for the next 2 (two) items:** Read the following passage and answer the items that follow. Your answers should be based solely on the passage.

The process by which countries close their labour-productivity gap with the technology leader is based on convergence theory. The convergence model divides economic eras into three phases: the breakaway, the catch-up, and the fine-tuning phase. It also divides economic entities into two categories: the technology leaders and the technology followers. The process begins with the development of a new technology, such as scavenging three million years ago (MYA), hunting—one MYA, farming—12 thousand years ago, and industrial technology—a little more than 200 years ago. During the breakaway phase, the per capita income of the technology leaders (e.g., Western Europe and North America in the industrial era) rises, but is unchanged for the technology followers. In the catch-up phase, the followers adopt the new technology and close their per capita income gap with the technology leaders. In the fine-tuning phase, where participants try to extract the remaining benefits from an increasingly exhausted technology, leaders and followers have similar per capita incomes.

<a id="2026-prelims-csat-q63"></a>
## Q63. Conclusions from convergence theory
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Conclusions · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following conclusions are correct?

1. In the breakaway phase, economic progress is slow for the technology followers.
2. In the catch-up phase, leaders stagnate and followers, therefore, close the gap between them and the leaders.
3. In the fine-tuning phase, technology is exhausted, as it were, and both leaders and followers attempt to extract leftover benefits, leading to more or less similar per capita income levels.
4. Industrial technology followed scavenging, which preceded hunting, which itself was followed by farming.

**Options:** (a) 3 and 4 only · (b) 1, 2, 3 and 4 · (c) 1 and 2 only · (d) 2, 3 and 4 only

**Metadata:** Family 01 · Reading Comprehension → Conclusions · Proposed slug: `convergence-theory-conclusions`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (a).**

**Passage-only justification:** Followers’ income is “unchanged,” not merely slow, so 1 is imprecise. The passage does not say leaders stagnate during catch-up, so 2 adds a cause. Statements 3 and 4 fit the stated phase and chronology.

---

<a id="2026-prelims-csat-q64"></a>
## Q64. Statements on convergence theory
**Primary route:** CSAT → [Reading Comprehension](../../topics/csat/reading-comprehension.md) → Reading Comprehension → Statements · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which of the following statements is/are correct?

1. The convergence model divides nations into three phases of economic progress.
2. At the heart of the convergence theory is the closing of the gap between labour and productivity.
3. Technology leaders typically have arrived earlier at different economic eras.
4. The time period covered by the convergence theory presented herein encompasses, as mentioned, 4012200 years.

**Options:** (a) 2 and 4 · (b) 2 and 3 · (c) 3 only · (d) 1, 3 and 4

**Metadata:** Family 01 · Reading Comprehension → Statements · Proposed slug: `convergence-theory-statements`  
**Canonical owner:** `CSAT/basic/01_Reading-Comprehension.md`

**PROVISIONAL answer: (b).**

**Passage-only justification:** 2 is explicit; 3 follows from leaders developing/adopting first. The model divides **eras**, not nations, into phases, so 1 fails. Adding isolated dates to assert an exact covered duration is not licensed, so 4 fails.  
**Ambiguity flag:** the printed wording “labour-productivity gap” means a productivity gap in labour, not a gap between labour and productivity.

---

<a id="2026-prelims-csat-q65"></a>
## Q65. Alloy mixture
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic/Commercial Math → Mixtures → alligation · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

An alloy P contains 20% copper and 80% zinc by weight. Another alloy Q contains 60% copper and 40% zinc by weight. A third alloy R is to be prepared from P and Q so that it contains equal amount of copper and zinc. In what ratio, amounts of P and Q be mixed in order to get R?

**Options:** (a) 1:3 · (b) 3:1 · (c) 2:3 · (d) 3:2

**Metadata:** Family 03 · Arithmetic/Commercial Math → Mixtures → alligation · Proposed slug: `copper-zinc-alloy-mixture`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (a).**

**Reasoning:** By alligation, \(P:Q=(60-50):(50-20)=10:30=1:3\).  
**Shortest safe method:** cross-differences around the target percentage.

---

<a id="2026-prelims-csat-q66"></a>
## Q66. Reversed two-digit numbers
**Primary route:** CSAT → [Number Systems and Number Sense](../../topics/csat/number-systems-and-number-sense.md) → Number Systems → Reversed digits → divisibility · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A is a 2-digit number with different digits. B is also a 2-digit number and is obtained by reversing the digits of A. If \(A-B\) is a multiple of 27, where \(A>B\), how many such different A’s are possible?

**Options:** (a) 6 · (b) 9 · (c) 12 · (d) 18

**Metadata:** Family 02 · Number Systems → Reversed digits → divisibility · Proposed slug: `reversed-two-digit-multiple-27`  
**Canonical owner:** `CSAT/basic/02_Number-Systems-and-Number-Sense.md`

**PROVISIONAL answer: (b).**

**Reasoning:** If digits are \(a>b\ge1\), \(A-B=9(a-b)\). Thus \(a-b\) is a positive multiple of 3: 3 or 6 (difference 9 would require \(b=0\), making B one-digit). Difference 3 gives six pairs; difference 6 gives three; total 9.  
**Shortest safe method:** reduce reversal difference to \(9(a-b)\).

---

<a id="2026-prelims-csat-q67"></a>
## Q67. Coding ZERO and STOP
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Letter coding → alternating shifts · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

If ZERO is encoded as ADSN, then how do you encode STOP?

**Options:** (a) SPOT · (b) TSPO · (c) TSOP · (d) POST

**Metadata:** Family 06 · Logical Reasoning → Letter coding → alternating shifts · Proposed slug: `zero-stop-letter-code`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (b).**

**Reasoning:** ZERO→ADSN applies alternating \(+1,-1,+1,-1\). STOP becomes T, S, P, O = TSPO.  
**Shortest safe method:** compare letters position by position; do not rearrange them.

---

<a id="2026-prelims-csat-q68"></a>
## Q68. Tiling a \(3\times100\) rectangle
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Geometry → One-dimensional tiling → integer optimisation · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

There are three types of rectangular tiles: 3′ × 3′, 3′ × 7′ and 3′ × 11′. An area of rectangular shape of dimensions 3′ × 100′ is to be covered using these tiles without breaking them. If \(x\) and \(y\) are the maximum and minimum numbers of tiles of various sizes, respectively, that can be used to cover the area exactly, then \(x-y\) is

**Options:** (a) 20 · (b) 12 · (c) 10 · (d) 7

**Metadata:** Family 04 · Geometry → One-dimensional tiling → integer optimisation · Proposed slug: `rectangular-tile-count-extrema`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Reduce to lengths 3,7,11 summing to 100. Maximum tile count: \(31\cdot3+7=100\), so \(x=32\). Minimum: \(8\cdot11+4\cdot3=100\), so \(y=12\); 9–11 tiles cannot reach 100 with the needed residue. Difference 20.  
**Shortest safe method:** maximise with 3s and minimise with 11s, adjusting residues.

---

<a id="2026-prelims-csat-q69"></a>
## Q69. Train slowed by accident and defect
**Primary route:** CSAT → [Rates, Motion, Time and Geometry](../../topics/csat/rates-motion-time-and-geometry.md) → Rates/Motion/Time → Piecewise speeds · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A train has to complete a journey of 800 km. If it meets a minor accident, its speed becomes half of the existing speed. If there is a mechanical defect, the speed becomes one-fourth of the existing speed. On its way, the train meets with a minor accident after 200 km; and 400 km thereafter, it develops a mechanical defect. Had the train developed the mechanical defect after 200 km and met the minor accident 400 km thereafter, it would have taken 4 more hours to reach its destination. What was the original speed of the train in km per hour?

**Options:** (a) 200 · (b) 190 · (c) 150 · (d) 100

**Metadata:** Family 04 · Rates/Motion/Time → Piecewise speeds · Proposed slug: `train-accident-defect-speed`  
**Canonical owner:** `CSAT/basic/04_Rates-Motion-Time-and-Geometry.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Actual time \(=200/v+400/(v/2)+200/(v/8)=2600/v\). Reversed time \(=200/v+400/(v/4)+200/(v/8)=3400/v\). Difference \(800/v=4\), so \(v=200\) km/h.  
**Shortest safe method:** only the middle 400 km changes from \(v/2\) to \(v/4\); extra time \(=400(4/v-2/v)=800/v\).

---

<a id="2026-prelims-csat-q70"></a>
## Q70. Weighted recruitment score
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Data Interpretation → Weighted scores → ranking · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

In a recruitment process, the selection of candidates is based on their performance in three components. The weightages of the components 1, 2 and 3 are 0.2, 0.3 and 0.5, respectively. Use the data given below and find the cutoff score if exactly three candidates are to be selected:

| Candidate | Score in component 1 | Score in component 2 | Score in component 3 |
|---:|---:|---:|---:|
| 1 | 5 | 4 | 6 |
| 2 | 4 | 6 | 5 |
| 3 | 3 | 2 | 8 |
| 4 | 9 | 4 | 3 |
| 5 | 8 | 8 | 2 |

**Options:** (a) 5.1 · (b) 5.2 · (c) 5.3 · (d) 5.4

**Metadata:** Family 06 · Data Interpretation → Weighted scores → ranking · Proposed slug: `weighted-recruitment-cutoff`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (a).**

**Reasoning:** Weighted scores: candidate 1 = 5.2; 2 = 5.1; 3 = 5.2; 4 = 4.5; 5 = 5.0. The third-highest score is 5.1, the cutoff.  
**Shortest safe method:** compute only one decimal place and rank.

---

<a id="2026-prelims-csat-q71"></a>
## Q71. Relationship among environmental statements
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → Logical Reasoning → Statement relationships · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Consider the following three statements, namely S1, S2 and S3:

S1. Protecting the environment is an existential exigency for humans, given the impact of environmental degradation on climate change.  
S2. Scientific consensus has not been achieved with regard to the extent of the contribution of human intervention to climate change.  
S3. Environmental activism includes climate alarmism and other extremist points of view that often become the focus of climate change deniers.

Which of the following relationships based on the statements given above is/are correct?

1. S3 is a counterpoint to S1.
2. S3 is unconnected to S1 and S2.
3. S2 could be the reason for S3.

**Options:** (a) 2 and 3 only · (b) 1, 2 and 3 · (c) 1 and 2 only · (d) 3 only

**Metadata:** Family 06 · Logical Reasoning → Statement relationships · Proposed slug: `environment-statements-relationship`  
**Canonical owner:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`

**PROVISIONAL answer: (d).**

**Reasoning:** S3 does not negate the existential need asserted in S1, so it is not a counterpoint. It is connected to both climate action and uncertainty, making 2 false. The uncertainty asserted by S2 could create room for alarmist/denialist contestation described in S3, so 3 is plausible.  
**Ambiguity flag:** “could be the reason” is permissive rather than a proven causal claim; the provisional key accepts that relationship.

---

<a id="2026-prelims-csat-q72"></a>
## Q72. Relationship category and communication type
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → 2026-prelims-csat-q72 · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Match List-I with List-II and select the answer using the code given below the Lists:

**List-I (Relationship category)**

A. Between cricket captain and team members  
B. Between judge and lawyers in court  
C. Between Vice Chancellor and Deputy Registrar  
D. Between peers and coworkers

**List-II (Communication type)**

1. Informal and firm  
2. Informal and open-ended  
3. Formal and open-ended  
4. Formal and firm

**Options:** (a) A-1, B-3, C-4, D-2 · (b) A-1, B-4, C-3, D-2 · (c) A-2, B-4, C-3, D-1 · (d) A-2, B-3, C-4, D-1

**Metadata:** Family 06; Topic-07 overlay · Interpersonal/Communication Skills → relationship and register · Proposed slug: `relationship-communication-type-matching`  
**Canonical owners:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; content overlay `CSAT/basic/07_Interpersonal-and-Communication-Skills.md`

**PROVISIONAL answer: (b).**

**Reasoning:** Captain–team is informal but firm (1); court communication is formal and firm (4); Vice Chancellor–Deputy Registrar is formal but permits administrative exchange (3); peers are informal and open-ended (2).  
**Competing options:** each alternative misclassifies at least one hierarchy or institutional setting.

---

<a id="2026-prelims-csat-q73"></a>
## Q73. Communication tools and purposes
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → 2026-prelims-csat-q73 · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Match List-I with List-II and select the answer using the code given below the Lists:

**List-I (Tool of communication)**

A. Memorandum  
B. Flyer  
C. Bcc  
D. Minutes

**List-II (Purpose)**

1. To record decisions  
2. To inform confidentially  
3. To intimate a directive  
4. To disseminate non-targeted information

**Options:** (a) A-1, B-4, C-2, D-3 · (b) A-1, B-2, C-4, D-3 · (c) A-3, B-4, C-2, D-1 · (d) A-3, B-2, C-4, D-1

**Metadata:** Family 06; Topic-07 overlay · Communication Skills → tools and purposes · Proposed slug: `communication-tool-purpose-matching`  
**Canonical owners:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; content overlay `CSAT/basic/07_Interpersonal-and-Communication-Skills.md`

**PROVISIONAL answer: (c).**

**Reasoning:** A memorandum conveys an internal directive (3); a flyer broadcasts non-targeted information (4); blind carbon copy conceals recipients and supports confidential informing (2); minutes record decisions (1).

---

<a id="2026-prelims-csat-q74"></a>
## Q74. Resolving culturally diverse office conflict
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → 2026-prelims-csat-q74 · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Which among the following actions would constitute the most appropriate directive(s) in resolving interpersonal conflict in an office with culturally diverse personnel?

1. Direct personnel to practise activities that are the cultural markers of diverse groups.
2. Allow conflicts to resolve naturally over time to set an appropriate precedent of leadership.
3. Encourage personnel to seek each other’s perspectives.

**Options:** (a) 1 and 3 · (b) 2 only · (c) 3 only · (d) 2 and 3

**Metadata:** Family 06; Topic-07 overlay · Interpersonal Skills → conflict resolution · Proposed slug: `culturally-diverse-office-conflict`  
**Canonical owners:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; content overlay `CSAT/basic/07_Interpersonal-and-Communication-Skills.md`

**PROVISIONAL answer: (c).**

**Reasoning:** Perspective-taking directly addresses misunderstanding and supports inclusive resolution. Compelled cultural performance may stereotype or intrude; passive waiting is not responsible leadership.  
**Shortest safe method:** choose the option that improves mutual understanding without coercion or avoidance.

---

<a id="2026-prelims-csat-q75"></a>
## Q75. Communication barriers and examples
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → 2026-prelims-csat-q75 · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Match List-I with List-II and select the answer using the code given below the Lists:

**List-I (Barrier to communication)**

A. Semantic  
B. Cognitive  
C. Organisational  
D. Affective

**List-II (Example)**

1. Lack of feedback  
2. Misunderstanding the meaning of a word  
3. Fear of social stigma  
4. Information overload

**Options:** (a) A-3, B-1, C-4, D-2 · (b) A-3, B-4, C-1, D-2 · (c) A-2, B-1, C-4, D-3 · (d) A-2, B-4, C-1, D-3

**Metadata:** Family 06; Topic-07 overlay · Communication Skills → barriers · Proposed slug: `communication-barrier-example-matching`  
**Canonical owners:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; content overlay `CSAT/basic/07_Interpersonal-and-Communication-Skills.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Semantic→word meaning (2); cognitive→information overload (4); organisational→missing feedback channel (1); affective→fear/stigma (3).

---

<a id="2026-prelims-csat-q76"></a>
## Q76. Resort-feasibility questionnaire
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → 2026-prelims-csat-q76 · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

You are required to design a “questionnaire” to be filled on-location by visitors, based on the following objective while writing a report:

“To determine the feasibility of setting up a family-oriented vacation resort in the vicinity of a lake destination in the mountains”

Which of the following heads would you include in the questionnaire to make it most appropriate for your purpose?

1. Size of family  
2. Budget  
3. Number of earners in the family  
4. Food allergies and dietary restrictions

**Options:** (a) 1 and 3 · (b) 1, 2 and 4 · (c) 1 and 2 only · (d) 2 and 3

**Metadata:** Family 06; Topic-07 overlay · Communication Skills → questionnaire design · Proposed slug: `resort-feasibility-questionnaire`  
**Canonical owners:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; content overlay `CSAT/basic/07_Interpersonal-and-Communication-Skills.md`

**PROVISIONAL answer: (c).**

**Reasoning:** Family size estimates accommodation demand; budget tests affordability. Number of earners is intrusive and redundant once budget is asked. Dietary restrictions concern operations after concept feasibility and are less central to the stated objective.  
**Ambiguity flag:** dietary needs could matter in a broader feasibility study, but the provisional key prioritises the narrow demand-and-affordability objective.

---

<a id="2026-prelims-csat-q77"></a>
## Q77. Circular letters
**Primary route:** CSAT → [Logical Reasoning, Coding, Counting and Data Interpretation](../../topics/csat/logical-reasoning-coding-counting-and-di.md) → 2026-prelims-csat-q77 · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

With reference to “circular letters”, which of the following statements is/are correct?

1. Circular letters are usually addressed to a group of people.
2. Non-standard and customized content is typical of circular letters.
3. Circular letters are used to intimate appraisals and increments of employees within organisations.
4. Circular letters are less cost-effective than personalised and specific recipient-directed letters.

**Options:** (a) 1 and 2 · (b) 2 and 4 · (c) 1, 3 and 4 · (d) 1 only

**Metadata:** Family 06; Topic-07 overlay · Communication Skills → circular letters · Proposed slug: `circular-letter-statements`  
**Canonical owners:** `CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`; content overlay `CSAT/basic/07_Interpersonal-and-Communication-Skills.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Circular letters distribute standardised information to many recipients, making 1 true and 2 false. Confidential individual appraisals are unsuitable, so 3 is false. Mass standardisation is generally more, not less, cost-effective, so 4 is false.

---

<a id="2026-prelims-csat-q78"></a>
## Q78. Partnership by capital-time
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic/Commercial Math → Partnership → capital×time · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

Three partners A, B and C entered into a business. A invested one-third of the capital for one-third duration. B invested one-fourth of the capital for one-fourth duration. C invested the remaining capital for the whole duration. Out of a profit of ₹17,000, how much profit will C get?

**Options:** (a) ₹12,000 · (b) ₹10,000 · (c) ₹12,500 · (d) ₹10,750

**Metadata:** Family 03 · Arithmetic/Commercial Math → Partnership → capital×time · Proposed slug: `partnership-capital-duration-share`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (a).**

**Reasoning:** A’s weight \(=1/3\cdot1/3=1/9\); B’s \(=1/4\cdot1/4=1/16\); C’s capital \(=1-1/3-1/4=5/12\), used full time. Ratio with denominator 144 is \(16:9:60\), total 85. C gets \(60/85\times17000=₹12,000\).  
**Shortest safe method:** convert capital×time shares to \(16:9:60\).

---

<a id="2026-prelims-csat-q79"></a>
## Q79. Repeated replacement of chemicals
**Primary route:** CSAT → [Arithmetic and Commercial Mathematics](../../topics/csat/arithmetic-and-commercial-math.md) → Arithmetic/Commercial Math → Mixtures → repeated replacement · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

There are two chemicals which do not react with each other. A container contains 10 litres of the chemical A. One litre of this chemical is removed from it and one litre of the chemical B is poured. Then one litre of the mixture is removed from the container and one litre of B is poured. If this process of replacing one litre of the mixture by one litre of B is performed once more, then what is the volume of B that is present in the container approximately (in percentage)?

**Options:** (a) 25 · (b) 27 · (c) 29 · (d) 31

**Metadata:** Family 03 · Arithmetic/Commercial Math → Mixtures → repeated replacement · Proposed slug: `three-stage-mixture-replacement`  
**Canonical owner:** `CSAT/basic/03_Arithmetic-and-Commercial-Math.md`

**PROVISIONAL answer: (b).**

**Reasoning:** A remaining \(=10(1-1/10)^3=10(0.9)^3=7.29\) litres. B \(=10-7.29=2.71\) litres \(=27.1\%\), approximately 27%.  
**Shortest safe method:** retained original fraction after \(n\) replacements is \((1-r/V)^n\).

---

<a id="2026-prelims-csat-q80"></a>
## Q80. Delivery earnings under a distance cap
**Primary route:** CSAT → [Algebra, Inequalities and Data Sufficiency](../../topics/csat/algebra-inequalities-and-data-sufficiency.md) → Algebra/Inequalities → Rate constraint → guaranteed threshold · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)

A shopkeeper employs a delivery boy and gives him a motorcycle for home delivery. For every delivery, the boy is given ₹5. At the end of the day, he also gets ₹2 for every kilometre of the distance covered in the day. The boy wants to earn more than ₹500 a day, but does not want to travel more than 100 km. Which of the following numbers of deliveries would definitely meet his target?

**Options:** (a) 80 · (b) 85 · (c) 90 · (d) The question cannot be answered due to insufficient data

**Metadata:** Family 05 · Algebra/Inequalities → Rate constraint → guaranteed threshold · Proposed slug: `delivery-earnings-rate-constraint`  
**Canonical owner:** `CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md`

**PROVISIONAL answer: (d).**

**Reasoning:** Earnings are \(5d+2k\), with only an upper bound \(0\le k\le100\). For \(d=80,85,90\), the delivery component is ₹400, ₹425, ₹450; whether total exceeds ₹500 depends on actual kilometres. None is guaranteed from the stated data.  
**Shortest safe method:** “definitely” requires testing the minimum possible distance payment, not the maximum.  
**Ambiguity flag:** if every delivery necessarily implied a positive known minimum distance, the result could change, but no such minimum is supplied.

---

## Paper reconciliation

- Questions solved: **80/80**, in exact Set-A order.
- Provisional-key sequence: **A D C D A | A A B D D | D B D A B | D A D B C | B B B A B | B D B C B | D A D C B | A A B B C | C C B D C | C C D B D | A C D C D | D D B C D | C B A B A | B B A A A | D B C C D | C D A B D**.
- Shared passages are printed once immediately before their linked question group; each question retains an independent stable anchor.
- No answer is represented as an official final UPSC key.
