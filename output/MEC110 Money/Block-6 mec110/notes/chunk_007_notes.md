# Chunk 007 — Unit 21 (cont.): Derivative Pricing Models — Binomial & Black-Scholes
<!-- Pages: 58-68 -->
<!-- Source: chunk_007.txt -->
<!-- Continues from: Unit 21 derivatives types (chunk 006) -->

## Section: 21.4 Models of Derivative Pricing — Overview 🟡

### Core Idea
Derivative pricing finds the *fair value* of a derivative contract. It depends on derivative type, underlying asset properties, market conditions, and methodology. Unit 21 covers two pricing models:
1. **Binomial Option Pricing Model** (Cox, Ross, Rubinstein, 1979) — discrete-time, lattice based.
2. **Black-Scholes Model** (Black, Scholes 1973) — continuous-time, closed-form formula.

---

## Section: 21.4.1 Binomial Option Pricing Model 🔴

### Core Idea
Introduced by **Cox, Ross, Rubinstein (1979)**. A discrete-time numerical approach: the underlying's future price is modelled as a tree (lattice) of "up" or "down" moves. Option value is computed by working *backwards* from expiry to today, using **risk-neutral probabilities** to discount.

> **In Simple Terms:** Think of a tree drawn on paper — at each step, the stock either goes up or down. At expiry, you know what the option is worth at every leaf. Roll the value back step by step (averaging up/down possibilities and discounting at $r$) until you reach today.

### Key Concepts

#### Strengths
- **Versatile** — handles American (anytime exercise), Bermudan (set of exercise dates), dividend-paying options.
- **Simple & implementable** in spreadsheets/software.
- **Accurate** for long-dated options or those with dividends.

#### Limitations
- Slower than Black-Scholes for European options.
- Struggles with multi-uncertainty options (real options) or complex features (Asian options) — **Monte Carlo** is preferred there, though computationally heavy.

### Mechanisms / Processes — 3-step valuation
1. **Price tree generation** — build a binomial tree of underlying-asset prices over N time steps.
2. **Calculate option value at final nodes** — intrinsic (exercise) value at expiry: max(S_T − K, 0) for call; max(K − S_T, 0) for put.
3. **Progressive (backward) calculation at earlier nodes** — at each prior node use risk-neutral pricing:
   - Today's fair value = discounted expected future value, with risk-neutral probabilities.

#### Binomial Value formula at each node
$$\text{Binomial Value} = [p \times \text{Option}_{up} + (1-p) \times \text{Option}_{down}] \times e^{-r \times t}$$

Where:
- $p$ = risk-neutral probability of an up move
- $1-p$ = probability of a down move
- $r$ = risk-free rate
- $t$ = time step length

#### American option rule at each node
$$\text{Node value} = \max(\text{Binomial Value}, \text{Exercise Value})$$

Holding ↔ Binomial Value; exercising now ↔ Exercise Value (intrinsic). Take the higher.

### Definitions
- **Binomial Option Pricing Model**: discrete-time lattice model that values options by recursive risk-neutral discounting through a tree of possible underlying prices. ⭐ (exam-important)
- **Risk-neutral probability (p)**: probability that, when used to discount expected future payoffs at $r$, gives today's fair price.

> **Quick Recall:**
> - 1979, Cox-Ross-Rubinstein.
> - 3 steps: tree, terminal payoff, backward induction.
> - American: max(BinValue, ExerciseValue) at each node.

### ⚠️ Common Mistakes
- ❌ Using real-world probabilities to discount → ✅ Use risk-neutral probability $p$ (so discount rate = $r$).

---

## Section: 21.4.2 Black-Scholes Option Pricing Model 🔴

### Core Idea
**Fischer Black & Myron Scholes (1973)** — building on Thorpe, Samuelson, Merton — give a **closed-form formula** for European call/put values when the underlying follows geometric Brownian motion. Fast, widely used, but limited to European options.

### Key Concepts

#### Six Black-Scholes assumptions (memorise)
1. Underlying generates **no dividends** during option life.
2. **Zero transaction costs**.
3. **Risk-free rate is known and constant** during option life.
4. **European exercise** only — at expiry, not before.
5. **Short selling allowed** — short seller gets full cash proceeds today.
6. **Stock price moves randomly** (geometric Brownian motion).

(Plus: no arbitrage, perfect divisibility, continuous trading, known constant volatility σ.)

#### Black-Scholes Formula

For a **European call**:
$$V_{CO} = P \cdot N(d_1) - Y \cdot e^{-rt} \cdot N(d_2)$$

