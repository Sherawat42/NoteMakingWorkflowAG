# Unit 15 Running Context — Basic Concepts of Metric Space and Point Set Topology
<!-- Source chunks: 011, 012, 013, 014 -->
<!-- For merging into global running_context.md -->

## Key Concepts Introduced

- **Generalisation as a theme** (Chunk 011): metric space generalises Euclidean space; topology generalises both metric space and Euclidean geometry.
- **Distance / metric as a formalised idea** (Chunk 011): spatial, temporal, genetic, economic, family-tree distances.
- **Topology as Rubber-Sheet Geometry** (Chunk 011): properties preserved under stretching/twisting/crumpling/bending; cup ↔ doughnut equivalence; E, F, T, Y equivalent.
- **Multiple metrics on the same set** (Chunk 011): Euclidean d_E, Taxicab/Manhattan d_T, Minkowski d_p.
- **Metric axioms (4)** (Chunk 011): non-negativity, identity of indiscernibles, symmetry, triangle inequality.
- **Metric space (S, d)** (Chunk 011).
- **Discrete metric** (Chunk 011, Example 15.2): d = 0 if x = y, else 1.
- **Open ball / open sphere / closed sphere** in R^2, R^3, R^n, and in arbitrary (X, d) (Chunk 011).
- **Open set in (X, d)** (Chunk 012): each point sits inside an open sphere contained in the set.
- **Closed set in (X, d)** (Chunk 012): complement is open.
- **Convergence in metric space** (Chunk 012).
- **Continuity in metric space** (Chunk 012): ε–δ form, open-sphere form, open-set form, sequential form.
- **Connectedness in metric space** (Chunk 012): cannot decompose into disjoint non-empty open sets.
- **Bounded set / bounded metric space** (Chunk 012).
- **Compactness in metric space** (Chunk 012, recap from earlier unit): closed and bounded.
- **Topology / Topological space (X, T)** (Chunk 012).
- **Open set / closed set in topology** (Chunk 012): membership in T.
- **Neighbourhood of a point / set** (Chunk 012).
- **Indiscrete topology** (Chunk 012, Example 15.9): { ∅, X }.
- **Discrete topology** (Chunk 012, Example 15.10): T = P(X).
- **Topology induced by a metric** (Chunk 012, Example 15.11).
- **Continuity in topology** (Chunk 012): neighbourhood-form.
- **Connectedness in topology** (Chunk 013).
- **Cover, open cover, subcover, finite subcover** (Chunk 013).
- **Compactness via covers** (Chunk 013): every open cover has a finite subcover.
- **Cofinite topology** (Chunk 013, Check Your Progress 3-3): on infinite X.

## ⭐ Definitions

- **Metric on a set S**: function d : S × S → R satisfying (i) d(x, y) ≥ 0, (ii) d(x, y) = 0 ⇔ x = y, (iii) d(x, y) = d(y, x), (iv) d(x, z) ≤ d(x, y) + d(y, z). [Chunk 011]
- **Metric space**: ordered pair (S, d), S ≠ ∅, d a metric on S. [Chunk 011]
- **Open sphere in (X, d)**: S(a, r) = { x ∈ X : d(a, x) < r }. [Chunk 011]
- **Closed sphere in (X, d)**: S^c(a, r) = { x ∈ X : d(a, x) ≤ r }. [Chunk 011]
- **Open set in (X, d)**: every point x has open sphere S(x, ε) ⊆ T. [Chunk 012]
- **Closed set in (X, d)**: complement X − T is open in X. [Chunk 012]
- **Convergent sequence in (X, d)**: x_n → x if ∀ ε > 0 ∃ k with d(x_n, x) < ε ∀ n > k. [Chunk 012]
- **Continuity at x_0 (metric)**: ∀ ε > 0, ∃ δ > 0 such that d_1(x, x_0) < δ ⟹ d_2(f(x), f(x_0)) < ε. [Chunk 012]
- **Connected set (metric)**: not the union of two or more disjoint non-empty open sets. [Chunk 012]
- **Bounded set**: ∃ r > 0 with d(s, t) < r for all s, t ∈ S. [Chunk 012]
- **Topology (X, T)**: T ⊆ P(X) with X, ∅ ∈ T; closed under arbitrary unions and finite intersections. [Chunk 012]
- **Open set in topology**: any S ∈ T. [Chunk 012]
- **Closed set in topology**: X − S ∈ T. [Chunk 012]
- **Neighbourhood of x (or S) in (X, T)**: open set (member of T) containing x (or S). [Chunk 012]
- **Continuity in topology**: f cts at x_0 if for each neighbourhood H of f(x_0), there is a neighbourhood G of x_0 with f(G) ⊆ H. [Chunk 012]
- **Connected set in topology**: cannot be written as a disjoint union of two or more non-empty open sets. [Chunk 013]
- **Open cover**: cover by open sets, F ⊆ T. [Chunk 013]
- **Compact set**: every open cover has a finite subcover. [Chunk 013]

## Named Theorems

- **Theorem 15.2.3.1.2.1** (Open sets in (X, d)): (i) arbitrary unions are open; (ii) finite intersections are open; (iii) X is open; (iv) ∅ is open; (v) every open sphere is an open set. [Chunk 012; (v) proved in Chunk 014]
- **Theorem 15.2.3.1.2.2** (Closed sets in (X, d)): (i) finite unions are closed; (ii) arbitrary intersections are closed; (iii) X is closed; (iv) ∅ is closed. (Hence X and ∅ are both open and closed.) [Chunk 012]
- **Theorem 15.2.4.1.1** (Convergence ↔ open spheres): (x_n) converges iff every open sphere around the limit eventually contains all terms. [Chunk 012]
- **Theorem 15.2.4.2.1** (Continuity ↔ open spheres): pre-image of an open sphere contains an open sphere. [Chunk 012]
- **Theorem 15.2.4.2.2** (Continuity ↔ open sets). [Chunk 012]
- **Theorem 15.2.4.2.3** (Sequential continuity): x_n → x_0 ⟹ f(x_n) → f(x_0). [Chunk 012]
- **Theorem 15.2.4.3.1** (Connected ↔ closed-set form): connected iff cannot be split into disjoint non-empty closed sets. [Chunk 012]
- **Theorem 15.2.4.3.2** (R-connected sets are intervals): a subset of R (Euclidean) is connected iff it is an interval. [Chunk 012]
- **Theorem (intervals in (R, |·|) are connected, no proof)**: any [a, b] with a ≤ b is connected. [Chunk 013]

## Key Formulas

- **Euclidean distance** in R^2: d_E(x, y) = √[(x_1 − y_1)^2 + (x_2 − y_2)^2]. [Chunk 011]
- **Euclidean distance** in R^n: d_E(x, y) = √[ Σ_{i=1..n} (x_i − y_i)^2 ]. [Chunk 011, also Chunk 014]
- **Taxicab / Manhattan** in R^n: d_T(x, y) = Σ_{i=1..n} |x_i − y_i|. [Chunk 011]
- **Minkowski distance of order p** in R^n: d_p(x, y) = ( Σ_{i=1..n} |x_i − y_i|^p )^{1/p}, p ≥ 1. [Chunk 011]
  - p = 1 → Manhattan; p = 2 → Euclidean.
- **Discrete metric**: d(x, y) = 0 if x = y, else 1. [Chunk 011]
- **|·|-induced metric on R**: d(x, y) = |x − y|. [Chunk 011, Example 15.1]
- **Open sphere / closed sphere** in (X, d): S(a, r) = { x : d(a, x) < r }; S^c(a, r) = { x : d(a, x) ≤ r }. [Chunk 011]
