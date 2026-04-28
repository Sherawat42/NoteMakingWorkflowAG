# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

- **Diversification**: spreading investments across various assets and asset classes to mitigate risk and optimize returns. ⭐ (exam-important)

**Quick Recall:**
- Diversification ≠ avoiding risk; it is *managing* risk by combining assets whose returns don't move together.
- Portfolio theory answers: how to diversify, which assets to pick, how to combine, what is portfolio risk, what is expected return.
| Aspect | Active Management | Passive Management |
|--------|-------------------|--------------------|
| Goal | Outperform the market | Match market returns |
| Returns | Potentially higher | Market-based, in diversified portfolios |
| Risk | Greater chance of missing target | Lower risk of underperformance |
| Use case | Beat benchmark | Solve cash-flow / diversification problem |
- **Portfolio management**: the practice of overseeing and optimizing investment collections — allocating resources, balancing risk and return, and adapting to market changes. ⭐ (exam-important)

**Quick Recall:**
- 5 stages: policy → strategy → selection → monitoring → review.
- 7 benefits — note the qualitative one (#7) is often overlooked in exams.

### 18.3 Relationship between Risk and Return 🔴

**Risk aversion**

**Active vs Passive — strategy choice**
- **Cash-flow problem over time** → passive (diversified, market-based returns).
- **Outperform the market** → active (aim higher, accept higher risk of underperforming).
- **Total risk**: the overall variability of returns of a financial asset; combines diversifiable and non-diversifiable risks. ⭐ (exam-important)

**Quick Recall:**
- Total risk = Diversifiable risk + Non-diversifiable risk.
- Risk-averse investor = demands compensation, doesn't reject risk outright.

### 18.3.1 Types of Risk — Diversifiable vs Non-Diversifiable 🔴
| Aspect | Diversifiable / Unsystematic Risk | Non-Diversifiable / Systematic Risk |
|--------|-----------------------------------|-------------------------------------|
| Also called | Unique risk, firm-specific risk | Market risk, non-diversifiable risk |
| Source | Firm- or industry-specific events | Macroeconomic, geopolitical, market-wide events |
| Examples | Scams, labour strikes, regulatory penalty, management change, internal issues, firm-specific news | COVID-19, monetary policy, geopolitical conflict, natural disasters |
| Components | Business risk, financial risk, management risk | Market sentiment, macroeconomic indicators |
| Can be eliminated? | Yes — through diversification | No — inherent in the market |
| Mitigation tool | Spread investments across assets/sectors | Asset allocation, hedging |
| Investor control | Reducible | Cannot control, minimise, or avoid |
- **Diversifiable risk (unsystematic risk / unique risk)**: firm-specific risks that affect individual stock prices rather than the entire industry or sector. Can be mitigated through diversification. ⭐ (exam-important)
- **Systematic risk (non-diversifiable risk / market risk)**: risks that affect the overall market or a sector; influenced by macroeconomic indicators, market sentiment, geopolitical events. Cannot be eliminated through diversification. ⭐ (exam-important)
- **COVID-19** — systematic risk because it impacted the *entire* stock market, no diversification within equities could have escaped it.
- **Labour strike at Company X** — diversifiable; if you also held Companies Y and Z, the impact on portfolio is muted.

### ⚠️ Common Mistakes
- ❌ "Diversification eliminates all risk" → ✅ It only eliminates *unsystematic* risk; market risk remains.
- ❌ Confusing "non-diversifiable" with "uncontrollable for the firm". → ✅ It means uncontrollable *for the investor through diversification*. The investor still has tools (asset allocation, hedging).

**Quick Recall:**
- Unsystematic = firm-level → diversifiable.
- Systematic = market-level → non-diversifiable.
- Total risk = systematic + unsystematic.
---

### 18.3.2 Measuring Risks — Variance & Standard Deviation 🔴

**Variance**
- $R_i$ = the *i*-th possible return (i = 1 … n)
- $E(R)$ = expected value of the investment
- $P_i$ = probability of the *i*-th return

**Standard deviation**
- **Variance ($\sigma^2$)**: probability-weighted average of squared deviations of returns from their expected value. ⭐ (exam-important)
- **Standard deviation ($\sigma$)**: square root of variance; standard measure of an asset's total risk. ⭐ (exam-important)

**Quick Recall:**
- Higher σ = higher risk.
- σ has same units as return; σ² does not — always report σ when comparing risk.

### 18.3.3 Expected Returns 🔴

**Formula**
- $E(R)$ = expected return on the investment
- $n$ = number of possible outcomes
- $R_i$ = the *i*-th possible return
- $P_i$ = probability of $R_i$
- **Expected return**: anticipated profit/loss from an investment within a specific timeframe; the probability-weighted average of possible returns. ⭐ (exam-important)
| Economic condition | R_A (%) | R_B (%) | Probability |
|---|---|---|---|
| Boom | 15 | 12 | 0.5 |
| Depression | 5 | 7 | 0.5 |
- $E(R_A) = 0.5 \times 15 + 0.5 \times 5 = 7.5 + 2.5 = 11.0\%$
- $E(R_B) = 0.5 \times 12 + 0.5 \times 7 = 6.0 + 3.5 = 9.5\%$
| Condition | $R_A$ | $R_A - E(R)$ | $(R_A - E(R))^2$ | P | $(R_A - E(R))^2 \times P$ |
|---|---|---|---|---|---|
| Boom | 15 | 4 | 16 | 0.5 | 8 |
| Depression | 5 | -6 | 36 | 0.5 | 18 |
| | | | | **Var** | **26** |
| Condition | $R_B$ | $R_B - E(R)$ | $(R_B - E(R))^2$ | P | $(R_B - E(R))^2 \times P$ |
|---|---|---|---|---|---|
| Boom | 12 | 2.5 | 6.25 | 0.5 | 3.125 |
| Depression | 7 | -2.5 | 6.25 | 0.5 | 3.125 |
| | | | | **Var** | **6.25** |

### ⚠️ Common Mistakes
- ❌ Forgetting to multiply squared deviations by probability — gives sum of squares, not variance.
- ❌ Reporting variance as the risk measure when standard deviation is asked — variance is in % squared, σ is in %.

**Quick Recall:**
- $E(R) = \sum R_i P_i$.
- $\sigma^2 = \sum [R_i - E(R)]^2 P_i$, $\sigma = \sqrt{\sigma^2}$.
- In Example 18.1: A → (E(R)=11, σ=5.09); B → (E(R)=9.5, σ=2.5). Higher reward, higher risk.
- **Builds on**: Diversification & risk types (this chunk) — sets the measurement tools needed to combine assets in §18.4.
- **Is prerequisite for**: §18.4 Valuation of Portfolio and §18.5 Markowitz Portfolio Theory (next chunk).
- **Pairs with**: CAPM (Unit 19) — which introduces β as the systematic-risk measure.

**Quick Recall:**
- $V = \sum N_i P_i$, $w_i = N_i P_i / V$, $\sum w_i = 1$.
- DCF, P/E, comparable-company are the asset-evaluation tools listed.

### 18.4.2 Expected Return and Risk from a Portfolio 🔴

**Portfolio return**

**Expected portfolio return**

**Portfolio variance — n-security general form**
- $\sigma_p^2$ = portfolio variance
- $x_i, x_j$ = proportions of total investment in assets *i* and *j*
- $\rho_{ij}$ = correlation in returns of securities *i* and *j*
- $\sigma_i, \sigma_j$ = security standard deviations

**Two-security case (memorise this form)**
1. Variance of stock A.
2. Variance of stock B.
3. **Interactive risk** — from the relationship between A and B's returns (the cross-term).
- **Interactive risk**: the cross-term $2 x_A x_B \rho_{AB} \sigma_A \sigma_B$ — risk arising from the relationship/correlation between assets, not from individual assets alone. ⭐ (exam-important)
- Manager has **no control over individual securities' variances**.
- Has control over **selection of portfolios** — choose securities with **least correlation** between them so cross/interaction terms shrink → total portfolio risk falls.
- As *n* grows: 4 securities → 4 variance terms + 8 covariance interaction terms (in 2-side n×n covariance matrix). Number of interaction terms grows much faster than variance terms — diversification's main lever.

### ⚠️ Common Mistakes
- ❌ "Portfolio variance is just $\sum w_i^2 \sigma_i^2$" → ✅ Wrong — must include $\rho_{ij}$ cross-terms; correlation can lower the total below the weighted average.
- ❌ Forgetting the factor of 2 in the cross-term for two securities.

**Quick Recall:**
- Portfolio return = weighted average. Portfolio variance ≠ weighted average — depends on $\rho_{ij}$.
- 2-asset variance: $x_A^2 \sigma_A^2 + x_B^2 \sigma_B^2 + 2 x_A x_B \rho_{AB} \sigma_A \sigma_B$.
- Lower $\rho_{ij}$ → bigger diversification benefit.
- **Builds on**: §18.3.2 Variance & SD (chunk 001) — extends single-asset risk measure to a portfolio.
- **Is prerequisite for**: §18.5 Markowitz Portfolio Theory (this chunk) — the variance formula is what Markowitz minimises.

### 18.5 Markowitz Portfolio Theory 🔴

**Traditional vs Modern Portfolio Theory**
| Aspect | Traditional Theory | Markowitz / MPT |
|---|---|---|
| Focus | Individual securities | Portfolio as a whole |
| Risk measure | SD of individual security returns | Portfolio SD (uses covariances) |
| Selection rule | Pick assets with lowest variability | Combine assets with low correlation |
| Inputs | Dividend, P/E, holding period, market value | Expected returns + covariance/correlation matrix |

**Mean-variance model**

**Dominance / efficiency definition**
- Lower SD with the same expected return, OR
- Higher expected return with the same SD.

**Markowitz Diversification**
- **Modern Portfolio Theory (MPT)**: Markowitz's 1952 theory that risk-averse investors construct portfolios to maximise expected return for a given level of market risk by exploiting correlation between securities. ⭐ (exam-important)
- **Mean-variance model**: alternative name for Markowitz model — portfolios judged on mean (expected return) and variance.
- **Markowitz diversification**: portfolio construction using security covariances.
- **Security universe**: the entire collection of alternatives from which specific investment choices are made.
- **Efficient portfolio**: a portfolio where no higher expected return can be attained without accepting higher risk, and no greater certainty of returns without sacrificing return. ⭐ (exam-important)
1. Investors are rational.
2. Supply-demand equilibrium is instantly achieved.
3. There are no arbitrage opportunities.
4. Price moves are efficient.
5. All participants have access to information.
6. The market is liquid.
7. There are no transaction costs.
8. There are no taxes.
9. Everyone has the same opportunity for borrowing and lending.

**Quick Recall:**
- 1952, Harry Markowitz, "Portfolio Selection".
- Risk = portfolio SD (uses covariance matrix).
- 9 assumptions — most often cited as unrealistic: rational investors, no taxes/transaction costs, equal borrow/lend access.

**Quick Recall:**
- Feasible set is huge; the efficient subset is a curve along its upper-left boundary.

### 18.5.3 Efficient Portfolio Frontier 🔴

**Reading Figure 18.1 (Efficient Portfolio Frontier)**
- Y-axis: Expected portfolio return; X-axis: Portfolio risk (SD).
- **Curve = efficient frontier** — the upper-left boundary of feasible portfolios.
- **Inside the curve** = inefficient portfolios (less return for same risk).
- **Outside the curve** = unobtainable / infeasible (more return than possible at given risk).
- **Portfolio A** = minimum-risk portfolio (does *not* mean "all in safest asset" — diversification means A typically has multiple assets).
- **Portfolio C** = maximum-return = maximum-risk portfolio (often 100% in highest-return asset).
- **Portfolio B** = balanced choice between A and C — typical investor preference.

**Why Portfolio A is not 100% in safest asset**
- **Efficient (Portfolio) Frontier**: the set of portfolios that yield the highest expected return for each given level of risk; the upper-left boundary of the feasible set. ⭐ (exam-important)
- **Unobtainable portfolio**: a (return, risk) point above the frontier — return higher than achievable at that risk level.
- **Inefficient portfolio**: a feasible portfolio dominated by another — less return at the same risk or more risk at the same return.

### ⚠️ Common Mistakes
- ❌ Drawing the frontier as a straight line → ✅ It is a curve (concave, upper-left of feasible set).
- ❌ "Min-risk portfolio = 100% safest asset" → ✅ Often a *combination* of assets that exploits correlations.

**Quick Recall:**
- Frontier = upper-left boundary; inside = inefficient; outside = infeasible.
- A = min-risk; C = max-return / max-risk; B = balanced.
---

### 18.5.4 Criticisms of Markowitz Portfolio Theory 🔴
1. **Unrealistic assumptions** — rational investors, unlimited borrowing/lending at risk-free rate, identical risk preferences. Real investors deviate.
2. **Complexity & practicality** — intricate calculations; correlations and expected returns hard to estimate.
3. **Sensitivity to input data** — small input changes (expected returns, covariances) → very different portfolios → unstable, hard to rely on.
4. **Neglect of transaction costs and taxes** — assumes none; real rebalancing eats into returns.
5. **Single-period analysis** — ignores dynamic markets and time-varying preferences → suboptimal in practice.
6. **Ignorance of behavioural finance** — herd mentality, overconfidence, loss aversion not modelled, but they shape decisions.
7. **Inability to capture tail risks** — extreme events / market crashes underestimated → potential losses understated.

### ⚠️ Common Mistakes
- ❌ Saying "Markowitz ignores covariances" → ✅ It *uses* covariances; it ignores transaction costs, taxes, multi-period, behavioural biases, tail risks.

**Quick Recall:**
- 7 criticisms: assumptions, complexity, input sensitivity, no costs/taxes, single-period, no behavioural finance, no tail risk.
---
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

### 19.2 The Capital Asset Pricing Model (CAPM) 🔴

**Building blocks of CAPM**
| Concept | Meaning |
|---|---|
| **Systematic risk** | Risk that cannot be diversified away — economic downturns, interest-rate moves, geopolitics. |
| **Beta (β)** | Sensitivity of an asset's returns to changes in the overall market. β = 1: moves with market; β > 1: more volatile; β < 1: less volatile. |
| **Risk-free rate ($R_f$)** | Return on a zero-risk investment, typically the yield on government bonds. Baseline. |
| **Market risk premium ($R_m - R_f$)** | Additional return investors demand for bearing systematic risk; expected market return minus the risk-free rate. |
| **Market portfolio** | A diversified portfolio containing all risky assets, weighted by market capitalisation. Benchmark in CAPM. |

**CAPM Equation**
- $E(R_i)$ = expected return of asset *i*
- $R_f$ = risk-free rate (proxy: government bond yield)
- $\beta_i$ = beta of asset *i* (systematic-risk sensitivity)
- $R_m$ = expected return on the market portfolio (proxy: broad index, e.g., S&P 500)
- $(R_m - R_f)$ = market risk premium
- **Capital Asset Pricing Model (CAPM)**: a single-factor model linking expected return on an asset to its systematic risk, $E(R_i) = R_f + \beta_i (R_m - R_f)$. ⭐ (exam-important)
- **Beta (β)**: measure of an asset's sensitivity to market movements (= cov(R_i, R_m) / var(R_m), implicitly). β = 1 ↔ moves with market; β > 1 ↔ more volatile; β < 1 ↔ less volatile. ⭐ (exam-important)
- **Risk-free rate ($R_f$)**: return on a zero-risk asset; typically yield on government bonds. ⭐ (exam-important)
- **Market risk premium**: $R_m - R_f$ — excess return demanded for bearing systematic risk. ⭐ (exam-important)
- **Market portfolio**: a diversified portfolio of all risky assets, weighted by market capitalisation.
1. **Systematic risk emphasis** — only non-diversifiable risk is priced.
2. **Single-factor model** — β is the sole risk measure.
3. **Risk-return relationship** — quantifies that higher β → higher required return.
4. **Market portfolio as benchmark** — performance/risk judged relative to it.
5. **Risk-free rate incorporation** — separates baseline return from systematic-risk premium.
6. **Equilibrium pricing** — assumes asset prices adjust so expected returns align with β; in equilibrium, all assets sit on the SML.
7. **Universal applicability** — works for stocks, bonds, and other instruments across markets.

### ⚠️ Common Mistakes
- ❌ "CAPM prices total risk" → ✅ CAPM prices only **systematic** risk; unsystematic risk earns no premium because it can be diversified away.
- ❌ Using a stock index as the risk-free rate → ✅ Use a *short-term government security* yield.

**Quick Recall:**
- Founders: Sharpe, Lintner, Mossin (1960s).
- Equation: $E(R_i) = R_f + \beta_i (R_m - R_f)$.
- Single factor: β.
- Only systematic risk earns a premium.
---

### 19.3 Sharpe Ratio (Importance of Sharpe's Theory) 🔴

**Formula**
- $R_p$ = expected return on the investment / portfolio
- $R_f$ = risk-free rate (yield on government bonds)
- $\sigma_p$ = standard deviation of portfolio returns (volatility / risk)

**Six objectives / functions of the Sharpe ratio**
1. **Objective measurement of risk-adjusted performance** — standardised metric; lets investors compare across investments consistently.
2. **Quantifying the risk-return tradeoff** — excess return per unit of risk; tells you whether reward compensates for volatility.
3. **Portfolio allocation decision** — pick portfolios with the highest return per unit of risk.
4. **Performance evaluation tool** — gauge skill of fund managers vs. benchmark / peers.
5. **Risk management tool** — manage exposures, ensure diversification, optimise risk-return per investor's preferences.
6. **Benchmark comparison** — compare a portfolio's risk-adjusted return to a market index or target return.
- **Sharpe ratio**: a measure of risk-adjusted return, $(R_p - R_f) / \sigma_p$ — excess return per unit of total risk. ⭐ (exam-important)
- **Excess return**: $R_p - R_f$ — return above the risk-free rate.

**Quick Recall:**
- SR = (R_p − R_f) / σ_p.
- Numerator: excess return; Denominator: total risk (σ_p, NOT β).
- Higher SR = better risk-adjusted performance.

### ⚠️ Common Mistakes
- ❌ Using β in the denominator → ✅ That is the **Treynor ratio**. Sharpe uses **σ_p** (total risk).
- ❌ Forgetting to subtract $R_f$ — without it, you get raw return, not risk-adjusted.
---
| Policy | Numerator (benefit) | Denominator (risk/volatility) | High SR ⇒ |
|---|---|---|---|
| **Expansionary fiscal** (↑G, ↓T) | Expected ↑GDP / aggregate demand | ↑Govt debt or inflation volatility | Benefits outweigh debt/inflation risks |
| **Accommodative monetary** (↓ rates) | ↑Output, ↑employment | Asset-price bubble risk, currency depreciation volatility | Growth gains outweigh bubble/FX risks |
| **Structural reforms** (deregulation, labour reform, infra) | Long-term growth gains | Short-term adjustment costs / uncertainty | Long-term gains justify short-term cost |

**Quick Recall:**
- SR can extend to macro: numerator = expected benefit, denominator = volatility/risk of side-effects.
- Three macro examples: fiscal stimulus, monetary easing, structural reforms.

### 19.4 Application of CAPM 🔴

**1. Expected Return Estimation**

**2. Cost of Equity Calculation**

**3. Risk-Adjusted Performance Measurement (Alpha)**
- **Alpha (α)**: excess return of a portfolio over its CAPM-predicted expected return; measures manager's skill / outperformance. ⭐ (exam-important)
- **Cost of equity**: return required by shareholders, computed via CAPM with the firm's β.

### ⚠️ Common Mistakes
- ❌ Treating α > 0 as proof of skill in a single period → ✅ It can be luck; need many periods + statistical significance.
- ❌ Using historical β only — β can shift over time as a firm's leverage / business changes.

**Quick Recall:**
- Three CAPM uses: expected return, cost of equity, α (performance).
- Worked numbers: 9%, 13%, +2% α — useful templates.
- **Builds on**: CAPM equation (this chunk).
- **Pairs with**: Sharpe ratio (this chunk) — both are CAPM-derived performance tools, but Sharpe uses σ_p while CAPM/α uses β.

### 19.5 Limitations of CAPM (general) 🔴
1. **Restrictive assumptions** — perfect competition, frictionless markets, constant correlations, rational investors. Deviations distort predictions.
2. **Market index choice** — CAPM uses the market index as a proxy for the market portfolio; different indices → different β estimates and expected returns.
3. **Single-factor model** — only systematic risk (β) priced; ignores firm-specific risk, macro variables, sentiment.
4. **Linearity and homogeneity** — assumes all investors have identical risk preferences and a linear risk-return relation; reality is nonlinear and heterogeneous.
5. **Risk-free rate** — fluctuates over time; may not match investors' actual borrow/lend opportunities; changes shift the entire SML.
6. **Empirical validity** — mixed evidence; predictive power often weak, especially in turbulent or crisis periods.
7. **Non-market risks** — overlooks idiosyncratic risks (company events, regulation) that move prices.

### ⚠️ Common Mistakes
- ❌ Listing only "no transaction costs" → ✅ The exam expects the seven-point list above.

**Quick Recall:**
- 7 limits: assumptions, index, single-factor, linearity/homogeneity, risk-free rate, empirical validity, non-market risks.
---

### 19.5.1 Theoretical Limitations of CAPM 🔴

**1. Perfect market assumptions**
- **Example:** *2007–08 Global Financial Crisis* — info asymmetries, liquidity shortages, regulatory interventions distorted prices and broke CAPM predictions.

**2. Homogeneous investor behaviour**
- **Example:** *During market volatility*, some investors turn risk-averse (demand higher returns), others take on more risk for higher returns — heterogeneous reactions break the single risk-return curve.

**3. Single-factor model**
- **Example:** Periods of high uncertainty (geopolitical, macro) cause asset returns to depend on factors *beyond* β — CAPM under-predicts.

**Quick Recall:**
- 3 theoretical limits: perfect market, homogeneous investors, single-factor.

### 19.5.2 Practical Limitations of CAPM 🔴

**1. Non-linear risk-return relationship**
- **Example:** *Tech start-ups* — high risk, high *potential* return. Many fail outright; survivors deliver outsize returns. Real distribution is skewed and nonlinear, not the smooth line CAPM assumes.

**2. Sensitivity to inputs and assumptions**
- **Example:** *Estimating market risk premium* — not directly observable. Different analysts use different historical windows or methods → divergent estimates → small variations cause large swings in expected returns.
- Implication: small input changes → unreliable forecasts in dynamic / uncertain environments.

**3. Poor predictor of returns**

**Quick Recall:**
- 3 practical limits: nonlinearity, input sensitivity, weak prediction.

### ⚠️ Common Mistakes
- ❌ Mixing up theoretical and practical limitations in answers → ✅ Theoretical = assumptions about markets/investors; Practical = problems applying the math.
---

### 19.6 Empirical Analysis of CAPM 🔴
| Method | What is done | Example |
|---|---|---|
| **Time-series analysis** | Collect historical returns of asset & market over a period; regress to estimate β; compare CAPM-predicted vs actual returns over time | 10-year study of stocks' β vs subsequent returns |
| **Cross-sectional analysis** | Across many assets at one point in time, test whether higher β → higher expected return | Sample stocks across industries; compare CAPM vs actual returns |
| **Event studies** | Examine how prices react to specific events (earnings, mergers); compare event-window returns to CAPM predictions | Quarterly earnings announcement reactions |
| **Portfolio performance evaluation** | Compute portfolio β, compare CAPM expected return to actual portfolio return → over- or under-performance | Investor evaluating their diversified portfolio over 1 year |

**Quick Recall:**
- 4 empirical methods: time-series, cross-sectional, event study, portfolio performance.
- Outperformance test: actual > CAPM expected return ⇒ positive alpha.
| Term | Definition |
|---|---|
| Anomalies | Return patterns CAPM cannot explain (e.g., size effect, value effect). |
| Asset pricing | Valuing assets based on risk-return characteristics. |
| Beta | Asset's sensitivity to market movements. |
| Diversification | Spreading investments across assets to reduce risk. |
| Efficient frontier | Set of optimal portfolios — highest expected return for each risk level. |
| Empirical analysis | Examination of real data to test theories like CAPM. |
| Expected return | Return investor anticipates given risk characteristics. |
| Market efficiency | Degree to which prices reflect all available info. |
| Market portfolio | All-asset value-weighted portfolio. |
| Market risk premium | $E(R_m) - R_f$ — excess return for holding a risky asset over risk-free. |
| Portfolio theory | Study of constructing portfolios to optimise returns / minimise risk. |
| Return | Gain/loss generated on an investment over a period. |
| Risk | Variability of returns. |
| Risk-free rate | Return on risk-free investment (proxy: gov't bonds). |
| Systematic risk | Market-related risk, non-diversifiable. |

### 20.2 Ross's Critique of CAPM 🔴
1. **Single-factor model** — only β / market risk; ignores other systematic forces.
2. **Homogeneous expectations** — assumes all investors agree on returns, SDs, correlations.
3. **Static risk** — assumes asset risk is constant over time; reality changes with economy, tech, sentiment.
4. **Risk-free rate assumption** — uses a constant baseline; gov't-bond proxy assumes no default risk, may not hold.
1. **Perfect markets** — no transaction costs, no taxes, no short-sale restrictions.
2. **Homogeneous assets** — all assets fully described by expected return + β.
3. **Normal distribution of returns** — ignores fat tails, volatility clustering.
4. **Constant correlations** — correlations actually change in crises / turbulence.
5. **Investor rationality** — ignores behavioural-finance evidence of biases.

**Quick Recall:**
- 4 drawbacks: single-factor, homogeneous expectations, static risk, risk-free rate.
- 5 assumptions: perfect markets, homogeneous assets, normal distribution, constant correlations, rationality.

### ⚠️ Common Mistakes
- ❌ Confusing drawbacks with assumptions in the answer → ✅ Drawbacks = model design flaws; assumptions = simplifications about markets/investors.
---

### 20.3 Introduction to APT 🔴

**APT Equation**
- $E(R_i)$ = expected return on asset *i*
- $R_f$ = risk-free rate
- $\beta_{ij}$ = sensitivity of asset *i* to factor *j*
- $\lambda_j$ = risk premium associated with factor *j*
- $\epsilon_i$ = idiosyncratic / specific return component for asset *i*

**Arbitrage discipline**
- **No-arbitrage assumption**: investors cannot consistently earn risk-free profits from price discrepancies. Any mispricing is corrected by arbitrageurs.
- **Law of One Price**: assets with similar risk exposures must have similar expected returns; otherwise arbitrage exists.

**Two key advantages**
- **Flexibility & dynamism** — multiple risk factors can be priced.
- **Empirical factor identification** — factors found from data, not theory.
- **Arbitrage Pricing Theory (APT)**: a multi-factor asset pricing model in which expected return is a linear function of multiple macroeconomic factor sensitivities and their risk premia, derived from a no-arbitrage condition. ⭐ (exam-important)
- **Law of One Price**: assets with the same risk exposures should have the same expected return — otherwise arbitrage exists. ⭐ (exam-important)
- **Factor sensitivity (β_ij)**: how much asset *i*'s return moves with factor *j*. ⭐ (exam-important)
- **Risk premium (λ_j)**: extra expected return for bearing one unit of factor *j* risk.
- **Idiosyncratic return (ε_i)**: asset-specific component, diversifiable.

### 20.3.1 Assumptions of APT 🔴
1. **Separation of systematic & unsystematic risk** — systematic captured by factor βs; unsystematic is diversifiable and can be eliminated through portfolio construction.
2. **Efficient markets** — prices reflect all available info; mispricing is quickly corrected by arbitrage.
3. **Rational expectations** — investors form expectations using all available info.
4. **Absence of arbitrage opportunities** — no risk-free profits from mispricing; central to model.
5. **Investor rationality** — investors maximise expected utility given their info and preferences.

**Quick Recall:**
- APT assumptions cluster around: risk separation, market efficiency, rational expectations, no arbitrage, investor rationality.

### 20.3.3 Key Differences between APT and CAPM 🔴
| Aspect | CAPM | APT |
|---|---|---|
| **Number of factors** | Single (market risk) | Multiple (macro factors: rates, inflation, GDP, industry) |
| **Factor identification** | Predefined (market portfolio, e.g., S&P 500 proxy) | Empirically identified from data; not predefined |
| **Sensitivity measure** | β = cov(R_i, R_m) / var(R_m) | Factor sensitivities β_ij — one per factor *j* |
| **Investor behaviour** | Rational, risk-averse, balance risk-return | No explicit assumption; focuses on factor-return relations |
| **Equation** | $E(R) = R_f + \beta(R_m - R_f)$ | $E(R) = R_f + \sum_j \beta_{ij} \lambda_j + \epsilon_i$ |

**Quick Recall:**
- 4 differences: # of factors, factor identification, sensitivity measure, investor-behaviour assumption.

### ⚠️ Common Mistakes
- ❌ "APT replaces β with multiple βs but is otherwise identical to CAPM" → ✅ APT also drops the homogeneous-expectations and predefined-factor structure; it is more flexible across the board.
---

**Quick Recall:**
- APT applications: asset allocation, cost of capital, manager evaluation.
- APT empirical issues: data, misspecification, time-varying β, factor redundancy, efficiency.

### 20.5 Criticisms of APT 🔴
1. **Arbitrage opportunities** — frictions, transaction costs, constraints prevent quick correction in reality.
2. **Market efficiency** — real markets imperfect; APT validity weakens.
3. **Factor independence** — APT assumes factors are independent; real factors often correlated.
4. **Static betas** — like CAPM, APT typically assumes constant β; really they vary with conditions.
5. **Investor rationality** — behavioural finance shows biases; rationality assumption questionable.
| Comparison | Critic's view |
|---|---|
| **APT vs CAPM** | APT solves CAPM's single-factor flaw but introduces own assumption set; choice depends on data/use. |
| **APT vs Fama-French (3-factor)** | Fama-French extends APT with explicit market, size (SMB), value (HML) factors; often *better explanatory power* in empirical tests for size/value effects. |
1. **Dynamic factor sensitivities** — allow time-varying βs.
2. **Behavioural integration** — embed sentiment, biases.
3. **Better factor identification** — refine selection of macro variables; ensure independence and non-redundancy.
4. **Nonlinear relationships** — relax linear-factor assumption.
- **Fama-French Three-Factor Model**: APT extension with market, size (SMB = small-minus-big), and value (HML = high-minus-low book-to-market) factors. ⭐ (exam-important)

**Quick Recall:**
- 5 APT criticisms: arbitrage limits, market inefficiency, factor dependence, static betas, irrational investors.
- Fama-French = market + SMB + HML.
- 4 improvement directions: dynamic β, behavioural, better factors, nonlinearity.
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

### 21.2 Derivatives — Basic Concepts 🔴

**What is "underlying"?**
| Type | Underlying examples |
|---|---|
| **Commodity derivatives** | Coffee, wheat, precious stones |
| **Financial derivatives** | Debt instruments, currency, equity shares |

**Trading venues**
- **Exchange-traded** — standardised; lower transaction costs; lower default risk.
- **Over-the-counter (OTC)** — customised; flexible terms; higher credit / default risk; lower liquidity.
- **Derivative**: a contract whose value is derived from an underlying asset; contract types include forwards, futures, options, swaps, hybrids, with predetermined durations. ⭐ (exam-important)
- **Notional turnover**: sum, over contracts traded today, of (strike price × number of underlying-asset units in each contract).
- **Farmer–merchant**: farmer worried about wheat price drop signs a derivative to lock a future price (exercise price). Value moves with market wheat price.
- **Soybean farmer**: 150 quintals expected in 3 months → can do OTC contract with food merchant or buy a standardised exchange wheat futures, leaving some uncovered for upside.

**Five economic functions of derivative markets**
1. **Risk transfer** — from risk-averse to risk-oriented players.
2. **Price discovery** — for current and future prices.
3. **Stimulation of entrepreneurial activity**.
4. **Increased market trading volumes** — risk-averse players join because they can hedge.
5. **Promotion of savings & long-term investment**.

**Quick Recall:**
- 5 functions: risk transfer, price discovery, entrepreneurship, more volume, savings & investment.
- Exchange-traded vs OTC: standardisation/liquidity vs customisation/credit risk.

### 21.3.1 Forward Contracts 🔴
- **Long position** — buyer; commits to buy at agreed price on the future date.
- **Short position** — seller; commits to sell at agreed price on the future date.
- **Settlement**: physical or cash. Cash settlement → single payment based on market value at expiry; underlier and money don't physically move.
- **Forward curve** = graph of forward prices for various maturities.
- **Bid / offer forward prices** influenced by time value of money + market expectations.
- $n$ = notional amount (units of underlier)
- $s$ = spot price at settlement
- $k$ = delivery (forward) price agreed at contract date
- **Reliance shares**: A and B agree to buy/sell 100 Reliance shares at Rs 850 in 2 months. Terms (product, quantity, price, delivery) are predetermined.
- **Crude oil**: 500,000 barrels at US $42.08/barrel in 3 months → variables = underlier (oil), n (= 500,000), k (= $42.08), settlement date.
- **Default risk**: if Reliance market price rockets above 850, seller may default to sell on the open market; if it crashes below 850, buyer may default to buy cheaper.

### ⚠️ Common Mistakes
- ❌ "Forwards have no default risk because both sides commit" → ✅ Mutual commitment is exactly what creates the risk: when one side wins big, the other has incentive to walk away.

**Quick Recall:**
- Forward = customised, bilateral, bespoke, default-risky.
- Payoff = n(s − k). Long wins if s > k.
- Forward curve = forward price vs maturity.
---

### 21.3.2 Futures 🔴
| Aspect | Forward | Futures |
|---|---|---|
| Trading | OTC, bilateral | Exchange-traded |
| Customisation | Fully customisable | Standardised (qty, quality, delivery) |
| Liquidity | Poor | High |
| Default risk | Significant | Eliminated by clearinghouse |
| Margining | None | Daily mark-to-market |
| Settlement | Physical or cash, at expiry | Physical or cash, with daily settlement |
| Counterparty | Other side of the trade | Clearinghouse (two contracts, each with clearinghouse) |

**Types of futures**
- **Index futures** — based on an underlying index; **cash-settled**; value derived from index.
- **Stock futures** — single specific stocks; **cash-settled** for single-stock futures.
- **Futures contract**: a legally binding standardised exchange-traded agreement to buy or sell an underlying on a predetermined future date, with clearinghouse-guaranteed settlement and daily margining. ⭐ (exam-important)
- **Margining**: daily profit/loss calculation on a futures position to ensure ongoing settlement and eliminate credit risk.

**Quick Recall:**
- Forward → futures = standardisation + exchange + clearinghouse + margining.
- Index futures and single-stock futures are typically cash-settled.

### 21.3.3 Options 🔴

**Call vs Put**
| | Call | Put |
|---|---|---|
| Right of buyer | Right to **buy** at strike | Right to **sell** at strike |
| Buyer profits when | Spot > Strike | Spot < Strike |

**American vs European**
- **American** — exercisable any time on or before expiry.
- **European** — exercisable only on expiry date.

**Moneyness**
- **In the money (call)**: current price > strike.
- **Out of the money (call)**: current price < strike.
- (Mirror for put.)

**Covered vs Naked**
- **Covered option**: writer owns the underlying.
- **Naked option**: writer does not own the underlying — higher risk.

**Index options**
- **Strike / Exercise price**: agreed price at which the option can be exercised. ⭐ (exam-important)
- **Premium**: cost paid by option buyer to writer for the right. ⭐ (exam-important)
- **Call option**: right to buy at strike. ⭐ (exam-important)
- **Put option**: right to sell at strike. ⭐ (exam-important)
- **Writer**: option seller; obligated if buyer exercises.
- **European put on Brent oil**: 100,000 barrels, strike US $45, 3-month expiry. Holder can sell 100,000 bbl @ $45 in 3 months *if* it suits them.
- **TV reservation analogy**: Mr A pays Rs 200–300 to reserve a TV for 2 days with right to buy. He's an option buyer; the Rs 200–300 is the premium; if he finds a better deal, he lets the option expire.

**Quick Recall:**
- Option = right (no obligation) for buyer; obligation for writer.
- Call = right to buy. Put = right to sell.
- American = anytime; European = expiry only.
- Index options = European, cash-settled.

### 21.3.4 Swaps 🔴

**Plain Vanilla Interest Rate Swap**
- One party pays **fixed-rate** interest on a notional principal; receives **floating-rate** (often **LIBOR**-linked).
- **Notional principal** = reference amount only — never actually exchanged.
- Maturities: typically **2–10 years**, can range from < 1 year to > 15 years.

**Currency Swap**
- Exchange foreign currencies in spot market with simultaneous **forward-market reversal** at predetermined rate and timing.
- Both **principal and interest** are swapped (unlike IR swap).
- At maturity, principal amounts are swapped back.

**Other swap forms (named)**
- **Interest rate swap**: exchange of one stream of interest obligations for another (typically fixed for floating) on a notional principal. ⭐ (exam-important)
- **Currency swap**: exchange of principal and interest in one currency for principal and interest in another, with reversed exchange at maturity. ⭐ (exam-important)
- **Notional principal**: reference amount used to compute interest in a swap; not physically exchanged.

**Quick Recall:**
- Most common swap: plain vanilla IR (fixed↔floating, often LIBOR).
- Currency swap involves both interest *and* principal exchange.
- Notional principal = reference only.
| Trader | Aim | Tool |
|---|---|---|
| **Hedger** | Mitigate risk from future price moves | Forwards, futures, options |
| **Speculator** | Profit from anticipated price moves | All derivatives |
| **Arbitrageur** | Lock in risk-free profit from price discrepancies between markets | Offsetting positions in 2+ instruments |

**Quick Recall:**
- Hedger reduces risk; speculator takes risk; arbitrageur takes no net risk.

### 21.3.5 Put-Call Parity 🔴

**Two equivalent portfolios at expiration (T)**
- **Portfolio 1**: long put + long share — value = max(K, S_T)
- **Portfolio 2**: long call + K bonds (each paying 1 at T) — value = max(S_T, K)

**Put-Call Parity Equation**
- $C(t)$ = time-t price of European call
- $P(t)$ = time-t price of European put
- $S(t)$ = time-t price of share
- $K$ = strike price
- $B(t, T)$ = time-t price of a zero-coupon bond paying 1 at T (i.e., $K \cdot B(t,T)$ is the PV of strike)
1. **Equivalence of calls and puts** — in any **delta-neutral portfolio**, calls and puts can substitute. If $d$ is the call's delta, then *long call + short d shares* ≡ *long put + long (1−d) shares*.
2. **Parity of implied volatility** — without dividends/carry costs, calls and puts must show the same implied volatility — keeps market expectations consistent.

### ⚠️ Common Mistakes
- ❌ Applying parity directly to American options → ✅ Strict parity holds for European options; American options have an inequality version due to early-exercise possibility.

**Quick Recall:**
- Parity: $C + K \cdot B(t,T) = P + S$.
- Same strike, same expiry, European, no dividends.
- Violation ⇒ arbitrage.
- **Builds on**: §21.3.3 Options (this chunk).
- **Pairs with**: Black-Scholes & Binomial pricing models (chunk 007 — §21.4).

### 21.4.1 Binomial Option Pricing Model 🔴

**Strengths**
- **Versatile** — handles American (anytime exercise), Bermudan (set of exercise dates), dividend-paying options.
- **Simple & implementable** in spreadsheets/software.
- **Accurate** for long-dated options or those with dividends.

**Limitations**
- Slower than Black-Scholes for European options.
- Struggles with multi-uncertainty options (real options) or complex features (Asian options) — **Monte Carlo** is preferred there, though computationally heavy.
1. **Price tree generation** — build a binomial tree of underlying-asset prices over N time steps.
2. **Calculate option value at final nodes** — intrinsic (exercise) value at expiry: max(S_T − K, 0) for call; max(K − S_T, 0) for put.
3. **Progressive (backward) calculation at earlier nodes** — at each prior node use risk-neutral pricing:
   - Today's fair value = discounted expected future value, with risk-neutral probabilities.

**Binomial Value formula at each node**
- $p$ = risk-neutral probability of an up move
- $1-p$ = probability of a down move
- $r$ = risk-free rate
- $t$ = time step length

**American option rule at each node**
- **Binomial Option Pricing Model**: discrete-time lattice model that values options by recursive risk-neutral discounting through a tree of possible underlying prices. ⭐ (exam-important)
- **Risk-neutral probability (p)**: probability that, when used to discount expected future payoffs at $r$, gives today's fair price.

**Quick Recall:**
- 1979, Cox-Ross-Rubinstein.
- 3 steps: tree, terminal payoff, backward induction.
- American: max(BinValue, ExerciseValue) at each node.

### ⚠️ Common Mistakes
- ❌ Using real-world probabilities to discount → ✅ Use risk-neutral probability $p$ (so discount rate = $r$).
---

### 21.4.2 Black-Scholes Option Pricing Model 🔴

**Six Black-Scholes assumptions (memorise)**
1. Underlying generates **no dividends** during option life.
2. **Zero transaction costs**.
3. **Risk-free rate is known and constant** during option life.
4. **European exercise** only — at expiry, not before.
5. **Short selling allowed** — short seller gets full cash proceeds today.
6. **Stock price moves randomly** (geometric Brownian motion).

**Black-Scholes Formula**
- $V_{CO}, V_{PO}$ = value of call, put
- $P$ = current price of underlying
- $Y$ = exercise / strike price
- $r$ = risk-free rate (continuously compounded)
- $t$ = time to expiry (in years, fractional ok)
- $\sigma^2$ = annualised variance of return on underlying; $\sigma$ = annualised SD
- $N(d_1), N(d_2)$ = cumulative areas under standard normal distribution
- $\ln(P/Y)$ = natural log of (P/Y)
- $e \approx 2.7183$
- **Black-Scholes Model**: a closed-form pricing formula for European call and put options under geometric Brownian motion of the underlying. ⭐ (exam-important)
- **N(d)**: cumulative probability under the standard normal distribution from −∞ to d. In Excel: `=NORM.DIST(d, 0, 1, TRUE)`.

**Example 21.1 — Worked TCS call**

**Example (Check Your Progress 3.2) — Worked**

### ⚠️ Common Mistakes
- ❌ Using simple compounding for $e^{-rt}$ → ✅ The model uses *continuously* compounded $r$.
- ❌ Forgetting $\sigma$ vs $\sigma^2$ — formula uses $\sigma$ in $d_1$, $d_2$ denominators, but $\sigma^2$ in the $d_1$ numerator's drift term.
- ❌ Applying Black-Scholes to American options → ✅ Black-Scholes prices European only; American options need binomial / lattice methods.
| Aspect | Status |
|---|---|
| **Speed** | ✅ Major advantage — fast for many options |
| **Closed form** | ✅ No iteration needed |
| **American options** | ❌ Cannot price — only at expiry, no early-exercise step |
| **Dividend-paying stocks** | ❌ Standard form excludes them |
| **Volatility** | Assumes σ known and constant |

**Quick Recall:**
- 1973, Black & Scholes (with Merton).
- $V_{CO} = P \cdot N(d_1) - Y e^{-rt} \cdot N(d_2)$.
- 6 assumptions: no dividends, no costs, constant r, European, short selling allowed, random stock moves.
- Worked Ex 21.1: VCO = ₹5.5099, VPO = ₹0.2598.

**Quick Recall:**
- Binomial (discrete) ↔ Black-Scholes (continuous), same GBM foundation.
- Black-Scholes is the limit of binomial as steps → ∞.
| Market | Nature | Examples |
|---|---|---|
| Exchange-traded | Standardised contracts on an exchange | NSE F&O, BSE F&O |
| OTC | Decentralised, bilateral | Customised forwards |
| Aspect | Cash market | Derivative market |
|---|---|---|
| Settlement | On the spot | At a future date |
| Participants | Spot traders | Futures traders |
| Mode | Physical commodity | Derivative contract |

**Quick Recall:**
- 2 markets: exchange-traded vs OTC.
- SEBI regulates.
- 2000 — first derivative on BSE; same year NSE launches index futures.
- NSE launched single-stock options (July 2001) before single-stock futures (November 2001).
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
- **Corporate finance**: area of finance dealing with sources of funding, capital structure, manager actions to increase firm value to shareholders, and tools to allocate financial resources. ⭐ (exam-important)
- **Capital budgeting**: setting criteria for which value-adding projects receive investment funding. ⭐ (exam-important)

### 22.2 Sources of Finance 🔴

**By time horizon**
| Type | Duration | Typical sources |
|---|---|---|
| **Short-term** | Up to 12 months | Short-term loans, bill discounting (commercial banks) |
| **Medium-term** | 1–5 years (intermediate) | Banks (medium-term loans), term lending institutions |
| **Long-term** | > 5 years | Shares, debentures, loans from special institutions (IFCI, ICICI) |

**By origin**
- **External**: equities/bonds (debentures) + loans.
- **Internal**: depreciation + retained earnings.

**1. Issue of Shares**

**(a) Preference Shares**
- Preferential rights: (i) guaranteed fixed dividend (amount or rate); (ii) priority in capital repayment in liquidation.
- Sub-classifications (3 axes — memorise):
  - **Cumulative vs Non-cumulative** — cumulative accumulates unpaid dividends until cleared; non-cumulative loses dividend right if no profit.
  - **Participating vs Non-participating** — participating shares share *surplus* profits after fixed-dividend payouts to equity shareholders; non-participating do not.
  - **Redeemable vs Irredeemable** — redeemable can be reclaimed during firm's life; irredeemable only at liquidation.

**(b) Equity Shares**
- No preferential rights; rank below preference shares for dividend & capital repayment.
- Variable dividend rate (depends on profits + directors' decision).
- Voting power at general meetings.
- Higher risk; higher potential return.

**2. Issue of Debenture**
| Type | Defining feature |
|---|---|
| **Convertible** | Convertible into shares at a designated time / on company notification. Lower interest rates than stocks. |
| **Partially convertible** | Conversion into shares only up to a certain % / limit; rest stays as debenture. |
| **Non-convertible** | No conversion option ever. |
| **Registered** | Tamper-proof transfer with documented records. Safer; lower fraud risk. |
| **Bearer** | Unregistered; transferable on delivery; no documentation. Vulnerable to fraud / tax evasion. |
| **Secured** | Collateral required; priority in repayment if firm winds up. |
| **Unsecured** | No collateral; lower priority in repayment. |
| **Redeemable** | Repaid at end of predetermined period. |
| **Irredeemable (perpetual)** | No fixed redemption period. |

**(a) Depreciation**

**(b) Retained Earnings**

**(c) Loan Financing (counted in this list, although external by origin)**
- **Share**: instrument representing ownership and voting rights in a company. ⭐ (exam-important)
- **Preference share**: share with preferential dividend & capital-repayment rights, typically with fixed dividend. ⭐ (exam-important)
- **Equity share**: ordinary share with variable dividend, voting rights, no preferential treatment. ⭐ (exam-important)
- **Debenture**: company-issued debt instrument acknowledging an obligation, with or without a charge on assets. ⭐ (exam-important)
- **Retained earnings (ploughing back of profits)**: undistributed profit kept inside the firm. ⭐ (exam-important)
- **Depreciation as finance source**: non-cash expense that creates an internal cash reserve via tax shield and asset-replacement provisioning.

**Quick Recall:**
- Time: short (≤ 1y), medium (1–5y), long (> 5y).
- Origin: external (shares + debentures + loans), internal (depreciation + retained earnings).
- Preference shares: 3 axis classification (cumulative/non, participating/non, redeemable/irredeemable).
- 9 debenture types: convertible, partly convertible, non-convertible, registered, bearer, secured, unsecured, redeemable, irredeemable.
- IFCI = Industrial Finance Corporation of India; ICICI = Industrial Credit and Investment Corporation of India.

### 22.3 Capital Structure 🔴
| Component | Sub-items |
|---|---|
| **Owner's capital (equity)** | Equity shares + Preference shares + Retained earnings |
| **Borrowed capital (debt)** | Debentures + Term loans + Lease financing + Short-term borrowings |
- **Capital structure**: composition and proportion of various sources of funds (equity + debt) a company uses to finance itself. ⭐ (exam-important)
- **Owner's capital / Shareholder's equity**: residual interest in the company's assets after liabilities are settled. ⭐ (exam-important)
- **Borrowed capital / Debt capital**: funds raised by borrowing from external sources, creating a legal obligation to repay with interest. ⭐ (exam-important)
1. **Business risk** — volatile/cyclical industries → lower debt to reduce financial risk.
2. **Tax considerations** — interest is tax-deductible; high-tax-bracket firms prefer debt.
3. **Cost of capital** — find optimal mix that minimises WACC.
4. **Market conditions** — stable economy → debt at favourable rates; downturn → shift toward equity.
5. **Company size and life cycle** — smaller/younger firms rely more on equity; larger/established firms have more debt access.
6. **Flexibility and control** — equity dilutes ownership; debt preserves it; debt also more flexible to adjust.
7. **Asset structure** — capital-intensive industries (e.g., manufacturing) use more debt; service industries use less.
8. **Lender and investor preferences** — risk/return appetites of capital-market players.
9. **Regulatory environment** — debt-equity ratio limits, financial regulations.

**Quick Recall:**
- Components: Owner's capital (equity + preference + retained) + Borrowed capital (debentures + loans + lease + short-term).
- 10 factors influencing capital structure (mnemonic: Business, Tax, Cost, Market, Size, Flex, Assets, Lenders, Regulator, Perception).

### 22.4 Working Capital Management — Forms 🔴

**Two forms of working capital**

**(I) Gross Working Capital**
1. **Cash and cash equivalents** — currency, bank balances, highly liquid assets.
2. **Accounts receivable** — money owed by customers for credit sales.
3. **Inventory** — stock of goods for sale, production, consumption.
4. **Short-term investments** — liquid financial instruments maturing < 1 year.

**(II) Net Working Capital**
- **Working capital**: current assets minus current liabilities; the capital available for day-to-day operations. ⭐ (exam-important)
- **Gross working capital**: total current assets. ⭐ (exam-important)
- **Net working capital**: current assets minus current liabilities. ⭐ (exam-important)
| Metric | High value implies | Low value implies |
|---|---|---|
| **Gross WC** | Large short-term resource base; **but** excessive carrying costs / inefficiency | Inadequate liquidity to fund short-term obligations |
| **Net WC** | Healthy liquidity; good financial mgmt | Liquidity stress — *but not always bad* (e.g., retail with fast inventory turnover & immediate cash collection) |

**Quick Recall:**
- Gross WC = total current assets; Net WC = CA − CL.
- Negative net WC isn't always bad — depends on industry (retail OK with negative).

### 22.4.2 Factors Determining Working Capital 🔴
1. **Nature of business** — manufacturing needs more (raw, WIP, finished); services need less (faster cash conversion).
2. **Business cycle and seasonality** — peaks need more WC for inventory & receivables; troughs need less.
3. **Sales volume and growth rate** — high sales / rapid growth → more WC.
4. **Credit policy** — lenient credit → higher receivables → more WC; strict credit reduces WC but may hurt sales.
5. **Supplier payment terms** — longer payable terms conserve cash → less WC; but strain supplier relations.
6. **Inventory management** — efficient turnover → less WC.
7. **Seasonal inventory needs** — peak seasons require WC ramp-up.
8. **Operating efficiency** — streamlined processes → less WC needed.
9. **Economic conditions** — inflation, interest rates, credit availability; downturns may increase WC needs.

**Quick Recall:**
- 9 factors: nature, cycle, volume/growth, credit policy, supplier terms, inventory, seasonality, efficiency, economy.
- **Builds on**: §22.2 sources of finance (this chunk).
- **Pairs with**: §22.6 capital budgeting (chunk 009).

### 22.4.3 Methods of Working Capital Forecast 🔴
| Method | Formula | What it captures |
|---|---|---|
| **1. Estimating CA & CL** | WC = Estimated CA − Estimated CL | Simple project of current asset/liability levels |
| **2. Cash costs of CA & CL** | WC = Cash Costs of CA − Cash Costs of CL | Timing of cash flows; actual cash needs |
| **3. Percent of Sales** | WC = (% Receivables + % Inventory − % Payables) × Sales | Working capital as fraction of sales |
| **4. Operating Cycle** | WC = (DIO + DSO) − DPO (in days) | Time-based — converts cycle days to WC need |

**Example 22.1 — Method 1: Estimating CA & CL**
- CA: Cash 50,000 + AR 120,000 + Inventory 80,000 + Prepaid 10,000 = **₹260,000**
- CL: AP 90,000 + Short-term debt 30,000 + Accrued 15,000 + Taxes 5,000 = **₹140,000**
- **WC Forecast = 260,000 − 140,000 = ₹120,000**

**Example 22.2 — Method 2: Cash Costs**
- Cash costs of CA (outflows): Inventory 500,000 + Prepaid 20,000 = **₹520,000**
- Cash costs of CL (inflows from settling): AP payments 400,000 + Short-term debt payments 100,000 = **₹500,000**
- **WC Forecast = 520,000 − 500,000 = ₹20,000**

**Example 22.3 — Method 3: Percent of Sales**
- AR = 20% of sales, Inventory = 15% of sales, AP = 10% of sales.
- Forecasted sales = ₹2,000,000.
- WC = (0.20 + 0.15 − 0.10) × 2,000,000 = (400,000 + 300,000) − 200,000 = **₹500,000**

**Example 22.4 — Method 4: Operating Cycle**
- DIO (Days Inventory Outstanding) = 60
- DSO (Days Sales Outstanding) = 45
- DPO (Days Payables Outstanding) = 30
- **WC = (60 + 45) − 30 = 75 − 30 = 45 days**
- **DIO (Days Inventory Outstanding)**: average days inventory is held before sale.
- **DSO (Days Sales Outstanding)**: average days to collect receivables.
- **DPO (Days Payables Outstanding)**: average days taken to pay suppliers.
- **Operating cycle (days)**: DIO + DSO − DPO. ⭐ (exam-important)

**Quick Recall:**
- 4 methods: CA/CL estimation, cash costs, % of sales, operating cycle.
- Operating cycle: WC days = DIO + DSO − DPO.
- % of sales: net WC ratio = (AR% + Inv%) − AP%.

### 22.4.4 Sources of Working Capital 🔴

**Short-term sources (6)**
| Source | Detail |
|---|---|
| **Trade credit** | Supplier credit, typically 30–90 days |
| **Bank loans** | WC loans, overdraft facilities |
| **Commercial paper** | Short-term unsecured promissory notes (creditworthy corps only) |
| **Factoring & receivables financing** | Sell AR to a factor at a discount → immediate cash |
| **Inventory financing** | Inventory used as collateral |
| **Trade advances** | Customer advance payments |

**Long-term sources (6)**
|---|---|
| **Equity financing** | Issue new shares (private placement / IPO) |
| **Debt financing** | Long-term bonds, long-tenor bank loans |
| **Retained earnings** | Reinvest accumulated profits |
| **Venture capital / private equity** | Ownership-stake funding for high-growth firms |
| **Asset-based lending** | Long-term loans against real estate / equipment collateral |
| **Debentures** | Long-term unsecured debt instruments |

**Quick Recall:**
- 6 + 6 sources: short-term (trade credit, bank, CP, factoring, inventory financing, advances) and long-term (equity, debt, retained earnings, VC/PE, asset-based, debentures).

### 22.4.5 Approaches for Determining the Financial Mix 🔴
1. **Hedging approach** — minimise WACC by balancing debt and equity.
2. **Conservative approach** — emphasise stability via more equity.
3. **Trade-off approach** (named in unit; characterised between hedging and conservative — balance between them).

**A. Hedging Approach**
- Find the **optimal capital structure** by **minimising WACC** (weighted average cost of debt + equity).
- Increase debt as long as **cost of debt < cost of equity** → WACC ↓ → firm value ↑.
- **Limit**: too much leverage raises financial risk → optimal point = WACC minimum without jeopardising solvency.

**B. Conservative Approach**
- Stability and security first.
- Rely more on **equity**, lower debt.
- **Trade-off**: higher cost of capital — equity is generally more expensive (issuance costs, dilution).
- **WACC (Weighted Average Cost of Capital)**: average cost of debt and equity, weighted by their proportion in the capital structure. Used to decide optimal financing mix. ⭐ (exam-important)
- **Hedging approach to financial mix**: select capital structure that minimises WACC. ⭐ (exam-important)
- **Conservative approach to financial mix**: maintain higher equity, lower debt — for stability.

**Quick Recall:**
- Hedging = minimise WACC (more debt while it's cheap).
- Conservative = more equity, more stable, more expensive.

### 22.5 Dividend Policy 🔴

**Nature of dividend decision**
- **Reciprocal relationship**: more dividend ↔ less retained earnings.
- Decision criterion: **maximisation of shareholders' wealth** — pay if dividends help; retain if reinvestment would help more.
- Effectively a **financing decision**: pay dividends if the firm can't beat the cost of retained earnings; retain if it can.

**Two conflicting schools**

**1. Irrelevance of Dividend (Soloman, Modigliani, Miller)**
- Dividend policy does **not** affect share price → no impact on firm value.
- Investors don't differentiate dividends from capital gains; they want **higher return on investment**.
- If the firm can earn > cost of retained earnings → investors prefer retention.
- If expected project return < cost → investors prefer dividends.
- ⇒ Dividend decision is really a **financing decision** about whether to use retained earnings.

**2. Modigliani–Miller (MM) Approach**
- Share price determined by **earnings potential + investment policy**, NOT by income-distribution pattern.
- Quote: *"Under conditions of perfect capital markets, rational investors, absence of tax discrimination between dividend income and capital appreciation, given the firm's investment policy, its dividend policy may not influence the market price of the shares."*
- **Logic**: any wealth gain from higher dividend is exactly offset by raising fresh capital → more shares → lower EPS → lower share value. Net effect: zero.
- **Dividend**: distribution to shareholders out of profits or reserves available for this purpose (ICAI). ⭐ (exam-important)
- **Dividend irrelevance theory**: dividend policy does not affect share price; investors don't distinguish dividends from capital gains. Associated with Solomon and Modigliani-Miller. ⭐ (exam-important)
- **Modigliani-Miller dividend irrelevance**: under perfect capital markets, rational investors, no tax discrimination, share price is independent of dividend policy given investment policy. ⭐ (exam-important)
1. Perfect capital markets.
2. Rational investors.
3. No tax discrimination between dividends and capital gains.
4. Investment policy is given (independent of dividend choice).

**Quick Recall:**
- 2 schools: Dividend Irrelevance (Soloman, MM) vs Dividend-affects-value (relevance schools, see chunk 010).
- MM logic: dividend gain offset by dilution from fresh capital raise.

### ⚠️ Common Mistakes
- ❌ "MM says dividend doesn't matter at all" → ✅ MM says it doesn't affect share price *under their assumptions* (perfect markets, no tax discrimination, given investment policy). Drop assumptions and dividends become relevant.
---

### 22.6 Capital Budgeting 🔴

**Six types of capital budgeting cases (real-world cases — useful for essay answers)**
1. **New product development** — launch new product line; estimate initial investment, marketing, multi-year cash flows; apply NPV / IRR / Payback.
2. **Expansion of manufacturing facilities** — open new stores/plants; assess regional returns and risks.
3. **Replacement of machinery** — replace ageing equipment; compare new-machine cost vs cost savings + cash-flow gains.
4. **Mergers and acquisitions** — assess synergies, expected cash flows, shareholder-value impact.
5. **R&D projects** — pharma drug-development; long lead time, scenario analysis, success probability.
6. **Capital improvement projects** — government infrastructure (bridges, roads, water plants); life of asset, maintenance, community benefit.
- **Capital budgeting**: long-term planning of proposed capital expenditures and their funding. ⭐ (exam-important)
1. **Long-term investment choices** — substantial resources, lasting impact on growth and profitability.
2. **Optimal resource allocation** — limited resources → highest-return projects.
3. **Maximising shareholder wealth** — choose projects with positive NPV / high IRR.
4. **Strategic alignment** — projects fit long-term organisational vision.
5. **Risk assessment** — evaluate uncertainties; design risk-mitigation.
6. **Capital rationing** — when capital is limited, prioritise the best projects.
7. **Efficient use of funds** — avoid negative-NPV / low-return investments.

**Quick Recall:**
- 7 importance points (mnemonic: Long-term, Allocation, Wealth, Strategy, Risk, Rationing, Efficiency).

### 22.6.2 Kinds of Capital Investment Proposals 🔴
| Type | Description | Example |
|---|---|---|
| **Independent** | Non-competing; accepting one doesn't prevent another. Accept all that exceed required return. | New warehouse + new logistics software (unrelated) |
| **Contingent (dependent)** | Acceptance depends on approval of another proposal. Present together. | Buying a new machine contingent on plant expansion |
| **Mutually exclusive** | Competing; accepting one excludes the others. Choose best one via decision technique. | Choosing between two temperature-control systems |
- **Independent proposals**: non-competing investment proposals; each judged on its own return-vs-required-return. ⭐ (exam-important)
- **Contingent proposals**: dependent on approval of another proposal — must be considered jointly. ⭐ (exam-important)
- **Mutually exclusive proposals**: accepting one excludes the others; need a decision-making technique. ⭐ (exam-important)

**Quick Recall:**
- 3 types: Independent, Contingent, Mutually Exclusive.
- Independent ⇒ accept-all-good. Mutually exclusive ⇒ pick-best-one. Contingent ⇒ bundle decision.

### 22.6.3 Factors Affecting Capital Investment Decision (continued) 🔴
6. **Payback period** — time to recoup initial investment; shorter = more favourable.
   - *Example:* smartphone project payback = 0.5 year → recovered in 6 months.
7. **Net Present Value (NPV)** — present value of future cash flows minus initial investment. **Positive NPV** = project generates more than initial outlay.
   - *Example:* smartphone project NPV ≈ ₹3,18,72,197 → financially attractive.
8. **Internal Rate of Return (IRR)** — discount rate that sets NPV = 0; the project's effective rate of return.
   - *Example:* smartphone project IRR ≈ 18%.
- **Payback period**: time required to recover the initial investment from project cash flows. ⭐ (exam-important)
- **Net Present Value (NPV)**: present value of future cash flows minus initial investment. Positive NPV ⇒ project adds value. ⭐ (exam-important)
- **Internal Rate of Return (IRR)**: discount rate at which NPV = 0; the project's effective rate of return. ⭐ (exam-important)

**Quick Recall:**
- 8 factors total: Market demand, Competition, Cost of capital, Initial cost, Cash flows, Payback, NPV, IRR.
- NPV > 0 ⇒ accept; IRR > required return ⇒ accept; shorter payback ⇒ better.

### 22.6.4 Computation of Capital Investment 🔴

**Step 1: Identify project components**
1. **Fixed assets** — machinery, equipment, land, buildings, vehicles, infrastructure.
2. **Working capital** — inventory, raw materials, operating expenses (day-to-day).
3. **Initial setup costs** — planning, feasibility studies, legal fees, permits, licences.
4. **R&D** — for projects involving product development / innovation.
5. **Marketing and promotion** — for market entry / product promotion.

**Step 2: Determine costs**

**Step 3: Sum the costs**

**Step 4: Add contingency**

**Step 5: Final capital investment required**
| Component | Amount (₹) |
|---|---|
| Machinery | 5,00,000 |
| Equipment | 3,00,000 |
| Land | 10,00,000 |
| Building | 20,00,000 |
| Working capital | 8,00,000 |
| Initial setup | 2,00,000 |
| R&D | 1,50,000 |
| Marketing | 1,00,000 |
| **Subtotal** | **₹50,50,000** |

**Quick Recall:**
- 5 steps: identify, cost, sum, contingency, final.
- Standard contingency = 10%.
- Worked example total = ₹55,55,000.

**Quick Recall:**
- 9 forecasting practices: analysis, history, inflation, economy, experts, sensitivity, CBS, contingency, cash flows.
| Term | Meaning |
|---|---|
| Managing money | Overseeing income and expenses to achieve financial goals. |
| Capital structure | Combination of debt and equity; long-term funds composition. |
| Capital budgeting | Process of investment decisions in long-term projects/capital assets. |
| Investment proposal | Document outlining details of a potential investment opportunity. |

**Quick Recall:**
- FDI = long-term, control. FPI = short-term, no control.
- 2021-22 FDI inflow ≈ $82.27 bn.

### 23.2 Concept of FDI 🔴

**IMF Definition (memorise)**

**India-specific definition**
- An **unlisted Indian company**, OR
- **≥ 10% of post-issue paid-up equity capital** (fully diluted basis) of a **listed** Indian company.
- **Foreign Direct Investment (FDI)**: cross-border investment establishing a lasting interest and ≥10% voting power / influence over an enterprise. ⭐ (exam-important)
- **10% threshold**: in India, FDI in a listed company requires ≥10% of post-issue paid-up equity capital on fully diluted basis. ⭐ (exam-important)

**Quick Recall:**
- 10% rule = lasting interest threshold.
- IMF definition emphasises "lasting interest and control".

### 23.3 Methods of FDI 🔴
| Method | Definition | Example |
|---|---|---|
| **Greenfield investment** | Setting up a new business / expanding operations in foreign country | **Samsung (2019)** — $500 million for new mobile-phone plant in Noida, UP |
| **Mergers & Acquisitions (M&A)** | FDI by acquiring/merging with existing foreign company | **Vodafone–Idea (2017)** — Vodafone (UK) merged Indian operations with Idea Cellular |
| **Joint Ventures** | Foreign company collaborates and invests with a domestic partner | **GE–Tata (2015)** — GE & Tata Group formed TCS (BPO) [as cited in unit] |
| **Subsidiary Companies** | Wholly-owned subsidiary in foreign country (or majority stake) | **Suzuki Motor Corporation** — majority stake in Maruti Suzuki India Ltd |

### ⚠️ Common Mistakes
- ❌ Confusing greenfield with brownfield → ✅ Greenfield = brand-new project; brownfield = expansion of existing facility (sometimes treated as separate method).
- ❌ Treating M&A and JV as the same → ✅ M&A = acquire/merge → control; JV = partnered investment with shared control.

**Quick Recall:**
- 4 methods: Greenfield, M&A, Joint Venture, Subsidiary.
- Memorable Indian examples: Samsung Noida (Greenfield), Vodafone-Idea (M&A), GE-Tata (JV), Maruti Suzuki (Subsidiary).
---

### 23.4 Types of FDI 🔴
| Type | Definition | Example |
|---|---|---|
| **Horizontal FDI** | Invest in foreign firm in *same industry / same business* | Foreign apparel company buys Indian apparel firm |
| **Vertical FDI** | Invest *within supply chain* — supplier or distributor (may differ in industry). Two sub-types: backward, forward integration | Foreign fast-food chain invests in Indian agri operations (backward); foreign pharma opens own pharmacies in India (forward) |
| **Conglomerate FDI** | Invest in foreign firm in a *completely different industry* | **General Electric (GE)** — invested in aviation, healthcare, renewable energy, financial services |
| **Platform FDI** | Set up operations in a foreign location to serve as base for regional/global activities (manufacturing, services, R&D hub) | **IBM, Microsoft, Accenture** — Indian operations as platform for global software dev / IT consulting |
- **Horizontal FDI**: investment in foreign firm in the *same industry* as the investor. ⭐ (exam-important)
- **Vertical FDI**: investment within the supply chain — backward (toward suppliers) or forward (toward distribution). ⭐ (exam-important)
- **Conglomerate FDI**: investment in a foreign firm in an *unrelated industry*. ⭐ (exam-important)
- **Platform FDI**: investment in a location used as a regional/global base / hub. ⭐ (exam-important)
- **Backward vertical integration**: invest in supplier-side activities (e.g., agri inputs).
- **Forward vertical integration**: invest in distribution/retail-side activities.

**Quick Recall:**
- 4 types: Horizontal (same industry), Vertical (supply chain), Conglomerate (different industry), Platform (regional hub).
- Vertical splits backward (suppliers) vs forward (distribution).
- Memorable examples: Apparel→apparel (H); Fast-food→agri (V back); Pharma→pharmacies (V fwd); GE→multi-sector (C); IBM/MS/Accenture India (P).

### ⚠️ Common Mistakes
- ❌ Confusing methods (Greenfield/M&A/JV/Subsidiary) with types (Horizontal/Vertical/Conglomerate/Platform). → ✅ **Methods** = HOW the investment is structured. **Types** = the *industry relationship* between investor and investee.
- **Builds on**: corporate finance + capital budgeting (Unit 22).
- **Continues into**: chunk 011 — Routes of FDI, advantages/limitations, FDI Policy 2020, FPI.

### 23.5 Routes of FDI 🔴

**Automatic Route**
- **No prior approval** of Government of India needed.
- Sectors: **agriculture, animal husbandry, plantation, mining, petroleum & natural gas, airports, construction, manufacturing, industrial parks, e-commerce, railway infrastructure, asset construction companies, credit information companies, pharmaceuticals**.

**Government Route**
- **Prior approval** required from GoI; processed by the respective Administrative Ministry/Department.
- Sectors: **mining (certain), defence, broadcasting, print/digital media, civil aviation, satellites, telecommunications, private security agencies**.
- Must follow **FEMA** regulations and **RBI** procedures.

**Prohibited Sectors (no FDI under any route)**
1. Lottery business (govt/private, online).
2. Gambling and betting (incl. casinos).
3. Chit funds.
4. **Hundis** (only Hundis manufactured by NRIs etc., per policy).
5. Nidhi companies.
6. Trading in **Transferable Development Rights (TDRs)**.
7. Real estate business or construction of farmhouses (except specific exceptions).
8. Manufacturing of cigars, cheroots, cigarillos, cigarettes, tobacco / tobacco substitutes.

**Closed to private sector entirely**
- **Atomic energy**.
- **Railway operations** (except specific permitted activities).
- **Automatic Route**: FDI route requiring no GoI approval; sector-specific. ⭐ (exam-important)
- **Government Route**: FDI route requiring prior GoI approval through the Administrative Ministry. ⭐ (exam-important)
- **FEMA**: Foreign Exchange Management Act — regulatory framework cited for govt-route FDI.
- **TDR**: Transferable Development Rights (real estate); FDI prohibited.

**Quick Recall:**
- 2 routes: Automatic (no approval) + Government (prior approval).
- 8 prohibited sectors: lottery, gambling, chit funds, Nidhi, TDRs, real estate, tobacco, atomic energy/railway (closed to private).

### 23.6 Advantages and Disadvantages of FDI 🔴
1. **Contribution to economic growth** — capital injection → production, consumption, activity rise.
2. **Jobs creation** — foreign companies hire local workers.
3. **Bringing technology** — advanced tech, expertise, management practices.
4. **Increase in exports** — local resources/labour producing for global markets.
5. **Infrastructure development** — host country develops transport, energy, telecom to attract FDI.
6. **Setting up of new industries** — diversifies host economy.
7. **Access to new markets** — local firms gain via foreign investors' global networks.
8. **Increased government revenue** — taxes from FDI activities.
1. **Loss of control** over domestic industries; reduced independent decision-making.
2. **Vulnerability to economic fluctuations** — foreign investor policies → instability.
3. **Profit repatriation** — foreign investors take profits home → less reinvestment in host.
4. **Environmental degradation** — profit may be prioritised over sustainability.
5. **IP rights challenges** — risk of knowledge / technology leakage.
6. **Resource competition** — drives up local costs; may price local businesses out.

**Quick Recall:**
- 8 advantages (mnemonic: Growth, Jobs, Tech, Exports, Infra, Industries, Markets, Tax revenue).
- 6 disadvantages (Control, Volatility, Repatriation, Environment, IP, Resource competition).

### 23.7 Highlights of FDI Policy 2020 🔴

**1. Eligible Investors**
- Non-resident entities allowed (with prohibitions in certain sectors).
- **NRIs in Nepal & Bhutan** (and citizens of those countries) — invest in Indian companies on **repatriation basis**.
- **OCBs (Overseas Corporate Bodies)** not under RBI scrutiny — can invest as non-resident entities under FDI Policy + Foreign Exchange Management (Non-Debt Instrument) Rules, 2019.
- Foreign-incorporated companies / trusts / partnerships **controlled by NRIs** — invest under special dispensation.
- **FPIs** and **FVCIs (Foreign Venture Capital Investors)** — permitted; can trade through recognised Indian Stock Exchanges via registered brokers.

**2. Eligible Investee Entities**
- **Indian companies** authorised to issue capital for FDI.
- **NRIs in partnership firms / proprietary concerns** — non-repatriation basis only; via inward remittances or specified accounts; **NOT** in agriculture, plantation, real estate, print media.
- **Trusts** cannot receive foreign investment, *except SEBI-regulated VCFs*.
- **LLPs** — automatic route allowed; downstream investment + conversion permitted.
- **Investment vehicles + startups** — under FEMA Rules, 2019.

**3. Entry Routes**

**4. Prohibited Sectors (per Policy 2020)**
- Lottery (govt/private/online).
- Gambling, betting (casinos).
- Chit funds, Nidhi companies.
- TDR trading.
- Real estate / farmhouse construction (with exceptions).
- Cigars, cheroots, tobacco manufacturing.
- Atomic energy, railway operations (except permitted activities).
- **No foreign tech collaboration** (licensing, franchise, trademark, brand, mgmt contracts) for lottery/gambling/betting.
| Sector | FDI Cap | Route |
|---|---|---|
| Agriculture & Animal Husbandry | 100% | Automatic |
| Plantation | 100% | Automatic |
| Mining | 100% | Automatic |
| Mining/mineral separation of Titanium | 100% | Government |
| Petroleum & Natural Gas | 100% | Automatic |
| Petroleum refining by PSU | 49% | Automatic |
| Defence Manufacturing | 100% | Automatic ≤ 49%; > 49% Government (if access to modern tech) |
| E-commerce | 100% | Automatic |
| Multi-Brand Retail Trading | 51% | Government |
| Insurance | 49% | Automatic |
| Banking — Private Sector | 74% | Automatic ≤ 49%; > 49% & up to 74% Government |
| Banking — Public Sector | 20% | Government |
| Food products manufactured/produced in India | 100% | Government |
- **DPIIT**: Department for Promotion of Industry and Internal Trade — regulator for FDI policy. ⭐ (exam-important)
- **Consolidated FDI Policy 2020**: DPIIT policy effective **15 October 2020** that lays out current FDI rules. ⭐ (exam-important)
- **OCB**: Overseas Corporate Body — entity owned by NRIs; investor category.
- **FVCI**: Foreign Venture Capital Investor.

**Quick Recall:**
- Regulator: DPIIT (formerly DIPP).
- Policy effective: 15 Oct 2020.
- 100% Automatic in: Agri, Plantation, Mining, P&NG, E-commerce.
- 49% Automatic: Insurance.
- 74% Banking-Private (49% Auto + 25% Govt).
- 20% Banking-Public, Govt route.

### ⚠️ Common Mistakes
- ❌ Confusing "100% via Automatic" with "fully unrestricted" → ✅ Even at 100% Automatic, FEMA reporting and post-investment compliance are still required.
---

### 23.8 Concept of FPI 🔴

**Indian definition (Rule 2(t), FEM Non-Debt Instruments Rules 2019; para 2.1.20 FDI Policy 15-10-2020)**

**Regulator and recordkeeping**
- **SEBI** regulates FPI in India.
- **NSDL (National Securities Depository Limited)** maintains the public list of registered FPIs in India.
- **Foreign Portfolio Investment (FPI)**: cross-border investment by a non-resident in equity instruments of < 10% of a listed Indian company's paid-up share capital (fully diluted basis). ⭐ (exam-important)
- **SEBI**: Securities and Exchange Board of India — regulator of FPI. ⭐ (exam-important)
- **NSDL**: National Securities Depository Limited — maintains the registered-FPI list.

**Quick Recall:**
- FDI vs FPI threshold = 10%.
- SEBI = regulator; NSDL = registry.

### 23.9 Difference between FDI and FPI 🔴
| Aspect | FDI | FPI |
|---|---|---|
| **Business interest** | Direct — establishes presence | Indirect — financial assets only |
| **Knowledge / tech transfer** | Yes (tech know-how, mgmt practices, joint ventures) | No |
| **Duration** | Long-term | Short-term |
| **Mode** | Manufacturing unit, acquisition, JV | Securities/assets outside the country |
| **Investor type** | Institutions, VC firms | Any market participant in securities |
| **Liquidity** | Low (long-term) | High (easily bought/sold) |
| **Activeness** | Active investor | Passive investor |
| **Decision-making say** | Yes — actively participates in mgmt | No — no role in management |
| **Risk type** | Political, economic, regulatory, structural | Market volatility, currency / interest-rate fluctuations |
| **Risk magnitude** | Higher | Lower than FDI |
| **Threshold (India)** | ≥ 10% | < 10% |

**Quick Recall:**
- FDI = direct, long-term, active, illiquid, control. FPI = indirect, short-term, passive, liquid, no control.
- 10% line is the legal divider.

### ⚠️ Common Mistakes
- ❌ "FPI is riskier than FDI" → ✅ FDI is riskier overall (political, structural). FPI risk is mostly market-volatility risk.
---

### 23.10 Categories of FPI 🔴
| Category | Risk | Examples |
|---|---|---|
| **Category I** | **Low** | Government / govt-related: central banks, World Bank, IMF, **sovereign wealth funds** |
| **Category II** | **Medium** | Mutual funds, insurance firms, asset management companies, banks, pension funds |
| **Category III** | **High** | All other forms not in I or II — e.g., **private equity funds** |

**Quick Recall:**
- I = govt/SWFs; II = institutional managers; III = private/alt funds.
- Risk increases I → III.

### 23.11 Advantages and Disadvantages of FPI 🔴
1. **Stimulates stock demand** → cost-effective capital raising for companies.
2. **Greater diversification** for investors → broader investment base.
3. **Exchange-rate gains** — investors benefit from currency fluctuations.
4. **Access to larger markets** with potentially less competition than home market.
5. **Liquidity** — agility to capitalise on opportunities.
6. **Boosts stock market performance** — increased demand for Indian shares.
7. **Foreign capital inflow** for infrastructure, job creation, growth.
1. **Capital flight** — large inflows and outflows destabilise markets and FX rates; in uncertainty, foreign investors withdraw.
2. **Speculative behaviour** — short-term profits → market bubbles and volatility.
3. **Currency exposure** — exchange-rate fluctuations risk for both investors and economy.
4. **No long-term commitment** — investors don't align with country's long-term goals.
5. **Herd behaviour** — cascading panics.
6. **Short-termism** — pressure on local companies for quarterly results vs long-term growth.
7. **Manipulative activities** — exploitation of regulatory gaps.
8. **Regulatory burden** — managing FPI flows requires strong oversight to prevent abuses.

**Quick Recall:**
- 7 advantages (capital, diversification, FX, market access, liquidity, stock boost, growth).
- 8 disadvantages (capital flight, speculation, FX risk, no commitment, herd, short-termism, manipulation, regulation burden).
- **Builds on**: FDI concept and routes (this chunk + chunk 010).
- **Continues into**: chunk 012 — FPI eligibility, Unit 23 summary, exam questions.

### 23.12 Eligibility Criteria for FPI in India 🔴

**The 5 Eligibility Conditions**
1. **Non-resident status** — applicant must be a **non-resident Indian** as per the **Income Tax Act, 1961**.
2. **FATF clearance** — applicant must **NOT** be a citizen of a country listed under the **public statement of the Financial Action Task Force (FATF)** (i.e. high-risk / non-cooperative jurisdictions).
3. **Home-country eligibility** — applicant must be eligible to invest in securities **of other countries** under their own jurisdiction's rules.
4. **Charter authorisation** — applicant must be authorised to invest in securities by their **Memorandum of Association (MoA)** and **Articles of Association (AoA)**.
5. **BIS membership (banks only)** — if the applicant is a **bank**, the bank's home country's **central bank must be a member of the Bank for International Settlements (BIS)**.
- **FATF (Financial Action Task Force)**: inter-governmental body whose public statement lists high-risk jurisdictions; FPI applicants from these countries are barred. ⭐ (exam-important)
- **Bank for International Settlements (BIS)**: central-bankers' bank based in Basel; bank-applicants for FPI registration must come from a country whose central bank is a BIS member. ⭐ (exam-important)
- **Memorandum of Association (MoA)**: foundational charter of a company; must permit foreign-securities investment for FPI eligibility.
- **Articles of Association (AoA)**: company's internal rulebook; must permit foreign-securities investment for FPI eligibility.

**Quick Recall:**
- 5 criteria: NRI status → not on FATF list → home-country investment-eligible → MoA/AoA authorised → (if bank) central bank in BIS.
- Income Tax Act, 1961 defines NRI.
- FATF gate keeps high-risk jurisdictions out.
- BIS gate applies only to bank applicants.

### ⚠️ Common Mistakes
- ❌ "FPI eligibility = SEBI registration alone" → ✅ SEBI registration is governed by the **SEBI (Foreign Portfolio Investors) Regulations, 2019** but it is conditional on first satisfying these five eligibility criteria.
- ❌ "BIS condition applies to all applicants" → ✅ It applies **only when the applicant is a bank**.
- Builds on: **23.8 Concept of FPI** (Chunk 011) — defines who an FPI is; this section says who can become one.
- Builds on: **23.9 FDI vs FPI** (Chunk 011) — the < 10% threshold is the activity test; this section is the entity test.

**Quick Recall:**
- FDI = direct, long-term integrator; 4 benefits: trade, tech, development, jobs.
- FPI = passive financial-asset investment; lifts domestic asset prices.
- **Automatic Route**: entry route under which investment by a person resident outside India does **not** require prior approval of the **RBI or the Central Government**. ⭐ (exam-important)
- **Government Route**: entry route under which investment by a person resident outside India **requires prior Government approval**, and the foreign investment received under this route shall be subject to the conditions stipulated by the Government in its approval. ⭐ (exam-important)
- **Foreign Portfolio Investor**: a person registered under the provisions of the **SEBI (Foreign Portfolio Investors) Regulations, 2019**, as amended from time to time. ⭐ (exam-important)
- **RBI (Reserve Bank of India)**: regulates FDI in India; provides certain rules and regulations for FDI. ⭐ (exam-important)
- **SEBI (Securities and Exchange Board of India)**: provides guidelines for investments made in securities and other financial assets issued in another country. ⭐ (exam-important)

**Quick Recall:**
- **Automatic** = no approval; **Government** = prior approval required.
- **SEBI** regulates FPI; **RBI** regulates FDI; **NSDL** monitors limits & sub-limits.
- FPI is registered under **SEBI (FPI) Regulations, 2019**.

### ⚠️ Common Mistakes
- ❌ "RBI alone approves the Automatic Route" → ✅ Automatic Route requires **no** prior approval from either RBI **or** the Central Government.
- ❌ "NSDL grants the FPI licence" → ✅ NSDL only **monitors limits and sub-limits**; SEBI registers FPIs.
---

### 23.16 Answers/Hints to Check Your Progress (Exercises 1-4) 🔴
- 1. **FDI definition**: investment made outside the home country where an investor resident in one country invests in another country in a way that establishes a **long interest in** and a **high degree of influence over** an enterprise. ⭐
2. **FDI methods**: Greenfield Investment, Mergers & Acquisitions (M&A), Joint Ventures, Subsidiary Companies.
3. **Types of FDI**: Horizontal, Vertical, Conglomerate, Platform.
1. **Routes of FDI**: Automatic Route, Government Route.
2. **Advantages of FDI**: contributes significantly to host's economic growth; creates new jobs (foreign companies bring advanced tech, expertise, mgmt practices); raises exports as foreign companies use host resources to attract investment; etc.
3. **Disadvantages of FDI**: loss of control over domestic industries; vulnerability to economic fluctuations → instability; profit repatriation; environmental degradation; etc.
- 1. **FPI definition**: investment by a person resident outside India through equity instruments where such investment is **less than 10%** of the **post-issue paid-up share capital on a fully diluted basis** of a listed Indian company, OR **less than 10%** of the paid-up value of each series of an equity instrument of a listed Indian company. ⭐
2. **FDI vs FPI**: FDI establishes a **direct business interest** overseas; FPI is **not direct**, involves **passive** investors; FDI investors are **active**.
3. **Categories of FPI** (3): Cat I = low risk; Cat II = medium risk; Cat III = highest risk.
1. **Advantages of FPI**: stimulates demand for companies' stocks; offers greater diversification to investors; benefits from exchange-rate fluctuations; etc.
2. **Disadvantages of FPI**: may **destabilize financial markets and exchange rates**; may lead to **speculative behaviour**; may **expose currency to exchange-rate fluctuations**; etc.
3. **FPI eligibility**: must be NRI (Income Tax Act 1961); must NOT be a citizen of a country on the FATF public statement; if a bank, the home-country central bank must be a BIS member; etc.

**Quick Recall:**
- **FDI definition** → "long interest + high degree of influence" — memorise verbatim.
- **FPI definition** → "< 10% post-issue paid-up share capital on fully diluted basis" — memorise verbatim.
- **3-pointer answers** are standard: list 3-4 bullets crisply.
- Closes Unit 23 — last chunk of Block 6.
- Cross-refs back to: chunk 010 (FDI methods/types), chunk 011 (FDI routes, FDI adv/disadv, FDI Policy 2020, FPI concept, FDI vs FPI, FPI categories, FPI adv/disadv), and this chunk's §23.12 (FPI eligibility).
1. How does the FATF public-statement list shift over time and what compliance costs does that impose on Indian custodians of FPI flows?
2. How are LLP downstream investments treated under the Automatic Route in practice, given SEBI/RBI co-regulation?
