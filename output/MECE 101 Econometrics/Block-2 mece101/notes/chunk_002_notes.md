# Chunk 002 — Estimation of Two-Variable Regression: Standard Errors, Properties, Goodness of Fit, Hypothesis Testing & Forecasting
<!-- Pages: 11–22 -->
<!-- Source: chunk_002.txt -->
<!-- See chunk 001 for start of Unit 4 -->

## Section: Standard Error of OLS Estimators 🔴
<!-- Continues from: Interpretation of OLS Estimators (Chunk 001) -->

### Core Idea
Since β̂₁ and β̂₂ are computed from sample data, they vary across samples. We need to measure this variability through the **standard error (se)** — the positive square root of their variance. The variances depend on the unknown σ², which is estimated from the sample. These standard errors are essential for hypothesis testing and confidence intervals.

> **In Simple Terms:** The standard error tells us how much our slope estimate would wiggle if we drew many different samples — a smaller se means we can trust the estimate more.

### Key Concepts

#### Variance of β̂₂
var(β̂₂) = σ² / Σxᵢ² ... (4.40)

se(β̂₂) = σ / √(Σxᵢ²) ... (4.41)

Interpretation: var(β̂₂) is **directly proportional to σ²** and **inversely proportional to Σxᵢ²**. Therefore:
- Greater variation in X values → larger Σxᵢ² → smaller var(β̂₂) → more precise β̂₂
- Larger sample size → larger Σxᵢ² → smaller variance

#### Variance of β̂₁
var(β̂₁) = (ΣXᵢ² / n·Σxᵢ²) · σ² ... (4.42)

se(β̂₁) = √(ΣXᵢ² / n·Σxᵢ²) · σ ... (4.43)

var(β̂₁) is directly proportional to σ² and ΣXᵢ², inversely proportional to Σxᵢ² and n.

#### Estimator of Error Variance (σ̂²)
The true σ² is unknown. OLS unbiased estimator:
**σ̂² = RSS / (n−2) = Σûᵢ² / (n−2)** ... (4.44)

The denominator (n−2) = degrees of freedom for simple regression (2 parameters β̂₁ and β̂₂ are estimated).

Contrast: MLE estimator σ̃² = RSS/n is **biased** (too small); σ̂² = RSS/(n−2) is **unbiased** but consistent.

### Definitions
- **Standard Error (se)**: The positive square root of an estimator's variance; measures precision of the estimator. ⭐ (exam-important)
- **Unbiased estimator of σ²**: σ̂² = RSS/(n−2) — uses (n−2) degrees of freedom for simple regression. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Using σ̃² = RSS/n (MLE) for inference → ✅ Correct: Use σ̂² = RSS/(n−2) for unbiased standard errors.
- ❌ Mistake: Thinking more X variability increases estimation error → ✅ Correct: More variability in X (larger Σxᵢ²) reduces var(β̂₂).

> **Quick Recall:**
> - var(β̂₂) = σ²/Σxᵢ² → wider X spread = more precision
> - var(β̂₁) = σ²·ΣXᵢ²/(n·Σxᵢ²)
> - σ̂² = RSS/(n−2) → unbiased; σ̃² = RSS/n → biased (MLE)
> - se = √var(·)

### Connections
- Builds on: OLS estimators β̂₁, β̂₂ (Chunk 001)
- Used in: Hypothesis testing (this chunk), Confidence intervals (this chunk)

---

## Section: Properties of OLS Estimators — Algebraic & Statistical 🔴

### Core Idea
OLS estimators have two categories of properties: **algebraic (numerical)** properties that hold for any sample, and **statistical properties** (unbiasedness, consistency, efficiency) that describe behaviour in repeated sampling. The most important result is the **Gauss-Markov Theorem**: OLS is BLUE.

> **In Simple Terms:** OLS gives you estimates that are, on average, correct (unbiased), get better with more data (consistent), and have the smallest possible error among all "fair" linear rules (efficient = BLUE).

### Key Concepts

#### Algebraic Properties of OLS (Numerical — always hold)
1. OLS provides **point estimates** — one value per parameter.
2. The regression line passes through the **sample means** (X̄, Ȳ): Ȳ = β̂₁ + β̂₂X̄.
3. Mean of predicted values = mean of actual values: Ȳ̂ = Ȳ ... (4.45).
4. The SRF in **deviation form**: ŷᵢ = β̂₂xᵢ ... (4.49).
5. The **residual ûᵢ and Ŷᵢ are uncorrelated**: Σŷᵢûᵢ = 0 ... (4.50).
6. The **residual ûᵢ and Xᵢ are uncorrelated**: ΣXᵢûᵢ = 0.

