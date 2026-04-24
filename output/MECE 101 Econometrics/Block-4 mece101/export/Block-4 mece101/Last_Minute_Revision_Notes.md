# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

- **Dummy Variables**: Artificial variables constructed to take the value 1 or 0, indicating the presence (1) or absence (0) of a particular attribute. Also known as binary, indicator, categorical, or dichotomous variables. ⭐ (exam-important)

**Quick Recall:**
- Structural change means parameters shift within a sample.
- Qualitative variables are handled using dummy variables (0 and 1).

### 14.2 Chow Test for Structural Stability 🔴

**Assumptions of Chow Test**
1. The error terms are normally distributed with the same variance: ε₁ ~ N(0, σ²) and ε₂ ~ N(0, σ²).
2. The error terms are independently distributed.

**Restricted vs Unrestricted Models**
- **Restricted Model**: Combines all observations into one single regression, assuming structural stability. Produces RSS_R (Restricted Residual Sum of Squares) with degrees of freedom (n₁ + n₂ - k).
- **Unrestricted Model**: Estimates separate regressions for each subset. Produces RSS_UR = RSS₁ + RSS₂ with degrees of freedom (n₁ + n₂ - 2k).
| Model | Equation | RSS | Degrees of Freedom |
|-------|----------|-----|--------------------|
| Restricted | Y_t = λ₁ + λ₂X_t + ε_t | RSS_R | n₁ + n₂ - k |
| Unrestricted | Y_t = α₁ + α₂X_t + ε_t (Group 1)<br>Y_t = β₁ + β₂X_t + ε_t (Group 2) | RSS_UR = RSS₁ + RSS₂ | n₁ + n₂ - 2k |
- **Structural Break**: Occurs if the parameters underlying a relationship differ from one subset of the data to another. ⭐ (exam-important)
1. Estimate the Restricted Model (combined data) and obtain RSS_R.
2. Estimate the Unrestricted Models (separate regressions) and obtain RSS₁ and RSS₂.
3. Calculate RSS_UR = RSS₁ + RSS₂.
4. Compute the F-ratio: `F = [ (RSS_R - RSS_UR) / k ] / [ RSS_UR / (n₁ + n₂ - 2k) ]`
5. Compare the computed F-value with the critical F-value. If it exceeds the critical value, reject the hypothesis of structural stability.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming the Chow test tells us exactly *why* the models differ (intercept vs slope). → ✅ Correct: The Chow test only confirms *if* there is a difference; it does not specify whether the difference is in the intercept, slope, or both. Dummy variables are needed for that.

**Quick Recall:**
- Chow test checks for structural stability.
- `F = [ (RSS_R - RSS_UR) / k ] / [ RSS_UR / (n₁ + n₂ - 2k) ]`
- Does not specify if the difference is in slope or intercept.
- Contrasts with testing through Dummy Variables (Chunk 002) which can isolate intercept vs slope differences.

### 14.3 The Nature of Dummy Variables 🔴

**Dummy Variable Trap**

**Base Category**
- **Differential Intercept Coefficient**: The coefficient attached to the dummy variable. It tells by how much the value of the intercept term of the category receiving value 1 differs from that of the base category. ⭐ (exam-important)
- **Dummy Variable Trap**: A situation of perfect multicollinearity that occurs when too many dummy variables are introduced for a qualitative variable. ⭐ (exam-important)
1. Determine the number of categories 'm' for a qualitative variable.
2. Introduce 'm-1' dummy variables.
3. Choose one category to be the base category (all its dummy values are 0).
4. Interpret the dummy coefficients as the difference from the base category.

**Quick Recall:**
- Rule of thumb: 'm' categories require 'm-1' dummy variables.
- Dummy Variable Trap = perfect multicollinearity.
- The coefficient shows the difference from the base category.
- Prerequisite for ANOVA and ANCOVA Models (Chunk 001).
- **ANOVA Models**: Regression models that contain only dummy explanatory variables. ⭐ (exam-important)

**Quick Recall:**
- ANOVA = Only dummy variables.
- Intercept = Base category mean.
- **ANCOVA Models**: Regression models that contain both qualitative and quantitative explanatory variables. ⭐ (exam-important)

