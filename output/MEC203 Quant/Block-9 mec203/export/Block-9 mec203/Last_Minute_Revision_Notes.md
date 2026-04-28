# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Aspect | Census | Sample Survey |
|---|---|---|
| Coverage | Every population unit (size N) | Subset of size n (n ≪ N) |
| Sampling error | None | Inherent and unavoidable |
| Non-sampling error | Likely (time/cost pressure) | Minimised (smaller scope, better questionnaire/staff) |
| Cost & time | Very high | Lower |
| Quality of data | Often weaker (rushed) | Often better (deeper interviews) |
| Standard error | Not produced | Produced — gives precision bounds |
- **Population**: aggregate of objects, animate or inanimate, under study; may be finite or infinite. ⭐ (exam-important)
- **Sample**: a finite subset of statistical individuals in a population. ⭐ (exam-important)
- **Parameter**: a numerical characteristic of the population (e.g., μ, σ²). ⭐ (exam-important)
- **Statistic**: a numerical characteristic computed from sample observations only (e.g., x̄, s²); R. A. Fisher's terminology. ⭐ (exam-important)

**Quick Recall:**
- μ, σ² → parameters (population, usually unknown)
- x̄, s² → statistics (sample, calculated)
- Census = no sampling error but has non-sampling error
- Sample survey = has sampling error but generally lower non-sampling error

**Quick Recall:**
- 4 advantages: cheap, deeper info, better quality, computable standard error
- The fourth advantage is unique to sampling — a census produces no SE

### Sample Design 🔴

**Random (Probability) Sampling**
- avoids systematic bias;
- allows quantifying the size of the sampling error.

**Randomization**

**With Replacement vs. Without Replacement**
- For *very large* populations, sample without replacement.
- If sample size is a small proportion of population, sample with replacement is acceptable (and simplifies derivations).

**Cost vs. Efficiency Trade-off**
- Cost rises with sample size *n*.
- Efficiency = 1 / Var(estimator). For the sample mean, Var(x̄) = σ²/n → efficiency rises with n.
- The optimal design balances these opposing forces.
- **Random sample**: a sample in which each population unit has a known, non-zero probability of being selected. ⭐ (exam-important)
- **Sampling frame**: a list of all population members; required for probability sampling.
- **Probability sampling**: sampling techniques in which each unit has a known, non-zero probability of inclusion.
- **Validity**: review that the data answer the questions of interest.
- **Pilot survey**: a small-scale pre-test of the survey method conducted before the main survey.
1. **Defining the Objectives** → identify variables, decide data type and analysis technique.
2. **Defining the Population to be Sampled** → establish a sampling frame; resolve borderline cases.
3. **Determination of the Data to be Collected** → align data with objectives; avoid irrelevant or missing items.
4. **Questionnaire / Schedule Design** → questionnaire (filled by respondents) or schedule (filled by investigators).
5. **Method of Collecting Data** → choose between questionnaire and interview methods; manage non-response (which can cause endogeneity if patterned).
6. **Choice of Sampling Units** → align with objectives.
7. **Designing the Survey** → conduct a pilot survey + decide flexible variables.
8. **Organisation of Field Work** → train field staff; supervise to minimise sampling errors.
9. **Drawing the Sample** → e.g., put numbered slips in an urn, mix, draw n.

**Why a Pilot Survey?**
- Improves field-work organisation by exposing defects.
- Improves question framing and questionnaire design.
- Trains field staff on real conditions.
- Surfaces unanticipated problems.
- Provides cost and time estimates for the main survey.

**Quick Recall:**
- Sampling frame is a *prerequisite* for probability sampling.
- Var(x̄) = σ²/n → larger n → better precision but higher cost.
- Pilot survey = small dry-run before main survey.

### Biases in the Survey 🔴

**Selection Bias and Its Sub-types**
| Sub-type | What it is | Typical example |
|---|---|---|
| **Under-coverage** | Some population members inadequately represented | Exit poll; surveys based on telephone directories or car-registration lists |
| **Non-response bias** | Selected individuals refuse / can't participate, and they differ meaningfully from respondents | Mail surveys; "call-in radio" shows on controversial topics over-represent strongly opinionated people |
| **Substitution bias** | Investigator replaces a hard-to-reach unit with a convenient one | Replacing a missing household with a neighbour |
| **Faulty demarcation of sampling units** | Borderline cases at investigator's discretion | Crop-cutting / agricultural field surveys |
| **Self-selection bias** | Subjects pick themselves; less proactive people excluded | Volunteer-only studies |
| **Recall bias** | Respondent forgets or mis-remembers | Survey asking "what did you eat last week?" |
| **Observer bias** | Researcher subconsciously projects expectations | Cherry-picking statistics that support hypothesis |
| **Survivorship bias** | Looking only at "survivors" of a pre-selection process | Reading only published case studies (success stories) |
- Response bias (people respond improperly)
- Observational bias (unrepresentative sample)
- Non-response bias
- Interviewer bias (biased frame of mind)

**Omitted Variable Bias (OVB)**
- **Selection bias**: bias resulting from an unrepresentative sample. ⭐ (exam-important)
- **Non-response bias**: arises when respondents differ in meaningful ways from non-respondents.
- **Survivorship bias**: bias from focusing only on data points that survived a pre-selection process.
- **Omitted Variable Bias (OVB)**: bias in regression estimates due to leaving out a relevant variable correlated with both the dependent and an included independent variable. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: "If I just take a bigger sample, my survey results will be unbiased." → ✅ Correct: Sample size only affects sampling error (variability). It cannot correct survey bias caused by under-coverage, non-response, etc. A large biased sample is still biased.
- ❌ Mistake: Confusing sampling error with bias. → ✅ Correct: Sampling error is random variability between samples; bias is a systematic shift.

**Quick Recall:**
- 8 selection-bias subtypes; 4 procedural-bias forms; 1 OVB.
- Bigger n → smaller sampling error, NOT smaller bias.
- For an unbiased statistic, the average of all possible sample statistics equals the true parameter.
- Sampling error is reduced by larger n; bias is not (key contrast).
- Probability sampling [Section: Sample Design] is the antidote for several biases (it allows the *known* probability of inclusion that bias often violates).

### Types of Sampling 🔴

**A. Non-probability Sampling**
1. Some population units have **zero probability** of selection.
2. Selectable units have an **unknown** non-zero probability.
3. Sampling errors **cannot be quantified**.
| Type | Mechanism | Example |
|---|---|---|
| **Convenience Sampling** | Pick whoever is in the vicinity / accessible | Reporters approaching people in a market for political opinion |
| **Judgement Sampling** | Expert opinion picks individuals | Research firm filtering people through qualifying questions for a focus group; TV-show panellists |
| **Quota Sampling** | Specifies quotas on age, gender, social class, etc. to mirror population | Survey requiring "30 females aged 25-40, 30 males aged 25-40, …" |

**B. Probability Sampling**
| Type | What it does | Where it's best |
|---|---|---|
| **Simple Random Sampling (SRS)** | Each unit has equal probability | Simple; produces unbiased estimates; baseline for theory |
| **Systematic Random Sampling** | Random start, then every k-th element where k = N/n | Use only if population is logically homogeneous; researcher must ensure k has no pattern |
| **Stratified Random Sampling** | Population split into homogeneous strata; SRS within each stratum | When natural groupings exist (gender, age); higher accuracy (smaller SE); broad cross-section |
| **Cluster Sampling** | Population split into heterogeneous clusters; SRS of clusters; survey all units in chosen clusters (one-stage) or subsample (two-stage) | Cost reduction; useful for geographically dispersed populations |
| **Multistage Sampling** | Sample primary units, then secondary, then tertiary, … | Large government surveys (often combine stratification + clustering) |

**Stratified vs. Cluster — the contrast**
| Aspect | Stratified | Cluster |
|---|---|---|
| Within-group | Homogeneous | Heterogeneous |
| Between-group | Heterogeneous | Homogeneous (ideally) |
| Sampling rule | Sample from *every* stratum | Sample *some* clusters; survey all (or sub-sample) units in chosen ones |
| Goal | Higher accuracy (smaller SE) | Lower cost |
| Stages | Generally one-stage | One-stage or multi-stage |

**Tippet's Random Numbers Table**
- **Non-probability sampling**: selection without a sampling frame; some units have zero probability and the rest unknown probability. ⭐
- **Probability sampling**: every unit has a known, non-zero probability of selection.
- **Simple Random Sampling (SRS)**: each unit has *equal* probability; produces unbiased estimates.
- **Systematic random sampling**: select an initial element at random, then every k-th element (k = N/n). ⭐
- **Stratified random sampling**: divide heterogeneous population into homogeneous strata, then SRS within each. ⭐
- **Cluster sampling**: divide population into heterogeneous clusters, SRS of clusters; one-stage or multi-stage. ⭐
- **Multistage sampling**: sequential sampling at two or more successive stages.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing stratified and cluster sampling. → ✅ Correct: Strata are sampled *all*; clusters are sampled *some*. Strata are homogeneous internally; clusters are (ideally) heterogeneous internally.

**Quick Recall:**
- Non-probability: convenience / judgement / quota
- Probability: SRS / systematic / stratified / cluster / multistage
- Tippet's table = 10,400 four-digit numbers
- Standard errors are **only** computable for probability samples
- Builds on: **Sampling Frame** (Chunk 001) — distinguishes probability from non-probability methods.
- Prerequisite for: **Standard Error** (later in this chunk) — derivations assume probability sampling.

**Quick Recall:**
- Parameter = constant of the population
- Statistic = function of sample data
- Sampling fluctuations = sample-to-sample variation in a statistic

### Sampling Distribution of a Statistic 🔴

**Definition**

**Number of Possible Samples**

**Unbiasedness of x̄**

**Worked Example (Source Text)**
- Population: N = 3, values x₁ = 1, x₂ = 3, x₃ = 5. So μ = 3.
- Sample size n = 2 → number of samples = ³C₂ = 3.
  - Sample 1: (1,3) → x̄₁ = 2
  - Sample 2: (3,5) → x̄₂ = 4
  - Sample 3: (1,5) → x̄₃ = 3
- E(x̄) = (2 + 4 + 3)/3 = 3 = μ ✓

