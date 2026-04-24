# Complete Notes


## Section: Possible Problems in Specification 🔴

### Core Idea
Correct model specification is the foundational step in regression analysis, essential for obtaining unbiased and efficient estimates. The specification should be driven by theoretical logic rather than purely empirical or methodological considerations, as any specification error cascades into flawed estimation and interpretation.

> **In Simple Terms:** Think of building a model like cooking a recipe. If you start with the wrong ingredients (wrong variables) or the wrong cooking method (wrong functional form), the final dish (your predictions) will be ruined, no matter how good your oven is.

### Key Concepts

#### Importance of Model Specification
The causal relationship between a dependent and independent variable involves three critical steps: specifying the model, estimating parameters, and interpreting them. Adding or deleting orthogonal independent variables does not affect the partial regression coefficients of other independent variables, but it significantly affects their standard errors and the error variance of the dependent variable.

#### Sources of Specification Error
There are five primary ways an error or bias can enter a regression model:
1. Inclusion of redundant/irrelevant variables
2. Omission of relevant variables
3. Incorrect functional form (e.g., using a linear model when the true relationship is non-linear like Cobb-Douglas or quadratic)
4. Incorrect assumptions regarding the error term (e.g., non-zero mean, heteroscedasticity, autocorrelation)
5. Error in measurement of variables (which is distinct from the error term; measurement error occurs when a variable is included but measured incorrectly, such as using "years of schooling" as a proxy for "education")

#### Implications of Specification Error
Violating the classical assumptions of the regression model compromises the desirable properties of OLS estimators. Econometric models must ensure that the dependent variable is logically explained by the independent variables. If the functional form is incorrectly specified, or if variables are measured with error (due to non-response, reporting, or computing errors), the accuracy of parameters and subsequent inferences are compromised.

### Definitions
- **Specification Error**: Errors arising from incorrect model formulation, including omitted/irrelevant variables, wrong functional forms, incorrect error term assumptions, or measurement errors. ⭐ (exam-important)
- **Measurement Error**: Errors resulting from incorrect measurement of a variable included in the model, often due to proxies, reporting errors, or data collection issues.

### Mechanisms / Processes
1. Theoretical model formulation based on economic logic.
2. Selection of relevant variables and appropriate functional form.
3. Verification of OLS assumptions (linearity, no measurement error, no perfect multicollinearity, zero error mean, homoscedasticity, no autocorrelation).

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing the "error term" with "measurement error." → ✅ Correct: The error term reflects excluded variables that influence the dependent variable. Measurement error reflects inaccuracies in measuring the variables that *are* included in the model.

> **Quick Recall:**
> - Specification is the most critical step; errors here ruin estimation.
> - The five sources of specification error are: omitted variables, irrelevant variables, wrong functional form, wrong error assumptions, and measurement errors.
> - Measurement error is distinct from the stochastic error term.

### Connections
- Prerequisite for: Inclusion of Variables in a Model (Chunk 001: Possible Problems in Specification)

### Open Questions
- How do we specifically test for measurement error if the true variables are unobservable?

## Section: Inclusion of Variables in a Model 🔴

### Core Idea
The consequences of misspecifying the variables in a model vary drastically: including irrelevant variables yields unbiased but inefficient estimators, while omitting relevant variables results in biased, inconsistent estimators and invalid hypothesis tests.

> **In Simple Terms:** If you pack a raincoat for a sunny trip (irrelevant variable), it's harmless but wastes space in your bag (inefficient). But if you forget your passport for an international trip (omitted relevant variable), you're completely stuck and the trip is ruined (biased and faulty inferences).

### Key Concepts

#### Inclusion of Irrelevant Variables
When a redundant/irrelevant variable is added to a model:
- The estimators of the parameters remain **unbiased** ($E(\\hat{\\beta}_1) = \\beta_1$).
- The coefficient for the irrelevant variable will have an expected value of 0.
- The **efficiency** of the estimators declines (variance increases).
- The larger variance reduces precision, causing wider confidence intervals and increasing the probability of a **Type II error** (failing to reject a false null hypothesis).
- The $R^2$ value increases artificially.

#### Omission of Relevant Variables
When a relevant variable that influences the dependent variable is excluded:
- Its impact is absorbed into the residuals, causing them to show a systematic pattern (e.g., autocorrelation detectable by the Durbin-Watson statistic).
- The estimators of the included parameters become **biased**. The bias is equal to: (coefficient of the excluded variable, $\\beta_2$) $\\times$ (regression coefficient of the excluded variable on the included variable, $b_{21}$).
- The variance of the estimators is biased (often an over-estimate).
- Conventional hypothesis tests and confidence intervals become **invalid**, leading to faulty inferences.

