"""Authored learner-v2 data for Internal Security Topic 05."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/en/divisionofmha/jammu-kashmir-and-ladakh-affairs "
        "— attempted 2026-09-04; direct retrieval returned 403. The module "
        "therefore imports no current incident, infiltration, recruitment, "
        "force-strength, rehabilitation-output or return-outcome figure from "
        "the page."
    ),
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the Jammu "
        "and Kashmir Reorganisation Act, 2019 and the Armed Forces (Jammu and "
        "Kashmir) Special Powers Act, 1990; direct retrieval returned 403. "
        "Only owner-audited statutory distinctions are used, and constitutional "
        "doctrine remains routed to Polity."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=1700782 — attempted "
        "2026-09-04 for the official account of the 25 February 2021 DGMO "
        "reaffirmation; direct retrieval returned 403. The module preserves "
        "the owner-audited date and treats the instrument as a military "
        "ceasefire understanding, not a treaty or conflict settlement."
    ),
    (
        "https://www.mha.gov.in/ and https://www.pib.gov.in/ — searched "
        "2026-09-04 for a claimed 26 February 2026 Kashmiri-migrant relief "
        "update; no matching official release was substantiated in the live "
        "search. That date and any associated output claim are excluded from "
        "the authored facts."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Accession anchor", "Maharaja Hari Singh signed the Instrument of Accession on 26 October 1947 on Defence, External Affairs and Communications; detailed constitutional doctrine belongs to Polity."),
        ("LoC legal-status boundary", "The Line of Control replaced the earlier ceasefire line after the 1971 war and the Shimla process; it is not described here as an internationally recognised boundary."),
        ("Proxy-war mechanism", "The owner frames J&K militancy as externally enabled proxy warfare using deniable non-state intermediaries, infiltration, finance, weapons, propaganda and local facilitation."),
        ("Attribution gradient", "Cross-border attribution must identify the evidentiary basis—material, communications, cadre origin, training provenance, financing trail or state-institution linkage—rather than rely on an unsupported label."),
        ("Ceasefire understanding", "The November 2003 LoC ceasefire understanding was reaffirmed by the Indian and Pakistani DGMOs on 25 February 2021; it is a military-to-military arrangement, not a treaty or political settlement."),
        ("Separate security metrics", "LoC firing, attempted and successful infiltration, local recruitment, financing, drone or tunnel delivery, and hinterland incidents are distinct metrics that can move independently."),
        ("OGW evidentiary boundary", "An over-ground worker is an alleged non-combatant facilitator whose role must be established through admissible evidence; the label cannot lawfully substitute for proof."),
        ("OGW function map", "Possible facilitation functions include reconnaissance or information, shelter and logistics, communications, recruitment or propaganda, and finance, but each alleged function requires case-specific proof."),
        ("OGW response chain", "Neutralising facilitation requires protected community reporting, evidence-led investigation, lawful financial tracing, prevention or rehabilitation where appropriate, and prosecution on admissible evidence."),
        ("Reorganisation structure", "The Jammu and Kashmir Reorganisation Act, 2019 created the Union Territory of Jammu and Kashmir with a legislature and the Union Territory of Ladakh without one."),
        ("Police-public-order consequence", "Under the 2019 Act, public order and police are outside the J&K Assembly's legislative competence, making the operational chain Lieutenant-Governor and Union centred rather than an ordinary Centre-State chain."),
        ("Constitutional-domain firewall", "Article 370's text, the 2019 constitutional measures and the December 2023 Supreme Court reasoning belong to Polity; this topic uses only clearly identified operational internal-security consequences."),
        ("J&K AFSPA distinction", "The Armed Forces (Jammu and Kashmir) Special Powers Act, 1990 is distinct from the Armed Forces (Special Powers) Act, 1958 applicable in parts of the North-East."),
        ("Village Defence Guards boundary", "Village Defence Committees were renamed Village Defence Guards and operate under district SP or SSP supervision; local presence and warning benefits must be balanced against training, command and accountability risks."),
        ("Hearts-and-minds meaning", "Winning hearts and minds is an operational legitimacy strategy combining civilian protection, proportionate force, participation, grievance redress, service and livelihood delivery, rehabilitation and credible accountability."),
        ("Rehabilitation-evidence rung", "A relief package, job, accommodation or registered beneficiary is an implementation input; none alone proves safe return, restored trust or conflict resolution."),
        ("CPEC bounded route", "For CPEC, this owner supplies only the sovereignty and security leg: the corridor passes through territory claimed by India and administered by Pakistan and may affect strategic logistics; wider connectivity and diplomacy belong to IR and Economy."),
        ("Displacement-and-return boundary", "Kashmiri Pandit displacement is a durable rehabilitation and justice issue; any present return, residence, employment or security outcome requires a dated official source."),
        ("Integrated response chain", "Counter-infiltration, intelligence, policing, counter-finance, evidence-led investigation, prosecution, governance and communication are complementary layers rather than substitutes."),
        ("Qualified end-state", "Durable security requires disruption of the proxy mechanism alongside civilian protection, lawful accountability, accountable local governance, rehabilitation and trust; a quieter LoC does not prove the wider conflict resolved."),
    ]
    traps = [
        "Do not turn the accession chronology into the whole internal-security answer.",
        "Do not describe the LoC as a settled international boundary.",
        "Do not merge sponsor, proxy group and alleged local facilitator into one legal actor.",
        "Do not assert cross-border attribution without naming the evidence status.",
        "Do not equate the 2021 ceasefire reaffirmation with a treaty or settlement.",
        "Do not merge LoC firing, infiltration, recruitment and hinterland violence into one trend.",
        "Do not use OGW as a label for political disagreement or as a substitute for proof.",
        "Do not publish operational routes, deployment patterns or tactical vulnerabilities.",
        "Do not treat the 2019 reorganisation as proof of a security outcome.",
        "Do not import Article 370 constitutional reasoning into an Internal Security answer.",
        "Do not equate a rehabilitation input with safe return or restored trust.",
        "Do not use an unverified current incident, casualty or force statistic.",
    ]
    titles = [
        "Accession LoC and constitutional scope",
        "Proxy war actors means and objectives",
        "Attribution gradient and evidence status",
        "Ceasefire understanding and separate metrics",
        "Infiltration finance information and facilitation chain",
        "Over-ground workers definition and functions",
        "Evidence-led OGW response and rights safeguard",
        "2019 reorganisation operational consequence",
        "Police public order and Lieutenant-Governor chain",
        "J&K AFSPA and legal-instrument distinctions",
        "Village Defence Guards and accountability",
        "Hearts and minds as operational legitimacy",
        "Rehabilitation displacement and outcome discipline",
        "CPEC sovereignty and bounded security route",
        "Integrated response and qualified end-state",
    ]
    routes = [
        "Open with the proxy-security issue, then bound constitutional history to Polity.",
        "Separate sponsor, intermediary, facilitator, vector and intended end-state.",
        "State the evidence rung before making any attribution claim.",
        "Compare LoC firing with infiltration, recruitment, finance and hinterland activity.",
        "Trace the support chain without exposing tactical vulnerabilities.",
        "Define facilitation neutrally and require proof for each alleged function.",
        "Match every intervention to lawful evidence, protection and remedy.",
        "Explain administrative command effects without claiming constitutional adjudication.",
        "Name the statutory exclusion of police and public order precisely.",
        "Identify the correct J&K-specific statute and stop before field-outcome claims.",
        "Balance local warning capacity with supervision and accountability.",
        "Evaluate protection, participation, delivery, rehabilitation and remedy separately.",
        "Stop at implementation input unless safe return and trust are officially verified.",
        "Enumerate sovereignty, logistics and security concerns within the cross-subject boundary.",
        "Conclude with disruption plus legitimacy, not a single security metric.",
    ]
    panels = [
        common.panel("Accession-to-LoC boundary", "timeline", [
            "26 OCT 1947 -> INSTRUMENT OF ACCESSION",
            "1947-48 -> CONFLICT / CEASEFIRE-LINE CONTEXT",
            "1971 + SHIMLA PROCESS -> LINE OF CONTROL",
            "BOUNDARY -> constitutional doctrine routes to Polity",
        ], ["Accession anchor", "LoC legal-status boundary", "Constitutional-domain firewall"]),
        common.panel("Proxy-war system", "systems-map", [
            "EXTERNAL SPONSOR -> DENIABLE PROXY",
            "PROXY -> INFILTRATION / FINANCE / WEAPONS / PROPAGANDA",
            "LOCAL FACILITATION -> only where evidence proves the role",
            "END-STATE -> coercion, fear, legitimacy and strategic pressure",
        ], ["Proxy-war mechanism", "Attribution gradient"]),
        common.panel("Attribution ladder", "status-ladder", [
            "1 ALLEGATION / CLAIM",
            "2 RECOVERED MATERIAL OR COMMUNICATION",
            "3 FINANCING / TRAINING / CADRE LINK",
            "4 INVESTIGATIVE OR JUDICIAL FINDING",
            "RULE -> state the rung; do not jump to adjudicated certainty",
        ], ["Attribution gradient"]),
        common.panel("Ceasefire-versus-conflict matrix", "comparison-table", [
            "LoC FIRING -> governed by military understanding",
            "INFILTRATION -> separate border-security metric",
            "RECRUITMENT / FINANCE -> separate network metrics",
            "HINTERLAND INCIDENT -> separate policing/investigation metric",
        ], ["Ceasefire understanding", "Separate security metrics"]),
        common.panel("Proxy-support chain", "process-flow", [
            "INFILTRATION / DELIVERY",
            "-> LOGISTICS / SHELTER / COMMUNICATION",
            "-> FINANCE / RECRUITMENT / PROPAGANDA",
            "-> ATTACK OR COERCIVE INFLUENCE",
            "SAFE RULE -> describe categories, not exploitable methods",
        ], ["Proxy-war mechanism", "OGW function map"]),
        common.panel("OGW proof-and-response", "decision-tree", [
            "ALLEGED FACILITATION?",
            "-> PROTECT REPORTING + PRESERVE EVIDENCE",
            "-> INVESTIGATE FUNCTION + FINANCIAL TRAIL",
            "-> REHABILITATE / PREVENT OR PROSECUTE AS EVIDENCE WARRANTS",
            "TRAP -> label is not proof",
        ], ["OGW evidentiary boundary", "OGW response chain"]),
        common.panel("2019 operational chain", "institution-map", [
            "J&K UT -> LEGISLATURE EXISTS",
            "POLICE + PUBLIC ORDER -> OUTSIDE ASSEMBLY COMPETENCE",
            "OPERATIONAL CHAIN -> LIEUTENANT GOVERNOR / UNION",
            "POLITY FIREWALL -> constitutional merits and judgment elsewhere",
        ], ["Reorganisation structure", "Police-public-order consequence", "Constitutional-domain firewall"]),
        common.panel("Legal-instrument firewall", "comparison-table", [
            "J&K REORGANISATION ACT 2019 -> administrative / competence structure",
            "J&K AFSPA 1990 -> special-powers statute",
            "LoC CEASEFIRE -> military understanding",
            "RULE -> none proves field capability or outcome",
        ], ["Police-public-order consequence", "J&K AFSPA distinction", "Ceasefire understanding"]),
        common.panel("Community-security balance", "balance-scale", [
            "VDG GAIN -> local presence / warning / self-protection",
            "VDG RISK -> training / command / accountability",
            "SAFEGUARD -> SP / SSP supervision + lawful review",
            "VERDICT -> community partnership, never unaccountable substitution",
        ], ["Village Defence Guards boundary"]),
        common.panel("Hearts-and-minds scorecard", "matrix", [
            "CIVILIAN SECURITY | PROPORTIONATE FORCE",
            "PARTICIPATION | GRIEVANCE REDRESS",
            "SERVICES / LIVELIHOOD | REHABILITATION",
            "ACCOUNTABILITY / REMEDY | TRUST OUTCOME",
        ], ["Hearts-and-minds meaning", "Rehabilitation-evidence rung"]),
        common.panel("CPEC bounded route", "answer-spine", [
            "PRINCIPAL OWNERS -> IR / ECONOMY",
            "INTERNAL-SECURITY LEG -> SOVEREIGNTY CLAIM",
            "STRATEGIC LEG -> LOGISTICS / CONTINGENCY RISK",
            "LIMIT -> no invented troop movement or current outcome",
        ], ["CPEC bounded route"]),
        common.panel("PYQ and end-state rail", "answer-spine", [
            "2018 -> CPEC SOVEREIGNTY / SECURITY LEG",
            "2019 -> OGW ROLE + EVIDENCE-LED RESPONSE",
            "2023 -> HEARTS AND MINDS EVALUATION",
            "END -> DISRUPTION + RIGHTS + GOVERNANCE + REHABILITATION",
            "QUALIFY -> last verified metric and evidence rung",
        ], ["Integrated response chain", "Qualified end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018", "GS-III",
            "CPEC as an OBOR subset and India's strategic objections.",
            "Audited routed demand; Enumerate · 10 marks · 150 words. The solution uses only the bounded sovereignty/security leg owned here.",
            [0, 1, 2, 3, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2019", "GS-III",
            "The role of over-ground workers in assisting terrorist organisations in insurgency-affected areas and measures to neutralise their influence.",
            "Printed stem inspected in the OCR-searchable official paper; Examine/Discuss · 10 marks · 150 words.",
            [2, 3, 6, 7, 8, 14, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2023", "GS-III",
            "Winning hearts and minds in terrorism-affected areas and Government measures for conflict resolution in Jammu and Kashmir.",
            "Printed stem inspected in the OCR-searchable official paper; Discuss · 10 marks · 150 words.",
            [5, 9, 10, 14, 15, 17, 18, 19],
        ),
    ]
    return common.topic(
        5, "Jammu & Kashmir and Cross-Border Terrorism",
        "05_Jammu-Kashmir-and-Cross-Border-Terrorism", facts, traps,
        [
            (10, "Explain why a LoC ceasefire cannot by itself establish the end of cross-border terrorism.", [3, 4, 5, 18, 19]),
            (10, "Examine the role attributed to over-ground workers and propose evidence-led measures to neutralise unlawful facilitation.", [2, 3, 6, 7, 8, 14]),
            (15, "Analyse the proxy-war mechanism in Jammu and Kashmir while preserving attribution and rights safeguards.", [1, 2, 3, 5, 6, 7, 8, 18, 19]),
            (15, "Discuss the operational internal-security consequences of the 2019 reorganisation without entering the constitutional merits.", [9, 10, 11, 12, 18, 19]),
            (20, "Critically evaluate the hearts-and-minds approach as part of conflict resolution in Jammu and Kashmir.", [5, 6, 8, 13, 14, 15, 17, 18, 19]),
            (20, "Assess India's integrated response to cross-border proxy warfare across ceasefire, infiltration, facilitation, finance, governance and rehabilitation dimensions.", [1, 2, 3, 4, 5, 6, 8, 14, 15, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Instrument of Accession", "Line of Control", "proxy war",
            "ISI", "over-ground worker", "25 February 2021",
            "J&K Assembly", "public order", "police",
            "Armed Forces (Jammu and Kashmir) Special Powers Act",
            "Village Defence Guards", "Hearts and Minds", "CPEC",
            "Article 370", "ceasefire",
        ],
        "The audited GS-III ledger routes the 2018 CPEC cross-subject demand, the 2019 OGW demand and the 2023 Jammu and Kashmir hearts-and-minds demand here. OCR inspection confirmed the 2019 and 2023 printed stems; no official model answer is inferred.",
        pyqs, LIVE_ATTEMPTS,
        "Live official-source attempts on 2026-09-04 substantiated no new J&K operational statistic. The module therefore relies on stable owner-audited legal and institutional anchors, preserves the 25 February 2021 ceasefire status, and requires a dated MHA, NIA, police or court source for any current attribution or outcome claim.",
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "ACCESSION, LoC AND PROXY-WAR THREAT GRAMMAR",
            "ATTRIBUTION, OGW AND OPERATIONAL-LEGAL FIREWALLS",
            "HEARTS-AND-MINDS, REHABILITATION AND PYQ SPINES",
            "SEPARATE METRICS AND QUALIFIED CONFLICT-RESOLUTION VERDICT",
        ),
        register_answer_spine=[
            "OPEN WITH THE EXTERNALLY ENABLED PROXY MECHANISM",
            "BOUND ACCESSION ARTICLE 370 AND CONSTITUTIONAL DOCTRINE TO POLITY",
            "SEPARATE SPONSOR PROXY FACILITATOR VECTOR AND END-STATE",
            "STATE THE ATTRIBUTION AND EVIDENCE RUNG",
            "DISTINGUISH CEASEFIRE INFILTRATION RECRUITMENT FINANCE AND INCIDENT METRICS",
            "DEFINE OGW FUNCTIONS WITHOUT TREATING ALLEGATION AS PROOF",
            "EVALUATE HEARTS AND MINDS THROUGH PROTECTION PARTICIPATION DELIVERY AND REMEDY",
            "CONCLUDE WITH DISRUPTION ACCOUNTABILITY GOVERNANCE REHABILITATION AND TRUST",
        ],
    )


TOPIC_05 = _build()
