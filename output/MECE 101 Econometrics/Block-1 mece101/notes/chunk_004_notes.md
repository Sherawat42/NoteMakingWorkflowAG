# Chunk 004 — Unit 2: Asymptotic Properties, LLN, CLT, Hypothesis Testing & Estimation Methods
<!-- Pages: 29–39 -->
<!-- Source: chunk_004.txt -->
<!-- Continues from: Estimator Properties — Sufficiency, MSE (Chunk 003) -->
<!-- Continues into: Unit 2 CYP Answers + Unit 3 Matrix Algebra (Chunk 005) -->

## Section: Asymptotic Properties of Estimators 🔴
<!-- See Chunk 003 for finite-sample properties (Unbiasedness, Efficiency, Sufficiency) -->

### Core Idea
Asymptotic properties describe the behaviour of estimators as sample size n approaches infinity. Unlike finite-sample properties, they are mathematically tractable and applicable even when exact finite-sample results are unavailable. Two key asymptotic properties are: asymptotic unbiasedness (bias vanishes as n→∞) and asymptotic consistency (both bias and variance vanish as n→∞).

> **In Simple Terms:** Asymptotic properties are what happens "in the long run" — given enough data, a consistent estimator will eventually home in on the true value. It's like saying "with enough practice, you'll get it right."

### Key Concepts

#### Asymptotic Unbiasedness
An estimator T is **asymptotically unbiased** if lim_{n→∞} E(T) = Ø. An estimator that was biased for finite n can become unbiased as n→∞.

#### Asymptotic Consistency
An estimator T is **consistent** (in the asymptotic sense) if both:
1. lim_{n→∞} [E(T) - Ø] = 0 (bias vanishes)
2. lim_{n→∞} Var(T) = 0 (variance vanishes)

Both conditions must hold simultaneously for consistency.

### Definitions
- **Asymptotic Unbiasedness**: lim_{n→∞} E(T) = Ø; the bias of estimator T vanishes as sample size grows to infinity. ⭐ (exam-important)
- **Asymptotic Consistency**: lim_{n→∞} [E(T) - Ø] = 0 AND lim_{n→∞} Var(T) = 0; both bias and variance approach zero as n→∞. ⭐ (exam-important)

### Quick Recall
> **Quick Recall:**
> - Asymptotic unbiasedness: bias → 0 as n → ∞
> - Consistency (asymptotic): bias → 0 AND variance → 0 as n → ∞
> - Consistency is stronger than asymptotic unbiasedness (requires two conditions)

### Connections
- Builds on: Finite-sample properties (Chunk 003)
- Is prerequisite for: Law of Large Numbers (below), OLS large-sample theory (Block 2)

---

## Section: Law of Large Numbers (Weak & Strong) 🔴

### Core Idea
The Law of Large Numbers (LLN) formalises the intuition that with more data, the sample mean converges to the population mean. There are two versions: the Weak LLN (convergence in probability) and the Strong LLN (almost sure convergence). Both require the samples to be i.i.d. (independent and identically distributed).

> **In Simple Terms:** Flip a fair coin many times. At first, you might get 70% heads. But as you flip more and more, the fraction of heads will converge to 50%. That's the Law of Large Numbers at work.

### Key Concepts

#### Weak Law of Large Numbers (WLLN)
Let X₁, X₂, ..., Xₙ be i.i.d. random variables each with mean µ and standard deviation σ. Let Aₙ = (X₁ + X₂ + ... + Xₙ)/n.

**WLLN**: For all α > 0:
lim_{n→∞} P(|Aₙ - µ| > α) = 0
or equivalently: lim_{n→∞} P(|Aₙ - µ| < α) = 1

The sample mean **converges in probability** to the population mean.

#### Strong Law of Large Numbers (SLLN)
**SLLN**: lim_{n→∞} P(Aₙ = µ) = 1, or equivalently lim_{n→∞} P(|Aₙ - µ| = 0) = 1

The sample mean **converges almost surely** (with probability 1) to the population mean. The SLLN is a stronger statement than the WLLN.

