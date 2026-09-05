"""Learner-v2 source data: Ethics Topic 17, Citizens' Charters, Work Culture and Service Delivery."""


SESSION_TITLES = (
    "Citizen-centric service: charter, culture and delivery as one ethical chain",
    "Designing a credible Citizens' Charter: services, standards, timelines and disclosure",
    "Consultation, ownership, monitoring and periodic review of charter commitments",
    "Charter, grievance redress and statutory service guarantee: keep the remedies distinct",
    "Sevottam and CPGRAMS: linking promise, complaint and delivery capability",
    "Work culture: leadership, professionalism, empathy and solution-oriented legality",
    "Process redesign and digital delivery: simplify before computerising",
    "Inclusion and last-mile access: assisted, accessible and multi-channel public service",
    "Metrics and ethical failure modes: resolution, quality, gaming and learning",
    "PYQ synthesis, reform architecture and complete answer-writing spine",
)


SESSION_GROUPS = (
    ("1", "2"),
    ("3", "4", "5", "6"),
    ("7", "8"),
    ("9",),
    ("10",),
    ("11", "12"),
    ("13", "14"),
    ("15", "16"),
    ("17", "18"),
    ("19", "20"),
)


def _mcq(label, statement, scenario_a, scenario_b, group):
    return {
        "label": label,
        "statement": statement,
        "scenario_a": scenario_a,
        "scenario_b": scenario_b,
        "group": group,
    }


