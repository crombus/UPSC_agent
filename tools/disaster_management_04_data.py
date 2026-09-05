"""Authored learner-v2 data for Disaster Management Topic 04."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://sachet.ndma.gov.in/About — attempted 2026-09-04; the official "
        "SACHET page failed at the transport layer. Official search metadata "
        "confirmed CAP-based multi-channel alerting, but no reach, handset or "
        "avoided-loss statistic was imported."
    ),
    (
        "https://wmo.int/all-activities/build-resilience/early-warnings-all "
        "— fetched 2026-09-04; WMO confirms the end-of-2027 aim and four "
        "people-centred end-to-end pillars. The page is not treated as proof "
        "that every country or community is covered."
    ),
    (
        "https://tsunami.incois.gov.in/TEWS/dsssop.jsp — fetched 2026-09-04; "
        "the official ITEWC procedure confirms event-analysis thresholds, "
        "bulletin stages and the use of model and sea-level information. "
        "Technical thresholds are not converted into local evacuation outcomes."
    ),
    (
        "https://cwc.gov.in/flood-forecasting-hydrological-observation — "
        "fetched 2026-09-04; CWC confirms its flood-monitoring, forecasting and "
        "warning role and multi-channel dissemination to authorities. Dynamic "
        "network figures are not used as timeless facts."
    ),
    (
        "https://www.isro.gov.in/DisasterManagementSupport.html — fetched "
        "2026-09-04; the official ISRO page was content-thin. Official search "
        "metadata was used only to confirm disaster-management support through "
        "Earth observation, GIS and decision-support applications."
    ),
    (
        "https://mausam.imd.gov.in/index_en.php — fetched 2026-09-04; the IMD "
        "landing page was content-thin for service architecture. No claim about "
        "nationwide impact-based forecast coverage or warning performance was "
        "made from that page."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("End-to-end MHEWS", "A multi-hazard early warning system is a people-centred chain linking risk knowledge, monitoring and forecasting, authoritative warning, dissemination, preparedness, early action and feedback."),
        ("Risk knowledge", "Risk knowledge combines hazard, exposure, vulnerability, capacity and spatial information so warnings can target people, places and actions."),
        ("Monitoring and forecasting", "Sensors, observations, models and expert analysis detect or forecast hazard conditions; capability and lead time differ sharply by hazard."),
        ("Authoritative warning", "A warning is an authorised, understandable and actionable message, not raw sensor data or an unverified social-media post."),
        ("Dissemination", "Effective dissemination uses redundant channels and geo-targeting while preserving message consistency, accessibility, timing and source authenticity."),
        ("Preparedness and action", "A warning has protective value only when recipients understand it and have routes, transport, shelters, supplies, authority and practice to act."),
        ("Last-mile feedback", "Receipt, comprehension, action and user feedback should return to risk knowledge and warning design; alerts issued are not the same as people protected."),
        ("IMD role", "IMD monitors and forecasts weather hazards and issues official meteorological and cyclone warnings, including impact information where its service supports it."),
        ("CWC role", "CWC monitors river conditions and issues flood forecasts and warnings to administrations, project authorities, States and relevant Central agencies."),
        ("INCOIS role", "INCOIS operates the Indian Tsunami Early Warning Centre, integrating earthquake analysis, pre-run scenarios and sea-level observations for tsunami bulletins."),
        ("ISRO and NRSC role", "ISRO and NRSC provide Earth-observation, remote-sensing, GIS and decision-support products for preparedness, event assessment and recovery planning."),
        ("NDMA and local roles", "NDMA supports national alert integration and guidance, while State and local authorities translate authoritative warnings into evacuation, shelter, route and public-action decisions."),
        ("CAP and SACHET", "Common Alerting Protocol standardises a structured alert for multiple channels; SACHET is NDMA's CAP-based portal, but format interoperability does not settle institutional mandate."),
        ("GIS and remote sensing", "GIS integrates spatial layers for risk mapping, shelter siting, route planning and damage assessment; satellite imagery supplies repeat and synoptic observations."),
        ("Radar sensors and lead time", "Doppler radar, gauges, buoys, seismic networks and other sensors serve different hazards; no single sensor or lead-time claim applies across all hazards."),
        ("Drones and crowdsourcing", "Drones and citizen reports can add local imagery or observations where lawful and safe, but require verification, airspace safety, provenance and bias controls."),
        ("AI and models", "AI and machine learning can assist pattern detection, forecasting and prioritisation, but inherit data gaps and model uncertainty and require expert oversight."),
        ("Interoperability and redundancy", "Resilient warning systems need interoperable data and message formats, backup power, communications, sensors and manual alternatives to avoid single points of failure."),
        ("Privacy and equity", "Geo-targeting, imagery, device and crowdsourced data can create privacy, exclusion and surveillance risks; necessity, minimisation, access control and inclusive channels remain essential."),
        ("Technology-outcome firewall", "A platform, model, alert, drone sortie or dashboard proves a technical or administrative input; timely comprehension, action and avoided loss need separate evidence."),
    ]
    traps = [
        "Do not reduce an early warning system to detection technology.",
        "Do not confuse prediction, forecast, watch, alert and warning.",
        "Do not assign every hazard to IMD.",
        "Do not treat CAP interoperability as a solution to mandate conflicts.",
        "Do not infer last-mile reach from platform availability.",
        "Do not assume one lead time or warning method fits every hazard.",
        "Do not present AI output as certainty.",
        "Do not treat crowdsourced reports as verified official warnings.",
        "Do not omit redundancy, accessibility or privacy.",
        "Do not equate technology deployment with avoided disaster loss.",
    ]
    titles = [
        "People-centred end-to-end warning chain",
        "Risk knowledge and exposure mapping",
        "Monitoring observation and forecasting",
        "Authoritative warning and uncertainty",
        "Dissemination communication and redundancy",
        "Preparedness response and early action",
        "Last-mile feedback and outcome metrics",
        "IMD weather and cyclone role",
        "CWC river-flood role",
        "INCOIS tsunami-warning role",
        "ISRO NRSC GIS and remote sensing",
        "NDMA SACHET and CAP interoperability",
        "Doppler radar sensors satellites and lead time",
        "Drones AI crowdsourcing privacy and limits",
        "Multi-agency synthesis and technology-outcome boundary",
    ]
    routes = [
        "Draw the complete chain before naming technologies.",
        "Map who and what is exposed before selecting a warning channel.",
        "Match observing system and lead time to the hazard.",
        "Name the competent issuer and communicate uncertainty.",
        "Use redundant accessible channels with one consistent message.",
        "Attach every warning to a feasible protective action.",
        "Measure receipt, comprehension and action, not alerts alone.",
        "Attribute meteorological warning functions precisely.",
        "Attribute river forecasting to CWC and local action to authorities.",
        "Separate earthquake detection from tsunami threat assessment.",
        "Connect spatial products to a decision rather than listing platforms.",
        "Explain format interoperability and its mandate limit.",
        "Compare technologies by hazard, resolution and lead time.",
        "Add validation, human oversight, privacy and safety safeguards.",
        "Conclude with people protected, not tools deployed.",
    ]
    panels = [
        common.panel("End-to-end MHEWS rail", "numbered-rail", [
            "1 RISK KNOWLEDGE",
            "2 MONITOR / OBSERVE / FORECAST",
            "3 AUTHORITATIVE WARNING",
            "4 DISSEMINATE -> 5 PREPARE / ACT -> 6 FEEDBACK",
        ], ["End-to-end MHEWS", "Last-mile feedback"]),
        common.panel("Risk-knowledge stack", "layered-map", [
            "HAZARD + EXPOSURE + VULNERABILITY + CAPACITY",
            "SPATIAL LAYERS + HISTORICAL / REAL-TIME DATA",
            "DECISION -> WHO WHERE WHEN WHAT ACTION",
            "UPDATE -> COMMUNITY AND EVENT FEEDBACK",
        ], ["Risk knowledge"]),
        common.panel("Observation-to-warning firewall", "process-flow", [
            "SENSOR / REPORT -> QUALITY CONTROL",
            "MODEL + EXPERT ANALYSIS -> FORECAST / ASSESSMENT",
            "COMPETENT AUTHORITY -> WARNING",
            "PUBLIC ACTION -> NOT RAW DATA",
        ], ["Monitoring and forecasting", "Authoritative warning"]),
        common.panel("Dissemination redundancy", "network-map", [
            "CAP MESSAGE -> SMS / CELL / APP / WEB",
            "CAP MESSAGE -> RADIO / TV / SIREN",
            "LOCAL RELAY -> VOLUNTEER / PUBLIC ADDRESS",
            "BACKUP -> POWER + NETWORK + MANUAL PATH",
        ], ["Dissemination", "Interoperability and redundancy"]),
        common.panel("Warning-to-action test", "decision-tree", [
            "RECEIVED? -> UNDERSTOOD?",
            "TRUSTED? -> ACTION FEASIBLE?",
            "ROUTE / TRANSPORT / SHELTER AVAILABLE?",
            "RESULT -> EARLY ACTION OR LAST-MILE FAILURE",
        ], ["Preparedness and action", "Last-mile feedback"]),
        common.panel("Agency ownership matrix", "matrix", [
            "IMD -> WEATHER / CYCLONE",
            "CWC -> RIVER FLOOD FORECAST",
            "INCOIS -> TSUNAMI",
            "ISRO / NRSC -> EARTH OBSERVATION / GIS",
            "NDMA + STATE / LOCAL -> INTEGRATION AND ACTION",
        ], ["IMD role", "CWC role", "INCOIS role", "ISRO and NRSC role", "NDMA and local roles"]),
        common.panel("CAP and SACHET boundary", "comparison-table", [
            "CAP -> structured message format",
            "SACHET -> national alert portal / dissemination layer",
            "SOLVES -> channel-format interoperability",
            "DOES NOT SOLVE -> hazard ownership or local readiness",
        ], ["CAP and SACHET"]),
        common.panel("Geospatial decision cycle", "process-flow", [
            "SATELLITE / AERIAL / FIELD DATA",
            "GIS LAYERS -> RISK MAP / ROUTE / SHELTER",
            "EVENT IMAGE -> DAMAGE / ACCESS ASSESSMENT",
            "RECOVERY MAP -> SAFER SITING",
        ], ["GIS and remote sensing", "ISRO and NRSC role"]),
        common.panel("Sensor-hazard matching", "comparison-table", [
            "DOPPLER RADAR -> WEATHER STRUCTURE",
            "GAUGE -> RAIN / RIVER / SEA LEVEL",
            "BUOY / BPR -> OCEAN RESPONSE",
            "SEISMIC NETWORK -> EARTHQUAKE PARAMETERS",
        ], ["Radar sensors and lead time"]),
        common.panel("Emerging-technology safeguards", "matrix", [
            "DRONE -> local imagery | airspace + safety",
            "AI -> pattern / prioritisation | uncertainty + oversight",
            "CROWD REPORT -> local signal | verification + provenance",
            "DATA -> utility | privacy + minimisation",
        ], ["Drones and crowdsourcing", "AI and models", "Privacy and equity"]),
        common.panel("Failure and redundancy map", "failure-tree", [
            "SENSOR FAIL | POWER FAIL | NETWORK FAIL",
            "AUTHORITY DELAY | FORMAT MISMATCH",
            "LANGUAGE / ACCESS BARRIER | NO TRANSPORT",
            "CONTROL -> REDUNDANT TECHNICAL AND HUMAN PATHS",
        ], ["Interoperability and redundancy", "Privacy and equity"]),
        common.panel("Technology answer spine", "answer-spine", [
            "MAP HAZARD + LEAD TIME -> NAME COMPETENT AGENCY",
            "TRACE DATA -> FORECAST -> WARNING -> DISSEMINATION",
            "ADD ACCESSIBLE ACTION + FEEDBACK",
            "QUALIFY UNCERTAINTY PRIVACY AND OUTCOME EVIDENCE",
        ], ["Technology-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss policies and frameworks for tackling urban flooding.",
            "Verified direct ownership remains Topic 08; this conservative card supplies CWC, IMD, GIS, forecasting, dissemination and local-action architecture.",
            [0, 1, 2, 4, 5, 7, 8, 11, 13, 14]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe the elements that determine disaster resilience.",
            "Verified direct ownership remains Topic 01; this card routes risk knowledge, redundancy, warning, preparedness and feedback as resilience elements.",
            [0, 1, 5, 6, 17, 19]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Give an account of technology used in managing the COVID-19 pandemic.",
            "Verified direct ownership remains Topic 13; this card is limited to transferable technology-governance tests and does not force-fit pandemic-specific facts.",
            [3, 4, 5, 16, 17, 18, 19]),
    ]
    return common.topic(
        4, "Multi-Hazard Early Warning and Disaster Technology",
        "04_Multi-Hazard-Early-Warning-and-Disaster-Technology", facts, traps,
        [
            (10, "Explain why an early warning system is an end-to-end action chain rather than a sensor.", [0, 1, 2, 3, 4, 5, 6]),
            (10, "Distinguish the disaster-warning roles of IMD, CWC, INCOIS, ISRO and NDMA.", [7, 8, 9, 10, 11]),
            (15, "Assess CAP and SACHET as tools for interoperable warning dissemination.", [3, 4, 11, 12, 17, 19]),
            (15, "Examine GIS, remote sensing, radar, sensors and satellites across the disaster-management cycle.", [1, 2, 10, 13, 14, 17]),
            (20, "Evaluate the opportunities and limits of drones, AI and crowdsourcing in disaster management.", [15, 16, 17, 18, 19]),
            (20, "Design a people-centred multi-hazard early warning system with uncertainty, redundancy, accessibility, privacy and feedback safeguards.", [0, 1, 2, 3, 4, 5, 6, 12, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "risk knowledge", "monitoring", "forecasting", "warning",
            "dissemination", "response capability", "GIS", "satellite",
            "Doppler", "Common Alerting Protocol", "SACHET", "IMD",
            "CWC", "INCOIS", "ISRO", "interoperability", "redundancy",
            "impact-based forecasting",
        ],
        "No audited 2024-2025 question directly owns the whole MHEWS architecture. The two 2024 cards and the 2020 technology card are explicitly limited cross-topic routes with verified year, paper, directive and marks retained in their primary owners.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered WMO's end-to-end benchmark, NDMA SACHET, INCOIS tsunami procedures, CWC flood forecasting, ISRO support and IMD services. Thin or blocked pages are logged, and no platform is treated as proof of last-mile action or avoided loss.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "END-TO-END WARNING CHAIN AND AGENCY-OWNERSHIP MAP",
            "FORECAST WARNING CAP SACHET AND LEAD-TIME FIREWALLS",
            "GEOSPATIAL EMERGING-TECHNOLOGY AND LAST-MILE ANSWER SPINE",
            "CURRENT PLATFORM UNCERTAINTY PRIVACY AND OUTCOME BOUNDARY",
        ),
        register_answer_spine=[
            "START WITH RISK KNOWLEDGE AND HAZARD-SPECIFIC LEAD TIME",
            "NAME IMD CWC INCOIS ISRO NDMA STATE AND LOCAL ROLES",
            "TRACE MONITORING FORECAST AUTHORITATIVE WARNING AND DISSEMINATION",
            "ADD CAP SACHET REDUNDANT ACCESSIBLE CHANNELS",
            "CONNECT MESSAGE TO PREPAREDNESS EARLY ACTION AND FEEDBACK",
            "QUALIFY DRONES AI CROWDSOURCING UNCERTAINTY AND PRIVACY",
            "MEASURE PEOPLE PROTECTED NOT TECHNOLOGY DEPLOYED",
        ],
    )


TOPIC_04 = _build()
