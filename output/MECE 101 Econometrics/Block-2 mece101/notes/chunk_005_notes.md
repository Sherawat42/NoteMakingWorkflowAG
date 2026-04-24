# Chunk 005 — Multiple Regression: Matrix Form, Classical Assumptions & OLS Derivation
<!-- Pages: 40–49 -->
<!-- Source: chunk_005.txt -->

## Section: Multiple Regression Model — Specification & Advantages 🔴

### Core Idea
Multiple regression models extend bivariate regression to include **two or more explanatory variables** (k variables, one dependent variable). The key advantage is the ability to examine the effect of each independent variable on Y **ceteris paribus** — holding all other variables constant. This enables both theoretical testing and policy evaluation.

> **In Simple Terms:** Instead of asking "how does income affect savings?" multiple regression asks "how does income affect savings, *while controlling* for age, education, and family size?" — giving a cleaner, more realistic answer.

### Key Concepts

#### General Multiple Regression Model
**Yᵢ = β₁ + β₂X₂ᵢ + β₃X₃ᵢ + … + βₖXₖᵢ + uᵢ**, i = 1, 2, …, n ... (6.2)

- β₁ = intercept (X₁ = 1 for all observations by convention)
- β₂, …, βₖ = partial regression coefficients
- uᵢ = stochastic error term

This gives k normal equations when minimizing RSS (one per parameter).

#### Advantages of Multiple Regression (CYP 1 Q1)
1. **Control for multiple factors simultaneously**: Avoids omitted variable bias present in bivariate models.
2. **Ceteris paribus interpretation**: Isolates the effect of one X on Y while holding other X's constant.
3. **Eliminates correlation bias**: Reduces bias from correlation between error term and explanatory variables (common in two-variable models).
4. **General functional form**: Allows flexible specification of cause-effect relationships.
5. **Higher R²**: More explanatory variables → explains more variation in Y.

#### Ceteris Paribus Interpretation
The partial regression coefficient βₖ measures the effect of Xₖ on Y **holding all other X variables constant**. This is impossible in bivariate regression when multiple factors are correlated.

### Definitions
- **Multiple regression model**: A regression model with one dependent variable and two or more independent variables. ⭐ (exam-important)
- **Ceteris paribus**: "All other things being equal" — holding other explanatory variables constant when interpreting one coefficient. ⭐ (exam-important)
- **Partial regression coefficient (βₖ)**: The change in Y per unit change in Xₖ, holding all other X's constant.

### ⚠️ Common Mistakes
- ❌ Mistake: Adding more variables always improves the model → ✅ Correct: More variables always increase R², but may hurt adjusted R² and introduce multicollinearity.

> **Quick Recall:**
> - Multiple regression: Yᵢ = β₁ + β₂X₂ᵢ + … + βₖXₖᵢ + uᵢ
> - β₁ is intercept (X₁ = 1); βₖ is partial coefficient of Xₖ
> - k variables → k normal equations
> - Key advantage: ceteris paribus interpretation

### Connections
- Extends: Bivariate OLS (Chunk 001)
- Simplified by: Matrix algebra (this chunk)

---

## Section: Matrix Representation of Multiple Regression 🔴

### Core Idea
With k variables and n observations, writing individual equations is impractical. Matrix notation **Y = Xβ + U** ... (6.4) compactly represents the entire system. Understanding matrix dimensions is essential — the design matrix X is (n×k), the parameter vector β is (k×1), and the error vector U is (n×1).

> **In Simple Terms:** Matrix notation is the "shorthand" — instead of writing 500 equations, one matrix equation captures all of them at once.

### Key Concepts

#### The Y = Xβ + U Notation

**Y** (n×1): Column vector of dependent variable observations

**X** (n×k): Design matrix — each row is an observation, each column is an explanatory variable; X₁ᵢ = 1 for all i (intercept column)

**β** (k×1): Parameter vector [β₁, β₂, …, βₖ]'

**U** (n×1): Error vector [u₁, u₂, …, uₙ]'

Matrix equation: **Y = Xβ + U** ... (6.4)

#### Matrix Dimensions — Must Memorize

| Matrix | Dimension | Contents |
|--------|-----------|----------|
| Y | n × 1 | Dependent variable values |
| X | n × k | Xᵢⱼ = value of jth regressor at ith obs |
| β | k × 1 | k parameters to be estimated |
| U | n × 1 | Error terms |

