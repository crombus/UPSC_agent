# Economy Topic 7 — Money Market, Capital Market and Financial Instruments

**Current-law cutoff:** 9 September 2026  
**Central thesis:** classify every claim by purpose, maturity, issuer, security, venue, settlement and
regulator; market development is sound only when access, price discovery and resilience improve together.

```text
SAVINGS
  |
  +-- SHORT-TERM LIQUIDITY (generally <=1 year) -> MONEY MARKET
  |      call / notice / term | repo / TREPS | T-Bills / CMBs | CP / CD / bills
  |
  +-- MEDIUM-LONG FINANCE / OWNERSHIP -> CAPITAL MARKET
         dated G-Secs / SDLs | corporate bonds | equity / hybrids
                               |
                       PRIMARY ISSUE
                               |
                    SECONDARY LIQUIDITY
                               |
       TRADE -> CLEAR / NOVATE -> DvP SETTLE -> DEPOSITORY OWNERSHIP RECORD
```

## 1. Decode the short-funds market

| Category | Decoded rule |
|---|---|
| Call money | Unsecured overnight borrowing/lending |
| Notice money | Unsecured, above one day and through 14 days |
| Term money | Unsecured, above 14 days and through one year |
| Source | RBI Call, Notice and Term Money Markets Directions, 1 April 2021; updated 8 June 2023 |
| Repo | Collateralised sale plus agreed repurchase; reverse repo for cash lender |
| TREPS | Tri-Party Repo Dealing and Settlement; current successor to CBLO |
| CCIL | Clearing Corporation of India Limited; CCP in covered G-Sec/repo markets |
| Repo source | RBI Repo Directions, 11 November 2025; market repo, excluding RBI LAF/MSF repo |

**LAF = Liquidity Adjustment Facility; MSF = Marginal Standing Facility; CCP = Central Counterparty.**
**RBI = Reserve Bank of India; CBLO = Collateralised Borrowing and Lending Obligation.**

## 2. Instruments and current thresholds

| Instrument | Exam definition | Dated current rule |
|---|---|---|
| T-Bill | Government of India discount security; 91, 182 or 364 days | RBI G-Sec Primer; General Notification 26 March 2025 |
| CMB | Cash Management Bill below 91 days for temporary GoI cash mismatch | Not a standard fourth T-Bill |
| CP | Commercial Paper: unsecured promissory-note money-market instrument | RBI Directions 3 January 2024, effective 1 April 2024 |
| CP limits | 7 days-one year; minimum Rs 5 lakh; minimum rating A3 | Primary settlement no later than T+4; OTC T+0/T+1 |
| Short-term NCD | Non-Convertible Debenture: secured under this framework; 90 days-one year | Same 2024 Directions |
| CD | Certificate of Deposit: negotiable unsecured money-market instrument | RBI Directions 4 June 2021, effective 7 June 2021 |
| Bank CD limits | 7 days-one year; demat; minimum Rs 5 lakh | Primary T+1; OTC T+0/T+1 through DvP |
| Commercial bill | Trade receivable evidenced by a bill; discount/rediscount creates finance | Not a Treasury Bill |

**SCB = Scheduled Commercial Bank; RRB = Regional Rural Bank; SFB = Small Finance Bank; AIFI =
All-India Financial Institution; OTC = Over the Counter; DvP = Delivery versus Payment.**
**GoI = Government of India; A3 is a credit-rating grade, not a count of rating agencies.**

## 3. Sovereign debt and valuation

```text
CENTRAL GOVERNMENT                     STATE GOVERNMENT
T-Bills (<1 year)                      SDLs (dated only)
CMBs (<91 days)                        no State T-Bills
Dated G-Secs (>=1 year)

yield rises -> discount rate rises -> fixed-cash-flow present value falls -> bond price falls
```

- **G-Sec:** Government Security.
- **SDL:** State Development Loan.
- **Coupon rate:** annual coupon / face value.
- **Current yield:** annual coupon / current price.
- **YTM:** Yield to Maturity; one discount rate equating price to all promised cash flows.
- **Duration:** weighted timing; modified duration approximates percentage price change for a small yield move.
- **Primary Dealer:** RBI-authorised dealer supporting G-Sec auctions and secondary market making.
- **Uniform-price auction:** all successful competitive bidders pay the cut-off.
- **Multiple-price auction:** successful bidders pay their accepted own-bid prices.
- **Non-competitive bid:** no price/yield quote; investor accepts auction-derived result.

## 4. Capital claims and issuance