#### Top-down vs. Bottom-up Approaches
- **General-to-specific (Top-down)**: Start with a large model including many variables and drop the statistically insignificant ones. This is preferred by researchers to avoid the severe biases of omitting relevant variables.
- **Specific-to-general (Bottom-up)**: Start with a simple model and add variables. This is criticized because nominal significance levels differ from true significance levels if relevant variables are missing.

### Definitions
- **Type II Error**: The error of not rejecting a null hypothesis when the null hypothesis is actually false.

### Mechanisms / Processes
**Calculating Omitted Variable Bias:**
1. Assume true model: $y = \\beta_1 x_1 + \\beta_2 x_2 + u$
2. Estimated incorrect model: $y = \\beta_1^* x_1 + e$
3. The expected value of the biased estimator is: $E(\\beta_1^*) = \\beta_1 + \\beta_2 b_{21}$
4. The bias is exactly $\\beta_2 b_{21}$.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that adding more variables always makes a model better. → ✅ Correct: While omitting variables causes severe bias, adding irrelevant variables decreases the model's efficiency and widens confidence intervals.

> **Quick Recall:**
> - Irrelevant variable included → Unbiased but inefficient estimators. Increases risk of Type II error.
> - Relevant variable omitted → Biased estimators, biased variance, invalid hypothesis tests.
> - Bias formula: $Bias = \\beta_{excluded} \\times b_{(excluded \\ on \\ included)}$.
> - General-to-specific modeling is preferred over specific-to-general.

### Connections
- Builds on: Possible Problems in Specification (Chunk 001: Possible Problems in Specification)

## Section: Specification Error Test (RESET) 🔴

### Core Idea
Ramsey's RESET (Regression Specification Error Test) is a widely used diagnostic tool to determine if the functional form of a regression model is correctly specified by checking if non-linear combinations of the fitted values help explain the dependent variable.

> **In Simple Terms:** RESET is a diagnostic tool that checks if your straight-line model is missing important curves. It artificially adds curves (squares and cubes of your predictions) to see if they fit the data better. If they do, your original straight-line model is wrong.

### Key Concepts

#### RESET Method
RESET introduces quadratic and cubic functions of the estimated dependent variable ($\\hat{y}$) into the original regression model as additional explanatory variables. It then uses an F-test to compare the $R^2$ of the new model against the old model. If the new variables significantly improve the $R^2$, it indicates that the original linear specification was flawed.

#### Limitations of RESET
While RESET is excellent for detecting if the functional form is misspecified (e.g., trying to fit a linear line to non-linear data), it **does not test for omitted variables**. Furthermore, if the test rejects the null hypothesis (meaning the model is misspecified), it only flags that an error exists—it does not provide guidance on *how* to fix it or which functional form should be adopted instead.

### Definitions
- **RESET (Regression Specification Error Test)**: A general test for model misspecification that checks if non-linear functional forms of the estimated dependent variable improve the model's fit. ⭐ (exam-important)

### Mechanisms / Processes
**Steps to perform RESET:**
1. Estimate the original model (e.g., $y = \\beta_1 x_1 + \\beta_2 x_2 + u$) and obtain the fitted values ($\\hat{y}$).
2. Re-run the model, introducing non-linear forms of $\\hat{y}$ (like $\\hat{y}^2$ and $\\hat{y}^3$) as additional regressors: $y = \\beta_1 x_1 + \\beta_2 x_2 + \\beta_3 \\hat{y}^2 + \\beta_4 \\hat{y}^3 + v$.
3. Calculate the $R^2$ for both models ($R_{old}^2$ and $R_{new}^2$).
4. Compute the F-statistic: $F = \\frac{(R_{new}^2 - R_{old}^2) / (number \\ of \\ new \\ regressors)}{(1 - R_{new}^2) / (n - number \\ of \\ new \\ parameters)}$.
5. If the F-value is statistically significant (e.g., at the 5% level), reject the null hypothesis of correct specification.

> **Quick Recall:**
> - RESET tests for incorrect functional form, NOT omitted variables.
> - It uses $\\hat{y}^2$ and $\\hat{y}^3$ as test variables.
> - A significant F-test means the original model is misspecified.
> - Limitation: It tells you the model is wrong, but not how to fix it.

### Connections
- Contrasts with tests for specific issues like Durbin-Watson for autocorrelation.

## Section: Model Selection Criteria 🟡
<!-- This section continues into chunk 002 -->

### Core Idea
When evaluating competing econometric models that attempt to explain the same phenomenon, researchers rely on specific statistical criteria to measure goodness of fit and determine which model provides the most accurate and parsimonious representation of the data.

