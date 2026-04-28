# Content Index
**Source**: Block-9 mec203.pdf | **Chunks**: 11 | **Completed**: 2026-04-28

## Notes Files

| Chunk | Title | Pages | Top Sections | Key Terms |
|-------|-------|-------|--------------|-----------|
| 001 | Sampling Theory: Foundations, Sample Design, Biases | 1–10 | Block 9 Overview; Unit 28 Objectives; Advantages of Sample Survey; Sample Design; Biases (selection, procedural, OVB) | Population, Sample, Parameter, Statistic, Random sample, Sampling frame, Selection bias, OVB |
| 002 | Types of Sampling, Sampling Distribution, Standard Error | 11–20 | Probability vs non-probability sampling; SRS / systematic / stratified / cluster / multistage; Sampling distribution; Standard error; SE of x̄ | SRS, Tippet's table, Sampling distribution, Standard error, Probable error, Stratified, Cluster |
| 003 | End of Unit 28 + Start of Unit 29 (Chi-square) | 21–30 | SE of sample proportion; Finite Population Correction; Unit 28 wrap-up; Unit 29 intro; χ² distribution definition | Sample proportion p̂, FPC, Chi-square variate, Degrees of freedom |
| 004 | χ² Properties, Goodness of Fit, t/F distributions, Sampling of x̄ and s² | 31–40 | χ² critical values; Pearson's goodness-of-fit; Student's t; Fisher's t; F-distribution; Independence of x̄ and s² | Pearson χ² statistic, Student's t, F-distribution (Snedecor), Cauchy, MGF of χ² |
| 005 | s² distribution, CLT, Unit 30 Estimation Intro & Properties | 41–50 | Distribution of s²; Central Limit Theorem; Unit 29 wrap-up; Unit 30 estimation intro; Parameter space; Unbiased / Consistent / Efficient / MVUE | CLT, LLN, Parameter space Θ, Unbiasedness, Consistency, Efficiency, MVUE |
| 006 | MVUE, Sufficiency, Cramer-Rao, Asymptotic, Methods of Estimation | 51–60 | MVUE x̄; Mean vs Median (eff. 0.64); Sufficiency & Factorization; Koopman's exp. family; Cramer-Rao; Rao-Blackwell; Asymptotic properties; ML / GMM / PLS | Sufficient statistic, Factorization theorem, Cramer-Rao, Fisher Information, Rao-Blackwell, MLE, GMM |
| 007 | Estimation wrap-up + Unit 31 Hypothesis Testing intro | 61–70 | Unit 30 key words; Worked answers/hints; Unit 31 intro; Null & alternative hypotheses; Critical region; Level of significance; Confidence intervals; One- vs two-tailed | Null hypothesis, Alternative hypothesis, Critical region, Level of significance, Confidence interval/limits/coefficient |
| 008 | Critical Values, P-value, Type I/II, Power, Tests under Normality | 71–80 | Table 31.1 z critical values; Critical-region vs P-value method; 5-step recipe (Table 31.2); Type I/II errors; Power; MP / UMP; Univariate normal Cases I/II/III | P-value, Type I error α, Type II error β, Power, MP test, UMP test, Student's t-test, Pooled vs unbiased variance |
| 009 | Two-Normal Comparisons, Bivariate Normal, Unit 31 Wrap-up | 81–90 | Two-sample Cases I/II/III; Pooled variance; Fisher's t-test; F-test for variance equality; Correlation t-test; Paired t-test; Bivariate σ-ratio; Unit 31 key words | Pooled variance s'², Fisher's two-sample t, F variance test, Sample correlation r, Paired t-test |
| 010 | Unit 31 Answers, Worked Exercises, Bibliography, Tables A1–A4 (start) | 91–100 | CYP answers (CYP1–CYP4); §31.11 six exercises; Bibliography; Tables A1 (Normal), A2 (χ²), A3 (t), A4 5% F | Worked one-sample t, Worked F-test, Worked paired t, Critical-value tables |
| 011 | Statistical Tables (F at 1% level), Imprint | 101–103 | Table A4 1%-level F (df₁=1..10 and 12..∞); ISBN imprint | F₀.₀₁ critical values |

