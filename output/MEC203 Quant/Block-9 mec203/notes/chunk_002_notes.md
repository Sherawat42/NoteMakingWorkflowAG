# Chunk 002 — Types of Sampling, Sampling Distribution, Standard Error, Sample Mean
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

## Section: Types of Sampling 🔴
<!-- See chunk 001 for biases that motivate the choice of sampling method -->

### Core Idea
Sampling techniques split into two large families: **non-probability sampling** (used when no sampling frame exists; standard errors cannot be computed) and **probability sampling** (every unit has a known non-zero probability of selection; standard errors and confidence intervals are available). Within probability sampling, the source text lists five techniques in order of increasing sophistication: SRS, systematic, stratified, cluster, and multistage.

> **In Simple Terms:** If you have a list of everyone in the population, you can use probability sampling and rigorously compute uncertainty. If you don't have such a list, you fall back to non-probability methods — useful but you can't put real error bars on them.

### Key Concepts

#### A. Non-probability Sampling
Used when no sampling frame is available. Three properties:
1. Some population units have **zero probability** of selection.
2. Selectable units have an **unknown** non-zero probability.
3. Sampling errors **cannot be quantified**.

| Type | Mechanism | Example |
|---|---|---|
| **Convenience Sampling** | Pick whoever is in the vicinity / accessible | Reporters approaching people in a market for political opinion |
| **Judgement Sampling** | Expert opinion picks individuals | Research firm filtering people through qualifying questions for a focus group; TV-show panellists |
| **Quota Sampling** | Specifies quotas on age, gender, social class, etc. to mirror population | Survey requiring "30 females aged 25-40, 30 males aged 25-40, …" |

Limitation: confidence intervals and hypothesis testing rules of inferential statistics **don't apply** here — standard errors cannot be estimated.

