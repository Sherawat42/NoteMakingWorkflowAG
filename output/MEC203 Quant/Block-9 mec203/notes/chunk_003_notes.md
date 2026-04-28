# Chunk 003 — Sample Proportion SE, Unit 28 Wrap-up, Unit 29 Chi-square Distribution
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

## Section: Expectation and Standard Error of Sample Proportion 🔴
<!-- See chunk 002 for the parallel treatment of sample mean -->

### Core Idea
The expectation and standard error of the sample proportion p̂ = f/n are obtained from the sample-mean results by substituting:
- x → f/n (sample proportion p̂),
- μ → P (population proportion),
- σ² → PQ (Bernoulli variance, where Q = 1 − P).

This yields E(p̂) = P (unbiased) in both replacement schemes, and SE forms that match the sample-mean structure with PQ instead of σ².

### Mechanisms / Processes

Substituting in formulas derived in chunk 002:

#### With Replacement
- E(f/n) = P → p̂ is unbiased.
- σ_p̂ = √(PQ/n)

#### Without Replacement (Finite Population Correction)
- E(f/n) = P (still unbiased).
- σ_p̂ = √(PQ/n) · √[(N − n)/(N − 1)]

### Definitions
- **Sample proportion (p̂)**: f/n, the fraction of the sample with the attribute of interest. ⭐ (exam-important)
- **Finite Population Correction (FPC)**: the factor √[(N − n)/(N − 1)] applied when sampling without replacement from a finite population. ⭐ (exam-important)

> **Quick Recall:**
> - σ_p̂ = √(PQ/n) (with replacement)
> - σ_p̂ = √(PQ/n)·√[(N−n)/(N−1)] (without replacement, finite population)
> - FPC ≈ 1 when n ≪ N

### Connections
- Builds on: SE of sample mean derivation (Chunk 002).
- Used in: pineapple defective example (worked exercise below).

---

## Section: Unit 28 — Let Us Sum Up + Key Words 🟢

### Core Idea
Unit 28 covered: sample survey concepts, advantages, sample design, biases, types of sampling (probability and non-probability), parameter vs. statistic distinction, sampling distribution, standard error, and expectations/standard errors of x̄ and p̂.

### Definitions (Glossary)
| Term | Definition |
|---|---|
| **Cluster Sampling** ⭐ | Population divided into clusters, ideally heterogeneous within and homogeneous between |
| **Quota Sampling** | Representative sample by specifying quotas on age, gender, social class etc. |
| **Population** | Aggregate of objects, animate or inanimate, under study; finite or infinite |
| **Purposive Sampling** | Sampling units selected with a definite purpose in view |
| **Random Sampling** ⭐ | Each unit of population has known probability of inclusion |
| **Sample** | Finite subset of statistical individuals; sample size = number in the sample |
| **Sampling Distribution** ⭐ | Probability distribution of all possible values of a sample statistic |
| **Sampling Without Replacement** | Once selected, an element cannot reappear |
| **Sampling With Replacement** | Selected element returns to population; can be selected again |
| **Standard Error** ⭐ | Standard deviation of the sampling distribution of a statistic |
| **Stratified Sampling** ⭐ | Population divided into homogeneous groups (strata); SRS within each |
| **Unbiased** ⭐ | Property: E(estimator) = parameter |

---

## Section: Unit 28 — Worked Exercises 🔴

### Examples

#### Example: Defective Pineapples
- Sample n = 500 pineapples; 65 found defective.
- Sample proportion: p̂ = 65/500 = 0.13.
- SE = √(p̂(1−p̂)/n) = √(0.13·0.87/500) = **0.022**.
- 95% CI: p̂ ± 1.96·SE = 0.13 ± 1.96·0.022 = **[0.086, 0.174]**, i.e., 8.6% to 17.4%.
- Conclusion: with 95% confidence, the true defective rate lies between 8.6% and 17.4%.

#### Example: Sample Mean from Population
- N is large; population μ = 100, σ = 20; sample size n = 225.
- Sample mean has μ_x̄ = 100, σ_x̄ = 20/√225 = **1.33**.

#### Example: Probability that |x̄ − μ| < 0.5 day
- Mean germination time μ = 22, σ = 2.3, sample size n = 160.
- Required: P(|x̄ − μ| < 0.5) = **0.9940**.

#### Example: Vehicle Speeds
- Speeds are N(36.6, 1.7²).
- (a) P(35 < X < 40) = **0.8036** (single observation).
- (b) For sample of n = 20, P(35 < x̄ < 40) ≈ **1.0000**.

#### Example: Marriage Duration
- μ = 7.8 years, σ = 1.2 years, n = 75.
- Required probability ≈ **0.9251**.

> **Quick Recall:**
> - For proportion CI: p̂ ± z_(α/2) · √(p̂(1−p̂)/n)
> - 95% z = 1.96; 99% z = 2.58
> - Sample-mean CI: x̄ ± z·σ/√n

---

## Section: Unit 29 — Sampling Distributions: Objectives and Introduction 🟢

