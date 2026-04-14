# Chunk 004 — Precision of Estimates, SRSWR, SRSWOR, I-PSS, Systematic Sampling, PPS (intro)
<!-- Pages: 32-41 -->
<!-- Source: chunk_004.txt -->
<!-- Continues from: Section: Random or Probability Sampling (Chunk 003) -->
<!-- Continues into: Section: PPS-WR Sampling, Stratified Sampling (Chunk 005) -->

## Section: Precision of Estimates — Standard Errors and Confidence Intervals 🔴

### Core Idea
When a random sample is drawn from a population, the sample mean (an estimate of the population mean) will vary from sample to sample. The *sampling distribution* of the sample mean describes how these estimates are distributed across all possible samples. The *standard error (SE)* measures this variability and quantifies the precision of the estimate. Confidence intervals use the SE to give a range within which the true population parameter likely falls.

> **In Simple Terms:** Imagine you weigh 30 apples from a bag and calculate their average weight. If you repeated this with another 30 apples from the same bag, you'd get a slightly different average. The standard error tells you how much your average weight is likely to vary — the smaller the SE, the more confident you can be that your sample average is close to the true average for all apples.

### Key Concepts

#### Sampling Distribution of Sample Mean
- The sample mean *m* computed from a random sample is a random variable.
- All possible values of *m* from repeated samples form a **sampling distribution** of the sample mean.
- If parent population is N(µ, σ²), then sampling distribution of *m* is **N(µ, σ²/n)**.
- The variability of *m* (σ²/n) is much smaller than the population variance (σ²) and decreases as *n* increases → precision increases with sample size.

#### Unbiased Estimator
- Estimator "t" of parameter "θ" is **unbiased** if E(t) = θ (the mean of its sampling distribution equals the true parameter).
- The sample mean *m* is an unbiased estimator of the population mean M (under SRSWR/SRSWOR).
- If E(t) = Kθ or K+θ, bias can be corrected by using t/K or (t–K) as the estimator.

#### Standard Error (SE) and Coefficient of Variation (CV/RSE)
- **Standard Error (SE)**: Standard deviation of the sampling distribution of an estimator. Measures the precision of the estimate.
  - SE(m) = σ/√n
- **Coefficient of Variation (CV) = Relative Standard Error (RSE)**: SE divided by mean — dimensionless measure of relative precision.
  - CV or RSE = C = σ/M = SE(m)/ m̄

#### Properties of the Normal Distribution (for Confidence Intervals)
| Coverage | SD from mean | Z-value |
|---------|-------------|---------|
| ~68% | ±1 SD | 1.00 |
| ~95% | ±1.96 SD | 1.96 |
| ~99% | ±2.576 SD | 2.576 |

#### Confidence Intervals (Known σ²)
A confidence interval for the population mean M with confidence coefficient 99%:
```
Lower limit = m – 2.576 × (σ/√n)
Upper limit = m + 2.576 × (σ/√n)
```
**General Rule**: Estimate ± (z-value × Standard Error of estimate)

#### Confidence Intervals (Unknown σ² — Student's t-distribution)
When population variance σ² is not known:
- Use unbiased estimate of variance: **v(y) = [ss]²/(n–1)** where [ss]² = Σ(yᵢ – m)²
- Unbiased estimate of sampling variance of m: **v(m) = v(y)/n**
- The statistic t = (m – M) / √v(m) follows **Student's t-distribution** with (n–1) degrees of freedom.
- Confidence interval: **[m – tα × √v(m) < M < m + tα × √v(m)]**

#### Central Limit Theorem (Non-Normal Parent Population)
Even if the population is **not** normally distributed:
- The sampling distribution of m has mean = population mean M, regardless of sample size.
- As sample size n increases, the sampling distribution of m approaches **normal distribution**.
- For n ≥ 30: use normal approximation (or t ≈ z). Proceed as in the known-σ² case.

### Definitions
- **Sampling Distribution**: The probability distribution of a statistic over all possible samples of a given size from a population. ⭐ (exam-important)
- **Unbiased Estimator**: An estimator whose sampling distribution has a mean equal to the true parameter value. ⭐ (exam-important)
- **Standard Error (SE)**: Standard deviation of the sampling distribution of an estimator; measures precision. ⭐ (exam-important)
- **Coefficient of Variation (CV) / Relative Standard Error (RSE)**: SE divided by mean; dimensionless. ⭐ (exam-important)
- **Confidence Interval**: A range within which the population parameter lies with a stated probability (confidence coefficient). ⭐ (exam-important)
- **Sampling Variance**: Variance of the sampling distribution of an estimator.

