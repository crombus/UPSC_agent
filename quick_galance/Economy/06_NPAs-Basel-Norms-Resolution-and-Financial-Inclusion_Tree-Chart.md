# Economy Topic 6 - Non-Performing Assets (NPAs), Basel Norms, Resolution and Financial Inclusion

**Current-source cutoff: 9 September 2026**

```text
DECODE KEY
|
+-- RBI = Reserve Bank of India
+-- NPA = Non-Performing Asset; IRACP = Income Recognition, Asset
|   Classification and Provisioning
+-- CC/OD = Cash Credit/Overdraft; GNPA/NNPA = Gross/Net NPA
+-- PCR = Provisioning Coverage Ratio; ICR = Interest Coverage Ratio
+-- SCB = Scheduled Commercial Bank; SFB = Small Finance Bank
+-- RRB = Regional Rural Bank; RWA = Risk-Weighted Assets
+-- CET1/AT1 = Common Equity Tier 1/Additional Tier 1
+-- CRAR = Capital to Risk-Weighted Assets Ratio
+-- CCB/CCyB = Capital Conservation/Countercyclical Capital Buffer
+-- D-SIB = Domestic Systemically Important Bank
+-- LCR = Liquidity Coverage Ratio; HQLA = High-Quality Liquid Assets
+-- NSFR = Net Stable Funding Ratio; SMA = Special Mention Account
+-- AQR = Asset Quality Review; CRILC = Central Repository of Information
|   on Large Credits; PCA = Prompt Corrective Action
+-- ICA = Inter-Creditor Agreement; RP = Resolution Plan
+-- SARFAESI = Securitisation and Reconstruction of Financial Assets and
|   Enforcement of Security Interest Act, 2002
+-- DRT/DRAT = Debt Recovery Tribunal/Debt Recovery Appellate Tribunal
+-- ARC/SR = Asset Reconstruction Company/Security Receipt
+-- IBC/CIRP = Insolvency and Bankruptcy Code, 2016/Corporate Insolvency
|   Resolution Process
+-- NCLT = National Company Law Tribunal; CoC = Committee of Creditors
+-- IP = Insolvency Professional; IBBI = Insolvency and Bankruptcy Board of India
+-- NARCL = National Asset Reconstruction Company Limited
+-- IDRCL = India Debt Resolution Company Limited
+-- DFS = Department of Financial Services
+-- DICGC = Deposit Insurance and Credit Guarantee Corporation
+-- PMJDY = Pradhan Mantri Jan-Dhan Yojana; DBT = Direct Benefit Transfer
+-- BSBD = Basic Savings Bank Deposit; BC = Business Correspondent
+-- PSL = Priority Sector Lending; ANBC = Adjusted Net Bank Credit
+-- CEOBE = Credit Equivalent of Off-Balance Sheet Exposures
+-- MUDRA/PMMY = Micro Units Development and Refinance Agency/
|   Pradhan Mantri Mudra Yojana
+-- NABARD = National Bank for Agriculture and Rural Development
+-- SHG/JLG = Self-Help Group/Joint Liability Group
`-- FI-Index = Financial Inclusion Index

NPA RECOGNITION — RBI Commercial Banks IRACP Directions 2025,
updated 01-07-2026
|
+-- overdue = unpaid on contractual due date
+-- term loan -> principal/interest overdue >90 days
+-- bills purchased/discounted -> overdue >90 days
+-- agriculture -> 2 crop seasons short crop; 1 crop season long crop
`-- CC/OD out of order for 90 days:
    excess over sanctioned limit/drawing power; OR
    no credits; OR credits cannot cover interest debited in prior 90 days

ASSET CLASSIFICATION
|
STANDARD -> SUBSTANDARD (NPA <=12 months)
         -> DOUBTFUL (after 12 months substandard)
         -> LOSS (identified uncollectible; write off or 100% provision)
|
`-- borrower-wise within one bank; security does not normally delay recognition

GNPA / NNPA / PROVISION
|
+-- GNPA = recognised gross non-performing exposure
+-- PCR = provisions / GNPA
+-- NNPA = residual after prescribed provisions/adjustments
+-- provision -> profit charge; loan remains
+-- technical write-off -> accounting removal; recovery may continue
`-- waiver -> liability relinquished to stated extent

GENERAL NPA PROVISIONS — RBI directions updated 01-07-2026
|
+-- substandard: 15%; unsecured substandard: 25%
+-- doubtful unsecured portion: 100%
+-- doubtful secured portion: 25% <=1 year; 40% 1-3 years; 100% >3 years
`-- loss asset retained in books: 100%

STRESS AND CONCEALMENT
|
+-- weak appraisal / project delay / macro shock / leverage / governance
+-- ICR = earnings available for interest / interest expense
|   `-- stress indicator, NOT legal NPA definition
+-- Twin Balance Sheet -> Economic Survey 2016-17 diagnostic
+-- restructuring -> viable concession + prudential recognition
+-- forbearance -> temporary regulatory relief
`-- evergreening -> fresh accommodation hides unviable old dues