**Standard Error of x̄**

**Probable Error**
- **Sampling distribution**: probability distribution of all possible values of a sample statistic. ⭐ (exam-important)
- **Standard error (SE)**: the standard deviation of the sampling distribution of a statistic. ⭐ (exam-important)
- **Probable error**: 0.6745 × standard error.

**Quick Recall:**
- E(x̄) = μ → x̄ is unbiased
- σ_x̄ = σ/√n
- Probable error = 0.6745 × SE
- Number of possible samples (without replacement) from finite N = ᴺCₙ
- Builds on: **Probability Sampling** (Section: Types of Sampling, this chunk).
- Foundation for: **Hypothesis Testing** (Unit 31, later chunks).

### Standard Error 🔴

**What Drives SE**
- **Population spread (σ)**: more spread → more scope for sampling error → larger SE.
- **Sample size (n)**: larger n → tighter dispersion → smaller SE.

**Table 28.1 — Standard Errors of Common Statistics (Large Samples)**
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
1. **Index of precision** — the magnitude of SE measures how precise the estimate is; the **reciprocal of SE = measure of reliability**.
2. **Determines probable limits** — given x̄ ± k·SE for some k tied to the desired confidence level, we can construct an interval likely to contain the population parameter.
- **Standard error (SE)** ⭐: the standard deviation of the sampling distribution of a statistic.

**Quick Recall:**
- Mean SE = σ/√n
- Proportion SE = √(PQ/n)
- Median SE = 1.25331·σ/√n (so median is less efficient than mean)
- Reciprocal of SE = reliability
- Quadrupling n halves SE (√n behaviour)

### Expectation and Standard Error of Sample Mean 🔴
- Population mean: μ = (1/N)·ΣXₐ.
- Population variance: σ² = (1/N)·Σ(Xₐ − μ)².
- Sample mean: x̄ = (1/n)·Σxᵢ.
- Probability theorems used:

**Case I — Random Sampling **With** Replacement**
- For each i: xᵢ takes values X₁,…,Xₙ each with probability 1/N.
- E(xᵢ) = ΣXₐ·(1/N) = μ
- Var(xᵢ) = Σ(Xₐ − μ)²·(1/N) = σ²
- Independence of xᵢ, xⱼ (i ≠ j) → cov(xᵢ, xⱼ) = 0.
- ⇒ E(x̄) = (1/n)·n·μ = μ
- ⇒ Var(x̄) = (1/n²)·n·σ² + 0 = σ²/n
- **Standard error: σ_x̄ = σ/√n**

**Case II — Random Sampling **Without** Replacement**
- For each i: E(xᵢ) = μ, Var(xᵢ) = σ² (same as Case I, since the marginal distribution of each xᵢ is unchanged).
- The covariance term is **non-zero** here because once one unit is drawn, the conditional distribution of the next changes. (Derivation continues in **chunk 003**, where the finite population correction √[(N−n)/(N−1)] enters.)

**Quick Recall:**
- With replacement: σ_x̄ = σ/√n
- Without replacement: SE includes finite population correction (FPC)
- x̄ is unbiased in both cases: E(x̄) = μ
- Builds on: probability theorems (E(bx) = bE(x), E(x+y) = E(x)+E(y)).
- Continues into: SE of sample proportion + finite population correction (Chunk 003).

### Expectation and Standard Error of Sample Proportion 🔴
- x → f/n (sample proportion p̂),
- μ → P (population proportion),
- σ² → PQ (Bernoulli variance, where Q = 1 − P).

**With Replacement**
- E(f/n) = P → p̂ is unbiased.
- σ_p̂ = √(PQ/n)

**Without Replacement (Finite Population Correction)**
- E(f/n) = P (still unbiased).
- σ_p̂ = √(PQ/n) · √[(N − n)/(N − 1)]
- **Sample proportion (p̂)**: f/n, the fraction of the sample with the attribute of interest. ⭐ (exam-important)
- **Finite Population Correction (FPC)**: the factor √[(N − n)/(N − 1)] applied when sampling without replacement from a finite population. ⭐ (exam-important)

**Quick Recall:**
- σ_p̂ = √(PQ/n) (with replacement)
- σ_p̂ = √(PQ/n)·√[(N−n)/(N−1)] (without replacement, finite population)
- FPC ≈ 1 when n ≪ N
- Builds on: SE of sample mean derivation (Chunk 002).
- Used in: pineapple defective example (worked exercise below).
| Term | Definition |
|---|---|
| **Cluster Sampling** ⭐ | Population divided into clusters, ideally heterogeneous within and homogeneous between |
| **Quota Sampling** | Representative sample by specifying quotas on age, gender, social class etc. |
| **Population** | Aggregate of objects, animate or inanimate, under study; finite or infinite |
| **Purposive Sampling** | Sampling units selected with a definite purpose in view |
| **Random Sampling** ⭐ | Each unit of population has known probability of inclusion |
| **Sample** | Finite subset of statistical individuals; sample size = number in the sample |
| **Sampling Distribution** ⭐ | Probability distribution of all possible values of a sample statistic |
| **Sampling Without Replacement** | Once selected, an element cannot reappear |
| **Sampling With Replacement** | Selected element returns to population; can be selected again |
| **Standard Error** ⭐ | Standard deviation of the sampling distribution of a statistic |
| **Stratified Sampling** ⭐ | Population divided into homogeneous groups (strata); SRS within each |
| **Unbiased** ⭐ | Property: E(estimator) = parameter |

### Unit 28 — Worked Exercises 🔴

**Example: Defective Pineapples**
- Sample n = 500 pineapples; 65 found defective.
- Sample proportion: p̂ = 65/500 = 0.13.
- SE = √(p̂(1−p̂)/n) = √(0.13·0.87/500) = **0.022**.
- 95% CI: p̂ ± 1.96·SE = 0.13 ± 1.96·0.022 = **[0.086, 0.174]**, i.e., 8.6% to 17.4%.
- Conclusion: with 95% confidence, the true defective rate lies between 8.6% and 17.4%.

**Example: Sample Mean from Population**
- N is large; population μ = 100, σ = 20; sample size n = 225.
- Sample mean has μ_x̄ = 100, σ_x̄ = 20/√225 = **1.33**.

**Example: Probability that |x̄ − μ| < 0.5 day**
- Mean germination time μ = 22, σ = 2.3, sample size n = 160.
- Required: P(|x̄ − μ| < 0.5) = **0.9940**.

**Example: Vehicle Speeds**
- Speeds are N(36.6, 1.7²).
- (a) P(35 < X < 40) = **0.8036** (single observation).
- (b) For sample of n = 20, P(35 < x̄ < 40) ≈ **1.0000**.

**Example: Marriage Duration**
- μ = 7.8 years, σ = 1.2 years, n = 75.
- Required probability ≈ **0.9251**.

**Quick Recall:**
- For proportion CI: p̂ ± z_(α/2) · √(p̂(1−p̂)/n)
- 95% z = 1.96; 99% z = 2.58
- Sample-mean CI: x̄ ± z·σ/√n

**Quick Recall:**
- Knowledge of sampling distribution = key to both estimation and hypothesis testing.
- For finite population, count is ᴺCₙ.

### Three Fundamental Distributions Derived from Normal — Chi-square 🔴

**Definition**

**Probability Density Function**

**Shape**
- For n ≤ 2: density is monotonically decreasing.
- For n > 2: unique maximum (mode) at χ² = n − 2.
- Always **positively skewed**.

**Additive Property of χ²**
1. Verify n = 1 case directly using transformation z = x² (two-to-one map from x to z).
2. Assume true for n = t; consider U = Σx²ᵢ (i=1..t) and 𝔠 = x²_(t+1) (independent χ²(1)).
3. Apply one-to-one polar-style transformation (u = u'·cos θ, 𝔠 = u'·sin θ).
4. Compute Jacobian J = u'.
5. Integrate out θ using the Beta function ∫cos²θ·dθ = B(½,½)/2 etc.
6. Resulting marginal of u'² has the χ²(t+1) form ⇒ induction closes.
- **Chi-square variate (χ²)** ⭐ (exam-important): sum of squares of independent standard normal variates.
- **Degrees of freedom (df)** ⭐: parameter n governing shape; equals number of independent squared normals being summed.
- **Additive property of χ²** ⭐: independent χ² with df n₁, n₂ sum to χ² with df (n₁ + n₂).
- **Jacobian transformation**: technique for finding the density of a transformed random variable using the determinant of partial derivatives.

**Quick Recall:**
- χ²₁ = Z² (square of one standard normal)
- χ² ≥ 0 always; positively skewed
- Mode at n − 2 (for n > 2)
- Sum of independent χ²s is χ² with df added
- Used in: variance tests, goodness-of-fit, contingency tables
- Builds on: properties of standard normal distribution (assumed prior).
- Foundation for: t-distribution and F-distribution (next chunk).
- Used in: chi-square goodness-of-fit test (Chunk 004), variance tests (Chunk 008).

### Chi-square — Critical Values and Two Key Properties 🔴
- the difference of two nested χ²'s is itself χ²,
- in a normal sample, x̄ and S² are independent and (n−1)S²/σ² ~ χ²(n−1).

**Large-n Approximation**

**Critical Values**
- χ²(α, n) = upper α point: P[χ² > χ²(α, n)] = α (right tail).
- Lower α point = χ²(1 − α, n).
- As n increases, critical values increase; as α decreases, critical values increase.

**Moment Generating Function Derivation (additive property)**

**Property 1 — Subtraction**

**Property 2 — Sample Mean and Variance from Normal**
- (a) **x̄ and S² are independent.**
- (b) **(n − 1)S²/σ² ~ χ²(n − 1).**

**Proof Sketch of (b)**
- **Critical value of χ²** ⭐: the value χ²(α, n) such that P[χ² > χ²(α, n)] = α.
- **Significant value**: synonymous with critical value.

**Quick Recall:**
- For n > 30: √(2χ²) ≈ N(√(2n−1), 1)
- x̄ ⊥ S² (independence) for normal samples — *unique* to normality
- (n−1)S²/σ² ~ χ²(n−1) — basis for variance tests and CIs for σ²
- MGF of χ²(n): M(t) = (1−2t)^(−n/2)