#### Statistical Properties: Unbiasedness
E(β̂₂) = β₂ — the expected value of the estimator equals the true parameter. (Proved by substituting β̂₂ = β₂ + Σcᵢuᵢ and using E(uᵢ) = 0).

#### Statistical Properties: Efficiency (Gauss-Markov Theorem)
Any other linear unbiased estimator b₂ = Σdᵢyᵢ has var(b₂) ≥ var(β̂₂).
The OLS estimator β̂₂ has **minimum variance** in the class of all linear unbiased estimators.

**Proof sketch:**
- Let b₂ = Σdᵢyᵢ be any linear unbiased estimator with Σdᵢxᵢ = 1 (unbiasedness condition).
- var(b₂) = Σdᵢ²·σ². Minimize this subject to Σdᵢxᵢ = 1 using Lagrangian.
- Solution: dᵢ = xᵢ/Σxᵢ² = cᵢ → this is exactly the OLS weight.
- Therefore, minimum-variance linear unbiased estimator is the OLS estimator. ✓

#### BLUE Summary
OLS β̂₂ is **B**est (minimum variance) **L**inear **U**nbiased **E**stimator.
- **Linear**: β̂₂ = Σcᵢyᵢ where cᵢ = xᵢ/Σxᵢ²
- **Unbiased**: E(β̂₂) = β₂
- **Minimum Variance**: among all linear unbiased estimators

**Important caveat:** Gauss-Markov holds only when all CLRM assumptions are satisfied. No assumption about the distribution of uᵢ is made — normality is NOT required for BLUE. Violation of homoscedasticity makes OLS no longer BLUE.

### Definitions
- **Unbiased estimator**: E(β̂) = β; the expected value equals the true parameter. ⭐ (exam-important)
- **Efficient estimator**: Minimum variance in its class of estimators.
- **Consistent estimator**: As n → ∞, the estimator converges in probability to the true parameter.
- **BLUE**: Best Linear Unbiased Estimator — OLS is BLUE under CLRM. ⭐ (exam-important)
- **Gauss-Markov Theorem**: "Given CLRM assumptions, OLS estimators have minimum variance in the class of all linear unbiased estimators." ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Requiring normality for Gauss-Markov → ✅ Correct: Gauss-Markov does NOT require normality of errors.
- ❌ Mistake: OLS is always best → ✅ Correct: BLUE only if all 5 CLRM assumptions hold; violated homoscedasticity breaks this.

> **Quick Recall:**
> - Algebraic: passes through (X̄, Ȳ); Ȳ̂ = Ȳ; ΣûᵢXᵢ = 0; Σûᵢ = 0
> - Statistical: Unbiased [E(β̂₂) = β₂], Consistent, Efficient (BLUE)
> - Gauss-Markov: OLS is BLUE under CLRM (no normality needed)
> - Statistical properties hold regardless of sample size

### Connections
- Builds on: Classical Assumptions (Chunk 001)
- Extended to matrix form: Chunk 006 (Gauss-Markov for multiple regression)

---

## Section: Goodness of Fit — Coefficient of Determination (r²) 🔴

### Core Idea
r² measures the **proportion of total variation in Y that is explained by the regression**. It is computed by decomposing total variation (TSS) into explained variation (ESS) and unexplained variation (RSS). r² ranges from 0 to 1; higher is better.

> **In Simple Terms:** r² tells you what percentage of Y's ups and downs can be "blamed on" X. If r² = 0.80, then 80% of Y's variation is explained by X.

### Key Concepts

#### TSS, ESS, RSS Decomposition
From yᵢ = ŷᵢ + ûᵢ (deviation form):

Σyᵢ² = Σŷᵢ² + Σûᵢ²   [cross term Σŷᵢûᵢ = 0 by algebraic property]

**TSS = ESS + RSS** ... (4.65)

