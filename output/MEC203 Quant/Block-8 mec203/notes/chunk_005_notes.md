# Chunk 005 — Moments, Chebyshev's Theorem, MGFs, Joint Distribution
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt -->

## Section: Higher-order Moments — Skewness and Chebyshev's Theorem 🔴
<!-- See chunk 004 for start of Moments -->

### Core Idea
The **third central moment** (μ_3) describes the **symmetry / skewness** of a distribution. The variance + Chebyshev's theorem together give a *distribution-free* bound on how often a random variable deviates from its mean — a remarkable fact with no shape assumption.

> **In Simple Terms:** Variance only tells you how spread out a distribution is. The third moment tells you whether the spread is symmetric (μ_3 = 0) or lopsided to one side. Chebyshev says: no matter what the distribution looks like, it's "rare" for X to be many σ's away from μ — and quantifies how rare.

### Key Concepts

#### Skewness via μ_3
The third moment about the mean describes asymmetry: μ_3 = 0 for symmetric distributions; μ_3 > 0 for right-skewed (tail extends right); μ_3 < 0 for left-skewed.

#### Chebyshev's Theorem
If X has mean μ and variance σ² (with σ ≠ 0), then for any constant k:
**P(|X − μ| < k·σ) ≥ 1 − 1/k²**.

Equivalently, **P(|X − μ| ≥ k·σ) ≤ 1/k²**.

This is **distribution-free** — no normality assumption. Crude but universal.

| k | Lower bound on P(|X − μ| < kσ) |
|---|--------------------------------|
| 1 | 0 (trivial) |
| 2 | 1 − 1/4 = 0.75 |
| 3 | 1 − 1/9 ≈ 0.889 |
| 4 | 1 − 1/16 = 0.9375 |

