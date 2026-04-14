# Chunk 001 — Introduction to Two Variable Regression Models
<!-- Pages: 1-9 -->
<!-- Source: chunk_001.txt -->

---

## Section: Introduction and The Issue of Linearity 🟢

### Core Idea

Regression analysis is the primary statistical tool used to study relationships among economic variables. A **regression model** expresses the dependent variable as a function of one or more explanatory (independent) variables. This unit introduces the **two-variable regression model**, covering its probabilistic nature, estimation of parameters, and the classical assumptions required for valid inference.

> **In Simple Terms:** Think of regression as drawing the "best-fit line" through a scatter plot of data points. If you plot income vs. consumption, regression tells you the equation of that line — so you can predict consumption for any given income level.

### Key Concepts

#### Linearity in Parameter vs Linearity in Variable

The concept of linearity in a regression model can mean two different things, and understanding the distinction is critical:

- **Linear in variable**: Highest power of the *independent variable* is 1 (e.g., Y = α + βX). The graph is a straight line.
- **Linear in parameter**: Highest power of any *parameter* (α, β, γ…) is 1. This is what matters for regression analysis.

For regression purposes, **only linearity in parameter is required**, not linearity in variable. Consider:
- Y = α + βX + γX² → **linear in parameter** (can be estimated by OLS), non-linear in variable
- Y = α + β²X → **non-linear in parameter** (OLS cannot directly estimate this)

Some non-linear-in-parameter models can be transformed (e.g., log transformation) to become estimable by OLS. But intrinsically non-linear models require iterative procedures beyond this unit's scope.

| Feature | Linear in Variable | Linear in Parameter |
|---------|-------------------|---------------------|
| Requirement for OLS | Not required | **Required** |
| Example | Y = α + βX | Y = α + βX + γX² |
| Graph | Straight line | Can be curved |

### Definitions

- **Regression Model**: Formulation of an economic relationship as an equation where the dependent variable is a function of explanatory variables, used for parameter estimation and hypothesis testing. ⭐ (exam-important)
- **Linear in Parameter**: A model where the highest power of any parameter (constant) is 1 — the essential requirement for OLS estimation. ⭐ (exam-important)

### Mechanisms / Processes

**How to check if a model is linear in parameter:**
1. Look at the parameters (constants, not variables) in the equation
2. Check the highest power of each parameter
3. If all powers = 1 → linear in parameter → OLS applicable
4. If any power > 1 → non-linear → try log transformation or other methods

**Log transformation example:**
- Non-linear model: Y = αX^β
- After log: log Y = log α + β log X → now linear in log(α) and β

### Examples

**Example 1 — Linear in both:** Y = α + βX
→ Straight line; linear in variable AND parameter. ✅

**Example 2 — Linear in parameter only:** Y = α + βX + γX²
→ Curved (parabola), but parameters α, β, γ each have power 1. Estimable by OLS. ✅

**Example 3 — Non-linear in parameter:** Y = α + β²X
→ β has power 2. Cannot directly estimate by OLS. ❌

**Example 4 — Transformable:** Y = αX^β → take logs → log Y = log α + β log X ✅

### ⚠️ Common Mistakes

- ❌ Mistake: Assuming a "curved" regression line means it's non-linear and can't be estimated → ✅ Correct: Linearity in *parameter* (not variable) is what OLS requires; polynomial curves are fine.
- ❌ Mistake: Confusing intercept (α) with disturbance term (U) → ✅ Correct: α captures known systematic effects; U captures random/unknown effects.

### Edge Cases & Caveats

- Some regressions are "intrinsically non-linear in parameter" — no transformation makes them linear. These require special iterative methods not covered here.
- Log transformation is only valid when all values are positive (log of zero/negative is undefined).

> **Quick Recall:**
> - OLS requires linearity in **parameter**, not necessarily in variable
> - Y = α + βX² is OK for OLS (linear in α, β)
> - Y = α + β²X is NOT OK for OLS directly
> - Log transformation can linearize some non-linear models

### Connections

- Builds on: Unit 8 (Least Squares method, referenced in source text)
- Leads to: Population Regression Function (next section, same chunk)

### Open Questions

1. What are the iterative procedures used for intrinsically non-linear regression models?

---

## Section: The Non-deterministic Nature of Regression Model 🟡

### Core Idea

In social sciences, relationships between variables are never exactly deterministic. There is always random variation — for a given income level X, different people will have different consumption levels Y. The regression model accounts for this by incorporating a **random/stochastic component**. The dependent variable Y is probabilistic in nature; for each value of X, there is a *distribution* of Y values.

