# Running Context

## Key Concepts Introduced
- **Regression Model** (Chunk 001): Statistical technique to estimate relationship between dependent and independent variables
- **Population Regression Function** (Chunk 001): The unknown true relationship Y = α + βX + U in the population
- **Sample Regression Function** (Chunk 001): The estimated counterpart Ŷ = α̂ + β̂X + Û from sample data
- **Disturbance Term / U** (Chunk 001): Random variable capturing all unexplained variation in the dependent variable
- **OLS Estimators** (Chunk 002): β̂ = Σxy/Σx², α̂ = Ȳ − β̂X̄ — minimize sum of squared residuals
- **R² (Coefficient of Determination)** (Chunk 002): ESS/TSS = proportion of Y variation explained by regression
- **TSS = ESS + RSS** (Chunk 002): Fundamental decomposition of total variation in Y
- **Log-linear Model** (Chunk 002): log Y = α + β log X — β measures constant elasticity (% ΔY/% ΔX)

## Definitions (⭐ exam-important)
- **Linearity in Parameter** (Chunk 001): A model is linear if the highest power of any parameter (α, β) is one — this is the requirement for OLS estimation
- **Classical Regression Model Assumptions** (Chunk 001): Five key assumptions: zero mean of U, homoscedasticity, no autocorrelation, non-stochastic X, linear in parameter
- **Disturbance Term** (Chunk 001): Random variable U introduced to capture inherent randomness, omitted variables, measurement errors, and specification errors
- **Homoscedasticity** (Chunk 001): Assumption that variance of U is constant for all X values: V(X) = σ²
- **BLUE** (Chunk 002): Best Linear Unbiased Estimator — property OLS estimators hold under classical assumptions (Gauss-Markov)
- **Standard Error of Estimate** (Chunk 002): σ̂ = √[Σ Û²/(n−2)]; denominator uses degrees of freedom n−2
- **R²** (Chunk 002): ESS/TSS = 1 − RSS/TSS; ranges 0 to 1; proportion of Y variation explained by regression
- **Adjusted R² (R̄²)** (Chunk 005): Coefficient of determination adjusted for degrees of freedom; penalizes adding unnecessary variables
- **Multi-co-linearity** (Chunk 006): Exact or near-exact linear relationship between explanatory variables; breaks or weakens OLS
- **Heteroscedasticity** (Chunk 006): Variance of error terms differs across observations (σᵢ² ≠ σ²); OLS is no longer BLUE
- **Autocorrelation** (Chunk 006): Correlation between error terms at different time periods: E(uᵢuⱼ) ≠ 0
- **Maximum Likelihood Estimation (MLE)** (Chunk 006): Estimation method maximizing the probability of observing data; MLE β = OLS β under normality
- **Positive Measures of Inequality** (Chunk 007): Captures inequality without value judgments (e.g., Range, Gini, RSD)
- **Normative Measures of Inequality** (Chunk 009): Incorporates value judgments about social welfare (e.g., Dalton, Atkinson, Sen, Theil)
- **Gini Index** (Chunk 008): Mean absolute difference between all pairs of incomes divided by 2μ; bounded in [0, 1]
- **Lorenz Curve** (Chunk 008): Graphical tool plotting cumulative population against cumulative income (Qᵢ ≤ Pᵢ)
- **Atkinson Index & ε** (Chunk 009): Measures inequality based on equally distributed equivalent income (μ*); ε = inequality aversion parameter
- **Composite Index** (Chunk 011): A combined multi-dimensional score made of different unidimensional scores
- **Principal Component Analysis (PCA)** (Chunk 012): Technique transforming correlated variables into a smaller set of uncorrelated components (eigenvalues > 1)

## Named Models / Laws / Theories
- **Classical Linear Regression Model (CLRM)** (Chunk 001): Two-variable regression model Y = α + βX + U under five classical assumptions
- **Gauss-Markov Theorem** (Chunk 002): Under classical assumptions, OLS estimators are BLUE (Best Linear Unbiased Estimators)
- **Log-linear / Double-log Model** (Chunk 002): log Y = α + β log X; β = constant elasticity
- **Durbin-Watson d Test** (Chunk 006): Most common test for autocorrelation. d ≈ 2 means no problem.
- **Dalton Index** (Chunk 009): D = 1 − [actual welfare / maximum possible welfare]. Assumes additive, concave U(x). Not scale-invariant.
- **Atkinson Index** (Chunk 009): A = 1 − μ*/μ. Invariant to scale transformations.
- **Theil Entropy Index** (Chunk 009): Index derived from information theory; decomposable into between-group and within-group.
- **Pigou-Dalton Transfer Condition** (Chunk 010): Transfer from richer to poorer must strictly reduce inequality.
- **Sen Transfer Condition** (Chunk 010): Transfer at lower income bound must have a greater inequality-reducing impact than at a higher bound.

## Key Data & Numbers
<!-- To be updated as chunks are processed -->
