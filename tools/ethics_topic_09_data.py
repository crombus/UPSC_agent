"""Learner-v2 source data: Ethics Topic 09, Public Service Values."""

SESSION_TITLES = (
    "Public office, Nolan values and essential distinctions",
    "Recognising and diagnosing ethical dilemmas",
    "Public-service applications: trust, impartiality and compassion",
    "Legal floors, public propriety and UPSC close-option traps",
    "PYQ demand and a Nolan-based answer thesis",
    "Conflict of interest: types, disclosure and proportionate response",
    "Coercion, undue influence and unequal workplace power",
    "Evidence units: public-private interfaces and institutional safeguards",
    "Directive decoding and case-study integration",
    "Study links, audited PYQ routes and final synthesis",
)

SESSION_GROUPS = (
    ("1", "2"),
    ("3",),
    ("4",),
    ("5", "6"),
    ("7", "8"),
    ("9", "10"),
    ("11",),
    ("12",),
    ("13",),
    ("14",),
)

MCQ_ITEMS = (
    {
        "label": "Public office is a public trust",
        "statement": (
            "Public office confers entrusted authority, information and discretion for public "
            "purpose; status therefore increases rather than relaxes the duty of restraint, "
            "reason-giving and conduct that can retain citizens' confidence."
        ),
        "scenario_a": (
            "A district officer uses an official guest house for a family celebration because "
            "it is vacant. Which public-service proposition makes the convenience ethically relevant?"
        ),
        "scenario_b": (
            "A regulator says senior rank permits informal favours that junior staff cannot give. "
            "Which conception of office rejects this reasoning?"
        ),
        "family": "public office and role morality",
        "group": "public office and role morality",
    },
    {
        "label": "Role morality is bounded by constitutional public purpose",
        "statement": (
            "Role morality gives an official special duties of fidelity, competence and impartial "
            "implementation, but it cannot licence discrimination, concealment or personal loyalty "
            "where these defeat constitutional values, lawful authority or public interest."
        ),
        "scenario_a": (
            "A licensing officer says loyalty to her department requires concealing an unlawful "
            "selection practice. What qualification to role loyalty is decisive?"
        ),
        "scenario_b": (
            "A collector implements an unpopular but lawful welfare eligibility rule equally after "
            "recording reasons. Which feature makes this role-based conduct defensible?"
        ),
        "family": "public office and role morality",
        "group": "public office and role morality",
    },
    {
        "label": "Public interest is not majoritarian preference",
        "statement": (
            "Public interest concerns constitutionally permissible, evidence-based welfare of the "
            "community, including affected minorities and future citizens; it is not identical to "
            "electoral popularity, a minister's preference or the loudest group's immediate demand."
        ),
        "scenario_a": (
            "Residents demand that a night shelter be moved away before elections despite no "
            "alternative site. Which distinction should guide the municipal commissioner?"
        ),
        "scenario_b": (
            "A minister seeks a road diversion that benefits supporters but displaces a poorer "
            "hamlet without hearing. Which public-interest test is missing?"
        ),
        "family": "public office and role morality",
        "group": "public office and role morality",
    },
    {
        "label": "Status creates an appearance obligation",
        "statement": (
            "Because public authority depends on confidence, officials should avoid impropriety "
            "and its reasonable appearance; this is not a demand for private perfection but a "
            "duty to manage relationships and conduct that could credibly compromise official judgment."
        ),
        "scenario_a": (
            "An officer attends a bidder's lavish family function during tender evaluation but "
            "claims no favour was requested. Which ethical risk remains?"
        ),
        "scenario_b": (
            "A public hospital superintendent publicly discloses a relative's connection before "
            "a procurement decision. Which confidence-preserving duty is being served?"
        ),
        "family": "public office and role morality",
        "group": "public office and role morality",
    },
    {
        "label": "Integrity excludes compromising obligations",
        "statement": (
            "Nolan integrity requires public office holders not to place themselves under financial "
            "or other obligations that might influence official duty; risk of compromised judgment "
            "matters before proof of actual bias or corrupt payment."
        ),
        "scenario_a": (
            "A mining inspector accepts repeated hospitality from a company he may inspect next "
            "month. Which Nolan principle identifies the prior risk?"
        ),
        "scenario_b": (
            "A procurement member declares an investment and withdraws before bids are opened. "
            "Which value is operationalised even without proof of bias?"
        ),
        "family": "Nolan and constitutional values",
        "group": "Nolan and constitutional values",
    },
    {
        "label": "Objectivity is merit-based official procedure",
        "statement": (
            "Nolan objectivity requires appointments, contracts and benefits to be decided on merit "
            "and stated criteria; it is a procedural guard against favouritism, not a claim that "
            "public policy can be wholly value-neutral."
        ),
        "scenario_a": (
            "A scholarship committee publishes scoring criteria and anonymises applications. Which "
            "Nolan principle is most directly strengthened?"
        ),
        "scenario_b": (
            "An officer says a compassionate policy choice proves objectivity because it is humane. "
            "Which distinction corrects the claim?"
        ),
        "family": "Nolan and constitutional values",
        "group": "Nolan and constitutional values",
    },
    {
        "label": "Impartiality and political neutrality differ",
        "statement": (
            "Impartiality applies relevant criteria equally among persons; political neutrality "
            "requires non-partisan advice and implementation under the elected government. Neither "
            "requires indifference to constitutional rights, evidence or unlawful directions."
        ),
        "scenario_a": (
            "A district officer applies the same relief criteria to supporters and opponents of "
            "the ruling party. What value is directly displayed?"
        ),
        "scenario_b": (
            "A secretary gives frank written advice against an illegal proposal, then implements "
            "a lawful revised decision without partisan comment. What role ethic is illustrated?"
        ),
        "family": "Nolan and constitutional values",
        "group": "Nolan and constitutional values",
    },
    {
        "label": "Accountability is answerability to scrutiny",
        "statement": (
            "Accountability requires an office holder to explain and justify decisions to appropriate "
            "external scrutiny and accept consequences or correction; it exceeds private sincerity "
            "and differs from merely having responsibility to perform an assigned task."
        ),
        "scenario_a": (
            "A programme director meets targets but refuses to disclose beneficiary-selection reasons "
            "to an audit. Which public value is deficient?"
        ),
        "scenario_b": (
            "A block officer records alternatives, publishes reasons and corrects an exclusion after "
            "appeal. Which form of accountability is visible?"
        ),
        "family": "Nolan and constitutional values",
        "group": "Nolan and constitutional values",
    },
    {
        "label": "A genuine dilemma conflicts legitimate duties",
        "statement": (
            "An ethical dilemma arises when two legitimate duties, values or loyalties cannot both "
            "be fully honoured; it differs from a simple temptation to obtain gain by breaking a "
            "known rule or disguising favouritism as compassion."
        ),
        "scenario_a": (
            "During a cloudburst, a deputy commissioner must choose between leading fragile rescue "
            "operations and attending a parent's last rites. Why is this a genuine dilemma?"
        ),
        "scenario_b": (
            "An officer calls accepting a contractor's gift a dilemma between friendship and duty. "
            "What diagnosis should precede balancing?"
        ),
        "family": "dilemma diagnosis and resolution",
        "group": "dilemma diagnosis and resolution",
    },
    {
        "label": "Legality is a floor, not the whole ethical inquiry",
        "statement": (
            "A legal prohibition removes an option from ordinary ethical choice, but technical legality "
            "does not automatically establish morality or propriety; officials must also test public "
            "purpose, equality, constitutional values, reasons and foreseeable institutional effects."
        ),
        "scenario_a": (
            "A minister's preferred applicant technically meets minimum eligibility but is expedited "
            "outside the published queue. Which distinction must the officer apply?"
        ),
        "scenario_b": (
            "A rule permits several lawful relief priorities. How should a collector choose among "
            "them without treating legality as a complete answer?"
        ),
        "family": "dilemma diagnosis and resolution",
        "group": "dilemma diagnosis and resolution",
    },
    {
        "label": "Stakeholder mapping prevents tunnel vision",
        "statement": (
            "Dilemma resolution begins by identifying affected citizens, weaker groups, colleagues, "
            "institutions and future interests; mapping them exposes hidden burdens before an official "
            "chooses among lawful alternatives or invokes a public-good slogan."
        ),
        "scenario_a": (
            "A city proposes clearing a forest edge for housing. Which step prevents electricity "
            "benefits from obscuring tribal livelihood and ecological costs?"
        ),
        "scenario_b": (
            "A hospital administrator reallocates staff during an outbreak. Which diagnostic method "
            "ensures workers, patients and continuity of other care are considered?"
        ),
        "family": "dilemma diagnosis and resolution",
        "group": "dilemma diagnosis and resolution",
    },
    {
        "label": "A defensible resolution is reasoned and reviewable",
        "statement": (
            "After excluding unlawful options, an official should compare realistic alternatives through "
            "duties, consequences and virtues, select a proportionate option, record reasons, communicate "
            "it fairly and mitigate residual harm under independent or administrative review."
        ),
        "scenario_a": (
            "A collector makes an emergency departure from normal documentation requirements. What "
            "sequence keeps the choice from becoming arbitrary discretion?"
        ),
        "scenario_b": (
            "A senior officer resolves a family-linked tender concern privately without a file note. "
            "What feature of defensible resolution is absent?"
        ),
        "family": "dilemma diagnosis and resolution",
        "group": "dilemma diagnosis and resolution",
    },
    {
        "label": "Actual conflict calls for recusal",
        "statement": (
            "An actual conflict exists when a private interest and an immediate official decision "
            "directly collide; the normal safeguard is prompt declaration, removal from the particular "
            "decision and reassignment, rather than waiting to prove corrupt motive or outcome."
        ),
        "scenario_a": (
            "A procurement officer's sibling submits a bid being evaluated by that officer. Which "
            "conflict type and operational response apply?"
        ),
        "scenario_b": (
            "A municipal chair says impartiality is enough despite deciding on her spouse's licence. "
            "Why is private assurance insufficient?"
        ),
        "family": "public-private relationships and conflicts",
        "group": "public-private relationships and conflicts",
    },
    {
        "label": "Potential conflict is managed prospectively",
        "statement": (
            "A potential conflict is a private interest that could later intersect with official duty; "
            "proactive disclosure and a register enable later screening, while automatic present recusal "
            "is unnecessary where no relevant decision is before the officer."
        ),
        "scenario_a": (
            "An officer owns shares in a sector she may later regulate but has no current file. "
            "Which proportionate management response is appropriate?"
        ),
        "scenario_b": (
            "A new regulator hides a spouse's consultancy because no tender is active today. Which "
            "conflict concept exposes the error?"
        ),
        "family": "public-private relationships and conflicts",
        "group": "public-private relationships and conflicts",
    },
    {
        "label": "Apparent conflict requires confidence protection",
        "statement": (
            "An apparent conflict exists where a reasonable informed observer could suspect compromised "
            "judgment despite no proved private benefit; transparency, reasons and sometimes voluntary "
            "recusal preserve confidence without mechanically treating appearance as established corruption."
        ),
        "scenario_a": (
            "A childhood friend seeks a routine approval from an officer using published criteria. "
            "What confidence-focused analysis is needed?"
        ),
        "scenario_b": (
            "A journalist alleges bias because an official studied with an applicant decades ago. "
            "Which response avoids both concealment and automatic guilt?"
        ),
        "family": "public-private relationships and conflicts",
        "group": "public-private relationships and conflicts",
    },
    {
        "label": "Disclosure does not itself resolve conflict",
        "statement": (
            "Declaration is a necessary first safeguard but does not cleanse every conflict; the "
            "institution must assess materiality, decide recusal, reassignment or conditions, record "
            "the response and ensure the private interest cannot distort public decision-making."
        ),
        "scenario_a": (
            "A board member declares a major holding, then participates in regulating that company. "
            "Which management principle remains unmet?"
        ),
        "scenario_b": (
            "A district office maintains an interest register but never screens files against it. "
            "Why is the safeguard incomplete?"
        ),
        "family": "public-private relationships and conflicts",
        "group": "public-private relationships and conflicts",
    },
    {
        "label": "Coercion overbears choice through threat",
        "statement": (
            "Coercion compels conduct through an explicit or implicit threat of harm, such as punitive "
            "transfer, dismissal or retaliation; apparent consent under such duress is not a reliable "
            "ethical defence for the pressured official or decision."
        ),
        "scenario_a": (
            "A superior threatens an adverse appraisal unless a junior certifies an unsafe building. "
            "Which workplace-power concept applies?"
        ),
        "scenario_b": (
            "A ministerial aide threatens to block an officer's transfer unless a file is expedited. "
            "What makes this more than firm instruction?"
        ),
        "family": "power, influence and discretion",
        "group": "power, influence and discretion",
    },
    {
        "label": "Undue influence exploits dependency without threat",
        "statement": (
            "Undue influence exploits trust, authority or dependency to bend another's autonomous judgment "
            "without an overt threat; it requires attention to relationship patterns, career vulnerability "
            "and informal pressure rather than only searching for a provable quid pro quo."
        ),
        "scenario_a": (
            "A mentor repeatedly hints that a junior's promotion depends on selecting a preferred vendor. "
            "Which power abuse is present?"
        ),
        "scenario_b": (
            "A retiring regulator cultivates a future job from a recently supervised firm without an "
            "express bargain. Which ethical risk needs scrutiny?"
        ),
        "family": "power, influence and discretion",
        "group": "power, influence and discretion",
    },
    {
        "label": "Discretion needs legal purpose and recorded reasons",
        "statement": (
            "Discretion is not personal freedom: it must stay within authority, pursue statutory and "
            "constitutional purpose, use relevant facts and equal criteria, remain proportionate and "
            "be documented so that citizens, supervisors and courts can review it."
        ),
        "scenario_a": (
            "A flood officer accepts equivalent proof from every applicant whose papers were destroyed. "
            "What conditions make this calibrated discretion rather than favour?"
        ),
        "scenario_b": (
            "A licensing official waives documents only for politically connected applicants. Which "
            "controls on discretion have failed?"
        ),
        "family": "power, influence and discretion",
        "group": "power, influence and discretion",
    },
    {
        "label": "Automation can reduce but not erase accountability",
        "statement": (
            "Automating rule-bound services can reduce arbitrary discretion and improve traceability, "
            "but accountable administration still requires accessible alternatives, human review of "
            "exclusion, reliable data and responsibility for biased design, implementation and redress."
        ),
        "scenario_a": (
            "A digital benefit portal rejects persons whose biometric authentication fails repeatedly. "
            "What accountability safeguard must accompany automation?"
        ),
        "scenario_b": (
            "A department claims its algorithm makes recruitment fully objective. Which ethical "
            "qualification should a review committee insist upon?"
        ),
        "family": "power, influence and discretion",
        "group": "power, influence and discretion",
    },
    {
        "label": "Openness has a justified public-interest limit",
        "statement": (
            "Nolan openness favours maximum disclosure, but information may be restricted when a "
            "clear wider public-interest and lawful ground supports it; secrecy must be justified, "
            "narrowly tailored and not used to conceal embarrassment, favouritism or maladministration."
        ),
        "scenario_a": (
            "A disaster authority withholds exact shelter locations temporarily because disclosure "
            "would expose women to a verified security risk. Which value balance is required?"
        ),
        "scenario_b": (
            "A department refuses an audit request solely because criticism may embarrass a minister. "
            "Why is this not a valid openness exception?"
        ),
        "family": "accountability and ethical governance",
        "group": "accountability and ethical governance",
    },
    {
        "label": "Honesty includes private-interest declaration",
        "statement": (
            "In the Nolan formulation, honesty specifically requires declaration of private interests "
            "relating to public duties and resolution of resulting conflicts; ordinary truthfulness "
            "remains important, but this principle directly targets transparent conflict management."
        ),
        "scenario_a": (
            "A committee member accurately reports project data but conceals a relative's consultancy "
            "with the vendor. Which Nolan requirement is breached?"
        ),
        "scenario_b": (
            "An officer voluntarily places a financial interest on record before joining a regulatory "
            "panel. Which public-life value is being applied?"
        ),
        "family": "accountability and ethical governance",
        "group": "accountability and ethical governance",
    },
    {
        "label": "Leadership shapes institutional ethical climate",
        "statement": (
            "Nolan leadership requires senior office holders to promote public-life values through "
            "personal example, fair systems and response to misconduct; ethical culture cannot be "
            "created by slogans while leaders reward target achievement obtained through improper means."
        ),
        "scenario_a": (
            "A department head refuses to reward staff who manipulate beneficiary data to meet targets. "
            "Which Nolan principle is being demonstrated?"
        ),
        "scenario_b": (
            "A senior officer signs a conflict declaration, protects dissenters and reviews procurement "
            "reasons. How does this build ethical climate?"
        ),
        "family": "accountability and ethical governance",
        "group": "accountability and ethical governance",
    },
    {
        "label": "Metrics illustrate monitoring, not complete ethics",
        "statement": (
            "Disposal, pendency and response-time metrics can make administrative monitoring visible, "
            "but they do not by themselves prove correctness, fairness, satisfaction, impartiality "
            "or absence of misconduct; qualitative review and remedy remain necessary."
        ),
        "scenario_a": (
            "A ministry closes one lakh grievance records quickly but gives identical non-speaking "
            "replies. Which distinction prevents equating speed with accountability?"
        ),
        "scenario_b": (
            "A dashboard shows low pendency while inaccessible digital procedures exclude elderly "
            "claimants. What ethical limitation of metrics is exposed?"
        ),
        "family": "accountability and ethical governance",
        "group": "accountability and ethical governance",
    },
)

