# Chunk 001 — Estimation of Two-Variable Regression: Setup & Estimation Methods
<!-- Pages: 1–10 -->
<!-- Source: chunk_001.txt -->

## Section: Unit 4 Overview & Objectives 🟢

### Core Idea
Unit 4 covers the estimation of two-variable (bivariate) regression models. After studying a sample, we use estimation to recover the unknown parameters (β₁ and β₂) that generated the data. Three methods are introduced: Ordinary Least Squares (OLS), Method of Moments (MOM), and Maximum Likelihood Estimation (MLE).

> **In Simple Terms:** When we can't study everyone in a population, we study a sample and use mathematical rules to guess the population's true relationship between two variables — like income and savings.

### Key Concepts

#### Population vs Sample Regression
The relationship between Y and X in the **population** is given by the **Population Regression Function (PRF)**: Yᵢ = β₁ + β₂Xᵢ + uᵢ. Since this is not directly observable, we estimate it from the sample using the **Sample Regression Function (SRF)**: Ŷᵢ = β̂₁ + β̂₂Xᵢ. The difference between actual Yᵢ and estimated Ŷᵢ is the **residual** ûᵢ.

### Definitions
- **Estimation**: The process of recovering the unknown parameters (β₁, β₂) that were used to generate the sample data. ⭐ (exam-important)
- **Residual (ûᵢ)**: ûᵢ = Yᵢ − Ŷᵢ. The difference between the actual observed value and the predicted value. Distinguished from the error term uᵢ.
- **PRF (Population Regression Function)**: Yᵢ = β₁ + β₂Xᵢ + uᵢ — the true unobservable relationship.
- **SRF (Sample Regression Function)**: Ŷᵢ = β̂₁ + β̂₂Xᵢ — the estimated relationship from sample data.

> **Quick Recall:**
> - Three estimation methods: OLS, MOM, MLE
> - PRF is unobservable; SRF is estimated
> - Residual ûᵢ = Yᵢ − Ŷᵢ

### Connections
- Builds on: basic statistics and probability (MEC 203 Units 30–31)

---

## Section: Classical Assumptions of OLS 🔴

### Core Idea
The OLS method rests on five classical assumptions about the stochastic error term uᵢ. These define the "ideal conditions" for estimation. All five collectively are called the **Classical Regression Model** assumptions. The fifth assumption (normality) is not needed for OLS but is required for hypothesis testing.

> **In Simple Terms:** Think of these assumptions as the "rules the errors must follow" — if they do, OLS gives us the best possible estimates.

### Key Concepts

#### The Five Classical Assumptions
1. **E(uᵢ) = 0** [Eq. 4.4]: The average error across the population is zero — positive errors cancel negative ones. This implies the regression line is correctly specified (no systematic bias).
2. **E(uᵢ²) = σ²** [Eq. 4.5]: The variance of the error term is constant (σ²) for all observations. This is **homoscedasticity**. Example: variance of consumption expenditure is the same for rich and poor.
3. **E(uᵢuⱼ) = 0 for i ≠ j** [Eq. 4.6]: Error terms of different observations are uncorrelated — **no autocorrelation**.
4. **E(Xᵢuᵢ) = 0** [Eq. 4.7]: The explanatory variable Xᵢ is not correlated with the error term. This requires Xᵢ to be **non-stochastic** (fixed in repeated samples) and exogenously given.
5. **uᵢ ~ N(0, σ²)** [Eq. 4.8]: The error follows a **normal distribution** with zero mean and constant variance. Required for hypothesis testing, NOT for OLS estimation itself.

### Definitions
- **Classical Regression Model**: A regression model satisfying all five classical assumptions about the error term. ⭐ (exam-important)
- **Homoscedasticity**: Constant variance of error term: E(uᵢ²) = σ² for all i. ⭐ (exam-important)
- **No Autocorrelation**: E(uᵢuⱼ) = 0 for i ≠ j — errors across observations are uncorrelated. ⭐ (exam-important)
- **Non-stochastic X**: The regressor Xᵢ is exogenous and fixed in repeated sampling, ensuring E(Xᵢuᵢ) = 0.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming all 5 assumptions are needed for OLS → ✅ Correct: Assumption (v) — normality — is NOT needed for OLS; it IS needed for hypothesis testing.
- ❌ Mistake: Confusing error term uᵢ with residual ûᵢ → ✅ Correct: uᵢ is the true (unknown) error; ûᵢ is the estimated residual.

> **Quick Recall:**
> - E(uᵢ) = 0 → zero mean
> - E(uᵢ²) = σ² → homoscedasticity
> - E(uᵢuⱼ) = 0, i≠j → no autocorrelation
> - E(Xᵢuᵢ) = 0 → X is exogenous
> - uᵢ ~ N(0, σ²) → normality (for t/F tests only)

### Connections
- Continues into: OLS Method (Chunk 001), Matrix-form assumptions for multiple regression (Chunk 005)

---

## Section: OLS Method of Estimation 🔴

