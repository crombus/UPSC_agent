"""Authored Economy learner-v2 data for Topic 03."""

from __future__ import annotations

import generate_economy_common as common


def panel(title: str, kind: str, lines: list[str]) -> tuple[str, str, str, list[str]]:
    return (
        title,
        kind,
        "\n".join(lines),
        [
            "upsc-ai-kit/knowledge/Economy/basic/03_Inflation-Price-Indices-and-Business-Cycles.md",
            "upsc-ai-kit/knowledge/Economy/advanced/03_Inflation-Price-Indices-and-Business-Cycles.md",
        ],
    )


FACTS = [
    ("Inflation, disinflation and deflation", "Inflation is a sustained rise in the general price level, disinflation is a fall in the inflation rate while prices may still rise, and deflation is a sustained fall in the general price level."),
    ("Headline and core inflation", "Headline CPI includes food and fuel, while core inflation conventionally excludes them; relative component movements mean core is not mechanically always below headline."),
    ("CPI coverage", "CPI is a retail consumer basket that includes services and has a larger food component than WPI; headline CPI is India's formal inflation-targeting nominal anchor."),
    ("WPI coverage", "WPI is a wholesale-goods price index compiled by the Office of the Economic Adviser, excludes services and is not a household cost-of-living measure."),
    ("GDP deflator coverage", "The GDP deflator is derived from nominal and real national accounts and covers domestically produced final goods and services; it is broader but less suited to monthly retail-inflation management."),
    ("Demand-pull inflation", "Demand-pull inflation arises when aggregate spending grows faster than available output, especially as the positive output gap narrows spare capacity."),
    ("Cost-push and supply inflation", "Cost-push inflation arises from input costs or supply constraints, so crop failure, logistics disruption or imported commodity scarcity can raise prices even with weak demand."),
    ("Output gap and stagflation", "A negative output gap weakens demand pressure but does not prevent supply-shock inflation; stagflation combines inflation with weak growth or high unemployment."),
    ("Expectations and persistence", "As price changes broaden, households and workers revise consumption, wage demands and expectations, which can make an initially temporary shock more persistent."),
    ("Policy assignment", "RBI and the MPC manage demand and expectations through rates, liquidity and communication, while governments use buffers, taxes, trade, logistics and anti-hoarding tools against physical supply shocks."),
    ("Lockdown supply shock", "India's 2020 lockdown combined activity contraction with transport, mandi and logistics disruption, illustrating why a negative output gap does not guarantee low headline inflation."),
    ("Imported commodity pass-through", "The 2021-22 commodity surge and Russia-Ukraine war raised crude, edible-oil and fertiliser costs, with pass-through shaped by taxes, subsidies, exchange rates and buffers."),
    ("Food-price administration", "Onion-price episodes and Price Stabilisation Fund interventions show why perishables may need buffer, logistics and calibrated trade action rather than a repo-only response."),
    ("Index divergence", "CPI, WPI and the GDP deflator can diverge because household services, wholesale goods and domestically produced final output have different coverage and weights."),
    ("Inflation targeting framework", "India's 2016 flexible inflation-targeting framework made headline CPI the formal nominal anchor and assigned the six-member MPC the collective repo-rate decision."),
    ("Distributional incidence", "Inflation harms poor and fixed-income households most because food and fuel occupy larger budget shares and indexation such as CPI-IW-linked dearness allowance protects organised workers unevenly."),
    ("Phillips-curve limit", "The short-run Phillips curve is a demand-management guide rather than a mechanical law; supply shocks can worsen inflation and output together."),
    ("Business-cycle sequence", "Recovery, expansion, peak, slowdown or recession and trough form a stylised business cycle, while potential output and the source of the shock determine the suitable policy response."),
    ("Demand determinants and deficit finance", "Consumer demand depends on income, expectations and substitute or complement prices, an inferior good can gain demand when income falls, and direct deficit monetisation is generally the most inflationary financing route because it expands reserve money directly."),
    ("Price-series break discipline", "MoSPI began current CPI releases on a 2024=100 series from January 2026 and the Office of the Economic Adviser introduced a 2022-23-base WPI for the May 2026 release onward; a revised basket is a measurement update, not a price shock."),
]

