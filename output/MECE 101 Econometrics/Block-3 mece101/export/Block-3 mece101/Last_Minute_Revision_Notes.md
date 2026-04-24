# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics


### Possible Problems in Specification 🔴

**Importance of Model Specification**

**Sources of Specification Error**
1. Inclusion of redundant/irrelevant variables
2. Omission of relevant variables
3. Incorrect functional form (e.g., using a linear model when the true relationship is non-linear like Cobb-Douglas or quadratic)
4. Incorrect assumptions regarding the error term (e.g., non-zero mean, heteroscedasticity, autocorrelation)
5. Error in measurement of variables (which is distinct from the error term; measurement error occurs when a variable is included but measured incorrectly, such as using "years of schooling" as a proxy for "education")

**Implications of Specification Error**
- **Specification Error**: Errors arising from incorrect model formulation, including omitted/irrelevant variables, wrong functional forms, incorrect error term assumptions, or measurement errors. ⭐ (exam-important)
- **Measurement Error**: Errors resulting from incorrect measurement of a variable included in the model, often due to proxies, reporting errors, or data collection issues.
1. Theoretical model formulation based on economic logic.
2. Selection of relevant variables and appropriate functional form.
3. Verification of OLS assumptions (linearity, no measurement error, no perfect multicollinearity, zero error mean, homoscedasticity, no autocorrelation).

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing the "error term" with "measurement error." → ✅ Correct: The error term reflects excluded variables that influence the dependent variable. Measurement error reflects inaccuracies in measuring the variables that *are* included in the model.

**Quick Recall:**
- Specification is the most critical step; errors here ruin estimation.
- The five sources of specification error are: omitted variables, irrelevant variables, wrong functional form, wrong error assumptions, and measurement errors.
- Measurement error is distinct from the stochastic error term.
- Prerequisite for: Inclusion of Variables in a Model (Chunk 001)
- How do we specifically test for measurement error if the true variables are unobservable?

### Inclusion of Variables in a Model 🔴

**Inclusion of Irrelevant Variables**
- The estimators of the parameters remain **unbiased** ($E(\\hat{\\beta}_1) = \\beta_1$).
- The coefficient for the irrelevant variable will have an expected value of 0.
- The **efficiency** of the estimators declines (variance increases).
- The larger variance reduces precision, causing wider confidence intervals and increasing the probability of a **Type II error** (failing to reject a false null hypothesis).
- The $R^2$ value increases artificially.

**Omission of Relevant Variables**
- Its impact is absorbed into the residuals, causing them to show a systematic pattern (e.g., autocorrelation detectable by the Durbin-Watson statistic).
- The estimators of the included parameters become **biased**. The bias is equal to: (coefficient of the excluded variable, $\\beta_2$) $\\times$ (regression coefficient of the excluded variable on the included variable, $b_{21}$).
- The variance of the estimators is biased (often an over-estimate).
- Conventional hypothesis tests and confidence intervals become **invalid**, leading to faulty inferences.

**Top-down vs. Bottom-up Approaches**
- **General-to-specific (Top-down)**: Start with a large model including many variables and drop the statistically insignificant ones. This is preferred by researchers to avoid the severe biases of omitting relevant variables.
- **Specific-to-general (Bottom-up)**: Start with a simple model and add variables. This is criticized because nominal significance levels differ from true significance levels if relevant variables are missing.
- **Type II Error**: The error of not rejecting a null hypothesis when the null hypothesis is actually false.
1. Assume true model: $y = \\beta_1 x_1 + \\beta_2 x_2 + u$
2. Estimated incorrect model: $y = \\beta_1^* x_1 + e$
3. The expected value of the biased estimator is: $E(\\beta_1^*) = \\beta_1 + \\beta_2 b_{21}$
4. The bias is exactly $\\beta_2 b_{21}$.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that adding more variables always makes a model better. → ✅ Correct: While omitting variables causes severe bias, adding irrelevant variables decreases the model's efficiency and widens confidence intervals.

**Quick Recall:**
- Irrelevant variable included → Unbiased but inefficient estimators. Increases risk of Type II error.
- Relevant variable omitted → Biased estimators, biased variance, invalid hypothesis tests.
- Bias formula: $Bias = \\beta_{excluded} \\times b_{(excluded \\ on \\ included)}$.
- General-to-specific modeling is preferred over specific-to-general.
- Builds on: Possible Problems in Specification (Chunk 001)

### Specification Error Test (RESET) 🔴

**RESET Method**

**Limitations of RESET**
- **RESET (Regression Specification Error Test)**: A general test for model misspecification that checks if non-linear functional forms of the estimated dependent variable improve the model's fit. ⭐ (exam-important)
1. Estimate the original model (e.g., $y = \\beta_1 x_1 + \\beta_2 x_2 + u$) and obtain the fitted values ($\\hat{y}$).
2. Re-run the model, introducing non-linear forms of $\\hat{y}$ (like $\\hat{y}^2$ and $\\hat{y}^3$) as additional regressors: $y = \\beta_1 x_1 + \\beta_2 x_2 + \\beta_3 \\hat{y}^2 + \\beta_4 \\hat{y}^3 + v$.
3. Calculate the $R^2$ for both models ($R_{old}^2$ and $R_{new}^2$).
4. Compute the F-statistic: $F = \\frac{(R_{new}^2 - R_{old}^2) / (number \\ of \\ new \\ regressors)}{(1 - R_{new}^2) / (n - number \\ of \\ new \\ parameters)}$.
5. If the F-value is statistically significant (e.g., at the 5% level), reject the null hypothesis of correct specification.

