# Chunk 012 — Open/Closed Sets in Metric Space; Convergence, Continuity, Connectedness, Compactness; Topology Begins
<!-- Pages: 111-120 -->
<!-- Source: chunk_012.txt -->

## Section: Example 15.4 — Open & Closed Spheres in (R^2, d_E) [🟡]
<!-- Reason: Concrete instance of open/closed sphere; supporting example. -->

### Core Idea
In the metric space (R^2, d_E) — Euclidean plane — the open sphere centred at a = (a_1, a_2) of radius r is the open disk; the closed sphere is the closed disk.

### Worked Example

**Example 15.4** (continues from chunk 011's Example 15.3).
For x = (x_1, x_2), y = (y_1, y_2):

d_E(x, y) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]

- **Open sphere** S(a, r) with centre a = (a_1, a_2) ∈ R^2, r > 0:
  S(a, r) = { x ∈ R^2 : d_E(x, a) = √[(x_1 − a_1)^2 + (x_2 − a_2)^2] < r }
- **Closed sphere** S^c(a, r):
  S^c(a, r) = { x ∈ R^2 : d_E(x, a) = √[(x_1 − a_1)^2 + (x_2 − a_2)^2] ≤ r }

> **Quick Recall:**
> - In (R, |·|), the open sphere is an open interval.
> - In (R^2, d_E), the open sphere is an open disk.

### Connections
- Builds on: Open sphere in arbitrary metric space (15.2.3.1.1, Chunk 011)

---

## Section: 15.2.3.1.2 Open Set & Closed Set of a Metric Space [🔴]
<!-- Reason: The fundamental definitions for the rest of the unit and for topology. -->

### Core Idea
A subset T of a metric space (X, d) is **open** if every point of T can be surrounded by some open sphere (in X) that lies entirely inside T — i.e., no point of T is a "boundary" point. A subset is **closed** if its complement (in X) is open.

> **In Simple Terms:** "Open" means every point has elbow room — a small sphere around it stays in the set. "Closed" is just the dual: it's what's left when you remove an open set from X.

### Definitions
- **Open set of (X, d)** ⭐: A subset T of X is **open** if for each x ∈ T, there is an open sphere S(x, ε) with ε > 0 such that S(x, ε) ⊆ T. Equivalently, every member of T is well inside T; no member is a boundary point.
- **Closed set of (X, d)** ⭐: A set T ⊆ X is **closed** if its complement X − T is an open set in X.

