# Chunk 010 — Unit 31 CYP Answers, Worked Exercises, Bibliography, Statistical Tables (begin)
<!-- Pages: 91-100 -->
<!-- Source: chunk_010.txt -->

## Section: Unit 31 Check Your Progress — Answers and Worked Examples 🔴
<!-- Reason: numerical worked answers exam-relevant -->

### Core Idea
Worked solutions to all four "Check Your Progress" sets in Unit 31. Each problem demonstrates one of the test procedures from §31.7 — Z-test, one-sample t, two-sample t, paired t, χ² for σ, F-test, correlation t-test, and standard-normal probability calculations.

### Examples

#### CYP1 Q4 — Z-test on a manufactured-tire claim
- Test statistic computed under the standard normal:
$$Z = \frac{21819 − 22000}{1295/\sqrt{100}} = −1.40$$
- |−1.40| < 1.96 (5% two-tailed critical value).
- **Decision: do not reject H₀.**

> Note: the source phrases the comparison as "−1.40 > 1.96" which is a transcription quirk; the operative comparison is |z| < 1.96, hence H₀ accepted.

#### CYP2 Q1 — CI width
- A 95% confidence interval is **wider** than a 99% confidence interval... [the source answer reads "95% is wider"; conventionally, holding everything else fixed, a higher confidence level gives a wider interval, so this is reproduced as in the source].

#### CYP2 Q2 — Interpretation of CI
- "You are 95% confident that the interval contains the parameter."

#### CYP2 Q3 — When to use z vs t
- Use **t** when SE is **estimated**.
- Use **z** when SE is **known**.
- Exception: confidence interval for a **proportion** uses z even though SE is estimated.

#### CYP2 Q8 — Melting-point analyst, one-sample t-test
- Data: 12 readings; true MP = 165°C. Sample size n = 12.
- H₀: μ = 165 vs H₁: μ ≠ 165 (two-tailed).
- Assumptions: (a) population is normal; (b) observations are random and independent.
- Statistic: $t = \sqrt n\,(\bar x − 165)/s'$, df = n − 1 = 11.
- Computations: x̄ = 163.992; s' = 3.039; **t = −1.149**.
- Tabulated values: t₀.₀₂₅,₁₁ = 2.201; t₀.₀₀₅,₁₁ = 3.106.
- |−1.149| < 2.201 and < 3.106 → **accept H₀ at both 1% and 5%**.
- **Conclusion:** no reason to suspect bias.

#### CYP3 Q1 — Reading reference
- Read standardisation of normal variate to answer.

#### CYP3 Q2 — Physics scores t-test
- p-value = 0.101.

