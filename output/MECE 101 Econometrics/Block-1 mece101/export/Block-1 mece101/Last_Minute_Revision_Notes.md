# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Block | Title | Units | Key Topics |
|-------|-------|-------|-----------|
| Block 1 | Introduction | 1–3 | What econometrics is, Statistical foundations, Matrix algebra |
| Block 2 | Classical Regression Model | 4–7 | Two-variable OLS, Residuals, Multiple regression |
| Block 3 | Violations of Basic Assumptions | 8–13 | Specification, Autocorrelation, Multicollinearity, Heteroscedasticity, Errors-in-variables, Endogeneity |
| Block 4 | Extensions of Regression Models | 14–16 | Dummy variables, Qualitative dependent variables (Logit/Probit), Simultaneous equations |

**Quick Recall:**
- 4 Blocks → 16 Units total
- Block 1: Foundations; Block 2: OLS; Block 3: Violations; Block 4: Extensions
- Advanced follow-up: MECE 102 (time series, panel data)
| Dimension | Theoretical Econometrics | Applied Econometrics |
|-----------|--------------------------|----------------------|
| Focus | Developing new statistical methods | Using existing methods on real-world data |
| Output | New estimators, test statistics | Empirical findings, policy conclusions |
| Example | Deriving properties of OLS | Estimating a consumption function |
- **Econometrics**: The application of mathematical statistics and probability theory to economic data to test hypotheses and estimate economic relationships. ⭐ (exam-important)

**Quick Recall:**
- Econometrics = Economics + Mathematics + Statistics applied to data
- Theoretical = develops new tools; Applied = uses those tools on real data
- After MECE 101: can do model selection, estimation, and diagnostics

### Econometric Models 🔴

**Econometric Model vs Economic Model**
| Dimension | Economic Model | Econometric Model |
|-----------|---------------|-------------------|
| Form | Theoretical, logical | Mathematical + Statistical |
| Includes error? | No | Yes — stochastic error (u) |
| Testable? | Sometimes | Yes — uses real data |
| Purpose | Explain behaviour conceptually | Estimate, test, predict |

**Population Regression Function (PRF) vs Sample Regression Function (SRF)**
- **Econometric Model**: A statistical model, expressed in mathematical form, specifying relationships between economic quantities; a simplification of reality estimated using real data. ⭐ (exam-important)
- **Population Regression Function (PRF)**: The theoretical relationship between Y and X in the entire population; represents conditional expectation E(Y|X). ⭐ (exam-important)
- **Sample Regression Function (SRF)**: The estimated relationship derived from sample data; used to draw inferences about the PRF.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking an econometric model must capture all determinants of Y → ✅ Correct: It only includes the *important* variables; the rest are absorbed by u

**Quick Recall:**
- Econometric model = Economic model + Stochastic error term
- PRF is unknown (population truth); SRF is what we estimate from sample
- Statistical significance matters because we work with one sample, not the whole population
- Builds on: Scope of Econometrics (Chunk 001)
- Is prerequisite for: Stochastic Specification (below), Functional Forms (below)

### Important Steps in an Econometric Study 🔴

**Six Steps in Econometric Research**
1. **State the hypothesis**: An assertion about an economic relationship, drawn from theory or logic. Written as H₀ and H₁.
2. **Formulate the mathematical model**: Transform the hypothesis into one or more equations (the economic model).
3. **Collect relevant data**: Primary or secondary sources; entered into a worksheet (e.g., Excel). Data must cover all variables in the model.
4. **Estimate parameters**: Select an appropriate estimation method (Least Squares, Maximum Likelihood, or Method of Moments) and compute parameter values.
5. **Test the hypothesis**: Use test statistics (e.g., t-ratio) or p-values to assess statistical significance.
6. **Interpret and draw inferences**: Explain results in economic terms; draw policy conclusions.
- **Hypothesis**: An assertion or claim about a property of a population; may express a relationship between variables. ⭐ (exam-important)
- **Null Hypothesis (H₀)**: The hypothesis whose validity is tested; asserts no relationship between variables (e.g., H₀: β₁ = 0).
- **Alternative Hypothesis (H₁)**: Tested indirectly; its acceptance/rejection is determined by what happens to H₀.

### ⚠️ Common Mistakes
- ❌ Mistake: "Accepting" a null hypothesis → ✅ Correct: We either "reject" or "do not reject" H₀; we never truly "accept" it

**Quick Recall:**
- 6 Steps: Hypothesis → Model → Data → Estimation → Testing → Interpretation
- Steps 1–2 are theoretical; Steps 3–6 are empirical
- The process is iterative — unsatisfactory results trigger revision
- Builds on: Econometric Models (above)
- Connects to: Estimation Methods (Chunk 004)

### Specification — Deterministic vs Stochastic Relationship 🔴

**Deterministic Relationship**

**Stochastic Relationship**

**Role of the Error Variable (u)**
1. **Omitted explanatory variables** — variables that affect Y but are not included in the model
2. **Wrong functional form** — e.g., fitting a linear model when the true relationship is non-linear
3. **Selection of wrong sample** — sampling error or measurement error in the data

**Classical Assumptions on u (Equations 1.3–1.7)**
- E(u) = 0 — zero mean
- Var(u) = σ² — constant variance (homoscedasticity)
- Cov(uᵢ, uⱼ) = 0 for i ≠ j — no autocorrelation
- u is independent of X
- u ~ N(0, σ²) — normally distributed (for inference)
- **Deterministic Component**: The systematic part of the regression equation; E(Y|X) = βₒ + β₁X. ⭐ (exam-important)
- **Stochastic Component / Error Variable (u)**: The random disturbance term that makes the regression relationship probabilistic; captures omitted variables, wrong functional form, and sampling error. ⭐ (exam-important)
- **Classical Regression Model**: A linear regression model where the error variable fulfils all classical assumptions (zero mean, homoscedasticity, no autocorrelation, normality). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking u is just "random noise" → ✅ Correct: u has three specific sources — omitted variables, specification error, and sampling error
- ❌ Mistake: Confusing stochastic model with a bad model → ✅ Correct: Stochasticity is inherent in all economic data