> **In Simple Terms:** When you have multiple models trying to explain the same thing, you need a scoring system to decide which one is the "best."

### Key Concepts

#### R-squared and Adjusted R-squared
The coefficient of determination ($R^2$) measures the explanatory power or goodness of fit of a regression model, representing the proportion of variation in the dependent variable explained by the independent variables. 

However, $R^2$ has severe limitations for model selection:
- It only measures **in-sample** goodness of fit and cannot forecast out-of-sample observations.
- It can only compare models that share the exact same dependent variable.
- Its value **never decreases** when additional regressors are added, even if they are completely irrelevant. This can tempt researchers to arbitrarily add variables to inflate the $R^2$, which ultimately increases the variance of the forecast error and ruins model precision.

### Definitions
- **R-squared ($R^2$)**: The ratio of the explained sum of squares to the total sum of squares, measuring the proportion of variation in the dependent variable explained by the model.

### Mechanisms / Processes
$R^2 = \\frac{\\text{explained sum of squares}}{\\text{total sum of squares}} = 1 - \\frac{\\text{residual sum of squares}}{\\text{total sum of squares}}$

<!-- This section continues in chunk 002 -->


---


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
- Builds on: Model Selection Criteria (Chunk 001: Possible Problems in Specification)

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
- Prerequisite for: Consequences of Autocorrelation (Chunk 002: Model Selection Criteria)

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


---


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
- Builds on: Concept of Autocorrelation (Chunk 002: Model Selection Criteria)

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
- Solves problems raised in: Consequences of Autocorrelation (Chunk 003: Consequences of Autocorrelation)

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
- Fixes issues from: Consequences of Autocorrelation (Chunk 003: Consequences of Autocorrelation)

<!-- This section continues in chunk 004 -->


---

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
- Solves problems raised in: Remedial Measures for Autocorrelation (Chunk 003: Consequences of Autocorrelation)

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
- Prerequisite for: Consequences of Multicollinearity (Chunk 004: Methods of Estimating \rho)

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
- Leads to: Detection of Multicollinearity (Chunk 004: Methods of Estimating \rho)

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


---

<!-- Structure adjusted: Consequences and Detection were fully covered in chunk 004 -->

## Section: Consequences of Multicollinearity 🔴
<!-- See chunk 004 for the beginning and end of this section -->
> *Note: The core content for this section was completely extracted in Chunk 004 due to document boundaries.*

## Section: Detection of Multicollinearity 🔴
<!-- See chunk 004 for the beginning of this section -->
> *Note: The core content for this section was completely extracted in Chunk 004 due to document boundaries. The concluding thought from page 43 is simply that if t-ratios remain statistically significant despite high pair-wise correlation, multicollinearity is not a serious practical issue.*

## Section: Remedial Measures for Multicollinearity 🔴
<!-- This section starts here -->
<!-- Exam importance: 🔴 HIGH YIELD -->
<!-- Reason: Key solutions to fix multicollinearity are frequent exam topics -->

### Core Idea
Because multicollinearity is primarily a sample-specific data deficiency rather than a theoretical error, the best solutions involve obtaining more information. Mathematical fixes like dropping variables, Ridge Regression, or Principal Component Analysis (PCA) can help stabilize the model but usually force the researcher to sacrifice either the unbiasedness of the estimators or the economic interpretability of the results.

> **In Simple Terms:** Since the math can't separate two highly correlated variables, you have to either bring in outside information, measure them differently, or use advanced "hacks" that give you a stable answer but might be slightly biased.

### Key Concepts

#### 1. Dropping one of the correlated variables
This is the simplest fix but the most dangerous. While it eliminates the collinearity and reduces the variance of the remaining variable, it introduces **omission bias**. If economic theory dictates that the dropped variable should be in the model, removing it violates the model's true specification. OLS estimators lose their "unbiased" status, which is generally considered a worse problem than the inefficiency caused by multicollinearity.

#### 2. Ignoring it
Since OLS estimators remain BLUE (Best Linear Unbiased Estimators) even under multicollinearity, sometimes the best action is no action. If the model is statistically adequate, the coefficients have their theoretically expected signs, and the t-ratios are still significant, the problem can be ignored. 

#### 3. Transforming Variables
- **Ratio transformations**: Expressing variables in per capita terms or as percentages of GDP. (Caveat: this can induce heteroscedasticity).
- **First differences**: $\\Delta y_t$ on $\\Delta x_t$. (Caveat: this reduces degrees of freedom by losing one observation and may worsen autocorrelation if not careful).