**Quick Recall:**
- RESET tests for incorrect functional form, NOT omitted variables.
- It uses $\\hat{y}^2$ and $\\hat{y}^3$ as test variables.
- A significant F-test means the original model is misspecified.
- Limitation: It tells you the model is wrong, but not how to fix it.
- Contrasts with tests for specific issues like Durbin-Watson for autocorrelation.

**Quick Recall:**
- $R^2$ always increases with more variables; Adjusted-$R^2$ penalizes extra variables.
- For AIC, SIC, and Mallow's $C_p$: **Lower is better.**
- Statistical criteria can never substitute economic theory and common sense.

### Concept of Autocorrelation 🔴

**Spatial Correlation**

**Serial Correlation / Autocorrelation**
- Non-stationarity of the series (mean/variance changes over time).
- Omission of a relevant variable (the error term absorbs its systematic effect).
- Incorrect functional form (fitting a straight line to a curve creates a pattern in errors).
- Interpolation and extrapolation of data.
- Inertia or lagged effects (e.g., current consumption heavily depends on past habits).
- **Autocorrelation**: The correlation between successive error terms in a dataset, most commonly in time series data. Mathematically, $E(u_i, u_j) \\neq 0$ for $i \\neq j$. ⭐ (exam-important)
- **First order autocorrelation**: The correlation between the error term at time $t$ ($u_t$) and the immediately preceding error term ($u_{t-1}$).
- **Spatial Correlation**: Correlation between error terms in cross-sectional data due to geographic or social proximity.
- **Auto-regressive AR(1) process**: The current error depends on a proportion of the previous error plus a random shock.
- **Moving Average MA(1) process**: The current error depends on the current random shock plus a proportion of the previous period's random shock.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing autocorrelation only happens when the model is mathematically wrong. → ✅ Correct: It often happens simply due to the nature of time-series data (momentum, inertia, changing habits).

**Quick Recall:**
- Autocorrelation = $E(u_i, u_j) \\neq 0$.
- AR(1) formula: $u_t = \\rho u_{t-1} + \\varepsilon_t$.
- Causes: omitted variables, wrong functional form, inertia, data manipulation.
- Prerequisite for: Consequences of Autocorrelation (Chunk 002)

### Consequences of Autocorrelation 🔴

**Unbiasedness**

**Minimum Variance**
- **White noise**: A purely random error term ($\\varepsilon_t$) that has a zero mean, constant variance, and no covariance with other periods. ⭐ (exam-important)

### Consequences of Autocorrelation 🔴

**Biasedness of Var(OLS estimator)**
- The true variance of the estimator $Var(\\hat{\\beta})_{AR(1)}$ is multiplied by an inflation factor of $\\frac{1+\\rho r}{1-\\rho r}$ (where $r$ is the autocorrelation of $x$).
- If both $\\rho$ and $r$ are positive, the standard OLS formula **underestimates** the true variance ($E(\\hat{\\sigma}^2) < \\sigma^2$).
- Using the standard OLS variance leads to biased results. When the true $Var(\\hat{\\beta})_{AR(1)}$ is used instead, confidence intervals are wider than those obtained from Generalized Least Squares (GLS). This increases the likelihood of incorrectly accepting the null hypothesis (declaring a significant variable as insignificant).
- **GLS (Generalized Least Squares)**: An estimation procedure that transforms variables to account for autocorrelation, producing estimators that have minimum variance (BLUE).
1. The OLS variance formula assumes zero covariance between errors.
2. Under AR(1), $E(\\sum \\hat{u}_t^2) = \\sigma^2 \\left[T - \\frac{1+\\rho r}{1-\\rho r}\\right]$.
3. Therefore, $E(\\hat{\\sigma}^2) \\neq \\sigma^2$. The bias depends on the signs of $\\rho$ and $r$.

**Quick Recall:**
- OLS estimators are unbiased but NOT minimum variance (not BLUE).
- OLS variance is biased (usually underestimating the true variance).
- Standard hypothesis tests ($t$-test, $F$-test) become invalid.
- Builds on: Concept of Autocorrelation (Chunk 002)

### Detection of Autocorrelation 🔴

**Residual Plot**
- A linear trend (upward/downward), cyclical, or quadratic pattern indicates autocorrelation.
- Positive autocorrelation often clusters positive residuals together and negative residuals together.
- Limitation: It is highly subjective.