**Quick Recall:**
- Deterministic: Y = f(X) exactly; Stochastic: Y = f(X) + u
- Error u has 3 sources: omitted vars, wrong functional form, sampling error
- OLS applies when u fulfils classical assumptions (zero mean, constant variance, no correlation)
- Builds on: Econometric Models (above)
- Is prerequisite for: Block 2 (OLS estimation), Block 3 (violations of assumptions)

### Data Generation Process (DGP) 🔴

**General-to-Specific vs Specific-to-General**
| Approach | Direction | Description |
|----------|-----------|-------------|
| General-to-Specific | Many → fewer variables | Start with a large model; remove irrelevant variables. Preferred in practice. |
| Specific-to-General | Few → more variables | Start with a simple model; add variables based on logic. Less preferred. |

**Four Steps in DGP-Based Model Building**
1. Guess the DGP (choose variables, functional form)
2. Assume the associated probability theory (choose probability distribution for u)
3. Use that theory for empirical evidence (estimate and test)
4. Revise the model if results don't match data → repeat
- **Data Generation Process (DGP)**: The true real-world mechanism that generates the observed data; unknown to the researcher; represents reality. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking a good-fitting model = we understand the DGP → ✅ Correct: A fitting model only means "our model was adequate for this case" — it does NOT reveal the true DGP

**Quick Recall:**
- DGP = hidden truth; we approximate it with econometric models
- General-to-specific: preferred approach (start big, trim down)
- Good fit ≠ true DGP revealed; model building is iterative
- Builds on: Stochastic specification (above)
- Connects to: Karl Popper's falsificationism (referenced: MEC 109)

### Functional Forms — Classical, Semi-Log, Log-Linear 🔴

**Classical Linear Regression Model**

**Semi-Log Model**

**Log-Linear (Double-Log) Model**
| Model | Form | β₁ Interpretation |
|-------|------|-------------------|
| Linear | Y = β₀ + β₁X + u | Absolute change: ΔY = β₁ for ΔX = 1 |
| Semi-Log | lnY = β₀ + β₁X + u | Percentage change in Y per unit change in X (growth rate) |
| Log-Linear (Double-Log) | lnY = β₀ + β₁lnX + u | Elasticity: % change in Y per 1% change in X |
- **Linear Regression Model**: A model linear in both parameters (β) and variables (X, Y); can be estimated directly by OLS. ⭐ (exam-important)
- **Intrinsically Linear Model**: A non-linear model that can be transformed into a linear form (e.g., by taking logarithms), enabling OLS estimation.
- **Semi-Log Model**: A regression model where only one variable is in logarithmic form (typically ln Y); the slope coefficient measures the **proportional/percentage rate of change** in Y per unit change in X. ⭐ (exam-important)
- **Log-Linear (Double-Log) Model**: A regression model where both variables are in logarithmic form; the slope coefficient measures the **elasticity** of Y with respect to X. ⭐ (exam-important)
- **Elasticity**: The percentage change in Y for a 1 percent change in X; given by β₁ in the log-linear model. ⭐ (exam-important)
- Linear: Y = 5 + 2X → For every 1 unit increase in X, Y increases by **2 units** (absolute).
- Semi-Log: lnY = 5 + 0.03X → For every 1 unit increase in X (e.g., 1 year), Y increases by **3% per year** (growth rate).
- Log-Linear: lnY = 5 + 0.8lnX → For every **1% increase in X**, Y increases by **0.8%** (elasticity = 0.8, inelastic).

### ⚠️ Common Mistakes
- ❌ Mistake: Interpreting semi-log β₁ as an absolute change → ✅ Correct: It is a proportional (percentage) change
- ❌ Mistake: Confusing semi-log with log-linear — one takes log of Y only, the other takes log of both Y and X → ✅ Correct: Semi-log = lnY; Log-linear = lnY and lnX
- ❌ Mistake: Thinking we can apply OLS to Y_t = e^{β₀+β₁X} directly → ✅ Correct: Must transform first (take logs) to make it intrinsically linear
- Semi-log and log-linear require Y > 0 and X > 0 (logarithms of negative numbers undefined).
- The interpretation of β₁ in semi-log model gives an approximation of the growth rate (exact formula uses e^{β₁} - 1).

**Quick Recall:**
- Linear: ΔY = β₁ (absolute) | Semi-Log: %ΔY = β₁ (growth rate) | Log-Linear: %ΔY/%ΔX = β₁ (elasticity)
- CYP Q3 slope interpretations: (i) Absolute ΔY (ii) % ΔY per unit ΔX (iii) Elasticity β₁%
- Intrinsically linear = non-linear model that logs can linearise
- Builds on: Classical Regression Model (above)
- Connects to: Block 2 Units 4–7 (OLS estimation of these models)
- Contrasts with: Non-linear models not in scope of MECE 101
1. When is it better to use a semi-log model vs a log-linear model?
2. What happens to interpretation if β₁ is negative in a semi-log model?
| Software | Type | Key Features |
|----------|------|-------------|
| R | Open-source (free) | Requires programming knowledge; highly extensible |
| STATA | Licensed (paid) | Point-and-click; widely used in economics |
| E-Views | Licensed (paid) | Specialised for time series; point-and-click |
| SPSS | Licensed (paid) | Popular in social sciences |
| Gretl | Freeware | Freely downloadable; good for econometrics |
| EasyReg | Freeware | Downloadable; user-friendly |

**Quick Recall:**
- Open-source (free): R, Gretl, EasyReg, Matrixer
- Licensed (paid): STATA, E-Views, SPSS
- R advantage: extensible; R limitation: requires programming
- **Alternative Hypothesis**: In hypothesis testing, the condition opposite to the null hypothesis; expressed as H₁: β₂ ≠ 0 (slope coefficient is non-zero, positive or negative). ⭐ (exam-important)
- **Confidence Interval**: The range of values determining the probability that the parameter lies within the interval. ⭐ (exam-important)
- **Null Hypothesis**: The hypothesis asserting no significant difference between a specified population parameter and a claimed value; observed differences are due to sampling/experimental error. ⭐ (exam-important)
- **Population Regression Function (PRF)**: A function hypothesizing a theoretical linear relationship between a dependent variable and explanatory variables; defines how conditional expectation of Y responds to changes in X. ⭐ (exam-important)
- **Stochastic Error**: The error variable representing influences of variables not included in the regression model; reflects intrinsic randomness between variables. ⭐ (exam-important)

