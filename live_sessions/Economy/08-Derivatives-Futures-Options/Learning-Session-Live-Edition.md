# Derivatives, Futures and Options - Live Session Edition

> Source: completed guided session from the current Copilot conversation.
> Substantive teaching, visuals, questions, explanations and remediation are preserved.
> Navigation-only turns, tool logs, tracker operations and unrelated administrative chatter are excluded.

# Derivatives, Futures and Options

## Roadmap

| # | Subtopic |
|---:|---|
| 1 | Derivative foundations: underlying asset, long/short positions, hedging and speculation |
| 2 | Forward contracts: price locking, settlement and counterparty risk |
| 3 | Futures: standardisation, margins, leverage and daily mark-to-market |
| 4 | Options: calls, puts, strike price, premium and expiry |
| 5 | Four payoff positions: long call, short call, long put and short put |
| 6 | Moneyness, intrinsic value, time value and break-even |
| 7 | Practical hedging: farmers, importers, exporters and equity investors |
| 8 | Basis risk, option-writing risk, swaps, PYQs and final synthesis |

**Method:** numerical examples → payoff diagrams → adaptive MCQs.
**Estimated effort:** 8 focused lessons.

Type **Start** to begin derivative foundations.

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Economy 08 Basic and Advanced files queried
🔍 **CA Search:** “Indian derivatives, hedging, leverage and retail risk, March–September 2026”
📰 **CA Found:** SEBI continued tightening position-limit and risk controls in derivatives markets, reflecting concern over leverage, excessive speculation and retail losses
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 1/8 | Stage: Foundation | Subtopic: What Is a Derivative?**

## 🖼️ Basic idea

```text
             UNDERLYING
     Share / index / wheat / gold
      currency / bond / interest rate
                  │
                  │ determines value
                  ▼
             DERIVATIVE
     Futures / option / forward / swap
```

A **derivative is a financial contract whose value depends on—or is derived from—another asset, price, rate or index.**

> 🔑 The underlying is the reference; the derivative is the contract built around it.

## 1. Underlying versus derivative

| Underlying | Possible derivative |
|---|---|
| Reliance share | Reliance futures or options |
| Nifty 50 index | Nifty futures or options |
| Wheat | Wheat futures |
| Gold | Gold futures/options |
| US dollar–rupee rate | Currency forward/future/option |
| Government bond | Interest-rate future |
| Interest rate | Interest-rate swap |

### Example

```text
Wheat                 = physical commodity
Wheat futures         = contract linked to wheat price

Company share         = ownership in company
Share option          = contract linked to share price

US dollar             = currency
USD-INR forward       = contract linked to exchange rate
```

Buying a derivative does not necessarily mean owning the underlying asset.

## 2. Why derivatives exist

Businesses and investors face uncertain future prices.

```text
Farmer fears wheat price will fall
Importer fears dollar will rise
Airline fears fuel price will rise
Investor fears share portfolio will fall
Bank fears interest rates will change
```

A derivative allows this price risk to be transferred or reshaped.

```text
Party wanting less risk
          ↓ transfers exposure
Derivative market
          ↓
Party willing to accept exposure
```

Risk is not destroyed; it is transferred between parties.

## 3. Essential contract elements

Most derivatives specify:

| Element | Meaning |
|---|---|
| Underlying | Asset/rate determining contract value |
| Quantity | Amount covered |
| Agreed price/strike | Relevant contractual price |
| Expiry/maturity | Date on which contract ends |
| Settlement | Physical delivery or cash payment |
| Counterparties | Parties assuming opposite positions |

## 4. Long and short positions

For a simple linear contract such as a forward or future:

### Long position

The long party benefits when the underlying price rises.

```text
Agreed purchase price = ₹100
Market price at expiry = ₹130
                       ↓
Long benefits by ₹30
```

### Short position

The short party benefits when the underlying price falls.

```text
Agreed selling price = ₹100
Market price at expiry = ₹70
                       ↓
Short benefits by ₹30
```

## 🖼️ Opposite payoff

```text
Underlying price rises
     Long gains ←→ Short loses

Underlying price falls
     Long loses ←→ Short gains
```

This simple symmetry applies directly to forwards and futures. Options have asymmetrical rights and obligations, which we will study separately.

## 5. Hedging

A hedge uses a derivative to reduce an existing economic risk.

### Farmer example

A farmer expects to harvest wheat after three months and fears a price decline.

```text
Existing exposure:
Farmer benefits if wheat price rises
Farmer suffers if wheat price falls

Hedge:
Take a derivative position that benefits when wheat falls
```

If the wheat price falls:

- farmer receives less in the physical market;
- derivative position gains;
- the gain offsets part of the physical-market loss.

### Importer example

An Indian importer must pay $1 million after three months.

```text
Risk: Rupee may depreciate
      ₹83/$ → ₹88/$
             ↓
Dollar payment becomes costlier
```

The importer can lock or hedge the future exchange rate through a currency derivative.

> 🔑 **Hedging begins with a pre-existing risk.**

## 6. Speculation

A speculator deliberately takes price risk to earn a profit.

```text
No wheat crop
No dollar payment
No existing portfolio exposure
             ↓
Trader takes derivative position
because a price movement is expected
```

Example: A trader buys Nifty futures solely because they expect the index to rise.

| Hedger | Speculator |
|---|---|
| Already faces underlying risk | Intentionally takes new risk |
| Seeks greater certainty | Seeks profit from price movement |
| Derivative offsets exposure | Derivative creates exposure |
| Accepts reduced upside for protection | Accepts losses if prediction fails |

The same futures contract can be used by one party for hedging and another for speculation.

## 7. Arbitrage

Arbitrage exploits inconsistent prices in related markets.

Example:

```text
Fair value of asset: ₹100
Same economic exposure available elsewhere: ₹105
                  ↓
Buy cheaper exposure
Sell costlier exposure
                  ↓
Attempt near-riskless profit
```

Arbitrage activity helps bring related prices back into alignment.

True risk-free arbitrage is difficult because of:

- transaction costs;
- taxes;
- funding costs;
- execution delays;
- settlement risk;
- market impact.

## 8. Cash versus physical settlement

### Physical settlement

The underlying asset is delivered.

```text
Seller delivers commodity/shares
Buyer makes payment
```

### Cash settlement

No physical asset is delivered. The parties exchange the price difference.

```text
Agreed index level: 20,000
Final index level: 21,000
Difference settled in cash
```

An index itself cannot ordinarily be physically delivered, so index derivatives are commonly cash-settled.

## 9. Derivatives do not require a price rise

Investors can construct exposure to:

- rising prices;
- falling prices;
- volatility;
- interest-rate changes;
- exchange-rate movements;
- relative price differences.

This differs from ordinary cash-market investment, where profit is often associated mainly with buying an asset and hoping its price rises.

## 10. Leverage preview

Derivatives often require only margin or premium rather than the full underlying value.

```text
Underlying exposure = ₹10 lakh
Margin paid         = ₹1 lakh
                     ↓
₹1 lakh controls ₹10 lakh exposure
```

This is leverage.

If the underlying moves 5%:

\[
5\%\times ₹10\text{ lakh}=₹50,000
\]

That ₹50,000 equals 50% of the ₹1 lakh margin.

Leverage magnifies both gains and losses.

## 11. Economic usefulness

Derivatives can support:

- risk management;
- price discovery;
- future-price planning;
- market liquidity;
- portfolio management;
- lower uncertainty for businesses.

But poorly controlled derivatives can create:

- excessive leverage;
- margin calls;
- speculative losses;
- counterparty exposure;
- market manipulation;
- systemic contagion.

## 12. Current-affairs anchor

✅ **Fact:** SEBI regulates exchange-traded securities and commodity derivatives, while RBI governs specified interest-rate, currency and OTC derivative activity within its jurisdiction.

✅ **Fact:** Position limits and margins are used to contain excessive concentration and default risk.

⚠️ **Inference:** High retail losses arise partly because leveraged derivatives are treated as simple directional bets rather than risk-management contracts.

```text
Small margin
     ↓
Large exposure
     ↓
Small price error
     ↓
Large percentage loss
```

