# Running Context — MEC-203 Block 4 (Real Analysis)

Compiled across all 14 chunks. Source: IGNOU MEC-203 Quantitative Methods, Block 4.
Block 4 contains: Unit 13 (Real Analysis), Unit 14 (Calculus of Several Variables), Unit 15 (Metric Space and Point Set Topology).

## Key Concepts Introduced

### Unit 13 — Real Analysis (Chunks 002–006 partial)
- Real Analysis as branch of Mathematical Analysis (real-numbers domain) — Chunk 002
- Difference between Calculus and Real Analysis (apply vs justify) — Chunk 002
- Sequence (set view: ordered, enumerated, repetition allowed) — Chunk 002
- Sequence (function view: `f: S → R`, with `S = N` or interval subset) — Chunk 002
- Indexing set, term/element, index/rank, length, n-tuple, subsequence — Chunk 002
- Recursively definable sequence — Chunk 002
- Arithmetic Progression (A.P.), nth term, sum derivation by reverse-and-pair — Chunk 002
- Geometric Progression (G.P.), trivial cases, sum when `|r| < 1` — Chunk 003
- Harmonic Progression (H.P.), Harmonic sequence — Chunk 003
- Fibonacci sequence; Binet closed form; sum formula `Σ F_i = F_{n+2} − 1` — Chunk 003 (proof completed in 006)
- Bounded above / below / bounded sequence — Chunk 003
- Monotone sequence (increasing / decreasing / strict) — Chunk 003
- Alternating sequence — Chunk 003
- Independence of boundedness and monotonicity — Chunk 003
- Convergent sequence (ε–`n_ε`); uniqueness of limit — Chunk 003
- Cauchy sequence; equivalence of convergent and Cauchy — Chunk 003
- Non-convergent: finitely oscillatory / divergent to ±∞ / infinitely oscillatory — Chunk 003
- Limit point of a sequence — Chunk 003
- Open / closed / bounded / compact sets in R — Chunk 004
- Only `∅` and `R` are both open and closed — Chunk 004
- Limit point of a set (= accumulation / condensation / cluster point) — Chunk 004
- R^n as n-fold Cartesian product; vector +, scalar ·, zero vector, additive inverse — Chunk 004
- Euclidean distance, Euclidean norm; relation `||x − y|| = d(x, y)` — Chunk 004
- Functions over Euclidean spaces: dot product, projection, etc. — Chunk 004
- Open / closed disc; open / closed / bounded / compact in R^n — Chunk 004
- Limit and continuity for `f: R^n → R` (ε-δ with norm) — Chunk 004
- Limit and continuity for `f: R^n → R^m` — Chunk 005
- Local minima/maxima as values; Global / Absolute extremes — Chunk 005

### Unit 14 — Calculus of Several Variables (Chunks 006–010)
- Closed/open set verification via complements — Chunk 006
- Multivariate limit existence requires consistency along all directions — Chunk 006
- Path testing for non-existence of limit (two paths disagree → DNE) — Chunk 006
- Three forms of dependent-variable specification: explicit / implicit / composite — Chunk 007
- Partial derivative as one-variable limit with other variables held constant — Chunk 007
- Implicit partial derivatives via product/chain rule — Chunk 007
- Chain rule for one independent variable; for partials (Case I one parameter, Case II two parameters) — Chunk 007
- Higher-order partial derivatives, notation suffix order — Chunk 007
- Partial derivatives as direction-specific rate of change — Chunk 007
- Total differential `dz = f_x dx + f_y dy` (extended to many variables) — Chunk 007
- Directional derivative as `∇f · û` — Chunk 007/008
- Direction cosines for n-D unit vectors — Chunk 008
- Function `R^n → R^m` as m-tuple of scalar functions — Chunk 008
- Jacobian matrix; Jacobian determinant when n = m, applications to multiple integrals — Chunk 008
- Hessian as matrix of second partials encoding local curvature — Chunk 008
- MVT (single, geometric interpretation); MVT extended to several variables — Chunk 008
- Polynomial approximation idea — Chunk 008
- Taylor polynomial of order k; Taylor formula `f = P_k + R_k` — Chunk 008
- Remainder forms: Peano, Lagrange, Cauchy — Chunk 008
- Maclaurin's series (Taylor at `a = 0`) — Chunk 009
- Linear and quadratic approximations (1 var) — Chunk 009
- Multivariate linear and quadratic approximations — Chunk 009
- General k-th order multivariate Taylor polynomial — Chunk 009
- MVT corollaries: `f' ≡ 0 ⇒ f` constant; `f' > 0 ⇒ f` strictly increasing — Chunk 010

