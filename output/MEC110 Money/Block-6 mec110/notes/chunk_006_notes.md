# Chunk 006 — Unit 20 wrap-up + Unit 21: Derivatives Basics & Types
<!-- Pages: 47-57 -->
<!-- Source: chunk_006.txt -->
<!-- Continues from: APT critique (chunk 005) -->

## Section: 20.6 Unit 20 Summary & Key Words 🟢

### Summary points
- APT (Ross) — alternative to CAPM; uses multiple systematic risk factors.
- Expected return = linear function of macro-factor sensitivities + risk-free rate.
- Applications: equities, commodities, real assets, fixed income, cross-border pricing.
- Empirical issues: data, misspecification, time-varying β, factor redundancy, efficiency.
- APT remains valuable for flexibility and empirical testability.
- Future directions: better factor ID, dynamic models, behavioural aspects, nonlinear relations.

### Unit 20 Key Words (glossary)
| Term | Meaning |
|---|---|
| Arbitrage Pricing Theory (APT) | Multi-factor asset-pricing alternative to CAPM. |
| CAPM | Single-factor model linking expected return to systematic risk via β. |
| Efficient Market Hypothesis (EMH) | Prices reflect all available info; can't beat market consistently with public info. |
| Factor sensitivities (β_ij) | How asset *i* responds to factor *j*. |
| Market portfolio | Theoretical value-weighted portfolio of all assets. |
| Market risk premium | $R_m − R_f$ — excess return for systematic risk. |
| Rational expectations | Forecasts use all available information. |
| Risk-free rate | Return on zero-risk asset; gov't-bond yield proxy. |
| Systematic risk (β) | Asset's sensitivity to market portfolio. |
| Unsystematic risk | Idiosyncratic / specific risk; diversifiable. |

---

## Section: Unit 21 — Pricing of Derivatives: Objectives & Introduction 🟢

### Core Idea
Unit 21 picks up derivatives (basics covered in Unit 13) and adds pricing models. Indian derivatives market (NSE) has overtaken cash-segment turnover; the **NSE is the world's largest derivatives bourse by contract count**. As of 2 January 2024, 10-day MA notional turnover hit **$5.04 trillion** (vs $2.5 trillion at end-2022).

> **In Simple Terms:** Derivatives are bets / insurance contracts whose value is *derived* from another asset (a stock, a barrel of oil). They're now traded more than stocks themselves on NSE.

### Key Concepts
- Derivatives' three economic roles: **price discovery**, **portfolio diversification**, **risk hedging**.
- Notional turnover = Σ(strike price × underlying-asset quantity) per contract.

### Connections
- **Builds on**: Unit 13 (basic derivatives, types).
- **Extends to**: §21.4 pricing models (chunks 007–008).

---

## Section: 21.2 Derivatives — Basic Concepts 🔴

### Core Idea
A **derivative**'s value is *derived* from an underlying asset (security, commodity, currency, index). Derivative contracts have predetermined durations (typically 3–12 months). They are *not* backed by the original asset issuer — they are "deferred delivery / deferred payment instruments".

### Key Concepts

#### What is "underlying"?
Real or financial assets, or a securities index. Two flavours:
| Type | Underlying examples |
|---|---|
| **Commodity derivatives** | Coffee, wheat, precious stones |
| **Financial derivatives** | Debt instruments, currency, equity shares |

#### Trading venues
- **Exchange-traded** — standardised; lower transaction costs; lower default risk.
- **Over-the-counter (OTC)** — customised; flexible terms; higher credit / default risk; lower liquidity.

### Definitions
- **Derivative**: a contract whose value is derived from an underlying asset; contract types include forwards, futures, options, swaps, hybrids, with predetermined durations. ⭐ (exam-important)
- **Notional turnover**: sum, over contracts traded today, of (strike price × number of underlying-asset units in each contract).

### Examples
- **Farmer–merchant**: farmer worried about wheat price drop signs a derivative to lock a future price (exercise price). Value moves with market wheat price.
- **Soybean farmer**: 150 quintals expected in 3 months → can do OTC contract with food merchant or buy a standardised exchange wheat futures, leaving some uncovered for upside.

#### Five economic functions of derivative markets
1. **Risk transfer** — from risk-averse to risk-oriented players.
2. **Price discovery** — for current and future prices.
3. **Stimulation of entrepreneurial activity**.
4. **Increased market trading volumes** — risk-averse players join because they can hedge.
5. **Promotion of savings & long-term investment**.

> **Quick Recall:**
> - 5 functions: risk transfer, price discovery, entrepreneurship, more volume, savings & investment.
> - Exchange-traded vs OTC: standardisation/liquidity vs customisation/credit risk.

---

## Section: 21.3.1 Forward Contracts 🔴

### Core Idea
A forward contract is a **bespoke bilateral agreement** between two parties to exchange an asset on a future date at a price agreed today. It is the simplest derivative — old, customised, and prone to **default risk**.