## UPSC traps

1. Every derivative holder owns the underlying asset — incorrect.
2. Every derivative reduces risk — incorrect.
3. Hedging and speculation use completely different contracts — incorrect.
4. Risk disappears when hedged — incorrect; it is transferred or offset.
5. Short positions always mean borrowing money — incorrect.
6. Index derivatives must physically deliver the index — impossible.
7. Margin is the total economic exposure — incorrect.
8. Derivatives have no real-economy use — incorrect.

## Revision notes

1. A derivative derives value from an underlying.
2. Underlyings include assets, indices, currencies and rates.
3. A derivative is a contract, not necessarily ownership.
4. Long linear positions benefit from rising prices.
5. Short linear positions benefit from falling prices.
6. Hedgers reduce pre-existing exposure.
7. Speculators deliberately assume exposure.
8. Arbitrage exploits price inconsistencies.
9. Settlement may be physical or cash-based.
10. Risk is transferred, not destroyed.
11. Margin can create leverage.
12. Leverage magnifies both gains and losses.

### MCQ 1

Consider the following statements:

1. A person must own the underlying asset before entering every derivative contract.
2. A hedger uses derivatives to reduce an already existing economic exposure.
3. A speculator can use the same derivative contract that another participant uses for hedging.
4. Cash-settled derivatives necessarily require physical delivery of the underlying.

Which statements are correct?

**A. 1 and 2 only**
**B. 1, 3 and 4 only**
**C. 2 and 3 only**
**D. 2, 3 and 4 only**

---

**Correct answer: C. 2 and 3 only**

- **1 — Incorrect:** Derivatives can be entered without owning the underlying asset.
- **2 — Correct:** Hedging reduces an existing price, interest-rate or currency risk.
- **3 — Correct:** The same contract may hedge one participant’s risk while enabling another to speculate.
- **4 — Incorrect:** Cash-settled derivatives settle through the price difference, not physical delivery.

---

**Learner question / doubt**

> shal we to next mcq

### MCQ 2

Consider the following statements:

1. The value of a derivative is linked to an underlying asset or variable.
2. Derivatives can be based on interest rates, currencies and market indices.
3. Every derivative contract guarantees profits to one of its parties.
4. Derivatives may facilitate both risk transfer and price discovery.

Which statements are correct?

A. 1 and 2 only
B. 2 and 3 only
C. 1, 3 and 4 only
D. 1, 2 and 4 only

---

✅ **Correct: D — 1, 2 and 4 only**

Statement 3 is incorrect because derivatives transfer risk; they do not guarantee profit.

### MCQ 3

Which situation best represents **hedging** through derivatives?

A. An importer buys a currency future to protect against rupee depreciation.
B. A trader buys an index future solely because they expect the market to rise.
C. An investor purchases shares for long-term dividends.
D. A company issues bonds to finance a factory.

---

✅ **Correct: A**

The importer already faces currency risk; buying currency futures offsets potential losses from rupee depreciation.

**MCQ loop cleared: 2 consecutive correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—local Economy 08 Markdown and *Indian Economy* reference PDF
🔍 **CA Search:** “India derivatives futures forwards RBI SEBI April–September 2026”
📰 **CA Found:** RBI issued the **Credit Derivatives Directions, 2026** on **25 June 2026**, covering OTC and exchange-traded contracts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 2/8 | Stage: Foundation | Subtopic: Forwards vs Futures**

## 🖼️ Visual comparison

| Feature | Forward | Future |
|---|---|---|
| Trading venue | OTC/private agreement | Recognised exchange |
| Contract terms | Customised | Standardised |
| Quantity/date/quality | Negotiable | Exchange-defined |
| Counterparty | Known contracting party | Clearing corporation intervenes |
| Margin | Depends on agreement | Initial and maintenance margin |
| Profit/loss settlement | Usually at maturity | Daily mark-to-market |
| Liquidity | Generally lower | Generally higher |
| Counterparty risk | Relatively high | Reduced through clearing |
| Exit | Requires cancellation or opposite agreement | Offset through opposite exchange trade |
| Obligation | Both parties | Both parties |

```text
FORWARD
Buyer ───── customised private contract ───── Seller
              Direct counterparty risk

FUTURE
Buyer ── Broker ── Clearing Corporation ── Broker ── Seller
                      ↑
              margin + daily MTM
```

*A futures exchange converts a customised bilateral promise into a standardised, collateralised and regularly settled contract.*

## Core concept

### 1. Forward contract

A **forward** is a private agreement to buy or sell an underlying asset at a predetermined price on a future date.

**Example:** An Indian importer must pay **$1 million after three months**. It enters a forward contract with a bank to lock the rupee–dollar exchange rate.

- If the rupee depreciates, the forward protects the importer.
- If the rupee appreciates, the importer cannot ordinarily abandon the contract merely because the market rate is better.

### 2. Futures contract

A **future** creates the same basic two-sided obligation, but it is:

- exchange-traded;
- standardised;
- backed by margins;
- marked to market regularly; and
- supported by a clearing corporation.

> 🔑 **Mnemonic:** **FUTURES = Fixed Units, Transparent Exchange, Regular Settlement**

## Margin and mark-to-market

```text
Open futures position
        ↓
Deposit initial margin
        ↓
Market price changes daily
        ↓
Profit credited / Loss debited
        ↓
Margin falls too low?
        ↓
Additional margin required
```

**Margin is not the purchase price** of the underlying. It is performance security against potential losses.

### Example

You agree through a futures contract to buy an index at **20,000**.

| Closing level | Buyer’s position |
|---:|---|
| 20,300 | Gain of 300 points |
| 19,700 | Loss of 300 points |

The gain or loss is adjusted through mark-to-market settlement.

## Why clearing matters

The clearing corporation effectively becomes:

- buyer to every seller; and
- seller to every buyer.

It reduces the risk that one original party’s failure directly prevents settlement. However, it cannot eliminate:

- market risk;
- leverage-related losses;
- liquidity risk; or
- basis risk.

## Forward versus futures hedging

| Economic exposure | Possible hedge |
|---|---|
| Importer fears rupee depreciation | Buy USD forward/future |
| Exporter fears rupee appreciation | Sell USD forward/future |
| Farmer fears crop-price decline | Sell commodity futures |
| Food processor fears input-price rise | Buy commodity futures |

✅ **Fact:** Both forwards and futures impose obligations on both parties.
✅ **Fact:** Neither requires prior ownership of the underlying asset.
✅ **Fact:** Settlement may be physical or cash-based, depending on contract design.
⚠️ **Inference:** Futures are generally safer operationally than bilateral forwards, but leverage can still produce substantial losses.

## CA anchor

✅ RBI’s **Credit Derivatives Directions, 2026** distinguish between OTC and exchange-traded derivatives.

- OTC products retain contractual flexibility.
- Exchange-traded products gain standardisation and clearing support.
- The same institutional distinction applies to understanding forwards and futures.

## UPSC traps

1. **“A futures buyer has a right but no obligation.”**
   ❌ That describes an option buyer.

2. **“Margin is the price paid for purchasing the asset.”**
   ❌ Margin is performance security.

3. **“Futures eliminate all risk.”**
   ❌ Clearing reduces counterparty risk, not market risk.

4. **“Cash settlement means the derivative had no underlying.”**
   ❌ Its value still derives from the underlying; only settlement occurs through money.

## Revision notes

- Forward = customised OTC obligation.
- Future = standardised exchange-traded obligation.
- Both buyer and seller are bound.
- Futures require margin and mark-to-market settlement.
- Clearing corporations reduce counterparty risk.
- Margin is not an option premium or asset purchase price.
- Futures positions can normally be closed through an opposite trade.
- Contracts may permit physical or cash settlement.
- Hedging does not guarantee profit; it reduces uncertainty.
- Basis risk arises when the hedge and actual exposure do not move identically.

### MCQ 1

Consider the following statements:

1. Forward contracts are necessarily traded on recognised stock exchanges.
2. Futures contracts generally involve standardisation and margin requirements.
3. Both forward and futures contracts create obligations for the contracting parties.
4. Clearing corporations eliminate the market risk arising from futures positions.