> **Quick Recall:**
> - SE(m) = σ/√n → precision ↑ as n ↑, but not proportionally (need 4× sample for 2× precision)
> - 99% CI: m ± 2.576 SE; 95% CI: m ± 1.96 SE
> - Unknown σ²: use t-distribution with v(m) = v(y)/n
> - Central Limit Theorem: for n ≥ 30, sampling dist. is approximately normal regardless of parent distribution

### ⚠️ Common Mistakes
- ❌ Mistake: SE decreases proportionally with sample size → ✅ Correct: SE = σ/√n; it decreases in proportion to √n, not n. To halve the SE, you need to quadruple the sample size.
- ❌ Mistake: SRSWOR gives no advantage over SRSWR when sampling fraction is very small → ✅ Correct: When n/N < 0.05, the finite population correction ≈ 1, and the advantage of SRSWOR disappears.

---

## Section: Determination of Sample Size 🟡

### Core Idea
Random sampling allows us to determine the required sample size in advance — based on either a desired precision level (CV or permissible error) or a sanctioned budget. This is a major advantage over non-random sampling.

> **In Simple Terms:** Before cooking a feast, you decide how many guests you're hosting and plan your ingredients accordingly. Sample size determination is the same — you decide what level of accuracy you need, then calculate how large a sample that requires.

### Mechanisms / Processes

**Method 1: Based on desired CV**
```
C(m) = C/√n  →  n = [C/C(m)]²
```
Where C = population CV (from prior data), C(m) = desired CV of sample mean.

**Method 2: Based on permissible error (e)**
```
n = [2.576 × C / e]²
```
Where e = permissible relative error = (m – M)/M.

**Method 3: Budget-constrained (cost function)**
- Linear cost: F = F₀ + F₁n → n = (F – F₀)/F₁
- With loss from imprecision: minimise total cost L(n) → **n = [(ℓ/2)(C/F₁)]^(2/3)**

---

## Section: Simple Random Sampling with Replacement (SRSWR) 🔴

### Core Idea
SRSWR is the simplest random sampling method. Every unit has an **equal probability** of selection at each draw, and selected units are **placed back** before the next draw. Units can appear more than once in the sample. The sample mean is an unbiased estimator of the population mean.

> **In Simple Terms:** SRSWR is like drawing a name from a hat, noting it, and putting it back before the next draw. The same name could come up again.

### Mechanisms / Processes
**Operational Procedure** (using Random Number Tables):
1. Number all N population units from 1 to N.
2. Turn to a random page of the random number table.
3. Select random numbers between 1 and N; record the corresponding units.
4. If a number > N, reject it. If a number repeats, include that unit again (with replacement).
5. Repeat until n units are selected.

### Key Formulae (SRSWR)
| Quantity | Formula | Formula Number |
|---------|---------|----------------|
| Estimator of M | m_srswr = (1/n)Σyᵢ | 2.25 |
| Sampling Variance of m | V(m_srswr) = σ²/n | 2.26 |
| Standard Error of m | SE(m_srswr) = σ/√n | 2.27 |
| CV/RSE of m | C(m_srswr) = C(y)/√n | 2.28 |
| Unbiased estimate of σ² | v(y) = [ss]²/(n–1) | 2.29 |
| Unbiased estimate of V(m) | v(m_srswr) = v(y)/n | 2.30 |
| Estimator of population total Y | Y* = Nm | 2.31 |
| V(Y*) | N²(σ²/n) | 2.32 |
| Sample proportion estimator of P | p_srswr (unbiased) | 2.34 |
| V(p_srswr) | PQ/n | 2.35 |

### Definitions
- **SRSWR**: Random sampling where each unit has equal probability of selection at every draw with replacement; units can repeat. ⭐ (exam-important)

> **Quick Recall:**
> - SRSWR: equal probability, with replacement, units can repeat
> - m_srswr = unbiased estimator of M
> - V(m_srswr) = σ²/n; SE = σ/√n
> - Precision ↑ as n ↑, but SE reduction not proportional to n increase