**Quick Recall:**
- ANCOVA = Mix of qualitative and quantitative variables.
- Represents parallel regression lines with the same slope but different intercepts.
- **Multiple Dummy Variables**: The use of more than one set of dummy variables in a single regression model to represent multiple qualitative attributes. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Introducing `m` dummy variables for a variable with `m` categories. → ✅ Correct: Always use `m-1` dummy variables for each qualitative variable to avoid perfect multicollinearity (the dummy variable trap).

**Quick Recall:**
- You can use multiple qualitative variables in one model.
- Always use the `m-1` rule for each variable independently.
- The intercept represents the combined base category.

### 14.5 Testing for Structural Stability through Dummy Variables 🔴

**Coincident Regression**

**Parallel Regression**

**Concurrent Regression**

**Dissimilar Regression**
- **Differential Slope Coefficient**: A coefficient created by multiplying a dummy variable by a quantitative variable (an interaction term like `D_t * Y_t`). It indicates how much the slope of the category receiving value 1 differs from the slope of the base category. ⭐ (exam-important)
1. Define a dummy variable `D` for the two periods/groups.
2. Create an interaction term `D * X`.
3. Run the regression: `Y_t = a + bD_t + cX_t + d(D_t * X_t) + u_t`.
4. Test the significance of `b` (differential intercept) and `d` (differential slope).
- Pre-reforms mean savings: `(a + b) + (c + d)Y_t`
- Post-reforms mean savings (base): `a + cY_t`

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking the Chow test is better because it's a dedicated test. → ✅ Correct: The dummy variable approach is generally preferred because it requires only one regression (higher degrees of freedom) and pinpoints the exact source of difference (intercept vs slope).

**Quick Recall:**
- Dummy variables > Chow Test for structural stability.
- Requires one regression instead of three.
- Identifies if the difference is in the intercept (parallel), slope (concurrent), or both (dissimilar).
- Provides a better alternative to the Chow Test (Chunk 001).
- **Seasonal Adjustment (Deseasonalisation)**: The process of removing the seasonal factor from a time series. ⭐ (exam-important)

**Quick Recall:**
- Deseasonalisation removes seasonal effects.
- Uses `s-1` seasonal dummies.
- **Pooled Data**: Data that combines both cross-sectional (e.g., multiple sectors) and time-series (e.g., multiple years) dimensions. ⭐ (exam-important)

**Quick Recall:**
- Pooling data increases sample size and degrees of freedom.
- Cross-sectional differences are handled via dummy variables for units.
- **Limited Dependent Variable Models**: Regression models where the dependent variable is constrained, for instance, being non-negative or strictly taking binary values (0 or 1). ⭐ (exam-important)

### 15.2 Linear Probability Model 🔴

**LPM Basics**
- **Linear Probability Model (LPM)**: A regression model where the dependent variable is a binary (dummy) variable, and it is estimated using the OLS method. ⭐ (exam-important)
- Builds on basic OLS concepts but applies them to binary outcomes.
- **Conditional Expectation in LPM**: Represents the conditional probability that the event will occur given the values of the explanatory variables. ⭐ (exam-important)

### 15.2.2 Limitations of the Model 🔴

**Non-Normality of u_i**

**Heteroscedasticity of u_i**

**Value remains outside range**

**R-squared is not appropriate**
- **Heteroscedasticity in LPM**: The variance of the error term changes with the explanatory variables because the variance of a Bernoulli variable is a function of its mean. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Using R-squared to judge if an LPM is a "good" model. → ✅ Correct: R-squared is conceptually flawed for binary dependent variables; pseudo R-squared or other fit measures are needed for such data.

**Quick Recall:**
Four main LPM flaws:
1. Non-normal errors.
2. Heteroscedastic errors.
3. Probabilities can be < 0 or > 1.
4. R-squared is meaningless.
- These limitations justify the need for Logit and Probit models (introduced later in Chunk 003 and 004).

### 15.3 Logit Model 🔴

**Cumulative Logistic Distribution Function**

