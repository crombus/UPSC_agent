# Accountability and Ethical Governance - MUST-DO

> **Subject:** Ethics | **Tier:** Must-Do (foundation) | **GS Paper:** GS-IV.
> **Core area:** Accountability in governance; accountability vs responsibility; the ethics-specific
> reading of India's accountability architecture (CVC, CBI, Lokpal/Lokayukta, CAG, judiciary).
> **Grounded in:** 2nd ARC, 4th Report *Ethics in Governance* (2007), Ch.4 Institutional Framework
> and the ARC's National Colloquium annexures (control-systems discussion); official UPSC GS-IV
> syllabus; audited GS-IV PYQs (2024-2025 Mains, accountability/leakages question).
> ✅ = source-grounded | ⚠️ = analytical inference | 📰 = current anchor.
> *Companion: `advanced/11_Accountability-and-Ethical-Governance.md`.*

---

## 1. Visual foundation

```text
RESPONSIBILITY                          ACCOUNTABILITY
(assigned duty or obligation —           (obligation to explain and justify
 "what must I do?")                       conduct to a forum that can judge,
                                          correct, remedy or sanction)
        |                                        |
        v                                        v
   discretion + role                    external/internal control system
   assignment                           (Nolan Principle 4: "submit to
                                          whatever scrutiny is appropriate")
                                                  |
                          +------------------------+------------------------+
                          v                        v                        v
                    INTERNAL CONTROL          EXTERNAL CONTROL          SOCIAL CONTROL
                    (CVC, CVO, CBI,           (CAG audit,               (RTI, media, civil
                     departmental              independent judiciary)    society, citizens'
                     vigilance)                                          charters)
```

**Core proposition:** ⚠️ Responsibility and accountability are related but distinct. Responsibility
is the assigned duty attached to a role. Accountability is an identifiable actor's obligation to
explain and justify conduct to a specific forum that can question, judge, require correction or
remedy, and attach consequences. It operates ex ante through standards, records and reporting and
ex post through review, correction and sanction.

## 2. Essential definitions

