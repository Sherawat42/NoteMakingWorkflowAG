# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

- **Estimation**: The process of recovering the unknown parameters (β₁, β₂) that were used to generate the sample data. ⭐ (exam-important)

**Quick Recall:**
- Three estimation methods: OLS, MOM, MLE
- PRF is unobservable; SRF is estimated
- Residual ûᵢ = Yᵢ − Ŷᵢ

### Classical Assumptions of OLS 🔴

**The Five Classical Assumptions**
1. **E(uᵢ) = 0** [Eq. 4.4]: The average error across the population is zero — positive errors cancel negative ones. This implies the regression line is correctly specified (no systematic bias).
2. **E(uᵢ²) = σ²** [Eq. 4.5]: The variance of the error term is constant (σ²) for all observations. This is **homoscedasticity**. Example: variance of consumption expenditure is the same for rich and poor.
3. **E(uᵢuⱼ) = 0 for i ≠ j** [Eq. 4.6]: Error terms of different observations are uncorrelated — **no autocorrelation**.
4. **E(Xᵢuᵢ) = 0** [Eq. 4.7]: The explanatory variable Xᵢ is not correlated with the error term. This requires Xᵢ to be **non-stochastic** (fixed in repeated samples) and exogenously given.
5. **uᵢ ~ N(0, σ²)** [Eq. 4.8]: The error follows a **normal distribution** with zero mean and constant variance. Required for hypothesis testing, NOT for OLS estimation itself.
- **Classical Regression Model**: A regression model satisfying all five classical assumptions about the error term. ⭐ (exam-important)
- **Homoscedasticity**: Constant variance of error term: E(uᵢ²) = σ² for all i. ⭐ (exam-important)
- **No Autocorrelation**: E(uᵢuⱼ) = 0 for i ≠ j — errors across observations are uncorrelated. ⭐ (exam-important)
- **Non-stochastic X**: The regressor Xᵢ is exogenous and fixed in repeated sampling, ensuring E(Xᵢuᵢ) = 0.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming all 5 assumptions are needed for OLS → ✅ Correct: Assumption (v) — normality — is NOT needed for OLS; it IS needed for hypothesis testing.
- ❌ Mistake: Confusing error term uᵢ with residual ûᵢ → ✅ Correct: uᵢ is the true (unknown) error; ûᵢ is the estimated residual.

**Quick Recall:**
- E(uᵢ) = 0 → zero mean
- E(uᵢ²) = σ² → homoscedasticity
- E(uᵢuⱼ) = 0, i≠j → no autocorrelation
- E(Xᵢuᵢ) = 0 → X is exogenous
- uᵢ ~ N(0, σ²) → normality (for t/F tests only)
- Continues into: OLS Method (Chunk 001), Matrix-form assumptions for multiple regression (Chunk 005)

### OLS Method of Estimation 🔴

**Principle of Least Squares**

**Normal Equations**

**OLS Estimators — Formulas**
- **RSS (Residual Sum of Squares)**: Σûᵢ² = Σ(Yᵢ − β̂₁ − β̂₂Xᵢ)² — quantity minimized by OLS. ⭐ (exam-important)
- **Normal equations**: Two simultaneous equations derived by setting ∂RSS/∂β̂₁ = 0 and ∂RSS/∂β̂₂ = 0. ⭐ (exam-important)
- **OLS estimator β̂₂**: β̂₂ = Σxᵢyᵢ / Σxᵢ² (slope). ⭐ (exam-important)
- **OLS estimator β̂₁**: β̂₁ = Ȳ − β̂₂X̄ (intercept). ⭐ (exam-important)
1. Write RSS = Σ(Yᵢ − β̂₁ − β̂₂Xᵢ)²
2. Take ∂RSS/∂β̂₁ = 0 → Normal Equation 1
3. Take ∂RSS/∂β̂₂ = 0 → Normal Equation 2
4. Solve simultaneously → β̂₁, β̂₂
- When s = 0 (illiterate): predicted wage = Rs. 0.89/hr
- When s = 8: predicted wage = 0.89 + 0.63(8) = Rs. 5.93/hr
- Each additional year of schooling → hourly wage increases by Rs. 0.63

### ⚠️ Common Mistakes
- ❌ Mistake: Using N in denominator for β̂₂ formula → ✅ Correct: β̂₂ = Σxᵢyᵢ / Σxᵢ² (deviation form)
- ❌ Mistake: Forgetting to convert to deviation form → ✅ xᵢ = Xᵢ − X̄, yᵢ = Yᵢ − Ȳ

