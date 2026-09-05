"""Source-grounded content data for learner-v2: Ethics and Human Interface."""

SESSION_TITLES = (
    "Where Ethics Enters Everyday Public Life",
    "Four Ways to Ask an Ethical Question",
    "Ethics, Morality, Law, and Propriety",
    "The Human Interface: Power Meets Citizen Need",
    "Why Values Need Institutions",
    "How Systems Produce or Prevent Corruption",
    "Coercive and Collusive Corruption: Do Not Confuse Them",
    "Citizen Power, Transparency, and Ethical Governance",
    "Constitutional Morality and National Power",
    "Writing a Balanced GS-IV Ethics Answer",
)

SESSION_GROUPS = (
    (1, 2),
    (3,),
    (4,),
    (5,),
    (6,),
    (7,),
    (8,),
    (9,),
    (10, 11),
    (12, 13),
)

MCQ_ITEMS = (
    {
        "label": "Ethics and morality",
        "statement": (
            "Ethics is the systematic and reasoned examination of standards of right conduct, "
            "whereas morality denotes the beliefs and practices actually held by persons or "
            "communities; they overlap in ordinary usage but should be distinguished when an "
            "ethical claim is being critically assessed."
        ),
        "scenario_a": (
            "A district team surveys customary views on accepting festival gifts, then asks "
            "whether the practice is defensible for procurement officers. Which part is moral "
            "description and which is ethical evaluation?"
        ),
        "scenario_b": (
            "A senior says, 'Everyone in this office gives priority to relatives, so it is "
            "right.' Identify why a shared practice does not by itself settle an ethical question."
        ),
        "group": "Foundations and inquiry",
    },
    {
        "label": "Descriptive inquiry",
        "statement": (
            "Descriptive ethics records what individuals or groups in fact believe, approve, "
            "or do; it neither establishes what they ought to do nor excuses a practice merely "
            "because it is widespread."
        ),
        "scenario_a": (
            "A state training institute reports that many field staff see small facilitation "
            "payments as normal. Is its report descriptive ethics, a normative defence, or both?"
        ),
        "scenario_b": (
            "A municipal survey finds that residents tolerate queue-jumping for elderly relatives. "
            "What additional inquiry is needed before an officer can adopt the practice as policy?"
        ),
        "group": "Foundations and inquiry",
    },
    {
        "label": "Normative inquiry",
        "statement": (
            "Normative ethics asks what ought to be done and justifies the answer through "
            "standards such as duty, consequences, justice, or virtue; it cannot be reduced "
            "to a report of prevailing attitudes."
        ),
        "scenario_a": (
            "A hospital superintendent must decide whether to publish a waiting list despite "
            "staff discomfort. Which inquiry tests the duty of fairness rather than merely "
            "measuring staff opinion?"
        ),
        "scenario_b": (
            "A panchayat notes that a majority supports excluding migrants from a water queue. "
            "Which ethical approach asks whether the majority preference is justifiable?"
        ),
        "group": "Foundations and inquiry",
    },
    {
        "label": "Meta-ethics",
        "statement": (
            "Meta-ethics examines the meaning, status, and possible truth of moral language, "
            "for example whether 'wrong' states an objective fact or expresses an attitude; "
            "it is conceptually useful but usually subordinate to normative and applied reasoning "
            "in GS-IV answers."
        ),
        "scenario_a": (
            "Two trainees debate whether the word 'integrity' can ever have a truth value, "
            "without discussing a pending service decision. Which level of ethical inquiry is "
            "their debate conducting?"
        ),
        "scenario_b": (
            "An answer to a flood-relief dilemma spends its entire space on whether moral "
            "judgments are objective. Why does that miss the principal applied task?"
        ),
        "group": "Foundations and inquiry",
    },
    {
        "label": "Applied ethics",
        "statement": (
            "Applied ethics brings normative standards to a definite domain, such as public "
            "administration, medicine, business, environmental regulation, or artificial "
            "intelligence, by testing a concrete decision rather than merely naming a theory."
        ),
        "scenario_a": (
            "A district magistrate applies fairness, harm prevention, and accountability to an "
            "AI-assisted beneficiary list. Why is this applied ethics rather than meta-ethics?"
        ),
        "scenario_b": (
            "A doctor explains that confidentiality is important, then decides whether to share "
            "a notifiable disease report with the health authority. What makes this an applied "
            "ethical decision?"
        ),
        "group": "Foundations and inquiry",
    },
    {
        "label": "Legality, morality, propriety",
        "statement": (
            "Legality tests conformity with enacted law, morality tests conformity with a "
            "standard of right conduct, and propriety tests what is appropriate to an office "
            "and occasion; an action can satisfy the letter of law yet fail morality or public "
            "propriety."
        ),
        "scenario_a": (
            "A licensing officer accepts a lavish dinner from a bidder before any formal decision. "
            "No payment is proved and no rule is visibly breached. Which ethical test most clearly "
            "identifies the public-confidence problem?"
        ),
        "scenario_b": (
            "A municipal councillor lawfully uses official social media to praise a relative's "
            "firm during a tender period. Why is legality alone an incomplete ethical defence?"
        ),
        "group": "Ethical tests and professional judgment",
    },
    {
        "label": "Spirit and letter",
        "statement": (
            "Ethical public conduct requires attention to the spirit as well as the letter of "
            "rules, because narrowly legal conduct may create a reasonable appearance of bias, "
            "private favour, or misuse of entrusted position."
        ),
        "scenario_a": (
            "A collector arranges a private interview with one of several land-acquisition bidders "
            "outside office hours, while retaining the formal record required by law. What concern "
            "arises even if the meeting is not expressly prohibited?"
        ),
        "scenario_b": (
            "An officer awards a contract after following every formality but suppresses a known "
            "conflict that did not trigger a mandatory disclosure rule. Which distinction exposes "
            "the ethical defect?"
        ),
        "group": "Ethical tests and professional judgment",
    },
    {
        "label": "Human interface",
        "statement": (
            "The human interface is the point at which an official's public duty encounters a "
            "citizen's need and possible private interest; ethical quality is tested most sharply "
            "where discretion, vulnerability, delay, and unequal power converge."
        ),
        "scenario_a": (
            "A widow seeking a pension must repeatedly meet a clerk who can delay verification. "
            "Why is this more than a technical service-delivery problem?"
        ),
        "scenario_b": (
            "A fully automated utility payment system gives identical receipts and appeal routes "
            "to every user. Which part of the human-interface ethical risk has it reduced?"
        ),
        "group": "Ethical tests and professional judgment",
    },
    {
        "label": "Professional decision-making",
        "statement": (
            "Responsible professional decision-making combines reasons, relevant facts, duty to "
            "affected persons, foreseeable consequences, fairness, and accountability; personal "
            "good intention alone cannot cure a biased procedure or an unreviewable decision."
        ),
        "scenario_a": (
            "A welfare officer sincerely wants to help a neighbour but bypasses the published "
            "eligibility list. Which professional dimensions besides benevolent intention must "
            "be tested?"
        ),
        "scenario_b": (
            "A public hospital adopts a triage rule that is transparent and reviewable but produces "
            "hard individual outcomes. Why is accountability relevant alongside compassion?"
        ),
        "group": "Ethical tests and professional judgment",
    },
    {
        "label": "Values and institutions",
        "statement": (
            "Values orient conduct, but durable integrity also needs institutional containers: "
            "clear procedures, transparency, competent supervision, sanctions, and appeal routes. "
            "Neither moral exhortation alone nor punishment alone adequately explains or corrects "
            "ethical failure."
        ),
        "scenario_a": (
            "A department conducts an integrity pledge every Monday but has no audit trail for "
            "approvals. Why may its values programme fail under procurement pressure?"
        ),
        "scenario_b": (
            "Another department installs surveillance and harsh penalties but never trains staff "
            "to recognise conflicts of interest. What limitation does the values-institutions "
            "framework reveal?"
        ),
        "group": "Values, institutions, and structural causes",
    },
    {
        "label": "Decline-of-values view",
        "statement": (
            "The decline-of-values explanation locates corruption primarily in weakened character "
            "and therefore stresses moral renewal; it identifies a real concern but is incomplete "
            "when it overlooks discretion, opacity, monopoly, and incentives created by institutions."
        ),
        "scenario_a": (
            "After bribery complaints, a state orders only motivational lectures for revenue staff "
            "while leaving approvals discretionary and unrecorded. Which causal explanation is "
            "being overextended?"
        ),
        "scenario_b": (
            "A trainee says all corruption proves officials are personally immoral. How would the "
            "structural account qualify, rather than wholly deny, that claim?"
        ),
        "group": "Values, institutions, and structural causes",
    },
    {
        "label": "Deviant-minority view",
        "statement": (
            "The deviant-minority explanation treats corruption as the work of a small self-interested "
            "group and emphasises detection and punishment; deterrence is necessary, but this view "
            "is incomplete where routine systems reward opaque discretion or make citizens dependent."
        ),
        "scenario_a": (
            "A vigilance drive arrests several brokers but retains the same manual, opaque permit "
            "process that created demand for brokers. What does the deviant-minority view miss?"
        ),
        "scenario_b": (
            "A department says one suspended officer has solved its ethical problem. Which "
            "institutional question should an auditor ask next?"
        ),
        "group": "Values, institutions, and structural causes",
    },
    {
        "label": "Asymmetry of power",
        "statement": (
            "Asymmetry of power weakens the citizen's ability to demand ethical conduct because "
            "the official controls information, time, access, or certification; transparency, "
            "voice, and review mechanisms therefore have ethical as well as administrative value."
        ),
        "scenario_a": (
            "A tribal applicant cannot read the online land-record status and relies on an "
            "intermediary connected to the office. Which structural ethical condition is most "
            "relevant before blaming the applicant for paying a fee?"
        ),
        "scenario_b": (
            "A service centre displays timelines, fees, reasons for rejection, and an independent "
            "appeal channel. How does this change the official-citizen power relationship?"
        ),
        "group": "Values, institutions, and structural causes",
    },
    {
        "label": "Centralisation and accountability",
        "statement": (
            "Over-centralisation can widen the distance between authority and accountability by "
            "placing many functionaries between the citizen and the decision-maker; decentralisation "
            "helps only when local capacity, transparency, and audit prevent smaller discretionary monopolies."
        ),
        "scenario_a": (
            "A village water repair waits for four remote approvals, each without a public timeline. "
            "Which mechanism links this design to the ethical quality of service?"
        ),
        "scenario_b": (
            "A gram panchayat receives fund-control power but keeps no public works register. Why "
            "is decentralisation not automatically an integrity guarantee?"
        ),
        "group": "Values, institutions, and structural causes",
    },
    {
        "label": "Coercive corruption",
        "statement": (
            "Coercive corruption occurs when an official extracts payment or favour for a service "
            "to which a citizen is entitled, making the citizen an unwilling victim; its ethical "
            "core is extortion through public power, not a mutually beneficial bargain."
        ),
        "scenario_a": (
            "A clerk refuses to release a widow's sanctioned pension unless she pays a 'file "
            "movement' charge. Is the widow a collusive beneficiary or an unwilling victim, and why?"
        ),
        "scenario_b": (
            "A driving-test examiner demands cash merely to conduct the statutory test. Which "
            "corruption category best captures the relationship?"
        ),
        "group": "Corruption, empowerment, and constitutional morality",
    },
    {
        "label": "Collusive corruption",
        "statement": (
            "Collusive corruption occurs when giver and taker jointly gain at the cost of society, "
            "as in false certification, tax evasion, adulteration, or manipulated procurement; "
            "unlike coercive corruption, both parties have an incentive to conceal the transaction."
        ),
        "scenario_a": (
            "A contractor and an engineer agree to certify substandard rural road work so that "
            "both profit while villagers bear the damage. Which form of corruption is this?"
        ),
        "scenario_b": (
            "A restaurant owner pays an inspector to ignore adulteration. Why does calling the "
            "owner merely a helpless victim misdescribe the ethical structure?"
        ),
        "group": "Corruption, empowerment, and constitutional morality",
    },
    {
        "label": "Competition and discretion",
        "statement": (
            "Where monopoly and unreviewable discretion dominate, corruption risk rises; competition, "
            "choice, transparent processes, and automation can reduce opportunity for rent-seeking, "
            "though they do not eliminate the need for accountability and ethical judgment."
        ),
        "scenario_a": (
            "An applicant can obtain a certificate only from one opaque counter, whose clerk fixes "
            "informal priorities. Which structural combination creates the strongest rent-seeking risk?"
        ),
        "scenario_b": (
            "A state shifts routine licence renewal to a time-stamped portal with published criteria. "
            "Why is this a preventive ethics reform rather than simply a technology upgrade?"
        ),
        "group": "Corruption, empowerment, and constitutional morality",
    },
    {
        "label": "Citizen empowerment",
        "statement": (
            "Citizen empowerment through information, effective citizens' charters, stakeholder "
            "participation, public consultation, and social audit turns a passive recipient into "
            "a check on power; it is a structural response to unequal access and discretion."
        ),
        "scenario_a": (
            "MGNREGA workers publicly verify muster rolls and works before payment. Which corrective "
            "principle is operating beyond ordinary internal inspection?"
        ),
        "scenario_b": (
            "A hospital displays only a slogan about service but no timelines, grievance route, "
            "or information on entitlements. Why is this not an effective citizen charter?"
        ),
        "group": "Corruption, empowerment, and constitutional morality",
    },
    {
        "label": "Prevention and punishment",
        "statement": (
            "Ethically sound governance requires both preventive redesign and credible enforcement: "
            "transparency and reduced discretion lower opportunities for wrongdoing, while rule-of-law "
            "enforcement and deterrent punishment address violations that prevention does not avert."
        ),
        "scenario_a": (
            "A department digitises approvals but declines to investigate officials who manipulated "
            "legacy records. Which half of the anti-corruption response is missing?"
        ),
        "scenario_b": (
            "A department prosecutes bribe-takers but preserves an opaque, delay-prone licensing "
            "system. Why might misconduct recur despite strong punishment?"
        ),
        "group": "Corruption, empowerment, and constitutional morality",
    },
    {
        "label": "Constitutional morality",
        "statement": (
            "Constitutional morality is cultivated through civil education and adherence to the "
            "rule of law; for a public servant it requires fidelity to constitutional values, "
            "reasoned restraint of personal prejudice, fair procedure, and accountable exercise "
            "of public power."
        ),
        "scenario_a": (
            "A local majority demands that a district officer deny a lawful benefit to an unpopular "
            "minority. Which idea requires the officer to follow equal constitutional standards "
            "rather than social pressure?"
        ),
        "scenario_b": (
            "An officer says personal sympathy permits ignoring a hearing requirement. Why does "
            "constitutional morality connect good ends to lawful, accountable means?"
        ),
        "group": "Corruption, empowerment, and constitutional morality",
    },
    {
        "label": "CNP and integrity",
        "statement": (
            "Ethics and values enhance Comprehensive National Power by improving institutional "
            "trust, economic predictability, procurement integrity, social harmony, scientific "
            "credibility, and diplomatic reliability; they are capability multipliers rather than "
            "a substitute for material economic or strategic capacity."
        ),
        "scenario_a": (
            "A defence purchase favours the most suitable equipment through transparent evaluation "
            "instead of commissions. Which national-power pathway is strengthened, beyond an "
            "individual officer's honesty?"
        ),
        "scenario_b": (
            "A state claims that military spending alone establishes CNP while communal distrust "
            "undermines institutions. Which missing ethics-and-values dimension should an answer "
            "identify?"
        ),
        "group": "CNP, current anchor, and answer craft",
    },
    {
        "label": "CNP and social harmony",
        "statement": (
            "Social harmony is a direct ethics-and-values contribution to Comprehensive National "
            "Power because equal respect, constitutional conduct, and trusted institutions reduce "
            "internal fragmentation and make economic, strategic, and diplomatic capacities more durable."
        ),
        "scenario_a": (
            "A district administration applies relief criteria equally across caste and religion "
            "during a flood. How can this ethical conduct strengthen national capacity beyond "
            "immediate welfare delivery?"
        ),
        "scenario_b": (
            "A policy has impressive infrastructure targets but repeatedly treats vulnerable groups "
            "with contempt. Which CNP-related cost is likely to be overlooked?"
        ),
        "group": "CNP, current anchor, and answer craft",
    },
    {
        "label": "Mission Karmayogi",
        "statement": (
            "Mission Karmayogi frames capacity building around citizen-government interface and "
            "functional and behavioural competencies, shifting from a rules-based to a roles-based "
            "approach; ethical capacity therefore includes how public servants perform roles, not "
            "merely their knowledge of procedures."
        ),
        "scenario_a": (
            "A training programme teaches a revenue officer only forms and service rules, but not "
            "empathy, conflict handling, or accountability. Which competency gap is most relevant "
            "to the human interface?"
        ),
        "scenario_b": (
            "A department assigns a role solely by seniority despite a demonstrated mismatch in "
            "citizen-facing skills. How does a roles-based approach diagnose the problem?"
        ),
        "group": "CNP, current anchor, and answer craft",
    },
    {
        "label": "Answer architecture",
        "statement": (
            "A high-quality ethics answer should state a precise thesis, explain the mechanism "
            "through relevant dimensions, use a concrete Indian administrative illustration, "
            "acknowledge a real limitation or counterpoint, and end with a qualified reasoned verdict."
        ),
        "scenario_a": (
            "An answer says 'corruption is bad' and lists RTI, punishment, and values without "
            "explaining how they alter discretion or accountability. Which answer-writing defect "
            "most weakens it?"
        ),
        "scenario_b": (
            "A candidate praises decentralisation but notes the risk of local elite capture and "
            "adds audit safeguards. Why is this stronger than a one-sided conclusion?"
        ),
        "group": "CNP, current anchor, and answer craft",
    },
)

