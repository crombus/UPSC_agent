"""Learner-v2 source data: Ethics Topic 21, protecting honest officials."""


SESSION_TITLES = (
    "Visual foundation: protection, vigilance and the bona fides test",
    "Essential definitions and close legal distinctions",
    "Mechanism: screening, verification, evaluation and escalation",
    "Indian applications: risk-taking, transfers, dissent and workplace process",
    "Must-know facts for Prelims",
    "UPSC traps: protection without impunity",
    "PYQ application across honest-official and retaliation cases",
    "Mains analysis: calibrated safeguards and accountable investigators",
    "Probable questions and examiner-ready case routes",
    "Study links, current legal uncertainty and final synthesis",
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
        "A bad outcome does not by itself prove misconduct",
        (
            "The bona fides test asks whether a person of common prudence, acting within prescribed "
            "rules and for the organisation's genuine interest, could have taken the decision in the "
            "circumstances then known."
        ),
        (
            "A loan approved after documented due diligence later defaults because of an unforeseen "
            "market shock. Which test prevents outcome bias from becoming a vigilance charge?"
        ),
        (
            "An officer bypasses mandatory checks to favour a connected borrower and later cites "
            "commercial risk. Which feature defeats a claim of bona fides?"
        ),
        "bona fides calibration",
    ),
    _mcq(
        "Risk-taking is compatible with vigilance",
        (
            "The Second Administrative Reforms Commission states that vigilance should enhance, not "
            "reduce, managerial efficiency; legitimate commercial or administrative risk must remain "
            "possible while corrupt motive and reckless rule evasion receive scrutiny."
        ),
        (
            "A department punishes every innovative decision that produces a loss. Which vigilance "
            "purpose identified by the Commission has been reversed?"
        ),
        (
            "A review distinguishes documented risk from concealed conflict and deliberate deviation. "
            "Which calibrated approach is being applied?"
        ),
        "bona fides calibration",
    ),
    _mcq(
        "Process evidence is central to bona fides",
        (
            "Contemporaneous reasons, consultation, disclosed conflicts, applicable rules, available "
            "information and equal treatment are stronger evidence of good faith than a later assertion "
            "that the official merely intended a public benefit."
        ),
        (
            "An officer claims good intent but kept no reasons and concealed a relative's interest. "
            "Which evidentiary weakness matters most?"
        ),
        (
            "A file records alternatives, expert advice, risk limits and dissent before the decision. "
            "How does this support honest decision-making?"
        ),
        "bona fides calibration",
    ),
    _mcq(
        "Protection follows good faith, not hierarchy",
        (
            "Honest-official protection is justified by lawful good-faith decision-making rather than "
            "seniority, status or institutional prestige; corruption control loses legitimacy when rank "
            "alone determines whether credible allegations may be examined."
        ),
        (
            "A rule shields senior officers from scrutiny but exposes junior officers for identical "
            "conduct. Which equality defect is present?"
        ),
        (
            "A rank-neutral process screens allegations by conduct, evidence and official-duty nexus. "
            "Which protective principle does it better reflect?"
        ),
        "bona fides calibration",
    ),
    _mcq(
        "Allegations require threshold screening",
        (
            "Before formal inquiry, the Second Administrative Reforms Commission recommends testing each "
            "corruption allegation for specificity, credibility and verifiability so that vague hostility "
            "does not automatically become coercive process."
        ),
        (
            "An anonymous complaint identifies no act, date, benefit or record, yet immediately triggers "
            "public accusation. Which threshold safeguard was omitted?"
        ),
        (
            "A complaint names the transaction, decision trail, alleged benefit and checkable documents. "
            "Why is it suitable for preliminary verification?"
        ),
        "screening and evidence",
    ),
    _mcq(
        "Secret verification has a limited protective purpose",
        (
            "Confidential preliminary verification can protect an innocent official's reputation and "
            "preserve evidence, but it must not become an indefinite, unreviewed device for burying a "
            "specific and credible complaint."
        ),
        (
            "A false allegation is discreetly checked and closed without publicity. Which legitimate "
            "function of secrecy is illustrated?"
        ),
        (
            "A credible complaint remains secretly pending for years without reasons or review. Which "
            "abuse of the same safeguard appears?"
        ),
        "screening and evidence",
    ),
    _mcq(
        "Competence and impartiality determine evaluation quality",
        (
            "Complex commercial, technical and financial decisions should be evaluated by honest and "
            "impartial personnel who understand the domain and consult experts, because ignorance can "
            "misclassify ordinary risk as corrupt conduct."
        ),
        (
            "A technically complex procurement decision is judged only by an investigator unfamiliar "
            "with the sector. Which Commission safeguard is missing?"
        ),
        (
            "An independent team obtains engineering and financial advice before fixing responsibility. "
            "Which evaluation principle is satisfied?"
        ),
        "screening and evidence",
    ),
    _mcq(
        "Strong evidence should precede prosecution",
        (
            "Protecting honest officials does not mean suppressing investigation; it means narrowing "
            "coercive action toward persons against whom evidence is strong while separating error, "
            "negligence, poor judgment and corrupt intent."
        ),
        (
            "Investigators implicate everyone who signed a file without identifying knowledge, benefit "
            "or agreement. Which overbroad method is being criticised?"
        ),
        (
            "The inquiry identifies the actual beneficiary, concealed communication and deliberate rule "
            "evasion before prosecution. Which calibrated standard is shown?"
        ),
        "screening and evidence",
    ),
    _mcq(
        "Section 17A operates before specified investigative steps",
        (
            "PC Act 17A concerns prior approval before enquiry, inquiry or investigation into an alleged "
            "Prevention of Corruption Act offence relatable to an official-duty recommendation or decision, "
            "subject to its statutory on-the-spot exception."
        ),
        (
            "A candidate describes Section 17A only as permission for a court to begin trial. Which stage "
            "has been confused?"
        ),
        (
            "An allegation concerns a recorded policy recommendation rather than an on-the-spot bribe. "
            "Which approval question ordinarily arises first?"
        ),
        "legal safeguards",
    ),
    _mcq(
        "Section 19 is a prosecution-cognizance safeguard",
        (
            "PC Act 19 requires previous sanction before a court takes cognizance of specified Prevention "
            "of Corruption Act offences against a covered public servant; it is distinct from PC Act 17A's "
            "earlier investigative-stage approval."
        ),
        (
            "An answer treats sanction for cognizance as identical to approval before inquiry. Which two "
            "statutory stages must be separated?"
        ),
        (
            "Investigation is completed and the court is asked to take cognizance. Which safeguard becomes "
            "directly relevant at this point?"
        ),
        "legal safeguards",
    ),
    _mcq(
        "The former single directive is not current law",
        (
            "The rank-based Delhi Special Police Establishment Act provision requiring approval to investigate "
            "Joint Secretary-level and equivalent officers was struck down in 2014 for violating Article 14; "
            "it must not be presented as operative."
        ),
        (
            "A note says senior rank alone still activates the old single directive. Which constitutional "
            "development corrects it?"
        ),
        (
            "A current analysis instead asks whether alleged conduct is linked to an official-duty decision. "
            "Which change in legal framing is recognised?"
        ),
        "legal safeguards",
    ),
    _mcq(
        "The 2026 Section 17A case produced no common final holding",
        (
            "On 13 January 2026, two Supreme Court judges expressed divergent opinions on PC Act 17A and "
            "directed that the matter be placed before the Chief Justice for an appropriate Bench, leaving "
            "the constitutional issue unresolved by that order."
        ),
        (
            "A writer claims the January 2026 order unanimously invalidated Section 17A. Which feature of "
            "the official order disproves the claim?"
        ),
        (
            "An answer labels the judgment a split decision referred for fresh consideration. Why is that "
            "the accurate current anchor?"
        ),
        "legal safeguards",
    ),
    _mcq(
        "Investigators require accountability too",
        (
            "The Second Administrative Reforms Commission proposed a specialised unit linked to the proposed "
            "Lok Pal or State Lokayukta to examine corruption by investigating agencies and allegations that "
            "investigators themselves harassed officials."
        ),
        (
            "An agency insists that scrutiny of investigators always destroys independence. Which Commission "
            "recommendation answers that position?"
        ),
        (
            "A separate competent body examines fabricated evidence and retaliatory investigation. Which "
            "watch-the-watchers principle is applied?"
        ),
        "investigator and transfer accountability",
    ),
    _mcq(
        "Over-suspicion can weaken anti-corruption outcomes",
        (
            "The Commission warned that assuming every wrong decision implies corruption and implicating the "
            "entire decision chain can demoralise honest officials, lower precision, waste capacity and allow "
            "actual wrongdoers to escape."
        ),
        (
            "Every signatory is accused of conspiracy solely because a project failed. Which two-sided vigilance "
            "failure mode appears?"
        ),
        (
            "Investigators isolate who knew, benefited, concealed and deliberately deviated. How does this improve "
            "both fairness and enforcement?"
        ),
        "investigator and transfer accountability",
    ),
    _mcq(
        "The transfer industry is soft retaliation",
        (
            "Arbitrary transfer can punish an honest officer without formal disciplinary action, destabilise "
            "professional independence and convert postings into transactions; transparent policy and minimum "
            "tenure are therefore integrity safeguards."
        ),
        (
            "An officer is moved immediately after refusing political favour, without stated administrative "
            "grounds. Which harassment mechanism is illustrated?"
        ),
        (
            "A published policy requires reasons, tenure norms and review of premature transfer. Which corrective "
            "architecture is present?"
        ),
        "investigator and transfer accountability",
    ),
    _mcq(
        "Tenure protection needs justified exceptions",
        (
            "Minimum tenure should reduce punitive transfers, yet urgent reassignment may remain legitimate where "
            "continued posting creates conflict, evidence risk or serious operational harm; any exception should "
            "be narrow, recorded and reviewable."
        ),
        (
            "A tenure rule prevents moving an officer who is tampering with a live inquiry. Which qualification "
            "has been ignored?"
        ),
        (
            "A premature transfer order records evidence risk and receives independent review. Which balance is "
            "being maintained?"
        ),
        "investigator and transfer accountability",
    ),
    _mcq(
        "Written dissent converts conscience into an administrative record",
        (
            "When pressured to act improperly, an official should seek written instructions, record facts and "
            "reasons, state a reasoned dissent and preserve the decision trail rather than rely on oral refusal "
            "or silent compliance."
        ),
        (
            "A superior orally orders favour to a bidder and the officer obeys without noting objection. Which "
            "protective step was missed?"
        ),
        (
            "The officer records the direction, relevant rule, public risk and lawful alternative. What ethical "
            "function does this dissent serve?"
        ),
        "dissent and whistleblowing",
    ),
    _mcq(
        "Escalation should ordinarily begin through authorised channels",
        (
            "The whistleblowing ladder begins with evidence preservation and internal or authorised vigilance "
            "reporting, then uses higher independent channels if capture persists; public disclosure is reserved "
            "for grave residual harm and lawful necessity."
        ),
        (
            "An officer uploads unverified allegations before using any protected channel. Which sequencing problem "
            "does this create?"
        ),
        (
            "Records are secured, the CVO is approached and an independent authority is used after internal capture. "
            "Which ladder is followed?"
        ),
        "dissent and whistleblowing",
    ),
    _mcq(
        "Resignation is usually not the first ethical response",
        (
            "Immediate resignation may abandon records, institutional duty and affected citizens; the official should "
            "first document, dissent, escalate, seek protection and reduce harm unless continued service itself requires "
            "direct illegality."
        ),
        (
            "An officer resigns before preserving evidence of procurement manipulation. Which public-duty concern "
            "arises?"
        ),
        (
            "The officer refuses illegality, records reasons and activates oversight while remaining available for "
            "lawful implementation. Which approach is stronger?"
        ),
        "dissent and whistleblowing",
    ),
    _mcq(
        "Confidentiality must accompany anti-retaliation",
        (
            "A protected reporting system needs restricted identity access, secure records, retaliation monitoring, "
            "interim safety measures and review of adverse postings; secrecy alone is inadequate if reprisals remain "
            "easy and invisible."
        ),
        (
            "A complainant's name is hidden, but a punitive transfer follows without review. Which safeguard remains "
            "incomplete?"
        ),
        (
            "Access logs, safety assessment and independent review of adverse action accompany confidential reporting. "
            "Which design is illustrated?"
        ),
        "dissent and whistleblowing",
    ),
    _mcq(
        "POSH inquiry is distinct from corruption vigilance",
        (
            "The Internal Committee conducts workplace due process for sexual-harassment complaints, while vigilance "
            "machinery examines corruption-related misconduct; neither route should be manipulated to suppress the "
            "other or prejudge criminal responsibility."
        ),
        (
            "A builder threatens a fabricated workplace complaint to stop a corruption inquiry. Which dual-process "
            "response is required?"
        ),
        (
            "The corruption evidence is preserved while an independent Internal Committee fairly examines the separate "
            "complaint. Which boundary is respected?"
        ),
        "POSH and balanced protection",
    ),
    _mcq(
        "POSH protection does not erase respondent due process",
        (
            "A credible sexual-harassment system must enable complaint, confidentiality, assistance and protection from "
            "victimisation while also providing an impartial inquiry, defined allegations, opportunity to respond and "
            "reasoned recommendations."
        ),
        (
            "Management pays a complainant to withdraw and declare the respondent innocent. Which institutional duties "
            "are defeated?"
        ),
        (
            "The committee protects participants, tests evidence and gives both sides procedural fairness. Which balanced "
            "standard is applied?"
        ),
        "POSH and balanced protection",
    ),
    _mcq(
        "Safeguards cannot become shields for corruption",
        (
            "Approval, sanction, confidentiality and tenure rules are legitimate only when applied promptly, independently "
            "and with recorded reasons; indefinite delay or partisan control converts protection of honest action into "
            "impunity for misconduct."
        ),
        (
            "A competent authority ignores a complete evidence file until limitation risks arise. Which safeguard misuse "
            "is present?"
        ),
        (
            "A time-bound reasoned decision distinguishes bona fide judgment from concealed benefit. Which protective "
            "balance is achieved?"
        ),
        "POSH and balanced protection",
    ),
    _mcq(
        "Protection without impunity needs symmetric design",
        (
            "A credible vigilance system filters malice, protects lawful risk-taking and checks investigator abuse, yet "
            "also preserves evidence, reviews refusals, prosecutes strong cases and prevents hierarchy or procedure from "
            "blocking accountability."
        ),
        (
            "A reform proposal only increases immunity for officials. Which half of the symmetric design is missing?"
        ),
        (
            "Another proposal abolishes every safeguard and equates accusation with guilt. Which opposite failure does "
            "it create?"
        ),
        "POSH and balanced protection",
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
        2019,
        (
            "GS-IV Q8: Honesty and uprightness are the hallmarks of a civil servant. Civil "
            "servants possessing these qualities are considered as the backbone of any strong "
            "organization. In line of duty, they take various decisions, at times some become "
            "bonafide mistakes. As long as such decisions are not taken intentionally and do "
            "not benefit personally, the officer cannot be said to be guilty. Though such "
            "decisions may, at times, lead to unforeseen adverse consequences in the long-term. "
            "In the recent past, a few instances have surfaced wherein civil servants have been "
            "implicated for bonafide mistakes. They have often been prosecuted and even imprisoned. "
            "These instances have greatly rattled the moral fibre of the civil servants. How does "
            "this trend affect the functioning of the civil services? What measures can be taken "
            "to ensure that honest civil servants are not implicated for bonafide mistakes on "
            "their part? Justify your answer. (250 words)"
        ),
        20,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 5. The official paper uses the spelling "
            "'bonafide'; the model answer retains the question while applying ARC's bona fides test."
        ),
        (
            "Fear of implication changes administrative behaviour before any case is filed. Officers avoid innovation, "
            "defer decisions through unnecessary committees, refuse difficult postings and privilege personal safety over "
            "public value. Honest and dishonest officials then become indistinguishable in a culture of defensive delay. "
            "Institutional morale falls, talented officers exit sensitive assignments and citizens bear slower delivery.\n\n"
            "Protection should begin with ARC's bona fides test: would a prudent person, working within rules and using the "
            "information then available, have taken the decision in the organisation's genuine interest? Review must examine "
            "contemporaneous reasons, due diligence, disclosed interests, expert advice and personal benefit, not merely the "
            "later outcome. Specificity, credibility and verifiability screening should precede discreet preliminary checking. "
            "Technically competent and impartial investigators should identify actual knowledge, benefit and deliberate rule "
            "evasion rather than implicating every signatory.\n\n"
            "Section 17A and Section 19 represent different statutory safeguards, but approvals and sanctions must be timely, "
            "reasoned and reviewable so they do not shelter corruption. Investigators should themselves face independent "
            "accountability for fabricated or retaliatory cases. Transparent transfer policies, minimum tenure, written "
            "instructions and protected reporting channels address softer forms of harassment.\n\n"
            "The aim is neither official immunity nor accusation-based punishment. A calibrated system protects good-faith "
            "risk-taking while pursuing strong evidence against actual misconduct."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q9 case study: A successful marketing executive in an apparel company is "
            "accused by a woman employee of workplace sexual harassment. Management initially "
            "ignores her grievance and later offers money for withdrawal of both the complaint "
            "and FIR, along with a written declaration exonerating the executive. Identify the "
            "ethical issues and the options available to the woman employee. (250 words)"
        ),
        20,
        (
            "Neutral routing verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 5. The official stem is longer; this entry "
            "preserves its parties, pressure, complaint, FIR and demands without claiming verbatim reproduction."
        ),
        (
            "The issues are sexual harassment, managerial indifference, abuse of economic power, attempted suppression "
            "of evidence, retaliation risk, conflict between sales performance and dignity, and denial of institutional "
            "due process. The payment offer also seeks a false declaration, converting settlement pressure into an "
            "integrity problem.\n\n"
            "The employee may insist that the employer activate the Internal Committee, preserve messages and witness "
            "accounts, seek confidentiality and interim protection, continue the police process where she chooses, approach "
            "the Local Committee or competent authority if the workplace mechanism is absent or compromised, and obtain "
            "legal or counselling support. She should not be compelled to choose between workplace inquiry and criminal "
            "process because they are distinct routes.\n\n"
            "The employer must constitute and assist the committee, prevent victimisation, avoid predetermining guilt, and "
            "act on reasoned recommendations. The respondent must receive defined allegations and a fair opportunity to "
            "answer; protecting the complainant does not authorise a sham inquiry. Equally, commercial value cannot excuse "
            "harassment or institutional capture.\n\n"
            "Her strongest course is to reject coercive withdrawal, document the offer, use the Internal Committee with "
            "safeguards, and continue lawful external remedies as advised. Dignity, truth and fair procedure must prevail "
            "over both corporate reputation management and allegation-based condemnation."
        ),
    ),
    _pyq(
        2020,
        (
            "GS-IV Q10 case study: An honest Municipal Commissioner investigates a fatal mall "
            "collapse and finds poor material, unauthorised construction, inspection failures and "
            "a prima facie official-builder nexus. Colleagues press for delay, the influential "
            "builder offers a bribe, and a threatened POSH complaint is used to demand silence. "
            "Discuss the ethical issues, options and selected course of action. (250 words)"
        ),
        20,
        (
            "Neutral routing verified against books\\more_previous_papers\\Gen_St_P4.pdf, "
            "pages 8-9. The official multi-paragraph stem and final demand control; this entry "
            "condenses the facts for Topic 21's protection, dissent and POSH-process route."
        ),
        (
            "The case combines loss of life, corruption, regulatory capture, child labour concerns, friendship conflict, "
            "ministerial influence, bribery, pressure from colleagues and weaponisation of a possible POSH complaint. The "
            "Commissioner owes duties to victims, lawful construction, fair investigation, colleagues, the complainant if "
            "one emerges, and his own procedural protection.\n\n"
            "He may slow or suppress the inquiry, recuse entirely, disclose and seek an independent team, or continue with "
            "institutional safeguards. Suppression is illegal and betrays victims. Total recusal may protect appearance but "
            "can abandon responsibility unless a competent substitute is secured. The best course is to preserve the site, "
            "records and electronic trails; provide relief to victims; disclose friendship with the former Commissioner; "
            "constitute a multidisciplinary inquiry; record all oral pressure and the bribe approach; and escalate through "
            "vigilance and criminal channels.\n\n"
            "Any workplace complaint must go independently to a properly constituted Internal Committee. It should neither "
            "be dismissed as retaliation without inquiry nor used to halt corruption evidence. Interim reporting lines can "
            "avoid contact while both processes continue.\n\n"
            "The Commissioner should issue reasoned directions, resist transfer or career threats through written records, "
            "and seek protection for witnesses. This preserves accountability for the deaths while demonstrating that honest "
            "official protection means due process, not immunity from a separate lawful complaint."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q7 case study: Sunil, a young civil servant confronting an illegal sand-mining "
            "mafia supported by local functionaries and insiders, faces threats to himself and "
            "surveillance of his family. Identify his options, critically evaluate them, and select "
            "the most appropriate course of action. (250 words)"
        ),
        20,
        (
            "Neutral routing verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, pages 4-5. The official paper supplies "
            "the complete case; this routing retains the nexus, threats, family risk and three-part demand."
        ),
        (
            "Sunil can withdraw, seek transfer, continue alone, negotiate informally, or build a protected institutional "
            "response. Withdrawal rewards coercion and harms communities; transfer may protect family but leaves the network "
            "intact. Acting alone shows courage but creates avoidable safety and evidence risks. Informal compromise is "
            "unacceptable where organised crime and official collusion are involved.\n\n"
            "He should document threats and operational facts, secure evidence outside the compromised office, inform senior "
            "police and administrative authorities in writing, request assessed protection for family and witnesses, rotate "
            "sensitive personnel, and form a multi-agency team covering mining, transport, revenue, police and financial "
            "trails. Insider access should be restricted through need-to-know controls and access logs. Raids must remain "
            "lawful, intelligence-led and supervised.\n\n"
            "If local channels are captured, Sunil should use higher vigilance or authorised anti-corruption routes and seek "
            "judicial protection where necessary. Media disclosure should not be the first step because it may expose sources "
            "and operations. A transfer request can be reconsidered after evidence and continuity arrangements are secured, "
            "not as immediate surrender.\n\n"
            "The course combines courage with prudence. Integrity does not require reckless martyrdom; it requires sustained "
            "public action, institutional escalation, personal safety and an auditable trail that makes retaliation visible."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q6(a): Whistle-blower, who reports corruption and illegal activities, wrongdoing "
            "and misconduct to the concerned authorities, runs the risk of being exposed to grave "
            "danger, physical harm and victimization by the vested interests, accused persons and "
            "his team. What policy measures would you suggest to strengthen protection mechanism "
            "to safeguard the whistle-blower? (Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 4."
        ),
        (
            "Protection must cover the full disclosure cycle. First, provide secure authorised channels with identity "
            "segregation, encrypted records, acknowledgement and jurisdiction routing. Only designated officers should access "
            "identity, and every access should be logged. Second, require prompt threat assessment, police protection where "
            "needed, safe transfer on the complainant's request, witness protection and emergency contact arrangements.\n\n"
            "Third, create a rebuttable review of adverse transfers, appraisals, suspensions, contracts or harassment occurring "
            "after disclosure. Interim relief and restoration should be available without waiting for final prosecution. Fourth, "
            "time-bound independent investigation should separate the disclosure's merits from retaliation complaints. Malicious "
            "falsehood may receive proportionate action only after intent is proved; mere inability to prove corruption should "
            "not attract punishment.\n\n"
            "Finally, publish anonymised outcomes, impose personal consequences for identity leakage, train officers, and permit "
            "escalation beyond a captured department. The Whistle Blowers Protection Act's non-commencement makes dependable "
            "administrative channels especially important, but reform should ultimately provide an operational statutory regime. "
            "Confidentiality without safety and remedy is incomplete protection."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q8 case study: Ramesh, a State Civil Services officer in a border State, submits "
            "a confidential report on illegal migrant infiltration and forged documents. A superior "
            "orders withdrawal and threatens loss of his capital posting and promotion. Examine his "
            "options, preferred course, ethical dilemmas and relevant policy measures. (250 words)"
        ),
        20,
        (
            "Neutral routing verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, pages 8-9. The official paper "
            "contains the complete factual narrative and five-part demand."
        ),
        (
            "Ramesh faces conflict between lawful duty and obedience, national security and humane treatment, family needs "
            "and public interest, confidentiality and escalation, and career pressure versus integrity. Withdrawal protects "
            "his immediate posting but falsifies the record. Public leakage may trigger action but compromises intelligence, "
            "privacy and operations. Silent refusal without escalation may preserve conscience yet leave the threat untreated.\n\n"
            "He should ask for the withdrawal direction in writing, preserve the original report and supporting evidence, "
            "record a reasoned dissent, and seek review by the competent senior authority through secure channels. The report "
            "should distinguish verified infiltration, suspected official complicity and untested inference. A multidisciplinary "
            "investigation should protect intelligence sources while testing document and financial trails. If departmental "
            "capture persists, he should use authorised vigilance, security or judicial channels rather than partisan or public "
            "disclosure.\n\n"
            "He should disclose the personal posting and promotion pressure but not allow it to determine substance. Any "
            "transfer should be challenged through recorded reasons and applicable review, while continuity of investigation "
            "is secured.\n\n"
            "Policy measures include secure border systems, document-authentication audits, staff rotation, anti-collusion "
            "controls, reasoned transfer policy and protected reporting. His answer should be firm but evidence-based: written "
            "dissent protects integrity only when followed by lawful escalation and operational follow-through."
        ),
    ),
    _pyq(
        2023,
        (
            "GS-IV Q10 case study: Vinod, an honest IAS officer and Managing Director of a State "
            "Road Transport Corporation after six transfers in three years, receives documents and "
            "a video alleging bribery by the politically powerful Chairman. The opposition source "
            "offers future career support, while exposure may cause another transfer. Evaluate Vinod's "
            "options and the ethical issues arising from politicisation of bureaucracy. (250 words)"
        ),
        20,
        (
            "Neutral routing verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, pages 10-11. The official stem "
            "controls; this entry preserves the transfers, evidence, political incentives and two-part demand."
        ),
        (
            "Vinod can ignore the material, immediately publicise it, align with the opposition, confront the Chairman alone, "
            "or verify and route it institutionally. Ignoring credible evidence breaches fiduciary duty. Public disclosure may "
            "taint evidence and convert administration into partisan contest. Accepting promised advancement creates a fresh "
            "conflict even if the allegation is true. Solo confrontation risks destruction of records and retaliation.\n\n"
            "Vinod should acknowledge the source without accepting political terms, make a conflict record, secure copies and "
            "metadata, and order lawful discreet verification by a competent team. Procurement files, payment trails, tender "
            "criteria and communications should be preserved. If the threshold is met, he should refer the matter through the "
            "CVO or competent anti-corruption channel, recuse from any step creating personal conflict, and maintain confidentiality. "
            "He should document threatened transfer and seek review under applicable tenure policy while ensuring an institutional "
            "handover if moved.\n\n"
            "Politicisation produces transfer markets, partisan loyalty, selective exposure, policy discontinuity and public distrust. "
            "Its cure is not bureaucratic unaccountability but published posting criteria, fixed tenure with reasoned exceptions, "
            "board-level controls and independent investigation.\n\n"
            "Vinod must be non-partisan in method and fearless in substance. Evidence, not the source's electoral interest or the "
            "Chairman's proximity to power, should determine action."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q8 case study: Raman, a newly posted State Director General of Police, confronts "
            "online recruitment of unemployed youth by a global terrorist group. State intelligence "
            "indicates targeting of a particular community and extremist social-media activity. "
            "Examine his options, measures to strengthen the existing setup and an action plan for "
            "better intelligence gathering. (250 words)"
        ),
        20,
        (
            "Neutral routing verified against books\\mains\\05 UPSC 2024 Paper-IV_Final 1.pdf, "
            "pages 5-6. The official paper provides the complete case. Topic 21 uses it for calibrated "
            "screening, investigator accountability and protection against indiscriminate suspicion."
        ),
        (
            "Raman must act against a credible security threat without equating unemployment, community identity, dissent or "
            "heavy social-media use with terrorism. Options range from mass coercive action to passive monitoring; both extremes "
            "fail. Blanket profiling can alienate citizens, generate false positives and obscure actual recruiters, while delay "
            "permits mobilisation.\n\n"
            "He should establish a legally supervised, intelligence-led task force that verifies source reliability, maps recruiter "
            "networks and distinguishes advocacy, radical belief, preparation and criminal action. Targeted digital forensics should "
            "follow authorisation, necessity, proportionality, access controls and audit logs. Community leaders, educational bodies, "
            "employment agencies and mental-health or counselling services can support prevention and credible counter-messaging. "
            "At-risk youth should receive exit pathways rather than automatic criminal branding.\n\n"
            "The intelligence system needs trained analysts, multilingual capability, inter-agency fusion, source protection, false-"
            "positive review, periodic legal audit and independent complaint handling for abuse. Officers should record reasons for "
            "intrusive measures and supervisors should review discriminatory patterns.\n\n"
            "The ethics of honest-official protection applies to investigators too: clear rules and recorded approvals protect lawful "
            "decisions, while accountability for fabrication, profiling or leakage prevents impunity. Raman's objective is precise "
            "prevention that protects both public safety and constitutional trust."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Explain how the bona fides test protects honest administrative risk-taking without "
            "creating immunity for negligent or corrupt decisions."
        ),
        (
            "The bona fides test asks whether a person of common prudence, acting within prescribed rules and on the "
            "information then available, could have taken the decision in the organisation's genuine interest. It corrects "
            "outcome bias: a failed loan, procurement or policy experiment is not automatically misconduct.\n\n"
            "Protection depends on process evidence. Contemporaneous reasons, due diligence, expert consultation, disclosed "
            "conflicts, equal treatment and absence of personal benefit support good faith. Concealed interests, fabricated "
            "records, deliberate rule evasion or reckless disregard defeat it. ARC's warning that every loss need not become "
            "a vigilance case preserves managerial initiative.\n\n"
            "The test is therefore neither subjective intention nor blanket immunity. Screening should separate error, "
            "negligence and corruption; competent investigators should then pursue actual knowledge, benefit and collusion. "
            "A reasoned, evidence-based test protects honest risk while keeping culpable conduct accountable."
        ),
    ),
    _original(
        10,
        (
            "Why do specificity screening and secret preliminary verification need both confidentiality "
            "and external accountability?"
        ),
        (
            "ARC recommends testing allegations for specificity, credibility and verifiability before formal inquiry. This "
            "filters revenge complaints from disciplined subordinates or blocked beneficiaries and prevents accusation alone "
            "from damaging an honest officer. Secret verification also preserves evidence and reputation: if the claim is false, "
            "unnecessary publicity is avoided.\n\n"
            "Yet secrecy can conceal institutional inaction. A captured vigilance unit may indefinitely shelve a specific "
            "complaint, protect senior officials or deny the complainant any traceable outcome. Confidentiality must therefore "
            "be paired with registration, time limits, recorded reasons, supervisory review and anonymised reporting. Identity "
            "access should be restricted, while closure remains reviewable by a competent independent authority.\n\n"
            "The correct design separates privacy from invisibility. Verification should be discreet enough to protect persons "
            "and evidence, but accountable enough to prevent secrecy from becoming impunity."
        ),
    ),
    _original(
        15,
        (
            "Differentiate Section 17A and Section 19 of the Prevention of Corruption Act, and "
            "assess the significance of the Supreme Court's split decision of 13 January 2026."
        ),
        (
            "Section 17A addresses an early stage. It requires prior approval before enquiry, inquiry or investigation into an "
            "alleged Prevention of Corruption Act offence relatable to a recommendation made or decision taken in discharge of "
            "official functions, subject to the statutory on-the-spot exception. Its purpose is to protect official decision-making "
            "from vexatious investigation. Section 19 operates later: previous sanction is required before a court takes cognizance "
            "of specified offences against a covered public servant. Thus investigative approval and prosecution-cognizance sanction "
            "must not be conflated.\n\n"
            "The former rank-based single directive in Delhi Special Police Establishment Act Section 6A was struck down in 2014 "
            "under Article 14. Section 17A is differently framed around conduct rather than rank, but its capacity to block even "
            "preliminary police action remains contested.\n\n"
            "In Centre for Public Interest Litigation v. Union of India, the two judges delivered divergent opinions on 13 January "
            "2026. The official order directed placement before the Chief Justice for an appropriate Bench. It therefore supplies "
            "no common final holding on constitutionality.\n\n"
            "The ethical verdict remains calibrated: honest decisions need protection, but approval must be prompt, independent, "
            "reasoned and reviewable so that procedure does not become a shield for corruption."
        ),
    ),
    _original(
        15,
        (
            "Investigator accountability and protection against arbitrary transfers are complementary "
            "requirements of ethical vigilance administration. Discuss."
        ),
        (
            "Vigilance can harass without proving guilt. ARC identified over-suspicion: investigators may treat a wrong outcome as "
            "corruption and implicate every person in the decision chain. This lowers precision, demoralises honest officials and can "
            "let actual wrongdoers escape. Its proposal for a specialised unit to examine corruption or harassment by investigators "
            "recognises that independence cannot mean immunity. Such review should test fabrication, selective targeting, delay and "
            "conflict while protecting bona fide investigative judgment.\n\n"
            "Transfer is a second, softer instrument. ARC's transfer-industry diagnosis shows how political control of postings can "
            "punish dissent without formal proceedings. Published policies, minimum tenure, recorded grounds for premature movement "
            "and independent appeal make retaliation visible. The Fifth Pay Commission's three-to-five-year norm, with shorter tenure "
            "for especially sensitive posts, supplies a concrete reform anchor.\n\n"
            "Both safeguards need qualifications. Investigator review must not permit accused officials to intimidate agencies, and "
            "tenure cannot block urgent reassignment where conflict or evidence risk is established. Narrow exceptions, written reasons "
            "and external review reconcile operational flexibility with integrity.\n\n"
            "Together, accountable investigation and fair postings protect lawful courage while preserving consequences for misconduct."
        ),
    ),
    _original(
        20,
        (
            "A procurement officer is orally directed by a Minister to favour an unqualified bidder "
            "and is threatened with transfer. Design the officer's written-dissent and whistleblowing response."
        ),
        (
            "The officer should first prevent an irreversible award without converting disagreement into personal confrontation. "
            "She should seek the direction in writing and make a contemporaneous file note recording the tender criteria, bidder's "
            "deficiency, public-finance risk and lawful alternatives. If any personal connection exists, it must be disclosed and "
            "recusal considered. A committee using pre-published criteria should complete evaluation so that discretion is not "
            "concentrated in one person.\n\n"
            "If pressure continues, she should record a reasoned dissent, cite the applicable rule and ask the competent superior to "
            "review. Relevant bids, communications, access logs and meeting records should be preserved securely. The concern should "
            "then move through the authorised vigilance or CVO channel. If that route is captured, escalation may proceed to the "
            "competent independent anti-corruption authority. Public disclosure is a last resort for grave residual harm after lawful "
            "channels fail; premature leakage can prejudice procurement and expose witnesses.\n\n"
            "The transfer threat should also be documented. She may seek review under published tenure policy and request a reasoned "
            "order, but must ensure a secure handover if moved. Resignation is not the first response because it abandons the file and "
            "citizens unless continued service demands direct illegality.\n\n"
            "Safeguards must not become self-exoneration. An independent body should verify the allegation, and the bidder and Minister "
            "must receive lawful process. The officer's protection rests on evidence, consistency and good faith, not merely on claiming "
            "to be honest. The course combines deontological refusal, consequential protection of funds and virtue-based courage with "
            "institutional prudence."
        ),
    ),
    _original(
        20,
        (
            "Design a vigilance system that protects honest officials, fairly handles POSH complaints "
            "and prevents procedural safeguards from becoming impunity."
        ),
        (
            "A sound system begins with symmetric risk: malicious allegation and investigative overreach can destroy honest initiative, "
            "while captured approvals, secrecy and hierarchy can shield corruption or harassment. Protection must therefore attach to "
            "good-faith process, not status.\n\n"
            "At entry, every corruption complaint should be registered securely and screened for specificity, credibility and verifiability. "
            "Confidential preliminary checking should protect reputation and evidence, but carry deadlines, reasons and supervisory review. "
            "Technically competent, impartial teams should examine the decision trail, conflict disclosures, benefit, knowledge and deliberate "
            "deviation. Prosecution should focus on strong evidence rather than every file signatory. Section 17A approval and Section 19 sanction "
            "must remain stage-distinct, prompt and reviewable. A separate mechanism should examine fabricated cases, selective investigation, "
            "identity leakage and retaliatory delay by investigators.\n\n"
            "The POSH route must remain independent. The Internal Committee should receive written complaints, protect confidentiality and "
            "participants, provide interim safeguards, define allegations, hear the respondent and issue reasoned recommendations. A threatened "
            "or actual POSH complaint must neither be dismissed merely because a vigilance case exists nor be used to freeze corruption evidence. "
            "Separate teams, restricted information sharing and anti-retaliation monitoring preserve both processes.\n\n"
            "Published transfer policy, minimum tenure, reasons for premature movement, protected whistleblowing channels and review of adverse "
            "career action address informal retaliation. Aggregate reporting should reveal delays without exposing identities.\n\n"
            "The final principle is protection without impunity: honest risk receives fair screening and defence, complainants receive safety and "
            "voice, investigators receive operational space, and every actor remains answerable through reasons, evidence and independent review."
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
        "1. Bona fides decision test",
        "decision-tree",
        (
            "Identify the decision actually taken",
            "Reconstruct facts known at that time",
            "Check prescribed rules and authority",
            "Test prudent-person plausibility",
            "Inspect reasons and due diligence",
            "Check conflict or personal benefit",
            "Separate outcome from decision process",
            "Classify error, negligence or misconduct",
        ),
        "A later loss is evidence to examine, not automatic proof of corruption.",
        "Use to open any good-faith-decision-gone-wrong answer.",
    ),
    _panel(
        "2. ARC's two-sided vigilance failure",
        "balance-map",
        (
            "Over-suspicion begins with bad outcome",
            "Whole decision chain is implicated",
            "Honest officers become risk-averse",
            "Investigative capacity loses precision",
            "Under-suspicion begins with captured safeguard",
            "Approval or secrecy creates delay",
            "Actual wrongdoers obtain protection",
            "Calibrated scrutiny corrects both sides",
        ),
        "Ethical vigilance must resist both harassment and institutional shielding.",
        "Use as the central thesis in a 15-mark analytical answer.",
    ),
    _panel(
        "3. Screening and secret verification rail",
        "process-rail",
        (
            "Receive complaint through secure channel",
            "Test specificity of alleged conduct",
            "Test credibility of source and facts",
            "Test verifiability through available records",
            "Preserve identity and evidence discreetly",
            "Use competent technical evaluation",
            "Record closure, escalation or investigation",
            "Permit supervisory review of delay",
        ),
        "Confidentiality protects persons; recorded review prevents invisible burial.",
        "Use for ARC paragraph 7.9 safeguards and complaint triage.",
    ),
    _panel(
        "4. Section 17A and Section 19",
        "comparison-chain",
        (
            "17A gate: pre-enquiry or investigation",
            "17A nexus: official recommendation or decision",
            "17A exception: on-the-spot undue advantage",
            "17A risk: inquiry blocked too early",
            "19 gate: court takes cognizance",
            "19 scope: specified corruption offences",
            "Both require timely competent decision",
            "Neither converts sanction into acquittal",
        ),
        "The provisions protect at different stages and must never be collapsed.",
        "Use for a legal-ethical distinction in GS-IV or GS-II overlap.",
    ),
    _panel(
        "5. From single directive to current uncertainty",
        "timeline",
        (
            "Executive single directive protected senior ranks",
            "Vineet Narain annulled executive protection",
            "CVC Act inserted DSPE Act 6A",
            "Subramanian Swamy struck 6A in 2014",
            "PC Amendment inserted 17A in 2018",
            "17A shifted from rank to conduct nexus",
            "Supreme Court split on 13 January 2026",
            "Official order referred matter for new Bench",
        ),
        "The old rank rule is gone; Section 17A's final constitutional status remains contested.",
        "Use for chronology and current-anchor accuracy.",
    ),
    _panel(
        "6. Accountability of investigators",
        "watchdog-loop",
        (
            "Protect operational independence",
            "Demand allegation and jurisdiction records",
            "Audit selective targeting or omission",
            "Test fabricated or suppressed evidence",
            "Review coercive delay and publicity",
            "Protect bona fide investigative judgment",
            "Provide independent complaint forum",
            "Publish anonymised accountability outcomes",
        ),
        "Watching investigators is compatible with independence when review targets abuse, not outcomes.",
        "Use to explain ARC's proposed investigator-accountability unit.",
    ),
    _panel(
        "7. Transfer industry and tenure protection",
        "cause-correction-map",
        (
            "Political demand targets an honest refusal",
            "Posting becomes reward or punishment",
            "Repeated movement destroys continuity",
            "Informal retaliation avoids formal process",
            "Publish objective transfer policy",
            "Provide minimum tenure norms",
            "Record grounds for premature transfer",
            "Allow independent appeal and narrow exception",
        ),
        "Transfer reform protects neutrality without creating ownership of a post.",
        "Use in politicisation, non-partisanship and honest-official cases.",
    ),
    _panel(
        "8. Written dissent implementation sequence",
        "action-ladder",
        (
            "Seek improper oral direction in writing",
            "Record facts, rules and public risk",
            "Disclose conflict and recuse if needed",
            "Use committee and published criteria",
            "State a reasoned written dissent",
            "Preserve records and access trails",
            "Escalate if the dissent is overridden",
            "Monitor residual risk after decision",
        ),
        "Conscience becomes administratively effective when converted into reasons, records and escalation.",
        "Use as the operational core of a Section-B answer.",
    ),
    _panel(
        "9. Whistleblower protection ladder",
        "escalation-ladder",
        (
            "Verify concern and avoid reckless accusation",
            "Preserve documents lawfully and securely",
            "Use internal authorised vigilance channel",
            "Restrict and log identity access",
            "Assess safety and retaliation risk",
            "Escalate beyond captured management",
            "Use external disclosure only as last resort",
            "Seek remedy for adverse career action",
        ),
        "Effective voice requires safe routing, evidence discipline and remedies against reprisals.",
        "Use for the 2022 whistleblower PYQ and retaliation cases.",
    ),
    _panel(
        "10. POSH due-process channel",
        "parallel-process-map",
        (
            "Receive written workplace complaint",
            "Constitute competent Internal Committee",
            "Protect confidentiality and participants",
            "Define allegations and preserve evidence",
            "Give respondent fair opportunity",
            "Complete impartial workplace inquiry",
            "Issue reasoned recommendations and action",
            "Keep criminal and vigilance routes distinct",
        ),
        "Protection of the complainant and fairness to the respondent are mutually necessary.",
        "Use where POSH is ignored, weaponised or mixed with corruption pressure.",
    ),
    _panel(
        "11. Protection without impunity matrix",
        "safeguard-matrix",
        (
            "Bona fide risk receives process protection",
            "Specific credible complaint receives inquiry",
            "False publicity receives confidentiality control",
            "Credible delay receives independent review",
            "Honest investigator receives operational space",
            "Abusive investigator receives accountability",
            "Tenure receives recorded protection",
            "Proved misconduct receives lawful consequence",
        ),
        "Every safeguard must protect integrity while preserving a path to verified accountability.",
        "Use as a balanced conclusion rather than a one-sided immunity claim.",
    ),
    _panel(
        "12. Examiner-ready answer spine",
        "answer-framework",
        (
            "Name the competing public values",
            "Identify over-suspicion or shielding risk",
            "Apply the bona fides process test",
            "Add screening and verification safeguards",
            "Separate 17A, 19 and adjudication stages",
            "Add dissent, transfer and reporting remedies",
            "Protect parallel POSH due process",
            "Conclude with protection without impunity",
        ),
        "A high-quality answer joins ethical principle, named institution, action and qualification.",
        "Use to structure 10-, 15- and 20-mark responses.",
    ),
)


