# Complete Notes


## Section: Course Overview — MECE 101 Structure 🟢

### Core Idea
MECE 101 is an introductory econometrics course from IGNOU covering single-equation regression models. It is organised into four blocks: Introduction (Units 1–3), Classical Regression Model (Units 4–7), Violations of Basic Assumptions (Units 8–13), and Extensions of Regression Models (Units 14–16). The companion advanced course is MECE 102: Advanced Econometric Methods (time series and panel data).

> **In Simple Terms:** Think of the four blocks as four chapters in a story: first you learn what econometrics is, then you learn the basic tool (OLS regression), then you learn what happens when things go wrong, and finally you learn how to handle special cases.

### Key Concepts

#### MECE 101 Block Structure

| Block | Title | Units | Key Topics |
|-------|-------|-------|-----------|
| Block 1 | Introduction | 1–3 | What econometrics is, Statistical foundations, Matrix algebra |
| Block 2 | Classical Regression Model | 4–7 | Two-variable OLS, Residuals, Multiple regression |
| Block 3 | Violations of Basic Assumptions | 8–13 | Specification, Autocorrelation, Multicollinearity, Heteroscedasticity, Errors-in-variables, Endogeneity |
| Block 4 | Extensions of Regression Models | 14–16 | Dummy variables, Qualitative dependent variables (Logit/Probit), Simultaneous equations |

### Quick Recall
> **Quick Recall:**
> - 4 Blocks → 16 Units total
> - Block 1: Foundations; Block 2: OLS; Block 3: Violations; Block 4: Extensions
> - Advanced follow-up: MECE 102 (time series, panel data)

### Connections
- Entire course is context for all subsequent chunks

---

## Section: Unit 1 Objectives & Scope of Econometrics 🟡

### Core Idea
Unit 1 sets out what econometrics is and what a student should be able to do after studying it. Econometrics is the application of mathematical and statistical methods to economic data to give empirical content to economic relationships. After Unit 1, students are expected to explain why econometrics matters, distinguish deterministic from stochastic relationships, and identify reasons for including an error variable.

> **In Simple Terms:** Econometrics is where economics meets statistics — you take an economic theory, express it as a regression equation, throw in real data, and use statistics to check if the theory holds up.

### Key Concepts

#### What is Econometrics?
Econometrics is a powerful tool for understanding economic relationships and conducting meaningful research. Economists use econometric methods across fields — macroeconomics, finance, labour economics, health economics — and for business decisions, policy formulation, and prediction. It combines economic theory, mathematics, and statistical inference.

#### Theoretical vs Applied Econometrics

| Dimension | Theoretical Econometrics | Applied Econometrics |
|-----------|--------------------------|----------------------|
| Focus | Developing new statistical methods | Using existing methods on real-world data |
| Output | New estimators, test statistics | Empirical findings, policy conclusions |
| Example | Deriving properties of OLS | Estimating a consumption function |

### Definitions
- **Econometrics**: The application of mathematical statistics and probability theory to economic data to test hypotheses and estimate economic relationships. ⭐ (exam-important)
- **Theoretical Econometrics**: The branch that develops new statistical methods for use in economic analysis.
- **Applied Econometrics**: The branch that applies established econometric methods to specific economic questions using real data.

### Quick Recall
> **Quick Recall:**
> - Econometrics = Economics + Mathematics + Statistics applied to data
> - Theoretical = develops new tools; Applied = uses those tools on real data
> - After MECE 101: can do model selection, estimation, and diagnostics

### Connections
- Builds into: Econometric Models (Chunk 002: Econometric Models)
- Prerequisite for: All subsequent Units in this block

### Open Questions
1. What makes an econometric method "applied" vs "theoretical"?


---

<!-- Continues from: Unit 1 Objectives (Chunk 001: Course Overview — MECE 101 Structure) -->
<!-- Continues into: Software packages, Unit 1 Summary (Chunk 003: End of Unit 1 — Software, Summary & Key Words) -->

## Section: Econometric Models 🔴

### Core Idea
An econometric model is a simplified, mathematical representation of economic reality, used to analyse and predict economic behaviour. It is stochastic — meaning it includes a random error term — unlike a purely deterministic economic model. The key tension in econometrics is that we observe a sample from a population; the Population Regression Function (PRF) is unknown, and we use the Sample Regression Function (SRF) to estimate it.

> **In Simple Terms:** An econometric model is like a recipe that tries to capture how the economy works. But since we can't know everything, we add an "error" ingredient — it represents everything we missed or can't measure.

### Key Concepts

#### Econometric Model vs Economic Model

| Dimension | Economic Model | Econometric Model |
|-----------|---------------|-------------------|
| Form | Theoretical, logical | Mathematical + Statistical |
| Includes error? | No | Yes — stochastic error (u) |
| Testable? | Sometimes | Yes — uses real data |
| Purpose | Explain behaviour conceptually | Estimate, test, predict |

An economic model is based on assumptions that simplify reality (e.g., assuming only two factors of production: capital and labour). An econometric model retains these assumptions but adds a probabilistic structure so it can be estimated with data.

#### Population Regression Function (PRF) vs Sample Regression Function (SRF)
Since it is impractical to conduct a census, econometrics works with a single sample. The PRF is the true theoretical relationship in the population — it is unknown. The SRF is our estimate of it from sample data. Statistical significance of estimates is crucial because we are drawing inferences about the population from a single sample. Different researchers using the same dataset may reach different conclusions depending on their assumptions and model choices.

### Definitions
- **Econometric Model**: A statistical model, expressed in mathematical form, specifying relationships between economic quantities; a simplification of reality estimated using real data. ⭐ (exam-important)
- **Population Regression Function (PRF)**: The theoretical relationship between Y and X in the entire population; represents conditional expectation E(Y|X). ⭐ (exam-important)
- **Sample Regression Function (SRF)**: The estimated relationship derived from sample data; used to draw inferences about the PRF.

### Mechanisms / Processes
Model building choices → Variable inclusion → Assumption on error structure → Estimation → Inference → PRF approximation

### Examples
**Example: Keynesian Consumption Model**
In the Keynesian model, aggregate consumption depends on aggregate income. We ignore individual households and firm behaviour. A macro econometric model of this form is Y = βₒ + β₁C + β₂I + β₃G + u, where the focus is on equilibrium output, not individual decisions.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking an econometric model must capture all determinants of Y → ✅ Correct: It only includes the *important* variables; the rest are absorbed by u

### Quick Recall
> **Quick Recall:**
> - Econometric model = Economic model + Stochastic error term
> - PRF is unknown (population truth); SRF is what we estimate from sample
> - Statistical significance matters because we work with one sample, not the whole population

### Connections
- Builds on: Scope of Econometrics (Chunk 001: Course Overview — MECE 101 Structure)
- Is prerequisite for: Stochastic Specification (below), Functional Forms (below)

---

## Section: Important Steps in an Econometric Study 🔴

### Core Idea
Every econometric study follows six sequential steps, regardless of its specific objective or data source. The steps run from stating a hypothesis to interpreting results. This process is iterative — results may lead the researcher back to revise the model specification.

> **In Simple Terms:** Econometrics works like a scientific method: you guess (hypothesis), write it as a math equation, collect data, estimate, test, and interpret. If the results don't make sense, you revise and try again.

### Key Concepts

#### Six Steps in Econometric Research

1. **State the hypothesis**: An assertion about an economic relationship, drawn from theory or logic. Written as H₀ and H₁.
2. **Formulate the mathematical model**: Transform the hypothesis into one or more equations (the economic model).
3. **Collect relevant data**: Primary or secondary sources; entered into a worksheet (e.g., Excel). Data must cover all variables in the model.
4. **Estimate parameters**: Select an appropriate estimation method (Least Squares, Maximum Likelihood, or Method of Moments) and compute parameter values.
5. **Test the hypothesis**: Use test statistics (e.g., t-ratio) or p-values to assess statistical significance.
6. **Interpret and draw inferences**: Explain results in economic terms; draw policy conclusions.

### Definitions
- **Hypothesis**: An assertion or claim about a property of a population; may express a relationship between variables. ⭐ (exam-important)
- **Null Hypothesis (H₀)**: The hypothesis whose validity is tested; asserts no relationship between variables (e.g., H₀: β₁ = 0).
- **Alternative Hypothesis (H₁)**: Tested indirectly; its acceptance/rejection is determined by what happens to H₀.

### Mechanisms / Processes
Hypothesis → Mathematical Model → Data Collection → Estimation → Hypothesis Testing → Interpretation → (Revision loop)

### ⚠️ Common Mistakes
- ❌ Mistake: "Accepting" a null hypothesis → ✅ Correct: We either "reject" or "do not reject" H₀; we never truly "accept" it

### Quick Recall
> **Quick Recall:**
> - 6 Steps: Hypothesis → Model → Data → Estimation → Testing → Interpretation
> - Steps 1–2 are theoretical; Steps 3–6 are empirical
> - The process is iterative — unsatisfactory results trigger revision

### Connections
- Builds on: Econometric Models (above)
- Connects to: Estimation Methods (Chunk 004: Asymptotic Properties of Estimators)