**Durbin-Watson (DW) Test**
- **Formula approximation**: $d \\approx 2(1 - \\hat{\\rho})$
- Because $-1 \\le \\hat{\\rho} \\le 1$, the test statistic $d$ ranges from 0 to 4.
  - $d \\approx 2$: No autocorrelation.
  - $d$ near 0: Positive autocorrelation.
  - $d$ near 4: Negative autocorrelation.
- **Limitations**: The test has a "zone of indecision" between critical limits $d_L$ and $d_U$ where no conclusion can be drawn. It requires an intercept, assumes non-stochastic regressors, and strictly tests only for AR(1) processes without lagged dependent variables.

**Breusch-Godfrey (BG) Test**
- **Durbin-Watson Test**: A statistical test used to detect the presence of first-order autocorrelation in the residuals of a regression. ⭐ (exam-important)
- **Breusch-Godfrey (BG) Test**: A generalized test for autocorrelation that can detect higher-order autoregressive and moving average processes. ⭐ (exam-important)
1. Estimate the primary regression using OLS and get residuals $\\hat{u}_t$.
2. Run an auxiliary regression: regress $\\hat{u}_t$ on all original $X$ variables PLUS lagged values of the residuals ($\\hat{u}_{t-1}, \\hat{u}_{t-2}, \\dots, \\hat{u}_{t-p}$).
3. Calculate the test statistic: $(T-p)R^2$, which follows a Chi-square ($\\chi^2$) distribution with $p$ degrees of freedom in large samples.
4. If the computed value exceeds the tabulated $\\chi^2$ value, reject the null hypothesis of no autocorrelation.

### ⚠️ Common Mistakes
- ❌ Mistake: Concluding there is no autocorrelation if $d$ falls in the "zone of indecision". → ✅ Correct: The test is simply inconclusive; you must use an alternative test like the BG test.

**Quick Recall:**
- DW $d \\approx 2$: No autocorrelation. DW $d \\approx 0$: Positive. DW $d \\approx 4$: Negative.
- DW has a zone of indecision and only tests AR(1).
- BG (LM) test overcomes DW limits: tests AR(p), MA processes, and allows lagged dependent variables.
- Solves problems raised in: Consequences of Autocorrelation (Chunk 003)

### Remedial Measures for Autocorrelation 🔴

**Quasi-first Differencing**
- The Prais-Winsten transformation is used to save the first observation from being lost during differencing.
- Limitation: $\\rho$ is rarely known and must be estimated (making it Feasible GLS / FGLS).

**First-Differencing**

**The Newey-West Method**
- It is an extension of White's standard errors.
- It is only valid for **large samples**.
- **Quasi-first Differencing**: A GLS transformation technique where a proportion ($\\rho$) of the previous period's value is subtracted from the current value to eliminate AR(1) autocorrelation.
- **First-Differencing**: A transformation where the previous period's value is entirely subtracted from the current value (assuming $\\rho = +1$) to induce stationarity.
- **Newey-West Method**: A technique that corrects OLS standard errors for both heteroscedasticity and autocorrelation in large samples. ⭐ (exam-important)
1. Check if the Durbin-Watson statistic is very small (rule of thumb: $d < R^2$).
2. If true, it implies $\\rho \\approx 1$.
3. Run the regression on the differences ($\\Delta y_t$ on $\\Delta x_t$).

**Quick Recall:**
- Ensure autocorrelation is "pure" before applying remedies.
- GLS / Quasi-differencing restores estimators to BLUE by removing the AR(1) pattern.
- First-differencing is used when $\\rho = 1$ (unit root).
- Newey-West provides HAC standard errors for large samples without changing the OLS estimators.
- Fixes issues from: Consequences of Autocorrelation (Chunk 003)

**Quick Recall:**
- $\\rho$ must be estimated to run GLS.
- $\\hat{\\rho} \\approx 1 - d/2$.
- Iterative methods: Cochrane-Orcutt, Durbin's.
- Grid-search methods: Hildreth-Lu, Maximum Likelihood.

### Concept of Multicollinearity 🔴

**Perfect Multicollinearity**

**Near Multicollinearity**
- **Multicollinearity**: The presence of high correlation between explanatory variables in a multiple regression model. ⭐ (exam-important)
- **Perfect Multicollinearity**: A situation where two or more explanatory variables bear an exact linear relationship, making it impossible to uniquely estimate their coefficients. ⭐ (exam-important)
- **Orthogonal**: A state where independent variables are completely uncorrelated with one another.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing multicollinearity applies to non-linear relationships. → ✅ Correct: Multicollinearity specifically and exclusively refers to *linear* relationships between explanatory variables (e.g., $X_3 = X_1 + X_2^2$ does not violate the rule, because $X_2^2$ is a non-linear transformation).

**Quick Recall:**
- Multicollinearity violates the assumption of independent regressors.
- Perfect multicollinearity = impossible to estimate individual coefficients.
- Near multicollinearity = can estimate, but with huge standard errors.
- Prerequisite for: Consequences of Multicollinearity (Chunk 004)

### Consequences of Multicollinearity 🔴

**Estimator Properties**

