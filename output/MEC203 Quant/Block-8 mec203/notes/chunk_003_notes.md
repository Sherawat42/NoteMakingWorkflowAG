# Chunk 003 — Variance, Theorems of Expectation, Unit 25 Wrap-up
<!-- Pages: 21-30 -->
<!-- Source: chunk_003.txt -->

## Section: Variance and Functions of a Random Variable 🔴
<!-- See chunk 002 for start of this section (Mathematical Expectation) -->

### Core Idea
Variance Var(x) = E[(x − m)²] measures how much a random variable's values spread around its mean m = E(x). It uses the *second moment about the mean*. The standard deviation σ = √Var(x). For any function g(x), the expected value generalises: E[g(x)] = Σ g(x_i) p_i.

> **In Simple Terms:** The expectation tells you the centre of the distribution; the variance tells you how spread out the distribution is around that centre. Two distributions can have the same mean but very different shapes.

### Key Concepts

#### Variance — formal definition
If E(x) = m (the mean), then Var(x) = E[(x − m)²] = Σ (x_i − m)² p_i.

#### Computational identity ⭐
**Var(x) = E(x²) − [E(x)]²**.
This identity is *the* working formula — much faster than computing each (x_i − m)².

#### Standard deviation
σ = √Var(x). Same units as the variable; variance has units squared.

#### Expectation of a function g(x)
E[g(x)] = Σ g(x_i) p_i (discrete). Lets us compute E(x²), E(e^(tx)), etc.

### Definitions
- **Variance Var(x)**: E[(x − E(x))²] = E(x²) − [E(x)]². ⭐ (exam-important)
- **Standard deviation σ**: √Var(x). ⭐ (exam-important)

### Mechanisms / Processes
Derivation of Var(x) = E(x²) − [E(x)]²:
1. Var(x) = E[(x − m)²] = Σ (x − m)² p_i.
2. Expand: Σ (x² − 2xm + m²) p_i = Σ x² p_i − 2m Σ x p_i + m² Σ p_i.
3. Identify: Σ x² p_i = E(x²); Σ x p_i = E(x) = m; Σ p_i = 1.
4. = E(x²) − 2m·m + m² = E(x²) − m² = E(x²) − [E(x)]².

> **Quick Recall:**
> - Var(x) = E(x²) − [E(x)]² ← faster computation
> - σ = √Var(x)
> - E[g(x)] = Σ g(x_i) p_i

---

## Section: Theorems on Mathematical Expectation 🔴

### Core Idea
Two key linearity-style theorems govern expectations: (1) **expectation of a sum** of random variables equals the **sum of expectations** (always, no independence required); (2) **expectation of a product** of *independent* random variables equals the **product of expectations**. The second theorem is essential for variance of sums, covariance, and the moment generating function machinery used later.

> **In Simple Terms:** If you toss two dice, the expected sum is just (expected first) + (expected second) — addition always works. But the expected *product* of two random outcomes equals the product of their averages only when the variables don't influence each other.

### Key Concepts

#### Theorem 1: Expectation of a sum
For random variables a, b, c, … (independent or not):
**E(a + b + c + …) = E(a) + E(b) + E(c) + …**

#### Theorem 2: Expectation of a product (requires independence)
If x and y are **independent**:
**E(xy) = E(x) · E(y)**.
Extends to any number of mutually independent variables.

#### Joint and marginal probabilities (bivariate)
For two discrete variables x (n values) and y (m values), p_ij = P(x = x_i AND y = y_j).
- **Marginal probability of x = x_i**: p_(i,•) = Σ_j p_ij (row sum).
- **Marginal probability of y = y_j**: p_(•,j) = Σ_i p_ij (column sum).
- **Conditional distribution of x given y = y_j**: p_(i,j) / p_(•,j) for each i.

| Concept | Formula | Use |
|---------|---------|-----|
| Joint p_ij | P(x=x_i, y=y_j) | Full bivariate |
| Marginal p_(i,•) | Σ_j p_ij | Distribution of x ignoring y |
| Conditional p_ij/p_(•,j) | P(x=x_i \| y=y_j) | Distribution of x given y |

#### Variance of a sum (Corollary)
**Var(x₁ + x₂ + … + x_n) = Σ Var(x_i) + 2 Σ_(i<j) Cov(x_i, x_j)**.
For mutually independent variables, all covariances are 0:
**Var(x₁ + … + x_n) = Σ Var(x_i)**.
- **Cov(x_i, x_j) = E[(x_i − m_i)(x_j − m_j)]**.

### Definitions
- **Marginal probability**: Probability that one variable takes a given value, summed over all values of the other(s). ⭐ (exam-important)
- **Conditional distribution**: For each value of the conditioning variable, a (re-normalised) probability distribution of the other.
- **Covariance Cov(x, y)**: E[(x − m_x)(y − m_y)] — measures co-variation; zero under independence.

### Mechanisms / Processes
Proof sketch of Theorem 1 (sum of expectations):
1. (x + y) takes value (x_i + y_j) with probability p_ij.
2. E(x + y) = ΣΣ (x_i + y_j) p_ij.
3. Split: ΣΣ x_i p_ij + ΣΣ y_j p_ij = Σ x_i (Σ_j p_ij) + Σ y_j (Σ_i p_ij) = Σ x_i p_(i,•) + Σ y_j p_(•,j) = E(x) + E(y).

Proof sketch of Theorem 2 (product, with independence):
1. P(x = x_i AND y = y_j) = p_i · q_j (independence).
2. E(xy) = ΣΣ x_i y_j (p_i · q_j) = (Σ x_i p_i)(Σ y_j q_j) = E(x) · E(y).