**Quick Recall:**
- H₀: no relationship; H₁: there is a relationship
- Parameter = fixed population quantity; Statistic = sample-based estimate
- PRF = theoretical (unknown); SRF = estimated from data

### Unit 2 — Statistical Inference: Point & Interval Estimation 🔴

**Point Estimation**
- **Estimator**: A rule or formula used to estimate a parameter (e.g., x̄ = Σxᵢ/n)
- **Estimate**: The specific numerical value obtained when the estimator is applied to a particular sample

**Interval Estimation (Confidence Interval)**

**Sampling Distribution**
- **Point Estimate**: A specific value of a statistic used to estimate a population parameter. ⭐ (exam-important)
- **Interval Estimate (Confidence Interval)**: A range (T₁, T₂) such that P(T₁ ≤ θ ≤ T₂) = 1 - α; also called a confidence interval. ⭐ (exam-important)
- **Estimator**: A rule or formula (function of sample observations) used to compute an estimate of a population parameter.
- **Estimate**: The specific numerical value of an estimator for a given sample; varies from sample to sample.
- **Sampling Distribution**: The probability distribution of a statistic (e.g., sample mean) computed from many samples of the same size.
- **Statistic**: A function of sample observations; used to estimate a population parameter (e.g., sample mean, sample variance). ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing estimator and estimate → ✅ Correct: Estimator = the formula (same for all samples); Estimate = the value (varies across samples)
- ❌ Mistake: Thinking "95% confidence" means there's a 95% chance the true parameter is in this specific interval → ✅ Correct: It means that if we repeated this sampling procedure many times, 95% of such intervals would contain the true parameter

**Quick Recall:**
- Point estimate = one number; Interval estimate = a range with stated probability
- Estimator (rule) → applied to sample → Estimate (number)
- Sampling distribution = distribution of estimates across many samples
- Builds on: Classical assumptions on u (Chunk 002)
- Is prerequisite for: Properties of estimators (below), Hypothesis testing (Chunk 004)
- Connects to: Confidence intervals in OLS (Block 2)

### Properties of a Good Estimator 🔴

**Unbiasedness**
- E(xᵢ) = (X₁ + X₂ + ... + Xₙ)/N = µ (in SRSWR)
- E(x̄) = (1/n)[E(X₁) + E(X₂) + ... + E(Xₙ)] = (1/n)(nµ) = µ ✓

**Minimum Variance Unbiased Estimator (MVUE)**
- E(Tₘ) = Ø (unbiased)
- Var(Tₘ) < Var(T) for any other unbiased estimator T

**Consistency**

**Efficiency**

**Sufficiency**

**Mean Squared Error (MSE)**
- **Unbiased Estimator**: An estimator T where E(T) = Ø; it targets the true parameter on average. ⭐ (exam-important)
- **Minimum Variance Unbiased Estimator (MVUE)**: The unbiased estimator with the smallest variance in its class. ⭐ (exam-important)
- **Consistent Estimator**: An estimator T where lim_{n→∞} P(T → Ø) = 1; requires both asymptotic unbiasedness and vanishing variance. ⭐ (exam-important)
- **Efficient Estimator**: An estimator with minimum variance among all consistent estimators; relative efficiency = V₁/V₂. ⭐ (exam-important)
- **Sufficient Estimator**: An estimator that uses all available information in the sample about the parameter Ø. ⭐ (exam-important)
- **Mean Squared Error (MSE)**: MSE(T) = Var(T) + [bias(T)]²; a composite measure combining bias and variance for comparing estimators.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking consistency implies unbiasedness → ✅ Correct: A biased estimator can be consistent (if bias → 0 as n → ∞)
- ❌ Mistake: Thinking efficiency means "small variance" alone → ✅ Correct: Efficiency is *relative* — smallest variance compared to all other consistent estimators
- ❌ Mistake: Confusing sufficiency with unbiasedness → ✅ Correct: Sufficiency is about using all sample information; unbiasedness is about centering on the true parameter
- An estimator can be unbiased but inefficient (large variance).
- An estimator can be biased but have lower MSE than an unbiased one (if variance gain > bias penalty).
- MSE = Var(T) for unbiased estimators (since bias = 0).

**Quick Recall:**
- 4 properties: Unbiasedness [E(T)=Ø] | Consistency [T→Ø as n→∞] | Efficiency [min variance] | Sufficiency [all info used]
- MVUE = best of all unbiased estimators (lowest variance)
- MSE = Var + Bias² — use when bias-variance trade-off arises
- x̄ is unbiased and consistent for µ; S² is consistent for σ²
- Is prerequisite for: Asymptotic Properties (Chunk 004), OLS BLUE properties (Block 2 Unit 4)
- Connects to: Gauss-Markov Theorem (Block 2) — OLS is BLUE (Best Linear Unbiased Estimator)
1. Can an estimator be sufficient but not efficient?
2. How does the Cramér-Rao lower bound relate to MVUE?

### Asymptotic Properties of Estimators 🔴

**Asymptotic Unbiasedness**

**Asymptotic Consistency**
1. lim_{n→∞} [E(T) - Ø] = 0 (bias vanishes)
2. lim_{n→∞} Var(T) = 0 (variance vanishes)
- **Asymptotic Unbiasedness**: lim_{n→∞} E(T) = Ø; the bias of estimator T vanishes as sample size grows to infinity. ⭐ (exam-important)
- **Asymptotic Consistency**: lim_{n→∞} [E(T) - Ø] = 0 AND lim_{n→∞} Var(T) = 0; both bias and variance approach zero as n→∞. ⭐ (exam-important)

