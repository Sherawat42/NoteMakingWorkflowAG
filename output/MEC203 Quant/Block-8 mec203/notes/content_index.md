# Content Index
**Source**: Block-8 mec203.pdf | **Chunks**: 8 | **Completed**: 2026-04-28

## Notes Files
| Chunk | Title | Pages | Top Sections | Key Terms |
|-------|-------|-------|--------------|-----------|
| 001 | Probability Theory: Foundations & Definitions | 1–10 | Deterministic vs Random; Sample Space & Terminology; Four Definitions of Probability | sample space, event, mutually exclusive, classical, axiomatic, empirical, subjective, ⁿC_r |
| 002 | Theorems of Probability, Conditional Probability, Bayes' Theorem | 11–20 | Total Probability; Compound Probability; Independent Events; Bayes' Theorem; Mathematical Expectation (intro) | addition theorem, multiplication theorem, conditional, independence, Bayes', E(X) |
| 003 | Variance, Theorems of Expectation, Unit 25 wrap-up | 21–30 | Variance; Theorems on Expectation; Joint and marginal probability (bivariate); Unit 25 Summary | variance, σ², covariance, marginal probability, sum/product theorems |
| 004 | Random Variables, p.m.f., p.d.f., c.d.f., Moments | 31–40 | RVs (discrete vs continuous); p.m.f.; p.d.f.; c.d.f.; Moments | random variable, p.m.f., p.d.f., c.d.f., raw moment, central moment |
| 005 | Higher Moments, Chebyshev, MGF, Joint Distribution | 41–50 | Skewness; Chebyshev's Theorem; MGF; Joint Probability Distribution | skewness, Chebyshev, MGF, joint p.m.f., joint p.d.f., independence (joint) |
| 006 | Marginal Distribution; Binomial; Poisson | 51–60 | Joint c.d.f. example; Marginal Distribution; Binomial Distribution; Poisson Distribution | marginal density, binomial p.m.f., μ = np, σ² = npq, Poisson p.m.f., μ = σ² = λ |
| 007 | Normal Distribution; Standard Normal Variable | 61–70 | Poisson examples & sum-of-Poisson; Normal Distribution; Standard Normal Distribution & Standardisation | normal p.d.f., Empirical Rule, standardisation, Φ(z), critical z-values |
| 008 | Unit 27 Summary, Key Words, Worked Exercises | 71–76 | Unit 27 Summary; Check Your Progress solutions; Block 8 Final Exercises | binomial / Poisson / normal recap, exercise templates |

## Cross-References
| From | To | Relationship |
|------|----|-------------|
| Theorem of Total Probability (Chunk 002) | Sample Space & Terminology (Chunk 001) | Builds on |
| Theorem of Compound Probability (Chunk 002) | Conditional events (Chunk 001) | Builds on |
| Bayes' Theorem (Chunk 002) | Total Probability + Compound Probability (Chunk 002) | Combines |
| Independence (Chunk 002) | Compound Probability (Chunk 002) | Special case |
| Mathematical Expectation (Chunk 002) | Mathematical expectation (Chunk 003) | Continues into |
| Variance & Theorems on Expectation (Chunk 003) | Mathematical Expectation (Chunk 002) | Continues from |
| Moments (Chunk 004) | Variance & Functions of an RV (Chunk 003) | Builds on |
| MGF (Chunk 005) | Moments (Chunk 004) | Pre-requisite for |
| Binomial Distribution (Chunk 006) | Independent Events (Chunk 002), Mathematical Expectation (Chunks 002–003) | Builds on |
| Poisson Distribution (Chunk 006) | Binomial Distribution (Chunk 006) | Limiting case (n→∞, p→0, np = λ) |
| Normal Distribution (Chunk 007) | Linear-transformation rules (Chunk 005) | Builds on |
| Standard Normal Variable (Chunk 007) | Normal Distribution (Chunk 007) | Standardised case |
| Joint Distribution (Chunk 005) | p.m.f./p.d.f. (Chunk 004) | Bivariate generalisation |
| Marginal Distribution (Chunk 006) | Joint Distribution (Chunk 005) | Sums out one variable |
| Final Exercises (Chunk 008) | Binomial / Poisson / Normal (Chunks 006–007) | Applies |

