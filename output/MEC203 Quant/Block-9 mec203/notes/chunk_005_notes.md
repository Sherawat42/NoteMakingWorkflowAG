# Chunk 005 — s² distribution, Central Limit Theorem, Unit 30 Estimation Intro and Properties
<!-- Pages: 41-50 -->
<!-- Source: chunk_005.txt -->

## Section: Sampling Distribution of s² 🟡
<!-- See chunk 004 for the joint derivation of x̄ and s² distributions -->

### Core Idea
The text completes the p.d.f. of the sample variance s² (in scaled form) — a chi-square-like density on the positive reals. Combined with the result from Chunk 004 that (n−1)s²/σ² ~ χ²(n−1), it confirms that s² follows a scaled χ² distribution.

### Key Concepts
- p.d.f. of s² (extracted from text):
$$u(s^2) = \frac{n^{(n−1)/2}}{(2σ^2)^{(n−1)/2}\,Γ((n−1)/2)}\,(s^2)^{(n−3)/2}\,\exp\left[-\frac{(n−1)s^2}{2σ^2}\right]\quad s^2 > 0$$

> **Quick Recall:**
> - s² is a scaled χ² distribution
> - (n−1)s²/σ² ~ χ²(n−1)

---

## Section: Central Limit Theorem 🔴

### Core Idea
The **Central Limit Theorem (CLT)** says that the sum (or mean) of a large number of independent random variables, each with finite mean and variance, is approximately normally distributed regardless of the original distribution. This rescues normal-theory inference for non-normal populations: with n large enough (typically n ≥ 30 in practice), x̄ is approximately normal even when the underlying x is not.

> **In Simple Terms:** The CLT is the magic behind why so many tests use the normal distribution. Even if the population isn't normal, if you average enough observations, the average behaves normally. That's why a lot of inferential statistics works in the wild.

### Key Concepts

#### Setup — Law of Large Numbers
For any positive constant c, the probability that x̄ falls within (μ − c, μ + c) is at least 1 − σ²/(nc²). As n → ∞, this tends to 1 — the **law of large numbers** (a foundation for CLT).

#### Statement of CLT
If x₁,…,xₙ are independently distributed random variables with E(xᵢ) = μᵢ and V(xᵢ) = σᵢ², then under certain general conditions, the sum
$$S_n = x_1 + x_2 + \ldots + x_n$$
is asymptotically normal with mean μ = Σμᵢ and standard deviation σ = √(Σσᵢ²).

#### Practical Form (iid version)
For an iid sample with E(xᵢ) = μ, Var(xᵢ) = σ², the standardized mean
$$Z_n = \frac{x̄ − μ}{σ/\sqrt{n}} \xrightarrow{D} N(0, 1)$$
where →ᴰ denotes convergence in distribution. (The text formalises this in Unit 30 Section 30.5.3.)

#### Conventions
- **n ≥ 30** is the common rule of thumb for CLT to "kick in" in practice.
- Sampling done with replacement (or n ≪ N).

### Definitions
- **Central Limit Theorem (CLT)** ⭐: under general conditions, the sum of n independent random variables is asymptotically normal as n → ∞.
- **Law of Large Numbers**: the probability that x̄ lies near μ tends to 1 as n increases.

> **Quick Recall:**
> - CLT: x̄ → N(μ, σ²/n) as n → ∞
> - Rule of thumb: n ≥ 30
> - Works for sums and averages, regardless of underlying distribution
> - Foundation of normal-test approximation for many distributions (binomial, Poisson, etc.)

### Connections
- Builds on: law of large numbers.
- Foundation for: large-sample tests in Unit 31 (use of normal critical values for large n).

---

## Section: Unit 29 — Let Us Sum Up + Key Words 🟢

### Definitions (Glossary)
| Term | Definition |
|---|---|
| **Central Limit Theorem** ⭐ | iid sum is asymptotically normal |
| **Chi-square Distribution** ⭐ | square of standard normal = χ²(1) |
| **F Distribution** ⭐ | F = (X/n₁)/(Y/n₂) for independent χ²s |
| **Fisher's t Distribution** ⭐ | t = T/√(χ²/n), T ~ N(0,1) |
| **Standard Normal Distribution** | continuous variable, mean 0, variance 1 |
| **Student's t Distribution** ⭐ | t = (x̄−μ)/(σ/√n) (text uses σ — typo for s); df = n−1 |

---

## Section: Unit 29 Worked Exercises 🔴

### Examples

#### Example: 9:3:3:1 Goodness-of-Fit Test
- 1600 bins predicted to split 9:3:3:1 across groups A, B, C, D.
- Observed: 882, 313, 287, 118.
- Expected: E_A = (9/16)·1600 = 900; E_B = E_C = (3/16)·1600 = 300; E_D = (1/16)·1600 = 100.
- Compute χ² = Σ(Oᵢ − Eᵢ)²/Eᵢ ≈ **4.7266**.
- Tabulated χ²(0.05, 3) = **7.815**.
- 4.7266 < 7.815 → **accept H₀** (theory is supported).

