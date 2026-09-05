"""Authored Economy learner-v2 data for Topic 02."""

from __future__ import annotations

import generate_economy_common as common


def panel(title: str, kind: str, lines: list[str]) -> tuple[str, str, str, list[str]]:
    return (
        title,
        kind,
        "\n".join(lines),
        [
            "upsc-ai-kit/knowledge/Economy/basic/02_Growth-Development-HDI-IHDI-and-MPI.md",
            "upsc-ai-kit/knowledge/Economy/advanced/02_Growth-Development-HDI-IHDI-and-MPI.md",
        ],
    )


FACTS = [
    ("Growth versus development", "Economic growth is a sustained quantitative increase in real output or income, whereas development adds structural change, capability expansion and better distribution."),
    ("Capability approach", "Amartya Sen's capability approach judges development by substantive freedoms and real opportunities to lead valued lives, not by income or commodity possession alone."),
    ("HDI architecture", "UNDP's HDI is the geometric mean of normalised health, education and standard-of-living indices, using life expectancy, schooling measures and GNI per capita."),
    ("IHDI inequality adjustment", "IHDI discounts each HDI dimension for inequality, equals HDI only in the absence of inequality and falls farther below HDI as unequal distribution increases."),
    ("MPI purpose", "MPI identifies overlapping household deprivations in health, education and living standards rather than classifying poverty from income alone."),
    ("Social capital", "Trust, norms and networks can improve cooperation, collective action and scheme effectiveness, making social capital a development resource beyond private income."),
    ("Growth-resource channel", "Real productivity and output growth enlarge household income, profits and the tax base, creating resources that can finance capabilities but not guaranteeing their conversion."),
    ("Composition of growth", "Labour intensity, sectoral composition, regional spread and access to productive jobs determine whether aggregate growth reaches lagging regions and vulnerable groups."),
    ("Public-service conversion", "Nutrition, health, education, housing and risk protection convert public revenue and household income into capabilities, employability and intergenerational mobility."),
    ("Institutional division", "UNDP publishes HDI and IHDI, UNDP and OPHI are associated with the global MPI, NITI Aayog publishes India's national MPI, and governments deliver capability-building services."),
    ("Kerala-Bihar comparison", "The familiar Kerala-Bihar contrast shows that per-capita output does not convert one-for-one into social outcomes because public services, history, migration, demography and state capacity matter."),
    ("National MPI targeting", "NITI Aayog's national MPI uses household evidence to identify simultaneous deficits such as nutrition, schooling, sanitation, housing and amenities for targeted policy."),
    ("Aspirational Districts lesson", "The Aspirational Districts Programme illustrates why state averages can hide district-level divergence, while dashboard or rank improvement alone does not prove structural transformation."),
    ("MGNREGA conversion role", "MGNREGA links public expenditure with wage employment and rural asset creation, supporting minimum protection without substituting for productivity growth or formal jobs."),
    ("Nutrition and schooling interventions", "ICDS and PM POSHAN show that direct nutrition and schooling support can expand capabilities, although access and attendance do not by themselves establish service quality or employability."),
    ("Kudumbashree and SHGs", "Kudumbashree and the wider self-help-group model show how organised women's networks can support savings, credit, agency and local problem-solving while remaining complements to formal capacity."),
    ("MPI incidence", "In MPI, H is the proportion of people identified as multidimensionally poor at the chosen weighted-deprivation cutoff; standard global methodology uses at least one-third of weighted indicators."),
    ("MPI intensity", "In MPI, A is the average share of weighted indicators in which multidimensionally poor people are deprived, so MPI equals H multiplied by A and incidence can move differently from intensity."),
    ("Income-poverty contrast", "An income or consumption poverty line records whether a monetary threshold is crossed but cannot show the overlap or composition of nutrition, schooling, sanitation and housing deprivation."),
    ("Composite and benchmark caution", "HDI, IHDI and MPI depend on dimensions, weights and survey timing, while the owner's USD 3-a-day extreme-poverty figure uses 2021 PPP prices and is not India's official domestic poverty line or directly comparable with older lines."),
]

TRAPS = [
    "Do not infer development from nominal or aggregate GDP growth alone.",
    "Do not say HDI directly measures political freedom; its formal dimensions are health, education and income.",
    "Do not treat IHDI as a separate welfare basket; it inequality-adjusts the HDI dimensions.",
    "Do not reduce MPI to an income poverty-line headcount.",
    "Do not merge incidence H with intensity A; they answer how many and how deprived.",
    "Do not compare poverty lines across PPP revisions without stating the price basis.",
    "Do not treat a dashboard ranking gain as proof of durable transformation.",
    "Do not assume welfare access guarantees service quality or productive employment.",
    "Do not copy one state's development path mechanically across different histories and capacities.",
    "Do not treat social capital as a substitute for infrastructure, markets or public finance.",
    "Do not use an international poverty benchmark as India's official domestic poverty line.",
    "Do not let average HDI conceal caste, gender, tribal, regional or district inequality.",
]

SESSION_TITLES = [
    "Growth, development and substantive freedom",
    "HDI dimensions and geometric aggregation",
    "How IHDI exposes inequality",
    "What multidimensional poverty measures",
    "Social capital as a development resource",
    "Growth resources, composition and jobs",
    "Public services as conversion channels",
    "Who produces each development index",
    "State variation and the Kerala-Bihar lesson",
    "National MPI and household targeting",
    "District targeting and MGNREGA protection",
    "Nutrition and schooling capability channels",
    "Women's networks and collective agency",
    "MPI incidence and intensity",
    "Income poverty, composite limits and PPP vintage",
]

