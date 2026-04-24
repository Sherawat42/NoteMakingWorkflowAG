# Chunk 006 — Multiple Regression: Properties of OLS Estimators & Gauss-Markov Theorem
<!-- Pages: 50–58 -->
<!-- Source: chunk_006.txt -->
<!-- See chunk 005 for OLS derivation -->

## Section: Properties of OLS Estimators — Unbiasedness, Consistency & Efficiency 🔴
<!-- Continues from: OLS Estimation in Matrix Form (Chunk 005) -->

### Core Idea
The OLS estimator β̂ = (X'X)⁻¹X'Y has three key statistical properties: it is **unbiased** (E(β̂) = β), **consistent** (converges to β as n → ∞), and **efficient** (minimum variance among linear unbiased estimators). The variance-covariance matrix is **var(β̂) = σ²(X'X)⁻¹**. The unbiased estimator of error variance is **σ̂² = RSS/(n−k)**.

> **In Simple Terms:** The matrix OLS formula gives estimates that are correct on average (unbiased), become more accurate with more data (consistent), and have the least possible spread (efficient = BLUE).

### Key Concepts

#### Unbiasedness of β̂
From β̂ = (X'X)⁻¹X'Y = (X'X)⁻¹X'(Xβ + U) = β + (X'X)⁻¹X'U ... (6.18)

**E(β̂) = β + (X'X)⁻¹X'·E(U) = β + 0 = β** ... (6.19)

Since X is non-stochastic (fixed in repeated samples) and E(U) = 0 by Assumption 1.
→ OLS estimators are **unbiased**. ✓

#### Variance-Covariance Matrix of β̂
β̂ − β = (X'X)⁻¹X'U (from 6.18)

var(β̂) = E[(β̂ − β)(β̂ − β)']
= (X'X)⁻¹X' · E(UU') · X(X'X)⁻¹
= (X'X)⁻¹X' · σ²I · X(X'X)⁻¹
= **σ²(X'X)⁻¹** ... (6.21) ⭐

This is a (k×k) symmetric matrix:
- Diagonal elements: var(β̂ₖ) for each coefficient
- Off-diagonal elements: cov(β̂ᵢ, β̂ⱼ) between pairs of coefficients

#### Estimator of Error Variance σ̂² (Unbiased)
Residual vector: **Û = MY** where **M = I − X(X'X)⁻¹X'** (idempotent matrix)

Key properties of M:
- M' = M (symmetric)
- MM = M (idempotent)
- MX = 0 → so Û = MU (not MXβ)

Taking E(Û'Û):
E(Û'Û) = E(U'MU) = σ²·Tr(M) = σ²·Tr(I − X(X'X)⁻¹X') = σ²(n − k)

Therefore, unbiased estimator:
**σ̂² = RSS/(n−k) = Û'Û/(n−k)** ... (6.26)

Degrees of freedom = **n − k** for multiple regression (k parameters estimated).
For bivariate regression: k = 2 → σ̂² = RSS/(n−2) ← confirms result from Chunk 002.

### Definitions
- **Unbiased estimator**: E(β̂) = β; OLS estimator is unbiased under CLRM. ⭐ (exam-important)
- **Consistent estimator**: β̂ converges in probability to β as n → ∞. ⭐ (exam-important)
- **Asymptotic properties**: Properties of estimators as n → ∞; consistency is an asymptotic property.
- **Idempotent matrix M**: M = I − X(X'X)⁻¹X'; satisfies MM = M; used to express residuals.

### ⚠️ Common Mistakes
- ❌ Mistake: Degrees of freedom for multiple regression = n−2 → ✅ Correct: df = n−k (k = total parameters including intercept).
- ❌ Mistake: var(β̂) = σ² (scalar) → ✅ Correct: var(β̂) = **σ²(X'X)⁻¹** (a k×k matrix).

> **Quick Recall:**
> - E(β̂) = β → unbiased (uses E(U) = 0 and X non-stochastic)
> - var(β̂) = σ²(X'X)⁻¹ → k×k variance-covariance matrix
> - σ̂² = RSS/(n−k) → unbiased estimator of σ²
> - df = n−k for multiple regression
> - CYP 1 Q3: Derive var(β̂) = σ²(X'X)⁻¹

### Connections
- Builds on: OLS formula β̂ = (X'X)⁻¹X'Y (Chunk 005)
- Used in: Gauss-Markov proof (this chunk)

---

## Section: Algebraic Properties of Multiple Regression OLS 🟡

### Core Idea
OLS estimators in the multiple regression context have algebraic properties analogous to bivariate regression: residuals are uncorrelated with fitted values, and the regression hyperplane passes through the sample means.

### Key Concepts
- **Û'Ŷ = 0**: Residuals and fitted values are uncorrelated. (CYP2 Q1)
- **Û'X = 0**: Residuals and all explanatory variables are uncorrelated.
- Regression hyperplane passes through mean values (X̄₂, X̄₃, …, X̄ₖ, Ȳ).

### Connections
- Parallel to bivariate algebraic properties (Chunk 002)

---

## Section: Gauss-Markov Theorem — OLS is BLUE 🔴

### Core Idea
The **Gauss-Markov Theorem** proves that under CLRM assumptions, OLS is **BLUE** — the Best Linear Unbiased Estimator. Any other linear unbiased estimator β̃ has a variance-covariance matrix that is **at least as large** as σ²(X'X)⁻¹. The proof uses the positive semi-definite property of DD'.

> **In Simple Terms:** No matter what other "fair" and "straight-line" method you try, OLS will always give you estimates with the smallest possible variance. It's the most efficient estimator in its class.

### Key Concepts

#### Setup: Any Linear Unbiased Estimator β̃ = CY
Let β̃ be any alternative linear estimator: **β̃ = CY** ... (6.29)

where C is a (k×n) matrix (different from OLS's (X'X)⁻¹X').

Substituting Y = Xβ + U:
**β̃ = CXβ + CU** ... (6.31)

#### Condition for Unbiasedness: CX = I ... (6.34)
E(β̃) = CXβ (since E(U) = 0)

For β̃ to be unbiased: **CX = I** (the identity matrix) ... (6.34)

#### Variance of β̃
var(β̃) = E[(β̃ − β)(β̃ − β)'] = E[CUU'C'] = C·E(UU')·C' = σ²CC' ... (6.37)

#### Comparing var(β̂) and var(β̃) — The Key Step
Write C = (X'X)⁻¹X' + D, where D is a (k×n) matrix ... (6.38)

From CX = I: DX = 0 ... (6.39)

Then:
CC' = [(X'X)⁻¹X' + D][X(X'X)⁻¹ + D']
= (X'X)⁻¹X'X(X'X)⁻¹ + DX(X'X)⁻¹ + (X'X)⁻¹X'D' + DD'
= (X'X)⁻¹ + 0 + 0 + DD'    [using DX = 0]

So: **CC' = (X'X)⁻¹ + DD'** ... (6.40)

Therefore: **var(β̃) = σ²CC' = σ²(X'X)⁻¹ + σ²DD'**

Since **DD' is positive semi-definite** (i.e., DD' ≥ 0):
**var(β̃) ≥ var(β̂)** ... (6.41)

→ OLS has the minimum variance among all linear unbiased estimators. ✓

**BLUE Conclusion:** β̂ = (X'X)⁻¹X'Y is the **Best Linear Unbiased Estimator**.

### Definitions
- **BLUE (Best Linear Unbiased Estimator)**: Among all linear unbiased estimators, OLS has the smallest variance-covariance matrix. ⭐ (exam-important)
- **Gauss-Markov Theorem**: Under CLRM assumptions, OLS is BLUE; does NOT require normality of errors. ⭐ (exam-important)
- **Positive semi-definite matrix**: A matrix A where x'Ax ≥ 0 for all x; ensures var(β̃) ≥ var(β̂).

### Mechanisms / Processes
**BLUE Proof Roadmap:**
1. Assume any linear unbiased estimator β̃ = CY with CX = I
2. Write C = (X'X)⁻¹X' + D where DX = 0
3. Compute CC' = (X'X)⁻¹ + DD'
4. var(β̃) = σ²CC' = σ²(X'X)⁻¹ + σ²DD'
5. Since DD' ≥ 0 (positive semi-definite): var(β̃) ≥ var(β̂) ✓

### ⚠️ Common Mistakes
- ❌ Mistake: Gauss-Markov requires normality → ✅ Correct: No distributional assumption needed; only CLRM assumptions required.
- ❌ Mistake: OLS is BLUE even with heteroscedasticity → ✅ Correct: Violation of E(UU') = σ²I breaks the BLUE property; GLS becomes better.

> **Quick Recall:**
> - Gauss-Markov: OLS is BLUE under CLRM (no normality needed)
> - Proof: var(β̃) − var(β̂) = σ²DD' ≥ 0 (positive semi-definite)
> - BLUE: Best (minimum var) + Linear + Unbiased + Estimator
> - Breaks down if: heteroscedasticity, autocorrelation, endogeneity

### Connections
- Bivariate version: Gauss-Markov via Lagrangian (Chunk 002)
- Matrix version extends to k variables (this chunk)
- CYP 2 Q2 & Q3 ask to prove OLS is BLUE and show properties
- This completes Unit 6
