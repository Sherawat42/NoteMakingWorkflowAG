# Chunk 007 — Normal Distribution & Standard Normal Variable
<!-- Pages: 61-70 -->
<!-- Source: chunk_007.txt -->

## Section: Poisson Examples & Sum-of-Poissons Property 🔴
<!-- See chunk 006 for start of Poisson Distribution -->

### Examples
**Example: 5 defects per 10 sq.ft of cloth — P(at least 6 defects in 15 sq.ft)?**
Average defects per 15 sq.ft = (5/10) × 15 = 7.5. So λ = 7.5.
P(X ≥ 6) = 1 − P(X ≤ 5).
Using Poisson tables (Table 27.5 in source): P(X ≤ 5) = 0.2415.
Therefore **P(X ≥ 6) = 1 − 0.2415 = 0.7585**.

| x | P(X = x) at λ = 7.5 |
|---|---------------------|
| 0 | 0.0006 |
| 1 | 0.0041 |
| 2 | 0.0156 |
| 3 | 0.0389 |
| 4 | 0.0729 |
| 5 | 0.1094 |

### Mechanisms / Processes
Proof that Sum of independent Poisson is Poisson (using p.m.f.):
1. P[X₁ + X₂ = k] = Σ_{k₁=0..k} P[X₁ = k₁] P[X₂ = k − k₁].
2. = e^(−λ₁) e^(−λ₂) · (1/k!) · Σ_{k₁} kCk₁ · λ₁^k₁ · λ₂^(k−k₁) (binomial expansion).
3. = e^(−(λ₁+λ₂)) · (λ₁ + λ₂)^k / k!.
4. ⇒ X₁ + X₂ ~ Poi(λ₁ + λ₂). Generalises to n variables.

### Examples
**Example (CYP 2 Q5): Average defective rate 10% — P(exactly 3 defectives in sample of 10)? Use Poisson approximation, e = 2.72.**
λ = 10 × 0.1 = 1.
f(3) = e^(−1) · 1³ / 3! = 0.3679 / 6 ≈ **0.061**.

**Example (CYP 2 Q6): 2% items defective; sample of 100; P(3 or more defectives)?**
λ = np = 100 × 0.02 = 2.
P(≥ 3) = 1 − [f(0) + f(1) + f(2)] = 1 − e^(−2) [1 + 2 + 4/2] = 1 − e^(−2) · 5 ≈ 1 − 0.135·5 = **0.325**.

**Example (CYP 2 Q7): P(7 of 10 recover from disease), p = 0.8, independence.**
n = 10, p = 0.8, x = 7.
P = ¹⁰C₇ · (0.8)⁷ · (0.2)³ ≈ **0.20**.

> **Quick Recall:**
> - λ scales linearly with the size of the observation interval (e.g., per 15 sq.ft = 1.5 × per 10 sq.ft).
> - Sum of independent Poissons → Poisson with summed λ.

---

## Section: Normal Distribution 🔴

### Core Idea
The **normal distribution** is the most important continuous distribution in statistics. Its bell-shaped p.d.f. is fully determined by two parameters: the **mean μ** (location) and **standard deviation σ** (spread). It models measurement errors, heights, IQ scores, and (via the Central Limit Theorem) the sum of many independent random variables. Modern statistical inference rests on properties of the normal distribution.

> **In Simple Terms:** The "bell curve." Drop a dart at the centre many times — the spread of misses follows a normal distribution. So do most natural measurements when many small random factors add up.

### Key Concepts

#### p.d.f.
**f(x) = (1 / (σ·√(2π))) · exp(−(x − μ)² / (2σ²))** for −∞ < x < ∞, σ > 0.

#### Parameters
- μ = mean (also median, mode — they coincide).
- σ = standard deviation.

#### Properties (full list — high yield)

