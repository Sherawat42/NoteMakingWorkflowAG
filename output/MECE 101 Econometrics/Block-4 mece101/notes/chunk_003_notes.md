# Chunk 003 — Linear Probability and Logit Models
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->
<!-- Continues from: N/A -->

## Section: 15.1 Introduction 🟢

### Core Idea
Regression models can also have qualitative (dummy) variables as their dependent variables. These are called limited dependent variable models, representing binary choices (e.g., owning a house vs. not owning a house) and are typically estimated using Maximum Likelihood Estimation rather than OLS.

> **In Simple Terms:** Instead of trying to predict a number (like a salary), we are trying to predict a yes/no outcome (like whether someone buys a house or not).

### Key Concepts

#### Qualitative Dependent Variables
Variables that represent categories rather than continuous numbers. In the binary (or dichotomous) case, the dependent variable takes the value of exactly 1 or 0. Since the outcome is binary, the goal is to find the maximum probability of the occurrence of the given data.

### Definitions
- **Limited Dependent Variable Models**: Regression models where the dependent variable is constrained, for instance, being non-negative or strictly taking binary values (0 or 1). ⭐ (exam-important)

### Connections
- Shifts focus from qualitative explanatory variables (Chunk 001, 002) to qualitative dependent variables.

---

## Section: 15.2 Linear Probability Model 🔴

### Core Idea
The Linear Probability Model (LPM) is the simplest regression model for a binary outcome, where the dependent variable is regressed on explanatory variables using standard OLS. The predicted value is interpreted as the probability of the event occurring.

> **In Simple Terms:** We draw a straight line through our data, and we read the line's height as the "chance" or probability of the event happening (e.g., 0.8 means an 80% chance).

### Key Concepts

#### LPM Basics
In an LPM, the conditional expectation `E(Y_i | X_i)` is interpreted directly as the conditional probability `Pr(Y_i = 1 | X_i)` that the event will occur given the explanatory variables.

### Definitions
- **Linear Probability Model (LPM)**: A regression model where the dependent variable is a binary (dummy) variable, and it is estimated using the OLS method. ⭐ (exam-important)

### Connections
- Builds on basic OLS concepts but applies them to binary outcomes.

---

## Section: 15.2.1 Specification of the Model 🟡

### Core Idea
The mathematical formulation of the LPM translates the expected value of a Bernoulli random variable directly into a linear equation.

> **In Simple Terms:** We set up the math so that the average value we predict is exactly equal to the probability of getting a "1" (success).

### Key Concepts

#### Conditional Probability
If `Y_i` takes the value 1 with probability `p_i` and 0 with probability `1 - p_i`, then the expected value `E(Y_i)` equals `1 * p_i + 0 * (1 - p_i) = p_i`. Therefore, `E(Y_i | X_i) = p_i`. Because it is a probability, `E(Y_i | X_i)` must theoretically lie between 0 and 1.

### Definitions
- **Conditional Expectation in LPM**: Represents the conditional probability that the event will occur given the values of the explanatory variables. ⭐ (exam-important)

### Mechanisms / Processes
1. Define the binary dependent variable `Y_i` (1 for event, 0 otherwise).
2. Set up the linear equation: `Y_i = α₀ + α₁X_i + u_i`.
3. Interpret `Y_i` as `p_i`, the probability of the event occurring.

---

## Section: 15.2.2 Limitations of the Model 🔴

### Core Idea
Despite its simplicity, the LPM suffers from severe theoretical and practical flaws when estimated using OLS, making it generally unsuitable for binary outcome data.

> **In Simple Terms:** A straight line doesn't work well for probabilities. It can predict a "120% chance" or a "-10% chance," which is impossible. Also, the errors behave weirdly compared to normal regressions.

### Key Concepts

#### Non-Normality of u_i
Because `Y_i` only takes values 0 and 1, the error term `u_i` also only takes two possible values. Therefore, `u_i` follows a Bernoulli distribution, not a normal distribution. While OLS estimators are still unbiased in large samples, small sample hypothesis testing is compromised.

#### Heteroscedasticity of u_i
For a Bernoulli distribution, the variance is `p_i(1 - p_i)`. Since `p_i` depends on the explanatory variable `X_i`, the variance of the error term also depends on `X_i`. This means the errors are heteroscedastic.

#### Value remains outside range
Since OLS fits a straight line, there is no mathematical constraint to keep the predicted probability (`p_i`) between 0 and 1. For very large or small values of `X_i`, the model may predict probabilities > 1 or < 0.

#### R-squared is not appropriate
Because the actual data points are either exactly 0 or exactly 1, they cluster on two horizontal lines. A straight line will not fit this scatter plot well, resulting in conventionally computed R-squared values being artificially low (typically 0.2 to 0.6) and of limited value.

### Definitions
- **Heteroscedasticity in LPM**: The variance of the error term changes with the explanatory variables because the variance of a Bernoulli variable is a function of its mean. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Using R-squared to judge if an LPM is a "good" model. → ✅ Correct: R-squared is conceptually flawed for binary dependent variables; pseudo R-squared or other fit measures are needed for such data.

> **Quick Recall:**
> Four main LPM flaws:
> 1. Non-normal errors.
> 2. Heteroscedastic errors.
> 3. Probabilities can be < 0 or > 1.
> 4. R-squared is meaningless.

### Connections
- These limitations justify the need for Logit and Probit models (introduced later in Chunk 003 and 004).

---

## Section: 15.2.3 Interpretation of LPM 🟡

