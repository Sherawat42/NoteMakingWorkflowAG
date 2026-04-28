# Chunk 007 — Unit 30 Wrap-up + Worked MLE Examples + Unit 31 Hypothesis Testing Intro
<!-- Pages: 61-70 -->
<!-- Source: chunk_007.txt -->

## Section: Unit 30 — Key Words 🟢
<!-- See chunks 005, 006 for derivations of these terms -->

### Definitions (Glossary)
| Term | Definition |
|---|---|
| **Central Limit Theorem** ⭐ | iid sample mean is asymptotically normal |
| **Completeness** | Different distributions distinct under different parameter values; needed for MVUE uniqueness via sufficient statistic |
| **Cramer-Rao Inequality** ⭐ | Var(unbiased) ≥ {[ψ'(θ)]² / I(θ)} where I(θ) = E[(∂lnL/∂θ)²] — lower bound on variance |
| **Consistency** ⭐ | T_n →ᴾ τ(θ) (convergence in probability) |
| **Efficiency** ⭐ | Best estimator has smallest avar among consistent + asymptotically normal estimators |
| **Generalized Method of Moments** | Uses moment conditions instead of full distribution; more robust than ML |
| **Maximum Likelihood** ⭐ | Maximise L(θ) (or log-likelihood) to obtain MLE |
| **Minimum Variance Unbiased Estimator** ⭐ | Unbiased + smallest variance among all unbiased estimators |
| **Most Efficient Estimator** | Smallest sampling variance among rivals; E = V₁/V₂ ≤ 1 |
| **Parameter Space** ⭐ | Set Θ of all possible values of θ |
| **Partial Least Squares** | Estimation when many correlated regressors; uses PCA to reduce dimensionality |
| **Sufficiency** ⭐ | T captures all sample information about θ; conditional dist of sample given T is independent of θ |

---

## Section: Unit 30 — Worked Examples 🔴

### Examples — Check Your Progress 1

#### Q3: Is x̄ + (1/n)Σxᵢ² unbiased for μ² + 1?
- Given: X₁,…,Xₙ ~ N(μ, 1) (so Var(Xᵢ) = 1).
- E(Xᵢ²) = Var(Xᵢ) + [E(Xᵢ)]² = 1 + μ².
- E[x̄ + (1/n)·Σxᵢ²] = μ + (1/n)·Σ E(Xᵢ²) = μ + (1/n)·n(1 + μ²) = μ + 1 + μ². 

The text says the answer is *μ² + 1* (treating the estimator as (1/n)·Σxᵢ²), in which case E[(1/n)Σxᵢ²] = 1 + μ² — matching the target.

#### Q4: Best Linear Estimator from 5 Normal Samples
- Sample (X₁,…,X₅) of size 5 from N(μ, σ²) with unknown μ.
- Estimators:
  - t₁ = (X₁ + X₂ + X₃ + X₄ + X₅)/5
  - t₂ = (2X₁ + X₂ + λX₃)/3
- Unbiasedness: E(t₁) = μ; for t₂, E = (2μ + μ + λμ)/3 = μ requires (3+λ)/3 = 1 ⇒ λ = 0.
- Variances:
  - V(t₁) = (1/25)·5σ² = σ²/5
  - V(t₂) = (4σ² + σ²)/9 = 5σ²/9 (using λ = 0)
- Since V(t₁) = σ²/5 = 0.2σ² < V(t₂) = 5σ²/9 ≈ 0.556σ², **t₁ is the better (lower-variance) unbiased estimator**.

#### Q5: Sufficient Statistic for θ
- Sample x₁,…,xₙ from f(x, θ) = θx^(θ−1) for 0 < x < 1, θ > 0.
- Likelihood: L(x, θ) = ∏θxᵢ^(θ−1) = θⁿ·(∏xᵢ)^(θ−1).
- Set t₁ = ∏xᵢ. Then L = θⁿ·t₁^(θ−1) · 1 = g(t₁, θ)·h(x).
- By **Factorization Theorem**, **t₁ = ∏xᵢ is sufficient for θ**.

### Examples — Check Your Progress 2

#### Q3: MLE for biased coin (HHT)
- Likelihood: L(p) = P(HHT) = p²(1 − p).
- ℓ(p) = 2 ln p + ln(1 − p).
- dℓ/dp = 2/p − 1/(1 − p) = 0 ⇒ 2(1 − p) = p ⇒ **p̂_MLE = 2/3**.

#### Q4: MLE for power-family density
- Density: f(x|θ) = (θx^(θ−1))/2^θ on 0 ≤ x ≤ 2.
- Log-likelihood: ln L = Σ[ln θ + (θ − 1) ln xᵢ − θ ln 2] = n ln θ + (θ − 1)Σ ln xᵢ − nθ ln 2.
- ∂ ln L/∂θ = n/θ + Σ ln xᵢ − n ln 2 = 0
- ⇒ **θ̂_MLE = n / (n ln 2 − Σ ln xᵢ)**.

### Examples — Exercises (Q1–Q4)

#### Q1: Cauchy population
- f(x, θ) = (1/π)·1/(1 + (x − θ)²).
- L(x, θ) = (1/πⁿ)·∏ 1/(1 + (xᵢ − θ)²) — does **not** factor as g(t, θ)·h(x) with a single statistic t.
- Hence **no single sufficient statistic** for θ in Cauchy.
- The full sample (X₁,…,Xₙ) is jointly sufficient.

#### Q2: MLE of μ for normal — three baby weights
- Babies weigh 8, 9, 10 ounces.
- Maximise ∏ (1/(σ√(2π)))·exp[−(xᵢ − μ)²/(2σ²)].
- Log-likelihood: −3 ln(σ√(2π)) − (1/(2σ²))[(8−μ)² + (9−μ)² + (10−μ)²].
- ∂/∂μ: (1/σ²)·[(8−μ) + (9−μ) + (10−μ)] = 0 ⇒ **μ̂_MLE = (8+9+10)/3 = 9**.

#### Q3: Poisson MLE for sixes
- Counts: 14, 27, 25, 12. Likelihood = ∏ (λ^xᵢ·e^(−λ)/xᵢ!).
- log L = (Σxᵢ)·ln λ − nλ − Σ ln(xᵢ!).
- d/dλ = Σxᵢ/λ − n = 0 ⇒ **λ̂_MLE = (Σxᵢ)/n = (14 + 27 + 25 + 12)/4 = 78/4 = 19.5**.

#### Q4: MLE of normal mean is unbiased
- μ̂_MLE = (1/n)·ΣXᵢ = x̄.
- E(x̄) = (1/n)·Σ E(Xᵢ) = (1/n)·nμ = μ. **Unbiased**. ✓

> **Quick Recall:**
> - Coin HHT MLE: 2/3
> - Normal mean MLE = sample mean
> - Poisson λ MLE = sample mean
> - Cauchy: whole sample is sufficient (no single sufficient statistic)
> - For factorisation: L = g(t,θ)·h(x) ⇒ t sufficient

---

## Section: Unit 31 — Hypothesis Testing: Objectives and Introduction 🟢

### Core Idea
Unit 31 introduces **hypothesis testing** — the second arm of statistical inference (after estimation). Given hypothetical parameter values, the test of significance decides how plausible the hypothesis is in light of sample evidence. The unit covers the null/alternative framework, critical regions, confidence intervals, one-/two-tailed tests, P-values, Type I/II errors, power, and tests under normality.

### Unit 31 Stated Objectives
- form null and alternative hypotheses;
- determine the critical region and level of significance;
- specify confidence intervals and limits;
- calculate critical values for one-/two-tailed tests;
- distinguish Type I and Type II errors;
- identify the optimum test under different situations;
- compare two univariate normal distributions;
- solve hypothesis-testing problems.

---

## Section: Tests of Significance 🔴

### Core Idea
A test of significance decides whether the deviation between (i) an observed sample statistic and a hypothetical parameter, or (ii) two independent sample statistics, is significant or attributable to chance / sampling fluctuations. **Hypothesis testing is always about a population parameter, never about a sample statistic.**

### Key Concepts
- For large n, many distributions (binomial, Poisson, NB, hypergeometric, t, F, χ²) → approximated by normal → use **normal test of significance**.
- Common tests for *small* samples: t-test, F-test, Fisher's z-transformation.

> **Quick Recall:**
> - Hypothesis testing is about population parameters.
> - Large n → normal test; small n → t, F, z-transformation.

---

## Section: Null Hypothesis 🔴

### Core Idea
The **null hypothesis** H₀ is a definite hypothesis of "no difference" — the claim being tested for possible **rejection** under the assumption that it is true. It is denoted H₀. According to **R. A. Fisher**: "Null hypothesis is the hypothesis which is tested for possible rejection under the assumption that it is true."

### Key Concepts
- For a single statistic: H₀ asserts no significant difference between sample statistic and hypothetical parameter.
- For two-statistic comparison: H₀ asserts no significant difference between the two statistics.
- We compute P that the observed deviation occurred due to sampling fluctuations.
- Significant deviation → **reject H₀** at chosen level.
- Non-significant deviation → H₀ may be **retained**.

### Definitions
- **Null Hypothesis (H₀)** ⭐: hypothesis of no difference, tested for rejection under the assumption that it is true (Fisher).

> **Quick Recall:**
> - H₀ = no-difference hypothesis.
> - Tested *for rejection*.
> - Default belief unless evidence is strong against it.

---

## Section: Alternative Hypothesis 🔴

### Core Idea
The **alternative hypothesis** H₁ is any hypothesis complementary to H₀. There are three standard structures: two-tailed, right-tailed, left-tailed. The structure of H₁ determines whether the test is one-tailed or two-tailed.

### Key Concepts
| Test | H₀ | H₁ | Tail |
|---|---|---|---|
| Two-tailed | μ = μ₀ | μ ≠ μ₀ | Both tails |
| Right-tailed | μ ≤ μ₀ | μ > μ₀ | Right |
| Left-tailed | μ ≥ μ₀ | μ < μ₀ | Left |

### Definitions
- **Alternative Hypothesis (H₁)** ⭐: any hypothesis complementary to H₀.

> **Quick Recall:**
> - Two-tailed: ≠
> - Right-tailed: >
> - Left-tailed: <
> - Set H₁ first; it determines test type.

---

## Section: Critical Region and Level of Significance 🔴

### Core Idea
The **critical region** ω is the subset of the sample space where H₀ is rejected. Its complement ω′ is the **acceptance region**. The probability that a random value of the test statistic falls in ω is the **level of significance α** — also called the size of the Type I error or the producer's risk. Conventional values are 5% and 1%; α is fixed *before* sample collection.

### Key Concepts
- Sample space S = ω ∪ ω′; ω ∩ ω′ = ∅.
- P[t ∈ ω | H₀] = α.
- α = level of significance = size of Type I error = "producer's risk".
- 5% and 1% are most common.
- α must be fixed in advance (before drawing data).

### Definitions
- **Critical Region (ω)** ⭐: subset of sample space leading to rejection of H₀.
- **Level of Significance (α)** ⭐: probability that the statistic lands in the critical region under H₀.

> **Quick Recall:**
> - Critical region = "reject" zone.
> - α = size of Type I error = level of significance.
> - α fixed in advance.

---

## Section: Confidence Interval and Confidence Limits 🔴

### Core Idea
**Neyman's confidence-interval technique**: choose a small α (5% or 1%); find statistics c₁, c₂ such that P[c₁ < θ < c₂] = 1 − α. Then [c₁, c₂] is the **confidence interval**, c₁ and c₂ are the **confidence limits**, and (1 − α) is the **confidence coefficient**.

### Mechanisms / Processes

For finding c₁ and c₂:
- Let T₁, T₂ be statistics with P(T₁ > θ) = ω₁ and P(T₂ > θ) = ω₂ (constants independent of θ).
- Then P(T₁ < θ < T₂) = 1 − α where α = ω₁ + ω₂.
- T₁ and T₂ serve as c₁ and c₂.

### Examples

#### Worked: 95% CI for Normal Mean (σ Known)
- Z = (x̄ − μ)/(σ/√n) ~ N(0, 1).
- P(−1.96 < Z < 1.96) = 0.95.
- Rearranging: P(x̄ − 1.96·σ/√n < μ < x̄ + 1.96·σ/√n) = 0.95.
- 95% confidence limits: x̄ ± 1.96·(σ/√n).
- 95% confidence interval: [x̄ − 1.96·σ/√n, x̄ + 1.96·σ/√n].

### Definitions
- **Confidence Interval [c₁, c₂]** ⭐: interval expected to contain the unknown parameter at level (1−α).
- **Confidence Limits (c₁, c₂)** ⭐: endpoints of the CI.
- **Confidence Coefficient (1 − α)** ⭐: e.g., 0.95 or 0.99.

> **Quick Recall:**
> - 95% CI for normal mean: x̄ ± 1.96·σ/√n
> - 99% CI: x̄ ± 2.58·σ/√n
> - Confidence coefficient = 1 − α
> - α = level of significance

---

## Section: One-Tailed and Two-Tailed Tests 🔴

### Core Idea
The choice between one-tailed and two-tailed tests is dictated entirely by the alternative hypothesis. If H₁ is one-tailed (right or left), use a single-tailed test; if H₁ is two-tailed, use a two-tailed test.

### Key Concepts
- **Two-tailed**: critical region split between both tails (e.g., for H₁: μ ≠ μ₀).
- **Right-tailed**: critical region in right tail only (e.g., for H₁: μ > μ₀).
- **Left-tailed**: critical region in left tail only (e.g., for H₁: μ < μ₀).

### Examples

#### Bulb Comparison
- Two brands; mean lives μ₁ (standard process), μ₂ (new technique).
- Test if bulbs differ → H₀: μ₁ = μ₂; H₁: μ₁ ≠ μ₂ → **two-tailed**.
- Test if new ones live longer → H₀: μ₁ = μ₂; H₁: μ₁ < μ₂ → **left-tailed** (text frames it from standard's POV).
- Test if new ones inferior → H₀: μ₁ = μ₂; H₁: μ₁ > μ₂ → **right-tailed**.

> **Quick Recall:**
> - H₁ direction → tail direction
> - ≠ → two-tailed; > → right-tailed; < → left-tailed.

---

## Section: Critical Values / Significant Values 🔴

### Core Idea
The **critical value** (or significant value) of the test statistic is the value separating the critical and acceptance regions. It depends on (i) level of significance α and (ii) tail structure of H₁. For large samples, the standardised test statistic Z is asymptotically standard normal under H₀, with critical values from normal probability tables. (Continues into Chunk 008 with the values table.)

### Key Concepts
- Z = (observed value − expected value)/(standard error) = (t − E(t))/SE(t).
- Z ~ N(0, 1) approximately for large n.
- For two-tailed at level α: P[|Z| > z_α] = α ⇒ each tail has area α/2.
- For right-tailed at level α: P[Z > z_α] = α.
- For left-tailed at level α: P[Z < −z_α] = α.

> **Quick Recall:**
> - Two-tailed at α ↔ one-tailed at α/2 (in tail areas)
> - Critical value depends on α and tail type.

<!-- Continues in chunk 008 -->
