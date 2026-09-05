"""Authored learner-v2 data for Disaster Management Topic 18."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.undrr.org/implementing-sendai-framework/what-sendai-"
        "framework — fetched 2026-09-04; UNDRR listed the four Sendai "
        "priorities and described governance, investment and Build Back Better. "
        "https://www.mha.gov.in/en/commoncontent/disaster-management-act-2005 "
        "— attempted 2026-09-04 and returned HTTP 403."
    ),
    (
        "https://www.undrr.org/our-work — fetched 2026-09-04; UNDRR described "
        "itself as the lead UN entity coordinating disaster risk reduction. "
        "https://cdri.world/ — fetched 2026-09-04 for CDRI's official "
        "infrastructure-resilience purpose; no membership or outcome figure was "
        "imported."
    ),
    (
        "https://bimstec.org/sector/disaster-management — attempted 2026-09-04 "
        "and returned HTTP 404. https://saarc-sec.org/index.php/areas-of-"
        "cooperation/environment-natural-disasters-and-biotechnology — "
        "attempted 2026-09-04 and returned HTTP 404. "
        "https://pib.gov.in/ — searched 2026-09-04; no current exercise or "
        "agreement implementation claim was used."
    ),
    (
        "https://www.unocha.org/we-coordinate — fetched 2026-09-04; OCHA "
        "described UNDAC mobilisation when an affected country requests "
        "international assistance and OSOCC's government-link role. "
        "https://ndrf.gov.in/en/about-us — fetched 2026-09-04 only for the "
        "official specialised-response and international-assistance route."
    ),
    (
        "https://nidm.gov.in/ — searched 2026-09-04 for official capacity-"
        "building material; the route supplied no additional current outcome. "
        "https://ndma.gov.in/ — attempted 2026-09-04; the portal was not usable. "
        "No training count, exercise result, plan adoption or local capability "
        "ranking was inferred."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Policy governance capacity coordination accountability", "Policy sets direction, governance allocates authority and rules, capacity enables performance, coordination aligns actors, and accountability tests duty and results; the five terms are related but not interchangeable."),
        ("Centre State local architecture", "The Union, States, districts, urban and rural local bodies and line departments hold differentiated legal, fiscal and operational responsibilities; subsidiarity should place action close to risk while preserving support and standards."),
        ("Whole-of-society", "Whole-of-society disaster management includes government, communities, civil society, volunteers, academia, media, private operators and critical-service providers, but participation does not dilute public accountability."),
        ("Plan-to-capability gap", "A plan proves documented intent; capability additionally requires trained people, usable procedures, equipment, interoperable communications, finance, authority, exercises, maintenance and evidence of corrective learning."),
        ("Preparedness exercises", "Exercises test assumptions, roles, communications, resource mobilisation and decision thresholds in a controlled setting; an exercise validates only what was actually tested and corrected."),
        ("Training and capacity development", "Training builds knowledge and skill, but capability requires appropriate selection, refresher cycles, supervision, equipment, deployment opportunity and institutional retention."),
        ("Incident command governance", "Incident command or response arrangements should define leadership, operations, planning, logistics, finance and information at an exam-safe governance level; tactical details remain context-specific."),
        ("Coordination and interoperability", "Coordination requires shared terminology, contact routes, data standards, mutual-aid procedures, interoperable communications and clear lead/support roles before an incident."),
        ("Data learning and audit", "Risk, loss, expenditure, exercise and after-action data should support transparent review, correction and institutional memory; a database or report is not proof that recommendations were implemented."),
        ("Accountability chain", "Accountability links assigned duty, resources, standards, reporting, independent or legislative review, grievance and corrective action; coordination without identifiable responsibility can create diffusion of blame."),
        ("Sendai Framework", "The Sendai Framework for Disaster Risk Reduction 2015-2030 is a voluntary non-binding framework with four priorities and seven global targets; it does not itself create enforceable treaty obligations."),
        ("UNDRR and GPDRR", "UNDRR coordinates the UN disaster-risk-reduction agenda, while the Global Platform supports review and knowledge exchange; neither substitutes for national law or acts as a binding enforcement body."),
        ("CDRI", "The Coalition for Disaster Resilient Infrastructure supports cooperation on infrastructure risk, standards, finance and recovery; participation or membership demonstrates a cooperation platform, not resilient assets or reduced losses."),
        ("Regional cooperation", "SAARC, BIMSTEC and other regional routes can support exercises, knowledge, warning, mutual assistance and common procedures, but an agreement, meeting or exercise is not implementation or outcome evidence."),
        ("International assistance legal status", "International assistance is governed by the affected State's consent, domestic law, entry and customs arrangements, coordination structures and applicable agreements; a humanitarian offer does not create automatic access."),
        ("Sovereignty and humanitarian diplomacy", "Humanitarian diplomacy seeks timely access, cooperation and protection while respecting sovereignty, consent and national leadership; these principles must be balanced rather than presented as opposites."),
        ("Localisation", "Localisation gives national and local responders meaningful leadership, resources, information and voice, while international actors provide requested surge, expertise or finance; proximity alone does not prove inclusion or capacity."),
        ("Knowledge and technology cooperation", "Shared hazard data, standards, research, training and warning can be cooperation outputs, but interoperability, access, maintenance and local decision use determine whether they become capability."),
        ("Agreement implementation outcome ladder", "Signing an agreement establishes a formal commitment, implementation shows operational action, outputs show delivered activities, and outcomes show changed capacity or risk; evidence must stop at the verified rung."),
        ("Governance-outcome firewall", "A law, institution, plan, training, drill, summit, agreement, platform, database or membership proves its own existence or activity; preparedness, coordination quality, local capability and reduced loss require separate evidence."),
    ]
    traps = [
        "Do not use policy, governance, capacity, coordination and accountability as synonyms.",
        "Do not infer capability from a plan, training certificate or equipment list.",
        "Do not assume one exercise validates all hazards, actors or geographies.",
        "Do not let whole-of-society language obscure statutory public responsibility.",
        "Do not describe Sendai as a binding treaty.",
        "Do not present UNDRR or GPDRR as enforcement authorities.",
        "Do not infer resilient infrastructure from CDRI participation.",
        "Do not infer regional cooperation outcomes from meetings or agreements.",
        "Do not ignore sovereignty, consent and domestic legal arrangements for assistance.",
        "Do not equate international visibility with localised implementation.",
    ]
    titles = [
        "Policy governance capacity coordination and accountability distinctions",
        "Centre State district urban rural and line-department roles",
        "Whole-of-society participation with public accountability",
        "Plan-to-capability gap people procedure equipment finance authority",
        "Preparedness exercises test design evaluation and corrective action",
        "Training refresher supervision retention and deployable skill",
        "Incident response leadership and exam-safe command architecture",
        "Interoperability mutual aid data and communication protocols",
        "Risk loss expenditure after-action data learning and audit",
        "Sendai priorities targets voluntary status and domestic bridge",
        "UNDRR GPDRR review knowledge and non-enforcement boundary",
        "CDRI standards finance recovery and platform-outcome boundary",
        "SAARC BIMSTEC regional cooperation and mutual assistance",
        "International assistance sovereignty localisation and diplomacy",
        "PYQ synthesis agreement implementation outcome firewall",
    ]
    routes = [
        "Define each governance term and assign its evidence test.",
        "Map differentiated duties support standards finance and subsidiarity.",
        "Include communities private operators experts and media without duty dilution.",
        "Audit people procedure equipment communication finance and authority.",
        "State scope injects participants observations corrections and retest.",
        "Trace training to retained deployable supervised competence.",
        "Keep command at role coordination and accountability level.",
        "Build common language data contacts communications and mutual aid.",
        "Connect data to review correction ownership and institutional memory.",
        "State four priorities seven targets and voluntary non-binding status.",
        "Separate coordination review and knowledge from enforcement.",
        "Use CDRI as a cooperation mechanism, not an outcome proxy.",
        "Classify agreement exercise warning knowledge and assistance outputs.",
        "Balance consent national leadership local agency and requested surge.",
        "Conclude only at the verified agreement implementation output or outcome rung.",
    ]
    panels = [
        common.panel("Governance vocabulary", "comparison-table", [
            "POLICY -> DIRECTION",
            "GOVERNANCE -> AUTHORITY / RULES",
            "CAPACITY -> ABILITY TO PERFORM",
            "COORDINATION -> ALIGNMENT | ACCOUNTABILITY -> DUTY + REVIEW",
        ], ["Policy governance capacity coordination accountability"]),
        common.panel("Vertical architecture", "governance-ladder", [
            "UNION -> NATIONAL POLICY STANDARD SUPPORT / COORDINATION",
            "STATE -> STATE RISK GOVERNANCE AND LINE DEPARTMENTS",
            "DISTRICT -> MULTI-SECTOR OPERATIONS",
            "ULB / PRI / COMMUNITY -> LOCAL RISK ACTION AND FEEDBACK",
        ], ["Centre State local architecture"]),
        common.panel("Whole-of-society ring", "network-map", [
            "PUBLIC AUTHORITIES AT THE CORE OF ACCOUNTABILITY",
            "COMMUNITY / CIVIL SOCIETY / VOLUNTEERS",
            "ACADEMIA / MEDIA / PRIVATE AND LIFELINE OPERATORS",
            "PARTICIPATION COMPLEMENTS; DOES NOT ERASE PUBLIC DUTY",
        ], ["Whole-of-society"]),
        common.panel("Plan-to-capability audit", "audit-ladder", [
            "PLAN / SOP",
            "TRAINED PEOPLE + AUTHORITY",
            "EQUIPMENT FINANCE COMMUNICATION INTEROPERABILITY",
            "EXERCISE -> CORRECT -> RETEST -> DEPLOYABLE CAPABILITY",
        ], ["Plan-to-capability gap", "Preparedness exercises", "Training and capacity development"]),
        common.panel("Incident governance shell", "role-map", [
            "LEADERSHIP / COMMAND",
            "OPERATIONS | PLANNING | LOGISTICS",
            "FINANCE / ADMINISTRATION | PUBLIC INFORMATION",
            "TACTICS REMAIN HAZARD AND CONTEXT SPECIFIC",
        ], ["Incident command governance"]),
        common.panel("Interoperability bridge", "process-flow", [
            "COMMON TERMS + CONTACTS",
            "DATA / REQUEST / RESOURCE STANDARDS",
            "MUTUAL-AID AND COMMUNICATION PROCEDURES",
            "CLEAR LEAD SUPPORT ESCALATION AND HANDOVER",
        ], ["Coordination and interoperability"]),
        common.panel("Learning-accountability loop", "feedback-loop", [
            "RISK / LOSS / EXPENDITURE / EXERCISE DATA",
            "AFTER-ACTION REVIEW + PUBLIC / LEGISLATIVE / INDEPENDENT SCRUTINY",
            "ASSIGN CORRECTIVE OWNER DEADLINE RESOURCE",
            "IMPLEMENT -> RETEST -> RETAIN INSTITUTIONAL MEMORY",
        ], ["Data learning and audit", "Accountability chain"]),
        common.panel("Sendai map", "numbered-rail", [
            "1 UNDERSTAND RISK",
            "2 STRENGTHEN RISK GOVERNANCE",
            "3 INVEST IN DRR FOR RESILIENCE",
            "4 PREPARE / BUILD BACK BETTER | 7 TARGETS | VOLUNTARY",
        ], ["Sendai Framework"]),
        common.panel("Global institution boundary", "comparison-table", [
            "UNDRR -> UN DRR COORDINATION",
            "GPDRR -> REVIEW / KNOWLEDGE EXCHANGE",
            "CDRI -> INFRASTRUCTURE RISK STANDARDS FINANCE RECOVERY",
            "NONE PROVES NATIONAL IMPLEMENTATION OR ENFORCEMENT",
        ], ["UNDRR and GPDRR", "CDRI"]),
        common.panel("Regional cooperation ladder", "status-ladder", [
            "DIALOGUE / AGREEMENT",
            "COMMON PROCEDURE / TRAINING / EXERCISE",
            "ACTIVATION / ASSISTANCE / OUTPUT",
            "CAPACITY OR RISK OUTCOME -> SEPARATE EVIDENCE",
        ], ["Regional cooperation", "Agreement implementation outcome ladder"]),
        common.panel("Assistance and localisation balance", "balance-sheet", [
            "AFFECTED-STATE CONSENT + DOMESTIC LAW + NATIONAL LEADERSHIP",
            "INTERNATIONAL SURGE / EXPERTISE / FINANCE WHEN REQUESTED",
            "LOCAL RESPONDER DECISION POWER RESOURCES AND INFORMATION",
            "HUMANITARIAN ACCESS WITH SOVEREIGNTY AND ACCOUNTABILITY",
        ], ["International assistance legal status", "Sovereignty and humanitarian diplomacy", "Localisation"]),
        common.panel("Governance answer spine", "answer-spine", [
            "DEFINE TERMS -> MAP CENTRE STATE LOCAL AND SOCIETY ROLES",
            "CONVERT PLANS / TRAINING / EXERCISES INTO AUDITED CAPABILITY",
            "USE SENDAI UNDRR CDRI REGIONAL AND ASSISTANCE ROUTES PRECISELY",
            "STOP AT VERIFIED AGREEMENT IMPLEMENTATION OUTPUT OR OUTCOME",
        ], ["Knowledge and technology cooperation", "Governance-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2018", "GS-III",
            "Describe measures taken in India for disaster risk reduction before and after the Sendai Framework and explain how Sendai differs from Hyogo.",
            "Verified direct framework route owned by Topic 01 but central to this governance topic; preserve the comparative demand and voluntary-framework boundary.",
            [0, 1, 3, 8, 9, 10, 11, 18, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, how it is determined and the elements of the Sendai Framework.",
            "Verified direct support route: governance, capacity, accountability and international cooperation operationalise resilience while all seven targets remain Topic 01-owned.",
            [0, 1, 3, 4, 5, 8, 9, 10, 18, 19]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management in India.",
            "Verified adjacent governance route: plans, capacity, exercises, data, accountability and local roles demonstrate proactivity without inferring implementation outcomes.",
            [0, 1, 2, 3, 4, 5, 7, 8, 9, 19]),
    ]
    return common.topic(
        18, "Governance, Capacity and International Cooperation",
        "18_Governance-Capacity-and-International-Cooperation", facts, traps,
        [
            (10, "Distinguish policy, governance, capacity, coordination and accountability in disaster management.", [0, 3, 7, 9]),
            (10, "Explain the plan-to-capability gap and the role of exercises and training.", [3, 4, 5, 6]),
            (15, "Analyse Centre-State-local and whole-of-society roles in disaster governance.", [1, 2, 7, 8, 9]),
            (15, "Examine Sendai, UNDRR, GPDRR and CDRI through their distinct governance functions.", [10, 11, 12, 18]),
            (20, "Design an accountable capacity-development system using interoperability, exercises, data, audit and corrective learning.", [3, 4, 5, 6, 7, 8, 9, 19]),
            (20, "Critically evaluate regional and international disaster cooperation through sovereignty, localisation and the agreement-to-outcome ladder.", [13, 14, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "governance", "capacity", "coordination", "accountability",
            "Sendai Framework", "seven targets", "NPDRR", "GPDRR",
            "UNDRR", "CDRI", "SAARC", "BIMSTEC", "localisation",
            "implementation", "outcome",
        ],
        "The 2018 Hyogo-Sendai question and 2024 resilience question are verified direct framework routes, with Topic 01 retaining primary ownership. The 2020 reactive-to-proactive question is a bounded domestic-governance application.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered UNDRR/Sendai, MHA/NDMA/NIDM, CDRI, BIMSTEC, SAARC, PIB, OCHA and NDRF. Regional pages were thin or returned 404 and Indian portals were partly blocked; no exercise result, agreement activation, assistance status, membership count, localisation score or risk outcome was invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "GOVERNANCE CAPACITY VERTICAL ROLES COOPERATION AND ACCOUNTABILITY MAP",
            "PLAN DRILL TRAINING AGREEMENT MEMBERSHIP IMPLEMENTATION OUTCOME FIREWALLS",
            "ASSIGN BUILD TEST COORDINATE AUDIT LOCALISE AND COOPERATE SPINE",
            "CURRENT UNDRR SENDAI MHA NDMA NIDM CDRI SAARC BIMSTEC OCHA BOUNDARY",
        ),
        register_answer_spine=[
            "DISTINGUISH POLICY GOVERNANCE CAPACITY COORDINATION AND ACCOUNTABILITY",
            "MAP UNION STATE DISTRICT ULB PRI COMMUNITY AND WHOLE-OF-SOCIETY ROLES",
            "CONVERT PLANS INTO PEOPLE PROCEDURES EQUIPMENT FINANCE AND AUTHORITY",
            "EXERCISE REVIEW CORRECT RETEST AND PRESERVE INSTITUTIONAL LEARNING",
            "USE SENDAI UNDRR GPDRR AND CDRI WITH NON-ENFORCEMENT BOUNDARIES",
            "BALANCE REGIONAL / INTERNATIONAL ASSISTANCE WITH CONSENT AND LOCALISATION",
            "SEPARATE AGREEMENT IMPLEMENTATION OUTPUT OUTCOME AND VERIFY EACH RUNG",
        ],
    )


TOPIC_18 = _build()