### Chi-square Test of Goodness of Fit (Karl Pearson) 🔴
- Observed frequencies: O₁, O₂, …, Oₙ (from data)
- Expected frequencies: E₁, E₂, …, Eₙ (from theory; ΣEᵢ = ΣOᵢ)
- Test statistic:
- df = n − 1 (we lose 1 df due to the constraint ΣOᵢ = ΣEᵢ).
- Reject H₀ at level α if computed χ² > χ²(α, n − 1).
- **Goodness of fit** ⭐: assessment of how well theoretical frequencies match observed frequencies.
- **Pearson's χ² statistic** ⭐: Σ(Oᵢ − Eᵢ)²/Eᵢ.

**Quick Recall:**
- Formula: Σ(O − E)²/E
- df = (number of categories) − 1
- Approximate test (large n)
- Builds on: chi-square distribution (Section: Chi-square, this chunk and Chunk 003).
- Applications: digit-uniformity test, dice-bias test (Check Your Progress 1, Chunk 004 questions).

### Student's t-Distribution 🔴

**Definition**

**Probability Density Function**

**Special Cases**
- ν = 1 → standard **Cauchy distribution**: f(t) = 1/[π(1 + t²)].
- ν → ∞ → standard normal.

**Symmetry**
- **Student's t** ⭐: t = (x̄ − μ)/(s/√n) when σ unknown; df = n − 1.
- **Cauchy distribution**: special case of Student's t with df = 1.

**Quick Recall:**
- df = n − 1
- More peaked than normal but heavier tails for small df
- df = 1 → Cauchy
- Use t when σ is unknown and estimated by s

**Quick Recall:**
- Fisher's t = N(0,1) / √(χ²(n)/n)
- Student's t ⊂ Fisher's t
- For large n: t ≈ z

### Snedecor's F Distribution 🔴

**Definition**

**Properties**
- Distribution depends only on (n₁, n₂); independent of population parameters.
- Highly **positively skewed**.
- Special case: with n₁ = 1, F = t² where t has df n₂.
- **Reciprocal property:**

