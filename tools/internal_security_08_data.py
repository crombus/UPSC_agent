"""Authored learner-v2 data for Internal Security Topic 08."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the "
        "Information Technology Act, 2000 provisions on sections 66F, 69-70B "
        "and protected systems; direct retrieval returned 403. The module uses "
        "only owner-audited section functions and does not infer practice or "
        "outcomes from statutory power."
    ),
    (
        "https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf "
        "and https://www.pib.gov.in/ — fetched and searched 2026-09-04; the "
        "official CERT-In PDF was retrievable as an eight-page PDF stream. The "
        "owner-audited six-hour reporting rule is retained, while no incident, "
        "audit or compliance count is imported."
    ),
    (
        "https://i4c.mha.gov.in/ — fetched 2026-09-04; the official site "
        "identifies the Indian Cyber Crime Coordination Centre under the "
        "Ministry of Home Affairs and displays citizen cybercrime-awareness "
        "activity. The module does not turn awareness outputs into prevention, "
        "investigation or recovery outcomes."
    ),
    (
        "https://www.meity.gov.in/documents/act-and-policies/digital-personal-"
        "data-protection-rules-2025-gDOxUjMtQWa and https://i4c.mha.gov.in/ "
        "— searched and attempted 2026-09-04; the official MeitY search result "
        "confirmed notification of the DPDP Rules, 2025 on 13 November 2025 "
        "with staged commencement, while direct page retrieval returned 403. "
        "The module records notification and phase boundaries, not enforcement "
        "or adjudication outcomes."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("CIA security triad", "Cybersecurity seeks to preserve confidentiality, integrity and availability of information and systems; an event may affect one, two or all three."),
        ("Risk-chain grammar", "Cyber risk arises when a threat actor or event exploits a vulnerability and produces a consequence; policy can reduce exposure, vulnerability, impact and recovery time without eliminating hostile intent."),
        ("Cyber-incident chain", "A cyber incident is a technical security event handled through detection, containment, eradication, recovery and learning; reporting an incident does not prove a crime or foreign operation."),
        ("Cybercrime chain", "Cybercrime is a penal offence committed using or against digital systems and follows complaint or registration, investigation, electronic evidence, prosecution and adjudication."),
        ("Cyber-warfare boundary", "Cyber warfare refers to state-linked strategic cyber activity against another state; political attribution requires evidence beyond technical indicators and is not established merely by origin infrastructure."),
        ("Cyber-terrorism law", "Section 66F of the Information Technology Act defines cyber terrorism around specified acts and terror or sovereignty-related intent; the legal offence is distinct from generic hacking or cybercrime."),
        ("Attribution discipline", "Cyber attribution is graded across technical, operational, legal and political assessments; shared tools, compromised infrastructure and false flags make confident public attribution difficult."),
        ("CII definition", "Section 70 of the IT Act defines Critical Information Infrastructure by the debilitating consequence that incapacitation or destruction would have for national security, economy, public health or safety."),
        ("Protected-system boundary", "Section 70 permits the appropriate government to declare a computer resource affecting CII as a protected system; notification creates legal protection but does not prove resilience."),
        ("NCIIPC mandate", "Under Section 70A, the National Critical Information Infrastructure Protection Centre under NTRO is the national nodal agency for CII protection and coordination with protected-system entities."),
        ("CERT-In mandate", "Under Section 70B, CERT-In is the national cyber-incident response agency for alerts, advisories, coordination and emergency response; it is not the police investigator for every cybercrime."),
        ("I4C mandate boundary", "The Indian Cyber Crime Coordination Centre under MHA supports cybercrime reporting, coordination, capacity and investigation assistance, while State and Union Territory police retain crime-registration and investigation roles."),
        ("Sectoral-regulator layer", "Sectoral CERTs, regulators and CII-owning entities have domain-specific resilience responsibilities and must coordinate with CERT-In and NCIIPC rather than transfer all risk to one national body."),
        ("CERT-In directions", "CERT-In's Directions dated 28 April 2022 require specified cyber incidents to be reported within six hours of noticing them or being informed; reporting is an incident-response input, not proof of attribution."),
        ("IT Act powers map", "Sections 69, 69A and 69B concern interception or decryption, blocking public access and traffic-data monitoring respectively, each subject to its statutory purpose and prescribed procedure."),
        ("Section 66A status", "Section 66A was struck down by the Supreme Court in Shreya Singhal v. Union of India in 2015; it must not be cited as a current offence."),
        ("CyberDome role", "CyberDome is Kerala Police's collaborative cyber-security and cybercrime support initiative for expertise, research, forensics, awareness and police capacity; a State model is not the national incident-response architecture."),
        ("DPDP boundary and phases", "The DPDP Act, 2023 and Rules, 2025 create a personal-data-governance layer distinct from cybersecurity and CII protection; the Rules notified on 13 November 2025 have staggered commencement rather than full same-day operation."),
        ("Evidence-status firewall", "A detected event, CERT-In report, citizen complaint, FIR, technical assessment, arrest, charge-sheet, attribution statement, conviction and recovered service are separate evidentiary and operational rungs."),
        ("Resilience-first end-state", "Because prevention and attribution are imperfect, India needs identify-protect-detect-respond-recover-learn resilience, tested CII continuity, lawful evidence handling, sectoral accountability and proportionate rights safeguards."),
    ]
    traps = [
        "Do not treat confidentiality, integrity and availability as identical failures.",
        "Do not describe hostile intent alone as cyber risk.",
        "Do not equate a cyber incident with a registered cybercrime.",
        "Do not equate cybercrime, cyber warfare and cyber terrorism.",
        "Do not attribute a state operation solely from an IP address or server location.",
        "Do not call generic hacking cyber terrorism without Section 66F intent and conduct.",
        "Do not merge technical, legal and political attribution.",
        "Do not expose exploit steps, credentials, vulnerable targets or evasion methods.",
        "Do not confuse CII designation with operational resilience.",
        "Do not use CERT-In, NCIIPC, I4C and police as interchangeable institutions.",
        "Do not cite Section 66A as current law.",
        "Do not describe notified DPDP Rules as fully commenced or fully enforced.",
    ]
    titles = [
        "Confidentiality integrity and availability",
        "Threat vulnerability consequence and recovery",
        "Cyber incident versus cybercrime",
        "Cyber warfare cyber terrorism and attribution",
        "Section 66F and offence-intent boundary",
        "Critical Information Infrastructure and protected systems",
        "NCIIPC Section 70A mandate",
        "CERT-In Section 70B and incident directions",
        "I4C police and citizen-reporting chain",
        "Sectoral CERTs regulators and CII owners",
        "Sections 69 69A 69B and rights safeguards",
        "Section 66A and Shreya Singhal",
        "CyberDome as a State collaborative model",
        "DPDP data governance and phased commencement",
        "Evidence rungs and resilience-first end-state",
    ]
    routes = [
        "Name the affected security property before describing consequence.",
        "Use threat, vulnerability, capability, consequence and recovery as separate variables.",
        "Route technical response and penal investigation through different chains.",
        "State actor, intent, evidence status and attribution confidence separately.",
        "Apply the statutory elements before using the cyber-terrorism label.",
        "Define CII by consequence and distinguish notification from resilience.",
        "Keep NCIIPC focused on CII protection and coordination.",
        "Keep CERT-In focused on incident response, directions and advisories.",
        "Show citizen reporting, police investigation and I4C coordination as distinct roles.",
        "Assign preventive and continuity duties to the relevant sectoral owner.",
        "Name the power, purpose, procedure and proportionality safeguard.",
        "Correct obsolete-law options immediately.",
        "Evaluate utility, scalability, privacy and institutional limits.",
        "Separate personal-data governance from system and CII security.",
        "Conclude at the last verified rung and prioritise tested recovery.",
    ]
    panels = [
        common.panel("CIA impact map", "triad", [
            "CONFIDENTIALITY -> unauthorised disclosure",
            "INTEGRITY -> unauthorised alteration / trust loss",
            "AVAILABILITY -> disruption / denial of service",
            "RULE -> identify the property before the remedy",
        ], ["CIA security triad"]),
        common.panel("Cyber-risk chain", "process-flow", [
            "THREAT ACTOR / EVENT",
            "-> EXPLOITS VULNERABILITY",
            "-> OPERATIONAL / SOCIAL CONSEQUENCE",
            "CAPABILITY -> prevent / contain / recover / learn",
        ], ["Risk-chain grammar"]),
        common.panel("Incident-crime-operation matrix", "comparison-table", [
            "INCIDENT -> CERT-In / entity -> contain and recover",
            "CRIME -> police / I4C support -> investigate and prosecute",
            "WARFARE -> state-linked strategic activity -> graded attribution",
            "TERRORISM -> Section 66F conduct + intent",
        ], ["Cyber-incident chain", "Cybercrime chain", "Cyber-warfare boundary", "Cyber-terrorism law"]),
        common.panel("Attribution confidence ladder", "status-ladder", [
            "TECHNICAL INDICATOR",
            "-> OPERATIONAL PATTERN / INFRASTRUCTURE CONTROL",
            "-> LEGAL EVIDENCE",
            "-> POLITICAL ATTRIBUTION",
            "RULE -> false flags and compromised systems require qualification",
        ], ["Attribution discipline"]),
        common.panel("IT Act CII ladder", "institution-map", [
            "SECTION 70 -> CII / PROTECTED SYSTEM",
            "SECTION 70A -> NCIIPC / CII PROTECTION",
            "SECTION 70B -> CERT-In / INCIDENT RESPONSE",
            "TRAP -> designation and incident handling are not the same function",
        ], ["CII definition", "Protected-system boundary", "NCIIPC mandate", "CERT-In mandate"]),
        common.panel("Cybercrime governance chain", "process-flow", [
            "CITIZEN / ENTITY REPORT",
            "-> POLICE REGISTRATION / INVESTIGATION",
            "-> I4C COORDINATION / CAPACITY SUPPORT",
            "-> ELECTRONIC EVIDENCE -> PROSECUTION / ADJUDICATION",
        ], ["Cybercrime chain", "I4C mandate boundary", "Evidence-status firewall"]),
        common.panel("Sectoral-resilience system", "systems-map", [
            "CII OWNER -> asset inventory / continuity / controls",
            "SECTOR REGULATOR / CERT -> domain standards / response",
            "NCIIPC -> CII coordination",
            "CERT-In -> national incident coordination",
            "RULE -> accountability stays distributed but interoperable",
        ], ["Sectoral-regulator layer"]),
        common.panel("CERT-In reporting boundary", "timeline", [
            "28 APR 2022 -> DIRECTIONS",
            "NOTICE OF SPECIFIED INCIDENT",
            "-> REPORT WITHIN SIX HOURS",
            "-> CONTAIN / COORDINATE / RECOVER",
            "NOT PROVED -> crime, culprit or foreign attribution",
        ], ["CERT-In directions"]),
        common.panel("Cyber-law powers firewall", "comparison-table", [
            "SECTION 69 -> intercept / monitor / decrypt",
            "SECTION 69A -> block public access",
            "SECTION 69B -> monitor / collect traffic data",
            "SECTION 66A -> STRUCK DOWN IN 2015",
            "RULE -> purpose + procedure + proportionality",
        ], ["IT Act powers map", "Section 66A status"]),
        common.panel("CyberDome model", "hub-and-spoke", [
            "KERALA POLICE HUB",
            "-> SPECIALISTS / INDUSTRY / ACADEMIA",
            "-> RESEARCH / FORENSICS / AWARENESS / CAPACITY",
            "LIMIT -> State collaboration is not CERT-In or NCIIPC",
        ], ["CyberDome role"]),
        common.panel("DPDP-versus-cybersecurity", "comparison-table", [
            "DPDP -> PERSONAL DATA / FIDUCIARY OBLIGATIONS / BOARD",
            "IT ACT / CERT-In -> INCIDENTS / OFFENCES / RESPONSE",
            "NCIIPC -> CII PROTECTION",
            "13 NOV 2025 -> RULES NOTIFIED; COMMENCEMENT STAGGERED",
        ], ["DPDP boundary and phases"]),
        common.panel("PYQ and resilience rail", "answer-spine", [
            "2019 -> CYBERDOME UTILITY + LIMIT",
            "2021 -> CROSS-BORDER IMPACT + DEFENSIVE RESILIENCE",
            "2022 -> ELEMENTS + CHALLENGES + STRATEGY ASSESSMENT",
            "END -> IDENTIFY / PROTECT / DETECT / RESPOND / RECOVER / LEARN",
            "QUALIFY -> evidence rung and attribution confidence",
        ], ["Evidence-status firewall", "Resilience-first end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2019", "GS-III",
            "What CyberDome is and how it can help control internet crimes in India.",
            "Printed stem inspected in the OCR-searchable official paper; Explain · 10 marks · 150 words.",
            [2, 3, 10, 11, 12, 16, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2021", "GS-III",
            "Impact of cross-border cyber attacks on India's internal security and defensive measures against sophisticated attacks.",
            "Printed stem inspected in the OCR-searchable official paper; Analyse/Discuss · 10 marks · 150 words.",
            [0, 1, 2, 4, 6, 7, 9, 10, 12, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2022", "GS-III",
            "Elements and challenges of cyber security and the extent to which India has developed a comprehensive National Cyber Security Strategy.",
            "The routing ledger records official-scan verification; Examine · 15 marks · 250 words.",
            [0, 1, 2, 3, 4, 7, 9, 10, 11, 12, 13, 17, 18, 19],
        ),
    ]
    return common.topic(
        8, "Cyber Security, CII and Cybercrime",
        "08_Cyber-Security-CII-and-Cybercrime", facts, traps,
        [
            (10, "Distinguish a cyber incident from a cybercrime and explain the correct institutional response chain.", [0, 1, 2, 3, 10, 11, 18]),
            (10, "Explain CyberDome's utility and limits as a State-level collaborative model.", [2, 3, 11, 12, 16, 18]),
            (15, "Analyse the impact of cross-border cyber attacks on internal security and propose defensive measures.", [0, 1, 2, 4, 6, 7, 9, 10, 12, 18, 19]),
            (15, "Examine India's institutional architecture for Critical Information Infrastructure protection and cybercrime response.", [7, 8, 9, 10, 11, 12, 13, 18, 19]),
            (20, "Critically assess whether India's cyber-security architecture amounts to a comprehensive national strategy.", [0, 1, 6, 7, 9, 10, 11, 12, 13, 14, 17, 18, 19]),
            (20, "Evaluate the relationship among cybersecurity, CII protection, cybercrime enforcement and personal-data governance.", [2, 3, 5, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Confidentiality", "Integrity", "Availability",
            "cyber crime", "cyber warfare", "cyber terrorism",
            "Section 66F", "Critical Information Infrastructure",
            "protected system", "Section 70A", "NCIIPC",
            "Section 70B", "CERT-In", "I4C", "CyberDome",
            "Section 69A", "Shreya Singhal", "DPDP Rules",
            "six hours",
        ],
        "The audited ledgers route the 2019 CyberDome, 2020 cybercrime-types, 2021 cross-border cyber-attack and 2022 cyber-elements/strategy demands here. The three conservative cards cover 2019, 2021 and 2022; OCR inspection confirmed the 2019 and 2021 printed stems, while the ledger records official-scan verification for 2022.",
        pyqs, LIVE_ATTEMPTS,
        "On 2026-09-04 the official CERT-In Directions PDF was reachable, the I4C portal identified the MHA institution, and the official MeitY search result confirmed the 13 November 2025 DPDP Rules notification with staged commencement. No incident volume, loss, audit, attribution, arrest, conviction or recovery statistic is used.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "CIA, RISK AND INCIDENT-CRIME-OPERATION THREAT GRAMMAR",
            "IT ACT, CII, CERT-In, NCIIPC, I4C AND SECTORAL FIREWALLS",
            "CYBERDOME, DPDP AND THREE CONSERVATIVE PYQ SPINES",
            "ATTRIBUTION, EVIDENCE, RIGHTS AND RESILIENCE-FIRST VERDICT",
        ),
        register_answer_spine=[
            "NAME CONFIDENTIALITY INTEGRITY OR AVAILABILITY IMPACT",
            "SEPARATE THREAT VULNERABILITY CONSEQUENCE AND RECOVERY",
            "CLASSIFY INCIDENT CRIME WARFARE OR SECTION 66F TERRORISM",
            "STATE TECHNICAL LEGAL AND POLITICAL ATTRIBUTION CONFIDENCE",
            "MAP SECTION 70 70A 70B TO CII NCIIPC AND CERT-In",
            "KEEP I4C POLICE SECTORAL CERTS REGULATORS AND OWNERS DISTINCT",
            "SEPARATE IT ACT POWERS DPDP GOVERNANCE AND COMMENCEMENT",
            "CONCLUDE WITH TESTED CONTINUITY EVIDENCE RIGHTS AND RECOVERY",
        ],
    )


TOPIC_08 = _build()