**Quick Recall:**
- Minimize RSS → take derivatives → set to zero → solve normal equations
- β̂₂ = Σxᵢyᵢ / Σxᵢ²
- β̂₁ = Ȳ − β̂₂X̄
- Regression line passes through (X̄, Ȳ)
- Builds on: Classical Assumptions (this chunk)
- Extends to: Matrix form β̂ = (X'X)⁻¹X'Y for multiple regression (Chunk 005)
- **Method of Moments**: An estimation method that equates population moments (derived from model assumptions) with sample moments to obtain parameter estimates. ⭐ (exam-important)

**Quick Recall:**
- MOM uses E(uᵢ) = 0 and E(Xᵢuᵢ) = 0 as moment conditions
- MOM and OLS produce identical estimators for bivariate regression

### Maximum Likelihood Method (MLE) 🔴

**Likelihood Function for Regression**

**Log-Likelihood Maximization**

**MLE of σ² — Biased Result**
- **Likelihood Function L(·)**: The joint probability of observing the sample data as a function of unknown parameters β₁, β₂, σ². ⭐ (exam-important)
- **Maximum Likelihood Estimates (MLEs)**: Parameter values that maximize L(·); for β₁ and β₂ they equal OLS estimates.
- **Biased MLE of σ²**: σ̃² = RSS/n is biased downward; uses n instead of (n−2). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking MLE always gives different estimates than OLS → ✅ Correct: Under normality, MLEs of β₁, β₂ are identical to OLS; only σ² estimate differs.
- ❌ Mistake: Using MLE σ̃² = RSS/n for inference → ✅ Correct: Use unbiased σ̂² = RSS/(n−2) for hypothesis testing.

**Quick Recall:**
- MLE of β₁, β₂ = OLS estimators (under normality)
- MLE of σ² = RSS/n → biased but consistent
- OLS estimator of σ² = RSS/(n−2) → unbiased
- Equivalent to OLS for β̂: OLS Method (this chunk)
- MLE σ̃² discussed further: Standard Error section (Chunk 002)

### Interpretation of OLS Estimators 🔴

**Linear Model: Yᵢ = β₁ + β₂Xᵢ + uᵢ**

**Semi-Log Model: ln Yᵢ = β₁ + β₂Xᵢ + uᵢ**

**Double-Log (Log-Linear) Model: ln Yᵢ = β₁ + β₂ ln Xᵢ + uᵢ**
| Model Type | Y | X | β₂ Interpretation |
|------------|---|---|-------------------|
| Linear | Levels | Levels | ΔY per unit ΔX |
| Semi-log | ln Y | Levels | % change in Y per unit ΔX |
| Double-log | ln Y | ln X | Elasticity (% ΔY per % ΔX) |
- **Semi-log model**: Regression where only the dependent variable is in logarithmic form; β₂ gives % change in Y per unit change in X. ⭐ (exam-important)
- **Double-log / Log-linear model**: Both variables in log form; β₂ is a constant elasticity. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Interpreting β₂ as elasticity in a linear model → ✅ Correct: Elasticity interpretation applies only to double-log models.

**Quick Recall:**
- Linear: β₂ = ΔY per unit ΔX
- Semi-log: β₂ = % ΔY per unit ΔX
- Double-log: β₂ = elasticity (% ΔY per % ΔX)
- Builds on: OLS Method (this chunk)
- Continues into: Standard Error of Estimators (Chunk 002)
1. Wage example in CYP1 Q2 (n=526 workers) — compute β̂₂ and interpret.

### Standard Error of OLS Estimators 🔴

**Variance of β̂₂**
- Greater variation in X values → larger Σxᵢ² → smaller var(β̂₂) → more precise β̂₂
- Larger sample size → larger Σxᵢ² → smaller variance

**Variance of β̂₁**

**Estimator of Error Variance (σ̂²)**
- **Standard Error (se)**: The positive square root of an estimator's variance; measures precision of the estimator. ⭐ (exam-important)
- **Unbiased estimator of σ²**: σ̂² = RSS/(n−2) — uses (n−2) degrees of freedom for simple regression. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Using σ̃² = RSS/n (MLE) for inference → ✅ Correct: Use σ̂² = RSS/(n−2) for unbiased standard errors.
- ❌ Mistake: Thinking more X variability increases estimation error → ✅ Correct: More variability in X (larger Σxᵢ²) reduces var(β̂₂).

**Quick Recall:**
- var(β̂₂) = σ²/Σxᵢ² → wider X spread = more precision
- var(β̂₁) = σ²·ΣXᵢ²/(n·Σxᵢ²)
- σ̂² = RSS/(n−2) → unbiased; σ̃² = RSS/n → biased (MLE)
- se = √var(·)
- Builds on: OLS estimators β̂₁, β̂₂ (Chunk 001)
- Used in: Hypothesis testing (this chunk), Confidence intervals (this chunk)

### Properties of OLS Estimators — Algebraic & Statistical 🔴

**Algebraic Properties of OLS (Numerical — always hold)**
1. OLS provides **point estimates** — one value per parameter.
2. The regression line passes through the **sample means** (X̄, Ȳ): Ȳ = β̂₁ + β̂₂X̄.
3. Mean of predicted values = mean of actual values: Ȳ̂ = Ȳ ... (4.45).
4. The SRF in **deviation form**: ŷᵢ = β̂₂xᵢ ... (4.49).
5. The **residual ûᵢ and Ŷᵢ are uncorrelated**: Σŷᵢûᵢ = 0 ... (4.50).
6. The **residual ûᵢ and Xᵢ are uncorrelated**: ΣXᵢûᵢ = 0.

**Statistical Properties: Unbiasedness**

**Statistical Properties: Efficiency (Gauss-Markov Theorem)**
- Let b₂ = Σdᵢyᵢ be any linear unbiased estimator with Σdᵢxᵢ = 1 (unbiasedness condition).
- var(b₂) = Σdᵢ²·σ². Minimize this subject to Σdᵢxᵢ = 1 using Lagrangian.
- Solution: dᵢ = xᵢ/Σxᵢ² = cᵢ → this is exactly the OLS weight.
- Therefore, minimum-variance linear unbiased estimator is the OLS estimator. ✓

**BLUE Summary**
- **Linear**: β̂₂ = Σcᵢyᵢ where cᵢ = xᵢ/Σxᵢ²
- **Unbiased**: E(β̂₂) = β₂
- **Minimum Variance**: among all linear unbiased estimators
- **Unbiased estimator**: E(β̂) = β; the expected value equals the true parameter. ⭐ (exam-important)
- **Efficient estimator**: Minimum variance in its class of estimators.
- **Consistent estimator**: As n → ∞, the estimator converges in probability to the true parameter.
- **BLUE**: Best Linear Unbiased Estimator — OLS is BLUE under CLRM. ⭐ (exam-important)
- **Gauss-Markov Theorem**: "Given CLRM assumptions, OLS estimators have minimum variance in the class of all linear unbiased estimators." ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Requiring normality for Gauss-Markov → ✅ Correct: Gauss-Markov does NOT require normality of errors.
- ❌ Mistake: OLS is always best → ✅ Correct: BLUE only if all 5 CLRM assumptions hold; violated homoscedasticity breaks this.

**Quick Recall:**
- Algebraic: passes through (X̄, Ȳ); Ȳ̂ = Ȳ; ΣûᵢXᵢ = 0; Σûᵢ = 0
- Statistical: Unbiased [E(β̂₂) = β₂], Consistent, Efficient (BLUE)
- Gauss-Markov: OLS is BLUE under CLRM (no normality needed)
- Statistical properties hold regardless of sample size
- Builds on: Classical Assumptions (Chunk 001)
- Extended to matrix form: Chunk 006 (Gauss-Markov for multiple regression)

### Goodness of Fit — Coefficient of Determination (r²) 🔴

**TSS, ESS, RSS Decomposition**
| Component | Formula | Meaning |
|-----------|---------|---------|
| TSS (Total SS) | Σ(Yᵢ − Ȳ)² | Total variation of Y around its mean |
| ESS (Explained SS) | Σ(Ŷᵢ − Ȳ)² = β̂₂²·Σxᵢ² | Variation explained by regression |
| RSS (Residual SS) | Σûᵢ² | Unexplained variation |

**r² Definition and Interpretation**
- 0 ≤ r² ≤ 1 always
- r² = 1 → perfect fit (all points on regression line)
- r² = 0 → no linear relationship between Y and X
- **TSS (Total Sum of Squares)**: Σ(Yᵢ − Ȳ)² — total variation in Y around its mean. ⭐ (exam-important)
- **ESS (Explained Sum of Squares)**: Σ(Ŷᵢ − Ȳ)² — variation explained by the regression model.
- **RSS (Residual Sum of Squares)**: Σûᵢ² — unexplained variation; minimized by OLS. ⭐ (exam-important)
- **Coefficient of Determination r²**: r² = ESS/TSS; proportion of total variation in Y explained by X. ⭐ (exam-important)

**Quick Recall:**
- TSS = ESS + RSS
- r² = ESS/TSS = 1 − RSS/TSS ∈ [0, 1]
- Higher r² → better fit
- Note: r² for bivariate; R² for multiple regression
- Builds on: OLS Algebraic Properties (this chunk) — uses Σŷᵢûᵢ = 0
- Extended to: Adjusted R² for multiple regression (Chunk 007)
- Used in: F-test (Chunk 007)

### Hypothesis Testing — t-Test for Regression Coefficients 🔴

**t-Statistic for β̂₂**

**Two-Tailed Test**
- H₀: β₂ = β₂* vs H₁: β₂ ≠ β₂*
- Reject H₀ if |t| > t(α/2, n−2)
- t(α/2) = 2.306 → CI = [0.2177, 0.3823]
- Since β̂₂ = 0.5091 falls outside CI → **Reject H₀**
- Verified: t = (0.5091 − 0.3)/0.0357 = 5.86 > 2.306 ✓

**One-Tailed Test**
- H₀: β₂ ≤ β₂* vs H₁: β₂ > β₂* → right-tail test
- H₀: β₂ ≥ β₂* vs H₁: β₂ < β₂* → left-tail test
- Critical value at 5%: t(α, n−2) = t₀.₀₅; one tail only
| Type | H₀ | H₁ | Reject H₀ if |
|------|----|----|-------------|
| Two-tail | β₂ = β₂* | β₂ ≠ β₂* | \|t\| > t(α/2, df) |
| Right-tail | β₂ ≤ β₂* | β₂ > β₂* | t > t(α, df) |
| Left-tail | β₂ ≥ β₂* | β₂ < β₂* | t < −t(α, df) |
- **Level of significance (α)**: Probability of rejecting H₀ when it is true (Type I error); typically 0.05 or 0.01. ⭐ (exam-important)
- **Critical region**: The region of t-values for which H₀ is rejected; defined by critical values t(α/2) or t(α).
- **Degrees of freedom (df)**: For simple regression: n−2.

### ⚠️ Common Mistakes
- ❌ Mistake: Using two-tailed critical values for a one-tailed test → ✅ Correct: One-tailed at 5% uses t₀.₀₅ (not t₀.₀₂₅).
- ❌ Mistake: Rejecting H₀ when |t| < critical value → ✅ Correct: Reject only when |t| > critical value.

**Quick Recall:**
- t = (β̂₂ − β₂*)/se(β̂₂) ~ t(n−2)
- Two-tailed: reject if |t| > t(α/2, df)
- 95% CI: β̂₂ ± t(α/2)·se(β̂₂)
- Larger |t| → stronger evidence against H₀
- Builds on: Standard Error of OLS Estimators (this chunk)
- Extended to: t-test for multiple regression (Chunk 007)

### Forecasting — Mean and Individual 🔴

**Mean Forecasting: E(Y|X₀)**

**Individual Forecasting: Y₀**

**Width of Confidence Band**
| Forecast Type | Variance Formula | Band Width |
|---------------|-----------------|------------|
| Mean forecast | σ²[1/n + (X₀−X̄)²/Σxᵢ²] | Narrower |
| Individual forecast | σ²[1 + 1/n + (X₀−X̄)²/Σxᵢ²] | Wider |
- **Mean forecasting**: Predicting the conditional mean E(Y|X₀); point on the regression line. ⭐ (exam-important)
- **Individual forecasting**: Predicting a specific Y₀ for given X₀; higher variance than mean forecast.
- **Forecast error variance**: var(Y₀ − Ŷ₀) = σ²[1 + 1/n + (X₀ − X̄)²/Σxᵢ²].

### ⚠️ Common Mistakes
- ❌ Mistake: Using mean forecast formula for individual prediction → ✅ Correct: Individual forecast has extra σ² term (the "+1").
- ❌ Mistake: Treating all X₀ values as equally reliable → ✅ Correct: Prediction accuracy decreases as X₀ departs from X̄.

**Quick Recall:**
- Mean forecast CI < Individual forecast CI (always)
- Both CIs widen as X₀ moves from X̄
- Caution in extrapolation beyond observed X range
- Unit 4 summary: OLS, MOM, MLE → same β̂; Classical properties; r²; t-test; forecasting
- Builds on: OLS estimation (Chunk 001), Standard errors (this chunk)
- This completes Unit 4
1. CYP 3 Q1: Compute r² from wage-schooling data (CYP 1 Q2)
2. CYP 3 Q2: Test H₀: β₂ = 0 using computed r²
3. CYP 3 Q3: Why does predictive capacity decrease as X₀ moves from X̄?

### Residuals — Definition and Properties 🔴

**Residual vs Error Term**
| Concept | Symbol | Nature | Observable? |
|---------|--------|--------|-------------|
| Error term | uᵢ | True gap from PRF | No (theoretical) |
| Residual | ûᵢ or eᵢ | Estimated gap from SRF | Yes (computed) |

**Algebraic Properties of Residuals**
1. **Σûᵢ = 0** — sum of residuals is zero (they cancel out)
2. They measure the **unaccounted-for variability** in Y that the model couldn't explain
- **Residual (ûᵢ or eᵢ)**: ûᵢ = Yᵢ − Ŷᵢ; the difference between observed and predicted Y. ⭐ (exam-important)
- **Observed vs Predicted**: Yᵢ is observed; Ŷᵢ = β̂₁ + β̂₂Xᵢ is predicted/fitted.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating residuals as the same as error terms → ✅ Correct: uᵢ is theoretical (unobservable); ûᵢ is computable from sample data.

**Quick Recall:**
- ûᵢ = Yᵢ − Ŷᵢ
- Σûᵢ = 0 (always)
- Patterns in residuals → assumption violations
- Builds on: OLS definition of RSS (Chunk 001)
- Used in: All residual plots below

### Residual Plot — Patterns and Interpretation 🔴

**Residual Plot Against Xᵢ — Three Patterns (Fig. 5.1)**
| Pattern | Shape | Inference |
|---------|-------|-----------|
| (a) Random | Cloud around zero axis | ✅ Linear model appropriate |
| (b) U-shaped | Curve — residuals dip then rise | ❌ Non-linear relationship |
| (c) Inverted-U | Curve — residuals rise then dip | ❌ Non-linear relationship |

**Residual Plot Against Ŷᵢ — Five Patterns (Fig. 5.2)**
|---------|-------|-----------|
| (a) Horizontal band | Residuals randomly within a band | ✅ No model defect |
| (b) Outward funnel | Variance increases with Ŷᵢ | ❌ Heteroscedasticity (σ²ᵤ increases) |
| (c) Inward funnel | Variance decreases with Ŷᵢ | ❌ Heteroscedasticity (σ²ᵤ decreases) |
| (d) Double bow | Residuals form two curves | ❌ Binomial Y; non-linear relationship; variance proportional to Ŷ(1−Ŷ) |
| (e) Curved shape | Single curve pattern | ❌ Non-linearity; higher-order X terms or log transformation needed |

**Residual Plot Over Time (Fig. 5.3)**
- Random band → ✅ No temporal autocorrelation
- Funnel shape → ❌ Variance changing over time
- Double bow / non-linear → ❌ Relationship is not stable; add linear/quadratic time terms
- (a) Horizontal band → no model defects
- (b) Funnel shape → non-constant variance (heteroscedasticity)
- (c) Double bow / nonlinear → assumed relationship incorrect or Y may be proportion, higher-order terms needed
- **Residual plot**: A scatter diagram with ûᵢ on the Y-axis and Xᵢ or Ŷᵢ on the X-axis, used to visually diagnose regression model assumptions. ⭐ (exam-important)
- **Horizontal band pattern**: Residuals randomly within a constant-width band around zero — indicates correct model specification. ⭐ (exam-important)
- **Funnel shape pattern**: Residuals form an expanding or contracting shape — indicates heteroscedasticity (non-constant error variance). ⭐ (exam-important)
- **Double bow pattern**: Residuals enclosed in two curves — suggests Y may follow binomial distribution or that the relationship is non-linear with variance proportional to Ŷ(1−Ŷ).

### ⚠️ Common Mistakes
- ❌ Mistake: Random residuals in ûᵢ vs Ŷᵢ plot means no problems → ✅ Correct: Also need to check temporal plots and normality (not just Ŷᵢ).
- ❌ Mistake: All non-linear patterns require a log transformation → ✅ Correct: Non-linearity could also be resolved by adding higher-order terms or omitted variables.

**Quick Recall:**
- Random band around zero → ✅ Good model
- Funnel → ❌ Heteroscedasticity
- U-shape / Inverted-U → ❌ Non-linearity
- Double bow → ❌ Non-linear; Y possibly bounded [0,1]
- Temporal funnel → ❌ Time-varying variance
- Best diagnostic: visual examination of residual plots
- Builds on: Residuals definition (this chunk)
- Continues into: Formal normality tests (Chunk 004)
- Related to: Heteroscedasticity (Unit 11, mentioned in Chunk 005)
| Type | Description |
|------|-------------|
| Positive outlier | Value much higher than typical data; e.g., sudden sales spike |
| Negative outlier | Value much lower than typical data; e.g., unexpected loss |
| Multivariate outlier | Not obvious in single variable; visible in multi-variable relationships |
- **Outlier**: An observation with a notably large residual that deviates substantially from the typical pattern; can be influential on OLS estimates. ⭐ (exam-important)

**Quick Recall:**
- Outlier → large ûᵢ → disproportionate OLS penalty
- Detect via scatter plot, box plot, residual examination
- Re-estimate without suspected outlier to assess influence

**Quick Recall:**
- Visual diagnosis is preliminary; formal tests must follow
- Funnel residual plot → heteroscedasticity
- Patterns in time plot of residuals → autocorrelation
- ACF/PACF plots: significant spikes → autocorrelation

### Testing for Normality of Errors 🔴

**P-P Plot (Probability-Probability Plot)**
- Scatter plot of **theoretical normal percentiles** (x-axis) vs **sample residual percentiles** (y-axis)
- Reference line: 45-degree diagonal
- If all points lie on the diagonal → normal distribution ✅
- Deviations from diagonal → non-normal distribution ❌

**Jarque-Bera (JB) Test**
- n = sample size
- S = sample skewness (measure of asymmetry)
- K = sample kurtosis (measure of tail heaviness)
- **P-P Plot (Probability-Probability Plot)**: A scatter plot comparing theoretical normal quantiles (x-axis) with sample residual quantiles (y-axis); points on 45° line → normality. ⭐ (exam-important)
- **Jarque-Bera (JB) Test**: Formal test of normality using sample skewness (S) and kurtosis (K); JB ~ χ²(2) under H₀ of normality. ⭐ (exam-important)
- **Skewness (S)**: Measure of asymmetry of a distribution; S = 0 for normal distribution.
- **Kurtosis (K)**: Measure of tail heaviness; K = 3 for normal distribution (mesokurtic). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Using JB test on small samples → ✅ Correct: JB is designed for large samples; use other tests for small n.
- ❌ Mistake: JB = 0 always requires exact normality → ✅ Correct: JB ≈ 0 under H₀; any departure increases JB.
- ❌ Mistake: Confusing kurtosis K with excess kurtosis → ✅ Correct: For normality, K = 3 (not excess kurtosis = 0).

**Quick Recall:**
- CNLRM assumes uᵢ ~ N(0, σ²)
- P-P plot: points on 45° diagonal → normal
- JB = (n/6)[S²/6 + (K−3)²/24]; H₀: normality; ~ χ²(2)
- JB ≈ 0 under normality (S→0, K→3)
- JB > χ² critical value → reject normality
- JB valid for large samples only
- Builds on: Classical assumption (v) — normality (Chunk 001)
- Related to: t-test and F-test validity (which require normality)
- **Zero-intercept model**: Yᵢ = βXᵢ + uᵢ; OLS with intercept constrained to zero. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Comparing R² of intercept vs no-intercept models → ✅ Correct: R² definitions differ; not directly comparable.
- ❌ Mistake: Assuming Σûᵢ = 0 for zero-intercept model → ✅ Correct: This property holds ONLY when intercept is included.

**Quick Recall:**
- Zero-intercept: Yᵢ = βXᵢ + uᵢ; uses raw (not mean-adjusted) sums
- Σûᵢ = 0 only guaranteed with intercept in model
- R² of models with/without intercept NOT comparable
- Only omit intercept if strong theoretical reason
- **Change of origin**: Subtracting a constant from variable values; does NOT affect regression coefficients. ⭐ (exam-important)
- **Change of scale**: Multiplying/dividing variable values by a constant; DOES affect regression coefficients. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking R² changes when you change units → ✅ Correct: R² is invariant to any unit changes.
- ❌ Mistake: Change of origin changes slope → ✅ Correct: Only scale changes affect slope.

**Quick Recall:**
- R² → invariant to origin and scale changes
- Origin change (subtract c) → coefficients unchanged
- Scale change (multiply Y by c) → both β̂₁ and β̂₂ multiply by c
- Intercept always in Y-units
- Standardize variables to get unit-free coefficients

### Multiple Regression Model — Specification & Advantages 🔴

**General Multiple Regression Model**
- β₁ = intercept (X₁ = 1 for all observations by convention)
- β₂, …, βₖ = partial regression coefficients
- uᵢ = stochastic error term

**Advantages of Multiple Regression (CYP 1 Q1)**
1. **Control for multiple factors simultaneously**: Avoids omitted variable bias present in bivariate models.
2. **Ceteris paribus interpretation**: Isolates the effect of one X on Y while holding other X's constant.
3. **Eliminates correlation bias**: Reduces bias from correlation between error term and explanatory variables (common in two-variable models).
4. **General functional form**: Allows flexible specification of cause-effect relationships.
5. **Higher R²**: More explanatory variables → explains more variation in Y.

**Ceteris Paribus Interpretation**
- **Multiple regression model**: A regression model with one dependent variable and two or more independent variables. ⭐ (exam-important)
- **Ceteris paribus**: "All other things being equal" — holding other explanatory variables constant when interpreting one coefficient. ⭐ (exam-important)
- **Partial regression coefficient (βₖ)**: The change in Y per unit change in Xₖ, holding all other X's constant.

### ⚠️ Common Mistakes
- ❌ Mistake: Adding more variables always improves the model → ✅ Correct: More variables always increase R², but may hurt adjusted R² and introduce multicollinearity.

**Quick Recall:**
- Multiple regression: Yᵢ = β₁ + β₂X₂ᵢ + … + βₖXₖᵢ + uᵢ
- β₁ is intercept (X₁ = 1); βₖ is partial coefficient of Xₖ
- k variables → k normal equations
- Key advantage: ceteris paribus interpretation
- Extends: Bivariate OLS (Chunk 001)
- Simplified by: Matrix algebra (this chunk)

### Matrix Representation of Multiple Regression 🔴

**The Y = Xβ + U Notation**

**Matrix Dimensions — Must Memorize**
| Matrix | Dimension | Contents |
|--------|-----------|----------|
| Y | n × 1 | Dependent variable values |
| X | n × k | Xᵢⱼ = value of jth regressor at ith obs |
| β | k × 1 | k parameters to be estimated |
| U | n × 1 | Error terms |
- **Design matrix X (n×k)**: Matrix of all explanatory variable values; each row = one observation, each column = one regressor. ⭐ (exam-important)
- **Parameter vector β (k×1)**: Column vector of all regression parameters [β₁, …, βₖ]'. ⭐ (exam-important)
- **Error vector U (n×1)**: Column vector of stochastic error terms.

**Quick Recall:**
- Y = Xβ + U (n×1) = (n×k)(k×1) + (n×1) — dimensions check out
- X is (n×k): n observations, k regressors (including intercept column)
- β is (k×1), U is (n×1)
- Always track matrix dimensions!
- Builds on: Multiple Regression Specification (this chunk)
- Used in: Classical Assumptions and OLS derivation below

### Classical Assumptions for Multiple Regression 🔴

**Assumption 1: E(U) = 0 ... (6.5)**

**Assumption 2: E(UU') = σ²I ... (6.6)**
- **Diagonal elements**: E(uᵢ²) = σ² → **homoscedasticity** (constant variance)
- **Off-diagonal elements**: E(uᵢuⱼ) = 0 for i ≠ j → **no autocorrelation**
| | u₁ | u₂ | … | uₙ |
|---|---|---|---|---|
| u₁ | σ² | 0 | … | 0 |
| u₂ | 0 | σ² | … | 0 |
| uₙ | 0 | 0 | … | σ² |

**Assumption 3: X Has Full Rank ... (6.7)**

**Assumption 4: E(X'U) = 0 ... (6.8)**
- **Homoscedasticity (matrix form)**: var(uᵢ) = σ² for all i — diagonal elements of E(UU') = σ²I. ⭐ (exam-important)
- **Heteroscedasticity**: var(u₁) ≠ var(u₂) ≠ … ≠ var(uₙ) — non-constant error variance; discussed in Unit 11.
- **No autocorrelation**: E(uᵢuⱼ) = 0 for i ≠ j — off-diagonal elements of E(UU') = 0.
- **Full rank**: Rank(X) = k — all regressors are linearly independent; no perfect multicollinearity. ⭐ (exam-important)
- **Variance-covariance matrix of U**: E(UU') — (n×n) matrix; equals σ²I under CLRM assumptions.

### ⚠️ Common Mistakes
- ❌ Mistake: E(UU') = σ² (scalar) → ✅ Correct: E(UU') = σ²**I** (identity matrix scaled by σ²).
- ❌ Mistake: If X lacks full rank, we can still estimate β → ✅ Correct: (X'X)⁻¹ doesn't exist without full rank → OLS formula breaks down.

**Quick Recall:**
- E(U) = 0 → zero mean errors
- E(UU') = σ²I → homoscedastic + no autocorrelation
- Full rank X → X'X invertible → OLS exists
- E(X'U) = 0 → X is exogenous (non-stochastic)
- Extends: Five classical assumptions (Chunk 001) to matrix form
- Used in: OLS derivation below, Gauss-Markov proof (Chunk 006)
- Violations: Heteroscedasticity (Unit 11), Autocorrelation (Unit 12), Endogeneity (Unit 13)

### OLS Estimation in Matrix Form 🔴

**Minimizing RSS in Matrix Form**

**Normal Equations: X'Xβ̂ = X'Y**

**OLS Estimator: β̂ = (X'X)⁻¹X'Y**
- **β̂ = (X'X)⁻¹X'Y** ... (6.15) ⭐

**Variance of β̂: var(β̂) = σ²(X'X)⁻¹**
- **Normal equations (matrix form)**: X'Xβ̂ = X'Y — the k equations obtained by minimizing RSS w.r.t. β̂. ⭐ (exam-important)
- **OLS estimator (matrix form)**: **β̂ = (X'X)⁻¹X'Y** — requires X to have full rank. ⭐ (exam-important)
1. Write RSS = Û'Û = (Y − Xβ̂)'(Y − Xβ̂)
2. Expand to Y'Y − 2β̂'X'Y + β̂'X'Xβ̂
3. Differentiate w.r.t. β̂, set = 0 → −2X'Y + 2X'Xβ̂ = 0
4. Rearrange: X'Xβ̂ = X'Y (normal equations)
5. Pre-multiply by (X'X)⁻¹: β̂ = (X'X)⁻¹X'Y

### ⚠️ Common Mistakes
- ❌ Mistake: ∂(β̂'X'Xβ̂)/∂β̂ = 2β̂'X'X → ✅ Correct: Result is 2X'Xβ̂ (eliminate β̂', keep β̂)
- ❌ Mistake: β̂ = (X'X)⁻¹X' (missing Y) → ✅ Correct: β̂ = **(X'X)⁻¹X'Y**

**Quick Recall:**
- RSS = Û'Û = Y'Y − 2β̂'X'Y + β̂'X'Xβ̂
- Normal equations: X'Xβ̂ = X'Y
- OLS formula: **β̂ = (X'X)⁻¹X'Y** ← most important formula
- var(β̂) = σ²(X'X)⁻¹
- Builds on: Matrix representation, Classical Assumptions (this chunk)
- Continues into: Chunk 006 (Variance derivation, BLUE proof)
- CYP 1 Q2 (variance formula), Q4 (why full rank needed)

### Properties of OLS Estimators — Unbiasedness, Consistency & Efficiency 🔴

**Unbiasedness of β̂**

**Variance-Covariance Matrix of β̂**
- = **σ²(X'X)⁻¹** ... (6.21) ⭐
- Diagonal elements: var(β̂ₖ) for each coefficient
- Off-diagonal elements: cov(β̂ᵢ, β̂ⱼ) between pairs of coefficients

**Estimator of Error Variance σ̂² (Unbiased)**
- M' = M (symmetric)
- MM = M (idempotent)
- MX = 0 → so Û = MU (not MXβ)
- **Unbiased estimator**: E(β̂) = β; OLS estimator is unbiased under CLRM. ⭐ (exam-important)
- **Consistent estimator**: β̂ converges in probability to β as n → ∞. ⭐ (exam-important)
- **Asymptotic properties**: Properties of estimators as n → ∞; consistency is an asymptotic property.
- **Idempotent matrix M**: M = I − X(X'X)⁻¹X'; satisfies MM = M; used to express residuals.

### ⚠️ Common Mistakes
- ❌ Mistake: Degrees of freedom for multiple regression = n−2 → ✅ Correct: df = n−k (k = total parameters including intercept).
- ❌ Mistake: var(β̂) = σ² (scalar) → ✅ Correct: var(β̂) = **σ²(X'X)⁻¹** (a k×k matrix).

**Quick Recall:**
- E(β̂) = β → unbiased (uses E(U) = 0 and X non-stochastic)
- var(β̂) = σ²(X'X)⁻¹ → k×k variance-covariance matrix
- σ̂² = RSS/(n−k) → unbiased estimator of σ²
- df = n−k for multiple regression
- CYP 1 Q3: Derive var(β̂) = σ²(X'X)⁻¹
- Builds on: OLS formula β̂ = (X'X)⁻¹X'Y (Chunk 005)
- Used in: Gauss-Markov proof (this chunk)

### Gauss-Markov Theorem — OLS is BLUE 🔴

**Setup: Any Linear Unbiased Estimator β̃ = CY**

**Condition for Unbiasedness: CX = I ... (6.34)**

**Variance of β̃**

**Comparing var(β̂) and var(β̃) — The Key Step**
- **BLUE (Best Linear Unbiased Estimator)**: Among all linear unbiased estimators, OLS has the smallest variance-covariance matrix. ⭐ (exam-important)
- **Gauss-Markov Theorem**: Under CLRM assumptions, OLS is BLUE; does NOT require normality of errors. ⭐ (exam-important)
- **Positive semi-definite matrix**: A matrix A where x'Ax ≥ 0 for all x; ensures var(β̃) ≥ var(β̂).
1. Assume any linear unbiased estimator β̃ = CY with CX = I
2. Write C = (X'X)⁻¹X' + D where DX = 0
3. Compute CC' = (X'X)⁻¹ + DD'
4. var(β̃) = σ²CC' = σ²(X'X)⁻¹ + σ²DD'
5. Since DD' ≥ 0 (positive semi-definite): var(β̃) ≥ var(β̂) ✓

### ⚠️ Common Mistakes
- ❌ Mistake: Gauss-Markov requires normality → ✅ Correct: No distributional assumption needed; only CLRM assumptions required.
- ❌ Mistake: OLS is BLUE even with heteroscedasticity → ✅ Correct: Violation of E(UU') = σ²I breaks the BLUE property; GLS becomes better.

**Quick Recall:**
- Gauss-Markov: OLS is BLUE under CLRM (no normality needed)
- Proof: var(β̃) − var(β̂) = σ²DD' ≥ 0 (positive semi-definite)
- BLUE: Best (minimum var) + Linear + Unbiased + Estimator
- Breaks down if: heteroscedasticity, autocorrelation, endogeneity
- Bivariate version: Gauss-Markov via Lagrangian (Chunk 002)
- Matrix version extends to k variables (this chunk)
- CYP 2 Q2 & Q3 ask to prove OLS is BLUE and show properties
- This completes Unit 6

### Goodness of Fit in Multiple Regression — R² & Adjusted R² 🔴

**R² = ESS/TSS in Multiple Regression**

**Problem: Over-Fitting (R² Always Increases)**
- **R² ALWAYS increases** (even if the variable is irrelevant)
- This incentivizes researchers to keep adding variables — which is statistically unsound
- Models with many variables lose interpretability and degrees of freedom

**Adjusted R² (R̄²) Formula and Properties**
- ESS = 1383.16, TSS = 1480.00
- R² = 1383.16/1480.00 = **0.93**
- R̄² = 1 − (1 − 0.93)·(5−1)/(5−3) = 1 − 0.07·2 = **0.86**

**Four Properties of Adjusted R² (R̄²)**
| Property | R² | R̄² |
|----------|----|----|
| When variables added | Always increases | May rise or fall |
| Incentive to over-fit | Yes | No (penalizes weak variables) |
| Relationship | — | R̄² ≤ R² always |
| Can be negative? | No (always ≥ 0) | Yes (can be negative) |
- **R² (coefficient of determination)**: ESS/TSS; proportion of variation in Y explained by all regressors jointly. ⭐ (exam-important)
- **Adjusted R² (R̄²)**: R̄² = 1 − (1 − R²)·(n−1)/(n−k); penalizes for adding extra regressors; preferred over R². ⭐ (exam-important)
- **TSS, ESS, RSS**: Total, Explained, Residual Sums of Squares — TSS = ESS + RSS.

### ⚠️ Common Mistakes
- ❌ Mistake: Higher R² always means better model → ✅ Correct: Adding irrelevant variables inflates R²; use R̄² to compare.
- ❌ Mistake: R̄² is always between 0 and 1 → ✅ Correct: R̄² can be **negative** (unusual but possible).
- ❌ Mistake: Comparing R² across models with different Y → ✅ Correct: R² comparison requires **same dependent variable**.

**Quick Recall:**
- R² = ESS/TSS = 1 − RSS/TSS ∈ [0,1]
- R̄² = 1 − (1−R²)·(n−1)/(n−k) ≤ R²
- R̄² may be negative; R² never is
- R² always ↑ with more variables; R̄² may ↓
- CYP 1 Q4: R² increases even with useless variables; R̄² is the solution
- Extends: r² in bivariate regression (Chunk 002)
- Used in: F-test formulas (this chunk)
- Related to: F-test via R² formula (equation 7.19)

### Hypothesis Testing — t-Test for Individual Coefficients 🔴

**t-Statistic for βₖ (General)**

**Two-Tailed Test (Most Common): H₀: βₖ = 0**

**One-Tailed Test: H₀: βₖ ≤ βₖ⁰, H₁: βₖ > βₖ⁰**

**t-Ratio in Software Output**
- **t-ratio**: bₖ/se(bₖ); t statistic testing H₀: βₖ = 0; follows t(n−k). ⭐ (exam-important)
- **One-tailed test**: Tests directional hypothesis (> or <); critical value at full α level.
- **Two-tailed test**: Tests non-directional hypothesis (≠); critical value at α/2 level.

### ⚠️ Common Mistakes
- ❌ Mistake: Two-tailed 5% critical value is 1.64 → ✅ Correct: 1.64 is for one-tailed; 1.96 is for two-tailed at 5%.
- ❌ Mistake: Degrees of freedom for t-test = n−2 → ✅ Correct: For multiple regression with k parameters, df = n−k.

**Quick Recall:**
- tₖ = bₖ/se(bₖ) ~ t(n−k) under H₀: βₖ = 0
- Two-tailed: reject if |tₖ| > 1.96 (large n, 5%)
- One-tailed: reject if tₖ > 1.64 (large n, 5%)
- Large |t| → bₖ significant → Xₖ matters for Y
- Extends: bivariate t-test (Chunk 002)
- se(bₖ) comes from: diagonal of var(β̂) = σ²(X'X)⁻¹ (Chunk 006)

### Confidence Interval for βₖ 🔴

**Confidence Interval from t-Distribution**

**Standard Normal Approximation (Large n)**
- **Confidence interval**: Range of βₖ values for which t-test does not reject H₀: βₖ = βₖ⁰; provides plausible values for true βₖ. ⭐ (exam-important)

**Quick Recall:**
- 95% CI: bₖ ± 1.96·se(bₖ) [large n]
- CI inversion: all βₖ⁰ where |tₖ| ≤ 1.96
- Wider CI → larger se → less precise estimate
- Extends: bivariate CI (Chunk 002)

### F-Test — Joint Significance of Regression Coefficients 🔴

**F-Test: Full vs Restricted Model**
- **RSS₁**: RSS of full (unrestricted) model
- **RSS₀**: RSS of restricted model (J regressors dropped)

**F-Statistic Formula (RSS form)**

**F-Statistic Formula (R² form)**

**Special Case: All Slope Coefficients = 0**
- **F-test**: Joint significance test for J restrictions on β; uses F-distribution. ⭐ (exam-important)
- **Restricted model**: Model with J regressors removed (all set to zero) — tested under H₀.
- **Unrestricted model**: Full model with all k regressors.
- **F-distribution**: F ~ F(J, n−k); critical values one-sided even though H₁ is two-sided.

### ⚠️ Common Mistakes
- ❌ Mistake: F-test rejects H₀ → model is definitely good → ✅ Correct: Rejection only means ≥1 variable is significant; doesn't validate the overall model.
- ❌ Mistake: F-distribution is two-sided → ✅ Correct: F critical values are **one-sided** (always reject for large F).

**Quick Recall:**
- F tests J coefficients jointly (t tests one at a time)
- F = [(RSS₀−RSS₁)/J] / [RSS₁/(n−k)] ~ F(J, n−k)
- F in R²: [(R₁²−R₀²)/J] / [(1−R₁²)/(n−k)]
- Special case all slopes = 0: F = [R²/(k−1)] / [(1−R²)/(n−k)]
- Large F → reject H₀ → at least one regressor significant
- Uses: RSS and R² from goodness of fit (this chunk)
- Compared with: t-test (single restriction) vs F-test (multiple restrictions)
- Extends to: Wald/LM/LR tests for restrictions (Chunk 008)

### Testing Linear Restrictions on Multiple Parameters 🔴

**General Linear Restriction: Rβ = q**

**Cobb-Douglas Example: Constant Returns to Scale**
- **Linear restriction**: A constraint of the form Rβ = q imposed on regression parameters; more general than single-parameter restrictions.

**Quick Recall:**
- t-test: tests βₖ = 0 (one restriction at a time)
- Linear restrictions: Rβ = q (multiple coefficients constrained)
- Cobb-Douglas constant returns: β₂ + β₃ = 1
- Three test methods: Wald, LM, LR → Chunk 008
- Continues into: Chunk 008 (Wald, LM, LR Test derivations)
- CYP 3 Q1: Describes the need for testing beyond single parameters

### Wald Test for Linear Restrictions 🔴

**Wald Statistic Formula**

**Based on Unrestricted Model Only**

**Wald Test vs t-Test**
| Feature | t-Test | Wald Test |
|---------|--------|-----------|
| Number of restrictions | 1 | J ≥ 1 |
| What it tests | βₖ = 0 | Rβ = q |
| Model required | Unrestricted | Unrestricted only |
| Distribution | t(n−k) | χ²(J) |
- **Wald test**: Tests J linear restrictions Rβ = q using unrestricted model estimates only; W ~ χ²(J). ⭐ (exam-important)
- **Wald statistic W**: W = (Rb − q)'[R(X'X)⁻¹R']⁻¹(Rb − q)/s²; measures distance of Rb from q.

### ⚠️ Common Mistakes
- ❌ Mistake: Wald test requires restricted model → ✅ Correct: Only **unrestricted** model needed; this distinguishes Wald from LR test.

**Quick Recall:**
- Wald: unrestricted model only
- Tests Rβ = q; W ~ χ²(J)
- Logic: if H₀ is true, Rb ≈ q; large W → reject H₀
- Advantage: no restricted model estimation needed
- Builds on: Linear restrictions Rβ = q (Chunk 007)
- Contrasts with: LM test (restricted only) and LR test (both)
- CYP 3 Q2: Define Wald test

### Lagrange Multiplier (LM) Test 🔴

**LM Test Logic — Score Test**

**Based on Restricted Model Only**
- LM test requires only the **restricted parameter estimates θ̃**
- At the unrestricted MLE, q(θ̂ᵤ) = 0 by definition; at restricted MLE, q(θ̃) ≠ 0 unless restriction is true
- **Lagrange Multiplier (LM) test**: Score test based on restricted model only; tests if the score at restricted estimates is significantly non-zero; LM ~ χ²(J) under H₀. ⭐ (exam-important)
- **Score function q(θ)**: ∂L(θ)/∂θ; gradient of log-likelihood; = 0 at unconstrained MLE; ≠ 0 at restricted MLE if restrictions are wrong.

### ⚠️ Common Mistakes
- ❌ Mistake: LM test requires both models → ✅ Correct: LM requires only the **restricted model** (contrast with LR which needs both).

**Quick Recall:**
- LM: restricted model only
- Tests if score ≠ 0 at restricted estimates
- LM ~ χ²(J) under H₀
- Equivalent to: "Are the Lagrange multipliers significantly different from zero?"
- Contrasts with: Wald (unrestricted only), LR (both models)
- CYP 3 Q3: Compare Wald and LM model requirements

### Likelihood Ratio (LR) Test 🔴

**LR Statistic Formula**

**Requires Both Restricted and Unrestricted Models**

**Degrees of Freedom = Number of Restrictions**
- **Likelihood Ratio (LR) test**: Tests J restrictions by comparing log-likelihood of unrestricted vs restricted model; LR ~ χ²(J). ⭐ (exam-important)
- **LR statistic**: LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)]; always ≥ 0 since restricted likelihood ≤ unrestricted.

### ⚠️ Common Mistakes
- ❌ Mistake: LR requires only one model → ✅ Correct: LR requires **both** restricted and unrestricted MLE estimates.
- ❌ Mistake: df for LR = number of parameters → ✅ Correct: df = **number of restrictions** J, not total parameters.

**Quick Recall:**
- LR: both models needed (unrestricted AND restricted)
- LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)] ~ χ²(J)
- df = number of restrictions J
- Cannot test simple H₀ vs H₁ (df would be 0)
- Tests whether new variables improve log-likelihood
- Contrasts with: Wald (unrestricted only), LM (restricted only)
- CYP 3 Q4 & Q5: Define LR test and why df = J

### Comparison — Wald, LM, LR Tests 🔴

**Which Model Each Test Requires**
| Test | Model Required | Statistic | Distribution |
|------|---------------|-----------|-------------|
| **Wald** | Unrestricted only | W = (Rb−q)'[R(X'X)⁻¹R']⁻¹(Rb−q)/s² | χ²(J) |
| **LM** | Restricted only | LM = q̃'Ĩ⁻¹q̃ | χ²(J) |
| **LR** | Both models | LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)] | χ²(J) |
- **W**ald → needs the **W**hole (unrestricted) model
- **LM** → needs the **L**imited (restricted) model only
- **LR** → needs **L**eft and **R**ight (both) models

**Asymptotic Equivalence**
- t(sales) = 0.2803/0.0353 = **7.94** → |t| > 1.96 → **significant**
- t(roe) = 0.0174/0.0041 = **4.25** → |t| > 1.96 → **significant**
- t(ros) = 0.0002/0.0005 = **0.44** → |t| < 1.96 → **not significant**

### ⚠️ Common Mistakes
- ❌ Mistake: The three tests always give the same result in finite samples → ✅ Correct: They are equivalent only asymptotically; finite sample results may differ.

**Quick Recall:**
- All three test H₀: Rβ = q; all ~ χ²(J)
- Wald: unrestricted only | LM: restricted only | LR: both
- Asymptotically equivalent for large n
- In practice: use whichever model is easier to estimate
- CEO salary: sales and roe significant; ros not significant; model overall significant (F = 26.91)
- Builds on: All of Unit 7 (t-test, F-test, linear restrictions)
- This completes Unit 7 and Block 2
1. Q1: t-test covers single restriction; need Wald/LM/LR for multiple (e.g. β₂ + β₃ = 1 in Cobb-Douglas).
2. Q2: Wald test based on unrestricted estimates; advantage = no restricted model needed.
3. Q3: LM requires restricted model only (contrast with Wald requiring unrestricted).
4. Q4: LR tests whether new variables improve log-likelihood; requires both models.
5. Q5: LR df = number of restrictions (parameters reduced by restrictions).
