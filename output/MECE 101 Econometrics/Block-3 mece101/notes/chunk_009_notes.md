# Chunk 009 — Inverse Regression and Stochastic Regressors Intro
<!-- Pages: 82-89 -->
<!-- Source: chunk_009.txt -->

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
- Prerequisite for: Endogeneity Problem (Chunk 009)

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
- Builds upon: Omitted Variable Bias (Block 2) and Measurement Error (Chunk 008).
- Leads to: Instrumental Variables and 2SLS (Chunk 010).
