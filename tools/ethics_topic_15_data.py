"""Learner-v2 source data: Ethics Topic 15, Transparency, RTI and Information Sharing."""


SESSION_TITLES = (
    "Transparency, disclosure, information sharing, accountability and privacy",
    "RTI foundations: rights-holder, public authority and existing records",
    "Proactive disclosure, record management, open data and usable information",
    "Request route: application, transfer, time limits, fees and assistance",
    "Exemptions, harm, public-interest balancing and the twenty-year rule",
    "Severability and third-party consultation without a disclosure veto",
    "Appeals, burden of proof, remedies, penalties and excluded organisations",
    "Information Commission independence and the RTI Amendment Act, 2019",
    "Official secrecy, Puttaswamy privacy and the DPDP-RTI interface",
    "Digital information sharing, PYQ routes and answer architecture",
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
        "Transparency is a systemic condition, not one isolated release",
        "Transparency is the continuing institutional visibility of rules, criteria, reasons, records and results to appropriate scrutiny; one compelled disclosure may reveal information without changing an organisation's secrecy-oriented default.",
        "A department releases one contract only after litigation but keeps criteria and reasons routinely hidden. Which distinction prevents calling the whole institution transparent?",
        "An agency regularly publishes decision criteria, reasons and outcomes in usable form. Which governance condition is being institutionalised?",
        "conceptual distinctions",
    ),
    _mcq(
        "Disclosure is a particular act of making information available",
        "Disclosure is the release of specified information to a person or public, whether proactively or on request; it is an instrument of transparency but does not by itself create answerability, correction or consequence.",
        "A ministry supplies a requested file but no forum can examine the revealed irregularity. What has occurred without completing accountability?",
        "A public authority uploads a sanctioned project report before any request. Which specific information act has occurred?",
        "conceptual distinctions",
    ),
    _mcq(
        "Information sharing is purpose-bound exchange, not automatic publication",
        "Information sharing is the authorised movement of information between officials, institutions or persons for a defined function; unlike public disclosure, it may remain restricted and must respect necessity, accuracy, security and privacy.",
        "Two departments exchange the minimum verified beneficiary fields under lawful authority without publishing them. Which concept best describes the exchange?",
        "An officer forwards an entire health database to an unrelated unit merely because both are governmental. Which purpose-bound limitation has failed?",
        "conceptual distinctions",
    ),
    _mcq(
        "Accountability requires answerability and a corrective forum",
        "Accountability exists when an identified actor must explain conduct against a standard before a competent forum capable of judgment, correction, remedy or consequence; visibility is enabling evidence, not the completed relationship.",
        "An expenditure dashboard reveals delay but no officer must answer and no authority can correct it. Which governance element remains incomplete?",
        "A review body examines disclosed reasons, orders correction and fixes responsibility. Which concept is fully operational?",
        "conceptual distinctions",
    ),
    _mcq(
        "Section 3 creates a citizen's statutory right",
        "The Right to Information Act confers the right to information on all citizens; applicants ordinarily need not establish a special interest, although access remains subject to the Act's defined scope and exemptions.",
        "A PIO rejects an Indian citizen solely for not proving personal loss from the requested contract. Which statutory starting point corrects the refusal?",
        "A foreign corporation claims Section 3 in its own right as though citizenship were irrelevant. Which limitation must be noticed?",
        "right, records and request route",
    ),
    _mcq(
        "RTI reaches existing material held or controlled, not new explanations",
        "The Act concerns information in material form held by or under the control of a public authority, including accessible private-body material under another law; it does not generally require creation of fresh opinions, analysis or answers.",
        "An applicant asks a PIO to invent a new economic forecast from raw files. Which boundary applies?",
        "A regulator can lawfully access a licensee's inspection report under another statute. Which RTI scope principle may bring that existing report within reach?",
        "right, records and request route",
    ),
    _mcq(
        "Section 6 minimises applicant burden and requires transfer",
        "A request may be made in writing or electronically in English, Hindi or the area's official language; reasons cannot be demanded, assistance is due where needed, and a misdirected request must be transferred promptly.",
        "A PIO insists that an applicant reveal why she wants expenditure vouchers. Which Section 6 safeguard is violated?",
        "The requested record is held by another public authority and the application is transferred with notice. Which statutory route is illustrated?",
        "right, records and request route",
    ),
    _mcq(
        "Section 7 combines ordinary, urgent and deemed-refusal timelines",
        "The ordinary RTI decision period is thirty days, life-or-liberty information is due within forty-eight hours, silence becomes deemed refusal, and information is free when the authority misses the statutory time limit.",
        "A life-saving drug record is withheld for the ordinary thirty-day period despite a demonstrated life-or-liberty nexus. Which timeline applies?",
        "A PIO gives no decision until after the statutory period and then demands the normal access fee. Which consequence should be considered?",
        "right, records and request route",
    ),
    _mcq(
        "Section 4 makes proactive disclosure the first transparency channel",
        "RTI requires organised records and specified suo motu publication, with a constant endeavour to provide information proactively so citizens need minimum resort to individual requests.",
        "A department receives thousands of identical applications for already digitised subsidy criteria. Which statutory strategy should be strengthened first?",
        "A ministry publishes functions, decision norms, budget and subsidy details before any request. Which RTI architecture is operating?",
        "proactive and digital transparency",
    ),
    _mcq(
        "Usability matters alongside publication",
        "Proactive transparency requires current, searchable, accessible and intelligible information, not merely scanned dumps or obsolete links; publication without findability, context, disability access or timely updating can become compliance theatre.",
        "A website uploads thousands of unsearchable image files without dates or headings. Which quality dimension of transparency is missing?",
        "A portal offers machine-readable data, plain-language metadata, accessible formats and update dates. Which ethical improvement is demonstrated?",
        "proactive and digital transparency",
    ),
    _mcq(
        "Open data and RTI overlap but are not identical",
        "Open data emphasises reusable, often machine-readable public datasets, whereas RTI can also secure records, reasons and correspondence not suitable for open release; both remain bounded by lawful confidentiality, security and privacy.",
        "A candidate claims a statistical open-data portal eliminates the need for access to recorded reasons. Which distinction corrects the claim?",
        "A city releases anonymised transport data for reuse while retaining a request route for file-level decisions. Which complementary design is shown?",
        "proactive and digital transparency",
    ),
    _mcq(
        "Digital records can reduce opacity but preserve new risks",
        "Digitisation can improve search, time stamps, audit trails and simultaneous access, yet poor indexing context, deletion, vendor lock-in, manipulated logs, cyber insecurity and inaccessible interfaces can reproduce opacity electronically.",
        "A department scans files but cannot search, authenticate or preserve versions. Why has digitisation not ensured transparency?",
        "A records system preserves provenance, retention schedules, access logs and exportable formats. Which enabling architecture is strengthened?",
        "proactive and digital transparency",
    ),
    _mcq(
        "Section 8 exemptions are specific protections, not a secrecy slogan",
        "RTI exemptions protect defined interests such as security, judicial restrictions, legislative privilege, commercial confidence, fiduciary information, safety, investigation, cabinet material and personal information; withholding needs clause-linked reasoning.",
        "A PIO writes only 'confidential' without identifying a statutory harm or clause. Which exemption discipline is absent?",
        "Disclosure would reveal a protected source and endanger that person's safety. Which kind of Section 8 interest is legitimately engaged?",
        "exemptions and balancing",
    ),
    _mcq(
        "Section 8(2) retains a statutory public-interest override",
        "The statutory public-interest override permits access despite official-secrecy law or listed exemptions where disclosure benefit outweighs harm to protected interests; it requires a reasoned balance, not an automatic presumption.",
        "Evidence of serious public harm is requested, but disclosure also creates a concrete protected risk. Which statutory balance must the authority perform?",
        "An applicant asserts that uttering 'public interest' automatically defeats every exemption. Which qualification corrects the claim?",
        "exemptions and balancing",
    ),
    _mcq(
        "Section 10 requires severability",
        "Where an exempt part can reasonably be separated from the remainder, severability requires access to the non-exempt record with notice of reasons, decision-maker, fee and review rights rather than blanket withholding.",
        "Only two names in a long inspection report require lawful protection, yet the entire report is denied. Which statutory technique was omitted?",
        "A PIO redacts protected identifiers and releases the remaining findings with appeal details. Which principle is applied?",
        "exemptions and balancing",
    ),
    _mcq(
        "Section 11 is consultation, not a third-party veto",
        "Confidential third-party material triggers notice and consideration, but the PIO makes the reasoned decision subject to public-interest and appeal rules; the third party does not possess an absolute veto.",
        "A contractor objects to release and the PIO treats objection as automatically conclusive. Which procedural misconception is present?",
        "The PIO notifies the contractor, considers its representation and independently decides disclosure with appeal notice. Which procedure is correctly followed?",
        "exemptions and balancing",
    ),
    _mcq(
        "Section 19 makes the PIO justify denial",
        "RTI provides a first appeal within the public authority and a second appeal to the Information Commission; in appeal proceedings the burden of proving that denial was justified lies on the denying PIO.",
        "An appellate authority tells the citizen alone to prove that secrecy was unlawful. Which burden rule has been reversed?",
        "A first appellate authority reviews the PIO's reasons before a later Commission appeal. Which two-stage appellate structure is illustrated?",
        "appeals and institutions",
    ),
    _mcq(
        "Section 20 penalty is personal, conditional and capped",
        "The Information Commission may impose two hundred and fifty rupees per day up to twenty-five thousand rupees for specified PIO failures after hearing, unless reasonable and diligent conduct is proved; persistent default may support disciplinary recommendation.",
        "A note says every delayed reply automatically fines the department without hearing. Which penalty qualifications are missing?",
        "A PIO knowingly destroys requested information and cannot show reasonable diligence. Which Section 20 consequence may arise?",
        "appeals and institutions",
    ),
    _mcq(
        "Section 24 exclusion has corruption and human-rights exceptions",
        "Specified intelligence and security organisations are generally excluded, but information concerning allegations of corruption or human-rights violations is not wholly outside the Act; human-rights disclosure follows Commission approval and a special timeline.",
        "An authority claims a Second Schedule organisation can never face any RTI request. Which exceptions defeat the absolute proposition?",
        "A human-rights allegation involving an excluded organisation is routed for the required Commission approval. Which special architecture is engaged?",
        "appeals and institutions",
    ),
    _mcq(
        "The 2019 amendment shifted service-condition detail to rules",
        "The RTI Amendment Act, 2019 replaced Parliament-fixed tenure and salary links for Central and State Information Commissioners with terms prescribed by the Central Government; the 2019 Rules prescribe a three-year term, subject to the age ceiling.",
        "A candidate says the Amendment itself wrote 'three years' into Sections 13 and 16. Which statute-versus-rule distinction corrects the answer?",
        "A critic focuses on executive rule-making over watchdog tenure rather than abolition of RTI rights. Which institutional issue is being identified?",
        "appeals and institutions",
    ),
    _mcq(
        "Section 22 displaces inconsistent secrecy law without repealing it",
        "The RTI Act overrides inconsistent provisions, including official-secrecy law, while the OSA remains in force; genuine protected interests must therefore be tested through RTI's exemption architecture.",
        "A department invokes the OSA label alone and refuses to examine Sections 8 and 10. Which interface rule is ignored?",
        "An answer says Parliament repealed the OSA when enacting RTI. Which legal correction is required?",
        "secrecy privacy and sharing",
    ),
    _mcq(
        "Privacy and transparency protect different democratic goods",
        "Privacy protects dignity, autonomy and contextual control over personal information, while transparency checks public power and expenditure; a sound decision identifies whose privacy, what public function and whether narrower disclosure can serve the interest.",
        "A request seeks a public servant's unrelated medical details merely to attract attention. Which competing value requires serious weight?",
        "A record of public expenditure includes beneficiary identifiers that can be masked without hiding aggregate delivery. Which balancing method is preferable?",
        "secrecy privacy and sharing",
    ),
    _mcq(
        "DPDP Section 44(3) changed the text of RTI Section 8(1)(j)",
        "From 13 November 2025, the DPDP amendment substituted the RTI personal-information exemption with 'information which relates to personal information'; public-interest, severability and third-party provisions remain, requiring careful legal reasoning.",
        "A current answer reproduces only the former public-activity and larger-public-interest wording of clause (j). Which date-stamped correction is necessary?",
        "A candidate says the substitution repealed every other RTI balancing and procedural provision. Which surviving architecture disproves the claim?",
        "secrecy privacy and sharing",
    ),
    _mcq(
        "Purpose limitation governs inter-departmental sharing",
        "Government possession does not create unlimited permission to circulate data; ethical information sharing should have lawful authority, a defined purpose, minimum necessary fields, accuracy, access control, retention limits, security and an auditable remedy route.",
        "A welfare database is copied to an unrelated publicity unit because both belong to government. Which information-sharing safeguard fails first?",
        "Two agencies share verified minimum fields under a recorded legal purpose with access logs and correction. Which governance model is demonstrated?",
        "secrecy privacy and sharing",
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
            "GS-IV Q2(a): What is meant by public interest? What are the principles and "
            "procedures to be followed by the civil servants in public interest? "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf, page 2. Topic 09 is the "
            "primary public-service-values owner; Topic 15 uses it only for disclosure balancing."
        ),
        (
            "Public interest is constitutionally permissible common welfare assessed through evidence, "
            "rights and fair distribution, not the preference of an official, a powerful group or a bare "
            "numerical majority. It includes vulnerable, remote and future citizens who may lack an effective "
            "voice.\n\n"
            "A civil servant should first identify lawful authority and the affected interests. She should "
            "collect relevant facts, disclose material conflicts, consult affected groups where feasible, "
            "compare less restrictive alternatives, apply objective criteria and record reasons. Equality, "
            "dignity, proportionality, economy and long-term effects should guide the choice. Transparency "
            "requires publication of non-sensitive criteria and outcomes; privacy or security restrictions "
            "must be specific and no wider than necessary. An appeal or review route should correct exclusion.\n\n"
            "For example, releasing a village-wise relief list may expose diversion, but unnecessary medical "
            "details should be masked. Public interest therefore does not mean maximum disclosure or maximum "
            "secrecy. It is a reasoned constitutional judgment whose evidence, procedure and balance are capable "
            "of scrutiny."
        ),
    ),
    _pyq(
        2018,
        (
            "GS-IV Q2(b): \"The Right to Information Act is not all about citizens' empowerment "
            "alone, it essentially redefines the concept of accountability.\" Discuss. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf, page 2. This is Topic 15's "
            "direct historical PYQ."
        ),
        (
            "RTI empowers a citizen to seek existing records, but its deeper contribution is to change the "
            "relationship between public authority and citizen. Section 4 requires organised records and "
            "proactive disclosure; Sections 6 and 7 create a time-bound request route; Section 19 supplies "
            "appeal; and Section 20 can attach personal consequence to specified PIO failures. The authority, "
            "rather than the applicant, must justify withholding under a statutory exemption.\n\n"
            "This makes decisions traceable. Tender criteria, beneficiary lists, expenditure and recorded "
            "reasons can be compared with law and actual delivery. MKSS-style verification of muster rolls "
            "illustrates how information becomes evidence for social accountability. Yet disclosure alone is "
            "not complete accountability: a competent forum must hear, judge, correct and remedy the revealed "
            "failure.\n\n"
            "Privacy, security and other protected interests also require narrow, reasoned treatment, including "
            "severability. RTI therefore redefines accountability by moving administration from discretionary "
            "secrecy toward documented answerability, while remaining one component of a wider audit, grievance "
            "and remedial system."
        ),
    ),
    _pyq(
        2018,
        (
            "GS-IV Q12: Edward Snowden, a computer expert and former CIA systems administrator, "
            "released confidential Government documents to the press about the existence of "
            "Government surveillance programmes. According to many legal experts and the US "
            "Government, his actions violated the Espionage Act of 1917, which identified the leak "
            "of State secrets as an act of treason. Yet, despite the fact that he broke the law, "
            "Snowden argued that he had a moral obligation to act. He gave a justification for his "
            "\"whistle blowing\" by stating that he had a duty \"to inform the public as to that "
            "which is done in their name and that which is done against them.\" According to "
            "Snowden, the Government's violation of privacy had to be exposed regardless of "
            "legality since more substantive issues of social action and public morality were "
            "involved here. Many agreed with Snowden. Few argued that he broke the law and "
            "compromised national security, for which he should be held accountable. Do you agree "
            "that Snowden's actions were ethically justified even if legally prohibited? Why or "
            "why not? Make an argument by weighing the competing values in this case. "
            "(Answer in 250 words)"
        ),
        20,
        (
            "Exact full case verified against "
            "books\\more_previous_papers\\GENERAL-STUDIES-PAPER-IV.pdf, page 11. Topic 10 and Topic "
            "22 own conscience and full case method; Topic 15 owns the disclosure-secrecy-privacy boundary. "
            "The stem's legal characterisations are not independently asserted as settled conclusions."
        ),
        (
            "The case opposes privacy, informed democratic consent and exposure of possible abuse to legality, "
            "official confidentiality, institutional loyalty and national security. A disclosure is not ethical "
            "merely because the discloser invokes conscience; nor does classification automatically defeat a "
            "serious public-interest claim.\n\n"
            "The decision should test the gravity and evidence of the alleged wrong, the availability and safety "
            "of internal or independent oversight channels, necessity of external disclosure, reliability of the "
            "material, and proportionality of what is revealed. Information unrelated to the wrongdoing should "
            "be minimised or redacted. Consequentialism weighs democratic correction against operational and "
            "personal harm; duty ethics recognises duties of truth and confidentiality; virtue ethics requires "
            "courage joined with prudence.\n\n"
            "For an Indian administrator, the normal route is to preserve evidence, record objection and use "
            "competent vigilance, legislative, judicial or protected-reporting channels. External disclosure "
            "becomes morally stronger where grave illegality is evidenced, ordinary remedies are ineffective "
            "and release is narrowly tailored. The defensible verdict is therefore conditional: exposing unlawful "
            "surveillance may serve public morality, but indiscriminate publication that creates avoidable security "
            "or privacy harm remains unjustified. Independent review and severability offer the best reconciliation."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q4(b): There is a view that the Official Secrets Act is an obstacle to the "
            "implementation of Right to Information Act. Do you agree with the view? Discuss. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 3. This is Topic 15's "
            "direct PYQ; Citizens' Charter in Q4(a) is excluded."
        ),
        (
            "The view is substantially persuasive as an administrative-culture critique, but it needs a legal "
            "qualification. The Official Secrets Act, 1923 remains in force and can reinforce classification, "
            "fear of disclosure and a colonial need-to-know mindset. The Second ARC therefore recommended its "
            "repeal and relocation of genuine secrecy offences into a national-security law.\n\n"
            "Legally, however, OSA is not an automatic answer to an RTI request. Section 22 gives the RTI Act "
            "overriding effect to the extent of inconsistency. Withholding must be justified through a relevant "
            "RTI exemption, while Section 8(2) permits disclosure where public interest outweighs harm. Section "
            "10 requires release of a reasonably severable non-exempt part.\n\n"
            "National security, protected sources and operational details can require secrecy; transparency does "
            "not mean indiscriminate release. Reform should narrow classification, record reasons, review secrecy "
            "periodically, train PIOs and strengthen independent appeal. Thus the chief obstacle is not coexistence "
            "alone but using the OSA label to bypass RTI's clause-specific, harm-based and reviewable architecture."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q12: In recent times, there has been an increasing concern in India to develop "
            "effective civil service ethics, codes of conduct, transparency measures, ethics and "
            "integrity systems and anti-corruption agencies. In view of this, there is a need being "
            "felt to focus on three specific areas, which are directly relevant to the problems of "
            "internalizing integrity and ethics in the civil services. These are as follows: "
            "1. Anticipating specific threats to ethical standards and integrity in the civil services, "
            "2. Strengthening the ethical competence of civil servants and "
            "3. Developing administrative processes and practices which promote ethical values and "
            "integrity in civil services. Suggest institutional measures to address the above three "
            "issues. (Answer in 250 words)"
        ),
        20,
        (
            "Faithful English text and numbering verified against "
            "books\\more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 7. Topic 16/20 own the "
            "full ethics-system demand; Topic 15 contributes transparency and information architecture."
        ),
        (
            "The three demands require a prevention-capability-process architecture. First, departments should "
            "map risks around procurement, transfers, licensing, data access and conflicts of interest. Published "
            "criteria, rotation in sensitive posts, conflict registers, electronic audit trails, protected reporting "
            "and risk-based vigilance can expose threats before loss occurs.\n\n"
            "Second, ethical competence needs induction and recurring dilemma-based training, confidential ethics "
            "advice, mentoring and leadership by example. Officers should practise giving speaking reasons, balancing "
            "RTI with privacy, managing conflicts and using lawful dissent channels. Training should be evaluated "
            "through decisions and institutional outcomes, not attendance.\n\n"
            "Third, processes should reduce opaque discretion: Section 4-style proactive disclosure, accessible "
            "service standards, e-procurement, reasoned orders, record-retention rules, independent audit, time-bound "
            "appeal and grievance remedy. Information systems must show decision ownership without exposing protected "
            "personal or security data. Social audit can compare official records with delivery where the function "
            "permits citizen verification.\n\n"
            "No agency alone can manufacture integrity. Excessive surveillance may chill honest judgment, while "
            "publication without correction becomes theatre. Controls should therefore be proportionate, protect "
            "documented good faith and link disclosure to a competent forum, remedy and learning. Ethical culture "
            "becomes durable when character is supported by reviewable institutional design."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q6(a): An independent and empowered social audit mechanism is an absolute must "
            "in every sphere of public service, including judiciary, to ensure performance, "
            "accountability and ethical conduct. Elaborate. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against "
            "books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3. Topic 11 "
            "is primary; Topic 15 supplies the records-and-disclosure precondition."
        ),
        (
            "Social audit enables citizens to compare official records with lived delivery. Independence from the "
            "implementing body, proactive access to intelligible records, field verification and a public hearing "
            "can expose ghost entries, exclusion and poor performance hidden by aggregate reports. MGNREGA workers, "
            "for example, may compare job cards, muster rolls, wages and completed works.\n\n"
            "Information is necessary but insufficient. Empowerment requires a time-bound action-taken report, "
            "correction or compensation, recovery or disciplinary referral where evidence supports it, reasoned "
            "rejection of unsupported claims and protection against intimidation. Privacy-sensitive identifiers "
            "should be minimised or masked where public verification does not require them.\n\n"
            "The phrase 'every sphere' must be functionally adapted. Citizen scrutiny of court administration cannot "
            "become crowd control of adjudication; decisional independence, confidentiality and lawful appeal remain. "
            "Social audit complements CAG, departmental audit and courts. Its ethical value lies in converting usable "
            "disclosure into participatory verification and enforceable follow-up."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q5(a): The 'Code of Conduct' and 'Code of Ethics' are the sources of guidance in "
            "public administration. There is code of conduct already in operation, whereas code of "
            "ethics is not yet put in place. Suggest a suitable model for code of ethics to maintain "
            "integrity, probity and transparency in governance. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated subpart verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "page 3. Topic 16 is primary; Topic 15 contributes openness, information-use and review."
        ),
        (
            "A Code of Ethics should begin with constitutional fidelity and public purpose, then state "
            "selflessness, integrity, merit objectivity, impartiality, openness, honest interest declaration, "
            "accountability and leadership by example. Its transparency chapter should require publication of "
            "decision criteria, speaking reasons, accurate records, lawful RTI assistance and responsible use of "
            "confidential and personal information.\n\n"
            "Implementation matters more than a declaration. Officers need dilemma training, confidential ethics "
            "advice, interest registers, recusal protocols, secure reporting, independent complaint handling, fair "
            "inquiry and an annual account of observance. Proactive disclosure should be current and intelligible, "
            "while privacy, security and fiduciary limits are applied through stated law rather than generic secrecy.\n\n"
            "A Code of Conduct remains complementary because it specifies prohibited behaviour, procedures and "
            "consequences. Neither code can replace the RTI Act, service rules or due process. The suitable model "
            "therefore joins values with records, institutional advice, review and remedy, making claimed ethical "
            "standards visible without treating maximum publicity as maximum probity."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q1(b): \"Constitutional morality is not a natural sentiment but a product of civil "
            "education and adherance of the rule of law.\" Examine the significance of constitutional "
            "morality for public servant highlighting the role in promoting good governance and ensuring "
            "accountability in public administration. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording, including the printed 'adherance', verified against "
            "books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, page 2. Topic 10/14 are primary; Topic 15 "
            "uses the public-reasons and accountability cross-link."
        ),
        (
            "Constitutional morality is learned fidelity to constitutional values, procedures and limits on power "
            "rather than obedience to private preference or a temporary majority. For a public servant it turns "
            "equality, dignity, liberty and rule of law into daily decision standards.\n\n"
            "It promotes good governance by requiring lawful competence, objective criteria, fair hearing, public "
            "reasons and review. These disciplines restrain arbitrary discretion and protect minorities even where "
            "local prejudice is popular. Accountability improves because a decision leaves a record that citizens, "
            "auditors and appellate bodies can test. A district officer allocating relief should publish need-based "
            "criteria, record exclusions, protect unnecessary personal data and provide a grievance route.\n\n"
            "Constitutional morality is not mechanical publicity or rule worship. Sensitive information may be "
            "withheld under law, and humane discretion may be needed, but both require proportionate reasons and "
            "review. It thus makes transparency purposeful: information enables citizens to examine whether public "
            "power remained within constitutional values and to obtain correction when it did not."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q6(b): India is an emerging economic power of the world as it has recently secured "
            "the status of fourth largest economy of the world as per IMF projection. However, it has "
            "been observed that in some sectors, allocated funds remain either underutilised or "
            "misutilised. What specific measures would you recommend for ensuring accountability in "
            "this regard to stop leakages and gaining the status of third largest economy of the world "
            "in near future? (Answer in 150 words)"
        ),
        10,
        (
            "Wording verified from books\\mains\\UPSC Mains 2025 GS Paper 4.pdf, pages 3-4; the "
            "scan's text layer drops part of one printed line. Topic 18 is primary and Topic 11 owns "
            "general accountability; Topic 15 supplies disclosure and information-system measures."
        ),
        (
            "Public-fund accountability begins by naming responsibility for sanction, release, utilisation, output "
            "and outcome. Each budget head should have realistic milestones, interoperable expenditure records and "
            "a reviewing officer. E-procurement, time-stamped transaction trails and exception alerts can identify "
            "idle balances, duplicate payments and delay.\n\n"
            "Visibility must reach citizens and competent forums. Departments should proactively publish scheme-wise "
            "allocations, releases, physical progress, utilisation and audit responses in accessible, machine-readable "
            "form, subject to legitimate redaction. CAG and legislative scrutiny, field verification, social audit and "
            "protected complaints should test the data. Deviations require speaking explanations, time-bound correction, "
            "recovery or disciplinary referral where evidence supports it, and restoration of affected service.\n\n"
            "Dashboards alone may contain poor or strategically reported data. Independent verification, data-quality "
            "responsibility, grievance appeal and outcome evaluation are essential. Information sharing across treasury, "
            "procurement and implementing units should be purpose-bound and secure. Thus transparency supports growth "
            "only when it matures into answerability, judgment and remedy."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        "Distinguish transparency, disclosure, information sharing and accountability in public administration.",
        (
            "Transparency is the continuing visibility of rules, criteria, reasons, records and outcomes to "
            "appropriate scrutiny. Disclosure is a particular act of releasing specified information, proactively "
            "or on request. Information sharing is the authorised movement of information for a defined function; "
            "it may occur between departments without becoming public. Accountability is the relationship in which "
            "an identified actor explains conduct against a standard before a competent forum capable of correction, "
            "remedy or consequence.\n\n"
            "The distinctions are practical. Publishing a tender is disclosure and may strengthen transparency. "
            "Sharing verified bidder debarment data with another authorised buyer is purpose-bound information "
            "sharing. If an audit body examines the award, hears the officer and orders correction, accountability "
            "is completed. Conversely, a data dump without reasons may disclose much while remaining opaque.\n\n"
            "Privacy and security qualify each process: public access may require redaction, while restricted sharing "
            "needs lawful purpose, minimum fields and access controls. Therefore transparency supplies visibility, "
            "disclosure and sharing move information, and accountability converts relevant information into answerable "
            "and correctable public power."
        ),
    ),
    _original(
        10,
        "Why is Section 4 proactive disclosure ethically superior to excessive dependence on individual RTI applications?",
        (
            "Section 4 places the burden of routine openness on the public authority rather than on a citizen who "
            "must know what to ask, draft an application and pursue delay. Organised records and regular publication "
            "of functions, norms, budgets, subsidies, concessions and decision processes reduce information asymmetry "
            "before suspicion or litigation arises.\n\n"
            "Proactive disclosure promotes equality because persons with less legal literacy, money or time gain the "
            "same baseline information. It also reduces repetitive applications and PIO workload, supports media and "
            "social audit, and disciplines officials who know that criteria and outcomes will be visible. Publishing "
            "ward-wise works and expenditure, for example, lets residents compare records with the site.\n\n"
            "Its ethical superiority is conditional. Obsolete links, scanned dumps and unexplained datasets create "
            "compliance theatre; personal data and genuine security interests require lawful protection. Authorities "
            "should therefore publish current, searchable, accessible and machine-readable material with metadata, "
            "review dates and grievance routes. Individual RTI remains necessary for file-specific records. Section 4 "
            "is the first channel, not a substitute for request, appeal and remedy."
        ),
    ),
    _original(
        15,
        "Examine how Sections 8(2), 10 and 11 prevent both absolute secrecy and reckless disclosure under the RTI Act.",
        (
            "The RTI Act does not choose between disclosure of everything and secrecy by label. Section 8(1) protects "
            "specified interests, but Section 8(2) permits access where public interest in disclosure outweighs harm "
            "to those interests, notwithstanding the Official Secrets Act or the listed exemptions. The authority "
            "must therefore identify the protected harm and weigh it against a concrete public benefit.\n\n"
            "Section 10 narrows withholding. If protected names, coordinates or trade details can reasonably be "
            "separated, the remainder must be supplied with reasons and review information. It prevents one exempt "
            "sentence from concealing an entire report. Section 11 adds procedural fairness where confidential "
            "third-party material may be released: notice and representation inform the PIO's decision, but objection "
            "is not an absolute veto.\n\n"
            "Consider a completed public-works contract containing a proprietary technique and evidence of inflated "
            "payment. The PIO should hear the contractor, protect genuinely competitive material, sever it where "
            "possible and assess public interest in expenditure disclosure. The applicant and third party retain "
            "appeal rights.\n\n"
            "These provisions demand reasoned calibration. Section 8(2) is not a magic phrase, severability must be "
            "practicable, and consultation must not outsource the statutory decision. Together they make secrecy "
            "exceptional, disclosure proportionate and the process reviewable."
        ),
    ),
    _original(
        15,
        "Assess the institutional-independence implications of the RTI (Amendment) Act, 2019 without overstating its effect.",
        (
            "Before 2019, the RTI Act itself fixed the tenure of the Chief Information Commissioner and Information "
            "Commissioners and linked their salaries to specified constitutional or senior offices. The Amendment "
            "changed Sections 13 and 16 so that tenure, salary, allowances and service conditions for Central and "
            "State Commissions are prescribed by the Central Government. The 2019 Rules, not the Amendment's text, "
            "prescribe a three-year term subject to the age ceiling.\n\n"
            "The ethical concern is structural. Information Commissions decide appeals involving public authorities, "
            "including governments. Moving safeguards from Parliament-fixed text to executive rules can reduce the "
            "appearance or durability of insulation and may create a chilling-risk argument. Central prescription "
            "for State commissioners also raises a federal-design concern.\n\n"
            "However, the Amendment did not abolish the citizen's right, exemptions, appeals or penalty power, and "
            "a rule-making change does not prove actual interference in any decision. Administrative uniformity and "
            "flexibility are legitimate counterclaims. Independence also depends on transparent appointments, vacancies, "
            "resources, reasoned orders and review, not tenure alone.\n\n"
            "A balanced reform would place core tenure and remuneration safeguards in statute, ensure timely merit-based "
            "appointments and publish performance information while preserving adjudicatory autonomy. The defensible "
            "conclusion is a serious institutional-design concern, not an allegation of established misconduct."
        ),
    ),
    _original(
        20,
        "Privacy is not an exemption from accountability, and transparency is not a licence for personal-data exposure. Discuss after Puttaswamy and the DPDP-driven amendment to RTI Section 8(1)(j).",
        (
            "Privacy and transparency protect different constitutional-democratic goods. Privacy preserves dignity, "
            "autonomy and contextual control over personal information; transparency exposes the exercise of public "
            "power and public money. Puttaswamy recognised privacy as a fundamental right, requiring State intrusion "
            "to rest on legality, legitimate aim, proportionality and safeguards. Yet public office cannot convert "
            "every service-related record into a private enclave.\n\n"
            "DPDP Act Section 44(3), commenced on 13 November 2025, substituted RTI Section 8(1)(j) with the broader "
            "text 'information which relates to personal information'. A current answer must not reproduce the former "
            "clause as operative law. Equally, it should not claim that all balancing vanished: Section 8(2)'s public-"
            "interest override, Section 10 severability, Section 11 third-party procedure and appeal remain in the Act. "
            "How these provisions interact with the substituted clause may require authoritative adjudication; Section "
            "8(2) should not be treated as automatically restoring every deleted phrase.\n\n"
            "Administrators should ask: whose privacy is affected, what public function or expenditure is under scrutiny, "
            "what concrete harm follows, and can masking or aggregation serve accountability? Aggregate beneficiary "
            "delivery, tender evaluation and conflict information may often be disclosed without unrelated medical, "
            "family or identity details. Notice, reasoned redaction and appeal protect both sides.\n\n"
            "As of 29 August 2026, the DPDP Act is not wholly operational: Section 44(3) is in force; Section 6(9) and "
            "Section 27(1)(d) commence on 13 November 2026; and many core processing, rights and penalty provisions "
            "commence on 13 May 2027. Ethical minimisation, security and purpose limitation remain prudent before full "
            "commencement. The correct approach is accountable privacy: disclose what tests public power, protect what "
            "needlessly exposes the person, and explain the legal balance."
        ),
    ),
    _original(
        20,
        "A State plans to link welfare, health and land databases to detect fraud and publish a district dashboard. As the responsible secretary, design an ethical information-sharing and transparency framework.",
        (
            "The proposal can detect duplicate claims and improve planning, but it combines distinct purposes and "
            "creates exclusion, profiling, breach and function-creep risks. Stakeholders include genuine beneficiaries, "
            "wrongly flagged families, officials, local bodies, data processors, auditors and the public. I would not "
            "authorise unrestricted linkage or publication.\n\n"
            "First, each exchange must identify legal authority, a specific fraud or planning purpose, necessary fields, "
            "data quality and a responsible officer. A documented sharing agreement should prohibit unrelated reuse, "
            "set role-based access, encryption, retention and deletion, preserve logs, require breach response and permit "
            "independent audit. High-risk matches should be treated as leads, never automatic grounds for benefit denial. "
            "Affected persons need notice where lawful, assisted correction, a speaking decision and prompt human appeal.\n\n"
            "Second, the public dashboard should use aggregation and suppression thresholds so citizens can compare "
            "allocation, delivery, pendency and grievance outcomes without exposing names, diagnoses or precise land "
            "identifiers. Methodology, update date, limitations and responsible office should be published. File-level "
            "records remain available through RTI subject to exemptions, severability and third-party procedure.\n\n"
            "Third, an oversight group including legal, security, programme and field expertise should test bias, false "
            "matches and access patterns. Periodic necessity review must terminate fields or linkages that do not improve "
            "the stated purpose. Procurement contracts should ensure portability and government audit access.\n\n"
            "Puttaswamy supplies the legality and proportionality discipline; data ethics adds minimisation and purpose "
            "limitation. The framework therefore separates restricted sharing from public disclosure, and connects both "
            "to answerability, correction and remedy. Fraud control is legitimate only when the information system does "
            "not make an innocent citizen transparent to an unaccountable State."
        ),
    ),
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
        "1. Information-governance distinction map",
        "concept-separation",
        (
            "Transparency: systemic visibility",
            "Disclosure: particular release",
            "Sharing: purpose-bound exchange",
            "Open data: reusable datasets",
            "Privacy: dignity and control",
            "Accountability: answerability",
            "Forum supplies correction",
            "Law sets legitimate limits",
        ),
        "Moving information is not identical to making power accountable.",
        "Use to define the topic and prevent synonym traps.",
    ),
    _panel(
        "2. RTI scope and rights-holder route",
        "scope-chain",
        (
            "Section 3: citizen's right",
            "Identify public authority",
            "Locate held or controlled record",
            "Include law-accessible private data",
            "Do not demand new opinion",
            "Applicant need not give reasons",
            "Assist persons needing help",
            "Apply exemptions only afterward",
        ),
        "RTI opens existing recorded information; it does not compel fresh intellectual creation.",
        "Use for Sections 2, 3 and 6 answers.",
    ),
    _panel(
        "3. Section 4 proactive-disclosure engine",
        "proactive-cycle",
        (
            "Catalogue and index records",
            "Computerise appropriate records",
            "Publish organisation and duties",
            "Publish norms and decision process",
            "Publish budget and programmes",
            "Publish subsidies and concessions",
            "Update, search and make accessible",
            "Minimise need for applications",
        ),
        "The strongest RTI system answers routine questions before they become disputes.",
        "Use for reform, capacity and anti-corruption answers.",
    ),
    _panel(
        "4. Sections 6 and 7 request clock",
        "timeline-route",
        (
            "File written or electronic request",
            "Use English, Hindi or local official language",
            "Give contact detail, not reasons",
            "Transfer under Section 6(3)",
            "Ordinary decision: thirty days",
            "Life or liberty: forty-eight hours",
            "Silence becomes deemed refusal",
            "Delay makes information free",
        ),
        "Access is meaningful only when procedure is simple, assisted and time-bound.",
        "Use for application and timeline close-option questions.",
    ),
    _panel(
        "5. Section 8 exemption and balance",
        "harm-balance",
        (
            "Name exact exemption clause",
            "Identify protected interest",
            "Specify likely disclosure harm",
            "Reject generic confidentiality",
            "Test Section 8(2) public interest",
            "Consider twenty-year rule",
            "Record clause-linked reasons",
            "Preserve appeal and review",
        ),
        "A protected interest requires a reasoned harm analysis, not a secrecy label.",
        "Use for exemptions, OSA and public-interest questions.",
    ),
    _panel(
        "6. Severability and third-party procedure",
        "redaction-consultation-route",
        (
            "Identify protected segment",
            "Test reasonable separation",
            "Release non-exempt remainder",
            "Notify reasons and review rights",
            "Notify affected third party",
            "Receive timely representation",
            "PIO decides independently",
            "Notify both sides of appeal",
        ),
        "Redaction narrows secrecy; consultation improves fairness without creating a veto.",
        "Use for Sections 10 and 11.",
    ),
    _panel(
        "7. Appeal, burden, remedy and penalty",
        "accountability-ladder",
        (
            "PIO gives decision or defaults",
            "First appeal within authority",
            "Second appeal to Commission",
            "PIO bears denial burden",
            "Commission may order access",
            "Commission may require system reform",
            "Section 20 penalty is conditional",
            "Persistent default may trigger discipline",
        ),
        "RTI accountability joins access, justification, correction and personal consequence.",
        "Use for 2018 Q2(b) and enforcement reform.",
    ),
    _panel(
        "8. Section 24 special boundary",
        "exclusion-exception-tree",
        (
            "Check notified security organisation",
            "General exclusion applies",
            "Test corruption allegation",
            "Test human-rights allegation",
            "Corruption route remains open",
            "Human-rights route needs approval",
            "Apply special forty-five-day period",
            "Protect genuine operational harm",
        ),
        "Security-organisation exclusion is broad but not absolute.",
        "Use for statutory traps and balanced national-security answers.",
    ),
    _panel(
        "9. RTI Amendment 2019 institutional map",
        "before-after-comparison",
        (
            "Pre-2019 tenure fixed in Act",
            "Pre-2019 salary links fixed in Act",
            "2019 shifts detail to Central rules",
            "Change covers Central Commissions",
            "Change also covers State Commissions",
            "Rules prescribe three-year term",
            "Independence concern is structural",
            "Actual interference is not proved",
        ),
        "State the design risk precisely without claiming that RTI rights were abolished.",
        "Use for institutional-independence evaluation.",
    ),
    _panel(
        "10. OSA and RTI interface",
        "override-boundary",
        (
            "OSA 1923 remains in force",
            "ARC recommended repeal and relocation",
            "Recommendation is not enacted law",
            "RTI Section 22 overrides inconsistency",
            "Section 8 protects genuine interests",
            "Section 8(2) weighs public interest",
            "Section 10 narrows withholding",
            "Reasoned review replaces blanket label",
        ),
        "Official secrecy survives, but it cannot bypass the RTI Act's own decision architecture.",
        "Use for the 2019 direct PYQ.",
    ),
    _panel(
        "11. Privacy after Puttaswamy and DPDP",
        "rights-balance",
        (
            "Privacy protects dignity and autonomy",
            "State action needs legality",
            "Aim and proportionality matter",
            "Safeguards and remedy matter",
            "Section 44(3) commenced 13 Nov 2025",
            "RTI 8(1)(j) text was substituted",
            "Sections 8(2), 10 and 11 remain",
            "Sec 6(9): 13 Nov 2026; core: 13 May 2027",
        ),
        "Use current text and acknowledge unresolved interaction instead of reviving deleted wording.",
        "Use for privacy-transparency and current-law answers.",
    ),
    _panel(
        "12. Ethical digital information-sharing design",
        "governance-stack",
        (
            "Establish lawful authority",
            "Define specific purpose",
            "Share minimum necessary fields",
            "Verify accuracy and provenance",
            "Control access and retention",
            "Publish only safe aggregates",
            "Enable correction and appeal",
            "Audit necessity, use and outcomes",
        ),
        "An accountable State should be transparent about power without making citizens needlessly transparent.",
        "Use for databases, open data and twenty-mark design questions.",
    ),
)


