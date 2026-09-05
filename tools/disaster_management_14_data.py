"""Authored learner-v2 data for Disaster Management Topic 14."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://ndma.gov.in/Resources/awareness/Urban-Flooding — attempted "
        "2026-09-04; the NDMA route failed at the transport layer. "
        "https://mohua.gov.in/documents/publications/manuals-and-advisories-"
        "MDMwYTMtQWa?pageTitle=Manuals-And-Advisories — searched 2026-09-04; "
        "official results exposed urban-flood preparedness and drainage "
        "advisories, while the MoHUA home page itself returned HTTP 403."
    ),
    (
        "https://www.bis.gov.in/standards/national-building-code/?lang=en — "
        "searched 2026-09-04; official BIS results identified the National "
        "Building Code and disaster-mitigation standards route. "
        "https://www.mha.gov.in/en/commoncontent/disaster-management-act-2005 "
        "— attempted 2026-09-04; MHA returned HTTP 403. No city-level code "
        "compliance or retrofit outcome was inferred."
    ),
    (
        "https://cdri.world/ — fetched 2026-09-04; CDRI described its purpose "
        "as enhancing infrastructure-system resilience to climate and disaster "
        "risk. https://www.undrr.org/implementing-sendai-framework/what-sendai-"
        "framework — fetched 2026-09-04 for the structural/non-structural "
        "investment and Build Back Better boundary."
    ),
    (
        "https://amrut.mohua.gov.in/uploads/saasci/B1-Innovative-Method.pdf — "
        "searched 2026-09-04; the official AMRUT route surfaced sponge-city "
        "interventions. https://pib.gov.in/ — searched 2026-09-04 for official "
        "urban-programme corroboration; no completion, loss-avoidance or city "
        "ranking claim was imported."
    ),
    (
        "https://cea.nic.in/ps___lf/97719/?lang=en — searched 2026-09-04; "
        "official CEA results identified the Disaster Management Plan 2024 for "
        "the power sector. https://dot.gov.in/static/uploads/2025/07/"
        "0484fb15ff3f823ec7301b720112129e.pdf — searched 2026-09-04; official "
        "DoT results identified the telecom disaster-response SOP route. "
        "https://ndma.gov.in/ — attempted 2026-09-04; no sector readiness, "
        "uptime, restoration or compliance outcome was inferred."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Urban disaster risk", "Urban disaster risk arises where hazards interact with dense populations, concentrated assets, unequal vulnerability and tightly coupled services; it is not merely a rural hazard occurring inside municipal limits."),
        ("Systemic and cascading failure", "A disruption becomes systemic when failure propagates across connected services, such as electricity loss disabling pumping, telecom, hospitals, traffic management and emergency response."),
        ("Critical infrastructure and lifelines", "Critical infrastructure and lifelines are assets, networks and services whose disruption causes disproportionate effects on life, health, safety, governance or economic functioning; criticality depends on function and consequence, not ownership alone."),
        ("Interdependency mapping", "Interdependency mapping identifies physical, digital, geographic and organisational dependencies among water, power, transport, health, telecom, sanitation and emergency systems before prioritising protection."),
        ("Robustness redundancy and rapid recovery", "Robustness resists disruption, redundancy supplies alternative capacity or routes, and rapid recovery restores priority functions; the three are complementary and should not be used as synonyms."),
        ("Service continuity", "Continuity planning fixes minimum acceptable service, priority users, backup resources, alternate sites, manual workarounds, communication and restoration order before an incident."),
        ("Risk-informed land use", "Risk-informed land use keeps hazardous locations, drainage paths, evacuation routes and critical-service access visible in development control rather than treating hazard maps as stand-alone documents."),
        ("Building-code and retrofit chain", "Safer construction requires current risk-sensitive standards, municipal adoption, competent design, site supervision, occupancy control, maintenance and retrofit of vulnerable existing stock; publication of a code proves none of the later links."),
        ("Urban drainage governance", "Urban drainage resilience combines catchment-scale planning, protected natural drains and water bodies, adequate conveyance, solid-waste control, maintenance, pumping where needed and coordination across municipal boundaries."),
        ("Criticality-based prioritisation", "A resilience audit should identify single points of failure, dependency concentration, vulnerable locations, backup duration, restoration time and populations affected, then rank interventions by consequence."),
        ("Hospitals and emergency facilities", "Hospitals, emergency operations centres, fire services, shelters and control rooms require structural safety plus dependable water, power, oxygen or clinical support, communications, access and supply continuity."),
        ("Informal settlements and equity", "Informal settlements often combine high exposure, insecure tenure, weak drainage and intermittent services; resilience measures must protect residents and access rather than use risk reduction as a pretext for exclusionary displacement."),
        ("Accessible lifelines", "Continuity standards should account for persons with disabilities, older people, children, migrants, low-income households and people dependent on medical or mobility services, because equal nominal supply does not ensure equal access."),
        ("Urban institutions", "ULBs, utilities, development authorities, districts, SDMAs and sector regulators retain different mandates; a city resilience mechanism coordinates them without erasing statutory or technical responsibility."),
        ("Urban Flooding Cell status", "The Urban Flooding Cell is an NDMA 2010 guideline recommendation whose actual constitution and operation require separate notification evidence; a recommendation is not an automatically functioning institution."),
        ("Urban Disaster Management Authority status", "The statutory enabling provision for an Urban Disaster Management Authority does not prove that every city has constituted or operationalised one; State notification and local evidence remain necessary."),
        ("CDRI boundary", "CDRI supports disaster-resilient infrastructure through risk knowledge, standards, finance and recovery cooperation, but coalition membership or a publication is not domestic operational command or proof that an asset is resilient."),
        ("Smart technology and privacy", "Sensors, digital twins, cameras, integrated command platforms and predictive analytics can improve situational awareness, but resilience requires cybersecurity, privacy, interoperability, offline fallback and accountable human decisions."),
        ("Resilience versus efficiency", "Highly efficient just-in-time and centralised systems can remove spare capacity; resilience may deliberately retain buffers, diversity and redundancy even when they appear costly during normal operations."),
        ("Input-outcome firewall", "A plan, code, audit, dashboard, smart-city platform, sanctioned project or authority proves an input or status only; continuity, equitable access, shorter restoration and reduced losses require separate evidence."),
    ]
    traps = [
        "Do not reduce urban resilience to stronger buildings or larger drains.",
        "Do not use critical infrastructure and all infrastructure as synonyms.",
        "Do not confuse robustness, redundancy and rapid recovery.",
        "Do not infer interdependency management from separate utility plans.",
        "Do not treat code publication as municipal enforcement or retrofit completion.",
        "Do not assume every city has an operating Urban Flooding Cell or UDMA.",
        "Do not infer asset resilience from CDRI membership, a dashboard or project sanction.",
        "Do not let smart surveillance erase privacy, cybersecurity or offline fallback.",
        "Do not equate normal-time efficiency with shock resilience.",
        "Do not displace informal settlements in the name of resilience without safeguards and access.",
    ]
    titles = [
        "Urban risk density exposure vulnerability and systemic character",
        "Critical infrastructure lifelines and consequence-based criticality",
        "Cascading failure and physical digital geographic dependencies",
        "Robustness redundancy diversity and rapid recovery",
        "Continuity planning minimum service and restoration priorities",
        "Risk-informed land use drainage and water-sensitive planning",
        "Building codes enforcement maintenance and existing-stock retrofit",
        "Hospitals EOCs utilities and emergency-service continuity",
        "Resilience audits single points of failure and recovery time",
        "ULBs utilities districts regulators and cross-system coordination",
        "Informal settlements vulnerable groups and equitable lifeline access",
        "Smart sensors command platforms privacy and cyber resilience",
        "Resilience versus efficiency buffers and just-in-time trade-offs",
        "CDRI urban institutions finance and Build Back Better",
        "PYQ synthesis audits continuity and outcome firewall",
    ]
    routes = [
        "Define urban risk as a coupled social-infrastructure system.",
        "Classify criticality by consequence and service function.",
        "Trace at least one multi-lifeline cascade and its dependency.",
        "Prescribe resistance alternatives and restoration together.",
        "State minimum service priority users fallback and recovery time.",
        "Join land use hydrology drainage maintenance and enforcement.",
        "Separate standards adoption enforcement maintenance and retrofit.",
        "Protect both the facility and every service dependency it needs.",
        "Rank single points dependencies backup duration and affected users.",
        "Allocate mandates then create an accountable coordination bridge.",
        "Test access affordability displacement safeguards and inclusion.",
        "Use technology with privacy cyber interoperability and manual fallback.",
        "Justify buffers and diversity against brittle efficiency.",
        "Separate international standards from city operations and outcomes.",
        "Conclude with verified continuity equity and restoration evidence.",
    ]
    panels = [
        common.panel("Urban risk system", "systems-map", [
            "HAZARD + DENSITY + EXPOSED ASSETS + UNEQUAL VULNERABILITY",
            "-> INTERDEPENDENT WATER POWER TRANSPORT HEALTH TELECOM",
            "-> CASCADING SERVICE FAILURE",
            "-> SYSTEMIC URBAN DISASTER",
        ], ["Urban disaster risk", "Systemic and cascading failure"]),
        common.panel("Criticality test", "decision-tree", [
            "ASSET / NETWORK / SERVICE",
            "IF FAILURE -> DISPROPORTIONATE LIFE / HEALTH / GOVERNANCE EFFECT",
            "THEN CRITICAL / LIFELINE FUNCTION",
            "PRIORITY DEPENDS ON CONSEQUENCE, NOT OWNERSHIP OR SIZE",
        ], ["Critical infrastructure and lifelines"]),
        common.panel("Interdependency web", "network-map", [
            "POWER -> WATER PUMPS / HOSPITALS / TELECOM",
            "TELECOM -> WARNING / DISPATCH / PAYMENT",
            "TRANSPORT -> STAFF / SUPPLY / REPAIR ACCESS",
            "SHARED NODE FAILURE -> MULTI-SYSTEM CASCADE",
        ], ["Interdependency mapping", "Systemic and cascading failure"]),
        common.panel("Resilience triad", "comparison-table", [
            "ROBUSTNESS -> RESIST",
            "REDUNDANCY / DIVERSITY -> ALTERNATE CAPACITY",
            "RAPID RECOVERY -> RESTORE PRIORITY FUNCTION",
            "COMPLETE RESILIENCE NEEDS ALL THREE",
        ], ["Robustness redundancy and rapid recovery"]),
        common.panel("Continuity plan", "process-flow", [
            "DEFINE MINIMUM SERVICE + PRIORITY USERS",
            "MAP STAFF SUPPLY DATA SITE AND UTILITY DEPENDENCIES",
            "PROVIDE BACKUP / ALTERNATE / MANUAL MODE",
            "SET RESTORATION ORDER TIME AND COMMUNICATION",
        ], ["Service continuity"]),
        common.panel("Urban planning stack", "layered-map", [
            "LAND USE / FLOODPLAIN / DRAINAGE PATH",
            "BUILDING AND DEVELOPMENT CONTROL",
            "WATER BODY DRAIN SOLID-WASTE AND MAINTENANCE",
            "WARD-CITY-CATCHMENT COORDINATION",
        ], ["Risk-informed land use", "Building-code and retrofit chain", "Urban drainage governance"]),
        common.panel("Resilience audit", "audit-ladder", [
            "1 CRITICAL FUNCTION AND USERS",
            "2 HAZARD LOAD + DEPENDENCIES + SINGLE POINTS",
            "3 BACKUP DURATION + RECOVERY TIME",
            "4 PRIORITISED RETROFIT CONTINUITY AND DRILL ACTION",
        ], ["Criticality-based prioritisation"]),
        common.panel("Essential facility shell", "matrix", [
            "STRUCTURE / FIRE / FLOOD SAFETY",
            "POWER WATER CLINICAL SUPPLY AND TELECOM",
            "ACCESS STAFF REFERRAL AND SECURITY",
            "CONTINUE CARE WHILE DAMAGE IS REPAIRED",
        ], ["Hospitals and emergency facilities"]),
        common.panel("Equity access test", "balance-sheet", [
            "WHO LIVES IN HIGHEST EXPOSURE?",
            "WHO DEPENDS ON INTERRUPTIBLE OR INFORMAL SERVICES?",
            "WHO CAN REACH WARNING SHELTER HEALTH AND TRANSPORT?",
            "RISK REDUCTION WITHOUT EXCLUSIONARY DISPLACEMENT",
        ], ["Informal settlements and equity", "Accessible lifelines"]),
        common.panel("Governance map", "systems-map", [
            "ULB / UTILITY / DEVELOPMENT AUTHORITY / DISTRICT",
            "SECTOR REGULATOR + SDMA / NDMA",
            "COORDINATION DOES NOT ERASE OWNER DUTY",
            "RECOMMENDATION / ENABLING LAW / NOTIFICATION / OPERATION",
        ], ["Urban institutions", "Urban Flooding Cell status", "Urban Disaster Management Authority status"]),
        common.panel("Smart resilience firewall", "trade-off-matrix", [
            "SENSORS / DIGITAL TWIN / COMMAND PLATFORM -> AWARENESS",
            "PRIVACY + CYBERSECURITY + INTEROPERABILITY",
            "OFFLINE FALLBACK + HUMAN ACCOUNTABILITY",
            "EFFICIENCY WITHOUT BUFFER -> BRITTLE SYSTEM",
        ], ["Smart technology and privacy", "Resilience versus efficiency"]),
        common.panel("Urban resilience answer spine", "answer-spine", [
            "DEFINE SYSTEMIC URBAN RISK AND CRITICAL LIFELINES",
            "MAP CASCADES -> ROBUSTNESS REDUNDANCY CONTINUITY",
            "ADD LAND USE CODES DRAINAGE AUDIT EQUITY AND GOVERNANCE",
            "USE CDRI / TECHNOLOGY WITH STATUS AND OUTCOME FIREWALLS",
        ], ["CDRI boundary", "Input-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss urban flooding as a climate-induced disaster and the policies and frameworks in India that aim at tackling it.",
            "Verified direct adjacent route owned by Topic 08; this card contributes urban-system, drainage, lifeline, institutional and continuity dimensions without replacing the flood-specific answer.",
            [0, 1, 5, 6, 7, 8, 13, 14, 15, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, how it is determined and the elements of the Sendai Framework.",
            "Verified support route: apply resilience determination to critical functions, dependencies, robustness, redundancy, recovery time and equity.",
            [2, 3, 4, 5, 9, 11, 12, 19]),
        common.make_pyq_solution(facts, "2023", "GS-III",
            "Analyse the causes and catastrophic downstream effects of dam failures with examples.",
            "Verified cross-owned route led by Topic 08; use only cascading lifeline failure, continuity and interdependency as bounded infrastructure-resilience support.",
            [1, 2, 3, 4, 5, 9, 19]),
    ]
    return common.topic(
        14, "Urban and Critical Infrastructure Resilience",
        "14_Urban-and-Critical-Infrastructure-Resilience", facts, traps,
        [
            (10, "Distinguish critical infrastructure, lifelines, robustness, redundancy and rapid recovery.", [2, 4]),
            (10, "Explain why service-continuity planning is essential for urban lifelines.", [3, 4, 5, 10]),
            (15, "Analyse systemic and cascading urban infrastructure failure.", [0, 1, 2, 3, 4]),
            (15, "Examine land-use, building-code, drainage and service-governance requirements for urban resilience.", [6, 7, 8, 13, 14, 15]),
            (20, "Design an equitable resilience-audit and continuity framework for a city's critical infrastructure.", [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 19]),
            (20, "Critically evaluate smart-city technology and efficiency-led infrastructure from a disaster-resilience perspective.", [1, 3, 4, 5, 9, 11, 12, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Urban risk", "critical infrastructure", "lifeline",
            "service continuity", "Coalition for Disaster Resilient Infrastructure",
            "structural", "non-structural", "risk assessment",
            "Build Back Better", "Urban Flooding Cell", "criticality mapping",
            "informal settlements", "redundancy",
        ],
        "The 2024 urban-flood card is the closest verified direct application but remains Topic 08-owned. The 2024 resilience card is a direct conceptual support route; the 2023 dam-failure card is cross-owned infrastructure-cascade support.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered NDMA and MoHUA urban-flood routes, BIS building standards, AMRUT sponge-city material, CDRI and UNDRR. Blocked, transport-failed and search-only pages are recorded; no project completion, city ranking, code compliance, continuity result, avoided loss or resilience outcome was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "URBAN SYSTEM LIFELINE CASCADE AND CRITICALITY MAP",
            "CODE AUTHORITY SMART-TECH PROJECT AND OUTCOME FIREWALLS",
            "ROBUST REDUNDANT CONTINUOUS EQUITABLE RAPID-RECOVERY SPINE",
            "CURRENT NDMA MOHUA BIS AMRUT CDRI AND UNDRR EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE URBAN SYSTEMIC RISK AND CONSEQUENCE-BASED CRITICAL INFRASTRUCTURE",
            "MAP PHYSICAL DIGITAL GEOGRAPHIC AND ORGANISATIONAL INTERDEPENDENCIES",
            "DESIGN ROBUSTNESS REDUNDANCY DIVERSITY AND RAPID RECOVERY",
            "SET MINIMUM SERVICE PRIORITY USERS BACKUPS AND RESTORATION TIME",
            "LINK LAND USE BUILDING CODES RETROFIT DRAINAGE AND MAINTENANCE",
            "AUDIT SINGLE POINTS OF FAILURE AND PROTECT INFORMAL / VULNERABLE USERS",
            "ASSIGN ULB UTILITY DISTRICT REGULATOR CDRI ROLES AND VERIFY OUTCOMES",
        ],
    )


TOPIC_14 = _build()
