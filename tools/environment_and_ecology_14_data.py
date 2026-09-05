"""Authored data for Environment and Ecology learner-v2 Topic 14."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import (
    WATER_POLLUTION_LIVE_SOURCE_ATTEMPTS,
    panel,
)


FACTS = [
    ("Point and non-point sources", "A point source has an identifiable discharge location, while non-point pollution is diffuse across a catchment; the monitoring and regulatory tools are therefore different."),
    ("Water-quality and effluent boundary", "Receiving-water quality describes the water body, whereas an effluent standard controls a discharge from a source; meeting one cannot be assumed from the other."),
    ("Water class and discharge boundary", "A designated water-use class or criterion is not an industry effluent limit; each numeric value must retain its indicator, unit, sampling basis and legal source."),
    ("BOD and DO relation", "Biochemical Oxygen Demand indicates oxygen used in microbial decomposition of organic matter, while Dissolved Oxygen is oxygen available in water; high organic load can raise BOD and depress DO."),
    ("Faecal-indicator boundary", "Faecal coliform is an indicator of faecal contamination and possible pathogen risk; it is not a direct count of every pathogen or a complete water-quality verdict."),
    ("Eutrophication chain", "Excess nutrient loading can drive algal growth, decomposition and oxygen depletion; nutrient enrichment is distinct from, though it can coexist with, sewage and toxic industrial pollution."),
    ("Water Act institution layer", "The Water Act establishes the CPCB-SPCB pollution-control architecture, while state boards administer major consent, monitoring and enforcement functions for discharges."),
    ("CTE and CTO boundary", "Consent to Establish and Consent to Operate regulate a source under pollution-control law; neither is the same as prior environmental clearance, river-mission approval or proof of continuous compliance."),
    ("Sewage quantity chain", "Sewage generated, sewered flow, installed treatment capacity, commissioned capacity, actual inflow, compliant treatment and reuse are separate quantities."),
    ("Capacity and utilisation", "An STP's rated or installed capacity is not its actual operating load, treatment performance, utilisation or receiving-river outcome."),
    ("Municipal and industrial streams", "Municipal sewage and industrial effluent differ in source, composition, treatment train, monitoring and responsible institution; neither should be used as a proxy for the other."),
    ("STP ETP and CETP", "An STP treats sewage, an ETP treats an individual establishment's effluent, and a CETP serves a group of units; installation is not proof of compliant operation."),
    ("Regulation and mission boundary", "Water Act regulation applies through pollution-control institutions, while a river-cleaning mission coordinates projects and basin action; a mission does not replace statutory consent enforcement."),
    ("NMCG institutional boundary", "NMCG implements the Ganga mission within its notified institutional architecture; it is not interchangeable with CPCB, an SPCB, an urban local body or a generic all-river regulator."),
    ("Namami Gange component boundary", "River rejuvenation can combine sewage infrastructure, industrial monitoring, river-surface action, biodiversity, afforestation and public participation; visible works alone do not prove water-quality improvement."),
    ("NRCP and river scope", "The National River Conservation Plan and Ganga-specific architecture have different programme scopes; a Ganga institution or result cannot automatically be assigned to every river."),
    ("Input output outcome chain", "Mission outlay, sanction, expenditure, infrastructure completed, flow treated, pollutant load reduced and river-quality outcome are distinct stages."),
    ("Stretch season indicator", "River quality varies by monitoring location, season, flow and indicator; a result for one stretch or period cannot establish that an entire river is clean."),
    ("Dilution and ecological flow", "Higher flow may dilute a measured concentration without removing pollutant mass or source discharge; river rejuvenation therefore cannot be reduced to dilution."),
    ("Audited evidence boundary", "Audited ledgers carry industrial river pollution, freshwater treatment technologies, membrane bioreactors, activated carbon, microbeads and sand-mining effects into practice without inventing keys, capacities, outlays or river-quality values."),
]

TRAPS = [
    "Do not write a receiving-water criterion as an effluent limit.",
    "Do not treat a designated water-use class as a source standard.",
    "Do not say high BOD means oxygen-rich clean water.",
    "Do not treat faecal coliform as a count of every pathogen.",
    "Do not merge nutrient eutrophication with every form of sewage pollution.",
    "Do not exchange CPCB coordination and SPCB consent enforcement.",
    "Do not merge CTE, CTO and prior environmental clearance.",
    "Do not report sewage generation as sewered or treated flow.",
    "Do not report installed STP capacity as utilisation or outcome.",
    "Do not merge municipal sewage with industrial effluent.",
    "Do not treat an installed ETP or CETP as continuous compliance.",
    "Do not treat Namami Gange as the Water Act regulator.",
    "Do not generalise a Ganga institution or result to every river.",
    "Do not report mission input or output as river-quality outcome.",
    "Do not infer an entire river's status from one stretch, season or indicator.",
]

SESSION_TITLES = [
    "Point sources non-point sources and pathways",
    "Receiving-water quality and effluent standards",
    "Water-use classes indicators units and sampling",
    "BOD DO and faecal contamination",
    "Eutrophication and nutrient loading",
    "Water Act CPCB and SPCB architecture",
    "CTE CTO and prior-clearance boundary",
    "Sewage generation sewering and treatment chain",
    "Installed capacity operation and utilisation",
    "Municipal sewage and industrial effluent",
    "STP ETP and CETP treatment roles",
    "Regulation river missions and NMCG",
    "Namami Gange components and NRCP scope",
    "Inputs outputs outcomes stretch and season",
    "Evidence-safe exam synthesis",
]

ANSWER_ROUTES = [
    "Begin by locating the discharge and deciding whether the source is point or diffuse.",
    "Keep receiving-water and source-discharge standards on separate lines.",
    "Name the indicator, use class, unit and sampling basis before quoting a value.",
    "Explain organic load through BOD and DO, then add the pathogen-indicator limit.",
    "Trace nutrients to algal growth, decomposition and oxygen depletion.",
    "Assign standards, coordination, consent and enforcement to the correct board.",
    "List each approval separately and never infer compliance from possession.",
    "Trace sewage from generation through sewer connection to actual treatment.",
    "Use operation and compliant output, not installed nameplate capacity, as evidence.",
    "Diagnose municipal and industrial streams separately before combining policy.",
    "Match STP, ETP and CETP to the waste stream and responsible operator.",
    "Place statutory regulation beside the mission rather than replacing it.",
    "State the Ganga-specific and wider river-programme boundaries.",
    "Move from money and assets to treated flow, load reduction and monitored outcome.",
    "Close with verified PYQ ownership and explicit current-data limits.",
]

PANELS = [
    panel("Source-pathway map", "comparison-table", [
        "POINT SOURCE -> identifiable pipe, drain or outfall",
        "NON-POINT SOURCE -> diffuse catchment runoff",
        "PATHWAY -> source to receiving water",
        "MONITORING -> source sample versus catchment evidence",
        "CONTROL -> tool must match the pathway",
    ], [FACTS[0][0]]),
    panel("Standard firewall", "comparison-table", [
        "EFFLUENT STANDARD -> controls discharge from a source",
        "WATER-QUALITY CRITERION -> describes receiving water",
        "USE CLASS -> intended-water-use framework",
        "UNIT AND SAMPLING -> belong to the exact indicator",
        "RULE -> never exchange these values",
    ], [FACTS[1][0], FACTS[2][0]]),
    panel("Organic-pollution diagnostic", "process-flow", [
        "ORGANIC LOAD -> microbial decomposition",
        "BOD -> oxygen demand during decomposition",
        "DO -> oxygen remaining for aquatic life",
        "FAECAL INDICATOR -> contamination warning",
        "DIAGNOSIS -> use indicators together, not interchangeably",
    ], [FACTS[3][0], FACTS[4][0]]),
    panel("Eutrophication chain", "process-flow", [
        "NUTRIENT INPUT -> nitrogen or phosphorus enrichment",
        "ALGAL GROWTH -> biomass increase",
        "DECOMPOSITION -> oxygen demand",
        "LOW OXYGEN -> ecological stress",
        "BOUNDARY -> not identical to toxic industrial discharge",
    ], [FACTS[5][0]]),
    panel("Institution and approval ladder", "hierarchy", [
        "WATER ACT -> statutory pollution-control framework",
        "CPCB -> national coordination and framework",
        "SPCB OR PCC -> consent, monitoring and enforcement",
        "CTE OR CTO -> source permission layer",
        "ENVIRONMENTAL CLEARANCE -> separate prior-appraisal layer",
    ], [FACTS[6][0], FACTS[7][0]]),
    panel("Sewage quantity ledger", "layered-rail", [
        "GENERATED -> total wastewater produced",
        "SEWERED -> flow reaching a network",
        "INSTALLED -> nameplate treatment capacity",
        "ACTUALLY TREATED -> operating inflow and performance",
        "REUSED OR DISCHARGED -> final pathway and quality",
    ], [FACTS[8][0], FACTS[9][0]]),
    panel("Treatment-plant matrix", "comparison-table", [
        "STP -> municipal or domestic sewage",
        "ETP -> one establishment's industrial effluent",
        "CETP -> common treatment for a group of units",
        "INSTALLATION -> infrastructure output",
        "COMPLIANT OPERATION -> separately verified performance",
    ], [FACTS[10][0], FACTS[11][0]]),
    panel("Regulator-mission firewall", "comparison-table", [
        "CPCB OR SPCB -> statutory pollution-control role",
        "RIVER MISSION -> project and basin coordination",
        "NMCG -> Ganga mission implementation architecture",
        "ULB -> sewerage service and local operation",
        "RULE -> one actor never substitutes for all others",
    ], [FACTS[12][0], FACTS[13][0]]),
    panel("River-mission component wheel", "layered-rail", [
        "SEWAGE INFRASTRUCTURE -> intercept and treat flow",
        "INDUSTRIAL MONITORING -> source compliance",
        "ECOLOGY -> biodiversity and riverbank measures",
        "PUBLIC PARTICIPATION -> behaviour and accountability",
        "VISIBLE WORK -> not itself a water-quality outcome",
    ], [FACTS[14][0]]),
    panel("Programme-scope gate", "decision-gate", [
        "GANGA QUESTION -> use notified Ganga architecture",
        "OTHER RIVER -> identify applicable programme and state actors",
        "NRCP -> wider river-conservation programme context",
        "RESULT -> retain river, stretch and date",
        "NO TRANSFER -> never move one mission result to another river",
    ], [FACTS[15][0]]),
    panel("Performance and evidence chain", "process-flow", [
        "OUTLAY OR SANCTION -> input",
        "EXPENDITURE -> financial activity",
        "ASSET COMPLETED -> physical output",
        "FLOW TREATED OR LOAD REDUCED -> operational result",
        "RIVER QUALITY -> stretch-season-indicator outcome",
    ], [FACTS[16][0], FACTS[17][0], FACTS[18][0]]),
    panel("Water answer spine", "answer-spine", [
        "DIAGNOSE -> source, pathway and pollutant",
        "MEASURE -> indicator, unit, location, season and sampling",
        "REGULATE -> consent, effluent control and enforcement",
        "TREAT -> sewer network, STP, ETP or CETP operation",
        "JUDGE -> load and river outcome, with PYQ and live-data limits",
    ], [FACTS[19][0]]),
]

TOPIC_14 = common.topic(
    14,
    "Water Pollution and River Cleaning Missions",
    "14_Water-Pollution-and-River-Cleaning-Missions",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-14_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish receiving-water criteria from source-effluent standards.", [0, 1, 2]),
        (10, "Explain the use and limits of BOD, DO and faecal indicators.", [3, 4, 5]),
        (15, "Trace sewage from generation to compliant treatment and reuse.", [8, 9, 11]),
        (15, "Distinguish Water Act regulation from river-mission implementation.", [6, 7, 12, 13, 15]),
        (20, "Evaluate river cleaning through input, output, utilisation and outcome metrics.", [8, 9, 14, 16, 17, 18]),
        (20, "Build an integrated response to municipal, industrial and diffuse water pollution.", [0, 5, 6, 10, 11, 12, 17, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "point source", "non-point source", "water-quality criterion",
        "effluent standard", "use class", "BOD", "Dissolved Oxygen",
        "faecal coliform", "eutrophication", "Water Act", "CPCB", "SPCB",
        "Consent to Establish", "Consent to Operate", "sewage generation",
        "installed capacity", "utilisation", "STP", "ETP", "CETP",
        "NMCG", "Namami Gange", "NRCP", "river stretch",
    ],
    (
        "Audited ledgers route direct Mains demands on industrial river "
        "pollution and freshwater technologies, plus objective concepts on "
        "membrane bioreactors, activated carbon, PFAS, microbeads and sand-"
        "mining effects. No objective key or current mission metric is inferred."
    ),
    [],
    WATER_POLLUTION_LIVE_SOURCE_ATTEMPTS,
    (
        "NMCG home, status and guideline pages were stubs; the 2026 press PDF "
        "was retrievable only as raw bytes; CPCB pages exposed only a yearly-"
        "data heading or board title. No outlay, target, sewage generation, "
        "installed or utilised capacity, project count, river value or outcome "
        "was imported."
    ),
    extra=[
        "basic/02_Biogeochemical-Cycles-and-Ecological-Pyramids.md",
        "basic/15_Solid-Plastic-and-E-Waste-Rules.md",
        "basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
        "advanced/02_Biogeochemical-Cycles-and-Ecological-Pyramids.md",
        "advanced/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
    ],
    pyq_audit_heading="AUDITED WATER-POLLUTION, TREATMENT AND RIVER-MISSION PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "SOURCE, PATHWAY, INDICATOR, STANDARD AND TREATMENT MAP",
        "WATER CLASS, EFFLUENT, CAPACITY, UTILISATION AND OUTCOME TRAPS",
        "RIVER-CLEANING GOVERNANCE ANSWER SPINE",
        "LIVE CAPACITY, OUTLAY, RIVER-QUALITY AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "IDENTIFY POINT OR NON-POINT SOURCE AND RECEIVING WATER",
        "SEPARATE WATER-QUALITY CRITERION FROM EFFLUENT STANDARD",
        "USE BOD, DO, FAECAL INDICATOR AND NUTRIENTS PRECISELY",
        "TRACE GENERATED, SEWERED, INSTALLED, OPERATED AND TREATED FLOW",
        "MATCH STP, ETP AND CETP TO THE CORRECT STREAM",
        "SEPARATE WATER ACT REGULATION FROM RIVER-MISSION DELIVERY",
        "CONCLUDE WITH LOAD REDUCTION AND STRETCH-SEASON OUTCOME MONITORING",
    ],
)
