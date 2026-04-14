# Chunk 006 — Econometric Problems and Maximum Likelihood Estimation
<!-- Pages: 46-57 -->
<!-- Source: chunk_006.txt -->

---

## Section: Problem of Multi-co-linearity 🔴

### Core Idea

**Multi-co-linearity** occurs when two or more explanatory variables in a regression model have a (near-)exact linear relationship among themselves. This violates the assumption of linearly independent columns in the X matrix. Perfect multicollinearity makes OLS estimation impossible; imperfect multicollinearity makes estimates highly unreliable even if technically computable.

> **In Simple Terms:** Imagine trying to separate the effect of price vs. income on demand — but in your sample, price always rises when income rises. You can't tell whose effect is whose. That's multicollinearity: the variables are "too similar" to be told apart.

### Key Concepts

#### What Causes Multi-co-linearity?

**Perfect multicollinearity example**: If Y = milk demand, X₁ = price of milk, X₂ = family income — but the family produces milk, so as price rises, their income rises proportionally. X₁ and X₂ are perfectly correlated.

In this case:
- The X matrix becomes **singular** (determinant → 0)
- (X'X)⁻¹ doesn't exist
- **Normal equations have no unique solution** → estimation fails

**Imperfect (near) multicollinearity**: X variables are highly (but not perfectly) correlated. OLS estimates exist but are unreliable.

#### Sources of Multicollinearity

- Sample design: researchers may inadvertently select data with correlated Xs
- Model specification: including variables that are linear functions of each other
- Economic structure: many economic variables tend to move together (e.g., income, consumption, wealth)

#### Consequences of Multi-co-linearity (Gujarati's List) ⭐

| # | Consequence |
|---|-------------|
| 1 | **Large variances/SEs** of OLS estimates |
| 2 | **Wider confidence intervals** |
| 3 | **Insignificant t-ratios** for β coefficients (even if R² is high) |
| 4 | **High R² despite few significant t-values** (signature symptom!) |
| 5 | **Instability of OLS estimators**: sensitive to small data changes |
| 6 | **Wrong signs** on some coefficients (e.g., income negatively affects milk demand) |
| 7 | **Individual contributions to ESS cannot be assessed** properly |

#### How to Detect Multi-co-linearity

1. **High R² but few significant t-ratios** — the "classic symptom"
2. **High pairwise correlations** between explanatory variables
3. Partial correlations, auxiliary regressions (subsidiary regressions of each X on others)

#### Multi-co-linearity: Key Nuance

- **OLS still BLUE** even with imperfect multicollinearity — but practically, estimates are unreliable
- The problem is **sample-specific**: variables may not be correlated in the population, but the sample may create correlation
- More data (larger n) can reduce the problem

### Definitions

- **Multi-co-linearity**: Existence of exact or near-exact linear relationships between explanatory variables, vitiating the classical regression model assumption of linearly independent predictors. ⭐ (exam-important)
- **Perfect Multicollinearity**: When one X variable is an exact linear combination of other X variables → X matrix is singular → impossible to estimate OLS.
- **Imperfect Multicollinearity**: High but not perfect correlation between X variables → large SEs, unreliable estimates, wrong signs.

### ⚠️ Common Mistakes

- ❌ Mistake: Multicollinearity means OLS is always invalid → ✅ Correct: **Imperfect** multicollinearity still allows OLS (it's still BLUE), but estimates become imprecise; only *perfect* multicollinearity breaks OLS entirely
- ❌ Mistake: Multicollinearity only exists in the population → ✅ Correct: It is essentially a **sample problem** — X may be independent in population but correlated in the sample

> **Quick Recall:**
> - Multicollinearity = linear relationships among Xs
> - **Signature**: High R², low t-values
> - Perfect → OLS fails (no solution); Imperfect → OLS less reliable
> - Consequences: large SEs, wide CIs, wrong signs, unstable estimates
> - Detection: high pairwise correlations, high R² with few significant ts

### Connections

- Builds on: Assumptions for n-variable model (Chunk 005)
- Related to: Heteroscedasticity, Autocorrelation (next two sections)

---

## Section: Problem of Hetero-scedasticity 🔴

### Core Idea

**Heteroscedasticity** occurs when the variance of the error term is not constant across observations (violating the homoscedasticity assumption). If E(uᵢ²) = σᵢ² (each error has its own variance), the OLS estimators are no longer BLUE — they lose minimum-variance property, making hypothesis tests unreliable.

> **In Simple Terms:** Imagine measuring spending across both poor and rich families. Rich families vary wildly in spending; poor families are more similar. This "fanning out" pattern in the data is heteroscedasticity. The OLS line is still drawn, but the error bands around it are wrong.

### Key Concepts

#### The Homoscedasticity Assumption (Recall)

Classical assumption: All error terms have the **same constant variance σ²**:
- E(uᵢ²) = σ² for all i

**Heteroscedasticity** = violation: each error has its own variance σᵢ²:
- E(uᵢ²) = σᵢ² ≠ σ² (varies from one observation to another)

#### Where Heteroscedasticity is More Common

- **Cross-sectional data**: More likely (different-sized firms, different income levels)
- **Time series data**: Less common (usually well-behaved over time)

#### Consequences of Heteroscedasticity

| Consequence | Detail |
|-------------|--------|
| OLS still **linear** | ✅ |
| OLS still **unbiased** | ✅ |
| OLS **no longer BLUE** | ❌ No minimum variance — **true BLUE are WLS estimators** |
| σ̂² (estimator of σ²) | Biased → standard errors of β estimates are biased |
| Hypothesis tests (t, F) | **Unreliable** — wrong conclusions possible |

**Root cause**: The σᵢ² enters the formula for se(β̂). If σᵢ² is mis-specified (assumed constant when it isn't), the standard errors are wrong → t-tests and F-tests give incorrect results.

#### How to Detect Heteroscedasticity

- **Visual**: Plot residuals (eᵢ²) against Xᵢ — a "flaring out" or "funnel" pattern indicates heteroscedasticity
  - No pattern → homoscedasticity likely
  - Expanding/contracting fan → heteroscedasticity
- **Formal tests**: Park Test, Glejser Test, White's General Test, Spearman's Rank Correlation Test, Goldfeld-Quandt Test

#### How to Tackle Heteroscedasticity

**Case 1: σᵢ² is known** → Divide all variables by √σᵢ → Transforms error terms to be homoscedastic → **Weighted Least Squares (WLS)**

**Case 2: σᵢ² proportional to Xᵢ** → Divide by √Xᵢ (square root transformation)

**Case 3: σᵢ² proportional to Xᵢ²** → Divide by Xᵢ → effectively converts to regression of (Y/X) on (1/X)

**Case 4: Respecification** → Use log-linear model (ln Y on ln X), which often corrects heteroscedasticity:
Y = β₀ + β₁ln(X) + μ

### Definitions

- **Heteroscedasticity**: Violation of homoscedasticity; the variance of error terms differs across observations (σᵢ² ≠ σ²). ⭐ (exam-important)
- **Weighted Least Squares (WLS)**: Estimation method that corrects for heteroscedasticity by dividing each observation by √σᵢ, making error terms uniform variance.
- **Homoscedasticity**: The classical assumption that V(uᵢ) = σ² (constant) for all observations. ⭐ (exam-important)

### ⚠️ Common Mistakes

- ❌ Mistake: Heteroscedasticity makes OLS biased → ✅ Correct: OLS remains **unbiased but NOT BLUE** (loses minimum variance property)
- ❌ Mistake: Heteroscedasticity is mainly a time-series problem → ✅ Correct: It's primarily a **cross-sectional data** problem

> **Quick Recall:**
> - Heteroscedasticity: V(uᵢ) = σᵢ² (varies, not constant)
> - OLS: still linear, still unbiased, **NOT BLUE anymore**
> - σ̂² becomes biased → t and F tests unreliable
> - Common in **cross-section** data, less in time-series
> - Fix: WLS (if σᵢ² known), square-root/log transformation

### Connections

- Builds on: Classical assumptions (Chunk 001), Gauss-Markov theorem (Chunk 002)
- Related to: Autocorrelation (next section)

---

## Section: Problem of Autocorrelation 🔴

### Core Idea

**Autocorrelation (serial correlation)** occurs when error terms are correlated with their own past values: E(uᵢuⱼ) ≠ 0 for i≠j. This violates the no-autocorrelation assumption. Like heteroscedasticity, it makes OLS estimators no longer BLUE — t and F tests become unreliable.

> **In Simple Terms:** If today's forecast error is positive, tomorrow's error is also likely positive. That's autocorrelation — errors "remember" the past. Your regression model is systematically missing something that persists over time.

### Key Concepts

#### What is Autocorrelation?

Definition: Disturbance terms are correlated across observations:
- Classical assumption: **E(uᵢuⱼ) = 0** for i≠j
- Violation (autocorrelation): **E(uᵢuⱼ) ≠ 0** for some i≠j

#### Causes of Autocorrelation

| Cause | Explanation |
|-------|-------------|
| **Inertia** | Cyclical ups/downs in economic time series (GDP, employment) tend to persist |
| **Model misspecification** | Omitted variables create systematic patterns in residuals |
| **Cobweb phenomenon** | Agricultural price-quantity cycles create correlated errors |
| **Data manipulation** | Averaging monthly to quarterly data dampens fluctuations, creating artificial correlation |

#### Consequences of Autocorrelation

Same as heteroscedasticity:
- OLS still **linear** and **unbiased** ✅
- OLS **no longer BLUE** ❌ (not minimum variance)
- t and F tests **unreliable**
- **R² is not a reliable measure of goodness of fit**

#### Detection: Durbin-Watson (d) Test

The most commonly used test for autocorrelation is the **Durbin-Watson d-statistic**:

**d = Σ(eₜ − eₜ₋₁)² / Σeₜ²**

- d ranges from 0 to 4
- d ≈ 2 → no autocorrelation
- d ≈ 0 → positive autocorrelation
- d ≈ 4 → negative autocorrelation

Other detection methods: visual inspection of error plots, Runs Test, Swed-Eisenhart critical runs test.

### Definitions

- **Autocorrelation (Serial Correlation)**: Correlation between error terms at different time periods: E(uᵢuⱼ) ≠ 0 for i≠j. Violates classical assumption. ⭐ (exam-important)
- **Durbin-Watson d Test**: Most common test for autocorrelation. d = Σ(eₜ − eₜ₋₁)²/Σeₜ²; d ≈ 2 means no autocorrelation. ⭐ (exam-important)

> **Quick Recall:**
> - Autocorrelation: E(uᵢuⱼ) ≠ 0 for i ≠ j
> - OLS: unbiased but **NOT BLUE**; t, F tests unreliable
> - Common in **time-series** data (unlike heteroscedasticity)
> - **Durbin-Watson d**: ≈2 = no problem; ≈0 = positive AC; ≈4 = negative AC

---

## Section: Maximum Likelihood Estimation (MLE) 🔴

### Core Idea

**Maximum Likelihood Estimation (MLE)** is an alternative to OLS that estimates parameters by maximizing the probability (likelihood) of observing the data given the model. Under normality of errors, **MLE and OLS give identical estimates for β parameters**. However, the MLE estimate of σ² is **biased** (divides by n instead of n−2), so OLS is preferred in practice.

> **In Simple Terms:** MLE asks "What values of β would make the data we see most probable?" OLS asks "What values of β minimize the sum of squared errors?" Conveniently, under normal errors, both questions have the same answer for β — but OLS handles σ² more accurately.

### Key Concepts

#### MLE Method

Given the model Yᵢ = β₀ + β₁Xᵢ + uᵢ, with uᵢ ~ N(0, σ²):
- Yᵢ is normally distributed with mean β₀ + β₁Xᵢ and variance σ²
- **Likelihood function (LF)**: The joint probability density of all observations:
  L(β₀, β₁, σ²) = (2πσ²)^(−n/2) · exp[−(1/2σ²)Σ(Yᵢ − β₀ − β₁Xᵢ)²]

- **Maximize log-likelihood** by differentiating w.r.t. β₀, β₁, σ² and setting equal to zero

#### MLE vs OLS Comparison ⭐

| Feature | OLS | MLE |
|---------|-----|-----|
| β estimates | b₀, b₁ | Same as OLS |
| σ² estimate | Σeᵢ²/(n−2) — **unbiased** | Σeᵢ²/n — **biased** (downward) |
| Assumption needed | 5 classical assumptions | 5 classical + normality |
| Theoretical strength | Moderate (BLUE under GM) | Stronger (asymptotic properties) |
| Practical preference | **Generally preferred** | Reserved for special cases |

**Key result**: When errors are normal, MLE gives the same β as OLS, so there's no practical gain in using MLE for β. And since MLE's σ̂² is biased, OLS with normality assumption dominates.

### Definitions

- **Maximum Likelihood Estimation (MLE)**: Method that estimates parameters by maximizing the probability (likelihood) of observing the given sample data. ⭐ (exam-important)
- **Likelihood Function**: The joint probability density function of all observations viewed as a function of the unknown parameters.

### Examples

**Regression of India's Imports on Exports and Foreign Investment (SPSS results):**

Model 1: Regressions of Imports on Exports and Foreign Investment Inflows (1991-2003)
- R² = 0.966; R̄² = 0.958 → Model explains ~96% of variation
- β̂(exports) = 1.263 (t = 12.192) → highly significant
- β̂(FDI) = −0.288 (t = −0.552) → insignificant
- F = 127.097 → overall model is significant

Model 2: Regression of FDI Inflows on Exports and Imports
- R² = 0.468; R̄² = 0.349 → Only 35% explained → poor fit
- Coefficients insignificant → theoretical expectation not supported

**Interpretation**: Imports are well-explained by exports (makes economic sense: exports earn foreign exchange → finance imports). FDI, however, is influenced by factors not captured by imports/exports alone.

> **Quick Recall:**
> - MLE maximizes likelihood function
> - Under normality: **MLE β = OLS β** (identical!)
> - But **MLE σ̂² is biased** (divides by n, not n−2)
> - Therefore: stick with OLS + normality assumption
> - Durbin-Watson signature: d ≈ 2 → OK; d < 2 → positive AC

### Connections

- Builds on: Classical Normal Regression Model (Chunk 003)
- Related to: MLE mentioned also in Unit 9 summary (Chunk 004)

### Open Questions

1. When would MLE be preferred over OLS (e.g., non-normal errors, limited dependent variable models)?