---

## Cross-References

| From | To | Relationship |
|------|----|--------------|
| Random sampling (Chunk 001) | Probability sampling techniques (Chunk 002) | builds on |
| Standard error (Chunk 002) | SE of sample proportion (Chunk 003) | specialises into |
| Chi-square distribution (Chunk 003) | χ² goodness-of-fit (Chunk 004) | builds on |
| Sampling distribution of s² (Chunk 004) | Independence of x̄ and s² (Chunk 004) | uses |
| t-distribution (Chunk 004) | Student's t-test for μ (Chunk 008) | applied in |
| t-distribution (Chunk 004) | Fisher's two-sample t (Chunk 009) | extended into |
| F-distribution (Chunk 004) | F-test for variance equality (Chunk 009) | applied in |
| CLT (Chunk 005) | Asymptotic normality (Chunk 006) | generalises into |
| MVUE (Chunk 005) | Cramer-Rao bound (Chunk 006) | quantifies |
| Cramer-Rao (Chunk 006) | Rao-Blackwell theorem (Chunk 006) | refined by |
| Estimation criteria (Chunk 005-006) | Hypothesis testing framework (Chunk 007) | precedes |
| Null hypothesis (Chunk 007) | 5-step procedure (Chunk 008) | structures |
| Type I / Type II error (Chunk 008) | Power of the test (Chunk 008) | inverse of |
| Power of test (Chunk 008) | MP / UMP tests (Chunk 008) | maximised by |
| Univariate normal Cases I/II/III (Chunk 008) | Two-sample Cases I/II/III (Chunk 009) | parallels |
| Pooled variance (Chunk 009) | Fisher's two-sample t (Chunk 009) | denominator of |
| Sample correlation r (Chunk 009) | Bivariate σ-ratio test (Chunk 009) | trick reuses |
| Paired t-test (Chunk 009) | CYP4 / Q6 worked examples (Chunk 010) | demonstrated by |
| F-test (Chunk 009) | Q3 worked example (Chunk 010) | demonstrated by |
| F-table 5% (Chunk 010) | F-table 1% (Chunk 011) | continues into |

---

## Key Terms Glossary

