"""Learner-v2 source data: Ethics Topic 14, Probity and its philosophical basis."""


SESSION_TITLES = (
    "Probity in the UPSC syllabus and the public-office setting",
    "Honesty, integrity, propriety, accountability and their overlap",
    "How entrusted public power turns character into a governance question",
    "Indian applications: disclosure, reasons, audit and conflict control",
    "Prelims facts, legal distinctions and close-option traps",
    "PYQ routes, answer theses and cross-topic boundaries",
    "Probable questions and exam entry points",
    "Philosophical foundations: duty, virtue, trusteeship and constitutional morality",
    "Procedural and substantive probity under risk-graded scrutiny",
    "Current procurement anchor, advanced limits and final synthesis",
)


SESSION_GROUPS = (
    ("1",),
    ("2",),
    ("3",),
    ("4",),
    ("5",),
    ("6",),
    ("7",),
    ("8",),
    ("9",),
    ("10",),
)


def _mcq(label, statement, scenario_a, scenario_b, group):
    return {
        "label": label,
        "statement": statement,
        "scenario_a": scenario_a,
        "scenario_b": scenario_b,
        "group": group,
    }


MCQ_ITEMS = (
    _mcq(
        "The syllabus clause is about governance and public office",
        (
            "The UPSC clause joins the philosophical basis of governance with probity in governance, "
            "so the controlling setting is entrusted public office and the institutions that make public "
            "power upright, impartial, public-purpose and reviewable."
        ),
        (
            "A candidate writes only about private friendship and personal manners when asked about "
            "probity in governance. Which scope correction is required?"
        ),
        (
            "An officer exercises statutory licensing power affecting citizens and public resources. "
            "Which syllabus setting makes her conduct a probity question?"
        ),
        "concept and public-office scope",
    ),
    _mcq(
        "Probity is upright public-purpose conduct capable of justification",
        (
            "A working definition of probity is upright, impartial and public-purpose conduct in entrusted "
            "public office, supported by reasons and records that make the exercise of power capable of "
            "public justification and appropriate verification."
        ),
        (
            "A district officer records objective reasons for a discretionary allotment and permits review. "
            "Which working definition best captures the standard displayed?"
        ),
        (
            "An official claims that good intentions alone establish probity although no decision trail exists. "
            "Which definition reveals the missing public dimension?"
        ),
        "concept and public-office scope",
    ),
    _mcq(
        "Honesty tests truthfulness and non-deception",
        (
            "Honesty concerns truthfulness, non-deception and candid disclosure, including disclosure of a "
            "relevant private interest; it overlaps with integrity and probity but should not be described "
            "as a subset in a rigid hierarchy."
        ),
        (
            "A licensing officer truthfully declares that her spouse owns shares in an applicant company. "
            "Which ethical quality is directly demonstrated by the declaration?"
        ),
        (
            "A training note says honesty is merely a subset of integrity and has no independent question. "
            "Which non-hierarchical distinction corrects it?"
        ),
        "concept and public-office scope",
    ),
    _mcq(
        "Integrity is broader than the bounded Nolan formulation",
        (
            "Integrity ordinarily means consistent adherence to ethical principle and resistance to improper "
            "influence; the Nolan wording reproduced by the ARC specifically stresses freedom from outside "
            "obligations influencing official duty and does not exhaust the concept."
        ),
        (
            "An official refuses a benefactor's request because gratitude must not influence a statutory decision. "
            "Which Nolan-linked aspect of integrity is most directly involved?"
        ),
        (
            "A note treats the Nolan outside-obligations sentence as the complete universal definition of integrity. "
            "Which bounded-reading caution applies?"
        ),
        "concept and public-office scope",
    ),
    _mcq(
        "Propriety asks whether lawful conduct is appropriate",
        (
            "Propriety asks whether conduct is appropriate, fair and compatible with the purpose of entrusted "
            "power, including cases where an act may be technically lawful yet create favouritism, extravagance "
            "or misuse of institutional position."
        ),
        (
            "A minister lawfully uses a broad hospitality allowance for a bidder's luxury event during evaluation. "
            "Which ethical test remains even before illegality is proved?"
        ),
        (
            "An authority asks only whether expenditure was formally authorised, not whether it served the entrusted "
            "public purpose. Which governance concept has been omitted?"
        ),
        "overlap and entrusted power",
    ),
    _mcq(
        "Accountability requires answerability plus correction",
        (
            "Accountability means answerability to a competent forum able to examine reasons and evidence and "
            "secure correction, remedy or consequence; publication alone increases transparency but does not "
            "complete the accountability relationship."
        ),
        (
            "A department uploads expenditure data but provides no hearing, audit response or corrective authority. "
            "Which element beyond transparency remains absent?"
        ),
        (
            "A review body can inspect reasons, order correction and refer supported misconduct for action. "
            "Which concept is institutionalised?"
        ),
        "overlap and entrusted power",
    ),
    _mcq(
        "Probity concepts overlap without a strict hierarchy",
        (
            "Honesty, integrity, propriety, transparency, accountability and probity overlap and support one another, "
            "but they ask different functional questions; a sound answer compares their tests instead of arranging "
            "them as rigid nested sets."
        ),
        (
            "An officer is truthful about a conflict yet refuses to recuse and leaves the decision unreviewable. "
            "Which overlap analysis explains why honesty alone is insufficient?"
        ),
        (
            "A candidate draws honesty inside integrity inside probity as universally settled doctrine. "
            "Which conceptual correction should replace the diagram?"
        ),
        "overlap and entrusted power",
    ),
    _mcq(
        "Entrusted power must be used for citizens and public purpose",
        (
            "Public authority, discretion, information and money are entrusted powers rather than personal property; "
            "probity therefore forbids extraction of private advantage and demands use directed to the authorised "
            "public purpose."
        ),
        (
            "A regulator shares confidential applicant data with a relative to create a commercial opportunity. "
            "Which entrusted-power principle is violated?"
        ),
        (
            "A civil servant treats a discretionary quota as a personal favour bank. Which view of public office "
            "most precisely exposes the error?"
        ),
        "overlap and entrusted power",
    ),
    _mcq(
        "Public office as trust is an ethical analogy with a legal boundary",
        (
            "Public-office-as-trust is an ethical fiduciary analogy: officials hold authority for citizens and public "
            "purpose. The settled Indian environmental public-trust doctrine concerns State trusteeship of certain "
            "natural resources and does not directly govern every public-office decision."
        ),
        (
            "An essay uses trusteeship to explain why office cannot be converted into personal entitlement. "
            "Which qualification prevents doctrinal overclaiming?"
        ),
        (
            "A candidate asserts that M.C. Mehta v. Kamal Nath directly supplies the legal rule for every transfer "
            "and tax decision. Which boundary has been crossed?"
        ),
        "philosophical foundations",
    ),
    _mcq(
        "Deontology grounds probity in duty independent of detection",
        (
            "A deontological basis treats truthful, impartial and non-corrupt exercise of public power as a duty "
            "owed to persons and constitutional office, not merely as conduct justified when it produces convenient "
            "results or avoids detection."
        ),
        (
            "An officer refuses to manipulate a record even though concealment would save the department embarrassment. "
            "Which philosophical basis controls the refusal?"
        ),
        (
            "A procurement official asks only whether bid-rigging will be discovered or improve price. Which duty-based "
            "question is missing?"
        ),
        "philosophical foundations",
    ),
    _mcq(
        "Virtue ethics adds habituation and practical wisdom",
        (
            "Virtue ethics understands probity as a stable public character cultivated through practice, while "
            "phronesis supplies practical wisdom to apply honesty, fairness and public purpose sensitively rather "
            "than through mechanical rule worship."
        ),
        (
            "An experienced officer identifies the fair lawful course in an unusual relief case without abandoning "
            "reasons or review. Which virtue-ethics idea explains the judgment?"
        ),
        (
            "A trainee knows every conduct rule but changes principles whenever supervision disappears. "
            "Which character-based account reveals the deficit?"
        ),
        "philosophical foundations",
    ),
    _mcq(
        "Gandhian trusteeship joins means, ends and stewardship",
        (
            "Gandhian trusteeship treats possession and power as stewardship for social welfare, while the unity of "
            "means and ends rejects corrupt methods for desirable outcomes; applied to governance, both ideas support "
            "public-purpose administration without converting analogy into positive law."
        ),
        (
            "An officer takes an illegal donation to fund a genuinely useful clinic. Which Gandhian means-ends "
            "principle rejects the defence?"
        ),
        (
            "A public corporation treats surplus and authority as resources to be responsibly administered for "
            "society. Which Gandhian philosophical link is being used?"
        ),
        "philosophical foundations",
    ),
    _mcq(
        "Constitutional morality restrains power through constitutional values",
        (
            "Constitutional morality requires fidelity to constitutional values, procedures and restraints rather "
            "than personal preference or temporary majority pressure; civil education, institutional practice, "
            "reasoned decisions and lawful review help sustain it."
        ),
        (
            "A popular majority demands exclusion of a minority from a public hearing, but the officer protects equal "
            "participation. Which moral framework guides the decision?"
        ),
        (
            "A public servant invokes personal ideology while ignoring equality, due process and institutional competence. "
            "Which standard corrects this misuse of moral language?"
        ),
        "procedure and public purpose",
    ),
    _mcq(
        "Procedural probity makes decisions traceable and fair",
        (
            "Procedural probity asks whether authority, notice, equal information, objective criteria, recorded reasons, "
            "conflict controls, audit trails and review were properly built into the decision-making process."
        ),
        (
            "Every bidder receives identical information, evaluators declare interests and scoring reasons are preserved. "
            "Which dimension of probity is most directly demonstrated?"
        ),
        (
            "A beneficiary receives a useful outcome through secret criteria and an undocumented oral order. "
            "Which dimension remains deficient despite the benefit?"
        ),
        "procedure and public purpose",
    ),
    _mcq(
        "Substantive probity tests the authorised public purpose",
        (
            "Substantive probity asks whether the decision and its real effects serve the authorised public purpose, "
            "respect equal citizenship and avoid disguised private capture; impeccable paperwork cannot legitimise "
            "an outcome engineered for a narrow interest."
        ),
        (
            "A tender follows every form but its specifications were designed to favour one connected vendor without "
            "public need. Which probity test exposes the defect?"
        ),
        (
            "An emergency action saves lives but initially misses a minor formality that is promptly cured. "
            "Which dimension explains why purpose matters alongside procedure?"
        ),
        "procedure and public purpose",
    ),
    _mcq(
        "Transparency needs written reasons and a usable record",
        (
            "Transparency supports probity when material criteria, interests, reasons and records are accessible to "
            "appropriate scrutiny; written reasons discipline discretion, enable audit and appeal, and must still "
            "respect lawful privacy and confidentiality."
        ),
        (
            "A licensing authority announces the result but conceals the criteria and gives no reasons. Which "
            "probity-enabling transparency feature is missing?"
        ),
        (
            "A file records the evidence, alternatives and reasons while redacting protected personal data. "
            "Which balanced transparency design is illustrated?"
        ),
        "procedure and public purpose",
    ),
    _mcq(
        "Material conflicts normally require disclosure and recusal",
        (
            "A material conflict of interest requires timely disclosure and, where impartiality or its appearance "
            "would reasonably be compromised, recusal or independent reassignment; private assurances of fairness "
            "are not an adequate institutional safeguard."
        ),
        (
            "A procurement chair's sibling submits a bid and the chair promises privately to remain neutral. "
            "Which safeguard should ordinarily follow disclosure?"
        ),
        (
            "An official has a remote immaterial acquaintance with an applicant. Which principle calls for a "
            "proportionate conflict assessment rather than automatic paralysis?"
        ),
        "institutional safeguards",
    ),
    _mcq(
        "Codes of ethics and conduct perform different functions",
        (
            "A code of ethics states public-service values and decision principles, whereas a code of conduct "
            "specifies expected or prohibited behaviour, procedures and consequences; credible implementation "
            "requires advice, training, monitoring, fair inquiry and leadership."
        ),
        (
            "A department publishes selflessness and impartiality but gives no guidance for gifts, recusals or "
            "complaints. Which code distinction identifies the missing layer?"
        ),
        (
            "A service rule lists gift limits and disciplinary consequences but never explains constitutional "
            "public-purpose values. Which complementary instrument is needed?"
        ),
        "institutional safeguards",
    ),
    _mcq(
        "Indian asset-disclosure regimes must not be conflated",
        (
            "RPA s.75A requires an elected candidate to a House of Parliament to declare assets and liabilities "
            "within ninety days of oath; CCS Rule 18 and AIS Rule 16 create separate service-rule annual property-return "
            "regimes, while current Lokpal s.44 uses substituted prescribed-form wording."
        ),
        (
            "A note describes RPA section 75A as an annual return for every legislator and civil servant. "
            "Which statutory distinction corrects it?"
        ),
        (
            "An answer claims current Lokpal section 44 itself mandates universal online publication under its earlier "
            "elaborate text. Which amendment-sensitive caution applies?"
        ),
        "institutional safeguards",
    ),
    _mcq(
        "Audit and vigilance bodies have distinct roles",
        (
            "Departmental and CAG audit examine records, legality, regularity and performance within their mandates; "
            "CVC exercises vigilance oversight and CVOs coordinate departmental vigilance, while social audit enables "
            "citizens to compare official claims with lived delivery and demand follow-up."
        ),
        (
            "Workers compare muster rolls with actual employment at a public hearing, while financial auditors examine "
            "accounts separately. Which institutional distinction is illustrated?"
        ),
        (
            "A department asks its CVO to replace statutory audit, citizen verification and adjudicatory remedy. "
            "Which role-boundary principle rejects this consolidation?"
        ),
        "institutional safeguards",
    ),
    _mcq(
        "UNESCAP identifies eight characteristics of good governance",
        (
            "The UNESCAP formulation cited by the ARC describes good governance as participatory, consensus oriented, "
            "accountable, transparent, responsive, effective and efficient, equitable and inclusive, and following "
            "the rule of law."
        ),
        (
            "A government is transparent but systematically excludes affected communities and ignores legal limits. "
            "Which wider good-governance framework shows why transparency alone is insufficient?"
        ),
        (
            "A prelims option replaces responsiveness with secrecy while retaining seven familiar terms. "
            "Which exact eight-characteristic formulation resolves the trap?"
        ),
        "governance design and current application",
    ),
    _mcq(
        "Scrutiny should be graded by value, discretion and harm",
        (
            "Risk-graded scrutiny applies lighter documentation to routine low-value decisions and stronger ex-ante "
            "disclosure, competition, reasons and review to high-value, high-discretion or high-harm decisions, avoiding "
            "both uniform suspicion and blind trust."
        ),
        (
            "A department requires fifty approvals for every minor stationery purchase but little review of land allotment. "
            "Which design principle would reverse the mismatch?"
        ),
        (
            "A high-value specialised procurement carries narrow competition and major safety consequences. "
            "Which scrutiny approach is proportionate?"
        ),
        "governance design and current application",
    ),
    _mcq(
        "Bona-fide action needs protection, review and remedy",
        (
            "A sound probity regime protects documented bona-fide judgment and honest risk-taking while preserving "
            "independent review, correction and remedy for affected persons; protection from hindsight punishment is "
            "not immunity from reasons, evidence or accountability."
        ),
        (
            "An officer makes a reasoned emergency choice on incomplete information and later faces automatic punishment "
            "solely because the outcome was poor. Which safeguard applies?"
        ),
        (
            "A good-faith clause is invoked to block every appeal and deny compensation for proven harm. "
            "Which accountability qualification defeats that use?"
        ),
        "governance design and current application",
    ),
    _mcq(
        "A GeM Integrity Pact is an incorporated procurement control",
        (
            "A GeM bid may incorporate an Integrity Pact committing buyer and sellers against corrupt influence, "
            "collusion and misuse of electronic information while requiring equitable treatment and vigilance reporting; "
            "its contractual force depends on incorporation in the particular procurement."
        ),
        (
            "Bid document 9511605 requires bidders to upload a signed buyer-organisation Integrity Pact. "
            "Which ex-ante probity mechanism is illustrated?"
        ),
        (
            "An investigator treats the Pact as automatic proof of criminal guilt and a substitute for competition review. "
            "Which limitation applies?"
        ),
        "governance design and current application",
    ),
)


