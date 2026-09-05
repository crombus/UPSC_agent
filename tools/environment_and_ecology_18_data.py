"""Authored data for Environment and Ecology learner-v2 Topic 18."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import IPCC_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("IPCC identity", "The Intergovernmental Panel on Climate Change is an intergovernmental scientific-assessment body that provides policy-relevant climate information; it is not the UNFCCC negotiating forum."),
    ("WMO-UNEP origin", "The IPCC was created in 1988 by the World Meteorological Organization and the United Nations Environment Programme; founding bodies, current members and report authors are distinct categories."),
    ("Assess-not-research mandate", "The IPCC assesses published scientific, technical and socio-economic literature and identifies agreement and knowledge gaps; it does not conduct its own original research."),
    ("Working Group I", "Working Group I assesses the physical science basis of climate change, including observations, drivers, attribution and conditional projections."),
    ("Working Group II", "Working Group II assesses impacts, adaptation and vulnerability; it is not the mitigation-options working group."),
    ("Working Group III", "Working Group III assesses mitigation of climate change, including pathways, sectors and enabling conditions; it does not negotiate national commitments."),
    ("TFI boundary", "The Task Force on National Greenhouse Gas Inventories develops and refines inventory methodologies; it is a distinct IPCC body, not a fourth thematic Working Group."),
    ("Synthesis Report", "A Synthesis Report integrates assessment-cycle findings across the Working Group contributions and relevant products; it is not simply another Working Group report."),
    ("Special and methodology reports", "Special Reports assess defined policy-relevant themes, while Methodology Reports support measurement and inventory methods; neither label means a completed full assessment cycle."),
    ("Assessment-cycle sequence", "An assessment cycle proceeds through scoped products, author selection, drafts, review, revision and plenary consideration; a planned outline or workplan is not a published scientific finding."),
    ("Author-review architecture", "Experts author reports and multiple rounds of expert and government review test completeness, balance and traceability; reviewers do not automatically become report authors."),
    ("Approval-acceptance distinction", "Summaries for Policymakers are considered line by line with governments and authors, while longer reports follow their applicable acceptance or approval procedure; government involvement must not be misdescribed as governments conducting the science."),
    ("Policy-relevant boundary", "IPCC assessments are policy-relevant but not policy-prescriptive: they assess evidence, risks and response options without selecting a national policy or negotiating a treaty target."),
    ("Confidence-likelihood distinction", "Confidence communicates the validity of a finding through evidence and agreement, whereas likelihood expresses an assessed probability for a well-defined outcome; the two calibrated dimensions are not synonyms."),
    ("Confidence discipline", "A confidence term must remain attached to the precise finding, evidence base, scale and report that used it; it cannot be transferred to a broader claim."),
    ("Likelihood discipline", "A likelihood term is meaningful only within the IPCC calibrated framework and the statement to which it applies; no probability threshold is quoted unless verified from the cited report guidance."),
    ("Scenario-not-forecast", "IPCC scenarios and pathways explore conditional futures under stated assumptions; an assessed scenario is not an unconditional forecast or a promise that policy will follow it."),
    ("Assessment-lag boundary", "Assessments synthesise literature available within defined cut-offs, so the completed report remains authoritative for its scope but does not automatically include later studies or events."),
    ("AR6-AR7 status", "AR6 is the latest completed assessment cycle in the official material checked, while AR7 is a cycle in progress with planned products; an AR7 outline or schedule is not an AR7 finding."),
    ("Science-policy evidence boundary", "An IPCC finding, UNFCCC decision, national NDC, media summary and model output have different authorship and legal status; every answer must cite the exact report, cycle, working group and status."),
]

TRAPS = [
    "Do not call the IPCC a negotiating body, treaty secretariat or climate regulator.",
    "Do not say the IPCC conducts its own primary experiments or observations.",
    "Do not swap the mandates of Working Groups I, II and III.",
    "Do not call the Task Force on Inventories a fourth Working Group.",
    "Do not merge a Working Group report with the Synthesis Report.",
    "Do not treat a Special Report or Methodology Report as a full assessment cycle.",
    "Do not convert an outline, scoping decision or workplan into a published finding.",
    "Do not describe government SPM consideration as government authorship of the science.",
    "Do not treat policy-relevant as policy-prescriptive.",
    "Do not use confidence and likelihood as interchangeable labels.",
    "Do not transfer calibrated language from one finding or scale to another.",
    "Do not call a scenario a forecast.",
    "Do not present AR7 process milestones as replacement evidence for AR6.",
    "Do not invent a report publication date, status, confidence or likelihood threshold.",
    "Do not convert IPCC assessment language into a legal obligation for a Party.",
]

SESSION_TITLES = [
    "IPCC identity origin and institutional boundary",
    "Assessing literature rather than conducting research",
    "Working Group I physical science basis",
    "Working Group II impacts adaptation vulnerability",
    "Working Group III mitigation assessment",
    "TFI and Synthesis Report boundary",
    "Special Reports and Methodology Reports",
    "Assessment-cycle sequence and status gates",
    "Authors review rounds and evidence traceability",
    "Approval and acceptance distinction",
    "Policy relevance and confidence-likelihood boundary",
    "Confidence attachment discipline",
    "Likelihood attachment discipline",
    "Scenario assessment and literature cut-off",
    "AR6 AR7 and science-policy synthesis",
]

ANSWER_ROUTES = [
    "Define the IPCC and separate assessment from UNFCCC negotiation.",
    "Explain literature synthesis, author assessment and knowledge-gap identification.",
    "Use Working Group I only for physical science, attribution and projections.",
    "Use Working Group II for impacts, vulnerability, adaptation and limits.",
    "Use Working Group III for mitigation pathways and enabling conditions.",
    "Separate TFI inventory methodology from the integrative Synthesis Report.",
    "Distinguish topic-specific assessments from inventory-method guidance.",
    "Move through scope, draft, review, revision and plenary status without skipping gates.",
    "Show how review improves traceability without implying reviewer authorship.",
    "Separate SPM approval from the applicable status of the underlying report.",
    "Keep policy relevance and calibrated uncertainty distinct from prescription.",
    "Attach confidence only to the exact assessed statement and evidence base.",
    "Attach likelihood only to the defined outcome and verified calibration.",
    "State scenario assumptions and literature cut-off before using a projection.",
    "Use AR6 findings and label AR7 only as an in-progress assessment cycle.",
]

PANELS = [
    panel("Institutional identity map", "comparison-table", [
        "IPCC -> scientific assessment by an intergovernmental body",
        "UNFCCC -> treaty framework and negotiation process",
        "COP OR CMA -> party decision-making forum",
        "NATIONAL GOVERNMENT -> policy and implementation",
        "RULE -> assessment evidence is not a negotiated obligation",
    ], [FACTS[0][0], FACTS[1][0], FACTS[12][0]]),
    panel("Assessment-production rail", "process-flow", [
        "PUBLISHED LITERATURE -> assessed evidence base",
        "AUTHORS -> evaluate findings, agreement and gaps",
        "DRAFTS -> expert and government review",
        "REVISION -> comments addressed and traceability strengthened",
        "PLENARY STATUS -> product-specific approval or acceptance",
    ], [FACTS[2][0], FACTS[9][0], FACTS[10][0], FACTS[11][0]]),
    panel("Three-Working-Group matrix", "comparison-table", [
        "WG I -> physical science, observations, drivers and projections",
        "WG II -> impacts, adaptation and vulnerability",
        "WG III -> mitigation pathways and enabling conditions",
        "NO NEGOTIATION -> none sets a Party's NDC",
        "INTEGRATION -> Synthesis Report joins assessment findings",
    ], [FACTS[3][0], FACTS[4][0], FACTS[5][0], FACTS[7][0]]),
    panel("TFI firewall", "hierarchy", [
        "IPCC BODY -> Task Force on National Greenhouse Gas Inventories",
        "FUNCTION -> methodology development and refinement",
        "OUTPUT -> inventory guidance and methodology reports",
        "NOT WG IV -> no fourth thematic assessment mandate",
        "LINK -> supports comparable national reporting methods",
    ], [FACTS[6][0], FACTS[8][0]]),
    panel("Report-family hierarchy", "hierarchy", [
        "ASSESSMENT CYCLE -> Working Group contributions",
        "SYNTHESIS REPORT -> integration across the cycle",
        "SPECIAL REPORT -> defined urgent theme",
        "METHODOLOGY REPORT -> measurement or inventory method",
        "STATUS -> title, outline and publication are different facts",
    ], [FACTS[7][0], FACTS[8][0], FACTS[9][0]]),
    panel("Cycle status gate", "decision-tree", [
        "SCOPING OR OUTLINE -> intended coverage",
        "AUTHORING -> draft evidence assessment",
        "REVIEW -> expert and government comments",
        "APPROVAL OR ACCEPTANCE -> product-specific plenary act",
        "PUBLICATION -> citable completed product",
    ], [FACTS[9][0], FACTS[10][0], FACTS[18][0]]),
    panel("SPM governance ladder", "layered-rail", [
        "SCIENTIST AUTHORS -> defend assessed basis",
        "GOVERNMENT DELEGATIONS -> consider wording line by line",
        "CONSISTENCY GATE -> summary must remain tied to report",
        "APPROVED SPM -> policy-relevant high-level text",
        "LIMIT -> not a treaty target or national law",
    ], [FACTS[11][0], FACTS[12][0]]),
    panel("Calibrated-language matrix", "comparison-table", [
        "CONFIDENCE -> evidence and agreement supporting a finding",
        "LIKELIHOOD -> assessed probability of a defined outcome",
        "SCALE -> global, regional and local claims differ",
        "ATTACHMENT -> term stays with its exact sentence",
        "NO BORROWING -> one calibrated term cannot validate another claim",
    ], [FACTS[13][0], FACTS[14][0], FACTS[15][0]]),
    panel("Scenario firewall", "decision-gate", [
        "ASSUMPTIONS -> socioeconomic or emissions pathway",
        "MODEL RESPONSE -> conditional climate projection",
        "RISK ASSESSMENT -> impacts under the stated pathway",
        "POLICY OPTION -> separately evaluated",
        "NOT FORECAST -> no unconditional prediction",
    ], [FACTS[16][0]]),
    panel("Assessment-lag timeline", "timeline", [
        "LITERATURE CUT-OFF -> evidence eligible for assessment",
        "DRAFT AND REVIEW -> synthesis takes time",
        "PUBLICATION -> completed assessment baseline",
        "NEW STUDIES -> may post-date the cut-off",
        "NEXT PRODUCT -> later incorporation is not automatic",
    ], [FACTS[17][0]]),
    panel("AR6-AR7 status board", "comparison-table", [
        "AR6 -> completed assessment cycle",
        "AR7 -> cycle in progress in official material checked",
        "OUTLINE -> planned coverage, not evidence",
        "SCHEDULE -> intended timing, not publication",
        "EXAM RULE -> cite report, year, group and status exactly",
    ], [FACTS[18][0], FACTS[19][0]]),
    panel("IPCC answer spine", "answer-spine", [
        "DEFINE -> assessment body, origin and non-research mandate",
        "ORGANISE -> WG I, WG II, WG III, TFI and Synthesis",
        "TRACE -> authors, review, SPM and product status",
        "QUALIFY -> confidence, likelihood, scenario and cut-off",
        "CONNECT -> informs UNFCCC but does not negotiate policy",
    ], [FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2023", "GS-III",
        "Discuss IPCC sea-level-rise assessment and impacts on the Indian Ocean region.",
        "Verified routed Mains demand; no unverified regional projection is supplied.",
        [0, 3, 4, 7, 13, 16, 17, 19],
    ),
]

TOPIC_18 = common.topic(
    18,
    "IPCC Assessment Reports",
    "18_IPCC-Assessment-Reports",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-18_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Explain the IPCC's assess-not-research mandate and institutional identity.", [0, 1, 2]),
        (10, "Differentiate the three Working Groups, TFI and Synthesis Report.", [3, 4, 5, 6, 7]),
        (15, "Explain the assessment cycle, review process and Summary for Policymakers.", [9, 10, 11, 12]),
        (15, "Distinguish IPCC confidence, likelihood, scenarios and projections.", [13, 14, 15, 16]),
        (20, "Evaluate the IPCC as a science-policy interface.", [0, 2, 7, 10, 11, 12, 13, 17]),
        (20, "Build a status-disciplined answer comparing completed and in-progress assessments.", [8, 9, 16, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "Intergovernmental Panel on Climate Change", "WMO", "UNEP",
        "does not conduct its own research", "Working Group I",
        "Working Group II", "Working Group III",
        "Task Force on National Greenhouse Gas Inventories",
        "Synthesis Report", "Special Report", "Methodology Report",
        "assessment cycle", "Summary for Policymakers",
        "policy-relevant", "policy-prescriptive", "confidence",
        "likelihood", "scenario", "forecast", "literature cut-off",
        "AR6", "AR7",
    ],
    (
        "Audited ledgers route the verified 2023 GS-III demand on an IPCC "
        "sea-level-rise prediction and Indian Ocean impacts. Recurring objective "
        "distinctions concern founding institutions, Working Group mandates, "
        "inventory methodology and the assess-not-research boundary. No "
        "unverified question, key, projection or model answer is inferred."
    ),
    PYQ_SOLUTIONS,
    IPCC_LIVE_SOURCE_ATTEMPTS,
    (
        "The official IPCC About page and AR7 page returned substantive process "
        "information. The AR6 landing page and glossary response were thin, and "
        "a Working Group URL redirected to an unrelated event. AR7 is recorded "
        "only as a cycle in progress; no planned report, outline, date, confidence "
        "term, likelihood threshold, scenario or projection was treated as a finding."
    ),
    extra=[
        "basic/17_Climate-Change-Science-Greenhouse-Effect.md",
        "basic/19_UNFCCC-COP-Kyoto-Paris-Agreement.md",
        "basic/24_Coastal-and-Marine-Ecology-CRZ-Blue-Economy.md",
        "advanced/17_Climate-Change-Science-Greenhouse-Effect.md",
        "advanced/24_Coastal-and-Marine-Ecology-CRZ-Blue-Economy.md",
    ],
    pyq_audit_heading="AUDITED IPCC ARCHITECTURE, ASSESSMENT AND SEA-LEVEL PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "IPCC BODY, WORKING GROUP, TFI AND REPORT-FAMILY MAP",
        "CYCLE, SPM, CONFIDENCE, LIKELIHOOD AND SCENARIO TRAPS",
        "IPCC SCIENCE-POLICY ANSWER SPINE",
        "LIVE REPORT, PUBLICATION, STATUS AND CALIBRATION EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "DEFINE THE IPCC AS AN ASSESSMENT BODY CREATED BY WMO AND UNEP",
        "STATE THAT IT ASSESSES PUBLISHED LITERATURE AND DOES NOT RESEARCH",
        "SEPARATE WG I, WG II, WG III, TFI AND THE SYNTHESIS REPORT",
        "TRACE SCOPE, AUTHORS, REVIEW, SPM AND PRODUCT-SPECIFIC STATUS",
        "DISTINGUISH CONFIDENCE FROM LIKELIHOOD",
        "LABEL SCENARIOS AND PROJECTIONS AS CONDITIONAL, NOT FORECASTS",
        "CONNECT IPCC EVIDENCE TO UNFCCC POLICY WITHOUT MERGING THEIR ROLES",
    ],
)