**Quick Recall:**
- Asymptotic unbiasedness: bias → 0 as n → ∞
- Consistency (asymptotic): bias → 0 AND variance → 0 as n → ∞
- Consistency is stronger than asymptotic unbiasedness (requires two conditions)
- Builds on: Finite-sample properties (Chunk 003)
- Is prerequisite for: Law of Large Numbers (below), OLS large-sample theory (Block 2)

### Law of Large Numbers (Weak & Strong) 🔴

**Weak Law of Large Numbers (WLLN)**

**Strong Law of Large Numbers (SLLN)**
- **Weak Law of Large Numbers (WLLN)**: For i.i.d. {Xᵢ} with mean µ: lim_{n→∞} P(|Aₙ - µ| < α) = 1 for all α > 0; convergence in probability. ⭐ (exam-important)
- **Strong Law of Large Numbers (SLLN)**: For i.i.d. {Xᵢ} with mean µ: lim_{n→∞} P(Aₙ = µ) = 1; almost sure convergence. ⭐ (exam-important)
- **i.i.d. (Independent and Identically Distributed)**: A collection of random variables where each has the same probability distribution as the others, and all are mutually independent. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing WLLN and SLLN — SLLN is strictly stronger (almost sure convergence vs convergence in probability) → ✅ Correct: SLLN requires the more demanding condition
- ❌ Mistake: Thinking LLN requires a normal distribution → ✅ Correct: LLN applies for any distribution with finite mean µ

**Quick Recall:**
- WLLN: P(|Aₙ - µ| < α) → 1 as n → ∞ [convergence in probability]
- SLLN: P(Aₙ = µ) = 1 as n → ∞ [almost sure convergence; stronger]
- Both require i.i.d. with finite mean µ
- Builds on: Consistency (Chunk 003), Asymptotic properties (above)
- Is prerequisite for: Central Limit Theorem (below)
- Connects to: Sampling distribution concept revisited via CLT

### Central Limit Theorem (CLT) 🔴

**The CLT Statement**

**Standardised Normal Variable (Z-statistic)**
- **Central Limit Theorem (CLT)**: For i.i.d. {Xᵢ} with mean µ and variance σ², X̄ → N(µ, σ²/n) as n → ∞; the sample mean approaches normality regardless of population distribution. ⭐ (exam-important)
- **Standard Normal Variable (Z)**: Z = (X̄ - µ)/(σ/√n); approaches N(0,1) as n → ∞; the basis for Z-tests. ⭐ (exam-important)
- n = 30 tosses, heads = 13, x̄ = 0.43
- If coin is unbiased: p = 0.5, σ = √(p(1-p)) = 0.5
- Z = (0.43 - 0.5)/(0.5/√30) = −0.07/0.091 ≈ −0.77
- Since |Z| < 1.96 (at α=5%, two-tailed), fail to reject H₀; coin appears unbiased

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking CLT means population must be normal → ✅ Correct: CLT works for ANY population distribution with finite mean and variance
- ❌ Mistake: Applying CLT to very small samples (n < 30) → ✅ Correct: CLT is an asymptotic result; for small n, assumptions about population distribution matter more

**Quick Recall:**
- CLT: X̄ ~ N(µ, σ²/n) as n → ∞ (regardless of population distribution)
- Z = (X̄ - µ)/(σ/√n) → N(0,1)
- CLT underpins ALL large-sample hypothesis testing in econometrics
- Builds on: WLLN and SLLN (above), Sampling distribution (Chunk 003)
- Is prerequisite for: Hypothesis Testing (below), t-tests and F-tests in OLS (Block 2)

### Hypothesis Testing — Null/Alternative, Type Errors, Level of Significance 🔴

**Simple vs Composite Hypothesis**
- **Simple hypothesis**: Completely specifies all parameters (e.g., H: µ = µ₀, σ² = σ₀²)
- **Composite hypothesis**: Leaves at least one parameter unspecified or in a range (e.g., H: µ = µ₀ [σ² unspecified], or H: µ < µ₀)

**Null and Alternative Hypothesis**
- **H₀ (Null)**: The hypothesis whose validity is tested; asserts no relationship or a specific value. We either "reject" or "do not reject" H₀ — we never "accept" H₀.
- **H₁ (Alternative)**: Accepted/rejected indirectly via what happens to H₀.

**One-Tailed vs Two-Tailed Tests**
| Test Type | H₁ Form | Description |
|-----------|----------|-------------|
| Two-tailed | H₁: µ ≠ µ₀ | Reject in either tail |
| Right-tailed | H₁: µ > µ₀ | Reject only in right tail |
| Left-tailed | H₁: µ < µ₀ | Reject only in left tail |

**Type-I and Type-II Errors**
| Decision | H₀ True | H₀ False |
|----------|---------|----------|
| Accept H₀ | Correct | **Type-II Error** |
| Reject H₀ | **Type-I Error** | Correct |

**Level of Significance (α), Critical Region & p-value**
- **Level of significance (α)**: Maximum allowed probability of committing Type-I error. Commonly α = 5% or 1%.
- **Confidence coefficient (1-α)**: Probability of making the correct decision = 1 - P(Type-I error).
- **Critical region**: The set of test statistic values for which H₀ is rejected; separates acceptance from rejection regions.
- **p-value**: The lowest level of significance at which H₀ can be rejected; if p-value < α, reject H₀.
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

**Quick Recall:**
- Type-I: Reject true H₀ (P = α). Type-II: Fail to reject false H₀
- α = 5% → 95% confidence; α = 1% → 99% confidence
- p-value < α → Reject H₀; p-value > α → Do not reject H₀
- One-tailed: µ > µ₀ or µ < µ₀ | Two-tailed: µ ≠ µ₀
- Builds on: CLT (above), Confidence interval (Chunk 003)
- Is prerequisite for: t-test, F-test in OLS regression (Block 2)
- Connects to: CYP Check Your Progress 2 (Chunk 005 answers)

### Estimation Methods — OLS, MLE, Method of Moments 🔴

**Method of Least Squares (OLS)**

