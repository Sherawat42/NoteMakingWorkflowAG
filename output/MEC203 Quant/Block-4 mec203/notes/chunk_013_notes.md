# Chunk 013 — Connectedness & Compactness in Topology; Sum-Up; Key Words; Check-Your-Progress Answers
<!-- Pages: 121-130 -->
<!-- Source: chunk_013.txt -->

## Section: 15.3.2.2 Connectedness of a Set in a Topological Space [🔴]
<!-- Reason: Core named concept in topology. -->

### Core Idea
A set S in a topological space is **connected** if you cannot split it into two non-empty open pieces with empty overlap. Intuitively, you can trace a path from any point of S to any other "without picking up the pencil."

> **In Simple Terms:** A connected set hangs together as a single piece — nothing inside it can be cleanly walled off into two open chunks.

### Definitions
- **Connected set in topology (X, T)** ⭐: A set S ∈ T is **connected** if whenever S = A ∪ B with A, B ∈ T (i.e., open in X) and A ∩ B = ∅, then either A = ∅ or B = ∅.
  Equivalently, S cannot be written as a disjoint union of two or more non-empty open sets.

(Note: the source text writes "with A ∪ B = ∅" in one place; in context — and consistent with the equivalent definition stated immediately after — this should be A ∩ B = ∅, the standard meaning of "disjoint.")

### Theorem (no proof — proof is "quite complicated despite the claim appearing simple")
In (R, d), where d(x, y) = |x − y|, any interval in R, e.g., [a, b] with a ≤ b, is connected.

### Examples and Non-Examples

