# Chunk 004 — χ² Properties, Goodness of Fit, t and F Distributions, Joint Sampling Distributions
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->

## Section: Chi-square — Critical Values and Two Key Properties 🔴
<!-- See chunk 003 for χ² definition and additive property -->

### Core Idea
For practical use of χ², two ideas matter: (i) for large n, χ² critical values can be approximated using a normal-distribution shortcut, and (ii) the **MGF derivation** confirms the additive structure. Two properties of the χ² distribution are central to its use in testing variance:
- the difference of two nested χ²'s is itself χ²,
- in a normal sample, x̄ and S² are independent and (n−1)S²/σ² ~ χ²(n−1).

### Key Concepts

#### Large-n Approximation
For n > 30, √(2χ²) is approximately normally distributed with mean √(2n − 1) and SD 1. This is used to compute χ² probability levels for large n.

#### Critical Values
- χ²(α, n) = upper α point: P[χ² > χ²(α, n)] = α (right tail).
- Lower α point = χ²(1 − α, n).
- As n increases, critical values increase; as α decreases, critical values increase.

#### Moment Generating Function Derivation (additive property)
For χ²(1): M_χ²(t) = (1 − 2t)^(−1/2).
For sum of n independent χ²(1)s: M(t) = ∏(1 − 2t)^(−1/2) = (1 − 2t)^(−n/2). This is the MGF of χ²(n) — confirming additivity.

#### Property 1 — Subtraction
If X₁, X₂ are independent and X₁ + X₂ ~ χ²(n), with X₁ ~ χ²(n₁), then X₂ ~ χ²(n − n₁).

#### Property 2 — Sample Mean and Variance from Normal
For a random sample of size n from N(μ, σ²) with mean x̄ and variance S²:
- (a) **x̄ and S² are independent.**
- (b) **(n − 1)S²/σ² ~ χ²(n − 1).**

#### Proof Sketch of (b)
Identity: Σ(xᵢ − μ)² = Σ(xᵢ − x̄)² + n(x̄ − μ)². Divide by σ². The LHS is a sum of n independent squared standard normals → χ²(n). The second RHS term equals [(x̄ − μ)/(σ/√n)]² ~ χ²(1). Since x̄ ⊥ S² (by part (a)), the two terms on the RHS are independent. Subtraction property → (n−1)S²/σ² ~ χ²(n − 1).

### Definitions
- **Critical value of χ²** ⭐: the value χ²(α, n) such that P[χ² > χ²(α, n)] = α.
- **Significant value**: synonymous with critical value.

> **Quick Recall:**
> - For n > 30: √(2χ²) ≈ N(√(2n−1), 1)
> - x̄ ⊥ S² (independence) for normal samples — *unique* to normality
> - (n−1)S²/σ² ~ χ²(n−1) — basis for variance tests and CIs for σ²
> - MGF of χ²(n): M(t) = (1−2t)^(−n/2)

---

## Section: Chi-square Test of Goodness of Fit (Karl Pearson) 🔴

### Core Idea
**Karl Pearson's χ² goodness-of-fit test** measures the discrepancy between observed (Oᵢ) and expected (Eᵢ) frequencies. The test statistic, computed as Σ(Oᵢ − Eᵢ)²/Eᵢ, follows a χ² distribution with (n − 1) df under the null hypothesis. It is an **approximate** test, valid for large n.

> **In Simple Terms:** You expect the digits 0–9 to appear about equally often in a phone book. Count how many times each does. Pearson's test tells you whether the gap between expected and observed is big enough to call "biased".

### Key Concepts
- Observed frequencies: O₁, O₂, …, Oₙ (from data)
- Expected frequencies: E₁, E₂, …, Eₙ (from theory; ΣEᵢ = ΣOᵢ)
- Test statistic:
$$\chi^2 = \sum_{i=1}^{n} \frac{(O_i − E_i)^2}{E_i} \sim \chi^2(n − 1)$$
- df = n − 1 (we lose 1 df due to the constraint ΣOᵢ = ΣEᵢ).
- Reject H₀ at level α if computed χ² > χ²(α, n − 1).

