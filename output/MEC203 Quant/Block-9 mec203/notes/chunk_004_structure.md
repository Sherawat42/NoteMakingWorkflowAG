# Chunk 004 — χ² Properties, Goodness of Fit, t-distribution, F-distribution, Sampling Distributions of x̄ and s²
<!-- Pages: 31-40 -->
<!-- Continues from: Unit 29 — Chi-square distribution intro (Chunk 003) -->
<!-- Continues into: Unit 29 Central Limit Theorem + Unit 30 Estimation (Chunk 005) -->

## Section: Chi-square: Critical Values & Properties 🔴
<!-- Reason: tabular value usage; appears in tests; properties asked in CYP -->

### Key Concepts
- For large n: χ² ~ N(√(2n-1), 1) approximation for n>30
- χ²(α,n) — upper α point (right-tail critical)
- Lower α point: χ²(1-α, n)
- MGF derivation: M(t) = (1-2t)^(-n/2)
- Property 1: If X₁ ~ χ²(n₁) and X₁+X₂ ~ χ²(n) independent, then X₂ ~ χ²(n-n₁)
- Property 2: For sample of size n from N(μ, σ²): x̄ and s² independent; (n-1)s²/σ² ~ χ²(n-1)

### Definitions ⭐
- Critical value / Significant value of χ²

## Section: Chi-square Test of Goodness of Fit 🔴
<!-- Reason: Karl Pearson's test; numerical exam questions; CYP problems -->

### Key Concepts
- Test for discrepancy between observed (Oᵢ) and expected (Eᵢ) frequencies
- Pearson formula: χ² = Σ((Oᵢ - Eᵢ)²/Eᵢ)
- df = n - 1
- Approximate test for large n
- ΣOᵢ = ΣEᵢ constraint

### Definitions ⭐
- Goodness of fit
- Pearson's χ² statistic ⭐

## Section: Student's t-Distribution 🔴
<!-- Reason: foundational; appears in tests; reduces to Cauchy when v=1 -->

### Key Concepts
- Definition: t = (x̄-μ)/(s/√n) when σ unknown
- df = n-1
- p.d.f. formula
- v=1 special case → standard Cauchy distribution
- Symmetric about 0; more peaked than normal

### Definitions ⭐
- Student's t

## Section: Fisher's t 🟡
<!-- Reason: theoretical generalization; ratio of Z to √(χ²/n) -->

### Key Concepts
- t = T/√(χ²/n) where T~N(0,1) and χ² independent
- Derivation by Jacobian transformation → same as Student's t
- Student's t is special case of Fisher's t
- t_α,n approximation: large n → standard normal

## Section: F-Distribution (Snedecor's F) 🔴
<!-- Reason: ANOVA, variance ratio tests; widely used -->

### Key Concepts
- F = (X/n₁)/(Y/n₂) — ratio of two independent χ² over their df
- p.d.f. derivation
- Distribution depends only on df, not population parameters
- F is highly positively skewed
- F with n₁=1 is t² with df=n₂
- Reciprocal property: F_(1-α; n₁,n₂) = 1/F_(α; n₂,n₁) → tables only need upper α

### Definitions ⭐
- F-statistic
- Snedecor's F distribution

## Section: Sampling Distributions of Mean and Variance from Normal 🔴
<!-- Reason: Foundational result; underlies all subsequent tests -->

### Key Concepts
- Sample x₁,...,xₙ from N(μ,σ²)
- One-to-one orthogonal transformation x → y
- Result 1: x̄ ~ N(μ, σ²/n)
- Result 2: (n-1)s²/σ² ~ χ²(n-1)
- Result 3: x̄ and s² are independent

### Definitions ⭐
- Independence of x̄ and s² in normal sampling

<!-- Continues in chunk 005 -->
