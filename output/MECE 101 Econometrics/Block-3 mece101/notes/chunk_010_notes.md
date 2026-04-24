# Chunk 010 — Instrumental Variables and 2SLS
<!-- Pages: 90-97 -->
<!-- Source: chunk_010.txt -->

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
- Solves the problem introduced in: Endogeneity Problem (Chunk 009)

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
