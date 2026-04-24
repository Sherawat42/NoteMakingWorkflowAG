# Chunk 008 — Evaluation of Multiple Regression: Wald, LM & Likelihood Ratio Tests
<!-- Pages: 69–77 -->
<!-- Source: chunk_008.txt -->
<!-- See chunk 007 for setup of linear restrictions Rβ = q -->

## Section: Wald Test for Linear Restrictions 🔴
<!-- Continues from: Linear Restrictions (Chunk 007) -->

### Core Idea
The **Wald test** tests whether J linear restrictions **Rβ = q** are satisfied. It is based on the idea that if the restrictions are true, the unrestricted OLS estimates (Rb) should be approximately equal to q. The Wald statistic follows a χ²(J) distribution. Its **key advantage**: requires estimation of the **unrestricted model only** — no restricted model needed.

> **In Simple Terms:** The Wald test says: "If the restrictions are true, my unrestricted estimates should roughly satisfy them. How far off are they?" Large distance → reject the restrictions.

### Key Concepts

#### Wald Statistic Formula
Distribution result: **Rb ~ N(Rβ, σ²·R(X'X)⁻¹R')** ... (7.24)

Under H₀: Rβ = q, the quadratic form:

**ξ = (Rb − q)' [R(X'X)⁻¹R']⁻¹ (Rb − q) / σ² ~ χ²(J)** ... (7.25)

Replacing unknown σ² with estimate s² → **Wald statistic W**.

#### Based on Unrestricted Model Only
The Wald test estimates only the **unrestricted model** (full model with all k parameters).

From the unrestricted estimates b, we compute Rb and check how far it is from q.

No need to estimate the restricted model — this is the **main computational advantage** of the Wald test.

#### Wald Test vs t-Test
| Feature | t-Test | Wald Test |
|---------|--------|-----------|
| Number of restrictions | 1 | J ≥ 1 |
| What it tests | βₖ = 0 | Rβ = q |
| Model required | Unrestricted | Unrestricted only |
| Distribution | t(n−k) | χ²(J) |

Special case: For J = 1 restriction, Wald test is equivalent to t²-test.

### Definitions
- **Wald test**: Tests J linear restrictions Rβ = q using unrestricted model estimates only; W ~ χ²(J). ⭐ (exam-important)
- **Wald statistic W**: W = (Rb − q)'[R(X'X)⁻¹R']⁻¹(Rb − q)/s²; measures distance of Rb from q.

### ⚠️ Common Mistakes
- ❌ Mistake: Wald test requires restricted model → ✅ Correct: Only **unrestricted** model needed; this distinguishes Wald from LR test.

> **Quick Recall:**
> - Wald: unrestricted model only
> - Tests Rβ = q; W ~ χ²(J)
> - Logic: if H₀ is true, Rb ≈ q; large W → reject H₀
> - Advantage: no restricted model estimation needed

### Connections
- Builds on: Linear restrictions Rβ = q (Chunk 007)
- Contrasts with: LM test (restricted only) and LR test (both)
- CYP 3 Q2: Define Wald test

---

## Section: Lagrange Multiplier (LM) Test 🔴

### Core Idea
The **LM test** (also called the Score test) tests restrictions by checking whether the **score function** (derivative of the log-likelihood) is significantly different from zero at the **restricted** estimates. Its key feature: requires estimation of the **restricted model only**. Large LM → the restricted estimates are far from the unconstrained optimum → reject H₀.

> **In Simple Terms:** The LM test says: "If the restrictions are wrong, then at the restricted estimates, we're not at the log-likelihood maximum — the 'slope' of the likelihood will be non-zero." Large slope at the restricted point → reject H₀.

### Key Concepts

#### LM Test Logic — Score Test
Score function: **q(θ) = ∂L(θ)/∂θ** ... (7.26)

Information matrix: **I(θ) = −E[∂²L(θ)/∂θ∂θ']** ... (7.27)

Lagrangian (restricted MLE): **ℒ = L(θ) − λ'h(θ)** ... (7.28)

First-order conditions at restricted estimates θ̃: q(θ̃) − H(θ̃)λ̃ = 0

**LM statistic: LM = q̃'Ĩ⁻¹q̃ = λ̃'H̃'Ĩ⁻¹H̃λ̃** ... (7.29)

Under H₀, **LM ~ χ²(k−r)** where r = number of restrictions.

Large values of q̃ (score at restricted point) and λ̃ (Lagrange multipliers) → reject H₀.

#### Based on Restricted Model Only
Unlike the Wald test (unrestricted) and LR test (both):
- LM test requires only the **restricted parameter estimates θ̃**
- At the unrestricted MLE, q(θ̂ᵤ) = 0 by definition; at restricted MLE, q(θ̃) ≠ 0 unless restriction is true

### Definitions
- **Lagrange Multiplier (LM) test**: Score test based on restricted model only; tests if the score at restricted estimates is significantly non-zero; LM ~ χ²(J) under H₀. ⭐ (exam-important)
- **Score function q(θ)**: ∂L(θ)/∂θ; gradient of log-likelihood; = 0 at unconstrained MLE; ≠ 0 at restricted MLE if restrictions are wrong.

### ⚠️ Common Mistakes
- ❌ Mistake: LM test requires both models → ✅ Correct: LM requires only the **restricted model** (contrast with LR which needs both).

> **Quick Recall:**
> - LM: restricted model only
> - Tests if score ≠ 0 at restricted estimates
> - LM ~ χ²(J) under H₀
> - Equivalent to: "Are the Lagrange multipliers significantly different from zero?"

### Connections
- Contrasts with: Wald (unrestricted only), LR (both models)
- CYP 3 Q3: Compare Wald and LM model requirements

---

## Section: Likelihood Ratio (LR) Test 🔴

### Core Idea
The **LR test** compares the **log-likelihood values** of the restricted and unrestricted models. If the restrictions are valid, imposing them should not substantially reduce the likelihood — the difference should be small. Large difference → restrictions are invalid → reject H₀. Requires **both** the restricted and unrestricted models to be estimated.

> **In Simple Terms:** The LR test asks: "How much did we lose in 'fit' by imposing these restrictions?" Big loss → the restrictions are probably wrong.

### Key Concepts

#### LR Statistic Formula
Unrestricted MLE: θ̂ᵤ (all parameters free)
Restricted MLE: θ̂ᴿ (restrictions H₀ imposed)

**LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)] ~ χ²(J)** ... (7.30)

