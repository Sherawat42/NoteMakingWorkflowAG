# Chunk 003 — End of Unit 1 & Unit 2: Statistical Inference, Estimation & Estimator Properties
<!-- Pages: 19–28 -->
<!-- Source: chunk_003.txt -->
<!-- Continues from: Functional Forms / DGP (Chunk 002) -->
<!-- Continues into: Asymptotic Properties, LLN, CLT (Chunk 004) -->

## Section: End of Unit 1 — Software, Summary & Key Words 🟢

### Core Idea
Unit 1 concludes with a summary, key words, and a list of software packages used in econometric analysis. The key takeaway from Unit 1 is that econometric models are stochastic (include error term u) and that the DGP is unknown — we approximate it through iterative model building.

> **In Simple Terms:** Unit 1 wraps up by reminding you: all economic models are simplified approximations of reality (the DGP), and that's okay. The error term is your honest admission of that simplification.

### Key Concepts

#### Econometric Software Landscape

| Software | Type | Key Features |
|----------|------|-------------|
| R | Open-source (free) | Requires programming knowledge; highly extensible |
| STATA | Licensed (paid) | Point-and-click; widely used in economics |
| E-Views | Licensed (paid) | Specialised for time series; point-and-click |
| SPSS | Licensed (paid) | Popular in social sciences |
| Gretl | Freeware | Freely downloadable; good for econometrics |
| EasyReg | Freeware | Downloadable; user-friendly |

### Definitions
- **R**: Free, open-source statistical computing software; highly extensible but requires programming knowledge.
- **Gretl**: Free, open-source econometric software; a practical alternative to paid packages.

### Quick Recall
> **Quick Recall:**
> - Open-source (free): R, Gretl, EasyReg, Matrixer
> - Licensed (paid): STATA, E-Views, SPSS
> - R advantage: extensible; R limitation: requires programming

### Connections
- Wraps up: Unit 1 (Chunks 001–003)
- Software used in: All empirical econometric work (Block 2 onwards)

---

## Section: Unit 1 Key Words Glossary 🟡

### Core Idea
Unit 1 provides formal definitions of 11 key terms that recur throughout the entire course. These definitions are directly sourced from the text and serve as the precise language for exam answers.

### Definitions
- **Alternative Hypothesis**: In hypothesis testing, the condition opposite to the null hypothesis; expressed as H₁: β₂ ≠ 0 (slope coefficient is non-zero, positive or negative). ⭐ (exam-important)
- **Classical Linear Regression Model**: A linear regression model establishing a linear relationship between variables, based on specific assumptions about the error variable.
- **Confidence Interval**: The range of values determining the probability that the parameter lies within the interval. ⭐ (exam-important)
- **Deterministic Component**: The systematic component of the regression equation; the expected value of Y for given values of X.
- **Econometric Model**: Statistical models specifying relationships between various economic quantities.
- **Estimation of Parameters**: The process of estimating values of parameters based on empirical data that has a random component.
- **Null Hypothesis**: The hypothesis asserting no significant difference between a specified population parameter and a claimed value; observed differences are due to sampling/experimental error. ⭐ (exam-important)
- **Parameter**: A quantity or statistical measure for a given population that is fixed (e.g., mean, variance of a population).
- **Population Regression Function (PRF)**: A function hypothesizing a theoretical linear relationship between a dependent variable and explanatory variables; defines how conditional expectation of Y responds to changes in X. ⭐ (exam-important)
- **Statistical Inference**: The process of deducing properties of underlying probability distributions of parameters by analysing data.
- **Stochastic Error**: The error variable representing influences of variables not included in the regression model; reflects intrinsic randomness between variables. ⭐ (exam-important)

### Quick Recall
> **Quick Recall:**
> - H₀: no relationship; H₁: there is a relationship
> - Parameter = fixed population quantity; Statistic = sample-based estimate
> - PRF = theoretical (unknown); SRF = estimated from data

### Connections
- All 11 terms recur in subsequent blocks; especially PRF, H₀/H₁, confidence interval
- Connects to: Block 2 (OLS estimation), Block 3 (violations), Block 4 (extensions)

---

## Section: Unit 2 — Statistical Inference: Point & Interval Estimation 🔴

### Core Idea
Statistical inference is the process of drawing conclusions about a population based on sample data. It has two main forms: point estimation (a single best guess for a parameter) and interval estimation (a range within which the parameter lies with some probability). The sampling distribution of a statistic is what makes this possible — different samples give different estimates, and their distribution provides the basis for inference.