MCQ_CONCEPTS = (
    _mcq(
        "A Citizens' Charter is a public service commitment",
        (
            "A Citizens' Charter states what services an organisation provides, the standards and "
            "timelines it commits to, relevant responsibilities and the route available when the "
            "commitment is not met; publication alone does not guarantee performance."
        ),
        (
            "A district office displays a mission slogan but identifies no service, standard, "
            "timeline or recourse. Why is the display not yet a credible charter?"
        ),
        (
            "A transport office publishes service-wise requirements, time standards, contact points "
            "and escalation routes. Which administrative instrument is being operationalised?"
        ),
        "charter architecture",
    ),
    _mcq(
        "The citizen is a rights-holder, not merely a customer",
        (
            "Citizen-centricity borrows useful ideas from customer service but remains constitutionally "
            "different: public authorities owe legality, equality, dignity and special attention to "
            "persons who cannot choose another provider or purchase faster treatment."
        ),
        (
            "A monopoly welfare office serves only applicants who can pay an agent and calls the rest "
            "unprofitable customers. Which public-service distinction has been ignored?"
        ),
        (
            "A service centre combines courteous assistance with equal eligibility rules and priority "
            "support for persons with disabilities. Which conception of citizenship is shown?"
        ),
        "charter architecture",
    ),
    _mcq(
        "A charter must identify the complete service journey",
        (
            "A useful charter specifies the service, eligibility, required documents, fee if any, "
            "submission channel, responsible contact, delivery standard, expected citizen conduct, "
            "grievance route and review date in accessible language."
        ),
        (
            "An office promises a certificate within ten days but hides required documents until the "
            "applicant reaches the counter. Which completeness defect remains?"
        ),
        (
            "A charter explains both departmental commitments and the accurate information applicants "
            "must provide. Why can reciprocal clarity improve delivery without shifting official duty?"
        ),
        "charter architecture",
    ),
    _mcq(
        "Fewer credible promises are better than decorative abundance",
        (
            "The Second ARC preferred a few promises that can be kept over a long list of impractical "
            "declarations, because specific and feasible obligations allow citizens and supervisors to "
            "recognise default and demand correction."
        ),
        (
            "A department lists fifty unmeasurable aspirations that exceed its lawful mandate and "
            "capacity. Which charter-design lesson should guide revision?"
        ),
        (
            "An office begins with five high-volume services, measures delivery and expands only after "
            "capability improves. Which credibility principle is illustrated?"
        ),
        "charter architecture",
    ),
    _mcq(
        "Standards must combine time, quality and fairness",
        (
            "A service standard should specify not only speed but also accuracy, completeness, lawful "
            "eligibility, accessibility and fair treatment; a bare time target can reward hurried "
            "disposal, wrongful rejection or transfer of unfinished work."
        ),
        (
            "Staff meet a two-day target by rejecting every incomplete pension claim without offering "
            "legally required assistance. Which metric-design error has occurred?"
        ),
        (
            "A certificate standard tracks timeliness, correction rate and unequal rejection patterns. "
            "Why is this stronger than a turnaround target alone?"
        ),
        "standards and accountability",
    ),
    _mcq(
        "A timeline needs a defined trigger and stop rule",
        (
            "A meaningful time limit states when counting begins, which verified event may pause it, "
            "who records that pause, how the citizen is informed and when counting resumes; otherwise "
            "offices can manipulate the clock."
        ),
        (
            "A portal resets the service clock whenever any internal desk forwards the application. "
            "Which time-standard design safeguard is missing?"
        ),
        (
            "The clock starts on receipt of a complete application and any lawful deficiency notice is "
            "time-stamped and communicated. Which accountability feature is present?"
        ),
        "standards and accountability",
    ),
    _mcq(
        "Named ownership prevents diffuse responsibility",
        (
            "A charter should identify the responsible service unit and accessible contact or "
            "designation, while internal workflow assigns decision, supervisory and escalation roles; "
            "otherwise every desk can blame another without owning the citizen's outcome."
        ),
        (
            "A pension request moves among five desks and each says another unit owns delay. Which "
            "accountability defect does named ownership repair?"
        ),
        (
            "A service manager receives breach alerts and must record corrective action. Which feature "
            "turns a published promise into managed responsibility?"
        ),
        "standards and accountability",
    ),
    _mcq(
        "Consultation and review keep standards citizen-relevant",
        (
            "Service users, frontline staff and affected groups should inform charter design and "
            "periodic review, because internal drafters may measure administrative convenience rather "
            "than the outcome citizens need or the barriers vulnerable users face."
        ),
        (
            "A hospital counts registration speed while patients mainly face inaccessible diagnostics "
            "and unclear referrals. Which design process could reveal the mismatch?"
        ),
        (
            "Frontline staff and disability groups test a revised application journey before adoption. "
            "Which charter-quality mechanism is being used?"
        ),
        "standards and accountability",
    ),
    _mcq(
        "A charter is not automatically a statutory right",
        (
            "An administrative Citizens' Charter ordinarily communicates organisational commitments but "
            "does not by itself create a legally enforceable entitlement, penalty or compensation; those "
            "consequences require an applicable law, rule or other competent instrument."
        ),
        (
            "A claimant argues that every sentence in an unsigned office poster is directly enforceable "
            "as a statutory right. Which distinction corrects the claim?"
        ),
        (
            "A notified service under a State law has a designated officer, time limit and appeal route. "
            "What gives the commitment a stronger legal status?"
        ),
        "remedy and service guarantee",
    ),
    _mcq(
        "Grievance redress addresses failure after or during delivery",
        (
            "A charter states the promised service and standard, whereas grievance redress registers, "
            "routes, investigates, responds to and escalates a complaint about delay, denial, conduct or "
            "poor delivery; neither instrument substitutes for the other."
        ),
        (
            "A ministry publishes a delivery standard but offers no way to contest breach. Which separate "
            "institutional function is absent?"
        ),
        (
            "A portal tracks a complaint but the underlying service has no published standard. Why does "
            "grievance machinery not become a charter?"
        ),
        "remedy and service guarantee",
    ),
    _mcq(
        "CPGRAMS is a grievance platform, not an all-purpose tribunal",
        (
            "CPGRAMS enables citizens to lodge service-delivery grievances, obtain a registration ID, "
            "track status, give feedback and use the available appeal route, but the concerned public "
            "authority remains responsible for substantive redress."
        ),
        (
            "A department closes a complaint with a generic reply and claims the portal itself has "
            "adjudicated the citizen's entitlement. Which institutional misconception arises?"
        ),
        (
            "A dissatisfied complainant records poor feedback and uses the enabled appeal facility. Which "
            "official CPGRAMS feature is being used?"
        ),
        "remedy and service guarantee",
    ),
    _mcq(
        "State service guarantees apply through their own notified design",
        (
            "State right-to-service or public-service-guarantee laws generally operate through notified "
            "services, designated officers, stipulated periods and statutory appeal or consequence "
            "routes; coverage and procedure must be checked in the particular State instrument."
        ),
        (
            "An answer imports one State's penalty, appeal levels and service list into every other State. "
            "Which federal and legal error is present?"
        ),
        (
            "An applicant first checks whether the requested certificate is a notified service under the "
            "applicable State law. Which statutory-scope discipline is shown?"
        ),
        "remedy and service guarantee",
    ),
    _mcq(
        "Sevottam joins promise, grievance and capability",
        (
            "Sevottam treats service quality as an integrated system of Citizens' Charter commitments, "
            "public grievance redress and service-delivery capability, showing why a well-worded promise "
            "fails when workflow, staff or infrastructure cannot keep it."
        ),
        (
            "A department rewrites its charter but leaves vacancies, broken records and unresolved "
            "complaints untouched. Which Sevottam insight exposes the incomplete reform?"
        ),
        (
            "An office aligns standards, complaint learning and process capability. Which quality model "
            "does this three-part design reflect?"
        ),
        "culture and capability",
    ),
    _mcq(
        "Work culture is the lived norm behind the formal promise",
        (
            "Work culture consists of repeated expectations, leadership signals, peer behaviour, routines "
            "and incentives that tell employees what is actually rewarded; it can sustain a charter or "
            "silently defeat it despite formal compliance."
        ),
        (
            "A charter requires courtesy, but supervisors praise staff who intimidate applicants to reduce "
            "footfall. Which organisational layer explains the contradiction?"
        ),
        (
            "Team leaders review citizen harm, reward accurate problem-solving and correct disrespect. "
            "Which route turns service values into daily practice?"
        ),
        "culture and capability",
    ),
    _mcq(
        "Professionalism combines competence, legality and service",
        (
            "Professionalism in public delivery requires role competence, reliable preparation, "
            "impartiality, timely communication, accurate records, respect and willingness to solve "
            "problems within law; neither technical skill nor politeness alone is sufficient."
        ),
        (
            "An officer is courteous but repeatedly gives legally wrong eligibility advice. Which element "
            "of professionalism is missing?"
        ),
        (
            "A clerk explains a curable defect, protects the queue and records the decision accurately. "
            "Which integrated professional ethic is shown?"
        ),
        "culture and capability",
    ),
    _mcq(
        "Empathy improves design without replacing rules",
        (
            "Administrative empathy identifies how procedures are experienced by elderly, disabled, "
            "remote, poor or distressed citizens and supports lawful assistance and redesign; it does not "
            "authorise favouritism, false records or waiver of mandatory safeguards."
        ),
        (
            "An official fabricates eligibility because an applicant's hardship evokes sympathy. Which "
            "boundary between empathy and legality was crossed?"
        ),
        (
            "A pension office offers seating, assisted forms and home verification where authorised. Which "
            "proper use of empathy is illustrated?"
        ),
        "culture and capability",
    ),
    _mcq(
        "Process redesign must precede or accompany digitisation",
        (
            "Digital delivery improves service only when unnecessary approvals, duplicate data, unclear "
            "responsibility and avoidable visits are removed or redesigned; computerising a fragmented "
            "process can make opacity faster rather than create citizen-centricity."
        ),
        (
            "An online licence still requires the applicant to visit every old counter with printed copies. "
            "Which reform sequence was neglected?"
        ),
        (
            "A department removes redundant approvals before building a tracked digital workflow. Which "
            "service-design principle is applied?"
        ),
        "process and inclusion",
    ),
    _mcq(
        "A single window requires integrated back-end responsibility",
        (
            "A single-window service is genuine only when the front interface coordinates the complete "
            "back-end journey, preserves ownership and prevents citizens from carrying files between "
            "departments; one counter over unchanged silos is merely a reception desk."
        ),
        (
            "A centre accepts applications but tells citizens to chase three departments separately. Why "
            "is it not a functional single window?"
        ),
        (
            "One service manager coordinates departmental checks and communicates one reasoned outcome. "
            "Which integration feature is present?"
        ),
        "process and inclusion",
    ),
    _mcq(
        "Digital-by-default must not become digital-only",
        (
            "Digital channels can widen convenience and traceability, but ethical delivery preserves "
            "assisted, offline or alternative access where connectivity, literacy, disability, language "
            "or authentication barriers would otherwise exclude eligible citizens."
        ),
        (
            "A remote widow loses pension access because biometric failure has no exception or assisted "
            "route. Which inclusion principle has failed?"
        ),
        (
            "A portal offers screen-reader support, local-language help and a staffed service centre. Which "
            "multi-channel ethic is shown?"
        ),
        "process and inclusion",
    ),
    _mcq(
        "Data minimisation and human review protect digital dignity",
        (
            "Citizen-centric digital delivery should collect only necessary data, secure it, explain "
            "decisions, correct errors and provide meaningful human review where automated matching or "
            "authentication can wrongly deny a service."
        ),
        (
            "A system rejects benefits after a name mismatch and offers neither reason nor correction. "
            "Which digital service safeguards are absent?"
        ),
        (
            "An applicant can inspect the mismatch, update evidence and obtain human reconsideration. Which "
            "ethical digital design is operating?"
        ),
        "process and inclusion",
    ),
    _mcq(
        "Measure outcomes and resolution, not disposal alone",
        (
            "Service metrics should track timeliness, accuracy, accessibility, first-contact resolution, "
            "repeat grievance, appeal outcome, citizen feedback and distribution across groups; disposal "
            "counts alone can reward premature closure or movement of backlog."
        ),
        (
            "A department improves its dashboard by closing complaints with copy-pasted replies. Which "
            "measurement failure does this reveal?"
        ),
        (
            "Managers study repeat grievances and appeal reversals to repair the upstream process. Which "
            "learning-oriented metric use is shown?"
        ),
        "metrics and failure modes",
    ),
    _mcq(
        "Targets require anti-gaming safeguards",
        (
            "Any target can be gamed by rejecting hard cases, pausing clocks, shifting queues or lowering "
            "quality, so performance review must combine quantitative indicators with sample audit, reasons, "
            "equity checks and citizen experience."
        ),
        (
            "A service centre meets its average time by delaying complex disability claims outside the "
            "measured queue. Which ethical failure mode is present?"
        ),
        (
            "An audit compares reported timeliness with case files, correction rates and group-wise access. "
            "Which anti-gaming control is being applied?"
        ),
        "metrics and failure modes",
    ),
    _mcq(
        "Feedback must produce a visible learning loop",
        (
            "Consultation and complaint data create accountability only when responsible managers analyse "
            "patterns, correct individual harm, redesign recurring failure, communicate action and revise "
            "standards; collection without response becomes participation theatre."
        ),
        (
            "An office conducts satisfaction surveys for publicity but never changes process or answers "
            "complainants. Which feedback failure has occurred?"
        ),
        (
            "Repeated certificate complaints lead to a simpler evidence rule and revised charter. Which "
            "continuous-improvement loop is demonstrated?"
        ),
        "metrics and failure modes",
    ),
    _mcq(
        "Responsiveness is reasoned action, not automatic agreement",
        (
            "Responsiveness requires timely listening, communication, lawful assistance and correction, "
            "but a public authority may still refuse an ineligible or harmful request through clear reasons, "
            "equal treatment and an available review route."
        ),
        (
            "An officer grants an unlawful permit merely to avoid a poor satisfaction score. Which false "
            "idea of responsiveness caused the error?"
        ),
        (
            "A claim is refused promptly with evidence, reasons and appeal information. Why can this still "
            "be citizen-centric service?"
        ),
        "metrics and failure modes",
    ),
)


