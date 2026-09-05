"""Authored learner-v2 data for Disaster Management Topic 13."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://ncdc.mohfw.gov.in/includes/About/CentresAndDivision/IDSP.php "
        "— fetched 2026-09-04; NCDC described decentralised laboratory-based "
        "IT-enabled surveillance, Centre/State/district units, S/P/L reporting, "
        "Rapid Response Teams, laboratories and zoonotic coordination. "
        "https://ndma.gov.in/Man-made-Hazards/Biological — attempted "
        "2026-09-04; the NDMA page failed at the transport layer."
    ),
    (
        "https://www.icmr.gov.in/ — fetched 2026-09-04 but returned a thin "
        "institutional feature rather than emergency guidance. "
        "https://www.mohfw.gov.in/ — attempted 2026-09-04 and returned HTTP "
        "403. "
        "https://www.mha.gov.in/en/commoncontent/disaster-management-act-2005 "
        "— attempted 2026-09-04; MHA returned HTTP 403. No laboratory, vaccine, "
        "workforce, outbreak or operational-readiness figure was imported."
    ),
    (
        "https://www.who.int/news/item/19-09-2025-amended-international-health-"
        "regulations-enter-into-force — fetched 2026-09-04; WHO confirmed the "
        "2024 IHR amendments, pandemic-emergency alert and national sovereignty "
        "boundary. https://ndrf.gov.in/en/about-us — fetched 2026-09-04 only "
        "for the general specialised disaster-response role."
    ),
    (
        "https://www.who.int/news/item/20-07-2026-who-member-states-continue-"
        "negotiations-on-the-pathogen-access-and-benefit-sharing-annex — "
        "searched 2026-09-04; official WHO results showed PABS negotiations "
        "continuing. https://pib.gov.in/ — searched 2026-09-04 for an Indian "
        "official corroboration route but no additional status proposition was "
        "used. The Pandemic Agreement was not described as in force."
    ),
    (
        "https://nidm.gov.in/documentations.asp — searched 2026-09-04; the "
        "official NIDM documentation route was identified but did not supply "
        "additional current epidemic-readiness evidence."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Outbreak", "An outbreak is the occurrence of disease cases above what is normally expected in a limited place, population or period; scale and baseline determine the label."),
        ("Epidemic", "An epidemic is occurrence of disease above the expected level in a community, region or population; it does not require international spread."),
        ("Pandemic", "A pandemic is an epidemic with sustained spread across countries or continents and substantial population reach; severity is not defined by geography alone."),
        ("Endemic", "An endemic disease has a persistent or expected presence in a particular area or population; endemicity does not mean harmlessness or absence of outbreaks."),
        ("Public-health emergency status", "A domestic public-health emergency, a Public Health Emergency of International Concern and the amended IHR's pandemic emergency are different legal or operational statuses with different authorities and tests."),
        ("Surveillance", "Surveillance is continuous collection, analysis, interpretation and use of health information for action; it includes signals and trends rather than only confirmed case totals."),
        ("Laboratory confirmation", "Laboratory evidence supports diagnosis and classification, but sampling, transport, quality, turnaround and interpretation determine whether confirmation can guide timely public-health action."),
        ("Risk assessment", "Risk assessment integrates hazard, transmissibility or route, severity, exposure, vulnerable groups, uncertainty, health-system capacity and geographic or temporal context before selecting proportionate measures."),
        ("One Health", "One Health coordinates human, animal and environmental health knowledge and action, especially for zoonotic and vector-borne threats, while preserving sector-specific expertise and accountability."),
        ("Prevention and preparedness", "Prevention and preparedness include water, sanitation, vector control, infection prevention, routine immunisation where applicable, stock and workforce planning, laboratories, plans, training, drills and trusted communication."),
        ("Outbreak response", "Response links verification, investigation, case finding, testing, clinical care, isolation where indicated, contact or exposure management, community measures, logistics and iterative reassessment."),
        ("Health-system surge", "Surge capacity covers trained staff, beds and referral, laboratories, medicines and supplies, oxygen or other clinical support where relevant, transport, information systems and staff safety without abandoning routine care."),
        ("Continuity of essential services", "A health emergency plan must preserve maternal, child, chronic-disease, emergency and other essential services as far as possible because response measures can create indirect harm."),
        ("Risk communication", "Risk communication should be timely, transparent, multilingual, accessible and updateable, explaining what is known, unknown, changing and expected from the public without blame or false certainty."),
        ("Quarantine versus isolation", "Quarantine separates or restricts movement of persons who may have been exposed but are not known to be infected; isolation separates infected or ill persons under applicable public-health protocols."),
        ("Federal and local roles", "Health is principally a State field, while Union law, inter-State disease control, national standards, laboratories, border health and disaster coordination can support or direct specified functions; implementation remains local and multi-level."),
        ("Institutional roles", "MoHFW provides national health leadership, NCDC and IDSP support surveillance and outbreak response, ICMR supports research and technical evidence, States deliver public health, and WHO coordinates the international IHR framework."),
        ("Vulnerable groups", "Risk and access differ for older people, children, pregnant persons, persons with disabilities or chronic illness, health workers, migrants, crowded households and those facing digital, language, income or care barriers."),
        ("Misinformation and recovery", "Rumours, stigma and information overload can undermine response; recovery should restore services, address interrupted care and livelihoods, support workers and communities, review excess harm and institutionalise lessons."),
        ("Platform-outcome firewall", "A surveillance portal, laboratory, app, guideline, emergency declaration, agreement or vaccination platform proves a tool or status; early detection, equitable care, trust, continuity and reduced harm require separate evidence."),
    ]
    traps = [
        "Do not use outbreak, epidemic, pandemic and endemic as synonyms.",
        "Do not infer severity solely from the geographic label pandemic.",
        "Do not treat endemic as harmless or static.",
        "Do not confuse a domestic emergency, PHEIC and pandemic emergency.",
        "Do not equate surveillance signals with laboratory-confirmed cases.",
        "Do not treat laboratory confirmation as timely action without logistics and interpretation.",
        "Do not use quarantine for known infected cases or isolation for merely exposed persons.",
        "Do not infer that State-list health excludes Union or inter-State roles.",
        "Do not route vaccine platforms, diagnostics or biotechnology internals away from their Science and Technology owners.",
        "Do not infer preparedness or successful outcomes from a portal, app, plan, declaration or agreement.",
    ]
    titles = [
        "Outbreak epidemic pandemic endemic and emergency-status grammar",
        "Transmission exposure severity uncertainty and risk assessment",
        "Surveillance signals S P L reporting and early detection",
        "Laboratory confirmation quality logistics and decision timing",
        "One Health zoonoses vectors and cross-sector coordination",
        "Prevention preparedness plans workforce stocks and drills",
        "Investigation case finding testing care and reassessment",
        "Isolation quarantine and proportionate public-health measures",
        "Health-system surge referral supplies and staff safety",
        "Continuity of essential health and social services",
        "Risk communication trust misinformation and stigma",
        "Federal Union State district and local responsibilities",
        "MoHFW NCDC IDSP ICMR WHO and disaster coordination",
        "Vulnerable groups recovery and institutional learning",
        "PYQ synthesis platforms international status and outcome firewall",
    ]
    routes = [
        "Fix the epidemiological and legal status before selecting measures.",
        "Assess hazard route exposure vulnerability capacity and uncertainty.",
        "Trace signal collection analysis verification and response.",
        "Explain confirmation as a chain, not a laboratory label alone.",
        "Link human animal environment sectors without erasing ownership.",
        "Build capability before the surge and retain routine services.",
        "Sequence investigation care community action and repeated assessment.",
        "Use the correct person-status distinction and proportionality.",
        "Plan staff space supplies referral transport information and safety.",
        "Measure indirect harm and preserve non-outbreak care.",
        "State known unknown action update and correction channels.",
        "Separate national standards and inter-State coordination from local delivery.",
        "Assign surveillance research health delivery international and disaster roles.",
        "Design accessible care support recovery and lesson adoption.",
        "Conclude with detected-to-acted, equitable and continuity outcomes.",
    ]
    panels = [
        common.panel("Epidemiological status ladder", "status-ladder", [
            "OUTBREAK -> local excess over expected",
            "EPIDEMIC -> population / regional excess",
            "PANDEMIC -> sustained multi-country / continental spread",
            "ENDEMIC -> expected persistent presence",
        ], ["Outbreak", "Epidemic", "Pandemic", "Endemic"]),
        common.panel("Emergency-status firewall", "comparison-table", [
            "DOMESTIC STATUS -> national / subnational legal basis",
            "PHEIC -> IHR international-concern status",
            "PANDEMIC EMERGENCY -> amended-IHR higher alert",
            "WHO COORDINATES -> STATES RETAIN SOVEREIGN AUTHORITY",
        ], ["Public-health emergency status"]),
        common.panel("Risk-assessment map", "systems-map", [
            "AGENT / HAZARD + TRANSMISSION ROUTE",
            "EXPOSURE + VULNERABLE GROUPS",
            "SEVERITY + HEALTH-SYSTEM CAPACITY",
            "UNCERTAINTY + PLACE / TIME -> PROPORTIONATE ACTION",
        ], ["Risk assessment"]),
        common.panel("Surveillance-to-action rail", "numbered-rail", [
            "1 SIGNAL / S-P-L REPORTING",
            "2 ANALYSE TREND AND VERIFY",
            "3 RAPID RESPONSE INVESTIGATION",
            "4 CONTROL + FEEDBACK TO SURVEILLANCE",
        ], ["Surveillance", "Laboratory confirmation"]),
        common.panel("One Health triangle", "network-map", [
            "HUMAN HEALTH <-> ANIMAL HEALTH",
            "       \\           /",
            "        ENVIRONMENT",
            "JOINT SURVEILLANCE / INVESTIGATION; SECTOR OWNERS REMAIN",
        ], ["One Health"]),
        common.panel("Preparedness portfolio", "matrix", [
            "PREVENT -> WASH vector control infection prevention immunisation",
            "PREPARE -> workforce labs stocks plans training drills",
            "COMMUNICATE -> trusted accessible channels",
            "CONTINUE -> routine health and social services",
        ], ["Prevention and preparedness", "Continuity of essential services"]),
        common.panel("Outbreak-response loop", "feedback-loop", [
            "VERIFY -> INVESTIGATE -> CASE FIND / TEST",
            "CARE + ISOLATE WHERE INDICATED",
            "MANAGE EXPOSURE / COMMUNITY RISK",
            "REASSESS DATA EFFECTS EQUITY AND PROPORTIONALITY",
        ], ["Outbreak response"]),
        common.panel("Quarantine-isolation split", "comparison-table", [
            "QUARANTINE -> exposed, not known infected",
            "ISOLATION -> infected / ill case",
            "BOTH -> lawful proportionate supported and time-bounded",
            "TRAP -> LABEL DOES NOT REPLACE CARE OR RIGHTS",
        ], ["Quarantine versus isolation"]),
        common.panel("Surge and continuity balance", "matrix", [
            "SURGE -> staff space lab supplies referral transport",
            "WORKFORCE -> protection rest communication support",
            "ESSENTIAL CARE -> maternal child chronic emergency services",
            "OUTCOME -> outbreak care without avoidable indirect harm",
        ], ["Health-system surge", "Continuity of essential services"]),
        common.panel("Risk communication chain", "process-flow", [
            "KNOWN + UNKNOWN + CHANGING",
            "WHO / WHERE / WHAT ACTION / WHERE CARE",
            "MULTILINGUAL ACCESSIBLE TRUSTED MESSENGERS",
            "MONITOR RUMOUR STIGMA FEEDBACK AND CORRECT",
        ], ["Risk communication", "Misinformation and recovery"]),
        common.panel("Institutional map", "systems-map", [
            "MOHFW / NCDC-IDSP / ICMR -> STANDARD SURVEILLANCE EVIDENCE",
            "STATE / DISTRICT / LOCAL -> PUBLIC HEALTH DELIVERY",
            "DM AUTHORITIES -> CROSS-SECTOR COORDINATION",
            "WHO / IHR -> INTERNATIONAL NOTIFICATION AND COOPERATION",
        ], ["Federal and local roles", "Institutional roles"]),
        common.panel("Public-health answer spine", "answer-spine", [
            "DEFINE STATUS -> ASSESS ROUTE EXPOSURE SEVERITY CAPACITY",
            "SURVEIL CONFIRM INVESTIGATE RESPOND AND REASSESS",
            "ADD ONE HEALTH SURGE CONTINUITY COMMUNICATION AND EQUITY",
            "ASSIGN FEDERAL / INTERNATIONAL ROLES + VERIFY OUTCOMES",
        ], ["Platform-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Give an account of technology used in COVID-19 pandemic management and its advancements.",
            "Verified direct routing: Give an account of · 15 marks · 250 words; organise technology by surveillance, diagnosis, communication, care and delivery functions and preserve equity and outcome limits.",
            [5, 6, 7, 10, 11, 13, 16, 17, 19]),
        common.make_pyq_solution(facts, "2020", "GS-II",
            "Discuss WHO's role in global health security during the COVID-19 pandemic.",
            "Verified cross-paper route owned by International Relations/global governance; this card contributes only IHR status, national institutions and sovereignty boundaries.",
            [4, 13, 16, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, its determination and the Sendai Framework elements.",
            "Verified support route, not a public-health-emergency-specific PYQ; surveillance, surge, continuity, communication and recovery are bounded resilience illustrations.",
            [5, 8, 9, 11, 12, 13, 18, 19]),
    ]
    return common.topic(
        13, "Epidemics and Public Health Emergencies",
        "13_Epidemics-and-Public-Health-Emergencies", facts, traps,
        [
            (10, "Distinguish outbreak, epidemic, pandemic, endemic and public-health emergency statuses.", [0, 1, 2, 3, 4]),
            (10, "Differentiate quarantine and isolation and state their governance safeguards.", [10, 14, 17]),
            (15, "Explain the surveillance, laboratory-confirmation and risk-assessment chain for outbreak response.", [5, 6, 7, 10, 19]),
            (15, "Analyse One Health and federal coordination for zoonotic and epidemic threats.", [8, 15, 16, 19]),
            (20, "Design a public-health-emergency framework covering prevention, surge, continuity, communication and vulnerable groups.", [5, 6, 7, 9, 10, 11, 12, 13, 17, 18, 19]),
            (20, "Critically evaluate whether laws, platforms and international agreements ensure pandemic resilience.", [4, 5, 6, 7, 13, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "outbreak", "epidemic", "pandemic", "endemic", "PHEIC",
            "pandemic emergency", "surveillance", "laboratory",
            "risk assessment", "One Health", "zoonotic", "quarantine",
            "isolation", "NCDC", "IDSP",
        ],
        "The 2020 GS-III technology-in-COVID card is the verified direct route. The 2020 GS-II WHO card is cross-paper and remains global-governance-owned; the 2024 resilience card is an explicit support route.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered NCDC/IDSP, ICMR, MoHFW/MHA/NDMA routes and WHO's amended IHR and Pandemic Agreement/PABS status. Thin, blocked and transport-failed pages are logged; no current outbreak total, forecast, laboratory readiness, stock, vaccine performance, casualty, event outcome or international compliance claim was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "OUTBREAK EPIDEMIC PANDEMIC ENDEMIC STATUS SURVEILLANCE AND RISK MAP",
            "PHEIC PANDEMIC-EMERGENCY PLATFORM QUARANTINE AND OUTCOME FIREWALLS",
            "ONE-HEALTH PREVENT SURGE CONTINUE COMMUNICATE RECOVER SPINE",
            "CURRENT NCDC IDSP ICMR MOHFW WHO IHR AND PABS EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE OUTBREAK EPIDEMIC PANDEMIC ENDEMIC AND THE RELEVANT EMERGENCY STATUS",
            "ASSESS TRANSMISSION EXPOSURE SEVERITY VULNERABILITY CAPACITY AND UNCERTAINTY",
            "TRACE SURVEILLANCE LAB CONFIRMATION INVESTIGATION RESPONSE AND FEEDBACK",
            "LINK ONE HEALTH HUMAN ANIMAL ENVIRONMENT SECTORS",
            "DISTINGUISH QUARANTINE FROM ISOLATION AND KEEP MEASURES PROPORTIONATE",
            "BUILD SURGE WHILE PRESERVING ESSENTIAL SERVICES COMMUNICATION AND EQUITY",
            "ASSIGN UNION STATE LOCAL NCDC ICMR WHO ROLES AND VERIFY RECOVERY OUTCOMES",
        ],
    )


TOPIC_13 = _build()
