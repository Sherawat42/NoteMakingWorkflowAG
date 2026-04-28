# Chunk 009 — Comparison of Two Univariate Normals, Bivariate Normal Tests, Unit 31 Wrap-up
<!-- Pages: 81-90 -->
<!-- Source: chunk_009.txt -->

## Section: Comparison of Two Univariate Normal Distributions 🔴
<!-- Continues from chunk 008 (univariate normal tests) -->

### Core Idea
Two independent normal samples — one from N(μ₁, σ₁²) of size n₁ and one from N(μ₂, σ₂²) of size n₂ — give rise to three test cases, parallel to the single-sample situation: (I) variances known, (II) means known, (III) all four parameters unknown. Each case yields a specific test statistic with a known sampling distribution under H₀, plus matching confidence-limit formulas.

> **In Simple Terms:** When you have two groups (say, two batches of bulbs), the test you use depends on what you already know. If you know both standard deviations, use a Z-test on the mean difference; if you know both means, use an F-test on the variance ratio; if you know nothing, pool the variances and use Fisher's two-sample t-test.

### Subsection: Case I — μ₁, μ₂ Unknown, σ₁, σ₂ Known 🔴

#### Test Statistic
Since x̄₁ − x̄₂ is a linear function of normals, it is itself normal with mean (μ₁ − μ₂) and variance σ₁²/n₁ + σ₂²/n₂ (covariance term zero by independence). Hence

$$T = \frac{(x̄_1 − x̄_2) − ε_0}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}} \sim N(0, 1) \text{ under } H_0: μ_1 − μ_2 = ε_0$$

#### Rejection Rules
| Alternative H₁ | Reject H₀ if |
|---|---|
| μ₁ − μ₂ > ε₀ | T > τ_α |
| μ₁ − μ₂ < ε₀ | T < −τ_α |
| μ₁ − μ₂ ≠ ε₀ | \|T\| > τ_(α/2) |

The commonest case is ε₀ = 0, i.e. testing equality of the two means.

#### Confidence Limits for (μ₁ − μ₂)