def _pyq(year, question, marks, source_note, answer):
    return {
        "year": year,
        "question": question,
        "marks": marks,
        "source_note": source_note,
        "answer": answer,
    }


PYQS = (
    _pyq(
        2018,
        (
            "GS-IV Q11: Dr. X is a leading medical practitioner in a city. He has set up a charitable "
            "trust through which he plans to establish a super-speciality hospital in the city to cater "
            "to the medical needs of all sections of the society. Incidentally, that part of the State "
            "had been neglected over the years. The proposed hospital would be a boon for the region.\n\n"
            "You are heading the tax investigation agency of that region. During an inspection of the "
            "doctor's clinic, your officers have found out some major irregularities. A few of them are "
            "substantial which had resulted in considerable withholding of tax that should be paid by him "
            "now. The doctor is cooperative. He undertakes to pay the tax immediately.\n\n"
            "However, there are certain other deficiencies in his tax compliance which are purely technical "
            "in nature. If these technical defaults are pursued by the agency, considerable time and energy "
            "of the doctor will be diverted to issues which are not so serious, urgent or even helpful to the "
            "tax collection process. Further, in all probability, it will hamper the prospects of the hospital "
            "coming up.\n\n"
            "There are two options before you: (i) Taking a broader view, ensure substantial tax compliance "
            "and ignore defaults that are merely technical in nature. (ii) Pursue the matter strictly and "
            "proceed on all fronts, whether substantial or merely technical. As the head of the tax agency, "
            "which course of action will you opt for and why? (Answer in 250 words)"
        ),
        20,
        (
            "Exact full case, facts and both options verified against "
            "books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf, page 10. Topic 14 supplies "
            "probity, propriety and proportionality; Topic 22 supplies the case-study architecture."
        ),
        (
            "Stakeholders are taxpayers, Dr. X, patients in a neglected region, the charitable trust, honest "
            "assessees, tax officials and the credibility of revenue administration. The competing values are "
            "legality, equality, revenue collection and deterrence on one side, and proportionality, administrative "
            "economy, public health and facilitation of a beneficial hospital on the other.\n\n"
            "Option (i) correctly prioritises substantial compliance but cannot mean informal waiver. Ignoring technical "
            "defaults without statutory authority may create unequal treatment, precedent and suspicion of favouritism. "
            "Option (ii) displays formal consistency, yet mechanically pursuing harmless defects may waste public resources "
            "and frustrate the law's revenue purpose without proportionate gain.\n\n"
            "I would adopt a reasoned, lawful version of the broader course. The agency should quantify and recover the "
            "withheld tax, interest and any legally warranted consequence after due process. Technical defaults should be "
            "classified: cure remediable defects within a written deadline; use statutory compounding, warning or minimal "
            "penalty where available; pursue any defect that conceals income, obstructs audit or affects third-party rights. "
            "The hospital proposal must not buy immunity, and the doctor should receive no treatment unavailable to a "
            "similarly placed taxpayer.\n\n"
            "I would record reasons, obtain competent legal approval, preserve an audit trail and separate the tax order "
            "from any decision concerning the charitable trust. A review route should remain open. This course joins "
            "procedural probity with substantive public purpose: it collects lawful revenue and protects equality while "
            "avoiding mindless formality. If the statute mandates action on a particular default, the agency must comply; "
            "discretion permits proportionality, not suspension of law."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q3(a): What is meant by the term 'constitutional morality'? How does one uphold "
            "constitutional morality? (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, "
            "page 2. Crisis of conscience in Q3(b) is excluded; Topic 10 remains a cross-link."
        ),
        (
            "Constitutional morality is fidelity to the Constitution's values, procedures and restraints on public "
            "power, rather than obedience to personal preference or a temporary majority. It requires liberty, equality, "
            "dignity, due process, institutional competence and non-arbitrariness to guide public action.\n\n"
            "It is upheld through civil education and repeated institutional practice: acting within lawful authority; "
            "giving affected persons notice and hearing; treating like cases alike; recording intelligible reasons; "
            "protecting minority participation; respecting checks and judicial review; and correcting decisions that fail "
            "constitutional standards. For example, a district officer should resist popular pressure to exclude a minority "
            "group from a public consultation and should preserve equal access through a reasoned order.\n\n"
            "Constitutional morality does not authorise an official to replace valid law with private ideology. It disciplines "
            "both majoritarian power and bureaucratic discretion through public reasons, lawful process and review. Thus it "
            "turns public office from personal command into accountable constitutional service."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q5(a): What do you understand by probity in governance? Based on your understanding "
            "of the term, suggest measures for ensuring probity in government. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, "
            "page 3. Emotional intelligence in Q5(b) is excluded."
        ),
        (
            "Probity in governance is upright, impartial and public-purpose conduct in entrusted office, made capable "
            "of public justification and appropriate verification. It draws on honesty, integrity and propriety but is "
            "not a rigid synonym or hierarchy; it asks whether power was exercised for authorised purposes through a "
            "fair and reviewable process.\n\n"
            "Measures should combine character and institutions: values-based recruitment and training; clear codes of "
            "ethics and conduct; timely conflict disclosure and recusal; transparent criteria and written reasons; "
            "e-procurement and tamper-evident records; proportionate asset declarations; independent departmental and CAG "
            "audit; effective CVC-CVO vigilance; RTI-compatible proactive disclosure; social audit where citizens can verify "
            "delivery; protected good-faith reporting; time-bound inquiry, appeal and remedy.\n\n"
            "Scrutiny should be risk-graded, strongest for high-value or high-discretion decisions, while documented bona-fide "
            "judgment receives protection from hindsight punishment. Probity is therefore neither private virtue alone nor "
            "paper compliance: it is ethical public purpose translated into traceable, contestable and correctable administration."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q6(a): An independent and empowered social audit mechanism is an absolute must in "
            "every sphere of public service, including judiciary, to ensure performance, accountability "
            "and ethical conduct. Elaborate. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, "
            "page 3. Topic 11 is the primary accountability owner; this is a probity cross-link."
        ),
        (
            "Social audit converts citizens from passive recipients into participants who compare official records with "
            "lived outcomes. Independence from the implementing body, proactive access to records, beneficiary verification "
            "and a public hearing can expose exclusion, ghost entries, weak performance and ethical failure hidden by files.\n\n"
            "Empowerment requires follow-up: a time-bound action-taken report, correction or compensation, recovery or "
            "disciplinary referral where evidence supports it, reasoned rejection of unsupported allegations and protection "
            "against intimidation. In MGNREGA, workers can compare job cards, muster rolls, wages and physical works.\n\n"
            "The phrase 'every sphere' needs functional adaptation. Judicial accountability cannot permit a crowd to dictate "
            "adjudication; confidentiality, decisional independence and lawful appellate or disciplinary structures must remain. "
            "Social audit complements, rather than replaces, CAG or departmental audit, vigilance, courts and statutory remedies. "
            "Its probity contribution is public verifiability joined to competent correction; disclosure without response is "
            "transparency, not complete accountability."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q6(b): 'Integrity is a value that empowers the human being.' Justify with suitable "
            "illustration. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, "
            "page 3. Topic 07/09 is primary; Topic 14 uses it to distinguish integrity from probity."
        ),
        (
            "Integrity empowers because consistency between principle, word and action reduces inner fragmentation and "
            "dependence on improper influence. A person who has settled ethical commitments can decide with courage, earn "
            "trust and cooperate without the continuing fear that concealed compromise will be exposed.\n\n"
            "For example, a procurement officer offered political protection for favouring a bidder can disclose the approach, "
            "apply published criteria and seek independent review. Integrity enables resistance because career convenience no "
            "longer determines the decision. Institutional safeguards still matter: secure reporting, written directions and "
            "fair inquiry convert personal courage into sustainable action.\n\n"
            "Integrity should not be collapsed into probity. Integrity is principled consistency and independence from improper "
            "influence; probity is the public-office standard that also asks whether entrusted power is demonstrably upright, "
            "impartial, public-purpose and reviewable. Nor is honesty merely a subset of integrity. These values overlap, but "
            "their functional distinctions help explain how character empowers the person while institutions protect the public."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q5(b)(iii): Write a short note in 30 words: Probity in public life. "
            "(Official demand: 2 marks and 30 words.)"
        ),
        2,
        (
            "Exact isolated short-note demand verified against books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER "
            "IV-190922.pdf, page 4. This model is deliberately expanded beyond the official 30-word demand to satisfy the "
            "current learner-v2 minimum-answer contract; it is for learning, not an exam-length prescription."
        ),
        (
            "Exam-ready 30-word core: Probity in public life is upright, impartial and public-purpose use of entrusted "
            "power, demonstrated through transparent reasons, conflict control, audit, answerability and effective remedy.\n\n"
            "Learning expansion: The definition combines ethical character with institutional verification. Honesty asks "
            "whether the official is truthful; integrity asks whether principle survives pressure; propriety asks whether "
            "conduct is appropriate to office; accountability asks whether a competent forum can examine and correct it. "
            "Probity brings these overlapping tests to the exercise of public power without turning them into a rigid hierarchy.\n\n"
            "Practical mechanisms include declared interests, recusal, written reasons, fair procurement, asset returns, audit "
            "trails, RTI-compatible disclosure and review. Yet paperwork alone is insufficient: a formally perfect decision "
            "designed for private capture fails substantive probity. In the examination, compress the first sentence to the "
            "official thirty-word demand; the longer treatment here exists only for conceptual mastery."
        ),
    ),
    _pyq(
        2023,
        (
            "GS-IV Q5(b): 'Probity is essential for an effective system of governance and socio-economic "
            "development.' Discuss. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, "
            "page 4. Conscience in Q5(a) is excluded."
        ),
        (
            "Probity makes public power upright, impartial, public-purpose and reviewable. It improves governance because "
            "written reasons, fair competition, conflict control and audit reduce arbitrary discretion, leakage and policy "
            "capture. Citizens and firms can plan when like cases receive like treatment, while officials gain a defensible "
            "record for bona-fide decisions.\n\n"
            "The development link is causal. Clean procurement yields more infrastructure from each rupee; transparent "
            "beneficiary selection improves inclusion; reliable regulation encourages investment; and correction mechanisms "
            "protect citizens from exclusion. Conversely, corruption and opaque discretion divert resources, raise transaction "
            "costs and distribute opportunity by connection rather than need or merit.\n\n"
            "Probity is necessary but not sufficient. UNESCAP's wider framework also requires participation, responsiveness, "
            "effectiveness, equity and rule of law. Excessive uniform scrutiny can delay legitimate action, so controls should "
            "be risk-graded and protect documented good faith while retaining review and remedy. Development becomes durable "
            "when ethical public purpose is supported by capable institutions, not moral exhortation alone."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q5(a): The 'Code of Conduct' and 'Code of Ethics' are the sources of guidance in "
            "public administration. There is code of conduct already in operation, whereas code of ethics "
            "is not yet put in place. Suggest a suitable model for code of ethics to maintain integrity, "
            "probity and transparency in governance. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, page 3. "
            "Topic 16 is the dedicated primary owner; the premise is retained as the PYQ's wording."
        ),
        (
            "A Code of Ethics should open with constitutional fidelity and public purpose, then state selflessness, "
            "integrity, merit objectivity, impartiality, openness, honest interest declaration, accountability and leadership "
            "by example. It should guide gifts, conflicts, post-employment, use of information, reasoned discretion, citizen "
            "treatment and good-faith dissent.\n\n"
            "Implementation is decisive: public adoption, confidential ethics advice, induction and scenario training, updated "
            "interest registers, recusal protocols, independent complaint handling, fair inquiry and an annual report on "
            "observance. Senior officers should record how recurring dilemmas were resolved without exposing protected data.\n\n"
            "A Code of Conduct remains complementary because it specifies behaviour, procedures and consequences. An ethics "
            "code cannot replace service rules, criminal law or due process, and a symbolic declaration cannot establish probity. "
            "The suitable model therefore joins Nolan-type principles with Indian constitutional morality, practical decision "
            "support, monitoring and remedy. It should be intelligible to citizens so transparency permits public evaluation "
            "of the standards claimed by administration."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q6(a): 'In Indian culture and value system, an equal opportunity has been provided "
            "irrespective of gender identity. The number of women in public service has been steadily "
            "increasing over the years.' Examine the gender-specific challenges faced by female public "
            "servants and suggest suitable measures to increase their efficiency in discharging their duties "
            "and maintaining high standards of probity. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, page 3. "
            "Topic 04 supplies foundational-values depth; Topic 14 owns the probity application."
        ),
        (
            "Women public servants may face unsafe field conditions, inadequate sanitation and childcare, sexual harassment, "
            "stereotyping in assignments, biased appraisal, disproportionate care burdens and exclusion from informal mentoring "
            "networks. These barriers reduce efficiency and can create pressure to rely on patronage or remain silent about "
            "misconduct.\n\n"
            "Measures include safe infrastructure and transport; functional Internal Committees with time-bound, confidential "
            "redress; childcare and gender-neutral flexible work without career penalty; transparent posting and appraisal "
            "criteria; structured mentoring; equal access to operational roles; and periodic gender audit of outcomes. Decisions "
            "on accommodation should use published eligibility, recorded reasons and review so support does not become favouritism.\n\n"
            "High probity is maintained not by demanding exceptional personal sacrifice but by designing institutions that permit "
            "impartial and documented performance. Harassment complaints require due process for both complainant and respondent. "
            "Equal opportunity is therefore substantive: removing gender-specific barriers improves capability while transparent "
            "rules, conflict controls and answerability preserve public trust."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q1(b): 'Constitutional morality is not a natural sentiment but a product of civil "
            "education and adherance of the rule of law.' Examine the significance of constitutional "
            "morality for public servant highlighting the role in promoting good governance and ensuring "
            "accountability in public administration. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart, including the printed spelling 'adherance', verified against "
            "books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, page 2. Social-media ethics in Q1(a) is excluded."
        ),
        (
            "Constitutional morality is learned fidelity to constitutional values, procedures and restraints, not an automatic "
            "sentiment. Civil education explains equality, liberty, dignity and institutional roles; repeated adherence to rule "
            "of law turns those commitments into administrative habit.\n\n"
            "For a public servant it requires lawful competence, impartial treatment, hearing, reasoned discretion, respect for "
            "minorities, honest advice and acceptance of review. A district officer who rejects popular pressure to exclude a "
            "community from relief and publishes neutral eligibility reasons demonstrates constitutional rather than majoritarian "
            "morality.\n\n"
            "This promotes good governance through predictable rules, transparency, participation and trust. It ensures "
            "accountability because reasons and records let legislatures, auditors, courts and citizens test whether power served "
            "its authorised purpose and obtain correction. Constitutional morality does not permit private conviction to override "
            "valid law; change must use competent constitutional channels. Its significance lies in converting public office from "
            "personal authority into disciplined, reviewable service to equal citizens."
        ),
    ),
)


ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Distinguish honesty, integrity, propriety, accountability and probity without arranging them "
            "in a rigid hierarchy."
        ),
        "answer": (
            "Honesty asks whether a person speaks truthfully, avoids deception and candidly declares relevant interests. "
            "Integrity asks whether ethical principle remains consistent under pressure and improper outside obligations. "
            "Propriety asks whether conduct is appropriate to the purpose and dignity of office, even where technically lawful. "
            "Accountability asks whether a competent forum can demand reasons, examine evidence and secure correction or consequence.\n\n"
            "Probity brings these overlapping tests to entrusted public power: is the conduct upright, impartial, public-purpose "
            "and capable of reasoned verification? They are not rigid nested sets. An officer may honestly disclose a sibling's "
            "bid yet fail propriety and probity by continuing to score it; transparency exists, but accountability remains incomplete "
            "without independent review and remedy.\n\n"
            "The examiner-safe method is functional comparison, not the claim that honesty is a subset of integrity or probity. "
            "Each concept illuminates a different failure point, while sound governance requires them to reinforce one another."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Why must procedural probity and substantive public purpose be assessed together in administration?"
        ),
        "answer": (
            "Procedural probity examines authority, notice, equal information, objective criteria, conflict controls, written "
            "reasons, records and review. Substantive probity examines whether the decision genuinely serves the authorised public "
            "purpose, respects equal citizenship and avoids private capture.\n\n"
            "Either can fail alone. A tender may contain perfect forms and scoring sheets but use tailor-made specifications to "
            "favour a connected vendor; procedure becomes a facade for an improper end. Conversely, an emergency officer may save "
            "lives through a reasonable departure from a minor formality, yet must record necessity, cure the defect and accept "
            "review. Good purpose cannot excuse corruption, but literalism should not defeat the law's purpose where lawful "
            "discretion exists.\n\n"
            "The combined test asks: was the route fair and traceable, and was the destination public-purpose? Written reasons, "
            "independent review and proportionate remedy connect both. Probity therefore rejects both results-only administration "
            "and compliance theatre."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Explain the public-office-as-trust idea and critically delimit it from India's settled "
            "environmental public-trust doctrine."
        ),
        "answer": (
            "Public-office-as-trust is an ethical fiduciary analogy. Citizens entrust authority, information, discretion and "
            "public money to officials for authorised purposes; office is therefore not personal property or a source of private "
            "favour. The analogy explains duties of loyalty to public purpose, care, impartiality, disclosure of conflicting "
            "interests and answerability for reasons.\n\n"
            "Its philosophical support is broad. Social-contract reasoning derives authority from citizens; Gandhian trusteeship "
            "treats possession and power as stewardship; deontology makes non-corrupt service a duty independent of detection; "
            "constitutional morality restrains office through equality, dignity and lawful process. A licensing officer who "
            "refuses to use confidential data for a relative acts consistently with this trust framing.\n\n"
            "The legal boundary is essential. India's settled environmental public-trust doctrine, associated with cases such as "
            "M.C. Mehta v. Kamal Nath, concerns State trusteeship of certain natural resources. It should not be cited as a direct "
            "holding governing every appointment, tax or procurement decision. Public-office-as-trust is persuasive ethical and "
            "administrative reasoning unless a specific legal duty independently applies.\n\n"
            "The analogy is useful because it converts power into stewardship, but precise answers separate philosophical extension "
            "from positive doctrine and identify the actual statute, service rule or review mechanism governing the case."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Discuss deontology, virtue ethics, Gandhian trusteeship and constitutional morality as "
            "complementary philosophical bases of probity."
        ),
        "answer": (
            "Deontology treats truthful, impartial and non-corrupt public action as a duty owed to persons and office, even when "
            "misconduct would be undetected or administratively convenient. It protects moral limits but can become mechanical if "
            "rules are applied without context.\n\n"
            "Virtue ethics asks what kind of public servant institutions cultivate. Habituated integrity, courage and justice make "
            "probity stable; phronesis, or practical wisdom, applies those virtues sensitively in unusual cases. Yet character alone "
            "needs public controls because citizens cannot audit an official's inner virtue.\n\n"
            "Gandhian trusteeship frames power and resources as stewardship for social welfare, while the unity of means and ends "
            "rejects bribery or deception even for an attractive project. It is an ethical analogy, not a universal statutory rule. "
            "Constitutional morality supplies the Indian public standard: equality, liberty, dignity, institutional competence, "
            "reasoned process and review restrain both personal preference and majority pressure.\n\n"
            "Together they answer four questions: what duty binds, what character sustains it, whose purpose power serves, and which "
            "constitutional limits govern. Institutions then translate philosophy into conflict registers, written reasons, audit, "
            "appeal and remedy. Probity is strongest when duty and virtue become publicly verifiable without reducing ethics to forms."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Design a risk-calibrated probity framework for high-value specialised public procurement without "
            "paralysing bona-fide administrative judgment."
        ),
        "answer": (
            "High-value specialised procurement combines fiscal exposure, technical information asymmetry, limited competition, "
            "safety consequences and wide official discretion. A sound framework must deter capture without assuming every official "
            "is corrupt.\n\n"
            "First, classify risk by value, discretion, market concentration, safety impact, urgency, past complaints and conflict "
            "exposure. Publish functional specifications and evaluation weights after independent market consultation, while "
            "protecting legitimate confidential data. Require evaluator interest declarations, recusal where material, segregation "
            "of technical and financial roles, equal bidder information and a secure electronic record. For the highest tier, use "
            "independent technical members, an incorporated Integrity Pact, beneficial-ownership and agent disclosure, reasoned "
            "deviation approval, competition review and milestone-based contract monitoring.\n\n"
            "Accountability must continue after award through inspection, change-order controls, payment audit, complaint windows, "
            "CVO vigilance coordination and CAG or departmental audit within mandate. Red flags should trigger focused inquiry, not "
            "automatic criminal inference. Affected bidders need reasoned debriefing and review; proven loss requires correction, "
            "recovery or other lawful remedy.\n\n"
            "Bona-fide judgment should receive a safe harbour when authority was verified, material facts disclosed, alternatives "
            "considered, reasons contemporaneously recorded and no improper interest existed. The protection defeats hindsight "
            "punishment, not audit or appeal. Routine low-risk purchases should face lighter controls so expertise remains available "
            "for serious risks.\n\n"
            "Thus risk grading reconciles probity with administrative capacity: scrutiny rises with potential harm, while documented "
            "good faith, independent review and proportionate remedy preserve decisive, timely and trustworthy public service."
        ),
    },
    {
        "marks": 20,
        "question": (
            "You chair a tender committee for essential hospital equipment. A technically strong preferred vendor "
            "has supplied the department reliably for years, but its local agent is your former business partner and "
            "the tender specifications closely match that vendor's product. Evaluate the options and recommend action."
        ),
        "answer": (
            "Stakeholders are patients, competing vendors, taxpayers, hospital staff, the preferred supplier, the local agent, "
            "the committee and the chair. The issues are actual or apparent conflict, possible tailor-made specifications, "
            "continuity and safety, competition, confidential information and public trust.\n\n"
            "The chair could continue after private assurance of fairness; disclose but retain the vote; cancel the process "
            "immediately; or disclose, recuse and obtain independent review of the specifications. Silence preserves speed but "
            "makes every later decision suspect. Disclosure without recusal may not cure a material former financial relationship. "
            "Automatic cancellation wastes time and may disrupt essential care before facts are tested.\n\n"
            "I would file a complete written disclosure, cease contact with the agent and recuse from specification and evaluation "
            "decisions. The competent authority should appoint an independent chair and technical reviewers. They should test whether "
            "each specification follows patient need and interoperability or unnecessarily excludes equivalent products. Any change "
            "must be notified equally, with adequate bid time. Existing evaluation data and electronic logs should be preserved.\n\n"
            "If only that product can safely meet a documented need, a lawful limited-competition route may be used with market-price "
            "benchmarking, recorded reasons, higher approval and post-award audit. If specifications were manipulated, the tender "
            "should be corrected or reissued and supported misconduct referred through due process. Urgent interim supply should be "
            "narrow, time-bound and separately approved.\n\n"
            "The recommendation protects both procedure and public purpose. It does not punish a reliable vendor merely for association, "
            "nor permit reliability to become inherited entitlement. Recusal, independent technical judgment, equal information, review "
            "and continuity safeguards produce a defensible patient-centred result."
        ),
    },
)