#### 4. Expanding the sample size
Since multicollinearity is a sample problem, collecting more data—or pooling cross-sectional and time-series data—can introduce enough random variation to break the collinear pattern.

#### 5. Using extraneous estimates & a priori information
- **Extraneous estimates**: Borrowing parameter estimates from other studies (e.g., using income elasticity from a cross-sectional budget study to fix a time-series model).
- **A priori information**: Using economic theory to impose mathematical constraints. For example, applying the Constant Returns to Scale constraint ($\\alpha + \\beta = 1$) in a Cobb-Douglas production function allows you to eliminate one parameter by substituting $\\beta = 1 - \\alpha$.

#### 6. Ridge Regression
This is a biased estimation technique. By artificially adding a constant ($\\lambda$) to the diagonal elements of the $X'X$ variance-covariance matrix, it forcefully decreases the intercorrelation. 
- **Trade-off**: The estimators become biased, but their Mean Squared Error (MSE) declines compared to standard OLS. 
- **Limitation**: Choosing the value of $\\lambda$ is highly subjective.

#### 7. Principal Components Regression (PCA)
PCA transforms '$k$' highly correlated explanatory variables into '$k$' completely uncorrelated (orthogonal) artificial indices known as principal components ($z_1, z_2, \\dots, z_k$). The regression is then run on these components instead.
- **Limitation**: The resulting components often make absolutely no economic sense (e.g., a variable representing $2 \\times \\text{Income} + 3 \\times \\text{Price}$ is meaningless to interpret).

#### 8. Generalized Inverse Solution
Used mathematically when the $X'X$ matrix is singular (determinant is zero) due to perfect multicollinearity, preventing the standard $X'X^{-1}$ calculation.

### Definitions
- **Omission bias**: The bias introduced into the remaining parameter estimators when a theoretically relevant variable is deliberately dropped from the model. ⭐ (exam-important)
- **Ridge Regression**: An estimation technique that resolves severe multicollinearity by adding a small constant penalty ($\\lambda$) to the variance, resulting in biased but more stable (lower MSE) estimators. ⭐ (exam-important)
- **Principal Component Analysis (PCA)**: A multivariate technique that transforms a set of correlated explanatory variables into a set of completely uncorrelated linear combinations (components). ⭐ (exam-important)

### Mechanisms / Processes
**The Trade-off of Dropping a Variable:**
1. True model: $y = \\beta_1 x_1 + \\beta_2 x_2 + u$
2. Estimated model with $x_2$ dropped: $y = \\beta_1^* x_1 + v$
3. Resulting Variance: $Var(\\beta_1^*) = \\frac{\\sigma^2}{\\sum x_1^2}$. This is strictly smaller than the OLS variance under collinearity.
4. Resulting Bias: $E(\\beta_1^*) = \\beta_1 + \\beta_2 \\frac{\\sum x_1 x_2}{\\sum x_1^2}$. The estimator is biased by the effect of $x_2$.

### ⚠️ Common Mistakes
- ❌ Mistake: Immediately dropping a variable when high correlation is detected. → ✅ Correct: Never drop a theoretically relevant variable just to fix collinearity; the resulting omitted variable bias is mathematically worse than multicollinearity.

> **Quick Recall:**
> - Doing nothing is a valid solution if t-ratios are still significant.
> - Dropping variables fixes variance but creates omitted variable bias.
> - Ridge regression creates biased estimators but lowers Mean Squared Error.
> - PCA creates uncorrelated variables but destroys economic interpretability.
> - The best pure fix is collecting more data or using theoretical constraints.

### Connections
- Solves problems raised in: Consequences of Multicollinearity (Chunk 004: Methods of Estimating \rho)


---


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
- Prerequisite for: Consequences of Heteroscedasticity (Chunk 006: Concept of Heteroscedasticity)

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


---


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
- Completes the tests started in: Detection of Heteroscedasticity (Chunk 006: Concept of Heteroscedasticity)

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
- Fixes issues from: Consequences of Heteroscedasticity (Chunk 006: Concept of Heteroscedasticity)

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


---


## Section: Consequences of Errors in Variables 🔴

### Core Idea
The consequence of measurement error depends entirely on which variable is flawed. If the dependent variable ($Y$) is measured with error, the estimators remain unbiased but lose efficiency. However, if the independent variable ($X$) is measured with error, the OLS estimators become biased and inconsistent, systematically underestimating the true relationship.

> **In Simple Terms:** If the thing you are trying to predict ($Y$) has measurement errors, your model will just be a bit less confident (wider confidence intervals), but the core guess is still accurate. But if the input data ($X$) has errors, the entire math breaks down, and your model's guesses will be systematically wrong forever, no matter how much data you add.

