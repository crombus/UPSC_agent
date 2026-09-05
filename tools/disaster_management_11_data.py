"""Authored learner-v2 data for Disaster Management Topic 11."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://fsi.nic.in/focus-areas?pgID=focus-areas — fetched "
        "2026-09-04; FSI described MODIS and SNPP-VIIRS near-real-time "
        "detection, automated dissemination, Large Forest Fire monitoring and "
        "danger-rating development. https://www.isro.gov.in/"
        "DisasterManagementSupport.html — fetched 2026-09-04 but returned "
        "only a thin title. No response-time or containment outcome was inferred."
    ),
    (
        "https://fsiforestfire.gov.in/ — fetched 2026-09-04; the official FSI "
        "dashboard returned only an SMS-registration notice. "
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2035043 — attempted "
        "2026-09-04; PIB returned HTTP 403, so the FPM Scheme is used only at "
        "the owner-verified centrally sponsored support rung."
    ),
    (
        "https://moef.gov.in/forest-protection-forest-fire — attempted "
        "2026-09-04; the official MoEFCC route returned HTTP 404. "
        "https://ndma.gov.in/Natural-Hazards/Forest-Fire — attempted "
        "2026-09-04; the NDMA page failed at the transport layer. No current "
        "budget, incidence, crew-capacity or national-readiness claim was added."
    ),
    (
        "https://nidm.gov.in/iec.asp — searched 2026-09-04; the official NIDM "
        "awareness-material route was identified. No fire-behaviour, crew "
        "readiness, containment or ecological-outcome proposition was imported."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Fire triangle", "Combustion requires fuel, heat and oxygen; forest-fire prevention and suppression act by limiting ignition, fuel continuity or heat transfer without assuming every forest can be made fire-free."),
        ("Fire behaviour", "Rate and direction of spread, flame intensity, spotting and persistence are shaped by fuel condition and arrangement, weather and topography; detection alone does not reveal safe tactical access."),
        ("Surface fire", "A surface fire burns litter, grasses, shrubs and other material near the ground and may provide the heat pathway into tree crowns."),
        ("Ground fire", "A ground fire burns organic matter below or within the surface layer and can persist or re-emerge, making it distinct from a visible surface flame front."),
        ("Crown fire", "A crown fire spreads through tree canopies, often supported by surface fire and fuel continuity; it is not simply a larger surface fire."),
        ("Ignition sources", "Natural ignition can include lightning, while human ignition may be deliberate or accidental through land or resource use, discarded smoking material, escaped burning, equipment or other heat sources."),
        ("Weather", "Temperature, humidity, wind and recent precipitation affect fuel dryness, ignition probability, spread and smoke, but a weather signal is not proof that a fire will start or be contained."),
        ("Fuel", "Fuel type, load, moisture, continuity and vertical arrangement influence fire behaviour; unmanaged accumulation, invasive biomass or post-disturbance debris can alter risk."),
        ("Topography", "Slope, aspect, valleys and access shape heating, wind and spread as well as crew movement; fire commonly moves faster upslope, but site conditions remain decisive."),
        ("Prevention governance", "Prevention combines locally legitimate resource-use rules, awareness, patrols, equipment maintenance, fire-season readiness and action on recurrent human ignition rather than relying only on punitive messaging."),
        ("Detection and FSI", "FSI's satellite-based monitoring processes MODIS and SNPP-VIIRS detections and disseminates alerts, while Large Forest Fire monitoring tracks selected events; these systems locate possible fire, not field suppression."),
        ("Initial response", "Initial response requires rapid verification, incident reporting, trained and protected crews, access assessment, local command, communication, water or tools suited to the setting and escalation when capacity is exceeded."),
        ("Community partnership", "Forest-dependent and forest-fringe communities can support prevention, early reporting and response when participation is institutionalised, compensated, trained and linked to State responsibility rather than used as unpaid crisis labour."),
        ("Fire lines", "Fire lines are breaks in fuel continuity maintained for prevention or control; their usefulness depends on placement, width, maintenance, terrain and conditions and they do not guarantee containment."),
        ("Prescribed burning boundary", "Prescribed burning is a planned, authorised and ecologically informed fuel-management concept with objectives, weather limits, trained supervision, contingency arrangements and monitoring; it is not permission for uncontrolled ignition."),
        ("Ecology-suppression trade-off", "Some ecosystems and livelihoods interact with periodic fire, while severe or poorly timed fire can damage life, assets and ecological function; universal exclusion or universal burning are both unsafe prescriptions."),
        ("Smoke and health", "Smoke can expose firefighters and communities to hazardous air pollution, reduce visibility and disrupt transport or services, requiring public-health communication, protective measures and continuity planning."),
        ("Wildland-urban interface", "Settlements, roads, tourism sites and utilities at the forest edge create two-way exposure between vegetation fire and structures, requiring defensible planning, evacuation routes and utility coordination."),
        ("Restoration", "Post-fire work may include safety assessment, burnt-area and severity mapping, erosion and runoff control, invasive-species surveillance, livelihood support and ecologically suitable restoration rather than automatic mass planting."),
        ("Alert-outcome firewall", "A hotspot, danger rating, SMS, fire line, trained crew, scheme or restoration plan proves an input; verified ignition reduction, safe response, containment, health protection and ecological recovery require separate evidence."),
    ]
    traps = [
        "Do not omit ground fire or collapse all fire types into surface and crown.",
        "Do not treat every forest fire as unnatural or every fire as ecologically beneficial.",
        "Do not convert a weather or danger rating into certainty that ignition will occur.",
        "Do not confuse satellite detection with field verification or suppression.",
        "Do not describe communities as a substitute for trained and accountable State capacity.",
        "Do not present fire lines as maintenance-free or guaranteed barriers.",
        "Do not provide actionable ignition detail or portray prescribed burning as uncontrolled burning.",
        "Do not recommend total suppression without considering fuel and ecosystem context.",
        "Do not omit smoke, responder safety, evacuation and service continuity.",
        "Do not infer containment or restoration success from an alert, scheme or plan.",
    ]
    titles = [
        "Fire triangle and bounded fire-behaviour grammar",
        "Surface ground and crown fire distinctions",
        "Natural deliberate and accidental ignition",
        "Weather fuel topography and spread interaction",
        "Prevention governance and recurrent-use incentives",
        "FSI satellite detection danger rating and alert chain",
        "Field verification initial response and escalation",
        "Community participation training compensation and accountability",
        "Fire lines access and maintenance limits",
        "Prescribed burning as bounded governance",
        "Ecological role versus suppression trade-offs",
        "Smoke health visibility and service continuity",
        "Wildland-urban interface evacuation and utilities",
        "Burnt-area assessment restoration and livelihood recovery",
        "PYQ synthesis alert suppression and outcome firewall",
    ]
    routes = [
        "Start with fuel heat oxygen and identify the controllable link.",
        "Classify the burning layer before discussing behaviour or response.",
        "Separate natural ignition from deliberate and accidental human causes.",
        "Explain interaction rather than assigning spread to one variable.",
        "Address incentives rules readiness and recurrent local practices.",
        "Trace sensor processing dissemination and field-verification boundaries.",
        "Move from alert to safe verification command resources and escalation.",
        "Design participation with training compensation and continuing State duty.",
        "Evaluate placement maintenance conditions and residual risk.",
        "Keep the concept authorised planned supervised monitored and non-instructional.",
        "Balance life safety fuel accumulation ecosystem process and livelihood use.",
        "Add health advisories visibility worker safety and essential services.",
        "Treat forest-edge settlements and infrastructure as a distinct risk interface.",
        "Sequence safety erosion severity livelihood and ecological restoration.",
        "Conclude with measured alert-to-action and recovery evidence.",
    ]
    panels = [
        common.panel("Fire triangle and control", "systems-map", [
            "FUEL + HEAT + OXYGEN -> COMBUSTION",
            "PREVENT -> reduce unsafe ignition / fuel continuity",
            "RESPOND -> interrupt heat transfer where safe",
            "LIMIT -> FIRE-FREE FOREST IS NOT A UNIVERSAL GOAL",
        ], ["Fire triangle"]),
        common.panel("Fire-type matrix", "matrix", [
            "SURFACE -> litter grass shrub layer",
            "GROUND -> organic matter below / within surface",
            "CROWN -> tree canopy",
            "TRANSITION -> vertical fuel and conditions connect layers",
        ], ["Surface fire", "Ground fire", "Crown fire"]),
        common.panel("Fire-behaviour triangle", "causal-chain", [
            "WEATHER -> dryness wind humidity temperature",
            "FUEL -> type load moisture continuity",
            "TOPOGRAPHY -> slope aspect valley access",
            "INTERACTION -> spread intensity smoke and response limits",
        ], ["Fire behaviour", "Weather", "Fuel", "Topography"]),
        common.panel("Ignition governance map", "comparison-table", [
            "NATURAL -> lightning and source-bounded causes",
            "DELIBERATE HUMAN -> land / resource-use motive",
            "ACCIDENTAL HUMAN -> escaped heat / equipment / smoking",
            "RESPONSE -> prevention by cause not generic blame",
        ], ["Ignition sources", "Prevention governance"]),
        common.panel("FSI alert rail", "numbered-rail", [
            "1 MODIS / SNPP-VIIRS DETECTION",
            "2 AUTOMATED PROCESSING AND FOREST FILTER",
            "3 SMS / EMAIL / MAP DISSEMINATION",
            "4 FIELD VERIFY -> COMMAND -> RESPONSE",
        ], ["Detection and FSI", "Alert-outcome firewall"]),
        common.panel("Initial response chain", "process-flow", [
            "ALERT -> VERIFY LOCATION AND ACCESS",
            "LOCAL COMMAND + TRAINED PROTECTED CREW",
            "TOOLS WATER COMMUNICATION AND SAFETY",
            "ESCALATE IF CAPACITY / CONDITIONS EXCEEDED",
        ], ["Initial response"]),
        common.panel("Community partnership ladder", "status-ladder", [
            "CONSULT ON RESOURCE-USE AND IGNITION DRIVERS",
            "TRAIN + EQUIP + COMPENSATE",
            "LINK EARLY REPORTING TO FOREST DEPARTMENT",
            "DO NOT OFFLOAD STATE DUTY",
        ], ["Community partnership"]),
        common.panel("Fuel-break boundary", "comparison-table", [
            "FIRE LINE -> maintained break in fuel continuity",
            "PRESCRIBED BURN -> authorised planned fuel treatment",
            "BOTH -> objectives conditions supervision contingency",
            "NEITHER -> guaranteed containment or licence for ignition",
        ], ["Fire lines", "Prescribed burning boundary"]),
        common.panel("Ecology-suppression balance", "decision-tree", [
            "WHAT ECOSYSTEM / FIRE REGIME / SEASON / INTENSITY?",
            "LIFE OR ASSET THREAT -> SAFETY-LED RESPONSE",
            "FUEL / ECOLOGY OBJECTIVE -> BOUNDED MANAGEMENT",
            "TRAP -> UNIVERSAL EXCLUSION OR UNIVERSAL BURNING",
        ], ["Ecology-suppression trade-off"]),
        common.panel("Smoke and interface map", "network-map", [
            "FIRE -> SMOKE / VISIBILITY / TRANSPORT",
            "FOREST EDGE -> HOME ROAD POWER TOURISM SITE",
            "HEALTH MESSAGE + EVACUATION + UTILITY ACTION",
            "RESPONDER AND VULNERABLE-GROUP PROTECTION",
        ], ["Smoke and health", "Wildland-urban interface"]),
        common.panel("Restoration sequence", "process-flow", [
            "SAFETY + BURNT AREA / SEVERITY ASSESSMENT",
            "EROSION RUNOFF AND INVASIVE-SPECIES CONTROL",
            "LIVELIHOOD SUPPORT + ECOLOGICALLY SUITABLE RESTORATION",
            "MONITOR RECOVERY -> DO NOT EQUATE WITH PLANTING COUNT",
        ], ["Restoration"]),
        common.panel("Forest-fire answer spine", "answer-spine", [
            "CLASSIFY FIRE + TRACE IGNITION WEATHER FUEL TOPOGRAPHY",
            "PREVENT -> DETECT -> VERIFY -> RESPOND -> RESTORE",
            "ADD COMMUNITY FIRE-LINE ECOLOGY SMOKE AND WUI GOVERNANCE",
            "SEPARATE ALERT CAPACITY CONTAINMENT AND RECOVERY OUTCOMES",
        ], ["Alert-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, its determination and the Sendai Framework elements.",
            "Verified support route, not a forest-fire-specific PYQ; use prevention, detection, community capacity and restoration only as a bounded resilience illustration.",
            [0, 9, 10, 11, 12, 18, 19]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management in India.",
            "Verified adjacent governance route; prevention, danger rating and community partnership illustrate proactivity without claiming the printed question named forest fire.",
            [5, 6, 7, 9, 10, 12, 14, 19]),
        common.make_pyq_solution(facts, "2025", "GS-IV",
            "Examine an administrative case involving deforestation for housing and social-welfare objectives.",
            "Verified cross-paper adjacent card owned by Ethics; this topic contributes only the bounded wildland-interface, fuel and community-governance risk lens.",
            [7, 9, 12, 15, 17, 19]),
    ]
    return common.topic(
        11, "Forest Fire Risk Management",
        "11_Forest-Fire-Risk-Management", facts, traps,
        [
            (10, "Explain the fire triangle and distinguish surface, ground and crown fires.", [0, 2, 3, 4]),
            (10, "Show how weather, fuel and topography interact to shape forest-fire behaviour.", [1, 6, 7, 8]),
            (15, "Evaluate FSI satellite detection and the alert-to-initial-response chain.", [10, 11, 19]),
            (15, "Examine community participation, fire lines and prescribed burning as bounded governance tools.", [9, 12, 13, 14, 15]),
            (20, "Design an integrated forest-fire strategy covering prevention, detection, response, smoke health and restoration.", [0, 1, 5, 6, 7, 8, 9, 10, 11, 16, 18, 19]),
            (20, "Critically analyse ecological, suppression and wildland-urban-interface trade-offs in forest-fire governance.", [7, 12, 13, 14, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "fire triangle", "surface fire", "ground fire", "crown fire",
            "lightning", "weather", "fuel", "topography", "firebreaks",
            "Forest Fire Line", "controlled", "community participation",
            "FAST 3.0", "Large Forest Fire Monitoring", "Burnt Scar Assessment",
        ],
        "No audited GS-III route directly names forest-fire management. The 2024 resilience and 2020 proactive-governance cards are support/adjacent applications; the 2025 Ethics card is cross-paper context only and remains Ethics-owned.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered FSI's monitoring and alert architecture, the forest-fire dashboard, ISRO disaster support, the MoEFCC/FPM PIB route and NDMA. Thin, blocked, missing and transport-failed pages are recorded; no current fire count, affected area, crew strength, response time, containment, casualty, health or restoration outcome was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "FIRE TRIANGLE TYPE IGNITION WEATHER FUEL TOPOGRAPHY AND WUI MAP",
            "SATELLITE ALERT FIRE-LINE PRESCRIBED-BURN AND OUTCOME FIREWALLS",
            "PREVENT DETECT VERIFY RESPOND PROTECT HEALTH AND RESTORE SPINE",
            "CURRENT FSI MOEFCC ISRO NDMA AND CAPACITY EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "START WITH FUEL HEAT OXYGEN AND CLASSIFY SURFACE GROUND OR CROWN",
            "SEPARATE NATURAL DELIBERATE AND ACCIDENTAL IGNITION",
            "TRACE WEATHER FUEL TOPOGRAPHY AND ACCESS INTERACTION",
            "CONNECT FSI DETECTION TO FIELD VERIFICATION COMMAND AND ESCALATION",
            "DESIGN ACCOUNTABLE COMMUNITY PARTICIPATION AND MAINTAINED FIRE LINES",
            "BOUND PRESCRIBED BURNING BY AUTHORISATION ECOLOGY SUPERVISION AND MONITORING",
            "ADD SMOKE HEALTH WUI EVACUATION RESTORATION AND VERIFIED OUTCOMES",
        ],
    )


TOPIC_11 = _build()