#### Example: t-Test for Bulb Life
- CEO claim: average bulb life = 300 days.
- Sample n = 15, x̄ = 290, s = 50.
- Test stat: t = (290 − 300)/(50/√15) = −10/12.910 = **−0.7745966**.
- df = n − 1 = 14.
- Cumulative probability = **0.226** → 22.6% chance of seeing x̄ ≤ 290 if μ = 300 is true.

> **Quick Recall:**
> - 9:3:3:1 problem: χ² = 4.73 vs critical 7.82 → accept H₀
> - Bulb-life t = −0.77 (df=14) → P = 0.226 → don't reject

---

## Section: Unit 30 — Estimation: Objectives and Introduction 🟢

### Core Idea
Unit 30 develops **point estimation** and the **interval estimation** preview, then characterises *good* estimators. The opening positions estimation in the broader inference framework: given a sample, we either (i) estimate unknown parameters (estimation problem) or (ii) test claims about parameter values (hypothesis-testing problem). Unit 30 covers (i); Unit 31 covers (ii).

### Key Concepts
- **Statistical inference**: drawing population conclusions from a sample.
- **Estimation problem**: no information about the parameter; produce an estimate.
- **Hypothesis testing problem**: test how well a hypothesised parameter value fits the data.
- **Point estimation**: single numerical estimate (a function of sample observations = an *estimator*).
- **Interval estimation**: an interval likely to contain the parameter at a stated confidence level.

> **Quick Recall:**
> - Inference splits into estimation + hypothesis testing.
> - Point estimate = single number; interval estimate = range with confidence.

### Connections
- Continues the framework opened in Unit 28 (sampling theory) and Unit 29 (sampling distributions); the latter provides the distribution machinery used here.

---

## Section: Theory of Estimation — Parameter Space 🟡

### Core Idea
The **parameter space Θ** is the set of all admissible values of an unknown parameter θ. The functional form of the population distribution is usually known up to θ; the family of distributions is {f(x; θ): θ ∈ Θ}. An *estimator* is a function of sample values whose distribution should be concentrated as closely as possible around the true value of the parameter.

### Key Concepts
- p.d.f. f(x, θ), with θ ∈ Θ; e.g., for X ~ N(μ, σ²): Θ = {(μ, σ²): −∞ < μ < ∞, 0 < σ² < ∞}.
- For known σ²: Θ reduces to {μ: −∞ < μ < ∞}.
- General family: {f(x; θ₁,…,θ_k)}.
- Estimator T = θ̂(x₁,…,xₙ) — function of sample observations.

### Definitions
- **Parameter space (Θ)** ⭐: set of all possible values of the unknown parameter(s).
- **Estimator**: a function of sample observations whose distribution is concentrated around the true parameter.

> **Quick Recall:**
> - Θ = admissible parameter values
> - Family of distributions {f(x;θ): θ ∈ Θ}
> - Estimator = a function of sample data

---

## Section: Characteristics of Estimators 🔴

### Core Idea
Four standard criteria classify good estimators: **Unbiasedness**, **Consistency**, **Efficiency**, and **Sufficiency**. They form the standard checklist when judging an estimator.

### Subsection: Unbiasedness 🔴

#### Definition
T_n is unbiased for θ if E(T_n) = θ for all θ ∈ Θ.

#### Examples
1. **Sample mean** x̄ for population mean μ: E(x̄) = μ ⇒ unbiased.
2. **Sample proportion** for binomial parameter θ: with X ~ Binomial(n, θ), E(X/n) = (1/n)·E(X) = (1/n)·nθ = θ ⇒ X/n unbiased.
3. **Sample variance** S² for σ² of an *infinite* population: E(S²) = σ². However, S² is **not** an unbiased estimator of finite-population variance, and S is **not** an unbiased estimator of σ (square root creates bias).

#### Bias
$$b(θ) = E(T_n) − τ(θ)$$
- b(θ) > 0 → positively biased; b(θ) < 0 → negatively biased.

#### Caveats
- Unbiasedness is **not** preserved under non-linear functional transformations: ψ(θ̂) is generally biased even when θ̂ is unbiased.
- Unbiased estimators are **not unique** — multiple may exist.
- Unbiasedness is a property defined for finite n.

> **Quick Recall:**
> - x̄ is unbiased for μ; X/n unbiased for binomial p.
> - S² unbiased for σ² of infinite population; S biased for σ.
> - Bias = E(estimator) − parameter.

### Subsection: Consistency 🔴

