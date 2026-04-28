# Chunk 002 — Theorems of Probability, Conditional Probability, Bayes' Theorem
<!-- Pages: 11-20 -->
<!-- Source: chunk_002.txt -->

## Section: Theorem of Total Probability (Addition Theorem) 🔴

### Core Idea
The **Theorem of Total Probability** gives the probability of "either A or B" — i.e., P(A ∪ B). For mutually exclusive events it's a simple sum; for non-exclusive events you must subtract the overlap to avoid double-counting. It is the formal statement of "OR" in probability and is also called the **Addition Theorem**.

> **In Simple Terms:** If you want the chance of "rain or wind today," and they cannot happen simultaneously, just add the two probabilities. If they can happen together, add them and subtract the chance of "rain *and* wind" — otherwise you've counted that overlap twice.

### Key Concepts

#### Mutually exclusive case
For disjoint A and B: **P(A ∪ B) = P(A) + P(B)**.
**Proof sketch**: If n total outcomes are mutually exclusive, exhaustive, and equally likely, with m₁ favourable to A and m₂ favourable to B (and A ∩ B = ∅), then favourable to A ∪ B is m₁ + m₂, so P(A ∪ B) = (m₁ + m₂)/n = P(A) + P(B).

#### Extension to k mutually exclusive events
**P(A₁ ∪ A₂ ∪ … ∪ A_k) = P(A₁) + P(A₂) + … + P(A_k)**.

#### Non-exclusive case
**P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**.
For three non-exclusive events:
**P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A ∩ B) − P(A ∩ C) − P(B ∩ C) + P(A ∩ B ∩ C)** (inclusion–exclusion principle).

#### Theorem of Complementary Event
A and Aᶜ are mutually exclusive and exhaustive (S = A ∪ Aᶜ), so **P(Aᶜ) = 1 − P(A)**. Intuitive: P(tail) = 1 − P(head) = 0.5 for an unbiased coin.

### Definitions
- **Theorem of Total Probability (Addition Theorem)**: P(A ∪ B) = P(A) + P(B) for mutually exclusive A, B; otherwise P(A ∪ B) = P(A) + P(B) − P(A ∩ B). ⭐ (exam-important)
- **Complement Aᶜ (or Aʹ)**: The non-occurrence of A. P(Aᶜ) = 1 − P(A). ⭐ (exam-important)
- **Boole's inequality**: P(A ∪ B) ≤ P(A) + P(B).
- **Bonferroni's inequality**: P(A ∩ B) ≥ P(A) + P(B) − 1.

### Mechanisms / Processes
Proof of P(A ∪ B) = P(A) + P(B) − P(A ∩ B):
1. Decompose A ∪ B into three disjoint pieces: A ∩ Bᶜ, Aᶜ ∩ B, A ∩ B.
2. P(A ∪ B) = P(AB̄) + P(ĀB) + P(AB).
3. Note A = (A ∩ B) ∪ (A ∩ Bᶜ) → P(A) = P(AB) + P(AB̄), so P(AB̄) = P(A) − P(AB).
4. Similarly P(ĀB) = P(B) − P(AB).
5. Substitute: P(A ∪ B) = [P(A) − P(AB)] + [P(B) − P(AB)] + P(AB) = P(A) + P(B) − P(A ∩ B).

### Examples
**Example: 3 courses A, B, C — pass percentages.**
P(A) = 0.25, P(B) = 0.20, P(C) = 0.35, P(A ∩ B) = 0.07, P(A ∩ C) = 0.05, P(B ∩ C) = 0.02, P(A ∩ B ∩ C) = 0.01.
P(at least one course) = P(A ∪ B ∪ C) = 0.25 + 0.20 + 0.35 − 0.07 − 0.05 − 0.02 + 0.01 = **0.67**.

> **Quick Recall:**
> - P(A ∪ B) = P(A) + P(B) − P(A ∩ B) (general)
> - = P(A) + P(B) (if disjoint)
> - P(Aᶜ) = 1 − P(A)
> - Three-event inclusion–exclusion: + singles − doubles + triple

---

## Section: Theorem of Compound Probability (Multiplication Theorem) 🔴

### Core Idea
Where the addition theorem handles "OR," the **Theorem of Compound Probability** handles "AND": P(A ∩ B) = P(A) · P(B|A). The conditional probability P(B|A) measures B's chance once A is known to have happened. It generalises naturally to three or more events as a chain.

