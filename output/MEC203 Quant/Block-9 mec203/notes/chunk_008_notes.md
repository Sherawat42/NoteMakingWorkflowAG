# Chunk 008 — Critical Values, P-value Method, Type I/II Errors, Power, Tests under Normality
<!-- Pages: 71-80 -->
<!-- Source: chunk_008.txt -->

## Section: Critical Values of Z (Table 31.1) 🔴
<!-- See chunk 007 for the introduction of critical values -->

### Core Idea
The text tabulates the standard normal critical values commonly used in hypothesis testing, separated by tail structure (two-tailed, right-tailed, left-tailed). For small n (<30), the sampling distribution of Z is *not* normal, so these values cannot be used.

### Key Concepts

#### Table 31.1 — Critical Values of Z
| Test type | α = 1% | α = 5% | α = 10% |
|---|---|---|---|
| Two-tailed | \|z_α\| = 2.58 | \|z_α\| = 1.96 | \|z_α\| = 1.645 |
| Right-tailed | z_α = 2.33 | z_α = 1.645 | z_α = 1.28 |
| Left-tailed | z_α = −2.33 | z_α = −1.645 | z_α = −1.28 |

#### Key Observation
The two-tailed critical value at α equals the one-tailed critical value at α/2 (since each tail of the two-tailed has area α/2).

> **Quick Recall:**
> - 5% two-tailed: ±1.96
> - 5% one-tailed: 1.645
> - 1% two-tailed: ±2.58
> - 1% one-tailed: 2.33
> - For n < 30, use t-table (not normal).

---

## Section: Critical Region Method vs P-value Method 🔴

### Core Idea
Two equivalent procedures for hypothesis testing:
- **Critical Region method** — compute test statistic, compare with tabulated critical value.
- **P-value method** — compute the *probability* of observing data as extreme as that obtained, assuming H₀; compare with α.

The P-value is the lowest level of significance at which H₀ could be rejected.

> **In Simple Terms:** Both methods give the same answer. The critical-region method asks "is my test statistic extreme enough?". The P-value method asks "how rare would my data be if H₀ were true?"

### Key Concepts

#### P-value Method Steps (for two-tailed test)
1. Compute test statistic Z.
2. Find the tail area:
   - Z > 0 → area to right of Z under standard normal.
   - Z < 0 → area to left of Z.