### Core Idea
OLS selects the estimates β̂₁ and β̂₂ that **minimize the Residual Sum of Squares (RSS)** — the sum of squared differences between observed and predicted Y values. Setting partial derivatives of RSS to zero yields two **normal equations**, which are solved simultaneously for β̂₁ and β̂₂.

> **In Simple Terms:** OLS finds the "best-fit" line by minimizing the total squared distance of all data points from the line. The closer points cluster to the line, the smaller the RSS.

### Key Concepts

#### Principle of Least Squares
Minimize RSS = Σûᵢ² = Σ(Yᵢ − β̂₁ − β̂₂Xᵢ)²
Conditions: (i) first derivative = 0; (ii) second derivative > 0.

#### Normal Equations
Taking partial derivatives and setting to zero:

**∂RSS/∂β̂₁ = 0** gives:
ΣYᵢ = nβ̂₁ + β̂₂ΣXᵢ ... (4.10)

**∂RSS/∂β̂₂ = 0** gives:
ΣXᵢYᵢ = β̂₁ΣXᵢ + β̂₂ΣXᵢ² ... (4.12)

These two simultaneous equations are the **normal equations**.

#### OLS Estimators — Formulas
From the normal equations:

**β̂₁ = Ȳ − β̂₂X̄** ... (4.13)

**β̂₂ = Σxᵢyᵢ / Σxᵢ²** ... (4.14)

where xᵢ = Xᵢ − X̄ and yᵢ = Yᵢ − Ȳ (deviations from sample means).

### Definitions
- **RSS (Residual Sum of Squares)**: Σûᵢ² = Σ(Yᵢ − β̂₁ − β̂₂Xᵢ)² — quantity minimized by OLS. ⭐ (exam-important)
- **Normal equations**: Two simultaneous equations derived by setting ∂RSS/∂β̂₁ = 0 and ∂RSS/∂β̂₂ = 0. ⭐ (exam-important)
- **OLS estimator β̂₂**: β̂₂ = Σxᵢyᵢ / Σxᵢ² (slope). ⭐ (exam-important)
- **OLS estimator β̂₁**: β̂₁ = Ȳ − β̂₂X̄ (intercept). ⭐ (exam-important)

### Mechanisms / Processes
1. Write RSS = Σ(Yᵢ − β̂₁ − β̂₂Xᵢ)²
2. Take ∂RSS/∂β̂₁ = 0 → Normal Equation 1
3. Take ∂RSS/∂β̂₂ = 0 → Normal Equation 2
4. Solve simultaneously → β̂₁, β̂₂

### Examples
**Example (from text):** For wage (w) and education (s): ŵ = 0.89 + 0.63s
- When s = 0 (illiterate): predicted wage = Rs. 0.89/hr
- When s = 8: predicted wage = 0.89 + 0.63(8) = Rs. 5.93/hr
- Each additional year of schooling → hourly wage increases by Rs. 0.63

**Savings example:** Savings = 34,560 + 0.58 Income → each Rs. 1,000 increase in income raises savings by Rs. 580.

### ⚠️ Common Mistakes
- ❌ Mistake: Using N in denominator for β̂₂ formula → ✅ Correct: β̂₂ = Σxᵢyᵢ / Σxᵢ² (deviation form)
- ❌ Mistake: Forgetting to convert to deviation form → ✅ xᵢ = Xᵢ − X̄, yᵢ = Yᵢ − Ȳ

> **Quick Recall:**
> - Minimize RSS → take derivatives → set to zero → solve normal equations
> - β̂₂ = Σxᵢyᵢ / Σxᵢ²
> - β̂₁ = Ȳ − β̂₂X̄
> - Regression line passes through (X̄, Ȳ)

