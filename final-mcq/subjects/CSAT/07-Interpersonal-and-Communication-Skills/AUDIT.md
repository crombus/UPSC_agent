# csat-07 — Verification audit (judgement items)

Date of audit: 2026-11-01. Scope: `revision-1/`, `revision-2/`, `revision-3/` (30 items each). No item is numerical, so keys are verified by **principle mapping**: each key is traced to the owner principle that decides it, and each distractor is tied to a named error pattern. Mechanical checks were run with a Python script kept outside the repository (`/tmp/mcq_audit/check_csat07.py`, with `cue_check.py` and the edit scripts beside it).

## 1. Method

1. **Principle mapping.** For each item, the decisive owner principle is recorded (table in section 3). A key is accepted only if (a) the owner principle selects it and (b) each other option fails that principle or a named error pattern. Where two options could both be defended, the item was rewritten or the wording narrowed until only one survives.
2. **Format and key integrity (script).** The script checks: IDs run R*n*-Q01 to Q30 in order; each item has exactly four options labelled A–D; each answer header `**R*n*-Qnn — X.**` matches the planned key; each entry has an explanation for every option (A–D), one option labelled "(key)" whose letter equals the header, a trap, and a time target; and no placeholder or "all/none of the above" text appears.
3. **Option-length balance (script).** Character lengths of A–D are compared. Measured: the share of items in which the correct option is uniquely longest, the longest/shortest ratio, and the letter distribution.
4. **Cue check (script).** Hits for consultation, legal, record, review and similar cue words are counted separately for the key and for distractors, so that the key does not carry the only "consult" or "law" language.
5. **Cross-set similarity (script).** Stems are compared across sets to confirm that the three sets are not reshuffles.

## 2. Results

### 2.1 Format and key integrity

| Set | Items | Key-header vs plan | Key label "(key)" vs header | Errors |
|---|---|---|---|---|
| R1 | 30 | 30/30 match | 30/30 match | 0 |
| R2 | 30 | 30/30 match | 30/30 match | 0 |
| R3 | 30 | 30/30 match | 30/30 match | 0 |

### 2.2 Correct-letter distribution

| Set | A | B | C | D | Share range |
|---|---|---|---|---|---|
| R1 | 8 | 8 | 7 | 7 | 23–27% |
| R2 | 7 | 8 | 7 | 8 | 23–27% |
| R3 | 8 | 7 | 8 | 7 | 23–27% |

Every letter is within the 20–30% band in each set.

### 2.3 Option-length balance

| Set | Correct option uniquely longest | Median longest/shortest option ratio | Maximum ratio | Items with ratio above 1.25 |
|---|---|---|---|---|
| R1 | 1 of 30 (3.3%) | 1.10 | 1.23 | 0 |
| R2 | 4 of 30 (13.3%) | 1.10 | 1.23 | 0 |
| R3 | 7 of 30 (23.3%) | 1.12 | 1.22 | 0 |

The target is at most about 25–30% uniquely longest, and all three sets meet it. Qualifiers (such as "only if", "after", "provisional", "in writing") were added to distractors as well as to keys.

### 2.4 Cue check

Consultation, law and procedure words appear in distractors as often as in keys. Across each set, "consult", "rule", "record", "procedure" and "authority" were checked separately for keys and distractors, and no key carries a cue that its distractors lack. The highest key-only cue is "law/lawful" in R3 (two keys, no distractors), which affects only two items and is not a substitute for the principle.

### 2.5 Cross-set distinctness

The highest stem similarities between sets are 0.52–0.65 (SequenceMatcher on stem text). Each pair is the same owner theme with different facts, roles and options, for example R1-Q28 vs R3-Q28 (promised-date delay) and R1-Q17 vs R3-Q05 (rumour). No stem or option is repeated across sets.

## 3. Principle-based verification of every key

Format: ID — key — deciding owner principle — strongest distractor and its failing pattern.

### Revision 1

