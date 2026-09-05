"""Authored Economy learner-v2 data for Topic 01."""

from __future__ import annotations

import generate_economy_common as common


def panel(title: str, kind: str, lines: list[str]) -> tuple[str, str, str, list[str]]:
    return (
        title,
        kind,
        "\n".join(lines),
        [
            "upsc-ai-kit/knowledge/Economy/basic/01_National-Income-GDP-GVA-and-Measurement.md",
            "upsc-ai-kit/knowledge/Economy/advanced/01_National-Income-GDP-GVA-and-Measurement.md",
        ],
    )


FACTS = [
    ("Territory-residence boundary", "GDP follows production within domestic territory, whereas GNP follows income accruing to normal residents; the sign of net factor income from abroad determines whether GNP is above or below GDP."),
    ("GDP expenditure identity", "GDP at market prices can be read from final expenditure as C + I + G + (X - M); imports are subtracted because consumption and investment totals can contain foreign production."),
    ("GDP-GVA reconciliation", "GDP at market prices equals GVA at basic prices plus product taxes minus product subsidies, so changing net product taxes can make GDP and GVA growth diverge."),
    ("Gross-net distinction", "Gross measures include consumption of fixed capital, while NDP equals GDP minus depreciation and NNP equals GNP minus depreciation."),
    ("Three measurement methods", "Production or value-added, income and expenditure methods should theoretically converge because produced output creates income and is purchased as final expenditure; each method has a different data risk."),
    ("Double-counting boundary", "The production method sums value added at each stage rather than gross sales, preventing the value of intermediate inputs from being counted again inside final output."),
    ("Income-side coverage", "The income method adds wages, profits, rent and mixed income, but India's large informal sector requires survey, administrative and benchmark-indicator estimation rather than complete enterprise accounts."),
    ("Expenditure-side boundary", "The expenditure method counts private and government final consumption, capital formation and net exports while excluding intermediate purchases and pure financial transfers."),
    ("Nominal-real-deflator triangle", "Nominal GDP uses current prices, real GDP uses constant or base-year prices, and the GDP deflator equals nominal GDP divided by real GDP multiplied by 100."),
    ("Production boundary", "Current final goods and services, applicable imputations and government services valued mainly by production cost enter GDP; intermediate goods already embodied in final output do not."),
    ("Transfer and resale exclusions", "Pure transfer payments and resale of an existing asset do not add current production, although the current brokerage or service associated with a resale can add value."),
    ("Unpaid work and welfare limit", "Conventional GDP excludes much unpaid household work and does not directly measure distribution, ecological depletion, service quality or every dimension of welfare."),
    ("2015 national-accounts revision", "India's 2015 revision shifted the national-accounts base to 2011-12 and expanded use of corporate administrative data, improving relevance while creating a comparability need for a reliable back series."),
    ("2026 series revision", "MoSPI released the 2022-23-base GDP series on 27 February 2026 with revised coverage, sources and methods; the owner records that a complete comparable back series was still pending at its 19 July 2026 cutoff."),
    ("Potential GDP and output gap", "Potential GDP is sustainable capacity implied by labour, capital and productivity, while the output gap compares actual output with that estimated capacity; potential output is not directly observed."),
    ("ICOR and investment efficiency", "The Incremental Capital-Output Ratio links additional capital to additional output; a higher ICOR signals weaker aggregate investment efficiency, so high saving or investment need not produce high growth."),
    ("PPP versus market exchange rate", "Purchasing Power Parity uses a common price basket for real purchasing-power comparison, whereas market-exchange-rate GDP is suited to external trade, debt and market-size comparison; ranks are reference-year specific."),
    ("Intangible capital formation", "Research and development, software and databases, mineral exploration and artistic originals can be gross fixed capital formation, while advertising, routine training and much brand creation remain intermediate consumption."),
    ("Sector and capital classification", "Primary, secondary and tertiary activity classification concerns the nature of production, while working capital is used up in production and fixed capital provides services over multiple periods."),
    ("Estimate-vintage discipline", "A national-accounts number must retain its period, series base and estimate vintage such as First Advance Estimate, later advance estimate or revised estimate; a projection or old-series estimate is not an actual on a new series."),
]

