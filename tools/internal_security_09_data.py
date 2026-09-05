"""Authored learner-v2 data for Internal Security Topic 09."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.meity.gov.in/content/information-technology-"
        "intermediary-guidelines-and-digital-media-ethics-code-rules-2021 "
        "and https://www.pib.gov.in/ — attempted 2026-09-04 for the current "
        "Intermediary Rules and official deepfake or misinformation advisories; "
        "direct retrieval returned 403. The module therefore retains only the "
        "owner-audited rule functions and does not infer amendment, compliance "
        "or takedown outcomes."
    ),
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the "
        "Information Technology Act, 2000 and Telecommunications Act, 2023; "
        "direct retrieval returned 403. Sections 69A and 79 and the "
        "telecommunications-suspension framework are used only as audited legal "
        "anchors, never as proof that a restriction was necessary in a case."
    ),
    (
        "https://i4c.mha.gov.in/ — fetched 2026-09-04; the official portal "
        "identifies the Indian Cyber Crime Coordination Centre under the "
        "Ministry of Home Affairs and displayed a 31 August 2025 cybercrime-"
        "awareness activity. This supports the institutional identity only, not "
        "a content-governance, attribution or information-warfare mandate."
    ),
    (
        "https://www.cert-in.org.in/PDF/Advisory_fake_news.pdf and "
        "https://www.pib.gov.in/ — fetched and attempted 2026-09-04; the "
        "CERT-In URL returned an official 'requested URL is not found' page and "
        "PIB retrieval returned 403. No current deepfake duty, detection rate, "
        "platform action or attribution claim is imported from either attempt."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Platform-intermediary distinction", "A social-media platform enables users to create, share and amplify content, while an intermediary's legal duties arise from the IT Act and rules; platform design, user speech and State restriction are separate analytical layers."),
        ("Dual-use communication", "The speed, reach and decentralisation that support participation, awareness and emergency communication can also amplify intimidation, radicalisation, fraud, communal incitement and hostile narratives."),
        ("End-to-end encryption", "End-to-end encryption is designed so message content is readable at the communicating endpoints rather than by the service in transit; it protects legitimate privacy and security while complicating some lawful investigations."),
        ("Encryption-anonymity boundary", "Encryption protects content, whereas anonymity or pseudonymity concerns identity; encrypted content does not by itself prove an anonymous actor, unlawful conduct or foreign direction."),
        ("Lawful-access debate", "Rule 4(2) of the 2021 Intermediary Rules concerns identification of the first originator on a specified lawful order in defined serious cases; it is distinct from a general content-decryption demand and remains architecturally contested."),
        ("Misinformation", "Misinformation is false or misleading content shared without the necessary intent to deceive; correction, trusted communication and literacy are central responses."),
        ("Disinformation", "Disinformation is false or manipulated content deliberately created or spread to deceive; intent, coordination, amplification and attribution therefore matter."),
        ("Malinformation", "Malinformation is genuine information used maliciously or out of context; because the underlying material may be true, contextual rebuttal and proportional process are especially important."),
        ("Propaganda-influence-warfare ladder", "Propaganda is systematic persuasion, an influence operation coordinates activity to shape a target audience, and information warfare uses information effects as part of a strategic contest; the labels are related but not interchangeable."),
        ("Information-operation chain", "A sound analysis traces actor, narrative or content, platform or network amplification, targeted audience and behavioural or institutional consequence without assuming that reach proves persuasion or control."),
        ("Deepfake boundary", "A deepfake is synthetic or manipulated audio-visual media generated using AI techniques; detection or virality does not establish the creator, intent, target, legal offence or strategic sponsor."),
        ("Attribution ladder", "Attribution should move from content and technical indicators to coordination patterns, infrastructure control, intelligence assessment, legal evidence and any public political finding, with confidence stated at each rung."),
        ("Intermediary-duties map", "Rules 3 and 4(1) structure due diligence, grievance and compliance roles for covered intermediaries, while Rule 7 links non-observance to loss of Section 79 safe harbour; duties do not make platforms courts or universal publishers."),
        ("Blocking-process boundary", "Section 69A permits blocking public access for specified statutory purposes through prescribed process; the existence of power is not proof that a particular blocking direction is lawful, necessary or proportionate."),
        ("Network-restriction boundary", "Section 20 of the Telecommunications Act, 2023 concerns specified interception or transmission-suspension powers subject to legal purpose and safeguards; Anuradha Bhasin requires publication, review, necessity, proportionality and rejects indefinite suspension."),
        ("Section 66A status", "Section 66A of the IT Act was struck down in Shreya Singhal v. Union of India in 2015 and cannot be cited as a current offence for objectionable online speech."),
        ("Cyber-content firewall", "CERT-In responds to cyber incidents, I4C supports cybercrime coordination and State police investigate offences, while a foreign information operation additionally requires intelligence and diplomatic assessment; cybersecurity is not content governance."),
        ("Extraterritorial limit", "Foreign platforms, infrastructure and state-linked influence activity create jurisdiction and evidence-access limits that domestic takedown law alone cannot solve, making bounded international and platform cooperation necessary."),
        ("Rights-proportionality test", "A legitimate response should identify legal authority, legitimate aim, suitability, necessity, least-restrictive design, transparency, independent review and remedy while protecting privacy and free expression; proportionality as a decided standard, not an aspiration, must govern the final restriction."),
        ("Information-resilience end-state", "Durable security combines rapid verification, trusted public communication, provenance and platform process, lawful investigation, digital and media literacy, community early warning, international cooperation and qualified attribution."),
    ]
    traps = [
        "Do not use platform, intermediary, user and State as one legal actor.",
        "Do not treat social media as inherently beneficial or inherently harmful.",
        "Do not describe end-to-end encryption as anonymity or illegality.",
        "Do not convert Rule 4(2) into a settled general decryption mandate.",
        "Do not use misinformation, disinformation and malinformation as synonyms.",
        "Do not call every persuasive message propaganda or information warfare.",
        "Do not infer creator, intent or sponsor from a detected deepfake.",
        "Do not attribute a foreign influence operation from virality or server location alone.",
        "Do not equate intermediary due diligence with unreviewable State censorship.",
        "Do not cite Section 66A as current law.",
        "Do not collapse a cyber incident, cybercrime and information operation.",
        "Do not present shutdown, blanket encryption weakening or mass removal as the default remedy.",
    ]
    titles = [
        "Social-media platforms intermediaries and dual use",
        "End-to-end encryption and anonymity distinction",
        "Rule 4(2) first-originator lawful-access debate",
        "Misinformation disinformation and malinformation",
        "Propaganda influence operations and information warfare",
        "Information-operation actor-content-audience chain",
        "Deepfakes provenance and evidence status",
        "Attribution confidence and foreign-operation claims",
        "Intermediary due diligence officers and safe harbour",
        "Section 69A blocking and procedural limits",
        "Telecommunications suspension and Anuradha Bhasin",
        "Section 66A and Shreya Singhal correction",
        "CERT-In I4C State police and content-governance firewall",
        "Extraterritorial cooperation and platform jurisdiction",
        "Rights-conscious information resilience",
    ]
    routes = [
        "Separate platform function, intermediary duty, user conduct and State power.",
        "Define content protection and identity concealment before discussing misuse.",
        "State legal trigger, requested output, technical objection and unresolved status.",
        "Classify truth value and intent before selecting the remedy.",
        "Fix actor, objective, coordination and strategic context before using the label.",
        "Trace the full chain and stop short of assuming behavioural effect.",
        "Separate synthetic-media detection from creator, intent and legal attribution.",
        "State the evidence rung and confidence before naming a sponsor.",
        "Distinguish due diligence, lawful order, liability and adjudication.",
        "Name purpose, procedure, necessity, proportionality and remedy.",
        "Treat network restriction as exceptional, written, reviewable and time-bound.",
        "Remove obsolete-law options before analysing current remedies.",
        "Route technical incident, penal offence and hostile operation separately.",
        "Pair domestic process with bounded cross-border evidence cooperation.",
        "Conclude with trusted communication, literacy, due process and qualified attribution.",
    ]
    panels = [
        common.panel("Platform-actor map", "institution-map", [
            "USER -> CREATES / SHARES CONTENT",
            "PLATFORM -> HOSTS / RECOMMENDS / AMPLIFIES",
            "INTERMEDIARY DUTY -> DUE PROCESS / GRIEVANCE / COMPLIANCE",
            "STATE -> LAWFUL ORDER / INVESTIGATION / REVIEW",
            "RULE -> four actors, not one undifferentiated speaker",
        ], ["Platform-intermediary distinction"]),
        common.panel("Dual-use communication balance", "balance-scale", [
            "GAIN -> PARTICIPATION / AWARENESS / EMERGENCY COMMUNICATION",
            "RISK -> RADICALISATION / INCITEMENT / FRAUD / HOSTILE NARRATIVE",
            "SAME ENABLER -> SPEED + REACH + DECENTRALISATION",
            "VERDICT -> govern misuse without destroying legitimate security",
        ], ["Dual-use communication"]),
        common.panel("Encryption lawful-access matrix", "comparison-table", [
            "E2EE -> CONTENT READABLE AT ENDPOINTS",
            "ANONYMITY -> IDENTITY CONCEALMENT",
            "RULE 4(2) -> FIRST ORIGINATOR ON DEFINED ORDER",
            "DISPUTE -> METADATA REQUEST / SYSTEM ARCHITECTURE EFFECT",
            "NOT THE ANSWER -> blanket weakening",
        ], ["End-to-end encryption", "Encryption-anonymity boundary", "Lawful-access debate"]),
        common.panel("Information-disorder taxonomy", "comparison-table", [
            "MISINFORMATION -> FALSE / NO NECESSARY DECEPTIVE INTENT",
            "DISINFORMATION -> FALSE OR MANIPULATED / DELIBERATE",
            "MALINFORMATION -> GENUINE / MALICIOUS CONTEXT OR USE",
            "REMEDY -> correction | attribution | contextual rebuttal",
        ], ["Misinformation", "Disinformation", "Malinformation"]),
        common.panel("Influence-label ladder", "status-ladder", [
            "PERSUASIVE CONTENT",
            "-> SYSTEMATIC PROPAGANDA",
            "-> COORDINATED INFLUENCE OPERATION",
            "-> STRATEGIC INFORMATION WARFARE",
            "RULE -> prove actor, coordination, objective and context",
        ], ["Propaganda-influence-warfare ladder"]),
        common.panel("Information-operation chain", "process-flow", [
            "ACTOR -> NARRATIVE / CONTENT",
            "-> PLATFORM / NETWORK AMPLIFICATION",
            "-> TARGETED AUDIENCE",
            "-> BEHAVIOURAL / INSTITUTIONAL CONSEQUENCE",
            "TRAP -> reach is not proof of persuasion",
        ], ["Information-operation chain"]),
        common.panel("Deepfake evidence ladder", "decision-tree", [
            "SYNTHETIC / MANIPULATED MEDIA DETECTED",
            "-> VERIFY PROVENANCE + CONTEXT",
            "-> ASSESS INTENT / COORDINATION / HARM",
            "-> PRESERVE EVIDENCE + CORRECT / INVESTIGATE",
            "NOT PROVED -> creator, sponsor or offence",
        ], ["Deepfake boundary", "Attribution ladder"]),
        common.panel("Intermediary law map", "institution-map", [
            "RULE 3 -> DUE DILIGENCE / GRIEVANCE",
            "RULE 4(1) -> SIGNIFICANT-INTERMEDIARY COMPLIANCE ROLES",
            "RULE 7 -> SECTION 79 SAFE-HARBOUR CONSEQUENCE",
            "SECTION 69A -> PRESCRIBED BLOCKING PROCESS",
            "RULE -> duty and a specific lawful order remain distinct",
        ], ["Intermediary-duties map", "Blocking-process boundary"]),
        common.panel("Restriction proportionality rail", "audit-ladder", [
            "LEGAL AUTHORITY + LEGITIMATE AIM",
            "-> SUITABILITY + NECESSITY",
            "-> LEAST-RESTRICTIVE / TIME-BOUND DESIGN",
            "-> PUBLICATION / REVIEW / REMEDY",
            "ANURADHA BHASIN -> no indefinite suspension",
        ], ["Network-restriction boundary", "Rights-proportionality test"]),
        common.panel("Incident-crime-operation firewall", "comparison-table", [
            "CYBER INCIDENT -> CERT-In / ENTITY RESPONSE",
            "CYBERCRIME -> STATE POLICE / I4C SUPPORT",
            "INFORMATION OPERATION -> INTELLIGENCE + LEGAL + DIPLOMATIC ASSESSMENT",
            "CONTENT GOVERNANCE -> platform and lawful-process layer",
        ], ["Cyber-content firewall"]),
        common.panel("Cross-border attribution ladder", "status-ladder", [
            "CONTENT / TECHNICAL INDICATOR",
            "-> COORDINATION / INFRASTRUCTURE CONTROL",
            "-> INTELLIGENCE + LEGAL EVIDENCE",
            "-> PUBLIC POLITICAL FINDING",
            "LIMIT -> jurisdiction and evidence access",
        ], ["Attribution ladder", "Extraterritorial limit"]),
        common.panel("PYQ and resilience rail", "answer-spine", [
            "2024 GS-III -> MULTI-LEVEL MEASURES + OTHER REMEDIES",
            "2025 GS-IV -> CROSS-OWNED ETHICAL DILEMMAS",
            "2023 GS-IV -> CROSS-OWNED CYBERBULLYING CASE",
            "END -> VERIFY / COMMUNICATE / GOVERN / INVESTIGATE / EDUCATE",
            "QUALIFY -> rights, evidence status and attribution confidence",
        ], ["Information-resilience end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2024", "GS-III",
            "Security challenge posed by social media and encrypted messaging, measures adopted at different levels, and additional remedies.",
            "Printed stem is routed to this owner; Suggest measures · 15 marks · 250 words.",
            [0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 16, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2025", "GS-IV",
            "Ethical dilemmas created by social media in the digital age.",
            "Conservative cross-owned concept card routed to Ethics; Section A · 10 marks · 150 words. It is used here only for platform, truth, privacy and proportionality distinctions.",
            [0, 1, 5, 6, 7, 10, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2023", "GS-IV",
            "Case involving cyberbullying and a retaliatory social-media video by a senior public official.",
            "Conservative cross-owned case-study card routed to Ethics; 20 marks · 250 words. No official model solution is inferred.",
            [0, 1, 5, 6, 9, 10, 18, 19],
        ),
    ]
    return common.topic(
        9, "Social Media, Encrypted Messaging and Information Warfare",
        "09_Social-Media-Encrypted-Messaging-and-Information-Warfare", facts, traps,
        [
            (10, "Distinguish misinformation, disinformation and malinformation and match each with a proportionate response.", [5, 6, 7, 9, 18, 19]),
            (10, "Explain why end-to-end encryption and anonymity must not be treated as the same security problem.", [2, 3, 4, 18]),
            (15, "Assess measures adopted at different levels to address the security implications of social media and encrypted messaging.", [0, 1, 2, 4, 9, 12, 13, 14, 16, 18, 19]),
            (15, "Examine deepfakes as an information-security challenge while preserving attribution and rights safeguards.", [6, 7, 9, 10, 11, 18, 19]),
            (20, "Critically evaluate India's platform-accountability and lawful-access architecture without collapsing cybersecurity into content governance.", [0, 2, 4, 12, 13, 14, 15, 16, 18, 19]),
            (20, "Design a whole-of-government information-resilience strategy for state-linked and non-state influence operations.", [1, 5, 6, 7, 8, 9, 10, 11, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "social media", "end-to-end encryption", "misinformation",
            "disinformation", "malinformation", "propaganda",
            "hybrid warfare", "deepfake", "Rule 4(2)",
            "first originator", "Rule 7", "Section 79 safe harbour",
            "Section 69A", "Telecommunications Act, 2023",
            "Section 20", "Anuradha Bhasin", "Shreya Singhal", "Christchurch Call",
            "I4C", "State police",
        ],
        "The routed ledger gives this topic one direct GS-III demand in 2024. To preserve exactly three conservative cards, the 2025 GS-IV social-media ethics demand and 2023 GS-IV cyberbullying case are included only as explicitly cross-owned applications; neither is relabelled as an Internal Security PYQ.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts on 2026-09-04 left the MeitY, PIB and India Code pages blocked, while the I4C portal confirmed only its MHA institutional identity and a dated awareness activity. The module therefore makes no current platform-compliance, takedown, shutdown, deepfake-detection, attribution or harm-reduction outcome claim.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "PLATFORMS, ENCRYPTION AND INFORMATION-DISORDER TAXONOMY",
            "INTERMEDIARY DUTIES, RESTRICTIONS AND ATTRIBUTION FIREWALLS",
            "DEEPFAKES, INFLUENCE OPERATIONS AND THREE CONSERVATIVE PYQ SPINES",
            "PROPORTIONALITY, TRUSTED COMMUNICATION AND INFORMATION RESILIENCE",
        ),
        register_answer_spine=[
            "SEPARATE USER PLATFORM INTERMEDIARY AND STATE",
            "DEFINE E2EE AND KEEP ENCRYPTION DISTINCT FROM ANONYMITY",
            "CLASSIFY MISINFORMATION DISINFORMATION OR MALINFORMATION",
            "TRACE ACTOR CONTENT AMPLIFICATION AUDIENCE AND CONSEQUENCE",
            "DISTINGUISH PROPAGANDA INFLUENCE OPERATION AND INFORMATION WARFARE",
            "MAP RULES 3 4(1) 4(2) 7 SECTION 79 AND SECTION 69A",
            "STATE ATTRIBUTION EVIDENCE CONFIDENCE AND EXTRATERRITORIAL LIMIT",
            "CONCLUDE WITH PROPORTIONALITY TRUST LITERACY REVIEW AND REMEDY",
        ],
    )


TOPIC_09 = _build()
