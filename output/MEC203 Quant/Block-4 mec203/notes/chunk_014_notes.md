# Chunk 014 — Unit 15 Exercises and Answers (Conclusion)
<!-- Pages: 130-131 -->
<!-- Source: chunk_014.txt -->

## Section: 15.7 Exercises — Problems Posed [🟡]
<!-- Reason: Lists the questions; their full worked solutions follow. -->

### Exercises (statements)

1. Show (R^n, d_T) is a metric space, with R^n = R × R × … × R, and d_T the **Taxicab distance**:
   For x = (x_1, …, x_n), y = (y_1, …, y_n), d_T(x, y) = |x_1 − y_1| + … + |x_n − y_n| = Σ_{i=1..n} |x_i − y_i|.

2. Show (R^n, d_E) is a metric space, with d_E the **Euclidean distance**:
   d_E(x, y) = √[ Σ_{i=1..n} (x_i − y_i)^2 ].

3. In (R^2, d_T), with d_T(x, y) = |x_1 − y_1| + |x_2 − y_2|, for a = (a_1, a_2) find the open sphere S(a, 1) and the closed sphere S^c(a, 1).

4. Prove: every open sphere S(a, r) (in any metric space) is an open set.

(Answers below.)

---

## Section: Answer — Exercise 1: (R^n, d_T) is a metric space [🔴]
<!-- Reason: Generalises Check-Your-Progress 1 to arbitrary n; verifies all four metric axioms — exam-relevant. -->

### Core Idea
The Taxicab metric on R^n satisfies all four axioms exactly as on R^2, with the sum running over all n coordinates.

### Worked Proof
With d_T(x, y) = Σ_{i=1..n} |x_i − y_i|:

- **(i) Non-negativity.** Each |x_i − y_i| ≥ 0, so d_T(x, y) ≥ 0 + 0 + … + 0 = 0.
- **(ii) Identity.** d_T(x, y) = 0 iff |x_i − y_i| = 0 for each i = 1, …, n iff x_i − y_i = 0 (since |x| = 0 ⇔ x = 0) iff x_i = y_i for each i iff x = y.
- **(iii) Symmetry.** d_T(x, y) = Σ |x_i − y_i| = Σ |y_i − x_i| (by definition of mod) = d_T(y, x).
- **(iv) Triangle Inequality.** For x, y, z ∈ R^n,
  d_T(x, z) = Σ |x_i − z_i| = Σ |(x_i − y_i) + (y_i − z_i)|
  ≤ Σ [ |x_i − y_i| + |y_i − z_i| ] (by |a + b| ≤ |a| + |b|)
  = Σ |x_i − y_i| + Σ |y_i − z_i| (rearranging the summation)
  = d_T(x, y) + d_T(y, z). ⬛

### Connections
- Builds on: Check Your Progress 1 (R^2 case) (Chunk 013)

---

## Section: Answer — Exercise 2: (R^n, d_E) is a metric space [🔴]
<!-- Reason: Generalises Euclidean to arbitrary n; verifies all four metric axioms. -->

### Core Idea
The Euclidean metric on R^n satisfies all four axioms; the only delicate axiom is the triangle inequality.

### Worked Proof
With d_E(x, y) = √[ Σ_{i=1..n} (x_i − y_i)^2 ]:

- **(i) Non-negativity.** (x_i − y_i)^2 ≥ 0 for each i, so d_E(x, y) ≥ 0.
- **(ii) Identity.** d_E(x, y) = 0 iff (x_i − y_i)^2 = 0 for each i iff x_i = y_i for each i iff x = y.
- **(iii) Symmetry.** d_E(x, y) = √[ Σ (x_i − y_i)^2 ] = √[ Σ (y_i − x_i)^2 ] = d_E(y, x).
- **(iv) Triangle Inequality.** For x, y, z ∈ R^n,
  d_E(x, z) = √[ Σ (x_i − z_i)^2 ] = √[ Σ ((x_i − y_i) + (y_i − z_i))^2 ]   ... (a)
  By the generalised Pythagorean (more precisely, Minkowski / Cauchy-Schwarz) inequality,
  (a_1 + a_2 + … + a_n)^2 ≤ a_1^2 + a_2^2 + … + a_n^2 [as the source states]
  so (a) ≤ √[ Σ (x_i − y_i)^2 + Σ (y_i − z_i)^2 ]
  ≤ √[ Σ (x_i − y_i)^2 ] + √[ Σ (y_i − z_i)^2 ] (rearranging)
  = d_E(x, y) + d_E(y, z). ⬛

