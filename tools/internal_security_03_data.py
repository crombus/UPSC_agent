"""Authored learner-v2 data for Internal Security Topic 03."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/en/divisionofmha/left-wing-extremism-division "
        "— searched 2026-09-04; the official MHA LWE division is treated as "
        "the policy owner for the National Policy and Action Plan and current "
        "scheme/status material. No force disposition or operational method "
        "is reproduced."
    ),
    (
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2292864 — "
        "attempted 2026-09-04; direct fetch returned 403, while official-domain "
        "search surfaced the post-deadline 'Naxal-Free India' assessment. The "
        "module preserves qualified official wording and does not convert it "
        "into literal zero violence or resolved grievances."
    ),
    (
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2179489 — "
        "searched 2026-09-04 for the December 2025 LWE position; official "
        "search results report decline metrics, but nearby official releases "
        "can use different cut-off dates and incident totals. The authored "
        "fact follows the canonical owner's dated 89%, 91% and 218 formulation "
        "and never combines unlike reporting periods."
    ),
    (
        "https://www.indiacode.nic.in/ — searched 2026-09-04 for the Forest "
        "Rights Act, 2006 and PESA, 1996; the module uses their owner-audited "
        "rights and Gram Sabha roles without claiming that enactment proves "
        "title recognition, consultation or implementation."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Naxalbari origin", "The Naxalite movement began in May 1967 in the Naxalbari area of Darjeeling district under leaders including Charu Majumdar and Kanu Sanyal; origin history is not a current spread map."),
        ("LWE objective", "Left-Wing Extremism is a Maoist armed challenge aimed at capturing state power through protracted people's war, not a secessionist claim for a separate sovereign State."),
        ("Five-phase strategy", "The owner's Maoist spread sequence is preparatory, perspective, guerrilla, base and liberated phases; it describes organisational strategy rather than verified present territorial control."),
        ("CPI Maoist formation", "CPI (Maoist) was formed in 2004 through the merger of the People's War Group and Maoist Communist Centre of India; current organisational claims require dated official verification."),
        ("Land-forest causes", "Land alienation, weak recognition of traditional forest rights, acquisition without adequate compensation and disruption of jal-jangal-zameen relationships are core enabling grievances."),
        ("Development-governance causes", "Poverty, unemployment, infrastructure deficit, administrative absence, weak justice, social exclusion and alienation create exploitable vulnerabilities but do not mechanically cause violence."),
        ("Mineral-extortion nexus", "LWE intensity historically overlapped mineral-rich areas because infrastructure, mining and contracting activity created extortion opportunities; resource presence alone does not explain recruitment."),
        ("Instrumental underdevelopment", "The owner records that Maoists can obstruct roads, electricity, water and administration because continued underdevelopment sustains territorial influence; the movement may maintain the condition it claims to oppose."),
        ("Civilian impact", "Affected people face coercion, violence, extortion, blocked education and health access, livelihood and displacement pressures, weakened panchayats and exposure to both extremist and State action."),
        ("Clear-hold-develop", "Security forces may clear access, but durable control requires police and civil administration to hold the area before rights, services and infrastructure can develop it."),
        ("Three-pronged policy", "MHA's National Policy and Action Plan to address LWE, 2015 combines security, development, and ensuring the rights and entitlements of local communities."),
        ("Three-track operational frame", "The owner separately emphasises security strategy, development strategy and psychological or trust-restoration work; trust is not an automatic by-product of operations."),
        ("FRA rights boundary", "The Forest Rights Act, 2006 is a rights-based counter-LWE instrument, but enactment is not proof of individual or community forest-right recognition in an affected area."),
        ("PESA governance boundary", "PESA, 1996 extends self-governance and Gram Sabha roles in Fifth Schedule areas, including consultation-related safeguards; procedure and implementation must be evidenced separately."),
        ("UAPA listing boundary", "CPI (Maoist) and its formations are listed in the First Schedule of UAPA; a ban or listing is a legal status, not proof that every alleged member or front is guilty."),
        ("Inter-State trijunction", "Maoist movement across the Dandakaranya interfaces of Chhattisgarh, Odisha, Maharashtra and the former Andhra Pradesh region illustrates how differing State pressure and policy can be exploited."),
        ("Specialised-force lesson", "The Greyhounds precedent shows the value of specialised, trained State-police capability, while displacement into adjoining States shows why one-State success needs inter-State coordination."),
        ("Surrender-rehabilitation firewall", "Surrender is a verifiable event, while rehabilitation requires livelihood, safety, social reintegration and time; a surrender count cannot be reported as a completed rehabilitation outcome."),
        ("Dated decline metrics", "The canonical owner records a December 2025 MHA reply reporting an 89% decline in violence, a 91% decline in deaths since 2010 and 218 incidents in 2025; these are security metrics, not a grievance-resolution verdict."),
        ("Post-deadline status", "PIB's June 2026 material describes India as effectively free from Left-Wing Extremism; the qualifier does not mean zero risk, zero incidents, completed rehabilitation or resolved land and forest grievances."),
    ]
    traps = [
        "Do not describe LWE as a secessionist movement.",
        "Do not treat poverty or mineral resources as mechanically sufficient causes.",
        "Do not use a book-period Red Corridor map as current status.",
        "Do not treat security operations as the whole response.",
        "Do not omit rights and entitlements from the 2015 policy.",
        "Do not treat FRA or PESA enactment as implementation.",
        "Do not equate clearing an area with holding trusted administration.",
        "Do not convert a district classification into grievance resolution.",
        "Do not equate surrender with rehabilitation.",
        "Do not treat an announced elimination target as an achieved outcome.",
        "Do not merge official figures from different dates or cut-offs.",
        "Do not disclose tactical deployments or operational methods.",
    ]
    titles = [
        "Naxalbari origin and Maoist objective",
        "Protracted people's war and five phases",
        "CPI Maoist formation and legal status",
        "Land forest and jal-jangal-zameen grievances",
        "Poverty governance exclusion and organised conversion",
        "Mineral belt extortion economy",
        "Instrumental underdevelopment and blocked administration",
        "People affected and legitimacy costs",
        "Clear hold develop as three capabilities",
        "National Policy and Action Plan 2015",
        "Security development and trust-restoration tracks",
        "FRA PESA Fifth Schedule and rights delivery",
        "Dandakaranya inter-State coordination problem",
        "Greyhounds surrender and rehabilitation design",
        "Dated decline effectively-free claim and durable end-state",
    ]
    routes = [
        "Define LWE's objective and distinguish it from separatism.",
        "Explain organisational progression without claiming current control.",
        "Separate historical formation, statutory listing and individual guilt.",
        "Link rights exclusion to vulnerability and recruitment.",
        "Add the organised actor that converts grievance into coercion.",
        "Explain extortion opportunity without blaming resources themselves.",
        "Show how development obstruction can sustain the movement.",
        "Answer impact through services, livelihoods, institutions and coercion.",
        "Use holding administration as the durability test.",
        "Name all three official prongs exactly.",
        "Treat trust restoration as a separate strategic task.",
        "Pair legal entitlements with implementation evidence.",
        "Explain why State boundaries are operational discontinuities.",
        "Separate specialised capability, surrender event and rehabilitation outcome.",
        "Grade target, metric, classification and qualified status separately.",
    ]
    panels = [
        common.panel("LWE concept rail", "process-flow", [
            "MAY 1967 NAXALBARI -> MOVEMENT ORIGIN",
            "MAOIST OBJECTIVE -> CAPTURE STATE POWER",
            "METHOD -> PROTRACTED PEOPLE'S WAR",
            "BOUNDARY -> NOT A SECESSIONIST CLAIM",
        ], ["Naxalbari origin", "LWE objective"]),
        common.panel("Five-phase expansion", "status-ladder", [
            "PREPARATORY -> PERSPECTIVE -> GUERRILLA",
            "-> BASE -> LIBERATED PHASE",
            "USE -> understand organisational intent",
            "TRAP -> do not infer present territorial status",
        ], ["Five-phase strategy"]),
        common.panel("Cause-actor matrix", "matrix", [
            "LAND / FOREST EXCLUSION | GOVERNANCE ABSENCE",
            "POVERTY / SERVICES | SOCIAL ALIENATION",
            "ORGANISED MAOIST ACTOR -> recruitment and coercion",
            "RULE -> grievance is vulnerability, not automatic violence",
        ], ["Land-forest causes", "Development-governance causes"]),
        common.panel("Mineral-extortion loop", "causal-chain", [
            "MINERAL / INFRASTRUCTURE ACTIVITY",
            "-> CONTRACTING AND MOVEMENT OF FUNDS",
            "-> EXTORTION OPPORTUNITY",
            "-> FINANCE FOR COERCIVE CONTROL",
            "QUALIFY -> resource wealth is not itself the cause",
        ], ["Mineral-extortion nexus"]),
        common.panel("Instrumental underdevelopment", "feedback-loop", [
            "POVERTY / ADMINISTRATIVE GAP -> RECRUITMENT VULNERABILITY",
            "MAOIST OBSTRUCTION -> ROADS / POWER / WATER DELAYED",
            "DELAY -> PARALLEL AUTHORITY PERSISTS",
            "PERSISTENCE -> FURTHER OBSTRUCTION",
        ], ["Instrumental underdevelopment"]),
        common.panel("People-affected map", "branch-map", [
            "LIFE / SAFETY -> violence and coercion",
            "LIVELIHOOD -> extortion, displacement, forest insecurity",
            "SERVICES -> roads, schools, health access blocked",
            "GOVERNANCE -> panchayat and justice presence weakened",
        ], ["Civilian impact"]),
        common.panel("Clear-hold-develop chain", "process-flow", [
            "CLEAR -> secure lawful access",
            "HOLD -> resident police + civil administration",
            "DEVELOP -> rights + services + infrastructure",
            "TRUST -> accountable delivery prevents relapse",
        ], ["Clear-hold-develop"]),
        common.panel("2015 policy tripod", "systems-map", [
            "SECURITY RESPONSE",
            "DEVELOPMENT RESPONSE",
            "RIGHTS AND ENTITLEMENTS OF LOCAL COMMUNITIES",
            "RULE -> no prong substitutes for the others",
        ], ["Three-pronged policy"]),
        common.panel("Rights-governance pair", "comparison-table", [
            "FRA 2006 -> individual and community forest-right claims",
            "PESA 1996 -> Gram Sabha role in Fifth Schedule governance",
            "ENACTMENT -> legal basis",
            "IMPLEMENTATION -> separate verified outcome",
        ], ["FRA rights boundary", "PESA governance boundary"]),
        common.panel("Inter-State pressure map", "institution-map", [
            "CHHATTISGARH | ODISHA | MAHARASHTRA | FORMER ANDHRA REGION",
            "PRESSURE IN ONE STATE -> MOVEMENT TOWARD ANOTHER",
            "DIFFERING POLICIES -> exploitable discontinuity",
            "RESPONSE -> shared intelligence and compatible strategy",
        ], ["Inter-State trijunction", "Specialised-force lesson"]),
        common.panel("Surrender status firewall", "status-ladder", [
            "SURRENDER -> one-time recorded event",
            "SCREENING / PACKAGE -> administrative steps",
            "LIVELIHOOD / SAFETY -> rehabilitation process",
            "SOCIAL REINTEGRATION -> long-term outcome",
        ], ["Surrender-rehabilitation firewall"]),
        common.panel("Outcome and answer spine", "answer-spine", [
            "DEFINE -> CAUSES -> ACTOR / EXTORTION -> PEOPLE AFFECTED",
            "MAP -> SECURITY + DEVELOPMENT + RIGHTS + TRUST",
            "TEST -> CLEAR / HOLD / DEVELOP + INTER-STATE COORDINATION",
            "GRADE -> TARGET / METRIC / DISTRICT LABEL / QUALIFIED STATUS",
            "CONCLUDE -> TRUSTED CONSTITUTIONAL GOVERNANCE WITHOUT PARALLEL COERCION",
        ], ["Dated decline metrics", "Post-deadline status"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018", "GS-III",
            "Left Wing Extremism challenges and the Government's counter-strategy.",
            "Audited neutral rendering; Explain · 10 marks · 150 words; stem verified against the official scan.",
            [0, 1, 4, 5, 6, 8, 10, 11],
        ),
        common.make_pyq_solution(
            facts, "2020", "GS-III",
            "Left-wing extremism determinants in eastern India and a differentiated strategy for Government, civil administration and security forces.",
            "Audited neutral rendering; What are/strategy · 15 marks · 250 words.",
            [4, 5, 6, 7, 9, 10, 12, 13, 15, 16],
        ),
        common.make_pyq_solution(
            facts, "2022", "GS-III",
            "Naxalism as an internal-security threat and the required multilayered response strategy.",
            "Audited neutral rendering; Discuss · 15 marks · 250 words.",
            [1, 6, 7, 8, 9, 10, 11, 17],
        ),
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "\"The Government of India recently stated that Left Wing Extremism (LWE) will be eliminated by 2026. What do you understand by LWE and how are the people affected by it? What measures have been taken by the government to eliminate LWE?\"",
            "Verbatim owner-preserved question; Explain · 10 marks · 150 words.",
            [1, 4, 5, 7, 8, 9, 10, 12, 13, 18, 19],
        ),
    ]
    return common.topic(
        3, "Left-Wing Extremism and Integrated Response",
        "03_Left-Wing-Extremism-and-Integrated-Response", facts, traps,
        [
            (10, "Explain why LWE is not merely a law-and-order problem.", [1, 4, 5, 6, 7]),
            (10, "Describe how people are affected by LWE and identify the State's immediate duties.", [8, 9, 11]),
            (15, "Analyse the determinants of LWE in eastern India and assign roles to Government, civil administration and security forces.", [4, 5, 6, 7, 9, 10, 12, 13, 15]),
            (15, "Discuss the security-development-rights strategy for countering Naxalism.", [9, 10, 11, 12, 13, 14, 16]),
            (20, "Evaluate whether India's reported LWE decline represents durable root-cause resolution.", [4, 5, 7, 9, 12, 13, 17, 18, 19]),
            (20, "Examine LWE through clear-hold-develop, inter-State coordination and surrender-rehabilitation outcomes.", [6, 8, 9, 10, 11, 15, 16, 17, 19]),
        ],
        titles, routes, panels,
        [
            "Naxalbari", "Charu Majumdar", "Kanu Sanyal",
            "Protracted People's War", "Preparatory", "CPI (Maoist)",
            "jal-jangal-zameen", "Forest Rights Act", "PESA",
            "Fifth Schedule", "First Schedule", "Dandakaranya",
            "Greyhounds", "psychological operations", "effectively free",
        ],
        "The audited GS-III ledgers route the 2018, 2020, 2022 and 2025 LWE demands here. The module preserves directive and marks metadata, grades dated official claims, and does not infer tactical details or objective keys.",
        pyqs, LIVE_ATTEMPTS,
        "The December 2025 MHA metrics and the June 2026 PIB phrase 'effectively free from Left-Wing Extremism' are kept as separate dated claims. Neither proves zero violence, completed rehabilitation, implemented forest rights or irreversible grievance resolution.",
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "IDEOLOGY, CAUSATION AND PEOPLE-AFFECTED MAP",
            "SECURITY, DEVELOPMENT, RIGHTS AND FEDERAL RESPONSE",
            "CLEAR-HOLD-DEVELOP AND REINTEGRATION ANSWER SPINE",
            "DATED METRICS, QUALIFIED STATUS AND CLAIM FIREWALL",
        ),
        register_answer_spine=[
            "DEFINE LWE AS MAOIST STATE-POWER CAPTURE NOT SECESSION",
            "SEPARATE STRUCTURAL GRIEVANCE FROM ORGANISED COERCIVE CONVERSION",
            "EXPLAIN LAND FOREST GOVERNANCE MINERAL AND EXTORTION LINKS",
            "SHOW EFFECTS ON PEOPLE SERVICES LIVELIHOODS AND LOCAL INSTITUTIONS",
            "APPLY SECURITY DEVELOPMENT RIGHTS AND TRUST-RESTORATION TRACKS",
            "TEST CLEAR HOLD DEVELOP AND INTER-STATE COORDINATION",
            "SEPARATE SURRENDER REHABILITATION DISTRICT LABEL AND OUTCOME",
            "CONCLUDE WITH TRUSTED GOVERNANCE AND RELAPSE PREVENTION",
        ],
    )


TOPIC_03 = _build()
