"""Authored learner-v2 data for Internal Security Topic 01."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/sites/default/files/AREnglish_24032026.pdf "
        "— searched 2026-09-04; the official MHA Annual Report 2024-25 "
        "result confirms that public order and police are State subjects and "
        "that Union assistance operates under Article 355 without displacing "
        "State responsibility. The direct PDF fetch returned 403, so no "
        "unstated agency strength, incident count or outcome was imported."
    ),
    (
        "https://legislative.gov.in/constitution-of-india/ — attempted "
        "2026-09-04; this is the official constitutional source for Article "
        "355 and the Seventh Schedule. The authored anchors preserve State "
        "List Entries 1 and 2 and Union List Entry 2A without treating aid to "
        "civil power as a transfer of ordinary policing."
    ),
    (
        "https://www.indiacode.nic.in/ — searched 2026-09-04 for BNSS "
        "section 173, the Official Secrets Act, 1923 and the Arms Act, 1959; "
        "the module uses only distinctions already preserved in the audited "
        "owner and does not infer a 2026 objective answer letter."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Internal-security boundary", "Internal security concerns peace, law and order, rule of law and sovereignty within India's territory; external security addresses foreign aggression, but neighbourhood linkages make the two domains inter-related."),
        ("MHA-MoD boundary", "The Ministry of Home Affairs is the Union ministry responsible for internal security, while the Ministry of Defence owns external defence; central assistance does not erase State policing competence."),
        ("Kautilya fourfold frame", "Kautilya's four-fold classification distinguishes internal, external, internally aided external and externally aided internal threats; India's threat environment can combine all four."),
        ("Security attributes", "The owner identifies territorial integrity, domestic peace, law and order, rule of law and equality, freedom from fear, peaceful coexistence and communal harmony as attributes of internal security."),
        ("Eight-element doctrine", "The internal-security doctrine has political, socio-economic, governance, police and security-forces, Centre-State coordination, intelligence, border-management and cyber-security elements."),
        ("Root-cause matrix", "Governance deficit, poverty, unemployment, inequitable growth, communal or caste tension, porous borders, hostile neighbours, corruption and a weak criminal-justice system are enabling conditions rather than interchangeable threats."),
        ("Threat-vulnerability-capability", "A threat is a hostile actor or event, a vulnerability is an exploitable weakness, capability is the State's actual preventive or responsive means, and consequence is the realised harm when the first exploits the second."),
        ("Actor-means-objective", "External state and non-state actor analysis should identify actor, means, objective and intended end-state; proxy support can give a sponsor deniability without making sponsor and proxy the same legal actor."),
        ("State List primacy", "Public order is State List Entry 1 and police is State List Entry 2, making the State the primary day-to-day authority for internal order and investigation."),
        ("Union aid boundary", "Union List Entry 2A permits deployment of an armed force of the Union in a State in aid of the civil power; assistance supplements rather than replaces the State authority."),
        ("Article 355 duty", "Article 355 places a duty on the Union to protect every State against external aggression and internal disturbance and to ensure constitutional government."),
        ("Coordination constraint", "Because policing is primarily State-owned while intelligence, border guarding and several central capabilities are Union-linked, Centre-State coordination is a structural constitutional requirement."),
        ("Coercion-accommodation calibration", "The doctrine differentiates stringent response to secessionist or separatist violence from a softer and sympathetic approach to constitutional regional and ethnic aspirations."),
        ("Security-development sequencing", "Security, development and rights cannot be reduced to a universal order; area-specific sequencing must restore access and administration without allowing coercion to reproduce grievance."),
        ("Prevention-response distinction", "Prevention reduces vulnerability through intelligence, community trust and governance, whereas response contains an event; visible response outputs cannot substitute for harder-to-measure prevention."),
        ("Statutory-power boundary", "A legal power is not operational capability: trained personnel, forensics, court time, lawful procedure and inter-agency trust remain separate implementation conditions."),
        ("Area-management end-state", "Area management should protect people, deny coercive support networks and restore durable civil administration; clearing territory is not the same as holding it through legitimate governance."),
        ("Zero-FIR boundary", "BNSS section 173 permits information about a cognisable offence to be given irrespective of the area where it occurred; Zero FIR facilitates registration and transfer but does not alter final investigative jurisdiction."),
        ("OSA-Arms boundary", "The Official Secrets Act, 1923 addresses prohibited places, spying and wrongful communication, while Arms Act sections distinguish licensed possession from manufacture, sale or transfer; neither is a generic label for every security offence."),
        ("Evidence-rung discipline", "A law, notification, deployment, arrest, charge-sheet, agreement, implementation step and verified outcome are distinct evidentiary rungs and must never be collapsed in an Internal Security answer."),
    ]
    traps = [
        "Do not treat internal and external security as fully separable.",
        "Do not convert every root cause into a threat actor.",
        "Do not confuse threat, vulnerability, capability and consequence.",
        "Do not use the eight elements as a decorative checklist.",
        "Do not treat Union List Entry 2A as displacement of State police.",
        "Do not describe Article 355 as automatic President's Rule.",
        "Do not prescribe a heavy hand for every identity demand.",
        "Do not equate a statute with field capability or a scheme with outcome.",
        "Do not equate territorial clearing with legitimate administrative holding.",
        "Do not infer an objective key where the routing ledger withholds it.",
        "Do not merge Zero FIR registration with final jurisdiction.",
        "Do not expose tactical methods or unverified attribution.",
    ]
    titles = [
        "Internal and external security boundary",
        "Kautilya threat classification",
        "Attributes of internal security",
        "Eight-element doctrine",
        "Root causes triggers and organised conversion",
        "Threat vulnerability capability and consequence",
        "External state actors proxies and deniability",
        "Public order police and State primacy",
        "Union aid under Entry 2A and Article 355",
        "Centre-State coordination architecture",
        "Coercion accommodation and calibrated response",
        "Security development and rights sequencing",
        "Prevention response and measurement asymmetry",
        "Area management local perception and governance",
        "Legal distinctions PYQ routing and answer spine",
    ]
    routes = [
        "Define the territorial boundary, then explain neighbourhood interdependence.",
        "Classify the threat before naming a response.",
        "Show which protected attribute the threat actually undermines.",
        "Use the doctrine diagnostically to identify the weakest elements.",
        "Separate structural condition, proximate trigger and organised actor.",
        "Match measures to vulnerabilities and capabilities, not hostile intent alone.",
        "Trace actor, means, objective, end-state and attribution qualification.",
        "Begin with State competence before listing central support.",
        "Use the exact phrase in aid of the civil power.",
        "Explain coordination as a constitutional design problem.",
        "Match coercive or accommodative tools to the character of the demand.",
        "Argue for sequenced convergence rather than a one-size-fits-all order.",
        "Separate absent-event prevention from visible response outputs.",
        "Assess whether lawful administration and public trust can hold after action.",
        "Preserve every legal and evidentiary rung in the conclusion.",
    ]
    panels = [
        common.panel("Security boundary map", "comparison-table", [
            "INTERNAL -> peace, law and order, rule of law, sovereignty within territory",
            "EXTERNAL -> defence against foreign aggression",
            "INTERFACE -> neighbours, proxies, borders, finance and information",
            "RULE -> different lead institutions, connected threat environment",
        ], ["Internal-security boundary", "MHA-MoD boundary"]),
        common.panel("Kautilya fourfold matrix", "matrix", [
            "INTERNAL | EXTERNAL",
            "INTERNALLY AIDED EXTERNAL | EXTERNALLY AIDED INTERNAL",
            "DIAGNOSIS -> identify actor and support relationship separately",
            "TRAP -> proxy status does not erase sponsor attribution standards",
        ], ["Kautilya fourfold frame", "Actor-means-objective"]),
        common.panel("Protected-attribute rail", "causal-chain", [
            "THREAT -> territorial integrity / peace / law and order",
            "THREAT -> rule of law / equality / freedom from fear",
            "THREAT -> coexistence / communal harmony",
            "ANSWER -> name the exact attribute under stress",
        ], ["Security attributes"]),
        common.panel("Eight-element doctrine wheel", "systems-map", [
            "POLITICAL + SOCIO-ECONOMIC + GOVERNANCE",
            "POLICE / FORCES + CENTRE-STATE + INTELLIGENCE",
            "BORDER MANAGEMENT + CYBER SECURITY",
            "USE -> hypotheses to test, not eight generic headings",
        ], ["Eight-element doctrine"]),
        common.panel("Cause-trigger-actor chain", "causal-chain", [
            "STRUCTURAL CONDITION -> exclusion, weak justice, porous border",
            "TRIGGER -> incident, notice, arrest, riot or shock",
            "ORGANISED ACTOR -> recruitment, coercion, parallel authority",
            "CONSEQUENCE -> violence, fear, legitimacy loss",
        ], ["Root-cause matrix"]),
        common.panel("Risk grammar", "process-flow", [
            "THREAT + VULNERABILITY",
            "        | countered by CAPABILITY",
            "        v",
            "CONSEQUENCE if exploitation succeeds",
            "POLICY LEVER -> reduce vulnerability and build lawful capability",
        ], ["Threat-vulnerability-capability"]),
        common.panel("Federal competence ladder", "status-ladder", [
            "STATE LIST ENTRY 1 -> public order",
            "STATE LIST ENTRY 2 -> police",
            "UNION LIST ENTRY 2A -> armed force in aid of civil power",
            "ARTICLE 355 -> Union protective duty",
            "END-STATE -> cooperative action without competence erasure",
        ], ["State List primacy", "Union aid boundary", "Article 355 duty"]),
        common.panel("Response calibration", "decision-tree", [
            "VIOLENT SECESSION / SEPARATISM -> lawful coercive containment",
            "REGIONAL / ETHNIC ASPIRATION -> dialogue and accommodation",
            "MIXED CASE -> security plus political settlement",
            "SAFEGUARD -> necessity, proportionality, accountability",
        ], ["Coercion-accommodation calibration"]),
        common.panel("Security-development sequence", "process-flow", [
            "SECURE ACCESS -> HOLD THROUGH CIVIL ADMINISTRATION",
            "DELIVER RIGHTS / SERVICES -> RESTORE TRUST",
            "REASSESS VULNERABILITY -> PREVENT RELAPSE",
            "RULE -> scheme launch is not governance outcome",
        ], ["Security-development sequencing", "Area-management end-state"]),
        common.panel("Prevention versus response", "comparison-table", [
            "PREVENTION -> intelligence, trust, vulnerability reduction",
            "RESPONSE -> containment, rescue, investigation support",
            "MEASUREMENT -> absence of event versus visible outputs",
            "BUDGET TRAP -> visibility can bias resources toward response",
        ], ["Prevention-response distinction"]),
        common.panel("Legal-rung firewall", "status-ladder", [
            "LAW -> NOTIFICATION -> DEPLOYMENT / REGISTRATION",
            "INVESTIGATION -> CHARGE-SHEET -> TRIAL / DECISION",
            "AGREEMENT -> IMPLEMENTATION -> VERIFIED OUTCOME",
            "RULE -> never jump to the next rung",
        ], ["Statutory-power boundary", "Evidence-rung discipline"]),
        common.panel("PYQ answer spine", "answer-spine", [
            "DEFINE -> CLASSIFY ACTOR / THREAT",
            "DIAGNOSE -> ATTRIBUTE + VULNERABILITY + DOCTRINE GAP",
            "MAP -> STATE LEAD + UNION AID + COORDINATION",
            "CALIBRATE -> SECURITY + DEVELOPMENT + RIGHTS",
            "QUALIFY -> EVIDENCE RUNG, ATTRIBUTION AND END-STATE",
        ], ["Area-management end-state", "Evidence-rung discipline"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2020", "GS-III",
            "Area management to deny militant support and improve local perception.",
            "Audited neutral rendering of the routed demand; Discuss · 10 marks · 150 words. The exact printed stem should be taken from the OCR-searchable official paper during final assembly.",
            [6, 13, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2021", "GS-III",
            "Analyse the multidimensional challenges posed by external state and non-state actors to India's internal security.",
            "Verified routed demand; Analyse · 15 marks · 250 words.",
            [0, 2, 6, 7, 11, 19],
        ),
        common.make_pyq_solution(
            facts, "2026", "Prelims GS-I",
            "Zero FIR under BNSS and police jurisdiction for reported offences.",
            "Provisional routed objective concept; no answer letter is recorded or inferred.",
            [8, 17, 19],
        ),
    ]
    return common.topic(
        1, "Internal-Security Foundations and Governance",
        "01_Internal-Security-Foundations-and-Governance", facts, traps,
        [
            (10, "Distinguish internal security from external security in India's federal setting.", [0, 1, 8, 9, 10]),
            (10, "Explain the utility of the threat-vulnerability-capability framework for internal-security policy.", [5, 6, 14, 15]),
            (15, "Analyse the multidimensional challenges posed by external state and non-state actors to India's internal security.", [0, 2, 6, 7, 11, 19]),
            (15, "Discuss why Centre-State coordination is a structural requirement in internal-security governance.", [1, 8, 9, 10, 11, 15]),
            (20, "Evaluate India's eight-element internal-security doctrine as a framework for calibrated security, development and rights-based response.", [3, 4, 5, 12, 13, 14, 16, 19]),
            (20, "Compare coercive, accommodative and preventive approaches to internal-security challenges and propose a legitimate end-state.", [3, 7, 12, 13, 14, 16, 19]),
        ],
        titles, routes, panels,
        [
            "Kautilya", "territorial integrity", "eight-element",
            "governance deficit", "Threat", "Vulnerability", "Capability",
            "State List Entry 1", "State List Entry 2", "Union List Entry 2A",
            "Article 355", "in aid of the civil power", "Zero FIR",
            "Official Secrets Act", "Arms Act",
        ],
        "The audited ledgers route the 2020 area-management framework, the 2021 external-state/non-state actor demand and the provisional 2026 Zero FIR concept to this owner. Cross-topic wording is labelled rather than silently reassigned.",
        pyqs, LIVE_ATTEMPTS,
        "The MHA Annual Report 2024-25 is the dated institutional anchor. It confirms State primacy for public order and police alongside Article 355-based Union assistance; it does not convert assistance into ordinary central policing or supply an outcome statistic.",
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "FOUNDATIONAL DEFINITIONS AND THREAT GRAMMAR",
            "FEDERAL COMPETENCE AND RESPONSE CALIBRATION",
            "AREA-MANAGEMENT AND ANSWER-WRITING SPINE",
            "CURRENT INSTITUTIONAL AND EVIDENCE-RUNG FIREWALL",
        ),
        register_answer_spine=[
            "DEFINE INTERNAL SECURITY AND ITS PROTECTED ATTRIBUTES",
            "CLASSIFY THE THREAT THROUGH KAUTILYA AND ACTOR-MEANS-OBJECTIVE",
            "SEPARATE THREAT VULNERABILITY CAPABILITY AND CONSEQUENCE",
            "DIAGNOSE THE WEAKEST OF THE EIGHT DOCTRINE ELEMENTS",
            "STATE STATE-LIST PRIMACY AND UNION AID UNDER ENTRY 2A ARTICLE 355",
            "CALIBRATE COERCION ACCOMMODATION DEVELOPMENT AND RIGHTS",
            "TEST WHETHER PEOPLE ADMINISTRATION AND TRUST CAN HOLD",
            "CONCLUDE AT THE LAST VERIFIED EVIDENTIARY RUNG",
        ],
    )


TOPIC_01 = _build()