### ⚠️ Note on the Source's Argument
The source justifies the triangle inequality via "the generalised Pythagorean theorem," writing (a_1 + … + a_n)^2 ≤ a_1^2 + … + a_n^2. This stated inequality is **not generally true** as written (e.g., (1+1)^2 = 4 > 1+1 = 2). The correct underlying tool is the **Minkowski inequality** (or Cauchy-Schwarz). We reproduce the source's proof structure as the question requires faithfulness, but the careful proof of the Euclidean triangle inequality uses Minkowski, not "(a + b)^2 ≤ a^2 + b^2."

### Connections
- Builds on: Check Your Progress 1(2) (R^2 case) (Chunk 013)

---

## Section: Answer — Exercise 3: Open and Closed Spheres of radius 1 in (R^2, d_T) [🟡]
<!-- Reason: Routine application of definitions. -->

### Core Idea
In the Taxicab metric, the unit "sphere" around a is the set of points whose summed coordinate-wise gaps are below (open) or up to (closed) 1. Geometrically, this is a tilted square (a "diamond"), not a disk.

### Worked Answer
For a = (a_1, a_2) ∈ R^2, with d_T(x, a) = |x_1 − a_1| + |x_2 − a_2|:
- **Open sphere of radius 1**: S(a, 1) = { x = (x_1, x_2) : |x_1 − a_1| + |x_2 − a_2| < 1 }.
- **Closed sphere of radius 1**: S^c(a, 1) = { x = (x_1, x_2) : |x_1 − a_1| + |x_2 − a_2| ≤ 1 }.

> **Quick Recall:**
> - Euclidean unit ball in R^2 = open disk.
> - Taxicab unit ball in R^2 = open diamond (tilted square).

### Connections
- Builds on: Open/closed sphere in metric space (15.2.3.1.1, Chunk 011); Taxicab metric (Chunk 011)

---

## Section: Answer — Exercise 4: Every Open Sphere S(a, r) is an Open Set [🔴]
<!-- Reason: Essential theorem (Theorem 15.2.3.1.2.1(v)); proof is exam-critical. -->

### Core Idea
Inside any open sphere S(a, r), every point x has some smaller open sphere centred at x lying entirely within S(a, r). The trick is to choose the radius (r − ε), where ε = d(x, a), and apply the triangle inequality.

> **In Simple Terms:** If you're inside a ball of radius r, you have some breathing room — at least a "shell's-thickness" of room — and a tiny ball within that gap stays inside the original.

### Worked Proof

**Claim.** For (X, d) a metric space, a ∈ X, r > 0: S(a, r) is an open set.

**Proof.** By definition, S(a, r) is open if for each x ∈ S(a, r) there is an open sphere around x contained in S(a, r).

Let x ∈ S(a, r). Then d(a, x) < r.

- **Case 1: x = a.** Then S(x, r) = S(a, r) ⊆ S(a, r). ✓
- **Case 2: x ≠ a.** Then d(x, a) > 0, and d(a, x) < r.
  - Let ε = d(x, a) > 0. Then ε < r, i.e., r − ε > 0.
  - We show ]x − (r − ε), x + (r − ε)[ ⊆ S(a, r). (More precisely, the *open sphere* S(x, r − ε), which the source writes as the interval ]x − (r − ε), x + (r − ε)[ — appropriate for the R case.)
  - Let y ∈ S(x, r − ε), i.e., d(x, y) < r − ε.
  - Then by the triangle inequality, d(a, y) ≤ d(a, x) + d(x, y) < ε + (r − ε) = r.
  - Hence y ∈ S(a, r).
  - So S(x, r − ε) ⊆ S(a, r). ⬛

### Connections
- Completes: Theorem 15.2.3.1.2.1(v) (Chunk 012)
- Builds on: Triangle inequality (15.2.1, Chunk 011)

---

## End of Unit 15
This chunk concludes Unit 15 — Basic Concepts of Metric Space and Point Set Topology.