### Definitions
- **Weak Law of Large Numbers (WLLN)**: For i.i.d. {Xᵢ} with mean µ: lim_{n→∞} P(|Aₙ - µ| < α) = 1 for all α > 0; convergence in probability. ⭐ (exam-important)
- **Strong Law of Large Numbers (SLLN)**: For i.i.d. {Xᵢ} with mean µ: lim_{n→∞} P(Aₙ = µ) = 1; almost sure convergence. ⭐ (exam-important)
- **i.i.d. (Independent and Identically Distributed)**: A collection of random variables where each has the same probability distribution as the others, and all are mutually independent. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing WLLN and SLLN — SLLN is strictly stronger (almost sure convergence vs convergence in probability) → ✅ Correct: SLLN requires the more demanding condition
- ❌ Mistake: Thinking LLN requires a normal distribution → ✅ Correct: LLN applies for any distribution with finite mean µ

### Quick Recall
> **Quick Recall:**
> - WLLN: P(|Aₙ - µ| < α) → 1 as n → ∞ [convergence in probability]
> - SLLN: P(Aₙ = µ) = 1 as n → ∞ [almost sure convergence; stronger]
> - Both require i.i.d. with finite mean µ

### Connections
- Builds on: Consistency (Chunk 003), Asymptotic properties (above)
- Is prerequisite for: Central Limit Theorem (below)
- Connects to: Sampling distribution concept revisited via CLT

---

## Section: Central Limit Theorem (CLT) 🔴

### Core Idea
The Central Limit Theorem (CLT) states that for i.i.d. random variables, the distribution of the sample mean approaches a normal distribution as n→∞, regardless of the original population distribution. This is why hypothesis tests and confidence intervals based on normality work even when the data is not normally distributed — as long as n is large enough.

> **In Simple Terms:** Even if individuals' heights, incomes, or error terms follow a weird distribution, the *average* of a large sample will always look like a bell curve (normal distribution). That's the CLT — it's why statistics works so broadly.

### Key Concepts

#### The CLT Statement
Let X₁, X₂, ..., Xₙ be i.i.d. random variables with mean µ and variance σ², then as n → ∞:

**X̄ ~ N(µ, σ²/n)**

The sample mean is approximately normal with mean µ and variance σ²/n.

#### Standardised Normal Variable (Z-statistic)
By subtracting the mean and dividing by the standard error:

**Z = (X̄ - µ) / (σ/√n)**

As n→∞, Z → N(0,1) (standard normal). This Z-statistic is used in hypothesis tests.

**Coin-toss example from source**: Coin tossed n=30 times; heads = 13; x̄ = 13/30 = 0.43. To test if coin is unbiased (p=0.5), compute Z = (x̄ - p₀) / (σ/√n) and compare to critical values of N(0,1).

### Definitions
- **Central Limit Theorem (CLT)**: For i.i.d. {Xᵢ} with mean µ and variance σ², X̄ → N(µ, σ²/n) as n → ∞; the sample mean approaches normality regardless of population distribution. ⭐ (exam-important)
- **Standard Normal Variable (Z)**: Z = (X̄ - µ)/(σ/√n); approaches N(0,1) as n → ∞; the basis for Z-tests. ⭐ (exam-important)

### Examples
**Example: Coin-toss test**
- n = 30 tosses, heads = 13, x̄ = 0.43
- If coin is unbiased: p = 0.5, σ = √(p(1-p)) = 0.5
- Z = (0.43 - 0.5)/(0.5/√30) = −0.07/0.091 ≈ −0.77
- Since |Z| < 1.96 (at α=5%, two-tailed), fail to reject H₀; coin appears unbiased

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking CLT means population must be normal → ✅ Correct: CLT works for ANY population distribution with finite mean and variance
- ❌ Mistake: Applying CLT to very small samples (n < 30) → ✅ Correct: CLT is an asymptotic result; for small n, assumptions about population distribution matter more

### Quick Recall
> **Quick Recall:**
> - CLT: X̄ ~ N(µ, σ²/n) as n → ∞ (regardless of population distribution)
> - Z = (X̄ - µ)/(σ/√n) → N(0,1)
> - CLT underpins ALL large-sample hypothesis testing in econometrics

