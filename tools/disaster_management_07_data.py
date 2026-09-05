"""Authored learner-v2 data for Disaster Management Topic 07."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://mausam.imd.gov.in/responsive/cycloneinformation.php — "
        "fetched 2026-09-04; the official IMD page exposed a tropical-weather "
        "outlook link but was content-thin for warning architecture. No current "
        "storm category, track, surge height or performance claim was inferred."
    ),
    (
        "https://mausam.imd.gov.in/imd_latest/contents/pdf/cyclone_sop.pdf — "
        "fetched 2026-09-04; the official IMD SOP returned as a raw PDF. Exact "
        "classification and bulletin details remain bounded to the audited "
        "canonical owner; no operational forecast was reconstructed."
    ),
    (
        "https://mitigation.ndma.gov.in/ncrmp/ — attempted 2026-09-04; the "
        "official NDMA NCRMP portal failed at the transport layer. The module "
        "therefore records NCRMP as the completed project status already "
        "cross-checked in the owner and does not claim a Phase III."
    ),
    (
        "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2021706 — "
        "attempted 2026-09-04; the official PIB Cyclone Remal page returned "
        "HTTP 403. The case is used only as an owner-audited warning, evacuation "
        "and cascading-impact illustration, without casualty or damage figures."
    ),
    (
        "https://sachet.ndma.gov.in/ — attempted 2026-09-04; the official "
        "SACHET portal failed at the transport layer. Platform availability is "
        "not treated as proof of message receipt, evacuation or protection."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Compound cyclone hazard", "Tropical-cyclone risk combines destructive wind, intense rainfall, storm surge, waves, river or urban flooding, erosion and cascading failure of power, communications, transport and health services."),
        ("Cyclogenesis boundary", "Warm water, atmospheric instability, moisture, Coriolis force, a pre-existing disturbance and limited vertical wind shear support tropical cyclogenesis, but disaster management focuses on the resulting risk and action chain rather than detailed meteorological derivation."),
        ("Wind hazard", "Cyclone wind can damage roofs, weak structures, trees, transmission systems and communications, while debris and prolonged service interruption extend impacts beyond the landfall point."),
        ("Rainfall hazard", "Cyclone rainfall can produce riverine, flash, pluvial and urban flooding well inland, so coastal landfall warnings must connect to catchment and city preparedness."),
        ("Storm surge", "Storm surge is abnormal coastal water-level rise driven chiefly by cyclone winds and low pressure; impact varies with storm track, intensity, coast shape, bathymetry and tide."),
        ("Surge tide tsunami firewall", "Storm surge is not an astronomical tide and not a tsunami; tide can modify the total coastal water level, while tsunami generation involves sudden water displacement rather than cyclone forcing."),
        ("IMD classification", "IMD classifies cyclonic disturbances by maximum sustained wind speed and names systems from the Cyclonic Storm stage; exact category thresholds should be quoted only from the current official IMD standard."),
        ("Forecast and warning", "IMD monitoring and forecasts communicate track, intensity, rainfall, wind, sea condition, storm-surge and likely impact information with uncertainty; a forecast is not a deterministic outcome."),
        ("Action codes and bulletin stages", "Green, Yellow, Orange and Red communicate action levels, while Pre-Cyclone Watch, Cyclone Alert, Cyclone Warning and Post-Landfall Outlook form a separate lead-time bulletin sequence."),
        ("Evacuation decision", "Authorities convert official forecasts into area-specific evacuation, sheltering, route control, transport, livestock and asset-protection decisions, with priority assistance for people unable to self-evacuate."),
        ("Cyclone shelters", "Multi-purpose cyclone shelters require safe siting, all-weather access, water, sanitation, backup power, accessibility, protection, management and maintenance; construction alone does not prove readiness."),
        ("Critical-service continuity", "Hospitals, emergency operations, power, water, telecom, roads, ports and supply chains need redundancy, shutdown protocols, rapid assessment and restoration plans."),
        ("Resilient housing", "Risk-sensitive siting, code-compliant construction, roof and connection safety, maintenance and safer repair reduce housing vulnerability; exam answers should not prescribe engineering details."),
        ("Coastal ecosystems", "Mangroves, dunes, wetlands and other coastal ecosystems can moderate some wind-wave-surge effects and support livelihoods, but they complement rather than replace warnings, shelters and resilient infrastructure."),
        ("NCRMP status", "The National Cyclone Risk Mitigation Project created structural and non-structural coastal-risk assets through completed phases; asset operation, maintenance and current readiness now require separate evidence."),
        ("Differentiated coastal risk", "Cyclone frequency, coast geometry, exposure, housing, poverty, ecosystems and local capacity differ across coasts, so a lower-category or less-frequent area is not risk-free."),
        ("Livelihood preparedness", "Fishers, farmers, coastal workers, vendors and tourism-dependent households need vessel and gear safety, market and income continuity, livestock arrangements and timely reopening information."),
        ("Last-mile preparedness", "Warnings require trusted multilingual relay, drills, local volunteers, accessible transport, route familiarity and shelter management; warning issuance does not demonstrate household action."),
        ("Build Back Better", "Recovery should restore housing, services, ecosystems and livelihoods with safer siting and construction, risk-informed finance and social protection rather than recreate pre-cyclone vulnerability."),
        ("Warning-outcome firewall", "A forecast, colour code, alert, shelter, embankment, ecosystem project or deployment proves an input; timely evacuation, service continuity, maintained assets and reduced loss require separate verification."),
    ]
    traps = [
        "Do not reduce cyclone risk to wind alone.",
        "Do not confuse storm surge with tide, tsunami or ordinary high waves.",
        "Do not merge IMD action colour codes with bulletin lead-time stages.",
        "Do not quote classification thresholds without a current official IMD source.",
        "Do not treat a forecast track, category or red alert as guaranteed impact.",
        "Do not describe evacuation without transport shelter and assistance arrangements.",
        "Do not equate shelter construction with accessible maintained readiness.",
        "Do not present ecosystems as a complete substitute for built protection.",
        "Do not describe the completed NCRMP as an automatically ongoing new phase.",
        "Do not infer protection or reduced loss from warning issuance or asset creation.",
    ]
    titles = [
        "Cyclone risk as a compound hazard",
        "Cyclogenesis and risk-management boundary",
        "Wind damage debris and housing vulnerability",
        "Cyclone rainfall and inland flood cascade",
        "Storm surge tide and tsunami distinctions",
        "IMD classification naming and uncertainty",
        "Forecast products impact information and warning",
        "Colour action codes versus bulletin stages",
        "Evacuation transport livestock and route control",
        "Cyclone shelters accessibility and maintenance",
        "Critical services ports and supply continuity",
        "Resilient housing and risk-sensitive siting",
        "Coastal ecosystems livelihoods and residual risk",
        "NCRMP asset hand-off and last-mile preparedness",
        "Build Back Better and warning-outcome boundary",
    ]
    routes = [
        "Name wind rain surge waves flooding and service cascades.",
        "State the formation requirements briefly and return to risk management.",
        "Connect wind exposure to weak housing debris and utilities.",
        "Trace landfall rain into basin city and inland preparedness.",
        "Separate all three coastal water-level mechanisms.",
        "Use only current official IMD classification and naming language.",
        "Communicate uncertainty and impact without deterministic claims.",
        "Explain action level and lead-time sequence as different systems.",
        "Convert warning into area transport shelter livestock and inclusion decisions.",
        "Test siting access services management maintenance and accessibility.",
        "Protect emergency health power water telecom port and road functions.",
        "Keep construction measures exam-safe and governance-focused.",
        "Balance ecosystem protection livelihood needs and residual risk.",
        "Move from completed project assets to current operation and drills.",
        "End with safer recovery and verified outcomes.",
    ]
    panels = [
        common.panel("Compound cyclone hazard map", "systems-map", [
            "WIND -> structure debris power telecom",
            "RAIN -> riverine flash pluvial urban flood",
            "STORM SURGE + WAVES -> coastal inundation erosion",
            "CASCADE -> transport health water and livelihoods",
        ], ["Compound cyclone hazard", "Wind hazard", "Rainfall hazard"]),
        common.panel("Cyclogenesis boundary", "process-flow", [
            "WARM WATER + INSTABILITY + MOISTURE",
            "CORIOLIS + DISTURBANCE + LIMITED SHEAR",
            "CYCLONIC SYSTEM",
            "DM FOCUS -> exposure warning action continuity",
        ], ["Cyclogenesis boundary"]),
        common.panel("Coastal water firewall", "comparison-table", [
            "STORM SURGE -> cyclone wind and pressure",
            "TIDE -> astronomical gravitational cycle",
            "TSUNAMI -> sudden water displacement",
            "TOTAL WATER LEVEL -> interacting but distinct components",
        ], ["Storm surge", "Surge tide tsunami firewall"]),
        common.panel("IMD information rail", "numbered-rail", [
            "1 OBSERVE / ANALYSE",
            "2 CLASSIFY / FORECAST TRACK AND INTENSITY",
            "3 ISSUE IMPACT AND HAZARD INFORMATION",
            "4 UPDATE AS UNCERTAINTY CHANGES",
        ], ["IMD classification", "Forecast and warning"]),
        common.panel("Colour-stage matrix", "matrix", [
            "GREEN / YELLOW / ORANGE / RED -> ACTION LEVEL",
            "WATCH / ALERT / WARNING / POST-LANDFALL -> BULLETIN STAGE",
            "COLOUR != LEAD-TIME SEQUENCE",
            "BOTH -> require local action protocol",
        ], ["Action codes and bulletin stages"]),
        common.panel("Warning-to-evacuation chain", "process-flow", [
            "OFFICIAL FORECAST -> AREA DECISION",
            "TRANSPORT + ROUTE + LIVESTOCK / ASSET PLAN",
            "ACCESSIBLE SHELTER + REGISTRATION",
            "ALL CLEAR / RETURN -> COMPETENT AUTHORITY",
        ], ["Evacuation decision", "Last-mile preparedness"]),
        common.panel("Shelter readiness test", "decision-tree", [
            "SAFE SITE AND ACCESS?",
            "WATER SANITATION POWER ACCESSIBILITY?",
            "TRAINED MANAGEMENT AND MAINTENANCE?",
            "NO -> ASSET EXISTS BUT READINESS UNPROVEN",
        ], ["Cyclone shelters"]),
        common.panel("Critical-service web", "network-map", [
            "EOC / HOSPITAL / RESCUE",
            "POWER / WATER / TELECOM",
            "ROAD / PORT / SUPPLY CHAIN",
            "REDUNDANCY -> ASSESS -> RESTORE",
        ], ["Critical-service continuity"]),
        common.panel("Housing-to-ecosystem portfolio", "comparison-table", [
            "HOUSING -> siting code compliance maintenance",
            "INFRASTRUCTURE -> lifeline hardening and redundancy",
            "ECOSYSTEM -> mangrove dune wetland protection",
            "RULE -> layered defence with residual risk",
        ], ["Resilient housing", "Coastal ecosystems"]),
        common.panel("NCRMP status ladder", "status-ladder", [
            "PROJECT APPROVAL -> ASSET CREATION",
            "PHASE COMPLETION -> STATE / LOCAL HAND-OFF",
            "OPERATION + MAINTENANCE + DRILLS",
            "CURRENT READINESS -> needs separate evidence",
        ], ["NCRMP status"]),
        common.panel("Livelihood recovery loop", "feedback-loop", [
            "WARNING -> BOAT GEAR LIVESTOCK AND MARKET ACTION",
            "IMPACT -> RELIEF + SOCIAL PROTECTION",
            "REPAIR / REOPEN -> SAFER CONDITIONS",
            "BUILD BACK BETTER -> REDUCE FUTURE EXPOSURE",
        ], ["Livelihood preparedness", "Build Back Better"]),
        common.panel("Cyclone answer spine", "answer-spine", [
            "DEFINE COMPOUND HAZARD -> SEPARATE SURGE TIDE TSUNAMI",
            "MAP IMD CLASSIFICATION FORECAST COLOUR AND BULLETIN STAGE",
            "CONNECT EVACUATION SHELTER LIFELINES HOUSING AND ECOSYSTEMS",
            "ADD LIVELIHOODS BBB MAINTENANCE AND OUTCOME QUALIFICATION",
        ], ["Differentiated coastal risk", "Warning-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2022", "GS-I",
            "Discuss the meaning of colour-coded weather warnings for cyclone-prone areas.",
            "Verified direct routing: Discuss the meaning · 10 marks · 150 words; the solution must distinguish action colours from the separate cyclone bulletin sequence.",
            [7, 8, 9, 17, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe the elements that determine disaster resilience.",
            "Verified direct ownership remains Topic 01; this conservative card routes shelters, lifeline continuity, resilient housing, ecosystems, livelihoods and recovery as cyclone-resilience elements.",
            [10, 11, 12, 13, 16, 17, 18, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss causes, cases, policies and frameworks for urban flooding.",
            "Verified direct ownership remains Topic 08; this card is limited to cyclone rainfall, storm surge and service-cascade contributions to coastal and urban flooding.",
            [0, 3, 4, 7, 9, 11, 19]),
    ]
    return common.topic(
        7, "Cyclones, Storm Surge and Coastal Preparedness",
        "07_Cyclones-Storm-Surge-and-Coastal-Preparedness", facts, traps,
        [
            (10, "Distinguish cyclone wind, rainfall and storm-surge hazards.", [0, 2, 3, 4, 5]),
            (10, "Explain how IMD classification, forecasts, action codes and bulletin stages differ.", [6, 7, 8]),
            (15, "Analyse the warning-to-evacuation and cyclone-shelter preparedness chain.", [7, 8, 9, 10, 17, 19]),
            (15, "Examine resilient housing, critical services and coastal ecosystems as a layered cyclone-risk portfolio.", [11, 12, 13, 15]),
            (20, "Evaluate India's coastal cyclone preparedness after NCRMP, focusing on maintenance, last-mile action and differentiated risk.", [9, 10, 11, 14, 15, 16, 17, 19]),
            (20, "Design a Build Back Better framework for cyclone-affected coastal communities and livelihoods.", [0, 11, 12, 13, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "storm surge", "cyclogenesis", "ACWCs", "CWCs",
            "colour codes", "Pre-Cyclone Watch", "Cyclone Alert",
            "Cyclone Warning", "Post-Landfall Outlook", "NCRMP",
            "cyclone shelters", "saline embankments", "bio-shields",
            "grass root", "Aircraft Probing of Cyclone",
        ],
        "The 2022 GS-I warning-colour card is directly routed. The two 2024 GS-III cards are conservative resilience and flood-cascade applications and retain Topics 01 and 08 as primary owners.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered IMD cyclone services and SOP material, NDMA's NCRMP portal, PIB's Cyclone Remal case and SACHET. Raw, thin, blocked or transport-failed pages are logged; no track, landfall, surge, rainfall, casualty, damage, shelter-readiness or avoided-loss figure was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "WIND RAIN STORM-SURGE CASCADE AND COASTAL-RISK MAP",
            "IMD CLASSIFICATION COLOUR BULLETIN EVACUATION AND SHELTER FIREWALLS",
            "LIFELINE HOUSING ECOSYSTEM LIVELIHOOD AND BBB ANSWER SPINE",
            "CURRENT IMD NDMA NCRMP AND WARNING-OUTCOME EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE CYCLONE RISK AS WIND RAIN SURGE WAVES AND CASCADES",
            "DISTINGUISH STORM SURGE TIDE TSUNAMI AND TOTAL WATER LEVEL",
            "NAME IMD CLASSIFICATION FORECAST UNCERTAINTY AND OFFICIAL WARNING",
            "SEPARATE ACTION COLOUR CODES FROM BULLETIN LEAD-TIME STAGES",
            "CONVERT WARNING INTO INCLUSIVE EVACUATION AND MAINTAINED SHELTER",
            "PROTECT HOUSING LIFELINES ECOSYSTEMS AND LIVELIHOODS",
            "BUILD BACK BETTER AND VERIFY ACTION CONTINUITY AND OUTCOME",
        ],
    )


TOPIC_07 = _build()
