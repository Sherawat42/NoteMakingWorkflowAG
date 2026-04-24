# Chunk 002 — Unit 1: Econometric Models, Steps, Specification & Functional Forms
<!-- Pages: 9–18 -->
<!-- Source: chunk_002.txt -->
<!-- Continues from: Unit 1 Objectives (Chunk 001) -->
<!-- Continues into: Software packages, Unit 1 Summary (Chunk 003) -->

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
- Builds on: Scope of Econometrics (Chunk 001)
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
- Connects to: Estimation Methods (Chunk 004)

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