---

## Section: Simple Random Sampling without Replacement (SRSWOR) 🔴

### Core Idea
SRSWOR selects n **distinct** units — once selected, a unit is not placed back. This method is more efficient than SRSWR because it reduces the variance by a *finite population correction* factor. However, this advantage diminishes when the sampling fraction n/N is small (< 0.05).

> **In Simple Terms:** SRSWOR is like a lottery where each ticket can only be drawn once. Since you can never pick the same person twice, you get a better cross-section of the population, making your estimate more precise.

### Key Concepts

#### Finite Population Correction (FPC)
- V(m_srswor) = [(N–n)/(N–1)] × (σ²/n)
- The factor **(N–n)/(N–1)** is the FPC (also called finite population multiplier).
- FPC < 1 for n > 1 → V(m_srswor) < V(m_srswr) → SRSWOR is **more efficient**.
- When sampling fraction n/N < 0.05: FPC ≈ 1 → advantage of SRSWOR disappears.

### Key Formulae (SRSWOR)
| Quantity | Formula | Formula Number |
|---------|---------|----------------|
| Estimator of M | m_srswor = (1/n)Σyᵢ (unbiased) | 2.38 |
| Sampling Variance of m | V(m_srswor) = [(N–n)/(N–1)] × σ²/n | 2.39 |
| Comparison | V(m_srswor) < V(m_srswr) for n > 1 | 2.40 |
| Unbiased estimate of V(m) | v(m_srswor) = [(N–n)/N] × (1/n) × [ss]²/(n–1) | 2.41 |
| Estimator of Y | Y*_srswor = N × m_srswor (unbiased) | 2.42 |
| V(p) (sample proportion) | [(N–n)/(N–1)] × PQ/n | 2.47 |

### Definitions
- **SRSWOR**: Random sampling where each unit has equal probability of selection; selected units are NOT replaced — each unit appears at most once. ⭐ (exam-important)
- **Finite Population Correction (FPC)**: The factor (N–n)/(N–1) applied to the variance formula in SRSWOR; accounts for the finite population size. ⭐ (exam-important)

> **Quick Recall:**
> - SRSWOR: n distinct units; more efficient than SRSWR
> - FPC = (N–n)/(N–1); V(m_srswor) < V(m_srswr)
> - FPC ≈ 1 when n/N < 0.05 → SRSWOR advantage disappears
> - Both m_srswr and m_srswor are unbiased for M; but m_srswor is more efficient

### ⚠️ Common Mistakes
- ❌ Mistake: SRSWOR is always better than SRSWR → ✅ Correct: Only when sampling fraction > 0.05; for very small fractions (n/N < 0.05), FPC ≈ 1, so the advantage is negligible.
- ❌ Mistake: V(Y*) = N × V(m) → ✅ Correct: V(Y*) = N² × V(m) (since Y* = Nm, not Nm).

---

## Section: Interpenetrating Sub-Samples (I-PSS) 🟡

### Core Idea
I-PSS involves splitting the sample into *h* independent sub-samples, each drawn by the same method, each providing a valid estimate of the population parameter. The key advantage of **independent** I-PSS: provides a simple, unbiased estimate of V(t) even when the sampling design or estimator is complex.

> **In Simple Terms:** I-PSS is like asking h different teams to independently survey the same city using the same method. Each team gives its own estimate; the spread among those estimates tells you how reliable the overall estimate is.

### Key Formulae (I-PSS)
| Quantity | Formula | Number |
|---------|---------|--------|
| Combined estimate of θ | t = (1/h)Σtᵢ (unbiased) | 2.50 |
| Unbiased estimate of V(t) | v(t) = [1/h(h–1)] Σ(tᵢ – t)² | 2.51 |
| Confidence interval probability | Pr[Min{t} < θ < Max{t}] = [1 – (1/2)^(h–1)] | 2.52 |

- Probability increases rapidly with h: 0.5 (h=2) → 0.875 (h=4)

### Definitions
- **Interpenetrating Sub-Samples (I-PSS)**: Two or more sub-samples drawn by the same method from the same population, each providing a valid estimate of the parameter. ⭐ (exam-important)

---

## Section: Systematic Sampling 🔴

### Core Idea
Select a random start *r* (from 1 to k, where k = [N/n]), then select every k-th unit. Only one random number is needed. Operationally very convenient. The sampling variance depends on how units are arranged in the population, which is both an advantage and a disadvantage.

