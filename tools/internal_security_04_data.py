"""Authored learner-v2 data for Internal Security Topic 04."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/sites/default/files/AREnglish_24032026.pdf "
        "— attempted 2026-09-04; direct retrieval returned 403, while the "
        "canonical owner uses the MHA Annual Report 2024-25 for dated accord "
        "mapping. The module does not infer implementation from signature."
    ),
    (
        "https://pib.gov.in/FeaturesDeatils.aspx?NoteId=151186&ModuleId=2 "
        "— searched 2026-09-04; the official PIB feature provides a public "
        "North-East peace-and-accord overview. Every entry remains classified "
        "as ceasefire, framework, settlement or separately verified "
        "implementation rather than one undifferentiated success count."
    ),
    (
        "https://www.mha.gov.in/ — searched 2026-09-04 for the 2026 AFSPA "
        "disturbed-area notifications and the 23 April 2026 North-East "
        "peace-process update. The module preserves notification-specific and "
        "time-bound status without treating reduced coverage as repeal."
    ),
    (
        "https://www.indiacode.nic.in/ — searched 2026-09-04 for AFSPA 1958 "
        "and constitutional autonomy provisions; the module uses sections 3, "
        "4 and 6 plus Articles 244(2), 371A and 371C as owner-audited legal "
        "anchors, not as proof of current field conditions."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Historical-isolation condition", "British excluded-area policy, limited links with the wider freedom struggle and distinct missionary and administrative experiences shaped later identity and alienation in the North-East."),
        ("Assamisation trigger", "The 1960 Assamese official-language decision generated strong tribal-district resistance and fear of identity loss, illustrating how a proximate policy trigger can activate a deeper historical condition."),
        ("Statehood accommodation", "Nagaland became a State in 1963; Meghalaya, Manipur and Tripura in 1972; Mizoram and Arunachal Pradesh in 1987, showing political accommodation through territorial reorganisation."),
        ("Sixth Schedule boundary", "The Sixth Schedule under Articles 244(2) and 275(1) applies to tribal areas of Assam, Meghalaya, Tripura and Mizoram through Autonomous District and Regional Councils; it does not cover the entire North-East."),
        ("Articles 371A-371C boundary", "Nagaland's special constitutional protection operates through Article 371A, while Manipur's hill-area mechanism is linked to Article 371C; these are not substitutes for the Sixth Schedule."),
        ("Insurgency-driver matrix", "Identity and autonomy claims, inter-ethnic tension, demographic anxieties, underdevelopment, weak governance, difficult terrain, arms or narcotics routes and cross-border sanctuary interact differently across States."),
        ("Myanmar-border linkage", "Shared ethnic ties, terrain and cross-border movement make Myanmar a major external linkage for North-East insurgency; current sanctuary or group claims require dated official evidence."),
        ("Composite strategy", "The Government's composite approach combines talks with groups abjuring violence, lawful action against continuing violence, development and connectivity, and political or autonomy arrangements."),
        ("SoO boundary", "A Suspension of Operations agreement is a renewable, revocable cessation-of-hostilities arrangement with ground rules; it is not disarmament, a final political settlement or verified rehabilitation."),
        ("Framework-agreement boundary", "A framework agreement records agreed principles for future negotiation but leaves competencies, territory or implementation open; the NSCN (IM) Framework Agreement of 3 August 2015 is not a final settlement."),
        ("Settlement boundary", "A Memorandum of Settlement or accord records specified commitments, but signature alone does not prove council formation, legal amendment, package disbursement, disbandment or reintegration."),
        ("Implementation boundary", "Implementation is the separate rung where constitutional, statutory, financial and rehabilitation commitments are verified; accord counts cannot substitute for an implementation audit."),
        ("Past-decade accord map", "The owner maps the 2019 NLFT(SD), 2020 Bodo and Bru-Reang, 2021 Karbi Anglong, 2022 boundary and Adivasi-group, 2023 DNLA, UNLF and ULFA pro-talks, and 2024 TIPRA Motha instruments, each requiring exact status."),
        ("UPF-KNO SoO status", "Revised tripartite Suspension of Operations ground rules with UPF and KNO were signed on 4 September 2025 and stated to run through 3 September 2026; this is a ceasefire rung, not a Manipur settlement."),
        ("AFSPA sections", "Under AFSPA 1958, section 3 governs disturbed-area declaration, section 4 confers specified powers in a notified area, and section 6 requires previous Central Government sanction before prosecution."),
        ("Notification-repeal firewall", "Shrinking or withdrawing a disturbed-area notification ends AFSPA's operation only in the de-notified area for that notification period; it neither repeals the Act nor proves final peace."),
        ("AFSPA judicial boundary", "Naga People's Movement of Human Rights (1997) upheld AFSPA with binding safeguards, while EEVFAM (2016) rejected absolute immunity and kept alleged excessive force open to investigation."),
        ("FMR decision boundary", "MHA announced on 8 February 2024 a decision to scrap the India-Myanmar Free Movement Regime; an announcement must not be stated as the complete operational regime without the governing notification."),
        ("Assam-Rifles mandate issue", "The owner identifies a border-guarding versus counter-insurgency mandate tension for Assam Rifles along the Myanmar border; current deployments and force numbers require dated official verification."),
        ("Peace-process end-state", "Durable peace requires State- and faction-specific accommodation, lawful and accountable security, inter-ethnic reconciliation, border governance and verified implementation rather than signatures alone."),
    ]
    traps = [
        "Do not treat the North-East as one homogeneous insurgency.",
        "Do not treat every autonomy demand as a Sixth Schedule demand.",
        "Do not confuse SoO, framework agreement, settlement and implementation.",
        "Do not call an SoO disarmament or rehabilitation.",
        "Do not call the 2015 Framework Agreement a final Naga settlement.",
        "Do not treat accord signature as implemented peace.",
        "Do not equate reduced disturbed-area coverage with AFSPA repeal.",
        "Do not describe AFSPA as absolute immunity.",
        "Do not convert the 2024 FMR decision into operational abolition without notification.",
        "Do not carry book-period group strength or status into the present.",
        "Do not use border hardening as the only peace-process answer.",
        "Do not publish tactical camp, movement or force-deployment detail.",
    ]
    titles = [
        "Historical isolation identity and alienation",
        "Assamisation statehood and accommodation",
        "Sixth Schedule and differentiated autonomy",
        "Identity border development and governance drivers",
        "Myanmar linkages and attribution discipline",
        "Composite strategy talks security and development",
        "Suspension of Operations ceasefire rung",
        "Framework agreement and settlement distinction",
        "Implementation audit and accord mapping",
        "Past-decade State and faction map",
        "UPF KNO SoO and Manipur process status",
        "AFSPA sections notification and repeal boundary",
        "AFSPA necessity accountability and judicial safeguards",
        "FMR decision and border-community trade-offs",
        "Assam Rifles mandate and durable peace end-state",
    ]
    routes = [
        "Explain historical condition without making it a deterministic cause.",
        "Use territorial reorganisation as political accommodation evidence.",
        "Name the exact constitutional instrument for the exact State.",
        "Map drivers State by State rather than homogenising the region.",
        "Separate cross-border vulnerability from current group attribution.",
        "Show accommodation and lawful coercion as parallel calibrated tracks.",
        "State ground-rule purpose and stop before disarmament claims.",
        "Identify the rung before assessing progress.",
        "Audit legal, fiscal and reintegration follow-through separately.",
        "Use date, State, faction and instrument type in every map entry.",
        "Keep the 2025-26 instrument at ceasefire status.",
        "Separate the Act, notification footprint and repeal.",
        "Balance operational necessity with investigation and accountability.",
        "Distinguish announced policy from notified implementation and livelihood effects.",
        "Conclude with reconciliation, accountable security and verified delivery.",
    ]
    panels = [
        common.panel("Isolation-to-identity chain", "causal-chain", [
            "EXCLUDED-AREA GOVERNANCE + LIMITED WIDER CONTACT",
            "-> DISTINCT IDENTITY AND POLITICAL EXPERIENCE",
            "-> POST-INDEPENDENCE ASSIMILATION FEAR",
            "-> AUTONOMY / STATEHOOD DEMANDS",
        ], ["Historical-isolation condition", "Assamisation trigger"]),
        common.panel("Statehood timeline", "timeline", [
            "1963 -> NAGALAND",
            "1972 -> MEGHALAYA / MANIPUR / TRIPURA",
            "1987 -> MIZORAM / ARUNACHAL PRADESH",
            "LESSON -> political accommodation can change conflict incentives",
        ], ["Statehood accommodation"]),
        common.panel("Autonomy instrument map", "comparison-table", [
            "SIXTH SCHEDULE -> Assam, Meghalaya, Tripura, Mizoram tribal areas",
            "ARTICLE 371A -> Nagaland",
            "ARTICLE 371C -> Manipur hill-area mechanism",
            "RULE -> autonomy instruments are not interchangeable",
        ], ["Sixth Schedule boundary", "Articles 371A-371C boundary"]),
        common.panel("Challenge matrix", "matrix", [
            "IDENTITY / AUTONOMY | INTER-ETHNIC TENSION",
            "BORDER / SANCTUARY | ARMS / NARCOTICS ROUTES",
            "UNDERDEVELOPMENT | GOVERNANCE / TRUST DEFICIT",
            "ANSWER -> identify State, actor and dominant pathway",
        ], ["Insurgency-driver matrix", "Myanmar-border linkage"]),
        common.panel("Composite response system", "systems-map", [
            "TALKS / ACCORDS -> accommodation",
            "LAWFUL SECURITY -> contain continuing violence",
            "DEVELOPMENT / CONNECTIVITY -> reduce isolation",
            "AUTONOMY / REPRESENTATION -> political end-state",
        ], ["Composite strategy"]),
        common.panel("Peace-instrument ladder", "status-ladder", [
            "1 SOO / CEASEFIRE",
            "2 FRAMEWORK AGREEMENT",
            "3 MEMORANDUM OF SETTLEMENT / ACCORD",
            "4 VERIFIED IMPLEMENTATION",
            "RULE -> each rung proves only itself",
        ], ["SoO boundary", "Framework-agreement boundary", "Settlement boundary", "Implementation boundary"]),
        common.panel("Accord map 2015-2020", "timeline", [
            "2015 NSCN(IM) -> FRAMEWORK",
            "2019 NLFT(SD) -> AGREEMENT",
            "2020 BODO -> SETTLEMENT",
            "2020 BRU-REANG -> PERMANENT-SETTLEMENT AGREEMENT",
        ], ["Past-decade accord map"]),
        common.panel("Accord map 2021-2024", "timeline", [
            "2021 KARBI ANGLONG -> AGREEMENT",
            "2022 ASSAM-MEGHALAYA -> INTER-STATE BOUNDARY AGREEMENT",
            "2023 DNLA / UNLF / ULFA PRO-TALKS -> DISTINCT INSTRUMENTS",
            "2024 TIPRA MOTHA -> TRIPARTITE AGREEMENT",
        ], ["Past-decade accord map"]),
        common.panel("Manipur SoO status", "status-ladder", [
            "4 SEP 2025 -> REVISED UPF / KNO GROUND RULES SIGNED",
            "STATED VALIDITY -> THROUGH 3 SEP 2026",
            "STATUS -> CESSATION-OF-HOSTILITIES RUNG",
            "NOT PROVED -> FINAL SETTLEMENT / DISARMAMENT / REINTEGRATION",
        ], ["UPF-KNO SoO status"]),
        common.panel("AFSPA legal architecture", "institution-map", [
            "SECTION 3 -> DISTURBED-AREA NOTIFICATION",
            "SECTION 4 -> POWERS IN NOTIFIED AREA",
            "SECTION 6 -> PRIOR CENTRAL SANCTION BEFORE PROSECUTION",
            "COURTS -> CONSTITUTIONALITY WITH SAFEGUARDS; NO ABSOLUTE IMMUNITY",
        ], ["AFSPA sections", "AFSPA judicial boundary"]),
        common.panel("FMR and border-policy boundary", "decision-tree", [
            "8 FEB 2024 -> DECISION ANNOUNCEMENT",
            "SECURITY CONCERN -> misuse, movement, narcotics, identity conflict",
            "COMMUNITY COST -> kinship, livelihood and small trade",
            "RULE -> operative regime requires formal notification",
        ], ["FMR decision boundary"]),
        common.panel("PYQ map and end-state", "answer-spine", [
            "CHALLENGES -> IDENTITY / BORDER / DEVELOPMENT / TRUST",
            "MAP -> STATE + FACTION + DATE + INSTRUMENT RUNG",
            "AUDIT -> AFSPA ACCOUNTABILITY + ACCORD IMPLEMENTATION",
            "REFORM -> RECONCILIATION + BORDER GOVERNANCE + CLEAR MANDATES",
            "CONCLUDE -> VERIFIED DELIVERY, NOT SIGNATURE COUNT",
        ], ["Assam-Rifles mandate issue", "Peace-process end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2019", "GS-III",
            "India-Myanmar border security challenges and their connection with insurgency in the North-East.",
            "Audited neutral rendering; Examine · 15 marks · 250 words.",
            [5, 6, 7, 17, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "\"What are the major challenges to internal security and peace process in the North-Eastern States? Map the various peace accords and agreements initiated by the government in the past decade.\"",
            "Verbatim owner-preserved question; Map · 15 marks · 250 words.",
            [0, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 19],
        ),
    ]
    return common.topic(
        4, "North-East Insurgency and Peace Processes",
        "04_North-East-Insurgency-and-Peace-Processes", facts, traps,
        [
            (10, "Explain how historical isolation and identity formation contributed to insurgency in the North-East.", [0, 1, 2, 3, 5]),
            (10, "Distinguish a Suspension of Operations agreement from a political settlement and implementation.", [8, 9, 10, 11, 13]),
            (15, "Examine India-Myanmar border-security challenges and their links with North-East insurgency.", [5, 6, 7, 17, 18, 19]),
            (15, "Map the major internal-security challenges and peace instruments in the North-East over the past decade.", [3, 5, 7, 8, 9, 10, 11, 12, 13]),
            (20, "Critically evaluate AFSPA's operational necessity and accountability architecture in the North-East.", [14, 15, 16, 19]),
            (20, "Assess whether the North-East peace process has moved from accords to durable implementation and inter-ethnic reconciliation.", [2, 3, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "excluded area", "Assamization", "All Party Hill",
            "Articles 244(2)", "275(1)", "Article 371A", "Article 371C",
            "Suspension of Operations", "NSCN (IM)", "Bodo Accord",
            "Karbi Anglong Agreement", "UPF", "KNO", "Section 3",
            "EEVFAM", "Free Movement Regime", "Assam Rifles",
        ],
        "The audited GS-III ledgers route the 2019 India-Myanmar-border demand and the 2025 North-East challenges-and-accord-map demand here. Every instrument retains its date, State or faction and legal/status rung; signature is never rewritten as implementation.",
        pyqs, LIVE_ATTEMPTS,
        "The current anchors are notification- and instrument-specific: the 8 February 2024 FMR decision remains an announcement unless supported by an operative notification; the 4 September 2025 UPF/KNO instrument remains an SoO; and 2026 disturbed-area notifications do not repeal AFSPA.",
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "IDENTITY, AUTONOMY AND CROSS-BORDER CHALLENGE MAP",
            "PEACE-INSTRUMENT LADDER AND PAST-DECADE ACCORD MAP",
            "AFSPA, BORDER GOVERNANCE AND ANSWER-WRITING SPINE",
            "NOTIFICATION, IMPLEMENTATION AND DURABLE-PEACE FIREWALL",
        ),
        register_answer_spine=[
            "BEGIN WITH STATE-SPECIFIC IDENTITY AUTONOMY BORDER AND GOVERNANCE PATHWAYS",
            "NAME THE CORRECT SIXTH-SCHEDULE OR ARTICLE 371 INSTRUMENT",
            "SEPARATE SOO FRAMEWORK SETTLEMENT AND IMPLEMENTATION",
            "MAP DATE STATE FACTION AND INSTRUMENT FOR EVERY ACCORD",
            "BALANCE AFSPA NECESSITY WITH SAFEGUARDS INVESTIGATION AND REMEDY",
            "GRADE FMR DECISION AND DISTURBED-AREA NOTIFICATION PRECISELY",
            "ADDRESS ASSAM RIFLES MANDATE AND BORDER-COMMUNITY COSTS",
            "CONCLUDE ON RECONCILIATION ACCOUNTABLE SECURITY AND VERIFIED DELIVERY",
        ],
    )


TOPIC_04 = _build()
