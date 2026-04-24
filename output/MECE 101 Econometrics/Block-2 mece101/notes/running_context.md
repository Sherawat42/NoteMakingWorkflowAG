# Running Context

## Key Concepts Introduced
- **Bivariate Regression Model** (Chunk 001): Yᵢ = β₁ + β₂Xᵢ + uᵢ — two-variable linear regression
- **Population Regression Function (PRF)** (Chunk 001): True unobservable relationship in population
- **Sample Regression Function (SRF)** (Chunk 001): Estimated relationship from sample: Ŷᵢ = β̂₁ + β̂₂Xᵢ
- **OLS Normal Equations** (Chunk 001): ΣYᵢ = nβ̂₁ + β̂₂ΣXᵢ and ΣXᵢYᵢ = β̂₁ΣXᵢ + β̂₂ΣXᵢ²
- **Method of Moments** (Chunk 001): Equates sample moments to population moments; identical to OLS here
- **Gauss-Markov Theorem** (Chunk 001 reference): OLS is BLUE under classical assumptions

## Definitions (⭐ exam-important)
- **Estimation** (Chunk 001): Recovering unknown parameters from sample data
- **Residual ûᵢ** (Chunk 001): ûᵢ = Yᵢ − Ŷᵢ; differs from error term uᵢ
- **RSS** (Chunk 001): Σûᵢ² — minimized by OLS
- **Normal Equations** (Chunk 001): Two equations from ∂RSS/∂β̂ᵢ = 0
- **OLS estimator β̂₂** (Chunk 001): Σxᵢyᵢ / Σxᵢ²
- **OLS estimator β̂₁** (Chunk 001): Ȳ − β̂₂X̄
- **Classical Regression Model** (Chunk 001): Model satisfying all 5 classical assumptions
- **Homoscedasticity** (Chunk 001): E(uᵢ²) = σ² — constant error variance
- **No Autocorrelation** (Chunk 001): E(uᵢuⱼ) = 0 for i ≠ j
- **Likelihood Function** (Chunk 001): Joint probability of sample data as function of parameters
- **MLE of σ²** (Chunk 001): σ̃² = RSS/n — biased but consistent
- **Semi-log model** (Chunk 001): ln Y = β₁ + β₂X; β₂ = % change in Y per unit ΔX
- **Double-log model** (Chunk 001): ln Y = β₁ + β₂ ln X; β₂ = elasticity

## Named Models / Laws / Theories
- **Gauss-Markov Theorem** (Chunk 001 reference): OLS is BLUE under classical assumptions; proved in Chunk 002

- **Standard Error se(β̂₂)** (Chunk 002): σ/√(Σxᵢ²); measures precision of slope estimate
- **Gauss-Markov Theorem** (Chunk 002): OLS is BLUE under CLRM; normality NOT required
- **TSS = ESS + RSS** (Chunk 002): variance decomposition; r² = ESS/TSS
- **t-test for β₂** (Chunk 002): t = (β̂₂ − β₂*)/se(β̂₂) ~ t(n−2)
- **Residual plot patterns** (Chunk 003): random=ok; U-shape/funnel=problems
- **JB test for normality** (Chunk 004): JB = (n/6)[S²/6 + (K−3)²/24] ~ χ²(2)
- **Multiple regression Y = Xβ + U** (Chunk 005): matrix form; β̂ = (X'X)⁻¹X'Y
- **Gauss-Markov (matrix)** (Chunk 006): var(β̃) − var(β̂) = σ²DD' ≥ 0 → OLS BLUE
- **Adjusted R²** (Chunk 007): R̄² = 1 − (1−R²)(n−1)/(n−k); can be negative
- **F-test** (Chunk 007): F = [R²/(k−1)]/[(1−R²)/(n−k)] ~ F(k−1, n−k)
- **Wald/LM/LR** (Chunk 008): all ~ χ²(J); Wald=unrestricted; LM=restricted; LR=both

## Key Data & Numbers
- Wage-schooling example (Chunk 001): ŵ = 0.89 + 0.63s; n = 600 workers
- Savings-income example (Chunk 001): Savings = 34,560 + 0.58·Income; n = 20 households
- CYP answers (Chunk 003): β̂₂ = 0.5413; β̂₁ = −0.9043; σ̂² = 11.41; r² = 0.1648 (n=526 workers)
- Example 7.1 (Chunk 007): n=5, k=3; R² = 0.93; R̄² = 0.86
- CEO salary example (Chunk 008): n=209; t(sales)=7.94, t(roe)=4.25, t(ros)=0.44; F=26.91