> **In Simple Terms:** If you give 100 families the same income, they won't all spend exactly the same amount. Some spend more, some less. The random variable U captures this variation — the "noise" around the average relationship.

### Key Concepts

#### Stochastic vs Non-stochastic Variables

In the classical two-variable regression model:
- **Dependent variable (Y)**: **Stochastic** (random) — its value cannot be predicted exactly; it has a probability distribution for each X
- **Independent variable (X)**: **Non-stochastic** (fixed/deterministic) — treated as fixed in repeated sampling

This asymmetry is a simplification. In advanced treatments, even X is considered stochastic, but at this level, X is treated as fixed.

### Definitions

- **Stochastic Variable**: A variable whose value is determined by a probability distribution, not by a fixed rule. The dependent variable Y in regression is stochastic. ⭐ (exam-important)

### Mechanisms / Processes

The probabilistic nature is captured by recognizing that:
- For each fixed value of X, Y forms a **conditional distribution**
- The regression model estimates the **conditional mean** of Y given X: E(Y|X)
- Actual Y values scatter around this mean — captured by the disturbance term U

### Edge Cases & Caveats

- At an advanced level, even X can be treated as stochastic (e.g., in simultaneous equations models)
- The probabilistic nature of Y is what makes statistical inference (confidence intervals, hypothesis tests) meaningful

> **Quick Recall:**
> - Y is stochastic; X is non-stochastic in classical regression
> - For each X, there's a distribution of Y values
> - Regression estimates the **mean** of Y for given X

### Connections

- Directly leads to: Population Regression Function (next section)
- Related to: Classical assumptions about U (this chunk)

---

## Section: Population Regression Function 🔴

### Core Idea

The **Population Regression Function (PRF)** is the true, unknown relationship between X and Y in the entire population: **Y = α + βX + U**. The parameters α and β are unknown constants to be estimated. The disturbance term U is a random variable that captures all the randomness in the relationship. The PRF is never directly observable — we can only work with a sample.

> **In Simple Terms:** Imagine that the true law of nature says "for every ₹1 rise in income, consumption rises by exactly ₹0.80." That's the PRF — the real underlying truth. We can't see it directly; we have to estimate it from survey data.

### Key Concepts

#### The Disturbance Term (U)

The disturbance term U is a critical component of the regression model. It represents the net effect of all factors not explicitly included in the model:

| Source of U | Description |
|-------------|-------------|
| Inherent randomness in human behaviour | Unpredictable human decisions even with same X |
| Omitted variables | Known factors deliberately left out for parsimony |
| Measurement error | Errors in measuring Y accurately |
| Model misspecification | Wrong functional form chosen for the model |

**Key property**: The net/mean effect of U is assumed to be zero: **E(U) = 0**. This is because positive and negative random effects tend to cancel out.

#### Disturbance Term vs Intercept (α)

These two are often confused but serve different purposes:

| Feature | Disturbance Term (U) | Intercept (α) |
|---------|---------------------|---------------|
| Nature | Random, stochastic | Fixed constant |
| Represents | Unknown, random factors | Known, systematic factors not explicitly included |
| Mean | E(U) = 0 | Non-zero in general |
| Example | Random mood effects on spending | Average effect of all omitted income-categories |

#### Population Regression Line

Applying expectation to Y = α + βX + U:
- **E(Y|X) = α + βX** (since E(U) = 0)
- This is the **Population Regression Line** — gives the average/conditional mean of Y for given X
- Loosely written as: Y = α + βX, where Y here means E(Y|X)

#### Assumptions of the Classical Regression Model ⭐

These five assumptions are needed for OLS estimates to be valid:

| # | Assumption | Mathematical Form | Name |
|---|-----------|------------------|------|
| 1 | Zero mean of disturbance | E(U) = 0 for all X | Zero conditional mean |
| 2 | Constant variance of U | V(U|X) = σ² | **Homoscedasticity** |
| 3 | No correlation between disturbances | Cov(Uᵢ, Uⱼ) = 0 for i≠j | No autocorrelation |
| 4 | X is non-stochastic | X is fixed in repeated samples | Non-stochastic X |
| 5 | Linearity in parameter | All parameters have power 1 | Linearity |

**Corollary of Assumption 4**: Since X is non-stochastic, X and U are independent: Cov(X, U) = 0.

### Definitions

