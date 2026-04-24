# Chunk 003 — Model Diagnostics: Residual Analysis & Residual Plots
<!-- Pages: 23–31 -->
<!-- Source: chunk_003.txt -->

## Section: Unit 4 Keywords & Answers — Context 🟢
<!-- Continues from: Unit 4 content (Chunks 001–002) -->

The first pages of this chunk contain Unit 4 keywords, references, and CYP answers. Key computed values from answers:

- **CYP1 Q2 Answer**: n=526 workers; β̂₂ = Σxᵢyᵢ/Σxᵢ² = 2179.204/4025.43 = **0.5413**; β̂₁ = 5.896 − 0.5413(12.5627) = **−0.9043**
- **CYP2 Q5 Answer**: σ̂² = RSS/(n−2) = 5980.682/524 = **11.41**
- **CYP3 Q1 Answer**: r² = 1 − 5980.682/7160.414 = **0.1648** → 16.48% of wage variation explained by education

---

## Section: Unit 5 Overview — Model Diagnostics Introduction 🟢

### Core Idea
Unit 5 (Model Diagnostics) extends Unit 4 by teaching how to **verify that a fitted regression model is appropriate**. Diagnosis involves examining residuals to check for assumption violations: non-linearity, heteroscedasticity, autocorrelation, and non-normality.

> **In Simple Terms:** After fitting a regression, you inspect the "mistakes" (residuals) — if those mistakes show patterns, your model has a problem.

### Key Concepts
Diagnostic tools covered in Unit 5:
1. Residual plots (against X, against Ŷ, against time)
2. Normality tests (P-P plot, Jarque-Bera test)
3. Special cases (regression through origin, scale changes)

### Connections
- Builds on: Residuals defined in OLS Method (Chunk 001)
- Continues into: Specific diagnostic tests (Chunks 003–004)

---

## Section: Residuals — Definition and Properties 🔴

### Core Idea
The **residual** ûᵢ is the observed difference between the actual value Yᵢ and the model's predicted value Ŷᵢ for each observation. Residuals have a mean of zero (Σûᵢ = 0) and serve as estimates of the true but unobservable error terms uᵢ. Systematic patterns in residuals indicate model inadequacy.

> **In Simple Terms:** Residuals are the "leftovers" after the model has done its best to predict Y. If the leftovers clump together in patterns, the model missed something.

### Key Concepts

#### Residual vs Error Term
| Concept | Symbol | Nature | Observable? |
|---------|--------|--------|-------------|
| Error term | uᵢ | True gap from PRF | No (theoretical) |
| Residual | ûᵢ or eᵢ | Estimated gap from SRF | Yes (computed) |

**Formula:** ûᵢ = Yᵢ − Ŷᵢ ... (5.1)

#### Algebraic Properties of Residuals
1. **Σûᵢ = 0** — sum of residuals is zero (they cancel out)
2. They measure the **unaccounted-for variability** in Y that the model couldn't explain

High error variance (σ²ᵤ) → widely dispersed residuals → lower R² (residuals inflate RSS; recall R² = 1 − RSS/TSS).

### Definitions
- **Residual (ûᵢ or eᵢ)**: ûᵢ = Yᵢ − Ŷᵢ; the difference between observed and predicted Y. ⭐ (exam-important)
- **Observed vs Predicted**: Yᵢ is observed; Ŷᵢ = β̂₁ + β̂₂Xᵢ is predicted/fitted.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating residuals as the same as error terms → ✅ Correct: uᵢ is theoretical (unobservable); ûᵢ is computable from sample data.

> **Quick Recall:**
> - ûᵢ = Yᵢ − Ŷᵢ
> - Σûᵢ = 0 (always)
> - Patterns in residuals → assumption violations

### Connections
- Builds on: OLS definition of RSS (Chunk 001)
- Used in: All residual plots below

---

## Section: Residual Plot — Patterns and Interpretation 🔴