### Key Concepts
- **Long position** — buyer; commits to buy at agreed price on the future date.
- **Short position** — seller; commits to sell at agreed price on the future date.
- **Settlement**: physical or cash. Cash settlement → single payment based on market value at expiry; underlier and money don't physically move.
- **Forward curve** = graph of forward prices for various maturities.
- **Bid / offer forward prices** influenced by time value of money + market expectations.

### Mechanisms / Processes — Forward payoff
$$\text{Payoff} = n(s - k)$$

Where:
- $n$ = notional amount (units of underlier)
- $s$ = spot price at settlement
- $k$ = delivery (forward) price agreed at contract date

Linear payoff — gains/losses scale 1-to-1 with $s$ moves.

### Examples
- **Reliance shares**: A and B agree to buy/sell 100 Reliance shares at Rs 850 in 2 months. Terms (product, quantity, price, delivery) are predetermined.
- **Crude oil**: 500,000 barrels at US $42.08/barrel in 3 months → variables = underlier (oil), n (= 500,000), k (= $42.08), settlement date.
- **Default risk**: if Reliance market price rockets above 850, seller may default to sell on the open market; if it crashes below 850, buyer may default to buy cheaper.

### ⚠️ Common Mistakes
- ❌ "Forwards have no default risk because both sides commit" → ✅ Mutual commitment is exactly what creates the risk: when one side wins big, the other has incentive to walk away.

> **Quick Recall:**
> - Forward = customised, bilateral, bespoke, default-risky.
> - Payoff = n(s − k). Long wins if s > k.
> - Forward curve = forward price vs maturity.

---

## Section: 21.3.2 Futures 🔴

### Core Idea
**Futures** are standardised, exchange-traded forward contracts. Their key innovation: a **clearing corporation/house** acts as central counterparty, providing settlement guarantee → *eliminates credit risk*. Daily mark-to-market via margining settles P&L.

### Key Concepts — Forward vs Futures (memorise the contrast)

| Aspect | Forward | Futures |
|---|---|---|
| Trading | OTC, bilateral | Exchange-traded |
| Customisation | Fully customisable | Standardised (qty, quality, delivery) |
| Liquidity | Poor | High |
| Default risk | Significant | Eliminated by clearinghouse |
| Margining | None | Daily mark-to-market |
| Settlement | Physical or cash, at expiry | Physical or cash, with daily settlement |
| Counterparty | Other side of the trade | Clearinghouse (two contracts, each with clearinghouse) |

#### Types of futures
- **Index futures** — based on an underlying index; **cash-settled**; value derived from index.
- **Stock futures** — single specific stocks; **cash-settled** for single-stock futures.

### Definitions
- **Futures contract**: a legally binding standardised exchange-traded agreement to buy or sell an underlying on a predetermined future date, with clearinghouse-guaranteed settlement and daily margining. ⭐ (exam-important)
- **Margining**: daily profit/loss calculation on a futures position to ensure ongoing settlement and eliminate credit risk.

> **Quick Recall:**
> - Forward → futures = standardisation + exchange + clearinghouse + margining.
> - Index futures and single-stock futures are typically cash-settled.

---

## Section: 21.3.3 Options 🔴

### Core Idea
An **option** gives the *buyer* the **right but not the obligation** to buy (call) or sell (put) the underlying at a predetermined price (strike) within or at end of a specified period. The *seller* (writer) has the obligation if the buyer exercises. The buyer pays the writer an upfront **premium** for this right.

> **In Simple Terms:** An option is like paying a small reservation fee for a TV — if you find a better deal, you walk away (let it expire). Forwards/futures are *contracts*; options are *rights*.

### Key Concepts

#### Call vs Put
| | Call | Put |
|---|---|---|
| Right of buyer | Right to **buy** at strike | Right to **sell** at strike |
| Buyer profits when | Spot > Strike | Spot < Strike |

#### American vs European
- **American** — exercisable any time on or before expiry.
- **European** — exercisable only on expiry date.

#### Moneyness
- **In the money (call)**: current price > strike.
- **Out of the money (call)**: current price < strike.
- (Mirror for put.)

#### Covered vs Naked
- **Covered option**: writer owns the underlying.
- **Naked option**: writer does not own the underlying — higher risk.

#### Index options
Based on an index, **European-style**, **cash-settled** at expiry.

### Definitions
- **Strike / Exercise price**: agreed price at which the option can be exercised. ⭐ (exam-important)
- **Premium**: cost paid by option buyer to writer for the right. ⭐ (exam-important)
- **Call option**: right to buy at strike. ⭐ (exam-important)
- **Put option**: right to sell at strike. ⭐ (exam-important)
- **Writer**: option seller; obligated if buyer exercises.