3. **Double** the tail area (because it's two-tailed) → P-value.
4. Decide:
   - P < α → reject H₀.
   - P ≥ α → do not reject H₀.

#### Guidelines for P-values
| P-value | Decision |
|---|---|
| < 0.01 | Reject H₀; significant at 1% |
| 0.01 ≤ P < 0.05 | Reject H₀; significant at 5% |
| 0.05 ≤ P < 0.10 | Consider Type I consequences before rejecting |
| ≥ 0.10 | Do not reject H₀; not significant |

### Definitions
- **P-value** ⭐: lowest level of significance at which H₀ could be rejected; tail probability under H₀.

> **Quick Recall:**
> - P-value < α → reject
> - P-value method and critical region method are equivalent
> - For two-tailed test, double the one-tailed area.

---

## Section: Procedure for Hypothesis Testing (5-Step Recipe) 🔴

### Mechanisms / Processes

| Step | Action |
|---|---|
| 1 | Set up null hypothesis H₀. |
| 2 | Set up alternative hypothesis H₁ (decides one-tailed vs two-tailed). |
| 3 | Choose level of significance α (in advance!). |
| 4 | Compute test statistic Z = (t − E(t))/SE(t) under H₀. |
| 5 | Compare with z_α: if \|Z\| < z_α → not significant (do not reject); if \|Z\| > z_α → significant → reject H₀. |

#### Table 31.2 — Hypothesis Tests about Population Mean (σ Known)
| Test | H₀ | H₁ | Test statistic | Reject H₀ if |
|---|---|---|---|---|
| Lower-tail | μ ≥ μ₀ | μ < μ₀ | z = (x̄ − μ₀)/(σ/√n) | z ≤ −z_α (or P-value < α) |
| Upper-tail | μ ≤ μ₀ | μ > μ₀ | z = (x̄ − μ₀)/(σ/√n) | z ≥ z_α (or P-value < α) |
| Two-tailed | μ = μ₀ | μ ≠ μ₀ | z = (x̄ − μ₀)/(σ/√n) | z ≤ −z_(α/2) or z ≥ z_(α/2) (or P-value < α) |

### Examples

#### Example: Junior Manager Salary
- Claim: average junior-manager salary > Rs. 42,000.
- Sample: n = 30, x̄ = Rs. 43,260; σ = Rs. 5,260; α = 0.05.
- H₀: μ ≤ 42,000; H₁: μ > 42,000 → **right-tailed test**, z_α = 1.65.
- z = (43,260 − 42,000)/(5,260/√30) = 1,260/960.4 = **1.32**.
- 1.32 < 1.65 → **do not reject H₀**. Sample mean is higher but not *significantly* higher; difference may be due to chance.

#### Example: Average Wind Speed (P-value Method)
- Claim: average wind speed = 8 mph.
- Sample: n = 32, x̄ = 8.2; s = 0.6; α = 0.05.
- H₀: μ = 8 (claim); H₁: μ ≠ 8 → **two-tailed**.
- z = (8.2 − 8)/(0.6/√32) = 0.2/0.106 ≈ **1.89**.
- Area to right of z = 1.89 (Z table) = 0.5 − 0.4706 = **0.0294**.
- Two-tailed: 0.0294 vs α/2 = 0.025; 0.0294 > 0.025 → P > α ⇒ **accept H₀**.
- Conclusion: not enough evidence to reject the claim.

> **Quick Recall:**
> - Step 1–5 recipe is the standard procedure.
> - Step 3: fix α *before* drawing data.
> - Test statistic always: z = (observed − expected)/SE.

---

## Section: Type I and Type II Error 🔴

### Core Idea
Hypothesis testing risks two errors:
- **Type I**: rejecting H₀ when it is true (probability α — the level of significance).
- **Type II**: accepting H₀ when it is false (probability β).

These are also called **producer's risk** (Type I — rejecting good lots) and **consumer's risk** (Type II — accepting bad lots) in industrial sampling. For fixed n, reducing one error generally increases the other.

> **In Simple Terms:** Type I says "guilty when innocent" (false alarm). Type II says "innocent when guilty" (missed detection). You can't reduce both at once with a fixed sample.

### Key Concepts
- α = P[reject H₀ | H₀ true] = level of significance = size of critical region.
- β = P[accept H₀ | H₁ true].
- Producer's risk (industrial term) ↔ α.
- Consumer's risk (industrial term) ↔ β.
- For continuous population: probability of Type I error = level of significance = size of critical region.
- Trade-off: tests are usually framed to fix α at 5% or 1% and then minimise β.

### Definitions
- **Type I Error (α)** ⭐: rejecting H₀ when it is true.
- **Type II Error (β)** ⭐: accepting H₀ when it is false.
- **Producer's Risk = α**; **Consumer's Risk = β**.

### ⚠️ Common Mistakes
- ❌ Mistake: thinking we can simultaneously reduce α and β by tweaking the test. → ✅ Correct: For fixed n, reducing α typically *increases* β, and vice versa. The remedy is increasing n.
- ❌ Mistake: confusing α (Type I) with β (Type II). → ✅ Correct: α = false rejection; β = false acceptance. Power = 1 − β.

> **Quick Recall:**
> - Type I = α = false rejection (producer's risk)
> - Type II = β = false acceptance (consumer's risk)
> - Power = 1 − β
> - For continuous distributions: α = size of critical region.

---

## Section: Power of the Test 🔴

### Core Idea
The **power** of a test is its probability of correctly rejecting H₀ when the alternative is true. Power = 1 − β. The **power function** is (1 − β) viewed as a function of the parameter under H₁; the **power of the test at a parameter point** is the value of this function at that point.

### Key Concepts
- Power = P[reject H₀ | H₁ true] = 1 − P[Type II error] = 1 − β.
- High power = good test = correctly detects falsity of H₀.
- Power varies with the parameter (some H₁ values are easier to detect than others).

### Definitions
- **Power of the test** ⭐: probability of correctly rejecting H₀ when H₁ is true (= 1 − β).
- **Power function**: (1 − β) as a function of the parameter.

> **Quick Recall:**
> - Power = 1 − β
> - Higher power = better test
> - Larger n → higher power (for fixed α).

---

## Section: Optimum Test Under Different Situations 🔴

### Core Idea
The "best" test is the one that maximises power (for a given α). When the alternative is **simple** (single value), the best test is the **Most Powerful Test (MP)**. When the alternative is **composite** (multiple values), the best test is the **Uniformly Most Powerful Test (UMP)** if it exists for all values in H₁.

### Subsection: Most Powerful Test 🔴

#### Definition
For testing simple H₀: θ = θ₀ against simple H₁: θ ≠ θ₀, a critical region W is **most powerful** of size α if:
1. P(x ∈ W | H₀) = α.
2. P(x ∈ W | H₁) > P(x ∈ W₁ | H₁) for every other critical region W₁ satisfying condition 1.

### Subsection: Uniformly Most Powerful Test 🔴

#### Definition
For testing simple H₀: θ = θ₀ against composite H₁: θ ≠ θ₀, a critical region W is **uniformly most powerful** of size α if:
1. P(x ∈ W | H₀) = α.
2. For all θ ≠ θ₀: P(x ∈ W | H₁) ≥ P(x ∈ W₁ | H₁) for any other W₁ satisfying condition 1.

### Definitions
- **Most Powerful Test** ⭐: best test against a simple alternative.
- **Uniformly Most Powerful Test (UMP)** ⭐: best test against a composite alternative, uniformly across all values.

> **Quick Recall:**
> - MP ⇒ simple alternative.
> - UMP ⇒ composite alternative.
> - Both maximise power at level α.

---

## Section: Test Procedure Under Normality — Univariate Normal 🔴

### Core Idea
Three cases for testing the mean μ and/or the standard deviation σ of a single normal population, depending on which parameter is known:
- **Case I**: μ unknown, σ known → use Z-test.
- **Case II**: μ known, σ unknown → use χ²-test for σ².
- **Case III**: both unknown → use Student's t-test for μ.

### Notation
- Sample mean: x̄ = (1/n)·Σxᵢ.
- Sample variance s² = (1/n)·Σ(xᵢ − x̄)² (biased) or **s'² = (1/(n−1))·Σ(xᵢ − x̄)² (unbiased)**.
- Distinction: s²·n = s'²·(n−1).

### Subsection: Case I — μ Unknown, σ Known 🔴

#### Test Statistic
$$T = \frac{\sqrt n\,(x̄ − μ_0)}{σ} \sim N(0, 1) \text{ under } H_0$$

#### Rejection Rules
- H₁: μ > μ₀ → reject if T > τ_α (upper α point).
- H₁: μ < μ₀ → reject if T < τ_(1−α) = −τ_α.
- H₁: μ ≠ μ₀ → reject if |T| > τ_(α/2).

#### Confidence Limits for μ (level 1 − α)
$$x̄ ± τ_{α/2}\cdot \frac{σ}{\sqrt n}$$

### Subsection: Case II — μ Known, σ Unknown 🔴

#### Test Statistic
$$\psi = \frac{\sum (x_i − μ)^2}{σ_0^2} \sim \chi^2(n) \text{ under } H_0: σ = σ_0$$

#### Rejection Rules
- H₁: σ > σ₀ → reject if ψ > χ²_(α, n).
- H₁: σ < σ₀ → reject if ψ < χ²_(1−α, n).
- H₁: σ ≠ σ₀ → reject if ψ < χ²_(1−α/2, n) or ψ > χ²_(α/2, n).

#### Confidence Limits for σ²
$$\left[\frac{\sum(x_i − μ)^2}{\chi^2_{α/2, n}},\ \frac{\sum(x_i − μ)^2}{\chi^2_{1−α/2, n}}\right]$$

For σ: positive square roots of these.

### Subsection: Case III — Both μ and σ Unknown 🔴

#### Test Statistic — Student's t-test
$$t = \frac{\sqrt n\,(x̄ − μ_0)}{s'} \sim t(n − 1) \text{ under } H_0$$
This is the classical **Student's t-test**.

#### Rejection Rules
- H₁: μ > μ₀ → reject if t > t_(α, n−1).
- H₁: μ < μ₀ → reject if t < −t_(α, n−1).
- H₁: μ ≠ μ₀ → reject if |t| > t_(α/2, n−1).

#### Confidence Limits for μ
$$x̄ ± t_{α/2, n−1}\cdot \frac{s'}{\sqrt n}$$

#### Test for σ in Case III (μ unknown)
Use $(n − 1)s'^2/σ_0^2 \sim \chi^2(n − 1)$ under H₀: σ = σ₀.
- Compare computed value with χ²_(α, n−1) or χ²_(1−α, n−1) as per H₁.
- Two-tailed: compare with both χ²_(1−α/2, n−1) and χ²_(α/2, n−1).
- CI for σ²: [(n−1)s'²/χ²_(α/2, n−1), (n−1)s'²/χ²_(1−α/2, n−1)].

### Definitions
- **Student's t-test** ⭐: classical test for μ when σ unknown; t = √n·(x̄ − μ₀)/s' ~ t(n−1).
- **Sample variance s² vs s'² distinction** ⭐: s² uses n in denominator (biased); s'² uses n−1 (unbiased).

### ⚠️ Common Mistakes
- ❌ Mistake: Using z-test when σ is unknown. → ✅ Correct: Use t-test with df = n − 1; for n large, t ≈ z but the t-table is the right reference.
- ❌ Mistake: Confusing s² and s'². → ✅ Correct: s² = (1/n)Σ(x−x̄)² (MLE-style); s'² = (1/(n−1))Σ(x−x̄)² (unbiased). Use s'² for inference.

> **Quick Recall:**
> - Case I (σ known): z-test
> - Case II (μ known): χ² test of σ²
> - Case III (both unknown): t-test for μ, χ²(n−1) for σ²
> - 95% CI for μ: x̄ ± t_(0.025, n−1)·s'/√n

### Connections
- Builds on: t-distribution and χ²-distribution (Chunk 004).
- Continues into: comparison of two univariate normals (Chunk 009).

<!-- Continues in chunk 009 -->
