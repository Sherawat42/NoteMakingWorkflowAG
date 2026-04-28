# Chunk 006 — MVUE Continued, Sufficiency, Cramer-Rao, Asymptotic Properties, Methods of Estimation
<!-- Pages: 51-60 -->
<!-- Source: chunk_006.txt -->

## Section: MVUE Continued — Mean vs Median Efficiency 🟡
<!-- See chunk 005 for the MVUE definition and x̄ being MVUE for normal μ -->

### Core Idea
For a normal population, **both** sample mean and sample variance are consistent estimators of μ — but their variances differ. The text computes Var(x̄) = σ²/n and Var(median) = (π/2)·σ²/n. Hence **efficiency of mean over median = (2/π) ≈ 0.64**, meaning the median's variance is larger than the mean's. The mean is therefore the more efficient estimator of μ for normal data.

### Key Concepts
- Var(x̄) = σ²/n
- Var(Median) = πσ²/(2n)
- Efficiency of mean = Var(median)/... actually text computes ratio (2/π) ≈ 0.64 → mean is more efficient than median
- A statistic with minimum variance among all estimators of θ is called a **Minimum Variance (MV) estimator**.

> **Quick Recall:**
> - Mean is more efficient than median (for normal data).
> - Efficiency = Var(best)/Var(rival) ≤ 1.

---

## Section: Sufficiency 🔴

### Core Idea
A **sufficient statistic** captures all the information in the sample about a parameter — meaning the conditional distribution of the data given the statistic doesn't depend on the parameter. Checking sufficiency directly is tedious, so we use the **Factorization Theorem (Neyman)** as a practical test. The most general distributional family admitting a sufficient statistic is **Koopman's exponential family**, which includes binomial, Poisson, and normal as members.

> **In Simple Terms:** A sufficient statistic is a "summary" of the sample that loses nothing relevant about the parameter. If you know the summary, the rest of the sample doesn't tell you anything more about the parameter.

### Key Concepts

#### Definition
T = T(x₁,…,xₙ) is sufficient for θ if the conditional distribution of x₁,…,xₙ given T = t is independent of θ.

#### Factorization Theorem (Neyman)
T = t(x) is sufficient for θ if and only if the joint p.d.f. (likelihood) L can be expressed as:
$$L = g_θ[t(x)] \cdot h(x)$$
where g_θ depends on θ and x only through t(x), and h(x) is independent of θ.

##### Notes
- "Independent of θ" means neither in the function nor in its domain.
- The original full sample (X₁,…,Xₙ) is *always* a sufficient statistic.

#### Koopman's Exponential Family
The most general form of distributions admitting a sufficient statistic:
$$L = g(x)\cdot h(θ)\cdot \exp\{a(θ)\,w(x)\}$$
Members include: binomial, Poisson, normal (with unknown mean and variance), exponential, gamma, etc.

#### Invariance Property
If T is sufficient for θ and ψ(T) is a one-to-one function of T, then ψ(T) is sufficient for ψ(θ).

#### Fisher–Neyman Criterion
Statistic t₁ = t₁(x₁,…,xₙ) is sufficient for θ iff the likelihood factors as
$$L = \prod_{i=1}^n f(x_i, θ) = g_1(t_1, θ)\cdot k(x_1, x_2, …, x_n)$$
where g₁(t₁, θ) is the p.d.f. of the statistic t₁ and k is a function of sample observations only.

