"""Authored learner-v2 data for Internal Security Topic 06."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/en/divisionofmha/border-management-ii-division "
        "— attempted 2026-09-04; direct retrieval returned 403. Search results "
        "confirmed the division's broad BADP, Vibrant Villages, coastal-security "
        "and LPAI coordination remit, but no allocation, coverage or outcome "
        "number is imported."
    ),
    (
        "https://www.mha.gov.in/en/divisionofmha/border-management-i-division "
        "— attempted 2026-09-04; direct retrieval returned 403. The module uses "
        "the owner-audited BIM and CIBMS distinctions and does not convert a "
        "scheme period, sensor deployment or sanctioned work into an outcome."
    ),
    (
        "https://vvp.mha.gov.in/Home/About — fetched 2026-09-04; the official "
        "page confirms Vibrant Villages Programme as a Centrally Sponsored "
        "Scheme announced in Budget 2022-23 for northern-border villages, with "
        "district and Gram Panchayat action plans and an express non-overlap "
        "rule with BADP."
    ),
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the "
        "Constitution (One Hundredth Amendment) Act, 2015 and the "
        "India-Bangladesh land-boundary settlement; direct retrieval returned "
        "403, so only the audited owner distinction is retained."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Security-management distinction", "Border security concerns defence and guarding, while border management also includes regulation, infrastructure and area development, legal mobility or trade, and bilateral mechanisms."),
        ("Boundary vocabulary", "An International Boundary is mutually recognised and demarcated; the LoC is a military control line in the J&K context, the LAC is the differently perceived India-China alignment, and the AGPL runs north of NJ 9842 in the Siachen sector."),
        ("China-border character", "The India-China frontier is disputed and lacks a mutually agreed LAC in stretches, making perception, patrol protocols, infrastructure and diplomatic-military mechanisms central management issues."),
        ("Pakistan-border segmentation", "The Pakistan-facing boundary must be separated into the Radcliffe International Boundary, the Line of Control and the Actual Ground Position Line because terrain, legal status, lead forces and threat vectors differ."),
        ("Bangladesh settled-by-instrument case", "The India-Bangladesh land-enclave and adverse-possession questions were resolved through the 2015 Land Boundary Agreement and the Constitution (One Hundredth Amendment) Act, while the maritime boundary was settled by a 2014 arbitral award."),
        ("Nepal open-border case", "The India-Nepal open border facilitates legitimate movement under the bilateral treaty framework but can also be misused for transit, requiring facilitation and risk-based enforcement together."),
        ("Myanmar FMR status rule", "MHA announced on 8 February 2024 a decision to scrap the India-Myanmar Free Movement Regime; announcement, formal notification and field implementation must not be collapsed."),
        ("Border-specific force map", "The owner maps BSF to the Pakistan and Bangladesh borders, ITBP to the China border, SSB to Nepal and Bhutan, and Assam Rifles to Myanmar, while recognising border-specific operational overlap."),
        ("One-border-one-force boundary", "The post-Kargil one border, one force principle is a coordination objective, not proof that every sector is presently under one exclusive command."),
        ("Four-element framework", "A complete border-management answer combines guarding, regulation, development of border areas and bilateral institutional mechanisms, calibrated to terrain and legal mobility."),
        ("BADP purpose", "The Border Area Development Programme addresses development gaps in eligible border villages through local infrastructure, services and livelihood support; sanction or expenditure does not prove security or welfare outcomes."),
        ("BIM purpose", "The Border Infrastructure and Management scheme is the infrastructure umbrella for assets such as roads, fencing, floodlighting, outposts, communications and technology; its current period and outlay require a dated MHA source."),
        ("BADP-BIM distinction", "BADP is primarily area and community development, while BIM primarily builds border-management infrastructure; they are complementary but not interchangeable schemes."),
        ("CIBMS role", "The Comprehensive Integrated Border Management System integrates sensors, communications, intelligence and command-and-control to cover difficult gaps; detection and track generation are not the same as interdiction."),
        ("ICP-LPAI role", "Integrated Check Posts consolidate customs, immigration and regulatory services at legal crossings, while the Land Ports Authority of India is the statutory body responsible for their development and management."),
        ("Vibrant Villages boundary", "The official VVP page describes a Centrally Sponsored Scheme for selected northern-border villages, using district and Gram Panchayat action plans and expressly avoiding overlap with BADP."),
        ("Community-security link", "Border residents are rights-bearing citizens and security partners; livelihoods, legal trade, grievance channels and protected reporting strengthen state presence without treating mobility as inherently suspect."),
        ("Adversarial-UAV classification", "A hostile unmanned aerial vehicle is a vector that may carry surveillance, weapons or contraband; the response must separate detection, lawful counter-action, recovery, forensics and prosecution."),
        ("Input-outcome firewall", "A fence, road, outpost, sensor, village plan or interception is an input or output at a specific rung; border security outcomes require separately verified evidence."),
        ("Differentiated end-state", "Effective border management is neighbour-, terrain- and community-specific: clear mandates, interoperable awareness and response, lawful mobility, resilient infrastructure, bilateral mechanisms and audited development outcomes."),
    ]
    traps = [
        "Do not use border security and border management as synonyms.",
        "Do not call the IB, LoC, LAC and AGPL interchangeable boundary lines.",
        "Do not merge China and Pakistan border challenges into one paragraph.",
        "Do not describe every India-Pakistan segment as an International Boundary.",
        "Do not repeat the outdated claim that India-Bangladesh enclaves remain unresolved.",
        "Do not treat an open border as an unregulated or lawless border.",
        "Do not convert the 8 February 2024 FMR decision into complete implementation.",
        "Do not present one border, one force as fully implemented everywhere.",
        "Do not confuse BADP, BIM and Vibrant Villages Programme.",
        "Do not equate sensor detection with interdiction or conviction.",
        "Do not publish tactical coverage gaps, patrol patterns or counter-UAS methods.",
        "Do not infer outcomes from scheme sanction, expenditure or asset creation.",
    ]
    titles = [
        "Border security and border management",
        "IB LoC LAC and AGPL distinctions",
        "China border dispute and mechanism map",
        "Pakistan border segment-by-segment analysis",
        "Bangladesh settled-by-instrument comparison",
        "Nepal open border and lawful mobility",
        "Myanmar FMR status and community trade-off",
        "Border-specific forces and mandate clarity",
        "One border one force implementation gap",
        "Guarding regulation development and bilateral mechanisms",
        "BADP BIM and Vibrant Villages",
        "CIBMS awareness and interdiction boundary",
        "Integrated Check Posts and LPAI",
        "Adversarial UAV vector and evidence chain",
        "Community partnership and differentiated end-state",
    ]
    routes = [
        "Define the broader management system before discussing physical guarding.",
        "Name the line's exact legal and operational character.",
        "Explain disputed alignment and de-escalation without tactical detail.",
        "Separate IB, LoC and AGPL before mapping threats and institutions.",
        "Use Bangladesh as a controlled example of settlement by legal instruments.",
        "Balance facilitation with intelligence-led and lawful risk control.",
        "State decision, notification and implementation as separate rungs.",
        "Map force to border while acknowledging formally verified overlap only.",
        "Present the principle as a reform objective and test implementation.",
        "Use all four elements as the answer's organising spine.",
        "Distinguish scheme purpose, funding route, implementation and outcome.",
        "Separate awareness, decision, interdiction and evidence.",
        "Show how legal crossings improve facilitation and enforcement together.",
        "Classify UAV as a vector and preserve forensic and legal handover.",
        "Conclude with residents, lawful mobility and audited outcomes at the centre.",
    ]
    panels = [
        common.panel("Border-management system", "systems-map", [
            "BORDER SECURITY -> guarding / defence",
            "BORDER MANAGEMENT -> guarding + regulation",
            "                         + development + legal mobility",
            "                         + bilateral mechanisms",
            "RULE -> the wider system is the answer unit",
        ], ["Security-management distinction", "Four-element framework"]),
        common.panel("Boundary-line matrix", "comparison-table", [
            "IB -> mutually recognised / demarcated international boundary",
            "LoC -> military control line in J&K context",
            "LAC -> differently perceived India-China alignment",
            "AGPL -> Siachen-sector line north of NJ 9842",
        ], ["Boundary vocabulary"]),
        common.panel("China-border answer map", "process-flow", [
            "DISPUTED / DIFFERENTLY PERCEIVED LAC",
            "-> PATROL / INFRASTRUCTURE / ESCALATION RISK",
            "-> MILITARY-DIPLOMATIC MECHANISMS",
            "-> DE-ESCALATION INPUT, NOT BOUNDARY SETTLEMENT",
        ], ["China-border character"]),
        common.panel("Pakistan segment map", "comparison-table", [
            "RADCLIFFE IB -> guarding / smuggling / legal crossings",
            "LoC -> military ceasefire + infiltration dimension",
            "AGPL -> high-altitude military / logistics dimension",
            "SIR CREEK -> separately unsettled maritime-adjacent issue",
        ], ["Pakistan-border segmentation"]),
        common.panel("Settled-by-instrument ladder", "timeline", [
            "2014 -> INDIA-BANGLADESH MARITIME ARBITRAL AWARD",
            "2015 -> LAND BOUNDARY AGREEMENT",
            "2015 -> CONSTITUTION (100TH AMENDMENT) ACT",
            "LESSON -> legal instrument can change boundary status",
        ], ["Bangladesh settled-by-instrument case"]),
        common.panel("Mobility-regulation balance", "balance-scale", [
            "NEPAL -> OPEN BORDER + LEGITIMATE MOVEMENT",
            "MYANMAR -> ETHNIC / LIVELIHOOD LINKS + FMR STATUS",
            "SECURITY -> risk-based checks and intelligence",
            "SAFEGUARD -> notification clarity + community consultation",
        ], ["Nepal open-border case", "Myanmar FMR status rule", "Community-security link"]),
        common.panel("Force-to-border architecture", "institution-map", [
            "BSF -> PAKISTAN / BANGLADESH",
            "ITBP -> CHINA",
            "SSB -> NEPAL / BHUTAN",
            "ASSAM RIFLES -> MYANMAR",
            "PRINCIPLE -> one border, one force; verify actual overlap",
        ], ["Border-specific force map", "One-border-one-force boundary"]),
        common.panel("Scheme purpose firewall", "comparison-table", [
            "BADP -> BORDER-AREA PEOPLE / SERVICES / LIVELIHOOD",
            "BIM -> BORDER INFRASTRUCTURE / GUARDING ASSETS",
            "VVP -> SELECT NORTHERN VILLAGES; NO BADP OVERLAP",
            "RULE -> sanction / outlay / asset is not outcome",
        ], ["BADP purpose", "BIM purpose", "BADP-BIM distinction", "Vibrant Villages boundary"]),
        common.panel("CIBMS capability chain", "process-flow", [
            "SENSOR -> NETWORK -> FUSED AWARENESS",
            "-> COMMAND DECISION -> LAWFUL RESPONSE",
            "-> RECOVERY / FORENSICS -> INVESTIGATION",
            "TRAP -> a detected track is not an interdiction",
        ], ["CIBMS role", "Input-outcome firewall"]),
        common.panel("Legal-crossing system", "institution-map", [
            "INTEGRATED CHECK POST",
            "-> CUSTOMS + IMMIGRATION + REGULATORY SERVICES",
            "LPAI -> DEVELOPMENT / MANAGEMENT OF LAND PORTS",
            "RESULT SOUGHT -> facilitation and enforcement together",
        ], ["ICP-LPAI role"]),
        common.panel("Adversarial UAV response", "decision-tree", [
            "VECTOR -> SURVEILLANCE / WEAPON / CONTRABAND",
            "DETECT -> IDENTIFY -> LAWFUL COUNTER-ACTION",
            "RECOVER -> FORENSICS -> ATTRIBUTION / PROSECUTION",
            "LIMIT -> no unsourced incident or interception count",
        ], ["Adversarial-UAV classification"]),
        common.panel("PYQ and end-state rail", "answer-spine", [
            "2020 -> MYANMAR / BANGLADESH / LoC COMPARISON",
            "2023 -> UAV VECTOR + CAPABILITY + EVIDENCE",
            "2024 -> CHINA / PAKISTAN + BADP / BIM",
            "END -> differentiated borders + community + audited outcomes",
        ], ["Differentiated end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2020", "GS-III",
            "Security challenges along the Myanmar and Bangladesh borders and the Pakistan Line of Control.",
            "Audited routed demand; Analyse · 15 marks · 250 words. The routing ledger records official-scan verification.",
            [1, 3, 4, 5, 6, 7, 9, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2023", "GS-III",
            "Use of unmanned aerial vehicles by adversaries across borders to ferry arms, ammunition and drugs, and measures to tackle the threat.",
            "Printed stem inspected in the OCR-searchable official paper; Comment · 10 marks · 150 words.",
            [7, 9, 13, 16, 17, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2024", "GS-III",
            "China-Pakistan border issues and security challenges, together with BADP and the Border Infrastructure and Management scheme.",
            "Printed stem inspected in the OCR-searchable official paper; Examine · 15 marks · 250 words. The scan renders BIM as BM, while the audited owner supplies the official scheme name.",
            [1, 2, 3, 4, 8, 9, 10, 11, 12, 16, 18, 19],
        ),
    ]
    return common.topic(
        6, "Border Management and Border Area Development",
        "06_Border-Management-and-Border-Area-Development", facts, traps,
        [
            (10, "Distinguish border security from border management and explain the four-element management framework.", [0, 8, 9, 16, 19]),
            (10, "Explain why BADP, BIM and the Vibrant Villages Programme must not be treated as one scheme.", [10, 11, 12, 15, 18]),
            (15, "Analyse security challenges along the Myanmar and Bangladesh borders and the Pakistan Line of Control.", [1, 3, 4, 5, 6, 7, 9, 16, 19]),
            (15, "Examine conflicting issues along the China and Pakistan borders and assess BADP and BIM as distinct responses.", [1, 2, 3, 8, 9, 10, 11, 12, 18, 19]),
            (20, "Critically evaluate the one border, one force principle alongside technology and community participation.", [7, 8, 9, 13, 16, 18, 19]),
            (20, "Design a differentiated border-management strategy that balances security, legal mobility, infrastructure, area development and bilateral mechanisms.", [0, 1, 2, 3, 4, 5, 6, 9, 14, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "border security", "border management", "Radcliffe Line",
            "Line of Control", "Actual Ground Position Line",
            "LAC", "one-force-one-border", "BSF",
            "ITBP", "SSB", "Assam Rifles", "BADP", "BIM", "CIBMS",
            "Land Ports Authority of India", "Vibrant Villages Programme",
            "Free Movement Regime", "Madhukar Gupta Committee",
        ],
        "The audited ledgers route the 2020 Myanmar-Bangladesh-LoC comparison, the 2023 adversarial-UAV demand and the 2024 China-Pakistan-BADP-BIM demand here. OCR inspection confirmed the 2023 and 2024 printed stems; no operational detail or official model answer is inferred.",
        pyqs, LIVE_ATTEMPTS,
        "On 2026-09-04, the official VVP page confirmed the programme's scheme type, northern-border focus, district/Gram Panchayat planning and non-overlap with BADP. MHA division pages returned 403, so no current allocation, border coverage, fencing, CIBMS or outcome figure is used.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "IB, LoC, LAC, AGPL AND NEIGHBOUR-SPECIFIC CHALLENGE MAP",
            "FORCE, SCHEME, TECHNOLOGY AND LEGAL-MOBILITY FIREWALLS",
            "BADP, BIM, VVP AND THREE CONSERVATIVE PYQ SPINES",
            "COMMUNITY PARTNERSHIP, IMPLEMENTATION AND OUTCOME AUDIT",
        ),
        register_answer_spine=[
            "DEFINE BORDER MANAGEMENT AS WIDER THAN PHYSICAL SECURITY",
            "NAME THE EXACT IB LoC LAC OR AGPL STATUS",
            "SEPARATE CHINA PAKISTAN BANGLADESH NEPAL AND MYANMAR CHALLENGES",
            "MAP THE BORDER-SPECIFIC FORCE AND VERIFY OVERLAP",
            "USE GUARDING REGULATION DEVELOPMENT AND BILATERAL MECHANISMS",
            "DISTINGUISH BADP BIM VVP CIBMS ICP AND LPAI",
            "SEPARATE SENSOR AWARENESS INTERDICTION FORENSICS AND OUTCOME",
            "CONCLUDE WITH LEGAL MOBILITY COMMUNITY TRUST AND AUDITED DELIVERY",
        ],
    )


TOPIC_06 = _build()