TRAPS = [
    "Do not say disinflation means prices are falling.",
    "Do not use WPI as a household cost-of-living index.",
    "Do not assume core inflation is always below headline inflation.",
    "Do not prescribe repo action as if it could produce vegetables or repair logistics.",
    "Do not treat a single commodity price rise as general inflation without breadth and persistence.",
    "Do not treat a base effect or index rebasing as a new price shock.",
    "Do not join CPI or WPI levels across base-year breaks without an official link.",
    "Do not assume a negative output gap eliminates supply inflation.",
    "Do not treat the Phillips curve as a stable mechanical trade-off under supply shocks.",
    "Do not ignore producer incentives when using export restrictions or price suppression.",
    "Do not assess inflation only by the aggregate rate; distribution and components matter.",
    "Do not call a Survey-period projection or historical-series figure a current actual.",
]

SESSION_TITLES = [
    "Inflation states, headline and core",
    "CPI as the household and policy basket",
    "WPI as the wholesale-goods basket",
    "GDP deflator and domestic output prices",
    "Demand-pull inflation and available output",
    "Cost-push shocks, output gaps and stagflation",
    "Expectations, wages and persistence",
    "Monetary and supply-side policy assignment",
    "The lockdown supply-shock lesson",
    "Imported commodity pass-through",
    "Food-price tools and index divergence",
    "Flexible inflation targeting and the MPC",
    "Distributional incidence of inflation",
    "Phillips-curve limits and business cycles",
    "Demand traps, monetisation and price-series breaks",
]

ANSWER_ROUTES = [
    "Diagnose the source, breadth, persistence and expectations channel before prescribing policy.",
    "Separate measurement from mechanism and assign each policy tool to the shock it can influence.",
    "Conclude with price stability as protection for real income without ignoring growth and producer incentives.",
]

PANELS = [
    panel("Three price-level states", "state-ladder", ["INFLATION -> prices rise", "DISINFLATION -> prices rise more slowly", "DEFLATION -> general price level falls", "TRAP -> rate change is not level change"]),
    panel("CPI-WPI-deflator matrix", "comparison-matrix", ["CPI -> retail basket + services", "WPI -> wholesale goods, no services", "GDP DEFLATOR -> domestic final output", "POLICY ANCHOR -> headline CPI"]),
    panel("Demand-pull chain", "causal-chain", ["SPENDING > AVAILABLE OUTPUT", "-> inventories and spare capacity shrink", "-> firms raise prices", "POLICY -> demand restraint can work"]),
    panel("Supply-shock chain", "bottleneck-flow", ["CROP / OIL / LOGISTICS SHOCK", "-> costs or availability worsen", "-> prices rise despite weak demand", "POLICY -> repair supply + anchor expectations"]),
    panel("Output gap fork", "gap-diagram", ["NEGATIVE GAP -> weak demand", "POSITIVE GAP -> overheating risk", "SUPPLY SHOCK -> inflation can coexist with negative gap", "STAGFLATION -> inflation + weak growth"]),
    panel("Expectations loop", "feedback-loop", ["PRICE SHOCK", "-> wage and price expectations", "-> second-round adjustments", "-> persistence beyond initial shock"]),
    panel("Policy assignment board", "instrument-map", ["RBI -> rates + liquidity + communication", "GOVERNMENT -> buffers + tax + trade", "STATES -> logistics + enforcement", "RULE -> tool must match shock"]),
    panel("India shock timeline", "timeline-strip", ["2020 -> lockdown logistics shock", "2021-22 -> global commodity surge", "2016 -> formal CPI-targeting framework", "LESSON -> demand and supply can conflict"]),
    panel("Distributional incidence", "incidence-map", ["POOR -> high food and fuel share", "FIXED INCOME -> real purchasing power falls", "INDEXED WORKERS -> partial protection", "TIGHTENING -> borrowers and MSMEs bear costs"]),
    panel("Business-cycle rail", "cycle-rail", ["TROUGH -> RECOVERY -> EXPANSION", "-> PEAK -> SLOWDOWN / RECESSION", "POLICY DEPENDS ON output gap and shock", "PHILLIPS CURVE -> guide, not law"]),
    panel("Index-series break", "timeline-gate", ["CPI 2024=100 -> releases from JAN 2026", "WPI 2022-23 base -> MAY 2026 onward", "NEW BASKET != NEW INFLATION", "RULE -> no casual level splicing"]),
    panel("Inflation answer spine", "answer-spine", ["IDENTIFY index + component", "DIAGNOSE demand / cost / supply", "TRACE expectations + distribution", "PRESCRIBE coordinated policy mix"]),
]

