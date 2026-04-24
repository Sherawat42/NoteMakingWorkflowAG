# Chunk 003 — Detection and Remedies of Autocorrelation
<!-- Pages: 21-32 -->
<!-- Source: chunk_003.txt -->

## Section: Consequences of Autocorrelation 🔴
<!-- This section continues from chunk 002 -->

### Core Idea
While OLS estimators remain unbiased in the presence of autocorrelation, their calculated variances are biased. Specifically, the standard OLS formula tends to underestimate the true variance, which inflates the standard errors and leads to unreliable hypothesis testing.

> **In Simple Terms:** The standard OLS formula is "blind" to the chain-reaction of errors. Because it ignores this connection, it severely underestimates how wrong the estimates might actually be.

### Key Concepts

#### Biasedness of Var(OLS estimator)
In an AR(1) model, the OLS estimator of the variance ($E(\\hat{\\sigma}^2)$) does not equal the true variance ($\\sigma^2$). 
- The true variance of the estimator $Var(\\hat{\\beta})_{AR(1)}$ is multiplied by an inflation factor of $\\frac{1+\\rho r}{1-\\rho r}$ (where $r$ is the autocorrelation of $x$).
- If both $\\rho$ and $r$ are positive, the standard OLS formula **underestimates** the true variance ($E(\\hat{\\sigma}^2) < \\sigma^2$).
- Using the standard OLS variance leads to biased results. When the true $Var(\\hat{\\beta})_{AR(1)}$ is used instead, confidence intervals are wider than those obtained from Generalized Least Squares (GLS). This increases the likelihood of incorrectly accepting the null hypothesis (declaring a significant variable as insignificant).

### Definitions
- **GLS (Generalized Least Squares)**: An estimation procedure that transforms variables to account for autocorrelation, producing estimators that have minimum variance (BLUE).

### Mechanisms / Processes
**Why OLS variance is biased:**
1. The OLS variance formula assumes zero covariance between errors.
2. Under AR(1), $E(\\sum \\hat{u}_t^2) = \\sigma^2 \\left[T - \\frac{1+\\rho r}{1-\\rho r}\\right]$.
3. Therefore, $E(\\hat{\\sigma}^2) \\neq \\sigma^2$. The bias depends on the signs of $\\rho$ and $r$.

> **Quick Recall:**
> - OLS estimators are unbiased but NOT minimum variance (not BLUE).
> - OLS variance is biased (usually underestimating the true variance).
> - Standard hypothesis tests ($t$-test, $F$-test) become invalid.

### Connections
- Builds on: Concept of Autocorrelation (Chunk 002)

## Section: Detection of Autocorrelation 🔴

### Core Idea
Since true error terms are unobservable, we use estimated residuals ($\\hat{u}_t$) to detect autocorrelation. This can be done visually through scatter plots or quantitatively using statistical tests like Durbin-Watson (for AR(1) processes) and Breusch-Godfrey (for higher-order processes).

> **In Simple Terms:** Since we can't see the true errors, we look at our model's leftovers (residuals). We can eyeball a graph of them to look for a pattern, or run a math test to check if today's leftover predictably follows yesterday's leftover.

### Key Concepts

#### Residual Plot
A simple visual check. Plotting $\\hat{u}_t$ against time ($t$) or against the previous residual ($\\hat{u}_{t-1}$).
- A linear trend (upward/downward), cyclical, or quadratic pattern indicates autocorrelation.
- Positive autocorrelation often clusters positive residuals together and negative residuals together.
- Limitation: It is highly subjective.

#### Durbin-Watson (DW) Test
The most popular quantitative test, computing the ratio of the sum of squared differences in successive residuals to the overall residual sum of squares.
- **Formula approximation**: $d \\approx 2(1 - \\hat{\\rho})$
- Because $-1 \\le \\hat{\\rho} \\le 1$, the test statistic $d$ ranges from 0 to 4.
  - $d \\approx 2$: No autocorrelation.
  - $d$ near 0: Positive autocorrelation.
  - $d$ near 4: Negative autocorrelation.
- **Limitations**: The test has a "zone of indecision" between critical limits $d_L$ and $d_U$ where no conclusion can be drawn. It requires an intercept, assumes non-stochastic regressors, and strictly tests only for AR(1) processes without lagged dependent variables.

#### Breusch-Godfrey (BG) Test
Also known as the Lagrange Multiplier (LM) test, it overcomes DW's limitations. It is a general test that can detect higher-order autocorrelations (AR(p)) and moving average (MA) errors. It is also valid when lagged dependent variables are present.

### Definitions
- **Durbin-Watson Test**: A statistical test used to detect the presence of first-order autocorrelation in the residuals of a regression. ⭐ (exam-important)
- **Breusch-Godfrey (BG) Test**: A generalized test for autocorrelation that can detect higher-order autoregressive and moving average processes. ⭐ (exam-important)

