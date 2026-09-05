"""Authored data for Environment and Ecology learner-v2 Topic 10."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import CMS_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Migratory-species test", "The CMS Convention text defines a migratory species through a significant proportion of members cyclically and predictably crossing one or more national jurisdictional boundaries; merely moving within one landscape is not enough."),
    ("Range definition", "A migratory range includes land or water inhabited, used temporarily, crossed or overflown on the normal migration route; breeding and wintering sites are not the only relevant places."),
    ("Range State definition", "A Range State exercises jurisdiction over any part of that range, with the Convention text also addressing relevant flag-vessel situations; it is not limited to the breeding State or final destination."),
    ("Weakest-link logic", "Because the life cycle spans route segments and jurisdictions, loss at one breeding, stopover, wintering or passage site can undermine protection elsewhere; CMS is a coordination response to that transboundary problem."),
    ("Appendix I", "Appendix I lists endangered migratory species and requires Range States to endeavour to conserve or restore important habitat, address migration obstacles and prohibit taking subject only to precise Convention exceptions."),
    ("Taking exceptions", "Appendix I exceptions for taking must fit the Convention grounds and remain precise in content and limited in space and time; an exception is not a general permission."),
    ("Appendix II", "Appendix II covers migratory species with unfavourable conservation status requiring agreements and species that would significantly benefit from international cooperation; it opens a cooperation route rather than duplicating Appendix I."),
    ("Dual listing", "The Convention expressly permits a migratory species to be listed in both Appendix I and Appendix II because strict protection and cooperative agreement serve different functions."),
    ("AGREEMENT architecture", "A CMS AGREEMENT should cover the whole range, remain open to Range States and address coordinated conservation, monitoring, information exchange, habitat networks and obstacles as applicable."),
    ("Agreement versus MOU", "A binding Agreement and a non-binding Memorandum of Understanding must be identified by the exact instrument; neither an Appendix listing nor an Action Plan proves that one of those instruments exists."),
    ("Action Plan boundary", "An Action Plan can organise conservation measures for a species or flyway, but its legal and institutional status must be read from the adopting instrument; plan adoption is not a recovery outcome."),
    ("Concerted Action boundary", "CMS Concerted Actions prioritise focused cooperative work between COPs; they do not replace Appendix status, an Agreement, an MOU or domestic legal protection."),
    ("Central Asian Flyway", "The flyway is an ecological route and cooperation geography, not itself a species, Appendix or treaty; every claim about its institution, Range States or action plan requires the dated official instrument."),
    ("COP14 initiative", "The official CMS COP14 release states that Samarkand in February 2024 adopted a Central Asian Flyway initiative including a coordinating unit in India with Indian Government financial support; it must be called an initiative, not silently upgraded to an Agreement or MOU."),
    ("Strategic plan status", "COP14 adopted the Samarkand Strategic Plan for Migratory Species 2024-2032; adoption establishes targets and direction, not proof that populations, habitats or route safety improved."),
    ("Threat classification", "Habitat loss, taking, barriers, power lines, light pollution, bycatch and other pressures must be located on the route; some are transboundary coordination failures and others are domestic implementation failures."),
    ("Amur Falcon PYQ anchor", "The provisional 2026 routed demand concerns Amur Falcon migration to Doyang Lake and community-based conservation; it is carried as an answer-free concept anchor without inferring the option key."),
    ("Amur Falcon distinction", "The Doyang or Pangti conservation example illustrates protection of a stopover or roost link through local action; it does not by itself prove protection across the species' complete migratory circuit."),
    ("CMS-CITES-Ramsar split", "CMS coordinates migratory-range conservation, CITES regulates international trade and Ramsar concerns wetland wise use and designation; one migratory bird can engage all three without merging their legal effects."),
    ("Current-listing boundary", "The package does not assert a current species Appendix, Party count, MOU signatory count or post-COP14 action-plan status unless it was substantively retrieved from the dated official source."),
]

TRAPS = [
    "Do not call every mobile or seasonally shifting animal a CMS migratory species.",
    "Do not reduce range to breeding and destination sites.",
    "Do not restrict Range State to the State where breeding occurs.",
    "Do not treat Appendix I exceptions as a general taking permission.",
    "Do not say Appendix II creates the same duty as Appendix I.",
    "Appendix I and II are not mutually exclusive; dual listing serves separate functions.",
    "Do not treat every CMS instrument as legally binding.",
    "Do not call an Action Plan an Agreement or MOU without the instrument.",
    "Do not convert a Concerted Action into an Appendix amendment.",
    "Do not call the Central Asian Flyway a treaty.",
    "Do not upgrade the COP14 initiative to a binding Agreement.",
    "Do not report a strategic-plan target as a conservation outcome.",
    "Do not classify every threat as a transboundary failure.",
    "Do not infer the 2026 provisional PYQ key.",
    "Do not invent a current Appendix or membership count.",
]

SESSION_TITLES = [
    "Migratory species and complete range",
    "Range State definition",
    "Weakest-link conservation logic",
    "Appendix I duties",
    "Taking prohibition and narrow exceptions",
    "Appendix II and dual-listing functions",
    "CMS AGREEMENT design",
    "Binding Agreement versus non-binding MOU",
    "Action Plans",
    "Concerted Actions",
    "Central Asian Flyway and COP14 initiative",
    "Strategic plan status",
    "Threat classification and Amur Falcon PYQ",
    "Amur Falcon local link and convention distinctions",
    "Current listing and instrument-status boundary",
]

ANSWER_ROUTES = [
    "Apply the cross-boundary migration test and map the complete life-cycle range.",
    "Define every jurisdiction touching the route as potentially relevant.",
    "Explain why one unprotected route segment can defeat protection elsewhere.",
    "State endangered listing, habitat duties, obstacle response and taking rule.",
    "Name the narrow Convention ground and retain space-time limits.",
    "Present Appendix II and simultaneous listing through their distinct functions.",
    "Describe whole-range and open-to-Range-States agreement design.",
    "Name the exact instrument and its binding status.",
    "State the plan's measures without upgrading its legal status or outcomes.",
    "Use priority action as an operational bridge, not a new listing.",
    "Describe the flyway separately from the COP14 initiative and its coordinating unit.",
    "Separate adopted initiative and targets from achieved conservation results.",
    "Classify the threat and carry the provisional Amur Falcon concept without a key.",
    "Use the local stopover link, then distinguish CMS, CITES and Ramsar.",
    "Close without inventing current listings, Parties or instrument status.",
]

PANELS = [
    panel("Migratory-species gate", "decision-tree", [
        "MOVEMENT OBSERVED -> ask whether it crosses national jurisdiction",
        "PATTERN -> significant proportion crosses cyclically and predictably",
        "YES -> CMS migratory-species test may be met",
        "NO -> mobility alone does not establish CMS status",
        "VERIFY -> use the taxon and current Appendix record",
    ], [FACTS[0][0], FACTS[19][0]]),
    panel("Range geography", "route-map", [
        "BREEDING SITE -> life-cycle stage",
        "PASSAGE AND STOPOVER -> temporary habitat and route link",
        "WINTERING OR FEEDING SITE -> another life-cycle stage",
        "OVERFLIGHT OR WATER ROUTE -> also within Convention range",
        "RULE -> conserve the connected circuit, not only endpoints",
    ], [FACTS[1][0], FACTS[3][0]]),
    panel("Range State map", "authority-map", [
        "STATE A -> breeding jurisdiction",
        "STATE B -> passage or stopover jurisdiction",
        "STATE C -> wintering jurisdiction",
        "FLAG STATE -> relevant taking beyond national limits where applicable",
        "CMS TASK -> coordinate every material jurisdiction",
    ], [FACTS[2][0], FACTS[3][0]]),
    panel("Appendix I duty chain", "process-flow", [
        "ENDANGERED MIGRATORY SPECIES -> Appendix I",
        "HABITAT -> conserve and restore where feasible and appropriate",
        "OBSTACLES -> prevent, remove, compensate for or minimize",
        "TAKING -> prohibit subject to narrow Convention exceptions",
        "EXCEPTION -> precise content plus space-and-time limits",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("Appendix II cooperation chain", "process-flow", [
        "UNFAVOURABLE STATUS OR SIGNIFICANT BENEFIT -> Appendix II",
        "RANGE STATES -> endeavour to conclude AGREEMENTS",
        "WHOLE RANGE -> agreement design objective",
        "COORDINATION -> habitat, monitoring, information and threats",
        "RULE -> cooperation route is not Appendix I duplication",
    ], [FACTS[6][0], FACTS[8][0]]),
    panel("Dual-listing matrix", "comparison-table", [
        "APPENDIX I -> endangered status and immediate protection duties",
        "APPENDIX II -> international-cooperation and agreement route",
        "BOTH -> expressly possible under Article IV",
        "NOT HIERARCHY -> functions overlap without cancelling each other",
        "ANSWER -> state each consequence separately",
    ], [FACTS[4][0], FACTS[6][0], FACTS[7][0]]),
    panel("Instrument-status ladder", "comparison-table", [
        "APPENDIX -> Convention listing status",
        "AGREEMENT -> identify exact binding instrument",
        "MOU -> identify exact non-binding instrument",
        "ACTION PLAN -> planned measures under its adopting authority",
        "CONCERTED ACTION -> priority cooperative work between COPs",
    ], [FACTS[9][0], FACTS[10][0], FACTS[11][0]]),
    panel("AGREEMENT design rail", "layered-rail", [
        "SCOPE -> whole migratory range",
        "ACCESS -> open to relevant Range States",
        "SCIENCE -> status review, research and information exchange",
        "HABITAT -> network, restoration and obstacle response",
        "GOVERNANCE -> authority, monitoring, reporting and coordination",
    ], [FACTS[8][0]]),
    panel("Central Asian Flyway firewall", "layered-rail", [
        "FLYWAY -> ecological migration geography",
        "INITIATIVE -> COP14 cooperation arrangement",
        "COORDINATING UNIT -> official release locates it in India",
        "AGREEMENT OR MOU -> not inferred",
        "OUTCOME -> not inferred from institutional adoption",
    ], [FACTS[12][0], FACTS[13][0]]),
    panel("Plan-versus-outcome gate", "decision-gate", [
        "COP14 -> Samarkand, February 2024",
        "STRATEGIC PLAN -> 2024-2032 direction and targets",
        "INITIATIVE -> Central Asian Flyway coordination step",
        "MONITORING -> needed for implementation evidence",
        "RULE -> adoption is an output, not species recovery",
    ], [FACTS[13][0], FACTS[14][0]]),
    panel("Threat-location matrix", "comparison-table", [
        "ROUTE-WIDE -> habitat network, taking and shared data",
        "DOMESTIC -> power line, wetland loss or local enforcement",
        "LOCAL SUCCESS -> Doyang or Pangti stopover protection",
        "LIMIT -> one repaired link does not prove whole-route safety",
        "RESPONSE -> match institution to threat location",
    ], [FACTS[15][0], FACTS[17][0]]),
    panel("PYQ and convention spine", "answer-spine", [
        "DEFINE -> migratory species, range and Range State",
        "CLASSIFY -> Appendix I, II or both",
        "NAME -> Agreement, MOU, Action Plan or Concerted Action",
        "APPLY -> Amur Falcon answer-free route-and-community concept",
        "SEPARATE -> CMS, CITES, Ramsar and current-listing evidence",
    ], [FACTS[16][0], FACTS[18][0], FACTS[19][0]]),
]

TOPIC_10 = common.topic(
    10,
    "CMS Bonn Convention Migratory Species",
    "10_CMS-Bonn-Convention-Migratory-Species",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-10_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Define a CMS migratory species, its range and a Range State.", [0, 1, 2]),
        (10, "Distinguish CMS Appendix I, Appendix II and dual listing.", [4, 5, 6, 7]),
        (15, "Explain the legal and functional differences among Agreements, MOUs, Action Plans and Concerted Actions.", [8, 9, 10, 11]),
        (15, "Explain the Central Asian Flyway's status after CMS COP14 without overstating the instrument or outcome.", [12, 13, 14]),
        (20, "Assess migratory-species conservation as a weakest-link problem requiring both international and domestic action.", [1, 2, 3, 15, 17]),
        (20, "Use the Amur Falcon route to build a source-disciplined CMS answer.", [0, 3, 12, 16, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "cyclically and predictably", "Range State", "Appendix I", "Appendix II",
        "dual listing", "taking", "AGREEMENT", "Memorandum of Understanding",
        "Action Plan", "Concerted Action", "Central Asian Flyway",
        "coordinating unit in India", "Samarkand Strategic Plan",
        "2024-2032", "Amur Falcon", "Doyang Lake", "local action",
    ],
    (
        "The audited provisional 2026 routing ledger carries one Topic 10 "
        "objective demand: Amur Falcon migration to Doyang Lake and community-"
        "based conservation. The provisional answer key is not recorded or inferred."
    ),
    [],
    CMS_LIVE_SOURCE_ATTEMPTS,
    (
        "The CMS Convention text and official COP14 outcome release were "
        "substantively retrieved on 2026-09-03. They support definitions, "
        "Appendix mechanics, AGREEMENT design, the dated Central Asian Flyway "
        "initiative and strategic-plan adoption. No current Appendix species "
        "list, Party count, MOU count or implementation outcome was inferred."
    ),
    extra=[
        "basic/07_Biosphere-Reserves-and-Ramsar-Sites.md",
        "basic/09_CITES-and-Wildlife-Trade.md",
        "basic/28_Species-and-Current-Affairs-Tracker.md",
        "advanced/09_CITES-and-Wildlife-Trade.md",
    ],
    pyq_audit_heading="PROVISIONAL OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
    register_headings=(
        "MIGRATORY-SPECIES, RANGE, RANGE-STATE AND APPENDIX MAP",
        "AGREEMENT, MOU, ACTION-PLAN, FLYWAY AND OUTCOME TRAPS",
        "CMS ANSWER SPINE",
        "LIVE COP, LISTING, INSTRUMENT AND PROVISIONAL-PYQ BOUNDARY",
    ),
    register_answer_spine=[
        "APPLY THE CYCLICAL AND PREDICTABLE CROSS-BOUNDARY TEST",
        "MAP THE COMPLETE RANGE AND EVERY MATERIAL RANGE STATE",
        "DISTINGUISH APPENDIX I, APPENDIX II AND DUAL LISTING",
        "NAME THE EXACT AGREEMENT, MOU, ACTION PLAN OR CONCERTED ACTION",
        "LOCATE EACH THREAT AS TRANSBOUNDARY OR DOMESTIC",
        "USE AMUR FALCON AS A LOCAL LINK, NOT WHOLE-ROUTE PROOF",
        "CONCLUDE WITH SYNCHRONISED RANGE-STATE AND LOCAL IMPLEMENTATION",
    ],
)