## Key Terms Glossary
| Term | Definition | First Appears |
|------|-----------|---------------|
| Sample space | All possible outcomes of an experiment | Chunk 001 |
| Event | Subset of S satisfying a particular criterion | Chunk 001 |
| Mutually exclusive events | A ∩ B = ∅ — cannot co-occur | Chunk 001 |
| Mutually exhaustive events | A ∪ B ∪ … = S — at least one must occur | Chunk 001 |
| Equally likely events | All elementary outcomes have equal probability | Chunk 001 |
| Classical probability | P(A) = N_A / N (under symmetry) | Chunk 001 |
| Axiomatic probability | Defined by axioms: P ≥ 0; P(S) = 1; additivity for disjoint | Chunk 001 |
| Empirical probability | Limit of relative frequency m/N as N → ∞ | Chunk 001 |
| Subjective probability | Degree-of-belief measure | Chunk 001 |
| Theorem of Total Probability | P(A ∪ B) = P(A) + P(B) − P(A ∩ B); equals sum if disjoint | Chunk 002 |
| Theorem of Complementary Event | P(Aᶜ) = 1 − P(A) | Chunk 002 |
| Theorem of Compound Probability | P(A ∩ B) = P(A) · P(B|A) | Chunk 002 |
| Conditional probability | P(B|A) = P(A ∩ B)/P(A) when P(A) > 0 | Chunk 002 |
| Independent events | P(A ∩ B) = P(A) · P(B); equivalently P(B|A) = P(B) | Chunk 002 |
| Bayes' Theorem | P(B_i|A) = P(B_i) P(A|B_i) / Σ P(B_j) P(A|B_j) | Chunk 002 |
| Mathematical expectation E(X) | Σ x_i p_i (discrete) or ∫ x f(x) dx (continuous) | Chunk 002 |
| Variance Var(X) | E[(X − μ)²] = E(X²) − [E(X)]² | Chunk 003 |
| Standard deviation σ | √Var(X) | Chunk 003 |
| Covariance Cov(X, Y) | E[(X − μ_X)(Y − μ_Y)] | Chunk 003 |
| Random variable | Real-valued function on the sample space | Chunk 004 |
| Discrete RV | Takes countable values | Chunk 004 |
| Continuous RV | Takes values in a continuous range; P(X = c) = 0 | Chunk 004 |
| p.m.f. | f(x) = P(X = x), discrete; f ≥ 0 and Σ = 1 | Chunk 004 |
| p.d.f. | Continuous density; f ≥ 0 and ∫ = 1; P(c ≤ X ≤ d) = ∫_c^d f(x) dx | Chunk 004 |
| c.d.f. | F(x) = P(X ≤ x); F(−∞) = 0, F(∞) = 1 | Chunk 004 |
| Raw moment μ_r' | E(X^r) | Chunk 004 |
| Central moment μ_r | E[(X − μ)^r] | Chunk 004 |
| Skewness | Asymmetry of a distribution; μ_3 ≠ 0 indicates skew | Chunk 005 |
| Chebyshev's Theorem | P(|X − μ| < kσ) ≥ 1 − 1/k² | Chunk 005 |
| MGF | M_X(t) = E(e^(tX)); μ_r' = M^(r)(0) | Chunk 005 |
| Joint p.m.f./p.d.f. | Bivariate function with f ≥ 0 and ΣΣ = 1 (or ∫∫ = 1) | Chunk 005 |
| Marginal distribution | Sum / integrate joint over the other variable | Chunk 006 |
| Binomial distribution | P(X = x) = ⁿC_x p^x q^(n−x); μ = np, σ² = npq | Chunk 006 |
| Poisson distribution | P(X = x) = e^(−λ) λ^x / x!; μ = σ² = λ | Chunk 006 |
| Normal distribution | f(x) = (1/(σ√2π)) exp(−(x−μ)²/(2σ²)) | Chunk 007 |
| Standard normal Z | Z = (X − μ)/σ ~ N(0, 1) | Chunk 007 |
| Φ(z) | c.d.f. of standard normal; Φ(−z) = 1 − Φ(z) | Chunk 007 |
| Empirical Rule | 68% within 1σ, 95% within 2σ, 99.7% within 3σ | Chunk 007 |
