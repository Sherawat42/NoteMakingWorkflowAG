# Chunk 008 — Critical Values Table, P-value, Type I/II Errors, Power, Tests under Normality
<!-- Pages: 71-80 -->
<!-- Continues from: Unit 31 alternative hypothesis & critical region (Chunk 007) -->
<!-- Continues into: Unit 31 comparison of two normal distributions, bivariate (Chunk 009) -->

## Section: Critical Values of Z (Table 31.1) 🔴
<!-- Reason: tabulated values; commonly memorized for exam -->

### Key Concepts
- Two-tailed |z_α| at 1%, 5%, 10%: 2.58, 1.96, 1.645
- Right-tailed z_α: 2.33, 1.645, 1.28
- Left-tailed: -2.33, -1.645, -1.28
- Note: small n (<30) → cannot use these normal values

## Section: Critical Region Method vs. P-value Method 🔴
<!-- Reason: two ways to test; modern stat papers use p-value -->

### Key Concepts
- Critical Region method: compare test stat with z_α
- P-value method: compare P-value with α
- P-value = lowest level of significance at which H₀ could be rejected
- Steps to compute p-value (4 steps for two-tailed)
- Decision rule: P-value < α → reject H₀

### Definitions ⭐
- P-value ⭐

### Subsection: Guidelines for P-values
- P < 0.01 → significant at 1%
- 0.01 ≤ P < 0.05 → significant at 5%
- 0.05 ≤ P < 0.10 → consider Type I error consequences
- P ≥ 0.10 → not significant

## Section: Procedure for Hypothesis Testing 🔴
<!-- Reason: 5-step recipe; appears verbatim -->

### Mechanism
1. Set H₀
2. Set H₁ (decide tail type)
3. Choose α (in advance)
4. Compute test statistic z = (t-E(t))/SE(t)
5. Compare |Z| with z_α; reject or accept

### Subsection: Summary Table (Table 31.2 Population Mean σ Known)
- Lower-tail: H₀: μ ≥ μ₀, reject if z ≤ -z_α
- Upper-tail: H₀: μ ≤ μ₀, reject if z ≥ z_α
- Two-tailed: H₀: μ = μ₀, reject if |z| ≥ z_(α/2)

### Examples
- Junior manager salary example (n=30, x̄=43260, μ=42000, σ=5260, α=0.05): z=1.32 < 1.65 → don't reject H₀
- Wind speed P-value example (n=32, x̄=8.2, μ=8, s=0.6): z=1.89, P=0.0294, two-tailed compare to α/2=0.025 → not significant

## Section: Type I and Type II Error 🔴
<!-- Reason: foundational; CYP / explicit unit objective -->

### Key Concepts
- Type I: Reject H₀ when true (probability α)
- Type II: Accept H₀ when false (probability β)
- Producer's risk vs. Consumer's risk
- Trade-off: cannot reduce both for fixed n
- α = level of significance = size of critical region
- β used to define power

### Definitions ⭐
- Type I Error ⭐
- Type II Error ⭐
- Producer's risk / Consumer's risk

## Section: Power of the Test 🔴
<!-- Reason: defines test quality; cited everywhere -->

### Key Concepts
- Power = 1 − β = P(reject H₀ | H₁ true)
- Power function (1 − β) as function of parameter

### Definitions ⭐
- Power of the test ⭐
- Power function

## Section: Optimum Test Under Different Situations 🔴
<!-- Reason: explicit Unit objective; named test types -->

### Subsection: Most Powerful Test
- Critical region W is MP if P(x∈W|H₀) = α and P(x∈W|H₁) ≥ P(x∈W₁|H₁) for any other W₁

### Subsection: Uniformly Most Powerful Test
- For composite alternative; same condition for all θ ≠ θ₀

### Definitions ⭐
- Most Powerful Test ⭐
- Uniformly Most Powerful Test ⭐

## Section: Test Procedure Under Normality — Univariate Normal 🔴
<!-- Reason: case-by-case derivation; common exam questions -->

### Subsection: Univariate Normal — Case I: μ unknown, σ known
- Test stat: T = √n(x̄ − μ₀)/σ ~ N(0,1) under H₀
- Right-/left-/two-tailed rejection rules
- CI: x̄ ± τ_(α/2) · σ/√n

### Subsection: Case II: μ known, σ unknown
- Test stat: ψ = Σ(xᵢ − μ)²/σ₀² ~ χ²(n) under H₀
- Three rejection rules
- CI for σ²: [Σ(xᵢ−μ)²/χ²_(α/2,n), Σ(xᵢ−μ)²/χ²_(1-α/2,n)]

### Subsection: Case III: μ and σ both unknown
- Test stat: t = √n(x̄ − μ₀)/s' ~ t(n−1) — Student's t-test
- CI for μ: x̄ ± t_(α/2,n-1) · s'/√n
- For σ: (n−1)s'²/σ² ~ χ²(n−1)

### Definitions ⭐
- Student's t-test ⭐
- s² vs. s'² distinction

<!-- Continues in chunk 009 -->
