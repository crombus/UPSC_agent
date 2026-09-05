"""Authored data for Environment and Ecology learner-v2 Topic 08."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import WILDLIFE_ACT_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Legal vintage first", "Every answer must identify whether it uses the pre-2022 six-schedule structure or the post-2022 four-schedule structure of the Wildlife Protection Act."),
    ("Six schedules to four", "The Wildlife Protection Amendment Act 2022 restructured the earlier six schedules into four; an older PYQ may still test the law in force at its own time point."),
    ("Schedule I", "Under the post-2022 owner framework, Schedule I lists animals receiving the greatest degree of protection; no species placement is assumed without the current schedule."),
    ("Schedule II", "Schedule II lists animals receiving a lesser degree of protection than Schedule I, while still remaining protected under the Act."),
    ("Schedule III", "Post-2022 Schedule III is the specified plant schedule; it is not a third animal-protection tier and replaces the function of old Schedule VI."),
    ("Schedule IV", "Post-2022 Schedule IV covers CITES-listed scheduled specimens for international trade regulation; it is not a higher protection rung than Schedule I or II."),
    ("Species placement discipline", "Exact species-to-schedule placement can change through the applicable legal process and must be checked against the current consolidated schedule or notification."),
    ("Vermin time point", "The old Schedule V vermin list was omitted in 2022; the owner records a central notification route for a specified area and period and excludes Schedule I animals."),
    ("Hunting prohibition", "The Act's baseline is prohibition of hunting protected wild animals; a legal exception must be traced to its statutory condition, authority and written permission."),
    ("Permit and exception", "Scientific, educational, collection or management purposes do not create a free-standing right to hunt; the applicable permit and statutory conditions remain necessary."),
    ("Dangerous or beyond recovery route", "The owner records narrow action where an animal is dangerous to human life or disabled or diseased beyond recovery, with the competent authority depending on schedule and provision."),
    ("CITES Management Authority", "The post-2022 framework requires a Management Authority for permits and certificates in international trade in scheduled specimens."),
    ("CITES Scientific Authority", "The Scientific Authority advises on the conservation consequences of trade; it performs a different function from the permit-issuing Management Authority."),
    ("Chapter VB trade architecture", "The 2022 amendment inserted a dedicated international-trade chapter for scheduled specimens, translating CITES obligations into domestic legal machinery."),
    ("Invasive alien species", "The amendment empowered the Central Government to regulate or prohibit the import, trade, possession or proliferation of invasive alien species under the applicable provision."),
    ("WCCB statutory role", "MoEFCC's retrievable page states that WCCB was constituted under section 38Y and lists section 38Z functions including intelligence, coordination, capacity and international cooperation."),
    ("State and Chief Wildlife Warden", "State wildlife departments and the Chief Wildlife Warden perform on-ground authorisation and enforcement functions; their jurisdiction must not be assigned to WCCB."),
    ("NBWL and NTCA", "NBWL and NTCA exercise protected-area and tiger-specific roles under their respective provisions; they do not replace the Chief Wildlife Warden or CITES authorities."),
    ("Science, law and trade", "IUCN category assesses extinction risk, Wildlife Protection Act schedules create domestic legal consequences, and CITES regulates international trade; the three systems are related but distinct."),
    ("Audited PYQ vintage boundary", "Routed demands cover old Schedule VI plant implications, protected-animal provisions and a 2024 Indian Flying Fox vermin question; each must be answered at its legal time point without inferring an option key."),
]

TRAPS = [
    "Do not answer a pre-2022 question with the post-2022 schedule count without qualification.",
    "Do not say the current Act still has six schedules.",
    "Do not assign a species to Schedule I from memory without checking the current text.",
    "Do not describe Schedule II as unprotected wildlife.",
    "Do not call post-2022 Schedule III an animal-protection tier.",
    "Do not call Schedule IV the highest domestic protection category.",
    "Do not treat CITES Appendix change as an instantaneous Indian schedule amendment.",
    "Do not say the old Schedule V vermin list still exists.",
    "Do not convert a hunting exception into a general permission.",
    "Do not omit the competent authority and written-permission requirement.",
    "Do not merge Management Authority and Scientific Authority functions.",
    "Do not use WCCB as the authority for every wildlife-law decision.",
    "Do not attach a penalty amount without the applicable amendment and offence provision.",
    "Do not equate an IUCN category, domestic schedule and CITES Appendix.",
    "Do not infer an objective answer key from a routed PYQ demand.",
]

SESSION_TITLES = [
    "Legal vintage and six-to-four restructuring",
    "Schedule I animals",
    "Schedule II animals",
    "Schedule III plants",
    "Schedule IV CITES specimens",
    "Species placement and vermin time point",
    "Hunting prohibition",
    "Permit and exception architecture",
    "Dangerous or beyond-recovery route",
    "CITES Management Authority",
    "Scientific Authority and Chapter VB",
    "Invasive alien species power",
    "WCCB statutory role",
    "State, Chief Wildlife Warden, NBWL and NTCA roles",
    "Science-law-trade and audited PYQ boundary",
]

ANSWER_ROUTES = [
    "Open by fixing the pre- or post-2022 legal structure.",
    "State the highest animal-protection schedule without guessing species placement.",
    "Contrast Schedule II with Schedule I while retaining legal protection.",
    "Identify the plant schedule and its old Schedule VI lineage.",
    "Describe Schedule IV as trade regulation, not a protection rung.",
    "Verify current notification and treat vermin through the correct legal vintage.",
    "Start from prohibition rather than exception.",
    "Name the purpose, permit, authority and statutory condition.",
    "Use the narrow condition without converting it into a general culling power.",
    "Assign permits and certificates to the Management Authority.",
    "Separate scientific advice from Chapter VB's wider trade machinery.",
    "State the Central Government power without inventing a listed species.",
    "Use sections 38Y and 38Z only for the WCCB role confirmed by MoEFCC.",
    "Map each domestic authority to its own jurisdiction.",
    "Close by separating IUCN science, domestic law, CITES trade and PYQ vintage.",
]

PANELS = [
    panel("Legal-vintage timeline", "timeline", [
        "1972 ACT -> original wildlife-protection framework",
        "PRE-2022 -> six schedules",
        "2022 AMENDMENT -> restructuring",
        "POST-2022 -> four schedules",
        "RULE -> answer the law applicable to the question's time point",
    ], [FACTS[0][0], FACTS[1][0]]),
    panel("Post-2022 schedule map", "hierarchy", [
        "SCHEDULE I -> animals, greatest degree of protection",
        "SCHEDULE II -> animals, lesser degree than Schedule I",
        "SCHEDULE III -> specified plants",
        "SCHEDULE IV -> CITES scheduled specimens and trade control",
        "RULE -> Schedule IV is not another protection rung",
    ], [FACTS[2][0], FACTS[3][0], FACTS[4][0], FACTS[5][0]]),
    panel("Species-placement gate", "decision-tree", [
        "NAME A SPECIES -> identify legal date",
        "CHECK -> current consolidated schedule or notification",
        "IUCN STATUS -> separate scientific field",
        "CITES APPENDIX -> separate trade field",
        "NO MEMORY SHORTCUT -> placement can change",
    ], [FACTS[6][0], FACTS[18][0]]),
    panel("Vermin time-point map", "timeline", [
        "OLD STRUCTURE -> Schedule V vermin list",
        "2022 CHANGE -> old Schedule V omitted",
        "CURRENT OWNER ROUTE -> central notification",
        "LIMITS -> specified area and period; Schedule I excluded",
        "PYQ RULE -> use the law in force when the question is framed",
    ], [FACTS[7][0], FACTS[19][0]]),
    panel("Prohibition and exception gate", "process-flow", [
        "BASELINE -> hunting prohibited",
        "CLAIMED EXCEPTION -> identify statutory purpose or condition",
        "AUTHORITY -> Chief Wildlife Warden or other authorised officer",
        "FORM -> applicable written permission or permit",
        "RULE -> exception never becomes general permission",
    ], [FACTS[8][0], FACTS[9][0], FACTS[10][0]]),
    panel("Narrow animal-action route", "decision-gate", [
        "DANGEROUS TO HUMAN LIFE -> test statutory condition",
        "DISABLED OR DISEASED BEYOND RECOVERY -> test evidence",
        "SCHEDULE -> determines applicable authority route",
        "WRITTEN PERMISSION -> retain in the answer",
        "NO EXTENSION -> do not invent a population-control exception",
    ], [FACTS[10][0]]),
    panel("CITES authority split", "comparison-table", [
        "MANAGEMENT AUTHORITY -> permits and certificates",
        "SCIENTIFIC AUTHORITY -> conservation advice on trade",
        "CHAPTER VB -> domestic international-trade machinery",
        "SCHEDULE IV -> scheduled specimens",
        "RULE -> advice, permission and species listing are separate functions",
    ], [FACTS[11][0], FACTS[12][0], FACTS[13][0]]),
    panel("CITES incorporation firewall", "layered-rail", [
        "CITES COP OR APPENDIX -> international decision",
        "INDIAN LEGAL PROCESS -> applicable domestic update",
        "SCHEDULE IV -> domestic scheduled-specimen status",
        "PERMIT SYSTEM -> Management Authority action",
        "NO AUTOMATICITY -> international change is not instant domestic text",
    ], [FACTS[5][0], FACTS[6][0], FACTS[13][0]]),
    panel("Invasive alien species power", "process-flow", [
        "IDENTIFY -> species claimed to be invasive",
        "VERIFY -> applicable legal notification or order",
        "CENTRAL POWER -> regulate or prohibit listed activities",
        "IMPLEMENT -> trade, possession and proliferation controls as applicable",
        "CAUTION -> no species list is inferred from the enabling power",
    ], [FACTS[14][0]]),
    panel("WCCB statutory map", "authority-map", [
        "SECTION 38Y -> constitution of WCCB on MoEFCC page",
        "SECTION 38Z -> functions on MoEFCC page",
        "INTELLIGENCE -> collection, collation and dissemination",
        "COORDINATION -> enforcement and international cooperation",
        "LIMIT -> WCCB does not replace every statutory decision-maker",
    ], [FACTS[15][0]]),
    panel("Domestic authority matrix", "comparison-table", [
        "CHIEF WILDLIFE WARDEN -> state authorisation and enforcement route",
        "WCCB -> organised wildlife-crime intelligence and coordination",
        "NBWL -> protected-area governance role",
        "NTCA -> tiger-specific statutory role",
        "CITES AUTHORITIES -> international scheduled-specimen trade",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("PYQ and answer spine", "answer-spine", [
        "DATE -> pre-2022 or post-2022 structure",
        "CLASSIFY -> Schedule I, II, III or IV function",
        "TRACE -> prohibition, exception, authority and permit",
        "SEPARATE -> IUCN risk, domestic schedule and CITES trade",
        "QUALIFY -> verify current placement, penalty and objective key",
    ], [FACTS[18][0], FACTS[19][0]]),
]

TOPIC_08 = common.topic(
    8,
    "Wildlife Protection Act and Schedules",
    "08_Wildlife-Protection-Act-and-Schedules",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-08_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Explain the post-2022 four-schedule structure.", [0, 1, 2, 3, 4, 5]),
        (10, "Distinguish Schedule IV trade control from animal protection tiers.", [2, 3, 5, 18]),
        (15, "Explain hunting prohibition and narrow statutory exceptions.", [8, 9, 10, 16]),
        (15, "Explain CITES alignment through Schedule IV and the two authorities.", [5, 11, 12, 13]),
        (20, "Assess the 2022 amendment as treaty-alignment and enforcement reform.", [1, 6, 13, 14, 15, 17]),
        (20, "Why must wildlife-law answers be time-sensitive and jurisdiction-specific?", [0, 6, 7, 16, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "pre-2022", "post-2022", "four schedules", "Schedule I", "Schedule II",
        "Schedule III", "Schedule IV", "specified plants", "CITES scheduled specimens",
        "vermin", "specified area and period", "hunting prohibition",
        "Chief Wildlife Warden", "Management Authority", "Scientific Authority",
        "Chapter VB", "invasive alien species", "section 38Y", "section 38Z", "WCCB",
    ],
    (
        "Audited ledgers route the 2020 old Schedule VI plant demand, 2022 "
        "protected-animal provisions and 2024 Indian Flying Fox vermin framing. "
        "They remain answer-free objective demands. The package fixes the legal "
        "time point and does not infer a species placement, penalty, notification "
        "or option key."
    ),
    [],
    WILDLIFE_ACT_LIVE_SOURCE_ATTEMPTS,
    (
        "India Code returned HTTP 403 on 2026-09-03. Official state forest "
        "department copies of the 2022 amendment were retrievable only as raw "
        "or image PDF bytes and were not text-mined. MoEFCC's wildlife page was "
        "used narrowly for WCCB sections 38Y and 38Z; its stale or erroneous "
        "material was excluded. No species schedule, penalty or later amendment "
        "was inferred."
    ),
    extra=[
        "basic/06_Protected-Area-Network-India.md",
        "basic/09_CITES-and-Wildlife-Trade.md",
        "basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
        "advanced/09_CITES-and-Wildlife-Trade.md",
    ],
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
    register_headings=(
        "LEGAL VINTAGE, SCHEDULE AND AUTHORITY MAP",
        "PROHIBITION, EXCEPTION, VERMIN AND TRADE TRAPS",
        "STATUTE-TO-ENFORCEMENT ANSWER SPINE",
        "LIVE STATUTE, NOTIFICATION, PENALTY AND SPECIES-PLACEMENT BOUNDARY",
    ),
    register_answer_spine=[
        "FIX THE LEGAL TIME POINT: PRE-2022 OR POST-2022",
        "STATE THE FUNCTION OF SCHEDULE I, II, III OR IV",
        "VERIFY THE SPECIES PLACEMENT OR NOTIFICATION",
        "START WITH PROHIBITION, THEN TEST THE NARROW EXCEPTION",
        "NAME THE COMPETENT AUTHORITY, PERMIT AND JURISDICTION",
        "SEPARATE IUCN SCIENCE, DOMESTIC LAW AND CITES TRADE",
        "CONCLUDE WITH FORENSICS, COORDINATION AND ENFORCEMENT CAPACITY",
    ],
)
