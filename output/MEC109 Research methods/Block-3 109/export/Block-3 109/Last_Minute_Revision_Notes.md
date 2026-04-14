# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Feature | Linear in Variable | Linear in Parameter |
|---------|-------------------|---------------------|
| Requirement for OLS | Not required | **Required** |
| Example | Y = α + βX | Y = α + βX + γX² |
| Graph | Straight line | Can be curved |
- **Regression Model**: Formulation of an economic relationship as an equation where the dependent variable is a function of explanatory variables, used for parameter estimation and hypothesis testing. ⭐ (exam-important)
- **Linear in Parameter**: A model where the highest power of any parameter (constant) is 1 — the essential requirement for OLS estimation. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming a "curved" regression line means it's non-linear and can't be estimated → ✅ Correct: Linearity in *parameter* (not variable) is what OLS requires; polynomial curves are fine.
- ❌ Mistake: Confusing intercept (α) with disturbance term (U) → ✅ Correct: α captures known systematic effects; U captures random/unknown effects.

**Quick Recall:**
- OLS requires linearity in **parameter**, not necessarily in variable
- Y = α + βX² is OK for OLS (linear in α, β)
- Y = α + β²X is NOT OK for OLS directly
- Log transformation can linearize some non-linear models
- **Stochastic Variable**: A variable whose value is determined by a probability distribution, not by a fixed rule. The dependent variable Y in regression is stochastic. ⭐ (exam-important)

**Quick Recall:**
- Y is stochastic; X is non-stochastic in classical regression
- For each X, there's a distribution of Y values
- Regression estimates the **mean** of Y for given X

### Population Regression Function 🔴

**The Disturbance Term (U)**
| Source of U | Description |
|-------------|-------------|
| Inherent randomness in human behaviour | Unpredictable human decisions even with same X |
| Omitted variables | Known factors deliberately left out for parsimony |
| Measurement error | Errors in measuring Y accurately |
| Model misspecification | Wrong functional form chosen for the model |

**Disturbance Term vs Intercept (α)**
| Feature | Disturbance Term (U) | Intercept (α) |
|---------|---------------------|---------------|
| Nature | Random, stochastic | Fixed constant |
| Represents | Unknown, random factors | Known, systematic factors not explicitly included |
| Mean | E(U) = 0 | Non-zero in general |
| Example | Random mood effects on spending | Average effect of all omitted income-categories |

**Population Regression Line**
- **E(Y|X) = α + βX** (since E(U) = 0)
- This is the **Population Regression Line** — gives the average/conditional mean of Y for given X
- Loosely written as: Y = α + βX, where Y here means E(Y|X)

**Assumptions of the Classical Regression Model ⭐**
| # | Assumption | Mathematical Form | Name |
|---|-----------|------------------|------|
| 1 | Zero mean of disturbance | E(U) = 0 for all X | Zero conditional mean |
| 2 | Constant variance of U | V(U|X) = σ² | **Homoscedasticity** |
| 3 | No correlation between disturbances | Cov(Uᵢ, Uⱼ) = 0 for i≠j | No autocorrelation |
| 4 | X is non-stochastic | X is fixed in repeated samples | Non-stochastic X |
| 5 | Linearity in parameter | All parameters have power 1 | Linearity |
- **Population Regression Function (PRF)**: The true but unknown relationship Y = α + βX + U in the population, expressing Y as a linear function of X plus a random disturbance. ⭐ (exam-important)
- **Disturbance Term (U)**: A random variable in the regression model representing the combined effect of all omitted, unknown, and random factors affecting Y. Also called "error term" or "stochastic term." ⭐ (exam-important)
- **Homoscedasticity**: The assumption that the variance of the disturbance term U is constant (σ²) for all values of X. ⭐ (exam-important)
1. Start with PRF: Y = α + βX + U
2. Take conditional expectation: E(Y|X) = E(α + βX + U|X)
3. Since α and β are constants and X is non-stochastic: E(α + βX|X) = α + βX
4. Since E(U) = 0: E(U|X) = 0
5. Result: **E(Y|X) = α + βX** — the population regression line
- Y = consumption, X = income
- PRF: Consumption = α + β(Income) + U
- For a given income level X₀, consumption is not fixed — it follows a distribution around α + βX₀
- U captures random variation (different spending habits, unexpected expenses, etc.)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking V(U) = 0 means no disturbance term → ✅ Correct: Homoscedasticity means *constant*, not *zero*, variance: V(U) = σ² (a fixed positive number)
- ❌ Mistake: Confusing PRF and the population regression LINE → ✅ Correct: PRF is Y = α + βX + U; the line is E(Y|X) = α + βX (U removed by taking expectation)
- If any of the 5 classical assumptions are violated, OLS estimates may lose their desirable properties (unbiasedness, minimum variance)
- Violations are covered in Unit 10 (multicollinearity, heteroscedasticity, autocorrelation)

