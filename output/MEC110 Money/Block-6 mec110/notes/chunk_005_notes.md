# Chunk 005 — Unit 20: Arbitrage Pricing Theory (APT) — Foundations & Empirics
<!-- Pages: 37-46 -->
<!-- Source: chunk_005.txt -->
<!-- Continues from: Unit 19 CAPM (chunk 004) -->

## Section: 20.0–20.1 Unit 20 Objectives & Introduction 🟢

### Core Idea
Unit 20 introduces APT as a generalisation of CAPM. Stephen A. Ross critiqued CAPM's reliance on a single market factor and proposed a multi-factor model — APT — that allows multiple sources of systematic risk and empirical identification of factors.

> **In Simple Terms:** CAPM said "the market" is the only risk that gets paid. Ross said "actually, lots of macro forces matter — interest rates, inflation, GDP, oil prices…" APT lets each of these have its own risk premium.

### Connections
- **Builds on**: CAPM (Unit 19, chunks 003-004).
- **Generalises to**: Fama-French three-factor model (referenced in §20.5.2).

---

## Section: 20.2 Ross's Critique of CAPM 🔴

### Core Idea
Ross argued CAPM is an oversimplification. He grouped his concerns into "drawbacks" (4 items) and "simplifying assumptions" (5 items) — these are the standard exam-answer lists.

### Key Concepts — 4 Drawbacks of CAPM
1. **Single-factor model** — only β / market risk; ignores other systematic forces.
2. **Homogeneous expectations** — assumes all investors agree on returns, SDs, correlations.
3. **Static risk** — assumes asset risk is constant over time; reality changes with economy, tech, sentiment.
4. **Risk-free rate assumption** — uses a constant baseline; gov't-bond proxy assumes no default risk, may not hold.

### Key Concepts — 5 Simplifying Assumptions of CAPM
1. **Perfect markets** — no transaction costs, no taxes, no short-sale restrictions.
2. **Homogeneous assets** — all assets fully described by expected return + β.
3. **Normal distribution of returns** — ignores fat tails, volatility clustering.
4. **Constant correlations** — correlations actually change in crises / turbulence.
5. **Investor rationality** — ignores behavioural-finance evidence of biases.

> **Quick Recall:**
> - 4 drawbacks: single-factor, homogeneous expectations, static risk, risk-free rate.
> - 5 assumptions: perfect markets, homogeneous assets, normal distribution, constant correlations, rationality.

### ⚠️ Common Mistakes
- ❌ Confusing drawbacks with assumptions in the answer → ✅ Drawbacks = model design flaws; assumptions = simplifications about markets/investors.

---

## Section: 20.3 Introduction to APT 🔴

### Core Idea
**Arbitrage Pricing Theory (APT)** — Stephen Ross, "The Arbitrage Theory of Capital Asset Pricing", 1976. APT models expected return as a linear combination of multiple **macroeconomic factors**, each with its own sensitivity (factor β) and risk premium (λ). It does *not* pre-specify the factors — they are identified empirically.

> **In Simple Terms:** Different stocks dance to different tunes — some to interest rates, some to oil, some to inflation. APT lets every tune have its own price for risk and adds them up.

### Key Concepts

#### APT Equation
$$E(R_i) = R_f + \beta_{i1} \lambda_1 + \beta_{i2} \lambda_2 + \cdots + \beta_{ik} \lambda_k + \epsilon_i$$

Where:
- $E(R_i)$ = expected return on asset *i*
- $R_f$ = risk-free rate
- $\beta_{ij}$ = sensitivity of asset *i* to factor *j*
- $\lambda_j$ = risk premium associated with factor *j*
- $\epsilon_i$ = idiosyncratic / specific return component for asset *i*

#### Arbitrage discipline
- **No-arbitrage assumption**: investors cannot consistently earn risk-free profits from price discrepancies. Any mispricing is corrected by arbitrageurs.
- **Law of One Price**: assets with similar risk exposures must have similar expected returns; otherwise arbitrage exists.

#### Two key advantages
- **Flexibility & dynamism** — multiple risk factors can be priced.
- **Empirical factor identification** — factors found from data, not theory.

### Definitions
- **Arbitrage Pricing Theory (APT)**: a multi-factor asset pricing model in which expected return is a linear function of multiple macroeconomic factor sensitivities and their risk premia, derived from a no-arbitrage condition. ⭐ (exam-important)
- **Law of One Price**: assets with the same risk exposures should have the same expected return — otherwise arbitrage exists. ⭐ (exam-important)
- **Factor sensitivity (β_ij)**: how much asset *i*'s return moves with factor *j*. ⭐ (exam-important)
- **Risk premium (λ_j)**: extra expected return for bearing one unit of factor *j* risk.
- **Idiosyncratic return (ε_i)**: asset-specific component, diversifiable.

---

## Section: 20.3.1 Assumptions of APT 🔴

### Key Concepts — 5 Assumptions
1. **Separation of systematic & unsystematic risk** — systematic captured by factor βs; unsystematic is diversifiable and can be eliminated through portfolio construction.
2. **Efficient markets** — prices reflect all available info; mispricing is quickly corrected by arbitrage.
3. **Rational expectations** — investors form expectations using all available info.
4. **Absence of arbitrage opportunities** — no risk-free profits from mispricing; central to model.
5. **Investor rationality** — investors maximise expected utility given their info and preferences.

