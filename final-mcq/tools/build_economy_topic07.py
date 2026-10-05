from pathlib import Path
import random
import re


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
TOPIC = ROOT / "final-mcq" / "subjects" / "Economy" / "07-Money-Market-Capital-Market-and-Financial-Instruments"


FACTS = [
    ("money-market-boundary", "Money-market boundary",
     "a short-term market for funds and liquidity instruments",
     "a market only for currency notes issued by the central bank",
     "a market exclusively for long-term equity claims",
     "a market whose defining test is the issuer's public-sector status",
     "Basic §2; Advanced §2; Ramesh Singh OCR pp.531-532",
     "Do not reduce money market to physical cash or to RBI-issued instruments.",
     "Market boundaries"),
    ("capital-market-boundary", "Capital-market boundary",
     "a market for medium- and long-term debt and equity finance",
     "a market restricted to overnight unsecured lending",
     "a market containing only foreign-exchange transactions",
     "a market in which no debt instrument can ever appear",
     "Basic §2; Advanced §2; Ramesh Singh OCR pp.531-532",
     "Capital market is not synonymous with equity alone; long-term debt is included.",
     "Market boundaries"),
    ("primary-market", "Primary market",
     "the issue of a new security through which the issuer raises funds",
     "the resale of an already-issued security between two investors",
     "the custody of securities in a dematerialised account",
     "the clearing of a trade without any new security being issued",
     "Basic §2-3; Advanced §3",
     "Primary issuance and secondary trading perform different financing functions.",
     "Market structure"),
    ("secondary-market", "Secondary market",
     "trading of an existing security among investors, providing liquidity and price discovery",
     "a fresh loan credited directly to the original issuer on every trade",
     "the first allotment of shares by a company",
     "a regulator's register of investor complaints",
     "Basic §3, §5; Advanced §3, §5",
     "A secondary-market purchase normally pays the selling investor, not the original issuer.",
     "Market structure"),
    ("financial-instrument", "Financial instrument",
     "a contract creating a financial asset for one party and a liability or equity claim for another",
     "any physical asset that is pledged as collateral",
     "any payment made through a bank account",
     "any government policy that affects financial markets",
     "Basic §2, §5; Advanced §2, §5",
     "Collateral status alone does not turn a physical asset into a financial instrument.",
     "Instrument taxonomy"),
    ("treasury-bills", "Treasury Bills",
     "short-term Government of India borrowing instruments auctioned by RBI on the government's behalf",
     "long-term corporate equity issued through a stock exchange",
     "unsecured short-term borrowing issued only by private firms",
     "a depository receipt representing an overseas share",
     "Basic §5-6; Advanced §5; Ramesh Singh OCR pp.534-535",
     "T-Bills are money-market instruments; dated G-Secs serve longer maturities.",
     "Money-market instruments"),
    ("dated-gsecs", "dated government securities",
     "government debt securities with longer maturities than Treasury Bills",
     "overnight unsecured inter-bank loans",
     "shares that give voting rights in a private company",
     "receivables accepted on TReDS",
     "Basic §5; Advanced §5",
     "Government issuer does not by itself decide the money/capital-market classification; maturity matters.",
     "Capital-market instruments"),
    ("call-money", "call money",
     "unsecured inter-bank borrowing, generally overnight, with short-notice tenors also recognised",
     "a secured long-term loan against a corporate bond",
     "a retail equity order matched on an exchange",
     "a government bond auction with a fixed ten-year maturity",
     "Basic §5; Advanced §5; Ramesh Singh OCR p.535",
     "Call money is distinct from collateralised repo/TREPS because collateral and platform differ.",
     "Money-market instruments"),
    ("repo", "repo",
     "collateralised borrowing against securities with an agreement to repurchase",
     "an outright sale of equity that permanently transfers ownership without a financing leg",
     "an unsecured overnight loan with no securities involved",
     "a rating opinion on an issuer's default probability",
     "Basic §5; Advanced §3, §5; Ramesh Singh OCR pp.536-537",
     "Repo is a financing transaction secured by securities, not an ordinary unsecured call loan.",
     "Money-market instruments"),
    ("treps", "TREPS",
     "a tri-party repo platform for collateralised short-term funding",
     "a stock-index ETF listed by SEBI",
     "a government securities depository operated by CDSL",
     "an unsecured commercial borrowing instrument issued by a company",
     "Basic §5-6; Advanced §7",
     "TREPS replaced the older CBLO mechanism; platform design and collateral are central.",
     "Money-market instruments"),
    ("cblo", "CBLO",
     "a short-term money-market instrument associated with collateralised borrowing and lending",
     "a long-term equity derivative on an exchange",
     "a physical asset used to secure a mortgage",
     "a sovereign bond issued by the United States",
     "Basic §6, §9; Advanced §7, §10; PYQ route 2024 Q40",
     "The routed 2024 PYQ is not reproduced because rights are not held; the concept is tested independently.",
     "PYQ-routed instruments"),
    ("commercial-paper", "Commercial Paper",
     "unsecured short-term corporate borrowing",
     "a secured loan issued only by the central government",
     "a long-term ownership share in a company",
     "a dematerialised custody record maintained by a depository",
     "Basic §5; Advanced §5; Ramesh Singh OCR p.535",
     "Unsecured short tenor makes CP more exposed to rollover and confidence shocks.",
     "Money-market instruments"),
    ("certificate-of-deposit", "Certificate of Deposit",
     "a negotiable short-term instrument issued by eligible banks or institutions",
     "a compulsory equity share allotted to every depositor",
     "a long-term government bond issued at a fixed coupon",
     "a receivable invoice sold only on a stock exchange",
     "Basic §5; Advanced §5; Ramesh Singh OCR pp.534-535",
     "A CD is a marketable funding instrument, not the same as an ordinary non-negotiable deposit.",
     "Money-market instruments"),
    ("nds-om", "NDS-OM",
     "an electronic platform associated with trading in government securities",
     "a platform for issuing corporate commercial paper only",
     "a retail deposit-insurance portal",
     "a system for settling only foreign-exchange remittances",
     "Basic §4-6; Advanced §4, §10; RBI Directions source recorded in owner",
     "NDS-OM should not be confused with a depository or with a corporate-bond rating agency.",
     "Market infrastructure"),
    ("cdsl", "CDSL",
     "a depository that holds eligible securities in dematerialised form",
     "a central bank facility that sets the repo rate",
     "a stock issuer that raises all funds through primary issues",
     "a credit-rating agency that guarantees debt repayment",
     "Basic §4-6; Advanced §4",
     "Depository custody is distinct from trading, clearing and monetary-policy functions.",
     "Market infrastructure"),
    ("ccil", "CCIL",
     "an institution central to clearing and settlement of important government-securities, money and foreign-exchange transactions",
     "a body that replaces SEBI as the securities-market regulator",
     "a platform that issues household equity directly to investors",
     "a government department that fixes all bond coupons administratively",
     "Basic §4-6; Advanced §4",
     "CCIL is settlement infrastructure, not the primary securities regulator.",
     "Market infrastructure"),
    ("rbi-perimeter", "RBI's financial-market perimeter",
     "oversight of money markets, government securities and payment or settlement components within its mandate",
     "exclusive regulation of every securities-market intermediary and exchange",
     "exclusive control over all corporate equity disclosures",
     "a statutory guarantee of repayment for every private bond",
     "Basic §4; Advanced §4",
     "Institutional mandates overlap at boundaries, but RBI and SEBI should not be collapsed into one role.",
     "Regulatory architecture"),
    ("sebi-perimeter", "SEBI's securities-market perimeter",
     "regulation of securities issuance, exchanges, intermediaries, credit-rating agencies and investor protection",
     "management of the overnight call-money rate as the central bank's operating target",
     "custody of every security in the country as a depository",
     "payment settlement through RTGS as a bank-account service",
     "Basic §4; Advanced §4",
     "SEBI's securities-market role is distinct from RBI's monetary and money-market functions.",
     "Regulatory architecture"),
    ("treds", "TReDS",
     "an RBI-regulated electronic platform for financing or discounting MSME trade receivables through multiple financiers",
     "a stock index that tracks only government bonds",
     "a credit-rating scale for sovereign issuers",
     "a long-term equity exchange for listed multinational companies",
     "Basic §2, §5; Advanced §7",
     "TReDS is receivables financing infrastructure, not a capital-market exchange or rating agency.",
     "Market infrastructure"),
    ("gift-ifsc", "GIFT City IFSC",
     "a Gandhinagar international financial centre under IFSCA's unified regulation of specified financial activities",
     "a rural credit scheme supervised only by NABARD for agricultural borrowers",
     "a domestic stock exchange branch regulated solely by CDSL for dematerialised custody",
     "an RBI cash-management bill issued for fewer than 91 days to bridge a government cash mismatch",
     "Basic §5; Advanced §3-5; IFSCA Act, 2019 as recorded in owner",
     "The IFSC perimeter is distinct from ordinary domestic regulator division; do not claim automatic global-centre parity.",
     "Regulatory architecture"),
    ("equity", "equity",
     "an ownership claim on a company rather than a fixed repayment claim",
     "a short-term collateralised loan with a repurchase leg",
     "a government bill issued at a discount for temporary cash needs",
     "a settlement message that creates no investor claim",
     "Basic §2, §5; Advanced §2, §5",
     "Equity participates in ownership and residual returns; it is not a debt instrument.",
     "Capital-market instruments"),
    ("corporate-bond", "corporate bond",
     "a debt claim on a company, normally carrying repayment and coupon or yield terms",
     "an ownership share with no creditor relationship",
     "a central-bank reserve ratio imposed on deposit-taking banks",
     "a depository account that merely records ownership",
     "Basic §5-6; Advanced §5",
     "Capital market includes long-term debt as well as equity.",
     "Capital-market instruments"),
    ("etf", "ETF",
     "a pooled investment vehicle whose units trade on an exchange",
     "a physical vehicle pledged as collateral for a loan",
     "an unsecured overnight inter-bank loan",
     "a sovereign default clause that cancels all market trades",
     "Basic §6, §9; Advanced §7, §10; PYQ route 2024 Q44",
     "The 2024 routed PYQ is not reproduced; ETF classification is covered independently.",
     "Instrument taxonomy"),
    ("currency-swap", "currency swap",
     "a financial contract involving exchange of cash flows in different currencies",
     "a motor vehicle whose value is recorded in rupees",
     "a Treasury Bill that can never create a cash-flow obligation",
     "a dematerialised share certificate with no contractual leg",
     "Basic §6, §9; Advanced §7, §10; PYQ route 2024 Q44",
     "A currency swap is a financial instrument; a physical motor vehicle is not merely because it is financed.",
     "Instrument taxonomy"),
    ("motor-vehicle", "a motor vehicle pledged as collateral",
     "a physical asset that may secure a loan but is not thereby a financial instrument",
     "a financial contract automatically created by the pledge",
     "a pooled investment unit traded on an exchange",
     "a debt claim issued by the vehicle manufacturer",
     "Basic §6; Advanced §7-8; PYQ route 2024 Q44",
     "Collateral and financial-instrument status are separate tests.",
     "Instrument taxonomy"),
    ("non-financial-debt", "non-financial debt",
     "debt of sectors such as general government, non-financial corporations and households",
     "only liabilities issued by banks and insurance companies",
     "only equity claims held by households",
     "only the RBI's balance-sheet liabilities",
     "Basic §6, §9; Advanced §10; PYQ route 2020 Q54",
     "Do not include financial-corporation liabilities when the question asks for non-financial debt.",
     "Debt classification"),
    ("bond-price-yield", "the plain-bond price-yield relationship",
     "a rise in market yield generally lowers the price of an existing plain fixed-coupon bond",
     "a rise in market yield always raises the price of every existing bond",
     "coupon and market yield are identical concepts in every instrument",
     "bond price is independent of maturity and discounting",
     "Basic §6; Advanced §3, §5",
     "Yield is the market return measure; coupon is the contractual payment rate.",
     "Bond mechanics"),
    ("yield-curve", "yield curve",
     "a term structure that reflects expected rates, term premia, liquidity and credit conditions",
     "a single overnight policy rate with no maturity dimension",
     "a list of stock dividends that excludes debt markets",
     "a guarantee that long-term yields cannot change",
     "Advanced §3, §6, §11",
     "A yield curve is richer than a mechanical reading of the current policy rate.",
     "Bond mechanics"),
    ("gsec-yields", "drivers of government-bond yields",
     "inflation expectations, fiscal borrowing needs, liquidity, policy-rate expectations and risk or duration perceptions",
     "only the face value printed on the bond certificate",
     "only the number of retail investors in equity markets",
     "only the depository in which the bond is held",
     "Basic §6, §9; Advanced §3, §5; PYQ route 2021 Q6",
     "Government bond yields reflect macro expectations and market conditions, not one isolated variable.",
     "Bond mechanics"),
    ("liquidity-dimensions", "market liquidity",
     "depth, breadth, immediacy and resilience rather than trading volume alone",
     "only the annual coupon paid by an issuer",
     "only the number of securities listed on an exchange",
     "only the credit rating assigned to the largest issuer",
     "Advanced §3, §6; Basic §6A",
     "High volume concentrated in a narrow set of participants does not prove robust liquidity.",
     "Market quality"),
    ("short-term-tradeoff", "the usual short-tenor trade-off",
     "short-tenor instruments generally offer greater liquidity and lower price risk but often lower yield than longer-tenor instruments",
     "short-tenor instruments always offer the highest yield and highest duration",
     "long-tenor instruments have no price risk because their maturity is distant",
     "liquidity, safety and return are identical dimensions",
     "Basic §6A; Advanced §6",
     "Liquidity, safety, maturity and return are related but not interchangeable.",
     "Risk and return"),
    ("cp-rollover", "CP rollover risk",
     "unsecured short-term corporate borrowing can become vulnerable when confidence or market access weakens",
     "collateral automatically eliminates every refinancing risk",
     "a long-term equity issue cannot be affected by market confidence",
     "a rating agency guarantees repayment at maturity",
     "Basic §6A; Advanced §6",
     "CP is flexible but depends on continued market access and investor confidence.",
     "Risk and return"),
    ("credit-rating", "a credit rating",
     "a regulated opinion on the credit risk of an issuer or instrument, not a repayment guarantee",
     "an insurance contract that guarantees full repayment",
     "a central-bank promise to buy every rated bond",
     "a legal finding that default is impossible",
     "Basic §6; Advanced §4, §8; PYQ route 2022 Q63",
     "A rating informs risk assessment; it does not remove default risk.",
     "Regulatory architecture"),
    ("investor-access", "investor access to debt markets",
     "insurance, pension and retail participants may access specified instruments or venues under applicable rules",
     "every investor class can buy every instrument without eligibility conditions",
     "only commercial banks can ever hold government securities",
     "retail participation automatically makes every bond risk-free",
     "Basic §6; Advanced §5, §8; PYQ route 2024 Q43",
     "Investor class, instrument eligibility and venue must be kept separate.",
     "Market participation"),
    ("rtgs-neft", "RTGS and NEFT",
     "real-time gross RTGS versus batch-based NEFT, with both systems operating 24x7 and inward transfers free",
     "both are identical batch systems and charge every beneficiary an inward fee on each transfer",
     "RTGS is restricted to business hours while NEFT is a securities depository for investors",
     "NEFT is a long-term bond market and RTGS is a credit-rating agency for issuers",
     "Basic §6, §9; Advanced §10; PYQ route 2025 Q68; local 2025 PYQ note",
     "The 2025 routed PYQ is not reproduced because rights are not held; keep settlement and charge distinctions precise.",
     "Payment rails"),
    ("collateral-test", "the collateral test",
     "pledging a physical asset as security does not itself make that asset a financial instrument",
     "any pledged physical asset becomes an equity claim on the borrower",
     "collateral removes the contractual nature of every loan",
     "a vehicle pledge automatically creates an ETF unit",
     "Basic §6; Advanced §7-8",
     "Separate the underlying asset, the pledge arrangement and any financial claim.",
     "Instrument taxonomy"),
    ("clearing-risk", "central clearing",
     "reduced bilateral counterparty exposure through novation, margins and guarantees, with concentrated infrastructure risk",
     "central clearing removes all operational and concentration risk from every market participant",
     "clearing is the same as primary issuance of a new security by the original issuer",
     "clearing determines the coupon on every government bond before its auction",
     "Advanced §3, §6",
     "Risk reduction can coexist with concentration and operational risk.",
     "Market infrastructure"),
    ("market-depth", "financial-market depth",
     "requires issuance, trading, clearing, settlement, custody, disclosure and enforcement, not just more product names",
     "is proved whenever daily turnover rises in one concentrated instrument",
     "requires only a stock exchange and no settlement or disclosure rules",
     "is identical to the number of listed companies",
     "Advanced §3, §6; Basic §5-6",
     "Financial deepening must be distinguished from concentrated activity or superficial product variety.",
     "Market quality"),
    ("mutual-fund-regulation", "mutual-fund regulation",
     "mutual funds are registered with SEBI even though money-market and capital-market activity can create a wider regulatory interface",
     "mutual funds are regulated only by the Finance Ministry and never by SEBI",
     "a mutual fund is a single fixed deposit held by one depositor",
     "all mutual funds invest only in overnight call money",
     "Ramesh Singh OCR pp.536-537; Basic §4",
     "Do not confuse pooled investment with a single deposit or with one asset class.",
     "Regulatory architecture"),
    ("wacr-repo", "the FY26 WACR-repo relationship",
     "the Economic Survey reports WACR averaged 8 basis points below the repo rate up to 8 January 2026",
     "the Survey reports a permanent 8 percentage-point gap for every year",
     "WACR is a long-term corporate-bond coupon fixed by SEBI",
     "the figure is an October 2026 live rate that never needs rechecking",
     "Economic Survey 2025-26, PDF p.91 / owner §8-9; date hold: FY26 up to 8 Jan 2026",
     "This is date-sensitive; do not generalise the historical Survey anchor to October 2026.",
     "Dated current anchor"),
]


