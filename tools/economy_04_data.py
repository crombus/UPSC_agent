"""Authored Economy learner-v2 data for Topic 04."""

from __future__ import annotations

import generate_economy_common as common


def panel(title: str, kind: str, lines: list[str]) -> tuple[str, str, str, list[str]]:
    return (
        title,
        kind,
        "\n".join(lines),
        [
            "upsc-ai-kit/knowledge/Economy/basic/04_RBI-Monetary-Policy-and-Liquidity-Management.md",
            "upsc-ai-kit/knowledge/Economy/advanced/04_RBI-Monetary-Policy-and-Liquidity-Management.md",
        ],
    )


FACTS = [
    ("Repo-rate signal", "The repo rate is the policy rate for collateralised liquidity from RBI under the operating framework; a repo-rate decision signals stance but is not identical to every liquidity injection."),
    ("Standing Deposit Facility", "The SDF is an uncollateralised RBI facility for absorbing surplus liquidity and has served as the floor-side standing facility since its introduction in 2022."),
    ("Marginal Standing Facility", "MSF is an overnight backstop borrowing window for scheduled commercial banks against eligible securities; its counterparty and emergency role differ from ordinary repo operations."),
    ("Cash Reserve Ratio", "CRR is the share of net demand and time liabilities maintained as cash with RBI, broadly impounding bank resources and affecting lendable funds."),
    ("Open Market Operations", "OMO purchases or sales are outright transactions in government securities that add or absorb durable liquidity and can influence yields beyond overnight cash conditions."),
    ("WACR operating target", "The weighted average call rate is the operating target that RBI liquidity operations seek to align with the policy corridor; the policy target, repo rate and operating target are distinct."),
    ("Monetary Policy Committee", "The six-member MPC consists of the RBI Governor, the monetary-policy Deputy Governor, one RBI-nominated officer and three external members appointed by the Central Government, and decides the policy repo rate."),
    ("Flexible inflation targeting", "India's framework uses headline CPI as the nominal anchor with a 4 per cent target and a tolerance band of plus or minus 2 percentage points while considering growth."),
    ("Statutory RBI status", "RBI is a statutory body under the RBI Act, not a constitutional body; the Governor is appointed by the Central Government and RBI performs monetary, currency, banking, reserve and payment functions."),
    ("Transmission chain", "MPC communication and the repo signal influence money-market rates, bank funding and deposit rates, lending rates, bond yields, credit, demand, output and inflation with lags."),
    ("SDF-liquidity distinction", "The 2022 SDF illustrates that RBI can absorb collateral-free surplus liquidity to align overnight rates without necessarily changing the repo-rate stance."),
    ("Pandemic policy package", "During the pandemic RBI combined repo reductions with CRR easing, OMOs and targeted longer-term liquidity operations, showing that expansionary policy is an instrument package rather than a repo cut alone."),
    ("Uneven pass-through", "Post-pandemic repo increases passed relatively quickly into external-benchmark-linked lending rates and more gradually into deposit rates and legacy loans because funding mix, competition and balance-sheet strength differ."),
    ("Forex intervention and sterilisation", "RBI may sell or buy foreign exchange to smooth excessive rupee volatility and offset the domestic-liquidity effect through OMOs or absorption operations; sterilisation does not imply a fixed exchange-rate promise."),
    ("OMO and yield conditions", "OMO affects durable liquidity and the government-securities yield curve, but its effect depends on market expectations, the fiscal borrowing environment and the broader monetary stance."),
    ("Legal tender and RBI liabilities", "Legal tender must be accepted in settlement within the legal framework, and Indian currency notes issued are liabilities on RBI's balance sheet rather than RBI income."),
    ("Money multiplier", "Reserve money supports broader money creation through banking; lower reserve impounding and currency leakage and greater willingness to lend generally raise the money multiplier."),
    ("RBI income sources", "RBI income can arise from interest on government securities and foreign-currency assets, liquidity operations or lending to banks, and fees or commissions from banking and market functions."),
    ("Payment-data direction", "RBI required payment-system data relating to systems operated in India to be stored in India for supervisory access; this is a regulated payments direction, not a universal data-localisation law."),
    ("Committee-institution pairs", "The Hilton-Young Commission concerns colonial currency and central-banking reform, Narasimham Committees concern Government of India banking reform, and the Tarapore Committee concerns RBI work on capital-account convertibility."),
]

TRAPS = [
    "Do not equate every liquidity injection with a repo-rate cut.",
    "Do not treat OMO and repo as identical; one is outright and the other is a repurchase transaction.",
    "Do not assume ordinary NBFCs have routine LAF access like scheduled banks.",
    "Do not call currency notes RBI income; notes issued are liabilities.",
    "Do not assume a lower repo guarantees equal lending-rate reductions.",
    "Do not merge the inflation target, tolerance band, repo rate and WACR operating target.",
    "Do not treat SDF as collateralised borrowing; it is uncollateralised absorption.",
    "Do not say CRR and OMO have the same mechanics or time horizon.",
    "Liquidity management aligns market rates with the operating framework; it is distinct from a fresh change in the monetary-policy stance.",
    "Do not claim monetary policy can directly repair food, energy or logistics shortages.",
    "Do not generalise a payment-system storage direction into a law for all data.",
    "Do not mismatch reform committees with their sponsoring institution or subject.",
]