**Example 15.12.** In the topology (R, T) induced by the mod function |x − y|, each of ]3, 7[, ]3, 7], [3, 7[, and [3, 7] is connected. In general, every interval — open, closed, or semi-open — is connected in this topology.

**Example 15.13.** For any topology (X, T), each set in T (which by definition is an open set of the topology) is connected.

**Example 15.14.** None of the following is connected in (R, d), d induced by |x − y|: ]3, 7[ ∪ ]8, 11[. In general, the union of at least two intervals [a_1, b_1], …, [a_n, b_n] with a_i < b_i and b_i < a_{i+1} (strict gap between consecutive intervals) is not connected. The result also holds for intervals of any open/closed/semi-open type.

### Connections
- Builds on: Connectedness in metric space (15.2.4.3, Chunk 012)

---

## Section: 15.3.2.3 Compactness of a Set in a Topological Space [🔴]
<!-- Reason: Core named concept; most general definition in unit. -->

### Core Idea
**Compactness via covers.** A cover of S is a family of subsets of X whose union contains S; an open cover is a cover by open sets. S is **compact** if every open cover of S has a **finite subcover**. This generalises "closed and bounded" (the metric/Euclidean characterisation) to settings where there is no metric.

> **In Simple Terms:** No matter how you cover the set with open clouds, finitely many of those clouds are already enough to cover it. This rules out infinite "spreading out" — N (the naturals) fail this criterion.

### Definitions
- **Cover**: In a topological space (X, T), for a set S, a **cover** of S is a family F of subsets of X with S ⊆ ⋃_{B ∈ F} B.
- **Open cover** ⭐: A cover F is an **open cover** if every B ∈ F is open, i.e., F ⊆ T.
- **Subcover / Finite subcover** ⭐: For a cover F of S, a **subcover** F′ is a sub-family F′ ⊆ F that is also a cover of S. If F′ contains only finitely many sets, it is a **finite subcover**.
- **Compact Set / Space** ⭐: A set S in (X, T) is **compact** if every open cover of S has a finite subcover. If X itself is compact, X is a **compact space**.

### Example

**Example 15.15 — N is not compact in (R, d), d = |x − y|.**

Consider open intervals O_n = ]n − 1/4, n + 1/2[ for n = 1, 2, …. (This is the source's family; the precise endpoints aren't critical, only that each O_n contains exactly one natural number.) Then N ⊆ ⋃_{n=1}^∞ O_n because n ∈ O_n for every n ∈ N.

If N were compact, finitely many O_n would suffice. But each O_n contains only one integer, so finitely many O_n contain only finitely many naturals — not all of N. Contradiction. Hence N is not compact. ⬛

> **Quick Recall:**
> - Compact = "every open cover has a finite subcover."
> - In metric/Euclidean space, this is equivalent to "closed and bounded."

### Connections
- Builds on: Compactness in metric space (15.2.4.4, Chunk 012)

---

## Section: Check Your Progress 3 [🟡]
<!-- Reason: Practice problems; their answers are given in 15.6, summarised here. -->

### Problems posed
1. In (R, d), d induced by |x − y|:
   - (i) Each of N, Z, Q (subset of R) is not connected. Also, any subset of N, Z, Q is not connected.
   - (ii) Any singleton {a} of Euclidean metric space is not connected.
   - (iii) Any finite subset {a_1, …, a_n} of Euclidean metric space is not connected.
2. Let X = {a, b, c}, T = { ∅, {a}, {a, b}, {a, c}, X }. Show (X, T) is a topology.
3. Let X be any infinite set, T = { S : S ⊆ X, X − S is a finite subset of X } ∪ { ∅ }. Show (X, T) is a topology. (This is the **cofinite topology**.)
4. Show that a finite set in (R, d), d = |x − y|, is compact.

(Answers in section 15.6 — summarised below.)

---

## Section: 15.4 Let Us Sum Up [🟢]
<!-- Reason: Course summary, not exam-critical content. -->

### Recap
The unit covered two advanced disciplines: **Metric Space** and **Topology**. After defining each, the underlying notions of open/closed interval/sphere were developed and their properties discussed. Within each discipline, practically useful concepts were introduced: convergence of sequences, continuity of functions, connectedness of sets, and compactness of sets — along with their properties and applications.

---

## Section: 15.5 Key Words — Glossary [🔴]
<!-- Reason: Exam-critical reference list of all formal definitions in the unit. -->

### All Key Definitions (consolidated from the source's Key Words section)

- **Euclidean Distance d_E** in 2-D space R^2: For P(x_1, y_1), Q(x_2, y_2),
  d_E(P, Q) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]. ⭐

- **Taxicab / Manhattan Distance d_T** between P(x_1, y_1) and Q(x_2, y_2):
  d_T(x, y) = |x_1 − x_2| + |y_1 − y_2|. ⭐

- **Minkowski Distance of order p** in R^n:
  d_p(x, y) = ( Σ_{i=1..n} |x_i − y_i|^p )^{1/p}, for p = 1, 2, 3, ….

- **Metric on a Set** (4 axioms): a function d : S × S → R with (i) d(x, y) ≥ 0, (ii) d(x, y) = 0 ⇔ x = y (i.e., d(x, x) = 0; d(x, y) > 0 if x ≠ y), (iii) d(x, y) = d(y, x), (iv) d(x, z) ≤ d(x, y) + d(y, z). ⭐

- **Metric Space**: ordered pair (S, d), S ≠ ∅, d a metric on S. ⭐

- **Open ball / sphere in R^n**: For a ∈ R^n, r > 0, S(a, r) = { x ∈ R^n : d_E(x, a) < r }.
- **Closed ball / sphere in R^n**: S^c(a, r) = { x ∈ R^n : d_E(x, a) ≤ r }. (S^c not standard notation.)

- **Open Set in R**: S ⊆ R is open if for each a ∈ S, there exists ε > 0 such that ]a − ε, a + ε[ ⊆ S.
- **Closed Set in R**: S ⊆ R is closed if R − S is open in R.

- **Open Sphere in (X, d)**: S(a, r) = { x ∈ X : d(a, x) < r }. ⭐
- **Closed Sphere in (X, d)**: S^c(a, r) = { x ∈ X : d(a, x) ≤ r }. ⭐

- **Open Set in (X, d)**: T ⊆ X is open if for each x ∈ T there is an open sphere S(x, ε), ε > 0, with S(x, ε) ⊆ T. ⭐
- **Closed Set in (X, d)**: T ⊆ X is closed if X − T is open in X. ⭐

- **Convergence in (X, d)**: (x_n) → x if for every ε > 0 there exists positive integer k with d(x_n, x) < ε for all n > k. ⭐

- **Continuity at x_0 in metric space**: For (X_i, d_i), i = 1, 2, f : X_1 → X_2 is continuous at x_0 if for every ε > 0 there exists δ > 0 such that d_1(x, x_0) < δ ⟹ d_2(f(x), f(x_0)) < ε. ⭐

- **Connected Set (metric space)**: S ⊆ X is connected if it cannot be represented as a union of two or more disjoint non-empty open sets in (X, d). ⭐

- **Bounded Set / Bounded Metric Space**: S ⊆ X bounded if ∃ r > 0 with d(s, t) < r for all s, t ∈ S. (X, d) bounded if X is bounded as a subset of itself. ⭐

- **Topology / Topological Space (X, T)**: For X ≠ ∅, T ⊆ P(X) with (i) X ∈ T, (ii) ∅ ∈ T, (iii) T closed under arbitrary unions, (iv) T closed under finite intersections. ⭐

- **Open Set in (X, T)**: any element of T.
- **Closed Set in (X, T)**: S ⊆ X with X − S ∈ T.
- **Neighbourhood of x (or set S) in (X, T)**: an open set (member of T) containing x (or S). ⭐

- **Continuity in topology**: f : X_1 → X_2 continuous at x_0 if for each neighbourhood H of f(x_0) in X_2, there is a neighbourhood G of x_0 in X_1 with f(G) ⊆ H. ⭐

- **Connectedness in topology**: S ∈ T is connected if it cannot be written as a disjoint union of two or more non-empty open sets. ⭐

- **Cover**: family F of subsets of X with S ⊆ ⋃_{B ∈ F} B.
- **Open Cover**: cover with F ⊆ T (every B is open). ⭐
- **Subcover / Finite subcover**: F′ ⊆ F that is itself a cover; finite if F′ has finitely many sets. ⭐
- **Compact Set / Space**: S in (X, T) compact if every open cover has a finite subcover. (X, T) compact if X is compact. ⭐

---

## Section: 15.6 Answers / Hints to Check Your Progress [🟡]
<!-- Reason: Worked solutions to in-text exercises; supports earlier core definitions. -->

### Check Your Progress 1 — Solutions

**(1) (R^2, d_T) is a metric space.** With d_T(x, y) = |x_1 − y_1| + |x_2 − y_2| = Σ_{i=1,2} |x_i − y_i|.
- (i) Each |x_i − y_i| ≥ 0, so d_T(x, y) ≥ 0.
- (ii) d_T(x, y) = 0 iff |x_i − y_i| = 0 for i = 1, 2 iff x_i = y_i iff x = y.
- (iii) Symmetry: |x_i − y_i| = |y_i − x_i| ⟹ d_T(x, y) = d_T(y, x).
- (iv) Triangle inequality: For x, y, z ∈ R^2,
  d_T(x, z) = Σ |x_i − z_i| = Σ |(x_i − y_i) + (y_i − z_i)|
  ≤ Σ [ |x_i − y_i| + |y_i − z_i| ] (by |a + b| ≤ |a| + |b|)
  = Σ |x_i − y_i| + Σ |y_i − z_i| = d_T(x, y) + d_T(y, z). ⬛

**(2) (R^2, d_E) is a metric space.** With d_E(x, y) = √[(x_1 − y_1)^2 + (x_2 − y_2)^2] = √[ Σ_{i=1,2} (x_i − y_i)^2 ].
- (i) (x_i − y_i)^2 ≥ 0 ⟹ d_E ≥ 0.
- (ii) d_E = 0 iff (x_i − y_i)^2 = 0 for each i iff x_i = y_i iff x = y.
- (iii) Symmetry: (x_i − y_i)^2 = (y_i − x_i)^2 ⟹ d_E(x, y) = d_E(y, x).
- (iv) Triangle inequality: For x, y, z ∈ R^2,
  d_E(x, z) = √[ Σ (x_i − z_i)^2 ] = √[ Σ ((x_i − y_i) + (y_i − z_i))^2 ]
  ≤ √[ Σ (x_i − y_i)^2 ] + √[ Σ (y_i − z_i)^2 ] (the source labels this "Pythagorean theorem"; rigorously this is the **Minkowski / triangle inequality** for the L^2 norm — the source's invocation of "(a + b)^2 ≤ a^2 + b^2" is loosely worded but the conclusion stands)
  = d_E(x, y) + d_E(y, z). ⬛

### Check Your Progress 2 — Solutions

**(1) Discrete metric spheres.**
For (X, d) with d(x, y) = 0 if x = y, else 1; for a ∈ X:
- **S(a, 1)** = { a }. Only a itself is at distance < 1; every other point has distance exactly 1, not less.
- **S^c(a, 1)** = X. Every point has distance ≤ 1.

**(2) X is open in any metric space.**
Let x ∈ X; for any ε > 0, S(x, ε) = { y ∈ X : d(x, y) < ε } ⊆ X by definition. ⬛

**(3) ∅ is open.**
By contradiction: if ∅ were not open, it would contain some y with no S(y, ε) ⊆ ∅. But ∅ has no elements — contradiction. ⬛

**(4) X is closed.**
X − X = ∅, which is open (just proved). So X^c is open, hence X is closed. ⬛

**(5) ∅ is closed.**
X − ∅ = X, which is open. So ∅^c is open, hence ∅ is closed. ⬛

(Combined: in any metric space, X and ∅ are each both open and closed.)

### Check Your Progress 3 — Solutions

**(1) N, Z, Q (and any subsets of these) are not connected in (R, |·|).**
Use Theorem 15.2.4.3.2: a subset of R is connected iff it is an interval. None of N, Z, Q (or any of their subsets except trivial intervals) is an interval — so each is not connected.

**(1)(ii) Singleton {a} is not connected.**
R − {a} = ]−∞, a[ ∪ ]a, ∞[ is a union of two non-empty open intervals — i.e., {a} can be sandwiched in a way that makes its complement disconnected … (The source's argument: the singleton's complement is a union of two open intervals, demonstrating it is not an interval. Note: under the Theorem 15.2.4.3.2 criterion, a single point is technically a degenerate "closed interval" [a, a]; the source nevertheless classifies it as "not connected" presumably under the strict-interval reading. We follow the source.)

**(1)(iii) Finite subset {a_1 < a_2 < … < a_n} is not connected.**
R − {a_1, …, a_n} = ]−∞, a_1[ ∪ ]a_1, a_2[ ∪ … ∪ ]a_{n−1}, a_n[ ∪ ]a_n, ∞[, each piece an open interval. Hence the finite set is not an interval and not connected.

**(2) (X, T) with X = {a, b, c}, T = { ∅, {a}, {a, b}, {a, c}, X } is a topology.**
- (i) X ∈ T. (ii) ∅ ∈ T.
- (iii) Unions: any union involving X gives X ∈ T. Any union involving ∅ gives the other set ∈ T. Also {a, b} ∪ {a, c} = X ∈ T, and {a, b} ∪ {a, c} ∪ {a} = X ∈ T. ✓
- (iv) Intersections: any intersection involving ∅ gives ∅ ∈ T. Any intersection involving {a} gives {a} ∈ T. {a, b} ∩ {a, c} = {a} ∈ T. ✓

**(3) The cofinite topology on an infinite set X.**
T = { S ⊆ X : X − S is finite } ∪ { ∅ }.
- (i) X ∈ T because X − X = ∅, finite. (ii) ∅ ∈ T by definition.
- (iii) Let { Y_i } ⊆ T. Their union Y has X − Y ⊆ X − Y_1, which is finite, hence X − Y is finite, hence Y ∈ T.
- (iv) For finite intersection of Y_1, …, Y_n in T: by De Morgan, X − ⋂ Y_i = ⋃_{i=1..n} (X − Y_i), a finite union of finite sets, hence finite. So ⋂ Y_i ∈ T. ✓

**(4) A finite set is compact in (R, |·|).**
Let S = {x_1, …, x_k} and let { O_α } be any open cover of S. For each x_i, pick some O_{α_i} containing x_i. Then { O_{α_1}, …, O_{α_k} } is a finite subcover of S. ⬛

### Connections
- Builds on: Definitions and theorems throughout 15.2 and 15.3.
- Leads to: Exercises and Answers (15.7), in chunk 014.
