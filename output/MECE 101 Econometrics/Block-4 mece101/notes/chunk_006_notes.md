# Chunk 006 — Simultaneity Bias and Identification
<!-- Pages: 52-61 -->
<!-- Source: chunk_006.txt -->
<!-- Continues from: 16.3 Endogenous Variables and Exogenous Variables (Chunk 005) -->

## Section: 16.4 Simultaneity Bias 🔴

### Core Idea
Simultaneity bias occurs when Ordinary Least Squares (OLS) is applied to an equation that belongs to a simultaneous equations system. The bias arises because an explanatory variable is correlated with the stochastic error term, violating a fundamental OLS assumption.

> **In Simple Terms:** If you try to draw a straight line (run OLS) on data where X and Y cause each other, your math will be systematically wrong. It will give you a "biased" answer because it ignores half the relationship.

### Key Concepts

#### Covariance between Explanatory Variable and Error Term
The core assumption of classical OLS is `cov(X, u) = 0`. In a simultaneous system, a change in the error term `u` affects the dependent variable `Y`. Because `Y` also determines `X` (in another equation), the change in `u` indirectly affects `X`. Thus, `X` and `u` move together, meaning `cov(X, u) ≠ 0`.

### Definitions
- **Simultaneity Bias**: The statistical bias that results from applying standard OLS to estimate the parameters of a simultaneous equations model, leading to inaccurate parameter estimates. ⭐ (exam-important)

### Connections
- Connects back to the OLS assumptions introduced earlier in the course.

---

## Section: 16.4.1 Endogeneity Problem 🟡

### Core Idea
The endogeneity problem is the specific mathematical manifestation of simultaneity bias. By substituting equations within a system, we can mathematically prove that an endogenous explanatory variable is correlated with the error term.

> **In Simple Terms:** We can use algebra to prove that in a two-way street, the "random noise" (error term) in one equation leaks over and mixes with the input variables of the other equation.

### Key Concepts

#### Correlation between Y and u
Using the Keynesian model (`C_t = β₀ + β₁Y_t + u_t` and `Y_t = C_t + I_t`), if we substitute the consumption function into the income identity, we find that `Y_t` is a function of `u_t`. 
Specifically, `Y_t = β₀/(1-β₁) + I_t/(1-β₁) + u_t/(1-β₁)`. 
When we calculate the covariance, we get `cov(Y_t, u_t) = σ² / (1-β₁)`. Since `σ²` is positive, the covariance is non-zero.

### Definitions
- **Endogeneity**: A situation where an explanatory variable is correlated with the error term in a regression model. ⭐ (exam-important)

---

## Section: 16.4.2 The OLS Estimator is Biased 🟡

### Core Idea
Because of the endogeneity problem, the expected value of the OLS estimator is not equal to the true population parameter. 

> **In Simple Terms:** If we use OLS, our average guess for the relationship will always be off the true mark.

### Key Concepts

#### OLS Bias Proof
The OLS estimator `β₁_hat = Σyc / Σy²`. In deviation form, expanding this yields `β₁_hat = β₁ + Σ(yu) / Σy²`.
Taking the expectation: `E(β₁_hat) = β₁ + E[Σ(yu) / Σy²]`. 
Because `Y` and `u` are correlated, the second term is not zero. Therefore, `E(β₁_hat) ≠ β₁`, proving the estimator is biased.

### Definitions
- **Biased Estimator**: An estimator whose expected value (average across repeated samples) does not equal the true population parameter. ⭐ (exam-important)

---

## Section: 16.4.3 The OLS Estimator is not Consistent 🟡

### Core Idea
Not only is the OLS estimator biased in small samples, but the bias also persists even if the sample size increases infinitely. The estimator does not converge to the true value.

> **In Simple Terms:** Even if we had an infinite amount of data, OLS would still give us the wrong answer because the fundamental math is flawed for this specific situation.

### Key Concepts

#### Inconsistency Proof (plim)
An estimator is consistent if its probability limit (`plim`) equals the true parameter. 
Applying plim rules: `plim(β₁_hat) = β₁ + plim[Σ(yu)/n] / plim[Σy²/n]`.
Since `plim[Σ(yu)/n]` approaches the population covariance (which is `σ² / (1-β₁)` and not zero), `plim(β₁_hat) = β₁ + [σ²/(1-β₁)] / σ_y²`.
Assuming `0 < β₁ < 1`, this means `plim(β₁_hat) > β₁`. The estimator overestimates the true parameter regardless of sample size.

### Definitions
- **Inconsistent Estimators**: Estimators whose values do not converge to the true population parameter even as the sample size approaches infinity. ⭐ (exam-important)

---

## Section: 16.4.4 Solution to Simultaneity Bias 🟡

### Core Idea
Because standard OLS is biased and inconsistent for SEMs, specialized estimation methods must be used to obtain consistent estimates.

> **In Simple Terms:** Since OLS is broken for these models, we have to use different, more advanced statistical tools to solve the math.

### Key Concepts

#### Estimation Methods
The most common methods to resolve simultaneity bias include:
1. Reduced form method (Indirect Least Squares - ILS)
2. Instrumental variables (IV)
3. Two-stage least squares (2SLS)
4. Limited information maximum likelihood (LIML)
5. Three-stage least squares (3SLS)
6. Full information maximum likelihood (FIML)