### Core Idea
If an LPM is used, its coefficients are interpreted as the absolute change in the probability of the event occurring for a one-unit change in the independent variable.

> **In Simple Terms:** If the slope is 0.05, it means for every extra unit of X, the chance of Y happening goes up by exactly 5 percentage points.

### Key Concepts

#### Interpretation
- **Intercept**: The probability that the event occurs when all independent variables are zero. (If negative, it's theoretically treated as zero).
- **Slope**: The absolute percentage point change in the probability of the event for a unit change in the explanatory variable.

### Examples
**Example: House Ownership**
`Y_hat = -0.5 + 0.0652 X_i` (where X is income in thousands).
- Intercept (-0.5): A household with zero income has a -0.5 probability of owning a house (treated as 0).
- Slope (0.0652): For a 1-unit (Rs. 1000) increase in income, the probability of owning a house increases by 6.52%.

---

## Section: 15.3 Logit Model 🔴

### Core Idea
The logit model resolves the LPM's out-of-range problem by using the cumulative logistic distribution function. This ensures that predicted probabilities always stay within the logical 0 to 1 bounds by producing an S-shaped curve rather than a straight line.

> **In Simple Terms:** The logit model uses an S-shaped curve that flattens out at 0% and 100%, so it can never predict an impossible chance, no matter how extreme the input variables are.

### Key Concepts

#### Cumulative Logistic Distribution Function
The probability `p_i` is defined as: `p_i = e^{Z_i} / (1 + e^{Z_i})`, where `Z_i = α₀ + α₁X_i`. This function ensures that as `X_i` goes from negative infinity to positive infinity, `p_i` stays strictly between 0 and 1.

#### Odds-Ratio
The ratio of the probability that the event will occur (`p_i`) to the probability that it will not occur (`1 - p_i`). 
Odds-Ratio = `p_i / (1 - p_i) = e^{Z_i}`.

If we take the natural logarithm of the odds-ratio, we get the **Logit (L_i)**:
`L_i = ln[p_i / (1 - p_i)] = Z_i = α₀ + α₁X_i + u_i`

### Definitions
- **Logit Model**: A nonlinear regression model for binary dependent variables that uses the cumulative logistic distribution function to model the log-odds as a linear function of explanatory variables. ⭐ (exam-important)

### Mechanisms / Processes
1. `Y_i` is an unobservable latent variable (e.g. utility), but we observe a binary outcome.
2. We calculate the odds ratio: `p_i / (1 - p_i)`.
3. We take the natural log of the odds ratio to create a linear model: `L_i = α₀ + α₁X_i`.

> **Quick Recall:**
> - Logit = ln(Odds-Ratio)
> - Logit ensures probabilities stay between 0 and 1.

### Connections
- Solves the out-of-range limitation of the LPM (Chunk 003).

---

## Section: 15.3.1 Features of the Logit Model 🟡

### Core Idea
The Logit model transforms the bounded probability into an unbounded log-odds scale, allowing for standard linear estimation techniques on the transformed variable.

> **In Simple Terms:** We change "probability" (which is stuck between 0 and 1) into "log-odds" (which can be any number from negative to positive infinity). This lets us use linear math to solve the problem.

### Key Concepts

#### Logit Features
1. **Unbounded Logit**: While `p_i` is bounded between 0 and 1, the logit `L_i` ranges from -∞ to +∞.
2. **Non-linear Probabilities**: The logit `L_i` is linear in `X`, but the probability `p_i` is non-linear. The probability approaches 0 and 1 at slower and slower rates as `X` becomes very small or very large (creating the S-curve).
3. **Slope Interpretation**: The slope measures the change in the *log-odds* (not the probability itself) for a unit change in the explanatory variable.

---

## Section: 15.3.2 Estimation of Logit Model 🟡

### Core Idea
Because the dependent variable in a logit model is a binary outcome rather than a continuous logit, standard OLS cannot be used for individual-level data. Maximum Likelihood Estimation (MLE) or Grouped data techniques must be used.

> **In Simple Terms:** Because our actual data only has 1s and 0s, we can't easily calculate "log-odds" for a single person. We have to use advanced math (Maximum Likelihood) to find the best fit, or we group similar people together to estimate their group probability.

### Key Concepts

#### Grouped vs Ungrouped Data
- **Individual (Micro) Data**: We only observe `p_i = 1` or `p_i = 0`. If `p_i = 1`, the logit is infinity. If `p_i = 0`, the logit is negative infinity. Therefore, OLS is impossible. We must use non-linear Maximum Likelihood (ML) estimation.
- **Grouped (Replicated) Data**: Individuals with the same values of explanatory variables `X_i` are grouped. The relative frequency `n_i / N_i` (successes over total in group) is used as an estimate for `p_i`. Then `L_i = ln[ (n_i/N_i) / (1 - n_i/N_i) ]` can be calculated and used in OLS. This is called a Grouped Logit (GLogit).

### Definitions
- **Maximum Likelihood Method**: A non-linear estimation procedure used to estimate the parameters of models like logit and probit when individual micro-data is used. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Trying to use OLS on individual-level binary data in a logit framework. → ✅ Correct: For individual data, the logit is mathematically undefined (log of 0 or log of infinity). MLE must be used.

> **Quick Recall:**
> - Individual data -> Maximum Likelihood Estimation (MLE).
> - Grouped data -> GLogit (can use OLS on group frequencies).

<!-- Continues in chunk 004 -->
