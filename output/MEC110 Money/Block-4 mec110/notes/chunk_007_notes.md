# Chunk 007 — Derivatives: Characteristics, History, Types, Futures vs Forwards, and Options
<!-- Pages: 61-72 -->
<!-- Source: chunk_007.txt -->

## Section: Meaning and Characteristics of Derivatives 🔴

<!-- Continues from chunk 006 introduction to derivatives. -->

### Core Idea
Derivatives are contracts whose value depends on an underlying asset, used to manage or speculate on **price, interest-rate, and credit risks**. They share six characteristics: dependence on an underlying, global popularity, four main forms (futures, forwards, options, swaps), heavy OTC use, exchange-traded standardisation reducing risk, and built-in **leverage** that amplifies both rewards and risks.

### Key Concepts

#### Six characteristics
a) **Derives value** from an underlying asset (share, stock).
b) Traded **globally**; very popular in developed economies.
c) Common forms: **futures, forwards, options, swaps**.
d) **Most are not exchange-traded** — used OTC by institutions to hedge or speculate.
e) **Exchange-traded** derivatives (futures, stock options) are **standardised** and reduce many OTC risks.
f) Usually **leveraged** instruments → amplified risks and rewards.

### Definitions
- **Hedging** ⭐: Strategy/transaction undertaken to reduce or manage risk.
- **Speculation**: Taking a position to profit from anticipated price changes (no offsetting underlying exposure).
- **Leverage** (in derivatives context): Gaining exposure to a larger position than the cash invested would otherwise allow.

> **Quick Recall:**
> - 6 characteristics: underlying-derived, global, 4 forms, OTC-heavy, standardised on exchanges, leveraged.

---

## Section: Advantages and Limitations of Derivatives 🔴

### Core Idea
Derivatives offer four big advantages — **price-locking, hedging, leverage, diversification** — and four offsetting limitations — **valuation difficulty, counterparty default, complexity, and demand-supply sensitivity**. Each side of the ledger illustrates why they are powerful but require careful use.

### Key Concepts

#### Advantages

| Advantage | How it works |
|-----------|---------------|
| **Lock in prices** | Hedge against price fluctuations in commodities, currencies, securities — supports financial planning and budgeting |
| **Hedge against risk** | Producers/consumers of commodities lock in prices via futures/options; firms with debt use **interest-rate swaps/futures** to neutralise rate risk |
| **Leveraged exposure** | Small capital → large position; small underlying-price moves → big derivative value moves |
| **Portfolio diversification** | Access to commodities, currencies, rates, equities; even hard-to-reach emerging markets |

#### Limitations

| Limitation | Why it matters |
|------------|-----------------|
| **Difficult to value** | Often requires advanced models — **Black-Scholes** or **binomial pricing** (covered in Unit 21); strong assumptions about market behaviour |
| **Counterparty default** | Loss if counterparty fails to honour the contract; counterparty's credit-rating decline reduces derivative's value |
| **Complex** | Many types — options, futures, forwards, swaps, **CDOs, CDS** etc. — each with own rules, characteristics, and pricing |
| **Sensitive to demand-supply** | Speculative trading can amplify volatility |

### ⚠️ Common Mistakes
- ❌ Mistake: Leverage only works in your favour. → ✅ Correct: Leverage amplifies **losses** equally; small adverse moves in the underlying produce large derivative losses.
- ❌ Mistake: Exchange-traded derivatives have no counterparty risk. → ✅ Correct: They drastically *reduce* it via clearing corporations; OTC derivatives carry full counterparty risk.

> **Quick Recall:**
> - 4 advantages: lock prices, hedge risk, leverage, diversify.
> - 4 limitations: hard to value, counterparty default, complex, demand-supply volatility.

---

## Section: Brief History of Derivatives in India 🟡

### Core Idea
Indian derivative use traces back to commodity trading (cotton, **1875** with the Cotton Trade Association). Modern exchange-traded financial derivatives launched at NSE/BSE in **June 2000**, and **NCDEX** opened December 2003 for commodities. Stock futures grew to ~55% of NSE derivatives turnover by April 2005.

### Mechanisms / Processes

