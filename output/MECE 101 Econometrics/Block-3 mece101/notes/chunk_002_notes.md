# Chunk 002 — Model Selection Criteria & Autocorrelation Intro
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

## Section: Model Selection Criteria 🟡
<!-- This section continues from chunk 001 -->

### Core Idea
While $R^2$ is a basic measure of fit, sophisticated models require penalized criteria like Adjusted-$R^2$, AIC, SIC, or Mallow's $C_p$ to prevent overfitting and ensure the model is parsimonious and theoretically sound.

> **In Simple Terms:** Because $R^2$ can be "cheated" by just adding more variables (even useless ones), statisticians invented stricter scoring systems that deduct points for every extra variable you add.

### Key Concepts

#### Adjusted R-squared
The adjusted-$R^2$ ($\\bar{R}^2$) introduces a penalty for adding regressors. It only increases if the absolute t-value of the newly added regressor is greater than 1.
- Unlike $R^2$, $\\bar{R}^2$ can decrease if an irrelevant variable is added.
- $\\bar{R}^2 \\le R^2$ always.
- Comparison using $\\bar{R}^2$ is only valid between models with the exact same dependent variable.

#### AIC and SIC Criteria
- **Akaike Information Criterion (AIC)**: Based on maximum likelihood estimation, it evaluates both in-sample fit and out-of-sample forecasting performance. It is useful for non-nested models and determining lag lengths. A lower AIC value indicates a better model.
- **Schwartz Information Criterion (SIC)**: Also known as the Bayesian Information Criterion (BIC). It imposes a harsher penalty for adding regressors than the AIC. Like AIC, a lower value signifies a better model.

#### Mallow's $C_p$ Criterion
This criterion helps select a model following the principle of parsimony. You want a model with $p$ regressors (where $p < k$ total available regressors) that provides a good fit. A model with a lower $C_p$ value, approximately equal to $p$, is selected.

#### Cautions about Model Selection
Empirical criteria cannot replace theoretical reasoning. A high correlation might be "spurious" (superficial) or "confounded" (where a third unobserved variable drives both the independent and dependent variables, e.g., traffic rules causing both the lights to change and cars to stop). If different test criteria suggest different models, the researcher must rely on logic, common sense, and theoretical literature to make the final choice.

### Definitions
- **Adjusted R-squared ($\\bar{R}^2$)**: A modified version of $R^2$ that penalizes the addition of explanatory variables that do not significantly improve the model's fit.
- **AIC Criterion**: A model selection tool that balances the goodness of fit with the complexity of the model, defined as $\\ln AIC = (2k/n) + \\ln(RSS/n)$.
- **SIC Criterion**: A stricter model selection criterion compared to AIC, where the penalty factor grows logarithmically with sample size, defined as $\\ln SIC = (k/n)\\ln(n) + \\ln(RSS/n)$.
- **Mallow's $C_p$**: A model selection criterion that aims for parsimony, aiming for $C_p \\approx p$.

### Mechanisms / Processes
**Comparing Models:**
1. Calculate the chosen criteria (e.g., AIC, SIC) for all competing models.
2. Select the model with the **lowest** AIC or SIC value.
3. Ensure the selected model makes logical and theoretical sense to avoid spurious relationships.

> **Quick Recall:**
> - $R^2$ always increases with more variables; Adjusted-$R^2$ penalizes extra variables.
> - For AIC, SIC, and Mallow's $C_p$: **Lower is better.**
> - Statistical criteria can never substitute economic theory and common sense.

### Connections
- Builds on: Model Selection Criteria (Chunk 001)

## Section: Concept of Autocorrelation 🔴

### Core Idea
Autocorrelation violates the classical regression assumption that error terms are independent. In time series data, successive observations often share an underlying momentum, causing their error terms to be correlated with one another over time.

> **In Simple Terms:** Autocorrelation means yesterday's mistake affects today's mistake. If the stock market drops today because of panic, that same panic will likely cause it to drop tomorrow too. The errors are carrying over.

### Key Concepts

