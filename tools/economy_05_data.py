"""Authored Economy learner-v2 data for Topic 05."""

from __future__ import annotations

import generate_economy_common as common


def panel(title: str, kind: str, lines: list[str]) -> tuple[str, str, str, list[str]]:
    return (
        title,
        kind,
        "\n".join(lines),
        [
            "upsc-ai-kit/knowledge/Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md",
            "upsc-ai-kit/knowledge/Economy/advanced/05_Banking-Structure-NBFCs-and-Financial-Regulation.md",
        ],
    )


FACTS = [
    ("Scheduled-bank status", "A scheduled bank is included in the Second Schedule to the RBI Act subject to eligibility conditions; scheduled status is a legal classification rather than a guarantee against failure."),
    ("Commercial-bank function", "Commercial banks accept deposits, provide payment services and allocate credit, transforming short-maturity withdrawable liabilities into longer-maturity loans and investments."),
    ("Co-operative-bank perimeter", "Co-operative banks are member-based institutions governed by co-operative law while their banking functions also attract RBI and banking-law oversight."),
    ("NBFC boundary", "An NBFC is a company carrying specified financial activity without being a bank; RBI registration does not confer full bank-style demand-deposit, cheque-payment or DICGC privileges."),
    ("Systemic regulation", "Systemic regulation addresses institutional safety and financial-system stability through entry, governance, prudential, conduct, reporting and interconnectedness rules."),
    ("Multi-tier banking structure", "India combines public, private and foreign banks, Regional Rural Banks, co-operative banks, Small Finance Banks and Payments Banks to serve different ownership, reach, credit and payment functions."),
    ("Differentiated licensing", "Small Finance Banks undertake deposit mobilisation and lending, whereas Payments Banks focus on deposits and payments and cannot lend from their own balance sheets."),
    ("Rural place-based architecture", "RRBs, the Lead Bank Scheme and Service Area Approach linked branch expansion and formal rural credit with district and local-area planning."),
    ("Priority Sector Lending", "RBI's owner record states a 40 per cent ANBC or credit-equivalent target for most domestic banks, 18 per cent for agriculture including 10 per cent for small and marginal farmers, and 12 per cent for weaker sections, with higher overall targets for RRBs and SFBs under the latest cited direction."),
    ("PSL status caution", "PSL ratios, sub-targets and categories are periodically revised through RBI Master Directions, so a cited ratio must retain its effective direction and cannot be presented as a permanent constitutional or statutory number."),
    ("NBFC contagion risk", "The IL&FS default in 2018 and DHFL-related stress showed how wholesale funding, maturity mismatch and interconnectedness can transmit NBFC stress to mutual funds, banks and credit markets."),
    ("DICGC perimeter", "DICGC provides statutory insurance for eligible deposits in covered banks up to the owner's stated cap of five lakh rupees per depositor per bank, including principal and interest, but not shares, bonds, mutual funds or ordinary NBFC liabilities."),
    ("Prompt Corrective Action", "RBI's PCA framework uses risk-based thresholds and graduated restrictions for weak banks before disorderly failure; PCA is not liquidation or a deposit-insurance payout."),
    ("Public-sector banking reform", "PSB recapitalisation, the SBI associate-bank merger and appointment-governance reforms show that ownership, capital and structure matter alongside prudential supervision."),
    ("Regulatory architecture", "RBI regulates banking and NBFC activity, DICGC insures eligible bank deposits, SEBI regulates securities, IRDAI insurance, PFRDA pensions, and FSDC supports cross-regulatory coordination."),
    ("Bank asset-liability classification", "Loans, investments, cash and balances with RBI or other banks are typical commercial-bank assets, while customer deposits are liabilities."),
    ("Financial Inclusion Index", "RBI's FI-Index measures Access, Usage and Quality, so it is broader than counting branches or accounts opened."),
    ("Syndicated lending", "Syndicated lending uses multiple lenders under coordinated terms to share one exposure; risk sharing does not remove the need for appraisal and lender coordination."),
    ("Foreign banks and facility access", "Foreign banks may use branch or wholly owned subsidiary modes under RBI rules, and ordinary NBFCs do not automatically receive the same routine LAF access as scheduled banks."),
    ("Money, insurance and liability traps", "Withdrawing a demand deposit into cash changes the composition of money held rather than automatically creating fresh credit, while aviation hull insurance is distinct from airline legal liability under the Montreal Convention framework."),
]

