"""Authored learner-v2 data for Internal Security Topic 07."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the "
        "Territorial Waters, Continental Shelf, Exclusive Economic Zone and "
        "Other Maritime Zones Act, 1976; Coast Guard Act, 1978; SUA Act, 2002; "
        "and Anti-Maritime Piracy Act, 2022. Direct retrieval returned 403, so "
        "only owner-audited statutory distinctions are used."
    ),
    (
        "https://www.mha.gov.in/en/divisionofmha/border-management-ii-division "
        "— attempted 2026-09-04 for the Coastal Security Scheme and marine-"
        "police capacity framework; direct retrieval returned 403. No current "
        "asset, station, vessel, training or coverage count is imported."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=1996947 — searched and "
        "attempted 2026-09-04; the official PIB search result identifies a "
        "National Academy of Coastal Policing foundation course, while direct "
        "retrieval returned 403. The module uses it only as evidence that "
        "specialised coastal-police training exists, not as proof of readiness."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=1952972 — searched and "
        "attempted 2026-09-04 for official coastal-security and maritime-domain-"
        "awareness material; direct retrieval returned 403. No unverified "
        "partner, liaison-officer, exercise or operational-result count is used."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Maritime-coastal distinction", "Maritime security covers sea lanes, offshore interests, the EEZ and high seas, while coastal security is its near-shore subset protecting the coast and maritime approaches from sea-originating threats."),
        ("Maritime-zone ladder", "India's zone framework distinguishes the territorial sea to 12 nautical miles, contiguous zone to 24 nautical miles, Exclusive Economic Zone to 200 nautical miles, and the high seas beyond."),
        ("Threat-category map", "Relevant challenges include sea-borne terrorism, piracy or armed robbery, smuggling and trafficking, infiltration or illegal migration, illegal fishing and fishermen straying, and physical or cyber disruption of ports."),
        ("Navy role", "The Indian Navy's principal security contribution lies in sea control, surveillance, offshore and sea-lane protection and the wider maritime domain; near-shore tasking must not erase its broader defence role."),
        ("Coast Guard role", "The Indian Coast Guard, under the Ministry of Defence and Coast Guard Act, protects maritime and national interests in India's maritime zones and performs security, law-enforcement, safety and coordination functions within its mandate."),
        ("Marine Police role", "State Marine Police conduct close coastal patrolling and investigation within State jurisdiction, supported through the Coastal Security Scheme and coordinated with the Coast Guard and Navy."),
        ("Layered-architecture boundary", "Navy, Coast Guard and Marine Police form a layered arrangement with connected but distinct mandates; the architecture does not make any one institution the sole owner of every maritime incident."),
        ("NCSMCS coordination", "The National Committee for Strengthening Maritime and Coastal Security is the apex inter-agency coordination mechanism headed by the Cabinet Secretary."),
        ("Joint Operations Centres", "Joint Operations Centres at Mumbai, Visakhapatnam, Kochi and Port Blair are jointly manned coordination nodes linking the Navy, Coast Guard and Marine Police."),
        ("NC3I function", "The National Command Control Communication and Intelligence Network collates and disseminates vessel and sensor information to strengthen coastal maritime-domain awareness."),
        ("IMAC-IFC boundary", "The Information Management and Analysis Centre supports India's maritime picture, while the Navy-hosted IFC-IOR adds partner information-sharing for the Indian Ocean Region; awareness cooperation is not itself interdiction."),
        ("Awareness-interdiction distinction", "Radar, AIS, vessel reporting and fused information answer what is at sea; vessels, trained crews, lawful boarding, investigation and prosecution determine whether the State can act."),
        ("Surveillance-system role", "Coastal radar, Automatic Identification System receivers, vessel traffic systems and related reporting improve identification and tracking but depend on maintenance, compliance and response capacity."),
        ("Fishing-community interface", "Fishing communities are livelihood stakeholders and early-warning partners; registration, identification, safety communication and protected reporting should build trust rather than presume criminality."),
        ("Port-security convergence", "Ports combine physical access, cargo, customs, industrial assets, operational technology and data systems, so continuity planning must integrate physical security, cyber resilience and recovery."),
        ("Coastal Security Scheme", "The Coastal Security Scheme supports marine-police stations, jetties, boats, training and surveillance capacity; sanctioned infrastructure is not proof of staffing, serviceability or outcomes."),
        ("Three-statute legal map", "The Maritime Zones Act establishes zone rights, the SUA Act, 2002 addresses unlawful acts against navigation and fixed platforms, and the Anti-Maritime Piracy Act, 2022 creates a piracy-specific framework."),
        ("Piracy-location boundary", "Piracy is a high-seas or applicable EEZ offence under the piracy framework; violence in territorial or internal waters is not automatically piracy and may follow other criminal or maritime statutes."),
        ("Reactive-buildout lesson", "India's coastal-security architecture expanded through successive vulnerability-driven reforms, especially after the 2008 Mumbai attacks; later institution-building must be assessed for capacity and coordination, not announced existence alone."),
        ("Resilient end-state", "Maritime security requires zone-specific mandate clarity, interoperable awareness and response, trained coastal police, port resilience, community partnership, lawful enforcement and repeated preparedness and recovery exercises."),
    ]
    traps = [
        "Do not use maritime security and coastal security as synonyms.",
        "Do not confuse territorial sea, contiguous zone, EEZ and high seas.",
        "Do not describe the Navy as the sole coastal-security authority.",
        "Do not transfer a Coast Guard mandate to State Marine Police or vice versa.",
        "Do not infer readiness from a force's statutory existence.",
        "Do not turn a simplified three-tier diagram into exclusive jurisdiction in every incident.",
        "Do not equate an apex committee with operational command at sea.",
        "Do not expose patrol patterns, sensor gaps or exploitable port vulnerabilities.",
        "Do not equate a fused maritime picture with boarding or prosecution capacity.",
        "Do not treat fishing communities collectively as suspects.",
        "Do not use piracy, maritime terrorism and territorial-water crime interchangeably.",
        "Do not infer outcomes from sanctioned stations, boats, radars, exercises or training seats.",
    ]
    titles = [
        "Maritime and coastal security distinction",
        "Territorial sea contiguous zone EEZ and high seas",
        "Threat categories and sea-trade exposure",
        "Navy role and wider maritime defence",
        "Coast Guard mandate and coordination",
        "State Marine Police and Coastal Security Scheme",
        "Layered architecture and command clarity",
        "NCSMCS and Joint Operations Centres",
        "NC3I IMAC and IFC-IOR information sharing",
        "Maritime-domain awareness versus interdiction",
        "Coastal surveillance and vessel identification",
        "Fishing communities safety livelihood and reporting",
        "Ports as physical and cyber security nodes",
        "Maritime Zones SUA and Piracy Acts",
        "Reactive build-out resilience and way forward",
    ]
    routes = [
        "Define the broader maritime domain before the coastal subset.",
        "Fix the zone before assigning institution or law.",
        "Link each challenge to location, actor, capability and consequence.",
        "Protect sea-control and SLOC roles from near-shore mandate conflation.",
        "State Coast Guard functions without converting coordination into sole ownership.",
        "Separate infrastructure, staffing, training, serviceability and outcome.",
        "Use layering to explain cooperation and identify overlap risks.",
        "Distinguish apex policy coordination from operational incident command.",
        "Map domestic and partner information flows without claiming enforcement power.",
        "Separate detection, identification, decision, interception and adjudication.",
        "Treat technology as maintained capability, not a procurement list.",
        "Frame fishers as partners and rights-bearing livelihood communities.",
        "Integrate cargo, access, operational technology, cyber continuity and recovery.",
        "Choose the statute only after fixing offence and maritime zone.",
        "Conclude with anticipatory resilience, drills, recovery and audited command clarity.",
    ]
    panels = [
        common.panel("Maritime-coastal nesting", "hierarchy", [
            "MARITIME SECURITY",
            "|-- HIGH SEAS / SLOCs / OFFSHORE INTERESTS",
            "|-- EEZ AWARENESS / ENFORCEMENT",
            "`-- COASTAL SECURITY -> near-shore subset",
            "RULE -> subset is not synonym",
        ], ["Maritime-coastal distinction"]),
        common.panel("Maritime-zone ladder", "status-ladder", [
            "0-12 nm -> TERRITORIAL SEA",
            "12-24 nm -> CONTIGUOUS ZONE",
            "TO 200 nm -> EXCLUSIVE ECONOMIC ZONE",
            "BEYOND -> HIGH SEAS",
            "FIX ZONE -> THEN INSTITUTION + LAW",
        ], ["Maritime-zone ladder"]),
        common.panel("Threat-to-response matrix", "matrix", [
            "SEA-BORNE TERROR | INTELLIGENCE + INTERDICTION + SUA",
            "PIRACY / ROBBERY | ZONE + PIRACY / OTHER LAW",
            "SMUGGLING / TRAFFICKING | COAST GUARD / CUSTOMS / POLICE",
            "PORT CYBER / SABOTAGE | PHYSICAL + DIGITAL RESILIENCE",
        ], ["Threat-category map", "Port-security convergence"]),
        common.panel("Institutional layers", "institution-map", [
            "NAVY -> wider defence / sea control / SLOCs",
            "COAST GUARD -> maritime-zone security / law enforcement / coordination",
            "MARINE POLICE -> close coastal patrol / State investigation",
            "RULE -> connected mandates, not one undifferentiated force",
        ], ["Navy role", "Coast Guard role", "Marine Police role", "Layered-architecture boundary"]),
        common.panel("Coordination architecture", "systems-map", [
            "NCSMCS -> APEX POLICY COORDINATION",
            "JOCs -> MUMBAI / VISAKHAPATNAM / KOCHI / PORT BLAIR",
            "NC3I / IMAC -> DOMESTIC INFORMATION FUSION",
            "IFC-IOR -> PARTNER INFORMATION-SHARING LAYER",
        ], ["NCSMCS coordination", "Joint Operations Centres", "NC3I function", "IMAC-IFC boundary"]),
        common.panel("Awareness-to-action chain", "process-flow", [
            "DETECT -> IDENTIFY -> FUSE -> DECIDE",
            "-> INTERCEPT / BOARD UNDER LAWFUL AUTHORITY",
            "-> INVESTIGATE -> PROSECUTE / RECOVER",
            "TRAP -> awareness is not interdiction",
        ], ["Awareness-interdiction distinction", "Surveillance-system role"]),
        common.panel("Coastal-police capacity audit", "audit-ladder", [
            "SCHEME SANCTION",
            "-> STATION / JETTY / BOAT / TRAINING INPUT",
            "-> STAFFING + MAINTENANCE + SEA-TIME",
            "-> EXERCISE PERFORMANCE + VERIFIED RESPONSE",
            "RULE -> never skip from input to outcome",
        ], ["Coastal Security Scheme", "Marine Police role"]),
        common.panel("Fishing-community interface", "balance-scale", [
            "SECURITY VALUE -> LOCAL KNOWLEDGE / EARLY WARNING",
            "LIVELIHOOD NEED -> SAFE ACCESS / COMMUNICATION / DUE PROCESS",
            "TOOLS -> REGISTRATION / IDENTIFICATION / DISTRESS / REPORTING",
            "VERDICT -> partnership, not collective suspicion",
        ], ["Fishing-community interface"]),
        common.panel("Port-resilience map", "systems-map", [
            "WATERSIDE ACCESS + LANDSIDE ACCESS",
            "CARGO / CUSTOMS + INDUSTRIAL ASSETS",
            "OPERATIONAL TECHNOLOGY + DATA SYSTEMS",
            "CONTINUITY -> PREVENT / RESPOND / RECOVER / LEARN",
        ], ["Port-security convergence"]),
        common.panel("Maritime-law decision tree", "decision-tree", [
            "WHERE? -> TERRITORIAL / EEZ / HIGH SEAS",
            "WHAT ACT? -> PIRACY / TERROR / OTHER CRIME",
            "MARITIME ZONES ACT -> zone framework",
            "SUA ACT -> navigation / fixed-platform unlawful acts",
            "PIRACY ACT -> piracy-specific trigger",
        ], ["Three-statute legal map", "Piracy-location boundary"]),
        common.panel("Reactive-to-resilient timeline", "timeline", [
            "1977/1978 -> INDIAN COAST GUARD",
            "2005 -> COASTAL SECURITY SCHEME",
            "POST-26/11 -> JOCs / NETWORKED AWARENESS EXPANSION",
            "2022 -> ANTI-MARITIME PIRACY ACT",
            "NEXT -> anticipatory capacity + recovery",
        ], ["Reactive-buildout lesson"]),
        common.panel("PYQ and end-state rail", "answer-spine", [
            "2022 PRELIMS -> UNCLOS ZONE CONCEPT, CROSS-OWNED",
            "2022 MAINS -> ORGANISATIONAL / TECHNICAL / PROCEDURAL",
            "2025 MAINS -> SEA TRADE + CHALLENGES + WAY FORWARD",
            "END -> mandate + awareness + action + community + resilience",
        ], ["Resilient end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2022", "Prelims GS-I",
            "UNCLOS concepts concerning territorial sea, innocent passage and Exclusive Economic Zone provisions.",
            "Conservative cross-owned concept card; the central ledger routes the objective question to International Relations. No answer letter is recorded or inferred here.",
            [0, 1, 3, 4, 17],
        ),
        common.make_pyq_solution(
            facts, "2022", "GS-III",
            "Maritime security challenges in India and organisational, technical and procedural initiatives taken to improve maritime security.",
            "Printed stem inspected in the OCR-searchable official paper; Discuss · 10 marks · 150 words.",
            [0, 1, 2, 6, 7, 8, 9, 11, 12, 15, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "Why maritime security is vital for India's sea trade, maritime and coastal security challenges, and the way forward.",
            "Printed stem inspected in the OCR-searchable official paper; Discuss · 15 marks · 250 words.",
            [0, 1, 2, 3, 4, 5, 11, 13, 14, 15, 16, 18, 19],
        ),
    ]
    return common.topic(
        7, "Maritime and Coastal Security",
        "07_Maritime-and-Coastal-Security", facts, traps,
        [
            (10, "Distinguish maritime security from coastal security and map India's layered institutional architecture.", [0, 1, 3, 4, 5, 6]),
            (10, "Explain why maritime-domain awareness cannot be treated as interdiction capability.", [8, 9, 10, 11, 12]),
            (15, "Discuss maritime security challenges and the organisational, technical and procedural initiatives taken by India.", [1, 2, 6, 7, 8, 9, 12, 15, 16, 18]),
            (15, "Why is maritime security vital to protect India's sea trade? Discuss challenges and the way forward.", [0, 1, 2, 3, 4, 5, 11, 13, 14, 16, 19]),
            (20, "Critically evaluate the Navy-Coast Guard-Marine Police architecture with reference to command clarity and capacity.", [3, 4, 5, 6, 7, 8, 11, 15, 18, 19]),
            (20, "Assess how ports, fishing communities, maritime-domain awareness and legal modernisation can produce resilient coastal security.", [9, 10, 11, 12, 13, 14, 15, 16, 17, 19]),
        ],
        titles, routes, panels,
        [
            "coastal security", "maritime security", "territorial sea",
            "contiguous zone", "EEZ", "Indian Coast Guard",
            "Coast Guard Act", "Marine Police Force", "NC3I",
            "National Committee for Strengthening Maritime and Coastal Security",
            "Joint Operations Centres", "AIS",
            "IFC-IOR", "Coastal Security Scheme", "Maritime Zones Act",
            "SUA Act", "Anti-Maritime Piracy Act", "Sagar Kavach",
        ],
        "The audited ledgers route the 2022 maritime-security initiatives demand and the 2025 sea-trade, maritime/coastal challenge and way-forward demand here. OCR inspection confirmed both printed Mains stems. A 2022 UNCLOS Prelims concept is included only as a clearly labelled cross-owned zone-law card.",
        pyqs, LIVE_ATTEMPTS,
        "Live official attempts on 2026-09-04 confirmed no new operational readiness or outcome statistic. The module therefore uses stable owner-audited mandates and statutes, records the official coastal-police training search only as an institutional input, and requires dated Navy, Coast Guard, MHA, ports or police evidence for current performance claims.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "MARITIME ZONES, THREATS AND INSTITUTIONAL LAYERS",
            "AWARENESS, INTERDICTION, PORT AND FISHING-COMMUNITY FIREWALLS",
            "MARITIME LAW AND THREE CONSERVATIVE PYQ SPINES",
            "CAPACITY, COORDINATION, RECOVERY AND RESILIENT END-STATE",
        ),
        register_answer_spine=[
            "DEFINE COASTAL SECURITY AS A SUBSET OF MARITIME SECURITY",
            "FIX TERRITORIAL SEA CONTIGUOUS ZONE EEZ OR HIGH SEAS",
            "MAP NAVY COAST GUARD MARINE POLICE AND COORDINATION BODIES",
            "SEPARATE NC3I IMAC IFC-IOR AWARENESS FROM INTERDICTION",
            "TREAT FISHING COMMUNITIES AS PARTNERS AND LIVELIHOOD STAKEHOLDERS",
            "INTEGRATE PORT PHYSICAL CYBER CONTINUITY AND RECOVERY",
            "DISTINGUISH MARITIME ZONES SUA AND PIRACY ACT TRIGGERS",
            "CONCLUDE WITH TRAINING COMMAND CLARITY EXERCISES AND AUDITED CAPABILITY",
        ],
    )


TOPIC_07 = _build()
