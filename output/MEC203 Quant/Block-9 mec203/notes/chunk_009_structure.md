# Chunk 009 — Comparison of Two Normal Distributions, Bivariate Normal, Unit 31 Wrap-up
<!-- Pages: 81-90 -->
<!-- Continues from: Unit 31 univariate normal tests (Chunk 008) -->
<!-- Continues into: Unit 31 answers/exercises + Bibliography + Tables (Chunk 010) -->

## Section: Comparison of Two Univariate Normal Distributions 🔴
<!-- Reason: two-sample tests are heavily tested -->

### Subsection: Case I — μ₁,μ₂ unknown, σ₁,σ₂ known
- Test stat: T = ((x̄₁−x̄₂)−ε₀)/√(σ₁²/n₁ + σ₂²/n₂) ~ N(0,1)
- Confidence limits for (μ₁−μ₂)

### Subsection: Case II — μ₁,μ₂ known, σ₁,σ₂ unknown
- Test ratio σ₁²/σ₂² = ξ₀
- F = [Σ(x_{1j}-μ₁)²/n₁σ₁²] / [Σ(x_{2j}-μ₂)²/n₂σ₂²] ~ F(n₁,n₂)
- Three rejection rules
- F = 1 when ξ₀=1 (test of equality of variances)

### Subsection: Case III — All unknown (means and variances)
- Pooled variance: s² = [(n₁−1)s₁² + (n₂−1)s₂²]/(n₁+n₂−2)
- Fisher's t-test: t = ((x̄₁−x̄₂) − ε₀)/(s·√(1/n₁ + 1/n₂)) ~ t(n₁+n₂−2)
- Confidence limits for (μ₁−μ₂)
- F-test for σ₁²/σ₂² uses sample-mean-replaced version with df (n₁−1, n₂−1)

### Definitions ⭐
- Pooled variance ⭐
- Fisher's t-test ⭐ (two-sample t)
- F-test for variance equality

## Section: Problems Relating to Bivariate Normal Distribution 🔴
<!-- Reason: explicit Unit objective + multiple CYP problems -->

### Subsection: Test for Correlation Coefficient
- Sample r = Σ(xᵢ−x̄)(yᵢ−ȳ)/√[Σ(xᵢ−x̄)²·Σ(yᵢ−ȳ)²]
- When ρ=0: t = r√(n−2)/√(1−r²) ~ t(n−2)
- ρ ≠ 0 case: complicated, approximate test for large n

### Subsection: Difference between μ_x and μ_y (paired t)
- z = x − y, normally distributed
- z̄ ± t·s_z/√n with df = n − 1
- Paired t-test for ratios as well

### Subsection: Ratio σ_x/σ_y (variance ratio in bivariate)
- u = x + ξ y, v = x − ξ y → cov(u,v) = 0
- Test H₀: σ_x/σ_y = ξ₀ via H₀: ρ_uv = 0
- Quadratic equation for confidence limits

### Definitions ⭐
- Paired t-test ⭐
- Sample correlation coefficient ⭐

## Section: Unit 31 Let Us Sum Up + Key Words 🟢

### Definitions ⭐
- Alternative hypothesis ⭐
- Confidence interval / limits ⭐
- Critical region ⭐
- Level of significance ⭐
- Null hypothesis ⭐
- One-tailed / Two-tailed tests ⭐
- Critical/significant values
- Most powerful test ⭐
- Uniformly most powerful test ⭐
- Parameter space
- Power of the test ⭐
- Type I and Type II error ⭐

## Section: Beginning of Unit 31 Answers/Hints 🟢
<!-- Reason: continues into chunk 010 -->

<!-- Continues in chunk 010 -->