**Maximum Likelihood Method (MLE)**
1. **Consistent**: Converges to true value as n→∞
2. **Efficient**: Attains Cramér-Rao lower bound (asymptotically)
3. **Sufficient**: Uses all information in the sample
4. **Not necessarily unbiased** in finite samples (but can be corrected)
5. **Approximately normal**: For large samples, MLE estimates are approximately normally distributed
6. **Invariant**: If θ̂ is MLE of θ, then g(θ̂) is MLE of g(θ) for any function g

**Method of Moments**
- **Method of Least Squares**: A method that estimates unknown parameters by minimising the sum of squares of residuals S = Σeᵢ². ⭐ (exam-important)
- **Normal Equations**: The set of n equations obtained by setting ∂S/∂xⱼ = 0; solving them gives the OLS estimates.
- **Maximum Likelihood Estimator (MLE)**: The parameter value that maximises the likelihood function L(θ|data); consistent, efficient, sufficient, and asymptotically normal. ⭐ (exam-important)
- **Method of Moments**: Estimation method that equates sample moments to population moments and solves for parameters.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking OLS gives one equation per unknown → ✅ Correct: OLS gives n **normal equations** for n unknowns; exact solution exists only when equations = unknowns
- ❌ Mistake: Thinking MLE is always unbiased → ✅ Correct: MLE can be biased in small samples; bias correction exists

**Quick Recall:**
- OLS: Minimise Σeᵢ² → solve normal equations (n equations, n unknowns)
- MLE: Maximise L(θ|data) → consistent, efficient, sufficient, asymptotically normal
- MLE properties: (a) Consistent (b) Efficient (c) Sufficient (d) Not always unbiased (e) Approx normal (f) Invariant
- Method of Moments: sample moments = population moments
- Builds on: Properties of estimators (Chunk 003), CLT (above)
- Is prerequisite for: OLS derivation (Block 2, Unit 4), MLE applied in Logit/Probit (Block 4, Unit 15)
- Connects to: Matrix formulation of OLS (Unit 3 → Block 2)

**Quick Recall:**
- WLLN: P(|Aₙ - µ| < α) = 1; SLLN: P(Aₙ = µ) = 1 (both as n→∞)
- Type-I (worse): reject true H₀; Type-II: accept false H₀
- MLE: consistent + efficient + sufficient + approx normal + invariant

