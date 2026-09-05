"""Authored data for Environment and Ecology learner-v2 Topic 11."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import FRA_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Four forest vocabularies", "Forest type is an ecological classification, Reserved or Protected Forest is a legal category, recorded forest area is a government-record category, and forest or tree cover is a canopy measurement; none can substitute automatically for another."),
    ("Ecological type drivers", "Champion-Seth-style forest types organise vegetation mainly through climate, rainfall and altitude, while soils, fire, grazing and land-use history can modify local expression."),
    ("Wet to dry sequence", "Tropical wet evergreen, semi-evergreen, moist deciduous, dry deciduous and thorn formations represent different ecological conditions; they are not canopy-density grades or legal protection ranks."),
    ("Montane zonation", "Montane, sub-alpine and alpine vegetation reflect altitude and exposure in mountain systems; an elevational belt must not be presented as one nationwide legal forest category."),
    ("Legal forest categories", "Reserved Forest, Protected Forest and Village Forest arise through the Indian Forest Act framework, while unclassed forest is a record or administration expression; legal consequence must be checked from the applicable notification and law."),
    ("Reserved-Protected reversal", "The owner preserves the classic exam distinction: a Reserved Forest uses a more restrictive permission logic, whereas a Protected Forest does not create the same presumption; neither label is an ecological forest type."),
    ("Forest-cover measurement", "FSI forest cover uses remote-sensing canopy criteria across ownership and legal status; plantations or orchards can enter the cover measure, so canopy presence is not proof of natural-forest quality or legal forest status."),
    ("Recorded forest area", "Recorded forest area refers to land entered as forest in government records and may include different legal classes; degraded recorded forest can have little measured canopy, while measured cover can occur outside recorded forest."),
    ("Tree-cover boundary", "Tree cover is measured separately from forest cover under the applicable FSI methodology; combining them can describe canopy extent but cannot establish forest type, tenure or rights."),
    ("FRA purpose", "The Forest Rights Act, 2006 is a rights-recognition and historical-injustice statute for forest-dwelling Scheduled Tribes and eligible Other Traditional Forest Dwellers, not a blanket transfer of every forest to private ownership."),
    ("Eligibility and cutoff", "The owner records occupation before 13 December 2005 and an additional three-generation or 75-year residence-and-dependence test for Other Traditional Forest Dwellers; Scheduled Tribe claimants do not face that OTFD generational test."),
    ("Individual forest right", "An individual forest right concerns pre-existing habitation or self-cultivation under actual occupation, subject to the Act's conditions and statutory ceiling; recognition does not authorise fresh encroachment."),
    ("Community rights", "Community rights include specified customary uses such as grazing, access to water bodies and ownership, access, use or disposal of minor forest produce; they are not identical to individual cultivation rights."),
    ("Community forest resource right", "A community forest resource right is the community-level right to protect, regenerate, conserve and manage a traditionally used community forest resource; it is distinct from both IFR and the wider set of community-use rights."),
    ("Habitat and special rights", "The Act also recognises habitat rights for Particularly Vulnerable Tribal Groups and pre-agricultural communities and traditional seasonal resource access where the statutory conditions are met."),
    ("Recognition procedure", "The claims route begins with the Gram Sabha and proceeds through Sub-Divisional and District Level Committees; filing or recommendation is not the same as final recognition, and recognition is not assumed without the completed procedure."),
    ("Section 4(5) safeguard", "The owner records section 4(5) as barring eviction or removal of eligible forest dwellers until recognition and verification are complete; it is a sequencing safeguard, not an automatic finding that every claim succeeds."),
    ("Section 3(2) facilities", "The owner records a conditional route for specified community development facilities on forest land through section 3(2), including area, tree-felling and Gram Sabha recommendation limits; it is not a general exemption for any project."),
    ("Rights and conservation", "FRA assigns conservation responsibilities and CFR can support stewardship, but title recognition alone does not prove an ecological outcome; capacity, tenure security, monitoring and coordination still matter."),
    ("Audited PYQ boundary", "Audited ledgers route forest type, forest cover, FRA, bamboo, critical wildlife habitat, Miyawaki and forest-resource demands to Topic 11; objective keys are not inferred, while the 2020 GS-I Mains demand receives a source-bounded model route."),
]

TRAPS = [
    "Do not equate ecological forest type with legal forest category.",
    "Do not equate forest cover with recorded forest area.",
    "Do not treat tree cover as proof of a forest right or natural forest.",
    "Do not classify evergreen, deciduous and thorn as canopy-density classes.",
    "Do not treat Reserved and Protected Forest permission logic as identical.",
    "Do not say FRA applies only to Scheduled Tribes.",
    "Do not apply the OTFD three-generation test to Scheduled Tribe claimants.",
    "Do not treat IFR as permission for fresh occupation.",
    "Do not merge community rights and community forest resource rights.",
    "Do not treat a Gram Sabha resolution as the final title.",
    "Do not treat section 4(5) as automatic approval of every claim.",
    "Do not convert section 3(2) into a general diversion exemption.",
    "Do not say rights recognition automatically proves conservation improvement.",
    "Do not use a forest-cover figure to establish forest quality or tenure.",
    "Do not infer an objective PYQ key from the routing ledger.",
]

SESSION_TITLES = [
    "Four forest vocabularies and ecological drivers",
    "Wet evergreen to thorn sequence",
    "Montane sub-alpine and alpine zonation",
    "Reserved Protected Village and unclassed forests",
    "Reserved versus Protected permission logic",
    "Forest cover and recorded forest area",
    "Tree cover boundary",
    "FRA historical-injustice purpose",
    "Scheduled Tribe OTFD cutoff and eligibility",
    "Individual forest rights",
    "Community rights and community forest resource rights",
    "Habitat and special rights",
    "Recognition procedure and section 4(5)",
    "Section 3(2) community facilities",
    "Rights conservation and audited PYQ boundary",
]

ANSWER_ROUTES = [
    "Open with the four vocabularies, then qualify ecological type with local drivers.",
    "Use the moisture sequence without turning it into a protection rank.",
    "Map altitude belts without making one legal category.",
    "Name each legal or record class and verify its notification source.",
    "Use the classic reversal only within the Indian Forest Act context.",
    "Contrast remotely sensed canopy with the government forest record.",
    "Keep tree-cover extent separate from type, rights and ecological quality.",
    "Frame FRA as recognition of historical rights, not blanket ownership transfer.",
    "State the cutoff and apply the additional test only to OTFDs.",
    "Tie IFR to actual prior occupation and statutory conditions.",
    "Separate customary community uses from the CFR management right.",
    "Identify habitat and seasonal-resource rights without extending eligibility.",
    "Trace Gram Sabha to DLC and retain the no-eviction sequencing safeguard.",
    "Apply the facility route only within its statutory conditions.",
    "Close with conditional stewardship and the answer-free objective PYQ audit.",
]

PANELS = [
    panel("Four-vocabulary firewall", "comparison-table", [
        "FOREST TYPE -> ecology, climate and vegetation",
        "LEGAL CATEGORY -> Reserved, Protected or Village Forest",
        "RECORDED FOREST AREA -> government forest record",
        "FOREST OR TREE COVER -> canopy measurement",
        "RULE -> never use one vocabulary as automatic proof of another",
    ], [FACTS[0][0], FACTS[4][0], FACTS[6][0], FACTS[7][0], FACTS[8][0]]),
    panel("Moisture-gradient map", "process-flow", [
        "VERY WET -> tropical wet evergreen",
        "TRANSITION -> semi-evergreen",
        "SEASONAL MOISTURE -> moist deciduous",
        "DRIER SEASONAL CLIMATE -> dry deciduous",
        "ARIDITY -> thorn and drought-adapted vegetation",
    ], [FACTS[1][0], FACTS[2][0]]),
    panel("Mountain-zonation rail", "route-map", [
        "LOWER SLOPES -> climate and aspect condition forest",
        "MONTANE BELTS -> changing temperature and moisture",
        "SUB-ALPINE -> upper tree-limit transition",
        "ALPINE -> vegetation above forest limit",
        "CAUTION -> local exposure and land use modify the ideal sequence",
    ], [FACTS[1][0], FACTS[3][0]]),
    panel("Legal-category matrix", "comparison-table", [
        "RESERVED FOREST -> restrictive permission presumption",
        "PROTECTED FOREST -> different permission and prohibition structure",
        "VILLAGE FOREST -> statutory management category",
        "UNCLASSED FOREST -> verify record and applicable legal basis",
        "NONE -> an ecological type or canopy-density class",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("Cover-record divergence", "comparison-table", [
        "RECORDED FOREST WITH LOW CANOPY -> legal record can remain",
        "PLANTATION OR ORCHARD WITH CANOPY -> may enter cover measurement",
        "FOREST COVER -> remote-sensing criterion",
        "TREE COVER -> separate measurement category",
        "RESULT -> area figures answer different questions",
    ], [FACTS[6][0], FACTS[7][0], FACTS[8][0]]),
    panel("FRA purpose gate", "layered-rail", [
        "PAST EXCLUSION -> historical injustice",
        "ELIGIBLE FOREST DWELLER -> statutory claimant category",
        "RIGHT CLAIM -> evidence and procedure",
        "RECOGNITION -> defined right and title",
        "NO BLANKET TRANSFER -> State governance framework continues",
    ], [FACTS[9][0], FACTS[15][0]]),
    panel("Eligibility decision tree", "decision-tree", [
        "CLAIMANT -> forest-dwelling Scheduled Tribe or OTFD",
        "OCCUPATION -> before 13 December 2005",
        "OTFD ONLY -> three generations or 75 years plus dependence",
        "EVIDENCE -> apply statutory and Rules-based forms",
        "PROCEDURE -> eligibility claim still requires verification",
    ], [FACTS[10][0], FACTS[15][0]]),
    panel("Rights matrix", "comparison-table", [
        "IFR -> prior habitation or self-cultivation under actual occupation",
        "COMMUNITY RIGHTS -> customary access, grazing, water and MFP",
        "CFR RIGHT -> protect, regenerate, conserve and manage resource",
        "HABITAT RIGHT -> PVTG or pre-agricultural community route",
        "RULE -> right categories have different holders and content",
    ], [FACTS[11][0], FACTS[12][0], FACTS[13][0], FACTS[14][0]]),
    panel("Recognition procedure", "process-flow", [
        "GRAM SABHA -> initiate, receive and verify claims",
        "SDLC -> scrutinise and hear the intermediate claim stage",
        "DLC -> final district-level decision",
        "TITLE OR REASONED REJECTION -> outcome after procedure",
        "NO ASSUMPTION -> filing or recommendation is not conferment",
    ], [FACTS[15][0]]),
    panel("Safeguard and facility gate", "decision-gate", [
        "SECTION 4(5) -> no eviction before recognition process completes",
        "LIMIT -> safeguard does not automatically approve every claim",
        "SECTION 3(2) -> specified community facilities only",
        "CONDITIONS -> retain area, tree and Gram Sabha limits from the owner",
        "NO EXTENSION -> not a general non-forest-use exemption",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("Rights-conservation bridge", "process-flow", [
        "RECOGNISED TENURE -> stronger stewardship incentive may follow",
        "CFR INSTITUTION -> community management authority",
        "SUPPORT -> ecological, technical and livelihood capacity",
        "MONITOR -> forest condition and distributional outcomes",
        "QUALIFY -> title is an input, not automatic ecological success",
    ], [FACTS[13][0], FACTS[18][0]]),
    panel("PYQ answer spine", "answer-spine", [
        "CLASSIFY -> type, legal category, record, cover or right",
        "DEFINE -> claimant, right holder and procedure",
        "TRACE -> Gram Sabha, SDLC and DLC",
        "APPLY -> bamboo, habitat, forest type, Miyawaki or resource demand",
        "QUALIFY -> dated data and objective keys remain source-bounded",
    ], [FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS,
        "2020",
        "GS-I Q17 · 15 marks · 250 words",
        "Examine the status of forest resources in India and their impact on climate change.",
        "Official-paper demand routed to Topic 11; this is a repository-authored model route, not an official UPSC solution.",
        [0, 1, 6, 7, 8, 18],
    )
]

TOPIC_11 = common.topic(
    11,
    "Forest Types and Forest Rights Act",
    "11_Forest-Types-and-Forest-Rights-Act",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-11_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish forest type, legal forest category, recorded forest area, forest cover and tree cover.", [0, 1, 4, 6, 7, 8]),
        (10, "Explain the FRA eligibility and recognition route for Scheduled Tribes and OTFDs.", [9, 10, 15, 16]),
        (15, "Distinguish individual, community, community forest resource and habitat rights.", [11, 12, 13, 14]),
        (15, "Assess how FRA procedure can reconcile tenure security and conservation.", [9, 15, 16, 18]),
        (20, "Analyse the category errors that weaken Indian forest-governance debates.", [0, 2, 3, 4, 6, 7, 8]),
        (20, "Evaluate FRA as a rights-restoration statute with conservation implications and implementation limits.", [9, 10, 11, 12, 13, 15, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "forest type", "legal forest category", "recorded forest area",
        "forest cover", "tree cover", "Reserved Forest", "Protected Forest",
        "13 December 2005", "Other Traditional Forest Dwellers",
        "Individual Forest Rights", "Community Rights",
        "Community Forest Resource", "habitat rights", "Gram Sabha",
        "Sub-Divisional Level Committee", "District Level Committee",
        "section 4(5)", "section 3(2)", "recognition is not assumed",
    ],
    (
        "Audited ledgers route seven Topic 11 demands: 2018 FRA critical "
        "wildlife habitat and Baiga rights; 2019 forest-cover ranking and bamboo "
        "as minor forest produce; 2020 GS-I forest resources; 2022 Miyawaki; "
        "2023 deciduous trees; and 2024 native-tree identification. Objective "
        "keys are not inferred. The direct 2020 Mains demand receives a model route."
    ),
    PYQ_SOLUTIONS,
    FRA_LIVE_SOURCE_ATTEMPTS,
    (
        "The Ministry of Tribal Affairs FRA page was substantively retrieved "
        "for the historical-injustice purpose, right families, Gram Sabha role "
        "and conservation responsibilities. Its official Act-and-Rules PDF was "
        "raw bytes and was not text-mined. No current claims total, title area, "
        "forest-cover figure or ecological outcome was imported."
    ),
    extra=[
        "basic/03_Ecological-Succession-and-Biomes.md",
        "basic/06_Protected-Area-Network-India.md",
        "basic/12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
        "advanced/06_Protected-Area-Network-India.md",
        "advanced/12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
    ],
    pyq_audit_heading="AUDITED FOREST-TYPE, COVER AND FRA PYQ OWNERSHIP",
    register_headings=(
        "FOREST TYPE, LEGAL CATEGORY, RECORD, COVER AND TREE MAP",
        "ELIGIBILITY, RIGHTS, PROCEDURE AND CONSERVATION TRAPS",
        "FOREST-RIGHTS ANSWER SPINE",
        "LIVE FRA, FSI, TITLE, COVER AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "CLASSIFY THE QUESTION: ECOLOGY, LAW, RECORD, CANOPY OR RIGHTS",
        "MAP CLIMATE AND ALTITUDE ONLY FOR ECOLOGICAL FOREST TYPE",
        "NAME RESERVED, PROTECTED OR OTHER LEGAL-RECORD STATUS PRECISELY",
        "APPLY FRA CLAIMANT, CUTOFF AND RIGHT CATEGORY",
        "TRACE GRAM SABHA TO SDLC TO DLC WITHOUT ASSUMING CONFERMENT",
        "ADD SECTION 4(5), SECTION 3(2) OR CFR ONLY WHERE RELEVANT",
        "CONCLUDE WITH TENURE SECURITY PLUS ECOLOGICAL MONITORING",
    ],
)
