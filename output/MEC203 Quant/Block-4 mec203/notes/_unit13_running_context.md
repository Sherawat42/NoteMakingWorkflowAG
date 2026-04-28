# Unit 13 (MEC-203 Block 4) — Running Context

Compiled from chunks 001-005 of Unit 13: Real Analysis. To be merged into the global `running_context.md`.

## Key Concepts Introduced
- Real Analysis as branch of Mathematical Analysis (real-numbers domain) — Chunk 002
- Difference between Calculus and Real Analysis (apply vs justify) — Chunk 002
- Sequence (set view: ordered, enumerated, repetition allowed) — Chunk 002
- Sequence (function view: `f: S → R`, with `S` = N or interval subset) — Chunk 002
- Indexing set, term/element, index/rank, length, n-tuple, subsequence — Chunk 002
- Recursively definable sequence — Chunk 002
- Arithmetic Progression (A.P.) with initial term `a` and common difference `d` — Chunk 002
- A.P. sum derivation by reverse-and-pair argument — Chunk 002
- Geometric Progression (G.P.) with scale factor `a` and common ratio `r` — Chunk 003
- Trivial G.P. cases (`a = 0`, `r = 0`, `r = 1`) excluded — Chunk 003
- Sum of G.P. when `|r| < 1` form — Chunk 003
- Harmonic Progression (H.P.) as reciprocals of A.P. — Chunk 003
- Harmonic Sequence: `1, 1/2, 1/3, ...` — Chunk 003
- Fibonacci sequence with closed-form (Binet) formula — Chunk 003
- Sum formula for Fibonacci: `Σ F_i = F_{n+2} − 1` — Chunk 003
- Bounded above / below / bounded sequence — Chunk 003
- Boundedness results for non-trivial A.P., G.P., Fibonacci — Chunk 003
- Monotone sequences (increasing / decreasing / strict) — Chunk 003
- Alternating sequence — Chunk 003
- Independence of boundedness and monotonicity — Chunk 003
- Convergent sequence (ε–`n_ε` definition) — Chunk 003
- Limit of a sequence (uniqueness) — Chunk 003
- Cauchy sequence — Chunk 003
- Equivalence of convergent and Cauchy sequences — Chunk 003
- Non-convergent categories: finitely oscillatory, divergent to ±∞, infinitely oscillatory — Chunk 003
- Limit point of a sequence — Chunk 003
- Open / closed / bounded / compact sets in R — Chunk 004
- Only `∅` and `R` are both open and closed — Chunk 004
- Limit point of a set (= accumulation / condensation / cluster point) — Chunk 004
- R^n as n-fold Cartesian product of R; n-tuples — Chunk 004
- Vector addition, scalar multiplication, zero vector, additive inverse on R^n — Chunk 004
- Euclidean distance `d(x, y)`; Euclidean norm `||x||`; relation `||x − y|| = d(x, y)` — Chunk 004
- Functions over Euclidean spaces (vector +, scalar ·, dot product, norm, distance, projection) — Chunk 004
- Open disc / closed disc in R^n (replacing open / closed interval) — Chunk 004
- Open / closed / bounded / compact sets in R^n — Chunk 004
- Limit and continuity for `f: R^n → R` (ε-δ with norm) — Chunk 004
- Limit and continuity for `f: R^n → R^m` (ε-δ with norm on both sides) — Chunk 005
- Local minima / maxima as *values* (not points) — Chunk 005
- Global / Absolute Minimum / Maximum — Chunk 005
- Global extremum at boundary may not be local — Chunk 005