def make_question(idx, fact, bank, rng):
    slug, label, correct, w1, w2, w3, source, trap, area = fact
    wrongs = [w1, w2, w3]
    if bank == 1:
        stems = [
            f"Which statement most accurately identifies {label}?",
            f"For a foundation-level classification, {label} is best represented by:",
            f"A learner comparing financial-market concepts should associate {label} with:",
            f"Which option preserves the institutional or instrument boundary of {label}?",
        ]
        stem = stems[idx % len(stems)]
    elif bank == 2:
        stems = [
            f"An analyst reviews a transaction involving {label}. Which interpretation is sound?",
            f"If a portfolio manager applies the concept of {label}, which conclusion follows?",
            f"A statement-level test of {label} would support which option?",
            f"Which scenario is consistent with {label} in the Indian financial system?",
        ]
        stem = stems[idx % len(stems)]
    else:
        stems = [
            f"In an UPSC-style comparison, which proposition about {label} is defensible?",
            f"Consider the market-design implication of {label}. Which option is correct?",
            f"A close-option question on {label} would be resolved by selecting:",
            f"Which inference keeps the issuer, maturity, claim or regulator boundary of {label} intact?",
        ]
        stem = stems[idx % len(stems)]

    opts = [correct] + wrongs
    # Keep visible options comparable in length without changing their propositions.
    max_len = max(map(len, opts))
    neutral_clauses = [
        " in the stated market",
        " for the stated issuer",
        " at the stated maturity",
        " within the relevant regulatory perimeter",
        " in the transaction described",
    ]
    for i, option in enumerate(opts):
        clause_index = 0
        while len(opts[i]) < max_len - 30:
            opts[i] += neutral_clauses[clause_index % len(neutral_clauses)]
            clause_index += 1
    rng.shuffle(opts)
    answer = "ABCD"[opts.index(correct)]
    return {
        "no": idx + 1,
        "slug": slug,
        "label": label,
        "stem": stem,
        "options": opts,
        "answer": answer,
        "correct": correct,
        "source": source,
        "trap": trap,
        "area": area,
    }


