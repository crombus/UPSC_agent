"""Authored Economy learner-v2 data for Topics 06-10."""

from __future__ import annotations

import generate_economy_common as common


STEMS = {
    6: "06_NPAs-Basel-Norms-Resolution-and-Financial-Inclusion",
    7: "07_Money-Market-Capital-Market-and-Financial-Instruments",
    8: "08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds",
    9: "09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators",
    10: "10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism",
}


def panel(
    topic_number: int,
    title: str,
    kind: str,
    lines: list[str],
) -> tuple[str, str, str, list[str]]:
    stem = STEMS[topic_number]
    return (
        title,
        kind,
        "\n".join(lines),
        [
            f"upsc-ai-kit/knowledge/Economy/basic/{stem}.md",
            f"upsc-ai-kit/knowledge/Economy/advanced/{stem}.md",
        ],
    )


FACTS_06 = [
    ("NPA recognition", "For a term loan, the standard RBI prudential test is interest or principal overdue for more than 90 days; the legal classification must not be replaced by a general idea of borrower weakness."),
    ("Gross and net NPA", "Gross NPA records the classified stressed exposure, while net NPA deducts provisions and specified adjustments to show the uncovered portion."),
    ("Provisioning and write-off", "Provisioning charges expected loss against income, whereas a write-off removes the loan from the active loan book without necessarily ending recovery rights or waiving the debt."),
    ("Risk-weighted capital", "Capital adequacy is measured against risk-weighted assets, so capital needs depend on asset risk rather than only on total balance-sheet size."),
    ("Basel and RBI minima", "The owner records Basel III global minima of CET1 4.5 per cent, Tier 1 6 per cent and total capital 8 per cent, while RBI's 1 April 2025 Master Circular records India-specific minima of CET1 5.5 per cent, Tier 1 7 per cent and total CRAR 9 per cent for its stated bank perimeter."),
    ("Capital Conservation Buffer", "The owner records a 2.5 per cent Capital Conservation Buffer met with CET1, taking the stated effective CET1 minimum to 8 per cent and effective total CRAR to 11.5 per cent; current use must retain the applicable RBI circular and bank perimeter."),
    ("Twin Balance Sheet diagnosis", "Economic Survey 2016-17 used the Twin Balance Sheet framing for simultaneous corporate over-leverage and bank stress; it is a dated diagnostic, not a statute or scheme."),
    ("Asset Quality Review", "RBI's Asset Quality Review pushed recognition of previously under-reported stress, which could worsen reported ratios initially while improving information and provisioning discipline."),
    ("SARFAESI perimeter", "The SARFAESI Act, 2002 is centred on enforcement of secured assets and is not a substitute for the entire insolvency system."),
    ("DRT and NCLT distinction", "Debt Recovery Tribunals are specialised recovery forums, whereas the NCLT-based IBC route addresses collective corporate insolvency and resolution."),
    ("IBC architecture", "The Insolvency and Bankruptcy Code, 2016 uses a creditor-in-committee process under the NCLT framework to pursue resolution or value-maximising exit rather than one lender's isolated recovery."),
    ("ARC and NARCL", "Asset Reconstruction Companies acquire stressed assets for recovery or resolution, while NARCL represents India's specialised bad-bank aggregation concept; transfer does not erase the underlying loss."),
    ("PCA and 4R", "Prompt Corrective Action is supervisory intervention for weak banks, while the 4R approach denotes Recognition, Resolution, Recapitalization and Reforms; neither is a deposit-insurance payout."),
    ("Inter-Creditor Agreement", "An Inter-Creditor Agreement coordinates lenders and reduces holdout problems in stressed resolution, but it is not itself a court or insolvency tribunal."),
    ("Interest Coverage Ratio", "Interest Coverage Ratio compares earnings with interest obligations and indicates debt-servicing capacity; it is not the legal definition of an NPA."),
    ("FI-Index dimensions", "RBI's annual Financial Inclusion Index uses Access, Usage and Quality and has no base year, so it cannot be reduced to a count of accounts opened."),
    ("PMJDY platform", "Pradhan Mantri Jan Dhan Yojana expanded account access and links to payments and transfers, but dormancy and low activity show why access does not automatically become effective inclusion."),
    ("SHG-Bank Linkage", "SHG-Bank Linkage connects commonly women-led savings groups to formal banking channels; a self-help group is not itself a bank."),
    ("WaterCredit", "WaterCredit is a microfinance-oriented model for water and sanitation access and illustrates targeted inclusion beyond plain account opening or general consumption credit."),
    ("Evergreening and forbearance", "Evergreening uses fresh finance to conceal unviable old dues, while temporary forbearance may bridge a shock; prolonged concealment creates zombie lending and misallocated credit."),
]

TRAPS_06 = [
    "Do not classify every weak borrower as an NPA without applying the prudential trigger.",
    "Do not equate gross NPA, net NPA, provisioning, write-off and waiver.",
    "Do not quote Basel or RBI ratios without the circular date and covered-bank perimeter.",
    "Do not equate secured recovery under SARFAESI with collective insolvency under IBC.",
    "Do not claim that transfer to an ARC or NARCL eliminates the economic loss.",
    "Do not call an Inter-Creditor Agreement a tribunal or statutory insolvency process.",
    "Do not use Interest Coverage Ratio as the legal NPA definition.",
    "Do not reduce financial inclusion to account opening without usage and quality.",
    "Do not treat every restructuring or temporary forbearance as fraud.",
    "Do not present the Twin Balance Sheet diagnosis as a current ratio or scheme.",
]