PYQS = (
    {
        "year": 2024,
        "question": (
            '"Ethics encompasses several key dimensions that are crucial in guiding individuals '
            'and organizations towards morally responsible behaviour." Explain the key dimensions '
            "of ethics that influence human actions. Discuss how these dimensions shape ethical "
            "decision&making in the professional context."
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: books/mains/05 UPSC 2024 "
            "Paper-IV_Final 1.pdf, Q1(b). The printed source uses 'decision&making'."
        ),
        "answer": (
            "Ethics supplies standards by which action is judged, not merely intentions by which "
            "an actor describes herself. Its important dimensions include duty and rights, "
            "consequences and harm, justice and fairness, virtues such as integrity and courage, "
            "care for affected persons, and accountability to the public. Together they make "
            "professional judgment reasoned rather than instinctive.\n\n"
            "In a professional setting, duty prevents an officer from treating a citizen as a "
            "means; consequence asks who may be harmed; fairness checks unequal treatment; virtue "
            "tests character under pressure; and accountability requires reasons capable of public "
            "scrutiny. For example, while finalising a beneficiary list, a district officer should "
            "apply published eligibility criteria, hear errors, protect personal data, and record "
            "reasons for inclusion or exclusion. Compassion may prompt assistance, but cannot "
            "justify secretly bypassing the list for a favoured applicant.\n\n"
            "No single dimension mechanically resolves every dilemma: rigid rule-following may "
            "ignore an exceptional hardship, while outcome-only reasoning can rationalise unfair "
            "means. Hence a public professional should balance legitimate consequences with "
            "constitutional duty, fair procedure, empathy, and review. The sound verdict is a "
            "decision that is both substantively humane and publicly defensible."
        ),
    },
    {
        "year": 2025,
        "question": (
            '"Constitutional morality is not a natural sentiment but a product of civil education '
            'and adherance of the rule of law." Examine the significance of constitutional morality '
            "for public servant highlighting the role in promoting good governance and ensuring "
            "accountability in public administration."
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: books/mains/UPSC Mains 2025 "
            "GS Paper 4.pdf, Q1(b). The printed source uses 'adherance'."
        ),
        "answer": (
            "Constitutional morality is disciplined fidelity to constitutional values and lawful "
            "procedure, rather than obedience to personal preference, social majority, or official "
            "convenience. Because it is learned through civic education and rule-of-law practice, "
            "it asks a public servant to convert equality, dignity, liberty, fairness, and "
            "accountability into everyday administrative conduct.\n\n"
            "It promotes good governance in three ways. First, it restrains arbitrary power: "
            "reasons, hearings, and published criteria prevent discretionary favour. Second, it "
            "protects minorities and vulnerable persons when local prejudice is politically "
            "popular. Third, it makes decisions auditable because the officer can state the "
            "constitutional value and rule supporting the action. A district magistrate allocating "
            "flood relief, for instance, must apply transparent need-based criteria across caste, "
            "religion, and political affiliation, record exclusions, and provide grievance review. "
            "This is not charity; it is equal public duty.\n\n"
            "Constitutional morality does not require mechanical rule worship. Exceptional "
            "circumstances may demand humane discretion, but discretion must remain reasoned, "
            "non-discriminatory, and reviewable. Thus it is the ethical bridge between legal "
            "authority and legitimate administration: it makes power citizen-centred while keeping "
            "it accountable."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Neutral rendering of the routed demand: Discuss the role of ethics and values in "
            "enhancing the three major components of Comprehensive National Power and social harmony."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand, neutral rendering from the Ethics Topic 01 PYQ integration; "
            "not claimed as verbatim wording in this data file."
        ),
        "answer": (
            "Comprehensive National Power (CNP) is not reducible to military assets. It rests on "
            "material capability, institutional capacity, social cohesion, technological credibility, "
            "and external trust. Ethics and values strengthen these components by making power "
            "reliable, legitimate, and sustainable.\n\n"
            "Economically, predictable rules, integrity, and low graft reduce uncertainty for "
            "citizens and investors. Strategically, ethical procurement and apolitical professional "
            "conduct help ensure that public money purchases capability rather than private "
            "commissions. Socially, equal respect, tolerance, and constitutional conduct reduce "
            "fragmentation and enable collective action. Technologically, research integrity and "
            "responsible data use sustain confidence in innovation. Diplomatically, a state that "
            "honours commitments and acts consistently accumulates credibility. India's "
            "post-liberalisation experience, noted by the 2nd ARC, illustrates the economic channel: "
            "reduced discretion and greater transparency can curb corruption in competitive sectors.\n\n"
            "Values alone cannot compensate for weak industry, defence preparedness, or state "
            "capacity; nor does social harmony arise from slogans. They need institutional expression "
            "through fair laws, transparent administration, and accountable leadership. Therefore "
            "ethics is not a decorative soft-power claim: it is a multiplier that enables economic, "
            "strategic, and social components of CNP to reinforce rather than undermine one another."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Neutral rendering of the routed demand: Examine education as a pervasive tool for "
            "individual development and social transformation, with reference to NEP 2020."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand, neutral rendering from the Ethics Topic 01 PYQ integration; "
            "not claimed as verbatim wording in this data file."
        ),
        "answer": (
            "Education is pervasive because it develops capability and also shapes the moral habits "
            "through which persons use capability. It can cultivate reasoning, empathy, scientific "
            "temper, constitutional values, and respect for diversity; hence its effects extend "
            "from individual agency to social institutions.\n\n"
            "For the individual, education enlarges informed choice, employability, self-respect, "
            "and the ability to question prejudice. For society, it can weaken inherited exclusion, "
            "support gender equality, foster civic participation, and create a workforce able to "
            "respond to changing public needs. In an Indian administrative illustration, a school "
            "that ensures girls' attendance, inclusive classroom practice, and grievance support "
            "does more than improve examination outcomes: it changes who can later participate in "
            "public and economic life. The ethical mechanism is civil education: repeated experience "
            "of equal treatment makes constitutional morality more practicable.\n\n"
            "Yet schooling is not automatically transformative. Poor quality, digital exclusion, "
            "segregated access, or rote moral instruction can reproduce hierarchy rather than "
            "challenge it. Education must therefore be accompanied by accessible institutions, "
            "fair opportunities, and accountable implementation. On balance, it is a powerful "
            "long-term instrument of transformation precisely when knowledge, values, and equal "
            "access are joined."
        ),
    },
    {
        "year": 2022,
        "question": (
            "Neutral rendering of the routed demand: Discuss ethics in human actions and its role "
            "in resolving conflicts in everyday functioning."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand, neutral rendering from the Ethics Topic 01 PYQ integration; "
            "not claimed as verbatim wording in this data file."
        ),
        "answer": (
            "Ethics in human action means selecting and justifying conduct through standards such "
            "as honesty, fairness, non-harm, empathy, duty, and accountability. It matters in "
            "everyday conflicts because disputes usually involve not only competing interests but "
            "also unequal power, incomplete information, and questions of respect.\n\n"
            "Ethical reasoning resolves conflict by first identifying stakeholders and facts, then "
            "separating entitlement from preference, hearing affected persons, testing foreseeable "
            "harm, and giving reasons that can be publicly defended. Consider a municipal officer "
            "facing competing claims over water-tanker supply in a drought. A first-come rule may "
            "appear neutral, but it can disadvantage settlements with poor transport or information. "
            "A fair response publishes need-based criteria, reserves an emergency channel for "
            "vulnerable households, records allocation, and provides a grievance route. This combines "
            "justice with compassion rather than choosing one against the other.\n\n"
            "Ethics cannot remove every scarcity conflict, and consensus may be impossible. An "
            "officer must still take a timely decision under law. Its value is that it converts "
            "power from personal preference into a transparent, reviewable process. Thus ethical "
            "action does not promise universal satisfaction; it produces a more legitimate and "
            "humane settlement."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Neutral rendering of the routed demand: Explain how a positive and a negative mindset "
            "can lead to different interpretations of rules and regulations."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand, neutral rendering from the Ethics Topic 01 PYQ integration; "
            "not claimed as verbatim wording in this data file."
        ),
        "answer": (
            "A mindset shapes how an official sees the purpose of a rule. A positive mindset "
            "treats regulation as an instrument to secure fairness, safety, and public trust; a "
            "negative mindset treats it chiefly as an obstacle, a source of power, or a shield "
            "against responsibility. The difference is ethical when interpretation affects citizens' "
            "rights and access.\n\n"
            "A constructive officer reads a rule with its public purpose, applies it consistently, "
            "and explains any refusal. A cynical officer may exploit ambiguity to delay service, "
            "demand informal payment, or deny reasonable assistance by saying 'the file cannot "
            "move.' For example, during disability-certificate verification, a facilitative officer "
            "helps an applicant correct a curable document error and records the reasoned decision; "
            "a negative one mechanically rejects the claim despite available verification and no "
            "risk to legality. The former respects both rule and citizen dignity.\n\n"
            "Positive interpretation is not permission to ignore mandatory conditions or grant "
            "favouritism. Compassion must operate within law, published criteria, and equal treatment. "
            "The sound administrative stance is therefore purposive but accountable: it avoids "
            "both obstructive literalism and arbitrary benevolence, and keeps the citizen-government "
            "interface lawful, responsive, and reviewable."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": "Distinguish ethics from morality. Why does the distinction matter to a public servant?",
        "answer": (
            "Ethics is the systematic, reasoned examination of standards of right conduct; morality "
            "is the set of beliefs and practices actually held by an individual or community. In "
            "ordinary speech the terms overlap, but the distinction matters because a popular "
            "practice need not be ethically justified.\n\n"
            "For a public servant, morality may explain why colleagues regard a festival gift, "
            "political recommendation, or preferential treatment as normal. Ethics asks a further "
            "question: is the conduct fair, compatible with public duty, non-harmful, and capable "
            "of being publicly defended? A revenue officer cannot justify giving a relative's "
            "mutation file priority merely because family loyalty is socially valued. Public office "
            "requires impartiality, reasons, and equal access.\n\n"
            "The distinction must not produce contempt for community values. Local knowledge can "
            "reveal genuine hardship and guide humane service delivery. But where custom conflicts "
            "with constitutional equality or public trust, the officer must use ethical reasoning "
            "and lawful procedure. Thus the public servant should respect moral diversity while "
            "testing conduct against principled, citizen-facing standards."
        ),
    },
    {
        "marks": 10,
        "question": "Why is conduct that is legal not necessarily proper in public office? Illustrate.",
        "answer": (
            "Legality means conformity with enacted law; propriety asks whether conduct is "
            "appropriate to the responsibilities and appearance of public office. The gap matters "
            "because rules cannot enumerate every conflict, and public trust can be damaged before "
            "a legal violation is proved.\n\n"
            "For example, a district procurement officer may legally attend a private dinner hosted "
            "by a bidder if no payment or formal favour is established. Yet the event can create a "
            "reasonable apprehension of bias and compromise the officer's independence. The prudent "
            "response is disclosure, recusal where necessary, and avoidance of hospitality that a "
            "citizen could fairly see as influencing a decision. Similar reasoning applies to "
            "informal meetings, use of official information, and public praise for connected firms.\n\n"
            "Propriety should not become vague moral policing or a device to punish harmless personal "
            "conduct. It requires a nexus with office, public perception, and entrusted power. "
            "Accordingly, legal compliance is the floor, not the ceiling: ethical administration "
            "also protects impartiality and the visible integrity of decision-making."
        ),
    },
    {
        "marks": 15,
        "question": "Evaluate the claim that corruption is structurally produced rather than merely a failure of character.",
        "answer": (
            "Corruption is partly a failure of character, but it is often structurally enabled. "
            "The 2nd ARC connects risk to public authority, discretion, control of funds, asymmetric "
            "power, historical habits of unchallenged authority, over-regulation, and excessive "
            "centralisation. These conditions shape temptations and the citizen's capacity to resist.\n\n"
            "A character-only explanation recommends moral education. It is necessary because "
            "integrity, empathy, and courage influence conduct under pressure. Yet it cannot explain "
            "why corruption falls when opaque intermediaries are removed without a change in personal "
            "virtue. The ARC's observation that competition and transparency reduced corruption in "
            "sectors after liberalisation supports institutional reasoning. In land administration, "
            "time-stamped digital records, published fees, and appeal routes can reduce a clerk's "
            "scope to demand speed money from a vulnerable applicant.\n\n"
            "Structural reform also has limits. Automation can exclude digitally weak citizens, "
            "decentralisation can create local monopolies, and corruption can migrate to discretionary "
            "areas if political incentives remain distorted. Hence the false choice must be rejected. "
            "The defensible remedy combines values-based leadership, transparent design, citizen "
            "empowerment, independent audit, and deterrent enforcement. Character makes integrity "
            "possible; institutions make it durable and verifiable. Recruitment, supervision, and "
            "public review must reinforce the same incentive for ethical conduct."
        ),
    },
    {
        "marks": 15,
        "question": "Distinguish coercive from collusive corruption and draw out the implications for ethical response.",
        "answer": (
            "Coercive corruption occurs when a public functionary extracts payment for a service "
            "to which the citizen is entitled; the citizen is an unwilling victim. Collusive "
            "corruption occurs when giver and taker jointly secure private gain while society bears "
            "the loss. The distinction changes both diagnosis and remedy.\n\n"
            "A clerk demanding money to release a sanctioned pension exemplifies coercion: the "
            "widow seeks no improper advantage and is constrained by need and delay. In contrast, "
            "an engineer and contractor jointly certifying substandard road work exemplify collusion: "
            "both gain, while taxpayers and villagers lose quality and safety. Coercion requires "
            "safe complaint channels, time-bound service guarantees, fee transparency, and protection "
            "for the victim. Collusion requires procurement transparency, technical audit, asset and "
            "beneficial-interest scrutiny, whistle-blower protection, and investigation of both "
            "sides of the bargain.\n\n"
            "In practice, categories can blur: a business may initially face coercion yet later "
            "seek an illegal advantage. Therefore labels must follow facts, not stereotypes about "
            "bribe-givers. The ethical verdict is that reform must reduce discretionary extraction "
            "while also disrupting mutually beneficial networks that damage the public interest. "
            "Training should make officers recognise the distinction before they choose a complaint, "
            "audit, investigation, or victim-support response."
        ),
    },
    {
        "marks": 20,
        "question": "Citizen empowerment is not a welfare add-on but an ethical redesign of the human interface. Discuss.",
        "answer": (
            "Citizen empowerment is an ethical redesign because it changes the relationship between "
            "the holder of public power and the person dependent on it. At the human interface, "
            "officials may control information, time, certification, and access. Where a poor or "
            "unorganised citizen cannot question those controls, formal entitlement can become "
            "dependence and discretion can become extraction.\n\n"
            "The 2nd ARC identifies Right to Information, effective citizens' charters, stakeholder "
            "involvement, public consultation, and social auditing as correctives. RTI reduces "
            "informational monopoly; a meaningful charter states service, fee, timeline, officer, "
            "and grievance route; consultation gives affected persons voice before a decision; and "
            "social audit lets beneficiaries test official records against lived reality. In an "
            "Indian rural works programme, public verification of muster rolls and completed assets "
            "can expose false entries that a closed departmental file may conceal. Such tools promote "
            "dignity, accountability, and substantive equality, not merely administrative efficiency.\n\n"
            "Empowerment has conditions. A portal without assisted access can deepen exclusion; "
            "social audit can be captured by local elites; information without response can create "
            "frustration. It must therefore be paired with literacy support, accessible formats, "
            "independent grievance handling, protection against retaliation, and enforceable follow-up. "
            "Punishment for proved misconduct remains necessary.\n\n"
            "Thus citizen empowerment does not replace honest officials or rule enforcement. It "
            "makes integrity less dependent on individual goodwill by giving citizens information, "
            "voice, and remedy. Its ethical achievement is to convert the citizen from supplicant "
            "to rights-bearing participant in accountable governance. It thereby improves both "
            "the fairness of outcomes and the legitimacy of the procedure that produces them in "
            "ordinary encounters with the state."
        ),
    },
    {
        "marks": 20,
        "question": "How can constitutional morality and role-based civil-service capacity together improve the ethical quality of public administration?",
        "answer": (
            "Constitutional morality supplies the normative compass of public administration; "
            "role-based capacity supplies the ability to practise it at the citizen-government "
            "interface. The first requires fidelity to equality, dignity, liberty, fair procedure, "
            "and accountable power even when prejudice or convenience points elsewhere. The second "
            "recognises that ethical administration depends on functional and behavioural competence, "
            "not rules memorised in isolation.\n\n"
            "A constitutional public servant gives reasons, avoids discrimination, hears affected "
            "persons, and keeps discretion reviewable. Mission Karmayogi's National Programme for "
            "Civil Services Capacity Building is relevant because the DoPT describes its focus on "
            "the citizen-government interface, functional and behavioural competencies, and a "
            "rules-based to roles-based shift. A welfare officer handling disability benefits, for "
            "example, needs procedural knowledge, data discipline, empathy, communication, and the "
            "courage to resist a politically favoured but ineligible claim. Capacity without "
            "constitutional morality can become efficient exclusion; morality without capability "
            "can remain an aspiration unable to deliver timely justice.\n\n"
            "Training alone cannot cure opaque systems, perverse incentives, or political pressure. "
            "It must be supported by transparent criteria, audit trails, grievance redress, "
            "leadership example, and proportionate enforcement. Nor should roles-based management "
            "be misread as discretion to ignore service safeguards.\n\n"
            "The reasoned conclusion is that constitutional morality determines the public purpose "
            "of administrative power, while role-based capacity operationalises it. Their union "
            "produces not merely compliant officials but competent, humane, and accountable public "
            "institutions. Performance assessment should therefore examine citizen-facing conduct "
            "and reasoned outcomes, not only course completion or mechanical target achievement. "
            "Feedback, grievance data, and reasoned review should inform improvement without "
            "turning complex ethical service into a crude numerical score alone."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": SESSION_TITLES[0],
        "structural_type": "concept ladder",
        "nodes": (
            "Ethics begins where conduct affects another person or public trust.",
            "Ethics derives from ethikos and points to standards practised as habits.",
            "Society places standards on itself to guide choices and actions.",
            "Values orient conduct before a rule is consulted.",
            "Public duty tests values when authority meets citizen need.",
            "Private interest can distort judgment at this point of contact.",
            "Integrity joins declared standards to actual conduct under pressure.",
            "Corruption is a major manifestation of ethical failure.",
        ),
        "verdict": "Ethics is lived standards, not merely admirable language.",
        "answer_use": "Open with ethics as standards guiding conduct, then locate the public interface.",
    },
    {
        "title": SESSION_TITLES[1],
        "structural_type": "four-level inquiry grid",
        "nodes": (
            "Descriptive ethics records what a group actually believes or does.",
            "Normative ethics asks what a person ought to do and why.",
            "Meta-ethics tests the meaning and truth-status of moral language.",
            "Applied ethics brings normative standards to a specific professional field.",
            "A survey on gift-taking is descriptive rather than justificatory.",
            "A duty or consequence argument is normative rather than descriptive.",
            "A debate over the meaning of wrong is meta-ethical rather than applied.",
            "GS-IV primarily rewards normative and applied ethical reasoning.",
        ),
        "verdict": "Do not confuse a social fact with an ethical justification.",
        "answer_use": "Name the inquiry level before applying a standard to an administrative case.",
    },
    {
        "title": SESSION_TITLES[2],
        "structural_type": "three-test comparison",
        "nodes": (
            "Legality asks whether enacted law has been followed.",
            "Morality asks whether conduct meets a standard of right action.",
            "Propriety asks whether conduct suits the office and occasion.",
            "Legal conduct can still undermine impartiality or public confidence.",
            "A lavish dinner from a bidder can fail propriety without a proven bribe.",
            "The letter of a rule cannot exhaust every conflict of interest.",
            "The spirit of public duty requires visible as well as actual integrity.",
            "A reasoned officer records and manages appearance-based conflicts.",
        ),
        "verdict": "Legal compliance is the floor; propriety protects the credibility of office.",
        "answer_use": "Use the bidder-dinner example to explain why legality is not the whole ethical test.",
    },
    {
        "title": SESSION_TITLES[3],
        "structural_type": "interface flow",
        "nodes": (
            "Human interface is where public duty meets a citizen's concrete need.",
            "The interface becomes ethically charged when private interest enters judgment.",
            "Discretion lets an official shape access, timing, or certification.",
            "Vulnerability makes delay and information asymmetry more damaging.",
            "A pension counter can turn entitlement into dependence through discretion.",
            "Clear criteria reduce scope for personal preference at the interface.",
            "Automation can reduce arbitrary contact when it retains appeal and access.",
            "Ethical service is timely, respectful, equal, and reviewable.",
        ),
        "verdict": "The ordinary service counter is a central site of public ethics.",
        "answer_use": "Ground abstraction in an Indian service-delivery encounter.",
    },
    {
        "title": SESSION_TITLES[4],
        "structural_type": "two-pillar synthesis",
        "nodes": (
            "Values give officials an internal reason to act with integrity.",
            "Institutions give values procedures, supervision, and consequences.",
            "Moral education alone leaves temptation-producing systems untouched.",
            "Punishment alone ignores culture, incentives, and ethical judgment.",
            "Transparent criteria make fair conduct easier to verify.",
            "Competent disciplinary machinery gives violations credible consequences.",
            "Audit trails make discretionary acts accountable to evidence.",
            "Durable integrity requires values contained within institutions.",
        ),
        "verdict": "Values and institutions are complementary, not rival explanations.",
        "answer_use": "Use the synthesis to answer causes and remedies together.",
    },
    {
        "title": SESSION_TITLES[5],
        "structural_type": "causal chain",
        "nodes": (
            "Colonial habits normalised unchallenged official authority.",
            "Asymmetric power weakens citizen pressure for ethical conduct.",
            "Over-regulation made citizens dependent on official discretion.",
            "Monopoly and opacity increase opportunities for rent-seeking.",
            "Over-centralisation lengthens the path from authority to accountability.",
            "Competition and choice can reduce discretion-based corruption.",
            "Transparency and automation can narrow the scope for concealed bargains.",
            "Political incentives can displace corruption into protected sectors.",
        ),
        "verdict": "Corruption is often produced by incentives and power structures.",
        "answer_use": "Explain mechanism before prescribing transparency, competition, or decentralisation.",
    },
    {
        "title": SESSION_TITLES[6],
        "structural_type": "contrast matrix",
        "nodes": (
            "Coercive corruption extracts payment for an entitled public service.",
            "The coerced citizen is an unwilling victim of official power.",
            "Collusive corruption gives private gain to both giver and taker.",
            "Society bears the cost of collusion through loss, danger, or unfairness.",
            "A delayed pension for speed money is coercive corruption.",
            "False road certification by engineer and contractor is collusive corruption.",
            "Victim-safe complaints are essential against coercive extraction.",
            "Audit and investigation of networks are essential against collusion.",
        ),
        "verdict": "Classify the relationship before choosing an anti-corruption response.",
        "answer_use": "Contrast victim protection with network disruption in one compact paragraph.",
    },
    {
        "title": SESSION_TITLES[7],
        "structural_type": "empowerment loop",
        "nodes": (
            "Information corrects the citizen's knowledge disadvantage.",
            "A meaningful charter states service, fee, time, officer, and remedy.",
            "Stakeholder participation gives affected persons voice before decisions.",
            "Public consultation makes policy reasons contestable.",
            "Social audit tests official records against community experience.",
            "RTI can expose unexplained delay and hidden decision grounds.",
            "Assisted access prevents digital systems from reproducing exclusion.",
            "Rule-of-law enforcement remains necessary after prevention fails.",
        ),
        "verdict": "Empowerment turns the citizen from supplicant into an accountability actor.",
        "answer_use": "Link each tool to the asymmetry of power it corrects.",
    },
    {
        "title": SESSION_TITLES[8],
        "structural_type": "constitutional capacity bridge",
        "nodes": (
            "Constitutional morality is cultivated rather than naturally inherited.",
            "Civil education develops respect for constitutional values.",
            "Rule-of-law practice disciplines personal prejudice and arbitrary power.",
            "Equality and dignity guide treatment of unpopular minorities.",
            "Fair procedure makes administrative reasons visible and contestable.",
            "Ethical governance improves trust and social harmony.",
            "Integrity strengthens economic, strategic, scientific, and diplomatic capacity.",
            "CNP needs material capacity but values make it credible and durable.",
        ),
        "verdict": "Constitutional morality converts public power into legitimate authority.",
        "answer_use": "Connect constitutional values to good governance, accountability, and social cohesion.",
    },
    {
        "title": SESSION_TITLES[9],
        "structural_type": "answer spine",
        "nodes": (
            "Define the ethical concept with a clear boundary.",
            "State a thesis that answers the directive rather than repeats it.",
            "Explain two or three mechanisms that make the thesis true.",
            "Use one named Indian administrative illustration.",
            "Distinguish related concepts before comparing them.",
            "Test the institutional and value dimensions together.",
            "Add one genuine limitation or counterpoint.",
            "Conclude with a qualified, implementable verdict.",
        ),
        "verdict": "A GS-IV answer earns depth through mechanism and qualification.",
        "answer_use": "Use this sequence for 10, 15, and 20-mark theory answers.",
    },
    {
        "title": "MCQ and trap repair",
        "structural_type": "close-option repair grid",
        "nodes": (
            "Ethics and morality are related but not technically identical.",
            "Descriptive evidence does not itself prove a normative conclusion.",
            "Meta-ethics is not the same as applied ethical decision-making.",
            "Legal conduct can fail propriety at a public office.",
            "Coercive corruption has an unwilling victim seeking an entitlement.",
            "Collusive corruption creates shared private benefit and public loss.",
            "Decentralisation needs audit and capacity to avoid local capture.",
            "Technology reduces discretion only when access and appeals remain real.",
        ),
        "verdict": "Identify the decisive threshold, not the familiar word, in close options.",
        "answer_use": "Repair common confusions before attempting statement-based questions.",
    },
    {
        "title": "PYQ and answer synthesis",
        "structural_type": "exam synthesis rail",
        "nodes": (
            "The 2024 routed theme tests dimensions shaping professional ethical decisions.",
            "The 2025 official question tests constitutional morality in public service.",
            "CNP answers need economic, strategic, social, and credibility mechanisms.",
            "Human-interface answers need a concrete citizen-official encounter.",
            "Corruption answers need values-plus-institutions rather than one cause.",
            "Citizen-empowerment answers need information, voice, remedy, and enforcement.",
            "A limitation prevents a formulaic and one-sided conclusion.",
            "A verdict must state the safeguard that makes reform ethically durable.",
        ),
        "verdict": "Translate every PYQ into a thesis, mechanism, illustration, limitation, and verdict.",
        "answer_use": "Use this rail as the final revision checklist before a GS-IV response.",
    },
)

CURRENT_ANCHOR = (
    "The DoPT NPCSCB Mission Karmayogi page states that the programme targets the "
    "citizen-government interface, functional and behavioural competencies, and a "
    "rules-based to roles-based shift. It describes six pillars, including iGOT-Karmayogi, "
    "and an intended scale of 2 crore users. A PIB release dated 6 February 2026 reports "
    "1.49 crore users, 4,342 courses, 7.26 crore completions, and 23 languages; these are "
    "dated figures, not an undated programme total."
)

CURRENT_SOURCE_URLS = (
    "https://dopt.gov.in/schemes/national-programme-civil-services-and-capacity-building-npcscb-mission-karmayogi",
    "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2226246&reg=3&lang=1",
)

SOURCE_CAVEAT = (
    "Core theory is grounded in the specified Ethics Basic and Advanced owners, the official "
    "syllabus mapping, and locally held PDFs. The 2024 and 2025 PYQ strings preserve the "
    "English wording printed in the local PDFs, including their printed spellings. Older PYQ "
    "demands are explicitly neutral renderings from the local routed-demand ledger, not claims "
    "of verbatim official wording. ARC's 2007 labour-sector figures are historical framing and "
    "must not be represented as current statistics. The Mission Karmayogi figures are dated "
    "6 February 2026 PIB figures."
)

REGISTER_SUPPLEMENT = """
## Ethics and Human Interface: Rapid Register Supplement

- Ethics is a set of standards society places on itself; ethics needs practice, integrity culture,
  sanctions, and competent disciplinary machinery.
- Ethics is systematic reasoning about right conduct; morality is lived belief and practice.
- Four levels: descriptive (what is), normative (what ought to be), meta-ethical (what moral
  language means), and applied (what a field should do). GS-IV mainly needs normative plus applied.
- Human interface: public duty, citizen need, private interest, discretion, and vulnerability meet.
- Legality, morality, and propriety are separate tests. Legal is not always proper.
- Public office combines authority, discretion, and public money; that bundle creates temptation.
- ARC rejects one-cause stories: values matter, but institutions contain and verify values.
- Structural causes: colonial authority, asymmetric power, over-regulation, monopoly, opacity, and
  over-centralisation. Competition, transparency, and citizen empowerment are correctives.
- Coercive corruption: extraction for an entitlement; protect the unwilling citizen-victim.
- Collusive corruption: giver and taker both gain while society loses; audit the network and outcome.
- Citizen empowerment means RTI, meaningful charters, participation, consultation, social audit,
  grievance remedies, and accessible information; prevention must be joined to enforcement.
- Constitutional morality is cultivated through civil education and adherence to the rule of law.
  It demands equality, dignity, fair procedure, reasons, and accountable discretion.
- CNP is strengthened when integrity improves economic predictability, procurement quality, social
  harmony, scientific credibility, and diplomatic trust; ethics does not replace material capacity.
- Mission Karmayogi link: citizen-government interface, functional and behavioural competencies,
  rules-based to roles-based shift, six pillars including iGOT-Karmayogi, and intended 2 crore scale.

### Answer spine

```text
DEFINE THE CONCEPT
        |
        v
STATE THE THESIS
        |
        v
EXPLAIN THE MECHANISM -> values + institutions -> Indian illustration
        |
        v
ADD THE LIMIT -> access, capture, opacity, political incentives, or enforcement gap
        |
        v
GIVE A QUALIFIED VERDICT -> ethical, lawful, citizen-centred, and reviewable
```
""".strip()
