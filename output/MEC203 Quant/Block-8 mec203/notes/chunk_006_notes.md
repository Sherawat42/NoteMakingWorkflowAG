# Chunk 006 — Marginal Distribution, Binomial & Poisson Distributions
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt -->

## Section: Joint c.d.f. — Worked Example 🟡
<!-- See chunk 005 for start of Joint Distribution -->

### Examples
**Example: Find joint c.d.f. for f(x, y) = (x + y) on 0 ≤ x ≤ 1, 0 ≤ y ≤ 1.**

Region I (0 ≤ x ≤ 1, 0 ≤ y ≤ 1):
F(x, y) = ∫₀^x ∫₀^y (s + t) dt ds = (1/2)·xy(x + y).

Region II (x ≥ 1, 0 ≤ y ≤ 1):
F(x, y) = ∫₀^1 ∫₀^y (s + t) dt ds = (1/2)·y(1 + y).

Region III (0 ≤ x ≤ 1, y ≥ 1):
F(x, y) = (1/2)·x(1 + x).

Region IV (x ≥ 1, y ≥ 1):
F(x, y) = 1.

Combined (with boundaries absorbed):
- F(x, y) = 0 for x < 0 or y < 0.
- F(x, y) = (1/2)·xy(x + y) for 0 ≤ x ≤ 1, 0 ≤ y ≤ 1.
- F(x, y) = (1/2)·y(1 + y) for x ≥ 1, 0 ≤ y ≤ 1.
- F(x, y) = (1/2)·x(1 + x) for 0 ≤ x ≤ 1, y ≥ 1.
- F(x, y) = 1 for x ≥ 1, y ≥ 1.

> **Quick Recall:**
> - Continuous joint c.d.f. is a *piecewise* function over rectangle regions.
> - Recover joint p.d.f. by ∂²F/∂x∂y.

---

## Section: Marginal Distribution 🔴

### Core Idea
A **marginal distribution** is what you get when you "ignore" or "sum out" one variable from a joint distribution. The marginal of X collapses the joint over all values of Y; it's the distribution of X by itself, regardless of Y.

> **In Simple Terms:** If the joint distribution is a heatmap of how (X, Y) values occur together, the marginal of X is the row totals, and the marginal of Y is the column totals.

### Key Concepts

#### Discrete marginals
- **g(x) = Σ_y f(x, y)** — marginal distribution of X.
- **h(y) = Σ_x f(x, y)** — marginal distribution of Y.

#### Continuous marginals
- **g(x) = ∫_{−∞}^∞ f(x, y) dy** — marginal density of X.
- **h(y) = ∫_{−∞}^∞ f(x, y) dx** — marginal density of Y.

### Definitions
- **Marginal distribution of X**: g(x) = Σ_y f(x, y) (discrete) / ∫ f(x, y) dy (continuous). ⭐ (exam-important)

### Examples
**Example: Marginal distribution from the 100-word table (continued from Chunk 005).**

Marginal of X (column sums): | x = 2 | x = 3 | x = 4 | x = 5 |
| | 0.35 | 0.44 | 0.16 | 0.05 |

Marginal of Y (row sums): | y = 0 | y = 1 | y = 2 |
| | 0.14 | 0.75 | 0.11 |

(Both add to 1.00 ✓.)

**Example (Check Your Progress 1, Q2): f(x, y) = (2/3)(x + 2y) for 0 ≤ x, y ≤ 1.**
Marginal of X:
g(x) = ∫₀¹ (2/3)(x + 2y) dy = (2/3)[xy + y²]₀¹ = (2/3)(x + 1) = **(1/3)(2x + 2)** for 0 ≤ x ≤ 1.

> **Quick Recall:**
> - Marginal = "row/column total" for joint p.m.f.
> - Use Σ over the *other* variable (or ∫ in continuous case)
> - Marginals must each sum/integrate to 1 individually

### Connections
- Builds on: [Joint Probability Distribution] (Chunk 005).
- Connects to: [Conditional distribution] = joint / marginal of conditioning variable.

---

## Section: Binomial Distribution 🔴

### Core Idea
The **binomial distribution** describes the number of "successes" in **n independent identical trials**, each with probability p of success. It's the model for repeated yes/no experiments — coin flips, defectives in a batch, recoveries in clinical trials. Binomial is the bedrock discrete distribution from which Poisson and (via the central limit theorem) the normal approximation are derived.

> **In Simple Terms:** Toss the same biased coin n times — how many heads do you get? That count follows the binomial distribution. The whole shape is determined by just two numbers: n (number of trials) and p (probability of success per trial).

### Key Concepts

#### p.m.f.
**f(x) = ⁿC_x · p^x · q^(n−x)**, x = 0, 1, …, n; q = 1 − p.

Defined when:
1. Each trial has only **two outcomes** (success / failure).
2. The probability **p is constant** across trials.
3. Trials are **independent**.

