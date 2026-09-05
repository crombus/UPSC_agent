"""Authored learner-v2 data for Disaster Management Topic 15."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.ipcc.ch/report/ar6/wg2/ — fetched 2026-09-04; IPCC "
        "described assessment of impacts, vulnerability and the capacities and "
        "limits of human and natural systems to adapt. "
        "https://www.undrr.org/implementing-sendai-framework/what-sendai-"
        "framework — fetched 2026-09-04 for the hazard-exposure-vulnerability-"
        "capacity risk framing."
    ),
    (
        "https://wmo.int/activities/climate-services — searched 2026-09-04; "
        "official WMO results described actionable climate information for "
        "agriculture, water, health, DRR and energy. "
        "https://imd.gov.in/ — searched 2026-09-04 as the Indian official "
        "climate-service route; no service-coverage or forecast-skill outcome "
        "was inferred."
    ),
    (
        "https://unfccc.int/wim-excom — searched 2026-09-04; official UNFCCC "
        "results identified the Warsaw International Mechanism Executive "
        "Committee and its current work route. "
        "https://www.mha.gov.in/en/commoncontent/disaster-management-act-2005 "
        "— attempted 2026-09-04 and returned HTTP 403; no international "
        "mechanism was converted into a domestic entitlement."
    ),
    (
        "https://unfccc.int/loss-and-damage-fund-joint-interim-secretariat — "
        "fetched 2026-09-04 but returned an Incapsula shell with no usable "
        "substantive text. https://pib.gov.in/ — searched 2026-09-04 for an "
        "Indian official corroboration route; no fund capitalisation, Indian "
        "access, disbursement or beneficiary outcome was used."
    ),
    (
        "https://unfccc.int/process-and-meetings/bodies/constituted-bodies/wim-"
        "excom/chronology — searched 2026-09-04; the official chronology route "
        "was located. https://nidm.gov.in/documentations.asp — searched "
        "2026-09-04 for domestic climate-risk material but supplied no "
        "additional current status proposition."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Climate disaster risk equation", "Climate-related disaster risk arises from the interaction of a hazard with exposure, vulnerability and capacity; a stronger climate signal does not by itself determine disaster loss."),
        ("Hazard exposure vulnerability", "Hazard is the potentially damaging event or trend, exposure is what is located in harm's way, and vulnerability is susceptibility to harm; policies can change the latter two even when the hazard cannot be eliminated."),
        ("Climate variability and climate change", "Climate variability describes fluctuations across seasons, years or longer natural modes, whereas anthropogenic climate change is a long-term human-influenced shift; a single event must not be attributed to either without appropriate evidence."),
        ("Attribution boundary", "Trend attribution, event attribution and disaster-loss attribution answer different questions: whether climate changed a hazard, whether it affected a particular event's likelihood or intensity, and why that event produced losses."),
        ("Mitigation adaptation and DRR", "Climate mitigation reduces greenhouse-gas-driven future change, adaptation adjusts systems to actual or expected impacts, and disaster risk reduction manages existing and prospective disaster risk; they overlap but are not interchangeable."),
        ("Incremental adaptation", "Incremental adaptation maintains the basic system while reducing risk through adjustments such as improved warnings, water efficiency, heat plans or protective standards."),
        ("Transformational adaptation", "Transformational adaptation changes fundamental attributes of a system when incremental measures cannot maintain acceptable risk, for example changing land use, livelihoods, settlement patterns or governance arrangements."),
        ("Maladaptation", "Maladaptation is an intervention that increases risk, emissions, inequality or future lock-in for some people, places or periods even if it produces a short-term benefit."),
        ("Residual risk", "Residual risk is the risk remaining after feasible mitigation, adaptation and DRR measures; its existence does not mean no further preparedness, protection or finance is possible."),
        ("Limits to adaptation", "A soft limit may be overcome through finance, technology, institutions or knowledge, while a hard limit cannot be avoided through adaptation within the system considered; limits are context-specific and evidence-dependent."),
        ("Loss and damage", "Loss and damage concerns adverse climate impacts that are not or cannot be fully avoided through mitigation and adaptation; it is not a synonym for every disaster loss, relief payment or adaptation project."),
        ("Avoid minimise address", "The UNFCCC loss-and-damage grammar distinguishes averting future loss, minimising unavoidable loss and addressing realised or residual impacts; each verb points to a different policy stage."),
        ("Economic loss and damage", "Economic loss and damage can be expressed in monetary terms, including damaged assets, production and income, while valuation method and baseline must remain explicit."),
        ("Non-economic loss and damage", "Non-economic loss and damage includes harms such as life, health, culture, identity, territory, biodiversity and social cohesion that may not be adequately represented by market valuation."),
        ("Warsaw International Mechanism", "The Warsaw International Mechanism was established under the UNFCCC loss-and-damage architecture to enhance knowledge, coordination and action and support; its existence does not prove delivery in a particular place."),
        ("Santiago Network and fund status", "The Santiago Network and the Fund for Responding to Loss and Damage belong to later institutional layers whose governance, access and operational status must be stated only from dated UNFCCC decisions and reports."),
        ("Climate services", "Climate services translate climate data, monitoring, forecasts and projections into usable information through co-design, communication and feedback; a model output alone is not a service or an adaptation outcome."),
        ("Locally led adaptation", "Locally led adaptation gives affected people meaningful decision power, predictable resources, accessible information and accountability while connecting local knowledge with technical and public institutions."),
        ("Displacement and justice", "Climate-related displacement can be temporary, prolonged, internal or cross-border; disaster-displaced persons are not automatically refugees, and protection must be analysed through applicable domestic, human-rights and humanitarian frameworks."),
        ("Mechanism-outcome firewall", "A plan, NAP, climate service, dialogue, network, fund decision or adaptation project proves its own status only; reduced vulnerability, avoided loss, equitable access and successful relocation require separate evidence."),
    ]
    traps = [
        "Do not infer disaster loss from hazard intensity alone.",
        "Do not use climate variability and anthropogenic climate change as synonyms.",
        "Do not attribute every flood, drought, cyclone or heat event to climate change.",
        "Do not collapse mitigation, adaptation and DRR into one policy category.",
        "Do not call every large adaptation project transformational.",
        "Do not present short-term protection that transfers risk as successful adaptation.",
        "Do not treat residual risk as proof that preparedness is futile.",
        "Do not use loss and damage as a synonym for all relief or insurance.",
        "Do not invent current UNFCCC fund access, corpus, disbursement or outcome.",
        "Do not equate consultation with locally led adaptation or a climate portal with climate-service use.",
    ]
    titles = [
        "Climate hazard exposure vulnerability capacity and disaster risk",
        "Climate variability anthropogenic change and attribution boundaries",
        "Mitigation adaptation and disaster risk reduction distinctions",
        "Incremental adaptation pathways and enabling conditions",
        "Transformational adaptation and system change",
        "Maladaptation risk transfer lock-in and unequal effects",
        "Residual risk soft limits and hard limits to adaptation",
        "Loss and damage definition and avoid minimise address grammar",
        "Economic and non-economic loss and damage",
        "Warsaw International Mechanism functions and status boundary",
        "Santiago Network fund decisions and verified-status discipline",
        "Climate services co-production communication and decision use",
        "Locally led adaptation participation finance and accountability",
        "Displacement justice ecosystems and vulnerable groups",
        "PYQ synthesis attribution adaptation and outcome firewall",
    ]
    routes = [
        "Begin with hazard exposure vulnerability and capacity, not hazard alone.",
        "Separate long-term signal event attribution and loss causation.",
        "Assign emission reduction adjustment and risk management correctly.",
        "Show how existing systems reduce risk without fundamental change.",
        "State why incremental measures fail before proposing transformation.",
        "Test distribution lock-in emissions and future risk.",
        "Distinguish remediable barriers from biophysical or system limits.",
        "Place averting minimising and addressing on a policy timeline.",
        "Use monetary and non-market categories without forced valuation.",
        "State knowledge coordination and action-support functions precisely.",
        "Use dated UNFCCC status and avoid entitlement or disbursement claims.",
        "Trace data to tailored information decision feedback and outcome.",
        "Test who decides who controls resources and who is accountable.",
        "Add protection mobility ecosystem and climate-justice dimensions.",
        "Conclude with evidence for vulnerability reduction and residual harm.",
    ]
    panels = [
        common.panel("Climate risk equation", "systems-map", [
            "CLIMATE HAZARD / TREND",
            "+ EXPOSURE + VULNERABILITY - CAPACITY",
            "-> DISASTER RISK",
            "HAZARD SIGNAL ALONE DOES NOT FIX LOSS",
        ], ["Climate disaster risk equation", "Hazard exposure vulnerability"]),
        common.panel("Attribution firewall", "comparison-table", [
            "VARIABILITY -> FLUCTUATION",
            "ANTHROPOGENIC CHANGE -> LONG-TERM HUMAN-INFLUENCED SHIFT",
            "EVENT ATTRIBUTION -> CHANGED LIKELIHOOD / INTENSITY?",
            "LOSS ATTRIBUTION -> WHY DID HARM OCCUR?",
        ], ["Climate variability and climate change", "Attribution boundary"]),
        common.panel("Three-policy map", "venn-map", [
            "MITIGATION -> REDUCE FUTURE CLIMATE CHANGE",
            "ADAPTATION -> ADJUST TO IMPACTS",
            "DRR -> MANAGE EXISTING / PROSPECTIVE DISASTER RISK",
            "OVERLAP EXISTS; PURPOSES REMAIN DISTINCT",
        ], ["Mitigation adaptation and DRR"]),
        common.panel("Adaptation pathway", "pathway-ladder", [
            "INCREMENTAL ADJUSTMENT",
            "-> MONITOR THRESHOLDS AND DISTRIBUTION",
            "-> TRANSFORMATION IF ACCEPTABLE RISK CANNOT BE MAINTAINED",
            "-> AVOID MALADAPTIVE LOCK-IN",
        ], ["Incremental adaptation", "Transformational adaptation", "Maladaptation"]),
        common.panel("Residual risk and limits", "decision-tree", [
            "RISK AFTER FEASIBLE ACTION -> RESIDUAL RISK",
            "BARRIER REMOVABLE? -> SOFT LIMIT",
            "NO ADAPTATION OPTION IN SYSTEM? -> HARD LIMIT",
            "PREPARE PROTECT FINANCE AND ADDRESS REMAINING HARM",
        ], ["Residual risk", "Limits to adaptation"]),
        common.panel("Avoid minimise address", "numbered-rail", [
            "1 AVERT -> MITIGATION / RISK AVOIDANCE",
            "2 MINIMISE -> ADAPTATION / DRR",
            "3 ADDRESS -> REALISED OR RESIDUAL IMPACT",
            "LOSS AND DAMAGE IS NOT EVERY DISASTER PAYMENT",
        ], ["Loss and damage", "Avoid minimise address"]),
        common.panel("Loss taxonomy", "comparison-table", [
            "ECONOMIC -> ASSETS OUTPUT INCOME; MONETARY METHOD",
            "NON-ECONOMIC -> LIFE HEALTH CULTURE IDENTITY ECOSYSTEMS",
            "BOTH -> DISTRIBUTION AND BASELINE MATTER",
            "DO NOT FORCE NON-MARKET HARM INTO ONE PRICE",
        ], ["Economic loss and damage", "Non-economic loss and damage"]),
        common.panel("UNFCCC status ladder", "status-ladder", [
            "WIM -> KNOWLEDGE COORDINATION ACTION / SUPPORT",
            "SANTIAGO NETWORK -> TECHNICAL-ASSISTANCE LAYER",
            "FUND -> DATED GOVERNANCE / ACCESS / OPERATIONAL STATUS ONLY",
            "DECISION != ACCESS != DISBURSEMENT != OUTCOME",
        ], ["Warsaw International Mechanism", "Santiago Network and fund status"]),
        common.panel("Climate-service chain", "process-flow", [
            "OBSERVE / MONITOR / FORECAST / PROJECT",
            "CO-DESIGN FOR USER DECISION",
            "COMMUNICATE UNCERTAINTY AND ACTION WINDOW",
            "USE + FEEDBACK + EVALUATE DECISION OUTCOME",
        ], ["Climate services"]),
        common.panel("Locally led test", "accountability-map", [
            "LOCAL PRIORITIES AND DECISION POWER",
            "PREDICTABLE ACCESSIBLE RESOURCES",
            "LOCAL + TECHNICAL KNOWLEDGE",
            "INCLUSION GRIEVANCE LEARNING AND ACCOUNTABILITY",
        ], ["Locally led adaptation"]),
        common.panel("Justice and mobility", "systems-map", [
            "UNEQUAL EXPOSURE / CAPACITY -> UNEQUAL HARM",
            "TEMPORARY / PROLONGED / INTERNAL / CROSS-BORDER MOVEMENT",
            "NON-AUTOMATIC REFUGEE STATUS",
            "PROTECTION LIVELIHOOD CULTURE AND DURABLE CHOICES",
        ], ["Displacement and justice"]),
        common.panel("Climate-risk answer spine", "answer-spine", [
            "DEFINE RISK -> FIX ATTRIBUTION BOUNDARY",
            "DISTINGUISH MITIGATION ADAPTATION DRR AND ADAPTATION PATHWAYS",
            "TRACE RESIDUAL RISK -> LOSS AND DAMAGE -> JUSTICE",
            "ADD CLIMATE SERVICES LOCAL LEADERSHIP + VERIFIED STATUS / OUTCOME",
        ], ["Mechanism-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss urban flooding as a climate-induced disaster and the policies and frameworks in India that aim at tackling it.",
            "Verified climate-risk application but Topic 08-owned; this card contributes attribution discipline, adaptation/DRR distinction, climate services and maladaptation safeguards.",
            [0, 1, 2, 3, 4, 7, 16, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, how it is determined and the elements of the Sendai Framework.",
            "Verified support route: climate risk, adaptation pathways, residual risk and local capacity illustrate resilience without converting Sendai into a climate treaty.",
            [0, 1, 4, 5, 6, 7, 8, 16, 17, 19]),
        common.make_pyq_solution(facts, "2025", "GS-III",
            "Review India's climate commitments under the Paris Agreement and the strengthening announced at COP26.",
            "Verified adjacent Environment/UNFCCC-owned route; this card supplies only adaptation, attribution and loss-and-damage distinctions and does not absorb NDC or mitigation-commitment detail.",
            [2, 3, 4, 8, 10, 11, 14, 15, 19]),
    ]
    return common.topic(
        15, "Climate Risk, Adaptation and Loss and Damage",
        "15_Climate-Risk-Adaptation-and-Loss-and-Damage", facts, traps,
        [
            (10, "Distinguish hazard, exposure, vulnerability and climate-change attribution.", [0, 1, 2, 3]),
            (10, "Differentiate mitigation, adaptation, disaster risk reduction and loss and damage.", [4, 8, 10, 11]),
            (15, "Explain incremental and transformational adaptation, maladaptation and limits to adaptation.", [5, 6, 7, 8, 9]),
            (15, "Analyse economic and non-economic loss and damage through the avoid-minimise-address framework.", [10, 11, 12, 13, 18]),
            (20, "Design a climate-risk governance framework integrating climate services, locally led adaptation and residual-risk protection.", [0, 1, 3, 4, 5, 7, 8, 9, 16, 17, 18, 19]),
            (20, "Critically evaluate whether current loss-and-damage institutions can address climate justice without causal and status overclaiming.", [3, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19]),
        ],
        titles, routes, panels,
        [
            "climate risk", "slow-onset", "mitigation", "adaptation",
            "disaster risk reduction", "residual risk", "Warsaw International Mechanism",
            "Suva Expert Dialogue", "Paris Agreement Article 8",
            "averting", "minimizing", "addressing", "displacement",
            "vulnerability", "attribution",
        ],
        "No audited 2024-2025 GS-III question directly owns the full topic. The 2024 urban-flood and resilience questions are bounded applications; the 2025 Paris question remains Environment/UNFCCC-owned and adjacent only.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered IPCC adaptation limits, UNDRR risk grammar, WMO climate services, IMD, UNFCCC WIM and loss-and-damage routes, plus domestic MHA/NIDM corroboration. The fund page was technically blocked; no capitalisation, access, disbursement, attribution, adaptation outcome or loss estimate was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "CLIMATE RISK ATTRIBUTION ADAPTATION PATHWAY AND LIMITS MAP",
            "MITIGATION DRR MALADAPTATION LOSS-DAMAGE AND STATUS FIREWALLS",
            "AVERT MINIMISE ADDRESS CLIMATE-SERVICE AND LOCAL-LEADERSHIP SPINE",
            "CURRENT IPCC UNDRR WMO IMD UNFCCC WIM AND FUND EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE HAZARD EXPOSURE VULNERABILITY CAPACITY AND CLIMATE RISK",
            "SEPARATE VARIABILITY TREND EVENT ATTRIBUTION AND LOSS CAUSATION",
            "DISTINGUISH MITIGATION ADAPTATION AND DISASTER RISK REDUCTION",
            "TRACE INCREMENTAL TRANSFORMATIONAL AND MALADAPTIVE PATHWAYS",
            "IDENTIFY RESIDUAL RISK SOFT / HARD LIMITS AND AVOID-MINIMISE-ADDRESS",
            "CLASSIFY ECONOMIC / NON-ECONOMIC LOSS AND PROTECT DISPLACED PEOPLE",
            "USE CLIMATE SERVICES LOCAL DECISION POWER AND DATED UNFCCC STATUS",
        ],
    )


TOPIC_15 = _build()