(Compare with normal: P(|X − μ| < 2σ) ≈ 0.9545; Chebyshev's 0.75 is much weaker but holds for *any* distribution.)

### Definitions
- **Chebyshev's Theorem**: For any RV X with mean μ and variance σ², P(|X − μ| < kσ) ≥ 1 − 1/k². ⭐ (exam-important)
- **Skewness**: Asymmetry of a distribution; μ_3 ≠ 0 indicates skew.

> **Quick Recall:**
> - μ_3 governs skewness; μ_3 = 0 ⇒ symmetric distribution
> - Chebyshev: P(|X − μ| ≥ kσ) ≤ 1/k² (any distribution)
> - At k = 2 ⇒ at most 25% of mass beyond 2σ

---

## Section: Moment Generating Function (MGF) 🔴

### Core Idea
The **moment generating function** M_X(t) = E(e^(tX)) is a single function of t whose Maclaurin coefficients are exactly the moments of X. So the MGF "packages" all moments together — by differentiating M_X(t) r times at t = 0 you read off the r-th raw moment μ_r'. It's the standard tool for deriving the mean, variance, and key properties of binomial, Poisson, and normal distributions.

> **In Simple Terms:** The MGF is a generating function — a magical formula whose Taylor series expansion gives you all the moments of the distribution in one shot. Differentiate r times, plug in t = 0, and out pops μ_r'.

### Key Concepts

#### Definition
- Discrete: **M_X(t) = E(e^(tX)) = Σ_i e^(t·x_i) · f(x_i)**.
- Continuous: **M_X(t) = ∫_{−∞}^∞ e^(tx) · f(x) dx**.

t is in a neighbourhood of 0; the MGF is required to exist there.

#### Why "moment generating"?
Use Maclaurin's series: e^(tx) = 1 + tx + (tx)²/2! + (tx)³/3! + …
So **M_X(t) = 1 + t·μ_1' + t²/2! · μ_2' + t³/3! · μ_3' + … + t^r/r! · μ_r' + …**
The coefficient of t^r/r! in M_X(t) is **μ_r'** (the r-th raw moment).

#### Recovery formula
**μ_r' = d^r M_X(t)/dt^r |_(t=0)**.

#### Key MGF transformation rules
For constants a, b:
1. **M_(X+a)(t) = e^(at) · M_X(t)**.
2. **M_(bX)(t) = M_X(bt)**.
3. **M_((X+a)/b)(t) = e^((a/b)t) · M_X(t/b)**.

Special case (standardisation): with a = −μ, b = σ:
**M_((X−μ)/σ)(t) = e^(−μt/σ) · M_X(t/σ)** — used to get the standardised variable's MGF.

### Definitions
- **Moment Generating Function (MGF)**: M_X(t) = E(e^(tX)). ⭐ (exam-important)
- **Generating relation**: μ_r' = M_X^(r)(0) = the r-th derivative of M_X(t) at t = 0. ⭐ (exam-important)

### Mechanisms / Processes
Step-by-step recipe to find moments via MGF:
1. Write M_X(t) = E(e^(tX)) — sum or integral.
2. Compute closed-form M_X(t) (often using known series like geometric, exponential).
3. Differentiate once: μ_1' = M'(0) = mean.
4. Differentiate twice: μ_2' = M''(0) = E(X²); then σ² = μ_2' − μ_1'².

### Examples
**Example: f(x) = e^(−x) for x > 0 (exponential distribution).**
M_X(t) = ∫₀^∞ e^(tx) e^(−x) dx = ∫₀^∞ e^(−(1−t)x) dx = **1/(1 − t)** for t < 1.

Maclaurin expansion: 1/(1 − t) = 1 + t + t² + t³ + … = Σ t^r = Σ (r!) · t^r/r!.
So **μ_r' = r!** for r = 0, 1, 2, … (Mean = 1, Var = 2! − 1² = 1, etc.).

**Example (Check Your Progress 2): X ~ p.m.f. f(x) = (1/8) · ³C_x for x = 0,1,2,3.**
M_X(t) = Σ_{x=0..3} e^(tx) · (1/8) · ³C_x = (1/8) · (1 + e^t)³ (binomial expansion).
- M'(t) at t = 0: μ_1' = (3/8)(1+1)² = 12/8 = **3/2** = mean.
- M''(t) at t = 0: μ_2' = **3** = E(X²).
- σ² = 3 − (3/2)² = 3 − 9/4 = **3/4**.

> **Quick Recall:**
> - **M_X(t) = E(e^(tX))**
> - μ_r' = r-th derivative at t = 0
> - Linear shifts: M_(X+a) = e^(at) M_X(t); M_(bX) = M_X(bt)

### Connections
- Builds on: [Moments — Definition] (Chunk 004).
- Pre-requisite for: [MGF of Binomial / Poisson / Normal] (Chunks 006–007).

---

## Section: Unit 26 Summary, Key Words, Exercises 🟢

### Definitions (Key Words — verbatim restatements ⭐)
- **Continuous Random Variable**: A random variable that can take any value within its range.
- **Discrete Random Variable**: A random variable that takes only countable values, with no possible value located between two adjacent ones.
- **Probability Distribution**: Statement specifying the set of possible values together with their respective probabilities.
- **Probability Mass Function (p.m.f.)**: f(x) = P(X = x) for discrete X, satisfying f(x) > 0 and Σ f(x_i) = 1.
- **Probability Density Function (p.d.f.)**: A continuous non-negative function f(x) for continuous X, giving P(c ≤ X ≤ d) = ∫_c^d f(x) dx, with ∫_a^b f(x) dx = 1 over the range (a, b).

### Examples (Exercise solutions)

**Q1: Fair coin tossed twice; X = number of heads. Find R(X) and p.m.f. P_X.**
Sample space S = {HH, HT, TH, TT}. R(X) = {0, 1, 2}.
- P_X(0) = 1/4 (TT)
- P_X(1) = 2/4 = 1/2 (HT, TH)
- P_X(2) = 1/4 (HH)

**Q2: Find r given p.m.f. P(Y).**
| Y | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P | 0 | 2r | 3r | 6r² |

Σ P = 1 ⇒ 0 + 2r + 3r + 6r² = 1 ⇒ 6r² + 5r − 1 = 0.
Factoring: (6r − 1)(r + 1) = 0 ⇒ r = 1/6 or r = −1. Reject r = −1 (probability constraint). **r = 1/6**.

**Q3: Two conditions for p.d.f.**
1. f(x) ≥ 0 for all x.
2. Total area under f(x) equals 1.

**Q4: Difference between p.m.f. and p.d.f.**
- p.d.f. describes a **continuous** probability distribution.
- p.m.f. describes a **discrete** probability distribution.

> **Quick Recall:**
> - Always end p.m.f./p.d.f. validity check with Σ = 1 / ∫ = 1.
> - Reject negative or out-of-range solutions to algebraic constraints.

---

## Section: Joint Probability Distribution — Discrete and Continuous 🔴

### Core Idea
When more than one random variable is involved, we use a **joint distribution** f(x, y) = P(X = x, Y = y) (discrete) or its continuous analogue f(x, y) (a 2-D density). The two-dimensional p.m.f./p.d.f. encodes the *complete* statistical relationship between X and Y. Independence of X, Y is the special case where f(x, y) factorises into f_X(x) · f_Y(y).

> **In Simple Terms:** Where one variable's distribution is a curve, two variables' joint distribution is a surface above the (x, y) plane. The "volume" under that surface is 1.

### Key Concepts

#### Discrete joint p.m.f.
For discrete X, Y: **f(x, y) = P(X = x, Y = y)**. Conditions:
1. f(x, y) ≥ 0 for every pair (x, y) in the domain.
2. **ΣΣ f(x, y) = 1** — double sum over all (x, y).

#### Continuous joint p.d.f.
For continuous X, Y: f(x, y) is a non-negative bivariate function with:
1. f(x, y) ≥ 0 for −∞ < x < ∞, −∞ < y < ∞.
2. **∫∫ f(x, y) dx dy = 1**.
3. P[(X, Y) ∈ A] = ∫∫_A f(x, y) dx dy for any region A.

#### Joint cumulative distribution (c.d.f.)
- Discrete: **F(x, y) = P(X ≤ x, Y ≤ y) = Σ_{s≤x} Σ_{t≤y} f(s, t)**.
- Continuous: F(x, y) = ∫_{−∞}^x ∫_{−∞}^y f(s, t) ds dt; recover density via **f(x, y) = ∂²F(x, y)/∂x∂y**.

#### Independence
**X and Y independent ⇔ f(x, y) = f_X(x) · f_Y(y)** for all (x, y).
Generalises: random variables X₁, …, X_n are mutually independent if every subset's joint p.m.f./p.d.f. equals the product of marginals.

### Definitions
- **Joint probability distribution f(x, y)**: P(X = x, Y = y) for discrete RVs; f(x, y) ≥ 0 and ΣΣ f = 1. ⭐ (exam-important)
- **Joint p.d.f.**: Continuous bivariate analogue with f ≥ 0 and ∫∫ f dx dy = 1. ⭐ (exam-important)
- **Independence (joint)**: f(x, y) = f_X(x) · f_Y(y). ⭐ (exam-important)

### Examples
**Example: f(x, y) = k·xy for x, y ∈ {1, 2, 3} — find k.**
Sum over all 9 cells:
ΣΣ kxy = k · (Σ_x x)(Σ_y y) = k · 6 · 6 = 36k = 1 ⇒ **k = 1/36**.

**Example: 100-word corpus.**
Word | c(w) | P(w) | x = length | y = vowels
---|---|---|---|---
Shall | 5 | 0.05 | 5 | 1
Up | 8 | 0.08 | 2 | 1
Next | 5 | 0.05 | 4 | 1
As | 5 | 0.05 | 2 | 1
Fore | 3 | 0.03 | 4 | 2
To | 10 | 0.10 | 2 | 1
We | 12 | 0.12 | 2 | 1
Some | 8 | 0.08 | 4 | 2
Will | 30 | 0.30 | 4 | 1
BBC | 14 | 0.14 | 3 | 0

Joint p.m.f. f(x, y) = P(X = x, Y = y), e.g.:
- f(4, 2) = P(Fore) + P(Some) = 0.03 + 0.08 = **0.11**.
- f(3, 0) = P(BBC) = **0.14**.
- f(2, 1) = P(Up) + P(As) + P(To) + P(We) = 0.08 + 0.05 + 0.10 + 0.12 = **0.35**.

| | x = 2 | x = 3 | x = 4 | x = 5 |
|--|------|-------|-------|-------|
| y = 0 | 0 | 0.14 | 0 | 0 |
| y = 1 | 0.35 | 0.30 | 0.05 | 0.05 |
| y = 2 | 0 | 0 | 0.11 | 0 |

(Verify: total = 1.00 ✓.)

### ⚠️ Common Mistakes
- ❌ Mistake: Validating only Σ_x f(x, y) = 1 instead of the **double sum** → ✅ Correct: Joint p.m.f. requires Σ_x Σ_y f(x, y) = 1.
- ❌ Mistake: Assuming independence whenever f(x, y) is given → ✅ Correct: Must verify factorisation f(x, y) = f_X(x) f_Y(y) for *all* (x, y).

> **Quick Recall:**
> - Joint p.m.f./p.d.f. — 2-D analogue of single-variable case
> - Total mass = 1 (double sum or double integral)
> - Independence ⇔ product of marginals

### Connections
- Builds on: [Probability Mass Function] and [Probability Density Function] (Chunk 004).
- Pre-requisite for: [Marginal Distribution] (Chunk 006).

### Open Questions
1. How does conditional density f(y|x) = f(x, y)/f_X(x) generalise the discrete conditional probability formula?
