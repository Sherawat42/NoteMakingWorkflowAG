# Chunk 007 — Evaluation of Multiple Regression: R², Adjusted R², t-Test, F-Test & Linear Restrictions
<!-- Pages: 59–68 -->
<!-- Source: chunk_007.txt -->

## Section: Goodness of Fit in Multiple Regression — R² & Adjusted R² 🔴

### Core Idea
In multiple regression, R² = ESS/TSS still measures the proportion of variation in Y explained by the model. However, **R² always increases when variables are added** — even irrelevant ones. **Adjusted R² (R̄²)** corrects for degrees of freedom, penalizing the addition of weak variables. R̄² is the preferred measure of goodness of fit.

> **In Simple Terms:** R² is like a student's score that only goes up — even adding random subjects inflates it. Adjusted R² is the "fair" score that also accounts for how many subjects you added.

### Key Concepts

#### R² = ESS/TSS in Multiple Regression
From (Yᵢ − Ȳ) = (Yᵢ − Ŷᵢ) + (Ŷᵢ − Ȳ):

**TSS = RSS + ESS** ... (7.2)

**R² = ESS/TSS = Σ(Ŷᵢ − Ȳ)²/Σ(Yᵢ − Ȳ)²** ... (7.3)

Alternatively: **R² = 1 − RSS/TSS** ... (7.4) → as RSS decreases, R² increases.

Range: 0 ≤ R² ≤ 1

**Important caveat:** R² comparisons are valid only when the **dependent variable is the same** in both models. Cannot compare R² across models with different Y.

#### Problem: Over-Fitting (R² Always Increases)
Adding a new explanatory variable:
- **R² ALWAYS increases** (even if the variable is irrelevant)
- This incentivizes researchers to keep adding variables — which is statistically unsound
- Models with many variables lose interpretability and degrees of freedom

#### Adjusted R² (R̄²) Formula and Properties
**Degrees of freedom:** TSS: (n−1), ESS: 1, RSS: (n−k)

**R̄² = 1 − RSS/(n−k) / TSS/(n−1)** ... (7.5)

Or equivalently: **R̄² = 1 − (1 − R²)·(n−1)/(n−k)** ... (7.6)

As n → ∞: R̄² → R² (correction becomes negligible).

**Example 7.1:** Y = α + β₁X₁ + β₂X₂ + u; n = 5, k = 3
- ESS = 1383.16, TSS = 1480.00
- R² = 1383.16/1480.00 = **0.93**
- R̄² = 1 − (1 − 0.93)·(5−1)/(5−3) = 1 − 0.07·2 = **0.86**

#### Four Properties of Adjusted R² (R̄²)
| Property | R² | R̄² |
|----------|----|----|
| When variables added | Always increases | May rise or fall |
| Incentive to over-fit | Yes | No (penalizes weak variables) |
| Relationship | — | R̄² ≤ R² always |
| Can be negative? | No (always ≥ 0) | Yes (can be negative) |

R̄² is a **more desirable** goodness of fit measure than R² in multiple regression.

### Definitions
- **R² (coefficient of determination)**: ESS/TSS; proportion of variation in Y explained by all regressors jointly. ⭐ (exam-important)
- **Adjusted R² (R̄²)**: R̄² = 1 − (1 − R²)·(n−1)/(n−k); penalizes for adding extra regressors; preferred over R². ⭐ (exam-important)
- **TSS, ESS, RSS**: Total, Explained, Residual Sums of Squares — TSS = ESS + RSS.

### ⚠️ Common Mistakes
- ❌ Mistake: Higher R² always means better model → ✅ Correct: Adding irrelevant variables inflates R²; use R̄² to compare.
- ❌ Mistake: R̄² is always between 0 and 1 → ✅ Correct: R̄² can be **negative** (unusual but possible).
- ❌ Mistake: Comparing R² across models with different Y → ✅ Correct: R² comparison requires **same dependent variable**.

> **Quick Recall:**
> - R² = ESS/TSS = 1 − RSS/TSS ∈ [0,1]
> - R̄² = 1 − (1−R²)·(n−1)/(n−k) ≤ R²
> - R̄² may be negative; R² never is
> - R² always ↑ with more variables; R̄² may ↓
> - CYP 1 Q4: R² increases even with useless variables; R̄² is the solution

### Connections
- Extends: r² in bivariate regression (Chunk 002)
- Used in: F-test formulas (this chunk)
- Related to: F-test via R² formula (equation 7.19)

---

## Section: Hypothesis Testing — t-Test for Individual Coefficients 🔴

### Core Idea
To test whether an individual coefficient βₖ is statistically significant, use the **t-statistic**: tₖ = bₖ/se(bₖ). Under H₀: βₖ = 0, this follows a t-distribution with (n−k) degrees of freedom. At 5% significance for large samples: reject H₀ if |tₖ| > 1.96 (two-tailed) or |tₖ| > 1.64 (one-tailed).