**Quick Recall:**
- PRF: Y = α + βX + U (unknown — we can't observe it)
- Population regression line: E(Y|X) = α + βX (after taking E[U] = 0)
- 5 classical assumptions needed for valid OLS
- **Homoscedasticity**: V(U) = σ² (constant), not zero
- **No autocorrelation**: Cov(Uᵢ, Uⱼ) = 0 for i ≠ j
- Builds on: Linearity concepts (earlier in this chunk)
- Leads to: Sample Regression Function (next section, continues in Chunk 002)
- Related to: Gauss-Markov theorem (Chunk 002) which proves OLS is BLUE under these assumptions
- Violations covered in: Unit 10 (Chunk 005-006)
1. Can these classical assumptions all hold simultaneously in real economic data?

### Sample Regression Function 🔴
- **α̂** = estimator for population intercept α
- **β̂** = estimator for population slope β
- **Ŷ** = estimated/fitted value of Y (the prediction)
- **Û** = residual = (actual Y) − (fitted Ŷ) = estimator for population U
- **Sample Regression Function (SRF)**: Ŷ = α̂ + β̂X + Û — the estimated regression equation from sample data, used to approximate the PRF. ⭐ (exam-important)
- **Residual (Û)**: The difference between the actual value Y and the fitted value Ŷ from the SRF. It is the sample counterpart of the population disturbance U.

**Quick Recall:**
- PRF: Y = α + βX + U (unknown population truth)
- SRF: Ŷ = α̂ + β̂X + Û (estimated from sample)
- α̂, β̂ are **estimators** for the unknown α, β
- Û (residual) is the sample version of population disturbance U
- Builds on: Population Regression Function (this chunk)
- Continues in: Chunk 002 (Estimation of SRF using OLS, Gauss-Markov theorem)
1. How exactly are α̂ and β̂ computed? (Answered in Chunk 002 — OLS estimation)
2. How do we know if our SRF is a good approximation of the PRF?

### Sample Regression Function 🔴

### Estimation of Sample Regression Function 🔴

**Ordinary Least Squares (OLS) Procedure**
1. ΣY = nα̂ + β̂ΣX
2. ΣXY = α̂ΣX + β̂ΣX²
- **β̂ = Σxy / Σx²** where x = X − X̄ (deviation from mean), y = Y − Ȳ  
- **α̂ = Ȳ − β̂X̄** (intercept estimated from the means)

**Gauss-Markov Theorem**
| Property | Meaning | Technical Statement |
|---------|---------|---------------------|
| **Linear** | Can be expressed as a linear function of observed Y | α̂ = ΣaᵢYᵢ, β̂ = ΣkᵢYᵢ |
| **Unbiased** | On average, equal to the population parameter | E(α̂) = α, E(β̂) = β |
| **Minimum Variance** | Smallest variance among all linear unbiased estimators | More efficient than any other LUE |
- **The Gauss-Markov Theorem** states: *"Under the assumptions of the classical linear regression model, among all linear unbiased estimators, the least square estimators have the minimum variance — i.e., OLS estimators are BLUE (Best Linear Unbiased Estimators)."* ⭐

**Standard Error of Estimate**
- **Unbiased estimator of σ²**: σ̂² = Σ Û² / (n−2)
- **n−2** is the degrees of freedom (we lose 2 df because we estimated 2 parameters: α̂ and β̂)
- **Standard Error of Estimate (σ̂)** = √[Σ Û² / (n−2)] — measures how spread out residuals are around the regression line
- **se(β̂)** = σ̂ / √(Σx²)
- **se(α̂)** = σ̂ √(ΣX² / n·Σx²)
- **OLS (Ordinary Least Squares)**: Method that estimates regression parameters by minimizing the sum of squared residuals Σ Û². ⭐ (exam-important)
- **BLUE (Best Linear Unbiased Estimator)**: The property of OLS estimators guaranteed by the Gauss-Markov theorem — linear, unbiased, and with minimum variance among all linear unbiased estimators. ⭐ (exam-important)
- **Standard Error of Estimate**: σ̂ = √[Σ Û² / (n−2)] — the standard deviation of residuals around the regression line. ⭐ (exam-important)
- **Degrees of Freedom**: n−2 in simple regression (n observations, 2 parameters estimated: α̂ and β̂).
1. Compute means: X̄ = ΣX/n, Ȳ = ΣY/n
2. Compute deviations: x = X − X̄, y = Y − Ȳ
3. Compute β̂ = Σxy / Σx²
4. Compute α̂ = Ȳ − β̂X̄
5. Compute fitted values: Ŷᵢ = α̂ + β̂Xᵢ
6. Compute residuals: Ûᵢ = Yᵢ − Ŷᵢ
7. Compute σ̂² = Σ Û² / (n−2)
8. Compute standard errors of α̂ and β̂
| Variable | Value |
|---------|-------|
| Y = Employed (million) | Range: 100–295 |
| X = Labour Force (million) | Range: 120–320 |
| Sample size (n) | 10 |
- β̂ = 38850 / 40250 = **0.965217** → For every 100 additional persons in labour force, about 97 get employed
- α̂ = 193.5 − (0.965217 × 215) = **−14.0217** → Negative intercept: average effect of omitted variables
- σ̂² = 403.8043 / 8 = **50.475537** (degrees of freedom = 10 − 2 = 8)
- se(β̂) = 0.0354118; se(α̂) = 7.938264
- R² = 37498.67 / 37902.5 = **0.989345** → ~99% of employment variation explained by labour force
- Slope β̂ = 0.965: For 100 more job seekers, ~97 find employment
- Intercept α̂ = −14.02: Average combined effect of all omitted factors (e.g., technology, policy)  
- R² = 0.989: Excellent fit — labour force alone explains 99% of employment variation

### ⚠️ Common Mistakes
- ❌ Mistake: Using n instead of (n−2) in the denominator of σ̂² → ✅ Correct: Must use degrees of freedom (n−2), otherwise σ̂² is biased
- ❌ Mistake: Thinking BLUE means OLS is the best estimator overall → ✅ Correct: BLUE only means best among **linear unbiased** estimators; non-linear estimators could theoretically do better
- BLUE property holds **only when all 5 classical assumptions are satisfied**
- If assumptions are violated (e.g., heteroscedasticity), OLS is no longer BLUE — see Unit 10

**Quick Recall:**
- OLS minimizes Σ Û² → gives β̂ and α̂
- **Gauss-Markov**: OLS is **BLUE** under classical assumptions
- Standard error σ̂ = √[Σ Û²/(n−2)] — uses n−2 (degrees of freedom)
- β̂ = Σxy/Σx² ; α̂ = Ȳ − β̂X̄
- Builds on: Classical regression model assumptions (Chunk 001)
- Leads to: Goodness of Fit (next section, same chunk)
- Related to: Heteroscedasticity and autocorrelation violations (Chunk 006)

### Goodness of Fit 🔴

**Decomposition of Total Variation (TSS = ESS + RSS)**
| Component | Formula | Meaning |
|-----------|---------|---------|
| **TSS** (Total Sum of Squares) | Σ(Y − Ȳ)² | Total variation in Y |
| **ESS** (Explained Sum of Squares) | Σ(Ŷ − Ȳ)² | Variation explained by regression |
| **RSS** (Residual Sum of Squares) | Σ(Y − Ŷ)² = Σ Û² | Unexplained variation (residuals) |

**Coefficient of Determination (R²)**
- R² = 0: Regression explains nothing (the line is flat/useless)
- R² = 1: Regression explains everything (perfect fit, no residuals)
- 0 ≤ R² ≤ 1 always holds
- **Coefficient of Determination (R²)**: The ratio ESS/TSS; measures the proportion of total variation in Y explained by the regression model. Ranges from 0 to 1. ⭐ (exam-important)
- **TSS (Total Sum of Squares)**: Σ(Y − Ȳ)² — measures total variation of Y around its mean.
- **ESS (Explained Sum of Squares)**: Σ(Ŷ − Ȳ)² — variation of Y accounted for by the regression.
- **RSS (Residual Sum of Squares)**: Σ(Y − Ŷ)² = Σ Û² — unexplained variation.
1. Compute TSS = Σ(Y − Ȳ)²
2. Compute RSS = Σ Û² (from OLS residuals)
3. ESS = TSS − RSS
4. R² = ESS / TSS
- TSS = Σy² = 37902.5
- RSS = Σ Û² = 403.8043
- ESS = 37902.5 − 403.8043 = 37498.67
- R² = 37498.67 / 37902.5 = **0.989345 ≈ 0.99**
- Interpretation: **99%** of variation in employment is explained by variation in labour force → excellent fit

### ⚠️ Common Mistakes
- ❌ Mistake: High R² always means the model is good → ✅ Correct: R² can be inflated by adding more variables; use adjusted R² to penalize for extra variables (covered in Unit 10)
- ❌ Mistake: R² = 1 is always the goal → ✅ Correct: Perfect R² = 1 means every point lies exactly on the line, which is almost never the case in real data and could indicate overfitting
- R² can never decrease when adding more explanatory variables — this motivates the **adjusted R²** (R̄²) in multiple regression
- R² is not appropriate if the regression model has no intercept

**Quick Recall:**
- **TSS = ESS + RSS** (fundamental identity)
- **R² = ESS/TSS = 1 − RSS/TSS**
- R² ∈ [0, 1]: Higher = better fit
- R² = 0.989 means "regression explains 98.9% of variation in Y"
- Builds on: OLS estimation (previous section, same chunk)
- Extended to adjusted R² in: Unit 10 Multivariable Regression (Chunk 005)

### Functional Forms of Regression Model 🔴

**1. Linear Model**
- **Equation**: Y = α + βX + U
- Both linear in variable AND linear in parameter
- **Slope β**: Constant — for every 1-unit increase in X, Y changes by β units
- **Interpretation**: β = dY/dX = constant
- **When to use**: When the effect of X on Y is constant (no acceleration/deceleration)

**2. Log-linear Model (Double-Log or Constant Elasticity Model)**
- **Equation**: log Y = α + β log X + U
- Linear in parameter (after log transformation), non-linear in original variables
- **Slope β**: Measures **elasticity** — % change in Y for 1% change in X → **β = (dY/Y)/(dX/X)**
- **Key property**: β is the **constant elasticity** → same elasticity at every point on the curve
- **When to use**: When the relationship is proportional (e.g., demand functions)
- Also called: "double-log model" or "constant-elasticity model"

**Quick Recall:**
- Linear: β = dY/dX (slope = constant)
- Log-linear: β = elasticity = % ΔY / % ΔX (constant throughout)
- Semi-log: slope = % ΔY / absolute ΔX (covered in chunk 003)
- Reciprocal: Y has an upper or lower limit (covered in chunk 003)
- Builds on: Linearity concept (Chunk 001)
- Continues in: Chunk 003 (Semi-log, Reciprocal models, examples)
1. How do we choose between functional forms in practice?

### Functional Forms of Regression Model 🔴

**3. Semi-Log Model (Growth Rate Model)**
- **Equation**: log Y = α + βt + U (where t = time)
- Y is in logs; the independent variable (time t) is in absolute terms → **"semi-log"** because only one side is logged
- **Slope β**: Measures the **proportional change** in Y per unit change in t → β measures the **growth rate** of Y
- **Interpretation**: If β = 0.034 → Y grows at approximately **3.4% per year**
- **When to use**: Estimating constant growth rates over time (GDP growth, population growth, money supply growth)
| Model | LHS | RHS | β measures |
|-------|-----|-----|-----------|
| Linear | Y | X | dY/dX = constant slope |
| Log-linear | log Y | log X | Elasticity = %ΔY/%ΔX |
| **Semi-log** | **log Y** | **t (time)** | **Growth rate of Y** |
| Reciprocal | Y | 1/X | Rate of approach to limit |

**4. Reciprocal Model**
- **Equation**: Y = α + β(1/X) + U
- Non-linear in variable (power of X is −1), but **linear in parameter** → estimable by OLS
- **Key characteristic**: As X → ∞, the term β/X → 0, so Y approaches **α as an asymptote/limit**
- Y has a fixed **upper or lower bound** = α
- **When to use**: When there's a theoretical limit to Y regardless of how large X gets
1. **Infant mortality vs per capita GNP**: As income rises, child mortality falls — but cannot fall below zero; approaches a lower limit
2. **Phillips Curve**: As unemployment rises, inflation rate falls — but approaches a negative limiting value, not −∞
- **Semi-log Model**: log Y = α + βt + U; β measures the growth rate of Y; used when one variable grows at a constant proportional rate over time. ⭐ (exam-important)
- **Reciprocal Model**: Y = α + β/X + U; Y approaches α as X increases indefinitely (asymptote). Used when there's a theoretical limit. ⭐ (exam-important)
- **Elasticity**: In log-linear model, β = %ΔY / %ΔX = constant throughout; the slope coefficient measures elasticity directly.
- Data: 23 quarterly observations
- Regression: ln(ExpDur) = −9.697 + 1.906 ln(PCExp)
- β̂ = 1.906 → **elasticity > 1** → expenditure on durables is **highly elastic** (luxury good behavior)
- R² = 0.985 → excellent fit
- Regression: log GDP = 12.19473 + 0.033729t
- β̂ = 0.034 → **growth rate ≈ 3.4% per year**
- R² = 0.984 → tight fit
- **Interpretation**: Confirms the "Hindu Rate of Growth" (~3.5%) documented in India's 1960s–1970s
- Regression: Y = 81.944 + (−2723.117)(1/X)
- β̂ = −2723 (negative) → as GNP rises, mortality falls
- α̂ = 81.944 → **asymptotic limit ≈ 82 deaths per 1000 live births** (floor value of infant mortality)
- R² = 0.459 → moderate fit
- Linear regression: FCE = −108206.4 + 0.719674 GDP
- β̂ = 0.720 → **MPC ≈ 72%** — for every ₹100 increase in GDP, final consumption rises by ₹72
- R² = 0.998 → almost perfect fit
- t-statistic for β̂ = 91.50 >> critical values (2.845 at 1%, 2.086 at 5%) → relationship is highly significant

### ⚠️ Common Mistakes
- ❌ Mistake: Interpreting Semi-log β as an absolute change → ✅ Correct: β in semi-log = proportional/percentage change in Y, not absolute
- ❌ Mistake: Thinking the reciprocal model's limiting value is β → ✅ Correct: The asymptote/limit is **α** (the intercept); β governs how fast Y approaches that limit
- The log-linear model's elasticity β is constant throughout the range — real-world elasticities often vary, so this is a simplification
- Semi-log model β approximates growth rate well only for small values of β; for large growth rates, exact formula is (e^β − 1)

**Quick Recall:**
- **4 functional forms**: Linear (β = dY/dX), Log-linear (β = elasticity), Semi-log (β = growth rate), Reciprocal (α = limiting value)
- All 4 are **linear in parameter** → OLS applicable
- Semi-log: log Y on left, time t on right
- Reciprocal: Y approaches **α** as X → ∞
- Builds on: Log-linear model (Chunk 002)
- Leads to: Classical Normal Regression Model (next section, same chunk)

### Classical Normal Regression Model 🔴

**Normality Assumption**
- E(Uᵢ) = 0 for all i (mean zero)
- V(Uᵢ) = σ² for all i (constant variance — homoscedasticity)  
- Cov(Uᵢ, Uⱼ) = 0 for i ≠ j (no autocorrelation)
- All three conditions together: U ~ N(0, σ²) independently and identically distributed
1. Since β̂ is a linear function of U (β̂ = ΣkᵢYᵢ = ΣkᵢUᵢ + constants), and U is normal → **β̂ is also normally distributed**
2. This allows standard form hypothesis testing using the t-distribution

**Connection to Maximum Likelihood Estimation (MLE)**
- MLE gives **identical estimates** to OLS for β parameters
- However, MLE estimate of σ² is **biased** (divides by n, not by n−2)
- Therefore, OLS + normality is generally preferred over MLE for regression
- **Classical Normal Regression Model (CNRM)**: The classical regression model (5 assumptions) PLUS the normality assumption for U: U ~ N(0, σ²). Required for hypothesis testing. ⭐ (exam-important)
- **iid Normal**: Independent and Identically Distributed Normal — all disturbances follow the same N(0, σ²) distribution independently.
1. U ~ N(0, σ²) (normality assumption)
2. β̂ = ΣkᵢYᵢ = ΣkᵢUᵢ + constants (β̂ is linear in U)
3. Linear combination of normal variables → normal
4. Therefore: **β̂ ~ N(β, σ²/Σx²)**
5. Known mean = β; known variance = σ²/Σx²

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking normality assumption is one of the original 5 → ✅ Correct: Normality is a 6th assumption, added in addition to the 5 classical assumptions, specifically needed for hypothesis testing
- ❌ Mistake: Thinking MLE gives better β estimates → ✅ Correct: OLS and MLE give **identical β estimates** under normality; MLE's σ² estimate is actually biased

**Quick Recall:**
- CNRM = 5 classical assumptions + **U ~ N(0, σ²)**
- Normality allows: β̂ ~ N(β, σ²/Σx²)
- Needed for: **hypothesis testing using t-distribution**
- MLE gives same β̂ as OLS but biased σ̂²
- Builds on: 5 Classical assumptions (Chunk 001)
- Leads to: Hypothesis Testing (next section, continues in Chunk 004)
- Related to: Maximum Likelihood Estimation (Unit 10 / Chunk 006)

### Hypothesis Testing 🔴

**Student-t Distribution for Hypothesis Testing**
- β₀ = value under null hypothesis (usually 0)
- se(β̂) = estimated standard error = σ̂ / √(Σx²)
- n−2 = degrees of freedom
- Builds on: Classical Normal Regression Model (this chunk)
- Continues in: Chunk 004 (worked examples of hypothesis tests)
1. When should we use a one-tailed vs two-tailed t-test?

### Hypothesis Testing 🔴

**Student-t Distribution**
- β₀ = hypothesized value of β (usually **0** for testing significance)
- se(β̂) = estimated standard error of β̂
- n−2 = degrees of freedom
- Under H₀: β = 0, the t-statistic simplifies to **t = β̂ / se(β̂)**

**Null and Alternative Hypotheses**
- H₀: β = 0 (no relationship)
- H₁: β ≠ 0 (any relationship)
- H₀: β = β₀ (e.g., β = 0.80)
- H₁: β ≠ β₀
- Compute |t_calculated|
- Find t_critical from t-table (at desired significance level, with n−2 df)
- If |t_calc| > t_critical → **Reject H₀**
- If |t_calc| ≤ t_critical → **Cannot reject H₀**

**Steps for Hypothesis Testing in Regression**
| Step | Action |
|------|--------|
| 1 | Set H₀ and H₁ |
| 2 | Choose significance level (1% or 5%) |
| 3 | Compute t = (β̂ − β₀) / se(β̂) |
| 4 | Find critical t from table (df = n−2) |
| 5 | Compare: Reject H₀ if |t_calc| > t_critical |
| 6 | Interpret in the context of the economic hypothesis |
1. Start with CNRM → β̂ ~ N(β, σ²/Σx²)
2. σ is unknown → substitute σ̂
3. Standardize → t = (β̂ − β) / se(β̂) ~ t(n−2)
4. Under H₀: β = β₀ → t = (β̂ − β₀) / se(β̂)
5. Use t-table to find critical value for given df and significance level
- H₀: β = 0; H₁: β ≠ 0 (two-tailed)
- β̂ = 0.719676; se(β̂) = 0.007865; df = n−2 = 22−2 = 20
- t_calc = β̂ / se(β̂) = 0.719676 / 0.007865 = **91.503**
- t_critical at 5% (df=20, two-tailed) = **2.086**; at 1% = **2.845**
- Since 91.503 >> 2.845: **Reject H₀ decisively**
- **Conclusion**: FCE significantly depends on GDP in India (1980-2001) ✅
- H₀: β = 0.80; H₁: β ≠ 0.80 (two-tailed)
- t_calc = (0.719676 − 0.80) / 0.007865 = (−0.080324) / 0.007865 = **−10.211**
- |t_calc| = 10.211 >> critical values of 2.086 and 2.845
- **Reject H₀**: MPC was NOT 80% during 1980-2001
- **Conclusion**: India's MPC ≈ 72%, not 80%, during the sample period

### ⚠️ Common Mistakes
- ❌ Mistake: Using Z-table instead of t-table when σ is unknown → ✅ Correct: When σ is estimated (replaced by σ̂), use student-t distribution, not standard normal
- ❌ Mistake: Accepting H₀ when we fail to reject it → ✅ Correct: We either "reject H₀" or "fail to reject H₀" — we never "accept" H₀ (absence of evidence ≠ evidence of absence)
- One-tailed tests are appropriate when the direction of the effect is specified by theory (e.g., H₁: β > 0)
- The t-distribution approaches the normal distribution as n → ∞ (df → ∞)
- High t-statistic → statistically significant, but not necessarily economically meaningful

**Quick Recall:**
- t-test statistic: t = (β̂ − β₀) / se(β̂) ~ t(n−2)
- Reject H₀ if |t_calc| > t_critical
- At 5% significance, two-tailed, df=20: t_critical = **2.086**
- At 1% significance, two-tailed, df=20: t_critical = **2.845**
- India's consumption function: t = 91.5 → highly significant!
- Builds on: Classical Normal Regression Model (Chunk 003)
- Builds on: Standard Error of Estimate (Chunk 002)
- Related to: F-test in multiple regression (Chunk 005/006)
- **Classical Normal Regression Model**: A linear regression model in which the disturbance term is additionally assumed to be **normally distributed** (in addition to the 5 classical assumptions). Required for hypothesis testing using t-distribution. ⭐ (exam-important)
- **Classical Regression Model**: The conventional regression model Y = α + βX + U whose parameters are estimated by OLS under 5 assumptions. ⭐ (exam-important)
- **Gauss-Markov Theorem**: Under the assumptions of the classical regression model, among all linear unbiased estimators, the least square estimators have the minimum variance — i.e., OLS is BLUE. ⭐ (exam-important)
- **Goodness of Fit**: The ratio of Explained Sum of Squares (ESS) to Total Sum of Squares (TSS) — the R² coefficient. Measures how well the regression line fits the data. ⭐ (exam-important)
- **Functional Forms**: Linear (dY/dX = constant), Log-linear (elasticity = constant), Semi-log (growth rate = constant), Reciprocal (limiting value = α). All are linear in parameter. ⭐ (exam-important)
- **Hypothesis Testing**: Testing hypotheses about β using t = (β̂ − β₀)/se(β̂) ~ t(n−2). ⭐ (exam-important)

**Quick Recall:**
1. PRF: Y = α + βX + U (population truth — unknown)
2. 5 Classical Assumptions → OLS is BLUE (Gauss-Markov)
3. SRF: Ŷ = α̂ + β̂X (estimated from sample)
4. R² = ESS/TSS (goodness of fit: 0 to 1)
5. 4 Functional Forms: Linear, Log-linear, Semi-log, Reciprocal
6. +Normality assumption → CNRM → t-test for β

### Introduction to Multivariable Regression Models 🔴

**Regression Model with Two Explanatory Variables**
- **Non-stochastic form**: E(Yₜ) = β₀ + β₁X₁ₜ + β₂X₂ₜ
- **Stochastic form**: Yₜ = β₀ + β₁X₁ₜ + β₂X₂ₜ + μₜ
- (β₀ + β₁X₁ + β₂X₂) = **systematic/deterministic component** = E(Y) point on the regression plane
- μₜ = **random component** — determined by factors other than X₁ and X₂

**OLS Estimation with Two Explanatory Variables**
1. ΣY = nb₀ + b₁ΣX₁ + b₂ΣX₂
2. ΣYX₁ = b₀ΣX₁ + b₁ΣX₁² + b₂ΣX₁X₂
3. ΣYX₂ = b₀ΣX₂ + b₁ΣX₁X₂ + b₂ΣX₂²
- b₀ = Ȳ − b₁X̄₁ − b₂X̄₂
- b₁ = (Σx₁²·Σyx₂ − Σx₁x₂·Σyx₁) / (Σx₁²·Σx₂² − (Σx₁x₂)²)
- b₂ = (Σx₂²·Σyx₁ − Σx₁x₂·Σyx₂) / (Σx₁²·Σx₂² − (Σx₁x₂)²)

**Degrees of Freedom in Multiple Regression**
- **Degrees of freedom = n − k**
- For two-variable model (k=3: b₀, b₁, b₂): **df = n − 3**
- Unbiased estimator of σ²: **σ̂² = Σeₜ² / (n − 3)**

**Interpretation of Partial Regression Coefficients**
- **b₁** = rate of change in Y per unit change in X₁, **holding X₂ constant** (ceteris paribus)
- **b₂** = rate of change in Y per unit change in X₂, **holding X₁ constant** (ceteris paribus)
- **Multiple Regression**: Regression of one dependent variable on **more than one** independent/explanatory variable. ⭐ (exam-important)
- **Partial Regression Coefficient**: The coefficient of an individual predictor in multiple regression — measures the effect of that variable holding all other variables constant. ⭐ (exam-important)
- **Degrees of Freedom (DF)**: n − k, where k = number of parameters estimated. In two-variable multiple regression (3 parameters): df = n − 3.
1. Set up SRF: Yₜ = b₀ + b₁X₁ₜ + b₂X₂ₜ + eₜ
2. Minimize Σeₜ² by partial differentiation w.r.t. b₀, b₁, b₂
3. Solve the three normal equations simultaneously → get b₀, b₁, b₂
4. Compute σ̂² = Σeₜ²/(n−3)
5. Compute standard errors: se(b₁), se(b₂), se(b₀)

### ⚠️ Common Mistakes
- ❌ Mistake: Interpreting b₁ as the total effect of X₁ on Y → ✅ Correct: b₁ is the **partial** effect (holding X₂ constant); the total effect includes indirect effects through X₂
- ❌ Mistake: Using df = n−2 in multiple regression → ✅ Correct: df = n−k; with 3 parameters, df = n−3

**Quick Recall:**
- Multiple regression: Y = β₀ + β₁X₁ + β₂X₂ + μ
- Each coefficient = partial effect (other things equal)
- OLS minimizes Σeₜ²; 3 normal equations for 2-variable model
- df = n−k (k = number of parameters)
- σ̂² = Σeₜ²/(n−3) for two-variable regression
---

### Multiple Coefficient of Determination (R²) and ANOVA 🔴

**Multiple R² (Coefficient of Multiple Determination)**
- ESS = b₁Σyx₁ + b₂Σyx₂ (explained sum of squares)
- TSS = Σy² (total sum of squares)
- RSS = Σy² − b₁Σyx₁ − b₂Σyx₂ (residual sum of squares)
- R² = ESS/TSS = 1 − RSS/TSS; ∈ [0,1]

**Adjusted R² (R̄²)**
- **R̄² = 1 − (1−R²)(n−1)/(n−k)** ⭐ (exam-important)
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

**ANOVA Table for Multiple Regression**
| Source | Sum of Squares | df | Mean SS |
|--------|---------------|-----|---------|
| Due to regression (ESS) | b₁Σyx₁ + b₂Σyx₂ | 2 (= k−1) | ESS/2 |
| Due to residuals (RSS) | Σeₜ² | n−3 | RSS/(n−3) |
| Total (TSS) | Σy² | n−1 | — |
- **F = (ESS/df_ESS) / (RSS/df_RSS)** ~ F(k−1, n−k)
- F can also be expressed as: **F = [R²/(k−1)] / [(1−R²)/(n−k)]**
- Large F → reject H₀ → at least one X variable significantly affects Y
- **Adjusted R² (R̄²)**: Coefficient of determination adjusted for degrees of freedom; penalizes adding unnecessary variables. ⭐ (exam-important)
- **F-test (ANOVA)**: Overall significance test for the regression model; tests whether all slope coefficients are simultaneously zero.
- **Analysis of Variance (ANOVA)**: Study of the components of TSS (ESS + RSS) and their degrees of freedom.

### ⚠️ Common Mistakes
- ❌ Mistake: Maximizing R² by adding many variables will always yield a better model → ✅ Correct: Use R̄² to compare models; adding variables that don't add meaningful information hurts model quality
- ❌ Mistake: F-test tests each coefficient individually → ✅ Correct: F-test is a *joint* test that ALL slopes simultaneously equal zero

**Quick Recall:**
- **R² always ↑** when variables added → use **R̄²** for comparison
- R̄² = 1 − (1−R²)(n−1)/(n−k)
- Include variable if R̄² ↑ (or |t| > 1)
- ANOVA: F = (ESS/df_ESS) / (RSS/df_RSS) ~ F(k−1, n−k)
- F captures overall goodness-of-fit significance
- Builds on: R² from Unit 9 (Chunk 002)
- Leads to: Econometric problems — multicollinearity, heteroscedasticity, autocorrelation (Chunk 006)

### Generalisation to N Explanatory Variables 🔴

**Classical Assumptions for General Multiple Regression**
1. **E(μᵢ) = 0** for all i (zero mean errors)
2. **E(μᵢ²) = σ² for all i** and **E(μᵢμⱼ) = 0 for i≠j** (homoscedasticity + no autocorrelation)
   - In matrix form: E(UU') = σ²I
3. **X is linearly independent** (no exact linear relationship between any X variables → no multicollinearity)
4. **Number of observations > number of parameters** (n > k)

**Matrix OLS Formula**
- Valid only when X'X is invertible (full rank X matrix)
- Requires absence of exact multicollinearity among X variables
- **Variance**: Var(b) = σ²(X'X)⁻¹
- **Multi-co-linearity**: Existence of exact or near-exact linear relationships between explanatory variables, causing X'X to be singular or near-singular. ⭐ (exam-important)
- **The three key violations**: Multicollinearity, heteroscedasticity, autocorrelation — each causes OLS to no longer be BLUE.
- Builds on: Two-variable multiple regression (earlier in this chunk)
- Continues in: Chunk 006 — Econometric problems (multicollinearity, heteroscedasticity, autocorrelation, MLE)
1. How many explanatory variables should a model include? (Partially answered by adjusted R² and t-values)

### Problem of Multi-co-linearity 🔴

**What Causes Multi-co-linearity?**
- The X matrix becomes **singular** (determinant → 0)
- (X'X)⁻¹ doesn't exist
- **Normal equations have no unique solution** → estimation fails

**Sources of Multicollinearity**
- Sample design: researchers may inadvertently select data with correlated Xs
- Model specification: including variables that are linear functions of each other
- Economic structure: many economic variables tend to move together (e.g., income, consumption, wealth)

**Consequences of Multi-co-linearity (Gujarati's List) ⭐**
| # | Consequence |
|---|-------------|
| 1 | **Large variances/SEs** of OLS estimates |
| 2 | **Wider confidence intervals** |
| 3 | **Insignificant t-ratios** for β coefficients (even if R² is high) |
| 4 | **High R² despite few significant t-values** (signature symptom!) |
| 5 | **Instability of OLS estimators**: sensitive to small data changes |
| 6 | **Wrong signs** on some coefficients (e.g., income negatively affects milk demand) |
| 7 | **Individual contributions to ESS cannot be assessed** properly |

**How to Detect Multi-co-linearity**
1. **High R² but few significant t-ratios** — the "classic symptom"
2. **High pairwise correlations** between explanatory variables
3. Partial correlations, auxiliary regressions (subsidiary regressions of each X on others)

**Multi-co-linearity: Key Nuance**
- **OLS still BLUE** even with imperfect multicollinearity — but practically, estimates are unreliable
- The problem is **sample-specific**: variables may not be correlated in the population, but the sample may create correlation
- More data (larger n) can reduce the problem
- **Multi-co-linearity**: Existence of exact or near-exact linear relationships between explanatory variables, vitiating the classical regression model assumption of linearly independent predictors. ⭐ (exam-important)
- **Perfect Multicollinearity**: When one X variable is an exact linear combination of other X variables → X matrix is singular → impossible to estimate OLS.
- **Imperfect Multicollinearity**: High but not perfect correlation between X variables → large SEs, unreliable estimates, wrong signs.

### ⚠️ Common Mistakes
- ❌ Mistake: Multicollinearity means OLS is always invalid → ✅ Correct: **Imperfect** multicollinearity still allows OLS (it's still BLUE), but estimates become imprecise; only *perfect* multicollinearity breaks OLS entirely
- ❌ Mistake: Multicollinearity only exists in the population → ✅ Correct: It is essentially a **sample problem** — X may be independent in population but correlated in the sample

**Quick Recall:**
- Multicollinearity = linear relationships among Xs
- **Signature**: High R², low t-values
- Perfect → OLS fails (no solution); Imperfect → OLS less reliable
- Consequences: large SEs, wide CIs, wrong signs, unstable estimates
- Detection: high pairwise correlations, high R² with few significant ts
- Builds on: Assumptions for n-variable model (Chunk 005)
- Related to: Heteroscedasticity, Autocorrelation (next two sections)

### Problem of Hetero-scedasticity 🔴

**The Homoscedasticity Assumption (Recall)**
- E(uᵢ²) = σ² for all i
- E(uᵢ²) = σᵢ² ≠ σ² (varies from one observation to another)

**Where Heteroscedasticity is More Common**
- **Cross-sectional data**: More likely (different-sized firms, different income levels)
- **Time series data**: Less common (usually well-behaved over time)

**Consequences of Heteroscedasticity**
| Consequence | Detail |
|-------------|--------|
| OLS still **linear** | ✅ |
| OLS still **unbiased** | ✅ |
| OLS **no longer BLUE** | ❌ No minimum variance — **true BLUE are WLS estimators** |
| σ̂² (estimator of σ²) | Biased → standard errors of β estimates are biased |
| Hypothesis tests (t, F) | **Unreliable** — wrong conclusions possible |

**How to Detect Heteroscedasticity**
- **Visual**: Plot residuals (eᵢ²) against Xᵢ — a "flaring out" or "funnel" pattern indicates heteroscedasticity
  - No pattern → homoscedasticity likely
  - Expanding/contracting fan → heteroscedasticity
- **Formal tests**: Park Test, Glejser Test, White's General Test, Spearman's Rank Correlation Test, Goldfeld-Quandt Test

**How to Tackle Heteroscedasticity**
- **Heteroscedasticity**: Violation of homoscedasticity; the variance of error terms differs across observations (σᵢ² ≠ σ²). ⭐ (exam-important)
- **Weighted Least Squares (WLS)**: Estimation method that corrects for heteroscedasticity by dividing each observation by √σᵢ, making error terms uniform variance.
- **Homoscedasticity**: The classical assumption that V(uᵢ) = σ² (constant) for all observations. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Heteroscedasticity makes OLS biased → ✅ Correct: OLS remains **unbiased but NOT BLUE** (loses minimum variance property)
- ❌ Mistake: Heteroscedasticity is mainly a time-series problem → ✅ Correct: It's primarily a **cross-sectional data** problem

**Quick Recall:**
- Heteroscedasticity: V(uᵢ) = σᵢ² (varies, not constant)
- OLS: still linear, still unbiased, **NOT BLUE anymore**
- σ̂² becomes biased → t and F tests unreliable
- Common in **cross-section** data, less in time-series
- Fix: WLS (if σᵢ² known), square-root/log transformation
- Builds on: Classical assumptions (Chunk 001), Gauss-Markov theorem (Chunk 002)
- Related to: Autocorrelation (next section)

### Problem of Autocorrelation 🔴

**What is Autocorrelation?**
- Classical assumption: **E(uᵢuⱼ) = 0** for i≠j
- Violation (autocorrelation): **E(uᵢuⱼ) ≠ 0** for some i≠j

**Causes of Autocorrelation**
| Cause | Explanation |
|-------|-------------|
| **Inertia** | Cyclical ups/downs in economic time series (GDP, employment) tend to persist |
| **Model misspecification** | Omitted variables create systematic patterns in residuals |
| **Cobweb phenomenon** | Agricultural price-quantity cycles create correlated errors |
| **Data manipulation** | Averaging monthly to quarterly data dampens fluctuations, creating artificial correlation |

**Consequences of Autocorrelation**
- OLS still **linear** and **unbiased** ✅
- OLS **no longer BLUE** ❌ (not minimum variance)
- t and F tests **unreliable**
- **R² is not a reliable measure of goodness of fit**

**Detection: Durbin-Watson (d) Test**
- d ranges from 0 to 4
- d ≈ 2 → no autocorrelation
- d ≈ 0 → positive autocorrelation
- d ≈ 4 → negative autocorrelation
- **Autocorrelation (Serial Correlation)**: Correlation between error terms at different time periods: E(uᵢuⱼ) ≠ 0 for i≠j. Violates classical assumption. ⭐ (exam-important)
- **Durbin-Watson d Test**: Most common test for autocorrelation. d = Σ(eₜ − eₜ₋₁)²/Σeₜ²; d ≈ 2 means no autocorrelation. ⭐ (exam-important)

**Quick Recall:**
- Autocorrelation: E(uᵢuⱼ) ≠ 0 for i ≠ j
- OLS: unbiased but **NOT BLUE**; t, F tests unreliable
- Common in **time-series** data (unlike heteroscedasticity)
- **Durbin-Watson d**: ≈2 = no problem; ≈0 = positive AC; ≈4 = negative AC

### Maximum Likelihood Estimation (MLE) 🔴

**MLE Method**
- Yᵢ is normally distributed with mean β₀ + β₁Xᵢ and variance σ²
- **Likelihood function (LF)**: The joint probability density of all observations:
- **Maximize log-likelihood** by differentiating w.r.t. β₀, β₁, σ² and setting equal to zero

**MLE vs OLS Comparison ⭐**
| Feature | OLS | MLE |
|---------|-----|-----|
| β estimates | b₀, b₁ | Same as OLS |
| σ² estimate | Σeᵢ²/(n−2) — **unbiased** | Σeᵢ²/n — **biased** (downward) |
| Assumption needed | 5 classical assumptions | 5 classical + normality |
| Theoretical strength | Moderate (BLUE under GM) | Stronger (asymptotic properties) |
| Practical preference | **Generally preferred** | Reserved for special cases |
- **Maximum Likelihood Estimation (MLE)**: Method that estimates parameters by maximizing the probability (likelihood) of observing the given sample data. ⭐ (exam-important)
- **Likelihood Function**: The joint probability density function of all observations viewed as a function of the unknown parameters.
- R² = 0.966; R̄² = 0.958 → Model explains ~96% of variation
- β̂(exports) = 1.263 (t = 12.192) → highly significant
- β̂(FDI) = −0.288 (t = −0.552) → insignificant
- F = 127.097 → overall model is significant
- R² = 0.468; R̄² = 0.349 → Only 35% explained → poor fit
- Coefficients insignificant → theoretical expectation not supported

**Quick Recall:**
- MLE maximizes likelihood function
- Under normality: **MLE β = OLS β** (identical!)
- But **MLE σ̂² is biased** (divides by n, not n−2)
- Therefore: stick with OLS + normality assumption
- Durbin-Watson signature: d ≈ 2 → OK; d < 2 → positive AC
- Builds on: Classical Normal Regression Model (Chunk 003)
- Related to: MLE mentioned also in Unit 9 summary (Chunk 004)
1. When would MLE be preferred over OLS (e.g., non-normal errors, limited dependent variable models)?
| Type | What it does | Examples |
|------|-------------|---------|
| **Positive** | Captures inequality without value judgments | Range, IQR, SD, Gini, Lorenz |
| **Normative** | Incorporates social welfare judgments | Dalton, Atkinson, Sen, Theil |

### Positive Measures of Inequality 🔴

**11.2.1: Relative Range (RR)**
- **RR₂ = (Max xᵢ − Min xᵢ) / (μN)** → lies in [0,1], gap between max and min income shares
- **RR₃ = (Max xᵢ − Min xᵢ) / Max xᵢ** → normalized by maximum
- **RR₄ = (Max xᵢ − Min xᵢ) / (Max xᵢ + Min xᵢ)** → normalized by sum
- RR₁ = 0 when everyone has equal income (perfect equality)
- RR₁ is maximum when one person has all income
- **Weakness**: Only uses extreme values (min and max) — ignores the entire middle of the distribution; any transfer between two non-extreme persons doesn't affect it

**11.2.2: Relative Inter-Quartile Range (Bowley's B)**
- B = 0 when all incomes are equal (degenerate distribution)
- B = 1 when lowest 75% have zero income
- **Weakness**: Uses only 50% of data (between Q1 and Q3); ignores transfers within Q1-Q3 range or beyond Q3

**11.2.3: Relative Standard Variation (RSD)**
- Also known as **coefficient of variation** when squared: **CV = (σ/μ)²**
- RSD = 0 when perfect equality
- Upper bound: (N−1)^(1/2) — depends on distribution size, NOT bounded in [0,1]
- **Advantage**: Sensitive to transfers at any level (uses all values)
- **Weakness**: Equally sensitive to transfers at all income levels (d transferred between rich vs poor changes RSD by equal amount)

**11.2.4: Standard Deviation of Logarithms (SDL)**
- Lower limit = 0 (perfect equality)
- Upper limit → ∞ as N → ∞
- **Advantage**: More sensitive to transfers at lower end (log "stretches" small income differences)
- **Critical weakness**: A transfer from rich to poor can **increase** measured inequality if the poor person's income is more than 2.72 times the mean. This is a serious logical flaw.
- **Variance of Logarithms (V₂)**: Square of SDL₂; is **decomposable** into between-group and within-group components

**11.2.5: Champernowne Index (CII)**
- Bounded in [0, 1]
- CII = 0 when everyone has equal income
- Sensitive to income transfers (especially at lower end)
- **Weakness**: Cannot be defined when any income = 0 (log of zero undefined)

**11.2.6: Hirschman-Herfindahl Indices (H)**
- Both measures depend on N (number of units) as well as inequality
- **H₃ = Σqᵢ² − 1/N** (adjusted version for N=2 case)
- For N=2, q₁=0.99, q₂=0.01: H₂ = 0.98 (better characterizes monopoly than H₃=0.48)

**11.2.7: Kolm's Index (K)**
- **Positive Measure of Inequality**: A statistical measure that captures the degree of inequality in a distribution without incorporating value judgments about social welfare. ⭐ (exam-important)
- **Relative Range (RR)**: (Max xᵢ − Min xᵢ)/μ; simplest inequality measure, but uses only extreme values.
- **Relative Standard Variation (RSD)**: σ/μ; uses all data points; equi-sensitive at all income levels.
- **Coefficient of Variation**: Square of RSD = (σ/μ)².
- **Champernowne Index**: 1 − (geometric mean / arithmetic mean); bounded in [0,1].
- **Herfindahl Index**: Σqᵢ² (sum of squared income shares); used in trade and market concentration analysis.
| Measure | Uses All Values? | Bounded [0,1]? | Transfer Sensitivity | Major Weakness |
|---------|-----------------|----------------|---------------------|----------------|
| Relative Range | ❌ (only extremes) | No (RR₁) | Only extreme transfers | Ignores middle |
| IQR / Bowley's B | ❌ (middle 50%) | Yes | Only middle 50% | Ignores extremes |
| RSD | ✅ | No ([0, √(N−1)]) | Equal at all levels | Not more sensitive at lower end |
| SDL | ✅ | No (0 to ∞) | Greater at lower end | Can violate Pigou-Dalton condition |
| Champernowne | ✅ | Yes | Greater at lower end | Undefined if any income = 0 |
| Herfindahl | Per unit | Bounded | --- | Depends on N |

### ⚠️ Common Mistakes
- ❌ Mistake: RSD is bounded between 0 and 1 → ✅ Correct: RSD = σ/μ can exceed 1; it's bounded by (N−1)^(1/2)
- ❌ Mistake: Transferring from rich to poor always reduces all inequality measures → ✅ Correct: SDL can *increase* if the poor person's income exceeds 2.72μ — a known flaw

**Quick Recall:**
- **Positive measures**: No value judgment — statistical dispersion only
- **RR**: Uses only extremes (max/min income) — weakest measure
- **RSD = σ/μ**: Uses all data; equi-sensitive at all income levels
- **Champernowne**: 1 − (geometric mean/arithmetic mean); bounded [0,1]
- **Herfindahl**: Σqᵢ² — from trade/market concentration analysis
- Leads to: Gini Index and Lorenz Curve (Chunk 008)
- Leads to: Normative Measures — Dalton, Atkinson, Sen, Theil (Chunk 009)
1. Which positive measure is most commonly used in practice for policy analysis — and why?

### Gini Index 🔴

**Gini as a Measure of Dispersion**
- ΣΣ|xᵢ − xⱼ| (summed over all i and j)
- Total number of pairs with replacement = N²
- ΣΣ|xᵢ − xⱼ| / N² → ranges from 0 to 2μ
- CMD = (1/μN²)ΣΣ|xᵢ − xⱼ| → ranges from 0 to 2

**Gini in Terms of Income Shares (qᵢ)**

**Gini Computational Device (via Lorenz Curve)**
- Pᵣ = cumulative proportion of population at class r
- Qᵣ = cumulative share of income at class r
- Sum is over all income groups g
1. Arrange data in increasing order of income
2. Compute cumulative population shares (P₁, P₂, …, Pg)
3. Compute cumulative income shares (Q₁, Q₂, …, Qg)
4. Plot Lorenz curve (Pᵣ on x-axis, Qᵣ on y-axis)
5. Calculate area under Lorenz curve (A) using trapezoid formula
6. G = 1 − 2A
- **Gini Index (G)**: Measure of income inequality equal to half the mean absolute difference between all pairs of incomes divided by mean income; bounded in [0, 1]. ⭐ (exam-important)
- **Coefficient of Mean Difference (CMD)**: Mean absolute difference between all pairs (including self comparisons); CMD = 2G · μ.
- **G = 1 − 2A**: Gini equals 1 minus twice the area under the Lorenz Curve — the most practical formula for computation. ⭐ (exam-important)
1. Lorenz curve lies in the unit square; diagonal OB = line of equality
2. Area under the diagonal OB = 1/2
3. Area between diagonal and Lorenz curve = 1/2 − A (where A = area under Lorenz curve)
4. Lorenz Coefficient of Concentration (LCC) = 2 × (Area between diagonal and curve) = 2(1/2 − A) = 1 − 2A
5. LCC = Gini = **G = 1 − 2A**

### ⚠️ Common Mistakes
- ❌ Mistake: Gini = 0 means zero income → ✅ Correct: Gini = 0 means **perfect equality** (everyone has the same income); Gini = 1 means one person has all income
- ❌ Mistake: Gini compares each income to the mean → ✅ Correct: Gini compares **all pairs** of incomes with each other — this is its distinctive feature

**Quick Recall:**
- Gini: compares **all pairs** (not just to mean)
- G = (1/2μN²)ΣΣ|xᵢ − xⱼ| → bounded [0, 1]
- G = 1 − 2A (area under Lorenz curve)
- G = 0: perfect equality; G = 1: perfect inequality
- Gini = Lorenz Coefficient of Concentration (LCC)
---

### Lorenz Curve 🔴

**Geometrical Definition**
- pⱼ = proportion of population in class j; qⱼ = income share of class j
- Pᵢ = Σⱼ pⱼ (cumulative population up to class i)
- Qᵢ = Σⱼ qⱼ (cumulative income share up to class i)
- First point: (0, 0) — 0% of people have 0% of income
- Last point: (1, 1) — 100% of people have 100% of income

**Properties of the Lorenz Curve ⭐**
| Property | Statement |
|---------|-----------|
| pⱼ ∈ [0,1]; qⱼ ∈ [0,1] for all j | All shares are fractions |
| P₀ = Q₀ = 0 | Starts at origin |
| P_N = Q_N = 1 | Ends at (1,1) |
| Qᵢ ≤ Pᵢ for all i | Curve is in lower triangle |
| Line of equality | OB (diagonal): Pᵢ = Qᵢ → no inequality |
| Line of perfect inequality | Triangle OAB (Lorenz = OAB boundary) → one person has all income |

**Using Lorenz Curve to Compare Distributions**
- **Non-intersecting curves**: The curve **closer to the diagonal** has **less inequality**
- **Intersecting curves**: Direct comparison is impossible — reducing to a scalar measure (like Gini) is needed
- If curves intersect, one distribution has more inequality in one income range and less in another

**Area-Based Measure (Lorenz Coefficient / Gini)**
- Area between diagonal and Lorenz curve → divided by area of triangle OAB (= 1/2)
- **LCC = 2 × (Area between diagonal and curve) = 1 − 2A = Gini G** ⭐

**Length-Based Measure (Kakwani's LK)**
- Length of egalitarian line (diagonal) = √2 (minimum possible curve length)
- Length of perfect inequality line (sides OA + AB) = 2 (maximum possible)
- LK = 0 when Lorenz curve = diagonal (perfect equality)
- LK = 1 when Lorenz curve = sides of triangle (perfect inequality)
- **Lorenz Curve**: A graphical tool plotting cumulative population share (P) against cumulative income share (Q), both in ascending order of income; invented by Max O. Lorenz (1905). ⭐ (exam-important)
- **Line of Equality (Egalitarian Line)**: The 45° diagonal OB; represents perfect equality where bottom X% of people earn exactly X% of total income. ⭐ (exam-important)
- **Line of Perfect Inequality**: The two sides of triangle OAB; represents one person holding all income.
- **Lorenz Coefficient of Concentration (LCC)**: = 2 × (area between diagonal and Lorenz curve) = Gini coefficient. ⭐ (exam-important)
- **Kakwani's LK**: Length-based inequality measure: LK = (ℓ − √2)/(2 − √2).
1. Arrange all income recipients in ascending order of income (poorest first)
2. Divide into classes (deciles, quintiles, etc.)
3. Compute pⱼ = class population / total population; qⱼ = class income share / total income
4. Compute cumulative Pᵢ = Σpⱼ; Qᵢ = Σqⱼ
5. Plot (Pᵢ, Qᵢ) points and connect them; also draw diagonal (egalitarian line)
6. The area between diagonal and the curve is the basis for Gini computation

### ⚠️ Common Mistakes
- ❌ Mistake: Lorenz curves that cross can still be compared by visual inspection → ✅ Correct: When Lorenz curves **intersect**, visual comparison fails; must use a numerical measure like Gini
- ❌ Mistake: Lorenz curve can be above the diagonal → ✅ Correct: Lorenz curve is **always below or on** the diagonal (Qᵢ ≤ Pᵢ always)

**Quick Recall:**
- Lorenz curve: X-axis = cumulative population share; Y-axis = cumulative income share
- Always lies below (or on) the 45° diagonal
- Diagonal OB = line of equality (Gini = 0)
- Triangle OAB = line of perfect inequality (Gini = 1)
- **G = 1 − 2A** (Gini = 1 minus twice area under Lorenz)
- Curves can't be compared when they intersect → use Gini
- Kakwani's LK = (ℓ − √2)/(2 − √2)
- Builds on: Gini Index (earlier in this chunk)
- Gini = Lorenz Coefficient of Concentration — they are intrinsically linked
- Leads to: Normative Measures (Chunk 009)
1. Why might two countries with the same Gini coefficient have very different distributions?

### Normative Measures of Inequality 🔴

**Three Issues in Normative Inequality Measurement**
1. Relationship between individual's income and their welfare (utility function U(xᵢ))
2. Relationship between personal income-welfare functions (same for all? different?)
3. Relationship between personal welfare and social welfare (additive? more complex?)

### 11.5.1 Dalton Index 🔴

**Dalton's Assumptions**
1. **Diminishing marginal utility**: ∂U/∂x > 0 (income increases welfare) but ∂²U/∂x² < 0 (at decreasing rate) → U(x) is concave
2. **Additive social welfare**: W = Σ U(xᵢ) (simple sum of individual welfares)
3. **Same welfare function for all**: U(xᵢ) = U(x) for all i → every person has identical income-welfare relationship

**Dalton's Index (D)**
- **D₃ = 1 − [ΣU(xᵢ)] / [N·U(μ)]** ⭐
- D = 0 when all incomes equal (maximum welfare)
- D > 0 when incomes are unequal (some welfare loss)
- Upper bound is not necessarily 1 (depends on welfare function shape)

**Dalton's Two Illustrations**
- **Dalton Index**: D = 1 − [ΣU(xᵢ)]/[N·U(μ)]; measures welfare loss from inequality; requires an explicit welfare function U(x). ⭐ (exam-important)
- **Diminishing Marginal Utility of Income**: ∂U/∂x > 0, ∂²U/∂x² < 0 — income increases welfare but at a decreasing rate; implies concave utility function.

**Quick Recall:**
- Dalton: social welfare = ΣU(xᵢ); U(x) is concave (diminishing marginal utility)
- Equal income → maximum social welfare
- D = 1 − [actual welfare / maximum possible welfare]
- Weakness: **Not invariant** to linear transformations of U → value changes with scale

### 11.5.2 Atkinson Index 🔴

**Key Concept: Four Income Vectors (Chart I)**
| Vector | Type | Description |
|--------|------|-------------|
| (a) | Actually distributed | {x₁, x₂, …, xₙ} — real distribution |
| (b) | Equally distributed | {μ, μ, …, μ} — everyone earns mean income |
| (c) | Equivalently distributed | {x₁*, x₂*, …, xₙ*} — same welfare as (a) but differently distributed |
| (d) | **Equally distributed equivalent** | {μ*, μ*, …, μ*} — equal AND same welfare as (a) |

**Atkinson Index**
- **A = 1 − μ*/μ** ⭐
- A = 0: perfect equality (μ* = μ)
- A → 1: maximum inequality (μ* → 0)
- **Bounded in [0, 1]** (approximately)
- Invariant to scale transformations (fixes Dalton's flaw)

**Iso-elastic Utility Function (Atkinson's Specification)**
| ε value | Utility function U(xᵢ) |
|---------|----------------------|
| ε ≠ 1 | α + β·xᵢ^(1−ε) |
| ε = 1 | log xᵢ |
- ε = 0 → linear utility → no aversion to inequality → A = 0 always (no information)
- ε increases → more weight to lower-income transfers
- As ε → ∞ → only the minimum income matters (Rawlsian)
- When ε → 1 → A = 1 − μ̂/μ (same as Champernowne Index)

**Atkinson vs Dalton**
| Feature | Dalton | Atkinson |
|---------|--------|---------|
| Basis | Welfare loss ratio | Equivalent income ratio |
| Scale invariant? | ❌ No (main flaw) | ✅ Yes |
| Requires welfare function? | Yes | Yes (restricted form) |
| Bounded in [0,1]? | Not always | Yes (approximately) |
- **Equally Distributed Equivalent Income (μ*)**: The per-capita income that, if equally distributed, generates the same social welfare as the current distribution. Always μ* ≤ μ. ⭐ (exam-important)
- **Atkinson Index**: A = 1 − μ*/μ; measures what fraction of income could be sacrificed if uniformly distributed to maintain the same social welfare. ⭐ (exam-important)
- **Inequality Aversion Parameter (ε)**: In Atkinson's formula, ε determines how much weight is given to income transfers at the bottom; ε = 0 → no concern; ε → ∞ → only the poorest matter. ⭐ (exam-important)

**Quick Recall:**
- μ* = "ethical mean" — per-capita wealth under equality with same welfare as today
- **A = 1 − μ*/μ** → A=0: equality; A→1: inequality
- Fixes Dalton's scale problem; requires ε > 0 for meaningful results
- ε = 1 → A = Champernowne Index (1 − geometric mean/arithmetic mean)

### 11.5.3 Sen Index 🔴
- x* = income level such that W(x*, x*, …, x*) = W(x₁, x₂, …, xₙ)
- Under quasi-concavity: x* ≤ μ
- Under utilitarian framework (additive W): **S = A** (Sen and Atkinson give same result)
- More general than Atkinson — doesn't require additive utility

**Quick Recall:**
- Sen: broad social welfare W(x₁,...,xₙ) — symmetric, quasi-concave
- **S = 1 − x*/μ** (same formula as Atkinson but more general W)
- Under additivity: S = A (same as Atkinson)

### 11.5.4 Theil Entropy Index 🔴

**Derivation from Information Theory**
- Perfect equality (qᵢ = 1/N for all i): **H = logN** (maximum entropy)
- Perfect inequality (qᵢ = 1 for one person, 0 for others): **H = 0** (minimum entropy)
- **T = logN − Σ qᵢ · log(1/qᵢ) = Σ qᵢ · log(N · qᵢ)** ⭐
- T = 0: perfect equality (H = logN)
- T = logN: maximum inequality (H = 0) → upper limit depends on N

**Properties of Theil Index**
- Lower limit: **T = 0** (perfect equality)
- Upper limit: **T = logN** (varies with population size — criticized as a weakness)
- **Decomposable**: Can be split into within-group and between-group inequality summands
- The changing upper limit is defended by Theil: "Inequality with 2 crore people, one having all, is greater than inequality with 2 people, one having all"
- Normalized version: **T' = T / logN** (used by some researchers to fix the upper limit at 1)
- **Theil Entropy Index**: T = Σ qᵢ log(Nqᵢ); measures inequality as deviation from maximum entropy; lower limit T=0, upper limit logN. ⭐ (exam-important)
- **Entropy**: Measure of randomness/evenness in information theory; maximum for equal distribution, minimum for most concentrated.
- **Decomposability**: Property that a measure can be broken into additive between-group and within-group components — crucial for policy analysis.
| Index | Formula | Range | Key Parameter | Decomposable? | Scale-Invariant? |
|-------|---------|-------|--------------|--------------|----------------|
| Dalton | 1 − ΣU(xᵢ)/N·U(μ) | [0, varies] | Welfare function U | No | ❌ |
| Atkinson | 1 − μ*/μ | [0, 1] | ε (aversion) | No | ✅ |
| Sen | 1 − x*/μ | [0, 1] | General W | No | ✅ |
| Theil | Σqᵢlog(Nqᵢ) | [0, logN] | — | ✅ | ✅ |

### ⚠️ Common Mistakes
- ❌ Mistake: Theil Index is always bounded by 1 → ✅ Correct: Upper bound is logN, which varies with the population size
- ❌ Mistake: Atkinson and Sen are always different → ✅ Correct: Under utilitarian (additive) social welfare, **S = A**

**Quick Recall:**
- **Theil T = Σ qᵢ log(Nqᵢ)** — from information theory (entropy)
- T = 0: equality; T = logN: maximum inequality
- Unique advantage: **Decomposable** (between-group + within-group)
- All 4 normative measures agree: equal distribution is better for social welfare
- **Key difference**: Dalton (not scale-invariant); Atkinson (ε determines aversion); Sen (general W); Theil (entropy, decomposable)
- All normative measures build on: Positive measures (Chunk 007), Lorenz Curve/Gini (Chunk 008)
- All share: U(x) concave → equal distribution better → inequality creates welfare loss
- Leads to: Unit 12 Composite Index (Chunks 010-013)

### Axioms of Inequality Measures 🔴

**General Desirable Properties of Any Statistical Measure**
1. Simplicity of comprehension
2. Ease of computation
3. Clear range of variation
4. Minimum data requirements

**1. Axiom of Scale Independence ⭐**

**2. Axiom of Population Size Independence ⭐**

**3. Axiom of Equal Income Addition ⭐**

**4. First Axiom of Income Transfer: Pigou-Dalton Condition ⭐**
- Transfer from person with income xₖ to person with income xⱼ (where xₖ > xⱼ)
- Transfer amount ≤ (xₖ − xⱼ)/2 (so rankings are preserved)
- Result: I(new distribution) < I(original distribution)

**5. Second Axiom of Income Transfer: Sen Condition ⭐**
- This axiom implies the Pigou-Dalton condition (but is stricter)
- Measures satisfying Sen Condition automatically satisfy Pigou-Dalton
- Gini and Theil satisfy the Pigou-Dalton condition; SDL/log variance can fail both conditions

**6. Axiom of Symmetry ⭐**

**7. Axiom of Interval ⭐**
- Minimum value = **0** (all incomes equal: perfect equality)
- Maximum value = **1** (one person has all income: perfect inequality)

**8. Axiom of Decomposability ⭐**
- Population A: (60,70,80) and (30,30,130) — group means same in A and B
- Population B: (60,60,90) and (10,60,120)
- Group inequalities in B > Group inequalities in A
- Yet **overall Gini in B < overall Gini in A** → paradox!
- **Pigou-Dalton Condition**: A transfer from a richer to a poorer person must strictly reduce the inequality measure (provided the transfer doesn't reverse income rankings). ⭐ (exam-important)
- **Sen Condition**: Transfer at a lower income level must have a greater inequality-reducing impact than an equal transfer at a higher level. ⭐ (exam-important)
- **Axiom of Scale Independence**: Inequality measure must be unchanged when all incomes are multiplied by a positive constant. ⭐ (exam-important)
- **Axiom of Decomposability**: Overall inequality can be expressed as a function of group-level inequalities; Theil satisfies this; Gini does not (when groups overlap). ⭐ (exam-important)
- **Population Replication**: Inequality unaffected by proportionate replication of all income groups.
| Axiom | Relative Range | Gini | Theil | Atkinson |
|-------|---------------|------|-------|---------|
| Scale Independence | ✅ | ✅ | ✅ | ✅ |
| Population Independence | ✅ | ✅ | ✅ | ✅ |
| Equal Income Addition | ❌ | ✅ | ✅ | ✅ |
| Pigou-Dalton | ❌ | ✅ | ✅ | ✅ |
| Sen Condition | ❌ | Partially | ✅ | ✅ (with ε>0) |
| Symmetry | ✅ | ✅ | ✅ | ✅ |
| Interval [0,1] | No | ✅ | ❌ (logN) | ✅ |
| Decomposability | ❌ | Partial | ✅ | ❌ |

### ⚠️ Common Mistakes
- ❌ Mistake: Gini satisfies all axioms → ✅ Correct: Gini fails decomposability when groups overlap (Cowell's paradox)
- ❌ Mistake: SDL always satisfies Pigou-Dalton → ✅ Correct: SDL can violate Pigou-Dalton if the poor recipient's income exceeds 2.72μ

**Quick Recall:**
1. **Scale Independence**: All incomes × constant → no change
2. **Population Replication**: Proportionate cloning → no change
3. **Equal Income Addition**: Same d to all → inequality ↓
4. **Pigou-Dalton**: Rich → Poor transfer (rank-preserving) → I ↓
5. **Sen Condition**: Lower-end transfer → greater I reduction
6. **Symmetry**: Permuting incomes → no change
7. **Interval**: I ∈ [0, 1]
8. **Decomposability**: Overall = f(group inequalities) [Theil: ✅; Gini: ❌ when groups overlap]
- Summarizes and synthesizes: All measures in Unit 11 (Chunks 007-009)
- Provides criteria for: Choosing which inequality measure to use in specific contexts
- Leads to: Unit 12 Composite Index (Chunks 011-013)

### Steps in Constructing Composite Index 🔴

**The 10 Steps (OECD Handbook Guidelines) ⭐**
| Step | Action | Purpose |
|------|--------|---------|
| **1. Theoretical framework** | Define the multidimensional phenomenon | Basis for selection; defining sub-groups (input/output) |
| **2. Data selection** | Select measurable, relevant indicators | Check quality; use proxies if scarce |
| **3. Imputation of missing data** | Estimate missing values | Prevent sample loss; identify extreme outliers |
| **4. Multivariate analysis** | Analyze data structure (e.g., PCA, cluster analysis) | Check suitability; group similar indicators; guide weighting |
| **5. Normalisation** | Render variables comparable | Put different units (e.g., %, ₹, ratios) onto a common scale |
| **6. Weighting & aggregation** | Combine variables | According to theory/data properties; handle correlations |
| **7. Uncertainty & sensitivity** | Test robustness | Multi-modeling; see how assumptions change the ranks |
| **8. Back to the data** | Deconstruct the index | Reveal main drivers of good/bad performance |
| **9. Links to other indicators** | Correlate with existing measures | Develop data-driven narratives; identify causal links |
| **10. Visualisation** | Present accurately | Enhance interpretability for target audience |

**Caution in Variable Selection**
- **Justification**: Every variable must be justified by empirical evidence, policy research, or theory.
- **Unidirectionality** ⭐: All variables must point in the same direction before combining. 
  - *Example*: If building a "Food Security Index", "per capita agricultural output" (positive) and "% of agricultural workers" (negative) clash.
  - *Fix*: Convert the negative one to positive (e.g., subtract from 100 to get "% of non-agricultural workers") OR convert the positive to negative (take reciprocal).
- **Composite Index**: A single score derived by combining multiple variables to measure a multi-dimensional concept (e.g., Human Development Index). ⭐ (exam-important)
- **Unidirectionality**: The requirement that all variables in an index must move in the same logical direction (all positive/developmental OR all negative/deprivational) before aggregation. ⭐ (exam-important)

### Dealing with Missing Values and Outliers 🔴

**Handling Missing Values**
1. **Option 1: Drop cases (Listwise deletion)**
   - **Risk**: Reduces sample size. If missingness correlates with a characteristic (e.g., poor households more likely to skip questions), dropping them biases the sample towards the upper classes.
   - **When to use**: Only if the frequency of missing values is random and exclusion has minimal impact on final results.
2. **Option 2: Imputation (Substitution)**
   - **Method A**: Substitute the overall sample average.
   - **Method B (Better)**: Group data by a known variable (e.g., asset holding category) and substitute the missing value with the average of *that specific group*.
   - **Advantage**: Maintains sample size; triangulates indices. Used by World Bank (WGI) and Transparency International (CPI).

**Handling Outliers**
- **Outlier**: An extreme value that drastically skews the mean (e.g., incomes: 18k, 17k, 18.5k, 19k, and one at 60k).
- **Action**: Drop extreme cases or transform them, as they can severely distort the index.
- **Rule of thumb**: Always document and explain the chosen imputation/deletion procedures.

### ⚠️ Common Mistakes
- ❌ Mistake: Always replace missing values with zero → ✅ Correct: Never replace with zero; use imputation (group averages) or drop the case.
- ❌ Mistake: It's fine to mix positive and negative variables when averaging → ✅ Correct: Variables MUST be made **unidirectional** before any aggregation.
---

### Methods to Construct Composite Index (Part 1) 🔴

**Method 1: Simple Ranking Method**
1. Convert all variables to unidirectional (e.g., all positive).
2. For each variable, rank the districts. (e.g., 1st rank to highest value, 11th rank to lowest value).
3. Sum the ranks for each district across all variables.
4. Calculate average rank = Sum of Ranks / Number of Variables.
5. **Interpretation**: District with the lowest average rank score (closest to 1) is the most developed; highest score is the most backward.

**Method 2: Indices Method**
1. Ensure unidirectionality.
2. Find the mean across all districts for Variable X.
3. Compute Index for District A = **(Actual Value of A / Mean Value of Variable) × 100**
4. Repeat for all variables.
5. **Composite Index** = Arithmetic mean of all the variable indices for that district.
6. **Interpretation**: District with the highest average index is the most developed.
- *Check*: You can run a correlation between Rank Method results and Indices Method results to verify robustness (e.g., r = 0.927 indicates high agreement).

**Method 3: Mean Standardization Method**
1. Normalize each value by dividing by the mean: **Normalized Value = Actual Value / Mean Value**
2. **Composite Index** = Average of the normalized values across all indicators for a district.
- **Simple Ranking Method**: An indexing method where actual values are replaced by their rank ordinal, and the composite score is the average of a unit's ranks across all variables. ⭐ (exam-important)
- **Indices Method**: Normalizes data by expressing each value as a percentage of the overall mean for that variable, then averaging these percentages to form the composite index. ⭐ (exam-important)

**Quick Recall:**
- To combine "Apples" and "Oranges", we normalize them.
- **Rank Method**: Uses ordinal positions (1st, 2nd, 3rd); simple but loses magnitude information.
- **Indices Method**: Value / Mean * 100.
- **Mean Standardization**: Value / Mean.
- Builds on: Basic statistical measures (mean, range)
- Leads to: More advanced index construction methods (Range Equalization, Principal Component Analysis) in Chunks 012 and 013.

### Methods to Construct Composite Index (Part 2) 🔴

**Method 4: Range Equalization Method (RE Method)**
1. **Purpose**: Normalizes variables so they all sit on a scale exactly between 0 and 1, preventing variables with large numerical ranges (e.g., income in thousands) from dominating variables with small ranges (e.g., literacy rates in percentages).
2. **Formula**: 
3. **Goalposts**: Instead of just using the sample's max and min, researchers often define theoretically desirable "goalposts" (e.g., Min literacy = 0%, Max literacy = 100%).
4. **Composite Index**: Average of the RE indices of all variables.

### Principal Component Analysis (PCA) 🔴

**When to use PCA?**
- Useful when you have an array of variables with **high correlation**.
- **Not suitable for categorical data** (e.g., Religion: 1=Hindu, 2=Muslim, 3=Christian). Categorical data must be converted to binary/dummy variables (e.g., Dalit=1, Non-Dalit=0) before using PCA.

**How PCA Works**
1. **Extracting Components**: PCA creates equations where each Principal Component (PC) is a linear combination of all the original variables (weighted by coefficients).
   - PC₁ = a₁₁X₁ + a₁₂X₂ + ... + a₁ₙXₙ
2. **Variance Explanation**: Components are ordered. 
   - **PC₁** explains the *largest* possible amount of variation in the data.
   - **PC₂** is completely uncorrelated to PC₁ and explains the second largest amount of variation, and so on.
3. **Eigenvalues (λ)**: The eigenvalue tells you how much variance is captured by that component. 
   - Total variance = Number of variables (if data is standardized).
   - Proportion of variation explained by PCᵢ = λᵢ / n.
   - *Rule of thumb*: We only keep components with an **Eigenvalue > 1**.

**Pre-PCA Checks**
1. **Correlation Matrix**: Variables should be correlated. If two variables are perfectly correlated, one should be removed.
2. **Kaiser-Meyer-Olkin (KMO) Test**: Measures sampling adequacy. Value should be close to 1 (minimum acceptable is 0.6).
3. **Bartlett's Test of Sphericity (BTS)**: Tests the null hypothesis that the correlation matrix is an identity matrix (variables are totally uncorrelated). We want this test to be **significant** (p < 0.05), allowing us to reject the null hypothesis and proceed with PCA.

**Output 1: Communalities**
- Shows the proportion of each variable's variance that is explained by the extracted components.
- Value ranges from 0 to 1. Closer to 1 = the variable is well-represented by the PCA model.
- If communality is very low, the variable doesn't fit well with the others and might need to be dropped or treated as a stand-alone variable.

**Output 2: Total Variance Explained**
- Lists the Eigenvalues for all components.
- Shows the % of variance explained by each component and the cumulative %.
- Example: If Component 1 explains 31.4% and Component 2 explains 21.8%, then cumulatively they explain 53.2% of the total variation in the data.

**Output 3: Scree Plot**
- A line graph plotting Component Number (X-axis) against Eigenvalue (Y-axis).
- The curve drops steeply at first and then flattens out.
- **Use**: Helps visually determine how many components to keep (usually the ones on the steep slope before it flattens).

**Output 4: Component Matrix**
- Shows the "loadings" (correlations) between the original variables and the extracted Principal Components.
- Values range from -1 to +1. High absolute values mean the variable is strongly associated with that component.
- The sum of squared loadings for a variable across the kept components equals its communality.
- **Principal Component Analysis (PCA)**: A mathematical data reduction technique that transforms a set of correlated variables into a smaller set of uncorrelated variables called principal components. ⭐ (exam-important)
- **Eigenvalue**: A number representing the amount of variance in the dataset explained by a specific principal component. ⭐ (exam-important)
- **KMO Test**: Kaiser-Meyer-Olkin measure of sampling adequacy; validates if data is suitable for PCA (should be ≥ 0.6).
- **Communalities**: The proportion of a variable's variation that is explained by the retained principal components.
- **Range Equalization (UNDP method)**: Index = (Actual − Min) / (Max − Min). ⭐ (exam-important)
1. Check correlations and convert categorical variables to binary.
2. Standardize data (optional but recommended; e.g., Value/Mean).
3. Run KMO and Bartlett's Test (ensure KMO > 0.6 and BTS is significant).
4. Run PCA extraction.
5. Review Communalities (drop items with very low values).
6. Review Total Variance Explained / Scree Plot (keep components where Eigenvalue > 1).
7. Review Component Matrix to understand which variables "load" onto which components.

### ⚠️ Common Mistakes
- ❌ Mistake: Using categorical classifications (like 1=General, 2=SC, 3=ST) directly in PCA → ✅ Correct: Convert to binary variables first (e.g., 1=ST, 0=Non-ST)
- ❌ Mistake: Keeping all principal components → ✅ Correct: Only keep components that capture significant variance (Eigenvalue > 1)

**Quick Recall:**
- PCA solves the problem of double-counting highly correlated variables.
- KMO test tells you if you *should* run PCA (>0.6).
- Eigenvalue tells you how much variance a component explains.
- PC1 always explains the most variance.
- Range Equalization sets everything between 0 and 1 using Max and Min goalposts (UNDP method).
- Builds on: Normalization techniques from Chunk 011.
- Leads to: Finalizing the composite index using PCA weights (Chunk 013).

### Finalizing PCA Index Value and Validation 🔴

**Reproducing Correlations and Analyzing Residuals (PCA Output 5)**
- **Reproduced Correlation**: The correlation between original variables as estimated by the extracted components.
- **Residual Matrix**: The difference between the *original* correlation and the *reproduced* correlation.
- **Quality Check**: For a robust PCA, the residuals should be **near zero**. If residuals are large, it means the extracted components failed to capture significant parts of the original relationships.

**Calculating the Final PCA Index Value**
- **x₁, x₂, ..., xₙ** = The *normalized* values of the variables for that district (from the Mean Standardization or Range Equalization step).
- **a₁₁, a₁₂, ..., a₁ₙ** = The Component Loadings (eigenvectors) for the *first principal component* (which explains the most variance).

**Validation: Use of Output Indicators**
- **Method**: Run a correlation between your newly created composite index and an independent "output" indicator that reflects the same underlying phenomenon but wasn't part of the index construction.
- **Example**: If you built a "District Development Index", an excellent external output indicator is the Infant Mortality Rate (IMR). 
- **Validation rule**: If the most backward districts (according to your index) have the highest IMR, your index is validated (high correlation). If the correlation is weak or contradicts reality, the index construction must be revisited.

### Weighting, Merits, and Limitations 🔴

**Approaches to Assigning Weights**
1. **Equal Weight Approach**: All variables are assigned the same weight (e.g., Range Equalization method example).
2. **Differential/Expert Weighting**: Weights are assigned based on theoretical importance, past research, or expert consensus. 
   - *Example*: In a sanitation index, "access to a toilet" might be deemed far more critical than "washing hands before eating," thus receiving a higher weight based on public health knowledge (Value/Expert Judgment).
3. **Statistical Weighting (PCA)**: Data drives the weighting. The variables that covary the most strongly with others receive the highest loadings.
4. **Mixed Approach (e.g., Human Development Index / Planning Commission)**: Sub-indices (like Health) might use differential weights for their components (Life expectancy=2/3, IMR=1/3), but the *overall* aggregate index averages those sub-indices using equal weights (1/3 for Health, 1/3 for Education, 1/3 for Income).

**Limitations of Principal Component Analysis (PCA)**
- **Arbitrariness**: The retention of components and variables is not governed by hard and fast rules (e.g., keeping components with eigenvalues > 1 is a rule of thumb, not a scientific law).
- **Dependence on PC1**: If the first principal component explains only a small fraction of the total variance (e.g., 15%), then using its loadings to create a unidimensional index is highly flawed. 
- **Alternatives**: Correspondence analysis, multivariate regression, or factor analysis.

**Merits of Composite Indices in General**
1. **Summarization**: Reduces complex, multi-dimensional indicators into a single, easy-to-understand number without losing underlying information.
2. **Policy utility**: Helps policymakers target interventions, allocate resources, and measure progress over time.
3. **Comparability**: Allows ranking and comparison of districts, states, or nations.
4. **Communication**: Easily communicated to the public, promoting transparency and political accountability.

**Limitations of Composite Indices in General**
1. **Misleading if poorly constructed**: A badly built index using flawed statistical principles sends the wrong policy message.
2. **Debatable Weights**: Especially when using value judgments, weight allocation is frequently criticized as subjective.
3. **Debatable Bounds**: In methods like Range Equalization, the choice of "Goalposts" (maximum and minimum bounds) can be subjective and dramatically alter rankings.
- **Residual Matrix (in PCA)**: The difference between the original correlation matrix and the reproduced correlation matrix; should be near zero for a good model.
- **Output Indicator (for validation)**: An independent, reliable variable (like Infant Mortality Rate) used to test whether the final composite index accurately reflects reality. ⭐ (exam-important)
1. Generate PC1 loadings from PCA output matrix.
2. Multiply loadings by normalized dataset variables for each unit.
3. Sum the products to get the raw PCA score.
4. Correlate raw PCA scores against a known output indicator.
5. If correlation is high → Validate and publish Index. If low → Re-evaluate variables, weights, or method.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing statistical weighting (like PCA) is perfectly objective → ✅ Correct: PCA is data-driven, but the choice of variables included in the dataset is still subjective, making the final weights sensitive to initial design choices.
- ❌ Mistake: Skipping external validation → ✅ Correct: Always validate an index against an independent output indicator to ensure it matches ground truth.

**Quick Recall:**
- PCA Index = Sum of (PC1 loading × Normalized Variable Value).
- Residuals in PCA should be near zero.
- Validation: correlate index with an "output indicator" (e.g., Dev Index vs. IMR).
- Weights can be equal (simple average), expert-driven (value judgment), or statistical (PCA).
- Advantage: Summarizes complexity for policy. Disadvantage: Subjective weight/goalpost debates.
- Completes the PCA and indexing process started in Chunk 011 and 012.
- Represents the final stage of Unit 12.
