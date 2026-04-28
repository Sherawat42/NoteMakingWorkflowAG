# Chunk 002 — Portfolio Valuation, Returns, & Markowitz Theory
<!-- Pages: 9-18 -->
<!-- Source: chunk_002.txt -->
<!-- Continues from: Unit 18 (Risk-Return basics, chunk 001) -->

## Section: 18.4 Valuation of Portfolio 🟡

### Core Idea
Portfolio valuation is computing the worth of an entire investment portfolio at a point in time. It is essential for performance evaluation, decision-making, and stakeholder transparency, and is built up by valuing each constituent asset and adding them in proportion to holdings.

> **In Simple Terms:** Like checking the total bill at a buffet — count each plate's price (asset) times how many you took (shares), then add them up.

### Key Concepts

#### Portfolio value formula
For a portfolio of *n* assets with share price $P_i$ and number of shares $N_i$:

$$V = N_1 P_1 + N_2 P_2 + \cdots + N_n P_n = \sum_{i=1}^{n} N_i P_i$$

A typical portfolio has $V > 0$.

#### Portfolio weights
Weight of asset *i* in portfolio:

$$w_i = \frac{N_i P_i}{N_1 P_1 + N_2 P_2 + \cdots + N_n P_n} = \frac{N_i P_i}{V}$$

By construction, $\sum w_i = 1$.

#### Factors affecting portfolio valuation
1. **Asset evaluation** — value individual assets via DCF, P/E ratios, comparative company analysis.
2. **Market dynamics** — fluctuations in market conditions and liquidity affect asset prices; regular monitoring needed.
3. **Impact of diversification** — diversified portfolios may show reduced volatility and higher valuation metrics due to risk mitigation.

### Definitions
- **Portfolio valuation**: assessing the worth of each asset in a portfolio at a point in time, using market prices, potential earnings, and intrinsic value.
- **Portfolio weight ($w_i$)**: share of asset *i*'s value in the total portfolio value, $N_i P_i / V$.

> **Quick Recall:**
> - $V = \sum N_i P_i$, $w_i = N_i P_i / V$, $\sum w_i = 1$.
> - DCF, P/E, comparable-company are the asset-evaluation tools listed.

---

## Section: 18.4.2 Expected Return and Risk from a Portfolio 🔴

### Core Idea
Portfolio return is a **weighted average of individual asset returns**, but portfolio variance is **not** a simple weighted average — it depends on **covariances/correlations** between assets. This is the central insight enabling diversification benefit.

> **In Simple Terms:** If you mix two ingredients, the average sweetness is just the weighted average. But the *texture* (risk) depends on how the ingredients interact — sometimes they reinforce each other, sometimes they cancel out.

### Key Concepts

#### Portfolio return
For weights $\{w_1, w_2, \dots, w_n\}$ with $\sum w_i = 1$:

$$\tilde{r}_p = w_1 \tilde{r}_1 + w_2 \tilde{r}_2 + \cdots + w_n \tilde{r}_n$$

#### Expected portfolio return
$$\bar{r}_p = E[r_p] = w_1 \bar{r}_1 + w_2 \bar{r}_2 + \cdots + w_n \bar{r}_n$$

#### Portfolio variance — n-security general form
$$\sigma_p^2 = \sum_{i=1}^{n} \sum_{j=1}^{n} x_i x_j \rho_{ij} \sigma_i \sigma_j$$

Where:
- $\sigma_p^2$ = portfolio variance
- $x_i, x_j$ = proportions of total investment in assets *i* and *j*
- $\rho_{ij}$ = correlation in returns of securities *i* and *j*
- $\sigma_i, \sigma_j$ = security standard deviations

#### Two-security case (memorise this form)
$$\sigma_p^2 = x_A^2 \sigma_A^2 + x_B^2 \sigma_B^2 + 2 x_A x_B \rho_{AB} \sigma_A \sigma_B$$

The total risk has **three components**:
1. Variance of stock A.
2. Variance of stock B.
3. **Interactive risk** — from the relationship between A and B's returns (the cross-term).

### Definitions
- **Interactive risk**: the cross-term $2 x_A x_B \rho_{AB} \sigma_A \sigma_B$ — risk arising from the relationship/correlation between assets, not from individual assets alone. ⭐ (exam-important)

### Mechanisms / Processes — How a manager reduces risk
- Manager has **no control over individual securities' variances**.
- Has control over **selection of portfolios** — choose securities with **least correlation** between them so cross/interaction terms shrink → total portfolio risk falls.
- As *n* grows: 4 securities → 4 variance terms + 8 covariance interaction terms (in 2-side n×n covariance matrix). Number of interaction terms grows much faster than variance terms — diversification's main lever.

### ⚠️ Common Mistakes
- ❌ "Portfolio variance is just $\sum w_i^2 \sigma_i^2$" → ✅ Wrong — must include $\rho_{ij}$ cross-terms; correlation can lower the total below the weighted average.
- ❌ Forgetting the factor of 2 in the cross-term for two securities.