| Component | Formula | Meaning |
|-----------|---------|---------|
| TSS (Total SS) | Σ(Yᵢ − Ȳ)² | Total variation of Y around its mean |
| ESS (Explained SS) | Σ(Ŷᵢ − Ȳ)² = β̂₂²·Σxᵢ² | Variation explained by regression |
| RSS (Residual SS) | Σûᵢ² | Unexplained variation |

#### r² Definition and Interpretation
**r² = ESS/TSS = 1 − RSS/TSS** ... (4.68, 4.69)

Also: r² = (Σxᵢyᵢ)² / (Σxᵢ²·Σyᵢ²) ... (4.72)

And: r² = β̂₂²·(Sx²/Sy²) ... (4.71) where Sx², Sy² are sample variances.

Properties:
- 0 ≤ r² ≤ 1 always
- r² = 1 → perfect fit (all points on regression line)
- r² = 0 → no linear relationship between Y and X

### Definitions
- **TSS (Total Sum of Squares)**: Σ(Yᵢ − Ȳ)² — total variation in Y around its mean. ⭐ (exam-important)
- **ESS (Explained Sum of Squares)**: Σ(Ŷᵢ − Ȳ)² — variation explained by the regression model.
- **RSS (Residual Sum of Squares)**: Σûᵢ² — unexplained variation; minimized by OLS. ⭐ (exam-important)
- **Coefficient of Determination r²**: r² = ESS/TSS; proportion of total variation in Y explained by X. ⭐ (exam-important)

> **Quick Recall:**
> - TSS = ESS + RSS
> - r² = ESS/TSS = 1 − RSS/TSS ∈ [0, 1]
> - Higher r² → better fit
> - Note: r² for bivariate; R² for multiple regression

### Connections
- Builds on: OLS Algebraic Properties (this chunk) — uses Σŷᵢûᵢ = 0
- Extended to: Adjusted R² for multiple regression (Chunk 007)
- Used in: F-test (Chunk 007)

---

## Section: Hypothesis Testing — t-Test for Regression Coefficients 🔴

### Core Idea
Hypothesis testing examines whether a sample-estimated β̂₂ is consistent with a hypothesized value β₂*. Under normality and the CLRM, the test statistic t = (β̂₂ − β₂*)/se(β̂₂) follows a **t-distribution with (n−2) df**. Rejection occurs when |t| exceeds the critical value (two-tailed) or t exceeds the critical value (one-tailed).

> **In Simple Terms:** We're asking "Is our estimate far enough from what we expected that we should reject our initial guess?" The t-statistic tells us how many standard errors away our estimate is.

### Key Concepts

#### t-Statistic for β̂₂
**t = (β̂₂ − β₂*) / se(β̂₂)** ... (4.73)

Follows t(n−2) distribution under H₀: β₂ = β₂*.

Large |t| → large discrepancy between β̂₂ and β₂* → reject H₀.

If β̂₂ = β₂*, then t = 0. As the difference increases, |t| increases.

#### Two-Tailed Test
- H₀: β₂ = β₂* vs H₁: β₂ ≠ β₂*
- Reject H₀ if |t| > t(α/2, n−2)

95% confidence interval: β₂* ± t(α/2)·se(β̂₂) ... (4.75)

**Example 4.1:** H₀: β₂ = 0.3; β̂₂ = 0.5091, se(β̂₂) = 0.0357, df = 8, α = 5%
- t(α/2) = 2.306 → CI = [0.2177, 0.3823]
- Since β̂₂ = 0.5091 falls outside CI → **Reject H₀**
- Verified: t = (0.5091 − 0.3)/0.0357 = 5.86 > 2.306 ✓

#### One-Tailed Test
- H₀: β₂ ≤ β₂* vs H₁: β₂ > β₂* → right-tail test
- H₀: β₂ ≥ β₂* vs H₁: β₂ < β₂* → left-tail test
- Critical value at 5%: t(α, n−2) = t₀.₀₅; one tail only

**Table 4.1 Decision Rules:**

| Type | H₀ | H₁ | Reject H₀ if |
|------|----|----|-------------|
| Two-tail | β₂ = β₂* | β₂ ≠ β₂* | \|t\| > t(α/2, df) |
| Right-tail | β₂ ≤ β₂* | β₂ > β₂* | t > t(α, df) |
| Left-tail | β₂ ≥ β₂* | β₂ < β₂* | t < −t(α, df) |