Under H₀, LR follows chi-square distribution with J degrees of freedom (J = number of restrictions).

Note: LR = −2 ln λ where λ = L(θ̂ᴿ)/L(θ̂ᵤ) ≤ 1 (restricted can never exceed unrestricted likelihood).

#### Requires Both Restricted and Unrestricted Models
Both θ̂ᵤ and θ̂ᴿ must be estimated by maximum likelihood.

LR tests whether adding new variables improves the model's explaining capacity.

#### Degrees of Freedom = Number of Restrictions
df = J = number of restrictions imposed under H₀.

**Limitation 1:** Cannot test simple null hypothesis against alternative (df would be 0).

**Limitation 2:** Cannot test one distributional assumption against another — likelihood functions of different distributions are unrelated (unrelated functional forms).

### Definitions
- **Likelihood Ratio (LR) test**: Tests J restrictions by comparing log-likelihood of unrestricted vs restricted model; LR ~ χ²(J). ⭐ (exam-important)
- **LR statistic**: LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)]; always ≥ 0 since restricted likelihood ≤ unrestricted.

### ⚠️ Common Mistakes
- ❌ Mistake: LR requires only one model → ✅ Correct: LR requires **both** restricted and unrestricted MLE estimates.
- ❌ Mistake: df for LR = number of parameters → ✅ Correct: df = **number of restrictions** J, not total parameters.

> **Quick Recall:**
> - LR: both models needed (unrestricted AND restricted)
> - LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)] ~ χ²(J)
> - df = number of restrictions J
> - Cannot test simple H₀ vs H₁ (df would be 0)
> - Tests whether new variables improve log-likelihood

### Connections
- Contrasts with: Wald (unrestricted only), LM (restricted only)
- CYP 3 Q4 & Q5: Define LR test and why df = J

---

## Section: Comparison — Wald, LM, LR Tests 🔴

### Core Idea
All three tests — Wald, LM, and LR — test the same null hypothesis H₀: Rβ = q (J restrictions) and are **asymptotically equivalent** (give same result in large samples). They differ in which model(s) they require to be estimated, making them computationally interchangeable depending on context.

> **In Simple Terms:** Three different paths to the same destination. Choose the one that's easiest to compute given what you've already estimated.

### Key Concepts

#### Which Model Each Test Requires

| Test | Model Required | Statistic | Distribution |
|------|---------------|-----------|-------------|
| **Wald** | Unrestricted only | W = (Rb−q)'[R(X'X)⁻¹R']⁻¹(Rb−q)/s² | χ²(J) |
| **LM** | Restricted only | LM = q̃'Ĩ⁻¹q̃ | χ²(J) |
| **LR** | Both models | LR = 2[ln L(θ̂ᵤ) − ln L(θ̂ᴿ)] | χ²(J) |

Memory aid:
- **W**ald → needs the **W**hole (unrestricted) model
- **LM** → needs the **L**imited (restricted) model only
- **LR** → needs **L**eft and **R**ight (both) models

#### Asymptotic Equivalence
All three tests are **asymptotically equivalent**: as n → ∞, they yield the same test decision. For finite samples, they may differ.

### Empirical Example (from source — CEO salary model)
Model: ln(salary) = β₁ + β₂(sales) + β₃(roe) + β₄(ros) + u
n = 209; R² = 0.2826; R̄² = 0.2721

t-tests:
- t(sales) = 0.2803/0.0353 = **7.94** → |t| > 1.96 → **significant**
- t(roe) = 0.0174/0.0041 = **4.25** → |t| > 1.96 → **significant**
- t(ros) = 0.0002/0.0005 = **0.44** → |t| < 1.96 → **not significant**

F-test (H₀: β₂ = β₃ = β₄ = 0):
F = [R²/(k−1)] / [(1−R²)/(n−k)] = [0.2826/3] / [(0.7174/205)] = **26.91**
→ p-value ≈ 0 → reject H₀ → model is jointly significant.

### ⚠️ Common Mistakes
- ❌ Mistake: The three tests always give the same result in finite samples → ✅ Correct: They are equivalent only asymptotically; finite sample results may differ.

> **Quick Recall:**
> - All three test H₀: Rβ = q; all ~ χ²(J)
> - Wald: unrestricted only | LM: restricted only | LR: both
> - Asymptotically equivalent for large n
> - In practice: use whichever model is easier to estimate
> - CEO salary: sales and roe significant; ros not significant; model overall significant (F = 26.91)

### Connections
- Builds on: All of Unit 7 (t-test, F-test, linear restrictions)
- This completes Unit 7 and Block 2

### Open Questions (from CYP 3)
1. Q1: t-test covers single restriction; need Wald/LM/LR for multiple (e.g. β₂ + β₃ = 1 in Cobb-Douglas).
2. Q2: Wald test based on unrestricted estimates; advantage = no restricted model needed.
3. Q3: LM requires restricted model only (contrast with Wald requiring unrestricted).
4. Q4: LR tests whether new variables improve log-likelihood; requires both models.
5. Q5: LR df = number of restrictions (parameters reduced by restrictions).
