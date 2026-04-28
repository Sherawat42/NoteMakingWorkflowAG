# Chunk 004 — Random Variables, p.m.f., p.d.f., c.d.f., and Moments
<!-- Pages: 31-40 -->
<!-- Source: chunk_004.txt -->

## Section: Random Variables — Discrete vs Continuous 🔴

### Core Idea
A **random variable** is a real-valued function whose value depends on the outcome of a random experiment. They split sharply into two types — **discrete** (takes only countably many distinct values, like 0, 1, 2, …) and **continuous** (takes any value in an interval, e.g. all real numbers between 0 and 1). The discrete/continuous distinction governs every subsequent technique: probability mass function vs probability density function, sum vs integral, Σ vs ∫.

> **In Simple Terms:** A random variable is a number whose value depends on chance. Discrete = countable values like the number of heads in 3 coin tosses; continuous = any value in a range like the exact weight of a person.

### Key Concepts

#### Random variable — formal
A real-valued function defined over the points of a sample space (the set of all possible outcomes of an experiment) with a probability measure attached. It "translates" outcomes into numbers.

#### Discrete random variable
Takes only distinct (countable) values — e.g., number when rolling a die ∈ {1,2,3,4,5,6}, never 4.3 or 5.5. Examples: number of heads in 3 coin tosses, number of red cards in a 10-card draw, number of accidents in a city, number of misprints per page.

#### Continuous random variable
Takes any value within a given interval (uncountably infinite). Examples: life of an electrical gadget, duration of phone calls, annual rainfall in a district.

| Aspect | Discrete | Continuous |
|--------|----------|------------|
| Values | Countable (finite or countably infinite) | Uncountable (any real in interval) |
| Probability tool | p.m.f. f(x) = P(X = x) | p.d.f. f(x), used as ∫ f(x) dx |
| Probability of single value | f(x) > 0 possible | Always 0 |
| Aggregation | Σ | ∫ |

### Definitions
- **Random variable**: A real-valued function on the sample space (with a probability measure). ⭐ (exam-important)
- **Discrete random variable**: Takes countable values with no possible value strictly between two adjacent ones. ⭐ (exam-important)
- **Continuous random variable**: Takes any value within an interval / range. ⭐ (exam-important)

### Examples
- Toss a coin three times — X = number of heads → X ∈ {0,1,2,3} (discrete).
- Y = the number on a rolled die → Y ∈ {1,2,3,4,5,6} (discrete).
- Z = exact rainfall in mm → Z ∈ ℝ⁺ (continuous).

> **Quick Recall:**
> - RV = function from sample space to real numbers
> - Discrete ↔ countable values, p.m.f.
> - Continuous ↔ interval values, p.d.f., P(X = a) = 0 always

---

## Section: Probability Mass Function (p.m.f.) 🔴

### Core Idea
For a **discrete** random variable X taking values x_i with probabilities p_i, the **probability mass function** f(x) = P(X = x) lists the probability of each value. A valid p.m.f. must satisfy two conditions: non-negativity and total mass equal to 1.

> **In Simple Terms:** A p.m.f. is just a table that tells you the probability of each possible value. Like a histogram where the heights add up to 100%.

### Key Concepts

#### Definition
For discrete X taking values x₁, x₂, … with probabilities p₁, p₂, …, **f(x) = P(X = x) = p_i** when x = x_i. The function f(x) must satisfy:
1. **f(x) ≥ 0** for all x (probabilities are non-negative).
2. **Σ_i f(x_i) = 1** (total probability is one).

#### Discrete probability distribution
The full specification: the set of possible values along with their probabilities. May involve countably infinite values.

### Definitions
- **Probability Mass Function (p.m.f.)**: f(x) = P(X = x) for discrete X, satisfying f(x) ≥ 0 and Σ f(x_i) = 1. ⭐ (exam-important)

### Examples
**Example: Coin tossed until first head — X = number of tails preceding head.**
Sample points: H, TH, TTH, TTTH, …
| X | 0 | 1 | 2 | 3 | … | n |
|---|---|---|---|---|---|---|
| f(X = x) | 1/2 | (1/2)² | (1/2)³ | (1/2)⁴ | … | (1/2)^(n+1) |

p.m.f.: **f(x) = (1/2)^(x+1)** for x = 0, 1, 2, …
Verification: Σ = (1/2)/(1 − 1/2) = 1 ✓.

**Example: Discrete distribution table.**
| X | −3 | −1 | 1 | 3 |
|---|----|----|---|---|
| f | 0.216 | 0.432 | 0.288 | 0.064 |

(Sum = 1.0 ✓)

### ⚠️ Common Mistakes
- ❌ Mistake: Allowing f(x) < 0 → ✅ Correct: A function with any negative value cannot be a p.m.f.
- ❌ Mistake: Missing the total-mass-1 check → ✅ Correct: Always verify Σ f(x_i) = 1 before using a function as a p.m.f.

> **Quick Recall:**
> - p.m.f.: f(x) = P(X = x), discrete only
> - Two conditions: f(x) ≥ 0 and Σ f(x_i) = 1
> - Used to compute means, variances, expectations of discrete RVs

