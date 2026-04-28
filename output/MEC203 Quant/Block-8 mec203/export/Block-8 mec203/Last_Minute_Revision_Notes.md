# Last Minute Revision Notes

> *This document contains ONLY ultra-high-yield definitions (⭐), Quick Recall facts, Common Mistakes, and core bullet points.*


## Topics

| Aspect | Deterministic | Non-Deterministic |
|--------|---------------|-------------------|
| Repeatability with same outcome | Yes | No |
| Predictability | Outcome fully fixed by conditions | Outcome cannot be foretold |
| Tool for analysis | Classical mechanics, calculus | Probability, statistics |
| Examples | Falling stone, chemical reaction | Coin toss, dice, card draw |
- **Random experiment**: An act that can be repeated under given conditions whose outcome is not predictable beforehand. ⭐ (exam-important)

**Quick Recall:**
- Deterministic = same result every time; Non-deterministic = unpredictable result
- Probability theory deals only with **random** experiments

### Sample Space and Important Terminology 🔴

**Sample space (S)**

**Sub-sample space**

**Event types**
| Term | Meaning | Quick test |
|------|---------|-----------|
| Mutually exclusive | Two/more events cannot occur at the same time | A ∩ B = ∅ |
| Mutually exhaustive | At least one of the events must occur | A ∪ B ∪ … = S |
| Equally likely | No outcome is preferred over another | All P equal |
| Exhaustive set | Complete group of all elementary events of an experiment | Covers S |
| Independent | Occurrence of one event does not affect another | P(B\|A) = P(B) |
| Conditional | One event depends on another (rain depends on clouds) | P(B\|A) ≠ P(B) |
- **Sample space**: The collection of all possible outcomes of an experiment, denoted S. ⭐ (exam-important)
- **Event**: A subset of the sample space whose outcomes satisfy a particular criterion. ⭐ (exam-important)
- **Mutually exclusive events**: Events that cannot occur simultaneously. ⭐ (exam-important)
- **Mutually exhaustive events**: At least one of them necessarily occurs.
- **Equally likely events**: Outcomes such that none is expected in preference to another (e.g., head/tail of an unbiased coin).
- **Exhaustive set of events**: Set in which at least one event must occur — the complete group of elementary events of a random experiment.
- **Independent events**: Occurrence of one is not affected by occurrence of others.
- **Conditional events**: Events that are neither independent nor mutually exclusive — one is dependent on the other.
- **Venn diagram**: A rectangle (S) with circles (events). Disjoint circles = mutually exclusive; full coverage = exhaustive.
- E₁ = {HHH} = "all heads"
- E₂ = {HHH, HHT, HTH, THH} = "at least 2 heads"
- E₃ = {HHT, HTH, THH} = "exactly 2 heads"

**Quick Recall:**
- S = sample space (everything possible)
- Mutually exclusive ↔ disjoint sets ↔ cannot co-occur
- Exhaustive ↔ at least one must occur ↔ union covers S
- Equally likely ↔ symmetry assumption needed for the classical definition

### Four Definitions of Probability 🔴

**Classical Definition**
- **P(A) = 0** ⇔ event is impossible (no favourable outcome).
- **P(A) = 1** ⇔ event is sure (every outcome favourable).

**Axiomatic Definition (Kolmogorov-style)**
1. **P(A) ≥ 0** (non-negative).
2. **P(S) = 1** (the sure event has probability 1).
3. If A and B are mutually exclusive: **P(A ∪ B) = P(A) + P(B)**.

**Empirical Definition (Von Mises)**

**Subjective Definition**
| Definition | Uses | Strength | Weakness |
|------------|------|----------|----------|
| Classical | Coins, dice, cards | Simple, intuitive | Needs symmetry; fails for infinite outcomes |
| Axiomatic | Modern theory | General, rigorous | Abstract |
| Empirical | Long-run data | Data-driven | Limit cannot be observed |
| Subjective | Belief/judgement | Captures uncertainty in unique events | Not data-based |
- **Classical probability**: P(A) = (favourable outcomes) / (total outcomes), assuming outcomes are mutually exclusive, exhaustive, and equally likely. ⭐ (exam-important)
- **Axiomatic probability**: Probability assignment satisfying P(A) ≥ 0, P(S) = 1, and P(A ∪ B) = P(A) + P(B) for disjoint A, B. ⭐ (exam-important)
- **Empirical probability**: P(A) = lim(m/N) as N → ∞.
- **Subjective probability**: P(A) is a measure of belief about A.
1. Total outcomes N = 36 (mutually exclusive, exhaustive, equally likely under unbiased assumption).
2. Favourable outcomes for product = 18: only (3, 6) and (6, 3) → N_A = 2.
3. P(A) = N_A / N = 2/36 = 1/18.
| # | Technique | Formula |
|---|-----------|---------|
| 1 | Fundamental Principle of Counting | If processes done in p × q × r × … ways |
| 2 | Permutation (n distinct, take r) | ⁿP_r = n(n−1)(n−2)…(n−r+1) |
| 3a | Arrangement in a line | n! = 1·2·3·…·n |
| 3b | Arrangement in a circle | (n−1)! |
| 4 | Permutation with repetition (p alike, q alike, …) | n! / (p! q! r! …) |
| 5 | Combination | ⁿC_r = n! / [r!(n−r)!] |
| 6 | Choosing balls (a white from A, b black from B) | ᴬC_a · ᴮC_b |
| 7 | Ordered partition (distinct objects into r compartments with n₁, n₂, …, n_r in each) | n! / (n₁! n₂! … n_r!); total ways = rⁿ |
| 8 | Ordered partition (n identical objects into r compartments) | ⁽ⁿ⁺ʳ⁻¹⁾C_(r−1); none-empty: ⁽ⁿ⁻¹⁾C_(r−1) |

### ⚠️ Common Mistakes
- ❌ Mistake: Applying classical definition when outcomes are not equally likely (e.g., loaded die) → ✅ Correct: Use empirical or subjective definition.
- ❌ Mistake: Confusing the **axiomatic** P(S) = 1 with the **classical** "every outcome is favourable" → ✅ Correct: Axiomatic axiom is a definitional rule for the entire space; classical is a counting result for a specific event A = S.
- ❌ Mistake: Reading "equally likely" as a derived fact → ✅ Correct: It is an *assumption* one must justify (typically by symmetry of the physical setup).
- Classical definition fails for infinite sample spaces (e.g., picking a real number in [0,1]).
- The phrase "equally likely" inside the classical definition is itself a probability statement → the definition is **circular**.
- Empirical definition's limit cannot be empirically verified — it's an assumption.

