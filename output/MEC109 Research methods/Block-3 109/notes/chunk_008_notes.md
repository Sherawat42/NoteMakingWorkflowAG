# Chunk 008 — Gini Index and Lorenz Curve
<!-- Pages: 66-74 -->
<!-- Source: chunk_008.txt -->

---

## Section: Gini Index 🔴

### Core Idea

The **Gini Index** (or Gini Coefficient), developed by Italian statistician Corrado Gini (1912), is the most widely used measure of income inequality. Unlike range-based measures that compare only extremes, Gini compares **all pairs of incomes** — measuring the average absolute difference between all pairs as a proportion of mean income. It equals **twice the area between the diagonal of equality and the Lorenz Curve**, and is bounded between 0 (perfect equality) and 1 (perfect inequality).

> **In Simple Terms:** Imagine picking any two people from a society at random. How different are their incomes on average? Gini captures this "average difference between random pairs" as a fraction of mean income. Gini = 0 means everyone earns the same; Gini = 1 means one person earns everything.

### Key Concepts

#### Gini as a Measure of Dispersion

Other dispersion measures (mean deviation, SD) compare each income to the mean. Gini's innovation: compare **all pairs with each other** — not just each value to the mean.

**Aggregate of absolute differences** of all pairs:
- ΣΣ|xᵢ − xⱼ| (summed over all i and j)
- Total number of pairs with replacement = N²

**Mean of absolute differences (with replacement)**:
- ΣΣ|xᵢ − xⱼ| / N² → ranges from 0 to 2μ

**Coefficient of Mean Difference (CMD)**:
- CMD = (1/μN²)ΣΣ|xᵢ − xⱼ| → ranges from 0 to 2

**Gini Coefficient (G)** = CMD / 2 → **bounded in [0, 1]**:

**G = (1/2μN²) ΣΣ|xᵢ − xⱼ|**

Equivalently (Kendall & Stuart definition): "One half of the average value of absolute differences between all pairs of incomes divided by the mean income."

#### Gini in Terms of Income Shares (qᵢ)

Since qᵢ = xᵢ/(Nμ), Gini can also be written as:

**G = (1/2N²) ΣΣ|qᵢ − qⱼ|**

And for grouped data with proportions pᵣ and income shares qᵣ:

**G = (1/2)ΣΣ|qᵣ/pᵣ − qₛ/pₛ| · pᵣ · pₛ**

#### Gini Computational Device (via Lorenz Curve)

Gini (1914) showed that the Gini Index equals **1 minus twice the area under the Lorenz Curve**:

**G = 1 − 2A** (where A = area under Lorenz Curve)

To compute G numerically from grouped data (using trapezoids approximation):

**G = 1 − Σ(Pᵣ − Pᵣ₋₁)(Qᵣ + Qᵣ₋₁)**

Where:
- Pᵣ = cumulative proportion of population at class r
- Qᵣ = cumulative share of income at class r
- Sum is over all income groups g

**Steps to compute Gini:**
1. Arrange data in increasing order of income
2. Compute cumulative population shares (P₁, P₂, …, Pg)
3. Compute cumulative income shares (Q₁, Q₂, …, Qg)
4. Plot Lorenz curve (Pᵣ on x-axis, Qᵣ on y-axis)
5. Calculate area under Lorenz curve (A) using trapezoid formula
6. G = 1 − 2A

### Definitions

- **Gini Index (G)**: Measure of income inequality equal to half the mean absolute difference between all pairs of incomes divided by mean income; bounded in [0, 1]. ⭐ (exam-important)
- **Coefficient of Mean Difference (CMD)**: Mean absolute difference between all pairs (including self comparisons); CMD = 2G · μ.
- **G = 1 − 2A**: Gini equals 1 minus twice the area under the Lorenz Curve — the most practical formula for computation. ⭐ (exam-important)

### Mechanisms / Processes

**Deriving the Gini computation formula step by step:**
1. Lorenz curve lies in the unit square; diagonal OB = line of equality
2. Area under the diagonal OB = 1/2
3. Area between diagonal and Lorenz curve = 1/2 − A (where A = area under Lorenz curve)
4. Lorenz Coefficient of Concentration (LCC) = 2 × (Area between diagonal and curve) = 2(1/2 − A) = 1 − 2A
5. LCC = Gini = **G = 1 − 2A**

### ⚠️ Common Mistakes

- ❌ Mistake: Gini = 0 means zero income → ✅ Correct: Gini = 0 means **perfect equality** (everyone has the same income); Gini = 1 means one person has all income
- ❌ Mistake: Gini compares each income to the mean → ✅ Correct: Gini compares **all pairs** of incomes with each other — this is its distinctive feature

> **Quick Recall:**
> - Gini: compares **all pairs** (not just to mean)
> - G = (1/2μN²)ΣΣ|xᵢ − xⱼ| → bounded [0, 1]
> - G = 1 − 2A (area under Lorenz curve)
> - G = 0: perfect equality; G = 1: perfect inequality
> - Gini = Lorenz Coefficient of Concentration (LCC)

---

## Section: Lorenz Curve 🔴

### Core Idea

The **Lorenz Curve** (Max O. Lorenz, 1905) is a graphical tool that plots the cumulative share of income against the cumulative share of population, both arranged in ascending order of income. The **diagonal of equality** represents perfect equality. The further the Lorenz Curve bows below this diagonal, the greater the inequality. Gini is directly derived from Lorenz curve.