PYQ_NOTE = (
    "The audited ledgers route 2019 GS-III on growth with low inflation, 2022 "
    "GS-II on managing inflation and unemployment beyond welfare schemes, and "
    "2024 GS-III on food inflation and RBI effectiveness here. Objective "
    "routes on CPI-WPI, demand determinants, deficit monetisation and "
    "demand-pull inflation remain unkeyed in this package."
)

PYQ_SOLUTIONS = [
    common.make_pyq_solution(FACTS, "2019", "GS-III", "Discuss the Indian economy's GDP-growth and low-inflation combination.", "Verified routed Mains demand; original model solution.", [0, 5, 7, 13]),
    common.make_pyq_solution(FACTS, "2022", "GS-II", "Discuss managing inflation and unemployment beyond welfare schemes.", "Verified cross-cutting Mains demand; original model solution.", [9, 15, 16, 17]),
    common.make_pyq_solution(FACTS, "2024", "GS-III", "Comment on causes of persistent food inflation and the effectiveness of RBI monetary policy.", "Verified routed Mains demand; original model solution.", [6, 9, 12, 14]),
]

TOPIC_03 = common.topic(
    3,
    "Inflation, Price Indices and Business Cycles",
    "03_Inflation-Price-Indices-and-Business-Cycles",
    "03_Inflation-Price-Indices-and-Business-Cycles_Learner-V2-Complete-Topic-Package.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish inflation, disinflation and deflation.", [0, 1]),
        (10, "Why are CPI, WPI and the GDP deflator not interchangeable?", [2, 3, 4, 13]),
        (15, "Explain demand-pull and cost-push inflation with Indian evidence.", [5, 6, 10, 11]),
        (15, "Assess the distributional effects of inflation and disinflation.", [15, 16, 17]),
        (20, "Design a coordinated response to persistent food inflation without weakening farm incentives.", [6, 9, 12, 15]),
        (20, "Analyse inflation through output gaps, expectations, business cycles and index-vintage discipline.", [7, 8, 17, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    ["disinflation", "CPI", "WPI", "GDP deflator", "output gap", "stagflation", "Phillips curve", "2024=100", "2022-23"],
    PYQ_NOTE,
    PYQ_SOLUTIONS,
    [
        "https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=metadata — attempted 2026-09-03; only the Ministry title shell was returned, so no basket weight, index level or inflation rate was taken from it.",
        "https://eaindustry.nic.in/uploaded_files/wpi/WPI_Users_Note.pdf — not used as a live factual source because no substantive text was independently retrieved in this run; the repository owner's audited series note was preserved unchanged.",
    ],
    "The live CPI metadata attempt returned only a shell and no WPI text was independently retrieved. The package therefore uses no fresh inflation number and preserves only the owners' dated CPI 2024=100 and WPI 2022-23-base series-boundary statements.",
)