| Term | Decode |
|---|---|
| Debt | Contractual creditor claim; promised service and priority |
| Equity | Residual ownership and loss-bearing claim |
| Hybrid | Combines contractual debt-like and equity-like features |
| Secured debenture | Charge over specified assets |
| Unsecured debenture | General-credit claim |
| Convertible debenture | Can become equity under stated terms |
| IPO | Initial Public Offer by an unlisted issuer |
| FPO | Further Public Offer by an already listed issuer |
| Rights issue | Offer to existing holders on record date |
| Private placement | Offer to selected persons within legal conditions |
| QIP | Qualified Institutions Placement by a listed issuer to QIBs |
| QIB | Qualified Institutional Buyer |
| Fresh issue | Proceeds ordinarily reach company |
| OFS | Offer for Sale; proceeds ordinarily reach selling holder |

**ICDR = SEBI Issue of Capital and Disclosure Requirements Regulations; current amendments through
21 March 2026. SEBI = Securities and Exchange Board of India.**

## 5. Venue, clearing, settlement and ownership

| Link | Function | Trap |
|---|---|---|
| Exchange | Recognised organised venue | Not final custodian |
| OTC | Bilateral or platform-facilitated non-exchange execution | Not automatically unregulated |
| ETP | Electronic Trading Platform | Electronic does not always mean exchange |
| Clearing corporation | Calculates obligations; can act as CCP | Not issuer or market-price guarantor |
| Novation | CCP becomes buyer to seller and seller to buyer | Concentrates infrastructure risk |
| DvP | Links final securities delivery and corresponding payment | Reduces principal risk, not every failure |
| Depository | Electronic holdings and transfer records | Registered owner only for transfer |
| DP | Depository Participant; investor-facing intermediary | Not the regulator |
| Beneficial owner | Investor with substantive rights/liabilities | Depository does not take economic ownership |

**Depositories Act 1996, section 10:** the depository is registered owner only to effect transfer; the
beneficial owner retains all rights and liabilities.

## 6. NDS-OM and current settlement

- **NDS-OM:** Negotiated Dealing System-Order Matching, RBI-regulated anonymous G-Sec platform.
- **SGL:** Subsidiary General Ledger account used to hold Government securities.
- Directions dated 7 February 2025 and updated 27 April 2026 define:
  - **Direct access:** member settles in own SGL/funds arrangements.
  - **Indirect access:** another entity assumes settlement responsibility.
  - **Stock Broker Connect:** access for eligible individual demat clients through brokers.
- Equity cash market: **T+1 standard**, phased transition completed January 2023.
- **Optional T+0** beta introduced 28 March 2024; expanded framework dated 10 December 2024.
- SEBI circular 30 October 2025 further extended the Qualified Stock Broker implementation timeline
  without a replacement date in that circular. **T+0 is optional same-day, not universal instantaneous.**

## 7. Regulator map

```text
RBI
  money market | G-Secs | foreign exchange | payment systems | regulated entities

SEBI
  public/listed securities | exchanges | clearing corporations | depositories
  intermediaries | disclosure | market conduct

ONE TRANSACTION MAY INVOLVE BOTH PERIMETERS + A VENUE + CCP + DEPOSITORY
```

**NSE = National Stock Exchange; BSE = BSE Limited; NSDL = National Securities Depository Limited;
CDSL = Central Depository Services (India) Limited.**

## 8. Functions, transmission and stability

```text
policy/liquidity expectations -> overnight rates -> T-Bills -> G-Sec curve
                              -> bank and corporate funding -> investment

PRIMARY: capital formation
SECONDARY: liquidity + price discovery
INFRASTRUCTURE: netting + DvP + ownership integrity
```

Qualifications: fiscal supply, inflation expectations, global yields, term premium, credit spreads and
liquidity can weaken transmission. Faster settlement reduces open exposure but increases prefunding and
operational-readiness demands.

## 9. Prelims traps

1. Money market is not risk-free.
2. Repo is collateralised; call money is unsecured.
3. Market repo is not automatically the RBI policy repo.
4. States issue SDLs, not T-Bills.
5. CP is unsecured; short-term NCD is secured under the 2024 definition.
6. CD is negotiable bank funding, not an ordinary withdrawable deposit.
7. Coupon, current yield and YTM differ.
8. Price and yield move inversely for fixed cash flows.
9. IPO/FPO does not reveal fresh issue versus OFS.
10. QIP is one private-placement route.
11. Clearing, settlement, custody and regulation differ.
12. T+0 is optional same-day, not universal real-time settlement.

## 10. PYQ route and Mains spine

- 2024 official routes: CBLO/TREPS; eligible corporate-bond/G-Sec investors; financial-instrument
  classification; sovereign Treasury debt.
- 2025 official route: RTGS versus NEFT settlement.
- 2018-2023 routed questions retain: **Answer withheld pending official UPSC key.**

**Mains spine:** definition -> classification -> named dated framework -> market function -> risk /
boundary -> resilient-inclusion conclusion.

**Topic boundary:** detailed derivatives, mutual funds, exchange-traded funds, alternative investment
funds and hedging strategy belong to Topic 8.
