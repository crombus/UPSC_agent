"""Learner-v2 source data: Ethics Topic 19, corruption legal framework."""


SESSION_TITLES = (
    "Visual foundation: evolution and the coercive-collusive legal map",
    "Essential definitions and exact statutory boundaries",
    "Mechanism: offences, proof, safeguards and supporting legal layers",
    "Indian applications and legally bounded examples",
    "Must-know facts for Prelims",
    "UPSC traps and close-option corrections",
    "PYQ application and source-routed legal use",
    "Mains angles, reform choices and the qualified answer thesis",
    "Probable questions and practice routes",
    "Study links, ownership boundaries and final synthesis",
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
        "The 2018 Amendment changed both reach and safeguards",
        (
            "The Prevention of Corruption (Amendment) Act, 2018 replaced the older "
            "gratification-centred s.7 with an undue-advantage formulation, created a "
            "standalone bribe-giving offence in s.8, added commercial-organisation "
            "liability, narrowed s.13, inserted s.17A and omitted s.24."
        ),
        (
            "A revision note says the 2018 reform merely increased punishments while leaving the "
            "offence structure unchanged. Which set of structural changes disproves that claim?"
        ),
        (
            "An answer calls the 2018 reform wholly pro-enforcement. Which simultaneous narrowing "
            "and approval safeguard require a more qualified assessment?"
        ),
        "evolution, classification and reform",
    ),
    _mcq(
        "Coercive and collusive bribery are ARC categories",
        (
            "The Second Administrative Reforms Commission distinguishes coercive bribery, where "
            "an unwilling citizen pays for an entitlement or to avoid harassment, from collusive "
            "bribery, where giver and taker benefit while the state or public loses; these labels "
            "are analytical categories, not express classifications in the PC Act."
        ),
        (
            "A pensioner pays after an official threatens indefinite delay. How should the "
            "transaction be classified for ethical analysis without falsely claiming that the "
            "statute itself uses that label?"
        ),
        (
            "A contractor pays to secure acceptance of substandard work. Why is equal moral "
            "treatment of the contractor and the extorted pensioner analytically unsound?"
        ),
        "evolution, classification and reform",
    ),
    _mcq(
        "Section 7 governs the public servant being bribed",
        (
            "PC Act s.7 covers a public servant who obtains, accepts or attempts to obtain an "
            "undue advantage with the required connection to improper or dishonest performance "
            "of public duty, including receipt as a reward; proof must satisfy the statutory "
            "ingredients rather than merely show an unpopular official decision."
        ),
        (
            "An officer accepts money to suppress a mandatory inspection. Which PC Act provision "
            "directly addresses the public servant's acceptance?"
        ),
        (
            "A policy choice benefits one firm but no undue advantage or corrupt exchange is "
            "shown. Why can Section 7 not be inferred from benefit alone?"
        ),
        "Sections 7 and 8",
    ),
    _mcq(
        "Section 8 separately criminalises bribe-giving",
        (
            "PC Act s.8 punishes giving or promising an undue advantage with intent to induce "
            "improper performance of public duty or to reward such performance; after 2018, the "
            "giver's liability is therefore not confined to abetment of the public servant's offence."
        ),
        (
            "A bidder promises payment so a tender evaluation will be dishonestly altered. Which "
            "standalone offence applies to the giver?"
        ),
        (
            "A note states that only the public servant can commit a principal bribery offence. "
            "Which 2018 provision makes that proposition obsolete?"
        ),
        "Sections 7 and 8",
    ),
    _mcq(
        "Section 8's compulsion defence is conditional",
        (
            "A person compelled to give an undue advantage can invoke s.8's statutory "
            "protection only if the matter is reported to a law-enforcement authority or "
            "investigating agency within seven days from giving it; this is narrower than a "
            "general immunity for every person who later claims pressure."
        ),
        (
            "A citizen pays an extortionate demand for release of an entitled certificate and "
            "reports it two days later. Which statutory condition is central?"
        ),
        (
            "A contractor voluntarily paid for an unlawful advantage and alleges coercion months "
            "after detection. Why does Section 8 not automatically protect that claim?"
        ),
        "Sections 7 and 8",
    ),
    _mcq(
        "Assisted investigative conduct has a separate Section 8 protection",
        (
            "PC Act s.8 does not apply where, after informing a law-enforcement authority or "
            "investigating agency, a person gives or promises an undue advantage in order to "
            "assist that authority or agency in its investigation; this must not be confused with "
            "the seven-day compulsion proviso."
        ),
        (
            "A complainant, acting after informing investigators, hands over marked currency in a "
            "lawful trap. Which Section 8 distinction prevents treating the complainant as an offender?"
        ),
        (
            "Why should an answer separate prior investigative cooperation from a post-payment "
            "claim of compulsion?"
        ),
        "Sections 7 and 8",
    ),
    _mcq(
        "Section 9 creates commercial-organisation liability",
        (
            "A commercial organisation is punishable with fine under s.9 when an associated "
            "person gives or promises an undue advantage intending to obtain or retain business, "
            "or an advantage in business, for that organisation, subject to the statutory "
            "adequate-procedures defence."
        ),
        (
            "An intermediary bribes a licensing officer to retain a company's contract. Which "
            "provision addresses organisational liability?"
        ),
        (
            "A company argues that only the individual intermediary can ever be liable. Which "
            "post-2018 offence defeats that categorical defence?"
        ),
        "corporate liability and criminal misconduct",
    ),
    _mcq(
        "Adequate procedures belong to Section 9",
        (
            "PC Act s.9 permits the commercial organisation to prove that it had adequate "
            "procedures, compliant with prescribed guidelines, to prevent associated persons from "
            "undertaking the prohibited conduct; it is a statutory defence for the organisation, "
            "not automatic immunity created by a paper compliance manual."
        ),
        (
            "A company had risk-based controls, training, due diligence and enforced reporting "
            "systems before a rogue agent acted. Which defence must still be proved on evidence?"
        ),
        (
            "A dormant anti-bribery policy was ignored by management. Why does the mere existence "
            "of the document not settle the adequate-procedures question?"
        ),
        "corporate liability and criminal misconduct",
    ),
    _mcq(
        "Section 10 requires consent or connivance",
        (
            "Where an s.9 offence is committed by a commercial organisation and is proved in "
            "court to have occurred with the consent or connivance of a director, manager, "
            "secretary or other officer, s.10 makes that officer personally guilty; it does "
            "not impose liability on every senior officer merely by designation."
        ),
        (
            "Emails show a director approved an agent's bribery plan. Which personal-liability "
            "ingredient is engaged?"
        ),
        (
            "A remote officer had no knowledge, involvement or connivance. Why is hierarchy alone "
            "insufficient under Section 10?"
        ),
        "corporate liability and criminal misconduct",
    ),
    _mcq(
        "Post-2018 Section 13 has two criminal-misconduct heads",
        (
            "PC Act s.13 now confines criminal misconduct to dishonest or fraudulent "
            "misappropriation or conversion of property entrusted to, or under the control of, a "
            "public servant, including allowing another person to do so, and intentional illicit "
            "enrichment during the period of office."
        ),
        (
            "A public servant diverts entrusted relief material for connected private sale. Which "
            "current Section 13 head is directly relevant?"
        ),
        (
            "Assets become disproportionate to known lawful income and cannot be satisfactorily "
            "accounted for. Which current Section 13 concept is engaged?"
        ),
        "corporate liability and criminal misconduct",
    ),
    _mcq(
        "The abuse-of-position head was removed from Section 13",
        (
            "The 2018 Amendment deleted the former broad s.13(1)(d) abuse-of-position route; "
            "favouritism or an indefensible decision may remain ethically, disciplinarily or under "
            "another offence legally wrongful, but it is not automatically current s.13 "
            "criminal misconduct without one of the surviving statutory heads."
        ),
        (
            "An official arbitrarily favours a relative but personal enrichment and entrusted-property "
            "misappropriation are not proved. Why must an answer avoid citing the deleted provision?"
        ),
        (
            "How does the narrowing protect good-faith policy discretion while potentially reducing "
            "reach against favouritism-based wrongdoing?"
        ),
        "supporting laws and current gaps",
    ),
    _mcq(
        "Section 17A operates before specified investigation",
        (
            "PC Act s.17A requires previous approval before a police officer conducts an enquiry, "
            "inquiry or investigation into a PC Act offence alleged against a serving or former "
            "public servant where the allegation is relatable to a recommendation made or decision "
            "taken in discharge of official functions or duties."
        ),
        (
            "Investigators propose to examine a retired officer's official procurement decision. "
            "Which approval-stage provision must be tested?"
        ),
        (
            "An answer limits Section 17A to serving Joint Secretary-level officers. Which two "
            "statutory scope errors does it make?"
        ),
        "Sections 17A and 19",
    ),
    _mcq(
        "Section 17A contains a timeline and spot-arrest exception",
        (
            "The approving authority must convey its s.17A decision within three months, "
            "extendable by one month for reasons recorded in writing; previous approval is not "
            "required for cases involving on-the-spot arrest of a person accepting or attempting "
            "to accept an undue advantage."
        ),
        (
            "An officer is caught while accepting marked currency. Which express exception prevents "
            "Section 17A from becoming a shield against the immediate trap?"
        ),
        (
            "An authority remains silent beyond four months. Why should an answer mention breach "
            "or delay without inventing deemed approval?"
        ),
        "Sections 17A and 19",
    ),
    _mcq(
        "Section 19 concerns court cognizance and prosecution sanction",
        (
            "PC Act s.19 bars a court from taking cognizance of specified offences alleged to have "
            "been committed by a public servant without previous sanction of the competent "
            "government or authority; the current list is Sections 7, 10, 11, 13 and 15, not every "
            "offence in the Act."
        ),
        (
            "A court is asked to take cognizance of a qualifying Section 13 charge against a public "
            "servant. Which stage-specific safeguard must be satisfied?"
        ),
        (
            "Why is it inaccurate to say Section 19 expressly lists Sections 8 and 9?"
        ),
        "Sections 17A and 19",
    ),
    _mcq(
        "Sections 17A and 19 guard different stages",
        (
            "PC Act s.17A addresses previous approval before specified enquiry, inquiry or "
            "investigation into an official-duty recommendation or decision, whereas s.19 "
            "addresses previous sanction before the court takes cognizance for listed offences; "
            "one safeguard cannot be described as merely another name for the other."
        ),
        (
            "An answer says prosecution sanction is always the first permission needed before any "
            "fact-finding. Which distinction corrects it?"
        ),
        (
            "Why can a matter raise both Section 17A and Section 19 questions at different times?"
        ),
        "Sections 17A and 19",
    ),
    _mcq(
        "Section 20 creates a rebuttable evidentiary presumption",
        (
            "In a trial for an offence punishable under s.7 or s.11, once acceptance, "
            "obtaining or attempted obtaining of an undue advantage by the accused public servant "
            "is proved, s.20 directs the court to presume the relevant corrupt motive, reward "
            "or absence/inadequacy of consideration unless the contrary is proved."
        ),
        (
            "The prosecution proves acceptance of an undue advantage in a Section 7 trial. Which "
            "provision shifts the evidentiary burden without eliminating the chance of rebuttal?"
        ),
        (
            "Why is it wrong to describe Section 20 as an irrebuttable presumption of guilt for "
            "every PC Act offence?"
        ),
        "proof and parallel accountability",
    ),
    _mcq(
        "Omitted Section 24 was limited even before omission",
        (
            "Before 2018, s.24 protected a person from s.12 prosecution on the basis "
            "of a statement in proceedings against a public servant that the person had offered "
            "gratification; it was not blanket immunity for all bribe-givers, and the 2018 "
            "Amendment omitted it."
        ),
        (
            "A note states that old Section 24 permanently immunised every payer in every setting. "
            "Which two qualifications are missing?"
        ),
        (
            "What replaced the earlier structure when Section 8 became a standalone giver offence?"
        ),
        "evolution, classification and reform",
    ),
    _mcq(
        "Special Judges and trial timelines remain distinct safeguards",
        (
            "PC Act offences are tried by Special Judges under s.4; trial should proceed "
            "day to day as far as practicable, with an endeavour to conclude within two years and "
            "recorded six-month extensions, while total trial time should not ordinarily exceed "
            "four years."
        ),
        (
            "A candidate confuses investigation approval with the forum and pace of trial. Which "
            "Section 4 features should be separately stated?"
        ),
        (
            "Why does the statutory trial endeavour not guarantee disposal in exactly two years?"
        ),
        "proof and parallel accountability",
    ),
    _mcq(
        "Criminal and departmental processes are not identical",
        (
            "The same suspected misconduct may generate vigilance screening, departmental "
            "proceedings, criminal prosecution and civil or confiscation action, each with its own "
            "authority, purpose, standard and remedy; criminal acquittal does not mechanically end "
            "every departmental inquiry."
        ),
        (
            "Evidence fails to prove a PC Act offence beyond reasonable doubt, but service-rule "
            "misconduct remains supported on the applicable departmental standard. What distinction applies?"
        ),
        (
            "Why must an audit or vigilance finding be treated as a lead rather than a criminal conviction?"
        ),
        "proof and parallel accountability",
    ),
    _mcq(
        "The 2016 Benami regime strengthened asset recovery prospectively in form",
        (
            "The Benami Transactions (Prohibition) Amendment Act, 2016 substantially re-enacted "
            "and renamed the 1988 statute as the Prohibition of Benami Property Transactions Act, "
            "1988, effective from 1 November 2016, with fuller definitions, adjudication, appeal "
            "and confiscation machinery."
        ),
        (
            "An answer treats the original 1988 confiscation provision as fully operational for "
            "the preceding eighteen years. Which ARC diagnosis and 2016 reform correct it?"
        ),
        (
            "Which date marks commencement of the substantially strengthened 2016 regime?"
        ),
        "supporting laws and current gaps",
    ),
    _mcq(
        "Ganpati Dealcom's 2022 judgment was recalled",
        (
            "On 18 October 2024, the Supreme Court recalled its 23 August 2022 Ganpati Dealcom "
            "judgment and restored Civil Appeal No. 5783 of 2022 for fresh adjudication because "
            "constitutional validity had been decided without a lis and contest; the recalled "
            "2022 conclusions must not be cited as the present settled merits position."
        ),
        (
            "A candidate states that the 2022 bar on retrospective operation remains the Supreme "
            "Court's final word. Which 2024 procedural event defeats that statement?"
        ),
        (
            "Why does recall reopen the issue rather than establish the opposite merits conclusion?"
        ),
        "supporting laws and current gaps",
    ),
    _mcq(
        "The Whistle Blowers Protection Act remains uncommenced",
        (
            "The Whistle Blowers Protection Act, 2014 received Presidential assent on 9 May 2014 "
            "but no commencement notification under s.1(3) has been issued; the 2015 "
            "Amendment Bill lapsed, while the 2004 PIDPI Resolution remains the interim central "
            "administrative mechanism."
        ),
        (
            "A public servant assumes the 2014 Act supplies an operational statutory shield today. "
            "Which commencement fact must be checked first?"
        ),
        (
            "What limited interim mechanism should be named without pretending that it equals a "
            "comprehensive commenced statute?"
        ),
        "supporting laws and current gaps",
    ),
    _mcq(
        "Wilful non-performance is not automatically a PC Act offence",
        (
            "The ARC's acts-of-omission analysis can treat wilful or grossly negligent "
            "non-performance that causes public harm or connected benefit as an ethical and "
            "disciplinary corruption failure, but criminal liability still requires proof of the "
            "ingredients of an applicable offence."
        ),
        (
            "An inspector knowingly suppresses a mandatory violation report to benefit a connected "
            "operator. How should the ethical failure be described without inventing a general PC Act offence?"
        ),
        (
            "A good-faith policy judgment later fails. Which bona-fides limit prevents every adverse "
            "outcome from being labelled corruption?"
        ),
        "proof and parallel accountability",
    ),
    _mcq(
        "ARC reform proposals must not be presented as enacted law",
        (
            "The ARC recommended a distinct and more severely punished collusive-bribery offence, "
            "a presumption where public loss is established, and extended coverage for specified "
            "public-utility providers and substantially government-funded NGOs; these are reform "
            "proposals, not descriptions of the current PC Act."
        ),
        (
            "An answer claims every NGO receiving more than half its operating cost from government "
            "is already expressly covered by the cited ARC clause. What source-status error occurs?"
        ),
        (
            "How should the proposal for tougher collusive-bribery treatment be used in a Mains conclusion?"
        ),
        "evolution, classification and reform",
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
            "Neutral routing of GS-IV Q12: Edward Snowden disclosed classified information about "
            "government surveillance, claiming a moral duty to inform the public despite the "
            "Espionage Act. Were his actions ethically justified even if legally prohibited? "
            "Weigh the competing values. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "GENERAL-STUDIES-PAPER-IV.pdf, page 11. The official paper contains the full case. "
            "Topic 19 uses it for the law-versus-whistleblowing boundary; Topic 22 owns complete "
            "case-study method."
        ),
        (
            "Snowden's claim engages public interest, privacy, democratic accountability and "
            "conscience, while the opposing side invokes legality, official secrecy, national "
            "security, institutional trust and foreseeable harm. Whistleblowing is not justified "
            "merely because the discloser sincerely disagrees with policy. A defensible ethical "
            "assessment asks whether the wrongdoing was serious, evidence was verified, authorised "
            "channels were available or compromised, disclosure was proportionate, sensitive "
            "material was minimised and likely public benefit exceeded avoidable harm.\n\n"
            "On that test, exposing unlawful or structurally unaccountable surveillance may serve "
            "constitutional democracy, especially where internal remedies are ineffective. Yet a "
            "bulk disclosure that unnecessarily exposes legitimate operations, individuals or "
            "security methods remains ethically blameworthy even if the central warning was "
            "valuable. Legal prohibition is highly relevant but not always morally conclusive; "
            "equally, moral purpose does not erase legal accountability.\n\n"
            "For Indian application, the answer should avoid claiming that the Whistle Blowers "
            "Protection Act, 2014 currently protects such disclosure: it has not been brought into "
            "force. The sound conclusion is qualified justification only where necessity, evidence, "
            "proportionality and public-interest safeguards are convincingly established."
        ),
    ),
    _pyq(
        2019,
        (
            'GS-IV Q2(b): "Non-performance of duty by a public servant is a form of corruption". '
            "Do you agree with this view? Justify your answer. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 2. Topic 19 owns the distinction between the "
            "ARC's ethical acts-of-omission analysis and actual PC Act criminal ingredients."
        ),
        (
            "I agree only in a qualified ethical sense. Public office is entrusted for lawful and "
            "timely performance. Wilful inaction can operate like corruption when an officer delays "
            "an entitlement to extract payment, deliberately ignores an offence to favour a "
            "connected person, or suppresses a mandatory report so another gains and the public "
            "loses. The ARC's broader acts-of-omission analysis therefore treats deliberate "
            "dereliction as a corruption failure even without a visible cash transfer.\n\n"
            "However, poor outcome, delay or error is not automatically corrupt. Capacity shortage, "
            "conflicting legal duties, reasonable prioritisation and a bona fide decision that later "
            "fails require administrative learning, not criminal stigma. The test should examine a "
            "clear duty, knowledge, capacity, wilfulness or gross negligence, improper benefit, "
            "foreseeable harm and concealment.\n\n"
            "The legal boundary is essential: the PC Act does not create a general offence called "
            "non-performance of duty. Criminal liability arises only when facts satisfy Section 7, "
            "13 or another applicable offence; disciplinary liability may operate on a different standard."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Section B concluding question: India seeks effective civil-service ethics, codes "
            "of conduct, transparency measures, ethics and integrity systems and anti-corruption "
            "agencies. Suggest institutional measures for anticipating threats, strengthening ethical "
            "competence and developing integrity-promoting administrative processes. (250 words)"
        ),
        20,
        (
            "Faithful condensed routing verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 7. Topic 19 uses the legal-framework component; "
            "Topics 16 and 20 own codes and detailed institutional jurisdictions."
        ),
        (
            "Threat anticipation should begin with legal and process mapping. Departments should "
            "identify points where an undue advantage can alter licensing, inspection, procurement, "
            "tax, transfer or benefit decisions. Risk registers should combine complaint patterns, "
            "audit findings, unexplained overrides, conflict declarations and recurring delay. "
            "Officials need practical training on Sections 7 and 8, corporate-bribery exposure under "
            "Sections 9 and 10, current Section 13 limits, evidence preservation and the distinct "
            "stages governed by Sections 17A and 19.\n\n"
            "Integrity-promoting processes include written criteria, reasoned orders, role separation, "
            "protected reporting, independent verification and fair, time-bound disciplinary and "
            "criminal referral. Section 17A should protect genuine official decisions without becoming "
            "indefinite investigative obstruction; Section 19 sanction decisions likewise require "
            "recorded, timely treatment. Companies dealing with government should maintain genuine "
            "adequate anti-bribery procedures rather than symbolic policies.\n\n"
            "Whistleblower safety remains a gap because the 2014 Act is uncommenced; interim PIDPI "
            "protection cannot be treated as equivalent to a comprehensive statute. Benami asset "
            "recovery and recovery of public loss should complement prosecution. The design must "
            "combine prevention, evidence, due process and remedy, while detailed agency allocation "
            "is left to the relevant institutional framework."
        ),
    ),
    _pyq(
        2021,
        (
            "Neutral routing of GS-IV Q7: a newly posted officer confronts an illegal sand-mining "
            "mafia supported by local functionaries, bribed and intimidated residents, compromised "
            "employees and a wider nexus. Examine the ethical issues and the appropriate official "
            "response. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, pages 4-5. The official paper contains the "
            "complete facts and sub-questions. Topic 19 uses it for bribery classification, evidence "
            "and legal-process boundaries; Topic 22 owns complete option analysis."
        ),
        (
            "The facts indicate an organised corruption network rather than a single transaction. "
            "Payments or inducements used to obtain illegal extraction and official protection are "
            "collusive in the ARC sense where both payer and recipient benefit while public revenue, "
            "ecology and rule of law suffer. Poor residents acting under intimidation may instead be "
            "coerced participants or witnesses and should not be equated with principal beneficiaries.\n\n"
            "The officer should protect life, secure records and physical evidence, separate compromised "
            "staff from sensitive functions and coordinate lawful investigation. Suspected acceptance "
            "by public servants must be tested against Section 7; giver conduct against Section 8; "
            "company involvement may raise Sections 9 and 10; illicit enrichment or entrusted-property "
            "misappropriation may engage current Section 13. These provisions should not be asserted "
            "without proof of their ingredients. Approval under Section 17A depends on whether inquiry "
            "concerns an official-duty recommendation or decision; the spot-acceptance exception must "
            "also be remembered.\n\n"
            "Witness protection, confidential reporting, transparent permit and transport trails, "
            "revenue recovery and disciplinary proceedings should accompany criminal referral. "
            "Individual arrests alone will fail unless the enabling administrative network is dismantled."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q6(a): A whistle-blower reporting corruption, illegal activities, wrongdoing and "
            "misconduct risks exposure to grave danger, physical harm and victimisation by vested "
            "interests. What policy measures would strengthen the protection mechanism? (150 words)"
        ),
        10,
        (
            "English wording verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 4. Minor punctuation is "
            "normalised from the official bilingual paper. This is Topic 19's direct whistleblower PYQ."
        ),
        (
            "Protection must begin with a safe, confidential reporting channel, identity minimisation, "
            "secure evidence handling and a prohibition on unauthorised disclosure. A credible system "
            "needs early threat assessment, transfer or workplace protection, legal and financial "
            "support, time-bound inquiry, anti-retaliation remedies and personal accountability for "
            "victimisation. Anonymous information may trigger verification, but adverse action should "
            "rest on tested evidence and fair hearing.\n\n"
            "India's legal status must be stated precisely. The Whistle Blowers Protection Act, 2014 "
            "received assent but has not been brought into force because no Section 1(3) commencement "
            "notification has issued. The 2015 Amendment Bill lapsed. The PIDPI Resolution, 2004 remains "
            "an interim administrative route for specified central matters, but it is not a substitute "
            "for a comprehensive commenced statute.\n\n"
            "Reform should operationalise a balanced law with narrowly defined security exclusions, "
            "independent review of withheld disclosures, witness protection, interim relief and "
            "penalties for retaliation or malicious identity disclosure. Protection should reward "
            "responsible evidence-based reporting without immunising knowingly false complaints."
        ),
    ),
    _pyq(
        2022,
        (
            "Neutral routing of GS-IV Q10: an investigative journalist uncovers a stone-mining "
            "mafia involving corrupt officials, politicians and a conflicted media owner, but faces "
            "inducement and pressure to suppress the report. Evaluate the legal-ethical issues and "
            "the appropriate response. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 10. Topic 19 uses the "
            "corruption-law and whistleblower-protection dimensions; Topic 22 owns complete case method."
        ),
        (
            "The network suggests collusive corruption: illegal commercial gain is exchanged for "
            "official protection, while ecology, public revenue and lawful competitors bear the loss. "
            "The offered inducement to the journalist creates a fresh integrity test. He should refuse "
            "and document it, authenticate the material, preserve copies and protect sources. Publication "
            "must be proportionate and legally reviewed so that necessary public disclosure does not "
            "recklessly expose witnesses or compromise a legitimate investigation.\n\n"
            "Evidence concerning public servants should be routed to competent authorities and tested "
            "against statutory ingredients: Section 7 for acceptance of undue advantage, Section 8 for "
            "the giver, Sections 9 and 10 where a commercial organisation and consenting officers are "
            "involved, and Section 13 only where its surviving misappropriation or illicit-enrichment "
            "heads are made out. A media allegation, however credible, is not itself conviction. "
            "Investigative permissions and prosecution sanction arise at their distinct statutory stages.\n\n"
            "The journalist cannot assume comprehensive protection under the uncommenced 2014 "
            "Whistle Blowers Act. Safety planning, secure channels and independent editorial or legal "
            "support are therefore indispensable. The administrative response must trace money, permits "
            "and decisions and dismantle the protective network, not merely punish one visible official."
        ),
    ),
    _pyq(
        2023,
        (
            'GS-IV Q2(a): "Corruption is the manifestation of the failure of core values in the '
            'society." In your opinion, what measures can be adopted to uplift the core values in '
            "the society? (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 2. Topic 19 supplies the "
            "law-and-incentive qualification; Topics 1 and 2 own general value formation."
        ),
        (
            "Corruption reflects failure of honesty, fairness, responsibility and regard for public "
            "goods, but values operate within incentives. A citizen may condemn bribery yet pay under "
            "coercion for an entitlement; a business may normalise collusion because opaque discretion "
            "and weak enforcement make it profitable. Value uplift therefore requires family and school "
            "example, civic education, ethical leadership and social disapproval of illicit wealth, "
            "combined with institutions that make integrity practicable.\n\n"
            "Law should distinguish roles and mechanisms. Section 8's conditional protection for a "
            "compelled payer supports reporting, while collusive givers require accountability. Sections "
            "9 and 10 should be reinforced by real corporate anti-bribery procedures. Clear entitlements, "
            "reasoned decisions, transparent processes, protected complaints and fair, timely enforcement "
            "reduce opportunities for values to be overwhelmed.\n\n"
            "Punishment alone can produce fear without character; moral exhortation alone can produce "
            "cynicism where corruption pays. Sustainable reform aligns personal virtue, professional "
            "norms, opportunity reduction, credible detection, proportionate consequence and protection "
            "for those who resist or report wrongdoing."
        ),
    ),
    _pyq(
        2023,
        (
            "GS-IV Q2(b): In the context of work environment, differentiate between 'coercion' "
            "and 'undue influence' with suitable examples. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 2. Topic 19 uses the "
            "distinction to clarify Section 8 compulsion; the PYQ's terms are not statutory labels "
            "for ARC coercive and collusive bribery."
        ),
        (
            "Coercion uses an explicit or implicit threat of serious harm to compel conduct. A licensing "
            "clerk who threatens indefinite denial of an entitled certificate unless paid constrains the "
            "citizen's practical freedom. Undue influence exploits authority, trust, dependence or "
            "vulnerability so that judgment is overborne without a direct threat; for example, a superior "
            "repeatedly links a junior's appraisal prospects to selection of a preferred vendor.\n\n"
            "Evidence differs. Coercion focuses on demand, threat, constrained choice and prompt complaint. "
            "Undue influence focuses on positional power, private access, dependency, unusual departure "
            "from criteria and the resulting decision. Reasoned persuasion is neither. Safeguards include "
            "written directions, plural decision-making, review of transfer and appraisal powers, conflict "
            "disclosure and anti-retaliation channels.\n\n"
            "For corruption law, precision matters. ARC's coercive-versus-collusive bribery distinction "
            "is analytical, while Section 8 uses the statutory word compelled and requires reporting within "
            "seven days. The workplace concept of undue influence should not be substituted for either "
            "the statutory ingredients of bribery or the ARC's collusive category."
        ),
    ),
    _pyq(
        2023,
        (
            "Neutral routing of GS-IV Q12: a public-sector executive receives documents and a video "
            "suggesting that the corporation's chairman demanded a bribe connected with a large tyre "
            "order and accelerated pending bills. What should the executive do and which ethical and "
            "legal concerns arise? (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, pages 10-11. The official case "
            "contains the full institutional and personal pressures. Topic 19 owns provision-level "
            "routing; Topic 22 owns complete case architecture."
        ),
        (
            "The documents create a credible allegation, not a concluded offence. The executive should "
            "secure original metadata and copies, record chain of custody, avoid alerting persons who "
            "could destroy evidence and seek confidential legal or authorised vigilance advice. The "
            "video must be authenticated and procurement files, bill-clearing patterns, communications "
            "and decision reasons independently examined. He should disclose any personal or political "
            "conflict and resist pressure either to suppress the matter or publicly convict the chairman.\n\n"
            "If a public servant demanded or accepted an undue advantage for dishonest performance, "
            "Section 7 may apply. The payer or promisor may raise Section 8; company liability depends "
            "on Section 9's associated-person and business-benefit elements, while personal corporate "
            "officer liability under Section 10 requires consent or connivance. Section 13 should be "
            "invoked only for its surviving misappropriation or illicit-enrichment heads. Section 17A "
            "and Section 19 must be assessed at their distinct investigation and cognizance stages.\n\n"
            "The executive's duty is lawful escalation, evidence protection and institutional continuity, "
            "not private retaliation. Fair hearing and confidentiality protect both the inquiry and innocent "
            "reputations while enabling proportionate criminal, disciplinary and contractual action if proved."
        ),
    ),
    _pyq(
        2024,
        (
            "Neutral routing of GS-IV Q11: farmers facing water scarcity allege that the district "
            "administration is corrupt and has been bribed by industries drawing groundwater, while "
            "closure threatens employment. Discuss the options, compatible stakeholder measures and "
            "the administrator's ethical dilemmas. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\mains\\"
            "05 UPSC 2024 Paper-IV_Final 1.pdf, page 9. The official case contains the full "
            "water-allocation facts and sub-questions. Topic 19 uses it for allegation, proof and "
            "legal-classification boundaries; Topic 22 owns complete case method."
        ),
        (
            "The collector must separate the urgent resource crisis from the unproved bribery allegation. "
            "Immediate action should use lawful water-priority rules, verified extraction data, temporary "
            "conservation directions, drinking-water protection and transparent allocation criteria. "
            "Industries should face metering, recharge, recycling and proportionate curbs; farmers need "
            "equitable schedules, efficient irrigation support and a reasoned grievance forum. Employment "
            "effects matter but cannot legalise unsustainable extraction.\n\n"
            "The corruption claim requires confidential evidence collection, protection against retaliation "
            "and independent review of permissions, inspection records, payments, communications and conflict "
            "links. Public accusations or political pressure cannot substitute for proof. If an undue "
            "advantage induced dishonest official action, Sections 7 and 8 may be engaged; company conduct "
            "may raise Sections 9 and 10. Current Section 13 is not a general abuse-of-position offence, so "
            "its surviving heads must be proved. Section 17A applicability depends on whether the proposed "
            "inquiry concerns an official-duty recommendation or decision.\n\n"
            "The ethical dilemma is not farmers versus workers alone; it is impartial scarcity management "
            "under distrust. Publishing verified data and reasons, while keeping the criminal inquiry fair "
            "and confidential, can protect both ecological justice and due process."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Distinguish Section 17A approval from Section 19 sanction under the Prevention of "
            "Corruption Act. Why does the distinction matter?"
        ),
        (
            "Section 17A and Section 19 protect different procedural stages. Section 17A requires "
            "previous approval before a police officer conducts an enquiry, inquiry or investigation "
            "into a PC Act allegation relatable to a recommendation made or decision taken by a serving "
            "or former public servant in discharge of official functions. It is rank-neutral, prescribes "
            "three months plus a recorded one-month extension, and excludes on-the-spot arrest while "
            "accepting or attempting to accept an undue advantage.\n\n"
            "Section 19, by contrast, prevents a court from taking cognizance of listed offences alleged "
            "against a public servant without previous sanction of the competent government or authority. "
            "Its list is Sections 7, 10, 11, 13 and 15; it is not a universal list of all PC Act offences.\n\n"
            "The distinction matters because conflation can either obstruct lawful preliminary action or "
            "erase a statutory safeguard. A precise answer states the stage, trigger, authority, timeline "
            "and exception, while acknowledging the common policy tension between protecting bona fide "
            "decision-making and preventing delay from shielding corruption."
        ),
    ),
    _original(
        10,
        (
            "How far does Section 8 of the Prevention of Corruption Act reflect the ARC's "
            "coercive-collusive bribery distinction?"
        ),
        (
            "The ARC classifies coercive bribery as extortion from an unwilling citizen seeking an "
            "entitlement, while collusive bribery benefits giver and taker at public cost. The PC Act "
            "does not expressly enact these labels. Nevertheless, Section 8 partly reflects the "
            "distinction by making bribe-giving a standalone offence while protecting a person who was "
            "compelled to give the undue advantage and reports it to law enforcement or an investigating "
            "agency within seven days. A separate protection covers giving after informing investigators "
            "to assist an investigation.\n\n"
            "This structure can protect the coerced victim and pursue the willing beneficiary. It also "
            "reduces the older mismatch after Section 24 was omitted. Yet the alignment is incomplete. "
            "Compelled is a statutory term requiring case-specific proof; collusive bribery is not a "
            "separately named current offence with the ARC's recommended special presumption and enhanced "
            "punishment. The seven-day condition may also burden fearful or vulnerable victims.\n\n"
            "Thus Section 8 moves toward the ARC's moral distinction but does not convert that analytical "
            "framework into a complete statutory classification."
        ),
    ),
    _original(
        15,
        (
            "The 2018 Prevention of Corruption Amendment simultaneously strengthened and narrowed "
            "anti-corruption law. Analyse with reference to Sections 7, 8, 9, 10 and 13."
        ),
        (
            "The Amendment strengthened the transactional side of anti-corruption law. Section 7 now "
            "uses the defined term undue advantage, which is not confined to cash and excludes legal "
            "remuneration. Section 8 makes giving "
            "or promising a bribe a standalone offence, while preserving conditional protection for a "
            "compelled payer who reports within seven days and for informed assistance to an investigation. "
            "Sections 9 and 10 add a corporate dimension: a commercial organisation may be fined for "
            "business-linked bribery by an associated person, subject to an adequate-procedures defence, "
            "and consenting or conniving directors or officers may incur personal liability.\n\n"
            "The same reform narrowed Section 13. Criminal misconduct is now confined to dishonest or "
            "fraudulent misappropriation or conversion of entrusted property and intentional illicit "
            "enrichment. The former broad abuse-of-position head was removed. This improves certainty and "
            "reduces the danger that a defensible policy choice is criminalised merely because it favours "
            "one outcome. Conversely, favouritism causing public loss without direct enrichment may become "
            "harder to prosecute under Section 13, even when disciplinary or other legal liability survives.\n\n"
            "The correct assessment is therefore double-edged. The Amendment closes giver and corporate "
            "liability gaps but contracts one route against public-servant misconduct. Reform should combine "
            "clear offences with evidence-based enforcement, genuine corporate prevention and safeguards "
            "that protect bona fide discretion without creating impunity."
        ),
    ),
    _original(
        15,
        (
            "Assess the two unresolved supporting gaps in India's anti-corruption legal framework: "
            "whistleblower protection and Benami-law retrospectivity."
        ),
        (
            "Detection and asset recovery are indispensable companions to bribery prosecution, yet both "
            "areas contain verified uncertainty. The Whistle Blowers Protection Act, 2014 received assent "
            "on 9 May 2014, but no commencement notification under Section 1(3) has been issued. A December "
            "2025 official parliamentary answer confirmed that amendments were considered necessary before "
            "commencement; the 2015 Amendment Bill had lapsed. PIDPI, 2004 remains an interim central "
            "administrative mechanism, but it cannot be presented as equivalent to a comprehensive operative "
            "statute. This gap chills reporting and leaves retaliation protection fragmented.\n\n"
            "The 2016 Benami amendment created fuller identification, adjudication and confiscation machinery "
            "from 1 November 2016. In 2022, Ganpati Dealcom made major findings against retrospective reach "
            "and the unamended provisions. On 18 October 2024, however, the Supreme Court recalled that "
            "judgment because constitutional validity had been decided without a lis and contest, and restored "
            "the appeal for fresh adjudication. Recall removes the earlier judgment as the settled merits "
            "position; it does not establish the opposite conclusion.\n\n"
            "India needs a balanced commenced whistleblower law with reviewable security exclusions, "
            "anti-retaliation relief and confidentiality, alongside prompt fresh adjudication and clear "
            "transition rules for Benami proceedings. Until then, answers must state the gaps and uncertainty."
        ),
    ),
    _original(
        20,
        (
            "Evaluate the internal architecture of the Prevention of Corruption Act after 2018, "
            "including offences, proof, investigation approval and prosecution sanction."
        ),
        (
            "The post-2018 Act creates a linked but stage-specific architecture. Section 7 targets the "
            "public servant who obtains, accepts or attempts to obtain an undue advantage in connection "
            "with improper or dishonest public-duty performance. Section 8 separately punishes the giver "
            "or promisor, while protecting a compelled payer who reports within seven days and informed "
            "conduct undertaken to assist an investigation. This partly answers the ARC's coercive-collusive "
            "concern, although those labels remain analytical rather than statutory.\n\n"
            "Corporate bribery is addressed by Section 9, which fines a commercial organisation for "
            "business-linked bribery by an associated person, subject to proof of adequate preventive "
            "procedures. Section 10 reaches directors and other officers only where consent or connivance "
            "is proved. Section 13 now covers entrusted-property misappropriation and intentional illicit "
            "enrichment; deletion of the abuse-of-position head improves certainty but may reduce reach "
            "against favouritism without direct enrichment.\n\n"
            "Proof and permission are also differentiated. Section 20 creates a rebuttable presumption in "
            "Section 7 or 11 trials after acceptance, obtaining or attempted obtaining is proved. Section "
            "17A requires previous approval before specified investigation of official-duty decisions, with "
            "a three-plus-one-month timeline and spot-arrest exception. Section 19 governs sanction before "
            "court cognizance for Sections 7, 10, 11, 13 and 15. Neither timeline should be converted into "
            "invented deemed approval.\n\n"
            "The architecture is defensible only if safeguards protect bona fide decisions without becoming "
            "delay devices. Effective law therefore requires prompt reasoned permissions, professional "
            "evidence gathering, genuine corporate compliance, whistleblower safety and separate but "
            "coordinated criminal, disciplinary and recovery processes."
        ),
    ),
    _original(
        20,
        (
            "A company's agent pays an official to approve non-compliant goods; senior managers knew "
            "of the plan, and the official's assets later appear disproportionate. Identify the legal "
            "routes and safeguards without presuming guilt."
        ),
        (
            "The first task is evidence preservation, not immediate attribution. Investigators should secure "
            "the approval file, specifications, inspection records, payment trail, communications, agency "
            "contract, corporate controls and the official's lawful income records. The non-compliance and "
            "commercial benefit support inquiry, but neither proves every offence.\n\n"
            "The official's receipt may engage Section 7 if an undue advantage and the required connection "
            "to improper or dishonest public-duty performance are proved. The agent may face Section 8 for "
            "giving or promising the advantage. A claim of compulsion requires genuine compulsion and "
            "reporting within seven days; voluntary purchase of an unlawful approval is characteristically "
            "collusive in ARC analysis. The company may be fined under Section 9 if the agent was associated "
            "with it and acted to obtain or retain business or a business advantage. It may prove adequate "
            "preventive procedures, but a symbolic policy is insufficient. Managers incur Section 10 "
            "liability only if consent or connivance is proved.\n\n"
            "Disproportionate assets may support Section 13's intentional-illicit-enrichment head where the "
            "public servant cannot satisfactorily account for them. Section 20's rebuttable presumption arises "
            "only in its specified trial setting after foundational acceptance or obtaining is proved. Section "
            "17A must be examined if the proposed investigation is relatable to an official-duty decision; "
            "the spot-arrest exception may matter. Section 19 sanction is separately required before court "
            "cognizance for listed offences.\n\n"
            "Corporate, criminal, disciplinary, contractual and recovery processes should remain distinct. "
            "Fair hearing, authenticated evidence and reasoned decisions protect innocent actors while allowing "
            "proportionate punishment, contract remedy and public-loss recovery when liability is established."
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
        "1. Anti-corruption legal evolution",
        "chronology-rail",
        (
            "IPC bribery provisions",
            "Prevention of Corruption Act 1947",
            "Criminal Law Amendment 1952",
            "Santhanam-linked 1964 reform",
            "PC Act 1988 consolidation",
            "Benami Act 1988 support layer",
            "Benami Amendment effective 2016",
            "PC Amendment effective 26 July 2018",
        ),
        "India's framework evolved through offence, procedure, asset and disclosure layers.",
        "Use to introduce chronology without treating every reform as linear expansion.",
    ),
    _panel(
        "2. ARC coercive-collusive branch",
        "two-path-classification",
        (
            "Start with giver's practical choice",
            "Threat for entitlement signals coercion",
            "Citizen is unwilling victim",
            "Protect report and restore service",
            "Shared unlawful benefit signals collusion",
            "Giver and taker both participate",
            "Public or state bears the loss",
            "Labels remain ARC analysis, not Act text",
        ),
        "Classification changes blame, evidence and remedy, but not statutory wording.",
        "Use before applying Sections 7 and 8.",
    ),
    _panel(
        "3. Sections 7 and 8 transaction map",
        "paired-offence-map",
        (
            "Section 7 begins with public servant",
            "Obtain accept or attempt",
            "Undue advantage is central",
            "Improper or dishonest duty link",
            "Section 8 begins with giver",
            "Give or promise with corrupt intent",
            "Compulsion plus seven-day report",
            "Informed investigative assistance protected",
        ),
        "The law addresses both sides but preserves two narrowly defined giver protections.",
        "Use for bribery fact patterns and close-option questions.",
    ),
    _panel(
        "4. Sections 9 and 10 corporate map",
        "organisation-liability-stack",
        (
            "Associated person supplies the conduct",
            "Undue advantage is given or promised",
            "Business retention or advantage intended",
            "Section 9 exposes organisation to fine",
            "Adequate procedures form a defence",
            "Evidence must test real implementation",
            "Consent or connivance links management",
            "Section 10 creates personal officer liability",
        ),
        "Organisation liability and officer liability have different statutory connectors.",
        "Use to avoid automatic vicarious-liability claims.",
    ),
    _panel(
        "5. Section 13 narrowing",
        "before-after-replacement",
        (
            "Pre-2018 abuse-of-position head existed",
            "2018 removed that broad route",
            "Current head one: entrusted property",
            "Dishonest or fraudulent diversion",
            "Allowing another to convert also covered",
            "Current head two: illicit enrichment",
            "Disproportionate assets require accounting",
            "Ethical abuse may survive outside Section 13",
        ),
        "Current criminal misconduct is narrower than general ethical misuse of office.",
        "Use for provision precision and balanced reform analysis.",
    ),
    _panel(
        "6. Section 17A investigation gate",
        "approval-gate",
        (
            "Identify PC Act allegation",
            "Identify serving or former public servant",
            "Link to official recommendation or decision",
            "Previous approval ordinarily required",
            "Appropriate authority must decide",
            "Three months is prescribed",
            "One recorded month may extend",
            "Spot acceptance arrest bypasses approval",
        ),
        "Section 17A is decision-linked and stage-specific, not rank-based immunity.",
        "Use for honest-decision protection versus delay debates.",
    ),
    _panel(
        "7. Section 19 cognizance gate",
        "sanction-gate",
        (
            "Investigation produces prosecutable material",
            "Court cognizance is the statutory stage",
            "Accused offence must be in listed set",
            "Sections 7 10 11 13 15 are listed",
            "Competent government or authority sanctions",
            "Three-month endeavour disciplines decision",
            "Legal consultation permits one more month",
            "No invented automatic sanction on expiry",
        ),
        "Investigation approval and prosecution sanction must never be collapsed.",
        "Use to compare Sections 17A and 19.",
    ),
    _panel(
        "8. Section 20 proof ladder",
        "evidence-presumption-ladder",
        (
            "Trial must concern Section 7 or 11",
            "Acceptance obtaining or attempt is proved",
            "Foundational proof precedes presumption",
            "Court presumes statutory corrupt purpose",
            "Section 11 consideration issue also covered",
            "Accused may prove the contrary",
            "Presumption is therefore rebuttable",
            "It is not guilt for every PC Act charge",
        ),
        "Burden shifting follows foundational proof and remains offence-specific.",
        "Use for Prelims traps and evidence analysis.",
    ),
    _panel(
        "9. Parallel accountability tracks",
        "four-track-system",
        (
            "Vigilance screening identifies angle",
            "Departmental process tests service breach",
            "Criminal process tests statutory offence",
            "Civil recovery restores proven loss",
            "Benami route targets concealed property",
            "Different standards of proof operate",
            "Acquittal does not mechanically erase misconduct",
            "Every adverse finding still requires due process",
        ),
        "One fact pattern may support several non-identical legal processes.",
        "Use to prevent audit, discipline and conviction from being conflated.",
    ),
    _panel(
        "10. Benami recovery and recall",
        "status-timeline",
        (
            "Original 1988 confiscation lacked rules",
            "ARC recorded eighteen-year inoperation",
            "2016 amendment rebuilt machinery",
            "New regime began 1 November 2016",
            "2022 judgment restricted retrospective reach",
            "2024 Court found no live validity contest",
            "Entire 2022 judgment was recalled",
            "Appeal restored and merits remain open",
        ),
        "Recall removes settled reliance on 2022 without deciding the opposite result.",
        "Use as the current legal-status anchor.",
    ),
    _panel(
        "11. Whistleblower protection gap",
        "protection-gap-chain",
        (
            "Evidence-based disclosure begins process",
            "Identity confidentiality reduces retaliation",
            "PIDPI Resolution dates to 21 April 2004",
            "2014 Act received assent 9 May",
            "Section 1(3) required notification",
            "No commencement notification has issued",
            "2015 Amendment Bill later lapsed",
            "Comprehensive statutory gap therefore persists",
        ),
        "Enactment and assent do not equal commencement or operation.",
        "Use for direct whistleblower and reform questions.",
    ),
    _panel(
        "12. Examiner-ready legal answer spine",
        "provision-answer-spine",
        (
            "Classify ethical transaction carefully",
            "Name exact section and legal actor",
            "State ingredients rather than conclusion",
            "Identify investigation or trial stage",
            "Add exception timeline or defence",
            "Separate statute from ARC proposal",
            "State current uncertainty honestly",
            "Conclude with balanced enforceable reform",
        ),
        "Provision plus stage plus qualification is the core of legal precision.",
        "Use to structure 10, 15 and 20-mark answers.",
    ),
)


