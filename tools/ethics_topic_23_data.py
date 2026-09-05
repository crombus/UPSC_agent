"""Learner-v2 source data: Ethics Topic 23, Comparative and Named Real Case Studies."""


SESSION_TITLES = (
    "Case method: mechanism, evidence, limitation and transfer",
    "Whistleblowers and parliamentary conduct: courage plus institutional response",
    "International models: prevention, deterrence, culture and attribution",
    "Civil society, research ethics, workplace safety and rights jurisprudence",
    "Prelims facts: dates, institutions, figures and legal status",
    "Close-option traps: precedent, interim order, guideline, statute and inference",
    "PYQ application: compare named evidence instead of decorating answers",
    "Mains analysis: causal mechanisms, trade-offs and selective adaptation",
    "Probable questions and examiner-ready comparative routes",
    "Study links, historical PYQs and the qualified rule-case answer spine",
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
        "Manjunath and Dubey reveal an unresolved protection gap",
        (
            "Manjunath Shanmugam and Satyendra Dubey exposed serious wrongdoing and were killed, "
            "but their ethical significance lies in the continuing need for safe reporting, "
            "identity protection, risk response and credible follow-up rather than martyrdom alone."
        ),
        (
            "An answer praises personal courage but proposes no secure channel, anti-retaliation measure "
            "or investigation route. What essential institutional lesson is missing?"
        ),
        (
            "A department separates the informer's identity, assesses threats, preserves evidence and "
            "routes the allegation independently. Which case-derived mechanism is being applied?"
        ),
        "whistleblower mechanism",
    ),
    _mcq(
        "The 2014 protection statute is not operational merely because enacted",
        (
            "The Whistle Blowers Protection Act received assent in 2014 but requires a commencement "
            "notification; an official Lok Sabha answer in 2025 stated that it had not been brought "
            "into force, while the administrative PIDPI route continued."
        ),
        (
            "A candidate says the 2014 enactment immediately supplied every whistleblower with an "
            "operational statutory remedy. Which legal-status distinction defeats the claim?"
        ),
        (
            "An answer distinguishes enacted text, commencement and the interim administrative route. "
            "Which form of legal precision does this demonstrate?"
        ),
        "whistleblower mechanism",
    ),
    _mcq(
        "Confidentiality is a process, not a slogan",
        (
            "Effective whistleblower protection requires restricted identity access, secure evidence "
            "storage, retaliation monitoring, emergency risk measures and independent review; merely "
            "labelling a complaint confidential does not control who can trace or punish the informant."
        ),
        (
            "A portal hides the complainant's name on screen but circulates an identifiable attachment "
            "to the accused chain. Which protection failure remains?"
        ),
        (
            "Only a designated cell can decrypt identity data, and every access is logged and reviewable. "
            "Which practical safeguard is illustrated?"
        ),
        "whistleblower mechanism",
    ),
    _mcq(
        "A whistleblower allegation still requires fair verification",
        (
            "The public value of disclosure does not convert allegation into guilt; institutions must "
            "protect the informant while authenticating records, defining the charge, hearing affected "
            "persons and leaving final responsibility to the competent forum."
        ),
        (
            "An agency publicly condemns an official solely because a protected complaint was filed. "
            "Which due-process error has occurred?"
        ),
        (
            "Identity protection operates alongside independent evidence testing and a fair hearing. "
            "Which balanced rule follows from the named whistleblower cases?"
        ),
        "whistleblower mechanism",
    ),
    _mcq(
        "Mudgal established a parliamentary corrective precedent",
        (
            "The 1951 H.G. Mudgal case showed that the House could treat proven acceptance of benefits "
            "for parliamentary favours as conduct incompatible with membership and use expulsion as "
            "institutional self-discipline."
        ),
        (
            "A legislator claims parliamentary privilege prevents the House from responding to proven "
            "paid advocacy by a member. Which precedent answers the claim?"
        ),
        (
            "The House acts on a committee's evidence and protects the integrity of representation. "
            "Which institutional capacity is shown?"
        ),
        "public accountability",
    ),
    _mcq(
        "Cash-for-questions confirms power but also reactivity",
        (
            "The 2005 cash-for-questions episode led to expulsion of ten Lok Sabha members and one Rajya "
            "Sabha member, yet the process followed external exposure; it proves corrective capacity "
            "more clearly than proactive detection."
        ),
        (
            "An answer cites the expulsions as proof that internal ethics systems automatically detect "
            "all misconduct. Which limitation has been ignored?"
        ),
        (
            "A reform retains expulsion for proved misconduct but adds disclosure analytics and proactive "
            "ethics monitoring. Which gap is it addressing?"
        ),
        "public accountability",
    ),
    _mcq(
        "MKSS Jan Sunwai converts records into public proof",
        (
            "MKSS combined official muster rolls, vouchers, beneficiary lists and completion certificates "
            "with community-witnessed public hearings, allowing villagers to cross-check paper claims "
            "against work, payment and local knowledge."
        ),
        (
            "A social audit meeting gathers grievances without obtaining the underlying records. Which "
            "distinctive evidentiary element of Jan Sunwai is absent?"
        ),
        (
            "Villagers compare muster-roll names with actual workers and publicly record contradictions. "
            "Which accountability mechanism is operating?"
        ),
        "public accountability",
    ),
    _mcq(
        "Parivartan made PDS diversion testable through RTI",
        (
            "Parivartan used access to fair-price-shop stock registers to compare recorded grain and oil "
            "with actual distribution, turning diffuse suspicion of diversion into a transaction-level "
            "accountability claim."
        ),
        (
            "Residents complain of shortages but cannot inspect stock or issue records. Which information "
            "bridge would the Parivartan example recommend?"
        ),
        (
            "A community reconciles shop registers, beneficiary accounts and physical delivery before "
            "seeking action. Which case mechanism is replicated?"
        ),
        "public accountability",
    ),
    _mcq(
        "Gyandoot reduced costly human intermediation",
        (
            "Gyandoot used locally operated kiosks to provide land records, market rates, applications, "
            "grievances and benefit information; its anti-corruption value arose from accessible services "
            "and reduced dependence on discretionary intermediaries."
        ),
        (
            "A district buys computers but citizens still require a broker to obtain every certified "
            "record. Which Gyandoot design objective remains unmet?"
        ),
        (
            "Village kiosks publish service access, fees and grievance registration without repeated "
            "office visits. Which mechanism is illustrated?"
        ),
        "process redesign",
    ),
    _mcq(
        "Bhoomi changed the mutation workflow",
        (
            "Bhoomi did more than digitise land records: automatic mutation notices, a defined objection "
            "period and kiosk access altered the workflow and reduced the revenue official's discretionary "
            "gatekeeping over routine transactions."
        ),
        (
            "An office scans records but preserves an undefined approval queue controlled by one official. "
            "Why is this unlike the strongest Bhoomi lesson?"
        ),
        (
            "A mutation request automatically generates notice, deadline and auditable status. Which "
            "anti-corruption design principle is applied?"
        ),
        "process redesign",
    ),
    _mcq(
        "CARD is the necessary digital-government counter-example",
        (
            "The ARC-cited evaluation of Andhra Pradesh's CARD project found no significant corruption "
            "difference between computerised and non-computerised Sub-Registrar Offices, warning that "
            "digitised records alone may leave discretionary decisions intact."
        ),
        (
            "A ministry claims any database conversion necessarily lowers bribery. Which named comparison "
            "directly challenges that inference?"
        ),
        (
            "A project evaluation asks whether approval discretion, valuation opacity and citizen dependence "
            "actually changed. Which CARD-derived test is being used?"
        ),
        "process redesign",
    ),
    _mcq(
        "Technology must be tied to the corruption mechanism",
        (
            "Bhoomi and CARD should be compared through the decision process: automation, notice, deadlines "
            "and auditability can reduce gatekeeping, while digitising storage without changing approval "
            "power may reproduce the same rent opportunity."
        ),
        (
            "Two portals use similar software but only one removes manual discretion. What variable should "
            "an ethical evaluation prioritise?"
        ),
        (
            "A reform maps each bribery opportunity to a redesigned step and measurable citizen outcome. "
            "Which comparative lesson is followed?"
        ),
        "process redesign",
    ),
    _mcq(
        "Hong Kong ICAC uses three mutually supporting prongs",
        (
            "Hong Kong's ICAC links law enforcement, corruption prevention and community education through "
            "specialised departments; the model treats punishment, system repair and social norms as "
            "complements rather than interchangeable substitutes."
        ),
        (
            "A government copies only investigative powers and omits prevention review and public education. "
            "Which part of the ICAC mechanism has been lost?"
        ),
        (
            "Investigators pursue offences while specialists redesign procedures and educators build public "
            "resistance to bribery. Which model is represented?"
        ),
        "comparative models",
    ),
    _mcq(
        "Singapore penalties must use current official figures",
        (
            "Singapore's CPIB states that the current general maximum is S$100,000 or five years' imprisonment "
            "or both per count, rising to seven years where corruption concerns a Government or public-body "
            "contract."
        ),
        (
            "An answer repeats the lower fine printed in the ARC's 2007 annexure as present law. Which "
            "source-handling error has occurred?"
        ),
        (
            "A candidate dates the ARC figure, then cites CPIB's current maximum separately. Which comparative "
            "practice is correct?"
        ),
        "comparative models",
    ),
    _mcq(
        "Korea's wider liability claim requires attribution",
        (
            "The ARC annexure attributes family and recommender consequences to Korea's 1975 reform, but "
            "independent corroboration for that extension is lacking; it should be presented as the ARC's "
            "account, not verified current Korean law."
        ),
        (
            "A student states that modern Korean law automatically punishes an offender's grandchildren. "
            "Which evidentiary caveat is missing?"
        ),
        (
            "An essay uses the claim hypothetically, identifies its ARC attribution and examines individual "
            "fairness. Which disciplined use is shown?"
        ),
        "comparative models",
    ),
    _mcq(
        "Finland and Thailand defeat single-lever explanations",
        (
            "CPI 2025 placed Finland at 88 and rank 2, while Thailand stood at 33 and rank 116 of 182; "
            "paired with their legal contexts, the figures caution against equating statutory severity "
            "alone with integrity."
        ),
        (
            "A proposal assumes harsher punishment mechanically produces a cleaner administration. Which "
            "current comparison supplies a caution?"
        ),
        (
            "An answer links sanctions with rule of law, enforcement, transparency and culture. Which "
            "multi-causal conclusion follows?"
        ),
        "comparative models",
    ),
    _mcq(
        "Vishaka was binding interim judicial law",
        (
            "Vishaka treated workplace sexual harassment as violating constitutional guarantees and issued "
            "binding guidelines until legislation; the 2013 workplace statute later created a detailed "
            "preventive and redress framework."
        ),
        (
            "An employer in 2005 argues that no duty existed because Parliament had not legislated. Which "
            "judicial mechanism defeats the claim?"
        ),
        (
            "A present answer cites the 2013 statute while using Vishaka for its constitutional foundation. "
            "Which historical sequence is correct?"
        ),
        "rights and safeguards",
    ),
    _mcq(
        "A statutory committee is not automatically impartial",
        (
            "The workplace statute mandates an Internal Committee and procedural timelines, but formal "
            "constitution cannot cure a personal conflict, employer capture or unsafe reporting culture; "
            "fair composition and reasoned process remain essential."
        ),
        (
            "The presiding officer is the respondent's direct business partner but refuses recusal because "
            "the committee exists by law. Which limitation is exposed?"
        ),
        (
            "An alternate unconflicted process preserves the complainant's safety and the respondent's hearing. "
            "Which rule-case balance is achieved?"
        ),
        "rights and safeguards",
    ),
    _mcq(
        "ICMR ethics makes consent an ongoing protection",
        (
            "The ICMR 2017 guidelines require comprehensible voluntary consent, added safeguards for vulnerable "
            "participants and continuing Ethics Committee oversight; a signed form cannot validate concealment, "
            "coercion or distorted safety reporting."
        ),
        (
            "A poor participant signs a technical form after being told treatment depends on joining. Which "
            "research-ethics defects remain?"
        ),
        (
            "The committee reviews recruitment pressure, translated information, withdrawal rights and adverse "
            "events. Which ethical framework is operating?"
        ),
        "rights and safeguards",
    ),
    _mcq(
        "Guidelines depend on institutional enforcement quality",
        (
            "ICMR guidance supplies substantive standards, but site-level protection depends on an independent "
            "and competent Ethics Committee that reviews risk, consent, vulnerability, safety reporting and "
            "protocol deviations without sponsor capture."
        ),
        (
            "A committee routinely approves sponsor submissions without reading adverse-event data. Which "
            "implementation limitation is illustrated?"
        ),
        (
            "Independent members demand complete safety data and suspend recruitment pending clarification. "
            "Which oversight responsibility is fulfilled?"
        ),
        "rights and safeguards",
    ),
    _mcq(
        "NHRC v Arunachal Pradesh protects every person's life",
        (
            "NHRC v State of Arunachal Pradesh applied Article 21 to Chakma and Hajong refugees and required "
            "State protection from forcible eviction and violence, demonstrating that life and personal "
            "liberty are not confined to citizens."
        ),
        (
            "A mob threatens non-citizens while officials treat nationality as a reason for inaction. Which "
            "constitutional precedent requires protection?"
        ),
        (
            "Police prevent violence and authorities process claims lawfully without promising permanent residence. "
            "Which precise duty is respected?"
        ),
        "remedy and limitation",
    ),
    _mcq(
        "Salimullah is an interim-order authority with limits",
        (
            "Mohammad Salimullah's 8 April 2021 order declined interim protection against deportation, required "
            "lawful procedure and discussed citizen-only residence rights; it did not finally determine every "
            "customary non-refoulement argument in the underlying dispute."
        ),
        (
            "An answer calls the interim order a final universal rejection of refugee protection. Which "
            "precedential overstatement is present?"
        ),
        (
            "A decision protects Article 21 process while separately examining lawful removal authority. Which "
            "paired reading with NHRC is appropriate?"
        ),
        "remedy and limitation",
    ),
    _mcq(
        "Bhagalpur and Nanavati are retrospective accountability tools",
        (
            "The Bhagalpur and Nanavati inquiries can identify causes, responsibility and institutional failure "
            "after communal violence, but their fact-finding cannot substitute for timely intelligence, lawful "
            "crowd control, protection and confidence-building during a crisis."
        ),
        (
            "A district delays preventive action because a future commission can investigate later. Which "
            "mechanism limitation has been misunderstood?"
        ),
        (
            "Administration acts immediately, preserves records and later cooperates with independent inquiry. "
            "Which complementary design is shown?"
        ),
        "remedy and limitation",
    ),
    _mcq(
        "D.K. Basu safeguards operate before guilt is known",
        (
            "D.K. Basu made arrest documentation, communication, medical examination, custody records and "
            "magisterial visibility procedural safeguards against abuse; compliance is required independently "
            "of whether the detainee is later convicted."
        ),
        (
            "Police omit the arrest memo because they consider the suspect obviously guilty. Which constitutional "
            "error does the precedent expose?"
        ),
        (
            "Officers document custody and medical condition while continuing a lawful investigation. Which "
            "rule-case mechanism is applied?"
        ),
        "remedy and limitation",
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
            "GS-IV Q12: Edward Snowden, a computer expert and former CIA systems administrator, "
            "released confidential Government documents to the press about Government surveillance "
            "programmes. Do you agree that Snowden's actions were ethically justified even if legally "
            "prohibited? Why or why not? Make an argument by weighing the competing values in this "
            "case. (250 words)"
        ),
        20,
        (
            "Faithful condensed routing verified against books\\more_previous_papers\\"
            "GENERAL-STUDIES-PAPER-IV.pdf, page 11. The official printed stem is longer and controls "
            "exact wording; this entry preserves its actor, act, demand and word limit."
        ),
        (
            "Snowden's disclosure can be ethically defended only through a necessity and proportionality test. "
            "The public-interest claim is that secret mass surveillance affects privacy, autonomy and democratic "
            "consent. Satyendra Dubey and Manjunath Shanmugam similarly show why internal wrongdoing may require "
            "protected escalation when ordinary hierarchy is implicated. Their cases prove the need for voice, "
            "not an unlimited licence to disclose every secret.\n\n"
            "Competing values are national security, confidentiality, lawful office, institutional trust and "
            "possible harm to operations or persons. A responsible whistleblower should first test whether an "
            "independent authorised channel is safe and effective, authenticate evidence, minimise unrelated "
            "disclosure and choose the least harmful route. MKSS offers the opposite context: official records "
            "were publicly cross-verified because community scrutiny was the accountability mechanism; intelligence "
            "material demands narrower handling.\n\n"
            "Therefore legality is morally relevant but not conclusive. Disclosure is strongest where wrongdoing "
            "is serious, internal remedies are captured or futile, evidence is reliable, public benefit is high "
            "and avoidable harm is minimised. It is weakest where mass release is indiscriminate. The cases support "
            "protected, proportionate truth-telling plus independent review, not either blind secrecy or heroic "
            "law-breaking as an automatic rule."
        ),
    ),
    _pyq(
        2019,
        (
            '"Non-performance of duty by a public servant is a form of corruption". '
            "Do you agree with this view? Justify your answer. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 2."
        ),
        (
            "I agree when non-performance is a deliberate misuse of entrusted power for private benefit, "
            "protection of allies or foreseeable public harm. Satyendra Dubey's road-contract disclosures show "
            "how official inaction toward credible corruption can enable systemic loss. Parivartan likewise showed "
            "that failure to reconcile PDS stock records allowed diversion to persist.\n\n"
            "But every shortfall is not corrupt. CARD's limited anti-corruption result warns that poor system design "
            "may preserve discretion even when individual staff operate the new technology. Capacity shortage, "
            "legal ambiguity, negligence and bona fide error require different diagnoses.\n\n"
            "The test should identify a clear duty, knowledge, ability to act, motive, benefit, harm and evidence. "
            "Wilful omission for improper advantage is corrupt; inability or reasonable error is not. Fair inquiry "
            "protects both accountability and honest administration."
        ),
    ),
    _pyq(
        2019,
        (
            "What do you understand by probity in governance? Based on your understanding of "
            "the term, suggest measures for ensuring probity in government. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 3."
        ),
        (
            "Probity is demonstrable integrity in public power: legality, impartiality, transparent reasons, "
            "answerability and fidelity to public purpose. It must be designed into systems. MKSS Jan Sunwai made "
            "probity testable by comparing public records with community evidence. Bhoomi reduced routine gatekeeping "
            "through automatic notices and deadlines, whereas CARD warns that digitisation without process redesign "
            "may leave corruption unchanged.\n\n"
            "Government should publish criteria and records, protect whistleblowers, disclose conflicts, conduct "
            "independent social audit, reduce monopoly discretion and ensure time-bound remedies. Parliamentary ethics "
            "systems should learn from Mudgal and cash-for-questions by adding proactive monitoring to their proven "
            "corrective power.\n\n"
            "Hong Kong's ICAC adds a useful synthesis: enforcement, prevention and community education should reinforce "
            "one another. Probity is sustained when ethical culture, auditable process and fair consequence operate "
            "together."
        ),
    ),
    _pyq(
        2021,
        (
            "An independent and empowered social audit mechanism is an absolute must in every "
            "sphere of public service, including judiciary, to ensure performance, accountability "
            "and ethical conduct. Elaborate. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3."
        ),
        (
            "Social audit makes official performance answerable to affected people. MKSS's Jan Sunwai joined muster "
            "rolls and vouchers with public cross-verification, exposing false workers, bills and completion claims. "
            "Parivartan similarly used PDS stock registers to test whether recorded supplies reached citizens. These "
            "cases show that independence requires access to usable records, community voice, protection against "
            "retaliation and mandatory action-taken reports.\n\n"
            "The mechanism has limits. A public hearing is not a criminal trial, and organisational capacity varies. "
            "For the judiciary, administrative expenditure, listing systems and service delivery may be audited, but "
            "the merits of judgments belong to appeal and review so decisional independence is preserved.\n\n"
            "Thus social audit should produce verified evidence and institutional learning, then route misconduct "
            "to the competent forum. It strengthens accountability without replacing investigation or adjudication."
        ),
    ),
    _pyq(
        2022,
        (
            "Whistle-blower, who reports corruption and illegal activities, wrongdoing and misconduct "
            "to the concerned authorities, runs the risk of being exposed to grave danger, physical "
            "harm and victimization by vested interests, accused persons and his team. What policy "
            "measures would you suggest to strengthen protection mechanism to safeguard the whistle-blower? "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 4."
        ),
        (
            "Manjunath Shanmugam and Satyendra Dubey show that courage without institutional protection can become "
            "fatal. Policy should provide a secure authorised channel, identity separation, access logs, immediate "
            "threat assessment, police protection where necessary, safe transfer, service protection, compensation "
            "and punishment for retaliation. Evidence must be preserved outside the accused hierarchy and examined "
            "by an independent authority.\n\n"
            "The legal gap must be stated precisely: a 2025 official Lok Sabha answer said the Whistle Blowers "
            "Protection Act, 2014 had not been brought into force; the PIDPI administrative mechanism remains relevant "
            "but is not an equivalent statutory shield. Time-bound acknowledgement, investigation updates and external "
            "review are therefore vital.\n\n"
            "Protection should coexist with good-faith thresholds and fair verification. The informant is protected "
            "from retaliation; the accused is protected from allegation-based guilt."
        ),
    ),
    _pyq(
        2023,
        (
            '"Corruption is the manifestation of the failure of core values in the society." '
            "In your opinion, what measures can be adopted to uplift the core values in the society? "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 2."
        ),
        (
            "Corruption reflects weakened honesty, fairness and public spirit, but values are reinforced or eroded "
            "by institutions. Hong Kong's ICAC combines community education with prevention and enforcement, showing "
            "that moral learning needs credible systems. Finland's CPI 2025 position, despite no single dedicated "
            "anti-corruption statute, similarly cautions against reducing integrity to punishment alone.\n\n"
            "Families, schools, professional bodies and public leaders should reject admiration of illicit wealth, "
            "teach constitutional morality and reward public-minded conduct. Government should protect whistleblowers, "
            "publish reasons and records, reduce discretionary bottlenecks and support citizen verification such as "
            "MKSS Jan Sunwai. Thailand's severe-penalty yet weaker CPI position warns that deterrence without institutional "
            "culture is insufficient.\n\n"
            "Core values rise when ethical conduct is socially respected, administratively feasible and fairly enforced consistently."
        ),
    ),
    _pyq(
        2024,
        (
            "The 'Code of Conduct' and 'Code of Ethics' are the sources of guidance in public "
            "administration. There is code of conduct already in operation, whereas code of ethics "
            "is not yet put in place. Suggest a suitable model for code of ethics to maintain integrity, "
            "probity and transparency in governance. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording, with punctuation normalised, verified against books\\mains\\"
            "05 UPSC 2024 Paper-IV_Final 1.pdf, page 4."
        ),
        (
            "A code of ethics should state public-service purposes rather than merely prohibited acts: constitutional "
            "fidelity, impartiality, truthfulness, stewardship, dignity, courage and reasoned accountability. Each value "
            "needs an operational rule. Dubey and Manjunath support protected reporting; MKSS supports public access and "
            "verification; D.K. Basu shows that dignity requires documented procedure even for unpopular persons.\n\n"
            "The code should require conflict disclosure, written reasons, recusal, protection of personal data, fair "
            "hearing, safe consultation and refusal of unlawful directions. Training should use named comparative cases, "
            "while independent ethics advisers and annual public reporting convert aspiration into practice.\n\n"
            "Enforcement must be proportionate and reviewable. Mudgal shows meaningful consequence for proven breach, "
            "but CARD warns that formal adoption without process change may achieve little. A living code links values, "
            "decision tests, support and fair accountability."
        ),
    ),
    _pyq(
        2024,
        (
            "In Indian culture and value system, an equal opportunity has been provided irrespective "
            "of gender identity. The number of women in public service has been steadily increasing over "
            "the years. Examine the gender-specific challenges faced by female public servants and suggest "
            "suitable measures to increase their efficiency in discharging their duties and maintaining high "
            "standards of probity. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\mains\\"
            "05 UPSC 2024 Paper-IV_Final 1.pdf, page 4."
        ),
        (
            "Female public servants may face harassment, stereotyping, unsafe postings, exclusion from informal "
            "networks, disproportionate care burdens and retaliation for reporting misconduct. These barriers impair "
            "equal opportunity and may pressure officers to tolerate unethical conduct. Vishaka located workplace "
            "safety in Articles 14, 15, 19(1)(g) and 21; the 2013 statute supplies a formal prevention and redress process.\n\n"
            "Measures should include safe infrastructure and transport, transparent posting and promotion criteria, "
            "flexible but non-penalising work arrangements, mentoring, leadership representation and confidential reporting. "
            "Internal Committees must be properly composed, independent and free from personal conflict; their mere existence "
            "does not guarantee fairness.\n\n"
            "As ICMR ethics shows in another domain, vulnerable-position safeguards need continuing oversight, not one-time "
            "paper compliance. Equality, safety and impartial process enable both efficiency and probity."
        ),
    ),
    _pyq(
        2025,
        (
            '"Constitutional morality is not a natural sentiment but a product of civil education '
            'and adherence of the rule of law." Examine the significance of constitutional morality '
            "for public servant highlighting the role in promoting good governance and ensuring "
            "accountability in public administration. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English wording, with the paper's spelling normalised, verified against books\\mains\\"
            "UPSC Mains 2025 GS Paper 4.pdf, page 2."
        ),
        (
            "Constitutional morality requires officials to exercise power through equality, dignity, liberty, reason "
            "and lawful procedure, especially when popularity points elsewhere. NHRC v Arunachal Pradesh required "
            "protection of non-citizens from violence because Article 21 covers every person. D.K. Basu similarly made "
            "custody safeguards obligatory before guilt is determined.\n\n"
            "For good governance, this ethic demands transparent criteria, recorded reasons, hearing, recusal and review. "
            "Vishaka shows constitutional values filling a legislative vacuum, while the later workplace statute shows "
            "their translation into durable procedure. Salimullah must be cited cautiously: its 2021 interim order addressed "
            "deportation relief and lawful procedure, not every refugee-law question finally.\n\n"
            "Thus civil education teaches the values, but institutions make them habitual. Constitutional morality restrains "
            "majoritarian impulse and official convenience while keeping accountability evidence-based and reviewable."
        ),
    ),
    _pyq(
        2022,
        (
            "Neutral routing of GS-IV Q10: an investigative journalist uncovers a stone-mining "
            "mafia involving corrupt police and civil officials and a politically connected media "
            "owner, while inducement and pressure are used to suppress publication. Evaluate the "
            "options, ethical dilemmas and appropriate response. (250 words)"
        ),
        20,
        (
            "Neutral demand routed from books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 10. The official multi-part "
            "case stem controls its complete facts and wording."
        ),
        (
            "The journalist faces truth and public interest against personal safety, source protection, confidentiality, "
            "editorial loyalty and the risk that premature publication may destroy evidence. Manjunath and Dubey warn that "
            "exposing a profitable network without protection can invite lethal retaliation. The first duty is therefore "
            "neither silence nor reckless heroism.\n\n"
            "He should authenticate permits, transport records, payments and communications; preserve encrypted copies in "
            "independent custody; document threats and inducements; obtain legal and trusted editorial review; and assess "
            "source-specific risk. A secure disclosure to a competent independent authority should precede or accompany "
            "carefully timed publication. Unrelated personal data and operational details should be minimised.\n\n"
            "MKSS and Parivartan show the power of transaction-level records and public verification, but the mining network "
            "also shows their limit where police, administration, politics and media ownership are captured. Escalation may "
            "require judicial protection or another legally competent forum. Publication should explain evidence and uncertainty, "
            "not pronounce guilt.\n\n"
            "The long-term remedy is network-focused: protect witnesses, reconcile extraction and royalty data, rotate captured "
            "posts, disclose ownership conflicts and create independent complaint routes. The qualified verdict is protected, "
            "evidence-led disclosure using the least harmful effective channel, followed by fair investigation and systemic repair."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Compare the ethical significance of Manjunath Shanmugam and Satyendra Dubey without "
            "reducing either case to a hero story."
        ),
        (
            "Both officers demonstrate integrity and moral courage against organised wrongdoing: Manjunath challenged "
            "fuel adulteration, while Dubey exposed corruption in highway construction. Their deaths prove that individual "
            "virtue can reveal serious misconduct but cannot supply its own protection.\n\n"
            "The institutional mechanism is therefore central: a safe authorised channel, identity separation, threat "
            "assessment, independent evidence custody, anti-retaliation remedies and time-bound investigation. The unresolved "
            "legal position matters. An official 2025 Lok Sabha answer stated that the Whistle Blowers Protection Act, 2014 "
            "had not been brought into force; PIDPI remains an administrative route, not an equivalent statutory guarantee.\n\n"
            "The limitation is equally important: protection cannot make an allegation self-proving. Fair verification and "
            "hearing remain necessary. The cases support protected courage joined to institutional duty, not martyrdom as a "
            "governance model."
        ),
    ),
    _original(
        10,
        (
            "What do the Mudgal and cash-for-questions cases establish about parliamentary ethics, "
            "and what do they fail to establish?"
        ),
        (
            "Mudgal in 1951 established that proven acceptance of benefits for parliamentary favours could be treated as "
            "conduct incompatible with membership. The 2005 cash-for-questions episode confirmed that Houses could investigate "
            "clear evidence and expel ten Lok Sabha members and one Rajya Sabha member. Together they show meaningful institutional "
            "self-discipline and reputational protection of representative office.\n\n"
            "They do not establish an effective preventive system. Mudgal followed a complaint, while the later expulsions followed "
            "a media sting. The mechanism was reactive and evidence-triggered; it says little about undetected conduct. Nor does "
            "expulsion replace criminal or other legal process where applicable.\n\n"
            "Reform should preserve fair committee inquiry and decisive consequence while adding conflict disclosure, gift and "
            "interest registers, proactive pattern review and reasoned public reporting. The cases prove corrective capacity, not "
            "automatic ethical health."
        ),
    ),
    _original(
        15,
        (
            "Compare MKSS Jan Sunwai and Parivartan as civil-society accountability mechanisms. "
            "Why are they more than generic examples of activism?"
        ),
        (
            "Both cases converted information rights into verifiable public claims. MKSS obtained muster rolls, vouchers, "
            "beneficiary lists and completion certificates, then used Jan Sunwai to compare them with community testimony. "
            "False workers, bills and completion claims became publicly demonstrable. Parivartan obtained fair-price-shop stock "
            "registers and compared recorded grain and oil with actual PDS delivery, exposing diversion.\n\n"
            "Their common mechanism is an evidence chain: access -> intelligible records -> affected-person verification -> public "
            "hearing or reconciliation -> reasoned demand for action. This differs from unsupported accusation and helps overcome "
            "information asymmetry. MKSS also influenced Rajasthan's ward-sabha social-audit role, showing institutional absorption.\n\n"
            "The models have limits. They depend on organised citizens, record access, local safety and a responsive consequence "
            "forum. Public findings are not convictions, and elite or violent capture may require protected escalation. Therefore "
            "replication needs facilitation funds, open data, witness protection and mandatory action-taken reports. Their lesson is "
            "not merely that civil society is beneficial, but that documentary access plus collective verification can transform "
            "private suspicion into accountable public evidence. Periodic independent evaluation should also test inclusion, "
            "record accuracy and whether verified findings actually produce timely corrective action."
        ),
    ),
    _original(
        15,
        (
            "Compare Bhoomi and CARD to explain when digital governance reduces corruption and "
            "when it merely computerises an existing problem."
        ),
        (
            "Bhoomi combined record computerisation with workflow change. Kiosk access reduced dependence on intermediaries; "
            "automatic mutation notices and a defined objection period constrained routine gatekeeping and created an auditable "
            "sequence. The ARC cites a 2002 evaluation finding efficiency gains and reduced corruption.\n\n"
            "CARD also computerised registration administration, but the ARC-cited Ramanathan and Balakrishnan evaluation found no "
            "significant corruption difference between computerised and non-computerised Sub-Registrar Offices. The defensible "
            "comparison is not superior hardware. It is whether the reform changed valuation, approval, queue and citizen-dependence "
            "mechanisms that generated rents. Digital storage can coexist with opaque discretion.\n\n"
            "A credible project should therefore map each corruption opportunity, automate only rule-bound steps, publish fees and "
            "deadlines, log overrides, provide appeal and test actual citizen experience. Gyandoot adds accessibility through local "
            "kiosks, but technology still cannot solve collusive procurement or captured enforcement.\n\n"
            "The verdict is conditional: digitisation reduces corruption when it redesigns the decision process and makes exceptions "
            "visible; otherwise it may give an old monopoly a faster interface. Procurement, maintenance, digital exclusion and "
            "grievance independence must also be audited throughout the project's life cycle."
        ),
    ),
    _original(
        20,
        (
            "Design an India-adapted anti-corruption strategy using Hong Kong's ICAC, Singapore's "
            "CPIB regime, the Korea attribution caveat, and the Finland-Thailand comparison."
        ),
        (
            "India should borrow mechanisms, not reputations. Hong Kong's ICAC supplies the organising architecture: enforcement, "
            "corruption prevention and community education work through distinct but connected departments. India can adapt this "
            "through Union, State and district networks rather than one city-scale campaign. Prevention teams should redesign "
            "high-risk services; education should use schools, professional bodies and local languages; investigators should remain "
            "operationally independent and reviewable.\n\n"
            "Singapore contributes credible deterrence. CPIB's current official statement gives a maximum S$100,000 fine or five "
            "years' imprisonment or both per count, rising to seven years for Government or public-body contract corruption, plus "
            "repayment consequences. India should draw the lesson of certainty, asset tracing and equal reach, not copy sentence "
            "numbers without comparing legal systems and due process.\n\n"
            "The ARC attributes extended family and recommender consequences to Korea's 1975 reform, but independent corroboration "
            "for that feature is lacking. It should not be asserted as current Korean law. Even hypothetically, collective liability "
            "would offend individual culpability; targeted beneficial-ownership scrutiny is a fairer adaptation.\n\n"
            "CPI 2025 placed Finland at 88 and rank 2 and Thailand at 33 and rank 116 of 182. Finland's dispersed legal framework and "
            "Thailand's severe penalties caution that drafting or harshness alone cannot create integrity. India's package should "
            "combine transparent systems, protected voice, swift fair enforcement, civic norms and measured outcomes. The conclusion "
            "is selective adaptation governed by federal scale, constitutional rights and verified evidence."
        ),
    ),
    _original(
        20,
        (
            "Apply the rule-case mechanism and limitation method to workplace harassment, research "
            "ethics, refugee protection, communal violence and custodial justice."
        ),
        (
            "The method has four moves: state the governing rule, show the named case's mechanism, identify its remedy and retain "
            "its limitation. For workplace harassment, Vishaka derived preventive and redress duties from Articles 14, 15, 19(1)(g) "
            "and 21 until legislation. The 2013 statute supplies an Internal Committee and timelines, but formal constitution does "
            "not cure conflict or capture.\n\n"
            "For research, ICMR's 2017 guidelines require comprehensible voluntary consent, added protection for vulnerable participants "
            "and continuing Ethics Committee oversight. A signed form is insufficient where recruitment is coercive or safety data is "
            "distorted; enforcement quality varies by institution.\n\n"
            "For refugees, NHRC v Arunachal Pradesh confirms Article 21 protection for every person and required State protection of "
            "Chakma and Hajong refugees. Mohammad Salimullah's 2021 interim order declined deportation relief subject to lawful procedure; "
            "it must not be inflated into a final settlement of every non-refoulement question. Apply dignity and process without inventing "
            "an absolute right to remain.\n\n"
            "Bhagalpur and Nanavati inquiries support retrospective truth and accountability but cannot replace immediate prevention, "
            "protection and lawful crisis command. D.K. Basu makes arrest records, communication and medical checks independent duties "
            "before guilt is known.\n\n"
            "Thus named authority is useful only when linked to the decision mechanism and residual gap. The answer should move from rule "
            "to action, safeguard, review and qualified remedy, never from famous name to automatic conclusion."
            " That discipline also prevents false equivalence across unlike institutional contexts."
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
        "1. Named-case reasoning chain",
        "case-method",
        (
            "Name the authority and date",
            "Identify the governing rule",
            "Extract the causal mechanism",
            "Connect evidence to the claim",
            "State the institutional remedy",
            "Retain the residual limitation",
            "Test transfer to new facts",
            "Give a qualified verdict",
        ),
        "A famous name earns marks only when it changes the reasoning.",
        "Use as the opening method for every comparative answer.",
    ),
    _panel(
        "2. Whistleblower protection architecture",
        "protection-rail",
        (
            "Receive through secure channel",
            "Separate identity from allegation",
            "Assess physical and service risk",
            "Preserve evidence independently",
            "Restrict and log identity access",
            "Investigate outside accused chain",
            "Prevent and remedy retaliation",
            "Report outcome with fair process",
        ),
        "Manjunath and Dubey show why courage requires a protection system.",
        "Use for whistleblower PYQs and integrity case studies.",
    ),
    _panel(
        "3. Parliamentary ethics comparison",
        "precedent-pair",
        (
            "Mudgal: paid parliamentary favour",
            "Mudgal: committee found misconduct",
            "Mudgal: House chose expulsion",
            "2005: external media exposure",
            "Lok Sabha: ten expelled",
            "Rajya Sabha: one expelled",
            "Strength: corrective discipline",
            "Limit: reactive detection",
        ),
        "The Houses proved corrective power, not comprehensive prevention.",
        "Use to balance institutional self-discipline with reform.",
    ),
    _panel(
        "4. Citizen evidence chain",
        "evidence-ladder",
        (
            "Obtain official records",
            "Make records locally intelligible",
            "Compare claim with lived delivery",
            "Use community witness and hearing",
            "Record contradiction precisely",
            "Route proof to competent authority",
            "Demand action-taken disclosure",
            "Protect participants from retaliation",
        ),
        "MKSS and Parivartan convert information access into testable accountability.",
        "Use for RTI, social audit and civil-society answers.",
    ),
    _panel(
        "5. Bhoomi versus CARD",
        "process-comparison",
        (
            "Both used digital administration",
            "Bhoomi improved record access",
            "Bhoomi automated mutation notice",
            "Bhoomi defined objection timing",
            "CARD digitised registration work",
            "CARD evaluation found no gap",
            "Key variable: decision discretion",
            "Test outcome, not computer count",
        ),
        "Digitised storage is not equivalent to redesigned discretion.",
        "Use for e-governance, corruption and service-delivery questions.",
    ),
    _panel(
        "6. Comparative anti-corruption models",
        "model-matrix",
        (
            "ICAC: enforcement",
            "ICAC: prevention",
            "ICAC: community education",
            "CPIB: credible deterrence",
            "CPIB: current penalty precision",
            "Korea: attribute ARC claim",
            "Finland: broad integrity ecology",
            "Thailand: severity is insufficient",
        ),
        "No single lever or foreign model is self-executing.",
        "Use to design selective, India-specific adaptation.",
    ),
    _panel(
        "7. Vishaka to workplace statute",
        "rule-transition",
        (
            "Harassment violates constitutional rights",
            "Court filled legislative vacuum",
            "Guidelines bound workplaces",
            "Directions lasted until legislation",
            "2013 law created formal process",
            "Internal Committee handles complaints",
            "Conflict can still impair fairness",
            "Safety and hearing must coexist",
        ),
        "A statutory forum needs impartial operation, not paper existence alone.",
        "Use for gender, dignity and institutional-design answers.",
    ),
    _panel(
        "8. ICMR research-ethics gate",
        "consent-gate",
        (
            "Explain purpose and procedure",
            "Disclose risk and expected benefit",
            "Ensure voluntary participation",
            "Protect withdrawal without penalty",
            "Add safeguards for vulnerability",
            "Review through Ethics Committee",
            "Report adverse events fully",
            "Reassess consent when facts change",
        ),
        "A signature cannot cure coercion, concealment or weak oversight.",
        "Use for clinical research and vulnerable-participant cases.",
    ),
    _panel(
        "9. Refugee-rights paired reading",
        "precedent-bridge",
        (
            "NHRC: Article 21 covers every person",
            "State must prevent threatened violence",
            "Claims require lawful processing",
            "Protection is not automatic residence",
            "Salimullah: interim order",
            "Interim stay was declined",
            "Removal still needs lawful procedure",
            "Customary-law debate not finally closed",
        ),
        "Hold dignity and lawful removal authority together without absolutes.",
        "Use for refugee, non-citizen and constitutional-morality answers.",
    ),
    _panel(
        "10. Crisis action versus later inquiry",
        "time-horizon",
        (
            "Monitor tension and credible rumour",
            "Use representative peace channels",
            "Protect vulnerable locations",
            "Apply lawful proportionate policing",
            "Preserve command and incident records",
            "Bhagalpur inquiry studies failure",
            "Nanavati inquiry assigns retrospective lessons",
            "Implement findings through reform",
        ),
        "A commission explains the past; administration must still prevent present harm.",
        "Use for communal peace and accountability case studies.",
    ),
    _panel(
        "11. D.K. Basu custody safeguards",
        "procedure-stack",
        (
            "Identify arresting personnel",
            "Prepare witnessed arrest memo",
            "Inform friend or relative",
            "Record place and time of custody",
            "Document injuries and medical checks",
            "Maintain custody diary entries",
            "Provide magistrate visibility",
            "Treat compliance as independent duty",
        ),
        "Procedural dignity applies before the State knows final guilt.",
        "Use for police ethics, rule of law and constitutional morality.",
    ),
    _panel(
        "12. Examiner-ready answer spine",
        "answer-spine",
        (
            "Open with direct ethical thesis",
            "Choose two genuinely comparable cases",
            "State each rule and exact mechanism",
            "Explain what the evidence proves",
            "Add current law or figure carefully",
            "Name limitation and contrary evidence",
            "Adapt remedy to Indian institutions",
            "Conclude with qualified transfer",
        ),
        "Case plus mechanism plus limitation is stronger than a catalogue of heroes.",
        "Use to structure 10-, 15- and 20-mark responses.",
    ),
)