### Unit 15 — Metric Space & Point Set Topology (Chunks 011–014)
- Metric space generalises Euclidean space; topology generalises both — Chunk 011
- Distance / metric as a formalised idea (spatial, temporal, etc.) — Chunk 011
- Topology as Rubber-Sheet Geometry; cup ↔ doughnut equivalence — Chunk 011
- Multiple metrics on same set: Euclidean d_E, Taxicab/Manhattan d_T, Minkowski d_p — Chunk 011
- Metric axioms (4): non-negativity, identity of indiscernibles, symmetry, triangle inequality — Chunk 011
- Metric space `(S, d)`; discrete metric — Chunk 011
- Open / closed sphere in `(X, d)` — Chunk 011
- Open set / closed set in `(X, d)` — Chunk 012
- Convergence in metric space — Chunk 012
- Continuity in metric space (ε–δ, open-sphere, open-set, sequential) — Chunk 012
- Connectedness in metric space — Chunk 012
- Bounded set; bounded metric space — Chunk 012
- Compactness in metric space (closed and bounded) — Chunk 012
- Topology / Topological space `(X, T)`; open / closed / neighbourhood — Chunk 012
- Indiscrete, discrete, induced topology — Chunk 012
- Continuity in topology (neighbourhood form) — Chunk 012
- Connectedness in topology — Chunk 013
- Cover / open cover / subcover / finite subcover — Chunk 013
- Compactness via covers — Chunk 013
- Cofinite topology — Chunk 013

## ⭐ Definitions (exam-critical)

### Sequences and series (Unit 13)
- **Sequence (function form)**: `f: S → R`, `S = N` or interval subset of N — Chunk 002
- **Subsequence**: deletion preserving relative order — Chunk 002
- **Recursively definable sequence**: nth term via formula on previous terms — Chunk 002
- **A.P.**: `a, a+d, a+2d, …`; `t_n = a + (n−1)d`; `S_n = (n/2)[2a + (n−1)d]` — Chunk 002
- **G.P.**: `a, ar, ar², …`; `t_n = a · r^{n−1}`; `S_n = a(r^n − 1)/(r − 1)` — Chunk 003
- **H.P.**: reciprocals of A.P., `1/[a + (n−1)d]` — Chunk 003
- **Fibonacci**: `F_0 = 0, F_1 = 1, F_n = F_{n−1} + F_{n−2}` — Chunk 003
- **Bounded sequence**: `D ≤ S_n ≤ C` for all `n` — Chunk 003
- **Monotone sequence** (increasing / decreasing, strict variants) — Chunk 003
- **Convergent sequence**: `∀ε > 0, ∃ n_ε: |S_n − l| < ε ∀ n > n_ε` — Chunk 003
- **Cauchy sequence**: `∀ε > 0, ∃ n_ε: |S_n − S_m| < ε ∀ n, m > n_ε` — Chunk 003
- **Limit point of sequence**: subsequence converges to it — Chunk 003

### Sets in R and R^n (Unit 13)
- **Open set in R**: every point has an ε-interval inside the set — Chunk 004
- **Closed set in R**: complement is open — Chunk 004
- **Bounded set**: bounded above and below — Chunk 004
- **Compact set**: closed AND bounded — Chunk 004
- **Limit point of a set**: every ε-interval contains a point of S different from p — Chunk 004
- **R^n**: `{(a_1, …, a_n) : a_i ∈ R}` — Chunk 004
- **Euclidean distance / norm**: `d(x, y) = √Σ(x_i − y_i)²`, `||x|| = √Σ x_i²` — Chunk 004
- **Open disc / closed disc in R^n**: `||x − a|| < ε` (resp. `≤ ε`) — Chunk 004
- **Limit / continuity for `f: R^n → R^m`**: ε-δ with norms both sides — Chunk 005

