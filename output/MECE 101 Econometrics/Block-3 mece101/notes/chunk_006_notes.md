# Chunk 006 — Heteroscedasticity Concept and Detection
<!-- Pages: 52-61 -->
<!-- Source: chunk_006.txt -->

## Section: Concept of Heteroscedasticity 🔴

### Core Idea
In the classical regression model, we assume the error terms have a constant variance regardless of the value of the independent variables (homoscedasticity). Heteroscedasticity occurs when this assumption is violated, meaning the variance of the stochastic disturbance term changes across the sample.

> **In Simple Terms:** Heteroscedasticity means the "spread" or "range of mistakes" your model makes is not consistent. For example, predicting the savings of a poor household will have a very narrow margin of error, but predicting the savings of a rich household will have a massive margin of error because wealthy households have much more freedom in how they spend or save.

### Key Concepts

#### Homoscedasticity vs Heteroscedasticity
- **Homoscedasticity**: The conditional variance of $u_i$ is equal to a constant $\\sigma^2$. $E(u_i^2) = Var(u_i) = \\sigma^2$.
- **Heteroscedasticity**: The conditional variance of $u_i$ varies across observations. $E(u_i^2) = Var(u_i) = \\sigma_i^2$ (notice the $i$ subscript on $\\sigma$).

#### Causes in Cross-Section Data
Heteroscedasticity is much more common in cross-sectional data than in time-series data.
**Common causes include:**
1. Inherent variations in behavior (e.g., spending habits of the rich vs poor).
2. Outliers in the data.
3. Massive differences in the scale of variables (e.g., comparing the GDP of a tiny state vs a massive state without adjusting to per-capita terms).
4. Incorrect data transformation.

### Definitions
- **Homoscedasticity**: The assumption that the variance of the stochastic disturbance term is finite and remains constant over the sample.
- **Heteroscedasticity**: The condition where the variance of the error term is not constant, but changes with the values of the independent or dependent variable. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Believing heteroscedasticity is common in time-series data. → ✅ Correct: It is most common in cross-sectional data. Autocorrelation is the typical problem for time-series data.

> **Quick Recall:**
> - Homo = same, Hetero = different. Scedasticity = scatter/variance.
> - Constant variance: $Var(u_i) = \\sigma^2$.
> - Non-constant variance: $Var(u_i) = \\sigma_i^2$.

### Connections
- Prerequisite for: Consequences of Heteroscedasticity (Chunk 006)

## Section: Consequences of Heteroscedasticity 🔴

### Core Idea
Under heteroscedasticity, OLS estimators remain linear and unbiased, but they are no longer efficient (they do not have minimum variance, meaning they are no longer BLUE). Crucially, the estimated variance of the OLS estimator becomes biased, which invalidates standard hypothesis tests (t and F tests).

> **In Simple Terms:** The model's guesses are still right on average, but they are not the sharpest guesses possible. More importantly, the model's confidence in its own guesses is mathematically broken, making its "p-values" totally unreliable.

### Key Concepts

#### Unbiasedness of $\\hat{\\beta}$
The OLS estimator remains unbiased ($E(\\hat{\\beta}) = \\beta$) because the core assumptions ensuring unbiasedness—namely $E(u_i) = 0$ and the independence of $u_i$ from $x_i$—are still intact.

#### Efficiency of $\\hat{\\beta}$
The OLS estimator is inefficient because we can find another linear unbiased estimator with a smaller variance. Specifically, the **Weighted Least Squares (WLS)** estimator provides a smaller variance than standard OLS when heteroscedasticity is present.

#### Biased Variance
The calculation for the variance of the OLS estimator itself is biased: $E(Var(\\hat{\\beta})) \\neq Var(\\hat{\\beta}_{true})$. 
- Standard errors become unreliable.
- Confidence intervals become inappropriately wide or narrow.
- As a result, t-ratios and F-tests lead to faulty statistical inferences.

### Definitions
- **Weighted Least Squares (WLS)**: An estimation method where observations are weighted inversely by their variances to correct for heteroscedasticity, restoring efficiency (BLUE). ⭐ (exam-important)