SESSION_TITLES = [
    "Repo signal and SDF absorption",
    "MSF as the overnight backstop",
    "CRR and broad reserve impounding",
    "OMO and durable liquidity",
    "WACR as the operating target",
    "MPC architecture and flexible inflation targeting",
    "RBI's statutory mandate",
    "From policy signal to macro outcome",
    "Why liquidity management differs from stance",
    "Pandemic multi-instrument easing",
    "Uneven pass-through and forex sterilisation",
    "OMO effects on yields and conditions",
    "Legal tender and RBI liabilities",
    "Money multiplier and RBI income",
    "Payment directions and committee pairs",
]

ANSWER_ROUTES = [
    "Separate the repo signal from liquidity implementation and then trace pass-through.",
    "Evaluate monetary effectiveness by inflation source, banking health, fiscal conditions and external pressure.",
    "Conclude with credible communication, flexible operations and realistic limits on rate policy.",
]

PANELS = [
    panel("Policy signal versus implementation", "two-track-rail", ["MPC -> repo-rate signal", "RBI OPERATIONS -> liquidity alignment", "WACR -> operating target", "TRAP -> stance and quantity are distinct"]),
    panel("Liquidity corridor", "corridor-map", ["MSF -> overnight backstop", "REPO -> collateralised injection", "WACR -> market operating rate", "SDF -> uncollateralised absorption"]),
    panel("CRR versus OMO", "comparison-matrix", ["CRR -> reserve impounding ratio", "OMO -> outright G-sec transaction", "CRR -> broad bank-resource effect", "OMO -> durable liquidity + yield effect"]),
    panel("MPC institution map", "institution-map", ["RBI GOVERNOR", "MONETARY-POLICY DEPUTY GOVERNOR", "ONE RBI OFFICER + THREE EXTERNAL MEMBERS", "SIX MEMBERS -> repo decision"]),
    panel("Inflation target frame", "target-band", ["NOMINAL ANCHOR -> headline CPI", "TARGET -> 4 per cent", "TOLERANCE -> plus/minus 2 percentage points", "MANDATE -> price stability while mindful of growth"]),
    panel("Transmission chain", "causal-chain", ["REPO + COMMUNICATION", "-> WACR + funding + deposit rates", "-> lending rates + credit + demand", "-> output and inflation with lags"]),
    panel("Pandemic package", "instrument-stack", ["REPO REDUCTIONS", "CRR EASING", "OMO PURCHASES", "TARGETED LONGER-TERM LIQUIDITY"]),
    panel("Pass-through frictions", "friction-map", ["EBLR LOANS -> faster response", "DEPOSITS / LEGACY LOANS -> slower response", "FRICTIONS -> funding + competition + risk", "RESULT -> uneven burden"]),
    panel("Forex-liquidity bridge", "sterilisation-flow", ["FOREX INTERVENTION", "-> domestic liquidity changes", "-> OMO / absorption offset", "LIMIT -> volatility smoothing, not a fixed rate"]),
    panel("Money multiplier", "multiplier-flow", ["RESERVE MONEY", "-> bank deposits and lending", "LOWER CRR / LEAKAGE -> higher potential multiplier", "LIMIT -> banks may hold reserves or avoid risk"]),
    panel("RBI balance-sheet traps", "classification-board", ["NOTES ISSUED -> liability", "G-SEC / FX INTEREST -> income source", "PAYMENT STORAGE -> supervisory direction", "COMMITTEES -> match sponsor and subject"]),
    panel("Monetary-policy answer spine", "answer-spine", ["DIAGNOSE inflation and output", "STATE MPC signal", "MAP liquidity implementation", "TEST transmission, growth and external limits"]),
]

PYQ_NOTE = (
    "This Basic owner carries audited objective routes on legal tender, rupee "
    "management, payment-data storage, the money multiplier, expansionary "
    "instruments, RBI status, lender of last resort, interest-rate hikes, "
    "sterilisation, RBI income and reform committees. No routed Mains demand "
    "is manufactured and no unavailable or provisional objective answer is inferred."
)

TOPIC_04 = common.topic(
    4,
    "RBI, Monetary Policy and Liquidity Management",
    "04_RBI-Monetary-Policy-and-Liquidity-Management",
    "04_RBI-Monetary-Policy-and-Liquidity-Management_Learner-V2-Complete-Topic-Package.md",
    FACTS,
    TRAPS,
    [
        (10, "Why is liquidity management necessary after an MPC repo-rate decision?", [0, 1, 5]),
        (10, "Distinguish repo, SDF, MSF, CRR and OMO.", [0, 1, 2, 3, 4]),
        (15, "Explain India's monetary-policy transmission chain and its frictions.", [9, 12, 14]),
        (15, "Assess the role of OMOs and sterilisation in liquidity and external management.", [4, 13, 14]),
        (20, "Critically evaluate India's flexible inflation-targeting and MPC framework.", [6, 7, 9, 12]),
        (20, "Analyse RBI's monetary, liquidity, currency and payment functions with their legal boundaries.", [8, 15, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    ["repo rate", "Standing Deposit Facility", "MSF", "CRR", "OMO", "WACR", "MPC", "4 per cent", "sterilisation"],
    PYQ_NOTE,
    [],
    [
        "https://www.rbi.org.in/Scripts/Annualpolicy.aspx — attempted 2026-09-03; the official page returned raw HTML identifying the RBI Monetary Policy page but no safely extracted current resolution, rate or stance, so no live policy number was used.",
    ],
    "The RBI Monetary Policy page was reachable only as raw HTML in this run. No current repo rate, stance, reserve ratio, liquidity amount or meeting outcome was extracted; the package relies on the audited owners for stable instrument mechanics and preserves every counterparty and legal distinction.",
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)
