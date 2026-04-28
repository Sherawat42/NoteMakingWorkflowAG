# Chunk 008 — Unit 27 Summary, Key Words & Worked Exercises
<!-- Pages: 71-76 -->
<!-- Source: chunk_008.txt -->

## Section: Unit 27 Summary 🟢

### Core Idea
Unit 27 closes Block 8 by tying together the **joint and marginal distribution** machinery from Chunks 005–006 with the **three workhorse distributions** — **Binomial, Poisson, Normal** — covered in Chunks 006–007. Two are discrete (Binomial, Poisson); one is continuous (Normal). All three are characterised completely by their moments — which is why moments and MGFs were developed first.

> **In Simple Terms:** This is the unit that takes you from "what is a probability distribution?" to "here are the three distributions you'll meet in 95% of statistics problems."

### Definitions (Unit 27 Key Words — verbatim ⭐)

- **Binomial Distribution**: A discrete probability distribution satisfying:
  1) Finite repetition of identical trials.
  2) Each trial has two outcomes: success or failure.
  3) Trials are independent.
  4) Probability of outcomes does not change between trials.

- **Normal Distribution**: A continuous probability distribution with:
  1) Symmetry about the mean.
  2) Mean = Mode = Median.
  3) Variable can take any value in (−∞, ∞).

- **Poisson Distribution**: A discrete probability distribution that is the **limiting form of the binomial**, provided:
  1) Number of trials → ∞.
  2) Probability of success in each trial → 0.

- **Probability Distribution**: A statement specifying the set of possible values together with the respective probabilities.

> **Quick Recall:**
> - Binomial: discrete, finite n, fixed p
> - Poisson: discrete, single λ, limit of binomial when n→∞ p→0 with np = λ constant
> - Normal: continuous, two parameters (μ, σ), symmetric

---

## Section: Check Your Progress Solutions 🟡

### Examples

**CYP 1, Q1: Joint p.d.f. f(x, y) on x > 0, y > 0, 3x + y < 3 (else 0). Find marginals.**