> **In Simple Terms:** The t-test answers: "Is this coefficient significantly different from zero?" If |t| is large enough, we conclude the variable meaningfully contributes to explaining Y.

### Key Concepts

#### t-Statistic for βₖ (General)
Under normality: **z = (bₖ − βₖ) / σ√cₖₖ** ... (7.7) follows standard normal

where cₖₖ = k-th diagonal element of (X'X)⁻¹ (standard error numerics from var(β̂) = σ²(X'X)⁻¹).

Replacing σ with estimated s: **tₖ = (bₖ − βₖ⁰) / se(bₖ)** ... (7.9)

→ follows t(n−k) distribution (ratio of standard normal to √chi-squared/df).

#### Two-Tailed Test (Most Common): H₀: βₖ = 0
**tₖ = bₖ / se(bₖ)** ... (7.10)

Reject H₀ if |tₖ| > t(n−k; α/2)

At 5%: |tₖ| > **1.96** for large samples.

Rejection means: bₖ differs significantly from 0 → Xₖ has significant impact on Y.

#### One-Tailed Test: H₀: βₖ ≤ βₖ⁰, H₁: βₖ > βₖ⁰
Reject H₀ if tₖ > t(n−k; α)

At 5%: tₖ > **1.64** for large samples.

#### t-Ratio in Software Output
Statistical software reports: **t-ratio = bₖ / se(bₖ)** — this tests H₀: βₖ = 0.

### Definitions
- **t-ratio**: bₖ/se(bₖ); t statistic testing H₀: βₖ = 0; follows t(n−k). ⭐ (exam-important)
- **One-tailed test**: Tests directional hypothesis (> or <); critical value at full α level.
- **Two-tailed test**: Tests non-directional hypothesis (≠); critical value at α/2 level.

### ⚠️ Common Mistakes
- ❌ Mistake: Two-tailed 5% critical value is 1.64 → ✅ Correct: 1.64 is for one-tailed; 1.96 is for two-tailed at 5%.
- ❌ Mistake: Degrees of freedom for t-test = n−2 → ✅ Correct: For multiple regression with k parameters, df = n−k.

> **Quick Recall:**
> - tₖ = bₖ/se(bₖ) ~ t(n−k) under H₀: βₖ = 0
> - Two-tailed: reject if |tₖ| > 1.96 (large n, 5%)
> - One-tailed: reject if tₖ > 1.64 (large n, 5%)
> - Large |t| → bₖ significant → Xₖ matters for Y

