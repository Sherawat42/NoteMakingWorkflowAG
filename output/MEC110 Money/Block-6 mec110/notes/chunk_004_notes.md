# Chunk 004 — Unit 19 (cont.): CAPM Limitations, Empirical Analysis, Summary
<!-- Pages: 27-36 -->
<!-- Source: chunk_004.txt -->
<!-- Continues from: Unit 19 CAPM intro & applications (chunk 003) -->

## Section: 19.5 Limitations of CAPM (general) 🔴

### Core Idea
CAPM is widely used, but it rests on simplifying assumptions that often fail in real markets. Standard exam-answer list of seven limitations.

### Key Concepts — 7 General Limitations
1. **Restrictive assumptions** — perfect competition, frictionless markets, constant correlations, rational investors. Deviations distort predictions.
2. **Market index choice** — CAPM uses the market index as a proxy for the market portfolio; different indices → different β estimates and expected returns.
3. **Single-factor model** — only systematic risk (β) priced; ignores firm-specific risk, macro variables, sentiment.
4. **Linearity and homogeneity** — assumes all investors have identical risk preferences and a linear risk-return relation; reality is nonlinear and heterogeneous.
5. **Risk-free rate** — fluctuates over time; may not match investors' actual borrow/lend opportunities; changes shift the entire SML.
6. **Empirical validity** — mixed evidence; predictive power often weak, especially in turbulent or crisis periods.
7. **Non-market risks** — overlooks idiosyncratic risks (company events, regulation) that move prices.

### ⚠️ Common Mistakes
- ❌ Listing only "no transaction costs" → ✅ The exam expects the seven-point list above.

> **Quick Recall:**
> - 7 limits: assumptions, index, single-factor, linearity/homogeneity, risk-free rate, empirical validity, non-market risks.

---

## Section: 19.5.1 Theoretical Limitations of CAPM 🔴

### Core Idea
The theoretical limitations come from CAPM's idealised assumptions about markets and investors. Three are emphasised, each with a real-world example.

### Key Concepts — 3 Theoretical Limitations

#### 1. Perfect market assumptions
CAPM assumes all info is freely accessible, zero transaction costs, no borrowing/lending restrictions. Real markets have asymmetric info, transaction costs, regulation.
- **Example:** *2007–08 Global Financial Crisis* — info asymmetries, liquidity shortages, regulatory interventions distorted prices and broke CAPM predictions.

#### 2. Homogeneous investor behaviour
CAPM assumes identical expectations, risk preferences, and time horizons. Real investors differ.
- **Example:** *During market volatility*, some investors turn risk-averse (demand higher returns), others take on more risk for higher returns — heterogeneous reactions break the single risk-return curve.

#### 3. Single-factor model
β alone determines expected return. Reality: macro events, geopolitics, sentiment, interest-rate shifts, inflation, regulatory change all matter.
- **Example:** Periods of high uncertainty (geopolitical, macro) cause asset returns to depend on factors *beyond* β — CAPM under-predicts.

> **Quick Recall:**
> - 3 theoretical limits: perfect market, homogeneous investors, single-factor.

---

## Section: 19.5.2 Practical Limitations of CAPM 🔴

### Core Idea
Even if assumptions were tolerable, applying CAPM in practice runs into three problems — nonlinear risk-return, input sensitivity, and weak forecasting power.

### Key Concepts — 3 Practical Limitations

#### 1. Non-linear risk-return relationship
CAPM assumes linearity: higher β → proportionally higher return. In reality, the relationship may bend, especially at extremes.
- **Example:** *Tech start-ups* — high risk, high *potential* return. Many fail outright; survivors deliver outsize returns. Real distribution is skewed and nonlinear, not the smooth line CAPM assumes.

#### 2. Sensitivity to inputs and assumptions
CAPM uses $R_f$, market risk premium, and β as inputs. All are uncertain or estimated.
- **Example:** *Estimating market risk premium* — not directly observable. Different analysts use different historical windows or methods → divergent estimates → small variations cause large swings in expected returns.
- Implication: small input changes → unreliable forecasts in dynamic / uncertain environments.