### Definitions
- **Goodness of fit** ⭐: assessment of how well theoretical frequencies match observed frequencies.
- **Pearson's χ² statistic** ⭐: Σ(Oᵢ − Eᵢ)²/Eᵢ.

> **Quick Recall:**
> - Formula: Σ(O − E)²/E
> - df = (number of categories) − 1
> - Approximate test (large n)

### Connections
- Builds on: chi-square distribution (Section: Chi-square, this chunk and Chunk 003).
- Applications: digit-uniformity test, dice-bias test (Check Your Progress 1, Chunk 004 questions).

---

## Section: Student's t-Distribution 🔴

### Core Idea
The Student's t-distribution arises when σ is unknown and we replace it by the sample standard deviation s. The resulting standardized statistic t = (x̄ − μ)/(s/√n) does **not** have a normal distribution; instead, it has a heavier-tailed distribution with df = n − 1, called Student's t. It approaches the standard normal as df → ∞ and reduces to the **Cauchy distribution** when df = 1.

> **In Simple Terms:** The normal distribution assumes you know σ. In real life you usually don't, so you estimate it with s. That extra uncertainty gives you the t-distribution — which has fatter tails than the normal, especially for small samples.

### Key Concepts

#### Definition
For a random sample of size n from N(μ, σ²) with σ unknown:
$$t = \frac{x̄ − μ}{s/\sqrt{n}} \sim t(n − 1)$$

where s² = (1/(n−1))·Σ(xᵢ − x̄)² is the unbiased estimator of σ².

#### Probability Density Function
$$f(t) = \frac{1}{\sqrt{ν}\,B(1/2, ν/2)}\,\left(1 + \frac{t^2}{ν}\right)^{-(ν+1)/2},\quad −∞ < t < ∞$$

#### Special Cases
- ν = 1 → standard **Cauchy distribution**: f(t) = 1/[π(1 + t²)].
- ν → ∞ → standard normal.

#### Symmetry
Symmetric about t = 0; more peaked than the normal of same SD.

### Definitions
- **Student's t** ⭐: t = (x̄ − μ)/(s/√n) when σ unknown; df = n − 1.
- **Cauchy distribution**: special case of Student's t with df = 1.

> **Quick Recall:**
> - df = n − 1
> - More peaked than normal but heavier tails for small df
> - df = 1 → Cauchy
> - Use t when σ is unknown and estimated by s

---

## Section: Fisher's t 🟡

### Core Idea
**Fisher's t** is the more general definition: t is the ratio of a standard normal variate to the square root of an *independent* chi-square divided by its df. Student's t is a *special case* of Fisher's t (in which the χ² comes from sample variance of the same data).

### Key Concepts
- Definition: if T ~ N(0, 1) and χ² ~ χ²(n) are independent, then **t = T / √(χ²/n) ~ t(n)**.
- Derived via Jacobian transformation:
  - Joint density of (T, χ²) → polar transformation → marginal of t matches Student's t p.d.f.
- Relationship: Student's t is a particular case of Fisher's t.
- For large n, t ≈ N(0,1).
- Symbol: t_(α, n) such that P[t > t_(α, n)] = α.
- Symmetry: t_(α, n) = −t_(α, n) ... wait, actually t_(1−α, n) = −t_(α, n).

> **Quick Recall:**
> - Fisher's t = N(0,1) / √(χ²(n)/n)
> - Student's t ⊂ Fisher's t
> - For large n: t ≈ z

---

## Section: Snedecor's F Distribution 🔴

### Core Idea
The **F-distribution** is the ratio of two independent χ² variates each divided by their respective degrees of freedom. It depends on (n₁, n₂) — the two df parameters — but **not** on any population parameter. It is highly **positively skewed**. It is the basis for variance-ratio tests (testing equality of variances and ANOVA).

### Key Concepts

#### Definition
If X ~ χ²(n₁) and Y ~ χ²(n₂) are independent:
$$F = \frac{X/n_1}{Y/n_2} \sim F(n_1, n_2)$$