def _panel(title, structural_type, nodes, verdict, answer_use):
    return {
        "title": title,
        "structural_type": structural_type,
        "nodes": nodes,
        "verdict": verdict,
        "answer_use": answer_use,
    }


ASCII_PANELS = (
    _panel(
        "1. Entrusted office and legitimacy",
        "entrustment-chain",
        (
            "Citizens confer authority",
            "Law defines competence",
            "Office holds discretion",
            "Public purpose limits use",
            "Reasons explain choice",
            "Records permit scrutiny",
            "Review corrects error",
            "Legitimacy earns trust",
        ),
        "Public power becomes legitimate when entrusted authority remains purpose-bound and reviewable.",
        "Use to define probity and open governance answers.",
    ),
    _panel(
        "2. Non-hierarchical overlap map",
        "overlap-matrix",
        (
            "Honesty: truthful disclosure",
            "Integrity: principle under pressure",
            "Propriety: fitness for office",
            "Transparency: visible record",
            "Accountability: answer and correct",
            "Probity: public-office test",
            "Concepts overlap",
            "No rigid nesting",
        ),
        "Compare functional questions; never reduce honesty to a settled subset.",
        "Use for definitions, distinctions and close-option traps.",
    ),
    _panel(
        "3. Law, propriety and remedy",
        "three-stage-test",
        (
            "Identify legal authority",
            "Check mandatory procedure",
            "Test equality and fairness",
            "Ask office appropriateness",
            "Ask authorised purpose",
            "Record proportional reasons",
            "Provide competent review",
            "Secure correction or remedy",
        ),
        "Legality is the floor; propriety, purpose and remedy complete the probity inquiry.",
        "Use for Dr. X and form-versus-substance cases.",
    ),
    _panel(
        "4. Conflict and recusal route",
        "conflict-decision-tree",
        (
            "Identify private interest",
            "Assess material connection",
            "Disclose before decision",
            "Stop informal contact",
            "Recuse when impartiality risks",
            "Reassign independently",
            "Preserve decision record",
            "Review appearance and outcome",
        ),
        "Private confidence in fairness cannot replace institutional conflict control.",
        "Use for procurement, licensing and appointment cases.",
    ),
    _panel(
        "5. High-discretion control stack",
        "risk-control-stack",
        (
            "Grade value and harm",
            "Publish objective criteria",
            "Give equal information",
            "Separate decision roles",
            "Record conflicts and recusals",
            "Require written reasons",
            "Use focused audit",
            "Keep appeal and remedy",
        ),
        "Controls should intensify with discretion, value and foreseeable harm.",
        "Use for land, licensing and specialised procurement.",
    ),
    _panel(
        "6. Deontology and constitutional morality",
        "dual-foundation-chain",
        (
            "Duty binds despite detection",
            "Persons are not mere means",
            "Office limits private gain",
            "Constitution supplies values",
            "Equality disciplines choice",
            "Due process disciplines means",
            "Review restrains power",
            "Public reason joins both",
        ),
        "Duty sets moral limits; constitutional morality gives them public institutional form.",
        "Use for philosophical-basis and 2019/2025 PYQs.",
    ),
    _panel(
        "7. Virtue and phronesis",
        "character-to-judgment",
        (
            "Practice truthful conduct",
            "Build stable integrity",
            "Cultivate courage",
            "Cultivate justice",
            "Read context carefully",
            "Balance relevant duties",
            "Choose proportionate means",
            "Accept public verification",
        ),
        "Practical wisdom applies stable virtue without abandoning reasons or institutions.",
        "Use when rules leave lawful discretion.",
    ),
    _panel(
        "8. Trusteeship boundary",
        "analogy-boundary-map",
        (
            "Authority comes from citizens",
            "Office is not property",
            "Gandhi: power as stewardship",
            "Means must fit ends",
            "Public-office trust is analogy",
            "Natural-resource doctrine is settled",
            "M.C. Mehta boundary retained",
            "Specific law still controls",
        ),
        "Use trusteeship philosophically, not as a universal environmental-doctrine holding.",
        "Use to gain sophistication without legal overclaiming.",
    ),
    _panel(
        "9. Procurement Integrity Pact",
        "pact-control-chain",
        (
            "Incorporate pact in bid",
            "Buyer rejects corrupt influence",
            "Sellers reject bribery",
            "Sellers reject collusion",
            "Protect electronic information",
            "Treat bidders equitably",
            "Report vigilance concerns",
            "Retain other safeguards",
        ),
        "The Pact is an incorporated preventive control, not proof of guilt or a complete regime.",
        "Use with GeM bid document 9511605.",
    ),
    _panel(
        "10. Asset-disclosure distinctions",
        "four-regime-comparison",
        (
            "RPA s75A: elected MP",
            "File within 90 days of oath",
            "Not an annual RPA return",
            "CCS Rule 18: service regime",
            "AIS Rule 16: separate regime",
            "Annual property returns differ",
            "Lokpal s44 text substituted",
            "No universal online claim",
        ),
        "State the population, timing and legal source of each disclosure duty separately.",
        "Use for Prelims traps and probity mechanisms.",
    ),
    _panel(
        "11. RTI, audit and social audit",
        "scrutiny-ecosystem",
        (
            "Records make action visible",
            "RTI enables lawful access",
            "Departmental audit checks systems",
            "CAG acts within mandate",
            "CVC oversees vigilance",
            "CVO coordinates departments",
            "Citizens verify lived delivery",
            "Follow-up supplies accountability",
        ),
        "No single institution replaces financial, vigilance, citizen and remedial scrutiny.",
        "Use for 2021 social-audit and transparency answers.",
    ),
    _panel(
        "12. Bona fides and proportionate review",
        "balanced-review-route",
        (
            "Verify authority and facts",
            "Disclose material interests",
            "Consider reasonable alternatives",
            "Record contemporaneous reasons",
            "Protect honest risk-taking",
            "Review without outcome bias",
            "Correct proven error",
            "Remedy supported harm",
        ),
        "Good-faith protection blocks hindsight punishment, not evidence, review or remedy.",
        "Use as the final advanced answer and case-study test.",
    ),
)