#### 3. Poor predictor of returns
Empirical evidence: predicted returns from CAPM correlate weakly with realised returns. Asset returns are *not* explained by systematic risk alone — major problem because investing relies on return forecasts.

> **Quick Recall:**
> - 3 practical limits: nonlinearity, input sensitivity, weak prediction.

### ⚠️ Common Mistakes
- ❌ Mixing up theoretical and practical limitations in answers → ✅ Theoretical = assumptions about markets/investors; Practical = problems applying the math.

---

## Section: 19.6 Empirical Analysis of CAPM 🔴

### Core Idea
CAPM is testable — researchers fit it to data via several methods to see how well it explains real returns. Four standard methodologies are listed in the unit.

### Key Concepts — 4 Empirical Methodologies

| Method | What is done | Example |
|---|---|---|
| **Time-series analysis** | Collect historical returns of asset & market over a period; regress to estimate β; compare CAPM-predicted vs actual returns over time | 10-year study of stocks' β vs subsequent returns |
| **Cross-sectional analysis** | Across many assets at one point in time, test whether higher β → higher expected return | Sample stocks across industries; compare CAPM vs actual returns |
| **Event studies** | Examine how prices react to specific events (earnings, mergers); compare event-window returns to CAPM predictions | Quarterly earnings announcement reactions |
| **Portfolio performance evaluation** | Compute portfolio β, compare CAPM expected return to actual portfolio return → over- or under-performance | Investor evaluating their diversified portfolio over 1 year |

### Examples — Worked CAPM empirical example
**Setup:** $R_f$ = 3%, $E(R_m)$ = 8%, $\beta_A$ = 1.2.

$E(R_A) = R_f + \beta_A \times (E(R_m) - R_f) = 0.03 + 1.2 \times (0.08 - 0.03) = 0.03 + 0.06 = 0.09 = 9\%$.

If actual return = 10% > 9% predicted, Stock A **outperformed** relative to its systematic risk → positive alpha.

> **Quick Recall:**
> - 4 empirical methods: time-series, cross-sectional, event study, portfolio performance.
> - Outperformance test: actual > CAPM expected return ⇒ positive alpha.

---

## Section: 19.7 Let Us Sum Up 🟢

### Summary points
- CAPM links risk and return for assets / portfolios in well-diversified markets.
- Risk that matters = **systematic risk**, measured by **β**.
- Expected return = $R_f + \beta (E(R_m) - R_f)$.
- $R_f$ proxied by government-bond yields (no default risk).
- Market risk premium = excess of market expected return over $R_f$.
- Market portfolio = theoretical portfolio of all assets weighted by market value.
- CAPM implies investors hold a combination of risk-free asset + market portfolio (capital market line / efficient frontier with risk-free borrowing-lending).
- Wide use: asset pricing, portfolio management, performance evaluation.
- Limitations: simplifying assumptions, historical-data reliance, can't capture non-market risks, mixed empirics.
- Extensions: multi-factor models (e.g., APT — Unit 20), behavioural finance frameworks.

### Key Words (Unit 19 Glossary)
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

### Connections
- **Builds on**: Markowitz (Unit 18, chunks 001–002).
- **Extended by**: APT (Unit 20, chunks 005+) — multi-factor generalisation.
- **Pairs with**: Sharpe ratio (chunk 003) and α (chunk 003) for performance evaluation.

### Open Questions (Terminal Questions to revisit)
1. Common statistical measures of CAPM goodness-of-fit (R², t-statistics on β).
2. How do anomalies (e.g., size, value, momentum) affect CAPM applicability?
3. Theoretical vs practical limitations — must answer both halves separately.
<!-- Continues into chunk 005: Unit 20 — Arbitrage Pricing Theory -->
