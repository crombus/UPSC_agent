"""Authored Geography learner-v2 data for Part B Topics 26, 27 and 29."""

from __future__ import annotations

import generate_geography_common as common


def plan(
    title: str, indexes: list[int], caution: str, exam_use: str
) -> tuple[str, list[int], str, str]:
    return title, indexes, caution, exam_use


def panel(
    title: str,
    kind: str,
    lines: list[str],
    references: list[str],
) -> tuple[str, str, str, list[str]]:
    return title, kind, "\n".join(lines), references


TOPIC_26 = common.topic(
    26,
    "World Population and Demographic Transition",
    "26_World-Population-and-Demographic-Transition.md",
    "26_World-Population-and-Demographic-Transition.md",
    "26_World-Population-and-Demographic-Transition_Complete-Topic-Package.md",
    [
        (
            "Population geography baseline",
            "Population distribution, growth and composition are core human-geography variables because they shape pressure on land, jobs, housing and services.",
        ),
        (
            "Census snapshot rule",
            "A census gives a time-specific demographic snapshot, while growth between two dates reflects births, deaths and migration together.",
        ),
        (
            "Vital-rate toolkit",
            "Growth rate, crude birth rate, crude death rate, total fertility rate, infant mortality rate, life expectancy and sex ratio are the standard population indicators.",
        ),
        (
            "Mortality-first transition logic",
            "In demographic transition the death rate usually falls before the birth rate, so the gap between them produces the growth spurt.",
        ),
        (
            "Stage 1 and Stage 2 profile",
            "Stage 1 has high birth and high death rates with fluctuating growth, while Stage 2 keeps birth rates high but mortality falls rapidly.",
        ),
        (
            "Stage 3 to Stage 5 profile",
            "Stage 3 brings fertility decline, Stage 4 has low birth and death rates with stable growth, and Stage 5 in some advanced societies means below-replacement fertility and ageing.",
        ),
        (
            "Population pyramid types",
            "Expansive, stationary and constrictive population pyramids are the quick visual forms for youthful, slower-growth and ageing populations respectively.",
        ),
        (
            "Dependency and dividend condition",
            "A large working-age share reduces dependency pressure, but a demographic dividend appears only when education, health, skills and jobs convert that structure into productivity.",
        ),
        (
            "Over-under-optimum population",
            "Under-population, over-population and optimum population describe the relationship among people, resources, technology and living standards.",
        ),
        (
            "Optimum population shifts",
            "Optimum population is not a permanent number because technology, trade and institutions can change the carrying capacity of the same resource base.",
        ),
        (
            "India 1901-1921 stagnation",
            "Khullar treats 1901-1921 as a phase of high birth and high death rates, epidemics, famine stress and demographic stagnation.",
        ),
        (
            "India 1921 turning point",
            "The years 1921-1951 are the steady-growth phase, and 1921 is widely treated as India's demographic turning point.",
        ),
        (
            "India 1951-1981 explosion",
            "The period 1951-1981 saw sharp mortality decline while fertility remained high, producing the population-explosion phase.",
        ),
        (
            "India 1981-2011 slowdown",
            "From 1981 to 2011 fertility decline deepened and growth slowed, showing a later transition phase rather than stagnation.",
        ),
        (
            "Census 2011 total",
            "Census 2011 recorded India's population at 1.21 billion, and no later projection should be called a census count.",
        ),
        (
            "Census 2011 social indicators",
            "Census 2011 reported a sex ratio of 943 females per 1,000 males and a literacy rate of 74.04 percent.",
        ),
        (
            "SRS-NFHS fertility anchor",
            "SRS 2022 and NFHS-5 both place India's total fertility rate at 2.0, showing replacement-level fertility nationally in dated survey evidence.",
        ),
        (
            "UN 2024 projection boundary",
            "UN World Population Prospects 2024 places India's mid-2024 population at about 1.45 billion, but this remains a projection rather than a census count.",
        ),
        (
            "Kerala-EAG contrast",
            "Kerala had reached a high stage of transition comparable to advanced countries by the 2011 period, while several populous EAG states retained more youthful structures for longer.",
        ),
        (
            "Ageing with momentum",
            "India simultaneously contains ageing pockets, replacement-level states and youth-bulge states, so population momentum and regional divergence continue together.",
        ),
    ],
    [
        "Do not treat population growth as the same thing as birth rate.",
        "Do not say the birth and death rates fall together at the start of transition.",
        "Do not call a UN projection or survey estimate a census count.",
        "Do not read replacement-level fertility as immediate zero population growth.",
        "Do not treat optimum population as a single fixed number for all time.",
        "Do not confuse expansive, stationary and constrictive population pyramids.",
        "Do not assume a working-age bulge automatically creates a dividend.",
        "Do not flatten India into one uniform demographic stage.",
        "Do not quote post-2011 totals without naming Census, SRS, NFHS or UN properly.",
        "Do not treat Kerala's transition profile as identical to all northern states.",
        "Do not ignore migration while interpreting sex ratio and age structure.",
        "Do not invent a direct PYQ when the routing stays cross-owner.",
    ],
    [
        (
            10,
            "Explain the demographic transition model and identify why the growth spurt appears in the middle stages.",
            "The demographic transition model is driven by mortality decline preceding fertility decline; the temporary gap between the two rates creates rapid population growth before stability returns.",
            [2, 3, 4, 5],
        ),
        (
            10,
            "Show how population pyramids and dependency ratio together help in reading a population structure.",
            "Population pyramids reveal age-sex structure at a glance, while dependency ratio shows whether a youthful or ageing structure is likely to create burden or dividend conditions.",
            [6, 7],
        ),
        (
            15,
            "Discuss the idea of optimum population with suitable qualifications.",
            "Optimum population is a relational concept balancing people, resources, technology and living standards; it shifts when productive capacity, trade links and institutions change.",
            [8, 9],
        ),
        (
            15,
            "Trace India's long demographic transition from 1901 to 2011.",
            "India's demographic story moves from stagnation to steady growth, to population explosion, and then to slowdown, showing mortality decline first and fertility decline later.",
            [10, 11, 12, 13],
        ),
        (
            20,
            "Is India in a demographic-dividend phase or a demographic-divergence phase? Analyse.",
            "India has a dividend window at the national scale, but regional divergence, population momentum and unequal labour absorption mean the same age structure can produce both opportunity and burden.",
            [7, 16, 18, 19],
        ),
        (
            20,
            "Why must population answers on India separate Census 2011 data from SRS, NFHS and UN updates?",
            "Data discipline is essential because Census, survey-based fertility estimates and UN projections answer different questions; mixing them casually turns demographic evidence into factual error.",
            [14, 15, 16, 17],
        ),
    ],
    [
        plan("Population geography baseline and census snapshot", [0, 1, 2], "Growth depends on births, deaths and migration together.", "Open with definition plus the indicator toolkit before citing any number."),
        plan("Mortality-first transition logic", [3, 4], "Stage 2 begins with mortality decline, not fertility decline.", "Explain why the middle-stage gap produces rapid growth."),
        plan("Late transition, ageing and below replacement", [5], "Below-replacement fertility is not the same as immediate decline.", "Contrast Stage 4 stability with Stage 5 ageing pressures."),
        plan("Population pyramid reading", [6], "Do not confuse youthful and ageing pyramid shapes.", "Use expansive, stationary and constrictive pyramids as a fast visual answer."),
        plan("Dependency ratio and dividend conditions", [7], "A working-age bulge is only potential until jobs and skills exist.", "Move from age structure to productivity, not to slogans about youth."),
        plan("Population-resource relationship", [8, 9], "Optimum population shifts with technology and institutions.", "Use over, under and optimum population as relational, not moral, categories."),
        plan("India's stagnation phase 1901-1921", [10], "Do not call this a steady-growth phase.", "Link high mortality, epidemics and unstable growth clearly."),
        plan("India's turning point 1921-1951", [11], "1921 matters because the demographic trend changes, not because fertility collapses.", "Use 1921 as the turning point and steady-growth bridge."),
        plan("Population explosion 1951-1981", [12], "Explosion refers to rapid growth, not to one sudden event.", "Show mortality decline outrunning fertility decline."),
        plan("Slowdown after 1981", [13], "Slowing growth does not mean the population stops growing.", "Explain fertility decline and momentum together."),
        plan("Census 2011 baseline", [14, 15], "Do not merge Census totals with later projections.", "Quote population, sex ratio and literacy only with the census label."),
        plan("SRS and NFHS fertility anchor", [16], "Survey fertility evidence is dated and source-specific.", "Use TFR 2.0 as a named SRS-NFHS fertility marker."),
        plan("UN projection boundary", [17], "A UN estimate must stay labelled as a projection.", "Use the 2024 estimate only to explain population momentum."),
        plan("Kerala-EAG contrast", [18], "India is not one uniform demographic stage.", "Contrast early-transition and lagging-transition regions carefully."),
        plan("Ageing, youth bulge and momentum together", [19], "Do not force India into only a dividend or only an ageing frame.", "Conclude with coexistence: momentum, ageing pockets and youth-bulge states."),
    ],
    [
        panel("Population balance equation", "process-flow", [
            "POPULATION AT T2 = population at T1 + births - deaths +/- migration",
            "CENSUS -> time-specific snapshot, not a continuous live counter",
            "GROWTH RATE -> outcome of all three components together",
            "TRAP -> birth rate alone cannot explain total population change",
        ], ["Census snapshot rule", "Vital-rate toolkit"]),
        panel("Demographic transition spine", "process-flow", [
            "STAGE 1 -> high birth, high death, unstable growth",
            "STAGE 2 -> death rate falls first, birth stays high",
            "STAGE 3 -> fertility falls, growth slows",
            "STAGE 4/5 -> low rates, then ageing or decline in some societies",
        ], ["Mortality-first transition logic", "Stage 1 and Stage 2 profile", "Stage 3 to Stage 5 profile"]),
        panel("Population pyramid reading", "comparison-table", [
            "EXPANSIVE -> broad base, youthful age structure, high fertility",
            "STATIONARY -> moderated base and fuller middle, slower growth",
            "CONSTRICTIVE -> narrow base and wider upper ages, ageing trend",
            "READING RULE -> shape, dependency and labour supply move together",
        ], ["Population pyramid types", "Dependency and dividend condition"]),
        panel("Dependency to dividend fork", "decision-tree", [
            "WORKING-AGE SHARE RISES -> dependency ratio can fall",
            "IF health + education + skills + jobs improve -> dividend window",
            "IF labour absorption fails -> unemployment and informality rise",
            "VERDICT -> demography gives potential, institutions decide the outcome",
        ], ["Dependency and dividend condition", "Ageing with momentum"]),
        panel("Population-resource triangle", "comparison-table", [
            "UNDER-POPULATION -> too few people to use resources fully",
            "OVER-POPULATION -> pressure lowers living standards and employment quality",
            "OPTIMUM POPULATION -> relative balance of people, resources and technology",
            "SHIFT RULE -> technology, trade and institutions can move the optimum",
        ], ["Over-under-optimum population", "Optimum population shifts"]),
        panel("India demographic timeline", "timeline-strip", [
            "1901-1921 -> stagnation under high birth and high death rates",
            "1921-1951 -> steady growth after the turning point",
            "1951-1981 -> population explosion as mortality falls sharply",
            "1981-2011 -> slowing growth as fertility decline deepens",
        ], ["India 1901-1921 stagnation", "India 1921 turning point", "India 1951-1981 explosion", "India 1981-2011 slowdown"]),
        panel("India data-source firewall", "institutional-ladder", [
            "CENSUS 2011 -> 1.21 billion total; sex ratio 943; literacy 74.04%",
            "SRS 2022 / NFHS-5 -> TFR 2.0; fertility anchor, not census count",
            "UN WPP 2024 -> mid-2024 estimate about 1.45 billion projection",
            "RULE -> keep instrument, date and status label attached to every figure",
        ], ["Census 2011 total", "Census 2011 social indicators", "SRS-NFHS fertility anchor", "UN 2024 projection boundary"]),
        panel("Kerala-EAG contrast rail", "comparison-table", [
            "KERALA -> early fertility decline, higher literacy, later-ageing pressures",
            "EAG STATES -> more youthful structures and slower transition timing",
            "NATIONAL AVERAGE -> hides staggered state-level transition stages",
            "EXAM USE -> India contains early, middle and late transition spaces together",
        ], ["Kerala-EAG contrast", "Ageing with momentum"]),
        panel("Ageing with population momentum", "causal-system", [
            "REPLACEMENT-LEVEL TFR -> does not stop growth immediately",
            "YOUNG COHORT BULGE -> population momentum keeps totals rising",
            "EARLY-TRANSITION STATES -> old-age burden appears sooner",
            "LATE-TRANSITION STATES -> youth bulge and migration pressure persist longer",
        ], ["SRS-NFHS fertility anchor", "Ageing with momentum"]),
        panel("Sex ratio interpretation rule", "process-flow", [
            "SEX RATIO -> shaped by births, mortality and migration together",
            "LABOUR MIGRATION -> can skew all-age ratios without changing births",
            "CHILD SEX RATIO -> isolates a different part of the demographic problem",
            "SAFE ANSWER -> define the measure before comparing regions",
        ], ["Vital-rate toolkit", "Census 2011 social indicators"]),
        panel("World divergence under one model", "comparison-table", [
            "SUB-SAHARAN AFRICA -> youthful, high-growth structures remain common",
            "EUROPE / EAST ASIA -> low fertility, ageing and labour shortage concerns",
            "INDIA -> dividend window plus internal divergence at the same time",
            "LESSON -> one transition model yields very different policy problems",
        ], ["Stage 3 to Stage 5 profile", "Ageing with momentum"]),
        panel("Population answer spine", "answer-spine", [
            "DEFINE -> indicator, census or survey, and what exactly is being measured",
            "ORDER -> transition stage, pyramid shape and dependency condition",
            "LOCATE -> world contrast plus Kerala-EAG or other state divergence",
            "QUALIFY -> projection versus census, dividend versus momentum, no fabricated PYQ",
        ], ["Population geography baseline", "Kerala-EAG contrast", "UN 2024 projection boundary"]),
    ],
    [
        "demographic transition",
        "population pyramid",
        "dependency ratio",
        "optimum population",
        "population momentum",
        "demographic dividend",
        "Census 2011",
        "SRS 2022",
        "Kerala",
        "EAG",
    ],
    (
        "The audited routing ledgers consulted for this rebuild do not assign a direct solved PYQ to Geography Topic 26. Population questions are routed mainly through Indian Society, Economy and cross-owner demographic files, so this package keeps the demographic-geography framework transparent and does not fabricate a direct PYQ answer card."
    ),
    [],
    [
        "https://population.un.org/wpp/",
        "https://censusindia.gov.in/",
        "https://mospi.gov.in/",
    ],
    (
        "UN World Population Prospects 2024, Census 2011 and SRS 2022 are used only as dated anchors. No projection is presented as a census total, and no post-2011 demographic claim is left without its instrument and date label."
    ),
)