### Calculus of Several Variables (Unit 14)
- **Multivariable limit**: value consistent along every direction of approach — Chunk 006
- **Partial derivatives**: `f_x = lim_{h→0}[f(x+h, y) − f(x, y)]/h`; `f_y` analogous — Chunk 007
- **Total differential**: `dz = f_x dx + f_y dy` — Chunk 007
- **Directional derivative**: `D_û f = ∇f · û` — Chunk 007/008
- **Gradient `∇f`**: `⟨f_{x_1}, …, f_{x_n}⟩` — Chunk 008
- **Direction cosines**: `(cos θ_1, …, cos θ_n)` — Chunk 008
- **Jacobian**: m × n matrix `(∂f_i/∂x_j)`; det used in multiple integrals — Chunk 008
- **Hessian**: n × n second-partial matrix — Chunk 008
- **MVT (single)**: `f'(c) = (f(b) − f(a))/(b − a)` — Chunk 008
- **MVT (several)**: `f(y) − f(x) = ∇f((1−c)x + cy) · (y − x)` — Chunk 008
- **Taylor polynomial `P_{k, a}`**: `Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j` — Chunk 008
- **Taylor formula**: `f(x) = P_{k, a}(x) + R_{k, a}(x)` — Chunk 008
- **Maclaurin series**: Taylor with `a = 0` — Chunk 009
- **Linear approx (1 var)**: `f(a) + f'(a)(x − a)` — Chunk 009
- **Quadratic approx (1 var)**: `+ (f''(a)/2!)(x − a)²` — Chunk 009
- **Linear approx (2 vars)**: `f(a, b) + (x − a) f_x(a, b) + (y − b) f_y(a, b)` — Chunk 009
- **Quadratic approx (2 vars)**: + `½ f_{xx}(x−a)² + f_{xy}(x−a)(y−b) + ½ f_{yy}(y−b)²` — Chunk 009

### Metric Space & Topology (Unit 15)
- **Metric on S**: `d: S × S → R` with (i) non-negativity, (ii) identity, (iii) symmetry, (iv) triangle inequality — Chunk 011
- **Metric space `(S, d)`** — Chunk 011
- **Open sphere `S(a, r)`**: `{x ∈ X : d(a, x) < r}` — Chunk 011
- **Closed sphere `S^c(a, r)`**: `{x ∈ X : d(a, x) ≤ r}` — Chunk 011
- **Open set in `(X, d)`**: every point has an open sphere inside — Chunk 012
- **Closed set in `(X, d)`**: complement is open — Chunk 012
- **Convergent sequence in `(X, d)`**: `d(x_n, x) < ε` eventually — Chunk 012
- **Continuity (metric)**: `d_1(x, x_0) < δ ⇒ d_2(f(x), f(x_0)) < ε` — Chunk 012
- **Connected set (metric)**: not the union of disjoint non-empty open sets — Chunk 012
- **Bounded set**: `∃ r > 0` with `d(s, t) < r` for all `s, t ∈ S` — Chunk 012
- **Topology `(X, T)`**: T contains X, ∅; closed under arbitrary union and finite intersection — Chunk 012
- **Open set / closed set in topology**; **Neighbourhood**: open set containing the point — Chunk 012
- **Continuity in topology**: pre-image of every neighbourhood of f(x_0) contains a neighbourhood of x_0 — Chunk 012
- **Connected set in topology**; **Open cover**; **Compact set**: every open cover has a finite subcover — Chunk 013

## Named Theorems / Models