Which statements are correct?

A. 1 and 4 only
B. 2 and 3 only
C. 1, 2 and 3 only
D. 2, 3 and 4 only

---

✅ **Correct: B — Statements 2 and 3 only**

- **1 incorrect:** Forwards are generally private OTC contracts.
- **4 incorrect:** Clearing reduces counterparty risk, but market losses remain.

### MCQ 2

Regarding futures margins, consider the following statements:

1. Initial margin is a security deposit rather than the full purchase price.
2. Mark-to-market settlement periodically recognises gains and losses.
3. A margin requirement guarantees that a participant cannot suffer losses.
4. Additional margin may be demanded when losses substantially reduce the available margin.

Which statements are correct?

A. 1 and 2 only
B. 2, 3 and 4 only
C. 1, 2 and 4 only
D. 1, 3 and 4 only

---

✅ **Correct: C — Statements 1, 2 and 4**

Margin provides loss protection to the clearing system but **does not guarantee that traders cannot lose money**.

**Subtopic 2 mastered: 2/2 correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—Economy 08 knowledge files and local economy PDF
🔍 **CA Search:** “SEBI index options investor risk April–September 2026”
📰 **CA Found:** SEBI published an **August 2026 consultation paper on settlement and risk management**, continuing its scrutiny of derivatives-market risk
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 3/8 | Stage: Core | Subtopic: Options—Calls, Puts and Payoffs**

## 🖼️ Basic structure

```text
OPTION BUYER                           OPTION WRITER
Pays premium ───────────────────────► Receives premium
Gets a RIGHT                          Accepts an OBLIGATION
Maximum loss = premium                Loss may be substantial
Chooses whether to exercise           Must perform if exercised
```

> 🔑 **Mnemonic:** **Buyer has a Choice; Writer carries the Commitment.**

## 1. What is an option?

An **option** gives its buyer the **right, but not the obligation**, to buy or sell an underlying asset at a predetermined **strike price**, within or on a specified date.

The buyer pays an upfront **premium** to the option writer.

| Term | Meaning |
|---|---|
| Underlying | Asset or variable determining option value |
| Strike price | Predetermined transaction price |
| Premium | Price paid to acquire the option |
| Expiry | Last date of the option contract |
| Exercise | Using the contractual right |
| Writer | Person who sells the option and assumes the obligation |

## 2. Call option

A **call option** gives the buyer the right to **buy** the underlying at the strike price.

> 🔑 **Mnemonic:** **CALL = Call the asset towards you.**

### Example

You buy a Reliance call with:

- strike price: ₹3,000;
- premium: ₹100.

| Market price at expiry | Exercise? | Gross payoff | Net result after premium |
|---:|---|---:|---:|
| ₹3,400 | Yes | ₹400 | **₹300 profit** |
| ₹3,050 | Yes | ₹50 | **₹50 loss** |
| ₹2,800 | No | ₹0 | **₹100 loss** |

Notice that exercise does not automatically mean profit. The market price must exceed the strike by more than the premium.

```text
Call buyer benefits when price rises

Market price
    ↑
Above strike + premium ── Net profit
Between strike and break-even ── Exercise, but net loss
Below strike ── Do not exercise; lose premium
```

**Call buyer’s break-even:**

\[
\text{Strike price}+\text{Premium}
\]

## 3. Put option

A **put option** gives the buyer the right to **sell** the underlying at the strike price.

> 🔑 **Mnemonic:** **PUT = Put the asset onto someone else.**

### Example

You own shares currently worth ₹1,000 and buy a put with:

- strike price: ₹950;
- premium: ₹30.

| Market price at expiry | Put payoff | Net result from option |
|---:|---:|---:|
| ₹1,100 | ₹0 | −₹30 |
| ₹900 | ₹50 | +₹20 |
| ₹700 | ₹250 | +₹220 |

The put works like **price insurance**: it establishes a floor against a severe decline.

**Put buyer’s break-even:**

\[
\text{Strike price}-\text{Premium}
\]

## 4. Call versus put

| Feature | Call buyer | Put buyer |
|---|---|---|
| Right | Buy | Sell |
| Typical expectation | Price will rise | Price will fall |
| Hedging use | Protect against rising purchase cost | Protect an owned asset against decline |
| Maximum loss | Premium | Premium |
| Benefit increases when | Underlying rises | Underlying falls |

## 5. Buyer versus writer risk

| Participant | Maximum gain | Maximum loss |
|---|---|---|
| Call buyer | Theoretically unlimited | Premium |
| Put buyer | Substantial but bounded as price cannot fall below zero | Premium |
| Call writer without protection | Premium | Theoretically unlimited |
| Put writer | Premium | Substantial if price collapses |

This asymmetry is why saying **“options have limited risk”** is incomplete.

- It is generally true for the **option buyer**.
- It is not generally true for the **option writer**.

## 6. Hedging versus speculation

### Protective put

```text
Investor owns shares
        +
Buys a put option
        ↓
Share rises → benefits from share appreciation
Share falls → put limits downside
```

### Speculative call

A trader who owns no underlying shares may buy a call simply because they expect the price to rise. This is speculation, not hedging.

✅ **Fact:** Prior ownership of the underlying is not necessary for buying most exchange-traded options.
✅ **Fact:** The same option can be used for hedging or speculation.
⚠️ **Inference:** Limited buyer loss can encourage excessive speculation because the small premium controls a much larger notional exposure.

## 7. Option premium versus futures margin

| Option premium | Futures margin |
|---|---|
| Price paid for acquiring a right | Security deposited for contractual performance |
| Generally paid by option buyer | Required from futures participants |
| Buyer can lose the entire premium | Margin losses may require additional funds |
| Not ordinarily refundable merely because option expires unused | Margin balance is adjusted for gains and losses |

## Current-affairs anchor

✅ SEBI’s continuing review of derivatives settlement and risk management reflects concerns about leverage, expiry-day activity and investor protection.

⚠️ An option’s low premium should not be confused with low economic exposure. Trading apps such as Groww or Zerodha merely provide market access; they do not make an option position safe.

## UPSC traps

- A call buyer is **not obligated** to purchase.
- A put buyer need not necessarily own the asset when entering the contract.
- An unused option expires; the buyer still loses the premium.
- Option buyers have limited loss, but writers may face very large losses.
- Premium is not the same as futures margin.
- Cash settlement does not mean the contract lacks an underlying reference.

## Mini recap

```text
CALL → Right to BUY → Benefits from price rise
PUT  → Right to SELL → Benefits from price fall

BUYER  → Pays premium → Has choice
WRITER → Receives premium → Bears obligation
```

### MCQ 1

Consider the following statements:

1. A call-option buyer is obligated to buy the underlying asset at expiry.
2. The maximum loss of an option buyer is generally limited to the premium paid.
3. A put option can be used to protect an owned asset against a price decline.
4. The option writer receives the premium and assumes a contingent obligation.

Which statements are correct?

A. 1 and 2 only
B. 1, 3 and 4 only
C. 2 and 3 only
D. 2, 3 and 4 only

---

✅ **Correct: D — Statements 2, 3 and 4**

Statement 1 is incorrect: a call-option **buyer has a right, not an obligation**, to buy.

### MCQ 2

A share trades at ₹800. An investor buys a call option with a strike price of ₹850 for a premium of ₹20. At expiry, the share price is ₹900. Ignoring transaction costs, what is the buyer’s net result per share?

A. Profit of ₹30
B. Profit of ₹50
C. Loss of ₹20
D. Profit of ₹70

---

✅ **Correct: A — Profit of ₹30**

- Gross payoff: ₹900 − ₹850 = **₹50**
- Less premium: ₹50 − ₹20 = **₹30 net profit**

**Subtopic 3 mastered: 2/2 correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—Economy 08 Markdown and local economy reference
🔍 **CA Search:** “RBI swaps India April–September 2026”
📰 **CA Found:** RBI issued the **Credit Derivatives Directions, 2026** on **25 June 2026**, introducing a framework that includes **total return swaps on corporate bonds**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 4/8 | Stage: Core | Subtopic: Swaps and Cash-Flow Exchange**

