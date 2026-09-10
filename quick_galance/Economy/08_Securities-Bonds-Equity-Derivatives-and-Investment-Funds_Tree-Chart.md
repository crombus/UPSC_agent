# Economy Topic 8 — Securities, Bonds, Equity, Derivatives and Investment Funds

**Current-law cutoff:** 9 September 2026  
**Central thesis:** classify the legal claim, cash flow, priority, optionality, leverage, liquidity promise
and regulator before comparing return. This is education, not investment advice.

```text
DIRECT: debt / equity / hybrid
DERIVED: forward / future / option / swap
POOLED: mutual fund / ETF / REIT / InvIT / AIF
MANAGED OR RETIREMENT: PMS / NPS
        |
price + payoff + liquidity + custody + conduct + systemic risk
```

## 1. Claim hierarchy

| Claim | Meaning | Boundary |
|---|---|---|
| Debt | Contractual creditor claim | Priority is not guaranteed recovery |
| Equity | Residual ownership claim | Dividend and capital gain are not promised |
| Preference share | Share capital with priority over ordinary equity | Ordinarily behind creditors |
| Hybrid | Contract combines debt/equity features | Read actual conversion and loss terms |

## 2. Bond sheet

- Face value: contractual reference principal.
- Coupon rate: annual coupon / face value.
- Current yield: annual coupon / market price.
- YTM: Yield to Maturity, discount rate equating price to promised cash flows through maturity.
- Duration: cash-flow timing and approximate price sensitivity; not default probability.
- Convexity: curvature correction beyond duration.
- Credit spread: excess yield over benchmark reflecting default, liquidity and other premia.

```text
yield up -> discount rate up -> present value down -> bond price down
```

**Risks:** default, spread, interest rate, duration, reinvestment, liquidity, inflation, currency, event
and embedded-option risk.

## 3. Special bond types

| Bond | Decode | Trap |
|---|---|---|
| Zero-coupon | No periodic coupon; issued at discount and redeemed later | Zero coupon != zero yield |
| Floating-rate | Coupon resets to benchmark plus spread | Basis and credit risk remain |
| Inflation-indexed | Specified cash flow linked to inflation index | No assured after-tax real return |
| Callable | Issuer may redeem early | Creates investor reinvestment risk |
| Puttable | Investor may demand redemption | Contract conditions govern |
| Convertible | Debt may convert into equity | `May convert` != already equity |
| Masala | Rupee-denominated debt issued overseas | Direct INR risk lies with overseas investor |
| Green debt | Proceeds linked to eligible environmental uses | Label != credit guarantee |

**SEBI green-debt disclosure/anti-greenwashing framework:** 6 February 2023.  
**ECB = External Commercial Borrowing; INR = Indian rupee.** Current Masala-bond thresholds must be
checked in the live RBI ECB framework rather than memorised from old circulars.

## 4. Equity and ratios

- Market capitalisation = market price per share x shares outstanding.
- EPS = Earnings Per Share = relevant profit / weighted-average ordinary shares.
- P-E = Price-Earnings ratio; weak with negative or cyclically distorted earnings.
- P-B = Price-Book ratio; context matters for asset-light firms.
- Dividend yield = dividend per share / market price; can rise because price fell.
- Beta = historical co-movement relative to a chosen market benchmark, not guaranteed return.

## 5. Derivative map and payoff

| Contract | Rights/obligations | Venue / risk |
|---|---|---|
| Forward | Both parties obligated; customised | Usually OTC; bilateral/cleared exposure |
| Future | Both parties obligated; standardised | Exchange, CCP, daily MTM and margin |
| Call | Buyer has right to buy at strike | Writer has contingent obligation |
| Put | Buyer has right to sell at strike | Premium affects break-even |
| Swap | Exchange specified cash-flow streams | Rate/currency basis and counterparty risk |

```text
long call payoff = max(spot - strike, 0) - premium
long put payoff  = max(strike - spot, 0) - premium

hedge = offsets existing exposure
speculation = creates/enlarges exposure
arbitrage = exploits inconsistent prices using offsetting positions
```

**OTC = Over the Counter; CCP = Central Counterparty; MTM = Mark to Market.**

## 6. Margin and current controls

```text
price shock -> MTM loss -> variation-margin call -> funding need
           -> forced sale -> more price pressure -> contagion
```

- Initial margin covers potential future exposure; variation margin settles current change.
- SEBI equity-index derivatives strengthening circular: 1 October 2024.
- SEBI position-monitoring updates: 29 May and 1 September 2025.
- RBI Margin for Derivative Contracts Directions: 8 May 2024.
- RBI non-centrally cleared OTC derivative margin directions: updated 21 February 2025.
- Exchange/CCP control does not abolish leverage, basis, liquidity or operational risk.

## 7. Mutual-fund map

```text
investor -> units -> trust
                  -> AMC manages
                  -> trustee oversees
                  -> custodian holds assets

NAV = (assets - liabilities) / units outstanding
```

