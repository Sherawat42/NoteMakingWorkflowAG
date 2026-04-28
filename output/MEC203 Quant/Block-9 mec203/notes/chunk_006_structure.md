# Chunk 006 — MVUE Continued, Sufficiency, Cramer-Rao, Asymptotic, Methods of Estimation
<!-- Pages: 51-60 -->
<!-- Continues from: Unit 30 estimator properties (Chunk 005) -->
<!-- Continues into: Unit 30 worked problems + Unit 31 Hypothesis Testing (Chunk 007) -->

## Section: MVUE Example — x̄ for Normal Mean 🟡
<!-- Reason: worked derivation of MVUE for normal -->

### Key Concepts
- Mean vs. Median efficiency: efficiency of mean = (2/π) ≈ 0.64
- → Var(x̄) < Var(Median)

## Section: Sufficiency 🔴
<!-- Reason: critical concept tied to MVUE; CYP problem -->

### Key Concepts
- Definition: T sufficient if conditional dist of x given T is independent of θ
- Factorization Theorem (Neyman): L = g_θ[t(x)]·h(x)
- Original sample is always sufficient
- Koopman's form / Exponential family: L = g(x)h(θ)exp{a(θ)w(x)}
- Invariance property: ψ(T) is sufficient for ψ(θ) if 1-1
- Fisher-Neyman criterion

### Definitions ⭐
- Sufficient estimator ⭐
- Factorization theorem ⭐
- Exponential family of distributions

## Section: Cramer-Rao Inequality 🔴
<!-- Reason: famous result; given as Unit 30 objective -->

### Key Concepts
- Lower bound on variance of unbiased estimator
- Var(θ̂) ≥ 1/{nE[(∂lnf/∂θ)²]}
- Information I(θ) = nE[(∂lnf/∂θ)²]
- Regularity conditions (5 conditions listed)
- MVB estimator: attains Cramer-Rao bound

### Definitions ⭐
- Cramer-Rao Inequality ⭐
- Minimum Variance Bound (MVB) estimator
- Fisher Information

## Section: MVUE and Blackwellisation / Rao-Blackwell Theorem 🟡
<!-- Reason: technique to obtain MVUE; theorem named -->

### Key Concepts
- Rao-Blackwell theorem statement
- Blackwellisation: improving unbiased estimator using sufficient statistic
- φ(T) = E(Y|T=t): unbiased and Var ≤ Var(Y)
- Completeness → uniqueness

### Definitions ⭐
- Rao-Blackwell Theorem ⭐
- Blackwellisation
- Completeness

## Section: Asymptotic Properties 🔴
<!-- Reason: large-sample theory; explicitly listed unit objective -->

### Subsection: Asymptotic Unbiasedness
- lim B(θ̂_n) = θ as n → ∞

### Subsection: Asymptotic Consistency
- lim Pr(|θ̂ − θ| > ε) = 0
- Convergence in probability
- Sufficient condition: unbiased + Var → 0
- Example: S² consistent for σ² in normal population

### Subsection: Convergence in Distribution and Asymptotic Normality
- Z_n →ᴰ Z if P(Z_n ≤ z) → P(Z ≤ z)
- Asymptotic standard normal
- CLT restated: Z_n = (x̄−μ)/(σ/√n) →ᴰ N(0,1)

### Definitions ⭐
- Convergence in probability
- Convergence in distribution ⭐
- Asymptotic normality ⭐

## Section: Methods of Estimation 🔴
<!-- Reason: explicitly named (ML, GMM, PLS) and required by Unit objective -->

### Subsection: Maximum Likelihood (ML) 🔴
- Likelihood function L(θ) = ∏f(xᵢ|θ)
- Log-likelihood ℓ(θ) = ΣlogL
- MLE: argmax of L (or ℓ)
- "Excellent" estimator for large samples

### Subsection: Generalized Method of Moments (GMM) 🟡
- Uses moment conditions m(θ₀) = E[g(Y_t,θ)] = 0
- Sample analog: ĝ(θ) = (1/T)Σg(Y_t,θ)
- Robustness: doesn't require full distribution
- Asymptotically normal, consistent, efficient

### Subsection: Partial Least Squares (PLS) 🟡
- Use case: many correlated explanatory variables
- Reduces dimensionality via Principal Component Analysis (PCA)
- Identifies uncorrelated components

### Definitions ⭐
- Maximum Likelihood Estimator (MLE) ⭐
- GMM
- PLS
- PCA

<!-- Continues in chunk 007 -->