PANELS_06 = [
    panel(6, "Stress recognition rail", "causal-flow", ["WEAK CASH FLOW", "-> OVERDUE UNDER RBI TEST", "-> NPA RECOGNITION", "-> PROVISIONING + CAPITAL PRESSURE"]),
    panel(6, "Loan-accounting fork", "comparison-matrix", ["PROVISION -> expected loss charged to income", "WRITE-OFF -> removed from active loan book", "WAIVER -> liability legally relinquished", "RECOVERY RIGHTS may survive a write-off"]),
    panel(6, "Risk-weighted capital board", "ratio-map", ["BASEL GLOBAL -> CET1 4.5 | TIER 1 6 | TOTAL 8", "RBI INDIA -> CET1 5.5 | TIER 1 7 | CRAR 9", "CCB -> 2.5 CET1", "VINTAGE -> RBI Master Circular, 1 Apr 2025"]),
    panel(6, "Twin-balance-sheet loop", "feedback-loop", ["CORPORATE OVER-LEVERAGE", "-> WEAK DEBT SERVICE", "-> BANK NPAs + CAPITAL LOSS", "-> WEAKER FRESH CREDIT"]),
    panel(6, "Recovery-resolution ladder", "legal-route-ladder", ["SARFAESI -> secured-asset enforcement", "DRT -> specialised debt recovery", "IBC / NCLT -> collective insolvency", "ICA -> lender coordination, not a tribunal"]),
    panel(6, "Stressed-asset transfer", "vehicle-map", ["BANK BALANCE SHEET", "-> ARC / NARCL TRANSFER", "-> SPECIALISED RECOVERY OR SALE", "LOSS REMAINS -> valuation and buyer interest decide"]),
    panel(6, "Supervisory repair sequence", "reform-rail", ["AQR -> RECOGNITION", "PCA -> GRADUATED SUPERVISION", "RECAPITALISATION -> LOSS ABSORPTION", "4R -> RECOGNITION + RESOLUTION + RECAP + REFORMS"]),
    panel(6, "Stress indicators board", "classification-board", ["NPA -> prudential loan classification", "ICR -> earnings / interest-service indicator", "EVERGREENING -> concealed stress", "FORBEARANCE -> temporary relief, not permanent concealment"]),
    panel(6, "Inclusion quality triangle", "quality-triangle", ["ACCESS -> account or service availability", "USAGE -> active and suitable use", "QUALITY -> protection + grievance + suitability", "FI-INDEX -> all three; no base year"]),
    panel(6, "Inclusion delivery map", "institution-map", ["PMJDY -> transaction-account platform", "SHG-BANK LINKAGE -> group savings to formal bank", "BUSINESS CORRESPONDENT -> last-mile access", "WATERCREDIT -> targeted water/sanitation finance"]),
    panel(6, "Credit-cleanup trade-offs", "trade-off-board", ["EARLY RECOGNITION -> credibility / short-run ratio shock", "HIGHER CAPITAL -> resilience / lending constraint", "FAST RECOVERY -> discipline / viability risk", "DIGITAL ACCESS -> lower cost / exclusion and mis-selling risk"]),
    panel(6, "NPA answer spine", "answer-spine", ["DEFINE stress and classification", "ABSORB loss through provisions and capital", "CHOOSE recovery, resolution or transfer", "RESTORE governance and useful inclusion"]),
]

TOPIC_06 = common.topic(
    6,
    "NPAs, Basel Norms, Resolution and Financial Inclusion",
    STEMS[6],
    f"{STEMS[6]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_06,
    TRAPS_06,
    [
        (10, "Distinguish NPA recognition, provisioning, write-off and waiver.", [0, 1, 2]),
        (10, "Why is capital adequacy measured against risk-weighted assets?", [3, 4, 5]),
        (15, "Compare SARFAESI, DRT, IBC and Inter-Creditor Agreements.", [8, 9, 10, 13]),
        (15, "Explain why access, usage and quality must be separated in financial inclusion.", [15, 16, 17, 18]),
        (20, "Evaluate India's balance-sheet cleanup architecture from recognition to resolution.", [6, 7, 8, 10, 11, 12]),
        (20, "How can prudential stability and responsible financial inclusion reinforce each other?", [3, 5, 12, 15, 16, 19]),
    ],
    [
        "Term-loan overdue NPA recognition",
        "Provisioning, write-off and waiver",
        "Risk-weighted capital adequacy",
        "Basel global floor and RBI India overlay",
        "Capital Conservation Buffer and dated perimeter",
        "Twin Balance Sheet and Asset Quality Review",
        "SARFAESI secured recovery",
        "DRT and NCLT institutional separation",
        "IBC collective insolvency",
        "ARC and NARCL stressed-asset transfer",
        "PCA, 4R and Inter-Creditor Agreements",
        "Interest Coverage Ratio",
        "FI-Index: Access, Usage and Quality",
        "PMJDY and SHG-Bank Linkage",
        "WaterCredit, evergreening and forbearance",
    ],
    [
        "Sequence recognition, loss absorption, resolution, recapitalisation and governance repair.",
        "Compare legal tools by secured claim, collective action, tribunal and value-preservation purpose.",
        "Judge inclusion by active, suitable and protected use rather than headline account counts.",
    ],
    PANELS_06,
    ["90 days", "risk-weighted assets", "CET1", "CRAR", "Capital Conservation Buffer", "SARFAESI", "IBC", "NARCL", "Access", "Usage", "Quality"],
    "Audited ledgers route objective demands on capital adequacy, Inter-Creditor Agreements, Interest Coverage Ratio, WaterCredit and SHG-Bank Linkage here. No answer letter is inferred.",
    [],
    [
        "https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12815 — retrieved 2026-09-03; the official page substantively identifies RBI/2025-26/08 dated 1 April 2025, its scheduled-commercial-bank perimeter and the consolidated Basel III Capital Regulations circular. Ratio detail remains tied to the circular text and repository owner.",
        "https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=51984 — retrieved 2026-09-03; despite the owner label, the live page returned a dated 2021 Treasury-Bill auction rather than FI-Index text, so no FI-Index score or current NPA statistic was taken from it.",
    ],
    "The live RBI Basel page confirmed the circular identity, date and covered-bank perimeter. The attempted FI-Index URL resolved to an unrelated 2021 Treasury-Bill release, so Access-Usage-Quality and all prudential ratios remain sourced to the audited Markdown owner with their stated status.",
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)


FACTS_07 = [
    ("Money-market boundary", "The money market supplies short-term funds and liquidity instruments; classification depends on tenor and function rather than on whether the issuer is public or private."),
    ("Capital-market boundary", "The capital market supplies medium- and long-term debt and equity finance, so it includes long-term bonds as well as shares."),
    ("Primary market", "Primary issuance transfers fresh funds to the issuer through a new security issue."),
    ("Secondary market", "Secondary trading normally transfers an existing security between investors and provides liquidity and price discovery rather than fresh money to the original issuer."),
    ("Treasury Bills", "Treasury Bills are short-term Government of India borrowing instruments auctioned by RBI on the government's behalf, while dated government securities serve longer maturities."),
    ("Call and term money", "Call money is unsecured overnight inter-institutional borrowing, while notice and term money extend the unsecured tenor beyond overnight under the applicable market definitions."),
    ("Repo and TREPS", "Repo is collateralised borrowing against securities, and TREPS is the tri-party repo platform that replaced the older CBLO mechanism; collateral and platform design distinguish both from call money."),
    ("Commercial Paper", "Commercial Paper is unsecured short-term borrowing by eligible corporates and therefore carries confidence and rollover risk."),
    ("Certificate of Deposit", "Certificates of Deposit are short-term negotiable instruments issued by eligible banks or institutions to manage funding and liquidity."),
    ("RBI and SEBI perimeter", "RBI oversees money markets, government securities and payment or settlement components within its mandate, while SEBI regulates securities issuance, exchanges, intermediaries and investor protection."),
    ("NDS-OM access", "RBI's Access Criteria for NDS-OM Directions, 2025 define NDS-OM as the authorised electronic trading platform for government securities and distinguish direct, indirect and Stock Broker Connect access."),
    ("CCIL and depositories", "CCIL clears and settles important government-securities, money and foreign-exchange transactions, while depositories hold eligible securities in dematerialised ownership records."),
    ("Liquidity dimensions", "Market liquidity has depth, breadth, immediacy and resilience dimensions; high volume alone does not prove deep, robust liquidity."),
    ("Yield-curve information", "A yield curve embeds expected rates, term premia, liquidity and credit conditions rather than a single policy-rate signal."),
    ("Credit ratings", "A regulated credit rating is an opinion on credit risk for an issuer or instrument and does not guarantee repayment."),
    ("Investor and venue distinctions", "Insurance, pension and retail investors may access government or corporate debt under specified rules, so investor class, instrument and venue must be kept separate."),
    ("Financial-instrument test", "A financial instrument creates a financial asset for one party and a liability or equity claim for another; a motor vehicle remains a physical asset even when financed or pledged."),
    ("Non-financial debt", "Non-financial debt refers to liabilities of general government, non-financial corporations and households rather than the liabilities of financial corporations."),
    ("RTGS and NEFT", "RTGS settles transactions individually in real time and gross terms, while NEFT uses batch settlement; the owner records both as operating continuously and inward transfers as free."),
    ("TReDS and IFSC", "TReDS is an RBI-regulated MSME receivables-discounting platform, while GIFT City IFSC is a separate international financial jurisdiction regulated by IFSCA across banking, capital markets, insurance and fund management."),
]

