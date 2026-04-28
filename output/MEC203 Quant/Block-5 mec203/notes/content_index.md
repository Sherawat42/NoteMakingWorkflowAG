# Content Index
**Source**: Block-5 mec203.pdf | **Chunks**: 10 | **Completed**: 2026-04-28

## Notes Files
| Chunk | Title | Pages | Top Sections | Key Terms |
|-------|-------|-------|--------------|-----------|
| 001 | Block 5 Intro & Unit 16 Univariate Extrema | 1–10 | Maxima/minima, FOC/SOC, Inflexion, Taylor criterion, Bivariate FOC | stationary point, extremum, point of inflexion |
| 002 | Unit 16 Multivariate SOC | 11–20 | Bivariate Hessian SOC, 3-variable principal minors, n-variable test | Hessian, Young's theorem, saddle point, principal minor |
| 003 | Unit 17 Unconstrained Optimisation | 21–30 | FOC differential/derivative, SOC for f(x,y), determinantal test, multi-product firm (competitive & monopoly) | unconstrained optimisation, choice variables |
| 004 | Unit 17 Constrained & KT | 31–40 | No-arbitrage, Lagrange theorem, bordered Hessian, KT theorem with CS, KT case analysis | Lagrange multiplier, CQ, complementary slackness, binding/slack |
| 005 | KT Cases & Unit 18 Convexity | 41–50 | KT Ex 17.10 cases, Unit 17 wrap-up, Convex/concave definitions, examples | convex function, strictly concave, affine |
| 006 | Unit 18 Quasi-Convex, NDCQ, Slackness | 51–60 | Hessian PSD/NSD test, Quasi-convex/concave, NDCQ, Binding analysis, LP CS | quasi-convex, PSD, NDCQ, feasible region |
| 007 | Unit 18 KT Lagrangian + Exercises | 61–70 | LP CS proof, mixed constraints theorem, KT Lagrangian, worked KT problems | active set, KT Lagrangian |
| 008 | Unit 19 Multiplier, Envelope, Homogeneous | 71–80 | Lagrange method restated, Envelope theorem (unconstrained/constrained), Homogeneous functions, Theorems A-C | value function, envelope theorem, homogeneous of degree k, CRS/IRS/DRS, Cobb-Douglas, CES |
| 009 | Unit 19 Homothetic, Concave, Bordered Hessian, Euler | 81–90 | Homothetic functions (Theorems D-F), Concave functions (Theorems G-I), Quasi-concave (Theorems J-L), Bordered Hessian quasi-concavity, Euler economic apps | homothetic, ordinal, upper level set, bordered Hessian, Euler's theorem |
| 010 | Unit 19 Solutions & Exercises | 91–94 | CYP 1-4 solutions, Q1 envelope verification, Q2 monomial homogeneity, Q3 constrained min | shadow price, factor payments |

## Cross-References
| From | To | Relationship |
|------|----|--------------| 
| Univariate FOC (Chunk 001) | Bivariate FOC (Chunk 001) | generalises to |
| Bivariate SOC (Chunks 002, 003) | n-variable Hessian test (Chunk 002, 003) | generalises to |
| Unconstrained SOC (Chunk 003) | Constrained SOC / bordered Hessian (Chunk 004) | extended by |
| Lagrange theorem (Chunk 004) | Kuhn-Tucker theorem (Chunk 004) | generalised to inequalities |
| KT theorem (Chunk 004) | Mixed-constraint theorem (Chunk 007) | extended to mixed |
| KT theorem (Chunk 004) | KT Lagrangian (Chunk 007) | streamlined for non-negativity |
| Convex function (Chunk 005) | Quasi-convex (Chunk 006) | weakened to |
| Concave function (Chunks 005, 009) | Stationary point = max (Chunk 009) | implies |
| Concave function (Chunk 005) | Local max = global max (Chunk 004) | sufficient condition |
| Hessian convexity test (Chunk 006) | Bordered Hessian quasi-concavity (Chunk 009) | analogous structure |
| Lagrange multiplier (Chunk 004) | Envelope theorem `dV/da = ∂L/∂a` (Chunk 008) | gives interpretation |
| Homogeneous functions (Chunk 008) | Euler's theorem (Chunk 009) | yields key identity |
| Homogeneous functions (Chunk 008) | Homothetic functions (Chunk 009) | generalised by |
| Demand homogeneity of degree 0 (Chunk 008) | Money illusion-free demand | economic application |

