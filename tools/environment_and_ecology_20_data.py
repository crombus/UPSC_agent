"""Authored data for Environment and Ecology learner-v2 Topic 20."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import INDIA_CLIMATE_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("NAPCC identity", "The National Action Plan on Climate Change is India's domestic mission-based climate framework launched in 2008; it is not an NDC, treaty or long-term strategy."),
    ("Original eight missions", "NAPCC originally organised action through eight national missions covering solar energy, enhanced energy efficiency, sustainable habitat, water, the Himalayan ecosystem, Green India, sustainable agriculture and strategic climate knowledge."),
    ("Mitigation-adaptation portfolio", "The NAPCC missions combine mitigation, adaptation, knowledge and development co-benefits; no mission label should be assumed to represent only one response category."),
    ("SAPCC boundary", "State Action Plans on Climate Change translate climate priorities into state contexts; a state plan is not proof of implementation, finance or achieved resilience."),
    ("Panchamrit status", "Panchamrit is the five-part political announcement made by India at COP26; announcement, later NDC communication, domestic implementation and verified achievement are distinct stages."),
    ("Panchamrit five elements", "The announced Panchamrit comprised 500 GW non-fossil capacity by 2030, 50 percent of energy requirements from renewables by 2030, a one-billion-tonne reduction in projected carbon emissions by 2030, a 45 percent emissions-intensity reduction from 2005 by 2030, and net zero by 2070."),
    ("Updated NDC quantified terms", "India's 2022 updated NDC formally strengthened the quantified 2030 emissions-intensity target to 45 percent from the 2005 level and the cumulative installed electric-power capacity target to about 50 percent from non-fossil sources."),
    ("Forest-sink continuity", "The additional forest-and-tree-cover carbon-sink objective belongs to India's communicated NDC architecture and must be distinguished from Panchamrit's five announced elements and from a verified sink achievement."),
    ("Panchamrit-NDC boundary", "Not every Panchamrit phrase became a separately quantified term in the 2022 updated NDC; the political announcement and communicated contribution must be read as separate official instruments."),
    ("LT-LEDS identity", "India's Long-Term Low-Carbon Development Strategy was submitted to the UNFCCC in 2022 as a long-horizon strategic pathway; it is distinct from the shorter-term NDC and is not a domestic penalty-bearing law."),
    ("LT-LEDS pathway families", "The LT-LEDS addresses low-carbon electricity, integrated transport, sustainable urbanisation and buildings, lower-emission industry, carbon-dioxide removal, forest and vegetative cover, and economic or financial aspects of transition."),
    ("Net-zero pathway boundary", "The announced net-zero year states a long-term destination, while LT-LEDS discusses pathways and enabling conditions; neither proves a linear trajectory or achieved net-zero balance."),
    ("Intensity-absolute distinction", "Emissions intensity measures emissions per unit of economic output, whereas absolute emissions measure total emissions; intensity can fall while total emissions follow a different path."),
    ("Capacity-generation-energy distinction", "Installed power capacity, electricity generation and the share of total energy requirements are different denominators; a non-fossil capacity percentage cannot be relabelled as renewable generation or total-energy share."),
    ("Target-achievement distinction", "A target states an intended future result, while achievement requires source-dated measured evidence against the same metric, boundary, baseline and target year."),
    ("Gross-net distinction", "Gross emissions, gross removals and net emissions balance are separate quantities; a net-zero claim requires a defined boundary and cannot be inferred from one sectoral capacity milestone."),
    ("BUR-NDC-LTLEDS distinction", "A Biennial Update Report is backward-looking reporting, an NDC is a forward nationally determined contribution, and LT-LEDS is a long-term strategy; none is a substitute for the others."),
    ("Co-benefits and equity", "India frames climate action alongside development, energy access, resilience, equity and CBDR-RC; this analytical framing does not remove the need to evaluate measurable domestic implementation."),
    ("Sector-interdependency", "Power, transport, industry, buildings, land and finance pathways interact, so progress in one sector can depend on grid, storage, technology, land, institutions and capital elsewhere."),
    ("Current-status evidence boundary", "Current mission counts, NDC status, installed capacity, generation, emissions, sinks, finance and achievement claims must come from a dated official source; conflicting registry discovery is recorded rather than resolved by guesswork."),
]

TRAPS = [
    "Do not call NAPCC an NDC, treaty or LT-LEDS.",
    "Do not replace the original eight NAPCC missions with an undated current count.",
    "Do not treat every mission as exclusively mitigation or exclusively adaptation.",
    "Do not treat an SAPCC document as proof of implementation or outcome.",
    "Do not merge a Panchamrit announcement with a communicated NDC.",
    "Do not alter the Panchamrit wording, target year, percentage, baseline or denominator.",
    "Do not say all five Panchamrit elements became quantified 2022 NDC targets.",
    "Do not call the forest-sink objective a separate Panchamrit element.",
    "Do not call LT-LEDS the same document as the NDC.",
    "Do not treat LT-LEDS pathways as legally binding sectoral caps or penalties.",
    "Do not merge emissions intensity with absolute emissions.",
    "Do not merge installed capacity, electricity generation and total energy requirements.",
    "Do not present a target as an achievement.",
    "Do not infer net zero from one sectoral or capacity milestone.",
    "Do not merge BUR reporting, NDC pledge and LT-LEDS strategy.",
    "Do not assert a post-2022 India NDC status from conflicting search discovery.",
]

SESSION_TITLES = [
    "NAPCC identity and original eight missions",
    "Mitigation adaptation knowledge and co-benefits",
    "SAPCC state translation and implementation boundary",
    "Panchamrit announcement and five elements",
    "Panchamrit target-type classification",
    "Updated NDC quantified terms and forest-sink continuity",
    "Political pledge versus communicated NDC",
    "LT-LEDS identity and legal status",
    "LT-LEDS sectoral pathway families",
    "Net-zero destination and pathway boundary",
    "Intensity and energy-denominator accounting",
    "Target versus achievement",
    "Gross and net emissions balance",
    "BUR reporting and co-benefits distinction",
    "Equity interdependency and current evidence boundary",
]

ANSWER_ROUTES = [
    "Define NAPCC as domestic policy and list the original missions exactly.",
    "Classify each mission by response function while retaining development co-benefits.",
    "Move from state planning to finance, implementation, monitoring and outcome evidence.",
    "Reproduce Panchamrit only with the exact official wording, metric and year.",
    "Classify each element as capacity, share, projected reduction, intensity or net-zero goal.",
    "Quote only the two strengthened quantified 2030 terms in the updated NDC.",
    "Keep the forest-sink objective inside the communicated NDC architecture.",
    "Separate speech announcement, formal communication and domestic action.",
    "Define LT-LEDS as a long-term strategy rather than a binding domestic statute.",
    "Organise the strategy by interacting sectoral transitions and enabling conditions.",
    "Separate long-term destination, strategic pathway and measured trajectory.",
    "State the numerator, denominator, baseline, period and netting boundary.",
    "Identify whether the claim concerns capacity, generation, electricity or total energy.",
    "Match every achievement claim to a dated official measurement and reporting instrument.",
    "Conclude with equity and co-benefits while auditing current status and cross-sector constraints.",
]

PANELS = [
    panel("India climate-policy timeline", "timeline", [
        "2008 NAPCC -> domestic mission-based framework",
        "PARIS NDC -> internationally communicated contribution",
        "COP26 PANCHAMRIT -> five-part political announcement",
        "2022 UPDATED NDC -> strengthened communicated 2030 terms",
        "2022 LT-LEDS -> long-horizon low-carbon development strategy",
    ], [FACTS[0][0], FACTS[4][0], FACTS[6][0], FACTS[9][0]]),
    panel("Original mission map", "hierarchy", [
        "MITIGATION-HEAVY -> solar and enhanced energy efficiency",
        "ADAPTATION-HEAVY -> water, Himalaya and agriculture",
        "CROSS-CUTTING -> habitat, Green India and strategic knowledge",
        "CO-BENEFITS -> development, resilience and environmental quality",
        "COUNT RULE -> eight original missions in the 2008 architecture",
    ], [FACTS[1][0], FACTS[2][0]]),
    panel("Centre-state implementation rail", "process-flow", [
        "NAPCC MISSION -> national direction",
        "MINISTRY OR AGENCY -> programme and guidance",
        "SAPCC -> state-context translation",
        "BUDGET AND EXECUTION -> implementation evidence",
        "MONITORING AND OUTCOME -> separate verification stage",
    ], [FACTS[3][0], FACTS[14][0]]),
    panel("Panchamrit five-part board", "comparison-table", [
        "500 GW -> non-fossil capacity by 2030",
        "50 PERCENT -> energy requirements from renewables by 2030",
        "ONE BILLION TONNES -> projected carbon-emissions reduction by 2030",
        "45 PERCENT -> emissions-intensity reduction from 2005 by 2030",
        "2070 -> announced net-zero destination",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("Target-type classifier", "comparison-table", [
        "CAPACITY -> installed power quantity",
        "SHARE -> renewable fraction of energy requirements",
        "PROJECTED REDUCTION -> counterfactual-dependent emissions quantity",
        "INTENSITY -> emissions per unit of GDP",
        "NET ZERO -> economy-wide net balance with defined boundary",
    ], [FACTS[5][0], FACTS[12][0], FACTS[15][0]]),
    panel("Pledge-to-NDC firewall", "decision-tree", [
        "COP26 SPEECH -> announced Panchamrit",
        "OFFICIAL NDC DOCUMENT -> communicated international contribution",
        "2022 QUANTIFIED TERMS -> intensity and non-fossil capacity",
        "FOREST SINK -> continuing NDC objective, not Panchamrit item six",
        "RULE -> no automatic one-to-one conversion of every phrase",
    ], [FACTS[6][0], FACTS[7][0], FACTS[8][0]]),
    panel("LT-LEDS pathway map", "layered-rail", [
        "ELECTRICITY -> lower-carbon supply and system transition",
        "TRANSPORT AND CITIES -> integrated mobility and urban efficiency",
        "INDUSTRY -> lower-emission growth and technology pathways",
        "REMOVALS AND LAND -> carbon dioxide removal and vegetative cover",
        "FINANCE AND ECONOMY -> enabling transition conditions",
    ], [FACTS[9][0], FACTS[10][0], FACTS[18][0]]),
    panel("Net-zero status ladder", "hierarchy", [
        "ANNOUNCED YEAR -> political long-term destination",
        "LT-LEDS -> strategic pathways",
        "SECTOR POLICY -> programmes and regulation",
        "MEASURED TRAJECTORY -> source-dated emissions and removals",
        "NET RESULT -> defined economy-wide balance, not one milestone",
    ], [FACTS[11][0], FACTS[15][0]]),
    panel("Climate-accounting matrix", "comparison-table", [
        "ABSOLUTE EMISSIONS -> total flow",
        "EMISSIONS INTENSITY -> flow per unit of GDP",
        "GROSS REMOVALS -> sink uptake before netting",
        "NET EMISSIONS -> emissions minus removals within boundary",
        "BASELINE AND YEAR -> mandatory for comparison",
    ], [FACTS[12][0], FACTS[15][0]]),
    panel("Energy-denominator firewall", "comparison-table", [
        "INSTALLED CAPACITY -> rated power-system capacity",
        "ELECTRICITY GENERATION -> energy actually produced",
        "NON-FOSSIL -> source classification broader than renewables",
        "TOTAL ENERGY REQUIREMENTS -> wider denominator than electricity",
        "NO RELABELLING -> each metric needs its own source and date",
    ], [FACTS[13][0], FACTS[14][0]]),
    panel("Reporting-instrument matrix", "comparison-table", [
        "NDC -> forward nationally determined contribution",
        "LT-LEDS -> long-term strategic pathway",
        "BUR -> backward-looking inventory and progress reporting",
        "TARGET -> intended result",
        "ACHIEVEMENT -> verified result on the same metric",
    ], [FACTS[14][0], FACTS[16][0]]),
    panel("India climate answer spine", "answer-spine", [
        "MAP -> NAPCC, SAPCC, Panchamrit, NDC and LT-LEDS",
        "CLASSIFY -> mitigation, adaptation and target type",
        "DISTINGUISH -> pledge, communication, strategy and report",
        "MEASURE -> baseline, denominator, gross, net and as-on date",
        "EVALUATE -> equity, co-benefits, interdependency and delivery",
    ], [FACTS[17][0], FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2025", "GS-III",
        "Review India's Paris commitments, COP26 strengthening and the 2022 updated NDC.",
        "Verified routed Mains demand; treaty mechanics are cross-owned by Topic 19.",
        [0, 4, 5, 6, 7, 8, 9, 13, 14],
    ),
]

TOPIC_20 = common.topic(
    20,
    "India Climate Policy NAPCC Panchamrit LTLEDS",
    "20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-20_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Explain NAPCC's original mission-based architecture.", [0, 1, 2, 3]),
        (10, "Classify the five Panchamrit elements by target type.", [4, 5, 12, 13, 15]),
        (15, "Distinguish Panchamrit, the 2022 updated NDC and the forest-sink objective.", [4, 5, 6, 7, 8]),
        (15, "Explain the purpose and sectoral structure of India's LT-LEDS.", [9, 10, 11, 18]),
        (20, "Evaluate India's climate-policy architecture from mission to long-term pathway.", [0, 2, 3, 4, 6, 9, 10, 17, 18]),
        (20, "Build an evidence-disciplined review of India's targets and achievements.", [5, 6, 7, 8, 12, 13, 14, 15, 16, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "National Action Plan on Climate Change", "2008",
        "eight national missions", "State Action Plans on Climate Change",
        "Panchamrit", "500 GW", "50 percent of energy requirements",
        "one-billion-tonne", "45 percent emissions-intensity",
        "2005", "2030", "net zero by 2070", "2022 updated NDC",
        "cumulative installed electric-power capacity", "forest-and-tree-cover",
        "Long-Term Low-Carbon Development Strategy", "LT-LEDS",
        "emissions intensity", "absolute emissions", "installed capacity",
        "generation", "total energy requirements", "target", "achievement",
        "gross emissions", "gross removals", "net emissions",
        "Biennial Update Report", "CBDR-RC", "co-benefits",
    ],
    (
        "Audited ledgers route the verified 2025 GS-III review of India's Paris "
        "commitments, COP26 announcement and updated NDC, and a 2026 objective "
        "demand distinguishing LT-LEDS, BUR reporting, net-zero pathway and "
        "resilience. Provisional or unavailable objective keys are not inferred."
    ),
    PYQ_SOLUTIONS,
    INDIA_CLIMATE_LIVE_SOURCE_ATTEMPTS,
    (
        "MoEFCC returned only a NAPCC title and its dashboard failed at transport "
        "level. Official UNFCCC NDC and LT-LEDS PDFs were raw bytes, PIB returned "
        "403, and official-registry search results conflicted on post-2022 NDC "
        "status. The package therefore asserts no new NDC, current mission count, "
        "capacity, generation, emissions, sink, finance or achievement figure."
    ),
    extra=[
        "basic/12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
        "basic/17_Climate-Change-Science-Greenhouse-Effect.md",
        "basic/19_UNFCCC-COP-Kyoto-Paris-Agreement.md",
        "basic/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md",
        "basic/25_Renewable-Energy-and-Green-Hydrogen.md",
        "advanced/12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
        "advanced/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md",
        "advanced/25_Renewable-Energy-and-Green-Hydrogen.md",
    ],
    pyq_audit_heading="AUDITED INDIA CLIMATE-POLICY, NDC, LT-LEDS AND REPORTING PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "NAPCC, PANCHAMRIT, NDC, LT-LEDS AND REPORTING-INSTRUMENT MAP",
        "TARGET-TYPE, DENOMINATOR, GROSS-NET, STATUS AND ACHIEVEMENT TRAPS",
        "INDIA CLIMATE-POLICY ANSWER SPINE",
        "LIVE NDC, MISSION, CAPACITY, GENERATION, SINK AND DELIVERY EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "MAP NAPCC, SAPCC, PANCHAMRIT, UPDATED NDC AND LT-LEDS",
        "LIST THE ORIGINAL EIGHT MISSIONS AND FIVE PANCHAMRIT ELEMENTS EXACTLY",
        "SEPARATE POLITICAL ANNOUNCEMENT FROM COMMUNICATED NDC TERMS",
        "CLASSIFY INTENSITY, CAPACITY, SHARE, PROJECTED REDUCTION AND NET ZERO",
        "DISTINGUISH INSTALLED CAPACITY, GENERATION AND TOTAL ENERGY REQUIREMENTS",
        "DISTINGUISH NDC, LT-LEDS, BUR, TARGET AND ACHIEVEMENT",
        "CONCLUDE WITH CO-BENEFITS, EQUITY, INTERDEPENDENCY AND DATED EVIDENCE",
    ],
)
