# Chunk 005 — Multivariable Regression Models (Introduction)
<!-- Pages: 36-45 -->
<!-- Source: chunk_005.txt -->

---

## Section: Introduction to Multivariable Regression Models 🔴

### Core Idea

Unit 10 extends the simple two-variable regression model to include **multiple explanatory variables**. This makes the model more realistic since most economic outcomes depend on more than one factor. The multiple regression model Y = β₀ + β₁X₁ + β₂X₂ + … + βₙXₙ + μ estimates the **partial effect** of each variable on Y while holding others constant.

> **In Simple Terms:** Instead of saying "consumption depends only on income," we now say "consumption depends on income AND wealth AND interest rates AND age." Each variable gets its own slope coefficient (partial regression coefficient) while the others are held fixed.

### Key Concepts

#### Regression Model with Two Explanatory Variables

The model:
- **Non-stochastic form**: E(Yₜ) = β₀ + β₁X₁ₜ + β₂X₂ₜ
- **Stochastic form**: Yₜ = β₀ + β₁X₁ₜ + β₂X₂ₜ + μₜ

Where:
- (β₀ + β₁X₁ + β₂X₂) = **systematic/deterministic component** = E(Y) point on the regression plane
- μₜ = **random component** — determined by factors other than X₁ and X₂

The model is **linear in parameters** (β₀, β₁, β₂ each have power 1).

**Sample Regression Function:**
Ŷₜ = b₀ + b₁X₁ₜ + b₂X₂ₜ + eₜ

Where b₀, b₁, b₂ are estimators for β₀, β₁, β₂ and eₜ is the sample error term.

#### OLS Estimation with Two Explanatory Variables

**Objective**: Minimize RSS = Σeₜ² = Σ(Yₜ − b₀ − b₁X₁ₜ − b₂X₂ₜ)²

This gives **three normal equations** (derived by partial differentiation and setting to zero):
1. ΣY = nb₀ + b₁ΣX₁ + b₂ΣX₂
2. ΣYX₁ = b₀ΣX₁ + b₁ΣX₁² + b₂ΣX₁X₂
3. ΣYX₂ = b₀ΣX₂ + b₁ΣX₁X₂ + b₂ΣX₂²

**Solution formulas:**
- b₀ = Ȳ − b₁X̄₁ − b₂X̄₂
- b₁ = (Σx₁²·Σyx₂ − Σx₁x₂·Σyx₁) / (Σx₁²·Σx₂² − (Σx₁x₂)²)
- b₂ = (Σx₂²·Σyx₁ − Σx₁x₂·Σyx₂) / (Σx₁²·Σx₂² − (Σx₁x₂)²)
(lowercase = deviations from means)

#### Degrees of Freedom in Multiple Regression

In a model estimating k parameters from n observations:
- **Degrees of freedom = n − k**
- For two-variable model (k=3: b₀, b₁, b₂): **df = n − 3**
- Unbiased estimator of σ²: **σ̂² = Σeₜ² / (n − 3)**

#### Interpretation of Partial Regression Coefficients

- **b₁** = rate of change in Y per unit change in X₁, **holding X₂ constant** (ceteris paribus)
- **b₂** = rate of change in Y per unit change in X₂, **holding X₁ constant** (ceteris paribus)

This is the **"other things equal"** interpretation — analogous to the law of demand (quantity demanded varies with price, ceteris paribus).

### Definitions

- **Multiple Regression**: Regression of one dependent variable on **more than one** independent/explanatory variable. ⭐ (exam-important)
- **Partial Regression Coefficient**: The coefficient of an individual predictor in multiple regression — measures the effect of that variable holding all other variables constant. ⭐ (exam-important)
- **Degrees of Freedom (DF)**: n − k, where k = number of parameters estimated. In two-variable multiple regression (3 parameters): df = n − 3.

### Mechanisms / Processes

**OLS in Two-Variable Model:**
1. Set up SRF: Yₜ = b₀ + b₁X₁ₜ + b₂X₂ₜ + eₜ
2. Minimize Σeₜ² by partial differentiation w.r.t. b₀, b₁, b₂
3. Solve the three normal equations simultaneously → get b₀, b₁, b₂
4. Compute σ̂² = Σeₜ²/(n−3)
5. Compute standard errors: se(b₁), se(b₂), se(b₀)

### ⚠️ Common Mistakes

- ❌ Mistake: Interpreting b₁ as the total effect of X₁ on Y → ✅ Correct: b₁ is the **partial** effect (holding X₂ constant); the total effect includes indirect effects through X₂
- ❌ Mistake: Using df = n−2 in multiple regression → ✅ Correct: df = n−k; with 3 parameters, df = n−3

> **Quick Recall:**
> - Multiple regression: Y = β₀ + β₁X₁ + β₂X₂ + μ
> - Each coefficient = partial effect (other things equal)
> - OLS minimizes Σeₜ²; 3 normal equations for 2-variable model
> - df = n−k (k = number of parameters)
> - σ̂² = Σeₜ²/(n−3) for two-variable regression

---

## Section: Multiple Coefficient of Determination (R²) and ANOVA 🔴

### Core Idea

The R² in multiple regression measures the proportion of total variation in Y explained jointly by all explanatory variables. However, because R² increases automatically as we add more variables, we need the **adjusted R²** (R̄²) to compare models with different numbers of variables. The F-test (ANOVA) provides an overall significance test for the model.

> **In Simple Terms:** R² is like a grade — it always improves when you add more features. Adjusted R² is the "penalized grade" that discourages cheating by adding useless variables. F-test asks the big question: "Do ANY of the variables matter at all?"