| ID | Key | Deciding principle | Strongest distractor and failure |
|---|---|---|---|
| R1-Q01 | C | Feedback confirms understanding (B§1, B§3) | A: one-way re-sending of slides |
| R1-Q02 | A | Formal written channel for a binding, traceable instruction (B§2) | B: informal relay with no record |
| R1-Q03 | B | Active listening: paraphrase and clarify (B§3) | C: promise of transfers before facts |
| R1-Q04 | D | Listening is not agreement; record the concern (B§3, B§11) | A: dismisses the objection as resistance |
| R1-Q05 | A | Semantic barrier: plain language, tested (B§4) | B: glossary leaves the wording in place |
| R1-Q06 | C | Organisational barrier: controlling authority, one instruction (B§4, B§7) | D: recency mistaken for authority |
| R1-Q07 | D | Physical and technological barriers: alternate, accessible channels (B§4, B§5) | A: proceeds online, excluding members |
| R1-Q08 | D | Psychological barrier: private, no-blame reporting route (B§4, B§5) | B: threatens discipline, deepening fear |
| R1-Q09 | A | Assertiveness: facts, need and next step (B§5) | B: withdraws, then issues a conditional threat |
| R1-Q10 | C | Assertive versus passive or aggressive style (B§5) | A: passive dismissal of the miss |
| R1-Q11 | B | Emotional regulation, with a boundary on abuse (B§5, A§5) | A: matches volume and expels |
| R1-Q12 | D | Position versus interest; test options against both (B§6, A§4) | A: allocation by rank (positional) |
| R1-Q13 | A | Establish facts first (B§6 PAUSE, A§9) | B: accepts the contractor's account as fact |
| R1-Q14 | C | Compromise is not automatically correct; reject unsupported claims (B§6) | B: "provisional" split of the same unsupported claim |
| R1-Q15 | B | Serious allegation goes to the designated process; "talk first" trap (B§6, B§11) | A: informal first, report only if repeated |
| R1-Q16 | D | Service failure: acknowledge, facts, remedy, timeline (B§7) | A: blames a vendor without evidence |
| R1-Q17 | A | Rumour: verify, credible channel, correct (B§7, A§6) | B: denial with no detail |
| R1-Q18 | B | Sensitive matter: minimum necessary disclosure via secure channel (B§7) | A: full medical detail by email |
| R1-Q19 | B | Stakeholder opposition: hear interests, record objections (B§7, A§2) | D: survey rigged to two preferred routes |
| R1-Q20 | B | Double-barrelled item (B§8) | Not applicable: the distractors are single-issue |
| R1-Q21 | A | Neutral wording (B§8) | B: leading ("every responsible household should welcome") |
| R1-Q22 | C | Objective-to-data: family size and budget bear on feasibility (B§8) | D: family size with dietary needs (scope confusion) |
| R1-Q23 | C | Fairness: no preferential queue; record the request (B§9 legality) | B: preference put in writing |
| R1-Q24 | B | Proportionality: verify before sanction (B§9) | A: immediate suspension before facts |
| R1-Q25 | D | Feedback: specific, behavioural, actionable (B§3) | B: attributes motive ("not interested") |
| R1-Q26 | A | Open question for exploration without presumed cause (B§3) | C: presumes a cause (vehicles) |
| R1-Q27 | D | Persuasion by reasons and evidence, not pressure or selection (B§5) | C: shows only favourable results |
| R1-Q28 | B | Trustworthiness: correct commitments openly (B§5) | A: keeps silent about a broken date |
| R1-Q29 | A | Clarify, then test a proposal on a small sample (B§9, B§5 cooperation) | B: rejects an idea because of opposition |
| R1-Q30 | C | Allocation by skill and workload, with review (B§5 cooperation) | B: equal numbers regardless of skill |

### Revision 2

