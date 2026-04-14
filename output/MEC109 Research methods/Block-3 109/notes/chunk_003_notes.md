# Chunk 003 — Functional Forms (Continued) and Classical Normal Regression
<!-- Pages: 20-27 -->
<!-- Source: chunk_003.txt -->
<!-- See chunk 002 for the beginning of Functional Forms section -->

---

## Section: Functional Forms of Regression Model 🔴
<!-- See chunk 002 for Linear and Log-linear models -->

### Core Idea

Continuing from Chunk 002 — in addition to the linear and log-linear models, two more functional forms are commonly used: the **Semi-log model** (for estimating growth rates) and the **Reciprocal model** (for relationships with limiting values). All four forms are linear in parameter, making OLS estimation possible.

> **In Simple Terms:** A semi-log model is like tracking exponential growth on a spreadsheet — as time increases by 1, GDP grows by a fixed *percentage*. A reciprocal model captures the idea of a ceiling or floor — like how infant mortality falls as income rises, but can never go below zero.

### Key Concepts

#### 3. Semi-Log Model (Growth Rate Model)

- **Equation**: log Y = α + βt + U (where t = time)
- Y is in logs; the independent variable (time t) is in absolute terms → **"semi-log"** because only one side is logged
- **Slope β**: Measures the **proportional change** in Y per unit change in t → β measures the **growth rate** of Y
- **Interpretation**: If β = 0.034 → Y grows at approximately **3.4% per year**
- **When to use**: Estimating constant growth rates over time (GDP growth, population growth, money supply growth)

| Model | LHS | RHS | β measures |
|-------|-----|-----|-----------|
| Linear | Y | X | dY/dX = constant slope |
| Log-linear | log Y | log X | Elasticity = %ΔY/%ΔX |
| **Semi-log** | **log Y** | **t (time)** | **Growth rate of Y** |
| Reciprocal | Y | 1/X | Rate of approach to limit |

#### 4. Reciprocal Model

- **Equation**: Y = α + β(1/X) + U
- Non-linear in variable (power of X is −1), but **linear in parameter** → estimable by OLS
- **Key characteristic**: As X → ∞, the term β/X → 0, so Y approaches **α as an asymptote/limit**
- Y has a fixed **upper or lower bound** = α
- **When to use**: When there's a theoretical limit to Y regardless of how large X gets

**Applications:**
1. **Infant mortality vs per capita GNP**: As income rises, child mortality falls — but cannot fall below zero; approaches a lower limit
2. **Phillips Curve**: As unemployment rises, inflation rate falls — but approaches a negative limiting value, not −∞

### Definitions

- **Semi-log Model**: log Y = α + βt + U; β measures the growth rate of Y; used when one variable grows at a constant proportional rate over time. ⭐ (exam-important)
- **Reciprocal Model**: Y = α + β/X + U; Y approaches α as X increases indefinitely (asymptote). Used when there's a theoretical limit. ⭐ (exam-important)
- **Elasticity**: In log-linear model, β = %ΔY / %ΔX = constant throughout; the slope coefficient measures elasticity directly.

### Examples

**Example 9.3 — Log-linear: US Consumer Durables vs Personal Consumption Expenditure (1993-1998):**
- Data: 23 quarterly observations
- Regression: ln(ExpDur) = −9.697 + 1.906 ln(PCExp)
- β̂ = 1.906 → **elasticity > 1** → expenditure on durables is **highly elastic** (luxury good behavior)
- R² = 0.985 → excellent fit

**Example 9.4 — Semi-log: India's GDP Growth (1960-1980):**
- Regression: log GDP = 12.19473 + 0.033729t
- β̂ = 0.034 → **growth rate ≈ 3.4% per year**
- R² = 0.984 → tight fit
- **Interpretation**: Confirms the "Hindu Rate of Growth" (~3.5%) documented in India's 1960s–1970s

**Example: Reciprocal Model — Child Mortality vs Per Capita GNP (64 countries):**
- Regression: Y = 81.944 + (−2723.117)(1/X)
- β̂ = −2723 (negative) → as GNP rises, mortality falls
- α̂ = 81.944 → **asymptotic limit ≈ 82 deaths per 1000 live births** (floor value of infant mortality)
- R² = 0.459 → moderate fit

**Example 9.2 — India's Consumption Function (1980-2001):**
- Linear regression: FCE = −108206.4 + 0.719674 GDP
- β̂ = 0.720 → **MPC ≈ 72%** — for every ₹100 increase in GDP, final consumption rises by ₹72
- R² = 0.998 → almost perfect fit
- t-statistic for β̂ = 91.50 >> critical values (2.845 at 1%, 2.086 at 5%) → relationship is highly significant

### ⚠️ Common Mistakes

- ❌ Mistake: Interpreting Semi-log β as an absolute change → ✅ Correct: β in semi-log = proportional/percentage change in Y, not absolute
- ❌ Mistake: Thinking the reciprocal model's limiting value is β → ✅ Correct: The asymptote/limit is **α** (the intercept); β governs how fast Y approaches that limit

### Edge Cases & Caveats

- The log-linear model's elasticity β is constant throughout the range — real-world elasticities often vary, so this is a simplification
- Semi-log model β approximates growth rate well only for small values of β; for large growth rates, exact formula is (e^β − 1)