> **In Simple Terms:** Systematic sampling is like checking every 10th student on the attendance register starting from a random initial position. Very easy to do — but if students are listed in height order and you want to estimate height, every 10th student might give biased results.

### Key Concepts

#### Systematic Sampling with Random Start
- Choose random start r (1 ≤ r ≤ k); k = [N/n] = sampling interval
- Select units: U_r, U_{r+k}, U_{r+2k}, ...
- If N = nk: all k systematic samples have size n; m_sys* = m (sample mean, unbiased for M)
- If N ≠ nk: sample sizes vary; m_sys* = (k/N)Σyᵢ ≠ m (bias in using m directly)

#### Circular Systematic Sampling (CSS) — Advantage
Overcomes the N ≠ nk problem:
- If r+jk > N, select unit U_{r+jk–N}
- All samples have equal size; m_r is unbiased for M.

#### Efficiency of Systematic Sampling
- V(m_sys) = σ_b² (between-sample variance)
- V(m_sys) = V(y) – σ_w² (total variance – within-sample variance)
- V(m_sys) ↓ when within-sample variance σ_w² ↑ (units within a sample are heterogeneous → arrange population to maximize heterogeneity within samples)

### Definitions
- **Systematic Sampling**: Selecting every k-th unit from the population after a random start r. ⭐ (exam-important)
- **Sampling Interval (k)**: The integer nearest to N/n; the gap between selected units.
- **Circular Systematic Sampling (CSS)**: Modification ensuring all samples have equal size n by wrapping around.

### Edge Cases & Caveats
- **Periodic/Cyclic trends**: Systematic sampling is NOT recommended when the population has periodic or cyclic variations, as the sample might consistently hit peaks or troughs. (Workaround: if the period is known, adjust accordingly.)
- **N not a multiple of n**: Causes unequal sample sizes and bias in using sample mean; overcome by CSS.
- **Unbiased estimate of V(m_sys)**: Not directly possible from a single systematic sample. (Workaround: use I-PSS technique.)

> **Quick Recall:**
> - Systematic: random start r, then every k-th unit (k = [N/n])
> - Very operationally convenient; only 1 random number needed
> - CSS: wraps around to ensure equal sample size and unbiased m
> - NOT recommended for periodic populations
> - V(m_sys) ↓ when within-sample heterogeneity ↑

---

## Section: Sampling with Probability Proportional to Size (PPS) 🔴
<!-- Continues in Chunk 005 -->

### Core Idea
In PPS, the **probability of selecting a unit is proportional to its size** (a related auxiliary variable). If the size variable X is proportional to the study variable Y, then PPS is more efficient than SRSWR. Each selected unit's observation is weighted by 1/pᵢ to produce unbiased estimates.

> **In Simple Terms:** PPS sampling gives larger factories a higher chance of selection (since they contribute more to total employment). But we then weight their observations accordingly, so the overall estimate remains unbiased.

### Mechanisms / Processes

**For a Sample of Size 1 (pps):**
- Pᵢ = Xᵢ/X (probability of selecting unit i)
- Unbiased estimator of population total Y: Y*(1)_pps = y₁/p₁ (Formula 2.58)
- Unbiased estimator of M: m*(1)_pps = (1/N)(y₁/p₁) (Formula 2.59)
- V[Y*(1)_pps] = Σ(Yᵢ²/Pᵢ) – Y² (Formula 2.60)
- Variance is small when Pᵢ are proportional to Yᵢ (i.e., X linearly related to Y through origin)

**Operational Procedure (PPS with replacement):**
1. Cumulate the sizes X₁, X₂, ..., Xₙ → cumulative totals T₁, T₂, ..., Tₙ
2. Select a random number R between 1 and Tₙ = X (total)
3. Select unit Uᵢ if Tᵢ₋₁ < R ≤ Tᵢ → P(Uᵢ) = Xᵢ/X = Pᵢ
4. Repeat n times for a sample of size n (pps-wr)
<!-- Continues in Chunk 005 -->

### Connections
- Builds on: SRSWR (this chunk) — PPS is a generalisation where equal probabilities are replaced by size-proportional probabilities
- Continues into: PPS-WR formulae, Stratified Sampling (Chunk 005)
