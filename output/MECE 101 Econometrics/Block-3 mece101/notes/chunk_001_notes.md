# Chunk 001 — Model Specification Issues
<!-- Pages: 1-10 -->
<!-- Source: chunk_001.txt -->

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
- Prerequisite for: Inclusion of Variables in a Model (Chunk 001)

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
- Builds on: Possible Problems in Specification (Chunk 001)

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
