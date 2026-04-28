# Chunk 005 — Sampling Distribution of s², CLT, Unit 30 Estimation Intro & Properties
<!-- Pages: 41-50 -->
<!-- Continues from: Unit 29 sampling distributions (Chunk 004) -->
<!-- Continues into: Unit 30 sufficiency, Cramer-Rao, asymptotic properties (Chunk 006) -->

## Section: Sampling Distribution of s² 🟡
<!-- Reason: completes Unit 29's distribution result -->

### Key Concepts
- p.d.f of s²: chi-square form

## Section: Central Limit Theorem 🔴
<!-- Reason: foundational theorem; widely cited -->

### Key Concepts
- Law of large numbers (preview)
- CLT statement: x_i independent → S_n asymptotically N(μ, σ²)
- Use case: non-randomly distributed observations

### Definitions ⭐
- Central Limit Theorem ⭐

## Section: Unit 29 — Let Us Sum Up + Key Words + Exercises 🟢

### Key Concepts
- KW: CLT, Chi-square dist, F dist, Fisher's t, Student's t, Standard normal
- Worked Q1: 9:3:3:1 ratio test → χ² = 4.7266 < 7.815 → accept H₀
- Worked Q2: t-test for bulb life: t = -0.7745, df=14, P = 0.226

## Section: Unit 30 Estimation — Objectives & Introduction 🟢
<!-- Reason: orients statistical inference framework -->

### Key Concepts
- Statistical inference: estimation vs. hypothesis testing
- Point estimation vs. interval estimation
- Confidence interval / confidence limits

## Section: Theory of Estimation — Parameter Space 🟡

### Key Concepts
- Parameter space Θ
- Family of distributions {f(x;θ): θ∈Θ}
- Estimator function notation T_n = θ̂(x₁,...,x_n)

### Definitions ⭐
- Parameter space ⭐

## Section: Characteristics of Estimators 🔴
<!-- Reason: core exam topic; "describe characteristics of good estimators" Unit objective -->

### Key Concepts
- Four properties: Unbiasedness, Consistency, Efficiency, Sufficiency

### Subsection: Unbiasedness 🔴
- E(T_n) = θ
- Examples: x̄ for μ; X/n for binomial p; S² unbiased for σ² of infinite population
- Bias b(θ) = E(T_n) − τ(θ); positive vs negative bias
- Caveats: not preserved under functional transformation; not unique

### Subsection: Consistency 🔴
- T_n →ᴾ τ(θ) as n→∞
- Khinchin's WLLN → x̄ is always consistent for μ
- Sufficient conditions: E(T_n)→τ(θ) AND Var(T_n)→0

### Subsection: Efficiency 🔴
- Asymptotic variance criterion
- Most Efficient Estimator: smallest sampling variance
- Efficiency E = V₁/V₂ ≤ 1
- MVUE: Minimum Variance Unbiased Estimator
  - Uniqueness theorem
  - Correlation bounds with other unbiased estimators
  - Example: x̄ is MVUE of μ for normal

### Definitions ⭐
- Unbiased estimator ⭐
- Consistent estimator ⭐
- Efficient estimator ⭐
- Most Efficient Estimator
- MVUE ⭐

<!-- Continues in chunk 006 -->