### Connections
- Builds on: Classical Assumptions (this chunk)
- Extends to: Matrix form β̂ = (X'X)⁻¹X'Y for multiple regression (Chunk 005)

---

## Section: Method of Moments (MOM) 🟡

### Core Idea
MOM equates **sample moments** to **population moments** derived from classical assumptions. Using assumptions E(uᵢ) = 0 and E(Xᵢuᵢ) = 0 applied to the sample, we get the same two equations as OLS normal equations — confirming that MOM and OLS give **identical estimators**.

> **In Simple Terms:** MOM says "the sample should behave like the population on average" — plugging in sample data for population expectations gives the same answer as OLS.

### Key Concepts

#### Population vs Sample Moments
- Population moment 1: E(uᵢ) = 0 → becomes: (1/n)Σ(Yᵢ − β̂₁ − β̂₂Xᵢ) = 0 ... (4.17)
- Population moment 2: E(Xᵢuᵢ) = 0 → becomes: (1/n)ΣXᵢ(Yᵢ − β̂₁ − β̂₂Xᵢ) = 0 ... (4.18)

These reduce to the same normal equations as OLS (4.10) and (4.12). Hence **MOM = OLS in this context**.

### Definitions
- **Method of Moments**: An estimation method that equates population moments (derived from model assumptions) with sample moments to obtain parameter estimates. ⭐ (exam-important)

> **Quick Recall:**
> - MOM uses E(uᵢ) = 0 and E(Xᵢuᵢ) = 0 as moment conditions
> - MOM and OLS produce identical estimators for bivariate regression

### Connections
- Equivalent to: OLS Method (this chunk)
- Contrasts with: MLE (this chunk)

---

## Section: Maximum Likelihood Method (MLE) 🔴

### Core Idea
MLE chooses parameter estimates that **maximize the probability (likelihood) of observing the given sample data**. Under the normality assumption (uᵢ ~ N(0, σ²)), the MLE estimators of β₁ and β₂ are **identical to OLS**. However, the MLE estimator of σ² (σ̃² = RSS/n) is **biased** (underestimates true σ²), though it is consistent.

> **In Simple Terms:** MLE asks: "What values of the parameters make this sample most likely to have occurred?" Under normal errors, the answer is the same line as OLS gives.

### Key Concepts

#### Likelihood Function for Regression
Since uᵢ ~ N(0, σ²) and Yᵢ = β₁ + β₂Xᵢ + uᵢ, each Yᵢ is normally distributed. The likelihood function L(·) is the joint probability of observing all Yᵢ values.

#### Log-Likelihood Maximization
ln L(·) = −(n/2)·ln σ² − (n/2)·ln(2π) − (1/2)·Σ(Yᵢ − β₁ − β₂Xᵢ)²/σ²

Maximizing w.r.t. β₁ and β₂ gives the same normal equations as OLS (equations 4.33–4.34), so **MLEs of β₁ and β₂ equal OLS estimators**.

#### MLE of σ² — Biased Result
Taking ∂lnL/∂σ̃ = 0 yields:
**σ̃² = RSS/n** ... (4.35)

This is biased because the true unbiased estimator uses (n−2) in denominator: σ̂² = RSS/(n−2). However, MLE estimator is **consistent** (converges to true σ² as n → ∞).

### Definitions
- **Likelihood Function L(·)**: The joint probability of observing the sample data as a function of unknown parameters β₁, β₂, σ². ⭐ (exam-important)
- **Maximum Likelihood Estimates (MLEs)**: Parameter values that maximize L(·); for β₁ and β₂ they equal OLS estimates.
- **Biased MLE of σ²**: σ̃² = RSS/n is biased downward; uses n instead of (n−2). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking MLE always gives different estimates than OLS → ✅ Correct: Under normality, MLEs of β₁, β₂ are identical to OLS; only σ² estimate differs.
- ❌ Mistake: Using MLE σ̃² = RSS/n for inference → ✅ Correct: Use unbiased σ̂² = RSS/(n−2) for hypothesis testing.

> **Quick Recall:**
> - MLE of β₁, β₂ = OLS estimators (under normality)
> - MLE of σ² = RSS/n → biased but consistent
> - OLS estimator of σ² = RSS/(n−2) → unbiased

### Connections
- Equivalent to OLS for β̂: OLS Method (this chunk)
- MLE σ̃² discussed further: Standard Error section (Chunk 002)

---

## Section: Interpretation of OLS Estimators 🔴

### Core Idea
There are three regression model forms: linear, semi-log, and double-log. Each requires a different interpretation of the slope coefficient β₂. The form chosen depends on the nature of the relationship between Y and X as suggested by economic theory.

> **In Simple Terms:** How you read "a one-unit change in X causes this change in Y" depends entirely on whether the variables are in raw or log form.

### Key Concepts

#### Linear Model: Yᵢ = β₁ + β₂Xᵢ + uᵢ
β₂ = dY/dX = the absolute change in Y for a one-unit change in X.
**Example:** ŵ = 0.89 + 0.63s → each additional year of schooling raises wage by Rs. 0.63/hr.

#### Semi-Log Model: ln Yᵢ = β₁ + β₂Xᵢ + uᵢ
β₂ = percentage change in Y for a one-unit change in X (proportional/growth rate interpretation).

#### Double-Log (Log-Linear) Model: ln Yᵢ = β₁ + β₂ ln Xᵢ + uᵢ
β₂ = **elasticity** of Y with respect to X. A 1% change in X causes a β₂% change in Y.

| Model Type | Y | X | β₂ Interpretation |
|------------|---|---|-------------------|
| Linear | Levels | Levels | ΔY per unit ΔX |
| Semi-log | ln Y | Levels | % change in Y per unit ΔX |
| Double-log | ln Y | ln X | Elasticity (% ΔY per % ΔX) |

### Definitions
- **Semi-log model**: Regression where only the dependent variable is in logarithmic form; β₂ gives % change in Y per unit change in X. ⭐ (exam-important)
- **Double-log / Log-linear model**: Both variables in log form; β₂ is a constant elasticity. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Interpreting β₂ as elasticity in a linear model → ✅ Correct: Elasticity interpretation applies only to double-log models.

> **Quick Recall:**
> - Linear: β₂ = ΔY per unit ΔX
> - Semi-log: β₂ = % ΔY per unit ΔX
> - Double-log: β₂ = elasticity (% ΔY per % ΔX)

### Connections
- Builds on: OLS Method (this chunk)
- Continues into: Standard Error of Estimators (Chunk 002)

### Open Questions
1. Wage example in CYP1 Q2 (n=526 workers) — compute β̂₂ and interpret.