CURRENT_ANCHOR = {
    "title": "Current official anchor: protection status, current penalties and comparative outcomes",
    "verified_facts": (
        "Lok Sabha Unstarred Question 628, answered 3 December 2025, stated that the Whistle Blowers Protection Act, 2014 had not been brought into force and described the 2015 amendment bill as lapsed; the answer also identified the PIDPI Resolution route.",
        "Singapore CPIB's current PCA page states a maximum fine of S$100,000 or imprisonment up to five years or both per corruption count, rising to seven years where the transaction concerns a Government or public-body contract.",
        "Transparency International's CPI 2025 data place Finland at 88 and rank 2, and Thailand at 33 and rank 116, among 182 countries.",
        "The Supreme Court's official 8 April 2021 Mohammad Salimullah order disposed of the interim application by declining release and a restraint on deportation, while requiring deportation to follow the prescribed procedure.",
    ),
    "administrative_link": (
        "These anchors update four distinct comparisons. The protection statute's non-commencement keeps the "
        "Manjunath-Dubey institutional gap live. Singapore requires current penalty figures rather than the ARC's "
        "historical amount. Finland and Thailand caution that integrity cannot be inferred from penalty severity "
        "alone. Salimullah must be used as an interim-order authority and paired with NHRC v Arunachal Pradesh, "
        "not converted into a final universal rule about refugees."
    ),
    "limit": (
        "CPI is a perception index and does not prove the causal effect of one law. Cross-country rankings cannot "
        "be transplanted without institutional context. The accessible official Salimullah order verifies the "
        "interim application's disposal and reasoning, but this data module does not claim a later final disposal "
        "of the underlying writ petition. Korea's family and recommender extension remains an ARC-attributed claim "
        "without independent corroboration."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://www.sansad.in/getFile/loksabhaquestions/annex/186/AU628_LKQJPi.pdf?source=pqals",
    "https://dopt.gov.in/sites/default/files/TheWhistleBlowersProtectionAct2011_2.pdf",
    "https://www.cpib.gov.sg/about-corruption/legislation-and-enforcement/prevention-of-corruption-act/",
    "https://sso.agc.gov.sg/Act/PCA1960",
    "https://www.icac.org.hk/en/about/struct/index.html",
    "https://www.icac.org.hk/symposium/2006/exhibition/p02.pdf",
    "https://www.transparency.org/en/cpi/2025",
    "https://www.transparency.org/en/countries/finland",
    "https://www.transparency.org/en/countries/thailand",
    "https://korruptiontorjunta.fi/en/national-legislation",
    "https://www.nacc.go.th/categorydetail/2019122712514151207005112EK12853/82f4a840959a42793e58377b270540ea",
    "https://www.indiacode.nic.in/handle/123456789/18898",
    "https://ethics.ncdirindia.org/asset/pdf/ICMR_National_Ethical_Guidelines.pdf",
    "https://api.sci.gov.in/supremecourt/2017/27338/27338_2017_31_1502_27493_Judgement_08-Apr-2021.pdf",
    "https://api.sci.gov.in/jonew/judis/13856.pdf",
    "https://api.sci.gov.in/jonew/judis/14580.pdf",
)


SOURCE_CAVEAT = (
    "Topic 23 owns the disciplined use of named evidence, not the complete law of every domain it "
    "touches. The 2nd ARC's Ethics in Governance report controls its accounts of Manjunath Shanmugam, "
    "Satyendra Dubey, H.G. Mudgal, cash-for-questions, MKSS Jan Sunwai, Parivartan, Gyandoot, Bhoomi, "
    "CARD and the comparative annexure. Manjunath and Dubey must establish the protection mechanism "
    "and unresolved gap, not a heroic narrative. Mudgal and cash-for-questions establish reactive "
    "parliamentary corrective capacity, not proof of preventive detection. MKSS and Parivartan work "
    "through documentary access plus public or beneficiary verification; a social-audit finding is "
    "evidence for action, not conviction. Bhoomi must be compared with CARD through process redesign "
    "and discretion, not technology branding. Singapore's ARC-era figures are historical; current "
    "penalties must follow CPIB or Singapore Statutes Online. The Korea family and recommender claim "
    "is attributed to the ARC annexure because independent corroboration was not found. CPI 2025 "
    "figures are comparative perception data, not causal proof. Vishaka was binding interim judicial "
    "law until legislation; the 2013 workplace statute now supplies the formal process, whose practical "
    "impartiality must still be tested. ICMR's 2017 research guidance supplies consent, vulnerability "
    "and Ethics Committee standards but is not one central criminal code. NHRC v State of Arunachal "
    "Pradesh confirms Article 21 protection for every person without creating an automatic right to "
    "remain. Mohammad Salimullah is an interim order of 8 April 2021 declining the requested restraint "
    "subject to lawful procedure; do not describe it as a final settlement of every non-refoulement "
    "argument. Bhagalpur and Nanavati inquiry materials are retrospective accountability evidence, not "
    "substitutes for real-time prevention. D.K. Basu safeguards are procedural duties independent of "
    "ultimate guilt; current statutory numbering should be checked under the BNSS before use. Official "
    "local UPSC PDFs control PYQ wording. Condensed case-study entries are neutral routing where stated "
    "and do not pretend to reproduce every printed fact. A named case should always be written through "
    "rule, mechanism, application, remedy and limitation."
)


REGISTER_SUPPLEMENT = (
    "### COMPARATIVE AND NAMED REAL CASES RAPID REGISTER\n\n"
    "#### 1. THE RULE-CASE-MECHANISM-LIMIT METHOD\n\n"
    "- Do not write a hero list.\n"
    "- Start with the governing ethical or legal rule.\n"
    "- Name the case, institution, date and source only when relevant.\n"
    "- State the causal mechanism: what changed behaviour, evidence, discretion or remedy?\n"
    "- Explain what the named evidence proves for the question.\n"
    "- Add the residual limitation, counter-example or unresolved status.\n"
    "- Transfer the mechanism, not the prestige of the name, to the new facts.\n"
    "- End with a qualified remedy and verdict.\n\n"
    "#### 2. MANJUNATH SHANMUGAM AND SATYENDRA DUBEY\n\n"
    "- Manjunath: IOC officer opposing fuel adulteration; killed 19 November 2005.\n"
    "- Dubey: NHAI engineer exposing road-construction corruption; killed 27 November 2003.\n"
    "- Core value: integrity plus moral courage.\n"
    "- Mechanism lesson: secure reporting, identity separation, threat response, independent evidence custody and anti-retaliation.\n"
    "- Official Lok Sabha answer dated 3 December 2025: Whistle Blowers Protection Act, 2014 had not been brought into force.\n"
    "- PIDPI is an administrative route; do not equate it with a commenced statutory shield.\n"
    "- Limitation: protection never turns allegation into guilt; independent verification remains necessary.\n"
    "- Best thesis: courage exposes wrongdoing, but institutions must make courage survivable and consequential.\n\n"
    "#### 3. MUDGAL AND CASH-FOR-QUESTIONS\n\n"
    "- H.G. Mudgal, 1951: acceptance of money or benefits for parliamentary favours; House accepted expulsion.\n"
    "- Cash-for-questions, 2005: ten Lok Sabha members and one Rajya Sabha member expelled.\n"
    "- Strength: Parliament can enforce ethical boundaries against its own members on clear evidence.\n"
    "- Mechanism: inquiry, recorded findings, House action and reputational defence of membership.\n"
    "- Limitation: both were complaint or exposure triggered; the cases show corrective more than preventive capacity.\n"
    "- Do not imply expulsion replaces any separately applicable criminal or legal process.\n"
    "- Reform route: disclosure registers, proactive ethics monitoring, fair inquiry and reasoned public consequence.\n\n"
    "#### 4. MKSS JAN SUNWAI AND PARIVARTAN\n\n"
    "- MKSS: muster rolls, vouchers, beneficiary lists and completion certificates cross-checked in public hearings.\n"
    "- Specific mechanism: record access + community witness + public contradiction + action demand.\n"
    "- Rajasthan later empowered ward sabhas with social-audit functions.\n"
    "- Parivartan: RTI access to fair-price-shop stock registers exposed PDS diversion.\n"
    "- Specific mechanism: recorded stock compared with beneficiary delivery.\n"
    "- Shared lesson: information becomes accountability only when intelligible, verifiable and linked to consequence.\n"
    "- Limitation: organisational capacity, local safety, record quality and follow-up are not automatic.\n"
    "- Social-audit evidence informs action; it does not itself adjudicate guilt.\n\n"
    "#### 5. GYANDOOT, BHOOMI AND CARD\n\n"
    "- Gyandoot: community-linked kiosks reduced citizen dependence on intermediaries for records, rates, applications and grievances.\n"
    "- Bhoomi: computerised land records plus automatic mutation notice and defined objection timing.\n"
    "- Bhoomi mechanism: accessible record + workflow automation + reduced discretionary gatekeeping + audit trail.\n"
    "- CARD: ARC-cited 2000 evaluation found no significant corruption difference between computerised and non-computerised offices.\n"
    "- CARD lesson: digital storage can preserve opaque valuation, approval and monopoly discretion.\n"
    "- Best comparison: similar digital reform, different redesign of the decision process.\n"
    "- Project test: map rent point, remove avoidable discretion, log override, publish fee and deadline, measure citizen outcome.\n"
    "- Limitation: service digitisation does not by itself solve collusive procurement or captured enforcement.\n\n"
    "#### 6. HONG KONG, SINGAPORE AND KOREA\n\n"
    "- Hong Kong ICAC established in 1974.\n"
    "- Three prongs: law enforcement, corruption prevention and community education.\n"
    "- Mechanism: punish wrongdoing, redesign opportunity and change social tolerance together.\n"
    "- Singapore CPIB current official maximum: S$100,000 or five years or both per count.\n"
    "- Government or public-body contract matter: imprisonment maximum rises to seven years.\n"
    "- Do not repeat the ARC's 2007 fine as current law.\n"
    "- Korea: ARC attributes wider family and recommender consequences to a 1975 reform.\n"
    "- Caveat: use only as an ARC-attributed claim; independent corroboration for that extension is lacking.\n"
    "- Ethical limit: collective liability conflicts with individual culpability; targeted asset scrutiny is safer.\n\n"
    "#### 7. FINLAND AND THAILAND\n\n"
    "- CPI 2025: Finland 88/100, rank 2 of 182.\n"
    "- CPI 2025: Thailand 33/100, rank 116 of 182.\n"
    "- Finland has no single dedicated anti-corruption statute, but bribery and related wrongdoing are criminalised through broader law.\n"
    "- Thailand's severe sanctions do not by themselves establish low corruption.\n"
    "- CPI measures perceptions of public-sector corruption; it is not direct prevalence or causal proof.\n"
    "- Comparative thesis: rule of law, transparency, enforcement certainty, civic norms and institutional trust interact.\n"
    "- Never infer that one statute, one agency or sentence severity explains a country's score.\n\n"
    "#### 8. VISHAKA AND THE 2013 WORKPLACE LAW\n\n"
    "- Vishaka, decided 13 August 1997: workplace sexual harassment violates Articles 14, 15, 19(1)(g) and 21.\n"
    "- Court issued binding guidelines until Parliament legislated.\n"
    "- The guidelines operated for sixteen years before the 2013 statute.\n"
    "- The statute mandates a workplace complaint and redress structure, including an Internal Committee.\n"
    "- Mechanism: prevention duties + safe complaint + inquiry + recommendation + employer action.\n"
    "- Limitation: formal committee existence does not cure conflict, employer capture or retaliation.\n"
    "- Case-study rule: protect complainant safety and confidentiality while preserving fair hearing and reasoned findings.\n\n"
    "#### 9. ICMR RESEARCH ETHICS\n\n"
    "- ICMR National Ethical Guidelines, 2017: informed consent is a comprehensible, voluntary process.\n"
    "- Explain purpose, procedure, risk, benefit, privacy, withdrawal and relevant alternatives.\n"
    "- Vulnerable participants require additional justification and safeguards.\n"
    "- Institutional Ethics Committee oversight continues beyond initial approval.\n"
    "- Safety data and protocol deviations must not be distorted or withheld.\n"
    "- A signed form cannot cure coercion, therapeutic misconception or material concealment.\n"
    "- Limitation: implementation depends on the independence and competence of the site-level committee.\n\n"
    "#### 10. NHRC v ARUNACHAL PRADESH AND SALIMULLAH\n\n"
    "- NHRC v State of Arunachal Pradesh, 1996: Article 21 protects every person, not citizens alone.\n"
    "- State had to protect Chakma and Hajong refugees from threatened eviction and violence.\n"
    "- The judgment does not create a general automatic right to remain in India.\n"
    "- Mohammad Salimullah order dated 8 April 2021 was an interim-order decision on requested relief.\n"
    "- The Court declined release and restraint on deportation, while requiring prescribed procedure.\n"
    "- Do not present the order as a final settlement of every customary non-refoulement argument.\n"
    "- Paired rule: universal life and due-process protection + lawful authority questions considered separately.\n"
    "- Avoid both automatic-protection and automatic-deportation answers.\n\n"
    "#### 11. BHAGALPUR, NANAVATI AND D.K. BASU\n\n"
    "- Bhagalpur 1989 inquiry: retrospective examination of communal violence and administrative or police failure.\n"
    "- Nanavati Commission, constituted 2000: retrospective inquiry into the 1984 anti-Sikh violence.\n"
    "- Commission mechanism: preserve evidence, reconstruct events, identify failure and recommend reform.\n"
    "- Limitation: later inquiry cannot replace real-time intelligence, protection, lawful policing and peacebuilding.\n"
    "- D.K. Basu, decided 18 December 1996: eleven safeguards governing arrest and custody.\n"
    "- High-yield safeguards: arrest memo, relative or friend information, custody record, injury record, medical checks and magistrate visibility.\n"
    "- Compliance is an independent constitutional duty regardless of eventual guilt.\n"
    "- Current statutory citations should use verified BNSS numbering, not assumed Cr.P.C. numbers.\n\n"
    "#### 12. PYQ AND ANSWER-WRITING SPINE\n\n"
    "- Whistleblower PYQ: Manjunath + Dubey -> courage, risk, legal status, secure protection architecture.\n"
    "- Social-audit PYQ: MKSS + Parivartan -> documentary access, public verification, competent follow-up.\n"
    "- Probity PYQ: Bhoomi + CARD -> system design and measured outcome; ICAC -> culture plus institution.\n"
    "- Core-values PYQ: Finland + Thailand -> sanctions are necessary but insufficient.\n"
    "- Gender PYQ: Vishaka + 2013 law -> constitutional foundation, statutory process, implementation conflict.\n"
    "- Constitutional-morality PYQ: NHRC + D.K. Basu + cautious Salimullah use -> dignity and lawful procedure.\n"
    "- Communal case study: immediate prevention first; Bhagalpur or Nanavati inquiry is later accountability.\n"
    "- Comparison formula: common question -> mechanism A -> mechanism B -> difference -> limits -> India-adapted remedy.\n"
    "- Evidence formula: claim -> named case -> what it proves -> limitation or qualification.\n"
    "- Final verdict: use named cases as transferable institutional reasoning, never decorative authority.\n\n"
    "> **Final thesis:** A high-quality GS-IV answer does not celebrate a case name and stop. It "
    "identifies the rule, explains the causal mechanism, shows what the evidence proves, retains "
    "the unresolved limitation and adapts the remedy to the new facts. Manjunath and Dubey, Mudgal "
    "and cash-for-questions, MKSS and Parivartan, Bhoomi and CARD, ICAC and CPIB, Vishaka and the "
    "workplace statute, NHRC and Salimullah, the inquiry commissions and D.K. Basu are therefore "
    "reasoning tools, not hero stories."
)