**Five Major Consequences**
1. **Regression coefficients are indeterminate**: Under perfect multicollinearity, there are infinite solutions for the coefficients.
2. **Standard errors are inflated**: As the correlation ($r_{12}$) between variables approaches 1, the variance formula denominator approaches 0, driving the variance and standard error toward infinity.
3. **Wider confidence intervals**: Inflated standard errors lead to wide confidence intervals, drastically increasing the chance of a **Type II error** (failing to reject a false null hypothesis).
4. **High $R^2$ but insignificant t-ratios**: The overall model explains the data very well (the F-test is highly significant), but when looking at individual variables, their t-tests are found to be statistically insignificant. This is the classic hallmark of multicollinearity.
5. **Extreme sensitivity**: The estimated coefficients swing wildly with small changes to the data or if an independent variable is added/removed.
- **Indeterminate coefficients**: A state in perfect multicollinearity where an infinite number of solutions exist for regression coefficients, preventing unique estimation.

**Quick Recall:**
- OLS estimators are STILL BLUE under multicollinearity.
- Standard errors inflate heavily.
- Classic symptom: High $R^2$ (significant F-test) but insignificant t-ratios.
- Results become highly sensitive to small data changes.
- Leads to: Detection of Multicollinearity (Chunk 004)

### Detection of Multicollinearity 🔴

**Various Tests to Detect Multicollinearity**
1. **Correlation Matrix**: Examining pair-wise correlations. High correlation (e.g., > 0.8) indicates multicollinearity. However, low pair-wise correlation does NOT guarantee absence of multicollinearity (three or more variables might be collectively collinear).
2. **High Standard Errors / Classic Symptom**: Observing high standard errors. But note: high standard errors can also be caused by a high $\\sigma^2$ or low variation in $X$, so it's not a foolproof indicator.
3. **Variance Inflation Factor (VIF)**: Measures how much the variance of an estimator is inflated by collinearity. $VIF_j = \\frac{1}{1 - R_j^2}$. As $R_j^2 \\to 1$, VIF approaches infinity.
4. **Tolerance (TOL)**: The inverse of VIF ($1 - R_j^2$). It ranges from 0 (perfect collinearity) to 1 (no collinearity).
5. **Klein's Rule of Thumb**: Suggests multicollinearity is a serious problem only if the $R_j^2$ of an auxiliary regression exceeds the overall model's $R^2$.
6. **Condition Number (CN)**: An overall measure derived from the maximum and minimum eigenvalues of the $X'X$ matrix. $CN = \\sqrt{\\frac{\\text{Maximum eigenvalue}}{\\text{Minimum eigenvalue}}}$. 
   - $CN = 1$: No collinearity.
   - $CN = 15$: Moderate collinearity.
   - $CN > 30$: Severe collinearity.

### Consequences of Multicollinearity 🔴

### Detection of Multicollinearity 🔴

### Remedial Measures for Multicollinearity 🔴

**1. Dropping one of the correlated variables**

**2. Ignoring it**

**3. Transforming Variables**
- **Ratio transformations**: Expressing variables in per capita terms or as percentages of GDP. (Caveat: this can induce heteroscedasticity).
- **First differences**: $\\Delta y_t$ on $\\Delta x_t$. (Caveat: this reduces degrees of freedom by losing one observation and may worsen autocorrelation if not careful).

**4. Expanding the sample size**

**5. Using extraneous estimates & a priori information**
- **Extraneous estimates**: Borrowing parameter estimates from other studies (e.g., using income elasticity from a cross-sectional budget study to fix a time-series model).
- **A priori information**: Using economic theory to impose mathematical constraints. For example, applying the Constant Returns to Scale constraint ($\\alpha + \\beta = 1$) in a Cobb-Douglas production function allows you to eliminate one parameter by substituting $\\beta = 1 - \\alpha$.

**6. Ridge Regression**
- **Trade-off**: The estimators become biased, but their Mean Squared Error (MSE) declines compared to standard OLS. 
- **Limitation**: Choosing the value of $\\lambda$ is highly subjective.

**7. Principal Components Regression (PCA)**
- **Limitation**: The resulting components often make absolutely no economic sense (e.g., a variable representing $2 \\times \\text{Income} + 3 \\times \\text{Price}$ is meaningless to interpret).

**8. Generalized Inverse Solution**
- **Omission bias**: The bias introduced into the remaining parameter estimators when a theoretically relevant variable is deliberately dropped from the model. ⭐ (exam-important)
- **Ridge Regression**: An estimation technique that resolves severe multicollinearity by adding a small constant penalty ($\\lambda$) to the variance, resulting in biased but more stable (lower MSE) estimators. ⭐ (exam-important)
- **Principal Component Analysis (PCA)**: A multivariate technique that transforms a set of correlated explanatory variables into a set of completely uncorrelated linear combinations (components). ⭐ (exam-important)
1. True model: $y = \\beta_1 x_1 + \\beta_2 x_2 + u$
2. Estimated model with $x_2$ dropped: $y = \\beta_1^* x_1 + v$
3. Resulting Variance: $Var(\\beta_1^*) = \\frac{\\sigma^2}{\\sum x_1^2}$. This is strictly smaller than the OLS variance under collinearity.
4. Resulting Bias: $E(\\beta_1^*) = \\beta_1 + \\beta_2 \\frac{\\sum x_1 x_2}{\\sum x_1^2}$. The estimator is biased by the effect of $x_2$.

