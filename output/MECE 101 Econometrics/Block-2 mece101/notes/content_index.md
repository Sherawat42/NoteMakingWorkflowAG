# Content Index
**Source**: Block-2 mece101.pdf | **Chunks**: 8 | **Completed**: 2026-04-24T03:19:00Z

## Notes Files

| Chunk | Title | Pages | Top Sections | Key Terms |
|-------|-------|-------|-------------|-----------|
| 001 | Unit 4: Estimation Setup & Methods | 1–10 | Classical Assumptions, OLS, MOM, MLE, Model Interpretation | PRF, SRF, residual, RSS, normal equations, β̂₁, β̂₂, MLE, semi-log, double-log |
| 002 | Unit 4: SE, Properties, r², t-Test, Forecasting | 11–22 | Standard Errors, BLUE/Gauss-Markov, r², t-test, Forecasting | se(β̂), σ̂², BLUE, TSS/ESS/RSS, r², t-distribution, confidence interval, mean/individual forecast |
| 003 | Unit 5: Residuals & Residual Plots | 23–31 | Unit 4 answers, Residual definition, Residual plot patterns | residual, ûᵢ, horizontal band, funnel, U-shape, double bow, heteroscedasticity |
| 004 | Unit 5: Outliers, Normality, Special Cases | 32–39 | Outliers, Visual diagnostics, JB test, Regression through origin, Change in scale | outlier, JB test, P-P plot, skewness K=3, zero-intercept, origin, scale, standardized |
| 005 | Unit 6: Multiple Regression Matrix Form | 40–49 | Multiple Regression Specification, Y=Xβ+U, CLRM (matrix), OLS derivation | ceteris paribus, design matrix X, σ²I, full rank, X'Xβ̂=X'Y, β̂=(X'X)⁻¹X'Y |
| 006 | Unit 6: OLS Properties & Gauss-Markov | 50–58 | Unbiasedness, var(β̂)=σ²(X'X)⁻¹, σ̂²=RSS/(n−k), BLUE proof | E(β̂)=β, idempotent M, var(β̂), σ̂², BLUE, CC'=(X'X)⁻¹+DD', positive semi-definite |
| 007 | Unit 7: R², Adjusted R², t-test, F-test | 59–68 | R²=ESS/TSS, Adjusted R², t-test (multiple), CI, F-test, Linear restrictions | R², R̄², over-fitting, tₖ=bₖ/se(bₖ), F=RSS comparison, Rβ=q, Cobb-Douglas |
| 008 | Unit 7: Wald, LM, LR Tests | 69–77 | Wald test, LM test, LR test, Comparison table | W~χ²(J), score function, LM=q̃'Ĩ⁻¹q̃, LR=2Δ(lnL), Wald/LM/LR equivalence |

---

## Cross-References

| From | To | Relationship |
|------|-----|-------------|
| OLS Normal Equations (Chunk 001) | Normal Equations Matrix (Chunk 005) | Matrix form extends bivariate version |
| Classical Assumptions (Chunk 001) | Matrix Assumptions (Chunk 005) | Same 5 conditions in matrix notation |
| Gauss-Markov bivariate (Chunk 002) | Gauss-Markov matrix (Chunk 006) | Matrix proof generalises scalar proof |
| MLE of σ² biased (Chunk 001) | σ̂² = RSS/(n−k) unbiased (Chunk 006) | Contrast MLE vs OLS estimator of variance |
| r² bivariate (Chunk 002) | R² multiple regression (Chunk 007) | Same definition; R² notation for multiple |
| r² bivariate (Chunk 002) | Adjusted R² (Chunk 007) | Adjusted R² corrects for df; R̄² ≤ R² |
| t-test bivariate (Chunk 002) | t-test multiple regression (Chunk 007) | df changes from n−2 to n−k |
| Residual plots (Chunk 003) | Visual heteroscedasticity (Chunk 004) | Funnel pattern → heteroscedasticity |
| RSS/TSS (Chunk 002) | F-test (Chunk 007) | F statistic expressed in terms of R² |
| F-test (Chunk 007) | Wald/LM/LR (Chunk 008) | F handles J restrictions; W/LM/LR general |
| t-test (Chunk 007) | Wald test (Chunk 008) | t-test is special case of Wald (J=1) |
| Linear restrictions (Chunk 007) | Wald/LM/LR (Chunk 008) | General restriction framework tested |

---

## Key Terms Glossary

| Term | Definition | First Appears |
|------|-----------|---------------|
| Estimation | Recovering unknown parameters from sample data | Chunk 001 |
| PRF | Population Regression Function: Yᵢ = β₁ + β₂Xᵢ + uᵢ | Chunk 001 |
| SRF | Sample Regression Function: Ŷᵢ = β̂₁ + β̂₂Xᵢ | Chunk 001 |
| Residual (ûᵢ) | ûᵢ = Yᵢ − Ŷᵢ; estimated error term | Chunk 001 |
| RSS | Residual Sum of Squares = Σûᵢ²; minimized by OLS | Chunk 001 |
| Normal Equations | ∂RSS/∂β̂ᵢ = 0 equations for OLS estimates | Chunk 001 |
| β̂₂ | Σxᵢyᵢ/Σxᵢ²; OLS slope estimator | Chunk 001 |
| β̂₁ | Ȳ − β̂₂X̄; OLS intercept estimator | Chunk 001 |
| Homoscedasticity | E(uᵢ²) = σ² = constant for all i | Chunk 001 |
| MLE of σ² | RSS/n; biased but consistent | Chunk 001 |
| Semi-log model | ln Y = β₁ + β₂X; β₂ = % change in Y per unit X | Chunk 001 |
| Double-log model | ln Y = β₁ + β₂ ln X; β₂ = elasticity | Chunk 001 |
| se(β̂₂) | σ/√(Σxᵢ²); standard error of slope | Chunk 002 |
| σ̂² | RSS/(n−2); unbiased estimator of σ² (bivariate) | Chunk 002 |
| BLUE | Best Linear Unbiased Estimator; what OLS is under CLRM | Chunk 002 |
| Gauss-Markov Theorem | OLS is BLUE under CLRM; no normality needed | Chunk 002 |
| TSS | Σ(Yᵢ − Ȳ)²; Total Sum of Squares | Chunk 002 |
| ESS | Σ(Ŷᵢ − Ȳ)²; Explained Sum of Squares | Chunk 002 |
| r² | ESS/TSS; proportion of Y variation explained | Chunk 002 |
| Confidence interval | bₖ ± t·se(bₖ); range containing true βₖ with (1−α)% probability | Chunk 002 |
| Mean forecasting | E(Y\|X₀) = β̂₁ + β̂₂X₀ | Chunk 002 |
| Individual forecasting | Predicts specific Y₀; wider CI than mean forecast | Chunk 002 |
| Residual plot | Graph of ûᵢ vs Xᵢ or Ŷᵢ; diagnoses model fit | Chunk 003 |
| Funnel shape | Residuals expand/contract; indicates heteroscedasticity | Chunk 003 |
| P-P Plot | Compares theoretical vs sample normal quantiles | Chunk 004 |
| Jarque-Bera (JB) | JB=(n/6)[S²/6+(K−3)²/24] ~ χ²(2); tests normality | Chunk 004 |
| Zero-intercept model | Yᵢ = βXᵢ + uᵢ; forces line through origin | Chunk 004 |
| Change of origin | Subtracting constant from variables; doesn't change β | Chunk 004 |
| Change of scale | Multiplying by constant; changes β but not R² | Chunk 004 |
| Multiple regression | Yᵢ = β₁ + β₂X₂ᵢ + … + βₖXₖᵢ + uᵢ; k regressors | Chunk 005 |
| Ceteris paribus | Holding all other regressors constant | Chunk 005 |
| Design matrix X | (n×k) matrix of all regressor values | Chunk 005 |
| β̂ = (X'X)⁻¹X'Y | OLS estimator in matrix form | Chunk 005 |
| Full rank | Rank(X) = k; X'X is invertible; no multicollinearity | Chunk 005 |
| E(UU') = σ²I | Homoscedasticity + no autocorrelation in matrix form | Chunk 005 |
| var(β̂) = σ²(X'X)⁻¹ | Variance-covariance matrix of OLS estimators | Chunk 006 |
| σ̂² = RSS/(n−k) | Unbiased estimator of error variance (multiple regression) | Chunk 006 |
| Idempotent matrix M | M = I−X(X'X)⁻¹X'; MM=M; MX=0 | Chunk 006 |
| R² (multiple) | ESS/TSS for multiple regression; 0 ≤ R² ≤ 1 | Chunk 007 |
| Adjusted R² | R̄² = 1−(1−R²)(n−1)/(n−k); penalizes extra regressors; can be negative | Chunk 007 |
| t-ratio | bₖ/se(bₖ); tests H₀: βₖ = 0; ~ t(n−k) | Chunk 007 |
| F-test | Joint significance test; F = [(RSS₀−RSS₁)/J]/[RSS₁/(n−k)] ~ F(J,n−k) | Chunk 007 |
| Restricted model | Model with J restrictions imposed under H₀ | Chunk 007 |
| Linear restriction | Rβ = q; constrains multiple coefficients simultaneously | Chunk 007 |
| Wald test | W ~ χ²(J); uses unrestricted model only | Chunk 008 |
| LM test | LM ~ χ²(J); uses restricted model only | Chunk 008 |
| LR test | LR = 2[lnL(θ̂ᵤ)−lnL(θ̂ᴿ)] ~ χ²(J); uses both models | Chunk 008 |