MCQ_ITEMS = MCQ_CONCEPTS


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
            "GS-IV Q4(a): Explain the basic principles of citizens charter movement and "
            "bring out its importance. (150 words)"
        ),
        10,
        (
            "Exact isolated English question verified against books\\more_previous_papers\\"
            "QP-CSM19-GeneralStudies-IV.pdf, page 3. This is the direct charter PYQ."
        ),
        (
            "The Citizens' Charter movement seeks to reverse the traditional relationship in which the "
            "citizen appears as a supplicant before an opaque monopoly office. Its basic principles are "
            "published service commitments, clear standards and time limits, accessible information on "
            "requirements and fees, identified responsibility, courteous and fair treatment, grievance "
            "redress, consultation, monitoring and periodic improvement.\n\n"
            "Its importance lies in converting a general duty to serve into a visible standard against "
            "which performance can be questioned. The Second ARC observed that many charters became "
            "pious declarations because commitments were vague and remedies absent. It therefore preferred "
            "a few feasible promises and called for remedy, penalty or compensation on default. A pension "
            "charter, for example, should specify documents, a realistic processing standard, the responsible "
            "unit and escalation when delay occurs.\n\n"
            "Yet a charter is ordinarily an administrative commitment, not automatically a statutory right. "
            "It succeeds only when grievance machinery, capable staff, process redesign, citizen feedback "
            "and leadership make the published promise part of daily work culture."
        ),
    ),
    _pyq(
        2021,
        (
            "GS-IV, Section A: An independent and empowered social audit mechanism is an "
            "absolute must in every sphere of public service, including judiciary, to ensure "
            "performance, accountability and ethical conduct. Elaborate. (Answer in 150 words)"
        ),
        10,
        (
            "Faithful English text verified against books\\more_previous_papers\\"
            "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf, page 3. The extracted numbering is "
            "not relied upon. This is a broader accountability question, neutrally routed here "
            "for citizen feedback, performance monitoring and service-learning; detailed social "
            "audit law remains outside Topic 17."
        ),
        (
            "Public service is often delivered by institutions possessing monopoly, expertise and "
            "information advantages. An independent social audit can compare official claims with the "
            "experience and records of affected people, require explanation in public and reveal exclusion "
            "that routine internal reporting misses. Independence from the implementing hierarchy, access "
            "to relevant records, representative participation, protection from retaliation, reasoned "
            "follow-up and publication of corrective action are therefore essential.\n\n"
            "For service delivery, social feedback can test whether charter timelines conceal wrongful "
            "rejection, inaccessible offices or repeated grievance closure. However, the form must respect "
            "institutional boundaries. Judicial independence, confidentiality, privacy and pending matters "
            "cannot be displaced by an unstructured public forum; suitable performance, administrative and "
            "user-access dimensions can still face independent scrutiny.\n\n"
            "Social audit is thus not public accusation or a substitute for appeal and adjudication. It is "
            "a participatory evidence mechanism. Its ethical value is realised when verified findings produce "
            "individual remedy, assigned responsibility and redesign of recurring service failure."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q1(a): Wisdom lies in knowing what to reckon with and what to overlook. "
            "An officer being engrossed with the periphery, ignoring the core issues before him, "
            "is not rare in the bureaucracy. Do you agree that such preoccupation of an "
            "administrator leads to travesty of justice to the cause of effective service delivery "
            "and good governance? Critically evaluate. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English question verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 2. Directly routed for "
            "purpose-sensitive process and service delivery."
        ),
        (
            "I agree substantially. Bureaucratic procedure protects equality, evidence and public money, "
            "but peripheral compliance becomes unjust when it defeats the lawful purpose of the service. "
            "An office may celebrate acknowledgements issued within one day while pensions remain unpaid, "
            "or return an elderly applicant repeatedly for a curable spelling mismatch. Such behaviour "
            "shifts institutional cost to the least powerful and rewards file movement over outcomes.\n\n"
            "Wisdom requires separating mandatory safeguards from inherited friction. The officer should "
            "identify the citizen outcome, map the complete process, remove duplicate approvals, offer lawful "
            "assistance, record reasons and measure accuracy, inclusion and resolution along with speed. A "
            "Citizens' Charter should therefore state the real service standard, not an easy intermediate "
            "activity.\n\n"
            "However, 'substance over form' cannot authorise bypass of eligibility, safety, hearing or audit. "
            "The correct ethic is solution-oriented legality: preserve safeguards that protect rights and "
            "redesign procedures that merely transfer delay. Effective service delivery is neither mechanical "
            "literalism nor benevolent arbitrariness."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q1(b): Apart from intellectual competency and moral qualities, empathy "
            "and compassion are some of the other vital attributes that facilitate the civil "
            "servants to be more competent in tackling the crucial issues or taking critical "
            "decisions. Explain with suitable illustrations. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English question verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 2. Foundational-values "
            "ownership is broader; Topic 17 uses it for inclusive service encounters and design."
        ),
        (
            "Intellectual competence identifies legal options and technical consequences; moral qualities "
            "supply integrity and impartiality. Empathy adds knowledge of how a decision is experienced by "
            "another person, while compassion creates a disciplined motivation to reduce avoidable suffering. "
            "Together they improve both diagnosis and implementation.\n\n"
            "A technically correct online pension system may exclude an elderly claimant after biometric "
            "failure. An empathetic officer anticipates this barrier and provides an authorised assisted or "
            "alternative verification route. During disaster relief, compassion supports priority access for "
            "persons with disabilities, while objective criteria prevent favouritism. In a hospital, listening "
            "to a distressed family can improve communication without altering clinical triage dishonestly.\n\n"
            "These attributes require boundaries. Sympathy cannot justify false records, waiver of mandatory "
            "safety or unequal favour. Institutional empathy should therefore be translated into accessible "
            "forms, plain language, seating, home or mobile delivery where lawful, human review and reasoned "
            "grievance handling. Competence becomes public-service competence when accurate judgment is joined "
            "to dignity, accessibility and solution-oriented legality."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q2(a): The Rules and Regulations provided to all the civil servants are "
            "same, yet there is difference in the performance. Positive minded officers are "
            "able to interpret the Rules and Regulations in favour of the case and achieve "
            "success, whereas negative minded officers are unable to achieve goals by interpreting "
            "the same Rules and Regulations against the case. Discuss with illustrations. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Faithful English text verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 2. Shared with codes and "
            "attitude topics; routed here for work culture and facilitative service."
        ),
        (
            "Rules create predictability and equality, but administration still requires judgment about "
            "purpose, evidence, sequencing and curable defects. Performance differs because officers vary in "
            "competence, empathy, initiative, bias, fear and the informal culture surrounding discretion. A "
            "positive officer does not bend law for a preferred applicant; she finds the lawful route that "
            "best fulfils the authorised service.\n\n"
            "For example, a pension clerk may explain how to cure a minor documentation defect, use available "
            "records and preserve the claim date rather than issue a mechanical rejection. Conversely, a "
            "licensing officer cannot call favouritism or waiver of safety a positive interpretation. Written "
            "reasons and equal treatment remain necessary.\n\n"
            "Organisations should issue plain guidance, publish service standards, train staff through cases, "
            "provide advice, protect documented good-faith initiative and examine appeals for recurring "
            "literalism. Leadership must reward genuine resolution rather than mere disposal. Positive "
            "administration is therefore purposive legality reinforced by a citizen-centric work culture, not "
            "personal benevolence above rules."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q4(a): What do you understand by the term 'good governance'? How far "
            "recent initiatives in terms of e-Governance steps taken by the State have helped "
            "the beneficiaries? Discuss with suitable examples. (Answer in 150 words)"
        ),
        10,
        (
            "Exact English question verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 3. Primary governance "
            "scope is broader; Topic 17 neutrally routes the digital service-delivery dimension."
        ),
        (
            "Good governance is lawful, participatory, transparent, accountable, responsive, equitable and "
            "effective exercise of public authority. E-governance can advance these values by reducing visits, "
            "standardising workflows, time-stamping action, enabling status tracking and widening access to "
            "services. An integrated portal for certificates or pensions can reduce queues and make delay "
            "visible; digital records can support consistent decisions and grievance review.\n\n"
            "Yet technology is an instrument, not evidence of good governance by itself. A portal laid over "
            "duplicate approvals merely digitises delay. Connectivity, language, disability, authentication "
            "failure, poor data and cyber or privacy risks can exclude beneficiaries. Dashboard disposal may "
            "also conceal wrong rejection.\n\n"
            "Therefore government should simplify the process before computerisation, publish a service standard, "
            "preserve assisted and offline access, minimise data, give reasons, enable correction and human review, "
            "and measure first-contact resolution, equity and citizen feedback. E-governance helps beneficiaries "
            "to the extent that it changes the whole service journey, not merely the front screen."
        ),
    ),
    _pyq(
        2022,
        (
            "GS-IV Q4(b): Online methodology is being used for day-to-day meetings, "
            "institutional approvals in the administration and for teaching and learning in "
            "education sector to the extent telemedicine in the health sector is getting popular "
            "with the approvals of the competent authority. No doubt, it has advantages and "
            "disadvantages for both the beneficiaries and the system at large. Describe and "
            "discuss the ethical issues involved in the use of online method particularly to the "
            "vulnerable section of the society. (Answer in 150 words)"
        ),
        10,
        (
            "Faithful English text verified against books\\more_previous_papers\\"
            "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf, page 3. Broader technology-ethics "
            "question, neutrally routed here for digital inclusion and last-mile service access."
        ),
        (
            "Online methods can reduce travel, waiting and geographic barriers, preserve records and extend "
            "specialist access. For a remote patient or student, these gains can be substantial. Ethical concerns "
            "arise, however, when digital delivery assumes reliable devices, connectivity, literacy, language, "
            "privacy and a safe home environment that vulnerable users may not possess.\n\n"
            "A digital-only welfare process can convert poverty or disability into exclusion. Biometric or data "
            "mismatch may deny service without explanation; telemedicine can risk confidentiality and diagnostic "
            "quality; automated approvals may reproduce biased data. Women, elderly persons, migrants and persons "
            "with disabilities may face distinct access constraints.\n\n"
            "The public-service response is digital-by-default where useful, never digital-only where rights are "
            "at stake. Provide assisted centres, accessible design, local-language and low-bandwidth channels, "
            "alternative authentication, data minimisation, informed consent where applicable, reasoned decisions, "
            "correction and human review. Monitor group-wise exclusion and repeat grievances. Technology is ethical "
            "when it expands effective choice and dignity rather than transferring administrative burden to those "
            "least able to bear it."
        ),
    ),
    _pyq(
        2024,
        (
            "GS-IV Q6(b): Mission Karmayogi is aiming for maintaining a very high standard "
            "of conduct and behaviour to ensure efficiency for serving citizens and in turn "
            "developing oneself. How will this scheme empower the civil servants in enhancing "
            "productive efficiency and delivering the services at the grassroots level. "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Faithful isolated English question verified against books\\mains\\"
            "05 UPSC 2024 Paper-IV_Final 1.pdf, page 4. Directly routed for capability and "
            "work-culture analysis; the answer avoids unverified platform statistics or targets."
        ),
        (
            "Mission Karmayogi's ethical promise is to connect individual capability with citizen outcomes. "
            "Role-based learning can help officials understand law, technology, local context and behavioural "
            "skills required for their actual functions rather than treating training as a one-time formality. "
            "Competency mapping can expose gaps; continuous learning and peer exchange can spread workable "
            "solutions across districts.\n\n"
            "At the grassroots, empowerment should appear as accurate eligibility advice, simpler workflow, "
            "respectful communication, data-informed planning and quicker resolution of recurring service "
            "problems. A trained frontline officer can use empathy to assist an elderly claimant while preserving "
            "verification and equal treatment. Supervisors should link learning to charter standards, grievance "
            "patterns and observed performance, not course completion alone.\n\n"
            "Training, however, cannot substitute for adequate staffing, delegated authority, interoperable "
            "records and accountable leadership. Nor should efficiency mean faster wrongful disposal. Mission "
            "Karmayogi empowers service delivery when capability-building is role-specific, evaluated in workplace "
            "behaviour and joined to process redesign, inclusion, reasons and citizen feedback."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q4(a): For any kind of social re-engineering by successfully implementing "
            "welfare schemes, a civil servant must use reason and critical thinking in an ethical "
            "framework. Justify this statement with suitable examples. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated English question verified against books\\mains\\"
            "UPSC Mains 2025 GS Paper 4.pdf, page 3. Broader welfare-implementation demand, "
            "neutrally routed here for citizen-centred delivery and feedback."
        ),
        (
            "Welfare implementation changes access, incentives and social relations; good intention alone cannot "
            "show whether a design works fairly. Reason identifies causal links, feasible alternatives and evidence. "
            "Critical thinking tests assumptions, unintended effects and whose experience is missing. An ethical "
            "framework supplies dignity, equality, proportionality, privacy and accountability.\n\n"
            "For example, a digital benefit system may appear efficient but biometric failure can exclude elderly "
            "or manual workers. The civil servant should examine group-wise rejection, create lawful alternative "
            "verification and preserve human review. A nutrition scheme should test last-mile availability and "
            "social barriers rather than count allocations alone. Citizen consultation and grievance patterns can "
            "reveal design failure invisible in aggregate dashboards.\n\n"
            "Critical thinking does not authorise endless experimentation with vulnerable lives. Decisions need "
            "lawful authority, pilots where appropriate, safeguards, transparent criteria, monitoring and correction. "
            "Thus social re-engineering becomes ethical when the officer combines evidence with constitutional "
            "values and treats beneficiaries as participants and rights-holders, not passive objects of administrative "
            "benevolence."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q5(a): \"One who is devoted to one's duty attains highest perfection in "
            "life.\" Analyse this statement with reference to sense of responsibility and personal "
            "fulfilment as a civil servant. (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated English question verified against books\\mains\\"
            "UPSC Mains 2025 GS Paper 4.pdf, page 3. Broader duty question, neutrally routed "
            "for professionalism and service-oriented work culture."
        ),
        (
            "Devotion to duty is sustained, competent and public-purpose performance despite inconvenience; it "
            "is not unquestioning obedience, overwork or attachment to a target. A civil servant's responsibility "
            "includes understanding the lawful mandate, preparing carefully, treating citizens impartially, "
            "communicating delay, preserving records and correcting preventable error.\n\n"
            "Fulfilment arises when professional skill and moral purpose converge. An officer who redesigns an "
            "inaccessible pension journey, listens to frontline staff and sees eligible citizens receive timely "
            "service gains mastery, trust and meaningful connection with public work. Such success strengthens a "
            "service culture in which accuracy and empathy reinforce each other.\n\n"
            "The idea needs limits. Duty cannot mean implementing an unlawful instruction, hiding harm to protect "
            "the organisation, exhausting staff or meeting speed targets through wrongful rejection. The devoted "
            "officer gives candid advice, seeks written clarity where needed and uses lawful review. Personal "
            "perfection in administration lies in reliable service bounded by Constitution, competence, dignity "
            "and care."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q5(b): To achieve holistic development goal, a civil servant acts as an "
            "enabler and active facilitator of growth rather than a regulator. What specific "
            "measures will you suggest to achieve this goal? (Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated English question verified against books\\mains\\"
            "UPSC Mains 2025 GS Paper 4.pdf, page 3. Directly routed for facilitative service "
            "delivery. 'Enabler' is not interpreted as abandonment of necessary regulation."
        ),
        (
            "An enabler removes avoidable administrative friction, coordinates legitimate activity and expands "
            "citizens' capability while preserving safety, rights and fair competition. Specific measures include "
            "service-wise Citizens' Charters with realistic time and quality standards; single-window coordination "
            "with integrated back-end responsibility; risk-based inspection; plain eligibility guidance; lawful "
            "pre-application assistance; time-stamped tracking; and reasoned approval or refusal.\n\n"
            "Process maps should eliminate duplicate documents and approvals. Digital channels need assisted, "
            "offline and accessible alternatives. CPGRAMS and departmental grievances should feed recurring problems "
            "back into redesign. Frontline officers require delegated authority, role-based training, ethics advice "
            "and protection for documented good-faith initiative. Performance measures should reward resolution, "
            "accuracy and inclusion, not disposal alone.\n\n"
            "Facilitation is not deregulation. High-risk activities still require proportionate safeguards, conflict "
            "control and audit. A regulator becomes developmental when it explains requirements, targets scrutiny "
            "to risk and helps compliant citizens navigate law without favour. The goal is solution-oriented legality, "
            "not permission by personal discretion."
        ),
    ),
    _pyq(
        2025,
        (
            "GS-IV Q6(a): It is said that for an ethical work culture, there must be code of "
            "ethics in place in every organisation. To ensure value-based and compliance-based "
            "work culture, what suitable measures would you adopt in your work place? "
            "(Answer in 150 words)"
        ),
        10,
        (
            "Exact isolated English question verified against books\\mains\\"
            "UPSC Mains 2025 GS Paper 4.pdf, page 3. Shared with Topic 16's code architecture; "
            "Topic 17 neutrally routes the lived-culture, leadership and service-performance dimensions."
        ),
        (
            "I would begin with a participatively drafted ethics statement linking constitutional service, integrity, "
            "impartiality, dignity, empathy and stewardship to recurring workplace situations. A complementary conduct "
            "matrix would specify conflicts, gifts, harassment, data use, record integrity and retaliation, with fair "
            "reporting and consequence routes.\n\n"
            "Culture is formed by daily signals. Leaders should model respectful citizen interaction, invite bad news, "
            "protect advice-seeking and explain decisions. Teams should discuss near misses and grievance patterns; "
            "training should use actual service scenarios. Citizens' Charter standards should be realistic and connected "
            "to named process ownership. Recognition should reward accurate resolution, collaboration and inclusion, not "
            "targets achieved through hidden rejection.\n\n"
            "Compliance requires secure complaints, audit trails, segregation of duties, timely impartial inquiry and "
            "proportionate sanctions with review. Staff climate, repeat grievances, appeal reversals and citizen feedback "
            "should guide periodic improvement. A code becomes culture only when capability, incentives, leadership and "
            "fair accountability make ethical action both expected and practicable."
        ),
    ),
)