For a **European put**:
$$V_{PO} = Y \cdot e^{-rt} \cdot [1 - N(d_2)] - P \cdot [1 - N(d_1)]$$

Where:
$$d_1 = \frac{\ln(P/Y) + [r + \sigma^2/2] \cdot t}{\sigma \sqrt{t}}$$
$$d_2 = d_1 - \sigma \sqrt{t}$$

Notation:
- $V_{CO}, V_{PO}$ = value of call, put
- $P$ = current price of underlying
- $Y$ = exercise / strike price
- $r$ = risk-free rate (continuously compounded)
- $t$ = time to expiry (in years, fractional ok)
- $\sigma^2$ = annualised variance of return on underlying; $\sigma$ = annualised SD
- $N(d_1), N(d_2)$ = cumulative areas under standard normal distribution
- $\ln(P/Y)$ = natural log of (P/Y)
- $e \approx 2.7183$

### Definitions
- **Black-Scholes Model**: a closed-form pricing formula for European call and put options under geometric Brownian motion of the underlying. ⭐ (exam-important)
- **N(d)**: cumulative probability under the standard normal distribution from −∞ to d. In Excel: `=NORM.DIST(d, 0, 1, TRUE)`.

### Examples

#### Example 21.1 — Worked TCS call
**Inputs:** P = ₹25, Y = ₹20, r = 5% (= 0.05), t = 3 months (= 0.25 years), σ² = 0.16 → σ = 0.4.

**Step 1 — d₁:**
$d_1 = \frac{\ln(25/20) + [0.05 + 0.16/2] \times 0.25}{0.4 \sqrt{0.25}} = \frac{\ln(1.25) + 0.13 \times 0.25}{0.4 \times 0.5}$
$= \frac{0.2231 + 0.0325}{0.2} = \frac{0.2556}{0.2} = 1.278$

**Step 2 — d₂:**
$d_2 = d_1 - \sigma \sqrt{t} = 1.278 - 0.4 \times 0.5 = 1.278 - 0.2 = 1.078$

**Step 3 — Cumulative normals (from table or NORM.DIST):**
$N(d_1) = N(1.278) = 0.8994$
$N(d_2) = N(1.078) = 0.8595$

**Step 4 — Call value:**
$V_{CO} = 25 \times 0.8994 - 20 \times e^{-0.0125} \times 0.8595$
$= 22.485 - 20 \times 0.9875 \times 0.8595$
$= 22.485 - 16.97513$
$= ₹5.5099$

**If it were a put (same data):**
$V_{PO} = 20 \times 0.9875 \times [1 - 0.8595] - 25 \times [1 - 0.8994]$
$= 2.7748 - 2.515 = ₹0.2598$

#### Example (Check Your Progress 3.2) — Worked
**Inputs:** P = ₹35, Y = ₹35, r = 10% (= 0.10), t = 1 year, σ² = 0.04 → σ = 0.20.

$d_1 = \frac{\ln(35/35) + [0.10 + 0.04/2] \times 1}{0.20 \sqrt{1}} = \frac{0 + 0.12}{0.20} = 0.6$

$d_2 = 0.6 - 0.20 \times 1 = 0.4$

$N(0.6) = 0.7257$; $N(0.4) = 0.6554$.

$V_{CO} = 35 \times 0.7257 - 35 \times e^{-0.10} \times 0.6554$
$= 35 \times 0.7257 - 35 \times 0.9048 \times 0.6554$
$\approx 25.40 - 20.755 = ₹4.644$

$V_{PO} = 35 \times 0.9048 \times [1 - 0.6554] - 35 \times [1 - 0.7257]$
$= 11.91024 - 9.6005 = ₹1.312$

### ⚠️ Common Mistakes
- ❌ Using simple compounding for $e^{-rt}$ → ✅ The model uses *continuously* compounded $r$.
- ❌ Forgetting $\sigma$ vs $\sigma^2$ — formula uses $\sigma$ in $d_1$, $d_2$ denominators, but $\sigma^2$ in the $d_1$ numerator's drift term.
- ❌ Applying Black-Scholes to American options → ✅ Black-Scholes prices European only; American options need binomial / lattice methods.

### Advantages / Limitations summary
| Aspect | Status |
|---|---|
| **Speed** | ✅ Major advantage — fast for many options |
| **Closed form** | ✅ No iteration needed |
| **American options** | ❌ Cannot price — only at expiry, no early-exercise step |
| **Dividend-paying stocks** | ❌ Standard form excludes them |
| **Volatility** | Assumes σ known and constant |

