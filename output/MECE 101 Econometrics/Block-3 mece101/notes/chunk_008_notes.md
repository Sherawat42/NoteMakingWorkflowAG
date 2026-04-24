# Chunk 008 — Consequences and Remedies for Errors in Variables
<!-- Pages: 72-81 -->
<!-- Source: chunk_008.txt -->

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
- Prerequisite for: Instrumental Variables Method (Chunk 008)

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
- Fixes issues from: Consequences of Errors in Variables (Chunk 008)

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