---

## Section: Specification — Deterministic vs Stochastic Relationship 🔴

### Core Idea
Economic relationships are not exact. A deterministic model says Y is precisely determined by X (no randomness). A stochastic model acknowledges that Y depends on X plus a random error term (u), which captures all factors not explicitly included. The error term makes econometric models realistic — it represents our ignorance of reality, not just noise.

> **In Simple Terms:** If economics were deterministic, every household with the same income would spend exactly the same on food. But they don't — families differ in size, tastes, habits. The error term is the "everything else" bucket.

### Key Concepts

#### Deterministic Relationship
A relationship of the form Y = f(X) with no random component. Given X, Y is uniquely determined. Example: Ohm's Law in physics (V = IR) is deterministic. In economics, no such pure relationships exist.

#### Stochastic Relationship
A relationship of the form Y = f(X) + u, where u is a random variable. Given X, Y is determined up to a random disturbance. All regression models in econometrics are stochastic.

#### Role of the Error Variable (u)
The error term captures three sources of randomness:
1. **Omitted explanatory variables** — variables that affect Y but are not included in the model
2. **Wrong functional form** — e.g., fitting a linear model when the true relationship is non-linear
3. **Selection of wrong sample** — sampling error or measurement error in the data

#### Classical Assumptions on u (Equations 1.3–1.7)
The "classical" in Classical Regression Model comes from assumptions about u:
- E(u) = 0 — zero mean
- Var(u) = σ² — constant variance (homoscedasticity)
- Cov(uᵢ, uⱼ) = 0 for i ≠ j — no autocorrelation
- u is independent of X
- u ~ N(0, σ²) — normally distributed (for inference)

### Definitions
- **Deterministic Component**: The systematic part of the regression equation; E(Y|X) = βₒ + β₁X. ⭐ (exam-important)
- **Stochastic Component / Error Variable (u)**: The random disturbance term that makes the regression relationship probabilistic; captures omitted variables, wrong functional form, and sampling error. ⭐ (exam-important)
- **Classical Regression Model**: A linear regression model where the error variable fulfils all classical assumptions (zero mean, homoscedasticity, no autocorrelation, normality). ⭐ (exam-important)

### Mechanisms / Processes
Y = Deterministic Component + Stochastic Component
Y_i = β₀ + β₁X_i + u_i (two-variable form)
Y = β₀ + β₁X₁ + β₂X₂ + ... + β_kX_k + u (multiple regression form)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking u is just "random noise" → ✅ Correct: u has three specific sources — omitted variables, specification error, and sampling error
- ❌ Mistake: Confusing stochastic model with a bad model → ✅ Correct: Stochasticity is inherent in all economic data

### Quick Recall
> **Quick Recall:**
> - Deterministic: Y = f(X) exactly; Stochastic: Y = f(X) + u
> - Error u has 3 sources: omitted vars, wrong functional form, sampling error
> - OLS applies when u fulfils classical assumptions (zero mean, constant variance, no correlation)

### Connections
- Builds on: Econometric Models (above)
- Is prerequisite for: Block 2 (OLS estimation), Block 3 (violations of assumptions)

---

## Section: Data Generation Process (DGP) 🔴

### Core Idea
The Data Generation Process (DGP) is the real-world mechanism that produces the data we observe. We never know the DGP directly — we only observe its outcomes. Econometric modelling is the attempt to uncover the DGP through approximating models. Two philosophical approaches exist: general-to-specific (start big, trim down) and specific-to-general (start simple, add variables). The standard is iterative model building with four steps.

> **In Simple Terms:** The DGP is like the hidden recipe for reality. We only see the dish (the data), not the recipe. Econometrics is our attempt to reverse-engineer that recipe by trying different models.

### Key Concepts

#### General-to-Specific vs Specific-to-General

| Approach | Direction | Description |
|----------|-----------|-------------|
| General-to-Specific | Many → fewer variables | Start with a large model; remove irrelevant variables. Preferred in practice. |
| Specific-to-General | Few → more variables | Start with a simple model; add variables based on logic. Less preferred. |

#### Four Steps in DGP-Based Model Building
1. Guess the DGP (choose variables, functional form)
2. Assume the associated probability theory (choose probability distribution for u)
3. Use that theory for empirical evidence (estimate and test)
4. Revise the model if results don't match data → repeat

### Definitions
- **Data Generation Process (DGP)**: The true real-world mechanism that generates the observed data; unknown to the researcher; represents reality. ⭐ (exam-important)

### Mechanisms / Processes
Guess DGP → Assume probability structure → Estimate → Test → If unsatisfactory: Revise → Repeat

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking a good-fitting model = we understand the DGP → ✅ Correct: A fitting model only means "our model was adequate for this case" — it does NOT reveal the true DGP

### Quick Recall
> **Quick Recall:**
> - DGP = hidden truth; we approximate it with econometric models
> - General-to-specific: preferred approach (start big, trim down)
> - Good fit ≠ true DGP revealed; model building is iterative

### Connections
- Builds on: Stochastic specification (above)
- Connects to: Karl Popper's falsificationism (referenced: MEC 109)

---

## Section: Functional Forms — Classical, Semi-Log, Log-Linear 🔴

### Core Idea
Regression models do not always have to be linear in variables. Three functional forms are standard: (1) the classical linear model (linear in both parameters and variables), (2) the semi-log model (log Y, linear X — estimates growth rates), and (3) the log-linear (double-log) model (log Y, log X — estimates elasticities). Non-linear models can often be made "intrinsically linear" by logarithmic transformation, enabling OLS estimation.

> **In Simple Terms:** OLS only works directly on equations that are straight-line in their variables. But taking logs can turn a curved equation into a straight one — then OLS can handle it.

### Key Concepts

#### Classical Linear Regression Model
**Two-variable form**: Y_i = β₀ + β₁X_i + u_i ... (Eq. 1.2)
**Multiple regression form**: Y = β₀ + β₁X₁ + β₂X₂ + ... + β_kX_k + u ... (Eq. 1.8)

Interpretation of β₁ (linear): A **unit increase in X** produces a **β₁ unit increase in Y** (absolute change, constant throughout the sample).

#### Semi-Log Model
Original non-linear form: Y_t = e^{β₀ + β₁t + u_t} ... (Eq. 1.9)

After taking natural logs: **ln Y_t = β₀ + β₁t + u_t** ... (Eq. 1.10)

Interpretation of β₁ (semi-log): A **unit increase in X** produces a **β₁ × 100 percent increase in Y** (relative/percentage change). Useful for estimating **growth rates**.

Mathematical derivation:
d(lnY)/dt = β₁  →  (1/Y)(dY/dt) = β₁  →  β₁ = proportional rate of change

#### Log-Linear (Double-Log) Model
Original form: Y = β₀ X^{β₁} ... (Eq. 1.14)

After taking natural logs of both variables: **ln Y_i = β₀ + β₁ ln X_i + u_i** ... (Eq. 1.16)

Interpretation of β₁ (log-linear): A **1 percent increase in X** produces a **β₁ percent increase in Y** — β₁ is the **elasticity** of Y with respect to X.

Mathematical derivation:
d(lnY)/d(lnX) = β₁  →  β₁ = (dY/dX)(X/Y) = elasticity

| Model | Form | β₁ Interpretation |
|-------|------|-------------------|
| Linear | Y = β₀ + β₁X + u | Absolute change: ΔY = β₁ for ΔX = 1 |
| Semi-Log | lnY = β₀ + β₁X + u | Percentage change in Y per unit change in X (growth rate) |
| Log-Linear (Double-Log) | lnY = β₀ + β₁lnX + u | Elasticity: % change in Y per 1% change in X |

### Definitions
- **Linear Regression Model**: A model linear in both parameters (β) and variables (X, Y); can be estimated directly by OLS. ⭐ (exam-important)
- **Intrinsically Linear Model**: A non-linear model that can be transformed into a linear form (e.g., by taking logarithms), enabling OLS estimation.
- **Semi-Log Model**: A regression model where only one variable is in logarithmic form (typically ln Y); the slope coefficient measures the **proportional/percentage rate of change** in Y per unit change in X. ⭐ (exam-important)
- **Log-Linear (Double-Log) Model**: A regression model where both variables are in logarithmic form; the slope coefficient measures the **elasticity** of Y with respect to X. ⭐ (exam-important)
- **Elasticity**: The percentage change in Y for a 1 percent change in X; given by β₁ in the log-linear model. ⭐ (exam-important)

### Mechanisms / Processes
**Converting Semi-Log to Linear:**
Y_t = e^{β₀ + β₁X + u}  →  (take ln both sides)  →  lnY_t = β₀ + β₁X + u  → OLS applicable

**Converting Log-Linear to Linear:**
Y = β₀X^{β₁}  →  (take ln both sides)  →  lnY = lnβ₀ + β₁lnX  →  Y' = β₀' + β₁X' + u  → OLS applicable