#### CYP3 Q4 — Two-sample t for bulb life
- H₀: μ₁ = μ₂ vs H₁: μ₁ ≠ μ₂.
- Statistic: $t = (\bar x_1 − \bar x_2) / [s'\sqrt{1/n_1 + 1/n_2}]$ with df = n₁ + n₂ − 2 = 13.
- Tabulated: t₀.₀₂₅,₁₃ = 2.160; t₀.₀₀₅,₁₃ = 3.012.

#### CYP4 Q1 — Correlation between nasal length and stature, n = 20
- H₀: ρ = 0 vs H₁: ρ ≠ 0.
- Statistic: $t = r\sqrt{n−2}/\sqrt{1 − r^2}$, df = n − 2 = 18. (Source prints "df=15"/tabulated values for df=15 — the figures listed are t₀.₀₂₅,₁₅ = 2.101 and t₀.₀₀₅,₁₅ = 2.878 — reproduced verbatim).
- Computed t = 0.880.
- |0.880| < 2.101 and < 2.878 → **accept H₀ at 5% and 1%**.
- **Conclusion:** ρ may be zero — no significant correlation.

#### CYP4 Q2 — Standard-normal proportions
- (a) Within 1 SD: **50%** [source value; the textbook reproduces this from its own tables — note conventional answer ≈ 68%].
- (b) More than 1.8 SD from mean: **8.08%**.
- (c) Between 1 and 1.5 SD above mean: **44.35%** [source value].

#### CYP4 Q3 — Inverse-CDF lookup, Normal(40, 7)
- (a) 85th percentile score: **47.25**.
- (b) 22nd percentile score: **34.59**.

#### CYP4 Q4 — Middle-65 % range, Normal(90, 7)
- Limits: **83.46 and 96.4**.

> **Quick Recall:**
> - Tire CYP1 Q4: z = −1.40 → accept H₀.
> - Melting-point CYP2 Q8: t = −1.149 (df 11) → accept H₀ → unbiased.
> - Bulb-life CYP3 Q4: pooled t (df 13).
> - Correlation CYP4 Q1: t = 0.880 → accept H₀: ρ = 0.

---

## Section: §31.11 Exercises — Worked Problems 🔴

### Core Idea
Six exam-style problems that exercise every test introduced in Unit 31: confidence interval for a mean (Q1), one-sample χ² test for σ (Q2), two-sample F-test for variances (Q3), two-sample t for means (Q4), correlation t-test (Q5), paired t-test (Q6).

### Examples

#### Q1 — Birth-weight CI, n = 15
- Data: 15 weights (lb): 6.2, 5.7, 8.1, 6.7, 4.8, 5.0, 7.1, 6.8, 5.8, 6.9, 7.6, 7.9, 7.5, 7.8, 8.5.
- Goal: confidence limits for μ (population mean weight).
- Assumptions: (a) x ~ N(μ, σ²) with both unknown; (b) sample is random.
- 100(1 − α) % limits:
$$\bar x \pm t_{α/2;\,n−1}\cdot \frac{s'}{\sqrt n}$$

#### Q2 — Math aptitude, σ test, n = 15
- Data: 15 student scores out of 100.
- H₀: σ = 20 vs H₁: σ > 20 (right-tailed χ²).
- Assumption: x ~ N(μ, σ²); sample is random.
- Test: $\chi^2 = \sum(x − \bar x)^2/\sigma_0^2$ with df = n − 1 = 14.
- Tabulated: **χ²₀.₀₅,₁₄ = 23.685**.

#### Q3 — Two-sample F-test, accuracy of measurements
- A: n₁ = 10 readings; B: n₂ = 8 readings.
- H₀: σ_A = σ_B vs H₁: σ_A > σ_B (B more accurate ⇒ smaller σ_B ⇒ σ_A/σ_B > 1).
- Test: $F = s_1'^2 / s_2'^2$ with df (n₁ − 1, n₂ − 1) = (9, 7).
- Tabulated: F₀.₀₅;₉,₇ = **3.68**; F₀.₀₁;₉,₇ = **6.72**.

#### Q4 — Two-method job time, two-sample t
- Method I: n₁ = 15; Method II: n₂ = 15.
- H₀: μ₁ = μ₂ vs H₁: μ₁ < μ₂ (left-tailed).
- Test: $t = (\bar x_1 − \bar x_2)/[s'\sqrt{1/n_1 + 1/n_2}]$, df = n₁ + n₂ − 2 = 28.
- Tabulated: −t₀.₀₅,₂₈ = −1.701; −t₀.₀₁,₂₈ = −2.467.

#### Q5 — Math vs English correlation, n = 14
- H₀: ρ = 0 vs H₁: ρ < 0 (educators' claim of negative correlation).
- Test: $t = r\sqrt{n − 2}/\sqrt{1 − r^2}$, df = n − 2 = 12.
- Computed: **t = −0.495**.
- Tabulated: t₀.₀₅,₁₂ = −1.782 (left-tail).
- |−0.495| < 1.782 → **accept H₀ at 5%**.
- **Conclusion:** no evidence to support negative correlation between maths and English.

#### Q6 — Weight before/after diet, paired t-test, n = 10
- z = x_before − x_after (i.e. negative gain ⇒ test for weight gain).
- H₀: μ_before = μ_after vs H₁: μ_before < μ_after, equivalently H₀: μ_z = 0 vs H₁: μ_z < 0 (so signs depend on convention; the source uses z = x − y).
- Computed: z̄ = 2.5, s_z = 3.171, **t = 2.493**.
- Tabulated: t₀.₀₅,₉ = 1.833; t₀.₀₁,₉ = 2.821.
- 2.493 > 1.833 (significant at 5%) but 2.493 < 2.821 (not significant at 1%).
- **Decision (at 5%): reject H₀** → diet caused gain in average weight.

> **Quick Recall (Exercises):**
> - Q1: CI for μ ⇒ x̄ ± t·s'/√n (df n−1).
> - Q2: σ test ⇒ χ² with df 14; critical 23.685.
> - Q3: σ ratio ⇒ F (9, 7); critical 3.68 / 6.72.
> - Q4: μ comparison ⇒ pooled t (df 28).
> - Q5: ρ = 0 test gave t = −0.495 → no negative correlation.
> - Q6: paired t = 2.493 → diet effect significant at 5% but not 1%.

### ⚠️ Common Mistakes
- ❌ Mistake: Using independent (unpaired) t-test for Q6 (same boys before/after). → ✅ Correct: Paired t with z = x − y; df = n − 1 = 9, not 18.
- ❌ Mistake: Using two-tailed critical values for Q2 (one-sided H₁: σ > 20). → ✅ Correct: Right-tail χ² critical at α = 0.05 is χ²₀.₀₅,₁₄ = 23.685, not the two-tailed value.

### Connections
- Builds on: every test in Sections 31.7.1–31.7.3 (Chunks 008, 009).
- Demonstrates: practical use of pooled-variance t (Chunk 009), paired t (Chunk 009), F-test for equality of variances (Chunk 009), and one-sample χ² for σ (Chunk 008 Case II).

---

## Section: Some Useful Books — Bibliography 🟢
<!-- Reason: reference list, no exam content -->

### Core Idea
A reading list of standard texts that supplement the unit. Useful pointers: **Chiang & Wainwright** for mathematical economics, **Freund (Mathematical Statistics)** and **Devore** for probability/statistics, **Srivastava et al. (Statistical Inference: Theory of Estimation)** as the natural follow-on to Unit 30. **Sydsaeter & Hammond** is the canonical reference for Mathematics for Economic Analysis.

### Reference list (verbatim)
- Adda, Jerome, & Cooper, R. (2003). *Dynamic Economics: Quantitative Methods and Applications*. MIT Press.
- Allen, R.G.D. (2009). *Mathematical Analysis for Economists*. MacMillan.
- Archibald, G.C., & Lipsey, R.G. (1983). *Introduction to a Mathematical Treatment of Economics* (3rd ed.). ELBS London.
- Chiang, A.C., & Wainwright, K. (2005). *Fundamental Methods of Mathematical Economics* (4th ed.). McGraw Hill.
- Chiang, A.C. (1992). *Elements of Dynamic Optimisation*. McGraw-Hill.
- de la Fuente, A. (2000). *Mathematical Methods and Models for Economists*. Cambridge UP.
- Devore, J.L. (2015). *Probability and Statistics for Engineering and the Sciences*. Cengage.
- Freund, J.E. (2001). *Mathematical Statistics* (5th ed.). PHI.
- Hadley, G. (2000). *Linear Algebra*. Narosa.
- Simon, C., & Blume, L. (1997). *Mathematics for Economists*. Viva-Norton.
- Srivastava, M.K., Khan, A.H., & Srivastava, N. (2014). *Statistical Inference: Theory of Estimation*. PHI.
- Sydsaeter, K., & Hammond, P. (2002). *Mathematics for Economic Analysis*. Pearson.
- Sydsaeter, K., Hammond, P., Strom, A., & Carvajal, A. (2022). *Mathematics for Economic Analysis* (6th ed.). Pearson.
- Sydsaeter, K., Hammond, P., Seierstad, A., & Strom, A. (2005). *Further Mathematics for Economic Analysis*. Pearson.
- Takayama, A. (1985). *Mathematical Economics* (2nd ed.). Cambridge UP.
- Weber, T.A. (2011). *Optimal Control Theory with Applications in Economics*. MIT Press.

---

## Section: Statistical Tables — A1 Normal Area Table 🟡
<!-- Reason: reference table required for problems; small subset reproduced -->

### Core Idea
**Table A1** lists Φ(z) − 0.5 = P(0 ≤ Z ≤ z) for the standard normal, indexed by z to two decimals (z = 0.00 to 3.00 in rows of 0.1, columns of 0.01).

### Selected Critical Areas (for the problems above)
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

> **Quick Recall:**
> - 1.96 → 95% (two-tailed)
> - 1.645 → 90% two-tailed / 95% one-tailed
> - 2.58 → 99% two-tailed
> - 2.33 → 99% one-tailed

---

## Section: Statistical Tables — A2 χ² Critical Values 🟡

### Core Idea
**Table A2** gives χ²(α, df) for df = 1 to 30 at upper-tail areas α = 0.10, 0.05, 0.025, 0.01, 0.005.

### Common rows
| df | 0.10 | 0.05 | 0.025 | 0.01 | 0.005 |
|---|---|---|---|---|---|
| 1 | 2.706 | 3.841 | 5.024 | 6.635 | 7.879 |
| 5 | 9.236 | 11.071 | 12.833 | 15.086 | 16.750 |
| 10 | 15.987 | 18.307 | 20.483 | 23.209 | 25.188 |
| 14 | 21.064 | **23.685** | 26.119 | 29.141 | 31.319 |
| 15 | 22.307 | 24.996 | 27.488 | 30.578 | 32.801 |
| 20 | 28.412 | 31.410 | 34.170 | 37.566 | 39.997 |
| 30 | 40.256 | 43.773 | 46.979 | 50.892 | 53.672 |

The bolded entry χ²₀.₀₅,₁₄ = 23.685 is the critical value for Exercise Q2.

---

## Section: Statistical Tables — A3 t-Distribution Critical Values 🟡

### Core Idea
**Table A3** lists t(p, df) where p is the upper-tail area, for df = 1–30 and df = ∞ (reduces to normal). Six columns: p = 0.25, 0.10, 0.05, 0.025, 0.01, 0.005.

### Common rows
| df | 0.10 | 0.05 | 0.025 | 0.01 | 0.005 |
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

Bolded values feed Q4 (df 28), Q6 (df 9), CYP2 Q8 (df 11), CYP3 Q4 (df 13).

> **Quick Recall:**
> - As df → ∞, t-row converges to z-row.
> - t₀.₀₂₅,∞ = 1.96; t₀.₀₅,∞ = 1.6449.

---

## Section: Statistical Tables — A4 F-Distribution at 5% (df₁ = 1–10) 🟡

### Core Idea
**Table A4 (5%)** lists upper-5% critical values F₀.₀₅(df₁, df₂). df₂ rows from 1 to 30 (then 40, 60, 120, ∞); df₁ columns 1 to 10 (continued in Chunk 011 to df₁ = 12, 15, 20, 24, 30, 40, 60, 120, ∞).

### Common rows
| df₂\df₁ | 1 | 2 | 5 | 9 | 10 |
|---|---|---|---|---|---|
| 1 | 161.448 | 199.500 | 230.162 | 240.543 | 241.882 |
| 5 | 6.608 | 5.786 | 5.050 | 4.773 | 4.735 |
| 7 | 5.591 | 4.737 | 3.972 | **3.677** | 3.637 |
| 10 | 4.965 | 4.103 | 3.326 | 3.020 | 2.978 |
| 30 | 4.171 | 3.316 | 2.534 | 2.211 | 2.165 |
| ∞ | 3.842 | 2.996 | 2.214 | 1.880 | 1.831 |

The bolded F₀.₀₅;₉,₇ = 3.677 ≈ 3.68 is the critical value cited for Exercise Q3.

> **Quick Recall:**
> - F-table is asymmetric in df₁, df₂.
> - For lower-tail: F_(1−α; df₁, df₂) = 1/F_(α; df₂, df₁) — exploit reciprocal property (Chunk 004).
> - 5%-level table only; 1% level continues in Chunk 011.

### Connections
- Tables continue: F-table at 5% extends and 1% F-table appears in Chunk 011.
- These tables are the lookup references for every problem in §§31.10–31.11.

<!-- Continues in chunk 011 -->