---

## Section: Probability Density Function (p.d.f.) 🔴

### Core Idea
For **continuous** random variables, single values have probability **zero**, so we cannot list "P(X = x)." Instead the **probability density function f(x)** assigns probability to *intervals* via integration. The probability of X falling in (c, d) is the area under f(x) between c and d.

> **In Simple Terms:** With continuous random variables you don't ask "what's the chance of exactly 1.7 cm of rain?" — that's always 0. You ask "what's the chance of between 1 and 2 cm?" — that's the area under the density curve between those bounds.

### Key Concepts

#### Definition
A non-negative continuous function f(x) is a p.d.f. of continuous RV X if:
1. **f(x) ≥ 0** for all x.
2. **∫_a^b f(x) dx = 1** where (a, b) is the range of X.

#### Probability of an interval
**P(c ≤ X ≤ d) = ∫_c^d f(x) dx** = area under the probability curve between vertical lines x = c and x = d.

#### Total area
The area under the entire probability curve equals 1; the curve never goes below the x-axis.

| Aspect | p.m.f. | p.d.f. |
|--------|--------|--------|
| Type of RV | Discrete | Continuous |
| Value at a point | Probability P(X=x) | Density (not probability) |
| Sum-to-1 | Σ f(x_i) = 1 | ∫ f(x) dx = 1 |
| P(X = c) | f(c) | 0 (always) |
| P(c ≤ X ≤ d) | Σ over [c,d] | ∫_c^d f(x) dx |

### Definitions
- **Probability Density Function (p.d.f.)**: A continuous non-negative function f(x) with ∫_a^b f(x) dx = 1; gives P(c ≤ X ≤ d) = ∫_c^d f(x) dx. ⭐ (exam-important)

### Examples
**Example: f(x) = k·e^(−3x) for x > 0, 0 otherwise — find k and P(0.5 ≤ X ≤ 1).**

1. Solve for k: ∫₀^∞ k·e^(−3x) dx = 1 → k · [−e^(−3x)/3]₀^∞ = k/3 = 1 → **k = 3**.
2. P(0.5 ≤ X ≤ 1) = ∫_{0.5}^1 3 e^(−3x) dx = [−e^(−3x)]_{0.5}^1 = −e^(−3) + e^(−1.5) ≈ **0.173**.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating f(c) as P(X = c) for continuous X → ✅ Correct: f(c) is a *density*; P(X = c) = 0 always for continuous RVs.
- ❌ Mistake: Forgetting f(x) can exceed 1 → ✅ Correct: Density values can be any non-negative number; only the *integral* must equal 1.

> **Quick Recall:**
> - Continuous: P(X = c) = 0; only intervals carry probability
> - p.d.f. f(x) ≥ 0 and ∫ f(x) dx = 1 over its range
> - P(c ≤ X ≤ d) = ∫_c^d f(x) dx (area under curve)

### Connections
- Builds on: [Probability Mass Function] (this chunk).
- Pre-requisite for: [Cumulative Distribution Function] (this chunk).
- Pre-requisite for: Normal distribution (Chunk 007) — defined via its p.d.f.

---

## Section: Cumulative Distribution Function (c.d.f.) 🔴

### Core Idea
The **c.d.f. F(x) = P(X ≤ x)** is the running total of probability up to value x. It works for both discrete and continuous variables. For continuous RVs, F(x) is the area under the p.d.f. to the left of x; differentiation recovers f(x).

> **In Simple Terms:** The c.d.f. answers "what's the chance the variable is at most x?" It always rises from 0 (at −∞) to 1 (at +∞).

### Key Concepts

#### Definition
**F(c) = P(X ≤ c) = ∫_{−∞}^c f(x) dx** (continuous) or Σ_{x_i ≤ c} f(x_i) (discrete).

#### Properties
1. F(−∞) = 0, F(+∞) = 1.
2. F is non-decreasing: a < b ⇒ F(a) ≤ F(b).
3. **P(a ≤ X ≤ b) = F(b) − F(a)**.
4. f(x) = dF(x)/dx (continuous, where derivative exists).
5. P(X = c) = F(c) − F(c⁻) = 0 for continuous X.

### Definitions
- **Cumulative distribution function (c.d.f.) F(x)**: P(X ≤ x); area under p.d.f. to the left of x. ⭐ (exam-important)

### Examples
**Example: c.d.f. of f(x) = 3e^(−3x) for x > 0.**
- For x < 0: F(x) = 0.
- For x ≥ 0: F(x) = ∫₀^x 3e^(−3t) dt = 1 − e^(−3x).

Re-evaluate P(0.5 ≤ X ≤ 1) using c.d.f.:
P = F(1) − F(0.5) = (1 − e^(−3)) − (1 − e^(−1.5)) = e^(−1.5) − e^(−3) ≈ **0.173** ✓.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating P(a < X < b) and P(a ≤ X ≤ b) as different for continuous RVs → ✅ Correct: They're equal because P(X = a) = P(X = b) = 0.