## 🖼️ What is a swap?

```text
Party A                                      Party B
Fixed-rate payment ─────────────────────────►
                   ◄───────────────────────── Floating-rate payment

              Calculated on a notional amount
```

A **swap** is a derivative agreement under which two parties exchange specified cash-flow streams according to predetermined rules.

The underlying asset need not change ownership.

> 🔑 **Mnemonic:** **SWAP = Switch What A Party pays**

## 1. Interest-rate swap

An interest-rate swap commonly exchanges:

- fixed-rate interest payments; for
- floating-rate interest payments.

### Example

Two companies calculate payments on a **₹10 crore notional principal**:

| Company A pays | Company B pays |
|---|---|
| Fixed 7% | Floating benchmark + agreed spread |

If the floating rate becomes 8%, the net payment is normally based on the **1 percentage-point difference**.

```text
₹10 crore × (8% − 7%) = ₹10 lakh net difference
```

The ₹10 crore is generally **not exchanged**; it is the notional amount used for calculation.

### Why enter this swap?

- A borrower with floating-rate debt fears rising rates.
- It pays fixed and receives floating under the swap.
- The floating receipt offsets its floating loan payment.
- Its effective exposure becomes more predictable.

## 2. Currency swap

A currency swap exchanges cash flows denominated in different currencies.

```text
Indian company                    Foreign counterparty
Pays rupees ────────────────────►
             ◄────────────────── Pays dollars
```

Unlike a typical interest-rate swap, principal amounts in different currencies may be:

1. exchanged initially;
2. used for periodic interest payments; and
3. exchanged back at maturity.

### Purpose

- hedge exchange-rate risk;
- obtain financing in a required currency;
- manage foreign-currency liabilities.

## 3. Total return swap

A **total return swap (TRS)** transfers the complete economic performance of a reference asset without necessarily transferring its legal ownership.

```text
Total-return payer
    │
    ├── Interest/coupon
    ├── Capital gain
    └── Capital loss
            ↓
Total-return receiver
            │
            └── Pays fixed/floating financing return
```

✅ Under RBI’s 2026 Directions, a TRS can reference corporate bonds.

The receiver gains synthetic economic exposure to the bond without necessarily purchasing it directly.

## 4. Credit default swap

A CDS specifically transfers **credit risk**.

```text
Protection buyer ── periodic premium ──► Protection seller
Protection buyer ◄── payment after defined credit event ──
```

It resembles insurance economically, but it is a derivative governed by contractual and regulatory rules.

## Swap versus forward

| Forward | Swap |
|---|---|
| Usually one future transaction | Series of cash-flow exchanges |
| Fixes a future price or rate | Exchanges defined payment streams |
| Commonly settled at maturity | Payments may occur periodically |
| Example: currency forward | Example: fixed–floating interest swap |

A swap can therefore be understood as a **series of related forward-like commitments**.

## Risks

| Risk | Meaning |
|---|---|
| Counterparty risk | Other party may fail to pay |
| Market risk | Rates, currencies or asset values may move adversely |
| Basis risk | Swap payment may not perfectly match actual exposure |
| Liquidity risk | Position may be difficult or costly to terminate |
| Legal risk | Contract terms may be disputed or unenforceable |
| Complexity risk | User may misunderstand valuation or embedded leverage |

✅ **Fact:** Swaps exchange cash-flow streams rather than necessarily transferring assets.
✅ **Fact:** Interest-rate swaps commonly use a notional principal without exchanging it.
✅ **Fact:** Currency swaps may involve exchanging principal in different currencies.
⚠️ **Inference:** A swap lowers risk only when its amount, maturity and reference rate adequately match the underlying exposure.

## UPSC traps

- “Swap” does not necessarily mean exchanging ownership of two assets.
- Notional principal is not always physically transferred.
- Interest-rate and currency swaps are not identical.
- A TRS can transfer economic exposure without legal ownership.
- A swap used without an existing exposure can become speculation.

## Mini recap

```text
Interest-rate swap → fixed cash flow ↔ floating cash flow
Currency swap      → currency A ↔ currency B
Total return swap  → asset performance ↔ financing return
Credit default swap→ premium ↔ credit-event protection
```

### MCQ 1

Consider the following statements:

1. In a conventional interest-rate swap, fixed and floating interest payments may be calculated on a notional principal.
2. The notional principal must always be physically exchanged between the parties.
3. Currency swaps may involve the exchange and later re-exchange of principal amounts in different currencies.
4. Every swap necessarily transfers legal ownership of the underlying asset.

Which statements are correct?

A. 1 and 2 only
B. 1 and 3 only
C. 2, 3 and 4 only
D. 1, 3 and 4 only

---

✅ **Correct: B — Statements 1 and 3 only**

- A notional amount may only provide the calculation base.
- Swaps exchange economic cash flows, not necessarily legal ownership.

### MCQ 2

Consider the following statements:

1. A total return swap necessarily transfers legal ownership of the reference bond.
2. A credit default swap requires the protection buyer to make periodic premium payments.
3. A total return swap can transfer coupon income and changes in the value of a reference asset.
4. A swap can increase risk when used speculatively without a matching underlying exposure.

Which statements are correct?

A. 1 and 2 only
B. 1, 3 and 4 only
C. 2, 3 and 4 only
D. 2 and 3 only

---

❌ **Incorrect. Correct answer: C — Statements 2, 3 and 4**

Statement 1 is false: a total return swap transfers the asset’s **economic performance**, not necessarily its legal ownership.

### Remedial MCQ 3

Which situation correctly describes a swap?

A. An investor purchases shares and becomes their legal owner.
B. An option buyer pays a premium for the right to buy an asset.
C. A futures buyer deposits margin for an exchange-traded obligation.
D. A floating-rate borrower exchanges floating payments for fixed payments to stabilise borrowing costs.

---

✅ **Correct: D**

The borrower uses an interest-rate swap to convert an uncertain floating-rate exposure into a more predictable fixed-rate exposure.

**Consecutive correct: 1/2**

### MCQ 4

Which statement best distinguishes a **currency swap** from a conventional interest-rate swap?

A. A currency swap may exchange principal and interest in different currencies.
B. A currency swap cannot be used for hedging.
C. An interest-rate swap always transfers ownership of the underlying loan.
D. An interest-rate swap gives only one party a contractual obligation.

---

❌ **Incorrect. Correct answer: A**

A currency swap may exchange **principal and interest in two currencies**. An interest-rate swap normally exchanges fixed and floating interest streams, with obligations on both parties.

**Consecutive correct reset: 0/2**

### Remedial MCQ 5

Match the derivative with its principal function:

1. Interest-rate swap — exchange fixed and floating payment streams
2. Currency swap — exchange cash flows denominated in different currencies
3. Total return swap — necessarily transfer legal ownership of the reference asset
4. Credit default swap — transfer credit-event risk

Which pairs are correctly matched?

A. 1 and 3 only
B. 1, 2 and 4 only
C. 2, 3 and 4 only
D. 1, 2, 3 and 4

---

✅ **Correct: B — Pairs 1, 2 and 4**

Pair 3 is incorrect: a total return swap transfers **economic performance**, not necessarily legal ownership.

**Consecutive correct: 1/2**

### MCQ 6

A company has a floating-rate loan but expects interest rates to rise. Which arrangement most directly hedges this exposure?

A. Receive fixed interest and pay floating interest
B. Buy an equity put option
C. Pay fixed interest and receive floating interest
D. Sell a currency future without foreign-currency exposure

---

✅ **Correct: C**

The floating-rate receipt offsets the floating-rate loan payment, while the company pays a predictable fixed rate.

**Subtopic 4 mastered after remediation: 2 consecutive correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—Economy 08 foundational and advanced files
🔍 **CA Search:** “SEBI derivatives hedging speculation risk management April–September 2026”
📰 **CA Found:** SEBI issued an **August 2026 consultation paper on settlement and risk management**, reflecting continuing concern over derivatives leverage and market stability
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 5/8 | Stage: Core | Subtopic: Hedging, Speculation and Arbitrage**