### Examples
- **European put on Brent oil**: 100,000 barrels, strike US $45, 3-month expiry. Holder can sell 100,000 bbl @ $45 in 3 months *if* it suits them.
- **TV reservation analogy**: Mr A pays Rs 200–300 to reserve a TV for 2 days with right to buy. He's an option buyer; the Rs 200–300 is the premium; if he finds a better deal, he lets the option expire.

> **Quick Recall:**
> - Option = right (no obligation) for buyer; obligation for writer.
> - Call = right to buy. Put = right to sell.
> - American = anytime; European = expiry only.
> - Index options = European, cash-settled.

---

## Section: 21.3.4 Swaps 🔴

### Core Idea
A **swap** is a contractual agreement to exchange cash flows or financial obligations over a specified period at predetermined intervals. Main forms: **interest rate swaps** (most common — "plain vanilla") and **currency swaps**.

### Key Concepts

#### Plain Vanilla Interest Rate Swap
- One party pays **fixed-rate** interest on a notional principal; receives **floating-rate** (often **LIBOR**-linked).
- **Notional principal** = reference amount only — never actually exchanged.
- Maturities: typically **2–10 years**, can range from < 1 year to > 15 years.

#### Currency Swap
- Exchange foreign currencies in spot market with simultaneous **forward-market reversal** at predetermined rate and timing.
- Both **principal and interest** are swapped (unlike IR swap).
- At maturity, principal amounts are swapped back.

**Example:** Indian company borrows in rupees at fixed rate but has $-revenue. Enters a currency swap: receives rupees at fixed rate, pays dollars at fixed/floating. Manages both interest-rate AND exchange-rate risk.

#### Other swap forms (named)
Coupon swaps, basis rate swaps, bond swaps, substitution swaps, intermarket spread swaps, swaps with timing mismatches, options-like swaps, currency swaps.

### Definitions
- **Interest rate swap**: exchange of one stream of interest obligations for another (typically fixed for floating) on a notional principal. ⭐ (exam-important)
- **Currency swap**: exchange of principal and interest in one currency for principal and interest in another, with reversed exchange at maturity. ⭐ (exam-important)
- **Notional principal**: reference amount used to compute interest in a swap; not physically exchanged.

> **Quick Recall:**
> - Most common swap: plain vanilla IR (fixed↔floating, often LIBOR).
> - Currency swap involves both interest *and* principal exchange.
> - Notional principal = reference only.

---

## Section: Three Trader Types in Derivatives Markets 🟡

| Trader | Aim | Tool |
|---|---|---|
| **Hedger** | Mitigate risk from future price moves | Forwards, futures, options |
| **Speculator** | Profit from anticipated price moves | All derivatives |
| **Arbitrageur** | Lock in risk-free profit from price discrepancies between markets | Offsetting positions in 2+ instruments |

> **Quick Recall:**
> - Hedger reduces risk; speculator takes risk; arbitrageur takes no net risk.

---

## Section: 21.3.5 Put-Call Parity 🔴

### Core Idea
**Put-call parity** is a no-arbitrage relationship between **European call** and **European put** prices on the same underlying with the **same strike and same expiry**. It enforces consistent pricing — any deviation creates an arbitrage.

### Key Concepts

#### Two equivalent portfolios at expiration (T)
At expiration, with underlier value $S_T$ and strike $K$:
- **Portfolio 1**: long put + long share — value = max(K, S_T)
- **Portfolio 2**: long call + K bonds (each paying 1 at T) — value = max(S_T, K)

Same payoffs ⇒ same prices at every $t < T$.

#### Put-Call Parity Equation
$$C(t) + K \cdot B(t, T) = P(t) + S(t)$$

Where:
- $C(t)$ = time-t price of European call
- $P(t)$ = time-t price of European put
- $S(t)$ = time-t price of share
- $K$ = strike price
- $B(t, T)$ = time-t price of a zero-coupon bond paying 1 at T (i.e., $K \cdot B(t,T)$ is the PV of strike)

### Implications
1. **Equivalence of calls and puts** — in any **delta-neutral portfolio**, calls and puts can substitute. If $d$ is the call's delta, then *long call + short d shares* ≡ *long put + long (1−d) shares*.
2. **Parity of implied volatility** — without dividends/carry costs, calls and puts must show the same implied volatility — keeps market expectations consistent.

### ⚠️ Common Mistakes
- ❌ Applying parity directly to American options → ✅ Strict parity holds for European options; American options have an inequality version due to early-exercise possibility.

> **Quick Recall:**
> - Parity: $C + K \cdot B(t,T) = P + S$.
> - Same strike, same expiry, European, no dividends.
> - Violation ⇒ arbitrage.

### Connections
- **Builds on**: §21.3.3 Options (this chunk).
- **Pairs with**: Black-Scholes & Binomial pricing models (chunk 007 — §21.4).
<!-- Continues in chunk 007: §21.4 Pricing models (Binomial, Black-Scholes) -->