> **In Simple Terms:** You can't measure every household's income (the population). So you take a sample, compute the sample mean (point estimate), and say "I'm 95% confident the population mean lies between X and Y" (interval estimate). That's statistical inference.

### Key Concepts

#### Point Estimation
A **point estimate** is a specific single value of a statistic used to estimate a population parameter. For example, the sample mean x̄ is a point estimate of the population mean µ.

The key distinction:
- **Estimator**: A rule or formula used to estimate a parameter (e.g., x̄ = Σxᵢ/n)
- **Estimate**: The specific numerical value obtained when the estimator is applied to a particular sample

Since different samples give different estimates, we get a *distribution* of estimates across samples — the **sampling distribution**.

#### Interval Estimation (Confidence Interval)
An interval estimate is a range (T₁, T₂) such that P(T₁ ≤ θ ≤ T₂) = 1 - α, where α is the significance level. This range is called the **confidence interval**.

**Example from source**: If the sample mean x̄ = 5 and we say the population mean lies between (x̄ - 0.5) and (x̄ + 0.5), i.e., between 4.5 and 5.5, that range is the interval estimate of the population mean.

#### Sampling Distribution
The **sampling distribution** is the probability distribution of sample means (or other statistics) obtained from many samples of the same size n drawn from a population.

If samples are i.i.d. from a normal population, we can apply the Central Limit Theorem (see Chunk 004) to characterize this distribution.

### Definitions
- **Point Estimate**: A specific value of a statistic used to estimate a population parameter. ⭐ (exam-important)
- **Interval Estimate (Confidence Interval)**: A range (T₁, T₂) such that P(T₁ ≤ θ ≤ T₂) = 1 - α; also called a confidence interval. ⭐ (exam-important)
- **Estimator**: A rule or formula (function of sample observations) used to compute an estimate of a population parameter.
- **Estimate**: The specific numerical value of an estimator for a given sample; varies from sample to sample.
- **Sampling Distribution**: The probability distribution of a statistic (e.g., sample mean) computed from many samples of the same size.
- **Statistic**: A function of sample observations; used to estimate a population parameter (e.g., sample mean, sample variance). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing estimator and estimate → ✅ Correct: Estimator = the formula (same for all samples); Estimate = the value (varies across samples)
- ❌ Mistake: Thinking "95% confidence" means there's a 95% chance the true parameter is in this specific interval → ✅ Correct: It means that if we repeated this sampling procedure many times, 95% of such intervals would contain the true parameter

### Quick Recall
> **Quick Recall:**
> - Point estimate = one number; Interval estimate = a range with stated probability
> - Estimator (rule) → applied to sample → Estimate (number)
> - Sampling distribution = distribution of estimates across many samples

### Connections
- Builds on: Classical assumptions on u (Chunk 002)
- Is prerequisite for: Properties of estimators (below), Hypothesis testing (Chunk 004)
- Connects to: Confidence intervals in OLS (Block 2)

---

## Section: Properties of a Good Estimator 🔴

### Core Idea
Not all estimators are equal. Four properties define what makes an estimator "good": unbiasedness (it targets the right value on average), consistency (it improves as sample size grows), efficiency (minimum variance), and sufficiency (uses all information in the sample). When bias and variance must be traded off, Mean Squared Error (MSE) provides a composite criterion. The ideal estimator is the **Minimum Variance Unbiased Estimator (MVUE)**.

> **In Simple Terms:** An unbiased estimator aims at the right target (on average). A consistent one gets more accurate with more data. An efficient one is the most precise. The MVUE is the gold standard — unbiased AND most precise.

### Key Concepts

#### Unbiasedness
An estimator T is **unbiased** for parameter Ø if E(T) = Ø. The expected value of the estimator equals the true parameter value.

**Proof from source**: Sample mean x̄ is unbiased for population mean µ.
- E(xᵢ) = (X₁ + X₂ + ... + Xₙ)/N = µ (in SRSWR)
- E(x̄) = (1/n)[E(X₁) + E(X₂) + ... + E(Xₙ)] = (1/n)(nµ) = µ ✓