**Quick Recall:**
- Four definitions: **Classical, Axiomatic, Empirical, Subjective**
- Classical formula: P(A) = N_A / N (under symmetry)
- Axioms: P(A) ≥ 0, P(S) = 1, additivity for disjoint events
- Counting techniques: factorials, ⁿP_r, ⁿC_r, ordered partitions
- Sets the stage for: [Theorems of Probability] (Chunk 002) — total and compound probability are derived from the classical/axiomatic definitions.
- Connects forward to: [Mathematical Expectation] (Chunks 002–003) — uses the probability-weighted sum that depends on these definitions.
1. How does the axiomatic definition handle continuous sample spaces (e.g., choosing a point uniformly on [0, 1])?
2. When two definitions give different numerical answers for the same problem, which should we prefer?

### Theorem of Total Probability (Addition Theorem) 🔴

**Mutually exclusive case**

**Extension to k mutually exclusive events**

**Non-exclusive case**

**Theorem of Complementary Event**
- **Theorem of Total Probability (Addition Theorem)**: P(A ∪ B) = P(A) + P(B) for mutually exclusive A, B; otherwise P(A ∪ B) = P(A) + P(B) − P(A ∩ B). ⭐ (exam-important)
- **Complement Aᶜ (or Aʹ)**: The non-occurrence of A. P(Aᶜ) = 1 − P(A). ⭐ (exam-important)
- **Boole's inequality**: P(A ∪ B) ≤ P(A) + P(B).
- **Bonferroni's inequality**: P(A ∩ B) ≥ P(A) + P(B) − 1.
1. Decompose A ∪ B into three disjoint pieces: A ∩ Bᶜ, Aᶜ ∩ B, A ∩ B.
2. P(A ∪ B) = P(AB̄) + P(ĀB) + P(AB).
3. Note A = (A ∩ B) ∪ (A ∩ Bᶜ) → P(A) = P(AB) + P(AB̄), so P(AB̄) = P(A) − P(AB).
4. Similarly P(ĀB) = P(B) − P(AB).
5. Substitute: P(A ∪ B) = [P(A) − P(AB)] + [P(B) − P(AB)] + P(AB) = P(A) + P(B) − P(A ∩ B).

**Quick Recall:**
- P(A ∪ B) = P(A) + P(B) − P(A ∩ B) (general)
- = P(A) + P(B) (if disjoint)
- P(Aᶜ) = 1 − P(A)
- Three-event inclusion–exclusion: + singles − doubles + triple

### Theorem of Compound Probability (Multiplication Theorem) 🔴

**Compound probability formula**

**Extension to three events**

**Decomposition of P(B) using complementary partition**
- **Theorem of Compound Probability (Multiplication Theorem)**: P(A ∩ B) = P(A) × P(B|A). ⭐ (exam-important)
- **Conditional probability P(B|A)**: Probability of B given A has occurred = P(A ∩ B)/P(A), provided P(A) > 0. ⭐ (exam-important)