### ⚠️ Common Mistakes
- ❌ Mistake: Immediately dropping a variable when high correlation is detected. → ✅ Correct: Never drop a theoretically relevant variable just to fix collinearity; the resulting omitted variable bias is mathematically worse than multicollinearity.

**Quick Recall:**
- Doing nothing is a valid solution if t-ratios are still significant.
- Dropping variables fixes variance but creates omitted variable bias.
- Ridge regression creates biased estimators but lowers Mean Squared Error.
- PCA creates uncorrelated variables but destroys economic interpretability.
- The best pure fix is collecting more data or using theoretical constraints.
- Solves problems raised in: Consequences of Multicollinearity (Chunk 004)

### Concept of Heteroscedasticity 🔴

**Homoscedasticity vs Heteroscedasticity**
- **Homoscedasticity**: The conditional variance of $u_i$ is equal to a constant $\\sigma^2$. $E(u_i^2) = Var(u_i) = \\sigma^2$.
- **Heteroscedasticity**: The conditional variance of $u_i$ varies across observations. $E(u_i^2) = Var(u_i) = \\sigma_i^2$ (notice the $i$ subscript on $\\sigma$).

**Causes in Cross-Section Data**
1. Inherent variations in behavior (e.g., spending habits of the rich vs poor).
2. Outliers in the data.
3. Massive differences in the scale of variables (e.g., comparing the GDP of a tiny state vs a massive state without adjusting to per-capita terms).
4. Incorrect data transformation.
- **Homoscedasticity**: The assumption that the variance of the stochastic disturbance term is finite and remains constant over the sample.
- **Heteroscedasticity**: The condition where the variance of the error term is not constant, but changes with the values of the independent or dependent variable. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Believing heteroscedasticity is common in time-series data. → ✅ Correct: It is most common in cross-sectional data. Autocorrelation is the typical problem for time-series data.

**Quick Recall:**
- Homo = same, Hetero = different. Scedasticity = scatter/variance.
- Constant variance: $Var(u_i) = \\sigma^2$.
- Non-constant variance: $Var(u_i) = \\sigma_i^2$.
- Prerequisite for: Consequences of Heteroscedasticity (Chunk 006)

### Consequences of Heteroscedasticity 🔴

**Unbiasedness of $\\hat{\\beta}$**

**Efficiency of $\\hat{\\beta}$**

**Biased Variance**
- Standard errors become unreliable.
- Confidence intervals become inappropriately wide or narrow.
- As a result, t-ratios and F-tests lead to faulty statistical inferences.
- **Weighted Least Squares (WLS)**: An estimation method where observations are weighted inversely by their variances to correct for heteroscedasticity, restoring efficiency (BLUE). ⭐ (exam-important)
1. Under homoscedasticity, $E(RSS) = (n-1)\\sigma^2$.
2. Under heteroscedasticity, $E(RSS)$ does not simplify this way. It depends on $\\sum \\sigma_i^2$.
3. Thus, the expected value of the OLS variance formula does not equal the true variance of the parameter.

**Quick Recall:**
- OLS is STILL unbiased.
- OLS is NO LONGER efficient (not BLUE).
- OLS variance is BIASED -> Hypothesis tests are INVALID.
- Leads to: Detection and Remedial Measures (Chunks 006, 007)

### Detection of Heteroscedasticity 🔴

**1. Residual Plot**

**2. Auxiliary Regression**

**3. Park Test**
- **Method**: Run the auxiliary regression $\\ln \\hat{u}_i^2 = \\alpha + \\beta \\ln X_i + v_i$.
- **Test**: If the coefficient $\\beta$ is statistically significant (reject $H_0: \\beta = 0$), heteroscedasticity is present.

**4. Glejser Test**
- **Test**: Regress $|\\hat{u}_i| = \\alpha + \\beta f(X_i) + v_i$. If $\\beta$ is significant, heteroscedasticity exists.

**5. Goldfeld-Quandt Test**
- **Method**: 
  1. Order the data by $X$ (lowest to highest).
  2. Omit '$c$' central observations to clearly separate the low and high extremes.
  3. Run separate OLS on the lower group (to get $RSS_1$) and upper group (to get $RSS_2$).
- **Test**: Compute $\\lambda = (RSS_2 / df) / (RSS_1 / df)$. If $\\lambda > F_{critical}$, reject homoscedasticity. 
- **Limitation**: Arbitrary choices of which variable to order by and how many middle observations to drop.

**6. Breusch-Pagan Test**
- **Test**: Regress $\\hat{u}_i^2$ on $z_1, z_2, \\dots$. Calculate the Explained Sum of Squares ($S_0$). The statistic $\\lambda = S_0 / 2\\hat{\\sigma}^4$ follows a $\\chi^2$ distribution.

