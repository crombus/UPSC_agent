"""Learner-v2 source data: Ethics Topic 03, Attitude: Content, Structure and Persuasion."""

SESSION_TITLES = (
    "What attitude is: the ABC model and key distinctions",
    "How attitudes form and change through experience and persuasion",
    "Indian administrative applications of attitude and persuasion",
    "Must-know facts for prelims on attitude and persuasion",
    "Traps that cost marks in attitude questions",
    "PYQ application: what the examiner actually tested",
    "Mains angles and answer architecture for attitude questions",
    "Selectable evidence units for attitude answers",
    "Moral attitude versus political attitude in civil service",
    "Directive decoding, study links, and consolidated revision",
)

SESSION_GROUPS = (
    (1, 2),
    (3,),
    (4,),
    (5,),
    (6,),
    (7,),
    (8,),
    (9, 10),
    (11,),
    (12, 13),
)

MCQ_ITEMS = (
    # Group 1: ABC model and definitions
    {
        "label": "Attitude is object-specific, not a general life principle",
        "statement": (
            "An attitude is a relatively stable evaluative disposition directed toward a "
            "specific object, person or idea, comprising cognitive, affective and behavioural "
            "components; it is narrower than a value, which operates across situations and is "
            "not tied to any single object."
        ),
        "scenario_a": (
            "A district official strongly favours a particular watershed programme but remains "
            "indifferent to an unrelated literacy drive. Which concept explains why her stance "
            "toward each programme differs despite her broad commitment to public welfare?"
        ),
        "scenario_b": (
            "A trainee declares honesty as a lifelong principle yet shows no evaluative stance "
            "toward a new digital-attendance system. Which distinction separates a cross-"
            "situational value from an object-directed attitude?"
        ),
        "group": "ABC model and definitions",
    },
    {
        "label": "The cognitive component carries beliefs, not feelings",
        "statement": (
            "The cognitive component of attitude refers to the beliefs, knowledge and "
            "informational claims a person holds about the attitude object; it supplies "
            "the factual basis on which evaluative judgement rests and is distinct from the "
            "emotional charge that constitutes the affective component."
        ),
        "scenario_a": (
            "A revenue officer believes that RTI requests increase workload and reduce "
            "efficiency. She has not yet developed resentment toward applicants. Which "
            "attitudinal component is currently engaged and which remains dormant?"
        ),
        "scenario_b": (
            "A health inspector reads research showing that street-food vendors follow "
            "safe practices in most sampled cities. His factual beliefs change, but his "
            "emotional discomfort persists. Which two components are pulling in opposite "
            "directions?"
        ),
        "group": "ABC model and definitions",
    },
    {
        "label": "The affective component carries emotional charge",
        "statement": (
            "The affective component of attitude is the emotional response, whether "
            "positive or negative, attached to the attitude object; it can persist even "
            "when new factual information contradicts the cognitive component, making "
            "training that targets only beliefs insufficient for durable attitude change."
        ),
        "scenario_a": (
            "After attending a sensitisation workshop a block officer intellectually "
            "accepts that tribal applicants deserve equal service, yet continues to feel "
            "discomfort during face-to-face interactions. Which component explains the "
            "residual resistance?"
        ),
        "scenario_b": (
            "A municipal engineer dislikes a community but cannot articulate any factual "
            "reason for the dislike. Which attitudinal component is dominant and which is "
            "weak or absent?"
        ),
        "group": "ABC model and definitions",
    },
    {
        "label": "The behavioural component is a tendency, not a guarantee",
        "statement": (
            "The behavioural or conative component of attitude is the predisposition to "
            "act in a certain way toward the attitude object; it does not guarantee actual "
            "behaviour because situational pressures, institutional incentives and social "
            "norms can override the predisposition and produce an attitude-behaviour gap."
        ),
        "scenario_a": (
            "A sub-divisional magistrate privately intends to report a senior's misconduct "
            "but remains silent when the departmental meeting begins. Which concept "
            "explains the gap between intention and inaction?"
        ),
        "scenario_b": (
            "An officer who dislikes a transfer policy still complies because career "
            "incentives outweigh personal resistance. Which feature of the behavioural "
            "component does this illustrate?"
        ),
        "group": "ABC model and definitions",
    },
    # Group 2: Attitude formation and persuasion
    {
        "label": "Attitudes form through experience, learning and reinforcement",
        "statement": (
            "Attitudes form through direct experience with an object, social learning from "
            "family, peers and media, and reinforcement through repeated positive or negative "
            "outcomes; their origin explains why two officials in the same office can hold "
            "opposite evaluations of the same beneficiary community."
        ),
        "scenario_a": (
            "A newly posted collector who grew up in a rural area readily trusts local "
            "panchayat leaders, whereas her predecessor from an urban background was "
            "skeptical. Which formation pathway best explains the divergence?"
        ),
        "scenario_b": (
            "An officer who is praised every time she clears files quickly develops a "
            "positive stance toward speed over thoroughness. Which formation mechanism "
            "is operating and what risk does it carry?"
        ),
        "group": "Formation and persuasion",
    },
    {
        "label": "Hovland-Yale persuasion rests on source, message and audience",
        "statement": (
            "The Hovland-Yale attitude-change approach identifies the communicator's "
            "credibility, the message's content and framing, and the audience's "
            "predispositions as the three original persuasion variables; the channel or "
            "medium is a later addition from wider communication research and was not part "
            "of the original 1953 Yale triad."
        ),
        "scenario_a": (
            "A state vaccination campaign uses a respected local ASHA worker to deliver "
            "simplified messages in the vernacular language to hesitant parents. Which "
            "Hovland-Yale variables are being activated and which one is absent from the "
            "original model?"
        ),
        "scenario_b": (
            "A central ministry issues a detailed technical circular on maternal health "
            "to illiterate beneficiaries through a formal gazette notification. Which "
            "persuasion variable has been ignored and why does the campaign likely fail?"
        ),
        "group": "Formation and persuasion",
    },
    {
        "label": "Cognitive dissonance creates three resolution paths",
        "statement": (
            "When behaviour contradicts a held attitude, cognitive dissonance produces "
            "psychological discomfort that can be resolved by changing the attitude to "
            "match behaviour, changing future behaviour to match the attitude, or adding "
            "a self-justifying cognition; the third path is the ethically dangerous one "
            "because it enables rationalisation of misconduct."
        ),
        "scenario_a": (
            "An officer who values transparency is directed to withhold a routine file "
            "under a stretched RTI exemption. She convinces herself the exemption is "
            "broader than it actually is. Which dissonance resolution path has she taken "
            "and why is it ethically risky?"
        ),
        "scenario_b": (
            "A procurement officer accepts a first small gift and then reasons that "
            "everyone does it, so it must be acceptable. Which Festinger pathway explains "
            "how small compromises consolidate into settled corrupt practice?"
        ),
        "group": "Formation and persuasion",
    },
    {
        "label": "The attitude-behaviour gap shows that good attitudes are necessary but insufficient",
        "statement": (
            "LaPiere's 1934 study demonstrated that a general stated attitude predicts a "
            "specific act poorly; institutional design through binding external constraints "
            "such as RTI mandates, whistleblower protection and audit trails exists precisely "
            "because attitude alone cannot guarantee consistent ethical behaviour."
        ),
        "scenario_a": (
            "In an annual ethics survey, every officer in a revenue department declares "
            "commitment to transparency, yet RTI compliance rates remain below fifty "
            "per cent. Which concept explains the divergence and what institutional "
            "response is indicated?"
        ),
        "scenario_b": (
            "A district training programme improves officers' pro-citizen attitudes but "
            "leaves the opaque manual approval system unchanged. Why might service-delivery "
            "improvements be temporary despite genuine attitude change?"
        ),
        "group": "Formation and persuasion",
    },
    # Group 3: Persuasion ethics and social media
    {
        "label": "Persuasion is ethically distinct from manipulation and propaganda",
        "statement": (
            "Persuasion respects audience autonomy and relies on truthful argument; "
            "manipulation exploits cognitive biases or asymmetric information while "
            "concealing intent; propaganda uses repetition and emotional framing at scale, "
            "often state-sponsored, to bypass critical evaluation rather than engage it."
        ),
        "scenario_a": (
            "A district administration runs a community-leader-led campaign with verified "
            "facts to change attitudes toward girl-child education. A neighbouring district "
            "uses fear-based imagery without disclosing government sponsorship. Which "
            "campaign crosses the persuasion-propaganda boundary and why?"
        ),
        "scenario_b": (
            "A social-media cell creates emotionally charged posts about a welfare scheme "
            "using undisclosed paid influencers and suppresses critical comments. Which "
            "ethical line has been crossed even though the underlying policy goal may be "
            "legitimate?"
        ),
        "group": "Persuasion ethics and social media",
    },
    {
        "label": "Algorithmic targeting changes the audience variable at unprecedented scale",
        "statement": (
            "Social-media platforms operationalise persuasion variables at a scale the "
            "Hovland-Yale model did not anticipate: the audience variable is now "
            "algorithmically segmented through micro-targeting, which can shade legitimate "
            "persuasion into manipulation by exploiting individual cognitive biases "
            "invisible to the audience itself."
        ),
        "scenario_a": (
            "A political party uses voter data to send contradictory health-scheme messages "
            "to different demographic segments on the same day. Which Hovland-Yale variable "
            "has been transformed by digital technology and what ethical problem does this "
            "create?"
        ),
        "scenario_b": (
            "A state uses algorithmic recommendation to promote its vaccination campaign "
            "with transparent sponsorship labels and factual content. Does this cross the "
            "ethical boundary and what test determines the answer?"
        ),
        "group": "Persuasion ethics and social media",
    },
    {
        "label": "Legitimate government campaigns rest on truthfulness and non-coercion",
        "statement": (
            "Public information campaigns such as financial literacy drives, sanitation "
            "behaviour change under Swachh Bharat, and digital-payment adoption are "
            "legitimate state persuasion exercises whose ethical standing depends on "
            "truthful content, transparent sponsorship and freedom from coercion rather "
            "than on the mere fact that a government is communicating."
        ),
        "scenario_a": (
            "A gram panchayat uses wall paintings with local-language facts about "
            "handwashing benefits, names the sponsoring ministry, and invites questions "
            "at weekly meetings. Which persuasion criteria make this ethically "
            "defensible?"
        ),
        "scenario_b": (
            "A block administration withholds ration cards from families that refuse to "
            "attend a sanitation rally. Even though the sanitation goal is legitimate, "
            "which ethical condition has been violated?"
        ),
        "group": "Persuasion ethics and social media",
    },
    {
        "label": "The same digital channel enables both legitimate persuasion and disinformation",
        "statement": (
            "Social media raises a distinctive GS-IV dilemma because the same channel "
            "used for legitimate public information campaigns can be used for "
            "disinformation and political manipulation; the ethical test is transparency "
            "of intent and respect for audience autonomy rather than the technology "
            "itself."
        ),
        "scenario_a": (
            "A health ministry uses short videos with doctor endorsements and sponsorship "
            "labels to counter vaccine misinformation, while a private network spreads "
            "deepfake testimonials on the same platform. Which factor distinguishes "
            "the two ethically?"
        ),
        "scenario_b": (
            "A state bans all social-media health communication to prevent "
            "misinformation, thereby also blocking verified government advisories. "
            "Which ethical nuance has the blanket ban missed?"
        ),
        "group": "Persuasion ethics and social media",
    },
    # Group 4: Moral versus political attitude
    {
        "label": "Moral attitude judges right and wrong; political attitude evaluates parties and power",
        "statement": (
            "A moral attitude is an evaluative stance toward what is right or wrong, "
            "grounded in ethical reasoning and applicable across contexts; a political "
            "attitude is a stance toward a specific party, ideology or contest for "
            "power, which is by design partisan and does not claim universal applicability."
        ),
        "scenario_a": (
            "A collector refuses to fast-track a ruling-party worker's land file "
            "because the application lacks statutory documents. She applies the same "
            "rule to an opposition supporter's file. Which type of attitude is she "
            "exercising and which is she bracketing?"
        ),
        "scenario_b": (
            "An officer openly criticises a welfare policy because it was announced "
            "by the opposition when they were in power, not because of any procedural "
            "or ethical deficiency. Which attitudinal category has improperly entered "
            "official conduct?"
        ),
        "group": "Moral versus political attitude",
    },
    {
        "label": "CCS Conduct Rules require behavioural non-partisanship, not mental blankness",
        "statement": (
            "Central Civil Services Conduct Rules 1964 restrict a government servant's "
            "participation in politics and demonstrations under Rule 5 and election "
            "canvassing under Rule 7, operationalising political neutrality; the "
            "obligation covers official conduct and public activity, not the private "
            "holding of a political opinion or the exercise of one's vote."
        ),
        "scenario_a": (
            "A senior IAS officer votes in a general election and privately discusses "
            "policy preferences with family members but never lets party preference "
            "influence file disposal. Has she violated the non-partisanship obligation?"
        ),
        "scenario_b": (
            "A block development officer distributes pamphlets for a political party "
            "during office hours and uses official vehicles for rally logistics. Which "
            "specific Conduct Rules has he breached and what is the ethical basis of "
            "the prohibition?"
        ),
        "group": "Moral versus political attitude",
    },
    {
        "label": "Policy awareness is duty, not partisanship",
        "statement": (
            "A civil servant is expected to understand the political executive's policy "
            "priorities, brief ministers candidly including with unwelcome advice, and "
            "implement lawfully enacted policy faithfully; this becomes partisan only "
            "when the officer's personal preference for a party rather than law and "
            "record drives a discretionary decision."
        ),
        "scenario_a": (
            "A secretary prepares a candid note advising against a proposed scheme "
            "on grounds of fiscal risk and legal infirmity, then implements the "
            "minister's final lawful decision. Is this constructive dissent or "
            "political disloyalty?"
        ),
        "scenario_b": (
            "A district magistrate accelerates files of the ruling party's "
            "preferred contractors while delaying others, claiming she is merely "
            "implementing government priorities. Which test distinguishes lawful "
            "policy implementation from partisan conduct?"
        ),
        "group": "Moral versus political attitude",
    },
    {
        "label": "Moral objection to a lawful policy is not political attitude",
        "statement": (
            "An officer who raises a reasoned ethical or legal objection to an "
            "instruction in a reasoned written note is exercising moral judgement "
            "about propriety and legality, not political preference, provided the "
            "objection is framed in terms of law, rules and public interest rather "
            "than partisan alignment."
        ),
        "scenario_a": (
            "A sub-divisional magistrate records in a written note that a proposed demolition "
            "drive lacks mandatory notice under municipal law and may harm vulnerable "
            "residents. Is this principled objection or political obstruction?"
        ),
        "scenario_b": (
            "An officer opposes a policy solely because it was proposed by a party she "
            "personally dislikes, without citing any legal, procedural or public-interest "
            "ground. Which boundary between moral and political attitude has she crossed?"
        ),
        "group": "Moral versus political attitude",
    },
    # Group 5: Attitude strength, malleability and institutional closure
    {
        "label": "Attitude strength improves but does not guarantee behavioural prediction",
        "statement": (
            "Attitudes held with high certainty, personal relevance and frequent rehearsal "
            "resist persuasion and predict behaviour better than weakly held attitudes; "
            "however, even strong attitudes can be overridden by intense situational "
            "pressure, making institutional safeguards necessary even for committed officers."
        ),
        "scenario_a": (
            "A senior officer with decades of anti-corruption commitment remains silent "
            "when a powerful political figure pressures her during a transfer posting. "
            "Which concept explains why even a strong attitude did not translate into "
            "resistant behaviour?"
        ),
        "scenario_b": (
            "A newly recruited officer with only classroom exposure to integrity quickly "
            "abandons her stance under peer pressure to accept facilitation payments. "
            "Which feature of attitude strength explains her vulnerability?"
        ),
        "group": "Attitude strength and institutional closure",
    },
    {
        "label": "William James's teaching affirms attitude malleability, not determinism",
        "statement": (
            "The proposition that a person can alter life by altering attitudes captures "
            "the malleability of attitude: it is not fixed temperament but a chosen, "
            "revisable stance that can be reshaped through reflection, training and "
            "experience; it must not be misread as claiming that attitude change alone "
            "mechanically determines outcomes."
        ),
        "scenario_a": (
            "A probationer initially treats a difficult rural posting as punishment "
            "but reframes it as a learning opportunity after field immersion and "
            "mentoring. Which aspect of the malleability principle is illustrated "
            "and what structural support made the shift possible?"
        ),
        "scenario_b": (
            "A department tells drought-affected farmers that they can overcome water "
            "scarcity by changing their attitude. Which misapplication of the "
            "malleability principle does this represent?"
        ),
        "group": "Attitude strength and institutional closure",
    },
    {
        "label": "Persuasion-based reform is slower but more durable than rule-based constraint",
        "statement": (
            "Attitude change through persuasion is slower and less certain than "
            "rule-based reform through binding institutional constraints, but more "
            "durable once internalised; over-reliance on institutional constraint "
            "without attitude change risks purely compliance-based conduct that reverts "
            "once monitoring relaxes."
        ),
        "scenario_a": (
            "A department installs CCTV and strict attendance monitoring; absenteeism "
            "drops immediately but returns to previous levels when cameras malfunction. "
            "Which limitation of purely institutional constraint does this illustrate?"
        ),
        "scenario_b": (
            "A Mission Karmayogi behavioural-competency module uses simulation and "
            "case-based learning over six months, producing slower but lasting change "
            "in citizen-facing conduct. Which trade-off between persuasion and "
            "constraint is demonstrated?"
        ),
        "group": "Attitude strength and institutional closure",
    },
    {
        "label": "Training must target affective, not only cognitive, component for durable change",
        "statement": (
            "Civil-service training that targets only the cognitive component through "
            "lectures and manuals is insufficient for durable attitude change; "
            "simulation-based and case-based learning that engages the affective "
            "component through empathetic exposure is necessary to reshape long-held "
            "biases toward marginalised communities."
        ),
        "scenario_a": (
            "A foundation-course module sends probationers to live in a tribal "
            "settlement for a week, interact with families and document access "
            "barriers. Which attitudinal component does immersive experience target "
            "that a classroom lecture cannot reach?"
        ),
        "scenario_b": (
            "A training institute tests officers only on their knowledge of "
            "anti-discrimination law and declares bias eliminated. Which gap in "
            "the ABC model does this assessment miss?"
        ),
        "group": "Attitude strength and institutional closure",
    },
    # Group 6: Positive mindset in rule interpretation
    {
        "label": "Positive mindset reads rules with their public purpose",
        "statement": (
            "A positive mindset interprets rules and regulations with their public "
            "purpose in view, applying them to enable fair access and citizen welfare; "
            "a negative mindset treats rules chiefly as obstacles, sources of power "
            "or shields against responsibility, producing delay, denial and extraction."
        ),
        "scenario_a": (
            "During disability-certificate verification, an officer helps an applicant "
            "correct a curable document error and records the reasoned decision rather "
            "than mechanically rejecting the claim. Which mindset is demonstrated?"
        ),
        "scenario_b": (
            "A licensing clerk exploits an ambiguous clause to demand informal payment "
            "for processing a routine renewal that the applicant is entitled to receive. "
            "Which attitudinal stance toward rules makes this extraction possible?"
        ),
        "group": "Positive mindset and rule interpretation",
    },
    {
        "label": "Positive attitude under stress preserves judgement and citizen trust",
        "statement": (
            "A positive attitude is an essential characteristic of a civil servant "
            "under stress because it preserves analytical judgement, prevents panic "
            "from amplifying a crisis, and maintains citizen trust in the "
            "administration's competence and fairness during difficult situations."
        ),
        "scenario_a": (
            "During a communal tension incident a sub-divisional magistrate remains "
            "calm, verifies rumours before acting, deploys peace committees and "
            "communicates transparently with both communities. Which attitudinal "
            "quality prevents administrative paralysis?"
        ),
        "scenario_b": (
            "A collector facing a flood emergency panics, issues contradictory "
            "orders and blames subordinates publicly. Which consequence of a "
            "negative attitude under stress is most damaging to the relief operation?"
        ),
        "group": "Positive mindset and rule interpretation",
    },
    {
        "label": "Attitude toward vulnerable groups shapes discretionary service quality",
        "statement": (
            "A field officer's negative attitude toward a beneficiary community, "
            "formed through biased social conditioning, can distort service delivery "
            "even where rules are formally neutral; training must therefore target "
            "the affective component through immersive exposure rather than relying "
            "on rule-knowledge alone."
        ),
        "scenario_a": (
            "A tehsildar consistently delays mutation applications from a scheduled "
            "caste hamlet while processing upper-caste applications promptly, even "
            "though the same rules apply. Which attitudinal component most likely "
            "drives the differential treatment?"
        ),
        "scenario_b": (
            "A district sends a welfare officer to live in a tribal settlement for "
            "a week before her posting begins. Which component of attitude is this "
            "immersive intervention designed to reshape?"
        ),
        "group": "Positive mindset and rule interpretation",
    },
    {
        "label": "Purposive interpretation avoids both literalism and arbitrary benevolence",
        "statement": (
            "A sound administrative reading of rules avoids obstructive literalism "
            "that denies citizens entitled services and arbitrary benevolence that "
            "bypasses mandatory conditions for favoured applicants; the positive "
            "mindset interprets with public purpose while remaining accountable "
            "to law, published criteria and equal treatment."
        ),
        "scenario_a": (
            "A municipal officer waives a mandatory safety inspection for a "
            "school run by a local dignitary, citing compassion for children. "
            "Which limit on positive interpretation has been crossed?"
        ),
        "scenario_b": (
            "A licensing authority mechanically rejects a renewal because one "
            "supporting document has a minor typographical error that does not "
            "affect eligibility. Which interpretive deficiency does the "
            "attitude-behaviour gap framework identify here?"
        ),
        "group": "Positive mindset and rule interpretation",
    },
)

