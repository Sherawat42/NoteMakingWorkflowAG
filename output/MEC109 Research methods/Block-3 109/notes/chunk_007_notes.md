# Chunk 007 — Measures of Inequality: Positive Measures
<!-- Pages: 58-65 -->
<!-- Source: chunk_007.txt -->

---

## Section: Introduction to Measures of Inequality 🟢

### Core Idea

Income inequality is a central concern of economic policy. To study and compare inequality across societies, we need quantitative measures. Measures fall into two broad categories: **(i) Positive Measures** — which capture inequality without value judgment (purely statistical), and **(ii) Normative Measures** — which incorporate value judgments about social welfare. This chunk focuses on positive measures.

> **In Simple Terms:** Positive measures are like rulers — they just tell you how spread out incomes are, without saying whether that spread is "bad" or "good." Normative measures are like judges — they tell you whether inequality is morally problematic.

### Key Concepts

#### Two Categories of Inequality Measures

| Type | What it does | Examples |
|------|-------------|---------|
| **Positive** | Captures inequality without value judgments | Range, IQR, SD, Gini, Lorenz |
| **Normative** | Incorporates social welfare judgments | Dalton, Atkinson, Sen, Theil |

**Setup notation**:
- N persons in the distribution, income xᵢ (i = 1, 2, …, N) arranged in non-decreasing order
- Mean income = μ
- qᵢ = relative share of income for person i = xᵢ/Nμ
- Qᵢ = cumulative share of income for persons with income ≤ xᵢ
- pᵢ = proportion of persons with income xᵢ; Pᵢ = cumulative proportion of people

---

## Section: Positive Measures of Inequality 🔴

### Core Idea

Positive measures of inequality measure the **dispersion** in the income distribution using statistical tools — without implying any judgment about whether such inequality is socially desirable or harmful. The key ones covered are: Relative Range, Inter-Quartile Range, Relative Standard Variation, Standard Deviation of Logarithms, Champernowne Index, Hirschman-Herfindahl Indices, and Kolm's Index.

> **In Simple Terms:** These are just descriptive statistics applied to income distributions — like measuring how wide the "spread" is between the richest and poorest.

### Key Concepts

#### 11.2.1: Relative Range (RR)

The simplest measure: the gap between highest and lowest income relative to the mean.

**RR₁ = (Max xᵢ − Min xᵢ) / μ**

Variants:
- **RR₂ = (Max xᵢ − Min xᵢ) / (μN)** → lies in [0,1], gap between max and min income shares
- **RR₃ = (Max xᵢ − Min xᵢ) / Max xᵢ** → normalized by maximum
- **RR₄ = (Max xᵢ − Min xᵢ) / (Max xᵢ + Min xᵢ)** → normalized by sum

**Properties of RR:**
- RR₁ = 0 when everyone has equal income (perfect equality)
- RR₁ is maximum when one person has all income
- **Weakness**: Only uses extreme values (min and max) — ignores the entire middle of the distribution; any transfer between two non-extreme persons doesn't affect it

**Extreme Disparity Ratio (EDR)**: Ratio of mean income of highest fractile (percentile/decile) to mean of lowest fractile. Not bounded in [0,1]. Ignores transfers not involving extreme fractiles.

#### 11.2.2: Relative Inter-Quartile Range (Bowley's B)

Moderates the extremism of the range by focusing on the middle 50% of the distribution:

**B = (x₃q − x₁q) / (x₃q + x₁q)**

Where xᵣq = income at rth quartile (i.e., divides population into r and (4−r) quarters).

- B = 0 when all incomes are equal (degenerate distribution)
- B = 1 when lowest 75% have zero income
- **Weakness**: Uses only 50% of data (between Q1 and Q3); ignores transfers within Q1-Q3 range or beyond Q3

**Variant**: Inter-quartile ratio = (75th percentile − 25th percentile) / Median

#### 11.2.3: Relative Standard Variation (RSD)

Uses the full distribution (all observations):

**RSD = σ/μ** (standard deviation divided by mean)

- Also known as **coefficient of variation** when squared: **CV = (σ/μ)²**
- RSD = 0 when perfect equality
- Upper bound: (N−1)^(1/2) — depends on distribution size, NOT bounded in [0,1]
- **Advantage**: Sensitive to transfers at any level (uses all values)
- **Weakness**: Equally sensitive to transfers at all income levels (d transferred between rich vs poor changes RSD by equal amount)

#### 11.2.4: Standard Deviation of Logarithms (SDL)

