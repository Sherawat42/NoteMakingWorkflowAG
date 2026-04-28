# Chunk 007 — Estimation Wrap-up, Worked Examples, Unit 31 Hypothesis Testing Intro
<!-- Pages: 61-70 -->
<!-- Continues from: Unit 30 methods of estimation (Chunk 006) -->
<!-- Continues into: Unit 31 P-value method, Type I/II errors, normality testing (Chunk 008) -->

## Section: Unit 30 — Key Words 🟢
<!-- Reason: glossary -->

### Definitions ⭐
- Central Limit Theorem ⭐
- Completeness
- Cramer-Rao Inequality ⭐
- Consistency ⭐
- Efficiency ⭐
- Generalized Method of Moments
- Maximum Likelihood ⭐
- Minimum Variance Unbiased Estimator ⭐
- Most Efficient Estimator
- Parameter Space ⭐
- Partial Least Squares
- Sufficiency ⭐

## Section: Unit 30 — Worked Examples (Answers/Hints + Exercises) 🔴
<!-- Reason: typical exam-style problems -->

### Examples
- CYP1 Q3: Show x̄ + (1/n)Σxᵢ² is unbiased for μ²+1 (E(xᵢ²)=μ²+1 since Var=1)
- CYP1 Q4: Best linear estimator from 5 normal samples → t₁ has lowest variance
- CYP1 Q5: t = ∏xᵢ sufficient for θ (factorization)
- CYP2 Q3: MLE for biased coin (HHT) → p̂ = 2/3
- CYP2 Q4: MLE for power-family density → θ̂_MLE = n/(n·ln2 − Σlnxᵢ)
- Q1: Cauchy population — no single sufficient statistic; whole sample jointly sufficient
- Q2: MLE of μ for normal with babies (8,9,10)
- Q3: Poisson MLE for sixes per match
- Q4: MLE for normal mean = x̄ is unbiased

## Section: Unit 31 Hypothesis Testing — Objectives & Introduction 🟢
<!-- Reason: orienting -->

### Key Concepts
- Test of hypothesis / test of significance

## Section: Tests of Significance — Null Hypothesis 🔴
<!-- Reason: foundational; Fisher's definition -->

### Key Concepts
- H₀ — hypothesis of "no difference"
- Tested for possible rejection
- Compute probability P of deviation under H₀
- Significant deviation → reject H₀

### Definitions ⭐
- Null Hypothesis ⭐ (Fisher's definition)

## Section: Alternative Hypothesis 🔴
<!-- Reason: 3 types — two-tailed, right-tailed, left-tailed -->

### Key Concepts
- Two-tailed: H₁: μ ≠ μ₀
- Right-tailed: H₁: μ > μ₀
- Left-tailed: H₁: μ < μ₀
- Determines test type (single vs two-tailed)

### Definitions ⭐
- Alternative Hypothesis ⭐

## Section: Critical Region and Level of Significance 🔴
<!-- Reason: vocabulary; α; CYP question -->

### Key Concepts
- Critical region ω in sample space → rejection region
- P[t ∈ ω | H₀] = α
- α = level of significance = size of Type I error = "producer's risk"
- Conventional values: 5% and 1%
- Fixed in advance

### Definitions ⭐
- Critical Region ⭐
- Level of Significance ⭐

## Section: Confidence Interval and Confidence Limits 🔴
<!-- Reason: Neyman's technique; widely tested -->

### Key Concepts
- P[c₁ < θ < c₂] = 1 − α
- (1 − α) = confidence coefficient
- Construction via T₁, T₂ statistics
- Worked example: x̄ ± 1.96·σ/√n is 95% CI for normal mean

### Definitions ⭐
- Confidence Interval ⭐
- Confidence Limits ⭐
- Confidence coefficient

## Section: One-Tailed and Two-Tailed Tests 🔴
<!-- Reason: choice based on alternative; CYP question -->

### Key Concepts
- Determined by alternative hypothesis
- Critical region position depends on tail
- Bulb example: testing if new bulbs differ vs. inferior

## Section: Critical Values / Significant Values 🔴
<!-- Reason: tabulated z values -->

### Key Concepts
- Z = (t − E(t))/SE(t) under H₀
- Two-tailed at α equivalent to one-tailed at α/2 by area
- Notes preview Table 31.1 (continues in chunk 008)

<!-- Continues in chunk 008 -->