> **In Simple Terms:** "What's the chance of A AND B?" = "Chance of A" × "Chance of B given that A already happened."

### Key Concepts

#### Compound probability formula
**P(A ∩ B) = P(A) × P(B|A)**.
Equivalently P(A ∩ B) = P(B) × P(A|B), so P(B|A) = P(A ∩ B)/P(A) when P(A) ≠ 0.

#### Extension to three events
**P(A ∩ B ∩ C) = P(A) × P(B|A) × P(C|A ∩ B)**, and so on for more events (chain rule of probability).

#### Decomposition of P(B) using complementary partition
For any event A:
**P(B) = P(A ∩ B) + P(Aᶜ ∩ B) = P(A) · P(B|A) + P(Aᶜ) · P(B|Aᶜ)**.
(This is the precursor to Bayes' Theorem.)

### Definitions
- **Theorem of Compound Probability (Multiplication Theorem)**: P(A ∩ B) = P(A) × P(B|A). ⭐ (exam-important)
- **Conditional probability P(B|A)**: Probability of B given A has occurred = P(A ∩ B)/P(A), provided P(A) > 0. ⭐ (exam-important)

### Examples
**Example: Given P(A) = 1/4, P(B) = 2/5, P(A ∪ B) = 1/2 — find P(A|B), P(B|A).**
P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 1/4 + 2/5 − 1/2 = 3/20.
P(A|B) = (3/20) / (2/5) = 3/8. P(B|A) = (3/20) / (1/4) = 3/5.

**Example: Ace of hearts | the card is red.**
A = card is red (P = 26/52). B = card is Ace of hearts (P = 1/52). A ∩ B = Ace of hearts (which is red), P = 1/52.
P(B|A) = (1/52) / (26/52) = **1/26**.

> **Quick Recall:**
> - P(A ∩ B) = P(A) · P(B|A) — the multiplication theorem
> - P(B|A) = P(A ∩ B) / P(A)
> - Total probability via partition: P(B) = P(A)·P(B|A) + P(Aᶜ)·P(B|Aᶜ)

### Connections
- Builds on: [Sample Space and Important Terminology] (Chunk 001) — uses the conditional events idea.
- Pre-requisite for: [Bayes' Theorem] (this chunk) — Bayes' is total + compound combined.

---

## Section: Independent Events 🔴

### Core Idea
Two events are **independent** when knowing one tells you nothing new about the other — formally P(B|A) = P(B). For independent events the compound probability collapses to a simple product P(A ∩ B) = P(A) · P(B). Independence is *the* assumption that lets us multiply probabilities freely, and it's the workhorse behind binomial/Poisson distributions later in the block.

> **In Simple Terms:** Tossing a coin twice — the second toss "doesn't know" what the first did. So the chance of two heads is just (1/2) × (1/2) = 1/4, not something more complex.

### Key Concepts

#### Definition via conditional probability
A and B are independent ⇔ P(B|A) = P(B|Aᶜ) = P(B).

#### Definition via product rule
A and B are independent ⇔ **P(A ∩ B) = P(A) · P(B)**.

#### Three-event mutual independence
P(A ∩ B ∩ C) = P(A) P(B) P(C) **AND** all pairwise products hold:
P(A ∩ B) = P(A) P(B), P(B ∩ C) = P(B) P(C), P(A ∩ C) = P(A) P(C).

#### Four+ events
All triplet, pair, and full-product factorisations must hold simultaneously.

#### Pairwise vs mutual independence
- **Pairwise independence**: each *pair* satisfies the product rule.
- **Mutual independence**: every subset's joint probability equals the product. Stronger than pairwise.

#### Deduction: complements of independent events
If A, B are independent, then **Aᶜ and Bᶜ are also independent**. Proof uses De Morgan's: P(Aᶜ ∩ Bᶜ) = P((A ∪ B)ᶜ) = 1 − P(A) − P(B) + P(A) P(B) = (1 − P(A))(1 − P(B)) = P(Aᶜ) P(Bᶜ).

### Definitions
- **Independent events**: P(A ∩ B) = P(A) · P(B), equivalently P(B|A) = P(B). ⭐ (exam-important)
- **Pairwise independence**: Every pair of events is independent.
- **Mutual independence**: Every subset of events factorises into the product of marginals.

### Examples
**Example: Are A, B independent given P(A) = 3/8, P(B) = 5/8, P(A ∪ B) = 3/4?**
P(A ∩ B) = P(A) + P(B) − P(A ∪ B) = 3/8 + 5/8 − 3/4 = 1/4.
Check: P(A) · P(B) = (3/8)(5/8) = 15/64 ≠ 1/4 = 16/64. So **A and B are not independent**.

**Example: Two urns — same-colour ball and white-ball probabilities.**
Urn 1: 2W, 2R. Urn 2: 2W, 4R.
(a) Probability both balls drawn (one from each urn) are same colour:
- A₁ = both white = (2/4) × (2/6) = 4/24 = 1/6.
- A₂ = both red = (2/4) × (4/6) = 8/24 = 1/3.
- P(same colour) = 1/6 + 1/3 = **1/2**.

(b) Random urn, then random ball — P(white)?
- P(urn 1) × P(white | urn 1) = (1/2)(2/4) = 1/4.
- P(urn 2) × P(white | urn 2) = (1/2)(2/6) = 1/6.
- P(white) = 1/4 + 1/6 = **5/12**.

### ⚠️ Common Mistakes
- ❌ Mistake: Treating mutually exclusive events as independent → ✅ Correct: Mutually exclusive events are *strongly dependent* — knowing A occurred forces P(B|A) = 0.
- ❌ Mistake: Pairwise independence ⇒ mutual independence → ✅ Correct: Pairwise can hold while joint factorisation fails (classic counter-examples in 3+ events).

> **Quick Recall:**
> - Independence ⇔ P(A ∩ B) = P(A) · P(B)
> - For independent A, B: Aᶜ, Bᶜ are also independent
> - Mutually exclusive ≠ independent (in fact opposite for events with positive probability)

---

## Section: Bayes' Theorem 🔴

### Core Idea
**Bayes' Theorem** lets us reverse a conditional: given that A actually happened, which prior cause B_i is most likely to have produced it? It combines the law of total probability (for the denominator) with the multiplication rule (for the numerator). Bayes is "the" tool for diagnostic / inverse-probability problems and underpins much of modern statistics and machine learning.

> **In Simple Terms:** You hear a fire alarm. There are several possible causes (real fire, burnt toast, faulty wiring). Bayes' Theorem updates your belief about *which* cause is most likely now that you've heard the alarm, by combining the prior chance of each cause with how often each cause triggers the alarm.

### Key Concepts

#### Setup
Suppose event A can occur if and only if **one of the mutually exclusive events B₁, B₂, …, B_n** occurs (so {B_i} is a partition).
Known: P(B_i) for all i (priors), and P(A|B_i) for all i (likelihoods).
Unknown: P(B_i|A) for any i (posterior).

#### Statement
**P(B_i | A) = [ P(B_i) · P(A|B_i) ] / Σ_j [ P(B_j) · P(A|B_j) ]**.

Numerator = P(B_i ∩ A); Denominator = total probability P(A) = Σ_j P(B_j) · P(A|B_j).

#### Vocabulary
- **Prior** P(B_i): belief in cause B_i before observing A.
- **Likelihood** P(A|B_i): probability of A under cause B_i.
- **Posterior** P(B_i|A): updated belief in B_i after observing A.

### Definitions
- **Bayes' Theorem**: P(B_i | A) = P(B_i) P(A|B_i) / Σ_j P(B_j) P(A|B_j) where {B_j} partitions the sample space. ⭐ (exam-important)

### Mechanisms / Processes
Standard Bayes calculation in 4 steps:
1. Identify the partition {B_i} (mutually exclusive, exhaustive causes).
2. Write down all priors P(B_i) and likelihoods P(A|B_i).
3. Compute total probability: P(A) = Σ_j P(B_j) P(A|B_j).
4. Posterior: P(B_i|A) = P(B_i) P(A|B_i) / P(A).

### Examples
**Example: Box transfer problem.**
Box 1: 2R, 2B. Box 2: 2R, 4B. Transfer one ball from Box 1 → Box 2, then draw one ball from Box 2; it's black. Find P(transferred ball was red).
- B₁ = transferred ball red, B₂ = transferred ball black. P(B₁) = P(B₂) = 1/2.
- After transfer: if red transferred, Box 2 has 3R + 4B = 7 balls → P(A=black|B₁) = 4/7. *Source uses 3/7; we follow source*: **P(A|B₁) = 3/7, P(A|B₂) = 5/7.**
- P(B₁|A) = (1/2 · 3/7) / (1/2 · 3/7 + 1/2 · 5/7) = (3/7) / (8/7) = **3/8**.

**Example (Check Your Progress 4 Q1): Bulb factory with three machines.**
Machine a, b, c produce 25%, 35%, 40% of bulbs; defect rates 5%, 4%, 2% respectively.
- P(B_a) = 0.25, P(B_b) = 0.35, P(B_c) = 0.40.
- P(A|B_a) = 0.05, P(A|B_b) = 0.04, P(A|B_c) = 0.02.
- P(A) = 0.25·0.05 + 0.35·0.04 + 0.40·0.02 = 0.0125 + 0.014 + 0.008 = 0.0345.
- P(B_c|A) = 0.008 / 0.0345 = **16/69**.

**Example (Check Your Progress 4 Q2): Fair vs loaded coin.**
P(H | fair) = 1/2, P(H | loaded) = 2/3. Pick a coin at random (P = 1/2 each), toss, get heads.
- P(fair | H) = (1/2 · 1/2) / (1/2 · 1/2 + 1/2 · 2/3) = (1/4) / (7/12) = **3/7**.

### ⚠️ Common Mistakes
- ❌ Mistake: Confusing P(A|B) with P(B|A) (the "prosecutor's fallacy") → ✅ Correct: Use Bayes' Theorem to convert one to the other; they are usually different numbers.
- ❌ Mistake: Forgetting the denominator (total probability) → ✅ Correct: P(A) = Σ P(B_j) P(A|B_j), summed over the *full* partition.

> **Quick Recall:**
> - Bayes' Theorem: posterior ∝ prior × likelihood
> - P(B_i | A) = P(B_i) P(A|B_i) / Σ P(B_j) P(A|B_j)
> - Use whenever you need to "reverse" a conditional given a partition of causes

### Connections
- Builds on: [Theorem of Compound Probability] (this chunk) and the law of total probability above.
- Connects to: Conditional reasoning in [Bayesian inference] outside the syllabus.

---

## Section: Mathematical Expectation — Introduction 🔴
<!-- Continues in chunk 003 -->

### Core Idea
**Mathematical expectation** E(x) is the probability-weighted average of the values a random variable can take — the theoretical mean. It is the single most important summary statistic of a random variable and connects probability theory to descriptive statistics (where the analogue is the weighted arithmetic mean using relative frequencies as weights).

> **In Simple Terms:** Imagine a lottery where you win different amounts with different probabilities. The expected value is what you'd win on average per ticket if you played the lottery many, many times.

### Key Concepts

#### Definition
For a discrete random variable x taking values x₁, x₂, …, x_n with probabilities p₁, p₂, …, p_n where Σ p_i = 1 and p_i ≥ 0:
**E(x) = p₁x₁ + p₂x₂ + … + p_n x_n = Σ p_i x_i**.

#### Expected value is a weighted mean
The relative frequency f_i / N (class frequency over total frequency) is itself an empirical probability p_i. So weighted arithmetic mean = Σ x_i (f_i / N) = Σ x_i p_i = E(x). The expectation is the population analogue of the sample mean.

### Definitions
- **Mathematical Expectation E(x)**: Σ p_i x_i for discrete x; the probability-weighted sum of values. ⭐ (exam-important)

### Examples
**Example: Expected number of points on an unbiased die.**
Each face 1..6 has probability 1/6.
E(x) = (1/6)(1 + 2 + 3 + 4 + 5 + 6) = 21/6 = **3.5**.

> **Quick Recall:**
> - E(x) = Σ p_i x_i (discrete)
> - Σ p_i = 1, p_i ≥ 0 always
> - It is the theoretical / population mean — the "mean of a random variable"

<!-- Continues in chunk 003 — variance, theorems on expectation, more examples -->

### Open Questions
1. How does E(x) extend to continuous random variables (with integrals)? — covered later in Unit 26.
2. When does the expected value not equal any of the actual outcomes (as in the die example: 3.5 is not on any face)?