### Connections
- Builds on: WLLN and SLLN (above), Sampling distribution (Chunk 003)
- Is prerequisite for: Hypothesis Testing (below), t-tests and F-tests in OLS (Block 2)

---

## Section: Hypothesis Testing — Null/Alternative, Type Errors, Level of Significance 🔴

### Core Idea
Hypothesis testing is the formal procedure for using sample data to evaluate claims about population parameters. A null hypothesis (H₀) is either rejected or not rejected based on a test statistic. Two types of errors are possible: rejecting a true H₀ (Type-I) or not rejecting a false H₀ (Type-II). The significance level α controls the maximum allowed probability of Type-I error.

> **In Simple Terms:** Think of a trial. H₀ = "innocent until proven guilty". Type-I error = convicting an innocent person. Type-II error = letting a guilty person go free. The significance level α = the maximum chance you're willing to wrongly convict.

### Key Concepts

#### Simple vs Composite Hypothesis
- **Simple hypothesis**: Completely specifies all parameters (e.g., H: µ = µ₀, σ² = σ₀²)
- **Composite hypothesis**: Leaves at least one parameter unspecified or in a range (e.g., H: µ = µ₀ [σ² unspecified], or H: µ < µ₀)

#### Null and Alternative Hypothesis
- **H₀ (Null)**: The hypothesis whose validity is tested; asserts no relationship or a specific value. We either "reject" or "do not reject" H₀ — we never "accept" H₀.
- **H₁ (Alternative)**: Accepted/rejected indirectly via what happens to H₀.

#### One-Tailed vs Two-Tailed Tests
| Test Type | H₁ Form | Description |
|-----------|----------|-------------|
| Two-tailed | H₁: µ ≠ µ₀ | Reject in either tail |
| Right-tailed | H₁: µ > µ₀ | Reject only in right tail |
| Left-tailed | H₁: µ < µ₀ | Reject only in left tail |

#### Type-I and Type-II Errors
| Decision | H₀ True | H₀ False |
|----------|---------|----------|
| Accept H₀ | Correct | **Type-II Error** |
| Reject H₀ | **Type-I Error** | Correct |

Type-I error is considered more serious — we try to minimise it by setting α.

#### Level of Significance (α), Critical Region & p-value
- **Level of significance (α)**: Maximum allowed probability of committing Type-I error. Commonly α = 5% or 1%.
- **Confidence coefficient (1-α)**: Probability of making the correct decision = 1 - P(Type-I error).
- **Critical region**: The set of test statistic values for which H₀ is rejected; separates acceptance from rejection regions.
- **p-value**: The lowest level of significance at which H₀ can be rejected; if p-value < α, reject H₀.

### Definitions
- **Null Hypothesis (H₀)**: An assertion tested for possible rejection based on sample observations. ⭐ (exam-important)
- **Alternative Hypothesis (H₁)**: Condition opposite to H₀; accepted/rejected indirectly. ⭐ (exam-important)
- **Simple Hypothesis**: A hypothesis that completely specifies all parameters of the population.
- **Composite Hypothesis**: A hypothesis that leaves at least one parameter unspecified or in a range.
- **Type-I Error**: Error of rejecting H₀ when it is actually true (false positive). ⭐ (exam-important)
- **Type-II Error**: Error of accepting H₀ (not rejecting it) when it is actually false (false negative). ⭐ (exam-important)
- **Level of Significance (α)**: Maximum permissible probability of Type-I error; commonly 5% or 1%. ⭐ (exam-important)
- **Confidence Coefficient (1-α)**: Probability of correctly not rejecting H₀ when it is true; the degree of confidence. ⭐ (exam-important)
- **Critical Region**: The set of test statistic values leading to rejection of H₀. ⭐ (exam-important)
- **p-value**: The lowest significance level at which H₀ can be rejected; reject H₀ if p-value < α. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: "Accepting" H₀ → ✅ Correct: We "fail to reject" or "do not reject" H₀ — never formally "accept" it
- ❌ Mistake: Thinking p-value = probability that H₀ is true → ✅ Correct: p-value = probability of observing this extreme a result IF H₀ were true
- ❌ Mistake: Confusing Type-I and Type-II errors → ✅ Correct: Type-I = rejecting true H₀ (worse); Type-II = not rejecting false H₀