## 🖼️ Purpose determines the classification

```text
Does the participant already face economic risk?
                  │
           ┌──────┴──────┐
          Yes            No
           │              │
Derivative offsets   Is a price discrepancy
that exposure?       being exploited?
     │                     │
   HEDGE              ┌────┴────┐
                     Yes        No
                      │          │
                 ARBITRAGE  SPECULATION
```

The derivative itself does not reveal its purpose. The participant’s **existing exposure and objective** determine the classification.

## 1. Hedging

A hedger uses derivatives to reduce an already existing economic exposure.

### Short hedge

Used when someone owns or will produce an asset and fears its price will fall.

```text
Farmer expects to sell wheat later
                 +
         Sells wheat futures
                 ↓
Wheat price falls → cash-market loss
                 ↔ futures-market gain
```

### Long hedge

Used when someone will purchase an asset and fears its price will rise.

```text
Airline will purchase fuel later
                 +
          Buys fuel futures
                 ↓
Fuel price rises → higher physical cost
                ↔ futures gain
```

| Exposure | Appropriate hedge |
|---|---|
| Exporter fears rupee appreciation | Sell foreign-currency forward/future |
| Importer fears rupee depreciation | Buy foreign-currency forward/future |
| Shareholder fears price decline | Buy put option |
| Borrower fears interest-rate rise | Pay-fixed, receive-floating swap |

> 🔑 **Mnemonic:** **Own or produce → short hedge; need to purchase → long hedge.**

## 2. Hedging does not guarantee profit

Suppose a farmer expects to sell wheat at ₹2,500 but locks a futures price of ₹2,400.

- If the market falls to ₹2,100, the futures hedge protects the farmer.
- If the market rises to ₹2,800, the farmer loses the opportunity to receive the full higher price.

The objective is **certainty**, not maximum profit.

## 3. Basis risk

\[
\text{Basis}=\text{Spot price}-\text{Futures price}
\]

An ideal hedge requires the derivative and actual exposure to move together. If they do not, some risk remains.

Causes include:

- different commodity quality;
- different location;
- different maturity;
- imperfect contract size;
- changing spot–futures relationship.

```text
Actual exposure ≠ Exact derivative match
                       ↓
                  Basis risk
```

### Over-hedging

Exposure = ₹10 lakh, but derivative position = ₹15 lakh.

- ₹10 lakh offsets the exposure.
- The remaining ₹5 lakh effectively becomes speculation.

## 4. Speculation

A speculator creates or enlarges risk to profit from an expected price movement.

### Example

A trader who owns no Reliance shares buys Reliance futures because they expect the price to rise.

- This is not hedging.
- It is a leveraged directional position.
- Losses may exceed the initial margin deposited.

Speculators may contribute liquidity and absorb risk transferred by hedgers, but excessive leverage can amplify volatility and losses.

## 5. Arbitrage

An arbitrageur attempts to profit from inconsistent prices for the same or economically equivalent asset.

### Example

```text
Spot-market price                    = ₹1,000
Fair futures price                   = ₹1,030
Actual futures price                 = ₹1,100
                                       ↓
Buy relatively cheap spot asset
Sell relatively expensive future
                                       ↓
Prices converge toward expiry
```

The transactions must normally be coordinated so that one position offsets the other.

> 🔑 **Mnemonic:** **Arbitrage = Buy cheap and sell expensive simultaneously.**

Arbitrage is theoretically low-risk, but real-world risks include:

- transaction costs;
- execution delay;
- funding costs;
- liquidity constraints;
- model error; and
- settlement failure.

## Comparison

| Participant | Existing exposure? | Objective | Typical risk effect |
|---|---:|---|---|
| Hedger | Yes | Reduce uncertainty | Reduces existing risk |
| Speculator | Usually no | Profit from direction | Creates or enlarges risk |
| Arbitrageur | Not essential | Exploit price inconsistency | Helps align prices |

## Economic role

```text
Hedgers transfer risk
          ↓
Speculators accept directional risk
          ↓
Arbitrageurs connect market prices
          ↓
Liquidity + price discovery
```

✅ **Fact:** The same futures contract may hedge one participant and enable another to speculate.
✅ **Fact:** Hedging reduces exposure but may sacrifice favourable price movements.
✅ **Fact:** Arbitrage encourages convergence between related prices.
⚠️ **Inference:** Derivatives benefit the economy when risk transfer and price discovery dominate excessive leverage and unsuitable retail speculation.

## UPSC traps

- A hedger need not earn a derivative profit.
- A profitable trade is not automatically arbitrage.
- Arbitrage requires a price inconsistency, not merely a prediction.
- Owning an asset does not make every derivative position a hedge.
- A hedge larger than the exposure can create speculative risk.

## Mini recap

```text
HEDGE      → Reduce existing exposure
SPECULATE  → Take directional exposure
ARBITRAGE  → Exploit inconsistent prices
```

### MCQ 1

Consider the following statements:

1. A hedging transaction must independently produce a profit to be successful.
2. Speculation involves creating or enlarging exposure based on an expected price movement.
3. Arbitrage seeks to exploit price inconsistencies between related markets or instruments.
4. The same derivative contract may be used by one participant for hedging and another for speculation.

Which statements are correct?

A. 1 and 2 only
B. 1, 3 and 4 only
C. 2 and 3 only
D. 2, 3 and 4 only

---

✅ **Correct: D — Statements 2, 3 and 4**

Statement 1 is incorrect: a hedge succeeds by reducing the overall exposure’s uncertainty, even if the derivative leg itself incurs a loss.

### MCQ 2

An Indian importer must pay US dollars after three months and fears rupee depreciation. Which transaction most directly represents hedging?

A. Selling US-dollar futures
B. Buying US-dollar futures
C. Buying an unrelated equity call option
D. Selling Indian equity-index futures without equity exposure

---

✅ **Correct: B**

The importer will need dollars later. Buying dollar futures protects against dollars becoming costlier due to rupee depreciation.

**Subtopic 5 mastered: 2/2 correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—Economy 08 foundational and advanced files
🔍 **CA Search:** “SEBI derivatives margins, clearing and default protection 2026”
📰 **CA Found:** From **16 March 2026**, SEBI required commodity-derivative clearing corporations to stress-test their Settlement Guarantee Funds assuming simultaneous default of at least **three highest-exposure clearing members**, replacing the earlier two-member assumption
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 6/8 | Stage: Advanced | Subtopic: Margins, Clearing and Leverage**

## 🖼️ Complete transaction structure

```text
Trader A                    CLEARING                    Trader B
(Long)                   CORPORATION                   (Short)
   │                           │                           │
   ├── initial margin ────────►│◄────── initial margin ──┤
   │                           │                           │
   │◄── daily gain/loss ──────►│◄──── daily gain/loss ──►│
   │                           │                           │
   └──── must perform ────────►│◄────── must perform ────┘

Clearing corporation becomes:
• seller to every buyer
• buyer to every seller
```

## 1. Margin

**Margin** is collateral or performance security deposited to cover potential derivative losses.

It is **not**:

- a down payment on the underlying asset;
- the option premium; or
- the maximum possible loss.

### Types of margin

| Margin | Purpose |
|---|---|
| Initial margin | Collected when the position is opened |
| Maintenance margin | Minimum balance that must remain available |
| Variation/MTM margin | Covers losses arising from price changes |
| Additional margin | Imposed during higher volatility or concentrated risk |

> 🔑 **Mnemonic:** **Initial enters; maintenance sustains; variation settles.**

## 2. Mark-to-market settlement

Futures gains and losses are recognised regularly instead of being postponed entirely until expiry.

### Example

You buy a futures contract covering **100 shares at ₹1,000**.

- Notional value = ₹1,00,000
- Initial margin = ₹15,000

| Closing price | Daily movement | Buyer’s MTM |
|---:|---:|---:|
| ₹1,020 | +₹20 × 100 | +₹2,000 |
| ₹980 | −₹40 × 100 | −₹4,000 |
| ₹950 | −₹30 × 100 | −₹3,000 |