> **Quick Recall:**
> - APT assumptions cluster around: risk separation, market efficiency, rational expectations, no arbitrage, investor rationality.

---

## Section: 20.3.3 Key Differences between APT and CAPM 🔴

### Comparison Table — exam-tested

| Aspect | CAPM | APT |
|---|---|---|
| **Number of factors** | Single (market risk) | Multiple (macro factors: rates, inflation, GDP, industry) |
| **Factor identification** | Predefined (market portfolio, e.g., S&P 500 proxy) | Empirically identified from data; not predefined |
| **Sensitivity measure** | β = cov(R_i, R_m) / var(R_m) | Factor sensitivities β_ij — one per factor *j* |
| **Investor behaviour** | Rational, risk-averse, balance risk-return | No explicit assumption; focuses on factor-return relations |
| **Equation** | $E(R) = R_f + \beta(R_m - R_f)$ | $E(R) = R_f + \sum_j \beta_{ij} \lambda_j + \epsilon_i$ |

> **Quick Recall:**
> - 4 differences: # of factors, factor identification, sensitivity measure, investor-behaviour assumption.

### ⚠️ Common Mistakes
- ❌ "APT replaces β with multiple βs but is otherwise identical to CAPM" → ✅ APT also drops the homogeneous-expectations and predefined-factor structure; it is more flexible across the board.

---

## Section: 20.4 Empirical Studies on APT 🟡

### Core Idea
APT has been tested in three main applications: (1) **asset allocation**, (2) **cost of capital**, (3) **money-manager evaluation**. In each, factor selection is the central practical challenge — different studies pick different factors, with mixed results.

### Key Concepts — 3 Practical Applications

#### 1. Asset allocation
APT's factor structure connects to mean-variance efficiency. *k* factors imply a *k*-spanned efficient frontier; with *k* small, dimensionality is reduced. **Caveat**: if the factor structure is wrong, the resulting portfolio is not mean-variance efficient. *Pastor & Stambaugh (2000)* used Bayesian methods to incorporate investor priors.

#### 2. Cost of capital
Studies: *Elton, Gruber, & Mei (1994)*, *Bower & Schink (1994)*. Major issue = factor specification disagreement. The U.S. Federal Reserve Board has been reluctant to adopt APT for certain purposes due to factor instability.

#### 3. Money manager evaluation
Regress managed-fund returns on factors; compare intercepts to benchmark returns to gauge manager skill. Studies: *Busse (1999)*, *Carhart (1997)*. **Caveat**: APT is one-period — limits use for derivatives and dynamic trading strategies (stochastic discount factor problems). *Glosten & Jagannathan (1994)* suggest Black-Scholes for dynamic strategies instead.

### Challenges / Criticisms from Empirical Work — 5 issues
1. **Data limitations** — historical macro data is hard to collect and clean.
2. **Model misspecification** — wrong factor choice → wrong predictions.
3. **Time-varying betas** — factor sensitivities aren't static; assumption of constant β fails.
4. **Factor redundancy** — selected factors may be correlated/redundant; violates independence.
5. **Market efficiency concerns** — real markets aren't perfectly efficient; arbitrage may not correct all mispricing.

> **Quick Recall:**
> - APT applications: asset allocation, cost of capital, manager evaluation.
> - APT empirical issues: data, misspecification, time-varying β, factor redundancy, efficiency.

---

## Section: 20.5 Criticisms of APT 🔴

### 20.5.1 Critical Evaluation of APT's Assumptions — 5 critiques
1. **Arbitrage opportunities** — frictions, transaction costs, constraints prevent quick correction in reality.
2. **Market efficiency** — real markets imperfect; APT validity weakens.
3. **Factor independence** — APT assumes factors are independent; real factors often correlated.
4. **Static betas** — like CAPM, APT typically assumes constant β; really they vary with conditions.
5. **Investor rationality** — behavioural finance shows biases; rationality assumption questionable.

### 20.5.2 Comparison with Other Asset Pricing Models 🟡
| Comparison | Critic's view |
|---|---|
| **APT vs CAPM** | APT solves CAPM's single-factor flaw but introduces own assumption set; choice depends on data/use. |
| **APT vs Fama-French (3-factor)** | Fama-French extends APT with explicit market, size (SMB), value (HML) factors; often *better explanatory power* in empirical tests for size/value effects. |

### 20.5.3 Areas of Improvement for APT — 4 directions
1. **Dynamic factor sensitivities** — allow time-varying βs.
2. **Behavioural integration** — embed sentiment, biases.
3. **Better factor identification** — refine selection of macro variables; ensure independence and non-redundancy.
4. **Nonlinear relationships** — relax linear-factor assumption.

### Definitions
- **Fama-French Three-Factor Model**: APT extension with market, size (SMB = small-minus-big), and value (HML = high-minus-low book-to-market) factors. ⭐ (exam-important)

> **Quick Recall:**
> - 5 APT criticisms: arbitrage limits, market inefficiency, factor dependence, static betas, irrational investors.
> - Fama-French = market + SMB + HML.
> - 4 improvement directions: dynamic β, behavioural, better factors, nonlinearity.
<!-- Continues into chunk 006: Unit 20 wrap-up + Unit 21 Derivatives intro -->