TRAPS_07 = [
    "Do not classify every government security as a money-market instrument.",
    "Do not say that secondary trading normally gives fresh funds to the issuer.",
    "Do not merge call money, repo, TREPS and the former CBLO mechanism.",
    "Do not call Commercial Paper secured or a Certificate of Deposit a corporate share.",
    "Do not equate liquidity, safety, return and credit quality.",
    "Do not treat a credit rating as repayment insurance.",
    "Do not call a pledged physical asset a financial instrument.",
    "Do not merge RTGS real-time gross settlement with NEFT batch settlement.",
    "Do not call TReDS a stock exchange or credit-rating agency.",
    "Do not apply the ordinary RBI-SEBI division unchanged inside the IFSCA-regulated IFSC.",
]

PANELS_07 = [
    panel(7, "Market maturity fork", "comparison-matrix", ["MONEY MARKET -> short-term funds + liquidity", "CAPITAL MARKET -> medium/long debt + equity", "CLASSIFY BY -> tenor + claim + function", "NOT BY -> issuer name alone"]),
    panel(7, "Issue-to-trade rail", "market-flow", ["SAVER FUNDS", "-> PRIMARY ISSUE -> fresh issuer finance", "-> SECONDARY TRADE -> investor liquidity", "-> PRICE DISCOVERY -> future financing signal"]),
    panel(7, "Government borrowing ladder", "tenor-ladder", ["TREASURY BILL -> short tenor", "DATED G-SEC -> longer maturity", "RBI -> auction and market architecture", "ROLLOVER RISK persists at short tenor"]),
    panel(7, "Overnight market map", "segment-map", ["CALL MONEY -> unsecured overnight", "REPO -> collateralised bilateral funding", "TREPS -> tri-party collateral platform", "CBLO -> older mechanism replaced by TREPS"]),
    panel(7, "Corporate and bank funding", "issuer-map", ["CORPORATE -> Commercial Paper", "BANK / ELIGIBLE INSTITUTION -> Certificate of Deposit", "CP -> unsecured + rollover-sensitive", "CD -> negotiable short-term liability"]),
    panel(7, "Regulatory division", "regulator-map", ["RBI -> money market + G-Secs + payment rails", "SEBI -> securities issuance + exchanges", "IFSCA -> unified IFSC perimeter", "KEEP instrument, venue and regulator distinct"]),
    panel(7, "G-Sec trading infrastructure", "infrastructure-chain", ["NDS-OM -> electronic G-Sec trading", "CCIL -> clearing and settlement", "SGL / DEMAT -> ownership records", "DIRECT / INDIRECT / BROKER CONNECT -> access modes"]),
    panel(7, "Liquidity quality board", "quality-matrix", ["DEPTH -> absorb order size", "BREADTH -> participant and instrument range", "IMMEDIACY -> transact quickly", "RESILIENCE -> recover after shocks"]),
    panel(7, "Risk and return dimensions", "dimension-board", ["MATURITY is not LIQUIDITY", "LIQUIDITY is not SAFETY", "RATING is not GUARANTEE", "YIELD reflects expectations + premia + risk"]),
    panel(7, "Payment-system fork", "comparison-matrix", ["RTGS -> real time + gross + transaction-wise", "NEFT -> batch settlement", "BOTH -> owner records continuous operation", "PAYMENT RAIL is not a capital-market security"]),
    panel(7, "Receivables and physical assets", "classification-board", ["TReDS -> accepted MSME receivable discounting", "ETF / SWAP -> financial instruments", "MOTOR VEHICLE -> physical asset", "COLLATERAL status does not change asset class"]),
    panel(7, "Financial-market answer spine", "answer-spine", ["CLASSIFY tenor, issuer and claim", "MAP primary versus secondary function", "TRACE trading, clearing and settlement", "BALANCE depth with disclosure and resilience"]),
]

TOPIC_07 = common.topic(
    7,
    "Money Market, Capital Market and Financial Instruments",
    STEMS[7],
    f"{STEMS[7]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_07,
    TRAPS_07,
    [
        (10, "Distinguish money markets, capital markets, primary markets and secondary markets.", [0, 1, 2, 3]),
        (10, "Compare call money, repo and TREPS.", [5, 6]),
        (15, "Explain the issuer and risk logic of T-Bills, Commercial Paper and Certificates of Deposit.", [4, 7, 8]),
        (15, "What infrastructure makes the government-securities market liquid and safe?", [10, 11, 12]),
        (20, "Compare India's short-term and long-term financial markets through maturity, liquidity, risk and regulation.", [0, 1, 4, 6, 9, 13]),
        (20, "Evaluate whether financial deepening requires more than higher trading volume.", [11, 12, 13, 14, 15, 19]),
    ],
    [
        "Money-market and capital-market boundaries",
        "Primary market and fresh issuer finance",
        "Secondary market liquidity and price discovery",
        "Treasury Bills and dated government securities",
        "Call, notice and term money",
        "Repo, TREPS, CBLO and Commercial Paper",
        "Certificates of Deposit",
        "RBI-SEBI functional regulation",
        "NDS-OM access architecture",
        "CCIL, depositories and settlement",
        "Liquidity dimensions and yield curves",
        "Credit ratings",
        "Investor classes and trading venues",
        "Financial assets and non-financial debt",
        "RTGS, NEFT, TReDS and the IFSC",
    ],
    [
        "Classify each market by tenor, claim, issuer, collateral, tradability and regulator.",
        "Trace how issuance, trading, clearing, settlement and custody convert savings into finance.",
        "Balance market depth with rollover risk, disclosure, suitability and systemic resilience.",
    ],
    PANELS_07,
    ["money market", "capital market", "Treasury Bills", "Commercial Paper", "Certificate of Deposit", "TREPS", "NDS-OM", "CCIL", "RTGS", "NEFT", "TReDS", "IFSCA"],
    "Audited ledgers route objective demands on CBLO or TREPS, corporate-bond and G-Sec investors, financial-instrument classification, sovereign bonds, RTGS and NEFT, T-Bills, non-financial debt, bond yields, NDS-OM, CDSL and credit-rating agencies here. No answer letter is inferred.",
    [],
    [
        "https://www.rbi.org.in/Scripts/BS_ViewMMO.aspx — retrieved 2026-09-03; the official live page substantively displayed dated 2-3 September 2026 overnight money-market segments and separately labelled Call Money, Triparty Repo, Market Repo and Repo in Corporate Bonds. Volumes and rates were not carried into the stable fact anchors.",
        "https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13376 — retrieved 2026-09-03; the official Direction is dated 7 February 2025, updated 27 April 2026, defines NDS-OM and direct, indirect and Stock Broker Connect access, and states eligible direct-access categories and settlement requirements.",
    ],
    "The live RBI pages confirmed current market-segment labels and the dated NDS-OM access framework. Volumes, rates and auction results were intentionally omitted from stable anchors because they are date-specific operational data.",
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)