TRAPS = [
    "Do not treat every market transaction as current production; old-asset resale and transfers are excluded.",
    "Do not equate domestic territory with resident income; GDP and GNP answer different boundary questions.",
    "Do not say net measures include depreciation; net measures deduct consumption of fixed capital.",
    "Do not splice 2011-12-base and 2022-23-base growth or levels without an official comparable series.",
    "Do not use nominal GDP growth as proof of volume growth or welfare improvement.",
    "Do not describe every intangible outlay as investment; national-accounting capitalisation has a defined boundary.",
    "Do not compare PPP and market-exchange-rate ranks without the reference year and purpose.",
    "Do not treat a First Advance Estimate or projection as a final actual.",
    "Do not count intermediate inputs again inside final output.",
    "Do not infer that high saving guarantees high growth when ICOR and implementation quality can weaken conversion.",
    "Do not treat potential GDP as directly observed; it is method-dependent.",
    "Do not infer welfare, distribution or ecological sustainability from GDP alone.",
]

SESSION_TITLES = [
    "Territory, residence and final expenditure",
    "Producer value added and purchaser prices",
    "Gross output and depreciation",
    "Three routes to the same aggregate",
    "Value added and double-counting control",
    "Income coverage and expenditure boundaries",
    "Nominal output, real output and the deflator",
    "Inside the production boundary",
    "Transfers, resales and current services",
    "Unpaid work and the welfare boundary",
    "The 2015 and 2022-23-base revisions",
    "Potential GDP and the output gap",
    "ICOR and investment efficiency",
    "PPP comparison and intangible investment",
    "Sector, capital and estimate-vintage classification",
]

ANSWER_ROUTES = [
    "Open with the accounting boundary, reconcile the formula, and only then assess performance.",
    "Separate measurement change from real economic change before drawing a growth conclusion.",
    "Use one named Indian revision, one method limitation and one welfare qualification.",
]

PANELS = [
    panel("Territory before arithmetic", "boundary-map", ["DOMESTIC TERRITORY -> GDP", "NORMAL RESIDENCE -> GNP", "NFIA BRIDGE -> GDP + NFIA", "TRAP -> location and ownership are not the same boundary"]),
    panel("Gross-to-net ladder", "replacement-ladder", ["GDP -> minus depreciation -> NDP", "GNP -> minus depreciation -> NNP", "GROSS -> capital consumption retained", "NET -> capital consumption deducted"]),
    panel("Three-method convergence", "triangular-flow", ["PRODUCTION -> value added", "INCOME -> wages + profits + rent + mixed income", "EXPENDITURE -> C + I + G + (X - M)", "IDENTITY -> one output, three measurement routes"]),
    panel("GDP-GVA tax bridge", "equation-band", ["GVA AT BASIC PRICES", "+ PRODUCT TAXES", "- PRODUCT SUBSIDIES", "= GDP AT MARKET PRICES"]),
    panel("Nominal-real decoder", "comparison-matrix", ["NOMINAL -> current prices -> size and ratios", "REAL -> base-year prices -> volume growth", "DEFLATOR -> nominal / real x 100", "LIMIT -> base revision changes the comparison frame"]),
    panel("Production-boundary gate", "inclusion-gate", ["IN -> current final goods and services", "IN -> permitted imputations and government services", "OUT -> embedded intermediate inputs and pure transfers", "OUT -> old assets except current brokerage"]),
    panel("Informal-sector estimation", "evidence-chain", ["MISSING COMPLETE ACCOUNTS", "-> surveys + administrative sources", "-> benchmark-indicator extrapolation", "LIMIT -> shocks can break historical ratios"]),
    panel("Base-year revision timeline", "timeline-strip", ["2015 -> shift to 2011-12 base", "27 FEB 2026 -> release of 2022-23-base series", "19 JUL 2026 CUTOFF -> full back series pending", "RULE -> never splice unsupported series"]),
    panel("Capacity diagnosis", "gap-diagram", ["ACTUAL < POTENTIAL -> negative output gap", "ACTUAL NEAR CAPACITY -> demand stimulus meets supply limits", "POTENTIAL -> labour + capital + productivity", "LIMIT -> capacity is estimated, not observed"]),
    panel("Saving-to-growth conversion", "causal-chain", ["SAVING -> INVESTMENT", "INVESTMENT -> capital formation", "ICOR -> capital needed per extra output", "HIGH ICOR -> weak conversion efficiency"]),
    panel("Cross-country comparison fork", "purpose-fork", ["PPP -> common basket -> purchasing power", "MARKET RATE -> external value -> trade and debt", "SAME OUTPUT, DIFFERENT PRICE BASIS", "RULE -> quote source and reference year"]),
    panel("Examiner closing spine", "answer-spine", ["DEFINE -> boundary + formula", "VERIFY -> base year + period + vintage", "ANALYSE -> coverage + method + efficiency", "QUALIFY -> distribution + unpaid work + ecology"]),
]