Losses are debited from the margin account. If available margin falls below the required level, the trader receives a **margin call**.

```text
Market moves adversely
          ↓
MTM loss debited
          ↓
Margin falls below requirement
          ↓
Deposit additional funds
          ↓
Failure to pay → position may be closed
```

## 3. Leverage

Leverage means controlling a large notional exposure with comparatively little upfront capital.

Using the previous example:

\[
\text{Leverage}=\frac{₹1,00,000}{₹15,000}\approx6.67
\]

A **5% fall** in the underlying causes:

\[
₹1,00,000\times5\%=₹5,000
\]

Relative to the ₹15,000 margin:

\[
\frac{₹5,000}{₹15,000}=33.3\%
\]

Thus, a 5% market movement produces a 33.3% loss relative to the initial capital deposited.

```text
Small capital
     ↓
Large market exposure
     ↓
Small price movement
     ↓
Large percentage gain OR loss
```

> 🔑 **Leverage magnifies direction; it does not create accuracy.**

## 4. Clearing corporation

Through **novation**, the clearing corporation interposes itself between the original parties:

```text
Original arrangement:
Buyer ↔ Seller

After novation:
Buyer ↔ Clearing corporation ↔ Seller
```

If the seller defaults, the buyer does not ordinarily pursue that seller directly. The clearing corporation manages settlement according to its rules and resources.

### Main functions

- calculate and collect margins;
- mark positions to market;
- net obligations;
- monitor member exposures;
- manage settlement;
- close defaulting positions; and
- maintain default-management resources.

## 5. Default waterfall

If a clearing member defaults, losses are absorbed through a predetermined sequence.

```text
Defaulting member’s margin
            ↓
Defaulting member’s other contributions
            ↓
Clearing corporation’s designated resources
            ↓
Settlement Guarantee Fund/default fund
            ↓
Further assessments or recovery measures
```

The exact order depends on applicable regulations and clearing-corporation rules.

A default waterfall **mutualises residual risk** only after resources linked to the defaulter are used.

## 6. What margin and clearing can—and cannot—do

| They reduce | They do not eliminate |
|---|---|
| Counterparty exposure | Market risk |
| Settlement failure | Leverage-related loss |
| Accumulation of unpaid losses | Basis risk |
| Bilateral uncertainty | Liquidity risk |
| Contagion from an isolated default | Extreme systemic stress |

Daily settlement may identify losses early, but it can also generate sudden demands for cash during volatile markets.

```text
Sharp price movement
        ↓
Large variation-margin calls
        ↓
Participants sell assets to raise cash
        ↓
Market stress may intensify
```

## 7. Futures margin versus option premium

| Futures margin | Option premium |
|---|---|
| Performance security | Price paid for the contractual right |
| Adjusted for gains and losses | Normally paid upfront by buyer |
| Additional funds may be required | Buyer’s maximum loss generally limited to premium |
| Not the maximum possible loss | Writer may separately face margin requirements |

## Current-affairs anchor

✅ SEBI’s revised 2026 SGF stress test asks commodity-derivative clearing corporations to consider simultaneous failure of at least three members producing the highest credit exposures.

⚠️ This does not predict that three members will fail. It is a **stress-testing assumption** designed to assess whether default resources are sufficiently robust.

## UPSC traps

1. **“Margin is the maximum amount a futures trader can lose.”**
   ❌ Losses may exceed initial margin.

2. **“Clearing corporations eliminate market risk.”**
   ❌ They primarily manage settlement and counterparty risk.

3. **“A smaller margin makes the position safer.”**
   ❌ A smaller margin implies greater effective leverage.

4. **“MTM loss exists only when the contract expires.”**
   ❌ Futures losses are recognised periodically.

5. **“Settlement Guarantee Fund is the first resource used.”**
   ❌ Resources belonging to the defaulting member are generally used first.

## Revision notes

- Margin is performance security, not asset price.
- Initial margin is collected when opening a position.
- MTM recognises gains and losses regularly.
- A margin call demands additional collateral or funds.
- Leverage magnifies both gains and losses.
- Notional exposure may greatly exceed deposited margin.
- Novation places the clearing corporation between counterparties.
- Clearing reduces counterparty and settlement risk.
- Default waterfalls determine the sequence of loss absorption.
- Clearing cannot remove market, basis or liquidity risk.
- Margin calls can create liquidity pressure during volatility.
- Option premium and futures margin are conceptually different.

### MCQ 1

Consider the following statements:

1. Futures margin represents the maximum loss that a trader can suffer.
2. Mark-to-market settlement periodically recognises gains and losses on open futures positions.
3. A clearing corporation becomes the buyer to every seller and seller to every buyer.
4. Lower upfront margin, for the same notional exposure, generally implies greater leverage.

Which statements are correct?

A. 1 and 2 only
B. 1, 3 and 4 only
C. 2 and 3 only
D. 2, 3 and 4 only

---

❌ **Incorrect. Correct answer: D — Statements 2, 3 and 4**

Statement 4 is correct: for unchanged notional exposure, lower margin means that each rupee deposited controls more exposure—hence **greater leverage**.

### Remedial MCQ 2

A futures position has a notional value of ₹5 lakh and requires ₹50,000 as initial margin. Which statement is correct?

A. The position provides approximately 10-times notional leverage.
B. The trader cannot lose more than ₹50,000.
C. The ₹50,000 represents full payment for the underlying asset.
D. A 2% change in the contract’s value means only a 0.2% change relative to the margin.

---

✅ **Correct: A**

\[
₹5,00,000 \div ₹50,000=10
\]

The position has approximately **10-times notional leverage**, and losses can exceed the initial margin.

**Consecutive correct: 1/2**

### MCQ 3

Which statement correctly explains a clearing corporation’s role?

A. It guarantees that derivatives traders will earn profits.
B. It manages counterparty and settlement risk through novation, margins and default resources.
C. It prevents the underlying asset’s market price from declining.
D. It eliminates the need for participants to meet margin calls.

---

✅ **Correct: B**

A clearing corporation manages counterparty and settlement risk, but it cannot guarantee profits or prevent market losses.

**Subtopic 6 mastered after remediation: 2 consecutive correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—Economy 08 files and local economy reference
🔍 **CA Search:** “SEBI derivatives retail risk and investor protection 2026”
📰 **CA Found:** SEBI’s **August 2026 Settlement and Risk Management consultation** continued regulatory examination of margining, settlement and market safeguards
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 7/8 | Stage: Advanced | Subtopic: Derivative Risks, Regulation and Suitability**

## 🖼️ Risk map

```text
DERIVATIVE POSITION
       │
       ├── Price moves wrongly ─────────► Market risk
       ├── Large notional/small margin ─► Leverage risk
       ├── Hedge does not match asset ──► Basis risk
       ├── Cannot exit cheaply ─────────► Liquidity risk
       ├── Counterparty defaults ───────► Counterparty risk
       ├── Option approaches expiry ────► Time-decay risk
       └── System/process failure ──────► Operational risk
```

## 1. Direction alone is insufficient

Suppose you correctly believe that Reliance will eventually rise. You can still lose through derivatives.

| Instrument | How you may still lose |
|---|---|
| Futures | Price falls first, producing margin calls before recovery |
| Call option | Rise occurs after the option expires |
| Call option | Rise is smaller than the premium paid |
| Short put | Price decline generates substantial writer losses |
| Leveraged position | Temporary movement exhausts available capital |

> 🔑 **Correct direction + wrong timing or leverage = loss.**

## 2. Major risks

### Market risk

The underlying price, rate or index moves against the position.

### Leverage risk

A small amount of capital controls a much larger exposure, magnifying losses.

### Basis risk

The derivative does not move perfectly with the actual exposure being hedged.

### Liquidity risk

The trader cannot exit without accepting a significantly unfavourable price.

### Counterparty risk

A contracting party fails to perform. Clearing reduces this risk for exchange-traded contracts but cannot eliminate every extreme scenario.

### Option time decay

An option is a wasting asset because its remaining time decreases.

```text
More time until expiry ──► More opportunity for favourable movement
Expiry approaches ───────► Time value generally declines
At expiry ────────────────► Only intrinsic value remains
```