#### Definition
T_n is consistent for τ(θ) if T_n →ᴾ τ(θ) — that is, for every ε > 0, η > 0, there exists m such that for all n ≥ m: P[|T_n − τ(θ)| < ε] > 1 − η.

#### Khinchin's Weak Law of Large Numbers
For an iid sample with finite mean: x̄_n →ᴾ E(xᵢ) = μ. Hence the sample mean is **always** consistent for μ.

#### Sufficient Conditions for Consistency
For a sequence {T_n}:
1. E(T_n) → τ(θ) as n → ∞ (asymptotic unbiasedness)
2. Var(T_n) → 0 as n → ∞.
Then T_n is consistent.

#### Caveats
- Many consistent estimators may exist for the same parameter; e.g., T_n + a/φ(n), T_n·{1 + a/φ(n)} for any constant a, increasing function φ.
- Consistency is a *large-n* property; it says nothing about finite-n behaviour.

> **Quick Recall:**
> - Consistency = convergence in probability to the parameter.
> - Sufficient conditions: asymptotic unbiased + Var → 0.
> - x̄ is always consistent for μ (Khinchin's WLLN).

### Subsection: Efficiency 🔴

#### Definition
Among multiple consistent (asymptotically normal) estimators, the one with **smallest asymptotic variance** is most efficient. T is the *best* estimator if it is consistent, asymptotically normal, and has the smallest avar(T) among all such estimators.

#### Most Efficient Estimator
If among consistent estimators there exists one whose sampling variance is *less* than any rival's, it is called the **most efficient estimator**.

#### Efficiency E
$$E = \frac{V_1}{V_2} \le 1$$
where V₁ = variance of most efficient estimator, V₂ = variance of any rival.

For a set T₁,…,T_n with Var(T) = min:
$$E_i = \frac{Var(T)}{Var(T_i)} \le 1$$

#### Minimum Variance Unbiased Estimator (MVUE)
T is **MVUE** of τ(θ) if:
1. T is unbiased for τ(θ) for all θ ∈ Θ.
2. Among the class of all unbiased estimators of τ(θ), T has the smallest variance.

##### Important Theorems for MVUE
- **Uniqueness**: if T₁ and T₂ are both MVUE for ψ(θ), then T₁ = T₂.
- **Correlation bound**: if T₁, T₂ are unbiased with efficiencies e₁, e₂ and correlation ρ:
$$\sqrt{e_1 e_2} − \sqrt{(1 − e_1)(1 − e_2)} \le ρ \le \sqrt{e_1 e_2} + \sqrt{(1 − e_1)(1 − e_2)}$$
- **MVUE correlation rule**: if T₁ is MVUE and T₂ is any unbiased estimator with efficiency e₀, then ρ(T₁, T₂) = √e₀.

##### Worked Sketch — x̄ is MVUE of μ for normal population
- Density: f(x) = (1/(σ√(2π)))·exp[−(x−μ)²/(2σ²)].
- ln f(x) = −ln(σ√(2π)) − (x − μ)²/(2σ²).
- ∂lnf/∂μ = (x − μ)/σ².
- E[(∂lnf/∂μ)²] = E[(x − μ)²]/σ⁴ = 1/σ².
- Cramer-Rao bound (preview, Chunk 006): Var(estimator) ≥ 1/(n·E[(∂lnf/∂μ)²]) = σ²/n.
- Var(x̄) = σ²/n attains this bound ⇒ **x̄ is MVUE of μ**.

### Definitions
- **Unbiased estimator** ⭐: E(T) = θ.
- **Consistent estimator** ⭐: T_n →ᴾ θ as n → ∞.
- **Efficient estimator** ⭐: smallest asymptotic variance among consistent, asymptotically normal estimators.
- **Most Efficient Estimator**: minimal sampling variance among rivals.
- **Minimum Variance Unbiased Estimator (MVUE)** ⭐: unbiased + smallest variance among all unbiased.
- **Bias b(θ)** = E(T) − τ(θ).

### ⚠️ Common Mistakes
- ❌ Mistake: assuming ψ(θ̂) is unbiased whenever θ̂ is. → ✅ Correct: unbiasedness fails under non-linear transformations.
- ❌ Mistake: thinking "consistent" means "unbiased". → ✅ Correct: a consistent estimator may be biased for finite n; it just gets better as n grows.

> **Quick Recall:**
> - Four properties of a good estimator: unbiased, consistent, efficient, sufficient.
> - x̄ is unbiased + consistent + MVUE for normal μ.
> - Efficiency E = V_min / V_estimator ≤ 1.
> - Sample variance S² is unbiased for σ² of infinite population only.

### Connections
- Builds on: sampling distribution (Chunks 002–004).
- Continues into: Sufficiency, Cramer-Rao, Rao-Blackwell, asymptotic properties (Chunk 006).

<!-- Continues in chunk 006 -->
