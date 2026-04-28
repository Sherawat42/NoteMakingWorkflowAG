# Chunk 011 — Statistical Tables (F-Distribution at 1% Level), Block-9 Imprint
<!-- Pages: 101-103 -->
<!-- Source: chunk_011.txt -->

## Section: Statistical Tables — A4 (contd.) F Distribution at 1% Level 🟡
<!-- See Chunk 010 for the F-table at 5% level and intro -->

### Core Idea
**Table A4 (1%)** lists upper-1% critical values F₀.₀₁(df₁, df₂) for the F-distribution. df₂ rows: 1–30, then 40, 60, 120, ∞. df₁ columns: 1–10 (Page 101); 12, 15, 20, 24, 30, 40, 60, 120, ∞ (Page 102). Used for testing variance ratios at the more stringent 1% level — e.g. Exercise Q3's secondary critical value F₀.₀₁;₉,₇ = 6.72.

> **In Simple Terms:** Same F-table, stricter cut-off. If you want to be "really sure" before declaring two variances unequal, use 1% instead of 5%; the critical value roughly doubles for typical df.

### Key Concepts

#### Selected critical values F₀.₀₁(df₁, df₂)

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

The bolded entry F₀.₀₁;₉,₇ ≈ 6.72 (table reads 6.719) is the 1% critical value cited for Exercise Q3 (Chunk 010).

#### Selected critical values for larger df₁

| df₂ \ df₁ | 12 | 15 | 20 | 30 | 60 | 120 | ∞ |
|---|---|---|---|---|---|---|---|
| 1 | 6106.32 | 6157.29 | 6208.73 | 6260.65 | 6313.03 | 6339.39 | 6365.86 |
| 5 | 9.888 | 9.722 | 9.553 | 9.379 | 9.202 | 9.112 | 9.020 |
| 10 | 4.706 | 4.558 | 4.405 | 4.247 | 4.082 | 3.996 | 3.909 |
| 20 | 3.231 | 3.088 | 2.938 | 2.778 | 2.608 | 2.517 | 2.421 |
| 30 | 2.843 | 2.700 | 2.549 | 2.386 | 2.208 | 2.111 | 2.006 |
| ∞ | 2.185 | 2.039 | 1.878 | 1.696 | 1.473 | 1.325 | 1.000 |

### Definitions
- **F₀.₀₁(df₁, df₂)**: upper-1% critical value of the F-distribution; reject H₀ at 1% if computed F exceeds this entry.

### Mechanisms / Processes
1. Identify df₁ (numerator) and df₂ (denominator) from the F-statistic.
2. Choose 5% (Chunk 010 table) or 1% (this table) based on stated α.
3. Compare computed F with tabulated value:
   - F > F_(α; df₁, df₂) → reject H₀.
   - For lower-tail or two-tailed: use reciprocal property F_(1−α; df₁, df₂) = 1/F_(α; df₂, df₁) (see Chunk 004).

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing df₁ (numerator) with df₂ (denominator). → ✅ Correct: Numerator is the variance estimate **on top** of the F ratio; columns are df₁, rows are df₂.
- ❌ Mistake: Using 1% critical value when the question states α = 5%. → ✅ Correct: The 5%-level table is in Chunk 010; this chunk is 1%.

> **Quick Recall:**
> - F₀.₀₁;₉,₇ = 6.72 (vs F₀.₀₅;₉,₇ = 3.68 in Chunk 010).
> - F₀.₀₁;∞,∞ = 1.000 (point distribution at 1).
> - As df₂ → ∞ (with fixed df₁), F-critical → χ²(df₁)/df₁.

### Connections
- Continues from: F-table at 5% (Chunk 010).
- Used by: Exercise Q3 secondary critical value (Chunk 010).
- Builds on: F-distribution theory (Chunk 004) and reciprocal property F_(1−α; n₁, n₂) = 1/F_(α; n₂, n₁).

---

## Section: Block 9 Imprint Page 🟢
<!-- Reason: publishing metadata; no exam content -->

### Core Idea
The final page records the publishing imprint for Block 9.

### Definitions
- **Publisher / Imprint**: MPDD/IGNOU/P.O. 5.3K/September, 2023.
- **ISBN**: 978-93-5568-929-0.

### Connections
- Closes Block 9 entirely. Ends Unit 31 ("Hypothesis Testing") and the inferential-statistics arc spanning Units 28–31.
