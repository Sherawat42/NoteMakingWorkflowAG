# Chunk 009 — Normative Measures of Inequality
<!-- Pages: 75-84 -->
<!-- Source: chunk_009.txt -->

---

## Section: Normative Measures of Inequality 🔴

### Core Idea

**Normative measures** incorporate social welfare judgments into inequality measurement. Dalton (1920) was first to argue that economists should measure inequality in terms of its impact on social welfare, not just statistical dispersion. Four major normative indices are: Dalton's Index, Atkinson's Index, Sen's Index, and Theil's Entropy Index. All share the idea that distributing income equally would yield higher social welfare than unequal distribution (assuming diminishing marginal utility of income).

> **In Simple Terms:** If giving ₹100 to a poor person gains more welfare than taking it away from a rich person loses, then inequality is socially costly. Normative measures quantify this cost. They are "opinionated" — they embed a value judgment that inequality is bad for society.

### Key Concepts

#### Three Issues in Normative Inequality Measurement

1. Relationship between individual's income and their welfare (utility function U(xᵢ))
2. Relationship between personal income-welfare functions (same for all? different?)
3. Relationship between personal welfare and social welfare (additive? more complex?)

---

## Section: 11.5.1 Dalton Index 🔴

### Core Idea

Dalton (1920) assumes that individual welfare U(xᵢ) is a **concave** function of income (diminishing marginal utility). Social welfare is the **sum of individual welfares**. Under this framework, equal distribution maximizes social welfare for a given total income. The Dalton Index measures the ratio of actual social welfare to the maximum possible (equally distributed) social welfare.

> **In Simple Terms:** If everyone's happiness grows more slowly as they get richer (diminishing utility), then giving $1 to a poor person gains more happiness than taking $1 from a rich person loses. The Dalton Index measures how much welfare society *loses* by having unequal distribution.

### Key Concepts

#### Dalton's Assumptions

1. **Diminishing marginal utility**: ∂U/∂x > 0 (income increases welfare) but ∂²U/∂x² < 0 (at decreasing rate) → U(x) is concave
2. **Additive social welfare**: W = Σ U(xᵢ) (simple sum of individual welfares)
3. **Same welfare function for all**: U(xᵢ) = U(x) for all i → every person has identical income-welfare relationship

**Consequence**: For equal incomes (each = μ), W = N·U(μ). For an unequal distribution, ΣU(xᵢ) < N·U(μ) (due to concavity). Therefore, **equal distribution gives maximum social welfare** for any given total income.

#### Dalton's Index (D)

**D₃ = 1 − [ΣU(xᵢ)] / [N·U(μ)]** ⭐

- D = 0 when all incomes equal (maximum welfare)
- D > 0 when incomes are unequal (some welfare loss)
- Upper bound is not necessarily 1 (depends on welfare function shape)

**Problem with Dalton's Index**: It is **not invariant** to positive linear transformations of U(x). If you multiply the welfare function by a constant, the index value changes even though the underlying distribution didn't change.

#### Dalton's Two Illustrations

Using Bernoulli's welfare function: **U(xᵢ) = log(xᵢ + c)**
→ D = 1 − (log μ̂ + c)/(log μ + c)  where μ̂ = geometric mean

Using reciprocal welfare function: **U(xᵢ) = c − 1/xᵢ**
→ D = 1 − (c − 1/μ̃) / (c − 1/μ)  where μ̃ = harmonic mean

### Definitions

- **Dalton Index**: D = 1 − [ΣU(xᵢ)]/[N·U(μ)]; measures welfare loss from inequality; requires an explicit welfare function U(x). ⭐ (exam-important)
- **Diminishing Marginal Utility of Income**: ∂U/∂x > 0, ∂²U/∂x² < 0 — income increases welfare but at a decreasing rate; implies concave utility function.

> **Quick Recall:**
> - Dalton: social welfare = ΣU(xᵢ); U(x) is concave (diminishing marginal utility)
> - Equal income → maximum social welfare
> - D = 1 − [actual welfare / maximum possible welfare]
> - Weakness: **Not invariant** to linear transformations of U → value changes with scale

---

## Section: 11.5.2 Atkinson Index 🔴

### Core Idea

**Atkinson (1970)** addresses Dalton's weakness by defining inequality in terms of the **"equally distributed equivalent income" (μ*)**. μ* is the income level such that, if equally distributed, would generate the same social welfare as the current unequal distribution. The Atkinson Index A = 1 − μ*/μ measures what fraction of current mean income could be forgone if income were equally distributed and maintain the same welfare.

