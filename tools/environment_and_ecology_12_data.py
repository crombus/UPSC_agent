"""Authored data for Environment and Ecology learner-v2 Topic 12."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import (
    FOREST_GOVERNANCE_LIVE_SOURCE_ATTEMPTS,
    panel,
)


FACTS = [
    ("Diversion approval first", "Prior Central approval for specified non-forest use of covered forest land belongs to the forest-conservation statute; approval, rejection or exemption is a legal decision distinct from later compensatory-afforestation finance."),
    ("CAMPA trigger", "When an approved diversion carries compensatory conditions, the user agency pays the applicable compensatory-afforestation cost and Net Present Value; a fund flow does not itself grant diversion approval."),
    ("NPV distinction", "Net Present Value monetises specified foregone forest ecosystem services for the approval framework, while compensatory-afforestation cost finances plantation or restoration activity; the two payments are related but not identical."),
    ("CAF Act architecture", "The Compensatory Afforestation Fund Act, 2016 establishes National and State Compensatory Afforestation Funds and their authorities for receiving and using eligible monies under the statutory framework."),
    ("National authority boundary", "The National Authority and National Fund perform central planning, coordination, monitoring and nationally assigned functions; they do not replace State Authorities as the ordinary executors of state plans."),
    ("State authority boundary", "State Authorities prepare and implement the applicable annual plans and use State Fund resources for permitted activities; a release or approved plan is not proof of completed ecological restoration."),
    ("Fund-flow discipline", "An answer must trace user agency payment to the applicable fund, authority, approved plan, release, expenditure, physical output and ecological outcome; each is a separate accounting or performance stage."),
    ("Permitted-use boundary", "CAMPA monies may support compensatory afforestation and other permitted forest, wildlife, regeneration, protection or infrastructure activities under the Act and Rules; no allocation or expenditure value is assumed without the dated record."),
    ("Compensation limit", "A plantation cannot reproduce the structure, species composition, soil history, spatial location and accumulated services of a mature natural forest within the project accounting period; finance mitigates loss but does not prove ecological equivalence."),
    ("Site and tenure due diligence", "Compensatory-afforestation land must be checked for ecological suitability, native-biome fidelity, existing use and recognised or pending forest rights; describing land as degraded does not make it rights-free or ecologically empty."),
    ("Output versus outcome", "Money accrued, money spent, seedlings planted, area treated, canopy detected and ecosystem function restored are different metrics; none can be substituted for the next without monitoring evidence."),
    ("GIM policy identity", "The Green India Mission is one of the original eight missions under the National Action Plan on Climate Change and combines adaptation and mitigation through forest and ecosystem restoration; it is not the CAMPA statute."),
    ("GIM official targets", "The retrieved MoEFCC page publishes mission targets of increasing forest or tree cover over 5 million hectares, improving quality over another 5 million hectares and enhancing forest-based livelihood income for about 3 million families; these are targets, not verified achievements."),
    ("GIM ecosystem scope", "The official page emphasises biodiversity, water, biomass, mangroves, wetlands, critical habitats, carbon storage, agroforestry, social forestry and urban or peri-urban tree cover; GIM is broader than compensating one diverted parcel."),
    ("GIM convergence", "MoEFCC describes convergence with CAMPA and MGNREGS and a role for local communities; convergence is a planning approach, not automatic pooling of every fund or proof of implementation."),
    ("Mission-versus-CAMPA", "CAMPA is diversion-triggered statutory compensation finance, whereas GIM is a broader mission with ecosystem-service objectives and multiple implementation channels; overlap in activity does not make them one programme."),
    ("Forest-law vintage", "The Forest Conservation Amendment Act, 2023 renamed and altered the scope of the 1980 statute, while the Supreme Court's February 2024 interim direction preserved the broader Godavarman forest meaning pending State records; both must be stated together."),
    ("Green-credit boundary", "A green credit for an eligible environmental action is not a carbon credit and is not proof that a diverted mature ecosystem has been replaced; action registration, carbon accounting and ecological outcome are separate."),
    ("Audited PYQ ownership", "Audited ledgers route 2019 CAMPA, 2021 New York Declaration on Forests, 2021 Tree City and provisional 2026 Plan Vivo community-carbon demands to Topic 12; no objective key is inferred."),
    ("Live-data boundary", "Official CAMPA pages attempted on 2026-09-03 yielded HTTP 404 or DNS failure and the FSI page was a contact-only stub, so no fund, allocation, expenditure, afforestation-area, survival or outcome figure is asserted."),
]

TRAPS = [
    "Do not treat CAMPA payment as the legal approval for diversion.",
    "Do not merge NPV and compensatory-afforestation cost.",
    "Do not assign State implementation to the National Authority.",
    "Do not assign national coordination to a State Authority.",
    "Do not treat an approved annual plan as completed work.",
    "Do not report accrued funds as expenditure.",
    "Do not report expenditure as plantation survival or ecosystem restoration.",
    "Do not treat compensatory plantation as like-for-like mature forest.",
    "Do not assume degraded land is rights-free.",
    "Do not merge CAMPA and Green India Mission.",
    "Do not report GIM targets as achieved outputs or outcomes.",
    "Do not infer fund convergence from policy convergence.",
    "Do not state the 2023 amendment without the 2024 interim judicial direction.",
    "Do not equate green credit with carbon credit.",
    "Do not infer PYQ keys or current fund figures from stubs.",
]

SESSION_TITLES = [
    "Forest diversion approval and payment trigger",
    "NPV and compensatory-afforestation cost",
    "Compensatory Afforestation Fund Act architecture",
    "National Authority and Fund",
    "State Authorities and Funds",
    "Fund flow and permitted CAMPA uses",
    "Ecological non-equivalence of mature forest and plantation",
    "Site quality native biome and tenure due diligence",
    "Output versus outcome metrics",
    "Green India Mission identity",
    "Official GIM targets and ecosystem scope",
    "GIM CAMPA MGNREGS convergence",
    "CAMPA GIM distinction and forest-law vintage",
    "Green-credit boundary",
    "Audited PYQs and live-data boundary",
]

ANSWER_ROUTES = [
    "Begin with the legal decision, then trace conditions to user-agency payment.",
    "Separate ecosystem-service valuation from activity cost.",
    "Map the statute, funds and authorities before discussing implementation.",
    "Assign central planning and monitoring to the National layer.",
    "Assign state plans and execution to the State layer.",
    "Trace the fund stages and name only uses allowed by the Act, Rules and plan.",
    "Explain why restoration finance cannot establish like-for-like replacement.",
    "Test ecology, land tenure and pending rights before site selection.",
    "Separate accrual, expenditure, physical output and ecological outcome.",
    "Define GIM as a NAPCC mission, not a compensatory fund.",
    "Quote official targets as targets and connect them to ecosystem services.",
    "Treat convergence as coordinated planning rather than automatic fund merger.",
    "Distinguish CAMPA and GIM while stating the statute-court sequence.",
    "Keep green credit separate from carbon accounting and restoration proof.",
    "Close with answer-free PYQs and failed current fund-data attempts.",
]

PANELS = [
    panel("Diversion-to-finance firewall", "process-flow", [
        "PROJECT PROPOSAL -> forest-conservation legal scrutiny",
        "PRIOR CENTRAL APPROVAL OR EXEMPTION TEST -> legal decision",
        "CONDITIONS -> compensatory afforestation and NPV where applicable",
        "USER AGENCY PAYMENT -> finance trigger",
        "RULE -> payment never substitutes for approval",
    ], [FACTS[0][0], FACTS[1][0]]),
    panel("Payment distinction", "comparison-table", [
        "NPV -> specified ecosystem-service value in the approval framework",
        "CA COST -> finances compensatory plantation or restoration activity",
        "BOTH -> may arise from an approved diversion condition",
        "NEITHER -> evidence that ecological replacement has occurred",
        "VERIFY -> rate, category and date from the applicable order",
    ], [FACTS[1][0], FACTS[2][0]]),
    panel("Fund architecture", "hierarchy", [
        "CAF ACT 2016 -> statutory framework",
        "NATIONAL FUND -> centrally assigned receipts and uses",
        "NATIONAL AUTHORITY -> central planning, coordination and monitoring",
        "STATE FUND -> state-assigned receipts and uses",
        "STATE AUTHORITY -> annual plan and on-ground implementation",
    ], [FACTS[3][0], FACTS[4][0], FACTS[5][0]]),
    panel("National-State authority matrix", "comparison-table", [
        "NATIONAL -> coordination, national functions and oversight",
        "STATE -> plan preparation, execution and reporting",
        "TRANSFER OR RELEASE -> financial stage",
        "EXPENDITURE -> accounting stage",
        "OUTCOME -> ecological evidence stage",
    ], [FACTS[4][0], FACTS[5][0], FACTS[6][0]]),
    panel("Performance chain", "process-flow", [
        "ACCRUAL -> money received",
        "PLAN -> approved proposed activity",
        "RELEASE -> money made available",
        "EXPENDITURE -> money booked as spent",
        "OUTPUT AND OUTCOME -> physical work then ecological effect",
    ], [FACTS[6][0], FACTS[10][0]]),
    panel("Permitted-use gate", "decision-tree", [
        "PROPOSED ACTIVITY -> locate Act, Rules and annual plan authority",
        "PERMITTED USE -> afforestation or other eligible forest activity",
        "AUTHORITY -> National or State role",
        "RECORD -> dated sanction and expenditure evidence",
        "NO FIGURE -> never infer allocation, spend or area",
    ], [FACTS[7][0], FACTS[19][0]]),
    panel("Ecological equivalence test", "comparison-table", [
        "DIVERTED MATURE FOREST -> layered structure and accumulated history",
        "NEW PLANTATION -> young stand with different location and trajectory",
        "AREA MATCH -> administrative comparison only",
        "CANOPY GAIN -> does not prove biodiversity or hydrological recovery",
        "VERDICT -> compensation finance is not like-for-like replacement",
    ], [FACTS[8][0], FACTS[10][0]]),
    panel("Site and rights gate", "decision-gate", [
        "LAND IDENTIFIED -> verify legal and recorded status",
        "ECOLOGY -> match native biome, soil, water and connectivity",
        "TENURE -> check recognised and pending FRA rights",
        "COMMUNITY -> include rights holders in planning and monitoring",
        "NO EMPTY-LAND ASSUMPTION -> degraded does not mean unused",
    ], [FACTS[9][0]]),
    panel("GIM identity and scope", "layered-rail", [
        "NAPCC -> original eight-mission architecture",
        "GIM -> adaptation plus mitigation mission",
        "ECOSYSTEMS -> forests, wetlands, mangroves and critical habitats",
        "LANDSCAPES -> agroforestry, social forestry and urban tree cover",
        "LIVELIHOODS -> forest-dependent households and local communities",
    ], [FACTS[11][0], FACTS[13][0]]),
    panel("Target-versus-achievement gate", "decision-gate", [
        "OFFICIAL TARGET -> 5 mha cover increase",
        "OFFICIAL TARGET -> quality improvement over another 5 mha",
        "OFFICIAL TARGET -> livelihood income for about 3 million families",
        "ACHIEVEMENT CLAIM -> requires dated monitoring evidence",
        "RULE -> mission target is not actual output or outcome",
    ], [FACTS[12][0]]),
    panel("Convergence matrix", "comparison-table", [
        "GIM -> ecosystem-service mission objectives",
        "CAMPA -> diversion-triggered statutory finance",
        "MGNREGS -> eligible labour and asset channel",
        "CONVERGENCE -> align plans, sites and monitoring",
        "NO AUTOMATICITY -> institutions and accounts remain distinct",
    ], [FACTS[14][0], FACTS[15][0]]),
    panel("Law metric and PYQ spine", "answer-spine", [
        "LAW -> 2023 statute plus February 2024 interim direction",
        "FINANCE -> approval, NPV, CA cost and fund flow",
        "MISSION -> GIM targets separated from achievements",
        "METRIC -> accrual, spend, output and outcome kept distinct",
        "AUDIT -> objective PYQs and failed live figures remain answer-free",
    ], [FACTS[16][0], FACTS[17][0], FACTS[18][0], FACTS[19][0]]),
]

TOPIC_12 = common.topic(
    12,
    "Forest Governance CAMPA and Green India Mission",
    "12_Forest-Governance-CAMPA-and-Green-India-Mission",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-12_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Explain the sequence from forest-diversion approval to compensatory payments.", [0, 1, 2]),
        (10, "Distinguish the National and State Compensatory Afforestation Fund authorities.", [3, 4, 5, 6]),
        (15, "Explain why CAMPA performance must be tracked from accrual through ecological outcome.", [6, 7, 10, 19]),
        (15, "Distinguish Green India Mission from CAMPA and classify the official GIM targets correctly.", [11, 12, 13, 14, 15]),
        (20, "Critically examine the ecological equivalence and tenure assumptions in compensatory afforestation.", [8, 9, 10, 17]),
        (20, "Build a current forest-governance answer integrating law, CAMPA, GIM and evidence limits.", [0, 3, 6, 11, 12, 16, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "prior Central approval", "user agency", "Net Present Value",
        "compensatory-afforestation cost", "National Fund", "State Fund",
        "National Authority", "State Authority", "annual plan",
        "accrual", "expenditure", "ecological outcome", "Green India Mission",
        "original eight missions", "5 million hectares", "another 5 million hectares",
        "about 3 million families", "convergence", "green credit",
    ],
    (
        "Audited ledgers route four objective demands: CAMPA in 2019, the New "
        "York Declaration on Forests and Tree City in 2021, and provisional "
        "2026 Plan Vivo community forest carbon. No direct Mains demand or "
        "objective answer key is invented; the concepts are carried into practice."
    ),
    [],
    FOREST_GOVERNANCE_LIVE_SOURCE_ATTEMPTS,
    (
        "The official MoEFCC GIM page was substantively retrieved for mission "
        "identity, ecosystem scope, convergence and published targets. Those "
        "targets are not reported as achievements. CAMPA paths failed with "
        "HTTP 404 or DNS error and the FSI page was a contact-only stub, so no "
        "fund, allocation, expenditure, area, survival or outcome figure was used."
    ),
    extra=[
        "basic/03_Ecological-Succession-and-Biomes.md",
        "basic/11_Forest-Types-and-Forest-Rights-Act.md",
        "basic/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md",
        "advanced/11_Forest-Types-and-Forest-Rights-Act.md",
        "advanced/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md",
    ],
    pyq_audit_heading="AUDITED CAMPA, FOREST-POLICY AND COMMUNITY-CARBON PYQ OWNERSHIP",
    register_headings=(
        "DIVERSION, NPV, CA COST, FUND AND AUTHORITY MAP",
        "CAMPA, GIM, TARGET, TENURE, METRIC AND EQUIVALENCE TRAPS",
        "FOREST-GOVERNANCE ANSWER SPINE",
        "LIVE FUND, EXPENDITURE, AREA, OUTCOME AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "START WITH THE FOREST-DIVERSION APPROVAL OR EXEMPTION QUESTION",
        "SEPARATE NPV FROM COMPENSATORY-AFFORESTATION COST",
        "TRACE NATIONAL AND STATE FUND-AUTHORITY ROLES",
        "MOVE FROM ACCRUAL TO PLAN TO RELEASE TO SPEND TO OUTPUT TO OUTCOME",
        "DISTINGUISH CAMPA'S TRIGGER FROM GIM'S MISSION OBJECTIVES",
        "LABEL EVERY GIM NUMBER AS TARGET OR DATED ACHIEVEMENT",
        "CONCLUDE WITH NATIVE-BIOME, FRA AND LONG-TERM MONITORING SAFEGUARDS",
    ],
)
