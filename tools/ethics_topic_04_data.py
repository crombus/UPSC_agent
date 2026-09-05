"""Learner-v2 source data: Ethics Topic 04, Aptitude and Foundational Values for Civil Service."""

SESSION_TITLES = (
    "What aptitude means and why it is not attitude or value",
    "Integrity: the hardest test is when no one is watching",
    "Impartiality and non-partisanship under real pressure",
    "Objectivity and dedication to public service",
    "Empathy, sympathy and compassion: from feeling to service design",
    "Tolerance and constitutional morality",
    "Institutional architecture: Mission Karmayogi and tenure safeguards",
    "How foundational values interact under administrative pressure",
    "Enabler versus regulator: calibrating facilitation and oversight",
    "Writing foundational-values answers that earn GS-IV marks",
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
    ("10", "11", "12", "13"),
)

MCQ_ITEMS = (
    # --- Group: aptitude-attitude-value taxonomy ---
    {
        "label": "Aptitude is a trainable capacity",
        "statement": (
            "Aptitude is a natural or cultivable capacity to perform a task or role competently; "
            "it is not a fixed personality trait but can be developed through deliberate practice, "
            "foundation courses and competency-based training such as Mission Karmayogi."
        ),
        "scenario_a": (
            "A probationer initially struggles with citizen grievance handling but improves "
            "after structured mentoring and community immersion. Which concept best describes "
            "her growing capacity to serve effectively?"
        ),
        "scenario_b": (
            "A selection board assumes that aptitude for public service is entirely innate and "
            "cannot be improved by training. Which contemporary civil-service pedagogy challenges "
            "that assumption?"
        ),
        "group": "aptitude-attitude-value taxonomy",
    },
    {
        "label": "Aptitude differs from attitude and value",
        "statement": (
            "Aptitude denotes capacity to perform, attitude denotes an evaluative stance toward "
            "a specific object, and value denotes a general cross-situational standard of what is "
            "worth pursuing; confusing the three weakens any answer on civil-service assessment."
        ),
        "scenario_a": (
            "A district collector has the skill to manage flood relief efficiently but privately "
            "resents the posting. Which of the three concepts describes his competence and which "
            "describes his evaluative stance?"
        ),
        "scenario_b": (
            "A trainee says integrity is an attitude she holds toward her department. Why is "
            "it more precise to classify integrity as a value rather than an object-specific "
            "evaluation?"
        ),
        "group": "aptitude-attitude-value taxonomy",
    },
    {
        "label": "Aptitude is tested in combination under pressure",
        "statement": (
            "The GS-IV syllabus lists foundational values as though independent, but Mains "
            "questions usually test them in combination; a welfare-scheme dilemma may require "
            "impartiality and compassion together rather than either one alone."
        ),
        "scenario_a": (
            "A block officer must decide whether to relax documentation for elderly pension "
            "applicants in a remote tribal area while maintaining transparent eligibility criteria. "
            "Which two foundational values are being tested simultaneously?"
        ),
        "scenario_b": (
            "A candidate writes an answer treating each value in isolation, defining each without "
            "showing how they interact. Why does the examiner find the response inadequate for a "
            "pressure-based question?"
        ),
        "group": "aptitude-attitude-value taxonomy",
    },
    {
        "label": "Foundational values are operational commitments",
        "statement": (
            "Each foundational value in the GS-IV syllabus is exam-credible only when paired "
            "with a specific institutional test and safeguard; advanced answers must show the "
            "value surviving a realistic pressure scenario rather than merely define it."
        ),
        "scenario_a": (
            "A revenue officer describes integrity as important but cannot name any institutional "
            "mechanism that monitors it. Why does her answer lack the operational element that "
            "the examiner expects?"
        ),
        "scenario_b": (
            "A district administration pairs an integrity pledge with random asset inspections, "
            "audit trails and conflict-of-interest disclosures. Which feature converts the value "
            "from an aspiration into an observable administrative commitment?"
        ),
        "group": "aptitude-attitude-value taxonomy",
    },
    # --- Group: integrity and honesty ---
    {
        "label": "Integrity is not the same as honesty",
        "statement": (
            "Honesty is truthful communication in a given instance, while integrity is the "
            "consistency of one's values across situations including when unobserved; the Nolan "
            "Committee treats them as related but separate principles of public life."
        ),
        "scenario_a": (
            "A procurement officer truthfully answers a direct audit query but routinely allows "
            "a favoured contractor to bypass published criteria when no auditor is present. "
            "Which principle is satisfied and which is violated?"
        ),
        "scenario_b": (
            "A colleague says honesty and integrity are identical because both concern truth. "
            "Which Nolan-based distinction shows why this conflation is inaccurate for a "
            "civil-service ethics answer?"
        ),
        "group": "integrity and honesty",
    },
    {
        "label": "Integrity is tested by discretion and secrecy",
        "statement": (
            "Integrity is asymmetrically tested: it is nearly costless to display when observed "
            "and only genuinely tested when discretion, secrecy and personal gain are simultaneously "
            "present; institutional responses convert this unobservable trait into partially "
            "observable behaviour through asset declarations and random inspections."
        ),
        "scenario_a": (
            "A licensing officer handles applications transparently during departmental reviews "
            "but expedites files for relatives when supervisors are transferred. Which feature "
            "of integrity testing explains why normal compliance missed the failure?"
        ),
        "scenario_b": (
            "A state government mandates annual asset declarations and cooling-off periods for "
            "retiring officials joining private firms. Which analytical logic justifies these "
            "measures as proxies for an otherwise unobservable quality?"
        ),
        "group": "integrity and honesty",
    },
    {
        "label": "Buffett's integrity-intelligence-energy hierarchy",
        "statement": (
            "The proposition that integrity, intelligence and energy are three hiring qualities "
            "and that without the first the other two will harm rather than help was endorsed by "
            "Warren Buffett; intelligence and energy amplify whatever the underlying disposition "
            "already is, making integrity the precondition."
        ),
        "scenario_a": (
            "A highly intelligent and energetic tax officer uses her skills to construct elaborate "
            "schemes that conceal favouritism toward a politically connected firm. Which element "
            "of the hiring proposition does this illustrate?"
        ),
        "scenario_b": (
            "A recruitment panel tests aptitude and drive extensively but has no mechanism to "
            "assess integrity at entry. Why does the proposition suggest that continuous "
            "institutional safeguards are needed throughout a career?"
        ),
        "group": "integrity and honesty",
    },
    {
        "label": "Buffett attribution requires care",
        "statement": (
            "Buffett himself introduces the integrity-intelligence-energy line as something "
            "somebody once said; its traceable published form is a 1994 Omaha World-Herald "
            "report of his 1993 Columbia Business School remarks, so it should be treated as "
            "a widely endorsed teaching rather than an originally coined aphorism."
        ),
        "scenario_a": (
            "A candidate writes that Buffett personally invented the three-quality framework "
            "and cites it as a proven management theorem. Which provenance correction preserves "
            "exam utility without fabricating a primary source?"
        ),
        "scenario_b": (
            "An ethics training module uses the proposition to discuss why integrity cannot be "
            "tested at entry alone, while noting the attribution caveat. Why is this a more "
            "responsible use than treating popular wording as settled scholarship?"
        ),
        "group": "integrity and honesty",
    },
    # --- Group: impartiality and non-partisanship ---
    {
        "label": "Impartiality is not identical treatment",
        "statement": (
            "Impartiality requires deciding without personal bias on transparent, rule-based "
            "merit or criteria; it does not require identical treatment regardless of need, "
            "because targeted needs-based support for weaker sections is impartial when applied "
            "consistently to all similarly situated persons."
        ),
        "scenario_a": (
            "A sub-divisional magistrate waives documentation fees for below-poverty-line "
            "applicants under a published government order while charging standard fees to "
            "others. A petitioner claims this violates impartiality. Which distinction resolves "
            "the complaint?"
        ),
        "scenario_b": (
            "A welfare office informally fast-tracks a file because the applicant is the "
            "officer's relative, not because any published criterion applies. Why does the same "
            "action that is impartial under transparent rules become nepotism under informal "
            "selection?"
        ),
        "group": "impartiality and non-partisanship",
    },
    {
        "label": "Non-partisanship under political pressure",
        "statement": (
            "Non-partisanship means a civil servant serves the government of the day loyally "
            "without allowing party political considerations to shape official advice or action; "
            "personal political views are permitted but official conduct must remain party-neutral."
        ),
        "scenario_a": (
            "A returning officer during state assembly elections applies identical scrutiny to "
            "nomination papers of ruling-party and opposition candidates despite phone calls "
            "from a minister. Which foundational value is she exercising under real pressure?"
        ),
        "scenario_b": (
            "A colleague argues that non-partisanship requires a civil servant to have no "
            "political opinions whatsoever. Which clarification distinguishes personal belief "
            "from official conduct?"
        ),
        "group": "impartiality and non-partisanship",
    },
    {
        "label": "Transfer is the structural threat to non-partisanship",
        "statement": (
            "The ARC documents the transfer as the politicians' basic weapon of control over "
            "the bureaucracy, citing Robert Wade's study of Andhra Pradesh; non-partisanship "
            "is structurally difficult to sustain without tenure and transfer protection such "
            "as Civil Services Board mechanisms."
        ),
        "scenario_a": (
            "A district education officer who resists politically motivated teacher transfers "
            "is herself transferred to a remote posting within weeks. Which structural factor "
            "identified by the ARC explains why her non-partisanship was unsustainable?"
        ),
        "scenario_b": (
            "A state constitutes a Civil Services Board to review transfer recommendations "
            "against published criteria before they take effect. Which institutional gap in "
            "non-partisanship protection is this mechanism designed to close?"
        ),
        "group": "impartiality and non-partisanship",
    },
    {
        "label": "Non-partisanship is an institutional-design problem",
        "statement": (
            "No amount of individual training fully substitutes for institutional safeguards "
            "against discretionary transfer power; non-partisanship is therefore an "
            "institutional-design issue as much as a personal virtue, which elevates it from "
            "character advice to structural reform."
        ),
        "scenario_a": (
            "A state invests heavily in ethics training for officers but retains the power to "
            "transfer any official without recorded reasons. Why might non-partisan conduct "
            "still collapse under political transition despite the training?"
        ),
        "scenario_b": (
            "A reform proposal combines fixed three-year tenure, transparent transfer criteria "
            "and a review board with ethics sensitisation modules. Why is this more durable "
            "than either training or tenure protection alone?"
        ),
        "group": "impartiality and non-partisanship",
    },
    # --- Group: objectivity, dedication and enabler-regulator ---
    {
        "label": "Objectivity means evidence-based judgment",
        "statement": (
            "Objectivity requires evidence-based and rule-bound judgment free of personal "
            "preconception; it is supported by reasoned written orders, appeal mechanisms and "
            "transparent decision criteria that make official reasoning reviewable."
        ),
        "scenario_a": (
            "A food safety inspector issues closure orders based on published contamination "
            "thresholds and recorded lab results, giving the establishment a hearing before "
            "the order takes effect. Which foundational value is most directly demonstrated?"
        ),
        "scenario_b": (
            "An officer rejects a mining application because the applicant belongs to a "
            "community she personally dislikes, without recording evidence-based reasons. "
            "Which foundational value has been violated despite the apparently protective outcome?"
        ),
        "group": "objectivity, dedication and enabler-regulator",
    },
    {
        "label": "Dedication exceeds minimum compliance",
        "statement": (
            "Dedication to public service is motivation that exceeds minimum compliance and "
            "is visible in responsiveness, initiative and proactive problem-solving; it is now "
            "measured by outcomes enabled rather than only rules enforced."
        ),
        "scenario_a": (
            "A taluk officer identifies that elderly pensioners cannot travel to the tehsil "
            "office and arranges monthly doorstep verification camps without being ordered to "
            "do so. Which foundational value distinguishes this initiative from routine rule "
            "following?"
        ),
        "scenario_b": (
            "A department meets every procedural deadline but citizens still cannot access "
            "services because the forms are available only in English in a predominantly "
            "Hindi-speaking district. Which gap between compliance and dedication does this "
            "reveal?"
        ),
        "group": "objectivity, dedication and enabler-regulator",
    },
    {
        "label": "Enabler versus regulator requires calibration",
        "statement": (
            "The civil servant as enabler and active facilitator of growth rather than a "
            "regulator is not a call to abandon regulation but to sequence and calibrate it: "
            "pre-clearance single-window facilitation for legitimate activity combined with "
            "post-facto risk-based regulatory scrutiny."
        ),
        "scenario_a": (
            "A district industrial officer replaces seven separate pre-clearances with a "
            "single-window approval for low-risk enterprises while retaining random post-"
            "approval safety inspections. Which calibration principle is being applied?"
        ),
        "scenario_b": (
            "A state abolishes all environmental inspections for new factories in the name of "
            "facilitation. A chemical leak harms nearby residents within months. Which dimension "
            "of the enabler-regulator proposition was ignored?"
        ),
        "group": "objectivity, dedication and enabler-regulator",
    },
    {
        "label": "Facilitation without safeguards risks capture",
        "statement": (
            "Excessive enabling without regulatory safeguards risks regulatory capture, while "
            "excessive regulating without enabling stifles legitimate development; the enabler-"
            "regulator calibration requires reliable risk-based information systems to avoid "
            "under-regulation by omission."
        ),
        "scenario_a": (
            "A mining department fast-tracks all clearances without environmental impact "
            "assessments, and a politically connected firm exploits the gap. Which institutional "
            "failure does the capture risk describe?"
        ),
        "scenario_b": (
            "A cottage-industry applicant faces the same inspection regime as a large chemical "
            "plant, causing a two-year delay. Which side of the calibration spectrum has the "
            "administration defaulted to?"
        ),
        "group": "objectivity, dedication and enabler-regulator",
    },
    # --- Group: empathy, sympathy and compassion ---
    {
        "label": "Empathy is cognitive and affective perspective-taking",
        "statement": (
            "Empathy is accurately grasping another person's situation and feelings from their "
            "frame of reference through both cognitive and affective perspective-taking; it "
            "differs from sympathy, which feels for someone from the outside with an implicit "
            "hierarchy between giver and receiver."
        ),
        "scenario_a": (
            "A disaster-relief officer sits with displaced families, listens to their accounts "
            "of loss and adjusts the relief process to address specific needs they describe. "
            "Which concept best captures her active effort to understand their perspective?"
        ),
        "scenario_b": (
            "A senior official expresses sorrow for flood victims on social media but does not "
            "consult them before designing the rehabilitation plan. Which concept describes his "
            "response and what is missing?"
        ),
        "group": "empathy, sympathy and compassion",
    },
    {
        "label": "Compassion requires motivated action",
        "statement": (
            "Compassion is empathy plus a motivated commitment to relieve suffering; it "
            "necessarily issues in action or service design and is therefore the only form "
            "among empathy, sympathy and compassion that is administratively assessable."
        ),
        "scenario_a": (
            "A tehsildar redesigns the pension verification process to allow video calls "
            "instead of mandatory in-person appearance for elderly and disabled beneficiaries. "
            "Which concept is operationalised through this specific process change?"
        ),
        "scenario_b": (
            "An officer deeply understands the hardship of migrant workers but takes no step "
            "to simplify registration or provide multilingual service access. Why does the "
            "officer's response fall short of the concept that earns GS-IV marks?"
        ),
        "group": "empathy, sympathy and compassion",
    },
    {
        "label": "Compassion must be operationalised as service design",
        "statement": (
            "Compassion toward weaker sections is exam-credible only when it changes a process: "
            "simplified forms, doorstep delivery, vernacular communication or accessible digital "
            "design; good intention alone does not reach a citizen who cannot navigate a complex "
            "bureaucratic procedure."
        ),
        "scenario_a": (
            "A district converts all land-record applications to an online-only portal but "
            "provides no assisted kiosks or vernacular support in tribal areas. Why does this "
            "reform fail the compassion standard despite its modernisation intent?"
        ),
        "scenario_b": (
            "A block office introduces simplified one-page forms, local-language help desks "
            "and doorstep camps for disability-certificate applicants. Which feature converts "
            "compassion from sentiment into an observable administrative output?"
        ),
        "group": "empathy, sympathy and compassion",
    },
    {
        "label": "Compassion-driven discretion can become favouritism",
        "statement": (
            "Compassion-driven discretion without transparent eligibility criteria can be "
            "indistinguishable in form from favouritism; the safeguard is transparent rule-based "
            "criteria, not the presence or absence of discretion itself."
        ),
        "scenario_a": (
            "A welfare officer informally expedites ration-card renewal for a neighbour's "
            "family claiming compassionate grounds, without any published criterion justifying "
            "the expedited treatment. Why is this indistinguishable from favouritism despite "
            "the officer's sincere concern?"
        ),
        "scenario_b": (
            "A district publishes a government order listing conditions under which fee waivers "
            "apply, requires written reasons for each waiver granted, and audits waivers "
            "quarterly. Which mechanism prevents compassionate discretion from degenerating "
            "into selective favour?"
        ),
        "group": "empathy, sympathy and compassion",
    },
    # --- Group: tolerance, institutional architecture and answer craft ---
    {
        "label": "Tolerance anchored in constitutional morality",
        "statement": (
            "Tolerance in the GS-IV syllabus means respect for and acceptance of diversity "
            "of belief, culture and viewpoint; it is anchored in constitutional morality "
            "through Article 51A(e) and the duty of secular conduct, going beyond mere passive "
            "non-interference."
        ),
        "scenario_a": (
            "A district magistrate ensures that a minority community's lawful religious "
            "procession receives the same police protection and route facilitation as the "
            "majority community's festival. Which foundational value and constitutional "
            "anchor is she demonstrating?"
        ),
        "scenario_b": (
            "An officer says she tolerates a minority group by ignoring them entirely and "
            "providing no positive facilitation. Why does the constitutional-morality standard "
            "require more than passive non-interference?"
        ),
        "group": "tolerance, institutional architecture and answer craft",
    },
    {
        "label": "Mission Karmayogi operationalises values as competencies",
        "statement": (
            "Mission Karmayogi under the NPCSCB converts foundational values from informal "
            "socialisation into trainable competencies through the FRAC framework and the "
            "iGOT-Karmayogi digital platform; it demonstrates institutional commitment to "
            "values education but does not by itself prove ethical internalisation."
        ),
        "scenario_a": (
            "A department records 100 percent course completion on iGOT modules on empathy "
            "and objectivity but field audits reveal continued discrimination against "
            "Scheduled Tribe applicants. Which distinction between training exposure and "
            "ethical conduct does this gap illustrate?"
        ),
        "scenario_b": (
            "A citizen-facing office uses FRAC-based role mapping to identify empathy and "
            "communication gaps, assigns targeted learning modules and supplements them with "
            "citizen-feedback loops. Which institutional logic connects values training to "
            "observable service improvement?"
        ),
        "group": "tolerance, institutional architecture and answer craft",
    },
    {
        "label": "Nolan principles overlap but are not identical to GS-IV list",
        "statement": (
            "The Nolan Committee's seven principles of public life are selflessness, integrity, "
            "objectivity, accountability, openness, honesty and leadership; they overlap "
            "substantially with the GS-IV syllabus list but are not identical, since the "
            "syllabus adds empathy, tolerance and compassion while Nolan adds accountability "
            "and openness as separate principles."
        ),
        "scenario_a": (
            "A candidate equates the GS-IV foundational-values list with the Nolan seven "
            "without qualification. Which specific values are present in one list but absent "
            "from the other?"
        ),
        "scenario_b": (
            "A training module presents the Nolan principles as the complete ethical framework "
            "for Indian civil servants. Why is it necessary to also address empathy, tolerance "
            "and compassion toward weaker sections to cover the UPSC syllabus fully?"
        ),
        "group": "tolerance, institutional architecture and answer craft",
    },
    {
        "label": "Answer craft for foundational-values questions",
        "statement": (
            "A strong foundational-values answer names the value precisely, identifies the "
            "realistic pressure under which it is tested, names the institutional safeguard "
            "that operationalises or protects it, gives a concrete Indian example, and "
            "acknowledges the value's operational limit."
        ),
        "scenario_a": (
            "A candidate writes that integrity is important and lists adjectives without "
            "mentioning asset declarations, audit trails or any specific pressure scenario. "
            "Which structural element of a high-scoring answer is missing?"
        ),
        "scenario_b": (
            "Another candidate names integrity, describes the discretion-secrecy test, cites "
            "asset-declaration rules as the institutional proxy, gives a procurement example "
            "and notes that declarations monitor but cannot guarantee internalisation. Why does "
            "this architecture score higher?"
        ),
        "group": "tolerance, institutional architecture and answer craft",
    },
)

