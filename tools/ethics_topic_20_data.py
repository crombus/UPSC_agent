"""Learner-v2 source data: Ethics Topic 20, Anti-Corruption Institutions."""


SESSION_TITLES = (
    "Institutional map: why India uses multiple anti-corruption bodies",
    "CVC, CBI, Lokpal and Lokayukta: precise roles and boundaries",
    "Jurisdiction and coordination: from authorised complaint to competent forum",
    "Institutional evolution: Santhanam, Vineet Narain, ARC and the enacted Lokpal",
    "Prelims-ready design facts without role inflation",
    "Close-option traps: advice, inquiry, investigation, prosecution and adjudication",
    "PYQ application: accountability, probity, federalism and institutional reform",
    "Mains analysis: independence, coherence, legitimacy and due process",
    "Probable questions and institution-specific answer routes",
    "Study boundaries, reform synthesis and examiner-ready architecture",
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
        "Anti-corruption architecture is stage-separated",
        (
            "Complaint receipt, preliminary inquiry, evidence-gathering investigation, prosecution "
            "before a competent court and adjudication are distinct functions; institutional "
            "coordination must connect them without allowing one preliminary finding to become guilt."
        ),
        (
            "A department treats an audit alert as conclusive guilt and dismisses an officer without "
            "hearing. Which institutional-design principle has been collapsed?"
        ),
        (
            "A credible complaint is screened, investigated by the competent agency, prosecuted through "
            "lawful process and decided by a court. Which architecture is being respected?"
        ),
        "stage separation",
    ),
    _mcq(
        "Multiplicity can create overlap without coherence",
        (
            "The Second Administrative Reforms Commission identified overlapping Union and State "
            "anti-corruption bodies as a coherence problem; adding a watchdog helps only when referrals, "
            "records, responsibility and follow-up are clearly allocated."
        ),
        (
            "A Minister-official collusion complaint is repeatedly transferred among bodies until "
            "limitation and evidence risks grow. Which structural diagnosis best explains the failure?"
        ),
        (
            "A referral protocol names the lead body, evidence custodian, reporting deadline and next "
            "forum. Which response to institutional multiplicity is illustrated?"
        ),
        "stage separation",
    ),
    _mcq(
        "Independence and accountability must coexist",
        (
            "An anti-corruption body needs protected appointments, tenure, resources and decisional space, "
            "but independence is not absence of reasons, legislative reporting, judicial review, financial "
            "scrutiny or fair procedure."
        ),
        (
            "A watchdog rejects all external review as interference and issues unexplained adverse findings. "
            "Which misconception about independence is present?"
        ),
        (
            "An agency has operational autonomy while publishing aggregate results, recording reasons and "
            "remaining subject to courts and audit. Which balanced principle is shown?"
        ),
        "stage separation",
    ),
    _mcq(
        "Institutional design must protect public trust and due process",
        (
            "Credible enforcement requires timely action and insulation from influence, while specificity, "
            "confidentiality, hearing, evidence standards and reasoned decisions protect reputation, honest "
            "administration and the legitimacy of eventual sanctions."
        ),
        (
            "A complaint naming no transaction is publicised before verification, causing irreversible "
            "reputational harm. Which legitimacy safeguard was neglected?"
        ),
        (
            "A body preserves evidence confidentially, defines allegations and gives the affected person a "
            "lawful opportunity to respond. Which institutional ethic is applied?"
        ),
        "stage separation",
    ),
    _mcq(
        "CVC is advisory and superintending, not a trial court",
        (
            "The Central Vigilance Commission advises on vigilance administration and exercises statutory "
            "superintendence over the Delhi Special Police Establishment for specified corruption "
            "investigations; it does not itself convict or impose a criminal sentence."
        ),
        (
            "A ministry states that CVC advice itself proves criminal guilt. Which role boundary corrects "
            "this claim?"
        ),
        (
            "The Commission reviews vigilance handling while a competent court determines guilt after "
            "prosecution. Which institutional distinction is maintained?"
        ),
        "CVC precision",
    ),
    _mcq(
        "CVC superintendence over CBI is subject-matter limited",
        (
            "CVC superintendence concerns the Delhi Special Police Establishment's investigation of offences "
            "under the Prevention of Corruption Act and connected trial offences; it is not general command "
            "over every CBI investigation."
        ),
        (
            "A candidate says the CVC directs all CBI work, including every unrelated special-crime case. "
            "Which statutory limitation has been missed?"
        ),
        (
            "The Commission reviews progress in a corruption investigation but does not demand a predetermined "
            "outcome in a particular case. Which boundary is respected?"
        ),
        "CVC precision",
    ),
    _mcq(
        "CVC advice does not replace the disciplinary authority",
        (
            "Vigilance advice informs the competent government's or organisation's decision, but the lawful "
            "disciplinary authority must independently apply service rules, evidence, hearing requirements "
            "and reasons before imposing a penalty."
        ),
        (
            "A public enterprise mechanically punishes an employee because a vigilance opinion was received, "
            "without conducting the required proceeding. What has it displaced?"
        ),
        (
            "The disciplinary authority considers vigilance advice, records its own findings and follows the "
            "applicable procedure. Which allocation of responsibility is correct?"
        ),
        "CVC precision",
    ),
    _mcq(
        "A departmental CVO is the internal vigilance node",
        (
            "A Chief Vigilance Officer coordinates preventive vigilance, examines complaints and suspected "
            "vigilance matters, supports disciplinary routing and interfaces with the CVC; the CVO is not an "
            "independent criminal court or a substitute for investigators."
        ),
        (
            "A ministry asks its CVO to pronounce a criminal sentence after checking a procurement complaint. "
            "Which role inflation is involved?"
        ),
        (
            "A CVO secures records, examines the vigilance angle and refers suspected criminality through the "
            "competent channel. Which departmental function is illustrated?"
        ),
        "CVC precision",
    ),
    _mcq(
        "CBI draws police powers from the DSPE Act",
        (
            "The Central Bureau of Investigation was created by executive resolution, while its police powers "
            "for investigation derive from the Delhi Special Police Establishment Act; the institutional name "
            "and statutory source should not be conflated."
        ),
        (
            "An answer describes the CBI itself as a body created directly by the DSPE Act. Which precision "
            "correction is required?"
        ),
        (
            "An investigator identifies the DSPE Act as the source of police powers while separately noting "
            "the CBI's executive creation. Which distinction is correct?"
        ),
        "CBI federalism",
    ),
    _mcq(
        "State consent ordinarily controls DSPE extension",
        (
            "The Union may extend Delhi Special Police Establishment jurisdiction to a State, but ordinary "
            "exercise of those police powers within that State requires its consent, whether general or "
            "case-specific, under the federal statutory arrangement."
        ),
        (
            "The Union executive directs a fresh CBI police investigation wholly within a State that has not "
            "consented. Which federal requirement arises?"
        ),
        (
            "A State grants case-specific consent after withdrawing general consent. What lawful route enables "
            "the CBI to exercise DSPE powers there?"
        ),
        "CBI federalism",
    ),
    _mcq(
        "Constitutional courts form the consent caveat",
        (
            "State consent is not an absolute bar because the Supreme Court under Article 32 and High Courts "
            "under Article 226 may direct a CBI investigation to enforce fundamental rights and constitutional "
            "justice, using that exceptional power cautiously."
        ),
        (
            "A State argues that withdrawal of general consent prevents even a High Court from ordering a CBI "
            "probe. Which constitutional caveat answers the claim?"
        ),
        (
            "A High Court orders an exceptional CBI investigation after recording constitutional reasons. Why "
            "is ordinary executive consent analysis not decisive?"
        ),
        "CBI federalism",
    ),
    _mcq(
        "CBI investigation is not adjudication",
        (
            "CBI may register and investigate cases within lawful jurisdiction and its prosecutors may conduct "
            "cases before competent courts, but charges and agency conclusions remain allegations until the "
            "court adjudicates responsibility."
        ),
        (
            "A press release calls an accused person guilty immediately after a charge sheet. Which "
            "investigation-adjudication distinction is violated?"
        ),
        (
            "An agency presents tested evidence through prosecution while the court independently determines "
            "guilt. Which separation preserves legitimacy?"
        ),
        "CBI federalism",
    ),
    _mcq(
        "ARC's Lok Pal proposal and the enacted Lokpal differ",
        (
            "The Second Administrative Reforms Commission proposed a three-member Lok Pal for Ministers and "
            "Members of Parliament with the CVC ex officio, whereas the 2013 law enacted a broader and "
            "differently composed institution."
        ),
        (
            "A candidate attributes the enacted Chairperson-plus-eight-member structure directly to the ARC's "
            "three-member proposal. Which historical distinction is missing?"
        ),
        (
            "An answer first states the 2007 recommendation and then separately explains the 2013 enacted "
            "design. Which source discipline is demonstrated?"
        ),
        "Lokpal design",
    ),
    _mcq(
        "Enacted Lokpal combines judicial membership and representation",
        (
            "The Lokpal consists of a Chairperson and not more than eight Members; at least half the Members "
            "must be judicial, and at least half must come from the specified social categories, minorities "
            "and women."
        ),
        (
            "An option says every Lokpal Member must be a judge. Which composition rule makes it incorrect?"
        ),
        (
            "A selection process must respect both the judicial-member floor and the statutory representation "
            "requirement. Which enacted design feature is involved?"
        ),
        "Lokpal design",
    ),
    _mcq(
        "Lokpal jurisdiction is broad but legally bounded",
        (
            "The enacted Lokpal covers the Prime Minister subject to safeguards, Union Ministers, Members of "
            "Parliament, central officials and specified funded or foreign-contribution bodies, while preserving "
            "express exclusions and procedural conditions."
        ),
        (
            "A statement claims Lokpal jurisdiction extends without qualification to every person and every "
            "public controversy in India. Which correction is required?"
        ),
        (
            "A complaint is first tested against the office, subject matter, funding category and statutory "
            "conditions. Which jurisdictional discipline is being applied?"
        ),
        "Lokpal design",
    ),
    _mcq(
        "Lokpal may use inquiry and investigating agencies",
        (
            "Lokpal may order preliminary inquiry through its Inquiry Wing or another agency and may refer "
            "investigation to a competent agency, including CBI in appropriate cases; referral does not convert "
            "the ombudsman into the adjudicating court."
        ),
        (
            "A complaint is within Lokpal jurisdiction, so an answer says the Lokpal itself must perform every "
            "evidence-gathering and trial function. Which design feature disproves this?"
        ),
        (
            "Lokpal directs a referred investigation, reviews progress and later uses the lawful prosecution "
            "route. Which coordinated model is illustrated?"
        ),
        "Lokpal design",
    ),
    _mcq(
        "Prime Minister jurisdiction is qualified, not absent",
        (
            "The 2013 law includes the Prime Minister but excludes allegations relating to international "
            "relations, external or internal security, public order, atomic energy and space, and requires "
            "enhanced approval and confidentiality safeguards."
        ),
        (
            "An option says the Prime Minister is completely outside Lokpal jurisdiction. Which enacted "
            "compromise makes that option false?"
        ),
        (
            "A complaint concerning an unexcluded subject is considered by the full bench under the special "
            "threshold and in-camera process. Which qualified jurisdiction applies?"
        ),
        "high-office and states",
    ),
    _mcq(
        "ARC preferred Parliamentary scrutiny of a sitting Prime Minister",
        (
            "The ARC treated government continuity under the Westminster model as the reason to keep a sitting "
            "Prime Minister outside formal Lok Pal inquiry, relying on Parliamentary confidence rather than "
            "claiming personal immunity from accountability."
        ),
        (
            "A student says the ARC believed the Prime Minister should never be answerable. Which nuance corrects "
            "the interpretation?"
        ),
        (
            "An answer contrasts Parliamentary confidence accountability with the enacted qualified Lokpal "
            "route. Which institutional debate is accurately framed?"
        ),
        "high-office and states",
    ),
    _mcq(
        "Lokayukta design remains heterogeneous across States",
        (
            "The 2013 law required States to establish Lokayuktas within one year of commencement but did not "
            "prescribe one uniform national model; composition, jurisdiction, powers, appointment arrangements "
            "and practical independence therefore vary under State laws."
        ),
        (
            "An option assumes every State Lokayukta has the same composition and jurisdiction as Lokpal. Which "
            "federal fact defeats it?"
        ),
        (
            "A reform compares State laws before proposing common minimum safeguards. Which heterogeneity is it "
            "addressing?"
        ),
        "high-office and states",
    ),
    _mcq(
        "State ACB and Lokayukta roles are not nationally uniform",
        (
            "A State Anti-Corruption Bureau ordinarily performs police investigation within the State framework, "
            "while a Lokayukta performs the ombudsman role assigned by its State law; exact powers must be checked "
            "jurisdiction by jurisdiction."
        ),
        (
            "A candidate copies the central Lokpal-CBI relationship onto every State without examining State law. "
            "Which institutional mistake occurs?"
        ),
        (
            "A State complaint is routed after checking the relevant Lokayukta Act and ACB police competence. "
            "Which precision rule is followed?"
        ),
        "high-office and states",
    ),
    _mcq(
        "Minister-official collusion requires coordinated jurisdiction",
        (
            "A corruption allegation joining political direction and bureaucratic execution should not be split "
            "into isolated fragments; lawful Lokpal, CVC, departmental and investigating roles must exchange "
            "records through a clear lead-and-referral design."
        ),
        (
            "Separate bodies investigate the Minister and official without sharing the common transaction record. "
            "Which coordination failure follows?"
        ),
        (
            "One forum preserves the complete allegation and assigns institution-specific tasks with deadlines. "
            "Which organic-link principle is being applied?"
        ),
        "coordination reform",
    ),
    _mcq(
        "An overarching body does not erase specialist bodies",
        (
            "Lokpal's broad jurisdiction and power over referred matters complement rather than abolish CVC "
            "vigilance functions, CVO departmental work, CBI investigation, prosecution through competent officers "
            "and adjudication by courts."
        ),
        (
            "An answer claims the 2013 law made CVC, CVOs and CBI legally unnecessary. Which systems principle "
            "corrects it?"
        ),
        (
            "A reform keeps specialist capacity while establishing common referral and progress-review rules. "
            "Which institutional logic is shown?"
        ),
        "coordination reform",
    ),
    _mcq(
        "Performance cannot be inferred from legal existence",
        (
            "Enactment, appointment, creation of internal wings, receipt of complaints, completed inquiry, "
            "prosecution and final adjudication are different milestones; institutional evaluation must use "
            "verified stage-wise evidence rather than symbolic existence."
        ),
        (
            "A report calls an institution fully effective merely because its statute exists. Which evaluation "
            "error has occurred?"
        ),
        (
            "An assessment separately measures timeliness, referral quality, investigation, prosecution and final "
            "outcomes. Which performance discipline is used?"
        ),
        "coordination reform",
    ),
    _mcq(
        "Reform should improve coherence without creating a mega-agency",
        (
            "A sound reform clarifies jurisdiction, interoperable records, referral deadlines, independence and "
            "public reporting while preserving functional separation; concentrating complaint, investigation, "
            "prosecution and judgment in one body would create fresh arbitrariness."
        ),
        (
            "A proposal gives one watchdog exclusive power to investigate, prosecute and finally determine guilt. "
            "Which institutional risk does it create?"
        ),
        (
            "A protocol coordinates bodies but keeps courts and disciplinary authorities as independent decision "
            "forums. Which reform balance is achieved?"
        ),
        "coordination reform",
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
            'GS-IV Q2(b): "Non-performance of duty by a public servant is a form of '
            'corruption". Do you agree with this view? Justify your answer. (150 words)'
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 2. Topic 20 uses the institutional-routing "
            "dimension; detailed offence ingredients remain Topic 19-owned."
        ),
        (
            "I agree only when non-performance is a culpable misuse of entrusted office. An official who "
            "wilfully delays an entitlement to extract payment, suppresses a credible vigilance reference or "
            "protects a connected contractor can confer improper advantage through omission. The institutional "
            "response should begin by identifying the duty, authority, knowledge, motive, harm and records. A "
            "departmental CVO may examine whether a vigilance angle exists; suspected criminality can then reach "
            "the competent investigating agency, while the disciplinary authority and court retain their distinct "
            "decision roles.\n\n"
            "However, every failure is not corruption. Staff shortage, conflicting instructions, genuine legal "
            "uncertainty or a bona fide decision that later performs poorly may indicate capacity failure or "
            "negligence. Stigmatising these as corruption would deter initiative and undermine fair process.\n\n"
            "Thus non-performance becomes ethically corrupt when deliberate or recklessly indifferent omission "
            "uses public power for improper advantage or foreseeable public harm. Investigation must establish "
            "facts; legal liability depends on Topic 19's statutory ingredients, not on the slogan alone."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q5(a): What do you understand by probity in governance? Based on your "
            "understanding of the term, suggest measures for ensuring probity in government. "
            "(150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 3. Topic 14 owns the complete probity concept; "
            "Topic 20 supplies institution-specific enforcement and coordination."
        ),
        (
            "Probity is demonstrable rectitude in public power: legality, impartiality, integrity, transparency, "
            "reasoned discretion and answerability must be visible in decisions, not merely claimed as personal "
            "virtue. Institutions make probity credible. Departments need CVO-led preventive vigilance, conflict "
            "declarations, speaking records and safe complaint handling. The CVC should provide vigilance advice "
            "and exercise its specified superintendence without being described as a criminal court. CBI or State "
            "ACBs investigate within lawful jurisdiction; Lokpal or the relevant Lokayukta handles complaints within "
            "its enacted remit; courts adjudicate guilt.\n\n"
            "The ARC's multiplicity diagnosis shows why these bodies need referral protocols, common record "
            "preservation and time-bound follow-up. Independence must be matched by reasons, aggregate reporting, "
            "audit and judicial review. Technology can preserve trails but cannot decide motive or guilt.\n\n"
            "Probity therefore requires both ethical culture and stage-separated institutions. The best system "
            "makes wrongdoing difficult, detection credible, investigation competent and punishment lawful while "
            "protecting bona fide administration from allegation-based condemnation."
        ),
    ),
    _pyq(
        2019,
        (
            "GS-IV Q12: India seeks effective civil-service ethics, "
            "codes of conduct, transparency measures, ethics and integrity systems and "
            "anti-corruption agencies. Suggest institutional measures for anticipating threats, "
            "strengthening ethical competence and developing processes that promote integrity. "
            "(250 words)"
        ),
        20,
        (
            "Faithful condensed routing of the English demand verified against books\\"
            "more_previous_papers\\QP-CSM19-GeneralStudies-IV.pdf, page 7. The official paper "
            "contains the complete enumerated stem. Topic 20 owns anti-corruption institutional "
            "coherence; Topics 15-16 own codes and Topic 21 owns honest-official safeguards."
        ),
        (
            "The demand has three linked levels. First, anticipate threats through department-wise integrity-risk "
            "maps covering procurement, licensing, inspection, transfers and grants. CVOs should analyse complaint, "
            "audit and disciplinary patterns, while leadership reviews concentration of discretion and repeated "
            "control failures. This is preventive vigilance, not a presumption of guilt.\n\n"
            "Second, strengthen competence through scenario-based training on conflicts, written reasons, lawful "
            "directions, evidence preservation and institution choice. Officials should know that CVC advice, CBI "
            "investigation, Lokpal jurisdiction, disciplinary proceedings, prosecution and judicial adjudication "
            "are not interchangeable. Safe consultation and mentoring should precede crisis.\n\n"
            "Third, build a coherent process. Complaints need triage, confidentiality, acknowledgement, jurisdiction "
            "checks and time-bound referral. The CVC-CVO network should connect preventive and departmental vigilance; "
            "CBI or State ACBs should investigate within federal limits; Lokpal or Lokayukta should exercise enacted "
            "ombudsman powers; competent prosecutors and courts should complete the consequence chain. Shared case "
            "identifiers and record protocols can prevent duplication without creating a mega-agency.\n\n"
            "Independence requires secure tenure and resources, but also reasons, audit, legislative reporting and "
            "judicial review. The ARC's organic-link principle is useful: coordinate specialist institutions while "
            "preserving their autonomy. An integrity system succeeds when prevention, voice, competent investigation, "
            "fair adjudication and institutional learning reinforce one another."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-II Q11: The jurisdiction of the Central Bureau of Investigation (CBI) regarding "
            "lodging an FIR and conducting probe within a particular State is being questioned "
            "by various States. However, the power of the States to withhold consent to the CBI "
            "is not absolute. Explain with special reference to the federal character of India. "
            "(250 words)"
        ),
        15,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-II-110122.pdf, page 3. This GS-II overlap is Topic "
            "20's direct federal-jurisdiction PYQ; detailed offence law remains outside scope."
        ),
        (
            "CBI's police powers arise through the Delhi Special Police Establishment Act, 1946. The Union may "
            "extend DSPE jurisdiction to a State, but ordinary exercise of those powers there requires State "
            "consent. Consent may be general or case-specific; withdrawal of general consent therefore requires "
            "fresh jurisdictional care for new investigations. This protects police as a State responsibility and "
            "prevents routine Union displacement of the State machinery.\n\n"
            "The power is nevertheless not absolute. In State of West Bengal v. Committee for Protection of "
            "Democratic Rights (2010), the Supreme Court held that constitutional courts may order a CBI inquiry "
            "without State consent. The Supreme Court's Article 32 and High Courts' Article 226 powers protect "
            "fundamental rights and constitutional justice; ordinary legislation cannot disable them. Because such "
            "orders affect federal balance, courts should use the power sparingly and on recorded grounds.\n\n"
            "The correct synthesis is cooperative federalism, not institutional supremacy. The Union cannot treat "
            "CBI as a general national police force free of the DSPE consent structure, while a State cannot convert "
            "consent into immunity from constitutional review. Clear consent records, prompt intergovernmental "
            "requests, judicial restraint and independent investigation preserve both federal autonomy and credible "
            "accountability."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV Q6(a): An independent and empowered social audit mechanism is an absolute "
            "must in every sphere of public service, including judiciary, to ensure performance, "
            "accountability and ethical conduct. Elaborate. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3. Social audit is mainly Topic "
            "11/18 material; Topic 20 uses it as detection and referral, not adjudication."
        ),
        (
            "Social audit allows affected citizens to compare official records with lived delivery, exposing ghost "
            "beneficiaries, absent works, exclusion and local coercion. Its anti-corruption value is detection and "
            "voice: it can generate a documented complaint, preserve witness accounts and reveal patterns that a "
            "remote vigilance body may miss.\n\n"
            "Its institutional boundary is equally important. A social-audit finding is not a conviction. Suspected "
            "departmental misconduct should reach the competent authority or CVO; criminal evidence should go to the "
            "lawful State ACB, CBI or other investigating body; a matter within Lokpal or Lokayukta jurisdiction should "
            "be referred there. Prosecution and adjudication require their own safeguards.\n\n"
            "Independence needs access to usable records, facilitation separate from implementation, protection from "
            "retaliation, public hearings and action-taken reports. Application to the judiciary must respect decisional "
            "independence: administration and expenditure can be scrutinised, while merits of judgments follow appeal "
            "and review. Social audit strengthens the detection layer when it connects evidence to a competent, fair "
            "consequence chain."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q6(a): Whistle-blower, who reports corruption and illegal activities, "
            "wrongdoing and misconduct to the concerned authorities, runs the risk of being "
            "exposed to grave danger, physical harm and victimization by vested interests, "
            "accused persons and his team. What policy measures would you suggest to strengthen "
            "protection mechanism to safeguard the whistle-blower? (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 4. Topic 20 addresses "
            "authorised institutional channels; detailed whistleblower and honest-official "
            "protection belongs to Topics 19 and 21."
        ),
        (
            "Protection begins with a safe authorised channel, not merely a promise of secrecy. Complaints should "
            "receive secure intake, identity separation, restricted access, risk assessment, acknowledgement and "
            "time-bound jurisdictional routing. Central vigilance complaints within the PIDPI framework may reach "
            "the CVC; matters within Lokpal jurisdiction should follow its complaint process; suspected offences "
            "must reach the competent investigating agency. The recipient must not circulate identity casually "
            "among the accused chain.\n\n"
            "Policy should prohibit retaliation, permit interim transfer or security support where risk is credible, "
            "preserve service benefits, penalise retaliators and provide independent review when the employer is "
            "implicated. Digital systems need access logs and breach accountability. Anonymous allegations may offer "
            "leads, but confidentiality should not be confused with anonymity under a formal protection mechanism.\n\n"
            "Institutional separation protects both sides: a complaint triggers screening, not guilt; investigation "
            "tests evidence; prosecution and courts decide consequence. Detailed statutory status and safeguards "
            "belong to Topics 19 and 21. Topic 20's central lesson is that protection fails when the authorised channel "
            "cannot preserve identity, jurisdiction and follow-up."
        ),
    ),
    _pyq(
        2022,
        (
            "Neutral routing of GS-IV Q10: an investigative journalist uncovers a stone-mining "
            "mafia linked with corrupt police, civil officials and a politically connected media "
            "owner, but faces inducement and pressure to suppress the report. Evaluate options, "
            "dilemmas and the appropriate response. (250 words)"
        ),
        20,
        (
            "Neutral demand faithfully routed from books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 10. Topic 20 uses the "
            "multi-agency and State-institution dimension; Topic 22 owns full case-study method."
        ),
        (
            "The facts indicate networked corruption: illegal extraction, police protection, administrative "
            "facilitation, political influence and media ownership can disable ordinary complaint channels. The "
            "journalist should not accept the inducement or surrender the only evidence, but immediate sensational "
            "publication may expose sources and compromise investigation. He should authenticate records, preserve "
            "copies and chronology, obtain independent legal-editorial review and assess physical risk.\n\n"
            "Institutionally, the route depends on jurisdiction. State police vigilance or the State ACB ordinarily "
            "investigates corruption within the State framework; the State Lokayukta may have a role defined by its "
            "own law. If local machinery is demonstrably compromised, judicial remedies or another lawfully competent "
            "forum may be necessary. CBI entry cannot be assumed without DSPE consent, case-specific authority or a "
            "constitutional-court direction. Lokpal is not a universal forum for State political corruption.\n\n"
            "The response must also attack the network: secure witnesses, trace permits and money, review sensitive "
            "postings, reconcile transport and royalty data and separate investigation from political command. "
            "Publication, if used, should minimise unrelated personal data and protect sources. The case demonstrates "
            "why institutional independence, federal precision and multiple protected escalation routes are essential "
            "when the first-line agency is captured."
        ),
    ),
    _pyq(
        2023,
        (
            'GS-IV Q2(a): "Corruption is the manifestation of the failure of core values in '
            'the society." In your opinion, what measures can be adopted to uplift the core '
            "values in the society? (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 2. Values are Topic "
            "1/2-owned; Topic 20 supplies the institutional complement to moral formation."
        ),
        (
            "Corruption reflects weakened honesty, fairness and public spirit, but values operate within incentives "
            "and institutions. Families, schools and public leaders should model respect for common resources, reject "
            "admiration of illicit wealth and teach that public office is a trust. Civil-service training should use "
            "real dilemmas involving conflict, pressure, reporting and reasoned refusal.\n\n"
            "Moral education alone fails where wrongdoing is rewarded. CVO-led preventive vigilance, transparent "
            "criteria, CVC guidance, independent investigation, Lokpal or Lokayukta access within jurisdiction, "
            "protected complaints and fair courts make integrity practicable. The ARC's multiplicity diagnosis also "
            "requires coordinated referral, so citizens are not defeated by institutional buck-passing. Swift action "
            "must remain evidence-based; allegation-driven humiliation can itself corrode justice.\n\n"
            "The durable strategy joins character with credible consequence. Institutions without values may become "
            "formalistic or captured, while values without institutions leave honest persons exposed. Core values rise "
            "when ethical conduct is socially respected, administratively feasible and supported by a coherent system "
            "that detects, investigates, adjudicates and learns."
        ),
    ),
    _pyq(
        2023,
        (
            "GS-IV Q5(b): 'Probity is essential for an effective system of governance and "
            "socio-economic development.' Discuss. (150 words)"
        ),
        10,
        (
            "Exact English wording verified against books\\more_previous_papers\\"
            "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf, page 4. Topic 14 owns the "
            "general concept; Topic 20 supplies the anti-corruption institutional mechanism."
        ),
        (
            "Probity makes public decisions lawful, impartial, transparent and demonstrably directed to public "
            "purpose. It improves development because citizens and firms can rely on fair rules, scarce resources "
            "reach intended uses and honest officials are not displaced by patronage. Yet probity cannot depend only "
            "on personal virtue.\n\n"
            "Institutional support is stage-specific. Departmental CVOs reduce opportunity and examine vigilance "
            "concerns; the CVC advises and exercises specified superintendence; CBI or State ACBs investigate within "
            "lawful federal jurisdiction; Lokpal and State-specific Lokayuktas provide ombudsman routes; prosecutors "
            "present cases and courts adjudicate. Clear referrals and shared records address the ARC's warning about "
            "overlapping institutions. Reasons, hearing and review prevent vigilance from becoming arbitrary.\n\n"
            "Probity therefore produces both ethical legitimacy and economic reliability. However, the existence of "
            "watchdogs does not prove effectiveness: staffing, independence, timeliness, coordination and follow-up "
            "must be verified. Development is best served when prevention, investigation and lawful consequence coexist "
            "with protection for bona fide decisions."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Differentiate the roles of the CVC, CBI and Lokpal in India's anti-corruption "
            "architecture."
        ),
        (
            "The three institutions occupy connected but distinct positions. The CVC is a statutory vigilance "
            "body. It advises the Union system, exercises superintendence over DSPE corruption investigations "
            "within its specified remit and reviews vigilance administration; it does not adjudicate criminal "
            "guilt. The CBI is an investigating agency whose police powers derive from the DSPE Act. It gathers "
            "evidence within lawful territorial jurisdiction, while prosecution and the court complete later stages.\n\n"
            "Lokpal is the ombudsman created by the 2013 law for the Prime Minister subject to safeguards, Union "
            "Ministers, MPs, central officials and specified bodies. It may order preliminary inquiry and refer or "
            "direct investigation, including through CBI in appropriate cases. It complements rather than abolishes "
            "CVC and CBI.\n\n"
            "The ARC's organic-link principle explains the relationship: political and administrative aspects of one "
            "transaction need coordinated handling, but advice, inquiry, investigation, prosecution and adjudication "
            "must not collapse. Role precision protects both effectiveness and due process."
        ),
    ),
    _original(
        10,
        (
            "Why is State consent for CBI investigation important, and why is it not an "
            "absolute constitutional veto?"
        ),
        (
            "State consent reflects India's federal distribution of police responsibility. Under the DSPE Act, "
            "extension of Delhi Special Police Establishment powers to a State ordinarily requires that State's "
            "consent. General consent enables a category of cases; after its withdrawal, fresh investigations need "
            "case-specific authority unless another lawful basis exists. The Union executive therefore cannot treat "
            "CBI as a general national police force.\n\n"
            "Consent is not an absolute constitutional veto. In State of West Bengal v. Committee for Protection of "
            "Democratic Rights (2010), the Supreme Court held that the Supreme Court under Article 32 and High Courts "
            "under Article 226 may order a CBI investigation without State consent to enforce constitutional rights. "
            "That exceptional power should be used cautiously because routine use would weaken federal balance.\n\n"
            "The synthesis is cooperative federalism: respect statutory consent in ordinary administration, permit "
            "reasoned constitutional intervention where justice requires it, and preserve investigation from both "
            "Union and State political control."
        ),
    ),
    _original(
        15,
        (
            "Compare the Second ARC's 2007 Lok Pal proposal with the Lokpal enacted under "
            "the Lokpal and Lokayuktas Act, 2013."
        ),
        (
            "The ARC proposed a lean three-member Lok Pal: a serving or retired Supreme Court judge as Chair, an "
            "eminent jurist and the CVC ex officio. Its jurisdiction centred on Union Ministers and MPs. It excluded "
            "formal inquiry into a sitting Prime Minister, reasoning that Westminster government depends on the "
            "Prime Minister's Parliamentary confidence and that an inquiry could destabilise governance. It also "
            "envisaged an organic link in which CVC retained functional autonomy under the Lok Pal's overall guidance.\n\n"
            "The 2013 Act enacted a different institution: a Chairperson and not more than eight Members, with at "
            "least half judicial Members and a statutory representation requirement. Jurisdiction extends to the "
            "Prime Minister subject to subject-matter exclusions, full-bench consideration, a two-thirds threshold "
            "and confidentiality; it also covers Ministers, MPs, central officials and specified funded bodies. "
            "Inquiry, investigation and prosecution mechanisms are correspondingly broader.\n\n"
            "The difference reflects competing design values. ARC prioritised focus, judicial anchoring and continuity; "
            "the enacted model prioritised comprehensive coverage and representative legitimacy after later political "
            "mobilisation. Neither should be misquoted as the other. A strong answer treats the 2007 recommendation "
            "and 2013 law as related but separate historical facts."
        ),
    ),
    _original(
        15,
        (
            "Assess whether the Lokpal and Lokayuktas Act resolved the multiplicity and "
            "coherence problem identified by the Second ARC."
        ),
        (
            "The Act improved coherence by creating an overarching central ombudsman with jurisdiction over high "
            "political functionaries, central officials and specified bodies. Lokpal can order preliminary inquiry, "
            "refer investigation and exercise direction over agencies in referred matters. This reduces the risk that "
            "a Minister-official collusion allegation is divided between political and bureaucratic silos. The later "
            "constitution of dedicated Inquiry and Prosecution Wings strengthens the visible stage architecture.\n\n"
            "The ARC's problem is nevertheless only partly resolved. CVC, departmental CVOs, CBI, disciplinary "
            "authorities and courts retain distinct statutes and functions; coordination depends on practical referral, "
            "record-sharing and timelines. At State level, the central law required Lokayuktas but prescribed no "
            "uniform model. State Lokayukta and ACB powers therefore remain heterogeneous. More bodies can reproduce "
            "delay, forum shopping, evidence fragmentation or needless duplication if responsibility is unclear.\n\n"
            "Reform should establish common case identifiers, lead-agency rules, protected evidence exchange, reasoned "
            "referrals and stage-wise public reporting while preserving due process and specialist autonomy. The goal "
            "is not one mega-agency. Coherence means connected responsibility across inquiry, investigation, prosecution "
            "and adjudication, not institutional merger."
        ),
    ),
    _original(
        20,
        (
            "Design a coordinated anti-corruption process for a complaint alleging collusion "
            "between a Union Minister, senior officials and a private beneficiary."
        ),
        (
            "The complaint should enter through a secure channel with identity protection, transaction details and "
            "record-preservation instructions. Initial triage must test whether the allegation concerns corruption, "
            "which persons and bodies fall within Lokpal jurisdiction, whether departmental vigilance issues coexist "
            "and whether urgent steps are needed to prevent evidence loss. Publicity should not precede verification.\n\n"
            "Lokpal can preserve the complete collusion allegation rather than fragmenting the Minister and officials. "
            "It may order preliminary inquiry through its Inquiry Wing or another competent agency. The departmental "
            "CVO can secure internal files and identify control failures; CVC can perform its statutory vigilance and "
            "specified superintendence roles. If full investigation is ordered through CBI, lawful evidence gathering, "
            "financial and decision trails, witness protection and technical expertise should follow. No body should "
            "direct a predetermined finding.\n\n"
            "After investigation, prosecution must be handled through the legally competent route and adjudication "
            "left to the court. Departmental proceedings may address service responsibility under their own standard "
            "and safeguards without being confused with criminal conviction. Aggregate progress reporting should avoid "
            "prejudicing trial or exposing complainants.\n\n"
            "System repair should continue alongside individual accountability: disclose conflicts, redesign the "
            "licensing or procurement process, separate sensitive roles, review beneficial ownership and close the "
            "control gap. The ARC's organic-link principle supplies the design thesis—one transaction, coordinated "
            "institutions, preserved functional autonomy. Effectiveness comes from clear lead responsibility, deadlines "
            "and evidence exchange; legitimacy comes from confidentiality, hearing, reasons, review and independent "
            "adjudication."
        ),
    ),
    _original(
        20,
        (
            "Critically evaluate the qualified jurisdiction of Lokpal over the Prime Minister "
            "as an accountability-continuity compromise."
        ),
        (
            "The accountability case is strong: democratic office cannot become personal immunity, and excluding the "
            "highest executive office entirely could weaken equality before public standards. The 2013 Act therefore "
            "includes the Prime Minister. Yet it excludes allegations relating to international relations, external "
            "and internal security, public order, atomic energy and space. An inquiry requires full-bench consideration, "
            "approval by at least two-thirds of Members and in-camera proceedings; dismissal brings strict record "
            "confidentiality.\n\n"
            "These safeguards answer part of the ARC's continuity concern. The ARC had argued that a formal inquiry "
            "could damage the Parliamentary-confidence-based authority on which Westminster government rests, even if "
            "the allegation later fails. The enacted model substitutes a high threshold and protected process for the "
            "ARC's exclusion, balancing answerability with protection against frivolous destabilisation.\n\n"
            "The compromise remains imperfect. Subject-matter exclusions may shield mixed decisions where security and "
            "commercial considerations overlap. Conversely, even a confidential inquiry can create political paralysis "
            "if leaked. A high threshold may prevent harassment but can also make scrutiny unusually difficult. "
            "Parliamentary accountability, judicial review, electoral judgment and ordinary institutional checks "
            "therefore remain important.\n\n"
            "The defensible verdict is qualified inclusion rather than either absolute exemption or routine inquiry. "
            "Periodic review should examine whether complaints are filtered by reasons rather than political convenience, "
            "whether confidentiality works and whether excluded subjects are construed narrowly. Accountability should "
            "remain publicly credible without allowing accusation alone to destabilise constitutional government or "
            "institutional trust."
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
        "1. Anti-corruption institutional map",
        "role-map",
        (
            "CVO: departmental vigilance node",
            "CVC: advice and superintendence",
            "CBI: DSPE-based investigation",
            "Lokpal: central ombudsman jurisdiction",
            "Lokayukta: State-law ombudsman",
            "State ACB: State investigation",
            "Prosecutor: presents the case",
            "Court: adjudicates responsibility",
        ),
        "Institutional plurality works only when each role and hand-off is explicit.",
        "Use as the opening visual in any architecture answer.",
    ),
    _panel(
        "2. Complaint-to-adjudication chain",
        "stage-rail",
        (
            "Receive secure specific complaint",
            "Triage jurisdiction and urgency",
            "Conduct preliminary inquiry",
            "Order evidence-based investigation",
            "Decide competent prosecution route",
            "Present charges before court",
            "Adjudicate with hearing and proof",
            "Apply remedy and system learning",
        ),
        "A complaint initiates process; it never proves guilt.",
        "Use to separate inquiry, investigation, prosecution and adjudication.",
    ),
    _panel(
        "3. CVC role boundary",
        "mandate-stack",
        (
            "Statutory body under 2003 Act",
            "Origins in 1964 resolution",
            "Advises Union vigilance system",
            "Superintends specified DSPE work",
            "Reviews investigation progress",
            "Oversees vigilance administration",
            "Works through departmental CVOs",
            "Does not criminally convict",
        ),
        "CVC strengthens vigilance coherence without becoming investigator, prosecutor and court.",
        "Use for close-option role questions.",
    ),
    _panel(
        "4. CBI federal-jurisdiction route",
        "federal-gate",
        (
            "CBI created by executive resolution",
            "Police powers derive from DSPE Act",
            "Union extends DSPE jurisdiction",
            "State consent ordinarily required",
            "General or case-specific consent",
            "Constitutional courts may direct",
            "Exceptional power used cautiously",
            "Court still adjudicates final guilt",
        ),
        "State consent is the ordinary rule; constitutional-court direction is the caveat.",
        "Use for the 2021 GS-II CBI PYQ.",
    ),
    _panel(
        "5. Enacted Lokpal design",
        "institution-card",
        (
            "Chairperson plus up to eight Members",
            "At least half judicial Members",
            "Statutory representation requirement",
            "Covers Ministers and MPs",
            "Covers central officials A to D",
            "Qualified Prime Minister coverage",
            "Specified funded bodies included",
            "Inquiry and referral powers coexist",
        ),
        "The 2013 Lokpal is broader than the ARC's proposed three-member body.",
        "Use for composition and jurisdiction answers.",
    ),
    _panel(
        "6. ARC proposal versus enacted law",
        "comparison-bridge",
        (
            "ARC year: 2007 recommendation",
            "ARC body: three members",
            "ARC remit: Ministers and MPs",
            "ARC PM route: Parliament",
            "Act year: 2013 enactment",
            "Act body: Chair plus up to eight",
            "Act remit: broader central coverage",
            "Act PM route: qualified inclusion",
        ),
        "Recommendation and enactment are related developments, not identical designs.",
        "Use to avoid the most common historical trap.",
    ),
    _panel(
        "7. Prime Minister jurisdiction compromise",
        "threshold-funnel",
        (
            "Democratic answerability supports inclusion",
            "Continuity concern supports safeguards",
            "Five sensitive subjects excluded",
            "Full bench considers initiation",
            "Two-thirds approval is required",
            "Proceedings remain in camera",
            "Dismissed records stay confidential",
            "Parliamentary accountability also remains",
        ),
        "Qualified inclusion balances scrutiny with constitutional stability but resolves neither concern completely.",
        "Use for a balanced 15- or 20-mark evaluation.",
    ),
    _panel(
        "8. State-level institutional diversity",
        "federal-matrix",
        (
            "Central Act requires Lokayuktas",
            "No single model is prescribed",
            "State laws define composition",
            "State laws define jurisdiction",
            "State laws define investigative powers",
            "ACBs perform State police roles",
            "CVOs remain departmental nodes",
            "Common safeguards need local adaptation",
        ),
        "Never copy the central Lokpal-CBI model mechanically onto every State.",
        "Use for federalism and Lokayukta reform.",
    ),
    _panel(
        "9. Organic linkage for collusion cases",
        "coordination-web",
        (
            "Preserve one common transaction record",
            "Lokpal holds political-official allegation",
            "CVO secures departmental evidence",
            "CVC performs statutory vigilance role",
            "CBI gathers criminal evidence lawfully",
            "Prosecutor tests trial readiness",
            "Court determines criminal responsibility",
            "Departments repair enabling controls",
        ),
        "Coordination should connect specialist roles without merging them.",
        "Use for Minister-bureaucrat collusion analysis.",
    ),
    _panel(
        "10. Institutional quality test",
        "eight-test-grid",
        (
            "Jurisdiction is clear",
            "Appointments protect independence",
            "Resources match workload",
            "Referrals have deadlines",
            "Evidence exchange is secure",
            "Findings contain reasons",
            "Review preserves due process",
            "Outcomes feed system learning",
        ),
        "Legal existence is only the first milestone of institutional effectiveness.",
        "Use for reform and performance questions.",
    ),
    _panel(
        "11. Examiner trap board",
        "trap-correction",
        (
            "CVC advice is not conviction",
            "CBI name is not DSPE creation",
            "Consent rule has court caveat",
            "Lokpal does not replace CBI",
            "ARC proposal is not 2013 design",
            "PM coverage is qualified",
            "Lokayuktas are not uniform",
            "Inquiry finding is not adjudication",
        ),
        "Most marks are lost by inflating one institution into the whole system.",
        "Use for Prelims elimination and Mains precision.",
    ),
    _panel(
        "12. Examiner-ready answer spine",
        "answer-spine",
        (
            "Define the institutional problem",
            "Map each body's lawful role",
            "State the federal or jurisdiction gate",
            "Separate all accountability stages",
            "Use ARC and enacted-law contrast",
            "Add independence and due process",
            "Recommend coordination without merger",
            "Conclude with qualified coherence",
        ),
        "Precise role plus hand-off plus safeguard produces a high-quality institutional answer.",
        "Use to structure 10-, 15- and 20-mark responses.",
    ),
)