#### Properties
- Distribution depends only on (n₁, n₂); independent of population parameters.
- Highly **positively skewed**.
- Special case: with n₁ = 1, F = t² where t has df n₂.
- **Reciprocal property:**
$$F_{1−α; n_1, n_2} = \frac{1}{F_{α; n_2, n_1}}$$
This means tables only need to publish the upper α points; lower α points are obtained by reciprocal.

#### Probability Density Function
$$f(F) = \frac{(n_1/n_2)^{n_1/2}}{B(n_1/2, n_2/2)}\,F^{(n_1/2)−1}\,\left(1 + \frac{n_1 F}{n_2}\right)^{-(n_1+n_2)/2},\ F > 0$$

### Definitions
- **F-statistic / F-distribution (Snedecor's F)** ⭐: ratio of two independent χ² variates each over their df. ⭐

> **Quick Recall:**
> - F(n₁, n₂) — first df is for numerator
> - Only positive values; skewed right
> - Tables publish only upper α; lower comes from reciprocal
> - F with n₁=1 corresponds to t²

### Connections
- Builds on: chi-square distribution.
- Used in: variance-ratio test, ANOVA, two-sample variance comparison (Chunks 008–010).

---

## Section: Sampling Distributions of Mean and Variance from a Normal Distribution 🔴

### Core Idea
Starting from a random sample x₁,…,xₙ from N(μ, σ²), the text proves three deeply connected results:
1. **x̄ ~ N(μ, σ²/n)** — sample mean is itself normally distributed.
2. **(n−1)s²/σ² ~ χ²(n−1)** — the sample variance follows a scaled χ² distribution.
3. **x̄ and s² are independent** — a property unique to the normal distribution.

These three results together justify the t-statistic and most normal-theory inference.

### Mechanisms / Processes — Derivation Sketch

Set up an orthogonal transformation from xᵢ to yᵢ:
- y₁ = (1/√n) · Σ(xᵢ − μ)/σ = √n·(x̄ − μ)/σ
- y_i (i = 2,…,n) = orthogonal contrasts (e.g., (1,−1,0,…,0)/√2, (1,1,−2,0,…,0)/√6, …)
- All (n−1) contrast vectors are mutually orthogonal and orthogonal to (1/√n,…,1/√n).

Steps:
1. Jacobian J = σⁿ.
2. Σyᵢ² = Σ(xᵢ − μ)²/σ² (preserved by orthogonal transform).
3. Joint p.d.f of y₁,…,yₙ: ∏ N(0,1) — i.e., n iid standard normals.
4. y₁ alone gives x̄: marginal x̄ ~ N(μ, σ²/n).
5. Σyᵢ² (i=2..n) = Σyᵢ² − y₁² = Σ(xᵢ − μ)²/σ² − n(x̄ − μ)²/σ² = Σ(xᵢ − x̄)²/σ² = (n−1)s²/σ².
6. As (n−1) independent N(0,1) squared, this sum is χ²(n−1).
7. Independence of y₁ and (y₂,…,yₙ) ⇒ independence of x̄ and s².

#### p.d.f. of x̄
$$g(x̄) = \frac{\sqrt{n}}{σ\sqrt{2π}}\exp\left[-\frac{n(x̄ − μ)^2}{2σ^2}\right]$$

#### p.d.f. of s²
(continues into Chunk 005 in the source text)
$$u(s^2) = \frac{n^{(n−1)/2}}{(2σ^2)^{(n−1)/2}\,Γ((n−1)/2)}\,(s^2)^{(n−3)/2}\,\exp\left[-\frac{(n−1)s^2}{2σ^2}\right]$$

### Definitions
- **Independence of x̄ and s² in normal sampling** ⭐: uniquely holds in normal samples; foundational for Student's t-test.

> **Quick Recall:**
> - Normal sample of size n: x̄ ~ N(μ, σ²/n); (n−1)s²/σ² ~ χ²(n−1); x̄ ⊥ s².
> - Independence of x̄ and s² is what allows the t-statistic to be a ratio of independent normal/√(χ²/df).

### Connections
- Builds on: chi-square distribution (this chunk).
- Foundation for: Student's t-test in Unit 31 (Chunks 008–009).

<!-- Continues in chunk 005 -->
