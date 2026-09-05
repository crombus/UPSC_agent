"""Authored learner-v2 data for Disaster Management Topic 05."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.bis.gov.in/other/PRESS_NOTE.pdf and "
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2247533 — fetched and "
        "attempted 2026-09-04; the BIS structural-safety press note returned "
        "as a raw PDF and the PIB page returned HTTP 403. The canonical owner "
        "remains the source for the operative IS 1893 (Part 1): 2016 status; "
        "no clause-level engineering instruction was reconstructed."
    ),
    (
        "https://services.bis.gov.in/tmp/SR4326.pdf and "
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2247533 — fetched and "
        "attempted 2026-09-04; the BIS preview returned as a raw PDF and PIB "
        "was blocked. It confirms an official BIS standards route, but no "
        "design value, detailing rule or compliance outcome was inferred."
    ),
    (
        "https://ndma.gov.in/Natural-Hazards/Earthquakes — attempted "
        "2026-09-04; the official NDMA page failed at the transport layer. "
        "The authored module therefore preserves the six-pillar framework "
        "already audited in the Basic owner without claiming current rollout."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2247533 — attempted "
        "2026-09-04; the official PIB page returned HTTP 403. Official search "
        "metadata was used only to cross-check the NCS, BhooKamp and operative "
        "zoning-status discussion; no network-performance outcome was imported."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Seismic risk", "Earthquake risk arises when seismic hazard interacts with exposed people and assets, vulnerable sites and construction, and limited coping capacity; the event alone is not the disaster."),
        ("Prediction boundary", "Earthquake occurrence cannot be precisely predicted by magnitude, place and time, so risk reduction must concentrate on vulnerability, preparedness and continuity rather than deterministic prediction."),
        ("Magnitude and intensity", "Magnitude describes the size or energy of an earthquake event, whereas intensity describes observed effects at a place; one event has one reported magnitude but can produce different intensities across locations."),
        ("Zoning and prediction", "Seismic zoning classifies broad expected hazard for planning and design; it neither predicts the next earthquake nor determines the fate of an individual building."),
        ("Site effects and microzonation", "Local ground conditions, slope, soil and built form can modify shaking and secondary effects, so microzonation refines broad regional zoning for risk-sensitive local planning."),
        ("Exposure", "Dense settlements, informal housing, schools, hospitals, bridges, utilities and other lifelines create concentrated exposure when located in seismic-risk settings."),
        ("Constructed vulnerability", "Irregular form, weak materials, poor connections, deficient workmanship, unauthorised alteration and absent maintenance can turn ground shaking into collapse and service failure."),
        ("Structural mitigation", "Structural mitigation includes earthquake-resistant new construction and selective strengthening or retrofitting of deficient priority structures under competent professional assessment."),
        ("Non-structural mitigation", "Non-structural mitigation includes land-use control, code enforcement, professional training and licensing, safety audits, awareness, drills, emergency planning and securing hazardous contents."),
        ("Code-compliant design", "BIS standards, the National Building Code and local building bye-laws form a safety framework, but a published code is not proof that a particular structure was correctly designed, built, inspected or maintained."),
        ("Ductility concept", "Ductility is the capacity to undergo deformation while retaining life-safety resistance; for UPSC purposes it explains why controlled energy dissipation matters, not how to calculate or detail a structure."),
        ("Retrofitting boundary", "Retrofitting seeks to improve the safety of existing deficient structures after assessment and prioritisation; identification, sanction or audit is not proof that strengthening is complete."),
        ("Non-structural components", "Falling fixtures, equipment, partitions, storage and utility connections can injure occupants or disable services even when the main structural frame remains standing."),
        ("Lifeline resilience", "Hospitals, emergency facilities, transport links, water, power and communications require both physical safety and continuity arrangements because post-event functionality is a separate test from collapse prevention."),
        ("Risk-sensitive land use", "Land-use decisions should avoid compounding shaking, slope, access and emergency-response risks; zoning must be connected to enforceable development control rather than treated as a map alone."),
        ("Compliance chain", "Seismic safety depends on linked code adoption, competent design, trained construction, approval, inspection, maintenance and enforcement; failure at one link can defeat the formal standard."),
        ("Monitoring boundary", "The National Centre for Seismology monitors and reports earthquake parameters and supports hazard assessment; post-event parameter dissemination is not prediction of a future event."),
        ("Institutional responsibility", "Central and State authorities set standards and protect structures under their control, while States and local bodies identify, regulate and prioritise vulnerable or lifeline stock for action."),
        ("Equity and informality", "Lower-income, rural and peri-urban households may depend more on informal or owner-built construction and have fewer resources for audit, retrofit, insurance, relocation and recovery."),
        ("Safety-outcome firewall", "A hazard map, code, guideline, audit, app, training programme or retrofit list proves an input; verified compliance, service continuity, reduced collapse and equitable recovery require separate evidence."),
    ]
    traps = [
        "Do not equate earthquake hazard with earthquake disaster.",
        "Do not confuse magnitude with place-specific intensity.",
        "Do not present seismic zoning or monitoring as prediction.",
        "Do not infer an individual building's safety from its zone alone.",
        "Do not turn exam-safe ductility concepts into engineering instructions.",
        "Do not treat a code or approved plan as proof of compliant construction.",
        "Do not limit mitigation to the structural frame or omit contents and utilities.",
        "Do not treat an audit or priority list as a completed retrofit.",
        "Do not reduce lifeline resilience to collapse prevention.",
        "Do not infer reduced losses from monitoring, training or guideline publication.",
    ]
    titles = [
        "Hazard exposure vulnerability and seismic risk",
        "Magnitude intensity and observed effects",
        "Seismic zoning prediction and microzonation",
        "Site effects and local risk variation",
        "Built-environment vulnerability",
        "Structural and non-structural mitigation",
        "Code-compliant resilient construction",
        "Ductility as an exam-safe life-safety concept",
        "Existing-stock audit and retrofitting",
        "Non-structural components and household safety",
        "Lifeline and critical-service continuity",
        "Land use development control and access",
        "NCS monitoring preparedness and response",
        "Compliance enforcement equity and informality",
        "PYQ synthesis and safety-outcome boundary",
    ]
    routes = [
        "Open with the hazard-exposure-vulnerability interaction.",
        "Separate event size from effects observed at different places.",
        "Use zoning for broad planning and microzonation for local refinement.",
        "Connect soil slope access and built form to uneven intensity and loss.",
        "Trace how design workmanship alteration and maintenance create vulnerability.",
        "Classify each measure before presenting the mitigation package.",
        "Move from standards to competent execution inspection and maintenance.",
        "Explain deformation and energy dissipation without prescribing design details.",
        "Prioritise deficient schools hospitals utilities and other lifelines transparently.",
        "Include contents fixtures equipment and utility connections.",
        "Test post-event functionality as well as physical survival.",
        "Connect hazard information to enforceable siting and development control.",
        "Distinguish monitoring parameter reporting early warning and prediction.",
        "Identify who enforces and who bears the cost of safety.",
        "Conclude at verified compliance and continuity rather than formal inputs.",
    ]
    panels = [
        common.panel("Seismic risk grammar", "systems-map", [
            "HAZARD -> ground shaking and secondary effects",
            "EXPOSURE -> people buildings infrastructure lifelines",
            "VULNERABILITY -> site + design + construction + maintenance",
            "CAPACITY -> preparedness response and recovery",
        ], ["Seismic risk", "Exposure", "Constructed vulnerability"]),
        common.panel("Magnitude-intensity firewall", "comparison-table", [
            "MAGNITUDE -> event size / energy measure",
            "INTENSITY -> observed effects at a location",
            "ONE EVENT -> varying local intensities",
            "TRAP -> scales are not interchangeable",
        ], ["Magnitude and intensity"]),
        common.panel("Zoning-to-site ladder", "status-ladder", [
            "SEISMIC ZONE -> broad expected hazard",
            "MICROZONATION -> finer local variation",
            "SITE ASSESSMENT -> project-specific conditions",
            "NONE OF THESE -> predicts the next event",
        ], ["Zoning and prediction", "Site effects and microzonation"]),
        common.panel("Site-effect map", "causal-chain", [
            "GROUND / SLOPE / SOIL CONDITION",
            "        -> modifies shaking or secondary risk",
            "BUILT FORM + ACCESS",
            "        -> modifies exposure response and loss",
        ], ["Site effects and microzonation", "Risk-sensitive land use"]),
        common.panel("Vulnerability chain", "failure-tree", [
            "IRREGULAR FORM | WEAK CONNECTION | POOR WORKMANSHIP",
            "UNAUTHORISED ALTERATION | DEGRADED MATERIAL",
            "FAILED APPROVAL / INSPECTION / MAINTENANCE",
            "RESULT -> collapse or service disruption risk",
        ], ["Constructed vulnerability", "Compliance chain"]),
        common.panel("Mitigation matrix", "matrix", [
            "STRUCTURAL -> safe new build + assessed strengthening",
            "NON-STRUCTURAL -> land use + enforcement + drills",
            "CONTENTS -> secure fixtures equipment utilities",
            "RULE -> combine; do not substitute one for all",
        ], ["Structural mitigation", "Non-structural mitigation", "Non-structural components"]),
        common.panel("Code-to-compliance rail", "numbered-rail", [
            "1 STANDARD / BYE-LAW",
            "2 COMPETENT DESIGN",
            "3 TRAINED CONSTRUCTION",
            "4 APPROVAL -> INSPECTION -> MAINTENANCE",
        ], ["Code-compliant design", "Compliance chain"]),
        common.panel("Ductility concept box", "concept-map", [
            "DEFORMATION CAPACITY",
            "        -> controlled energy dissipation",
            "        -> supports life-safety objective",
            "BOUNDARY -> concept only, no detailing instruction",
        ], ["Ductility concept"]),
        common.panel("Retrofit priority funnel", "decision-tree", [
            "SCREEN EXISTING STOCK",
            "PRIORITISE LIFELINES + HIGH OCCUPANCY + HIGH VULNERABILITY",
            "DETAILED ASSESSMENT -> SANCTION -> WORK -> VERIFY",
            "AUDIT / LISTING ALONE -> NOT COMPLETION",
        ], ["Retrofitting boundary", "Institutional responsibility"]),
        common.panel("Lifeline continuity map", "network-map", [
            "HOSPITAL + EOC + FIRE / RESCUE",
            "POWER + WATER + TELECOM",
            "ROAD / BRIDGE / ACCESS",
            "TEST -> physical safety AND post-event function",
        ], ["Lifeline resilience"]),
        common.panel("Monitoring-prediction boundary", "process-flow", [
            "SENSOR -> EVENT DETECTION -> PARAMETER REPORT",
            "HAZARD ASSESSMENT -> PLANNING INPUT",
            "PREPAREDNESS -> PROTECTIVE ACTION",
            "NOT -> precise future magnitude place and time",
        ], ["Prediction boundary", "Monitoring boundary"]),
        common.panel("Earthquake answer spine", "answer-spine", [
            "DEFINE RISK -> SEPARATE MAGNITUDE INTENSITY",
            "MAP ZONE + SITE + EXPOSURE + VULNERABILITY",
            "COMBINE CODE RETROFIT LAND USE CONTENTS AND LIFELINES",
            "TEST ENFORCEMENT EQUITY CONTINUITY AND VERIFIED OUTCOME",
        ], ["Equity and informality", "Safety-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2021", "GS-III",
            "Discuss India's vulnerability to earthquake hazards and use historical disaster examples.",
            "Verified direct routing: Discuss · 10 marks · 150 words; examples must remain source-bounded and need no casualty or magnitude recital.",
            [0, 3, 4, 5, 6, 8, 14, 18]),
        common.make_pyq_solution(facts, "2019", "GS-III",
            "Discuss vulnerability as a concept for defining disaster impacts and explain its types.",
            "Verified direct ownership remains Topic 01; this conservative card supplies the earthquake site, construction, lifeline and social-vulnerability application.",
            [0, 4, 5, 6, 12, 13, 18]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe the elements that determine disaster resilience.",
            "Verified direct ownership remains Topic 01; this card routes code compliance, ductility, retrofit, land use and lifeline continuity as seismic-resilience elements.",
            [7, 8, 9, 10, 11, 13, 15, 19]),
    ]
    return common.topic(
        5, "Earthquake Risk and Resilient Construction",
        "05_Earthquake-Risk-and-Resilient-Construction", facts, traps,
        [
            (10, "Distinguish earthquake hazard, exposure, vulnerability and seismic risk.", [0, 1, 5, 6]),
            (10, "Differentiate magnitude, intensity, seismic zoning and prediction.", [1, 2, 3, 4]),
            (15, "Explain structural and non-structural measures for earthquake-risk reduction.", [7, 8, 9, 10, 12, 14]),
            (15, "Analyse the priorities and limits of seismic retrofitting and lifeline resilience.", [11, 13, 17, 18, 19]),
            (20, "Critically examine why code-compliant construction is primarily a governance and enforcement challenge.", [6, 7, 8, 9, 10, 15, 17, 18, 19]),
            (20, "Design an exam-safe earthquake-resilience framework covering land use, construction, retrofitting, lifelines, preparedness and equity.", [0, 3, 4, 7, 8, 11, 12, 13, 14, 16, 18, 19]),
        ],
        titles, routes, panels,
        [
            "magnitude", "intensity", "seismic zones", "IS 1893",
            "Zone V", "microzonation", "National Centre for Seismology",
            "National Building Code", "BMTPC", "retrofitting",
            "lifeline", "land-use", "earthquake early warning",
            "prediction", "non-structural",
        ],
        "The 2021 GS-III card is directly routed. The 2019 vulnerability and 2024 resilience cards are explicitly conservative cross-topic applications and do not displace Topic 01 ownership.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered BIS structural-safety standards, NDMA earthquake guidance and PIB/MoES-NCS status material. Raw, blocked or transport-failed pages are logged; no design coefficient, prediction claim, compliance rate or loss outcome was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "SEISMIC RISK MAGNITUDE INTENSITY ZONING AND SITE-EFFECT MAP",
            "CODE DUCTILITY RETROFIT CONTENTS AND LIFELINE FIREWALLS",
            "LAND-USE COMPLIANCE EQUITY AND CONTINUITY ANSWER SPINE",
            "CURRENT BIS NDMA NCS AND SAFETY-OUTCOME EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE HAZARD EXPOSURE VULNERABILITY CAPACITY AND SEISMIC RISK",
            "SEPARATE MAGNITUDE INTENSITY ZONING MICROZONATION AND PREDICTION",
            "MAP SITE EFFECTS AND CONSTRUCTED VULNERABILITY",
            "COMBINE CODE-COMPLIANT NEW BUILD DUCTILITY AND NON-STRUCTURAL SAFETY",
            "PRIORITISE ASSESSED RETROFITTING AND LIFELINE CONTINUITY",
            "ADD LAND-USE ENFORCEMENT PROFESSIONAL CAPACITY AND EQUITY",
            "CONCLUDE AT VERIFIED COMPLIANCE FUNCTION AND OUTCOME",
        ],
    )


TOPIC_05 = _build()