**7. White's Test (Introduction)**
- **Method**: Regress $\\hat{u}_i^2$ on all independent variables, their squares, and all cross-products. (e.g., $X_2, X_3, X_2^2, X_3^2, X_2 X_3$).
- **Park Test**: A test for heteroscedasticity that regresses the natural log of squared residuals on the natural log of an explanatory variable. ⭐
- **Goldfeld-Quandt Test**: A test that orders observations by an explanatory variable, drops central data points, and compares the residual variances of the resulting high and low groups. ⭐

### Detection of Heteroscedasticity 🔴

**White's Test (continued)**
- In large samples, $n R^2$ follows a Chi-square ($\\chi^2$) distribution. The degrees of freedom equal the number of regressors in the auxiliary regression (excluding the intercept).
- If the computed $\\chi^2$ exceeds the critical value, we reject the null hypothesis of homoscedasticity.
- **Limitations**: 
  1. Adding squares and cross-products drastically reduces the degrees of freedom (especially with many $X$ variables).
  2. A significant result might actually indicate a **specification error** (e.g., omitting a relevant variable or using the wrong functional form) rather than pure heteroscedasticity. Thus, it is a joint test of both.
- **White's Test**: A general test for heteroscedasticity that regresses squared residuals on all independent variables, their squares, and cross-products. ⭐ (exam-important)
- Completes the tests started in: Detection of Heteroscedasticity (Chunk 006)

### Remedial Measures for Heteroscedasticity 🔴

**Weighted Least Squares (WLS)**
- The new error term becomes $v_i = \\frac{u_i}{z_i}$.
- The variance of the new error term is $Var(v_i) = \\sigma^2$, which is constant (homoscedastic).
- The regression is then run on the transformed variables **without an intercept term**.
- Common patterns: If $Var(u_i)$ is proportional to $x_i$, divide by $\\sqrt{x_i}$. If it is proportional to $x_i^2$, divide by $x_i$.

**Two-Step WLS**
1. Run standard OLS to obtain the estimated coefficients $\\hat{\\alpha}$ and $\\hat{\\beta}$.
2. Use these to find the predicted values $\\hat{y}_i$.
3. Divide the original equation by $\\hat{y}_i$ and run the regression. Standard errors here are only asymptotically valid because the weights are estimated, not known perfectly.

**Generalised Least Squares (GLS)**

**White's Estimator (Robust Standard Errors)**
- **Advantage**: It does not require knowing the pattern of heteroscedasticity.
- **Limitation**: It is strictly a **large-sample** procedure. It may be less efficient than a proper WLS transformation.

**Logarithmic Transformation & Deflators**
- **Log Transformation**: Taking the natural log of variables (e.g., Cobb-Douglas $\\ln Y = \\ln A + \\alpha \\ln K + \\beta \\ln L$) inherently compresses the scale of the data, naturally mitigating heteroscedasticity.
- **Deflators**: Dividing by a relevant size metric (e.g., population to get per-capita figures, or a price index to get real figures). 
  - *Rule of thumb*: If the deflation is supported by economic theory, use the deflated model for inferences. If it is done purely as a mathematical hack to fix heteroscedasticity, use the original parameters to draw inferences.
- **Generalised Least Squares (GLS)**: An estimation technique that transforms the variables to produce homoscedastic error terms, yielding BLUE estimators. ⭐
- **White's Estimator**: A large-sample procedure that calculates robust standard errors to correct for heteroscedasticity when its exact pattern is unknown. ⭐

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that fixing heteroscedasticity changes the OLS coefficients significantly. → ✅ Correct: The OLS coefficients are already unbiased. The main goal of WLS and Robust Standard Errors is to fix the *variances* so hypothesis tests are valid.

**Quick Recall:**
- If variance pattern is known: Use WLS.
- If variance pattern is unknown (large sample): Use White's Robust Standard Errors.
- Logs compress data naturally, fixing heteroscedasticity.
- Fixes issues from: Consequences of Heteroscedasticity (Chunk 006)

### Concept of Errors in Variables 🔴

**Measurement Errors**
- **Errors in Variables**: A violation of the classical assumption that regressors are measured perfectly, occurring when the observed variables contain random measurement errors (often due to using proxy variables). ⭐ (exam-important)

### Consequences of Errors in Variables 🔴

**Measurement Error in Y**
- Because $u_i$ is just a measurement error in $Y$, it simply merges into the stochastic disturbance term: $y_i^* = \\beta x_i + (\\varepsilon_i + u_i)$.
- **Consequence**: The explanatory variable $x_i$ remains uncorrelated with the new composite error term. Therefore, the OLS estimator $\\hat{\\beta}$ remains **unbiased**.
- **Drawback**: The variance of the estimator increases from $\\frac{\\sigma_\\varepsilon^2}{\\sum x_i^2}$ to $\\frac{\\sigma_\\varepsilon^2 + \\sigma_u^2}{\\sum x_i^2}$. The estimates are less precise.

