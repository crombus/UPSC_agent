"""Authored data for Environment and Ecology learner-v2 Topic 24."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import panel


FACTS = [
    ("Coastal-system boundary", "A coast is a coupled land-sea system shaped by waves, tides, currents, sediment, freshwater, ecosystems and human use; an administrative coastal zone is not the same thing as the ecological system."),
    ("Ecosystem-service portfolio", "Mangroves, seagrasses, salt marshes, dunes, reefs, estuaries and mudflats can support habitat, fisheries, sediment processes, carbon storage and hazard moderation; service magnitude is site-specific."),
    ("Mangrove boundary", "Mangroves are intertidal salt-tolerant woody ecosystems with ecological and livelihood functions; a plantation area, legal category or mapped patch is not automatically equivalent to a functioning mangrove system."),
    ("Seagrass-marsh boundary", "Seagrass meadows are submerged flowering-plant ecosystems and salt marshes are vegetated intertidal wetlands; neither should be merged with mangrove forest or coral reef."),
    ("Coral stress distinction", "Thermal bleaching involves stress-driven loss of coral symbionts, while ocean acidification alters carbonate chemistry and calcification conditions; they are distinct, compounding processes."),
    ("Sediment and erosion chain", "Coastal erosion or accretion reflects sediment supply, waves, currents, storms, river regulation and structures; a shoreline shift cannot be attributed to one driver without site-specific evidence."),
    ("CRZ legal identity", "The Coastal Regulation Zone is an administrative regulatory framework under the Environment (Protection) Act, not an ecosystem type, protected-area designation or maritime entitlement."),
    ("Notification-vintage boundary", "CRZ claims must identify the governing notification and applicable amendment or Coastal Zone Management Plan; rules from different vintages cannot be silently combined."),
    ("CRZ category boundary", "CRZ-I, II, III and IV organise different ecological, developed, relatively undisturbed and water-area contexts, with subcategories and activity rules that require the applicable notification text."),
    ("HTL-LTL boundary", "High Tide Line, Low Tide Line, hazard line, setback and mapped CRZ boundary perform different functions; a generic distance from the shore cannot replace the approved map and category rule."),
    ("CZMP evidence boundary", "A Coastal Zone Management Plan maps categories and boundaries for regulatory administration; map approval does not itself grant project clearance or prove ecological condition."),
    ("Classification-clearance distinction", "CRZ classification determines the applicable regulatory regime, while project appraisal or clearance is a separate decision based on project type, location and procedure."),
    ("ICZM-clearance distinction", "Integrated Coastal Zone Management coordinates ecosystems, hazards, livelihoods and development across a coastal system; it is broader than approving or rejecting one project."),
    ("Layered legal geography", "CRZ, protected-area law, Ramsar designation, forest law, port limits, maritime zones and local tenure can overlap, but each has a different authority, boundary and legal consequence."),
    ("Seawater-intrusion chain", "Coastal-aquifer salinisation can occur when groundwater extraction or reduced recharge lowers freshwater head, allowing saline water to move landward or upward; sea-level and local engineering can compound the process."),
    ("Intrusion response hierarchy", "Responses combine demand management, recharge protection, pumping control, monitoring and site-specific hydraulic barriers; desalination treats supplied water but does not by itself restore aquifer balance."),
    ("Blue-economy definition", "A blue economy links ocean-based livelihoods and production with ecosystem health, equity and long-term resource stewardship; economic activity at sea is an opportunity, not proof of sustainability."),
    ("Sector-outcome boundary", "Fisheries, aquaculture, ports, shipping, tourism, offshore energy, biotechnology and seabed activity have different pressures and governance needs; sector growth is not automatically a sustainable outcome."),
    ("Maritime-zone boundary", "CRZ regulates specified coastal land and water contexts, the territorial sea and exclusive economic zone arise from maritime law, and areas beyond national jurisdiction have a separate international governance layer."),
    ("Current evidence boundary", "Coastline length, mangrove or coral extent, fish stocks, blue-carbon rates, CRZ category or clearance status, Blue Economy output and project outcomes require dated official maps, surveys, notifications or decisions."),
]

TRAPS = [
    "Do not merge a coastal ecosystem with an administrative CRZ.",
    "Do not assign one service value to all coastal habitats.",
    "Do not equate plantation or mapped area with functioning mangrove ecology.",
    "Do not merge seagrass, salt marsh, mangrove and coral reef.",
    "Do not merge coral bleaching with ocean acidification.",
    "Do not attribute every shoreline change to sea-level rise.",
    "Do not call CRZ a protected-area or maritime-zone designation.",
    "Do not combine CRZ rules from different notification vintages.",
    "Do not state category rules without the applicable subcategory and text.",
    "Do not replace approved coastal mapping with a generic distance.",
    "Do not treat CZMP approval as project clearance.",
    "Do not merge classification with appraisal or clearance.",
    "Do not reduce ICZM to project clearance.",
    "Do not merge overlapping legal designations.",
    "Do not make sea-level rise the only cause of seawater intrusion.",
    "Do not call desalination aquifer restoration.",
    "Do not define Blue Economy as unrestricted extraction.",
    "Do not equate sector growth with sustainability.",
    "Do not merge CRZ, territorial sea, EEZ and high seas.",
    "Do not invent coastal, ecosystem, fisheries, CRZ or output values.",
]

SESSION_TITLES = [
    "Coupled coastal system and ecosystem services",
    "Mangrove ecological boundary",
    "Seagrass and salt-marsh boundary",
    "Coral bleaching and ocean acidification",
    "Sediment budget erosion and accretion",
    "CRZ legal identity and notification vintage",
    "CRZ category and subcategory logic",
    "HTL LTL hazard line setback and mapped boundary",
    "Coastal Zone Management Plan purpose",
    "CRZ classification and project clearance",
    "ICZM and overlapping coastal legal geographies",
    "Seawater intrusion causes and hydraulic mechanism",
    "Aquifer demand recharge and barrier responses",
    "Blue Economy sectors equity and ecosystem outcomes",
    "Maritime zones BBNJ and current evidence audit",
]

ANSWER_ROUTES = [
    "Define the ecological coast before introducing its administrative regulation.",
    "Compare habitats by structure, location and services without importing universal values.",
    "Separate thermal symbiont loss from carbonate-chemistry stress.",
    "Trace sediment sources, transport, structures and shoreline response.",
    "Name the CRZ legal instrument and notification vintage.",
    "Identify category and subcategory before stating any activity rule.",
    "Use approved mapping terms rather than a generic shoreline distance.",
    "Explain CZMP as regulatory mapping, not a project approval.",
    "Separate classification, appraisal, clearance and compliance monitoring.",
    "Use ICZM for cumulative ecological, hazard, livelihood and development coordination.",
    "List overlapping designations while preserving each authority and consequence.",
    "Lead seawater intrusion with freshwater-head imbalance and compounding factors.",
    "Organise remedies into demand, recharge, pumping, monitoring and barriers.",
    "Evaluate each ocean sector against ecology, livelihoods, equity and cumulative pressure.",
    "Close with maritime jurisdiction and dated official maps, surveys and decisions.",
]

PANELS = [
    panel("Coastal system map", "causal-chain", [
        "RIVER AND SEDIMENT -> material reaches the coast",
        "WAVES TIDES CURRENTS -> transport and reshape shoreline",
        "ECOSYSTEMS -> trap sediment buffer hazards support habitat",
        "HUMAN USE -> extraction structures ports settlements and livelihoods",
        "OUTCOME -> coupled land-sea response, not one isolated driver",
    ], [FACTS[0][0], FACTS[5][0]]),
    panel("Coastal ecosystem matrix", "comparison-table", [
        "MANGROVE -> intertidal woody vegetation",
        "SEAGRASS -> submerged flowering-plant meadow",
        "SALT MARSH -> vegetated intertidal wetland",
        "CORAL REEF -> biogenic marine structure",
        "DUNE MUDFLAT ESTUARY -> distinct sediment and habitat systems",
    ], [FACTS[1][0], FACTS[2][0], FACTS[3][0]]),
    panel("Coral dual-stress diagram", "comparison-table", [
        "THERMAL STRESS -> symbiont loss and bleaching",
        "ACIDIFICATION -> carbonate chemistry changes",
        "LOCAL POLLUTION -> compounding stress",
        "RECOVERY -> event severity and local condition matter",
        "RULE -> bleaching and acidification are not synonyms",
    ], [FACTS[4][0]]),
    panel("Sediment-budget rail", "process-flow", [
        "SOURCE -> rivers cliffs reefs and alongshore supply",
        "TRANSPORT -> waves currents and tides",
        "INTERRUPTION -> dams mining ports and coastal structures",
        "EVENT -> storm and surge redistribution",
        "SHORELINE -> erosion accretion or reorientation",
    ], [FACTS[5][0]]),
    panel("CRZ legal hierarchy", "hierarchy", [
        "ENVIRONMENT PROTECTION ACT -> enabling legal base",
        "CRZ NOTIFICATION -> national regulatory framework",
        "AMENDMENT -> changes specified provisions",
        "CZMP -> mapped state or UT implementation layer",
        "PROJECT DECISION -> separate appraisal and clearance",
    ], [FACTS[6][0], FACTS[7][0], FACTS[10][0], FACTS[11][0]]),
    panel("CRZ category compass", "comparison-table", [
        "CRZ I -> ecologically sensitive and intertidal contexts",
        "CRZ II -> developed urban coastal context",
        "CRZ III -> relatively undisturbed rural context",
        "CRZ IV -> specified water-area context",
        "SUBCATEGORY RULE -> official notification controls detail",
    ], [FACTS[8][0]]),
    panel("Coastal line firewall", "comparison-table", [
        "HTL -> mapped tidal reference",
        "LTL -> mapped lower tidal reference",
        "HAZARD LINE -> hazard-information function",
        "SETBACK OR NDZ -> rule-defined regulatory function",
        "APPROVED MAP -> category boundary evidence",
    ], [FACTS[9][0], FACTS[10][0]]),
    panel("CZMP-to-clearance sequence", "process-flow", [
        "CZMP -> category and boundary map",
        "PROJECT LOCATION -> overlaid on approved plan",
        "APPLICABLE RULE -> category subcategory and activity",
        "APPRAISAL OR CLEARANCE -> project-specific decision",
        "COMPLIANCE -> construction and operation monitoring",
    ], [FACTS[10][0], FACTS[11][0]]),
    panel("ICZM coordination wheel", "layered-rail", [
        "ECOSYSTEMS -> cumulative ecological condition",
        "HAZARDS -> erosion surge flooding and intrusion",
        "LIVELIHOODS -> fishing access tenure and settlements",
        "DEVELOPMENT -> ports tourism energy and infrastructure",
        "COORDINATION -> wider than one project clearance",
    ], [FACTS[12][0], FACTS[13][0]]),
    panel("Coastal aquifer mechanism", "causal-chain", [
        "OVER EXTRACTION OR LOWER RECHARGE -> freshwater head falls",
        "HYDRAULIC GRADIENT CHANGES -> saline interface moves",
        "SEA LEVEL OR ENGINEERING -> possible compounding pressure",
        "SALINISATION -> wells soils and supply affected",
        "RESPONSE -> demand recharge pumping monitoring and barriers",
    ], [FACTS[14][0], FACTS[15][0]]),
    panel("Blue Economy sustainability test", "decision-tree", [
        "SECTOR OPPORTUNITY -> fisheries shipping tourism energy or science",
        "ECOSYSTEM PRESSURE -> habitat pollution extraction and carbon",
        "LIVELIHOOD AND EQUITY -> access benefit and displacement",
        "CUMULATIVE GOVERNANCE -> thresholds monitoring and enforcement",
        "VERDICT -> growth is not sustainability without outcomes",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("Coastal answer spine", "answer-spine", [
        "DEFINE -> ecological coast and administrative CRZ separately",
        "MAP -> habitat sediment hazard aquifer and livelihood systems",
        "PLACE -> notification CZMP category clearance ICZM and maritime zone",
        "EVALUATE -> sector opportunity against ecosystem and equity outcome",
        "VERIFY -> official map survey notification decision and date",
    ], [FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2019", "GS-I",
        "Discuss causes of mangrove depletion and explain their role in maintaining coastal ecology.",
        "Verified routed Mains demand; no current mangrove extent is inferred.",
        [0, 1, 2, 5, 13, 19],
    ),
    common.make_pyq_solution(
        FACTS, "2025", "GS-III",
        "Explain causes of seawater intrusion in coastal aquifers and remedial measures.",
        "Verified routed Mains demand; response is organised by hydraulic mechanism.",
        [14, 15, 12, 19],
    ),
]

LIVE_SOURCES = [
    "https://moef.gov.in/crz-notifications — attempted 2026-09-03; the official path returned HTTP 404, so no notification amendment, category, boundary or clearance claim was imported.",
    "https://moef.gov.in/coastal-regulation-zone — attempted 2026-09-03; the official path returned HTTP 404, so current CRZ procedure and CZMP status remain unasserted.",
    "https://moes.gov.in/schemes/deep-ocean-mission — attempted 2026-09-03; the official route returned HTTP 403, so no mission component, deployment milestone or project outcome was imported.",
    "https://www.un.org/bbnjagreement/en — attempted 2026-09-03; substantive official text confirmed the Agreement's four issue areas and that it entered into force on 17 January 2026; no India-specific status was inferred.",
    "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted 2026-09-03; no topic-specific coastline, ecosystem, fisheries, CRZ or Blue Economy value was imported.",
]

TOPIC_24 = common.topic(
    24,
    "Coastal and Marine Ecology CRZ Blue Economy",
    "24_Coastal-and-Marine-Ecology-CRZ-Blue-Economy",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-24_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Explain the ecological structure and services of major coastal ecosystems.", [0, 1, 2, 3, 4]),
        (10, "Distinguish CRZ notification, category, CZMP and project clearance.", [6, 7, 8, 10, 11]),
        (15, "Explain coastal erosion through a sediment-budget approach.", [0, 5, 12, 19]),
        (15, "Explain seawater intrusion and an integrated response.", [14, 15, 12]),
        (20, "Evaluate CRZ and ICZM as complementary but distinct governance instruments.", [6, 7, 8, 9, 10, 11, 12, 13]),
        (20, "Assess Blue Economy opportunities against ecosystem, livelihood and jurisdictional limits.", [1, 4, 13, 16, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "coupled land-sea system", "mangroves", "seagrasses", "salt marshes",
        "coral bleaching", "ocean acidification", "sediment", "erosion",
        "Coastal Regulation Zone", "Environment (Protection) Act",
        "notification", "CRZ-I", "CRZ-II", "CRZ-III", "CRZ-IV",
        "High Tide Line", "Low Tide Line", "Coastal Zone Management Plan",
        "classification", "clearance", "Integrated Coastal Zone Management",
        "seawater intrusion", "freshwater head", "recharge", "Blue Economy",
        "ecosystem health", "equity", "territorial sea", "exclusive economic zone",
        "areas beyond national jurisdiction", "BBNJ Agreement",
    ],
    (
        "Audited ledgers route verified Mains demands on mangroves, coastal sand "
        "mining, erosion, oil pollution, dead zones and seawater intrusion, plus "
        "objective coastal-ecology demands. No provisional key or current value is inferred."
    ),
    PYQ_SOLUTIONS,
    LIVE_SOURCES,
    (
        "The UN BBNJ page supplied substantive scope and entry-into-force text. "
        "MoEFCC CRZ routes failed and the MoES route was blocked; therefore no "
        "coastline, mangrove, coral, fisheries, CRZ category or clearance status, "
        "Blue Economy output, mission milestone or project outcome is asserted."
    ),
    extra=[
        "basic/02_Biogeochemical-Cycles-and-Ecological-Pyramids.md",
        "basic/07_Biosphere-Reserves-and-Ramsar-Sites.md",
        "basic/14_Water-Pollution-and-River-Cleaning-Missions.md",
        "basic/16_Environmental-Impact-Assessment-and-NGT.md",
        "basic/17_Climate-Change-Science-Greenhouse-Effect.md",
        "advanced/07_Biosphere-Reserves-and-Ramsar-Sites.md",
        "advanced/16_Environmental-Impact-Assessment-and-NGT.md",
    ],
    pyq_audit_heading="AUDITED COASTAL ECOLOGY, CRZ, EROSION, INTRUSION AND BLUE-ECONOMY PYQ OWNERSHIP",
    register_headings=(
        "COASTAL ECOSYSTEM, CRZ, CZMP, ICZM AND MARITIME-ZONE MAP",
        "VINTAGE, CATEGORY, BOUNDARY, CLEARANCE AND SUSTAINABILITY TRAPS",
        "COASTAL AND BLUE-ECONOMY ANSWER SPINE",
        "LIVE MAP, ECOSYSTEM, FISHERIES, CRZ, OUTPUT AND PROJECT EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "DEFINE ECOLOGICAL COAST AND ADMINISTRATIVE CRZ SEPARATELY",
        "MAP HABITATS SEDIMENT CORAL STRESS AND AQUIFER MECHANISMS",
        "IDENTIFY NOTIFICATION VINTAGE CATEGORY SUBCATEGORY AND APPROVED CZMP",
        "SEPARATE CLASSIFICATION PROJECT CLEARANCE COMPLIANCE AND ICZM",
        "TRACE SEAWATER INTRUSION THROUGH FRESHWATER-HEAD IMBALANCE",
        "TEST BLUE-ECONOMY SECTORS AGAINST ECOLOGY LIVELIHOODS EQUITY AND JURISDICTION",
        "CONCLUDE WITH DATED MAP SURVEY NOTIFICATION DECISION AND OUTCOME EVIDENCE",
    ],
    allow_existing_history=True,
)