CURRENT_ANCHOR = {
    "title": "Current official anchor: Supreme Court split on Section 17A",
    "verified_facts": (
        "On 13 January 2026, a two-judge Supreme Court Bench delivered divergent opinions in Centre for Public Interest Litigation v. Union of India on the constitutional validity and operation of Section 17A of the Prevention of Corruption Act.",
        "The signed order of the Court directed the Registry to place the matter before the Chief Justice of India for constitution of an appropriate Bench to consider the issues afresh.",
        "Because the opinions diverged and the matter was referred, the order did not produce a common final holding that either unanimously upheld or unanimously struck down Section 17A.",
    ),
    "administrative_link": (
        "The split captures the topic's central institutional dilemma. Prior approval may protect "
        "good-faith official decisions from frivolous or retaliatory investigation, yet an early "
        "executive gate may also obstruct scrutiny of actual corruption. An examiner-ready answer "
        "should therefore distinguish the continuing statutory text from the unresolved constitutional "
        "challenge and recommend prompt, independent, reasoned and reviewable administration."
    ),
    "limit": (
        "This anchor must not be described as a final Constitution Bench settlement. One opinion's "
        "reasoning cannot be presented as the common ratio of the Court. The operative official fact "
        "is the divergent decision and referral for fresh consideration; later orders or a larger-Bench "
        "decision would need fresh verification."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://api.sci.gov.in/supremecourt/2018/40618/40618_2018_4_1501_67544_Judgement_13-Jan-2026.pdf",
)


SOURCE_CAVEAT = (
    "Topic 21 owns the ethical and administrative design for protecting honest officials while "
    "preserving accountability. Its primary source spine is the Second Administrative Reforms "
    "Commission's bona fides test, two-sided vigilance diagnosis, allegation screening, secret "
    "preliminary verification, competent evaluation, strong-evidence prosecution and proposed "
    "accountability mechanism for investigating agencies. Topic 19 owns detailed Prevention of "
    "Corruption Act offence ingredients and complete criminal-law treatment; Topic 20 owns the "
    "full institutional jurisdictions of CVC, CBI, Lokpal, Lokayuktas, CVOs and State agencies; "
    "Topic 22 owns the general case-study method. Section 17A concerns approval before enquiry, "
    "inquiry or investigation of covered official-duty recommendations or decisions, subject to "
    "its statutory exception. Section 19 concerns previous sanction before court cognizance of "
    "specified offences. Neither provision is an acquittal. The former DSPE Act Section 6A single "
    "directive was rank-based and was struck down in Dr. Subramanian Swamy v. Director, CBI in "
    "2014. The Supreme Court's 13 January 2026 Centre for Public Interest Litigation order records "
    "divergent opinions on Section 17A and referral to the Chief Justice for a fresh Bench; it must "
    "not be stated as a unanimous final settlement. Transfer-industry material follows ARC Chapter "
    "9 and supports tenure, recorded reasons and review, but minimum tenure requires narrow justified "
    "exceptions. POSH Act workplace inquiry is distinct from corruption vigilance and from criminal "
    "process: complainant protection, confidentiality and anti-retaliation must coexist with defined "
    "allegations, impartial inquiry and respondent opportunity. Official local UPSC PDFs control PYQ "
    "wording. Long case studies are expressly labelled neutral routing because condensed entries do "
    "not reproduce every printed fact. Protection is earned by good-faith process and evidence, not "
    "by rank, self-description or institutional prestige."
)


REGISTER_SUPPLEMENT = (
    "### PROTECTING HONEST OFFICIALS AND VIGILANCE RAPID REGISTER\n\n"
    "#### 1. CENTRAL ETHICAL PROBLEM\n\n"
    "- Vigilance must protect lawful risk-taking and still expose actual corruption.\n"
    "- Two equal dangers: harassment through over-suspicion and impunity through captured safeguards.\n"
    "- Best thesis: protection follows bona fide process, while accountability follows verified evidence.\n"
    "- Never equate complaint, inquiry, charge or adverse outcome with guilt.\n\n"
    "#### 2. BONA FIDES TEST\n\n"
    "- ARC 7.1: ask whether a person of common prudence, acting within prescribed rules, could have taken the decision in the prevailing circumstances for the organisation's genuine interest.\n"
    "- Judge the process using facts known then, not hindsight alone.\n"
    "- Positive indicators: reasons, due diligence, expert advice, disclosed conflicts, equal treatment and no personal benefit.\n"
    "- Negative indicators: concealed interest, fabricated record, deliberate rule evasion, collusion or reckless disregard.\n"
    "- Every organisational loss need not become a vigilance inquiry.\n"
    "- Moral-luck correction: bad result can follow a reasonable decision; good result can conceal a corrupt process.\n\n"
    "#### 3. ARC'S TWO-SIDED FAILURE MODES\n\n"
    "- Over-suspicion: investigators presume that a wrong decision means corruption.\n"
    "- Overbreadth: everyone in the decision chain is alleged to be part of a conspiracy without role-specific proof.\n"
    "- Consequences: demoralisation, policy paralysis, weak investigation and actual offenders escaping.\n"
    "- Under-suspicion: approval, sanction, secrecy or hierarchy is used to delay or block a credible case.\n"
    "- Corrective: precise screening, competent evaluation, strong evidence and review of both investigators and sanctioning authorities.\n\n"
    "#### 4. SCREENING AND SECRET VERIFICATION\n\n"
    "- ARC 7.9(a): test specificity, credibility and verifiability before formal inquiry.\n"
    "- ARC 7.9(b): preliminary verification should remain secret to protect reputation and evidence.\n"
    "- ARC 7.9(c)-(d): use competent, honest and impartial evaluators; obtain technical expertise where needed.\n"
    "- ARC 7.9(f): prosecute public servants against whom evidence is strong.\n"
    "- Confidentiality is not invisibility: register the matter, impose timelines, record reasons and permit supervisory review.\n"
    "- False or unproved allegation is not automatically malicious; deliberate falsity needs separate proof.\n\n"
    "#### 5. SECTION 17A VERSUS SECTION 19\n\n"
    "- Section 17A: prior approval before enquiry, inquiry or investigation into an alleged PC Act offence relatable to an official-duty recommendation or decision.\n"
    "- Section 17A carries a statutory on-the-spot undue-advantage exception.\n"
    "- Section 19: previous sanction before a court takes cognizance of specified PC Act offences against a covered public servant.\n"
    "- Stage distinction: 17A is an investigative gate; 19 is a prosecution-cognizance gate.\n"
    "- Neither approval nor sanction decides guilt, and neither refusal should be unreasoned or indefinitely delayed.\n"
    "- Ethics test: does the authority independently distinguish bona fide judgment from evidence of corrupt benefit?\n\n"
    "#### 6. SINGLE DIRECTIVE AND CURRENT LEGAL ANCHOR\n\n"
    "- Executive single directive protected Joint Secretary-level and equivalent officers before investigation.\n"
    "- Vineet Narain annulled the executive version; CVC Act, 2003 inserted DSPE Act Section 6A.\n"
    "- Dr. Subramanian Swamy v. Director, CBI struck Section 6A down under Article 14 on 6 May 2014.\n"
    "- PC Amendment, 2018 inserted Section 17A with a conduct-based rather than rank-based nexus.\n"
    "- Centre for Public Interest Litigation v. Union of India, 13 January 2026: two judges gave divergent opinions.\n"
    "- The official order referred the issue to the Chief Justice for an appropriate Bench.\n"
    "- Current trap: do not call the split order a unanimous final validation or invalidation of Section 17A.\n\n"
    "#### 7. ACCOUNTABILITY OF INVESTIGATORS\n\n"
    "- ARC 7.8 proposed a specialised Lok Pal-linked unit, with State equivalents, to examine corruption by investigating agencies and allegations of harassment by them.\n"
    "- Investigator independence protects evidence-based judgment from accused-person pressure.\n"
    "- Investigator accountability addresses fabrication, selective targeting, leakage, coercive publicity, deliberate delay and conflict.\n"
    "- Review should assess misconduct and process, not punish investigators merely because a court later acquits.\n"
    "- Watch-the-watchers safeguard: independent appointment, recorded reasons, confidentiality, hearing and anonymised reporting.\n\n"
    "#### 8. TRANSFER INDUSTRY\n\n"
    "- ARC Chapter 9 treats arbitrary transfers as a political-control and transaction mechanism.\n"
    "- Repeated transfer can punish integrity without formal disciplinary action.\n"
    "- Fifth Pay Commission anchor: ordinary three-to-five-year tenure; two-to-three years for especially sensitive posts.\n"
    "- Correctives: published policy, objective criteria, stated grounds for premature transfer and appeal.\n"
    "- Transfers must not substitute for disciplinary procedure.\n"
    "- Qualification: urgent reassignment may be justified for conflict, evidence risk or operational harm, but reasons and review are essential.\n\n"
    "#### 9. WRITTEN DISSENT AND IMPLEMENTATION\n\n"
    "1. Seek improper oral instruction in writing.\n"
    "2. File-note facts, governing rule, public risk and lawful alternatives.\n"
    "3. Disclose conflict and recuse where personal interest exists.\n"
    "4. Use committees and pre-published criteria for discretionary decisions.\n"
    "5. Record a reasoned written dissent if pressure persists.\n"
    "6. Preserve records, communications and access trails.\n"
    "7. Escalate through authorised vigilance if dissent is overridden.\n"
    "8. Monitor residual risk through audit flag, reporting cycle or secure handover.\n"
    "- Silent compliance is unethical; silent refusal may also be inadequate because it leaves no institutional trail.\n\n"
    "#### 10. WHISTLEBLOWER LADDER\n\n"
    "- Verify the concern and preserve evidence lawfully.\n"
    "- Begin with internal or authorised vigilance channels where they are usable.\n"
    "- Restrict identity access; log every disclosure; assess threats promptly.\n"
    "- Provide interim safety, witness protection and review of adverse transfer, appraisal or suspension.\n"
    "- Escalate beyond a captured department to a competent independent authority.\n"
    "- External public disclosure is a last resort for grave residual harm and lawful necessity.\n"
    "- Resignation is not the first response unless remaining in office requires direct illegality.\n"
    "- Whistle Blowers Protection Act non-commencement makes dependable operational channels a continuing concern.\n\n"
    "#### 11. POSH DUE PROCESS\n\n"
    "- POSH Internal Committee is a workplace/service-rule inquiry route, not corruption vigilance and not a criminal court.\n"
    "- Core safeguards: accessible complaint, confidentiality, participant protection, impartial members, defined allegation, evidence testing, respondent opportunity and reasoned recommendation.\n"
    "- Employer must not ignore a complaint, purchase withdrawal or retaliate against complainant and witnesses.\n"
    "- A possible retaliatory motive does not justify dismissing the complaint without fair inquiry.\n"
    "- A POSH complaint does not erase corruption evidence or automatically halt a separate vigilance process.\n"
    "- Use separate teams, restricted information sharing and interim reporting arrangements when processes overlap.\n\n"
    "#### 12. PYQ AND ANSWER-WRITING SPINE\n\n"
    "- 2019 honest-official case: effects of fear plus bona fides test, screening, competent investigation and transfer protection.\n"
    "- 2019 apparel case: dignity, non-suppression, Internal Committee fairness and parallel remedies.\n"
    "- 2020 mall case: preserve evidence, disclose friendship, reject bribe, independently process threatened POSH complaint.\n"
    "- 2021 mining mafia: courage plus family safety, multi-agency evidence and protected escalation.\n"
    "- 2022 whistleblower: confidentiality plus physical safety, retaliation remedy and independent review.\n"
    "- 2022 Ramesh: written instruction, reasoned dissent, secure escalation and transfer-pressure record.\n"
    "- 2023 Vinod: verify political-source evidence without joining partisan incentives.\n"
    "- 2024 Raman: targeted intelligence, no community profiling, reasoned intrusion and investigator audit.\n"
    "- Answer order: value conflict -> failure mode -> bona fides test -> named safeguard -> action sequence -> accountability check -> qualification.\n\n"
    "> **Final thesis:** Ethical vigilance protects honest officials not by insulating rank or "
    "treating self-proclaimed good intention as proof, but by testing contemporaneous reasons, "
    "rules, conflicts and evidence through a fair process. The same architecture must prevent "
    "approval, secrecy, tenure, investigator independence or POSH procedure from becoming tools "
    "of impunity. Protection and accountability are credible only when each is reasoned, time-bound "
    "and independently reviewable."
)