### Examples and Non-Examples (open sets)
1. **]1, 3[ ∪ ]5, 7[ is open**, because (a) every open interval is an open set, and (b) union of open sets is open. (Both will be proved in the theorem below.)
2. **[1, 3[ is NOT open**: no open sphere ]1 − ε, 1 + ε[ with ε > 0 fits inside [1, 3[. Similarly **[1, 3] is not open**.
3. For a real number a:
   - **]−∞, a[ is open**. Proof: Let x ∈ ]−∞, a[, so x < a. Let ε = a − x > 0. Then S(x, ε) ⊆ ]−∞, a[.
   - **]a, ∞[ is open**. Proof: Let x ∈ ]a, ∞[, so a < x. Let ε = x − a > 0. Then S(x, ε) ⊆ ]a, ∞[.

### Theorem 15.2.3.1.2.1 — Properties of Open Sets [🔴]

In a metric space (X, d):
- **(i) Union of an arbitrary number of open sets is open.**
- **(ii) Intersection of a finite number of open sets is open.**
- **(iii) The universal set X is open.**
- **(iv) The empty set ∅ is open.**
- **(v) Every open sphere S(a, r) is an open set.**

(Note: (i), (ii) proved here; (iii), (iv) under "Check Your Progress"; (v) under "Exercises and Answers" — see chunk 014.)

#### Proof of (i): Union of arbitrary open sets is open
Let { X_i : i ∈ I } be open, I an index set (finite or infinite).
- Let x ∈ ⋃_{i ∈ I} X_i, so x ∈ X_j for some particular j.
- Since X_j is open, there exists ε > 0 with S(x, ε) ⊆ X_j.
- And X_j ⊆ ⋃_i X_i.
- Hence S(x, ε) ⊆ ⋃_i X_i. ⬛

#### Proof of (ii): Finite intersection of open sets is open
Let X_1, …, X_n be open. Show ⋂_{i=1..n} X_i is open.
- If the intersection is ∅, by (iv) it is open.
- Else, let x ∈ ⋂_{i=1..n} X_i; then x ∈ X_i for each i.
- Since each X_i is open, ∃ ε_i > 0 with S(x, ε_i) ⊆ X_i.
- Let ε = min{ε_i : i = 1, …, n}. Then ε > 0 and S(x, ε) ⊆ S(x, ε_i) ⊆ X_i for each i.
- So S(x, ε) ⊆ ⋂_{i=1..n} X_i. ⬛

### ⚠️ Common Mistake
- ❌ "Intersection of arbitrary open sets is open." ✅ Only **finite** intersections are guaranteed open. (For arbitrary intersection, the analogous result holds for **closed** sets.)

### Theorem 15.2.3.1.2.2 — Properties of Closed Sets [🔴]

In a metric space (X, d):
- **(i) Union of a finite number of closed sets is closed.**
- **(ii) Arbitrary intersection of closed sets is closed.** (The source text says "arbitrary intersection of closed sets is open" but the proof clearly establishes closed; this is a typo in the source.)
- **(iii) The universal set X is closed.**
- **(iv) The empty set ∅ is closed.**

(From Theorems 15.2.3.1.2.1 and .2 together, **X and ∅ are each both open and closed.**)

#### Proof of (i): Finite union of closed sets is closed
Let C_1, …, C_n be closed. Consider X − ⋃_{i=1..n} C_i. By De Morgan's Law,
X − ⋃ C_i = ⋂_{i=1..n} (X − C_i),
where each X − C_i is open (by definition of "closed"). By Theorem 15.2.3.1.2.1(ii), the finite intersection of open sets is open. Hence X − ⋃ C_i is open, so ⋃ C_i is closed. ⬛

#### Proof of (ii): Arbitrary intersection of closed sets is closed
Let { C_i : i ∈ I } be closed. By De Morgan,
X − ⋂_{i ∈ I} C_i = ⋃_{i ∈ I} (X − C_i),
where each X − C_i is open. Union of open sets is open, so the complement of ⋂ C_i is open, hence ⋂ C_i is closed. ⬛

### Examples and Non-Examples (closed sets), Example 15.5
1. **[1, 3] ∪ [5, 7] is closed**: every closed interval is closed, and union of finitely many closed sets is closed.
2. **[1, 3[ is NOT closed**: its complement ]−∞, 1[ ∪ [3, ∞[ is not open — no sphere S(3, ε) = ]3 − ε, 3 + ε[ fits inside the complement.
3. **]−∞, a] is closed**: complement ]a, ∞[ is open. **[a, ∞[ is closed**: complement ]−∞, a[ is open.

### Check Your Progress 2 (problem in this chunk)
For (X, d) the discrete metric (d(x, y) = 0 if x = y, else 1), find S(a, 1) and S^c(a, 1) — solutions in chunk 013.

### Connections
- Builds on: Open sphere of metric space (15.2.3.1.1, Chunk 011)
- Leads to: Convergence, continuity (15.2.4); topology (15.3)

---

## Section: 15.2.4.1 Convergence of a Sequence in a Metric Space [🔴]
<!-- Reason: Core concept; generalises sequence convergence from R to any metric space. -->

### Core Idea
A sequence (x_n) in a metric space (X, d) **converges** to a point x ∈ X if eventually all of its terms lie within any prescribed positive distance of x. Equivalently, every open sphere around x eventually contains all terms of the sequence.

### Definitions
- **Convergent sequence in (X, d)** ⭐: Let (X, d) be a metric space, X ≠ ∅, with (x_n) = (x_1, x_2, …, x_n, …) an infinite sequence in X. We say (x_n) is **convergent** if there exists x ∈ X such that for each ε > 0, there exists a positive integer k such that d(x_n, x) < ε for all n > k.

### Theorem 15.2.4.1.1 (equivalent formulation, no proof)
In a metric space, (x_n) is convergent iff for each open sphere S(x, ε), ε > 0, centred on x, there exists a positive integer k such that x_n ∈ S(x, ε) for all n > k.

> **Quick Recall:**
> - Convergence "ε-style": d(x_n, x) < ε eventually.
> - Convergence "open-sphere style": x_n eventually inside S(x, ε).

### Connections
- Builds on: Convergence in R (Unit 9), R^n (Unit 12)
- Leads to: Sequence-based characterisation of continuity (Theorem 15.2.4.2.3)

---

## Section: 15.2.4.2 Continuity of a Function in Metric Space [🔴]
<!-- Reason: Major exam-relevant generalisation; three equivalent characterisations. -->

### Core Idea
Continuity at a point generalises directly from real functions to maps between metric spaces. We replace |x − x_0| < δ in the domain with d_1(x, x_0) < δ, and |f(x) − f(x_0)| < ε in the codomain with d_2(f(x), f(x_0)) < ε. Three equivalent statements: ε-δ form, open-sphere form, open-set form, and a sequential form.

> **In Simple Terms:** "Continuous at x_0" means that you can keep f's outputs arbitrarily close to f(x_0) by keeping inputs sufficiently close to x_0 — and we can phrase this with epsilons, with little balls, with open sets, or with sequences. They all say the same thing.

### Definitions
- **Continuity at x = x_0** ⭐: Let (X_1, d_1), (X_2, d_2) be metric spaces and f : X_1 → X_2. Then f is **continuous at x_0 ∈ X_1** if for each ε > 0 there exists δ > 0 such that for all x ∈ X_1, d_1(x, x_0) < δ implies d_2(f(x), f(x_0)) < ε. (Note f(x), f(x_0) ∈ X_2.)

This subsumes the Unit 9 definition for real-valued real functions.

### Theorems on Continuity (no proofs in source)

**Theorem 15.2.4.2.1** — open-sphere characterisation: f is continuous at x_0 iff for each open sphere S_2 in X_2 with centre f(x_0) and radius ε > 0, there is an open sphere S_1 in X_1 with centre x_0 and radius δ > 0 such that f(S_1) ⊆ S_2.

**Theorem 15.2.4.2.2** — open-set characterisation: f is continuous at x_0 iff for each non-empty open set S_2 in X_2, there is an open set S_1 in X_1 such that f(S_1) ⊆ S_2. (Since every open sphere is an open set, this follows from 15.2.4.2.1.)

**Theorem 15.2.4.2.3** — sequential characterisation: f is continuous at x_0 iff for every sequence (x_n) → x_0, the image sequence (f(x_n)) → f(x_0). Symbolically: x_n → x_0 ⟹ f(x_n) → f(x_0).

> **Quick Recall — three faces of continuity:**
> 1. ε–δ: d_1 small ⟹ d_2 small.
> 2. Open spheres / open sets: pre-image of "small region" contains a "small region."
> 3. Sequential: convergent sequences map to convergent sequences.

### Connections
- Builds on: Continuity in R (Unit 9)
- Leads to: Continuity in topological space (15.3.2.1)

---

## Section: 15.2.4.3 Connectedness in a Metric Space [🔴]
<!-- Reason: Core named concept; supports connectedness theorems. -->

### Core Idea
A set S in a metric space is **connected** if you cannot split it into two or more disjoint non-empty open pieces. For subsets of R (Euclidean metric), the connected sets are exactly the intervals.

> **In Simple Terms:** A connected set is "all of one piece" — no clean break into separate open clumps.

### Definitions
- **Connected set in (X, d)** ⭐: A set S in (X, d) is **connected** if it cannot be represented as the union of two or more disjoint non-empty open sets in the metric space.

### Theorems (no proofs)
- **Theorem 15.2.4.3.1**: S in (X, d) is connected iff it cannot be represented as the union of two or more disjoint non-empty closed sets.
- **Theorem 15.2.4.3.2**: A subset of R, equipped with Euclidean metric, is connected iff it is an interval (open, semi-open, or closed).

### Examples
- **Example 15.6**: In (R, d_E), each of ]3, 7[, [3, 7[, [3, 7] is a connected set. In general, any interval — open, semi-open, or closed — is connected.
- **Example 15.7**: S = ]3, 7[ ∪ ]10, 16[ is **not** connected in (R, d_E). In general, the union of two non-overlapping intervals is not connected.

### Connections
- Leads to: Connectedness in topology (15.3.2.2)

---

## Section: 15.2.4.4 Compactness in a Metric Space; Bounded Sets [🔴]
<!-- Reason: Core named concept; bounded set definition is also exam-relevant. -->

### Core Idea
A set in a metric space is **compact** iff it is closed and bounded (this characterisation is recalled here from the previous unit; the general topological definition via covers is given in 15.3.2.3). "Bounded" means all pairwise distances are uniformly capped.

### Definitions
- **Bounded set in (X, d)** ⭐: S ⊆ X is **bounded** if there exists r > 0 such that for all s, t ∈ S, d(s, t) < r.
- **Bounded metric space**: (X, d) is bounded if X itself is bounded as a subset of itself.

### Recap from Previous Unit
A subset of R is **compact** iff it is closed and bounded. The Bolzano-Weierstrass theorem and its economic applications were discussed there. Here, the concept is briefly extended to general metric spaces, and further generalised to topological spaces in 15.3.2.3.

### Worked Example

**Example 15.8 — Every finite set in (X, d) is compact (closed and bounded).**

Let A = { a_1, a_2, …, a_n } ⊆ X.
- **Boundedness.** Let M = max{ d(a_i, a_j) : i, j = 1, …, n }. Then for every pair (a_i, a_j), d(a_i, a_j) ≤ M. So A is bounded.
- **Closedness.** Show X − A is open. The universal set X is open. We can write
  X − A = (X − {a_1}) ∩ (X − {a_2}) ∩ … ∩ (X − {a_n})
  (the source writes a union but the De-Morgan-correct expression for the complement of a finite union of singletons is the **intersection** of complements; in either case the same argument applies). To show each X − {a_i} is open: let y ∈ X − {a_i}, so y ≠ a_i. Let ε = d(y, a_i) > 0. Then S(y, ε/2) does not contain a_i, i.e., S(y, ε/2) ⊆ X − {a_i}. Hence X − {a_i} is open. So A = (X − A)^c is closed.

Thus a finite set is closed and bounded, hence compact.

### Connections
- Builds on: Compactness in R (previous unit; Bolzano-Weierstrass)
- Leads to: Compactness via open covers in topology (15.3.2.3, Chunk 013)

---

## Section: 15.3 Point Set Topology — Motivation [🟢]
<!-- Reason: Motivational, sets up Section 15.3 which is core. -->

### Core Idea
Topology drops the metric entirely. The crucial concept becomes the **open set**. Theorem 15.2.4.2.2 already showed that continuity itself can be expressed using only open sets — so we have a route to define continuity, connectedness, and compactness in a setting where no metric is available or useful.

> **In Simple Terms:** Imagine zooming out so far you stop noticing exact distances and angles, but you can still tell which clumps of points stick together. That's the topological view.

### Why Generalise Beyond Metric
- The Delhi Metro example: in-train maps lose exact distance/angle but become more comprehensible to travellers.
- Real-life problems sometimes have **no useful metric**, yet still require the concept of continuity. Continuity must therefore be liberated from dependence on metrics.

### What Topology Ignores
- The concept of distance (basis of metric space).
- Distance, angle, and geometric congruence (basis of Euclidean geometry).

Topology uses only the concept of **open set**. Most concepts and theorems from metric space that are based on open sets carry over almost directly.

### Connections
- Builds on: Open set in metric space (15.2.3.1.2)
- Leads to: 15.3.1 (basic topological definitions)

---

## Section: 15.3.1 Topology — Basic Definitions [🔴]
<!-- Reason: Definitional core; topology, open/closed set, neighbourhood. -->

### Core Idea
A **topology** on X is a chosen collection T of subsets of X (i.e., T ⊆ P(X)) that contains X and ∅, and is closed under arbitrary unions and finite intersections. Members of T are decreed to be the open sets of (X, T). A set is closed iff its complement is in T. A neighbourhood of a point (or set) is any open set containing it.

> **In Simple Terms:** Hand-pick which subsets you want to call "open." As long as your list contains X and ∅, and is stable under unions and finite intersections, you have a topology — and you've inherited the entire toolkit (continuity, connectedness, compactness) for free.

### Recall: Power Set
The set of all subsets of A is the **power set** P(A). Example: A = {1, 2, 3} ⟹ P(A) = { ∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} }.

### Definitions
- **Topology / Topological Space** ⭐: For X non-empty, a **topology on X** is the ordered pair (X, T), where T ⊆ P(X) is a collection of subsets of X satisfying:
  - (i) X ∈ T,
  - (ii) ∅ ∈ T,
  - (iii) the union of any number of sets in T is in T,
  - (iv) the intersection of any **finite** number of sets in T is in T.
  Equivalently, T is closed under unions and finite intersections, and contains both X and ∅. (X, T) is also called a **topological space**.

- **Open Set** (in topology) ⭐: Each set in T is an **open set** of (X, T). A set is open iff it belongs to T. So X and ∅ are always open.

- **Closed Set** (in topology) ⭐: A subset S ⊆ X is **closed** if its complement X − S ∈ T. So X and ∅ are always closed too.

- **Neighbourhood of a point x (or a set S)** ⭐: A neighbourhood of x (or of S) is an open set (member of T) which contains the point x (or the set S).

Note: different choices of T give different topologies on the same X.

### Examples

**Example 15.9 — Indiscrete (trivial) topology.**
Let X be non-empty, T = { ∅, X }. Then (X, T) is a topology.
- (i) X ∈ T, (ii) ∅ ∈ T — obvious.
- (iii) Only union is X ∪ ∅ = X ∈ T. ✓
- (iv) Only intersection is X ∩ ∅ = ∅ ∈ T. ✓

**Example 15.10 — Discrete topology.**
(X, P(X)) is a topology on X (where P(X) is the power set).
- (i) X ∈ P(X). (ii) ∅ ∈ P(X). ✓
- (iii) Any union of subsets of X is itself a subset of X, hence in P(X). ✓
- (iv) Any intersection of subsets of X is itself a subset of X, hence in P(X). ✓

This is called the **discrete topology** on X.

**Example 15.11 — Topology induced by a metric.**
Let (X, d) be a metric space, T = { S : S is open in (X, d) }. Then (X, T) is a topological space, called the **topology induced by the metric d** (or by the metric space).
- X, ∅ are always open in any metric space, so both ∈ T.
- (iii), (iv) follow from Theorem 15.2.3.1.2.1: arbitrary unions of open sets are open; finite intersections of open sets are open.

> **Quick Recall:**
> - **Indiscrete topology** = { ∅, X }. Smallest possible.
> - **Discrete topology** = P(X). Largest possible.
> - **Metric-induced topology** = open sets of (X, d).

### Comparison Table — Open/Closed across Frameworks

| Setting | Open set defined as | Notes |
|---|---|---|
| (R, |·|) | every point has surrounding open interval inside the set | Recap from earlier unit |
| Metric space (X, d) | every point has surrounding open sphere inside the set | 15.2.3.1.2 |
| Topology (X, T) | being a member of the chosen collection T | 15.3.1 — most general |

### Connections
- Builds on: Open sets in metric space (15.2.3.1.2)
- Leads to: Continuity / connectedness / compactness in topological space (15.3.2)

---

## Section: 15.3.2.1 Continuity of a Function in Topological Space [🔴]
<!-- Reason: Continuity in the most general setting in this unit. -->

### Core Idea
A map f : X_1 → X_2 between topological spaces is **continuous at x_0** if every neighbourhood of f(x_0) in X_2 has a neighbourhood of x_0 in X_1 that is mapped into it. Distance is gone — only neighbourhoods (open sets) remain.

### Definition
Let (X_i, T_i), i = 1, 2, be topological spaces, and f : X_1 → X_2. Then f is **continuous at x_0 ∈ X_1** ⭐ if for each neighbourhood H of f(x_0) in X_2, there exists a neighbourhood G of x_0 in X_1 such that f(G) ⊆ H.

> **Quick Recall:**
> - Metric-space continuity (ε–δ) ⟹ this when T comes from d.
> - Topological continuity is just "neighbourhood of image has a neighbourhood of pre-image inside."

### Connections
- Builds on: Theorem 15.2.4.2.2 (open-set characterisation of continuity in metric spaces)
- Leads to: Connectedness, compactness (15.3.2.2, .3 — Chunk 013)