Note: Xᵢⱼ = value of the **j**th explanatory variable at the **i**th observation.

### Definitions
- **Design matrix X (n×k)**: Matrix of all explanatory variable values; each row = one observation, each column = one regressor. ⭐ (exam-important)
- **Parameter vector β (k×1)**: Column vector of all regression parameters [β₁, …, βₖ]'. ⭐ (exam-important)
- **Error vector U (n×1)**: Column vector of stochastic error terms.

> **Quick Recall:**
> - Y = Xβ + U (n×1) = (n×k)(k×1) + (n×1) — dimensions check out
> - X is (n×k): n observations, k regressors (including intercept column)
> - β is (k×1), U is (n×1)
> - Always track matrix dimensions!

### Connections
- Builds on: Multiple Regression Specification (this chunk)
- Used in: Classical Assumptions and OLS derivation below

---

## Section: Classical Assumptions for Multiple Regression 🔴

### Core Idea
The four classical assumptions for bivariate regression are extended to matrix form. The key additions are: the variance-covariance structure of U is a **scalar matrix σ²I** (capturing both homoscedasticity and no autocorrelation), and X must have **full rank** (no exact linear relationship between regressors — no perfect multicollinearity).

> **In Simple Terms:** The rules the errors must follow are the same as before, but now stated in matrix language — and we add the rule that no explanatory variable can be an exact combination of others.

### Key Concepts

#### Assumption 1: E(U) = 0 ... (6.5)
E(uᵢ) = 0 for all i — the expected value of each error is zero.

#### Assumption 2: E(UU') = σ²I ... (6.6)
This single matrix assumption captures TWO conditions:
- **Diagonal elements**: E(uᵢ²) = σ² → **homoscedasticity** (constant variance)
- **Off-diagonal elements**: E(uᵢuⱼ) = 0 for i ≠ j → **no autocorrelation**

The variance-covariance matrix of U:

| | u₁ | u₂ | … | uₙ |
|---|---|---|---|---|
| u₁ | σ² | 0 | … | 0 |
| u₂ | 0 | σ² | … | 0 |
| uₙ | 0 | 0 | … | σ² |

= σ²·I (identity matrix scaled by σ²)

#### Assumption 3: X Has Full Rank ... (6.7)
No exact linear relationship among explanatory variables — no perfect **multicollinearity**.

Implication: Rank(X) = k and k < n → **X'X is invertible** → (X'X)⁻¹ exists.

If any column of X is an exact linear combination of other columns → rank drops → X'X is singular → OLS cannot be computed.

#### Assumption 4: E(X'U) = 0 ... (6.8)
No explanatory variable is correlated with the error term. X is **non-stochastic** (fixed in repeated samples). Relaxed in Unit 13 (instrumental variables).