**Measurement Error in X**
- Substituting this into the true equation gives $y_i = \\beta x_i^* + (\\varepsilon_i - \\beta \\nu_i)$.
- **Consequence**: The new independent variable $x_i^*$ is now correlated with the new composite error term (because both contain $\\nu_i$). This violates the most critical OLS assumption.
- **Result**: The OLS estimator becomes **biased and inconsistent**. Even in an infinitely large sample, the estimator evaluates to:

**Measurement Errors in both X and Y**

**Quick Recall:**
- Error in $Y$: OLS is unbiased but inefficient (higher variance).
- Error in $X$: OLS is biased and inconsistent (underestimates true $\\beta$).
- Measurement error violates the assumption that $Cov(x_i, u_i) = 0$.
- Prerequisite for: Instrumental Variables Method (Chunk 008)

### Instrumental Variables Method 🔴

**Conditions for an Instrument**
1. **Relevance**: The correlation between $Z$ and the true explanatory variable $X$ must be non-zero (they must be highly correlated).
2. **Exogeneity**: The correlation between $Z$ and the error terms (both the equation error $\\varepsilon$ and the measurement error $\\nu$) must be strictly zero.

**Instrumental Variables Estimator**
- **Instrumental Variable (IV)**: A proxy variable $Z$ used in regression analysis that is highly correlated with the explanatory variable but uncorrelated with the error term, used to obtain consistent estimators when variables are measured with error. ⭐ (exam-important)
- **Consistency vs Unbiasedness**: IV guarantees **consistency** (it will eventually hit the true parameter if you have an infinitely large sample), but it does NOT guarantee **unbiasedness** (in small samples, it may still be biased).
- OLS is actually just a special case of the IV method where $X$ is used as its own instrument (which only works if $X$ has no measurement error).

**Quick Recall:**
- IV solves Measurement Error in $X$.
- Instrument $Z$ must be: 1. Correlated with $X$. 2. Uncorrelated with error $u$.
- IV formula: $\\sum zy / \\sum zx^*$.
- IV provides consistent, but not necessarily unbiased, estimates.
- Fixes issues from: Consequences of Errors in Variables (Chunk 008)

### Test of Measurement Errors 🔴

