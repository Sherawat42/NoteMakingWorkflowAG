# Chunk 002 — Estimation of SRF, Goodness of Fit, and Functional Forms
<!-- Pages: 10-19 -->
<!-- Source: chunk_002.txt -->
<!-- See chunk 001 for the introduction to Sample Regression Function -->

---

## Section: Sample Regression Function 🔴
<!-- See chunk 001 for the beginning of this section -->

### Core Idea

Due to sampling fluctuations, different samples from the same population will yield different values of α̂ and β̂. The key requirement is that **on average**, these estimates must represent the true population parameters. This is the estimation problem — solved using the **Ordinary Least Squares (OLS)** method.

> **In Simple Terms:** Each time you survey different people, you'll get a slightly different regression line. The goal is to pick an estimation method that, on average across many surveys, gives you the right line. OLS achieves this.

---

## Section: Estimation of Sample Regression Function 🔴

### Core Idea

The **Ordinary Least Squares (OLS)** method estimates α̂ and β̂ by minimising the sum of squared residuals: **minimize Σ Û²**. This gives the "best-fitting" regression line through the sample scatter. The resulting estimators are called the **Least Square Estimators**, and under the classical assumptions, they possess the BLUE property (Best Linear Unbiased Estimators).

> **In Simple Terms:** OLS finds the line where the total squared distance between actual data points and the line is as small as possible. It's like pulling a rubber band taut through a cloud of dots to minimize how far the dots are from the band.

### Key Concepts

#### Ordinary Least Squares (OLS) Procedure

**Objective**: Minimize Σ Û² = Σ(Y − α̂ − β̂X)² with respect to α̂ and β̂

**Solving** by partial differentiation gives two **Normal Equations**:
1. ΣY = nα̂ + β̂ΣX
2. ΣXY = α̂ΣX + β̂ΣX²

**Solving these simultaneously gives the OLS formulas:**

- **β̂ = Σxy / Σx²** where x = X − X̄ (deviation from mean), y = Y − Ȳ  
  Also written as: β̂ = [nΣXY − ΣXΣY] / [nΣX² − (ΣX)²]

- **α̂ = Ȳ − β̂X̄** (intercept estimated from the means)

**Key result**: β̂ is a **linear function** of the observed Y values (β̂ = Σkᵢyᵢ, where kᵢ = xᵢ/Σx²). This linearity property is crucial for hypothesis testing.

#### Gauss-Markov Theorem

Under the five classical regression model assumptions, the OLS estimators α̂ and β̂ have three key properties:

| Property | Meaning | Technical Statement |
|---------|---------|---------------------|
| **Linear** | Can be expressed as a linear function of observed Y | α̂ = ΣaᵢYᵢ, β̂ = ΣkᵢYᵢ |
| **Unbiased** | On average, equal to the population parameter | E(α̂) = α, E(β̂) = β |
| **Minimum Variance** | Smallest variance among all linear unbiased estimators | More efficient than any other LUE |

**The Gauss-Markov Theorem** states: *"Under the assumptions of the classical linear regression model, among all linear unbiased estimators, the least square estimators have the minimum variance — i.e., OLS estimators are BLUE (Best Linear Unbiased Estimators)."* ⭐

#### Standard Error of Estimate

Since we cannot directly observe σ (standard deviation of U), we estimate it from the sample:

- **Unbiased estimator of σ²**: σ̂² = Σ Û² / (n−2)
- **n−2** is the degrees of freedom (we lose 2 df because we estimated 2 parameters: α̂ and β̂)
- **Standard Error of Estimate (σ̂)** = √[Σ Û² / (n−2)] — measures how spread out residuals are around the regression line

Standard errors of the OLS estimators:
- **se(β̂)** = σ̂ / √(Σx²)
- **se(α̂)** = σ̂ √(ΣX² / n·Σx²)

These standard errors measure **precision** of the estimates — smaller SE = more reliable estimate.

### Definitions

- **OLS (Ordinary Least Squares)**: Method that estimates regression parameters by minimizing the sum of squared residuals Σ Û². ⭐ (exam-important)
- **BLUE (Best Linear Unbiased Estimator)**: The property of OLS estimators guaranteed by the Gauss-Markov theorem — linear, unbiased, and with minimum variance among all linear unbiased estimators. ⭐ (exam-important)
- **Standard Error of Estimate**: σ̂ = √[Σ Û² / (n−2)] — the standard deviation of residuals around the regression line. ⭐ (exam-important)
- **Degrees of Freedom**: n−2 in simple regression (n observations, 2 parameters estimated: α̂ and β̂).