FACTS_08 = [
    ("Bond claim", "A bond is a creditor claim with contractual interest and principal obligations, and bondholders generally rank ahead of equity shareholders in repayment."),
    ("Equity claim", "Equity is an ownership and residual-return claim that absorbs losses after creditors and may carry voting rights."),
    ("Coupon and yield", "Coupon is the stated contractual cash-flow rate, while yield depends on market price, cash flows and maturity; they need not remain equal after issuance."),
    ("Price-yield relationship", "For a fixed cash-flow bond, market price and comparable yield generally move inversely."),
    ("Duration and convexity", "Duration and convexity describe bond-price sensitivity to yield changes beyond the simple inverse-direction rule."),
    ("Credit spread", "A credit spread over a benchmark reflects default, liquidity and other risk-premium components rather than contractual coupon alone."),
    ("Futures", "A standardised futures contract creates symmetric obligations for buyer and seller and is supported by margining and clearing."),
    ("Options", "An option gives the buyer a right but not an obligation, while the writer bears a contingent obligation; value depends on the underlying, strike, time, volatility and rates."),
    ("Swaps", "A swap exchanges cash-flow streams linked to interest rates, currencies or other variables and may be centrally or bilaterally risk-managed according to the market segment."),
    ("Hedging and speculation", "Hedging reduces a pre-existing exposure, while speculation creates or enlarges exposure for expected profit; the same derivative form can serve either purpose."),
    ("Clearing and leverage", "Margins, clearing corporations and default waterfalls reduce settlement and counterparty risk but do not remove leverage, basis risk or mark-to-market losses."),
    ("Mutual funds and ETFs", "A mutual fund is a SEBI-regulated pooled vehicle, while an ETF unit trades intraday on an exchange and may deviate from its net asset value."),
    ("Alternative Investment Funds", "An AIF is a privately pooled vehicle under SEBI's category framework; venture-capital and hedge funds can fall within AIF categories, whereas direct stocks and bonds are not AIFs."),
    ("REIT and InvIT", "REITs and InvITs are SEBI-regulated pooled vehicles linked respectively to real-estate and infrastructure cash flows and are distinct from ordinary mutual funds and AIFs."),
    ("Participatory Notes", "Participatory Notes are offshore instruments issued by registered foreign portfolio investors to overseas investors and are not the same as direct domestic shareholding."),
    ("Inflation-Indexed Bonds", "Inflation-Indexed Bonds link specified payouts or principal to inflation to protect real purchasing power, while market-price and liquidity risks remain."),
    ("Convertible bonds", "Convertible bonds begin as debt and may convert into equity under specified contractual terms."),
    ("Beta", "Beta measures a stock's volatility relative to the broader market and is a market-risk indicator rather than a guarantee of return."),
    ("Tokenisation and sustainability bonds", "Real-world-asset tokenisation changes access and transfer mechanics but not the underlying legal and economic risk, while a sustainability bond finances eligible environmental and social projects rather than only green projects."),
    ("Investor protection and liquidity mismatch", "SEBI's disclosure, adviser, margin, settlement and grievance architecture reduces conduct risk, but open-ended or pooled structures can still face liquidity mismatch, valuation opacity and mis-selling."),
]

TRAPS_08 = [
    "Do not treat equity dividends as contractual in the same way as bond interest.",
    "Do not say bond prices generally rise when comparable market yields rise.",
    "Do not infer that every derivative position is a hedge.",
    "Do not merge futures, options and swaps into one obligation structure.",
    "Do not treat exchange clearing as elimination of leverage or market risk.",
    "Do not call an ETF unit the same legal claim as one constituent stock.",
    "Do not treat direct stocks and bonds as Alternative Investment Funds.",
    "Do not merge mutual funds, AIFs, REITs and InvITs.",
    "Do not present beta as a promised return or complete risk measure.",
    "Do not equate tokenisation with assured liquidity, title or regulatory protection.",
]

PANELS_08 = [
    panel(8, "Claim-priority waterfall", "priority-waterfall", ["ISSUER CASH FLOW", "-> CONTRACTUAL DEBT SERVICE", "-> BONDHOLDER PRIORITY", "-> EQUITY RESIDUAL RETURN"]),
    panel(8, "Bond pricing board", "pricing-map", ["COUPON -> contractual rate", "YIELD -> market-price-based return", "YIELD RISE -> fixed bond price generally falls", "DURATION + CONVEXITY -> sensitivity detail"]),
    panel(8, "Credit-risk decomposition", "spread-map", ["BENCHMARK YIELD", "+ DEFAULT PREMIUM", "+ LIQUIDITY PREMIUM", "+ OTHER RISK PREMIA -> CREDIT SPREAD"]),
    panel(8, "Derivative obligation fork", "comparison-matrix", ["FUTURE -> symmetric buyer/seller obligations", "OPTION BUYER -> right, not obligation", "OPTION WRITER -> contingent obligation", "SWAP -> exchange cash-flow streams"]),
    panel(8, "Purpose test", "decision-tree", ["PRE-EXISTING EXPOSURE?", "YES -> hedge size and tenor", "NO -> speculative exposure", "SAME CONTRACT can reduce or enlarge risk"]),
    panel(8, "Clearing and leverage rail", "risk-control-flow", ["POSITION", "-> MARGIN + MARK-TO-MARKET", "-> CLEARING CORPORATION", "RESIDUAL -> basis, liquidity and leverage risk"]),
    panel(8, "Pooled-vehicle map", "vehicle-matrix", ["MUTUAL FUND -> pooled mandate + NAV", "ETF -> exchange-traded fund unit", "AIF -> privately pooled category framework", "REIT / InvIT -> property / infrastructure cash flows"]),
    panel(8, "Access instruments board", "classification-board", ["P-NOTE -> offshore instrument via registered FPI", "IIB -> inflation-linked payout or principal", "CONVERTIBLE -> debt with equity conversion terms", "BETA -> relative market volatility"]),
    panel(8, "Tokenisation boundary", "legal-tech-map", ["UNDERLYING REAL-WORLD ASSET", "-> DIGITAL TOKEN REPRESENTATION", "ACCESS may become fractional", "TITLE + CUSTODY + DISCLOSURE remain decisive"]),
    panel(8, "Use-of-proceeds taxonomy", "taxonomy-tree", ["GREEN BOND -> environmental projects", "SOCIAL BOND -> social projects", "SUSTAINABILITY BOND -> both", "LABEL does not eliminate credit risk"]),
    panel(8, "Investor-protection stack", "institution-stack", ["DISCLOSURE + PRODUCT LABELLING", "REGISTERED ADVISERS + INTERMEDIARIES", "MARGIN + SETTLEMENT + GRIEVANCE", "LIMIT -> business and market loss remain"]),
    panel(8, "Securities answer spine", "answer-spine", ["CLASSIFY claim and cash-flow priority", "MAP liquidity promise and leverage", "TRACE regulator and settlement", "MATCH instrument to investor exposure"]),
]