> **Quick Recall:**
> - Portfolio return = weighted average. Portfolio variance ≠ weighted average — depends on $\rho_{ij}$.
> - 2-asset variance: $x_A^2 \sigma_A^2 + x_B^2 \sigma_B^2 + 2 x_A x_B \rho_{AB} \sigma_A \sigma_B$.
> - Lower $\rho_{ij}$ → bigger diversification benefit.

### Connections
- **Builds on**: §18.3.2 Variance & SD (chunk 001) — extends single-asset risk measure to a portfolio.
- **Is prerequisite for**: §18.5 Markowitz Portfolio Theory (this chunk) — the variance formula is what Markowitz minimises.

---

## Section: 18.5 Markowitz Portfolio Theory 🔴

### Core Idea
**Modern Portfolio Theory (MPT)** — Harry Markowitz, "Portfolio Selection," *Journal of Finance* (1952). Risk-averse investors can construct portfolios that maximise expected return for a given level of market risk. The breakthrough: success is not simply choosing the lowest-risk securities, but combining securities so that *portfolio* variance is low — i.e., exploiting **correlation between securities**.

> **In Simple Terms:** Don't pick "safest 5 stocks". Pick stocks whose ups and downs cancel out. A pair of moderately risky stocks that move opposite to each other can give a *less* risky portfolio than two "safe" stocks that move together.

### Key Concepts

#### Traditional vs Modern Portfolio Theory

| Aspect | Traditional Theory | Markowitz / MPT |
|---|---|---|
| Focus | Individual securities | Portfolio as a whole |
| Risk measure | SD of individual security returns | Portfolio SD (uses covariances) |
| Selection rule | Pick assets with lowest variability | Combine assets with low correlation |
| Inputs | Dividend, P/E, holding period, market value | Expected returns + covariance/correlation matrix |

#### Mean-variance model
MPT is also called the **mean-variance model** because portfolios are evaluated on (expected return, SD). It analyses many possible portfolios of given assets and finds the most efficient one.

#### Dominance / efficiency definition
A portfolio **dominates** another if it has either:
- Lower SD with the same expected return, OR
- Higher expected return with the same SD.

A portfolio is **efficient** if no other portfolio offers a higher expected return at same/lower risk, or lower risk at same/higher expected return.

#### Markowitz Diversification
The term "Markowitz Diversification" still refers today to portfolio construction that uses security **covariances** (not just spreading capital across many names).

### Definitions
- **Modern Portfolio Theory (MPT)**: Markowitz's 1952 theory that risk-averse investors construct portfolios to maximise expected return for a given level of market risk by exploiting correlation between securities. ⭐ (exam-important)
- **Mean-variance model**: alternative name for Markowitz model — portfolios judged on mean (expected return) and variance.
- **Markowitz diversification**: portfolio construction using security covariances.
- **Security universe**: the entire collection of alternatives from which specific investment choices are made.
- **Efficient portfolio**: a portfolio where no higher expected return can be attained without accepting higher risk, and no greater certainty of returns without sacrificing return. ⭐ (exam-important)

### Assumptions of the Markowitz Model (memorise — list of 9)
1. Investors are rational.
2. Supply-demand equilibrium is instantly achieved.
3. There are no arbitrage opportunities.
4. Price moves are efficient.
5. All participants have access to information.
6. The market is liquid.
7. There are no transaction costs.
8. There are no taxes.
9. Everyone has the same opportunity for borrowing and lending.

> **Quick Recall:**
> - 1952, Harry Markowitz, "Portfolio Selection".
> - Risk = portfolio SD (uses covariance matrix).
> - 9 assumptions — most often cited as unrealistic: rational investors, no taxes/transaction costs, equal borrow/lend access.

---

## Section: 18.5.2 Opportunity Set / Feasible Set 🟡

### Core Idea
With *n* securities, an investor can form many portfolios by varying weights. The set of all such portfolios is the **opportunities set / feasible set**. Each portfolio is a (expected return, SD) point. Some portfolios in this set are dominated by others — investors discard those.

### Key Concepts
- **Feasible set** = all combinations attainable from the given securities.
- **Inefficient portfolios** lie inside the frontier; they are dominated.
- **Efficient portfolios** sit on the upper-left edge of the feasible set — best risk-return trade-off.

> **Quick Recall:**
> - Feasible set is huge; the efficient subset is a curve along its upper-left boundary.

---

## Section: 18.5.3 Efficient Portfolio Frontier 🔴

### Core Idea
The **Efficient Frontier** is the curve of efficient portfolios — those offering the highest expected return for each level of risk (or equivalently, lowest risk for each level of expected return). Investors choose a point on this curve matching their risk-return preference.

### Key Concepts