Emphasizes transfers at lower income levels (as required by Sen's principle) by applying log transformation:

**SDL₁ = [1/N · Σ(log xᵢ − log μ)²]^(1/2)** (using arithmetic mean)

**SDL₂ = [1/N · Σ(log xᵢ − log μ̂)²]^(1/2)** (using geometric mean μ̂)

- Lower limit = 0 (perfect equality)
- Upper limit → ∞ as N → ∞
- **Advantage**: More sensitive to transfers at lower end (log "stretches" small income differences)
- **Critical weakness**: A transfer from rich to poor can **increase** measured inequality if the poor person's income is more than 2.72 times the mean. This is a serious logical flaw.
- **Variance of Logarithms (V₂)**: Square of SDL₂; is **decomposable** into between-group and within-group components

#### 11.2.5: Champernowne Index (CII)

Based on the fact that in an unequal distribution, geometric mean < arithmetic mean:

**CII = 1 − (μ̂/μ)** (additive inverse of ratio of geometric to arithmetic mean)

- Bounded in [0, 1]
- CII = 0 when everyone has equal income
- Sensitive to income transfers (especially at lower end)
- **Weakness**: Cannot be defined when any income = 0 (log of zero undefined)

#### 11.2.6: Hirschman-Herfindahl Indices (H)

Originally developed for measuring commodity concentration in trade (Hirschman, 1945) and market monopoly (Herfindahl, 1950); adapted for income inequality.

**H₁ = N^(1/2) · [Σqᵢ²]^(1/2)** (Hirschman's original, square root of sum of squares)

**H₂ = Σqᵢ²** (Herfindahl's measure — more commonly used)

Where qᵢ = income share of person/unit i.

- Both measures depend on N (number of units) as well as inequality
- **H₃ = Σqᵢ² − 1/N** (adjusted version for N=2 case)
- For N=2, q₁=0.99, q₂=0.01: H₂ = 0.98 (better characterizes monopoly than H₃=0.48)

**Application areas**: Commodity concentration in international trade, monopoly power in industries, autonomy/dependence in federations.

#### 11.2.7: Kolm's Index (K)

A curiosum (unusual/novel approach) by Kolm (1996) based on equal pairs in the distribution.

For a distribution with n different incomes and m recipients each:
**K = (N − Σfᵢ²) / (N² − N)** (approximately)

Where fᵢ = frequency of income xᵢ.

Purpose: Demonstrates the variety of approaches possible for measuring inequality.

### Definitions

- **Positive Measure of Inequality**: A statistical measure that captures the degree of inequality in a distribution without incorporating value judgments about social welfare. ⭐ (exam-important)
- **Relative Range (RR)**: (Max xᵢ − Min xᵢ)/μ; simplest inequality measure, but uses only extreme values.
- **Relative Standard Variation (RSD)**: σ/μ; uses all data points; equi-sensitive at all income levels.
- **Coefficient of Variation**: Square of RSD = (σ/μ)².
- **Champernowne Index**: 1 − (geometric mean / arithmetic mean); bounded in [0,1].
- **Herfindahl Index**: Σqᵢ² (sum of squared income shares); used in trade and market concentration analysis.

### Mechanisms / Processes

**Comparing Positive Measures by Key Criteria:**

| Measure | Uses All Values? | Bounded [0,1]? | Transfer Sensitivity | Major Weakness |
|---------|-----------------|----------------|---------------------|----------------|
| Relative Range | ❌ (only extremes) | No (RR₁) | Only extreme transfers | Ignores middle |
| IQR / Bowley's B | ❌ (middle 50%) | Yes | Only middle 50% | Ignores extremes |
| RSD | ✅ | No ([0, √(N−1)]) | Equal at all levels | Not more sensitive at lower end |
| SDL | ✅ | No (0 to ∞) | Greater at lower end | Can violate Pigou-Dalton condition |
| Champernowne | ✅ | Yes | Greater at lower end | Undefined if any income = 0 |
| Herfindahl | Per unit | Bounded | --- | Depends on N |

### ⚠️ Common Mistakes

- ❌ Mistake: RSD is bounded between 0 and 1 → ✅ Correct: RSD = σ/μ can exceed 1; it's bounded by (N−1)^(1/2)
- ❌ Mistake: Transferring from rich to poor always reduces all inequality measures → ✅ Correct: SDL can *increase* if the poor person's income exceeds 2.72μ — a known flaw

> **Quick Recall:**
> - **Positive measures**: No value judgment — statistical dispersion only
> - **RR**: Uses only extremes (max/min income) — weakest measure
> - **RSD = σ/μ**: Uses all data; equi-sensitive at all income levels
> - **Champernowne**: 1 − (geometric mean/arithmetic mean); bounded [0,1]
> - **Herfindahl**: Σqᵢ² — from trade/market concentration analysis

### Connections

- Leads to: Gini Index and Lorenz Curve (Chunk 008)
- Leads to: Normative Measures — Dalton, Atkinson, Sen, Theil (Chunk 009)

### Open Questions

1. Which positive measure is most commonly used in practice for policy analysis — and why?