1. **Continuous probability distribution.**
2. **Two parameters**: μ and σ.
3. **Symmetric about μ** — mean = mode = median.
4. **Quartiles**: Q₁ ≈ μ − 0.67σ; Q₃ ≈ μ + 0.67σ (equidistant from μ).
5. **All odd central moments = 0** (μ_(2r+1) = 0 for r = 1, 2, 3, …) — direct corollary of symmetry.
6. **Tails extend to infinity** on both sides; never touch the horizontal axis.
7. **Maximum ordinate** = 1 / (σ·√(2π)), at x = μ.
8. **Beyond x = μ ± 3σ** the density is essentially zero.
9. **Inflexion points** at x = μ ± σ — where curvature changes.
10. **Unimodal**: f'(x) > 0 for x < μ; f'(x) < 0 for x > μ; f'(μ) = 0.
11. **P(X = c) = 0** for any constant c (continuous).
12. P(X > a) = area under the curve to the right of a.
13. **Empirical Rule (68–95–99.7)**:
    - ≈ 68% within 1σ of mean.
    - ≈ 95% within 2σ of mean.
    - ≈ 99.7% within 3σ of mean.
14. **Sum of two independent normals**: X ~ N(μ₁, σ₁²), Y ~ N(μ₂, σ₂²) ⇒ X + Y ~ N(μ₁ + μ₂, σ₁² + σ₂²).

#### Moment Generating Function
**M_X(t) = exp(μt + σ²t²/2)**.
- M'(0) = μ ⇒ E(X) = μ.
- M''(0) = μ² + σ² ⇒ Var(X) = σ².

### Definitions
- **Normal Distribution**: f(x) = (1/(σ√(2π))) exp(−(x − μ)²/(2σ²)). Two parameters: mean μ, std dev σ. ⭐ (exam-important)
- **Empirical Rule (68-95-99.7)**: 1σ, 2σ, 3σ contain ≈ 68%, 95%, 99.7% of the area. ⭐ (exam-important)

### Mechanisms / Processes
Verification ∫f(x) dx = 1:
1. Substitute z = (x − μ)/σ, dx = σ dz.
2. Integral becomes (1/√(2π)) ∫_{−∞}^∞ e^(−z²/2) dz.
3. By symmetry: 2 × (1/√(2π)) ∫₀^∞ e^(−z²/2) dz.
4. Using Gaussian integral ∫₀^∞ e^(−z²/2) dz = √(π/2).
5. = 2 · (1/√(2π)) · √(π/2) = 1 ✓.

> **Quick Recall:**
> - **f(x) = (1/(σ√(2π))) e^(−(x−μ)²/(2σ²))**
> - μ = mean = median = mode (symmetric)
> - σ controls spread; ±3σ contains 99.7%
> - 68-95-99.7 rule
> - MGF: e^(μt + σ²t²/2)

---

## Section: Standard Normal Distribution & Standardisation 🔴

### Core Idea
Any normal random variable X ~ N(μ, σ²) can be transformed into a **standard normal variable** Z = (X − μ)/σ with mean 0 and variance 1. The c.d.f. of Z is tabulated as Φ(z), so any normal probability calculation reduces to looking up Φ values. The Central Limit Theorem is what makes this trick worth memorising.

> **In Simple Terms:** Subtract the mean and divide by the standard deviation, and your normal variable becomes "standard" — mean 0, std dev 1. Now you can use a single universal table to find any normal probability.

### Key Concepts

#### Z transformation
**Z = (X − μ)/σ** ⇒ **Z ~ N(0, 1)**.

#### Standard normal p.d.f.
**φ(z) = (1/√(2π)) · exp(−z²/2)** for −∞ < z < ∞.

#### Standard normal c.d.f.
**Φ(z) = ∫_{−∞}^z φ(t) dt** = area to the left of z.
By symmetry: **Φ(−z) = 1 − Φ(z)**.

#### Key area facts (must memorise)
- Area between z = ±3 ⇒ 99.73%.
- Area between z = ±2.58 ⇒ 99%.
- Area between z = ±1.96 ⇒ 95%.

#### Critical values (right-tail areas) — used in hypothesis testing
- z = 1.645 ⇒ right-tail area 5% (denoted z_(0.05)).
- z = 1.96 ⇒ right-tail area 2.5% (z_(0.025)).
- z = 2.33 ⇒ right-tail area 1% (z_(0.01)).

