# Running Context

## Key Concepts Introduced
- **Random experiment** (Chunk 001): Repeatable act with unpredictable outcome.
- **Sample space S** (Chunk 001): All possible outcomes of an experiment.
- **Event** (Chunk 001): Subset of S satisfying some criterion.
- **Mutually exclusive / exhaustive / equally likely / independent / conditional events** (Chunk 001).
- **Four definitions of probability** (Chunk 001): Classical, Axiomatic, Empirical, Subjective.
- **Techniques of counting** (Chunk 001): Permutation, combination, ordered partition.
- **Theorem of Total Probability (Addition)** (Chunk 002): P(A ∪ B) = P(A) + P(B) − P(A ∩ B).
- **Theorem of Compound Probability (Multiplication)** (Chunk 002): P(A ∩ B) = P(A) · P(B|A).
- **Conditional probability** (Chunk 002): P(B|A) = P(A ∩ B)/P(A).
- **Independence** (Chunk 002): P(A ∩ B) = P(A) · P(B).
- **Bayes' Theorem** (Chunk 002).
- **Mathematical Expectation E(x)** (Chunk 002).
- **Variance Var(x), standard deviation σ** (Chunk 003).
- **Theorem of expectation of sum** (Chunk 003): E(X+Y) = E(X) + E(Y) always.
- **Theorem of expectation of product (independent)** (Chunk 003): E(XY) = E(X) E(Y).
- **Marginal & conditional distributions (bivariate)** (Chunk 003).
- **Covariance Cov(X, Y)** (Chunk 003).
- **Random variable (discrete vs continuous)** (Chunk 004).
- **Probability mass function (p.m.f.) f(x)** (Chunk 004).
- **Probability density function (p.d.f.) f(x)** (Chunk 004).
- **Cumulative distribution function (c.d.f.) F(x)** (Chunk 004).
- **Moments (raw and central)** (Chunk 004).
- **Skewness** (Chunk 005).
- **Chebyshev's theorem** (Chunk 005).
- **Moment Generating Function (MGF) M_X(t)** (Chunk 005).
- **Joint probability distribution / joint p.d.f.** (Chunk 005).
- **Marginal distribution** (Chunk 006).
- **Binomial distribution** (Chunk 006).
- **Poisson distribution** (Chunk 006).
- **Normal distribution** (Chunk 007).
- **Standard normal variable Z and Φ(z)** (Chunk 007).
- **Empirical Rule (68-95-99.7)** (Chunk 007).

## Definitions (⭐ exam-important)
- **Sample space**: Collection of all possible outcomes of an experiment.
- **Mutually exclusive events**: Events that cannot occur simultaneously.
- **Independent events**: P(A ∩ B) = P(A) · P(B), or P(B|A) = P(B).
- **Conditional probability**: P(B|A) = P(A ∩ B)/P(A) when P(A) > 0.
- **Total probability theorem**: P(A ∪ B) = P(A) + P(B) − P(A ∩ B); = P(A) + P(B) if disjoint.
- **Compound probability**: P(A ∩ B) = P(A) · P(B|A).
- **Bayes' Theorem**: P(B_i|A) = P(B_i) P(A|B_i) / Σ P(B_j) P(A|B_j).
- **Mathematical expectation**: E(X) = Σ x_i p_i (discrete); ∫ x f(x) dx (continuous).
- **Variance**: Var(X) = E(X²) − [E(X)]². σ = √Var.
- **Probability mass function (p.m.f.)**: f(x) = P(X = x), discrete; f ≥ 0, Σ = 1.
- **Probability density function (p.d.f.)**: continuous f ≥ 0, ∫ f = 1; P(c ≤ X ≤ d) = ∫_c^d f(x) dx.
- **c.d.f.**: F(x) = P(X ≤ x); 0 to 1; non-decreasing.
- **r-th raw moment**: μ_r' = E(X^r).
- **r-th central moment**: μ_r = E[(X − μ)^r]; μ_2 = variance.
- **Chebyshev's theorem**: P(|X − μ| < kσ) ≥ 1 − 1/k².
- **MGF**: M_X(t) = E(e^(tX)); μ_r' = d^r M(t)/dt^r at t = 0.
- **Joint p.m.f./p.d.f.**: f(x, y); double sum/integral = 1.
- **Marginal distribution**: g(x) = Σ_y f(x, y) or ∫ f(x, y) dy.
- **Binomial distribution**: P(X = x) = ⁿC_x p^x q^(n−x); μ = np, σ² = npq.
- **Poisson distribution**: P(X = x) = e^(−λ) λ^x / x!; μ = σ² = λ.
- **Normal distribution**: f(x) = (1/(σ√2π)) exp(−(x−μ)²/(2σ²)).
- **Standard normal Z**: Z = (X − μ)/σ ~ N(0, 1).
- **Φ(z)**: c.d.f. of standard normal. Φ(−z) = 1 − Φ(z).

## Named Models / Laws / Theories
- **Theorem of Complementary Event** (Chunk 002): P(Aᶜ) = 1 − P(A).
- **Boole's inequality** (Chunk 002): P(A ∪ B) ≤ P(A) + P(B).
- **Bonferroni's inequality** (Chunk 002): P(A ∩ B) ≥ P(A) + P(B) − 1.
- **De Morgan's theorem** (Chunk 002): used to show Aᶜ, Bᶜ independent if A, B independent.
- **Bayes' Theorem** (Chunk 002).
- **Inclusion–Exclusion Principle** (Chunk 002): three-event total probability formula.
- **Chebyshev's Theorem** (Chunk 005): distribution-free deviation bound.
- **Chain rule of probability** (Chunk 002): P(A₁ ∩ … ∩ A_n) = product of conditional probabilities.
- **Binomial Theorem** (Chunk 006): binomial sum-of-independent-binomials proof.
- **Maclaurin series** (Chunk 005): basis for MGF and Poisson derivation.
- **Empirical Rule (68-95-99.7)** (Chunk 007).
- **Linear transformation theorem (normal)** (Chunk 007): Y = a + bX; Y ~ N(a + bμ, b²σ²).

## Key Data & Numbers
- E(roll of die) = 3.5 (Chunk 002).
- Boole, Bonferroni inequalities (Chunk 002).
- Standard normal critical values: z_(0.05) = 1.645, z_(0.025) = 1.96, z_(0.01) = 2.33 (Chunk 007).
- Empirical Rule percentages: ±1σ → 68%, ±2σ → 95%, ±3σ → 99.7% (Chunk 007).
- Area between z = ±2.58 = 99%; ±1.96 = 95% (Chunk 007).
- Chebyshev: at k = 2, P(|X − μ| ≥ 2σ) ≤ 1/4 = 25% (Chunk 005).
- e ≈ 2.718, e^(−1) ≈ 0.368, e^(−2) ≈ 0.135, e^(−3) ≈ 0.0498 (Chunks 006–008).