PYQ_SOLUTIONS_08: list[tuple[str, str, str, str, str]] = []

TOPIC_08 = common.topic(
    8,
    "Securities, Bonds, Equity, Derivatives and Investment Funds",
    STEMS[8],
    f"{STEMS[8]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_08,
    TRAPS_08,
    [
        (10, "Distinguish bondholder and equity-holder claims.", [0, 1, 2]),
        (10, "Why do bond prices and yields generally move inversely?", [2, 3, 4]),
        (15, "Compare futures, options and swaps as risk-transfer contracts.", [6, 7, 8, 10]),
        (15, "Compare mutual funds, ETFs, AIFs, REITs and InvITs.", [11, 12, 13]),
        (20, "Evaluate the hedging benefit and leverage risk of derivatives.", [6, 7, 8, 9, 10, 19]),
        (20, "How should India widen household market participation without encouraging unsuitable risk?", [11, 12, 13, 14, 18, 19]),
    ],
    [
        "Bondholder and equity-holder claims",
        "Coupon and market yield",
        "Bond price-yield movement",
        "Duration and convexity",
        "Credit spreads",
        "Futures and options obligations",
        "Swaps and cash-flow exchange",
        "Hedging versus speculation",
        "Margins, clearing and leverage",
        "Mutual funds and ETFs",
        "AIFs, REITs and InvITs",
        "Participatory Notes and offshore access",
        "Inflation-Indexed Bonds",
        "Convertible bonds and beta",
        "Tokenisation, sustainability bonds and investor protection",
    ],
    [
        "Classify each product by legal claim, cash flow, priority, liquidity and leverage.",
        "Distinguish the contract's form from the user's hedging, speculative or arbitrage purpose.",
        "Balance wider access with suitability, disclosure, margining and liquidity-risk controls.",
    ],
    PANELS_08,
    ["bondholders", "coupon", "yield", "duration", "futures", "options", "swaps", "ETF", "AIF", "REIT", "InvIT", "Participatory Notes", "beta", "tokenisation", "sustainability bond"],
    "Audited ledgers route objective demands on Participatory Notes, Inflation-Indexed Bonds, convertible bonds, InvITs, beta, AIF classification, bondholder priority, equity derivatives and real-world-asset tokenisation here. No answer letter is inferred.",
    PYQ_SOLUTIONS_08,
    [
        "https://www.sebi.gov.in/legal/circulars/nov-2025/reclassification-of-real-estate-investment-trusts-reits-as-equity-related-instruments-for-facilitating-enhanced-participation-by-mutual-funds-and-specialized-investment-funds-sifs-_98031.html — retrieved 2026-09-03; the live official page returned only Circular No. HO/24/13/12(1)2025-IMD-POD-2/I/157/2025 without substantive operative text, so no effective-date, classification or investment-limit claim was imported.",
    ],
    "The attempted SEBI circular page returned only a circular identifier. Stable instrument definitions, legal-claim distinctions and PYQ concepts therefore remain bounded to the repository owners and audited routing ledgers.",
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)


FACTS_09 = [
    ("Annual Financial Statement", "Article 112 provides for the Union Annual Financial Statement, and the budget procedure keeps charged expenditure distinct from expenditure submitted to vote."),
    ("Revenue receipts", "Revenue receipts neither create a liability nor reduce a financial asset and include tax and non-tax revenue within the stated budget perimeter."),
    ("Capital receipts", "Capital receipts create liabilities or reduce financial assets; borrowings create liabilities, while recovery of loans and disinvestment are non-debt capital receipts."),
    ("Revenue and capital expenditure", "Revenue expenditure generally supports current services and transfers, whereas capital expenditure creates assets or reduces liabilities; classification is accounting-based rather than a moral label."),
    ("Revenue deficit", "Revenue deficit equals revenue expenditure minus revenue receipts."),
    ("Fiscal deficit", "Fiscal deficit equals total expenditure minus non-debt receipts and broadly indicates the period's borrowing requirement rather than the stock of public debt."),
    ("Primary deficit", "Primary deficit equals fiscal deficit minus interest payments and isolates the current fiscal gap after removing the burden of past-debt interest."),
    ("Effective revenue deficit", "Effective revenue deficit equals revenue deficit minus grants-in-aid to states or Union Territories for creation of capital assets; it reclassifies the transfer but does not prove the asset was well used."),
    ("Effective capital expenditure", "Effective capital expenditure adds grants for capital-asset creation to the Centre's own capital expenditure."),
    ("BE, RE and Actuals", "Budget Estimates are policy authorisations or projections, Revised Estimates update the year's expected outcome, and Actuals record realised accounts; the three vintages are not interchangeable."),
    ("FRBM framework", "The FRBM Act, 2003 and its annual fiscal statements impose medium-term targets, macro disclosure and deviation reporting rather than a guarantee that every announced path will be met."),
    ("Macro Economic Framework Statement", "The Macro Economic Framework Statement supplies the growth, inflation and macro assumptions needed to interpret Budget numbers."),
    ("Debt anchor and glide path", "The N.K. Singh-led FRBM Review Committee advanced a debt-anchor and operational glide-path logic; its recommendations are advisory and not self-executing."),
    ("Deficit and debt coverage", "A fiscal deficit is a flow for a specified government and period, while debt is a stock; the Union Budget does not by itself capture states, local bodies and every public-sector liability."),
    ("Crowding-out channel", "Government borrowing may raise interest rates or absorb financial savings and crowd out private credit, but the effect depends on slack, liquidity, household savings and monetary conditions."),
    ("Crowding-in through capex", "Public capital expenditure can crowd in private investment when it removes infrastructure bottlenecks and raises expected demand, subject to project selection and execution."),
    ("Off-budget and contingent risk", "Guarantees, extra-budgetary borrowing and delayed payments can understate genuine public-sector risk in the headline fiscal deficit; several historical items have since been moved on-budget."),
    ("Fiscal Health Index", "NITI Aayog's Fiscal Health Index compares state fiscal performance across dimensions including revenue mobilisation, expenditure quality, prudence and debt sustainability rather than one ratio alone."),
    ("Black money and household savings", "Undisclosed income narrows the declared tax base, while household financial savings influence how much public borrowing can be absorbed domestically without intensifying financing pressure."),
    ("Union Budget 2026-27 vintage", "The owner records Union Budget 2026-27 Budget Estimates of a 4.3 per cent fiscal deficit-to-GDP ratio and 12.22 lakh crore rupees of capital expenditure, alongside a 4.4 per cent fiscal-deficit ratio for 2025-26 Revised Estimates; these are dated BE or RE figures, not Actuals."),
]