| Concept | Exam-ready meaning |
|---|---|
| ⚠️ **Responsibility** | The assigned duty or obligation attached to a role, existing independent of whether anyone later checks its performance. |
| ✅ **Accountability** (Nolan Principle 4, ARC 2.2.5) | Being "accountable for their decisions and actions to the public" and submitting "to whatever scrutiny is appropriate to their office"; analytically, it requires a named actor, forum, standard, explanation, judgment and possible correction, remedy or consequence. |
| ✅ **Internal/institutional control system** | Departmental vigilance and CVOs are internal administrative controls; the CBI investigates specified offences; the statutory CVC performs vigilance, advisory and superintendence functions but is not itself a prosecuting body. Their powers and locations are not identical (see `20`). |
| ✅ **External control system** | The Comptroller and Auditor General (CAG) and the independent judiciary — mechanisms *outside* executive control (ARC Colloquium Annexure-I(2)). |
| ✅ **Social control** | Civil society, media and citizen vigilance acting as an accountability check where formal mechanisms are weak (ARC Colloquium Annexure-I(2), citing Hong Kong's ICAC public-education model). |

## 2A. Accountability under AI assistance: the six-element test applied to non-human agents

> ⚠️ **Routing note.** 2026 GS-IV Q1(a) (a university professor generates a Ph.D. evaluation report
> using Artificial Intelligence and submits it with some modifications — "discuss this from the
> perspective of accountability and integrity") is **primarily owned by**
> `13_Emerging-Ethics-Technology-AI-and-Environment.md`, which carries the AI-governance substance.
> **This file owns the accountability grammar** the answer must be built on, and the section below
> is written to be independently answer-sufficient for the accountability half of any such question.
> The syllabus-level demand is general: *what happens to accountability when a decision-support tool
> is inserted between an office-holder and a judgment the office-holder is obliged to make?*

### The six-element test applied to a machine

Section 2 defines accountability analytically as requiring **a named actor, a forum, a standard, an
explanation, a judgment and a possible correction, remedy or consequence**. That definition is the
decisive analytical instrument here, because a generative model fails every element:

| Element of accountability | What it requires | Can an AI system supply it? |
|---|---|---|
| **Named actor** | An identifiable person or body whose conduct is at issue | ❌ No. A model is not a legal or moral person; it holds no office and bears no duty. |
| **Forum** | A body entitled to summon and question the actor | ❌ No. A model cannot be summoned, cross-examined or held to an oath. |
| **Standard** | A prior norm against which conduct is measured | ⚠️ Partly. A model can be *evaluated* against a standard, but it cannot *undertake* to meet one. |
| **Explanation** | Reasons that actually caused the decision | ❌ No. Output fluency is not reason-giving; a plausible-sounding rationale may be post-hoc and unconnected to the actual computation. |
| **Judgment** | The forum's verdict on the actor's conduct | ❌ No. Judgment can attach only to the human who deployed and adopted the output. |
| **Correction / consequence** | Remedy, sanction, restoration, learning | ❌ No. A model cannot be sanctioned, cannot compensate, and cannot be disqualified from office. |

⚠️ **Analytical conclusion:** accountability cannot be transferred to a tool. It can only be
**retained, diffused or concealed**. Inserting an AI between the office-holder and the judgment does
not create a second accountable party; it creates the *appearance* of one.

### Delegable task vs non-delegable duty

- ⚠️ **Delegable task:** a step whose quality can be independently verified by the office-holder
  before adoption — language editing, formatting, reference-checking, translation, summarising a
  document the officer has also read, first-pass similarity screening.
- ⚠️ **Non-delegable duty:** a duty whose whole content *is* the exercise of personal judgment by a
  designated office-holder — the evaluative assessment of a thesis, a disciplinary finding, a
  sanctioning order, a bail or clearance recommendation, a performance appraisal. Here the person's
  own reasoning is not a means to the output; it **is** the output the office was created to supply.
- ⚠️ **The test:** *if the tool's output were removed, would there be anything left that the
  office-holder was appointed to contribute?* If no, the duty was non-delegable and has been
  abandoned, regardless of how the result reads.
- ⚠️ **"With some modifications" does not cure the defect.** Editing an output one did not generate
  converts the office-holder into a reviewer of the machine; but the office required an *originator*
  of judgment. Superficial modification also produces **automation bias** — the human anchors on the
  machine's framing and the "check" becomes ratification rather than independent assessment.

### Named failure modes

1. ⚠️ **Responsibility gap / accountability diffusion:** harm occurs, but no actor both (i) made the
   decision and (ii) can be held to answer for it — the developer points to the deployer, the
   deployer to the model, the model to no one.
2. ⚠️ **"Problem of many hands":** where a decision passes through designers, procurers, deployers
   and adopters, each contribution looks too small to ground blame while the aggregate harm is real.
3. ⚠️ **Moral crumple zone:** the least powerful human in the loop (a junior assistant, a data-entry
   clerk) absorbs blame for a failure structurally produced by the automated system and by the
   senior officer who adopted it.
4. ⚠️ **Misrepresentation / integrity failure (distinct from the efficiency question):** submitting
   machine-generated assessment as one's own scholarly or official judgment is a false implicit
   claim about authorship of reasoning. This is a breach of **integrity**, not of productivity — and
   it survives even if the output happens to be substantively correct.
5. ⚠️ **Unexplainable explanation:** the office-holder cannot answer the forum's central question —
   *"why did you conclude this?"* — because the reasons were never theirs.

### Permissibility matrix for AI assistance in a duty-bearing role

| Use of AI | Permissible? | Governing test |
|---|---|---|
| Language polishing, formatting, reference-checking of the office-holder's **own** assessment | ⚠️ Yes, with disclosure where a disclosure norm exists | Judgment remains human; output is verifiable line by line |
| Similarity/plagiarism screening or evidence retrieval, flagged to the institution, human decides | ⚠️ Yes | Transparency plus a human final call; the tool informs, does not conclude |
| Summarising a long record the office-holder has also read, as a drafting aid | ⚠️ Yes, with verification against the primary record | Verifiability; errors are detectable by the adopter |
| AI drafts the **substantive evaluation**; the human "modifies" and signs | ❌ No | Non-delegable judgment delegated; explanation cannot be given; submission misrepresents authorship |
| AI output adopted for a decision affecting rights, with no disclosure and no human reasoning on record | ❌ No | Fails named-actor, explanation and correction elements simultaneously |

### Objections and replies

- **Objection 1 — "Scarcity of time is a real institutional problem; purism ignores workload."**
  ⚠️ Reply: the pressure is genuine and the institutional answer is workload reform — examiner-load
  caps, realistic deadlines, honoraria, the right to decline or return an assignment. None of these
  is served by a silent private workaround, which *conceals* the capacity deficit and therefore
  guarantees it will not be fixed. Declining the assignment is the honest response to overload;
  fabricating capacity is not.
- **Objection 2 — "The output was checked, so accountability is intact."**
  ⚠️ Reply: accountability requires the ability to give *the reasons that actually operated*. A check
  establishes absence of detected error; it does not establish authorship of judgment, and under
  automation bias the check is systematically weaker than independent assessment.
- **Objection 3 — "If the conclusion is correct, the process is a formality."**
  ⚠️ Reply: in evaluative offices the process *is* the product. A candidate is entitled to the
  considered judgment of a qualified examiner, not to a correct-looking verdict; and a verdict whose
  reasons cannot be defended before a forum cannot be corrected on appeal.
- **Objection 4 — "Tools have always assisted; this is only a new tool."**
  ⚠️ Reply: the distinction is not novelty but **substitutability of judgment**. A calculator
  executes a step the user has specified and can verify; a generative model supplies the very
  conclusion and its apparent justification, which is the office-holder's own assigned contribution.

### Institutional response (what an institution must put in place)

1. ⚠️ A **published AI-use policy** naming permitted, restricted and prohibited uses for each
   category of duty, so that the line is institutional rather than left to private conscience.
2. ⚠️ A **mandatory disclosure statement** attached to evaluative and decisional outputs, declaring
   any AI assistance and its scope.
3. ⚠️ A **reasoned-record requirement**: the office-holder must record reasons in their own
   analysis, capable of being defended before the relevant forum.
4. ⚠️ **Capacity reform** — assignment caps, realistic timelines and an explicit, penalty-free right
   to decline — so that the honest route is also the feasible route.
5. ⚠️ **Audit and sampling** of evaluative outputs, plus a grievance route for the affected party,
   closing the correction/remedy element.
6. ⚠️ **Training** on automation bias and on the delegable-task/non-delegable-duty distinction.

### Sources and caveats

- ✅ **ICMJE Recommendations, "Defining the Role of Authors and Contributors," §4 (Use of Artificial
  Intelligence Technology):** authors "should not list AI and AI-assisted technologies as an author
  or co-author, nor cite AI as an author," and must "carefully review and edit the result because AI
  can generate authoritative-sounding output that can be incorrect, incomplete, or biased." The four
  ICMJE authorship criteria — substantial contribution; drafting or critical revision; final
  approval; and **agreement to be accountable for all aspects of the work** — supply a clean
  four-point test, and the fourth criterion is exactly the element a machine cannot satisfy.
  ⚠️ ICMJE governs biomedical publishing; its use for a thesis evaluation is an argument by
  analogy, and should be presented as such.
- ✅ **UNESCO, *Guidance for Generative AI in Education and Research* (2023):** human accountability
  may not be ceded to the tool; AI use should be disclosed; institutions should publish permitted
  and prohibited uses.
- ⚠️ **UGC (Promotion of Academic Integrity and Prevention of Plagiarism in Higher Educational
  Institutions) Regulations, 2018:** establish a mandatory institutional mechanism — a Departmental
  Academic Integrity Panel (DAIP) and an Institutional Academic Integrity Panel (IAIP) — with graded
  consequences rising with the similarity level. ⚠️ **Two cautions:** (i) quote the tiered similarity
  percentages only after checking the gazette text, since the slab boundaries are frequently
  misstated in secondary sources; (ii) the 2018 Regulations address **plagiarism/similarity**, and do
  not of themselves define *undisclosed generative-AI use* as an offence — that is presently handled
  through institutional policy, not a settled national numerical threshold.
- ❓ **"UGC AI rules"** circulating in coaching material: no binding national UGC instrument on
  generative-AI use has been verified in this repository. ❌ Do not assert one.
- ✅ Accountability and human-oversight principles in the **MeitY India AI Governance Guidelines**,
  the **UNESCO Recommendation on the Ethics of AI (2021)** and the **OECD AI Principles** are held in
  `13_Emerging-Ethics-Technology-AI-and-Environment.md`; cite from there rather than restating here.

### 10-mark answer spine (~150 words)

1. **Define the distinction in one line:** responsibility is the duty attached to the role;
   accountability is the obligation to explain and justify that conduct to a forum that can judge
   and correct it (Section 2).
2. **Name two distinct wrongs, not one:** (i) delegation of a **non-delegable evaluative judgment**;
   (ii) **misrepresentation** of machine output as one's own assessment — an integrity breach that
   stands independently of output quality.
3. **Apply the six-element test:** the model supplies no actor, forum, explanation or correctable
   consequence; accountability was not transferred but diffused.
4. **Anchor:** ICMJE's "accountable for all aspects of the work"; UNESCO 2023 on non-cession of human
   accountability; the institution's own academic-integrity machinery.
5. **Concede the real pressure:** workload and time scarcity are genuine; the honest responses are
   declining, seeking an extension, or institutional load reform.
6. **Remedy:** published AI-use policy, mandatory disclosure, reasons in the officer's own hand,
   audit and grievance route.
7. **Verdict (one line):** AI may assist in *drafting* reasons; it cannot hold the *duty to reason*.

### Traps

- ❌ **Trap:** treating this as a bias/algorithmic-fairness question. -> The wrong here is not model
  bias; it is abandonment of a fiduciary judgment plus misrepresentation. Bias is a different
  failure mode (owned by `13`).
- ❌ **Trap:** "he modified it, so he owns it." -> Modification of an output one did not generate is
  review, not judgment; the office required judgment.
- ❌ **Trap:** blanket technophobia ("ban AI in academia"). -> The defensible line is
  use-specific: verifiable assistance yes, substitution of the assigned judgment no.
- ❌ **Trap:** collapsing accountability into punishment. -> Accountability is answerability with
  possible correction; a system with sanctions but no reason-giving or remedy is still unaccountable.

## 3. Mechanism: how ethical accountability actually operates

1. **Assign responsibility clearly** — accountability is meaningless if it is unclear who was
   responsible for a decision (diffused responsibility undermines both).
2. **Route accountability through differentiated institutions:** departmental vigilance/CVOs for
   internal administrative control; CVC supervision/advice and CBI investigation within their
   statutory remits; **external control** (CAG, legislature and judiciary) for financial, political
   and legal scrutiny; and **social control** (RTI, media, civil society and social audit) for
   citizen-based answerability.
3. ✅ ARC's own Colloquium annexure diagnosis: internal control in India has historically been weak
   because of collusion, lack of independence of investigating agencies from the executive, and
   procedural delay; external control (CAG, judiciary) is independent but time-lagged; social
   control depends on civil-society capacity and information access (RTI).
4. ⚠️ 2025 GS-IV Q6(b) is primarily owned by Topic `18` because its subject is utilisation of
   public funds. Topic `11` is a shared accountability-mechanism cross-link: clear responsibility,
   traceable transactions, audit, disclosure, grievance remedy and enforceable follow-up.
5. ⚠️ Effective ethical governance requires **all three control layers reinforcing each other** —
   internal vigilance catching misconduct early, external audit verifying propriety after the fact,
   and social control (RTI, citizens' charters) sustaining pressure between audit cycles.

## 4. Indian applications and examples

- ⚠️ A Direct Benefit Transfer or expenditure dashboard can improve traceability and timely
  exception detection only where data access, data quality, review responsibility and escalation
  are specified. Visibility becomes accountability when an authorised forum can investigate,
  correct, remedy and sanction.
- ✅ CAG's independent audit and legislative scrutiny remain indispensable for propriety,
  performance and systemic correction. Concurrent/internal audit, transaction controls and
  dashboards add in-course detection and correction; they do not replace constitutional audit.
- ⚠️ A Lokayukta/Lokpal-style institution strengthens accountability specifically for high-level
  functionaries otherwise insulated from routine departmental vigilance (see `20`).

### Social audit: from disclosure to remedy

- ⚠️ A credible social audit separates verification from the implementing agency, proactively
  discloses muster rolls, estimates, bills and asset records, verifies them with workers and at the
  worksite, and places findings before a public hearing or Gram Sabha.
- ⚠️ The cycle is incomplete without a time-bound action-taken report, recovery or disciplinary
  referral where supported, grievance remedy for affected workers and protection against
  intimidation or capture. Social audit is therefore more than publication of data.

### Political and bureaucratic accountability

- ⚠️ Political accountability makes ministers answerable to the legislature and electorate for
  policy and departmental outcomes. Bureaucratic accountability makes officials answerable for
  lawful, impartial and competent execution through hierarchy, files, audit, vigilance,
  legislative committees and courts.
- ⚠️ Political direction cannot require illegality; bureaucratic neutrality does not permit
  obstruction of a lawful democratic mandate or evasion of reasoned implementation.

### E-governance with ethical safeguards

- ⚠️ E-governance can reduce delay, discretion and record tampering, but may also create exclusion,
  language/disability barriers, authentication errors, privacy risks, opaque automated decisions,
  vendor dependence and poor-quality data. Assisted/offline access, human review, speaking reasons,
  audit logs and appeal are ethical design requirements.

### MGNREGA accountability restoration

- ⚠️ A district administrator confronting ghost beneficiaries or unverifiable work should reconcile
  demand registers, job cards, muster rolls, attendance, wage payments, technical sanctions and
  physical assets; hold an independent social-audit hearing; protect complainants; initiate
  recovery/disciplinary or criminal referral where evidence warrants; and restore timely wages and
  grievance closure. The 2025 case facts are an exam hypothetical, not proof of programme-wide
  conditions.

## 5. Must-Know Facts for Prelims

- ✅ ARC's Colloquium annexure classifies control systems into internal (CVC/CVO/CBI), external
  (CAG/judiciary) and social (civil society/media/RTI).
- ✅ The Fifth Pay Commission recommended that audit "should try to be as concurrent as possible" to
  reduce the time-lag between an act of corruption and its exposure.
- ✅ The Central Vigilance Commission was set up by executive resolution in **1964** on the Santhanam
  Committee's recommendation and given statutory status by the Central Vigilance Commission Act,
  2003 (assent 11 September 2003), following *Vineet Narain v. Union of India*, (1998) 1 SCC 226,
  decided on **18 December 1997**.
- ⚠️ Accountability requires answerability to a forum capable of judgment and follow-up; it is
  conceptually distinct from responsibility, the assigned duty itself.

## 6. UPSC traps

- ❌ Accountability and responsibility mean the same thing. -> Responsibility assigns the duty;
  accountability requires explanation and justification to a forum capable of review, correction,
  remedy or consequence.
- ❌ CAG audit alone is sufficient to ensure ethical use of public funds. -> The ARC's own diagnosis
  notes CAG audit is typically time-lagged, often reviewing transactions years after the fact,
  limiting its deterrent value unless made more concurrent.
- ❌ Strengthening internal vigilance automatically substitutes for external/social control. -> Each
  control layer catches different failure modes (collusion is best exposed externally/socially;
  administrative lapses are best caught internally) — they are complementary, not substitutable.

## 7. PYQ application

- ⚠️ 2025 GS-IV Q6(b): India's economic rise despite fund underutilisation/misuse is primarily a
  Topic `18` public-fund question and a shared Topic `11` cross-link for accountability mechanisms.
- ⚠️ Any question on "ensuring good governance" or "reducing corruption through institutions" should
  invoke the internal-external-social control triad explicitly.

## 8. Mains angles

- ⚠️ Structure accountability answers as: define accountability precisely (distinct from
  responsibility) -> map the specific control layer(s) relevant to the question's scenario -> note
  the layer's known limitation (time-lag, capture, capacity) -> propose a specific strengthening
  measure (concurrent audit, real-time dashboards, protected disclosure, citizen social audit).

> **Answer thesis:** Ethical governance requires clearly assigned responsibility backed by
> accountability across all three control layers — internal vigilance, external audit/judiciary,
> and social control — since each catches different failure modes and no single layer suffices alone.

## 9. Probable questions

- ⚠️ **Prelims:** Classify the CVC, CAG and RTI Act under the correct control-system category
  (internal/external/social).
- ⚠️ **Mains (10 marks):** Distinguish accountability from responsibility with an Indian
  administrative example.
- ⚠️ **Mains (15 marks):** Suggest specific measures to strengthen accountability and reduce
  leakages in the utilisation of public funds in India's fast-growing economy.

## 10. Social capital as the informal complement to formal accountability (historical demand)

> ⚠️ 2023 GS-IV Q6(b) (historical demand, routed at the 06/11 boundary): social capital and its role
> in good governance. **Full concept, definition and Indian-moral-thought antecedents (Putnam's
> bonding/bridging distinction, Guru Nanak's Vand Chhako, Basava's Dasoha) are taught in
> `06_Indian-Moral-Thinkers-and-Philosophers.md`, Section 11 — this file's own contribution is the
> accountability-architecture placement.**

- ⚠️ Social capital operates as an informal fourth input into the accountability triad (Section 1):
  it lowers the cost of **social control** specifically — citizens who trust each other and local
  institutions are more willing to participate in social audits, report leakages (see `18`), and
  hold local functionaries answerable *between* formal audit cycles.
- ⚠️ **Worked mechanism:** MKSS-style social audits function only where a baseline of bridging
  social capital exists (villagers trusting the audit process and each other's testimony against a
  powerful local functionary); where social capital is low or purely bonding (caste/faction-based),
  social audits are more easily captured or intimidated into silence.
- ⚠️ **Limitation as an accountability substitute:** social capital cannot replace internal
  (CVC/CVO) or external (CAG/judiciary) control — it strengthens the *social* leg of the triad only,
  and a society rich in bonding but poor in bridging social capital can even *weaken* accountability
  by reinforcing in-group shielding of misconduct.

## 11. Executable directive decoding and answer architecture

| Directive word | What is tested | Structural move |
|---|---|---|
| **Suggest** | A specific, implementable measure | Diagnose which control layer is weak -> name its specific limitation -> propose one concrete measure -> note the measure's own limitation |
| **Distinguish** | Two related concepts kept precisely apart | Define both -> point-by-point contrast -> one Indian example each |
| **Explain the role of X in good governance** | Mechanism, not a definitional restatement | Define X -> the specific mechanism by which it strengthens governance -> one Indian example -> one limitation |

**10-mark architecture (~150 words):** define accountability/responsibility or the named concept
precisely -> map it to the relevant control layer -> one Indian example -> one limitation -> one
concrete strengthening measure -> one-line conclusion.

**Counterpoint and reasoned verdict (template):** "[Named control layer/mechanism] addresses [X
failure mode], but its limitation is [Y]; strengthening it requires pairing it with [named
complementary layer/measure], since no single layer is self-sufficient."

## 12. Study links

- ✅ Advanced companion: `advanced/11_Accountability-and-Ethical-Governance.md`.
- ✅ `20_Anti-Corruption-Institutions.md` — CVC/CBI/Lokpal ethics-specific jurisdiction treatment.
- ✅ `18_Utilization-of-Public-Funds-and-Challenges-of-Corruption.md` — leakage/misuse mechanics.
- ✅ `Polity/advanced/32_CAG.md` and `Polity/advanced/37_CVC-and-CBI.md` — constitutional-body detail.
- ✅ `06_Indian-Moral-Thinkers-and-Philosophers.md` — social capital's full concept and antecedents.
- ✅ `13_Emerging-Ethics-Technology-AI-and-Environment.md` — primary owner of AI-governance substance
  (bias, opacity, human oversight, MeitY/UNESCO/OECD anchors) that Section 2A cross-links to.

<!-- 2026 POINTER (non-generated; kept outside the generated PYQ blocks above/below) -->
## 2026 GS-IV Section-A pointer

> ⚠️ The generated PYQ blocks below end at 2024-2025. The **2026 GS-IV Section-A** routing ledger for
> all thirteen official parts is maintained separately in
> [`../_PYQ-GS4-SectionA-2026.md`](../_PYQ-GS4-SectionA-2026.md).
>
> **Parts touching this owner:** **2026 Q1(a)** (AI-generated Ph.D. evaluation report — accountability
> and integrity) as a **cross-link**; the primary owner is
> `13_Emerging-Ethics-Technology-AI-and-Environment.md`. The accountability grammar this owner must
> now support is in **Section 2A** above.

<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->
## Recent PYQ Integration (2024-2025)

> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md`.

- **Years represented:** 2025
- **Paper(s):** GS-IV
- **Routed question demands:** 1

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---|---|---|---|---|
| 2025 | GS-IV | 11 | Case study: restoring proper functioning of the MGNREGA programme | Section B case study · 20 marks · 250 words | Routed to owning topic | Apply stakeholders, dilemmas, options, justification, implementation and safeguards. |

### What this owner must now support

- Case study: restoring proper functioning of the MGNREGA programme

> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective question into a solved answer.
<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->

<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->
## Historical PYQ Integration (2018-2023)

> **Status:** Question-level PYQ demand is integrated into this owner.
> **Provenance:** Audited local official-paper routing ledgers: `_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md`.

- **Years represented:** 2019, 2021, 2022, 2023
- **Paper(s):** GS-IV
- **Routed question demands:** 5

| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format | Source status | Owner requirement |
|---:|---|---:|---|---|---|---|
| 2019 | GS-IV | 10 | Rising politicization of bureaucracy - political executive encroaching on permanent executive including transfers and postings; consequences of this trend | Discuss · 20 marks · 250 words | Case routed to Ethics case-study method | Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion. |
| 2021 | GS-IV | 6 | (a) independent social audit mechanism as absolute must for public service accountability and ethical conduct; (b) integrity as a value that empowers the human being | Elaborate / Justify · 10 + 10 marks · 150 words each | Routed to owning Ethics topic | Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion. |
| 2021 | GS-IV | 9 | project manager of elevated corridor notices crack in pier; minister and chief engineer pressure to overlook - (a) options; (b) ethical dilemmas; (c) professional challenges; (d) consequences | Case study · 20 marks · 250 words | Case routed to Ethics case-study method | Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion. |
| 2022 | GS-IV | 4 | (a) good governance and e-governance initiatives for beneficiaries; (b) ethical issues in online methodology affecting vulnerable sections of society | Discuss · 10 + 10 marks · 150 words each | Routed to owning Ethics topic | Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion. |
| 2023 | GS-IV | 6 | (a) major teachings of Guru Nanak and their contemporary relevance; (b) social capital and its role in good governance | Explain · 10 + 10 marks · 150 words each | Routed to owning Ethics topic | Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion. |

### What this owner must now support

- Rising politicization of bureaucracy - political executive encroaching on permanent executive including transfers and postings; consequences of this trend
- (a) independent social audit mechanism as absolute must for public service accountability and ethical conduct; (b) integrity as a value that empowers the human being
- project manager of elevated corridor notices crack in pier; minister and chief engineer pressure to overlook - (a) options; (b) ethical dilemmas; (c) professional challenges; (d) consequences
- (a) good governance and e-governance initiatives for beneficiaries; (b) ethical issues in online methodology affecting vulnerable sections of society
- (a) major teachings of Guru Nanak and their contemporary relevance; (b) social capital and its role in good governance

> The table integrates the examinable demand and paper metadata. It does not turn an unkeyed objective question into a solved answer, and it does not claim that lexical presence alone proves full conceptual sufficiency.
<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->
