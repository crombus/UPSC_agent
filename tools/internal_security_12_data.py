"""Authored learner-v2 data for Internal Security Topic 12."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/sites/default/files/"
        "AnnualReport_2024_25_English.pdf and "
        "https://www.mha.gov.in/en/about-us/central-armed-police-forces — "
        "attempted 2026-09-04 for the current CAPF taxonomy, force status and "
        "NATGRID references; direct retrieval returned 403. No strength, "
        "deployment, leadership or operational-readiness figure is imported."
    ),
    (
        "https://nia.gov.in/about-us and https://www.mha.gov.in/ — fetched and "
        "attempted 2026-09-04. The official NIA page confirms creation under "
        "the NIA Act in a concurrent-jurisdiction framework and describes NIA "
        "as a central counter-terrorism law-enforcement agency; its displayed "
        "case statistics are dated 5 February 2020 and are excluded."
    ),
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the NIA Act, "
        "Protection of Human Rights Act Section 19, BNSS custody safeguards and "
        "force statutes; direct retrieval returned 403. Only owner-audited legal "
        "distinctions are used, and statutory power is not treated as field "
        "practice or accountability outcome."
    ),
    (
        "https://www.mha.gov.in/en/commoncontent/intelligence-bureau and "
        "https://www.nsg.gov.in/about-us — attempted 2026-09-04 for public "
        "institutional descriptions; the MHA page returned 403 and the NSG page "
        "had a transport-level failure. No classified detail, capability claim, "
        "deployment pattern, vulnerability or current operation is inferred."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Constitutional allocation", "Public order and police are State List Entries 1 and 2, while Union List Entry 2A permits deployment of Union armed forces in aid of civil power and Article 355 places a protective duty on the Union; support does not erase State responsibility."),
        ("Force-category boundary", "The Armed Forces are military services, CAPFs are Union police and security forces, State police exercise ordinary public-order and investigation powers, and specialised agencies have narrower statutory or executive functions."),
        ("Current CAPF map", "MHA's owner-audited list comprises Assam Rifles, BSF, CISF, CRPF, ITBP, NSG and SSB; SPG, RPF and the Indian Coast Guard have separate administrative arrangements and must not be added to that list."),
        ("Force-mandate fingerprints", "BSF, ITBP and SSB have designated border-guarding roles, CRPF supports internal security and public order, and CISF protects specified installations and sectors; each mandate has legal and operational boundaries."),
        ("Dual-and-specialised forces", "Assam Rifles is administratively under MHA and operates under Army command, while the Indian Coast Guard is an armed force under the Ministry of Defence; command arrangement and task do not make either an ordinary State police force."),
        ("Home Guards status", "Home Guards are auxiliary police and public-support organisations governed by respective State or Union Territory Acts and Rules, not one all-India Central Home Guards Act; Border Wing Home Guards exist in specified border contexts."),
        ("Army Corps PYQ facts", "For the provisionally keyed 2026 route, the owner records III Corps at Dimapur, IV Corps at Tezpur, XIV Corps at Leh and XXXIII Corps at Sukna; these factual matches do not disclose deployment, readiness or operations."),
        ("State-police primacy", "State police are first responders for public order, complaint registration, local intelligence, evidence preservation, witnesses and investigation; Central forces and agencies supplement rather than eliminate this local chain."),
        ("Intelligence cycle", "The intelligence cycle moves through direction, collection, processing, analysis, dissemination and feedback; volume of collection does not establish relevance, accuracy, lawful use or operational action."),
        ("IB-R&AW boundary", "IB supplies domestic intelligence and R&AW external intelligence within their public institutional roles; neither is a police investigating body or has a general power of arrest."),
        ("MAC-SMAC coordination", "The Multi Agency Centre and Subsidiary MACs are intelligence-sharing coordination mechanisms under the IB framework; a shared lead is not an FIR, admissible evidence or operational command."),
        ("NATGRID boundary", "NATGRID is a data-integration and authorised-access tool connecting existing government data sources for security use; it does not independently collect all intelligence, investigate, arrest or adjudicate."),
        ("NIA mandate", "NIA is a statutory Central investigative and prosecuting agency for scheduled offences in a concurrent-jurisdiction framework; it is not the domestic intelligence collector and does not replace every State-police case."),
        ("NSG mandate", "NSG is a specialised counter-terrorism and hostage-rescue response force within its mandate, whereas NIA investigates scheduled offences after or alongside response; tactical response and legal case-building are different functions."),
        ("Intelligence-evidence chain", "A disciplined chain separates intelligence lead, preventive action, incident response, lawful search or seizure, forensic preservation, investigation, charge, prosecution and judicial finding; intelligence may guide action but is not automatically trial evidence."),
        ("Federal coordination", "Internal security requires Centre-State and inter-agency coordination through lawful requisition, information sharing, agreed command, deconfliction and post-operation handoff; centralisation is not a substitute for functional clarity."),
        ("Police-reform architecture", "Prakash Singh v. Union of India set seven reform benchmarks including State Security Commissions, tenure protections, separation of investigation, Police Establishment Boards, Police Complaints Authorities and a National Security Commission."),
        ("Use-of-force legality", "Use of force must rest on legal authority and satisfy necessity, proportionality, precaution, command responsibility, record and review; a mandate or disturbed-area status never proves that every act within it is lawful."),
        ("Rights-accountability map", "Article 33 permits Parliament to restrict specified service rights, D.K. Basu safeguards arrest and custody, and Section 19 of the Protection of Human Rights Act limits the NHRC's armed-forces procedure; each safeguard's implementation must be assessed separately."),
        ("Technology-evidence end-state", "Security technology needs defined purpose, authorised access, data minimisation, accuracy checks, audit logs, human review, retention limits, cybersecurity and remedy; attribution, intelligence assessment, arrest, charge and conviction remain distinct statuses."),
    ]
    traps = [
        "Do not use Armed Forces, CAPFs, State police and specialised agencies as synonyms.",
        "Do not add SPG, RPF or the Coast Guard to MHA's CAPF list.",
        "Do not infer exclusive command or operational readiness from a force's mandate.",
        "Do not treat Home Guards as governed by one all-India Central Act.",
        "Do not add operational meaning to the Army Corps headquarters PYQ facts.",
        "Do not present a Central force or agency as a substitute for State-police primacy.",
        "Do not conflate intelligence collection, sharing, data integration and investigation.",
        "Do not describe MAC, NATGRID or IB as arresting or prosecuting bodies.",
        "Do not treat NSG response and NIA investigation as the same function.",
        "Do not convert an intelligence lead or attribution assessment into admissible evidence.",
        "Do not treat legal power or technology deployment as proof of proportionate use.",
        "Do not publish classified detail, deployment patterns, collection methods or operational vulnerabilities.",
    ]
    titles = [
        "Constitutional allocation and cooperative federalism",
        "Armed Forces CAPFs State police and specialised agencies",
        "Seven-force CAPF map and separate organisations",
        "Border internal-security and installation mandates",
        "Assam Rifles Coast Guard and command arrangements",
        "Home Guards and Border Wing Home Guards",
        "Army Corps routed factual anchors",
        "State-police first-response and investigation primacy",
        "Intelligence cycle collection analysis and feedback",
        "IB R&AW and absence of arrest power",
        "MAC SMAC and intelligence sharing",
        "NATGRID data integration and safeguards",
        "NIA investigation NSG response and Special Courts",
        "Intelligence lead evidence attribution and prosecution",
        "Police reform use of force rights and accountability",
    ]
    routes = [
        "Start with Entries 1, 2 and 2A plus Article 355 and preserve aid-to-civil-power.",
        "Classify the institution before stating its task or power.",
        "Use the current seven-force list and name separate organisations.",
        "Write administrative home, primary mandate and operational boundary.",
        "Explain dual reporting without revealing operational detail.",
        "State the State or UT legal basis and auxiliary status.",
        "Use only the headquarters-location fact and provisional-key caveat.",
        "Show why local response, evidence and witnesses cannot be centralised away.",
        "Assess direction, quality, analysis, dissemination and feedback separately.",
        "Keep domestic and external intelligence distinct from police powers.",
        "Treat sharing as coordination, not investigation or command.",
        "Pair authorised integration with purpose, access, audit and remedy safeguards.",
        "Separate tactical response, statutory investigation and prosecution.",
        "State each evidentiary rung and attribution confidence.",
        "Conclude with functional reform, lawful force, oversight and technology safeguards.",
    ]
    panels = [
        common.panel("Constitutional security map", "institution-map", [
            "STATE LIST 1 -> PUBLIC ORDER",
            "STATE LIST 2 -> POLICE",
            "UNION LIST 2A -> UNION FORCE IN AID OF CIVIL POWER",
            "ARTICLE 355 -> UNION PROTECTIVE DUTY",
            "RULE -> cooperation, not automatic substitution",
        ], ["Constitutional allocation"]),
        common.panel("Force-category hierarchy", "hierarchy", [
            "ARMED FORCES -> MILITARY SERVICES",
            "CAPFs -> UNION POLICE / SECURITY FORCES",
            "STATE POLICE -> PUBLIC ORDER / CRIME / INVESTIGATION",
            "SPECIALISED AGENCY -> narrow response, intelligence or investigation role",
        ], ["Force-category boundary"]),
        common.panel("Current CAPF firewall", "comparison-table", [
            "CAPFs -> ASSAM RIFLES / BSF / CISF / CRPF / ITBP / NSG / SSB",
            "SEPARATE -> SPG / RPF / INDIAN COAST GUARD",
            "TRAP -> historical CPMF labels do not control current taxonomy",
            "RULE -> verify current strength and leadership separately",
        ], ["Current CAPF map"]),
        common.panel("Mandate fingerprint map", "institution-map", [
            "BSF / ITBP / SSB -> DESIGNATED BORDER ROLES",
            "CRPF -> INTERNAL SECURITY / PUBLIC-ORDER SUPPORT",
            "CISF -> INSTALLATIONS / SPECIFIED SECTORS",
            "ASSAM RIFLES -> DUAL ARRANGEMENT",
            "COAST GUARD -> MoD MARITIME FORCE",
        ], ["Force-mandate fingerprints", "Dual-and-specialised forces"]),
        common.panel("Auxiliary and formation facts", "comparison-table", [
            "HOME GUARDS -> STATE / UT ACTS + AUXILIARY ROLE",
            "BORDER WING -> specified border-support contexts",
            "III / IV / XIV / XXXIII CORPS -> DIMAPUR / TEZPUR / LEH / SUKNA",
            "LIMIT -> no deployment or readiness inference",
        ], ["Home Guards status", "Army Corps PYQ facts"]),
        common.panel("State-police primacy chain", "process-flow", [
            "LOCAL INTELLIGENCE / COMPLAINT",
            "-> FIRST RESPONSE / PUBLIC ORDER",
            "-> EVIDENCE + WITNESS PRESERVATION",
            "-> INVESTIGATION / HANDOFF",
            "CENTRAL SUPPORT -> supplements each lawful stage",
        ], ["State-police primacy"]),
        common.panel("Intelligence cycle", "cycle", [
            "DIRECTION -> COLLECTION -> PROCESSING",
            "-> ANALYSIS -> DISSEMINATION -> FEEDBACK",
            "QUALITY TEST -> relevance / corroboration / timeliness",
            "RIGHTS TEST -> legality / purpose / access / review",
        ], ["Intelligence cycle"]),
        common.panel("Intelligence institution map", "comparison-table", [
            "IB -> DOMESTIC INTELLIGENCE",
            "R&AW -> EXTERNAL INTELLIGENCE",
            "MAC / SMAC -> SHARING COORDINATION",
            "NATGRID -> AUTHORISED DATA INTEGRATION",
            "NONE -> automatic FIR, arrest or conviction",
        ], ["IB-R&AW boundary", "MAC-SMAC coordination", "NATGRID boundary"]),
        common.panel("Response-investigation split", "comparison-table", [
            "NSG -> SPECIALISED TACTICAL RESPONSE",
            "NIA -> SCHEDULED-OFFENCE INVESTIGATION / PROSECUTION",
            "STATE POLICE -> LOCAL CASE / EVIDENCE / PUBLIC ORDER",
            "SPECIAL COURT -> JUDICIAL PROCESS",
        ], ["NIA mandate", "NSG mandate"]),
        common.panel("Intelligence-to-judgment ladder", "status-ladder", [
            "INTELLIGENCE LEAD",
            "-> PREVENTIVE / RESPONSE ACTION",
            "-> FORENSICALLY PRESERVED EVIDENCE",
            "-> INVESTIGATION / CHARGE / PROSECUTION",
            "-> JUDICIAL FINDING",
        ], ["Intelligence-evidence chain"]),
        common.panel("Rights and reform architecture", "systems-map", [
            "PRAKASH SINGH -> STRUCTURE / TENURE / COMPLAINTS",
            "USE OF FORCE -> LEGALITY / NECESSITY / PROPORTIONALITY",
            "D.K. BASU -> ARREST / CUSTODY SAFEGUARDS",
            "PHRA SECTION 19 -> NHRC ARMED-FORCES PROCEDURE",
            "ARTICLE 33 -> specified service-right restrictions",
        ], ["Police-reform architecture", "Use-of-force legality", "Rights-accountability map"]),
        common.panel("PYQ and accountable-security rail", "answer-spine", [
            "2023 GS-III -> CHALLENGES + INTELLIGENCE / INVESTIGATIVE ROLES",
            "2023 PRELIMS -> HOME GUARDS LEGAL-STATUS DISTINCTION",
            "2026 PRELIMS -> CORPS / HEADQUARTERS; PROVISIONAL KEY",
            "END -> SHARE / RESPOND / INVESTIGATE / PROSECUTE / REVIEW",
            "QUALIFY -> mandate, intelligence, evidence and outcome differ",
        ], ["Federal coordination", "Technology-evidence end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2023", "GS-III",
            "Internal security challenges faced by India and the role of Central Intelligence and Investigative Agencies tasked to counter them.",
            "Routed to this owner; Discuss · 15 marks · 250 words.",
            [0, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 19],
        ),
        common.make_pyq_solution(
            facts, "2023", "Prelims GS-I",
            "Home Guards legal basis, auxiliary roles and Border Wing Home Guard battalions.",
            "Routed objective concept card; the official key is unavailable locally, so no answer letter is inferred.",
            [1, 5, 7, 15],
        ),
        common.make_pyq_solution(
            facts, "2026", "Prelims GS-I",
            "Indian Army Corps formations matched with their operational headquarters locations.",
            "Routed objective concept card; the local Set-A key is provisional, so facts are recorded without inferring an answer option.",
            [1, 6],
        ),
    ]
    return common.topic(
        12, "Security Forces, Intelligence Coordination and Rights",
        "12_Security-Forces-Intelligence-Coordination-and-Rights", facts, traps,
        [
            (10, "Distinguish the Armed Forces, CAPFs, State police and specialised agencies by administrative home, primary function and legal boundary.", [0, 1, 2, 3, 4]),
            (10, "Explain why MAC, NATGRID and NIA perform different functions in India's security architecture.", [8, 9, 10, 11, 12, 14]),
            (15, "Discuss the role of Central Intelligence and Investigative Agencies in countering internal-security threats while preserving State-police primacy.", [0, 7, 8, 9, 10, 11, 12, 14, 15]),
            (15, "Assess India's federal coordination architecture across State police, CAPFs, NIA, NSG and intelligence-sharing mechanisms.", [0, 1, 3, 7, 10, 12, 13, 15]),
            (20, "Critically evaluate police reform, use-of-force legality and human-rights accountability as operational security capabilities.", [7, 15, 16, 17, 18, 19]),
            (20, "Examine how security technology and intelligence coordination can be strengthened without collapsing attribution, intelligence leads and admissible evidence.", [8, 10, 11, 14, 15, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "State List Entry 1", "Entry 2", "Union List Entry 2A",
            "Article 355", "CAPF", "Assam Rifles", "BSF", "CISF",
            "CRPF", "ITBP", "NSG", "SSB", "State police", "IB",
            "R&AW", "MAC", "SMAC", "NATGRID", "NIA",
            "Prakash Singh", "Police Complaints Authority", "D.K. Basu",
            "Section 19", "Article 33", "Home Guards", "III Corps",
        ],
        "The three conservative routed cards are the 2023 GS-III intelligence-agency demand, the 2023 Prelims Home Guards question and the 2026 provisional-key Army Corps question. Objective answer letters are not inferred, and the Corps card records only owner-audited public headquarters facts.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts on 2026-09-04 confirmed the NIA's public statutory and concurrent-jurisdiction description but exposed only dated 2020 statistics, which are excluded. MHA, India Code, IB and NSG pages were blocked or unavailable, so no current force strength, leadership, NATGRID status, deployment, capability or accountability-outcome claim is used.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "CONSTITUTIONAL ALLOCATION, FORCE CATEGORIES AND MANDATE MAP",
            "INTELLIGENCE, DATA, RESPONSE, INVESTIGATION AND EVIDENCE FIREWALLS",
            "HOME GUARDS, CORPS FACTS AND THREE CONSERVATIVE PYQ SPINES",
            "FEDERAL COORDINATION, POLICE REFORM, RIGHTS AND TECHNOLOGY SAFEGUARDS",
        ),
        register_answer_spine=[
            "FIX STATE LIST 1 2 UNION LIST 2A AND ARTICLE 355",
            "CLASSIFY ARMED FORCE CAPF STATE POLICE OR SPECIALISED AGENCY",
            "WRITE ADMINISTRATIVE HOME PRIMARY TASK AND BOUNDARY",
            "SEPARATE IB R&AW MAC SMAC NATGRID NIA AND NSG",
            "TRACE INTELLIGENCE RESPONSE EVIDENCE INVESTIGATION AND JUDGMENT",
            "PRESERVE STATE-POLICE PRIMACY AND COOPERATIVE FEDERALISM",
            "APPLY PRAKASH SINGH USE-OF-FORCE D.K. BASU AND PHRA SAFEGUARDS",
            "CONCLUDE WITH PURPOSE ACCESS AUDIT HUMAN REVIEW REMEDY AND RIGHTS",
        ],
    )


TOPIC_12 = _build()