TRAPS_09 = [
    "Do not classify all capital receipts as resources without future fiscal cost.",
    "Do not equate zero revenue deficit with zero fiscal deficit.",
    "Do not call fiscal deficit the stock of total public debt.",
    "Do not subtract borrowings as non-debt receipts in the fiscal-deficit identity.",
    "Do not merge primary deficit with fiscal deficit or interest payments.",
    "Do not treat effective revenue deficit as proof of completed asset creation.",
    "Do not equate Budget Estimates, Revised Estimates and Actuals.",
    "Do not infer the whole general-government risk from the Union headline alone.",
    "Do not assume every public capex programme automatically crowds in investment.",
    "Do not quote Budget 2026-27 figures without the BE or RE vintage.",
]

PANELS_09 = [
    panel(9, "Budget receipt fork", "classification-tree", ["REVENUE RECEIPT -> no liability / no asset reduction", "CAPITAL RECEIPT -> liability or asset reduction", "BORROWING -> debt capital receipt", "DISINVESTMENT / LOAN RECOVERY -> non-debt capital receipt"]),
    panel(9, "Expenditure classification", "comparison-matrix", ["REVENUE EXPENDITURE -> current service / transfer", "CAPITAL EXPENDITURE -> asset or liability reduction", "ACCOUNTING CLASS is not a moral verdict", "QUALITY depends on design and outcomes"]),
    panel(9, "Deficit identity board", "formula-board", ["REVENUE DEFICIT = RE - RR", "FISCAL DEFICIT = TOTAL EXPENDITURE - NON-DEBT RECEIPTS", "PRIMARY DEFICIT = FD - INTEREST", "KEEP flow, period and government perimeter"]),
    panel(9, "Effective measures", "formula-board", ["ERD = REVENUE DEFICIT - CAPITAL-ASSET GRANTS", "EFFECTIVE CAPEX = CENTRE CAPEX + CAPITAL-ASSET GRANTS", "TRANSFER accounting is refined", "OUTCOME quality still needs verification"]),
    panel(9, "Estimate-vintage rail", "timeline-strip", ["BUDGET ESTIMATE -> authorisation / projection", "REVISED ESTIMATE -> updated in-year expectation", "ACTUAL -> realised account", "NEVER compare without labels"]),
    panel(9, "Constitutional document stack", "document-stack", ["ARTICLE 112 -> Annual Financial Statement", "FRBM ACT -> medium-term fiscal discipline", "MEFS -> macro assumptions", "PARLIAMENT + CAG -> authorisation and scrutiny"]),
    panel(9, "Debt-dynamics chain", "causal-flow", ["PRIMARY BALANCE + INTEREST", "-> FISCAL DEFICIT", "-> DEBT STOCK", "-> FUTURE INTEREST FEEDBACK"]),
    panel(9, "Crowding fork", "decision-tree", ["BORROWING DURING TIGHT FINANCE", "-> rates / savings pressure -> crowding out", "CAPEX REMOVES BOTTLENECKS", "-> productivity / demand -> crowding in"]),
    panel(9, "Hidden-risk perimeter", "risk-map", ["HEADLINE DEFICIT", "+ GUARANTEES", "+ EXTRA-BUDGETARY BORROWING", "+ DELAYED PAYMENTS -> wider fiscal risk"]),
    panel(9, "State fiscal quality", "dimension-board", ["OWN-REVENUE MOBILISATION", "EXPENDITURE QUALITY", "FISCAL PRUDENCE", "DEBT SUSTAINABILITY"]),
    panel(9, "Budget 2026-27 status card", "vintage-card", ["2026-27 BE -> fiscal deficit 4.3% GDP", "2026-27 BE -> capex Rs 12.22 lakh crore", "2025-26 RE -> fiscal deficit 4.4% GDP", "STATUS -> BE / RE, not Actuals"]),
    panel(9, "Fiscal-policy answer spine", "answer-spine", ["DEFINE identities and coverage", "CHECK BE / RE / Actual vintage", "ASSESS composition and multiplier", "CONCLUDE on debt path and transparency"]),
]

PYQ_SOLUTIONS_09 = [
    common.make_pyq_solution(FACTS_09, "2019", "GS-III", "Clarify why public expenditure management remains a challenge in post-liberalisation budget making.", "Verified routed Mains demand; original model solution, not an official answer.", [3, 9, 16, 17]),
    common.make_pyq_solution(FACTS_09, "2021", "GS-III", "Distinguish the Capital Budget and Revenue Budget and explain their components.", "Verified routed Mains demand; original model solution, not an official answer.", [1, 2, 3, 8]),
    common.make_pyq_solution(FACTS_09, "2025", "GS-III", "Explain the Fiscal Health Index as a tool for assessing state fiscal performance.", "Verified routed Mains demand; original model solution, not an official answer.", [13, 17, 18]),
]