**Quick Recall:**
- P(A ∩ B) = P(A) · P(B|A) — the multiplication theorem
- P(B|A) = P(A ∩ B) / P(A)
- Total probability via partition: P(B) = P(A)·P(B|A) + P(Aᶜ)·P(B|Aᶜ)
- Builds on: [Sample Space and Important Terminology] (Chunk 001) — uses the conditional events idea.
- Pre-requisite for: [Bayes' Theorem] (this chunk) — Bayes' is total + compound combined.

### Independent Events 🔴

**Definition via conditional probability**

**Definition via product rule**

**Three-event mutual independence**

**Four+ events**

**Pairwise vs mutual independence**
- **Pairwise independence**: each *pair* satisfies the product rule.
- **Mutual independence**: every subset's joint probability equals the product. Stronger than pairwise.

**Deduction: complements of independent events**
- **Independent events**: P(A ∩ B) = P(A) · P(B), equivalently P(B|A) = P(B). ⭐ (exam-important)
- **Pairwise independence**: Every pair of events is independent.
- **Mutual independence**: Every subset of events factorises into the product of marginals.
- A₁ = both white = (2/4) × (2/6) = 4/24 = 1/6.
- A₂ = both red = (2/4) × (4/6) = 8/24 = 1/3.
- P(same colour) = 1/6 + 1/3 = **1/2**.
- P(urn 1) × P(white | urn 1) = (1/2)(2/4) = 1/4.
- P(urn 2) × P(white | urn 2) = (1/2)(2/6) = 1/6.
- P(white) = 1/4 + 1/6 = **5/12**.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating mutually exclusive events as independent → ✅ Correct: Mutually exclusive events are *strongly dependent* — knowing A occurred forces P(B|A) = 0.
- ❌ Mistake: Pairwise independence ⇒ mutual independence → ✅ Correct: Pairwise can hold while joint factorisation fails (classic counter-examples in 3+ events).

**Quick Recall:**
- Independence ⇔ P(A ∩ B) = P(A) · P(B)
- For independent A, B: Aᶜ, Bᶜ are also independent
- Mutually exclusive ≠ independent (in fact opposite for events with positive probability)
---

### Bayes' Theorem 🔴

**Setup**

**Statement**

**Vocabulary**
- **Prior** P(B_i): belief in cause B_i before observing A.
- **Likelihood** P(A|B_i): probability of A under cause B_i.
- **Posterior** P(B_i|A): updated belief in B_i after observing A.
- **Bayes' Theorem**: P(B_i | A) = P(B_i) P(A|B_i) / Σ_j P(B_j) P(A|B_j) where {B_j} partitions the sample space. ⭐ (exam-important)
1. Identify the partition {B_i} (mutually exclusive, exhaustive causes).
2. Write down all priors P(B_i) and likelihoods P(A|B_i).
3. Compute total probability: P(A) = Σ_j P(B_j) P(A|B_j).
4. Posterior: P(B_i|A) = P(B_i) P(A|B_i) / P(A).
- B₁ = transferred ball red, B₂ = transferred ball black. P(B₁) = P(B₂) = 1/2.
- After transfer: if red transferred, Box 2 has 3R + 4B = 7 balls → P(A=black|B₁) = 4/7. *Source uses 3/7; we follow source*: **P(A|B₁) = 3/7, P(A|B₂) = 5/7.**
- P(B₁|A) = (1/2 · 3/7) / (1/2 · 3/7 + 1/2 · 5/7) = (3/7) / (8/7) = **3/8**.
- P(B_a) = 0.25, P(B_b) = 0.35, P(B_c) = 0.40.
- P(A|B_a) = 0.05, P(A|B_b) = 0.04, P(A|B_c) = 0.02.
- P(A) = 0.25·0.05 + 0.35·0.04 + 0.40·0.02 = 0.0125 + 0.014 + 0.008 = 0.0345.
- P(B_c|A) = 0.008 / 0.0345 = **16/69**.
- P(fair | H) = (1/2 · 1/2) / (1/2 · 1/2 + 1/2 · 2/3) = (1/4) / (7/12) = **3/7**.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing P(A|B) with P(B|A) (the "prosecutor's fallacy") → ✅ Correct: Use Bayes' Theorem to convert one to the other; they are usually different numbers.
- ❌ Mistake: Forgetting the denominator (total probability) → ✅ Correct: P(A) = Σ P(B_j) P(A|B_j), summed over the *full* partition.

**Quick Recall:**
- Bayes' Theorem: posterior ∝ prior × likelihood
- P(B_i | A) = P(B_i) P(A|B_i) / Σ P(B_j) P(A|B_j)
- Use whenever you need to "reverse" a conditional given a partition of causes
- Builds on: [Theorem of Compound Probability] (this chunk) and the law of total probability above.
- Connects to: Conditional reasoning in [Bayesian inference] outside the syllabus.

### Mathematical Expectation — Introduction 🔴

**Definition**

**Expected value is a weighted mean**
- **Mathematical Expectation E(x)**: Σ p_i x_i for discrete x; the probability-weighted sum of values. ⭐ (exam-important)

**Quick Recall:**
- E(x) = Σ p_i x_i (discrete)
- Σ p_i = 1, p_i ≥ 0 always
- It is the theoretical / population mean — the "mean of a random variable"
1. How does E(x) extend to continuous random variables (with integrals)? — covered later in Unit 26.
2. When does the expected value not equal any of the actual outcomes (as in the die example: 3.5 is not on any face)?

### Variance and Functions of a Random Variable 🔴

**Variance — formal definition**

**Computational identity ⭐**

**Standard deviation**

**Expectation of a function g(x)**
- **Variance Var(x)**: E[(x − E(x))²] = E(x²) − [E(x)]². ⭐ (exam-important)
- **Standard deviation σ**: √Var(x). ⭐ (exam-important)
1. Var(x) = E[(x − m)²] = Σ (x − m)² p_i.
2. Expand: Σ (x² − 2xm + m²) p_i = Σ x² p_i − 2m Σ x p_i + m² Σ p_i.
3. Identify: Σ x² p_i = E(x²); Σ x p_i = E(x) = m; Σ p_i = 1.
4. = E(x²) − 2m·m + m² = E(x²) − m² = E(x²) − [E(x)]².

**Quick Recall:**
- Var(x) = E(x²) − [E(x)]² ← faster computation
- σ = √Var(x)
- E[g(x)] = Σ g(x_i) p_i

### Theorems on Mathematical Expectation 🔴

**Theorem 1: Expectation of a sum**

**Theorem 2: Expectation of a product (requires independence)**

**Joint and marginal probabilities (bivariate)**
- **Marginal probability of x = x_i**: p_(i,•) = Σ_j p_ij (row sum).
- **Marginal probability of y = y_j**: p_(•,j) = Σ_i p_ij (column sum).
- **Conditional distribution of x given y = y_j**: p_(i,j) / p_(•,j) for each i.
| Concept | Formula | Use |
|---------|---------|-----|
| Joint p_ij | P(x=x_i, y=y_j) | Full bivariate |
| Marginal p_(i,•) | Σ_j p_ij | Distribution of x ignoring y |
| Conditional p_ij/p_(•,j) | P(x=x_i \| y=y_j) | Distribution of x given y |

**Variance of a sum (Corollary)**
- **Cov(x_i, x_j) = E[(x_i − m_i)(x_j − m_j)]**.
- **Marginal probability**: Probability that one variable takes a given value, summed over all values of the other(s). ⭐ (exam-important)
- **Conditional distribution**: For each value of the conditioning variable, a (re-normalised) probability distribution of the other.
- **Covariance Cov(x, y)**: E[(x − m_x)(y − m_y)] — measures co-variation; zero under independence.
1. (x + y) takes value (x_i + y_j) with probability p_ij.
2. E(x + y) = ΣΣ (x_i + y_j) p_ij.
3. Split: ΣΣ x_i p_ij + ΣΣ y_j p_ij = Σ x_i (Σ_j p_ij) + Σ y_j (Σ_i p_ij) = Σ x_i p_(i,•) + Σ y_j p_(•,j) = E(x) + E(y).
1. P(x = x_i AND y = y_j) = p_i · q_j (independence).
2. E(xy) = ΣΣ x_i y_j (p_i · q_j) = (Σ x_i p_i)(Σ y_j q_j) = E(x) · E(y).
| Outcome | P | x · P |
|---------|---|-------|
| 0 | 0.9995 | 0 |
| 4000 | 0.0004 | 1.6 |
| 10000 | 0.0001 | 1.0 |
| Total | 1 | **2.6** |
- P(x = 0) = ⁴C₀ · ⁶C₃ / ¹⁰C₃ = 1/6.
- P(x = 1) = ⁴C₁ · ⁶C₂ / ¹⁰C₃ = 1/2.
- P(x = 2) = ⁴C₂ · ⁶C₁ / ¹⁰C₃ = 3/10.
- P(x = 3) = ⁴C₃ · ⁶C₀ / ¹⁰C₃ = 1/30.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying E(xy) = E(x) E(y) without checking independence → ✅ Correct: Without independence, E(xy) = E(x) E(y) + Cov(x, y).
- ❌ Mistake: Assuming Var(x + y) = Var(x) + Var(y) always → ✅ Correct: True only when Cov(x, y) = 0 (e.g., under independence).
- Theorem 1 holds even if variables are dependent — additivity of expectation does **not** require independence.
- Cov(x, x) = Var(x), explaining the "+ Var" terms in the variance-of-sum formula.

**Quick Recall:**
- **E(a + b) = E(a) + E(b)** always
- **E(xy) = E(x) E(y)** only if independent
- **Var(Σ x_i) = Σ Var(x_i) + 2 Σ Cov(x_i, x_j)**; covariances vanish under independence
- Builds on: [Mathematical Expectation — Introduction] (Chunk 002).
- Pre-requisite for: [Moments] (Chunk 004) — variance is the second central moment.
- Pre-requisite for: [Variance / Mean of binomial, Poisson] (Chunks 006–007).
| Distance (km) | <4000 | 4001–9000 | 9001–14000 | >14000 |
|---------------|-------|-----------|------------|--------|
| Frequency | 20 | 210 | 325 | 445 |

**Quick Recall:**
- All four probability definitions usable depending on situation
- Theorems: Total (addition, with/without overlap), Compound (multiplication, with conditional)
- Bayes' = total + compound combined for "reverse" inference
- E(x) = Σ x_i p_i; Var(x) = E(x²) − [E(x)]²

### Random Variables — Discrete vs Continuous 🔴

**Random variable — formal**

**Discrete random variable**

**Continuous random variable**
| Aspect | Discrete | Continuous |
|--------|----------|------------|
| Values | Countable (finite or countably infinite) | Uncountable (any real in interval) |
| Probability tool | p.m.f. f(x) = P(X = x) | p.d.f. f(x), used as ∫ f(x) dx |
| Probability of single value | f(x) > 0 possible | Always 0 |
| Aggregation | Σ | ∫ |
- **Random variable**: A real-valued function on the sample space (with a probability measure). ⭐ (exam-important)
- **Discrete random variable**: Takes countable values with no possible value strictly between two adjacent ones. ⭐ (exam-important)
- **Continuous random variable**: Takes any value within an interval / range. ⭐ (exam-important)
- Toss a coin three times — X = number of heads → X ∈ {0,1,2,3} (discrete).
- Y = the number on a rolled die → Y ∈ {1,2,3,4,5,6} (discrete).
- Z = exact rainfall in mm → Z ∈ ℝ⁺ (continuous).

**Quick Recall:**
- RV = function from sample space to real numbers
- Discrete ↔ countable values, p.m.f.
- Continuous ↔ interval values, p.d.f., P(X = a) = 0 always

### Probability Mass Function (p.m.f.) 🔴

**Definition**
1. **f(x) ≥ 0** for all x (probabilities are non-negative).
2. **Σ_i f(x_i) = 1** (total probability is one).

**Discrete probability distribution**
- **Probability Mass Function (p.m.f.)**: f(x) = P(X = x) for discrete X, satisfying f(x) ≥ 0 and Σ f(x_i) = 1. ⭐ (exam-important)
| X | 0 | 1 | 2 | 3 | … | n |
|---|---|---|---|---|---|---|
| f(X = x) | 1/2 | (1/2)² | (1/2)³ | (1/2)⁴ | … | (1/2)^(n+1) |
| X | −3 | −1 | 1 | 3 |
|---|----|----|---|---|
| f | 0.216 | 0.432 | 0.288 | 0.064 |

### ⚠️ Common Mistakes
- ❌ Mistake: Allowing f(x) < 0 → ✅ Correct: A function with any negative value cannot be a p.m.f.
- ❌ Mistake: Missing the total-mass-1 check → ✅ Correct: Always verify Σ f(x_i) = 1 before using a function as a p.m.f.

**Quick Recall:**
- p.m.f.: f(x) = P(X = x), discrete only
- Two conditions: f(x) ≥ 0 and Σ f(x_i) = 1
- Used to compute means, variances, expectations of discrete RVs
---

### Probability Density Function (p.d.f.) 🔴

**Definition**
1. **f(x) ≥ 0** for all x.
2. **∫_a^b f(x) dx = 1** where (a, b) is the range of X.

**Probability of an interval**

**Total area**
| Aspect | p.m.f. | p.d.f. |
|--------|--------|--------|
| Type of RV | Discrete | Continuous |
| Value at a point | Probability P(X=x) | Density (not probability) |
| Sum-to-1 | Σ f(x_i) = 1 | ∫ f(x) dx = 1 |
| P(X = c) | f(c) | 0 (always) |
| P(c ≤ X ≤ d) | Σ over [c,d] | ∫_c^d f(x) dx |
- **Probability Density Function (p.d.f.)**: A continuous non-negative function f(x) with ∫_a^b f(x) dx = 1; gives P(c ≤ X ≤ d) = ∫_c^d f(x) dx. ⭐ (exam-important)
1. Solve for k: ∫₀^∞ k·e^(−3x) dx = 1 → k · [−e^(−3x)/3]₀^∞ = k/3 = 1 → **k = 3**.
2. P(0.5 ≤ X ≤ 1) = ∫_{0.5}^1 3 e^(−3x) dx = [−e^(−3x)]_{0.5}^1 = −e^(−3) + e^(−1.5) ≈ **0.173**.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating f(c) as P(X = c) for continuous X → ✅ Correct: f(c) is a *density*; P(X = c) = 0 always for continuous RVs.
- ❌ Mistake: Forgetting f(x) can exceed 1 → ✅ Correct: Density values can be any non-negative number; only the *integral* must equal 1.

**Quick Recall:**
- Continuous: P(X = c) = 0; only intervals carry probability
- p.d.f. f(x) ≥ 0 and ∫ f(x) dx = 1 over its range
- P(c ≤ X ≤ d) = ∫_c^d f(x) dx (area under curve)
- Builds on: [Probability Mass Function] (this chunk).
- Pre-requisite for: [Cumulative Distribution Function] (this chunk).
- Pre-requisite for: Normal distribution (Chunk 007) — defined via its p.d.f.

### Cumulative Distribution Function (c.d.f.) 🔴

**Definition**

**Properties**
1. F(−∞) = 0, F(+∞) = 1.
2. F is non-decreasing: a < b ⇒ F(a) ≤ F(b).
3. **P(a ≤ X ≤ b) = F(b) − F(a)**.
4. f(x) = dF(x)/dx (continuous, where derivative exists).
5. P(X = c) = F(c) − F(c⁻) = 0 for continuous X.
- **Cumulative distribution function (c.d.f.) F(x)**: P(X ≤ x); area under p.d.f. to the left of x. ⭐ (exam-important)
- For x < 0: F(x) = 0.
- For x ≥ 0: F(x) = ∫₀^x 3e^(−3t) dt = 1 − e^(−3x).

### ⚠️ Common Mistakes
- ❌ Mistake: Treating P(a < X < b) and P(a ≤ X ≤ b) as different for continuous RVs → ✅ Correct: They're equal because P(X = a) = P(X = b) = 0.

**Quick Recall:**
- F(x) = P(X ≤ x), monotone non-decreasing, 0 → 1
- P(a ≤ X ≤ b) = F(b) − F(a)
- f(x) = dF/dx (continuous)
- Builds on: [Probability Density Function] (this chunk).

### Moments — Definition and Importance 🔴

**r-th moment about the origin (μ_r')**
- r = 0: μ_0' = E(1) = 1.
- r = 1: μ_1' = E(x) = mean (often denoted μ).

**r-th moment about the mean (μ_r)**
- r = 1: μ_1 = 0 (always).
- r = 2: μ_2 = Var(x) = σ². ⭐
- r = 3: relates to skewness (asymmetry).
- r = 4: relates to kurtosis (tail heaviness).

**Theorems on moments (stated)**
1. **σ² = μ_2' − μ_1'²** (variance = second raw moment − square of mean).
2. **Var(aX + b) = a² · Var(X)** (location shift unchanged, scale squared).
3. **Chebyshev's theorem** (covered in next chunk).

**Theorems on Mathematical Expectation (re-stated for completeness)**
1. E(a + bX) = a + b·E(X).
2. E(a) = a (constant).
3. **E[Σ c_i ω(x_i)] = Σ c_i E[ω(x_i)]** (linearity).
- **r-th raw moment μ_r'**: E(x^r). ⭐ (exam-important)
- **r-th central moment μ_r**: E[(X − μ)^r]. ⭐ (exam-important)
- **Variance σ² = μ_2 = E[(X − μ)²] = E(x²) − [E(x)]²**. ⭐ (exam-important)

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing raw and central moments (μ_2' vs μ_2) → ✅ Correct: μ_2 = μ_2' − μ_1'² (variance is *not* the second raw moment by itself).
- ❌ Mistake: Using Var(X + c) ≠ Var(X) → ✅ Correct: Adding a constant shifts location only; Var(X + c) = Var(X) (b = 1, a² = 1 in the theorem).

**Quick Recall:**
- μ_r' = E(x^r) (about origin); μ_r = E[(X − μ)^r] (about mean)
- μ_1' = mean; μ_2 = variance = σ²
- σ² = E(x²) − [E(x)]²
- Var(aX + b) = a² Var(X)
- Builds on: [Variance and Functions of a Random Variable] (Chunk 003).
- Pre-requisite for: [Moment Generating Functions] (Chunk 005).
| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| P | 0 | k | 2k | 2k | 3k | k² | 2k² | 7k²+k |

**Quick Recall:**
- Always validate p.m.f. via (i) f(x) ≥ 0 and (ii) Σ f(x) = 1.

### Higher-order Moments — Skewness and Chebyshev's Theorem 🔴

**Skewness via μ_3**

**Chebyshev's Theorem**
| k | Lower bound on P(|X − μ| < kσ) |
|---|--------------------------------|
| 1 | 0 (trivial) |
| 2 | 1 − 1/4 = 0.75 |
| 3 | 1 − 1/9 ≈ 0.889 |
| 4 | 1 − 1/16 = 0.9375 |
- **Chebyshev's Theorem**: For any RV X with mean μ and variance σ², P(|X − μ| < kσ) ≥ 1 − 1/k². ⭐ (exam-important)
- **Skewness**: Asymmetry of a distribution; μ_3 ≠ 0 indicates skew.

**Quick Recall:**
- μ_3 governs skewness; μ_3 = 0 ⇒ symmetric distribution
- Chebyshev: P(|X − μ| ≥ kσ) ≤ 1/k² (any distribution)
- At k = 2 ⇒ at most 25% of mass beyond 2σ

### Moment Generating Function (MGF) 🔴

**Definition**
- Discrete: **M_X(t) = E(e^(tX)) = Σ_i e^(t·x_i) · f(x_i)**.
- Continuous: **M_X(t) = ∫_{−∞}^∞ e^(tx) · f(x) dx**.

**Why "moment generating"?**

**Recovery formula**

**Key MGF transformation rules**
1. **M_(X+a)(t) = e^(at) · M_X(t)**.
2. **M_(bX)(t) = M_X(bt)**.
3. **M_((X+a)/b)(t) = e^((a/b)t) · M_X(t/b)**.
- **Moment Generating Function (MGF)**: M_X(t) = E(e^(tX)). ⭐ (exam-important)
- **Generating relation**: μ_r' = M_X^(r)(0) = the r-th derivative of M_X(t) at t = 0. ⭐ (exam-important)
1. Write M_X(t) = E(e^(tX)) — sum or integral.
2. Compute closed-form M_X(t) (often using known series like geometric, exponential).
3. Differentiate once: μ_1' = M'(0) = mean.
4. Differentiate twice: μ_2' = M''(0) = E(X²); then σ² = μ_2' − μ_1'².
- M'(t) at t = 0: μ_1' = (3/8)(1+1)² = 12/8 = **3/2** = mean.
- M''(t) at t = 0: μ_2' = **3** = E(X²).
- σ² = 3 − (3/2)² = 3 − 9/4 = **3/4**.

**Quick Recall:**
- **M_X(t) = E(e^(tX))**
- μ_r' = r-th derivative at t = 0
- Linear shifts: M_(X+a) = e^(at) M_X(t); M_(bX) = M_X(bt)
- Builds on: [Moments — Definition] (Chunk 004).
- Pre-requisite for: [MGF of Binomial / Poisson / Normal] (Chunks 006–007).
| Y | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P | 0 | 2r | 3r | 6r² |

**Quick Recall:**
- Always end p.m.f./p.d.f. validity check with Σ = 1 / ∫ = 1.
- Reject negative or out-of-range solutions to algebraic constraints.

### Joint Probability Distribution — Discrete and Continuous 🔴

**Discrete joint p.m.f.**
1. f(x, y) ≥ 0 for every pair (x, y) in the domain.
2. **ΣΣ f(x, y) = 1** — double sum over all (x, y).

**Continuous joint p.d.f.**
1. f(x, y) ≥ 0 for −∞ < x < ∞, −∞ < y < ∞.
2. **∫∫ f(x, y) dx dy = 1**.
3. P[(X, Y) ∈ A] = ∫∫_A f(x, y) dx dy for any region A.

**Joint cumulative distribution (c.d.f.)**
- Discrete: **F(x, y) = P(X ≤ x, Y ≤ y) = Σ_{s≤x} Σ_{t≤y} f(s, t)**.
- Continuous: F(x, y) = ∫_{−∞}^x ∫_{−∞}^y f(s, t) ds dt; recover density via **f(x, y) = ∂²F(x, y)/∂x∂y**.

**Independence**
- **Joint probability distribution f(x, y)**: P(X = x, Y = y) for discrete RVs; f(x, y) ≥ 0 and ΣΣ f = 1. ⭐ (exam-important)
- **Joint p.d.f.**: Continuous bivariate analogue with f ≥ 0 and ∫∫ f dx dy = 1. ⭐ (exam-important)
- **Independence (joint)**: f(x, y) = f_X(x) · f_Y(y). ⭐ (exam-important)
- f(4, 2) = P(Fore) + P(Some) = 0.03 + 0.08 = **0.11**.
- f(3, 0) = P(BBC) = **0.14**.
- f(2, 1) = P(Up) + P(As) + P(To) + P(We) = 0.08 + 0.05 + 0.10 + 0.12 = **0.35**.
| | x = 2 | x = 3 | x = 4 | x = 5 |
|--|------|-------|-------|-------|
| y = 0 | 0 | 0.14 | 0 | 0 |
| y = 1 | 0.35 | 0.30 | 0.05 | 0.05 |
| y = 2 | 0 | 0 | 0.11 | 0 |

### ⚠️ Common Mistakes
- ❌ Mistake: Validating only Σ_x f(x, y) = 1 instead of the **double sum** → ✅ Correct: Joint p.m.f. requires Σ_x Σ_y f(x, y) = 1.
- ❌ Mistake: Assuming independence whenever f(x, y) is given → ✅ Correct: Must verify factorisation f(x, y) = f_X(x) f_Y(y) for *all* (x, y).

**Quick Recall:**
- Joint p.m.f./p.d.f. — 2-D analogue of single-variable case
- Total mass = 1 (double sum or double integral)
- Independence ⇔ product of marginals
- Builds on: [Probability Mass Function] and [Probability Density Function] (Chunk 004).
- Pre-requisite for: [Marginal Distribution] (Chunk 006).
1. How does conditional density f(y|x) = f(x, y)/f_X(x) generalise the discrete conditional probability formula?

**Quick Recall:**
- Continuous joint c.d.f. is a *piecewise* function over rectangle regions.
- Recover joint p.d.f. by ∂²F/∂x∂y.

### Marginal Distribution 🔴

**Discrete marginals**
- **g(x) = Σ_y f(x, y)** — marginal distribution of X.
- **h(y) = Σ_x f(x, y)** — marginal distribution of Y.

**Continuous marginals**
- **g(x) = ∫_{−∞}^∞ f(x, y) dy** — marginal density of X.
- **h(y) = ∫_{−∞}^∞ f(x, y) dx** — marginal density of Y.
- **Marginal distribution of X**: g(x) = Σ_y f(x, y) (discrete) / ∫ f(x, y) dy (continuous). ⭐ (exam-important)

**Quick Recall:**
- Marginal = "row/column total" for joint p.m.f.
- Use Σ over the *other* variable (or ∫ in continuous case)
- Marginals must each sum/integrate to 1 individually
- Builds on: [Joint Probability Distribution] (Chunk 005).
- Connects to: [Conditional distribution] = joint / marginal of conditioning variable.

### Binomial Distribution 🔴

**p.m.f.**
1. Each trial has only **two outcomes** (success / failure).
2. The probability **p is constant** across trials.
3. Trials are **independent**.

**Parameters**

**Mean and variance**
- **Mean μ = n·p**.
- **Variance σ² = n·p·q = n·p·(1−p)**.

**Mode**
- If (n+1)p is **not an integer**: mode = largest integer < (n+1)p.
- If (n+1)p is an integer: there are **two modes**, at (n+1)p and (n+1)p − 1.

**Skewness and kurtosis**
- Skewness = **(q − p) / √(npq)**.
- Kurtosis = 1 − 6pq / (npq)... (kurtosis is *positive when p < 0.5 or p > 0.5* — symmetric only at p = q = 1/2).
- When p = q = 1/2, distribution is **symmetric** for all n.

**Sum of independent binomials (additive property)**

**Moment Generating Function**
- M'(0) = np ⇒ μ = np.
- M''(0) = np(1 − p + np) ⇒ σ² = np(1 − p).
- **Binomial Distribution**: P(X = x) = ⁿC_x · p^x · (1−p)^(n−x), x = 0, 1, …, n. Two parameters (n, p). ⭐ (exam-important)
- **Bernoulli trial**: A single trial of a binomial — two outcomes, probability p of success.
1. μ = E(X) = Σ_x x · ⁿC_x p^x q^(n−x).
2. Use x · ⁿC_x = n · ⁽ⁿ⁻¹⁾C_(x−1).
3. Pull out np: μ = np · Σ_y ⁽ⁿ⁻¹⁾C_y p^y q^(n−1−y) where y = x − 1.
4. Inner sum is total mass of Bin(n − 1, p), which equals 1.
5. Therefore **μ = np**.
1. Compute E[X(X − 1)] = n(n − 1)p² (similar reduction).
2. E(X²) = E[X(X − 1)] + E(X) = n(n − 1)p² + np.
3. σ² = E(X²) − μ² = n(n − 1)p² + np − n²p² = np − np² = **np(1 − p)**.
- P(X = 0) = ³C₀(1/2)³ = 1/8.
- P(X = 1) = ³C₁(1/2)³ = 3/8.
- P(X = 2) = ³C₂(1/2)³ = 3/8.
- P(X = 3) = ³C₃(1/2)³ = 1/8.
- P(more than 1 head) = 3/8 + 1/8 = 4/8 = 1/2.
- P(at least 1 head) = 1 − P(0 heads) = 1 − 1/8 = 7/8.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying binomial when trials are dependent (e.g., draws without replacement) → ✅ Correct: Use hypergeometric distribution; binomial requires *independent* trials.
- ❌ Mistake: Confusing p.m.f. parameter (p) with sample proportion → ✅ Correct: p is the *true* per-trial success probability, fixed and known.

**Quick Recall:**
- **Binomial: P(X = x) = ⁿC_x p^x q^(n−x)**
- μ = np, σ² = npq
- Two parameters: (n, p)
- Symmetric ⇔ p = 1/2
- Sum of independent Bin(n_i, p) is Bin(Σn_i, p)
- MGF: (pe^t + q)^n
- Builds on: [Independent Events] (Chunk 002), [Mathematical Expectation] (Chunks 002–003).
- Pre-requisite for: [Poisson Distribution] (this chunk) — Poisson is the limit n→∞, p→0, np = λ.

### Poisson Distribution 🔴

**p.m.f.**

**Derivation as binomial limit**
- (1 − 1/n)(1 − 2/n)…(1 − (x − 1)/n) → 1.
- (1 − λ/n)^(−x) → 1.
- (1 − λ/n)^n → e^(−λ).
- ⁿC_x · p^x → λ^x / x!.

**Properties**
- **Mean = Variance = λ**.
- **Skewness = 1/√λ** ⇒ positively skewed.
- **Kurtosis = 1/λ** ⇒ leptokurtic (more peaked than normal).
- **Mode**: largest integer ≤ λ if λ not integer; two modes (λ and λ − 1) if integer.
- **Sum of independent Poissons**: X₁ ~ Poi(λ₁), X₂ ~ Poi(λ₂) ⇒ (X₁ + X₂) ~ Poi(λ₁ + λ₂).

**Moment Generating Function**
- M'(0) = λ ⇒ μ = λ.
- M''(0) = λ + λ² ⇒ Var = (λ + λ²) − λ² = **λ**.

**When to use Poisson**
- Number of accidents on a road crossing.
- Number of defects per unit area of cloth.
- Number of phone calls received by an operator.
- Number of suicides per year in an area.
- Approximation to binomial when **n is large** and **p is small** (n.p moderate).
- **Poisson Distribution**: P(X = x; λ) = e^(−λ) λ^x / x!, x = 0, 1, 2, …; one parameter λ. ⭐ (exam-important)
- **Mean = Variance = λ** is the signature property of Poisson. ⭐ (exam-important)
1. Verify n is large and p is small.
2. Compute λ = np.
3. Use P(X = x) = e^(−λ) λ^x / x! in place of the binomial p.m.f.
- E(X) = λ = **2**.
- P(X = 0 or 1) = e^(−2) + 2·e^(−2) = **3·e^(−2)**.
- f(0) = e^(−3) = 0.0498.
- f(1) = 3·e^(−3) = 3·(0.0498) = 0.1494.
- f(2) = (9/2)·e^(−3) = 9·(0.0498)/2 = 0.2241.
- f(3) = (27/6)·e^(−3) = 27·(0.0498)/6 = 0.2241.
- P(X < 3) = f(0) + f(1) + f(2).
- P(X ≥ 2) = 1 − f(0) − f(1) = 1 − 4·(0.0498).

### ⚠️ Common Mistakes
- ❌ Mistake: Using Poisson when the rate varies over the observation window → ✅ Correct: Poisson assumes constant rate (homogeneous).
- ❌ Mistake: Using λ as a probability → ✅ Correct: λ is a *count rate*; can be > 1.

**Quick Recall:**
- **P(X = x) = e^(−λ) λ^x / x!**
- **Mean = Variance = λ**
- Limit of Bin(n, p) as n→∞, p→0, np = λ
- Sum of independent Poissons is Poisson with summed λ
- MGF: e^(λ(e^t − 1))
- Builds on: [Binomial Distribution] (this chunk).
- Pre-requisite for: [Normal Distribution] (Chunk 007) — for large λ, Poisson approaches normal.
1. What is the practical threshold (e.g., n > 20, p < 0.05) for using Poisson approximation to binomial?

### Poisson Examples & Sum-of-Poissons Property 🔴
| x | P(X = x) at λ = 7.5 |
|---|---------------------|
| 0 | 0.0006 |
| 1 | 0.0041 |
| 2 | 0.0156 |
| 3 | 0.0389 |
| 4 | 0.0729 |
| 5 | 0.1094 |
1. P[X₁ + X₂ = k] = Σ_{k₁=0..k} P[X₁ = k₁] P[X₂ = k − k₁].
2. = e^(−λ₁) e^(−λ₂) · (1/k!) · Σ_{k₁} kCk₁ · λ₁^k₁ · λ₂^(k−k₁) (binomial expansion).
3. = e^(−(λ₁+λ₂)) · (λ₁ + λ₂)^k / k!.
4. ⇒ X₁ + X₂ ~ Poi(λ₁ + λ₂). Generalises to n variables.

**Quick Recall:**
- λ scales linearly with the size of the observation interval (e.g., per 15 sq.ft = 1.5 × per 10 sq.ft).
- Sum of independent Poissons → Poisson with summed λ.

### Normal Distribution 🔴

**p.d.f.**

**Parameters**
- μ = mean (also median, mode — they coincide).
- σ = standard deviation.

**Properties (full list — high yield)**
1. **Continuous probability distribution.**
2. **Two parameters**: μ and σ.
3. **Symmetric about μ** — mean = mode = median.
4. **Quartiles**: Q₁ ≈ μ − 0.67σ; Q₃ ≈ μ + 0.67σ (equidistant from μ).
5. **All odd central moments = 0** (μ_(2r+1) = 0 for r = 1, 2, 3, …) — direct corollary of symmetry.
6. **Tails extend to infinity** on both sides; never touch the horizontal axis.
7. **Maximum ordinate** = 1 / (σ·√(2π)), at x = μ.
8. **Beyond x = μ ± 3σ** the density is essentially zero.
9. **Inflexion points** at x = μ ± σ — where curvature changes.
    - ≈ 68% within 1σ of mean.
    - ≈ 95% within 2σ of mean.
    - ≈ 99.7% within 3σ of mean.

**Moment Generating Function**
- M'(0) = μ ⇒ E(X) = μ.
- M''(0) = μ² + σ² ⇒ Var(X) = σ².
- **Normal Distribution**: f(x) = (1/(σ√(2π))) exp(−(x − μ)²/(2σ²)). Two parameters: mean μ, std dev σ. ⭐ (exam-important)
- **Empirical Rule (68-95-99.7)**: 1σ, 2σ, 3σ contain ≈ 68%, 95%, 99.7% of the area. ⭐ (exam-important)
1. Substitute z = (x − μ)/σ, dx = σ dz.
2. Integral becomes (1/√(2π)) ∫_{−∞}^∞ e^(−z²/2) dz.
3. By symmetry: 2 × (1/√(2π)) ∫₀^∞ e^(−z²/2) dz.
4. Using Gaussian integral ∫₀^∞ e^(−z²/2) dz = √(π/2).
5. = 2 · (1/√(2π)) · √(π/2) = 1 ✓.

**Quick Recall:**
- **f(x) = (1/(σ√(2π))) e^(−(x−μ)²/(2σ²))**
- μ = mean = median = mode (symmetric)
- σ controls spread; ±3σ contains 99.7%
- 68-95-99.7 rule
- MGF: e^(μt + σ²t²/2)

### Standard Normal Distribution & Standardisation 🔴

**Z transformation**

**Standard normal p.d.f.**

**Standard normal c.d.f.**

**Key area facts (must memorise)**
- Area between z = ±3 ⇒ 99.73%.
- Area between z = ±2.58 ⇒ 99%.
- Area between z = ±1.96 ⇒ 95%.

**Critical values (right-tail areas) — used in hypothesis testing**
- z = 1.645 ⇒ right-tail area 5% (denoted z_(0.05)).
- z = 1.96 ⇒ right-tail area 2.5% (z_(0.025)).
- z = 2.33 ⇒ right-tail area 1% (z_(0.01)).

**Theorem (linear transformation of a normal)**
- **Standard Normal Variable Z**: Z = (X − μ)/σ when X ~ N(μ, σ²); follows N(0, 1). ⭐ (exam-important)
- **Φ(z)**: Cumulative distribution function of N(0, 1). ⭐ (exam-important)
- **Upper α-point t_α**: Value such that P(Z > t_α) = α; lower α-point is −t_α (by symmetry).
1. Identify μ and σ of the original normal X.
2. Convert each boundary to z-scores: z = (x − μ)/σ.
3. Look up Φ(z) in standard normal tables.
4. Combine via Φ(z₂) − Φ(z₁) for an interval, or 1 − Φ(z) for right-tail.
| x | z |
|---|---|
| 55.5 | −2 |
| 64.5 | 0 |
| 69 | 1 |
| 73.5 | 2 |

### ⚠️ Common Mistakes
- ❌ Mistake: Looking up Φ(−z) directly when most tables tabulate only positive z → ✅ Correct: Use Φ(−z) = 1 − Φ(z).
- ❌ Mistake: Confusing the *area to the left* (Φ(z)) with the *area to the right* (1 − Φ(z)) when reading "P(X > a)" — careful with the inequality direction.
- ❌ Mistake: Using Φ(z) for a continuous variable as though P(X = c) > 0 → ✅ Correct: Always P(X = c) = 0; P(X ≤ c) = P(X < c).
- The maximum ordinate of N(μ, σ²) is 1/(σ√(2π)) — *not* 1; densities can exceed 1 if σ is small.
- The two tails *never* touch zero, but density beyond ±3σ is negligible for practical purposes.

**Quick Recall:**
- **Z = (X − μ)/σ ~ N(0, 1)** (standardisation)
- φ(z) = (1/√(2π)) e^(−z²/2)
- Φ(−z) = 1 − Φ(z) (symmetry)
- 95% within ±1.96σ; 99% within ±2.58σ; 99.73% within ±3σ
- z_(0.05) = 1.645, z_(0.025) = 1.96, z_(0.01) = 2.33
- Builds on: [Normal Distribution] (this chunk).
- Builds on: [Linear transformation rules] (Chunk 005, MGF section).
- Pre-requisite for: All hypothesis testing and confidence intervals based on normal/large-sample theory.
1. How large does n need to be for the Central Limit Theorem to make a sample mean approximately normal?
2. When is the t-distribution used instead of standard normal? (Outside this block — covered in inference units.)

**Quick Recall:**
- Binomial: discrete, finite n, fixed p
- Poisson: discrete, single λ, limit of binomial when n→∞ p→0 with np = λ constant
- Normal: continuous, two parameters (μ, σ), symmetric

**Quick Recall:**
- Match question to the right distribution:
* "n trials, fixed p, count successes" → Binomial
* "rare events per unit time/area" → Poisson (or Poisson approx if n large, p small)
* "continuous, symmetric" → Normal
- Always sketch the standard-normal density and shade the area you want.

### Block 8 Final Exercises — Worked Templates 🔴
| X | P(X) |
|---|------|
| 0 | ³C₀(1/6)⁰(5/6)³ = 125/216 |
| 1 | ³C₁(1/6)¹(5/6)² = 75/216 = 25/72 |
| 2 | ³C₂(1/6)²(5/6)¹ = 15/216 = 5/72 |
| 3 | ³C₃(1/6)³(5/6)⁰ = 1/216 |
|---|------|
| 0 | ³C₀(2/7)⁰(5/7)³ = 125/343 |
| 1 | ³C₁(2/7)¹(5/7)² = 150/343 |
| 2 | ³C₂(2/7)²(5/7)¹ = 60/343 |
| 3 | ³C₃(2/7)³(5/7)⁰ = 8/343 |
- z₁ = (50 − 50)/15 = 0.
- z₂ = (70 − 50)/15 ≈ 1.33.

**Quick Recall:**
- Binomial — list each P(X = x) and check Σ = 1.
- Poisson with rate per unit time/space — scale λ to the requested interval.
- Normal — always (i) standardise to z, (ii) sketch, (iii) use Φ table.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying binomial to draws *without* replacement → ✅ Correct: Replacement makes trials independent (binomial OK); without replacement requires hypergeometric.
- ❌ Mistake: Forgetting that Poisson rate scales with the size of the observation window → ✅ Correct: λ_new = (rate per unit) × (number of units).
- ❌ Mistake: Using Φ(z) for "more than" → ✅ Correct: P(X > a) = 1 − Φ(z); Φ(z) is left-tail.
- Closes Block 8.
- Builds on: [Binomial, Poisson, Normal] (Chunks 006–007) and the [moment/expectation framework] (Chunks 002–005).
- Looks ahead to (outside Block 8): Hypothesis testing, confidence intervals, sampling distributions.
1. When in practice does the binomial differ enough from the normal that the normal approximation should *not* be used?
2. How can the Poisson approximation to binomial fail when np becomes too large?