> **In Simple Terms:** Think of μ* as the "ethical income" — the per-capita income under perfect equality that would make society equally happy as now. If current mean = ₹100 but μ* = ₹75, then A = 1 − 75/100 = 0.25. Society could give up 25% of average income if it were distributed equally and be just as well-off!

### Key Concepts

#### Key Concept: Four Income Vectors (Chart I)

| Vector | Type | Description |
|--------|------|-------------|
| (a) | Actually distributed | {x₁, x₂, …, xₙ} — real distribution |
| (b) | Equally distributed | {μ, μ, …, μ} — everyone earns mean income |
| (c) | Equivalently distributed | {x₁*, x₂*, …, xₙ*} — same welfare as (a) but differently distributed |
| (d) | **Equally distributed equivalent** | {μ*, μ*, …, μ*} — equal AND same welfare as (a) |

**Key relationship**: W(b) ≥ W(a) = W(d) → **μ ≥ μ*** (mean income ≥ equally distributed equivalent income)

**μ* is defined by** the additive social welfare function:
N·U(μ*) = ΣU(xᵢ)

Or: **μ* = U⁻¹[(1/N)ΣU(xᵢ)]**

#### Atkinson Index

**A = 1 − μ*/μ** ⭐

- A = 0: perfect equality (μ* = μ)
- A → 1: maximum inequality (μ* → 0)
- **Bounded in [0, 1]** (approximately)
- Invariant to scale transformations (fixes Dalton's flaw)

#### Iso-elastic Utility Function (Atkinson's Specification)

For scale-invariance, Atkinson proposes:

| ε value | Utility function U(xᵢ) |
|---------|----------------------|
| ε ≠ 1 | α + β·xᵢ^(1−ε) |
| ε = 1 | log xᵢ |

**ε (epsilon) = inequality aversion parameter:**
- ε = 0 → linear utility → no aversion to inequality → A = 0 always (no information)
- ε increases → more weight to lower-income transfers
- As ε → ∞ → only the minimum income matters (Rawlsian)
- When ε → 1 → A = 1 − μ̂/μ (same as Champernowne Index)

**Atkinson's formula:**
**A = 1 − [1/N · Σxᵢ^(1−ε)]^(1/(1−ε)) / μ** (for ε ≠ 1)

Common values of ε: ½, 1/3, 2/3 — chosen based on degree of inequality aversion.

#### Atkinson vs Dalton

| Feature | Dalton | Atkinson |
|---------|--------|---------|
| Basis | Welfare loss ratio | Equivalent income ratio |
| Scale invariant? | ❌ No (main flaw) | ✅ Yes |
| Requires welfare function? | Yes | Yes (restricted form) |
| Bounded in [0,1]? | Not always | Yes (approximately) |

### Definitions

- **Equally Distributed Equivalent Income (μ*)**: The per-capita income that, if equally distributed, generates the same social welfare as the current distribution. Always μ* ≤ μ. ⭐ (exam-important)
- **Atkinson Index**: A = 1 − μ*/μ; measures what fraction of income could be sacrificed if uniformly distributed to maintain the same social welfare. ⭐ (exam-important)
- **Inequality Aversion Parameter (ε)**: In Atkinson's formula, ε determines how much weight is given to income transfers at the bottom; ε = 0 → no concern; ε → ∞ → only the poorest matter. ⭐ (exam-important)

> **Quick Recall:**
> - μ* = "ethical mean" — per-capita wealth under equality with same welfare as today
> - **A = 1 − μ*/μ** → A=0: equality; A→1: inequality
> - Fixes Dalton's scale problem; requires ε > 0 for meaningful results
> - ε = 1 → A = Champernowne Index (1 − geometric mean/arithmetic mean)

---

## Section: 11.5.3 Sen Index 🔴

### Core Idea

Sen (1973) generalizes Atkinson's index using a **broader social welfare function** W(x₁, x₂, …, xₙ) that need not be additively separable. Instead, W is assumed to be symmetric, quasi-concave, and increasing in all individual incomes. The Sen Index S is defined analogously to Atkinson's: **S = 1 − x*/μ** where x* is the "generalized equally distributed equivalent income."

> **In Simple Terms:** Sen says: "Why assume everyone's welfare just adds up? People's well-being also depends on how they compare to their neighbours." The Sen Index is a more flexible version of Atkinson's — it gives the same answer under utilitarian assumptions but allows richer social welfare functions.

### Key Concepts

**Generalized Equally Distributed Equivalent Income (x*)**:
- x* = income level such that W(x*, x*, …, x*) = W(x₁, x₂, …, xₙ)
- Under quasi-concavity: x* ≤ μ

**Sen Index**: **S = 1 − x*/μ**

- Under utilitarian framework (additive W): **S = A** (Sen and Atkinson give same result)
- More general than Atkinson — doesn't require additive utility

**Redistribution equivalent of growth**: Both Sen and Atkinson measures reveal that there is a "redistribution equivalent" of growth — some welfare gains can be achieved either through growth or through redistribution.

> **Quick Recall:**
> - Sen: broad social welfare W(x₁,...,xₙ) — symmetric, quasi-concave
> - **S = 1 − x*/μ** (same formula as Atkinson but more general W)
> - Under additivity: S = A (same as Atkinson)

---

## Section: 11.5.4 Theil Entropy Index 🔴

### Core Idea

Theil (1967) derives an inequality measure from **information theory (entropy)**. In information theory, entropy measures the degree of randomness or evenness of a probability distribution. Applied to income shares, maximum entropy (logN) corresponds to perfect equality, and minimum entropy (0) corresponds to perfect inequality. Theil's Index T = logN − H measures the deviation from maximum entropy.

> **In Simple Terms:** Think of entropy as "how surprising is the outcome?" If everyone earns the same, the rich person's income is no surprise (low inequality → high entropy/predictability). If one person has everything, that's highly concentrated (low entropy). Theil quantifies how far we are from the maximum spread-out situation.

### Key Concepts

#### Derivation from Information Theory

Start with income shares qᵢ = xᵢ/(Nμ), where Σqᵢ = 1.

**Entropy of income distribution** (treating qᵢ as "probabilities"):
**H = Σ qᵢ · log(1/qᵢ)** = − Σ qᵢ · log qᵢ

- Perfect equality (qᵢ = 1/N for all i): **H = logN** (maximum entropy)
- Perfect inequality (qᵢ = 1 for one person, 0 for others): **H = 0** (minimum entropy)

**Theil Index (T)** = logN − H = deviation from maximum entropy:
**T = logN − Σ qᵢ · log(1/qᵢ) = Σ qᵢ · log(N · qᵢ)** ⭐

- T = 0: perfect equality (H = logN)
- T = logN: maximum inequality (H = 0) → upper limit depends on N

#### Properties of Theil Index

- Lower limit: **T = 0** (perfect equality)
- Upper limit: **T = logN** (varies with population size — criticized as a weakness)
- **Decomposable**: Can be split into within-group and between-group inequality summands
- The changing upper limit is defended by Theil: "Inequality with 2 crore people, one having all, is greater than inequality with 2 people, one having all"
- Normalized version: **T' = T / logN** (used by some researchers to fix the upper limit at 1)

### Definitions

- **Theil Entropy Index**: T = Σ qᵢ log(Nqᵢ); measures inequality as deviation from maximum entropy; lower limit T=0, upper limit logN. ⭐ (exam-important)
- **Entropy**: Measure of randomness/evenness in information theory; maximum for equal distribution, minimum for most concentrated.
- **Decomposability**: Property that a measure can be broken into additive between-group and within-group components — crucial for policy analysis.

### Mechanisms / Processes

**Comparison of Normative Measures:**

| Index | Formula | Range | Key Parameter | Decomposable? | Scale-Invariant? |
|-------|---------|-------|--------------|--------------|----------------|
| Dalton | 1 − ΣU(xᵢ)/N·U(μ) | [0, varies] | Welfare function U | No | ❌ |
| Atkinson | 1 − μ*/μ | [0, 1] | ε (aversion) | No | ✅ |
| Sen | 1 − x*/μ | [0, 1] | General W | No | ✅ |
| Theil | Σqᵢlog(Nqᵢ) | [0, logN] | — | ✅ | ✅ |

### ⚠️ Common Mistakes

- ❌ Mistake: Theil Index is always bounded by 1 → ✅ Correct: Upper bound is logN, which varies with the population size
- ❌ Mistake: Atkinson and Sen are always different → ✅ Correct: Under utilitarian (additive) social welfare, **S = A**

> **Quick Recall:**
> - **Theil T = Σ qᵢ log(Nqᵢ)** — from information theory (entropy)
> - T = 0: equality; T = logN: maximum inequality
> - Unique advantage: **Decomposable** (between-group + within-group)
> - All 4 normative measures agree: equal distribution is better for social welfare
> - **Key difference**: Dalton (not scale-invariant); Atkinson (ε determines aversion); Sen (general W); Theil (entropy, decomposable)

### Connections

- All normative measures build on: Positive measures (Chunk 007), Lorenz Curve/Gini (Chunk 008)
- All share: U(x) concave → equal distribution better → inequality creates welfare loss
- Leads to: Unit 12 Composite Index (Chunks 010-013)