### Definitions
- **Homoscedasticity (matrix form)**: var(uᵢ) = σ² for all i — diagonal elements of E(UU') = σ²I. ⭐ (exam-important)
- **Heteroscedasticity**: var(u₁) ≠ var(u₂) ≠ … ≠ var(uₙ) — non-constant error variance; discussed in Unit 11.
- **No autocorrelation**: E(uᵢuⱼ) = 0 for i ≠ j — off-diagonal elements of E(UU') = 0.
- **Full rank**: Rank(X) = k — all regressors are linearly independent; no perfect multicollinearity. ⭐ (exam-important)
- **Variance-covariance matrix of U**: E(UU') — (n×n) matrix; equals σ²I under CLRM assumptions.

### ⚠️ Common Mistakes
- ❌ Mistake: E(UU') = σ² (scalar) → ✅ Correct: E(UU') = σ²**I** (identity matrix scaled by σ²).
- ❌ Mistake: If X lacks full rank, we can still estimate β → ✅ Correct: (X'X)⁻¹ doesn't exist without full rank → OLS formula breaks down.

> **Quick Recall:**
> - E(U) = 0 → zero mean errors
> - E(UU') = σ²I → homoscedastic + no autocorrelation
> - Full rank X → X'X invertible → OLS exists
> - E(X'U) = 0 → X is exogenous (non-stochastic)

### Connections
- Extends: Five classical assumptions (Chunk 001) to matrix form
- Used in: OLS derivation below, Gauss-Markov proof (Chunk 006)
- Violations: Heteroscedasticity (Unit 11), Autocorrelation (Unit 12), Endogeneity (Unit 13)

---

## Section: OLS Estimation in Matrix Form 🔴
<!-- Continues into: Chunk 006 (Variance of OLS, BLUE proof) -->

### Core Idea
The OLS estimator in matrix form minimizes **RSS = Û'Û** with respect to β̂. Setting the first-order condition to zero yields the **normal equations X'Xβ̂ = X'Y**, which solve to give the OLS estimator **β̂ = (X'X)⁻¹X'Y**. The variance-covariance matrix of β̂ is σ²(X'X)⁻¹.

> **In Simple Terms:** In matrix algebra, the one-line formula β̂ = (X'X)⁻¹X'Y replaces all the messy simultaneous equations — it's the same principle (minimize squared errors) done elegantly.

### Key Concepts

#### Minimizing RSS in Matrix Form
Estimated model: **Ŷ = Xβ̂** ... (6.9)
Residuals: **Û = Y − Xβ̂** ... (6.10)
RSS = **Û'Û** = (Y − Xβ̂)'(Y − Xβ̂) ... (6.11)

Expanding:
**Û'Û = Y'Y − 2β̂'X'Y + β̂'X'Xβ̂** ... (6.12)

#### Normal Equations: X'Xβ̂ = X'Y
Taking derivative of Û'Û w.r.t. β̂ and setting to zero:

∂(Û'Û)/∂β̂ = −2X'Y + 2X'Xβ̂ = 0

→ **X'Xβ̂ = X'Y** ... (6.14) ← **Normal equations (matrix form)**

Note: When differentiating β̂'X'Xβ̂ w.r.t. β̂, we eliminate β̂' (not β̂), giving 2X'Xβ̂.

#### OLS Estimator: β̂ = (X'X)⁻¹X'Y
Pre-multiply normal equations by (X'X)⁻¹:

**β̂ = (X'X)⁻¹X'Y** ... (6.15) ⭐

This requires (X'X)⁻¹ to exist → requires Assumption 3 (full rank of X).

#### Variance of β̂: var(β̂) = σ²(X'X)⁻¹
Proved in Chunk 006. The full variance-covariance matrix of β̂ is a (k×k) matrix.

### Definitions
- **Normal equations (matrix form)**: X'Xβ̂ = X'Y — the k equations obtained by minimizing RSS w.r.t. β̂. ⭐ (exam-important)
- **OLS estimator (matrix form)**: **β̂ = (X'X)⁻¹X'Y** — requires X to have full rank. ⭐ (exam-important)

### Mechanisms / Processes
1. Write RSS = Û'Û = (Y − Xβ̂)'(Y − Xβ̂)
2. Expand to Y'Y − 2β̂'X'Y + β̂'X'Xβ̂
3. Differentiate w.r.t. β̂, set = 0 → −2X'Y + 2X'Xβ̂ = 0
4. Rearrange: X'Xβ̂ = X'Y (normal equations)
5. Pre-multiply by (X'X)⁻¹: β̂ = (X'X)⁻¹X'Y

### Examples
**Example 6.1 (matrix derivative):**
For vectors a and x: ∂(a'x)/∂x = a
Used to show that ∂(β̂'X'Xβ̂)/∂β̂ = 2X'Xβ̂ (not 2β̂'X'X)

### ⚠️ Common Mistakes
- ❌ Mistake: ∂(β̂'X'Xβ̂)/∂β̂ = 2β̂'X'X → ✅ Correct: Result is 2X'Xβ̂ (eliminate β̂', keep β̂)
- ❌ Mistake: β̂ = (X'X)⁻¹X' (missing Y) → ✅ Correct: β̂ = **(X'X)⁻¹X'Y**

> **Quick Recall:**
> - RSS = Û'Û = Y'Y − 2β̂'X'Y + β̂'X'Xβ̂
> - Normal equations: X'Xβ̂ = X'Y
> - OLS formula: **β̂ = (X'X)⁻¹X'Y** ← most important formula
> - var(β̂) = σ²(X'X)⁻¹

### Connections
- Builds on: Matrix representation, Classical Assumptions (this chunk)
- Continues into: Chunk 006 (Variance derivation, BLUE proof)
- CYP 1 Q2 (variance formula), Q4 (why full rank needed)