#### Parameters
n (number of trials) and p (probability of success). Together they determine the distribution completely.

#### Mean and variance
- **Mean μ = n·p**.
- **Variance σ² = n·p·q = n·p·(1−p)**.

#### Mode
- If (n+1)p is **not an integer**: mode = largest integer < (n+1)p.
- If (n+1)p is an integer: there are **two modes**, at (n+1)p and (n+1)p − 1.

#### Skewness and kurtosis
- Skewness = **(q − p) / √(npq)**.
- Kurtosis = 1 − 6pq / (npq)... (kurtosis is *positive when p < 0.5 or p > 0.5* — symmetric only at p = q = 1/2).
- When p = q = 1/2, distribution is **symmetric** for all n.

#### Sum of independent binomials (additive property)
If X ~ Bin(n₁, p) and Y ~ Bin(n₂, p) (same p, independent), then **(X + Y) ~ Bin(n₁ + n₂, p)**.
Generalises to any number of independent binomials with shared p.

#### Moment Generating Function
M_X(t) = E(e^(tX)) = Σ ⁿC_x (p·e^t)^x (1−p)^(n−x) = **(p·e^t + 1 − p)^n** = **{1 + p(e^t − 1)}^n**.
- M'(0) = np ⇒ μ = np.
- M''(0) = np(1 − p + np) ⇒ σ² = np(1 − p).

### Definitions
- **Binomial Distribution**: P(X = x) = ⁿC_x · p^x · (1−p)^(n−x), x = 0, 1, …, n. Two parameters (n, p). ⭐ (exam-important)
- **Bernoulli trial**: A single trial of a binomial — two outcomes, probability p of success.

### Mechanisms / Processes
Deriving μ = np algebraically:
1. μ = E(X) = Σ_x x · ⁿC_x p^x q^(n−x).
2. Use x · ⁿC_x = n · ⁽ⁿ⁻¹⁾C_(x−1).
3. Pull out np: μ = np · Σ_y ⁽ⁿ⁻¹⁾C_y p^y q^(n−1−y) where y = x − 1.
4. Inner sum is total mass of Bin(n − 1, p), which equals 1.
5. Therefore **μ = np**.

Deriving σ² = np(1 − p):
1. Compute E[X(X − 1)] = n(n − 1)p² (similar reduction).
2. E(X²) = E[X(X − 1)] + E(X) = n(n − 1)p² + np.
3. σ² = E(X²) − μ² = n(n − 1)p² + np − n²p² = np − np² = **np(1 − p)**.

### Examples
**Example: Probability of getting 7 heads in 12 tosses of an unbiased coin.**
n = 12, x = 7, p = 1/2, q = 1/2.
P = ¹²C₇ · (1/2)⁷ · (1/2)⁵ = ¹²C₇ · (1/2)¹².

**Example: Three coin tosses.**
n = 3, p = 1/2.
- P(X = 0) = ³C₀(1/2)³ = 1/8.
- P(X = 1) = ³C₁(1/2)³ = 3/8.
- P(X = 2) = ³C₂(1/2)³ = 3/8.
- P(X = 3) = ³C₃(1/2)³ = 1/8.
- P(more than 1 head) = 3/8 + 1/8 = 4/8 = 1/2.
- P(at least 1 head) = 1 − P(0 heads) = 1 − 1/8 = 7/8.

**Example: Mean = 4, std dev = √(8/3) — find n and p.**
np = 4, npq = 8/3 ⇒ q = (8/3)/4 = 2/3, p = 1/3, n = 4 / (1/3) = **12**.

**Example: Pass rate 60%, group of 6 — P(at least 4 passed)?**
p = 0.6, q = 0.4, n = 6.
f(4) + f(5) + f(6) = ⁶C₄·0.6⁴·0.4² + ⁶C₅·0.6⁵·0.4 + ⁶C₆·0.6⁶ = 1701/3125.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying binomial when trials are dependent (e.g., draws without replacement) → ✅ Correct: Use hypergeometric distribution; binomial requires *independent* trials.
- ❌ Mistake: Confusing p.m.f. parameter (p) with sample proportion → ✅ Correct: p is the *true* per-trial success probability, fixed and known.

> **Quick Recall:**
> - **Binomial: P(X = x) = ⁿC_x p^x q^(n−x)**
> - μ = np, σ² = npq
> - Two parameters: (n, p)
> - Symmetric ⇔ p = 1/2
> - Sum of independent Bin(n_i, p) is Bin(Σn_i, p)
> - MGF: (pe^t + q)^n

### Connections
- Builds on: [Independent Events] (Chunk 002), [Mathematical Expectation] (Chunks 002–003).
- Pre-requisite for: [Poisson Distribution] (this chunk) — Poisson is the limit n→∞, p→0, np = λ.