| Term | Definition | First Appears |
|------|-----------|---------------|
| Population | Aggregate of all objects under study | Chunk 001 |
| Sample | Finite subset of the population | Chunk 001 |
| Parameter | Numerical characteristic of population (μ, σ²) | Chunk 001 |
| Statistic | Numerical characteristic computed from sample | Chunk 001 |
| Random / Probability sample | Each unit has known non-zero probability of selection | Chunk 001 |
| Sampling frame | List of all population members | Chunk 001 |
| Selection bias | Bias from unrepresentative sample | Chunk 001 |
| Omitted Variable Bias (OVB) | Regression bias from missing correlated variable | Chunk 001 |
| Simple Random Sampling (SRS) | Equal selection probability | Chunk 002 |
| Systematic random sampling | Random start + every k-th element | Chunk 002 |
| Stratified random sampling | Homogeneous strata, SRS within | Chunk 002 |
| Cluster sampling | Heterogeneous clusters, SRS of clusters | Chunk 002 |
| Multistage sampling | Sampling at two or more successive stages | Chunk 002 |
| Sampling distribution | Probability law of a statistic | Chunk 002 |
| Standard error | SD of sampling distribution | Chunk 002 |
| Probable error | 0.6745 × SE | Chunk 002 |
| Tippet's Random Numbers Table | 10,400 four-digit numbers (41,600 digits) | Chunk 002 |
| Sample proportion p̂ | f/n; unbiased estimator of P | Chunk 003 |
| Finite Population Correction | √[(N−n)/(N−1)] | Chunk 003 |
| Chi-square variate | Sum of squared independent N(0,1)s | Chunk 003 |
| Degrees of freedom | Number of independent squared normals summed | Chunk 003 |
| Pearson's χ² statistic | Σ(O−E)²/E ~ χ²(n−1) | Chunk 004 |
| Student's t | (x̄−μ)/(s/√n); df = n−1 | Chunk 004 |
| Cauchy distribution | t with df = 1 | Chunk 004 |
| Fisher's t | N(0,1)/√(χ²(n)/n) | Chunk 004 |
| F-distribution (Snedecor's) | Ratio of independent χ²/df | Chunk 004 |
| Central Limit Theorem (CLT) | Sample mean → Normal | Chunk 005 |
| Khinchin's Weak LLN | iid means converge in probability | Chunk 005 |
| Parameter space Θ | Set of all possible θ | Chunk 005 |
| Unbiased estimator | E(T) = θ | Chunk 005 |
| Consistent estimator | T_n →ᴾ θ | Chunk 005 |
| Efficient estimator | Smallest variance among unbiased | Chunk 005 |
| MVUE | Minimum-Variance Unbiased Estimator | Chunk 005 |
| Sufficient statistic | Captures all sample info about θ | Chunk 006 |
| Factorization Theorem (Neyman) | L = g_θ(t)·h(x) iff t is sufficient | Chunk 006 |
| Cramer-Rao Inequality | Var(unbiased) ≥ 1/(n·I(θ)) | Chunk 006 |
| Fisher Information | E[(∂lnf/∂θ)²] | Chunk 006 |
| Rao-Blackwell Theorem | Improve unbiased estimator using sufficient statistic | Chunk 006 |
| MLE | Maximum Likelihood Estimator | Chunk 006 |
| GMM | Generalised Method of Moments | Chunk 006 |
| Null hypothesis (H₀) | Hypothesis of no difference (Fisher) | Chunk 007 |
| Alternative hypothesis (H₁) | Complementary to H₀ | Chunk 007 |
| Critical region | Rejection zone in sample space | Chunk 007 |
| Level of significance α | P[reject H₀ \| H₀ true] | Chunk 007 |
| Confidence interval / limits / coefficient | [c₁, c₂] containing θ with probability 1 − α | Chunk 007 |
| One-tailed test | H₁ one-sided | Chunk 007 |
| Two-tailed test | H₁ two-sided | Chunk 007 |
| Critical / significant value | Boundary between rejection and acceptance | Chunk 007 |
| P-value | Lowest α at which H₀ would be rejected | Chunk 008 |
| Type I error (α) | Reject H₀ when true | Chunk 008 |
| Type II error (β) | Accept H₀ when false | Chunk 008 |
| Producer's risk / Consumer's risk | Industrial-sampling names for α / β | Chunk 008 |
| Power of the test | 1 − β | Chunk 008 |
| Most Powerful (MP) test | Maximises power for simple H₁ | Chunk 008 |
| Uniformly Most Powerful (UMP) test | MP for every value of composite H₁ | Chunk 008 |
| Sample variance s² vs s'² | s² uses 1/n (biased); s'² uses 1/(n−1) (unbiased) | Chunk 008 |
| Pooled variance s'² | Weighted average of s'₁² and s'₂² | Chunk 009 |
| Fisher's two-sample t-test | t with df = n₁ + n₂ − 2 | Chunk 009 |
| F-test for equality of variances | F = s'₁²/s'₂² | Chunk 009 |
| Sample correlation r | Σ(x−x̄)(y−ȳ)/√[Σ(x−x̄)²Σ(y−ȳ)²] | Chunk 009 |
| Paired t-test | t = √n·z̄/s_z, z = x − y, df = n − 1 | Chunk 009 |