An option buyer can therefore lose even if the underlying remains unchanged.

### Volatility risk

Option premiums respond to expected volatility.

- Higher expected volatility generally raises option premiums.
- A decline in volatility may reduce an option’s value even when the underlying moves slightly in the anticipated direction.

## 3. Why “the market has reached its bottom” is dangerous

A market bottom can only be identified confidently **afterward**.

Even if the long-term assessment is correct:

- prices may decline further temporarily;
- recovery may take longer than the derivative’s expiry;
- margin calls may force an early exit;
- option premiums may already reflect the expected recovery; and
- company-specific performance may diverge from the Sensex.

⚠️ **Inference:** Strong conviction is not a substitute for position sizing, liquidity and risk control.

## 4. Shares versus derivatives

| Feature | Cash share | Future | Purchased option |
|---|---|---|---|
| Ownership | Yes | No | No |
| Expiry | Generally none | Yes | Yes |
| Upfront amount | Full purchase value | Margin | Premium |
| Leverage | Usually lower | High | High notional exposure |
| Margin calls | Normally no | Yes | Usually no for buyer |
| Time decay | No | No direct time decay | Yes |
| Maximum buyer loss | Investment may fall substantially | Potentially large | Generally premium |

For someone seeking long-term company ownership, a derivative is not simply a “more confident” version of buying the share. It is a different contract with expiry and leverage.

## 5. Role of trading applications

Groww, Zerodha and similar platforms generally act as **brokers or market-access intermediaries**.

They may provide:

- order execution;
- charts and market data;
- margin information;
- contract details; and
- account statements.

They do not:

- guarantee market direction;
- guarantee settlement profit;
- eliminate leverage;
- establish that an asset has reached its bottom; or
- convert speculation into hedging.

## 6. Indian regulatory architecture

| Segment | Principal regulatory architecture |
|---|---|
| Exchange-traded equity derivatives | SEBI, exchanges and clearing corporations |
| Exchange-traded commodity derivatives | SEBI and recognised exchanges |
| Specified currency, interest-rate and credit derivatives | RBI framework |
| Derivatives within GIFT IFSC | IFSCA framework |
| Clearing and default management | Recognised clearing corporations |

Regulation can strengthen disclosure, margins and settlement, but it cannot prevent investors from making incorrect market forecasts.

## 7. Systemic-risk channel

```text
Market shock
    ↓
Large derivative losses
    ↓
Margin calls
    ↓
Forced sale of other assets
    ↓
Further price declines
    ↓
More margin calls
```

This feedback loop is called **procyclicality**: risk-control mechanisms may require cash precisely when markets are under stress.

## Mains angle

Derivatives simultaneously provide:

- risk transfer;
- liquidity;
- price discovery; and
- lower-cost exposure.

But their benefits require:

- suitable users;
- adequate margins;
- central clearing where appropriate;
- transparent reporting;
- position limits;
- risk disclosures; and
- controls against excessive leverage.

## UPSC traps

- Correctly predicting long-term direction does not ensure derivative profit.
- Exchange trading does not eliminate market risk.
- Option buyers face limited monetary loss but can lose 100% of the premium.
- Futures margin is not the maximum loss.
- A broker’s platform is not a guarantor or clearing corporation.
- Derivative regulation cannot eliminate speculative losses.

## Revision notes

- Derivative risk depends on direction, timing, volatility and leverage.
- Futures can trigger margin calls before an eventual recovery.
- Options lose time value as expiry approaches.
- Basis risk makes hedges imperfect.
- Liquidity determines the cost of exiting.
- Clearing principally reduces counterparty and settlement risk.
- Position sizing is as important as market prediction.
- Broker applications provide access, not guaranteed advice.
- SEBI regulates exchange-traded securities derivatives.
- RBI regulates specified interest-rate, currency and credit derivatives.
- IFSCA regulates relevant IFSC-market activity.
- Excessive leverage can transmit individual losses into systemic stress.

### MCQ 1

Consider the following statements:

1. Correctly predicting the eventual direction of an underlying asset guarantees a profit from a derivative position.
2. A futures trader may face margin calls before the underlying asset eventually moves in the predicted direction.
3. Basis risk arises when the hedge and the actual exposure do not move identically.
4. Using a regulated broker application does not eliminate market and leverage risks.

Which statements are correct?

A. 1 and 2 only
B. 1, 3 and 4 only
C. 2, 3 and 4 only
D. 2 and 3 only

---

✅ **Correct: C — Statements 2, 3 and 4**

Statement 1 is false because timing, expiry, premium, volatility and margin calls can cause losses despite predicting the eventual direction correctly.

### MCQ 2

Which situation best illustrates **time-decay risk**?

A. A futures trader receives a margin call after an adverse price movement.
B. A hedging instrument moves differently from the actual exposure.
C. A counterparty fails to make the contracted payment.
D. A call option loses value as expiry approaches while the underlying price remains broadly unchanged.

---

✅ **Correct: D**

As expiry approaches, an option’s remaining opportunity for a favourable movement diminishes, reducing its time value.

**Subtopic 7 mastered: 2/2 correct.**

---

━━━ **PRE-TEACH CHECKLIST** ━━━━━━━━━━━━━━━━━━
📚 **Book context:** Queried—complete Economy 08 derivatives material and local economy reference
🔍 **CA Search:** “India derivatives regulation RBI and SEBI 2026”
📰 **CA Found:** RBI’s **Credit Derivatives Directions, 2026**, effective **25 June 2026**, cover OTC and exchange-traded credit derivatives, including credit-index futures and total return swaps
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Progress: 8/8 | Stage: Final Synthesis | Topic: Derivatives**

## 🖼️ Master derivative map

```text
DERIVATIVE
Value derived from an underlying
          │
          ├── FORWARD
          │     Customised OTC obligation
          │
          ├── FUTURE
          │     Standardised exchange-traded obligation
          │
          ├── OPTION
          │     Buyer has right; writer has obligation
          │
          └── SWAP
                Exchange of cash-flow streams

PURPOSE
├── Hedge      → reduce existing exposure
├── Speculate  → create directional exposure
└── Arbitrage  → exploit inconsistent prices
```

## 1. Complete comparison

| Feature | Forward | Future | Option | Swap |
|---|---|---|---|---|
| Basic nature | Bilateral obligation | Standardised obligation | Asymmetric right and obligation | Cash-flow exchange |
| Trading | Usually OTC | Exchange | Exchange or OTC | Commonly OTC |
| Customisation | High | Low | Contract-dependent | High |
| Buyer obligation | Yes | Yes | No | Yes |
| Seller/writer obligation | Yes | Yes | Conditional upon exercise | Yes |
| Upfront amount | Usually none | Margin | Premium | Contract-dependent |
| Regular MTM | Not necessarily | Yes | Exchange rules apply | Contract-dependent |
| Major risk | Counterparty | Leverage/market | Premium loss or writer loss | Counterparty/complexity |

## 2. Core payoff logic

### Futures

```text
Buyer gains when price rises
Seller gains when price falls

Both are obligated
```

### Call option

```text
Right to BUY
Benefits from price rise
Buyer’s maximum loss = premium
```

### Put option

```text
Right to SELL
Benefits from price fall
Can protect an owned asset
```

### Swap

```text
Fixed ↔ Floating interest
Currency A ↔ Currency B
Asset return ↔ Financing return
Premium ↔ Credit protection
```

## 3. Contract versus purpose

| Position | Existing exposure | Classification |
|---|---:|---|
| Importer buys dollar futures | Yes | Hedging |
| Shareholder buys a put | Yes | Hedging |
| Trader buys index futures expecting a rise | No | Speculation |
| Trader exploits inconsistent spot/futures prices | Not necessary | Arbitrage |
| Company exchanges floating payments for fixed | Yes | Hedging |

The same instrument can serve different purposes.

## 4. Market infrastructure

```text
Trade executed
      ↓
Clearing corporation interposes itself
      ↓
Initial margin collected
      ↓
Position marked to market
      ↓
Losses produce margin calls
      ↓
Default waterfall protects settlement
```