| ID | Key | Deciding principle | Strongest distractor and failure |
|---|---|---|---|
| R2-Q01 | B | Urgency sets the first channel; writing follows for the record (B§2) | A: memorandum too slow for a danger tonight |
| R2-Q02 | D | Paraphrase and ask for the objection privately (B§3) | A: polite "yes, sir" taken as commitment |
| R2-Q03 | A | Specific, private, pre-issue correction (B§3, B§9 facts) | C: silence because of seniority |
| R2-Q04 | C | Selective perception: test the belief through paraphrase (B§4) | D: technological fix for a belief problem |
| R2-Q05 | D | Information overload: prioritise and structure (B§4) | B: marks everything urgent |
| R2-Q06 | B | Empathy with rules; verify the ground (B§5, B§9) | C: refusal without any hearing |
| R2-Q07 | A | Persuasion with the specific order and lawful phasing (B§5) | B: threat beyond the facts |
| R2-Q08 | C | Confidentiality is not absolute where safety is at risk (B§11, B§9) | A: keeps a possible hazard secret |
| R2-Q09 | B | Lawful alternative sets the walk-away point (A§4 BATNA and reservation point) | A: current price treated as the alternative |
| R2-Q10 | D | Integrative value creation within the criteria (A§4) | A: equal split, which is distributive |
| R2-Q11 | C | Mediation is unsuitable under threat; use the formal process (A§5) | A: joint meeting under intimidation |
| R2-Q12 | A | Measured fact, stated uncertainty, specific action (A§6) | B: certainty without data |
| R2-Q13 | D | Visible correction through the original channel (A§6, B§11) | A: silent reissue |
| R2-Q14 | B | Acquiescence: balanced wording and reverse check (A§7) | A: more pages of agreement items |
| R2-Q15 | C | Non-response bias: compare with non-respondents (A§7) | A: publish a self-selected 22 per cent as representative |
| R2-Q16 | A | Groupthink: independent views before a vote (A§7) | B: vote straight after the first proposal |
| R2-Q17 | B | Authority gradient: invite dissent and protect reporting (A§7) | C: inspection given to the dismissive senior |
| R2-Q18 | D | Confirmation bias: name disconfirming evidence and test it (A§7) | A: interviews only from those who agree |
| R2-Q19 | A | Accessible route for people without internet access (B§7) | B: rely on relatives to file |
| R2-Q20 | C | Stakeholder matrix: hear high-power and low-power groups in accessible ways (A§2) | B: single venue the households may not reach |
| R2-Q21 | B | Difficult-conversation sequence: observation, impact, perspective, requirement, agreed action and review (A§3) | C: judgement and warning before observation |
| R2-Q22 | D | Verify facts, preserve evidence, review motive separately (A§9) | A: delays a public-health result for a motive question |
| R2-Q23 | C | Cultural adaptation without excluding affected voices (B§4, B§5 adaptability) | D: avoids the elders on a stereotype |
| R2-Q24 | A | Assertive refusal: boundary, lawful alternative, request in writing (B§5) | B: complies and shares blame privately |
| R2-Q25 | D | Leading premise ("given how poorly") (B§8) | A/B/C: neutral factual or rating items |
| R2-Q26 | B | Sensitive topic, low literacy, need to probe: private trained interview (B§8) | A: headman mediates the answers |
| R2-Q27 | C | Protection first, then consultation and review (A§8) | A: delays protection for consultation |
| R2-Q28 | A | Confidentiality is not secrecy; public-safety record stays on the register (B§5, B§11) | B: hidden notebook keeps the failure off the register |
| R2-Q29 | D | Speak, agree task shifts, review with the team (B§5 cooperation, B§9) | C: daily written reporting after a bereavement |
| R2-Q30 | B | Privacy with the reason given to the person concerned (B§7) | A: reads the reason aloud in a public room |

### Revision 3