**Odds-Ratio**
- **Logit Model**: A nonlinear regression model for binary dependent variables that uses the cumulative logistic distribution function to model the log-odds as a linear function of explanatory variables. ⭐ (exam-important)
1. `Y_i` is an unobservable latent variable (e.g. utility), but we observe a binary outcome.
2. We calculate the odds ratio: `p_i / (1 - p_i)`.
3. We take the natural log of the odds ratio to create a linear model: `L_i = α₀ + α₁X_i`.

**Quick Recall:**
- Logit = ln(Odds-Ratio)
- Logit ensures probabilities stay between 0 and 1.
- Solves the out-of-range limitation of the LPM (Chunk 003).
- **Maximum Likelihood Method**: A non-linear estimation procedure used to estimate the parameters of models like logit and probit when individual micro-data is used. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Trying to use OLS on individual-level binary data in a logit framework. → ✅ Correct: For individual data, the logit is mathematically undefined (log of 0 or log of infinity). MLE must be used.

**Quick Recall:**
- Individual data -> Maximum Likelihood Estimation (MLE).
- Grouped data -> GLogit (can use OLS on group frequencies).
<!-- Continues in chunk 004 -->
- **Marginal Effect**: The change in the probability of the dependent variable for a one-unit change in an independent variable, calculated at a specific base point (usually the mean). ⭐ (exam-important)

### 15.4 Probit Model 🔴

**Normal CDF**
- **Probit Model**: A nonlinear regression model for binary outcomes that assumes the error term follows a standard normal distribution. ⭐ (exam-important)
- Alternative to Logit Model (Chunk 003) and superior to LPM (Chunk 003).
- **Latent Variable**: An unobservable underlying variable (like an index or utility) that crosses a threshold to produce the observed binary outcome. ⭐ (exam-important)
- **Gprobit**: The grouped probit model, estimated using OLS on grouped frequency data transformed via the inverse normal CDF. ⭐ (exam-important)
- **Interpretation**: Interpreting probit models relies on reading standard normal CDF tables to convert Z-scores back into probabilities or calculating marginal effects. ⭐ (exam-important)

### 15.5 Joint Significance in Qualitative Response Regression Models 🔴

**Likelihood Ratio (LR) Test**
- **LR Test (Likelihood Ratio Test)**: A statistical test used in maximum likelihood estimation to determine the joint significance of all explanatory variables, analogous to the F-test in OLS. ⭐ (exam-important)
- Analogous to the F-test used in the Chow Test (Chunk 001) but specifically for MLE models.

### 15.6 Goodness-of-Fit in Logit and Probit Models 🔴

**Pseudo R-squared**
- **Goodness-of-Fit (Pseudo R²)**: Statistical measures used to evaluate how well a qualitative response model fits the data, since traditional R² is invalid. ⭐ (exam-important)
- Solves the "R-squared is not appropriate" limitation of the LPM identified in Chunk 003.
- **Simultaneous Equations**: Models where the equations are related and cannot be solved independently because the variables mutually determine one another. ⭐ (exam-important)
- **Simultaneous Equations Model (SEM)**: A model consisting of a set of equations that jointly determine the values of several endogenous variables. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Believing you can just run OLS on one part of a simultaneous system if you only care about that one equation. → ✅ Correct: Running OLS on a single equation within a simultaneous system yields biased and inconsistent estimates for that equation's parameters.

**Quick Recall:**
- SEMs are needed when variables mutually cause each other.
- Classic examples: Supply & Demand, Wage-Price, Keynesian Income.
- Main problem: OLS assumption `cov(X,u) = 0` is violated.
---

### 16.3 Endogenous Variables and Exogenous Variables 🔴

**Endogenous Variables**

