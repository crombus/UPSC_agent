"""Authored learner-v2 data for Internal Security Topic 02."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/sites/default/files/NCTPolicyStrategy.pdf "
        "— attempted 2026-09-04; the direct PDF fetch returned 403, while "
        "official-domain search and the owner support PRAHAAR's 23 February "
        "2026 release and seven-element policy architecture. No budget, new "
        "agency, arrest power or measured outcome was inferred."
    ),
    (
        "https://www.indiacode.nic.in/handle/123456789/1513 — searched "
        "2026-09-04; the official UAPA source supports the 2019 individual-"
        "designation framework and statutory review route. Designation is "
        "kept separate from arrest, charge-sheet and conviction."
    ),
    (
        "https://www.indiacode.nic.in/bitstream/123456789/1218/1/A2019-16.pdf "
        "— searched 2026-09-04; the official NIA Amendment Act source supports "
        "extraterritorial scheduled-offence jurisdiction and Special Court "
        "changes. It supplies no case outcome or conviction claim."
    ),
    (
        "https://www.indiacode.nic.in/ — searched 2026-09-04 for Bharatiya "
        "Nyaya Sanhita section 113; the module preserves the owner-audited "
        "BNS-UAPA concurrency and SP-rank choice boundary without treating "
        "registration under either law as proof of guilt."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Terrorism definition", "Terrorism is the planned, organised and systematic use of violence as coercion for political, religious or ideological purposes; the owner notes the absence of a universally agreed international definition."),
        ("Terrorism-insurgency-Naxalism", "Terrorism is the broad coercive category, insurgency is armed rebellion with a claimed social base, and Naxalism is Maoist guerrilla violence aimed at capturing state power; the terms are not synonyms."),
        ("State-proxy boundary", "A nominally non-state organisation may receive state finance, sanctuary, logistics or training; proxy use creates deniability but current attribution still requires a dated competent-agency record."),
        ("Manifestation categories", "The owner's India framework separates hinterland terrorism, Jammu and Kashmir militancy, North-East insurgency and Left-Wing Extremism, with dedicated owners for the last three."),
        ("Funding architecture", "Terror funding may involve state sponsorship, extortion, taxation, hawala, counterfeit currency, contraband, charities or organised-crime links; each channel requires separate evidence and belongs in detail to Topic 10."),
        ("Counter-terror chain", "The response chain separates prevention and intelligence, containment and specialised response, investigation by NIA or State police, prosecution in competent courts, finance disruption, and recovery or resilience."),
        ("Post-26/11 build-out", "After the 2008 Mumbai attacks, NIA was created, MAC was strengthened, NATGRID was proposed, NCTC was debated, NSG hubs were added and coastal-security arrangements were revamped; these bodies have different functions."),
        ("NIA boundary", "The NIA Act, 2008 creates a central investigating agency for scheduled offences with concurrent jurisdiction; NIA does not replace the local police's first response, evidence preservation or ordinary policing role."),
        ("MAC-SMAC boundary", "MAC and SMAC are intelligence-sharing and coordination platforms, not arresting, investigating or prosecuting commands."),
        ("NATGRID boundary", "NATGRID is an intelligence data-linkage architecture; its operational status and accessible datasets require a dated official source and must not be inferred from a book-period description."),
        ("NCTC federalism issue", "The proposed NCTC faced objection because independent search, arrest and investigation powers under an intelligence body could bypass State policing competence; the coordination need did not automatically justify centralisation."),
        ("State-police primacy", "Local police ordinarily reach an attack first and secure the scene, witnesses, evidence and public order, making State capacity structurally irreplaceable even in nationally investigated cases."),
        ("UAPA 2019 designation", "The UAPA (Amendment) Act, 2019 permits the Central Government to designate an individual as a terrorist in the Fourth Schedule through executive notification and a statutory review or denotification route."),
        ("Designation-conviction firewall", "Individual designation, arrest, charge-sheet, trial and conviction are five distinct legal and evidentiary events; designation is not a judicial finding of guilt."),
        ("NIA 2019 amendment", "The NIA (Amendment) Act, 2019 extends jurisdiction to specified offences outside India affecting Indian citizens or interests, expands scheduled coverage and permits Sessions Courts to be designated Special Courts."),
        ("BNS-UAPA concurrency", "BNS section 113, in force from 1 July 2024, defines terrorist act in general penal law while UAPA remains the special law; an officer not below SP rank decides which route is invoked."),
        ("UAPA bail boundary", "UAPA section 43D(5) creates a stringent prima-facie-true bail threshold; pre-trial liberty, prosecution and conviction must be analysed separately."),
        ("TADA-POTA precedent", "TADA operated from 1985 to 1995 and POTA from 2002 to 2004 before lapse or repeal amid misuse concerns, illustrating the recurring necessity-accountability tension in special anti-terror law."),
        ("PRAHAAR policy", "PRAHAAR, released by MHA on 23 February 2026, is a national counter-terrorism policy and strategy organised around prevention, response, capacity aggregation, human rights and rule of law, attenuating conditions, international alignment, and recovery or resilience."),
        ("Policy-agency-outcome firewall", "PRAHAAR is a policy framework working through existing institutions; a policy release, search, seizure, arrest or charge-sheet is not a new agency, conviction, reduced-incident figure or verified prevention outcome."),
    ]
    traps = [
        "Do not use terrorism, insurgency and Naxalism as synonyms.",
        "Do not treat a proxy organisation as wholly detached from possible state support.",
        "Do not assert present attribution from book-period descriptions.",
        "Do not merge NIA, MAC, NATGRID, NCTC and NSG.",
        "Do not describe intelligence sharing as admissible proof.",
        "Do not describe NIA as a replacement for State police.",
        "Do not call individual designation a conviction.",
        "Do not say BNS section 113 repealed UAPA.",
        "Do not convert statutory reach into investigative throughput.",
        "Do not omit bail and review safeguards from a legal-power answer.",
        "Do not describe PRAHAAR as a new operational agency.",
        "Do not expose tactical details, identities or unverified incident claims.",
    ]
    titles = [
        "Definition actor and coercive purpose",
        "Terrorism insurgency and Naxalism distinctions",
        "State proxies deniability and attribution",
        "Manifestations of terrorism in India",
        "Funding and logistics architecture",
        "Prevention response investigation prosecution chain",
        "Post-26/11 institutional build-out",
        "NIA jurisdiction and State-police primacy",
        "MAC SMAC NATGRID and information sharing",
        "NCTC federalism and centralisation debate",
        "UAPA 2019 individual designation",
        "Designation arrest charge-sheet trial conviction",
        "NIA Amendment Act 2019 and Special Courts",
        "BNS section 113 UAPA and bail regimes",
        "PRAHAAR seven elements and qualified counter-terror answer",
    ]
    routes = [
        "Open with coercive purpose rather than an incident list.",
        "Define each category before comparing its support base and objective.",
        "Separate actor type, support relationship and attribution evidence.",
        "Use analytical categories and only safely dated examples.",
        "Map finance channels without drifting into unverified transaction detail.",
        "Assign each function to its competent institution.",
        "Explain why institutional multiplication requires coordination.",
        "Pair national jurisdiction with local first-response capacity.",
        "Keep information platforms outside arrest and prosecution functions.",
        "Balance coordination needs against federal and institutional safeguards.",
        "State the security rationale and the executive-notification safeguard.",
        "Preserve every evidentiary rung explicitly.",
        "Name the amendment's jurisdictional changes without claiming outcomes.",
        "Compare legal routes, bail and sanction without treating registration as guilt.",
        "Use the seven elements as a policy frame and finish with rule-of-law legitimacy.",
    ]
    panels = [
        common.panel("Terrorism concept map", "branch-map", [
            "PURPOSE -> political / religious / ideological coercion",
            "METHOD -> planned, organised, systematic violence",
            "ACTOR -> state, proxy, network or individual",
            "OUTCOME SOUGHT -> fear, compliance, legitimacy erosion",
        ], ["Terrorism definition", "State-proxy boundary"]),
        common.panel("Three-category firewall", "comparison-table", [
            "TERRORISM -> broad coercive violence category",
            "INSURGENCY -> armed rebellion with claimed social support",
            "NAXALISM -> Maoist guerrilla route to state power",
            "RULE -> overlap does not erase distinct objectives",
        ], ["Terrorism-insurgency-Naxalism"]),
        common.panel("Manifestation matrix", "matrix", [
            "HINTERLAND MODULES | J&K PROXY VIOLENCE",
            "NORTH-EAST INSURGENCY | LEFT-WING EXTREMISM",
            "FOR EACH -> actor + vulnerability + finance + response",
            "CURRENT EXAMPLE -> use dated official status only",
        ], ["Manifestation categories"]),
        common.panel("Funding disruption chain", "process-flow", [
            "SOURCE -> sponsor / extortion / contraband / charity",
            "TRANSFER -> hawala / cash / counterfeit / digital channel",
            "USE -> recruitment / logistics / propaganda",
            "RESPONSE -> intelligence + financial investigation + prosecution",
        ], ["Funding architecture"]),
        common.panel("Counter-terror function chain", "causal-chain", [
            "PREVENTION / INTELLIGENCE",
            "-> CONTAINMENT / SPECIALISED RESPONSE",
            "-> INVESTIGATION",
            "-> PROSECUTION",
            "-> RECOVERY / RESILIENCE",
        ], ["Counter-terror chain"]),
        common.panel("Post-26/11 institution map", "institution-map", [
            "NIA -> scheduled-offence investigation",
            "MAC / SMAC -> intelligence sharing",
            "NATGRID -> data-linkage architecture",
            "NCTC -> contested centralisation proposal",
            "NSG HUBS -> specialised crisis response",
        ], ["Post-26/11 build-out", "NIA boundary", "MAC-SMAC boundary"]),
        common.panel("Federal response architecture", "systems-map", [
            "STATE POLICE -> first response, scene, evidence, local order",
            "CENTRAL AGENCIES -> scheduled investigation / intelligence support",
            "SPECIAL COURTS -> trial",
            "RULE -> cooperation without institutional substitution",
        ], ["State-police primacy", "NIA boundary"]),
        common.panel("NCTC decision tree", "decision-tree", [
            "NEED -> real-time national coordination",
            "PROPOSED POWER -> search / arrest / investigation",
            "OBJECTION -> State police competence + intelligence-arrest separation",
            "DURABLE MODEL -> coordinated platforms and case-based investigation",
        ], ["NCTC federalism issue"]),
        common.panel("UAPA designation ladder", "status-ladder", [
            "CENTRAL NOTIFICATION -> FOURTH SCHEDULE DESIGNATION",
            "APPLICATION / REVIEW -> STATUTORY ROUTE",
            "ARREST / CHARGE-SHEET -> SEPARATE CRIMINAL PROCESS",
            "CONVICTION -> JUDICIAL FINDING AFTER TRIAL",
        ], ["UAPA 2019 designation", "Designation-conviction firewall"]),
        common.panel("NIA amendment map", "branch-map", [
            "OUTSIDE INDIA -> Indian citizen / interest nexus",
            "EXPANDED SCHEDULE -> specified additional offences",
            "SPECIAL COURTS -> Sessions Courts may be designated",
            "RULE -> jurisdictional power is not a case outcome",
        ], ["NIA 2019 amendment"]),
        common.panel("BNS-UAPA forum choice", "comparison-table", [
            "BNS 113 -> general penal law",
            "UAPA -> special anti-terror law",
            "SP-RANK DECISION -> route selected",
            "CONSEQUENCE -> agency, bail and sanction framework differ",
            "RULE -> both remain in force",
        ], ["BNS-UAPA concurrency", "UAPA bail boundary"]),
        common.panel("PRAHAAR policy rail", "answer-spine", [
            "PREVENT -> RESPOND -> AGGREGATE CAPACITIES",
            "RIGHTS / RULE OF LAW -> ATTENUATE CONDITIONS",
            "ALIGN INTERNATIONALLY -> RECOVER / BUILD RESILIENCE",
            "QUALIFY -> policy, not agency; framework, not outcome",
        ], ["PRAHAAR policy", "Policy-agency-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2019", "GS-III",
            "UAPA and NIA Act amendments in the prevailing security environment.",
            "Audited neutral rendering; Analyse · 15 marks · 250 words. The owner and OCR paper verify the routed demand.",
            [7, 10, 11, 12, 13, 14, 16, 17],
        ),
        common.make_pyq_solution(
            facts, "2021", "GS-III",
            "Terrorism complexity, causes, linkages, nexus and measures for eradication.",
            "Audited neutral rendering; Analyse · 15 marks · 250 words.",
            [0, 2, 3, 4, 5, 11, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "\"Terrorism is a global scourge. How has it manifested in India? Elaborate with contemporary examples. What are the counter measures adopted by the State? Explain.\"",
            "Verbatim owner-preserved question; Elaborate/Explain · 10 marks · 150 words.",
            [0, 2, 3, 5, 6, 7, 8, 18, 19],
        ),
    ]
    return common.topic(
        2, "Terrorism and Counter-Terror Architecture",
        "02_Terrorism-and-Counter-Terror-Architecture", facts, traps,
        [
            (10, "Distinguish terrorism, insurgency and Naxalism in India's internal-security discourse.", [0, 1, 3]),
            (10, "Explain the prevention-to-prosecution counter-terror chain and the institutions at each stage.", [5, 7, 8, 11]),
            (15, "Analyse the UAPA and NIA Act amendments in the prevailing security environment.", [7, 10, 11, 12, 13, 14, 16, 17]),
            (15, "Examine India's cooperative-federal counter-terror architecture with reference to the NCTC controversy.", [6, 7, 8, 10, 11]),
            (20, "Analyse terrorism's causes, linkages and finance-logistics nexus and suggest a calibrated response.", [0, 2, 3, 4, 5, 16, 18, 19]),
            (20, "Critically evaluate PRAHAAR as a policy framework for contemporary terrorism while preserving federalism and rights.", [5, 8, 10, 11, 12, 13, 15, 16, 18, 19]),
        ],
        titles, routes, panels,
        [
            "planned, organised", "Sleeper cell", "hinterland terrorism",
            "state-sponsored", "hawala", "National Investigation Agency",
            "NATGRID", "National Counter Terrorism Centre", "MAC/SMAC",
            "Fourth Schedule", "Inspector or above", "Director General, NIA",
            "Section 43D(5)", "Section 113", "PRAHAAR",
        ],
        "The owner and audited GS-III ledgers route the 2019 UAPA/NIA amendment demand, the 2021 terrorism-complexity demand and the 2025 manifestation/counter-measures demand here. No objective key or unverified contemporary incident attribution is supplied.",
        pyqs, LIVE_ATTEMPTS,
        "PRAHAAR is retained as MHA's 23 February 2026 policy and strategy with seven elements. Its release does not create a new agency or prove prevention, conviction, disruption or incident-reduction outcomes.",
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "TERRORISM DEFINITIONS, ACTORS AND MANIFESTATIONS",
            "INSTITUTIONS, SPECIAL LAWS AND FEDERAL BOUNDARIES",
            "COUNTER-TERROR CHAIN AND PYQ ANSWER SPINE",
            "PRAHAAR, RIGHTS AND EVIDENCE-RUNG FIREWALL",
        ),
        register_answer_spine=[
            "DEFINE TERRORISM AND DISTINGUISH INSURGENCY NAXALISM",
            "CLASSIFY MANIFESTATION ACTOR PROXY AND ATTRIBUTION",
            "TRACE FUNDING LOGISTICS AND VULNERABILITY WITHOUT TACTICAL DETAIL",
            "MAP PREVENTION RESPONSE INVESTIGATION PROSECUTION RECOVERY",
            "SEPARATE NIA MAC SMAC NATGRID NCTC AND STATE POLICE",
            "STATE UAPA DESIGNATION NIA JURISDICTION BNS ROUTE AND BAIL",
            "APPLY PRAHAAR'S SEVEN ELEMENTS",
            "CONCLUDE WITH FEDERAL COOPERATION RULE OF LAW AND VERIFIED STATUS",
        ],
    )


TOPIC_02 = _build()
