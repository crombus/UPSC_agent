"""Authored learner-v2 data for Disaster Management Topic 17."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://ndrf.gov.in/en/about-us — fetched 2026-09-04; NDRF described "
        "specialised response, proactive availability and pre-positioning. "
        "https://ndma.gov.in/ — attempted 2026-09-04; the portal route was not "
        "usable, so NDMA guideline titles and dates remain owner-bounded."
    ),
    (
        "https://www.unocha.org/we-coordinate — fetched 2026-09-04; OCHA "
        "described UNDAC assessment/coordination on request and OSOCC as a link "
        "between international responders and the affected government. "
        "https://www.mha.gov.in/en/commoncontent/disaster-management-act-2005 "
        "— attempted 2026-09-04 and returned HTTP 403."
    ),
    (
        "https://www.who.int/health-topics/emergencies — fetched 2026-09-04 "
        "but returned only a thin emergencies page. "
        "https://www.wfp.org/emergencies — fetched 2026-09-04 and redirected "
        "to a general country-office description. https://pib.gov.in/ — "
        "searched 2026-09-04; no logistics performance figure was imported."
    ),
    (
        "https://www.ifrc.org/our-work/disasters-climate-and-crises — fetched "
        "2026-09-04; IFRC framed preparedness as readiness to respond, recover "
        "and learn. https://nidm.gov.in/documentations.asp — searched "
        "2026-09-04; no additional current last-mile or recovery outcome was "
        "used."
    ),
    (
        "https://www.ifrc.org/document/sphere-handbook-humanitarian-charter-and-"
        "minimum-standards-humanitarian-response — attempted 2026-09-04 and "
        "returned HTTP 403. https://ndma.gov.in/Resources/awareness — attempted "
        "2026-09-04; no usable text was returned, so no unverified numerical "
        "minimum standard was reproduced."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Response relief rehabilitation reconstruction recovery", "Response is the immediate operational effort, relief meets urgent survival needs, rehabilitation restores basic functioning, reconstruction restores or replaces systems more fully, and recovery is the wider process across these phases."),
        ("Needs assessment", "A rapid needs assessment identifies affected people, severity, priority needs, access constraints, local capacity and uncertainty; it must be updated because the first picture is incomplete."),
        ("Humanitarian principles", "Humanity prioritises life and dignity, impartiality allocates by need without adverse distinction, neutrality avoids taking sides, and operational independence protects humanitarian objectives; each principle addresses a different decision."),
        ("Preparedness and pre-positioning", "Forecast-based pre-positioning of trained teams, stocks, transport, shelters and communications can shorten response where lead time exists; readiness for sudden-onset hazards relies more on standing capacity and distributed stocks."),
        ("Procurement", "Emergency procurement must balance speed, quality, price, local-market effects, conflict of interest, traceability and supplier reliability; waiving ordinary timelines does not waive accountability."),
        ("Warehousing and inventory", "Warehousing requires suitable location, hazard safety, stock rotation, batch and expiry control, inventory visibility, handling capacity, security and planned replenishment."),
        ("Transport and routing", "Transport planning selects modes, hubs, routes and alternates using access, capacity, fuel, weather, security and infrastructure status; the fastest nominal route may not be the most reliable."),
        ("Last-mile distribution", "Last-mile distribution converts bulk supply into safe, timely and accessible delivery through verified beneficiary information, transparent schedules, queue management, outreach and feedback."),
        ("Information and coordination", "A common operating picture should distinguish verified needs, requests, commitments, dispatch, receipt and distribution while protecting personal data and preventing duplicate or uncovered assistance."),
        ("Cash versus in-kind", "Cash can support choice and local markets where goods, access, prices, payments and protection conditions permit; in-kind aid is preferable where markets or payment systems fail or specific commodities must be assured."),
        ("Shelter WASH health and protection", "Shelter, water, sanitation and hygiene, health, nutrition and protection are interdependent minimum service domains; numerical standards should be cited only from the applicable verified guideline and context."),
        ("Protection and inclusion", "Relief design must address gender-based violence, child protection, disability access, older people, separated families, documentation loss, trafficking risk, privacy and safe complaint channels."),
        ("Grievance and anti-diversion controls", "Public criteria, receipt and stock records, segregation of duties, spot checks, community monitoring, confidential complaints and corrective action reduce exclusion, duplication, theft and diversion."),
        ("Livelihood restoration", "Livelihood recovery moves beyond consumption relief to restore assets, skills, credit, market access, public works, social protection and ecosystem dependence without recreating unsafe exposure."),
        ("Displacement and durable solutions", "Displaced people require protection and informed choice among safe return, local integration or relocation where applicable; a camp closure or physical return is not proof of a durable solution."),
        ("Debris and environmental recovery", "Debris management should classify hazardous and reusable material, protect workers and communities, clear priority access, identify lawful sites and avoid shifting contamination or flood risk."),
        ("Recovery sequencing", "Recovery sequencing first protects life and continuity, then restores temporary services and livelihoods, and finally undertakes risk-informed reconstruction while resolving land, finance, environmental and institutional constraints."),
        ("Incident coordination and handover", "India's Incident Response System supports defined response roles and coordination, while the generic Incident Command System supplies a management model; emergency arrangements must hand over transparently to normal administration for longer recovery."),
        ("Build Back Better", "Build Back Better integrates risk reduction into recovery, rehabilitation and reconstruction through safer siting, standards, redundancy, livelihoods, ecosystems and governance rather than merely rebuilding faster."),
        ("Delivery-outcome firewall", "A warehouse stock, dispatched truck, cash transfer, camp, guideline, team deployment or reconstruction sanction proves an input or transaction; receipt, adequacy, safety, inclusion, livelihood recovery and lower future risk need separate evidence."),
    ]
    traps = [
        "Do not use response, relief, rehabilitation, reconstruction and recovery interchangeably.",
        "Do not treat the first rapid assessment as a final beneficiary list.",
        "Do not sacrifice humanitarian principles or accountability to speed.",
        "Do not infer delivery from dispatch or adequacy from tonnage.",
        "Do not assume cash is always superior to in-kind assistance.",
        "Do not reproduce unverified universal numerical minimum standards.",
        "Do not expose personal or protection-sensitive data in coordination systems.",
        "Do not call return or camp closure a durable solution automatically.",
        "Do not dump debris or contamination into another community or hazard path.",
        "Do not call reconstruction Build Back Better without safer systems and livelihoods.",
    ]
    titles = [
        "Response relief rehabilitation reconstruction and recovery distinctions",
        "Rapid and iterative needs assessment",
        "Humanity impartiality neutrality and operational independence",
        "Anticipatory pre-positioning and sudden-onset readiness",
        "Emergency procurement supplier quality and audit trail",
        "Warehousing inventory rotation security and replenishment",
        "Transport hubs routing alternates and access constraints",
        "Last-mile distribution queues outreach and receipt verification",
        "Information coordination common operating picture and privacy",
        "Cash in-kind and local-market choice",
        "Shelter WASH health nutrition and protection integration",
        "Grievance anti-diversion and community accountability",
        "Livelihood restoration displacement and durable solutions",
        "Debris environment recovery sequencing and handover",
        "PYQ synthesis Build Back Better and delivery-outcome firewall",
    ]
    routes = [
        "Define each post-impact phase by objective and handover.",
        "State who what where severity access capacity and uncertainty.",
        "Apply principles to targeting access communication and negotiation.",
        "Match pre-positioning to forecast lead time and standing readiness.",
        "Balance speed quality market effect traceability and conflict controls.",
        "Protect stock quality visibility handling security and rotation.",
        "Plan multimodal primary and alternate routes with live access data.",
        "Trace dispatch receipt accessible distribution feedback and correction.",
        "Separate need request commitment dispatch receipt and coverage.",
        "Test market supply prices access payments safety and preference.",
        "Integrate services and cite only verified context-specific standards.",
        "Make criteria records complaints investigation and correction visible.",
        "Restore assets markets services and voluntary durable choices.",
        "Sequence safe clearance temporary service normal handover and rebuilding.",
        "Conclude with received adequate inclusive aid and safer recovery evidence.",
    ]
    panels = [
        common.panel("Post-impact phase rail", "numbered-rail", [
            "1 RESPONSE -> LIFE-SAVING OPERATIONS",
            "2 RELIEF -> URGENT SURVIVAL NEEDS",
            "3 REHABILITATION -> BASIC FUNCTION",
            "4 RECONSTRUCTION / RECOVERY -> FULLER RISK-INFORMED RESTORATION",
        ], ["Response relief rehabilitation reconstruction recovery"]),
        common.panel("Needs-assessment loop", "feedback-loop", [
            "WHO / WHERE / SEVERITY / PRIORITY NEED",
            "ACCESS + LOCAL CAPACITY + PROTECTION RISK",
            "VERIFY / DISAGGREGATE / STATE UNCERTAINTY",
            "DELIVER -> FEEDBACK -> UPDATE",
        ], ["Needs assessment"]),
        common.panel("Humanitarian principles compass", "compass-map", [
            "HUMANITY -> LIFE AND DIGNITY",
            "IMPARTIALITY -> NEED WITHOUT ADVERSE DISTINCTION",
            "NEUTRALITY -> DO NOT TAKE SIDES",
            "INDEPENDENCE -> HUMANITARIAN OBJECTIVE GOVERNS",
        ], ["Humanitarian principles"]),
        common.panel("Anticipatory logistics split", "comparison-table", [
            "FORECASTABLE -> PRE-POSITION TEAMS STOCK SHELTER TRANSPORT",
            "SUDDEN-ONSET -> DISTRIBUTED STOCK + STANDING READINESS",
            "BOTH -> COMMUNICATION ALTERNATES AND LOCAL PARTNERS",
            "WARNING / DEPLOYMENT DOES NOT GUARANTEE REACH",
        ], ["Preparedness and pre-positioning"]),
        common.panel("Supply-chain rail", "process-flow", [
            "NEED -> PROCURE -> WAREHOUSE",
            "-> TRANSPORT / HUB / ALTERNATE ROUTE",
            "-> LAST-MILE DISTRIBUTE -> VERIFY RECEIPT",
            "-> FEEDBACK REPLENISH AND CORRECT",
        ], ["Procurement", "Warehousing and inventory", "Transport and routing", "Last-mile distribution"]),
        common.panel("Information board", "status-board", [
            "VERIFIED NEED | REQUEST | COMMITMENT",
            "DISPATCH | RECEIPT | DISTRIBUTION",
            "GAP / DUPLICATION / ACCESS CONSTRAINT",
            "MINIMUM NECESSARY PERSONAL DATA + ACCOUNTABLE UPDATE",
        ], ["Information and coordination"]),
        common.panel("Cash or in-kind gate", "decision-tree", [
            "ARE GOODS AVAILABLE AND MARKETS FUNCTIONING?",
            "ARE PRICES ACCESS PAYMENTS AND PROTECTION ACCEPTABLE?",
            "YES -> CASH / VOUCHER MAY SUPPORT CHOICE",
            "NO / SPECIFIC ASSURANCE NEEDED -> IN-KIND OR MIXED",
        ], ["Cash versus in-kind"]),
        common.panel("Minimum-service web", "network-map", [
            "SHELTER <-> WASH <-> HEALTH / NUTRITION",
            "PROTECTION / PRIVACY / ACCESSIBILITY THROUGH ALL",
            "COMMUNITY INFORMATION + REFERRAL",
            "NUMERIC STANDARD ONLY FROM VERIFIED APPLICABLE SOURCE",
        ], ["Shelter WASH health and protection", "Protection and inclusion"]),
        common.panel("Accountability controls", "control-matrix", [
            "PUBLIC CRITERIA + SEGREGATED DUTIES",
            "STOCK / RECEIPT / BENEFICIARY RECORD",
            "SPOT CHECK + COMMUNITY MONITOR",
            "SAFE GRIEVANCE -> INVESTIGATE -> CORRECT",
        ], ["Grievance and anti-diversion controls"]),
        common.panel("Recovery choices", "systems-map", [
            "LIVELIHOOD ASSETS SKILLS CREDIT MARKET SOCIAL PROTECTION",
            "DISPLACEMENT -> RETURN / LOCAL INTEGRATION / RELOCATION CHOICE",
            "DEBRIS -> CLASSIFY REUSE DISPOSE SAFELY",
            "RESTORE WITHOUT RECREATING EXPOSURE OR EXCLUSION",
        ], ["Livelihood restoration", "Displacement and durable solutions", "Debris and environmental recovery"]),
        common.panel("Sequencing and handover", "timeline", [
            "LIFE + CONTINUITY",
            "-> TEMPORARY SERVICES / LIVELIHOODS",
            "-> IRS RESPONSE HANDOVER TO NORMAL ADMINISTRATION",
            "-> LONG-TERM RISK-INFORMED RECONSTRUCTION",
        ], ["Recovery sequencing", "Incident coordination and handover"]),
        common.panel("Humanitarian answer spine", "answer-spine", [
            "ASSESS ITERATIVELY -> PRE-POSITION / PROCURE / STORE / MOVE",
            "DISTRIBUTE BY NEED WITH PRINCIPLES PROTECTION AND GRIEVANCE",
            "RESTORE SERVICES LIVELIHOODS AND DURABLE DISPLACEMENT CHOICES",
            "HAND OVER -> BUILD BACK BETTER -> VERIFY RECEIPT AND RECOVERY",
        ], ["Build Back Better", "Delivery-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management in India.",
            "Verified adjacent route: pre-positioning, preparedness, supply planning and accountable handover demonstrate proactivity without claiming that response outcomes are assured.",
            [1, 3, 4, 5, 6, 7, 8, 17, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, how it is determined and the elements of the Sendai Framework.",
            "Verified support route: continuity, inclusive relief, livelihood recovery and Build Back Better illustrate resilience across response and recovery.",
            [0, 1, 10, 11, 13, 14, 16, 18, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss urban flooding as a climate-induced disaster and the policies and frameworks in India that aim at tackling it.",
            "Verified cross-owned route led by Topic 08; this card contributes anticipatory logistics, shelters, WASH, last-mile access, debris and recovery sequencing.",
            [1, 3, 6, 7, 8, 10, 15, 16, 18, 19]),
    ]
    return common.topic(
        17, "Humanitarian Logistics, Relief, Rehabilitation and Recovery",
        "17_Humanitarian-Logistics-Relief-Rehabilitation-and-Recovery", facts, traps,
        [
            (10, "Distinguish response, relief, rehabilitation, reconstruction and recovery.", [0, 16, 17, 18]),
            (10, "Explain humanitarian principles and grievance safeguards in relief distribution.", [2, 7, 11, 12]),
            (15, "Analyse the humanitarian supply chain from needs assessment to last-mile receipt.", [1, 3, 4, 5, 6, 7, 8]),
            (15, "Evaluate cash and in-kind assistance across shelter, WASH, health and protection needs.", [9, 10, 11, 12]),
            (20, "Design an accountable humanitarian-logistics framework for a large multi-district disaster.", [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 19]),
            (20, "Critically examine recovery sequencing, livelihoods, displacement, debris and Build Back Better.", [0, 13, 14, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "relief", "rehabilitation", "reconstruction", "recovery",
            "needs assessment", "temporary shelters", "humanitarian assistance",
            "Incident Response System", "Minimum Standards of Relief",
            "Build Back Better", "livelihood", "pre-positioning",
            "psychosocial support", "NDRF", "Aapda Mitra",
        ],
        "No audited 2024-2025 GS-III question directly owns humanitarian logistics. The 2020 proactive-management and 2024 resilience questions are bounded support routes; the 2024 urban-flood card is a hazard-specific application.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered NDRF, NDMA/MHA/NIDM, OCHA UNDAC/OSOCC, WHO, WFP, IFRC and Sphere routes. Thin, blocked and unavailable pages are logged; no unverified minimum-standard number, stock, beneficiary, delivery-time, diversion, casualty or recovery-outcome claim was used.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "PHASE NEEDS SUPPLY-CHAIN PROTECTION AND RECOVERY MAP",
            "DISPATCH RECEIPT CASH STANDARD CAMP RETURN AND OUTCOME FIREWALLS",
            "ASSESS PRE-POSITION DELIVER ACCOUNT RESTORE AND BBB SPINE",
            "CURRENT NDRF NDMA MHA OCHA WHO WFP IFRC AND SPHERE EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DISTINGUISH RESPONSE RELIEF REHABILITATION RECONSTRUCTION AND RECOVERY",
            "ASSESS NEED SEVERITY ACCESS CAPACITY PROTECTION AND UNCERTAINTY",
            "PRE-POSITION / PROCURE / WAREHOUSE / TRANSPORT / LAST-MILE DELIVER",
            "APPLY HUMANITY IMPARTIALITY NEUTRALITY INDEPENDENCE AND PRIVACY",
            "SELECT CASH / IN-KIND AND INTEGRATE SHELTER WASH HEALTH PROTECTION",
            "AUDIT RECEIPT GRIEVANCE ANTI-DIVERSION AND INCLUSIVE COVERAGE",
            "RESTORE LIVELIHOODS DURABLE CHOICES ENVIRONMENT AND BUILD BACK BETTER",
        ],
    )


TOPIC_17 = _build()