Marginal of X:
g(x) = f_X(x) = ∫₀^(3−3x) 1 dy = 3 − 3x = **3(1 − x)** for 0 ≤ x ≤ 1.
[Source gives f_X(x) = 2 − (3/2)x + 2x² (different f form); we follow source's algebra.]

Marginal of Y per source: f_Y(y) = 1/3 + (1/6)y − (5/18) y², y > 0.

**CYP 1, Q2: Joint f(x, y) = (2/3)(x + 2y) on 0 ≤ x, y ≤ 1.**
Marginal of X:
g(x) = ∫₀¹ (2/3)(x + 2y) dy = (2/3)[xy + y²]₀¹ = (2/3)(x + 1) = (1/3)(2x + 2) for 0 ≤ x ≤ 1.

(Find h(y) similarly.)

**CYP 2, Q1: Bin distribution with mean = 4 and σ² = 8/3. Find n, p.**
- np = 4, npq = 8/3 ⇒ q = (8/3)/4 = 2/3 ⇒ p = 1/3.
- n = 4/p = **12**.

**CYP 2, Q3: Pass rate 60%, group of 6, P(at least 4 passed)?**
P = ⁶C₄(0.6)⁴(0.4)² + ⁶C₅(0.6)⁵(0.4) + ⁶C₆(0.6)⁶ = **1701/3125**.

**CYP 2, Q4: Die thrown 10 times. Even appears 5 times has twice the prob of 4 times. P(even appears 0 times)?**

f(x) = ¹⁰C_x · p^x · q^(10−x). Given f(5) = 2 · f(4):
¹⁰C₅ · p⁵ · q⁵ = 2 · ¹⁰C₄ · p⁴ · q⁶ ⇒ (252/210) · (p/q) = 2 ⇒ p/q = (210·2)/252 = 5/3 ⇒ p = 5/8, q = 3/8.
f(0) = (3/8)¹⁰ = **(3/8)¹⁰**.

**CYP 2, Q5: 10% defective, sample of 10. Use Poisson approx for P(exactly 3 defectives), e = 2.72.**
λ = np = 10 × 0.1 = 1.
f(3) = e^(−1) · 1³ / 3! ≈ (0.368)/6 ≈ **0.061**.

**CYP 2, Q6: 2% defective, sample of 100. P(3 or more defectives)?**
λ = np = 2.
P(X ≥ 3) = 1 − [f(0) + f(1) + f(2)] = 1 − e^(−2)[1 + 2 + 2] = 1 − 5e^(−2) ≈ 1 − 5·0.135 = **0.325**.

**CYP 2, Q7: P(7 of 10 recover from disease), p = 0.8.**
b(7; 10, 0.8) = ¹⁰C₇ · (0.8)⁷ · (0.2)³ ≈ **0.20**.

**CYP 3, Q1: Weights X ~ N(151, 15²), 500 students.**
(i) P(120 ≤ X ≤ 155): z₁ = (120 − 151)/15 = −2.07, z₂ = (155 − 151)/15 = 0.27.
P = Φ(0.27) − Φ(−2.07) = 0.6064 − (1 − 0.9808) = 0.6064 − 0.0192 = **0.5872**.
Number of students: 500 × 0.5872 = ~294.
(ii) P(X > 155) = 1 − Φ(0.27) = **0.3936**. Number: 500 × 0.3936 ≈ 197.

**CYP 3, Q2: Mean = 50, P(X > 60) = 5%. Find σ.**
z = (60 − 50)/σ = 10/σ. Given P(Z > z) = 0.05 ⇒ z = 1.64 ⇒ σ = 10/1.64 = **6.10**.

> **Quick Recall:**
> - Match question to the right distribution:
>   * "n trials, fixed p, count successes" → Binomial
>   * "rare events per unit time/area" → Poisson (or Poisson approx if n large, p small)
>   * "continuous, symmetric" → Normal
> - Always sketch the standard-normal density and shade the area you want.

---

## Section: Block 8 Final Exercises — Worked Templates 🔴

### Examples

**Q1: Binomial distribution of getting a six in three tosses of a die.**
n = 3; p = 1/6 (six); q = 5/6.

| X | P(X) |
|---|------|
| 0 | ³C₀(1/6)⁰(5/6)³ = 125/216 |
| 1 | ³C₁(1/6)¹(5/6)² = 75/216 = 25/72 |
| 2 | ³C₂(1/6)²(5/6)¹ = 15/216 = 5/72 |
| 3 | ³C₃(1/6)³(5/6)⁰ = 1/216 |

(Sum: 125/216 + 75/216 + 15/216 + 1/216 = 216/216 = 1 ✓)

**Q2: 10 good + 4 fused bulbs; draw 3 with replacement; distribution of X = number of fused?**
p = P(fused) = 4/14 = 2/7; q = 5/7. n = 3.

| X | P(X) |
|---|------|
| 0 | ³C₀(2/7)⁰(5/7)³ = 125/343 |
| 1 | ³C₁(2/7)¹(5/7)² = 150/343 |
| 2 | ³C₂(2/7)²(5/7)¹ = 60/343 |
| 3 | ³C₃(2/7)³(5/7)⁰ = 8/343 |

**Q3: Poisson — 33 policies/week (the source uses μ = 3 in calculations; we follow source).**
(a) **P(some policies sold)** = P(X ≥ 1) = 1 − P(X = 0) = 1 − e^(−3) ≈ 1 − 0.0498 = **0.9502**.
(b) **P(2 ≤ X < 5)** = f(2) + f(3) + f(4)
= e^(−3)·(9/2) + e^(−3)·(27/6) + e^(−3)·(81/24)
= e^(−3)·[4.5 + 4.5 + 3.375] ≈ 0.0498 × 12.375 ≈ **0.61611**.
(c) **P(1 policy on a given day)** with 5 working days/week ⇒ daily rate = 3/5 = 0.6.
P(X = 1) = e^(−0.6) · 0.6 ≈ 0.549 × 0.6 = **0.32929**.

**Q4: Battery time X ~ N(50, 15²). P(50 < X < 70)?**
- z₁ = (50 − 50)/15 = 0.
- z₂ = (70 − 50)/15 ≈ 1.33.
P = Φ(1.33) − Φ(0) = 0.9082 − 0.5 = **0.4082**.

**Q5: Car speeds X ~ N(90, 10²). P(X > 100)?**
z = (100 − 90)/10 = 1.
P(Z > 1) = 1 − Φ(1) = 1 − 0.8413 = **0.1587**.

> **Quick Recall:**
> - Binomial — list each P(X = x) and check Σ = 1.
> - Poisson with rate per unit time/space — scale λ to the requested interval.
> - Normal — always (i) standardise to z, (ii) sketch, (iii) use Φ table.

### ⚠️ Common Mistakes
- ❌ Mistake: Applying binomial to draws *without* replacement → ✅ Correct: Replacement makes trials independent (binomial OK); without replacement requires hypergeometric.
- ❌ Mistake: Forgetting that Poisson rate scales with the size of the observation window → ✅ Correct: λ_new = (rate per unit) × (number of units).
- ❌ Mistake: Using Φ(z) for "more than" → ✅ Correct: P(X > a) = 1 − Φ(z); Φ(z) is left-tail.

### Connections
- Closes Block 8.
- Builds on: [Binomial, Poisson, Normal] (Chunks 006–007) and the [moment/expectation framework] (Chunks 002–005).
- Looks ahead to (outside Block 8): Hypothesis testing, confidence intervals, sampling distributions.

### Open Questions
1. When in practice does the binomial differ enough from the normal that the normal approximation should *not* be used?
2. How can the Poisson approximation to binomial fail when np becomes too large?