## ⭐ Definitions (exam-critical, explicit in Key Words or Objectives)
- **Sequence (function)**: `f: S → R`, `S = N` or interval subset of N (Chunk 002)
- **Subsequence**: deletion preserving relative order (Chunk 002)
- **Recursively definable sequence**: nth term via formula on previous terms (Chunk 002)
- **A.P.**: `a, a+d, a+2d, ...` (Chunk 002)
- **A.P. nth term**: `t_n = a + (n−1)d` (Chunk 002)
- **A.P. sum**: `S_n = (n/2)[2a + (n−1)d] = (n/2)(t_1 + t_n)` (Chunk 002)
- **G.P.**: `a, ar, ar², ...` (Chunk 003)
- **G.P. nth term**: `t_n = a · r^{n−1}` (Chunk 003)
- **G.P. sum**: `S_n = a(r^n − 1)/(r − 1)` (Chunk 003)
- **H.P.**: reciprocals of an A.P., `1/(a + (n−1)d)` (Chunk 003)
- **Fibonacci**: `F_0 = 0`, `F_1 = 1`, `F_n = F_{n−1} + F_{n−2}` (Chunk 003)
- **Bounded sequence**: `D ≤ S_n ≤ C` for all `n ∈ N` (Chunk 003)
- **Monotone sequence (increasing/decreasing, strict)** (Chunk 003)
- **Convergent sequence**: ∀`ε > 0`, ∃ `n_ε`: `|S_n − l| < ε` ∀ `n > n_ε` (Chunk 003)
- **Cauchy sequence**: ∀`ε > 0`, ∃ `n_ε`: `|S_n − S_m| < ε` ∀ `n, m > n_ε` (Chunk 003)
- **Limit point of sequence**: `LP` such that some subsequence converges to `LP` (Chunk 003)
- **Open set in R**: every point has an ε-interval inside the set (Chunk 004)
- **Closed set in R**: complement is open (Chunk 004)
- **Bounded set**: bounded above and below (Chunk 004)
- **Compact set**: closed AND bounded (Chunk 004)
- **Limit point of a set**: every ε-interval contains a point of S different from p (Chunk 004)
- **R^n**: `{(a_1, ..., a_n) : a_i ∈ R}` (Chunk 004)
- **Euclidean distance / norm**: `d(x, y) = √Σ (x_i − y_i)²`; `||x|| = √Σ x_i²` (Chunk 004)
- **Open disc in R^n**: `{x : ||x − a|| < ε}` (Chunk 004)
- **Closed disc in R^n**: `{x : ||x − a|| ≤ ε}` (Chunk 004)
- **Limit / continuity for `f: R^n → R^m`**: ε-δ with norms on both sides (Chunk 005)
- **Local maxima/minima**: *values*, attained at points where `f(p)` dominates/is dominated within an ε-neighbourhood (Chunk 005)

## Named Theorems / Models
- **Archimedean Property** — used in Examples 13.14, F.1, F.2 and in Q2/Q3 of exercises (Chunks 003, 005)
- **Triangle Inequality** — used in uniqueness-of-limit proof (Chunk 003)
- **Convergent ⇔ Cauchy Theorem** — Chunk 003
- **Bolzano-Weierstrass Theorem for Sequences**: every bounded sequence has a limit point. Corollary: every bounded sequence has a convergent subsequence. (Chunk 003)
- **Bolzano-Weierstrass Theorem for Sets**: every infinite and bounded set has a limit point. (Chunk 004)
- **Equivalent Limit-Point Characterisation**: `p` is a limit point of `S` iff every ε-interval around `p` contains infinitely many points of `S`. (Chunk 004)
- **Pareto-Efficient Allocation Existence** (economic application of Bolzano-Weierstrass): if the set of allocations is compact and non-empty, the system has a Pareto-efficient allocation. (Chunk 004)
- **Extreme Value Theorem (single variable)**: continuous on `[a, b]` ⇒ attains absolute max and min. (Chunk 005)
- **Extreme Value Theorem (several variables)**: continuous on closed disc `D` ⇒ attains absolute max and min. (Chunk 005)
- **Intermediate Value Theorem**: continuous `f` on `[a, b]` takes any value between `f(a)` and `f(b)`. (Chunk 005)
- **Mathematical Induction** (used in Q4 to prove Fibonacci inequality `F_{n+1} > F_n > n` for `n ≥ 7`). (Chunk 005)
- **Binomial Theorem** (used in Q3 G.P. unboundedness proof and CYP3 limit of `n^{1/n}`). (Chunks 003, 005)

## Key Formulas
- **A.P. nth term**: `t_n = a + (n − 1)d`
- **A.P. sum**: `S_n = (n/2)[2a + (n − 1)d] = (n/2)(t_1 + t_n)`
- **A.P. recursion**: `t_n = t_{n−1} + d`
- **G.P. nth term**: `t_n = a · r^{n−1}`
- **G.P. sum**: `S_n = a(r^n − 1)/(r − 1)`, or `a(1 − r^n)/(1 − r)` when `|r| < 1`
- **H.P. nth term**: `t_n = 1/[a + (n−1)d]`
- **Fibonacci recurrence**: `F_n = F_{n−1} + F_{n−2}`, `F_0 = 0`, `F_1 = 1`
- **Fibonacci closed form (Binet)**: `F_n = [{(1+√5)/2}^n − {(1−√5)/2}^n] / √5`
- **Fibonacci sum**: `Σ_{i=1}^n F_i = F_{n+2} − 1`
- **Convergence (ε-`n_ε`)**: `|S_n − l| < ε` for all `n > n_ε`
- **Cauchy criterion**: `|S_n − S_m| < ε` for all `n, m > n_ε`
- **Euclidean distance in R^n**: `d(x, y) = √[Σ_{i=1}^n (x_i − y_i)²]`
- **Euclidean norm in R^n**: `||x|| = √[Σ_{i=1}^n x_i²]`, with `||x|| = d(x, 0)`
- **Norm-distance link**: `||x − y|| = d(x, y)`
- **Scalar (dot) product**: `x · y = Σ_{i=1}^n x_i y_i`
- **Limit in R^n** (ε-δ): `||x − a|| < δ ⇒ ||f(x) − l|| < ε` (or `|f(x) − l| < ε` for real-valued `f`)