### Key Concepts

#### Measurement Error in Y
Let the true model be $y_i = \\beta x_i + \\varepsilon_i$, but we observe $y_i^* = y_i + u_i$.
- Because $u_i$ is just a measurement error in $Y$, it simply merges into the stochastic disturbance term: $y_i^* = \\beta x_i + (\\varepsilon_i + u_i)$.
- **Consequence**: The explanatory variable $x_i$ remains uncorrelated with the new composite error term. Therefore, the OLS estimator $\\hat{\\beta}$ remains **unbiased**.
- **Drawback**: The variance of the estimator increases from $\\frac{\\sigma_\\varepsilon^2}{\\sum x_i^2}$ to $\\frac{\\sigma_\\varepsilon^2 + \\sigma_u^2}{\\sum x_i^2}$. The estimates are less precise.

#### Measurement Error in X
Let the true model be $y_i = \\beta x_i + \\varepsilon_i$, but we observe $x_i^* = x_i + \\nu_i$.
- Substituting this into the true equation gives $y_i = \\beta x_i^* + (\\varepsilon_i - \\beta \\nu_i)$.
- **Consequence**: The new independent variable $x_i^*$ is now correlated with the new composite error term (because both contain $\\nu_i$). This violates the most critical OLS assumption.
- **Result**: The OLS estimator becomes **biased and inconsistent**. Even in an infinitely large sample, the estimator evaluates to:
  $plim \\hat{\\beta} = \\beta \\left( \\frac{1}{1 + \\sigma_\\nu^2 / \\sigma_x^2} \\right)$.
  Because the denominator is greater than 1, $\\hat{\\beta}$ systematically **underestimates** the true parameter $\\beta$.

#### Measurement Errors in both X and Y
When both variables are measured with error, the problems stack. The estimator remains inconsistent and systematically biased downward.

### Examples
**The Permanent Income Hypothesis:**
Measured income ($Y^*$) consists of permanent (true) income ($Y$) and transitory (error) income ($Y_\\varepsilon$). If we use measured income ($Y^*$) to estimate the Marginal Propensity to Consume (MPC), the measurement error ($\\nu_i$) causes the OLS estimator to systematically underestimate the true MPC. The larger the variance in transitory income, the worse the underestimation.

> **Quick Recall:**
> - Error in $Y$: OLS is unbiased but inefficient (higher variance).
> - Error in $X$: OLS is biased and inconsistent (underestimates true $\\beta$).
> - Measurement error violates the assumption that $Cov(x_i, u_i) = 0$.

### Connections
- Prerequisite for: Instrumental Variables Method (Chunk 008: Consequences of Errors in Variables)

## Section: Instrumental Variables Method 🔴

### Core Idea
To solve the inconsistency caused by measurement error in $X$, we replace the flawed $X$ variable with a new proxy variable $Z$, known as an **Instrumental Variable**. To work, $Z$ must be highly correlated with the true $X$, but completely uncorrelated with the measurement errors.

> **In Simple Terms:** If your thermometer ($X$) is broken and gives random errors, you can't use it in your math. Instead, you find a proxy ($Z$), like the amount of ice melting outside. It correlates perfectly with the true temperature but isn't affected by the broken thermometer's errors.

### Key Concepts

#### Conditions for an Instrument
A random variable $Z$ is a valid instrument if it strictly meets two conditions as sample size gets large:
1. **Relevance**: The correlation between $Z$ and the true explanatory variable $X$ must be non-zero (they must be highly correlated).
2. **Exogeneity**: The correlation between $Z$ and the error terms (both the equation error $\\varepsilon$ and the measurement error $\\nu$) must be strictly zero.

#### Instrumental Variables Estimator
Instead of using the standard OLS formula $\\hat{\\beta}_{OLS} = \\frac{\\sum x_i^* y_i}{\\sum (x_i^*)^2}$, we use the Instrumental Variables (IV) estimator:
$\\hat{\\beta}_{IV} = \\frac{\\sum z_i y_i}{\\sum z_i x_i^*}$
By using $z_i$ in the numerator, the estimator mathematically approaches the true $\\beta$ as the sample size grows.

### Definitions
- **Instrumental Variable (IV)**: A proxy variable $Z$ used in regression analysis that is highly correlated with the explanatory variable but uncorrelated with the error term, used to obtain consistent estimators when variables are measured with error. ⭐ (exam-important)