#### Spatial Correlation
This is correlation found in cross-sectional data. For example, a household's consumption might be influenced by its neighbors ("keeping up with the Joneses"), meaning the error terms across different households are correlated.

#### Serial Correlation / Autocorrelation
This refers specifically to correlation between error terms in time series data. 
**Causes include:**
- Non-stationarity of the series (mean/variance changes over time).
- Omission of a relevant variable (the error term absorbs its systematic effect).
- Incorrect functional form (fitting a straight line to a curve creates a pattern in errors).
- Interpolation and extrapolation of data.
- Inertia or lagged effects (e.g., current consumption heavily depends on past habits).

### Definitions
- **Autocorrelation**: The correlation between successive error terms in a dataset, most commonly in time series data. Mathematically, $E(u_i, u_j) \\neq 0$ for $i \\neq j$. ⭐ (exam-important)
- **First order autocorrelation**: The correlation between the error term at time $t$ ($u_t$) and the immediately preceding error term ($u_{t-1}$).
- **Spatial Correlation**: Correlation between error terms in cross-sectional data due to geographic or social proximity.

### Mechanisms / Processes
**Modeling Autocorrelation:**
- **Auto-regressive AR(1) process**: The current error depends on a proportion of the previous error plus a random shock.
  $u_t = \\rho u_{t-1} + \\varepsilon_t$
  (Where $\\rho$ is the coefficient of autocovariance, and $\\varepsilon_t$ is a random shock).
- **Moving Average MA(1) process**: The current error depends on the current random shock plus a proportion of the previous period's random shock.
  $u_t = \\varepsilon_t + \\rho_1 \\varepsilon_{t-1}$

### ⚠️ Common Mistakes
- ❌ Mistake: Believing autocorrelation only happens when the model is mathematically wrong. → ✅ Correct: It often happens simply due to the nature of time-series data (momentum, inertia, changing habits).

> **Quick Recall:**
> - Autocorrelation = $E(u_i, u_j) \\neq 0$.
> - AR(1) formula: $u_t = \\rho u_{t-1} + \\varepsilon_t$.
> - Causes: omitted variables, wrong functional form, inertia, data manipulation.

### Connections
- Prerequisite for: Consequences of Autocorrelation (Chunk 002)

## Section: Consequences of Autocorrelation 🔴
<!-- This section continues into chunk 003 -->

### Core Idea
When autocorrelation is present, ordinary least squares (OLS) estimators remain linear and unbiased, but they lose their minimum variance property (they are no longer BLUE). Consequently, the calculated standard errors are incorrect, invalidating standard hypothesis tests.

> **In Simple Terms:** Your estimates will still be "correct" on average, but they become wildly unpredictable. Because the standard error formulas don't know about the hidden correlation, your confidence in the results is falsely high.

### Key Concepts

#### Unbiasedness
Despite autocorrelation, $E(\\hat{\\beta}) = \\beta$ continues to hold. This is because the core assumptions $E(u_t) = 0$ and $E(x_tu_t) = 0$ are still valid. The OLS estimator centers around the true parameter value.

#### Minimum Variance
The variance of the error term in an AR(1) process is $Var(u_t) = \\frac{\\sigma_\\varepsilon^2}{1-\\rho^2}$. 
The covariance between error terms is $Cov(u_t, u_{t-s}) = \\rho^s \\frac{\\sigma_\\varepsilon^2}{1-\\rho^2}$.
Because the error terms are correlated, the OLS variance formula underestimates the true variance of the estimator. For these formulas to hold, we must assume $|\\rho| < 1$. If $|\\rho| \\ge 1$, we encounter the "unit root problem" (non-stationarity).

### Definitions
- **White noise**: A purely random error term ($\\varepsilon_t$) that has a zero mean, constant variance, and no covariance with other periods. ⭐ (exam-important)

### Mechanisms / Processes
**Why variance is inflated:**
The true variance of the estimator $\\hat{\\beta}$ must account for the covariance between all error terms. Because $Cov(u_t, u_{t-s})$ is non-zero, the sum of these covariances inflates the overall variance, making the estimator inefficient compared to one that corrects for this correlation.

<!-- This section continues in chunk 003 -->
