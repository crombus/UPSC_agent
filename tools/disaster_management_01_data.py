"""Authored learner-v2 data for Disaster Management Topic 01."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030 "
        "— fetched 2026-09-04; the official page confirms adoption on 18 March "
        "2015, four priorities and seven targets. It was not used as a current "
        "scoreboard for country-level progress."
    ),
    (
        "https://wmo.int/all-activities/build-resilience/early-warnings-all "
        "— fetched 2026-09-04; WMO confirms the end-of-2027 universal-warning "
        "aim, the four end-to-end pillars and WMO-UNDRR co-leadership. No "
        "unverified India coverage percentage was imported."
    ),
    (
        "https://www.undrr.org/implementing-sendai-framework/sendai-framework-action "
        "— searched 2026-09-04; the official UNDRR implementation domain was "
        "used only to cross-check framework terminology, not to invent target "
        "progress or disaster-loss statistics."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Hazard", "A hazard is a dangerous process, phenomenon or condition with the potential to cause loss; it is not itself a disaster."),
        ("Exposure", "Exposure identifies people, livelihoods, infrastructure and other assets located in hazard-prone settings."),
        ("Vulnerability", "Vulnerability comprises physical, social, economic and environmental conditions that increase susceptibility to hazard impacts."),
        ("Capacity", "Capacity is the combination of strengths, attributes and resources available to manage and reduce disaster risks and strengthen resilience."),
        ("Risk heuristic", "Risk is commonly organised as hazard interacting with exposure and vulnerability, moderated by capacity; the equation is a heuristic, not a universal numerical law."),
        ("Disaster threshold", "A disaster is serious disruption produced by hazardous events interacting with exposure, vulnerability and capacity, not a synonym for the triggering hazard."),
        ("Resilience", "Resilience includes resisting, absorbing, accommodating, adapting, transforming and recovering while preserving or restoring essential functions."),
        ("Prevention", "Prevention seeks to avoid existing and new disaster risk where avoidance is feasible; it is distinct from reducing unavoidable risk."),
        ("Mitigation", "Mitigation lessens the adverse impacts of a hazardous event through structural or non-structural measures."),
        ("Preparedness", "Preparedness develops knowledge and capacities for anticipation, response and recovery through plans, training, warning and drills."),
        ("Response", "Response consists of actions taken directly before, during or immediately after a disaster to save life, reduce impacts and meet basic needs."),
        ("Recovery", "Recovery restores or improves livelihoods, health, systems and assets while reducing future risk rather than reproducing prior vulnerability."),
        ("DRR scope", "Disaster risk reduction prevents new risk, reduces existing risk and manages residual risk as part of sustainable development."),
        ("Risk creation", "Land-use, construction, infrastructure and environmental choices can create or accumulate risk even when the underlying hazard does not change."),
        ("Sendai status", "The Sendai Framework for Disaster Risk Reduction 2015-2030 is a voluntary, non-binding global framework adopted on 18 March 2015."),
        ("Sendai priorities", "Sendai's four priorities are understanding risk, strengthening risk governance, investing in DRR for resilience, and preparedness with Build Back Better."),
        ("Targets A-D", "Sendai Targets A-D concern mortality, affected people, direct economic loss relative to global GDP, and damage to critical infrastructure and basic services."),
        ("Targets E-G", "Targets E-G concern national and local DRR strategies, international cooperation, and multi-hazard early warning plus risk information; Target E used a 2020 deadline."),
        ("Framework linkage", "Sendai, climate adaptation, the Paris Agreement and the Sustainable Development Goals overlap in risk-informed development but retain different legal and policy architectures."),
        ("Evidence boundary", "A framework, strategy, investment or warning platform proves an input or mandate; avoided loss and resilience improvement require separate outcome evidence."),
    ]
    traps = [
        "Do not equate a hazard with a disaster.",
        "Do not omit exposure when explaining why identical hazards produce unequal losses.",
        "Do not present the risk equation as a precise universal formula.",
        "Do not merge prevention, mitigation and preparedness.",
        "Do not reduce resilience to restoring the pre-disaster condition.",
        "Do not describe Sendai as a binding treaty.",
        "Do not confuse Sendai priorities with its lettered targets.",
        "Do not turn Target G or EW4All into proof of universal warning coverage.",
        "Do not collapse climate adaptation, DRR and sustainable development into one framework.",
        "Do not infer current target progress without a dated official source.",
    ]
    titles = [
        "Hazard exposure vulnerability and capacity",
        "Risk equation as a disciplined heuristic",
        "Disaster threshold and serious disruption",
        "Resilience beyond bounce back",
        "Prevention and mitigation boundary",
        "Preparedness response and recovery sequence",
        "DRR and residual risk",
        "Risk creation through development choices",
        "Sendai status and architecture",
        "Four Sendai priorities",
        "Seven global targets",
        "Loss targets and means targets",
        "Build Back Better and recovery choices",
        "Climate adaptation and sustainable development linkage",
        "PYQ synthesis and evidence boundary",
    ]
    routes = [
        "Define each risk component before proposing measures.",
        "Use the heuristic to organise causation without claiming false precision.",
        "Show how disruption exceeds coping capacity.",
        "Link robustness, redundancy, resourcefulness and adaptive recovery.",
        "Classify the measure by the risk it avoids or reduces.",
        "Place every intervention in the correct management-cycle phase.",
        "Identify residual risk after prevention and mitigation.",
        "Explain how planning choices can increase exposure or vulnerability.",
        "State Sendai's voluntary character before using its priorities.",
        "Diagnose the weakest priority for the case rather than reciting all four.",
        "Name all targets compactly when the directive says mention.",
        "Separate outcome reduction from means of implementation.",
        "Test whether recovery removes or recreates the original risk.",
        "Show complementarity while preserving framework boundaries.",
        "Answer only the verified demand and qualify current-status claims.",
    ]
    panels = [
        common.panel("Risk grammar", "systems-map", [
            "HAZARD -> potential damaging event or process",
            "EXPOSURE -> people and assets in harm's way",
            "VULNERABILITY -> susceptibility",
            "CAPACITY -> strengths and resources",
            "INTERACTION -> disaster risk",
        ], ["Hazard", "Exposure", "Vulnerability", "Capacity"]),
        common.panel("Hazard-to-disaster threshold", "causal-chain", [
            "HAZARDOUS EVENT + EXPOSURE + VULNERABILITY",
            "                    | moderated by capacity",
            "                    v",
            "SERIOUS DISRUPTION BEYOND COPING -> DISASTER",
        ], ["Disaster threshold", "Risk heuristic"]),
        common.panel("Risk equation firewall", "comparison-table", [
            "USE -> organise relationships and policy levers",
            "DO NOT USE -> universal arithmetic prediction",
            "REDUCE -> exposure / vulnerability",
            "BUILD -> capacity",
        ], ["Risk heuristic"]),
        common.panel("Resilience capabilities", "radial-map", [
            "RESIST + ABSORB + ACCOMMODATE",
            "ADAPT + TRANSFORM + RECOVER",
            "PRESERVE ESSENTIAL FUNCTIONS",
            "TRAP -> recovery is not automatic restoration of old risk",
        ], ["Resilience", "Recovery"]),
        common.panel("Pre-disaster distinctions", "comparison-table", [
            "PREVENTION -> avoid risk where feasible",
            "MITIGATION -> lessen adverse impact",
            "PREPAREDNESS -> readiness to anticipate and act",
            "QUESTION -> what changes before impact?",
        ], ["Prevention", "Mitigation", "Preparedness"]),
        common.panel("Response-to-recovery bridge", "process-flow", [
            "IMMEDIATE RESPONSE -> life safety and basic needs",
            "EARLY RECOVERY -> restore access and services",
            "RECONSTRUCTION -> reduce future risk",
            "BUILD BACK BETTER -> do not reproduce vulnerability",
        ], ["Response", "Recovery"]),
        common.panel("DRR operating scope", "status-ladder", [
            "PREVENT NEW RISK",
            "REDUCE EXISTING RISK",
            "MANAGE RESIDUAL RISK",
            "LINK -> risk-informed sustainable development",
        ], ["DRR scope"]),
        common.panel("Risk-creation loop", "feedback-loop", [
            "DEVELOPMENT CHOICE -> exposure / vulnerability",
            "HAZARD INTERACTION -> loss",
            "RECOVERY CHOICE -> recreate or reduce risk",
            "FEEDBACK -> future resilience",
        ], ["Risk creation", "Recovery"]),
        common.panel("Sendai architecture", "framework-map", [
            "2015-2030 | voluntary and non-binding",
            "4 PRIORITIES -> governance pathway",
            "7 TARGETS -> global monitoring frame",
            "OUTCOME -> substantial reduction of disaster risk and losses",
        ], ["Sendai status", "Sendai priorities"]),
        common.panel("Four-priority rail", "numbered-rail", [
            "1 UNDERSTAND DISASTER RISK",
            "2 STRENGTHEN RISK GOVERNANCE",
            "3 INVEST IN DRR FOR RESILIENCE",
            "4 PREPARE + BUILD BACK BETTER",
        ], ["Sendai priorities"]),
        common.panel("Seven-target matrix", "matrix", [
            "A mortality | B affected people",
            "C economic loss/GDP | D critical systems",
            "E national/local strategies | F cooperation",
            "G multi-hazard warning and risk information",
        ], ["Targets A-D", "Targets E-G"]),
        common.panel("Answer and framework boundary", "answer-spine", [
            "DEFINE -> MAP RISK COMPONENTS -> LOCATE CYCLE PHASE",
            "APPLY SENDAI PRIORITY / TARGET",
            "LINK ADAPTATION + SDG WITHOUT MERGER",
            "QUALIFY -> INPUT IS NOT OUTCOME",
        ], ["Framework linkage", "Evidence boundary"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2018", "GS-III",
            "Describe disaster-risk-reduction measures and compare the Sendai Framework with the Hyogo Framework.",
            "Verified routing ledger: Describe · 15 marks · 250 words; no official model answer is claimed.",
            [7, 8, 9, 12, 14, 15, 16, 17]),
        common.make_pyq_solution(facts, "2019", "GS-III",
            "Discuss vulnerability as a concept for defining disaster impacts and explain its types.",
            "Verified routing ledger: Discuss · 10 marks · 150 words.",
            [0, 1, 2, 3, 4, 5]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Define disaster resilience, explain how it is determined and its framework elements, and mention Sendai's global targets.",
            "Exact local official-paper demand audited in the owner: Describe · 15 marks · 250 words.",
            [4, 6, 14, 15, 16, 17, 19]),
    ]
    return common.topic(
        1, "Concepts, Risk, Resilience and Sendai",
        "01_Concepts-Risk-Resilience-and-Sendai", facts, traps,
        [
            (10, "Distinguish hazard, exposure, vulnerability, capacity, risk and disaster.", [0, 1, 2, 3, 4, 5]),
            (10, "Differentiate prevention, mitigation and preparedness in disaster management.", [7, 8, 9]),
            (15, "Explain disaster resilience and the elements that determine it.", [4, 6, 11, 13]),
            (15, "Describe the four priorities and seven global targets of the Sendai Framework.", [14, 15, 16, 17]),
            (20, "Analyse how development choices create disaster risk and how Build Back Better can interrupt that cycle.", [4, 6, 11, 12, 13, 15, 19]),
            (20, "Examine the relationship among DRR, climate adaptation and sustainable development without collapsing their distinct frameworks.", [6, 12, 13, 14, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Hazard", "Exposure", "Vulnerability", "Capacity", "Risk",
            "Resilience", "prevention", "mitigation", "preparedness",
            "response", "recovery", "Sendai Framework", "four priorities",
            "seven global targets", "Build Back Better",
        ],
        "The three conservative cards are the direct 2018, 2019 and 2024 GS-III routes preserved in the audited ledgers and owner. Directive, marks and word limit are stated only where verified.",
        pyqs, LIVE_ATTEMPTS,
        "UNDRR's adopted Sendai text is the framework anchor; WMO's EW4All page is a current Target-G implementation anchor. Neither source is used to fabricate country performance, avoided losses or universal coverage.",
        extra=[
            "00_Master-Framework.md", "README.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md",
        ],
        register_headings=(
            "RISK VOCABULARY AND DISASTER THRESHOLD",
            "MANAGEMENT-CYCLE AND SENDAI FIREWALLS",
            "RISK-CREATION AND RESILIENCE ANSWER SPINE",
            "CURRENT FRAMEWORK AND OUTCOME-EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE HAZARD EXPOSURE VULNERABILITY CAPACITY RISK AND DISASTER",
            "USE THE RISK EQUATION ONLY AS A HEURISTIC",
            "LOCATE PREVENTION MITIGATION PREPAREDNESS RESPONSE AND RECOVERY",
            "DEFINE RESILIENCE BEYOND BOUNCE BACK",
            "MAP THE FOUR SENDAI PRIORITIES AND SEVEN TARGETS",
            "LINK DRR CLIMATE ADAPTATION AND SUSTAINABLE DEVELOPMENT",
            "CONCLUDE AT THE LAST VERIFIED OUTCOME RUNG",
        ],
    )


TOPIC_01 = _build()