CURRENT_ANCHOR = {
    "title": "Current official anchor: complaint-process transparency at Lokpal",
    "verified_facts": (
        "Lokpal Circular No. 01/2026 dated 24 July 2026 expressly sets procedure for complaints, listing of matters, uploading of orders and jurisdiction under Section 14.",
        "Official Financial Year 2025-26 administrative data report: complaints received 558 (154 post/hand and 404 online); complaints registered 431; registered complaints disposed 407; preliminary inquiries 81; investigations 8; prosecution sanctions 0; disciplinary directions 2; pending 99.",
    ),
    "administrative_link": (
        "Complaint handling, cause-list visibility, publication of orders and consolidated reporting can "
        "improve procedural traceability and public accountability. The labelled counts make different "
        "administrative stages visible, but they do not collapse jurisdiction screening, preliminary "
        "inquiry, investigation, prosecution and judicial adjudication into one function. A complaint, "
        "listing, uploaded order or administrative count is not proof of guilt."
    ),
    "limit": (
        "These are official FY 2025-26 administrative categories, not a measure of corruption prevalence "
        "or institutional success. They must not be treated as a single complaint cohort, converted into "
        "stage-to-stage rates without the report's definitions, or used alone to infer disposal quality, "
        "investigation quality, deterrence, conviction performance or effectiveness."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://lokpal.gov.in/api/cms-file?path=%2Fuploads%2Fcms%2F6%2F129%2F1_Circular_No._01.2026.pdf",
    "https://lokpal.gov.in/assets/pdf/consolidated_2025-26.pdf",
)


SOURCE_CAVEAT = (
    "Topic 20 owns the ethics and jurisdiction architecture of CVC, CBI, Lokpal, State "
    "Lokayuktas, departmental CVOs and State Anti-Corruption Bureaus. The CVC is an advisory "
    "and superintending vigilance body within its statutory remit; CVC advice is not a criminal conviction, "
    "and the Commission is not a criminal court "
    "and its superintendence does not extend to every CBI subject. The CBI was created by "
    "executive resolution, while its police powers derive from the Delhi Special Police "
    "Establishment Act, 1946. State consent is the ordinary gate for exercising DSPE powers "
    "within a State, but withdrawal of general consent does not disable constitutional courts; "
    "Supreme Court Article 32 and High Court Article 226 directions are the "
    "constitutional-court caveat, not a general executive bypass. The ARC's 2007 three-member "
    "Lok Pal proposal must remain separate from the broader Lokpal enacted in 2013. The enacted "
    "Prime Minister jurisdiction is qualified by subject exclusions, full-bench consideration, "
    "a two-thirds threshold and confidentiality. State Lokayuktas are heterogeneous because the "
    "central law did not prescribe a uniform model; exact State Lokayukta and ACB powers require "
    "the relevant State law. Departmental CVOs perform preventive, complaint-examination and "
    "disciplinary-routing functions; they do not adjudicate criminal guilt. Inquiry, investigation, "
    "prosecution, departmental decision and judicial adjudication must be written as distinct "
    "stages. Topic 19 owns detailed corruption offences, ingredients, sanction and allied criminal "
    "law. Topic 18 owns detailed public-fund, procurement, audit and leakage controls. Topic 21 "
    "owns safeguards for honest officials, vigilance screening and anti-retaliation design. Topic "
    "22 owns complete case-study method. Official local UPSC PDFs control PYQ wording; condensed "
    "case entries are neutral routing and do not pretend to reproduce every printed fact. The "
    "official India Code PDFs of the DSPE Act, 1946 and the Lokpal and Lokayuktas Act, 2013 "
    "control statutory wording; institutional portal summaries cannot enlarge those enactments. "
    "The State-consent constitutional-court caveat follows the Constitution Bench judgment in "
    "State of West Bengal v. Committee for Protection of Democratic Rights, available through "
    "the Supreme Court's official judgment PDF; it is not a general Union-executive exception."
)


REGISTER_SUPPLEMENT = (
    "### ANTI-CORRUPTION INSTITUTIONS RAPID REGISTER\n\n"
    "#### 1. INSTITUTIONAL STARTING POINT\n\n"
    "- No single institution owns the whole anti-corruption chain.\n"
    "- Core sequence: secure complaint -> jurisdiction triage -> preliminary inquiry -> investigation -> prosecution -> adjudication -> remedy/system repair.\n"
    "- Complaint, audit flag or preliminary finding is not guilt.\n"
    "- ARC 4.2.5 diagnosed multiplicity, overlap and lack of unified focus at Union and State levels.\n"
    "- Reform requires lead responsibility, referral deadlines, secure common records and stage-wise follow-up, not automatic institutional merger.\n\n"
    "#### 2. CVC — PRECISE ROLE\n\n"
    "- Established by executive resolution in 1964 following the Santhanam Committee; statutory under the CVC Act, 2003.\n"
    "- Advises the Union system on vigilance and integrity administration.\n"
    "- Exercises statutory superintendence over DSPE investigation of PC Act offences and connected trial offences.\n"
    "- Reviews progress of covered investigations and vigilance matters.\n"
    "- Cannot require an investigating agency to decide a particular case in a predetermined manner.\n"
    "- Is not itself the criminal court, and vigilance advice does not replace the competent disciplinary authority's procedure and reasons.\n"
    "- *Vineet Narain v. Union of India* supplied the independence context for statutory strengthening.\n\n"
    "#### 3. CVO — DEPARTMENTAL NODE\n\n"
    "- Heads or coordinates vigilance work inside a ministry, department, public enterprise or organisation.\n"
    "- Preventive role: risk review, systems examination, complaint pattern and control improvement.\n"
    "- Reactive role: secure records, examine vigilance angle, support preliminary fact gathering and disciplinary routing.\n"
    "- Interfaces with CVC where the statutory/administrative framework requires it.\n"
    "- Does not become an independent police force, prosecutor or court.\n"
    "- Topic 21 owns detailed safeguards against malicious or overbroad vigilance action.\n\n"
    "#### 4. CBI AND THE DSPE ACT\n\n"
    "- CBI was created by executive resolution; DSPE Act, 1946 supplies its police powers.\n"
    "- The Anti-Corruption Division investigates corruption cases within lawful subject and territorial jurisdiction.\n"
    "- Investigation gathers and tests evidence; a charge sheet remains an accusation until adjudication.\n"
    "- Prosecutors may present the case, but the competent court determines criminal responsibility.\n"
    "- Do not say CBI is a constitutional body or that the DSPE Act itself created the institutional name CBI.\n\n"
    "#### 5. STATE CONSENT AND THE COURT CAVEAT\n\n"
    "- DSPE jurisdiction may be extended to a State, but ordinary exercise of police powers there requires State consent.\n"
    "- Consent may be general or case-specific; withdrawal of general consent changes the route for fresh cases.\n"
    "- Union executive convenience is not a substitute for statutory consent.\n"
    "- *State of West Bengal v. Committee for Protection of Democratic Rights* (2010): Supreme Court under Article 32 and High Courts under Article 226 may order CBI investigation without State consent.\n"
    "- Constitutional-court power is exceptional and should be used cautiously because federal balance remains important.\n"
    "- Best thesis: ordinary consent rule + exceptional constitutional remedy = cooperative federal accountability.\n\n"
    "#### 6. ARC'S 2007 LOK PAL PROPOSAL\n\n"
    "- Three members: serving/retired Supreme Court judge as Chair, eminent jurist and CVC ex officio.\n"
    "- Jurisdiction centred on Union Ministers and MPs.\n"
    "- ARC excluded formal inquiry into a sitting Prime Minister and relied on Parliamentary-confidence accountability.\n"
    "- Rationale was continuity of Westminster government, not personal moral immunity.\n"
    "- Proposed organic link: CVC under Lok Pal's overall guidance/superintendence while retaining functional autonomy.\n"
    "- Always label this as a 2007 recommendation, not the enacted institutional structure.\n\n"
    "#### 7. LOKPAL AS ENACTED IN 2013\n\n"
    "- Chairperson plus not more than eight Members.\n"
    "- At least 50% of Members judicial; at least 50% of Members from SC/ST/OBC, minorities and women.\n"
    "- Covers Union Ministers, MPs, Groups A-D central officials and specified financed/foreign-contribution bodies.\n"
    "- Parliament speech/vote protection and other statutory limits must not be ignored.\n"
    "- Can order preliminary inquiry and refer/direct investigation through competent agencies.\n"
    "- The Act came into force on 16 January 2014; the first Chairperson was appointed only in March 2019, illustrating the enactment-to-operation gap.\n"
    "- Lokpal Circular No. 01/2026 dated 24 July 2026 sets procedure for complaints, listing, uploading orders and Section 14 jurisdiction.\n"
    "- Official Financial Year 2025-26 administrative data: complaints received 558 (154 post/hand, 404 online); registered 431; registered complaints disposed 407; preliminary inquiries 81; investigations 8; prosecution sanctions 0; disciplinary directions 2; pending 99.\n"
    "- Preserve those category labels: the counts are neither a measure of corruption prevalence nor proof of institutional success, and they are not automatically one continuous cohort.\n"
    "- Lokpal complements CVC/CBI; it does not adjudicate criminal guilt.\n\n"
    "#### 8. PRIME MINISTER JURISDICTION\n\n"
    "- Enacted law includes the Prime Minister subject to special safeguards.\n"
    "- Excluded subjects: international relations, external security, internal security, public order, atomic energy and space.\n"
    "- Full bench considers initiation; at least two-thirds of Members must approve.\n"
    "- Proceedings are in camera; dismissed complaint records remain confidential under the special rule.\n"
    "- Contrast: ARC proposed Parliamentary scrutiny instead of formal Lok Pal inquiry.\n"
    "- Analytical tension: equality and answerability versus continuity and protection from frivolous destabilisation.\n\n"
    "#### 9. LOKAYUKTA AND STATE ACB\n\n"
    "- The 2013 central law required States to establish Lokayuktas within one year of commencement but did not prescribe one uniform model.\n"
    "- Composition, jurisdiction, powers, appointment design and independence vary under State laws.\n"
    "- State ACB ordinarily performs State police investigation of corruption matters under the applicable framework.\n"
    "- Never assume the central Lokpal-CBI relationship automatically applies to every State.\n"
    "- State reform should seek common minimum safeguards while respecting federal legislative design.\n\n"
    "#### 10. COORDINATION WITHOUT ROLE COLLAPSE\n\n"
    "- Minister-official-private beneficiary collusion should be preserved as one transaction narrative.\n"
    "- Lokpal: jurisdiction and overarching handling of covered persons.\n"
    "- CVO: departmental records and vigilance angle.\n"
    "- CVC: advice, vigilance administration and specified DSPE superintendence.\n"
    "- CBI/State ACB: evidence-gathering investigation within lawful remit.\n"
    "- Prosecutor: presents legally sustainable charges.\n"
    "- Court/disciplinary authority: determines responsibility under the applicable process.\n"
    "- Shared records and deadlines should connect the bodies; no preliminary actor should become final judge.\n\n"
    "#### 11. PYQ AND PRELIMS ROUTES\n\n"
    "- **2019 non-performance:** agree conditionally; route wilful omission through specific vigilance and evidence tests.\n"
    "- **2019 probity:** connect ethical rectitude with CVO-CVC-investigation-court architecture.\n"
    "- **2019 institutional measures:** risk mapping + competence + stage-separated enforcement.\n"
    "- **2021 GS-II CBI:** DSPE consent rule + *CPDR* constitutional-court caveat + federal balance.\n"
    "- **2021 social audit:** detection and citizen evidence, never conviction.\n"
    "- **2022 whistleblower:** secure authorised channel, jurisdiction, confidentiality and anti-retaliation cross-link.\n"
    "- **2022 mining mafia:** check State law, ACB/Lokayukta competence, capture and lawful escalation.\n"
    "- **2023 corruption values:** institutions make values practicable; values keep institutions legitimate.\n"
    "- Prelims traps: CVC does not control every CBI case; ARC proposal is not enacted Lokpal; PM is not wholly excluded; Lokayuktas are not uniform.\n\n"
    "#### 12. ANSWER-WRITING SPINE — ROLE, GATE, HAND-OFF\n\n"
    "1. **Problem:** identify overlap, capture, federal consent, high-office scrutiny or stage collapse.\n"
    "2. **Role map:** state exactly what CVO, CVC, CBI/ACB, Lokpal/Lokayukta, prosecutor and court do.\n"
    "3. **Gate:** add jurisdiction, State consent, subject exclusion or State-law variation.\n"
    "4. **Hand-off:** show complaint -> inquiry -> investigation -> prosecution -> adjudication.\n"
    "5. **Evidence:** use Santhanam/1964, *Vineet Narain*, ARC 4.2.5/4.3.3, 2013 Act and *CPDR* where relevant.\n"
    "6. **Balance:** combine independence with reasons, confidentiality, hearing, review and reporting.\n"
    "7. **Reform:** common identifiers, referral deadlines, secure evidence exchange and stage-wise metrics without a mega-agency.\n"
    "8. **Conclusion:** coherent institutions protect public trust only when specialist autonomy and lawful accountability reinforce each other.\n\n"
    "> **Final thesis:** India's anti-corruption architecture should be understood as a chain of "
    "specialised institutions, not a contest for one all-powerful watchdog. CVC advice and "
    "superintendence, CVO departmental vigilance, CBI or ACB investigation, Lokpal or Lokayukta "
    "ombudsman jurisdiction, competent prosecution and independent adjudication become effective "
    "only through precise jurisdiction, secure hand-offs, federal respect, due process and verified "
    "follow-up."
)