BASEL ARCHITECTURE
|
+-- Basel I: credit-risk capital
+-- Basel II: Pillar 1 minimum | Pillar 2 review | Pillar 3 disclosure
`-- Basel III: better capital + buffers + leverage + liquidity

RBI BASEL III — Master Circular 01-04-2025; covered SCBs
|
+-- CET1 5.5% | Tier 1 7% | Total CRAR 9% of RWA, before buffers
+-- CCB 2.5% CET1 -> effective CET1 8%; total capital 11.5%
+-- CCyB framework up to 2.5%; not activated in cited circular
`-- excludes SFB, Payments Bank and RRB; category rules differ

RWA + CAPITAL QUALITY
|
+-- RWA -> credit + market + operational risk
+-- CRAR = eligible regulatory capital / RWA x100
`-- CET1 highest-quality going concern -> AT1 going concern -> Tier 2 gone concern

LEVERAGE + LIQUIDITY
|
+-- leverage ratio: Tier 1 / exposure measure
|   `-- 4% D-SIB; 3.5% others, effective 01-10-2019
+-- LCR: HQLA / 30-day stressed net cash outflows >=100% from 01-01-2019
`-- NSFR: available / required stable funding >=100% from 01-10-2021

EARLY WARNING + PCA
|
+-- SMA-0 <=30 days | SMA-1 >30-60 | SMA-2 >60-90
+-- AQR reveals under-recognised stress; CRILC shares large-credit data
`-- PCA 02-11-2021, effective 01-01-2022
    capital + NNPA + leverage; NNPA bands begin 6% / 9% / 12%
    -> corrective restrictions, NOT closure or deposit-insurance payout

RBI OUT-OF-COURT RESOLUTION — Directions 2025, updated 01-07-2026
|
+-- default/credit event -> 30-day Review Period
+-- ICA: 75% by value + 60% by number binds signatories
+-- independent credit evaluation: Rs100 cr+; two at Rs500 cr+; RP4+
+-- covered RP implementation: 180 days after Review Period
`-- delay: +20% provision; later +15% = total extra 35%

RECOVERY AND INSOLVENCY
|
+-- SARFAESI Act 2002 section 13(2): 60-day notice
|   `-- section 13(4) secured enforcement; borrower remedy at DRT
+-- Recovery of Debts and Bankruptcy Act 1993
|   `-- DRT adjudication/recovery; DRAT appeal
+-- ARC under SARFAESI + RBI ARC Directions 2024, updated 23-04-2025
|   `-- acquire assets; Security Receipt = undivided interest in pool
`-- IBC 2016
    NCLT admission -> section 14 moratorium -> IP -> CoC
    -> plan >=66% voting share -> NCLT approval
    -> or liquidation + section 53 waterfall
    IBBI regulates ecosystem; it does not decide an individual case

PERSONAL GUARANTOR — bounded cross-link
|
+-- specified Part III provisions operational from 01-12-2019
+-- IBC section 60 aligns forum with corporate-debtor NCLT
`-- corporate moratorium != automatic personal-guarantor moratorium

NARCL-IDRCL — operational status in DFS Annual Report 2024-25
|
+-- NARCL = RBI-registered ARC / acquirer
+-- IDRCL = resolution manager
+-- 15% cash + 85% Security Receipts
`-- guarantee supports eligible SR shortfall; loss does not vanish

CONDUCT CLASSIFICATIONS
|
+-- NPA -> repayment/asset status
+-- wilful default -> deliberate capacity/misuse test
|   RBI Directions 30-07-2024; threshold Rs25 lakh outstanding
`-- fraud -> separate deception/investigation/reporting process
    RBI Directions 15-07-2024; show cause + >=21 days + reasoned order

FINANCIAL INCLUSION
|
+-- PMJDY launched 28-08-2014 -> basic account + RuPay + DBT + BC
+-- BSBD amendment 04-12-2025, effective 01-04-2026
|   no minimum balance + listed free services + >=4 free withdrawals/month
+-- BC = bank's agent; principal bank responsible
+-- PSL effective 01-04-2025: most domestic banks 40% ANBC/CEOBE
+-- SFB PSL 60% from FY 2025-26 (circular 20-06-2025)
+-- MUDRA/PMMY: Shishu <=Rs50,000; Kishore >Rs50,000-Rs5 lakh;
|   Tarun >Rs5 lakh-Rs10 lakh
|   `-- Tarun Plus >Rs10 lakh-Rs20 lakh for eligible repeat borrower
|       from 24-10-2024
+-- NABARD SHG-Bank Linkage pilot 1992; JLG uses mutual liability
`-- RBI FI-Index: Access + Usage + Quality (release 22-07-2025)

PRELIMS TRAPS
|
+-- overdue != NPA immediately | SMA != NPA
+-- provision != write-off != waiver
+-- CRAR denominator is RWA | LCR != NSFR
+-- ICA 75/60 != IBC CoC 66%
+-- SARFAESI recovery != IBC collective insolvency
+-- ARC Security Receipt != insured deposit
+-- NPA != wilful default != fraud
`-- access/account opening != meaningful inclusion

MAINS ANSWER ROUTE
|
define exact trigger and dated perimeter
-> recognise loss -> provision/capital/liquidity impact
-> choose restructure/recovery/transfer/IBC by viability and security
-> assign RBI/DRT/NCLT/IBBI/ARC/NARCL/DICGC correctly
-> evaluate time + value + governance + distribution + moral hazard
`-- conclude with responsible inclusion and credible exit
```

> **Qualified conclusion:** Honest recognition, adequate loss absorption and credible resolution protect the same trust on which durable financial inclusion depends.