> **Quick Recall:**
> - **4 functional forms**: Linear (β = dY/dX), Log-linear (β = elasticity), Semi-log (β = growth rate), Reciprocal (α = limiting value)
> - All 4 are **linear in parameter** → OLS applicable
> - Semi-log: log Y on left, time t on right
> - Reciprocal: Y approaches **α** as X → ∞

### Connections

- Builds on: Log-linear model (Chunk 002)
- Leads to: Classical Normal Regression Model (next section, same chunk)

---

## Section: Classical Normal Regression Model 🔴

### Core Idea

The five classical assumptions (Chunk 001) are sufficient for **estimation** (OLS/BLUE). But for **hypothesis testing**, we also need to know the **probability distribution** of the estimators. This requires a sixth assumption: the disturbance term U follows a **normal distribution**. With this additional assumption, the model is called the **Classical Normal Regression Model (CNRM)**.

> **In Simple Terms:** OLS can fit a line from the data. But to answer "Is this slope statistically significant?" or "Could β = 0 by chance?", we need to know the shape of the distribution of β̂. Assuming U is normally distributed gives us that shape.

### Key Concepts

#### Normality Assumption

The sixth assumption adds: **U is normally distributed** for each given X:
- E(Uᵢ) = 0 for all i (mean zero)
- V(Uᵢ) = σ² for all i (constant variance — homoscedasticity)  
- Cov(Uᵢ, Uⱼ) = 0 for i ≠ j (no autocorrelation)
- All three conditions together: U ~ N(0, σ²) independently and identically distributed

In other words: **U ~ iid N(0, σ²)** — independent, identically, normally distributed.

**Why normality matters:**
1. Since β̂ is a linear function of U (β̂ = ΣkᵢYᵢ = ΣkᵢUᵢ + constants), and U is normal → **β̂ is also normally distributed**
2. This allows standard form hypothesis testing using the t-distribution

#### Connection to Maximum Likelihood Estimation (MLE)

The normality assumption also enables an alternative estimation approach — **Maximum Likelihood Estimation (MLE)**:
- MLE gives **identical estimates** to OLS for β parameters
- However, MLE estimate of σ² is **biased** (divides by n, not by n−2)
- Therefore, OLS + normality is generally preferred over MLE for regression

### Definitions

- **Classical Normal Regression Model (CNRM)**: The classical regression model (5 assumptions) PLUS the normality assumption for U: U ~ N(0, σ²). Required for hypothesis testing. ⭐ (exam-important)
- **iid Normal**: Independent and Identically Distributed Normal — all disturbances follow the same N(0, σ²) distribution independently.

### Mechanisms / Processes

**Why β̂ is normally distributed under CNRM:**
1. U ~ N(0, σ²) (normality assumption)
2. β̂ = ΣkᵢYᵢ = ΣkᵢUᵢ + constants (β̂ is linear in U)
3. Linear combination of normal variables → normal
4. Therefore: **β̂ ~ N(β, σ²/Σx²)**
5. Known mean = β; known variance = σ²/Σx²

### ⚠️ Common Mistakes

- ❌ Mistake: Thinking normality assumption is one of the original 5 → ✅ Correct: Normality is a 6th assumption, added in addition to the 5 classical assumptions, specifically needed for hypothesis testing
- ❌ Mistake: Thinking MLE gives better β estimates → ✅ Correct: OLS and MLE give **identical β estimates** under normality; MLE's σ² estimate is actually biased

> **Quick Recall:**
> - CNRM = 5 classical assumptions + **U ~ N(0, σ²)**
> - Normality allows: β̂ ~ N(β, σ²/Σx²)
> - Needed for: **hypothesis testing using t-distribution**
> - MLE gives same β̂ as OLS but biased σ̂²

### Connections

- Builds on: 5 Classical assumptions (Chunk 001)
- Leads to: Hypothesis Testing (next section, continues in Chunk 004)
- Related to: Maximum Likelihood Estimation (Unit 10 / Chunk 006)

---

## Section: Hypothesis Testing 🔴
<!-- This section continues in chunk 004 -->

### Core Idea

Given the CNRM, we can test whether regression parameters take specific values. The main test is whether the slope β is zero (no relationship between Y and X) or non-zero (significant relationship). The **t-statistic** is used, following a **Student-t distribution** with (n−2) degrees of freedom.

> **In Simple Terms:** Hypothesis testing answers: "Could this slope I estimated (β̂ = 0.72) just be a fluke of sampling, or is there a real relationship?" We use the t-test to decide — if t is very large, the relationship is real.

### Key Concepts

#### Student-t Distribution for Hypothesis Testing

Since σ is unknown (replaced by estimated σ̂), the standardized β̂ follows a **t-distribution** (not normal):

**t-statistic**: t = (β̂ − β₀) / se(β̂) ~ t(n−2)

Where:
- β₀ = value under null hypothesis (usually 0)
- se(β̂) = estimated standard error = σ̂ / √(Σx²)
- n−2 = degrees of freedom

**Decision rule**: If |computed t| > |critical t| → reject H₀

<!-- This section continues in chunk 004 -->

### Connections

- Builds on: Classical Normal Regression Model (this chunk)
- Continues in: Chunk 004 (worked examples of hypothesis tests)

### Open Questions

1. When should we use a one-tailed vs two-tailed t-test?