### Core Idea
Unit 29 develops the theoretical machinery — chi-square (χ²), t, and F distributions, plus the central limit theorem — that underpins inferential procedures. For finite samples, assigning probabilities to each possible sample is straightforward; for large or infinite samples, we must theoretically derive the sampling distribution from the population distribution.

### Unit 29 Stated Objectives
- discuss the concept of sampling distribution of a statistic;
- enlist properties of different sampling distributions;
- derive results using **Jacobian transformation**;
- measure goodness of fit using χ² test;
- analyse non-randomly distributed samples (CLT).

---

## Section: Concept of Sampling Distribution of a Statistic 🟡
<!-- See chunk 002 for first introduction; this section deepens the definition -->

### Core Idea
For a finite population of size N, with sample size n, there are k = ᴺCₙ distinct samples; each sample mean occurs with the same probability, so we can tabulate the sampling distribution. For very large N, the limiting form of the relative frequency distribution (over infinitely many samples) defines the sampling distribution. When the population follows a theoretical distribution (binomial, normal), the sampling distribution can be derived analytically — this is critical for **confidence limits** and **hypothesis testing**.

### Key Concepts
- Discrete (small N): tabulate probability of each x̄ value across all ᴺCₙ samples.
- Large N: take limiting form of the relative frequency distribution as number of samples → ∞.
- Theoretical population (e.g., normal): derive sampling distribution analytically.
- Sampling distribution → enables confidence limits + hypothesis tests.

> **Quick Recall:**
> - Knowledge of sampling distribution = key to both estimation and hypothesis testing.
> - For finite population, count is ᴺCₙ.

---

## Section: Three Fundamental Distributions Derived from Normal — Chi-square 🔴

### Core Idea
The **chi-square (χ²) distribution** with n degrees of freedom is the distribution of the sum of n independent squared standard normal variates. It plays a central role in tests for variance, goodness of fit, and many normal-theory procedures. Its shape is positively skewed (always non-negative), with the tail thickness controlled by the degrees of freedom. The χ² distribution has an important **additive property** that mirrors the additivity of independent χ² sums.

> **In Simple Terms:** Square a standard normal — that's a χ² with 1 d.f. Add up n of them — that's a χ² with n d.f. The bigger n gets, the more bell-shaped (and less skewed) it looks.

### Key Concepts

#### Definition
If X ~ N(μ, σ²), then Z = (X − μ)/σ ~ N(0, 1) and:
$$Z^2 = \left(\frac{X − μ}{σ}\right)^2 \sim \chi^2_1$$

In general, if X₁,…,Xₙ are independent N(μᵢ, σᵢ²):
$$\chi^2 = \sum_{i=1}^{n} \left(\frac{X_i − μ_i}{σ_i}\right)^2 \sim \chi^2_n$$

#### Probability Density Function
$$f(\chi^2) = \frac{1}{2^{n/2}\,Γ(n/2)}\,(\chi^2)^{(n/2)−1}\,e^{-\chi^2/2},\ \chi^2 > 0$$

#### Shape
- For n ≤ 2: density is monotonically decreasing.
- For n > 2: unique maximum (mode) at χ² = n − 2.
- Always **positively skewed**.

#### Additive Property of χ²
If χ²₁ ~ χ²(n₁) and χ²₂ ~ χ²(n₂) are independent, then χ²₁ + χ²₂ ~ χ²(n₁ + n₂). Justification: this is the sum of squares of (n₁ + n₂) independent standard normals — automatic from the definition.

### Mechanisms / Processes — Derivation Sketch
The text proves the χ²(n) p.d.f. by **mathematical induction**:
1. Verify n = 1 case directly using transformation z = x² (two-to-one map from x to z).
2. Assume true for n = t; consider U = Σx²ᵢ (i=1..t) and 𝔠 = x²_(t+1) (independent χ²(1)).
3. Apply one-to-one polar-style transformation (u = u'·cos θ, 𝔠 = u'·sin θ).
4. Compute Jacobian J = u'.
5. Integrate out θ using the Beta function ∫cos²θ·dθ = B(½,½)/2 etc.
6. Resulting marginal of u'² has the χ²(t+1) form ⇒ induction closes.

### Definitions
- **Chi-square variate (χ²)** ⭐ (exam-important): sum of squares of independent standard normal variates.
- **Degrees of freedom (df)** ⭐: parameter n governing shape; equals number of independent squared normals being summed.
- **Additive property of χ²** ⭐: independent χ² with df n₁, n₂ sum to χ² with df (n₁ + n₂).
- **Jacobian transformation**: technique for finding the density of a transformed random variable using the determinant of partial derivatives.

> **Quick Recall:**
> - χ²₁ = Z² (square of one standard normal)
> - χ² ≥ 0 always; positively skewed
> - Mode at n − 2 (for n > 2)
> - Sum of independent χ²s is χ² with df added
> - Used in: variance tests, goodness-of-fit, contingency tables

### Connections
- Builds on: properties of standard normal distribution (assumed prior).
- Foundation for: t-distribution and F-distribution (next chunk).
- Used in: chi-square goodness-of-fit test (Chunk 004), variance tests (Chunk 008).

<!-- Continues in chunk 004 -->