#### Indian derivative milestones (chronological)
| Year/Date | Event |
|-----------|-------|
| 1875 | Cotton Trade Association established → start of Indian commodity derivative market |
| **June 2000** | Exchange-traded financial derivatives launched at NSE & BSE; **Index Futures Contracts** introduced |
| June 2001 | **Index Options** introduced |
| July 2001 | **Stock Options** introduced |
| Nov 2001 | **Stock Futures** introduced |
| Dec 2002 | Sectoral-index derivatives approved |
| June 2003 | **Interest Rate Futures** on a notional bond and T-bill (priced off ZCYC) introduced |
| Dec 2003 | **NCDEX** (National Commodity & Derivatives Exchange Ltd) commenced operations |
| Jan 2004 | Exchange-traded interest-rate futures on a notional bond priced off a basket of G-secs approved |
| Apr 2005 | **Stock Futures ≈ 55% of NSE derivatives turnover** — most actively traded contracts |

#### Regulatory architecture
- Derivative trading at distinct Derivative Exchange or designated Stock Exchange segment.
- Operate as **Self-Regulatory Organisations (SROs)** with **SEBI** as overseer.
- Clearing & settlement via **independent Clearing Corporations / Houses**.

> **Quick Recall:**
> - Cotton Trade Association: 1875.
> - Financial derivatives at NSE/BSE: **June 2000**.
> - NCDEX: **Dec 2003**.
> - Stock futures: ~55% of NSE derivatives turnover by Apr 2005.

---

## Section: Types of Derivatives 🔴

### Core Idea
Seven main derivative families, each used for a distinct combination of hedging or speculative purposes — **Futures, Forwards, Options, Swaps, Credit derivatives, Equity derivatives, Commodity derivatives**.

### Key Concepts

| # | Type | What it does | Trading venue |
|---|------|---------------|----------------|
| 1 | **Futures** | Buy/sell underlying at predetermined price & time; standardised | Organised exchanges |
| 2 | **Forwards** | Customised buy/sell agreement at predetermined price & time | OTC (private) |
| 3 | **Options** | Right (not obligation) to buy/sell at strike price by date | Both exchanges and OTC |
| 4 | **Swaps** | Exchange cash flows based on different underlyings (rates, currencies, commodities); 2 most common: **interest-rate swap, credit-default swap (CDS)** | OTC |
| 5 | **Credit derivatives** | Manage credit risk by transfer (CDS, CDOs) | OTC |
| 6 | **Equity derivatives** | Exposure to a stock or index price (options/futures/swaps on equity) | Both |
| 7 | **Commodity derivatives** | Exposure to commodity price (gold, oil, wheat) | Both |

> **Quick Recall:**
> - 4 most common: **Futures, Forwards, Options, Swaps**.
> - 7 total families, including credit, equity, commodity derivatives.
> - Most popular swaps: **IRS** and **CDS**.

---

## Section: Futures and Forwards 🔴

### Core Idea
Both let parties lock in a future price for an asset, but they differ structurally. **Forwards** are private, customised, OTC contracts with default risk and physical settlement; **futures** are standardised, exchange-traded contracts with marking-to-market, cash settlement, and effective default safeguards via clearing.

### Key Concepts

#### Forwards — definition and use
- Two-party financial agreement to buy/sell asset at predetermined price at future date.
- Counterparties: individuals, corporations, financial institutions.
- Used to **hedge price fluctuations** in commodities, currencies, stocks, bonds.

**Example 13.1 (forward):** A company that wants to buy a commodity later signs a forward contract with a supplier at a fixed price → avoids price-volatility risk. An investor expecting a stock to appreciate signs a forward to buy the stock at a predetermined price.

#### Futures — definition and use
- Financial instrument that **legally binds** parties to buy/sell an asset at a predetermined price and date.
- Price of the underlying is fixed at contract creation.
- Used by traders/investors to **hedge or speculate**.

**Example (futures):** A wheat farmer sells a wheat futures contract to lock in a price for future delivery → hedges against price drop. A speculator buys a stock-index future expecting market to rise.

### Mechanisms / Processes

#### Forwards vs Futures (Table 13.1)