TOPIC_09 = common.topic(
    9,
    "Union Budget, Fiscal Policy and Deficit Indicators",
    STEMS[9],
    f"{STEMS[9]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_09,
    TRAPS_09,
    [
        (10, "Distinguish revenue receipts, capital receipts and borrowings.", [1, 2]),
        (10, "Calculate and interpret revenue, fiscal and primary deficits.", [4, 5, 6]),
        (15, "Explain effective revenue deficit and effective capital expenditure.", [7, 8]),
        (15, "Why must Budget Estimates, Revised Estimates and Actuals be separated?", [9, 11, 19]),
        (20, "Evaluate rule-based fiscal consolidation with countercyclical flexibility.", [10, 12, 14, 15, 16]),
        (20, "Judge India's fiscal stance through composition, transparency and debt sustainability.", [3, 13, 15, 16, 17, 18]),
    ],
    [
        "Annual Financial Statement and revenue receipts",
        "Capital receipts and non-debt receipts",
        "Revenue and capital expenditure",
        "Revenue-deficit identity",
        "Fiscal-deficit identity",
        "Primary deficit and effective revenue deficit",
        "Effective capital expenditure",
        "Budget Estimates, Revised Estimates and Actuals",
        "FRBM framework",
        "Macro Economic Framework Statement",
        "Debt anchor, deficit flow and debt stock",
        "Crowding-out channel",
        "Crowding in through public capex",
        "Off-budget risk and Fiscal Health Index",
        "Black money, household savings and Budget vintage",
    ],
    [
        "State every deficit formula, period, government perimeter and estimate vintage before inference.",
        "Judge borrowing by expenditure composition, multiplier, financing conditions and debt feedback.",
        "Combine fiscal rules with transparent escape clauses, contingent-liability disclosure and outcome scrutiny.",
    ],
    PANELS_09,
    ["Article 112", "revenue deficit", "fiscal deficit", "primary deficit", "effective revenue deficit", "effective capital expenditure", "Budget Estimates", "Revised Estimates", "FRBM", "Fiscal Health Index", "crowding-out"],
    "Audited ledgers route Mains demands on public expenditure management, Capital versus Revenue Budget and the Fiscal Health Index, plus objective demands on Article 112, capital receipts, deficit computation, recession policy, opportunity cost, household savings and crowding out. Objective answer letters are not inferred.",
    PYQ_SOLUTIONS_09,
    [
        "https://www.indiabudget.gov.in/doc/frbm1.pdf — attempted 2026-09-03; the official PDF returned HTTP 403 to the live fetcher, so no number was extracted from the live attempt and the repository owner's explicitly dated Budget 2026-27 BE and 2025-26 RE figures were retained unchanged.",
        "https://www.indiabudget.gov.in/ — attempted 2026-09-03; the official landing page also returned HTTP 403 to the live fetcher.",
    ],
    "Both live India Budget attempts were blocked with HTTP 403. The package therefore preserves the repository owner's figures only with their exact Union Budget 2026-27 BE and 2025-26 RE labels and does not upgrade them to Actuals.",
)


FACTS_10 = [
    ("Direct and indirect taxes", "Direct taxes impose legal incidence on income, profit or wealth-related bases, while indirect taxes apply to transactions or consumption and may be shifted through prices."),
    ("Progressivity", "Progressive, proportional and regressive describe how the burden changes relative to income, tax base or ability to pay; statutory rate alone does not establish incidence."),
    ("GST destination principle", "GST is a destination-based value-added tax on supply, so final consumption jurisdiction is central to revenue assignment."),
    ("Input tax credit", "Input tax credit reduces cascading only when legal eligibility, invoice and compliance conditions are satisfied."),
    ("Subsumed Union taxes", "The owner lists Central Excise Duty on covered items, Service Tax, Additional Excise Duties, CVD, SAD and relevant central cesses or surcharges on supply among Union levies subsumed into GST."),
    ("Subsumed State taxes", "The owner lists State VAT or Sales Tax, Central Sales Tax as collected, Purchase Tax, specified Entertainment Tax, Octroi or Entry Tax, Luxury Tax and taxes on lotteries, betting and gambling among State levies subsumed into GST."),
    ("GST exclusions", "Basic customs duty, stamp duty, property tax, electricity duty and state excise on alcohol for human consumption remain outside GST, while the owner records specified petroleum products as not yet brought under GST at its stated vintage."),
    ("GST Council voting", "Article 279A gives the Centre one-third of weighted GST Council votes and states together two-thirds, with at least three-fourths of weighted votes required for a decision."),
    ("IGST settlement", "The IGST architecture supports inter-state supply taxation and settlement toward the destination jurisdiction; it must not be described as simple origin-based revenue retention."),
    ("GST compensation", "The GST (Compensation to States) Act, 2017 created a five-year 2017-2022 transition guarantee based on 14 per cent annual protected revenue growth over the 2015-16 base; it was not a permanent constitutional entitlement."),
    ("Finance Commission role", "The Finance Commission is a constitutional body recommending tax devolution and grants and does not set GST rates."),
    ("Vertical and horizontal imbalance", "Vertical devolution addresses the Union-state resource gap, while horizontal distribution allocates the states' share among states using capacity, need and incentive criteria."),
    ("Fifteenth Finance Commission", "The owner records a 41 per cent vertical devolution share for the Fifteenth Finance Commission and criteria including income distance, population, area, forest and ecology, demographic performance and tax effort."),
    ("Sixteenth Finance Commission", "The owner records the Sixteenth Finance Commission award period as 2026-27 to 2030-31 and the accepted vertical share as 41 per cent of the divisible pool; other recommendations require the report and action-taken memorandum."),
    ("Cesses and surcharges", "Cesses and surcharges have sharing treatment distinct from ordinary divisible-pool taxes and can narrow states' untied share even when gross Union tax collections rise."),
    ("Tax administration", "CBDT administers Union direct taxes, while CBIC and state GST administrations handle indirect-tax and GST functions within their respective legal perimeters."),
    ("Economic-enforcement agencies", "ED, DRI and DGGI function under the Department of Revenue, Ministry of Finance, but their statutory domains are not interchangeable."),
    ("Agricultural-income boundary", "Allied rural activity is not automatically agricultural income, and rural agricultural land is generally outside the capital-asset definition only subject to statutory conditions."),
    ("Digital and indirect-transfer taxation", "The Equalisation Levy addressed specified non-resident digital services, while indirect-transfer rules can tax offshore share transfers deriving substantial value from Indian assets; both require year-specific legal status."),
    ("Income-tax law and federal trust", "The owner records the Income-tax Act, 2025 and Income-tax Rules, 2026 as commencing on 1 April 2026 while earlier years remain governed by the applicable prior law; sound fiscal federalism also requires predictable transfers, compliance capacity and transparent assignment."),
]

TRAPS_10 = [
    "Tax incidence requires analysing legal liability, shifting and the actual economic burden.",
    "Do not describe GST as an origin-based production tax.",
    "Do not equate exemption, zero-rating and input-tax-credit treatment.",
    "Do not say every pre-GST Union or State levy was subsumed.",
    "Do not treat petroleum inclusion or rate structure as timeless legal facts.",
    "Do not call the Finance Commission a GST-rate-setting body.",
    "Do not merge vertical devolution with horizontal distribution.",
    "Do not put cesses and surcharges into the divisible pool without qualification.",
    "Do not merge ED, DRI and DGGI statutory functions.",
    "Do not quote commission awards, tax rates or statutory status without the period.",
]