PYQ_NOTE = (
    "Audited Economy ledgers route 2020 GS-III on potential GDP and output gap "
    "and 2021 GS-III on the pre/post-2015 GDP methodology change to this Basic "
    "owner. Objective routes on ICOR, PPP, sector classification, physical "
    "capital and intangible investment are retained as concepts without "
    "inventing answer letters."
)

PYQ_SOLUTIONS = [
    common.make_pyq_solution(FACTS, "2020", "GS-III", "Define potential GDP, explain its determinants and examine India's output gap.", "Verified routed Mains demand; original model solution, not an official answer.", [14, 15, 19]),
    common.make_pyq_solution(FACTS, "2021", "GS-III", "Explain changes in India's GDP computation methodology before and after the 2015 revision.", "Verified routed Mains demand; original model solution, not an official answer.", [4, 6, 12, 13]),
]

TOPIC_01 = common.topic(
    1,
    "National Income: GDP, GVA, GNP, NDP and Measurement",
    "01_National-Income-GDP-GVA-and-Measurement",
    "01_National-Income-GDP-GVA-GNP-NDP-and-Measurement_Learner-V2-Complete-Topic-Package.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish GDP, GVA, GNP and NDP and explain why the distinctions matter.", [0, 2, 3]),
        (10, "Why can GDP and GVA growth tell different stories in the same year?", [2, 19]),
        (15, "Explain how the three methods of national-income measurement converge and where Indian data risks arise.", [4, 5, 6, 7]),
        (15, "A base-year revision improves relevance but complicates historical comparison. Examine.", [12, 13, 19]),
        (20, "Critically assess GDP as a measure of India's economic performance and welfare.", [8, 11, 14, 16, 19]),
        (20, "Analyse the saving-investment-growth chain with ICOR, intangible capital and measurement limitations.", [15, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    ["GDP", "GVA", "GNP", "NDP", "NFIA", "2022-23", "ICOR", "Purchasing Power Parity", "intangible"],
    PYQ_NOTE,
    PYQ_SOLUTIONS,
    [
        "https://mospi.gov.in/uploads/release_calendar/1772190058170_Press_Note_on_New_Series_of_GDP_Estimates_with_Base_Year_2022-23_27022026.pdf — attempted 2026-09-03; the official PDF was retrievable only as binary content through the live fetcher, so no text or number was extracted from that attempt and the repository owner's dated record was used unchanged.",
        "https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=metadata — attempted 2026-09-03; only the Ministry title shell was returned, so no national-accounts claim was taken from it.",
    ],
    "Live official checks on 2026-09-03 did not yield independently extractable national-accounts text. The package therefore preserves the owner's exact 27 February 2026 release date, 2022-23 base, back-series cutoff and estimate-vintage cautions without manufacturing a fresh growth number.",
    allow_existing_history=False,
)