| # | Forward contract | Futures contract |
|---|------------------|-------------------|
| 1 | Contract price **not publicly disclosed** | Contract price **transparent** |
| 2 | **Counterparty default risk** present | Effective safeguards against defaults |
| 3 | **Unique** in size, expiration, asset type | **Standardised** size, expiration, features |
| 4 | Suffers from **liquidity** problems | No liquidity problem |
| 5 | Settlement by **physical delivery** of asset | Cash settlement |
| 6 | Traded personally / by phone | Traded in competitive markets |
| 7 | **OTC** market | Organised exchange with physical location |
| 8 | Costs based on **bid-ask spread** | Brokerage fees |
| 9 | **Not subject to marking to market** | Subject to **marking to market** |
| 10 | Credit risk **borne by each party** | Credit risk **not borne by each party** (clearing house) |

### Definitions
- **Futures** ⭐: Standardised, exchange-traded contract obligating buyer to purchase and seller to sell an asset at predetermined price and date.
- **Forwards** ⭐: Customised, OTC contract between two parties to buy/sell an asset at predetermined price and date.
- **Marking to market**: Daily revaluation of futures positions to current market price; gains/losses settled daily.

### ⚠️ Common Mistakes
- ❌ Mistake: Futures and forwards are interchangeable. → ✅ Correct: Futures = **standardised**, exchange-traded, MTM; Forwards = **customised**, OTC, no MTM.
- ❌ Mistake: Futures are settled by delivery. → ✅ Correct: Futures usually **cash-settled**; forwards typically delivered.

> **Quick Recall:**
> - Futures = standardised + exchange + MTM + clearing house bears credit risk.
> - Forwards = customised + OTC + delivery + each party bears credit risk.

### Connections
- Cross-reference: Block 4 Unit 21 — Pricing of Derivatives (Black-Scholes, binomial models).

---

## Section: Options — Concept and Call Option 🔴

### Core Idea
An **option** is the right (not the obligation) to buy or sell an underlying asset at a predetermined **strike/exercise price** within a specified period — purchased for an upfront **option premium**. A **call option** gives the buyer the right to **buy**; the option is exercised only when the spot price exceeds the strike (S > E), otherwise it lapses. The option premium represents the cost of avoiding downside risk while retaining upside potential.

> **In Simple Terms:** A call option is like reserving a movie ticket at today's price for tomorrow's show. If tomorrow the ticket price rises, you win — you pay yesterday's price. If tomorrow's price drops, you don't go (the reservation lapses) and you only lose the small booking fee. The "booking fee" is the option premium.

### Key Concepts

#### What is an option
- Agreement: Party A has the **right** to buy/sell an asset at a predetermined price within a specified time frame.
- A is **not obligated** to execute — that's why it's called an option.
- **Hedging tool**: managing the risk of price fluctuations.

#### Option types (two)
1. **Call option** — right to **buy**.
2. **Put option** — right to **sell**.

#### Anatomy of a call option (running example)
- Current share price: ₹500.
- Vikas grants you the right to **buy** the share at **₹530** in 4 months, regardless of actual market price.
- He charges **₹20** as option premium.
- **If actual price rises to ₹580**: exercise → buy at ₹530 (from Vikas), sell at ₹580 (in market) → ₹50 gain − ₹20 premium = **₹30 net payoff**. Loss for Vikas.
- **If actual price stays low**: don't exercise. You lose only the ₹20 premium.

| Term | Meaning in this example |
|------|-------------------------|
| **Underlying asset** | The share |
| **Exercise / strike price (E)** | ₹530 |
| **Exercise / intrinsic value of call (S − E at expiry)** | ₹50 (when S = ₹580) |
| **Option premium** | ₹20 (cost to buyer for taking the option) |
| **Net payoff** | ₹30 (₹50 gross − ₹20 premium) |
| **Option writer** | Vikas (sells the option) |
| **Option buyer** | You |

#### Decision rule for a call option (Table 13.2)

| Situation | Decision | Market Term |
|-----------|----------|-------------|
| **S > E** at expiry (S − E > 0) | **Exercise** — profitable | **In-the-money call** (money flows to buyer) |
| **S < E** at expiry (S − E < 0) | **Don't exercise** | **Out-of-the-money call** (money would flow out if exercised) |

#### Formulas