#### Minimum Variance Unbiased Estimator (MVUE)
Among all unbiased estimators, the MVUE has the **smallest variance**. If Tₘ is the MVUE of Ø, then:
- E(Tₘ) = Ø (unbiased)
- Var(Tₘ) < Var(T) for any other unbiased estimator T

#### Consistency
An estimator T is **consistent** if it converges in probability to the true parameter as sample size n → ∞:
lim_{n→∞} P(|T - Ø| < ε) = 1 for any ε > 0 (equivalently: lim P(T → Ø) = 1)

Two conditions for consistency: (i) lim E(T) = Ø (asymptotic unbiasedness), AND (ii) lim Var(T) = 0.

**Standard results**: Sample mean x̄ is consistent for µ; sample variance S² is consistent for σ².

#### Efficiency
The **most efficient** estimator has minimum variance among all **consistent** estimators. If Var(T₁) < Var(T₂) for all n, then T₁ is more efficient than T₂.

**Efficiency ratio**: Efficiency = V₁/V₂ ≤ 1 (since V₁ ≤ V₂ for the more efficient estimator).

#### Sufficiency
An estimator T is **sufficient** for Ø if it captures all the information in the sample about Ø. Formally: the conditional distribution P[X₁ ∩ X₂ ∩ ... ∩ Xₙ | T = t] does not depend on Ø.

#### Mean Squared Error (MSE)
When comparing two estimators where one has less bias but more variance, MSE provides a joint criterion:
**MSE(T) = Var(T) + [bias(T)]²**

If MSE(T₁) < MSE(T₂), prefer T₁ even if T₁ has higher variance than T₂ (if its bias reduction more than compensates).

### Definitions
- **Unbiased Estimator**: An estimator T where E(T) = Ø; it targets the true parameter on average. ⭐ (exam-important)
- **Minimum Variance Unbiased Estimator (MVUE)**: The unbiased estimator with the smallest variance in its class. ⭐ (exam-important)
- **Consistent Estimator**: An estimator T where lim_{n→∞} P(T → Ø) = 1; requires both asymptotic unbiasedness and vanishing variance. ⭐ (exam-important)
- **Efficient Estimator**: An estimator with minimum variance among all consistent estimators; relative efficiency = V₁/V₂. ⭐ (exam-important)
- **Sufficient Estimator**: An estimator that uses all available information in the sample about the parameter Ø. ⭐ (exam-important)
- **Mean Squared Error (MSE)**: MSE(T) = Var(T) + [bias(T)]²; a composite measure combining bias and variance for comparing estimators.

### Mechanisms / Processes
**Unbiasedness check**: Compute E(T) → compare to Ø → if equal, T is unbiased
**MVUE finding**: Among all unbiased T, find the one with minimum Var(T)
**Consistency conditions**: (i) lim E(T) → Ø AND (ii) lim Var(T) → 0 as n→∞
**MSE comparison**: MSE(T1) = Var(T1) + [bias T1]² vs MSE(T2) → pick lower MSE

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking consistency implies unbiasedness → ✅ Correct: A biased estimator can be consistent (if bias → 0 as n → ∞)
- ❌ Mistake: Thinking efficiency means "small variance" alone → ✅ Correct: Efficiency is *relative* — smallest variance compared to all other consistent estimators
- ❌ Mistake: Confusing sufficiency with unbiasedness → ✅ Correct: Sufficiency is about using all sample information; unbiasedness is about centering on the true parameter

### Edge Cases & Caveats
- An estimator can be unbiased but inefficient (large variance).
- An estimator can be biased but have lower MSE than an unbiased one (if variance gain > bias penalty).
- MSE = Var(T) for unbiased estimators (since bias = 0).

> **Quick Recall:**
> - 4 properties: Unbiasedness [E(T)=Ø] | Consistency [T→Ø as n→∞] | Efficiency [min variance] | Sufficiency [all info used]
> - MVUE = best of all unbiased estimators (lowest variance)
> - MSE = Var + Bias² — use when bias-variance trade-off arises
> - x̄ is unbiased and consistent for µ; S² is consistent for σ²

### Connections
- Is prerequisite for: Asymptotic Properties (Chunk 004), OLS BLUE properties (Block 2 Unit 4)
- Connects to: Gauss-Markov Theorem (Block 2) — OLS is BLUE (Best Linear Unbiased Estimator)

### Open Questions
1. Can an estimator be sufficient but not efficient?
2. How does the Cramér-Rao lower bound relate to MVUE?