TOPIC_27 = common.topic(
    27,
    "Migration Theories and Patterns (India)",
    "27_Migration-Theories-and-Patterns-India.md",
    "27_Migration-Theories-and-Patterns-India.md",
    "27_Migration-Theories-and-Patterns-India_Complete-Topic-Package.md",
    [
        (
            "Migration definition",
            "Migration is a change in usual residence across a meaningful geographic or administrative boundary, and datasets may track it by place of birth or last usual residence.",
        ),
        (
            "Push-pull logic",
            "Migration is commonly explained through push factors at the origin and pull factors at the destination.",
        ),
        (
            "Ravenstein laws",
            "Ravenstein's laws emphasise short-distance movement, step migration and the creation of counter-streams.",
        ),
        (
            "Lee framework",
            "Lee's framework explains migration through origin factors, destination factors, intervening obstacles and personal selectivity.",
        ),
        (
            "Distance-decay principle",
            "Migration volume usually falls with distance unless exceptional opportunities or networks offset distance costs.",
        ),
        (
            "Step migration chain",
            "Step migration often proceeds village to small town to city to metropolis rather than by one direct leap.",
        ),
        (
            "Circular and seasonal migration",
            "Circular or seasonal migration repeats movement without final permanent settlement and is central to labour geography.",
        ),
        (
            "Stream classification",
            "Migration can be classified as internal or international and, within internal migration, as rural-rural, rural-urban, urban-urban and urban-rural streams.",
        ),
        (
            "Rural-rural dominance",
            "Rural-rural movement has historically been the largest internal stream in India, especially because marriage migration is large.",
        ),
        (
            "Rural-urban urbanisation link",
            "Rural-urban migration remains the classic labour stream that fuels urbanisation, construction and informal work.",
        ),
        (
            "Source-destination effects",
            "Migration changes source and destination regions together through remittances, labour redistribution, sex-structure change, congestion and slum pressure.",
        ),
        (
            "India's differentiated mobility",
            "Khullar describes India as historically less mobile than many Western societies but internally very differentiated by marriage, labour and interstate variation.",
        ),
        (
            "MoSPI all-India migration rate",
            "MoSPI's Migration in India 2020-21 gives an all-India migration rate of 28.9 percent.",
        ),
        (
            "Rural and urban migration rates",
            "The same MoSPI release gives a rural migration rate of 26.5 percent and an urban migration rate of 34.9 percent.",
        ),
        (
            "Intrastate versus interstate",
            "In MoSPI 2020-21, 87.5 percent of migrants were intrastate and 12.5 percent were interstate.",
        ),
        (
            "Marriage migration dominance",
            "Female migrants moving due to marriage formed 86.8 percent of female migrants in the MoSPI 2020-21 snapshot.",
        ),
        (
            "Net gainers and senders",
            "Khullar's spatial pattern shows Maharashtra, Gujarat, Delhi, Haryana and Punjab as classic gainers, while Bihar, Uttar Pradesh, Odisha and east-central belts are major sending regions.",
        ),
        (
            "Corridor logic",
            "India's broad direction of labour mobility runs from lower-income agrarian regions towards industrial, construction and service corridors, making migration both development-seeking and distress-driven.",
        ),
        (
            "Remittance and labour restructuring",
            "Remittances support consumption, housing, education and debt repayment in source regions, but they do not automatically create local productive employment.",
        ),
        (
            "Circular undercount and urban stress",
            "Circular migration is undercount-prone in usual-residence measures, while destination cities face rental insecurity, service pressure and informal settlement growth.",
        ),
    ],
    [
        "Do not treat migration as only long-distance movement.",
        "Do not use Ravenstein as if it were a law of universal certainty.",
        "Do not omit intervening obstacles from Lee's framework.",
        "Do not call all migration permanent settlement.",
        "Do not reduce migration streams to rural-urban alone.",
        "Do not present interstate migration as the dominant Indian stream.",
        "Do not forget that marriage migration dominates recorded female migration.",
        "Do not read raw migration totals as purely economic movement.",
        "Do not ignore remittances when analysing source regions.",
        "Do not treat circular migration as well captured by all datasets.",
        "Do not present destination-city congestion without the labour-demand side.",
        "Do not invent a direct indentured-labour PYQ ownership for this topic.",
    ],
    [
        (
            10,
            "Explain migration using push factors, pull factors and intervening obstacles.",
            "Migration decisions arise from origin distress, destination attraction, intervening obstacles and personal selectivity; no one factor explains every stream.",
            [0, 1, 3],
        ),
        (
            10,
            "Why is step migration important in understanding urbanisation?",
            "Step migration shows that urbanisation often grows through a hierarchy of places, not by one jump from village to metropolis.",
            [2, 4, 5],
        ),
        (
            15,
            "Discuss why India's migration is not one stream but many.",
            "India's migration geography must separate marriage-led rural-rural movement, labour-led rural-urban mobility, urban-urban professional movement and circular migration.",
            [7, 8, 9, 15],
        ),
        (
            15,
            "Assess the effects of migration on source and destination regions in India.",
            "Migration redistributes labour and income: remittances support origin households, but cities absorb labour with congestion, informality and service pressure.",
            [10, 18, 19],
        ),
        (
            20,
            "Use the latest official migration snapshot to explain India's internal mobility pattern.",
            "MoSPI 2020-21 shows that India's migration remains largely intrastate, marriage-heavy in recorded female movement and more urban in incidence, which complicates simplistic labour-migration readings.",
            [12, 13, 14, 15],
        ),
        (
            20,
            "Why do large cities attract more migrants than smaller towns? Analyse with Indian examples.",
            "Large cities concentrate diversified opportunities, networks and labour demand, so they attract migrants despite risk, while smaller centres intercept only part of the flow.",
            [5, 9, 16, 17, 19],
        ),
    ],
    [
        plan("Migration definition and data rule", [0], "Definition by usual residence matters before any analysis begins.", "Open with the residence concept before using census or survey migration numbers."),
        plan("Push and pull factors", [1], "Push and pull operate together, not in isolation.", "Use distress and opportunity in one causal frame."),
        plan("Ravenstein and short-distance logic", [2, 4], "Ravenstein is a heuristic, not an iron law.", "Explain distance-decay, short moves and counter-streams together."),
        plan("Lee framework and selectivity", [3], "Do not forget intervening obstacles and personal selectivity.", "Convert a migration answer into a diagram with origin, destination and obstacles."),
        plan("Step migration chain", [5], "Urbanisation often builds through stages, not one leap.", "Use village-town-city-metropolis as the classic sequence."),
        plan("Circular and seasonal migration", [6], "Circular migration is mobility without final permanent settlement.", "Use it to explain precarity, construction labour and welfare-portability issues."),
        plan("Migration stream classification", [7], "Separate administrative distance from rural-urban character.", "List rural-rural, rural-urban, urban-urban and urban-rural cleanly."),
        plan("Rural-rural and marriage migration", [8, 15], "Recorded migration totals are not identical to labour migration totals.", "Explain why marriage keeps rural-rural migration large in India."),
        plan("Rural-urban and urbanisation", [9], "Do not let marriage migration erase labour migration.", "Show why rural-urban flow remains the urban-growth stream."),
        plan("Source and destination effects", [10], "One-sided answers on cities or villages alone stay incomplete.", "Balance remittances, labour gains, congestion and slum pressure together."),
        plan("India's differentiated mobility", [11], "India is less mobile than some Western societies but highly varied internally.", "Use this as the transition sentence from theory to India."),
        plan("MoSPI 2020-21 headline figures", [12, 13], "Survey figures need the source and year label.", "Quote all-India, rural and urban migration rates together."),
        plan("Intrastate versus interstate", [14], "Interstate migration is not the dominant share in India.", "Use intrastate majority as the safest prelims firewall."),
        plan("Net gainers and sending regions", [16, 17], "Do not describe migration as random movement across the map.", "Map agrarian sending regions against industrial and service corridors."),
        plan("Remittances, undercount and urban stress", [18, 19], "Migration supports households but also exposes data and service-delivery gaps.", "Conclude with remittances, undercount and welfare-portability pressure."),
    ],
    [
        panel("Migration concept firewall", "comparison-table", [
            "MIGRATION -> change in usual residence across a meaningful boundary",
            "IMMIGRATION -> movement into a country or receiving region",
            "EMIGRATION -> movement out of a country or sending region",
            "DATA RULE -> place of birth and last usual residence answer different questions",
        ], ["Migration definition"]),
        panel("Push-pull-obstacle model", "decision-tree", [
            "ORIGIN PUSH -> job loss, conflict, debt, disaster, social pressure",
            "DESTINATION PULL -> wages, safety, education, amenities, networks",
            "INTERVENING OBSTACLES -> distance, cost, borders, information gaps",
            "SELECTIVITY -> age, gender, class and skills shape who actually moves",
        ], ["Push-pull logic", "Lee framework"]),
        panel("Ravenstein law strip", "process-flow", [
            "MOST MOVES -> short distance rather than very long distance",
            "STEP MIGRATION -> village to town to city to metropolis",
            "COUNTER-STREAM -> each major flow generates some reverse movement",
            "LIMIT -> use as an analytical guide, not as an absolute rule",
        ], ["Ravenstein laws", "Step migration chain"]),
        panel("Distance-decay and step migration", "causal-system", [
            "DISTANCE RISES -> cost, uncertainty and social risk rise",
            "OPPORTUNITY NODES -> nearer towns intercept part of the flow",
            "NETWORKS -> reduce cost and keep corridors alive",
            "RESULT -> many migrants move in stages rather than one leap",
        ], ["Distance-decay principle", "Step migration chain"]),
        panel("Migration stream matrix", "comparison-table", [
            "RURAL-RURAL -> marriage, local farm labour, nearby relocation",
            "RURAL-URBAN -> labour, services, education, construction",
            "URBAN-URBAN -> professional, business and higher-education mobility",
            "URBAN-RURAL -> return migration, retirement or peri-urban spillover",
        ], ["Stream classification", "Rural-rural dominance", "Rural-urban urbanisation link"]),
        panel("Source-destination balance sheet", "comparison-table", [
            "SOURCE -> reduced pressure, remittances, but loss of young workers",
            "DESTINATION -> labour gain, market expansion, but service pressure",
            "AGE-SEX EFFECT -> selective migration alters both ends differently",
            "VERDICT -> migration redistributes both opportunity and vulnerability",
        ], ["Source-destination effects", "Remittance and labour restructuring"]),
        panel("India official snapshot", "comparison-table", [
            "ALL-INDIA RATE -> 28.9% in MoSPI Migration in India 2020-21",
            "RURAL RATE -> 26.5% | URBAN RATE -> 34.9%",
            "INTRASTATE -> 87.5% | INTERSTATE -> 12.5%",
            "RULE -> label the source-year before using any percentage",
        ], ["MoSPI all-India migration rate", "Rural and urban migration rates", "Intrastate versus interstate"]),
        panel("Marriage migration dominance", "comparison-table", [
            "FEMALE MIGRANTS DUE TO MARRIAGE -> 86.8% in MoSPI 2020-21",
            "ANALYTICAL RESULT -> raw migration totals are not equal to labour migration",
            "RURAL-RURAL STREAM -> remains large because marriage mobility is large",
            "EXAM USE -> separate social migration from labour migration explicitly",
        ], ["Marriage migration dominance", "Rural-rural dominance"]),
        panel("India corridor map", "spatial-map", [
            "SENDING BELTS -> Bihar, Uttar Pradesh, Odisha and east-central regions",
            "GAINER ZONES -> Maharashtra, Gujarat, Delhi, Haryana and Punjab",
            "CURRENT LOGIC -> labour moves toward industrial, farm and service corridors",
            "QUALIFIER -> the same corridor may mix opportunity and distress migration",
        ], ["Net gainers and senders", "Corridor logic"]),
        panel("Circular migration and undercount", "hazard-flow", [
            "SEASONAL MOVEMENT -> brick kilns, harvesting, construction, informal work",
            "USUAL-RESIDENCE DATA -> can miss repeated short-duration mobility",
            "POLICY EFFECT -> portability of welfare becomes a major issue",
            "CITY EFFECT -> rental insecurity and service pressure stay concentrated",
        ], ["Circular and seasonal migration", "Circular undercount and urban stress"]),
        panel("Large-city attraction logic", "process-flow", [
            "DIVERSE JOB SET -> big cities offer multiple labour-market entry points",
            "NETWORKS -> earlier migrants lower cost and risk for later migrants",
            "TRANSPORT + SERVICES -> large nodes compress search costs",
            "COUNTERPOINT -> some nearer towns intercept flows as opportunities expand",
        ], ["Rural-urban urbanisation link", "Corridor logic", "Circular undercount and urban stress"]),
        panel("Migration answer spine", "answer-spine", [
            "DEFINE -> residence rule, stream type and whether migration is internal or international",
            "EXPLAIN -> push, pull, obstacles, distance-decay and step migration",
            "MAP -> marriage-heavy rural-rural and labour-heavy corridor movements in India",
            "QUALIFY -> intrastate dominance, remittances, undercount and verified PYQ routing",
        ], ["Migration definition", "Intrastate versus interstate", "Remittance and labour restructuring"]),
    ],
    [
        "Ravenstein",
        "Lee",
        "distance-decay",
        "step migration",
        "circular migration",
        "intrastate",
        "interstate",
        "marriage migration",
        "MoSPI",
        "remittances",
    ],
    (
        "Verified routing for this rebuild comes from the owner files: the 2024 GS-I demand on why large cities attract more migrants than smaller towns is supported directly inside the Basic owner, while the 2018 indentured-labour demand remains cross-cutting and is not falsely recast as a direct solved PYQ here."
    ),
    [
        (
            "2024",
            "GS-I",
            "Why do large cities attract more migrants than smaller towns?",
            "Verified routed demand from the Basic owner and the 2024-2025 PYQ integration block.",
            "Large cities attract more migrants because they concentrate diverse job opportunities, transport connections, services and migrant networks, so expected chances of finding some work are higher than in smaller towns. Smaller towns do intercept part of the flow, but big metropolitan nodes still dominate because they combine scale, labour demand and social support networks. The safe qualification is that migration reflects both opportunity and distress, and the attraction of big cities ultimately mirrors the spatial concentration of development.",
        ),
    ],
    [
        "https://mospi.gov.in/",
        "https://censusindia.gov.in/",
    ],
    (
        "MoSPI Migration in India 2020-21 remains the latest official all-India survey-style anchor at this cutoff. Census 2027 is only a scheduled baseline refresh, so no new migration result is invented or implied here."
    ),
)