| ID | Key | Deciding principle | Strongest distractor and failure |
|---|---|---|---|
| R3-Q01 | D | Fact-finding before sanction; apply the procedure (B§6, B§9) | C: suspension before a finding |
| R3-Q02 | C | Psychological barrier: impatience deters questions (B§4) | D: a dismissive reply relabelled as a test |
| R3-Q03 | B | Neutral selection by published criteria (B§9 legality) | A: selection by size |
| R3-Q04 | A | Ambiguous term: fix the period and bands (B§8) | C: "a lot" leaves the term undefined |
| R3-Q05 | C | Rumour: verified facts, source and dated update (B§7) | A: repeats the rumour's claims |
| R3-Q06 | D | Leadership by outcomes, owners and check-ins (B§5, B§9; owner gap noted in COVERAGE) | C: daily status without outcomes |
| R3-Q07 | A | Listening: acknowledge, restate, clarify (B§3) | C: demands calm before any discussion |
| R3-Q08 | B | Keep to facts; lawful review route (B§9, A§8) | C: reverses a rule-based decision under threat |
| R3-Q09 | C | Feedback: named behaviour and effect, with a question (B§3) | B: praise with an unrelated criticism |
| R3-Q10 | A | Semantic barrier: plain words and comprehension check (B§4) | D: a signature recorded as understanding |
| R3-Q11 | D | Conflict: ground rules, separate accounts, interests (B§6) | A: rota imposed before facts |
| R3-Q12 | B | BATNA: lawful alternative as the walk-away point (A§4) | A: accepts the first demand |
| R3-Q13 | C | Confidentiality on a need-to-know basis (B§5, B§11) | A: reveals the complainant to the accused |
| R3-Q14 | A | Assertive refusal with a lawful alternative and written instruction (B§5) | C: loud accusation of corruption |
| R3-Q15 | D | Apology for conduct while the decision and appeal route stand (B§5 respect) | A: apologises for a rule-compliant decision |
| R3-Q16 | B | Accessibility: alternative format and checked understanding (B§4, B§11) | C: moves the same inaccessible text |
| R3-Q17 | C | Written acknowledgement with reference, timeline and contact (B§7) | A: a reply after ninety days |
| R3-Q18 | A | Test a belief against records that could disconfirm it (A§7) | C: two visits reported as an established cause |
| R3-Q19 | B | Non-verbal cues are contextual; clarify verbally (B§2, B§11) | A: hostility concluded from posture |
| R3-Q20 | D | Informal account is not an official decision; confirm first (B§2) | A: acts on the tea-stall report |
| R3-Q21 | C | Minimum necessary through a secure official channel (B§7) | A: full file through a messaging app |
| R3-Q22 | B | Consistent questions and probes across candidates (B§8 interview) | C: family questions (irrelevant) |
| R3-Q23 | A | Consensus is not legality; check the rule (B§11) | B: proceeds because all agree |
| R3-Q24 | D | Facts-based conversation before escalation (B§6, B§11) | A: escalates an ordinary dispute at once |
| R3-Q25 | A | Mediator's first step: ground rules and interests (A§5) | B: equal split before interests are known |
| R3-Q26 | C | Confirm an instruction that changes a file in writing (B§9 accountability) | A: verbal only |
| R3-Q27 | B | Inclusion of low-power affected groups (A§2) | A: consults only the best-organised group |
| R3-Q28 | D | Trustworthiness: keep the date or correct it openly (B§5) | A: silence about a late report |
| R3-Q29 | A | Statutory requirement cannot be bargained away (B§6, B§9 legality) | B: suspends it for half the period |
| R3-Q30 | C | Framing effect: neutral parallel wording (A§7) | A: positive frame chosen for persuasive effect |

## 4. Items revised in this pass

- **Length balance (options only; keys unchanged):** R1 Q03, Q06, Q07, Q09, Q10, Q11, Q14, Q15, Q17, Q18, Q19, Q21, Q24, Q26, Q27, Q29, Q30; R2 Q01, Q04, Q05, Q06, Q07, Q08, Q09, Q10, Q11, Q12, Q13, Q15, Q16, Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q26, Q27, Q28, Q29; R3 Q02, Q03, Q05, Q07, Q08, Q09, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q18, Q19, Q20, Q22, Q23, Q24, Q25, Q28, Q29, Q30.
- **Review fixes:** R2-Q21 correct option restored to include "agree an action and review" (owner's AGREED ACTION + REVIEW). R2-Q04 explanation corrected to remove a claim not in the stem.
- **Replaced for coverage gaps:** R3-Q04 (double-barrelled removed; ambiguous-term defect added, because double-barrelled is tested in R1-Q20) and R3-Q30 (tender clarification replaced by the framing-effect item, which had no standalone item).
- **Replaced option text for ratio outliers:** R3-Q24 B.
- **Answers:** all three `ANSWERS.md` files were rewritten so that each option has a labelled explanation, matched to the final option text.

## 5. Residual risk

- These keys are principle-based judgements, not computed results. They are self-checked and have not been reviewed by a second person. A reviewer could reasonably dispute a few keys. The most arguable are listed in the final report.
- Team-leadership items rely on general cooperation and scenario principles because the owner has no leadership section.
- No item was tested with learners, so difficulty is calibrated by design (close distinctions and two-step reasoning), not by observed difficulty.