def _original(marks, question, answer):
    return {"marks": marks, "question": question, "answer": answer}


ORIGINAL_MAINS = (
    _original(
        10,
        (
            "Distinguish a Citizens' Charter from grievance redress and from a statutory "
            "right to time-bound public service."
        ),
        (
            "A Citizens' Charter is an organisation's public statement of services, standards, timelines, "
            "responsibilities and recourse. It makes the service promise visible but is ordinarily an "
            "administrative commitment; publication alone does not create a legal entitlement or penalty.\n\n"
            "Grievance redress operates when a citizen alleges delay, denial, misconduct or poor delivery. "
            "It registers, routes, examines, responds to and escalates the complaint. CPGRAMS, for example, "
            "provides lodging, tracking, feedback and appeal features, while the concerned authority remains "
            "responsible for substantive resolution. A complaint system can exist without a well-designed charter, "
            "and a charter can exist without effective grievance handling.\n\n"
            "A statutory service guarantee derives from an applicable State law or other competent instrument. "
            "It normally applies only to notified services and specifies designated officers, time limits and "
            "statutory appeal or consequence routes. Exact design varies by State. The three should therefore be "
            "connected but not conflated: promise, remedy process and enforceable entitlement."
        ),
    ),
    _original(
        10,
        (
            "Why can a public office meet its turnaround target and still fail ethically in "
            "service delivery?"
        ),
        (
            "Turnaround measures only one dimension of service. An office may meet it by rejecting difficult "
            "applications, resetting clocks, transferring unfinished work, ignoring accuracy or excluding citizens "
            "who need assistance. Fast disposal can therefore conceal denial of dignity, equality and substantive "
            "resolution.\n\n"
            "A pension office, for example, may close every case within two days by returning minor spelling "
            "mismatches without explaining correction. The dashboard improves while eligible elderly applicants "
            "bear repeated travel and lost income. Ethical measurement should combine timeliness with accuracy, "
            "first-contact resolution, correction rate, accessibility, repeat grievance, appeal reversal, citizen "
            "feedback and group-wise exclusion.\n\n"
            "Targets still matter because indefinite delay is unjust. The answer is not to abandon measurement but "
            "to add anti-gaming safeguards: clear clock rules, sample file audit, recorded reasons, equity checks and "
            "review of complex cases. Good service is timely, correct, fair and usable; speed without these qualities "
            "is efficient-looking failure."
        ),
    ),
    _original(
        15,
        (
            "Design a complete Citizens' Charter for a district pension service, including "
            "consultation, standards, monitoring and review."
        ),
        (
            "The district should first map the complete pension journey with pensioners, disability groups, "
            "frontline staff, treasury and banks. The charter should identify eligibility, required documents, "
            "lawful fees, submission and assisted channels, the responsible service unit and accessible contact. "
            "Standards must cover acknowledgement, decision and payment stages, with a defined clock trigger, "
            "lawful pause rule, accuracy floor and communication of deficiencies.\n\n"
            "The charter should promise plain-language reasons for approval, partial approval or refusal; status "
            "tracking; correction of record errors; and a grievance route distinct from appeal on entitlement. "
            "Where an applicable service-guarantee law covers the service, its designated officer and statutory "
            "remedies should be stated accurately rather than invented by the charter.\n\n"
            "Monitoring should track timeliness, first-contact resolution, correction, repeat grievance, appeal "
            "reversal, accessibility and outcomes across gender, disability and location. A manager should own "
            "breach alerts and corrective action. Quarterly frontline review and periodic user consultation should "
            "identify avoidable documents, authentication failures and last-mile gaps. Independent sample audit "
            "should test gaming. The charter must carry a review date and publish what changed. Thus consultation "
            "sets relevant promises, capability makes them feasible and feedback keeps them alive."
        ),
    ),
    _original(
        15,
        (
            "Examine how leadership and organisational culture determine whether service-delivery "
            "reforms become lived practice or compliance theatre."
        ),
        (
            "Formal reforms change text and technology quickly; culture changes what employees believe will actually "
            "be rewarded. If leaders praise low pendency regardless of wrongful rejection, staff learn to game the "
            "charter. If supervisors punish bad news, grievance records become ceremonial. Conversely, leaders who "
            "visit service points, model courtesy, protect advice-seeking and correct their own errors make citizen "
            "dignity operational.\n\n"
            "Culture is carried through recruitment, induction, peer stories, workload, discretion, promotion and "
            "sanction. Reform should therefore align these channels. Teams need scenario training in lawful assistance, "
            "bias, accessibility and reasons; frontline workers need tools and authority to resolve predictable cases; "
            "performance review should combine speed, accuracy, inclusion and citizen feedback; and complaint handling "
            "must protect staff and citizens from retaliation.\n\n"
            "Leadership is necessary but not heroic substitution for systems. A courteous collector cannot compensate "
            "permanently for broken records or vacancies. Process redesign, adequate capability and fair discipline must "
            "support the ethical message. Culture becomes credible when employees see consistent consequences: respectful "
            "problem-solving is recognised, manipulation is investigated through due process, and recurring failure leads "
            "to organisational learning rather than blame displacement."
        ),
    ),
    _original(
        20,
        (
            "A State proposes to integrate Citizens' Charters, a grievance portal and its "
            "public-service-guarantee law into one service-delivery system. Develop an ethical "
            "and administratively workable model."
        ),
        (
            "The model should preserve the distinct function of each layer. The Citizens' Charter should publish "
            "service-wise eligibility, documents, fee, responsible unit, realistic time and quality standards, "
            "accessible channels and ordinary grievance route. The service-guarantee layer should identify only "
            "notified services and reproduce the applicable statutory trigger, designated officer, appeal and "
            "consequence accurately. The grievance portal should register service failure, route it to the competent "
            "authority, provide tracking, record reasoned closure, collect feedback and enable lawful escalation.\n\n"
            "Integration should use a common service identifier. A missed charter standard should generate an alert; "
            "a grievance should draw verified application data without forcing resubmission; a statutory breach should "
            "move through the legal appeal route rather than be closed as an ordinary complaint. Citizens must see which "
            "route grants information, service correction, compensation or appeal.\n\n"
            "Capability is the fourth operational layer. Map and simplify the process, remove duplicate documents, "
            "integrate back-end responsibility, train staff and preserve assisted, offline and accessible access. Data "
            "collection should be necessary and secure, with correction and human review for automated errors.\n\n"
            "Governance should track timeliness, accuracy, first-contact resolution, repeat grievance, appeal reversal, "
            "citizen feedback and group-wise exclusion. Independent sample audit should detect clock manipulation and "
            "premature closure. A cross-department service council should publish learning and revise standards after "
            "consultation. Penalties require statutory authority and fair process; capability failure should not be "
            "mislabelled automatically as individual misconduct. The integrated system succeeds when promise, redress, "
            "entitlement and capacity reinforce rather than overwrite one another."
        ),
    ),
    _original(
        20,
        (
            "A digital welfare portal shows excellent disposal rates, yet field reports reveal "
            "biometric exclusion, repeated grievance closure and dependence on private agents. "
            "Diagnose the ethical failures and propose a complete service-recovery plan."
        ),
        (
            "The dashboard records administrative movement, not effective access. Biometric exclusion without "
            "alternative verification converts technology into an eligibility barrier. Repeated closure without "
            "resolution destroys answerability, while dependence on private agents shifts cost and data risk to "
            "citizens. The pattern also suggests inaccessible design, weak frontline capability, metric gaming and "
            "leadership preference for favourable numbers.\n\n"
            "Immediate recovery should reopen affected cases, stop adverse action based only on unresolved authentication, "
            "provide lawful alternative verification and assisted centres, protect registration dates and communicate "
            "reasons. High-risk groups should receive outreach through authorised mobile or local channels. Complaints "
            "must be reviewed by a competent officer rather than recycled to the original desk, with appeal information "
            "and correction of wrong data.\n\n"
            "System repair requires journey mapping with users and frontline staff; removal of duplicate fields and visits; "
            "accessible, local-language and low-bandwidth design; data minimisation and secure agent controls; human review "
            "of automated mismatch; and a genuine single owner for the complete service. The charter should state time, "
            "accuracy, accessibility and remedy standards.\n\n"
            "Replace disposal-only reporting with first-contact resolution, repeat grievance, appeal reversal, correction "
            "rate, assisted-channel use and group-wise exclusion. Audit samples should compare dashboard claims with field "
            "outcomes. Leaders must publish corrective learning and protect staff who report failure. Individual manipulation "
            "should face fair inquiry, while staffing or design defects require organisational responsibility. Digital "
            "delivery becomes ethical only when it reduces, rather than privatises, the burden of claiming a public service."
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
        "1. Citizen-centric service chain",
        "continuous-service-chain",
        (
            "Citizen is rights-holder",
            "Authority defines lawful service",
            "Charter publishes commitment",
            "Capability performs the work",
            "Culture shapes the encounter",
            "Grievance exposes failure",
            "Remedy corrects harm",
            "Learning redesigns the system",
        ),
        "A charter is credible only inside a complete promise-to-learning chain.",
        "Use to open any broad service-delivery answer.",
    ),
    _panel(
        "2. Complete charter anatomy",
        "charter-anatomy",
        (
            "Name service and eligibility",
            "List documents and lawful fee",
            "State time and quality standard",
            "Define clock and pause rules",
            "Identify responsible contact",
            "Explain status and reasons",
            "Publish grievance route",
            "Fix monitoring and review date",
        ),
        "Specific, usable and reviewable commitments replace decorative declarations.",
        "Use for the 2019 direct charter PYQ.",
    ),
    _panel(
        "3. Standard design matrix",
        "quality-standard-matrix",
        (
            "Speed without rushed disposal",
            "Accuracy without hidden backlog",
            "Fairness across social groups",
            "Accessibility across disabilities",
            "Completeness of final outcome",
            "Communication during delay",
            "Correction of official error",
            "Audit against target gaming",
        ),
        "Quality, fairness and usability must discipline every time target.",
        "Use for metrics and ethical-failure analysis.",
    ),
    _panel(
        "4. Consultation and review loop",
        "consultation-loop",
        (
            "Map users and non-users",
            "Hear vulnerable groups",
            "Test frontline feasibility",
            "Publish draft standards",
            "Pilot the service journey",
            "Measure citizen experience",
            "Revise weak commitments",
            "Publish changes and reasons",
        ),
        "A living charter learns from both citizen barriers and delivery capability.",
        "Use for reform and periodic-review recommendations.",
    ),
    _panel(
        "5. Three instruments kept distinct",
        "three-layer-distinction",
        (
            "Charter states the promise",
            "Grievance registers failure",
            "Authority investigates complaint",
            "Administrative remedy may follow",
            "Statute creates entitlement",
            "Only notified services qualify",
            "Appeal follows applicable law",
            "Exact State design controls",
        ),
        "Promise, complaint route and statutory right are connected but never interchangeable.",
        "Use for close-option distinctions and legal precision.",
    ),
    _panel(
        "6. Sevottam and CPGRAMS route",
        "integrated-quality-route",
        (
            "Charter sets service standard",
            "Capability makes it feasible",
            "Citizen experiences delivery",
            "CPGRAMS records grievance",
            "Registration enables tracking",
            "Feedback tests closure",
            "Appeal challenges poor resolution",
            "Patterns drive capability repair",
        ),
        "A portal makes failure visible; the responsible authority must still resolve it.",
        "Use for current official linkage.",
    ),
    _panel(
        "7. Ethical work-culture engine",
        "culture-engine",
        (
            "Leadership models public service",
            "Professionalism joins skill and care",
            "Empathy reveals lived barriers",
            "Rules preserve equal treatment",
            "Teams discuss near misses",
            "Incentives reward true resolution",
            "Safe feedback prevents concealment",
            "Fair accountability sustains trust",
        ),
        "Employees follow repeated signals more readily than ceremonial slogans.",
        "Use for the 2025 ethical-work-culture PYQ.",
    ),
    _panel(
        "8. Facilitative administration",
        "enabler-ladder",
        (
            "Explain lawful requirements",
            "Offer pre-application assistance",
            "Remove duplicate documents",
            "Coordinate a single window",
            "Use risk-based scrutiny",
            "Give reasoned decisions",
            "Correct curable defects",
            "Retain safeguards for high risk",
        ),
        "Enabler means solution-oriented legality, not abandonment of regulation.",
        "Use for the 2025 facilitator PYQ.",
    ),
    _panel(
        "9. Process before portal",
        "redesign-before-digital",
        (
            "Map present citizen journey",
            "Remove avoidable touchpoints",
            "Assign end-to-end ownership",
            "Simplify evidence requirements",
            "Integrate back-end workflow",
            "Digitise with traceable records",
            "Provide correction and review",
            "Audit real outcome after launch",
        ),
        "Computerising a fragmented process can accelerate opacity rather than service.",
        "Use for e-governance and Mission Karmayogi answers.",
    ),
    _panel(
        "10. Last-mile inclusion ladder",
        "inclusion-ladder",
        (
            "Accessible physical counter",
            "Assisted digital channel",
            "Local-language communication",
            "Low-bandwidth alternative",
            "Alternative authentication",
            "Disability-compatible interface",
            "Human review of exclusion",
            "Outreach to remote users",
        ),
        "Digital-by-default must never become exclusion by design.",
        "Use for vulnerable-group and online-method questions.",
    ),
    _panel(
        "11. Metrics and anti-gaming dashboard",
        "balanced-metrics-dashboard",
        (
            "Timeliness of final outcome",
            "Accuracy and correction rate",
            "First-contact resolution",
            "Repeat grievance frequency",
            "Appeal reversal pattern",
            "Citizen feedback quality",
            "Group-wise access and exclusion",
            "Independent sample-file audit",
        ),
        "Measure resolved, correct and equitable service rather than attractive disposal alone.",
        "Use for diagnosis, monitoring and evaluation.",
    ),
    _panel(
        "12. Complete examiner answer spine",
        "answer-spine",
        (
            "Define charter and citizen-centricity",
            "Distinguish redress and legal right",
            "State standards and ownership",
            "Add Sevottam capability logic",
            "Diagnose work-culture incentives",
            "Redesign process and access",
            "Use balanced metrics and review",
            "Conclude promise plus remedy",
        ),
        "The strongest answer connects ethical values to an administratively testable service system.",
        "Use for PYQ synthesis and original Mains practice.",
    ),
)


CURRENT_ANCHOR = {
    "title": (
        "Live official Sevottam and CPGRAMS service-delivery architecture, verified "
        "29 August 2026"
    ),
    "verified_facts": (
        "DARPG continues to host an official Sevottam resource identifying the model with citizen-charter, public-grievance-redress and service-delivery-capability components.",
        "The official CPGRAMS portal describes itself as a 24x7 online platform for citizens to lodge grievances concerning service delivery.",
        "The portal states that it is connected to all Ministries and Departments of the Government of India and States through role-based access.",
        "CPGRAMS provides a unique registration ID for status tracking and is also accessible through a standalone mobile application and UMANG integration.",
        "After closure, a complainant may provide feedback; the portal states that a Poor rating enables the appeal option and that appeal status can also be tracked.",
    ),
    "administrative_link": (
        "The official architecture confirms the central lesson of this topic: a published service "
        "promise, an accessible grievance route and organisational capability perform different functions. "
        "Citizen-centricity improves when grievance and feedback evidence is used to redesign the service, "
        "not when the portal merely records disposal."
    ),
    "limit": (
        "CPGRAMS is an administrative grievance platform, not a court, an RTI appellate body or a universal "
        "statutory right-to-service authority. A Citizens' Charter is not automatically enforceable as law. "
        "Any claim about notified services, designated officers, appeal levels, penalties or compensation must "
        "be checked against the applicable State or sectoral instrument. No mutable performance number or "
        "resolution benchmark is asserted here."
    ),
}


CURRENT_SOURCE_URLS = (
    "https://www.darpg.gov.in/relatedlinks/sevottam",
    "https://pgportal.gov.in/",
)


SOURCE_CAVEAT = (
    "The Topic 17 Basic and Advanced owners control the conceptual spine. The Second ARC's Fourth "
    "Report, Ethics in Governance, is a dated recommendation source: paragraph 5.1.7 defines the "
    "Citizens' Charter as an undertaking by a public service organisation, records that many charters "
    "had fallen into disuse and recommends specific obligations, time limits and clearly stated remedy, "
    "penalty or compensation, preferring a few feasible promises to impractical declarations. Paragraph "
    "5.1.8 proposes citizen feedback through professional assessment and public-office rating. Paragraph "
    "6.3.3 supports genuine single-window service backed by automated related offices and discusses "
    "positive silence with an explicit downstream-harassment caution; paragraph 6.3.5 recommends "
    "simplification, fewer tiers and time limits. These are ARC recommendations and examples, not proof "
    "that every element is current law or universally implemented. Sevottam joins Citizens' Charter, "
    "public grievance redress and service-delivery capability; do not reduce it to the charter alone. "
    "CPGRAMS provides administrative grievance lodging, routing, tracking, feedback and appeal features; "
    "it does not itself adjudicate every underlying entitlement and excludes specified matter categories "
    "listed on its official portal. A charter states a public commitment; grievance redress handles a "
    "complaint; an enforceable right to time-bound service must come from the applicable statutory or "
    "competent instrument. State service-guarantee laws differ in notified services, officers, trigger "
    "rules, appeals, penalties and compensation, so no one State model should be universalised. "
    "Citizen-centricity is not ordinary retail customer service: public authorities remain bound by "
    "legality, equality, dignity, accessibility and special duties toward persons lacking market choice. "
    "Speed is not quality by itself; measure accuracy, accessibility, resolution, correction and equity. "
    "Digital-by-default must not become digital-only exclusion. Facilitative administration means "
    "solution-oriented legality and risk-based regulation, not abandonment of safety or equal treatment. "
    "Topic 17 may note that simplified, traceable delivery can reduce opportunities for petty rent-seeking, "
    "but detailed corruption analysis and utilisation of public funds remain Topic 18-owned. Full legal "
    "analysis of individual State Acts belongs with the relevant Governance or Polity owner, and full "
    "case-study method remains Topic 22-owned. Official local UPSC PDFs control PYQ wording; broader "
    "questions are explicitly labelled as neutral routes rather than falsely presented as exclusive "
    "Topic 17 ownership."
)


REGISTER_SUPPLEMENT = (
    "### SESSION 1 — CITIZEN-CENTRIC SERVICE AS AN ETHICAL CHAIN\n\n"
    "- **Starting point:** the citizen is a constitutional rights-holder dealing with public authority, not merely a customer choosing among sellers.\n"
    "- **Complete chain:** lawful service definition → public promise → capable workflow → respectful encounter → grievance and remedy → learning and redesign.\n"
    "- **Charter:** makes services, standards, time expectations, responsibility and recourse visible.\n"
    "- **Culture:** determines what staff actually do when the queue is long, the case is difficult or the dashboard is under pressure.\n"
    "- **Delivery:** must be timely, correct, fair, accessible, reasoned and capable of correction.\n"
    "- **Recall line:** promise without capability is theatre; capability without accountability is unreviewable power.\n\n"
    "### SESSION 2 — CHARTER ANATOMY AND STANDARDS\n\n"
    "- **Service specification:** eligibility, documents, fee if any, submission channel, responsible contact, final outcome and ordinary recourse.\n"
    "- **Time standard:** define clock start, lawful pause, citizen notice, restart and final completion; internal forwarding must not reset responsibility invisibly.\n"
    "- **Quality standard:** accuracy, completeness, accessibility, equal treatment, communication and correction—not speed alone.\n"
    "- ✅ **Second ARC 5.1.7:** specific obligations and time limits; clear remedy/penalty/compensation; a few feasible promises rather than impractical abundance.\n"
    "- **Disclosure:** display at the point of service, online and in accessible language; disclose fees, documents and escalation rather than forcing dependence on agents.\n"
    "- **UPSC trap:** a mission statement or slogan is not a complete Citizens' Charter.\n\n"
    "### SESSION 3 — CONSULTATION, OWNERSHIP, MONITORING AND REVIEW\n\n"
    "- **Consultation set:** current users, non-users, vulnerable groups, frontline staff, supervisors and partner institutions.\n"
    "- **Design test:** measure the outcome citizens need, not merely the activity easiest for the department to count.\n"
    "- **Ownership:** identify service unit and contact publicly; assign decision, supervisory and escalation roles internally.\n"
    "- ✅ **Second ARC 5.1.8:** citizen perception, professional assessment and ratings can support accountability in high-contact offices.\n"
    "- **Review loop:** collect evidence → correct individual harm → analyse recurring pattern → redesign process → revise charter → publish changes.\n"
    "- **Caution:** consultation without response is participation theatre; ratings without case audit can reward popularity rather than lawful service.\n\n"
    "### SESSION 4 — CHARTER, GRIEVANCE AND STATUTORY GUARANTEE\n\n"
    "- **Charter:** prospective statement of the promised service and standard.\n"
    "- **Grievance redress:** complaint registration, routing, examination, response, escalation and corrective action after or during failure.\n"
    "- **Statutory guarantee:** enforceable only through applicable law or competent instrument, ordinarily for notified services with defined officers, periods and appeals.\n"
    "- **State-law caution:** service lists, triggers, appeal levels, penalties and compensation vary; verify the exact State instrument.\n"
    "- **Remedy routing:** information denial → RTI route; service delay/denial → department, applicable service guarantee or grievance route; corruption allegation → competent vigilance/investigation route.\n"
    "- **Recall line:** charter is promise; grievance is complaint route; statute is entitlement.\n\n"
    "### SESSION 5 — SEVOTTAM AND CPGRAMS\n\n"
    "- ✅ **Sevottam:** Citizens' Charter + public grievance redress + service-delivery capability.\n"
    "- **Interdependence:** promise without capability fails; capability without grievance feedback cannot learn; grievance machinery without standards cannot test breach clearly.\n"
    "- ✅ **CPGRAMS live portal:** 24x7 lodging for service-delivery grievances, unique registration ID, tracking, feedback and available appeal feature.\n"
    "- **Institutional limit:** the portal supports routing and monitoring; the competent public authority supplies substantive resolution.\n"
    "- **Quality test:** reasoned closure, actual correction, repeat grievance and appeal outcome—not disposal count alone.\n"
    "- **Exclusion caution:** CPGRAMS lists matter categories it does not take up; never present it as an all-purpose tribunal.\n\n"
    "### SESSION 6 — WORK CULTURE, LEADERSHIP AND PROFESSIONALISM\n\n"
    "- **Work culture:** repeated leadership signals, peer norms, routines and incentives that define what is truly rewarded.\n"
    "- **Leadership:** model courtesy and legality, invite bad news, protect advice-seeking, correct manipulation and own cross-unit failure.\n"
    "- **Professionalism:** competence + preparation + impartiality + records + communication + respect + lawful problem-solving.\n"
    "- **Empathy:** identify lived barriers and redesign access; never fabricate eligibility or waive mandatory safeguards from sympathy.\n"
    "- **Responsiveness:** timely listening, assistance, communication and correction; not automatic agreement with every request.\n"
    "- **Culture test:** falling complaints may indicate improvement or fear—triangulate with feedback, appeals, field audit and staff climate.\n\n"
    "### SESSION 7 — PROCESS REDESIGN AND DIGITAL DELIVERY\n\n"
    "- **Sequence:** map journey → remove duplicate steps → simplify evidence → assign end-to-end owner → integrate back end → digitise → audit outcome.\n"
    "- ✅ **Second ARC 6.3.3:** genuine single window needs automated backing of related offices; one reception counter over silos is insufficient.\n"
    "- **Facilitative administration:** explain requirements, assist before rejection, use risk-based scrutiny, cure defects and retain proportionate safeguards.\n"
    "- **Digital safeguards:** necessary data only, secure handling, reasons, correction and meaningful human review.\n"
    "- **Positive silence:** an ARC reform option for suitable permissions, never a universal rule; protect against downstream harassment and unsafe deemed approval.\n"
    "- **Boundary:** process simplification may reduce petty rent-seeking opportunities, but detailed corruption analysis belongs to Topic 18.\n\n"
    "### SESSION 8 — INCLUSION AND LAST-MILE ACCESS\n\n"
    "- **Digital-by-default, not digital-only:** preserve assisted, offline or alternative access where exclusion risk exists.\n"
    "- **Access dimensions:** connectivity, device, cost, literacy, language, disability, gendered mobility, authentication and remote geography.\n"
    "- **Design tools:** accessible interface, local-language support, low-bandwidth route, staffed centre, alternative authentication, authorised outreach and home/mobile service where lawful.\n"
    "- **Human review:** automated mismatch must be explainable, correctable and reviewable before irreversible denial.\n"
    "- **Agent risk:** remove unnecessary dependence on private intermediaries; publish documents, fees and status directly and protect citizen data.\n"
    "- **Equity metric:** compare delay, rejection, correction and grievance across groups and locations.\n\n"
    "### SESSION 9 — METRICS, FAILURE MODES AND LEARNING\n\n"
    "- **Balanced dashboard:** final-outcome time, accuracy, first-contact resolution, correction, repeat grievance, appeal reversal, accessibility, feedback and group-wise exclusion.\n"
    "- **Gaming patterns:** easy-case selection, hard-case rejection, clock reset, queue shifting, premature closure and quality sacrifice.\n"
    "- **Controls:** fixed definitions, reason codes, sample case audit, citizen verification, equity review and independent challenge.\n"
    "- **Failure demand:** repeated complaints about one process should trigger upstream redesign rather than endless downstream disposal.\n"
    "- **No-blame qualification:** distinguish individual manipulation from understaffing, obsolete rules or broken infrastructure; assign responsibility at the correct level.\n"
    "- **Learning:** publish corrective action and revise standards; secrecy about failure preserves recurrence.\n\n"
    "### SESSION 10 — PYQ AND ANSWER ARCHITECTURE\n\n"
    "- ✅ **2019:** direct principles and importance of Citizens' Charter movement.\n"
    "- ✅ **2021:** social-audit route for performance, accountability and ethical conduct.\n"
    "- ✅ **2022:** core versus peripheral bureaucracy; empathy; purposive rules; e-governance; vulnerable-group online access.\n"
    "- ✅ **2024:** Mission Karmayogi, productive efficiency and grassroots service.\n"
    "- ✅ **2025:** welfare implementation through reason; duty; enabler/facilitator; ethical work culture.\n"
    "- **10-mark spine:** define → distinguish → two mechanisms → Indian illustration → limit → verdict.\n"
    "- **15-mark spine:** diagnose charter/culture/capability → mapped reform → inclusion and metric safeguards → qualified conclusion.\n"
    "- **20-mark spine:** promise + grievance + statutory layer + process/culture/capability + digital inclusion + monitoring + institutional responsibility.\n"
    "- **Final thesis:** citizen-centric service is a governed learning system—specific promise, capable process, humane culture, correct remedy and evidence-led revision.\n\n"
    "### RAPID DISTINCTION TABLE\n\n"
    "| Pair | Controlling distinction |\n"
    "|---|---|\n"
    "| Charter vs grievance | Prospective service promise vs complaint-and-correction route |\n"
    "| Charter vs statutory right | Administrative commitment vs entitlement created by competent law/instrument |\n"
    "| CPGRAMS vs adjudication | Routing, tracking, feedback and appeal architecture vs final merits determination by competent authority |\n"
    "| Customer vs citizen | Service experience matters, but legality, equality, dignity and non-market duties remain controlling |\n"
    "| Speed vs quality | Turnaround is one indicator; accuracy, accessibility and resolution complete the standard |\n"
    "| Digitisation vs transformation | Electronic front end vs redesigned end-to-end service journey |\n"
    "| Enabler vs deregulator | Lawful facilitation and risk-based scrutiny vs abandonment of safeguards |\n"
    "| Feedback vs accountability | Collected opinion vs assigned response, remedy and visible correction |\n\n"
    "### FINAL REFORM CHECKLIST\n\n"
    "1. Define the citizen outcome and legal mandate.\n"
    "2. Consult users, non-users, vulnerable groups and frontline staff.\n"
    "3. Publish few feasible time, quality, fairness and access standards.\n"
    "4. Define the clock, documents, fee, owner, reasons and ordinary grievance route.\n"
    "5. State any statutory service guarantee only from the applicable instrument.\n"
    "6. Build staffing, workflow, records and technology before promising performance.\n"
    "7. Preserve assisted and alternative last-mile access.\n"
    "8. Link CPGRAMS or departmental complaint learning to process redesign.\n"
    "9. Audit metrics for premature closure, exclusion and queue manipulation.\n"
    "10. Revise the charter publicly and distinguish individual breach from system incapacity.\n\n"
    "### BOUNDARY AND SOURCE DISCIPLINE\n\n"
    "- Topic 17 owns charter design, work culture and ethical quality of service delivery.\n"
    "- Topic 18 owns detailed utilisation of public funds and corruption analysis; use only a boundary reference here.\n"
    "- Topic 16 owns the full Code of Ethics/Code of Conduct architecture; Topic 17 uses codes only as culture-supporting instruments.\n"
    "- Topic 15 owns detailed RTI law; a charter's disclosure function does not replace RTI.\n"
    "- Topic 22 owns full case-study method.\n"
    "- ARC recommendations are recommendations, not automatically current law.\n"
    "- Mutable CPGRAMS benchmarks, State service lists, penalty amounts and appeal structures require live verification before use."
)