**Exercise (intrinsic) value of a call option, V_CO:**
$$V_{CO} = \begin{cases} S - E & \text{if } S > E \\ 0 & \text{if } S \le E \end{cases}$$

Equivalently:
$$V_{CO} = \max(S - E, 0)$$

**Net payoff:**
$$\text{Net Payoff} = V_{CO} - \text{Option premium}$$

(Net payoff diagrams from buyer's perspective slope upward beyond E; from writer's perspective they're the mirror image — capped gain = premium, downside unbounded.)

### Examples

**Example 13.2 — Call option on Reliance Industries:**
- Current price ₹7; possible prices at expiry (3 months): ₹5, ₹10, ₹15, ₹20, ₹25, ₹30.
- Aakash buys a call: **strike E = ₹12**, premium = ₹2. (Source uses "₹35" then computes with ₹2; the worked table uses ₹2.)

**Buyer's payoff (Aakash):**

| Price S (₹) | Premium (₹) | Strike (₹) | Total Cost (₹) | Net Payoff (₹) | Exercise? |
|-------------|--------------|--------------|------------------|------------------|------------|
| 5 | 2 | — | 2 | −2 | No |
| 10 | 2 | — | 2 | −2 | No |
| 15 | 2 | 13 | 15 | 0 | Yes |
| 20 | 2 | 13 | 15 | 5 | Yes |
| 25 | 2 | 13 | 15 | 10 | Yes |
| 30 | 2 | 13 | 15 | 15 | Yes |

**Writer's payoff (derivative dealer)** — mirror image:

| Price S (₹) | Premium (₹) | Strike (₹) | Total Revenue (₹) | Net Payoff (₹) | Exercise? |
|-------------|--------------|--------------|---------------------|------------------|------------|
| 5 | 2 | — | 2 | 2 | No |
| 10 | 2 | — | 2 | 2 | No |
| 15 | 2 | 13 | 15 | 0 | Yes |
| 20 | 2 | 13 | 15 | −5 | Yes |
| 25 | 2 | 13 | 15 | −10 | Yes |
| 30 | 2 | 13 | 15 | −15 | Yes |

> Buyer's max loss = premium; potential gain = unbounded above strike.
> Writer's max gain = premium; potential loss = unbounded above strike.

### Definitions
- **Option** ⭐: Right (not obligation) of one party to buy or sell an underlying at a predetermined price within a specified time frame, for a premium.
- **Call option** ⭐: Type of derivative giving the buyer the right to **buy** the underlying at the strike price.
- **Strike / exercise price (E)** ⭐: Predetermined price at which the underlying may be bought (call) or sold (put).
- **Option premium** ⭐: Cost paid by buyer for taking the option; reflects time value and writer's risk.
- **Intrinsic / exercise value (V_CO)**: Max(S − E, 0) for a call.
- **In-the-money call**: S > E at expiry.
- **Out-of-the-money call**: S < E at expiry.
- **Hedging**: Strategy to reduce or manage risk.
- **Option writer**: Sells (writes) the option — receives premium, takes on obligation if exercised.
- **Option buyer**: Pays premium for the right to exercise.

### ⚠️ Common Mistakes
- ❌ Mistake: An option *forces* the holder to buy/sell. → ✅ Correct: It is a **right, not an obligation** — buyer can let it lapse.
- ❌ Mistake: Net payoff equals intrinsic value. → ✅ Correct: Net payoff = intrinsic value **− option premium**.
- ❌ Mistake: Out-of-the-money call should still be exercised. → ✅ Correct: Exercising a call when S < E means buying at a loss; never rational.

> **Quick Recall:**
> - Call: right to buy. Exercise iff S > E.
> - V_CO = max(S − E, 0). Net Payoff = V_CO − premium.
> - Buyer max loss = premium; writer max gain = premium.
> - Vocabulary: strike, premium, in/out of the money, writer, buyer.

### Connections
- Builds on: Derivative classification (this chunk).
- Continues into: Put options, Swaps (Chunk 008).

### Open Questions
1. How is the option premium priced — what are the main drivers?
2. Why do most exchange-traded options eventually expire worthless from the buyer's standpoint?

<!-- Continues in chunk 008 -->