**Quick Recall:**
- Matrix algebra compresses multiple regression into Y = Xβ + u
- Key operation: (X'X)⁻¹X'y = OLS estimator formula

### Matrix Notation & Basic Types 🔴

**Matrix, Vector, Scalar — Definitions**
- An m × n matrix A has m rows and n columns; element aᵢⱼ is at row i, column j
- If m = n: **square matrix**
- An n × 1 matrix: **column vector** (a bold lowercase letter, e.g., **a**)
- A 1 × n matrix: **row vector**
- A 1 × 1 matrix: **scalar**

**Special Matrix Types**
| Type | Definition | Symbol |
|------|-----------|--------|
| Diagonal | aᵢⱼ = 0 for i ≠ j, aᵢᵢ ≠ 0 for some i | D |
| Identity | Diagonal with all diagonal elements = 1 | Iₙ |
| Lower-triangular | aᵢⱼ = 0 for i < j | L |
| Upper-triangular | aᵢⱼ = 0 for i > j | U |
| Null (zero) | All elements = 0 | 0 |
| Symmetric | A = A' (transpose equals original) | A |
| Transpose | A' = (aⱼᵢ) — rows and columns swapped | A' or Aᵀ |
- **Matrix**: A rectangular array of numbers; m × n means m rows, n columns. ⭐ (exam-important)
- **Square Matrix**: A matrix where m = n (equal number of rows and columns).
- **Column Vector / Row Vector**: An n×1 or 1×n matrix.
- **Diagonal Matrix**: A matrix where all off-diagonal elements are zero.
- **Identity Matrix (Iₙ)**: A diagonal matrix where all diagonal elements equal 1. ⭐ (exam-important)
- **Lower/Upper Triangular Matrix**: Matrix where elements below/above the main diagonal are zero.
- **Null (Zero) Matrix**: A matrix where all elements are zero.
- **Transpose (A' or Aᵀ)**: Obtained by swapping rows and columns of A; (aᵢⱼ) → (aⱼᵢ).
- **Symmetric Matrix**: A matrix equal to its own transpose: A = A'. ⭐ (exam-important)

**Quick Recall:**
- Iₙ = n×n identity; diagonal = zeros off-diagonal; symmetric = A = A'
- Transpose notation: A' or Aᵀ (both used interchangeably in the text)
- Symmetric matrices have nice properties: orthogonal diagonalisation (Chunk 006)
- Prerequisite for: Matrix multiplication (below), Inverse (below), Rank (below)
- Connects to: OLS normal equations in matrix form (Block 2)

### Matrix Multiplication 🔴

**Conformability Condition**

**Properties of Matrix Multiplication**
- (AB)C = A(BC) — **Associativity** ✓
- A(B + C) = AB + AC — **Distributivity** ✓
- AB ≠ BA in general — **Not commutative** ✗
- (AB)' = B'A' — **Transpose of product reverses order** ⭐
- If AB = BA, A and B are said to **commute**
- **Conformable Matrices**: Two matrices where the inner dimensions match for multiplication (columns of A = rows of B). ⭐ (exam-important)
- **Pre-multiplication**: Multiplying from the left (BA); **Post-multiplication**: multiplying from the right (AB) — results differ.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming AB = BA for all matrices → ✅ Correct: Matrix multiplication is generally NOT commutative
- ❌ Mistake: Confusing (AB)' = A'B' → ✅ Correct: (AB)' = **B'A'** — order reverses

**Quick Recall:**
- AB defined when: cols(A) = rows(B); result is m×q
- > - (AB)' = B'A' — reversal rule ⭐
- AB ≠ BA (not commutative, in general)
- Prerequisite for: Determinants, Inverse, OLS β̂ = (X'X)⁻¹X'y

### Determinants, Orthogonal Matrices & Trace 🔴

**Determinant**
- det(A) ≠ 0 ↔ A is **non-singular** (invertible)
- det(A) = 0 ↔ A is **singular** (not invertible)
- det(AB) = det(A) × det(B)
- det(A') = det(A)
- det(I) = 1
- det(λA) = λⁿ det(A) for n×n matrix

**Orthogonal Matrix**

**Trace of a Matrix**
- tr(A + B) = tr(A) + tr(B)
- tr(λA + μB) = λtr(A) + μtr(B)
- tr(A) = tr(A')
- tr(AA') = tr(A'A) = Σᵢⱼ aᵢⱼ²
- **tr(In) = n**
- **Determinant**: A scalar value encoding the invertibility of a square matrix; det(A) ≠ 0 ↔ A is invertible. ⭐ (exam-important)
- **Singular Matrix**: A square matrix with det(A) = 0; cannot be inverted. ⭐ (exam-important)
- **Non-Singular Matrix**: A square matrix with det(A) ≠ 0; invertible. ⭐ (exam-important)
- **Orthogonal Matrix**: A matrix where A'A = I (transpose = inverse); det(A) = ±1. ⭐ (exam-important)
- **Trace**: tr(A) = Σ aᵢᵢ; sum of diagonal elements; equals sum of eigenvalues. ⭐ (exam-important)

**Quick Recall:**
- det(A) ≠ 0 → invertible; det(A) = 0 → singular (cannot invert)
- Orthogonal: A'A = I → det(A) = ±1
- trace(A) = Σ diagonal elements = Σ eigenvalues (see Chunk 006)
- Is prerequisite for: Inverse (below), Rank (below), Eigenvalues (Chunk 006)
- Connects to: Idempotent matrix trace = rank (Chunk 006)

### Inverse of a Matrix 🔴

**Conditions for Invertibility**

**Computing the Inverse — Cofactor/Adjoint Method**
1. Compute det(A)
2. Compute the cofactor matrix (each cᵢⱼ = (-1)^{i+j} × det(Aᵢⱼ))
3. Adjoint = transpose of cofactor matrix
- 4. **A⁻¹ = (1/det(A)) × adj(A)** ⭐

**CYP Worked Example (3×3 Inverse)**
- det(A) = 10 (computed via cofactor expansion along row 2)
- Cofactor matrix = [[2,2,-2],[-11,4,6],[25,-10,-10]]
- adj(A) = (cofactor matrix)ᵀ = [[2,-11,25],[2,4,-10],[-2,6,-10]]
- A⁻¹ = (1/10) × adj(A)

**Properties of the Inverse**
- (λA)⁻¹ = (1/λ)A⁻¹ for scalar λ ≠ 0
- (A⁻¹)⁻¹ = A
- (A⁻¹)' = (A')⁻¹ — inverse and transpose commute
- (AB)⁻¹ = B⁻¹A⁻¹ — **order reverses**
- For diagonal A: diagonal elements of A⁻¹ are 1/aᵢᵢ
- **Inverse of a Matrix (A⁻¹)**: Unique matrix satisfying AA⁻¹ = A⁻¹A = I; exists only for non-singular matrices. ⭐ (exam-important)
- **Adjoint (Adjugate) Matrix**: Transpose of the cofactor matrix of A; used in computing A⁻¹.
- **Cofactor Cᵢⱼ**: (-1)^{i+j} × det(Aᵢⱼ) where Aᵢⱼ is the submatrix obtained by deleting row i and column j.

### ⚠️ Common Mistakes
- ❌ Mistake: (AB)⁻¹ = A⁻¹B⁻¹ → ✅ Correct: **(AB)⁻¹ = B⁻¹A⁻¹** — order reverses (same reversal as transpose)
- ❌ Mistake: Attempting to invert a singular matrix → ✅ Correct: Singular matrices have no inverse

**Quick Recall:**
- A⁻¹ = (1/det(A)) × adj(A); requires det(A) ≠ 0
- > - (AB)⁻¹ = B⁻¹A⁻¹ (reversal rule) ⭐
- In OLS: β̂ = (X'X)⁻¹X'y — requires (X'X) to be invertible
- Builds on: Determinants (above)
- Is prerequisite for: Rank (below), Partitioned Matrices (Chunk 006), OLS estimator derivation (Block 2)

### Rank of a Matrix 🔴

**Row Echelon Form**
1. All zero rows are at the bottom
2. Each non-zero row has more leading zeros than the row above it
3. Operations allowed: scalar multiplication of rows, addition/subtraction of rows

**Rank via Row Reduction**
- After R₂ → R₂ + 2R₁, R₃ → R₃ - 7R₁, then R₃ → R₃ + (1/2)R₂:
- Result: [[3,0,2,2],[0,42,28,58],[0,0,0,0]]
- 2 non-zero rows → **rank = 2**

**Key Rank Properties**
- rank(A) = 0 ↔ A = 0
- rank(Iₙ) = n
- rank(λA) = rank(A) for λ ≠ 0
- rank(diagonal) = number of non-zero diagonal elements
- rank(A + B) ≤ rank(A) + rank(B)
- rank(AB) ≤ min(rank A, rank B)
- For m×n matrix: rank(A) ≤ min{m, n}
- For n×n matrix: A⁻¹ exists ↔ rank(A) = n (full rank)
- **Rank of a Matrix**: Maximum number of linearly independent rows (= maximum linearly independent columns) in the matrix. ⭐ (exam-important)
- **Row Echelon Form**: A matrix form where all zero rows are at bottom and each non-zero row has strictly more leading zeros than the row above.
- **Linearly Independent Rows**: Rows where no row can be expressed as a linear combination of the others.
- **Full Rank**: For an n×n matrix, rank = n; matrix is invertible. For X (n×k), full column rank = rank k; required for OLS.

### ⚠️ Common Mistakes
- ❌ Mistake: rank of A ≠ rank of A' → ✅ Correct: rank(A) = rank(A') always
- ❌ Mistake: Thinking square matrix = full rank automatically → ✅ Correct: A square matrix can be rank-deficient (singular)

**Quick Recall:**
- Rank = non-zero rows in row echelon form = number of pivots
- Full rank (n×n): rank = n ↔ invertible ↔ det ≠ 0
- X must have full column rank (rank k) for OLS to work
- rank(AB) ≤ min(rank A, rank B)
- Builds on: Determinants and Inverse (above)
- Continues into: Properties verified for M-matrix (Chunk 006)
- Connects to: Multicollinearity in regression — X rank-deficient when variables are perfectly collinear (Block 3)
- **Partitioned Matrix**: A matrix divided into submatrices (blocks); allows block-level arithmetic. ⭐ (exam-important)

**Quick Recall:**
- Partitioned matrix: Y = [[A,B],[C,D]]; Y' = [[A',C'],[B',D']]
- Block diagonal inverse: [[A,0],[0,D]]⁻¹ = [[A⁻¹,0],[0,D⁻¹]]
- tr([[A,B],[C,D]]) = tr(A) + tr(D)
- Direct sum: A ⊕ B = [[A,0],[0,B]]

### Eigenvalues and Eigenvectors 🔴

**Characteristic Equation and Eigenvalues**

**Eigenvectors and Eigenspaces**

**Diagonalisation: A = CΛC⁻¹**
- C = [x₁,...,xₙ] (matrix of eigenvectors)
- Λ = diag(λ₁,...,λₙ) (diagonal matrix of eigenvalues)
- **AT = TΛ** → **C⁻¹AC = Λ** → **A = CΛC⁻¹**

**Key Relationships**
- **trace(A) = trace(Λ) = Σλᵢ** (sum of eigenvalues = trace)
- **det(A) = det(Λ) = Πλᵢ** (product of eigenvalues = determinant)
- Eigenvalues of A⁻¹ = reciprocals of eigenvalues of A (1/λᵢ)
- Eigenvalues of A² = squares of eigenvalues of A (λᵢ²)
- Eigenvectors of A⁻¹, A², Aᵏ are the **same** as those of A
- **Eigenvalue (λ)**: A scalar satisfying Ax = λx for some non-zero x; root of the characteristic equation det(A - λI) = 0. ⭐ (exam-important)
- **Eigenvector**: A non-zero vector x such that Ax = λx for some eigenvalue λ. ⭐ (exam-important)
- **Characteristic Equation**: det(A - λI) = 0; an nth-degree polynomial whose roots are the eigenvalues of A. ⭐ (exam-important)
- **Eigenspace**: The set of all eigenvectors corresponding to a particular eigenvalue λ, plus the zero vector; forms a subspace.
- **Diagonalizable Matrix**: A matrix A that can be written as A = CΛC⁻¹ where C is a matrix of eigenvectors and Λ is diagonal; possible if A has n linearly independent eigenvectors.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking all matrices are diagonalizable → ✅ Correct: Only matrices with n linearly independent eigenvectors are diagonalizable
- ❌ Mistake: Computing eigenvalues of A² separately → ✅ Correct: Eigenvalues of A² = (eigenvalues of A)², eigenvectors are the same

**Quick Recall:**
- Eigenvalue equation: (A - λI)x = 0 → det(A - λI) = 0 → characteristic equation
- > - trace(A) = Σλᵢ; det(A) = Πλᵢ ⭐
- A = CΛC⁻¹ (diagonalisation) → simplifies Aᵏ = CΛᵏC⁻¹
- A⁻¹ has eigenvalues 1/λᵢ with the same eigenvectors
- Builds on: Determinants and Trace (Chunk 005)
- Is prerequisite for: Symmetric matrices (below), Idempotent matrices (below)
- Connects to: Variance-covariance matrices (positive definite) in OLS

### Special Matrices — Symmetric, Positive Definite, PSD 🔴

**Symmetric Matrices and Orthogonal Diagonalization**
- rank(A) = rank(Λ) = number of non-zero eigenvalues of A
- det(A) = Πλᵢ; trace(A) = Σλᵢ for symmetric A (same as general case)
- Rank is preserved under non-singular and orthogonal transformations

**Positive Definite (PD) Matrix**
- PD matrices are always non-singular (invertible).
- Variance-covariance matrices are positive definite.

**Positive Semi-Definite (PSD) Matrix**
- PSD matrices may be singular.
| Property | Condition | Eigenvalues | Invertible? |
|----------|-----------|-------------|------------|
| Positive Definite (PD) | b'Ab > 0 | All λᵢ > 0 | Yes |
| Positive Semi-Definite (PSD) | b'Ab ≥ 0 | All λᵢ ≥ 0 | Maybe |

**Matrix Square Root and Cholesky Decomposition**
- **Symmetric Matrix**: A = A'; all eigenvalues are real; eigenvectors for distinct eigenvalues are orthogonal. ⭐ (exam-important)
- **Positive Definite (PD) Matrix**: Symmetric matrix where b'Ab > 0 for all b ≠ 0; all eigenvalues strictly positive; always invertible. ⭐ (exam-important)
- **Positive Semi-Definite (PSD) Matrix**: Symmetric matrix where b'Ab ≥ 0 for all b ≠ 0; all eigenvalues non-negative; may be singular. ⭐ (exam-important)
- **Cholesky Decomposition**: Factorisation of a symmetric PSD matrix as A = LL' where L is lower triangular; used to compute matrix square roots.
- **Matrix Square Root (A^{1/2})**: Matrix such that A^{1/2} × A^{1/2} = A; exists for symmetric PSD matrices.

**Quick Recall:**
- Symmetric: real eigenvalues; orthogonal eigenvectors for distinct λ; C'AC = Λ, A = CΛC'
- > - PD: b'Ab > 0 ↔ all λᵢ > 0 → always invertible ⭐
- PSD: b'Ab ≥ 0 ↔ all λᵢ ≥ 0 → may be singular
- Variance-covariance matrix is always PD (in regular cases)
- Builds on: Eigenvalues (above), Orthogonal matrices (Chunk 005)
- Is prerequisite for: Idempotent matrix (below), Fisher Information Matrix (Chunk 007)
- Connects to: Gauss-Markov theorem — variance of OLS estimator involves PD matrix (Block 2)

**Quick Recall:**
- QR: A = QR where Q'Q = Iₙ (semi-orthogonal) and R upper triangular
- Gram-Schmidt orthogonalisation produces the columns of Q
- Used for numerical stability in OLS computation

**Quick Recall:**
- SVD: A = SΛ^{1/2}T'; works for any m×n matrix (unlike eigendecomposition)
- S'S = Iᵣ, T'T = Iᵣ; Λ = diag(singular values squared)

### Idempotent Matrix 🔴

**Definition: MM = M**

**Key Property: rank(M) = trace(M)**
- **rank(M) = trace(M)** ⭐ (unique to idempotent matrices!)

**The M-Matrix (Annihilator) and H-Matrix (Hat)**
- **Idempotent Matrix**: A matrix M where M² = MM = M. ⭐ (exam-important)
- **Annihilator Matrix (M)**: M = Iₙ - X(X'X)⁻¹X'; idempotent and symmetric; projects onto orthogonal complement of column space of X; MX = 0. ⭐ (exam-important)
- **Hat Matrix (H)**: H = X(X'X)⁻¹X'; idempotent and symmetric; projects Y onto fitted values Ŷ = HY. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking rank(M) = n for the M-matrix → ✅ Correct: rank(M) = n - k (n observations minus k parameters)
- ❌ Mistake: Forgetting that rank(idempotent) = trace(idempotent) → ✅ Correct: This is the defining trick for idempotent matrices

**Quick Recall:**
- > - Idempotent: MM = M ⭐
- > - rank(M) = trace(M) for idempotent M ⭐
- M = I - X(X'X)⁻¹X': symmetric, idempotent, MX = 0, rank = n-k
- H = X(X'X)⁻¹X': symmetric, idempotent, HX = X, rank = k
- Builds on: Matrix inverse (Chunk 005), Symmetric matrices (above)
- Is prerequisite for: OLS residuals ê = MY (Block 2), Degrees of freedom in regression
- Continues into: CYP 2 Q2(b) proof of MX=0, Q2(c) rank computation (Chunk 007)
- More generally: **vec(ABC) = (C' ⊗ A) vec(B)** ⭐
- **Kronecker Product (A ⊗ B)**: Block matrix where each element aᵢⱼ of A is replaced by the submatrix aᵢⱼB; dimension: (mp) × (nq). ⭐ (exam-important)
- **Vec-Operator**: An operator that stacks the columns of a matrix into a single column vector; vec(A) = [a₁', a₂', ..., aₙ']'. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing A ⊗ B with B ⊗ A → ✅ Correct: Kronecker product is NOT commutative; A ⊗ B ≠ B ⊗ A in general

**Quick Recall:**
- Kronecker: A ⊗ B replaces each aᵢⱼ with the block aᵢⱼB; dimension mp×nq
- vec(A): stacks columns of A into one column vector
- > - **vec(ABC) = (C' ⊗ A) vec(B)** ⭐ — the key identity
- vec(ab') = b ⊗ a

### Matrix Differentiation — Jacobian, Gradient & Hessian 🔴

**Jacobian Matrix**

**Gradient Matrix (Score Function in MLE)**

**Real Hessian Matrix**

**Fisher Information Matrix I(θ)**
- **Jacobian Matrix**: m×n matrix of first-order partial derivatives of a vector function **f**: Rⁿ → Rᵐ; Jᵢⱼ = ∂fᵢ/∂xⱼ. ⭐ (exam-important)
- **Gradient Matrix**: The gradient ∇f = [∂f/∂xᵢ]ᵀ; n×1 vector of first-order partial derivatives of a scalar function f. ⭐ (exam-important)
- **Hessian Matrix**: n×n symmetric matrix of second-order partial derivatives of f: Hᵢⱼ = ∂²f/(∂xᵢ∂xⱼ). ⭐ (exam-important)
- **Score Function S(θ)**: The gradient of the log-likelihood: S(θ) = ∂logL(θ)/∂θ; equals zero at the MLE estimate. ⭐ (exam-important)
- **Fisher Information Matrix I(θ)**: I(θ) = -E[∂²logL/∂θ∂θ']; a positive semi-definite matrix quantifying the information about θ in the data. ⭐ (exam-important)
- **Log-Likelihood Function**: logL(θ) = log P(data|θ); maximised in MLE to find θ̂.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing observed and expected Fisher information → ✅ Correct: Observed I(θ) = -Hessian(logL); Expected I(θ) = E_θ[observed I(θ)]
- ❌ Mistake: Thinking the Hessian is the gradient → ✅ Correct: Gradient = first derivatives (n×1 vector); Hessian = second derivatives (n×n matrix)
- ❌ Mistake: Assuming score function is non-zero at MLE → ✅ Correct: At MLE, S(θ̂) = 0 (gradient = 0 at maximum)

**Quick Recall:**
- > - Jacobian: ∂f/∂x (vector-to-vector); Gradient: ∂f/∂x (scalar-to-vector) ⭐
- > - Hessian: ∂²f/∂x∂x' (n×n, symmetric) ⭐
- Score: S(θ) = ∂logL/∂θ = 0 at MLE
- > - Fisher Information: I(θ) = -E[Hessian(logL)]; positive semi-definite ⭐
- For Normal N(µ,σ²): I(θ) = diag(n/σ², n/2σ⁴)
- Builds on: Matrix multiplication (Chunk 005), MLE (Chunk 004)
- Connects to: Cramér-Rao lower bound (the inverse of Fisher Information gives the minimum variance of any unbiased estimator)
- Connects to: Block 2 — OLS score equations are normal equations

**Quick Recall:**
- CYP 1: Inverse via cofactor method; Rank via row reduction
- CYP 2: T⁻¹AT = Λ (diagonalisation); M symmetric, idempotent, MX=0, rank=n-k
- CYP 3: vec(ABC)=(C'⊗A)vec(B); Fisher I(θ) = diag(n/σ², n/(2σ⁴)) for Normal