$$(x̄_1 − x̄_2) \pm \tau_{α/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

### Subsection: Case II — μ₁, μ₂ Known, σ₁, σ₂ Unknown 🔴

#### Test Statistic
Σⱼ(x_{1j} − μ₁)²/σ₁² ~ χ²(n₁) and Σⱼ(x_{2j} − μ₂)²/σ₂² ~ χ²(n₂), independent. The ratio (after dividing each by its df) is F-distributed:

$$F = \frac{\sum_j (x_{1j} − μ_1)^2 / (n_1 σ_1^2)}{\sum_j (x_{2j} − μ_2)^2 / (n_2 σ_2^2)} \sim F(n_1, n_2)$$

Under H₀: σ₁/σ₂ = ξ₀, replace σ₁² = ξ₀²σ₂² and the statistic becomes computable from data.

When ξ₀ = 1 (commonest form: H₀: σ₁ = σ₂):

$$F = \frac{\sum_j (x_{1j} − μ_1)^2 / n_1}{\sum_j (x_{2j} − μ_2)^2 / n_2}$$

#### Rejection Rules
| Alternative | Reject H₀ if |
|---|---|
| σ₁/σ₂ > ξ₀ | F > F_(α; n₁, n₂) |
| σ₁/σ₂ < ξ₀ | F < F_(1−α; n₁, n₂), i.e. 1/F > F_(α; n₂, n₁) |
| σ₁/σ₂ ≠ ξ₀ | F < F_(1−α/2; n₁, n₂) or F > F_(α/2; n₁, n₂) |

#### Confidence Limits for σ₁²/σ₂²

$$\left[\frac{1}{F_{α/2;\,n_1,n_2}} \cdot \frac{\sum(x_{1j}−μ_1)^2/n_1}{\sum(x_{2j}−μ_2)^2/n_2},\quad \frac{1}{F_{α/2;\,n_2,n_1}} \cdot \frac{\sum(x_{1j}−μ_1)^2/n_1}{\sum(x_{2j}−μ_2)^2/n_2}\right]$$

For σ₁/σ₂: take positive square roots.

### Subsection: Case III — All Means and Variances Unknown 🔴

#### (a) Test for Equality of Means (assume σ₁ = σ₂ = σ)

Under the simplifying assumption of a common standard deviation, we form the **pooled variance**

$$s'^2 = \frac{(n_1 − 1) s_1'^2 + (n_2 − 1) s_2'^2}{n_1 + n_2 − 2}$$

and use **Fisher's t-test**:

$$t = \frac{(x̄_1 − x̄_2) − ε_0}{s'\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 − 2)$$

The numerator is standard normal under H₀; the denominator is √(χ²/df) where the χ² (with df = n₁ + n₂ − 2) is the sum of two independent χ²s with df n₁ − 1 and n₂ − 1.

#### Confidence Limits for (μ₁ − μ₂)

$$(x̄_1 − x̄_2) \pm t_{α/2;\,n_1+n_2−2}\cdot s'\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$$

s'² is the estimate of the common variance σ².

#### (b) Test for Ratio of Variances (μ's unknown)

Replace μ₁ and μ₂ with x̄₁ and x̄₂, costing one df each. The F statistic becomes

$$F = \frac{s_1'^2}{s_2'^2}\cdot \frac{1}{ξ_0^2}\quad \text{with df } (n_1 − 1, n_2 − 1)$$

For H₀: σ₁ = σ₂ (ξ₀ = 1), F = s'₁²/s'₂². Confidence limits for σ₁²/σ₂²:

$$\left[\frac{1}{F_{α/2;\,n_1−1,n_2−1}}\cdot\frac{s_1'^2}{s_2'^2},\quad \frac{1}{F_{α/2;\,n_2−1,n_1−1}}\cdot\frac{s_1'^2}{s_2'^2}\right]$$

### Definitions
- **Pooled variance s'²** ⭐: weighted average of two unbiased sample variances; estimate of common σ²; df = n₁ + n₂ − 2.
- **Fisher's two-sample t-test** ⭐: t = ((x̄₁ − x̄₂) − ε₀)/(s'·√(1/n₁ + 1/n₂)) ~ t(n₁ + n₂ − 2). Assumes equal (but unknown) σ.
- **F-test for equality of variances** ⭐: F = s'₁²/s'₂² with df (n₁ − 1, n₂ − 1) when both means unknown; df (n₁, n₂) when both means known.

### ⚠️ Common Mistakes
- ❌ Mistake: Using independent (unpaired) t-test on paired data. → ✅ Correct: If observations are paired (before/after on same units), use paired t (see Bivariate section below).
- ❌ Mistake: Forgetting the df subtraction when means are estimated. → ✅ Correct: Estimating each μ from sample loses 1 df, so Case III df is (n₁ − 1, n₂ − 1) instead of (n₁, n₂).
- ❌ Mistake: Pooling variances when σ₁ ≠ σ₂. → ✅ Correct: Pooled t assumes equal variances; if equality is doubtful, run F-test for variance equality first.

> **Quick Recall:**
> - Case I (σ's known) → Z-test on (x̄₁ − x̄₂); SE = √(σ₁²/n₁ + σ₂²/n₂).
> - Case II (μ's known) → F-test on variance ratio; df (n₁, n₂).
> - Case III (all unknown) → pooled-variance t-test; df = n₁ + n₂ − 2; F-test uses df (n₁ − 1, n₂ − 1).
> - Pooled variance: s'² = [(n₁ − 1)s'₁² + (n₂ − 1)s'₂²] / (n₁ + n₂ − 2).

### Connections
- Builds on: Univariate normal tests (Chunk 008).
- Builds on: t and F distributions (Chunk 004).
- Continues into: Worked Q3, Q4 in Unit 31 Exercises (Chunk 010).

---

## Section: Problems Relating to a Bivariate Normal Distribution 🔴
<!-- Reason: explicit Unit 31 objective; multiple Check Your Progress problems -->

### Core Idea
When (x, y) is bivariate normal with means μ_x, μ_y, standard deviations σ_x, σ_y, and correlation ρ — and all parameters are unknown — three families of inference problems arise: tests on the correlation coefficient ρ, tests on the difference μ_x − μ_y (paired data), and tests on the ratio σ_x/σ_y. Each is reduced to a t-test by a clever transformation.

> **In Simple Terms:** A bivariate normal pair lets us ask "are x and y correlated?", "do they have the same mean?", and "do they have the same spread?" Each question becomes a t-test once we either compute the sample correlation or take a linear combination (x ± y).

### Subsection: Test for the Correlation Coefficient 🔴

#### Sample correlation coefficient
$$r = \frac{\sum_i(x_i − \bar x)(y_i − \bar y)}{\sqrt{\sum_i(x_i − \bar x)^2 \cdot \sum_i(y_i − \bar y)^2}}$$

#### Test of H₀: ρ = 0
When ρ = 0 the sampling pdf of r simplifies to f(r) = (1−r²)^((n−4)/2)/B(½, (n−2)/2) (a beta-form expression noted in the source). This makes

$$t = \frac{r\sqrt{n − 2}}{\sqrt{1 − r^2}} \sim t(n − 2) \text{ under } H_0$$

#### Test of H₀: ρ = ρ₀ (general)
Exact test is intractable because r has a complicated distribution when ρ ≠ 0. For moderately large n an approximate test exists (Fisher's z-transform; not derived in this unit).

### Subsection: Difference Between μ_x and μ_y — Paired t-test 🔴

#### Setup
Define z_i = x_i − y_i. Since z is a linear combination of jointly normal variables, z is also normal with

- mean: μ_z = μ_x − μ_y
- variance: σ_z² = σ_x² + σ_y² − 2ρσ_xσ_y

#### Test Statistic — Paired t

$$t = \frac{\sqrt{n}\,(\bar z − ε_0)}{s_z} \sim t(n − 1)\text{ under } H_0:\, μ_x − μ_y = ε_0$$

where s_z² = (1/(n−1))·Σ(z_i − z̄)².

#### Confidence Limits for (μ_x − μ_y)
$$\bar z \pm t_{α/2;\,n−1}\cdot \frac{s_z}{\sqrt n}$$

#### Test for Ratio μ_x/μ_y = η
Set z = x − ηy; under H₀: μ_x/μ_y = η₀, μ_z = 0, so use t = √n·z̄/s_z with df = n − 1 (paired t in disguise).

### Subsection: Ratio σ_x/σ_y in Bivariate Normal 🔴

#### Trick — orthogonal linear combinations
Let ξ = σ_x/σ_y. Define
- u = x + ξ y
- v = x − ξ y

Then u, v are jointly normal with cov(u, v) = σ_x² − ξ²σ_y² = 0, so they are uncorrelated normals.

Hence H₀: σ_x/σ_y = ξ₀ is **equivalent to H₀: ρ_{uv} = 0**.

#### Test Statistic
$$t = \frac{r_{uv}\sqrt{n − 2}}{\sqrt{1 − r_{uv}^2}} \sim t(n − 2) \text{ under } H_0$$

#### Confidence Limits for ξ = σ_x/σ_y
Use the inequality

$$P\left[\frac{r_{uv}^2(n−2)}{1 − r_{uv}^2} \leq t_{α/2,\,n−2}^2\right] = 1 − α$$

Setting r_{uv}²(n−2)/(1 − r_{uv}²) = t²_(α/2, n−2) defines a quadratic equation w(ξ) = 0 in ξ. Two roots ξ₁ < ξ₂:
- If real and w(ξ) is convex: ξ₁ ≤ ξ ≤ ξ₂.
- If real and w(ξ) is concave: 0 < ξ ≤ ξ₁ or ξ₂ ≤ ξ < ∞.
- If imaginary: 100(1−α) % confidence limits **do not exist** for the given sample.

### Definitions
- **Sample correlation coefficient r** ⭐: r = Σ(xᵢ−x̄)(yᵢ−ȳ)/√[Σ(xᵢ−x̄)²·Σ(yᵢ−ȳ)²].
- **Test for ρ = 0** ⭐: t = r√(n−2)/√(1−r²) ~ t(n−2).
- **Paired t-test** ⭐: t = √n·(z̄ − ε₀)/s_z ~ t(n − 1) where z = x − y; for matched-pairs / before-after data.
- **Bivariate ratio-of-σ test**: H₀: σ_x/σ_y = ξ₀ ↔ H₀: ρ_{uv} = 0 with u = x + ξ₀y, v = x − ξ₀y.

### ⚠️ Common Mistakes
- ❌ Mistake: Using two-sample t (independent) for before/after data on same individuals. → ✅ Correct: Use paired t with z = x − y; df = n − 1, not 2n − 2.
- ❌ Mistake: Treating the t-test for ρ = 0 as valid for any ρ₀. → ✅ Correct: Only valid at ρ₀ = 0; for ρ₀ ≠ 0 the sampling distribution of r is non-standard.

> **Quick Recall:**
> - r = Σ(x−x̄)(y−ȳ)/√[Σ(x−x̄)²·Σ(y−ȳ)²]
> - Test ρ = 0: t = r√(n−2)/√(1−r²) ~ t(n−2)
> - Paired t: t = √n·z̄/s_z ~ t(n−1), z = x − y
> - σ_x/σ_y = ξ₀ test: t-test on r_{uv} where u = x + ξ₀y, v = x − ξ₀y

### Connections
- Builds on: t-distribution (Chunk 004) and confidence-interval framework (Chunk 007).
- Used in: Unit 31 Exercises Q5 (correlation) and Q6 (paired weight-change), see Chunk 010.

---

## Section: Unit 31 Let Us Sum Up + Key Words 🟢

### Core Idea
The unit ties together: estimator analysis, hypothesis testing of statistical claims, and the **test procedures under normality** for one population (univariate normal), two populations (comparison of two normals), and joint distributions (bivariate normal). The Key Words section restates definitions in compact form.

### Definitions (from §31.9 Key Words)
- **Alternative Hypothesis (H₁)** ⭐: any hypothesis complementary to H₀.
- **Confidence Interval / Limits / Coefficient** ⭐: pick small α (5% or 1%); find c₁, c₂ such that P[c₁ < θ < c₂] = 1 − α; c₁, c₂ are **confidence limits**, [c₁, c₂] is the **confidence interval**, and (1 − α) is the **confidence coefficient**.
- **Critical Region** ⭐: subset of sample space whose occurrence leads to rejection of H₀.
- **Level of Significance** ⭐: probability that a random value of the statistic falls in the critical region (= size of Type I error).
- **Null Hypothesis (H₀)** ⭐: a definite hypothesis of "no difference."
- **One-tailed test** ⭐: H₁ is one-sided (e.g. μ > μ₀ or μ < μ₀).
- **Two-tailed test** ⭐: H₁ is two-sided (μ ≠ μ₀).
- **Critical / Significant Value** ⭐: the boundary between rejection and acceptance regions on the test-statistic scale.
- **Most Powerful Test** ⭐: critical region W of size α with P(x ∈ W \| H₁) ≥ P(x ∈ W₁ \| H₁) for every other size-α critical region W₁ (simple H₀ vs simple H₁).
- **Parameter Space Θ** ⭐: set of all possible values of θ in f(x, θ).
- **Power of the Test** ⭐: 1 − P(Type II error) = P(reject H₀ \| H₁ true).
- **Type I Error**: rejecting H₀ when it is true.
- **Type II Error**: accepting H₀ when it is wrong (i.e., when H₁ is true).
- **Uniformly Most Powerful Test** ⭐: critical region W of size α such that, for all θ ≠ θ₀, P(x ∈ W \| H₁) ≥ P(x ∈ W₁ \| H₁) for any other size-α W₁.

> **Quick Recall:**
> - The unit's core deliverable: a recipe to test means, variances, and correlations under normality assumptions.
> - All tests reduce to Z, t, χ², or F.
> - Most Powerful = simple vs simple; Uniformly Most Powerful = simple vs composite.

### Connections
- Closes Unit 31, the entire Block-9 hypothesis-testing thread.

---

## Section: Beginning of Unit 31 Answers/Hints 🟢
<!-- Reason: only first answer (CYP1) is at end of chunk 009; full answers continue in chunk 010 -->

### Examples (from §31.10 Answers)
This chunk includes only the very start of the answer set; the worked solutions begin in earnest in Chunk 010 (CYP1 Q4 and onward).

<!-- Continues in chunk 010 -->