ANSWER_ROUTES = [
    "Treat growth as the resource base and institutions, jobs and public services as the conversion mechanism.",
    "Compare average achievement with inequality and overlapping deprivation before judging inclusion.",
    "End with disaggregated outcomes, service quality and employment-intensive productivity growth.",
]

PANELS = [
    panel("Growth is the input, not the verdict", "causal-chain", ["REAL OUTPUT GROWTH", "-> income + profits + fiscal capacity", "-> jobs + public services + household investment", "DEVELOPMENT ONLY IF capabilities broaden"]),
    panel("Capability conversion", "conversion-funnel", ["RESOURCES", "-> health + education + nutrition", "-> substantive freedoms", "LIMIT -> income can rise without conversion"]),
    panel("HDI three-dimension frame", "three-axis-map", ["HEALTH -> life expectancy", "EDUCATION -> expected + mean years of schooling", "LIVING STANDARD -> GNI per capita", "AGGREGATION -> geometric mean"]),
    panel("HDI-to-IHDI discount", "inequality-ladder", ["HDI -> average achievement", "INEQUALITY WITHIN EACH DIMENSION", "-> achievement discounted", "ZERO INEQUALITY -> IHDI equals HDI"]),
    panel("MPI household lens", "deprivation-grid", ["HEALTH | EDUCATION | LIVING STANDARDS", "HOUSEHOLD -> overlapping deficits", "NOT AN INCOME-ONLY CLASSIFICATION", "USE -> composition and targeting"]),
    panel("H times A formula", "equation-band", ["H -> incidence: how many are poor", "A -> intensity: how deprived the poor are", "MPI = H x A", "TRAP -> H and A can move differently"]),
    panel("Income line versus MPI", "comparison-matrix", ["INCOME LINE -> monetary threshold", "MPI -> weighted deprivation overlap", "INCOME -> transfer adequacy", "MPI -> sectoral composition of deprivation"]),
    panel("Institutions map", "institution-map", ["UNDP -> HDI and IHDI", "UNDP + OPHI -> global MPI", "NITI AAYOG -> national MPI", "GOVERNMENTS -> service delivery"]),
    panel("Below-state diagnosis", "scale-ladder", ["NATIONAL AVERAGE", "-> STATE DIVERGENCE", "-> DISTRICT DIVERGENCE", "RULE -> ranking change is not transformation"]),
    panel("Protection versus transformation", "policy-fork", ["MGNREGA -> wage floor + rural assets", "ICDS / PM POSHAN -> nutrition + schooling", "SHGs -> savings + agency + networks", "LIMIT -> productivity and decent jobs remain necessary"]),
    panel("Composite-index limits", "limit-wheel", ["AVERAGE -> can hide distribution", "WEIGHTS -> shape results", "SURVEY TIMING -> misses sudden shocks", "QUALITY -> may differ from access"]),
    panel("Inclusive-growth answer spine", "answer-spine", ["DEFINE growth and development", "TRACE jobs + services + capabilities", "COMPARE HDI / IHDI / MPI", "QUALIFY with inequality, quality and ecology"]),
]

PYQ_NOTE = (
    "The audited ledgers route 2020 GS-II on incidence and intensity of poverty, "
    "2024 GS-III on social-service expenditure and inclusive growth, and 2025 "
    "GS-III on HDI versus IHDI here. Objective routes on GNP per capita, Ease "
    "of Doing Business, social capital and 2026 MPI methodology remain "
    "answer-letter free."
)

PYQ_SOLUTIONS = [
    common.make_pyq_solution(FACTS, "2020", "GS-II", "Analyse incidence and intensity of poverty against income-based measurement.", "Verified routed Mains demand; original model solution.", [16, 17, 18]),
    common.make_pyq_solution(FACTS, "2024", "GS-III", "Examine whether social-service expenditure has supported inclusive growth.", "Verified routed Mains demand; original model solution.", [6, 8, 13, 14]),
    common.make_pyq_solution(FACTS, "2025", "GS-III", "Distinguish HDI and IHDI and explain why IHDI better indicates inclusive growth.", "Verified routed Mains demand; original model solution.", [2, 3, 19]),
]

TOPIC_02 = common.topic(
    2,
    "Growth, Development, HDI, IHDI and MPI",
    "02_Growth-Development-HDI-IHDI-and-MPI",
    "02_Growth-Development-HDI-IHDI-and-MPI_Learner-V2-Complete-Topic-Package.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish economic growth from economic development.", [0, 1, 6]),
        (10, "Why does IHDI reveal dimensions of inclusive growth that HDI misses?", [2, 3]),
        (15, "Explain the MPI incidence-intensity framework and its advantage over an income headcount.", [4, 16, 17, 18]),
        (15, "Growth expands resources, but institutions determine human development. Discuss.", [6, 7, 8, 9]),
        (20, "Assess India's growth-to-capability conversion using jobs, public services and local variation.", [7, 10, 12, 13, 14]),
        (20, "Critically evaluate composite development indices for inclusive-growth policy.", [2, 3, 4, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    ["capability approach", "HDI", "IHDI", "MPI", "H", "intensity", "OPHI", "NITI Aayog"],
    PYQ_NOTE,
    PYQ_SOLUTIONS,
    [
        "https://hdr.undp.org/data-center/human-development-index#/indicies/HDI — retrieved 2026-09-03; the official UNDP page substantively states that HDI uses health, education and standard-of-living dimensions aggregated by a geometric mean and also states that HDI does not capture inequality, poverty, security or empowerment.",
    ],
    "The UNDP HDI page was substantively retrievable on 2026-09-03 and is used only for its HDI dimensions, geometric-mean construction and stated limits. No live India rank, score, IHDI loss, MPI headcount or poverty estimate was taken from it.",
)
