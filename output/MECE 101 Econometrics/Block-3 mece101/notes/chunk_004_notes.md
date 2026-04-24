# Chunk 004 — Estimating \rho and Multicollinearity Intro
<!-- Pages: 33-42 -->
<!-- Source: chunk_004.txt (and chunk_003.txt for Section 9.6) -->
<!-- Structure adjusted from original outline to include Detection of Multicollinearity -->

## Section: Methods of Estimating \rho 🟡

### Core Idea
To apply the Generalized Least Squares (GLS) or quasi-differencing methods to fix autocorrelation, the true population autocorrelation coefficient ($\\rho$) must be known. Because it is rarely known in practice, it must be estimated from the sample data using various techniques.

> **In Simple Terms:** To fix the problem of "momentum" in your errors, you first need to guess how strong that momentum is. These methods are mathematical ways to make an educated guess.

### Key Concepts

#### Estimation Methods
1. **From DW Statistic**: For large samples, $d \\approx 2(1 - \\hat{\\rho})$, which can be rearranged to $\\hat{\\rho} \\approx 1 - \\frac{d}{2}$.
2. **From Residuals**: Run OLS, get the residuals $\\hat{u}_t$, and then regress $\\hat{u}_t$ directly on $\\hat{u}_{t-1}$ to find the slope (which is $\\hat{\\rho}$).
3. **Iterative Procedures**:
   - **Cochrane-Orcutt Procedure**: Obtains initial residuals from OLS, computes $\\hat{\\rho} = \\frac{\\sum \\hat{u}_t \\hat{u}_{t-1}}{\\sum \\hat{u}_t^2}$, and transforms the model.
   - **Durbin's Procedure**: Regresses $y_t$ on $y_{t-1}, x_t$, and $x_{t-1}$. The coefficient on $y_{t-1}$ provides the estimate of $\\rho$.
4. **Grid-Search Procedures**:
   - **Hildreth and Lu Procedure**: Tests different values of $\\rho$ (from -1 to +1 at 0.1 intervals), runs regressions for each, and selects the $\\rho$ that yields the lowest Residual Sum of Squares (RSS).
   - **Maximum Likelihood Procedure**: Uses a grid search to find the $\\rho$ that minimizes the log-likelihood function.

### Definitions
- **Feasible GLS (FGLS) / Estimated GLS (EGLS)**: The application of the GLS procedure using an estimated $\\hat{\\rho}$ rather than the true (unknown) population $\\rho$.

### Edge Cases & Caveats
- In **large samples**, any of these methods provide consistent estimates of $\\rho$.
- In **small samples**, estimating $\\rho$ can introduce its own errors. As a rule of thumb, if the sample size is around 20 and $\\hat{\\rho} < 0.3$, it is often better to just stick with standard OLS rather than trying to perform FGLS.

> **Quick Recall:**
> - $\\rho$ must be estimated to run GLS.
> - $\\hat{\\rho} \\approx 1 - d/2$.
> - Iterative methods: Cochrane-Orcutt, Durbin's.
> - Grid-search methods: Hildreth-Lu, Maximum Likelihood.

### Connections
- Solves problems raised in: Remedial Measures for Autocorrelation (Chunk 003)

## Section: Concept of Multicollinearity 🔴

### Core Idea
Multicollinearity occurs when there is a high or perfect correlation among the explanatory (independent) variables in a multiple regression model. This violates the classical OLS assumption that explanatory variables should be independent of one another (orthogonal).

> **In Simple Terms:** Multicollinearity is like having two people trying to turn the steering wheel of a car at the same time. You know the car is turning, but you can't tell exactly whose hands are doing the work.

### Key Concepts

#### Perfect Multicollinearity
Occurs when there is an exact linear relationship between two or more independent variables (e.g., $x_2 = 2x_3$). When this happens, it is mathematically impossible to estimate the individual regression coefficients—you can only estimate their linear combinations.

#### Near Multicollinearity
Occurs when the correlation between variables is very high, but not exactly perfect. The coefficients can technically be estimated, but the estimates are highly imprecise and have massive standard errors.

### Definitions
- **Multicollinearity**: The presence of high correlation between explanatory variables in a multiple regression model. ⭐ (exam-important)
- **Perfect Multicollinearity**: A situation where two or more explanatory variables bear an exact linear relationship, making it impossible to uniquely estimate their coefficients. ⭐ (exam-important)
- **Orthogonal**: A state where independent variables are completely uncorrelated with one another.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing multicollinearity applies to non-linear relationships. → ✅ Correct: Multicollinearity specifically and exclusively refers to *linear* relationships between explanatory variables (e.g., $X_3 = X_1 + X_2^2$ does not violate the rule, because $X_2^2$ is a non-linear transformation).