---

## Section: 16.5 Structural Form and Reduced Form 🔴

### Core Idea
A simultaneous equations model can be written in two distinct forms: the structural form (representing theoretical relationships) and the reduced form (expressing endogenous variables solely in terms of predetermined variables).

> **In Simple Terms:** "Structural" is how we think the world works (A causes B, B causes A). "Reduced" is when we do algebra to solve for A and B so that they only depend on outside factors, making the math solvable.

### Key Concepts

#### Structural Equations
Equations that represent the underlying economic theory or behavior. They contain both endogenous and exogenous variables on the right-hand side. For example, the basic consumption function `C_t = β₀ + β₁Y_t + u_t`.

#### Reduced-Form Equations
Derived by solving the structural equations algebraically for the endogenous variables. In a reduced-form equation, an endogenous variable is expressed *solely* as a function of predetermined (exogenous) variables and stochastic error terms. Because only predetermined variables are on the right side, OLS can be applied to reduced-form equations without simultaneity bias.

### Definitions
- **Structural Equation**: Equations which represent the structure of an economic model or the behavior of an economic agent. ⭐ (exam-important)
- **Structural Parameters**: Parameters (like βs and γs) appearing in the structural equations. ⭐ (exam-important)
- **Reduced Form Models**: Models where each equation contains only one endogenous dependent variable expressed solely in terms of predetermined variables. ⭐ (exam-important)
- **Reduced Form Parameters (Impact Multipliers)**: Parameters of the reduced form equations (often denoted by Π). They measure the immediate impact on the endogenous variable of a unit change in an exogenous variable. ⭐ (exam-important)

### Connections
- Reduced forms provide a pathway to solving the Endogeneity Problem (Chunk 006).

---

## Section: 16.6 Concept of Identification 🔴

### Core Idea
Identification asks whether we can work backwards from the solvable reduced-form parameters to discover the underlying structural parameters. If we cannot uniquely deduce the structural parameters, the model is unidentified.

> **In Simple Terms:** We can solve the "Reduced Form" math easily. But can we use those answers to figure out the original "Structural" numbers we actually care about? That puzzle is called Identification.

### Key Concepts

#### Identification Problem
Identification is a problem of model formulation, not estimation. Before attempting to estimate a model, we must ensure it is uniquely defined statistically.

#### Observationally Equivalent Theories
If multiple different structural theories are consistent with the exact same data, they are observationally equivalent. For example, a scatter plot of market prices and quantities represents the intersection of supply and demand. Without further information, a line drawn through these points could be supply, demand, or a "mongrel equation" combining both.

### Definitions
- **Identification**: The possibility (or impossibility) of deducing the values of the structural parameters from the reduced form parameters. ⭐ (exam-important)

---

## Section: 16.6.1 Paradox of Identification 🟡

### Core Idea
To identify a specific equation within a system, it must lack certain variables that are present in other equations. This allows shifts in those other equations to trace out the stable equation.

> **In Simple Terms:** To identify the demand curve, we need a variable that shifts the supply curve (like fertilizer price) but *doesn't* affect demand. The fact that fertilizer price is *missing* from the demand equation is what allows us to identify demand!

### Key Concepts

#### Exclusion Restrictions
Assuming that certain exogenous variables do not appear in specific equations. In the paradox of identification, the relevant variables for identifying an equation are the ones that are *absent* from it but present elsewhere in the system.

### Definitions
- **Paradox of Identification**: The concept that identification is achieved in terms of the variables *absent* from the equation, not in terms of the variables present. ⭐ (exam-important)

---

## Section: 16.6.2 Identification Status of an Equation 🟡

### Core Idea
Every equation in a simultaneous system falls into one of three identification categories, which dictates how (and if) it can be estimated.

> **In Simple Terms:** 
> - **Under-identified**: Not enough info to solve it (stuck).
> - **Exactly identified**: Just enough info to find one unique answer (perfect).
> - **Over-identified**: So much info we get multiple conflicting answers (needs special math to average them out).

### Key Concepts

#### Under-identified
The structure of the equation is not unique; there is insufficient information to distinguish the equation. It cannot be estimated.

#### Exactly Identified
There is exactly sufficient information to obtain unique estimators for each structural parameter. Estimated using Indirect Least Squares (ILS).

#### Over-identified
There is more than sufficient information, leading to multiple possible estimates for some structural parameters. Indirect least squares cannot be used; methods like Two-Stage Least Squares (2SLS) must be employed.

### Definitions
- **Under-identified Equation**: An equation without sufficient information to uniquely distinguish its structural parameters. ⭐ (exam-important)
- **Exactly-identified Equation**: An equation with exactly sufficient information to yield unique structural parameter estimates. ⭐ (exam-important)
- **Over-identified Equation**: An equation with more than sufficient information, yielding multiple possible estimates for structural parameters. ⭐ (exam-important)

### Connections
- Sets up the mathematical rules (Order and Rank conditions) for determining this status in Chunk 007.
<!-- Continues in chunk 007 -->