**Probability Density Function**
- **F-statistic / F-distribution (Snedecor's F)** ⭐: ratio of two independent χ² variates each over their df. ⭐

**Quick Recall:**
- F(n₁, n₂) — first df is for numerator
- Only positive values; skewed right
- Tables publish only upper α; lower comes from reciprocal
- F with n₁=1 corresponds to t²
- Builds on: chi-square distribution.
- Used in: variance-ratio test, ANOVA, two-sample variance comparison (Chunks 008–010).

### Sampling Distributions of Mean and Variance from a Normal Distribution 🔴
1. **x̄ ~ N(μ, σ²/n)** — sample mean is itself normally distributed.
2. **(n−1)s²/σ² ~ χ²(n−1)** — the sample variance follows a scaled χ² distribution.
3. **x̄ and s² are independent** — a property unique to the normal distribution.
- y₁ = (1/√n) · Σ(xᵢ − μ)/σ = √n·(x̄ − μ)/σ
- y_i (i = 2,…,n) = orthogonal contrasts (e.g., (1,−1,0,…,0)/√2, (1,1,−2,0,…,0)/√6, …)
- All (n−1) contrast vectors are mutually orthogonal and orthogonal to (1/√n,…,1/√n).
1. Jacobian J = σⁿ.
2. Σyᵢ² = Σ(xᵢ − μ)²/σ² (preserved by orthogonal transform).
3. Joint p.d.f of y₁,…,yₙ: ∏ N(0,1) — i.e., n iid standard normals.
4. y₁ alone gives x̄: marginal x̄ ~ N(μ, σ²/n).
5. Σyᵢ² (i=2..n) = Σyᵢ² − y₁² = Σ(xᵢ − μ)²/σ² − n(x̄ − μ)²/σ² = Σ(xᵢ − x̄)²/σ² = (n−1)s²/σ².
6. As (n−1) independent N(0,1) squared, this sum is χ²(n−1).
7. Independence of y₁ and (y₂,…,yₙ) ⇒ independence of x̄ and s².

**p.d.f. of x̄**

**p.d.f. of s²**
- **Independence of x̄ and s² in normal sampling** ⭐: uniquely holds in normal samples; foundational for Student's t-test.

**Quick Recall:**
- Normal sample of size n: x̄ ~ N(μ, σ²/n); (n−1)s²/σ² ~ χ²(n−1); x̄ ⊥ s².
- Independence of x̄ and s² is what allows the t-statistic to be a ratio of independent normal/√(χ²/df).
- Builds on: chi-square distribution (this chunk).
- Foundation for: Student's t-test in Unit 31 (Chunks 008–009).

**Quick Recall:**
- s² is a scaled χ² distribution
- (n−1)s²/σ² ~ χ²(n−1)

### Central Limit Theorem 🔴

**Setup — Law of Large Numbers**

**Statement of CLT**

**Practical Form (iid version)**

**Conventions**
- **n ≥ 30** is the common rule of thumb for CLT to "kick in" in practice.
- Sampling done with replacement (or n ≪ N).
- **Central Limit Theorem (CLT)** ⭐: under general conditions, the sum of n independent random variables is asymptotically normal as n → ∞.
- **Law of Large Numbers**: the probability that x̄ lies near μ tends to 1 as n increases.

**Quick Recall:**
- CLT: x̄ → N(μ, σ²/n) as n → ∞
- Rule of thumb: n ≥ 30
- Works for sums and averages, regardless of underlying distribution
- Foundation of normal-test approximation for many distributions (binomial, Poisson, etc.)
- Builds on: law of large numbers.
- Foundation for: large-sample tests in Unit 31 (use of normal critical values for large n).
| Term | Definition |
|---|---|
| **Central Limit Theorem** ⭐ | iid sum is asymptotically normal |
| **Chi-square Distribution** ⭐ | square of standard normal = χ²(1) |
| **F Distribution** ⭐ | F = (X/n₁)/(Y/n₂) for independent χ²s |
| **Fisher's t Distribution** ⭐ | t = T/√(χ²/n), T ~ N(0,1) |
| **Standard Normal Distribution** | continuous variable, mean 0, variance 1 |
| **Student's t Distribution** ⭐ | t = (x̄−μ)/(σ/√n) (text uses σ — typo for s); df = n−1 |

### Unit 29 Worked Exercises 🔴

**Example: 9:3:3:1 Goodness-of-Fit Test**
- 1600 bins predicted to split 9:3:3:1 across groups A, B, C, D.
- Observed: 882, 313, 287, 118.
- Expected: E_A = (9/16)·1600 = 900; E_B = E_C = (3/16)·1600 = 300; E_D = (1/16)·1600 = 100.
- Compute χ² = Σ(Oᵢ − Eᵢ)²/Eᵢ ≈ **4.7266**.
- Tabulated χ²(0.05, 3) = **7.815**.
- 4.7266 < 7.815 → **accept H₀** (theory is supported).

**Example: t-Test for Bulb Life**
- CEO claim: average bulb life = 300 days.
- Sample n = 15, x̄ = 290, s = 50.
- Test stat: t = (290 − 300)/(50/√15) = −10/12.910 = **−0.7745966**.
- df = n − 1 = 14.
- Cumulative probability = **0.226** → 22.6% chance of seeing x̄ ≤ 290 if μ = 300 is true.

**Quick Recall:**
- 9:3:3:1 problem: χ² = 4.73 vs critical 7.82 → accept H₀
- Bulb-life t = −0.77 (df=14) → P = 0.226 → don't reject

**Quick Recall:**
- Inference splits into estimation + hypothesis testing.
- Point estimate = single number; interval estimate = range with confidence.
- **Parameter space (Θ)** ⭐: set of all possible values of the unknown parameter(s).

**Quick Recall:**
- Θ = admissible parameter values
- Family of distributions {f(x;θ): θ ∈ Θ}
- Estimator = a function of sample data

### Characteristics of Estimators 🔴

**Definition**

**Examples**
1. **Sample mean** x̄ for population mean μ: E(x̄) = μ ⇒ unbiased.
2. **Sample proportion** for binomial parameter θ: with X ~ Binomial(n, θ), E(X/n) = (1/n)·E(X) = (1/n)·nθ = θ ⇒ X/n unbiased.
3. **Sample variance** S² for σ² of an *infinite* population: E(S²) = σ². However, S² is **not** an unbiased estimator of finite-population variance, and S is **not** an unbiased estimator of σ (square root creates bias).

**Bias**
- b(θ) > 0 → positively biased; b(θ) < 0 → negatively biased.

**Caveats**
- Unbiasedness is **not** preserved under non-linear functional transformations: ψ(θ̂) is generally biased even when θ̂ is unbiased.
- Unbiased estimators are **not unique** — multiple may exist.
- Unbiasedness is a property defined for finite n.

**Quick Recall:**
- x̄ is unbiased for μ; X/n unbiased for binomial p.
- S² unbiased for σ² of infinite population; S biased for σ.
- Bias = E(estimator) − parameter.

**Definition**

**Khinchin's Weak Law of Large Numbers**

**Sufficient Conditions for Consistency**
1. E(T_n) → τ(θ) as n → ∞ (asymptotic unbiasedness)
2. Var(T_n) → 0 as n → ∞.

**Caveats**
- Many consistent estimators may exist for the same parameter; e.g., T_n + a/φ(n), T_n·{1 + a/φ(n)} for any constant a, increasing function φ.
- Consistency is a *large-n* property; it says nothing about finite-n behaviour.

**Quick Recall:**
- Consistency = convergence in probability to the parameter.
- Sufficient conditions: asymptotic unbiased + Var → 0.
- x̄ is always consistent for μ (Khinchin's WLLN).

**Definition**

**Most Efficient Estimator**

**Efficiency E**

**Minimum Variance Unbiased Estimator (MVUE)**
1. T is unbiased for τ(θ) for all θ ∈ Θ.
2. Among the class of all unbiased estimators of τ(θ), T has the smallest variance.

**Important Theorems for MVUE**
- **Uniqueness**: if T₁ and T₂ are both MVUE for ψ(θ), then T₁ = T₂.
- **Correlation bound**: if T₁, T₂ are unbiased with efficiencies e₁, e₂ and correlation ρ:
- **MVUE correlation rule**: if T₁ is MVUE and T₂ is any unbiased estimator with efficiency e₀, then ρ(T₁, T₂) = √e₀.

**Worked Sketch — x̄ is MVUE of μ for normal population**
- Density: f(x) = (1/(σ√(2π)))·exp[−(x−μ)²/(2σ²)].
- ln f(x) = −ln(σ√(2π)) − (x − μ)²/(2σ²).
- ∂lnf/∂μ = (x − μ)/σ².
- E[(∂lnf/∂μ)²] = E[(x − μ)²]/σ⁴ = 1/σ².
- Cramer-Rao bound (preview, Chunk 006): Var(estimator) ≥ 1/(n·E[(∂lnf/∂μ)²]) = σ²/n.
- Var(x̄) = σ²/n attains this bound ⇒ **x̄ is MVUE of μ**.
- **Unbiased estimator** ⭐: E(T) = θ.
- **Consistent estimator** ⭐: T_n →ᴾ θ as n → ∞.
- **Efficient estimator** ⭐: smallest asymptotic variance among consistent, asymptotically normal estimators.
- **Most Efficient Estimator**: minimal sampling variance among rivals.
- **Minimum Variance Unbiased Estimator (MVUE)** ⭐: unbiased + smallest variance among all unbiased.
- **Bias b(θ)** = E(T) − τ(θ).

### ⚠️ Common Mistakes
- ❌ Mistake: assuming ψ(θ̂) is unbiased whenever θ̂ is. → ✅ Correct: unbiasedness fails under non-linear transformations.
- ❌ Mistake: thinking "consistent" means "unbiased". → ✅ Correct: a consistent estimator may be biased for finite n; it just gets better as n grows.

**Quick Recall:**
- Four properties of a good estimator: unbiased, consistent, efficient, sufficient.
- x̄ is unbiased + consistent + MVUE for normal μ.
- Efficiency E = V_min / V_estimator ≤ 1.
- Sample variance S² is unbiased for σ² of infinite population only.
- Builds on: sampling distribution (Chunks 002–004).
- Continues into: Sufficiency, Cramer-Rao, Rao-Blackwell, asymptotic properties (Chunk 006).

**Quick Recall:**
- Mean is more efficient than median (for normal data).
- Efficiency = Var(best)/Var(rival) ≤ 1.

### Sufficiency 🔴

**Definition**

**Factorization Theorem (Neyman)**

**Notes**
- "Independent of θ" means neither in the function nor in its domain.
- The original full sample (X₁,…,Xₙ) is *always* a sufficient statistic.

**Koopman's Exponential Family**

**Invariance Property**

**Fisher–Neyman Criterion**
- **Sufficient estimator** ⭐: an estimator that contains all the sample information about the parameter.
- **Factorization theorem** ⭐ (Neyman): L = g_θ[t(x)] · h(x).
- **Exponential family of distributions**: L = g(x)·h(θ)·exp{a(θ)w(x)} (Koopman's form).
- **Invariance property of sufficiency**: 1-1 functions of sufficient statistics are sufficient for the corresponding 1-1 function of the parameter.

**Quick Recall:**
- Sufficient = full sample info about θ
- Factorization: L = g_θ[t(x)]·h(x)
- Exponential family ⇒ has a sufficient statistic
- Whole sample is always sufficient
- Builds on: parameter space, estimator definitions (Chunk 005).
- Used in: Rao-Blackwell theorem (next section).

### Cramer-Rao Inequality 🔴

**Statement**

**Fisher Information**

**Regularity Conditions (5 conditions)**
1. Parameter space Θ is a non-degenerate open interval on ℝ¹.
2. ∂f(x,θ)/∂θ exists for almost all x (the exceptional set independent of θ).
3. Range of integration is independent of θ → f(x,θ) differentiable under integral sign.
4. Conditions of uniform convergence are satisfied → differentiation under integral sign is valid.
5. I(θ) > 0 exists for all θ ∈ Θ.

**Minimum Variance Bound (MVB) Estimator**
- **Cramer-Rao Inequality** ⭐: Var(unbiased) ≥ 1/[n·E[(∂lnf/∂θ)²]].
- **Fisher Information I(θ)** ⭐: measures information in the sample about θ.
- **Minimum Variance Bound (MVB) Estimator**: attains the Cramer-Rao bound.

**Quick Recall:**
- CR-bound: Var(θ̂) ≥ 1/(n·I(θ)).
- I(θ) = E[(∂lnf/∂θ)²].
- More info → smaller variance.
- 5 regularity conditions required.
- **Rao-Blackwell Theorem** ⭐: technique for variance reduction via sufficient statistics.

**Quick Recall:**
- Rao-Blackwell: condition on a sufficient statistic to reduce variance.
- Sufficient + Complete → MVUE.
- MVB ≠ MVUE always; CR-bound may not be tight.

### Asymptotic Properties 🔴

**Sufficient Condition (corollary of Chebyshev)**

**Worked Example: S² consistent for σ² (Normal Population)**
- E(S²) = σ² (unbiased).
- Var(S²) = 2σ⁴/n → 0 as n → ∞.
- Hence S² is a consistent estimator of σ² for a normal population.

**Convergence in Distribution**

**Asymptotic Normality**

**Central Limit Theorem (restated)**
- **Convergence in probability** ⭐: P(|Z_n − Z| > ε) → 0.
- **Convergence in distribution** ⭐: c.d.f. of Z_n → c.d.f. of Z pointwise.
- **Asymptotic normality** ⭐: Z_n →ᴰ N(μ, σ²).

**Quick Recall:**
- Asymptotic unbiased: E(θ̂_n) → θ.
- Consistent: θ̂_n →ᴾ θ; sufficient condition = unbiased + Var → 0.
- Asymptotic normal: Z_n →ᴰ N.
- CLT: standardised sample mean → N(0,1).
- S² is consistent for σ² in normal samples (Var(S²) = 2σ⁴/n).

### Methods of Estimation 🔴

**Idea**

**Maximisation Trick**

**Properties**
- For large samples, MLE gives an "excellent" estimator of θ.
- MLE is consistent and asymptotically efficient (asymptotically achieves Cramer-Rao bound under regularity).

**Idea**

**Properties**
- Consistent, asymptotically normal, and most efficient in the class of estimators using only the moment conditions.
- More **robust** than ML because it doesn't assume the full distribution.

**Idea**
- Number of explanatory variables is large compared to observations, OR
- Explanatory variables are correlated.

**Tool: Principal Component Analysis (PCA)**
- **Maximum Likelihood Estimator (MLE)** ⭐: argmax of L(θ).
- **Generalized Method of Moments (GMM)** ⭐: estimator from sample moment conditions.
- **Partial Least Squares (PLS)**: dimension-reduction estimation via PCA.
- **Principal Component Analysis (PCA)**: reduces dimensionality preserving most information.

### ⚠️ Common Mistakes
- ❌ Mistake: Maximising L(θ) directly — often algebraically painful. → ✅ Correct: Maximise log L(θ); same maximiser, easier algebra.

**Quick Recall:**
- ML: maximise L(θ) (or log L).
- GMM: replace E[g(Y,θ)]=0 by sample average; more robust.
- PLS: dimension reduction with PCA for many correlated regressors.
- ML uses the full distribution → leads to MVB attainment under regularity.
- GMM is a relaxation: uses only moments.
- Continues into worked MLE problems (Chunk 007).
| Term | Definition |
|---|---|
| **Central Limit Theorem** ⭐ | iid sample mean is asymptotically normal |
| **Completeness** | Different distributions distinct under different parameter values; needed for MVUE uniqueness via sufficient statistic |
| **Cramer-Rao Inequality** ⭐ | Var(unbiased) ≥ {[ψ'(θ)]² / I(θ)} where I(θ) = E[(∂lnL/∂θ)²] — lower bound on variance |
| **Consistency** ⭐ | T_n →ᴾ τ(θ) (convergence in probability) |
| **Efficiency** ⭐ | Best estimator has smallest avar among consistent + asymptotically normal estimators |
| **Generalized Method of Moments** | Uses moment conditions instead of full distribution; more robust than ML |
| **Maximum Likelihood** ⭐ | Maximise L(θ) (or log-likelihood) to obtain MLE |
| **Minimum Variance Unbiased Estimator** ⭐ | Unbiased + smallest variance among all unbiased estimators |
| **Most Efficient Estimator** | Smallest sampling variance among rivals; E = V₁/V₂ ≤ 1 |
| **Parameter Space** ⭐ | Set Θ of all possible values of θ |
| **Partial Least Squares** | Estimation when many correlated regressors; uses PCA to reduce dimensionality |
| **Sufficiency** ⭐ | T captures all sample information about θ; conditional dist of sample given T is independent of θ |

### Unit 30 — Worked Examples 🔴

**Q3: Is x̄ + (1/n)Σxᵢ² unbiased for μ² + 1?**
- Given: X₁,…,Xₙ ~ N(μ, 1) (so Var(Xᵢ) = 1).
- E(Xᵢ²) = Var(Xᵢ) + [E(Xᵢ)]² = 1 + μ².
- E[x̄ + (1/n)·Σxᵢ²] = μ + (1/n)·Σ E(Xᵢ²) = μ + (1/n)·n(1 + μ²) = μ + 1 + μ². 

**Q4: Best Linear Estimator from 5 Normal Samples**
- Sample (X₁,…,X₅) of size 5 from N(μ, σ²) with unknown μ.
- Estimators:
  - t₁ = (X₁ + X₂ + X₃ + X₄ + X₅)/5
  - t₂ = (2X₁ + X₂ + λX₃)/3
- Unbiasedness: E(t₁) = μ; for t₂, E = (2μ + μ + λμ)/3 = μ requires (3+λ)/3 = 1 ⇒ λ = 0.
- Variances:
  - V(t₁) = (1/25)·5σ² = σ²/5
  - V(t₂) = (4σ² + σ²)/9 = 5σ²/9 (using λ = 0)
- Since V(t₁) = σ²/5 = 0.2σ² < V(t₂) = 5σ²/9 ≈ 0.556σ², **t₁ is the better (lower-variance) unbiased estimator**.

**Q5: Sufficient Statistic for θ**
- Sample x₁,…,xₙ from f(x, θ) = θx^(θ−1) for 0 < x < 1, θ > 0.
- Likelihood: L(x, θ) = ∏θxᵢ^(θ−1) = θⁿ·(∏xᵢ)^(θ−1).
- Set t₁ = ∏xᵢ. Then L = θⁿ·t₁^(θ−1) · 1 = g(t₁, θ)·h(x).
- By **Factorization Theorem**, **t₁ = ∏xᵢ is sufficient for θ**.

**Q3: MLE for biased coin (HHT)**
- Likelihood: L(p) = P(HHT) = p²(1 − p).
- ℓ(p) = 2 ln p + ln(1 − p).
- dℓ/dp = 2/p − 1/(1 − p) = 0 ⇒ 2(1 − p) = p ⇒ **p̂_MLE = 2/3**.

**Q4: MLE for power-family density**
- Density: f(x|θ) = (θx^(θ−1))/2^θ on 0 ≤ x ≤ 2.
- Log-likelihood: ln L = Σ[ln θ + (θ − 1) ln xᵢ − θ ln 2] = n ln θ + (θ − 1)Σ ln xᵢ − nθ ln 2.
- ∂ ln L/∂θ = n/θ + Σ ln xᵢ − n ln 2 = 0
- ⇒ **θ̂_MLE = n / (n ln 2 − Σ ln xᵢ)**.

**Q1: Cauchy population**
- f(x, θ) = (1/π)·1/(1 + (x − θ)²).
- L(x, θ) = (1/πⁿ)·∏ 1/(1 + (xᵢ − θ)²) — does **not** factor as g(t, θ)·h(x) with a single statistic t.
- Hence **no single sufficient statistic** for θ in Cauchy.
- The full sample (X₁,…,Xₙ) is jointly sufficient.

**Q2: MLE of μ for normal — three baby weights**
- Babies weigh 8, 9, 10 ounces.
- Maximise ∏ (1/(σ√(2π)))·exp[−(xᵢ − μ)²/(2σ²)].
- Log-likelihood: −3 ln(σ√(2π)) − (1/(2σ²))[(8−μ)² + (9−μ)² + (10−μ)²].
- ∂/∂μ: (1/σ²)·[(8−μ) + (9−μ) + (10−μ)] = 0 ⇒ **μ̂_MLE = (8+9+10)/3 = 9**.

**Q3: Poisson MLE for sixes**
- Counts: 14, 27, 25, 12. Likelihood = ∏ (λ^xᵢ·e^(−λ)/xᵢ!).
- log L = (Σxᵢ)·ln λ − nλ − Σ ln(xᵢ!).
- d/dλ = Σxᵢ/λ − n = 0 ⇒ **λ̂_MLE = (Σxᵢ)/n = (14 + 27 + 25 + 12)/4 = 78/4 = 19.5**.

**Q4: MLE of normal mean is unbiased**
- μ̂_MLE = (1/n)·ΣXᵢ = x̄.
- E(x̄) = (1/n)·Σ E(Xᵢ) = (1/n)·nμ = μ. **Unbiased**. ✓

**Quick Recall:**
- Coin HHT MLE: 2/3
- Normal mean MLE = sample mean
- Poisson λ MLE = sample mean
- Cauchy: whole sample is sufficient (no single sufficient statistic)
- For factorisation: L = g(t,θ)·h(x) ⇒ t sufficient

### Tests of Significance 🔴
- For large n, many distributions (binomial, Poisson, NB, hypergeometric, t, F, χ²) → approximated by normal → use **normal test of significance**.
- Common tests for *small* samples: t-test, F-test, Fisher's z-transformation.

**Quick Recall:**
- Hypothesis testing is about population parameters.
- Large n → normal test; small n → t, F, z-transformation.

### Null Hypothesis 🔴
- For a single statistic: H₀ asserts no significant difference between sample statistic and hypothetical parameter.
- For two-statistic comparison: H₀ asserts no significant difference between the two statistics.
- We compute P that the observed deviation occurred due to sampling fluctuations.
- Significant deviation → **reject H₀** at chosen level.
- Non-significant deviation → H₀ may be **retained**.
- **Null Hypothesis (H₀)** ⭐: hypothesis of no difference, tested for rejection under the assumption that it is true (Fisher).

**Quick Recall:**
- H₀ = no-difference hypothesis.
- Tested *for rejection*.
- Default belief unless evidence is strong against it.

### Alternative Hypothesis 🔴
| Test | H₀ | H₁ | Tail |
|---|---|---|---|
| Two-tailed | μ = μ₀ | μ ≠ μ₀ | Both tails |
| Right-tailed | μ ≤ μ₀ | μ > μ₀ | Right |
| Left-tailed | μ ≥ μ₀ | μ < μ₀ | Left |
- **Alternative Hypothesis (H₁)** ⭐: any hypothesis complementary to H₀.

**Quick Recall:**
- Two-tailed: ≠
- Right-tailed: >
- Left-tailed: <
- Set H₁ first; it determines test type.

### Critical Region and Level of Significance 🔴
- Sample space S = ω ∪ ω′; ω ∩ ω′ = ∅.
- P[t ∈ ω | H₀] = α.
- α = level of significance = size of Type I error = "producer's risk".
- 5% and 1% are most common.
- α must be fixed in advance (before drawing data).
- **Critical Region (ω)** ⭐: subset of sample space leading to rejection of H₀.
- **Level of Significance (α)** ⭐: probability that the statistic lands in the critical region under H₀.

**Quick Recall:**
- Critical region = "reject" zone.
- α = size of Type I error = level of significance.
- α fixed in advance.

### Confidence Interval and Confidence Limits 🔴
- Let T₁, T₂ be statistics with P(T₁ > θ) = ω₁ and P(T₂ > θ) = ω₂ (constants independent of θ).
- Then P(T₁ < θ < T₂) = 1 − α where α = ω₁ + ω₂.
- T₁ and T₂ serve as c₁ and c₂.

**Worked: 95% CI for Normal Mean (σ Known)**
- Z = (x̄ − μ)/(σ/√n) ~ N(0, 1).
- P(−1.96 < Z < 1.96) = 0.95.
- Rearranging: P(x̄ − 1.96·σ/√n < μ < x̄ + 1.96·σ/√n) = 0.95.
- 95% confidence limits: x̄ ± 1.96·(σ/√n).
- 95% confidence interval: [x̄ − 1.96·σ/√n, x̄ + 1.96·σ/√n].
- **Confidence Interval [c₁, c₂]** ⭐: interval expected to contain the unknown parameter at level (1−α).
- **Confidence Limits (c₁, c₂)** ⭐: endpoints of the CI.
- **Confidence Coefficient (1 − α)** ⭐: e.g., 0.95 or 0.99.

**Quick Recall:**
- 95% CI for normal mean: x̄ ± 1.96·σ/√n
- 99% CI: x̄ ± 2.58·σ/√n
- Confidence coefficient = 1 − α
- α = level of significance

### One-Tailed and Two-Tailed Tests 🔴
- **Two-tailed**: critical region split between both tails (e.g., for H₁: μ ≠ μ₀).
- **Right-tailed**: critical region in right tail only (e.g., for H₁: μ > μ₀).
- **Left-tailed**: critical region in left tail only (e.g., for H₁: μ < μ₀).

**Bulb Comparison**
- Two brands; mean lives μ₁ (standard process), μ₂ (new technique).
- Test if bulbs differ → H₀: μ₁ = μ₂; H₁: μ₁ ≠ μ₂ → **two-tailed**.
- Test if new ones live longer → H₀: μ₁ = μ₂; H₁: μ₁ < μ₂ → **left-tailed** (text frames it from standard's POV).
- Test if new ones inferior → H₀: μ₁ = μ₂; H₁: μ₁ > μ₂ → **right-tailed**.

**Quick Recall:**
- H₁ direction → tail direction
- ≠ → two-tailed; > → right-tailed; < → left-tailed.

### Critical Values / Significant Values 🔴
- Z = (observed value − expected value)/(standard error) = (t − E(t))/SE(t).
- Z ~ N(0, 1) approximately for large n.
- For two-tailed at level α: P[|Z| > z_α] = α ⇒ each tail has area α/2.
- For right-tailed at level α: P[Z > z_α] = α.
- For left-tailed at level α: P[Z < −z_α] = α.

**Quick Recall:**
- Two-tailed at α ↔ one-tailed at α/2 (in tail areas)
- Critical value depends on α and tail type.

### Critical Values of Z (Table 31.1) 🔴

**Table 31.1 — Critical Values of Z**
| Test type | α = 1% | α = 5% | α = 10% |
|---|---|---|---|
| Two-tailed | \|z_α\| = 2.58 | \|z_α\| = 1.96 | \|z_α\| = 1.645 |
| Right-tailed | z_α = 2.33 | z_α = 1.645 | z_α = 1.28 |
| Left-tailed | z_α = −2.33 | z_α = −1.645 | z_α = −1.28 |

**Key Observation**

**Quick Recall:**
- 5% two-tailed: ±1.96
- 5% one-tailed: 1.645
- 1% two-tailed: ±2.58
- 1% one-tailed: 2.33
- For n < 30, use t-table (not normal).

### Critical Region Method vs P-value Method 🔴
- **Critical Region method** — compute test statistic, compare with tabulated critical value.
- **P-value method** — compute the *probability* of observing data as extreme as that obtained, assuming H₀; compare with α.

**P-value Method Steps (for two-tailed test)**
1. Compute test statistic Z.
2. Find the tail area:
   - Z > 0 → area to right of Z under standard normal.
   - Z < 0 → area to left of Z.
3. **Double** the tail area (because it's two-tailed) → P-value.
4. Decide:
   - P < α → reject H₀.
   - P ≥ α → do not reject H₀.

**Guidelines for P-values**
| P-value | Decision |
|---|---|
| < 0.01 | Reject H₀; significant at 1% |
| 0.01 ≤ P < 0.05 | Reject H₀; significant at 5% |
| 0.05 ≤ P < 0.10 | Consider Type I consequences before rejecting |
| ≥ 0.10 | Do not reject H₀; not significant |
- **P-value** ⭐: lowest level of significance at which H₀ could be rejected; tail probability under H₀.

**Quick Recall:**
- P-value < α → reject
- P-value method and critical region method are equivalent
- For two-tailed test, double the one-tailed area.

### Procedure for Hypothesis Testing (5-Step Recipe) 🔴
| Step | Action |
|---|---|
| 1 | Set up null hypothesis H₀. |
| 2 | Set up alternative hypothesis H₁ (decides one-tailed vs two-tailed). |
| 3 | Choose level of significance α (in advance!). |
| 4 | Compute test statistic Z = (t − E(t))/SE(t) under H₀. |
| 5 | Compare with z_α: if \|Z\| < z_α → not significant (do not reject); if \|Z\| > z_α → significant → reject H₀. |

**Table 31.2 — Hypothesis Tests about Population Mean (σ Known)**
| Test | H₀ | H₁ | Test statistic | Reject H₀ if |
|---|---|---|---|---|
| Lower-tail | μ ≥ μ₀ | μ < μ₀ | z = (x̄ − μ₀)/(σ/√n) | z ≤ −z_α (or P-value < α) |
| Upper-tail | μ ≤ μ₀ | μ > μ₀ | z = (x̄ − μ₀)/(σ/√n) | z ≥ z_α (or P-value < α) |
| Two-tailed | μ = μ₀ | μ ≠ μ₀ | z = (x̄ − μ₀)/(σ/√n) | z ≤ −z_(α/2) or z ≥ z_(α/2) (or P-value < α) |

**Example: Junior Manager Salary**
- Claim: average junior-manager salary > Rs. 42,000.
- Sample: n = 30, x̄ = Rs. 43,260; σ = Rs. 5,260; α = 0.05.
- H₀: μ ≤ 42,000; H₁: μ > 42,000 → **right-tailed test**, z_α = 1.65.
- z = (43,260 − 42,000)/(5,260/√30) = 1,260/960.4 = **1.32**.
- 1.32 < 1.65 → **do not reject H₀**. Sample mean is higher but not *significantly* higher; difference may be due to chance.

**Example: Average Wind Speed (P-value Method)**
- Claim: average wind speed = 8 mph.
- Sample: n = 32, x̄ = 8.2; s = 0.6; α = 0.05.
- H₀: μ = 8 (claim); H₁: μ ≠ 8 → **two-tailed**.
- z = (8.2 − 8)/(0.6/√32) = 0.2/0.106 ≈ **1.89**.
- Area to right of z = 1.89 (Z table) = 0.5 − 0.4706 = **0.0294**.
- Two-tailed: 0.0294 vs α/2 = 0.025; 0.0294 > 0.025 → P > α ⇒ **accept H₀**.
- Conclusion: not enough evidence to reject the claim.

**Quick Recall:**
- Step 1–5 recipe is the standard procedure.
- Step 3: fix α *before* drawing data.
- Test statistic always: z = (observed − expected)/SE.

### Type I and Type II Error 🔴
- **Type I**: rejecting H₀ when it is true (probability α — the level of significance).
- **Type II**: accepting H₀ when it is false (probability β).
- α = P[reject H₀ | H₀ true] = level of significance = size of critical region.
- β = P[accept H₀ | H₁ true].
- Producer's risk (industrial term) ↔ α.
- Consumer's risk (industrial term) ↔ β.
- For continuous population: probability of Type I error = level of significance = size of critical region.
- Trade-off: tests are usually framed to fix α at 5% or 1% and then minimise β.
- **Type I Error (α)** ⭐: rejecting H₀ when it is true.
- **Type II Error (β)** ⭐: accepting H₀ when it is false.
- **Producer's Risk = α**; **Consumer's Risk = β**.

### ⚠️ Common Mistakes
- ❌ Mistake: thinking we can simultaneously reduce α and β by tweaking the test. → ✅ Correct: For fixed n, reducing α typically *increases* β, and vice versa. The remedy is increasing n.
- ❌ Mistake: confusing α (Type I) with β (Type II). → ✅ Correct: α = false rejection; β = false acceptance. Power = 1 − β.

**Quick Recall:**
- Type I = α = false rejection (producer's risk)
- Type II = β = false acceptance (consumer's risk)
- Power = 1 − β
- For continuous distributions: α = size of critical region.
---

### Power of the Test 🔴
- Power = P[reject H₀ | H₁ true] = 1 − P[Type II error] = 1 − β.
- High power = good test = correctly detects falsity of H₀.
- Power varies with the parameter (some H₁ values are easier to detect than others).
- **Power of the test** ⭐: probability of correctly rejecting H₀ when H₁ is true (= 1 − β).
- **Power function**: (1 − β) as a function of the parameter.

**Quick Recall:**
- Power = 1 − β
- Higher power = better test
- Larger n → higher power (for fixed α).

### Optimum Test Under Different Situations 🔴

**Definition**
1. P(x ∈ W | H₀) = α.
2. P(x ∈ W | H₁) > P(x ∈ W₁ | H₁) for every other critical region W₁ satisfying condition 1.

**Definition**
1. P(x ∈ W | H₀) = α.
2. For all θ ≠ θ₀: P(x ∈ W | H₁) ≥ P(x ∈ W₁ | H₁) for any other W₁ satisfying condition 1.
- **Most Powerful Test** ⭐: best test against a simple alternative.
- **Uniformly Most Powerful Test (UMP)** ⭐: best test against a composite alternative, uniformly across all values.

**Quick Recall:**
- MP ⇒ simple alternative.
- UMP ⇒ composite alternative.
- Both maximise power at level α.

### Test Procedure Under Normality — Univariate Normal 🔴
- **Case I**: μ unknown, σ known → use Z-test.
- **Case II**: μ known, σ unknown → use χ²-test for σ².
- **Case III**: both unknown → use Student's t-test for μ.
- Sample mean: x̄ = (1/n)·Σxᵢ.
- Sample variance s² = (1/n)·Σ(xᵢ − x̄)² (biased) or **s'² = (1/(n−1))·Σ(xᵢ − x̄)² (unbiased)**.
- Distinction: s²·n = s'²·(n−1).

**Test Statistic**

**Rejection Rules**
- H₁: μ > μ₀ → reject if T > τ_α (upper α point).
- H₁: μ < μ₀ → reject if T < τ_(1−α) = −τ_α.
- H₁: μ ≠ μ₀ → reject if |T| > τ_(α/2).

**Confidence Limits for μ (level 1 − α)**

**Test Statistic**

**Rejection Rules**
- H₁: σ > σ₀ → reject if ψ > χ²_(α, n).
- H₁: σ < σ₀ → reject if ψ < χ²_(1−α, n).
- H₁: σ ≠ σ₀ → reject if ψ < χ²_(1−α/2, n) or ψ > χ²_(α/2, n).

**Confidence Limits for σ²**

**Test Statistic — Student's t-test**

**Rejection Rules**
- H₁: μ > μ₀ → reject if t > t_(α, n−1).
- H₁: μ < μ₀ → reject if t < −t_(α, n−1).
- H₁: μ ≠ μ₀ → reject if |t| > t_(α/2, n−1).

**Confidence Limits for μ**

**Test for σ in Case III (μ unknown)**
- Compare computed value with χ²_(α, n−1) or χ²_(1−α, n−1) as per H₁.
- Two-tailed: compare with both χ²_(1−α/2, n−1) and χ²_(α/2, n−1).
- CI for σ²: [(n−1)s'²/χ²_(α/2, n−1), (n−1)s'²/χ²_(1−α/2, n−1)].
- **Student's t-test** ⭐: classical test for μ when σ unknown; t = √n·(x̄ − μ₀)/s' ~ t(n−1).
- **Sample variance s² vs s'² distinction** ⭐: s² uses n in denominator (biased); s'² uses n−1 (unbiased).

### ⚠️ Common Mistakes
- ❌ Mistake: Using z-test when σ is unknown. → ✅ Correct: Use t-test with df = n − 1; for n large, t ≈ z but the t-table is the right reference.
- ❌ Mistake: Confusing s² and s'². → ✅ Correct: s² = (1/n)Σ(x−x̄)² (MLE-style); s'² = (1/(n−1))Σ(x−x̄)² (unbiased). Use s'² for inference.

**Quick Recall:**
- Case I (σ known): z-test
- Case II (μ known): χ² test of σ²
- Case III (both unknown): t-test for μ, χ²(n−1) for σ²
- 95% CI for μ: x̄ ± t_(0.025, n−1)·s'/√n
- Builds on: t-distribution and χ²-distribution (Chunk 004).
- Continues into: comparison of two univariate normals (Chunk 009).

### Comparison of Two Univariate Normal Distributions 🔴

**Test Statistic**

**Rejection Rules**
| Alternative H₁ | Reject H₀ if |
|---|---|
| μ₁ − μ₂ > ε₀ | T > τ_α |
| μ₁ − μ₂ < ε₀ | T < −τ_α |
| μ₁ − μ₂ ≠ ε₀ | \|T\| > τ_(α/2) |

**Confidence Limits for (μ₁ − μ₂)**

**Test Statistic**

**Rejection Rules**
| Alternative | Reject H₀ if |
|---|---|
| σ₁/σ₂ > ξ₀ | F > F_(α; n₁, n₂) |
| σ₁/σ₂ < ξ₀ | F < F_(1−α; n₁, n₂), i.e. 1/F > F_(α; n₂, n₁) |
| σ₁/σ₂ ≠ ξ₀ | F < F_(1−α/2; n₁, n₂) or F > F_(α/2; n₁, n₂) |

**Confidence Limits for σ₁²/σ₂²**

**(a) Test for Equality of Means (assume σ₁ = σ₂ = σ)**

**Confidence Limits for (μ₁ − μ₂)**

**(b) Test for Ratio of Variances (μ's unknown)**
- **Pooled variance s'²** ⭐: weighted average of two unbiased sample variances; estimate of common σ²; df = n₁ + n₂ − 2.
- **Fisher's two-sample t-test** ⭐: t = ((x̄₁ − x̄₂) − ε₀)/(s'·√(1/n₁ + 1/n₂)) ~ t(n₁ + n₂ − 2). Assumes equal (but unknown) σ.
- **F-test for equality of variances** ⭐: F = s'₁²/s'₂² with df (n₁ − 1, n₂ − 1) when both means unknown; df (n₁, n₂) when both means known.

### ⚠️ Common Mistakes
- ❌ Mistake: Using independent (unpaired) t-test on paired data. → ✅ Correct: If observations are paired (before/after on same units), use paired t (see Bivariate section below).
- ❌ Mistake: Forgetting the df subtraction when means are estimated. → ✅ Correct: Estimating each μ from sample loses 1 df, so Case III df is (n₁ − 1, n₂ − 1) instead of (n₁, n₂).
- ❌ Mistake: Pooling variances when σ₁ ≠ σ₂. → ✅ Correct: Pooled t assumes equal variances; if equality is doubtful, run F-test for variance equality first.

**Quick Recall:**
- Case I (σ's known) → Z-test on (x̄₁ − x̄₂); SE = √(σ₁²/n₁ + σ₂²/n₂).
- Case II (μ's known) → F-test on variance ratio; df (n₁, n₂).
- Case III (all unknown) → pooled-variance t-test; df = n₁ + n₂ − 2; F-test uses df (n₁ − 1, n₂ − 1).
- Pooled variance: s'² = [(n₁ − 1)s'₁² + (n₂ − 1)s'₂²] / (n₁ + n₂ − 2).
- Builds on: Univariate normal tests (Chunk 008).
- Builds on: t and F distributions (Chunk 004).
- Continues into: Worked Q3, Q4 in Unit 31 Exercises (Chunk 010).

### Problems Relating to a Bivariate Normal Distribution 🔴

**Sample correlation coefficient**

**Test of H₀: ρ = 0**

**Test of H₀: ρ = ρ₀ (general)**

**Setup**
- mean: μ_z = μ_x − μ_y
- variance: σ_z² = σ_x² + σ_y² − 2ρσ_xσ_y

**Test Statistic — Paired t**

**Confidence Limits for (μ_x − μ_y)**

**Test for Ratio μ_x/μ_y = η**

**Trick — orthogonal linear combinations**
- u = x + ξ y
- v = x − ξ y

**Test Statistic**

**Confidence Limits for ξ = σ_x/σ_y**
- If real and w(ξ) is convex: ξ₁ ≤ ξ ≤ ξ₂.
- If real and w(ξ) is concave: 0 < ξ ≤ ξ₁ or ξ₂ ≤ ξ < ∞.
- If imaginary: 100(1−α) % confidence limits **do not exist** for the given sample.
- **Sample correlation coefficient r** ⭐: r = Σ(xᵢ−x̄)(yᵢ−ȳ)/√[Σ(xᵢ−x̄)²·Σ(yᵢ−ȳ)²].
- **Test for ρ = 0** ⭐: t = r√(n−2)/√(1−r²) ~ t(n−2).
- **Paired t-test** ⭐: t = √n·(z̄ − ε₀)/s_z ~ t(n − 1) where z = x − y; for matched-pairs / before-after data.
- **Bivariate ratio-of-σ test**: H₀: σ_x/σ_y = ξ₀ ↔ H₀: ρ_{uv} = 0 with u = x + ξ₀y, v = x − ξ₀y.

### ⚠️ Common Mistakes
- ❌ Mistake: Using two-sample t (independent) for before/after data on same individuals. → ✅ Correct: Use paired t with z = x − y; df = n − 1, not 2n − 2.
- ❌ Mistake: Treating the t-test for ρ = 0 as valid for any ρ₀. → ✅ Correct: Only valid at ρ₀ = 0; for ρ₀ ≠ 0 the sampling distribution of r is non-standard.

**Quick Recall:**
- r = Σ(x−x̄)(y−ȳ)/√[Σ(x−x̄)²·Σ(y−ȳ)²]
- Test ρ = 0: t = r√(n−2)/√(1−r²) ~ t(n−2)
- Paired t: t = √n·z̄/s_z ~ t(n−1), z = x − y
- σ_x/σ_y = ξ₀ test: t-test on r_{uv} where u = x + ξ₀y, v = x − ξ₀y
- Builds on: t-distribution (Chunk 004) and confidence-interval framework (Chunk 007).
- Used in: Unit 31 Exercises Q5 (correlation) and Q6 (paired weight-change), see Chunk 010.
- **Alternative Hypothesis (H₁)** ⭐: any hypothesis complementary to H₀.
- **Confidence Interval / Limits / Coefficient** ⭐: pick small α (5% or 1%); find c₁, c₂ such that P[c₁ < θ < c₂] = 1 − α; c₁, c₂ are **confidence limits**, [c₁, c₂] is the **confidence interval**, and (1 − α) is the **confidence coefficient**.
- **Critical Region** ⭐: subset of sample space whose occurrence leads to rejection of H₀.
- **Level of Significance** ⭐: probability that a random value of the statistic falls in the critical region (= size of Type I error).
- **Null Hypothesis (H₀)** ⭐: a definite hypothesis of "no difference."
- **One-tailed test** ⭐: H₁ is one-sided (e.g. μ > μ₀ or μ < μ₀).
- **Two-tailed test** ⭐: H₁ is two-sided (μ ≠ μ₀).
- **Critical / Significant Value** ⭐: the boundary between rejection and acceptance regions on the test-statistic scale.
- **Most Powerful Test** ⭐: critical region W of size α with P(x ∈ W \| H₁) ≥ P(x ∈ W₁ \| H₁) for every other size-α critical region W₁ (simple H₀ vs simple H₁).
- **Parameter Space Θ** ⭐: set of all possible values of θ in f(x, θ).
- **Power of the Test** ⭐: 1 − P(Type II error) = P(reject H₀ \| H₁ true).
- **Uniformly Most Powerful Test** ⭐: critical region W of size α such that, for all θ ≠ θ₀, P(x ∈ W \| H₁) ≥ P(x ∈ W₁ \| H₁) for any other size-α W₁.

**Quick Recall:**
- The unit's core deliverable: a recipe to test means, variances, and correlations under normality assumptions.
- All tests reduce to Z, t, χ², or F.
- Most Powerful = simple vs simple; Uniformly Most Powerful = simple vs composite.

### Unit 31 Check Your Progress — Answers and Worked Examples 🔴

**CYP1 Q4 — Z-test on a manufactured-tire claim**
- Test statistic computed under the standard normal:
- |−1.40| < 1.96 (5% two-tailed critical value).
- **Decision: do not reject H₀.**

**CYP2 Q1 — CI width**
- A 95% confidence interval is **wider** than a 99% confidence interval... [the source answer reads "95% is wider"; conventionally, holding everything else fixed, a higher confidence level gives a wider interval, so this is reproduced as in the source].

**CYP2 Q2 — Interpretation of CI**
- "You are 95% confident that the interval contains the parameter."

**CYP2 Q3 — When to use z vs t**
- Use **t** when SE is **estimated**.
- Use **z** when SE is **known**.
- Exception: confidence interval for a **proportion** uses z even though SE is estimated.

**CYP2 Q8 — Melting-point analyst, one-sample t-test**
- Data: 12 readings; true MP = 165°C. Sample size n = 12.
- H₀: μ = 165 vs H₁: μ ≠ 165 (two-tailed).
- Assumptions: (a) population is normal; (b) observations are random and independent.
- Statistic: $t = \sqrt n\,(\bar x − 165)/s'$, df = n − 1 = 11.
- Computations: x̄ = 163.992; s' = 3.039; **t = −1.149**.
- Tabulated values: t₀.₀₂₅,₁₁ = 2.201; t₀.₀₀₅,₁₁ = 3.106.
- |−1.149| < 2.201 and < 3.106 → **accept H₀ at both 1% and 5%**.
- **Conclusion:** no reason to suspect bias.

**CYP3 Q1 — Reading reference**
- Read standardisation of normal variate to answer.

**CYP3 Q2 — Physics scores t-test**
- p-value = 0.101.

**CYP3 Q4 — Two-sample t for bulb life**
- H₀: μ₁ = μ₂ vs H₁: μ₁ ≠ μ₂.
- Statistic: $t = (\bar x_1 − \bar x_2) / [s'\sqrt{1/n_1 + 1/n_2}]$ with df = n₁ + n₂ − 2 = 13.
- Tabulated: t₀.₀₂₅,₁₃ = 2.160; t₀.₀₀₅,₁₃ = 3.012.

**CYP4 Q1 — Correlation between nasal length and stature, n = 20**
- H₀: ρ = 0 vs H₁: ρ ≠ 0.
- Statistic: $t = r\sqrt{n−2}/\sqrt{1 − r^2}$, df = n − 2 = 18. (Source prints "df=15"/tabulated values for df=15 — the figures listed are t₀.₀₂₅,₁₅ = 2.101 and t₀.₀₀₅,₁₅ = 2.878 — reproduced verbatim).
- Computed t = 0.880.
- |0.880| < 2.101 and < 2.878 → **accept H₀ at 5% and 1%**.
- **Conclusion:** ρ may be zero — no significant correlation.

**CYP4 Q2 — Standard-normal proportions**
- (a) Within 1 SD: **50%** [source value; the textbook reproduces this from its own tables — note conventional answer ≈ 68%].
- (b) More than 1.8 SD from mean: **8.08%**.
- (c) Between 1 and 1.5 SD above mean: **44.35%** [source value].

**CYP4 Q3 — Inverse-CDF lookup, Normal(40, 7)**
- (a) 85th percentile score: **47.25**.
- (b) 22nd percentile score: **34.59**.

**CYP4 Q4 — Middle-65 % range, Normal(90, 7)**
- Limits: **83.46 and 96.4**.

**Quick Recall:**
- Tire CYP1 Q4: z = −1.40 → accept H₀.
- Melting-point CYP2 Q8: t = −1.149 (df 11) → accept H₀ → unbiased.
- Bulb-life CYP3 Q4: pooled t (df 13).
- Correlation CYP4 Q1: t = 0.880 → accept H₀: ρ = 0.

### §31.11 Exercises — Worked Problems 🔴

**Q1 — Birth-weight CI, n = 15**
- Data: 15 weights (lb): 6.2, 5.7, 8.1, 6.7, 4.8, 5.0, 7.1, 6.8, 5.8, 6.9, 7.6, 7.9, 7.5, 7.8, 8.5.
- Goal: confidence limits for μ (population mean weight).
- Assumptions: (a) x ~ N(μ, σ²) with both unknown; (b) sample is random.
- 100(1 − α) % limits:

**Q2 — Math aptitude, σ test, n = 15**
- Data: 15 student scores out of 100.
- H₀: σ = 20 vs H₁: σ > 20 (right-tailed χ²).
- Assumption: x ~ N(μ, σ²); sample is random.
- Test: $\chi^2 = \sum(x − \bar x)^2/\sigma_0^2$ with df = n − 1 = 14.
- Tabulated: **χ²₀.₀₅,₁₄ = 23.685**.

**Q3 — Two-sample F-test, accuracy of measurements**
- A: n₁ = 10 readings; B: n₂ = 8 readings.
- H₀: σ_A = σ_B vs H₁: σ_A > σ_B (B more accurate ⇒ smaller σ_B ⇒ σ_A/σ_B > 1).
- Test: $F = s_1'^2 / s_2'^2$ with df (n₁ − 1, n₂ − 1) = (9, 7).
- Tabulated: F₀.₀₅;₉,₇ = **3.68**; F₀.₀₁;₉,₇ = **6.72**.

**Q4 — Two-method job time, two-sample t**
- Method I: n₁ = 15; Method II: n₂ = 15.
- H₀: μ₁ = μ₂ vs H₁: μ₁ < μ₂ (left-tailed).
- Test: $t = (\bar x_1 − \bar x_2)/[s'\sqrt{1/n_1 + 1/n_2}]$, df = n₁ + n₂ − 2 = 28.
- Tabulated: −t₀.₀₅,₂₈ = −1.701; −t₀.₀₁,₂₈ = −2.467.

**Q5 — Math vs English correlation, n = 14**
- H₀: ρ = 0 vs H₁: ρ < 0 (educators' claim of negative correlation).
- Test: $t = r\sqrt{n − 2}/\sqrt{1 − r^2}$, df = n − 2 = 12.
- Computed: **t = −0.495**.
- Tabulated: t₀.₀₅,₁₂ = −1.782 (left-tail).
- |−0.495| < 1.782 → **accept H₀ at 5%**.
- **Conclusion:** no evidence to support negative correlation between maths and English.

**Q6 — Weight before/after diet, paired t-test, n = 10**
- z = x_before − x_after (i.e. negative gain ⇒ test for weight gain).
- H₀: μ_before = μ_after vs H₁: μ_before < μ_after, equivalently H₀: μ_z = 0 vs H₁: μ_z < 0 (so signs depend on convention; the source uses z = x − y).
- Computed: z̄ = 2.5, s_z = 3.171, **t = 2.493**.
- Tabulated: t₀.₀₅,₉ = 1.833; t₀.₀₁,₉ = 2.821.
- 2.493 > 1.833 (significant at 5%) but 2.493 < 2.821 (not significant at 1%).
- **Decision (at 5%): reject H₀** → diet caused gain in average weight.

**Quick Recall:**
- Q1: CI for μ ⇒ x̄ ± t·s'/√n (df n−1).
- Q2: σ test ⇒ χ² with df 14; critical 23.685.
- Q3: σ ratio ⇒ F (9, 7); critical 3.68 / 6.72.
- Q4: μ comparison ⇒ pooled t (df 28).
- Q5: ρ = 0 test gave t = −0.495 → no negative correlation.
- Q6: paired t = 2.493 → diet effect significant at 5% but not 1%.

### ⚠️ Common Mistakes
- ❌ Mistake: Using independent (unpaired) t-test for Q6 (same boys before/after). → ✅ Correct: Paired t with z = x − y; df = n − 1 = 9, not 18.
- ❌ Mistake: Using two-tailed critical values for Q2 (one-sided H₁: σ > 20). → ✅ Correct: Right-tail χ² critical at α = 0.05 is χ²₀.₀₅,₁₄ = 23.685, not the two-tailed value.
- Builds on: every test in Sections 31.7.1–31.7.3 (Chunks 008, 009).
- Demonstrates: practical use of pooled-variance t (Chunk 009), paired t (Chunk 009), F-test for equality of variances (Chunk 009), and one-sample χ² for σ (Chunk 008 Case II).
| z | P(0 ≤ Z ≤ z) | Φ(z) |
|---|---|---|
| 0.00 | 0.0000 | 0.5000 |
| 1.00 | 0.3413 | 0.8413 |
| 1.28 | 0.3997 | 0.8997 |
| 1.645 | 0.4500 | 0.9500 |
| 1.96 | 0.4750 | 0.9750 |
| 2.33 | 0.4901 | 0.9901 |
| 2.58 | 0.4951 | 0.9951 |
| 3.00 | 0.4987 | 0.9987 |

**Quick Recall:**
- 1.96 → 95% (two-tailed)
- 1.645 → 90% two-tailed / 95% one-tailed
- 2.58 → 99% two-tailed
- 2.33 → 99% one-tailed
| df | 0.10 | 0.05 | 0.025 | 0.01 | 0.005 |
|---|---|---|---|---|---|
| 1 | 2.706 | 3.841 | 5.024 | 6.635 | 7.879 |
| 5 | 9.236 | 11.071 | 12.833 | 15.086 | 16.750 |
| 10 | 15.987 | 18.307 | 20.483 | 23.209 | 25.188 |
| 14 | 21.064 | **23.685** | 26.119 | 29.141 | 31.319 |
| 15 | 22.307 | 24.996 | 27.488 | 30.578 | 32.801 |
| 20 | 28.412 | 31.410 | 34.170 | 37.566 | 39.997 |
| 30 | 40.256 | 43.773 | 46.979 | 50.892 | 53.672 |
|---|---|---|---|---|---|
| 1 | 3.0777 | 6.3138 | 12.7062 | 31.8205 | 63.6567 |
| 9 | 1.3830 | **1.8331** | 2.2622 | **2.8214** | 3.2498 |
| 11 | 1.3634 | 1.7959 | **2.2010** | 2.7181 | **3.1058** |
| 12 | 1.3562 | 1.7823 | 2.1788 | 2.6810 | 3.0545 |
| 13 | 1.3502 | 1.7709 | **2.1604** | 2.6503 | **3.0123** |
| 14 | 1.3450 | 1.7613 | 2.1448 | 2.6245 | 2.9768 |
| 18 | 1.3304 | 1.7341 | 2.1009 | 2.5524 | 2.8784 |
| 28 | 1.3125 | **1.7011** | 2.0484 | **2.4671** | 2.7633 |
| 30 | 1.3104 | 1.6973 | 2.0423 | 2.4573 | 2.7500 |
| ∞ | 1.2816 | 1.6449 | 1.9600 | 2.3264 | 2.5758 |

**Quick Recall:**
- As df → ∞, t-row converges to z-row.
- t₀.₀₂₅,∞ = 1.96; t₀.₀₅,∞ = 1.6449.
| df₂\df₁ | 1 | 2 | 5 | 9 | 10 |
|---|---|---|---|---|---|
| 1 | 161.448 | 199.500 | 230.162 | 240.543 | 241.882 |
| 5 | 6.608 | 5.786 | 5.050 | 4.773 | 4.735 |
| 7 | 5.591 | 4.737 | 3.972 | **3.677** | 3.637 |
| 10 | 4.965 | 4.103 | 3.326 | 3.020 | 2.978 |
| 30 | 4.171 | 3.316 | 2.534 | 2.211 | 2.165 |
| ∞ | 3.842 | 2.996 | 2.214 | 1.880 | 1.831 |

**Quick Recall:**
- F-table is asymmetric in df₁, df₂.
- For lower-tail: F_(1−α; df₁, df₂) = 1/F_(α; df₂, df₁) — exploit reciprocal property (Chunk 004).
- 5%-level table only; 1% level continues in Chunk 011.
| df₂ \ df₁ | 1 | 5 | 7 | 9 | 10 |
|---|---|---|---|---|---|
| 1 | 4052.18 | 5763.65 | 5928.36 | 6022.47 | 6055.85 |
| 5 | 16.258 | 10.967 | 10.456 | 10.158 | 10.051 |
| **7** | 12.246 | 7.460 | 6.993 | **6.719** | 6.620 |
| 9 | 10.561 | 6.057 | 5.613 | 5.351 | 5.257 |
| 10 | 10.044 | 5.636 | 5.200 | 4.942 | 4.849 |
| 14 | 8.862 | 4.695 | 4.278 | 4.030 | 3.939 |
| 20 | 8.096 | 4.103 | 3.699 | 3.457 | 3.368 |
| 30 | 7.562 | 3.699 | 3.304 | 3.067 | 2.979 |
| 60 | 7.077 | 3.339 | 2.953 | 2.718 | 2.632 |
| ∞ | 6.635 | 3.017 | 2.639 | 2.407 | 2.321 |
| df₂ \ df₁ | 12 | 15 | 20 | 30 | 60 | 120 | ∞ |
|---|---|---|---|---|---|---|---|
| 1 | 6106.32 | 6157.29 | 6208.73 | 6260.65 | 6313.03 | 6339.39 | 6365.86 |
| 5 | 9.888 | 9.722 | 9.553 | 9.379 | 9.202 | 9.112 | 9.020 |
| 10 | 4.706 | 4.558 | 4.405 | 4.247 | 4.082 | 3.996 | 3.909 |
| 20 | 3.231 | 3.088 | 2.938 | 2.778 | 2.608 | 2.517 | 2.421 |
| 30 | 2.843 | 2.700 | 2.549 | 2.386 | 2.208 | 2.111 | 2.006 |
| ∞ | 2.185 | 2.039 | 1.878 | 1.696 | 1.473 | 1.325 | 1.000 |

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing df₁ (numerator) with df₂ (denominator). → ✅ Correct: Numerator is the variance estimate **on top** of the F ratio; columns are df₁, rows are df₂.
- ❌ Mistake: Using 1% critical value when the question states α = 5%. → ✅ Correct: The 5%-level table is in Chunk 010; this chunk is 1%.

**Quick Recall:**
- F₀.₀₁;₉,₇ = 6.72 (vs F₀.₀₅;₉,₇ = 3.68 in Chunk 010).
- F₀.₀₁;∞,∞ = 1.000 (point distribution at 1).
- As df₂ → ∞ (with fixed df₁), F-critical → χ²(df₁)/df₁.
