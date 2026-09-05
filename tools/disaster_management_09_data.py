"""Authored learner-v2 data for Disaster Management Topic 09."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://agriwelfare.gov.in/Documents/Updated%20Drought%20Manual_0.pdf "
        "— fetched 2026-09-04; the official Department of Agriculture PDF was "
        "reachable only as raw PDF content. It confirms the owner route to the "
        "updated drought manual, but no unparsed threshold was imported. "
        "https://ndma.gov.in/Natural-Hazards/Drought — searched 2026-09-04; "
        "the NDMA route supplied no retrievable text."
    ),
    (
        "https://mausam.imd.gov.in/responsive/heatwave_guidance.php — "
        "attempted 2026-09-04; the official IMD page returned HTTP 500. "
        "Heat-wave criteria therefore remain bounded to the audited owner, "
        "with no current event, forecast or temperature claim added."
    ),
    (
        "https://cgwb.gov.in/ — fetched 2026-09-04; the official CGWB landing "
        "page confirmed its groundwater exploration, assessment, conservation, "
        "augmentation, pollution-protection and policy-monitoring remit. "
        "https://cwc.gov.in/ — fetched 2026-09-04; CWC described its water-"
        "resources control, conservation and utilisation responsibilities. "
        "Neither page was used to infer current drought severity."
    ),
    (
        "https://icar-crida.res.in/ — fetched 2026-09-04; the official ICAR-"
        "CRIDA page returned thin publication-list content. "
        "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=1982978 — "
        "attempted 2026-09-04; PIB returned HTTP 403. No crop contingency, "
        "Heat Action Plan coverage or implementation figure was inferred."
    ),
    (
        "https://nidm.gov.in/pdf/trgReports/2026/March/"
        "Trg_25-27March2026ms.pdf — searched 2026-09-04; the official NIDM "
        "result identified a dated drought-management training route. It was "
        "not used to create new declaration thresholds or performance claims."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Aridity versus drought", "Aridity is a long-term climatic condition of low moisture availability, whereas drought is a temporary or episodic deficit relative to the expected local water regime."),
        ("Meteorological drought", "Meteorological drought concerns prolonged inadequate or poorly distributed precipitation relative to the relevant climatology; it is a hazard indicator, not a complete account of impacts."),
        ("Agricultural drought", "Agricultural drought arises when soil moisture and crop-water availability become inadequate for crops, so rainfall information must be read with sowing, vegetation and soil-moisture evidence."),
        ("Hydrological drought", "Hydrological drought concerns below-normal availability in rivers, reservoirs, lakes or aquifers and may lag behind the rainfall deficit that initiated it."),
        ("Socio-economic drought", "Socio-economic drought occurs when water shortage disrupts the supply of goods, services, livelihoods or essential uses; it expresses the interaction of physical scarcity with demand and unequal access."),
        ("Ecological drought", "Ecological drought describes water shortage severe enough to impair ecosystem productivity or function; it must not be silently substituted for socio-economic drought."),
        ("Slow-onset cascade", "Drought can unfold from rainfall deficit through soil-moisture stress, storage decline, ecosystem damage, livelihood loss and health effects over different time scales, so one indicator cannot represent every stage."),
        ("Multi-indicator declaration", "India's Manual for Drought Management uses rainfall, vegetative indices, crop-sowing progression, soil moisture and hydrological indices in a graded assessment rather than one universal crop-loss percentage."),
        ("Heat-wave hazard", "A heat wave is a meteorological hazard identified through IMD's station and departure or actual-temperature criteria; it is not synonymous with every hot day or every episode of heat illness."),
        ("Heat stress", "Heat stress is the physiological burden produced by temperature, humidity, radiation, wind, exertion, clothing, health and access to rest, water or cooling; exposure and vulnerability therefore mediate the hazard."),
        ("Wet-bulb boundary", "Wet-bulb temperature combines heat and humidity by representing evaporative-cooling potential; it is not an IMD heat-wave declaration threshold, and dangerous stress can occur below a theoretical upper-limit benchmark."),
        ("Exposure inequality", "Outdoor and informal workers, older persons, children, people with illness, poorly housed households and those lacking dependable water or cooling may face different risk under the same forecast temperature."),
        ("Heat Action Plan", "A Heat Action Plan links seasonal preparedness, warnings, health-system readiness, public communication, water and cooling access, work or school timing and longer-term urban measures through locally assigned responsibilities."),
        ("Water-risk portfolio", "Drought management requires demand management, drinking-water security, groundwater and surface-water monitoring, watershed or recharge measures, storage governance and protection against shifting scarcity to weaker users."),
        ("Agriculture and livelihoods", "Crop choice, contingency planning, soil-moisture conservation, livestock support, insurance or social protection and alternative livelihoods address agricultural and socioeconomic drought without treating relief as adaptation."),
        ("Urban heat measures", "Cool roofs, shade, ventilation, trees and water bodies can reduce selected exposures, but benefits depend on design, maintenance, local climate and access; a cooling intervention can transfer costs or water demand."),
        ("Labour and health measures", "Risk-sensitive work-rest scheduling, drinking water, shaded rest, worker communication, clinical readiness and surveillance are distinct from the meteorological forecast and require responsible employers and public agencies."),
        ("Compound risk", "Drought, water scarcity, heat, wildfire risk, crop stress, power demand and public-health pressure can interact, while humid heat or hot nights may intensify harm without changing the formal hazard label."),
        ("Early action and maladaptation", "Forecast-triggered early action should precede severe impacts, but water-intensive cooling, indiscriminate groundwater extraction or unequal greening can increase future vulnerability and become maladaptation."),
        ("Monitoring-to-outcome firewall", "A drought declaration, forecast, Heat Action Plan, dashboard, water scheme or contingency plan proves a classification or input; timely reach, equitable access, livelihood continuity and reduced illness require separate evidence."),
    ]
    traps = [
        "Do not use aridity and drought as synonyms.",
        "Do not reduce drought to rainfall deficiency or omit socioeconomic impacts.",
        "Do not replace a multi-indicator drought assessment with a guessed crop-loss cut-off.",
        "Do not treat a heat-wave bulletin as proof of heat stress, exposure or illness.",
        "Do not substitute wet-bulb temperature for IMD heat-wave declaration criteria.",
        "Do not present Heat Action Plan adoption as enforceable worker protection or measured mortality reduction.",
        "Do not treat emergency water supply as a substitute for groundwater, cropping and demand governance.",
        "Do not recommend cooling measures without testing water, energy, access and maintenance burdens.",
        "Do not attribute a named event or outcome to climate change without source-specific evidence.",
        "Do not infer preparedness or reduced loss from a plan, forecast, scheme or declaration.",
    ]
    titles = [
        "Aridity drought and slow-onset risk grammar",
        "Meteorological agricultural hydrological socioeconomic and ecological drought",
        "Drought cascade lags and multi-indicator monitoring",
        "Drought declaration and evidence discipline",
        "Heat-wave hazard criteria and forecast boundary",
        "Heat stress wet-bulb exposure and vulnerability",
        "Compound drought heat water agriculture and health risk",
        "Heat Action Plan governance chain",
        "Water security groundwater and demand portfolio",
        "Agriculture livestock livelihoods and social protection",
        "Urban heat built form cooling and access",
        "Outdoor labour schools and health-system readiness",
        "Anticipatory action triggers and financing logic",
        "Maladaptation distribution and residual risk",
        "PYQ synthesis monitoring and outcome firewall",
    ]
    routes = [
        "Open by distinguishing a climatic baseline from an episodic deficit.",
        "Name the drought type before choosing an indicator or measure.",
        "Trace time lags from rainfall to soil storage livelihood and health.",
        "State the Manual's indicator families without inventing cut-offs.",
        "Separate meteorological classification from public-health consequence.",
        "Explain evaporative cooling and differentiated exposure without using a false universal threshold.",
        "Map interactions while avoiding unsupported event attribution.",
        "Assign forecast health labour water communication and urban responsibilities.",
        "Balance supply augmentation demand management monitoring and equity.",
        "Join contingency agriculture with livelihood continuity and social protection.",
        "Evaluate cooling, shade, ventilation, trees and water through access and maintenance.",
        "Translate a warning into work-rest, water, outreach and clinical action.",
        "Use forecast information before impact and retain uncertainty.",
        "Test every measure for transferred water energy land and inequality burdens.",
        "Conclude with observed reach and outcomes rather than plan existence.",
    ]
    panels = [
        common.panel("Drought identity firewall", "comparison-table", [
            "ARIDITY -> persistent climatic moisture condition",
            "DROUGHT -> temporary deficit relative to local expectation",
            "SCARCITY -> supply-demand-access condition",
            "DISASTER -> serious disruption beyond coping capacity",
        ], ["Aridity versus drought", "Socio-economic drought"]),
        common.panel("Drought-family matrix", "matrix", [
            "METEOROLOGICAL -> precipitation",
            "AGRICULTURAL -> soil moisture / crop water",
            "HYDROLOGICAL -> rivers reservoirs lakes aquifers",
            "SOCIOECONOMIC / ECOLOGICAL -> services-livelihoods / ecosystems",
        ], ["Meteorological drought", "Agricultural drought", "Hydrological drought", "Socio-economic drought", "Ecological drought"]),
        common.panel("Slow-onset cascade", "causal-chain", [
            "RAINFALL DEFICIT -> SOIL-MOISTURE STRESS",
            "-> STORAGE / GROUNDWATER DECLINE",
            "-> CROP ECOSYSTEM LIVELIHOOD AND HEALTH EFFECTS",
            "LAGS DIFFER -> MONITOR EACH STAGE",
        ], ["Slow-onset cascade"]),
        common.panel("Declaration dashboard", "layered-map", [
            "RAINFALL + VEGETATIVE INDICES",
            "CROP-SOWING PROGRESSION + SOIL MOISTURE",
            "HYDROLOGICAL INDICES",
            "GRADE STATUS -> DO NOT INVENT ONE CUT-OFF",
        ], ["Multi-indicator declaration"]),
        common.panel("Heat hazard-to-harm chain", "systems-map", [
            "IMD HAZARD CLASSIFICATION",
            "+ HUMIDITY / RADIATION / WIND / HOT NIGHT",
            "+ WORK / HEALTH / HOUSING / WATER / COOLING",
            "= HEAT STRESS AND UNEQUAL HARM",
        ], ["Heat-wave hazard", "Heat stress", "Exposure inequality"]),
        common.panel("Wet-bulb firewall", "comparison-table", [
            "DRY-BULB -> ambient air temperature",
            "WET-BULB -> evaporative-cooling potential",
            "IMD HEAT WAVE -> operational meteorological criteria",
            "TRAP -> NONE IS A UNIVERSAL PERSON-SAFE THRESHOLD",
        ], ["Wet-bulb boundary", "Heat-wave hazard"]),
        common.panel("Heat Action Plan rail", "numbered-rail", [
            "1 SEASONAL RISK AND RESPONSIBILITY MAP",
            "2 FORECAST / WARNING AND PUBLIC MESSAGE",
            "3 WATER COOLING WORK SCHOOL AND HEALTH ACTION",
            "4 REVIEW REACH EQUITY AND OUTCOMES",
        ], ["Heat Action Plan", "Monitoring-to-outcome firewall"]),
        common.panel("Water-agriculture portfolio", "network-map", [
            "DRINKING WATER + DEMAND MANAGEMENT",
            "GROUND / SURFACE WATER MONITORING",
            "WATERSHED RECHARGE STORAGE GOVERNANCE",
            "CROP LIVESTOCK LIVELIHOOD CONTINGENCY",
        ], ["Water-risk portfolio", "Agriculture and livelihoods"]),
        common.panel("Urban-labour-health matrix", "matrix", [
            "BUILT FORM -> cool roof shade ventilation trees",
            "LABOUR -> timing rest water communication",
            "HEALTH -> surveillance triage referral continuity",
            "ACCESS -> poor housing informal work vulnerable groups",
        ], ["Urban heat measures", "Labour and health measures", "Exposure inequality"]),
        common.panel("Compound-risk web", "feedback-loop", [
            "DROUGHT -> WATER / CROP / POWER PRESSURE",
            "HEAT -> HEALTH / LABOUR / COOLING DEMAND",
            "DRY FUEL -> FIRE RISK",
            "FEEDBACK -> DEEPER LIVELIHOOD AND SERVICE STRESS",
        ], ["Compound risk"]),
        common.panel("Early action or maladaptation", "decision-tree", [
            "FORECAST + VULNERABILITY SIGNAL?",
            "YES -> EARLY WATER HEALTH LABOUR LIVELIHOOD ACTION",
            "TEST -> ENERGY WATER LAND ACCESS MAINTENANCE",
            "FAIL TEST -> MALADAPTATION / TRANSFERRED RISK",
        ], ["Early action and maladaptation"]),
        common.panel("Slow-onset answer spine", "answer-spine", [
            "DISTINGUISH ARIDITY SCARCITY AND DROUGHT TYPES",
            "TRACE LAGS + MONITOR MULTIPLE INDICATORS",
            "SEPARATE HEAT HAZARD FROM STRESS AND EXPOSURE",
            "DESIGN EARLY ACTION + TEST EQUITY MALADAPTATION OUTCOME",
        ], ["Monitoring-to-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2025", "Prelims GS-I",
            "Assess the implications of wet-bulb temperature crossing the stated benchmark.",
            "Verified direct objective route; the official Set-A key exists locally, but this card records no answer option and preserves the wet-bulb-versus-IMD-threshold distinction.",
            [8, 9, 10, 11]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, its determination and the Sendai Framework elements.",
            "Verified support route, not a drought-specific PYQ; use slow-onset monitoring, early action and outcome evidence only as a bounded illustration.",
            [6, 12, 17, 18, 19]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management in India.",
            "Verified adjacent governance route; drought and heat supply an anticipatory-action example, not a claim that the printed question named either hazard.",
            [6, 7, 12, 18, 19]),
    ]
    return common.topic(
        9, "Drought, Heat Waves and Slow-Onset Risk",
        "09_Drought-Heat-Waves-and-Slow-Onset-Risk", facts, traps,
        [
            (10, "Distinguish aridity, water scarcity and the principal drought types.", [0, 1, 2, 3, 4, 5]),
            (10, "Explain why heat-wave hazard and heat stress are not interchangeable.", [8, 9, 10, 11]),
            (15, "Analyse drought as a slow-onset cascade requiring multi-indicator monitoring and early action.", [1, 2, 3, 4, 6, 7, 18]),
            (15, "Examine a Heat Action Plan through forecast, health, labour, water and urban-governance responsibilities.", [8, 9, 11, 12, 15, 16, 19]),
            (20, "Design an integrated drought-risk strategy for water, agriculture, livelihoods, health and social protection.", [0, 1, 2, 3, 4, 6, 7, 13, 14, 17, 19]),
            (20, "Critically evaluate compound drought-heat risk, anticipatory action and maladaptation in Indian cities and rural regions.", [6, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Meteorological", "Agricultural drought", "Hydrological drought",
            "Socio-economic", "aridity", "Heat Wave", "heat-risk",
            "wet-bulb", "Heat Action Plans", "slow-onset",
            "anticipatory action", "maladaptation", "soil moisture",
            "groundwater", "Manual for Drought Management",
        ],
        "The 2025 wet-bulb card is the only direct topic-specific route. The 2024 resilience and 2020 proactive-governance cards are explicitly support/adjacent applications and do not manufacture drought- or heat-specific PYQs.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered the Agriculture drought manual, IMD heat guidance, CGWB/CWC water mandates, ICAR-CRIDA and a PIB Heat Action Plan route. Raw, thin, blocked and failed pages are recorded; no current drought grade, rainfall, groundwater, crop-loss, HAP coverage, temperature, illness or mortality figure was imported.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "DROUGHT TYPE ARIDITY SCARCITY HEAT HAZARD AND EXPOSURE MAP",
            "DECLARATION WET-BULB HAP FORECAST AND OUTCOME FIREWALLS",
            "WATER AGRICULTURE URBAN LABOUR HEALTH EARLY-ACTION SPINE",
            "CURRENT IMD AGRICULTURE CGWB CWC ICAR AND EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DISTINGUISH ARIDITY SCARCITY AND EACH DROUGHT TYPE",
            "TRACE RAINFALL SOIL STORAGE ECOSYSTEM LIVELIHOOD AND HEALTH LAGS",
            "NAME THE MANUAL'S MULTI-INDICATOR STRUCTURE WITHOUT GUESSED CUT-OFFS",
            "SEPARATE IMD HEAT HAZARD FROM HEAT STRESS WET-BULB AND EXPOSURE",
            "ASSIGN HAP WATER AGRICULTURE URBAN LABOUR AND HEALTH ACTIONS",
            "TRIGGER EARLY ACTION AND TEST MALADAPTATION EQUITY AND RESIDUAL RISK",
            "VERIFY REACH ACCESS CONTINUITY AND OUTCOMES",
        ],
    )


TOPIC_09 = _build()