CURRENT_ANCHOR = {
    "title": "Current official anchors: unresolved Section 17A issues and the Ganpati Dealcom recall",
    "verified_facts": (
        "In Centre for Public Interest Litigation v. Union of India, 2026 INSC 55, dated 13 January 2026, the Supreme Court delivered separate opinions on the challenge to Section 17A of the Prevention of Corruption Act.",
        "The operative order records that the opinions were divergent and directs the Registry to place the matter before the Chief Justice of India for constitution of an appropriate Bench to consider the issues afresh.",
        "Accordingly, neither separate opinion is encoded as a final binding resolution of Section 17A's constitutional validity; the position must be reverified after the appropriate Bench acts.",
        "In Union of India v. Ganpati Dealcom Pvt Ltd, 2024 INSC 799, dated 18 October 2024, the Supreme Court allowed the review petition, recalled the judgment dated 23 August 2022, and restored Civil Appeal No. 5783 of 2022 to file for fresh adjudication.",
        "The recall means that the 2022 holdings on the unamended Benami provisions and retrospective application cannot be cited as the current settled merits position; it does not itself establish the opposite merits result.",
    ),
    "administrative_link": (
        "The two anchors show why anti-corruption answers must separate enacted text from unsettled "
        "constitutional adjudication. Section 17A raises the institutional balance between fearless "
        "official decision-making and independent investigation, while the Benami recall affects the "
        "certainty of asset-recovery doctrine. A sound answer states the statutory rule, identifies "
        "the pending judicial issue and refuses to convert a split or recall order into settled merits."
    ),
    "limit": (
        "The 2026 Section 17A document contains divergent opinions followed by a referral order; it "
        "must not be presented as a final judgment either upholding or invalidating the provision. "
        "The 2024 Ganpati Dealcom order is a recall and restoration order, not a fresh merits holding "
        "that the 2016 Benami regime either does or does not apply retrospectively. Both positions are "
        "deliberately tagged as open and require later official re-verification."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://api.sci.gov.in/supremecourt/2018/40618/40618_2018_4_1501_67544_Judgement_13-Jan-2026.pdf",
    "https://api.sci.gov.in/supremecourt/2022/34619/34619_2022_1_301_56563_Judgement_18-Oct-2024.pdf",
)


SOURCE_CAVEAT = (
    "Topic 19 owns the legal architecture of corruption control: the Prevention of Corruption "
    "Act, 1988 as amended in 2018; Sections 7, 8, 9, 10, 13, 17A, 19 and 20; the omission and "
    "historical limit of Section 24; the supporting Benami and whistleblower-law layers; and the "
    "Second ARC's legal-reform analysis. The expressions coercive bribery and collusive bribery "
    "are ARC analytical categories, not express classifications in the PC Act. Section 8's word "
    "compelled and its seven-day reporting condition partly reflect the victim-beneficiary "
    "distinction but do not enact the ARC's complete proposed collusive-bribery offence. Section "
    "10 personal liability requires proved consent or connivance; it is not automatic liability "
    "for every person in management. Current Section 13 is confined to entrusted-property "
    "misappropriation or conversion and intentional illicit enrichment; the former broad "
    "abuse-of-position head was deleted. Section 17A approval operates before specified enquiry, "
    "inquiry or investigation of an official-duty recommendation or decision, while Section 19 "
    "sanction operates before court cognizance for Sections 7, 10, 11, 13 and 15. Their timelines "
    "do not create a stated deemed approval or sanction. In Centre for Public Interest Litigation, "
    "2026 INSC 55, the two opinions on Section 17A diverged and the operative order referred the "
    "issues to the Chief Justice of India for an appropriate Bench; neither opinion is presented "
    "here as the Court's final binding resolution. Section 20 is a rebuttable presumption "
    "after foundational proof in a Section 7 or 11 trial, not an irrebuttable presumption for "
    "every PC Act offence. Before omission, Section 24 supplied only a proceedings-linked "
    "protection from Section 12 prosecution, not blanket giver immunity. The Whistle Blowers "
    "Protection Act, 2014 remains uncommenced on the latest official verification; PIDPI is an "
    "interim administrative mechanism, not equivalent statutory commencement. The Supreme "
    "Court recalled Ganpati Dealcom's 2022 judgment on 18 October 2024 and restored the appeal; "
    "retrospective application is therefore presented as open, not decided either way. ARC "
    "recommendations concerning a distinct collusive-bribery offence and expanded coverage of "
    "specified public-utility providers or substantially government-funded NGOs are proposals, "
    "not enacted-law claims. Detailed GFR, procurement and public-fund operations remain Topic "
    "18-owned. Detailed CVC, CBI and Lokpal jurisdiction remains Topic 20-owned. Vigilance "
    "administration, sanction policy and honest-official safeguards remain Topic 21-owned. Full "
    "case-study option analysis and action sequencing remain Topic 22-owned. Topic 19 may route "
    "those dimensions only far enough to state the governing legal provision, evidentiary limit "
    "or current statutory gap."
)


REGISTER_SUPPLEMENT = (
    "### CORRUPTION LEGAL FRAMEWORK RAPID REGISTER\n\n"
    "#### 1. VISUAL FOUNDATION — EVOLUTION AND LEGAL MAP\n\n"
    "- Evolution: IPC bribery provisions -> Prevention of Corruption Act, 1947 -> "
    "Criminal Law (Amendment) Act, 1952 -> Santhanam-linked 1964 changes -> "
    "Prevention of Corruption Act, 1988 -> Prevention of Corruption (Amendment) Act, 2018.\n"
    "- The 1988 Act consolidated the earlier central anti-bribery framework, broadened the "
    "public-servant concept and provided trial by Special Judges.\n"
    "- The 2018 Amendment came into force on 26 July 2018 and changed both liability and "
    "safeguards: revised Section 7, standalone giver liability in Section 8, commercial-"
    "organisation liability in Sections 9-10, narrowed Section 13, new Section 17A and "
    "omission of Section 24.\n"
    "- The post-2018 framework is double-edged: it strengthens giver and corporate liability "
    "while narrowing criminal misconduct and adding an approval gate before specified "
    "decision-linked investigation.\n"
    "- Operational chain: allegation -> ingredient and jurisdiction check -> Section 17A gate "
    "where applicable -> evidence-led investigation -> Section 19 sanction where applicable "
    "-> cognizance and Special Judge trial -> proof, consequence and recovery.\n"
    "- Keep four tracks distinct: vigilance screening, departmental proceedings, criminal "
    "prosecution and civil/confiscatory recovery can arise from the same facts but use "
    "different powers, standards and outcomes.\n\n"
    "#### 2. ESSENTIAL DEFINITIONS — COERCIVE, COLLUSIVE AND UNDUE ADVANTAGE\n\n"
    "- **Coercive bribery:** ARC analysis for an unwilling citizen compelled to pay for an "
    "entitlement or to avoid harassment, delay or loss.\n"
    "- **Collusive bribery:** ARC analysis for a giver and taker who both benefit while the "
    "State, lawful competitors, citizens or public interest bears the loss.\n"
    "- Use coercive and collusive only as ARC analytical categories: the Prevention of "
    "Corruption Act does not itself use those labels.\n"
    "- Section 8 instead uses the statutory word **compelled** and attaches a seven-day "
    "reporting condition; this partly reflects, but does not enact in full, the ARC taxonomy.\n"
    "- **Undue advantage** means an advantage other than legal remuneration that the public "
    "servant is not legally entitled to receive; do not reduce it to cash alone.\n"
    "- **Non-performance of duty** may be an ethical corruption failure when wilful omission, "
    "gross negligence or concealment produces improper benefit or public harm, but the PC Act "
    "contains no general offence named non-performance of duty.\n"
    "- Bad outcome, error, delay or a defensible policy choice is not by itself proof of corrupt "
    "intent, undue advantage or criminal misconduct.\n\n"
    "#### 3. MECHANISM I — SECTIONS 7, 8, 9 AND 10\n\n"
    "- **Section 7:** addresses a public servant who obtains, accepts or attempts to obtain an "
    "undue advantage with the required link to improper or dishonest performance of public "
    "duty, or as a reward for such performance. Benefit to another person or an unpopular "
    "decision alone does not prove its ingredients.\n"
    "- **Section 8:** separately punishes giving or promising an undue advantage to induce "
    "improper performance of public duty or reward such performance; giver liability is no "
    "longer confined to abetment of the public servant's offence.\n"
    "- A person compelled to give receives Section 8 protection only if the matter is reported "
    "to a law-enforcement authority or investigating agency within seven days from giving it.\n"
    "- Section 8 also preserves authorised investigative assistance where the person informs "
    "the law-enforcement or investigating agency and acts under its direction; a private "
    "after-the-fact claim of cooperation is not enough.\n"
    "- **Section 9:** a commercial organisation may be fined where an associated person gives "
    "or promises an undue advantage to a public servant intending to obtain or retain business "
    "or an advantage in business. The organisation may prove that adequate procedures designed "
    "to prevent such conduct were in place.\n"
    "- **Section 10:** personal liability of a director, manager, secretary or other officer "
    "requires proof that the Section 9 offence occurred with that person's consent or "
    "connivance; position in management alone is insufficient.\n"
    "- Answer route for a company case: public servant -> Section 7; giver/agent -> Section 8; "
    "organisation -> Section 9; consenting or conniving officer -> Section 10, each subject to "
    "its own evidence and defence.\n\n"
    "#### 4. MECHANISM II — SECTION 13 AND THE 2018 NARROWING\n\n"
    "- Current Section 13 criminal misconduct has two heads, not the former broad catalogue.\n"
    "- First head: dishonest or fraudulent misappropriation or conversion for personal use of "
    "property entrusted to or under the public servant's control, or knowingly allowing another "
    "person to do so.\n"
    "- Second head: intentional illicit enrichment during the period of office.\n"
    "- The explanation permits intentional illicit enrichment to be presumed where the public "
    "servant or a person on the public servant's behalf possesses pecuniary resources or "
    "property disproportionate to known sources of income that cannot be satisfactorily "
    "accounted for.\n"
    "- The former Section 13(1)(d) abuse-of-position route was deleted in 2018. Never cite "
    "favouritism, arbitrary benefit or abuse of office alone as the present Section 13 offence.\n"
    "- Analytical trade-off: narrowing improves certainty and protects bona fide discretion, "
    "but may leave some non-enrichment abuse-of-authority conduct to other criminal, "
    "disciplinary, administrative or recovery routes.\n"
    "- ARC's broader acts-of-commission and acts-of-omission diagnosis remains an ethical and "
    "reform lens; it must not be silently converted into current penal text.\n\n"
    "#### 5. MECHANISM III — SECTIONS 17A, 19, 20, 24 AND TRIAL\n\n"
    "- **Section 17A:** previous approval is required before a police officer conducts an "
    "enquiry, inquiry or investigation into an alleged PC Act offence relatable to a "
    "recommendation made or decision taken by a serving or former public servant in discharge "
    "of official functions or duties.\n"
    "- Section 17A is decision-linked, not rank-based. Approval is unnecessary for arrest on "
    "the spot on a charge of accepting or attempting to accept an undue advantage.\n"
    "- Its authority must convey a decision within three months, extendable by one further "
    "month for reasons recorded in writing; expiry does not create a stated deemed approval.\n"
    "- **Section 19:** operates at the later court-cognizance stage. Previous sanction applies "
    "to offences under Sections 7, 10, 11, 13 and 15 where the statutory public-servant and "
    "competent-authority conditions are met.\n"
    "- The Section 19 authority should endeavour to decide within three months, extendable by "
    "one month where legal consultation is required; this also is not a deemed-sanction rule.\n"
    "- Memorise the distinction: Section 17A controls specified investigation; Section 19 "
    "controls cognizance. Neither is a judicial finding of innocence or guilt.\n"
    "- **Section 20:** in a trial punishable under Section 7 or Section 11, foundational proof "
    "of obtaining, accepting or attempting to obtain the relevant undue advantage can trigger "
    "a rebuttable, offence-specific presumption. It is not universal, automatic or irrebuttable.\n"
    "- **Former Section 24:** a giver's statement in proceedings against a public servant could "
    "not subject that giver to Section 12 prosecution. It was proceedings-linked protection, "
    "never blanket immunity, and was omitted in 2018.\n"
    "- Section 4 trial precision: Special Judges conduct PC Act trials; day-to-day trial is "
    "required as far as practicable, with an endeavour to finish within two years, reasoned "
    "six-month extensions and a total period not ordinarily exceeding four years.\n\n"
    "#### 6. INDIAN APPLICATIONS AND SUPPORTING LEGAL LAYERS\n\n"
    "- Entitlement extortion: protect the coerced payer, preserve the demand evidence, restore "
    "the service and observe Section 8's reporting condition rather than treating payer and "
    "official as morally identical.\n"
    "- Procurement kickback: where a contractor and official cooperate to accept non-compliant "
    "goods, test both sides of the exchange, commercial-organisation responsibility, managerial "
    "consent or connivance, public loss and recovery without presuming any ingredient.\n"
    "- Mining or regulatory nexus: trace permits, decisions, money, company benefit, threats "
    "and official omissions; distinguish coerced residents or witnesses from collusive "
    "beneficiaries.\n"
    "- The Prohibition of Benami Property Transactions Act, 1988, substantially reworked in "
    "2016 and operational from 1 November 2016, supplies a complementary asset-identification, "
    "adjudication and confiscation layer; it is not a substitute for proving a PC Act offence.\n"
    "- The Whistle Blowers Protection Act, 2014 received assent but remains uncommenced on the "
    "latest verified official position. PIDPI remains an interim administrative route for "
    "covered central matters, not statutory commencement of the 2014 Act.\n"
    "- Satyendra Dubey and Manjunath Shanmugam illustrate why detection architecture is hollow "
    "without confidentiality, threat assessment, anti-retaliation protection and accountable "
    "follow-up.\n"
    "- ARC proposals for False Claims-type recovery, a distinct collusive-bribery offence and "
    "expanded coverage of specified public utilities or substantially government-funded NGOs "
    "are reform proposals, not enacted PC Act provisions.\n\n"
    "#### 7. MUST-KNOW CURRENT ANCHORS AND PRELIMS FACTS\n\n"
    "- **Centre for Public Interest Litigation v. Union of India, 2026 INSC 55, 13 January "
    "2026:** the separate opinions on Section 17A diverged. The operative order directed the "
    "Registry to place the matter before the Chief Justice of India for an appropriate Bench "
    "to consider the issues afresh.\n"
    "- Do not present either Section 17A opinion as the Supreme Court's final binding resolution "
    "upholding or invalidating the provision; later official developments require verification.\n"
    "- **Union of India v. Ganpati Dealcom Pvt Ltd, 2024 INSC 799, 18 October 2024:** review was "
    "allowed, the 23 August 2022 judgment was recalled and Civil Appeal No. 5783 of 2022 was "
    "restored for fresh adjudication.\n"
    "- The recall removes the 2022 judgment as the settled merits answer; it does not establish "
    "the opposite conclusion on retrospectivity or constitutional validity.\n"
    "- 2018 quick set: revised Section 7; new Section 8; new Sections 9-10; narrowed Section 13; "
    "new Section 17A; omitted Section 24.\n"
    "- Seven-day number belongs to a compelled giver's Section 8 reporting condition. Three "
    "months plus one month belongs, with different wording and conditions, to Sections 17A and "
    "19. Two years and ordinarily four years belong to Section 4 trial management.\n"
    "- Source discipline: use the two official Supreme Court PDFs in CURRENT_SOURCE_URLS for "
    "the live judicial anchors, and state order, date and procedural effect exactly.\n\n"
    "#### 8. UPSC TRAPS AND CLOSE-OPTION CORRECTIONS\n\n"
    "- **Trap:** coercive and collusive bribery are statutory offences by those names. "
    "**Correction:** they are ARC analytical categories; current liability follows the words "
    "and ingredients of Sections 7-10 and other applicable provisions.\n"
    "- **Trap:** every bribe-giver is immune if later willing to testify. **Correction:** former "
    "Section 24 was limited and is omitted; current Section 8 contains narrower compelled-payer "
    "and authorised-investigative-assistance protections.\n"
    "- **Trap:** Section 10 automatically punishes every senior manager. **Correction:** consent "
    "or connivance in the Section 9 offence must be proved.\n"
    "- **Trap:** current Section 13 still criminalises every abuse of official position. "
    "**Correction:** the former broad head was deleted; apply the two surviving heads exactly.\n"
    "- **Trap:** Section 17A approval and Section 19 sanction are interchangeable. "
    "**Correction:** investigation gate versus cognizance gate.\n"
    "- **Trap:** Section 20 reverses the burden for every corruption allegation. **Correction:** "
    "it is rebuttable, trial-stage, foundational-proof-dependent and confined to its specified "
    "Section 7 or 11 setting.\n"
    "- **Trap:** lapse of a three-month period automatically grants approval or sanction. "
    "**Correction:** neither cited provision states that result.\n"
    "- **Trap:** the 2026 Section 17A case finally settled constitutionality. **Correction:** "
    "divergent opinions led to referral through the CJI for fresh consideration.\n"
    "- **Trap:** the Ganpati recall proves retrospective application. **Correction:** recall and "
    "restoration reopen adjudication; they do not decide the opposite merits position.\n"
    "- **Trap:** enactment equals commencement. **Correction:** the Whistle Blowers Protection "
    "Act, 2014 remains uncommenced on the verified official position.\n\n"
    "#### 9. PYQ ROUTES AND PRACTICE QUESTIONS\n\n"
    "- **2018 Snowden:** legality versus conscience; test seriousness, verification, necessity, "
    "proportionality, channel integrity and avoidable harm, while stating India's protection gap.\n"
    "- **2019 non-performance:** qualified agreement; separate wilful omission as an ethical "
    "failure from the ingredients required for a PC Act crime.\n"
    "- **2019 institutional measures:** legal-risk mapping, exact provision training, reasoned "
    "decisions, protected reporting, evidence preservation and stage-separated accountability.\n"
    "- **2021 sand mining:** classify collusive beneficiaries and coerced witnesses, then route "
    "Sections 7-10, possible Section 13, Section 17A and recovery without declaring guilt.\n"
    "- **2022 whistleblower:** confidentiality, threat protection, independent time-bound inquiry, "
    "anti-retaliation remedy and the uncommenced-Act/PIDPI distinction.\n"
    "- **2022 mining journalist:** refuse inducement, authenticate and secure evidence, protect "
    "sources, disclose proportionately and route the corruption network lawfully.\n"
    "- **2023 core values:** combine moral formation with opportunity reduction, genuine corporate "
    "procedures, fair enforcement and protection for resistance and reporting.\n"
    "- **2023 coercion versus undue influence:** do not confuse workplace concepts, Section 8's "
    "word compelled and ARC's coercive-collusive classification.\n"
    "- **2023 public-sector executive:** allegation is not guilt; preserve chain of custody, test "
    "video and records, disclose conflicts and route the exact statutory ingredients.\n"
    "- **2024 groundwater case:** test alleged industrial-official collusion through permissions, "
    "benefits, evidence and due process while protecting legitimate public service and ecology.\n"
    "- Original-practice routes: 10-mark answers should master Section 17A versus Section 19 and "
    "Section 8 versus ARC; 15-mark answers should assess the 2018 strengthening/narrowing and "
    "supporting-law gaps; 20-mark answers should integrate offences, proof, gates, companies, "
    "assets and safeguards.\n\n"
    "#### 10. MAINS ANGLES, PROBABLE QUESTIONS AND REFORM BALANCE\n\n"
    "- Central evaluation: the 2018 Amendment is neither wholly enforcement-friendly nor wholly "
    "protective; identify what it strengthened, narrowed and procedurally gated.\n"
    "- Coercive-bribery reform: safe reporting, restored entitlement and realistic protection for "
    "fearful or low-capacity complainants, while preventing fabricated after-the-fact coercion.\n"
    "- Collusive-bribery reform: pursue both beneficiaries, trace public loss and corporate gain, "
    "and label ARC's distinct-offence/presumption proposal as a recommendation.\n"
    "- Honest-official balance: specific allegation, competent approval, recorded reasons, time "
    "discipline and review should protect bona fide judgment without insulating corrupt bargains.\n"
    "- Corporate reform: adequate procedures must be operational controls, training, due "
    "diligence, reporting and enforcement, not a paper policy drafted after detection.\n"
    "- Whistleblower reform: commence or suitably update a balanced statutory regime with "
    "confidentiality, interim protection, independent review, anti-retaliation sanctions and "
    "carefully bounded security exclusions.\n"
    "- Asset-recovery answer: combine lawful confiscation with notice, adjudication and appeal; "
    "never convert the open Ganpati question into certainty in either direction.\n"
    "- Probable-question set: evaluate narrowed Section 13; compare Sections 17A and 19; assess "
    "Section 8 against ARC analysis; explain Sections 9-10; examine current supporting-law gaps; "
    "design a balanced post-2018 anti-corruption framework.\n\n"
    "#### 11. STUDY LINKS AND OWNERSHIP BOUNDARIES\n\n"
    "- **Topic 18 owns:** GFR rules, procurement lifecycle, fund utilisation, audit operations, "
    "four-E assessment and detailed public-loss controls. Topic 19 only identifies the legal "
    "corruption or recovery route arising from those facts.\n"
    "- **Topic 20 owns:** detailed CVC, CBI, Lokpal, Lokayukta and State ACB composition, powers, "
    "jurisdiction and institutional coordination. Topic 19 names an authority only as needed to "
    "explain a legal gate or reporting route.\n"
    "- **Topic 21 owns:** vigilance-angle classification, sanction administration, bona fide "
    "decision safeguards, malicious-complaint controls and full honest-official protection design.\n"
    "- **Topic 22 owns:** complete case-study stakeholder mapping, option generation, sequencing "
    "and final action plan. Topic 19 contributes statutory issue spotting, proof limits and legal "
    "status only.\n"
    "- **Topic 16 owns:** codes, conduct-rule architecture and the detailed devotion-to-duty basis.\n"
    "- **Topic 23 owns:** full named-case treatment of Satyendra Dubey, Manjunath Shanmugam and "
    "other comparative cases.\n"
    "- Boundary rule: provision-level precision belongs here; operational procurement, agency "
    "jurisdiction, vigilance procedure and case-method depth must be routed to their owning topic.\n\n"
    "#### 12. ANSWER-WRITING SPINE — PROVISION, PROOF, GATE, BALANCE\n\n"
    "1. **Classify:** coercive, collusive, corporate, entrusted-property, illicit-enrichment, "
    "whistleblowing or asset-recovery problem.\n"
    "2. **State the legal status:** enacted provision, omitted provision, uncommenced statute, "
    "ARC proposal or unsettled judicial issue.\n"
    "3. **Name the provision:** use Sections 7, 8, 9, 10, 13, 17A, 19 or 20 only where facts fit.\n"
    "4. **List ingredients:** conduct, intent, relationship to public duty, consent or connivance, "
    "entrustment, enrichment or foundational proof as applicable.\n"
    "5. **Separate stages:** allegation is not proof; approval is not sanction; sanction is not "
    "conviction; audit or vigilance material is not a judicial verdict.\n"
    "6. **Add the safeguard:** compelled-payer protection, adequate-procedures defence, spot-arrest "
    "exception, competent authority, hearing, reasons, rebuttal or appeal.\n"
    "7. **Use the current anchor precisely:** divergent Section 17A opinions and referral; Ganpati "
    "recall and restoration; no invented final merits rule.\n"
    "8. **Evaluate the trade-off:** enforcement reach versus bona fide discretion, complainant "
    "safety versus false claims, recovery versus due process, and speed versus fair adjudication.\n"
    "9. **Recommend specifically:** safe reporting, genuine corporate controls, time-bound reasoned "
    "gates, evidence integrity, proportionate liability and system repair.\n"
    "10. **Conclude:** law earns legitimacy when it distinguishes victims, beneficiaries, honest "
    "decision-makers and culpable actors through precise proof and fair process.\n\n"
    "> **Final thesis:** India's corruption-control law should be read as a calibrated chain of "
    "offences, evidentiary rules, investigation and cognizance gates, corporate responsibility, "
    "asset-recovery support and protected disclosure. Its credibility depends on exact statutory "
    "classification, independent evidence, timely reasoned safeguards and proportionate remedy: "
    "protect the coerced citizen and honest official, pursue the collusive beneficiary and corrupt "
    "public servant, and never present an ARC proposal, an omitted provision, an uncommenced Act, "
    "a divergent opinion or a recalled judgment as settled current law."
)