### Institutional effects

| Mechanism | Principal function |
|---|---|
| Standardisation | Makes contracts comparable and tradable |
| Margin | Provides performance security |
| Mark-to-market | Recognises losses before expiry |
| Clearing corporation | Reduces counterparty and settlement risk |
| Position limits | Restrict excessive concentration |
| Default fund/SGF | Absorbs residual member-default losses |

None of these guarantees profits or eliminates market risk.

## 5. Complete risk framework

```text
Wrong direction ─────────────► Market risk
Large notional exposure ─────► Leverage risk
Imperfect hedge ─────────────► Basis risk
Approaching option expiry ───► Time-decay risk
Changing expected volatility ► Volatility risk
Inability to exit ───────────► Liquidity risk
Contracting-party failure ───► Counterparty risk
Process/model failure ───────► Operational/model risk
```

## 6. How to analyse a derivative question

Ask these seven questions:

1. What is the **underlying**?
2. Is the contract a forward, future, option or swap?
3. Does each party possess a right or an obligation?
4. What are the strike, premium, expiry or notional amount?
5. Is it exchange-traded or OTC?
6. Is the participant hedging, speculating or arbitraging?
7. Who bears market, counterparty, liquidity and leverage risk?

> 🔑 **Mnemonic:** **Underlying–Contract–Rights–Price–Venue–Purpose–Risk**

## 7. Share-market application

Suppose an investor believes a share is near its bottom.

| Action | Actual economic position |
|---|---|
| Buy cash share | Ownership without contractual expiry |
| Buy future | Leveraged obligation with margin calls |
| Buy call | Limited-loss directional position with expiry and premium |
| Sell put | Receives premium but accepts potentially substantial downside |
| Buy protective put after owning shares | Downside hedge |

No derivative is automatically the “confident” choice.

- Futures require sufficient liquidity to survive adverse interim movements.
- Calls require the rise to occur before expiry and exceed the premium.
- Put-writing can generate large losses if the share declines sharply.
- Cash ownership avoids derivative expiry but retains company and market risk.

## 8. Regulatory map

| Market segment | Main Indian architecture |
|---|---|
| Listed equity and commodity derivatives | SEBI, exchanges and clearing corporations |
| Interest-rate, currency and credit derivatives in specified markets | RBI |
| IFSC derivative activity | IFSCA |
| Settlement and default management | Recognised clearing corporations |

✅ RBI’s 2026 Directions define a central counterparty as an entity becoming buyer to every seller and seller to every buyer.

✅ They cover credit derivatives undertaken in OTC markets and recognised stock exchanges.

## 9. UPSC relevance

Derivatives are relevant primarily for:

- financial-market architecture;
- agricultural price-risk management;
- exchange-rate and interest-rate risk;
- investor protection;
- systemic stability;
- regulation by RBI and SEBI; and
- market deepening versus excessive speculation.

### Probable Prelims framing

- futures versus options;
- hedging versus speculation;
- margin versus premium;
- OTC versus exchange trading;
- cash versus physical settlement;
- role of clearing corporations; and
- currency or interest-rate swaps.

### Probable Mains framing

> “Derivatives facilitate risk transfer and price discovery but may amplify financial instability when combined with leverage and unsuitable participation. Discuss.”

### Mains answer spine

```text
Definition
   ↓
Economic benefits
• hedging
• liquidity
• price discovery
• risk allocation
   ↓
Risks
• leverage
• speculation
• margin spirals
• complexity
• counterparty exposure
   ↓
Safeguards
• margins
• clearing
• disclosure
• suitability
• position limits
• regulatory coordination
   ↓
Balanced conclusion
```

## Consolidated revision notes

1. Derivatives derive value from an underlying asset, rate or index.
2. Forwards are customised OTC obligations.
3. Futures are standardised exchange-traded obligations.
4. Option buyers possess rights; writers bear contingent obligations.
5. Calls provide the right to buy; puts provide the right to sell.
6. Swaps exchange specified cash-flow streams.
7. Hedging reduces pre-existing exposure.
8. Speculation creates or enlarges exposure.
9. Arbitrage exploits inconsistent prices.
10. Margin is security, while premium purchases an option right.
11. Clearing reduces counterparty risk but not market risk.
12. Leverage magnifies gains and losses.
13. Hedging remains exposed to basis risk.
14. Options are affected by expiry and time decay.
15. Correct long-term direction does not guarantee derivative profit.
16. SEBI, RBI and IFSCA regulate different derivative-market segments.

### Final Synthesis MCQ 1

Consider the following statements:

1. Futures generally create symmetric obligations for buyers and sellers.
2. An option writer possesses a right without any corresponding obligation.
3. Central clearing reduces counterparty risk but does not eliminate market risk.
4. A derivative transaction qualifies as hedging only if it produces a profit.

Which statements are correct?

A. 1 and 3 only
B. 1, 2 and 3 only
C. 2 and 4 only
D. 1, 3 and 4 only

---

❌ **Incorrect. Correct answer: A — Statements 1 and 3 only**

- **2 is incorrect:** The option **buyer** has the right; the writer bears the contingent obligation.
- **4 is incorrect:** Hedging aims to reduce overall uncertainty, not necessarily earn a derivative profit.

### Final Synthesis MCQ 2

Consider the following pairs:

1. Forward — customised OTC obligation
2. Future — standardised exchange-traded obligation
3. Call option — right to sell the underlying
4. Interest-rate swap — exchange of fixed and floating payment streams

Which pairs are correctly matched?

A. 1 and 2 only
B. 1, 2 and 4 only
C. 2, 3 and 4 only
D. 1, 2, 3 and 4

---

❌ **Incorrect. Correct answer: B — Pairs 1, 2 and 4**

Pair 3 is incorrect:

- **Call option:** right to **buy**
- **Put option:** right to **sell**

**Consecutive correct: 0/2**

### Remedial MCQ 3

Which statements correctly describe options?

1. A call gives its buyer the right to buy.
2. A put gives its buyer the right to sell.
3. An option buyer’s maximum loss is generally limited to the premium.
4. An option writer has no obligation when the buyer exercises the option.

A. 1 and 2 only
B. 1, 3 and 4 only
C. 1, 2 and 3 only
D. 2, 3 and 4 only

---

✅ **Correct: C — Statements 1, 2 and 3**

The option writer bears the obligation if the buyer validly exercises the contractual right.

**Consecutive correct: 1/2**

### Remedial MCQ 4

Which statements are correct?

1. Futures margin is performance security rather than the full contract value.
2. A hedger seeks to reduce an existing exposure.
3. A speculator may use the same derivative contract as a hedger.
4. Clearing corporations reduce settlement risk but cannot prevent market losses.

A. 1 and 2 only
B. 2, 3 and 4 only
C. 1, 3 and 4 only
D. 1, 2, 3 and 4

---

❌ **Incorrect. Correct answer: D — All four statements**

Statement 1 is also correct: futures margin is a **security deposit**, not payment of the full notional contract value.

**Consecutive correct reset: 0/2**

### Remedial MCQ 5

Which statement is correct?

A. Futures margin can be much smaller than the contract’s notional value, thereby creating leverage.
B. An option writer has a right but no obligation.
C. Hedging necessarily maximises profit.
D. Central clearing eliminates changes in market prices.

---

✅ **Correct: A**

A smaller margin controls a larger notional exposure, creating leverage and magnifying both gains and losses.

**Consecutive correct: 1/2**

### Remedial MCQ 6

An exporter expects to receive US dollars after three months and fears that the rupee may appreciate. Which transaction most directly hedges this exposure?

A. Buy US-dollar futures
B. Sell US-dollar futures
C. Buy an unrelated equity call option
D. Enter a pay-fixed interest-rate swap

---

✅ **Correct: B**

The exporter will receive dollars later, so selling dollar futures protects against those dollars losing rupee value.

**Final synthesis mastered: 2 consecutive correct.**

**Derivatives session completed: 8/8 subtopics**
Score: **19/25 (76%)**. Strong fundamentals; revise option rights and integrated contract distinctions.