TRAPS = [
    "Do not call every RBI-registered NBFC a bank without branches.",
    "Do not assume all co-operative banking activity is regulated only by states.",
    "Do not extend DICGC cover to bonds, mutual funds, insurance products or ordinary NBFC liabilities.",
    "Do not equate PCA with liquidation or deposit-insurance payout.",
    "Do not treat public ownership or a licence as proof of sound governance.",
    "Do not assume Payments Banks can lend from their own balance sheets.",
    "Do not present PSL ratios as timeless; retain the effective Master Direction.",
    "Do not infer routine LAF access for ordinary NBFCs.",
    "Do not confuse deposits, which are bank liabilities, with loans and investments, which are assets.",
    "Do not reduce the FI-Index to account or branch counts; it includes usage and quality.",
    "Do not generalise foreign-bank branch conditions to wholly owned subsidiaries or vice versa.",
    "Do not merge insurance cover with the separate legal-liability regime.",
]

SESSION_TITLES = [
    "Scheduled status and commercial-bank function",
    "Co-operative banking's dual perimeter",
    "What RBI registration does not make an NBFC",
    "Systemic regulation and financial stability",
    "India's multi-tier banking structure",
    "Differentiated licensing and rural credit planning",
    "Priority Sector Lending architecture",
    "Why PSL ratios need effective-date discipline",
    "IL&FS, DHFL and NBFC contagion",
    "DICGC depositor protection",
    "PCA and public-sector banking reform",
    "The cross-sector regulatory architecture",
    "Bank asset and liability classification",
    "FI-Index dimensions and syndicated lending",
    "Foreign banks, LAF and money-liability traps",
]

ANSWER_ROUTES = [
    "Compare institutions by legal powers, funding model, safety nets, payment access and supervisory intensity.",
    "Regulate according to function, leverage, liquidity fragility and systemic interconnectedness.",
    "Preserve useful institutional diversity while preventing regulatory arbitrage and moral hazard.",
]

