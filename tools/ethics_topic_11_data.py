"""Learner-v2 source data: Ethics Topic 11, Accountability and Ethical Governance."""

SESSION_TITLES = (
    "Accountability, responsibility and the complete accountability relationship",
    "Internal, external and social control architecture",
    "How ethical accountability operates in public administration",
    "Indian applications: audit, social audit, political control and digital governance",
    "Must-know facts and close-option accountability traps",
    "PYQ ownership, cross-links and answer architecture",
    "Mains angles and accountability-mechanism selection",
    "Social capital as an informal accountability resource",
    "Directive decoding and mark-scaled answer construction",
    "Study links, audited PYQ routes and final synthesis",
)

SESSION_GROUPS = (
    ("1",),
    ("2",),
    ("3",),
    ("4",),
    ("5", "6"),
    ("7",),
    ("8",),
    ("9", "10"),
    ("11",),
    ("12",),
)

MCQ_ITEMS = (
    {
        "label": "Accountability is a complete institutional relationship",
        "statement": (
            "Accountability requires an identifiable actor, a competent forum, a known standard, "
            "an explanation, a judgment and a credible route to correction, remedy or consequence."
        ),
        "scenario_a": (
            "A mission director uploads expenditure data but no authority reviews anomalies or orders "
            "correction. Which missing relationship prevents transparency from becoming accountability?"
        ),
        "scenario_b": (
            "A district officer must explain a decision against published standards before an appellate "
            "authority that can reverse it and compensate the claimant. Which concept is complete here?"
        ),
        "family": "accountability foundations",
        "group": "accountability foundations",
    },
    {
        "label": "Responsibility and accountability are distinct",
        "statement": (
            "Responsibility is the duty assigned to a role, whereas accountability arises when performance "
            "must be explained and justified before a forum capable of judgment and follow-up."
        ),
        "scenario_a": (
            "A block officer is assigned responsibility for wage payments but no one can demand reasons "
            "for delay or order relief. Which additional concept is absent?"
        ),
        "scenario_b": (
            "A secretary argues that a subordinate alone is accountable because the subordinate entered "
            "the data, although the secretary approved the process. Which distinction should be applied?"
        ),
        "family": "accountability foundations",
        "group": "accountability foundations",
    },
    {
        "label": "Accountability works before and after a decision",
        "statement": (
            "Standards, assigned roles, records and reporting create ex-ante discipline, while review, "
            "judgment, correction, remedy and proportionate consequences provide ex-post accountability."
        ),
        "scenario_a": (
            "A procurement platform requires prior conflict declarations and later permits audit and appeal. "
            "Which temporal understanding of accountability does this illustrate?"
        ),
        "scenario_b": (
            "A department treats accountability solely as punishment after loss has occurred. Which broader "
            "preventive and corrective understanding has it overlooked?"
        ),
        "family": "accountability foundations",
        "group": "accountability foundations",
    },
    {
        "label": "Transparency is necessary but not sufficient",
        "statement": (
            "Disclosure and dashboards improve visibility, but accountability additionally needs responsible "
            "actors, review against standards, reasoned findings and enforceable correction or remedy."
        ),
        "scenario_a": (
            "A state publishes real-time welfare exclusions but provides no human review or grievance remedy. "
            "Why is the system transparent yet incompletely accountable?"
        ),
        "scenario_b": (
            "A dashboard flags delayed pensions and names the reviewing officer, appeal authority and correction "
            "deadline. Which addition converts information into institutional control?"
        ),
        "family": "accountability foundations",
        "group": "accountability foundations",
    },
    {
        "label": "Departmental vigilance and CVOs are internal controls",
        "statement": (
            "Departmental vigilance and Chief Vigilance Officers support preventive checks, complaint handling "
            "and disciplinary processes within administration, subject to their actual authority and procedure."
        ),
        "scenario_a": (
            "A ministry asks its Chief Vigilance Officer to examine repeated tender complaints and recommend "
            "preventive controls. Which accountability layer is operating?"
        ),
        "scenario_b": (
            "An officer assumes every vigilance concern must begin as a criminal prosecution. Which differentiated "
            "internal role corrects that assumption?"
        ),
        "family": "institutional roles",
        "group": "institutional roles",
    },
    {
        "label": "The CVC supervises and advises but does not prosecute",
        "statement": (
            "The statutory Central Vigilance Commission performs vigilance, advisory and specified superintendence "
            "functions; it is not itself the body that conducts every investigation or prosecution."
        ),
        "scenario_a": (
            "A department sends a vigilance matter to the CVC and tells citizens that the Commission will itself "
            "prosecute the accused. Which institutional error has occurred?"
        ),
        "scenario_b": (
            "The CVC reviews vigilance administration and exercises its statutory role concerning anti-corruption "
            "investigation without acting as trial prosecutor. Which distinction is preserved?"
        ),
        "family": "institutional roles",
        "group": "institutional roles",
    },
    {
        "label": "The CBI investigates within its lawful remit",
        "statement": (
            "The Central Bureau of Investigation investigates specified offences within the applicable legal and "
            "jurisdictional framework; investigation, vigilance advice and departmental discipline remain distinct functions."
        ),
        "scenario_a": (
            "A ministry asks whether suspected bribery requires criminal investigation rather than only an internal "
            "process. Which differentiated role becomes relevant?"
        ),
        "scenario_b": (
            "A disciplinary authority waits for a vigilance body to perform every criminal-investigation function. "
            "Which institutional separation has been ignored?"
        ),
        "family": "institutional roles",
        "group": "institutional roles",
    },
    {
        "label": "CAG and legislative scrutiny provide external accountability",
        "statement": (
            "Independent CAG audit examines public expenditure and performance for legislative scrutiny and systemic "
            "correction; it remains indispensable even when departments possess internal or concurrent controls."
        ),
        "scenario_a": (
            "A department claims its internal dashboard makes independent constitutional audit unnecessary. Which "
            "external accountability principle defeats the claim?"
        ),
        "scenario_b": (
            "An audit report is placed before the legislature for committee examination and executive follow-up. "
            "Which control layer does this exemplify?"
        ),
        "family": "institutional roles",
        "group": "institutional roles",
    },
    {
        "label": "Political and bureaucratic accountability are related but separate",
        "statement": (
            "Ministers answer to the legislature and electorate for policy and departmental outcomes, while officials "
            "answer for lawful, impartial and competent advice, execution, records and use of discretion."
        ),
        "scenario_a": (
            "A secretary gives frank recorded advice, then implements a lawful cabinet decision impartially. Which "
            "division of democratic and administrative accountability is respected?"
        ),
        "scenario_b": (
            "A minister directs a transfer for partisan retaliation and the official complies without recording objection. "
            "Which accountability boundary has failed?"
        ),
        "family": "control and assurance",
        "group": "control and assurance",
    },
    {
        "label": "Lawful political direction does not erase official accountability",
        "statement": (
            "Civil servants must implement lawful democratic decisions without partisan obstruction, but illegality, "
            "discrimination or concealed favour requires reasoned advice, recorded dissent and competent escalation."
        ),
        "scenario_a": (
            "An officer invokes neutrality to delay a lawful elected-government welfare decision. Which duty within "
            "bureaucratic accountability has been neglected?"
        ),
        "scenario_b": (
            "A superior demands selective benefits for supporters, and the field officer seeks written directions and "
            "review. Which accountable response is illustrated?"
        ),
        "family": "control and assurance",
        "group": "control and assurance",
    },
    {
        "label": "Concurrent assurance complements independent ex-post audit",
        "statement": (
            "Transaction checks, internal audit and real-time exception review can correct problems during implementation, "
            "but they complement rather than replace CAG audit and legislative scrutiny."
        ),
        "scenario_a": (
            "A treasury system flags duplicate payments before release while later CAG audit tests propriety and performance. "
            "Which complementary design is operating?"
        ),
        "scenario_b": (
            "A department argues that an internal real-time alert conclusively settles responsibility for public loss. "
            "Which continuing external requirement is missing?"
        ),
        "family": "control and assurance",
        "group": "control and assurance",
    },
    {
        "label": "Accountability diffusion weakens responsibility-fixing",
        "statement": (
            "When authority, data entry, approval and review are scattered across many unnamed levels, citizens and forums "
            "cannot identify who must explain failure or deliver correction."
        ),
        "scenario_a": (
            "Five offices refer a pensioner to one another because no process assigns a final deciding officer. Which "
            "structural accountability failure is present?"
        ),
        "scenario_b": (
            "A scheme publishes a responsibility matrix, escalation deadline and final appellate authority. Which problem "
            "does this design reduce?"
        ),
        "family": "control and assurance",
        "group": "control and assurance",
    },
    {
        "label": "Social audit requires independent verification and public hearing",
        "statement": (
            "A credible social audit separates verification from the implementing agency, proactively opens records, tests "
            "them with workers and worksites, and presents findings in a public hearing."
        ),
        "scenario_a": (
            "A Gram Panchayat verifies its own muster rolls privately and announces that a social audit is complete. Which "
            "essential safeguards are absent?"
        ),
        "scenario_b": (
            "Workers compare disclosed muster rolls with attendance and physical works before a Gram Sabha hearing. Which "
            "accountability mechanism is operating?"
        ),
        "family": "social accountability",
        "group": "social accountability",
    },
    {
        "label": "Social audit is incomplete without action and remedy",
        "statement": (
            "Findings must lead to a time-bound action-taken report, worker remedy, recovery or disciplinary referral where "
            "evidence supports it, and safeguards against intimidation or capture."
        ),
        "scenario_a": (
            "A public hearing establishes unpaid wages, but the report is archived without payment correction or action. "
            "Which part of social accountability has failed?"
        ),
        "scenario_b": (
            "An independent unit protects witnesses, publishes follow-up and restores wrongly withheld wages. Which complete "
            "social-audit cycle is illustrated?"
        ),
        "family": "social accountability",
        "group": "social accountability",
    },
    {
        "label": "Bridging social capital can strengthen social control",
        "statement": (
            "Trust and cooperation across groups can lower the cost of collective monitoring, testimony and participation, "
            "thereby strengthening citizen oversight between formal audit cycles."
        ),
        "scenario_a": (
            "Workers from different hamlets jointly verify scheme records and support complainants against a powerful contractor. "
            "Which governance resource assists accountability?"
        ),
        "scenario_b": (
            "A grievance forum fails because communities distrust one another and witnesses fear isolation. Which informal "
            "resource is deficient?"
        ),
        "family": "social accountability",
        "group": "social accountability",
    },
    {
        "label": "Bonding capital can shield wrongdoing",
        "statement": (
            "Strong in-group loyalty may protect insiders, silence complainants and capture local oversight; social capital "
            "improves governance only when it is sufficiently inclusive and rights-respecting."
        ),
        "scenario_a": (
            "A dominant local network pressures members not to testify against a related functionary during a public hearing. "
            "Which limitation of social capital is visible?"
        ),
        "scenario_b": (
            "An audit team assumes community cohesion always guarantees honest monitoring. Which close-option qualification "
            "should correct that view?"
        ),
        "family": "social accountability",
        "group": "social accountability",
    },
    {
        "label": "E-governance can improve traceability and access",
        "statement": (
            "Digital records, time stamps, workflow visibility and remote service channels can reduce delay, record tampering "
            "and opaque discretion when responsibilities and review duties are clearly assigned."
        ),
        "scenario_a": (
            "A benefit portal time-stamps every decision, identifies the deciding officer and permits appeal. Which ethical "
            "advantage of e-governance is most direct?"
        ),
        "scenario_b": (
            "A department digitises files but leaves exception review and correction unassigned. Why has visibility not yet "
            "created full accountability?"
        ),
        "family": "digital ethical governance",
        "group": "digital ethical governance",
    },
    {
        "label": "Digital exclusion requires assisted and offline access",
        "statement": (
            "Online administration must address connectivity, language, disability and literacy barriers through assisted "
            "access, workable offline alternatives and equal treatment of comparable claimants."
        ),
        "scenario_a": (
            "Elderly pensioners lose benefits because the only filing channel requires a smartphone and English literacy. "
            "Which ethical safeguard is missing?"
        ),
        "scenario_b": (
            "A district offers village facilitation, paper fallback and disability support alongside its portal. Which "
            "e-governance duty is fulfilled?"
        ),
        "family": "digital ethical governance",
        "group": "digital ethical governance",
    },
    {
        "label": "Authentication error needs prompt human review",
        "statement": (
            "Biometric or automated failure should not become final deprivation; accountable design requires a human decision-maker, "
            "speaking reasons, correction of records and a timely offline remedy."
        ),
        "scenario_a": (
            "A worker's attendance is rejected after repeated biometric failure and no official can override the system. Which "
            "ethical design defect is decisive?"
        ),
        "scenario_b": (
            "An officer verifies alternate evidence, records reasons and corrects an erroneous automated exclusion. Which safeguard "
            "turns technology into accountable assistance?"
        ),
        "family": "digital ethical governance",
        "group": "digital ethical governance",
    },
    {
        "label": "Digital accountability includes privacy and explainability",
        "statement": (
            "Data collection and automated decisions require necessity, security, intelligible criteria, audit logs and review; "
            "administrative efficiency does not justify opaque profiling or excessive disclosure."
        ),
        "scenario_a": (
            "A welfare dashboard publicly displays identifiable health details to demonstrate transparency. Which competing ethical "
            "duty has been breached?"
        ),
        "scenario_b": (
            "A vendor model rejects applications without intelligible reasons or departmental review. Which accountability "
            "requirements are absent?"
        ),
        "family": "digital ethical governance",
        "group": "digital ethical governance",
    },
    {
        "label": "MGNREGA restoration begins with record reconciliation",
        "statement": (
            "Restoring scheme integrity requires reconciling job cards, employment demand, muster rolls, attendance, wage payments, "
            "technical sanctions and physical assets before fixing responsibility."
        ),
        "scenario_a": (
            "A district finds payments without visible work and immediately suspends all village employment. Which evidence-based "
            "restoration step should precede indiscriminate closure?"
        ),
        "scenario_b": (
            "Teams compare demand registers, rolls, bank credits and assets work by work. Which accountability method is being used?"
        ),
        "family": "MGNREGA restoration",
        "group": "MGNREGA restoration",
    },
    {
        "label": "Recovery and discipline must follow evidence and due process",
        "statement": (
            "Where reconciliation supports wrongdoing, authorities should secure records, hear affected persons and initiate proportionate "
            "recovery, disciplinary or criminal referral under competent procedures."
        ),
        "scenario_a": (
            "An administrator orders recovery from every field worker before verifying roles or giving a hearing. Which accountability "
            "standard is violated?"
        ),
        "scenario_b": (
            "Verified ghost payments are mapped to approving roles and referred through lawful recovery and investigation channels. Which "
            "corrective principle is applied?"
        ),
        "family": "MGNREGA restoration",
        "group": "MGNREGA restoration",
    },
    {
        "label": "Accountability must restore service, not only punish",
        "statement": (
            "Ethical correction includes unpaid wages, accurate job cards, valid work demand, grievance closure and improved process, "
            "alongside responsibility-fixing and deterrent action."
        ),
        "scenario_a": (
            "Officials arrest an intermediary but leave genuine workers unpaid and records corrupted. Which remedial dimension remains incomplete?"
        ),
        "scenario_b": (
            "A district pays verified arrears, corrects records and redesigns controls while pursuing culpable actors. Which balanced approach is shown?"
        ),
        "family": "MGNREGA restoration",
        "group": "MGNREGA restoration",
    },
    {
        "label": "Monitoring technology does not prove outcome quality",
        "statement": (
            "Biometric authentication, mobile monitoring, dashboards and public disclosure can strengthen traceability, yet their presence "
            "does not by itself prove fairness, work quality, correct payment or effective remedy."
        ),
        "scenario_a": (
            "A district declares a scheme ethically successful solely because every worksite uploads mobile attendance. Which inference is unjustified?"
        ),
        "scenario_b": (
            "Officials combine digital monitoring with field verification, social audit and grievance correction. Which qualified use of technology is defensible?"
        ),
        "family": "MGNREGA restoration",
        "group": "MGNREGA restoration",
    },
)