### Examples
**Example: Slope interpretation comparison**
- Linear: Y = 5 + 2X → For every 1 unit increase in X, Y increases by **2 units** (absolute).
- Semi-Log: lnY = 5 + 0.03X → For every 1 unit increase in X (e.g., 1 year), Y increases by **3% per year** (growth rate).
- Log-Linear: lnY = 5 + 0.8lnX → For every **1% increase in X**, Y increases by **0.8%** (elasticity = 0.8, inelastic).

### ⚠️ Common Mistakes
- ❌ Mistake: Interpreting semi-log β₁ as an absolute change → ✅ Correct: It is a proportional (percentage) change
- ❌ Mistake: Confusing semi-log with log-linear — one takes log of Y only, the other takes log of both Y and X → ✅ Correct: Semi-log = lnY; Log-linear = lnY and lnX
- ❌ Mistake: Thinking we can apply OLS to Y_t = e^{β₀+β₁X} directly → ✅ Correct: Must transform first (take logs) to make it intrinsically linear

### Edge Cases & Caveats
- Semi-log and log-linear require Y > 0 and X > 0 (logarithms of negative numbers undefined).
- The interpretation of β₁ in semi-log model gives an approximation of the growth rate (exact formula uses e^{β₁} - 1).

> **Quick Recall:**
> - Linear: ΔY = β₁ (absolute) | Semi-Log: %ΔY = β₁ (growth rate) | Log-Linear: %ΔY/%ΔX = β₁ (elasticity)
> - CYP Q3 slope interpretations: (i) Absolute ΔY (ii) % ΔY per unit ΔX (iii) Elasticity β₁%
> - Intrinsically linear = non-linear model that logs can linearise

### Connections
- Builds on: Classical Regression Model (above)
- Connects to: Block 2 Units 4–7 (OLS estimation of these models)
- Contrasts with: Non-linear models not in scope of MECE 101

### Open Questions
1. When is it better to use a semi-log model vs a log-linear model?
2. What happens to interpretation if β₁ is negative in a semi-log model?


---

<!-- Continues from: Functional Forms / DGP (Chunk 002: Econometric Models) -->
<!-- Continues into: Asymptotic Properties, LLN, CLT (Chunk 004: Asymptotic Properties of Estimators) -->

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
- Builds on: Classical assumptions on u (Chunk 002: Econometric Models)
- Is prerequisite for: Properties of estimators (below), Hypothesis testing (Chunk 004: Asymptotic Properties of Estimators)
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
- Is prerequisite for: Asymptotic Properties (Chunk 004: Asymptotic Properties of Estimators), OLS BLUE properties (Block 2 Unit 4)
- Connects to: Gauss-Markov Theorem (Block 2) — OLS is BLUE (Best Linear Unbiased Estimator)

### Open Questions
1. Can an estimator be sufficient but not efficient?
2. How does the Cramér-Rao lower bound relate to MVUE?


---

<!-- Continues from: Estimator Properties — Sufficiency, MSE (Chunk 003: End of Unit 1 — Software, Summary & Key Words) -->
<!-- Continues into: Unit 2 CYP Answers + Unit 3 Matrix Algebra (Chunk 005: Unit 2 CYP Answers (Self-Check)) -->

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
- Builds on: Finite-sample properties (Chunk 003: End of Unit 1 — Software, Summary & Key Words)
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
- Builds on: Consistency (Chunk 003: End of Unit 1 — Software, Summary & Key Words), Asymptotic properties (above)
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
- Builds on: WLLN and SLLN (above), Sampling distribution (Chunk 003: End of Unit 1 — Software, Summary & Key Words)
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
- Builds on: CLT (above), Confidence interval (Chunk 003: End of Unit 1 — Software, Summary & Key Words)
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
- Builds on: Properties of estimators (Chunk 003: End of Unit 1 — Software, Summary & Key Words), CLT (above)
- Is prerequisite for: OLS derivation (Block 2, Unit 4), MLE applied in Logit/Probit (Block 4, Unit 15)
- Connects to: Matrix formulation of OLS (Unit 3 → Block 2)


---

<!-- Continues from: Estimation Methods (Chunk 004: Asymptotic Properties of Estimators) -->
<!-- Continues into: Partitioned Matrices, Eigenvalues, Special Matrices (Chunk 006: Partitioned Matrices) -->

## Section: Unit 2 CYP Answers (Self-Check) 🟡

### Core Idea
The Check Your Progress answers for Unit 2 validate the core concepts of statistical inference: parameter vs statistic, point vs interval estimation, sampling distribution, estimator properties, hypothesis types, and estimation methods.

> **In Simple Terms:** This section is the answer key for Unit 2. Cross-check your understanding against these model answers before an exam.

### Key Concepts

#### CYP 1 Model Answers
1. **Parameter vs Statistic**: Parameter = unknown fixed quantity in the population (e.g., µ, σ²); Statistic = estimated mean or variance from a sample; statistic is a function of sample observations.
2. **Point vs Interval Estimate**: Point estimate = specific numerical value from a statistic. Interval estimate = range (T₁, T₂) such that P(T₁ ≤ Ø ≤ T₂) = 1-α; also called confidence interval.
3. **Estimator vs Estimate**: Estimator is the same rule for all samples; estimate varies from sample to sample. The distribution of many point estimates from different samples is the **sampling distribution** of the statistic.
4. **Four properties of good estimator**: (i) Unbiasedness (ii) Consistency (iii) Efficiency (iv) Sufficiency
5. **Two conditions for consistency**: (i) lim_{n→∞}[E(T) - Ø] = 0 AND (ii) lim_{n→∞} Var(T) = 0

#### CYP 2 Model Answers
1. **Simple vs Composite Hypothesis**: Simple = all parameters specified; Composite = one or more not exactly specified
2. **One-tailed vs Two-tailed**: H₁: µ ≠ µ₀ → two-tailed; H₁: µ < µ₀ or H₁: µ > µ₀ → one-tailed (left or right)
3. **Type-I vs Type-II**: Type-I = rejecting true H₀ (α = max allowed prob; usually 1% or 5%); Type-II = accepting false H₀. Type-I is more serious.
4. **OLS principle**: Choose values minimising S = Σeᵢ²; unique solution when normal equations = unknowns
5. **MLE properties**: (a) consistent, efficient, sufficient; (b) not necessarily unbiased (but correctable); (c) approximately normal for large samples; (d) invariant to functional transformation.

### Quick Recall
> **Quick Recall:**
> - WLLN: P(|Aₙ - µ| < α) = 1; SLLN: P(Aₙ = µ) = 1 (both as n→∞)
> - Type-I (worse): reject true H₀; Type-II: accept false H₀
> - MLE: consistent + efficient + sufficient + approx normal + invariant

### Connections
- Confirms: All Unit 2 content (Chunks 003–004)
- Transitions into: Unit 3 Matrix Algebra (below)

---

## Section: Unit 3 Introduction — Why Matrix Algebra 🟡

### Core Idea
Matrix algebra is integral to econometrics because it allows concise representation of many variables and generalisation of results from simple to complex models. Unit 3 revisits matrix concepts from MEC 203 (Quantitative Methods) with emphasis on special matrices relevant to econometric theory.

> **In Simple Terms:** Instead of writing 10 regression equations with 10 variables each, matrix algebra lets you write Y = Xβ + u — one line. That elegance is why matrices matter in econometrics.

