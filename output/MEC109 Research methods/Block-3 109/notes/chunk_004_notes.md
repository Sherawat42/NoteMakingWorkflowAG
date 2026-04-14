# Chunk 004 — Hypothesis Testing and Unit 9 Key Words
<!-- Pages: 28-35 -->
<!-- Source: chunk_004.txt -->
<!-- See chunk 003 for the beginning of Hypothesis Testing section -->

---

## Section: Hypothesis Testing 🔴
<!-- See chunk 003 for the conceptual introduction -->

### Core Idea

The t-statistic is used to test whether the regression slope β equals a hypothesized value β₀. Under the CNRM, since β̂ is normally distributed but σ is unknown, dividing (β̂ − β₀) by its estimated se gives a **t-distribution** with (n−2) degrees of freedom. Both two-tailed and one-tailed tests can be conducted depending on the nature of inquiry.

> **In Simple Terms:** Think of the t-test as measuring how many "standard errors" away your estimate is from the hypothesized value. If it's more than ~2 standard errors away (at 5% significance), you reject the hypothesis — the result is too improbable to be a coincidence.

### Key Concepts

#### Student-t Distribution

Since σ is unknown and estimated by σ̂, the test statistic becomes:

**t = (β̂ − β₀) / se(β̂)** ~ t(n−2)

Where:
- β₀ = hypothesized value of β (usually **0** for testing significance)
- se(β̂) = estimated standard error of β̂
- n−2 = degrees of freedom
- Under H₀: β = 0, the t-statistic simplifies to **t = β̂ / se(β̂)**

#### Null and Alternative Hypotheses

**Two-tailed test (testing for any significant relationship):**
- H₀: β = 0 (no relationship)
- H₁: β ≠ 0 (any relationship)

**Two-tailed test (testing a specific value):**
- H₀: β = β₀ (e.g., β = 0.80)
- H₁: β ≠ β₀

**Decision rule:**
- Compute |t_calculated|
- Find t_critical from t-table (at desired significance level, with n−2 df)
- If |t_calc| > t_critical → **Reject H₀**
- If |t_calc| ≤ t_critical → **Cannot reject H₀**

#### Steps for Hypothesis Testing in Regression

| Step | Action |
|------|--------|
| 1 | Set H₀ and H₁ |
| 2 | Choose significance level (1% or 5%) |
| 3 | Compute t = (β̂ − β₀) / se(β̂) |
| 4 | Find critical t from table (df = n−2) |
| 5 | Compare: Reject H₀ if |t_calc| > t_critical |
| 6 | Interpret in the context of the economic hypothesis |

### Mechanisms / Processes

**Chain of reasoning:**
1. Start with CNRM → β̂ ~ N(β, σ²/Σx²)
2. σ is unknown → substitute σ̂
3. Standardize → t = (β̂ − β) / se(β̂) ~ t(n−2)
4. Under H₀: β = β₀ → t = (β̂ − β₀) / se(β̂)
5. Use t-table to find critical value for given df and significance level

### Examples

**From Example 9.2: Is India's consumption function significant? (1980-2001)**

Test 1: Is β ≠ 0? (Is there any relationship between FCE and GDP?)
- H₀: β = 0; H₁: β ≠ 0 (two-tailed)
- β̂ = 0.719676; se(β̂) = 0.007865; df = n−2 = 22−2 = 20
- t_calc = β̂ / se(β̂) = 0.719676 / 0.007865 = **91.503**
- t_critical at 5% (df=20, two-tailed) = **2.086**; at 1% = **2.845**
- Since 91.503 >> 2.845: **Reject H₀ decisively**
- **Conclusion**: FCE significantly depends on GDP in India (1980-2001) ✅

Test 2: Is India's MPC equal to 80%? (H₀: β = 0.80)
- H₀: β = 0.80; H₁: β ≠ 0.80 (two-tailed)
- t_calc = (0.719676 − 0.80) / 0.007865 = (−0.080324) / 0.007865 = **−10.211**
- |t_calc| = 10.211 >> critical values of 2.086 and 2.845
- **Reject H₀**: MPC was NOT 80% during 1980-2001
- **Conclusion**: India's MPC ≈ 72%, not 80%, during the sample period