#### B. Probability Sampling
Every population unit has a known, non-zero probability of selection. Selection done by randomization (e.g., Tippet's tables, dice). More expensive and time-consuming than non-probability sampling, but allows quantification of error.

| Type | What it does | Where it's best |
|---|---|---|
| **Simple Random Sampling (SRS)** | Each unit has equal probability | Simple; produces unbiased estimates; baseline for theory |
| **Systematic Random Sampling** | Random start, then every k-th element where k = N/n | Use only if population is logically homogeneous; researcher must ensure k has no pattern |
| **Stratified Random Sampling** | Population split into homogeneous strata; SRS within each stratum | When natural groupings exist (gender, age); higher accuracy (smaller SE); broad cross-section |
| **Cluster Sampling** | Population split into heterogeneous clusters; SRS of clusters; survey all units in chosen clusters (one-stage) or subsample (two-stage) | Cost reduction; useful for geographically dispersed populations |
| **Multistage Sampling** | Sample primary units, then secondary, then tertiary, … | Large government surveys (often combine stratification + clustering) |

#### Stratified vs. Cluster — the contrast
| Aspect | Stratified | Cluster |
|---|---|---|
| Within-group | Homogeneous | Heterogeneous |
| Between-group | Heterogeneous | Homogeneous (ideally) |
| Sampling rule | Sample from *every* stratum | Sample *some* clusters; survey all (or sub-sample) units in chosen ones |
| Goal | Higher accuracy (smaller SE) | Lower cost |
| Stages | Generally one-stage | One-stage or multi-stage |

#### Tippet's Random Numbers Table
Contains 10,400 four-digit numbers (41,600 digits in all), drawn from British census reports. Any randomly selected row, column or diagonal can constitute a random number sequence.

### Definitions
- **Non-probability sampling**: selection without a sampling frame; some units have zero probability and the rest unknown probability. ⭐
- **Probability sampling**: every unit has a known, non-zero probability of selection.
- **Simple Random Sampling (SRS)**: each unit has *equal* probability; produces unbiased estimates.
- **Systematic random sampling**: select an initial element at random, then every k-th element (k = N/n). ⭐
- **Stratified random sampling**: divide heterogeneous population into homogeneous strata, then SRS within each. ⭐
- **Cluster sampling**: divide population into heterogeneous clusters, SRS of clusters; one-stage or multi-stage. ⭐
- **Multistage sampling**: sequential sampling at two or more successive stages.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing stratified and cluster sampling. → ✅ Correct: Strata are sampled *all*; clusters are sampled *some*. Strata are homogeneous internally; clusters are (ideally) heterogeneous internally.

> **Quick Recall:**
> - Non-probability: convenience / judgement / quota
> - Probability: SRS / systematic / stratified / cluster / multistage
> - Tippet's table = 10,400 four-digit numbers
> - Standard errors are **only** computable for probability samples

### Connections
- Builds on: **Sampling Frame** (Chunk 001) — distinguishes probability from non-probability methods.
- Prerequisite for: **Standard Error** (later in this chunk) — derivations assume probability sampling.

---

## Section: Parameter and Statistic 🟡
<!-- See chunk 001 for the high-level distinction; this section formalises notation -->

### Core Idea
**R. A. Fisher** named the sample-based numerical measures (mean, variance) "statistics" to keep them verbally distinct from the population's "parameters". Because a statistic is a function of sample values, and many possible samples can be drawn from the same population, the statistic varies across samples — these differences are called **sampling fluctuations**, and characterizing them is the central problem of sampling theory.

### Key Concepts
- Population constants: μ (mean), σ² (variance) — **parameters** (usually unknown)
- Sample-based functions: x̄ (sample mean), s² (sample variance) — **statistics** (computed)
- A statistic is an *estimate* of a parameter; its value changes from sample to sample → "sampling fluctuations"
- Notation convention from now on: μ, σ² for population; x̄, s for sample.

> **Quick Recall:**
> - Parameter = constant of the population
> - Statistic = function of sample data
> - Sampling fluctuations = sample-to-sample variation in a statistic

---

## Section: Sampling Distribution of a Statistic 🔴

### Core Idea
A **sampling distribution** is the probability distribution of all the values a statistic could take across every possible sample of fixed size *n* from a population. For a finite population of size N, there are NCₙ possible samples; the statistic's distribution can be tabulated. The mean of the sampling distribution of x̄ equals the population mean μ — that is, **x̄ is an unbiased estimator of μ**. The standard deviation of this sampling distribution is called the **standard error**.

> **In Simple Terms:** Imagine drawing every possible sample of size n from a population, computing x̄ for each, and listing all those x̄ values. That long list is the "sampling distribution of x̄". Its centre is μ and its spread is σ/√n.

### Key Concepts

#### Definition
The frequency distribution of a statistic obtained from infinitely many samples of fixed size *n*. Properties of interest: mean E(x̄), variance σ²_x̄ (or standard error σ_x̄).

#### Number of Possible Samples
For finite population N and sample size n: ᴺCₙ = N!/[n!(N−n)!] possible samples.

#### Unbiasedness of x̄
By definition E(x̄) = μ + (cancelling deviations). With unbiased sampling, deviations of x̄ from μ are equally likely above and below, so on average they cancel:
$$E(x̄) = μ$$

#### Worked Example (Source Text)
- Population: N = 3, values x₁ = 1, x₂ = 3, x₃ = 5. So μ = 3.
- Sample size n = 2 → number of samples = ³C₂ = 3.
  - Sample 1: (1,3) → x̄₁ = 2
  - Sample 2: (3,5) → x̄₂ = 4
  - Sample 3: (1,5) → x̄₃ = 3
- E(x̄) = (2 + 4 + 3)/3 = 3 = μ ✓

#### Standard Error of x̄
$$\sigma_{x̄} = \frac{\sigma}{\sqrt{n}}$$

#### Probable Error
The text introduces 0.6745 × SE as the "probable error" of the statistic. Justification: for a normal variable x with mean μ and standard deviation σ:
$$P[μ − 0.6745σ < x < μ + 0.6745σ] ≈ 0.5$$

### Definitions
- **Sampling distribution**: probability distribution of all possible values of a sample statistic. ⭐ (exam-important)
- **Standard error (SE)**: the standard deviation of the sampling distribution of a statistic. ⭐ (exam-important)
- **Probable error**: 0.6745 × standard error.

> **Quick Recall:**
> - E(x̄) = μ → x̄ is unbiased
> - σ_x̄ = σ/√n
> - Probable error = 0.6745 × SE
> - Number of possible samples (without replacement) from finite N = ᴺCₙ

### Connections
- Builds on: **Probability Sampling** (Section: Types of Sampling, this chunk).
- Foundation for: **Hypothesis Testing** (Unit 31, later chunks).

---

## Section: Standard Error 🔴

### Core Idea
The **standard error** measures the dispersion of a statistic around the parameter it estimates. Two intuitions explain its formula σ_x̄ = σ/√n: greater population spread σ → greater chance of an unrepresentative sample; larger sample size n → narrower dispersion. Crucially, n appears as **√n** (not n), so doubling precision requires *quadrupling* sample size — diminishing returns.

> **In Simple Terms:** SE tells you how off-target your sample average might be from the true average. Cut SE in half by tripling sample size? No — you have to *quadruple* it. That's why surveys can be expensive.

### Key Concepts

#### What Drives SE
Two factors:
- **Population spread (σ)**: more spread → more scope for sampling error → larger SE.
- **Sample size (n)**: larger n → tighter dispersion → smaller SE.

The √n in the denominator means **diminishing returns**: increasing n by a factor of 4 reduces SE by only a factor of 2.

#### Table 28.1 — Standard Errors of Common Statistics (Large Samples)

For a population with variance σ², proportion P, and Q = 1 − P; n is sample size; n₁, n₂ are sizes of two independent samples.

| # | Statistic | Standard Error |
|---|---|---|
| 1 | Sample mean: x̄ | σ/√n |
| 2 | Observed sample proportion: p | √(PQ/n) |
| 3 | Sample s.d.: s | σ/√(2n) |
| 4 | Sample variance: s² | σ²·√(2/n) |
| 5 | Sample quartile | 1.36263 σ/√n |
| 6 | Sample median | 1.25331 σ/√n |
| 7 | Sample correlation coefficient | (1 − ρ²)/√n |
| 8 | Sample moment μ₃ | σ³·√(96/n) |
| 9 | Sample moment μ₄ | σ⁴·√(96/n) |
| 10 | Sample coefficient of variation v | (v/√(2n))·√(1 + 2v²/100) approx. (text uses v·√[(1/2n) + (v²/(100·2n))]) |
| 11 | Difference of two sample means (x̄₁ − x̄₂) | √(σ₁²/n₁ + σ₂²/n₂) |
| 12 | Difference of two sample s.d.s (s₁ − s₂) | √(σ₁²/2n₁ + σ₂²/2n₂) |
| 13 | Difference of two sample proportions (p₁ − p₂) | √(P₁Q₁/n₁ + P₂Q₂/n₂) |

### Subsection: Utility of Standard Error
1. **Index of precision** — the magnitude of SE measures how precise the estimate is; the **reciprocal of SE = measure of reliability**.
2. **Determines probable limits** — given x̄ ± k·SE for some k tied to the desired confidence level, we can construct an interval likely to contain the population parameter.

### Definitions
- **Standard error (SE)** ⭐: the standard deviation of the sampling distribution of a statistic.

> **Quick Recall:**
> - Mean SE = σ/√n
> - Proportion SE = √(PQ/n)
> - Median SE = 1.25331·σ/√n (so median is less efficient than mean)
> - Reciprocal of SE = reliability
> - Quadrupling n halves SE (√n behaviour)

---

## Section: Expectation and Standard Error of Sample Mean 🔴

### Core Idea
The text formally derives E(x̄) and σ_x̄ in two cases — sampling **with replacement** and sampling **without replacement** — using elementary probability identities. The key result: E(x̄) = μ in both cases (so x̄ is always unbiased), but Var(x̄) takes different forms.

### Mechanisms / Processes

Setup: random sample of size n from finite population of size N.
- Population mean: μ = (1/N)·ΣXₐ.
- Population variance: σ² = (1/N)·Σ(Xₐ − μ)².
- Sample mean: x̄ = (1/n)·Σxᵢ.
- Probability theorems used:
  (i) If y = bx, then E(y) = b·E(x).
  (ii) If z = x + y (random variables), then E(z) = E(x) + E(y).

#### Case I — Random Sampling **With** Replacement
- For each i: xᵢ takes values X₁,…,Xₙ each with probability 1/N.
- E(xᵢ) = ΣXₐ·(1/N) = μ
- Var(xᵢ) = Σ(Xₐ − μ)²·(1/N) = σ²
- Independence of xᵢ, xⱼ (i ≠ j) → cov(xᵢ, xⱼ) = 0.
- ⇒ E(x̄) = (1/n)·n·μ = μ
- ⇒ Var(x̄) = (1/n²)·n·σ² + 0 = σ²/n
- **Standard error: σ_x̄ = σ/√n**

#### Case II — Random Sampling **Without** Replacement
- For each i: E(xᵢ) = μ, Var(xᵢ) = σ² (same as Case I, since the marginal distribution of each xᵢ is unchanged).
- The covariance term is **non-zero** here because once one unit is drawn, the conditional distribution of the next changes. (Derivation continues in **chunk 003**, where the finite population correction √[(N−n)/(N−1)] enters.)

> **Quick Recall:**
> - With replacement: σ_x̄ = σ/√n
> - Without replacement: SE includes finite population correction (FPC)
> - x̄ is unbiased in both cases: E(x̄) = μ

### Connections
- Builds on: probability theorems (E(bx) = bE(x), E(x+y) = E(x)+E(y)).
- Continues into: SE of sample proportion + finite population correction (Chunk 003).

<!-- Continues in chunk 003 -->