### Definitions
- **Level of significance (α)**: Probability of rejecting H₀ when it is true (Type I error); typically 0.05 or 0.01. ⭐ (exam-important)
- **Critical region**: The region of t-values for which H₀ is rejected; defined by critical values t(α/2) or t(α).
- **Degrees of freedom (df)**: For simple regression: n−2.

### ⚠️ Common Mistakes
- ❌ Mistake: Using two-tailed critical values for a one-tailed test → ✅ Correct: One-tailed at 5% uses t₀.₀₅ (not t₀.₀₂₅).
- ❌ Mistake: Rejecting H₀ when |t| < critical value → ✅ Correct: Reject only when |t| > critical value.

> **Quick Recall:**
> - t = (β̂₂ − β₂*)/se(β̂₂) ~ t(n−2)
> - Two-tailed: reject if |t| > t(α/2, df)
> - 95% CI: β̂₂ ± t(α/2)·se(β̂₂)
> - Larger |t| → stronger evidence against H₀

### Connections
- Builds on: Standard Error of OLS Estimators (this chunk)
- Extended to: t-test for multiple regression (Chunk 007)

---

## Section: Forecasting — Mean and Individual 🔴

### Core Idea
Regression can be used to **predict Y values** for a given X₀. Two types of forecasts: (1) **mean forecasting** — predicting E(Y|X₀), the conditional mean; and (2) **individual forecasting** — predicting a specific individual Y₀. The individual forecast has greater uncertainty, producing a **wider confidence band**.

> **In Simple Terms:** Mean forecasting asks "What will the average response be?" while individual forecasting asks "What will this specific observation be?" Individual prediction is always less certain than average prediction.

### Key Concepts

#### Mean Forecasting: E(Y|X₀)
Point estimate: **Ŷ₀ = β̂₁ + β̂₂X₀** ... (4.77)

Variance of Ŷ₀:
**var(Ŷ₀) = σ² · [1/n + (X₀ − X̄)²/Σxᵢ²]** ... (4.78)

95% CI: β̂₁ + β̂₂X₀ ± t(α/2)·se(Ŷ₀) ... (4.79)

Variance is **smallest when X₀ = X̄** and increases as X₀ moves away from X̄.

#### Individual Forecasting: Y₀
Variance of (Y₀ − Ŷ₀):
**var(Y₀ − Ŷ₀) = σ² · [1 + 1/n + (X₀ − X̄)²/Σxᵢ²]** ... (4.80)

Note the extra "1" compared to mean forecast variance — this accounts for the random error in the specific individual observation.

#### Width of Confidence Band
| Forecast Type | Variance Formula | Band Width |
|---------------|-----------------|------------|
| Mean forecast | σ²[1/n + (X₀−X̄)²/Σxᵢ²] | Narrower |
| Individual forecast | σ²[1 + 1/n + (X₀−X̄)²/Σxᵢ²] | Wider |

Both bands widen as X₀ moves away from X̄. The predictive capacity decreases as X₀ moves farther from X̄ — **caution needed in extrapolation**.

### Definitions
- **Mean forecasting**: Predicting the conditional mean E(Y|X₀); point on the regression line. ⭐ (exam-important)
- **Individual forecasting**: Predicting a specific Y₀ for given X₀; higher variance than mean forecast.
- **Forecast error variance**: var(Y₀ − Ŷ₀) = σ²[1 + 1/n + (X₀ − X̄)²/Σxᵢ²].

### ⚠️ Common Mistakes
- ❌ Mistake: Using mean forecast formula for individual prediction → ✅ Correct: Individual forecast has extra σ² term (the "+1").
- ❌ Mistake: Treating all X₀ values as equally reliable → ✅ Correct: Prediction accuracy decreases as X₀ departs from X̄.

> **Quick Recall:**
> - Mean forecast CI < Individual forecast CI (always)
> - Both CIs widen as X₀ moves from X̄
> - Caution in extrapolation beyond observed X range
> - Unit 4 summary: OLS, MOM, MLE → same β̂; Classical properties; r²; t-test; forecasting

### Connections
- Builds on: OLS estimation (Chunk 001), Standard errors (this chunk)
- This completes Unit 4

### Open Questions
1. CYP 3 Q1: Compute r² from wage-schooling data (CYP 1 Q2)
2. CYP 3 Q2: Test H₀: β₂ = 0 using computed r²
3. CYP 3 Q3: Why does predictive capacity decrease as X₀ moves from X̄?