> **In Simple Terms:** Draw a square. The diagonal from bottom-left to top-right means "bottom X% of people earn X% of income" — perfect equality. Now draw the actual income curve, which bows downward. The gap between them is inequality. Lorenz curve is that actual bowed curve.

### Key Concepts

#### Geometrical Definition

**X-axis (abscissa)**: Cumulative proportion of population (Pᵢ) — from 0 to 1  
**Y-axis (ordinate)**: Cumulative share of income (Qᵢ) — from 0 to 1

**Notation:**
- pⱼ = proportion of population in class j; qⱼ = income share of class j
- Pᵢ = Σⱼ pⱼ (cumulative population up to class i)
- Qᵢ = Σⱼ qⱼ (cumulative income share up to class i)

**Curve equation**: Qᵢ = L(Pᵢ) — the relationship between Pᵢ and Qᵢ

**Key points on the Lorenz Curve:**
- First point: (0, 0) — 0% of people have 0% of income
- Last point: (1, 1) — 100% of people have 100% of income

**Critical property**: Qᵢ ≤ Pᵢ for all i = 1, …, N−1 → Lorenz curve lies entirely in the **lower triangle** of the unit square (below the diagonal); curve never goes above the 45° line.

#### Properties of the Lorenz Curve ⭐

| Property | Statement |
|---------|-----------|
| pⱼ ∈ [0,1]; qⱼ ∈ [0,1] for all j | All shares are fractions |
| P₀ = Q₀ = 0 | Starts at origin |
| P_N = Q_N = 1 | Ends at (1,1) |
| Qᵢ ≤ Pᵢ for all i | Curve is in lower triangle |
| Line of equality | OB (diagonal): Pᵢ = Qᵢ → no inequality |
| Line of perfect inequality | Triangle OAB (Lorenz = OAB boundary) → one person has all income |

#### Using Lorenz Curve to Compare Distributions

- **Non-intersecting curves**: The curve **closer to the diagonal** has **less inequality**
- **Intersecting curves**: Direct comparison is impossible — reducing to a scalar measure (like Gini) is needed
- If curves intersect, one distribution has more inequality in one income range and less in another

#### Area-Based Measure (Lorenz Coefficient / Gini)

- Area between diagonal and Lorenz curve → divided by area of triangle OAB (= 1/2)
- **LCC = 2 × (Area between diagonal and curve) = 1 − 2A = Gini G** ⭐

#### Length-Based Measure (Kakwani's LK)

An alternative measure proposed by Kakwani (1980) based on the **length of the Lorenz curve**:

- Length of egalitarian line (diagonal) = √2 (minimum possible curve length)
- Length of perfect inequality line (sides OA + AB) = 2 (maximum possible)

**LK = (ℓ − √2) / (2 − √2)**

Where ℓ = actual length of the Lorenz curve.
- LK = 0 when Lorenz curve = diagonal (perfect equality)
- LK = 1 when Lorenz curve = sides of triangle (perfect inequality)

### Definitions

- **Lorenz Curve**: A graphical tool plotting cumulative population share (P) against cumulative income share (Q), both in ascending order of income; invented by Max O. Lorenz (1905). ⭐ (exam-important)
- **Line of Equality (Egalitarian Line)**: The 45° diagonal OB; represents perfect equality where bottom X% of people earn exactly X% of total income. ⭐ (exam-important)
- **Line of Perfect Inequality**: The two sides of triangle OAB; represents one person holding all income.
- **Lorenz Coefficient of Concentration (LCC)**: = 2 × (area between diagonal and Lorenz curve) = Gini coefficient. ⭐ (exam-important)
- **Kakwani's LK**: Length-based inequality measure: LK = (ℓ − √2)/(2 − √2).

### Mechanisms / Processes

**Constructing a Lorenz Curve from data:**
1. Arrange all income recipients in ascending order of income (poorest first)
2. Divide into classes (deciles, quintiles, etc.)
3. Compute pⱼ = class population / total population; qⱼ = class income share / total income
4. Compute cumulative Pᵢ = Σpⱼ; Qᵢ = Σqⱼ
5. Plot (Pᵢ, Qᵢ) points and connect them; also draw diagonal (egalitarian line)
6. The area between diagonal and the curve is the basis for Gini computation

### ⚠️ Common Mistakes

- ❌ Mistake: Lorenz curves that cross can still be compared by visual inspection → ✅ Correct: When Lorenz curves **intersect**, visual comparison fails; must use a numerical measure like Gini
- ❌ Mistake: Lorenz curve can be above the diagonal → ✅ Correct: Lorenz curve is **always below or on** the diagonal (Qᵢ ≤ Pᵢ always)

> **Quick Recall:**
> - Lorenz curve: X-axis = cumulative population share; Y-axis = cumulative income share
> - Always lies below (or on) the 45° diagonal
> - Diagonal OB = line of equality (Gini = 0)
> - Triangle OAB = line of perfect inequality (Gini = 1)
> - **G = 1 − 2A** (Gini = 1 minus twice area under Lorenz)
> - Curves can't be compared when they intersect → use Gini
> - Kakwani's LK = (ℓ − √2)/(2 − √2)

### Connections

- Builds on: Gini Index (earlier in this chunk)
- Gini = Lorenz Coefficient of Concentration — they are intrinsically linked
- Leads to: Normative Measures (Chunk 009)

### Open Questions

1. Why might two countries with the same Gini coefficient have very different distributions?