### Quick Recall
> **Quick Recall:**
> - Type-I: Reject true H₀ (P = α). Type-II: Fail to reject false H₀
> - α = 5% → 95% confidence; α = 1% → 99% confidence
> - p-value < α → Reject H₀; p-value > α → Do not reject H₀
> - One-tailed: µ > µ₀ or µ < µ₀ | Two-tailed: µ ≠ µ₀

### Connections
- Builds on: CLT (above), Confidence interval (Chunk 003)
- Is prerequisite for: t-test, F-test in OLS regression (Block 2)
- Connects to: CYP Check Your Progress 2 (Chunk 005 answers)

---

## Section: Estimation Methods — OLS, MLE, Method of Moments 🔴

### Core Idea
Three methods are used to estimate parameters of a population regression function: (1) Ordinary Least Squares (OLS) — minimises sum of squared residuals; (2) Maximum Likelihood Estimation (MLE) — maximises the likelihood of observing the data; (3) Method of Moments — equates sample moments to population moments. Each has different properties and is used in different contexts.

> **In Simple Terms:** OLS says "pick the line that minimises squared errors". MLE says "pick the parameters most likely to produce the data you observed". Method of Moments says "make the sample averages equal the theoretical averages."

### Key Concepts

#### Method of Least Squares (OLS)
Consider a system of m equations with n unknowns (m > n): finding an exact solution is impossible, so we minimise the sum of squared residuals S = Σeᵢ².

**Minimisation condition**: dS/dxⱼ = 0 for j = 1, 2, ..., n → gives **n normal equations** with n unknowns → unique solution.

**For fitting a line y = a + bx**: S = Σ(yᵢ - a - bxᵢ)² → set ∂S/∂a = 0 and ∂S/∂b = 0 → solve the two normal equations.

#### Maximum Likelihood Method (MLE)
MLE finds the values of parameters that **maximise the probability (likelihood) of observing the data**. Key properties of MLE:
1. **Consistent**: Converges to true value as n→∞
2. **Efficient**: Attains Cramér-Rao lower bound (asymptotically)
3. **Sufficient**: Uses all information in the sample
4. **Not necessarily unbiased** in finite samples (but can be corrected)
5. **Approximately normal**: For large samples, MLE estimates are approximately normally distributed
6. **Invariant**: If θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ) for any function g

#### Method of Moments
Equates sample moments (e.g., sample mean, sample variance) to the corresponding population moments, then solves for parameter values.

### Definitions
- **Method of Least Squares**: A method that estimates unknown parameters by minimising the sum of squares of residuals S = Σeᵢ². ⭐ (exam-important)
- **Normal Equations**: The set of n equations obtained by setting ∂S/∂xⱼ = 0; solving them gives the OLS estimates.
- **Maximum Likelihood Estimator (MLE)**: The parameter value that maximises the likelihood function L(θ|data); consistent, efficient, sufficient, and asymptotically normal. ⭐ (exam-important)
- **Method of Moments**: Estimation method that equates sample moments to population moments and solves for parameters.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking OLS gives one equation per unknown → ✅ Correct: OLS gives n **normal equations** for n unknowns; exact solution exists only when equations = unknowns
- ❌ Mistake: Thinking MLE is always unbiased → ✅ Correct: MLE can be biased in small samples; bias correction exists

### Quick Recall
> **Quick Recall:**
> - OLS: Minimise Σeᵢ² → solve normal equations (n equations, n unknowns)
> - MLE: Maximise L(θ|data) → consistent, efficient, sufficient, asymptotically normal
> - MLE properties: (a) Consistent (b) Efficient (c) Sufficient (d) Not always unbiased (e) Approx normal (f) Invariant
> - Method of Moments: sample moments = population moments

### Connections
- Builds on: Properties of estimators (Chunk 003), CLT (above)
- Is prerequisite for: OLS derivation (Block 2, Unit 4), MLE applied in Logit/Probit (Block 4, Unit 15)
- Connects to: Matrix formulation of OLS (Unit 3 → Block 2)