### Definitions
- **Sufficient estimator** ⭐: an estimator that contains all the sample information about the parameter.
- **Factorization theorem** ⭐ (Neyman): L = g_θ[t(x)] · h(x).
- **Exponential family of distributions**: L = g(x)·h(θ)·exp{a(θ)w(x)} (Koopman's form).
- **Invariance property of sufficiency**: 1-1 functions of sufficient statistics are sufficient for the corresponding 1-1 function of the parameter.

> **Quick Recall:**
> - Sufficient = full sample info about θ
> - Factorization: L = g_θ[t(x)]·h(x)
> - Exponential family ⇒ has a sufficient statistic
> - Whole sample is always sufficient

### Connections
- Builds on: parameter space, estimator definitions (Chunk 005).
- Used in: Rao-Blackwell theorem (next section).

---

## Section: Cramer-Rao Inequality 🔴

### Core Idea
The **Cramer-Rao Inequality** sets a *lower bound* on the variance of any unbiased estimator. If an estimator's variance attains this bound, no unbiased estimator can do better — it is a Minimum Variance Bound (MVB) estimator. The bound depends on the **Fisher information** about θ contained in the sample.

> **In Simple Terms:** Cramer-Rao tells you the best possible variance any unbiased estimator can have. If your estimator hits that floor, you can stop looking for a better one.

### Key Concepts

#### Statement
For any unbiased estimator θ̂ of θ:
$$Var(θ̂) \ge \frac{1}{n\,E\left[\left(\frac{\partial \ln f(x, θ)}{\partial θ}\right)^2\right]}$$
where f(x, θ) is the population density and n is the sample size.

#### Fisher Information
The denominator is the (sample) information about θ:
$$I(θ) = n\,E\left[\left(\frac{\partial \ln f(x, θ)}{\partial θ}\right)^2\right]$$
Smaller variance ⇔ more information.

#### Regularity Conditions (5 conditions)
1. Parameter space Θ is a non-degenerate open interval on ℝ¹.
2. ∂f(x,θ)/∂θ exists for almost all x (the exceptional set independent of θ).
3. Range of integration is independent of θ → f(x,θ) differentiable under integral sign.
4. Conditions of uniform convergence are satisfied → differentiation under integral sign is valid.
5. I(θ) > 0 exists for all θ ∈ Θ.

#### Minimum Variance Bound (MVB) Estimator
An unbiased estimator t of ψ(θ) for which the Cramer-Rao lower bound is attained.

### Definitions
- **Cramer-Rao Inequality** ⭐: Var(unbiased) ≥ 1/[n·E[(∂lnf/∂θ)²]].
- **Fisher Information I(θ)** ⭐: measures information in the sample about θ.
- **Minimum Variance Bound (MVB) Estimator**: attains the Cramer-Rao bound.

> **Quick Recall:**
> - CR-bound: Var(θ̂) ≥ 1/(n·I(θ)).
> - I(θ) = E[(∂lnf/∂θ)²].
> - More info → smaller variance.
> - 5 regularity conditions required.

---

## Section: MVUE and Blackwellisation 🟡

### Core Idea
The Cramer-Rao inequality identifies whether a candidate is MVB; but MVB ≠ MVUE always (CR-bound may not be attainable). When regularity conditions fail, the least-attainable variance may even be *less* than the CR bound. **Blackwellisation** (named after D. Blackwell) is a technique for obtaining MVUE from any unbiased estimator using a sufficient statistic.

### Key Concepts

#### Rao-Blackwell Theorem
Let X, Y be random variables with E(Y) = μ and Var(Y) = σ_Y² > 0. If E(Y | X = x) = φ(x), then:
1. E[φ(X)] = μ
2. Var[φ(X)] ≤ Var(Y).

The improved estimator is φ(X) = E(Y | X = x), which is unbiased and has smaller (or equal) variance than Y.

#### Generalised Form
- U = U(x₁,…,xₙ) — unbiased estimator of ψ(θ).
- T = T(x₁,…,xₙ) — sufficient statistic for ψ(θ).
- Define φ(T) = E(U | T = t) — independent of θ since T is sufficient.
- Then E[φ(T)] = ψ(θ) AND Var[φ(T)] ≤ Var(U).

#### Application
Starting from U (any unbiased estimator), construct φ(T) using a sufficient statistic. Result: φ(T) is unbiased and has smaller variance than U. If T is also **complete**, φ(T) is the unique MVUE.

### Definitions
- **Rao-Blackwell Theorem** ⭐: technique for variance reduction via sufficient statistics.
- **Blackwellisation**: the process of constructing an improved estimator E(U|T).
- **Completeness**: a property of a statistic ensuring different parameter values yield different distributions, key for uniqueness of MVUE.

> **Quick Recall:**
> - Rao-Blackwell: condition on a sufficient statistic to reduce variance.
> - Sufficient + Complete → MVUE.
> - MVB ≠ MVUE always; CR-bound may not be tight.

### Connections
- Builds on: sufficient statistic + factorisation theorem.
- Used in: deriving optimal estimators in normal-theory inference.

---

## Section: Asymptotic Properties 🔴

### Core Idea
Asymptotic theory studies estimators as n → ∞. Three properties matter: **asymptotic unbiasedness**, **consistency** (convergence in probability), and **convergence in distribution / asymptotic normality**. The **Central Limit Theorem** is the canonical asymptotic-normality result.

### Subsection: Asymptotic Unbiasedness
$$\lim_{n \to \infty} B(θ̂_n) = θ$$
If E(θ̂_n) → θ as n → ∞, the estimator is asymptotically unbiased.

### Subsection: Consistency (Convergence in Probability)
For any ε > 0:
$$\lim_{n \to \infty} P(|θ̂_n − θ| > ε) = 0$$
i.e., θ̂_n →ᴾ θ. Practically: for large n, the estimator is within any pre-assigned tolerance of θ with high probability.

#### Sufficient Condition (corollary of Chebyshev)
If θ̂_n is unbiased AND Var(θ̂_n) → 0 as n → ∞, then θ̂_n is consistent.

#### Worked Example: S² consistent for σ² (Normal Population)
- E(S²) = σ² (unbiased).
- Var(S²) = 2σ⁴/n → 0 as n → ∞.
- Hence S² is a consistent estimator of σ² for a normal population.

### Subsection: Convergence in Distribution and Asymptotic Normality

#### Convergence in Distribution
A sequence Z_n converges in distribution to a continuous Z if for any real z:
$$P(Z_n \le z) \to P(Z \le z) \quad \text{as } n \to \infty$$
Notation: Z_n →ᴰ Z.

#### Asymptotic Normality
If Z_n →ᴰ N(μ, σ²), then Z_n is asymptotically normal. If specifically Z_n →ᴰ N(0, 1), Z_n has an *asymptotic standard normal* distribution. Then for large n:
$$P(Z_n \le z) \approx \Phi(z)$$

#### Central Limit Theorem (restated)
For iid X₁,…,Xₙ with E(Xᵢ) = μ, Var(Xᵢ) = σ²:
$$Z_n = \frac{x̄ − μ}{σ/\sqrt{n}} \xrightarrow{D} N(0, 1)$$

### Definitions
- **Convergence in probability** ⭐: P(|Z_n − Z| > ε) → 0.
- **Convergence in distribution** ⭐: c.d.f. of Z_n → c.d.f. of Z pointwise.
- **Asymptotic normality** ⭐: Z_n →ᴰ N(μ, σ²).

> **Quick Recall:**
> - Asymptotic unbiased: E(θ̂_n) → θ.
> - Consistent: θ̂_n →ᴾ θ; sufficient condition = unbiased + Var → 0.
> - Asymptotic normal: Z_n →ᴰ N.
> - CLT: standardised sample mean → N(0,1).
> - S² is consistent for σ² in normal samples (Var(S²) = 2σ⁴/n).

---

## Section: Methods of Estimation 🔴

### Core Idea
Three named methods of estimation: **Maximum Likelihood (ML)**, **Generalized Method of Moments (GMM)**, and **Partial Least Squares (PLS)**. ML is the most widely used and yields excellent estimators for large samples. GMM relaxes the distributional assumption — using only specified moments — making it more robust. PLS handles regressions with many correlated regressors via PCA-type dimension reduction.

### Subsection: Maximum Likelihood (ML) 🔴

#### Idea
Given observations x₁,…,xₙ from f(x | θ), the **likelihood function** is the joint density viewed as a function of θ:
$$L(θ) = f(x_1, …, x_n | θ) = \prod_{i=1}^n f(x_i | θ)$$

The MLE is the value of θ that maximises L(θ) — the value under which the observed data is "most likely".

#### Maximisation Trick
Maximise log-likelihood ℓ(θ) = log L(θ):
$$\ell(θ) = \log L(θ) = \sum_{i=1}^n \log f(x_i | θ)$$
Find dℓ/dθ = 0 (or solve numerically).

#### Properties
- For large samples, MLE gives an "excellent" estimator of θ.
- MLE is consistent and asymptotically efficient (asymptotically achieves Cramer-Rao bound under regularity).

### Subsection: Generalized Method of Moments (GMM) 🟡

#### Idea
Use moment conditions instead of full distribution:
$$m(θ_0) = E[g(Y_t, θ)] = 0$$
The sample analog:
$$\hat g(θ) = \frac{1}{T}\sum_{t=1}^T g(Y_t, θ)$$
Minimise the norm of ĝ(θ); the minimiser is the GMM estimator.

#### Properties
- Consistent, asymptotically normal, and most efficient in the class of estimators using only the moment conditions.
- More **robust** than ML because it doesn't assume the full distribution.

### Subsection: Partial Least Squares (PLS) 🟡

#### Idea
Used when:
- Number of explanatory variables is large compared to observations, OR
- Explanatory variables are correlated.

PLS reduces the number of independent variables to keep only the relevant ones.

#### Tool: Principal Component Analysis (PCA)
PCA reduces dimensionality of large datasets by transforming many variables into a smaller set of uncorrelated "principal components" that retain most of the original information.

### Definitions
- **Maximum Likelihood Estimator (MLE)** ⭐: argmax of L(θ).
- **Generalized Method of Moments (GMM)** ⭐: estimator from sample moment conditions.
- **Partial Least Squares (PLS)**: dimension-reduction estimation via PCA.
- **Principal Component Analysis (PCA)**: reduces dimensionality preserving most information.

### ⚠️ Common Mistakes
- ❌ Mistake: Maximising L(θ) directly — often algebraically painful. → ✅ Correct: Maximise log L(θ); same maximiser, easier algebra.

> **Quick Recall:**
> - ML: maximise L(θ) (or log L).
> - GMM: replace E[g(Y,θ)]=0 by sample average; more robust.
> - PLS: dimension reduction with PCA for many correlated regressors.

### Connections
- ML uses the full distribution → leads to MVB attainment under regularity.
- GMM is a relaxation: uses only moments.
- Continues into worked MLE problems (Chunk 007).

<!-- Continues in chunk 007 -->