**Predetermined Variables**
1. **Current Exogenous variables**: Determined outside the model entirely (e.g., rainfall, government policy).
2. **Lagged Exogenous variables**: Past values of outside variables (e.g., last year's rainfall).
3. **Lagged Endogenous variables**: Past values of inside variables (e.g., last year's consumption). Because they happened in the past, their values are already known and thus non-stochastic for the current period.
- **Endogenous Variables**: Variables which get determined jointly and interdependently within the model. ⭐ (exam-important)
- **Exogenous Variables**: Variables which get determined outside the model, and independently of the endogenous variables. ⭐ (exam-important)
- **Predetermined Variables**: The combined set of current exogenous, lagged exogenous, and lagged endogenous variables. ⭐ (exam-important)
1. Economic theory dictates which variables are included in the model.
2. The researcher classifies them as endogenous (solved by the model) or predetermined (given as inputs).
3. The model must have as many equations as it has endogenous variables to be completely solvable.

**Quick Recall:**
- Endogenous = Determined IN the model (stochastic).
- Exogenous = Determined OUTSIDE the model (non-stochastic).
- Predetermined = Exogenous + Lagged variables.
- Identifying these variables is the first step required to perform Identification (Chunks 006, 007).

### 16.4 Simultaneity Bias 🔴

**Covariance between Explanatory Variable and Error Term**
- **Simultaneity Bias**: The statistical bias that results from applying standard OLS to estimate the parameters of a simultaneous equations model, leading to inaccurate parameter estimates. ⭐ (exam-important)
- Connects back to the OLS assumptions introduced earlier in the course.
- **Endogeneity**: A situation where an explanatory variable is correlated with the error term in a regression model. ⭐ (exam-important)
- **Biased Estimator**: An estimator whose expected value (average across repeated samples) does not equal the true population parameter. ⭐ (exam-important)
- **Inconsistent Estimators**: Estimators whose values do not converge to the true population parameter even as the sample size approaches infinity. ⭐ (exam-important)

### 16.5 Structural Form and Reduced Form 🔴

**Structural Equations**

**Reduced-Form Equations**
- **Structural Equation**: Equations which represent the structure of an economic model or the behavior of an economic agent. ⭐ (exam-important)
- **Structural Parameters**: Parameters (like βs and γs) appearing in the structural equations. ⭐ (exam-important)
- **Reduced Form Models**: Models where each equation contains only one endogenous dependent variable expressed solely in terms of predetermined variables. ⭐ (exam-important)
- **Reduced Form Parameters (Impact Multipliers)**: Parameters of the reduced form equations (often denoted by Π). They measure the immediate impact on the endogenous variable of a unit change in an exogenous variable. ⭐ (exam-important)
- Reduced forms provide a pathway to solving the Endogeneity Problem (Chunk 006).

### 16.6 Concept of Identification 🔴

**Identification Problem**

**Observationally Equivalent Theories**
- **Identification**: The possibility (or impossibility) of deducing the values of the structural parameters from the reduced form parameters. ⭐ (exam-important)
- **Paradox of Identification**: The concept that identification is achieved in terms of the variables *absent* from the equation, not in terms of the variables present. ⭐ (exam-important)
- **Under-identified Equation**: An equation without sufficient information to uniquely distinguish its structural parameters. ⭐ (exam-important)
- **Exactly-identified Equation**: An equation with exactly sufficient information to yield unique structural parameter estimates. ⭐ (exam-important)
- **Over-identified Equation**: An equation with more than sufficient information, yielding multiple possible estimates for structural parameters. ⭐ (exam-important)

### 16.7 Identification Conditions 🔴

**Necessary and Sufficient Conditions**
- The Order Condition is a *necessary* but not sufficient condition. If it fails, the equation is under-identified. If it passes, the equation *might* be identified.
- The Rank Condition is *both necessary and sufficient*. If it passes, the equation is definitely identified.
- **Identification Conditions**: Formal mathematical rules (order and rank conditions) used to determine if the structural parameters of an equation can be uniquely estimated. ⭐ (exam-important)
- These conditions provide the mechanical steps to solve the Identification Problem (Chunk 006).
- **Order Condition**: A necessary counting rule for identification stating that the number of variables excluded from an equation must be greater than or equal to the total number of equations minus one. ⭐ (exam-important)
- **Rank Condition**: A necessary and sufficient condition for identification requiring that a non-zero determinant of order `G-1` can be formed from the parameters of variables excluded from the equation. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming an equation is identified just because it passes the order condition. → ✅ Correct: The order condition is only a necessary first step. The rank condition must be verified (though in practice, order condition is often checked first for quick elimination).

**Quick Recall:**
- Order condition: Easy counting. `(K-M) ≥ (G-1)`.
- Rank condition: Harder matrix math. Non-zero determinant of size `(G-1)`.
- Rank is sufficient; Order is only necessary.