> **Quick Recall:**
> - 1973, Black & Scholes (with Merton).
> - $V_{CO} = P \cdot N(d_1) - Y e^{-rt} \cdot N(d_2)$.
> - 6 assumptions: no dividends, no costs, constant r, European, short selling allowed, random stock moves.
> - Worked Ex 21.1: VCO = ₹5.5099, VPO = ₹0.2598.

---

## Section: 21.4.3 Relation between Binomial & Black-Scholes 🟡

### Core Idea
Both models share the same **stochastic foundation** — geometric Brownian motion for stock prices. The binomial model with **infinite steps** converges to the Black-Scholes formula for European options. So Black-Scholes ≡ continuous limit of the binomial; binomial ≡ discrete approximation of Black-Scholes.

### Key Concepts
- **Convergence** — as N → ∞ in the binomial tree, prices → Black-Scholes value.
- **Practical takeaway**: use Black-Scholes for European; use binomial for American or dividend-paying.

> **Quick Recall:**
> - Binomial (discrete) ↔ Black-Scholes (continuous), same GBM foundation.
> - Black-Scholes is the limit of binomial as steps → ∞.

---

## Section: 21.5 Market of Derivatives in India 🟡

### Core Idea
India has **two derivative markets**: exchange-traded (standardised) and OTC (decentralised, bilateral). **SEBI** regulates derivatives. Trading happens on NSE, BSE for equities/indices; on MCX, NCDEX for commodities; on MSE for currencies.

### Key Concepts

#### Two market types
| Market | Nature | Examples |
|---|---|---|
| Exchange-traded | Standardised contracts on an exchange | NSE F&O, BSE F&O |
| OTC | Decentralised, bilateral | Customised forwards |

#### Cash market vs Derivative market
| Aspect | Cash market | Derivative market |
|---|---|---|
| Settlement | On the spot | At a future date |
| Participants | Spot traders | Futures traders |
| Mode | Physical commodity | Derivative contract |

#### Indian derivatives — milestones
- **June 2000** — first derivatives contract on **BSE**.
- **June 12, 2000** — NSE launches **index futures** on Nifty 50.
- **June 4, 2001** — NSE launches **index options** on Nifty 50.
- **July 2, 2001** — NSE first to launch **options on individual securities**.
- **November 9, 2001** — NSE launches **futures on individual securities**.
- **Today** — NSE F&O on 5 major indices (Nifty 50, Nifty Bank, Nifty Financial Services, Nifty Midcap Select, Nifty Next 50) + 180+ securities.

#### Commodity & currency
- **MCX** and **NCDEX** (Ministry of Finance, GoI) — commodity derivatives.
- **MSE** (Metropolitan Stock Exchange, MoF) — currency derivatives.

### Definitions
- **SEBI**: regulator of the derivative market in India.
- **Nifty F&O**: NSE's derivatives platform for Nifty futures and options.

> **Quick Recall:**
> - 2 markets: exchange-traded vs OTC.
> - SEBI regulates.
> - 2000 — first derivative on BSE; same year NSE launches index futures.
> - NSE launched single-stock options (July 2001) before single-stock futures (November 2001).

---

## Section: 21.6–21.7 Unit 21 Summary & Key Words 🟢

### Unit 21 Key Words (glossary)
| Term | Meaning |
|---|---|
| Arbitrageur | Investor exploiting price discrepancies for risk-free profit. |
| Call option | Right to *buy* at a predetermined price. |
| Put option | Right to *sell* at a predetermined price. |
| Forward contract | Bilateral agreement to exchange asset for cash at a future date at price fixed today. |
| Hedge | Investment to offset losses in another investment. |
| Interest rate future | Futures on fixed-income securities (T-bills, bonds, CDs). |
| Interest rate option | Option on fixed-income securities. |
| Interest rate parity | Difference in interest rates between two countries = forward-spot rate disparity. |
| Long position | Buyer; entitled to receive asset. |
| Short position | Seller; obligated to deliver asset. |
| Margin | Portion of transaction value paid upfront; **initial margin** vs **maintenance margin**. |
| Spot rate | Exchange rate for immediate delivery (settles ~T+2). |
| Swap contract | Counterparties exchange cash flows at predetermined intervals. |

### Connections
- **Builds on**: Unit 13 (basic derivatives), §21.3 (forwards, futures, options, swaps).
- **Pairs with**: Risk-return + portfolio theory (Units 18-19) — derivatives are risk-management tools.
<!-- Continues into chunk 008: Unit 22 — Corporate Finance -->