**Hausman Specification Test**
- Under the null hypothesis ($H_0$: No measurement error): Both OLS and IV are consistent, but OLS is efficient.
- Under the alternative hypothesis ($H_1$: Measurement error exists): OLS is inconsistent, but IV remains consistent.
1. Regress the flawed variable $x^*$ on the instrument $z$ to obtain the residuals, $\\hat{w}_i$.
2. Regress the dependent variable $y$ on both $x^*$ and the generated residuals $\\hat{w}_i$.
3. Perform a $t$-test on the coefficient of $\\hat{w}_i$ (let's denote it as $\\delta$).
4. If $\\delta$ is statistically significantly different from zero, reject the null hypothesis and conclude that measurement error is present.
- **Hausman Specification Test**: A statistical test used to detect measurement errors (or endogeneity) by comparing the consistency of OLS estimators against Instrumental Variables estimators. ⭐ (exam-important)

### Test of Measurement Errors (Continued) 🔴
1. We use "population of school children" as an instrument ($Z$) and regress aid on $Z$ to get residuals $\\hat{w}$.
2. We add $\\hat{w}$ to the original expenditure regression.
3. If the t-statistic of $\\hat{w}$ is significant (e.g., at the 10% level), we conclude measurement error is present, and we notice that correcting for it substantially lowers the coefficient on the aid variable.

### Inverse Regression 🔴

**Direct vs Inverse Regression**
- **Direct Regression**: Regressing $Y^*$ (measured dependent) on $X^*$ (measured independent). (e.g., Salary on Qualifications).
- **Inverse (Reverse) Regression**: Regressing $X^*$ on $Y^*$. (e.g., Qualifications on Salary).

**Use Cases**
- **Statistical Reality**: Because of the usual errors-in-variables problem, neither the direct nor the inverse regression alone gives the perfectly correct estimate. Instead, the estimates from both regressions are used to establish theoretical **bounds** for the true parameter $\\beta$.
- Completes the unit on Errors in Variables (Unit 12).

### Concept of Stochastic Regressors 🔴

**Relaxing OLS Assumptions**
- **Non-Stochastic (Classical Assumption)**: If $X$ is fixed, there is absolutely no relationship between $X$ and the random error term $u$. Thus, $E(x_i u_i) = 0$.
- **Stochastic (Real-world)**: If $X$ is a random variable, there is a high possibility that $X$ and $u$ move together. If $E(x_i u_i) \\neq 0$, the core assumption of OLS is violated, causing estimators to become biased and inconsistent.
- **Stochastic Regressor**: An explanatory variable that is a random variable, rather than having fixed, predetermined values in repeated samples. ⭐ (exam-important)
- Prerequisite for: Endogeneity Problem (Chunk 009)

### Endogeneity Problem 🔴

**The Three Major Sources of Endogeneity:**
1. **Omitted Variables**:
2. **Measurement Error**:
3. **Simultaneity (Reverse Causality)**:
   - *Example*: In a model predicting Earnings ($Y$) based on Years of Schooling ($X$), an unmeasured factor like "Innate Ability" falls into the error term ($u$). "Ability" positively impacts Earnings, but "Ability" *also* causes a person to stay in school longer. Therefore, $X$ (Schooling) is positively correlated with $u$ (Ability). A change in Earnings cannot be purely attributed to Schooling.

**Remedies for Endogeneity**
1. Instrumental Variables (IV) Method
2. Two-Stage Least Squares (2SLS) Method
- **Endogenous Variable**: An explanatory variable in a regression model that is correlated with the stochastic error term. ⭐ (exam-important)
- **Exogenous Variable**: An explanatory variable that is NOT correlated with the stochastic error term. ⭐ (exam-important)
- **Simultaneity (Reverse Causality)**: A situation where the explanatory variable is partly determined by the dependent variable, leading to a correlation with the error term (endogeneity). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that adding more data fixes endogeneity. → ✅ Correct: Endogeneity causes inconsistency. An inconsistent estimator will remain biased forever, even with an infinitely large sample size. You must change the estimation method (e.g., use IV).

**Quick Recall:**
- $E(X, u) = 0$ -> Exogenous (Good, OLS works).
- $E(X, u) \\neq 0$ -> Endogenous (Bad, OLS is biased/inconsistent).
- 3 Causes: Omitted variables, Measurement error, Simultaneity.
- Builds upon: Omitted Variable Bias (Block 2) and Measurement Error (Chunk 008).
- Leads to: Instrumental Variables and 2SLS (Chunk 010).

### Instrumental Variable Estimator 🔴

**IV Method Conditions**
1. **Exogeneity Condition**: $z_1$ must not be correlated with the stochastic error $u$. $Cov(z_1, u) = 0$. 
   - *Note*: This condition must simply be assumed/maintained by the researcher based on economic theory because $u$ is fundamentally unobservable, so this condition cannot be statistically tested.
2. **Relevance Condition**: $z_1$ must be correlated with the endogenous variable $x_K$, even after netting out the effects of all other exogenous variables in the model. 
   - *Note*: This condition *can* be statistically tested using a t-test on the reduced form equation.

**Identification & Reduced Form**
- **Reduced Form Equation**: Describes an endogenous variable strictly as a linear projection onto all available exogenous variables in the system. 
- By plugging the reduced form back into the structural equation, we solve the identification problem, allowing us to consistently estimate the true parameters.

### ⚠️ Common Mistakes
- ❌ Mistake: Believing that IV estimators are just as efficient as OLS estimators. → ✅ Correct: By using a proxy $z_1$ instead of the actual data $x_K$, we lose some information. This leads to larger error terms and larger standard errors. If the correlation between $z_1$ and $x_K$ is weak ("weak instruments"), the IV estimator will have unacceptably large standard errors.
- Solves the problem introduced in: Endogeneity Problem (Chunk 009)

### Two-Stage Least Squares (2SLS) Estimator 🔴

**Need for 2SLS**

**The Two-Stage Process**
1. Regress the endogenous variable $x_K$ on **all** exogenous variables in the model AND **all** available instrumental variables ($z_1, z_2, \\dots, z_M$) using OLS.
2. Obtain the fitted (predicted) values from this regression, denoted as $\\hat{x}_K$. This $\\hat{x}_K$ is now our optimal, purified instrument.
1. Regress the dependent variable $y$ on the original exogenous variables and the newly generated fitted values $\\hat{x}_K$ (replacing the original $x_K$) using OLS.
2. The resulting parameters are the 2SLS estimators.
- **Two-Stage Least Squares (2SLS)**: An estimation technique used when there are multiple instruments available for an endogenous variable, involving a first-stage regression to create an optimal fitted instrument, and a second-stage regression to estimate the main model. ⭐ (exam-important)
- If there is exactly **one** instrument for **one** endogenous variable (exact identification), the IV estimator and the 2SLS estimator will yield mathematically identical results. 2SLS is only distinct when there are more instruments than endogenous variables (overidentification).

**Quick Recall:**
- Stage 1: Predict endogenous $X$ using all instruments. (Purification phase)
- Stage 2: Run main regression using predicted $\\hat{X}$. (Estimation phase)
- 2SLS is the most efficient IV estimator when multiple instruments exist.

### Two-Stage Least Squares (2SLS) Estimator (Continued) 🔴

**Summary of Methods**
- If an explanatory variable is correlated with the error term, we face the endogeneity problem, and the OLS estimator is biased and inconsistent.
- To solve this, we use the Instrumental Variable (IV) method. An instrument must be strongly correlated with the endogenous variable and completely uncorrelated with the error term.
- Because there are often many more instrumental variables available than endogenous variables (e.g., any linear combination of $z_1, z_2, \\dots, z_M$), the 2SLS method is employed.
- **Why 2SLS is preferred**: The 2SLS estimator mathematically guarantees the most efficient (minimum variance) IV estimator possible when multiple instruments are present.
- Endogeneity -> Use IV.
- Multiple Instruments -> Use 2SLS.
- 2SLS provides the most efficient IV estimator.
- Concludes the unit on Stochastic Regressors (Unit 13).
- Concludes Block-3 of MECE-101.