TOPIC_29 = common.topic(
    29,
    "Regional Development and Five Year Plans",
    "29_Regional-Development-and-Five-Year-Plans.md",
    "29_Regional-Development-and-Five-Year-Plans.md",
    "29_Regional-Development-and-Five-Year-Plans_Complete-Topic-Package.md",
    [
        (
            "Regional development meaning",
            "Regional development treats planning as the deliberate improvement of production, welfare, infrastructure and social capability in a defined territorial unit.",
        ),
        (
            "Regional planning unit",
            "Regional planning applies development logic to a specific region rather than to the country as a whole.",
        ),
        (
            "Uneven development drivers",
            "Resource endowment, transport access, market size, state policy, technology and historical advantage all contribute to uneven regional development.",
        ),
        (
            "Perroux growth pole idea",
            "Perroux's growth-pole idea says development begins in propulsive nodes or industries and then diffuses outward through linkages.",
        ),
        (
            "Friedmann core-periphery logic",
            "Core-periphery logic explains how a strong core dominates and organises a weaker periphery.",
        ),
        (
            "Myrdal spread and backwash",
            "Myrdal's spread and backwash effects show that growth can either diffuse benefits outward or drain labour, capital and talent from surrounding regions.",
        ),
        (
            "Balanced-unbalanced growth debate",
            "The balanced-versus-unbalanced growth debate asks whether development should be spread widely or strategically concentrated in selected nodes.",
        ),
        (
            "Planning region criteria",
            "A planning region should combine functional unity, administrative manageability, economic viability, ecological balance and social acceptability.",
        ),
        (
            "Disparity versus diversity",
            "Regional diversity means unranked difference of character, while regional disparity means ranked inequality of outcomes such as income, literacy, health or infrastructure.",
        ),
        (
            "National Planning Committee 1938",
            "Khullar traces Indian planning back to the National Planning Committee of 1938.",
        ),
        (
            "Planning Commission and First Plan",
            "The Planning Commission was set up in 1950 and the First Five Year Plan launched the centralised planning framework in 1950-51.",
        ),
        (
            "First Plan priorities",
            "The First Plan prioritised irrigation, agriculture, refugee resettlement, power and early resource-region thinking.",
        ),
        (
            "Second Plan heavy industry",
            "The Second Plan shifted emphasis towards heavy industry and the public-sector industrial base.",
        ),
        (
            "Annual Plans and last cycle",
            "India moved to Annual Plans in 1966-69 after war, drought and macro stress, and the Twelfth Plan was the last Five Year Plan cycle.",
        ),
        (
            "Balanced development remained incomplete",
            "Khullar explicitly treats the failure to achieve balanced regional development as a major shortcoming of the Five Year Plan era.",
        ),
        (
            "NITI replacement date",
            "The Planning Commission was replaced by NITI Aayog on 1 January 2015.",
        ),
        (
            "NITI planning style",
            "The NITI era stresses think-tank coordination, cooperative and competitive federalism, dashboards and mission-mode monitoring rather than plan outlay alone.",
        ),
        (
            "Aspirational Districts",
            "NITI Aayog launched the Aspirational Districts Programme in January 2018 for 112 districts.",
        ),
        (
            "SDG India Index 2023-24",
            "The SDG India Index 2023-24 gave India an overall score of 71 and shows development benchmarking through territorial indicators.",
        ),
        (
            "District and block targeting",
            "Current planning geography pushes targeting downward from state averages to districts and blocks because intra-state disparity is often as serious as interstate disparity.",
        ),
    ],
    [
        "Do not confuse regional diversity with regional disparity.",
        "Do not treat growth poles as a guarantee of spread effects.",
        "Do not say a strong core always benefits its periphery.",
        "Do not describe planning regions as only administrative map units.",
        "Do not reduce regional imbalance to poor states alone; districts matter too.",
        "Do not forget the National Planning Committee in the pre-Independence planning timeline.",
        "Do not swap the First Plan's agrarian priority with the Second Plan's heavy-industry emphasis.",
        "Do not say Five Year Plans ended all planning in India.",
        "Do not misdate the replacement of the Planning Commission by NITI Aayog.",
        "Do not treat district dashboards as the same thing as plan outlays.",
        "Do not quote state rankings or income gaps from memory without a source-year label.",
        "Do not invent a direct PYQ beyond the verified 2024 regional-disparity demand.",
    ],
    [
        (
            10,
            "Distinguish regional disparity from regional diversity.",
            "Diversity is unranked difference, while disparity is ranked inequality; the distinction matters because policy should protect diversity but reduce disparity.",
            [0, 1, 8],
        ),
        (
            10,
            "Explain why planning regions need more than mere contiguity.",
            "A planning region is viable only when functional, economic, administrative, ecological and social criteria align well enough for implementation.",
            [7],
        ),
        (
            15,
            "Use growth-pole, core-periphery and spread-backwash ideas to explain regional imbalance.",
            "Regional imbalance persists because development clusters in propulsive nodes, dominant cores drain surrounding regions, and spread effects remain weaker than backwash in many settings.",
            [2, 3, 4, 5, 6],
        ),
        (
            15,
            "Trace the major spatial priorities of India's First and Second Five Year Plans.",
            "The First Plan stressed irrigation, agriculture, refugee resettlement and power, while the Second Plan shifted toward heavy industry and the public-sector industrial base.",
            [10, 11, 12],
        ),
        (
            20,
            "Why did balanced regional development remain an incomplete achievement in India despite successive plans?",
            "Regional disparity persisted because irrigation, industry, markets, connectivity and governance capacity remained uneven, so backwash forces often beat spread effects even under planned development.",
            [2, 5, 14, 19],
        ),
        (
            20,
            "Has India moved from planning by Five Year Plans to planning by dashboards? Analyse.",
            "India's planning style has changed from centralised plan documents to mission platforms, district dashboards and territorial benchmarking, but the core geographic problem of regional imbalance remains.",
            [13, 15, 16, 17, 18, 19],
        ),
    ],
    [
        plan("Regional development meaning", [0, 1], "Development must stay tied to a territorial unit, not only to GDP.", "Define region, development and regional planning before using theory."),
        plan("Why regions develop unevenly", [2], "Do not attribute unevenness to one cause alone.", "List resource, transport, market, policy and historical drivers as a combined mechanism."),
        plan("Perroux growth pole logic", [3], "Growth poles can become enclaves if diffusion fails.", "Use propulsive nodes and outward linkage logic carefully."),
        plan("Core-periphery structure", [4], "A core is not automatically a benefactor to the periphery.", "Explain dominance, dependency and selective concentration."),
        plan("Spread and backwash", [5], "Balanced development depends on which effect becomes stronger.", "Use Myrdal to show why inequality can widen under growth."),
        plan("Balanced versus unbalanced growth", [6], "Do not make the debate sound like one settled answer.", "Use it as an evaluative paragraph after theory."),
        plan("Planning region criteria", [7], "A planning region must be functional and implementable together.", "Move from map coherence to real administrative viability."),
        plan("Disparity versus diversity", [8], "Difference of character is not the same as inequality of outcome.", "Use this distinction as the 2024 GS-I firewall."),
        plan("National Planning Committee to Planning Commission", [9, 10], "Pre-Independence planning imagination matters in the timeline.", "Trace the 1938 committee to the 1950 Planning Commission."),
        plan("First Plan priorities", [11], "Do not rewrite the First Plan as a heavy-industry plan.", "Stress irrigation, agriculture, refugee resettlement and power."),
        plan("Second Plan shift", [12], "Heavy industry belongs to the Second Plan, not the First.", "Contrast agrarian recovery with the industrial base strategy."),
        plan("Annual Plans and the last cycle", [13], "Five Year Plans were interrupted and then ended; they were not one uninterrupted chain.", "Use Annual Plans and the Twelfth Plan boundary to structure the timeline."),
        plan("Why imbalance persisted", [14], "Planned development did not erase core-periphery outcomes automatically.", "Connect uneven irrigation, industry and governance capacity to persistent disparity."),
        plan("NITI Aayog transition", [15, 16], "Replacing the Planning Commission changed style, not the need for regional planning.", "Contrast outlay logic with dashboards and cooperative federalism."),
        plan("District and block targeting", [17, 18, 19], "State averages hide district and block disparities.", "End with Aspirational Districts, SDG India Index and the downward shift in scale."),
    ],
    [
        panel("Diversity versus disparity", "comparison-table", [
            "DIVERSITY -> difference of character: language, ecology, culture, crops",
            "DISPARITY -> ranked inequality: income, literacy, health, infrastructure",
            "POLICY -> diversity is accommodated; disparity is reduced",
            "TRAP -> treating inequality as harmless variety is a direct exam error",
        ], ["Disparity versus diversity"]),
        panel("Uneven development drivers", "causal-system", [
            "RESOURCE ENDOWMENT -> minerals, fertile land, ports or irrigation cluster growth",
            "TRANSPORT + MARKET -> corridors and urban nodes outpace interiors",
            "HISTORICAL HEAD START -> earlier centres keep cumulative advantage",
            "STATE CAPACITY -> policy and governance decide whether lagging regions catch up",
        ], ["Uneven development drivers"]),
        panel("Growth pole mechanism", "process-flow", [
            "PROPULSIVE NODE -> dynamic industry or city becomes the growth pole",
            "LINKAGES -> suppliers, labour and markets cluster around the pole",
            "SPREAD EFFECT -> benefits diffuse outward if linkages deepen locally",
            "LIMIT -> a pole may remain an enclave without regional diffusion",
        ], ["Perroux growth pole idea", "Balanced-unbalanced growth debate"]),
        panel("Core-periphery and backwash", "comparison-table", [
            "CORE -> capital, services, infrastructure and decision power concentrate",
            "PERIPHERY -> labour, raw materials and demand are organised around the core",
            "BACKWASH -> talent and capital drain outward toward the core",
            "SPREAD -> technology and demand may diffuse, but not automatically",
        ], ["Friedmann core-periphery logic", "Myrdal spread and backwash"]),
        panel("Planning region criteria", "comparison-table", [
            "FUNCTIONAL UNITY -> flows and linkages hold the region together",
            "ADMINISTRATIVE MANAGEABILITY -> policy must actually be implementable",
            "ECONOMIC + ECOLOGICAL VIABILITY -> strategy and resource base must align",
            "SOCIAL ACCEPTABILITY -> regional identity and needs affect success",
        ], ["Planning region criteria"]),
        panel("Indian planning timeline", "timeline-strip", [
            "1938 -> National Planning Committee begins the planning imagination",
            "1950-51 -> Planning Commission set up and First Plan launched",
            "1966-69 -> Annual Plans after war, drought and macro stress",
            "2012-17 / 2015 -> Twelfth Plan last cycle; NITI replaces Planning Commission",
        ], ["National Planning Committee 1938", "Planning Commission and First Plan", "Annual Plans and last cycle", "NITI replacement date"]),
        panel("First versus Second Plan", "comparison-table", [
            "FIRST PLAN -> irrigation, agriculture, refugee resettlement, power",
            "SECOND PLAN -> heavy industry and public-sector industrial base",
            "SPATIAL LOGIC -> agrarian recovery first, industrial concentration next",
            "TRAP -> do not swap the priorities of the two plans",
        ], ["First Plan priorities", "Second Plan heavy industry"]),
        panel("Why imbalance persisted", "causal-system", [
            "UNEVEN IRRIGATION -> Green Revolution gains stayed regionally selective",
            "INDUSTRIAL CONCENTRATION -> ports, metros and corridors pulled ahead",
            "CONNECTIVITY + GOVERNANCE GAPS -> interiors remained infrastructure-poor",
            "OUTCOME -> balanced regional development stayed incomplete",
        ], ["Balanced development remained incomplete", "Uneven development drivers"]),
        panel("Planning Commission versus NITI", "comparison-table", [
            "PLANNING COMMISSION -> centralised plan formulation and outlay logic",
            "NITI AAYOG -> think-tank coordination, competitive and cooperative federalism",
            "PLAN DOCUMENTS -> long-horizon allocation framework",
            "DASHBOARDS -> indicator monitoring and mission-mode comparison",
        ], ["NITI replacement date", "NITI planning style"]),
        panel("District and block targeting ladder", "institutional-ladder", [
            "STATE AVERAGE -> useful but hides internal inequality",
            "DISTRICT TARGETING -> Aspirational Districts brings lagging districts into focus",
            "BLOCK TARGETING -> scale moves further downward where district averages still hide gaps",
            "GEOGRAPHIC LESSON -> intra-state disparity is a first-order planning problem",
        ], ["Aspirational Districts", "District and block targeting"]),
        panel("SDG-style benchmarking", "comparison-table", [
            "SDG INDIA INDEX 2023-24 -> overall India score 71",
            "TERRITORIAL INDICATORS -> development is ranked spatially, not only nationally",
            "CURRENT STYLE -> dashboards complement missions and programme convergence",
            "SAFE USE -> planning changed form, but not the geography of disparity",
        ], ["SDG India Index 2023-24", "NITI planning style"]),
        panel("Regional development answer spine", "answer-spine", [
            "DEFINE -> disparity versus diversity and the meaning of regional planning",
            "EXPLAIN -> growth pole, core-periphery, spread and backwash",
            "TRACE -> 1938 committee, First Plan, Second Plan, NITI transition",
            "QUALIFY -> district dashboards matter because state averages conceal disparity",
        ], ["Disparity versus diversity", "National Planning Committee 1938", "NITI planning style"]),
    ],
    [
        "growth pole",
        "core-periphery",
        "backwash",
        "planning region",
        "regional disparity",
        "National Planning Committee",
        "Planning Commission",
        "NITI Aayog",
        "Aspirational Districts",
        "SDG India Index",
    ],
    (
        "This topic has a verified direct routed demand: the 2024 GS-I question asking what regional disparity is, how it differs from diversity and how serious it is in India. The package therefore keeps the disparity-diversity distinction explicit and does not fabricate any additional direct PYQ."
    ),
    [
        (
            "2024",
            "GS-I",
            "What is regional disparity? How does it differ from diversity? How serious is the issue of regional disparity in India?",
            "Verified direct PYQ routed inside the Advanced owner for Geography Topic 29.",
            "Regional disparity means ranked inequality among regions in income, productivity, infrastructure, literacy, health and opportunity, whereas regional diversity means unranked difference of character such as language, ecology or cropping pattern. India shows serious disparity because growth, irrigation, industry, services and governance capacity have clustered unevenly across states, districts and metropolitan corridors, and intra-state inequality often rivals interstate inequality. A balanced answer should therefore separate diversity from disparity, explain why markets and historical head starts concentrate development, and conclude that planning has changed in form but regional imbalance remains a first-order problem.",
        ),
    ],
    [
        "https://www.niti.gov.in/",
        "https://pib.gov.in/",
    ],
    (
        "NITI Aayog dashboards, the Aspirational Districts programme and the SDG India Index are used only as dated anchors for the present planning style. No district ranking, fiscal outlay or state-gap figure is quoted here without an explicit source-year label."
    ),
)