> **Quick Recall:**
> - F(x) = P(X ≤ x), monotone non-decreasing, 0 → 1
> - P(a ≤ X ≤ b) = F(b) − F(a)
> - f(x) = dF/dx (continuous)

### Connections
- Builds on: [Probability Density Function] (this chunk).

---

## Section: Moments — Definition and Importance 🔴

### Core Idea
**Moments** are expectations of integer powers of the random variable (or its centred version). They capture different features of a distribution: the first moment is the mean (location), the second central moment is the variance (spread), the third central moment relates to skewness, the fourth to kurtosis. A distribution is essentially characterised by its full set of moments.

> **In Simple Terms:** Moments are a sequence of numbers that progressively describe the shape of a distribution: mean, spread, asymmetry, peakedness. Knowing them is like knowing the silhouette of the distribution from far to near detail.

### Key Concepts

#### r-th moment about the origin (μ_r')
For discrete X: **μ_r' = E(x^r) = Σ x_i^r f(x_i)**.
For continuous X: **μ_r' = E(x^r) = ∫_{−∞}^∞ x^r f(x) dx**.
- r = 0: μ_0' = E(1) = 1.
- r = 1: μ_1' = E(x) = mean (often denoted μ).

#### r-th moment about the mean (μ_r)
For discrete X: **μ_r = E[(X − μ)^r] = Σ (x_i − μ)^r f(x_i)**.
- r = 1: μ_1 = 0 (always).
- r = 2: μ_2 = Var(x) = σ². ⭐
- r = 3: relates to skewness (asymmetry).
- r = 4: relates to kurtosis (tail heaviness).

#### Theorems on moments (stated)
1. **σ² = μ_2' − μ_1'²** (variance = second raw moment − square of mean).
2. **Var(aX + b) = a² · Var(X)** (location shift unchanged, scale squared).
3. **Chebyshev's theorem** (covered in next chunk).

#### Theorems on Mathematical Expectation (re-stated for completeness)
1. E(a + bX) = a + b·E(X).
2. E(a) = a (constant).
3. **E[Σ c_i ω(x_i)] = Σ c_i E[ω(x_i)]** (linearity).

### Definitions
- **r-th raw moment μ_r'**: E(x^r). ⭐ (exam-important)
- **r-th central moment μ_r**: E[(X − μ)^r]. ⭐ (exam-important)
- **Variance σ² = μ_2 = E[(X − μ)²] = E(x²) − [E(x)]²**. ⭐ (exam-important)

### Examples
**Example: Why "moment"?**
The term comes from physics. If f(x) is a "mass density" along the x-axis, then μ_1' (first moment about origin) is the centre of gravity, and μ_2' is related to the moment of inertia. Statistics borrows the geometric intuition.

**Visual (Fig. 26.4 in source):** Several distributions all have the same mean μ but progressively smaller variances: σ² = 5.26, 3.18, 1.66, 0.88 — high variance ↔ thick tails; low variance ↔ peaked at mean with thin tails.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing raw and central moments (μ_2' vs μ_2) → ✅ Correct: μ_2 = μ_2' − μ_1'² (variance is *not* the second raw moment by itself).
- ❌ Mistake: Using Var(X + c) ≠ Var(X) → ✅ Correct: Adding a constant shifts location only; Var(X + c) = Var(X) (b = 1, a² = 1 in the theorem).

> **Quick Recall:**
> - μ_r' = E(x^r) (about origin); μ_r = E[(X − μ)^r] (about mean)
> - μ_1' = mean; μ_2 = variance = σ²
> - σ² = E(x²) − [E(x)]²
> - Var(aX + b) = a² Var(X)

### Connections
- Builds on: [Variance and Functions of a Random Variable] (Chunk 003).
- Pre-requisite for: [Moment Generating Functions] (Chunk 005).

---

## Section: Check Your Progress 1 — p.m.f. validation 🟡

### Examples
**Q1: p.m.f. with parameter k.**
| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P | 0 | k | 2k | 2k | 3k | k² | 2k² | 7k²+k |

Σ P = 0 + k + 2k + 2k + 3k + k² + 2k² + 7k² + k = 10k² + 9k = 1 → **10k² + 9k − 1 = 0** → k = 1/10 (rejecting k = −1).

**Q2: Validity of p.m.f. candidates.**
- f(x) = (x − 2)/5 for x = 1..5: at x = 1, f = −1/5 < 0 → ❌ not valid (probability cannot be negative).
- f(x) = x²/30 for x = 0..4: all non-negative; sum = 0 + 1 + 4 + 9 + 16 = 30; 30/30 = 1 → ✓ valid p.m.f.
- f(x) = 1/5 for x = 0..5: 6 values × 1/5 = 6/5 ≠ 1 → ❌ not valid.

> **Quick Recall:**
> - Always validate p.m.f. via (i) f(x) ≥ 0 and (ii) Σ f(x) = 1.

### Open Questions
1. What does it mean for a distribution to *not* be characterised by its moments? (Some heavy-tailed distributions like the lognormal have moment problems — outside the syllabus.)
