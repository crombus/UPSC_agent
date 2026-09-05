"""Authored data for Environment and Ecology learner-v2 Topic 16."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import EIA_NGT_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Prior EC boundary", "Prior environmental clearance is a project-appraisal decision required before the prohibited starting point under the applicable notification; it is not a post-construction certificate of impact management."),
    ("EC and consent boundary", "Environmental clearance and Consent to Establish or Operate arise from different instruments and authorities; possession of one does not grant or prove the other."),
    ("Multiple-clearance boundary", "Environmental, forest, wildlife and coastal clearances protect different legal interests; one approval cannot be treated as a substitute for all others."),
    ("Schedule applicability", "The first EIA question is whether the proposed project or activity falls within the current notification and schedule; not every project automatically requires the same appraisal route."),
    ("Category A and B boundary", "Category A and Category B allocation determines the competent appraisal level under the owner, but the current schedule and thresholds must be checked before classifying a real project."),
    ("B1 and B2 boundary", "The B1-B2 distinction affects assessment and consultation requirements under the applicable notification; it must not be guessed from project size or label without the owner and current schedule."),
    ("Screening boundary", "Screening determines the applicable assessment route where the notification requires it; it is distinct from scoping, public consultation, appraisal and the final clearance decision."),
    ("Scoping and terms of reference", "Scoping identifies the significant issues and terms of reference for study; it does not itself grant clearance or establish that baseline evidence is adequate."),
    ("Assessment evidence", "A credible EIA examines baseline conditions, alternatives, likely impacts, mitigation and an environmental management plan; prediction remains bounded by data quality and assumptions."),
    ("Public-consultation boundary", "Public consultation is a defined process for applicable projects, not a universal stage without exceptions; every claimed exemption, notice period or hearing rule must be tied to the current notification."),
    ("Appraisal and decision", "An expert committee appraises the record and recommends a decision, while the competent authority grants, conditions or rejects clearance; recommendation and final order are distinct."),
    ("Post-clearance compliance", "A granted clearance and listed conditions are inputs to compliance monitoring; neither proves that safeguards were implemented or environmental outcomes achieved."),
    ("NGT statutory identity", "The National Green Tribunal is a specialised statutory adjudicatory body under the NGT Act, 2010; it is not the pollution-control regulator or the project appraisal committee."),
    ("Original-jurisdiction boundary", "NGT original jurisdiction concerns substantial environmental questions arising from the enactments within its statutory boundary; an environment-related label alone does not create jurisdiction."),
    ("Appellate-jurisdiction boundary", "NGT appellate jurisdiction attaches to specified appealable decisions under the governing statutes; it is distinct from original civil jurisdiction and constitutional writ review."),
    ("Remedy boundary", "Relief or compensation to affected persons, restitution of property and restitution of the environment are distinct statutory remedies; a remedy must match jurisdiction and evidence."),
    ("Principles and adjudication", "Sustainable development, precaution and polluter-pays guide NGT adjudication within the Act; they do not erase statutory jurisdiction, procedure or proof requirements."),
    ("Limitation discipline", "Original applications, compensation claims and statutory appeals can have different limitation clocks and extension rules; no period is stated without the exact provision and remedy."),
    ("Constitutional-court boundary", "The NGT does not replace Supreme Court or High Court constitutional jurisdiction; tribunal review, statutory appeal and writ review remain distinct routes."),
    ("Instrument and evidence boundary", "An EIA notification, draft proposal, amendment, office memorandum, clearance order and judgment have different legal force; audited PYQs and live pages are used without inventing thresholds, exemptions, penalties or current claims."),
]

TRAPS = [
    "Do not merge prior environmental clearance with CTE or CTO.",
    "Do not treat environmental clearance as forest, wildlife or coastal clearance.",
    "Do not assume every project follows the same EIA route.",
    "Do not assign Category A, B, B1 or B2 without the current schedule.",
    "Do not merge screening with scoping or appraisal.",
    "Do not treat terms of reference as project approval.",
    "Do not assume public consultation has no project-specific exceptions.",
    "Do not treat an expert recommendation as the final clearance order.",
    "Do not treat clearance conditions as proof of compliance.",
    "Do not call NGT a pollution-control board or appraisal committee.",
    "Do not assume unlimited NGT jurisdiction over every environmental dispute.",
    "Do not merge original and appellate jurisdiction.",
    "Do not merge compensation, property restitution and environmental restitution.",
    "Do not quote one limitation period for every NGT remedy.",
    "Do not present a draft or office memorandum as a final notification or judgment.",
]

SESSION_TITLES = [
    "Prior environmental clearance and starting-point rule",
    "EC consent forest wildlife and coastal boundaries",
    "Schedule applicability and project classification",
    "Category A and Category B appraisal level",
    "B1 B2 and current-schedule discipline",
    "Screening and route determination",
    "Scoping terms of reference and study design",
    "Baseline alternatives impacts mitigation and EMP",
    "Public consultation applicability and quality",
    "Appraisal recommendation and clearance decision",
    "Post-clearance conditions and compliance monitoring",
    "NGT statutory identity and original jurisdiction",
    "NGT appellate jurisdiction and remedies",
    "Principles limitation and constitutional courts",
    "Instrument hierarchy and evidence-safe synthesis",
]

ANSWER_ROUTES = [
    "Start with whether prior EC applies and identify the prohibited starting point.",
    "List every approval separately with its statute, authority and purpose.",
    "Read the current schedule before assigning an appraisal route.",
    "Use Category A or B only for the competent-level distinction supported by the owner.",
    "Treat B1 and B2 as notification-specific assessment routes, never intuition.",
    "Explain screening as route determination rather than final approval.",
    "Connect scoping to terms of reference and significant-impact selection.",
    "Test baseline, alternatives, prediction, mitigation and management as one evidence chain.",
    "State consultation applicability, access and response without inventing exemptions.",
    "Separate expert recommendation from the competent authority's final order.",
    "Move from condition to monitoring, compliance evidence and corrective action.",
    "Define NGT and then locate the substantial question within its statutory boundary.",
    "Identify whether the case is an appeal and match the remedy to the provision.",
    "Apply principles within jurisdiction and date the correct limitation route.",
    "Close by ranking statute, notification, amendment, order, memorandum and judgment correctly.",
]

PANELS = [
    panel("Prior-clearance firewall", "process-flow", [
        "PROJECT CONCEPT -> test EIA schedule applicability",
        "PRIOR EC REQUIRED -> appraisal before prohibited start",
        "CONDITIONAL GRANT OR REJECTION -> competent authority decision",
        "CONSTRUCTION OR OPERATION -> only under applicable approvals",
        "RULE -> later paperwork cannot recreate prior appraisal",
    ], [FACTS[0][0], FACTS[3][0]]),
    panel("Approval matrix", "comparison-table", [
        "ENVIRONMENTAL CLEARANCE -> project impact appraisal",
        "CTE OR CTO -> pollution-control consent",
        "FOREST CLEARANCE -> forest-law decision",
        "WILDLIFE OR CRZ APPROVAL -> separate legal interest",
        "NO SUBSTITUTION -> each approval retains its own test",
    ], [FACTS[1][0], FACTS[2][0]]),
    panel("Classification gate", "decision-tree", [
        "PROJECT OR ACTIVITY -> read current schedule",
        "THRESHOLD AND LOCATION -> apply notified criteria",
        "CATEGORY A OR B -> competent appraisal level",
        "B1 OR B2 -> assessment route only where supported",
        "NO GUESS -> title or size alone is insufficient",
    ], [FACTS[3][0], FACTS[4][0], FACTS[5][0]]),
    panel("Four-process distinction", "comparison-table", [
        "SCREENING -> determine applicable route where required",
        "SCOPING -> set significant issues and terms of reference",
        "PUBLIC CONSULTATION -> receive affected and stakeholder concerns",
        "APPRAISAL -> expert review of the full record",
        "DECISION -> competent authority grants, conditions or rejects",
    ], [FACTS[6][0], FACTS[7][0], FACTS[9][0], FACTS[10][0]]),
    panel("EIA evidence chain", "process-flow", [
        "BASELINE -> existing environmental and social condition",
        "ALTERNATIVES -> site, technology and no-project comparison",
        "IMPACT PREDICTION -> magnitude, duration and uncertainty",
        "MITIGATION -> avoid, minimise, restore or compensate",
        "EMP AND MONITORING -> implementation and verification",
    ], [FACTS[8][0]]),
    panel("Consultation quality gate", "decision-gate", [
        "APPLICABILITY -> read current notification",
        "NOTICE AND ACCESS -> affected people can inspect material",
        "HEARING OR WRITTEN RESPONSE -> collect concerns",
        "APPRAISAL RESPONSE -> show how issues were considered",
        "EXEMPTION CLAIM -> cite exact provision or do not assert it",
    ], [FACTS[9][0]]),
    panel("Recommendation-decision ladder", "hierarchy", [
        "PROJECT RECORD -> EIA, EMP and consultation material",
        "EXPERT COMMITTEE -> appraisal and recommendation",
        "COMPETENT AUTHORITY -> final reasoned order",
        "CONDITIONS -> enforceable project obligations",
        "MONITORING -> evidence after grant",
    ], [FACTS[10][0], FACTS[11][0]]),
    panel("Grant-to-outcome chain", "layered-rail", [
        "CLEARANCE GRANTED -> legal decision",
        "CONDITION LISTED -> required safeguard",
        "ACTION IMPLEMENTED -> physical compliance",
        "MONITORING VERIFIED -> evidence stage",
        "OUTCOME -> environmental result, separately assessed",
    ], [FACTS[11][0]]),
    panel("NGT identity map", "comparison-table", [
        "NGT -> specialised statutory tribunal",
        "CPCB OR SPCB -> pollution-control regulator",
        "EAC OR SEAC -> appraisal committee",
        "CLEARANCE AUTHORITY -> administrative decision-maker",
        "CONSTITUTIONAL COURT -> writ and appellate constitutional role",
    ], [FACTS[12][0], FACTS[18][0]]),
    panel("Jurisdiction fork", "decision-tree", [
        "SUBSTANTIAL ENVIRONMENTAL QUESTION -> test Schedule I boundary",
        "ORIGINAL CASE -> civil environmental dispute under the Act",
        "APPEAL -> specified order and appeal provision",
        "WRIT ROUTE -> separate constitutional review",
        "NO LABEL-BASED JURISDICTION -> statute controls",
    ], [FACTS[13][0], FACTS[14][0], FACTS[18][0]]),
    panel("Remedy and limitation matrix", "comparison-table", [
        "RELIEF OR COMPENSATION -> person or damage claim",
        "PROPERTY RESTITUTION -> restore affected property",
        "ENVIRONMENT RESTITUTION -> repair environmental harm",
        "LIMITATION -> remedy-specific clock and extension",
        "PRINCIPLES -> apply within jurisdiction and evidence",
    ], [FACTS[15][0], FACTS[16][0], FACTS[17][0]]),
    panel("Instrument and answer spine", "answer-spine", [
        "PREVENT -> applicability, category, study and consultation",
        "DECIDE -> appraisal, reasoned order and distinct approvals",
        "MONITOR -> conditions, compliance and environmental outcome",
        "REMEDY -> NGT jurisdiction, appeal, relief and limitation",
        "AUDIT -> draft, notification, memorandum, judgment and PYQ status",
    ], [FACTS[19][0]]),
]

TOPIC_16 = common.topic(
    16,
    "Environmental Impact Assessment and NGT",
    "16_Environmental-Impact-Assessment-and-NGT",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-16_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish prior environmental clearance from pollution-control consent.", [0, 1, 2]),
        (10, "Explain screening, scoping, public consultation and appraisal.", [6, 7, 9, 10]),
        (15, "Assess the evidence chain from baseline study to post-clearance monitoring.", [8, 9, 10, 11]),
        (15, "Distinguish NGT original and appellate jurisdiction.", [12, 13, 14, 18]),
        (20, "Evaluate India's preventive EIA and corrective NGT architecture.", [0, 3, 6, 8, 11, 12, 15, 16]),
        (20, "Build a legally disciplined project-clearance and remedy answer.", [1, 2, 4, 5, 9, 13, 14, 17, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "prior environmental clearance", "Consent to Establish",
        "CTO", "forest clearance", "wildlife",
        "CRZ clearance", "schedule applicability", "Category A", "Category B",
        "B1", "B2", "screening", "scoping", "terms of reference",
        "baseline", "alternatives", "public consultation", "appraisal",
        "post-clearance compliance", "National Green Tribunal",
        "original jurisdiction", "appellate jurisdiction", "Schedule I",
        "compensation", "restitution", "limitation", "draft notification",
    ],
    (
        "Audited ledgers route direct Mains demands on EIA reform, NGO and "
        "activist influence, mining hazards and constitutional environmental "
        "adjudication, plus objective distinctions between NGT and CPCB and "
        "Environment Protection Act powers. No answer key is inferred."
    ),
    [],
    EIA_NGT_LIVE_SOURCE_ATTEMPTS,
    (
        "MoEFCC pages substantively supported only the preventive appraisal "
        "function and the NGT's statutory identity. PARIVESH and NGT FAQ pages "
        "were title-only, India Code returned HTTP 403 and the NGT home page "
        "failed at transport level. No project threshold, category, exemption, "
        "clearance stage, limitation period, penalty or current case claim was imported."
    ),
    extra=[
        "basic/01_Ecosystem-Structure-and-Function.md",
        "basic/06_Protected-Area-Network-India.md",
        "basic/13_Air-Pollution-and-CPCB-Standards.md",
        "basic/14_Water-Pollution-and-River-Cleaning-Missions.md",
        "basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
        "advanced/06_Protected-Area-Network-India.md",
        "advanced/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
    ],
    pyq_audit_heading="AUDITED EIA, CLEARANCE, NGT AND ENVIRONMENTAL-JUSTICE PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "PRIOR EC, DISTINCT APPROVALS, CATEGORY AND PROCESS MAP",
        "CONSULTATION, COMPLIANCE, JURISDICTION, REMEDY AND LIMITATION TRAPS",
        "EIA-NGT GOVERNANCE ANSWER SPINE",
        "LIVE THRESHOLD, EXEMPTION, PENALTY, CASE AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "TEST EIA SCHEDULE APPLICABILITY BEFORE CLASSIFYING THE PROJECT",
        "SEPARATE PRIOR EC, CTE, CTO, FOREST, WILDLIFE AND CRZ APPROVALS",
        "TRACE SCREENING, SCOPING, CONSULTATION, APPRAISAL AND DECISION",
        "TEST BASELINE, ALTERNATIVES, MITIGATION, EMP AND COMPLIANCE",
        "DISTINGUISH NGT ORIGINAL AND APPELLATE JURISDICTION",
        "MATCH RELIEF, COMPENSATION, RESTITUTION AND LIMITATION TO THE REMEDY",
        "CONCLUDE WITH PREVENTION, REASONED DECISION AND ENFORCEABLE MONITORING",
    ],
)