PANELS_10 = [
    panel(10, "Tax-incidence fork", "comparison-matrix", ["DIRECT TAX -> legal incidence on income/profit base", "INDIRECT TAX -> transaction/consumption levy", "BURDEN may shift through prices", "PROGRESSIVITY requires incidence and base analysis"]),
    panel(10, "GST value-add chain", "mechanism-flow", ["OUTPUT TAX", "minus ELIGIBLE INPUT TAX CREDIT", "-> TAX ON VALUE ADDITION", "-> DESTINATION-JURISDICTION REVENUE"]),
    panel(10, "Subsumed-tax map", "classification-tree", ["UNION -> excise on covered items + service tax + CVD/SAD", "STATE -> VAT/CST + entry + luxury + specified entertainment", "RESULT -> reduced cascading through ITC", "VERIFY item and legal vintage"]),
    panel(10, "Outside-GST boundary", "exclusion-board", ["BASIC CUSTOMS DUTY", "STAMP / PROPERTY / ELECTRICITY DUTIES", "ALCOHOL FOR HUMAN CONSUMPTION", "SPECIFIED PETROLEUM PRODUCTS -> owner-vintage status"]),
    panel(10, "GST Council voting board", "constitutional-board", ["ARTICLE 279A", "CENTRE -> 1/3 weighted votes", "STATES -> 2/3 weighted votes", "DECISION -> at least 3/4 weighted votes"]),
    panel(10, "Inter-state settlement rail", "federal-flow", ["INTER-STATE SUPPLY", "-> IGST COLLECTION", "-> INPUT-CREDIT ADJUSTMENT", "-> DESTINATION SETTLEMENT"]),
    panel(10, "Compensation timeline", "timeline-strip", ["2015-16 -> protected-revenue base", "2017-2022 -> five-year guarantee", "14% -> stated annual protected growth", "TRANSITIONAL -> not permanent entitlement"]),
    panel(10, "Finance Commission map", "federal-matrix", ["VERTICAL -> Union versus states share", "HORIZONTAL -> distribution among states", "XV-FC -> owner records 41%", "XVI-FC -> 2026-27 to 2030-31; accepted 41%"]),
    panel(10, "Divisible-pool boundary", "pool-map", ["ORDINARY SHAREABLE UNION TAXES", "-> DIVISIBLE POOL", "CESSES / SURCHARGES -> distinct treatment", "FEDERAL EFFECT -> state untied-space concern"]),
    panel(10, "Administration and enforcement", "institution-map", ["CBDT -> Union direct taxes", "CBIC + STATE ADMIN -> indirect tax / GST", "ED / DRI / DGGI -> Revenue Department agencies", "FUNCTIONS remain legally distinct"]),
    panel(10, "Tax-base edge cases", "boundary-board", ["ALLIED RURAL ACTIVITY != automatic agricultural income", "RURAL AGRICULTURAL LAND -> statutory conditions", "EQUALISATION LEVY -> specified digital-service history", "INDIRECT TRANSFER -> offshore form, Indian-value link"]),
    panel(10, "Fiscal-federal answer spine", "answer-spine", ["DEFINE base, incidence and destination", "MAP collection, ITC and settlement", "SEPARATE devolution, grants and cesses", "BALANCE harmonisation, autonomy and trust"]),
]

PYQ_SOLUTIONS_10 = [
    common.make_pyq_solution(FACTS_10, "2019", "GS-III", "Enumerate the indirect taxes subsumed in GST and explain the revenue implications.", "Verified routed Mains demand; original model solution, not an official answer.", [2, 3, 4, 5, 6]),
    common.make_pyq_solution(FACTS_10, "2020", "GS-III", "Explain the GST Compensation to States Act, 2017 and the fiscal-federal challenge created by the COVID-19 shock.", "Verified routed Mains demand; original model solution, not an official answer.", [8, 9, 10, 14]),
]

TOPIC_10 = common.topic(
    10,
    "Taxation, GST, Finance Commission and Fiscal Federalism",
    STEMS[10],
    f"{STEMS[10]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_10,
    TRAPS_10,
    [
        (10, "Distinguish direct, indirect, progressive and regressive tax concepts.", [0, 1]),
        (10, "Explain GST's destination principle and input-tax-credit mechanism.", [2, 3, 8]),
        (15, "Enumerate the major subsumed and excluded tax categories under GST.", [4, 5, 6]),
        (15, "Distinguish the GST Council and Finance Commission.", [7, 10, 11]),
        (20, "Evaluate India's fiscal-federal architecture through devolution, cesses and GST settlement.", [8, 11, 12, 13, 14]),
        (20, "How can tax design balance equity, compliance, state autonomy and a common market?", [0, 1, 2, 3, 15, 19]),
    ],
    [
        "Direct, indirect and progressive tax incidence",
        "GST destination principle",
        "Input tax credit and cascading",
        "Union taxes subsumed into GST",
        "State taxes subsumed into GST",
        "GST exclusions and Article 279A voting",
        "IGST inter-state settlement",
        "GST compensation transition",
        "Finance Commission role",
        "Vertical and horizontal fiscal imbalance",
        "Fifteenth and Sixteenth Finance Commissions",
        "Cesses, surcharges and the divisible pool",
        "CBDT, CBIC and state administration",
        "Economic-enforcement and agricultural-income boundaries",
        "Digital taxation, indirect transfers and federal trust",
    ],
    [
        "Separate legal incidence, economic burden, collection mechanism and final revenue assignment.",
        "Map GST through supply, input credit, inter-state settlement and destination revenue.",
        "Balance harmonisation and equalisation with state autonomy, predictable transfers and accountability.",
    ],
    PANELS_10,
    ["direct tax", "indirect tax", "destination-based", "input tax credit", "Article 279A", "three-fourths", "IGST", "Finance Commission", "vertical", "horizontal", "41 per cent", "divisible pool", "cesses", "surcharges"],
    "Audited ledgers route Mains demands on taxes subsumed in GST and the GST compensation framework, plus objective demands on equalisation levy, GST exemptions, indirect transfers, Fifteenth Finance Commission criteria, enforcement agencies and agricultural-income boundaries. Objective answer letters are not inferred.",
    PYQ_SOLUTIONS_10,
    [
        "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/16fc-EM.pdf — attempted 2026-09-03; the official action-taken memorandum returned HTTP 403 to the live fetcher, so no recommendation beyond the repository owner's dated award period and accepted vertical share was imported.",
        "https://fincomindia.nic.in/ — attempted 2026-09-03; the official landing page also returned HTTP 403 to the live fetcher.",
    ],
    "The Finance Commission live pages were blocked with HTTP 403. The package therefore retains only the owner's explicit XVI-FC period and accepted 41 per cent vertical share and directs the learner to the official report for all other recommendations.",
)


TOPICS = {
    "economy-06": TOPIC_06,
    "economy-07": TOPIC_07,
    "economy-08": TOPIC_08,
    "economy-09": TOPIC_09,
    "economy-10": TOPIC_10,
}