### Mechanisms / Processes
**Steps for the BG Test:**
1. Estimate the primary regression using OLS and get residuals $\\hat{u}_t$.
2. Run an auxiliary regression: regress $\\hat{u}_t$ on all original $X$ variables PLUS lagged values of the residuals ($\\hat{u}_{t-1}, \\hat{u}_{t-2}, \\dots, \\hat{u}_{t-p}$).
3. Calculate the test statistic: $(T-p)R^2$, which follows a Chi-square ($\\chi^2$) distribution with $p$ degrees of freedom in large samples.
4. If the computed value exceeds the tabulated $\\chi^2$ value, reject the null hypothesis of no autocorrelation.

### ⚠️ Common Mistakes
- ❌ Mistake: Concluding there is no autocorrelation if $d$ falls in the "zone of indecision". → ✅ Correct: The test is simply inconclusive; you must use an alternative test like the BG test.

> **Quick Recall:**
> - DW $d \\approx 2$: No autocorrelation. DW $d \\approx 0$: Positive. DW $d \\approx 4$: Negative.
> - DW has a zone of indecision and only tests AR(1).
> - BG (LM) test overcomes DW limits: tests AR(p), MA processes, and allows lagged dependent variables.

### Connections
- Solves problems raised in: Consequences of Autocorrelation (Chunk 003)

## Section: Remedial Measures for Autocorrelation 🔴
<!-- This section continues into chunk 004 -->

### Core Idea
Before applying remedies, you must ensure the autocorrelation is "pure" and not a symptom of a misspecified model (like an omitted variable). If it is pure autocorrelation, the model is transformed using Generalized Least Squares (GLS), First-Differencing, or Newey-West standard errors to produce valid estimators.

> **In Simple Terms:** If your data has a built-in momentum that's messing up your standard errors, you can mathematically "strip away" that momentum (differencing) or use a tougher formula for standard errors (Newey-West) that accounts for it.

### Key Concepts

#### Quasi-first Differencing
This method transforms the variables to strip out the AR(1) process, creating a Generalized Difference equation:
$y_t - \\rho y_{t-1} = \\alpha(1-\\rho) + \\beta(x_t - \\rho x_{t-1}) + \\varepsilon_t$.
By regressing the transformed $y_t^*$ on $x_t^*$, the resulting error term $\\varepsilon_t$ satisfies classical assumptions. This is the **Generalized Least Squares (GLS)** procedure, which restores the estimators to being BLUE. 
- The Prais-Winsten transformation is used to save the first observation from being lost during differencing.
- Limitation: $\\rho$ is rarely known and must be estimated (making it Feasible GLS / FGLS).

#### First-Differencing
Used when $\\rho = +1$ (a severe case known as the unit root problem). The quasi-difference equation reduces to:
$\\Delta y_t = \\beta \\Delta x_t + \\varepsilon_t$.
The constant term disappears (unless there was a linear trend). This transformation induces stationarity. To compare the $R^2$ of this model against the original levels equation, specific adjustments must be made to the Residual Sum of Squares (RSS). The Berenblut-Webb test is used to check if $\\rho = +1$.

#### The Newey-West Method
Instead of transforming the data, this method sticks with the OLS estimators but computes **HAC (Heteroscedasticity-and-Autocorrelation-Corrected) standard errors**. 
- It is an extension of White's standard errors.
- It is only valid for **large samples**.

### Definitions
- **Quasi-first Differencing**: A GLS transformation technique where a proportion ($\\rho$) of the previous period's value is subtracted from the current value to eliminate AR(1) autocorrelation.
- **First-Differencing**: A transformation where the previous period's value is entirely subtracted from the current value (assuming $\\rho = +1$) to induce stationarity.
- **Newey-West Method**: A technique that corrects OLS standard errors for both heteroscedasticity and autocorrelation in large samples. ⭐ (exam-important)

### Mechanisms / Processes
**When to use First-Differencing:**
1. Check if the Durbin-Watson statistic is very small (rule of thumb: $d < R^2$).
2. If true, it implies $\\rho \\approx 1$.
3. Run the regression on the differences ($\\Delta y_t$ on $\\Delta x_t$).

> **Quick Recall:**
> - Ensure autocorrelation is "pure" before applying remedies.
> - GLS / Quasi-differencing restores estimators to BLUE by removing the AR(1) pattern.
> - First-differencing is used when $\\rho = 1$ (unit root).
> - Newey-West provides HAC standard errors for large samples without changing the OLS estimators.

### Connections
- Fixes issues from: Consequences of Autocorrelation (Chunk 003)

<!-- This section continues in chunk 004 -->