#### Reading Figure 18.1 (Efficient Portfolio Frontier)
- Y-axis: Expected portfolio return; X-axis: Portfolio risk (SD).
- **Curve = efficient frontier** — the upper-left boundary of feasible portfolios.
- **Inside the curve** = inefficient portfolios (less return for same risk).
- **Outside the curve** = unobtainable / infeasible (more return than possible at given risk).
- **Portfolio A** = minimum-risk portfolio (does *not* mean "all in safest asset" — diversification means A typically has multiple assets).
- **Portfolio C** = maximum-return = maximum-risk portfolio (often 100% in highest-return asset).
- **Portfolio B** = balanced choice between A and C — typical investor preference.

#### Why Portfolio A is not 100% in safest asset
Because **diversification across asset classes with varying risks** can drive *portfolio* risk below the risk of even the safest single asset (when correlations are low/negative).

### Definitions
- **Efficient (Portfolio) Frontier**: the set of portfolios that yield the highest expected return for each given level of risk; the upper-left boundary of the feasible set. ⭐ (exam-important)
- **Unobtainable portfolio**: a (return, risk) point above the frontier — return higher than achievable at that risk level.
- **Inefficient portfolio**: a feasible portfolio dominated by another — less return at the same risk or more risk at the same return.

### ⚠️ Common Mistakes
- ❌ Drawing the frontier as a straight line → ✅ It is a curve (concave, upper-left of feasible set).
- ❌ "Min-risk portfolio = 100% safest asset" → ✅ Often a *combination* of assets that exploits correlations.

> **Quick Recall:**
> - Frontier = upper-left boundary; inside = inefficient; outside = infeasible.
> - A = min-risk; C = max-return / max-risk; B = balanced.

---

## Section: 18.5.4 Criticisms of Markowitz Portfolio Theory 🔴

### Core Idea
Markowitz's framework is foundational but rests on strong assumptions that fail in practice. Standard exam answer: list seven criticisms.

### Key Concepts — 7 Criticisms (exam-tested)
1. **Unrealistic assumptions** — rational investors, unlimited borrowing/lending at risk-free rate, identical risk preferences. Real investors deviate.
2. **Complexity & practicality** — intricate calculations; correlations and expected returns hard to estimate.
3. **Sensitivity to input data** — small input changes (expected returns, covariances) → very different portfolios → unstable, hard to rely on.
4. **Neglect of transaction costs and taxes** — assumes none; real rebalancing eats into returns.
5. **Single-period analysis** — ignores dynamic markets and time-varying preferences → suboptimal in practice.
6. **Ignorance of behavioural finance** — herd mentality, overconfidence, loss aversion not modelled, but they shape decisions.
7. **Inability to capture tail risks** — extreme events / market crashes underestimated → potential losses understated.

### ⚠️ Common Mistakes
- ❌ Saying "Markowitz ignores covariances" → ✅ It *uses* covariances; it ignores transaction costs, taxes, multi-period, behavioural biases, tail risks.

> **Quick Recall:**
> - 7 criticisms: assumptions, complexity, input sensitivity, no costs/taxes, single-period, no behavioural finance, no tail risk.

---

## Section: 18.6 Let Us Sum Up 🟢

> **Unit 18 in one breath:** Diversification + portfolio management + risk-return measurement → Markowitz's mean-variance model → efficient frontier as the curve of best portfolios → criticisms (assumptions, complexity, input sensitivity, taxes/costs, single period, behavioural, tail risk).

### Key Words (Unit 18 Glossary)
| Term | Definition |
|---|---|
| Diversification | Spreading investments across assets/asset classes to mitigate risk and optimise returns. |
| Markowitz Portfolio Theory | Risk-averse investors construct portfolios to maximise expected return for a given level of market risk; risk inherent to higher reward. |
| Efficient Portfolio Frontier | Set of portfolios expected to provide the highest returns at a given level of risk. |
| Portfolio | Collection of investments owned by an entity (stocks, bonds, MFs, real estate). |
| Portfolio management | Practice of overseeing and optimising portfolios — allocate, balance risk-return, adapt. |
| Diversifiable risk | Firm-specific risks affecting individual stocks. |
| Non-diversifiable risk | Market/sector-wide risk influenced by economy-wide factors. |
| Expected returns | Anticipated profit/loss from an investment within a timeframe. |

### Useful Books (mentioned)
- Strong, R. A. (2006). *Portfolio construction, management and protection.*
- Mishkin & Eakins (2006). *Financial markets and institutions.*
- Counsel, I. (2008). *Portfolio Management: Theory & Practice.*
- Dicksler & Samuelson (1974). *Investment Portfolio Decision-Making.*

### Connections
- **Builds on**: §18.3 (risk types), §18.3.2 (variance/SD).
- **Is prerequisite for**: Unit 19 CAPM (chunk 003+) — which introduces β as the market-risk measure for the systematic-risk component MPT does not price separately.

### Open Questions
1. How is the efficient frontier modified when a risk-free asset is introduced? (Capital Allocation Line — addressed in CAPM, Unit 19.)
2. How sensitive is the frontier shape to estimation error in expected returns vs. covariances?
<!-- Continues into chunk 003: Unit 19 CAPM begins -->
