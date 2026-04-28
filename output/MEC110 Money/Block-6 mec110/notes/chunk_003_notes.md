# Chunk 003 — Unit 19: CAPM Foundations, Sharpe Ratio, Applications
<!-- Pages: 19-26 -->
<!-- Source: chunk_003.txt -->
<!-- Continues from: Unit 18 Markowitz / Efficient Frontier (chunk 002) -->

## Section: 19.0–19.1 Unit 19 Objectives & Introduction 🟢

### Core Idea
Unit 19 extends the Markowitz framework by *pricing* risk: it introduces the Capital Asset Pricing Model (CAPM), which links a single asset's expected return to its systematic risk via β. CAPM gives a price for risk and a benchmark expected return for any asset.

> **In Simple Terms:** Markowitz tells you which combinations of assets are good. CAPM tells you what return you should *demand* for owning a particular asset given how risky it is *relative to the market*.

### Connections
- **Builds on**: §18.5 Markowitz / Efficient Frontier (chunk 002).
- **Extends**: Risk-return measurement from §18.3 (chunk 001).

---

## Section: 19.2 The Capital Asset Pricing Model (CAPM) 🔴

### Core Idea
Developed in the **1960s** by **William Sharpe, John Lintner, and Jan Mossin**, CAPM is a single-factor model that quantifies the expected return on an investment based on its **systematic risk (β)**. It produces a linear relationship: expected return = risk-free rate + β × market risk premium.

> **In Simple Terms:** CAPM is a pricing rule for risk. It says: start with what you'd earn risk-free, then add a premium for the market's overall risk, scaled up or down by how sensitive your asset is to the market.

### Key Concepts

#### Building blocks of CAPM
| Concept | Meaning |
|---|---|
| **Systematic risk** | Risk that cannot be diversified away — economic downturns, interest-rate moves, geopolitics. |
| **Beta (β)** | Sensitivity of an asset's returns to changes in the overall market. β = 1: moves with market; β > 1: more volatile; β < 1: less volatile. |
| **Risk-free rate ($R_f$)** | Return on a zero-risk investment, typically the yield on government bonds. Baseline. |
| **Market risk premium ($R_m - R_f$)** | Additional return investors demand for bearing systematic risk; expected market return minus the risk-free rate. |
| **Market portfolio** | A diversified portfolio containing all risky assets, weighted by market capitalisation. Benchmark in CAPM. |

#### CAPM Equation
$$E(R_i) = R_f + \beta_i \times (R_m - R_f)$$

Where:
- $E(R_i)$ = expected return of asset *i*
- $R_f$ = risk-free rate (proxy: government bond yield)
- $\beta_i$ = beta of asset *i* (systematic-risk sensitivity)
- $R_m$ = expected return on the market portfolio (proxy: broad index, e.g., S&P 500)
- $(R_m - R_f)$ = market risk premium

### Definitions
- **Capital Asset Pricing Model (CAPM)**: a single-factor model linking expected return on an asset to its systematic risk, $E(R_i) = R_f + \beta_i (R_m - R_f)$. ⭐ (exam-important)
- **Beta (β)**: measure of an asset's sensitivity to market movements (= cov(R_i, R_m) / var(R_m), implicitly). β = 1 ↔ moves with market; β > 1 ↔ more volatile; β < 1 ↔ less volatile. ⭐ (exam-important)
- **Risk-free rate ($R_f$)**: return on a zero-risk asset; typically yield on government bonds. ⭐ (exam-important)
- **Market risk premium**: $R_m - R_f$ — excess return demanded for bearing systematic risk. ⭐ (exam-important)
- **Market portfolio**: a diversified portfolio of all risky assets, weighted by market capitalisation.

### Distinctive features of CAPM (memorise — list of 7)
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

> **Quick Recall:**
> - Founders: Sharpe, Lintner, Mossin (1960s).
> - Equation: $E(R_i) = R_f + \beta_i (R_m - R_f)$.
> - Single factor: β.
> - Only systematic risk earns a premium.

---

## Section: 19.3 Sharpe Ratio (Importance of Sharpe's Theory) 🔴

### Core Idea
The **Sharpe ratio**, derived from CAPM, measures **risk-adjusted return** — excess return per unit of total risk. A higher Sharpe ratio = better risk-adjusted performance. It is the standard metric for comparing portfolio performance.

> **In Simple Terms:** It's bang-for-the-buck for risk. Two portfolios may both earn 10%, but the one that does so with less volatility has a higher Sharpe ratio — it gave you more return per unit of stomach-churn.

### Key Concepts

#### Formula
$$\text{Sharpe ratio} = \frac{R_p - R_f}{\sigma_p}$$

Where:
- $R_p$ = expected return on the investment / portfolio
- $R_f$ = risk-free rate (yield on government bonds)
- $\sigma_p$ = standard deviation of portfolio returns (volatility / risk)

The numerator is the **excess return**; the denominator is **total risk**. Dividing gives a standardised risk-adjusted return.