| Axis | Decode |
|---|---|
| Open-ended | Continuing purchase/redemption under applicable NAV rules |
| Closed-ended | Fixed term; exchange route may provide liquidity |
| Active | Manager selects securities |
| Passive/index | Seeks benchmark tracking |
| ETF | Exchange-Traded Fund; intraday market price may differ from NAV |
| Equity/debt/hybrid | Underlying asset mix |
| Direct plan | No distributor commission in plan expenses |
| Regular plan | Distributor route and commission cost |
| TER | Total Expense Ratio; reduces scheme return |

**Current framework:** SEBI Mutual Funds Regulations dated 16 January 2026, effective 1 April 2026;
Master Circular dated 20 March 2026. Current TER caps are scheme/framework-dependent and not frozen here.

## 8. Riskometer and safeguards

- Six levels: Low, Low to Moderate, Moderate, Moderately High, High, Very High.
- SEBI circular dated 5 November 2024 strengthened expense, return, yield and Riskometer disclosure.
- SID = Scheme Information Document; KIM = Key Information Memorandum.
- Trustees oversee; AMC = Asset Management Company; custodian safeguards assets.
- Segregated portfolio can isolate specified credit-event assets; it does not erase loss.
- SCORES 2.0 = SEBI Complaints Redress System upgrade announced 1 April 2024.
- Risk label, past return, rating and registration are not investment guarantees.

## 9. Bounded vehicle comparison

| Vehicle | Core identity | Current anchor |
|---|---|---|
| REIT | Real Estate Investment Trust; pooled real-estate cash-flow exposure | SEBI Master Circular 11 Jul 2025 |
| InvIT | Infrastructure Investment Trust; pooled infrastructure exposure | SEBI Master Circular 11 Jul 2025 |
| AIF | Alternative Investment Fund; privately pooled category framework | SEBI Master Circular 3 Jun 2026 |
| PMS | Portfolio Management Services; client-specific management | SEBI Master Circular 16 Jul 2025 |
| NPS | National Pension System; defined-contribution pension architecture | PFRDA |

**AIF:** Category I includes specified venture/developmental funds; Category II is residual private
pooling; Category III may use complex/leverage strategies. Hedge funds and venture-capital funds are
AIFs; direct stocks and bonds are not.

**NPS architecture:** PFRDA = Pension Fund Regulatory and Development Authority; NPS Trust oversees;
pension funds invest; CRA = Central Recordkeeping Agency; PoP = Point of Presence; custodian holds assets.

## 10. Jurisdiction

| Regulator | Core scope |
|---|---|
| SEBI | Domestic listed securities, securities derivatives, mutual funds, AIFs, REITs, InvITs, PMS and conduct |
| RBI | Government securities and specified OTC rate/foreign-exchange derivatives |
| PFRDA | NPS and pension intermediaries |
| IFSCA | International Financial Services Centres Authority; IFSC products, services and institutions |

**GIFT IFSC = Gujarat International Finance Tec-City International Financial Services Centre.**
IFSCA Fund Management Regulations were notified on 19 February 2025.
AMFI = Association of Mutual Funds in India, an industry body rather than statutory regulator.

## 11. Topic 7 infrastructure cross-link

- Primary market creates and first allocates a security; secondary market transfers an existing claim.
- Exchange/OTC execution, clearing, DvP settlement and depository custody are different functions.
- Depositories Act 1996 section 10: depository is registered owner for transfer; investor remains
  beneficial owner with substantive rights and liabilities.
- T+1 is the standard equity cash settlement cycle after the January 2023 transition.
- Optional T+0 was introduced 28 March 2024 and expanded 10 December 2024; it is not universal
  instantaneous settlement.

## 12. Market abuse and suitability

- UPSI = Unpublished Price Sensitive Information.
- Insider Trading Regulations amended through 12 March 2025.
- PFUTP = Prohibition of Fraudulent and Unfair Trade Practices; regulations amended through 5 December 2025.
- Insider trading, manipulation, front running, false disclosure and unregistered advice are distinct.
- Disclosure informs; suitability matches product and investor; grievance systems provide remedy.
- Registration does not endorse performance.

## 13. Prelims traps and Mains route

1. Fixed income != fixed market price.
2. Coupon != current yield != YTM.
3. Duration != maturity or default probability.
4. Callable benefits issuer; puttable benefits investor.
5. Green label != repayment guarantee.
6. Long-option limited loss does not apply to the writer.
7. Margin != purchase price or maximum loss.
8. OTC != unregulated.
9. ETF price can differ from NAV.
10. Direct plan != direct security ownership.
11. Diversification != elimination of market/liquidity risk.
12. REIT, InvIT, AIF, PMS and NPS are different wrappers.

**Mains spine:** define claim/vehicle -> draw payoff/cash flow -> cite dated regulator -> explain
allocation benefit -> trace leverage/liquidity/conduct risk -> conclude with suitability and resilience.

**Boundary:** Topic 7 owns issue, venue, clearing, depository and settlement plumbing. Topic 9 owns fiscal
policy. Topic 8 owns product mechanics, derivative payoff, fund structure and investor risk.