PYQS = (
    {
        "year": 2018,
        "question": "GS-IV Q2(a): What is meant by public interest? What are the principles and procedures to be followed by civil servants in public interest? 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf. Topic 09 owns public-service values; RTI in Q2(b) belongs primarily to Topic 15.",
        "answer": "Public interest is constitutionally permissible, evidence-based welfare rather than a private, partisan or majoritarian preference. It includes the interests of weaker, remote and future citizens who may not be able to exert immediate political pressure. A civil servant should identify affected groups, act within law and delegated authority, use relevant evidence, apply published criteria equally, disclose conflicts, consult where feasible and record reasons capable of review. In disaster relief, need, vulnerability and access constraints should guide allocation rather than political connection or media visibility. A workable appeal channel can correct exclusion without suspending urgent delivery. Integrity prevents private capture, impartiality protects equal treatment, and accountability makes the decision publicly defensible. Thus public interest is neither an officer's private moral preference nor a numerical count of demands; it is a reasoned constitutional judgment about common welfare.",
    },
    {
        "year": 2018,
        "question": "GS-IV Q3(a): What is meant by conflict of interest? Illustrate with examples the difference between actual and potential conflicts of interest. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against the local 2018 GS-IV paper. Topic 09 is the direct owner; apparent conflict is useful supplementary teaching, not a substituted PYQ demand.",
        "answer": "A conflict of interest is a private interest capable of improperly influencing public duty, or reasonably appearing to do so. It is a risk situation, not by itself proof of corruption. An actual conflict is immediate: a procurement officer evaluates a sibling's bid. It requires prompt declaration, recusal from that decision and reassignment to an independent colleague. A potential conflict may arise later: a regulator owns shares in a sector she may subsequently supervise. It requires advance disclosure and an interest register so that later files can be screened. The distinction enables proportionate prevention: ignoring a potential interest loses an early safeguard, while treating every remote interest as an actual conflict can paralyse service delivery. Concealment, participation despite a material conflict and failure to follow prescribed management measures threaten integrity, equal treatment and public confidence.",
    },
    {
        "year": 2018,
        "question": "GS-IV Q5(b): Explain the process of resolving ethical dilemmas in Public Administration. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against the local 2018 GS-IV paper. Topic 09 supplies diagnosis; the full Section-B answer architecture is owned by Topic 22.",
        "answer": "First distinguish a genuine clash of legitimate duties from a simple illegal, corrupt or self-interested proposal. Establish the material facts, affected stakeholders, authority, time pressure and legal floor; options barred by law ordinarily drop out. Then generate realistic alternatives rather than comparing action only with inaction. Test each through rights and equality, public interest, foreseeable consequences, institutional precedent, integrity and the character expected of a public servant. Select the proportionate option, state reasons, communicate it respectfully and mitigate foreseeable residual harm. In a relief conflict between speed and verification, a temporary, uniformly available alternative-proof mechanism may protect both life and fairness. It should be time-bound, documented and reviewable. Consultation, a clear handover of responsibility and an appeal route improve implementation. Record and review make the decision accountable rather than privately intuitive or merely expedient.",
    },
    {
        "year": 2019,
        "question": "GS-IV Q1(a): What are the basic principles of public life? Illustrate any three with suitable examples. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf. It is shared with Topic 04; use the Nolan principles as ARC-cited public-life evidence, not as India-specific rules.",
        "answer": "The ARC reproduces the Nolan principles: selflessness, integrity, objectivity, accountability, openness, honesty and leadership. Selflessness means a district officer allocates relief by need, not electoral benefit. Integrity means a tender member declares a relative's interest and recuses before evaluation. Objectivity means appointments, contracts and benefits use published merit criteria rather than influence. Accountability requires recorded reasons, appropriate scrutiny and correction where a decision is defective. Openness favours disclosure unless a clear lawful public-interest ground justifies restriction; honesty includes declaring relevant private interests. Leadership requires seniors to model these standards and build systems that do not reward improper target achievement. These principles connect power with public trust. They should be joined to Indian constitutional equality, dignity and lawful procedure rather than copied as a free-standing or India-specific foreign checklist.",
    },
    {
        "year": 2019,
        "question": "GS-IV Q1(b): What do you understand by the term 'public servant'? Reflect on the expected role of a public servant. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against the local 2019 GS-IV paper. Shared with Topic 04; do not duplicate its aptitude/foundational-values treatment.",
        "answer": "A public servant exercises entrusted state authority to advance lawful public purposes. The role is neither personal patronage nor passive file movement: it requires competence, impartial and citizen-respectful implementation, frank non-partisan advice, protection of constitutional rights, prudent discretion and answerability for reasons and outcomes. A secretary should advise a minister honestly, flag legal or ethical difficulty through recorded channels, suggest workable lawful alternatives and loyally implement the lawful final decision without favour or fear. A field officer should also make services accessible to those facing disability, distance or documentation barriers, while treating comparable applicants by the same criteria. Public status therefore brings higher expectations of integrity, propriety and restraint in private relationships. The official is accountable for delivery and process, whereas the elected executive remains democratically answerable for broad policy choices. This balance safeguards both democratic mandate and professional neutrality.",
    },
    {
        "year": 2021,
        "question": "GS-IV Q2(b): Besides domain knowledge, a public official needs innovativeness and creativity of a high order while resolving ethical dilemmas. Discuss with suitable example. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf. Shared with Topic 13 for technology; innovation remains bounded by law, equality and review.",
        "answer": "Innovation helps an official avoid false binaries without evading ethical constraints. In flood relief, a collector can use mobile verification, community lists, assisted offline help and a time-bound appeal desk when documents are destroyed, instead of choosing between total exclusion and fabricated records. Creativity widens feasible options; it does not create authority to favour individuals, hide reasons or bypass rights. The officer must confirm delegated authority, identify vulnerable groups, apply the alternative equally to comparable claimants and disclose the temporary criteria. Consultation with local bodies can expose error, while audit trails protect against duplication and capture. The measure should have a clear review date and normal safeguards should be restored when emergency conditions end. Thus ethical innovation is principled, evidence-responsive problem-solving: it reconciles service delivery with integrity rather than treating compassion as a licence for irregularity.",
    },
    {
        "year": 2023,
        "question": "GS-IV Q2(b): In the context of work environment, differentiate between 'coercion' and 'undue influence' with suitable examples. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording verified against books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf. Topic 09 direct route.",
        "answer": "Coercion overbears choice through an explicit or implicit threat: a superior threatens a punitive transfer, dismissal or adverse appraisal unless a junior certifies unsafe work. Any apparent consent is impaired by fear. Undue influence exploits trust, authority or dependency without an overt threat: a mentor repeatedly links career goodwill to choosing a preferred vendor, making independent judgment difficult. Coercion is often incident-specific and more readily evidenced through the identified threat; undue influence is more likely to require pattern review of relationships, repeated favours and career vulnerability. Both corrupt autonomous professional judgment and may distort public decisions. Safeguards include protected reporting, written directions, independent appraisal, separation of conflicted decision-makers, rotation where necessary and recorded reasons for discretionary recommendations. An ethics response should not label every firm lawful instruction coercion, but must not dismiss subtle dependency pressure as ordinary professional advice.",
    },
    {
        "year": 2024,
        "question": "GS-IV Q5(a): The 'Code of Conduct' and 'Code of Ethics' are sources of guidance in public administration. There is a Code of Conduct already in operation whereas a Code of Ethics is not yet put in place. Suggest a suitable model for a Code of Ethics to maintain integrity, probity and transparency in governance. 10 marks; 150 words.",
        "marks": 10,
        "source_note": "Exact wording and format verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf. Topic 16 is the dedicated primary owner; Topic 09 supplies Nolan/public-service-values support. Treat the question premise as a PYQ premise, not proof of every category's current legal status.",
        "answer": "A Code of Ethics should begin with constitutional fidelity and public purpose, then require selflessness, integrity, merit objectivity, impartiality, openness, honest interest declaration, accountability and leadership by example. It should address gifts, conflicts, post-employment, reasoned discretion, treatment of citizens, use of information and protection of good-faith dissent. Its provisions should be intelligible to citizens as well as officials. Operational support is essential: public declaration, confidential ethics advice, periodic training, updated interest registers, independent complaint handling, fair inquiry and an annual public report on observance. A separate Code of Conduct can specify service rules, procedures and consequences; an ethics code cannot replace legal safeguards. The ARC's Nolan-based distinction therefore supports principles joined to implementation, monitoring and leadership, rather than a symbolic document or an unverified claim about every public-office category's present status.",
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q5(a): \"One who is devoted to one's duty attains highest perfection in "
            "life.\" Analyse this statement with reference to sense of responsibility and "
            "personal fulfilment as a civil servant. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": "Exact wording and format verified against books\\mains\\UPSC Mains 2025 GS Paper 4.pdf. Shared with Topic 04; do not treat devotion as blind obedience or self-erasure.",
        "answer": "Devotion to duty gives a civil servant purpose, reliability and satisfaction from advancing public welfare. It means competent, timely and impartial discharge of entrusted responsibility, not obedience to every informal demand or pursuit of visible targets at any cost. A disaster officer who remains accessible, protects vulnerable citizens, coordinates teams and records fair allocation decisions may experience fulfilment through meaningful service. Yet duty must be constitutional and sustainable: blind obedience can enable illegality, while relentless self-sacrifice can impair judgment, health and legitimate family obligations. In a personal emergency, responsible delegation and transparent communication may better serve citizens than either abandonment of duty or performative self-denial. Personal fulfilment is deepest when commitment joins integrity, empathy, lawful discretion, professional competence and accountable institutional support. It is the satisfaction of serving a public purpose well, not a claim to moral superiority over citizens or colleagues.",
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q5(b): To achieve holistic development goal, a civil servant acts as an "
            "enabler and active facilitator of growth rather than a regulator. What specific "
            "measures will you suggest to achieve this goal? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": "Exact wording and format verified against the local 2025 GS-IV paper and routing ledger. Shared with Topic 04; Topic 09 adds public-trust, impartiality and accountability limits.",
        "answer": "An enabler removes lawful barriers that prevent citizens from accessing rights and services; a facilitator coordinates agencies, information and participation to make policy work. A district officer can provide accessible grievance channels, help self-help groups complete applications, arrange language or disability support and coordinate departments after a disaster. This strengthens citizen capability rather than creating dependence on a personal patron. Facilitation is not patronage: comparable citizens need equal criteria, decisions need intelligible reasons, and private intermediaries cannot capture discretion. The official should verify authority, publish service standards, retain an audit trail and offer review where a person is excluded. The ethical role combines empathy with objectivity, initiative with lawful authority, and responsiveness with accountability. It shifts administration from command alone to citizen-capability building while retaining public trust and preventing selective convenience from becoming favouritism.",
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q7 case study: Vijay was Deputy Commissioner of remote district of Hilly "
            "Northern State of the country for the last two years. In the month of August heavy "
            "rains lashed the complete state followed by cloud burst in the upper reaches of the "
            "said district. The damage was very heavy in the complete state especially in the "
            "affected district. The complete road network and telecommunication were disrupted "
            "and the buildings were damaged extensively. People's houses have been destroyed and "
            "they were forced to stay in open. More than 200 people have been killed and about "
            "5000 were badly injured. The Civil Administration under Vijay got activated and "
            "started conducting rescue and relief operations. Temporary shelter camps and "
            "hospitals were established to provide shelter and medical facilities to the homeless "
            "and injured people. Helicopter services were pressed in, for evacuating sick and old "
            "people from remote areas. Vijay got a message from his hometown in Kerala that his "
            "mother was seriously sick. After two days Vijay received the unfortunate message that "
            "his mother has expired. Vijay has no close relative except one elder sister who was "
            "US citizen and staying there for last several years. In the meantime, the situation "
            "in the affected district deteriorated further due to resumption of heavy rains after "
            "a gap of five days. At the same time, continuous messages were coming on his mobile "
            "from his hometown to reach at the earliest for performing last rites of his mother. "
            "(a) What are the options available with Vijay? (b) What are the ethical dilemma being "
            "faced by Vijay? (c) Critically evaluate and examine each of these options identified "
            "by Vijay. (d) Which of the options, do you think, would be most appropriate for Vijay "
            "to adopt and why? (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": "Full case facts, all four demands and the single 250-word format reproduced from books\\mains\\UPSC Mains 2025 GS Paper 4.pdf. Topic 09 owns multi-duty diagnosis; Topic 22 owns the complete case-answer architecture.",
        "answer": "Vijay may remain throughout; leave immediately; stabilise and delegate before a brief visit; or participate remotely and travel after the crisis. The stakeholders are disaster-affected citizens, rescue staff, administration, his family and Vijay himself. The dilemma is public duty to protect lives versus filial, cultural and personal obligation; it also involves whether delegation is responsible leadership or abandonment, fair relief allocation and transparent crisis communication. Remaining offers command continuity, reassurance and rapid coordination but exacts grave personal cost and risks impaired judgment through unacknowledged grief. Immediate departure respects last rites but may endanger a fragile operation where roads and communications have failed. A brief absence is defensible only with a competent written handover, communication redundancy, authority clarity, resource access and a recall threshold. Remote rites protect operations but may insufficiently meet family duty. Vijay should immediately stabilise command, notify superiors, assess the deputy's competence and delegate in writing to the strongest available officer. He should brief teams and the public on the continuity arrangement, while protecting necessary family privacy. He must retain a clear escalation channel and periodically reassess whether delegated command remains adequate. He may travel only if operations are demonstrably stable; otherwise he should remain and arrange remote participation, with later institutional support for travel. Consequence analysis gives special weight to avoidable mass harm; duty ethics recognises family obligation; virtue requires compassion with practical wisdom. This preserves life-saving duty without treating private grief as ethically irrelevant.",
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q12 case study: Ashok is Divisional Commissioner of one of the border "
            "districts of the North East State. A few years back, Military has taken over the "
            "neighbouring country after overthrowing the elected civil government. Civil war "
            "situation is prevailing in the country especially in last two years. However, internal "
            "situation further deteriorated due to rebel groups taking over control of certain "
            "populated areas near own border. Due to intense fight between military and rebel "
            "groups, civilian casualties has increased manifold in recent past. In the meantime, "
            "in one night Ashok got information from the local police guarding the border check "
            "post that there are about 200-250 people mainly women and children trying to cross "
            "over to our side of the border. There are also about 10 soldiers with their weapons "
            "in military uniform part of this group who wants to cross over. Women and Children "
            "are also crying and begging for help. A few of them are injured and bleeding "
            "profusely need immediate medical care. Ashok tried to contact Home Secretary of the "
            "State but failed to do so due to poor connectivity mainly due to inclement weather. "
            "(a) What are the options available with Ashok to cope with the situation? (b) What "
            "are the ethical and legal dilemmas being faced by Ashok? (c) Which of the options, do "
            "you think would be more appropriate for Ashok to adopt and why? (d) In the present "
            "situation, what are the extra precautionary measures to be taken by the Border "
            "Guarding Police in dealing with soldiers in uniform? (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": "Full case facts, all four demands and the single 250-word format reproduced from books\\mains\\UPSC Mains 2025 GS Paper 4.pdf. Topic 09 supports ethical/legal dilemma diagnosis; Topic 22 controls full case methodology.",
        "answer": "Ashok can refuse entry; admit everyone without screening; provide emergency assistance while separating and screening groups; or hold civilians safely pending higher directions. Stakeholders include injured women and children, armed soldiers, local residents, border personnel, state authorities and persons on both sides of the border. He faces humanity and urgent medical care versus border security, legal authority, non-discrimination, public order and risk posed by armed personnel. Refusal risks preventable death and breaches the public servant's duty of care; unverified admission risks security and loss of control; delay without care is inhumane. The proportionate course is immediate life-saving aid and protected temporary shelter for civilians, gender- and child-sensitive registration, rapid communication with competent authorities, and individual rather than collective assessment. Armed soldiers should be disarmed, physically separated from civilians, searched lawfully, guarded by trained personnel, medically examined, documented and handled under applicable security and legal procedures without summary punishment. Separate interpreters, women officers and medical staff should reduce secondary harm and improve reliable assessment. Food, water, medical triage and safe shelter should not be withheld from civilians because armed persons are present. Ashok should record the emergency facts and decisions, seek instructions as soon as contact is restored and ensure staff use minimum necessary force. Subsequent independent review must test both humanitarian treatment and security procedure. This preserves dignity and impartiality while managing concrete risk through necessity, proportionality, reasons and review.",
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": "Distinguish public interest from majoritarian preference in public administration.",
        "answer": "Public interest is the constitutionally permissible, evidence-based welfare of the community, including persons who are weak, unpopular or not yet able to speak for themselves. Majoritarian preference is what a numerical or politically influential group currently wants. The two may overlap, but they are not identical. A city majority may oppose a night shelter near its homes; an administrator must assess safety, alternative sites, the homeless persons' dignity and equal access, not merely count objections. Public interest therefore requires lawful authority, relevant evidence, proportionality, hearing affected groups and recorded reasons. It rejects both elite paternalism and vote-seeking populism. The proper civil-service role is to convert competing claims into a transparent, reviewable decision anchored in equality, public purpose and long-term trust.",
    },
    {
        "marks": 10,
        "question": "Differentiate legality, morality and propriety in public office with an example.",
        "answer": "Legality asks whether an act is authorised by law or rule. Morality asks whether it respects duties, dignity, fairness and public purpose. Propriety asks whether conduct, including its reasonable appearance, sustains confidence appropriate to public office. They overlap but are not interchangeable. A technically permissible meeting with a bidder may be improper where it creates a credible appearance of preferential access; a lawful choice among relief priorities still needs moral justification through need and equality. Conversely, moral concern cannot create power contrary to law. An officer should first identify the legal floor, then test constitutional values, conflict risk, transparency and foreseeable institutional effects. Disclosure, written reasons and independent scrutiny convert this three-part inquiry into accountable administration. This sequencing also prevents private moral preference from becoming arbitrary public power.",
    },
    {
        "marks": 15,
        "question": "Political neutrality does not require value-neutral administration. Discuss.",
        "answer": "Political neutrality means that the permanent executive gives frank professional advice and implements the elected government's lawful decisions without partisan favour, campaign conduct or selective service delivery. It does not mean value-neutrality. Civil servants are constitutionally bound to equality, dignity, rule of law and public interest; they must identify discrimination, procedural unfairness and illegality even when politically inconvenient.\n\nA secretary should place evidence and legal limits before a minister, record material advice and suggest lawful alternatives. Once a revised direction is lawful, neutral implementation requires the same eligibility and service standards for supporters and opponents. In disaster relief, neutrality forbids directing resources to an electoral constituency, while constitutional values require special attention to persons with disability or remote communities facing unequal barriers.\n\nThe opposite errors are bureaucratic obstruction of a democratic mandate and obedient participation in unlawful patronage. A sound relationship distinguishes policy choice, for which the political executive is answerable, from competent impartial implementation and evidence-based advice, for which the civil servant is answerable. Fixed procedures, written directions, transfer safeguards and review support that balance. Political neutrality is thus principled constitutional fidelity, not ethical silence.",
    },
    {
        "marks": 15,
        "question": "Conflict-of-interest policy should prevent both concealment and paralysing recusal. Examine.",
        "answer": "A conflict of interest is a risk that private interest will compromise, or reasonably appear to compromise, public duty. A useful policy separates actual, potential and apparent conflicts. An actual conflict, such as evaluating a sibling's tender, generally requires declaration, recusal and reassignment. A potential conflict, such as shares in a sector an officer may later regulate, requires prospective disclosure and a register. An apparent conflict requires transparent reasons and a confidence assessment; it does not automatically establish misconduct.\n\nThis distinction prevents two failures. Concealment allows private financial, family or post-employment interests to distort judgment. Blanket recusal, however, can deprive administration of expertise and encourage tactical allegations. The response should be proportionate to materiality, proximity, decision sensitivity and a reasonable informed observer's view.\n\nInstitutions need updated declarations, screening before sensitive files, documented decisions, independent ethics advice, cooling-off where justified and audit trails. Disclosure alone is not a cure: the institution must decide whether recusal, conditions or reassignment are required. The goal is neither distrust of every relationship nor tolerance of hidden influence, but defensible decisions that preserve impartiality and public confidence.",
    },
    {
        "marks": 20,
        "question": "A minister lawfully seeks faster approval for a project, but the request would displace applicants under published eligibility criteria. Analyse the civil servant's ethical response.",
        "answer": "The officer faces a claimed development objective and ministerial expectation on one side, and impartiality, equality, procedural fairness and public trust on the other. Stakeholders include queued applicants, potential beneficiaries, departmental staff, the minister, future applicants and citizens who depend on predictable administration. The officer must first establish whether any proposed acceleration violates law, published criteria, delegated authority or a court direction. An illegal option should be declined through recorded advice, not balanced as if it were merely another ethical preference.\n\nFeasible lawful options include maintaining the queue; creating a general expedited channel under published urgent criteria available to all similarly placed projects; seeking competent approval for a transparent policy revision; or silently prioritising the minister's preferred project. The final option is ethically weakest because it converts status into privilege and creates an appearance of impropriety. A general, evidence-based urgency route may be defensible if it protects comparable claims and records reasons.\n\nThe officer should give frank written advice, propose lawful alternatives, disclose any personal connection, preserve the file record and communicate criteria to affected applicants. Affected persons should receive an intelligible opportunity to challenge a material departure. If a lawful final decision is made after advice, it should be implemented neutrally. Accountability requires auditability and an appeal route; leadership requires resisting informal pressure without public grandstanding. The conclusion is principled facilitation: accelerate public purpose through transparent rules, never through selective exception.",
    },
    {
        "marks": 20,
        "question": "Design an ethically accountable grievance-redress system for a digitally administered welfare programme.",
        "answer": "A grievance system should treat a complaint as both service information and a citizen's claim to fair hearing. It must begin with accessible multi-channel entry: online, assisted offline, telephone and local facilitation, with disability and language support. Each complaint should receive acknowledgement, a tracking number, time standard, responsible officer and protection against retaliation. Data should identify recurring exclusion without exposing complainants unnecessarily.\n\nAt decision stage, the officer should verify facts, hear the claimant where adverse action is possible, apply published eligibility criteria, give a speaking reason and provide correction, compensation or referral where warranted. Automated rejection must have a prompt human-review route; technology can reduce arbitrary discretion but cannot transfer accountability to an algorithm. Escalation, independent appeal, conflict screening and audit logs protect impartiality.\n\nThe June 2026 DARPG CPGRAMS report can illustrate monitoring: it reports high disposal and pendency indicators. Those metrics are useful for timeliness and managerial review, but they do not establish that every disposal was correct, fair, satisfactory or free from misconduct. The dashboard should therefore report quality sampling, reversal on appeal, repeat grievances, accessibility outcomes and action on systemic causes alongside volume and time.\n\nNolan openness, honesty and accountability require public standards, anonymised performance disclosure and documented correction. Senior leaders should review patterns rather than reward closure alone, and publish action on persistent causes promptly. The system thereby joins efficiency with dignity, remedy, equality and answerability.",
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
    _panel("1. Public trust chain", "linear-trust-chain", (
        "Public office", "Entrusted power", "Public purpose", "Integrity",
        "Impartiality", "Reasons", "Scrutiny", "Trust",
    ), "Status heightens restraint and answerability.", "Open a public-service-values answer."),
    _panel("2. Nolan public-life rail", "seven-value-rail", (
        "Selflessness", "Integrity", "Objectivity", "Accountability",
        "Openness", "Honesty", "Leadership", "Defensible action",
    ), "Use Nolan as an ARC-cited checklist, not an India-specific code.", "Use in values and Code-of-Ethics answers."),
    _panel("3. Status and role morality", "role-duty-ladder", (
        "Status", "Authority", "Information", "Asymmetry",
        "Higher duty", "Restraint", "Public confidence", "Legitimacy",
    ), "Role duty serves constitutional public purpose.", "Use for 2019 public-servant demand."),
    _panel("4. Constitutional decision boundary", "values-gate", (
        "Constitution", "Equality", "Dignity", "Rule of law",
        "Non-arbitrariness", "Due process", "Reasons", "Review",
    ), "Neutrality never excuses constitutional indifference.", "Use for political-executive directions."),
    _panel("5. Public-private interface", "interface-map", (
        "Family or finance", "Official power", "Risk", "Disclosure",
        "Screening", "Recusal or conditions", "Audit", "Trust",
    ), "Private interest must be managed before it distorts public duty.", "Use for conflict-of-interest questions."),
    _panel("6. Conflict management ladder", "three-type-ladder", (
        "Actual conflict", "Immediate decision", "Recusal", "Potential conflict",
        "Interest register", "Apparent conflict", "Transparent reasons", "Confidence test",
    ), "Scale safeguards to materiality; disclosure alone is not resolution.", "Use for 2018 Q3(a)."),
    _panel("7. Legality, morality and propriety", "three-lens-comparison", (
        "Legal validity", "Moral duty", "Propriety", "Public purpose",
        "Constitutional boundary", "Public reasons", "Oversight", "Verdict",
    ), "Legal permission is necessary but may not complete ethical justification.", "Use in law-versus-ethics answers."),
    _panel("8. Bounded discretion", "decision-gate", (
        "Rule gap", "Authority", "Relevant facts", "Equal criteria",
        "Proportionality", "Written reasons", "Review", "Learning",
    ), "Discretion is reviewable judgment, not personal freedom.", "Use for emergency and service-delivery cases."),
    _panel("9. Dilemma resolution sequence", "ethical-decision-flow", (
        "Facts", "Stakeholders", "Competing duties", "Legal floor",
        "Realistic options", "Ethical tests", "Choice", "Residual-harm mitigation",
    ), "Name genuine conflict before choosing a proportionate response.", "Use for 2018 Q5(b) and cases."),
    _panel("10. Neutrality and elected mandate", "dual-accountability-map", (
        "Elected mandate", "Frank advice", "Recorded dissent", "Lawful direction",
        "Neutral implementation", "No favour", "Accountability", "Continuity",
    ), "Advise frankly; implement lawful decisions without partisanship.", "Use for political neutrality."),
    _panel("11. Accountability loop", "feedback-loop", (
        "Duty", "Decision", "Record", "Transparency",
        "Answerability", "External scrutiny", "Remedy", "Institutional learning",
    ), "Responsibility becomes accountability through scrutiny and correction.", "Use with CPGRAMS and grievance cases."),
    _panel("12. Mains answer spine", "answer-writing-spine", (
        "Define", "Distinguish", "Evidence", "Stakeholders",
        "Options", "Ethical test", "Implementation", "Qualified conclusion",
    ), "A reasoned, reviewable verdict outperforms a moral slogan.", "Use in every Topic 09 Mains response."),
)

CURRENT_ANCHOR = {
    "title": "DARPG CPGRAMS Monthly Report for Central Ministries/Departments, June 2026",
    "verified_facts": (
        "The official report is the 50th edition of the CPGRAMS monthly report series.",
        "June 2026 was the 48th consecutive month in which Central Secretariat disposal exceeded one lakh grievances.",
        "The report records 78,793 pending grievances, with about 68% pending for less than 21 days.",
        "It records 83,544 new registrations, 1,96,133 grievances received and 1,99,968 grievances redressed.",
    ),
    "administrative_link": (
        "⚠️ Inference, not an official ethical classification: disposal, pendency, registration and "
        "redress indicators illustrate answerability and administrative monitoring. They can support "
        "discussion of accountable public service when combined with speaking reasons, review and remedy."
    ),
    "limit": (
        "Disposal and pendency data do not establish correctness, fairness, satisfaction, impartiality "
        "or absence of misconduct. Do not infer any of those conclusions from the reported metrics."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://darpg.gov.in/static/uploads/2026/07/45cfe50c8de7d2ad837dfabe72bffced.pdf",
    "https://darpg.gov.in/documents/reports/cpgrams-monthly-report-centre-ETN0QTMtQWa?pageTitle=CPGRAMS-Monthly-Report-Centre",
)

SOURCE_CAVEAT = (
    "The Topic 09 Basic and Advanced owners are controlling sources for public-service values, "
    "Nolan principles, conflict-of-interest taxonomy, coercion/undue influence and dilemma diagnosis. "
    "Topic 09 interfaces with but must not duplicate Topic 10 (laws, rules and conscience), Topic 11 "
    "(accountability), Topic 14 (probity), Topic 16 (Codes of Ethics/Conduct) and Topic 22 (complete "
    "case-study architecture). The Nolan wording cited by ARC is the 1995 UK formulation, not a claim "
    "about the current UK wording. A Code of Conduct should not be called sanctionable solely on ARC "
    "2.2.6 wording. A genuine dilemma is not every unethical act; do not describe GS-IV cases as "
    "almost entirely genuine dilemmas. Treat the 2024 Code-of-Ethics statement as a PYQ premise, not "
    "a universal current-status finding. Constitutional morality is primarily cross-owned; 2025 Q1(b) "
    "must not be claimed as a direct Topic 09 route. Historical ledger labels may be neutral renderings: "
    "quote official wording only where verified against the stated local GS-IV PDF."
)

REGISTER_SUPPLEMENT = (
    "PUBLIC OFFICE — power, status and information are held in trust; role morality requires faithful, "
    "competent, impartial service but cannot override constitutional equality, dignity or legality. "
    "NOLAN/ARC — selflessness; integrity; objectivity; accountability; openness; honesty; leadership. "
    "Integrity manages compromising obligations; objectivity is merit procedure; honesty includes "
    "interest declaration; accountability is answerability to scrutiny. PUBLIC/PRIVATE — actual conflict: "
    "declare, recuse, reassign; potential: disclose/register/screen; apparent: transparent reasons and "
    "confidence test. Disclosure alone does not cure a material conflict. NORMS — legality is a floor; "
    "morality tests duty and fairness; propriety protects public confidence beyond criminal liability. "
    "DISCRETION — authority, relevant facts, equal criteria, proportionality, reasons, review. DILEMMA — "
    "facts -> stakeholders -> competing legitimate duties -> legal floor -> options -> duty/consequence/"
    "virtue tests -> proportionate choice -> implementation and residual-risk mitigation. POWER — coercion "
    "uses threat; undue influence exploits dependency without overt threat. NEUTRALITY — give frank "
    "non-partisan advice; record material dissent; implement lawful final decisions without favour or fear. "
    "METRICS — CPGRAMS data illustrate monitoring, never by themselves fairness, correctness, satisfaction "
    "or integrity. ANSWER SPINE — define precisely, distinguish close concepts, use one verified example, "
    "state safeguards and conclude with a reviewable constitutional-public-interest verdict."
)