- **Population Regression Function (PRF)**: The true but unknown relationship Y = α + βX + U in the population, expressing Y as a linear function of X plus a random disturbance. ⭐ (exam-important)
- **Disturbance Term (U)**: A random variable in the regression model representing the combined effect of all omitted, unknown, and random factors affecting Y. Also called "error term" or "stochastic term." ⭐ (exam-important)
- **Homoscedasticity**: The assumption that the variance of the disturbance term U is constant (σ²) for all values of X. ⭐ (exam-important)

### Mechanisms / Processes

**From PRF to Population Regression Line:**
1. Start with PRF: Y = α + βX + U
2. Take conditional expectation: E(Y|X) = E(α + βX + U|X)
3. Since α and β are constants and X is non-stochastic: E(α + βX|X) = α + βX
4. Since E(U) = 0: E(U|X) = 0
5. Result: **E(Y|X) = α + βX** — the population regression line

### Examples

**Consumption function example (from text):**
- Y = consumption, X = income
- PRF: Consumption = α + β(Income) + U
- For a given income level X₀, consumption is not fixed — it follows a distribution around α + βX₀
- U captures random variation (different spending habits, unexpected expenses, etc.)

### ⚠️ Common Mistakes

- ❌ Mistake: Thinking V(U) = 0 means no disturbance term → ✅ Correct: Homoscedasticity means *constant*, not *zero*, variance: V(U) = σ² (a fixed positive number)
- ❌ Mistake: Confusing PRF and the population regression LINE → ✅ Correct: PRF is Y = α + βX + U; the line is E(Y|X) = α + βX (U removed by taking expectation)

### Edge Cases & Caveats

- If any of the 5 classical assumptions are violated, OLS estimates may lose their desirable properties (unbiasedness, minimum variance)
- Violations are covered in Unit 10 (multicollinearity, heteroscedasticity, autocorrelation)

> **Quick Recall:**
> - PRF: Y = α + βX + U (unknown — we can't observe it)
> - Population regression line: E(Y|X) = α + βX (after taking E[U] = 0)
> - 5 classical assumptions needed for valid OLS
> - **Homoscedasticity**: V(U) = σ² (constant), not zero
> - **No autocorrelation**: Cov(Uᵢ, Uⱼ) = 0 for i ≠ j

### Connections

- Builds on: Linearity concepts (earlier in this chunk)
- Leads to: Sample Regression Function (next section, continues in Chunk 002)
- Related to: Gauss-Markov theorem (Chunk 002) which proves OLS is BLUE under these assumptions
- Violations covered in: Unit 10 (Chunk 005-006)

### Open Questions

1. Can these classical assumptions all hold simultaneously in real economic data?

---

## Section: Sample Regression Function 🔴
<!-- This section continues in chunk 002 -->

### Core Idea

Since the Population Regression Function (PRF) is unknown, we estimate it from sample data using the **Sample Regression Function (SRF)**: **Ŷ = α̂ + β̂X + Û**. Here α̂ and β̂ are sample *estimators* for the unknown population parameters α and β. The SRF is the **estimated** counterpart of the PRF — our "best guess" at the true relationship based on available data.

> **In Simple Terms:** The PRF is the hidden truth. The SRF is our best guess at that truth based on the sample data we have. As we get more data, our SRF should get closer and closer to the true PRF.

### Key Concepts

The SRF mirrors the PRF in structure but uses estimated (hat) values:
- **α̂** = estimator for population intercept α
- **β̂** = estimator for population slope β
- **Ŷ** = estimated/fitted value of Y (the prediction)
- **Û** = residual = (actual Y) − (fitted Ŷ) = estimator for population U

The purpose is to use α̂ and β̂ drawn from the sample as the *best available estimates* for the unknown population α and β.

### Definitions

- **Sample Regression Function (SRF)**: Ŷ = α̂ + β̂X + Û — the estimated regression equation from sample data, used to approximate the PRF. ⭐ (exam-important)
- **Residual (Û)**: The difference between the actual value Y and the fitted value Ŷ from the SRF. It is the sample counterpart of the population disturbance U.

<!-- This section continues in chunk 002 -->

> **Quick Recall:**
> - PRF: Y = α + βX + U (unknown population truth)
> - SRF: Ŷ = α̂ + β̂X + Û (estimated from sample)
> - α̂, β̂ are **estimators** for the unknown α, β
> - Û (residual) is the sample version of population disturbance U

### Connections

- Builds on: Population Regression Function (this chunk)
- Continues in: Chunk 002 (Estimation of SRF using OLS, Gauss-Markov theorem)

### Open Questions

1. How exactly are α̂ and β̂ computed? (Answered in Chunk 002 — OLS estimation)
2. How do we know if our SRF is a good approximation of the PRF?