PYQS = (
    {
        "year": 2025,
        "question": (
            'Given below are three quotations of great thinkers. What do each '
            'of these quotations convey to you in the present context? 3-(b) '
            '"The greatest discovery of my generation is that a human being can '
            'alter his life by altering his attitudes." - William James '
            '(Answer in 150 words)'
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: "
            "books/mains/UPSC Mains 2025 GS Paper 4.pdf, Q3(b). "
            "Widely attributed to William James but not traceable to his "
            "writings; popularised by Norman Vincent Peale (1952). "
            "Cross-ownership: primarily routed to Topics 06/07 "
            "(Indian/Western Moral Thinkers) in the PYQ ledger; "
            "this owner has a strong cross-link claim via the "
            "malleability-of-attitude concept in Basic Section 3.5 and 7."
        ),
        "answer": (
            "The proposition conveys that attitudes are not permanently fixed: "
            "conscious reflection, learning and repeated practice can reshape how "
            "a person evaluates situations and therefore how that person acts. In "
            "public service, this matters because an officer's attitude toward "
            "citizens, marginalised groups and difficult postings shapes the quality "
            "of discretionary service delivery.\n\n"
            "A probationer initially treating a remote rural posting as punishment "
            "may, through field immersion, mentoring and feedback, come to recognise "
            "local knowledge, learn the language and redesign welfare-access "
            "procedures. The changed attitude does not alter material constraints by "
            "wish alone; it changes attention, effort and willingness to collaborate. "
            "Mission Karmayogi's behavioural-competency modules, which use simulation "
            "and case-based learning, institutionalise precisely this kind of targeted "
            "attitude reshaping.\n\n"
            "The proposition must not become victim-blaming. Poverty, discrimination, "
            "administrative opacity and inadequate staffing cannot be solved by asking "
            "citizens or employees merely to think positively. Structural reform, lawful "
            "entitlements and institutional accountability remain indispensable.\n\n"
            "There is also a provenance caution: the exact sentence is widely attributed "
            "to William James but is not traceable to his published writings; it was "
            "popularised by Norman Vincent Peale. The answer should analyse the "
            "proposition without inventing a James citation. The verdict is that "
            "reflective attitude change is a real ethical resource when paired with "
            "fair institutions and concrete action."
        ),
    },
    {
        "year": 2025,
        "question": (
            "In the present digital age, social media has revolutionised our "
            "way of communication and interaction. However, it has raised "
            "several ethical issues and challenges. Describe the key ethical "
            "dilemmas in this regard. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact English wording from locally held official PDF: "
            "books/mains/UPSC Mains 2025 GS Paper 4.pdf, Q1(a). "
            "Cross-ownership: primarily routed to Topic 13 "
            "(Emerging Ethics: Technology, AI and Environment) in the PYQ "
            "ledger; this owner has a strong cross-link claim because "
            "social media is fundamentally an attitude-persuasion-at-scale "
            "problem transforming the Hovland-Yale audience variable."
        ),
        "answer": (
            "Social media raises several interconnected ethical dilemmas for "
            "public administration and society. First, privacy and data "
            "harvesting: platforms collect personal data at scale, often "
            "without meaningful informed consent, creating conflicts with the "
            "Digital Personal Data Protection Act, 2023. Second, misinformation "
            "and deepfakes: algorithmically amplified false content can reshape "
            "public attitudes faster than corrections can reach the same "
            "audience. Third, echo chambers and polarisation: recommendation "
            "algorithms create self-reinforcing information environments that "
            "narrow deliberative capacity.\n\n"
            "Fourth, addictive design: attention-capture mechanisms exploit "
            "cognitive vulnerabilities, raising questions about platform "
            "responsibility. Fifth, anonymity and accountability: online "
            "anonymity enables hate speech and communal incitement while "
            "weakening deterrence. Sixth, the state's own use of the same "
            "channel: government social-media campaigns that use emotionally "
            "manipulative messaging without disclosing sponsorship shade from "
            "legitimate persuasion toward propaganda.\n\n"
            "The underlying ethical test, drawn from attitude-persuasion "
            "theory, is transparency of intent and respect for audience "
            "autonomy. Technology itself is ethically neutral; its governance "
            "requires content-moderation frameworks, algorithmic transparency "
            "mandates and due-process safeguards that distinguish legitimate "
            "public information from manipulation."
        ),
    },
    {
        "year": 2020,
        "question": (
            "Neutral rendering of the routed demand: Discuss why a positive "
            "attitude is an essential characteristic of a civil servant "
            "especially under conditions of stress."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand from 2020 GS-IV Q4(b), neutral rendering "
            "from the PYQ ledger (_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md "
            "line 291). Routed to this owner. Not claimed as verbatim "
            "wording in this data file."
        ),
        "answer": (
            "A positive attitude is essential under stress because it preserves "
            "analytical judgement, prevents panic from compounding a crisis, and "
            "maintains citizen trust in the administration's competence and "
            "fairness. Stress narrows attention and tempts hasty, arbitrary "
            "action; a constructive mental orientation keeps the officer focused "
            "on evidence, lawful procedure and the welfare of affected persons.\n\n"
            "During a flood emergency, for example, a collector with a positive "
            "attitude verifies damage reports before allocating relief, "
            "communicates uncertainty honestly rather than issuing false "
            "assurances, coordinates with district health and police teams, and "
            "records decisions for later review. A negative attitude under the "
            "same pressure may produce blame-shifting, contradictory orders and "
            "favouritism in distribution.\n\n"
            "The positive attitude needed is not naive optimism. It is a "
            "disciplined evaluative stance that treats obstacles as problems to "
            "be solved within rules rather than excuses for inaction or "
            "arbitrariness. It aligns with the ABC model: the cognitive "
            "component frames the crisis as manageable, the affective component "
            "sustains empathy, and the behavioural component translates both "
            "into timely, fair action.\n\n"
            "However, attitude alone is insufficient. Institutional support "
            "through clear SOPs, adequate staffing, transparent criteria and "
            "grievance mechanisms must close the attitude-behaviour gap so that "
            "the officer's positive orientation translates into consistent "
            "ethical conduct even when pressure intensifies."
        ),
    },
    {
        "year": 2021,
        "question": (
            "Neutral rendering of the routed demand: Discuss how to build a "
            "suitable attitude needed for a public servant."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand from 2021 GS-IV Q4(a), neutral rendering "
            "from the PYQ ledger (_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md "
            "line 308). Routed to this owner. Not claimed as verbatim "
            "wording in this data file."
        ),
        "answer": (
            "Building a suitable attitude for public service requires targeting "
            "all three components of the ABC model systematically. The cognitive "
            "component is addressed through foundational training that explains "
            "constitutional values, citizens' rights, service-delivery standards "
            "and the ethical reasoning behind rules. The affective component "
            "requires experiential learning: field immersion in underserved "
            "communities, structured interaction with beneficiaries, and "
            "simulation exercises that generate empathy and discomfort with "
            "exclusion.\n\n"
            "The behavioural component is built through supervised practice: "
            "handling real citizen grievances under mentorship, recording "
            "reasoned decisions, receiving feedback and correcting bias. "
            "Persuasion principles apply here: credible trainers with field "
            "experience are more effective than abstract lectures, and "
            "peer-group discussion strengthens internalisation.\n\n"
            "Mission Karmayogi's iGOT platform institutionalises continuous "
            "learning by linking role-based competencies to behavioural "
            "modules. However, training exposure alone does not guarantee "
            "internalisation. Institutional reinforcement through transparent "
            "work routines, ethical leadership, accountability mechanisms and "
            "protection of honest officers is necessary to close the "
            "attitude-behaviour gap.\n\n"
            "The process is ongoing, not a one-time induction event. Periodic "
            "refresher training, peer accountability and regular ethics review "
            "help prevent the gradual erosion of positive attitudes through "
            "cynicism, burnout or rationalisation of small compromises."
        ),
    },
    {
        "year": 2022,
        "question": (
            "Neutral rendering of the routed demand: Discuss how a positive "
            "and a negative mindset can lead to different interpretations of "
            "rules and regulations."
        ),
        "marks": 10,
        "source_note": (
            "Older routed demand from 2022 GS-IV Q2(a), neutral rendering "
            "from the PYQ ledger (_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md "
            "line 323). Routed to this owner. Not claimed as verbatim "
            "wording in this data file."
        ),
        "answer": (
            "A mindset shapes how an official sees the purpose of a rule. A "
            "positive mindset treats regulation as an instrument to secure "
            "fairness, safety and public trust; a negative mindset treats it "
            "chiefly as an obstacle, a source of discretionary power, or a "
            "shield against responsibility. The difference becomes ethical "
            "when interpretation affects citizens' rights and access.\n\n"
            "A constructive officer reads a rule with its public purpose, "
            "applies it consistently and explains any refusal with reasons. A "
            "cynical officer may exploit ambiguity to delay service, demand "
            "informal payment or deny reasonable assistance by saying the file "
            "cannot move. During disability-certificate verification, a "
            "facilitative officer helps an applicant correct a curable document "
            "error and records the reasoned decision; a negative one "
            "mechanically rejects the claim despite available verification and "
            "no risk to legality. The former respects both rule and citizen "
            "dignity.\n\n"
            "Positive interpretation is not permission to ignore mandatory "
            "conditions or grant favouritism. Compassion must operate within "
            "law, published criteria and equal treatment. The sound "
            "administrative stance is therefore purposive but accountable: it "
            "avoids both obstructive literalism and arbitrary benevolence, and "
            "keeps the citizen-government interface lawful, responsive and "
            "reviewable."
        ),
    },
    {
        "year": 2024,
        "question": (
            "Neutral rendering of the cross-linked demand: Discuss the "
            "significance of Mission Karmayogi in building behavioural "
            "competencies and reshaping attitudes of civil servants toward "
            "citizen-centred governance."
        ),
        "marks": 10,
        "source_note": (
            "Cross-linked demand synthesised from 2024 GS-IV Q6(b) "
            "(Mission Karmayogi). Primarily routed to Topic 04 "
            "(Aptitude and Foundational Values); this owner contributes "
            "the attitude-formation and training-design angle. "
            "Not claimed as verbatim wording."
        ),
        "answer": (
            "Mission Karmayogi's National Programme for Civil Services "
            "Capacity Building is significant for attitude reshaping because "
            "it shifts training focus from rules memorisation to role-based "
            "behavioural competencies at the citizen-government interface. "
            "This directly targets the cognitive and affective components of "
            "attitude through iGOT platform modules that use case studies, "
            "simulations and citizen-interaction scenarios.\n\n"
            "The programme's approach reflects sound persuasion principles: "
            "credible trainers with field experience deliver contextualised "
            "content to a receptive audience of serving officers, using "
            "appropriate digital and classroom channels. The shift from "
            "rules-based to roles-based orientation means that an officer "
            "learns not just what a regulation says but how to apply it "
            "empathetically and fairly in diverse citizen-facing situations.\n\n"
            "However, course completion statistics do not prove attitudinal "
            "internalisation. An officer may perform well on a module yet "
            "revert to old patterns under institutional pressure, peer norms "
            "or workload stress. The attitude-behaviour gap persists unless "
            "training is reinforced by ethical leadership, transparent work "
            "routines, citizen feedback mechanisms and protection of honest "
            "officers. Mission Karmayogi is therefore a valuable institutional "
            "channel for attitude change, not a certificate of ethical "
            "governance in every service setting."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Discuss why a positive attitude, though necessary, is not a "
            "sufficient condition for ethical conduct in civil service. "
            "Illustrate with the concept of the attitude-behaviour gap. "
            "(Answer in 150 words)"
        ),
        "answer": (
            "A positive attitude provides a civil servant with constructive "
            "orientation toward duty, fairness and citizen welfare. It shapes "
            "how rules are interpreted, how crises are managed and how "
            "vulnerable persons are treated. In this sense it is necessary for "
            "ethical administration.\n\n"
            "However, LaPiere's 1934 study established that stated attitudes "
            "predict specific behaviour poorly. An officer who sincerely "
            "values transparency may still withhold information when a superior "
            "exerts pressure, when career incentives discourage disclosure, or "
            "when institutional norms reward silence. This is the "
            "attitude-behaviour gap: situational forces and institutional "
            "design can override even strongly held positive attitudes.\n\n"
            "For example, in a revenue department, officers may declare "
            "commitment to impartiality yet allow political recommendations "
            "to influence file disposal because the transfer-posting system "
            "punishes non-compliance. The gap closes only when institutional "
            "safeguards such as RTI mandates, audit trails, whistleblower "
            "protection and transparent criteria reinforce the positive "
            "attitude with binding external constraints.\n\n"
            "The verdict is that attitude is the starting point of ethical "
            "conduct, but institutional design is its guarantor."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Examine how the three components of attitude can be targeted "
            "differently in civil-service training to reduce bias in service "
            "delivery. (Answer in 150 words)"
        ),
        "answer": (
            "The ABC model identifies cognitive, affective and behavioural "
            "components, each requiring a distinct training intervention to "
            "reduce bias.\n\n"
            "The cognitive component is addressed through factual correction: "
            "presenting officers with evidence on entitlements, dispelling "
            "stereotypes about beneficiary communities, and explaining legal "
            "standards of non-discrimination. However, correcting beliefs alone "
            "is insufficient because bias often resides in the affective "
            "component.\n\n"
            "The affective component requires experiential engagement: field "
            "immersion in tribal settlements, supervised interaction with "
            "persons with disabilities, and simulation exercises that generate "
            "empathy. Mission Karmayogi modules that use case-based learning "
            "target this layer. A probationer who lives in a rural community "
            "for a week develops emotional familiarity that a lecture cannot "
            "produce.\n\n"
            "The behavioural component is shaped through supervised practice: "
            "handling real citizen grievances, receiving mentor feedback on "
            "interpersonal conduct, and being held accountable for service "
            "timelines. Transparent work routines and citizen satisfaction "
            "feedback reinforce the behavioural shift.\n\n"
            "The trade-off is cost and time: affective training is slower "
            "and harder to scale. The verdict is that all three components "
            "must be targeted concurrently for bias reduction to be durable."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Distinguish between moral attitude and political attitude with "
            "reference to the obligations of a civil servant under the "
            "Central Civil Services (Conduct) Rules, 1964. Why must one be "
            "retained and the other bracketed? (Answer in 250 words)"
        ),
        "answer": (
            "A moral attitude is an evaluative stance toward what is right or "
            "wrong, grounded in ethical reasoning and applicable across "
            "contexts. A political attitude evaluates a specific party, "
            "ideology or contest for power. Both are attitudes in the "
            "ABC-model sense, but they serve fundamentally different roles "
            "in public office.\n\n"
            "The Central Civil Services (Conduct) Rules, 1964, operationalise "
            "this distinction. Rule 5 restricts participation in politics and "
            "demonstrations; Rule 7 restricts election canvassing. These "
            "rules implement the constitutional expectation, linked to "
            "Article 309, that a civil servant serves the permanent executive "
            "with non-partisanship. The same officer must serve successive, "
            "differently aligned elected governments; if political preference "
            "steered decisions, the neutrality that enables rotation would "
            "collapse.\n\n"
            "Moral attitude must be actively retained. A civil servant is "
            "expected to judge right from wrong: refusing an improper "
            "instruction, applying rules impartially and reporting corruption. "
            "This moral judgement makes non-partisanship trustworthy rather "
            "than merely mechanical compliance.\n\n"
            "Non-partisanship does not require political blankness of mind: "
            "private belief and the exercise of one's vote are not misconduct. "
            "Candid briefing of ministers is duty, not partisanship. A moral "
            "objection framed in law and public interest is principled "
            "dissent, not political obstruction.\n\n"
            "The verdict is that moral attitude is the instrument of ethical "
            "decision-making; political attitude must be bracketed because "
            "its expression substitutes partisan preference for the public "
            "interest the office exists to serve."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Analyse how cognitive dissonance operates as an ethical risk "
            "multiplier in public administration. Suggest institutional "
            "mechanisms to interrupt the rationalisation pathway. "
            "(Answer in 250 words)"
        ),
        "answer": (
            "Cognitive dissonance arises when an official's behaviour "
            "contradicts a held attitude. Festinger identifies three "
            "resolution paths: change the attitude, change the behaviour, or "
            "add a self-justifying cognition. The third path, rationalisation, "
            "is the ethical risk multiplier because it lets officials with "
            "sound values gradually normalise small compromises.\n\n"
            "Consider an officer who values transparency but is directed to "
            "withhold a routine file under a stretched RTI exemption. She "
            "convinces herself the exemption is broader than it is. The "
            "discomfort resolves without changing the unethical behaviour. "
            "Over time, 'everyone does it' becomes 'it is harmless' becomes "
            "settled practice. Small facilitation payments rationalised once "
            "as unavoidable become customary, then deserved. This is how "
            "dissonance multiplies ethical risk.\n\n"
            "Institutional mechanisms interrupt this pathway. Regular ethics "
            "review sessions let officers examine their own justifications "
            "under guided reflection. Transparent decision records make it "
            "harder to sustain private rationalisation when colleagues see "
            "the reasoning. Audit trails document actual exemption scope, "
            "preventing stretched interpretations from going unexamined. "
            "Whistleblower protection ensures that an officer who chooses "
            "the second path is not punished for principled objection. "
            "Rotation breaks the settled relationships that sustain "
            "rationalisation.\n\n"
            "The verdict is that cognitive dissonance is not itself unethical "
            "but its rationalisation pathway, unchecked by institutional "
            "design, converts individual psychological resolution into "
            "systemic ethical erosion."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Critically examine the ethical boundary between legitimate "
            "government persuasion campaigns and propaganda, with reference "
            "to social media's role in shaping public attitudes. Use Indian "
            "examples. (Answer in 250 words)"
        ),
        "answer": (
            "The ethical boundary between persuasion and propaganda turns on "
            "three criteria drawn from attitude-change theory: truthfulness "
            "of content, transparency of sponsorship and respect for audience "
            "autonomy. When all three are present, a government campaign is "
            "legitimate persuasion; when any is systematically violated, the "
            "campaign drifts toward manipulation or propaganda.\n\n"
            "Legitimate persuasion is visible in India's vaccination "
            "communication during the COVID-19 pandemic. ASHA workers, as "
            "credible local sources, delivered factual messages in vernacular "
            "languages through trusted community channels. The Hovland-Yale "
            "variables were operationalised transparently: source credibility, "
            "clear message content and audience-appropriate delivery. Swachh "
            "Bharat Mission's behaviour-change campaign similarly used wall "
            "paintings, community meetings and identified government "
            "sponsorship to shift sanitation attitudes.\n\n"
            "Social media complicates this picture. Platforms operationalise "
            "the audience variable at unprecedented precision through "
            "algorithmic micro-targeting. A government social-media cell that "
            "uses undisclosed paid influencers, emotionally manipulative "
            "imagery and suppresses critical comments crosses the ethical "
            "boundary even if the underlying policy goal is legitimate. The "
            "IT Rules' due-diligence obligations and the DPDP Act, 2023, "
            "provide regulatory anchors but enforcement remains uneven.\n\n"
            "The same digital channel that enables legitimate public health "
            "advisories also enables disinformation and deepfakes. A blanket "
            "ban on government social-media communication would sacrifice "
            "legitimate public information; unchecked use risks normalising "
            "propaganda. The ethical test must therefore be applied to each "
            "campaign individually.\n\n"
            "There is a boundary case that illustrates the difficulty. A "
            "district administration running a fear-based anti-open-defecation "
            "campaign without disclosing sponsorship may achieve behaviour "
            "change while violating transparency and autonomy. The ends do "
            "not settle the ethics; the means must also be defensible.\n\n"
            "The verdict is that persuasion-based governance is ethically "
            "legitimate and often necessary, but its digital-age application "
            "demands explicit transparency standards, algorithmic "
            "accountability and institutional restraint against the "
            "temptation to exploit the same tools of manipulation that "
            "the state has a duty to regulate."
        ),
    },
    {
        "marks": 20,
        "question": (
            "Evaluate the proposition that attitude change through persuasion "
            "is necessary but insufficient for ethical administration, "
            "discussing both the promise and the limits of attitude-based "
            "reform versus institutional constraint. (Answer in 250 words)"
        ),
        "answer": (
            "Attitude-based reform and institutional constraint are "
            "complementary strategies for ethical administration, each with "
            "distinctive strengths and limits.\n\n"
            "Attitude change through persuasion is necessary because no "
            "institutional rule can observe every exercise of discretion. An "
            "officer's evaluative disposition toward citizens, marginalised "
            "groups and public duty shapes how ambiguous situations are "
            "handled: whether a curable document error is helped or rejected, "
            "whether a whistle is blown or suppressed, whether a posting is "
            "treated as punishment or opportunity. William James's insight "
            "about attitude malleability applies: training, mentoring, field "
            "immersion and ethical leadership can genuinely reshape how "
            "officials interpret their role. Mission Karmayogi's "
            "behavioural-competency modules institutionalise this approach.\n\n"
            "But persuasion is slower than regulation and its effects are "
            "fragile. LaPiere's attitude-behaviour gap shows that sincere "
            "attitudes can be overridden by situational pressure, career "
            "incentives and peer norms. Cognitive dissonance theory warns "
            "that officials who begin with sound values can rationalise small "
            "compromises into settled corrupt practice. Therefore "
            "institutional constraints such as RTI mandates, transparent "
            "criteria, audit trails, whistleblower protection and enforceable "
            "codes of conduct are necessary to close the gap that attitude "
            "alone leaves open.\n\n"
            "Over-reliance on institutional constraint, however, risks purely "
            "compliance-based conduct, the box-ticking behaviour that reverts "
            "once monitoring relaxes. A department that installs surveillance "
            "without values education may see absenteeism drop temporarily "
            "but return when cameras malfunction. The code-of-ethics versus "
            "code-of-conduct distinction is relevant: the former targets "
            "internalised commitment, the latter external compliance.\n\n"
            "The reasoned verdict is that ethical administration requires "
            "both: persuasion to build durable internal commitment, and "
            "institutional constraint to catch the cases where even genuine "
            "commitment fails under pressure. Neither strategy alone is "
            "sufficient, and the administrator's task is to calibrate both "
            "to the specific governance context."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "1. The ABC model: what attitude is made of",
        "structural_type": "triad-structure",
        "nodes": (
            "Attitude is a stable evaluative disposition toward a specific object.",
            "The cognitive component holds beliefs and knowledge about the object.",
            "The affective component carries emotional charge, positive or negative.",
            "The behavioural component is the predisposition to act toward the object.",
            "Attitude is object-specific; value is general and cross-situational.",
            "Belief is a single cognitive claim; attitude is an evaluative stance.",
            "Aptitude is the trainable capacity to perform a role well.",
            "The ABC model is associated with Rosenberg and Hovland, 1960.",
        ),
        "verdict": "Attitude has three components; confusing it with value or aptitude costs marks.",
        "answer_use": "Open any attitude question by defining the ABC model and distinguishing it from value.",
    },
    {
        "title": "2. How attitudes form: experience, learning, reinforcement",
        "structural_type": "formation-funnel",
        "nodes": (
            "Direct experience with an object creates the strongest initial attitude.",
            "Social learning from family, peers and media shapes evaluative tendencies.",
            "Reinforcement through repeated outcomes attaches evaluative charge.",
            "Two officers in the same office can hold opposite attitudes toward the same community.",
            "Formation explains attitude but does not justify it ethically.",
            "Training can intervene at any formation pathway to reshape attitude.",
            "The affective component often resists change even when beliefs shift.",
            "Institutional incentives can reinforce or corrode attitudes over time.",
        ),
        "verdict": "Attitudes are formed, not born; understanding formation identifies training targets.",
        "answer_use": "Explain why attitudes differ before prescribing a change mechanism.",
    },
    {
        "title": "3. Hovland-Yale persuasion: source, message, audience, channel",
        "structural_type": "persuasion-engine",
        "nodes": (
            "The communicator's credibility and expertise determine source effect.",
            "The message's content, framing and emotional tone shape reception.",
            "The audience's predispositions determine resistance or openness.",
            "The channel or medium was added later from wider communication research.",
            "ASHA workers delivering vernacular vaccination messages illustrate source credibility.",
            "A gazette notification to illiterate beneficiaries shows audience-channel mismatch.",
            "Algorithmic micro-targeting transforms the audience variable at scale.",
            "The original 1953 Yale triad is source, message and audience only.",
        ),
        "verdict": "Effective persuasion activates all variables; the channel is not part of the original Yale triad.",
        "answer_use": "Structure any persuasion or campaign-effectiveness answer around these four variables.",
    },
    {
        "title": "4. Cognitive dissonance: three paths, one ethical risk",
        "structural_type": "decision-fork",
        "nodes": (
            "Dissonance arises when behaviour contradicts a held attitude.",
            "Path A: change the attitude to match the behaviour.",
            "Path B: change future behaviour to match the attitude.",
            "Path C: add a self-justifying cognition, the rationalisation path.",
            "Path C is the ethically dangerous one in administration.",
            "Small compromises rationalised once consolidate into settled practice.",
            "Ethics review and peer accountability interrupt the rationalisation cycle.",
            "Whistleblower protection supports officers who choose Path B.",
        ),
        "verdict": "Rationalisation, not dissonance itself, is the ethical risk multiplier.",
        "answer_use": "Use the three-path framework whenever a question involves value erosion or corruption creep.",
    },
    {
        "title": "5. The attitude-behaviour gap: why good attitudes fail",
        "structural_type": "gap-bridge",
        "nodes": (
            "LaPiere's 1934 study showed stated attitudes predicted specific acts poorly.",
            "Situational pressure can override even strongly held positive attitudes.",
            "Institutional incentives may reward conduct that contradicts declared values.",
            "Social norms in an office can normalise conduct that individuals privately oppose.",
            "RTI mandates are a binding external constraint closing the transparency gap.",
            "Audit trails make discretionary acts accountable to evidence.",
            "Whistleblower protection reduces the cost of acting on principled attitudes.",
            "Attitude is necessary but insufficient; institutional design is the bridge.",
        ),
        "verdict": "Close the gap with institutional constraint, not more exhortation.",
        "answer_use": "Use as the limitation paragraph in any answer that praises attitude change.",
    },
    {
        "title": "6. Persuasion, manipulation and propaganda: the ethical spectrum",
        "structural_type": "gradient-bar",
        "nodes": (
            "Persuasion respects audience autonomy and relies on truthful argument.",
            "Manipulation exploits cognitive biases or conceals intent.",
            "Propaganda uses repetition and emotional framing at scale to bypass critical evaluation.",
            "Swachh Bharat wall paintings with identified sponsorship are legitimate persuasion.",
            "Undisclosed paid influencers suppressing criticism cross the manipulation line.",
            "Fear-based state campaigns without disclosure shade toward propaganda.",
            "The ethical test is transparency of intent and audience autonomy.",
            "The same digital channel enables both legitimate information and disinformation.",
        ),
        "verdict": "Label the practice precisely: persuasion, manipulation or propaganda, then justify.",
        "answer_use": "Apply this spectrum to any social-media, campaign or information-governance question.",
    },
    {
        "title": "7. Moral attitude versus political attitude",
        "structural_type": "dual-column-comparison",
        "nodes": (
            "Moral attitude judges right and wrong across contexts; it must be retained.",
            "Political attitude evaluates parties and power contests; it must be bracketed.",
            "CCS Conduct Rules 1964, Rule 5 restricts political participation.",
            "CCS Conduct Rules 1964, Rule 7 restricts election canvassing.",
            "Non-partisanship covers official conduct, not private belief or voting.",
            "Policy awareness and candid briefing are duties, not partisan acts.",
            "Moral objection framed in law and public interest is principled dissent.",
            "The permanent executive convention requires the same officer to serve successive governments.",
        ),
        "verdict": "Retain moral judgement; bracket political preference; distinguish duty from partisanship.",
        "answer_use": "Use whenever a question tests impartiality, neutrality or the limits of official conduct.",
    },
    {
        "title": "8. Positive versus negative mindset in rule interpretation",
        "structural_type": "dual-lens-panel",
        "nodes": (
            "A positive mindset reads rules with their public purpose in view.",
            "A negative mindset treats rules as obstacles or sources of discretionary power.",
            "A facilitative officer helps correct a curable document error.",
            "A cynical officer exploits ambiguity to demand informal payment.",
            "Positive interpretation enables fair access without ignoring mandatory conditions.",
            "Negative interpretation produces delay, denial and extraction.",
            "Stress amplifies the dominant mindset in crisis situations.",
            "Purposive but accountable reading avoids both literalism and arbitrary benevolence.",
        ),
        "verdict": "Read rules with purpose, apply with accountability, explain with reasons.",
        "answer_use": "Apply this dual-lens to any question about discretion, mindset or citizen-facing service.",
    },
    {
        "title": "9. Attitude malleability: William James and training design",
        "structural_type": "circular-process",
        "nodes": (
            "The malleability principle holds that attitudes are revisable, not fixed.",
            "Reflection, field immersion and mentoring reshape evaluative stances.",
            "Mission Karmayogi modules target cognitive and affective components.",
            "Foundation-course immersion in underserved communities builds empathy.",
            "Malleability is not victim-blaming: structural constraints need structural reform.",
            "Periodic refresher training prevents cynicism and value erosion.",
            "Provenance caution: the attributed William James sentence is not traceable to his writings.",
            "The valid insight survives the attribution problem: attitude change is real when institutionally supported.",
        ),
        "verdict": "Attitudes can be changed; the change endures only with institutional reinforcement.",
        "answer_use": "Use for any question about training, attitude change, or the William James quotation.",
    },
    {
        "title": "10. Institutional closure: codes, constraints and the residual gap",
        "structural_type": "complementary-pillars",
        "nodes": (
            "Persuasion-based reform is slower but more durable once internalised.",
            "Rule-based constraint is faster but risks box-ticking compliance.",
            "Code of ethics targets internalised commitment; code of conduct targets external compliance.",
            "RTI, audit trails and whistleblower protection are binding constraints.",
            "Training without institutional reform becomes a box-ticking exercise.",
            "Institutional constraint without attitude change reverts when monitoring relaxes.",
            "The administrator must calibrate both strategies to the governance context.",
            "Durable ethical conduct requires values contained within institutions.",
        ),
        "verdict": "Neither persuasion alone nor constraint alone suffices; both must be calibrated together.",
        "answer_use": "Close any attitude-change answer with the institutional-closure qualification.",
    },
    {
        "title": "11. Trap detection: what costs marks in attitude questions",
        "structural_type": "contrast-matrix",
        "nodes": (
            "Attitude and value are related but not identical: value is broader.",
            "Positive attitude does not guarantee ethical behaviour: gap exists.",
            "Persuasion is not inherently unethical: it depends on truthfulness.",
            "Strong attitude does not always predict behaviour: situational override.",
            "Dissonance is not always resolved ethically: rationalisation is common.",
            "Persuasion and manipulation are not ethically identical: autonomy differs.",
            "Channel is not part of the original Hovland-Yale 1953 triad.",
            "Non-partisanship does not require enforced political blankness of mind.",
        ),
        "verdict": "The trap is always an absolute claim where the correct position is qualified.",
        "answer_use": "Scan each MCQ option for unqualified absolutes before selecting the answer.",
    },
    {
        "title": "12. PYQ synthesis and answer architecture",
        "structural_type": "answer-spine",
        "nodes": (
            "2020 Q4(b) tested positive attitude under stress: use ABC model and crisis example.",
            "2021 Q4(a) tested building suitable attitude: use formation pathways and training design.",
            "2022 Q2(a) tested positive versus negative mindset: use dual-lens rule-interpretation frame.",
            "2025 Q3(b) tested William James malleability: use provenance caution and institutional support.",
            "2025 Q1(a) tested social-media ethics: use persuasion-at-scale and Hovland-Yale variables.",
            "Define attitude via ABC before applying it to the scenario.",
            "Always note the attitude-behaviour gap as a qualification.",
            "Close with a verdict joining persuasion to institutional constraint.",
        ),
        "verdict": "Every attitude answer moves from definition to mechanism, example, gap and institutional closure.",
        "answer_use": "Use as the final revision checklist before writing any GS-IV attitude answer.",
    },
)

CURRENT_ANCHOR = {
    "title": "NIDM/MHA and UNICEF: Social and Behaviour Change for Disaster Risk Reduction",
    "verified_facts": (
        "Social and Behaviour Change (SBC) is a structured, research-driven methodology "
        "to influence attitudes, behaviours, norms and beliefs (NIDM/MHA-UNICEF "
        "Facilitator Guide, 2026 edition, ISBN 978-81-993586-1-4, pp. 2-6).",
        "SBC uses people-centred, inclusive and community-driven communication strategies.",
        "It supports risk perception, protective behaviour adoption, misinformation "
        "response, community trust building and accountability.",
        "The guide is a joint NIDM (Ministry of Home Affairs) and UNICEF publication "
        "designed for disaster-management facilitators across India.",
    ),
    "administrative_link": (
        "Use SBC to illustrate ethically grounded government persuasion in attitude-change "
        "answers. Its method can be analysed through credible communicators, evidence-based "
        "messages, audience-appropriate channels and community participation. It demonstrates "
        "how official campaigns can be truthful, credible, inclusive and autonomy-respecting "
        "rather than manipulative. The people-centred and "
        "community-driven design distinguishes legitimate persuasion from top-down propaganda "
        "by preserving audience participation and critical evaluation."
    ),
    "limit": (
        "The guide describes methodology and principles, not outcome data. Do not cite "
        "specific behavioural-change statistics from this source. SBC's ethical standing "
        "depends on faithful implementation; a programme that claims to be people-centred "
        "but suppresses dissent or withholds information crosses the persuasion-manipulation "
        "boundary despite using the SBC label."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://nidm.gov.in/PDF/Modules/SBCFacilitatorGuide_2026.pdf",
)

SOURCE_CAVEAT = (
    "Use the local Basic and Advanced owners as the controlling source. "
    "The ABC model is Rosenberg-Hovland 1960; cognitive dissonance is Festinger 1957; "
    "the Hovland-Yale approach is Hovland, Janis and Kelley, Communication and "
    "Persuasion, 1953. The channel variable is a later addition from wider communication "
    "research, not part of the original Yale triad. LaPiere's study is 'Attitudes vs. "
    "Actions,' Social Forces, 1934. The William James quotation tested in 2025 GS-IV "
    "Q3(b) is widely attributed but not traceable to his writings; it was popularised "
    "by Norman Vincent Peale. CCS Conduct Rules 1964, Rules 5 and 7, anchor the "
    "moral-versus-political attitude distinction. 2025 Q1(a) on social media is "
    "primarily routed to Topic 13 with a strong cross-link here. Do not fabricate "
    "primary citations or over-claim exclusive PYQ ownership."
)

REGISTER_SUPPLEMENT = (
    "Rapid recall: Attitude is a stable evaluative disposition toward a specific object "
    "with three components (cognitive-affective-behavioural, the ABC model, Rosenberg "
    "and Hovland 1960). It differs from value (general, cross-situational), belief "
    "(single cognitive claim) and aptitude (trainable capacity). Attitudes form through "
    "direct experience, social learning and reinforcement. Persuasion changes attitude "
    "via the Hovland-Yale variables: source credibility, message framing and audience "
    "predisposition; the channel is a later addition, not original Yale. Cognitive "
    "dissonance (Festinger 1957) has three resolution paths: change attitude, change "
    "behaviour, or rationalise; the third is ethically dangerous. LaPiere 1934 "
    "established the attitude-behaviour gap: stated attitudes predict specific acts "
    "poorly. Institutional constraints (RTI, audit, whistleblower protection) close the "
    "gap that attitude alone leaves open. Persuasion respects autonomy and uses truth; "
    "manipulation exploits bias; propaganda uses repetition at scale. Moral attitude "
    "(right/wrong judgement) must be retained in office; political attitude (party/power "
    "preference) must be bracketed per CCS Conduct Rules 1964 Rules 5 and 7. Positive "
    "mindset reads rules with public purpose; negative mindset creates delay and "
    "extraction. William James's malleability insight is valid but the exact quotation "
    "is not traceable to his writings. Mission Karmayogi targets attitude through "
    "role-based behavioural competencies but training reach does not prove ethical "
    "internalisation. Answer spine: define attitude via ABC, identify the targeted "
    "component, apply a persuasion lever, give an Indian example, note the "
    "attitude-behaviour gap as limitation, close with institutional closure."
)