### Mechanisms / Processes
**Proof logic for bias in variance:**
1. Under homoscedasticity, $E(RSS) = (n-1)\\sigma^2$.
2. Under heteroscedasticity, $E(RSS)$ does not simplify this way. It depends on $\\sum \\sigma_i^2$.
3. Thus, the expected value of the OLS variance formula does not equal the true variance of the parameter.

> **Quick Recall:**
> - OLS is STILL unbiased.
> - OLS is NO LONGER efficient (not BLUE).
> - OLS variance is BIASED -> Hypothesis tests are INVALID.

### Connections
- Leads to: Detection and Remedial Measures (Chunks 006, 007)

## Section: Detection of Heteroscedasticity 🔴
<!-- This section starts here -->
<!-- Continues into chunk 007 -->

### Core Idea
Because we cannot observe the true error variances ($\\sigma_i^2$), we use the estimated residuals ($\\hat{u}_i$) to test whether their spread changes systematically with the independent variables ($X$).

### Key Concepts

#### 1. Residual Plot
A visual check. Plot $\\hat{u}_i$ or $\\hat{u}_i^2$ against $X$ or $\\hat{y}_i$. If the plot shows a widening funnel, a cone, or a quadratic shape, it indicates that the error variance is growing or shrinking systematically.

#### 2. Auxiliary Regression
Regress $\\hat{u}_i^2$ on $X, X^2, X^3$ or on $\\hat{y}_i, \\hat{y}_i^2$ to see if the regression coefficients are statistically significant. If they are, it indicates heteroscedasticity.

#### 3. Park Test
Assumes the error variance is related to an explanatory variable via the function: $\\sigma_i^2 = \\sigma^2 X_i^\\beta e^{v_i}$.
- **Method**: Run the auxiliary regression $\\ln \\hat{u}_i^2 = \\alpha + \\beta \\ln X_i + v_i$.
- **Test**: If the coefficient $\\beta$ is statistically significant (reject $H_0: \\beta = 0$), heteroscedasticity is present.

#### 4. Glejser Test
Similar to Park, but uses the absolute value of residuals $|\\hat{u}_i|$ and tests it against various functional forms of $X$ (e.g., $1/X_i$, $\\sqrt{X_i}$, or $X_i$).
- **Test**: Regress $|\\hat{u}_i| = \\alpha + \\beta f(X_i) + v_i$. If $\\beta$ is significant, heteroscedasticity exists.

#### 5. Goldfeld-Quandt Test
Best for small samples. It compares the variances of two extreme groups in the dataset.
- **Method**: 
  1. Order the data by $X$ (lowest to highest).
  2. Omit '$c$' central observations to clearly separate the low and high extremes.
  3. Run separate OLS on the lower group (to get $RSS_1$) and upper group (to get $RSS_2$).
- **Test**: Compute $\\lambda = (RSS_2 / df) / (RSS_1 / df)$. If $\\lambda > F_{critical}$, reject homoscedasticity. 
- **Limitation**: Arbitrary choices of which variable to order by and how many middle observations to drop.

#### 6. Breusch-Pagan Test
An asymptotic (large sample) test that assumes $\\sigma_i^2$ is a linear function of some variables $z$.
- **Test**: Regress $\\hat{u}_i^2$ on $z_1, z_2, \\dots$. Calculate the Explained Sum of Squares ($S_0$). The statistic $\\lambda = S_0 / 2\\hat{\\sigma}^4$ follows a $\\chi^2$ distribution.

#### 7. White's Test (Introduction)
A highly general test that does not require the assumption of normally distributed errors or any arbitrary ordering of data.
- **Method**: Regress $\\hat{u}_i^2$ on all independent variables, their squares, and all cross-products. (e.g., $X_2, X_3, X_2^2, X_3^2, X_2 X_3$).

### Definitions
- **Park Test**: A test for heteroscedasticity that regresses the natural log of squared residuals on the natural log of an explanatory variable. ⭐
- **Goldfeld-Quandt Test**: A test that orders observations by an explanatory variable, drops central data points, and compares the residual variances of the resulting high and low groups. ⭐

<!-- This section continues in chunk 007 -->