PYQS = (
    {
        "year": 2025,
        "question": (
            "To achieve holistic development goal, a civil servant acts as an enabler "
            "and active facilitator of growth rather than a regulator. What specific "
            "measures will you suggest to achieve this goal? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: books/mains/UPSC Mains "
            "2025 GS Paper 4.pdf, Q5(b)."
        ),
        "answer": (
            "The proposition redefines a civil servant's foundational value of dedication: "
            "service quality is now measured by outcomes enabled, not merely rules enforced. "
            "Enablement does not mean abandoning regulation but calibrating it through risk-"
            "based sequencing.\n\n"
            "Specific measures include: (1) single-window clearance combining multiple "
            "pre-approvals into one time-bound process for low-risk enterprises; "
            "(2) outcome-based key performance indicators that reward officials for citizen "
            "welfare improvements such as reduced processing time, rather than input compliance "
            "alone; (3) risk-based inspection replacing universal ex-ante gatekeeping with "
            "post-facto scrutiny proportionate to actual risk, so a cottage-industry unit is "
            "not subjected to the same regime as a chemical plant; (4) digital facilitation "
            "portals with published criteria, timelines and tracking, combined with assisted "
            "access for digitally weak populations; (5) capacity-building through Mission "
            "Karmayogi that orients officials toward a facilitative mindset while retaining "
            "regulatory competence.\n\n"
            "The limit is real. Pure facilitation without regulatory backstops risks capture "
            "and public harm, as shown when environmental inspections are abolished and "
            "chemical leaks follow. The calibrated position is: facilitate legitimate activity "
            "proactively, regulate safety and equity where law requires it, and use evidence-"
            "based risk assessment to allocate enforcement resources. This makes the civil "
            "servant an enabler of holistic development within a framework of accountable "
            "public duty."
        ),
    },
    {
        "year": 2025,
        "question": (
            '"For any kind of social re-engineering by successfully implementing welfare '
            'schemes, a civil servant must use reason and critical thinking in an ethical '
            'framework." Justify this statement with suitable examples. (Answer in 150 words)'
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: books/mains/UPSC Mains "
            "2025 GS Paper 4.pdf, Q4(a)."
        ),
        "answer": (
            "Reason and critical thinking apply objectivity to welfare-scheme design and "
            "delivery. A civil servant uses them within an ethical framework by testing "
            "assumptions against evidence, evaluating consequences for the weakest "
            "beneficiaries, and designing processes that are fair, transparent and revisable.\n\n"
            "For example, a district officer implementing a nutrition scheme may find that "
            "registration requires documents many tribal families lack. Critical thinking "
            "asks whether the documentation barrier serves a genuine verification purpose or "
            "merely excludes the intended beneficiaries. If alternative verification is "
            "available, reason supports simplifying access while maintaining accountability. "
            "Similarly, a housing scheme distributing units by lottery may appear neutral, but "
            "critical analysis may reveal that physically disabled applicants cannot access "
            "upper-floor units; ethical reasoning requires accessible design, not just formal "
            "equality.\n\n"
            "Social re-engineering through welfare schemes demands that the officer question "
            "inherited assumptions about who deserves help, how delivery works, and whether "
            "the process creates new exclusions. Reason supplies the analytical discipline; "
            "the ethical framework supplies the normative compass of fairness, compassion "
            "and constitutional equality.\n\n"
            "The limit is that reason alone can rationalise any end. It must be anchored in "
            "law, published criteria, citizen participation and review. The verdict is that "
            "objectivity and dedication together enable welfare schemes that transform social "
            "conditions rather than merely disburse funds."
        ),
    },
    {
        "year": 2025,
        "question": (
            '"One who is devoted to one\'s duty attains highest perfection in life." '
            "Analyse this statement with reference to sense of responsibility and personal "
            "fulfilment as a civil servant. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: books/mains/UPSC Mains "
            "2025 GS Paper 4.pdf, Q5(a)."
        ),
        "answer": (
            "Devotion to duty is a foundational value that combines responsibility for "
            "timely, fair and competent public action with a personal motivation that "
            "exceeds minimum compliance. It yields fulfilment when the officer finds meaning "
            "in the welfare impact of her work rather than in private reward.\n\n"
            "A revenue officer who stays after hours to resolve pending pension grievances, "
            "documents workload risks, delegates lawfully and sees elderly citizens receive "
            "their entitlements experiences fulfilment through responsible, citizen-centred "
            "service. This is consistent with the Nishkama karma ideal of performing duty "
            "without attachment to personal fruit while remaining concerned about public "
            "outcomes.\n\n"
            "Devotion to duty has ethical limits. It does not require obeying an unlawful "
            "order, accepting chronic burnout as virtue, or disregarding feedback from "
            "affected citizens. A civil servant who treats heroic overwork as the sole "
            "measure of dedication may neglect sustainable work design, staff welfare and "
            "institutional learning.\n\n"
            "The reasoned verdict is that devotion to duty gives both public accountability "
            "and personal fulfilment when it is guided by legality, empathy and measurable "
            "citizen welfare. It becomes self-defeating when it is confused with blind "
            "obedience or when the system exploits dedication without reciprocal support."
        ),
    },
    {
        "year": 2024,
        "question": (
            '"In Indian culture and value system, an equal opportunity has been provided '
            "irrespective of gender identity. The number of women in public service has "
            'been steadily increasing over the years." Examine the gender-specific '
            "challenges faced by female public servants and suggest suitable measures to "
            "increase their efficiency in discharging their duties and maintaining high "
            "standards of probity. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: books/mains/05 UPSC 2024 "
            "Paper-IV_Final 1.pdf, Q6(a)."
        ),
        "answer": (
            "Female public servants face gender-specific challenges including safety risks "
            "during field postings, inadequate sanitation and crache facilities, implicit bias "
            "in performance evaluation, disproportionate informal workload, and limited access "
            "to mentoring networks dominated by male colleagues. These barriers affect both "
            "efficiency and morale.\n\n"
            "Measures to address them while maintaining probity include: (1) safe and adequate "
            "infrastructure at workplaces and field stations; (2) enforceable sexual-harassment "
            "redress through functional Internal Complaints Committees with time-bound "
            "resolution; (3) flexible posting options during caregiving periods without career "
            "penalty; (4) structured mentoring and sponsorship programmes that connect women "
            "officers with senior leadership; (5) transparent and gender-audited performance "
            "appraisal criteria that assess outcomes rather than visibility.\n\n"
            "This question tests foundational values reflexively: impartiality means the "
            "civil service must apply its own values to its workforce, not only to citizens. "
            "Compassion requires institutional design, not sentiment. Probity is maintained "
            "because every measure operates within published rules, applies transparently to "
            "all eligible officers, and is reviewable.\n\n"
            "The verdict is that gender-specific measures are not preferential treatment but "
            "the operationalisation of equal opportunity within a system that must practise "
            "the impartiality it demands from its officers."
        ),
    },
    {
        "year": 2021,
        "question": (
            "Neutral rendering: (b) Discuss why impartiality and non-partisanship are "
            "indispensable qualities for a civil servant."
        ),
        "marks": 10,
        "source_note": (
            "Routed historical demand from 2021 GS-IV Q5(b); neutral rendering used because "
            "exact wording is not claimed from a locally held official PDF."
        ),
        "answer": (
            "Impartiality and non-partisanship are indispensable because a civil servant "
            "holds public power on behalf of all citizens, not a faction. Impartiality "
            "requires merit-based and rule-bound decisions free of personal, familial or "
            "political bias. Non-partisanship requires loyal service to the government of "
            "the day without allowing party political considerations to shape official "
            "advice or action.\n\n"
            "Their necessity arises from the structure of Indian democracy. A tax officer "
            "applying identical audit-selection criteria to politically connected and "
            "unconnected assessees demonstrates impartiality; selectively targeting or "
            "sparing either group on non-merit grounds violates it regardless of the "
            "direction of bias. A returning officer conducting elections must provide "
            "identical scrutiny to all candidates despite pressure from the ruling party.\n\n"
            "Structurally, non-partisanship is threatened by the arbitrary-transfer "
            "mechanism documented by the ARC. Without tenure safeguards such as Civil "
            "Services Board recommendations and fixed-tenure norms, an officer's "
            "non-partisan conduct may not survive political transition. Training alone "
            "cannot compensate for an institutional environment that punishes independence.\n\n"
            "The verdict is that these values are indispensable because they protect the "
            "citizen's right to equal, lawful and accountable governance. Their durability "
            "depends on institutional safeguards joining personal conviction."
        ),
    },
    {
        "year": 2021,
        "question": (
            "Neutral rendering: (a) Identify five ethical traits on which one can plot "
            "the performance of a civil servant."
        ),
        "marks": 10,
        "source_note": (
            "Routed historical demand from 2021 GS-IV Q1(a); neutral rendering used."
        ),
        "answer": (
            "Five ethical traits suitable for assessing a civil servant's performance are "
            "integrity, impartiality, empathy, accountability and dedication to public "
            "service. Each can be operationally assessed.\n\n"
            "Integrity is tested by whether the officer's conduct remains consistent when "
            "unobserved: asset declarations, conflict-of-interest disclosures and audit "
            "trails serve as institutional proxies. Impartiality is tested by whether "
            "decisions follow published criteria without personal or political favour. "
            "Empathy is tested by whether service design accounts for the weakest citizen's "
            "access barriers. Accountability is tested by whether the officer gives reasons, "
            "responds to grievances and submits to review. Dedication is tested by whether "
            "the officer takes initiative beyond minimum compliance to improve citizen "
            "outcomes.\n\n"
            "A performance matrix using these traits can supplement numerical targets with "
            "citizen feedback, grievance-resolution quality, reasoned file disposals and "
            "compliance with disclosure norms. This prevents the assessment from rewarding "
            "only quantitative output while ignoring ethical quality.\n\n"
            "The limitation is that trait-based assessment requires clear indicators and "
            "fair evaluators. Subjective appraisal without transparent criteria can itself "
            "violate impartiality. The verdict is that ethical traits strengthen performance "
            "evaluation when they are operationally defined, transparently measured and "
            "joined to institutional safeguards."
        ),
    },
    {
        "year": 2019,
        "question": (
            "Neutral rendering: (a) Discuss the basic principles of public life and "
            "illustrate each with an example."
        ),
        "marks": 10,
        "source_note": (
            "Routed historical demand from 2019 GS-IV Q1(a); neutral rendering used."
        ),
        "answer": (
            "The Nolan Committee identified seven basic principles of public life: "
            "selflessness, integrity, objectivity, accountability, openness, honesty "
            "and leadership. These principles, cited by the 2nd ARC, provide a portable "
            "ethical framework for any public servant.\n\n"
            "Selflessness means deciding solely in the public interest. A district "
            "magistrate allocating flood relief across communities regardless of "
            "personal affinity illustrates it. Integrity means freedom from financial "
            "or other obligations that could compromise duty. Objectivity means decisions "
            "on merit: a recruitment board applying published criteria to all candidates "
            "exemplifies it. Accountability means submitting to scrutiny: an officer "
            "responding to RTI queries and audit reports demonstrates it. Openness "
            "means maximum disclosure; restricting information only when public interest "
            "genuinely requires it. Honesty means declaring private interests and "
            "resolving conflicts to protect the public interest. Leadership means "
            "promoting these principles by example.\n\n"
            "These principles overlap with but are not identical to the GS-IV syllabus "
            "list, which adds empathy, tolerance and compassion while Nolan separately "
            "names accountability and openness. The verdict is that the Nolan principles "
            "supply a tested minimum standard; Indian administrative ethics must also "
            "address compassion toward weaker sections and constitutional morality."
        ),
    },
    {
        "year": 2018,
        "question": (
            "Neutral rendering: (b) Illustrate with examples the distinction between "
            "code of ethics and code of conduct."
        ),
        "marks": 10,
        "source_note": (
            "Routed historical demand from 2018 GS-IV Q1(b); neutral rendering used. "
            "ARC 2.2.6 is the primary source for the distinction."
        ),
        "answer": (
            "The 2nd ARC distinguishes a code of ethics from a code of conduct. A code "
            "of ethics states broad guiding principles of good behaviour and governance. "
            "A code of conduct specifies precise, unambiguous lists of acceptable and "
            "unacceptable actions, with enforceable sanctions.\n\n"
            "For example, a code of ethics may state that officers shall act with "
            "integrity and serve the public interest impartially. A code of conduct may "
            "specify that no officer shall accept a gift exceeding a stated value from "
            "any person with whom she has official dealings, and that violation attracts "
            "disciplinary proceedings. The ethics statement sets direction; the conduct "
            "rule makes it enforceable.\n\n"
            "Both are necessary. Without the code of ethics, a list of rules lacks a "
            "guiding rationale and cannot address situations the rule-drafters did not "
            "foresee. Without the code of conduct, broad principles remain aspirational "
            "and unenforceable, giving officials no clear boundary and citizens no basis "
            "for complaint. The ARC recommends both as complementary instruments.\n\n"
            "The verdict is that the ethics-conduct distinction is not academic: it "
            "directly affects how values are institutionalised. An answer that confuses "
            "the two fails to show how public administration moves from aspiration to "
            "accountability."
        ),
    },
    {
        "year": 2018,
        "question": (
            "Neutral rendering: (b) Illustrate with suitable examples Warren Buffett's "
            "idea that when hiring you look for integrity, intelligence and energy, and "
            "that without the first the other two will destroy you."
        ),
        "marks": 10,
        "source_note": (
            "Routed historical demand from 2018 GS-IV Q3(b); neutral rendering used. "
            "Attribution caution: Buffett introduces the line as something 'somebody "
            "once said'; traceable to a 1994 Omaha World-Herald report of his 1993 "
            "Columbia Business School remarks."
        ),
        "answer": (
            "The proposition holds that integrity is the precondition that determines "
            "whether intelligence and energy serve the public or damage it. Intelligence "
            "and energy are force-multipliers: they amplify whatever the underlying "
            "disposition already is. Without integrity, a highly capable and driven "
            "official becomes more effective at concealment, favouritism or embezzlement, "
            "not less likely to attempt them.\n\n"
            "A tax officer with exceptional analytical skill and tireless energy can, "
            "without integrity, construct schemes to conceal selective assessments "
            "favouring politically connected firms. Conversely, an officer of modest "
            "analytical ability but firm integrity will resist improper demands even "
            "under pressure, report conflicts and maintain reasoned records. The former "
            "is dangerous; the latter is trustworthy though possibly slower.\n\n"
            "The administrative implication is that competitive examinations test "
            "intelligence and probation tests energy, but integrity is structurally the "
            "hardest to test at entry. This justifies continuous institutional safeguards: "
            "asset declarations, conflict-of-interest disclosures, vigilance clearance, "
            "random audits, cooling-off periods and, under Mission Karmayogi, behavioural "
            "competency assessment.\n\n"
            "An attribution caution: Buffett endorsed this as a teaching but introduced "
            "the line as something somebody once said. Its ethical force is valid "
            "regardless. The verdict is that integrity is listed first among GS-IV values "
            "because without it every other capability becomes a risk rather than an asset."
        ),
    },
    {
        "year": 2019,
        "question": (
            "Neutral rendering: A rescue officer during a severe natural calamity finds "
            "team members assaulted by an angry crowd; some plead to call off rescue "
            "operations. What will be your response and what qualities of a public "
            "servant are required in such a situation?"
        ),
        "marks": 20,
        "source_note": (
            "Routed historical demand from 2019 GS-IV Q7; neutral rendering used. "
            "Case study format, 250 words."
        ),
        "answer": (
            "The situation tests several foundational values simultaneously: dedication "
            "to public service, courage, empathy, objectivity and leadership.\n\n"
            "Immediate response: (1) Ensure the safety of the team by withdrawing to a "
            "secure staging point if physical danger is imminent; no duty requires "
            "exposing unarmed rescuers to mob violence without protection. (2) Request "
            "police or paramilitary assistance to restore order and protect the rescue "
            "team. (3) Communicate with the crowd through a local community leader or "
            "elected representative to understand grievances and de-escalate hostility; "
            "often the crowd's anger stems from perceived government failure, delayed "
            "relief or misinformation rather than hatred of rescuers. (4) Resume rescue "
            "operations once minimum safety conditions are restored, prioritising the "
            "most vulnerable victims.\n\n"
            "Qualities required: Dedication to duty means the officer does not abandon "
            "affected persons because the task is dangerous, but pursues it through safe "
            "and lawful means. Empathy means understanding both the victims' suffering "
            "and the team's fear. Objectivity means assessing the situation factually "
            "rather than reacting emotionally. Courage means persisting under pressure "
            "while taking calculated rather than reckless risks. Leadership means "
            "communicating the mission clearly, supporting the team and modelling calm "
            "under stress.\n\n"
            "The officer should not call off operations entirely. But dedication does "
            "not mean suicidal heroism: it means finding a way to serve affected citizens "
            "through legitimate protective measures, communication and coordinated action. "
            "The verdict is that the public servant's response must combine compassion "
            "for all affected parties with the institutional discipline to secure the "
            "rescue mission through lawful, protective and coordinated measures."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Distinguish aptitude, attitude and value as objects of civil-service "
            "assessment. Illustrate each with one administrative example. Answer in "
            "150 words."
        ),
        "answer": (
            "Aptitude, attitude and value are three distinct objects of assessment. "
            "Aptitude is the capacity to perform: a trainee's ability to manage a flood-"
            "control room tests aptitude. Attitude is an evaluative stance toward a "
            "specific object: an officer's enthusiasm for digital governance reflects "
            "her attitude toward technology, which may not generalise to other domains. "
            "Value is a cross-situational standard: integrity governs conduct across "
            "procurement, citizen interaction and personal finances.\n\n"
            "Confusing them weakens answers. Saying integrity is an attitude reduces a "
            "general moral standard to a domain-specific preference. Saying aptitude is "
            "fixed ignores that contemporary civil-service pedagogy, including Mission "
            "Karmayogi's competency-based training, treats aptitude as cultivable through "
            "deliberate practice.\n\n"
            "The administrative implication is that recruitment tests primarily measure "
            "aptitude and intelligence, while probation and performance review assess "
            "dedication and initiative. Integrity and compassion require continuous "
            "institutional monitoring because they are values tested under discretion, "
            "not capacities measured in a single examination. The verdict is that precise "
            "classification strengthens both assessment design and answer writing."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Explain why integrity is described as the hardest foundational value to "
            "test at recruitment. What institutional mechanisms serve as continuous "
            "proxies? Answer in 150 words."
        ),
        "answer": (
            "Integrity is the consistency of values across situations, especially under "
            "unobserved conditions. Unlike intelligence or energy, which can be assessed "
            "through examinations and performance records, integrity is asymmetrically "
            "tested: it is nearly costless to display when observed and genuinely tested "
            "only when discretion, secrecy and personal gain converge.\n\n"
            "This makes one-time recruitment tests inadequate. A candidate may answer "
            "ethics questions correctly without possessing the disposition to act on them "
            "under real pressure. The state therefore legislates proxies: annual asset "
            "declarations, conflict-of-interest disclosures, cooling-off periods for "
            "retiring officials, random departmental inspections, vigilance clearance "
            "requirements and, increasingly, 360-degree feedback under Mission Karmayogi.\n\n"
            "These mechanisms convert an unobservable trait into partially observable "
            "behaviour. Their limitation is that they monitor symptoms rather than "
            "guarantee character. The verdict is that integrity requires both value "
            "internalisation through training and institutional containers that make "
            "departure from integrity detectable and consequential."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Discuss the claim that non-partisanship is an institutional-design "
            "problem rather than a matter of personal character alone, drawing on the "
            "ARC's analysis of the transfer mechanism. Answer in 200 words."
        ),
        "answer": (
            "Non-partisanship requires a civil servant to serve the government of the "
            "day without allowing party political considerations to shape official advice. "
            "The 2nd ARC's chapter on political executive-civil service relations "
            "documents the discretionary transfer as the structural threat to this value. "
            "Robert Wade's study of Andhra Pradesh, cited at ARC 9.4, describes the "
            "transfer as the politicians' basic weapon of control over the bureaucracy "
            "and the lever for surplus extraction from its clients.\n\n"
            "When an officer's posting depends on political patronage rather than merit "
            "or tenure norms, even a personally non-partisan officer faces a structural "
            "incentive to comply with improper directions. The Fifth Pay Commission "
            "recommended a minimum three-to-five-year tenure; the ARC endorsed Civil "
            "Services Board mechanisms to insulate routine transfers from unmediated "
            "political discretion. Without these safeguards, ethics training produces "
            "an officer with the right disposition but the wrong institutional environment.\n\n"
            "This does not mean personal character is irrelevant. Some officers maintain "
            "non-partisanship despite structural pressure, and training builds the moral "
            "vocabulary to articulate and defend professional independence. But character "
            "alone is an unreliable guarantee when the cost of independence is career "
            "disruption.\n\n"
            "The verdict is that durable non-partisanship requires both individual "
            "conviction and institutional protection. Fixed tenure, transparent criteria, "
            "review boards and safe dissent channels are not administrative luxuries but "
            "structural preconditions for a value that democracy depends upon."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Analyse the tension between compassion toward weaker sections and "
            "impartial rule-application in welfare-scheme delivery. When does "
            "compassion-driven discretion become indistinguishable from favouritism? "
            "Answer in 200 words."
        ),
        "answer": (
            "Compassion toward weaker sections requires service design that accounts "
            "for vulnerability: simplified forms, doorstep delivery, vernacular access "
            "and exemptions for those who cannot meet standard procedural demands. "
            "Impartiality requires that such accommodations be rule-based, transparent "
            "and applied consistently to all similarly situated persons. The tension "
            "arises when compassionate discretion operates without published criteria.\n\n"
            "A block officer who waives documentation for a below-poverty-line applicant "
            "under a government order exercises compassion within impartial rules. The "
            "same officer who informally expedites a neighbour's file on compassionate "
            "grounds, without any published criterion, crosses into favouritism regardless "
            "of sincerity. The distinguishing safeguard is transparent eligibility criteria, "
            "written reasons and periodic audit, not the presence or absence of "
            "discretion itself.\n\n"
            "Affirmative, needs-based facilitation for weaker sections, such as fee "
            "waivers or assisted kiosks, is impartial if the criteria are published and "
            "universally applied to all who meet them. The same facilitation extended "
            "selectively to a politically favoured individual is nepotism, not compassion.\n\n"
            "The verdict is that compassion and impartiality are not opposed. They become "
            "incompatible only when compassion operates outside rule-bound transparency. "
            "The institutional answer is clear eligibility criteria, recorded reasons "
            "and review mechanisms that make compassionate discretion auditable."
        ),
    },
    {
        "marks": 20,
        "question": (
            "A civil servant must be an enabler and active facilitator of growth rather "
            "than a regulator. Critically examine this proposition, suggesting specific "
            "risk-based measures that reconcile facilitation with regulatory oversight "
            "for holistic development. Answer in 250 words."
        ),
        "answer": (
            "The enabler proposition shifts the foundational value of dedication from "
            "gatekeeping compliance toward outcome-oriented facilitation. It asks a civil "
            "servant to remove unnecessary barriers, simplify access and proactively "
            "connect citizens and enterprises to public resources. This is consistent "
            "with the UPSC's 2025 GS-IV framing of holistic development.\n\n"
            "Specific risk-based measures include: single-window clearance for low-risk "
            "activities, replacing multiple sequential approvals with a consolidated "
            "time-bound process; deemed approval with accountability, where inaction "
            "within a specified period results in automatic clearance, shifting the "
            "bureaucratic incentive from delay to timely review; post-facto risk-based "
            "inspection, directing enforcement resources toward high-risk sectors while "
            "allowing low-risk establishments to self-certify; outcome-linked KPIs that "
            "reward officials for measurable citizen welfare improvements rather than "
            "input compliance; and digital facilitation platforms with published criteria "
            "and tracking, supplemented by assisted access for populations lacking "
            "digital literacy.\n\n"
            "The critical examination must acknowledge limits. Pure facilitation without "
            "regulatory backstops risks regulatory capture. When environmental inspections "
            "are abolished wholesale, chemical leaks and safety failures can follow. "
            "Facilitation without reliable risk-classification systems can default into "
            "under-regulation by omission rather than deliberate calibration. The ARC's "
            "analysis suggests that regulation and facilitation are not opposites but "
            "sequential: facilitate legitimate activity through transparent process, then "
            "regulate through proportionate, evidence-based oversight.\n\n"
            "The verdict is that a civil servant should be both enabler and regulator in "
            "calibrated sequence. Holistic development requires proactive service delivery "
            "combined with accountable oversight. The foundational value of dedication is "
            "fulfilled not by removing safeguards but by designing systems that serve "
            "citizens quickly, fairly and safely."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Evaluate the claim that foundational civil-service values are "
            "institutionally testable design commitments rather than personal "
            "adjectives. Substantiate with reference to Mission Karmayogi's competency "
            "architecture, the Civil Services Board mechanism, and one concrete "
            "service-delivery redesign. Answer in 250 words."
        ),
        "answer": (
            "The claim reframes foundational values from character descriptions to "
            "institutional design questions. Instead of asking whether an officer is "
            "honest, it asks whether the system makes integrity observable, protectable "
            "and consequential. Three illustrations substantiate this.\n\n"
            "First, Mission Karmayogi's competency architecture treats values as "
            "trainable inputs through the FRAC framework and iGOT platform. Functional "
            "and behavioural competencies are mapped to roles, and learning is delivered "
            "through the citizen-government interface orientation. As of 2026, the "
            "platform aligns roles with required competencies through the Karmayogi "
            "Competency Model, supports lifelong learning records and uses AI-enabled "
            "competency assessment including AI Sarthi and AI Tutor for role-based "
            "personalised learning. This demonstrates institutional investment, though "
            "learning architecture and AI-enabled delivery do not prove ethical "
            "internalisation.\n\n"
            "Second, the Civil Services Board mechanism institutionally protects "
            "non-partisanship by insulating routine transfer decisions from unmediated "
            "political discretion. Without it, non-partisanship remains a personal "
            "aspiration vulnerable to the transfer leverage documented by the ARC. With "
            "it, the value gains structural durability.\n\n"
            "Third, redesigning pension verification from mandatory in-person appearance "
            "to video-call options for elderly and disabled beneficiaries operationalises "
            "compassion as service design. The value is no longer a sentiment but an "
            "assessable administrative output with measurable access improvement.\n\n"
            "The limitation is real. Institutional tests can be gamed: declarations "
            "filed, courses completed, and processes redesigned without genuine ethical "
            "change. Values still require internalisation through mentoring, leadership "
            "example and a culture that rewards ethical conduct.\n\n"
            "The verdict is that foundational values are most durable when they are both "
            "personally internalised and institutionally operationalised. Design "
            "commitments make values testable, protectable and consequential; personal "
            "conviction makes them reliable where institutional observation fails."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. Aptitude, attitude and value: the three-object taxonomy",
        "structural_type": "comparison-matrix",
        "nodes": (
            "Aptitude is capacity to perform a task or role competently.",
            "Attitude is an evaluative stance toward a specific object.",
            "Value is a general cross-situational standard of worth.",
            "Aptitude is trainable through deliberate practice and mentoring.",
            "Attitude can change with experience; values are more enduring.",
            "Recruitment tests primarily measure aptitude and intelligence.",
            "Probation and appraisal assess dedication and initiative.",
            "Confusing the three weakens assessment design and answers.",
        ),
        "verdict": "Classify the object of assessment precisely before applying it to a civil-service case.",
        "answer_use": "Open foundational-values answers by distinguishing what is being assessed.",
    },
    {
        "title": "2. Integrity under discretion: the hardest test",
        "structural_type": "decision-tree",
        "nodes": (
            "Integrity means consistency of values across situations.",
            "The Nolan Committee treats integrity and honesty as separate principles.",
            "Integrity is costless to display when observed.",
            "It is genuinely tested when discretion, secrecy and gain converge.",
            "The state cannot legislate integrity directly.",
            "It legislates proxies: asset declarations and conflict disclosures.",
            "Random inspections and cooling-off periods add observable checks.",
            "Integrity proxies monitor behaviour but cannot guarantee character.",
        ),
        "verdict": "Integrity is the precondition for every other foundational value to be trustworthy.",
        "answer_use": "Use the discretion-secrecy-gain test to show how integrity is operationally assessed.",
    },
    {
        "title": "3. Impartiality is not identical treatment",
        "structural_type": "fork-diagram",
        "nodes": (
            "Impartiality requires decisions on merit without personal bias.",
            "It does not require identical treatment regardless of need.",
            "Needs-based support for weaker sections can be impartial.",
            "The criterion is whether differentiation is transparent and rule-based.",
            "A published fee waiver for BPL applicants is impartial.",
            "An informal favour for a relative is nepotism under any label.",
            "The safeguard is transparent eligibility, not removal of discretion.",
            "Affirmative facilitation strengthens equality of access.",
        ),
        "verdict": "Test the criteria, not the outcome, to distinguish impartiality from favouritism.",
        "answer_use": "Apply to welfare-scheme, reservation, or targeted-delivery answers.",
    },
    {
        "title": "4. Non-partisanship and the transfer industry",
        "structural_type": "causal-flow",
        "nodes": (
            "Non-partisanship requires party-neutral official conduct.",
            "Personal political views are permitted; official action is not.",
            "The ARC documents transfer as the politicians' control weapon.",
            "Robert Wade's AP study shows transfer as a lever for extraction.",
            "Without tenure protection, non-partisanship is structurally fragile.",
            "The Fifth Pay Commission recommended three-to-five-year tenure.",
            "Civil Services Board insulates transfers from political discretion.",
            "Training plus tenure protection produces durable non-partisanship.",
        ),
        "verdict": "Non-partisanship is an institutional-design achievement, not just a personal virtue.",
        "answer_use": "Ground non-partisanship answers in structural analysis rather than exhortation.",
    },
    {
        "title": "5. Empathy, sympathy and compassion: an ascending ladder",
        "structural_type": "ascending-ladder",
        "nodes": (
            "Sympathy feels for someone from outside with an implicit hierarchy.",
            "Empathy grasps another's situation from their frame of reference.",
            "Compassion adds a motivated commitment to relieve suffering.",
            "Only compassion necessarily issues in action or service design.",
            "A social media statement of sorrow is sympathy, not compassion.",
            "Listening to displaced families and adjusting relief is empathy.",
            "Redesigning pension verification for disabled applicants is compassion.",
            "GS-IV answers must translate feeling into a process change.",
        ),
        "verdict": "Compassion earns marks only when it changes a defensible administrative process.",
        "answer_use": "Use the ladder to escalate from sentiment to service-design in any answer.",
    },
    {
        "title": "6. Enabler versus regulator: calibration spectrum",
        "structural_type": "spectrum-slider",
        "nodes": (
            "Facilitation removes barriers and proactively connects citizens to services.",
            "Regulation protects safety, equity and public interest.",
            "Single-window clearance consolidates multiple approvals for low-risk cases.",
            "Post-facto risk-based inspection replaces universal ex-ante gatekeeping.",
            "Deemed approval shifts incentive from delay to timely review.",
            "Pure facilitation without backstops risks regulatory capture.",
            "Excessive regulation without enabling stifles legitimate development.",
            "Calibration requires reliable risk-classification systems.",
        ),
        "verdict": "The civil servant should sequence facilitation and regulation, not choose one exclusively.",
        "answer_use": "Use to build the calibrated-role paragraph in any enabler-regulator question.",
    },
    {
        "title": "7. Mission Karmayogi: values as trainable competencies",
        "structural_type": "institutional-flow",
        "nodes": (
            "NPCSCB approved by Cabinet on 2 September 2020.",
            "FRAC maps functional and behavioural competencies to roles.",
            "iGOT-Karmayogi delivers learning in 23 languages.",
            "KCM aligns roles with competencies and supports accountability and role-fit (CBC).",
            "AI Sarthi and AI Tutor showcased at IndiaAI Impact Summit (16-20 Feb 2026) for role-based personalised learning (CBC).",
            "Training reach does not prove ethical internalisation.",
            "Do not claim a general APAR linkage without a service-specific DoPT order.",
            "Values training needs supplementation by citizen feedback and field observation.",
        ),
        "verdict": "Mission Karmayogi institutionalises values education; it cannot certify ethical conduct.",
        "answer_use": "Cite as the institutional bridge between values and role-based capacity.",
    },
    {
        "title": "8. Compassion versus favouritism: the boundary",
        "structural_type": "fork-diagram",
        "nodes": (
            "Compassionate facilitation uses transparent published criteria.",
            "Favouritism uses informal selection without published justification.",
            "Both may look identical in form: expedited service for one person.",
            "The distinguishing test is whether criteria are rule-based and auditable.",
            "Written reasons for each discretionary decision create an audit trail.",
            "Periodic review of waiver and expedited-service patterns detects drift.",
            "Affirmative needs-based support passes the test; selective favour fails it.",
            "The safeguard is transparency, not the removal of all discretion.",
        ),
        "verdict": "Compassion and impartiality coexist when discretion operates within published rules.",
        "answer_use": "Use to resolve the compassion-favouritism tension in welfare-delivery answers.",
    },
    {
        "title": "9. Tolerance and constitutional morality",
        "structural_type": "anchor-framework",
        "nodes": (
            "Tolerance means respect for diversity of belief, culture and viewpoint.",
            "It goes beyond passive non-interference to positive facilitation.",
            "Article 51A(e) anchors tolerance in a fundamental duty of secular conduct.",
            "Constitutional morality requires fidelity to constitutional values.",
            "Equal police protection for minority processions demonstrates tolerance.",
            "Ignoring a minority community is not tolerance but neglect.",
            "Tolerance does not require approval; it requires equal respect and access.",
            "Constitutional morality disciplines personal prejudice with public duty.",
        ),
        "verdict": "Tolerance becomes a foundational administrative value through constitutional morality.",
        "answer_use": "Use to anchor diversity and secularism answers in specific constitutional provisions.",
    },
    {
        "title": "10. Nolan seven versus GS-IV syllabus list",
        "structural_type": "overlap-matrix",
        "nodes": (
            "Nolan lists selflessness, integrity, objectivity as shared with GS-IV.",
            "Nolan adds accountability, openness, honesty and leadership.",
            "GS-IV adds empathy, tolerance and compassion toward weaker sections.",
            "Non-partisanship appears in GS-IV but not explicitly in Nolan.",
            "Dedication to public service overlaps with Nolan's selflessness.",
            "The two lists are complementary, not identical.",
            "Equating them without qualification is a common exam trap.",
            "Indian civil-service ethics must address both frameworks.",
        ),
        "verdict": "Know both lists and where they diverge to avoid a false equivalence trap.",
        "answer_use": "Use the overlap and gaps to answer any Nolan or foundational-values comparison.",
    },
    {
        "title": "11. Values under pressure: an integration map",
        "structural_type": "hub-spoke",
        "nodes": (
            "Discretion creates the space in which integrity is tested.",
            "Political transition tests non-partisanship most sharply.",
            "Election duty tests impartiality under direct political pressure.",
            "Welfare delivery tests compassion alongside impartial rule-application.",
            "Gender-specific challenges test impartiality reflexively.",
            "Service-delivery redesign tests compassion as operational output.",
            "Enabler-regulator framing tests dedication and objectivity together.",
            "Each value interacts with others under realistic administrative stress.",
        ),
        "verdict": "Foundational values are tested in combination, not in isolation.",
        "answer_use": "Use to show multi-value interaction in any pressure-scenario question.",
    },
    {
        "title": "12. PYQ and answer synthesis",
        "structural_type": "exam-synthesis-rail",
        "nodes": (
            "2025 Q5(b) tested enabler-facilitator with specific measures.",
            "2025 Q4(a) tested objectivity and critical thinking in welfare schemes.",
            "2025 Q5(a) tested devotion to duty and personal fulfilment.",
            "2024 Q6(a) tested gender-specific challenges and probity.",
            "2018-2021 tested Nolan principles, Buffett, and non-partisanship.",
            "Name the value precisely rather than listing adjectives.",
            "Show the institutional mechanism that operationalises the value.",
            "Close with a qualified verdict acknowledging a real limitation.",
        ),
        "verdict": "The highest-scoring answer moves from value to pressure to mechanism to example to limit.",
        "answer_use": "Use as the revision checklist before any foundational-values PYQ attempt.",
    },
)

CURRENT_ANCHOR = {
    "title": "Mission Karmayogi: competency-based capacity building and AI-enabled delivery",
    "verified_facts": (
        "NPCSCB (Mission Karmayogi) was approved by Cabinet on 2 September 2020.",
        "Capacity Building Commission was constituted on 1 April 2021.",
        "Karmayogi Competency Model (KCM) aligns roles with required competencies, embeds competencies in training, and supports accountability, role-fit and continuous development (CBC KCM page).",
        "Ministries and Departments shift from rule-based to role-based thinking under the KCM framework (CBC KCM page).",
        "AI Sarthi and AI Tutor were showcased at the IndiaAI Impact Summit (16-20 February 2026) for role-based personalised learning, multilingual transcripts/subtitles and AI-enabled competency assessment (CBC IndiaAI page).",
        "DoPT iGOT page states competency-driven capacity building, an indigenous framework, lifelong learning records, AI-enabled competency assessment and accountability/transparency.",
    ),
    "administrative_link": (
        "Use Mission Karmayogi to show how foundational values are institutionalised through "
        "the Karmayogi Competency Model, role-based learning and AI-enabled delivery. Cite the "
        "KCM framework and AI tools as evidence of continuing institutional investment."
    ),
    "limit": (
        "Learning architecture and AI-enabled delivery demonstrate institutional design, not "
        "verified ethical internalisation. Do not assert a general APAR linkage without a "
        "service-specific DoPT order. AI-enabled personalisation is a delivery improvement, "
        "not proof of values adoption."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://cbc.gov.in/mission-karmayogi-showcases-ai-enabled-capacity-building-civil-servants-indiaai-impact-summit-2026",
    "https://cbc.gov.in/karmayogi-competency-model-kcm",
    "https://trgdiv.dopt.gov.in/igotmk/",
    "https://igotkarmayogi.gov.in/",
    "https://dopt.gov.in/schemes/national-programme-civil-services-and-capacity-building-npcscb-mission-karmayogi",
)

SOURCE_CAVEAT = (
    "Use the local Basic and Advanced owners as the controlling source. The Buffett "
    "integrity-intelligence-energy line is introduced by Buffett as something 'somebody once said'; "
    "its traceable published form is a 1994 Omaha World-Herald report of his 1993 Columbia Business "
    "School remarks. Do not assert original authorship. Robert Wade's transfer-industry study is "
    "cited via ARC 9.4 (the original is Wade's 'The System of Administrative and Political "
    "Corruption: Canal Irrigation in South India', 1982). Mission Karmayogi iGOT statistics evolve; "
    "always date-qualify any figure used. Do not claim a general APAR linkage without a "
    "service-specific DoPT order. The Nolan principles are cited from the UK Committee on Standards "
    "in Public Life (1995) via ARC 2.2.5; the GS-IV syllabus list is broader and not identical."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: Aptitude (capacity) differs from attitude (evaluative stance) and value "
    "(cross-situational standard). Six foundational values: integrity, impartiality/non-partisanship, "
    "objectivity, dedication, empathy/compassion, tolerance. Integrity is the hardest to test at "
    "entry; proxies include asset declarations, conflict disclosures and random inspections. "
    "Impartiality permits needs-based differentiation if criteria are transparent and rule-based. "
    "Non-partisanship is structurally threatened by discretionary transfers (ARC 9.4, Robert Wade "
    "AP study); safeguarded by Civil Services Board mechanisms and fixed tenure norms (Fifth Pay "
    "Commission: 3-5 years). Compassion must be operationalised as service design: doorstep "
    "delivery, vernacular access, simplified forms. Compassion without transparent criteria is "
    "indistinguishable from favouritism. Enabler-regulator is calibrated, not either-or: facilitate "
    "legitimate activity, regulate through risk-based post-facto oversight. Nolan 7 (selflessness, "
    "integrity, objectivity, accountability, openness, honesty, leadership) overlap with but are "
    "not identical to GS-IV list. Mission Karmayogi (NPCSCB, 2 Sep 2020): KCM aligns roles with "
    "competencies; iGOT supports lifelong learning; AI Sarthi/Tutor for personalised delivery. "
    "Learning architecture is not ethical proof. Buffett's integrity-intelligence-energy: "
    "he introduced the line as somebody once said (1994 Omaha World-Herald via 1993 Columbia BS). "
    "Tolerance anchored in Art 51A(e) and constitutional morality. Answer spine: name value -> "
    "pressure scenario -> institutional safeguard -> Indian example -> limitation -> verdict."
)