> **Quick Recall:**
> - Multicollinearity violates the assumption of independent regressors.
> - Perfect multicollinearity = impossible to estimate individual coefficients.
> - Near multicollinearity = can estimate, but with huge standard errors.

### Connections
- Prerequisite for: Consequences of Multicollinearity (Chunk 004)

## Section: Consequences of Multicollinearity 🔴

### Core Idea
Even under near multicollinearity, OLS estimators retain their desirable property of being BLUE (Best Linear Unbiased Estimators). However, their variances become drastically inflated, making it nearly impossible to isolate the individual impact of each highly correlated variable.

> **In Simple Terms:** The model overall works well and makes good predictions, but the math gets so confused by the highly correlated variables that it can't confidently give credit to any single variable.

### Key Concepts

#### Estimator Properties
Despite multicollinearity, OLS estimators remain unbiased, consistent, and BLUE. The issue is not that the estimates are inherently "wrong," but that they are practically useless due to massive uncertainty.

#### Five Major Consequences
1. **Regression coefficients are indeterminate**: Under perfect multicollinearity, there are infinite solutions for the coefficients.
2. **Standard errors are inflated**: As the correlation ($r_{12}$) between variables approaches 1, the variance formula denominator approaches 0, driving the variance and standard error toward infinity.
3. **Wider confidence intervals**: Inflated standard errors lead to wide confidence intervals, drastically increasing the chance of a **Type II error** (failing to reject a false null hypothesis).
4. **High $R^2$ but insignificant t-ratios**: The overall model explains the data very well (the F-test is highly significant), but when looking at individual variables, their t-tests are found to be statistically insignificant. This is the classic hallmark of multicollinearity.
5. **Extreme sensitivity**: The estimated coefficients swing wildly with small changes to the data or if an independent variable is added/removed.

### Definitions
- **Indeterminate coefficients**: A state in perfect multicollinearity where an infinite number of solutions exist for regression coefficients, preventing unique estimation.

### Mechanisms / Processes
**The Variance Inflation Mechanism:**
$Var(\\hat{\\beta}_1) = \\frac{\\sigma^2}{\\sum x_{1i}^2 (1 - r_{12}^2)}$
As $r_{12}^2 \\to 1$ (correlation increases), the term $(1 - r_{12}^2) \\to 0$. Dividing by a number approaching zero causes $Var(\\hat{\\beta}_1)$ to approach infinity.

> **Quick Recall:**
> - OLS estimators are STILL BLUE under multicollinearity.
> - Standard errors inflate heavily.
> - Classic symptom: High $R^2$ (significant F-test) but insignificant t-ratios.
> - Results become highly sensitive to small data changes.

### Connections
- Leads to: Detection of Multicollinearity (Chunk 004)

## Section: Detection of Multicollinearity 🔴
<!-- This section starts here -->
<!-- Continues into chunk 005 -->

### Core Idea
Because multicollinearity is a sample-specific data problem (rather than a theoretical modeling error), detection focuses on measuring its *degree* or *strength* in the specific dataset at hand, using various rules of thumb.

### Key Concepts

#### Various Tests to Detect Multicollinearity
1. **Correlation Matrix**: Examining pair-wise correlations. High correlation (e.g., > 0.8) indicates multicollinearity. However, low pair-wise correlation does NOT guarantee absence of multicollinearity (three or more variables might be collectively collinear).
2. **High Standard Errors / Classic Symptom**: Observing high standard errors. But note: high standard errors can also be caused by a high $\\sigma^2$ or low variation in $X$, so it's not a foolproof indicator.
3. **Variance Inflation Factor (VIF)**: Measures how much the variance of an estimator is inflated by collinearity. $VIF_j = \\frac{1}{1 - R_j^2}$. As $R_j^2 \\to 1$, VIF approaches infinity.
4. **Tolerance (TOL)**: The inverse of VIF ($1 - R_j^2$). It ranges from 0 (perfect collinearity) to 1 (no collinearity).
5. **Klein's Rule of Thumb**: Suggests multicollinearity is a serious problem only if the $R_j^2$ of an auxiliary regression exceeds the overall model's $R^2$.
6. **Condition Number (CN)**: An overall measure derived from the maximum and minimum eigenvalues of the $X'X$ matrix. $CN = \\sqrt{\\frac{\\text{Maximum eigenvalue}}{\\text{Minimum eigenvalue}}}$. 
   - $CN = 1$: No collinearity.
   - $CN = 15$: Moderate collinearity.
   - $CN > 30$: Severe collinearity.

<!-- This section continues in chunk 005 -->