CURRENT_ANCHOR = {
    "title": (
        "GeM Integrity Pact Guidelines and GeM bid document no. 9511605, created 23 June 2026"
    ),
    "verified_facts": (
        "The GeM Integrity Pact guidelines record buyer and seller commitments against corrupt practices and improper influence in bidding and contract execution.",
        "Seller commitments cover bribery, undisclosed agreements, restriction of competitiveness, cartelisation, misuse of electronically transmitted information and disclosure of intermediary payments.",
        "Buyer commitments include equitable and reasonable treatment, equal information during the bid process and reporting relevant suspected criminal conduct to the Chief Vigilance Officer.",
        "The official bid document linked as no. 9511605 was created on 23 June 2026 and records a buyer-added term requiring bidders to upload a signed buyer-organisation Integrity Pact.",
        "The digital bid document supplies an electronic record of the incorporated requirement and the buyer-added terms.",
    ),
    "administrative_link": (
        "The anchor shows procedural probity made ex ante and reviewable: anti-bribery, anti-collusion, "
        "equal-treatment, reporting and electronic-record commitments are placed inside a particular procurement "
        "rather than left as private moral aspiration."
    ),
    "limit": (
        "The Pact's force depends on incorporation in the bid or contract. It does not cover every GeM procurement, "
        "establish criminal guilt, or replace eligibility checks, conflict screening, competition safeguards, audit, "
        "CVC or CVO action, and statutory review or remedies."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://gem.gov.in/resources/pdf/Integrity-pact-guidelines.pdf",
    "https://bidplus.gem.gov.in/showbidDocument/9511605",
)


SOURCE_CAVEAT = (
    "The corrected canonical Topic 14 Basic and Advanced owners control the doctrinal spine. Honesty, "
    "integrity, propriety, transparency, accountability and probity overlap but are not a strict hierarchy; "
    "never state that honesty is a subset of integrity or probity. The description of verifiability is an "
    "analytical working test: reasons, records and scrutiny help demonstrate probity, but paperwork is neither "
    "its dictionary definition nor a substitute for public purpose. The public-office-as-trust formulation is "
    "an ethical fiduciary and Gandhian analogy. India's settled environmental public-trust doctrine concerns "
    "State trusteeship of certain natural resources; do not claim that it directly governs every public-office "
    "decision. RPA section 75A applies to an elected candidate to a House of Parliament and requires filing "
    "within ninety days of oath; it is not an annual return and does not itself cover every State legislator or "
    "civil servant. CCS (Conduct) Rules, 1964, Rule 18 and All India Services (Conduct) Rules, 1968, Rule 16 are "
    "separate service-rule property-return regimes. Lokpal and Lokayuktas Act section 44 must be described using "
    "its current substituted text, which requires every public servant to make a declaration in the prescribed "
    "form and manner; do not reproduce the former elaborate publication regime as current law. UNESCAP's eight "
    "characteristics, as cited by the ARC, frame good governance more broadly than probity alone. ARC and Nolan "
    "material should be attributed within their actual scope: Nolan's outside-obligations wording is a bounded "
    "integrity formulation, not the whole ordinary concept, and ARC recommendations or quotations are not enacted "
    "law merely because they are authoritative reform material. Official PYQ PDFs control exact question text; "
    "routing ledgers establish topic ownership only. Each PYQ here isolates the specified subpart: no social-media, "
    "emotional-intelligence, conscience or other paired demand is imported. The 2022 two-mark short note is expanded "
    "only to meet the learner-v2 minimum-answer contract and explicitly preserves the official thirty-word demand. "
    "The GeM anchor is bounded to the official Integrity Pact guidelines and bid document no. 9511605 dated 23 June "
    "2026. Incorporation gives the Pact relevance to that procurement; it neither covers every GeM bid nor proves "
    "criminal guilt, and it cannot replace eligibility, conflict and competition checks, audit, CVC-CVO vigilance, "
    "or statutory review and remedy."
)


REGISTER_SUPPLEMENT = (
    "### PROBITY: THE COMPLETE CORE MAP\n\n"
    "- **UPSC scope:** the syllabus couples the philosophical basis of governance with probity in governance; answer in the setting of entrusted public office, not private manners alone.\n"
    "- **Working definition:** upright, impartial and public-purpose conduct in entrusted office, supported by reasons and records capable of appropriate public justification and verification.\n"
    "- **Verifiability caution:** this is an analytical test, not a claim that paperwork defines probity. A complete file can conceal capture, while an urgent bona-fide act may cure a minor procedural defect.\n"
    "- **Entrusted power:** authority, discretion, confidential information and public money are held for authorised citizen-facing purposes, never as personal property or favour.\n\n"
    "### DISTINCTIONS WITHOUT A FALSE HIERARCHY\n\n"
    "- **Honesty:** truthfulness, non-deception and candid disclosure of material facts and interests.\n"
    "- **Integrity:** principled consistency and resistance to improper influence. Nolan's ARC-reproduced wording focuses on outside obligations influencing duty; it is not the exhaustive ordinary definition.\n"
    "- **Propriety:** appropriateness, fairness and fitness of conduct for the purpose and dignity of office, including technically lawful conduct.\n"
    "- **Transparency:** visibility of criteria, interests, reasons and records to appropriate scrutiny, subject to lawful privacy and confidentiality.\n"
    "- **Accountability:** answerability before a competent forum plus the capacity for correction, remedy or consequence.\n"
    "- **Probity:** the integrated public-office question -- was entrusted power exercised uprightly, impartially, for public purpose and in a reviewable manner?\n"
    "- **Exam warning:** these concepts overlap. Never write that honesty is a settled subset of integrity or probity.\n\n"
    "### PROCEDURE, SUBSTANCE AND PUBLIC PURPOSE\n\n"
    "- **Procedural probity:** lawful competence, notice, equal information, objective criteria, conflict control, written reasons, record preservation, audit trail and review.\n"
    "- **Substantive probity:** the decision and real effects must serve the authorised public purpose, respect equality and avoid disguised private capture.\n"
    "- **Double test:** fair route plus proper destination. Tailor-made tender specifications fail substance despite perfect forms; a life-saving emergency departure requires necessity, recorded reasons, cure and review.\n"
    "- **Written reasons:** discipline discretion, expose irrelevant considerations and enable appeal, audit and learning.\n"
    "- **Conflict route:** identify interest -> assess materiality -> disclose -> recuse or independently reassign where impartiality or its appearance is compromised -> preserve records -> review.\n\n"
    "### PHILOSOPHICAL BASIS OF GOVERNANCE\n\n"
    "- **Deontology:** truthful and impartial public action is a duty owed even when misconduct would remain hidden or produce convenient results.\n"
    "- **Virtue ethics:** probity is cultivated public character; courage, justice and integrity become habits rather than episodic compliance.\n"
    "- **Phronesis:** practical wisdom applies virtues and lawful rules sensitively to context without sliding into personal whim.\n"
    "- **Gandhi:** trusteeship treats power and resources as stewardship for social welfare; unity of means and ends rejects corrupt means for an attractive project.\n"
    "- **Constitutional morality:** learned fidelity to liberty, equality, dignity, lawful competence, due process, checks, reasons and review rather than personal or majoritarian preference.\n"
    "- **Public-office-as-trust boundary:** a persuasive ethical fiduciary analogy. The settled environmental public-trust doctrine concerns certain natural resources and is not a direct legal rule for every office decision.\n\n"
    "### INDIAN DISCLOSURE AND CODE ARCHITECTURE\n\n"
    "- **RPA, 1951, s.75A:** elected candidate to a House of Parliament; declaration of assets and liabilities within ninety days of taking oath. It is not an annual RPA return.\n"
    "- **CCS Conduct Rule 18:** separate civil-service property-transaction and annual immovable-property-return architecture for the relevant service categories.\n"
    "- **AIS Conduct Rule 16:** separate All India Services property-return regime; do not merge its legal source with CCS Rule 18.\n"
    "- **Lokpal Act s.44:** use current substituted prescribed-form-and-manner text; do not assert that the former detailed universal online-publication wording remains current.\n"
    "- **Code of Ethics:** values and decision principles -- constitutional fidelity, selflessness, integrity, impartiality, openness, accountability and leadership.\n"
    "- **Code of Conduct:** specific expected or prohibited behaviour, procedures and consequences. Advice, training, interest registers, fair inquiry and reporting make both credible.\n\n"
    "### SCRUTINY ECOSYSTEM\n\n"
    "- **Departmental audit:** tests records, controls, compliance and performance within the department's mandate.\n"
    "- **CAG:** constitutional external audit within its legal mandate; it does not replace vigilance investigation, courts or departmental responsibility.\n"
    "- **CVC:** vigilance oversight and integrity-system guidance within jurisdiction.\n"
    "- **CVO:** coordinates vigilance work inside an organisation and connects it with competent authorities; it is not a substitute for every audit or remedy.\n"
    "- **Social audit:** citizens compare official records with lived delivery through accessible evidence and public verification. Independence, an action-taken report and protection against intimidation are essential.\n"
    "- **RTI and proactive disclosure:** provide lawful access to criteria, records and reasons; exemptions and privacy still require disciplined application.\n"
    "- **Accountability chain:** disclose -> verify -> hear -> decide -> correct or remedy -> learn. Transparency alone stops before completion.\n\n"
    "### GOOD GOVERNANCE AND RISK-GRADED SCRUTINY\n\n"
    "- **UNESCAP eight:** participatory; consensus oriented; accountable; transparent; responsive; effective and efficient; equitable and inclusive; follows the rule of law.\n"
    "- **Probity is necessary, not sufficient:** participation, capability, responsiveness and equity remain independent governance requirements.\n"
    "- **Risk grading:** increase ex-ante controls with value, discretion, market concentration, safety or rights impact, urgency and conflict exposure.\n"
    "- **Low risk:** standard records and sample audit. **High risk:** independent expertise, interest declarations, equal information, reasoned deviations, electronic logs, focused audit and review.\n"
    "- **Bona-fide protection:** protect contemporaneously reasoned, authorised and conflict-free judgment from outcome bias and hindsight punishment.\n"
    "- **Limit:** good faith never blocks audit, appeal, correction, compensation or action on supported misconduct.\n\n"
    "### CURRENT PROCUREMENT ANCHOR: GEM 2026\n\n"
    "- **Guidelines:** buyer and sellers commit against corrupt influence; sellers also reject bribery, collusion, cartelisation and misuse of electronically transmitted information.\n"
    "- **Buyer duties:** equitable treatment, equal bid information and vigilance reporting where the stated threshold is met.\n"
    "- **Bid document no. 9511605:** created 23 June 2026; its buyer-added terms require bidders to upload a signed buyer-organisation Integrity Pact.\n"
    "- **Learning use:** the electronic bid record makes an ex-ante ethical commitment traceable and contract-linked.\n"
    "- **Limit:** incorporation controls force. The Pact does not govern every GeM procurement, prove criminal guilt or replace eligibility, conflict screening, competition safeguards, audit, CVC-CVO action or statutory remedies.\n\n"
    "### SOLVED-PYQ ROUTES\n\n"
    "- **2018 Q11, Dr. X:** reject both informal waiver and mindless literalism. Recover substantial dues, classify technical defaults lawfully, record proportional reasons, ensure equal treatment and preserve review.\n"
    "- **2019 Q3(a):** define constitutional morality, then show civil education, equality, due process, public reasons, checks and correction.\n"
    "- **2019 Q5(a):** definition first; then conflicts, codes, reasons, digital records, audit, disclosure, social audit, inquiry and remedy.\n"
    "- **2021 Q6(a):** social audit adds citizen verification but must be adapted to judicial independence and complemented by competent follow-up.\n"
    "- **2021 Q6(b):** integrity empowers principled action; distinguish it from probity without inventing a hierarchy.\n"
    "- **2022 Q5(b)(iii):** official demand is only thirty words and two marks; use the compressed definition, not the learning expansion.\n"
    "- **2023 Q5(b):** build the causal chain from probity to lower leakage, fair opportunity, investment confidence, inclusion and effective development.\n"
    "- **2024 Q5(a):** propose a values code plus advice, training, disclosure, monitoring, fair inquiry and leadership; retain conduct rules separately.\n"
    "- **2024 Q6(a):** remove gender-specific barriers through transparent institutional design; maintain probity through published criteria, reasons and review.\n"
    "- **2025 Q1(b):** connect civil education and rule of law to accountable constitutional habits; isolate it from the social-media subpart.\n\n"
    "### RAPID PRELIMS TRAPS\n\n"
    "- Probity is not identical to honesty, integrity, transparency or accountability.\n"
    "- Honesty is not to be stated as a subset of integrity or probity.\n"
    "- Nolan's integrity wording is bounded to outside obligations influencing official duty.\n"
    "- Public-office-as-trust is an ethical analogy; environmental public-trust doctrine is legally settled in a narrower natural-resource setting.\n"
    "- RPA s.75A is post-election, Parliament-focused and within ninety days of oath, not an annual civil-service return.\n"
    "- CCS Rule 18, AIS Rule 16 and Lokpal s.44 are distinct legal sources.\n"
    "- Maximum paperwork is not maximum probity; use risk-graded scrutiny.\n"
    "- An Integrity Pact is preventive and procurement-specific when incorporated; it is not a criminal conviction.\n\n"
    "### ANSWER METHOD: DEFINE -> DISTINGUISH -> GROUND -> INSTITUTIONALISE -> QUALIFY\n\n"
    "1. **Define** probity in one sentence with entrusted office, uprightness, impartiality and public purpose.\n"
    "2. **Distinguish** the nearest concept functionally; avoid rigid nesting.\n"
    "3. **Ground** the claim in one philosophy -- duty, virtue/phronesis, trusteeship or constitutional morality.\n"
    "4. **Institutionalise** it through a named mechanism: recusal, written reasons, code, asset return, audit, RTI, social audit, vigilance, review or remedy.\n"
    "5. **Apply** one India-centric administrative example and trace claim -> named evidence -> analysis.\n"
    "6. **Qualify** the strongest boundary: privacy, confidentiality, legal competence, doctrinal scope, good faith or proportional scrutiny.\n"
    "7. **Conclude** that probity joins ethical public purpose to demonstrable, reviewable and correctable exercise of power."
)
