"""Authored data for Environment and Ecology learner-v2 Topic 23."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import panel


FACTS = [
    ("Land-degradation umbrella", "Land degradation is a reduction or loss of land's biological or economic productivity or ecological function across land types; the driver, indicator and spatial boundary must be stated."),
    ("Desertification dryland boundary", "Desertification is land degradation in arid, semi-arid and dry sub-humid areas resulting from climatic variations and human activities; it is not simply the outward spread of a sand desert."),
    ("Drought event boundary", "Drought is a period of abnormal water deficit relative to local conditions and is an event or hazard, while desertification is a degradation process; one can influence the other without becoming identical."),
    ("Drought-risk components", "Drought disaster risk arises from the interaction of hazard, exposure and vulnerability; rainfall deficit alone does not determine livelihood, ecosystem or economic loss."),
    ("UNCCD treaty identity", "The UNCCD is the legally binding convention focused on desertification and the effects of drought through cooperation, national action and sustainable land management; treaty purpose is distinct from a single restoration programme."),
    ("Rio-convention relationship", "UNCCD, UNFCCC and CBD are related Rio-era regimes with interacting land, climate and biodiversity concerns, but their treaty objects, reporting systems and decisions remain separate."),
    ("National action pathway", "UNCCD implementation proceeds through national action programmes, enabling policy, participation, finance, knowledge and monitoring; submitting a plan does not prove restored land or reduced drought loss."),
    ("LDN definition", "Land Degradation Neutrality is a state in which the amount and quality of land resources needed to support ecosystem functions and services and food security remain stable or increase within specified spatial and temporal scales."),
    ("LDN baseline boundary", "An LDN claim requires a defined baseline, accounting unit, spatial scale, period and indicators; neutrality cannot be inferred from a national restoration announcement alone."),
    ("Avoid-reduce-reverse hierarchy", "LDN implementation prioritises avoiding new degradation, reducing ongoing degradation through sustainable land management, and reversing past degradation through restoration or rehabilitation."),
    ("Neutrality-not-zero boundary", "LDN is a counterbalancing no-net-loss framework at a defined scale, not a promise that no parcel will degrade; gains and losses are not automatically ecologically equivalent."),
    ("Indicator-evidence boundary", "Land cover, land productivity and soil organic carbon can support LDN monitoring, but each indicator has method, resolution and interpretation limits and does not alone establish every ecosystem service."),
    ("Remote-ground integration", "Remote sensing reveals spatial patterns and trends, while field soil, water, vegetation and livelihood evidence tests ecological meaning; one image or one season cannot establish a persistent process."),
    ("Driver interaction", "Climatic variability, vegetation removal, overgrazing, erosion, salinisation, unsustainable cultivation and water use can interact; national degradation totals do not imply one uniform cause."),
    ("Restoration-quality boundary", "Area treated, trees planted, money spent and ecological recovery are different outputs or outcomes; restoration quality requires function, native-system suitability, persistence and livelihood evidence."),
    ("Commensurability limit", "Restoration gains elsewhere may not replace the soil, hydrology, biodiversity, tenure or livelihood functions lost at the degraded site, so LDN accounting needs safeguards beyond aggregate area."),
    ("Watershed response chain", "Dryland response links soil cover, infiltration, runoff control, groundwater demand, crop or grazing choice and local institutions; tree planting alone is not a universal remedy."),
    ("Rangeland and open-ecosystem boundary", "Rangelands, grasslands and scrub can be functioning open natural ecosystems; classifying them as wasteland or afforesting them indiscriminately can create a false restoration claim."),
    ("Target-decision-outcome boundary", "A national LDN target, COP declaration, partnership, finance pledge, project approval and verified land or drought outcome are separate statuses and must be attributed precisely."),
    ("Current evidence boundary", "Land-degradation extent, LDN targets, restored area, drought trends, affected population, finance and COP outcomes require a dated official atlas, UNCCD decision or national report; scheduled negotiations are not outcomes."),
]

TRAPS = [
    "Do not merge land degradation with desertification.",
    "Do not define desertification as advancing sand.",
    "Do not merge drought events with long-term degradation.",
    "Do not equate hazard with disaster risk.",
    "Do not reduce the UNCCD to one restoration project.",
    "Do not merge the three Rio Conventions' obligations.",
    "Do not treat an action plan as an achieved outcome.",
    "Do not quote LDN without its spatial and temporal scale.",
    "Do not infer neutrality without a baseline and indicators.",
    "Do not reverse the avoid-reduce-reverse hierarchy.",
    "Do not interpret LDN as zero degradation on every parcel.",
    "Do not treat one indicator as complete ecological proof.",
    "Do not infer a persistent trend from one image or season.",
    "Do not attribute all degradation to one driver.",
    "Do not merge area treated or trees planted with recovery.",
    "Do not assume restoration sites are ecologically interchangeable.",
    "Do not prescribe tree planting as the universal dryland response.",
    "Do not call functioning rangeland wasteland by default.",
    "Do not merge target, pledge, project and verified outcome.",
    "Do not invent degradation, target, drought, finance or COP figures.",
]

SESSION_TITLES = [
    "Land degradation desertification and dryland scope",
    "Drought event boundary",
    "Drought hazard exposure and vulnerability",
    "UNCCD treaty identity",
    "Rio-convention relationship",
    "National action pathway and LDN definition",
    "LDN baseline scale period and indicators",
    "Avoid reduce reverse response hierarchy",
    "Neutrality counterbalancing and parcel boundary",
    "LDN indicator evidence boundary",
    "Remote sensing ground evidence and driver interaction",
    "Restoration output and ecological outcome",
    "Commensurability soil water biodiversity and tenure",
    "Watersheds rangelands and open ecosystems",
    "Target COP partnership outcome and current evidence audit",
]

ANSWER_ROUTES = [
    "Start with the land-degradation umbrella and narrow desertification to drylands.",
    "Separate drought hazard from exposure, vulnerability and realised loss.",
    "Define the UNCCD and distinguish its object from climate and biodiversity treaties.",
    "Move from national plan to institutions, finance, participation, monitoring and outcome.",
    "Quote LDN as stability or increase within specified scales.",
    "State baseline, accounting unit, period and indicators before claiming neutrality.",
    "Use avoid, reduce and reverse in that priority order.",
    "Explain counterbalancing while testing parcel and ecosystem equivalence.",
    "Combine multi-year remote-sensing trends with field evidence.",
    "Build a causal chain that allows climatic and human interactions.",
    "Separate expenditure, treatment and planting outputs from functional recovery.",
    "Test soil, hydrology, biodiversity, tenure and livelihood substitutability.",
    "Organise remedies through watershed processes and local land use.",
    "Recognise functioning open ecosystems before prescribing afforestation.",
    "Close with dated official targets, decisions, atlases and outcomes.",
]

PANELS = [
    panel("Land concept nesting", "hierarchy", [
        "LAND DEGRADATION -> broad productivity and function loss",
        "DESERTIFICATION -> degradation inside defined drylands",
        "DROUGHT -> abnormal water-deficit event or hazard",
        "INTERACTION -> drought can intensify degradation",
        "NO MERGER -> process event and spatial scope differ",
    ], [FACTS[0][0], FACTS[1][0], FACTS[2][0]]),
    panel("Drought-risk triangle", "causal-chain", [
        "HAZARD -> severity duration timing and spatial extent",
        "EXPOSURE -> people crops livestock ecosystems and assets",
        "VULNERABILITY -> sensitivity and coping capacity",
        "RISK -> interaction of all three",
        "LOSS -> realised impact, not rainfall deficit alone",
    ], [FACTS[3][0]]),
    panel("Rio convention map", "comparison-table", [
        "UNCCD -> desertification land degradation and drought effects",
        "UNFCCC -> climate system and greenhouse-gas response",
        "CBD -> biodiversity conservation use and benefit-sharing",
        "SYNERGY -> land connects all three",
        "RULE -> institutions reports and decisions remain distinct",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("UNCCD implementation rail", "process-flow", [
        "TREATY OBJECTIVE -> cooperation and land stewardship",
        "NATIONAL ACTION PROGRAMME -> country planning",
        "ENABLING POLICY AND FINANCE -> implementation capacity",
        "PARTICIPATION -> land users and local institutions",
        "MONITORING AND OUTCOME -> separate evidence stage",
    ], [FACTS[6][0], FACTS[18][0]]),
    panel("LDN accounting frame", "comparison-table", [
        "BASELINE -> starting condition",
        "SPATIAL SCALE -> accounting boundary",
        "TEMPORAL SCALE -> comparison period",
        "AMOUNT AND QUALITY -> land resource condition",
        "NEUTRALITY -> stable or increased functional resource base",
    ], [FACTS[7][0], FACTS[8][0]]),
    panel("LDN response hierarchy", "layered-rail", [
        "AVOID -> protect healthy land first",
        "REDUCE -> slow current degradation",
        "REVERSE -> restore or rehabilitate degraded land",
        "MONITOR -> indicators against baseline",
        "SAFEGUARD -> no automatic ecological equivalence",
    ], [FACTS[9][0], FACTS[10][0]]),
    panel("Indicator evidence board", "comparison-table", [
        "LAND COVER -> class and conversion pattern",
        "LAND PRODUCTIVITY -> trend in productive function",
        "SOIL ORGANIC CARBON -> soil carbon condition",
        "METHOD LIMIT -> resolution baseline and interpretation",
        "GROUND CHECK -> soil water vegetation and livelihoods",
    ], [FACTS[11][0], FACTS[12][0]]),
    panel("Degradation driver web", "causal-chain", [
        "CLIMATE VARIABILITY -> water stress and disturbance",
        "VEGETATION LOSS OR OVERGRAZING -> exposed soil",
        "EROSION OR SALINISATION -> declining function",
        "UNSUSTAINABLE WATER USE -> hydrological stress",
        "FEEDBACK -> lower resilience and greater drought impact",
    ], [FACTS[13][0]]),
    panel("Restoration evidence ladder", "hierarchy", [
        "MONEY SPENT -> financial input",
        "AREA TREATED -> programme output",
        "TREES OR STRUCTURES -> physical output",
        "FUNCTION RECOVERED -> ecological outcome",
        "PERSISTENCE AND LIVELIHOODS -> long-term result",
    ], [FACTS[14][0]]),
    panel("Commensurability test", "decision-tree", [
        "SOIL -> fertility erosion and carbon function comparable",
        "WATER -> infiltration runoff and aquifer effect comparable",
        "BIODIVERSITY -> native open or wooded system respected",
        "TENURE AND LIVELIHOOD -> users and rights considered",
        "VERDICT -> aggregate area alone cannot prove replacement",
    ], [FACTS[15][0], FACTS[17][0]]),
    panel("Dryland response chain", "process-flow", [
        "SOIL COVER -> reduce erosion",
        "INFILTRATION AND RUNOFF -> watershed treatment",
        "DEMAND -> groundwater crops and grazing pressure",
        "INSTITUTIONS -> commons tenure and participation",
        "ADAPTIVE MONITORING -> drought and recovery feedback",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("UNCCD answer spine", "answer-spine", [
        "DEFINE -> degradation desertification drought and risk",
        "PLACE -> UNCCD and LDN within distinct treaty roles",
        "ACCOUNT -> baseline scale period indicators and hierarchy",
        "TEST -> causes quality commensurability and open ecosystems",
        "VERIFY -> target atlas COP finance and measured outcome",
    ], [FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2020", "GS-I",
        "Justify that desertification as a process is not confined by climatic boundaries.",
        "Verified routed demand; the answer must still preserve the UNCCD dryland definition.",
        [0, 1, 2, 13, 16, 19],
    ),
]

LIVE_SOURCES = [
    "https://www.unccd.int/convention/about-convention — attempted 2026-09-03; the official redirect supplied substantive treaty-purpose text and identified the UNCCD as the legally binding framework on desertification and drought effects.",
    "https://www.unccd.int/land-and-life/land-degradation-neutrality/overview — attempted 2026-09-03; substantive official text supplied the LDN definition and avoid-reduce-reverse hierarchy; headline global figures were not imported into authored anchors.",
    "https://www.unccd.int/news-stories/press-releases/global-response-drought-takes-center-stage-un-land-conference-riyadh — attempted 2026-09-03; substantive official text described negotiations and a partnership, but no draft, pledge or opening statement was converted into a binding drought regime or verified outcome.",
    "https://dolr.gov.in/ — attempted 2026-09-03; no dated topic-specific LDN progress or restoration-outcome text was retrieved for use.",
    "https://www.sac.gov.in/ — attempted 2026-09-03; no atlas edition, degradation extent or trend figure was imported from the general institutional route.",
]

TOPIC_23 = common.topic(
    23,
    "Desertification UNCCD and Land Degradation",
    "23_Desertification-UNCCD-and-Land-Degradation",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-23_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish land degradation, desertification and drought.", [0, 1, 2, 3]),
        (10, "Explain the UNCCD implementation pathway.", [4, 5, 6]),
        (15, "Explain LDN definition, baseline and response hierarchy.", [7, 8, 9, 10, 11]),
        (15, "Assess how land degradation should be monitored.", [11, 12, 13, 19]),
        (20, "Critically evaluate LDN counterbalancing and restoration quality.", [8, 10, 14, 15, 17]),
        (20, "Design an integrated dryland and drought-resilience response.", [2, 3, 13, 16, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "land degradation", "desertification", "drylands", "drought",
        "hazard", "exposure", "vulnerability", "UNCCD", "Rio Conventions",
        "national action programmes", "Land Degradation Neutrality",
        "baseline", "spatial", "temporal", "avoid", "reduce", "reverse",
        "counterbalancing", "land cover", "land productivity",
        "soil organic carbon", "remote sensing", "ground evidence",
        "restoration quality", "commensurability", "watershed",
        "rangelands", "open natural ecosystems", "target", "outcome",
    ],
    (
        "Audited ledgers route the verified 2020 GS-I desertification demand and "
        "related soil and land concepts. The package does not infer an objective "
        "key, atlas statistic, national target achievement or official model answer."
    ),
    PYQ_SOLUTIONS,
    LIVE_SOURCES,
    (
        "UNCCD pages supplied substantive treaty and LDN definitions and the "
        "avoid-reduce-reverse hierarchy. Opening negotiations and pledges were "
        "not treated as a concluded regime. No degradation extent, LDN target, "
        "restored area, drought trend, population, finance or COP outcome is asserted."
    ),
    extra=[
        "basic/03_Ecological-Succession-and-Biomes.md",
        "basic/11_Forest-Types-and-Forest-Rights-Act.md",
        "basic/12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
        "basic/19_UNFCCC-COP-Kyoto-Paris-Agreement.md",
        "advanced/03_Ecological-Succession-and-Biomes.md",
        "advanced/12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
    ],
    pyq_audit_heading="AUDITED DESERTIFICATION, DROUGHT, UNCCD, LDN AND RESTORATION PYQ OWNERSHIP",
    register_headings=(
        "DRYLAND, DROUGHT-RISK, UNCCD AND LDN MAP",
        "BASELINE, INDICATOR, COUNTERBALANCING AND RESTORATION-QUALITY TRAPS",
        "LAND-DEGRADATION ANSWER SPINE",
        "LIVE ATLAS, TARGET, DROUGHT, FINANCE AND COP-OUTCOME EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "DEFINE LAND DEGRADATION THEN NARROW DESERTIFICATION TO DRYLANDS",
        "SEPARATE DROUGHT HAZARD FROM EXPOSURE VULNERABILITY AND LOSS",
        "PLACE UNCCD AND LDN WITHIN THEIR TREATY AND ACCOUNTING SCOPE",
        "STATE BASELINE SCALE PERIOD INDICATORS AND AVOID-REDUCE-REVERSE",
        "TEST REMOTE SENSING WITH SOIL WATER VEGETATION AND LIVELIHOOD EVIDENCE",
        "TEST RESTORATION QUALITY COMMENSURABILITY AND OPEN-ECOSYSTEM SUITABILITY",
        "CONCLUDE WITH DATED ATLAS TARGET COP FINANCE AND OUTCOME EVIDENCE",
    ],
    allow_existing_history=True,
)