### Key Concepts
#### Role of Matrix Algebra in Econometrics
- Compact notation: represents multiple equations in one expression (Y = Xβ + u)
- Facilitates mathematical operations (differentiation, inversion) on systems of equations
- Enables generalisation from small to large variable sets
- Essential for deriving OLS estimator β̂ = (X'X)⁻¹X'y

### Quick Recall
> **Quick Recall:**
> - Matrix algebra compresses multiple regression into Y = Xβ + u
> - Key operation: (X'X)⁻¹X'y = OLS estimator formula

### Connections
- Prerequisite for: OLS estimation in matrix form (Block 2, Unit 4)

---

## Section: Matrix Notation & Basic Types 🔴

### Core Idea
A matrix is a rectangular array of numbers. Key notation: upper-case bold for matrices (A), lower-case bold for vectors (a), lower-case for scalars. The dimension is m × n (rows × columns). Several special matrix types appear repeatedly in econometrics: identity, diagonal, triangular, symmetric, null, and transpose.

> **In Simple Terms:** A matrix is just a table of numbers, organised in rows and columns. Special tables (like the identity matrix) have nice mathematical properties that we exploit in regression derivations.

### Key Concepts

#### Matrix, Vector, Scalar — Definitions
- An m × n matrix A has m rows and n columns; element aᵢⱼ is at row i, column j
- If m = n: **square matrix**
- An n × 1 matrix: **column vector** (a bold lowercase letter, e.g., **a**)
- A 1 × n matrix: **row vector**
- A 1 × 1 matrix: **scalar**

#### Special Matrix Types

| Type | Definition | Symbol |
|------|-----------|--------|
| Diagonal | aᵢⱼ = 0 for i ≠ j, aᵢᵢ ≠ 0 for some i | D |
| Identity | Diagonal with all diagonal elements = 1 | Iₙ |
| Lower-triangular | aᵢⱼ = 0 for i < j | L |
| Upper-triangular | aᵢⱼ = 0 for i > j | U |
| Null (zero) | All elements = 0 | 0 |
| Symmetric | A = A' (transpose equals original) | A |
| Transpose | A' = (aⱼᵢ) — rows and columns swapped | A' or Aᵀ |

### Definitions
- **Matrix**: A rectangular array of numbers; m × n means m rows, n columns. ⭐ (exam-important)
- **Square Matrix**: A matrix where m = n (equal number of rows and columns).
- **Column Vector / Row Vector**: An n×1 or 1×n matrix.
- **Diagonal Matrix**: A matrix where all off-diagonal elements are zero.
- **Identity Matrix (Iₙ)**: A diagonal matrix where all diagonal elements equal 1. ⭐ (exam-important)
- **Lower/Upper Triangular Matrix**: Matrix where elements below/above the main diagonal are zero.
- **Null (Zero) Matrix**: A matrix where all elements are zero.
- **Transpose (A' or Aᵀ)**: Obtained by swapping rows and columns of A; (aᵢⱼ) → (aⱼᵢ).
- **Symmetric Matrix**: A matrix equal to its own transpose: A = A'. ⭐ (exam-important)

### Quick Recall
> **Quick Recall:**
> - Iₙ = n×n identity; diagonal = zeros off-diagonal; symmetric = A = A'
> - Transpose notation: A' or Aᵀ (both used interchangeably in the text)
> - Symmetric matrices have nice properties: orthogonal diagonalisation (Chunk 006: Partitioned Matrices)

### Connections
- Prerequisite for: Matrix multiplication (below), Inverse (below), Rank (below)
- Connects to: OLS normal equations in matrix form (Block 2)

---

## Section: Matrix Multiplication 🔴

### Core Idea
Two matrices A (m × n) and B (p × q) can be multiplied **only if n = p** (inner dimensions match). The result AB is m × q. The (i,j) element of AB is the dot product of the i-th row of A and the j-th column of B. Matrix multiplication is generally **not commutative** (AB ≠ BA in general).

> **In Simple Terms:** For AB to work, A's columns must equal B's rows — like making sure the pieces fit together. The result has A's rows and B's columns. Order matters — flipping A and B usually gives a different answer.

### Key Concepts

#### Conformability Condition
A (m × n) × B (p × q) is defined if and only if **n = p**. Result: (m × q).

#### Properties of Matrix Multiplication
For conformable matrices A, B, C and scalar λ:
- (AB)C = A(BC) — **Associativity** ✓
- A(B + C) = AB + AC — **Distributivity** ✓
- AB ≠ BA in general — **Not commutative** ✗
- (AB)' = B'A' — **Transpose of product reverses order** ⭐
- If AB = BA, A and B are said to **commute**

### Definitions
- **Conformable Matrices**: Two matrices where the inner dimensions match for multiplication (columns of A = rows of B). ⭐ (exam-important)
- **Pre-multiplication**: Multiplying from the left (BA); **Post-multiplication**: multiplying from the right (AB) — results differ.

### ⚠️ Common Mistakes
- ❌ Mistake: Assuming AB = BA for all matrices → ✅ Correct: Matrix multiplication is generally NOT commutative
- ❌ Mistake: Confusing (AB)' = A'B' → ✅ Correct: (AB)' = **B'A'** — order reverses

### Quick Recall
> **Quick Recall:**
> - AB defined when: cols(A) = rows(B); result is m×q
> - (AB)' = B'A' — reversal rule ⭐
> - AB ≠ BA (not commutative, in general)

### Connections
- Prerequisite for: Determinants, Inverse, OLS β̂ = (X'X)⁻¹X'y

---

## Section: Determinants, Orthogonal Matrices & Trace 🔴

### Core Idea
The determinant of a square matrix is a scalar that encodes whether the matrix is invertible (non-zero det → invertible). An orthogonal matrix preserves lengths and angles (A'A = I). The trace is the sum of diagonal elements and equals the sum of eigenvalues. These three properties are fundamental to understanding invertibility, orthogonality, and eigenvalue theory in econometrics.

> **In Simple Terms:** The determinant tells you whether the matrix is "usable" (non-zero = invertible). The trace is just the sum of diagonal numbers. Orthogonal matrices are "rotation" matrices that don't distort shapes.

### Key Concepts

#### Determinant
- det(A) ≠ 0 ↔ A is **non-singular** (invertible)
- det(A) = 0 ↔ A is **singular** (not invertible)
- det(AB) = det(A) × det(B)
- det(A') = det(A)
- det(I) = 1
- det(λA) = λⁿ det(A) for n×n matrix

#### Orthogonal Matrix
A matrix A is orthogonal if **A'A = AA' = I** (i.e., A' = A⁻¹).
Key property: **det(A'A) = [det(A)]² = det(I) = 1**, so det(A) = ±1.

#### Trace of a Matrix
**trace(A) = tr(A) = Σ aᵢᵢ** (sum of diagonal elements)

Properties:
- tr(A + B) = tr(A) + tr(B)
- tr(λA + μB) = λtr(A) + μtr(B)
- tr(A) = tr(A')
- tr(AA') = tr(A'A) = Σᵢⱼ aᵢⱼ²
- **tr(In) = n**

### Definitions
- **Determinant**: A scalar value encoding the invertibility of a square matrix; det(A) ≠ 0 ↔ A is invertible. ⭐ (exam-important)
- **Singular Matrix**: A square matrix with det(A) = 0; cannot be inverted. ⭐ (exam-important)
- **Non-Singular Matrix**: A square matrix with det(A) ≠ 0; invertible. ⭐ (exam-important)
- **Orthogonal Matrix**: A matrix where A'A = I (transpose = inverse); det(A) = ±1. ⭐ (exam-important)
- **Trace**: tr(A) = Σ aᵢᵢ; sum of diagonal elements; equals sum of eigenvalues. ⭐ (exam-important)

### Quick Recall
> **Quick Recall:**
> - det(A) ≠ 0 → invertible; det(A) = 0 → singular (cannot invert)
> - Orthogonal: A'A = I → det(A) = ±1
> - trace(A) = Σ diagonal elements = Σ eigenvalues (see Chunk 006)

### Connections
- Is prerequisite for: Inverse (below), Rank (below), Eigenvalues (Chunk 006: Partitioned Matrices)
- Connects to: Idempotent matrix trace = rank (Chunk 006: Partitioned Matrices)

---

## Section: Inverse of a Matrix 🔴

### Core Idea
The inverse A⁻¹ of a non-singular square matrix A satisfies AA⁻¹ = A⁻¹A = I. Only non-singular matrices (det ≠ 0) are invertible. The inverse is computed using the adjoint (adjugate) matrix: A⁻¹ = (1/det(A)) × adj(A). The OLS estimator β̂ = (X'X)⁻¹X'y requires (X'X) to be invertible — i.e., non-singular.

> **In Simple Terms:** The inverse is the matrix equivalent of "dividing by A." Just like 5 × (1/5) = 1, A × A⁻¹ = I. But you can only divide by a non-singular matrix — singular matrices are like dividing by zero.

### Key Concepts

#### Conditions for Invertibility
Matrix A is invertible ↔ det(A) ≠ 0 ↔ A is non-singular ↔ A has full rank.
A singular matrix **cannot be inverted**.

#### Computing the Inverse — Cofactor/Adjoint Method
For A = [[a₁₁, a₁₂], [a₂₁, a₂₂]] (2×2 case):
A⁻¹ = (1/(a₁₁a₂₂ - a₁₂a₂₁)) × [[a₂₂, -a₁₂], [-a₂₁, a₁₁]]

General formula for n×n:
1. Compute det(A)
2. Compute the cofactor matrix (each cᵢⱼ = (-1)^{i+j} × det(Aᵢⱼ))
3. Adjoint = transpose of cofactor matrix
4. **A⁻¹ = (1/det(A)) × adj(A)** ⭐

#### CYP Worked Example (3×3 Inverse)
For A = [[2,4,1],[4,3,7],[2,1,3]]:
- det(A) = 10 (computed via cofactor expansion along row 2)
- Cofactor matrix = [[2,2,-2],[-11,4,6],[25,-10,-10]]
- adj(A) = (cofactor matrix)ᵀ = [[2,-11,25],[2,4,-10],[-2,6,-10]]
- A⁻¹ = (1/10) × adj(A)

#### Properties of the Inverse
- (λA)⁻¹ = (1/λ)A⁻¹ for scalar λ ≠ 0
- (A⁻¹)⁻¹ = A
- (A⁻¹)' = (A')⁻¹ — inverse and transpose commute
- (AB)⁻¹ = B⁻¹A⁻¹ — **order reverses**
- For diagonal A: diagonal elements of A⁻¹ are 1/aᵢᵢ

### Definitions
- **Inverse of a Matrix (A⁻¹)**: Unique matrix satisfying AA⁻¹ = A⁻¹A = I; exists only for non-singular matrices. ⭐ (exam-important)
- **Adjoint (Adjugate) Matrix**: Transpose of the cofactor matrix of A; used in computing A⁻¹.
- **Cofactor Cᵢⱼ**: (-1)^{i+j} × det(Aᵢⱼ) where Aᵢⱼ is the submatrix obtained by deleting row i and column j.

### ⚠️ Common Mistakes
- ❌ Mistake: (AB)⁻¹ = A⁻¹B⁻¹ → ✅ Correct: **(AB)⁻¹ = B⁻¹A⁻¹** — order reverses (same reversal as transpose)
- ❌ Mistake: Attempting to invert a singular matrix → ✅ Correct: Singular matrices have no inverse

### Quick Recall
> **Quick Recall:**
> - A⁻¹ = (1/det(A)) × adj(A); requires det(A) ≠ 0
> - (AB)⁻¹ = B⁻¹A⁻¹ (reversal rule) ⭐
> - In OLS: β̂ = (X'X)⁻¹X'y — requires (X'X) to be invertible

### Connections
- Builds on: Determinants (above)
- Is prerequisite for: Rank (below), Partitioned Matrices (Chunk 006: Partitioned Matrices), OLS estimator derivation (Block 2)

---

## Section: Rank of a Matrix 🔴

### Core Idea
The rank of a matrix is the maximum number of linearly independent rows (or columns). Rank determines whether a system of equations has a unique solution — and whether the OLS estimator β̂ = (X'X)⁻¹X'y can be computed (requires X to have full column rank). Rank is found by reducing the matrix to row echelon form and counting non-zero rows.

> **In Simple Terms:** Rank counts how many "genuinely different" rows a matrix has. If two rows are just multiples of each other, they don't add new information — they're linearly dependent. Only independent rows count toward the rank.

### Key Concepts

#### Row Echelon Form
A matrix is in row echelon form if:
1. All zero rows are at the bottom
2. Each non-zero row has more leading zeros than the row above it
3. Operations allowed: scalar multiplication of rows, addition/subtraction of rows

#### Rank via Row Reduction
Rank = number of non-zero rows in row echelon form = number of **pivot** positions.

**CYP Worked Example**: For A = [[3,0,2,2],[-6,42,24,54],[21,-21,0,-15]]:
- After R₂ → R₂ + 2R₁, R₃ → R₃ - 7R₁, then R₃ → R₃ + (1/2)R₂:
- Result: [[3,0,2,2],[0,42,28,58],[0,0,0,0]]
- 2 non-zero rows → **rank = 2**

#### Key Rank Properties
- rank(A) = 0 ↔ A = 0
- rank(Iₙ) = n
- rank(λA) = rank(A) for λ ≠ 0
- rank(diagonal) = number of non-zero diagonal elements
- rank(A + B) ≤ rank(A) + rank(B)
- rank(AB) ≤ min(rank A, rank B)
- For m×n matrix: rank(A) ≤ min{m, n}
- For n×n matrix: A⁻¹ exists ↔ rank(A) = n (full rank)

### Definitions
- **Rank of a Matrix**: Maximum number of linearly independent rows (= maximum linearly independent columns) in the matrix. ⭐ (exam-important)
- **Row Echelon Form**: A matrix form where all zero rows are at bottom and each non-zero row has strictly more leading zeros than the row above.
- **Linearly Independent Rows**: Rows where no row can be expressed as a linear combination of the others.
- **Full Rank**: For an n×n matrix, rank = n; matrix is invertible. For X (n×k), full column rank = rank k; required for OLS.

### ⚠️ Common Mistakes
- ❌ Mistake: rank of A ≠ rank of A' → ✅ Correct: rank(A) = rank(A') always
- ❌ Mistake: Thinking square matrix = full rank automatically → ✅ Correct: A square matrix can be rank-deficient (singular)

### Quick Recall
> **Quick Recall:**
> - Rank = non-zero rows in row echelon form = number of pivots
> - Full rank (n×n): rank = n ↔ invertible ↔ det ≠ 0
> - X must have full column rank (rank k) for OLS to work
> - rank(AB) ≤ min(rank A, rank B)

### Connections
- Builds on: Determinants and Inverse (above)
- Continues into: Properties verified for M-matrix (Chunk 006: Partitioned Matrices)
- Connects to: Multicollinearity in regression — X rank-deficient when variables are perfectly collinear (Block 3)


---

<!-- Continues from: Rank of a Matrix (Chunk 005: Unit 2 CYP Answers (Self-Check)) -->
<!-- Continues into: Kronecker Product, Vec-Operator, Matrix Differentiation, CYP Answers (Chunk 007: Kronecker Product & Vec-Operator) -->

## Section: Partitioned Matrices 🟡

### Core Idea
A partitioned matrix is a matrix divided into submatrices (blocks). Partition allows complex matrix operations to be broken into smaller, manageable block operations. In econometrics, partitioned matrices appear in simultaneous equations systems (e.g., Keynesian model: AX = B) and in block-diagonal covariance structures.

> **In Simple Terms:** Partitioning a matrix is like organising a big spreadsheet by dividing it into groups. You can then do operations on each group separately, which is much easier than working with the whole thing at once.

### Key Concepts

#### Block Matrix Structure
Y = [[A, B], [C, D]] where A, B, C, D are submatrices.
Dimension rules:
- A and B have the same number of rows (m)
- C and D have the same number of rows (n)
- A and C have the same number of columns (p)
- B and D have the same number of columns (q)
- Y has dimension (m+n) × (p+q)

#### Block Multiplication
If Y₁ = [[A₁,B₁],[C₁,D₁]] and Y₂ = [[A₂,B₂],[C₂,D₂]] are conformable:
Y₁Y₂ = [[A₁A₂+B₁C₂, A₁B₂+B₁D₂], [C₁A₂+D₁C₂, C₁B₂+D₁D₂]]

#### Direct Sum (A ⊕ B)
A ⊕ B = [[A, 0], [0, B]] — a block-diagonal matrix. A block-diagonal matrix is the direct sum of its blocks.

#### Inversion of Block Diagonal
If A and D are non-singular:
[[A,0],[0,D]]⁻¹ = [[A⁻¹,0],[0,D⁻¹]]

#### Trace of Partitioned Matrix
tr([[A,B],[C,D]]) = tr(A) + tr(D) — only diagonal blocks contribute.

### Definitions
- **Partitioned Matrix**: A matrix divided into submatrices (blocks); allows block-level arithmetic. ⭐ (exam-important)
- **Block-Diagonal Matrix**: A square partitioned matrix where all off-diagonal blocks are zero matrices; equals the direct sum of diagonal blocks.
- **Direct Sum (A ⊕ B)**: [[A,0],[0,B]] — creates a block-diagonal matrix from two matrices A and B.

### Examples
**CYP 1 Q1 — Keynesian Model in Matrix Form**:
Y - C = I + G (national income identity)
-bY + C = a (consumption function)

In matrix notation: [[1,-1],[-b,1]] [[Y],[C]] = [[I+G],[a]]
i.e., AX = B where X = [[Y],[C]]

Solution: X = A⁻¹B = [[Y],[C]] = [[(I+G+a)/(1-b)], [(1+G)b+a)/(1-b)]]

(Using 2×2 inverse formula with det(A) = 1-b)

### Quick Recall
> **Quick Recall:**
> - Partitioned matrix: Y = [[A,B],[C,D]]; Y' = [[A',C'],[B',D']]
> - Block diagonal inverse: [[A,0],[0,D]]⁻¹ = [[A⁻¹,0],[0,D⁻¹]]
> - tr([[A,B],[C,D]]) = tr(A) + tr(D)
> - Direct sum: A ⊕ B = [[A,0],[0,B]]

### Connections
- Builds on: Inverse of a Matrix (Chunk 005: Unit 2 CYP Answers (Self-Check))
- Connects to: Block structures in simultaneous equations (Block 4, Unit 16)

---

## Section: Eigenvalues and Eigenvectors 🔴

### Core Idea
For a square matrix A, an eigenvalue λ and eigenvector x satisfy Ax = λx — the matrix "scales" the eigenvector by λ without changing its direction. Eigenvalues and eigenvectors allow a matrix to be diagonalised (A = CΛC⁻¹), which simplifies complex matrix operations. Two key relationships: trace(A) = Σλᵢ and det(A) = Πλᵢ, linking eigenvalues to the trace and determinant.

> **In Simple Terms:** Eigenvectors are the "special directions" of a matrix — they don't change direction when the matrix is applied, they just get scaled by the eigenvalue. Finding these special directions makes matrix computations much simpler.

### Key Concepts

#### Characteristic Equation and Eigenvalues
Eigenvalue equation: **Ax = λx** → **(A - λI)x = 0**
Non-trivial solutions exist when: **det(A - λI) = 0** (characteristic equation)
For an n×n matrix: characteristic equation is an nth-degree polynomial → at most n eigenvalues.

**Worked Example (2×2 matrix B = [[2,5],[2,3]])**:
det(B - λI) = det([[2-λ, 5],[2, 3-λ]]) = (2-λ)(3-λ) - 10
= λ² - 5λ + 6 - 10 = λ² - 5λ - 4 = 0
Factoring: (λ-1)(λ-4) = 0 → eigenvalues: **λ = 1 or λ = 4**

#### Eigenvectors and Eigenspaces
For each eigenvalue λ, the corresponding eigenvectors are found by solving (A - λI)x = 0.
Multiple eigenvectors for the same λ form the **eigenspace** — a subspace closed under scalar multiplication and vector addition.

#### Diagonalisation: A = CΛC⁻¹
If A (n×n) has n linearly independent eigenvectors x₁,...,xₙ:
- C = [x₁,...,xₙ] (matrix of eigenvectors)
- Λ = diag(λ₁,...,λₙ) (diagonal matrix of eigenvalues)
- **AT = TΛ** → **C⁻¹AC = Λ** → **A = CΛC⁻¹**

A is **diagonalizable** if it has n linearly independent eigenvectors.

#### Key Relationships
- **trace(A) = trace(Λ) = Σλᵢ** (sum of eigenvalues = trace)
- **det(A) = det(Λ) = Πλᵢ** (product of eigenvalues = determinant)
- Eigenvalues of A⁻¹ = reciprocals of eigenvalues of A (1/λᵢ)
- Eigenvalues of A² = squares of eigenvalues of A (λᵢ²)
- Eigenvectors of A⁻¹, A², Aᵏ are the **same** as those of A

### Definitions
- **Eigenvalue (λ)**: A scalar satisfying Ax = λx for some non-zero x; root of the characteristic equation det(A - λI) = 0. ⭐ (exam-important)
- **Eigenvector**: A non-zero vector x such that Ax = λx for some eigenvalue λ. ⭐ (exam-important)
- **Characteristic Equation**: det(A - λI) = 0; an nth-degree polynomial whose roots are the eigenvalues of A. ⭐ (exam-important)
- **Eigenspace**: The set of all eigenvectors corresponding to a particular eigenvalue λ, plus the zero vector; forms a subspace.
- **Diagonalizable Matrix**: A matrix A that can be written as A = CΛC⁻¹ where C is a matrix of eigenvectors and Λ is diagonal; possible if A has n linearly independent eigenvectors.

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking all matrices are diagonalizable → ✅ Correct: Only matrices with n linearly independent eigenvectors are diagonalizable
- ❌ Mistake: Computing eigenvalues of A² separately → ✅ Correct: Eigenvalues of A² = (eigenvalues of A)², eigenvectors are the same

### Quick Recall
> **Quick Recall:**
> - Eigenvalue equation: (A - λI)x = 0 → det(A - λI) = 0 → characteristic equation
> - trace(A) = Σλᵢ; det(A) = Πλᵢ ⭐
> - A = CΛC⁻¹ (diagonalisation) → simplifies Aᵏ = CΛᵏC⁻¹
> - A⁻¹ has eigenvalues 1/λᵢ with the same eigenvectors

### Connections
- Builds on: Determinants and Trace (Chunk 005: Unit 2 CYP Answers (Self-Check))
- Is prerequisite for: Symmetric matrices (below), Idempotent matrices (below)
- Connects to: Variance-covariance matrices (positive definite) in OLS

---

## Section: Special Matrices — Symmetric, Positive Definite, PSD 🔴

### Core Idea
For symmetric matrices, all eigenvalues are real and eigenvectors corresponding to distinct eigenvalues are orthogonal. This enables orthogonal diagonalisation (C'AC = Λ where C is orthogonal). A positive definite (PD) matrix has all eigenvalues strictly positive, guaranteeing invertibility. A positive semi-definite (PSD) matrix has all eigenvalues ≥ 0. PD matrices appear in variance-covariance matrices, ensuring valid statistical inference.

> **In Simple Terms:** Symmetric matrices are "nice" — their eigenvectors always point at right angles to each other. Positive definite means all eigenvalues are positive — like checking all springs in a machine are under tension. If any spring has zero or negative tension, the system may be unstable (or non-invertible).

### Key Concepts

#### Symmetric Matrices and Orthogonal Diagonalization
For symmetric A: eigenvectors for distinct eigenvalues are **orthogonal** (C₂'C₁ = 0).
This means symmetric A is **orthogonally diagonalizable**:
**C'AC = Λ** where C is an orthogonal matrix (C'C = I) and Λ = diag(eigenvalues)
Equivalently: **A = CΛC'**

Key consequences:
- rank(A) = rank(Λ) = number of non-zero eigenvalues of A
- det(A) = Πλᵢ; trace(A) = Σλᵢ for symmetric A (same as general case)
- Rank is preserved under non-singular and orthogonal transformations

#### Positive Definite (PD) Matrix
A symmetric matrix A is **positive definite** if **b'Ab > 0** for all vectors b ≠ 0.

Equivalent condition: A is PD ↔ **all eigenvalues are strictly positive (λᵢ > 0)**.
- PD matrices are always non-singular (invertible).
- Variance-covariance matrices are positive definite.

#### Positive Semi-Definite (PSD) Matrix
A symmetric matrix A is **positive semi-definite** if **b'Ab ≥ 0** for all b ≠ 0.

Equivalent condition: A is PSD ↔ **all eigenvalues are non-negative (λᵢ ≥ 0)**.
- PSD matrices may be singular.

| Property | Condition | Eigenvalues | Invertible? |
|----------|-----------|-------------|------------|
| Positive Definite (PD) | b'Ab > 0 | All λᵢ > 0 | Yes |
| Positive Semi-Definite (PSD) | b'Ab ≥ 0 | All λᵢ ≥ 0 | Maybe |

#### Matrix Square Root and Cholesky Decomposition
For symmetric PD matrix A: A^{1/2} exists where (A^{1/2})(A^{1/2}) = A
By orthogonal diagonalisation: **A^{-1/2} = CΛ^{-1/2}C'** and **A^{1/2} = CΛ^{1/2}C'**
Square root of PSD matrix can be found using **Cholesky Decomposition**: A = LL' where L is lower triangular.

Given two symmetric PD matrices A and B: if A-B is PSD, then B⁻¹ - A⁻¹ is also PSD.

### Definitions
- **Symmetric Matrix**: A = A'; all eigenvalues are real; eigenvectors for distinct eigenvalues are orthogonal. ⭐ (exam-important)
- **Positive Definite (PD) Matrix**: Symmetric matrix where b'Ab > 0 for all b ≠ 0; all eigenvalues strictly positive; always invertible. ⭐ (exam-important)
- **Positive Semi-Definite (PSD) Matrix**: Symmetric matrix where b'Ab ≥ 0 for all b ≠ 0; all eigenvalues non-negative; may be singular. ⭐ (exam-important)
- **Cholesky Decomposition**: Factorisation of a symmetric PSD matrix as A = LL' where L is lower triangular; used to compute matrix square roots.
- **Matrix Square Root (A^{1/2})**: Matrix such that A^{1/2} × A^{1/2} = A; exists for symmetric PSD matrices.

### Quick Recall
> **Quick Recall:**
> - Symmetric: real eigenvalues; orthogonal eigenvectors for distinct λ; C'AC = Λ, A = CΛC'
> - PD: b'Ab > 0 ↔ all λᵢ > 0 → always invertible ⭐
> - PSD: b'Ab ≥ 0 ↔ all λᵢ ≥ 0 → may be singular
> - Variance-covariance matrix is always PD (in regular cases)

### Connections
- Builds on: Eigenvalues (above), Orthogonal matrices (Chunk 005: Unit 2 CYP Answers (Self-Check))
- Is prerequisite for: Idempotent matrix (below), Fisher Information Matrix (Chunk 007: Kronecker Product & Vec-Operator)
- Connects to: Gauss-Markov theorem — variance of OLS estimator involves PD matrix (Block 2)

---

## Section: QR Factorization 🟡

### Core Idea
QR factorisation decomposes a real m×n matrix A (of rank n) into A = QR, where Q is a semi-orthogonal matrix (Q'Q = Iₙ) and R is a n×n upper triangular matrix with positive diagonal elements. The columns q₁, q₂,...,qₙ of Q form an orthonormal basis obtained by the Gram-Schmidt process.

> **In Simple Terms:** QR breaks a matrix into a "rotation part" (Q) and a "scaling/triangular part" (R). This decomposition is used in numerical computing to solve least squares problems stably.

### Key Concepts

#### QR Decomposition: A = QR
- A: real m×n matrix with rank n (n ≤ m)
- Q: m×n semi-orthogonal matrix (Q'Q = Iₙ, note: NOT QQ' = I unless m=n)
- R: n×n upper triangular matrix with positive diagonal elements
- Columns of Q: q₁,...,qₙ computed by **Gram-Schmidt orthogonalisation** of columns of A

### Definitions
- **Semi-Orthogonal Matrix (Q)**: A real matrix satisfying Q'Q = Iₙ; columns form an orthonormal set.
- **Upper Triangular Matrix (R)**: Matrix where all elements below the main diagonal are zero.
- **Gram-Schmidt Process**: An algorithm to produce an orthonormal set of vectors from a set of linearly independent vectors.

### Quick Recall
> **Quick Recall:**
> - QR: A = QR where Q'Q = Iₙ (semi-orthogonal) and R upper triangular
> - Gram-Schmidt orthogonalisation produces the columns of Q
> - Used for numerical stability in OLS computation

### Connections
- Builds on: Orthogonal matrices (Chunk 005: Unit 2 CYP Answers (Self-Check)), Rank (Chunk 005: Unit 2 CYP Answers (Self-Check))
- Connects to: Numerically stable OLS computation (Block 2)

---

## Section: Singular Value Decomposition (SVD) 🟡

### Core Idea
SVD generalises eigendecomposition to non-square matrices. Any real m×n matrix A of rank r can be written as A = SΛ^{1/2}T', where S and T are orthogonal matrices of left/right singular vectors and Λ is diagonal with positive elements (squared singular values). SVD is used for computing Moore-Penrose pseudoinverses and dimensionality reduction.

> **In Simple Terms:** SVD is like eigendecomposition, but it works for any matrix — even rectangular ones. It reveals the fundamental "shapes" of a transformation.

### Key Concepts
#### SVD: A = SΛ^{1/2}T'
- A: real m×n matrix with rank r > 0
- S: m×r matrix with S'S = Iᵣ (left singular vectors)
- T: n×r matrix with T'T = Iᵣ (right singular vectors)
- Λ: r×r diagonal matrix with positive diagonal elements (eigenvalues of AA')
- Finding S and T: AA'S = SΛ; T = A'SΛ^{-1/2}

### Definitions
- **Singular Value Decomposition (SVD)**: Factorisation A = SΛ^{1/2}T' for any m×n matrix; S and T are orthogonal, Λ diagonal with singular values.
- **Singular Values**: Square roots of eigenvalues of AA'; represent "scaling factors" in the SVD.

### Quick Recall
> **Quick Recall:**
> - SVD: A = SΛ^{1/2}T'; works for any m×n matrix (unlike eigendecomposition)
> - S'S = Iᵣ, T'T = Iᵣ; Λ = diag(singular values squared)

### Connections
- Builds on: Eigenvalues (above), Symmetric PD matrices (above)
- Connects to: Ridge regression, principal component analysis (advanced topics, MECE 102)

---

## Section: Idempotent Matrix 🔴

### Core Idea
A matrix M is idempotent if MM = M. Idempotent matrices appear naturally in OLS: the hat matrix H = X(X'X)⁻¹X' and the annihilator matrix M = I - H = I - X(X'X)⁻¹X' are both idempotent. The rank of an idempotent matrix equals its trace. M satisfies MX = 0, meaning it projects residuals orthogonal to the column space of X.

> **In Simple Terms:** An idempotent matrix "does it once and stays done." Applying it a second time gives the same result: MM = M. In regression, M projects the data onto the residual space — applying it twice is the same as applying it once.

### Key Concepts

#### Definition: MM = M
A matrix M is idempotent if and only if **M² = M**.

#### Key Property: rank(M) = trace(M)
For idempotent matrix M:
**rank(M) = trace(M)** ⭐ (unique to idempotent matrices!)

#### The M-Matrix (Annihilator) and H-Matrix (Hat)
**Hat matrix**: H = X(X'X)⁻¹X'
**Annihilator matrix**: M = Iₙ - X(X'X)⁻¹X' = I - H

CYP 2 Q2 proves these properties for M:

**Symmetry of M** (M = M'):
Since X(X'X)⁻¹X' is symmetric, M = I - X(X'X)⁻¹X' is also symmetric.

**Idempotency of M** (MM = M):
MM = (I - X(X'X)⁻¹X')(I - X(X'X)⁻¹X')
= I - X(X'X)⁻¹X' - X(X'X)⁻¹X' + X(X'X)⁻¹X'X(X'X)⁻¹X'
= I - X(X'X)⁻¹X' - X(X'X)⁻¹X' + X(X'X)⁻¹X'  [since X'X(X'X)⁻¹ = I]
= I - X(X'X)⁻¹X' = M ✓

**MX = 0** (M annihilates X):
MX = (I - X(X'X)⁻¹X')X = X - X(X'X)⁻¹X'X = X - X = **0** ✓

**Rank of M**:
rank(M) = trace(M) = tr(I - X(X'X)⁻¹X') = tr(Iₙ) - tr(X(X'X)⁻¹X')
= n - tr(X'X(X'X)⁻¹) = n - tr(Iₖ) = **n - k** ✓

(where k = number of parameters estimated)

### Definitions
- **Idempotent Matrix**: A matrix M where M² = MM = M. ⭐ (exam-important)
- **Annihilator Matrix (M)**: M = Iₙ - X(X'X)⁻¹X'; idempotent and symmetric; projects onto orthogonal complement of column space of X; MX = 0. ⭐ (exam-important)
- **Hat Matrix (H)**: H = X(X'X)⁻¹X'; idempotent and symmetric; projects Y onto fitted values Ŷ = HY. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Thinking rank(M) = n for the M-matrix → ✅ Correct: rank(M) = n - k (n observations minus k parameters)
- ❌ Mistake: Forgetting that rank(idempotent) = trace(idempotent) → ✅ Correct: This is the defining trick for idempotent matrices

### Quick Recall
> **Quick Recall:**
> - Idempotent: MM = M ⭐
> - rank(M) = trace(M) for idempotent M ⭐
> - M = I - X(X'X)⁻¹X': symmetric, idempotent, MX = 0, rank = n-k
> - H = X(X'X)⁻¹X': symmetric, idempotent, HX = X, rank = k

### Connections
- Builds on: Matrix inverse (Chunk 005: Unit 2 CYP Answers (Self-Check)), Symmetric matrices (above)
- Is prerequisite for: OLS residuals ê = MY (Block 2), Degrees of freedom in regression
- Continues into: CYP 2 Q2(b) proof of MX=0, Q2(c) rank computation (Chunk 007: Kronecker Product & Vec-Operator)


---

<!-- Continues from: Idempotent Matrix / SVD (Chunk 006: Partitioned Matrices) -->
<!-- Continues into: N/A (final chunk) -->

## Section: Kronecker Product & Vec-Operator 🟡

### Core Idea
The Kronecker product (A ⊗ B) and the vec-operator together form a powerful framework for vectorising matrix equations. The key identity vec(ABC) = (C' ⊗ A)vec(B) allows complex matrix derivatives to be expressed as standard linear operations. These tools appear in multivariate regression, GLS, and SUR models.

> **In Simple Terms:** The Kronecker product creates a "big matrix" by replacing each element of A with that element times the whole matrix B. The vec-operator stacks the columns of a matrix into one long vector. Together, they let you write complicated matrix equations as standard matrix multiplications.

### Key Concepts

#### Kronecker Product (A ⊗ B)
For matrix A (m×n) and B (p×q), the Kronecker product A ⊗ B is the mp × nq block matrix:

A ⊗ B = [[a₁₁B, a₁₂B, ..., a₁ₙB],
          [a₂₁B, a₂₂B, ..., a₂ₙB],
          [...                    ],
          [aₘ₁B, aₘ₂B, ..., aₘₙB]]

In other words, each element aᵢⱼ of A is replaced by the block aᵢⱼB.

#### Vec-Operator (Vectorisation)
For a matrix A with columns a₁, a₂, ..., aₙ:
**vec(A) = [a₁', a₂', ..., aₙ']'** — stacks columns of A into a single column vector.

**Key identity** (from CYP 3 Q1 proof):
**vec(ab') = b ⊗ a** for vectors a and b.
More generally: **vec(ABC) = (C' ⊗ A) vec(B)** ⭐

**Proof sketch from source**:
Let B = Σ bᵢeᵢ' (B expressed as sum of outer products).
Then vec(ABC) = Σ vec(Abᵢeᵢ'C)
Since vec(ab') = b ⊗ a:
vec(ABCᵢ) = (C'eᵢ) ⊗ (Abᵢ) = (C' ⊗ A)(eᵢ ⊗ bᵢ) = (C' ⊗ A)vec(bᵢeᵢ')
Therefore: vec(ABC) = (C' ⊗ A) vec(B) ✓

### Definitions
- **Kronecker Product (A ⊗ B)**: Block matrix where each element aᵢⱼ of A is replaced by the submatrix aᵢⱼB; dimension: (mp) × (nq). ⭐ (exam-important)
- **Vec-Operator**: An operator that stacks the columns of a matrix into a single column vector; vec(A) = [a₁', a₂', ..., aₙ']'. ⭐ (exam-important)

### Mechanisms / Processes
**Key vec identity**: vec(ABC) = (C' ⊗ A) vec(B)
Special cases:
- vec(AB) = (B' ⊗ I) vec(A) = (I ⊗ A) vec(B)
- vec(ab') = b ⊗ a for column vectors a and b

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing A ⊗ B with B ⊗ A → ✅ Correct: Kronecker product is NOT commutative; A ⊗ B ≠ B ⊗ A in general

### Quick Recall
> **Quick Recall:**
> - Kronecker: A ⊗ B replaces each aᵢⱼ with the block aᵢⱼB; dimension mp×nq
> - vec(A): stacks columns of A into one column vector
> - **vec(ABC) = (C' ⊗ A) vec(B)** ⭐ — the key identity
> - vec(ab') = b ⊗ a

### Connections
- Builds on: Matrix multiplication (Chunk 005: Unit 2 CYP Answers (Self-Check))
- Connects to: SUR (Seemingly Unrelated Regressions) and GLS (advanced topics)

---

## Section: Matrix Differentiation — Jacobian, Gradient & Hessian 🔴

### Core Idea
Matrix differentiation extends scalar calculus to matrices. Three key matrices arise: (1) the Jacobian — derivative of a vector function w.r.t. a vector; (2) the Gradient — first derivatives of a scalar function (used as score function in MLE); (3) the Hessian — second derivatives of a scalar function (used to verify maxima in MLE). The Fisher Information Matrix I(θ) is the expected negative Hessian of the log-likelihood, quantifying the information about θ in the data.

> **In Simple Terms:** When a function takes a vector input and gives a scalar output (like log-likelihood), the Gradient tells you which direction is "uphill" (how to increase the function), and the Hessian tells you the curvature (whether you're at a peak or a saddle point). The Fisher Information tells you how precisely you can estimate θ.

### Key Concepts

#### Jacobian Matrix
For a function **f: Rⁿ → Rᵐ** (vector → vector):
The Jacobian J is an m×n matrix of first-order partial derivatives:
Jᵢⱼ = ∂fᵢ/∂xⱼ

The Jacobian generalises the derivative to vector-valued functions.

#### Gradient Matrix (Score Function in MLE)
For a scalar function f: Rⁿ → R (vector → scalar):
The **gradient** is the n×1 vector of first-order partial derivatives:
∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]'

In MLE, the **score function** S(θ) = ∂logL(θ)/∂θ is the gradient of the log-likelihood.

**Worked Example from source** (MLE for Normal distribution — CYP 3 Q2):
Given x₁,...,xₙ i.i.d. from N(µ, σ²), parameter θ = (µ, σ²):

Log-likelihood: logL(θ) = -(n/2)lnσ² - (1/2σ²)Σ(xᵢ - µ)²

Score function S(θ) = ∂logL(θ)/∂θ = [∂lnL/∂µ, ∂lnL/∂σ²]'
= [n/σ²(x̄ - µ), -n/(2σ²) + Σ(xᵢ-µ)²/(2σ⁴)]'

#### Real Hessian Matrix
For scalar function f: Rⁿ → R, the **Hessian** is the n×n matrix of second-order partial derivatives:
Hᵢⱼ = ∂²f/(∂xᵢ∂xⱼ)

The Hessian is symmetric (if f has continuous second-order derivatives).
In MLE: **H = ∂²logL/∂θ∂θ'** — the negative Hessian gives the observed Fisher Information.

#### Fisher Information Matrix I(θ)
**Observed Fisher Information**: I(θ) = -∂²logL/∂θ∂θ'

**Expected Fisher Information**: I(θ) = E_θ[-∂²logL/∂θ∂θ'] = E_θ[S(θ)S(θ)']

The information matrix is a 2×2 variance matrix (for 2-parameter models) and is **positive semi-definite**.

**Worked Example (Fisher Information for Normal)**:
I(θ) = -H = [[n/σ², n/σ⁴(x̄-µ)], [n/σ⁴(x̄-µ), -n/(2σ⁴) + Σ(xᵢ-µ)²/(σ²)³]]

Expected Fisher Information (with E[Σ(xᵢ-µ)²] = nσ²):
I(θ) = [[n/σ², 0], [0, n/(2σ⁴)]]

det(I(θ)) = n²/(2σ⁶) > 0 (since n > 0, σ² > 0) → I(θ) is positive definite.

### Definitions
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

### Quick Recall
> **Quick Recall:**
> - Jacobian: ∂f/∂x (vector-to-vector); Gradient: ∂f/∂x (scalar-to-vector) ⭐
> - Hessian: ∂²f/∂x∂x' (n×n, symmetric) ⭐
> - Score: S(θ) = ∂logL/∂θ = 0 at MLE
> - Fisher Information: I(θ) = -E[Hessian(logL)]; positive semi-definite ⭐
> - For Normal N(µ,σ²): I(θ) = diag(n/σ², n/2σ⁴)

### Connections
- Builds on: Matrix multiplication (Chunk 005: Unit 2 CYP Answers (Self-Check)), MLE (Chunk 004: Asymptotic Properties of Estimators)
- Connects to: Cramér-Rao lower bound (the inverse of Fisher Information gives the minimum variance of any unbiased estimator)
- Connects to: Block 2 — OLS score equations are normal equations

---

## Section: Unit 3 CYP Answers 🟡
<!-- See Chunk 005-006 for content these answers verify -->

### Core Idea
The CYP answers for Unit 3 provide worked solutions for all three Check Your Progress exercises. CYP 1 tests matrix inverse and rank; CYP 2 tests eigenvector diagonalisation and M-matrix properties; CYP 3 tests the vec identity and Fisher Information matrix derivation.

> **In Simple Terms:** These are the answer keys for Unit 3 — use them to verify your matrix algebra and MLE derivations before the exam.

### Key Concepts

#### CYP 1 Answers — Inverse and Rank

**Q1: Inverse of A = [[2,4,1],[4,3,7],[2,1,3]]**
- det(A) = 10 (cofactor expansion along row 2: 4(-11) + 3(4) + 7(6) = -44+12+42 = 10)
- Cofactor matrix: [[2,2,-2],[-11,4,6],[25,-10,-10]]
- adj(A) = (cofactor)ᵀ = [[2,-11,25],[2,4,-10],[-2,6,-10]]
- A⁻¹ = (1/10) × adj(A)

**Q2: Rank of B = [[3,0,2,2],[-6,42,24,54],[21,-21,0,-15]]**
- R₂ → R₂ + 2R₁: [[3,0,2,2],[0,42,28,58],[21,-21,0,-15]]
- R₃ → R₃ - 7R₁: [[3,0,2,2],[0,42,28,58],[0,-21,-14,-29]]
- R₃ → R₃ + (1/2)R₂: [[3,0,2,2],[0,42,28,58],[0,0,0,0]]
- 2 non-zero rows → **rank = 2** ✓

#### CYP 2 Answers — Eigenvectors and M-Matrix

**Q1: Diagonalisation**
If A has n linearly independent eigenvectors x₁,...,xₙ, let T = (x₁,...,xₙ).
AT = (Ax₁,...,Axₙ) = (λ₁x₁,...,λₙxₙ) = TΛ
Since T is non-singular: **T⁻¹AT = Λ** ✓
(Converse: columns of T that satisfy AT = TΛ are eigenvectors of A)

**Q2: M = Iₙ - X(X'X)⁻¹X'**
(a) **Symmetry**: X(X'X)⁻¹X' is symmetric → M = I - X(X'X)⁻¹X' is symmetric
(b) **Idempotency**: MM = (I-H)(I-H) = I - H - H + H² = I - H = M (since H is idempotent: H²=H)
(c) **MX = 0**: MX = (I-H)X = X - X(X'X)⁻¹X'X = X - X = 0 ✓
(d) **rank(M) = n-k**: rank(M) = trace(M) = n - trace(Iₖ) = n - k

**Q3: X'V⁻¹M = 0 (given)**
(a) X'V⁻¹ = X'V⁻¹X(X'X)⁻¹X' → (X'V⁻¹X)⁻¹X'V⁻¹ = (X'X)⁻¹X'
(b) Post-multiply by VX(X'X)⁻¹: (X'V⁻¹X)⁻¹ = (X'X)⁻¹X'VX(X'X)⁻¹

#### CYP 3 Answers — Vec Identity and Fisher Information

**Q1: vec(ABC) = (C' ⊗ A) vec(B)**
(Proof as in Section above — using B = Σbᵢeᵢ' decomposition)

**Q2: Fisher Information for N(µ, σ²)**
logL(θ) = -(n/2)lnσ² - (1/(2σ²))Σ(xᵢ-µ)²

Score function: S(θ) = [n/σ²(x̄-µ), -n/(2σ²) + Σ(xᵢ-µ)²/(2σ⁴)]'

Fisher Information (expected): I(θ) = [[n/σ², 0], [0, n/(2σ⁴)]]

This is positive definite (det > 0) since n > 0 and σ² > 0.

### Quick Recall
> **Quick Recall:**
> - CYP 1: Inverse via cofactor method; Rank via row reduction
> - CYP 2: T⁻¹AT = Λ (diagonalisation); M symmetric, idempotent, MX=0, rank=n-k
> - CYP 3: vec(ABC)=(C'⊗A)vec(B); Fisher I(θ) = diag(n/σ², n/(2σ⁴)) for Normal

### Connections
- Verifies: All content in Chunks 005 and 006
- Closes: Unit 3 (Block 1 is now complete)
- Connects to: MLE Fisher Information → Cramér-Rao bound → efficiency of OLS vs MLE


---

