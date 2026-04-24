# Chunk 007 — Heteroscedasticity Remedies and Errors in Variables Intro
<!-- Pages: 62-71 -->
<!-- Source: chunk_007.txt -->

## Section: Detection of Heteroscedasticity 🔴
<!-- This section continues from chunk 006 -->

### Core Idea
White's test is a highly general test for heteroscedasticity, but its comprehensiveness comes with a significant cost to degrees of freedom and a risk of confounding heteroscedasticity with model misspecification.

### Key Concepts

#### White's Test (continued)
Once the auxiliary regression is run using all independent variables, their squares, and cross-products, the test statistic is calculated as $n R^2$.
- In large samples, $n R^2$ follows a Chi-square ($\\chi^2$) distribution. The degrees of freedom equal the number of regressors in the auxiliary regression (excluding the intercept).
- If the computed $\\chi^2$ exceeds the critical value, we reject the null hypothesis of homoscedasticity.
- **Limitations**: 
  1. Adding squares and cross-products drastically reduces the degrees of freedom (especially with many $X$ variables).
  2. A significant result might actually indicate a **specification error** (e.g., omitting a relevant variable or using the wrong functional form) rather than pure heteroscedasticity. Thus, it is a joint test of both.

### Definitions
- **White's Test**: A general test for heteroscedasticity that regresses squared residuals on all independent variables, their squares, and cross-products. ⭐ (exam-important)

### Connections
- Completes the tests started in: Detection of Heteroscedasticity (Chunk 006)

## Section: Remedial Measures for Heteroscedasticity 🔴

### Core Idea
To correct heteroscedasticity and restore the estimators to being BLUE (minimum variance), we must mathematically transform the model so that the new error term has a constant variance. This is typically achieved by weighting the observations inversely to their variance (Weighted Least Squares).

> **In Simple Terms:** If rich households have wildly unpredictable savings but poor households have very predictable savings, the model should pay more attention (give more "weight") to the poor households' data to get a stable estimate.

### Key Concepts

#### Weighted Least Squares (WLS)
If the exact pattern of the variance is known (e.g., $\\sigma_i^2 = \\sigma^2 z_i^2$), we divide the entire regression equation by $z_i$.
- The new error term becomes $v_i = \\frac{u_i}{z_i}$.
- The variance of the new error term is $Var(v_i) = \\sigma^2$, which is constant (homoscedastic).
- The regression is then run on the transformed variables **without an intercept term**.
- Common patterns: If $Var(u_i)$ is proportional to $x_i$, divide by $\\sqrt{x_i}$. If it is proportional to $x_i^2$, divide by $x_i$.

#### Two-Step WLS
If the variance pattern is unknown but believed to be proportional to the squared expected value of $Y$ ($[E(y_i)]^2$), a two-step process is used:
1. Run standard OLS to obtain the estimated coefficients $\\hat{\\alpha}$ and $\\hat{\\beta}$.
2. Use these to find the predicted values $\\hat{y}_i$.
3. Divide the original equation by $\\hat{y}_i$ and run the regression. Standard errors here are only asymptotically valid because the weights are estimated, not known perfectly.

#### Generalised Least Squares (GLS)
WLS is simply a special case of GLS. In matrix algebra, GLS involves pre-multiplying the data by the inverse square root of the variance-covariance matrix ($\\phi^{-1/2}$). This transforms the error variances to be homoscedastic and equal to 1. Because the true matrix is rarely known, researchers use **Estimated GLS (EGLS)** by using the residuals from an initial OLS run to estimate the weights.

#### White's Estimator (Robust Standard Errors)
If the variance pattern is completely unknown and cannot be modeled, we keep the standard OLS parameter estimates (which are unbiased) but replace the biased standard error formula with White's Heteroscedasticity-Corrected formula.
- **Advantage**: It does not require knowing the pattern of heteroscedasticity.
- **Limitation**: It is strictly a **large-sample** procedure. It may be less efficient than a proper WLS transformation.

#### Logarithmic Transformation & Deflators
- **Log Transformation**: Taking the natural log of variables (e.g., Cobb-Douglas $\\ln Y = \\ln A + \\alpha \\ln K + \\beta \\ln L$) inherently compresses the scale of the data, naturally mitigating heteroscedasticity.
- **Deflators**: Dividing by a relevant size metric (e.g., population to get per-capita figures, or a price index to get real figures). 
  - *Rule of thumb*: If the deflation is supported by economic theory, use the deflated model for inferences. If it is done purely as a mathematical hack to fix heteroscedasticity, use the original parameters to draw inferences.

### Definitions
- **Generalised Least Squares (GLS)**: An estimation technique that transforms the variables to produce homoscedastic error terms, yielding BLUE estimators. ⭐
- **White's Estimator**: A large-sample procedure that calculates robust standard errors to correct for heteroscedasticity when its exact pattern is unknown. ⭐

### Mechanisms / Processes
**WLS Example Mechanism:**
Original: $y_i = \\beta x_i + u_i$
Given: $Var(u_i) = \\sigma^2 x_i$
Transform: Divide by $\\sqrt{x_i}$
New model: $\\frac{y_i}{\\sqrt{x_i}} = \\beta \\frac{x_i}{\\sqrt{x_i}} + \\frac{u_i}{\\sqrt{x_i}}$

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that fixing heteroscedasticity changes the OLS coefficients significantly. → ✅ Correct: The OLS coefficients are already unbiased. The main goal of WLS and Robust Standard Errors is to fix the *variances* so hypothesis tests are valid.

> **Quick Recall:**
> - If variance pattern is known: Use WLS.
> - If variance pattern is unknown (large sample): Use White's Robust Standard Errors.
> - Logs compress data naturally, fixing heteroscedasticity.

### Connections
- Fixes issues from: Consequences of Heteroscedasticity (Chunk 006)

## Section: Concept of Errors in Variables 🔴
<!-- This section continues into chunk 008 -->

### Core Idea
Standard OLS assumes that all independent variables ($X$) are measured perfectly, without any error. In reality—especially when using proxy variables or secondary data—the data contains measurement errors. When the independent variables are flawed, the final model estimates will also be flawed.

> **In Simple Terms:** Imagine trying to measure the effect of "intelligence" on "income." Since you can't measure true intelligence perfectly, you use an IQ test score as a proxy. But an IQ score has measurement errors. Because your input data is mathematically "fuzzy," your model's final answer will be fuzzy too.

### Key Concepts

#### Measurement Errors
In classical regression, the only error we account for is the stochastic disturbance term ($u_i$), which captures the influence of omitted variables. However, "Errors in Variables" occurs when the observed data itself ($X$ or $Y$) is systematically or randomly different from the true, unobservable variable.

### Definitions
- **Errors in Variables**: A violation of the classical assumption that regressors are measured perfectly, occurring when the observed variables contain random measurement errors (often due to using proxy variables). ⭐ (exam-important)

<!-- This section continues in chunk 008 -->