---

## Section: Poisson Distribution 🔴

### Core Idea
The **Poisson distribution** is the **limiting case** of the binomial when n → ∞ and p → 0 with **np = λ** held constant. It models the number of rare events in a fixed period — accidents per day, defects per unit area, calls per hour. It has **a single parameter λ** which equals both the mean *and* the variance.

> **In Simple Terms:** When something rare happens repeatedly with low probability across many opportunities, the count follows a Poisson distribution. Examples: number of typos per page, number of customers arriving in an hour, number of cars at a traffic signal.

### Key Concepts

#### p.m.f.
**P(X = x; λ) = (e^(−λ) · λ^x) / x!** for x = 0, 1, 2, …
Single parameter λ > 0; e ≈ 2.718.

#### Derivation as binomial limit
Set p = λ/n in binomial p.m.f. and let n → ∞ (with λ fixed):
- (1 − 1/n)(1 − 2/n)…(1 − (x − 1)/n) → 1.
- (1 − λ/n)^(−x) → 1.
- (1 − λ/n)^n → e^(−λ).
- ⁿC_x · p^x → λ^x / x!.

So binomial → **e^(−λ) · λ^x / x!** = Poisson p.m.f.

#### Properties
- **Mean = Variance = λ**.
- **Skewness = 1/√λ** ⇒ positively skewed.
- **Kurtosis = 1/λ** ⇒ leptokurtic (more peaked than normal).
- **Mode**: largest integer ≤ λ if λ not integer; two modes (λ and λ − 1) if integer.
- **Sum of independent Poissons**: X₁ ~ Poi(λ₁), X₂ ~ Poi(λ₂) ⇒ (X₁ + X₂) ~ Poi(λ₁ + λ₂).

#### Moment Generating Function
M_X(t) = e^(−λ) · Σ_x (λe^t)^x / x! = **e^(−λ) · e^(λe^t) = e^(λ(e^t − 1))**.
- M'(0) = λ ⇒ μ = λ.
- M''(0) = λ + λ² ⇒ Var = (λ + λ²) − λ² = **λ**.

#### When to use Poisson
- Number of accidents on a road crossing.
- Number of defects per unit area of cloth.
- Number of phone calls received by an operator.
- Number of suicides per year in an area.
- Approximation to binomial when **n is large** and **p is small** (n.p moderate).

### Definitions
- **Poisson Distribution**: P(X = x; λ) = e^(−λ) λ^x / x!, x = 0, 1, 2, …; one parameter λ. ⭐ (exam-important)
- **Mean = Variance = λ** is the signature property of Poisson. ⭐ (exam-important)

### Mechanisms / Processes
Setting up a Poisson approximation to binomial:
1. Verify n is large and p is small.
2. Compute λ = np.
3. Use P(X = x) = e^(−λ) λ^x / x! in place of the binomial p.m.f.

### Examples
**Example: P(X = 1) = P(X = 2) for Poisson — find P(X = 0 or 1) and E(X).**
P(X = 1) = λ·e^(−λ); P(X = 2) = λ² e^(−λ)/2. Equating: λ = λ²/2 ⇒ **λ = 2**.
- E(X) = λ = **2**.
- P(X = 0 or 1) = e^(−2) + 2·e^(−2) = **3·e^(−2)**.

**Example: λ = 3, e^(−3) = 0.0498. Find P(X = 0, 1, 2, 3), P(X < 3), P(X ≥ 2).**
- f(0) = e^(−3) = 0.0498.
- f(1) = 3·e^(−3) = 3·(0.0498) = 0.1494.
- f(2) = (9/2)·e^(−3) = 9·(0.0498)/2 = 0.2241.
- f(3) = (27/6)·e^(−3) = 27·(0.0498)/6 = 0.2241.
- P(X < 3) = f(0) + f(1) + f(2).
- P(X ≥ 2) = 1 − f(0) − f(1) = 1 − 4·(0.0498).

### ⚠️ Common Mistakes
- ❌ Mistake: Using Poisson when the rate varies over the observation window → ✅ Correct: Poisson assumes constant rate (homogeneous).
- ❌ Mistake: Using λ as a probability → ✅ Correct: λ is a *count rate*; can be > 1.

> **Quick Recall:**
> - **P(X = x) = e^(−λ) λ^x / x!**
> - **Mean = Variance = λ**
> - Limit of Bin(n, p) as n→∞, p→0, np = λ
> - Sum of independent Poissons is Poisson with summed λ
> - MGF: e^(λ(e^t − 1))

### Connections
- Builds on: [Binomial Distribution] (this chunk).
- Pre-requisite for: [Normal Distribution] (Chunk 007) — for large λ, Poisson approaches normal.

### Open Questions
1. What is the practical threshold (e.g., n > 20, p < 0.05) for using Poisson approximation to binomial?