PYQS = (
    {
        "year": 2019,
        "question": (
            "GS-IV Q1(a): What are the basic principles of public life? Illustrate any three of these with "
            "suitable examples. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact wording verified against books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, "
            "page 2. Shared with Topics 04 and 09; Topic 11 uses accountability as one principle and "
            "does not claim exclusive ownership."
        ),
        "answer": (
            "The ARC reproduces the Nolan principles of public life: selflessness, integrity, objectivity, "
            "accountability, openness, honesty and leadership. They convert public power into a trust rather "
            "than a personal privilege.\n\n"
            "Accountability requires an officer to explain a decision before appropriate scrutiny and accept "
            "correction. A district programme director should disclose beneficiary criteria, answer audit "
            "queries and restore an excluded eligible claimant. Objectivity requires decisions on stated merit; "
            "a recruitment board should use published scoring rather than political recommendation. Integrity "
            "requires avoiding compromising obligations; a tender member should disclose a relative's bid and "
            "recuse where the conflict is material.\n\n"
            "Openness is qualified by lawful confidentiality, while leadership requires seniors to model these "
            "standards. The principles should be applied with Indian constitutional equality, dignity and due "
            "process. Their ethical value lies not in recital but in reviewable procedures, remedies and conduct "
            "that retain public confidence."
        ),
    },
    {
        "year": 2019,
        "question": (
            "GS-IV Q8: Honesty and uprightness are the hallmarks of a civil servant. Civil servants "
            "possessing these qualities are considered as the backbone of any strong organization. In line "
            "of duty, they take various decisions, at times some become bonafide mistakes. As long as such "
            "decisions are not taken intentionally and do not benefit personally, the officer cannot be said "
            "to be guilty. Though such decisions may, at times, lead to unforeseen adverse consequences in "
            "the long-term. In the recent past, a few instances have surfaced wherein civil servants have been "
            "implicated for bonafide mistakes. They have often been prosecuted and even imprisoned. These "
            "instances have greatly rattled the moral fibre of the civil servants. How does this trend affect "
            "the functioning of the civil services? What measures can be taken to ensure that honest civil "
            "servants are not implicated for bonafide mistakes on their part? Justify your answer. "
            "(Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Full official case wording and both demands verified against "
            "books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 5. Topic 21 is the "
            "primary protection-of-honest-officials owner; Topic 11 supplies fair accountability design."
        ),
        "answer": (
            "Indiscriminate implication of honest officials converts accountability into fear. It encourages "
            "delay, excessive referral, avoidance of innovation and defensive documentation designed for self-protection "
            "rather than public service. Capable officers may avoid sensitive posts, while dishonest actors can exploit "
            "collective indecision. Yet blanket immunity would create impunity; good faith cannot excuse corruption, gross "
            "negligence or concealed conflict.\n\n"
            "The correct design separates error, negligence and misconduct. Investigators should examine authority, facts "
            "available at the time, recorded reasons, personal benefit, conflict, due diligence and whether similarly placed "
            "decisions were treated consistently. Preliminary scrutiny should be competent, time-bound and insulated from "
            "political retaliation. Speaking reasons should accompany prosecution sanction or disciplinary initiation. "
            "Independent review and appeal can correct malicious or mechanically framed cases.\n\n"
            "Administratively, clear delegations, updated manuals, written directions, legal and financial advice, decision "
            "logs and peer consultation reduce honest error. Training should distinguish a reasonable policy failure from "
            "mala fide action. Protection must remain conditional: destruction of records, deliberate disregard of safety, "
            "private gain or repeated reckless conduct warrants action.\n\n"
            "Thus fair accountability protects both citizens and honest discretion. It asks an identifiable actor to explain "
            "conduct against known standards, but attaches consequence only after evidence, judgment and due process. Such a "
            "system promotes courageous, reasoned administration without normalising either paralysis or immunity."
            " Periodic anonymised review of closed cases can reveal retaliatory patterns and improve standards "
            "without prejudging individual guilt in practice."
        ),
    },
    {
        "year": 2019,
        "question": (
            "GS-IV Q10: In a modern democratic polity, there is the concept of political executive and "
            "permanent executive. Elected people's representatives form the political executive and bureaucracy "
            "forms the permanent executive. Ministers frame policy decisions and bureaucrats execute these. In "
            "the initial decades after independence, relationship between the permanent executive and the political "
            "executive were characterized by mutual understanding, respect and co-operation, without encroaching "
            "upon each others domain. However, in the subsequent decades, the situation has changed. There are "
            "instances of the political executive insisting upon the permanent executive to follow its agenda. "
            "Respect for and appreciation of upright bureaucrats has declined. There is an increasing tendency "
            "among the political executive to get involved in routine administrative matters such as transfers, "
            "postings etc. Under this scenario, there is a difinitive trend towards 'politicization of bureaucracy'. "
            "The rising materialism and acquisitiveness in social life has also adversely impacted upon the ethical "
            "values of both the permanent executive and the political executive. What are the consequences of this "
            "'politicization of bureaucracy'? Discuss. (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Exact official wording, including the paper's spellings, verified against "
            "books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 6. Topic 11 owns the "
            "political-versus-bureaucratic accountability analysis; Topic 09 cross-links neutrality."
        ),
        "answer": (
            "Democratic administration needs both political responsiveness and a professional permanent executive. "
            "Ministers possess electoral legitimacy to choose lawful policy; officials owe frank advice, impartial "
            "execution and continuity. Politicisation arises when partisan loyalty, transfers, postings or patronage "
            "displace these role boundaries.\n\n"
            "Its consequences are serious. Fear of transfer weakens truthful advice and encourages anticipatory obedience. "
            "Recruitment, contracts, policing and welfare may become selectively administered, eroding equality and citizen "
            "trust. Frequent personnel changes destroy institutional memory, long-term planning and responsibility-fixing. "
            "Upright officers become isolated while compliant networks gain protection, diffusing accountability between "
            "minister and official. Legislative accountability also suffers when policy direction and operational interference "
            "are deliberately blurred. Conversely, bureaucratic resistance to every elected priority can become an undemocratic "
            "veto.\n\n"
            "Reform should therefore protect the relationship, not sever it. Clear tenure and transparent transfer criteria, "
            "written directions, civil-services boards where applicable, reasoned files, conflict disclosure and legislative "
            "scrutiny can expose improper intervention. Officials should record material legal and ethical objections, offer "
            "workable alternatives and implement lawful final decisions without partisan favour. Ministers should remain "
            "answerable for policy and departmental outcomes; officials should remain answerable for legality, competence and "
            "execution.\n\n"
            "The ethical objective is responsive neutrality: democratic direction bounded by constitutional values and "
            "professional administration protected by records, review and consequences for abuse."
            " Public reporting of transfer patterns and committee examination of repeated interference can add deterrence "
            "without preventing legitimate administrative reassignment itself."
        ),
    },
    {
        "year": 2021,
        "question": (
            "GS-IV Q6(a): An independent and empowered social audit mechanism is an absolute must in "
            "every sphere of public service, including judiciary, to ensure performance, accountability "
            "and ethical conduct. Elaborate. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3. Topic 11 is "
            "the primary accountability route; institutional feasibility must be tailored to each sphere."
        ),
        "answer": (
            "Social audit converts citizens from passive recipients into participants who test official records against "
            "lived outcomes. Independence from the implementing body, proactive disclosure, access to records, verification "
            "with users and a public hearing can reveal exclusion, false reporting and poor performance that ordinary files conceal.\n\n"
            "Its accountability value depends on follow-up. Findings need a time-bound action-taken report, correction or "
            "compensation, recovery or disciplinary referral where evidence supports it, and protection against intimidation. "
            "For MGNREGA, workers can compare job cards, muster rolls, wages and physical works. In other public services, the "
            "design must respect confidentiality, decisional independence and lawful review; citizen participation cannot become "
            "mob pressure on judges or adjudication.\n\n"
            "Thus the proposition is strongest as a demand for independent public verification and enforceable response, adapted "
            "to institutional function. Disclosure without competent judgment and remedy remains transparency, not complete accountability."
        ),
    },
    {
        "year": 2021,
        "question": (
            "GS-IV Q9: An elevated corridor is being constructed to reduce traffic congestion in the "
            "capital of a particular state. You have been selected as project manager of this prestigious "
            "project on your professional competence and experience. The deadline is to complete the project "
            "in next two years by 30 June, 2021, since this project is to be inaugurated by the Chief Minister "
            "before the elections are announced in the second week of July 2021. While carrying out the "
            "surprise inspection by inspecting team, a minor crack was noticed in one of the piers of the "
            "elevated corridor possibly due to poor material used. You immediately informed the chief engineer "
            "and stopped further work. It was assessed by you that minimum three piers of the elevated corridor "
            "have to be demolished and reconstructed. But this process will delay the project minimum by four "
            "to six months. But the chief engineer overruled the observation of inspecting team on the ground "
            "that it was a minor crack which will not in any way impact the strength and durability of the bridge. "
            "He ordered you to overlook the observation of inspecting team-and continue working with same speed "
            "and tempo. He informed you that the minister does not want any delay as he wants the Chief Minister "
            "to inaugurate the elevated corridor before the elections are declared. Also informed you that the "
            "contractor is far relative of the minister and he wants him to finish the project. He also gave you "
            "hint that your further promotion as additional chief engineer is under consideration with the ministry. "
            "However, you strongly felt that the minor crack in the pier of the elevated corridor will adversely "
            "affect the health and life of the bridge and therefore it will be very dangerous not to repair the "
            "elevated corridor. (a) Under the given conditions, what are the options available to you as a project "
            "manager? (b) What are the ethical dilemmas being faced by the project manager? (c) What are the "
            "professional challenges likely to be faced by the project manager and his response to overcome such "
            "challenges? (d) What can be the consequences of overlooking the observation raised by the inspecting "
            "team? (Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "Full facts and all four official demands verified against "
            "books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 7. Shared with "
            "Topics 09 and 22; Topic 11 supplies responsibility-fixing, scrutiny and corrective action."
        ),
        "answer": (
            "The project manager may obey and continue; resign or seek transfer; stop work unilaterally; or preserve the stop, "
            "seek an independent structural assessment and escalate through competent technical, administrative and vigilance "
            "channels. Stakeholders are commuters, workers, taxpayers, the government, contractor, inspecting team and future users.\n\n"
            "The dilemmas are safety versus deadline, professional integrity versus hierarchy, public interest versus career, "
            "and fair contracting versus ministerial relationship. Obedience risks catastrophic harm, criminal or disciplinary "
            "exposure, wasted public money and loss of trust. Immediate resignation protects personal conscience but abandons the "
            "public project. Unsupported public allegation may compromise due process. A reasoned technical escalation is strongest.\n\n"
            "The manager should secure the site and records, obtain the inspection report, seek written directions and request an "
            "independent expert test. He should document the conflict involving the contractor, inform the competent authority and "
            "vigilance channel, and propose reconstruction with a revised schedule. Retaliation risk should be recorded through "
            "prescribed review channels. No reopening should occur until safety is certified by competent independent expertise.\n\n"
            "Ignoring the crack can cause death, structural failure, escalation of repair cost, evidence destruction and institutional "
            "impunity. Accountability is not merely later blame: ex-ante standards, traceable decisions and the power to halt and correct "
            "unsafe work are essential. Professional courage therefore requires evidence-based resistance joined to lawful escalation."
            " A documented handover should preserve continuity if retaliation removes the manager from the project without warning."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q4(a): What do you understand by the term 'good governance'? How far recent initiatives "
            "in terms of e-Governance steps taken by the State have helped the beneficiaries? Discuss with "
            "suitable examples. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 3. "
            "Topic 11 owns the accountability-and-e-governance route; other governance topics may cross-link."
        ),
        "answer": (
            "Good governance is lawful, participatory, transparent, responsive, effective, equitable and accountable exercise of public "
            "authority. E-governance can advance it through time-stamped records, reduced physical discretion, remote access, direct benefit "
            "transfer, online certificates and trackable grievances. A beneficiary can know application status and challenge delay rather "
            "than depend entirely on an intermediary.\n\n"
            "Its success is conditional. Connectivity, language, disability and digital-literacy barriers may exclude the weakest. Biometric "
            "failure, poor data, privacy risks and opaque automated rejection can move discretion into technology rather than remove it. "
            "Dashboards show transactions but do not establish fairness or remedy.\n\n"
            "Therefore beneficiary-centred e-governance needs assisted and offline channels, data minimisation, accessible design, audit logs, "
            "speaking reasons, human review and appeal. Technology improves good governance when it makes the responsible officer, standard, "
            "decision and correction route more visible; digitisation without review merely automates administrative weakness."
        ),
    },
    {
        "year": 2022,
        "question": (
            "GS-IV Q4(b): Online methodology is being used for day-to-day meetings, institutional approvals "
            "in the administration and for teaching and learning in education sector to the extent telemedicine "
            "in the health sector is getting popular with the approvals of the competent authority. No doubt, "
            "it has advantages and disadvantages for both the beneficiaries and the system at large. Describe "
            "and discuss the ethical issues involved in the use of online method particularly to the vulnerable "
            "section of the society. (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 3. Topic 11 "
            "uses it for inclusive and accountable e-governance; technology ethics also cross-links Topic 13."
        ),
        "answer": (
            "Online methods improve reach, continuity, speed, recordability and reduced travel. Telemedicine can connect remote patients; "
            "digital approvals can create time-stamped trails. Yet vulnerable persons may lack devices, connectivity, literacy, language support, "
            "privacy or a safe place to participate. Persons with disabilities may face inaccessible interfaces, while authentication and data "
            "errors can deny essential services.\n\n"
            "Other concerns are weak informed consent, confidential data leakage, opaque algorithms, vendor dependence, reduced human attention "
            "and difficulty contesting an automated outcome. Formal approval by a competent authority does not by itself resolve these ethical harms.\n\n"
            "The response is hybrid and rights-sensitive: assisted access, meaningful offline alternatives, accessible design, minimal data collection, "
            "security, intelligible reasons, human review and prompt appeal. Emergency online delivery should be periodically evaluated through user "
            "experience and exclusion data. Efficiency is ethically defensible only when no vulnerable person is left without an accountable path "
            "to service, explanation and remedy."
        ),
    },
    {
        "year": 2023,
        "question": (
            "GS-IV Q6(b): Explain the term social capital. How does it enhance good governance? "
            "(Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 4. "
            "Topic 06 is the primary concept owner; Topic 11 owns the shared social-accountability application."
        ),
        "answer": (
            "Social capital is the network of trust, reciprocity and shared norms that enables people to cooperate. Bridging capital connects different "
            "groups, while bonding capital strengthens ties within a group.\n\n"
            "It enhances good governance by lowering the cost of collective action, improving information, supporting participation and enabling citizens "
            "to monitor services. In an MGNREGA social audit, villagers who trust the process and one another are more willing to compare muster rolls, "
            "testify and protect complainants. Community networks can also communicate local needs quickly and improve compliance through legitimate social norms.\n\n"
            "The effect is not automatically positive. Bonding capital based on caste, kinship or faction may shield insiders, intimidate witnesses or capture "
            "local institutions. Social capital cannot replace CAG audit, departmental control or legal remedy. It strengthens good governance when it is inclusive, "
            "rights-respecting and joined to transparent records, independent verification and enforceable follow-up."
        ),
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q6(b): India is an emerging economic power of the world as it has recently secured the "
            "status of fourth largest economy of the world as per IMF projection. However, it has been observed "
            "that in some sectors, allocated funds remain either underutilised or misutilised. What specific "
            "measures would you recommend for ensuring accountability in this regard to stop leakages and gaining "
            "the status of third largest economy of the world in near future? (Answer in 150 words)"
        ),
        "marks": 10,
        "source_note": (
            "Wording verified from the official local paper, "
            "books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, page 4; the scan's text layer omits part of "
            "one line, which was read with the printed line and canonical Topic 18 owner. Topic 18 is primary; "
            "Topic 11 is only a shared accountability-mechanism cross-link."
        ),
        "answer": (
            "Public-fund accountability begins with clear responsibility for sanction, release, utilisation, output and outcome. Budget heads should have realistic "
            "timelines, measurable milestones and named reviewing officers. Digital transaction trails, procurement controls and concurrent exception checks can identify "
            "idle balances, duplicate payments and delay during implementation.\n\n"
            "These controls must be complemented by independent CAG audit, legislative committee scrutiny, transparent utilisation and outcome reporting, protected complaints "
            "and social audit where beneficiaries can verify delivery. Deviations require speaking explanations, time-bound correction, recovery or disciplinary referral where "
            "evidence supports it, and restoration of affected service.\n\n"
            "Dashboards alone are insufficient: data quality, field verification, human review and grievance remedy are necessary. Outcome evaluation should distinguish honest "
            "implementation difficulty from negligence or diversion. This is primarily a public-fund-utilisation question under Topic 18; Topic 11 contributes the actor-forum-standard-"
            "judgment-remedy architecture that converts expenditure visibility into enforceable accountability."
        ),
    },
    {
        "year": 2025,
        "question": (
            "GS-IV Q11: Mahatma Gandhi National Rural Employment Guarantee Program, MGNREGA was earlier known "
            "as National Rural Employment Scheme, NREGA. It is an Indian Social Welfare Program that aimed at "
            "fulfilling the 'Right to Work' provisions made in the Constitution. MGNREGA was launched in 2006 "
            "under Rural Employment Sector by the Ministry of Rural Development. Main objective of the program "
            "is to give legal guarantee of wage employment to the adult members of rural households who are "
            "willing to do unskilled manual labour work subject to a maximum of 100 days per year for every household. "
            "Every rural household has the right to register under the scheme, job card is issued to the registered, "
            "Job Card holder can seek employment; State Government shall pay 25% of minimum wage for the first 30 "
            "days as compensatory daily unemployment allowance to the families and of wage for remaining period of "
            "the year. MGNREGA work was undertaken by various Gram Panchayats. You have been appointed as an Administrator "
            "Incharge of the District. You have been given the responsibility of monitoring MGNREGA work undertaken by "
            "various Gram Panchayats. You are also given the authority to give technical sanctions to all MGNREGA works. "
            "In one of the Panchayats in your jurisdiction, you notice that your predecessor has mismanaged the Program "
            "in terms of: (i) Money not disbursed to actual job-seekers. (ii) Muster Rolls of the Labourers not properly "
            "maintained. (iii) Mismatch between the work done and payments made. (iv) Payments made to fictitious persons. "
            "(v) Job Cards were given without looking into the need of person. (vi) Mismanagement of funds and to the extent "
            "of siphoning of funds. (vii) Approved works that never existed. (a) What is your reaction to the above situation "
            "and how do you restore the proper functioning of MGNREGA Program in this regard? (b) What actions would you "
            "initiate to solve the various issues listed above? (c) How would you deal with the above situation? "
            "(Answer in 250 words)"
        ),
        "marks": 20,
        "source_note": (
            "All printed facts, seven listed irregularities and all three sub-demands reproduced from the official "
            "local paper, books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, pages 9-10. The facts are a GS-IV hypothetical, "
            "not evidence of programme-wide conditions. Topic 11 owns this case; Topic 18 cross-links public funds."
        ),
        "answer": (
            "My reaction would be firm but evidence-led: protect genuine workers immediately, preserve records and avoid collective suspension of employment. Stakeholders are job-seekers, "
            "Gram Panchayats, field staff, banks, taxpayers, the predecessor and future beneficiaries.\n\n"
            "First, I would constitute an independent multidisciplinary verification team and secure digital and paper records. Work by work, it should reconcile registration and job cards, "
            "dated employment demand, muster rolls and attendance, wage calculations, bank credits, technical sanctions, measurements, bills and physical assets. Genuine unpaid workers should "
            "receive corrected wages and grievance decisions promptly. Duplicate or fictitious identities, payment-work mismatch and nonexistent assets should be mapped to the officials and "
            "intermediaries who entered, verified, approved and paid them.\n\n"
            "Second, an independent social audit should receive proactive records, conduct worker and worksite verification and hold a protected public hearing. Its findings require a published "
            "action-taken report. Where evidence warrants, I would initiate recovery, disciplinary proceedings or criminal referral through competent authorities, after notice and due process. "
            "Complainants and witnesses need anti-intimidation safeguards.\n\n"
            "Finally, I would restore demand registration, accurate job cards, timely muster closure, payment reconciliation, asset verification and accessible grievance channels. Biometric or "
            "mobile monitoring may strengthen traceability, but authentication failure needs human review and offline remedy. Monthly exception review, responsibility matrices and independent audit "
            "would prevent recurrence. The aim is service restoration, responsibility-fixing and institutional correction—not punishment without proof or technology without remedy."
            " That balance sustains trust."
        ),
    },
)