### Key Concepts

#### Multiple R² (Coefficient of Multiple Determination)

**R² = ESS / TSS** (same formula as simple regression)

Where:
- ESS = b₁Σyx₁ + b₂Σyx₂ (explained sum of squares)
- TSS = Σy² (total sum of squares)
- RSS = Σy² − b₁Σyx₁ − b₂Σyx₂ (residual sum of squares)
- R² = ESS/TSS = 1 − RSS/TSS; ∈ [0,1]

**Problem with R²**: Adding any new variable (even a random, useless one) can only increase or maintain R² — it never decreases. This creates incentive to overfit with many variables.

#### Adjusted R² (R̄²)

**R̄² = 1 − (1−R²)(n−1)/(n−k)** ⭐ (exam-important)

- Penalizes for additional variables (through the denominator n−k)
- Can **decrease** if added variable doesn't improve fit enough
- **Rule**: Include a new variable only if adding it **increases R̄²**
- Practical guide: Keep the variable if its |t-value| > 1

| Feature | R² | Adjusted R² (R̄²) |
|---------|----|--------------------|
| Range | [0, 1] | Can be negative |
| Adding variables | Always ↑ or stays same | Can go up or down |
| Purpose | Goodness of fit | Model comparison |
| Penalizes df? | No | Yes |

#### ANOVA Table for Multiple Regression

Degrees of freedom structure in two-explanatory-variable regression:

| Source | Sum of Squares | df | Mean SS |
|--------|---------------|-----|---------|
| Due to regression (ESS) | b₁Σyx₁ + b₂Σyx₂ | 2 (= k−1) | ESS/2 |
| Due to residuals (RSS) | Σeₜ² | n−3 | RSS/(n−3) |
| Total (TSS) | Σy² | n−1 | — |

**F-test**: Tests H₀: β₁ = β₂ = 0 (all slope coefficients = 0)
- **F = (ESS/df_ESS) / (RSS/df_RSS)** ~ F(k−1, n−k)
- F can also be expressed as: **F = [R²/(k−1)] / [(1−R²)/(n−k)]**
- Large F → reject H₀ → at least one X variable significantly affects Y

### Definitions

- **Adjusted R² (R̄²)**: Coefficient of determination adjusted for degrees of freedom; penalizes adding unnecessary variables. ⭐ (exam-important)
- **F-test (ANOVA)**: Overall significance test for the regression model; tests whether all slope coefficients are simultaneously zero.
- **Analysis of Variance (ANOVA)**: Study of the components of TSS (ESS + RSS) and their degrees of freedom.

### ⚠️ Common Mistakes

- ❌ Mistake: Maximizing R² by adding many variables will always yield a better model → ✅ Correct: Use R̄² to compare models; adding variables that don't add meaningful information hurts model quality
- ❌ Mistake: F-test tests each coefficient individually → ✅ Correct: F-test is a *joint* test that ALL slopes simultaneously equal zero

> **Quick Recall:**
> - **R² always ↑** when variables added → use **R̄²** for comparison
> - R̄² = 1 − (1−R²)(n−1)/(n−k)
> - Include variable if R̄² ↑ (or |t| > 1)
> - ANOVA: F = (ESS/df_ESS) / (RSS/df_RSS) ~ F(k−1, n−k)
> - F captures overall goodness-of-fit significance

### Connections

- Builds on: R² from Unit 9 (Chunk 002)
- Leads to: Econometric problems — multicollinearity, heteroscedasticity, autocorrelation (Chunk 006)

---

## Section: Generalisation to N Explanatory Variables 🔴

### Core Idea

The multiple regression model generalises to **n explanatory variables**: Y = β₀ + β₁X₁ + … + βₙXₙ + μ. In matrix form: **Y = Xβ + U**. The OLS solution is **b = (X'X)⁻¹X'Y**. Three additional assumptions are required beyond the basic classical assumptions: **no multicollinearity, no heteroscedasticity, and no autocorrelation.**

> **In Simple Terms:** Instead of one or two predictors, we can have dozens. Matrix algebra gives us an elegant formula — it's like doing OLS, but all at once for many variables simultaneously.

### Key Concepts

#### Classical Assumptions for General Multiple Regression

In addition to linearity in parameters and non-stochastic X, the general multiple regression model requires:

1. **E(μᵢ) = 0** for all i (zero mean errors)
2. **E(μᵢ²) = σ² for all i** and **E(μᵢμⱼ) = 0 for i≠j** (homoscedasticity + no autocorrelation)
   - In matrix form: E(UU') = σ²I
3. **X is linearly independent** (no exact linear relationship between any X variables → no multicollinearity)
4. **Number of observations > number of parameters** (n > k)

#### Matrix OLS Formula

**OLS solution in matrix notation**: **b = (X'X)⁻¹X'Y**

- Valid only when X'X is invertible (full rank X matrix)
- Requires absence of exact multicollinearity among X variables
- **Variance**: Var(b) = σ²(X'X)⁻¹

### Definitions

- **Multi-co-linearity**: Existence of exact or near-exact linear relationships between explanatory variables, causing X'X to be singular or near-singular. ⭐ (exam-important)
- **The three key violations**: Multicollinearity, heteroscedasticity, autocorrelation — each causes OLS to no longer be BLUE.

### Connections

- Builds on: Two-variable multiple regression (earlier in this chunk)
- Continues in: Chunk 006 — Econometric problems (multicollinearity, heteroscedasticity, autocorrelation, MLE)

### Open Questions

1. How many explanatory variables should a model include? (Partially answered by adjusted R² and t-values)