### Examples
**Example (Check Your Progress 5 Q1): Lottery expected winnings.**
First prize ₹10,000 with P = 0.0001; second prize ₹4,000 with P = 0.0004; otherwise 0.
| Outcome | P | x · P |
|---------|---|-------|
| 0 | 0.9995 | 0 |
| 4000 | 0.0004 | 1.6 |
| 10000 | 0.0001 | 1.0 |
| Total | 1 | **2.6** |
E(x) = ₹2.6.

**Example (Check Your Progress 5 Q2): Expected number of white balls drawn.**
Box: 4W, 6B. Draw 3 without replacement. Let x = number of white balls drawn.
- P(x = 0) = ⁴C₀ · ⁶C₃ / ¹⁰C₃ = 1/6.
- P(x = 1) = ⁴C₁ · ⁶C₂ / ¹⁰C₃ = 1/2.
- P(x = 2) = ⁴C₂ · ⁶C₁ / ¹⁰C₃ = 3/10.
- P(x = 3) = ⁴C₃ · ⁶C₀ / ¹⁰C₃ = 1/30.
Then E(x) = 0·(1/6) + 1·(1/2) + 2·(3/10) + 3·(1/30) = **6/5 = 1.2**.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying E(xy) = E(x) E(y) without checking independence → ✅ Correct: Without independence, E(xy) = E(x) E(y) + Cov(x, y).
- ❌ Mistake: Assuming Var(x + y) = Var(x) + Var(y) always → ✅ Correct: True only when Cov(x, y) = 0 (e.g., under independence).

### Edge Cases & Caveats
- Theorem 1 holds even if variables are dependent — additivity of expectation does **not** require independence.
- Cov(x, x) = Var(x), explaining the "+ Var" terms in the variance-of-sum formula.

> **Quick Recall:**
> - **E(a + b) = E(a) + E(b)** always
> - **E(xy) = E(x) E(y)** only if independent
> - **Var(Σ x_i) = Σ Var(x_i) + 2 Σ Cov(x_i, x_j)**; covariances vanish under independence

### Connections
- Builds on: [Mathematical Expectation — Introduction] (Chunk 002).
- Pre-requisite for: [Moments] (Chunk 004) — variance is the second central moment.
- Pre-requisite for: [Variance / Mean of binomial, Poisson] (Chunks 006–007).

---

## Section: Unit 25 Summary, Key Words & Exercises 🟢

### Core Idea
The unit closes by tying the four definitions, addition/multiplication theorems, conditional probability, Bayes' theorem, and mathematical expectation into a single coherent toolkit. The Key Words section gives canonical (exam-quotable) one-line definitions; the Exercises test routine application.

### Definitions (Key Words from textbook — verbatim restatements ⭐)
- **Bayes' Theorem**: P(B_i | A) = P(A|B_i) · P(B_i) / Σ P(B_j) P(A|B_j) when {B_j} is mutually exclusive and exhaustive.
- **Conditional Events**: When events are neither independent nor mutually exclusive — one's probability depends on the other.
- **Events**: When some elements of the sample space satisfy a particular criterion.
- **Independent Events**: P(A ∩ B) = P(A) × P(B).
- **Marginal Probability**: In a bivariate distribution, the probability that X takes a given value irrespective of Y (and vice versa).
- **Mathematical Expectation**: Weighted sum of values of x, weights = probabilities; E(x) = Σ x_i p_i.
- **Mutually Exclusive Events**: No two can occur simultaneously.
- **Mutually Exhaustive Events**: At least one must necessarily occur.
- **Sample Space**: Collection of all possible outcomes.

### Exercises (canonical worked examples — high-yield templates)

**Q1: Two balls drawn one by one without replacement (5 green + 7 red), first green & second red.**
P(G then R) = (5/12)(7/11) = **35/132**.

**Q2: Two cards drawn from 52 — both diamonds OR both kings.**
- Total = ⁵²C₂.
- Both diamonds = ¹³C₂ = 78. Both kings = ⁴C₂ = 6.
- P = (78 + 6)/⁵²C₂ = 84/1326 ≈ **0.063**.

**Q3: Tyre lifetime data (1000 cases).**
| Distance (km) | <4000 | 4001–9000 | 9001–14000 | >14000 |
|---------------|-------|-----------|------------|--------|
| Frequency | 20 | 210 | 325 | 445 |

(i) P(<4000) = 20/1000 = **0.02**.
(ii) P(>9000) = (325 + 445)/1000 = **0.77**.
(iii) P(4000 ≤ km ≤ 14000) = (210 + 325)/1000 = **0.535**.

**Q4: Coin tossed 3 times — P, Q, R mutually exclusive & exhaustive?**
- S = {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}.
- P = {TTT}, Q = {HTT, THT, TTH}, R = {HHH, HHT, HTH, THH}.
- P ∪ Q ∪ R = S → exhaustive. Pairwise intersections all empty → mutually exclusive. **Yes** they form a mutually exclusive and exhaustive set.

**Q5: P(A|B) when P(A) = 7/13, P(B) = 9/13, P(A ∩ B) = 4/13.**
P(A|B) = (4/13)/(9/13) = **4/9**.

> **Quick Recall:**
> - All four probability definitions usable depending on situation
> - Theorems: Total (addition, with/without overlap), Compound (multiplication, with conditional)
> - Bayes' = total + compound combined for "reverse" inference
> - E(x) = Σ x_i p_i; Var(x) = E(x²) − [E(x)]²

### Connections
- Closes Unit 25; sets up [Random Variables] in Unit 26 (Chunk 004).

### Open Questions
1. How does the addition theorem extend to countably infinite events (a key concern of measure theory)?