## Key Terms Glossary
| Term | Definition | First Appears |
|------|-----------|---------------|
| Stationary point | `f'(x) = 0` (univariate) / all first partials zero (multivariate) | Chunk 001 |
| Extremum | Collective term for maximum and minimum | Chunk 001 |
| Local extremum | Max/min in some neighbourhood; can be non-unique | Chunk 001 |
| Global extremum | Max/min over entire domain; unique for continuous f | Chunk 001 |
| Point of inflexion | `f''(x) = 0` and `f'''(x) ≠ 0`; curvature changes | Chunk 001 |
| FOC | First-order condition: `f'(x) = 0` (or `∇f = 0`) | Chunk 001 |
| SOC | Second-order condition: sign of `f''` or Hessian | Chunk 001 |
| Hessian | Symmetric matrix of second partials | Chunk 002 |
| Young's theorem | `f_ij = f_ji` (cross partials equal) | Chunk 002 |
| Saddle point | Stationary point with mixed-sign Hessian eigenvalues | Chunk 002 |
| Principal minor | Determinant of leading `i×i` submatrix | Chunk 002 |
| Choice variables | Independent variables we control | Chunk 003 |
| Unconstrained optimisation | Max/min with no domain constraints | Chunk 003 |
| Constrained optimisation | Max/min subject to constraints | Chunk 003 |
| Lagrangian | `L = f + λ(c - g)` | Chunk 004 |
| Lagrange multiplier λ\* | Shadow price; `dV/dc = λ*` | Chunk 004 |
| Constraint qualification (CQ) | Constraint gradients linearly independent | Chunk 004 |
| Bordered Hessian | SOC matrix for constrained problems | Chunk 004 |
| Binding constraint | `g(x*) = 0` at optimum | Chunk 004 |
| Slack constraint | `g(x*) > 0` at optimum; forces λ = 0 | Chunk 004 |
| Complementary slackness | `λ_i · g_i(x*) = 0` for each i | Chunk 004 |
| Kuhn-Tucker (KT) conditions | Stationarity + slackness + λ ≥ 0 + g ≥ 0 | Chunk 004 |
| Convex function | `f(θu+(1-θ)v) ≤ θf(u)+(1-θ)f(v)` | Chunk 005 |
| Concave function | Reverse inequality | Chunk 005 |
| Strictly convex / concave | Strict inequality versions | Chunk 005 |
| Affine function | Both convex and concave | Chunk 005 |
| Quasi-convex | `f(θu+(1-θ)v) ≤ max{f(u), f(v)}` | Chunk 006 |
| Quasi-concave | `f(θu+(1-θ)v) ≥ min{f(u), f(v)}` | Chunk 006 |
| Strongly quasi-convex | Strict inequality without `u ≠ v` clause | Chunk 006 |
| Quasi-linear | Both quasi-convex and quasi-concave | Chunk 006 |
| PSD (Positive Semidefinite) | `x'Hx ≥ 0` ∀ x | Chunk 006 |
| NSD (Negative Semidefinite) | `x'Hx ≤ 0` ∀ x | Chunk 006 |
| NDCQ | Non-degenerate constraint qualification | Chunk 006 |
| Feasible set Ω | Points satisfying all constraints | Chunk 006 |
| Active / inactive constraint | Synonyms for binding / slack | Chunk 008 |
| Value function V(a) | `V(a) = max f(u, a)` | Chunk 008 |
| Envelope theorem | `dV/da = ∂L/∂a` at optimum | Chunk 008 |
| Homogeneous of degree k | `f(tu) = t^k f(u)` for `t > 0` | Chunk 008 |
| Constant returns to scale (CRS) | Production fn homogeneous of degree 1 | Chunk 008 |
| Increasing returns (IRS) | Degree > 1 | Chunk 008 |
| Decreasing returns (DRS) | Degree between 0 and 1 | Chunk 008 |
| Cobb-Douglas | `A·x₁^α₁·...·xₙ^αₙ`; degree `Σ αᵢ` | Chunk 008 |
| CES function | `(a₁ x₁^ρ + a₂ x₂^ρ)^(q/ρ)`; degree q | Chunk 008 |
| Demand homogeneity (degree 0) | `D(tp, tI) = D(p, I)` | Chunk 008 |
| Homothetic | Monotonic transform of homogeneous | Chunk 009 |
| Ordinal property | Depends only on level-set shape | Chunk 009 |
| Cardinal property | Depends on shape AND function values | Chunk 009 |
| Upper level set U(f, α) | `{u : f(u) ≥ α}` | Chunk 009 |
| Bordered Hessian (quasi-concavity) | Adds gradient as border to Hessian | Chunk 009 |
| Euler's theorem | `u · ∇f = k·f` (degree-k homogeneous) | Chunk 009 |
| Marginal Rate of Substitution (MRS) | Slope of indifference curve | Chunk 009 |