### Edge Cases & Caveats
- **Consistency vs Unbiasedness**: IV guarantees **consistency** (it will eventually hit the true parameter if you have an infinitely large sample), but it does NOT guarantee **unbiasedness** (in small samples, it may still be biased).
- OLS is actually just a special case of the IV method where $X$ is used as its own instrument (which only works if $X$ has no measurement error).

> **Quick Recall:**
> - IV solves Measurement Error in $X$.
> - Instrument $Z$ must be: 1. Correlated with $X$. 2. Uncorrelated with error $u$.
> - IV formula: $\\sum zy / \\sum zx^*$.
> - IV provides consistent, but not necessarily unbiased, estimates.

### Connections
- Fixes issues from: Consequences of Errors in Variables (Chunk 008: Consequences of Errors in Variables)

## Section: Test of Measurement Errors 🔴
<!-- This section continues into chunk 009 -->

### Core Idea
We can test whether our model is suffering from measurement error in the independent variables by using a two-stage regression procedure known as the Hausman Specification Test, which compares the results of standard OLS against the Instrumental Variables method.

### Key Concepts

#### Hausman Specification Test
This test relies on a theoretical principle:
- Under the null hypothesis ($H_0$: No measurement error): Both OLS and IV are consistent, but OLS is efficient.
- Under the alternative hypothesis ($H_1$: Measurement error exists): OLS is inconsistent, but IV remains consistent.