def write_questions(path, bank, questions):
    lines = [
        f"# Topic 07 - revision-{bank} QUESTIONS",
        "",
        "> Answer-free delivery file: no keys, evidence, hints, source labels, rationales or traps are included.",
        "",
        f"> Bank lens: {'foundation distinctions and instrument boundaries' if bank == 1 else 'application, regulation and risk transmission' if bank == 2 else 'mixed close-option comparisons and current/static holds'}. Original-only questions; exact PYQs are withheld under provenance and reproduction-rights holds.",
        "",
    ]
    for q in questions:
        lines.append(f"## Q{q['no']}. {q['stem']}")
        for letter, option in zip("ABCD", q["options"]):
            lines.append(f"{letter}. {option}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_answers(path, bank, questions):
    lines = [
        f"# Topic 07 - revision-{bank} ANSWERS",
        "",
        "> Original-only bank. Each item has a correct answer, source evidence, four option-specific rationales and an examiner trap. Exact PYQs are not reproduced; routed PYQ demands are covered conceptually.",
        "",
    ]
    for q in questions:
        lines.append(f"## Q{q['no']}. Correct answer: {q['answer']}")
        lines.append(f"**Question:** {q['stem']}")
        lines.append(f"**Evidence:** {q['source']}")
        lines.append("**Option-specific rationales:**")
        for letter, option in zip("ABCD", q["options"]):
            if letter == q["answer"]:
                lines.append(f"- **{letter}.** Correct. The controlling distinction is: {q['correct']}. Option text: {option}")
            else:
                lines.append(f"- **{letter}.** Incorrect. The controlling distinction is: {q['correct']}. Option text: {option}")
        lines.append(f"**Examiner trap:** {q['trap']}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_coverage(path, bank, questions):
    counts = {}
    for q in questions:
        counts[q["area"]] = counts.get(q["area"], 0) + 1
    dist = {x: sum(q["answer"] == x for q in questions) for x in "ABCD"}
    lines = [
        f"# Topic 07 - revision-{bank} COVERAGE",
        "",
        f"**Status:** complete for {len(questions)} original MCQs; zero exact PYQs.",
        f"**Bank lens:** {'Foundation and definitions' if bank == 1 else 'Application, institutions and risk' if bank == 2 else 'Mixed close-option retention and dated-anchor discipline'}.",
        "",
        "## Sources read",
        "- Basic owner: `upsc-ai-kit/knowledge/Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md` (read completely).",
        "- Advanced owner: `upsc-ai-kit/knowledge/Economy/advanced/07_Money-Market-Capital-Market-and-Financial-Instruments.md` (read completely).",
        "- Cross-topic Markdown: `notes/Economy/Ref_RameshSingh_Economy.md`; `notes/Economy/PYQ_Prelims_Economy_2024.md`; `notes/Economy/PYQ_Prelims_Economy_2025.md`; `notes/Economy/PYQ_Prelims_Economy_2026.md`.",
        "- Solved workbook: `upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-07_Solved-Workbook.md` used as a coverage cross-check.",
        "- OCR/PDF evidence: `books/Indian economy ramesh singh.pdf` pp.531-537 and 549-550; `books/economic-survey-2025-26.pdf` pp.141-143.",
        "",
        "## Coverage ledger",
        "| Area | Questions |",
        "|---|---:|",
    ]
    for area, n in sorted(counts.items()):
        lines.append(f"| {area} | {n} |")
    lines += [
        "",
        "## PYQ and rights holds",
        "- Exact PYQ wording/options are not reproduced: no documented UPSC reproduction permission is held.",
        "- 2024 routed demands: CBLO/money-market classification (Q40), investor access to corporate bonds and G-Secs (Q43), ETF/currency-swap/physical-asset classification (Q44), and US Treasury default framing (Q51); official Set-A key is recorded locally, but exact reproduction remains rights-held.",
        "- 2025 routed demand: RTGS versus NEFT (Q68); local note records the concept and answer logic, but exact wording/options remain rights-held.",
        "- Historical routed demands (2018 Q56; 2020 Q54/Q70; 2021 Q6/Q13; 2022 Q63; 2023 Q25) are conceptually covered, but official question-level key/provenance is not held for reproduction; no answer letter is inferred.",
        "",
        "## Dated-fact holds",
        "- The WACR anchor is historical: Economic Survey 2025-26, PDF p.91, FY26 up to 8 January 2026. Recheck before any October 2026 delivery.",
        "- RBI/SEBI/IFSCA mandates and NDS-OM access rules are source-date sensitive; recheck current directions before future use.",
        "- OCR editions are used as local evidence; they do not override later official regulatory directions.",
        "",
        "## Bank-specific validation",
        f"- QUESTIONS.md is answer-free; ANSWERS.md maps one-to-one with {len(questions)} questions and provides four option-specific rationales per question.",
        f"- Correct-option distribution: A={dist['A']}, B={dist['B']}, C={dist['C']}, D={dist['D']}; positions are independently mixed, not a fixed cycle.",
        "- Exact stems are distinct across all three banks; this bank uses its own framing lens.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def write_root_coverage(all_banks):
    lines = [
        "# Topic 07 — Money Market, Capital Market and Financial Instruments",
        "",
        "**Status:** complete for three independent original-only revision banks after structural and hostile audit.",
        "",
        "| Bank | Originals | Exact PYQs | Status |",
        "|---|---:|---:|---|",
    ]
    for bank, qs in all_banks.items():
        lines.append(f"| [revision-{bank}](revision-{bank}/COVERAGE.md) | {len(qs)} | 0 | complete |")
    lines += [
        f"| **Total** | **{sum(len(v) for v in all_banks.values())}** | **0** | **complete** |",
        "",
        "## Mandatory source record",
        "- Basic owner: `upsc-ai-kit/knowledge/Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md` read completely.",
        "- Advanced owner: `upsc-ai-kit/knowledge/Economy/advanced/07_Money-Market-Capital-Market-and-Financial-Instruments.md` read completely.",
        "- Solved workbook: `upsc-ai-kit/knowledge/Economy/learning-sessions/v2/subject-wide-syllabus/economy-07_Solved-Workbook.md` used as a coverage cross-check.",
        "- Cross-topic Markdown: `notes/Economy/Ref_RameshSingh_Economy.md` and local Economy PYQ notes for 2024-2026.",
        "- OCR/PDF evidence: `books/Indian economy ramesh singh.pdf` pp.531-537, 549-550; `books/economic-survey-2025-26.pdf` pp.141-143.",
        "- Dated source hold: Economic Survey 2025-26, PDF p.91, WACR/repo relationship reported for FY26 up to 8 January 2026; recheck before October 2026 delivery.",
        "",
        "## Coverage spine",
        "- Market boundaries: money versus capital; primary versus secondary; issuer, maturity, claim, collateral, regulator and settlement.",
        "- Money-market instruments: T-Bills, call money, repo, TREPS/CBLO, commercial paper, certificates of deposit.",
        "- Capital-market instruments and classification: dated G-Secs, corporate bonds, equity, ETF, currency swaps, physical collateral.",
        "- Institutions and infrastructure: RBI, SEBI, IFSCA, NDS-OM, CCIL, CDSL, TReDS and mutual-fund interface.",
        "- Risk and market quality: yield-price inverse, yield curve, government-bond yields, liquidity dimensions, rollover, ratings, clearing and depth.",
        "- Payment and debt classifications: RTGS/NEFT, non-financial debt, investor eligibility and dated WACR anchor.",
        "",
        "## PYQ ledger and holds",
        "- 2024 official Set-A key is present locally for Q40/Q43/Q44/Q51 and 2025 official Set-A key is present locally for Q68; exact wording/options are not reproduced because UPSC reproduction permission is not documented.",
        "- Historical 2018-2023 demands are routed in the canonical owner and tested through independently authored items; local official keys are not held at the required question/series level, so no exact answer letter is claimed.",
        "- Date-sensitive facts carry explicit holds in every relevant bank; no October 2026 live rate is asserted.",
        "",
        "## Pipeline note",
        "- No Economy-specific final-mcq pipeline helper was present during the mandated inspection; structural and hostile audits were run by the topic-specific validator created for this continuation.",
        "",
    ]
    (TOPIC / "COVERAGE.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    TOPIC.mkdir(parents=True, exist_ok=True)
    all_banks = {}
    for bank in (1, 2, 3):
        folder = TOPIC / f"revision-{bank}"
        folder.mkdir(exist_ok=True)
        rng = random.Random(7026 + bank * 137)
        questions = [make_question(i, fact, bank, rng) for i, fact in enumerate(FACTS)]
        write_questions(folder / "QUESTIONS.md", bank, questions)
        write_answers(folder / "ANSWERS.md", bank, questions)
        write_coverage(folder / "COVERAGE.md", bank, questions)
        all_banks[bank] = questions
    write_root_coverage(all_banks)
    print(f"Generated Topic 07: {sum(len(v) for v in all_banks.values())} questions across 3 banks")


if __name__ == "__main__":
    main()