#### Six objectives / functions of the Sharpe ratio
1. **Objective measurement of risk-adjusted performance** — standardised metric; lets investors compare across investments consistently.
2. **Quantifying the risk-return tradeoff** — excess return per unit of risk; tells you whether reward compensates for volatility.
3. **Portfolio allocation decision** — pick portfolios with the highest return per unit of risk.
4. **Performance evaluation tool** — gauge skill of fund managers vs. benchmark / peers.
5. **Risk management tool** — manage exposures, ensure diversification, optimise risk-return per investor's preferences.
6. **Benchmark comparison** — compare a portfolio's risk-adjusted return to a market index or target return.

### Definitions
- **Sharpe ratio**: a measure of risk-adjusted return, $(R_p - R_f) / \sigma_p$ — excess return per unit of total risk. ⭐ (exam-important)
- **Excess return**: $R_p - R_f$ — return above the risk-free rate.

> **Quick Recall:**
> - SR = (R_p − R_f) / σ_p.
> - Numerator: excess return; Denominator: total risk (σ_p, NOT β).
> - Higher SR = better risk-adjusted performance.

### ⚠️ Common Mistakes
- ❌ Using β in the denominator → ✅ That is the **Treynor ratio**. Sharpe uses **σ_p** (total risk).
- ❌ Forgetting to subtract $R_f$ — without it, you get raw return, not risk-adjusted.

---

## Section: 19.3.2 Importance & Role of Sharpe's Theory in an Economy (Macro Applications) 🟡

### Core Idea
Though primarily a finance metric, Sharpe-ratio logic — *expected benefit per unit of risk* — can be applied to macroeconomic policy evaluation: fiscal, monetary, and structural-reform decisions can each be assessed for risk-adjusted effectiveness.

### Key Concepts — three illustrative macro applications
| Policy | Numerator (benefit) | Denominator (risk/volatility) | High SR ⇒ |
|---|---|---|---|
| **Expansionary fiscal** (↑G, ↓T) | Expected ↑GDP / aggregate demand | ↑Govt debt or inflation volatility | Benefits outweigh debt/inflation risks |
| **Accommodative monetary** (↓ rates) | ↑Output, ↑employment | Asset-price bubble risk, currency depreciation volatility | Growth gains outweigh bubble/FX risks |
| **Structural reforms** (deregulation, labour reform, infra) | Long-term growth gains | Short-term adjustment costs / uncertainty | Long-term gains justify short-term cost |

A **low Sharpe ratio** signals risks may outweigh benefits — re-think the policy.

> **Quick Recall:**
> - SR can extend to macro: numerator = expected benefit, denominator = volatility/risk of side-effects.
> - Three macro examples: fiscal stimulus, monetary easing, structural reforms.

---

## Section: 19.4 Application of CAPM 🔴

### Core Idea
CAPM is applied in three core financial-economics tasks: (1) estimating expected returns, (2) computing cost of equity, and (3) measuring risk-adjusted performance via alpha.

### Key Concepts — three applications

#### 1. Expected Return Estimation
$$E(R_i) = R_f + \beta_i \times (E(R_m) - R_f)$$

**Worked example:** Stock with β = 1.2, $R_f$ = 3%, $E(R_m)$ = 8%.
$E(R_i) = 0.03 + 1.2 \times (0.08 - 0.03) = 0.03 + 1.2 \times 0.05 = 0.03 + 0.06 = 0.09 = 9\%$.

#### 2. Cost of Equity Calculation
Cost of equity = required return for shareholders. Substitute the company's β into CAPM. Used in capital budgeting and valuation.

**Worked example:** β = 1.5, $R_f$ = 4%, market risk premium = 6%.
$\text{Cost of Equity} = 0.04 + 1.5 \times 0.06 = 0.04 + 0.09 = 0.13 = 13\%$.

#### 3. Risk-Adjusted Performance Measurement (Alpha)
Compare actual portfolio return with CAPM-predicted expected return:
$$\alpha = R_{\text{actual}} - E(R)_{\text{CAPM}}$$

**Worked example:** Actual return 10%, CAPM expected return 8% → α = +2% (positive alpha = manager outperformed risk-adjusted benchmark).

### Definitions
- **Alpha (α)**: excess return of a portfolio over its CAPM-predicted expected return; measures manager's skill / outperformance. ⭐ (exam-important)
- **Cost of equity**: return required by shareholders, computed via CAPM with the firm's β.

### ⚠️ Common Mistakes
- ❌ Treating α > 0 as proof of skill in a single period → ✅ It can be luck; need many periods + statistical significance.
- ❌ Using historical β only — β can shift over time as a firm's leverage / business changes.

> **Quick Recall:**
> - Three CAPM uses: expected return, cost of equity, α (performance).
> - Worked numbers: 9%, 13%, +2% α — useful templates.

### Connections
- **Builds on**: CAPM equation (this chunk).
- **Pairs with**: Sharpe ratio (this chunk) — both are CAPM-derived performance tools, but Sharpe uses σ_p while CAPM/α uses β.
<!-- Continues in chunk 004: Limitations and empirical analysis of CAPM -->