PANELS = [
    panel("Banking legal perimeter", "classification-tree", ["SCHEDULED BANK -> Second Schedule status", "COMMERCIAL BANK -> deposits + payments + credit", "CO-OPERATIVE BANK -> member form + banking oversight", "NBFC -> financial company, not full bank powers"]),
    panel("Maturity transformation", "balance-sheet-flow", ["WITHDRAWABLE DEPOSITS", "-> pooled bank funding", "-> longer loans and investments", "RISK -> liquidity + credit + interest-rate mismatch"]),
    panel("Multi-tier architecture", "institution-map", ["PSB / PRIVATE / FOREIGN", "RRB / CO-OPERATIVE", "SMALL FINANCE BANK", "PAYMENTS BANK"]),
    panel("Differentiated-bank fork", "comparison-matrix", ["SFB -> deposits + lending", "PAYMENTS BANK -> deposits + payments", "PAYMENTS BANK -> no own-balance-sheet lending", "RULE -> similar licence family, different powers"]),
    panel("Rural-credit map", "place-based-rail", ["RRB -> rural intermediary", "LEAD BANK -> district coordination", "SERVICE AREA -> local responsibility", "LIMIT -> coverage does not ensure viable credit"]),
    panel("PSL target board", "target-matrix", ["MOST DOMESTIC BANKS -> 40 per cent overall", "AGRICULTURE -> 18 per cent", "SMALL/MARGINAL FARMERS -> 10 per cent", "WEAKER SECTIONS -> 12 per cent"]),
    panel("PSL status gate", "legal-status-band", ["TARGETS COME FROM RBI MASTER DIRECTIONS", "CATEGORIES AND SUB-TARGETS CAN CHANGE", "QUOTE THE EFFECTIVE DIRECTION", "DO NOT CALL A RATIO PERMANENT"]),
    panel("NBFC contagion chain", "contagion-flow", ["WHOLESALE FUNDING + MATURITY MISMATCH", "-> IL&FS / DHFL stress", "-> mutual funds + banks + markets", "LESSON -> non-bank stress can be systemic"]),
    panel("Depositor protection boundary", "safety-net-map", ["DICGC -> eligible bank deposits", "OWNER CAP -> Rs 5 lakh per depositor per bank", "OUT -> securities + insurance + ordinary NBFC claims", "PCA -> prevention, not payout"]),
    panel("Regulatory perimeter", "regulator-map", ["RBI -> banks + NBFCs + payments", "SEBI -> securities", "IRDAI / PFRDA -> insurance / pensions", "FSDC -> cross-sector coordination"]),
    panel("Balance-sheet and inclusion traps", "classification-board", ["LOANS / INVESTMENTS -> assets", "DEPOSITS -> liabilities", "FI-INDEX -> Access + Usage + Quality", "SYNDICATION -> shared exposure, not zero risk"]),
    panel("Financial-regulation answer spine", "answer-spine", ["CLASSIFY institution and powers", "MAP funding + leverage + safety net", "TRACE contagion and supervision", "BALANCE inclusion, diversity and stability"]),
]

PYQ_NOTE = (
    "The audited ledgers route objective demands on PSB governance, the Service "
    "Area Approach, bank assets, public-bank appointments, demand deposits, "
    "urban co-operative banks, Banks Board Bureau, NBFC/LAF distinctions, "
    "foreign banks, syndicated lending, FI-Index dimensions and NBFC deposit "
    "and payment privileges here. No Mains demand or answer letter is invented."
)

TOPIC_05 = common.topic(
    5,
    "Banking Structure, NBFCs and Financial Regulation",
    "05_Banking-Structure-NBFCs-and-Financial-Regulation",
    "05_Banking-Structure-NBFCs-and-Financial-Regulation_Learner-V2-Complete-Topic-Package.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish banks, differentiated banks and ordinary NBFCs.", [1, 3, 6]),
        (10, "Why does activity-based financial regulation matter?", [4, 14]),
        (15, "Explain India's multi-tier banking architecture and its inclusion rationale.", [5, 6, 7, 8]),
        (15, "Assess depositor protection and preventive supervision through DICGC and PCA.", [11, 12, 13]),
        (20, "How can India preserve specialised NBFC credit without regulatory arbitrage and systemic risk?", [3, 4, 10, 14, 18]),
        (20, "Compare banks, RRBs, co-operatives, SFBs, Payments Banks and NBFCs in the inclusion-stability framework.", [2, 5, 6, 7, 8, 10]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    ["scheduled bank", "NBFC", "Small Finance Banks", "Payments Banks", "Priority Sector Lending", "DICGC", "PCA", "FI-Index", "Access", "Usage", "Quality"],
    PYQ_NOTE,
    [],
    [
        "https://www.dicgc.org.in/ — retrieved 2026-09-03; the official landing page returned only the current split 'Fully Protected Accounts 97.60%' and 'Partly Protected Accounts 2.40%' without a visible reference date or denominator in the fetched text, so those percentages were logged but not used as a dated analytical claim.",
    ],
    "The DICGC landing page returned two protection-account percentages but no visible vintage or denominator in the fetched text. They are therefore not quoted as current evidence. Stable statutory deposit-insurance scope and the owner's stated cap are retained from the audited Markdown owner.",
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)
