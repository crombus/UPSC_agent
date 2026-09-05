"""Authored learner-v2 data for Disaster Management Topic 08."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://cwc.gov.in/flood-forecasting-hydrological-observation — "
        "fetched 2026-09-04; the official CWC page confirmed river monitoring, "
        "forecast dissemination, reservoir-inflow use and site-level flood "
        "categories. Dynamic network, accuracy and annual-output figures were "
        "not imported as timeless facts."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2226438&reg=3&lang=1 "
        "— attempted 2026-09-04; the official PIB page returned HTTP 403. "
        "Official search metadata was used only to cross-check UFRMP Phase-2 "
        "approval status; approval was not converted into completed works."
    ),
    (
        "https://www.indiacode.nic.in/handle/123456789/17002"
        "?sam_handle=123456789/1362 — attempted 2026-09-04; India Code "
        "returned HTTP 403. The Dam Safety Act, 2021 is therefore used only at "
        "the high-level surveillance, inspection and emergency-planning rung "
        "already audited in the owner."
    ),
    (
        "https://ndma.gov.in/Natural-Hazards/Floods — attempted 2026-09-04; "
        "the official NDMA page failed at the transport layer. The 2010 urban-"
        "flood guideline content remains bounded to the canonical owner, and "
        "the recommended Urban Flooding Cell is not asserted as operational."
    ),
    (
        "https://www.isro.gov.in/DisasterManagementSupport.html — fetched "
        "2026-09-04; the official ISRO page was content-thin. It supports only "
        "the general Earth-observation and decision-support role already "
        "audited in Topic 04, not a flood-outcome claim."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Flood taxonomy", "Flood risk should distinguish riverine, pluvial, flash, urban and coastal flooding because their source, onset, spatial scale, warning and management responsibilities differ."),
        ("Riverine flooding", "Riverine flooding occurs when channel flow exceeds capacity or inundates floodplains through catchment rainfall, upstream contributions, sediment, obstruction, embankment interaction or regulated releases."),
        ("Pluvial flooding", "Pluvial flooding results when rainfall runoff exceeds local infiltration, storage or drainage capacity even without a river overtopping its banks."),
        ("Flash flooding", "Flash floods develop rapidly after intense local rainfall, cloudburst, sudden obstruction failure or steep-catchment runoff, leaving limited time for warning and evacuation."),
        ("Urban flooding", "Urban flooding is excessive runoff and waterlogging shaped by sealed surfaces, overburdened or blocked drainage, altered waterways, low-lying development and dense exposure; it is not merely river flooding inside a city."),
        ("Coastal flooding", "Coastal flooding can arise from storm surge, waves, high tide interaction, tsunami or drainage backflow and may combine with river and pluvial flooding in estuaries and coastal cities."),
        ("Basin-catchment process", "Flood risk is produced across the basin and catchment through rainfall, antecedent moisture, slope, land cover, tributary timing, sediment, channel condition and downstream constraints."),
        ("Floodplain encroachment", "Occupation or constriction of floodplains, wetlands, lakes, channels and natural drains increases exposure and removes space for water, making land-use enforcement central to prevention."),
        ("Imperviousness and drainage", "Impervious cover accelerates and synchronises runoff, while undersized, disconnected, encroached or waste-blocked drains delay removal and shift water into homes, roads and critical services."),
        ("Reservoir-operation boundary", "Reservoirs can moderate or redistribute flood flows, but storage, inflow forecasting, gate operation, dam safety and downstream warning involve trade-offs; a dam neither guarantees flood control nor alone explains every downstream flood."),
        ("CWC forecasting", "The Central Water Commission observes river levels and discharges, issues flood forecasts and warnings, and provides inflow forecasts used by administrations and reservoir authorities for mitigation decisions."),
        ("Site-specific thresholds", "CWC's Warning Level, Danger Level and Highest Flood Level are site-specific gauge references used for operational categories; they are not one national elevation or discharge standard."),
        ("Urban planning", "Risk-sensitive master plans, development control, floodplain zoning, drainage inventories, catchment-based design, contour information and protected overland flow paths connect flood risk to ordinary urban governance."),
        ("Wetlands and sponge-city concepts", "Wetlands, lakes, parks, permeable surfaces, detention, retention and distributed blue-green infrastructure can store, slow and infiltrate runoff; sponge-city concepts supplement rather than replace major drainage and basin measures."),
        ("Structural-measure limits", "Dams, embankments, channels, diversion and drainage works may reduce selected risks but can fail, transfer risk or induce unsafe development if design assumptions, maintenance, operation and residual risk are ignored."),
        ("Urban Flood Risk Management Programme", "UFRMP is a National Disaster Mitigation Fund-supported urban-flood mitigation programme; sanction or financial approval establishes an input, not city-wide completion, maintenance or reduced loss."),
        ("Resilient infrastructure", "Roads, metro systems, hospitals, power, water, sewerage, telecom and emergency facilities need flood-safe siting, protected equipment, redundancy, access and rapid service-restoration plans."),
        ("Inclusive evacuation and relief", "Warnings, transport, shelters, relief registration, health protection and grievance mechanisms must account for informal settlements, renters, migrants, children, older persons, persons with disabilities and livelihood assets."),
        ("Recovery and coordination", "Recovery should restore housing, drainage, wetlands, services and livelihoods while reducing future exposure, and requires basin, State, district, ULB, utility and neighbouring-jurisdiction coordination."),
        ("Forecast-outcome firewall", "A forecast, map, drain, embankment, reservoir rule, programme approval or dashboard proves an input; receipt, safe evacuation, maintained capacity, service continuity and reduced loss require separate evidence."),
    ]
    traps = [
        "Do not treat riverine, pluvial, flash, urban and coastal floods as synonyms.",
        "Do not describe urban flooding as rainfall alone or river flooding in a city.",
        "Do not invent a universal rainfall, discharge, return-period or warning threshold.",
        "Do not present floodplain zoning as costless when housing and land pressures are ignored.",
        "Do not treat drains independently of the catchment, waterways, solid waste and downstream outlet.",
        "Do not assume reservoirs or embankments eliminate flood risk.",
        "Do not attribute every downstream flood to a dam release without case-specific evidence.",
        "Do not convert UFRMP approval or a guideline recommendation into implementation.",
        "Do not use sponge-city language as a substitute for basin and drainage governance.",
        "Do not infer protection or reduced loss from forecasts, assets or sanctioned finance.",
    ]
    titles = [
        "Riverine pluvial flash urban and coastal flood taxonomy",
        "Basin catchment channel and floodplain processes",
        "Cloudburst flash-flood and short-lead-time boundary",
        "Urban imperviousness drainage and runoff synchronisation",
        "Floodplain wetlands lakes and natural-drain encroachment",
        "Coastal river tide and drainage interaction",
        "CWC monitoring forecasting and site thresholds",
        "Reservoir operation downstream warning and governance boundary",
        "Dams embankments channels and structural limits",
        "Urban planning floodplain zoning and drainage design",
        "Wetlands blue-green infrastructure and sponge-city concepts",
        "UFRMP NDMF status and implementation firewall",
        "Critical infrastructure and interdependent service resilience",
        "Inclusive evacuation relief health and recovery",
        "Inter-jurisdiction coordination PYQs and outcome boundary",
    ]
    routes = [
        "Classify the flood before selecting causes and measures.",
        "Trace water from catchment to channel floodplain and settlement.",
        "Explain rapid onset and preserve forecasting uncertainty.",
        "Connect sealed surfaces to peak timing drainage and exposure.",
        "Treat natural storage and flow paths as urban infrastructure.",
        "Map compound coastal river and pluvial interactions.",
        "Name CWC data forecasts categories and local-action dependency.",
        "Separate inflow information operating decisions dam safety and public warning.",
        "Evaluate structural protection residual risk maintenance and failure.",
        "Integrate master planning zoning drainage waste and enforcement.",
        "Use distributed storage and infiltration as a portfolio component.",
        "State sanction status without claiming completed mitigation.",
        "Test access redundancy protected equipment and restoration.",
        "Map warning-to-shelter-to-relief for differentiated needs.",
        "End with basin-city coordination and verified service outcomes.",
    ]
    panels = [
        common.panel("Flood-family matrix", "matrix", [
            "RIVERINE -> channel / floodplain overflow",
            "PLUVIAL -> rainfall exceeds local storage / drainage",
            "FLASH -> rapid concentrated runoff or sudden release",
            "URBAN / COASTAL -> built catchment or sea interaction",
        ], ["Flood taxonomy", "Riverine flooding", "Pluvial flooding", "Flash flooding"]),
        common.panel("Catchment-to-city chain", "causal-chain", [
            "RAINFALL + ANTECEDENT MOISTURE + SLOPE / LAND COVER",
            "TRIBUTARY TIMING + CHANNEL / SEDIMENT CONDITION",
            "FLOODPLAIN / CITY EXPOSURE",
            "OUTCOME -> drainage land use warning and capacity",
        ], ["Basin-catchment process", "Urban flooding"]),
        common.panel("Urban runoff mechanism", "process-flow", [
            "IMPERVIOUS SURFACE -> FASTER RUNOFF",
            "SYNCHRONISED PEAK -> OVERBURDENED DRAIN",
            "BLOCKAGE / ENCROACHMENT -> BACKFLOW / WATERLOGGING",
            "DENSE EXPOSURE -> SERVICE AND LIVELIHOOD LOSS",
        ], ["Imperviousness and drainage"]),
        common.panel("Water-space firewall", "comparison-table", [
            "FLOODPLAIN -> room for river expansion",
            "WETLAND / LAKE -> storage and attenuation",
            "NATURAL DRAIN -> conveyance path",
            "ENCROACHMENT -> exposure + lost hydraulic function",
        ], ["Floodplain encroachment", "Wetlands and sponge-city concepts"]),
        common.panel("Compound coastal flood map", "systems-map", [
            "RIVER FLOW -> ESTUARY",
            "PLUVIAL RUNOFF -> URBAN DRAIN",
            "SURGE / TIDE / WAVE -> DOWNSTREAM IMPEDANCE",
            "COMBINATION -> COMPOUND INUNDATION",
        ], ["Coastal flooding"]),
        common.panel("CWC forecast rail", "numbered-rail", [
            "1 OBSERVE LEVEL / DISCHARGE / INFLOW",
            "2 ANALYSE AND FORECAST",
            "3 ISSUE SITE-SPECIFIC CATEGORY / MESSAGE",
            "4 ADMINISTRATION / PROJECT AUTHORITY ACTS",
        ], ["CWC forecasting", "Site-specific thresholds"]),
        common.panel("Reservoir governance boundary", "decision-tree", [
            "INFLOW FORECAST + CURRENT STORAGE",
            "OPERATING RULE / DAM CONDITION / DOWNSTREAM CAPACITY",
            "GATE DECISION -> TIMELY DOWNSTREAM WARNING",
            "TRAP -> DAM IS NEITHER GUARANTEE NOR SINGLE CAUSE",
        ], ["Reservoir-operation boundary"]),
        common.panel("Structural measure test", "comparison-table", [
            "DAM / RESERVOIR -> storage and operation limits",
            "EMBANKMENT -> local protection and breach / transfer risk",
            "CHANNEL / DIVERSION -> conveyance and downstream effects",
            "DRAINAGE -> capacity depends on outlet and maintenance",
        ], ["Structural-measure limits"]),
        common.panel("Urban planning portfolio", "network-map", [
            "MASTER PLAN + FLOODPLAIN ZONING",
            "DRAIN INVENTORY + CATCHMENT / CONTOUR DESIGN",
            "SOLID WASTE + WATERWAY / WETLAND PROTECTION",
            "BUILDING / ROAD / UTILITY DEVELOPMENT CONTROL",
        ], ["Urban planning"]),
        common.panel("Sponge-city portfolio", "layered-map", [
            "ROOF / PLOT -> capture infiltrate delay",
            "STREET / PARK -> permeable and detention space",
            "LAKE / WETLAND -> distributed storage",
            "MAJOR DRAIN / BASIN -> convey residual flows",
        ], ["Wetlands and sponge-city concepts"]),
        common.panel("Inclusive service recovery loop", "feedback-loop", [
            "ACCESSIBLE WARNING -> TRANSPORT -> SHELTER",
            "RELIEF + HEALTH + GRIEVANCE -> SERVICE RESTORATION",
            "HOUSING LIVELIHOOD WETLAND AND DRAIN REPAIR",
            "FEEDBACK -> SAFER PLAN AND INTER-JURISDICTION ACTION",
        ], ["Resilient infrastructure", "Inclusive evacuation and relief", "Recovery and coordination"]),
        common.panel("Flood answer spine", "answer-spine", [
            "CLASSIFY FLOOD -> TRACE CATCHMENT CITY COAST MECHANISM",
            "MAP CWC FORECAST RESERVOIR DECISION AND LOCAL ACTION",
            "COMBINE ZONING DRAINAGE WETLANDS STRUCTURES AND UFRMP",
            "ADD INCLUSION COORDINATION RECOVERY AND OUTCOME QUALIFICATION",
        ], ["Urban Flood Risk Management Programme", "Forecast-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss urban-flood causes, features of two major Indian floods, and policies and frameworks for tackling such floods.",
            "Verified direct routing: Discuss · 15 marks · 250 words; cases must use source-bounded features and avoid unsupported casualty, rainfall, loss or attribution figures.",
            [4, 6, 7, 8, 10, 12, 13, 15, 18, 19]),
        common.make_pyq_solution(facts, "2020", "GS-I",
            "Account for flooding in million-plus cities and suggest lasting remedial measures.",
            "Verified direct routing: Account for and suggest · 15 marks · 250 words.",
            [2, 4, 7, 8, 12, 13, 14, 16, 17, 18]),
        common.make_pyq_solution(facts, "2023", "GS-III",
            "Analyse why dam failures cause catastrophic downstream effects and use case examples.",
            "Verified direct routing: Analyze · 10 marks · 150 words; this conservative card keeps engineering and causation bounded to surveillance, operation, warning and emergency planning.",
            [1, 6, 9, 10, 14, 17, 19]),
    ]
    return common.topic(
        8, "Riverine Floods and Urban Flood Resilience",
        "08_Riverine-Floods-and-Urban-Flood-Resilience", facts, traps,
        [
            (10, "Distinguish riverine, pluvial, flash, urban and coastal flooding.", [0, 1, 2, 3, 4, 5]),
            (10, "Explain CWC flood forecasting and the site-specific threshold framework.", [10, 11, 19]),
            (15, "Analyse urban flooding through catchment change, imperviousness, drainage and floodplain encroachment.", [4, 6, 7, 8, 12]),
            (15, "Examine reservoir operation, dam safety, downstream warning and the limits of structural flood control.", [9, 10, 11, 14, 19]),
            (20, "Evaluate an integrated urban-flood-resilience portfolio of planning, wetlands, sponge-city measures, infrastructure and mitigation finance.", [7, 8, 12, 13, 14, 15, 16, 19]),
            (20, "Design an inclusive basin-to-city flood-management framework covering warning, evacuation, relief, recovery and inter-jurisdiction coordination.", [0, 6, 10, 12, 13, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Urban flood", "Flood-plain zoning", "Flood proofing",
            "Urban Flooding Cell", "CWC", "IMD", "Warning Level",
            "Danger Level", "Highest Flood Level", "Aapda Mitra",
            "Decision Support System", "nowcasting", "Doppler radar",
            "Urban Flood Risk Management Programme",
            "National Disaster Mitigation Fund",
        ],
        "The 2024 GS-III urban-flood and 2020 GS-I million-plus-city cards are direct routes. The 2023 dam-failure card is direct but deliberately bounded to governance, surveillance, operation, warning and emergency planning rather than engineering reconstruction.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered CWC flood forecasting, PIB UFRMP status, India Code's Dam Safety Act route, NDMA flood guidance and ISRO disaster support. Thin, blocked and transport-failed pages are logged; no rainfall, discharge, return-period, dam-operation, casualty, damage, completion or avoided-loss figure was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "FLOOD TAXONOMY BASIN CATCHMENT CITY COAST AND RUNOFF MAP",
            "CWC THRESHOLD RESERVOIR DAM STRUCTURE AND PROGRAMME FIREWALLS",
            "ZONING DRAINAGE WETLAND INFRASTRUCTURE INCLUSION AND RECOVERY SPINE",
            "CURRENT CWC NDMA INDIA-CODE UFRMP AND OUTCOME EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "CLASSIFY RIVERINE PLUVIAL FLASH URBAN AND COASTAL FLOODING",
            "TRACE RAINFALL CATCHMENT CHANNEL FLOODPLAIN DRAIN AND COAST",
            "NAME CWC OBSERVATION FORECAST SITE THRESHOLD AND LOCAL ACTION",
            "BOUND RESERVOIR OPERATION DAM SAFETY AND STRUCTURAL-MEASURE CLAIMS",
            "COMBINE FLOODPLAIN ZONING DRAINAGE WETLANDS AND SPONGE-CITY STORAGE",
            "PROTECT CRITICAL SERVICES AND DESIGN INCLUSIVE EVACUATION RELIEF",
            "COORDINATE BASIN CITY JURISDICTIONS AND VERIFY RECOVERY OUTCOMES",
        ],
    )


TOPIC_08 = _build()
