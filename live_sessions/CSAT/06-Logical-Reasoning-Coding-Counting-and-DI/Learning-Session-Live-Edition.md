# Logical Reasoning, Coding, Counting and Data Interpretation - Learning Session Live Edition

**Paper:** CSAT (Civil Services Preliminary Examination, Paper II) | **Format:** four-option objective items only; there is no Mains component in this paper | **Practice in this session:** multiple choice, answered in a separate block after each item

This session teaches the reasoning that turns a stated structure into one forced answer. A seating plan, a code, a family, a set of statements, a counting rule or a table each hides a structure that the question describes only in words. The skill is to draw that structure, enter the strongest constraint first, and then check the result against every clue before you choose an option. Most errors in this paper are not arithmetic slips. They come from a wrong picture of the structure, a reversed implication, an order that does not matter, or a percentage read against the wrong base.

Work through the lessons in order. Each lesson depends on the ones before it, and each ends with a few original items that test the method and its typical failure, not the memory of a term. Attempt each item before you open its explanation.

Your personal target is a learning goal, not an official cut-off. The timed-set section explains how to use it.

## Roadmap

| # | Lesson | Stage | Depends on | Practice items |
|---:|---|---|---|---:|
| 1 | Conditional logic and implication chains | Foundation | None; start here | 3 |
| 2 | Syllogisms, statement sets and truth-teller logic | Core | Lesson 1 | 2 |
| 3 | Series, analogies and figural sequences | Foundation | Lessons 1 and 2 | 3 |
| 4 | Coding, decoding and alphametics | Core | Lessons 1 and 3 | 2 |
| 5 | Directions, distance and directed networks | Foundation | Lesson 1 | 2 |
| 6 | Blood relations and family graphs | Core | Lesson 2 | 3 |
| 7 | Ranking, ordering and comparison chains | Core | Lessons 1 and 2 | 2 |
| 8 | Seating and arrangement | Core | Lessons 6 and 7 | 3 |
| 9 | Logic grids and matching structures | Core | Lessons 6 and 7 | 2 |
| 10 | Counting arrangements: permutations, restrictions and codes | Core | Lessons 3 and 5 | 3 |
| 11 | Counting selections: combinations, partitions and routes | Core | Lesson 10 | 2 |
| 12 | Sets, overlap and inclusion-exclusion | Core | Lesson 11 | 2 |
| 13 | Probability, worst cases and weighing strategies | Core | Lessons 10 and 11 | 3 |
| 14 | Plane-figure counting | Core | Lessons 10 and 11 | 2 |
| 15 | Solid and cube counting | Core | Lessons 3 and 14 | 3 |
| 16 | Data interpretation I: levels, changes and shares | Core | Lessons 10 and 12 | 2 |
| 17 | Data interpretation II: pies, dual axes and weighted scores | Core | Lesson 16 | 2 |
| 18 | Decision scenarios and the decision procedure | Core | Lessons 2 and 9 | 3 |

After the eighteen lessons come the verified PYQ linkage and answer-approach section, six cumulative items that join two or more methods, the timed-set routine, remediation, the master method maps, the consolidated register notes, the coverage matrix and the source list.

---

## Lesson 1 - Conditional logic and implication chains

Progress: Lesson 1 of 18 | Stage: Foundation | Subtopic: Conditional logic and implication chains

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You are handed three or four sentences that begin with "if", "unless" or "only if", and then asked which claim "must follow", which "may be true", or which "is not necessarily true". The sentences look simple. The trap is that the mind reads every "if" sentence as working in both directions, and it treats "not necessary" as if it meant "false". This lesson gives you a small, reliable machine for these items: write each sentence as an arrow, write its mirror-safe partner beside it, join arrows into chains, and test claims by trying to break them.

### Visual: one arrow, its safe partner, and the two unsafe readings

```text
            GIVEN LINK                    SAFE PARTNER (always valid)
     A  ───────────────►  B          not B  ───────────────►  not A
   "if A then B"                     "if not B then not A"   (contrapositive)

   ┌──────────────────────── NOT FREE ────────────────────────┐
   │  B  ──?──►  A        converse   "if B then A"           │
   │  not A ──?──► not B  inverse    "if not A then not B"   │
   │  Why not free: A is ONE way to reach B. B may also be    │
   │  reached by another road C, so seeing B tells you        │
   │  nothing about which road was used.                      │
   │                                                          │
   │        A ────┐                                           │
   │              ├────►  B                                   │
   │        C ────┘                                           │
   └──────────────────────────────────────────────────────────┘

   CHAINING:  A ──► B ──► C        gives   A ──► C
   partners:  not C ──► not B ──► not A    gives   not C ──► not A
```

Read the top line first. A given link is a one-way arrow. Its contrapositive, drawn on the right, runs backwards with both ends negated, and it says exactly the same thing in different words. The panel in the middle shows why the two other readings fail. If both A and C lead to B, then finding B does not tell you that A happened, and finding "not A" does not stop B from happening through C. The last two lines show chaining: arrows that meet end to start can be joined, and their partners join in the reverse order.

### A one-way door, in plain words

Think of an "if A then B" sentence as a one-way door from room A into room B. Anyone in room A can pass into B. That is all the sentence promises. It does not say that everyone in room B came through that door; other doors may open into B. It also does not say that people outside A stay out of B.

What the door does guarantee is this: if someone is not in room B, they were never in room A, because anyone in A would have been carried into B. That backward guarantee is the contrapositive. It is not a new fact. It is the same door seen from the other side.

The analogy has a limit. Real doors can be locked or broken, but a logical arrow never fails. Once the sentence is given as true, every case of A is a case of B, with no exceptions.

### Reading an arrow: sufficient, necessary and "if and only if"

Two technical words describe the two ends of an arrow.

- **Sufficient condition.** In "if A then B", A is sufficient for B. Having A is enough to guarantee B.
- **Necessary condition.** In the same sentence, B is necessary for A. You cannot have A without B.

So one arrow carries two descriptions. "Passing the entry test is necessary for admission" means admission -> passed the test. It does not mean that passing the test guarantees admission.

An **implication** is a one-way arrow, A -> B. An **equivalence**, written A <-> B and read "A if and only if B", is two arrows at once: A -> B and B -> A. Only with an equivalence may you swap the two sides freely.

| Relation | Symbol | What you may deduce |
|---|---|---|
| Implication | A -> B | A is sufficient for B; B is necessary for A; the contrapositive not B -> not A is free |
| Equivalence | A <-> B | Both directions hold; A and B can replace each other |

**Failure condition.** The arrow reading fails when you place the arrow the wrong way round. The words "only if" are the usual cause. "A only if B" means A -> B, because B is the only route by which A can happen. "A if B" means B -> A. Before drawing any arrow, find which side is the condition that guarantees the other.

### Translating the English forms into arrows

The paper rarely writes "if A then B" plainly. Translate each form before you reason.

```text
ENGLISH FORM                        ARROW              NOTE
"If A, then B"                      A -> B
"A only if B"                       A -> B             B is the gate A must pass
"B if A"                            A -> B             the condition follows "if"
"No A without B"                    A -> B             same as "A only if B"
"Every A is B" / "All A are B"      A -> B             set language for the same arrow
"A unless B"                        not B -> A         equivalently: not A -> B
"Either A or B (or both)"           not A -> B         and not B -> A
"A if and only if B"                A <-> B            two arrows
```

Two of these deserve a worked example.

**"Unless."** "The meeting will be postponed unless the chairperson arrives." If the chairperson does not arrive, the meeting is postponed: not arrives -> postponed. Its contrapositive is: not postponed -> arrived. Notice what is not given. If the chairperson does arrive, the sentence does not say the meeting goes ahead; it may still be postponed for another reason.

**"Either-or."** "Each visitor shows either a pass or an identity card." Any visitor without a pass must show an identity card: not pass -> card. Equally, not card -> pass. In ordinary logic "or" is inclusive: a visitor who shows both still satisfies the sentence. Treat "or" as exclusive only when the stem says "but not both".

What this establishes: every common English form reduces to one or two arrows. Where it stops: the translation table is for statements about conditions. Sentences with "some" or "most" are not arrows at all; they need set diagrams instead of arrows.

### Method 1: the arrow and its contrapositive

**Rule.** Write each given sentence as A -> B. Immediately write not B -> not A beside it. These two lines, and nothing else, are what one sentence gives you.

**Worked example.** "If the generator fails, the lift stops." So fails -> stops, and not stops -> not fails. You are told that the lift is running. Running means not stopped, so by the contrapositive the generator has not failed.

Now a second fact: "the lift has stopped". Nothing follows about the generator. The lift could have stopped for a power cut, a fault in the motor, or routine maintenance. Concluding "the generator failed" would be the converse, stops -> fails, which was never given.

What this establishes: a negated consequence (the "then" part) lets you negate the condition. Where it stops: an affirmed consequence, or a negated condition, tells you nothing.

**Failure condition.** The method fails when the contrapositive is formed by negating only one side, or by negating without reversing. "Not fails -> not stops" is the inverse, not the contrapositive. Both ends must be negated and their order must be reversed.

### The converse trap

The single most common error in this family is to read A -> B as B -> A. It is tempting because many everyday sentences happen to work both ways ("if it is a square then it has four equal sides and four right angles" is often reversible in ordinary talk). But the paper gives one-way sentences on purpose.

**Worked example.** "Every registered voter in this ward has an identity card." Does it follow that every person with an identity card in this ward is a registered voter? No. Children over a certain age, non-residents and people who have not registered may all hold cards. The sentence placed voters inside card-holders; it did not say card-holders sit inside voters.

The **inverse**, not A -> not B, fails for the same reason. "A person who is not a registered voter has no identity card" is not given. In fact the inverse is the contrapositive of the converse, so it stands or falls with the converse.

**Failure condition for spotting the trap.** The converse becomes valid only when the stem itself supplies the reverse arrow, for example with "if and only if", "only those who", or a second sentence stating B -> A. If you cannot point to that reverse sentence, the converse is not available.

### Method 2: chaining arrows (transitivity)

**Transitivity** means that arrows that meet can be joined. From A -> B and B -> C you may conclude A -> C.

**Worked example (original).** Every falcon in the sanctuary is ringed. Every ringed bird is logged in the register. Every logged bird is inspected each month. Then:

- every falcon is logged (falcon -> ringed -> logged);
- every falcon is inspected each month (the full chain);
- any bird not inspected is not a falcon (the contrapositive of the full chain);
- it does not follow that every inspected bird is a falcon (converse of the chain).

**Teaching example: scholarship holders.** Given "Every scholarship holder is a hosteller" and "Every hosteller is a registered student", test three claims.

1. Every scholarship holder is a registered student. This follows, by chaining the two arrows.
2. Every registered student is a hosteller. This does not follow; it is the converse of the second sentence.
3. Someone who is not a registered student is not a scholarship holder. This follows; it is the contrapositive of claim 1.

So claims 1 and 3 follow and claim 2 does not. The only valid moves from one-way sentences are chaining and contraposition.

What these examples establish: a chain of any length collapses into one arrow from its first term to its last, and that arrow has its own contrapositive. Where they stop: the chain says nothing about the reverse direction, and nothing about members that enter the chain halfway.

**Failure condition.** Chaining fails when the middle terms do not match exactly. "Every falcon is ringed" and "every bird ringed before 2020 is logged" cannot be chained, because "ringed" and "ringed before 2020" are different classes. Chaining also fails when a link is not a full arrow: "most ringed birds are logged" or "some ringed birds are logged" cannot carry a falcon all the way through.

### Possible, certain and "not necessary"

Statement items use three verdict words. Keep them apart.

| Verdict | Meaning | How you settle it |
|---|---|---|
| Possible | At least one case consistent with all the statements makes the claim true | Build one such case |
| Certain, or must be true | Every consistent case makes the claim true | Show that its denial leads to a contradiction |
| Not necessary | At least one consistent case makes the claim false | Build one consistent case where it fails |

"Possible" and "probable" are different ideas. An event can be possible and very unlikely. In statement logic you never need a probability. "It is not necessary that Y is true" does not say that Y is false. It says only that Y can fail in some consistent case.

**Worked example.** Given: "if a file is urgent, it is flagged". Is it necessary that a flagged file is urgent? Build a case: a file flagged for being misplaced, not urgent. Every given sentence still holds. So "a flagged file is urgent" is not necessary. You did not need to show that flagged files are usually not urgent; one counter-case is enough.

**Failure condition.** A counter-case counts only if it obeys every given statement. A case that breaks one of the premises proves nothing, because the premises are assumed true. Check each premise against your counter-case before you use it.

### Method 3: test a claim by assuming its denial

To decide whether "if P then Q" must hold, do not hunt for a truth table. Assume the one situation that would break the claim, P true and Q false, and follow the arrows. If you reach a contradiction, the breaking situation cannot occur, so the claim holds. If you reach a full, consistent case, that case is your counter-example and the claim is not necessary.

**Worked example (original).** Given: (i) if the audit is late, the bonus is withheld; (ii) if the bonus is withheld, morale falls; (iii) if morale falls, attrition rises. Claim: "if attrition does not rise, the audit was not late". Assume the denial: attrition does not rise, and the audit was late. Late -> withheld -> falls -> rises. That contradicts "attrition does not rise". So the claim holds.

What this establishes: one assumed denial and one run along the arrows decides a claim. Where it stops: if the run ends without a contradiction, you must still check that the case you built satisfies every statement before calling it a counter-case.

**Failure condition.** The method fails when you assume the claim itself instead of its denial. Assuming P and Q true and finding no contradiction proves nothing, because a claim can be consistent without being forced.

### Advanced: implication chaining across negated links

Advanced. Real items mix positive and negative links, and the arrows then pass through negations. The rule is unchanged: each link gives its contrapositive, and arrows that meet may be joined. The converse and the inverse are never free, however many links there are.

```text
  (i)   not K ──► M              partner:  not M ──► K
  (ii)  M ──► not N              partner:  N ──► not M
  (iii) not L ──► N              partner:  not N ──► L
```

Write all six lines before reasoning. Two arrows meet when the end of one is exactly the start of another, including its sign. "M" and "not M" are different nodes.

**Worked derivation.** Test the claim "if L is false, then K is true".

1. Start at the node "not L". Line (iii) carries it to N.
2. Look for an arrow that starts at N. The partner of (ii) does: N leads to not M.
3. Look for an arrow that starts at "not M". The partner of (i) does: not M leads to K.
4. The joined chain is not L -> N -> not M -> K. The claim holds.

Now run the same chain backwards with every sign flipped: not K -> M (line i), M -> not N (line ii), not N -> L (partner of iii). That gives "if K is false, then L is true", which is simply the contrapositive of the first result, so no new work was needed.

A third claim, "if K is true, then L is false", looks similar but is the converse of the first result. One consistent case breaks it: K true, L true, M false, N false. Check each line: (i) needs nothing because K is true; (ii) needs nothing because M is false; (iii) needs nothing because L is true. All three links hold, and the claim fails, so it is not necessary.

**Failure condition.** Chaining across negations fails when a sign is dropped while copying. Writing "M -> N" for "M -> not N" turns a valid derivation into an invalid one. Copy each node with its sign, and circle every "not".

### Advanced Method 4: solve conditional chains backwards

Advanced. When an item gives several links and asks which claims follow, work backwards from the claim.

```text
1. Write every link as an arrow:            A -> B
2. Write the contrapositive beside it:      not B -> not A
3. To test "if P then Q", ASSUME P and not Q, then chain to a contradiction.
4. To test "it is not necessary that Q", find ONE consistent case with Q false.
```

**Worked example.** Four claims E, F, G and H satisfy: (i) if E is true, F is true; (ii) G is true only if F is false; (iii) if H is false, G is true. Translate (ii) first: "G only if not F" is G -> not F, with partner F -> not G.

- Does "if E is true, then H is true" hold? Assume the denial: E true and H false. From H false, (iii) gives G true, and (ii) then gives F false. From E true, (i) gives F true. F cannot be both true and false, so the denial is impossible and the claim holds. Notice that the contradiction came from two chains meeting at F, one from each half of the denial.
- Must E be false whenever H is true? Look for one consistent case with H true and E true: take F true and G false. Then (i) holds (E and F both true), (ii) holds (G is false, so it demands nothing), and (iii) holds (H is true, so it demands nothing). Every link survives, so "H true forces E false" is not necessary.

Only chaining and contraposition were used. Two arrows and one contradiction usually beat a full truth table under exam time.

What this establishes: a claim of the form "if P then Q" is tested by one assumed denial; a claim of the form "not necessary" is tested by one consistent counter-case. Where it stops: if the links contain "or" or "unless", translate them into arrows first (see the table above); the backward method works only on arrows.

**Failure condition.** The backward method fails when the assumed denial is written wrongly. The denial of "if P then Q" is "P and not Q", not "not P and Q". Write the denial in words before chaining.

### Falsifying an either-or claim

An "either-or" claim about a group, such as "every member either paid online or paid at the counter", is a universal claim with an inclusive "or". Translate it as: for each member, not online -> counter.

A universal claim is broken by one member who fails it. A member fails "online or counter" only when both parts are false. So the single finding that falsifies the claim is a member who paid neither online nor at the counter.

Three findings look damaging but do not falsify it:

- a member who paid online but not at the counter (one part true is enough);
- a person outside the group who paid neither way (the claim is only about members);
- the fact that most members chose one method (a universal claim is not about proportions).

**Failure condition.** This reasoning assumes the inclusive "or". If the stem says "either ... or ..., but not both", a member who did both would also falsify the claim. Read the stem for the exclusive wording before deciding.

### Checking a set of statements for consistency

Some items ask whether several statements can all be true together, or which added statement would make the set inconsistent. A set is **consistent** if at least one situation makes every statement true at once.

**Worked example (original).** (i) If the shop opens early, the bakery opens early. (ii) If the bakery opens early, the street is cleaned by seven. (iii) The street is not cleaned by seven. Can the shop open early? Chain (i) and (ii): early shop -> street cleaned by seven. With (iii), the contrapositive gives: the shop does not open early. Adding "the shop opens early" would make the set inconsistent.

**Failure condition.** You may declare a set consistent only after you have written out one complete case that satisfies every statement. Not finding a contradiction quickly is not the same as showing that none exists.

### Reading by feel, and why it fails

The tempting method is to "feel" which claim sounds natural, or to read each "if" sentence as a two-way rule because that is how everyday speech often works. It feels efficient. In this family it is the main source of wrong answers, because the options are built from the converse and the inverse.

The reply has two parts. First, write each sentence as a one-way arrow and its contrapositive, and refuse every other line. Second, settle "must" claims by contradiction and "not necessary" claims by a single consistent counter-case. This takes perhaps twenty seconds longer and removes the converse trap completely.

A second tempting method is to draw a full truth table for four claims (sixteen rows). It is valid, but slow, and copying errors creep in. The reply is the backward method: one assumed denial and one chain usually decide the claim.

### Look-alike readings to keep apart

- Contrapositive versus inverse: both negate, but only the contrapositive also reverses the order.
- "A only if B" versus "A if B": the first is A -> B; the second is B -> A.
- "Not necessary" versus "false": the first needs one failing case; the second needs every case to fail.
- Possible versus probable: possible needs one case; probable is about frequency, which statement logic never asks.

### UPSC application

The paper uses this method in four related families.

- **Conditional logic conclusion.** Several "if" links are given, and you choose the conclusion that follows. Write every arrow with its contrapositive, chain them, and reject the options that are converses or inverses.
- **Implication consistency.** You decide whether a set of statements can hold together, or which conclusion is consistent with them. Build one complete case, or chain to a contradiction.
- **Falsifying an either-or claim.** You choose the single observation that would show a universal "or" claim to be false. Look for the member for whom both parts fail, and ignore findings outside the stated group.
- **Statement-implication logic (2026 Q36, provisional).** Several statements are tied together by conditional links, and claims of the form "if P then Q" and "it is not necessary that Q" must be judged. Use the backward method: arrows, partners, an assumed denial for each "if" claim, and a single counter-case for each "not necessary" claim.

The common traps across all four are the converse, the inverse, a dropped "not", and treating "not necessary" as "false".

### Revision points

- Write every "if A then B" as A -> B, and write the contrapositive not B -> not A beside it.
- The converse (B -> A) and the inverse (not A -> not B) are never given by a one-way sentence.
- A is sufficient for B; B is necessary for A. "A only if B" means A -> B.
- "A unless B" means not B -> A; "either A or B" means not A -> B, with "or" inclusive unless the stem says "not both".
- Arrows chain when the end of one exactly matches the start of the next, including its "not".
- A chain of any length gives one arrow from its first term to its last, plus that arrow's contrapositive.
- To show "if P then Q" must hold, assume P and not Q and reach a contradiction.
- To show a claim is "not necessary", build one consistent case in which it fails; check every premise against that case.
- "Possible" needs one consistent case; "certain" needs every case; neither needs a probability.
- A universal either-or claim is falsified only by a member for whom both parts fail.
- A set of statements is consistent only when you can write one complete case satisfying all of them.
- Advanced: two arrows and one contradiction usually beat a sixteen-row truth table.

### Practice

**MCQ 1**

Two rules apply at a dam. If the reservoir overflows, its gates are opened. If the gates are opened, the lower road is closed. Today the gates were not opened. Which of the following must be true?

- A. The reservoir did not overflow today.
- B. The lower road was not closed today.
- C. Whether the reservoir overflowed today cannot be decided.
- D. No heavy rain fell over the catchment today.

**MCQ 1 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The first rule is overflow -> gates opened. Its contrapositive is gates not opened -> no overflow. The gates were not opened, so the reservoir did not overflow. This is the only option forced by the two rules and the fact.
- **B — Incorrect:** This uses the inverse of the second rule, gates not opened -> road not closed. The rules allow the road to be closed for some other reason, so "the road was not closed" is possible but not necessary.
- **C — Incorrect:** This handles a denied consequence as if it were an affirmed one. Seeing the "then" part happen leaves the "if" part open, but seeing it fail settles the "if" part through the contrapositive; here it fails, so the verdict "cannot be decided" is wrong.
- **D — Incorrect:** This imports a link that was never stated, heavy rain -> overflow, and then uses its contrapositive. Without that sentence, nothing about rain follows, so the verdict "no heavy rain" rests on an unstated premise.

**MCQ 2**

A recruiter states a rule: "An applicant is shortlisted only if she holds a degree or has at least five years of experience." The "or" in the rule includes the case of having both. Which single finding would show that the rule was broken?

- A. An applicant with a degree and five years of experience who was not shortlisted
- B. A shortlisted applicant with neither a degree nor five years of experience
- C. A shortlisted graduate who also has five years of experience
- D. A shortlisted graduate with only three years of experience

**MCQ 2 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** This reads "only if" as "if", turning the rule into qualified -> shortlisted. The rule is shortlisted -> (degree or experience); it never promises a place to a qualified applicant, so this applicant does not break it.
- **B — Correct:** "Shortlisted only if degree or experience" is the arrow shortlisted -> (degree or experience). Its contrapositive is (no degree and no experience) -> not shortlisted. A shortlisted applicant with neither qualification is exactly the case the contrapositive forbids, so this one finding breaks the rule.
- **C — Incorrect:** This reads the "or" as exclusive, as if holding both qualifications were not allowed. The stem says the "or" includes both, so this applicant satisfies the rule twice over.
- **D — Incorrect:** This reads "or" as "and", demanding both qualifications. The degree alone satisfies the condition, so the missing two years of experience do not matter.

**MCQ 3**

Three rules govern a software release. (i) The release goes ahead only if testing is complete. (ii) Testing is complete unless the budget is cut. (iii) If the budget is cut, a hiring freeze is announced. No hiring freeze was announced. Which of the following must be true?

- A. The budget was not cut, and the release goes ahead.
- B. The budget was not cut, but testing may still be incomplete.
- C. The budget was not cut, and testing is complete.
- D. The budget was cut; testing may be incomplete.

**MCQ 3 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** The first half is right, but "the release goes ahead" uses the converse of rule (i). Rule (i) is release -> testing complete; knowing that testing is complete does not force the release, and a case with testing complete and no release satisfies all three rules.
- **B — Incorrect:** This misreads rule (ii) as "if testing is complete, the budget was not cut", an arrow pointing the wrong way. The correct translation is not cut -> testing complete, so once the budget is known to be uncut, testing cannot be incomplete.
- **C — Correct:** Rule (iii) is cut -> freeze, with contrapositive no freeze -> not cut. Rule (ii), "testing is complete unless the budget is cut", is not cut -> testing complete. No freeze was announced, so the budget was not cut, and so testing is complete. Assuming either half false contradicts a rule, so both halves must hold.
- **D — Incorrect:** This forms the contrapositive of rule (iii) with a dropped "not", writing no freeze -> cut. With that slip the budget appears cut, rule (ii) then says nothing, and testing looks open; the correct contrapositive gives "not cut".

---

## Lesson 2 - Syllogisms, statement sets and truth-teller logic

Progress: Lesson 2 of 18 | Stage: Core | Subtopic: Syllogisms, statement sets and truth-teller logic

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Here the paper hands you two or three short statements ("all X are Y", "some Y are Z", "no Z is W"), or a few sentences about people, habits or groups, and asks which conclusions "definitely follow". In a third kind of item, several people make statements and you are told how many of them speak the truth. In all three, the statements might be about absurd things, such as cats being chairs, or about believable things, such as athletes eating well. Your job is the same in every case: decide what is forced by the statements, and ignore what you happen to believe about the world.

The previous lesson gave you arrows for "if ... then" sentences. This lesson adds pictures for "all", "some" and "no", a way to test conclusions by trying to break them, and a disciplined way to handle speakers who may be lying.

### Part A - Set containment and the counter-diagram

### Visual: the four statement forms and what each picture forbids

| Statement | Plain meaning | Picture | What it forbids | What it does not say |
|---|---|---|---|---|
| All A are B | A sits wholly inside B | circle A drawn inside circle B | any A outside B | whether every B is an A |
| No A is B | A and B do not touch | two separate circles | any member in both | anything about the size of A or B |
| Some A are B | at least one member is in both | two overlapping circles, overlap marked with a dot | an empty overlap | whether some A are outside B |
| Some A are not B | at least one A lies outside B | overlap or separation, with a dot in the part of A outside B | every A being inside B | whether any A is inside B |

```text
  All A are B            No A is B            Some A are B          Some A are not B
  ┌─────────B──┐        ┌──A──┐  ┌──B──┐      ┌──A──┬──┬──B──┐      ┌──A──┬──┬──B──┐
  │  ┌──A──┐   │        │     │  │     │      │     │• │     │      │  •  │  │     │
  │  └─────┘   │        └─────┘  └─────┘      └─────┴──┴─────┘      └─────┴──┴─────┘
  └────────────┘                               dot = "at least one"   dot outside B
```

**Working assumption for this lesson.** Every group that a statement names is taken to have at least one member. So if a statement mentions tutors, there is at least one tutor. Every diagram, conversion and verdict below uses this assumption. If a stem says that a group may be empty, drop the assumption, and drop with it every conclusion that needed a member to exist.

Read the table row by row. Each statement does one job: it forbids a region, or it puts a member (a dot) into a region. Everything it does not mention stays open. The pictures underneath show the minimum each statement commits you to. A dot means "at least one member is here". An empty region in a picture is not a claim that it is empty; it is only a region the statement says nothing about, unless the statement explicitly forbids it.

### Fences in a field: the picture behind the forms

Imagine each word, such as "tutors" or "referees", as a fenced field of people. "All tutors are graders" moves the tutors' fence inside the graders' field. "Some graders are authors" says that at least one person stands where those two fields overlap. A conclusion follows only if every possible way of drawing the fences, consistent with the statements, puts people where the conclusion says.

The analogy has a limit: real fields have fixed sizes, but statement circles can be drawn as large or small as you like, as long as each statement is obeyed. That freedom is exactly what you use when you look for a counter-diagram.

### The doctrine: a conclusion must hold in every arrangement

A **syllogism** is an argument with statements (premises) about groups and a conclusion about groups. A conclusion is **valid** only if it is true in every diagram that satisfies all the premises. It is not enough that it is true in the first diagram you draw.

A **counter-diagram** is one diagram that satisfies every premise and makes the conclusion false. Finding one counter-diagram disproves the conclusion.

**Method A: one diagram, then hunt for a counter-diagram.**

1. Draw one diagram that satisfies every premise.
2. Read off the candidate conclusion.
3. Redraw the circles, as freely as the premises allow, to try to make the conclusion false.
4. If you cannot break it without breaking a premise, it follows. If you can, it does not.

**Failure condition.** The method fails when your counter-diagram quietly breaks a premise. Before you reject a conclusion, re-check each premise against the counter-diagram. It also fails when you draw only the "natural" picture, such as overlapping circles for every pair, and accept whatever that picture shows.

### Safe conversions and unsafe ones

Some statements can be turned round; others cannot.

```text
  SAFE                                         UNSAFE
  No A is B      ->  No B is A                 All A are B   ->  All B are A     (converse)
  Some A are B   ->  Some B are A              Some A are B  ->  Some A are not B
  All A are B    ->  Some B are A *            Some A are not B -> Some B are not A
  * uses this lesson's working assumption that every named group has a member
```

"Some A are B" does not give "some A are not B". Existential statements, which say that something exists, do not license their negatives. If at least one tutor is a poet, it is still possible that every tutor is a poet.

### Worked example 1: "some" is not "all"

Statements: All painters are musicians. Some musicians are teachers.
Conclusion I: Some painters are teachers. Conclusion II: Some teachers are musicians.

- Conclusion II follows by the safe conversion of "some musicians are teachers".
- For conclusion I, draw a first diagram with the teachers overlapping the painters inside the musicians. It looks true. Now look for a counter-diagram: let the teachers overlap only the part of the musicians' circle outside the painters. Both statements still hold, and no painter is a teacher. So I does not follow.

What this establishes: a conclusion that is true in one diagram may fail in another. Where it stops: the conclusion "some painters are teachers" is still possible; it simply is not forced.

### Worked example 2: universal negatives chain cleanly

Statements: All clerks are typists. No typist is a manager.
Conclusion: No clerk is a manager. Every clerk is inside the typists, and no typist touches the managers, so no clerk can touch the managers. You cannot draw a counter-diagram. It follows.

The same shape appears with diploma holders. Given "every diploma holder is a graduate" and "no graduate is under 18": (i) "no diploma holder is under 18" follows, because diploma -> graduate and graduate -> not under 18 chain to diploma -> not under 18; (ii) "every graduate is a diploma holder" does not follow, because it is the converse of the first statement.

What these establish: "All A are B" plus "No B is C" always gives "No A is C". Where they stop: they give nothing about whether all graduates are adults, or whether any manager is a clerk's relative; only the stated groups are linked.

### Worked example 3: the arrow form of the same idea

"If a file is approved, it is signed" and "this file is not signed". In set language: approved files sit inside signed files; this file is outside the signed circle; so it is outside the approved circle. The file was not approved. That is the contrapositive from the previous lesson. It does not follow that a signed file was approved; that would be the converse.

The scholarship-holder example from the previous lesson can be redrawn in the same way: scholarship holders inside hostellers inside registered students. "Every scholarship holder is a registered student" follows; "every registered student is a hosteller" does not.

**Failure condition for set chaining.** Chaining with circles fails when the middle group is not the same group. "All painters are musicians" and "some violinists are teachers" share no middle group, so nothing links painters to teachers.

### The "either-or" pair of conclusions

Sometimes two conclusions such as "some A are B" and "no A is B" are each not forced, yet exactly one of them must be true, because they contradict each other and together cover every possibility. Many options then read "either I or II follows".

**Rule.** Two conclusions form an either-or pair when they have the same subject and predicate and are contradictory: "some A are B" with "no A is B"; "all A are B" with "some A are not B".

**Failure condition.** The pair test fails when the two conclusions are only contrary, not contradictory. "All A are B" and "no A is B" can both be false at once (when some A are B and some are not), so they are not an either-or pair.

### Advanced: syllogism validity by counter-diagram, and the traps that go with it

Advanced. When three or four premises interact, do not trust the first diagram. For each conclusion, ask: "Can I redraw so that this fails?" The advanced traps in this family are:

- reporting a placement true in one arrangement when the statements allow several; report only what is true in all of them;
- accepting a conclusion because it sounds right or matches the real world;
- reading "all A are B" as "all B are A";
- treating "some A are B" as if it also gave "some A are not B".

**Failure condition.** An advanced counter-diagram must still give every "some" statement its dot. A redraw that empties a region marked by a "some" premise is not allowed.

### Part B - Multi-statement and multi-conclusion sets

### Visual: a chain flow across statements

```text
  S1: All P are Q  ───►  S2: All Q are R  ───►  S3: No R is T
          │                     │                    │
          ▼                     ▼                    ▼
   P inside Q            Q inside R           R and T disjoint
          └──────────── chain ──────────────────────┘
                 P inside Q inside R, R apart from T
          (working assumption: P, Q, R and T each have a member)
                             │
     ┌───────────────┬───────┴────────┬──────────────────┐
     ▼               ▼                ▼                  ▼
 "No P is T"   "Some R are P"   "Some T are not Q"   "Some R are not Q"
   follows        follows           follows            NOT forced:
                 (P has a        (T has a member,     Q may fill the
                  member, and     and every T lies     whole of R
                  P sits in R)    outside R, so
                                  outside Q)
```

Follow the chain from left to right: each statement is turned into a containment or a separation, and the chain is read only along links that share a middle group. Then each candidate conclusion is checked against that chain. The first three follow: two of them need a member to exist, and the working assumption supplies one. The fourth looks just as natural, but a counter-diagram in which Q and R are the same circle obeys every statement and leaves no R outside Q, so it is not forced.

### Why long statement sets invite mistakes

When there are several statements and several conclusions, the danger is fatigue. You read the first conclusion carefully, then judge the rest by feel. The cure is mechanical: draw the chain once, then test every conclusion against the same picture, and against its best counter-picture.

### Method B: chain once, test each conclusion separately

1. Turn each statement into a containment, a separation or a dot.
2. Join statements that share a middle group, in a single chain or tree.
3. For each conclusion, find the shortest path in the chain that would prove it, and then try a counter-diagram.
4. Mark each conclusion "follows", "does not follow", or "either-or with another".

**Failure condition.** Method B fails when two statements are joined through a word that changes meaning, such as "swimmers" in one statement and "competitive swimmers" in another.

### Statement-conclusion items with everyday content

Many items use believable statements: people who meditate and aggression, athletes and diet, singers and practice, morning walkers, supporters of a political party, colour preferences. The same rule applies: a conclusion follows only if the statements force it.

**Worked example (original).** Statements: "Every member of the chess club practises daily. Some people who practise daily are students."
Conclusion I: "Some chess club members are students." Conclusion II: "Anyone who does not practise daily is not a chess club member."

- I does not follow: the students who practise daily may all be outside the club.
- II follows: it is the contrapositive of the first statement.

Real-world knowledge can tempt you either way. You may believe that most club members are students, but the statements do not say so.

**Rule for causal wording.** A conclusion such as "meditation reduces aggression" or "practice improves the voice" is causal. Statements that report that two things go together ("all who meditate are calm") support only the stated containment, not a cause. Accept a causal conclusion only if a statement asserts the cause.

**Failure condition.** The everyday-content method fails when you bring in a fact that seems like common knowledge. If a conclusion needs a fact not in the statements, it does not follow, however true it is.

### Finding a cause from a table of cases

Some items describe several cases, say what was present in each, and ask what definitely caused an outcome. Lay the cases out in a grid, and treat each new case as a chance to eliminate a candidate.

**Worked example (original).** A workshop logs, batch by batch, three settings and whether the finished parts were defective. The manager wants the single setting responsible.

| Batch | Fast cutting speed | New supplier's steel | Night shift | Defective |
|---|---|---|---|---|
| 1 | yes | yes | yes | yes |
| 2 | no | yes | yes | yes |
| 3 | yes | no | no | no |

**Rule.** A single cause must be present in every case where the outcome occurred and absent in every case where it did not (assuming one cause, acting reliably).

- Fast cutting speed fails: batch 2 was defective without it, and batch 3 had it without defects.
- New supplier's steel fits: present in batches 1 and 2, absent in batch 3.
- Night shift also fits: present in batches 1 and 2, absent in batch 3.

After three batches the cause is not fixed, because two settings match the pattern equally. A fourth batch separates them:

| Batch | Fast cutting speed | New supplier's steel | Night shift | Defective |
|---|---|---|---|---|
| 4 | no | no | yes | no |

The night shift was present in batch 4 and the parts were fine, so the night shift is eliminated. Under the one-cause assumption, the new supplier's steel is the cause.

What this establishes: the grid turns a story into an elimination, and a "definitely" verdict needs every rival to be eliminated, not just the first one. Where it stops: if two candidates are still tied when the cases run out, the cause is not fixed, and a "definitely" conclusion does not follow.

**Failure condition.** The method fails when the stem does not support the one-reliable-cause assumption, for example when it says "some batches with the new steel were defective". Then presence in every defective case is not required, and elimination by a single clean case is not valid.

### Case-split deduction: who must have stayed, who must be male

Some items give conditions about a group, such as who went out, who stayed home, or who in a group is male, and ask who definitely meets a description.

**Worked example (original).** Of four flatmates, F, G, H and J, at least two went to a concert. If F went, G stayed home. If H stayed home, J went. G went. Who definitely went?

- G went, so by the contrapositive of the first rule, F did not go (F went -> G stayed; G did not stay -> F did not go).
- At least two went. F did not, G did. So at least one of H and J went.
- If H stayed home, J went; if H went, J may or may not have gone. Cases: (H went, J went), (H went, J stayed), (H stayed, J went). All satisfy every condition.

So only G definitely went, and F definitely stayed home. H and J are each possible but not certain.

**Method C: split on the least-fixed person and keep only common facts.** List every case consistent with all conditions. A fact is definite only if it is true in every case.

**Failure condition.** The method fails when one consistent case is missed. Before reporting a definite fact, check that your list of cases is complete, splitting on one undecided person at a time.

### Sufficiency of a statement set

A **statement sufficiency check** asks whether the given statements are enough to establish a conclusion. Treat it like a validity test: sufficient means the conclusion holds in every consistent arrangement. One consistent arrangement where it fails shows the statements are not sufficient.

**Worked example (original).** Target conclusion: "No intern is a manager." Three statements are offered: (1) All interns are trainees. (2) No trainee is a manager. (3) Some managers are mentors.

- Statement 1 alone: interns sit inside trainees, but nothing keeps managers away from trainees. Draw the managers overlapping the interns; statement 1 still holds. Not sufficient.
- Statement 2 alone: trainees and managers are apart, but interns may lie outside the trainees and overlap the managers. Not sufficient.
- Statement 3 says nothing about interns at all, so it cannot help, alone or with either of the others.
- Statements 1 and 2 together: interns inside trainees, trainees apart from managers, so no intern can be a manager. No counter-diagram exists. Sufficient.

So the smallest sufficient set is statements 1 and 2. Adding statement 3 changes nothing.

**Failure condition.** Sufficiency is judged for the statements given, not for statements you add. If you find yourself adding "and presumably", the statements were not sufficient.

### The job each statement does: supports, weakens or unrelated

Some items do not ask what follows. They print a conclusion and several statements, and ask which statement would best strengthen or weaken it, or how each statement bears on it. Picture the conclusion as a target card, and each statement as a card that may push on it.

```text
  supporting card ──raises──►  CONCLUSION  ◄──lowers──  weakening card

  test each card against the conclusion:
   does it bear on the conclusion's exact link?  ── no ──►  "unrelated"
        │ yes
   if the card were true, would the conclusion become
   more believable (supports) or less believable (weakens)?
   how hard does it push: on the key link, or only on an edge?
   does the order of events still allow the stated cause?
```

- A **conclusion** is the position the passage argues for, often a cause ("X led to Y") or a recommendation.
- A statement **supports** the conclusion if, were it true, the conclusion would become more believable.
- A statement **weakens** the conclusion if, were it true, the conclusion would become less believable, for example by naming another cause or a cost.
- A statement is **unrelated** when its truth would leave the conclusion exactly as believable as before; sharing a word or a broad topic with the conclusion is not enough to bear on it.

**Worked example (original).** A college canteen cut the price of its lunch at the start of July, and its July lunch sales were a third higher than June's. Conclusion: "The price cut caused the rise in lunch sales." Choose the statement that would best strengthen the conclusion and the one that would best weaken it. (i) "In July the hostel kitchen closed for repairs, and its residents ate at the canteen instead." (ii) "At the college's second canteen, which kept the old price and the same menu, July sales matched June's." (iii) "The canteen also serves tea and snacks in the afternoon." (iv) "A few students said they liked the cheaper lunch."

| Statement | Bears on the causal link? | If it were true, the conclusion becomes ... | Role |
|---|---|---|---|
| (i) | yes: it offers a second cause for the rise | less believable: the extra diners could explain the rise without the price cut | weakens, strongly |
| (ii) | yes: same month, same menu, no price cut | more believable: July alone did not lift sales where the price stayed | supports, strongly |
| (iii) | no: afternoon items say nothing about lunch sales | no change | unrelated |
| (iv) | only at an edge: liking a lunch is not buying more lunches | slightly more believable | supports, weakly |

So (ii) best strengthens the conclusion and (i) best weakens it. Run the order test as well: the price cut came at the start of July and the rise was measured over July, so the stated cause comes before the effect; had the rise begun in June, the conclusion would fail on timing alone.

What this establishes: each role is fixed by two questions, "does it bear on the exact link?" and "if it were true, which way would belief move?", asked about one statement at a time. Where it stops: the method judges how a statement bears on the conclusion, not whether the statement is true; a weakening statement can be doubtful and still weaken.

**Failure condition.** The method fails when a role is judged by tone or by your own opinion of the conclusion. A statement you dislike can still support; a statement that merely mentions the same topic, like (iii), is not automatically relevant. When asked for the "best" strengthener or weakener, compare how hard each candidate pushes on the key link, not merely its direction.

### Numbered statements and combination options

Many items list numbered statements and offer combinations such as "1 only", "1 and 2", "2 and 3" and "1, 2 and 3". Judge one statement at a time, and let each secure verdict strike options.

**Worked example (original).** Options: (a) 1 only, (b) 1 and 2, (c) 2 and 3, (d) 1, 2 and 3. Suppose you are certain statement 1 is correct: option (c) goes, since it leaves 1 out. Suppose you are also certain statement 3 is wrong: option (d) goes. Only (a) and (b) are left, and they differ only on statement 2, so statement 2 is the one statement still worth your time.

**Failure condition.** Striking works only on verdicts you are sure of. A guess about one statement, used to strike options, can throw away the right combination before the statements you can actually judge are read.

### Part C - Truth-teller and suspect-statement logic

### Visual: the case tree for "exactly one statement is true"

```text
                     WHO IS THE CULPRIT?
       ┌──────────────────┼──────────────────┐
   assume U            assume V            assume W
       │                  │                  │
  score each          score each         score each
  statement           statement          statement
  true / false        true / false       true / false
       │                  │                  │
  count of true       count of true      count of true
  = stated count?     = stated count?    = stated count?
       │                  │                  │
   keep or drop       keep or drop        keep or drop
       └──────────────────┴──────────────────┘
          exactly one branch survives -> answer
          more than one survives     -> not fixed
```

Each branch assumes one possibility, scores every statement as true or false under that possibility, and compares the number of true statements with the number the stem allows. Branches that give the wrong count are dropped. The answer is fixed only if exactly one branch survives.

### Possible worlds instead of trusted speakers

When some speakers lie, you cannot take any statement at face value. You also cannot start by trusting the most confident speaker. Instead, try each possible world in turn, and see whether the speakers' statements would then have the stated pattern of truth and falsehood.

### Method D: assume, score, and check the count

1. List the possibilities: who did it, or which speakers are honest.
2. For each possibility, mark each statement true or false.
3. Keep the possibility only if the pattern matches the stem's condition (for example, "exactly one is true").
4. Report what is true in every surviving possibility.

**Worked example (original).** One of three runners, U, V and W, won. Exactly two of their statements are true. U: "I did not win." V: "W won." W: "V did not win."

| Assume winner | U's statement | V's statement | W's statement | True count |
|---|---|---|---|---|
| U | false | false | true | 1 |
| V | true | false | false | 1 |
| W | true | true | true | 3 |

No branch gives exactly two true statements. The statements are inconsistent with the condition, so the item as posed would have no answer. In a real item, one branch survives; this example shows why you must score every branch rather than stopping at the first plausible one.

**A second worked example (original).** Change the condition to "exactly one statement is true". Now the U and V branches both survive with a count of 1. The winner is not fixed: it is U or V. A definite answer exists only where one branch survives.

What these establish: the count condition does the eliminating, not the content of the statements. Where they stop: if the stem says "each person either always lies or always tells the truth" and gives two statements per person, a person's two statements must have the same truth value, which is an extra check per branch.

**Failure condition.** Method D fails when you assume one speaker honest and stop at the first consistent story. Every branch must be scored, because a second surviving branch makes the answer undetermined.

### Assume-then-contradict for honest and lying speakers

Where speakers are each wholly honest or wholly lying, assume one speaker is honest, follow what that forces about the others, and look for a contradiction. If assuming honesty leads to a contradiction, that speaker is lying.

**Worked example (original).** A says, "B is lying." B says, "A and C are both lying." C says, "B is honest." Assume B honest: then A and C are lying. C lying means "B is honest" is false, so B is lying, which contradicts the assumption. So B is lying. Then A's statement is true, so A is honest. C says B is honest, which is false, so C is lying. Check B's statement, "A and C are both lying": A is honest, so the statement is false, which fits B lying. Answer: A honest; B and C lying.

**Failure condition.** The contradiction must come from the statements and the honesty rule only. If you reach a "contradiction" by assuming an extra fact, the branch has not been eliminated.

### Judging by plausibility, and the counter-diagram reply

The tempting method is to judge a conclusion by whether it sounds sensible, or by drawing one diagram and reading the answer off it. With believable content it usually feels right, and that is why the paper uses believable content.

The reply is the counter-diagram. A conclusion that "sounds right" must survive the hardest redraw that obeys every premise. Likewise, in truth-teller items, the reply to "trust the confident speaker" is to score every branch and count.

### Paired ideas that are easy to confuse

- "Some A are B" versus "some A are not B": neither gives the other.
- Possible versus definite: true in one arrangement versus true in all arrangements.
- Correlation versus cause: "all who meditate are calm" versus "meditation causes calm".
- Contradictory versus contrary: the first pair always has exactly one true member; the second pair can have both false.

### UPSC application

Each family below is linked to the paper's items by year and question number; the method named beside it is the one taught above.

- **Syllogism conclusion checks** (2019 Q13; 2020 Q32 and Q33; 2021 Q10, Q15 and Q49; 2022 Q38 and Q39; 2015 Q55): draw one diagram, hunt for a counter-diagram, and watch for either-or pairs.
- **Everyday-content conclusions** (meditation and aggression, 2015 Q19; athletes and diet, 2015 Q20; UFO inference, 2015 Q56; fighters and cowards, 2015 Q78; population growth, 2016 Q8; music and gender, 2016 Q11; voice practice, 2017 Q15; morning walks, 2017 Q34; colour propositions, 2017 Q50; conclusion validity, 2024 Q58): accept only what the statements force, and reject causal conclusions that no statement asserts.
- **Party-supporter implication and statement validity** (2017 Q9 and Q10): translate each statement into a containment or arrow, then test each claim for validity.
- **Cause from cases** (2016 Q7): lay out a case grid and eliminate by presence and absence until one candidate is left.
- **Who stayed at home, and the definitely-male member** (2015 Q18; 2016 Q19): split cases on the least-fixed person and report only common facts.
- **Logical chain elimination** (2019 Q32): chain once, test each option.
- **Statement sufficiency** (2019 Q29): sufficient means true in every consistent arrangement.
- **True-false deduction and suspect statements** (2023 Q77; 2025 Q49): score every branch against the stated count or condition.
- **Transitive-colour syllogism (2026 Q48, provisional):** turn each statement into a containment, chain only through a shared middle group, and hunt for a counter-diagram before accepting any conclusion.
- **Statement-relationship logic (2026 Q71, provisional):** for each statement, ask whether it bears on the exact link in question and, if it were true, whether belief in the other would rise (supports), fall (weakens) or stay put (unrelated); check that the order of events allows any stated cause.
- **Numbered statements about a named term (2026 Q77, provisional):** this item asks which statements about a kind of business letter are correct, so it draws on knowledge of the term rather than on deduction from premises. The part this lesson supplies is the format: judge each numbered statement on its own against what the term means, and use only secure verdicts to strike combination options.

### Revision points

- Each statement form forbids a region or places a dot; everything else stays open.
- A conclusion is valid only if it holds in every diagram that satisfies all the premises.
- One counter-diagram that obeys every premise disproves a conclusion.
- "No A is B" and "some A are B" convert safely; "all A are B" does not convert to "all B are A".
- "Some A are B" does not give "some A are not B".
- "All A are B" plus "no B is C" gives "no A is C".
- An either-or pair must be contradictory and share subject and predicate.
- With everyday content, use only the statements; reject conclusions that need outside facts or unstated causes.
- In a case grid, a single reliable cause is present in every positive case and absent in every negative case.
- In case-split items, a fact is definite only if it holds in every consistent case.
- In truth-teller items, score every branch and keep only those matching the stated count.
- If more than one branch survives, the answer is not fixed.
- A statement supports a conclusion if, true, it makes the conclusion more believable; it weakens if it makes it less believable; it is unrelated if belief would not move, even when it shares a topic.
- In numbered-statement items, strike combination options only with verdicts you are sure of.
- Advanced: never report a placement true in only one arrangement.

### Practice

**MCQ 4**

Statements: All tutors are graders. No grader is a referee. Some authors are tutors. Take every group named here to have at least one member.

Conclusions: I. All graders are tutors. II. Some authors are not referees. III. No tutor is a referee. IV. Some referees are authors.

Which conclusions follow?

- A. Only III follows
- B. Only I, II and III follow
- C. I, II, III and IV all follow
- D. Only II and III follow

**MCQ 4 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** This rejects II on the belief that a "some ... not" conclusion needs a negative premise about authors. The authors who are tutors are graders, and no grader is a referee, so those authors are not referees; II follows, and "III only" is incomplete.
- **B — Incorrect:** This accepts I, the converse of "all tutors are graders". A diagram with graders outside the tutors' circle obeys every statement and makes I false, so the set "I, II and III" contains a conclusion that is not forced.
- **C — Incorrect:** This accepts I as a converse and IV as if possible meant definite. Referees may overlap the authors who are not tutors, but a diagram that keeps every referee away from every author also obeys all three statements, so IV is not forced.
- **D — Correct:** III follows because tutors sit inside graders and graders are wholly apart from referees. II follows because some authors are tutors, those tutors are graders, and graders are not referees. I is a converse and fails in a diagram with graders outside the tutors; IV fails in a diagram with referees apart from all authors. Exactly II and III follow.

**MCQ 5**

One of three clerks, X, Y and Z, misplaced a file. Each makes one statement, and exactly one of the three statements is true. X says, "Y misplaced it." Y says, "I did not misplace it." Z says, "X did not misplace it." Which conclusion is correct?

- A. X misplaced it; only Y's denial is a truthful statement.
- B. Y misplaced it, and X's statement is the only true one.
- C. Z misplaced it; only Z's statement is true.
- D. Y or Z misplaced it, and the count cannot separate the two.

**MCQ 5 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Score each branch. If X did it: X's statement is false, Y's is true, Z's is false, so exactly one is true. If Y did it: X's and Z's statements are true, a count of two. If Z did it: Y's and Z's statements are true, a count of two. Only the X branch matches the stated count, so X misplaced the file and only Y spoke truly.
- **B — Incorrect:** This trusts the accuser and scores only X's statement. In the Y branch, Z's statement "X did not misplace it" is also true, so the count is two, not one.
- **C — Incorrect:** This scores Z's statement in the Z branch but overlooks Y's denial. If Z did it, Y's "I did not misplace it" is true as well, so two statements are true and the branch fails.
- **D — Incorrect:** This flips the condition to "exactly one statement is false". Under that misreading the Y and Z branches each have one false statement and both survive; under the stated condition only the X branch survives.

---

## Lesson 3 - Series, analogies and figural sequences

Progress: Lesson 3 of 18 | Stage: Foundation | Subtopic: Series, analogies and figural sequences

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A row of numbers, letters or small pictures appears with a gap, and you must supply the missing piece. Or two items are paired, and you must find the partner of a third. Or four groups appear, and one does not belong. These items look like puzzles of insight, and that is why candidates lose time on them: they stare, hope for a flash, and then guess. This lesson replaces the stare with a routine. Every such item hides a rule. The rule must hold for every term, and there is a short list of places to look for it.

The previous two lessons trained you to accept only what holds in every case. Here the same discipline applies to rules: a rule that fits three terms and fails on the fourth is not the rule.

### Visual: two ladders and an invariant table

```text
  DIFFERENCE LADDER                     RATIO LADDER
  terms:    2    6    12    20    30    terms:   3    6    12    24
  1st diff:   4    6     8    10        ratio:     x2   x2    x2
  2nd diff:      2    2     2           next term: 24 x 2 = 48
  next 1st diff: 12  ->  next term 42
```

| Feature | Figure 1 | Figure 2 | Figure 3 | Figure 4 | Verdict |
|---|---|---|---|---|---|
| Number of sides | 4 | 4 | 4 | 4 | invariant |
| Shaded corner | top-left | top-right | bottom-right | bottom-left | moves one corner clockwise |
| Dots inside | 1 | 2 | 3 | 4 | rises by 1 |
| Arrow direction | up | right | down | left | turns 90 degrees clockwise |

The left ladder takes differences between neighbours until a row becomes constant; here the second differences are all 2, so the next first difference is 12 and the next term is 42. The right ladder divides neighbours; a constant ratio means a multiplying rule. The table does the same job for pictures. Each row is one feature tracked across the figures. A row that never changes is an **invariant**, a feature the rule keeps fixed. A row that changes by the same step each time is a **per-step rule**. The missing figure must obey every row at once: four sides, shaded corner back at top-left, five dots, arrow pointing up.

### A hidden machine: the intuition behind a series

A series is a machine that produces each term from the one before, or from its position in the line. You do not see the machine, only its output. Your job is to guess the machine and then test it on every output you can see. If it reproduces all of them, use it for the gap. If it fails on even one, it is the wrong machine.

The analogy has a limit. A real machine has one design, but a short list of terms can sometimes be produced by two different rules. When that happens, the item is decided by the rule that fits every given term and also appears among the options. Choose the simplest rule that fits all terms, and confirm it against the options.

### Part A - Number and letter series

### Method A: the rule search, in a fixed order

1. **Differences.** Subtract each term from the next. If the differences are constant, the series adds a fixed amount. If not, take differences of the differences.
2. **Ratios.** Divide each term by the one before. A constant ratio means multiplication.
3. **Operation rules.** Try "multiply then add", such as x2 + 1.
4. **Known sequences.** Squares (1, 4, 9, 16, 25), cubes (1, 8, 27, 64), primes (2, 3, 5, 7, 11, 13), and triangular numbers.
5. **Two interleaved series.** If neighbours jump up and down, split the odd-placed and even-placed terms.
6. **Verify on every term** before using the rule.

**Failure condition.** The search fails when you stop at the first rule that fits two or three terms. A rule is accepted only after it reproduces every given term.

### Triangular numbers

The **triangular numbers** are the totals 1, 1 + 2, 1 + 2 + 3, and so on: 1, 3, 6, 10, 15, 21. The n-th triangular number is n(n + 1)/2. Their differences are 2, 3, 4, 5, rising by one each time. So whenever the first differences of a series rise by one, triangular numbers are nearby.

**Worked example (letters).** A, C, F, J, ? Convert letters to positions, with A = 1 and Z = 26: 1, 3, 6, 10. The gaps are +2, +3, +4, so the next gap is +5 and the next position is 15, which is O. The positions are the triangular numbers.

What this establishes: letter series become number series once you write positions. Where it stops: if the positions run past 26, the series either wraps round to A or the item intends something else; check the options before assuming a wrap.

### Worked examples of the search

- **Second differences.** 2, 6, 12, 20, 30, ? First differences 4, 6, 8, 10; second differences constant at 2; next first difference 12; next term 42. Each term is n(n + 1), which confirms the answer by a second route.
- **Differences that are squares.** 1, 2, 6, 15, 31, ? First differences 1, 4, 9, 16; these are squares, so the next is 25, giving 56.
- **Multiply then add.** 5, 11, 23, 47, ? The differences 6, 12, 24 double, which suggests a multiplying rule. Test x2 + 1: 5 x 2 + 1 = 11, 11 x 2 + 1 = 23, 23 x 2 + 1 = 47. It fits every term, so the next is 47 x 2 + 1 = 95.
- **Two interleaved series.** 4, 20, 7, 17, 10, 14, ? Split by position: odd places 4, 7, 10 (rising by 3); even places 20, 17, 14 (falling by 3). The next term is in an odd place, so it is 13.
- **A backward letter series.** Z, X, U, Q, ? Positions 26, 24, 21, 17: gaps -2, -3, -4. The next gap is -5, giving 12, which is L.

What these establish: the five search steps cover the great majority of series in the paper. Where they stop: when two rules both fit, as can happen with only three given terms, the options decide; never invent a complex rule when a simple one fits every term.

### The middle term and the dual sequence

Some items hide the gap in the middle, not at the end. The same search applies; you simply test the rule on both sides of the gap.

**Worked example.** 12, 20, ?, 42, 56. Try differences around the gap: 20 - 12 = 8 and 56 - 42 = 14. If the differences rise by 2, the sequence of differences is 8, 10, 12, 14, giving 20 + 10 = 30 and 30 + 12 = 42. The rule fits on both sides, so the missing term is 30.

**Failure condition.** A middle-gap rule must be checked against the terms after the gap as well. A rule found only from the terms before the gap can produce a value that clashes with the terms after it.

A **dual sequence** item gives two related rows, such as a top row and a bottom row, and leaves a gap in one. Find the rule linking each column (top to bottom), and the rule along each row, and use whichever is fully determined. Where both can be found, use one to fill the gap and the other to check it.

**Worked example (original).** Top row: 2, 5, 8, 11, 14. Bottom row: 5, 26, ?, 122, 197.

- Column rule. Compare each top number with the number below it: 2 and 5, 5 and 26, 11 and 122, 14 and 197. Squaring the top number and adding 1 gives 4 + 1 = 5, 25 + 1 = 26, 121 + 1 = 122 and 196 + 1 = 197. It fits all four complete columns. The gap sits under 8, so it is 64 + 1 = 65.
- Row check. Along the bottom row, the gaps would be 26 to 65 = 39, then 65 to 122 = 57, and 122 to 197 = 75. With 5 to 26 = 21 at the start, the gaps are 21, 39, 57, 75, rising by 18 each time. The bottom row has its own steady pattern only if the gap is 65, so the two routes agree.

What this establishes: in a dual sequence, a column rule tested on every complete column is usually the fastest route, and a row rule is a free check. Where it stops: if the column rule fits only some columns, it is not the rule; try a row rule for each row separately, or a rule that uses the position number.

**Failure condition.** The dual-sequence method fails when a rule is read off a single column. Two numbers can be linked in many ways: 5 to 26 is "square plus 1", but it is also "times 5 plus 1". Only a rule that fits every complete column may be used, and "times 5 plus 1" fails at once on the first column, since 2 x 5 + 1 = 11, not 5.

### Letter positions and reverse positions

Write the alphabet line once and keep it beside you.

```text
  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1   <- position from Z
```

The **position from the right** of a letter is 27 minus its position from the left.

**Worked example.** Which letter is seventh to the left of the eighteenth letter from the right? The eighteenth from the right is at position 27 - 18 = 9 from the left, which is I. Seven places to its left is position 2, which is B.

**Failure condition.** Position questions fail when "to the left of" and "from the left" are confused. "From the left" counts from A; "to the left of X" counts backwards from X. Write each step as a number before converting to a letter.

### Repeating patterns with blanks

A **repeating pattern** item gives a string such as "a _ c a b _ a b c _ b c" with some letters missing. Find the shortest block that repeats.

**Worked example.** Try a block of length 3, "abc": a b c | a b c | a b c | a b c. Line it up with the given string: position 2 must be b, position 6 must be c, position 10 must be a. The blanks are b, c, a.

**Failure condition.** The method fails when you guess the block length from the first few letters only. Test the block against every given letter in the string; if any given letter clashes, try another length.

### Cyclic series: months, days and clock positions

Months, weekdays and clock positions repeat. Number them (January = 1 to December = 12) and work in steps that wrap round after the last.

**Worked example.** January, June, November, April, September, ? Each step moves forward 5 months: 1, 6, 11, 16 (which wraps to 4, April), 21 (wraps to 9, September), so the next is 26, which wraps to 2, February.

**Failure condition.** The wrap must use the right cycle length: 12 for months, 7 for weekdays, 12 or 24 for clock hours. Using the wrong length shifts every later term.

### Part B - Analogies and odd-one-out groups

### Method B: name the relation, then test it on the parallel pair

An **analogy** has the form A : B :: C : ?, read "A is to B as C is to ?". Name the relation that turns A into B, then apply exactly that relation to C.

**Worked example (letters).** CF : HK :: MP : ? Within each pair, the second letter is 3 after the first (C to F, H to K). Between pairs, the first letters move by 5 (C to H). Apply both: M + 3 is P, which matches; the next pair starts 5 after M, at R, and R + 3 is U. If the question asks for the partner of MP in the same pattern, it is RU.

**Worked example (numbers).** 3 : 27 :: 5 : ? The relation could be "cube" (27 is 3 cubed), giving 125. It could equally be "multiply by 9", giving 45. Both describe the first pair.

What these establish: a single pair can support more than one relation. Where they stop: the item is decided by the relation that the options support, or by a second given pair. If both 45 and 125 appear as options, look for a second pair in the stem; if there is none, prefer the relation that uses the number itself (the cube) over an arbitrary multiplier, and say so to yourself as a judgement, not a certainty.

**Failure condition.** The analogy method fails when you choose a relation that fits the first pair but not a second given pair. Test every pair in the stem.

### Odd-one-out: find the property that singles out exactly one

In an **odd-one-out** item, all groups but one share a property. The answer is the group that lacks it.

**Worked example (original).** (3, 9, 27), (2, 4, 8), (5, 25, 125), (4, 12, 36). Work down the list of properties.

- Fixed ratio inside the group: 3 to 9 to 27 is times 3; 2 to 4 to 8 is times 2; 5 to 25 to 125 is times 5; 4 to 12 to 36 is times 3. Every group has a fixed ratio, so this property marks no group out.
- All odd: true for (3, 9, 27) and (5, 25, 125), false for the other two. A two-against-two split decides nothing.
- Ratio equal to the first number: 3 times 3, 2 times 2 and 5 times 5 fit, so those groups are a number, its square and its cube. In (4, 12, 36) the ratio is 3, not 4. This property marks exactly one group.

The odd one out is (4, 12, 36).

**Rule.** Try properties in order: all prime, all even or odd, a fixed difference or ratio inside the group, a fixed sum or product, squares or cubes, digit sums. Keep going past properties that every group shares or that split the groups evenly.

**Failure condition.** A property that separates two groups from the other two does not decide the item. Keep searching until one property marks exactly one group out.

### Figural analogy

A **figural analogy** shows Figure 1 changed into Figure 2 and asks for the figure that Figure 3 becomes. List what changed between 1 and 2: rotation, reflection, added or removed parts, shading switched, size changed. Apply each change, in the same order, to Figure 3.

**Worked example (original).** Figure 1 is a white square with an arrow inside pointing up and a black dot in its top-left corner. Figure 2 is a grey square with the arrow pointing right and the dot in its bottom-right corner. Figure 3 is a white circle drawn inside an imaginary square, with the arrow pointing left and the dot at the top-right of that square. Which figure completes 1 : 2 :: 3 : ?

List the changes from Figure 1 to Figure 2, one feature per line:

| Feature | Figure 1 | Figure 2 | Change | Applied to Figure 3 |
|---|---|---|---|---|
| Outline | square | square | none | circle stays a circle |
| Shading | white | grey | white becomes grey | grey circle |
| Arrow | up | right | turns 90 degrees clockwise | left becomes up |
| Dot | top-left | bottom-right | moves to the opposite corner | top-right becomes bottom-left |

So the answer is a grey circle with the arrow pointing up and the dot at the bottom-left.

Now check the arrow change is a rotation, not a reflection. A reflection in a vertical mirror would send an up-arrow to an up-arrow, not to a right-arrow, so it cannot explain Figure 2. A quarter-turn clockwise does. An option showing the arrow pointing right for Figure 3 is the result of copying Figure 2's arrow instead of applying the change.

What this establishes: a figural analogy is settled by a change table, built on the first pair and applied feature by feature to the third figure. Where it stops: if two different changes explain the first pair equally (for example, a 90-degree clockwise turn and a 270-degree anticlockwise turn), they give the same result and do not need separating; if they give different results for Figure 3, the options decide.

**Failure condition.** The method fails when you apply a rotation as a reflection or the other way round. A rotation keeps a left-handed shape left-handed; a reflection turns it into its mirror image. Check one asymmetric feature, such as a small flag on one side, to tell them apart.

### Part C - Figural sequences, moving symbols, mirror images and matrices

### Method C: list invariants, then the per-step change for each element

1. Copy the figures roughly, so you can mark them.
2. List every feature: number of elements, their positions, orientation, shading, size.
3. For each feature, mark it invariant or find its per-step change.
4. Track each moving element separately; two symbols in one grid often follow different rules.
5. Build the missing figure from every row of your table, and check that it matches every feature.

**Failure condition.** The method fails when you track the figure as a whole rather than each element. If a triangle moves clockwise and a circle moves anticlockwise, a whole-figure impression of "everything rotates" will be wrong for one of them.

### Moving symbols in a grid and around a ring

**Worked example (original).** A hexagon has six corners, numbered 1 to 6 clockwise. A star starts at corner 4 and moves 2 corners clockwise each step. A square starts at corner 1 and moves 1 corner anticlockwise each step. After three steps, the star has moved 6 corners, a full turn, so it is back at corner 4. The square has moved 3 corners anticlockwise: 1 to 6 to 5 to 4. Both symbols now share corner 4.

When the step itself grows, as in moves of 1, then 2, then 3 corners, add the steps first and then wrap round: after three moves of that kind, the total is 6 corners.

What this establishes: each symbol's position after n steps is its start plus its total movement, wrapped round the ring. Where it stops: if a symbol changes direction or step size mid-way, the table must show that change explicitly; do not assume a constant step.

**Failure condition.** The count must use the ring's true size. On a 3 by 3 grid, the outer ring has 8 cells, not 9; the centre is not on the ring.

### Beads, arrows and rotation series

**Arrows and lines.** Track the angle. An arrow turning 45 degrees clockwise each step points north, north-east, east, south-east, and then south. A turn of 90 degrees is a quarter-turn; 180 degrees reverses it.

**Rotation series.** A figure that turns by a fixed angle at each step comes back to its starting position after a whole number of full turns. The number of figures before it repeats is 360 divided by the largest number that divides both the step and 360.

**Worked example (original).** A pointer starts at north and turns 135 degrees clockwise at each step. Where does it point in Figure 6, and which figure first repeats Figure 1?

| Figure | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Total turn | 0 | 135 | 270 | 405 = 45 | 540 = 180 | 675 = 315 | 810 = 90 | 945 = 225 | 1080 = 0 |
| Pointer | N | SE | W | NE | S | NW | E | SW | N |

Figure 6 points north-west. The largest number dividing both 135 and 360 is 45, so the cycle has 360 / 45 = 8 figures, and Figure 9 is the first repeat of Figure 1.

What this establishes: a rotation series is worked out by adding the turns and reducing by 360, and its cycle length comes from the common divisor, not from 360 divided by the step (360 / 135 is not even a whole number). Where it stops: if two parts of the figure turn by different amounts, each part has its own cycle, and the whole figure repeats only when both cycles meet.

**Failure condition.** Rotation series fail when the step is read from a single pair of figures as if it were the only possible step. A pointer that goes from north to south-east may have made a turn of 135 degrees clockwise, which is the same move as 225 degrees anticlockwise (the two differ by a full turn), or it may have turned 495 degrees, 855 degrees, and so on; all of these land on south-east and predict the same next figure only if the step really is constant. What one pair cannot tell you is whether the step is constant at all, or whether it grows (135, then 180, then 225 degrees). Read the step from every consecutive pair of the given figures: if the observed steps all agree modulo 360, use that step; if they differ, track the change in the step itself. Two moves that agree modulo 360 can never be told apart from the figures, and they never need to be, because they give identical figures.

**Beads on a rod or wire.** Treat each bead as a separate symbol with its own position rule, usually a fixed move per step, and read from the figures what happens at the end of the rod.

**Worked example (original).** A rod has five slots, numbered 1 to 5 from the left. The given figures show a black bead in slots 1, 3, 5 and 2, and a white bead in slots 5, 4, 3 and 2. Where are the beads in Figure 6?

- Black bead: 1 to 3 to 5 is a move of 2 to the right. From 5, two more slots would be slot 7, which does not exist; the figures show slot 2, so the bead wraps round to the left end (7 - 5 = 2). Figure 5: 2 + 2 = 4. Figure 6: 4 + 2 = 6, which wraps to 1.
- White bead: one slot to the left each step: 5, 4, 3, 2, so Figure 5 is slot 1 and Figure 6 wraps to slot 5.

In Figure 6 the black bead is in slot 1 and the white bead in slot 5.

What this establishes: a bead item is two or more independent position rules on one rod. Where it stops: the end behaviour must be read from the figures; a bead could equally bounce back from the end (5 to 3), and here the fourth figure is the only evidence that it wraps instead.

**Failure condition.** The bead method fails when the end behaviour is guessed. If no given figure shows a bead passing an end, the item cannot tell wrapping from bouncing, and only the options can settle it.

### Mirror images

A mirror placed to the right of a word reverses left and right. The letters appear in reverse order, and each letter is flipped. A capital letter looks unchanged in such a mirror only if it is symmetric about a vertical line.

```text
  Symmetric about a vertical line (look unchanged in a side mirror):
  A  H  I  M  O  T  U  V  W  X  Y
  Not symmetric (look reversed):  B C D E F G J K L N P Q R S Z
```

**Worked example (original).** In the word MAHOUT, every letter (M, A, H, O, U, T) is symmetric about a vertical line, so each looks the same in a side mirror, although the order is reversed. The consonants among them are M, H and T: three.

**Failure condition.** The method fails when a horizontal mirror (water image) is treated as a side mirror. A water image flips top and bottom; the letters that survive it unchanged are those symmetric about a horizontal line, such as B, C, D, E, H, I, K, O, X.

### Embedded figures

An **embedded figure** item asks which complex figure contains a given simple figure. Copy the simple figure. List its segments and angles. Look for a set of lines in each complex figure that matches in size, shape and orientation.

**Worked example (original).** The simple figure is a Z: a top stroke and a bottom stroke of equal length, joined by a slanting stroke from the right end of the top stroke down to the left end of the bottom stroke, at 45 degrees. Three complex figures are drawn on the same scale, each the same height as the Z. In how many of them is the Z embedded?

```text
   SIMPLE FIGURE         FIGURE P              FIGURE Q              FIGURE R
   ┌──────┐            ┌──────┐            ┌──────┐            ┌──────────────┐
         ╱             │╲     │            │╲    ╱│            │           ╱  │
       ╱               │  ╲   │            │  ╲╱  │            │      ╱       │
     ╱                 │    ╲ │            │  ╱╲  │            │ ╱            │
   └──────┘            └──────┘            └──────┘            └──────────────┘
   top, slant from     square, slant       square with         rectangle twice as
   top-right to        from top-left       both slants         wide, slant from
   bottom-left         to bottom-right                         top-right to bottom-left
```

| Figure | Top and bottom strokes of the right length? | Slant from top-right to bottom-left at 45 degrees? | Embedded? |
|---|---|---|---|
| P | yes, the square's top and bottom sides | no: its only slant runs top-left to bottom-right, which makes the mirror image of the Z | no |
| Q | yes | yes: one of its two slants runs top-right to bottom-left; the other slant and the side lines are extra lines, which do not matter | yes |
| R | the strokes exist, but the slant joining their ends is shallower than 45 degrees, and no other slant exists | no | no |

So the Z is embedded in exactly one figure, Q. Notice the two ways a figure can look right and still fail: P holds the mirror image, and R holds a stretched copy.

What this establishes: an embedded figure is found by matching strokes one at a time, by length, direction and the way they join, while ignoring extra lines around them. Where it stops: the match must use lines that are actually drawn; you may not complete a stroke the figure does not contain.

**Failure condition.** Unless the stem allows rotation, an embedded figure must keep its orientation. A matching shape turned on its side, or flipped into its mirror image as in Figure P, does not count, and neither does a copy stretched to a different size or angle, as in Figure R.

### Matrix completion

A **matrix** item gives a 3 by 3 arrangement with one cell missing. The rule may run along rows, down columns, or both.

**Worked example (numbers).** Rows: (2, 3, 6), (4, 5, 20), (3, 7, ?). In each complete row, the third number is the product of the first two: 2 x 3 = 6, 4 x 5 = 20. So the missing number is 3 x 7 = 21.

**Worked example (figures).** In a matrix of arrows, circles and triangles, a common rule is that each row contains each element exactly once, and each column also does. The missing cell is the element absent from its row and its column.

**Failure condition.** A row rule must hold for every complete row; a column rule for every complete column. If the rule you found works for one row only, try the columns, then a combined rule.

### Sequences versus counting questions

Some figure items do not ask for the next figure at all; they ask how many triangles or squares a drawing contains. That is a counting question, not a sequence question. The habit carries over (copy the figure and work one feature at a time, never by impression), but the counting itself is done size by size, with a total for each size.

### Fixing the rule too early, and the verification reply

The tempting method is to fix a rule from the first two or three terms and fill the gap at once. It feels fast, and on easy items it works. On harder items the paper deliberately builds series where a tempting early rule breaks on the fourth or fifth term, and the matching wrong value is printed among the options.

The reply is the verification step. Before answering, write your rule beside every given term and check it. If any term disagrees, the rule is wrong, however neatly it fitted the start. For figures, the reply is the invariant table: one row per feature, checked on every figure.

### Rules and pictures that are easily swapped

- Difference rule versus ratio rule: constant gaps versus constant multipliers.
- Position from the left versus position from the right: n versus 27 - n.
- Rotation versus reflection: a rotated shape keeps its handedness; a reflected one reverses it.
- Side mirror versus water image: left-right flip versus top-bottom flip.

### UPSC application

This lesson's methods meet a broad set of families.

- **Number series**: sequence completion, the middle term of a sequence, a series blank-fill pattern, and matrix trend and dual-sequence missing entries. Run the rule search and verify on every term.
- **Letter series**: letter sequence fill and completion, letter-pattern completion, and a letter series position item. Convert to positions, use the alphabet line, and keep "from the left" separate from "to the left of".
- **Repeating patterns and cycles**: a repeating pattern gap fill and a month-pattern sequence. Find the block length; wrap round with the correct cycle.
- **Analogies and odd-one-out**: letter analogy series, figural analogy completion, and a group odd-one-out built on a number property. Name the relation and test it on every pair; find the property that marks exactly one group.
- **Figural sequences**: moving symbols in a grid, triangle symbol, line-and-arrow and circular-arrow sequences, bead-position sequences, figure-sequence completion and figural rotation series. Track each element separately with an invariant table.
- **Matrix completion**: arrow matrix and circle-triangle matrix completion. Find the row rule and the column rule.
- **Embedded figure and mirror-image consonant count**: keep orientation fixed for embedded figures; use the vertical-symmetry list for side mirrors.

### Revision points

- Every series hides a rule; accept a rule only after it reproduces every given term.
- Search in order: differences, ratios, multiply-then-add, known sequences, interleaved series.
- Triangular numbers are 1, 3, 6, 10, 15, 21; their gaps rise by one; the n-th is n(n + 1)/2.
- Convert letters to positions (A = 1 to Z = 26); position from the right is 27 minus position from the left.
- Jumping up and down usually signals two interleaved series; split them by position.
- For a gap in the middle, check the rule on both sides.
- In a repeating pattern, find the shortest block that agrees with every given letter.
- Cyclic series wrap with the right cycle: 12 months, 7 days.
- In an analogy, the relation must fit every given pair; one pair may support two relations.
- An odd-one-out property must single out exactly one group.
- For figures, make one table row per feature, mark invariants, and track each element separately.
- A side mirror reverses order and flips letters; A, H, I, M, O, T, U, V, W, X, Y look unchanged.
- Embedded figures keep size and orientation unless the stem allows otherwise.

### Practice

**MCQ 6**

What is the next term in the series 5, 8, 14, 23, 35, ...?

- A. 47, by repeating the last gap of 12
- B. 50, as each gap is three more than the one before
- C. 58, by adding the two terms before it
- D. 59, by doubling the immediately preceding difference

**MCQ 6 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** This treats the series as if the gaps had stopped growing. The gaps are 3, 6, 9, 12, so repeating 12 gives 35 + 12 = 47, which breaks the pattern of rising gaps.
- **B — Correct:** The first differences are 3, 6, 9, 12, and they rise by 3 each time, so the next difference is 15 and the next term is 35 + 15 = 50. The rule reproduces every given term: 5 + 3 = 8, 8 + 6 = 14, 14 + 9 = 23, 23 + 12 = 35.
- **C — Incorrect:** This applies a two-term sum rule without checking it on the given terms. It first fails at the third term, since 5 + 8 = 13, not 14; applied anyway to the last two terms, it gives 23 + 35 = 58.
- **D — Incorrect:** This assumes the gaps double. The gap from 6 to 9 is not a doubling, so the rule fails on the given terms; applied anyway, it gives 35 + 24 = 59.

**MCQ 7**

The series 4, 8, 11, 22, 25, 50 is built by one rule. Which description fits every term?

- A. Add four to the previous term, then add three to it, alternately
- B. Add the two previous terms, then subtract one
- C. Double the previous term, then add three to it, alternately
- D. Add three to twice the term two places earlier

**MCQ 7 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** This reads the first two gaps, +4 and +3, as a repeating pair of additions, with the four first. It gives 4, 8, 11, 15, so it fails at the fourth term, where the series has 22.
- **B — Incorrect:** This is a two-term rule checked only on the first triple: 4 + 8 - 1 = 11 fits, but then 8 + 11 - 1 = 18, not 22.
- **C — Correct:** Doubling comes first, then adding three, and the two alternate: 4 x 2 = 8, 8 + 3 = 11, 11 x 2 = 22, 22 + 3 = 25, 25 x 2 = 50. Every given term is reproduced. With the order reversed (add three first), the second term would be 7, not 8.
- **D — Incorrect:** This links each term to the one two places earlier. It fits the third term (2 x 4 + 3 = 11) and even the fifth (2 x 11 + 3 = 25), but gives 2 x 8 + 3 = 19 for the fourth term instead of 22.

**MCQ 8**

The eight outer cells of a 3 by 3 grid form a ring. In the first figure, a dot sits in the top-right corner cell. In each later figure the dot moves clockwise around the ring: one cell in the first move, two cells in the second, three in the third, and so on. Where is the dot after the fifth move?

- A. the bottom-right corner cell of the ring
- B. the middle cell of the left column
- C. the cell in the middle of the right column
- D. the middle cell of the ring's top row

**MCQ 8 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** This stops after four moves. Four moves total 1 + 2 + 3 + 4 = 10 cells; from the top-right corner, 10 cells clockwise on an 8-cell ring is 2 cells on, the bottom-right corner.
- **B — Incorrect:** This keeps the step fixed at one cell per move. Five single-cell moves clockwise from the top-right corner reach the middle cell of the left column.
- **C — Incorrect:** This moves the dot anticlockwise. A total of 15 cells anticlockwise from the top-right corner is 15 - 8 = 7 cells, which is the same as 1 cell clockwise, the middle cell of the right column.
- **D — Correct:** The five moves total 1 + 2 + 3 + 4 + 5 = 15 cells. On a ring of 8 cells, 15 cells is one full turn plus 7 cells. Clockwise from the top-right corner, 7 cells lands one cell short of a full turn, in the middle cell of the top row. Step by step: right-middle, bottom-middle, top-left, bottom-right, top-middle.

---

## Lesson 4 - Coding, decoding and alphametics

Progress: Lesson 4 of 18 | Stage: Core | Subtopic: Coding, decoding and alphametics

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You are told that one word is written as a string of strange letters, or numbers, or symbols, and you must write another word in the same code. Or a sum is printed with letters instead of digits, and you must work out which digit each letter hides. The usual mistake is not a lack of cleverness. It is haste: a rule is guessed from the first letter, applied to the new word, and the matching wrong option is waiting. This lesson teaches you to extract a rule from every given letter, to prove it before you use it, and to break a letter-sum column by column.

The previous lesson taught you to verify a series rule on every term. Coding is the same habit applied to letters: a code rule is accepted only when it reproduces every given letter.

### Visual: the position line and the shift table

```text
  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
              ^              ^              ^              ^              ^
              E=5            J=10           O=15           T=20           Y=25   (anchor letters)

  MIRROR PAIRS (positions add to 27):  A-Z  B-Y  C-X  D-W  E-V  F-U  G-T  H-S  I-R  J-Q  K-P  L-O  M-N
```

| Plain letter | Shift +1 | Shift +2 | Shift +3 | Shift -2 | Mirror (27 - n) |
|---|---|---|---|---|---|
| A (1) | B | C | D | Y | Z |
| H (8) | I | J | K | F | S |
| W (23) | X | Y | Z | U | D |
| Y (25) | Z | A (wraps) | B (wraps) | W | B |

The top line gives each letter its position number. The five anchor letters, E, J, O, T and Y, sit at multiples of 5, so you can find any position in a second by counting from the nearest anchor. The mirror line pairs each letter with the letter at the same distance from the other end; the two positions always add to 27. The table shows how one plain letter moves under the commonest rules. A shift moves every letter the same number of places, wrapping from Z back to A. A mirror sends each letter to its partner. Notice that Y under a mirror and Y under a shift of +3 both give B: two different rules can agree on one letter. That is exactly why one letter never proves a rule.

### A private language with one rule

A code is a private language with one consistent rule. Whoever made it applied the same rule to every letter, otherwise it could not be decoded. So the given pair, plain word and coded word, is a sample of the rule at work. You are not inventing a rule; you are recovering one that already exists.

The analogy has a limit. A real secret language may change its rule from message to message. In the paper, unless the stem says so, the same rule applies to the given pair and to the new word.

### Method 1: derive the rule from every pair, then test every letter

1. Write the position number under each plain letter and each coded letter.
2. Compare them letter by letter: constant difference (a shift), sum of 27 (a mirror), a reordering of the same letters (a rearrangement), or numbers built from positions.
3. Name one rule and test it on every letter of every given pair.
4. Only then apply it to the new word, letter by letter, and re-check the wrap at Z.

**Failure condition.** The method fails when the rule is chosen from one letter. A first letter that moves back five places may belong to a mirror code, a shift code or a reordering; only the remaining letters decide.

### Worked example: a shift verified on two pairs

If CAT becomes DBU and DOG becomes EPH, code SUN.

- CAT to DBU: C (3) to D (4), A (1) to B (2), T (20) to U (21). Every letter moves +1.
- DOG to EPH: D to E, O to P, G to H. Every letter again moves +1.

The second pair confirms that the rule was not guessed from one letter. So S to T, U to V, N to O: SUN becomes TVO.

What this establishes: two pairs that agree on every letter fix a shift beyond doubt. Where it stops: a shift with a varying amount (+1, +2, +3 across the word) would also fit the first letters; only checking every letter rules it out.

### Advanced Method 2: the shift of two

Advanced. If EARTH is coded GCTVJ, how is MARS coded? Positions: E (5) to G (7), A (1) to C (3), R (18) to T (20), T (20) to V (22), H (8) to J (10). Each letter moves +2. So M (13) to O (15), A (1) to C (3), R (18) to T (20), S (19) to U (21): MARS becomes OCTU.

What this establishes: a word of five letters gives five independent checks of one rule. Where it stops: if MARS had contained Y or Z, the shift would wrap: Y + 2 is A, and Z + 2 is B.

**Failure condition for shifts.** A shift fails at the wrap if you count past Z without returning to A. Write the position, add the shift, and subtract 26 whenever the total exceeds 26.

### Mirror codes (alphabet reversal)

In a **mirror code**, also called alphabet reversal, each letter is replaced by the letter at the same distance from the other end. A becomes Z, B becomes Y, and in general a letter at position n becomes the letter at position 27 - n.

**Worked example (original).** GLOW becomes TOLD: G (7) to T (20), L (12) to O (15), O (15) to L (12), W (23) to D (4). Every pair of positions adds to 27.

A mirror code is its own reverse: applying it twice returns the original word. So decoding uses the same rule as encoding.

**Failure condition.** A mirror code can look like a shift on one letter. G to T is +13, but L to O is +3. Check the sum of 27 on every letter before naming the rule.

### Rearrangement codes

In a **rearrangement code**, the coded word uses the same letters, moved to new places. Number the positions of the plain word and read off where each coded letter came from.

**Worked example (original).** MANGO is coded GOMAN. The coded word takes letters from positions 4, 5, 1, 2, 3 of the plain word. Check on a second pair: LEMON becomes O (4), N (5), L (1), E (2), M (3), that is ONLEM, which matches if that pair is given. Apply to PLATE: T (4), E (5), P (1), L (2), A (3) gives TEPLA.

**Failure condition.** A rearrangement rule depends on word length. A rule found on five-letter words cannot be applied to a six-letter word unless the stem shows how the extra letter moves.

### Letter-to-number codes

Many codes turn a word into a number.

- **Position sum.** CAGE: 3 + 1 + 7 + 5 = 16.
- **Position product (a multiplicative code).** BAD: 2 x 1 x 4 = 8.
- **Reverse-position sum.** Use 27 - n for each letter before adding.
- **Cubes of positions.** If ACE is coded 1-27-125, each letter becomes the cube of its position (1, 3, 5 cubed), so BAD is coded 8-1-64.
- **Digit-for-letter substitution.** A table assigns a digit or symbol to each letter, and a word is written by looking up each letter. It has its own method, taught just below.

**Failure condition.** A number code fails when the operation is guessed from the total alone. A total of 16 could be a sum, a product of other letters, or a sum plus a constant. Test the operation on a second given word before applying it.

### Letter-digit substitution

In a **letter-digit substitution**, each letter has its own fixed digit, wherever it appears. The given coded words are samples of a hidden table. Build the table letter by letter, check that no letter has been given two different digits, and only then read or write a new word.

**Worked example 1 (original): one sample and a partial table, read a number.** In a fixed letter-digit code, MOTHER is written 724961. You are also told that S stands for 3 and A for 8, and that no two letters share a digit. Which word does 3214 stand for, and can 5214 be read?

1. Build the table from the sample: M = 7, O = 2, T = 4, H = 9, E = 6, R = 1. Add the given entries S = 3 and A = 8.
2. Check for clashes: eight letters, eight different digits (7, 2, 4, 9, 6, 1, 3, 8). No letter has two digits and no digit serves two letters, so the table is usable.
3. Read 3214 digit by digit: 3 is S, 2 is O, 1 is R, 4 is T. The word is SORT.
4. Try 5214: no letter in the table has the digit 5. That number cannot be read from this information; it needs a ninth letter whose digit was never given.

What this establishes: a fixed table can be read in either direction, from word to number or from number to word, once every letter involved has exactly one digit. Where it stops: a digit that no given letter uses, like 5 here, is a gap in the table, not a clue to guess from.

**Worked example 2 (original): when the table breaks.** NOON is written 5788 and TEN is written 177. Is this a fixed letter-digit table, and if not, how is NET written?

1. Try to build a table from NOON: N gets 5 at the start but 8 at the end, and O gets 7 and then 8. One letter with two digits already rules out a fixed table.
2. Look for a rule that uses position. Write alphabet position plus place in the word, and keep the last digit: N (14) + 1 = 15, so 5; O (15) + 2 = 17, so 7; O (15) + 3 = 18, so 8; N (14) + 4 = 18, so 8. That reproduces 5788.
3. Test it on the second sample: T (20) + 1 = 21, so 1; E (5) + 2 = 7; N (14) + 3 = 17, so 7. That reproduces 177, so the rule fits every given digit.
4. Apply it to NET: N (14) + 1 = 15, so 5; E (5) + 2 = 7; T (20) + 3 = 23, so 3. NET is written 573.

What this establishes: the clash test in a fixed-table problem is also the alarm that the code depends on position. Where it stops: a position rule found on two samples is still a guess until it reproduces every digit of every sample; here both samples agree, which is the minimum.

**Failure condition.** The method fails when a table is built from the first sample and used without the clash check, for example by reading N as 5 in NOON and then decoding every later 5 as N. Check that no letter has two digits and no digit has two letters before reading anything; if a clash appears, abandon the table and look for a position-dependent rule, as in Worked example 2.

### Coding facts worth carrying

- Positions: A = 1 to Z = 26; anchors E = 5, J = 10, O = 15, T = 20, Y = 25.
- Mirror partners add to 27.
- Shifts wrap: subtract 26 from any total over 26; add 26 to any total below 1.
- A rule must fit every given letter; one letter never proves a rule.

### The trap: a rule guessed from one letter

Suppose a code turns NOTE into MLGV. N (14) to M (13) suggests a shift of -1. But O (15) to L (12) is -3, T (20) to G (7) is -13, E (5) to V (22) is +17. The constant-shift idea collapses at once. The positions do add to 27 in every pair (14 + 13, 15 + 12, 20 + 7, 5 + 22), so the code is a mirror code. A candidate who stopped at N would have chosen the "minus one" option.

### Word-code deduction across sentences

Some items code whole sentences and ask for the code of one word.

```text
  "sun is hot"   ->  ka lo mi
  "sun is up"    ->  lo pi ka
  "moon is up"   ->  pi ka ru
```

**Method 2: match shared words to shared codes.** A word in all three sentences must have a code in all three. "is" appears in all three; "ka" is the only code in all three; so is = ka. "sun" is in the first two sentences only; apart from ka, the shared code there is lo; so sun = lo. "up" is in the last two; apart from ka, the shared code is pi; so up = pi. That leaves hot = mi and moon = ru.

What this establishes: shared words and shared codes pin each other, regardless of word order. Where it stops: if a word appears in only one sentence alongside another unique word, the two cannot be separated, and the code of either one is undetermined.

**Failure condition.** The method fails when word order is assumed to carry over. Codes in these items are often shuffled, so position in the sentence is not evidence.

### Symbol and operator substitution

**Interchanging two signs.** Some items print a false equation and ask which interchange of two signs makes it true. "Which interchange of two signs makes 18 - 3 x 4 / 2 + 5 = 19 correct?" First evaluate it as printed, with division and multiplication before addition and subtraction: 3 x 4 / 2 = 6, and 18 - 6 + 5 = 17, so it is false. Then test each possible interchange, rewriting the whole line before calculating.

| Interchange | Rewritten line | Value |
|---|---|---|
| + and - | 18 + 3 x 4 / 2 - 5 | 19 |
| + and x | 18 - 3 + 4 / 2 x 5 | 25 |
| - and x | 18 x 3 - 4 / 2 + 5 | 57 |
| - and / | 18 / 3 x 4 - 2 + 5 | 27 |
| x and / | 18 - 3 / 4 x 2 + 5 | 21.5 |
| + and / | 18 - 3 x 4 + 2 / 5 | 6.4 |

Only the interchange of + and - gives 19. Notice what a left-to-right reading would have done to the original line: ((18 - 3) x 4) / 2 + 5 = 35, a wrong starting value that would send the whole search astray.

**Defined operations.** "Let a # b mean a squared minus b." Then 4 # 3 = 16 - 3 = 13, and (2 # 1) # 5 = (4 - 1) # 5 = 3 # 5 = 9 - 5 = 4.

**Failure condition.** Sign items fail when you calculate before rewriting, or rewrite one symbol and then re-rewrite the result. Rewrite the whole line once, with every changed sign replaced at the same time, and only then calculate in the usual order.

### Coded operators: decoding the signs from true equations

In a **coded-operator** item, letters or symbols stand for the four signs, and true equations written in that code are given. The task is to work out which letter is which sign, and then use the decoded signs.

**Worked example (original).** K and M stand for two different signs from +, -, x and /. In this code, 8 K 2 M 3 = 7 and 6 M 4 K 2 = 8, with the usual order of operations. Find 9 K 3 M 5.

1. List the twelve ordered pairs (K, M) and test the first equation. Only two pairs give 7: K = +, M = - (8 + 2 - 3 = 7) and K = /, M = + (8 / 2 + 3 = 7). The first equation alone does not decide.
2. Test both survivors on the second equation. With K = +, M = -: 6 - 4 + 2 = 4, not 8. With K = /, M = +: 6 + 4 / 2 = 8. Only the second pair survives.
3. Apply it: 9 K 3 M 5 = 9 / 3 + 5 = 8.

What this establishes: each given equation is a filter, and a decoding is accepted only when it passes every filter. Where it stops: if two pairs survive every given equation, the decoding is not fixed, and only a value on which both pairs agree is definite.

**Failure condition.** The method fails when the first pair that fits one equation is taken as the code. The pair K = +, M = - fits the first equation perfectly and gives 9 + 3 - 5 = 7 for the final line, a wrong answer that a hasty solver would meet among the options.

### Filling blanks with signs

A second coded-operator form prints a line of numbers with blanks between them and asks which signs, placed in the blanks, make it true. The signs may be given directly or through a letter code; either way the task is a search over sign orders, with each candidate line computed in the usual order of operations.

**Worked example (original).** Fill the three blanks in 8 _ 4 _ 3 _ 2 = 10 with three different signs chosen from +, -, x and /, using the usual order of operations. How many fillings work, and which sign is left out?

There are 4 x 3 x 2 = 24 fillings. Group them by the sign left out, so that each group of six is easy to scan.

| Sign left out | The six fillings and their values |
|---|---|
| / | 8 + 4 - 3 x 2 = 6; 8 + 4 x 3 - 2 = 18; 8 - 4 + 3 x 2 = 10; 8 - 4 x 3 + 2 = -2; 8 x 4 + 3 - 2 = 33; 8 x 4 - 3 + 2 = 31 |
| x | 8 + 4 - 3 / 2 = 10.5; 8 + 4 / 3 - 2 = 7 1/3; 8 - 4 + 3 / 2 = 5.5; 8 - 4 / 3 + 2 = 8 2/3; 8 / 4 + 3 - 2 = 3; 8 / 4 - 3 + 2 = 1 |
| - | 8 + 4 x 3 / 2 = 14; 8 + 4 / 3 x 2 = 10 2/3; 8 x 4 + 3 / 2 = 33.5; 8 x 4 / 3 + 2 = 12 2/3; 8 / 4 + 3 x 2 = 8; 8 / 4 x 3 + 2 = 8 |
| + | 8 - 4 x 3 / 2 = 2; 8 - 4 / 3 x 2 = 5 1/3; 8 x 4 - 3 / 2 = 30.5; 8 x 4 / 3 - 2 = 8 2/3; 8 / 4 - 3 x 2 = -4; 8 / 4 x 3 - 2 = 4 |

Exactly one filling works, 8 - 4 + 3 x 2 = 10, and the sign left out is /.

What this establishes: a blank-filling item is a finite search, and grouping the cases (here by the unused sign) keeps it orderly and shows that no case was skipped. Where it stops: if the signs may repeat, there are 4 x 4 x 4 = 64 fillings, and the grouping must change; read whether repeats are allowed before counting.

**Failure condition.** The search fails when each candidate is computed from left to right. Read that way, 8 / 4 + 3 x 2 becomes ((8 / 4) + 3) x 2 = 10 and looks like a second answer, while the true filling, 8 - 4 + 3 x 2, would come out as 14 and be thrown away. Apply multiplication and division before addition and subtraction in every candidate line.

### Coded values under constraints

Some items assign digits to letters and give conditions.

**Worked example (original).** K, M and N stand for different digits from 1 to 5. K + M = N, N is even, and M is greater than K. Even values of N are 2 and 4. N = 2 would need K = M = 1, which breaks "different digits". N = 4 allows K + M = 4 with different digits: (1, 3) or (3, 1). M greater than K leaves K = 1, M = 3. So K = 1, M = 3, N = 4.

**Failure condition.** The method fails when one case is skipped. List each value of the most restricted letter (here N), and rule each out or keep it with a stated reason.

### Alphametics: constrained digit solving with carries

An **alphametic** is an addition or subtraction written with letters, each standing for a different digit. This is an analytical method, not a formula. It rests on three facts about columns.

```text
  ADDITION OF TWO NUMBERS
  carry into next column:  0 or 1   (largest column sum is 9 + 9 + 1 = 19)
  a leading digit that appears only in the total must be 1

          A  B          units:  B + B = A + 10 x carry
      +      B          tens:   A + carry = B
      -------           so B = A + 1, and 2B - A = 10
          B  A          -> B = 9, A = 8:  89 + 9 = 98
```

**Method 3: units column first, carries tracked.**

1. Start with the units column. Write its sum as "digit + 10 x carry".
2. Move left, adding the carry from the column before.
3. Use the leading-digit fact: in the sum of two numbers, a new leading digit is 1.
4. Keep every letter distinct; test each surviving case in the full sum.

**Worked example (addition).** AB + B = BA. The units column gives B + B = A + 10c, where c is the carry. The tens column gives A + c = B. If c = 0, then A = B, which is not allowed. So c = 1 and B = A + 1. Substituting: 2(A + 1) = A + 10, so A = 8 and B = 9. Check: 89 + 9 = 98.

**Worked example (subtraction with a borrow).** KL - LK = M, where M is a single digit. The units column needs L - K. If L were larger than K, the tens column would give K - L, a negative digit; so K is larger, and the units column must borrow: 10 + L - K = M. The tens column, after lending, gives K - 1 - L = 0, so K = L + 1. Then M = 10 + L - (L + 1) = 9. The letter M must be 9, and K must be one more than L, but K and L themselves are not fixed: 21 - 12 = 9, 32 - 23 = 9, and so on.

What these establish: the carry and the borrow are the key unknowns; once they are fixed, the letters fall out. Where they stop: an alphametic can have several solutions. Then only facts true in all of them, such as "M is 9", are definite.

**Failure condition.** Alphametic reasoning fails when the carry is dropped between columns, or when a carry is placed in the wrong column. Write the carry above each column as you go.

### Coding from the first letter, and the every-letter reply

The tempting method is to read the first coded letter, decide "it moves back five" or "it is the mirror", and code the new word immediately. The paper prints the option that this one-letter rule produces, and often the option that a reversed-order rule produces too.

The reply is to write positions under every letter of every given pair and confirm one rule across all of them. For alphametics, the tempting method is trial and error with random digits; the reply is the units column first, with each carry written down.

### Code types that are easy to confuse

- Shift versus mirror: a constant difference versus a constant sum of 27.
- Rearrangement versus substitution: the same letters moved versus new letters in the same places.
- Sum code versus product code: add positions versus multiply them.
- Forced letter versus fixed solution: in an alphametic, one letter can be forced while others are not.

### UPSC application

This lesson covers the coding families in the paper.

- **Letter substitution and letter-shift cipher decode**: find the shift or mirror on every letter, then apply it.
- **Alphabet reversal coding and alphabet reversal position coding**: use 27 - n.
- **Letter-to-number, letter-number and alphabetic-number coding, and the multiplicative-letter code**: identify the operation (sum, product, reverse positions) from at least two words.
- **Numeric-cube code and letter-digit substitution**: test the cube rule on every number; build the letter-digit table, check that no letter has two digits and no digit two letters, and treat a clash as the sign of a position-dependent code.
- **Word-code deduction and the military coding pattern**: match shared words with shared codes; do not rely on word order.
- **Letter-rearrangement coding**: write down the position map and confirm it on a second word.
- **Symbol substitution evaluation and operator substitution**: rewrite the whole line with every symbol replaced at once, then compute in the usual order.
- **Coded-operator arrangement and symbol operation decode**: treat each given equation as a filter on the possible sign assignments, keep only the assignments that pass every filter, and calculate in the usual order at each test; for a line with blanks, search the sign orders in tidy groups and compute every candidate with multiplication and division first.
- **Coded-value constraints**: list the cases for the most restricted letter.
- **Alphametic addition and alphametic subtraction**: units column first, track carries and borrows, and report only forced facts when several solutions exist.
- **Letter-code decoding (2026 Q67, provisional)**: write positions under every letter of the given pair and confirm one rule across all of them before decoding.

### Revision points

- Write the position number under every plain and coded letter before naming a rule.
- A shift has a constant difference; a mirror has a constant sum of 27.
- One letter never proves a rule; two different rules can agree on one letter.
- Shifts wrap: subtract 26 from totals above 26.
- A mirror code decodes with the same rule that encodes.
- A rearrangement code is a position map; confirm it on a second word of the same length.
- Number codes need a second word to separate sum, product and other operations.
- In sentence codes, a word in every sentence has the code in every sentence; word order is not evidence.
- Replace every operator symbol at once, then compute in the usual order.
- In a letter-digit code, check that no letter has two digits before reading a new word.
- Coded operators: each true equation filters the sign assignments; accept only an assignment that passes all of them.
- Blank-filling: count the possible sign orders, group them, and compute each in the usual order, never left to right.
- Under constraints, list each value of the most restricted letter.
- Alphametics: units column first; a carry between columns is 0 or 1 for two addends; a new leading digit of the total is 1.
- When an alphametic has several solutions, report only the facts true in all of them.

### Practice

**MCQ 9**

In a code, PLANT is written as KOZMG and STONE is written as HGLMV. Which rule fits both, and how is RIVER written?

- A. Each letter takes its reverse-alphabet partner: IREVI
- B. Each letter moves backward by five positions: MDQZM
- C. Each letter stays, but the order is reversed: REVIR
- D. Each letter moves forwards by three alphabet positions: ULYHU

**MCQ 9 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Every pair of positions adds to 27: P (16) and K (11), L (12) and O (15), A (1) and Z (26), N (14) and M (13), T (20) and G (7); likewise S and H, T and G, O and L, N and M, E and V. So each letter becomes its reverse-alphabet partner in the same place. RIVER becomes R (18) to I (9), I to R, V (22) to E (5), E to V, R to I: IREVI.
- **B — Incorrect:** This takes the rule from the first letter only, P to K, a move of five places back. It fails on the second letter, since L moved back five is G, not O; applied anyway, it gives MDQZM.
- **C — Incorrect:** This treats the code as a rearrangement of the same letters. PLANT reversed would be TNALP, which does not match KOZMG; applied anyway, it gives REVIR.
- **D — Incorrect:** This takes the rule from the second letter only, L (12) to O (15), a move of three places forward. It fails on the first letter, since P moved forward three is S, not K; applied anyway, it gives ULYHU.

**MCQ 10**

In the addition PQ + QP = RSR, each letter stands for a different digit, and P, Q and R are not zero. Which of the following is correct?

- A. The total must be 121, so P must be larger than Q.
- B. S must be 2, so neither P nor Q can be 9 or 2.
- C. P + Q must be 11, so Q must be odd.
- D. R must be 1, so S can take more than one value.

**MCQ 10 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** The first clause is right, but the second reports a fact from one solution as if it were forced. Both 38 + 83 = 121 and 83 + 38 = 121 satisfy every condition, so P can be smaller than Q.
- **B — Correct:** PQ + QP = 11(P + Q). The total has three digits, so P + Q is at least 10, and the total lies between 110 and 198. The only multiple of 11 in that range whose first and last digits match is 121, so R = 1, S = 2 and P + Q = 11. The digits must all differ, so neither P nor Q can be 2, the digit S already uses. A 9 in either place would need a 2 in the other to make 11, so neither can be 9. Brute force confirms the solutions: 38, 47, 56, 65, 74 and 83 added to their reversals.
- **C — Incorrect:** The first clause is right, but the second transfers the odd units digit of the total to Q. The units column only needs P + Q to end in 1; 74 + 47 = 121 gives Q = 4, which is even.
- **D — Incorrect:** The first clause is right, but the second treats the middle digit as free, as if any three-digit total starting and ending in 1 would do. The total is 11(P + Q), and with P + Q = 11 every solution gives 121, so S is fixed.

---

## Lesson 5 - Directions, distance and directed networks

Progress: Lesson 5 of 18 | Stage: Foundation | Subtopic: Directions, distance and directed networks

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A person walks north, turns right, walks again, turns left, walks again, and you are asked how far they are from the start and in which direction. Or a map of one-way roads or railway lines is described in words, and you must say which journeys are possible, which town every route must pass through, or what changes when one link is closed. Holding these paths in your head is how errors happen: a left turn becomes a right turn, a one-way arrow is travelled backwards. This lesson puts every path onto paper: a compass and a pair of axes for walks, and arrows for networks.

The first lesson treated an "if ... then" sentence as a one-way arrow. A one-way road is the same idea on a map: you may travel along the arrow, never against it.

### Visual: compass, axes and a one-way network

```text
           N (0°)                      y
           ▲                           ▲      final point (6, 8)
  NW       │       NE                  │         ●
     ╲     │     ╱                     │        ╱
W ◄───────┼───────► E  (90°)          8├      ╱  displacement:
(270°)    │                            │    ╱    √(6² + 8²) = 10 km
     ╱     │     ╲                     │  ╱      north-east quadrant
  SW       │       SE                  │╱
           ▼                       ────●──────────► x
           S (180°)                  start   6

  RIGHT turn = +90° (clockwise)     LEFT turn = -90° (anticlockwise)
  two rights = 180° = U-turn         right then left = original heading

  ONE-WAY NETWORK
     A ───► B ───► C
     ▲      │      │
     └──────┼──────┘   (C ───► A)
            ▼
            D ───► E ───► F
                   │
                   └───► B   (E ───► B)
```

The compass on the left gives each direction an angle measured clockwise from north. A right turn adds 90 degrees; a left turn subtracts 90 degrees. The axes in the middle are where a walk is added up: north and east are positive, south and west negative. The final point is joined to the start by one straight arrow, the **displacement**, whose length is found by the Pythagoras rule and whose direction is read from the quadrant. The network at the bottom shows one-way links as arrows. A journey may follow arrows only. Here C leads back to A, and E leads back to B, so there are loops, and F has no exit.

### Net effect and the walker's own left and right

A walk is a list of moves, and only the net effect matters for "how far from the start". Walking 4 km north and then 4 km south leaves you where you began, however tired you are. So you add north and subtract south, add east and subtract west, and then measure the straight line from start to finish.

The harder part is turning. "Right" and "left" are relative to the direction the walker is facing at that moment, not to the page. A walker facing south who turns left now faces east. Keep track of the heading after every turn.

The analogy with the page has a limit. On a map, left is always west; for a walker, left depends on the heading. That difference is the source of the most common error in this family.

### Method 1: track the heading, then sum signed displacements

1. Fix the starting heading as an angle: north 0, east 90, south 180, west 270 degrees.
2. After each turn, update the heading: right adds 90, left subtracts 90, and any stated angle is added (clockwise) or subtracted (anticlockwise). Wrap round 360.
3. Convert each walk into an (east, north) change: north (0, +d), east (+d, 0), south (0, -d), west (-d, 0).
4. Add all the east changes and all the north changes separately.
5. Distance from start = the square root of (east total squared + north total squared). Direction = the quadrant of the final point.

**Failure condition.** The method fails when a turn is applied to the page instead of to the walker's heading. "Left" for a walker facing south is east, not west. Write the new heading after every turn before converting the walk.

### Worked example: two rights make a U-turn

A man walks 3 km north, turns right and walks 4 km, turns right again and walks 3 km. Headings: north, then east (one right), then south (a second right). Changes: (0, +3), (+4, 0), (0, -3). Totals: east 4, north 0. He is 4 km due east of the start.

What this establishes: two right turns reverse the heading, so the first and third legs cancel when their lengths match. Where it stops: if the third leg were 5 km instead of 3, he would end 2 km south of his starting line, and the distance would be √(16 + 4), about 4.5 km, in the south-east quadrant.

### Worked example: a mixed walk

A woman walks 5 km north, turns right and walks 2 km, turns left and walks 3 km, then turns right and walks 4 km. Headings: north; right to east; left back to north; right to east. Changes: (0, +5), (+2, 0), (0, +3), (+4, 0). Totals: east 6, north 8. Distance √(36 + 64) = 10 km. The point (6, 8) lies north-east of the start, closer to north.

What this establishes: a right followed by a left restores the original heading. Where it stops: "north-east" here names a quadrant. If an option asks for an exact bearing, compare the east and north totals: equal totals mean exactly north-east (45 degrees); here north is larger, so the point lies between north-east and north.

### The left-turn trap

Each right turn is +90 degrees, clockwise. Each left turn is -90 degrees, anticlockwise. The trap is to treat a left turn as clockwise as well, or to swap the two.

**Worked example.** Facing west, a walker turns left. West is 270 degrees; minus 90 gives 180, which is south. Treating the left turn as clockwise would give 360, that is north, and send every later leg the wrong way.

**Failure condition.** The trap catches you whenever the walker faces south or west, because then "left" points towards the east or south side of the page, which feels wrong. Trust the angle arithmetic over the feeling.

### Method 2: rotations by stated angles

Some items give turns in degrees: "turns 135 degrees clockwise, then 270 degrees anticlockwise".

**Worked example (original).** A guard faces east, turns 135 degrees clockwise, then 270 degrees anticlockwise, then 45 degrees clockwise. Start at 90. After the first turn: 90 + 135 = 225 (south-west). After the second: 225 - 270 = -45, which wraps to 315 (north-west). After the third: 315 + 45 = 360, which is 0, north. The guard faces north.

What this establishes: a run of turns reduces to one signed sum, wrapped round 360. Where it stops: if the item uses eight compass points, each step of 45 degrees is one point; for sixteen points, each step is 22.5 degrees.

**Failure condition.** Rotation arithmetic fails when the starting heading is taken as 0 even though the walker starts facing another way. Always convert the starting heading first.

### Two walkers on a square path in opposite directions

A square path invites a different kind of direction item: two people start at one corner and walk round in opposite directions.

**Worked example (original).** A square park has corners K (south-west), L (south-east), M (north-east) and N (north-west), each side 3 km, so the perimeter is 12 km. Riya walks from K towards L at 2 km per hour; Sam walks from K towards N at 1 km per hour. Walking in opposite directions round a closed path, they meet when their distances add to the perimeter: combined speed 3 km per hour, so they meet after 12 / 3 = 4 hours. Riya has walked 8 km: K to L (3), L to M (6), then 2 km along the north side towards N. Sam has walked 4 km: K to N (3), then 1 km along the north side towards M. The north side is 3 km, so 2 km west of M is 1 km east of N: the same point.

What this establishes: on a closed path, opposite walkers meet after a combined distance of one perimeter. Where it stops: if they walk in the same direction, the faster one catches the slower one after gaining a full perimeter, so use the difference of speeds instead.

**Failure condition.** The method fails when the meeting is placed by one walker's distance without checking the other's. Locate both walkers; they must be at the same point.

### Part B - Directed networks

### Visual: a reachability table

| From \ To | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| A | - | direct | via B | via B | via B, D | via B, D, E |
| B | via C | - | direct | direct | via D | via D, E |
| C | direct | via A | - | via A, B | via A, B, D | via A, B, D, E |
| D | via E, B, C | via E | via E, B | - | direct | via E |
| E | via B, C | direct | via B | via B | - | direct |
| F | none | none | none | none | none | - |

This table summarises the network in the first visual. Each cell says whether the column town can be reached from the row town, and through which towns the shortest chain of arrows passes. Read across a row to see everything a traveller from that town can reach. The F row is empty: F has arrows coming in but none going out, so a traveller who reaches F is stuck.

### Arrows followed head to tail

A one-way network is a set of arrows, and a journey is a chain of arrows followed head to tail. Being able to get from A to B says nothing about getting from B back to A. The question "can I reach X?" is answered by following arrows outward from the start and marking every town you touch.

### Method 3: treat each arrow as one-way and test each claim against every route

1. Write the arrows as a list, and sketch them.
2. **Reachability.** From the starting town, mark every town one arrow away; then every town one arrow from those; continue until nothing new is marked.
3. **Necessity ("every route passes through X").** Remove X and repeat the reachability test. If the destination becomes unreachable, X is necessary.
4. **Closing a link.** Delete that one arrow and redo the reachability test.
5. **Revisit questions.** For a journey that must visit towns in a stated order, find the forced route for each leg, and see which towns appear in more than one leg.

**Failure condition.** The method fails when an arrow is travelled backwards. Before using any link, check its direction against the list. It also fails when "every route" is judged from one convenient route; a necessity claim needs the removal test.

### Worked example: reachability and necessity

In the network above (A to B, B to C, C to A, B to D, D to E, E to B, E to F), find every route from A to F that does not repeat a town. From A the only arrow goes to B. From B, the arrow to C leads back to A, so it cannot help reach F without repeating a town; the arrow to D goes on to E, and E leads to F. So the only such route is A, B, D, E, F.

Is D necessary for every A-to-F journey? Remove D. From A: B; from B: C (D is gone); from C: A. F is never reached. So every A-to-F journey passes through D. The same test shows that B and E are necessary too.

What this establishes: the removal test proves necessity for every route, including long ones with loops. Where it stops: necessity says nothing about how many routes exist. To count routes, list them one at a time from the start town, as in the first paragraph of this example, refusing any route that repeats a town.

### Worked example: a town that must be revisited

A journey must start at A, reach C, and then end at F. The first leg is forced: A, B, C. From C the only arrow goes to A, then to B, then D, E, F. So the full journey is A, B, C, A, B, D, E, F. Towns A and B are necessarily visited twice: there is no other arrow out of C, and no other arrow out of A.

**Failure condition.** A revisit claim is "necessary" only if no alternative arrow exists at the point of the loop. If C had a second outgoing arrow towards D, the revisit of B could be avoided.

### Worked example: closing a link

Close the link from B to D. From A, a traveller reaches B, then C, then A again, and nothing else. D, E and F become unreachable from A. A single closure has cut the network in two.

**Failure condition.** After a closure, redo the whole reachability test from the start. Do not assume that towns reachable before are still reachable by a "nearby" route.

### Directly connected towns

Two towns are **directly connected** when one arrow joins them, in either direction. A and B are directly connected (A to B). A and D are not: the journey from A to D needs B in between.

**Failure condition.** "Directly connected" and "reachable" are different. A town can be reachable through a long chain without being directly connected.

### Networks with distances and bearings

Some items attach a length and a compass direction to each link and ask for the straight-line distance between two towns, or the length of the shortest route.

**Worked example (original).** From town G, a road runs 4 km north to H. From H, a road runs 3 km east to J. From J, a road runs 4 km south to K. Placing G at (0, 0): H is (0, 4), J is (3, 4), K is (3, 0). The straight-line distance from G to K is 3 km, due east. The road distance is 4 + 3 + 4 = 11 km.

**Failure condition.** The method fails when the road distance is reported as the straight-line distance, or the other way round. Read which one the stem asks for.

### Picturing instead of plotting, and the reply

For walks, the tempting method is to picture the path and estimate. It works for two legs and fails for four, especially when the walker faces south or west and a left turn points across the page. The reply is to write the heading after every turn and to add signed displacements on axes.

A second tempting method is to add all the leg lengths and call that the distance. That is the length of the path walked, not the distance from the start. The reply is to ask which one the stem wants: "how far did he walk" is the path length; "how far is he from the start" is the displacement.

For networks, the tempting method is to find one route and treat it as the only route, or to travel an arrow backwards because the towns "look connected". The reply is to keep the arrow list in view and to use the removal test for any "every route" claim.

### Distances and links that are easily mixed up

- Path length versus displacement: total walked versus straight line from start to finish.
- Right versus left: +90 degrees versus -90 degrees, relative to the current heading.
- Reachable versus directly connected: some chain of arrows versus a single arrow.
- Possible route versus necessary town: one route exists versus every route passes through it.

### UPSC application

This lesson covers two clusters of families.

- **Direction sense.** Multi-turn direction sense, rotational direction sense, opposite-direction square paths, and direction turns with distance (2026 Q56, provisional). Track the heading after every turn, sum signed displacements, and use the Pythagoras rule for the straight-line distance.
- **Directed networks.** The direct route between two named towns, a city necessarily revisited, a directly connected city pair, directed railway route necessity, the route after closing one link, and direction-network distance. Follow arrows only; use the removal test for necessity; redo reachability after a closure; and separate road distance from straight-line distance.

### Revision points

- Give every heading an angle: north 0, east 90, south 180, west 270 degrees.
- A right turn adds 90 degrees; a left turn subtracts 90 degrees, both relative to the current heading.
- Two right turns make a U-turn; a right followed by a left restores the heading.
- Write north and east as positive, south and west as negative, and add each axis separately.
- Distance from the start is the square root of (east total squared + north total squared).
- Read the direction from the quadrant; compare the two totals for a finer bearing.
- Path length is not displacement; read which one is asked.
- For turns in degrees, add clockwise and subtract anticlockwise, then wrap round 360.
- On a closed path, opposite walkers meet after a combined distance of one perimeter.
- In a network, travel along arrows only, never against them.
- "Every route passes through X" is tested by removing X and checking reachability.
- After closing a link, redo reachability from the start.
- A revisit is necessary only when no other arrow leaves the loop point.

### Practice

**MCQ 11**

One-way roads link five towns: P to Q, P to S, Q to R, S to R, R to T, and T to S. No other roads exist. Which of the following must be true?

- A. Every P-to-T route uses both Q and R.
- B. There are three distinct P-to-T routes.
- C. Every route from P to T passes through R.
- D. A traveller starting at T can eventually reach Q by road.

**MCQ 11 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** This treats one convenient route as the only route. The route P, S, R, T reaches T without Q, so the verdict "Q is necessary" fails.
- **B — Incorrect:** This travels the road from T to S backwards, as if it ran from S to T, and so counts P, S, T as a third route. Listing routes from P that never repeat a town gives only two: P, Q, R, T and P, S, R, T. The only road into T comes from R, so no route can reach T straight from S.
- **C — Correct:** The only road into T comes from R, so every route that ends at T must pass through R. The removal test confirms it: delete R, and from P a traveller reaches Q and S but nothing further, so T is unreachable. Listing the routes gives P, Q, R, T and P, S, R, T, and both contain R.
- **D — Incorrect:** This sees the loop T, S, R and then travels the road from Q to R backwards, as if R led on to Q. From T the only road goes to S, from S only to R, and from R only back to T, so the towns reachable from T are S, R and T itself. The only road into Q comes from P, which no road enters, so Q cannot be reached from T.

**MCQ 12**

Asha and Bina start from the same point. Asha walks 3 km north, turns right and walks 1 km. Bina walks 12 km south, turns left and walks 9 km, then turns left again and walks 9 km. Which statement about where Asha ends up, compared with Bina, is correct?

- A. Asha is 10 km due east of Bina.
- B. Asha is 17 km from Bina.
- C. Asha is 10 km to the east and 6 km north of Bina.
- D. Asha is 8 km west and 6 km north of Bina.

**MCQ 12 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** This starts Bina facing north instead of south. Her legs then become 12 km north, 9 km west and 9 km south, ending at (-9, 3); Asha at (1, 3) would be 10 km due east of that point, but Bina never went north first.
- **B — Incorrect:** This drops Bina's last leg. Stopping her at (9, -12) puts Asha 8 km west and 15 km north of her, which is 17 km by the Pythagoras rule; the final 9 km north brings Bina much closer.
- **C — Incorrect:** This turns Bina clockwise at each "left". From south, two clockwise turns send her west and then north, ending at (-9, -3), so Asha appears 10 km east and 6 km north of her; a left turn is anticlockwise.
- **D — Correct:** Asha: north 3, then a right turn from north faces east, 1 km: she ends at (1, 3). Bina: south 12 to (0, -12); a left turn from south faces east, 9 km to (9, -12); a second left turn from east faces north, 9 km to (9, -3). Asha minus Bina is (1 - 9, 3 - (-3)) = (-8, 6): 8 km west and 6 km north, which is 10 km in a straight line.

---

## Lesson 6 - Blood relations and family graphs

Progress: Lesson 6 of 18 | Stage: Core | Subtopic: Blood relations and family graphs

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Pointing to a photograph, a man says, 'Her father is the only son of my grandfather.'" Or: "A # B means A is the father of B; A @ B means A is the sister of B." Or six people, three generations, a handful of clues, and the question "who is the husband of whom?". Family items are short, and they are lost in two ways: by tracing a chain of relations in the head and losing one generation, and by assuming something the clues never said, usually a person's sex, or that "only son" means "only child". This lesson builds a small family graph on paper and reads every answer off it.

The second lesson taught you to accept only what holds in every consistent case. Family items use the same rule: if the clues allow two different family pictures, only what is true in both is definite.

### Visual: a labelled family graph

```text
  GENERATION 1      [Hari] ════ (Uma)
                           │
              ┌────────────┴────────────┐
  GENERATION 2   [Dev] ════ (Rina)      (Mala) ════ [Kiran]
              │                              │
         ┌────┴────┐                         │
  GENERATION 3   (Asha)   <Neel>                   [Om]

  KEY   [ ] male     ( ) female     < > sex not stated
        ════ married couple     │ parent to child     ┌──┴──┐ siblings
```

Each row is one generation, so a step up or down a row is a parent or child link, and a step along a row is a sibling or a spouse. Square brackets mark males, round brackets females, and angle brackets a person whose sex the clues have not given. The double line joins a married couple; the vertical lines run from parents to children; a horizontal bar groups siblings. Once the graph is drawn, every relation is a path: Om to Asha goes up to Mala, across to her brother Dev, and down to Asha, so Om and Asha are first cousins. Neel's sex is not stated, so Neel can be called Asha's sibling, but not her brother or sister.

### Relation words as compressed walks

Relation words are compressed paths. "Uncle" means "a brother of a parent" or "a husband of a parent's sister". "Nephew" means "a son of a sibling". When a sentence strings several relation words together, it is describing a walk through the family, one step at a time. If you take the walk on paper, step by step, you cannot lose a generation.

The analogy has a limit. A walk on a map has one meaning, but relation words can hide a choice: "uncle" can be on the father's or the mother's side, and "brother-in-law" can be a spouse's brother or a sister's husband. When a word hides a choice, the graph must show both branches until a clue removes one.

### The vocabulary as paths

| Word | Path in the graph | Hidden choice |
|---|---|---|
| Paternal grandfather | father's father | none |
| Maternal uncle | mother's brother | none |
| Uncle | parent's brother, or parent's sister's husband | which parent; blood or marriage |
| Aunt | parent's sister, or parent's brother's wife | which parent; blood or marriage |
| Nephew / niece | sibling's son / daughter | none |
| First cousin | parent's sibling's child | which parent |
| Brother-in-law | spouse's brother, or sister's husband | which route |
| Daughter-in-law | son's wife | none |
| Grandchild | child's child | through which child |

Read each row as a path to walk on the graph. The last column lists the choices the word leaves open; those are exactly where wrong options are built.

### Method: build the graph from the clue that fixes most

1. **Classify and draw.** Set out generation rows and the key for sex markers.
2. **Enter the strongest clue first.** A clue that fixes a person's sex and generation at once, such as "X is the only daughter of Y", goes in before vague clues such as "X and Y are related".
3. **Add each further clue and check consistency.** After every addition, re-read the earlier clues against the graph.
4. **Read the asked relation as a path.** Walk from one person to the other and translate the walk into a word.
5. **Keep unknowns as unknowns.** If a sex or a side is not fixed, the answer must allow both, or the option set must be judged on what is forced.

**Failure condition.** The method fails when a person's sex or generation is assumed. A name does not fix sex; "child", "sibling", "parent" and "spouse" do not fix sex; and "related to" does not fix generation. Mark such people with the "not stated" marker and carry the uncertainty.

### "Only son" and "only daughter"

"X is the only son of Y" says that Y has no other son. It does not say that Y has no daughters. Likewise, "only daughter" removes other daughters, not sons. These phrases remove siblings of the same stated sex, and nothing more.

The phrase also tells you who the person is, once you know the speaker's position.

**Worked example (the speaker inside the phrase).** A woman says of a boy, "He is the son of the only daughter of my father." The woman is herself a daughter of her father. If her father has only one daughter, that daughter is the woman. So the boy is her son.

**Worked example (the speaker outside the phrase).** A man says of a boy, "He is the son of the only daughter of my father." The man is a son, not a daughter, so the only daughter of his father is his sister. The boy is his sister's son, his nephew.

What these establish: the speaker's own sex decides whether an "only son" or "only daughter" phrase points to the speaker. Where they stop: if the speaker's sex is not stated, both readings remain open, and only facts common to both are definite.

**Failure condition.** The phrase is misread when "only son" is treated as "only child". If a clue says "R is the only son of S" and another says "T is S's daughter", the two do not clash; T is R's sister.

### Worked example: the sister through a grandfather

A male speaker says, "She is the daughter of my paternal grandfather's only son." Draw it. The paternal grandfather is the speaker's father's father. His only son must be the speaker's father, because the speaker's father is one of his sons and there is only one. The woman is the daughter of the speaker's father, so she is the speaker's sister.

```text
  [paternal grandfather]
           │  (only son)
       [father]
     ┌─────┴─────┐
  [speaker]    (she)     -> sister
```

What this establishes: "my paternal grandfather's only son" collapses to "my father". Where it stops: if the phrase were "my maternal grandfather's only son", it would point to the speaker's maternal uncle, not the father, and the woman would be a cousin.

### Reading coded relations

Some items code relations as symbols. Decode each symbol into one edge of the graph, draw the edges in order, then read the path.

**Worked example (original).** Let A + B mean "A is the brother of B", A - B mean "A is the daughter of B", and A x B mean "A is the wife of B". Read K + L - M.

- K + L: K is the brother of L, so K is male and K and L are siblings.
- L - M: L is the daughter of M, so L is female and M is L's parent.
- Therefore K is a son of M.

Is M the mother of K? The clues give no sex for M; M is a parent of unstated sex. So "K is M's son" is definite, but "M is K's mother" is not.

What this establishes: each symbol is one step, and the path is read only through stated steps. Where it stops: if the expression were extended to K + L - M x N, then M would be N's wife. Whether K is then N's son depends on a convention: that a married couple's children are children of both. This lesson uses that convention only when it is stated, and a careful stem states it whenever the answer depends on it; otherwise K is definitely M's son but only possibly N's.

**Failure condition.** Coded reading fails when the direction of a symbol is reversed. "A - B means A is the daughter of B" puts A below B in the graph, not above. Write each decoded edge as "upper person, lower person" before chaining.

### Statement sufficiency for a relation

Some items ask whether given statements are enough to establish a relation.

**Worked example (original).** Question: is J the grandmother of K?

- Statement 1: J is the mother of K's father. This fixes both J's sex and the two generations. Sufficient.
- Statement 2: J is the mother of L, and L is a parent of K. This also fixes J as a female two generations above K. Sufficient.
- Statement 3: J is a parent of K's father. This fixes the generations but not J's sex. J could be the grandfather. Not sufficient.

**Failure condition.** Sufficiency is judged on the statement as written. If you fill in a sex because "it is probably the grandmother", you have added a fact that the statement did not give.

### Couples, counts and family inference

**Worked example (couples).** At a family gathering are grandparents A and B; their son C and daughter D; C's wife E; D's husband F; two children of C and E; and one child of D and F. Draw three generations. The married couples are A and B, C and E, D and F: three couples. A has three grandchildren.

**Worked example (inference puzzle, original).** Five members, V, W, X, Y and Z. V is the mother of W. X is W's only brother. Y is X's wife. Z is Y's daughter. Build the graph: V above W and X; X married to Y; Z below X and Y.

- Z is V's granddaughter only if Z is X's child as well as Y's. The clues say only that Z is Y's daughter, so this needs the convention that a married couple's children are children of both; without it, Z could be Y's daughter from an earlier marriage, and the granddaughter link is possible but not definite.
- W is Z's aunt or uncle, since W is X's sibling; W's sex is not stated, so the word must be "parent's sibling" until a clue fixes it.
- "X is V's only son" follows from "X is W's only brother" only if W is female; if W is male, W is also V's son. So V's number of sons is not fixed.

What this establishes: an inference puzzle is a graph plus a list of unknowns, and options that need an unknown are not definite. Where it stops: if an option asks "how many males", count only those whose sex is stated or forced.

### Ages on a family graph: possible ranges

Some items attach ages to family members and ask what age a cousin or relative can have. Put each age on its node, and turn each clue into an inequality.

**Worked example (original).** S is R's father. T is S's sister, and V is T's son, so R and V are first cousins. S is 36. T is 4 years younger than S, so T is 32. T had V when she was between 22 and 26, inclusive. R is 10. Then V's age is 32 minus a number from 22 to 26, which gives 6 to 10. V can be younger than R or the same age, but cannot be older.

**Failure condition.** An age range is only as wide as the clues allow. If a clue gives a strict "between" (excluding the ends), the range shrinks by one at each end. Read whether the bounds are inclusive.

### Translating in the head, and the graph reply

The tempting method is to translate a long relation sentence word by word in the head and land on the first familiar word. A second tempting method is to fill gaps with "normal" assumptions: that a person called Rina is female, that an only son is an only child, that a person mentioned in the same breath is of the same generation.

The reply is the graph. Draw each stated edge; mark unknown sexes as unknown; and translate only the path you can see. When the graph leaves two possibilities, the answer must cover both.

### Family terms that are easily swapped

- Only son versus only child: the first removes other sons only.
- Paternal versus maternal: the father's side versus the mother's side, fixed by the sex of the linking parent.
- Parent versus mother or father: "parent" leaves sex unstated.
- Definite versus possible: true in every graph the clues allow versus true in at least one.

### UPSC application

This lesson's method covers these family-relation question types in the paper.

- **Blood-relation deduction, logical relation deduction and family-relation deductions**: build the graph from the clue that fixes most, and read the asked relation as a path.
- **Symbolic family relation and coded relational chain deduction**: decode each symbol into one edge, keep the direction of each edge, and refuse to supply an unstated sex.
- **Family inference puzzle and family couples**: draw all generations, count married pairs from the graph, and list the unknowns before judging options.
- **Family-relation statement sufficiency**: a statement is sufficient only if it fixes both the generation and any sex that the question names.
- **Cousins' possible age**: attach ages to nodes and turn each clue into an inequality.
- **Blood-relation tree (2026 Q44, provisional)**: draw the tree from the clue that fixes most, and keep any unstated sex as unknown.

### Revision points

- Draw generation rows; mark males, females and unknown sexes with distinct markers.
- Relation words are paths; translate each path step by step.
- Enter the clue that fixes most (sex and generation together) first.
- Re-check earlier clues after each addition to the graph.
- A name, "child", "sibling", "parent" and "spouse" do not fix sex.
- "Only son" removes other sons, not daughters; "only daughter" removes other daughters, not sons.
- The speaker's own sex decides whether an "only son" or "only daughter" phrase points to the speaker.
- "My paternal grandfather's only son" is the speaker's father.
- In coded relations, write each edge as upper person and lower person before chaining.
- A sufficiency statement must fix the generation and any sex the question names.
- "A married couple's child is the child of both" is a convention; use it only when the stem states it, and otherwise keep the second parent as possible, not definite.
- Only facts true in every graph the clues allow are definite.

### Practice

**MCQ 13**

X says to Y, "The sister of your mother's husband is my aunt." Use these conventions: "aunt" means a sister of one's parent; every brother or sister shares both parents with their sibling; every child's two parents are married to each other; no one has more than one spouse; and no one is married to a blood relative. X and Y are different people. How is X related to Y?

- A. Y's sibling, or Y's first cousin
- B. Y's first cousin, but not Y's sibling
- C. Y's sibling only
- D. Y's maternal first cousin, or else Y's brother or sister

**MCQ 13 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Y's mother's husband is Y's father, because Y's parents are married and each has one spouse. His sister, call her Z, is a child of Y's paternal grandparents. Z is X's aunt, so Z is a sister of one of X's parents, and that parent is another child of the same grandparents. If that parent is Y's father, X is Y's full sibling, since X's other parent must be Y's father's only spouse, Y's mother. If it is another child of those grandparents, X is Y's first cousin. Both cases are consistent with every clue, and no other case exists.
- **B — Incorrect:** This assumes the roundabout wording must point away from Y's own father. Nothing stops Z from being X's aunt through Y's father himself, which makes X Y's sibling, so "not Y's sibling" is not forced.
- **C — Incorrect:** This assumes Z has only one brother or sister, Y's father. The clues allow Z further siblings, and a child of any of them is also Z's niece or nephew, making X Y's first cousin instead.
- **D — Incorrect:** This drops the "husband" step and reads the clue as "the sister of your mother", which would put the link on Y's mother's side. The chain runs through Y's mother's husband, Y's father. A model in which X's parent is a further brother or sister of Y's father, married to someone unrelated to Y's mother, makes X a cousin on the father's side only: X is then neither Y's sibling nor Y's maternal cousin, so this description fails in that case.

**MCQ 14**

In a code, A ★ B means A is the son of B; A ◆ B means A is the sister of B; and A ▲ B means A is the husband of B. Assume every brother or sister shares both parents with their sibling and no one is married to a blood relative. If J ★ K ◆ L ▲ M, which of the following must be true?

- A. M is the wife of J's brother, namely L
- B. M is married to L, who is J's mother's brother
- C. M is the wife of J's paternal uncle, L
- D. M is J's maternal grandmother: K's own mother

**MCQ 14 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** This drops a generation, attaching L to J instead of to K. K ◆ L makes L a brother of K, J's parent; L cannot also be J's brother, because a brother of J shares J's parents and K would then be L's parent as well as L's sister.
- **B — Correct:** Decode each edge. J ★ K: J is K's son, so K is J's parent. K ◆ L: K is L's sister, so K is female and is J's mother, and L is her sibling. L ▲ M: L is M's husband, so L is male, a brother of J's mother, and M is his wife. Read as one chain, J to K is son to mother, K to L is sister to brother, and L to M is husband to wife, so M is J's mother's brother's wife: L is J's maternal uncle and M is married to him.
- **C — Incorrect:** This ignores the sex fixed by the sister symbol. K ◆ L makes K female, so K is J's mother, not J's father, and L is on J's mother's side; L could be J's father's brother as well only if K had married her own brother, which the stem rules out.
- **D — Incorrect:** This reads K ◆ L as "K is the daughter of L", moving L up a generation. Then L would be J's maternal grandfather and M his wife; but the symbol means sister, so L stays in K's generation, and M, married to K's brother, cannot also be K's mother under the stated conventions.

**MCQ 15**

K, L, M, N, V and W are six different people. K is L's paternal grandmother. M is K's only son. N is M's wife. V is L's sister. W is N's mother. Assume every brother or sister shares both parents with their sibling, every child's two parents are married to each other, no one has more than one spouse, and no one is married to a blood relative. Which of the following must be true?

- A. L is the son of M.
- B. V is K's only granddaughter.
- C. W is the maternal grandmother of V.
- D. L and V are the only children of M and N.

**MCQ 15 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** This assumes a sex that no clue gives. "V is L's sister" fixes V as female, but L may be V's brother or V's sister, so "son" is possible, not forced.
- **B — Incorrect:** This reads "only son" as "only child" and treats L as male. K may also have daughters with daughters of their own, and L may be a girl; either case gives K a second granddaughter, so "only granddaughter" is possible but not forced.
- **C — Correct:** L's father is a son of K, and K has only one son, so L's father is M. L's parents are married and M has one spouse, so L's mother is N. V shares both parents with L, so N is V's mother as well. W is N's mother, so W is V's mother's mother, her maternal grandmother. Every model satisfying the clues gives this.
- **D — Incorrect:** This treats the people named in the clues as the whole family. Nothing stops M and N from having a third child, so "L and V are their only children" is possible but not forced.

---

## Lesson 7 - Ranking, ordering and comparison chains

Progress: Lesson 7 of 18 | Stage: Core | Subtopic: Ranking, ordering and comparison chains

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### The problem you face

You are told that one person is older than a second, that a third is younger than the first but older than someone else, and that a fourth is "not the youngest". Then you are asked who is third oldest, or whether a claim "must be true". Holding five names and six comparisons in your head is where marks are lost. The cure is to turn every comparison into a position on a ladder, so that the ladder, not your memory, answers the question.

### Visual: one ladder, two ways of counting, and a chain

```text
   RANKED LADDER (a row or a class of N = 9)

   from the TOP          position        from the BOTTOM
   (or left end)                         (or right end)
        1   ..........  [ Asha  ]  ..........   9
        2   ..........  [ Bilal ]  ..........   8
        3   ..........  [ Chitra]  ..........   7
        4   ..........  [ Dev   ]  ..........   6
        5   ..........  [ Ela   ]  ..........   5     <- the median of 9
        6   ..........  [ Farid ]  ..........   4
        7   ..........  [ Gita  ]  ..........   3
        8   ..........  [ Hari  ]  ..........   2
        9   ..........  [ Isha  ]  ..........   1

   RULE ON EVERY RUNG:  top-rank + bottom-rank = N + 1

   COMPARISON CHAIN (">" means "older than")

     Gopal > Lata > Mohan        Gopal > Rekha
         \______________/            \
          Gopal > Mohan  (transitive) Rekha vs Lata?  NO LINK -> unknown
```

Read the ladder first. Each person stands on one rung. The number on the left is the rank counted from the top; the number on the right is the rank counted from the bottom. On every rung the two numbers add to 10, which is N + 1 for N = 9. The person is counted once from each end, so the sum is one more than the number of people.

Now read the chain. Gopal is older than Lata, and Lata is older than Mohan, so Gopal is older than Mohan. That step is called **transitivity**: if one person beats a second and the second beats a third, the first beats the third. But Rekha hangs off Gopal on a separate branch. We know Gopal is older than Rekha, and we know Gopal is older than Lata, yet nothing links Rekha with Lata. A missing link means the order between them is unknown, not that it is whatever looks natural.

### A queue and a staircase

Think of a queue at a ticket counter. If you are 4th from the front of a queue of 12, you are 9th from the back. You did not move; only the end from which you counted changed. Every "from the end" question is that single fact in disguise.

Comparisons work like a staircase. "Taller than" is a step up. If you can walk up from one name to another by a sequence of steps that all go up, you know the order. If you need to go up one branch and down another, you know nothing about the two ends of that walk.

### Switching the end you count from

- **The fact.** In a single line of N people, rank from the top plus rank from the bottom equals N + 1. So rank from the bottom = N + 1 - rank from the top.
- **Try it.** In a class of 35, Kavya is 11th from the top. Her rank from the bottom is 35 + 1 - 11 = 25. Check with a small case: in a line of 3, the middle person is 2nd from either end, and 2 + 2 = 4 = 3 + 1.
- **Scope.** It converts a rank when there is one line and the person does not share a rung with anyone. Ties need the separate care described below under ties.
- **Where it breaks.** The rule fails when you forget the "+ 1". Subtracting directly, 35 - 11 = 24, counts the people below Kavya, not her own rank from the bottom. The difference between "people below me" and "my rank from the bottom" is exactly one person: Kavya herself.

### One person, two ranks: the length of the row

- **The fact.** If one person is p-th from the left and q-th from the right, the row has p + q - 1 people.
- **Try it.** Nikhil is 8th from the left and 15th from the right. The row has 8 + 15 - 1 = 22 people. Nikhil is counted in both numbers, so we subtract him once.
- **When people exchange places.** An exchange does not move any rung; it only swaps the names written on two rungs. So track rungs, not people: write every rung's rank from one end, then move the names. Everyone who is not part of an exchange keeps the rank they had.
- **Worked example: a chain of exchanges.** A row has 25 people. Ravi is 7th from the left, Sunil is 6th from the right and Meena is 10th from the left. First Ravi and Sunil exchange places; then Meena and Ravi exchange places. Where does each of the three end up? Convert everything to the left end first: Sunil's rung is 25 + 1 - 6 = 20th from the left. After the first exchange, Ravi is on rung 20 and Sunil on rung 7; Meena has not moved from rung 10. After the second exchange, Meena takes rung 20 and Ravi takes rung 10. Final picture: Sunil 7th, Ravi 10th and Meena 20th from the left, which makes Meena 25 + 1 - 20 = 6th from the right. Only three rungs (7, 10 and 20) were ever involved, and the 22 other people never changed rank.
- **Where it breaks.** Combining two numbers that do not describe the same rung gives nonsense. Ravi's old rank from the left and Sunil's old rank from the right sit on two different rungs, so their sum or difference is nobody's position. Convert every rank to one end before any name moves.

### Counting the people in between, and the shortest possible row

- **The fact.** If X is at position a and Y at position b, counted from the same end, the number of people strictly between them is |a - b| - 1.
- **Try it.** In a row, Uma is 5th from the left and Varun is 13th from the left. Between them stand 13 - 5 - 1 = 7 people.
- **Positions from opposite ends.** When X is a-th from the left and Y is b-th from the right, two pictures are possible: X to the left of Y, or the two "crossing over" so that Y lies to the left of X. A question asking for the least number of people in the row often depends on the crossing picture. Suppose X is 7th from the left and Y is 9th from the right, with 3 people between them. If X is left of Y, the row is 7 + 3 + 9 = 19. If they cross so that Y is left of X, then Y stands 4 places left of X, at position 3 from the left, and the row has 3 + 9 - 1 = 11 people. The least possible row is 11.
- **When the method fails.** The method fails when you assume only one picture. If the question asks "how many at least" or "how many at most", draw both pictures before choosing.

### Placing the clue that fixes the most

Enter first the clue that fixes the most: an absolute position ("is the oldest", "is 3rd from the top") beats a relative clue ("is older than Mohan"), and a relative clue with a fixed person beats a relative clue between two unplaced people.

Six runners, Ajay, Bina, Chetan, Divya, Esha and Firoz, finish a race with no ties. Clues: (a) Chetan finishes 2nd. (b) Divya finishes just ahead of Esha. (c) Ajay finishes ahead of Firoz but behind Esha. (d) Bina is not last. Start with (a): Chetan is 2nd. Clue (c) with (b) gives a block: Divya, Esha, then later Ajay, then later Firoz. That is four people in order, and only positions 1, 3, 4, 5, 6 are open. Who can be 1st? Esha, Ajay and Firoz each have someone ahead of them, so only Bina or Divya can lead. If Divya were 1st, then Esha must be 2nd, but Chetan is 2nd: impossible. Hence Bina is 1st, and the block Divya-Esha-Ajay-Firoz fills 3, 4, 5, 6 in that order. The order is Bina, Chetan, Divya, Esha, Ajay, Firoz. Bina is not last, so clue (d) holds.

Placing the absolute clue first collapsed the possibilities to one order in a few lines. Starting with clue (d), the weakest, would have left five positions open for Bina and no progress.

**The failure point.** The method fails when the "strongest" clue is chosen by its length rather than by how many positions it fixes. A long sentence about three people who are all unplaced may fix less than a short sentence that names one exact position.

### Advanced: recheck every earlier clue after each placement

This is the Advanced refinement of the strongest-clue habit. Each placement can break a clue you have already "used". In the race above, once Bina was placed 1st, we went back and checked clue (d) again, and we checked that clue (b) still had two adjacent free places for Divya and Esha.

- **Worked example.** Five boxes stand in a vertical stack, positions 1 (top) to 5 (bottom). Clues: (i) the red box is directly above the blue box; (ii) the green box is at the bottom; (iii) the white box is above the red box; (iv) the yellow box is not on top. Clue (ii) puts green at 5. Clue (i) makes red-blue a block occupying (1,2), (2,3) or (3,4). Clue (iii) needs white above red, so red is not at 1; the block is (2,3) or (3,4). If the block is (2,3), white must be 1, and yellow takes 4: check clue (iv): yellow is not on top. Allowed. If the block is (3,4), then positions 1 and 2 hold white and yellow, and clue (iv) forces yellow to 2 and white to 1. Also allowed. Two orders survive: white, red, blue, yellow, green and white, yellow, red, blue, green.
- **What the recheck shows.** Rechecking did not give a unique answer, and that is itself information. White on top and green at the bottom are forced, because they hold in both orders. Red's position is not forced.
- **The trap here.** Stopping at the first consistent order and reporting it as the answer. When several orders survive, only facts that hold in every surviving order are certain.

### Ties, one-direction chains and missing links

- **Ties.** "Arun is as tall as Biju" places them on the same rung. A tie is not a step up. When two people tie, they share one rank number and the next rank number is skipped: if two students tie for 4th, the next student is 6th, not 5th. A person who is not part of a tie still has rank = (number of people strictly ahead) + 1, so top-plus-bottom = N + 1 still holds for that person.
- **Transitive chains.** Write "Kiran is heavier than Leela" as Kiran > Leela. Write "Leela is lighter than Mala" as Mala > Leela, rewriting every clue into the same direction. Then link chains end to end. Only a continuous chain in one direction gives an order.
- **Missing links.** Two people who are each compared with a third person, one above it and one below it, are ordered. Two people who are both compared with the same third person in the same direction are not ordered. From "Pooja > Ravi" and "Pooja > Sita", nothing follows about Ravi and Sita.
- **Worked example.** Clues: Tanvi is older than Uday. Vikram is younger than Uday. Wasim is older than Vikram. Who must be older than Vikram? Rewrite: Tanvi > Uday, Uday > Vikram, Wasim > Vikram. Tanvi and Uday are older than Vikram by the chain, and Wasim is older by direct statement. So three people must be older than Vikram. But who is older, Wasim or Tanvi? Neither chain reaches from one to the other. That order is unknown.

Mixed directions are where this goes wrong: if "lighter than" and "heavier than" clues sit on the page as written, a chain can appear to continue when it actually reverses. Rewrite every clue into one direction before linking.

### Scaled and summed comparisons: weight chains

Some comparison items attach a multiplier or a sum to one side: "half of K's weight is more than L's weight", or "X weighs more than Y and Z together". The ladder still works, but you must first decide which plain comparisons such a statement really gives.

```text
   STEP 1: rewrite every statement in the standard form   X  >  c x Y
           ("X weighs more than c times Y", c a positive number)

   "Half of K is more than L"       K/2 > L   ->  K > 2 x L     c = 2      c >= 1
   "Three times M is more than K"   3M > K    ->  M > 1/3 x K   c = 1/3    c < 1

   STEP 2: read the factor c
           c >= 1   ->  c x Y is at least Y, so X > Y          ORDER FORCED
           c <  1   ->  c x Y is below Y, X may land either side   ORDER OPEN

   SUMS:   "X weighs more than Y and Z together"  ->  X > Y  and  X > Z
           "X and Y together weigh more than Z"   ->  nothing about X against Z alone
```

The plain idea: weights are positive. Put the person who is "more" on the left and read the number that multiplies the other person. If X beats Y even after Y has been doubled, X certainly beats plain Y. If X beats only a third of Y, X may still be lighter than the whole of Y.

- **Method.** (1) Rewrite each statement in the form X > c x Y, dividing through if the multiplier was written on X. (2) Read c: a factor of 1 or more gives X > Y; a factor below 1 gives no plain order between X and Y. (3) A sum written after "more than" splits into separate orders, because every part of a sum of positive weights is smaller than the sum. (4) Link the plain orders into chains as before; along a chain the factors multiply, so X > a x Y and Y > b x Z give X > ab x Z. (5) Settle the heaviest and the lightest as two separate questions, because one end of the ladder can be forced while the other stays open.
- **Worked example: which comparisons are certain?** Four parcels K, L, M and N have positive weights. (i) K weighs more than twice L. (ii) M weighs more than half of K. (iii) N weighs more than L and M together. Of the six pairs, which orders are certain?

  Statement (i) is K > 2 x L, with c = 2, so K > L. Statement (ii) is M > 1/2 x K, with c below 1, so M against K stays open. But chain it: M > K/2 and K/2 > L (dividing (i) by 2), so M > L. Statement (iii) splits into N > L and N > M. Collect the results: K > L, M > L, N > L and N > M are certain; K against M and K against N are open.

  ```text
                N
                |           a line means "above"; read downward
        K       M
         \      |           K is above L, but no line joins K to M or to N
          \     |
            L               every parcel is above L
  ```

  Two settings show that the open pairs really are open. K = 10, L = 4, M = 6, N = 11 satisfies all three statements and puts N on top; K = 10, L = 4, M = 5.5, N = 9.6 also satisfies them and puts K on top. So the lightest parcel is certain (L) while the heaviest is not (K or N): the two ends of the ladder had to be settled separately.
- **Counter-example to keep in mind.** Removing a factor below 1 is the classic slip. From 3M > K one may not conclude M > K: K = 10 and M = 4 give 3M = 12 > 10, yet M is lighter than K. Before dropping a multiplier, rewrite the statement as X > c x Y and check that c is at least 1.

### Advanced where it extends: comparisons that carry numbers

Some ordering families attach numbers to the comparisons. The structure is still a ladder, but the steps have sizes.

- **Relative speed in a race.** "In a 100 m race, P beats Q by 10 m" means that when P covers 100 m, Q covers 90 m. Their speeds are in the ratio 100 : 90. If Q beats R by 10 m in the same kind of race, then when Q covers 100 m, R covers 90 m. To compare P with R, scale: when P covers 100, Q covers 90, and R covers 90 x 90/100 = 81. So P beats R by 19 m, not 20 m. This is the Advanced extension: the two margins multiply as ratios; they do not add.
- **Why adding fails.** Adding the margins (10 + 10 = 20) treats both margins as measured on the same 100 m base. The second margin is measured on Q's 100 m, not on Q's 90 m, so the bases differ.
- **Slowest or fastest runner.** If only some pairs are compared, find the person who loses every comparison in which they appear and is never shown faster than anyone. If two people both have no "faster than" link, the slowest is not determined.
- **Age orders across families.** When cousins or siblings are compared, the family relations do not by themselves give ages. A father is older than his child, but two cousins have no forced age order unless a clue states it. Build the age ladder only from stated comparisons and forced family facts.
- **Price bounds.** Suppose a kettle costs more than two mugs, and a mug costs more than three spoons, and a spoon costs ₹15. Then a mug costs more than ₹45, and a kettle costs more than 2 x 45 = ₹90. The chain gives a lower bound, not a price. If a question asks for the least whole-rupee price of the kettle, with mugs and spoons priced in whole rupees, the mug is at least ₹46 and the kettle is at least ₹93, because "more than 92" in whole rupees means 93 or more.
- **Where bounds go wrong.** Treating "more than" as "equal to". A strict inequality moves the bound up by the smallest unit allowed, and that unit must be stated (whole rupees, whole years).

### The middle person and tournament totals

- **Median.** In an odd-sized group of N, the median is the person at position (N + 1)/2 from either end. With 7 people, the median is 4th from the top and 4th from the bottom. You do not need the full order; you need exactly three people above and three below.
- **Worked example.** Seven plants are compared by height. You know that exactly three plants are taller than the jasmine and that the rose is taller than the jasmine. Then the jasmine is 4th, the median, even though the full order is unknown.
- **Tournament scores.** In a round-robin tournament, every team plays every other team once. With 5 teams there are 5 x 4/2 = 10 matches. If a win gives 2 points, a draw gives 1 to each side, and a loss gives 0, every match adds exactly 2 points to the table, so the total is 20 points. A claimed score table that does not add to 20 is impossible. Ordering clues ("A finished above B", "no two teams tied") then work on this fixed total.
- **Limits of both rules.** The median rule fails for an even group, where there are two middle positions. The tournament total fails when the points per match change with the result, for example when a win gives 3 points and a draw gives 1 to each side; then each match adds 3 or 2 points, and the total depends on the number of draws.

### Writing names in a line as you read: why it misleads

The tempting method is to write the names in a line as you read the clues, from left to right, sliding names into gaps as new clues arrive. It feels fast. The reply is that this method silently decides every missing link: as soon as a name is written somewhere, it looks ordered with respect to every other name, even when no clue connects them. The arithmetic version of the same mistake is to add race margins, to treat "more than" as "equal to", or to read "three times M is more than K" as if it said "M is more than K". The correct method keeps the chain as a diagram with branches, so that an unknown order stays visibly unknown, converts margins through ratios, and drops a multiplier only after rewriting the statement as X > c x Y with c at least 1.

A second tempting method is to count from the wrong end. A stem may give one rank from the top and ask for a rank from the bottom. The reply is to write both numbers on the rung, as in the ladder visual, before answering.

### UPSC application

The paper uses this family in several costumes, and the method is the same each time.

- **Age-order inference (2013 Q23), age-order conclusion (2016 Q32), age-ordering deduction (2020 Q36), statement-based age ranking (2023 Q38) and cousins' age orders (2015 Q73).** Rewrite every age statement in one direction, link chains, and report only what a continuous chain forces. In statement-based items, test each conclusion: if any consistent order makes it false, it does not follow.
- **Rank from the end (2013 Q34), ladder ordering (2014 Q8) and ranking order deduction (2019 Q76, Q77, Q78).** Use top + bottom = N + 1, place the clue that fixes the most first, and in conditional sets rebuild the ladder for each "if" before answering.
- **Median by height (2014 Q9).** Count the people above and below; do not build the whole order unless needed.
- **Couple height-ordering (2015 Q17) and vegetable taste ordering (2015 Q32).** These are chains with several branches. Draw the branches, and answer "who is tallest" or "which is least liked" only when one name sits above, or below, every branch.
- **Relative running speed (2015 Q29) and slowest runner (2015 Q60).** Convert margins to ratios on a common base; identify the slowest only when every other runner is linked above that runner.
- **Cow-goat price bounds (2015 Q77).** Treat price comparisons as inequality chains and compute the bound, respecting strict inequality and the unit.
- **Weight inequality deductions (2019 Q79, Q80).** Rewrite each scaled statement in the form X > c x Y, drop the factor only when c is at least 1, and settle the heaviest and the lightest as two separate questions.
- **Tournament-score logic (2025 Q50).** Fix the total points first, then order teams.
- **Ranking-order logic (2026 Q33).** Place the fixed ranks first, then test each conditional statement against every ladder that the remaining clues allow.

### Revision points

- Rank from the top + rank from the bottom = N + 1 for one line, for anyone who does not share a rank.
- One person's two ranks, p from one end and q from the other, give a row of p + q - 1.
- After an exchange, each person stands on the other's old rung; convert that rung with N + 1 when the total is known.
- People strictly between positions a and b from the same end: |a - b| - 1.
- When positions are given from opposite ends, draw both the separate and the crossing pictures before answering "at least" or "at most".
- Enter the clue that fixes the most positions first.
- Advanced: after each placement, recheck every earlier clue; if several orders survive, only common facts are certain.
- Rewrite all comparisons in one direction before linking; only continuous one-direction chains give an order.
- Two people compared with the same third person in the same direction are not ordered.
- Two tied people share one rank number, and the next rank number is skipped.
- Write a scaled comparison as X > c x Y: c of 1 or more forces X above Y; c below 1 leaves the order open.
- Along a chain the factors multiply: X > a x Y and Y > b x Z give X > ab x Z.
- "X is heavier than Y and Z together" gives X above each of them; the reverse sum gives nothing.
- Advanced: race margins combine as ratios, so 10 m and 10 m give 19 m, not 20 m.
- A strict "more than" in whole units raises the bound by one unit.
- The median of an odd group of N is position (N + 1)/2; count those above and below.
- In a round robin with 2 points per match, total points = 2 x number of matches.

### Practice

**MCQ 16**

Six teams play a round-robin tournament, so every team plays every other team exactly once. A win earns 2 points, a draw earns 1 point for each team, and a loss earns 0 points. When the tournament ends, no two teams have the same points total. What is the least number of points that the top team can have?

- A. 5 points, the average share of the points
- B. 7 points, after rounding the lower bound of 7.5 down to a whole number
- C. 10 points, by winning each of its five matches
- D. 8 points, as six unequal totals must add up to 30

**MCQ 16 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Shares the 30 points equally, 30 / 6 = 5. Equal shares break the condition that every total is different, and six different totals with a top of 5 can add to at most 5 + 4 + 3 + 2 + 1 + 0 = 15.
- **B — Incorrect:** Solves 6m - 15 = 30 to get 7.5 and rounds down to 7. With a top of 7, six different totals add to at most 7 + 6 + 5 + 4 + 3 + 2 = 27, which is short of 30, so a lower bound on a whole number must be rounded up.
- **C — Incorrect:** Gives the greatest possible top score, which belongs to a team that wins all five of its matches. The question asks for the least top score, which comes from spreading the points as evenly as different totals allow.
- **D — Correct:** There are 6 x 5 / 2 = 15 matches, each adding 2 points, so the table holds 30 points. If the top team has m points, the six different totals are at most m, m - 1, ..., m - 5, which add to 6m - 15. This must reach 30, so m is at least 7.5, that is, 8. Eight can occur: let A beat B, C, D and E but lose to F; B beat C, D and E and draw with F; C beat D, E and F; D beat E and F; E beat F. The totals are A 8, B 7, C 6, D 4, F 3 and E 2, all different. A full search of all 3^15 result tables confirms that no table with different totals has a top below 8.

**MCQ 17**

Three sacks, P, Q and R, each have a positive weight. P weighs more than Q and R together. Q weighs more than two and a half times R. What is the largest number k for which the statement "P weighs more than k times R" must be true?

- A. 3.5, adding R to the bound on Q
- B. 4.5, counting R twice when bounding the pair Q and R
- C. 5, reading the pair as twice the heavier Q
- D. 1, using the sum alone to set P above R

**MCQ 17 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Q and R together weigh more than 2.5R + R = 3.5R, because Q alone is more than 2.5R. P weighs more than Q and R together, so P > 3.5R in every case. No larger k is forced: R = 1, Q = 2.51 and P = 3.52 satisfy both statements, and P is only 3.52 times R, so for any k above 3.5 the weights can be chosen with P below k times R.
- **B — Incorrect:** Counts R twice: it reads the second statement as if Q were more than R plus two and a half R, that is more than 3.5R, and then adds the R in the pair, giving 4.5R. The second statement bounds Q by 2.5R only. With R = 2, Q = 5.2 and P = 7.4, both statements hold, yet P is only 3.7 times R, so k = 4.5 is not forced.
- **C — Incorrect:** Turns "more than Q and R together" into "more than twice Q", which needs R to be at least as heavy as Q, the opposite of what the second statement says. With R = 1, Q = 2.6 and P = 3.7, both statements hold, yet P is less than 5 times R.
- **D — Incorrect:** Uses only the sum, which places P above R, and ignores the factor on Q. "P weighs more than R" is true, but the factor 2.5 on Q lifts the forced bound far above 1, so k = 1 is not the largest.

---

## Lesson 8 - Seating and arrangement

Progress: Lesson 8 of 18 | Stage: Core | Subtopic: Seating and arrangement

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Where the learner gets stuck

A seating item gives you six or seven people, a row or a round table, and a paragraph of clues such as "K sits second to the right of M" or "the person opposite O is not a doctor". The difficulty is not the logic of any one clue. It is that the clues refer to positions that do not yet exist on paper. Once you draw the seats and fix one person, most clues become simple placements. This lesson shows how to choose that first person, how left and right change at a round table, and how to count seatings when the question asks "in how many ways".

### Visual: a row of seats and a round table with an anchor

```text
   LINEAR ROW (everyone faces NORTH, the reader's "up")

      left end                                    right end
        [1]     [2]     [3]     [4]     [5]     [6]
         ^                                         ^
   "3rd from left" = seat 3      "2nd from right" = seat 5
   "immediately right of 3" = seat 4

   ROUND TABLE (6 seats, everyone faces the CENTRE)

                    seat 0
                   [ K ]   <- ANCHOR: fixed first, removes rotations
          seat 5             seat 1
          [ L ]               [ M ]
                  (centre)
          seat 4             seat 2
          [ P ]               [ O ]
                    seat 3
                   [ N ]   <- directly OPPOSITE K (3 seats away)

   Seats are numbered clockwise as seen from above.
   Facing the centre:  your RIGHT neighbour is the next seat ANTICLOCKWISE,
                       your LEFT neighbour is the next seat CLOCKWISE.
```

Look at the row first. Seats are numbered from the left end, so a clue such as "third from the left" names a seat at once, and "second from the right" in a row of 6 is seat 6 + 1 - 2 = 5. That is the same top-plus-bottom rule you met with rankings.

Now look at the circle. K has been written in seat 0 before any clue was used. That is the **anchor**: in a circle, turning everyone one seat round gives the same seating, so we fix one person to stop counting the same seating six times. Notice the direction note. When you sit at a round table facing the middle, your right hand points to the seat that lies anticlockwise from you as seen from above. Draw this once and keep it beside every circular item, because most circular errors are left-right errors.

### Why the most-constrained guest goes first

Imagine arranging guests at a wedding dinner. You would not start with the guest who "does not mind where he sits". You would start with the bride's grandmother, who must sit at the head of the table, then her husband, who must sit beside her. Each fixed guest removes choices for everyone else. Seating puzzles reward the same instinct: place the person with the fewest possible seats first.

A round table has no head unless you create one. Choosing an anchor creates it.

### Method 1: build the frame before the people

1. Decide the shape: a straight row, two facing rows, a round table, a square table, floors of a building, or desks in an office.
2. Decide the facing direction. In a row facing north, the person's right is your right. In a row facing south, the person's right is your left. At a round table facing the centre, right is anticlockwise.
3. Number the seats.

- **Worked example.** Two rows of three face each other: seats 1, 2, 3 in the north row face south; seats 4, 5, 6 in the south row face north, with seat 4 opposite seat 1. A person in seat 2 of the north row has seat 1 on their right, because they face south, and on the page seat 1 is to the left.
- **What goes wrong.** One facing direction gets used for both rows. Mark an arrow on each row before reading any clue that uses left or right.

### Method 2: strongest constraint first, then recheck

This is the same discipline you learnt with ladders, now applied to seats. The strongest clue fixes a seat absolutely ("sits at the extreme left", "sits in the middle"). The next strongest links an unplaced person to a placed one ("immediately right of R"). The weakest clues are negative ("is not at an end", "is not adjacent to Q") and are best used to eliminate the last few options.

- **Worked example (Advanced: multi-constraint seating).** Five people P, Q, R, S, T sit in seats 1 to 5 from left to right. R is in the middle, seat 3. P is at the extreme left, seat 1. Q is immediately right of P, so Q is in seat 2. T is not at an extreme end, so T cannot take seat 5 and must take seat 4. S takes seat 5. The unique order is P, Q, R, T, S.
- **What it establishes.** Three absolute or anchored clues placed three people. The negative clue was used last, when only two seats remained, and it decided both of them.
- **Where it stops.** When the clues do not force one seating, more than one arrangement survives. Then the only safe answers are facts that are true in every surviving arrangement.

Skipping the recheck after each placement is where this method breaks: a late placement can sit someone next to a person they were told not to sit beside.

### Method 3: the round table with one anchor

- **Rule.** Fix the most-constrained person as the anchor, then place everyone else by their distance from the anchor. "Opposite" in a table of 6 means 3 seats away; in a table of 8 it means 4 seats away. "Second to the right" means two seats in the right-hand direction.
- **Worked example.** Six friends K, L, M, N, O and P sit round a table facing the centre. N sits opposite K. L sits immediately to the right of K. O sits immediately to the right of N. M is not adjacent to N.

  Anchor K in seat 0. N is opposite: seat 3. Right is anticlockwise, so L, immediately right of K, takes seat 5, and O, immediately right of N, takes seat 2. Seats 1 and 4 remain for M and P. Seat 4 is next to N, and M may not sit next to N, so M takes seat 1 and P takes seat 4. This is the seating drawn in the visual.
- **What the anchor achieved.** One anchor and one "opposite" clue fixed two people; two "immediately right" clues fixed two more; the negative clue decided the last pair.
- **Counter-check.** Swap right and left and the whole seating changes. Had L been put in seat 1, M would have been forced into a different seat, and every later answer would change. Recheck by sitting yourself in K's seat and pointing with your right hand.

### Method 4: counting circular seatings, with no halving by default

When the question asks "in how many ways", you are counting, not deducing.

- **Factorial.** The number of ways to line up n different people is n x (n - 1) x ... x 2 x 1, written n! and read "n factorial". So 4! = 24 and 5! = 120.
- **Rule.** n different people round a table, where turning the whole table gives the same seating, can be seated in (n - 1)! ways. Fix one person as the anchor; the other n - 1 fill the remaining seats in a line.
- **Worked example.** Five friends round a table: fix one, and arrange the other four in 4! = 24 ways. Six people round a table: fix one, and arrange the other five in 5! = 120 ways.
- **No halving unless told.** A seating and its mirror image (everyone's left and right neighbours swapped) are different seatings, because each person has a different person on their right. Divide by 2 only when the stem says that clockwise and anticlockwise orders are the same, which happens for beads on a necklace or keys on a ring that can be flipped over.
- **When the rule does not apply.** Labelled seats break it, for example chairs with numbers or a table with one chair marked "chair". Then turning the table changes the seating, and the count is n!, not (n - 1)!.

### Method 5: restrictions at a round table

- **Opposite and not adjacent (Advanced).** Six people sit round a circle. A is opposite B, and C is not adjacent to A. Fix A to remove rotations. B's seat is fixed opposite A. Of the four seats left, two are A's neighbours, so C has 2 permitted seats. The last three people fill three seats in 3! = 6 ways. Total 2 x 6 = 12.
- **Two people not together.** For 6 people with X and Y not side by side: total seatings 5! = 120. Seatings with X and Y together: glue them into one block, giving 5 units round a table, (5 - 1)! = 24, times 2 for the order inside the block, so 48. Not together: 120 - 48 = 72.
- **The usual slip.** Forgetting the block's internal order. X then Y and Y then X are different seatings, so the block count is doubled.

### Method 6: keeping people apart in a row (the gap method)

- **Rule.** To arrange people so that no two of one group sit together, first seat the other group, then place the restricted group in the gaps between and around them.
- **Worked example.** Four guests take seats in a row of 9 chairs, and no two guests may sit side by side. Think of the 5 chairs that stay empty as the "other group". Five empty chairs in a line create 6 gaps: before the first, between each pair, and after the last. Each guest needs a gap of his or her own. Taking the guests in a fixed order, the first has 6 gaps to choose from, the second 5, the third 4 and the fourth 3, so 6 x 5 x 4 x 3 = 360 seatings. A direct listing of all ways to seat four people in nine chairs with no two adjacent gives the same 360.
- **At a round table.** Five men sit round a table first: fix one man and arrange the other four in 4! = 24 ways. Five men in a circle leave 5 gaps between them, not 6, because there is no "end". Two women then take two different gaps in order: 5 x 4 = 20. Total 24 x 20 = 480. Check by complement: seven people round a table give 6! = 720 seatings; the two women side by side give 5! x 2 = 240; and 720 - 240 = 480.
- **Where it breaks.** Counting the gaps at a circle as you would in a row. A row of k people has k + 1 gaps; a circle of k people has k gaps.

### Method 7: row-position counts

- **Rule.** These are ranking questions dressed as seating. Use rank from the left + rank from the right = N + 1, and people strictly between positions a and b = |a - b| - 1.
- **Worked example.** A row has 30 people. Hema is 9th from the left and Irfan is 8th from the right. Convert Irfan to the left end: 30 + 1 - 8 = 23rd from the left. Between them sit 23 - 9 - 1 = 13 people. Now shorten the row to 15 people with the same two ranks. Irfan is 15 + 1 - 8 = 8th from the left, which puts him to the left of Hema, in the very next seat, and nobody sits between them.
- **A quick test for crossing.** With a row of N, a person a-th from the left and another b-th from the right: if a + b is at most N, they have not crossed and N - a - b people sit between them (30 - 9 - 8 = 13). If a + b is more than N, they have crossed, and a + b - N - 2 people sit between them (9 + 8 - 15 - 2 = 0).
- **Warning sign.** Skipping the crossing test. Using N - a - b for the row of 15 gives 15 - 17 = -2, a negative number of people, which is the signal that the two have changed sides.

### Method 8: checking statements against the finished seating

Some sets give one seating paragraph and then ask several questions: who sits next to D, which statement is true, which pair sits opposite. Once the seating is finished, these become look-up questions. When the seating is not unique, each statement must be checked against every surviving arrangement.

- **Worked example.** Suppose the clues about five people in a row leave two seatings: A, B, C, D, E and A, C, B, D, E. "D is fourth from the left" is true in both, so it must be true. "B is second from the left" is true in only one, so it is not certain. "C is next to B" is true in both, so it must be true.

A statement tested against only the first seating you found has not been checked at all; the other seating may falsify it.

### Method 9: offices, floors and groups

Some seating sets use floors of a building, cabins along a corridor, or groups at different tables. The frame changes, the method does not.

- **Floors.** Number floors from the ground upward. "Two floors above" is +2. "Between X and Y" means strictly between in floor number.
- **Groups.** When people are split among tables, first decide who sits at which table, using the clues about grouping; then seat each table separately. A clue about two people "at the same table" is a grouping clue before it is a seating clue.
- **Order matters.** A seating clue applied before the grouping is settled can mislead, because the clue may refer to people at different tables.

### Starting from the first sentence: the trap and the fix

The tempting method is to start writing names at seat 1 of a circle in the order in which the clues mention them. It feels natural to begin with the first sentence. The reply is that the first sentence is often weak, and a circle has no seat 1 until you anchor someone. Starting with a weak clue leaves several seats open for each person, and you end up holding many half-seatings in your head. Anchor the person named in the most clues, especially in an "opposite" or "immediately next to" clue.

The counting version of the same error is to divide by 2 out of habit. The reply is that a seating and its mirror are different for people, because each person's right-hand neighbour changes. Halve only when the stem says mirror images are the same.

### UPSC application

- **Round-table necessities (2013 Q19), circular seating puzzles (2016 Q12, 2022 Q40) and circular-seating arrangement (2026 Q14).** Anchor, place opposites, then use right and left with the facing direction. For "which must be true", test every surviving seating.
- **Adjacent seat questions (2014 Q11).** Finish every seating the clues allow, then read off the neighbours in each.
- **Row-position counts (2014 Q67) and linear row position counts (2020 Q35).** Use the ranking rules, convert every rank to one end, and run the crossing test before counting.
- **Non-adjacent arrangements (2017 Q57).** Use the gap method, counting k + 1 gaps in a row and k gaps at a circle.
- **Row arrangement puzzles (2017 Q59), office seating deductions (2018 Q25, Q26) and placement logic deductions (2018 Q43, Q44, Q45).** Build the frame, place the strongest constraint, recheck after each placement.
- **Placement statement checks (2018 Q46, Q47, Q48).** After the arrangement is fixed, check each statement against every surviving arrangement.
- **Group-seating constraints (2026 Q35).** Settle the grouping first, then the seats.

### Revision points

- Draw the frame and mark the facing direction before reading any left-right clue.
- In a row facing north, the person's right is your right; facing south, it is your left.
- At a round table facing the centre, a person's right is the next seat anticlockwise.
- Fix the most-constrained person as the anchor; in a circle this also removes rotations.
- Use absolute clues first, linked clues next, negative clues last; recheck all clues after each placement.
- If several seatings survive, only facts true in all of them are certain.
- n different people round a table: (n - 1)! seatings when rotations are the same.
- Do not halve for mirror images unless the stem says they are the same.
- Labelled seats remove the rotation symmetry, so the count becomes n!.
- "Not together" = total - together; a glued block has 2 internal orders.
- Gap method: a row of k has k + 1 gaps; a circle of k has k gaps.
- Row-position counts follow left + right = N + 1; from opposite ends, between = N - a - b unless a + b exceeds N.
- In multi-table sets, settle the grouping before seating anyone.

### Practice

**MCQ 18**

Six people, P, Q, R, S, T and U, sit in a row of six seats numbered 1 to 6 from the left end, all facing north. S sits in seat 3. T sits immediately to the right of S. P sits at one of the two ends. Q does not sit next to T. R sits somewhere to the left of S. U does not sit at either end. Which one of the following must be true?

- A. P occupies seat 1, at the left end
- B. U occupies seat 5, between T and the right-end seat
- C. R occupies seat 2, directly beside S
- D. Q occupies seat 1 or seat 6

**MCQ 18 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Reads "one of the two ends" as the left end. The seating Q, R, S, T, U, P satisfies every clue and puts P in seat 6, so P's seat is not fixed.
- **B — Correct:** S is in seat 3 and T in seat 4, leaving seats 1, 2, 5 and 6. U is not at an end, so U takes seat 2 or seat 5. Suppose U took seat 2. R must be left of S, so R would take seat 1; P must be at an end, so P would take seat 6; that leaves seat 5 for Q, next to T, which the clues forbid. So U takes seat 5. Testing the rest gives exactly three seatings: P, R, S, T, U, Q; Q, R, S, T, U, P; and R, Q, S, T, U, P. U is in seat 5 in all three.
- **C — Incorrect:** Holds in the first two seatings found, which is why it is tempting, but the third seating, R, Q, S, T, U, P, puts R in seat 1 and Q in seat 2. A statement must hold in every surviving seating.
- **D — Incorrect:** Notices that Q is at an end in two seatings and stops checking. In R, Q, S, T, U, P, Q sits in seat 2, which is not next to T, so that seating is allowed and Q is not at an end.

**MCQ 19**

Eight people, including Anil, Bhavna and Chirag, sit around a round table. Two seatings are the same if one is a rotation of the other, and a seating and its mirror image are counted as different. In how many seatings do Anil, Bhavna and Chirag occupy three neighbouring seats, in any order among themselves?

- A. 120, with the block's inner order ignored
- B. 360, with mirror images treated as identical
- C. 720, with one unit fixed and the three reordered inside the block
- D. 4320, with the six units lined up as in a row

**MCQ 19 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Glues the three into one block and arranges the six units round the table, (6 - 1)! = 120, but forgets that the three can stand in different orders inside the block.
- **B — Incorrect:** Halves the full count, 720 / 2 = 360, as if a seating and its mirror were the same. The stem says mirror images are different, so no halving is allowed.
- **C — Correct:** Treat Anil, Bhavna and Chirag as one block. The block and the other five people make six units, which sit round the table in (6 - 1)! = 120 ways. Inside the block the three can be ordered in 3! = 6 ways. Total 120 x 6 = 720. Check by listing: put one particular person who is not Anil, Bhavna or Chirag in a fixed seat to remove rotations; the other seven people then fill the remaining seven seats in 7! = 5040 orders, and exactly 720 of those orders put the three in neighbouring seats.
- **D — Incorrect:** Arranges the six units as if they stood in a row, 6! = 720, then multiplies by 6 for the block, giving 4320. A round table has no first seat, so one unit must be fixed before arranging the rest.

**MCQ 20**

Six people sit at a round table whose six chairs are numbered 1 to 6 in order round the table, so two seatings that differ by a rotation are different seatings. Pranav must sit in an even-numbered chair, and Qadir must sit in the chair directly opposite Pranav. How many seatings are possible?

- A. 144, with Pranav free to take every chair
- B. 24, anchoring Pranav to undo rotation
- C. 360, with Qadir seated freely once Pranav is placed
- D. 72, three choices for Pranav, others 4!

**MCQ 20 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Lets Pranav take all 6 chairs, 6 x 4! = 144. Only chairs 2, 4 and 6 are even, so Pranav has 3 choices, not 6.
- **B — Incorrect:** Anchors Pranav as if the chairs were unlabelled, then fixes Qadir and arranges the other four, 4! = 24. Numbered chairs make a rotation a different seating, so Pranav's choice of chair must be counted.
- **C — Incorrect:** Gives Pranav his 3 even chairs but then lets the other five people, Qadir included, fill the remaining chairs freely, 3 x 5! = 360. The opposite clue fixes Qadir's chair once Pranav is seated.
- **D — Correct:** Pranav takes chair 2, 4 or 6: 3 ways. Qadir's chair, three places round, is then fixed. The other four people fill the four remaining chairs in 4! = 24 ways. Total 3 x 24 = 72. A direct listing of all 720 seatings in numbered chairs gives the same 72.

---

## Lesson 9 - Logic grids and matching structures

Progress: Lesson 9 of 18 | Stage: Core | Subtopic: Logic grids and matching structures

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Why these items feel slippery

Four colleagues, four days off, four hobbies, and six clues. Each clue sounds simple: "Kunal neither sings nor cycles", "the singer is off on Monday". Yet after the third clue you are juggling a dozen possibilities. Seating gave you a picture of seats. Here there are no seats; there are pairings between lists. The picture you need is a grid in which every possible pairing has one cell, and every clue either ticks a cell or crosses it out.

### Visual: the elimination grid and the matching table

```text
   ELIMINATION GRID  (one row per person; one block of columns per attribute)

                 |  DAY OFF               |  HOBBY
                 |  Mon  Tue  Wed  Thu    |  chess  cycle  paint  sing
   --------------+------------------------+----------------------------
   Jaya          |   X    ✓    X    X     |    X      X      ✓     X
   Kunal         |   X    X    ✓    X     |    ✓      X      X     X
   Leena         |   X    X    X    ✓     |    X      ✓      X     X
   Manav         |   ✓    X    X    X     |    X      X      X     ✓
   --------------+------------------------+----------------------------
   LINK BLOCK  (day x hobby):  sing <-> Mon     cycle <-> Thu

   MATCHING TABLE  (the finished answer, read across)

   | Person | Day off | Hobby    |
   |--------|---------|----------|
   | Jaya   | Tue     | painting |
   | Kunal  | Wed     | chess    |
   | Leena  | Thu     | cycling  |
   | Manav  | Mon     | singing  |
```

Read the grid row by row. A tick (✓) means "this pairing is true". A cross (X) means "this pairing is impossible". Because the matching is **one-to-one** (each person has exactly one day, and each day belongs to exactly one person), every row of a block has exactly one tick, and so does every column. That single fact does most of the work: one tick in a row lets you cross out the rest of that row and that column.

Notice the link block underneath. Some clues connect two attributes without naming a person: "the singer is off on Monday". You note such a clue as a link between columns, and you transfer it to a person only when one side of the link is placed.

The matching table is the finished answer. You build the grid; you read the table.

### Sudoku with names

A logic grid is a game of Sudoku with names. In Sudoku, each row and column holds each digit once; when a cell is forced, it removes that digit from its row and column. In a matching puzzle, each person holds each attribute once, and a forced pairing removes that attribute from everyone else. You win by crossing out, not by guessing.

### Entering clues: definite pairs, then negatives, then links

- **Order of entry.** List the people as rows. Give each attribute (day, hobby, city) its own block of columns. Enter definite pairings first ("Jaya's day off is Tuesday"), then negative clues ("Kunal does not sing"), then links ("the cyclist is off on Thursday").
- **Worked example.** Clues: (1) Jaya is off on Tuesday. (2) The singer is off on Monday. (3) Kunal neither sings nor cycles. (4) Leena's day off is later in the week than Manav's. (5) The cyclist is off on Thursday. (6) Jaya does not play chess.

  Clue (1) ticks Jaya-Tuesday and crosses the rest of that row and column. Clue (3) crosses Kunal-singing and Kunal-cycling. Now combine with the links: the singer is off on Monday and the cyclist on Thursday, and Kunal is neither, so Kunal is not off on Monday or Thursday. Tuesday is Jaya's. Kunal is off on Wednesday. Monday and Thursday remain for Leena and Manav, and clue (4) puts Manav on Monday and Leena on Thursday. The links now transfer: Manav sings, Leena cycles. Chess and painting remain for Jaya and Kunal, and clue (6) gives Jaya painting and Kunal chess.
- **What made it work.** The decisive move was not any single clue; it was crossing a negative clue (3) with two links (2) and (5) to remove two days from Kunal's row.
- **Where it breaks.** A link clue applied to a person before either side of it is placed. "The singer is off on Monday" does not say who sings. Keep it in the link block until a person is attached.

### Reading down the columns

- **The move.** When a row has only one empty cell left in a block, that cell is a tick. When a column has only one empty cell left in a block, that cell is a tick. Look down the columns as often as you look across the rows.
- **See it.** In a three-person grid for cities Agra, Bhopal and Cuttack, suppose Agra is crossed for Farhan and Gauri. Look down the Agra column: only Harsh is left, so Harsh lives in Agra, even though no clue mentions Harsh at all.
- **Limit of the method.** The method fails when you read only across rows. Column elimination finds the person who is never mentioned, and that person is often the answer.

### The final reread

- **The habit.** After the last tick, read each clue again and confirm it against the matching table.
- **Why it matters.** A slip in an early cross (for example, crossing Kunal-chess instead of Kunal-cycling) produces a complete, tidy grid that is wrong. Only a final reread catches it.
- **How the check fails.** The check fails if you reread only the clues you used last. Reread from the first clue.

### Exactly-one statements and wrong labels

Some matching items add a twist: a number of statements of which exactly one is true, or labels that are all wrong.

- **Exactly-one constraint.** If "exactly one of these three statements is true", test each statement as the true one, with the other two false, and keep only the cases that produce a consistent matching. This is the assume-and-contradict move from the truth-teller lesson, applied to a grid.
- **Worked example.** Three boxes hold a pen, a pencil and an eraser, one each. Statements: (i) the pen is in box 1; (ii) the pencil is not in box 1; (iii) the eraser is not in box 3. Exactly one is true. Try (i) true: then (ii) is false, so the pencil is in box 1, but the pen is in box 1: contradiction. Try (ii) true: then (i) is false (pen not in box 1) and (iii) is false (eraser in box 3). Box 1 holds neither pen nor pencil, nor the eraser, which is in box 3: contradiction. Try (iii) true: then (i) false and (ii) false, so the pencil is in box 1, the eraser is not in box 3, so the eraser is in box 2, and the pen is in box 3. Consistent. The only matching is pencil 1, eraser 2, pen 3.
- **All labels wrong.** Three cartons are labelled "pens", "pencils" and "pens and pencils", and every label is wrong. Draw one item from the carton labelled "pens and pencils". It cannot hold both, so the item you draw names its true contents. Suppose it is a pen: that carton holds pens. The carton labelled "pencils" cannot hold pencils, and pens are taken, so it holds the mixture; the carton labelled "pens" holds pencils.
- **Trap.** Stopping at the first case that "works" without testing the rest. If two cases survive, the matching is not unique, and only common facts are certain.

### What other people can see

Some deduction items involve people who see each other's caps or cards and say "I do not know". Each "I do not know" is a clue: it rules out every situation in which that person would have known.

- **Worked example.** Three people stand in a line facing forward. Caps come from a set of 2 red and 3 blue. The person at the back sees the two in front; the middle person sees only the front person; the front person sees no one. The back person says "I do not know my colour". If the back person had seen two red caps, they would have known their own was blue, because only 2 reds exist. So the two in front are not both red. The middle person then says "I do not know". If the middle person had seen a red cap on the front person, they would have known their own was blue, because the two in front are not both red. So the front cap is blue, and the front person can say so.
- **What to avoid.** Treating "I do not know" as no information. Each such statement removes the cases in which the speaker could have known.

### Rotations by remainder, and free days

- **Rotation.** If a duty rotates among four towns in a fixed order, the town in any later year is found by counting the years modulo 4, that is, by the remainder on division by 4. If the order is Ajmer, Bidar, Churu, Dhar starting with Ajmer in year 1, then year 11 leaves remainder 3, so the town is Churu.
- **Free days.** To find a day on which several people are all free, make a grid of people against days, cross out each person's busy days, and look for a column with no cross.
- **Off-by-one check.** The rotation goes wrong if the starting year is counted as remainder 0 instead of remainder 1. Check with a small year you can count by hand.

### Choosing teams under conditions

Some matching items choose a team, or fill posts, under conditions. Turn every condition into an arrow, as in the conditional-logic lesson, and list the cases by the member that the conditions mention most.

- **Worked example.** A three-person audit team is chosen from F, G, H, I and J. If G is chosen, H must also be chosen. I and J are not both chosen. Split on G. Case G in: H must come too, and the third member is F, I or J, giving FGH, GHI and GHJ, all of which keep I and J apart: 3 teams. Case G out: the team is three of F, H, I and J, which gives FHI, FHJ, FIJ and HIJ; the last two put I and J together, so 2 teams survive. Total 5 teams: FGH, GHI, GHJ, FHI and FHJ.
- **Easy to miss.** A condition applied in only one case. "I and J are not both chosen" applies in the G-out case as well, which is where it removes two teams.

### Pushing one count to its maximum

- **The principle.** To make one person's count as large as possible, make everyone else's as small as the rules allow.
- **Example.** Five clerks share seven files. Each file is handled by exactly one clerk, and each clerk handles at least one file. The most files one clerk can handle is 7 - 4 x 1 = 3, because the other four must each keep at least one.
- **Watch for.** The method fails when a hidden minimum is missed, such as "each clerk handles at least two files". Then the maximum for one person becomes 7 - 4 x 2, which is negative, so the stated numbers cannot all hold, and you must recheck the reading.

### Yes-no feature tables

Some items list people or objects with several yes-no features and ask which group satisfies a combination ("married women who are teachers"). Build a table with one row per person and one column per feature, mark yes or no, and read the combination down the columns.

- **Worked example.** Four women: Ruby is married and a teacher; Sana is unmarried and a teacher; Tara is married and not a teacher; Usha is unmarried and not a teacher. "Married, not a teacher" picks Tara alone. "Teacher" picks Ruby and Sana.
- **Classification by a stated definition.** When an item defines a category by its features and asks which example belongs to it, check each example against every defining feature. An example that has most of the features but lacks one does not belong.

One feature used as a stand-in for the whole definition is the error to watch for here. Check each defining feature separately.

### Matching two lists through printed codes

Some items print List I and List II and ask you to pick the correct code. The subject matter varies, from relationships and tools to barriers and examples; this section teaches only the matching mechanics, which are the same whatever the content.

- **Structure.** List I names items; List II names categories or functions. The task is a one-to-one matching, exactly like the grid above. Write the four items as rows and the four categories as columns, tick each pairing you are sure of, and cross the rest of its row and column. Often two sure pairings fix the code among the printed options.
- **Worked example.** List I: A. compass, B. stopwatch, C. ruler, D. balance. List II: 1. mass, 2. direction, 3. time, 4. length. Printed codes: (a) A-2, B-3, C-1, D-4; (b) A-2, B-3, C-4, D-1; (c) A-3, B-2, C-4, D-1; (d) A-2, B-4, C-3, D-1. The sure pairing A-2 removes code (c). The sure pairing D-1 removes code (a). Between (b) and (d), B-3 decides: the code is (b). Two sure pairings and one tie-breaker settled it without judging every pair.
- **Questionnaire-design structure.** A questionnaire item is judged by a checklist of features. Treat each feature as a column and each question as a row, and mark which features each question violates. The structural trap is a question that violates two features at once; it still gets one tick per feature column.
- **Advanced: the classification drill structure.** In the Advanced drill of this kind, each short description must receive exactly one label from a fixed set. The structural method is the same as a definition check: find the single defining feature that separates one label from its nearest neighbour, and test each description against it. If a description seems to fit two labels, the grid shows which label is already taken by a clearer description.
- **The familiar-word trap.** A pairing ticked on the basis of a familiar word rather than the function described. Match by what the item does, not by what it is called.

### Guess-and-erase: the trap and the reply

The tempting method is to write a guess for the first person, follow the clues forward, and erase when something breaks. It works on small puzzles. The reply is that guessing hides which clues were used and which were not, and when two guesses both seem to work you cannot tell which facts are forced. The grid keeps every cross with the clue that caused it, so you know exactly what is certain and what is still open.

A second tempting method is to stop as soon as the question's person is placed. The reply is that an early placement may rest on a slip; finishing the grid and rereading every clue is the only check.

### UPSC application

- **People and cities (2013 Q29), profession of B and of D (2014 Q78, Q80), surname of C, colour of the tie and sweater wearer (2016 Q54, Q55, Q56), dancer and violinist (2014 Q60), lecturer-subject grids (2017 Q69), the economics lecturer's city (2017 Q70) and the Hyderabad lecturer (2017 Q71).** These are one-to-one grids with several attribute blocks. Enter definite pairs, then negatives, then links; eliminate by rows and columns.
- **Profession puzzles about a doctor, an artist, a spouse and a lawyer (2016 Q15, Q16, Q17, Q18).** Add a block for relationships (married to whom) and use it as a link block.
- **Golf-ball box, box-colour statement and football-box colour (2016 Q34, Q35, Q36).** Build one grid for boxes against colours and another for boxes against games, and link them through the stated pairings.
- **Cap-colour deduction (2013 Q30).** Turn each statement about what a person can or cannot see into eliminated cases.
- **Likely poet this year (2014 Q59) and test scheduling (2017 Q13).** Use rotation by remainder and a day grid.
- **George free day (2014 Q66).** Use a subjects-by-days grid and find the clear column.
- **Principal and vice-principals (2015 Q48), subject combinations (2015 Q49), and language and driving puzzles (2015 Q75).** Use arrows for conditions and list cases by the most restricted post or member.
- **Maximum subjects taught (2017 Q72).** Read each person's count from a membership table; when a maximum is constrained, minimise everyone else's count.
- **Primary-group inference (2013 Q9), women-category logic grid (2017 Q29) and multi-attribute classification (2021 Q25).** Use a yes-no feature table and check every defining feature.
- **Segment matching (2026 Q34), relationship-type matching (2026 Q72), tool-purpose matching (2026 Q73) and barrier-example matching (2026 Q75).** Treat each as a one-to-one grid, fix the sure pairings first, and let the printed codes eliminate the rest.

### Revision points

- A one-to-one matching has exactly one tick in every row and every column of each block.
- Enter definite pairs first, then negative clues, then links between attributes.
- Keep a link clue ("the singer is off on Monday") in a link block until one side is placed.
- Eliminate down columns as well as across rows; the unmentioned person is often found by a column.
- Reread every clue against the finished table, from the first clue.
- Exactly-one items: test each statement as the true one and keep only consistent cases.
- All labels wrong: draw from the "mixed" label, since it cannot hold the mixture.
- Each "I do not know" removes every case in which the speaker would have known.
- Rotations are found by remainder; check the starting year with a small case.
- Selection conditions become arrows; list cases by the most restricted post.
- To maximise one count, minimise all the others within the rules.
- A yes-no feature table answers multi-attribute classification; check every defining feature.
- List matching uses the same grid: two sure pairings often remove all but one printed code.

### Practice

**MCQ 21**

Four trainees, K, L, M and N, each give one presentation, on four different days from Monday to Thursday. Exactly one of the following four statements is false.

1. K does not present on Monday.
2. N presents on the day after K.
3. L presents on Thursday.
4. N presents on the day after L.

Which one of the following must be true?

- A. M presents first, and N presents on the day before L
- B. K presents first, and N presents immediately after K
- C. L presents third, and N presents the day after L
- D. N presents first, and M presents the day before L

**MCQ 21 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Statements 2 and 4 both put N on the day after someone, so together they would put K and L on the same day; they cannot both be true, and the false statement is one of them. If statement 2 were false, statements 3 and 4 would put N on the day after Thursday, which does not exist. So statement 4 is false and statements 1, 2 and 3 are true. L presents on Thursday; K and N take consecutive days among Monday to Wednesday, and K is not on Monday, so K is on Tuesday and N on Wednesday; M takes Monday. M is first, and N's Wednesday is the day before L's Thursday. Listing all 24 schedules confirms that this is the only one with exactly one false statement.
- **B — Incorrect:** Picks statement 1 as the false one and builds K on Monday, N on Tuesday, M on Wednesday and L on Thursday. That schedule also breaks statement 4, because N is not the day after L, so two statements are false.
- **C — Incorrect:** Keeps statements 1 and 4 and moves L to Wednesday so that N can follow on Thursday, with M on Monday and K on Tuesday. That schedule breaks statement 3 and statement 2 together, so two statements are false.
- **D — Incorrect:** Treats both clashing statements, 2 and 4, as false and keeps only 1 and 3, giving N on Monday, K on Tuesday, M on Wednesday and L on Thursday. The stem allows exactly one false statement, and the clash only shows that one of the pair is false.

**MCQ 22**

Four friends, W, X, Y and Z, each take a different drink: black coffee, green tea, juice or milk. W takes neither green tea nor black coffee. X takes juice or milk. Y does not take black coffee. Z takes neither green tea nor juice. Which of the following can be stated with certainty?

- A. Z takes black coffee, so X must take the milk
- B. Z takes black coffee, so Y takes green tea
- C. W takes the milk
- D. Y takes green tea, so Z must then take the milk

**MCQ 22 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** The first part is forced, but X taking milk is not. W and X share juice and milk, and both ways of sharing them (W juice with X milk, or W milk with X juice) satisfy every clue, so this option treats an open pair as fixed.
- **B — Correct:** Look down the black coffee column: W, X and Y are all excluded, so Z takes black coffee. Look down the green tea column: W is excluded, X takes only juice or milk, and Z is now placed, so Y takes green tea. Juice and milk go to W and X in either order, so only these two pairings are certain. Listing all 24 matchings leaves exactly two, and both contain these pairings.
- **C — Incorrect:** Reads W's row alone: with green tea and black coffee excluded, W is left with juice or milk, and this option settles on milk. Exactly two matchings satisfy every clue, and W takes milk in only one of them (W milk, X juice); in the other, W takes juice and X takes milk. A claim that fails in one valid matching cannot be stated with certainty.
- **D — Incorrect:** The first part is certain, but the second reads Z's row alone, where milk and black coffee both look open. Down the black coffee column W, X and Y are all excluded, so Z must take black coffee and cannot take milk.

---

## Lesson 10 - Counting arrangements: permutations, restrictions and codes

Progress: Lesson 10 of 18 | Stage: Core | Subtopic: Counting arrangements: permutations, restrictions and codes

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### The question behind every item here

"How many three-digit numbers can be made from 0, 1, 2, 3 and 4 without repeating a digit?" Most learners can multiply. What goes wrong is the order of multiplying: they fill the slots left to right, give the first slot five choices, and count numbers that start with zero. This lesson teaches one habit that prevents nearly every error in arrangement counting: draw the slots, and fill the most restricted slot first.

### Visual: the slot diagram

```text
   QUESTION: three-digit numbers from {0,1,2,3,4}, no digit repeated

   WRONG ORDER (fill left to right, forget the restriction)
       [ 5 ]  x  [ 4 ]  x  [ 3 ]   =  60     <- includes 012, 034, ... (not 3-digit)

   RIGHT ORDER (restricted slot first)
     step 1: hundreds slot  -> cannot be 0          -> 4 choices
     step 2: tens slot      -> any unused digit,
                               zero now allowed     -> 4 choices
     step 3: units slot     -> any unused digit     -> 3 choices

       [ 4 ]  x  [ 4 ]  x  [ 3 ]   =  48

   CHECK BY COMPLEMENT:  all orderings 60  -  those starting with 0 (4 x 3 = 12)  =  48
```

Read the diagram as a story in three steps. Each box is a **slot**, one position to be filled. The number in a box is how many choices remain for that slot at the moment you fill it. The total is the product of the boxes, because every choice for one slot can be combined with every choice for the next. That rule is the **multiplication principle**.

The top row fills the slots left to right and ignores the rule that a three-digit number cannot begin with 0. It counts 60, which includes strings like 012. The second row fills the restricted slot first. The hundreds slot has 4 legal digits. The tens slot then has 4 digits left, because zero is now allowed there and one non-zero digit has been used. The units slot has 3. The answer is 48. The bottom line checks it a second way: count everything, then subtract the bad cases.

### Pack the awkward item first

When you pack a suitcase, you put the awkward large item in first and fit the small things around it. If you pack the socks first, the large item may not fit at all. Counting works the same way. The slot with a rule (no zero, must be a vowel, must be even) is the awkward item. Fill it first, while all its legal choices are still available, and the free slots will take whatever is left.

### Step 0: does order matter?

Before any formula, ask: if I swap two chosen things, do I get a different result? A three-digit number 312 is different from 213, so order matters: this is an **arrangement**, also called a **permutation**. A team of three people is the same team in any order, so order does not matter: that is a **selection**, which needs a different count from the one built here.

- **Where the decision slips.** Trouble starts when the stem uses a word like "group" for something that is really ordered (a group of people standing in a queue) or a word like "code" for something unordered (a set of three switches turned on). Decide from the meaning, not the word.

### Arranging r of n different things

- **The count.** The number of ways to arrange r things chosen from n different things, with no repetition, is P(n, r) = n x (n - 1) x ... (r factors) = n! / (n - r)!. Here n! ("n factorial") means n x (n - 1) x ... x 1, and 0! is taken as 1.
- **Worked example.** How many three-digit numbers with distinct digits can be formed from 1, 2, 3 and 4? There is no zero, so no slot is restricted: P(4, 3) = 4 x 3 x 2 = 24.
- **Second example.** Three-letter codes from five different letters, no letter repeated: P(5, 3) = 5 x 4 x 3 = 60.
- **Scope.** It counts orderings when every slot has the same pool and nothing repeats. It stops when there is a restricted slot, repeated items, or repetition allowed.
- **Limits.** The formula requires r to be no more than n, and it does not apply when repetition is allowed: three-letter codes from five letters with repetition allowed number 5 x 5 x 5 = 125, not 60.

### The leading-zero rule

- **The rule.** For an r-digit number built from a digit set that contains zero, fill the first place from the non-zero digits, then fill the remaining places under the repetition rule.
- **Worked example.** How many five-digit numbers can be made from 0, 1, 2, 3 and 4 without repetition? First place: 4 choices. The remaining four digits, including zero, fill four places in 4! = 24 ways. Total 4 x 24 = 96.
- **Second example.** Four-digit numbers from 0, 1, 2 and 3 without repetition: first place 3 choices, then 3! = 6, total 18.
- **With a second restriction.** If the number must also be even, the units slot is restricted too. Then the two restricted slots interact, because zero is both an even digit and a forbidden first digit. Split into cases: units digit zero, and units digit a non-zero even digit. Count each case with its own first-place choices and add.
- **Two ways to go wrong.** Filling the first place from all n digits; and the subtler one, when two restricted slots share a digit (such as zero) and you multiply their choices without splitting cases.

### Words with repeated letters

- **Formula.** The number of arrangements of a word of n letters in which one letter appears a times, another b times, and so on, is n! / (a! x b! x ...).
- **Why we divide.** If the two E's in a word were coloured differently, every arrangement would be counted once for each way of swapping the E's. Swapping identical letters does not create a new word, so we divide by the number of such swaps.
- **Worked example (LEVEL).** LEVEL has 5 letters: L twice and E twice. Arrangements: 5! / (2! x 2!) = 120 / 4 = 30.
- **Worked example (SUCCESS, from the Advanced drill).** SUCCESS has 7 letters: S three times and C twice. Arrangements: 7! / (3! x 2!) = 5040 / 12 = 420.
- **Counter-example.** Miss one repeat and the count doubles. Dividing SUCCESS by 3! only gives 840, which double-counts every word by swapping the two C's. Write the repeat count for every letter before dividing.

### Advanced: count the complement

- **Idea.** When the restricted cases are easier to count than the allowed ones, count all cases and subtract the forbidden ones. "At least one" is the classic signal: at least one = all - none.
- **Worked example.** How many three-digit numbers contain at least one digit 7? All three-digit numbers: 900. Numbers with no 7: first digit 8 choices (1 to 9 except 7), then 9 and 9, giving 648. At least one 7: 900 - 648 = 252.
- **Why direct counting is harder.** Counting "exactly one 7", "exactly two 7s" and "three 7s" separately works, but needs three cases and care about the first digit in each. The complement needs one case.

The complement is only as good as its two counts: if "all" and "none" are counted under different rules, the subtraction is meaningless. If "all" allows repetition and "none" is counted without repetition, the subtraction mixes two different populations.

### Items tied to positions

- **Approach.** If an item must sit in particular positions, place it first; if it must avoid particular positions, either place it in the allowed positions first or subtract the forbidden placements.
- **Worked example.** In how many arrangements of the letters of PLANT is A at one of the two ends? Place A first: 2 ways. Arrange the other four letters: 4! = 24. Total 48.
- **Second example.** Four colours, red, green, blue and yellow, fill a row of four cells, and red may not be at either end. Red takes one of the 2 middle cells; the other three colours fill three cells in 3! = 6 ways. Total 12.
- **The usual failure.** Placing the constrained item last. By then its allowed positions may already be taken in some branches, and a single product cannot express that.

### Neighbouring colours must differ

- **Formula.** To colour a strip of n stripes with k colours so that no two neighbouring stripes share a colour, the first stripe has k choices and each later stripe has k - 1 choices (anything except its left neighbour). Total k x (k - 1)^(n - 1).
- **Worked example.** Five stripes, three colours, no two neighbours alike: 3 x 2 x 2 x 2 x 2 = 48.
- **Watch for.** The formula fails for a ring of stripes, where the last stripe also touches the first. Then the last stripe's choices depend on whether the first and the second-last match, and cases must be split.

### Digit sums, number forms and digit frequency

These families are still arrangement counts, but the clean formula is replaced by a structured list.

- **Digit-relation counts.** When a rule ties one digit to the others, list by the digit that the rule pins down. How many three-digit numbers have a middle digit equal to the sum of the other two digits? Call the digits a, b, c, with a at least 1. The rule says b = a + c, so list by the middle digit b. For a given b, the first digit a can be 1, 2, ..., b, and then c = b - a is fixed and lies between 0 and b - 1: b numbers. For b = 1 there is 1 number (110); for b = 2 there are 2 (121, 220); and so on up to b = 9 with 9 numbers. Total 1 + 2 + ... + 9 = 45. Allowing a = 0 by mistake gives b + 1 choices for each b and 54, which counts strings such as 055 that are not three-digit numbers. A condition on the digit sum over a range of numbers is listed the same way: fix the leading digits that the range allows, then list the remaining digits under the sum rule.
- **Form constraints.** A five-digit palindrome reads the same both ways, so it has the form a b c b a. Choose a from 1 to 9 and b, c from 0 to 9: 9 x 10 x 10 = 900. Only three slots are free; the other two copy them.
- **Odd digits.** Three-digit numbers whose digits are all odd: each slot has 5 choices (1, 3, 5, 7, 9), giving 125; with distinct digits, P(5, 3) = 60. Zero is not odd, so the first-place rule never bites here.
- **Digit properties over a range.** Split the range by the number of digits, because each length has its own first-digit rule, and cut the last block at the end of the range. How many whole numbers from 1 to 400 have every digit even? One-digit: 2, 4, 6, 8, so 4. Two-digit: the tens digit is 2, 4, 6 or 8 and the units digit is 0, 2, 4, 6 or 8, so 4 x 5 = 20. Three-digit up to 400: the hundreds digit must be even and at most 4, so it is 2 (giving 5 x 5 = 25 numbers from 200 to 288) or 4, where only 400 itself lies in the range. That block gives 26. Total 4 + 20 + 26 = 50. Treating the hundreds digit 4 like the hundreds digit 2 would add 24 numbers above 400 and give 74. The same split by length and by place also counts how often a single digit is printed: each place is counted separately, and a number that shows the digit twice contributes twice.
- **What keeps a list honest.** A list goes wrong when the cases are not organised by one slot. Listing by one slot (the restricted slot, or the first digit), then the next, guarantees that no case is missed or repeated.

### Position in a dictionary list

- **Method.** To find the position of a word in the alphabetical list of all arrangements of its letters, count the words that come before it, slot by slot, and add 1.
- **Worked example.** Arrange A, B, C, D in every order and list alphabetically. Where is BDAC? Words starting with A: 3! = 6. Words starting with B whose second letter is smaller than D: the second letter could be A or C, each followed by 2! orders: 4 words. Then BDA followed by C is the next word. Position: 6 + 4 + 1 = 11.
- **Reverse position.** If the list is in reverse alphabetical order, the position is total + 1 - forward position. Here 24 + 1 - 11 = 14.
- **Sorting the letters of one word.** A different question sorts the letters of a single word and compares the sorted order with the original. Write PLANET, then write its letters in reverse alphabetical order beneath: T, P, N, L, E, A. Compare position by position: P-T, L-P, A-N, N-L, E-E, T-A. Only the 5th position keeps its letter, so one letter is unchanged. With repeated letters, keep every copy in the sorted row; dropping a repeat shifts every later position.
- **Common slip.** The position method goes wrong when, at each slot, you count smaller letters from the whole alphabet rather than from the letters still unused. The sorting comparison fails when repeated letters are merged.

### Codes, PINs and passwords

- **Set-up.** A code is a sequence of slots, each with its own pool and its own repetition rule. Write the pool size under each slot before multiplying.
- **Worked example.** A password has two different capital letters followed by three digits, and the first of the digits may not be zero. Slots: 26 x 25 x 9 x 10 x 10. Each slot's pool is written separately, which keeps the rules visible.
- **Read the rule per block.** Errors come from applying "different" to only some slots, or to all slots when it was stated for only some. Read the repetition rule for each block of slots.

### Error analysis (Advanced): the recurring slips and their repairs

```text
   SLIP                                      REPAIR
   order decision skipped                 -> ask "does swapping two items change it?"
   leading zero allowed                   -> write the legal first digits before any factorial
   one repeat factorial missed            -> list every repeated letter with its count
   restricted slot filled last            -> fill the slot with the rule first
   complement with mixed rules            -> count "all" and "none" under one rule
   ring treated as a strip                -> a ring's last item touches the first
```

The Advanced error table above is a diagnosis tool. After a wrong answer, find your slip in the left column before redoing the item. Two slips met in this lesson show how it is used: the repeat-factorial slip gives 840 instead of 420 for SUCCESS, and the leading-zero slip gives 60 instead of 48 in the slot diagram.

### One formula for the whole item: why it misleads

The tempting method is to write the whole answer as one formula, such as P(5, 3), because the numbers 5 and 3 appear in the stem. It looks expert. The reply is that a formula assumes every slot has the same pool, which is false whenever there is a leading zero, a parity rule, a fixed position or a repeated letter. The slot diagram makes the pool of each slot visible, and a formula is safe only when all the pools match.

The second tempting method is to divide by a repeat factorial for every letter that "looks important" while forgetting another. The reply is to write each letter with its count before dividing.

### UPSC application

- **Constrained digit-string permutations (2016 Q72), restricted digit arrangements (2021 Q66), digit row arrangements (2022 Q10) and constrained-digit arrangements (2025 Q58).** Draw slots, fill the restricted slot first, split cases when zero is both forbidden and required, and list cases when the conditions link one digit to another.
- **Colour arrangement counts (2018 Q62) and adjacent-colour stripe counts (2023 Q66).** Use the position rule or k x (k - 1)^(n - 1), and read whether every colour must be used.
- **Constrained permutation (2020 Q67) and position-constrained permutation counts (2023 Q19).** Place the constrained items first, or subtract their forbidden positions, then divide by repeat factorials within each group of positions.
- **Digit-sum integer counts (2021 Q19) and form-constraint number counts (2022 Q79).** List by the slot the rule or the range pins down, or count only the free slots of the form.
- **Odd-digit counting (2022 Q18) and digit-frequency counting (2024 Q45).** Use 5 choices per odd slot and fill any extra rule's slot first; for a digit counted over a range, split by length and by place.
- **Letter arrangement with a spacing condition (2022 Q24).** Place the constrained pair first by listing the position pairs that satisfy the spacing, then arrange the rest.
- **Constrained PIN enumeration (2022 Q55), constrained password counts (2022 Q76) and grid row arrangements (2022 Q77).** Write the pool and repetition rule under each slot; when the digits must appear in a fixed order, list the allowed digit sets instead of orderings; use the complement for "at least one".
- **Reverse alphabetical position counts (2023 Q80).** Write the sorted row under the original word, keep every repeated letter, and compare position by position.
- **Constrained-word permutation count (2026 Q9).** Glue the letters that must stay together into one unit, then divide by the repeats that remain.

### Revision points

- Decide first whether swapping two items changes the result; if it does, you are arranging.
- Draw one box per slot and write the number of choices in each box at the moment of filling.
- Fill the restricted slot first; the free slots take what is left.
- P(n, r) = n! / (n - r)! for r things from n different things, no repetition.
- With repetition allowed, each slot keeps the full pool: n^r.
- A number cannot start with zero; fill the first place from the non-zero digits.
- When zero is both forbidden in front and allowed at the end, split into cases.
- Repeated letters: n! / (a! x b! x ...); divide by every repeat.
- Advanced: at least one = all - none, with both counted under the same rule.
- No two neighbours alike in a strip: k x (k - 1)^(n - 1); a ring needs cases.
- Digit-relation and digit-sum counts: list by the digit the rule pins down, or by the leading digits the range allows.
- Digit properties over a range: split by number length and cut the last block at the end of the range.
- Palindromes and other forms: count only the free slots.
- Dictionary position: count earlier words slot by slot using unused letters, then add 1.
- Advanced error analysis: name the slip before redoing the item.

### Practice

**MCQ 23**

In how many distinct arrangements of the letters of the word TOFFEE do all three vowels appear together?

- A. 12, with no factor for the arrangements inside the vowel block
- B. 144, with every letter treated as different
- C. 36, with repeats divided out inside and outside the block
- D. 72, with the two E's treated as different

**MCQ 23 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Counts the arrangements of the outside units but forgets that the vowel block can itself be arranged. T, F, F and the block give 4! / 2! = 12, which must still be multiplied by the block's internal orders.
- **B — Incorrect:** Ignores both repeated letters: 4! for the units and 3! for the block, 24 x 6 = 144. The two F's and the two E's are identical, so both repeat factorials must divide.
- **C — Correct:** The vowels O, E, E form one block. The units T, F, F and the block number 4, with F repeated, so they arrange in 4! / 2! = 12 ways. Inside the block, O, E, E arrange in 3! / 2! = 3 ways. Total 12 x 3 = 36. Listing all 180 distinct arrangements of TOFFEE and keeping those with the three vowels side by side also gives 36.
- **D — Incorrect:** Divides the outside arrangement by 2! for the F's but treats the two E's inside the block as different: 12 x 3! = 72. The block's internal orders must also be divided by 2!.

**MCQ 24**

Using the digits 0, 1, 2, 3, 4 and 5, with no digit repeated, how many four-digit even numbers can be formed?

- A. 180, with zero allowed in the first place
- B. 96, with the endings in zero omitted
- C. 144, with four first-place choices in every case
- D. 156, with the zero ending and the other endings counted apart

**MCQ 24 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Fills the units slot with 0, 2 or 4 and then fills the other three slots from the five remaining digits, 3 x 5 x 4 x 3 = 180. This allows a zero in the first place whenever the units digit is 2 or 4.
- **B — Incorrect:** Counts only the case in which the units digit is 2 or 4, which gives 2 x 4 x 4 x 3 = 96. The numbers ending in 0 have been left out.
- **C — Incorrect:** Applies the "first digit has 4 choices" reasoning to all three units digits, 3 x 4 x 4 x 3 = 144. When the units digit is 0, zero is already used and the first place has 5 choices, so the two cases cannot share one product.
- **D — Correct:** Split by the units digit. Units 0: the first place has 5 choices, then 4 and 3, giving 60. Units 2 or 4: the first place cannot be 0 or the units digit, so 4 choices, then 4 and 3, giving 48 for each, 96 together. Total 60 + 96 = 156, which a direct listing of all four-digit strings from these digits confirms.

**MCQ 25**

A four-digit PIN uses the digits 0 to 9. A PIN may begin with 0, and digits may repeat. How many PINs contain at least one repeated digit?

- A. 4960, from 10000 by the complement route
- B. 5040, the all-different PINs
- C. 4320, the PINs with exactly one repeated pair
- D. 9790, by subtracting the unordered sets of four digits

**MCQ 25 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** All PINs: 10^4 = 10000, since a PIN may begin with 0. PINs with all four digits different: 10 x 9 x 8 x 7 = 5040. At least one repeat: 10000 - 5040 = 4960. Checking all 10000 PINs one by one gives the same 4960.
- **B — Incorrect:** Reports the count of PINs with all digits different, 5040. That is the complement of the requested set, so it must be subtracted from 10000, not given as the answer.
- **C — Incorrect:** Counts only PINs with exactly one pair and two other different digits: choose the two places for the pair in 6 ways, then 10 x 9 x 8 = 720, giving 4320. PINs with two pairs, a triple or four equal digits also have a repeat.
- **D — Incorrect:** Subtracts the number of unordered sets of four different digits, 210, from 10000, giving 9790. A PIN is ordered, so the all-different count is 5040, not 210.

---

## Lesson 11 - Counting selections: combinations, partitions and routes

Progress: Lesson 11 of 18 | Stage: Core | Subtopic: Counting selections: combinations, partitions and routes

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### The trouble with "how many teams"

A selector must choose three officers from seven for a field visit. Someone counts 7 x 6 x 5 = 210 and is surprised that the official answer is much smaller. The 210 counts the same three officers many times: once as Asha-Bilal-Chitra, again as Bilal-Asha-Chitra, and so on. A team does not care about order. This lesson teaches how to count when order does not matter, how to handle members who must be included or kept out, and how to count routes and splits, which turn out to be selections in disguise.

### Visual: a selection tree and a route lattice

```text
   SELECTION TREE: choose 3 from 7 when member X has a condition

                         all teams of 3 from 7
                               C(7,3) = 35
                       ____________|____________
                      |                         |
               X IS IN the team           X IS NOT in the team
          choose 2 more from 6          choose 3 from the other 6
              C(6,2) = 15                    C(6,3) = 20
                      |                         |
                      +-------> 15 + 20 = 35 <--+   (the two cases never overlap)

   ROUTE LATTICE: moves only EAST (->) or NORTH (^), from S to T

     y=2    1 ----- 3 ----- 6 ----- 10  = T
            |       |       |       |
     y=1    1 ----- 2 ----- 3 ----- 4
            |       |       |       |
     y=0    S=1 --- 1 ----- 1 ----- 1
           x=0     x=1     x=2     x=3

   each number = (number from the left) + (number from below)
   T = 10 = C(5,2): 5 moves in all, choose which 2 are NORTH
```

Start with the tree. Every team of three either contains X or does not. These two branches split the teams with no overlap and no gap, so their counts add to the total. When a question says "X must be included", you take only the left branch; when it says "X must be excluded", only the right.

Now the lattice. Each corner shows how many shortest routes reach it from S. A corner can be entered only from the left or from below, so its number is the sum of those two neighbours. The far corner T has 10 routes. There is also a shortcut: every route is 5 moves, of which exactly 2 are north, and choosing which 2 of the 5 moves are north is a selection. The lattice and the shortcut agree.

### Baskets and shelves

Picking fruit for a basket is a selection: an apple, a mango and a banana make the same basket whichever you picked first. Lining the same three fruits up on a shelf is an arrangement: each ordering looks different. The number of baskets is smaller than the number of shelves by exactly the number of ways to line up the chosen fruits.

### Step 0: the order test, again

Ask, as in the arrangements lesson: if two chosen items swap, is the result different? For a committee, a handshake, a set of coins or a group of questions to attempt, no: count selections. For a captain and vice-captain, a code, or a finishing order, yes: count arrangements.

- **Where the test misleads.** A selection that contains roles. "Choose a president and a secretary from 8" is ordered, because the two posts are different, even though the word "choose" appears.

### Combinations and their mirror symmetry

- **The count.** The number of ways to select r items from n different items, order ignored, is C(n, r) = n! / (r! x (n - r)!). It requires r to be between 0 and n.
- **Symmetry.** C(n, r) = C(n, n - r). Choosing 7 people to go is the same as choosing the 2 who stay: C(9, 7) = C(9, 2) = 9 x 8 / 2 = 36.
- **Worked example.** How many ways can 3 books be chosen from 6? C(6, 3) = 6 x 5 x 4 / (3 x 2 x 1) = 20.
- **Scope.** It counts unordered groups of different items. It stops when the items are identical (three identical coins have only one selection of two), or when items may be chosen more than once.
- **Counter-example.** Using the formula for identical items overcounts. Choosing 2 balls from 5 identical red balls gives one possible handful, not C(5, 2) = 10.

### Select first, then arrange

- **Identity.** P(n, r) = C(n, r) x r!. First select the r items, then arrange them.
- **Worked example.** Choose 3 of 6 books (20 ways), then arrange them on a shelf (3! = 6 ways): 120 = P(6, 3) = 6 x 5 x 4.
- **Use.** This gives a fast check. If you computed a selection and the options look about r! times too big, someone has counted orders.
- **Where it breaks.** The identity fails when some of the chosen items are identical, because then not all r! orderings are different.

### Handshakes and pairs

- **The fact.** Among n people, each pair shakes hands once: C(n, 2) = n(n - 1)/2 handshakes. The same count gives the number of line segments joining n points, the number of matches in a round robin, and the number of pairs of people.
- **Worked example.** Ten people each shake hands once with every other: C(10, 2) = 45.
- **Watch for.** The count of pairs equals the count of different straight lines only when no three points lie on one line. Three points on one line give three pairs but one line.

### Include, exclude, keep apart

- **Approach.** List the cases by the restricted member, as in the selection tree.
- **Must include.** Team of 4 from 9 that must include Anand: Anand is placed, so choose 3 more from the other 8. If it must also exclude Bina, choose those 3 from the 7 who are neither Anand nor Bina: C(7, 3) = 35.
- **Must include a whole subgroup.** A team of 5 from 10 that must contain all three members of a named subgroup: those 3 are placed, so choose 2 more from the remaining 7: C(7, 2) = 21.
- **Keep apart.** Team of 3 from 7 in which Xavier and Yamini will not serve together: all teams C(7, 3) = 35, minus teams containing both, which need 1 more from the other 5, so 5. Answer 30.
- **At least a number from one group.** Split into exact cases (exactly 2, exactly 3, and so on) and add; or subtract the forbidden cases from the total.
- **The double-count trap.** "At least two from group A" is often counted as "choose 2 from A, then choose the rest from everyone". That double-counts every team with more than two from A, because each such team can be built from several different "first two" choices.

### When to add and when to multiply

- **The principle.** If a task can be done in one of several separate ways, add the counts. If it is done in stages, multiply.
- **Worked example.** From a town to a city there are 3 buses and 2 trains: 3 + 2 = 5 ways to make the trip. From the city to a hill station there are 4 taxis. A trip from town to hill station through the city: 5 x 4 = 20 ways.
- **Maximum options.** When a question asks for the maximum number of travel options, it usually wants every separate way at each stage counted, then multiplied across stages.
- **When the rule fails.** The rule fails when the "separate" ways overlap. If one bus is also listed among the trains, adding counts it twice.

### Routes on a grid and on one-way roads

- **Lattice.** On a grid where you may move only east or north, the number of shortest routes from one corner to a corner a steps east and b steps north is C(a + b, b). The lattice visual shows 3 east and 2 north: C(5, 2) = 10.
- **Through a point.** Routes that must pass a given corner = routes to that corner x routes from it onward, because each first half combines with each second half.
- **Avoiding a point.** All routes minus routes through that point.
- **Directed network.** When roads are one-way arrows between towns, count by giving the start the value 1 and each later town the sum of the values of the towns with arrows into it. For example, with arrows S to A, S to B, A to B, A to C, A to T, B to T and C to T: S = 1, A = 1, B = S + A = 2, C = A = 1, T = A + B + C = 4. The four routes are S-A-T, S-A-B-T, S-B-T and S-A-C-T.

Two limits apply here. The lattice formula fails if some moves may go west or south, because routes are then no longer all of the same length. The network method fails if the arrows form a loop, because then routes can be infinitely long; check that no arrow leads back.

### Splitting a number into parts

- **Ordered splits.** The number of ways to write n as an ordered sum of k positive whole numbers is C(n - 1, k - 1). Think of n stars in a row and k - 1 bars placed in the n - 1 gaps between them. For x + y + z = 7 with each at least 1: C(6, 2) = 15.
- **Zero allowed.** If each part may be 0, the count is C(n + k - 1, k - 1). For x + y + z = 7 with each at least 0: C(9, 2) = 36.
- **Upper limits: count the shortfalls.** When each part has a maximum, count how far each part falls short of it. Three tests are each marked out of 10, and a student's total is 27. The shortfalls from 10 add to 30 - 27 = 3, and each shortfall is 0 or more, so the count is C(3 + 3 - 1, 2) = C(5, 2) = 10 ways. Counting the marks directly would need every part capped at 10, which is easy to forget; the shortfalls are automatically small enough.
- **Unordered splits.** If order does not matter, list in non-increasing order. The ways to write 7 as a sum of three positive parts are 5+1+1, 4+2+1, 3+3+1 and 3+2+2: 4 ways.
- **Score and coin splits.** How many ways can a score of 10 be made from 2-point and 3-point shots, counting only how many of each? Solve 2a + 3b = 10 in whole numbers: b = 0 gives a = 5; b = 2 gives a = 2. Two ways. How many ways can ₹10 be paid with ₹1, ₹2 and ₹5 coins? List by the number of ₹5 coins: none leaves ₹10 to be paid with ₹2 coins numbering 0 to 5, so 6 ways; one leaves ₹5, so 3 ways; two leaves nothing, so 1 way. Total 10.
- **Distinct amounts from notes.** With one each of ₹1, ₹2, ₹5 and ₹10 notes, the non-empty subsets number 2^4 - 1 = 15, and here every subset gives a different total, so 15 amounts can be paid exactly. When two subsets give the same total, the amounts are fewer than the subsets.
- **Ordered or not?** Stars and bars counts ordered splits. Applying it to an unordered question overcounts: 15 ordered splits of 7 into three positive parts collapse to 4 unordered ones.

### Gaps, circles and passing

- **No two consecutive.** Choosing k items from n in a line with no two next to each other: C(n - k + 1, k). Choosing 3 of 8 numbered posts with no two adjacent: C(6, 3) = 20. The reason: remove one post from each of the k - 1 gaps that must be left, then choose freely.
- **Consecutive blocks in a circle.** Choosing 3 neighbouring seats from 10 seats in a row gives 8 blocks; in a circle it gives 10, because the block may wrap round from the last seat to the first.
- **Passing with a growing step.** If the step grows by one each time (1 place, then 2, then 3, and so on), the ball has moved 1 + 2 + ... + k places after k passes; reduce that by the circle size to find the holder. Ten children stand in a circle and child 1 starts. Who holds the ball after 6 passes? It has moved 1 + 2 + ... + 6 = 21 places, which is two whole laps of 10 and 1 place more, so it is with child 2. Track a few passes by hand to check: child 1 to 2, to 4, to 7, to 1 (after 1 + 2 + 3 + 4 = 10 places), to 6, to 2.
- **Passing round a circle.** If a ball is passed k places clockwise each time among n people, it first returns to the starter after n / gcd(n, k) passes, where gcd is the greatest common divisor. With 12 people and a pass of 8, gcd(12, 8) = 4, so it returns after 3 passes.
- **Circle warning.** The gap formula breaks down in a circle, where the first and last items are also neighbours. Treat the circle separately by fixing whether the first item is chosen.

### Ordered pairs, triplets and assignments

- **Pairs.** Ordered pairs (a, b) from 1 to 10 with a < b: each such pair is just a selection of two different numbers, so C(10, 2) = 45. With a ≤ b, add the 10 equal pairs: 55.
- **Triplets.** Triplets a < b < c from 1 to 9: C(9, 3) = 84, because each set of three numbers can be written in increasing order in exactly one way.
- **Assignments.** Three people take three different jobs, one each, and Arif cannot take job 1. All assignments: 3! = 6. Those with Arif on job 1: 2! = 2. Allowed: 4. If jobs may be given to anyone with no limit, each of 4 tasks can go to any of 3 people: 3^4 = 81.
- **Scanning a printed sequence.** When a stem prints a sequence and asks how many entries meet a condition on their neighbours, pass through it once, left to right, writing a tick or a cross under each entry so that no entry is judged twice or skipped. How many entries of 3 8 2 6 6 9 1 4 7 5 are larger than both of their neighbours (the first and last entries, having one neighbour each, are not counted)? Testing the eight inner entries gives ticks under 8 (between 3 and 2), 9 (between 6 and 1) and 7 (between 4 and 5): three entries. The second 6 is not larger than the 6 beside it, so it gets a cross; a tie with a neighbour fails a "larger than" test. Read the stem's exact wording on which neighbour is tested (before, after or both) and on strict or non-strict comparison before scanning.
- **Conditional sequences.** When a count depends on an earlier choice ("if the first digit is even, the next must be odd"), split into cases by that earlier choice and add.

If the question's pairs are ordered with a and b free (a may exceed b), the selection count no longer applies. Then the count is 10 x 9 = 90 for different numbers.

### A bridge to overlapping groups

A related selection question asks how small an overlap can be. Of 60 students, 35 take Hindi and 28 take Tamil. However the students are chosen, at least 35 + 28 - 60 = 3 must take both, because the two groups together have 63 places and only 60 students.

This bound needs care when some students take neither language and that number is given: then the 60 must be reduced by those students first.

### Filling slots for a team: the trap and the reply

The tempting method is to fill slots, as in the arrangements lesson, because it worked so well there. For a team of three, it gives 7 x 6 x 5 = 210. The reply is that slot-filling counts orders, and a team has none, so divide by 3! or use C(7, 3) = 35 directly. The second tempting method is "choose the compulsory ones, then choose the rest from everyone" for an "at least" question. The reply is that this builds the same team in several ways; use exact cases or the complement.

### UPSC application

- **Maximum travel options (2013 Q14).** Add separate ways at a stage, multiply across stages, and compare the totals for each pair of places.
- **Tennis teams with or without named members (2013 Q15, Q16), teams containing all three males (2013 Q17) and compatible music teams (2013 Q18).** Use the include-exclude tree; remove every team that contains an incompatible pair.
- **Routes from S to T (2014 Q44), directed railway routes (2017 Q77) and route combination counts (2022 Q27).** Use the lattice sums or the directed-network sum, multiply through a forced point, and add separate direct routes.
- **Task assignment (2015 Q69) and constrained assignment counts (2023 Q68).** Place the most restricted task first, then fill the rest; or count all assignments and subtract the forbidden ones.
- **Denomination combinations (2019 Q56) and denomination subset counts (2020 Q60).** List by the largest coin or note; check for equal totals among subsets.
- **Natural number partition counts (2019 Q73), score partition counts (2023 Q5) and integer-constraint solution counts (2023 Q65).** Decide whether the split is ordered; use stars and bars for ordered splits, a non-increasing list for unordered ones, and remove cases that break an upper limit.
- **Sequence conditional counts (2019 Q70) and sequence pair counts (2020 Q34).** Read exactly which neighbour each condition names, then make one marked pass through the sequence.
- **Constrained-triplet counts (2024 Q49).** List by the most restricted member and test each case against every inequality.
- **Non-consecutive selection (2021 Q69), circular consecutive selection (2023 Q48) and circular pass-sequence return (2023 Q54).** Use C(n - k + 1, k) in a line, n blocks in a circle, and track the position round the circle by remainders when the pass length changes.

### Revision points

- If swapping two chosen items does not change the result, count selections.
- C(n, r) = n! / (r! x (n - r)!) and C(n, r) = C(n, n - r).
- P(n, r) = C(n, r) x r!: select, then arrange.
- Pairs, handshakes and round-robin matches among n: C(n, 2).
- List cases by the restricted member: in or out.
- "Not together" = all - together; "at least" = exact cases added, or total - forbidden.
- "Or" adds separate ways; "and then" multiplies stages.
- Lattice routes a east and b north: C(a + b, b); through a point, multiply the two halves.
- Directed network: each town's value is the sum of the values with arrows into it.
- Ordered positive splits of n into k parts: C(n - 1, k - 1); with zeros: C(n + k - 1, k - 1).
- Unordered splits: list parts in non-increasing order; with upper limits, count the shortfalls.
- No two consecutive from n in a line: C(n - k + 1, k); a circle needs separate care.
- Passing k places among n returns after n / gcd(n, k) passes.
- At least |A| + |B| - N people are in both groups of a population N.

### Practice

**MCQ 26**

A review panel of four is to be formed from six engineers and four doctors. The panel must contain at least two doctors. How many different panels are possible?

- A. 90, the panels with exactly two doctors
- B. 115, adding the panels with two, three and four doctors
- C. 168, picking two doctors first, then two more from the other eight
- D. 195, removing only the panels with no doctor from all 210

**MCQ 26 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Counts only panels with exactly two doctors: C(4, 2) x C(6, 2) = 6 x 15 = 90. Panels with three or four doctors also satisfy "at least two".
- **B — Correct:** Split by the number of doctors. Exactly two: C(4, 2) x C(6, 2) = 90. Exactly three: C(4, 3) x C(6, 1) = 24. Exactly four: C(4, 4) = 1. Total 90 + 24 + 1 = 115. Check by complement: all panels C(10, 4) = 210, minus no doctor C(6, 4) = 15, minus exactly one doctor 4 x C(6, 3) = 80, gives 115. Listing all 210 panels confirms 115.
- **C — Incorrect:** Chooses two doctors first and then two of the remaining eight people: 6 x C(8, 2) = 6 x 28 = 168. A panel with three doctors is built from three different "first pairs" of doctors, so it is counted three times.
- **D — Incorrect:** Subtracts only the panels with no doctor, 210 - 15 = 195. Panels with exactly one doctor, 80 of them, also fail the condition and must be removed.

**MCQ 27**

On a street grid, a courier moves only east or north along the streets. Her destination is 4 blocks east and 3 blocks north of her start. She must pass through the junction that is 2 blocks east and 1 block north of her start. How many shortest routes can she take?

- A. 35 shortest routes, disregarding the junction she must pass through
- B. 9 shortest routes, adding the two halves
- C. 18 shortest routes, multiplying 3 routes by 6 routes
- D. 17 shortest routes, avoiding the junction

**MCQ 27 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Counts all shortest routes to the destination, C(7, 3) = 35, ignoring the junction that must be passed.
- **B — Incorrect:** Adds the counts for the two halves, 3 + 6 = 9. Each first half can be followed by each second half, so the counts multiply, not add.
- **C — Correct:** Start to junction: 2 east and 1 north, C(3, 1) = 3 routes. Junction to destination: 2 east and 2 north, C(4, 2) = 6 routes. Each first half combines with each second half: 3 x 6 = 18. Listing all 35 orderings of four east and three north moves and keeping those that touch the junction also gives 18.
- **D — Incorrect:** Computes the routes that avoid the junction, 35 - 18 = 17. The courier must pass through the junction, so these are exactly the routes to exclude.

---

## Lesson 12 - Sets, overlap and inclusion-exclusion

Progress: Lesson 12 of 18 | Stage: Core | Subtopic: Sets, overlap and inclusion-exclusion

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### The double-counting problem

In an office of 40, 25 people drink tea and 22 drink coffee. Someone adds 25 + 22 = 47 and is puzzled, because only 40 people work there. The sum is 7 more than the headcount, and that surplus is not a mistake in the data. It shows that at least 7 people drink both and were counted twice; if some people drink neither, even more must drink both. Every item in this lesson is about counting each person exactly once when groups overlap, and about knowing how much an overlap can be when the stem does not state it.

### Visual: a Venn diagram with labelled regions, and a running tally

```text
   universe U = everyone counted; n = people in none of the three sets

   +- SET A ---------------------+
   |                             |
   |     a          +- SET B ----+-----------------+
   |                |            |                 |
   |                |    ab      |                 |
   |       +- SET C +------------+--------+        |
   |       |        |            |        |  b     |
   |       |  ac    |    abc     |  bc    |        |
   |       |        |            |        |        |
   +-------+--------+------------+        |        |
           |        |                     |        |
           |        +---------------------+--------+
           |             c                |
           |                              |
           +------------------------------+          n (outside all three)

   a, b, c   = "only A", "only B", "only C"
   ab, bc, ac = in exactly those two sets
   abc       = in all three        n = in none

   RUNNING TALLY for "in at least one set"
     + |A| + |B| + |C|      every two-set region counted twice, abc three times
     - |A∩B| - |B∩C| - |A∩C|  two-set regions now once; abc counted 3 - 3 = 0 times
     + |A∩B∩C|              abc restored to once
     = a + b + c + ab + bc + ac + abc
```

First read the diagram. Each of the eight regions is a different kind of person: only in A, in A and B but not C, in all three, in none, and so on. Every person sits in exactly one region. If you know all eight region numbers, every question can be answered by adding regions.

Now read the tally. Adding the three set sizes counts a person in exactly two sets twice and a person in all three sets three times. Subtracting the three pairwise overlaps fixes the two-set people, but it removes the all-three people three times, so they disappear altogether. Adding the triple overlap back restores them to one count. That is why the triple term is added, not subtracted.

### Two club lists in one hall

Imagine taking attendance at two clubs that meet in the same hall. If you count the chess club's list and then the music club's list, a student on both lists gets two ticks. To know how many different students came, you remove one tick from each student who appears twice. Inclusion-exclusion is just this tick-correction, done carefully.

### Two sets: correcting the double count

- **The formula.** |A ∪ B| = |A| + |B| - |A ∩ B|. Here |A| is the number of members of A, A ∪ B ("A union B") is the set of people in at least one of A and B, and A ∩ B ("A intersection B") is the set in both.
- **Worked example.** Of 40 office staff, 25 drink tea, 9 drink both tea and coffee, and 2 drink neither. How many drink coffee? At least one drink: 40 - 2 = 38. Put that into the formula: 38 = 25 + |coffee| - 9, so 22 drink coffee. Exactly one drink: 38 - 9 = 29, or 25 + 22 - 2 x 9 = 29, because the both-group must be removed from each set.
- **Scope.** It answers union, neither and exactly-one questions once the overlap is known. It stops when the overlap is not given; then only a range is possible.
- **Region or intersection?** The formula goes wrong when "both" is confused with "only one of them". If a stem says "9 drink only coffee", that is a region, not the intersection, and the equation must be rebuilt from regions.

### Overlap bounds: what the "neither" information allows

- **No information about "neither".** In a population of N, with |A| and |B| known and nothing said about people outside both sets, the overlap lies between max(0, |A| + |B| - N) and min(|A|, |B|).
- **Why the lower bound.** The two sets together have |A| + |B| places. If that exceeds N, the surplus people must be in both.
- **Why the upper bound.** The overlap cannot exceed the smaller set, because everyone in the overlap belongs to that smaller set.
- **Worked example.** In a group of 50, 28 study A and 24 study B. The overlap can be anything from max(0, 28 + 24 - 50) = 2 to min(28, 24) = 24. Choosing a single number without more data is unjustified.
- **Second example.** A shelf of 40 books holds 26 hardbacks and 23 novels. At least 26 + 23 - 40 = 9 books must be hardback novels, and at most 23.
- **Exactly k in neither.** Then exactly N - k people are in at least one set, and the overlap is no longer a range: it is fixed at |A| + |B| - (N - k). In a group of 70 where 46 like cricket, 37 like football and exactly 5 like neither, 65 like at least one game, so exactly 46 + 37 - 65 = 18 like both.
- **At least k in neither.** Then at most N - k people are in at least one set. The lower bound becomes max(0, |A| + |B| - (N - k)), and the upper bound stays min(|A|, |B|), because a larger overlap shrinks the union and only leaves more people outside. In the same group of 70, if at least 5 like neither, the overlap can be any whole number from 18 to 37: at 37, only 46 like a game and 24 like neither, which is at least 5.

Four slips break these bounds: treating an exact "neither" count as if it left a range, treating an "at least" count as if it fixed the overlap, ignoring the "neither" group, and taking the upper bound from the larger set. The larger set can hold more people than the smaller set has, but the overlap cannot.

### Advanced: three sets

- **The formula.** |A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |B ∩ C| - |A ∩ C| + |A ∩ B ∩ C|.
- **Worked example.** In a survey, 30 read paper A, 25 read B and 20 read C. Ten read A and B, 8 read B and C, 7 read A and C, and 4 read all three. At least one paper: 30 + 25 + 20 - 10 - 8 - 7 + 4 = 54.
- **Fill the regions from the centre outward.** All three: 4. Exactly A and B: 10 - 4 = 6. Exactly B and C: 8 - 4 = 4. Exactly A and C: 7 - 4 = 3. Only A: 30 - 6 - 3 - 4 = 17. Only B: 25 - 6 - 4 - 4 = 11. Only C: 20 - 4 - 3 - 4 = 9. Check: 17 + 11 + 9 + 6 + 4 + 3 + 4 = 54.
- **What the regions give.** Exactly two papers: 6 + 4 + 3 = 13. Exactly one: 17 + 11 + 9 = 37.
- **Counting by how many sets a person is in.** Sometimes the stem gives "exactly two" or "none" instead of the pairwise overlaps. Write E1, E2 and E3 for the numbers in exactly one, exactly two and all three sets. Adding the three set sizes counts each person once per set, so |A| + |B| + |C| = E1 + 2 x E2 + 3 x E3, while the number in at least one set is E1 + E2 + E3. Subtracting gives (sum of set sizes) - (at least one) = E2 + 2 x E3. Worked example: in a club of 100, 50 play chess, 40 play carrom and 30 play cards; 18 play exactly two of these games and 7 play all three. The sum of the set sizes is 120, and 120 - (at least one) = 18 + 2 x 7 = 32, so 88 play at least one game and 12 play none.
- **Check the wording first.** The formula gives a wrong union if the pairwise numbers are "exactly two" counts rather than "at least those two" counts. A stem that says "6 read exactly A and B" gives a region; "10 read A and B" includes the all-three readers. Read which one is given before subtracting.

### Advanced: multiples and the lcm

- **The shortcut.** For counting whole numbers divisible by given integers, the overlap "divisible by both p and q" is "divisible by the least common multiple (lcm) of p and q". The lcm is the smallest number that both p and q divide.
- **Worked example (Advanced drill).** How many integers from 1 to 100 are divisible by at least one of 2, 3 and 5? Divisible by 2: 50. By 3: 33. By 5: 20. By lcm(2, 3) = 6: 16. By lcm(2, 5) = 10: 10. By lcm(3, 5) = 15: 6. By lcm(2, 3, 5) = 30: 3. Total: 50 + 33 + 20 - 16 - 10 - 6 + 3 = 74. Enumerating 1 to 100 confirms 74.
- **Scope and a counter-example.** The lcm shortcut works only for "multiples of given integers". For people, books or any arbitrary sets, the overlap is whatever the data say. Another failure: using the product p x q when p and q share a factor. Multiples of both 4 and 6 are multiples of 12, not of 24.

### Membership tables for named people

Some items describe several people and the activities each takes part in, through clues rather than numbers. Build a table with people as rows and activities as columns, as in the logic-grid lesson, and mark membership. When the clues fix only totals, the table cannot be completed, but it can still be counted: the number of ticks read down the columns equals the number read across the rows.

```text
              stall 1  stall 2  stall 3 | ticks in row
   Asha          ✓        ✓        ✓    |  3
   four others   ?        ?        ?    |  1 or 2 each, 6 between them
   ------------------------------------------------
   ticks in column 3       3        3    |  9 = 9
```

- **Worked example: counting ticks two ways.** Five volunteers, Asha, Bharat, Chitra, Dev and Esha, staff three stalls at a fair. Each stall has exactly three volunteers, every volunteer works at least one stall, and Asha is the only volunteer who works at all three. How many volunteers work at exactly two stalls? Down the columns there are 3 x 3 = 9 ticks. Across the rows, Asha holds 3, so the other four volunteers hold 6, each holding 1 or 2. If all four held 1, they would hold only 4 ticks; each volunteer with 2 adds one more tick, so 6 - 4 = 2 volunteers work at exactly two stalls, and the other 2 work at exactly one.
- **What it establishes.** Many different tables fit these clues (listing them finds 90), and they disagree about who works where. Every one of them has exactly two volunteers on two stalls. A question about a count can be settled even when a question about a named person cannot.
- **Trap.** Drawing one table that fits and reading names off it. Unless the clues force every tick, a named-person answer read from one table may be false in another; and a clue such as "nobody else works at all three" must be applied to every row before any column is read.

### Classification inside classification

When a stem says "some books are novels, all novels are in Hindi, some Hindi books are old", draw nested or overlapping circles exactly as in the syllogism lesson. An intersection question then asks which region must be non-empty.

- **Worked example.** Every novel on a shelf is in Hindi, and every old book on the shelf is a novel. Then the old books sit inside the novels, which sit inside the Hindi books. The intersection of "old" and "Hindi" is the set of old books itself.
- **Draw only what is stated.** Errors come when "some" is drawn as "all" or when an overlap is drawn that the statements do not require. Draw only what is stated, and test claims against every permitted diagram.

### Fractions of one whole

- **The rule.** When set sizes are given as fractions of an unknown total, the total must be a multiple of the lcm of the denominators, and the regions are found by applying inclusion-exclusion to the fractions.
- **Worked example.** In a class, 1/3 like music, 1/4 like dance and 1/6 like both. The fraction liking at least one is 1/3 + 1/4 - 1/6 = 5/12, so 7/12 like neither. If 14 students like neither, the class has 14 / (7/12) = 24 students. The total 24 is a multiple of 12, the lcm of 3, 4 and 6, as it must be.

Mixing fractions with different bases is the error to avoid, for example "1/3 of the class" and "1/2 of the music-lovers". The second fraction is of a different whole and must first be converted to a fraction of the class (1/2 of 1/3 = 1/6).

### Subtracting the triple overlap: why it feels right and is wrong

The tempting method is to add all the set sizes, subtract all the pairwise overlaps, and then subtract the triple overlap as well, because "it is an overlap too". The reply comes from the tally in the visual: after subtracting the three pairwise overlaps, the people in all three sets have been counted 3 - 3 = 0 times, so they must be added back once. A second tempting method is to pick one number for an unknown overlap because it "looks reasonable". The reply is that without more data the overlap is a range, and only facts that hold across the whole range are certain.

### UPSC application

- **Friend who does not play hockey (2013 Q20), friend with a stated game count (2013 Q21) and game common to B, C and D (2013 Q22).** Build a membership table from the clues, then read a column, count across a row, or intersect rows.
- **Book classification intersection (2014 Q21).** Mark each book's features in a yes-no table and read the combination asked for.
- **Venn-diagram counting (2018 Q42, 2019 Q52) and Venn diagram deduction (2019 Q31).** Fill the regions from the centre outward, use the "neither" count to fix the union, and add the regions asked for.
- **Set overlap deduction (2019 Q20) and Venn set overlap range (2021 Q35).** Write the lower bound from the surplus over the population and the upper bound from the smaller set, and judge each "at least" or "at most" claim against that range.
- **Fractional set deduction (2021 Q46).** Treat every fraction as a share of the same whole, and accept only a statement that holds for every overlap the fractions allow.

### Revision points

- Each person sits in exactly one region of a Venn diagram; region numbers add to the total.
- Two sets: |A ∪ B| = |A| + |B| - |A ∩ B|; neither = N - union.
- Exactly one of two sets = |A| + |B| - 2|A ∩ B|.
- Overlap bounds: from max(0, |A| + |B| - N) to min(|A|, |B|).
- Exactly k in neither fixes the overlap at |A| + |B| - (N - k); at least k in neither raises only the lower bound.
- The upper bound comes from the smaller set, never the larger.
- Advanced: three sets: add singles, subtract pairs, add back the triple.
- Advanced: fill three-set regions from the centre outward and check that they sum to the union.
- Advanced: sum of set sizes - (at least one) = (exactly two) + 2 x (all three).
- Distinguish "in A and B" (includes all three) from "in exactly A and B" (a region).
- Advanced: for multiples, the overlap uses the lcm, not the product, and only for multiples.
- Membership tables answer "who does not", "common to" and "exactly k" questions; when only totals are fixed, count the ticks down the columns and across the rows.
- Fractions of one whole: inclusion-exclusion on the fractions; the total is a multiple of the lcm of denominators.
- An unknown overlap is a range; report only facts true over the whole range.

### Practice

**MCQ 28**

A survey covers 200 households. Of these, 110 read paper A, 90 read paper B and 70 read paper C. Exactly 60 households read exactly two of the three papers, and 30 households read none of them. How many households read all three papers?

- A. 40, removing 60 from the surplus of 100 and stopping
- B. 5, treating all 200 households as readers of some paper
- C. 90, which is the number of households reading exactly one paper
- D. 20, two extra counts per all-three household

**MCQ 28 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Finds the extra counts, 270 - 170 = 100, removes the 60 exactly-two households to get 40, and stops. Each all-three household carries two extra counts, not one, so the 40 must be halved.
- **B — Incorrect:** Takes all 200 households as readers of at least one paper, ignoring the 30 who read none: (270 - 200 - 60) / 2 = 5. Only 170 households read any of the papers.
- **C — Incorrect:** Computes 170 - 60 - 20 = 90, which is the number reading exactly one paper. The question asks for the households reading all three.
- **D — Correct:** The set sizes add to 110 + 90 + 70 = 270, which counts each household once for every paper it reads. The households reading at least one paper number 200 - 30 = 170, each counted once. The 100 extra counts come from the exactly-two households (one extra each, 60) and the all-three households (two extra each). So all three = (100 - 60) / 2 = 20. The regions can really occur: for example 25 read exactly A and B, 20 exactly A and C, 15 exactly B and C, 20 all three, and 45, 30 and 15 read only A, only B and only C, which gives every stated total.

**MCQ 29**

A department has 90 officers. Of them, 58 speak Tamil and 47 speak Telugu, and at least 5 officers speak neither language. Which of the following gives every possible value of the number of officers who speak both languages?

- A. 20 to 47, with each endpoint shown to occur
- B. 20 to 42, with the neither group taken from Telugu
- C. 15 to 47, with the neither group ignored
- D. 20 to 58, with the larger group taken as the cap

**MCQ 29 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** At least 5 speak neither, so at most 85 speak a language. Then the overlap is at least 58 + 47 - 85 = 20, and 20 occurs when exactly 5 speak neither. The overlap is at most the smaller group, 47; with 47 in the overlap, 58 officers speak a language and 32 speak neither, which is at least 5. Every whole number in between also leaves at least 5 outside, so the possible values are exactly 20 to 47, as a check of each value from 0 to 58 confirms.
- **B — Incorrect:** Subtracts the 5 officers who speak neither from the smaller group as well, 47 - 5 = 42, as if they had to come out of the Telugu speakers. They are outside both groups, so the upper limit stays at 47: an overlap of 47 leaves 32 officers speaking neither, which satisfies "at least 5".
- **C — Incorrect:** Computes the lower bound from all 90 officers, 58 + 47 - 90 = 15, ignoring the officers who speak neither. Those 5 or more cannot be in either language group, so at most 85 are available.
- **D — Incorrect:** Takes the upper bound from the larger group, 58. The overlap cannot exceed the 47 Telugu speakers, because every officer in the overlap speaks Telugu.

---

## Lesson 13 - Probability, worst cases and weighing strategies

Progress: Lesson 13 of 18 | Stage: Core | Subtopic: Probability, worst cases and weighing strategies

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You already know how to count arrangements and selections. This lesson asks three new questions about the same counted worlds. How likely is an outcome? What is the least I must do to be certain of it? And how do I find one odd object with the fewest tests? The first question is answered with a fraction. The second and third are answered by imagining the unluckiest possible run of events and planning against it.

### Visual: one listed space and one decision tree

```text
SAMPLE SPACE: two fair dice (36 equally likely cells)

             second die
             1   2   3   4   5   6
 first  1    2   3   4   5   6   7
 die    2    3   4   5   6   7   8
        3    4   5   6   7   8   9
        4    5   6   7   8   9  10
        5    6   7   8   9  10  11
        6    7   8   9  10  11  12      cell = sum of the two dice

WEIGHING TREE: 9 coins, one heavier, two-pan balance

                 weigh {1,2,3} v {4,5,6}
              /            |             \
       left heavy       balance        right heavy
       suspect 1-3     suspect 7-9     suspect 4-6
           |               |               |
     weigh 1 v 2      weigh 7 v 8      weigh 4 v 5
     (3 outcomes)     (3 outcomes)     (3 outcomes)
     -> heavy coin found in 2 weighings in every branch
```

Read the grid first. Every cell is one outcome, and every cell is equally likely because each die is fair and the two dice do not influence each other. A sum is not an outcome; it is a label written inside cells. The sum 7 sits on six cells (the long diagonal), while the sum 2 sits on one cell. That is why the eleven possible sums are not equally likely.

Now read the tree. A balance has three results, not two: left heavier, right heavier, or level. Each weighing therefore splits the suspects into three groups. Two weighings give 3 x 3 = 9 end points, which is exactly enough to single out one coin among nine. The tree is the picture behind every weighing question: count the end points the balance can produce, and compare them with the number of suspects.

### Fair lists and unlucky runs

Probability is a share of a fairly listed world. If you can list every outcome so that each one is as likely as every other, the probability of an event is the number of outcomes in the event divided by the number in the list. Everything else in Part A is a way of making that list honest.

Worst-case reasoning is the opposite attitude. You stop asking what usually happens and ask what could happen if every draw went against you. A guarantee must survive the worst run, so you build that run deliberately, then take one more step.

Weighing and crossing strategies use the same habit. You plan so that even the least helpful result of each test still leaves you on track.

### Part A - probability as a fraction of a listed world

### Favourable over total, for equally likely outcomes

**Probability** of an event E is written P(E). For equally likely outcomes, P(E) = (number of favourable outcomes) / (total number of outcomes). Every probability lies between 0 and 1. An answer above 1 or below 0 is a signal that the total was counted wrongly.

Worked example. A bag holds 3 red and 2 blue balls, and one ball is drawn at random. Each of the 5 balls is equally likely, and 3 of them are red, so P(red) = 3/5.

What it establishes: once the outcomes are equally likely, a probability is a plain count over a plain count. Where it stops: it says nothing about two draws, and it says nothing when the outcomes are not equally likely.

**When the formula breaks (equal likelihood, Advanced).** It fails when the listed outcomes are not equally likely. Listing the sums of two dice as "2, 3, ..., 12" gives eleven items, but P(sum = 2) is not 1/11. Rebuild the space from the 36 equally likely ordered pairs. A weighted spinner, a loaded die, or a choice that depends on an earlier choice also needs the space rebuilt.

### The complement

The **complement** of E, written "not E", is every outcome where E fails. P(not E) = 1 - P(E). Use it when "at least one" is hard to count directly but "none" is easy.

Worked example (Advanced). A fair coin is tossed three times. Find P(at least one head). The only outcome with no head is TTT, so P(no head) = (1/2)^3 = 1/8, and P(at least one head) = 1 - 1/8 = 7/8. A second check with fresh numbers: four tosses give P(at least one tail) = 1 - 1/16 = 15/16.

What this shows: "at least one" is usually fastest through "none". Its limit: the complement rule itself is always valid, but the step that computes P(none) by multiplying (1/2) x (1/2) x (1/2) needs the tosses to be independent, meaning one toss does not change the chances of the next.

**Counter-example.** Adding the chances of overlapping events instead of using a complement. "P(head on toss 1) + P(head on toss 2) + P(head on toss 3) = 3/2" is above 1, which proves the events overlap and cannot be added.

### A sequence multiplies conditional fractions

For two events in sequence, P(A and B) = P(A) x P(B | A). The bar is read "given": P(B | A) is the chance of B once A has happened. Without replacement, the second fraction changes, but multiplication is still valid because it uses the changed, conditional fraction.

Worked example. A bag holds 3 red and 2 blue balls. The first draw is red and is not returned. Now 2 red remain among 4 balls, so P(second red | first red) = 2/4 = 1/2. The chance of red then red is (3/5) x (2/4) = 3/10.

Second worked example. A bag holds 4 white and 6 black balls, two drawn in sequence without replacement. P(white then white) = (4/10) x (3/9) = 12/90 = 2/15. If you are simply told the first was white and ask about the second (Advanced), the answer is the conditional fraction alone: 3 white among the 9 left, so 3/9 = 1/3, not 4/10.

Why it matters: the denominator shrinks by one per draw and the numerator shrinks only if the drawn ball was of the counted kind. Where it stops: if the order of the draw is irrelevant, the sequence method must be multiplied by the number of orders, or replaced by the combination count described next.

The classic slip is multiplying the unchanged fraction, (4/10) x (4/10), treats the ball as returned. That answer is correct only with replacement.

### A draw taken together uses combinations

When several balls are drawn together, the order does not exist. Count unordered selections with C(n, r) from Lesson 11.

Worked example. A bag has 3 red and 2 blue balls and two are drawn together. Is it possible to draw two blue balls? Yes: exactly one blue pair exists. Its probability is 1/C(5,2) = 1/10, small but not zero. The probability of two red is C(3,2)/C(5,2) = 3/10. Notice the two different kinds of answer. "Possible" was a yes-or-no question. "Probability" was a number.

Worked example (Advanced). A bag holds 4 white and 6 black balls; two are drawn together. P(no white) = C(6,2)/C(10,2) = 15/45 = 1/3, so P(at least one white) = 2/3. The sequence method agrees: P(black, black) = (6/10) x (5/9) = 1/3.

The point: the unordered count and the sequential product give the same answer when applied correctly. The catch: if the question names an order ("the first is white and the second black"), the unordered count must not be used without adjustment.

**Trap.** Mixing the two worlds: an ordered numerator over an unordered total, or the reverse, doubles or halves the answer.

### Dice and coin counting (Advanced)

For k fair dice the space has 6^k ordered outcomes; for k fair coins it has 2^k. Count favourable outcomes by listing ordered tuples.

- Two dice, P(sum = 7): the pairs (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) give 6 of 36, so 1/6.
- Two dice, P(sum at least 10): sums 10, 11, 12 come from (4,6), (5,5), (6,4), (5,6), (6,5), (6,6), again 6 of 36, so 1/6. This equality with the previous answer is a coincidence of the counts, not a rule.
- A fresh check: P(sum = 8) uses (2,6), (3,5), (4,4), (5,3), (6,2), so 5/36. The pair (4,4) is counted once because the two dice show the same face in only one ordered way.

**Common slip.** Counting (3,5) and (5,3) as one outcome. The dice are two separate objects, so the ordered pairs are the equally likely units.

### Non-exclusive events (Advanced)

Two events are not exclusive when both can occur together. Then P(A or B) = P(A) + P(B) - P(A and B). Adding the two probabilities counts the overlap twice. Example: one card is drawn from a 52-card deck, A = the card is red, B = the card is a king. Red cards are 26, kings are 4 and red kings are 2, so P(red or king) = 26/52 + 4/52 - 2/52 = 28/52 = 7/13. Adding the first two terms alone gives 30/52, which counts the two red kings twice. The subtraction matters only when the overlap is non-empty; for exclusive events P(A and B) = 0 and the plain sum is correct.

### Possible, probable and certain

| Word | What it needs | Typical stem |
|---|---|---|
| Possible | at least one favourable outcome exists, so P > 0 | "Can it happen?" |
| Certain | every outcome is favourable, so P = 1 | "Must it happen?" |
| Probable | the measured fraction is large | "How likely is it?" |

An event with probability 1/1000 is fully possible and highly improbable. In statement items, "it is not necessary that Y" means that Y fails in at least one consistent case. One counter-case settles it; no probability is needed.

**Two category errors.** Answering a yes-or-no "possible?" question with a fraction, or treating "unlikely" as "impossible".

### Draws with repeats, wrong placements, rule tests and fixed flips

**Draws with and without repeats.** A quiz-master has 8 topic cards and draws one at random each round, putting it back before the next draw. The chance that the history card turns up at least once in three rounds is 1 - (7/8)^3 = 169/512, about one third. If instead each drawn card is set aside, the first three cards drawn are a random three of the eight, so the history card turns up within three rounds with chance 3/8. The words "put back" or "set aside" decide which model applies. Using the set-aside model when cards are put back, or the reverse, is the mistake to avoid.

**Wrong placements.** An arrangement in which no item sits in its own place is called a **derangement**, and the number of derangements of n items is written D_n. Small cases can be listed by hand: D_1 = 0, D_2 = 1 and D_3 = 2. Larger ones come from a recurrence, D_n = (n - 1) x (D_(n-1) + D_(n-2)). The reason: item 1 goes to some other place j, in n - 1 ways; then either item j goes to place 1, leaving n - 2 items to derange, or it does not, which behaves exactly like deranging n - 1 items. So D_4 = 3 x (2 + 1) = 9, D_5 = 4 x (9 + 2) = 44 and D_6 = 5 x (44 + 9) = 265. A direct formula agrees: D_n = n! x (1 - 1/1! + 1/2! - 1/3! + ... ± 1/n!), which is the whole number nearest to n!/e, so close to 37% of all arrangements are derangements once n is 4 or more.

Worked example. Six keys have been taken off their six locks and are hung back at random, one key on each lock. In how many ways does no key hang on its own lock, and in how many does at least one key hang on its own lock? No key on its own lock: D_6 = 265. At least one: all 6! = 720 hangings minus 265, which is 455, the complement again. The chance that no key is on its own lock is 265/720 = 53/144, about 0.37.

Two general facts follow from the same idea. The number of arrangements of n items with exactly k of them in their own places is C(n, k) x D_(n-k): choose the k items that stay, then derange all the others. And exactly n - 1 items in their own places can never happen, because the one item left over has only its own place free. Where this goes wrong: assuming every split of "right" and "wrong" can occur because each looks plausible on its own, or choosing the items that stay and then letting the others fall anywhere instead of deranging them.

**Rule-testing cards.** A clerk claims: "If a form is marked URGENT on the front, it carries a signature on the back." Four forms lie on a desk showing URGENT, ROUTINE, SIGNED and UNSIGNED. Which must be turned over to test the claim? Turn URGENT (it must show a signature) and UNSIGNED (it must not say URGENT). The claim is A -> B, and the only case that breaks it is "A and not B". This is the contrapositive from Lesson 1. **The tempting extra card:** SIGNED. A signed form with a ROUTINE front does not break the claim, because the claim never said only urgent forms are signed. That would be the converse.

**Turning a fixed number at a time: can the goal be reached?** Coins lie heads up, and every move turns over exactly k of them. Before hunting for moves, ask whether the goal can be reached at all, using an **invariant**: a feature that no move can change. Suppose a move turns k coins, h of which show heads. Those h become tails and the other k - h become heads, so the number of heads changes by (k - h) - h = k - 2h. If k is even, that change is even, so the head count never changes from odd to even or back. If k is odd, the change is odd, so the head count switches between odd and even at every move.

Worked example. Nine coins lie heads up, and each move turns exactly four coins. Can all nine be made to show tails? Four is even, so the head count stays odd after every move. It starts at 9, which is odd, while the goal of 0 heads is even, so no sequence of moves, however long, reaches it. Change the rules to eight coins with seven turned per move. Seven is odd, so the head count switches between even and odd at each move, and getting from 8 heads (even) to 0 heads (even) needs an even number of moves. Parity allows it, and a construction confirms it: in move i, turn every coin except coin i, for i = 1 to 8. Each coin is turned in seven of the eight moves, an odd number of times, so every coin ends tails up.

Keep the two checks apart. The invariant can prove a goal impossible, but passing the parity test does not by itself prove the goal reachable; that needs an explicit sequence of moves.

### Part B - the worst case and the "plus one" rule

```text
GOAL: be certain of 3 balls of one colour (bag: plenty of red, plenty of blue)

draw 1  draw 2  draw 3  draw 4  | draw 5
  R       B       R       B     |  R or B
  \_____ failing hand: ____/    |  any colour now makes 3
       2 red + 2 blue = 4       |  answer = 4 + 1 = 5
```

A **failing hand** is the largest collection you could hold that still does not meet the target. The guarantee is one more than the size of the failing hand. The picture shows the unluckiest drawer: every draw avoids the third ball of a colour for as long as it can.

### The rule, and where it fails

1. Describe the target exactly ("three of one colour", "two of a named colour", "one of each colour", "one matching pair").
2. Build the largest failing hand, respecting how many of each item actually exist.
3. Add one.

Worked example. From three colours of balls, with plenty of each, how many draws ensure two of one colour? The failing hand is one of each colour, 3 balls, so the answer is 4.

Worked example with a stock limit. A box holds 7 black, 4 white and 1 grey pen. How many draws, in the dark, ensure 3 pens of one colour? The failing hand takes 2 black, 2 white and only the 1 grey that exists: 5 pens. The answer is 6, not 2 x 3 + 1 = 7.

Worked example with a different target. With the same box, how many draws ensure two pens of different colours? Now the failing hand is a run of one colour only, and the longest such run is all 7 black pens. The answer is 8. The target changed, so the failing hand changed from a spread of colours to a single colour.

What these establish: the failing hand is built from the target, not from a formula. Where they stop: the rule gives the least number that guarantees the result; it does not give the chance of getting the result sooner.

**Where it fails.** Ignoring the stock. If a colour has fewer items than the failing hand would like to take, the hand can take only what exists.

### Pairs and gloves

Five pairs of socks in five different colours sit loose in a drawer. A matching pair is guaranteed after 6 socks, because the failing hand holds one sock of each colour. Gloves differ, because a left glove only pairs with a right glove of the same colour. With 4 pairs of gloves in four colours, the failing hand can hold all 4 left gloves (or any mix with at most one glove per colour), so 5 gloves guarantee a matching left-and-right pair. The error is treating handed objects as if any two of a colour match.

### Queues and elimination counts

**Positions in a queue.** A queue question may ask where someone can stand rather than how long the queue is. In a queue of 15 people, exactly 4 people stand between Ravi and Sita, and Ravi has more people ahead of him than behind him. How many different places can Sita occupy? Number the places 1 (front) to 15. If Ravi is at place p, he has p - 1 people ahead and 15 - p behind, so p - 1 > 15 - p, which gives p from 9 to 15. Four people between them puts Sita 5 places from Ravi: ahead of him at p - 5, which covers places 4 to 10, or behind him at p + 5, which stays inside the queue only when p is 9 or 10, giving places 14 and 15. Sita can stand at places 4 to 10, 14 or 15: 9 places. What to check: both sides. Placing Sita only ahead of Ravi, or only behind him, loses places, and every place must lie inside the queue for at least one of Ravi's allowed places.

**Counting by losses.** In a contest without draws, each match produces exactly one loser, so matches can be counted by counting losses instead of following the rounds. Thirty-two entrants enter a knockout in which every tie is a best-of-three series: the first entrant to win two games goes through, and the loser of a series is out. How many games can be played? Count series first: every entrant except the champion loses exactly one series, so there are 31 series. Each series lasts 2 games or 3 games. So the games number at least 2 x 31 = 62 and at most 3 x 31 = 93, and every total in between can occur, because each series independently lasts 2 or 3 games. The slip to avoid is following the bracket round by round, which needs the pairings and any byes, or multiplying by the number of entrants instead of the number of series.

### Part C - weighing and crossing strategies

### The thirds rule for one heavier coin

A two-pan balance gives three results, so k weighings can separate at most 3^k suspects. With one coin known to be heavier, the least number of weighings for n coins is the smallest k with 3^k at least n. The strategy splits the suspects into three groups as equal as possible, places two of them on the pans, and keeps the third aside.

A test follows from the same count: a first split works only if every group, both pans and the pile aside, holds at most 3^(k - 1) coins, because that is all the remaining k - 1 weighings can handle.

Worked example: which first weighings still work? There are 20 coins, one of them heavier, and three weighings are allowed (3^3 = 27 is at least 20, while 3^2 = 9 is not, so three is also the least number that can work). A first weighing of a coins against a coins leaves 20 - 2a aside. Whatever the result, the last two weighings can handle at most 3^2 = 9 suspects, so a must be at most 9 and 20 - 2a must be at most 9. That allows a = 6, 7, 8 or 9: four first weighings work, from 6 against 6 with 8 aside to 9 against 9 with 2 aside. Following 7 against 7 with 6 aside, the suspects drop to at most 7; then 3 against 3 with 1 aside leaves at most 3; then 1 against 1 with 1 aside finds the coin.

The principle behind it: the count of possible results must be at least the count of suspects, and splitting in thirds reaches that bound. Where it stops: if the odd coin could be heavier or lighter, each coin carries two possibilities, and the count changes. Three weighings then handle at most 12 coins, not 27.

**Why halving fails.** Placing half on each pan wastes the "level" result, because a level balance is impossible when all suspects are on the pans.

### Reading inequalities from weighings

Pan results are inequalities, and the ordering chains of Lesson 7 apply. Suppose A + D outweighs B + C, while A + B balances C + D. Subtract the balance from the inequality: (A + D) - (A + B) is greater than (B + C) - (C + D), so D - B is greater than B - D, and D is heavier than B. Put that into A + B = C + D: since D is heavier than B, A must be heavier than C. **Do not over-read a balance:** a balanced pair of groups does not mean that each member on one side equals a member on the other. A + B = C + D says nothing about A against C on its own.

### When the odd item may be heavier or lighter

When the odd item may be heavier or lighter, read each result as a statement about which items are cleared. With 3 coins and one odd of unknown direction: weigh coin 1 against coin 2. If they balance, coin 3 is odd, and one more weighing against coin 1 tells you heavier or lighter. If they do not balance, weigh coin 1 against coin 3. A balance clears 1 and 3 and convicts 2; an imbalance convicts 1. Two weighings decide both identity and direction. **What changes:** the 3^k count cannot be used unchanged. Each suspect now carries two possibilities, heavier or lighter, so the same number of weighings handles fewer coins.

### One weight of each: which loads can be measured?

A different question asks which loads a set of weights can measure. Take one weight each of 2 g, 5 g and 9 g. On one pan only, the weights can only add, so the measurable loads are the subset sums: 2, 5, 7, 9, 11, 14 and 16 g. If weights may go on both pans, a weight placed beside the load subtracts, so each weight is added, subtracted or left out. The positive signed sums are 2, 3 (5 - 2), 4 (9 - 5), 5, 6 (9 + 2 - 5), 7, 9, 11, 12 (9 + 5 - 2), 14 and 16. So, of the whole loads from 1 to 16 g, exactly 1, 8, 10, 13 and 15 g cannot be weighed even with both pans. To test one load, ask whether it can be written as a signed sum; to list every load, write the 3 x 3 x 3 = 27 sign patterns and drop duplicates and totals that are not positive. When a stem limits how many of each weight may be used, list by the largest weight first and respect the limit in every case. **Trap:** counting sign patterns or subsets instead of distinct totals; two patterns can give the same load, as 7 = 9 - 2 = 5 + 2 shows.

### Buying with coins versus weighing with coins

Coins of 4 g and 9 g are available in any number. Buying coins means the coins only add up, so a total can be bought only if it equals 4a + 9b for whole numbers a and b, each 0 or more. Weighing a load on a two-pan balance lets coins sit beside the load as well, so signed totals count too. Which of 14 g, 19 g and 26 g can be bought exactly, and which can be weighed?

Buying: list by the number of 9 g coins. 14 and 14 - 9 = 5 are not multiples of 4, so 14 g cannot be bought. 19, 10 and 1 are not multiples of 4, so 19 g cannot be bought. 26 - 18 = 8 = 2 x 4, so 26 g can be bought with two coins of each size. Weighing: all three can be weighed. 14 = 9 + 9 - 4, so put the load and one 4 g coin on one pan and two 9 g coins on the other; 19 = 9 + 9 + 9 - 4 - 4; and 26 = 9 + 9 + 4 + 4 on one pan. In fact 9 - 4 - 4 = 1 shows that a 1 g difference can be built, so every whole load can be weighed. In general, with two coin sizes that share no common factor above 1, every whole load can be weighed, while buying misses a finite list of small totals; here the totals that cannot be bought are 1, 2, 3, 5, 6, 7, 10, 11, 14, 15, 19 and 23 g, and every total from 24 g upward can be bought.

What separates the two questions is the rule, not the coins: add-only for buying, signed for weighing. Using one rule for the other question gives a wrong yes or a wrong no.

### Crossing with one torch: trips and deadlines

When a group must pass through a tunnel, or over a river, with one torch or one raft that has to come back, two ideas do most of the work.

```text
EACH FORWARD TRIP carries at most c people;  EACH RETURN brings at least 1 person back

after f forward trips and f - 1 returns:
      people across  <=  c x f - (f - 1)  =  (c - 1) x f + 1

least forward trips  =  smallest f with (c - 1) x f + 1 >= n
least crossings      =  2f - 1          (the last trip needs no return)
```

**Counting trips.** Eleven campers must cross a river on a raft that holds at most four, and someone must row it back after every trip except the last. What is the least number of crossings? Each round trip moves at most 4 - 1 = 3 people net, and the last trip moves up to 4. So (4 - 1) x f + 1 must reach 11. Three forward trips give at most 3 x 3 + 1 = 10, which is short, so 4 forward trips are needed, and 4 forward trips need 3 returns: 7 crossings. A plan that achieves it uses forward trips of 4, 4, 4 and 2 people, with one person rowing back after each of the first three: four cross and one rows back (3 across), four cross and one rows back (6 across), four cross and one rows back (9 across), then the last two cross (11 across). Dividing 11 by 4 and rounding up gives 3 forward trips, which forgets that every return carries one person back.

**Testing a deadline.** Six campers with crossing times of 1, 2, 3, 7, 8 and 9 minutes use a raft that holds four, and a group crosses at its slowest member's pace. Can all six be across within 12 minutes? Argue from lower bounds rather than by trying plans. The trip count gives 2 forward trips and 1 return. The forward trip that carries the 9-minute camper costs 9, and the return costs at least 1. If the 7-minute or 8-minute camper travels on the other forward trip, the total is at least 9 + 1 + 7 = 17. So all three slow campers share one trip, and the return must be made by a fast camper (a slow returner would cost at least 7 more). The other forward trip then carries the fast campers who have not yet crossed together with the returner, and the 3-minute camper is always among them, so that trip costs at least 3. The total is at least 9 + 1 + 3 = 13 minutes, so 12 minutes is not enough. Thirteen minutes is enough: 1, 7, 8 and 9 cross (9 minutes), the 1-minute camper rows back (1), and 1, 2 and 3 cross (3).

The general pairing idea behind both: put the slowest walkers on one trip so that their slow times are paid once, and let the fastest do the returning. Where it goes wrong: forgetting the returns when counting trips, splitting the slowest walkers across trips, or ignoring a stem's own rules about who must carry the light back and where it must finish, which can change both the trip count and the time.

### Averages, unchanged fractions and halving: three traps

The most tempting wrong method in this lesson is to answer a guarantee question with an average or a probability: "a third of the balls are green, so about three draws should give a green." That reasoning describes what usually happens. A guarantee must hold in the unluckiest run. The reply is to write the failing hand explicitly, with the stock limits, and add one.

The second tempting method is to multiply unchanged fractions after a draw without replacement. The reply is to rewrite the bag after each draw, then read off the new fraction.

The third is to halve in weighing problems. The reply is to count results: a balance has three, so thirds use every result.

### UPSC application

The paper uses this lesson in several recognisable families.

- **Blind-draw colour guarantees (2017 Q56), worst-case colour-group draws (2023 Q36) and worst-case shoe selection (2023 Q4):** build the failing hand with the stock, then add one. Read whether the target is "some colour reaches k", "every colour appears" or "a usable pair of a named colour".
- **Dinner-host lottery (2015 Q9):** decide which model the draw follows, then answer exactly the quantity asked, which may be a chance, a guaranteed count or neither.
- **Derangement possibility checks (2023 Q6):** test whether a stated split of right and wrong placements can exist before computing anything; count "exactly k right" by choosing the right ones and deranging the rest.
- **Card-flip puzzle (2014 Q25):** use the odd-or-even invariant to decide whether the goal can be reached, and build an explicit sequence of moves when it can.
- **Elimination-match counting (2022 Q17):** read the elimination rule and whether draws can occur before choosing how to count matches.
- **Queue minimum size (2022 Q30):** number the places, write each stated count ahead, behind or between as a relation between places, and keep every picture the relations allow.
- **Coin purchase versus weighing (2023 Q69):** decide for each statement whether it is about add-only buying or two-pan weighing before testing it.
- **Weighing-combination count (2026 Q23):** a count of ways to make up one stated load from weights of four sizes, with a limit on how many of one size are used; it belongs with the weights section.
- **Odd-item weighing logic (2026 Q51):** identical-looking objects, one of them odd in a stated direction, and a balance; it belongs with the thirds rule.
- **Bridge crossing with final lamp return (2016 Q27):** read every rule about capacity, who brings the light back and where it must finish before applying the trip count and the slowest-together idea.

### Revision points

- Probability = favourable / total only when the listed outcomes are equally likely.
- Every probability lies between 0 and 1; a value outside that range exposes a counting error.
- P(not E) = 1 - P(E); "at least one" is usually fastest through "none".
- A sequence multiplies conditional fractions; without replacement the later fractions change.
- A draw taken together uses C(n, r); an ordered numerator over an unordered total is a mixed count.
- Two dice give 36 ordered pairs; sums are labels, not equally likely outcomes.
- "Possible" is yes or no, "probability" is a number, "certain" means probability 1.
- A guarantee equals the largest failing hand plus one, with each colour capped at its stock.
- Handed objects such as gloves pair only left with right.
- Derangements: D_n = (n - 1)(D_(n-1) + D_(n-2)), giving 0, 1, 2, 9, 44, 265; exactly k in place = C(n, k) x D_(n-k); exactly n - 1 in place is impossible.
- Count matches by losses: one loss per match.
- Turning exactly k items per move: an even k never changes whether the head count is odd or even; test reachability with this invariant before searching for moves.
- k weighings separate at most 3^k suspects when the odd coin is known to be heavier; after the first weighing every group must be at most 3^(k - 1).
- Pan results are inequalities that can be subtracted and chained.
- Buying adds pieces; weighing may also subtract them, so a load is measurable when it is a positive signed sum.
- Crossings: least forward trips is the smallest f with (c - 1)f + 1 at least n; test a deadline with lower bounds; send the slowest together.

### Practice

**MCQ 30**

A bag holds 5 green and 3 yellow counters. Three counters are drawn one after another without replacement. What is the probability that the first two counters are green and the third is yellow?

- A. 75/512, slightly more than one chance in seven
- B. 5/28, nearly one chance in five
- C. 15/28, slightly more than one chance in two
- D. 15/128, slightly less than one chance in eight

**MCQ 30 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Treats the draws as if each counter were returned: (5/8) x (5/8) x (3/8) = 75/512, about 0.146. Without replacement the bag shrinks after every draw.
- **B — Correct:** The first draw is green with 5/8. Then 4 green are among the 7 counters in the bag, so 4/7. Then 3 yellow are among the 6 in the bag, so 3/6. The product is 60/336 = 5/28, about 0.179, which is nearly 1/5. A full listing of the 336 ordered draws gives the same fraction.
- **C — Incorrect:** Multiplies the correct product by 3, as if the yellow counter could come first, second or third: 3 x 5/28 = 15/28. The stem fixes the order, so only one order counts.
- **D — Incorrect:** Lowers the numerators but keeps the denominator at 8 for every draw: (5 x 4 x 3)/(8 x 8 x 8) = 60/512 = 15/128, about 0.117. The number of counters in the bag also falls with each draw.

**MCQ 31**

A pile of identical-looking coins contains exactly one counterfeit, which may be either heavier or lighter than a genuine coin. A two-pan balance may be used exactly twice, and a separate supply of coins known to be genuine may be placed on either pan. What is the largest number of coins in the pile for which the counterfeit, and whether it is heavier or lighter, can always be found?

- A. 9, the bound for a coin known to be heavier
- B. 3, the bound with no genuine coin to borrow
- C. 4, since each coin needs two end points, heavier and lighter
- D. 8, one coin per result except level twice

**MCQ 31 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Uses the count for a counterfeit whose direction is known, 3 x 3 end points for 9 coins. Here each coin can be heavier or lighter, so 9 coins would bring 18 cases to only 9 end points.
- **B — Incorrect:** Gives the largest pile that two weighings can settle when no genuine coin is available, as in the three-coin example of the lesson. The genuine supply lets the pans be balanced in number without using suspect coins, which raises the bound by one.
- **C — Correct:** Two weighings give at most 3 x 3 = 9 end points, and each coin brings two cases, heavier and lighter, so 2n cases need 2n to be at most 9, which gives n at most 4. Four coins can be done: weigh coins 1 and 2 against coin 3 and a genuine coin. If the pans balance, coin 4 is the counterfeit, and weighing it against a genuine coin shows heavier or lighter. If the left pan sinks, the cases are 1 heavier, 2 heavier or 3 lighter; weigh 1 against 2, and the heavier side names the coin, while a balance convicts coin 3 as lighter. A rising left pan is the mirror image. Checking every case of every coin confirms that this plan never fails, while five coins bring 10 cases, more than 9 end points.
- **D — Incorrect:** Gives each of the nine possible pairs of results one coin, leaving out level-then-level, which treats every coin as a single case. Each coin needs two end points, one for heavier and one for lighter, so 8 coins would need 16.

**MCQ 32**

A drawer holds 9 red, 6 blue, 4 green and 3 yellow socks. Socks are taken out one at a time in the dark and are not put back. What is the least number of socks that must be taken out to be certain of having at least two socks of each of two different colours?

- A. 5, enough for one matching pair
- B. 10, all nine reds and then a second colour
- C. 6, a red pair and three single socks, then another
- D. 13, every red and one each of blue, green, yellow, then one more

**MCQ 32 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Answers a smaller target. With four colours, 5 socks guarantee one pair of some colour, but the target is two socks in each of two different colours.
- **B — Incorrect:** Takes all 9 reds and one more sock, 10. That sock gives a second colour only one sock, and the other colours can each add a single sock without completing a second pair.
- **C — Incorrect:** Caps the red socks at a pair, giving a hand of 2 + 1 + 1 + 1 = 5 and then a sixth sock. Red socks can keep arriving well past two without helping the target, so the unluckiest hand is much larger.
- **D — Correct:** A hand misses the target while at most one colour has two or more socks. The largest such hand takes all 9 reds and one sock each of blue, green and yellow: 12 socks. The 13th sock must be blue, green or yellow, which gives that colour its second sock. Checking every possible hand from the drawer confirms that 12 is the largest hand without the target, so 13 socks are needed.

---

## Lesson 14 - Plane-figure counting

Progress: Lesson 14 of 18 | Stage: Core | Subtopic: Plane-figure counting

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A figure appears on the page with lines crossing in every direction, and the question asks how many squares, triangles or rectangles it contains. The eye jumps around, counts some shapes twice and misses others. The cure is not sharper eyesight. It is a counting plan: name the shapes by size or by the lines that form them, count each kind once, and add. This lesson turns plane figures into the selections you learned in Lesson 11.

### Visual: a size table and a diagonal matrix

```text
A 4 x 4 SQUARE GRID (5 horizontal and 5 vertical lines)

  +--+--+--+--+      SQUARES BY SIDE LENGTH
  |  |  |  |  |      side 1 : 4 x 4 positions = 16
  +--+--+--+--+      side 2 : 3 x 3 positions =  9
  |  |  |  |  |      side 3 : 2 x 2 positions =  4
  +--+--+--+--+      side 4 : 1 x 1 position  =  1
  |  |  |  |  |                          total = 30
  +--+--+--+--+      RECTANGLES: one choice of 2 vertical lines
  |  |  |  |  |      and 2 horizontal lines; C(5,2) x C(5,2)
  +--+--+--+--+      choices, minus the 30 squares = 70 non-square
```

| Convex polygon, n sides | Segments joining vertices, C(n,2) | Sides | Diagonals, n(n-3)/2 |
|---|---:|---:|---:|
| 4 (quadrilateral) | 6 | 4 | 2 |
| 5 (pentagon) | 10 | 5 | 5 |
| 6 (hexagon) | 15 | 6 | 9 |
| 7 (heptagon) | 21 | 7 | 14 |
| 12 (dodecagon) | 66 | 12 | 54 |

The size table lists every square exactly once, because each square has one side length and one position. A square of side s fits in (5 - s) positions across and (5 - s) down, which is where the products come from. The rectangle line underneath uses a different idea: a rectangle is fixed by its two vertical edges and its two horizontal edges, so it is a choice of two lines from each family.

The matrix shows the relationship behind the diagonal formula. Every pair of vertices gives a segment. Some of those segments are sides; the rest are diagonals. Subtract the sides from the pairs and you get the diagonal column.

### The plain idea

A shape in a figure is not a picture to be spotted; it is a choice of parts. A rectangle is a choice of two vertical lines and two horizontal lines. A triangle is a choice of three points that are not in a straight line. A diagonal is a choice of two corners that are not neighbours. Once you can say what choice makes the shape, the count becomes a selection count, and the only remaining danger is choosing the same shape twice or choosing something that is not a shape at all.

### Method 1: count by size, exactly once

List the shapes by size or type, count each class, and add the classes.

Worked example. A 3 x 3 square grid has 9 unit squares, 4 squares of side 2, and 1 square of side 3. The total is 14. In a square grid of side n, the number of squares is 1^2 + 2^2 + ... + n^2. For a full 8 x 8 board that sum is 204.

What it establishes: a class-by-class list cannot count the same square twice, because each square belongs to exactly one size class. Where it stops: the plain sum of squares works only for a full grid with every line drawn. If a line is missing, some squares disappear and each class must be recounted by position.

**Failure condition.** Scanning visually and adding as you go. The eye returns to a big square after counting its smaller pieces and counts the big one again, or it misses the squares that straddle two regions. This is the **double-count trap**: the same shape is counted under two descriptions.

### Method 2: rectangles and parallelograms from two families of lines

A rectangle drawn along grid lines is fixed by choosing 2 of the vertical lines and 2 of the horizontal lines. With a vertical lines and b horizontal lines the count is C(a, 2) x C(b, 2).

Worked example. How many rectangles in the 4 x 4 grid of the visual are not squares? There are 5 lines in each direction, so the line choices number C(5,2) x C(5,2) = 10 x 10 = 100. The size table has already counted the squares among them: 30. Subtract: 100 - 30 = 70 rectangles that are not squares. The pattern is "all line choices, then remove the class the stem excludes", which works for any excluded class you can count on its own.

The same reasoning counts **parallelograms**. When one family of a parallel lines crosses another family of b parallel lines, any 2 lines of the first family and any 2 of the second enclose exactly one parallelogram, so the count is C(a, 2) x C(b, 2). A parallelogram needs two pairs of parallel sides, so it always takes its two pairs from two different families.

Worked example with three families. A drawing has three families of parallel lines running in three different directions: 3 lines in family P, 4 in family Q and 5 in family R. Every parallelogram uses two lines from one family and two from another, so list the pairs of families and add:

| Families used | Count | Value |
|---|---|---:|
| P and Q | C(3,2) x C(4,2) = 3 x 6 | 18 |
| P and R | C(3,2) x C(5,2) = 3 x 10 | 30 |
| Q and R | C(4,2) x C(5,2) = 6 x 10 | 60 |
| Sum | | 108 |

The lines of the third family cut across each parallelogram but do not destroy it: its four sides are still drawn, so it can still be traced.

What it establishes: rectangles and parallelograms are counted by lines, not by boxes, and with more than two directions the count is a sum over pairs of families. Where it stops: multiplying all three choices together, 3 x 6 x 10 = 180, would build a figure from six lines, which is not a parallelogram. If extra slanting lines are not in parallel families, the new shapes need a separate list.

**Failure condition.** Counting boxes instead of lines. A row of 4 boxes has 5 boundary lines; choosing 2 of the 4 boxes gives C(4,2) = 6, while choosing 2 of the 5 lines gives C(5,2) = 10. The single boxes themselves are rectangles, and only the line count includes them.

### Method 3: segments, lines and diagonals

Among n points, the number of segments joining two of them is C(n, 2). These segments lie on C(n, 2) distinct straight lines only when no three points are **collinear**, meaning lying on one straight line.

Worked example with a collinear set. Eight points have exactly three on one line and no other three collinear. The pairs are C(8,2) = 28. The three collinear points give C(3,2) = 3 pairs, but all three lie on one line, so remove 3 and add back 1: 28 - 3 + 1 = 26 distinct lines.

The **diagonal formula** n(n - 3)/2 counts diagonals of a **convex** polygon, one in which every interior angle is less than 180 degrees, so every diagonal lies inside. Each vertex joins to n - 3 others by a diagonal (not itself and not its two neighbours), and each diagonal has two ends, so divide by 2.

Worked example (Advanced, the formula run backwards). Which convex polygon has exactly three times as many diagonals as sides? Set n(n - 3)/2 = 3n. Divide both sides by n: (n - 3)/2 = 3, so n - 3 = 6 and n = 9. A nonagon has 9 x 6 / 2 = 27 diagonals, which is 3 x 9. Check with the matrix logic: C(9,2) = 36 segments, minus 9 sides, gives 27. The backward use also settles impossibility: can a convex polygon have exactly 30 diagonals? That needs n(n - 3) = 60, but 9 x 6 = 54 and 10 x 7 = 70, so no whole n works and no such polygon exists.

What it establishes: diagonals are the vertex pairs that are not sides. Where it stops: the formula assumes the shape's corners are the only points, and that the polygon is convex.

**Failure condition (Advanced).** Using n(n - 3)/2 for a figure that is not a convex polygon, or for points that include collinear ones. For a star-shaped or dented shape, some joining segments pass outside the figure, and the question may or may not count them; read the stem.

### Method 4: triangles by type, removing collinear triples

A triangle needs three points that are not collinear. Start from C(n, 3) and subtract the triples that lie on a line.

Worked example. With the same eight points (three collinear), C(8,3) = 56 triples, and exactly one triple is collinear, so 55 triangles.

**Points on a circle.** No three points on a circle are collinear, so every triple gives a triangle. Seven points on a circle give C(7,3) = 35 triangles, and C(7,4) = 35 quadrilaterals. The same test extends to four corners: a quadrilateral needs four points with no three collinear, so any set of four that puts three or more points on one line must be removed.

**Right angles on a circle.** Picture a circle with a straight line through its centre, a diameter, and a third point anywhere else on the circle. Join the third point to both ends of the diameter: the angle at the third point is always 90 degrees. The property runs both ways. A triangle drawn with all three corners on a circle has a right angle exactly when one of its sides is a diameter, and the right angle sits opposite that side. So a right-angled triangle on a circle is a choice of one diameter plus one more point.

Two consequences follow, and both are counted through diameters rather than angles.

- **Rectangles on a circle.** A quadrilateral with all four corners on a circle has four right angles exactly when both of its diagonals are diameters. So every rectangle with corners among the points is a choice of 2 diameters, and with d diameters available there are C(d, 2) rectangles. A square is one of them, not an extra class.
- **Right angle at a named point.** If a point X is to carry the right angle, the side opposite X must be a diameter that does not use X. So the number of right-angled triangles with the right angle at X equals the number of diameters that avoid X.

Worked example. Nine points sit on a clock face at the hour marks 12, 1, 2, 4, 6, 7, 8, 10 and 11. (a) How many rectangles have all four corners among these points? (b) How many right-angled triangles have the right angle at the mark 11, and how many at the mark 12?

1. Find the diameters first. Two hour marks end a diameter when they are 6 hours apart: 12 and 6, 1 and 7, 2 and 8, 4 and 10. The mark 11 would need 5, which is not among the points. So d = 4.
2. Rectangles: C(4,2) = 6. One of the six, with corners 1, 4, 7 and 10, has its two diameters at right angles to each other, so it is a square; it is already inside the 6.
3. Right angle at 11: no diameter uses 11, so all 4 diameters can serve as the opposite side: 4 triangles. Right angle at 12: the diameter 12 and 6 uses 12 itself, so only the other 3 diameters serve: 3 triangles.

What it establishes: rectangles and right angles on a circle are both counted from the list of diameters. Where it stops: the points must lie on one circle, and a diameter exists only when both of its ends are among the points. If an odd number of points are equally spaced, no two are exactly opposite, so there are no diameters, no rectangles and no right angles among them.

**Failure condition.** Counting right angles at the centre, or crediting a triangle with a right angle at a corner that lies on its diameter. The centre is not one of the points, and the right angle sits only at the corner opposite the diameter; a point that ends a diameter cannot carry the right angle of a triangle built on that same diameter.

**Triangles inside a drawn figure.** Count by the vertex that every triangle shares. Draw a triangle, and from its top vertex draw lines to the base so that the base is cut into 4 parts. There are now 5 lines from the top vertex (two sides and three inner lines). Every triangle in the figure has the top vertex as a corner and its base on the bottom line, so it is a choice of 2 of the 5 lines: C(5,2) = 10. Add one line parallel to the base that crosses all five lines, and every pair of lines now makes one triangle with the base and one with the new line: 2 x 10 = 20.

What it establishes: a type list, organised by a shared vertex or by the line that carries the base, counts each triangle once. Where it stops: a figure with lines that meet at different points needs its own list; there is no single formula for every drawing.

**Triangles on a drawing of a solid.** A drawing of a solid shows several faces at once, and some drawn lines cross the inside. Count face by face, then add the triangles that use an inner line, and check each candidate: all three sides must be drawn lines and the three corners must not lie on one line. Worked example: a pyramid on a square base ABCD with apex P is drawn with both base diagonals AC and BD, which meet at O. The four slanting faces give 4 triangles (PAB, PBC, PCD, PDA). The two inner sections through the diagonals give 2 more (PAC, PBD), because PA, PC and AC are all drawn lines. The base square with its diagonals gives 4 half-squares (ABC, BCD, CDA, DAB) and 4 quarter-squares meeting at O (AOB, BOC, COD, DOA). The sum is 4 + 2 + 4 + 4 = 14. No triangle uses P and O together, because the line from P to O is not drawn. Where it stops: a drawing that hides some edges must say whether hidden edges count; read the stem before listing.

**Failure condition.** Forgetting collinear triples. Three points on one line pass the "choose 3" step but form no triangle.

### Method 5: board diagonals and runs of cells

A board with m rows and n columns of unit cells has a corner-to-corner diagonal. The number of cells that the diagonal passes through (through the inside, not only touching a corner) is m + n - gcd(m, n), where gcd is the greatest common divisor. The reason: the diagonal enters a new cell each time it crosses a vertical or horizontal line, but at a grid corner it crosses both at once, and those corners occur gcd(m, n) - 1 times along the way.

Worked example. A board with 4 rows and 6 columns: 4 + 6 - 2 = 8 cells. A square 8 x 8 board: 8 + 8 - 8 = 8 cells, because the diagonal passes only through corners between cells.

What it establishes: board-diagonal items reduce to counting line crossings. Where it stops: if the question asks how many squares of all sizes the board contains, use Method 1 instead; the two questions are different.

**Failure condition.** Adding m + n without subtracting the corner crossings, which counts cells that the line only touches at a point.

**Runs of consecutive cells along a line.** A different board question asks about runs of k consecutive cells in a straight line. Count line by line: a line of L cells holds L - k + 1 runs of length k when L is at least k, and none when L is shorter than k. Never let the term go negative. For slanting lines, list the length of every diagonal in each of the two slanting directions and apply the same rule to each diagonal on its own.

Worked example, run backwards. A board has 4 rows and 9 columns. For which run length k (k at least 2) do the rows and columns together hold exactly 16 runs of k consecutive cells?

| k | rows: 4 x (10 - k) | columns: 9 x (5 - k), or 0 if k > 4 | sum |
|---:|---:|---:|---:|
| 4 | 24 | 9 | 33 |
| 5 | 20 | 0 | 20 |
| 6 | 16 | 0 | 16 |
| 7 | 12 | 0 | 12 |

The answer is k = 6, and it is the only one: the sum falls steadily as k grows (59, 46, 33, 20, 16, 12, 8, 4 for k = 2 to 9). The columns are only 4 cells long, so they hold no run of 6. Failure condition: writing 9 x (5 - 6) = -9 for the columns gives 16 - 9 = 7 at k = 6, and the learner wrongly concludes that no k gives 16. A line shorter than k contributes zero, not a negative count. On slanting lines the same slip appears as a negative term for a short diagonal, and a second slip is forgetting one of the two slanting directions.

Worked example on slanting lines. A board has 4 rows and 6 columns. How many slanting lines (in both directions together) are long enough to hold a run of 3 cells, and how long is the longest slanting line? Lines running down to the right start on the top row or the left column, so there are 4 + 6 - 1 = 9 of them, with lengths 1, 2, 3, 4, 4, 4, 3, 2, 1. Five of the nine have length 3 or more. The lines running down to the left have the same lengths, so the two directions together give 10 lines long enough, and the longest slanting line has 4 cells, the number of rows. Failure condition: counting the lines as rows + columns = 10 per direction forgets that the corner cell is shared by a row start and a column start; counting one direction only gives 5; and counting every line, short ones included, gives 18 instead of 10.

### Why one careful look is not a counting plan

The tempting method is to look carefully and count everything in one pass, trusting attention. It feels faster, and on a small figure it may work. On anything larger it fails in two predictable ways: shapes made of several smaller shapes get missed, and shapes already counted get counted again from another angle. The reply is a written list by size or type, with one line per class and a total at the end. The list takes twenty seconds longer and removes both errors.

A second tempting method is to use a formula on the wrong figure: C(n,3) when some points are collinear, or n(n - 3)/2 for a non-convex shape. The reply is to state the formula's condition before using it.

### UPSC application

- **Rectangles from grid lines and grid parallelogram counts:** choose two lines from each family; subtract squares when the question asks for rectangles that are not squares.
- **Polygon diagonal counts:** n(n - 3)/2 for a convex polygon; check by pairs minus sides.
- **Chessboard diagonal counts:** decide whether the question counts cells crossed by a diagonal, squares of all sizes, or runs of consecutive cells along lines, then use the matching method.
- **Circle-inscribed triangle counts:** every triple of points on a circle forms a triangle; a right angle needs a diameter as the opposite side, so list the diameters among the points before counting anything else.
- **Solid-shape triangle counts:** go face by face, then add triangles that use inner lines, checking that all three sides are drawn.
- **Collinearity-aware triangle counts:** C(n,3) minus the collinear triples; for lines, remove the collinear pairs and add back one line.

### Worked check: the 2 x 2 grid

Quick case: a 2 x 2 square grid. It holds four unit squares and one square of side 2, so five squares in total. The same count comes from the sum of squares of the side lengths: 1 squared plus 2 squared is 5. Failure condition: the sum-of-squares form counts only grids whose sides are the whole number of cells, so it cannot be used when the figure is not a complete grid.

### Revision points

- Count shapes by size or type, with each class written down once.
- Squares in an n x n grid: 1^2 + 2^2 + ... + n^2; an 8 x 8 board has 204.
- Rectangles from a lines by b lines: C(a,2) x C(b,2); count lines, not boxes.
- Two crossing families of parallel lines give parallelograms by the same product; with three families, add the products for each pair of families.
- Segments among n points: C(n,2); distinct lines only if no three are collinear.
- With k collinear points, remove C(k,2) pairs and add back 1 line.
- Diagonals of a convex polygon: n(n - 3)/2 = C(n,2) - n.
- Triangles: C(n,3) minus collinear triples; points on a circle have none.
- On a circle, a triangle is right-angled exactly when one side is a diameter; rectangles on a circle = C(d,2) for d diameters.
- In a figure with a shared top vertex, triangles = pairs of lines from that vertex, times the number of base lines.
- A corner-to-corner diagonal of an m x n board crosses m + n - gcd(m,n) cells.
- A line of L cells holds L - k + 1 runs of k consecutive cells, and zero (never a negative number) when L is shorter than k; add over every line, in every direction the stem allows.
- Triangles on a solid drawing: face by face, then inner lines; all three sides must be drawn lines.
- Visual scanning double-counts; a written size list does not.

### Practice

**MCQ 33**

A rectangle is divided by grid lines into 3 rows and 5 columns of equal unit squares. The cell in the middle row and the middle column is shaded. How many rectangles that can be traced along the grid lines contain the shaded cell?

- A. 36, pairing boundary lines that enclose the shaded cell
- B. 90, counting every rectangle drawn on the board wherever it sits
- C. 54, counting the rectangles that reach across the whole middle column
- D. 8, counting only the squares of all sizes over it

**MCQ 33 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** A rectangle contains the shaded cell exactly when its left edge is one of the 3 vertical lines on the cell's left side or on its left boundary, its right edge is one of the 3 on the right, its top edge is one of the 2 horizontal lines above or on the cell, and its bottom edge is one of the 2 below or on it. That gives 3 x 3 x 2 x 2 = 36, which a full listing of all 90 rectangles confirms.
- **B — Incorrect:** Counts all C(6,2) x C(4,2) = 15 x 6 = 90 rectangles and ignores the condition that the shaded cell must lie inside.
- **C — Incorrect:** Applies the condition only across the columns: 3 x 3 choices of left and right edges times all C(4,2) = 6 choices of top and bottom gives 54. Many of these sit in the top or bottom row and miss the shaded cell.
- **D — Incorrect:** Lists only squares: 1 of side 1, 4 of side 2 and 3 of side 3 cover the cell, giving 8. Rectangles with unequal sides that contain the cell are left out.

**MCQ 34**

Six points are marked on one straight line, and four other points are marked on a second line parallel to the first. How many quadrilaterals have all four corners among these ten points? Count each set of four corners once.

- A. 210, from every choice of four of the ten marked points
- B. 90, two corners taken from each of the lines
- C. 194, after removing only the sets with all four on one line
- D. 21, adding the pairs of points available on the two lines

**MCQ 34 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Uses C(10,4) = 210 and ignores collinearity. A set with three or four corners on one line cannot be the corners of a quadrilateral.
- **B — Correct:** No three corners of a quadrilateral may lie on one line, and every point lies on one of the two lines, so a valid set takes exactly two points from each line: C(6,2) x C(4,2) = 15 x 6 = 90. The two pairs join in one way into a trapezium. Check: 210 - C(6,4) - C(4,4) - (C(6,3) x 4 + C(4,3) x 6) = 210 - 15 - 1 - 104 = 90.
- **C — Incorrect:** Removes the C(6,4) = 15 and C(4,4) = 1 sets with all four points on one line, giving 194, but keeps the 104 sets with three points on one line and one on the other. Three collinear corners leave no fourth side to close the figure, so those sets fail too.
- **D — Incorrect:** Adds C(6,2) + C(4,2) = 15 + 6 = 21. A quadrilateral needs one pair from each line at the same time, so the pair counts multiply.

---

## Lesson 15 - Solid and cube counting

Progress: Lesson 15 of 18 | Stage: Core | Subtopic: Solid and cube counting

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A flat page cannot show all six faces of a cube at once. The question gives you two or three pictures of the same cube, or an unfolded paper shape, or a painted block sawn into pieces, and asks about faces you cannot see. The learner's problem is that the hidden faces seem to require imagination. They do not. They require two facts used carefully: which faces can be seen together, and where each small piece sits in the block. Lesson 14 taught you to count flat shapes by class; this lesson counts solid pieces by class, and Lesson 3 taught you to track what stays fixed while a figure turns.

### Visual: a net that folds, and a block read slice by slice

```text
NET (cross shape)                        FOLDED RESULT
          +---+
          | A |                          A on top, F underneath
      +---+---+---+---+                  B, C, D, E form the ring
      | B | C | D | E |                  around the sides
      +---+---+---+---+
          | F |                          opposite pairs:
          +---+                          A-F,  B-D,  C-E

A 4 x 4 x 4 PAINTED CUBE, cut into 64 small cubes, read one slice at a time

  top slice        middle slices (two of them)      bottom slice
  3 2 2 3          2 1 1 2                          3 2 2 3
  2 1 1 2          1 0 0 1                          2 1 1 2
  2 1 1 2          1 0 0 1                          2 1 1 2
  3 2 2 3          2 1 1 2                          3 2 2 3
  (number = painted faces on that small cube)

  totals:  3 faces 8   |  2 faces 24  |  1 face 24  |  0 faces 8   |  sum 64
```

Start with the net. When the cross folds, the long row of four squares wraps around to make a ring of side faces. In that ring, faces two steps apart end up facing each other, so B is opposite D and C is opposite E. The single squares above and below C fold up to become the top and the bottom, so A is opposite F.

Then read the block. Each grid shows one horizontal slice of the cut cube, and each digit says how many painted faces that small cube carries. Corners of the whole block carry 3, the rest of the edges carry 2, the middles of the outer faces carry 1, and the hidden core carries 0. The totals at the bottom come from counting digits, and they add to 64, which is the check that nothing was missed.

### The plain idea

Two faces that appear in the same picture share an edge, so they cannot be opposite. A face is opposite another only if it never sits beside it. Painted blocks follow a matching idea: a small cube's paint depends only on how many outer faces it touches, and that depends only on whether it is a corner, an edge piece, a face piece or a core piece. Once you name the four classes, the count is arithmetic.

### Method 1: views of a cube and opposite faces

**Rule.** Faces visible together in one view are **adjacent** (they share an edge). Each face has exactly four adjacent faces and one opposite face. Collect every adjacency from every view; the opposite of a face is the one face left over when its four neighbours are known.

Worked example. A cube has its six faces coloured Red, Blue, Green, Yellow, White and Black. One picture shows the corner where Red, Blue and Green meet; a second picture shows the corner where Red, Yellow and White meet. Which opposite pairs do these two pictures fix, and which are still open?

1. Red's neighbours are Blue and Green (first picture) and Yellow and White (second picture). That is four neighbours, so the sixth colour, Black, is opposite Red. This pair is fixed.
2. The other four colours form the ring of side faces around the Red and Black pair. In a ring of four, each face touches two and is opposite one. The pictures show Blue touching Green and Yellow touching White, so Blue's opposite is Yellow or White, and both rings, Blue-Green-Yellow-White and Blue-Green-White-Yellow, fit both pictures.
3. So exactly one opposite pair is fixed. The rest is open: either Blue-Yellow with Green-White, or Blue-White with Green-Yellow. A third picture showing Blue beside Yellow would close it, leaving Blue opposite White and Green opposite Yellow.

What it establishes: four known neighbours fix the opposite face; two known neighbours leave two candidates, and the honest answer may be "not determined". Where it stops: if a face appears in only one view, you know just two of its neighbours, and you must work through other faces first.

**The common-pair rule.** Suppose two views both show the faces 1 and 2, and the third visible face is 3 in one view and 5 in the other. Then 3 and 5 are opposite. The reason: faces 1 and 2 meet along one edge, and exactly two faces touch both of them. One of those two faces closes off the edge at one end and the other closes it off at the other end; each view shows the corner at one end. Faces that cap the two ends of the same edge face away from each other, so they are opposite.

**Failure condition: the opposite pair from a single view.** One picture shows three faces and hides three. Any hidden face could be opposite any shown face. Declaring "the face I cannot see is opposite the one I can" from one picture is the classic trap. Use every view, and conclude only when four neighbours are known or when the common-pair rule applies.

**Working through other faces.** Suppose a face X appears only once, beside Y and Z. Find the opposite of some other face first, using its four neighbours, then strike that pair from X's candidates. Each fixed pair removes candidates elsewhere. This is the same chain of elimination you used in logic grids.

### Method 2: nets and folding

A **net** is a flat pattern of six squares that folds into a cube. Two rules decide most net questions.

- In a straight run of squares, faces separated by exactly one square are opposite.
- A square attached to the side of a run folds over to sit against the run; it is adjacent to the square it touches and to that square's neighbours in the ring.

Worked example. In the visual net, A and F both attach to C, one above and one below. When the ring closes, A becomes the top and F the bottom, so they are opposite.

What it establishes: opposite pairs can be read off a straight run without imagining the fold. Where it stops: in a staircase-shaped net, squares can be two apart along a bend without being opposite. Apply the "skip one" rule only along a straight line.

**Failure condition.** Treating any two squares that are two steps apart as opposite, even around a corner of the net. Trace the straight runs first.

### Method 3: painted cubes by class

Paint every outer face of an n x n x n cube, then cut it into n^3 small cubes.

| Class | Where it sits | Painted faces | Count |
|---|---|---:|---:|
| Corner | the 8 corners | 3 | 8 |
| Edge piece | along the 12 edges, corners excluded | 2 | 12(n - 2) |
| Face piece | inside each of the 6 faces | 1 | 6(n - 2)^2 |
| Core | hidden inside | 0 | (n - 2)^3 |

For n = 4 these are 8, 24, 24 and 8, matching the slice reading in the visual.

**Cuboids.** For a block a x b x c, the same classes apply. Corners: 8. Edge pieces: the block has 4 edges of each length, so 4[(a - 2) + (b - 2) + (c - 2)]. Face pieces: each pair of opposite faces contributes 2(length - 2)(width - 2). Core: (a - 2)(b - 2)(c - 2).

Worked example. A 3 x 3 x 5 block painted on all faces and cut into unit cubes. Corners 8. Edge pieces 4[(1) + (1) + (3)] = 20. Face pieces 2[(1)(1) + (1)(3) + (1)(3)] = 14. Core 1 x 1 x 3 = 3. Total 8 + 20 + 14 + 3 = 45 = 3 x 3 x 5, so the classes cover the block exactly.

What it establishes: four classes count every piece once, and the total is a built-in check. Where it stops: if a dimension is 1 or 2, some classes are empty or overlap in a way the formula does not show. A 2 x 2 x 2 cube has only corners. Check thin blocks by drawing a slice.

**Failure condition.** Using n - 1 or n instead of n - 2 along an edge. Each edge has n small cubes, but the two at its ends are corners, so n - 2 remain.

### Method 4: cuts and partitions

A cut is a flat saw stroke across the whole block. If there are x cuts parallel to one pair of faces, y parallel to the second and z parallel to the third, the block falls into (x + 1)(y + 1)(z + 1) pieces, provided the pieces are not moved between cuts.

- To get n^3 equal cubes, the least number of cuts is 3(n - 1). For 64 small cubes, 3 x 3 = 9 cuts.
- With a fixed number of cuts, the most pieces come from sharing the cuts as evenly as possible. Eight cuts shared 3, 3, 2 give 4 x 4 x 3 = 48 pieces, more than any other split (4, 2, 2 gives only 45).

Pieces that touch no outer face form an inner block. Its size along each direction is the number of pieces in that direction minus 2.

What it establishes: pieces multiply across the three directions. Where it stops: if pieces may be stacked and re-cut, one stroke can cut several pieces, and the count changes completely. Read whether rearranging is allowed.

**Failure condition.** Multiplying the numbers of cuts instead of the numbers of pieces in each direction.

**Cutting into cubes of two sizes.** Sometimes the pieces are not equal: a block is cut into some big cubes and some small cubes. Work in three steps.

1. Fix the size structure from volume. If a big cubes of edge s and b small cubes of edge t fill a block of volume V with no waste, then a x s^3 + b x t^3 = V. When the stem also gives the number of pieces, a + b = N, the two equations fix a and b.
2. Place the big cubes. The volume equation says how many, not where; use the stem's position clue (a corner, a face, a colour) and check that the pieces really fit.
3. Count painted faces piece by piece, by class, using the placement.

Worked example. A wooden cube of edge 6 cm is painted on all faces and then cut, with no wood wasted, into 34 cubes, each of edge 3 cm or 1 cm. Every 3 cm cube has a corner of the original block as one of its own corners. How many of the 34 pieces carry no paint?

1. Size structure. Let a pieces be 3 cm cubes and b be 1 cm cubes. Volume: 27a + b = 216. Count: a + b = 34. Subtract the second from the first: 26a = 182, so a = 7 and b = 27.
2. Placement. A 3 cm cube that shares a corner with the block fills that corner's eighth, a 3 x 3 x 3 octant. Seven big cubes fill seven octants, and the 27 small cubes fill the eighth exactly (27 = 3 x 3 x 3), which confirms the structure.
3. Paint. Each big cube touches three outer faces of the block, so all 7 are painted. The small cubes form a 3 x 3 x 3 corner block whose only painted surfaces are the three outer faces that meet at its corner. A small cube is unpainted when it touches none of those three: 2 x 2 x 2 = 8. The rest of the small cubes: 1 with three painted faces, 6 with two, 12 with one; 1 + 6 + 12 + 8 = 27.

So 8 pieces carry no paint.

What it establishes: with unequal pieces, volume fixes how many of each size, a placement clue fixes where they sit, and only then can painted faces be counted. Where it stops: volume alone does not fix placement. Without the corner clue, the seventh big cube could sit 1 cm or 2 cm along the last 3 x 3 x 6 column instead of in its corner, and the unpainted count falls from 8 to 4; an item whose answer changes with placement must supply the clue. Volume can also rule a split out: a 6 cm cube cannot be cut into a mix of 3 cm and 2 cm cubes, because 27a + 8b = 216 has whole-number solutions only at a = 0 (twenty-seven 2 cm cubes) and a = 8 (eight 3 cm cubes).

**Failure condition: the equal-cube table applied to unequal pieces.** Treating the 6 cm block as 216 unit cubes gives a core of 4 x 4 x 4 = 64 unpainted pieces. Most of that core lies inside big cubes, and every big cube is one piece painted on its outer faces. Count pieces, not unit volumes.

### Method 5: partly painted blocks and patterns

Some items paint only some faces, or paint stripes. The method does not change: classify each small cube by which painted surfaces it touches.

Worked example. A 4 x 4 x 4 cube has paint only on its top and front faces. A small cube can touch the top (the top slice of 16), the front (the front slice of 16), both (the 4 cubes on their shared edge), or neither. Painted on two faces: 4. Painted on one face: 16 + 16 - 2 x 4 = 24. Unpainted: 64 - 4 - 24 = 36. If instead the top and bottom are painted, no cube touches both, and the unpainted cubes are the two middle slices: 32.

What it establishes: inclusion and exclusion from Lesson 12 counts cubes touching more than one painted surface. Where it stops: each new paint pattern needs its own classification, and a pattern on a flat surface (a table top, a wall) is counted by listing placements, not by cube classes.

### Method 6: colouring faces and counting stacked cubes

**Colouring a cube with six different colours.** With 6 different colours, one per face, the number of distinct cubes is 6!/24 = 30, because a cube can be turned into 24 positions and each colouring is counted once per position. The least number of colours needed so that adjacent faces differ is 3, one colour per opposite pair. **Failure condition:** answering 6! = 720, which treats turned copies of the same cube as different. The division by 24 is valid only when all six faces carry different colours: then no turn of the cube (other than leaving it still) gives back the same colouring, so every distinct cube appears exactly 24 times in the 720.

**Colouring a cube when colours repeat.** Once a colour may sit on more than one face, some turns leave a colouring unchanged, and dividing by 24 gives a wrong or even fractional answer. The working method is to sort colourings by shape, not to divide:

1. Fix how many faces carry each colour.
2. For each colour that covers two faces, ask whether those faces are **opposite** or **adjacent**. For a colour that covers three faces, ask whether they **meet at one corner** or run as a **band** (two opposite faces joined by the face between them). These are the only shapes, because any two faces of a cube are either opposite or adjacent.
3. Count one cube for each distinct shape, and check whether a shape and its mirror image can be turned into each other. A cube can be turned but not reflected, so a shape whose mirror image cannot be reached by turning counts twice.

Worked example. Each face of a cube is painted red, blue or green, with every colour on exactly two faces. How many different cubes are possible?

| Colours on opposite pairs | Picture | Cubes |
|---|---|---:|
| all three | red top and bottom, blue front and back, green left and right | 1 |
| exactly one (choose which: 3 ways) | that colour top and bottom; the other two each take two neighbouring side faces of the ring | 3 |
| exactly two | impossible: the last two faces would then be opposite too | 0 |
| none | every colour on two adjacent faces; this shape and its mirror image cannot be turned into each other | 2 |
| sum | | 6 |

A computer check over all 90 ways of painting the labelled faces, grouped under the 24 turns, gives the same 6. Dividing 90 by 24 gives 3.75, which shows why the shortcut fails here.

What it establishes: with repeated colours, count shapes (opposite or adjacent; corner or band) rather than divide. Where it stops: on a solid where every two faces touch, such as a four-faced pyramid with triangular faces, only the number of faces of each colour matters; on a cube the arrangement matters too. **Failure condition:** listing only how many faces carry each colour and forgetting that two faces of one colour can be opposite or adjacent, which undercounts; or dividing by 24, which miscounts.

**Stacked solids.** A staircase of unit cubes, one cube deep, with steps of heights 1, 2, 3 and 4, contains 1 + 2 + 3 + 4 = 10 cubes. A stepped pile with square levels 3 x 3, 2 x 2 and 1 x 1 contains 9 + 4 + 1 = 14. Count column by column or level by level, and include hidden cubes that must be there to hold up the visible ones. **Failure condition:** counting only the cubes whose faces you can see.

### Where the mental cube slips, and what replaces it

The tempting method in cube-view items is to hold the cube in your head and rotate it. Under time pressure the mental cube slips: a left face becomes a right face, and the answer is fixed by accident. The reply is to write the adjacency list from every view, mark four neighbours for each face, and read off the leftover.

The tempting method in painted-block items is to count visible pieces on a sketch. The reply is the four-class table, with the total as a check.

### UPSC application

- **Cube-face items naming two faces, and cube-rotation opposite-face items:** collect adjacencies from all views; use four neighbours or the common-pair rule, and say "not determined" when neither applies.
- **Cardboard assembly from a net:** read straight runs, skip one for opposite faces, and fold side squares to top and bottom.
- **Coloured or painted cubes, interior cube counts and painted cuboid partition counts:** use corner, edge, face and core classes with n - 2 along each edge.
- **Cube partition cuts:** pieces = (x + 1)(y + 1)(z + 1), and even sharing gives the most pieces; when the pieces come in two sizes, fix the counts by volume, place the big cubes by the stem's clue, then classify every piece by its painted faces.
- **Cube face-colouring counts:** with six different colours divide by the 24 positions; when colours repeat, sort by shape (opposite or adjacent pairs, corner or band triples) and count each shape once.
- **Solid-shape counting:** count by column or level and include supporting cubes.
- **Painted-region pattern counts:** classify each piece or placement by the painted surfaces it touches, and list placements on a flat surface one by one.

### Revision points

- Faces in one view are adjacent; a face has four neighbours and one opposite.
- Never fix an opposite pair from a single view.
- Two views showing a common pair of faces make their third faces opposite.
- In a straight run of a net, faces one square apart are opposite.
- Painted n-cube: 8 corners, 12(n - 2) edge pieces, 6(n - 2)^2 face pieces, (n - 2)^3 core.
- For a cuboid, edge pieces are 4[(a - 2) + (b - 2) + (c - 2)].
- The four classes must add to the total number of pieces.
- x, y, z cuts give (x + 1)(y + 1)(z + 1) pieces when pieces are not moved.
- n^3 equal cubes need at least 3(n - 1) cuts.
- Two sizes of cube: volume fixes how many of each; a placement clue fixes where; then count pieces, not unit volumes.
- Unpainted pieces form an inner block, each side reduced by 2 pieces.
- Six different colours on a cube give 30 distinct cubes, not 720.
- With repeated colours, do not divide by 24; sort by opposite or adjacent pairs and corner or band triples.
- Stacked solids include the hidden cubes that support the visible ones.

### Practice

**MCQ 35**

A wooden block measuring 4 cm by 5 cm by 6 cm is painted on all its outer faces and then cut into cubes of side 1 cm. How many of the small cubes have paint on exactly two faces?

- A. 52, the cubes inside the faces but off every edge
- B. 24, the cubes hidden in the unpainted core
- C. 36, the edge cubes once the eight corner cubes are taken out
- D. 60, edge cubes counted with each corner repeated along three edges

**MCQ 35 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Counts the cubes with exactly one painted face: 2[(2)(3) + (3)(4) + (2)(4)] = 2(6 + 12 + 8) = 52. Those cubes sit inside the faces, not along the edges.
- **B — Incorrect:** Counts the unpainted core, (4 - 2)(5 - 2)(6 - 2) = 2 x 3 x 4 = 24. Those cubes have no paint at all.
- **C — Correct:** Cubes with two painted faces lie along the edges, excluding the corners. The block has 4 edges of each length 4, 5 and 6, and each edge loses its two end cubes: 4[(4 - 2) + (5 - 2) + (6 - 2)] = 4 x 9 = 36. Check: 8 corners + 36 + 52 + 24 = 120 = 4 x 5 x 6.
- **D — Incorrect:** Counts every cube along each edge, 4(4 + 5 + 6) = 60, which is also the total edge length in centimetres. Each corner cube then appears on three edges, and corners carry three painted faces, not two.

**MCQ 36**

A sheet of six squares is folded along the lines between them to make a cube. The squares sit as shown.

```text
+---+---+
| P | Q |
+---+---+---+---+
    | R | S | T |
    +---+---+---+
            | U |
            +---+
```

Which statement about the folded cube is correct?

- A. P is opposite R, two squares away around the bend
- B. S is opposite U, the one face it does not touch in the net
- C. P is opposite T, the face lying farthest from it in the net
- D. Q is opposite U, the face that folds over from T's side

**MCQ 36 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Applies the skip-one rule around a corner of the net. P, Q and R do not lie in one straight run, so P and R are not opposite; P and R both touch Q and end up adjacent.
- **B — Incorrect:** Treats "not touching in the net" as "opposite". U is attached to the side of T, so it folds against the run R, S, T and touches S as well as T.
- **C — Incorrect:** Judges by distance in the drawing. P and T are far apart on paper, but folding brings them together; the skip-one rule only works along a straight run.
- **D — Correct:** R, S, T is a straight run, so R is opposite T. Both squares attached to the side of a run fold against it: U folds over from T's side and touches S, and Q folds over from R's side and touches S too. So S is opposite neither U nor Q, and its opposite must be P. That leaves Q opposite U. A folding check gives the pairs P-S, Q-U and R-T.

**MCQ 37**

A solid cuboid is painted on all its outer faces. It is then cut into equal pieces by 2 cuts parallel to one pair of faces, 3 cuts parallel to a second pair and 4 cuts parallel to the third pair, without moving any piece. How many pieces have no painted face?

- A. 6, the inner block after one skin is peeled from each face
- B. 24, the product of the cut numbers 2, 3 and 4
- C. 54, the pieces touching the painted outer surface of the cuboid
- D. 60, every piece that the nine cuts make, painted or not

**MCQ 37 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** The cuts make 3, 4 and 5 pieces along the three directions. Removing one outer piece from each end in every direction gives (3 - 2)(4 - 2)(5 - 2) = 1 x 2 x 3 = 6 unpainted pieces.
- **B — Incorrect:** Multiplies the numbers of cuts, 2 x 3 x 4 = 24. Pieces depend on the number of pieces in each direction, which is one more than the cuts.
- **C — Incorrect:** Reports the painted pieces, 60 - 6 = 54. The question asks for pieces with no paint.
- **D — Incorrect:** Reports the total number of pieces, 3 x 4 x 5 = 60, without separating painted from unpainted ones.

---

## Lesson 16 - Data interpretation I: levels, changes and shares

Progress: Lesson 16 of 18 | Stage: Core | Subtopic: Data interpretation I: levels, changes and shares

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A table of numbers looks harmless. The arithmetic is rarely harder than division. Yet data items are missed constantly, and almost never because of a division error. They are missed because one row of a table holds five different numbers that all look like "the answer": the level, the change, the percentage change, the share and the change in share. The options are built from exactly those five. This lesson teaches you to name the quantity before you touch it, and to name the base of every percentage. It uses the percentage arithmetic from Lesson 12 and the careful counting habits from Lesson 10.

### Visual: one row, five different numbers

```text
WATER CONNECTIONS (thousand)

Year   Ward K   All wards   K's share
2023     60        300        20%
2024     72        320        22.5%

LABEL STRIP for Ward K, 2023 -> 2024
+-------------------+---------------------------+--------------+
| quantity          | how it is computed        | value        |
+-------------------+---------------------------+--------------+
| level (2024)      | read the cell             | 72 thousand  |
| change            | 72 - 60                   | +12 thousand |
| percent change    | 12 / 60  (base = 2023)    | +20%         |
| share (2024)      | 72 / 320                  | 22.5%        |
| change in share   | 22.5 - 20                 | +2.5 points  |
| relative change   | 2.5 / 20  (base = 20)     | +12.5%       |
|   in share        |                           |              |
+-------------------+---------------------------+--------------+
```

Read the strip from top to bottom. Six correct numbers come out of two rows, and each answers a different question. "How many connections?" is a level. "By how much did they grow?" is a change. "By what percent?" divides the change by the starting level. "What share?" divides by the total. A move in a share is measured in **percentage points**, which means a simple difference between two percentages. A **relative change** in a share divides that difference by the old share. If an option says "+2.5%", it has used the points figure as if it were a percent change, and that is wrong in this table.

### The plain idea

Every percentage is a fraction with a hidden denominator. "20% more" means 20% of something. Before you calculate, say out loud what that something is. Most errors in data reading are a wrong denominator: the right numbers divided by the wrong base. The other errors come from answering a nearby question, such as giving a total when a change was asked.

### Rule 1: answer the exact quantity asked

Before computing, underline the quantity in the stem and write its label: level, change, percent change, share, points, relative change, rate, ratio or average.

Worked example. Read this table.

| Month | Product X | Product Y |
|---|---:|---:|
| Jan | 200 | 150 |
| Feb | 250 | 180 |
| Mar | 300 | 120 |

- Total X = 200 + 250 + 300 = 750. Total Y = 150 + 180 + 120 = 450.
- Percent rise in X from January to March = (300 - 200)/200 = 50%.
- The bar for X rises by 100 units over the same period. A rise of 100 units is a change, not a percent.

What it establishes: one small table answers several different questions, and the stem picks one. Where it stops: it does not tell you which base to use when the stem is vague; for that, see Rule 2.

**Failure condition.** Computing a total when a change or a percent was asked, or reading the height difference of two bars as a percent. A bar that grows from 200 to 300 has grown by 100 units and by 50%; the two numbers answer different questions.

### Rule 2: name the base of every percentage

The base is the quantity you divide by. For a percent change, the base is the starting value. For a share, the base is the total. For "A is what percent more than B", the base is B.

Worked example. Revenue per thousand units is a rate. A firm makes 40 thousand units and earns ₹80 lakh in one quarter, then makes 50 thousand units and earns ₹90 lakh in the next. Output rose by 10 thousand units (not 10%; the percent rise is 25%). Revenue per thousand units fell from 80/40 = 2 lakh to 90/50 = 1.8 lakh. A product that took 25% of the first quarter's revenue and 30% of the second's earned 30% of 90 = ₹27 lakh in the second quarter. Its share rose by 5 percentage points, which is 5/25 = 20% in relative terms.

What it establishes: output, revenue and revenue per unit can move in different directions, and each needs its own base. Where it stops: a rate is only meaningful if both of its parts come from the same period and unit.

**Failure condition.** Using the later value as the base for a percent change. A slice of a pie that grows from 20% to 25% has risen by 5 percentage points and by 5/20 = 25% relatively. Dividing by 25 instead of 20 gives 20%, which is the wrong base.

### Rule 3: keep percentage points apart from percent change

When the quantity is itself a percentage (a share, a rate, a literacy figure), there are two ways to describe a change. **Percentage points** subtract: 20% to 25% is +5 points. **Percent change** divides: 5/20 = +25%. The paper often places both numbers among the options. Neither is wrong in itself; only one answers the question asked.

**Failure condition.** Writing "+5%" for a move from 20% to 25%. That phrase claims a relative change of 5%, which would be a move from 20% to 21%.

### Rule 4: rates per unit before comparisons

Raw counts are misleading when the groups differ in size. Convert to a rate per common unit first.

Worked example. In one district, 30 deaths occurred among 12,000 workers in Group A and 45 among 25,000 workers in Group B. Group B has more deaths, but its rate is lower: Group A has 30/12 = 2.5 deaths per thousand, Group B has 45/25 = 1.8 per thousand.

What it establishes: "more cases" and "a higher rate" are different claims. Where it stops: a rate shows association, not cause. A table cannot say why Group A has the higher rate.

**Failure condition.** Comparing counts across groups of different size, or comparing rates computed per different units (per hundred against per thousand).

**Overs as a unit.** In cricket tables, 30.4 overs means 30 overs and 4 balls, which is 30 + 4/6 overs, because an over has 6 balls. A team scoring 184 runs in 30.4 overs has a run rate of 184 ÷ (30 + 4/6) = 6.0 runs per over. Dividing by 30.4 as a decimal gives about 6.05, which is a unit error, not a rounding difference.

### Rule 5: cross-tables and the two margins

A **cross-table** splits a total two ways. Every inside cell can be divided by two different totals: its row total or its column total. The stem's wording decides which.

Students of a college by usual way of travel and year of study:

| Travel mode | First year | Final year | Total |
|---|---:|---:|---:|
| Bus | 120 | 80 | 200 |
| Cycle | 45 | 75 | 120 |
| Walk | 35 | 45 | 80 |
| Total | 200 | 200 | 400 |

- "What percent of final-year students cycle?" The group named after "of" is the base: all final-year students, the column total. 75/200 = 37.5%.
- "What percent of cyclists are in the final year?" Now the base is all cyclists, the row total. 75/120 = 62.5%. The same cell, 75, gives two different answers because the base changed.
- "If 25 first-year bus riders switched to cycling, what share of first-year students would cycle?" Move the 25 inside the first-year column: cycle becomes 70, the column total stays 200, so 70/200 = 35%. The row totals change (Bus 175, Cycle 145) but the column base does not.
- Check totals both ways: 120 + 45 + 35 = 200 down the first-year column, and 200 + 120 + 80 = 400 down the totals column. A cross-table whose rows and columns do not reach the same grand total has been misread.

What it establishes: an inside cell has no single percentage; it has one per margin. Where it stops: if the stem gives only percentages and no totals, you can compare shares within the same base but cannot turn them into counts.

**Failure condition.** Dividing by the wrong margin (the row total when the stem names the column group), or answering a share question with the largest count. Bus carries the most final-year students (80), but Cycle has the largest final-year share of its own riders.

### Rule 6: rises, growth rates and running totals

A single series can answer several different "growth" questions. A dairy cooperative collected milk (thousand litres) as follows:

| Month | Jan | Feb | Mar | Apr | May |
|---|---:|---:|---:|---:|---:|
| Collection | 40 | 50 | 60 | 72 | 80 |
| Rise on previous month | | 10 | 10 | 12 | 8 |
| Percent rise | | 25% | 20% | 20% | about 11.1% |
| Running total | 40 | 90 | 150 | 222 | 302 |

- Largest absolute rise: March to April (12 thousand litres).
- Largest percent rise: January to February (25%), even though its absolute rise (10) is smaller than April's.
- First month in which the running total passes 200: April (150 after March, 222 after April).
- Equal absolute rises (10 and 10 in February and March) are falling percent rises (25% then 20%), because the base keeps growing.

What it establishes: "rose most", "grew fastest" and "passed a target" are three different questions, and each needs its own row. Where it stops: a five-month table cannot support a forecast for June, and a running total cannot be read from the monthly row without adding.

**Failure condition.** Answering a percent-growth question from the absolute rises, or reading the running total off the monthly figure. Calling growth "steady" from equal absolute rises is the same slip.

### Rule 7: what a table can and cannot support

Some items ask which inference is valid or which assumption a table supports. A valid inference uses only the numbers given and the operations you can perform on them. An unsupported one adds a cause, a forecast, an unstated population or a comparison with data not shown.

Worked example. A table shows that District P has higher average income and higher literacy than District Q. Valid: P's average income exceeds Q's. Not valid from the table alone: higher literacy causes higher income, or every person in P earns more than every person in Q. An average says nothing about each individual.

**Failure condition.** Accepting a claim because it sounds reasonable, when the table does not contain the numbers needed to test it.

### Rule 8: amounts tied together by stated relations

Some items give no table at all, only sentences linking amounts: "A gets ₹200 less than B", "C gets one and a half times what A gets". The method is to write every amount in terms of one unknown. When one amount can be reached through two different sentences, set the two expressions equal. Then compute exactly what the stem asks: a total, a ratio, a difference or a single amount.

Worked example. Three volunteers, Ravi, Meera and Sana, collected money for a flood-relief fund. Meera collected one and a half times what Ravi collected. Sana collected ₹300 less than Meera, and Sana also collected ₹600 more than Ravi. How much did the three collect together, and what is the ratio Ravi : Meera : Sana?

1. Let Ravi = x. Then Meera = 1.5x.
2. Sana is reached by two sentences: from Meera, Sana = 1.5x - 300; from Ravi, Sana = x + 600. Set them equal: 1.5x - 300 = x + 600, so 0.5x = 900 and x = 1,800.
3. Ravi ₹1,800, Meera ₹2,700, Sana ₹2,400. Check both sentences: 2,700 - 300 = 2,400 and 1,800 + 600 = 2,400.
4. Together: 1,800 + 2,700 + 2,400 = ₹6,900. Ratio: divide each by 300 to get 6 : 9 : 8.

No total was given; the loop of three sentences around three people is what fixed x.

Two habits make these items safe:

- **Write the sentence as an equation in the order it is read.** "Sana collected ₹300 less than Meera" is S = M - 300. Reversed to M = S - 300, the same working gives Sana = 1.5x + 300 = x + 600, so x = 600 and a combined ₹2,700: every later figure changes.
- **Count what fixes the unknown before computing.** A loop of sentences (two paths to one amount) or a stated total fixes x. If the sentences form only a chain, with no loop and no total, x stays unknown: a total or a ratio cannot be found, and a comparison is safe only if it holds for every allowed value of x. With different multipliers, such as 1.5x against x + 600, the comparison usually depends on x, so it cannot be made until x is known.

What it establishes: sentences of relations become one-unknown expressions, and a loop or a total turns them into an equation. Where it stops: if the equation gives a negative or impossible amount, the sentences are inconsistent; say so rather than force an answer.

**Failure condition.** Adding the numbers in the sentences (300 + 600 = 900) and treating 900 as somebody's amount. Here 900 is half of Ravi's collection, the gap between the two paths to Sana; it is nobody's total. A second failure is turning "less than" into the wrong sign, as in the reversed equation above.

### Weighted-score tables: the reading step

Some tables give scores with weights. Before computing anything, identify which columns are scores, which row or line gives the weights, and whether the weights add to 1, to 100% or to some other total. A weighted score is each score times its weight, added up; if the weights do not add to 1, divide the result by their sum.

### Multi-step reading: different bases do not cancel (Advanced)

This revenue table (₹ crore) shows three traps in one place.

| Year | Product X | All products | X's share |
|---|---:|---:|---:|
| 2022 | 400 | 1000 | 40% |
| 2023 | 500 | 1250 | 40% |
| 2024 | 450 | 900 | 50% |

- Growth of X from 2022 to 2023: (500 - 400)/400 = +25%.
- Change of X from 2023 to 2024: (450 - 500)/500 = -10%.
- **Trap 1, different bases.** A rise of 25% followed by a fall of 10% does not return X to 400. 400 x 1.25 x 0.90 = 450, which matches the table. The two percentages use different bases, so they cannot be added or cancelled.
- **Trap 2, level against share.** From 2023 to 2024 X's revenue fell (500 to 450), while X's share rose (40% to 50%), because the total fell faster. "X did worse" and "X gained share" are both true.
- **Trap 3, points against percent.** The share move is +10 percentage points and +25% in relative terms (10/40). Expect both numbers among the options.

The decision rule: before any arithmetic, label the quantity as level, share, change in level, change in share in points, or relative change. Five different numbers live in one row.

**Failure condition (Advanced).** Reporting a percentage-point move as a percent change, or adding successive percentages as if they shared one base.

### The nearest number is rarely the asked number

The tempting method is to compute the first number that the eye connects with the stem. "Health spending" catches the eye, the share column is nearest, and its difference becomes the answer. The reply is the label strip: write the label of the asked quantity, then write the formula with its base, then compute. The strip takes ten seconds and catches nearly every trap in this family.

### UPSC application

- **Smallest money-share and other linked-amount items:** write every amount in one unknown, check what (a loop, a total or nothing) fixes that unknown, and answer only what the stem asks.
- **Share-of-total items:** divide by the total, then compare shares, not counts.
- **Cross-table families (professors by subject, sex and age band, totals, male-female ratio):** name the margin that is the base, check totals both ways, and compute ratios or shares rather than picking the largest count.
- **Seller-profit graph families (equal profit, profit difference, profit increase, trend):** read each value off the scale with its unit, sign the difference in the order the stem states, and separate absolute change from percent change.
- **Population-income and table-inference or assumption-validity items:** accept only what the numbers can show; reject causes, forecasts and claims about individuals from averages.
- **Mortality and accident-rate comparisons:** convert counts to rates per common unit.
- **Bar-chart comparisons, value calculations and ratio readings:** read the scale, then name level, change or ratio.
- **Table rate and run-rate comparisons:** use the true unit, including overs counted in sixths.
- **Weighted-score data tables:** identify scores and weights before computing, and multiply each score by its own weight.

### Revision points

- Name the quantity before computing: level, change, percent change, share, points or relative change.
- Every percentage has a base; percent change uses the starting value.
- Share uses the total as its base.
- Percentage points subtract; percent change divides.
- A move from 20% to 25% is +5 points and +25% relative.
- Different bases do not cancel: +25% then -10% is not +15%.
- A level can fall while a share rises, if the total falls faster.
- Compare groups of different sizes by rates, not counts.
- 30.4 overs means 30 + 4/6 overs.
- In a cross-table, a cell has one share per margin; the group named after "of" is the base.
- Check row and column totals against the grand total.
- The largest count does not imply the largest ratio.
- Equal absolute rises mean falling percent rises; "rose most" and "grew fastest" are different questions.
- Linked amounts: write each in one unknown; two paths to the same amount give an equation; a total or a ratio needs the unknown fixed.
- A table supports calculations on its numbers, not causes or forecasts.

### Practice

**MCQ 38**

A district spent 16% of a ₹250 crore budget on health in Year 1. In Year 2 the budget was ₹220 crore and health received 20% of it. By what percentage did the amount spent on health change from Year 1 to Year 2?

- A. A 4% rise, taken straight from the share column
- B. A 10% rise in rupees spent on healthcare
- C. A 25% rise, the relative change in the share
- D. A 12% fall, in line with the entire budget

**MCQ 38 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Takes the 4-point rise in the share (16% to 20%) and reports it as a percent change in spending. Points describe the share, not the amount of money.
- **B — Correct:** Health spending was 16% of 250 = ₹40 crore in Year 1 and 20% of 220 = ₹44 crore in Year 2. The change is (44 - 40)/40 = 10%, a rise.
- **C — Incorrect:** Computes the relative change in the share, 4/16 = 25%. That would be the change in spending only if the total budget had stayed the same, and it fell.
- **D — Incorrect:** Reports the change in the total budget, (220 - 250)/250 = -12%. The question asks about health spending, which rose because its share rose faster than the budget fell.

**MCQ 39**

Region X has a population of 2.5 lakh and reported 75 road accidents in a year. Region Y has a population of 4 lakh and reported 100 road accidents in the same year. Which statement correctly compares their accident rates per lakh of population?

- A. Y's rate is higher, by 33.3% of X's rate
- B. X's rate is higher, by 16.7% of Y's rate
- C. X's rate is higher, by 20% of Y's
- D. X's rate leads, by 5% of Y's

**MCQ 39 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Compares raw counts: 100 accidents against 75 is 33.3% more. The regions differ in population, so counts must first be turned into rates.
- **B — Incorrect:** Divides the gap of 5 by X's rate of 30, giving 16.7%, but states it against Y's rate. Measured against Y's rate the gap is 20%; the wrong base has been used.
- **C — Correct:** X's rate is 75/2.5 = 30 accidents per lakh and Y's is 100/4 = 25 per lakh. X exceeds Y by 5 per lakh, and 5/25 = 20% of Y's rate.
- **D — Incorrect:** Takes the gap of 5 accidents per lakh and reports it as 5%. The gap is an absolute difference in rates; as a percent of Y's rate it is 20%.

---

## Lesson 17 - Data interpretation II: pies, dual axes and weighted scores

Progress: Lesson 17 of 18 | Stage: Core | Subtopic: Data interpretation II: pies, dual axes and weighted scores

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tables give you numbers. Graphs give you shapes, and shapes persuade. A steep line looks like fast growth, a big slice looks like a big amount, and a bar that towers over a line looks larger than it. Each of those impressions can be false, because the shape depends on the axis, the unit and the total behind it. Lesson 16 taught you to name the quantity and its base. This lesson applies that habit to pictures: pie charts, two-axis charts, line graphs and weighted scores.

### Visual: a two-axis chart and a pie conversion table

```text
DUAL-AXIS CHART (one chart, two units)

 output (thousand units)                      revenue (₹ lakh)
 LEFT AXIS: bars                              RIGHT AXIS: line
  80 |                                             | 160
  75 |                 ###          ___o (135)     | 150
  60 |  ###  o (120)___###____----               | 120
  40 |  ###            ###                         |  80
  20 |  ###            ###                         |  40
   0 +--------------------------------------------+   0
        Year 1         Year 2
        60 thousand    75 thousand   (bars, left)
        ₹120 lakh      ₹135 lakh     (line, right)

  revenue per thousand units:  120/60 = 2.0 lakh  ->  135/75 = 1.8 lakh

PIE TO VALUE (total = ₹2,400 crore)

  slice given as      convert to share        value
  63 degrees          63/360 = 17.5%          17.5% of 2,400 = ₹420 crore
  35%                 35% (angle 126 deg)     35% of 2,400 = ₹840 crore
  "one quarter"       25% (angle 90 deg)      25% of 2,400 = ₹600 crore
```

Look at the chart's two axes before anything else. The bars are read on the left scale in thousand units; the line is read on the right scale in lakh rupees. Where the line crosses a bar means nothing, because the two are measured in different units on different scales. The only valid way to combine them is to read each on its own axis and then compute, as in the last line: revenue rose from 120 to 135, but revenue per thousand units fell from 2.0 to 1.8.

The pie table turns every way a slice can be labelled into a share, and every share into a value through the total. An angle is converted by dividing by 360, not 100. A share becomes money only after it is multiplied by the total, and the total must be the one for that pie.

### The plain idea

A graph is a table that has been drawn. Every point, bar or slice stands for a number, and the number depends on the scale. Before you trust a shape, turn it back into numbers: read the title, the unit and the scale of each axis, then compute exactly the quantity the stem asks for.

### Method 1: read title, unit, scale and both axes first

1. Title: what is measured, where and when.
2. Unit: thousands, lakh, crore, percent, index points.
3. Scale: where each axis starts. An axis that starts at 50 instead of 0 makes small changes look large.
4. Second axis: which series belongs to which side.

Worked example. A graph shows output of 60 thousand units and revenue of ₹120 lakh in Year 1, and 75 thousand units and ₹135 lakh in Year 2. Revenue per thousand units is 120/60 = 2 lakh in Year 1 and 135/75 = 1.8 lakh in Year 2. Revenue rose while the rate fell.

What it establishes: combining two series requires each to be read on its own axis. Where it stops: the chart cannot tell you why the rate fell; that would need prices or product mix.

**Failure condition.** Comparing the height of a bar with the height of a line on a two-axis chart, or reading a series against the wrong axis. Heights on different scales cannot be compared directly.

### Method 2: a share becomes a value only through its own total

**Pie angles.** A full pie is 360 degrees. A slice of angle a degrees is a/360 of the total. Going the other way, a share of p% is drawn with an angle of 3.6p degrees.

Worked example. In a ₹2,400 crore budget, a slice of 63 degrees is 17.5%, so ₹420 crore. A slice labelled 35% has an angle of 126 degrees.

**Two pies.** When two pies have different totals, a slice can shrink in share while growing in value. In Year 1 a sector has 30% of a ₹2,000 crore total, which is ₹600 crore. In Year 2 it has 25% of ₹2,600 crore, which is ₹650 crore. The share fell by 5 percentage points; the money rose by ₹50 crore.

**Points and percent again.** A slice that rises from 20% to 25% has moved by +5 percentage points and by +25% relatively (5/20). The pie picture shows the points; the relative change has to be computed.

What it establishes: shares and values are different quantities, and comparing slices across pies needs both totals. Where it stops: if a pie has no stated total, it can answer share questions only.

**Failure condition.** Treating an angle as a percent (dividing by 100), or comparing slices across pies as if the totals were equal.

### Method 3: line graphs, slopes and steps

**Slope and level.** On a line graph, the height is the level and the steepness between two points is the change per period. The steepest segment shows the largest absolute change, which is not always the largest percent change. Steepness can be compared only between segments drawn on the same axis scale and over equal time steps. Suppose a price graph has its vertical axis marked every ₹5 per kg and its horizontal axis marked every year, with the same spacing all the way along. A climb from ₹20 to ₹30 per kg in one year rises by ₹10, which is two gridlines up for one across, and by 50%. A later one-year climb from ₹60 to ₹75 rises by ₹15, three gridlines up for one across, so on this graph it is the steeper segment, yet it is only a 25% rise. If the two segments covered different numbers of years, compare the change per year, not the drawn steepness.

**Cumulative progress lines.** If a graph shows cumulative work done (total so far), the vertical gap between two lines is the difference in totals, and the slope of each line is the work rate. One project can be behind in total while working faster, and the lines will then be converging.

**Steps in rates.** Interest or policy rates are often drawn as steps. A move from 6.50% to 6.25% is a cut of 0.25 percentage points, which is called 25 **basis points** (one basis point is one hundredth of a percentage point). It is not a 0.25% cut in relative terms; relatively, it is about 3.8%.

**Shares inside groups.** An age-group graph may show the percentage of population aged 0 to 14 falling over time. That does not mean the number of children fell. If the total population grew, the number can still rise. Tax-revenue graphs show the same trap: tax as a share of national income can fall while the rupee amount rises.

What these establish: slope, level, share and count are separate claims, and the graph supports only the ones it actually draws. Where they stop: a line between two years shows the endpoints, not what happened in between, unless the points in between are plotted.

**Failure condition.** Reading the steepest segment as the largest percent rise, or reading a falling share as a falling count.

### Method 4: break-even and target profit on a graph

A **break-even point** is where revenue equals cost, so profit is zero. On a graph it is where the revenue line crosses the cost line. Below that output the firm loses money; above it, the firm earns.

Worked example. A workshop has a fixed cost of ₹20,000 and spends ₹30 on each unit; it sells each unit for ₹55. Cost is 20,000 + 30q and revenue is 55q for q units. The question asks for the output at which profit first reaches ₹5,000. Profit is revenue minus cost, so 55q - (20,000 + 30q) = 25q - 20,000. Setting 25q - 20,000 = 5,000 gives 25q = 25,000, so q = 1,000 units. Check: revenue is 55,000 and cost is 50,000, a profit of 5,000.

What it establishes: a target profit moves the reading from the crossing to a vertical gap between the two lines, measured at the chosen output. Where it stops: if the selling price or the cost per unit changes with volume, the lines are not straight, and the crossing must be read from the plotted curve.

**Failure condition.** Reading the target profit as the revenue line's height at that output. Profit is the vertical gap between the revenue line and the total-cost line, not the revenue line alone, and the fixed cost is only part of the total cost.

### Method 5: weighted scores, by unit and weight

A **weighted score** multiplies each component by its weight before adding. If the weights add to 1 (or 100%), the result is already an average. If they add to some other number, divide the weighted total by the sum of the weights.

Worked example. Weights are 50% for a written paper, 30% for an interview and 20% for a field test. Candidate K scores 60, 90 and 72. Candidate L scores 78, 62 and 70.

| Candidate | Written x 0.5 | Interview x 0.3 | Field x 0.2 | Weighted score | Simple average |
|---|---:|---:|---:|---:|---:|
| K | 30 | 27 | 14.4 | 71.4 | 74 |
| L | 39 | 18.6 | 14 | 71.6 | 70 |

The simple average favours K by 4 marks; the weighted score favours L by 0.2. The written paper carries half the weight, and L is much stronger there.

Weights given as 3, 2 and 1 add to 6. A candidate with 70, 85 and 60 has a weighted total of 210 + 170 + 60 = 440, and a weighted average of 440/6 ≈ 73.3.

What it establishes: the ranking can flip when weights are applied. Where it stops: if the components are on different scales (one out of 50, another out of 200), convert each to the same scale before weighting.

**Failure condition.** Averaging without weights, applying weights to the wrong components, or forgetting to divide by the sum of the weights when they do not add to 1.

### The decision rule for multi-step reading (Advanced)

Before any arithmetic on a graph or a table, label the quantity as one of these: level, share, change in level, change in share in points, relative change, rate per unit, or weighted score. Write the formula with its base. Then read each number from the right axis or slice. Five or six different numbers can be produced from one chart; this rule picks the one the stem wants.

**Failure condition (Advanced).** Doing the arithmetic first and deciding afterwards which label it fits. The arithmetic will always produce some number, and one of the options will match it.

### Trusting the picture, and the habit that corrects it

The tempting method is to trust the picture: the biggest slice, the tallest bar or the steepest line is taken to be the answer. Pictures are drawn to scale only within one axis or one pie. The reply is to convert every shape back into a number with its unit and base before comparing. A second tempting method is to combine two series from a two-axis chart by their heights. The reply is to read each on its own axis and divide or subtract the numbers, never the heights.

### UPSC application

- **Earnings graphs and commodity-price graphs:** separate level from change, and absolute change from percent change.
- **Progress-graph comparisons:** read the gap as the difference in totals and the slope as the rate.
- **Population graph inferences and population age-group graphs:** do not turn a falling share into a falling count.
- **Graph statement validity:** accept only claims the plotted numbers support.
- **Dual-scale graph comparisons:** read each series on its own axis and compute a rate where asked.
- **Break-even readings:** find where revenue meets total cost.
- **Policy-rate and tax-revenue graph inferences:** use percentage points and basis points for rates, and keep shares apart from amounts.
- **Pie-chart sector angles and pie-chart percentages:** angle = 3.6 x percent, value = share x total.

### Revision points

- Read title, unit, scale and both axes before computing.
- On a two-axis chart, never compare a bar's height with a line's height.
- Combine two series by reading numbers, then dividing or subtracting.
- Pie angle a degrees = a/360 of the total; p% = 3.6p degrees.
- A share becomes a value only through its own pie's total.
- A slice can lose share and gain value when the total grows.
- On one scale with equal time steps, the steepest segment = largest absolute change, not necessarily largest percent change.
- 25 basis points = 0.25 percentage points.
- A falling share of a group can hide a rising count.
- Break-even is where revenue equals total cost, fixed plus variable.
- Weighted score: multiply each component by its weight, add, and divide by the sum of weights if it is not 1.
- Weights can reverse a ranking based on simple averages.
- Label the quantity before computing; arithmetic first invites a matching distractor.

### Practice

**MCQ 40**

A pie chart shows a state's budget of ₹4,800 crore. The education sector is drawn with a central angle of 72 degrees, and the health sector carries the label 15%. How much more is budgeted for education than for health?

- A. ₹2,736 crore, reading the 72-degree angle as if 72%
- B. ₹864 crore, taking the 18-degree gap out of 100
- C. ₹960 crore, the education allocation by itself
- D. ₹240 crore, the 5-percentage-point gap applied

**MCQ 40 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Treats the angle as a percent: 72% of 4,800 = 3,456, minus health's 720, gives 2,736. An angle must be divided by 360, not 100.
- **B — Incorrect:** Converts health correctly to 54 degrees and finds the 18-degree gap, but then divides by 100: 18/100 x 4,800 = 864. Degrees are parts of 360.
- **C — Incorrect:** Computes education's amount, 72/360 x 4,800 = 960, and stops. The question asks for the difference between education and health.
- **D — Correct:** Education is 72/360 = 20% of the budget, ₹960 crore. Health is 15%, ₹720 crore. The difference is ₹240 crore, which is the 5-percentage-point gap applied to the ₹4,800 crore budget.

**MCQ 41**

A two-axis chart shows the number of bus passengers as bars on the left axis (lakh) and the average fare paid per passenger as a line on the right axis (₹). In Year 1 there were 40 lakh passengers at an average fare of ₹50. In Year 2 there were 50 lakh passengers at an average fare of ₹44. By what percentage did total fare revenue change from Year 1 to Year 2?

- A. A 10% rise, multiplying passengers by the average fare
- B. A 25% rise, read from the passenger bars considered alone
- C. A 12% drop, read from the fare line
- D. A 13% rise, adding the two percent changes

**MCQ 41 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Revenue is passengers times average fare: 40 lakh x ₹50 = ₹2,000 lakh in Year 1 and 50 lakh x ₹44 = ₹2,200 lakh in Year 2. The change is (2,200 - 2,000)/2,000 = +10%.
- **B — Incorrect:** Reads only the passenger bars, (50 - 40)/40 = +25%. That is the change in passengers, not in revenue.
- **C — Incorrect:** Reads only the fare line, (44 - 50)/50 = -12%. That is the change in the average fare, not in revenue.
- **D — Incorrect:** Adds +25% and -12% to get +13%. Percent changes on different bases do not add; combined, they multiply: 1.25 x 0.88 = 1.10, a 10% rise.

---

## Lesson 18 - Decision scenarios and the decision procedure

Progress: Lesson 18 of 18 | Stage: Core | Subtopic: Decision scenarios and the decision procedure

━━━ PRE-TEACH CHECKLIST ━━━━━━━━━━━━━━━━━━
Book context: not available
CA search: not applicable (aptitude paper)
CA found: not applicable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A scenario item describes a situation, often in an office or a public setting, and offers four courses of action. All four sound like something a real person might do. The learner's problem is that the options are not wrong in the way an arithmetic option is wrong; each has some appeal. What separates them is a procedure: sort what is known from what is wanted, list what rules out an action, and then pick the action that still stands and best serves the purpose. This is the same discipline you used for statements in Lesson 2 and for logic grids in Lesson 9: let the stated constraints eliminate options, and assume nothing that is not given.

### Visual: the four-box procedure

```text
+-------------------------+       +-------------------------+
| 1. FACTS                |       | 2. CONSTRAINTS          |
| what the stem states    | ----> | rules, laws, duties,    |
| (no guesses added)      |       | deadlines, resources    |
+-------------------------+       +-------------------------+
            |                                 |
            v                                 v
+-------------------------+       +-------------------------+
| 3. OBJECTIVE            |       | 4. FEASIBLE OPTIONS     |
| the purpose the actor   | ----> | options that break no   |
| is meant to serve       |       | constraint; choose the  |
|                         |       | one that best meets the |
|                         |       | objective with the      |
|                         |       | fewest added guesses    |
+-------------------------+       +-------------------------+

ELIMINATION SCREEN applied in box 4
  reject: illegal | coercive | deceptive or concealing | discriminatory
          disproportionate | abdicating (doing nothing, passing the buck)
  prefer: lawful | fair | clear | proportionate | logged | followed up
```

Read the boxes in order. Box 1 holds only what the stem says, which protects you from inventing facts that make a favourite option look better. Box 2 holds the rules that bind the actor: a law, a contract term, a deadline, a budget, a duty of the post. Box 3 states the purpose: a safe person, a fair allotment, a working service, a fair examination. Box 4 is where options are tested. An option that breaks a constraint is out, however attractive. Among the survivors, choose the one that serves the objective and needs the fewest assumptions not given in the stem.

The screen at the bottom is a fast filter. It is not a substitute for the boxes; it catches the options that fail on legality or fairness before you spend time weighing them.

### The plain idea

Good decisions in these items are not about being kind, strict or clever. They are about fit. The best option fits the facts as stated, respects the rules that bind the actor, and serves the purpose of the role. A generous option that breaks a rule fails. A rule-bound option that ignores the purpose also fails. The correct option usually does three things at once: it stays within the rules, it solves the actual problem, and it leaves a written trace or a follow-up so that the problem does not return.

### Step 1: separate facts from objectives

A **fact** is something the stem states. An **objective** is what the actor is supposed to achieve. Mixing them causes two errors: treating a hope as a fact ("the applicant probably exaggerates"), or treating a fact as the goal ("the inspection is on Monday, so the goal is to pass the inspection", when the goal is a safe building that will also pass it).

Worked example. A warden learns that a hostel's water tank has been contaminated. Facts: contamination confirmed, 200 residents, a repair team available tomorrow. Objective: residents' health. An option that "posts a notice and waits for the repair team" meets part of the objective; an option that "arranges safe drinking water today, posts a clear notice, and schedules the repair" meets all of it.

What it establishes: the objective decides which feasible option is best. Where it stops: the stem must actually state or clearly imply the objective; if it does not, use the purpose of the role described.

**Failure condition.** Adding a fact that the stem does not give. If you need "the supplier will deliver late anyway" or "the applicant is lying" to make an option work, that option rests on an assumption, and an option that needs no such assumption is better.

### Step 2: list the constraints that remove options

A **constraint** is anything that makes an option unavailable: a law, a contract, a rule of the office, a deadline, a resource limit, a stated duty. Write the constraints, then strike every option that breaks one.

Worked example. A training workshop needs a venue within 10 km of the district office, with seating for at least 60, at a cost inside a ₹15,000 budget. Venue G seats 80 and costs ₹12,000 but is 18 km away. Venue H is 4 km away and costs ₹9,000 but seats 45. Both are out, however attractive their other features. Only the venues that pass all three tests go on to compete on the objective, such as the better training facilities.

What it establishes: constraints act before preferences. Where it stops: if every option breaks some constraint, the item is asking which constraint may be relaxed lawfully, and the stem must say so.

**Failure condition.** Ranking options by the objective first and checking constraints afterwards. The highest-scoring option on the objective is often the one that breaks a rule.

### Step 3: choose the feasible option with the fewest added assumptions

Among the options that survive Step 2, pick the one that best meets the objective. If two seem equal, prefer the one that needs fewer facts not in the stem, and the one that includes verification, a written trace or follow-up.

Worked example. A clerk reports that two files have conflicting instructions. Option P: follow the newer file. Option Q: ask the issuing authority which instruction applies, write down the answer, and inform the team. P assumes that the newer file is the correct one. Q assumes nothing, and it prevents the same conflict next time. Q is better.

**Failure condition.** Choosing the option that "sounds most decisive". Speed is a virtue only if the action is lawful and correct.

### The elimination screen: what options typically fail on

| Fails because it is | Example of the pattern |
|---|---|
| Illegal or against a binding rule | releasing a payment before the required inspection |
| Coercive | threatening a citizen to make them comply |
| Deceptive or concealing | altering a register entry and telling no one |
| Discriminatory or favouring | giving a scarce allotment to an influential applicant |
| Disproportionate | closing a whole office because one counter is slow |
| Abdicating | doing nothing, or passing the matter on without acting |

| Survives because it is | Example of the pattern |
|---|---|
| Lawful and fair | applying published criteria to every applicant |
| Clear | explaining which rule controls and why |
| Proportionate | fixing the specific problem, not everything around it |
| Logged and followed up | noting the decision and checking that it worked |

**Failure condition.** Using the screen alone. Two options may both pass the screen; the four boxes then decide between them.

### Communication problems inside a decision item

Some scenarios turn on a misunderstanding, a conflict between people, the wrong channel for a message, or a poorly worded form. If you have studied communication earlier in your preparation, this section applies that learning to the decision procedure. The four boxes still decide; what changes is that Box 1 must include a diagnosis of why the message failed.

**Classify the barrier before choosing.** A communication barrier is whatever stops a message from arriving as it was meant. Five kinds cover almost every scenario, and each points to a different fix.

| Barrier | What has gone wrong | Original example | The fix it calls for |
|---|---|---|---|
| Physical | the setting blocks the message | a safety briefing given beside a running generator | change the place, the medium or the timing |
| Semantic | words or symbols are read differently | a notice says "submit by end of day"; some read 5 p.m., others midnight | define the term exactly ("by 5 p.m. on 12 March") |
| Psychological | attitude, fear or distrust filters the message | staff who expect bad news hear a routine audit as a threat | acknowledge the concern and explain the purpose |
| Organisational | the structure distorts or delays it | an instruction passes through four levels and arrives changed | shorten the chain or send it directly in writing |
| Technological | the tool fails or excludes people | an online form that works only on a desktop, for field staff who carry phones | provide a channel the audience can actually use |

Worked example. A ward office sends a circular on a new waste-collection timetable. Residents of one lane keep putting out bins on the old day. On enquiry: the circular used the phrase "alternate days from Monday", and half the lane read it as Monday-Wednesday-Friday while the other half read it as every second day counting from Monday. That is a semantic barrier, not defiance. The feasible option reissues the timetable with the actual dates, confirms it with the lane's residents' association, and checks the next two collections. An option that fines the lane first treats a wording failure as a conduct failure.

Where it stops: some scenarios have more than one barrier. Fix the one that the stem's facts actually show; do not add a barrier the stem does not support.

Two screens carry over unchanged. **Reject coercive and deceptive options:** humiliation, threats and concealment fail in communication scenarios exactly as they do elsewhere. **Prefer fair, clear and followed-up actions:** clarify privately, confirm understanding (for example, by asking the person to restate the requirement in their own words), and agree a check-in.

**Match the tool to the purpose.** Matching items pair a purpose with a channel. Decide by what the purpose needs: reach, a permanent written trace, privacy, a reply, or speed.

| Purpose | What it needs | A channel that fits | A channel that fails it |
|---|---|---|---|
| a binding instruction to all staff | reach and a written trace | written circular or office order | a passing remark in a meeting |
| feedback on one person's poor work | privacy and a reply | one-to-one conversation | a group email |
| views from several hundred residents | reach and comparable answers | short questionnaire | one public meeting where a few voices dominate |
| an urgent hazard warning | speed and reach | siren, SMS alert, loudspeaker | a printed notice for the next day |
| explaining a complex change to a small team | two-way discussion | meeting with questions, followed by a written summary | a one-line message |

The decision mechanics are those of matching grids: fix the pairs that only one channel can satisfy, then eliminate. **Failure condition:** choosing the most modern or most formal channel instead of the one whose features the purpose needs.

**Design a questionnaire from its objective.** A questionnaire is a list of heads (questions) chosen to collect exactly the information a stated objective needs. Work in four steps:

1. Write the decision the information will serve.
2. List the facts that decision depends on; each becomes a head.
3. Strike any head whose answer would not change the decision, and any head that intrudes on privacy without need.
4. Test the wording of each head: one idea per question, no leading phrasing, answer options that cover every case without overlap.

Worked example. Objective: to decide the departure times of a new evening bus from a college campus to the city. Draft heads and their test:

| Draft head | Keep or change | Reason |
|---|---|---|
| When does your last class usually end? | keep | departure times depend on it |
| Which area of the city do you travel to? | keep | the route and stops depend on it |
| How do you travel home now, and how long does it take? | split into two questions | two ideas in one question cannot be answered honestly with one reply |
| Don't you agree that a college bus is badly needed? | rewrite as "Would you use an evening college bus? Yes / No / Not sure" | leading wording pushes one answer |
| What were your marks in the last examination? | strike | it does not affect departure times and intrudes without need |

Where it stops: relevance depends on the stated objective. Marks would be relevant to a scholarship survey; they are not relevant here. **Failure condition:** keeping a head because it is "interesting" or "might be useful", which lengthens the form and lowers the response rate without serving the objective.

**Handle a conflict by separating the issue from the people.** In a conflict scenario, list the facts of the dispute, the rule or goal both parties share, and the options. Then test each option on the same screen as any other: does it rest on the stated facts, serve the shared goal, and leave something that can be checked later? An option that decides blame before the facts are known fails the screen.

Worked example. Two shift supervisors in a hospital store blame each other for medicines missing from the handover count. Facts: counts differ at handover on four days in a month; there is no written handover sheet. Shared goal: an accurate stock. The feasible option meets both supervisors, introduces a handover sheet that both sign, and reviews the counts after two weeks. Ordering one supervisor to "take responsibility" decides blame without facts; ignoring the dispute leaves the stock wrong.

**Failure condition.** Treating a communication or conflict scenario as a character flaw before checking whether the message, the channel or the process was clear.

### Applying the procedure to recurring public-office families

Each family below is taught through a situation with its own decision structure: a different pair of boxes pulling against each other, a different cast and set of choices, and a different path for taking the matter further. What carries over is the procedure, so that it works on whatever structure an item presents.

**Discretion that must correct the office's own error.** A municipal officer allots six vending spots each year by a public lottery among licensed vendors, under a published scheme. Two days after the draw, a licensed vendor shows that her name was missing from the lottery list because of a data-entry mistake in the office. The six winners have already been told.

- Boxes in tension: two constraints pull apart. The published scheme says every licensed vendor is in the draw; the six winners have been promised a result. The objective, a fair allocation under the scheme, decides between them.
- Options weighed: (i) create a seventh spot for her by order; (ii) tell her to wait for next year; (iii) hold a fresh public draw from the corrected list, after notice to all, with the reason written down; (iv) let her persuade a winner to swap privately.
- Test: (i) goes outside the scheme, which fixes six spots. (ii) makes her pay for the office's error and leaves the defect in place. (iv) is a private bargain with no trace. Option (iii) restores the published rule openly; the winners lose a result that was never valid, and they keep an equal chance.
- Taking it further: the officer holds the power and needs no one's permission; what goes upward is the clerk's error, for review of how the list is prepared.

Failure condition: treating the finality of an announcement as more binding than the rule that produced it, or inventing a remedy the scheme does not provide.

**A benefit offered while a decision is pending.** A district education officer is evaluating bids to supply school furniture. Before the result, one bidder offers to donate twenty computers to a government school "as goodwill, with no conditions". Rules: officials handling a tender may not accept gifts or donations from a bidder while the tender is open, and donations to schools are accepted only through the district donation committee.

| Option | What it serves | What it breaks |
|---|---|---|
| Accept, since the computers help children | the objective of better schools | the gift rule, during an open tender |
| Accept quietly once the result is out | the objective, later | the gift rule in spirit, and it leaves no trace |
| Disqualify the bidder at once | an appearance of firmness | the tender committee's own procedure |
| Decline for now, write down the offer, inform the tender committee, and tell the bidder that donations go through the donation committee after the tender closes | integrity of the tender, and the donation can still be considered properly | nothing |

The offer is tempting precisely because it serves the objective; the constraint still comes first. Taking it further means declaring the offer to the tender committee, which decides under its own rules whether the bid is affected. Failure condition: judging the offer by its usefulness instead of by the rule on timing and channel, or punishing the bidder personally before the committee acts.

**Protection that the person asks you to withhold.** A school counsellor notices bruises on a Class 7 pupil on several occasions. When she asks, the pupil says a relative at home hits him and begs her not to tell anyone. Rules: school staff must report suspected harm to a child to the school's designated child-protection officer within 24 hours, and may not investigate the family themselves.

1. Facts: repeated bruises, the pupil's own account, and his request for secrecy. The request is a fact to respect in how she acts, not a constraint that cancels the duty.
2. Constraint: the reporting rule, with its time limit, and the bar on investigating.
3. Objective: the child's safety.
4. Options: keep the promise; visit the relative to warn him; tell the class teacher and leave it there; report to the designated officer today, tell the pupil honestly what will happen and why, and stay available to him. Only the last meets the rule and the objective without overstepping the role.

The path for taking it further runs sideways to a named officer, not up the line, and the counsellor does not decide what follows. Failure condition: letting a promise of secrecy override a duty to protect, or acting beyond the role by confronting the family.

**A shortfall rationed by a stated priority.** A relief-camp officer receives 120 blankets for 150 registered families on a cold night; a second consignment is due in 48 hours. The published order is: families with an infant or a person over 70 first, then the rest by order of registration. Forty-five families are in the first group. A volunteer suggests cutting blankets in half "so that everyone gets something", and some late-registered families demand equal shares.

- Boxes in tension: the objective (protect those most at risk from cold) against a fairness demand that is not one of the constraints.
- Working: 45 blankets go to the priority families, the remaining 75 to the next 75 families by registration, and 30 families are without a blanket tonight.
- Feasible option: follow the published order, display the list so that anyone can check it, arrange shared shelter or other temporary warmth for the 30 families, and ask the district to bring the second consignment forward.
- Taking it further: upward for resources, not for permission; the order itself is already published.

Failure condition: an equal split that leaves the most vulnerable with half a blanket, or holding everything back until there is enough for all.

**Repairing trust after the office's own wrong message.** A health office sent parents an SMS with the wrong date for a school deworming day. Many children came on the wrong day and were turned away; parents now call the drive badly run, and a rumour says the tablets are unsafe. Here the communicator caused the barrier. The error was organisational, and the distrust it created is psychological, so both need a fix. The options range from sending a bare correction, to blaming the telephone company, to making attendance compulsory. The feasible option admits the error plainly, sends the correct date by SMS and through class teachers whom parents already trust, answers the safety rumour with the facts and a contact number, and offers a catch-up day. Failure condition: hiding the office's mistake or shifting the blame, which deepens the very distrust the message must overcome.

**A conflict of interest in custody of confidential material.** A senior clerk is placed in charge of the strong room that holds the sealed papers for a departmental promotion examination, three weeks away. She then learns that her husband has applied to sit it. Nobody has asked her for anything, and no seal has been touched. Rules: an official with a spouse among the candidates must declare it in writing to the examination controller and be relieved of any duty connected with the papers. The boxes in tension are her confidence in her own honesty, which the rule does not ask about, and the declaration rule; the objective is an examination whose integrity can be shown, not merely claimed. Her options are to carry on in silence, to ask her husband to withdraw, to swap duties informally with a colleague, or to declare in writing, hand over the keys and the seal register to the person the controller names, and step away from the strong room. Only the last satisfies the rule and leaves a trace that anyone can check later. Failure condition: reasoning "I am honest, so the rule does not apply to me", or asking a candidate to give up a lawful chance in order to solve the official's own conflict.

**Conflict-handling and questionnaire-design items.** Statement-evaluation items on resolving a workplace conflict, and items that ask which heads belong in a questionnaire, use the methods above. For a conflict item, list the facts, the shared goal and the binding rules, and test each numbered statement against them. For a questionnaire item, test every head against the stated objective, privacy and wording. Judge each numbered statement or head separately before choosing a code.

### Sounding right is not the same as fitting

The tempting method is to pick the option that sounds most moral or most firm, without checking it against the stem. "Suspend the clerk at once" sounds firm; "grant every request that arrives" sounds kind. Both add assumptions and ignore constraints: due process in the first, verification in the second. The reply is to run the four boxes. An option that sounds right but needs an unstated fact, or breaks a rule, loses to a plainer option that fits.

A second tempting method is to prefer the option that avoids all risk by doing nothing or by passing the matter upward without acting. The reply is that inaction is itself a choice, and it usually fails the objective.

### Stakeholder listening (Advanced)

Before proposing any action, identify the interests and constraints of each party involved. A feasible option must respect those constraints, and an option that ignores a stated interest is usually the one a careful reader eliminates first. Failure condition: the listening step does not license an option that breaks a stated rule, however much it pleases a party.

### UPSC application

- **House-allotment discretion and scarce-commodity favour families:** discretion works inside published criteria and limits; name the box the pressure comes from (a relationship, seniority, a shortage) and test every option against the published rule and its purpose, with reasons written down.
- **Illegal payment demands:** an unlawful payment or benefit stays unlawful whatever its size or good purpose; prefer options that stop it, leave a written trace and use the proper channel, without punishing anyone before the facts are established.
- **A person seeking protection:** act within your role, make sure the authority that can protect is engaged without delay, and follow up.
- **Communicating a programme to a resistant community:** classify the barrier first; then honest specifics, two-way channels and trusted local messengers; reject pressure and misinformation.
- **Confidential examination material:** do not use, pass on or seek it; declare or report at once to the competent authority, and leave decisions about the examination to that authority.
- **Conflict-handling and questionnaire-design statement items:** evaluate each numbered statement or head against the facts, the shared goal or stated objective, and the screen, then choose the code.

### Revision points

- Work in four boxes: facts, constraints, objective, feasible options.
- Facts are only what the stem states; do not add hopes or suspicions.
- Constraints remove options before the objective ranks them.
- Among feasible options, choose the one that best serves the objective with the fewest added assumptions.
- Reject illegal, coercive, deceptive, discriminatory, disproportionate and abdicating options.
- Prefer lawful, fair, clear, proportionate, logged and followed-up actions.
- Classify a communication barrier as physical, semantic, psychological, organisational or technological, and choose the fix that matches it.
- Match a channel to what the purpose needs: reach, a written trace, privacy, a reply or speed.
- A questionnaire head stays only if its answer serves the stated objective without needless intrusion.
- A question that asks two things at once, or leads the respondent, fails the wording test.
- Discretion is bounded by published criteria and conflict-of-interest rules.
- The size of an unlawful payment does not change its legality.
- In a conflict, separate the issue from the people, and test each option against the facts and the shared goal.
- Inaction is a choice and usually fails the objective.
- Firm-sounding and kind-sounding options often hide an unstated assumption.

### Practice

**MCQ 42**

A block officer must hold a one-day vaccination camp. The camp needs a day on which the hall is free, at least two nurses are on duty, and it is not the weekly market day (Wednesday). The aim is the largest turnout among the days that meet every condition.

| Day | Hall | Nurses on duty | Expected turnout |
|---|---|---:|---:|
| Monday | free | 1 | 300 |
| Tuesday | free | 4 | 250 |
| Wednesday | free | 3 | 400 |
| Thursday | booked | 2 | 350 |
| Friday | free | 2 | 280 |

Which day should be chosen?

- A. Wednesday, which carries the largest expected turnout
- B. Friday, with a larger expected turnout than Tuesday
- C. Thursday, with its two nurses and a turnout of 350
- D. Tuesday, the day with the most nurses

**MCQ 42 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** Ranks by the objective before checking constraints. Wednesday has the largest turnout, 400, but it is the market day, which the conditions exclude.
- **B — Correct:** Monday fails the nurse condition (1 nurse), Wednesday fails the market-day condition, and Thursday fails the hall condition. Only Tuesday (250) and Friday (280) are feasible, and Friday has the larger turnout.
- **C — Incorrect:** Checks only the nurse condition. Thursday has two nurses and a turnout of 350, but the hall is booked, so it is not a feasible day.
- **D — Incorrect:** Replaces the stated aim with a different one. Tuesday has the most nurses, 4, but the aim is turnout, and Tuesday's 250 is below Friday's 280.

**MCQ 43**

You supervise a road project that is three weeks behind schedule. The contractor offers to finish within ten days if you sign off the completed work without the quality-test reports that the contract requires. Under the contract, a contractor can be blacklisted only after a show-cause notice and an inquiry. What is the most appropriate response?

- A. Accept the offer and sign off, since the public needs the road soon
- B. Refuse the offer and announce a blacklisting today, skipping the required show-cause notice
- C. Refuse the sign-off, write down the offer and keep the contracted tests
- D. Extend the deadline quietly and leave the contractor's offer out of the file

**MCQ 43 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** Lets the deadline override a binding contract term. The quality tests are a constraint, and a fast road of untested quality does not meet the real objective.
- **B — Incorrect:** Refusing is right, but the stem states that blacklisting requires a show-cause notice and an inquiry first. Announcing it today breaks that constraint and is disproportionate.
- **C — Correct:** Keeps the constraint (the contracted tests), serves the objective (a road of proper quality), and logs the improper offer so that it can be dealt with through the contract's own procedure, including its remedies for delay. It needs no assumption beyond the stem.
- **D — Incorrect:** Conceals the offer and changes the schedule without a written trace. It fails the screen on concealment and leaves the improper condition unaddressed.

**MCQ 44**

You must publish the final list of families eligible for a ration scheme in three days. Twenty families complain that they were wrongly left out. Income and residence files for all families are available in your office. Which action best meets the aim of a correct list on time?

- A. Publish the list unchanged, since three days allow no checks
- B. Add every complaining family so none is missed
- C. Hold back the list until a fresh survey of every household is finished
- D. Check each complaint against the income and residence files in time

**MCQ 44 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** Treats the deadline as the whole objective and assumes, without evidence, that checking is impossible. Files are available, and twenty complaints can be checked in three days.
- **B — Incorrect:** Assumes every complainant is eligible, which the stem does not state. It may put ineligible families on the list and so fails the aim of a correct list.
- **C — Incorrect:** Is disproportionate. A fresh survey of all households misses the deadline to fix a problem that concerns twenty families.
- **D — Correct:** Uses the available files to test each complaint, adds only families that qualify, and still meets the deadline. It needs no assumption beyond the facts given.

---

# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES

This section links every Prelims CSAT question from 2013 to 2026 whose method is taught in these lessons. Each link opens the question-level entry of its year file. Nothing here reproduces a question, an option, a letter or a worked solution, and no answer key appears in this section.

Four points govern how to use the list.

1. **Family before calculation.** The family label names the kind of question the stem presents. Identify the family first; it tells you which lesson's method applies.
2. **Demand.** The demand states, in neutral words, what the question asks you to find or decide. Read it before the stem so that you know which quantity or verdict ends the work.
3. **Format.** A statement set needs each statement tested alone, and the code is read only after every statement has been checked. A matching item is settled pair by pair.
4. **The approach is a route, not a result.** It names the test to run. Run the test on the numbers in the stem and check the result by a second route.

## How the items add up

| Span | Items |
|---|---:|
| 2013 to 2017 | 123 |
| 2018 to 2026 | 172 |
| Total | 295 |

| Teaching home | Items |
|---|---:|
| Lesson 1 (Conditional logic and implication chains) | 4 |
| Lesson 2 (Syllogisms, statement sets and truth-teller logic) | 31 |
| Lesson 3 (Series, analogies and figural sequences) | 25 |
| Lesson 4 (Coding, decoding and alphametics) | 23 |
| Lesson 5 (Directions, distance and directed networks) | 10 |
| Lesson 6 (Blood relations and family graphs) | 12 |
| Lesson 7 (Ranking, ordering and comparison chains) | 20 |
| Lesson 8 (Seating and arrangement) | 18 |
| Lesson 9 (Logic grids and matching structures) | 32 |
| Lesson 10 (Counting arrangements: permutations, restrictions and codes) | 18 |
| Lesson 11 (Counting selections: combinations, partitions and routes) | 21 |
| Lesson 12 (Sets, overlap and inclusion-exclusion) | 10 |
| Lesson 13 (Probability, worst cases and weighing strategies) | 12 |
| Lesson 14 (Plane-figure counting) | 7 |
| Lesson 15 (Solid and cube counting) | 11 |
| Lesson 16 (Data interpretation I: levels, changes and shares) | 21 |
| Lesson 17 (Data interpretation II: pies, dual axes and weighted scores) | 12 |
| Lesson 18 (Decision scenarios and the decision procedure) | 8 |

Each item appears once. Where one family spans several lessons, each item is placed in the lesson that teaches its method most directly.

## 2013 - 34 items

For Q75 to Q80 the official key accepts two responses for each item. The approach for each names the tests to run on its options and does not indicate either accepted response.

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q9](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q009) | Primary-group inference | Statement set; choose by code | Decide which statement about a primary group is borne out by the three given characteristics. | Test each option against the three statements and accept only what the statements themselves support. | Lesson 9 |
| [Q10](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q010) | Smallest money share | Single answer | Identify the friend with the smallest amount from three stated differences between shares. | Write every share in terms of one unknown using the stated differences, then compare the expressions. | Lesson 16 |
| [Q11](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q011) | Direct route from Q to R | Single answer | Name the single transport mode that links Q to R without a change of mode. | For each mode in turn, write only that mode's links as a list, travelling each link only in the direction the data allows; run the reachability test outward from Q on that list alone, and accept only a mode under which R gets marked. | Lesson 5 |
| [Q12](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q012) | City necessarily revisited | Single answer | Identify the place that a closed tour from P must visit twice. | Draw the five places as a network with every link marked by its modes, find any place that has only one link, and ask which place a round trip from P cannot avoid passing through twice. | Lesson 5 |
| [Q13](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q013) | Directly connected city pair | Single answer | Identify the pair of places joined directly by some mode. | Draw the five places as a network from the connection data and check each named pair for a link of its own, without passing through a third place. | Lesson 5 |
| [Q14](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q014) | Maximum travel options | Single answer | Identify the pair of places with the largest number of direct travel options. | List the direct modes for each pair named in the options from the connection data, then compare the counts. | Lesson 11 |
| [Q15](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q015) | Tennis team with Y and without B | Single answer | Identify the four-member team forced when Y is in and B is out. | Strike every option that contains an incompatible pair or misses the gender minimum, then check the survivor against every condition. | Lesson 11 |
| [Q16](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q016) | Tennis team with B and without Y | Single answer | Identify the four-member team forced when B is in and Y is out. | Strike every option that contains an incompatible pair or misses the gender minimum, then check the survivor against every condition. | Lesson 11 |
| [Q17](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q017) | Teams containing all three males | Single answer | Count the four-member teams possible when all three males are chosen. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q18](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q018) | Compatible music team | Single answer | Choose the four-person group that satisfies every pairing condition. | Strike every option that contains a pair who will not work together or splits a pair who must, then check the survivor against every condition. | Lesson 11 |
| [Q19](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q019) | Round-table necessities | Statement set; choose by code | Decide which seating statements must hold at a five-seat round table. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q20](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q020) | Friend who does not play hockey | Single answer | Identify the friend who does not play hockey from the paired game data. | Tabulate each friend against each game from the paired statements, then read the row or column asked for. | Lesson 12 |
| [Q21](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q021) | Friend with a stated game count | Single answer | Identify the friend who plays a stated set of three games. | Tabulate each friend against each game from the paired statements, then read the row or column asked for. | Lesson 12 |
| [Q22](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q022) | Game common to B C and D | Single answer | Identify the game common to three named friends. | Tabulate each friend against each game from the paired statements, then read the row or column asked for. | Lesson 12 |
| [Q23](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q023) | Age-order inference | Single answer | Choose the conclusion that follows from stated age and game-result facts. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q29](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q029) | People and cities | Single answer | Identify the statement that is not correct about a person-to-city assignment. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q30](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q030) | Cap-colour deduction | Single answer | Determine the cap colour of one person in a queue from what each person can see. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q34](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q034) | Rank from the end | Single answer | Find a student's new rank from the end after two students join. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q44](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q044) | Moving symbols in a grid | Single answer | Choose the figure that continues a sequence of moving symbols. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q45](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q045) | Triangle symbol sequence | Single answer | Choose the figure that continues a triangle-and-symbol sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q46](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q046) | Line-and-arrow sequence | Single answer | Choose the figure that continues a line-and-arrow sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q51](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q051) | Cube faces A and B | Single answer | Identify possible numbers on two marked faces of a cube from three views. | Use every view to fix adjacency, count slice by slice, and track which faces remain painted. | Lesson 15 |
| [Q52](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q052) | Physics professors in a stated age band | Single answer | Read the number of professors in one discipline and age band from two figures. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q53](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q053) | Highest male-female ratio | Single answer | Identify the discipline with the highest male-to-female ratio. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q54](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q054) | Female psychology professors | Single answer | Find the female percentage among professors of one discipline. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q55](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q055) | Male Physics professors in a stated age band | Single answer | Find a male count in one age band from a stated female share of that band. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q56](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q056) | Total university professors | Single answer | Find the total number of professors from one discipline's stated share. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q57](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q057) | Circular-arrow sequence | Single answer | Choose the figure at the seventh position of a circular-arrow sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q75](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q075) | House-allotment discretion | Objective item; official key accepts two responses | Choose a course of action when a close subordinate seeks priority in an allotment that the published rules and their review do not give. | Set the published allotment rules and the finding of the office that applied them against your closeness to the applicant; test each option on whether the decision stays within rules you yourself made public, and on how it deals with the relationship and the hardship pleaded. | Lesson 18 |
| [Q76](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q076) | Illegal transport-counter payment | Objective item; official key accepts two responses | Choose a course of action when you witness an illegal collection at a transport counter. | Identify the illegal element (a charge collected without a receipt), your position as a passenger with a deadline, and who has the authority to act on it; test each option on whether it addresses the illegality, when, and through whom. | Lesson 18 |
| [Q77](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q077) | Villager seeking protection | Objective item; official key accepts two responses | Choose a course of action when a villager who has travelled far to seek protection approaches you between two meetings. | Weigh the vulnerability of an applicant who has travelled far and waited against the pressure of your own schedule; test each option on whether the application is received, who acts on it, and how soon protection could follow. | Lesson 18 |
| [Q78](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q078) | Sugar-allotment favour | Objective item; official key accepts two responses | Choose a course of action when a close friend seeks a release above a binding government limit. | Separate the binding government limit from the personal request and the friendship; test each option on whether it keeps the release within the limit, and on how it handles the friend's expectation that office can override the order. | Lesson 18 |
| [Q79](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q079) | Communicating family planning | Objective item; official key accepts two responses | Choose the most effective way to communicate a programme to an opposed community. | Treat this as a choice of message and channel for an audience that opposes the policy; compare how the channel, the messenger and the tone of each option would land with residents who already oppose it. | Lesson 18 |
| [Q80](../../../solved_pyqs/papers/2013/prelims-csat.md#2013-prelims-csat-q080) | Confidential examination paper | Objective item; official key accepts two responses | Choose a course of action when a colleague seeks confidential examination content. | Identify the duty of confidentiality that comes with setting the paper; test each option on whether it keeps that duty intact, and on how it answers the colleague's appeal, the past favour and the claimed consequence for his son. | Lesson 18 |

## 2014 - 24 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q8](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q008) | Ladder ordering | Single answer | Identify the person on the bottom step from relative ladder positions. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q9](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q009) | Median by height | Single answer | Identify the person in the middle position when ordered by height. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q11](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q011) | Adjacent seat to D | Single answer | Identify who sits next to D in a row of four from adjacency clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q21](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q021) | Book classification intersection | Single answer | Identify the two books that satisfy three attribute conditions together. | Tabulate each book against the three attributes and keep only the books that meet all three conditions. | Lesson 12 |
| [Q25](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q025) | Card-flip puzzle | Single answer | Find the least number of tries to turn all cards when exactly four are turned per try. | Track how many cards show each side after every try and find the smallest number of tries that can reach the target state. | Lesson 13 |
| [Q34](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q034) | Equal fruit-seller profit | Single answer | Identify the year in which two sellers' average profits are equal. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q35](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q035) | Profit difference across two years | Single answer | Find the difference between two sellers' average profits in one year. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q36](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q036) | Profit increase in a stated year | Single answer | Find one seller's change in average profit between two years. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q37](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q037) | Trend of B profit | Single answer | Describe the trend of one seller's average profit across four years. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q39](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q039) | Embedded figure | Single answer | Identify the figure in which the target figure is embedded. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q40](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q040) | Arrow matrix completion | Single answer | Choose the entry that completes an arrow matrix. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q41](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q041) | Population-income table inference | Single answer | Choose the correct statement about population and income over four years. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q43](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q043) | Circle-triangle matrix | Single answer | Choose the entry that completes a circle-and-triangle count matrix. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q44](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q044) | Routes from S to T | Single answer | Count the routes through a chain of networks without retracing. | Count the route choices through each section that must be passed, multiply across sections, and check that no route retraces. | Lesson 11 |
| [Q45](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q045) | Bead-position sequence | Single answer | Choose the fifth figure in a bead-orientation sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q59](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q059) | Likely poet this year | Single answer | Identify the poet most likely to be asked about this year from stated preferences. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q60](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q060) | Dancer and violinist | Single answer | Identify the woman who is certainly both a dancer and a violinist. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q62](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q062) | Army-civilian mortality comparison | Single answer | Choose the inference that the two mortality rates allow. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q63](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q063) | Accident-rate inference | Single answer | Choose the conclusion that a comparative accident statement allows. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q66](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q066) | George free day | Single answer | Identify the other free day in a weekly class timetable. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q67](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q067) | Row-position count | Single answer | Count the people in a row other than two who interchange positions. | Convert both positions to counts from one end before and after the interchange, then total the row. | Lesson 8 |
| [Q78](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q078) | Profession of B | Single answer | Identify one person's profession from the shared clue set. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q79](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q079) | Family couples | Single answer | Identify which pairs in the shared clue set are couples. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q80](../../../solved_pyqs/papers/2014/prelims-csat.md#2014-prelims-csat-q080) | Profession of D | Single answer | Identify another person's profession from the shared clue set. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |

## 2015 - 24 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q9](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q009) | Dinner-host lottery | Single answer | Find how many dinners a particular member hosts in a year under monthly lots. | Separate what is certain from what is merely possible or expected before judging the options. | Lesson 13 |
| [Q11](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q011) | Figure-sequence completion | Single answer | Choose the figure that continues a cycling T-shaped sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q14](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q014) | Cardboard assembly | Single answer | Identify the solid that the four given pieces can form. | Match each piece to a face or section of each candidate solid and reject candidates that need a piece not supplied. | Lesson 15 |
| [Q17](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q017) | Couple height-ordering puzzle | Single answer | Identify the statement that is not correct about two couples' heights. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q18](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q018) | Who remained at home | Single answer | Determine who remained at home from the family's movements. | List every family member and remove each one the statements place elsewhere. | Lesson 2 |
| [Q19](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q019) | Meditation and aggression | Single answer | Identify the belief that underlies the second speaker's reply. | Identify what the speaker must believe for the reply to make sense, and reject options that go beyond it. | Lesson 2 |
| [Q20](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q020) | Athletes and balanced diet | Single answer | Choose the best conclusion from a chained statement about athletes. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q29](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q029) | Relative running speed | Single answer | Compare C's speed with A's from two speed comparisons. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q32](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q032) | Vegetable taste ordering | Single answer | Choose the conclusion that the three taste comparisons allow. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q33](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q033) | Opposite-direction square paths | Single answer | Choose the correct statement about two walkers turning in opposite senses. | For a walk, track the heading after every turn and sum the signed displacements; for a network, treat each link exactly as stated (one-way or two-way) and test each claim against every route. | Lesson 5 |
| [Q48](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q048) | Principal and Vice-Principals | Single answer | Count the possible selections for one principal and two vice-principal posts. | Fill the restricted post first, then count the selections for the remaining posts and multiply. | Lesson 9 |
| [Q49](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q049) | Subject combinations | Single answer | Count the two-subject combinations allowed under one prerequisite. | Count the unrestricted pairs, then add only the restricted pairs that meet the prerequisite. | Lesson 9 |
| [Q52](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q052) | Earnings graph | Single answer | Choose the conclusion that the two earnings curves support. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q54](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q054) | Coloured cube | Single answer | Identify the colour opposite a given face from four adjacency statements. | Use every view to fix adjacency, count slice by slice, and track which faces remain painted. | Lesson 15 |
| [Q55](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q055) | Syllogistic conclusions | Single answer | Decide which of two conclusions follows from two "some" statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q56](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q056) | UFO inference | Single answer | Choose what may be concluded from three statements about space and life. | Test each conclusion against the statement alone; accept it only if it must hold, not merely because it is plausible or generally true. | Lesson 2 |
| [Q58](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q058) | Commodity-price graph | Single answer | Read the commodity price in one year from the curve. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q60](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q060) | Slowest runner | Single answer | Identify the slowest runner from three speed comparisons. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q69](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q069) | Task assignment count | Single answer | Count the assignments of five tasks to five persons under two restrictions. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q72](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q072) | Cousins' possible age | Single answer | Identify the possible statement about the cousins' ages. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q73](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q073) | Cousins' age orders | Single answer | Count the possible increasing-age orders of six cousins. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q75](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q075) | Language and driving puzzle | Single answer | Identify the true statement about language and driving in a group of four. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q77](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q077) | Cow-goat price bounds | Single answer | Choose the most valid conclusion about a cow's price from goat-price bounds. | Combine the two bounds to find the range of the price asked about, then test each conclusion against that range. | Lesson 7 |
| [Q78](../../../solved_pyqs/papers/2015/prelims-csat.md#2015-prelims-csat-q078) | Fighters and cowards | Single answer | Identify the correct statement about types in a fighter-and-coward society. | Assume a type for one person, propagate through the relationship rules, and test each option against every consistent assignment. | Lesson 2 |

## 2016 - 20 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q7](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q007) | Fruit-caused sickness | Single answer | Identify the cause of sickness from what each person ate. | Compare what each person who fell sick ate with what each person who stayed well ate, and test each option against both lists. | Lesson 2 |
| [Q8](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q008) | Population-growth conclusion | Single answer | Choose the conclusion that may be true given four population facts. | Test each conclusion against the statement alone; accept it only if it must hold, not merely because it is plausible or generally true. | Lesson 2 |
| [Q10](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q010) | Falsifying an either–or claim | Single answer | Identify the fact that would falsify an either-or claim. | Write each link as an arrow, add its contrapositive, then chain the arrows; test a claim by assuming its negation. | Lesson 1 |
| [Q11](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q011) | Music and gender conclusion | Single answer | Choose the conclusion about the party guests from the music and gender data. | Ask whether the observation forces the conclusion or is only consistent with it. | Lesson 2 |
| [Q12](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q012) | Circular seating puzzle | Statement set; choose by code | Decide which seating statements must be true at a five-seat round table. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q15](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q015) | Profession puzzle: doctor | Single answer | Identify the doctor from the shared profession clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q16](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q016) | Profession puzzle: artist | Single answer | Identify the artist from the shared profession clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q17](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q017) | Profession puzzle: spouse | Single answer | Identify R's spouse from the shared profession clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q18](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q018) | Profession puzzle: lawyer | Single answer | Identify the lawyer from the shared profession clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q19](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q019) | Definitely male group member | Single answer | Identify the group member who is definitely a man. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q27](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q027) | Bridge crossing with final lamp return | Single answer | Find the minimum total time for four people to cross with one lamp. | Write out candidate crossing plans step by step, add each plan's times including every lamp return, and compare the totals. | Lesson 13 |
| [Q32](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q032) | Age-order conclusion | Single answer | Choose the conclusion that follows from three either-or age statements. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q34](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q034) | Golf-ball box | Single answer | Identify the box that contains the golf ball. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q35](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q035) | Box-colour statement | Statement set; choose by code | Decide which statements about the boxes are correct. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q36](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q036) | Football-box colour | Single answer | Identify the colour of the box holding the football. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q54](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q054) | Surname of C | Single answer | Identify C's surname from the shared clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q55](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q055) | Colour of the tie | Single answer | Identify the colour of the tie from the shared clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q56](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q056) | Sweater wearer | Single answer | Identify the person who wore the sweater from the shared clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q61](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q061) | Military coding pattern | Single answer | Apply the rearrangement code shown on two words to a new word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q72](../../../solved_pyqs/papers/2016/prelims-csat.md#2016-prelims-csat-q072) | Constrained digit-string permutations | Single answer | Count four-digit numbers from four digits under four placement restrictions. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |

## 2017 - 21 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q9](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q009) | Party-supporter logical implication | Single answer | Identify the statement that must be true from the party-supporter information. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q10](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q010) | Party-supporter statement validity | Statement set; choose by code | Decide which statements about the party supporters are not correct. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q13](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q013) | Test scheduling puzzle | Single answer | Identify the last of four tests from two ordering clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q15](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q015) | Voice-practice conclusion | Single answer | Decide which of two conclusions follows from a statement about voice and practice. | Test each conclusion against the statement alone; accept it only if it must hold, not merely because it is plausible or generally true. | Lesson 2 |
| [Q19](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q019) | Symbolic family relation | Single answer | Interpret a two-symbol relation expression. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q29](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q029) | Women-category logic grid | Single answer | Identify the woman who both plays tennis and works in a bank. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q34](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q034) | Morning-walk conclusions | Statement set; choose by code | Decide which of two conclusions about morning walks are valid. | Test each conclusion against the statement alone; accept it only if it must hold, not merely because it is plausible or generally true. | Lesson 2 |
| [Q38](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q038) | Rectangles from grid lines | Single answer | Count the rectangles and squares formed by four horizontal and four vertical lines. | List each figure by size or type exactly once; use the diagonal formula only for a convex polygon. | Lesson 14 |
| [Q50](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q050) | Colour propositions | Single answer | Determine what is definitely concluded about the other three propositions when one is true. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q55](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q055) | Family inference puzzle | Single answer | Choose the inference that follows from six family relationships. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q56](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q056) | Blind draw colour guarantee | Single answer | Find the minimum blind draw that guarantees one ball of each colour. | Write the sample space, use conditional fractions without replacement, or take the worst case that avoids the target and add one. | Lesson 13 |
| [Q57](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q057) | Nonadjacent girls arrangement | Single answer | Count the row arrangements of two boys and two girls with girls not adjacent. | Arrange the unrestricted people first, then place the restricted people in the gaps between them. | Lesson 8 |
| [Q59](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q059) | Row arrangement puzzle | Single answer | Identify the correct statement about an eight-person row facing one way. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q60](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q060) | Word-code deduction | Single answer | Identify the code digit for one word from three coded phrases. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q69](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q069) | Lecturer-subject logic grid | Single answer | Identify the lecturer specialised in one subject from the shared grid clues. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q70](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q070) | Economics lecturer's city | Single answer | Identify the city of the lecturer of one subject. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q71](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q071) | Hyderabad lecturer | Single answer | Identify the lecturer belonging to one city. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q72](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q072) | Maximum subjects taught | Single answer | Identify the teacher who teaches the most subjects from paired teaching data. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q76](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q076) | Directed railway route necessity | Single answer | Identify the station that every route between two stations must pass. | Follow the one-way links head to tail from the start, list every route to the destination, and keep only a station that lies on all of them. | Lesson 5 |
| [Q77](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q077) | Counting directed railway routes | Single answer | Count the routes between two stations that pass no station twice. | List the routes station by station from the start without revisiting any station, then count them. | Lesson 11 |
| [Q78](../../../solved_pyqs/papers/2017/prelims-csat.md#2017-prelims-csat-q078) | Route after closing G-to-C | Single answer | Identify the station that need not be passed once one link is closed. | Remove the closed link, list every route that still runs from the start to the destination, and test each option against all of those routes. | Lesson 5 |

## 2018 - 33 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q1](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q01) | Triangle count in a drawn figure | Single answer | Count the triangles in a drawn three-dimensional figure. | Count the triangles face by face on the drawn solid, then add those that use a line crossing the inside; accept a candidate only if all three sides are drawn lines and its corners are not on one line, so that each triangle is counted once. | Lesson 14 |
| [Q4](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q04) | Polygon diagonal count | Single answer | Count the diagonals of a stated polygon. | List each figure by size or type exactly once; use the diagonal formula only for a convex polygon. | Lesson 14 |
| [Q11](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q11) | Bar-chart data comparison | Single answer | Find by how much one import exceeded another over three months. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q12](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q12) | Bar-chart value calculation | Single answer | Estimate the total value of one import over six months. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q13](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q13) | Bar-chart ratio reading | Single answer | Estimate the ratio of two imports over three months. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q14](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q14) | Cube rotation opposite face | Single answer | Identify the symbol opposite one face from given cube views. | Use every view to fix adjacency, count slice by slice, and track which faces remain painted. | Lesson 15 |
| [Q15](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q15) | Cube rotation opposite face | Single answer | Identify the symbol opposite a second face from the same views. | Use every view to fix adjacency, count slice by slice, and track which faces remain painted. | Lesson 15 |
| [Q16](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q16) | Cube rotation opposite face | Single answer | Identify the symbol opposite a third face from the same views. | Use every view to fix adjacency, count slice by slice, and track which faces remain painted. | Lesson 15 |
| [Q21](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q21) | Letter substitution coding | Single answer | Apply a letter-substitution code shown on one word to another word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q22](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q22) | Letter-to-number coding | Single answer | Apply a letter-to-digit code shown on two words to a new word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q25](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q25) | Office seating deduction | Single answer | Identify whose office lies to one person's left from the shared layout clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q26](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q26) | Office seating deduction | Single answer | Identify one person's immediate neighbours from the shared layout clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q42](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q42) | Venn-diagram counting | Single answer | Find the number of boys wearing both items of uniform. | Write the total as set sizes minus overlaps, bound the overlap, and add back the triple term when there are three sets. | Lesson 12 |
| [Q43](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q43) | Placement logic deduction | Single answer | Identify where one student studies from the shared placement clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q44](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q44) | Placement logic deduction | Single answer | Identify where one college is located from the shared placement clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q45](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q45) | Placement logic deduction | Single answer | Identify where another student studies from the shared placement clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q46](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q46) | Placement statement check | Single answer | Identify the correct statement about the completed placement. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q47](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q47) | Placement statement check | Single answer | Identify the correct statement about one college in the completed placement. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q48](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q48) | Placement statement check | Single answer | Identify another correct statement about the completed placement. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q61](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q61) | Progress graph comparison | Single answer | Identify the statement that is not correct about a progress graph. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q62](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q62) | Color arrangement counting | Single answer | Count the ways to colour three blocks with no two the same colour. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q63](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q63) | Population graph inference | Single answer | Choose what can be inferred from a population graph over two decades. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q64](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q64) | Graph statement validity | Statement set; choose by code | Decide which statements about population, growth, birth and death rates the graph supports. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q65](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q65) | Dual-scale graph comparison | Single answer | Choose the correct observation about two graphs of the same data on different scales. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q66](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q66) | Figural analogy completion | Single answer | Choose the figure that completes a figural analogy. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q67](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q67) | Graph break-even reading | Single answer | Find the minimum production that avoids a loss from cost and sales figures. | Read cost from one figure and sales revenue from the other at the same number of pieces, after checking the units and scale of both; find the smallest output at which revenue is no less than cost. | Lesson 17 |
| [Q70](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q70) | Figural rotation series | Single answer | Choose the figure at a later stage of a rotation sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q71](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q71) | Population age-group graph | Statement set; choose by code | Decide which statements about two countries' age-group curves are correct. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q72](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q72) | Logical relation deduction | Single answer | Identify who plays best, from positions across a doubles court. | Place the four people on the court from the positional clues, then apply the sibling and best-worst clues. | Lesson 6 |
| [Q73](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q73) | Policy rate graph inference | Single answer | Choose the most likely reason for a pattern of policy-rate changes. | Read the direction and timing of the rate changes, then choose the reason consistent with that pattern. | Lesson 17 |
| [Q74](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q74) | Table data inference | Statement set; choose by code | Decide which inferences about income, growth and tele-density the table supports. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q75](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q75) | Table assumption validity | Statement set; choose by code | Decide which assumptions about tele-density and growth are valid. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q76](../../../solved_pyqs/papers/2018/prelims-csat.md#2018-prelims-csat-q76) | Tax revenue graph inference | Statement set; choose by code | Decide which statements about the composition of tax revenue are correct. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |

## 2019 - 21 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q10](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q10) | Cube partition cuts | Single answer | Count the cubes with exactly one painted face after a cut into two sizes. | Fix the size structure from volume first: with the stated numbers of big and small pieces, find the edge lengths that make the pieces fill the block exactly; place the big cubes using the colour clue and check that they fit; then count painted faces piece by piece, by class, counting pieces rather than unit volumes. | Lesson 15 |
| [Q13](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q13) | Syllogism conclusion check | Statement set; choose by code | Decide which conclusions follow from three categorical statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q14](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q14) | Grid parallelogram count | Single answer | Count the parallelograms formed by two families of parallel lines. | List each figure by size or type exactly once; use the diagonal formula only for a convex polygon. | Lesson 14 |
| [Q20](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q20) | Set overlap deduction | Statement set; choose by code | Decide which "at least" claims about two overlapping groups are correct. | Write the total as set sizes minus overlaps, bound the overlap, and add back the triple term when there are three sets. | Lesson 12 |
| [Q29](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q29) | Statement sufficiency check | Statement set; choose by code | Decide which colouring conditions on a five-floor building are needed or sufficient. | Test each condition alone and in combination against the requirement that consecutive floors differ in colour. | Lesson 2 |
| [Q31](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q31) | Venn diagram deduction | Statement set; choose by code | Decide which overlap conclusions follow from stated activity percentages. | Write the total as set sizes minus overlaps, bound the overlap, and add back the triple term when there are three sets. | Lesson 12 |
| [Q32](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q32) | Logical chain elimination | Statement set; choose by code | Decide which conclusions cannot be drawn from chained statements about sports and vehicles. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q52](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q52) | Venn-diagram counting | Single answer | Count the people who read exactly one of two languages. | Write the total as set sizes minus overlaps, bound the overlap, and add back the triple term when there are three sets. | Lesson 12 |
| [Q54](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q54) | Letter sequence fill | Single answer | Identify the letters that fill the gaps in a repeating letter sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q56](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q56) | Denomination combination count | Single answer | Count the ways to pay a bill using three denominations. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q68](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q68) | Alphabet substitution coding | Single answer | Apply an alternating case rule to a month name. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q70](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q70) | Sequence conditional count | Single answer | Count the terms of a sequence meeting a preceded-and-followed condition. | Scan the sequence term by term and check both conditions at every position. | Lesson 11 |
| [Q71](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q71) | Blood-relation deduction | Statement set; choose by code | Decide which descriptions of one family member are correct. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q72](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q72) | Cube face coloring count | Single answer | Count the distinct ways to paint a cube's faces in two colours. | Classify the colourings by how many faces take each colour, and count the arrangements in each class that differ under rotation. | Lesson 15 |
| [Q73](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q73) | Natural number partition count | Single answer | Count the natural-number triplets with a fixed sum. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q74](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q74) | Symbol substitution evaluation | Single answer | Evaluate an expression after replacing coded operation symbols. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q76](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q76) | Ranking order deduction | Single answer | Find one student's position under a stated condition from shared score clues. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q77](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q77) | Ranking order deduction | Single answer | Find another student's rank under a second condition from the same clues. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q78](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q78) | Ranking order deduction | Single answer | Identify the correct statement under a third condition from the same clues. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q79](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q79) | Weight inequality deduction | Single answer | Identify the correct weight comparison from two inequality statements. | Rewrite each sentence as inequalities, keep only the plain heavier-lighter comparisons they force, chain those in one direction, and accept an option only if it holds for every set of weights consistent with the sentences. | Lesson 7 |
| [Q80](../../../solved_pyqs/papers/2019/prelims-csat.md#2019-prelims-csat-q80) | Weight inequality deduction | Single answer | Identify a second correct weight comparison from the same two statements. | Rewrite each sentence as inequalities, keep only the plain comparisons they force, and settle the heaviest and the lightest as two separate questions, each checked against every set of weights consistent with the sentences. | Lesson 7 |

## 2020 - 12 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q15](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q15) | Letter sequence completion | Single answer | Identify the letters that complete a patterned letter arrangement. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q19](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q19) | Blood-relation deduction | Single answer | Identify the correct statement about a two-generation family of six. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q32](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q32) | Syllogism deduction | Single answer | Decide which of two conclusions follows from two divisibility statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q33](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q33) | Syllogism deduction | Single answer | Decide which of two conclusions follows from two categorical statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q34](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q34) | Sequence pair counting | Single answer | Count the odd numbers in a sequence that are followed by an odd number. | Scan the sequence term by term and check the condition for each adjacent pair. | Lesson 11 |
| [Q35](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q35) | Linear row position count | Single answer | Find the number of people in a row from positions counted from both ends. | Convert every position to a count from one end, place the named people on one line, then total the row. | Lesson 8 |
| [Q36](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q36) | Age-ordering deduction | Single answer | Decide which of three statements are needed to identify the youngest person. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q48](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q48) | Letter-number coding | Single answer | Apply a letter-to-number code inferred from two examples. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q49](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q49) | Letter analogy series | Single answer | Find the missing term of a four-letter analogy. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q52](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q52) | Table rate comparison | Single answer | Identify the period with the highest natural growth from birth and death rates. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q60](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q60) | Denomination subset counting | Single answer | Count the distinct sums from at least three of five denominations. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q67](../../../solved_pyqs/papers/2020/prelims-csat.md#2020-prelims-csat-q67) | Constrained permutation count | Single answer | Count the arrangements of five letters with fixed first and last letters. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |

## 2021 - 18 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q10](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q10) | Syllogism conclusion selection | Single answer | Decide which of two "certainly" conclusions follows from three statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q15](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q15) | Syllogism conclusion selection | Single answer | Decide which of two conclusions follows from three categorical statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q17](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q17) | Mirror-image consonant count | Single answer | Count the capital consonants whose mirror images differ from the originals. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q19](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q19) | Digit-sum integer count | Single answer | Count the integers in a range whose digits sum to a stated value. | Fix the leading digit for each part of the range and count the digit combinations with the required sum. | Lesson 10 |
| [Q25](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q25) | Multi-attribute classification | Single answer | Identify the books that meet three attribute conditions together. | Tabulate each book against the three attributes and keep only the books that meet all three conditions. | Lesson 9 |
| [Q27](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q27) | Matrix trend missing entry | Single answer | Find the missing entry of a matrix that follows a row-wise trend. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q28](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q28) | Dual-sequence missing entry | Single answer | Find one entry of a second sequence built by the rule of a given sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q35](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q35) | Venn set overlap range | Single answer | Determine the possible number of people in the overlap of two groups. | Write the total as set sizes minus overlaps, bound the overlap, and add back the triple term when there are three sets. | Lesson 12 |
| [Q40](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q40) | Alphabet reversal position coding | Single answer | Identify a letter at a stated position after blockwise reversal of the alphabet. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q45](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q45) | Table run-rate comparison | Single answer | Identify the fastest scorer across two innings from runs and balls. | Name the quantity asked (level, change, share, points or relative change), name its base, then compute. | Lesson 16 |
| [Q46](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q46) | Fractional set deduction | Single answer | Identify the statement certainly correct from four fractional shares of one village. | Write the total as set sizes minus overlaps, bound the overlap, and add back the triple term when there are three sets. | Lesson 12 |
| [Q49](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q49) | Multi-conclusion syllogism | Single answer | Decide which of four conclusions follow from two categorical statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q56](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q56) | Letter-substitution coding | Single answer | Apply a letter-substitution code shown on one word to another word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q64](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q64) | Chessboard diagonal count | Single answer | Count the ways to choose six consecutive squares along a diagonal of a chessboard. | List the diagonals in each of the two diagonal directions by length, count the runs of six consecutive squares that fit on each diagonal long enough, and add across both directions. | Lesson 14 |
| [Q65](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q65) | Series blank-fill pattern | Single answer | Choose the letters that fill six blanks in a patterned series. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q66](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q66) | Restricted digit arrangement | Single answer | Count distinct numbers above a threshold from a multiset of digits. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q69](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q69) | Non-consecutive selection count | Single answer | Count the selections of three people in a row with no two adjacent. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q74](../../../solved_pyqs/papers/2021/prelims-csat.md#2021-prelims-csat-q74) | Pie-chart sector angle | Single answer | Find a central angle on a pie chart from given percentage shares. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |

## 2022 - 18 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q10](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q10) | Digit row arrangement count | Single answer | Count arrangements of nine digits in three rows under a first-row restriction. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q16](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q16) | Alphabet reversal coding | Single answer | Apply a reversed-alphabet code to a word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q17](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q17) | Elimination match counting | Single answer | Count the matches in a knockout tournament with no draws. | Relate every match to the number of entrants it eliminates, then count the eliminations required. | Lesson 13 |
| [Q18](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q18) | Odd digit counting | Single answer | Count three-digit numbers with distinct odd digits divisible by a stated number. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q24](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q24) | Letter arrangement counting | Single answer | Count the arrangements of five letters with a fixed gap between two of them. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q27](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q27) | Route combination counting | Single answer | Count the ways to travel between two places by direct and indirect roads. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q29](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q29) | Letter series position | Single answer | Identify the letter at a stated position of a growing letter series. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q30](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q30) | Queue minimum size | Single answer | Find the minimum queue size consistent with stated gaps and counts. | Place the three people on a line in each order allowed by the gaps and counts, and keep the arrangement with the fewest people. | Lesson 13 |
| [Q36](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q36) | Blood relation deduction | Single answer | Identify the correct relation in a six-member family. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q38](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q38) | Statement-set syllogism | Single answer | Decide which of four conclusions follow from two statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q39](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q39) | Multi-statement syllogism | Single answer | Decide which of three conclusions follow from three statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q40](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q40) | Circular seating arrangement | Single answer | Identify the definitely correct statement about an eight-seat round table. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q55](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q55) | Constrained PIN enumeration | Single answer | Find the maximum attempts to find a PIN under ordering and gap rules. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q56](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q56) | Circle inscribed triangle count | Single answer | Count the right-angled triangles with a diameter as one side among equally spaced points on a circle. | Count the diameters available among the points, then count the third vertices that complete a triangle with each diameter. | Lesson 14 |
| [Q70](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q70) | Pie chart percentage | Single answer | Find one item's percentage share from the other sectors' angles. | Read the title, unit, scale and both axes; convert shares to values through the base; weight before summing. | Lesson 17 |
| [Q76](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q76) | Constrained password count | Single answer | Count passwords formed from a digit, a vowel and a consonant under position rules. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q77](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q77) | Grid row arrangement count | Single answer | Count arrangements of cups in a square grid so that each row has at least one of one kind. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q79](../../../solved_pyqs/papers/2022/prelims-csat.md#2022-prelims-csat-q79) | Form constraint number count | Single answer | Count the numbers of a stated decimal form with distinct non-zero digits. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |

## 2023 - 25 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q4](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q04) | Worst-case shoe draw for a pair of one colour | Single answer | Find the maximum number of picks needed to be sure of a pair of one colour. | Write the sample space, use conditional fractions without replacement, or take the worst case that avoids the target and add one. | Lesson 13 |
| [Q5](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q05) | Score partition counting | Single answer | Count the ways to make a total score from three kinds of scoring shots. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q6](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q06) | Derangement possibility check | Statement set; choose by code | Decide which statements about letters and envelopes are correct. | Count the arrangements by the number of letters in correct envelopes, then test each statement. | Lesson 13 |
| [Q18](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q18) | Interior cube count | Single answer | Count the cubes in a block that are surrounded on every side. | Remove the outer shell of the block and count the cubes that are left inside. | Lesson 15 |
| [Q19](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q19) | Position-constrained permutation | Single answer | Count the rearrangements of a digit string under parity-position rules. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q24](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q24) | Symbol operation decode | Single answer | Find the value of a coded three-number operation from three examples. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q30](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q30) | Collinearity-aware triangle count | Single answer | Count the triangles formed from six points placed on the sides of a square. | Count all triples of points, then subtract the triples that lie on one side of the square. | Lesson 14 |
| [Q36](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q36) | Worst-case colour group draw | Statement set; choose by code | Decide which statements about guaranteed draws from six colours are correct. | Write the sample space, use conditional fractions without replacement, or take the worst case that avoids the target and add one. | Lesson 13 |
| [Q37](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q37) | Letter-shift cipher decode | Single answer | Apply a letter-shift code shown on one word to another word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q38](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q38) | Statement-based age ranking | Single answer | Count the statements needed to determine the oldest person or persons. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q39](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q39) | Family-relation statement sufficiency | Single answer | Decide which combination of statements suffices to answer a family question. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q40](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q40) | Prime-group odd-one-out | Single answer | Identify the group of four numbers that differs from the other groups. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q48](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q48) | Circular consecutive selection count | Single answer | Count the selections of consecutive objects arranged in a circle. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q54](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q54) | Circular pass-sequence return | Single answer | Find the number of passes before an object returns in a circle under a growing step. | Track the holder after each pass by its position around the circle until the object returns. | Lesson 11 |
| [Q55](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q55) | Sequence middle term | Single answer | Identify the middle term of a letter sequence with growing repetitions. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q65](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q65) | Integer-constraint solution count | Single answer | Count the integer mark combinations that give a stated total across four papers. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q66](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q66) | Adjacent-colour stripe count | Single answer | Count the stripe colourings with no two adjacent stripes alike. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q68](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q68) | Constrained assignment count | Single answer | Count the task assignments under two restrictions. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q69](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q69) | Weighing-coin optimisation | Statement set; choose by code | Decide which statements about buying and weighing a stated mass with given coins are correct. | Treat buying and weighing as different tasks, find the fewest coins each task needs, then test each statement. | Lesson 13 |
| [Q70](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q70) | Coded relational chain deduction | Single answer | Decide which conclusions follow from a statement written in coded comparison symbols. | Decode each symbol into an inequality, chain the inequalities, and test each conclusion against the chain. | Lesson 6 |
| [Q75](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q75) | Repeating pattern gap fill | Single answer | Choose the letters that complete a repeating pattern. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q77](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q77) | True-false logic deduction | Statement set; choose by code | Decide which conclusions follow when a stated number of statements are true. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q78](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q78) | Conditional logic conclusion | Statement set; choose by code | Decide which conditional conclusions follow from a set of implications. | Write each link as an arrow, add its contrapositive, then chain the arrows; test a claim by assuming its negation. | Lesson 1 |
| [Q79](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q79) | Painted cuboid partition count | Statement set; choose by code | Decide which statements about the faces of small cubes cut from a painted cuboid are correct. | Cut into unit cubes, locate the cubes with exactly two painted faces on the edges, identify the two colours meeting along each edge, count the interior cubes on each edge, then test each statement separately. | Lesson 15 |
| [Q80](../../../solved_pyqs/papers/2023/prelims-csat.md#2023-prelims-csat-q80) | Reverse alphabetical position count | Single answer | Count the letters that keep their positions when a word's letters are sorted in reverse. | Sort the letters in the stated order and compare each position with the original word. | Lesson 10 |

## 2024 - 12 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q24](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q24) | Sequence completion | Single answer | Choose the letters that complete a repeating pattern. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q45](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q45) | Digit-frequency counting | Single answer | Count the occurrences of one digit in page numbers up to a stated page. | Count the digit separately in the units, tens and hundreds places across the range. | Lesson 10 |
| [Q48](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q48) | Alphametic addition | Single answer | Determine one letter's digit in a two-number alphametic sum. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q49](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q49) | Constrained-triplet count | Single answer | Count triplets from a small set satisfying a chained inequality. | Decide whether the selection is ordered, count by cases on the restricted member, and check a small case by listing. | Lesson 11 |
| [Q56](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q56) | Multi-turn direction sense | Single answer | Find the initial direction from a multi-turn walk and the final bearing. | For a walk, track the heading after every turn and sum the signed displacements; for a network, treat each link exactly as stated (one-way or two-way) and test each claim against every route. | Lesson 5 |
| [Q57](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q57) | Rotational direction sense | Single answer | Find the final facing direction after turns including a stated clockwise angle. | For a walk, track the heading after every turn and sum the signed displacements; for a network, treat each link exactly as stated (one-way or two-way) and test each claim against every route. | Lesson 5 |
| [Q58](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q58) | Conclusion validity | Single answer | Decide which of two conclusions follows from a statement about production. | Test each conclusion against the statement alone; accept it only if it must hold, not merely because it is plausible or generally true. | Lesson 2 |
| [Q74](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q74) | Implication consistency | Single answer | Identify the ordered pair of statements where the first implies the second within an either-or claim. | Write each link as an arrow, add its contrapositive, then chain the arrows; test a claim by assuming its negation. | Lesson 1 |
| [Q75](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q75) | Operator substitution | Single answer | Evaluate an expression after simultaneous replacement of operators. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q77](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q77) | Alphabetic-number coding | Single answer | Apply a letter-to-number code inferred from two examples. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q78](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q78) | Letter-rearrangement coding | Single answer | Apply a rearrangement code inferred from two examples. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q80](../../../solved_pyqs/papers/2024/prelims-csat.md#2024-prelims-csat-q80) | Coded-value constraints | Single answer | Determine a combination of coded values from two equations and a value set. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |

## 2025 - 12 items

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q8](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q08) | Month-pattern sequence | Single answer | Identify the two missing terms of a month sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q29](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q29) | Alphametic subtraction | Single answer | Count the possible digit pairs in an alphametic subtraction under constraints. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q30](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q30) | Letter-pattern completion | Single answer | Choose the letters that complete a patterned sequence. | Find the rule that holds for every term or figure, verify it on all of them, then apply it to the blank. | Lesson 3 |
| [Q38](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q38) | Coded-operator arrangement | Single answer | Choose the operator sequence that makes a stated equation true. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q49](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q49) | Suspect-statement logic | Single answer | Identify the guilty suspect from statements under a one-guilty condition. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q50](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q50) | Tournament-score logic | Statement set; choose by code | Decide which statements about match results follow from tournament points and goals. | Translate the points into wins, draws and losses for each team, then test each statement against every consistent set of results. | Lesson 7 |
| [Q55](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q55) | Family-relation deductions | Count of definitely true statements | Count the statements about a family that are definitely true. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q56](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q56) | Multiplicative-letter code | Single answer | Apply a multiplicative letter code inferred from three examples. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q57](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q57) | Letter-digit substitution | Single answer | Apply a letter-to-digit code inferred from two words. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q58](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q58) | Constrained-digit arrangement | Single answer | Count five-digit numbers satisfying stated digit relations. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q65](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q65) | Direction-network distance | Single answer | Find the distance travelled along a road network with stated positions. | For a walk, track the heading after every turn and sum the signed displacements; for a network, treat each link exactly as stated (one-way or two-way) and test each claim against every route. | Lesson 5 |
| [Q66](../../../solved_pyqs/papers/2025/prelims-csat.md#2025-prelims-csat-q66) | Numeric-cube code | Single answer | Apply a numerical code inferred from two examples. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |

## 2026 - 21 items (provisional; no key stated)

| Question | Family (neutral label) | Directive | Demand | Approach | Teaching home |
|---|---|---|---|---|---|
| [Q9](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q09) | Constrained-word permutation count | Single answer (provisional) | Count the arrangements of a word's letters when one letter must be followed by another. | Decide whether order matters, fill the restricted slot first, divide by repeat factorials, or count the complement. | Lesson 10 |
| [Q14](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q14) | Circular-seating arrangement | Single answer (provisional) | Count the persons passed before meeting a target at a round table under given clues. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q15](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q15) | Painted-region pattern count | Single answer (provisional) | Count the distinct painted patterns on a fixed rectangular top. | List the possible placements of the painted portions and count those that look different from above when the top cannot be turned. | Lesson 15 |
| [Q23](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q23) | Weighing-combination count | Single answer (provisional) | Count the ways to make a stated mass under limits on one weight. | For each allowed count of the smallest weight, list the combinations of the larger weights that complete the total, then add the cases. | Lesson 13 |
| [Q33](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q33) | Ranking-order logic | Statement set; choose by code (provisional) | Decide which conditional statements about ranks follow from the clues. | Convert each comparison into an ordered chain, count positions from the stated end, and test every tie. | Lesson 7 |
| [Q34](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q34) | Segment-matching puzzle | Statement set; choose by code (provisional) | Decide which placements on two coloured rods are possible. | Set up one grid with a row per entity, enter the definite pairs, eliminate by row and column, and recheck every clue. | Lesson 9 |
| [Q35](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q35) | Group-seating constraints | Statement set; choose by code (provisional) | Decide which statements about car groupings are correct. | Fix the most constrained placement first, use one anchor for a circle, then test every clue on the completed layout. | Lesson 8 |
| [Q36](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q36) | Statement-implication logic | Statement set; choose by code (provisional) | Decide which statements follow from a set of conditional relations. | Write each link as an arrow, add its contrapositive, then chain the arrows; test a claim by assuming its negation. | Lesson 1 |
| [Q44](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q44) | Blood-relation tree | Single answer (provisional) | Identify one person's relation to another in a small family. | Build a labelled relation graph from the clue that fixes most, then read each relation along its path. | Lesson 6 |
| [Q48](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q48) | Transitive-colour syllogism | Statement set; choose by code (provisional) | Decide which derived statements follow from a chain of "every" statements. | Draw the containment for each premise, then search for one counter-diagram; for truth-teller items follow each assumption to its consequence. | Lesson 2 |
| [Q51](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q51) | Odd-item weighing logic | Single answer (provisional) | Find the minimum number of balance uses that identifies a lighter item with certainty. | Split the items into groups at each use of the balance so that every outcome narrows the candidates, and count the uses in the worst case. | Lesson 13 |
| [Q56](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q56) | Direction turns and distance | Single answer (provisional) | Find the shortest distance and final facing direction after a walk with turns. | For a walk, track the heading after every turn and sum the signed displacements; for a network, treat each link exactly as stated (one-way or two-way) and test each claim against every route. | Lesson 5 |
| [Q67](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q67) | Letter-code decoding | Single answer (provisional) | Apply a letter code shown on one word to another word. | Extract the rule from every given pair, verify it on each letter or symbol, then apply it; for alphametics fix the carries first. | Lesson 4 |
| [Q70](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q70) | Weighted-score data table | Single answer (provisional) | Find a stated quantity from component scores and their weights. | Multiply each component score by its stated weight, sum the products for each candidate, then answer the exact quantity the stem asks for. | Lesson 16 |
| [Q71](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q71) | Statement-relationship logic | Statement set; choose by code (provisional) | Decide which stated relationships among three statements are correct. | Take the proposed relationships one at a time; for each, ask whether one statement bears on the exact point of the other and, if it were true, whether it would support the other, weaken it or leave it unrelated; read the code only after every relationship has been judged. | Lesson 2 |
| [Q72](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q72) | List matching: category to style | List matching; choose by code (provisional) | Match each relationship category with a style of message. | Fix the pairings you are surest of first, strike every code that contradicts them, then confirm the remaining pairs. | Lesson 9 |
| [Q73](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q73) | List matching: item to purpose | List matching; choose by code (provisional) | Match each item with its purpose. | Fix the pairings you are surest of first, strike every code that contradicts them, then confirm the remaining pairs. | Lesson 9 |
| [Q74](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q74) | Multi-statement action selection | Statement set; choose by code (provisional) | Decide which actions are most appropriate for resolving a workplace disagreement. | Judge each action against the stated objective; keep those that serve it without breaking a constraint, then read the code. | Lesson 18 |
| [Q75](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q75) | List matching: category to example | List matching; choose by code (provisional) | Match each category with an example. | Fix the pairings you are surest of first, strike every code that contradicts them, then confirm the remaining pairs. | Lesson 9 |
| [Q76](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q76) | Multi-statement item selection | Statement set; choose by code (provisional) | Decide which items belong on a questionnaire for a stated objective. | Judge each item against the stated objective of the form; keep those that serve it, then read the code. | Lesson 18 |
| [Q77](../../../solved_pyqs/papers/2026/prelims-csat.md#2026-prelims-csat-q77) | Statement evaluation: a type of letter | Statement set; choose by code (provisional) | Decide which statements about a type of letter are correct. | Judge each numbered statement on its own against the term's stated meaning and usage, then read the code; no answer or pairing is taught here. | Lesson 2 |


# CUMULATIVE MCQS

These six items each join two or more lessons, and none of them can be finished with one lesson's method alone. Before you look at the options, write the rule you expect to use and the lessons it comes from. Then work the item and check your route against the explanation.

**MCQ 45**

Nine cards lie face down: five are marked with a circle and four with a star. Four cards are dealt at random, every set of four cards being equally likely. What is the chance, as a percentage, that the four cards include exactly two stars?

- A. About 48%
- B. Just over 64%
- C. Just under 8%
- D. 37.5%

**MCQ 45 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** A hand of four cards has no order, so the favourable and total counts are both selections (Lesson 11), and the chance is favourable over total for equally likely hands (Lesson 13). Favourable hands: two of the four stars, C(4, 2) = 6, with two of the five circles, C(5, 2) = 10, giving 60. All hands: C(9, 4) = 126. The chance is 60/126 = 10/21 = 0.476, about 48%. A sequence check gives the same value: one fixed order of deals gives 5/63, and the two stars can take C(4, 2) = 6 of the four deal positions, so 6 x 5/63 = 10/21.
- **B — Incorrect:** This counts "at least two stars" instead of "exactly two". It adds the hands with three stars, C(4, 3) x 5 = 20, and the one hand of four stars to the 60, giving 81/126 = 9/14 = 64.3%. The word "exactly" was not labelled before counting (Lesson 16: answer the exact quantity asked).
- **C — Incorrect:** This multiplies the conditional fractions for one fixed order only, star, star, circle, circle: (4/9)(3/8)(5/7)(4/6) = 5/63 = 7.9%. A hand does not depend on the order in which its cards were dealt, so the six orders that place two stars among four deals all count (Lesson 10).
- **D — Incorrect:** This treats each dealt card as equally likely to show a star or a circle, as if the chance were one half per card: C(4, 2)/2^4 = 6/16 = 37.5%. The two marks are not equally numerous, and the deck shrinks as cards are dealt, so the cards are not fifty-fifty; equal likelihood belongs to the 126 hands, not to the two marks (Lesson 13, equal likelihood).

**MCQ 46**

A team of three is chosen from five officers P, Q, R, S and T. A team is valid if it obeys all three conditions: if P is chosen, Q must be chosen; R and S are not both chosen; if T is not chosen, S must be chosen. Which one of the following must be true?

- A. R cannot be chosen
- B. Every valid team includes Q
- C. No valid team includes both S and T
- D. Exactly one valid team includes both P and Q

**MCQ 46 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** This reads "if T is not chosen, S must be chosen" as "S must be chosen", then uses the R-and-S condition to shut R out. Under that misreading the only teams are P, Q, S and Q, S, T, and neither contains R. Under the stated conditions the team Q, R, T is valid, so R can be chosen.
- **B — Correct:** Test the claim by assuming its denial (Lesson 1). Suppose Q is left out. The contrapositive of "P -> Q" is "not Q -> not P", so P is out as well. The three members must then be R, S and T, but R and S are not both allowed: a contradiction. So Q is in every valid team. Listing the cases by the restricted member confirms it (Lesson 11, selections by cases): the valid teams are P, Q, S; P, Q, T; Q, R, T; and Q, S, T, and all four contain Q.
- **C — Incorrect:** This reads the third condition as "exactly one of S and T is chosen". Under that reading the teams are P, Q, S; P, Q, T; and Q, R, T, and none has both S and T. The stated condition forbids only leaving both out, so the team Q, S, T is valid.
- **D — Incorrect:** This reads "R and S are not both chosen" as "exactly one of R and S is chosen". That reading removes the team P, Q, T and leaves P, Q, S as the only team with both P and Q. The stated condition also allows neither R nor S, so P, Q, S and P, Q, T are both valid: two such teams, not one.

**MCQ 47**

Three wards are scored out of 100 on three indicators. The final score weights sanitation at 40%, water supply at 35% and citizen feedback at 25%.

| Ward | Sanitation | Water supply | Citizen feedback |
|---|---:|---:|---:|
| Rampur | 78 | 82 | 58 |
| Hari Nagar | 50 | 78 | 90 |
| Lal Bagh | 82 | 50 | 90 |

Which ward ranks first on the final score, and by how many points does it lead the ward ranked second?

- A. Lal Bagh, by about 1.3 points
- B. Hari Nagar, by 1.8 points
- C. Rampur, by 1.6 points
- D. Rampur, by about 0.5 points

**MCQ 47 — Answer and explanation**

**Correct answer: C**

- **A — Incorrect:** This adds the three indicators and divides by three, ignoring the weights (Lesson 17, weighted scores). The simple averages are Rampur 72.67, Hari Nagar 72.67 and Lal Bagh 74.00, so Lal Bagh would lead by about 1.33. The stem defines the final score with weights, and sanitation carries the most weight.
- **B — Incorrect:** This attaches the 40% weight to citizen feedback and the 25% weight to sanitation. Hari Nagar then scores 0.25 x 50 + 0.35 x 78 + 0.4 x 90 = 75.8 against Lal Bagh's 74.0, a lead of 1.8. Each weight must sit on its own indicator.
- **C — Correct:** Multiply each indicator by its weight before adding; the weights sum to 100%, so no further division is needed (Lesson 17). Rampur: 0.4 x 78 + 0.35 x 82 + 0.25 x 58 = 31.2 + 28.7 + 14.5 = 74.4. Lal Bagh: 32.8 + 17.5 + 22.5 = 72.8. Hari Nagar: 20.0 + 27.3 + 22.5 = 69.8. The order is Rampur, Lal Bagh, Hari Nagar (Lesson 7), and the lead over the second-placed ward is 74.4 - 72.8 = 1.6 points (Lesson 16: answer the exact quantity asked).
- **D — Incorrect:** This applies the weights correctly and then divides each weighted total by three, as if it were still a sum of three marks. Rampur becomes 24.8 and Lal Bagh 24.27, a lead of about 0.53. Weights that add to 100% already produce an average, so the extra division shrinks every gap by a factor of three.

**MCQ 48**

A grandfather G, his son S, his daughter D, S's wife W, and S and W's two children, a boy B and a girl K, sit in a row of six seats, all facing north. S and D are brother and sister, S and W are the only married couple, and no one else in the group is related by marriage.

1. G sits at one end of the row.
2. No one sits next to his or her own brother or sister.
3. W sits next to both of her children.
4. D sits immediately to the right of her father.
5. S does not sit next to his wife.
6. K does not sit next to D.

Which one of the following is correct?

- A. The boy sits beside his father
- B. The grandfather sits at the east end of the row
- C. The mother sits beside her sister-in-law
- D. The boy sits between his aunt and his mother

**MCQ 48 — Answer and explanation**

**Correct answer: D**

- **A — Incorrect:** This drops the last clue. Without "K does not sit next to D", two seatings survive from west to east, G D B W K S and G D K W B S, and the second puts the boy beside his father. The last clue removes it, because K would then sit next to D, her aunt. In the only seating left, the boy sits third and his father sixth.
- **B — Incorrect:** This reverses right and left for a row facing north (Lesson 8). Placing D on G's west side forces G to the east end and gives S K W B D G. Facing north, a person's right is the east side, so D must sit east of G, and G must be at the west end.
- **C — Incorrect:** This reads "W sits next to both of her children" as "W sits next to one of her children" and stops at the first seating found, G D W B S K, where W sits beside D. With the clue read as stated, W must have a child on each side, so she cannot sit beside D.
- **D — Correct:** Build the family graph first (Lesson 6): D is S's sister, so she is the children's aunt; W is the children's mother and D's sister-in-law. Then seat the row (Lesson 8). Facing north, right is east, so D sits immediately east of G, and G, at an end, must be at the west end: G, D in seats 1 and 2. W needs a child on each side, so B, W, K or K, W, B occupy three consecutive seats among 3 to 6, and S takes the remaining seat. S cannot sit in seat 3 beside his sister, and he cannot sit next to W, so the block fills seats 3 to 5 and S sits in seat 6. K cannot sit next to D in seat 2, so K is in seat 5 and B in seat 3. The only seating is G, D, B, W, K, S, and the boy sits between his aunt (seat 2) and his mother (seat 4).

**MCQ 49**

In a district, 55% of farmers use drip irrigation, 60% use solar pumps, and 8% use neither. Among the farmers who use solar pumps, what percentage also use drip irrigation?

- A. About 38%
- B. 23%
- C. Just under 42%
- D. 25%

**MCQ 49 — Answer and explanation**

**Correct answer: A**

- **A — Correct:** Remove the 8% who use neither first: 92% use at least one (Lesson 12). Both = 55 + 60 - 92 = 23% of all farmers. The question's base is the solar-pump users (Lesson 16: name the base of every percentage), so the share is 23/60 = 0.383, about 38%.
- **B — Incorrect:** This finds the overlap correctly, 23, but reports it as a share of all farmers. The stem asks "among the farmers who use solar pumps", so the base must be the 60%, and the 23 farmers in every 100 who use both are 23 out of every 60 solar-pump users, which is 38.3%, not 23%.
- **C — Incorrect:** This divides the overlap by the drip-irrigation group: 23/55 = 0.418, just under 42%. That is the share of drip users who also use solar pumps, a question with a different base.
- **D — Incorrect:** This ignores the 8% who use neither and takes the overlap as 55 + 60 - 100 = 15%, then divides by 60 to get 25%. Farmers who use neither sit outside both circles, so the union is 92%, not 100%, and the overlap is 23%.

**MCQ 50**

Village Q is 3 km north of village P. Village R is 4 km east of Q. Village S is 2 km south of R, and village T is 6 km west of S. All distances in the options are straight-line distances. Which one of the following is correct?

- A. S is farther from P than R is
- B. R lies 5 km away from P
- C. T lies 2 km due west of P
- D. Q is nearest to P

**MCQ 50 — Answer and explanation**

**Correct answer: B**

- **A — Incorrect:** This compares the lengths of the routes along the roads, P to Q to R to S (9 km) against P to Q to R (7 km), instead of the straight-line distances (Lesson 5: path length is not displacement). S is 4 km east and 1 km north of P, so its distance is the square root of 17, about 4.12 km, which is less than R's 5 km.
- **B — Correct:** Put P at the origin with east and north positive (Lesson 5). Q is (0, 3), R is (4, 3), S is (4, 1) and T is (-2, 1). R's distance from P is the square root of (4 x 4 + 3 x 3) = 5 km. Ordering all four distances (Lesson 7, comparison chains) gives T about 2.24 km, Q 3 km, S about 4.12 km and R 5 km, which also rules out every other option.
- **C — Incorrect:** This keeps the east-west total, 4 - 6 = -2, and drops the north-south total, 3 - 2 = 1. T is 2 km west and 1 km north of P, about 2.24 km away and not due west.
- **D — Incorrect:** This treats the village reached in one leg as the nearest. Q is 3 km from P, but T, though reached last, is only about 2.24 km from P, so T is the nearest.

# TIMED-SET PRACTICE AND SCORING RUBRIC

The fifty items now become seven timed sets of eight. No new items are added here. The point is to practise the two skills the lessons cannot give you one at a time: choosing which item to attack first, and stopping an item before it eats the time of the next.

## The seven sets

| Set | Items | Lessons drawn on | Suggested set budget |
|---|---|---|---|
| Set 1 | 1, 2, 3, 4, 5, 6, 7, 8 | Lessons 1, 2, 3 | about 9 min 15 s |
| Set 2 | 9, 10, 11, 12, 13, 14, 15, 16 | Lessons 4, 5, 6, 7 | about 8 min 30 s |
| Set 3 | 17, 18, 19, 20, 21, 22, 23, 24 | Lessons 7, 8, 9, 10 | about 12 min 30 s |
| Set 4 | 25, 26, 27, 28, 29, 30, 31, 32 | Lessons 10, 11, 12, 13 | about 11 min 30 s |
| Set 5 | 33, 34, 35, 36, 37, 38, 39, 40 | Lessons 14, 15, 16, 17 | about 10 min 45 s |
| Set 6 | 41, 42, 43, 44, 45, 46, 47, 48 | Lessons 17 and 18, and cumulative items 45 to 48 | about 10 min 45 s |
| Set 7 | 49, 50, 1, 2, 3, 4, 5, 6 | Cumulative items 49 and 50, and Lessons 1, 2, 3 | about 10 min 45 s |

Each set budget is the sum of the per-item budgets in the next table. Set 7 deliberately returns to the opening items, so that you meet the implication and series rules again after the counting and data lessons, when the earlier rules have had time to fade.

## Time budgets by item type

These are practice budgets drawn from the length of each lesson's method, not official figures. They tell you when an item has run over, not how fast you must be on day one.

| Item type | Lessons | Budget per item | Why this budget |
|---|---|---|---|
| Implication chains, syllogisms, truth-teller sets | 1, 2 | 75 s | One arrow list or one counter-diagram, then one assumed denial or one branch score each |
| Number, letter and figure series | 3 | 60 s | Differences, ratios, known sequences in a fixed order; the verification pass takes the last 15 s |
| Coding, decoding, alphametics | 4 | 75 s | Positions under every letter of every pair; units column first for alphametics |
| Directions and directed networks | 5 | 60 s | One heading per turn and two signed totals; one removal test for "every route" claims |
| Family graphs | 6 | 60 s | One labelled graph with generation rows and sex markers |
| Ranking and comparison chains | 7 | 60 s | One ladder with both-end numbers, or one chain written in one direction |
| Seating: placement questions | 8 | 120 s | Frame, anchor, strongest clue, then a full recheck of every clue |
| Seating: counting questions | 8 | 75 s | Anchor, glued block or gap method, no halving unless stated |
| Logic grids and matching | 9 | 120 s | One grid per attribute pair; finishing the grid is part of the item |
| Arrangements and selections | 10, 11 | 90 s | Order test, slot diagram or case list by the restricted member, then a complement check |
| Sets and overlap | 12 | 75 s | Fill regions from the centre outward; check that they sum to the total |
| Probability, worst cases, weighing | 13 | 90 s | Listed space or conditional fractions; failing hand plus one; thirds for a balance |
| Plane-figure counting | 14 | 75 s | A written size list or a formula whose condition you have stated |
| Cube and solid counting | 15 | 75 s | Adjacency list from every view, or the four-class table with a total check |
| Data interpretation | 16, 17 | 90 s | Label strip first, then the base, then the arithmetic |
| Decision scenarios | 18 | 45 s | Four boxes and the elimination screen; no arithmetic, but every option checked |
| Cumulative items | 45 to 50 | 105 s | Two rules from two lessons, plus the trap the join creates |

## The three-pass routine

**Pass 1: easy items (about 40% of the set budget).** Read every stem once. Attempt at once only those items whose method you can name in one line before reading the options: a single arrow with its contrapositive, a series whose gaps you can see, a position-line code, a ranking with both-end numbers, a single pie conversion, a decision item where one option plainly breaks a stated constraint. Mark every other item with the type it belongs to and move on. Do not start any setup-heavy item in this pass.

**Pass 2: structured items (about 45% of the set budget).** Return to the marked items in order of setup cost, cheapest first. These are items that need a drawn structure before any option can be judged: a seat frame, a logic grid, a slot diagram, a Venn diagram filled from the centre, a family graph, a cube adjacency list. Draw the structure once and use it for every option. If an item reaches its budget and the structure is still not settled, write the item number and the stage you reached ("grid half filled", "two seatings survive") and leave it.

**Pass 3: checks (about 15% of the set budget).** Use the remaining time in this order. First, run the lesson check on every item from pass 2: reread every clue against the finished seating or grid (Lessons 8 and 9), recompute the complement (Lessons 10, 11, 13), check that the regions add to the total (Lessons 12 and 15). Second, reread the stem of every data item and confirm that the label of your number matches the label asked (Lessons 16 and 17). Third, only if time is left over, return to a left item at the stage you wrote down.

## Two retry gates

**Core gate: six items in nine minutes.** Work these six without notes, in nine minutes, and diagnose each miss with a code from the next table before you look at the answer.

1. Seven people sit round a table; rotations are the same and mirror images are different. How many seatings? (720.)
2. How many four-digit numbers can be formed from 0, 2, 5, 7 and 9 without repetition? (96: 4 choices for the first digit, then 4 x 3 x 2.)
3. Of 80 members, 50 swim and 45 cycle. What is the least possible number who do both? (15.)
4. A bag holds 5 red and 3 green counters. Two are drawn in sequence without replacement. What is P(green then green)? (3/28 = (3/8) x (2/7).)
5. A share rises from 16% to 20%. State the change in points and the relative change. (+4 points; +25%.)
6. One seating, coding or data item of your choice from Sets 1 to 5.

The usual misses on this gate are a rotation or reflection double-counted (code C or A), a leading zero or a repetition rule lost (R), one overlap assumed instead of its lower and upper bounds (C), a without-replacement fraction left unchanged (A), and a share or points measure confused (R or X). Pass when, after a 20-minute gap, you score 6 of 6 in nine minutes with no C or R code. Otherwise redo the lesson's worked example for each miss and retry with fresh numbers.

**Optional Advanced gate: ten items in fifteen minutes.** Work items 41 to 50 in fifteen minutes. A probability retry must show its listed space or its conditional fraction; a data retry must label the unit and the quantity asked. Advance at 9 of 10 with no conditional-probability, overlap-scope or multi-solution arrangement error; otherwise rebuild the table or diagram for each miss and take a fresh timed set.

Both gates are practice frames for you to set and adjust. They are not official standards.

## Error codes and their repairs

After every set, give each item you missed or guessed one code. Use the first code that explains the miss; if two apply, write down the earlier one in this list, because it is the root cause.

| Code | Meaning | What it looks like | Repair |
|---|---|---|---|
| C | Concept | You used a rule that is false: a converse, a halving for mirror images, a subtracted triple overlap, an angle read as a percent | Return to the lesson's rule section and its paired confusions; write the rule and its failure condition in one line each; redo the item from a blank page |
| A | Application | You knew the rule but applied it to the wrong structure: slot-filling a selection, chaining arrows whose ends do not match, the right leader but the wrong runner-up | Name the structure before the method: "order matters or not", "same end or opposite ends", "share or level"; redo the item and one fresh retry prompt from the remediation table |
| X | Calculation | The method was right, the arithmetic was not: a dropped carry, a 7! written for 6!, a wrong total | Recompute with the check the lesson gives (sum of regions, complement, reverse substitution); keep a written intermediate line for every product |
| R | Reading | You answered a different question: "at least" for "exactly", path length for displacement, all households for a stated subgroup, a "not" missed | Underline the quantity word and its base in the stem before the next attempt; write the label first, as in the label strip |
| T | Time | You ran out of time, or spent more than twice the budget on one item | Move the item type to pass 2 next time; practise only its setup stage until it fits the budget |
| G | Guess | You picked without a derivation, whether the pick was right or wrong | Treat a right guess as a miss; redo the item with the full method; note which step you could not take |

## The marks-per-minute rubric

Score each set with a practice rule that you set yourself. The simplest is: each right item earns 1 practice mark, a blank earns 0, and a wrong item loses w practice marks, where w is a deduction you fix for your practice. This is your own practice frame, not the scheme of any real paper; for a real paper, read the marking rules from the official notice for that year.

- Net practice marks = (right items) - w x (wrong items).
- Minutes used = the clock time from the first read to the end of pass 3.
- Marks per minute = net practice marks / minutes used.
- Accuracy = right items / attempted items.

Read the two numbers together, not one at a time:

| Pattern | What it usually means | What to change next set |
|---|---|---|
| High accuracy, low marks per minute | Correct methods, too much time on setup or on checks of easy items | Shorten pass 1; enter pass 2 sooner; reduce checks on items that passed the lesson check |
| Low accuracy, high marks per minute | Fast but careless; codes R and X dominate | Add the label step and the written intermediate line; accept a slower clock until accuracy recovers |
| Low accuracy, low marks per minute | A concept gap; codes C and A dominate | Stop timed work for that lesson; redo its worked examples and the remediation retry prompts, then retime |
| Many blanks, few wrongs | Over-cautious leaving | Review whether the left items were really beyond the budget; move one item type from pass 2 to pass 1 |
| Many G codes, net marks near zero | Picking without a derivation | Leave rather than pick; return to the item in pass 3 only with a method |

Keep one line per set: set number, right, wrong, blank, minutes, net practice marks, marks per minute, and the two most frequent error codes. Compare like with like: Set 7 against Set 1, since they share six items.

A learner might, for example, aim for at least six of eight right within the set budget and no more than one wrong. That is a personal practice target that you set and adjust yourself after three sets, using only your own results.

# REMEDIATION

Each row below names the miss that each lesson's practice items are built to catch, the error code it usually earns, the repair that returns you to that lesson's rule, and a short retry prompt with its expected result. The retry prompts are not multiple-choice items: write your working, then compare.

| Lesson | Typical miss | Code | Repair that returns to the lesson's rule | Retry prompt (expected result) |
|---|---|---|---|---|
| 1. Conditional logic and implication chains | Reading "if A then B" as two-way, so the converse or inverse is accepted | C | Write A -> B and its contrapositive not B -> not A side by side; refuse every other line; settle "must" by assuming the denial | "If a file is urgent, it is flagged. This file is not flagged." What follows? (The file is not urgent; nothing follows about flagged files.) |
| 2. Syllogisms, statement sets and truth-teller logic | Accepting a conclusion that holds in one diagram only | C | Draw the hardest counter-diagram that obeys every premise; in truth-teller sets, score every branch against the stated count | "All clerks are typists. Some typists are drivers." Does "some clerks are drivers" follow? (No: the drivers can sit among typists outside the clerks.) |
| 3. Series, analogies and figural sequences | Fixing a rule from the first two or three terms | A | Write the rule beside every given term before answering; for figures, one table row per feature | Next term of 2, 6, 12, 20, 30? (42: the gaps 4, 6, 8, 10 rise by 2, so the next gap is 12.) |
| 4. Coding, decoding and alphametics | Taking a code rule from one letter | A | Write positions under every letter of every pair; a shift has a constant difference, a mirror a constant sum of 27 | GATE is written TZGV. Write BOOK. (YLLP: each pair of positions adds to 27.) |
| 5. Directions, distance and directed networks | Adding leg lengths for distance, or turning left clockwise | R | Ask "path length or distance from the start?"; write the heading after every turn and sum signed displacements | Walk 6 km north, turn right, walk 8 km. How far from the start, and in which quadrant? (10 km, north-east of the start.) |
| 6. Blood relations and family graphs | Assuming a sex or a generation the clues do not give | C | Draw generation rows with sex markers; mark unknown sexes as unknown; translate only visible paths | "A is a child of B; B is C's brother." How is A related to C? (Nephew or niece; A's sex is not stated.) |
| 7. Ranking, ordering and comparison chains | Forgetting the minus one when combining ranks from both ends, or ordering two items that share only a common neighbour | X | Write both numbers on the rung; total = top rank + bottom rank - 1 for one person; write every comparison in one direction before linking | A boy is 12th from the top and 15th from the bottom. How many in the row? (26.) |
| 8. Seating and arrangement | Halving circular counts out of habit, or starting from the first clue instead of an anchor | C | Anchor the most-constrained person; (n - 1)! with mirror images different unless the stem says otherwise | Six people round a table, rotations the same, mirror images different. How many seatings? (120.) |
| 9. Logic grids and matching structures | Stopping once the asked person is placed, or eliminating by rows only | A | Enter definite pairs, then negatives; eliminate down columns as well as across rows; reread every clue against the finished grid | P, Q, R own a cat, a dog and a parrot, one each. P owns neither the dog nor the parrot. Q does not own the dog. Who owns the dog? (R.) |
| 10. Counting arrangements | Missing a repeat factorial or allowing a leading zero | X | Write each letter with its count before dividing; fill the restricted slot first | Distinct arrangements of the letters of LETTER? (180 = 6! / (2! x 2!).) |
| 11. Counting selections | Filling slots for a team, which counts orders a team does not have | C | Run the order test; if swapping two chosen members changes nothing, use C(n, r) | Ways to choose 3 of 8 volunteers? (56.) |
| 12. Sets, overlap and inclusion-exclusion | Subtracting the triple overlap, or forgetting a "neither" group | C | Fill regions from the centre outward; remove the "neither" group before any bound | Group of 40: 20 in A, 15 in B, 6 in both. How many in neither? (11.) |
| 13. Probability, worst cases and weighing | Keeping fractions unchanged without replacement, or answering a guarantee with an average | A | Rewrite the bag after each draw; for guarantees, write the largest failing hand with stock limits, then add one | A box has 4 red and 6 blue balls. Least draws to be certain of two red? (8: six blue and one red can come first.) |
| 14. Plane-figure counting | Double-counting by scanning, or using C(n, 3) with collinear points | A | Write a size or type list once; state each formula's condition before using it | Nine points lie on a circle. How many triangles have all three corners among them? (84 = C(9, 3): no three points on a circle are collinear.) |
| 15. Solid and cube counting | Fixing an opposite pair from one view, or skipping the class total check | C | Adjacency list from every view; four-class table that must add to the total | A painted 3 x 3 x 3 cube is cut into unit cubes. How many have exactly one painted face? (6.) |
| 16. Data interpretation I | Reporting percentage points as a percent change, or using the wrong base | R | Label the quantity, then the base, then compute; points subtract, percent change divides | A share rises from 10% to 12%. State the change in points and the relative change. (2 points; 20%.) |
| 17. Data interpretation II | Reading a pie angle as a percent, or comparing heights across two axes | X | Angle / 360 of the total; read each series on its own axis, then combine the numbers | A sector of 54 degrees in a pie of ₹2,000. Its value? (₹300.) |
| 18. Decision scenarios and the decision procedure | Choosing the most firm-sounding or kind-sounding option without testing constraints | R | Run the four boxes in order; constraints remove options before the objective ranks them | Name the four boxes in order. (Facts, constraints, objective, feasible options.) |

## Cumulative items 45 to 50

| Item | Lessons joined | Typical miss | Repair and retry |
|---|---|---|---|
| 45 | 10, 11, 13 (and the exact-quantity label from 16) | Counting "at least" for "exactly", one fixed order of deals, or a fifty-fifty chance per card | Count the hand as selections over selections; check by the sequence method with every order counted. Retry: 3 counters drawn together from 4 white and 3 black; chance of exactly one black? (18/35.) |
| 46 | 1, 11 | Reading a one-way condition as two-way, or "if not T then S" as "exactly one of S and T" | Write each condition as an arrow with its contrapositive; list the valid teams by the restricted member. Retry: choose two of A, B, C, D; if A is chosen, B is chosen; C and D are not both chosen. Which member is in every valid pair? (B: the valid pairs are AB, BC and BD.) |
| 47 | 7, 16, 17 | Averaging without weights, weights on the wrong columns, or dividing a weighted average again | Multiply each score by its own weight; check that the weights add to 100%; give the margin over the runner-up. Retry: weights 50%, 30%, 20%; scores X (60, 80, 70), Y (72, 60, 75). Who leads, and by how much? (Y by 1 point: X = 30 + 24 + 14 = 68, Y = 36 + 18 + 15 = 69; the simple average would wrongly put X ahead, 70 to 69.) |
| 48 | 6, 8 | Right and left reversed for a row facing north, a clue dropped, or a "both" clue read as "one" | Build the family graph first, then the seat frame with the facing direction marked; recheck every clue against the finished row. Retry: four people sit in a row facing south; B sits at one end, and A sits immediately to B's right. At which end does B sit? (The east end: facing south, a person's right is the west side, so A is west of B.) |
| 49 | 12, 16 | Ignoring the "neither" group, or reporting the overlap against the wrong base | Remove the "neither" group, find the overlap, then divide by the subgroup the stem names. Retry: 70% read Hindi, 50% read English, 10% neither; among English readers, what share read Hindi? (30/50 = 60%.) |
| 50 | 5, 7 | Path length taken for distance, a north-south total dropped, or the first village reached treated as nearest | Place every point on axes, then order the straight-line distances. Retry: A is 5 km east of O, B is 12 km north of A. How far is B from O? (13 km.) |

# MASTER METHOD MAPS

Each map compresses one family of lessons into the order in which you should act. Read each map from top to bottom; every arrow is a step you take, and every side branch is a trap the lesson named.

## Map 1: implication and syllogism logic (Lessons 1 and 2)

```text
STATEMENT IN WORDS
   |
   v
TRANSLATE  "if A then B" / "A only if B"  ->  A -> B
           "A unless B"                   ->  not B -> A
           "either A or B" (inclusive)    ->  not A -> B
   |
   v
WRITE THE SAFE PARTNER   A -> B   ==   not B -> not A   (contrapositive)
   |                     converse B -> A      : NOT given
   |                     inverse  not A -> not B : NOT given
   v
CHAIN   end of one arrow = start of next (including its "not")
   |    S -> not R -> P -> not Q   gives   S -> not Q
   v
TEST A CLAIM
   |-- "must hold"      -> assume claim false; follow arrows to a contradiction
   |-- "not necessary"  -> build ONE consistent case where it fails
   |-- "possible"       -> build ONE consistent case where it holds
   v
SET STATEMENTS (Lesson 2)
   all / no / some / some-not  -> one diagram -> try the hardest COUNTER-DIAGRAM
   |-- survives every redraw   -> conclusion follows
   |-- fails in one redraw     -> conclusion does not follow
   v
TRUTH-TELLER SETS
   assume each suspect in turn -> score every statement -> keep branches
   matching the stated count -> one branch = fixed; several = not fixed
```

Caption: one arrow and its contrapositive feed every later step; claims are settled by contradiction or by a single counter-case, never by how natural they sound.

## Map 2: directions, family graphs and ranking chains (Lessons 5, 6 and 7)

```text
DIRECTIONS (Lesson 5)
   heading after every turn: right = +90 clockwise, left = -90
   east and north positive -> sum each axis -> distance by the square root
   path length (sum of legs)  !=  displacement (straight line)
   one-way network: travel along arrows only; "every route passes X"
                    -> delete X and test reachability
   |
   v
FAMILY GRAPHS (Lesson 6)
   generation rows; markers for male, female, unknown
   enter the clue that fixes sex AND generation first
   "only son" removes other sons only; a name or "child" fixes no sex
   coded relations -> write each edge as upper person / lower person
   |
   v
RANKING AND COMPARISON CHAINS (Lesson 7)
   one person: top rank + bottom rank = N + 1
   comparisons: rewrite all in ONE direction (heavier > lighter) -> link
   |-- continuous chain        -> order fixed
   |-- shared neighbour only   -> NOT ordered with each other
   |-- scaled clue -> rewrite as X > c x Y : c >= 1 forces X > Y ;
   |                  c < 1 leaves X and Y open (a chain may still settle it)
   |-- summed clue -> "X beats Y and Z together" gives X > Y and X > Z
   v
REPORT only facts true in every order that fits all clues
```

Caption: each of the three lessons turns words into a drawing first, whether axes, a family graph or a ladder, and reports only what the drawing forces.

## Map 3: structure-building for arrangements and grids (Lessons 8 and 9)

```text
READ ALL CLUES ONCE  -> classify each: absolute | linked | negative
   |
   v
DRAW THE FRAME FIRST
   |-- row:    seats 1..n, mark facing direction (north: your right = their right)
   |-- circle: facing centre -> right neighbour = next seat ANTICLOCKWISE
   |-- grid:   one block per attribute pair, ticks and crosses
   v
ANCHOR
   |-- seating: the person named in most clues (opposite / immediately next)
   |-- grid:    the definite pairs
   v
PLACE IN ORDER   absolute -> linked -> negative
   |             grid: eliminate across rows AND down columns
   |             keep link clues in a link block until one side is placed
   v
RECHECK every earlier clue after each placement
   |
   v
SURVIVING CASES?
   |-- one case    -> read the answer
   |-- several     -> report only facts true in ALL cases
   v
COUNTING VERSION (Lesson 8)
   n people round a table: (n - 1)!     labelled seats: n!
   mirror images different by default -> no halving
   "not together" = total - together (glued block x 2 orders)
   keep apart: row of k has k + 1 gaps; circle of k has k gaps
```

Caption: the frame and the anchor come before any name is written; the answer is only what survives in every consistent case, and every clue is reread against the finished structure.

## Map 4: coding and series rules (Lessons 3 and 4)

```text
GIVEN TERMS OR GIVEN CODE PAIRS
   |
   v
CONVERT TO NUMBERS   letters -> positions A=1 .. Z=26 ; from right = 27 - n
   |
   v
SEARCH IN A FIXED ORDER
   series: differences -> ratios -> multiply-then-add -> known sequences
           (squares, triangular 1,3,6,10,15) -> interleaved series
   codes:  constant difference (shift) -> constant sum 27 (mirror)
           -> same letters moved (rearrangement) -> sum / product codes
           -> symbols for operators: replace all at once, then evaluate
   |
   v
VERIFY ON EVERY TERM / EVERY LETTER  <-- the step the traps target
   |-- one term or one letter disagrees -> rule rejected, search again
   v
APPLY   shifts wrap: subtract 26 above 26 ; months cycle 12 ; days cycle 7
   |
   v
FIGURES   one row per feature -> mark invariants -> per-step change for each
          element ; rotation keeps handedness, reflection reverses it
   |
   v
ALPHAMETICS   units column first -> carry 0 or 1 for two addends
              -> new leading digit of the total = 1
              -> report only facts true in ALL solutions
```

Caption: a rule is accepted only after it reproduces every given term or letter; the first-terms rule and the one-letter rule are exactly what the distractors print.

## Map 5: the counting ladder (Lessons 10 to 13)

```text
STEP 0: DOES SWAPPING TWO CHOSEN ITEMS CHANGE THE RESULT?
   |-- yes -> ARRANGEMENT (Lesson 10)
   |          slot diagram; restricted slot first; no leading zero
   |          repeats: n! / (a! x b! ...) ; at least one = all - none
   |-- no  -> SELECTION (Lesson 11)
              C(n, r) ; P(n, r) = C(n, r) x r!
              list cases by the restricted member: in or out
              "or" adds ; "and then" multiplies ; lattice routes C(a + b, b)
   |
   v
GROUPS OVERLAP? -> SETS (Lesson 12)
   remove "neither" first -> union = |A| + |B| - |A and B|
   three sets: add singles, subtract pairs, ADD BACK the triple
   unknown overlap = a range: max(0, |A| + |B| - N) .. min(|A|, |B|)
   |
   v
CHANCE OR GUARANTEE? -> (Lesson 13)
   |-- probability = favourable / total (same counting rule top and bottom)
   |     only for equally likely outcomes
   |     sequence without replacement: rewrite the bag after each draw
   |     "at least one" = 1 - P(none)
   |     A or B, not exclusive: P(A) + P(B) - P(A and B)
   |-- guarantee  = largest failing hand (capped at stock) + 1
   |-- weighing   = 3 results per weighing ; k weighings cover 3^k suspects
   |-- parity     = an even move size never changes the parity of the count
```

Caption: each rung uses the rung below it; the order test chooses between arrangement and selection, the counts feed the overlap tally, and the same counts become the numerator and denominator of a probability.

## Map 6: figure and solid counting (Lessons 14 and 15)

```text
PLANE FIGURE (Lesson 14)
   |
   v
WRITE A SIZE OR TYPE LIST (one line per class, total at the end)
   |-- squares in n x n grid       : 1^2 + 2^2 + ... + n^2
   |-- rectangles, a by b lines    : C(a, 2) x C(b, 2)   (count LINES, not boxes)
   |-- segments among n points     : C(n, 2) ; k collinear: - C(k, 2) + 1 line
   |-- diagonals, CONVEX n-gon     : n(n - 3)/2
   |-- triangles                   : C(n, 3) - collinear triples
   |-- board diagonal, m x n cells : m + n - gcd(m, n)
   v
STATE EACH FORMULA'S CONDITION BEFORE USING IT
   |
   v
SOLID (Lesson 15)
   |-- views: faces seen together are adjacent ; 4 neighbours + 1 opposite
   |          never fix an opposite pair from a single view
   |          two views sharing two faces -> their third faces are opposite
   |-- nets:  in a straight run, faces one square apart are opposite
   |-- painted n-cube: corners 8 | edges 12(n - 2) | faces 6(n - 2)^2
   |                   core (n - 2)^3 -> the four classes add to n^3
   |-- cuts:  x, y, z cuts -> (x + 1)(y + 1)(z + 1) pieces
   |          unpainted core: 2 pieces fewer in each direction
   |-- two sizes: volume (and piece count) fix how many of each
              -> placement clue fixes where -> count pieces, not unit volumes
```

Caption: both lessons replace visual scanning with a written list, either by size and type or by painted-face class, and close with a total that must match.

## Map 7: data interpretation reading order (Lessons 16 and 17)

```text
READ BEFORE COMPUTING: title -> unit -> scale -> both axes / pie total
   |
   v
LABEL THE QUANTITY ASKED
   level | change | percent change | share | change in points
   | relative change | rate per unit | weighted score
   |
   v
NAME THE BASE
   |-- percent change   : the starting value
   |-- share            : its own total (a slice -> value only via its pie's total)
   |-- rate per unit    : the group's own size (compare rates, not counts)
   |-- weighted score   : multiply each part by its weight, add,
   |                      divide by the sum of weights if it is not 1
   v
COMPUTE WITH THE FORMULA
   |-- pie: angle a = a/360 of total ; p% = 3.6p degrees
   |-- two axes: read numbers on their own axes ; never compare heights
   |-- points subtract ; percent change divides ; bases do not cancel
   v
CHECK THE LABEL AGAINST THE STEM, THEN STOP
   a table supports calculations on its numbers, not causes or forecasts
```

Caption: the label and the base are fixed before any arithmetic, which is why the distractors in this family are other correct numbers from the same chart.

## Map 8: the decision procedure (Lesson 18)

```text
BOX 1 FACTS        only what the stem states
   |
   v
BOX 2 CONSTRAINTS  laws, rules, duties, deadlines, resources, limits of role
   |               -> delete every option that breaks one
   v
BOX 3 OBJECTIVE    the purpose the actor is meant to serve
   |
   v
BOX 4 FEASIBLE OPTIONS -> elimination screen
   reject: illegal | coercive | deceptive | discriminatory
           | disproportionate | abdicating (inaction, passing upward)
   prefer: lawful | fair | clear | proportionate | documented | followed up
   |
   |-- the scenario turns on a message?  classify the barrier first
   |   (physical | semantic | psychological | organisational | technological)
   |   and choose the fix that matches it
   v
CHOOSE the survivor that best meets the objective with the fewest
added assumptions
```

Caption: constraints remove options before the objective ranks them, so a firm-sounding or kind-sounding option that needs an unstated fact loses to a plainer one that fits.

# COMPLETE CONSOLIDATED REGISTER NOTES

## Reading these notes

Each block below compresses one unit to its decision points: what the thing is, the rule, where the rule breaks, the trap that costs marks, and the lesson (L01 to L18) where it is taught in full. Advanced material is marked "(Advanced)" and is not needed for a core answer. Items about communication appear here only for their reasoning structure: matching, statement testing and option elimination.

## The one habit behind every item: externalise the structure

- **Definition.** A reasoning item is a structure (row, circle, family graph, compass, Venn, table) hidden inside words. Five item kinds: ARRANGE (row, circle, grid), RELATE (family, directions, network), CODE (letters, numbers, symbols), COUNT (arrange, choose, figures), READ (table, graph, pie).
- **Rule.** Draw the structure before reasoning; let the constraints do the work.
- **Failure condition.** Holding four or more constraints in the head; the fourth clue silently overwrites the first.
- **Trap.** Estimating a path, seating or chain "by picture in the mind" instead of on paper.
- **Taught.** Every lesson opens with its own visual; the drawing step is explicit in L06 ("Method: build the graph from the clue that fixes most", step 1 "Classify and draw") and L08 ("Method 1: build the frame before the people").

## The five-step working method

1. **Classify and draw** (L06 "Classify and draw"; L08 "Method 1: build the frame before the people").
2. **Strongest constraint first**, checking consistency after every entry (L07 "Placing the clue that fixes the most"; L08 "Method 2: strongest constraint first, then recheck"; L06 "Method: build the graph from the clue that fixes most"). Failure: entering clues in reading order and backtracking.
3. **Order matters?** Decide before any formula: arrangement (permutation) or selection (combination) (L10 "Step 0: does order matter?"; L11 "Step 0: the order test, again"). Failure: swapping two chosen items and not asking whether the result changed.
4. **Answer the exact quantity asked**: total, change, percent change, share, points, rate (L16 "Rule 1: answer the exact quantity asked"; L17 "Method 1: read title, unit, scale and both axes first"). Failure: computing the nearby quantity that sits among the options.
5. **Scenario step:** classify the barrier or failure, reject coercive and deceptive options, prefer fair, clear, followed-up action (L18 "Visual: the four-box procedure" and "The elimination screen").

## Conditional logic: arrows, contrapositives and chains (L01)

- **Implication.** "If A then B" = A -> B. A is sufficient for B; B is necessary for A. "A only if B" = A -> B. "A unless B" = not B -> A. "Either A or B" = not A -> B (inclusive "or" unless "not both" is stated).
- **Equivalence.** A <-> B = both A -> B and B -> A; only then may the two be swapped.
- **Safe moves.** Contrapositive (not B -> not A) always holds. Transitivity: A -> B and B -> C give A -> C, and its contrapositive not C -> not A.
- **Unsafe moves.** Converse (B -> A) and inverse (not A -> not B) are never given by a one-way sentence.
- **Chaining condition.** Arrows join only when the end of one matches the start of the next exactly, including any "not".
- **Testing a claim.** "Must P -> Q hold?" Assume P and not Q; chain to a contradiction. "Is Q not necessary?" Build one consistent case with Q false and check every premise against it.
- **Possible / certain.** Possible = one consistent case exists; certain = every consistent case; neither needs a probability.
- **Either-or falsification.** A universal "every X is A or B" is broken only by a member of X for whom both parts fail; a non-member or a proportion cannot break it.
- **Consistency of a set.** Consistent only if one complete case satisfies every statement.
- **Trap.** Copying a link without its "not" (P -> not Q written as P -> Q); reading "only if" the wrong way round.
- **(Advanced) Implication chaining across negated links.** Four-claim puzzles are settled by writing each link and its contrapositive and chaining; no truth table.
- **(Advanced) Method 4, solve chains backwards.** (1) write every arrow, (2) write its contrapositive, (3) to test "if P then Q" assume P and not Q, (4) to test "not necessary that Q" find one consistent case with Q false. Escalation rule: two arrows and one contradiction beat a sixteen-row table.
- **(Advanced) "Not necessary"** is settled by one counter-case; it does not mean "false".
- **Worked chain.** Every scholarship holder is a hosteller; every hosteller is a registered student. Then every scholarship holder is a registered student (chain) and anyone not registered is not a scholarship holder (contrapositive); "every registered student is a hosteller" is the converse and does not follow.
- **PYQ families.** Conditional logic conclusion; implication consistency; statement-implication logic; falsifying an either-or claim.

## Syllogisms and set containment (L02 Part A)

- **Four forms.** All A are B (A fence inside B), No A is B (fences apart), Some A are B (a dot in the overlap), Some A are not B (a dot in A outside B). Each forbids a region or places a dot; everything else stays open.
- **Validity doctrine.** A conclusion is valid only if it holds in every diagram that satisfies all premises; one counter-diagram that obeys every premise disproves it.
- **Safe conversions.** "No A is B" <-> "No B is A"; "Some A are B" <-> "Some B are A". Unsafe: "All A are B" to "All B are A".
- **Chains.** All A are B + No B is C -> No A is C. Some C are A + All A are B -> Some C are B.
- **Existential limit.** "Some A are B" does not give "some A are not B".
- **Either-or pair of conclusions.** Valid only for a contradictory pair with the same subject and predicate (Some/No; All/Some-not).
- **Trap.** Accepting a conclusion true in the one diagram you drew; reading "some" as "all".
- **(Advanced)** Syllogism validity by counter-diagram; never accept a conclusion because it "sounds right"; the diploma-graduate chain (every diploma holder is a graduate; no graduate is under 18) gives "no diploma holder is under 18", while "every graduate is a diploma holder" is the converse.
- **PYQ families.** Syllogism conclusion check and selection; multi-conclusion syllogism; transitive-colour syllogism; colour propositions.

## Multi-statement sets, causes and case-splits (L02 Part B)

- **Method.** Chain the statements once into a flow; test each conclusion separately against the chain.
- **Everyday content.** Use only what is stated; reject conclusions that need outside facts or an unstated cause.
- **Cause from a table of cases.** A single reliable cause is present in every positive case and absent in every negative case.
- **Case-split.** A fact is definite only if it holds in every consistent case ("who must have stayed home", "who must be male").
- **Sufficiency of a statement set.** Sufficient = conclusion true in every consistent arrangement.
- **Trap.** Treating a plausible everyday conclusion as following.
- **PYQ families.** Statement-conclusion items (party supporters, voice practice, morning walk, UFO, population growth, music and gender); fruit-caused sickness; who remained at home; definitely male member; statement sufficiency check; logical chain elimination; statement-set and multi-statement syllogism.

## Truth-teller and suspect-statement logic (L02 Part C)

- **Method.** Assume each candidate in turn; score how many statements come out true; keep only branches matching the stated count.
- **Rule.** If exactly one branch survives the answer is fixed; if several survive it is not.
- **Failure condition.** Trusting the first accuser, or picking the unaccused person, without scoring every branch.
- **The job each statement does: supports, weakens or unrelated.** Against a stated conclusion, a statement supports it if, were it true, the conclusion would become more believable; weakens it if belief would fall (another cause, a cost); and is unrelated if belief would not move, since sharing a word or a topic is not enough. Ask about one statement at a time: does it bear on the exact link, which way would belief move, and how hard does it push; check that a stated cause comes before its effect. Failure: judging a role by tone or by your own opinion of the conclusion.
- **Numbered statements and combination options.** Judge each numbered statement on its own; strike combinations only on verdicts you are sure of; read the code last.
- **PYQ families.** True-false logic deduction; suspect-statement logic; statement-relationship logic; statement evaluation.

## Number and letter series (L03 Part A)

- **Search order.** Differences (and second differences) -> ratios -> multiply-then-add -> known sequences (squares, cubes, primes, triangular) -> interleaved series.
- **Triangular numbers.** 1, 3, 6, 10, 15, 21; n-th = n(n + 1)/2; gaps rise by one.
- **Letters.** A = 1 to Z = 26; anchors E 5, J 10, O 15, T 20, Y 25; reverse position = 27 - position.
- **Middle gap / dual series.** Test the rule on both sides of the gap; an up-down series is two interleaved series.
- **Repeating patterns.** Find the shortest block that agrees with every given letter.
- **Cyclic series.** 12 months, 7 days, clock positions; wrap by remainder.
- **Rule of acceptance.** A rule is accepted only after it reproduces every given term.
- **Failure condition.** A rule fitted to the first two or three terms (5, 11, 23, 47: x2 + 1 gives 95; "sum of two before" fails on term four).
- **PYQ families.** Letter sequence fill and completion; letter series position; sequence middle term; dual-sequence missing entry; series blank-fill; repeating pattern gap fill; month-pattern sequence; letter-pattern completion.

## Analogies and odd-one-out (L03 Part B)

- **Method.** Name the relation in the given pair; test it on the parallel pair; a pair may support two relations, so test every given pair.
- **Odd-one-out.** The chosen property must single out exactly one group (of (3, 9, 27), (2, 4, 8), (5, 25, 125) and (4, 12, 36), every group has a fixed ratio and "all odd" splits the groups two against two, but only (4, 12, 36) fails to be a number followed by its square and its cube).
- **Figural analogy.** Distinguish rotation from reflection; a rotation keeps handedness, a reflection reverses it.
- **Trap.** A property that singles out two groups, or a relation fitted to one pair only.
- **PYQ families.** Prime-group odd-one-out; letter analogy series; figural analogy completion.

## Figural sequences, mirror images and matrices (L03 Part C)

- **Method.** One table row per feature (position, count, shading, orientation); mark invariants; track each moving element separately with its own per-step change.
- **Moving symbols.** Count steps around a ring by remainder (8 outer cells of a 3 x 3 grid).
- **Mirror images.** A side mirror reverses order and flips letters; A, H, I, M, O, T, U, V, W, X, Y look unchanged.
- **Embedded figures.** Size and orientation are kept unless the stem allows change.
- **Matrix completion.** The rule must work along every row and every column.
- **Figure counting** belongs to L14 ("Method 1: count by size, exactly once").
- **Trap.** Treating several moving elements as one; reading a rotation as a reflection.
- **PYQ families.** Moving symbols in a grid; triangle, line-and-arrow and circular-arrow sequences; embedded figure; arrow and circle-triangle matrices; bead-position sequence; figure-sequence completion; figural rotation series; mirror-image consonant count; matrix trend missing entry.

## Coding and decoding (L04)

- **Rule from every pair.** Write positions under every plain and coded letter; derive the rule from every pair; test it on every letter; then apply.
- **Shift code.** Constant difference (CAT -> DBU, DOG -> EPH, so SUN -> TVO; (Advanced) EARTH -> GCTVJ, so MARS -> OCTU). Shifts wrap: subtract 26 above 26.
- **Mirror code.** Constant sum 27 (A <-> Z); decodes with the same rule that encodes.
- **Rearrangement code.** A position map; confirm on a second word of the same length.
- **Letter-to-number code.** Needs a second word to separate sum, product and other operations.
- **Sentence (word) codes.** A word in every sentence carries the code common to every sentence; word order is not evidence.
- **Symbol / operator substitution.** Replace every symbol at once, then follow the usual order of operations.
- **Coded values under constraints.** List each value of the most restricted letter.
- **Failure condition and trap.** A rule guessed from one letter; two different rules can agree on one letter. (Advanced) Error code R: re-derive the rule on every letter.
- **PYQ families.** Letter substitution and shift ciphers; alphabet reversal coding; letter-to-number and multiplicative-letter codes; letter-rearrangement coding; word-code deduction; military coding pattern; symbol operation decode and operator substitution; coded-value constraints; coded-operator arrangement; numeric-cube code; letter-digit substitution.

## Alphametics: digit solving with carries (L04)

- **Method (analytical).** Units column first; a carry between columns is 0 or 1 for two addends; a new leading digit of a total is 1; use place-value algebra (PQ + QP = 11(P + Q)).
- **Failure condition.** Dropping a carry when reading the next column.
- **Trap.** Reporting a fact from one solution; report only facts true in every solution.
- **PYQ families.** Alphametic addition; alphametic subtraction.

## Directions and distance (L05)

- **Headings.** North 0, east 90, south 180, west 270 degrees.
- **Turns.** Right = +90 (clockwise), left = -90 (anticlockwise), both relative to the current heading. Two rights = U-turn (180); right then left restores the heading.
- **Displacement.** North and east positive; sum each axis; distance = square root of (east total squared + north total squared); direction from the quadrant.
- **Path vs displacement.** Path length adds every leg; displacement is the straight-line result.
- **Degree turns.** Add clockwise, subtract anticlockwise, wrap round 360.
- **Square path, opposite walkers.** They meet after a combined distance of one perimeter.
- **Trap.** Treating a left turn as clockwise; picturing the walk when facing south (left and right swap on the page).
- **PYQ families.** Multi-turn and rotational direction sense; direction turns and distance; opposite-direction square paths; direction-network distance.

## Directed networks (L05 Part B)

- **Rule.** Each arrow is one-way; travel along arrows only.
- **Necessity test.** "Every route passes through X": delete X and check whether the target is still reachable.
- **Closed link.** Redo reachability from the start after closing a link.
- **Revisit.** Necessary only when no other arrow leaves the loop point.
- **Trap.** Treating one convenient route as the only route; travelling an arrow backwards.
- **PYQ families.** Direct route; city necessarily revisited; directly connected pair; directed railway route necessity; route after closing a link. Route counts on networks belong to L11.

## Blood relations and family graphs (L06)

- **Graph.** Generation rows; distinct markers for male, female, unknown; relation words are paths read step by step.
- **Method.** Enter the clue that fixes sex and generation together first; recheck earlier clues after each addition.
- **Sex not fixed by.** A name, "child", "sibling", "parent", "spouse".
- **"Only son / only daughter".** Removes other children of the same stated sex only, not siblings of the other sex; the speaker's own sex decides whether the phrase points to the speaker. "My paternal grandfather's only son" = the speaker's father, so for a male speaker "the daughter of my paternal grandfather's only son" is his sister.
- **Coded relations.** Write each edge as upper person / lower person before chaining.
- **Sufficiency for a relation.** The statements must fix generation and any sex the question names.
- **Couples and ages.** A couple's child is the child of both unless step-relations are mentioned; ages on a graph give ranges, not values.
- **Trap.** Assuming sex or generation; "daughter-in-law" read as "daughter"; putting a link on the maternal side when it runs through the father.
- **PYQ families.** Blood-relation deduction and tree; symbolic and coded relational chains; family inference puzzles; family couples; cousins' possible age; family-relation statement sufficiency.

## Ranking and positions (L07)

- **From both ends.** Rank from top + rank from bottom = N + 1 (one line, no ties).
- **Two ranks of one person.** p from one end and q from the other give a row of p + q - 1.
- **Exchanges.** An exchange swaps the names on two rungs; no rung moves. Write every rung's rank from one end, then move the names; anyone outside the exchange keeps the same rank. Convert a rank from the other end (N + 1 - r) before combining two numbers.
- **Between.** People strictly between positions a and b from the same end = |a - b| - 1; from opposite ends, draw both the separate and the overlapping pictures before "at least" or "at most".
- **Median.** Odd group of N: position (N + 1)/2.
- **Trap.** Forgetting the -1 for the person counted twice.
- **PYQ families.** Rank from the end; median by height; ranking order deduction; ranking-order logic; ladder ordering.

## Comparison chains, speed, age and price ordering (L07)

- **Rule.** Rewrite every comparison in one direction ("heavier > lighter") before linking; only continuous one-direction chains give an order.
- **Missing link.** Two people compared with the same third person in the same direction are not ordered with each other.
- **Ties.** Two people tied at rank k both hold rank k; the next person is ranked k + 2, and no one holds rank k + 1.
- **(Advanced) Recheck rule.** After each placement recheck every earlier clue; if several orders survive, only common facts are certain.
- **(Advanced where it extends) Numbers.** Race margins combine as ratios (10 m and 10 m give 19 m, not 20 m); a strict "more than" in whole units raises a bound by one unit.
- **Scores.** Round robin with 2 points per match: total points = 2 x matches.
- **Scaled comparisons (weight chains).** Rewrite each statement as X > c x Y, with the heavier-claimed person on the left. A factor c of 1 or more forces X > Y; a factor below 1 leaves the pair open, though a chain through another person may still settle it. "X weighs more than Y and Z together" gives X > Y and X > Z; "X and Y together weigh more than Z" gives nothing about X against Z. Accept a claim only if it holds for every set of positive weights that fits.
- **Trap.** Ordering two items that share only a common neighbour.
- **PYQ families.** Age-order inference and conclusions; couple height ordering; vegetable taste ordering; relative running speed; slowest runner; cousins' age orders; cow-goat price bounds; statement-based age ranking; tournament-score logic; weight inequality deduction.

## Seating and arrangement (L08)

- **Frame first.** Draw seats and facing direction. Facing north, a person's right is your right; facing south, it is your left. At a round table facing the centre, a person's right is the next seat anticlockwise.
- **Anchor.** Fix the most-constrained person; in a circle this also removes rotations.
- **Order of clues.** Absolute clues, then linked clues, then negative clues; recheck all clues after each placement; test every statement against the finished seating.
- **Multiple solutions.** Only facts true in every surviving seating are certain.
- **Groups and floors.** Settle the grouping before seating anyone.
- **Row-position counts.** Left + right = N + 1; between = |a - b| - 1.
- **(Advanced) Method 1, multi-constraint seating.** R in seat 3, P at extreme left, Q immediately right of P, T not at an end -> P, Q, R, T, S, forced.
- **Trap.** Reporting a seat found in the first seating as fixed.
- **PYQ families.** Round-table necessities; adjacent seat; circular seating; non-adjacent girls; row arrangement; office seating; placement logic and placement statement checks; row-position counts; group-seating constraints.

## Counting seatings round a table (L08)

- **Rule.** n different people round a table, rotations identical: (n - 1)! (five friends: 4! = 24; six people: 5! = 120).
- **Mirror images.** Do not halve unless the stem says a seating and its mirror image are the same.
- **Labelled seats** remove rotation symmetry: n!.
- **Not together** = total - together; a glued block has 2 internal orders.
- **Gap method.** A row of k leaves k + 1 gaps; a circle of k leaves k gaps.
- **(Advanced) Opposite and not adjacent.** Six round a circle, A opposite B, C not next to A: fix A, B fixed, C has 2 seats, others 3! -> 12.
- **Trap.** Counting rotations as new seatings; halving by default.

## Logic grids and matching (L09)

- **Grid.** One block per attribute pair; one tick in every row and every column of a one-to-one block.
- **Order.** Definite pairs first, then negative clues, then link clues held in a link block until one side is placed.
- **Elimination.** Down columns as well as across rows; the unmentioned person is often found by a column.
- **Final check.** Reread every clue against the finished table, from the first clue.
- **Exactly-one statements.** Test each statement as the true one; keep only consistent cases.
- **Mislabelled boxes (all labels wrong).** Draw from the "mixed" label, since it cannot hold the mixture.
- **What others can see.** Each "I do not know" removes every case in which the speaker would have known.
- **Cycles and free days.** Rotations by remainder; check the starting year on a small case.
- **Selections with conditions.** Conditions become arrows; list cases by the most restricted post.
- **Max / min under rules.** To maximise one count, minimise all others within the rules.
- **Multi-attribute classification.** A yes-no feature table; check every defining feature.
- **Trap.** Treating an open pair (two people sharing two options either way) as fixed.
- **List matching (List I against List II).** List I as rows, List II as columns, one tick per row and column; match by the function described (relationship type, tool purpose, channel, feedback, barrier), not by a familiar word; fix the surest pair first and strike every code that contradicts it.
- **Questionnaire design.** Keep questions clear, neutral and single-issue with suitable response choices; reject leading, double-barrelled, ambiguous or intrusive wording; keep only items that serve the stated objective.
- **(Advanced) Classification drill.** A question asking two judgements at once is double-barrelled; a misunderstood technical acronym is a semantic barrier; a post-meeting form that checks understanding is a feedback tool.
- **PYQ families.** Profession puzzles; people and cities; cap-colour; poet, dancer and violinist; free day; principal and vice-principals; subject combinations; language and driving; golf-ball and box-colour statements; surname, tie and sweater; test scheduling; lecturer-subject grids; maximum subjects taught; women-category grid; multi-attribute classification; segment matching; primary-group inference. List matching (category to style, item to purpose, category to example): settled pair by pair.

## Arrangements: permutations, restrictions and codes (L10)

- **Step 0.** If swapping two items changes the result, you are arranging.
- **Slot diagram.** One box per slot; write the choices available at the moment of filling; restricted slot first.
- **P(n, r) = n! / (n - r)!** for 0 <= r <= n, no repetition (three-digit numbers with distinct digits from 1, 2, 3 and 4: P(4, 3) = 24). With repetition: n^r.
- **First-place and zero rule.** A number cannot start with 0 (five-digit numbers from 0 to 4 without repetition: 4 x 4! = 96; four-digit numbers from 0 to 3: 3 x 3! = 18). When 0 is forbidden in front and allowed in the units slot (even numbers), split by the units digit.
- **Repeated letters.** n! / (a! x b! x ...); divide by every repeat (LEVEL 30; (Advanced) SUCCESS 420, not 840).
- **(Advanced) Complement.** "At least one" = all - none, both counted under the same rule.
- **Position constraints; adjacent colours.** No two neighbours alike in a strip: k x (k - 1)^(n - 1); a ring needs cases.
- **Digit relations and properties over a range.** List by the digit the rule pins down; split a range by number length and cut the last block at the end of the range; palindromes count only free slots.
- **Dictionary position.** Count earlier words slot by slot using unused letters, then add 1.
- **Codes, PINs, passwords.** A PIN may start with 0 (a code, not a number).
- **(Advanced) Error analysis.** Name the slip (repeat-factorial, leading zero, order mistaken) before redoing.
- **Trap.** Leading zero admitted; one repeat factorial missed; order mistaken.
- **PYQ families.** Constrained digit strings; colour arrangement; digit-sum integer count; restricted and row digit arrangements; odd digit counting; letter arrangement; constrained PIN and password; grid row arrangement; form-constraint numbers; position-constrained permutation; adjacent-colour stripes; reverse alphabetical position; digit-frequency counting; constrained-word permutation.

## Selections: combinations, partitions and routes (L11)

- **C(n, r) = n! / (r! x (n - r)!)**, 0 <= r <= n; symmetry C(n, r) = C(n, n - r).
- **Bridge.** P(n, r) = C(n, r) x r!: select, then arrange.
- **Pairs.** Handshakes, segments, round-robin matches among n: C(n, 2) (10 people -> 45).
- **Include / exclude.** List cases by the restricted member, in or out; "at least" = exact cases added, or total minus forbidden.
- **"Or" adds; "and then" multiplies.**
- **Routes.** Lattice a east, b north: C(a + b, b); through a point, multiply the two halves. Directed network: each node's count = sum of counts on arrows into it.
- **Partitions.** Ordered positive splits of n into k parts: C(n - 1, k - 1); with zeros allowed: C(n + k - 1, k - 1); unordered splits: list parts in non-increasing order.
- **Gaps and circles.** No two consecutive from n in a line: C(n - k + 1, k); a circle needs separate care. Passing k places among n returns after n / gcd(n, k) passes.
- **Bridge to sets.** At least |A| + |B| - N are in both.
- **Trap.** Counting only the "exactly" case in an "at least" item; ignoring a required junction.
- **PYQ families.** Tennis and music team selections; teams containing all three males; travel options; routes S to T and route combinations; counting directed railway routes; task and constrained assignments; denomination combinations and subsets; sequence conditional and pair counts; natural-number, score and integer-constraint partitions; non-consecutive and circular consecutive selections; circular pass-sequence return; constrained triplets.

## Sets and inclusion-exclusion (L12)

- **Regions.** Each person sits in exactly one Venn region; regions add to the total.
- **Two sets.** |A ∪ B| = |A| + |B| - |A ∩ B|; neither = N - union; exactly one = |A| + |B| - 2|A ∩ B|.
- **Overlap bounds.** From max(0, |A| + |B| - N) to min(|A|, |B|) (50 people, 28 and 24 -> 2 to 24; 40 books, 26 hardbacks and 23 novels -> 9 to 23). Remove a known "neither" group from N first.
- **(Advanced) Three sets.** Add singles, subtract pairwise overlaps, add back the triple; fill regions from the centre outward; "in A and B" includes the triple, "exactly A and B" is a region.
- **(Advanced) Multiples.** Use lcm (not product) for overlaps, and only when the sets are multiples of given integers (1 to 100, divisible by 2, 3 or 5: 74).
- **Membership tables** answer "who does not", "common to", "exactly k".
- **Classification inside classification.** Draw nested or overlapping circles as in syllogisms.
- **Fractions of one whole.** Inclusion-exclusion on fractions; the total is a multiple of the lcm of denominators; do not mix bases.
- **Trap.** Inventing one overlap from two set sizes; subtracting the triple overlap instead of adding it back.
- **PYQ families.** Friends and games (hockey, game count, common game); book classification intersection; Venn-diagram counting and deduction; set overlap deduction and range; fractional set deduction.

## Probability as a listed world (L13 Part A)

- **Favourable over total.** P = favourable / total, only for equally likely outcomes (3 red, 2 blue: P(red) = 3/5). Every probability lies in [0, 1]; outside it signals a counting error.
- **Complement.** P(not E) = 1 - P(E); "at least one" via "none". (Advanced) The complement rule is always valid; independence is needed only to multiply components into P(none).
- **Sequence.** P(A and B) = P(A) x P(B | A); without replacement the later fraction changes (3 red and 2 blue: (3/5)(2/4) = 3/10; 4 white and 6 black: (4/10)(3/9) = 2/15).
- **Draw together.** Use C(n, r) (two red from 3 red, 2 blue: 3/10). Do not mix an ordered numerator with an unordered total.
- **(Advanced) Dice and coins.** Sample spaces 6^k and 2^k; two dice give 36 ordered pairs; sums are labels, not equally likely outcomes (sum 7: 1/6; sum at least 10: 1/6, a coincidence).
- **(Advanced) Drill values.** A coin tossed three times: P(at least one head) = 1 - 1/8 = 7/8. Two drawn together from 4 white and 6 black: P(at least one white) = 1 - C(6, 2)/C(10, 2) = 1 - 15/45 = 2/3. Second white given a white first draw, not replaced: 3/9 = 1/3.
- **Possible / probable / certain.** Possible is yes/no (P > 0); probability is a number; certain is P = 1.
- **Derangements.** No item in its own place: D_n = (n - 1)(D_(n-1) + D_(n-2)), giving 0, 1, 2, 9, 44, 265; exactly k in place = C(n, k) x D_(n-k); exactly n - 1 in place is impossible. Test whether a stated split can exist before computing.
- **Turning moves and parity.** When every move turns an even number of coins, the parity of the head count never changes, so a goal of the other parity is impossible; passing the parity test does not by itself prove a goal reachable.
- **(Advanced) Non-exclusive events.** P(A or B) = P(A) + P(B) - P(A and B); adding the two probabilities of events that can happen together counts the overlap twice. Use inclusion-exclusion or the complement.
- **Trap.** Unchanged fraction without replacement; non-equally-likely outcomes listed as equal.
- **PYQ families.** Dinner-host lottery; card-flip puzzle; derangement possibility check.

## Worst cases and "plus one" (L13 Part B)

- **Rule.** Guarantee = largest failing hand + 1, each colour capped at its stock (three colours, two of one: 4; red and blue, three of one: 5).
- **Pairs and gloves.** Handed objects pair only left with right.
- **Knockouts and queues.** A knockout among n needs n - 1 matches.
- **Failure condition.** Ignoring a colour whose stock is smaller than the target count.
- **PYQ families.** Blind-draw colour guarantee; worst-case pair and colour-group draws; queue minimum size; elimination match counting.

## Weighing and crossing strategies (L13 Part C)

- **Thirds rule.** With one heavier coin, k weighings separate at most 3^k suspects; a first split works only if both pans and the pile aside each hold at most 3^(k - 1). With an odd item of unknown direction, read each result as which items it clears.
- **Loads a set of weights can measure.** One pan only: the subset sums. Weights on both pans: a weight beside the load subtracts, so more loads become measurable.
- **Inequalities from pans.** Pan results are inequalities that can be chained and subtracted.
- **Crossing with one torch or raft.** With capacity c and a return after every trip but the last, the least number of forward trips is the smallest f with (c - 1)f + 1 at least n, and the least crossings 2f - 1. Test a deadline with lower bounds; send the slowest together.
- **Trap.** Treating a weighing as a two-way test (halving).
- **PYQ families.** Weighing-coin optimisation; weighing-combination count; odd-item weighing logic; bridge crossing with lamp return.

## Plane-figure counting (L14)

- **Count by size.** Count by size or type, each class written once (3 x 3 grid: 9 + 4 + 1 = 14; 2 x 2 grid: 4 + 1 = 5). Squares in an n x n grid: 1^2 + ... + n^2; an 8 x 8 board has 204.
- **Rectangles.** From a lines by b lines: C(a, 2) x C(b, 2); count lines, not boxes. Two crossing families of parallel lines give parallelograms by the same product.
- **Segments and lines.** C(n, 2) segments; distinct lines only if no three collinear; with k collinear points remove C(k, 2) and add back 1.
- **(Advanced) Diagonals.** n(n - 3)/2 = C(n, 2) - n, for a convex polygon (a decagon has 10 x 7 / 2 = 35); run backwards, n(n - 3)/2 = 3n gives n = 9 (nonagon, 27 diagonals), and 30 diagonals is impossible because no whole n gives n(n - 3) = 60.
- **Triangles.** C(n, 3) minus collinear triples (a quadrilateral likewise needs four points with no three on one line); points on a circle have none; shared-top-vertex figure: pairs of lines from the vertex x number of base lines.
- **Right angles and rectangles on a circle.** A triangle on a circle is right-angled exactly when one side is a diameter; with d diameters among the points there are C(d, 2) rectangles, and the right angles at a named point equal the diameters that avoid it.
- **Board diagonal.** A corner-to-corner diagonal of an m x n board crosses m + n - gcd(m, n) cells.
- **Trap.** Visual scanning double-counts; subtracting collinear pairs instead of collinear triples.
- **PYQ families.** Rectangles from grid lines; polygon diagonal count; grid parallelogram count; chessboard diagonal count; circle-inscribed triangles; collinearity-aware triangle count.

## Cube views and nets (L15)

- **Rule.** Faces in one view are adjacent; each face has four neighbours and one opposite; collect all neighbours from every view.
- **Two-shared-faces rule.** Two views sharing two faces make their third faces opposite.
- **Nets.** In a straight run, faces one square apart are opposite.
- **Four neighbours fix the opposite.** Views of the corners Red-Blue-Green and Red-Yellow-White give Red four neighbours, so Black is opposite Red; the other two pairs stay open until a third view.
- **Trap.** Fixing an opposite pair from a single view.
- **PYQ families.** Cube faces A and B; cube rotation opposite face; cardboard assembly; coloured cube.

## Painted cubes, cuts and solids (L15)

- **Painted n-cube.** 8 corners (3 faces), 12(n - 2) edge pieces (2 faces), 6(n - 2)^2 face pieces (1 face), (n - 2)^3 core (0 faces). The four classes must add to the total.
- **Cuboid a x b x c.** Edge pieces 4[(a - 2) + (b - 2) + (c - 2)]; unpainted pieces (a - 2)(b - 2)(c - 2).
- **Cuts.** x, y, z cuts give (x + 1)(y + 1)(z + 1) pieces if pieces are not moved; n^3 equal cubes need at least 3(n - 1) cuts.
- **Two sizes of cube.** Volume fixes how many of each size (a x s^3 + b x t^3 = V, with a + b = N when the piece count is given); a placement clue fixes where the big cubes sit; then count painted faces piece by piece. Failure: applying the equal-cube table to unequal pieces counts unit volumes, not pieces.
- **Partly painted blocks.** Classify each small cube by the painted surfaces it touches.
- **Colouring.** Six different colours on a cube give 30 distinct cubes, not 720.
- **Stacked solids.** Include hidden cubes that support visible ones; count by column or slice.
- **Trap.** Confusing the number of cuts with the number of pieces; a dimension of 1 or 2 empties some classes.
- **PYQ families.** Solid-shape counting; cube partition cuts; cube face colouring; interior cube count; painted cuboid partition; painted-region pattern count.

## Data interpretation: levels, changes and shares (L16)

- **Label strip.** Level, change, percent change, share, percentage points, relative change, rate.
- **Base rule.** Percent change uses the starting value; share uses the total.
- **Points vs percent.** Points subtract; percent change divides (20% to 25%: +5 points, +25% relative).
- **Rates.** Compare groups of different sizes by rates per unit, not counts; 30.4 overs = 30 + 4/6 overs.
- **Amounts tied by stated relations.** Write every amount in terms of one unknown; where one amount is reached through two sentences, set the two expressions equal; then compute exactly what is asked (total, ratio, difference or one amount).
- **Cross-tables.** Check row and column totals against the grand total; the largest count does not imply the largest ratio.
- **Trends.** Equal absolute rises mean falling percent rises.
- **Limits.** A table supports calculations on its numbers, not causes or forecasts.
- **Worked table.** Totals X 750, Y 450; X Jan to Mar +50%. **Output change.** 40 to 50 thousand units is +10 thousand units, not +10% (the percent rise is 25%).
- **(Advanced) Multi-step.** Different bases do not cancel (+25% then -10%: 400 -> 500 -> 450); level can fall while share rises (500 -> 450 while 40% -> 50%); +10 points = +25% relative.
- **Weighted-score tables.** Identify the scores, the weights and whether the weights add to 1 before computing.
- **Trap.** Total computed when a change was asked; points reported as percent.
- **PYQ families.** Professors-by-age tables; smallest money share; fruit-seller profit and profit trends; population-income table; army-civilian mortality and accident rates; bar-chart comparison, value and ratio reading; table inference and assumption validity; table rate and run-rate comparison; weighted-score data table.

## Data interpretation: pies, dual axes and weighted scores (L17)

- **Read first.** Read title, unit, scale and both axes first; never compare a bar's height with a line's height on a two-axis chart.
- **Combine series by numbers.** Revenue per thousand units on two axes: 120/60 = 2.0 -> 135/75 = 1.8 (revenue rose, rate fell); L16 runs the same check from a table, 80/40 = 2 -> 90/50 = 1.8.
- **Pie.** a degrees = a/360 of the total; p% = 3.6p degrees; a share becomes a value only through its own pie's total; a slice can lose share and gain value when the total grows (30% of ₹2,000 crore = ₹600 crore, then 25% of ₹2,600 crore = ₹650 crore).
- **Line graphs.** Steepest segment = largest absolute change, not necessarily largest percent change; 25 basis points = 0.25 percentage points; a falling share can hide a rising count.
- **Break-even.** Revenue = fixed cost + variable cost.
- **Weighted score.** Multiply each component by its weight, add, divide by the sum of weights if not 1; weights can reverse a simple-average ranking.
- **(Advanced) Decision rule.** Label the quantity (level, share, change in level, change in share in points, relative change) before computing.
- **Trap.** Reading an angle as a percentage; comparing across two axes by height.
- **PYQ families.** Earnings and commodity-price graphs; progress and population graphs; graph statement validity; dual-scale comparison; break-even reading; age-group graph; policy rate graph; tax revenue graph; pie-chart sector angle and percentage.

## Decision scenarios and the four-box procedure (L18)

- **Four boxes.** Facts (only what is stated) -> constraints (remove options) -> objective (ranks what is left) -> feasible options (choose the one that best serves the objective with the fewest added assumptions).
- **Elimination screen.** Fails: illegal, coercive, deceptive or concealing, discriminatory or favouring, disproportionate, abdicating. Survives: lawful and fair, clear, proportionate, documented and followed up.
- **Failure condition.** Using the screen alone; two options may pass, and the four boxes decide.
- **Public-office rules.** Discretion is bounded by published criteria and conflict-of-interest rules; the size of an unofficial payment does not change its legality; inaction is a choice and usually fails the objective; firm-sounding and kind-sounding options often hide an unstated assumption.
- **Scenarios that turn on a message.** Classify the barrier first: physical (the setting blocks it), semantic (words read differently), psychological (fear, distrust, stigma), organisational (hierarchy, roles, procedure) or technological (the channel fails). Each points to its own fix. Match the tool to its purpose: inform, consult, persuade, document or obtain feedback. Reject humiliation, threats and concealment; clarify privately, ask the person to restate, agree a check-in. Worked case (L18): two files carry conflicting instructions; asking the issuing authority, writing down the answer and informing the team beats simply following the newer file, which assumes it is correct.
- **(Advanced) Original scenario: an ambiguous reporting format.** Two field offices read a new monthly reporting format differently, so their figures cannot be compared. The barrier is semantic, not a lack of effort. The best option issues a short clarification with one filled-in sample, asks each office to confirm its reading, and checks the next report; a reprimand, or quietly correcting the figures at headquarters, fails the screen.
- **(Advanced) Response patterns.** Stakeholder listening (interests and constraints before action); clear communication (specific, neutral, confirmed); conflict handling (de-escalate, separate people from the problem, fair process); ethical decision (no deception, coercion, discrimination or avoidable harm); administrative feasibility (lawful, proportionate, documented, followed up).
- **Trap.** Treating a communication failure as a character flaw before checking whether the information was clear.
- **PYQ families.** House-allotment discretion; illegal counter payment; villager seeking protection; sugar-allotment favour; communicating family planning; confidential examination paper. Conflict and questionnaire scenarios: decision mechanics only.

## Rapid-recall strip

- Quick checks: decide permutation or combination in one read; sketch a family tree from "only son" clues; write a contrapositive at once; turn a table row into a percentage change.
- Contrapositive yes; converse and inverse no. Valid = true in every diagram.
- Rule accepted only if it reproduces every term or letter.
- Right +90, left -90; displacement is not path.
- "Only son" removes sons only. Rank sum = N + 1; one person's two ranks give p + q - 1.
- Round table (n - 1)!; no halving by default. First digit non-zero. Divide by every repeat factorial.
- P = C x r!; handshakes C(n, 2); lattice C(a + b, b).
- Overlap from max(0, A + B - N) to min(A, B); three sets add back the triple; lcm only for multiples.
- Without replacement multiply conditional fractions; worst case = failing hand + 1; weighings 3^k.
- Grid squares sum of squares; rectangles C(a, 2) x C(b, 2); diagonals n(n - 3)/2 for convex polygons; triangles minus collinear triples.
- Painted cube: 8, 12(n - 2), 6(n - 2)^2, (n - 2)^3.
- Points subtract, percent divides; name the base; share to value through its own total.
- Facts -> constraints -> objective -> feasible option with fewest assumptions.

## Timed gates, error codes and the weight of this family

- **Core gate.** Six items of the seating-count, number-count, overlap, without-replacement and points kind, plus one seating, coding or data item, in nine minutes. Diagnose each miss before checking: rotation or reflection double-counted (C or A), leading zero or repetition rule lost (R), one overlap assumed instead of its bounds (C), without-replacement fraction unchanged (A), share or points measure confused (R or X). Pass: 6 of 6 in nine minutes, with no C or R code, after a 20-minute gap; otherwise redo the matching worked example with fresh values. The gate items are set out in the timed-set practice.
- **(Advanced) Gate.** Ten items in fifteen minutes; mark misses as C, A, X, R or T; a probability retry shows its listed space or conditional fraction, a data retry labels the unit and the quantity asked; advance at 9 of 10 with no conditional-probability, overlap-scope or multi-solution arrangement error.
- **(Advanced) Error codes.** Over-claiming a unique seat (A); invalid syllogism accepted (C); converse used (C); wrong coding rule (R); sample-space error (X); data quantity mismatch (R).
- **(Advanced) Weight and shape of the family.** In one classification of three Prelims papers, reasoning items of this kind together with data-sufficiency items made up roughly a third of all questions. Treat that as an approximate share, not an official break-up: the boundary between the two families is a judgement call, and counts shift from year to year. The recurring shapes are seating and ordering, blood relations and directions, coding, syllogism and deduction, decision scenarios, counting and probability, and data read from tables and graphs. The paper rewards drawing the structure and reading the exact quantity asked.
- **Study links.** Counting rests on factor and number sense, and decision items share the sufficiency mindset of data-sufficiency questions; the Advanced material in these notes is optional speed depth, not a prerequisite for the core gate.

# COVERAGE MATRIX

Every "Where taught" entry below names a lesson (L01 to L18) and the exact heading or phrase under which the unit is taught; every heading and phrase, separated by semicolons, was confirmed by a scripted search of the final lesson text (and of the timed-set practice or these notes where a row points there), with no misses. A practice cell names only the multiple-choice items that test that unit; "Worked check (no item)" means the unit is taught through a worked example in the lesson and has no separate item. Six rows point only to the timed-set practice or to these register notes, because that is where those units are taught (two of them, the study links, are navigation only); a few other rows cite these notes beside a lesson.

## Core units

| Unit or family | Where taught (lesson and heading or term) | Practice cell |
|---|---|---|
| Basic 1 Visual foundation: externalise the structure | L06 — Method: build the graph from the clue that fixes most; Classify and draw; L08 — Method 1: build the frame before the people | Worked check (no item) |
| Basic 2 Linear and circular arrangement | L08 — Method 1: build the frame before the people; Method 3: the round table with one anchor | MCQ 18 (row facing north); MCQ 20 (numbered chairs and opposite seat); MCQ 48 (row seating with family clues) |
| Basic 2 Blood relations | L06 — graph from the clue that fixes most; "only son" and "only daughter" | MCQ 13, 14, 15; MCQ 48 |
| Basic 2 Directions | L05 — track the heading, then sum signed displacements | MCQ 12; MCQ 50 |
| Basic 2 Coding-decoding | L04 — derive the rule from every pair, then test every letter | MCQ 9 |
| Basic 2 Series | L03 — Part A - Number and letter series; Method A: the rule search, in a fixed order | MCQ 6, 7 |
| Basic 2 Visual and figure reasoning | L03 — figural sequences, moving symbols, mirror images; L14 — count by size; L15 — views of a cube and opposite faces | MCQ 8; MCQ 33; MCQ 36 |
| Basic 2 Conditional and statement logic | L01 — the arrow and its contrapositive; chaining arrows | MCQ 1, 2, 3; MCQ 46 |
| Basic 2 Counting | L10 — arranging r of n different things; L11 — combinations and their mirror symmetry | MCQ 23, 24, 25, 26, 27 |
| Basic 2 Probability | L13 — Favourable over total, for equally likely outcomes; A sequence multiplies conditional fractions | MCQ 30; MCQ 45 |
| Basic 2 Data interpretation | L16 — answer the exact quantity asked; L17 — title, unit, scale and both axes first | MCQ 38, 39, 40, 41; MCQ 47; MCQ 49 |
| Basic 2 Interpersonal and communication scenario (reasoning interface) | L18 — four-box procedure; elimination screen | MCQ 42, 43, 44 |
| Basic 2 Communication matching | L09 — Matching two lists through printed codes; L18 — Communication problems inside a decision item | Worked check (no item) |
| Basic 2 Questionnaire design | L09 — Yes-no feature tables; L18 — Design a questionnaire from its objective | Worked check (no item) |
| Basic 3 Step 1 classify and draw | L06 — "Classify and draw"; L08 — frame before the people | Worked check (no item) |
| Basic 3 Step 2 strongest constraint first | L07 — placing the clue that fixes the most; L08 — strongest constraint first, then recheck | MCQ 18; MCQ 48 |
| Basic 3 Step 3 order matters? | L10 — "does order matter?"; L11 — the order test | MCQ 26; MCQ 45 |
| Basic 3 Step 4 exact quantity | L16 — answer the exact quantity asked; L17 — read title, unit, scale and both axes | MCQ 38, 41; MCQ 47 |
| Basic 3 Step 5 scenario elimination | L18 — four-box procedure; elimination screen | MCQ 42, 43, 44 |
| Basic 4 P(n, r) | L10 — arranging r of n different things | MCQ 24 |
| Basic 4 C(n, r) and symmetry | L11 — combinations and their mirror symmetry | MCQ 26, 27; MCQ 45 |
| Basic 4 P = C x r! | L11 — select first, then arrange | Worked check (no item) |
| Basic 4 Repeated letters | L10 — repeated letters | MCQ 23 |
| Basic 4 Circular (n - 1)!, no halving | L08 — counting circular seatings, with no halving by default | MCQ 19, 20 |
| Basic 4 First digit non-zero | L10 — the leading-zero rule | MCQ 24 |
| Basic 4 Complement and the [0, 1] range | L13 — The complement; Every probability lies between 0 and 1; L10 — Advanced: count the complement | MCQ 25 |
| Basic 4 Sequential conditional probability | L13 — a sequence multiplies conditional fractions | MCQ 30 |
| Basic 4 Union and overlap bounds | L12 — two sets; overlap bounds | MCQ 29; MCQ 49 |
| Basic 4 Worst case; size-by-size figure listing | L13 — the worst case and the "plus one" rule; L14 — count by size, exactly once | MCQ 32; MCQ 33 |
| Basic 4 Handshakes C(n, 2); collinearity caveat | L11 — handshakes and pairs; L14 — segments, lines and diagonals; collinear points | MCQ 34 (sets with three collinear corners removed) |
| Basic 4.1 Possible, certain and probability | L01 — Possible, certain and "not necessary"; L13 — Possible, probable and certain | Worked check (no item) |
| Basic 4.2 Implication against equivalence; transitivity; converse | L01 — reading an arrow; chaining arrows; the converse trap | MCQ 1, 3; MCQ 46 |
| Basic 5 Example A (A, C, F, J, O) | L03 — Triangular numbers; 1, 3, 6, 10, 15, 21 | Worked check (no item); the lesson uses the numbers, not the letter form |
| Basic 5 Example B (grandfather's only son) | L06 — the sister through a grandfather | MCQ 15 ("only son" in a six-person family) |
| Basic 5 Example C (P(4, 3) = 24) | L10 — Arranging r of n different things; P(4, 3) = 4 x 3 x 2 = 24 | Worked check (no item) |
| Basic 5 Example D (3 red, 2 blue: 3/5) | L13 — Favourable over total, for equally likely outcomes; P(red) = 3/5 | Worked check (no item) |
| Basic 5 Example E (totals 750 and 450; +50%) | L16 — Total X = 200 + 250 + 300 = 750; Percent rise in X from January to March | Worked check (no item) |
| Basic 5 Example F (conflicting instructions, original) | L18 — two files have conflicting instructions | Worked check (no item) |
| Basic 5 Example G (implication chain) | L01 — chaining arrows | MCQ 1 |
| Basic 5 Example H (five round a table, 24) | L08 — Method 4: counting circular seatings, with no halving by default; Five friends round a table | Worked check (no item) |
| Basic 5 Example I (CAT to DBU, two pairs) | L04 — a shift verified on two pairs | MCQ 9 (rule verified on both words) |
| Basic 5 Example J (overlap 2 to 24) | L12 — Overlap bounds: what the "neither" information allows; In a group of 50, 28 study A and 24 study B | MCQ 29 |
| Basic 5 Example K (five-digit with zero, 96) | L10 — The leading-zero rule; five-digit numbers can be made from 0, 1, 2, 3 and 4 | MCQ 24 |
| Basic 5 Example L (without replacement, 3/10) | L13 — A sequence multiplies conditional fractions; (3/5) x (2/4) = 3/10 | MCQ 30 |
| Basic 5 Example M (table, pie and dual axis) | L16 — Output rose by 10 thousand units; L17 — Method 2: a share becomes a value only through its own total; revenue per thousand units | MCQ 40, 41 |
| Basic 5 Example N (cube views, grid, worst case) | L15 — Method 1: views of a cube and opposite faces; L14 — A 3 x 3 square grid has 9 unit squares; L13 — three of one colour | MCQ 36; MCQ 33; MCQ 32 |
| Basic 6 Must-know facts | L10 — Step 0: does order matter?; L05 — A right turn adds 90 degrees; L06 — "Only son" and "only daughter"; L02 — a conclusion must hold in every arrangement; L01 — Method 1: the arrow and its contrapositive; The converse trap; L16 — Rule 1: answer the exact quantity asked; L08 — Method 3: the round table with one anchor; L12 — Overlap bounds; L18 — The elimination screen | MCQ 1, 12, 13, 19, 24, 29, 38 (each tests one fact) |
| Basic 7 Common traps | L01 — The converse trap; L04 — The trap: a rule guessed from one letter; L05 — The left-turn trap; L13 — Averages, unchanged fractions and halving: three traps | MCQ 1, 9, 12, 24, 30, 36 (distractors built on these traps) |
| Basic 8 Quick checks | L10 — Step 0: does order matter?; L06 — "Only son" and "only daughter"; L01 — Method 1: the arrow and its contrapositive; L16 — Percent rise in X from January to March | Worked check (no item) |
| Basic 9 Mini-drill 1 (5, 11, 23, 47 -> 95) | L03 — multiply then add | MCQ 7 (alternating multiply and add) |
| Basic 9 Mini-drill 2 (LEVEL, 30) | L10 — Words with repeated letters; Worked example (LEVEL) | Worked check (no item) |
| Basic 9 Mini-drill 3 (3 north, right 4, right 3) | L05 — two rights make a U-turn | Worked check (no item) |
| Basic 9 Mini-drill 4 (ten people, 45 handshakes) | L11 — handshakes and pairs | Worked check (no item) |
| Basic 9 Mini-drill 5 (total of Y, 450) | L16 — Total Y = 150 + 180 + 120 = 450 | Worked check (no item) |
| Basic 9 Mini-drill 6 (two blue possible; two red 3/10) | L13 — a draw taken together uses combinations | Worked check (no item) |
| Basic 9 Mini-drill 7 (approved and signed: contrapositive) | L02 — Worked example 3: the arrow form of the same idea | Worked check (no item) |
| Basic 9 Mini-drill 8 (six round a table, 120) | L08 — Method 4: counting circular seatings, with no halving by default; Six people round a table | Worked check (no item) |
| Basic 9 Mini-drill 9 (four-digit from 0 to 3, 18) | L10 — The leading-zero rule; Four-digit numbers from 0, 1, 2 and 3 | Worked check (no item) |
| Basic 9 Mini-drill 10 (least overlap, 3) | L12 — Overlap bounds: what the "neither" information allows; A shelf of 40 books holds 26 hardbacks and 23 novels | MCQ 29; the lesson uses different figures |
| Basic 9 Mini-drill 11 (P(white then white) = 2/15) | L13 — A sequence multiplies conditional fractions; (4/10) x (3/9) = 12/90 = 2/15 | Worked check (no item) |
| Basic 9 Mini-drill 12 (+5 points, +25%) | L16 — keep percentage points apart from percent change | MCQ 40 (a 5-point gap applied to the total) |
| Basic 9 Mini-drill 13 (2 x 2 grid, 5 squares) | L14 — worked check: the 2 x 2 grid | Worked check (no item) |
| Basic 9 Mini-drill 14 (three colours, 4 draws) | L13 — Part B - the worst case and the "plus one" rule; From three colours of balls | MCQ 32 |
| Basic 10 Diagnosis symptoms | L08 — no halving by default; L10 — Error analysis (Advanced); L12 — Overlap bounds; L13 — A sequence multiplies conditional fractions; L17 — Method 1: read title, unit, scale and both axes first | Worked check (no item) |
| Basic 10 Timed nine-minute retry gate | Timed-set practice — Two retry gates; Core gate: six items in nine minutes; Register notes — Timed gates, error codes and the weight of this family; Core gate | Gate items 1 to 6 in the timed-set practice (not multiple-choice) |
| Basic 11 Study links | Register notes — Timed gates, error codes and the weight of this family; Study links | Navigation only; no item |

## Optional Advanced units

| Unit or family | Where taught (lesson and heading or term) | Practice cell |
|---|---|---|
| Advanced 1 Architecture: strongest first; valid only if true in every diagram | L07 — Placing the clue that fixes the most; Advanced: recheck every earlier clue after each placement; L02 — The doctrine: a conclusion must hold in every arrangement | MCQ 18; MCQ 4 |
| Advanced 2 Constraint ordering with recheck | L07 — recheck every earlier clue after each placement (Advanced); L08 — strongest constraint first, then recheck | MCQ 18 |
| Advanced 2 Syllogism validity | L02 — counter-diagram | MCQ 4 |
| Advanced 2 Implication chaining | L01 — implication chaining across negated links (Advanced) | MCQ 3 |
| Advanced 2 Coding rule extraction | L04 — derive the rule from every pair, then test every letter | MCQ 9 |
| Advanced 2 Dice and coin counting | L13 — Dice and coin counting (Advanced); Two dice, P(sum = 7) | Worked check (no item) |
| Advanced 2 Drawing without replacement | L13 — conditional fractions; a draw taken together | MCQ 30 |
| Advanced 2 Inclusion-exclusion, three sets, lcm | L12 — three sets (Advanced); multiples and the lcm (Advanced) | MCQ 28 |
| Advanced 2 Polygon diagonals | L14 — segments, lines and diagonals | Worked check (no item) |
| Advanced 3 Method 1 multi-constraint seating | L08 — Method 2: strongest constraint first, then recheck; The unique order is P, Q, R, T, S | MCQ 18 |
| Advanced 3 Method 2 EARTH and MARS | L04 — the shift of two | Worked check (no item) |
| Advanced 3 Method 3 dice P(sum 7) | L13 — Two dice, P(sum = 7) | Worked check (no item) |
| Advanced 3 Method 4 solve chains backwards | L01 — Advanced Method 4: solve conditional chains backwards | MCQ 3 |
| Advanced 4 Time-saving techniques | L07 — Placing the clue that fixes the most; L02 — counter-diagram; L10 — Advanced: count the complement; L12 — Two sets: correcting the double count | MCQ 25; MCQ 4 |
| Advanced 5 Boundary cases | L08 — If several seatings survive, only facts true in all of them are certain; L02 — Existential; L01 — Possible, certain and "not necessary"; L13 — equally likely | MCQ 22; MCQ 45 (equal likelihood belongs to hands of cards, not to the two marks) |
| Advanced 6 Traps: one-solution placement, sounds-right syllogism, converse, one-letter code, unchanged fraction, overlap, points as percent | L08 — Method 8: checking statements against the finished seating; L02 — counter-diagram; L01 — The converse trap; L04 — The trap: a rule guessed from one letter; L13 — without replacement; L12 — Advanced: three sets; L16 — Rule 3: keep percentage points apart from percent change | MCQ 4, 9, 18, 28, 30, 38 |
| Advanced 6 Trap: adding probabilities of non-exclusive events | L13 — non-exclusive events (Advanced) | Worked check (no item) |
| Advanced 7 Error analysis codes | L10 — error analysis (Advanced); Timed-set practice — error codes and their repairs | Worked check (no item) |
| Advanced 8 Drill 1 (at least one head, 7/8) | L13 — The complement; P(at least one head) = 1 - 1/8 = 7/8 | Worked check (no item) |
| Advanced 8 Drill 2 (decagon diagonals, 35) | L14 — Method 3: segments, lines and diagonals; A nonagon has 9 x 6 / 2 = 27 diagonals; Register notes — Plane-figure counting; a decagon has 10 x 7 / 2 = 35 | Worked check (no item) |
| Advanced 8 Drill 3 (SUCCESS, 420) | L10 — Words with repeated letters; SUCCESS | Worked check (no item) |
| Advanced 8 Drill 4 (1 to 100, at least one of 2, 3, 5: 74) | L12 — multiples and the lcm (Advanced) | Worked check (no item) |
| Advanced 8 Drill 5 (sum at least 10, 1/6) | L13 — two dice | Worked check (no item) |
| Advanced 8 Drill 6 (at least one white, 2/3) | L13 — a draw taken together | Worked check (no item) |
| Advanced 8 Drill 7 (diploma and graduate) | L02 — universal negatives chain cleanly | MCQ 4 (universal-negative chain) |
| Advanced 8 Drill 8 (opposite seat, not adjacent, 12) | L08 — restrictions at a round table | MCQ 20 |
| Advanced 8 Drill 9 (second white given first white, 1/3) | L13 — A sequence multiplies conditional fractions; told the first was white | Worked check (no item) |
| Advanced 8 Drill 10 (revenue per thousand units, 2 and 1.8) | L17 — Method 1: read title, unit, scale and both axes first; revenue per thousand units | MCQ 41 |
| Advanced 9 Timed fifteen-minute gate | Timed-set practice — Two retry gates; Optional Advanced gate: ten items in fifteen minutes; Register notes — Timed gates, error codes and the weight of this family; Ten items in fifteen minutes | Items 41 to 50 taken as one timed set |
| Advanced 10 Multi-step DI: bases, level against share, points against percent | L16 — multi-step reading: different bases do not cancel (Advanced); L17 — decision rule for multi-step reading (Advanced) | MCQ 38 |
| Advanced 11 Response patterns (listening, clarity, conflict, ethics, feasibility, matching, barriers, questionnaire) | L18 — Visual: the four-box procedure; The elimination screen; Communication problems inside a decision item; Stakeholder listening (Advanced) | MCQ 43, 44 |
| Advanced 11 Original scenario (ambiguous reporting format) | Register notes — Decision scenarios and the four-box procedure; Original scenario: an ambiguous reporting format | Worked check (no item) |
| Advanced 11 Original classification drill | L09 — Matching two lists through printed codes; Register notes — Logic grids and matching; Classification drill | Worked check (no item) |
| Advanced 12 Recurring shapes of this family | L01 — UPSC application; Register notes — The recurring shapes are seating and ordering | Worked check (no item) |
| Advanced 12 Share of this family together with data sufficiency | Register notes — Timed gates, error codes and the weight of this family; roughly a third of all questions | Worked check (no item) |
| Advanced 13 Study links | Register notes — study links | Navigation only; no item |

## Question families

| Unit or family | Where taught (lesson and heading or term) | Practice cell |
|---|---|---|
| Conditional and implication logic; either-or falsification; consistency | L01 — Method 2: chaining arrows (transitivity); Falsifying an either-or claim; Checking a set of statements for consistency | MCQ 1, 2, 3; MCQ 46 |
| Syllogism and multi-conclusion sets | L02 — Part A - Set containment and the counter-diagram; Part B - Multi-statement and multi-conclusion sets | MCQ 4 |
| Statement-conclusion items, cause from cases, case-split | L02 — Statement-conclusion items with everyday content; Finding a cause from a table of cases; Case-split deduction | Worked check (no item) |
| Truth-teller and suspect statements | L02 — Part C - Truth-teller and suspect-statement logic | MCQ 5 |
| Statement evaluation and statement-relationship items | L02 — The job each statement does; Numbered statements and combination options | Worked check (no item) |
| Number and letter series; cyclic series | L03 — Part A - Number and letter series; Cyclic series: months, days and clock positions | MCQ 6, 7 |
| Analogies and odd-one-out | L03 — Part B - Analogies and odd-one-out groups | Worked check (no item) |
| Figural sequences, matrices, mirror and embedded figures | L03 — Part C - Figural sequences, moving symbols, mirror images and matrices; Embedded figures | MCQ 8 |
| Letter, number and word codes; operator substitution; coded constraints | L04 — word-code deduction; symbol and operator substitution; coded values under constraints | MCQ 9 |
| Alphametics | L04 — alphametics: constrained digit solving with carries | MCQ 10 |
| Direction sense and square paths | L05 — Method 1: track the heading, then sum signed displacements; Method 2: rotations by stated angles; Two walkers on a square path | MCQ 12; MCQ 50 |
| Directed networks: reachability, necessity, revisit | L05 — Part B - Directed networks; Method 3: treat each arrow as one-way | MCQ 11 |
| Blood relations, coded relations, sufficiency, ages | L06 — Method: build the graph from the clue that fixes most; Reading coded relations; Statement sufficiency for a relation; Ages on a family graph | MCQ 13, 14, 15; MCQ 48 |
| Ranking positions, median and tournament totals | L07 — switching the end you count from; the middle person and tournament totals | MCQ 16 |
| Comparison chains: age, height, taste, speed, price, weight, scores | L07 — Ties, one-direction chains and missing links; Advanced where it extends: comparisons that carry numbers | MCQ 17; MCQ 50 (distances ordered) |
| Linear, circular and office or group seating | L08 — Method 1: build the frame before the people; Method 3: the round table with one anchor; Method 4: counting circular seatings; Method 6: keeping people apart in a row (the gap method); Method 7: row-position counts; Method 8: checking statements against the finished seating; Method 9: offices, floors and groups | MCQ 18, 19, 20; MCQ 48 |
| Logic grids, boxes, scheduling, selections, classification, segment matching | L09 — Visual: the elimination grid and the matching table; Exactly-one statements and wrong labels; Rotations by remainder, and free days; Choosing teams under conditions; Yes-no feature tables; Matching two lists through printed codes | MCQ 21, 22 |
| List-matching items (List I against List II) | L09 — Matching two lists through printed codes | Worked check (no item) |
| Digit, letter, colour and code permutations | L10 — Visual: the slot diagram; The leading-zero rule; Words with repeated letters; Codes, PINs and passwords | MCQ 23, 24, 25 |
| Team selections and assignments | L11 — Include, exclude, keep apart; Ordered pairs, triplets and assignments | MCQ 26; MCQ 46 |
| Route counts on a lattice and on a directed network | L11 — Routes on a grid and on one-way roads | MCQ 27 |
| Partitions, denominations, integer solutions, circular selections | L11 — Splitting a number into parts; Gaps, circles and passing | Worked check (no item) |
| Venn and set-overlap items | L12 — Two sets: correcting the double count; Overlap bounds; Advanced: three sets; Membership tables for named people; Fractions of one whole | MCQ 28, 29; MCQ 49 |
| Probability, lottery, cards, derangements | L13 — Part A - probability as a fraction of a listed world; Draws with repeats, wrong placements | MCQ 30; MCQ 45 |
| Worst-case draws, queues, knockouts | L13 — Part B - the worst case and the "plus one" rule; Queues and elimination counts | MCQ 32 |
| Weighing and crossing strategies; weight inequalities | L13 — Part C - weighing and crossing strategies; Crossing with one torch; L07 — Scaled and summed comparisons: weight chains | MCQ 31 |
| Plane-figure counting | L14 — Method 1: count by size, exactly once; Method 2: rectangles and parallelograms from two families of lines; Method 3: segments, lines and diagonals; Method 4: triangles by type, removing collinear triples; Method 5: board diagonals and runs of cells | MCQ 33, 34 |
| Cube views and nets | L15 — views of a cube; nets and folding | MCQ 36 |
| Painted cubes, cuts, solid counting | L15 — Method 3: painted cubes by class; Method 4: cuts and partitions; Method 5: partly painted blocks and patterns; Method 6: colouring faces and counting stacked cubes | MCQ 35, 37 |
| Tables and bar charts: levels, changes, shares, rates | L16 — Rule 1: answer the exact quantity asked; Rule 2: name the base of every percentage; Rule 3: keep percentage points apart from percent change; Rule 4: rates per unit before comparisons; Rule 5: cross-tables and the two margins; Rule 6: rises, growth rates and running totals; Rule 7: what a table can and cannot support | MCQ 38, 39 |
| Weighted-score tables | L16 — weighted-score tables; L17 — weighted scores, by unit and weight | MCQ 47 |
| Line, dual-axis, policy-rate and break-even graphs | L17 — Method 1: read title, unit, scale and both axes first; Method 3: line graphs, slopes and steps; basis points; Break-even is where revenue | MCQ 41 |
| Pie charts | L17 — a share becomes a value only through its own total | MCQ 40 |
| Public-office decision scenarios | L18 — applying the procedure to recurring public-office families | MCQ 42, 43, 44 |
| Conflict and questionnaire scenarios (decision mechanics) | L18 — Communication problems inside a decision item; Design a questionnaire from its objective; The elimination screen | Worked check (no item) |

## Item-to-lesson map (MCQ 1 to 44)

| Item | Where taught (lesson and heading or term) | What the item tests |
|---|---|---|
| MCQ 1 | L01 — chaining arrows; the contrapositive | Two-link chain read through its contrapositive |
| MCQ 2 | L01 — falsifying an either-or claim | Which finding breaks a rule with an inclusive "or" |
| MCQ 3 | L01 — Translating the English forms into arrows; Advanced Method 4: solve conditional chains backwards | Three links with "only if" and "unless", chained backwards |
| MCQ 4 | L02 — Part A - Set containment and the counter-diagram | Four conclusions from three categorical statements |
| MCQ 5 | L02 — Part C - Truth-teller and suspect-statement logic | Exactly one true statement among three clerks |
| MCQ 6 | L03 — Part A - Number and letter series | Next term by differences |
| MCQ 7 | L03 — Method A: the rule search, in a fixed order; multiply then add | A two-step rule checked on every term |
| MCQ 8 | L03 — Moving symbols in a grid and around a ring | A dot moving round the eight outer cells with a growing step |
| MCQ 9 | L04 — derive the rule from every pair, then test every letter | A code rule that must fit two words |
| MCQ 10 | L04 — Alphametics: constrained digit solving with carries | Two-digit addition with a three-digit total |
| MCQ 11 | L05 — Part B - Directed networks; Method 3: treat each arrow as one-way | Which claim holds on every route of a one-way network |
| MCQ 12 | L05 — Method 1: track the heading, then sum signed displacements | Two walkers compared by displacement |
| MCQ 13 | L06 — Relation words as compressed walks; The vocabulary as paths | A relation read along a path through a parent |
| MCQ 14 | L06 — reading coded relations | Three coded edges chained into one relation |
| MCQ 15 | L06 — "Only son" and "only daughter"; Couples, counts and family inference | A six-person family with sex and generation fixed by the clues |
| MCQ 16 | L07 — the middle person and tournament totals | Points totals in a round-robin tournament |
| MCQ 17 | L07 — scaled and summed comparisons: weight chains | Largest multiple forced by a summed and a scaled comparison |
| MCQ 18 | L08 — Method 1: build the frame before the people; Method 2: strongest constraint first, then recheck; Method 8: checking statements against the finished seating | Row seating facing north |
| MCQ 19 | L08 — Method 4: counting circular seatings, with no halving by default; a glued block has 2 internal orders | Three people kept together round a table, no halving |
| MCQ 20 | L08 — labelled seats; restrictions at a round table | Numbered chairs, an even-chair rule and an opposite seat |
| MCQ 21 | L09 — Exactly-one statements and wrong labels; Visual: the elimination grid | Days fixed when exactly one of four statements is false |
| MCQ 22 | L09 — Reading down the columns; The final reread | What can be true when a pair stays open |
| MCQ 23 | L10 — repeated letters | Repeated letters with a block that must stay together |
| MCQ 24 | L10 — the leading-zero rule | Even four-digit numbers with zero available |
| MCQ 25 | L10 — Advanced: count the complement; Codes, PINs and passwords | At least one repeat, by the complement |
| MCQ 26 | L11 — Include, exclude, keep apart | "At least two" counted by cases |
| MCQ 27 | L11 — Routes on a grid and on one-way roads | Shortest routes through a fixed junction |
| MCQ 28 | L12 — three sets (Advanced) | Exactly one of three sets |
| MCQ 29 | L12 — Overlap bounds: what the "neither" information allows | Two-set overlap with a "neither" group |
| MCQ 30 | L13 — a sequence multiplies conditional fractions | Ordered draws without replacement |
| MCQ 31 | L13 — Part C - weighing and crossing strategies | A balance plan for one odd item |
| MCQ 32 | L13 — Part B - the worst case and the "plus one" rule; respecting how many of each item actually exist | Failing hand capped by a small stock, plus one |
| MCQ 33 | L14 — count by size; two families of lines | Rectangles counted along grid lines |
| MCQ 34 | L14 — Method 4: triangles by type, removing collinear triples; The same test extends to four corners | Quadrilaterals from points on two parallel lines, removing sets with three corners on one line |
| MCQ 35 | L15 — painted cubes by class | Small cubes with exactly two painted faces |
| MCQ 36 | L15 — nets and folding | Opposite faces read from a net |
| MCQ 37 | L15 — cuts and partitions | Unpainted pieces after cuts in three directions |
| MCQ 38 | L16 — answer the exact quantity; name the base | Shares turned into levels, then a percent change |
| MCQ 39 | L16 — rates per unit before comparisons | Rates per lakh compared |
| MCQ 40 | L17 — a share becomes a value only through its own total | Pie angle and percent label turned into a value gap |
| MCQ 41 | L17 — Method 1: read title, unit, scale and both axes first; revenue per thousand units | Per-unit value across two axes |
| MCQ 42 | L18 — list the constraints that remove options | Constraints remove days, the objective ranks the rest |
| MCQ 43 | L18 — the elimination screen | Response to an improper offer under a contract |
| MCQ 44 | L18 — choose the feasible option with the fewest added assumptions | Feasible action using information already held in the office |

## Cumulative items (MCQ 45 to 50)

Each cumulative item joins two or more lessons and is not a repeat of any lesson item.

| Item | Where taught (lessons combined) | What the item tests |
|---|---|---|
| MCQ 45 | L11 — Combinations and their mirror symmetry; L13 — Favourable over total, for equally likely outcomes; L10 — Step 0: does order matter? | Lessons 10, 11 and 13 (with the exact-quantity label of Lesson 16): chance of exactly two stars in a random hand of four cards |
| MCQ 46 | L01 — Method 1: the arrow and its contrapositive; Method 3: test a claim by assuming its denial; L11 — Include, exclude, keep apart | Lessons 1 and 11: which claim holds for every valid team of three |
| MCQ 47 | L17 — weighted scores; L16 — exact quantity asked; L07 — ordering | Lessons 7, 16 and 17: leader and margin on a weighted score |
| MCQ 48 | L06 — Method: build the graph from the clue that fixes most; L08 — Method 2: strongest constraint first, then recheck | Lessons 6 and 8: a family seated in a row facing north |
| MCQ 49 | L12 — Overlap bounds: what the "neither" information allows; L16 — Rule 2: name the base of every percentage | Lessons 12 and 16: overlap share within a named subgroup |
| MCQ 50 | L05 — Method 1: track the heading, then sum signed displacements; path length; L07 — Ties, one-direction chains and missing links | Lessons 5 and 7: straight-line distances placed in order |

## Counts and gaps

- Core unit rows: 66. Optional Advanced unit rows: 36. Question-family rows: 35. Item rows: 50.
- Every core and Advanced unit is taught. Four units are taught outside the lessons: the nine-minute core retry gate and the fifteen-minute Advanced gate (both in the timed-set practice, "Two retry gates", and summarised in these notes), the approximate share of this family together with data sufficiency (in these notes, with its qualification), and the Advanced original scenario on an ambiguous reporting format (in the decision-scenarios block of these notes). The two study-link units are navigation only and are summarised in these notes.
- The trap of adding the probabilities of non-exclusive events is taught in L13, "Non-exclusive events (Advanced)".
- No unit is missing.

# SOURCE LEDGER

This ledger states what was read, what was used as evidence, which sources were not used and why, and how each disputed or mismatched point was handled. It is the verification record for the lessons above; it is not teaching material.

## Sources read and used

- **Canonical Basic owner:** `upsc-ai-kit/knowledge/CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md`. Teaching sections 1 to 11 (lines 1-352) were read in full and drive the lesson content and the register notes. Its generated PYQ integration blocks (lines 352-784) were read for family labels and counts only.
- **Canonical Advanced owner:** `upsc-ai-kit/knowledge/CSAT/advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md`. Sections 1 to 13 (lines 1-267) were read in full; every Advanced unit is taught and labelled. Its generated PYQ block (lines 267-525) was read for counts only.
- **Master Framework:** `upsc-ai-kit/knowledge/CSAT/00_Master-Framework.md`, lines 20-42 and 255-302 only. Lines 255-302 (the audited 2024-2026 Set-A trend table and its limitations) are the source of the Advanced owner's "78 of 240 audited items (32.5%)" figure: that figure is the count for the logical-reasoning family and the data-sufficiency family together (45 + 33 of 240), not for this family alone (45 of 240, about 19%). The register notes therefore state only an unattributed approximate share ("roughly a third", for the two families together) and carry the Master Framework's qualifications: the counts are a classification of OCR text, not an official break-up; the boundary between the two families is a judgement call; the 2026 row is provisional. Lines 20-42 (the paper's marking rule and the 33% qualifying minimum of 66 of 200) were read only to confirm that no learner-facing rubric states an official mark, deduction or qualifying figure; none does. No other Master Framework line was used. `00_Question-Audit-Ledger.md` was not read.
- **Syllabus mapping:** `upsc-ai-kit/knowledge/CSAT/OFFICIAL-UPSC-SYLLABUS-MAPPING.md`, read in full in the first build pass. The logical reasoning and data interpretation clauses map to this topic's owners.
- **PYQ routing ledgers (family 06 rows):** `upsc-ai-kit/knowledge/_PYQ-ROUTING-CSAT-2018-2023.md` (127 rows with family 06), `_PYQ-ROUTING-CSAT-2024-2025.md` (24 rows) and `_PYQ-ROUTING-CSAT-2026.md` (21 rows, provisional). Only the year, question number, neutral type and family columns were extracted; route and status text was not used as evidence of an answer.
- **Solved library topic list for 2013-2017:** `solved_pyqs/topics/csat/logical-reasoning-coding-counting-and-di.md`, the `### 2013` to `### 2017` entries (123 linked questions). Only the question number, the neutral title and the link target were extracted. All 295 link anchors resolve to an existing anchor in the year files.
- **PYQ stems (question text and options only):** for the repair pass, the stems of all 295 linked items were read from `solved_pyqs/papers/<year>/prelims-csat.md` to write the neutral demand and approach statement of each entry and to compare the structure of the cumulative items and worked examples with the linked questions. For 2013-2018 only the "Verified booklet transcription" section was read; for 2019-2026 only the text under each question heading, stopping at the first metadata, answer, key or solution line. The 2013 file's key-status header was read; it states that the official key accepts two responses for each of Q75-Q80, and the PYQ section states that directive for those six items without indicating either response. One disclosure: in an earlier round, while the 2020 file's format was being inspected, the answer and reasoning lines of one item outside this topic (2020 Q7) were displayed once before the extraction filter was in place. Nothing from them was used, and no later round displayed any answer line.
- **Reference style sessions:** `live_sessions/CSAT/05-Algebra-Inequalities-and-Data-Sufficiency/Learning-Session-Live-Edition.md` (lines 1-215, final-arc headings and the cumulative, timed-set and remediation openings), read in the first build pass. For the shape of one complete lesson, the first lesson of three Philosophy-Optional reference sessions was read; the line ranges below are the lines actually read and the lines each lesson occupies:
  - Nyaya-Vaisesika (`live_sessions/Philosophy-Optional/01-Nyaya-Vaisesika/Learning-Session-Live-Edition.md`), lesson 1 "Two Allied Realist Schools": the lesson occupies lines 13-246 (its pre-teach checklist is lines 7-11; lines 248-253 open lesson 2). Lines 1-260 were read, so the whole of lesson 1 was read.
  - Yoga (`live_sessions/Philosophy-Optional/06-Yoga/Learning-Session-Live-Edition.md`), subtopic 1 "Yoga as Seśvara-Sāṃkhya": the subtopic occupies lines 49-400 (its pre-teach checklist is lines 43-47; lines 402-405 are a learner remark and lines 407-413 open subtopic 2). Lines 1-425 were read, so the whole of subtopic 1 was read.
  - Mimamsa (`live_sessions/Philosophy-Optional/07-Mimamsa/Learning-Session-Live-Edition.md`), subtopic 1 "Dharma-jijñāsā and the Two Schools": the subtopic occupies lines 40-280 (its pre-teach checklist is lines 34-38; lines 284-290 open subtopic 2). Lines 1-300 were read, so the whole of subtopic 1 was read.
  An earlier version of this ledger gave these ranges as 1-247, 1-400 and 1-282 and described them as read in full; those ranges did not match the lesson boundaries (the Yoga range stopped before lines 401-412). The ranges above replace them. The three lessons were used for the shape of a complete lesson (visual first, plain explanation, traps, revision notes, mastery and remedial questions) only; no doctrine, wording or structure was copied. Those reference lessons print the answers to their own Philosophy practice questions; these were seen while reading and have no bearing on any CSAT item.
- **Validator and rules:** `tools/validate_live_session.py`, read in full before drafting. Rules: `live_sessions/LIVE-SESSION-GENERATION-RULES.md` (CSAT profile, structural and generation locks, language standard, reference arc), `instructions/GENERATION-OPTIMIZATION-AND-INTEGRITY.md`, `instructions/LIVE-SESSION-VALIDATION-AND-RELEASE.md` and `instructions/README.md`.

## Sources not used and why

- **Answers and solutions of PYQs:** no answer, key letter, rationale or solution text was read for any linked item, and none is reproduced or inferred. The PYQ section gives a neutral demand and a route for each item, never a result.
- **Question Audit Ledger:** `upsc-ai-kit/knowledge/CSAT/00_Question-Audit-Ledger.md` was not read; the Master Framework lines above were sufficient for the one share statement.
- **Notes and packages:** the Final-Learning-Packages folder, `upsc-ai-kit/knowledge/Learner-v2-Refreshed/`, any learner-v2 or `learning-sessions/v2` artifact, `final-mcq/` and `quick_galance/` were not read, searched, cited or compared against, in line with the permanent live-session exclusion.

## Ledger-versus-library discrepancy (2023)

The routing ledger and the solved library disagree on seven 2023 questions. The ledger was treated as authoritative for family assignment in 2018-2026, and the canonical owner's generated 2023 table agrees with the ledger.

- Ledger assigns family 06 but the library's topic list does not: 2023 questions 18, 30, 40, 69 and 79. These are placed in the lesson that teaches their method (Lessons 15, 14, 3, 13 and 15 respectively, as listed in the PYQ section). Question 69 (weighing coins) is kept in Lesson 13 under the ledger's family 06.
- Library assigns topic 06 but the ledger assigns family 02: 2023 questions 47 and 76. These are not placed in this file, because the ledger routes them elsewhere.

No other year differs: for 2018-2022 and 2024-2026 the library's topic-06 list matches the ledger exactly.

## Other notes

- Items from 2013-2017 come only from the library's topic list; no ledger covers those years.
- Placement changes in the repair pass: 2019 Q79 and Q80 (weight inequalities) are now taught in Lesson 7 (comparison chains) instead of Lesson 13.
- Placement and label changes in the second repair round: 2018 Q1 (triangles in a drawn figure) is placed in Lesson 14, where triangle counting by shared vertex and base line is taught, instead of Lesson 15; 2019 Q10 stays in Lesson 15, which now teaches cutting into cubes of two sizes, and its approach line follows that method; 2026 Q77 stays in Lesson 2, which supplies only the numbered-statement format for it; the 2026 Q72, Q73 and Q75 labels read "List matching" instead of "Numbered-heads matching"; the 2026 Q71 and Q77 approach lines name only methods taught in the lessons; the six 2013 Q75-Q80 approach lines are now distinct and follow each stem, and the demand lines for Q75, Q77 and Q78 were corrected to match their stems; the directive for those six items still states that the official key accepts two responses, and no approach indicates either response.
- The 2026 paper is provisional. Every 2026 entry is labelled provisional in the PYQ section. No key, option letter or inferred pairing is recorded or taught. The 2026 items Q72-Q77 belong in content to the separate communication session (Topic 07); here they are linked only for their reasoning structure, and their labels in the PYQ section are neutral question-type labels.
- The PYQ section's approach lines for 2013 Q75-Q80 are six distinct, stem-specific lists of tests that give neither accepted response. A second-round search of Lesson 18 for the distinctive elements of those six questions (secretary, sugar, wedding, family planning, villager, landlord, taxi, transport counter, question paper) found them only in neutral family names in the lesson's PYQ-application bullets and in two one-line examples in the elimination-screen table (a scarce allotment to an influential applicant; a slow counter). Lesson 18 also contains an original situation about custody of sealed confidential papers, which shares the confidential-material family of 2013 Q80; whether its structure differs sufficiently is a teaching-side judgement for Lesson 18, not something the PYQ section depends on. The approach lines do not depend on the lesson wording.
- No current-affairs check was made, because the paper is an aptitude paper with no meaningful current-affairs linkage.
- Third repair round: three approach lines were rewritten without changing any placement. 2013 Q11 now follows Lesson 5's one-way-network method (one mode's links as a list, then a reachability test from Q); 2026 Q77 is a neutral test instruction that teaches no answer or pairing; 2026 Q71 uses the supports / weakens / unrelated vocabulary of Lesson 2. The coverage matrix and the register notes were rechecked by a script that searches the final lesson text for every cited heading, phrase and figure; cells that named paraphrased headings were replaced by exact headings or phrases, source example and drill labels were removed from the register notes, and figures absent from the lessons were replaced by the lessons' own figures. The structure of each changed lesson item and worked example was compared with the stems of the questions linked to its lesson, reading stems only.

## SOURCE-MANIFEST GATE

| Category | Status | Evidence or reason |
|---|---|---|
| Canonical Markdown | checked | Basic owner lines 1-352 and Advanced owner lines 1-267 read in full; generated PYQ blocks read for counts; syllabus mapping read in full; Master Framework lines 20-42 and 255-302 read for the one share statement and its qualifications. |
| Final learner package | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule. |
| Layered/complete session | checked | One complete first lesson each: Nyaya-Vaisesika lesson 1 (occupies lines 13-246; lines 1-260 read), Yoga subtopic 1 (occupies lines 49-400; lines 1-425 read), Mimamsa subtopic 1 (occupies lines 40-280; lines 1-300 read); CSAT 05 live session lines 1-215 read for the final-arc structure. Style only. |
| Solved workbook | not relevant | Permanently excluded from all live-session work by the governing source-exclusion rule. |
| Advanced dossier | checked | `upsc-ai-kit/knowledge/CSAT/advanced/06_Logical-Reasoning-Coding-Counting-and-DI.md` read in full for teaching lines 1-267. |
| OCR books | not available | `books/` holds only previous-paper scans (`books/previous_papers_2013_2018`); no OCR-searchable book was consulted for this topic, so no book context is recorded. |
| PYQs through 2026 | checked | Family-06 ledger rows for 2018-2026 (172 items) and the library topic list for 2013-2017 (123 items); anchors verified in every year file; stems only read for demand and approach statements; 2026 linkage provisional; 2023 discrepancy disclosed above. |
| Official live sources | not relevant | Aptitude paper with no meaningful current-affairs linkage; no live source is used for any claim. |
