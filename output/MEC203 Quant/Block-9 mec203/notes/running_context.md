# Running Context

## Key Concepts Introduced
- **Population vs Sample** (Chunk 001): population = whole group under study (size N); sample = finite subset (size n)
- **Parameter vs Statistic** (Chunk 001): population characteristic μ,σ² vs sample characteristic x̄,s² (Fisher's terminology)
- **Census vs Sample Survey** (Chunk 001): full enumeration vs subset; only sample survey produces standard error
- **Random / Probability Sampling** (Chunk 001): each unit has known non-zero probability of selection
- **Sampling Frame** (Chunk 001): list of all population members; prerequisite for probability sampling
- **With/Without Replacement Sampling** (Chunk 001): without for large populations, with allowed if n ≪ N
- **Cost vs Efficiency Trade-off** (Chunk 001): efficiency = 1/Var; Var(x̄)=σ²/n
- **Selection Bias and sub-types** (Chunk 001): under-coverage, non-response, substitution, faulty demarcation, self-selection, recall, observer, survivorship
- **Procedural Bias** (Chunk 001): response, observational, non-response, interviewer
- **Omitted Variable Bias** (Chunk 001): regression bias from leaving out a relevant correlated variable
- **Sampling Error vs Survey Bias** (Chunk 001): only sampling error decreases with n

## Definitions (⭐ exam-important)
- **Population** (Chunk 001): aggregate of objects, animate or inanimate, under study
- **Sample** (Chunk 001): finite subset of statistical individuals from a population
- **Parameter** (Chunk 001): numerical characteristic of population (μ, σ²)
- **Statistic** (Chunk 001): numerical characteristic computed from sample observations only
- **Random sample** (Chunk 001): each unit has a known, non-zero probability of selection
- **Selection bias** (Chunk 001): bias from unrepresentative sample
- **Omitted Variable Bias (OVB)** (Chunk 001): regression-context bias from missing correlated variable

## Named Models / Laws / Theories
- **Fisher's parameter/statistic distinction** (Chunk 001): R. A. Fisher named the sample-based quantities "statistic"

## Key Data & Numbers
- Var(x̄) = σ²/n (Chunk 001): underlies cost-efficiency trade-off in sample design
- σ_x̄ = σ/√n (Chunk 002): standard error of the sample mean (with replacement)
- σ_p̂ = √(PQ/n) (Chunk 002): standard error of sample proportion
- Probable error = 0.6745 × SE (Chunk 002)
- ᴺCₙ = N!/(n!(N−n)!) possible samples (Chunk 002)
- Median SE = 1.25331·σ/√n; Quartile SE = 1.36263·σ/√n (Chunk 002, Table 28.1)
- Tippet's table: 10,400 four-digit numbers from British census reports (Chunk 002)

---
*New entries from Chunk 002:*

## Key Concepts (Chunk 002 additions)
- **Non-probability sampling** (Chunk 002): convenience, judgement, quota — no SE possible
- **Probability sampling** (Chunk 002): SRS, systematic, stratified, cluster, multistage
- **Sampling Distribution** (Chunk 002): probability law of a statistic over all possible samples
- **Standard Error** (Chunk 002): standard deviation of a sampling distribution; index of precision
- **Probable Error** (Chunk 002): 0.6745 × SE
- **Stratified vs Cluster sampling** (Chunk 002): strata internally homogeneous (sample all); clusters internally heterogeneous (sample some)

## Definitions (Chunk 002 additions)
- **Sampling distribution** ⭐ (Chunk 002): probability law of a statistic across all possible samples
- **Standard error** ⭐ (Chunk 002): SD of the sampling distribution
- **Simple Random Sampling (SRS)** ⭐ (Chunk 002): equal probability of selection
- **Systematic random sampling** ⭐ (Chunk 002): random start + every k-th element, k = N/n
- **Stratified random sampling** ⭐ (Chunk 002): split into homogeneous strata, SRS within
- **Cluster sampling** ⭐ (Chunk 002): split into heterogeneous clusters, SRS of clusters
- **Multistage sampling** (Chunk 002): sample at two or more successive stages
- **Sampling fluctuations** (Chunk 002): sample-to-sample variation in a statistic

## Named Models / Laws / Theories (Chunk 002 additions)
- **Tippet's Random Numbers Table** (Chunk 002): 10,400 four-digit numbers (41,600 digits)
- **R. A. Fisher's parameter/statistic distinction** (Chunk 002, restated)

---
*New entries from Chunk 003:*

## Key Concepts (Chunk 003 additions)
- **Sample Proportion p̂ = f/n** (Chunk 003): unbiased estimator of P
- **Finite Population Correction** (Chunk 003): √[(N−n)/(N−1)] applied when sampling without replacement
- **Chi-square distribution** (Chunk 003): sum of squared standard normals; positively skewed; mode at n−2
- **Additive property of χ²** (Chunk 003): independent χ² with df n₁,n₂ sum to χ² with df n₁+n₂
- **Jacobian transformation** (Chunk 003): tool for deriving densities of transformed variables

## Definitions (Chunk 003 additions)
- **Sample proportion p̂** ⭐ (Chunk 003): f/n
- **Finite Population Correction** ⭐ (Chunk 003): √[(N−n)/(N−1)]
- **Chi-square variate** ⭐ (Chunk 003): sum of squares of independent standard normals
- **Degrees of freedom** ⭐ (Chunk 003): parameter n; number of independent squares being summed

## Named Models / Laws / Theories (Chunk 003 additions)
- **Karl Pearson's χ² goodness-of-fit test** (Chunk 003 → 004): tests theory vs experiment

## Key Data & Numbers (Chunk 003 additions)
- σ_p̂ = √(PQ/n) with replacement; √(PQ/n)·√[(N−n)/(N−1)] without (Chunk 003)
- 95% CI: estimate ± 1.96·SE; 99% CI: ± 2.58·SE (Chunk 003 examples)
- Pineapple: p̂=0.13, SE=0.022, 95% CI [8.6%, 17.4%] (Chunk 003)

---
*New entries from Chunk 004:*

## Key Concepts (Chunk 004 additions)
- **MGF of χ²** (Chunk 004): (1−2t)^(−n/2)
- **χ² subtraction property** (Chunk 004): nested χ²s minus inner is also χ² with df subtracted
- **Independence of x̄ and s² for normal samples** (Chunk 004): uniquely holds in normal sampling
- **Student's t-distribution** (Chunk 004): t = (x̄−μ)/(s/√n) when σ unknown; df = n−1
- **Cauchy distribution** (Chunk 004): t with df=1
- **Fisher's t** (Chunk 004): generalization N(0,1)/√(χ²(n)/n)
- **F-distribution** (Chunk 004): ratio of two independent χ²/df
- **Reciprocal property of F** (Chunk 004): F_(1−α;n₁,n₂) = 1/F_(α;n₂,n₁)
- **Pearson's χ² goodness-of-fit** (Chunk 004): Σ(O−E)²/E ~ χ²(n−1)

## Definitions (Chunk 004 additions)
- **Critical value of χ²** ⭐ (Chunk 004): χ²(α,n) such that P[χ²>χ²(α,n)]=α
- **Goodness of fit** ⭐ (Chunk 004)
- **Pearson's χ² statistic** ⭐ (Chunk 004): Σ(O−E)²/E
- **Student's t** ⭐ (Chunk 004): df = n−1
- **F-distribution / Snedecor's F** ⭐ (Chunk 004): ratio (X/n₁)/(Y/n₂)
- **Independence of x̄ and s²** ⭐ (Chunk 004)

## Named Models / Laws / Theories (Chunk 004 additions)
- **Karl Pearson's χ² goodness-of-fit test** (Chunk 004): tests theory vs observation
- **Snedecor's F distribution** (Chunk 004)

## Key Data & Numbers (Chunk 004 additions)
- For n>30: √(2χ²) ≈ N(√(2n−1), 1) (Chunk 004)
- x̄ ~ N(μ, σ²/n) (Chunk 004)
- (n−1)s²/σ² ~ χ²(n−1) (Chunk 004)

---
*New entries from Chunk 005:*

## Key Concepts (Chunk 005 additions)
- **Law of Large Numbers** (Chunk 005): x̄ → μ in probability as n → ∞
- **Estimation problem vs Hypothesis testing problem** (Chunk 005)
- **Point vs Interval estimation** (Chunk 005)
- **Estimator** (Chunk 005): function of sample observations
- **Unbiasedness, Consistency, Efficiency, Sufficiency** (Chunk 005): four estimator criteria
- **Khinchin's Weak Law of Large Numbers** (Chunk 005)
- **Bias formula** b(θ) = E(T) − τ(θ) (Chunk 005)
- **Most Efficient Estimator** (Chunk 005); **MVUE** (Chunk 005)

## Definitions (Chunk 005 additions)
- **Central Limit Theorem (CLT)** ⭐ (Chunk 005)
- **Parameter Space Θ** ⭐ (Chunk 005)
- **Unbiased estimator** ⭐ (Chunk 005): E(T) = θ
- **Consistent estimator** ⭐ (Chunk 005): T_n →ᴾ θ
- **Efficient estimator** ⭐ (Chunk 005)
- **MVUE** ⭐ (Chunk 005)

## Named Models / Laws / Theories (Chunk 005 additions)
- **Khinchin's Weak Law of Large Numbers** (Chunk 005): iid mean converges in probability
- **Central Limit Theorem** (Chunk 005)

## Key Data & Numbers (Chunk 005 additions)
- 9:3:3:1 χ² test: χ²=4.73 < 7.815 → accept (Chunk 005)
- Bulb life t-test: t=−0.77, P=0.226 (Chunk 005)
- Efficiency upper bound E ≤ 1 (Chunk 005)
- Var(x̄)=σ²/n attains Cramer-Rao bound for normal μ (Chunk 005)

---
*New entries from Chunk 006:*

## Key Concepts (Chunk 006 additions)
- **Sufficient statistic** (Chunk 006): captures all sample info about θ
- **Factorization Theorem (Neyman)** (Chunk 006): L = g_θ(t)·h(x)
- **Koopman's exponential family** (Chunk 006): includes binomial/Poisson/normal
- **Cramer-Rao Inequality** (Chunk 006): Var(unbiased) ≥ 1/(n·I(θ))
- **Fisher Information I(θ)** (Chunk 006): E[(∂lnf/∂θ)²]
- **Rao-Blackwell Theorem** (Chunk 006): improve unbiased estimator using sufficient statistic
- **Blackwellisation** (Chunk 006): construct φ(T) = E(U|T)
- **Convergence in probability vs in distribution** (Chunk 006)
- **Asymptotic normality** (Chunk 006): Z_n →ᴰ N
- **Mean more efficient than Median** (Chunk 006): efficiency ratio ≈ 0.64
- **Maximum Likelihood, GMM, PLS** (Chunk 006): three estimation methods

## Definitions (Chunk 006 additions)
- **Sufficient estimator** ⭐ (Chunk 006)
- **Factorization theorem** ⭐ (Chunk 006)
- **Cramer-Rao Inequality** ⭐ (Chunk 006)
- **Fisher Information** ⭐ (Chunk 006)
- **Rao-Blackwell Theorem** ⭐ (Chunk 006)
- **Convergence in distribution** ⭐ (Chunk 006)
- **Asymptotic normality** ⭐ (Chunk 006)
- **Maximum Likelihood Estimator (MLE)** ⭐ (Chunk 006)
- **GMM** ⭐ (Chunk 006)
- **PLS / PCA** (Chunk 006)
- **Completeness** (Chunk 006)

## Named Models / Laws / Theories (Chunk 006 additions)
- **Neyman-Factorization Theorem** (Chunk 006)
- **Cramer-Rao Inequality** (Chunk 006)
- **Rao-Blackwell Theorem** (Chunk 006) — Blackwell + C.R. Rao
- **Koopman's exponential family** (Chunk 006)

## Key Data & Numbers (Chunk 006 additions)
- Var(median) = πσ²/(2n) ⇒ efficiency of mean ≈ 2/π ≈ 0.64 (Chunk 006)
- Var(S²) = 2σ⁴/n for normal sample (Chunk 006)

---
*New entries from Chunk 007:*

## Key Concepts (Chunk 007 additions)
- **Hypothesis testing about parameters, not statistics** (Chunk 007)
- **Null hypothesis H₀** (Chunk 007): no-difference hypothesis (Fisher)
- **Alternative hypothesis H₁** (Chunk 007): complementary to H₀; two-tailed/right-tailed/left-tailed
- **Critical Region ω** (Chunk 007): rejection zone in sample space
- **Level of significance α** (Chunk 007): size of Type I error
- **Producer's risk vs Consumer's risk** (Chunk 007 → 008)
- **Neyman's confidence-interval technique** (Chunk 007)
- **One-tailed vs Two-tailed** (Chunk 007)

## Definitions (Chunk 007 additions)
- **Null Hypothesis H₀** ⭐ (Chunk 007)
- **Alternative Hypothesis H₁** ⭐ (Chunk 007)
- **Critical Region** ⭐ (Chunk 007)
- **Level of Significance** ⭐ (Chunk 007)
- **Confidence Interval / Limits / Coefficient** ⭐ (Chunk 007)

## Named Models / Laws / Theories (Chunk 007 additions)
- **Fisher's definition of null hypothesis** (Chunk 007)
- **Neyman's confidence-interval technique** (Chunk 007)

## Key Data & Numbers (Chunk 007 additions)
- 95% CI for normal mean: x̄ ± 1.96·σ/√n (Chunk 007)
- Coin HHT MLE: p̂ = 2/3 (Chunk 007)
- Babies (8,9,10) MLE: μ̂ = 9 (Chunk 007)
- Sixes Poisson MLE: λ̂ = 19.5 (Chunk 007)
- 5-sample best linear: t₁ has variance σ²/5 < t₂ at 5σ²/9 (Chunk 007)

---
*New entries from Chunk 009:*

## Key Concepts (Chunk 009 additions)
- **Two-sample comparison cases I/II/III** (Chunk 009): mirror single-sample cases — σ known → Z; μ known → F on variances; all unknown → pooled-t and F with df subtracted
- **Pooled variance s'²** (Chunk 009): [(n₁−1)s'₁² + (n₂−1)s'₂²]/(n₁+n₂−2)
- **Fisher's two-sample t** (Chunk 009): df = n₁ + n₂ − 2; assumes equal σ
- **F-test for variance equality** (Chunk 009): df (n₁,n₂) when μ known; (n₁−1,n₂−1) when μ estimated
- **Reduction trick u=x+ξy, v=x−ξy** (Chunk 009): turns σ_x/σ_y test into ρ_uv = 0 test
- **Paired t-test** (Chunk 009): z = x − y → univariate t with df = n − 1; for matched pairs
- **Test for ρ = 0** (Chunk 009): t = r√(n−2)/√(1−r²) ~ t(n−2)
- **Quadratic-roots construction of CI for σ_x/σ_y** (Chunk 009): may give convex/concave/imaginary cases

## Definitions (Chunk 009 additions)
- **Pooled variance s'²** ⭐ (Chunk 009)
- **Fisher's two-sample t-test** ⭐ (Chunk 009)
- **F-test for equality of variances** ⭐ (Chunk 009)
- **Sample correlation r** ⭐ (Chunk 009)
- **Paired t-test** ⭐ (Chunk 009)
- **Significant value / Critical value** ⭐ (Chunk 009, Key Words)

## Named Models / Laws / Theories (Chunk 009 additions)
- **Fisher's two-sample t-test** (Chunk 009)
- **Bivariate-normal ρ=0 t-test** (Chunk 009)
- **Paired t-test** (Chunk 009)

## Key Data & Numbers (Chunk 009 additions)
- σ_z² = σ_x² + σ_y² − 2ρσ_xσ_y for z = x − y (Chunk 009)
- σ_z² = σ_x² + σ_y² when independent (covariance term vanishes; Chunk 009 — Case I)

---
*New entries from Chunk 010:*

## Key Concepts (Chunk 010 additions)
- **Worked CYP examples** (Chunk 010): tire Z-test, melting-point t-test, bulb-life pooled-t, correlation t
- **Six §31.11 exercises** (Chunk 010): CI for μ, χ² σ-test, F variance test, two-sample t, ρ-test, paired t
- **Standard tables A1–A4 (start)** (Chunk 010): standard normal, χ², t, F at 5%

## Key Data & Numbers (Chunk 010 additions)
- Tire CYP1: z = −1.40 (Chunk 010)
- Melting-point CYP2 Q8: t = −1.149, df 11 → unbiased (Chunk 010)
- Correlation CYP4 Q1: t = 0.880 → ρ = 0 accepted (Chunk 010)
- Q2 χ²₀.₀₅,₁₄ = 23.685 (Chunk 010)
- Q3 F₀.₀₅;₉,₇ = 3.68; F₀.₀₁;₉,₇ = 6.72 (Chunk 010)
- Q4 t₀.₀₅,₂₈ = 1.701; t₀.₀₁,₂₈ = 2.467 (Chunk 010)
- Q5 t = −0.495 vs −1.782 critical → no negative correlation (Chunk 010)
- Q6 paired t = 2.493 (z̄=2.5, s_z=3.171) → significant at 5% only (Chunk 010)
- t₀.₀₅,∞ = 1.6449; t₀.₀₂₅,∞ = 1.96 (Chunk 010, A3)

---
*New entries from Chunk 011:*

## Key Concepts (Chunk 011 additions)
- **F-table at 1% level** (Chunk 011): stricter cut-offs for variance-ratio tests; complements 5% table from Chunk 010

## Key Data & Numbers (Chunk 011 additions)
- F₀.₀₁;₉,₇ = 6.72 (matches Q3 critical value, Chunk 011)
- F₀.₀₁;∞,∞ = 1.000 (Chunk 011)
- ISBN 978-93-5568-929-0; published September 2023 (Chunk 011)