#### Theorem (linear transformation of a normal)
If X ~ N(μ, σ²) and Y = a + bX (b ≠ 0), then **Y ~ N(a + bμ, b²σ²)**.
Special case (a = −μ/σ, b = 1/σ): Y = (X − μ)/σ ~ N(0, 1).

### Definitions
- **Standard Normal Variable Z**: Z = (X − μ)/σ when X ~ N(μ, σ²); follows N(0, 1). ⭐ (exam-important)
- **Φ(z)**: Cumulative distribution function of N(0, 1). ⭐ (exam-important)
- **Upper α-point t_α**: Value such that P(Z > t_α) = α; lower α-point is −t_α (by symmetry).

### Mechanisms / Processes
Standardised normal probability lookup recipe:
1. Identify μ and σ of the original normal X.
2. Convert each boundary to z-scores: z = (x − μ)/σ.
3. Look up Φ(z) in standard normal tables.
4. Combine via Φ(z₂) − Φ(z₁) for an interval, or 1 − Φ(z) for right-tail.

### Examples
**Example: Heights of 10,000 men, X ~ N(64.5, 4.5²).**
Convert to z: z = (X − 64.5)/4.5.

| x | z |
|---|---|
| 55.5 | −2 |
| 64.5 | 0 |
| 69 | 1 |
| 73.5 | 2 |

(a) P(55.5 < X < 69) = P(−2 < Z < 1) = Φ(1) − Φ(−2) = 0.84 − 0.02 ≈ 0.82.
Number of men: 10,000 × 0.82 = **8,200**.

(b) P(X < 55.5) = P(Z < −2) ≈ 0.02 ⇒ **200** men.

(c) P(X > 73.5) = P(Z > 2) = 1 − Φ(2) ≈ 0.02 ⇒ **200** men.

**Example (CYP 3 Q1): Weights of 500 students, X ~ N(151, 15²).**
(i) P(120 < X < 155) = Φ(0.27) − Φ(−2.07) = Φ(0.27) − (1 − Φ(2.07)) = 0.6064 − 1 + 0.9808 = **0.5872**.
(ii) P(X > 155) = 1 − Φ(0.27) = 1 − 0.6064 = **0.3936**.

**Example (CYP 3 Q2): Mean = 50; 5% of values > 60. Find σ.**
P(X > 60) = 0.05 ⇒ z = 1.64 corresponds to area 0.95 to the left. So 1.64 = (60 − 50)/σ ⇒ **σ = 10/1.64 ≈ 6.10**.

### ⚠️ Common Mistakes
- ❌ Mistake: Looking up Φ(−z) directly when most tables tabulate only positive z → ✅ Correct: Use Φ(−z) = 1 − Φ(z).
- ❌ Mistake: Confusing the *area to the left* (Φ(z)) with the *area to the right* (1 − Φ(z)) when reading "P(X > a)" — careful with the inequality direction.
- ❌ Mistake: Using Φ(z) for a continuous variable as though P(X = c) > 0 → ✅ Correct: Always P(X = c) = 0; P(X ≤ c) = P(X < c).

### Edge Cases & Caveats
- The maximum ordinate of N(μ, σ²) is 1/(σ√(2π)) — *not* 1; densities can exceed 1 if σ is small.
- The two tails *never* touch zero, but density beyond ±3σ is negligible for practical purposes.

> **Quick Recall:**
> - **Z = (X − μ)/σ ~ N(0, 1)** (standardisation)
> - φ(z) = (1/√(2π)) e^(−z²/2)
> - Φ(−z) = 1 − Φ(z) (symmetry)
> - 95% within ±1.96σ; 99% within ±2.58σ; 99.73% within ±3σ
> - z_(0.05) = 1.645, z_(0.025) = 1.96, z_(0.01) = 2.33

### Connections
- Builds on: [Normal Distribution] (this chunk).
- Builds on: [Linear transformation rules] (Chunk 005, MGF section).
- Pre-requisite for: All hypothesis testing and confidence intervals based on normal/large-sample theory.

### Open Questions
1. How large does n need to be for the Central Limit Theorem to make a sample mean approximately normal?
2. When is the t-distribution used instead of standard normal? (Outside this block — covered in inference units.)