ORIGINAL_MAINS = (
    {
        "marks": 10,
        "question": (
            "Distinguish responsibility from accountability and identify the elements of a complete accountability relationship."
        ),
        "answer": (
            "Responsibility is the duty attached to a role: who must sanction a work, verify a muster roll or decide a grievance. "
            "It exists even if no later scrutiny occurs. Accountability begins when that actor must explain and justify performance "
            "before a forum capable of judgment and follow-up.\n\n"
            "A complete relationship therefore needs an identifiable actor, a competent forum, a known legal, ethical or performance "
            "standard, reliable information, an opportunity and duty to explain, a reasoned judgment, and correction, remedy or proportionate "
            "consequence. In a pension scheme, naming a processing officer assigns responsibility; an appellate authority that reviews delay, "
            "orders payment and records systemic correction supplies accountability.\n\n"
            "Accountability is not only retrospective punishment. Ex-ante standards, records and reporting shape conduct, while ex-post review "
            "and remedy correct failure. Clear responsibility without scrutiny produces unchecked discretion; scrutiny without identifiable "
            "responsibility produces blame diffusion. Ethical governance requires both."
        ),
    },
    {
        "marks": 10,
        "question": (
            "Why does dashboard visibility not by itself amount to accountability in digital governance?"
        ),
        "answer": (
            "A dashboard provides transparency by making transactions, delays or outcomes visible. Accountability is a thicker institutional "
            "relationship. It asks which officer is responsible, what standard applies, who reviews the data, whether the officer must explain "
            "an anomaly, who judges the explanation, and what correction or remedy follows.\n\n"
            "A welfare dashboard may display authentication failures while excluded citizens remain unable to reach a human decision-maker. "
            "It may also contain poor-quality data, conceal unequal access or reward rapid closure through non-speaking replies. Visibility then "
            "creates information without responsibility-fixing.\n\n"
            "An accountable design assigns exception review, preserves audit logs, protects privacy, gives speaking reasons, permits offline and "
            "assisted access, and provides human appeal with authority to restore benefits. Independent audit can test whether reported performance "
            "matches field reality. Thus dashboards are useful evidence and early-warning tools, but become accountability only when joined to "
            "review, judgment and enforceable remedy."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Explain the differentiated roles of departmental vigilance, CVOs, CVC, CBI and CAG in India's accountability architecture."
        ),
        "answer": (
            "India's accountability bodies occupy different locations and perform different functions. Departmental vigilance and Chief Vigilance "
            "Officers are internal controls. They support preventive vigilance, complaint examination, disciplinary processes and improvement of "
            "administrative systems within their actual authority.\n\n"
            "The statutory Central Vigilance Commission performs vigilance, advisory and specified superintendence functions. It is not itself the "
            "prosecuting body and should not be described as conducting every investigation. The Central Bureau of Investigation investigates specified "
            "offences within the applicable legal and jurisdictional framework. Criminal investigation, vigilance advice and departmental discipline may "
            "interact, but they are not interchangeable.\n\n"
            "The Comptroller and Auditor General provides independent external audit of public expenditure and performance for legislative scrutiny. "
            "CAG audit can reveal propriety, compliance and systemic failures, but its ex-post character means internal and concurrent checks remain useful "
            "for early correction. Those checks never replace constitutional audit.\n\n"
            "Effective design routes the problem correctly: administrative weakness to departmental control, credible offence to lawful investigation, "
            "systemic public-finance failure to independent audit and legislature, with due process throughout. Collapsing every institution into an "
            "all-purpose anti-corruption body creates delay, false expectations and accountability diffusion."
        ),
    },
    {
        "marks": 15,
        "question": (
            "Social audit is more than public disclosure. Examine the institutional conditions required for it to secure ethical accountability."
        ),
        "answer": (
            "Disclosure is only the evidentiary beginning of social audit. A credible process must be institutionally independent from the implementing "
            "agency, obtain proactive and intelligible records, and verify those records with workers, beneficiaries and physical works. A public hearing "
            "or Gram Sabha then permits officials and affected persons to answer the evidence openly.\n\n"
            "The cycle becomes accountability only through follow-up. Findings need a time-bound action-taken report, correction of job cards or wages, "
            "recovery or disciplinary and criminal referral where evidence warrants, and a route of appeal. Witnesses and complainants require anti-intimidation "
            "safeguards; otherwise dominant groups can capture the process. Records should remain accessible in local language and assisted formats.\n\n"
            "Social capital can help collective monitoring by building trust across groups, but bonding networks may shield insiders. Therefore community "
            "participation cannot substitute for independent CAG audit, departmental controls or due process. Social audit is strongest as the social leg "
            "of a layered architecture: citizens reveal ground reality, competent forums judge responsibility, and institutions deliver remedy and systemic "
            "correction. Publicity without verification or action is transparency theatre, not ethical accountability."
        ),
    },
    {
        "marks": 20,
        "question": (
            "A State welfare platform uses biometric authentication, mobile monitoring and real-time dashboards, but vulnerable citizens report exclusion "
            "and cannot obtain human review. Analyse the ethical issues and design an accountable remedy."
        ),
        "answer": (
            "The platform offers legitimate advantages: traceable transactions, faster detection of duplicate claims, reduced paper manipulation and real-time "
            "managerial visibility. Yet its accountability chain is broken. Stakeholders include beneficiaries, persons with weak connectivity or biometrics, "
            "field officials, technology vendors, the department and taxpayers.\n\n"
            "The ethical issues are digital divide, authentication error, disability and language barriers, privacy, excessive data collection, opaque automated "
            "decisions and transfer of responsibility to a vendor or algorithm. A dashboard may record failure without identifying who must correct it. Treating "
            "technology as conclusive can convert an administrative convenience into deprivation without hearing.\n\n"
            "The immediate remedy is continuity of service through alternate evidence, assisted and offline access, and a named human officer empowered to override "
            "erroneous exclusion with recorded reasons. Every adverse outcome should provide intelligible grounds, a time standard and appeal. Data collection should "
            "be necessary, secure and access-controlled. Audit logs must identify official and vendor actions without publicly exposing sensitive beneficiary information.\n\n"
            "Institutionally, the department should assign exception-review responsibility, sample outcomes through field verification, disclose anonymised failure and "
            "correction indicators, audit the vendor, and create compensation or restoration where wrongful denial caused harm. Independent audit and social feedback should "
            "test whether digital records match reality.\n\n"
            "The verdict is hybrid accountability: biometric and dashboard tools may support traceability, but only human review, offline remedy, privacy safeguards and "
            "enforceable correction make the system ethically defensible."
            " Periodic review should test recurring exclusion."
        ),
    },
    {
        "marks": 20,
        "question": (
            "As district administrator, you discover MGNREGA payments to fictitious persons, incomplete muster rolls, unpaid genuine workers and assets that cannot be located. "
            "Set out an ethically accountable restoration plan."
        ),
        "answer": (
            "I would separate urgent service restoration from responsibility-fixing while preserving evidence for both. Stakeholders are genuine job-seekers, Gram Panchayats, "
            "field and technical staff, banks, taxpayers, complainants and persons accused of wrongdoing. The immediate risks are destruction of records, continued false payment, "
            "collective stoppage of employment and retaliation against witnesses.\n\n"
            "First, secure paper and digital records and temporarily restrict only suspicious payment pathways under competent authority. An independent team should reconcile registration, "
            "job cards, dated demand, muster rolls, attendance, measurements, technical sanctions, bank credits and physical assets work by work. Genuine unpaid workers should receive prompt "
            "correction and speaking grievance orders; the whole village should not be punished for suspected misconduct.\n\n"
            "Second, conduct an independent social audit with proactive records, worker and worksite verification, a protected public hearing and a published action-taken report. Map each anomaly "
            "to the person who entered, verified, sanctioned and paid it. After notice and hearing, initiate recovery, disciplinary proceedings or criminal referral where evidence and jurisdiction "
            "support them. Protect complainants and preserve appeal.\n\n"
            "Third, restore reliable demand registration, accurate job cards, timely muster closure, wage reconciliation, asset geo-verification and accessible offline grievance channels. Digital "
            "authentication and mobile monitoring should generate alerts, not final denial; human review must correct failure. Monthly exception review, CAG and legislative scrutiny, and periodic "
            "social audit should test recurrence.\n\n"
            "The plan joins remedy, due process and deterrence. Accountability succeeds when genuine workers receive service, culpable actors face evidence-based consequence and the process itself "
            "is redesigned to prevent repetition."
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
        "1. Complete accountability relationship",
        "actor-forum-chain",
        (
            "Identify actor",
            "Assign responsibility",
            "Name forum",
            "State standard",
            "Provide information",
            "Demand explanation",
            "Reach judgment",
            "Correct, remedy or sanction",
        ),
        "Answerability becomes accountability only when review can produce follow-up.",
        "Use to define accountability and distinguish responsibility.",
    ),
    _panel(
        "2. Three control layers",
        "three-layer-control-map",
        (
            "Departmental vigilance",
            "CVO preventive control",
            "CVC advice and superintendence",
            "CBI investigation",
            "CAG independent audit",
            "Legislative scrutiny",
            "Judicial review",
            "Citizen social control",
        ),
        "Each layer addresses a different failure mode; none is self-sufficient.",
        "Use to classify institutions before recommending reform.",
    ),
    _panel(
        "3. Responsibility versus accountability",
        "two-column-distinction",
        (
            "Responsibility assigns duty",
            "Duty exists before scrutiny",
            "Role identifies expected action",
            "Delegation needs clarity",
            "Accountability demands reasons",
            "Forum tests a standard",
            "Judgment fixes failure",
            "Remedy completes the cycle",
        ),
        "Clear responsibility is necessary but does not alone create accountability.",
        "Use for a ten-mark distinction answer.",
    ),
    _panel(
        "4. Political and bureaucratic balance",
        "dual-accountability-rail",
        (
            "Electoral mandate",
            "Ministerial policy choice",
            "Legislative answerability",
            "Frank official advice",
            "Recorded dissent",
            "Lawful final direction",
            "Impartial execution",
            "Review of interference",
        ),
        "Democratic direction and professional neutrality must remain mutually accountable.",
        "Use for the 2019 politicisation question.",
    ),
    _panel(
        "5. Concurrent and external assurance",
        "complementary-audit-cycle",
        (
            "Set transaction controls",
            "Flag exceptions early",
            "Review during delivery",
            "Correct current loss",
            "Preserve audit trail",
            "CAG tests independently",
            "Legislature examines findings",
            "Executive reports follow-up",
        ),
        "Internal real-time assurance complements; it never replaces independent scrutiny.",
        "Use in public-fund and audit answers.",
    ),
    _panel(
        "6. Social audit cycle",
        "verification-to-remedy-loop",
        (
            "Independent audit unit",
            "Proactive local records",
            "Worker verification",
            "Worksite verification",
            "Protected public hearing",
            "Reasoned findings",
            "Action-taken report",
            "Recovery and worker remedy",
        ),
        "Disclosure without independent verification and follow-up is not social audit.",
        "Use for 2021 Q6(a) and MGNREGA cases.",
    ),
    _panel(
        "7. Social capital boundary",
        "bridging-bonding-comparison",
        (
            "Trust lowers participation cost",
            "Reciprocity sustains testimony",
            "Bridging links communities",
            "Collective monitoring improves",
            "Bonding protects insiders",
            "Faction can intimidate",
            "Rights limit social pressure",
            "Formal remedy remains necessary",
        ),
        "Inclusive social capital helps social control; insular loyalty can defeat it.",
        "Use for 2023 Q6(b) with a qualification.",
    ),
    _panel(
        "8. Accountable e-governance",
        "digital-safeguard-ladder",
        (
            "Accessible service channel",
            "Assisted offline option",
            "Minimal secure data",
            "Traceable decision log",
            "Intelligible reasons",
            "Human exception review",
            "Time-bound appeal",
            "Service correction",
        ),
        "Technology supports accountability only when exclusion can be reviewed and remedied.",
        "Use for both 2022 Q4 subparts.",
    ),
    _panel(
        "9. Dashboard-to-accountability test",
        "visibility-to-remedy-chain",
        (
            "Display reliable data",
            "Identify responsible officer",
            "Set review threshold",
            "Investigate anomaly",
            "Hear affected citizen",
            "Issue reasoned finding",
            "Correct record or service",
            "Learn and redesign",
        ),
        "Visibility is evidence; accountability requires judgment, correction and learning.",
        "Use to defeat the dashboard-equals-accountability trap.",
    ),
    _panel(
        "10. MGNREGA restoration sequence",
        "record-reconciliation-flow",
        (
            "Secure scheme records",
            "Match job card and demand",
            "Match muster and attendance",
            "Match wage and bank credit",
            "Match sanction and measurement",
            "Verify physical asset",
            "Map approving responsibility",
            "Restore service and controls",
        ),
        "Reconcile the complete transaction and service chain before fixing responsibility.",
        "Use as the spine for 2025 Q11.",
    ),
    _panel(
        "11. Corrective consequence ladder",
        "evidence-to-action-ladder",
        (
            "Preserve evidence",
            "Separate error from misconduct",
            "Give notice and hearing",
            "Correct beneficiary harm",
            "Recover supported loss",
            "Initiate discipline",
            "Refer credible offence",
            "Audit recurrence controls",
        ),
        "Consequence must be evidence-based, proportionate and joined to service remedy.",
        "Use in honest-error, vigilance and fund-leakage answers.",
    ),
    _panel(
        "12. Mains answer spine",
        "eight-step-answer-spine",
        (
            "Define actor-forum relationship",
            "Distinguish responsibility",
            "Locate control layer",
            "Name failure mechanism",
            "Use Indian illustration",
            "Propose targeted reform",
            "Add safeguard and limit",
            "Conclude with remedy",
        ),
        "Mechanism-specific accountability analysis outperforms generic calls for transparency.",
        "Use as the final checklist for theory and case answers.",
    ),
)

CURRENT_ANCHOR = {
    "title": (
        "Report of the Comptroller and Auditor General of India on Implementation of Mahatma "
        "Gandhi National Rural Employment Guarantee Act in Rajasthan (Report No. 2 of 2026)"
    ),
    "verified_facts": (
        "The official title is 'Report of the Comptroller and Auditor General of India on Implementation of Mahatma Gandhi National Rural Employment Guarantee Act in Rajasthan'.",
        "It is Report No. 2 of 2026.",
        "The report was tabled on 21 August 2026.",
        "The official VB-G RAM G page states that the system uses biometric authentication, mobile monitoring, real-time dashboards, weekly public disclosure and strengthened social audits.",
    ),
    "administrative_link": (
        "⚠️ Accountability use: the CAG report metadata provides a current external-audit anchor, while "
        "the official programme page illustrates tools for traceability and social oversight. Use them to "
        "explain how internal monitoring, independent audit and social audit can reinforce one another."
    ),
    "limit": (
        "Do not invent or infer audit findings, audited counts, financial totals or programme-wide outcomes "
        "from the report title or listing. Biometric authentication, mobile monitoring, dashboards, weekly "
        "disclosure and strengthened social audits do not by themselves prove outcome quality, correct payment, "
        "fairness or effective remedy."
    ),
}

CURRENT_SOURCE_URLS = (
    "https://cag.gov.in/en/audit-report/audit-report-list",
    "https://vbgramg.dord.gov.in/vbgramg/home.aspx",
)

SOURCE_CAVEAT = (
    "The canonical Topic 11 Basic and Advanced owners and books\\ethics4.pdf control doctrine. "
    "Define accountability as actor + forum + standard + explanation + judgment + correction, remedy "
    "or consequence; do not reduce it to retrospective answerability or equate it with responsibility. "
    "Keep departmental vigilance/CVO, CVC, CBI, CAG, legislature, judiciary and social control differentiated: "
    "the CVC is not a prosecuting body, and internal or concurrent assurance complements rather than replaces "
    "CAG and legislative scrutiny. Transparency and dashboard visibility require review and remedy before they "
    "become accountability. Social audit needs independent verification, proactive records, public hearing, "
    "action-taken follow-up, recovery or remedy and anti-intimidation safeguards. Treat political and bureaucratic "
    "accountability as related but distinct. E-governance claims must include digital divide, privacy, opacity, "
    "authentication error, human review and offline remedy. Social capital is a Topic 06 primary concept and a "
    "Topic 11 social-control cross-link; bonding capital can shield wrongdoing. The 2025 Q6(b) public-fund question "
    "is Topic 18 primary and only shared here. Quote exact official PYQs from the stated local GS-IV PDFs; routing "
    "summaries are not quotation sources. The 2025 MGNREGA case is an exam hypothetical, not proof of programme-wide "
    "conditions. The current CAG sources establish only the stated title, report number, tabling date and official "
    "programme-page features; they do not establish findings, totals or outcome quality."
)

REGISTER_SUPPLEMENT = (
    "### ACCOUNTABILITY RELATIONSHIP\n\n"
    "- **Complete chain:** actor -> forum -> standard -> information -> explanation -> judgment -> correction, remedy or consequence.\n"
    "- **Responsibility:** assigned duty; **accountability:** institutional scrutiny and follow-up for its performance.\n"
    "- **Temporal reach:** ex-ante standards, records and reporting; ex-post review, remedy and proportionate consequence.\n\n"
    "### CONTROL ARCHITECTURE\n\n"
    "- **Internal:** departmental vigilance and CVO preventive/disciplinary processes; CVC vigilance advice and specified superintendence; CBI investigation within lawful remit.\n"
    "- **External:** CAG independent audit, legislative scrutiny and judicial review.\n"
    "- **Social:** RTI-enabled citizens, media, civil society and social audit; participation needs safety, capacity and enforceable follow-up.\n"
    "- **Boundary:** CVC is not a prosecuting body; concurrent/internal assurance never replaces CAG or legislature.\n\n"
    "### POLITICAL, DIGITAL AND SOCIAL GOVERNANCE\n\n"
    "- **Political accountability:** ministers answer to legislature and electorate for policy and departmental outcomes.\n"
    "- **Bureaucratic accountability:** officials answer for lawful advice, impartial execution, records, competence and discretion.\n"
    "- **E-governance benefits:** traceability, speed, remote access and reduced record tampering.\n"
    "- **E-governance safeguards:** assisted/offline access, privacy, explainability, audit logs, human review and appeal.\n"
    "- **Social capital:** bridging trust supports monitoring; bonding loyalty may protect insiders or intimidate complainants.\n\n"
    "### SOCIAL AUDIT AND MGNREGA\n\n"
    "- **Social-audit cycle:** independent unit -> proactive records -> worker/worksite verification -> protected public hearing -> findings -> action-taken report -> recovery, discipline and worker remedy.\n"
    "- **MGNREGA reconciliation:** job card + demand + muster + attendance + wage + bank credit + sanction + measurement + physical asset.\n"
    "- **Restoration:** pay genuine workers, correct records and grievances, map responsibility, pursue evidence-based recovery/discipline/referral, then redesign controls.\n"
    "- **Technology limit:** biometric attendance, mobile monitoring and dashboards improve traceability but do not prove fair outcomes or remedy.\n\n"
    "### PYQ AND ANSWER SPINE\n\n"
    "- **2019 Q10:** consequences of politicisation; restore role boundaries, tenure, written directions and review.\n"
    "- **2021 Q6(a):** independent social audit requires verification plus enforceable follow-up.\n"
    "- **2022 Q4(a)/(b):** good governance gains from digital systems qualified by exclusion, privacy, opacity and human-remedy needs.\n"
    "- **2023 Q6(b):** social capital lowers collective-action costs but bonding capital may shield wrongdoing.\n"
    "- **2025 Q6(b):** Topic 18 primary; Topic 11 contributes the accountability-mechanism cross-link.\n"
    "- **2025 Q11:** reconcile records and assets, hold social audit, restore wages, fix responsibility and correct the service system.\n"
    "- **Answer method:** define precisely -> locate control layer -> name failure mechanism -> use Indian evidence -> propose targeted reform -> add safeguard -> conclude with correction and remedy."
)