### Mechanisms / Processes

**OLS Estimation Steps:**
1. Compute means: X̄ = ΣX/n, Ȳ = ΣY/n
2. Compute deviations: x = X − X̄, y = Y − Ȳ
3. Compute β̂ = Σxy / Σx²
4. Compute α̂ = Ȳ − β̂X̄
5. Compute fitted values: Ŷᵢ = α̂ + β̂Xᵢ
6. Compute residuals: Ûᵢ = Yᵢ − Ŷᵢ
7. Compute σ̂² = Σ Û² / (n−2)
8. Compute standard errors of α̂ and β̂

### Examples

**Example 9.1 — Employment vs Labour Force (1991-2000):**

| Variable | Value |
|---------|-------|
| Y = Employed (million) | Range: 100–295 |
| X = Labour Force (million) | Range: 120–320 |
| Sample size (n) | 10 |

**Results:**
- β̂ = 38850 / 40250 = **0.965217** → For every 100 additional persons in labour force, about 97 get employed
- α̂ = 193.5 − (0.965217 × 215) = **−14.0217** → Negative intercept: average effect of omitted variables
- σ̂² = 403.8043 / 8 = **50.475537** (degrees of freedom = 10 − 2 = 8)
- se(β̂) = 0.0354118; se(α̂) = 7.938264
- R² = 37498.67 / 37902.5 = **0.989345** → ~99% of employment variation explained by labour force

**Interpretation:**
- Slope β̂ = 0.965: For 100 more job seekers, ~97 find employment
- Intercept α̂ = −14.02: Average combined effect of all omitted factors (e.g., technology, policy)  
- R² = 0.989: Excellent fit — labour force alone explains 99% of employment variation

### ⚠️ Common Mistakes

- ❌ Mistake: Using n instead of (n−2) in the denominator of σ̂² → ✅ Correct: Must use degrees of freedom (n−2), otherwise σ̂² is biased
- ❌ Mistake: Thinking BLUE means OLS is the best estimator overall → ✅ Correct: BLUE only means best among **linear unbiased** estimators; non-linear estimators could theoretically do better

### Edge Cases & Caveats

- BLUE property holds **only when all 5 classical assumptions are satisfied**
- If assumptions are violated (e.g., heteroscedasticity), OLS is no longer BLUE — see Unit 10

> **Quick Recall:**
> - OLS minimizes Σ Û² → gives β̂ and α̂
> - **Gauss-Markov**: OLS is **BLUE** under classical assumptions
> - Standard error σ̂ = √[Σ Û²/(n−2)] — uses n−2 (degrees of freedom)
> - β̂ = Σxy/Σx² ; α̂ = Ȳ − β̂X̄

### Connections

- Builds on: Classical regression model assumptions (Chunk 001)
- Leads to: Goodness of Fit (next section, same chunk)
- Related to: Heteroscedasticity and autocorrelation violations (Chunk 006)

---

## Section: Goodness of Fit 🔴

### Core Idea

After fitting the regression line, we need a measure of **how well the line fits the data** — how much of the variation in Y is explained by X through the regression. This is the **Coefficient of Determination (R²)**, which ranges from 0 to 1. R² = proportion of total variation in Y explained by the regression.

> **In Simple Terms:** If you draw the best-fit line through a scatter plot, R² tells you what fraction of the dots' "spread" your line accounts for. R² = 1 means the line passes through every dot perfectly. R² = 0 means the line explains nothing.

### Key Concepts

#### Decomposition of Total Variation (TSS = ESS + RSS)

The total variation of Y around its mean can be broken into two parts:

| Component | Formula | Meaning |
|-----------|---------|---------|
| **TSS** (Total Sum of Squares) | Σ(Y − Ȳ)² | Total variation in Y |
| **ESS** (Explained Sum of Squares) | Σ(Ŷ − Ȳ)² | Variation explained by regression |
| **RSS** (Residual Sum of Squares) | Σ(Y − Ŷ)² = Σ Û² | Unexplained variation (residuals) |

And the fundamental identity: **TSS = ESS + RSS**

*(The cross-product term Σ(Ŷ − Ȳ)(Y − Ŷ) = 0, which can be proved using OLS properties.)*

#### Coefficient of Determination (R²)

**R² = ESS/TSS = 1 − RSS/TSS**

