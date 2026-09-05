"""Authored data for Environment and Ecology learner-v2 Topic 05."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import IUCN_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Red List function", "The IUCN Red List is a criteria-based scientific assessment of extinction risk; it is not itself an Indian statute or permit."),
    ("Nine assessment categories", "The owner distinguishes Not Evaluated, Data Deficient, Least Concern, Near Threatened, Vulnerable, Endangered, Critically Endangered, Extinct in the Wild and Extinct."),
    ("Threatened collective term", "Threatened collectively covers Vulnerable, Endangered and Critically Endangered; it is not a separate tenth category."),
    ("Not Evaluated and Data Deficient", "Not Evaluated means the criteria have not been applied, while Data Deficient means evidence is inadequate for a risk assessment; neither means safe."),
    ("Category and population trend", "A Red List category states assessed extinction risk, whereas increasing, stable, decreasing or unknown describes population trend; the two fields answer different questions."),
    ("Category and criterion", "Category is the resulting risk class; criterion is the quantitative route used to justify it, so a category name must not be substituted for criterion A, B, C, D or E."),
    ("Criterion A", "Criterion A concerns population-size reduction over the applicable assessment window; no percentage or assessment year is supplied unless the cited assessment provides it."),
    ("Criterion B", "Criterion B concerns restricted geographic range together with the applicable fragmentation, decline or fluctuation conditions; range restriction alone must be read with the criterion text."),
    ("Criterion C", "Criterion C combines small population size with continuing decline and its applicable population structure conditions."),
    ("Criterion D", "Criterion D addresses a very small or very restricted population under the applicable category threshold."),
    ("Criterion E", "Criterion E uses quantitative analysis of extinction probability; it is not a synonym for expert opinion or a simple headcount."),
    ("One qualifying route", "The owner records that meeting one applicable criterion can support a threatened category, but the taxon must meet that category's full threshold and subconditions."),
    ("Assessment scale", "Global and regional or national assessments can differ because their geographic scope differs; every status claim must name the assessment scale and year."),
    ("Endemic and native", "Native means naturally occurring in the stated region; endemic means naturally restricted to the stated region, so every endemic is native there but not every native is endemic."),
    ("Endemic, rare and threatened", "Endemism describes range restriction, rarity describes abundance or occurrence, and threatened status is an assessed extinction-risk class; they can overlap without being synonyms."),
    ("Endemism as risk multiplier", "Restricted range can remove spatial refuge and recolonisation options, but endemism does not automatically make a taxon threatened."),
    ("Assessment workflow", "The owner links specialist expertise, Species Survival Commission groups, assessment documentation and review; a published category must remain tied to its supporting assessment."),
    ("Green Status distinction", "IUCN Green Status addresses recovery and conservation impact, while the Red List addresses extinction risk; one does not replace the other."),
    ("Science-law-action chain", "The Great Indian Bustard route separates IUCN risk assessment, Indian legal protection and judicial or infrastructure mitigation; no current population count is inferred."),
    ("Audited PYQ boundary", "Routed demands cover Indian endemism, habitat matching and Western hoolock gibbon status, habitat and adaptation; objective keys and unstated current ranges are not inferred."),
]

TRAPS = [
    "Do not call the IUCN Red List a binding Indian wildlife law.",
    "Do not treat threatened as a category separate from VU, EN and CR.",
    "Do not equate Data Deficient or Not Evaluated with low risk.",
    "Do not substitute population trend for assessed Red List category.",
    "Do not substitute a category name for the criterion that supports it.",
    "Do not quote a Criterion A percentage without the assessment source and taxon context.",
    "Do not reduce Criterion B to range size while omitting its applicable subconditions.",
    "Do not describe Criterion C as a bare small-population test.",
    "Do not attach an unstated numerical threshold to Criterion D.",
    "Do not describe Criterion E as an ordinary census.",
    "Do not claim that every threatened taxon satisfies all five criteria.",
    "Do not transfer a global category automatically to a national population.",
    "Do not use native and endemic interchangeably.",
    "Do not use endemic, rare and threatened as synonyms.",
    "Do not infer current species status, trend or range from an undated example.",
]

SESSION_TITLES = [
    "Red List purpose and nine categories",
    "Threatened as a collective term",
    "Not Evaluated and Data Deficient",
    "Category versus population trend",
    "Category versus criterion",
    "Criteria A and B",
    "Criterion C",
    "Criterion D",
    "Criterion E",
    "One qualifying criterion and full subconditions",
    "Global and regional assessment scale",
    "Endemic and native",
    "Endemic, rare and threatened",
    "Assessment workflow and Green Status",
    "Science-law-action chain and audited PYQs",
]

ANSWER_ROUTES = [
    "Open with scientific extinction-risk assessment and map the nine categories.",
    "Define threatened precisely as VU plus EN plus CR.",
    "Use the attempted-assessment distinction between NE and DD.",
    "Write assessed risk and population trend in separate clauses.",
    "Name both the result category and the supporting criterion.",
    "Explain decline and range routes without inventing thresholds.",
    "Pair small population with continuing decline.",
    "Keep very small or restricted population tied to the applicable threshold.",
    "Identify quantitative extinction-probability analysis.",
    "State that one route can suffice only when all applicable subconditions are met.",
    "Name global or regional scale and assessment year.",
    "Define both terms through natural distribution.",
    "Separate range, abundance and assessed risk.",
    "Explain assessment review and keep recovery status separate.",
    "Close with science, domestic law, mitigation and PYQ evidence as distinct layers.",
]

PANELS = [
    panel("Red List category rail", "hierarchy", [
        "NE -> criteria not yet applied",
        "DD -> evidence inadequate for a risk assessment",
        "LC -> NT -> VU -> EN -> CR -> EW -> EX",
        "THREATENED -> VU + EN + CR only",
        "RULE -> category is assessed risk, not legal protection",
    ], [FACTS[0][0], FACTS[1][0], FACTS[2][0], FACTS[3][0]]),
    panel("Status fields firewall", "comparison-table", [
        "CATEGORY -> assessed extinction-risk class",
        "CRITERION -> quantitative route supporting the category",
        "TREND -> increasing, stable, decreasing or unknown",
        "SCALE -> global or regional/national assessment",
        "DATE -> assessment vintage; never silently omit it",
    ], [FACTS[4][0], FACTS[5][0], FACTS[12][0]]),
    panel("Criteria A to E map", "matrix", [
        "A -> population-size reduction",
        "B -> restricted range plus applicable subconditions",
        "C -> small population plus continuing decline",
        "D -> very small or very restricted population",
        "E -> quantitative extinction-probability analysis",
    ], [FACTS[6][0], FACTS[7][0], FACTS[8][0], FACTS[9][0], FACTS[10][0]]),
    panel("One-route decision gate", "process-flow", [
        "ASSESS TAXON -> test Criteria A to E",
        "ONE ROUTE MAY SUFFICE -> only for its applicable category",
        "CHECK -> threshold, subcriterion, evidence and scale",
        "DOCUMENT -> category plus criterion plus assessment year",
        "NEVER -> infer a threshold from the category name alone",
    ], [FACTS[5][0], FACTS[11][0], FACTS[12][0]]),
    panel("NE and DD diagnostic", "decision-tree", [
        "WERE THE CRITERIA APPLIED?",
        "NO -> Not Evaluated",
        "YES, BUT EVIDENCE INADEQUATE -> Data Deficient",
        "DD -> uncertainty, not reassurance",
        "RULE -> neither label establishes Least Concern",
    ], [FACTS[3][0]]),
    panel("Distribution vocabulary", "comparison", [
        "NATIVE -> naturally occurs in the stated region",
        "ENDEMIC -> naturally restricted to the stated region",
        "RARE -> low abundance or occurrence under a stated measure",
        "THREATENED -> VU, EN or CR assessment outcome",
        "RULE -> overlap does not erase distinct meanings",
    ], [FACTS[13][0], FACTS[14][0]]),
    panel("Endemism risk pathway", "causal-chain", [
        "RESTRICTED NATURAL RANGE -> fewer spatial refuges",
        "LOCAL HABITAT LOSS -> affects a larger share of total range",
        "ISOLATION -> weaker natural recolonisation",
        "RESULT -> vulnerability may rise",
        "LIMIT -> endemic does not automatically mean threatened",
    ], [FACTS[15][0]]),
    panel("Assessment scale lens", "nested-map", [
        "GLOBAL ASSESSMENT -> taxon across its global range",
        "REGIONAL ASSESSMENT -> taxon inside a stated region",
        "DIFFERENT SCOPE -> categories may differ",
        "POPULATION TREND -> separately reported field",
        "ANSWER RULE -> state scale, year and evidence",
    ], [FACTS[4][0], FACTS[12][0]]),
    panel("Assessment workflow", "process-flow", [
        "EVIDENCE -> specialist assessment",
        "CRITERIA -> documented application",
        "REVIEW -> consistency and supporting information",
        "PUBLICATION -> category tied to assessment record",
        "REASSESSMENT -> later change needs a dated source",
    ], [FACTS[16][0]]),
    panel("Red List and Green Status", "comparison-table", [
        "RED LIST -> extinction risk",
        "GREEN STATUS -> recovery and conservation impact",
        "SAME TAXON -> two different analytical questions",
        "NO SUBSTITUTION -> recovery metric does not erase risk category",
        "USE -> pair risk diagnosis with recovery ambition",
    ], [FACTS[17][0]]),
    panel("Science law action chain", "layered-rail", [
        "IUCN RED LIST -> scientific global or regional risk assessment",
        "WILDLIFE LAW -> domestic prohibition, permit and schedule rules",
        "COURT OR AGENCY -> remedy and implementation choices",
        "HABITAT ACTION -> mitigation, connectivity and monitoring",
        "RULE -> no layer automatically determines the next",
    ], [FACTS[0][0], FACTS[18][0]]),
    panel("PYQ and answer spine", "answer-spine", [
        "DEFINE -> category, criterion, trend and scale",
        "DISTINGUISH -> endemic, native, rare and threatened",
        "APPLY -> one source-bounded Indian species or habitat route",
        "QUALIFY -> assessment year and no inferred objective key",
        "CONCLUDE -> assessment must translate into habitat and legal action",
    ], [FACTS[12][0], FACTS[14][0], FACTS[19][0]]),
]

TOPIC_05 = common.topic(
    5,
    "IUCN Red List and Endemism",
    "05_IUCN-Red-List-and-Endemism",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-05_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish Red List category, criterion and population trend.", [0, 4, 5]),
        (10, "Explain why Data Deficient is not evidence of low extinction risk.", [1, 2, 3]),
        (15, "Explain Criteria A-E without inventing taxon-specific thresholds.", [6, 7, 8, 9, 10, 11]),
        (15, "Distinguish endemic, native, rare and threatened species.", [13, 14, 15]),
        (20, "Assess the value and limits of the IUCN Red List for Indian conservation.", [0, 12, 16, 17, 18]),
        (20, "Show how scientific assessment should translate into law and habitat action.", [5, 12, 15, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "Not Evaluated", "Data Deficient", "Vulnerable", "Endangered",
        "Critically Endangered", "Criterion A", "Criterion B", "Criterion C",
        "Criterion D", "Criterion E", "population trend", "assessment scale",
        "endemic", "native", "rare", "Green Status", "Species Survival Commission",
        "Great Indian Bustard", "Western hoolock gibbon", "scientific assessment",
    ],
    (
        "Audited ledgers route 2019 Indian endemism and habitat matching, 2022 "
        "species identification, 2023 marsupial distribution, 2024 natural-"
        "habitat pairs and 2026 Western hoolock gibbon status, habitat and "
        "adaptation. They are carried as answer-free demands; no objective key "
        "or unstated current range, trend or assessment year is inferred."
    ),
    [],
    IUCN_LIVE_SOURCE_ATTEMPTS,
    (
        "Direct IUCN pages returned HTTP 520 on 2026-09-03, India Code and PIB "
        "returned HTTP 403, and no current species assessment was imported. "
        "MoEFCC's wildlife page was substantive only for its domestic policy-law "
        "role. Category, criterion, trend, scale and year therefore remain "
        "bounded to the repository owners and each cited assessment."
    ),
    extra=[
        "basic/04_Biodiversity-Levels-and-Hotspots.md",
        "basic/08_Wildlife-Protection-Act-and-Schedules.md",
        "basic/09_CITES-and-Wildlife-Trade.md",
        "basic/28_Species-and-Current-Affairs-Tracker.md",
    ],
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
    register_headings=(
        "CATEGORY, CRITERION, TREND AND SCALE MAP",
        "ENDEMISM AND ASSESSMENT TRAPS",
        "ASSESSMENT-TO-ACTION ANSWER SPINE",
        "LIVE IUCN, LEGAL AND CURRENT-STATUS BOUNDARY",
    ),
    register_answer_spine=[
        "IDENTIFY THE CLAIM: CATEGORY, CRITERION, TREND OR DISTRIBUTION",
        "STATE THE ASSESSMENT SCALE AND YEAR",
        "APPLY THE CORRECT A-E ROUTE WITHOUT INVENTING A THRESHOLD",
        "SEPARATE ENDEMIC, NATIVE, RARE AND THREATENED",
        "ADD ONE SOURCE-BOUNDED SPECIES OR HABITAT EXAMPLE",
        "SEPARATE IUCN SCIENCE FROM DOMESTIC LAW AND TRADE CONTROL",
        "CONCLUDE WITH HABITAT ACTION, MONITORING AND REASSESSMENT",
    ],
)