CURRENT_ANCHOR = {
    "title": "RTI propagation in 2025-26 and the commenced DPDP amendment to RTI",
    "verified_facts": (
        "DoPT's 17 April 2025 annual-programme guidelines invited State Information Commissions and Administrative Training Institutes to submit 2025-26 proposals for propagation of the RTI Act to improve transparency and accountability.",
        "The official programme document links RTI propagation with training, awareness and effective implementation rather than treating enactment alone as sufficient.",
        "MeitY notification G.S.R. 843(E), published on 13 November 2025, commenced DPDP Act Section 44(3) on the date of publication.",
        "Section 44(3) substitutes RTI Act Section 8(1)(j) with the words 'information which relates to personal information'.",
        "The notification places Section 6(9) and Section 27(1)(d) in the one-year tranche commencing 13 November 2026.",
        "Its eighteen-month tranche, commencing 13 May 2027, includes Sections 3 to 5, the rest of Section 6, Sections 7 to 17 and linked core architecture.",
    ),
    "administrative_link": (
        "The two sources show the contemporary double task: build practical RTI capacity and proactive "
        "openness while updating privacy-transparency decisions to the amended statutory text and the "
        "DPDP framework's phased commencement."
    ),
    "limit": (
        "The 2025-26 programme document is an implementation and grant guideline, not evidence that every "
        "authority complies with Section 4. G.S.R. 843(E) does not make the whole DPDP Act operational on "
        "13 November 2025; as at 29 August 2026, the eighteen-month tranche is still prospective."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://rti.dopt.gov.in/Writereaddata/Guidelines_2025_26.pdf",
    "https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf",
)


SOURCE_CAVEAT = (
    "The corrected canonical Topic 15 Basic and Advanced owners control the teaching sequence. "
    "Transparency is systemic visibility; disclosure is a particular release; information sharing is "
    "purpose-bound exchange; open data concerns reusable datasets; accountability requires an actor, "
    "standard, competent forum, judgment and correction or consequence; privacy protects dignity, autonomy "
    "and contextual control. Do not use these terms as synonyms. RTI covers existing information held or "
    "controlled by a public authority, including private-body information accessible under another law; it "
    "does not generally compel creation of opinions or analysis. Section 4 proactive disclosure should be "
    "current, intelligible and accessible. Section 6 applicants need not give reasons; Section 7 ordinarily "
    "uses thirty days and forty-eight hours for life or liberty. Section 8 exemptions require clause-linked "
    "reasoning; Section 8(2) retains public-interest balancing; Section 10 requires reasonable severability; "
    "Section 11 consultation is not a third-party veto. Section 19 places the denial burden on the PIO. "
    "Section 20 penalty is personal, hearing-based, conditional on specified failure and capped at twenty-five "
    "thousand rupees; it is not an automatic departmental fine. Section 24 exclusions retain corruption and "
    "human-rights exceptions, with Commission approval and a forty-five-day rule for the latter. The Official "
    "Secrets Act, 1923 remains in force; the Second ARC recommendation to repeal and relocate genuine secrecy "
    "offences was not enacted. RTI Section 22 overrides inconsistent law but does not abolish legitimate RTI "
    "exemptions. The RTI Amendment Act, 2019 shifted tenure and remuneration detail for Central and State "
    "Information Commissioners from the Act to Central rules; the three-year term comes from the 2019 Rules, "
    "not the Amendment's text. Describe the resulting independence issue as a structural concern, not proof "
    "of actual interference or abolition of the right. Puttaswamy is the constitutional privacy foundation. "
    "DPDP Act Section 44(3) commenced on 13 November 2025 and substituted RTI Section 8(1)(j) with 'information "
    "which relates to personal information'. Sections 8(2), 10 and 11 remain, but do not claim without authority "
    "that Section 8(2) automatically recreates every deleted qualifier. G.S.R. 843(E) phased commencement: as "
    "at 29 August 2026 the Act is not wholly operational; Section 6(9) and Section 27(1)(d) commence on "
    "13 November 2026, while the major eighteen-month tranche begins 13 May 2027. "
    "Official local GS-IV PDFs control PYQ text. Cross-routed questions retain their primary owners, and full "
    "case-study method remains Topic 22-owned."
)


REGISTER_SUPPLEMENT = (
    "### TEN-SESSION RAPID REGISTER\n\n"
    "#### 1. CONCEPTUAL FIREWALLS\n\n"
    "- **Transparency:** continuing visibility of rules, criteria, reasons, records and outcomes to appropriate scrutiny.\n"
    "- **Disclosure:** one act of release; proactive or request-based; public or person-specific.\n"
    "- **Information sharing:** authorised exchange for a defined function; it may remain restricted.\n"
    "- **Open data:** reusable, usually machine-readable public datasets; it does not replace access to reasons or files.\n"
    "- **Accountability:** actor + standard + forum + evidence/reasons + judgment + correction/remedy/consequence.\n"
    "- **Privacy:** dignity, autonomy and contextual control; not identical to secrecy.\n"
    "- **Master line:** transparency enables accountability but does not complete it.\n\n"
    "#### 2. RTI SCOPE AND RIGHTS-HOLDER\n\n"
    "- **Section 3:** right belongs to citizens; a special personal interest is ordinarily unnecessary.\n"
    "- **Information:** existing material in any form held or controlled; includes private-body material accessible by a public authority under another law.\n"
    "- **Right to information:** inspection, notes/extracts, certified copies, certified samples and electronic access as statutorily described.\n"
    "- **Boundary:** PIO supplies records, not a newly invented opinion, justification or research product.\n"
    "- **Public authority:** use the statutory control, constitution, law, notification and substantial-financing tests; do not assume every private entity is directly covered.\n\n"
    "#### 3. SECTION 4: DISCLOSE BEFORE DEMAND\n\n"
    "- Catalogue, index and appropriately computerise records; connect systems where access is facilitated.\n"
    "- Publish organisation, powers, duties, decision process, norms, rules, document categories, consultation arrangements, boards, directory, remuneration, budget, subsidy programmes, concessions and PIO particulars under the statutory clauses.\n"
    "- Update disclosures; use local language, accessible formats, search, metadata and low-cost dissemination.\n"
    "- **Section 4(2):** constant endeavour to provide as much information suo motu at regular intervals so the public has minimum resort to RTI applications.\n"
    "- **Trap:** upload is not usability. Scanned, obsolete or unsearchable material can be compliance theatre.\n\n"
    "#### 4. REQUEST AND TIME ROUTE\n\n"
    "- **Section 6:** written/electronic request in English, Hindi or official language of the area; no reasons; reasonable assistance where required.\n"
    "- **Section 6(3):** transfer to the appropriate public authority as soon as practicable and within five days, with applicant informed.\n"
    "- **Section 7:** ordinary decision within thirty days; life or liberty within forty-eight hours; silence is deemed refusal.\n"
    "- BPL applicants are protected by the statutory fee rule; delayed information is supplied free under Section 7(6).\n"
    "- Assist persons with sensory disability to access the record.\n\n"
    "#### 5. EXEMPTION AND PUBLIC-INTEREST BALANCE\n\n"
    "- **Section 8(1):** identify the exact clause and protected interest; 'secret', 'confidential' or 'sensitive' alone is not analysis.\n"
    "- Common heads: sovereignty/security; court-forbidden information; legislative privilege; commercial confidence/IP; fiduciary material; foreign-government confidence; safety/source; investigation; cabinet material; personal information.\n"
    "- **Section 8(2):** disclosure may proceed where public interest outweighs harm to protected interests, notwithstanding OSA or Section 8(1).\n"
    "- **Section 8(3):** after twenty years, disclosure rule applies subject to the continuing statutory exceptions; do not state an absolute twenty-year declassification rule.\n"
    "- Use a four-step balance: clause -> concrete harm -> public benefit -> narrower alternative/reasons.\n\n"
    "#### 6. SEVERABILITY AND THIRD PARTY\n\n"
    "- **Section 10:** separate protected and non-protected portions where reasonable; release remainder and notify reasons, decision-maker, fee and review rights.\n"
    "- **Section 11:** notice to affected third party, opportunity to represent, independent PIO decision and appeal notice.\n"
    "- **Timing recall:** notice within five days; representation opportunity within ten days; decision ordinarily within forty days for the third-party route.\n"
    "- **Trap:** consultation is not consent and not veto. The statutory decision remains with the PIO/appellate system.\n\n"
    "#### 7. APPEAL, REMEDY, PENALTY AND SECTION 24\n\n"
    "- **Section 19:** first appeal within the public authority; second appeal to CIC/SIC; ordinarily thirty and ninety days respectively, subject to sufficient-cause admission.\n"
    "- First appeal ordinarily decided within thirty days, extendable to forty-five days with written reasons.\n"
    "- **Section 19(5):** PIO bears burden of proving denial justified.\n"
    "- **Section 20:** Rs 250 per day, maximum Rs 25,000, after opportunity of hearing, for specified failures; reasonable diligence is relevant; persistent default may support disciplinary recommendation.\n"
    "- **Section 24:** listed security/intelligence organisations generally excluded, but corruption and human-rights allegations remain exceptions; human-rights information needs Commission approval and follows forty-five days.\n\n"
    "#### 8. INFORMATION COMMISSION INDEPENDENCE\n\n"
    "- Pre-2019 core tenure and salary links were fixed in the Act; the 2019 Amendment shifted tenure, salary, allowances and service conditions to Central Government rules for Central and State commissioners.\n"
    "- The **three-year** term is prescribed by the RTI Rules, 2019, subject to age sixty-five; do not attribute that number to the Amendment Act itself.\n"
    "- Ethics issue: adjudicator insulation, security of tenure, federal design and appearance of independence.\n"
    "- Qualification: the amendment did not repeal Section 3, appeal or penalty, and does not prove interference in a decided case.\n"
    "- Reform bundle: statutory safeguards + timely transparent appointments + adequate staffing + reasoned decisions + publication of performance without outcome pressure.\n\n"
    "#### 9. OSA, PRIVACY AND CURRENT DPDP POSITION\n\n"
    "- OSA 1923 remains in force. Second ARC recommended repeal and relocation of genuine secrecy provisions; recommendation is not law.\n"
    "- **Section 22:** RTI prevails to the extent of inconsistency; test secrecy through Sections 8, 10 and appeal.\n"
    "- **Puttaswamy (2017):** privacy is fundamental; State restriction requires legality, legitimate aim, proportionality and safeguards.\n"
    "- **13 Nov 2025:** DPDP Section 44(3) commenced and RTI Section 8(1)(j) became 'information which relates to personal information'.\n"
    "- Sections 8(2), 10 and 11 survive. Their interaction with the substituted clause must be argued carefully, not assumed away.\n"
    "- **29 Aug 2026 status:** DPDP is not wholly operational; Section 6(9) and Section 27(1)(d) commence 13 Nov 2026; Sections 3-5, the rest of Section 6, Sections 7-17 and linked core architecture commence 13 May 2027.\n\n"
    "#### 10. DIGITAL SHARING, PYQS AND ANSWER METHOD\n\n"
    "- Digital gains: search, time stamp, provenance, simultaneous access, audit trail and machine readability.\n"
    "- Digital risks: bad metadata, silent deletion, manipulated logs, cyber breach, vendor lock-in, inaccessible portals and false confidence in dashboards.\n"
    "- Sharing checklist: authority -> purpose -> minimum fields -> accuracy -> access control -> retention -> security -> audit -> correction/remedy.\n"
    "- Dashboard rule: publish safe aggregates, methodology, limitations, update date and responsible office; never expose personal detail merely to look transparent.\n"
    "- **Direct PYQs:** 2018 RTI-accountability; 2019 OSA obstacle. **Cross-routes:** public interest, Snowden, institutional ethics, social audit, ethics code and fund accountability.\n\n"
    "### UPSC TRAP BANK\n\n"
    "- RTI is not absolute access, and privacy is not absolute secrecy.\n"
    "- Section 11 gives consultation, not a third-party veto.\n"
    "- Section 20 is not an automatic departmental fine for every delay.\n"
    "- Section 24 exclusion is not absolute because corruption and human-rights routes survive.\n"
    "- OSA has not been repealed; Section 22 supplies an inconsistency override.\n"
    "- The 2019 Amendment did not itself prescribe three years and did not abolish the citizen's right.\n"
    "- The former wording of Section 8(1)(j) is not current after 13 November 2025.\n"
    "- DPDP is enacted and partly commenced, not wholly operational as at 29 August 2026.\n"
    "- Open data does not replace recorded reasons, file access or appeal.\n"
    "- Maximum disclosure is not maximum ethics; use lawful, severable and proportionate openness.\n\n"
    "### MARK-SCALED ANSWER ARCHITECTURE\n\n"
    "1. **Define and distinguish** the nearest concepts in two lines.\n"
    "2. **State the legal spine** with only demand-relevant sections.\n"
    "3. **Explain the mechanism:** information asymmetry -> visibility -> verification -> answerability -> correction.\n"
    "4. **Apply one Indian example:** muster roll, tender, beneficiary dashboard, land record or public expenditure.\n"
    "5. **Balance the strongest limit:** privacy, security, commercial confidence, capacity or digital exclusion.\n"
    "6. **Give an operational reform:** proactive disclosure, severability, speaking order, appeal, audit, data minimisation or Commission independence.\n"
    "7. **Conclude:** transparent public power, protected personal dignity and a competent remedy must coexist."
)