- R² = 0: Regression explains nothing (the line is flat/useless)
- R² = 1: Regression explains everything (perfect fit, no residuals)
- 0 ≤ R² ≤ 1 always holds

R² is the square of the **correlation coefficient** between Y and Ŷ (or between Y and X in simple regression).

### Definitions

- **Coefficient of Determination (R²)**: The ratio ESS/TSS; measures the proportion of total variation in Y explained by the regression model. Ranges from 0 to 1. ⭐ (exam-important)
- **TSS (Total Sum of Squares)**: Σ(Y − Ȳ)² — measures total variation of Y around its mean.
- **ESS (Explained Sum of Squares)**: Σ(Ŷ − Ȳ)² — variation of Y accounted for by the regression.
- **RSS (Residual Sum of Squares)**: Σ(Y − Ŷ)² = Σ Û² — unexplained variation.

### Mechanisms / Processes

**Computing R²:**
1. Compute TSS = Σ(Y − Ȳ)²
2. Compute RSS = Σ Û² (from OLS residuals)
3. ESS = TSS − RSS
4. R² = ESS / TSS

### Examples

**From Example 9.1:**
- TSS = Σy² = 37902.5
- RSS = Σ Û² = 403.8043
- ESS = 37902.5 − 403.8043 = 37498.67
- R² = 37498.67 / 37902.5 = **0.989345 ≈ 0.99**
- Interpretation: **99%** of variation in employment is explained by variation in labour force → excellent fit

### ⚠️ Common Mistakes

- ❌ Mistake: High R² always means the model is good → ✅ Correct: R² can be inflated by adding more variables; use adjusted R² to penalize for extra variables (covered in Unit 10)
- ❌ Mistake: R² = 1 is always the goal → ✅ Correct: Perfect R² = 1 means every point lies exactly on the line, which is almost never the case in real data and could indicate overfitting

### Edge Cases & Caveats

- R² can never decrease when adding more explanatory variables — this motivates the **adjusted R²** (R̄²) in multiple regression
- R² is not appropriate if the regression model has no intercept

> **Quick Recall:**
> - **TSS = ESS + RSS** (fundamental identity)
> - **R² = ESS/TSS = 1 − RSS/TSS**
> - R² ∈ [0, 1]: Higher = better fit
> - R² = 0.989 means "regression explains 98.9% of variation in Y"

### Connections

- Builds on: OLS estimation (previous section, same chunk)
- Extended to adjusted R² in: Unit 10 Multivariable Regression (Chunk 005)

---

## Section: Functional Forms of Regression Model 🔴
<!-- This section continues in chunk 003 -->

### Core Idea

While all regression models considered here are **linear in parameter**, they can take different **functional forms** depending on the relationship between X and Y in the real world. The four main forms are: Linear, Log-linear, Semi-log, and Reciprocal models. The choice depends on economic theory and the shape of the data relationship.

> **In Simple Terms:** Just because we always use "linear in parameter" doesn't mean the relationship always looks like a straight line on a graph. We can model curves, accelerating growth, and fixed limits by choosing different functional forms.

### Key Concepts

#### 1. Linear Model

- **Equation**: Y = α + βX + U
- Both linear in variable AND linear in parameter
- **Slope β**: Constant — for every 1-unit increase in X, Y changes by β units
- **Interpretation**: β = dY/dX = constant
- **When to use**: When the effect of X on Y is constant (no acceleration/deceleration)

#### 2. Log-linear Model (Double-Log or Constant Elasticity Model)

- **Equation**: log Y = α + β log X + U
- Linear in parameter (after log transformation), non-linear in original variables
- **Slope β**: Measures **elasticity** — % change in Y for 1% change in X → **β = (dY/Y)/(dX/X)**
- **Key property**: β is the **constant elasticity** → same elasticity at every point on the curve
- **When to use**: When the relationship is proportional (e.g., demand functions)
- Also called: "double-log model" or "constant-elasticity model"

> **Quick Recall:**
> - Linear: β = dY/dX (slope = constant)
> - Log-linear: β = elasticity = % ΔY / % ΔX (constant throughout)
> - Semi-log: slope = % ΔY / absolute ΔX (covered in chunk 003)
> - Reciprocal: Y has an upper or lower limit (covered in chunk 003)

<!-- This section continues in chunk 003 -->

### Connections

- Builds on: Linearity concept (Chunk 001)
- Continues in: Chunk 003 (Semi-log, Reciprocal models, examples)

### Open Questions

1. How do we choose between functional forms in practice?