### Connections
- Extends: bivariate t-test (Chunk 002)
- se(bₖ) comes from: diagonal of var(β̂) = σ²(X'X)⁻¹ (Chunk 006)

---

## Section: Confidence Interval for βₖ 🔴

### Core Idea
A **confidence interval** for βₖ contains all values for which the t-test would not reject H₀. It provides a range of plausible values for the true βₖ. At 95% confidence, the CI is bₖ ± 1.96·se(bₖ) for large samples.

> **In Simple Terms:** The confidence interval says: "In 95 out of 100 samples, this interval would capture the true βₖ." It's a range, not a single guess.

### Key Concepts

#### Confidence Interval from t-Distribution
From t-test inversion: for (1−α) confidence level:
**bₖ − t(n−k; α/2)·se(bₖ) < βₖ < bₖ + t(n−k; α/2)·se(bₖ)** ... (7.12)

#### Standard Normal Approximation (Large n)
**95% CI: bₖ ± 1.96·se(bₖ)** ... (7.13)

Interpretation: In repeated sampling, 95% of such intervals contain the true βₖ.

### Definitions
- **Confidence interval**: Range of βₖ values for which t-test does not reject H₀: βₖ = βₖ⁰; provides plausible values for true βₖ. ⭐ (exam-important)

> **Quick Recall:**
> - 95% CI: bₖ ± 1.96·se(bₖ) [large n]
> - CI inversion: all βₖ⁰ where |tₖ| ≤ 1.96
> - Wider CI → larger se → less precise estimate

### Connections
- Extends: bivariate CI (Chunk 002)

---

## Section: F-Test — Joint Significance of Regression Coefficients 🔴
<!-- Continues into: Chunk 008 (linear restrictions) -->

### Core Idea
The **F-test** tests whether **multiple coefficients are jointly zero** — i.e., whether J regressors together contribute meaningfully to the model. It compares the RSS of the full (unrestricted) model with the RSS of the restricted model (J regressors omitted). F ~ F(J, n−k).

> **In Simple Terms:** The t-test asks "does *this one* variable matter?" The F-test asks "do *these J* variables matter as a group?" — requiring a different, larger test.

### Key Concepts

#### F-Test: Full vs Restricted Model
**H₀:** βₖ₋ⱼ₊₁ = … = βₖ = 0 (last J coefficients are zero) ... (7.14)
**H₁:** At least one of these coefficients ≠ 0

Compare:
- **RSS₁**: RSS of full (unrestricted) model
- **RSS₀**: RSS of restricted model (J regressors dropped)

Under H₀: (RSS₀ − RSS₁) ~ χ²(J)·σ²

#### F-Statistic Formula (RSS form)
**F = [(RSS₀ − RSS₁)/J] / [RSS₁/(n−k)]** ... (7.16)

F ~ F(J, n−k) — F-distribution with J and (n−k) degrees of freedom.

Reject H₀ if F > F(J, n−k; α).

#### F-Statistic Formula (R² form)
**F = [(R₁² − R₀²)/J] / [(1 − R₁²)/(n−k)]** ... (7.17)

where R₁² = R² of unrestricted, R₀² = R² of restricted model.

#### Special Case: All Slope Coefficients = 0
H₀: β₂ = β₃ = … = βₖ = 0 (intercept is the only regressor in restricted model)

**F = [RSS₀ − RSS₁]/(k−1) / [RSS₁/(n−k)]** ... (7.18)

**In R² form: F = [R²/(k−1)] / [(1−R²)/(n−k)]** ... (7.19)

**Interpretation:** If F fails to reject H₀ → model performs poorly. If F rejects H₀ → not sufficient to conclude model is good; just means at least one variable matters.

### Definitions
- **F-test**: Joint significance test for J restrictions on β; uses F-distribution. ⭐ (exam-important)
- **Restricted model**: Model with J regressors removed (all set to zero) — tested under H₀.
- **Unrestricted model**: Full model with all k regressors.
- **F-distribution**: F ~ F(J, n−k); critical values one-sided even though H₁ is two-sided.

### ⚠️ Common Mistakes
- ❌ Mistake: F-test rejects H₀ → model is definitely good → ✅ Correct: Rejection only means ≥1 variable is significant; doesn't validate the overall model.
- ❌ Mistake: F-distribution is two-sided → ✅ Correct: F critical values are **one-sided** (always reject for large F).

> **Quick Recall:**
> - F tests J coefficients jointly (t tests one at a time)
> - F = [(RSS₀−RSS₁)/J] / [RSS₁/(n−k)] ~ F(J, n−k)
> - F in R²: [(R₁²−R₀²)/J] / [(1−R₁²)/(n−k)]
> - Special case all slopes = 0: F = [R²/(k−1)] / [(1−R²)/(n−k)]
> - Large F → reject H₀ → at least one regressor significant

### Connections
- Uses: RSS and R² from goodness of fit (this chunk)
- Compared with: t-test (single restriction) vs F-test (multiple restrictions)
- Extends to: Wald/LM/LR tests for restrictions (Chunk 008)

---

## Section: Testing Linear Restrictions on Multiple Parameters 🔴
<!-- Continues into: Chunk 008 — Wald, LM, LR Tests -->

### Core Idea
The t-test restricts only **one parameter** at a time. In practice, economic hypotheses may impose **linear restrictions on multiple coefficients simultaneously** — for example, the Cobb-Douglas production function's constant returns to scale implies β₂ + β₃ + … + βₖ = 1. Such restrictions require special tests: Wald, LM, or LR.

> **In Simple Terms:** Sometimes theory says "the sum of these two slopes must equal 1" — neither a simple t-test nor F-test directly handles this. We need more general tools.

### Key Concepts

#### General Linear Restriction: Rβ = q
Restriction in matrix form: **Rβ = q** ... (7.20)

where R is a (J×k) matrix of restriction coefficients, q is a (J×1) vector of constants.
J = number of restrictions (linear equations); J < k.

#### Cobb-Douglas Example: Constant Returns to Scale
Log-linear Cobb-Douglas: ln Y = β₁ + β₂ ln K + β₃ ln L + u

Constant returns to scale: **β₂ + β₃ = 1**

This is one linear restriction on two parameters → cannot be tested by a single t-test.

### Definitions
- **Linear restriction**: A constraint of the form Rβ = q imposed on regression parameters; more general than single-parameter restrictions.

> **Quick Recall:**
> - t-test: tests βₖ = 0 (one restriction at a time)
> - Linear restrictions: Rβ = q (multiple coefficients constrained)
> - Cobb-Douglas constant returns: β₂ + β₃ = 1
> - Three test methods: Wald, LM, LR → Chunk 008

### Connections
- Continues into: Chunk 008 (Wald, LM, LR Test derivations)
- CYP 3 Q1: Describes the need for testing beyond single parameters