**Testing Procedure:**
1. Regress the flawed variable $x^*$ on the instrument $z$ to obtain the residuals, $\\hat{w}_i$.
2. Regress the dependent variable $y$ on both $x^*$ and the generated residuals $\\hat{w}_i$.
3. Perform a $t$-test on the coefficient of $\\hat{w}_i$ (let's denote it as $\\delta$).
4. If $\\delta$ is statistically significantly different from zero, reject the null hypothesis and conclude that measurement error is present.

### Definitions
- **Hausman Specification Test**: A statistical test used to detect measurement errors (or endogeneity) by comparing the consistency of OLS estimators against Instrumental Variables estimators. ⭐ (exam-important)

<!-- This section continues in chunk 009 -->


---


## Section: Test of Measurement Errors (Continued) 🔴
<!-- This section completes the topic started in chunk 008 -->

### Example of Hausman Test
Suppose we want to estimate state expenditures based on federal aid, income, and population. "Federal aid" is suspected to have measurement error. 
1. We use "population of school children" as an instrument ($Z$) and regress aid on $Z$ to get residuals $\\hat{w}$.
2. We add $\\hat{w}$ to the original expenditure regression.
3. If the t-statistic of $\\hat{w}$ is significant (e.g., at the 10% level), we conclude measurement error is present, and we notice that correcting for it substantially lowers the coefficient on the aid variable.

## Section: Inverse Regression 🔴

### Core Idea
When both variables $Y$ and $X$ are measured with error, researchers sometimes compute two regressions to establish boundaries for the true parameter. 

### Key Concepts

#### Direct vs Inverse Regression
- **Direct Regression**: Regressing $Y^*$ (measured dependent) on $X^*$ (measured independent). (e.g., Salary on Qualifications).
- **Inverse (Reverse) Regression**: Regressing $X^*$ on $Y^*$. (e.g., Qualifications on Salary).

#### Use Cases
Inverse regression is frequently advocated in salary discrimination analysis. Instead of asking "Do men get paid more for the same qualifications?" (Direct), the inverse regression asks "Do men have lower qualifications for the same pay?" (Inverse). 
- **Statistical Reality**: Because of the usual errors-in-variables problem, neither the direct nor the inverse regression alone gives the perfectly correct estimate. Instead, the estimates from both regressions are used to establish theoretical **bounds** for the true parameter $\\beta$.

### Connections
- Completes the unit on Errors in Variables (Unit 12).

## Section: Concept of Stochastic Regressors 🔴

### Core Idea
The classical linear regression model assumes that the values of the explanatory variables ($X$) are fixed in repeated samples (non-stochastic). However, in real-world economics and social sciences, the explanatory variables are almost always random variables themselves (stochastic). 

> **In Simple Terms:** We usually pretend that our input data, like a person's "years of schooling," is set in stone by the researcher before the experiment. In reality, "years of schooling" is random and varies unpredictably from person to person.

### Key Concepts

#### Relaxing OLS Assumptions
- **Non-Stochastic (Classical Assumption)**: If $X$ is fixed, there is absolutely no relationship between $X$ and the random error term $u$. Thus, $E(x_i u_i) = 0$.
- **Stochastic (Real-world)**: If $X$ is a random variable, there is a high possibility that $X$ and $u$ move together. If $E(x_i u_i) \\neq 0$, the core assumption of OLS is violated, causing estimators to become biased and inconsistent.

### Definitions
- **Stochastic Regressor**: An explanatory variable that is a random variable, rather than having fixed, predetermined values in repeated samples. ⭐ (exam-important)

### Connections
- Prerequisite for: Endogeneity Problem (Chunk 009: Test of Measurement Errors (Continued))

## Section: Endogeneity Problem 🔴

### Core Idea
Endogeneity occurs when an explanatory variable is correlated with the stochastic error term ($u$). When this happens, OLS estimators become biased and inconsistent, and standard regression analysis completely fails to isolate the true causal effect of $X$ on $Y$.

> **In Simple Terms:** Endogeneity means your input variable is tangled up with invisible "error" factors you couldn't measure. Because they move together, the math can't tell whether a change in the outcome is caused by your input variable or by the hidden error factor.

### Key Concepts

#### The Three Major Sources of Endogeneity:

1. **Omitted Variables**:
   If a relevant variable ($q$) is excluded from the model (often due to lack of data), its influence is absorbed into the stochastic error term ($u$). If the included explanatory variable ($x_j$) is correlated with the omitted variable ($q$), then $x_j$ becomes correlated with $u$. 

2. **Measurement Error**:
   As established in Unit 12, if an independent variable is measured with an additive error ($x^* = x + v$), that measurement error mathematically becomes part of the equation's overall error term. This mechanically forces a correlation between the observed variable $x^*$ and the error term $u$.

3. **Simultaneity (Reverse Causality)**:
   This occurs when an explanatory variable is determined simultaneously along with the dependent variable $Y$. Instead of a one-way street ($X \\rightarrow Y$), there is a two-way street ($X \\leftrightarrow Y$). 
   - *Example*: In a model predicting Earnings ($Y$) based on Years of Schooling ($X$), an unmeasured factor like "Innate Ability" falls into the error term ($u$). "Ability" positively impacts Earnings, but "Ability" *also* causes a person to stay in school longer. Therefore, $X$ (Schooling) is positively correlated with $u$ (Ability). A change in Earnings cannot be purely attributed to Schooling.

#### Remedies for Endogeneity
To resolve the endogeneity problem, econometricians rely on two main methods:
1. Instrumental Variables (IV) Method
2. Two-Stage Least Squares (2SLS) Method
Both methods provide **consistent** estimators (they converge to the true parameter as sample size approaches infinity).

### Definitions
- **Endogenous Variable**: An explanatory variable in a regression model that is correlated with the stochastic error term. ⭐ (exam-important)
- **Exogenous Variable**: An explanatory variable that is NOT correlated with the stochastic error term. ⭐ (exam-important)
- **Simultaneity (Reverse Causality)**: A situation where the explanatory variable is partly determined by the dependent variable, leading to a correlation with the error term (endogeneity). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that adding more data fixes endogeneity. → ✅ Correct: Endogeneity causes inconsistency. An inconsistent estimator will remain biased forever, even with an infinitely large sample size. You must change the estimation method (e.g., use IV).

> **Quick Recall:**
> - $E(X, u) = 0$ -> Exogenous (Good, OLS works).
> - $E(X, u) \\neq 0$ -> Endogenous (Bad, OLS is biased/inconsistent).
> - 3 Causes: Omitted variables, Measurement error, Simultaneity.

### Connections
- Builds upon: Omitted Variable Bias (Block 2) and Measurement Error (Chunk 008: Consequences of Errors in Variables).
- Leads to: Instrumental Variables and 2SLS (Chunk 010: Instrumental Variable Estimator).


---


## Section: Instrumental Variable Estimator 🔴

### Core Idea
When an explanatory variable ($x_K$) is endogenous (correlated with $u$), ordinary least squares fails. The Instrumental Variable (IV) method solves this by explicitly replacing the endogenous $x_K$ with an observable instrument ($z_1$) that is free of endogeneity.

> **In Simple Terms:** Because $x_K$ is "contaminated" by the hidden error term, we swap it out for a proxy variable $z_1$ that tracks $x_K$ perfectly but is entirely immune to the contamination.

### Key Concepts

#### IV Method Conditions
To use a variable $z_1$ as an instrument for $x_K$, it must satisfy two strict conditions:
1. **Exogeneity Condition**: $z_1$ must not be correlated with the stochastic error $u$. $Cov(z_1, u) = 0$. 
   - *Note*: This condition must simply be assumed/maintained by the researcher based on economic theory because $u$ is fundamentally unobservable, so this condition cannot be statistically tested.
2. **Relevance Condition**: $z_1$ must be correlated with the endogenous variable $x_K$, even after netting out the effects of all other exogenous variables in the model. 
   - *Note*: This condition *can* be statistically tested using a t-test on the reduced form equation.

#### Identification & Reduced Form
- **Reduced Form Equation**: Describes an endogenous variable strictly as a linear projection onto all available exogenous variables in the system. 
- By plugging the reduced form back into the structural equation, we solve the identification problem, allowing us to consistently estimate the true parameters.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that IV estimators are just as efficient as OLS estimators. → ✅ Correct: By using a proxy $z_1$ instead of the actual data $x_K$, we lose some information. This leads to larger error terms and larger standard errors. If the correlation between $z_1$ and $x_K$ is weak ("weak instruments"), the IV estimator will have unacceptably large standard errors.

### Connections
- Solves the problem introduced in: Endogeneity Problem (Chunk 009: Test of Measurement Errors (Continued))

## Section: Two-Stage Least Squares (2SLS) Estimator 🔴
<!-- This section continues into chunk 011 -->

### Core Idea
What happens if we have *more than one* valid instrument ($z_1, z_2, \\dots, z_M$) for a single endogenous variable? The Two-Stage Least Squares (2SLS) method mathematically combines all available instruments to create the single most efficient "super-instrument" possible.

> **In Simple Terms:** If you have five different imperfect proxies that all somewhat track the true variable, you don't just pick one at random. You blend them all together mathematically to create the most accurate possible synthetic proxy, and then you use that synthetic proxy in your final calculation.

### Key Concepts

#### Need for 2SLS
When there are multiple valid instruments, there are multiple possible IV estimators. Any linear combination of the valid instruments is theoretically uncorrelated with the stochastic error $u$. 2SLS is the systematic process of choosing the specific linear combination that has the **maximum possible correlation** with the endogenous explanatory variable ($x_K$).

#### The Two-Stage Process
2SLS involves applying the ordinary least squares (OLS) method twice in sequence:

**Step 1: First-Stage Regression**
1. Regress the endogenous variable $x_K$ on **all** exogenous variables in the model AND **all** available instrumental variables ($z_1, z_2, \\dots, z_M$) using OLS.
2. Obtain the fitted (predicted) values from this regression, denoted as $\\hat{x}_K$. This $\\hat{x}_K$ is now our optimal, purified instrument.

**Step 2: Second-Stage Regression**
1. Regress the dependent variable $y$ on the original exogenous variables and the newly generated fitted values $\\hat{x}_K$ (replacing the original $x_K$) using OLS.
2. The resulting parameters are the 2SLS estimators.

### Definitions
- **Two-Stage Least Squares (2SLS)**: An estimation technique used when there are multiple instruments available for an endogenous variable, involving a first-stage regression to create an optimal fitted instrument, and a second-stage regression to estimate the main model. ⭐ (exam-important)

### Edge Cases & Caveats
- If there is exactly **one** instrument for **one** endogenous variable (exact identification), the IV estimator and the 2SLS estimator will yield mathematically identical results. 2SLS is only distinct when there are more instruments than endogenous variables (overidentification).

> **Quick Recall:**
> - Stage 1: Predict endogenous $X$ using all instruments. (Purification phase)
> - Stage 2: Run main regression using predicted $\\hat{X}$. (Estimation phase)
> - 2SLS is the most efficient IV estimator when multiple instruments exist.

<!-- This section continues in chunk 011 -->


---


## Section: Two-Stage Least Squares (2SLS) Estimator (Continued) 🔴
<!-- This section continues from chunk 010 -->

### Core Idea
When there are multiple potential instrumental variables ($z_h$) available, there are multiple possible Instrumental Variable (IV) estimators. The 2SLS method resolves the dilemma of choosing among them by mathematically combining all instruments into a single optimal estimation process.

### Key Concepts

#### Summary of Methods
- If an explanatory variable is correlated with the error term, we face the endogeneity problem, and the OLS estimator is biased and inconsistent.
- To solve this, we use the Instrumental Variable (IV) method. An instrument must be strongly correlated with the endogenous variable and completely uncorrelated with the error term.
- Because there are often many more instrumental variables available than endogenous variables (e.g., any linear combination of $z_1, z_2, \\dots, z_M$), the 2SLS method is employed.
- **Why 2SLS is preferred**: The 2SLS estimator mathematically guarantees the most efficient (minimum variance) IV estimator possible when multiple instruments are present.

### Quick Recall
- Endogeneity -> Use IV.
- Multiple Instruments -> Use 2SLS.
- 2SLS provides the most efficient IV estimator.

### Connections
- Concludes the unit on Stochastic Regressors (Unit 13).
- Concludes Block-3 of MECE-101.


---