### ⚠️ Common Mistakes

- ❌ Mistake: Using Z-table instead of t-table when σ is unknown → ✅ Correct: When σ is estimated (replaced by σ̂), use student-t distribution, not standard normal
- ❌ Mistake: Accepting H₀ when we fail to reject it → ✅ Correct: We either "reject H₀" or "fail to reject H₀" — we never "accept" H₀ (absence of evidence ≠ evidence of absence)

### Edge Cases & Caveats

- One-tailed tests are appropriate when the direction of the effect is specified by theory (e.g., H₁: β > 0)
- The t-distribution approaches the normal distribution as n → ∞ (df → ∞)
- High t-statistic → statistically significant, but not necessarily economically meaningful

> **Quick Recall:**
> - t-test statistic: t = (β̂ − β₀) / se(β̂) ~ t(n−2)
> - Reject H₀ if |t_calc| > t_critical
> - At 5% significance, two-tailed, df=20: t_critical = **2.086**
> - At 1% significance, two-tailed, df=20: t_critical = **2.845**
> - India's consumption function: t = 91.5 → highly significant!

### Connections

- Builds on: Classical Normal Regression Model (Chunk 003)
- Builds on: Standard Error of Estimate (Chunk 002)
- Related to: F-test in multiple regression (Chunk 005/006)

---

## Section: Unit 9 Summary and Key Words 🟢

### Core Idea

Unit 9 covers the complete framework of the two-variable classical regression model: specification (PRF), estimation (OLS/SRF), measurement of fit (R²), alternative functional forms, and hypothesis testing using the t-distribution. The key takeaway is that the Gauss-Markov theorem guarantees OLS is BLUE, and the CNRM provides the basis for statistical inference.

### Key Definitions from Text

- **Classical Normal Regression Model**: A linear regression model in which the disturbance term is additionally assumed to be **normally distributed** (in addition to the 5 classical assumptions). Required for hypothesis testing using t-distribution. ⭐ (exam-important)

- **Classical Regression Model**: The conventional regression model Y = α + βX + U whose parameters are estimated by OLS under 5 assumptions. ⭐ (exam-important)

- **Gauss-Markov Theorem**: Under the assumptions of the classical regression model, among all linear unbiased estimators, the least square estimators have the minimum variance — i.e., OLS is BLUE. ⭐ (exam-important)

- **Goodness of Fit**: The ratio of Explained Sum of Squares (ESS) to Total Sum of Squares (TSS) — the R² coefficient. Measures how well the regression line fits the data. ⭐ (exam-important)

- **Functional Forms**: Linear (dY/dX = constant), Log-linear (elasticity = constant), Semi-log (growth rate = constant), Reciprocal (limiting value = α). All are linear in parameter. ⭐ (exam-important)

- **Hypothesis Testing**: Testing hypotheses about β using t = (β̂ − β₀)/se(β̂) ~ t(n−2). ⭐ (exam-important)

- **Population Regression Function (PRF)**: Y = α + βX + U. The true but unknown model in the population.

- **Sample Regression Function (SRF)**: Ŷ = α̂ + β̂X + Û. The estimated model from sample data.

- **Standard Errors of Estimate**: Standard deviations of α̂ and β̂ — measures of precision.

- **Two Variable Regression Model**: A regression model with exactly one explanatory variable (X).

> **Quick Recall: The Big Picture of Unit 9**
> 1. PRF: Y = α + βX + U (population truth — unknown)
> 2. 5 Classical Assumptions → OLS is BLUE (Gauss-Markov)
> 3. SRF: Ŷ = α̂ + β̂X (estimated from sample)
> 4. R² = ESS/TSS (goodness of fit: 0 to 1)
> 5. 4 Functional Forms: Linear, Log-linear, Semi-log, Reciprocal
> 6. +Normality assumption → CNRM → t-test for β

### Connections

- Unit 9 establishes the foundation for:
  - Unit 10 (Chunk 005-006): Extension to multiple variables + econometric problems
  - Maximum Likelihood Estimation (Chunk 006)