### Core Idea
A **residual plot** graphs residuals (ûᵢ) on the Y-axis against Xᵢ or Ŷᵢ on the X-axis. If the residuals scatter **randomly** around zero within a horizontal band, the linear model is appropriate. Non-random patterns (U-shape, funnel, bow) signal model inadequacy.

> **In Simple Terms:** Imagine scattering your model's mistakes on a graph. If they look like a cloud around zero, you're fine. If they form a smiley face or a trumpet shape — something's wrong.

### Key Concepts

#### Residual Plot Against Xᵢ — Three Patterns (Fig. 5.1)
| Pattern | Shape | Inference |
|---------|-------|-----------|
| (a) Random | Cloud around zero axis | ✅ Linear model appropriate |
| (b) U-shaped | Curve — residuals dip then rise | ❌ Non-linear relationship |
| (c) Inverted-U | Curve — residuals rise then dip | ❌ Non-linear relationship |

Conclusion: If residuals exhibit non-random pattern → linear regression is **not** a good fit → consider non-linear model.

#### Residual Plot Against Ŷᵢ — Five Patterns (Fig. 5.2)
| Pattern | Shape | Inference |
|---------|-------|-----------|
| (a) Horizontal band | Residuals randomly within a band | ✅ No model defect |
| (b) Outward funnel | Variance increases with Ŷᵢ | ❌ Heteroscedasticity (σ²ᵤ increases) |
| (c) Inward funnel | Variance decreases with Ŷᵢ | ❌ Heteroscedasticity (σ²ᵤ decreases) |
| (d) Double bow | Residuals form two curves | ❌ Binomial Y; non-linear relationship; variance proportional to Ŷ(1−Ŷ) |
| (e) Curved shape | Single curve pattern | ❌ Non-linearity; higher-order X terms or log transformation needed |

#### Residual Plot Over Time (Fig. 5.3)
When data is collected over time, plot residuals against time order (instead of Ŷᵢ):
- Random band → ✅ No temporal autocorrelation
- Funnel shape → ❌ Variance changing over time
- Double bow / non-linear → ❌ Relationship is not stable; add linear/quadratic time terms

**General interpretation for all residual-vs-Xᵢ plots:**
- (a) Horizontal band → no model defects
- (b) Funnel shape → non-constant variance (heteroscedasticity)
- (c) Double bow / nonlinear → assumed relationship incorrect or Y may be proportion, higher-order terms needed

### Definitions
- **Residual plot**: A scatter diagram with ûᵢ on the Y-axis and Xᵢ or Ŷᵢ on the X-axis, used to visually diagnose regression model assumptions. ⭐ (exam-important)
- **Horizontal band pattern**: Residuals randomly within a constant-width band around zero — indicates correct model specification. ⭐ (exam-important)
- **Funnel shape pattern**: Residuals form an expanding or contracting shape — indicates heteroscedasticity (non-constant error variance). ⭐ (exam-important)
- **Double bow pattern**: Residuals enclosed in two curves — suggests Y may follow binomial distribution or that the relationship is non-linear with variance proportional to Ŷ(1−Ŷ).

### ⚠️ Common Mistakes
- ❌ Mistake: Random residuals in ûᵢ vs Ŷᵢ plot means no problems → ✅ Correct: Also need to check temporal plots and normality (not just Ŷᵢ).
- ❌ Mistake: All non-linear patterns require a log transformation → ✅ Correct: Non-linearity could also be resolved by adding higher-order terms or omitted variables.

> **Quick Recall:**
> - Random band around zero → ✅ Good model
> - Funnel → ❌ Heteroscedasticity
> - U-shape / Inverted-U → ❌ Non-linearity
> - Double bow → ❌ Non-linear; Y possibly bounded [0,1]
> - Temporal funnel → ❌ Time-varying variance
> - Best diagnostic: visual examination of residual plots

### Connections
- Builds on: Residuals definition (this chunk)
- Continues into: Formal normality tests (Chunk 004)
- Related to: Heteroscedasticity (Unit 11, mentioned in Chunk 005)