- **Archimedean Property** — used in convergence/divergence proofs (Chunks 003, 005)
- **Triangle Inequality** — uniqueness of limit (Chunk 003)
- **Convergent ⇔ Cauchy Theorem** — Chunk 003
- **Bolzano-Weierstrass Theorem (sequences)**: every bounded sequence has a limit point — Chunk 003
- **Bolzano-Weierstrass Theorem (sets)**: every infinite, bounded set has a limit point — Chunk 004
- **Equivalent Limit-Point Characterisation** (every ε-interval contains infinitely many points) — Chunk 004
- **Pareto-Efficient Allocation Existence** (econ application of B-W) — Chunk 004
- **Extreme Value Theorem (single variable)** — continuous on `[a, b]` ⇒ attains max/min — Chunk 005
- **Extreme Value Theorem (several variables)** — Chunk 005
- **Intermediate Value Theorem** — Chunk 005
- **Mathematical Induction** (used for Fibonacci `F_{n+1} > F_n > n` for n ≥ 7) — Chunk 005
- **Binomial Theorem** (used in G.P. unboundedness, `lim n^{1/n} = 1`) — Chunks 003, 005
- **Mean Value Theorem (Lagrange's)** — single + several variables — Chunk 008
- **Taylor's Theorem** — Chunks 008, 009
- **Chain Rule** — Chunk 007
- **Directional Derivative formula** `D_A f = ∇f · Â` — Chunk 007
- **Theorem 15.2.3.1.2.1** — Open sets in `(X, d)`: arbitrary unions, finite intersections; X, ∅ open; every open sphere is an open set — Chunk 012; (v) proved in Chunk 014
- **Theorem 15.2.3.1.2.2** — Closed sets in `(X, d)`: finite unions, arbitrary intersections; X, ∅ closed — Chunk 012
- **Theorem 15.2.4.1.1** — convergence ↔ open spheres — Chunk 012
- **Theorem 15.2.4.2.1/.2/.3** — Continuity ↔ open spheres / open sets / sequential — Chunk 012
- **Theorem 15.2.4.3.1** — connected ↔ closed-set form — Chunk 012
- **Theorem 15.2.4.3.2** — R-connected sets are intervals — Chunk 012
- **Theorem (intervals in `(R, |·|)` are connected)** — Chunk 013

## Key Formulas

### Sequences (Unit 13)
- A.P.: `t_n = a + (n−1)d`; `S_n = (n/2)[2a + (n−1)d]`
- G.P.: `t_n = a · r^{n−1}`; `S_n = a(r^n − 1)/(r − 1)`
- H.P.: `t_n = 1/[a + (n−1)d]`
- Fibonacci recurrence: `F_n = F_{n−1} + F_{n−2}`, `F_0 = 0, F_1 = 1`
- Fibonacci closed form (Binet): `F_n = [{(1+√5)/2}^n − {(1−√5)/2}^n]/√5`
- Fibonacci sum: `Σ_{i=1}^n F_i = F_{n+2} − 1`

### Norms / distances (Units 13 & 15)
- Euclidean distance: `d_E(x, y) = √[Σ(x_i − y_i)²]`
- Euclidean norm: `||x|| = √Σ x_i²`
- Taxicab/Manhattan: `d_T(x, y) = Σ|x_i − y_i|`
- Minkowski-p: `d_p(x, y) = (Σ|x_i − y_i|^p)^{1/p}`, p ≥ 1
- Discrete: `d(x, y) = 0 (x = y), 1 (else)`
- Scalar/dot product: `x · y = Σ x_i y_i`

### Calculus of Several Variables (Unit 14)
- Partial derivatives: `f_x = lim_{h→0}[f(x+h, y) − f(x, y)]/h`; `f_y` analogous
- Chain rule (1 var): `dy/dx = (dy/dz)(dz/dw)(dw/dx)`
- Chain rule (1 parameter): `dw/dt = (∂w/∂x)(dx/dt) + (∂w/∂y)(dy/dt)`
- Chain rule (2 parameters): `∂w/∂r = (∂w/∂x)(∂x/∂r) + (∂w/∂y)(∂y/∂r)`
- Total differential: `dz = f_x dx + f_y dy`
- Directional derivative (2 var): `D_û f = f_x cos θ + f_y sin θ`
- Directional derivative (3 var): `f_x cos α + f_y cos β + f_z cos γ`
- Jacobian: `J_f[i, j] = ∂f_i/∂x_j` (m × n)
- Hessian: `H_f[i, j] = ∂²f/(∂x_i ∂x_j)` (n × n)
- MVT: `f'(c) = (f(b) − f(a))/(b − a)`
- Taylor polynomial: `P_{k, a}(x) = Σ_{j=0}^k (f^{(j)}(a)/j!)(x − a)^j`
- Taylor formula: `f(x) = P_{k, a}(x) + R_{k, a}(x)`
- 2-var quadratic Taylor: linear part + `½ f_{xx}(x−a)² + f_{xy}(x−a)(y−b) + ½ f_{yy}(y−b)²`

### Useful Maclaurin / Taylor expansions
- `sin(x) = x − x³/3! + x⁵/5! − …`
- `cos(x) = 1 − x²/2! + x⁴/4! − …`
- `log(x)` near `x = 1`: `(x − 1) − (x − 1)²/2 + (x − 1)³/3 − …`
- `e^{x_1+x_2+x_3} ≈ 1 + (x_1+x_2+x_3) + (½)(x_1+x_2+x_3)² + (1/6)(x_1+x_2+x_3)³`

### Convergence criteria
- `|S_n − l| < ε` for all `n > n_ε` (convergence)
- `|S_n − S_m| < ε` for all `n, m > n_ε` (Cauchy)
- `||x − y|| = d(x, y)` (norm-distance)
