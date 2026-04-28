# Chunk 011 — Unit 15 Begins: Metric Space Foundations
<!-- Pages: 101-110 -->
<!-- Source: chunk_011.txt -->

## Section: 15.0 Objectives & 15.1 Introduction [🟢]
<!-- Reason: Course-level motivation and historical context, not exam-critical formulas. -->

### Core Idea
Unit 15 generalises ideas from Euclidean space in two big steps. First, the notion of "distance" is abstracted into a metric, giving the discipline of metric space (any set with a notion of distance). Second, even the dependence on distance is removed, leaving only the concept of "open set," giving the discipline of topology. Both disciplines were built to handle problems where the ordinary Euclidean idea of distance is unavailable, inappropriate, or unnecessary.

> **In Simple Terms:** First we promote distance from "a tape measure between two points" to "any rule that behaves like a distance." Then we throw away the tape entirely and just keep track of "which neighbourhoods belong together" — that's topology.

### Key Concepts

#### Why generalise — metric space and topology
The 20th century pushed mathematics toward generalisation. Metric space generalises Euclidean spaces (R^2, R^3, …, R^n) to arbitrary sets equipped with a metric. Topology further generalises both metric space and Euclidean geometry by ignoring distance, angle, and congruence — only "open sets" remain. The unit will reach concepts like convergence, continuity, connectedness, and compactness in each setting.

#### "Distance" appears everywhere
The text gives many examples of intuitive distance: spatial (between cities, stars), temporal (days between two dates), thermal (difference in average temperature), social (sibling = 1, first cousin = 2, second cousin = 3), generational (parent = 1, grand-parent = 2, …). These intuitions need a formal counterpart, which is the metric.

#### Applications of distance/metric
Distance/metric is now essential in probability, statistics, graph theory, clustering, data analysis, pattern recognition, computer graphics, image analysis, speech recognition, information retrieval, astronomy, molecular biology, etc. Two specific examples cited: **Genetic distance** (genetic divergence between species/populations), and **Economic distance** (Patel, 1965 — time in years for a lagging country to catch up to the present per-capita income of an advanced country). Production-economics distances mentioned: directional distance function, Shephard input distance function, distance to frontier. (For finer applications, the text refers to Deza & Deza, 2016.)

#### Topology as "Rubber-Sheet Geometry"
The text gives a comparison of an aerial Delhi Metro Network map (LHS, with curves and varying angles/distances) versus an in-train metro map (RHS, with straight lines, near-uniform angles, and equidistant stops). Losing exact distance and angle yields a more comprehensible map. Cup ↔ doughnut and the four letters E, F, T, Y are taken as topologically equivalent because each can be obtained from another by stretching/shrinking the "rubber sheet." Topology is concerned with properties preserved under continuous deformations: stretching, twisting, crumpling, bending. Application in economics: General Equilibrium theory (e.g., Nash equilibrium); see Songzi Du, "Topology and Economics."

#### Historical origins
- **Maurice Fréchet** (French): introduced "Metric Space" in 1906 in his thesis *Sur Quelques Points du Calcul Fonctionnel*.
- **Felix Hausdorff** (German): published *Grundzüge der Mengenlehre* (Foundations of Set Theory) in 1914, where the theory of topological and metric spaces (*metrische Räume*) was created.

### Connections
- Builds on: Real numbers, intervals, |·| (Unit 1, mentioned)
- Builds on: Euclidean R^2, R^3, R^n (Unit 14, "previous unit")
- Leads to: Continuity, convergence, connectedness, compactness in metric and topological spaces (later sections of Unit 15)

---

## Section: 15.2 Metric Space — Motivation & Multiple Distances [🟡]
<!-- Reason: Sets up multiple metrics; the formulas (Euclidean, Taxicab, Minkowski) are exam-relevant though the section is preparatory. -->

### Core Idea
For the same pair of points, more than one metric may be useful, depending on the application. The Euclidean and Taxicab distances are special cases of the Minkowski distance. A useful metric must satisfy reasonable conditions — these become the metric axioms in 15.2.1.

> **In Simple Terms:** "How far apart are these two points?" can have several legitimate answers. A car driving in a grid city covers more road than a crow flies. Both numbers are valid distances — they just answer different questions.

### Key Concepts

#### Euclidean distance d_E in R^2
For points P(x_1, y_1) and Q(x_2, y_2):

d_E(P, Q) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2]

This is the "straight-line" distance.

#### Taxicab / Manhattan distance d_T
Idealising city roads as mutually parallel/perpendicular, the minimum drivable distance is the sum of the moves along the x-axis and the y-axis:

d_T(x, y) = |x_1 − x_2| + |y_1 − y_2|, for x = (x_1, y_1), y = (x_2, y_2)

Useful in **urban planning** — siting medical, educational, and other facilities depends on mass-transit/road/metro networks (Taxicab) more than Euclidean lines. The road map of Chandigarh is given as an illustration.

#### Minkowski distance of order p
For R^n (n-dimensional space over reals), order p = 1, 2, 3, …:

d_p(x, y) = ( Σ_{i=1..n} |x_i − y_i|^p )^{1/p}

- Order p = 1 → Manhattan/Taxicab distance.
- Order p = 2 → Euclidean distance.

Minkowski distances of various orders are used in statistics and optimisation problems across many domains, including economics. The most appropriate distance depends on application domain.

#### Distance on the Earth's surface
Two natural notions for distance between P and Q on Earth: (i) length of the shortest path along the great circle of the surface (used for shipping/aviation, shown in blue), and (ii) the straight-line distance through the Earth's interior (shown in red, used e.g. in seismology for travel-time of seismic waves).

### Examples / Sanity Check
Any candidate distance must rule out absurdities — e.g., "distance Delhi to Chennai by direct train" cannot exceed "distance Delhi to Chennai via the moon." The conditions that prevent such absurdities will be the **metric axioms** below.

### Comparison Table — Common Metrics

| Metric | Formula (between x, y in R^n) | Where used |
|---|---|---|
| Euclidean d_E | √[ Σ (x_i − y_i)^2 ] | Geometry, "straight-line" distance |
| Taxicab / Manhattan d_T | Σ |x_i − y_i| | Urban planning, grid streets |
| Minkowski d_p | ( Σ |x_i − y_i|^p )^{1/p} | Generalisation; statistics, optimisation |
| (Chebyshev d_∞ — implicit limit case; not formula-defined here) | — | — |

> **Quick Recall:**
> - Manhattan = Minkowski with p = 1
> - Euclidean = Minkowski with p = 2

### Connections
- Builds on: Euclidean distance in R^2 / R^3 (Unit 14)
- Leads to: Metric axioms (15.2.1)

---

## Section: 15.2.1 Metrics — The Formalised Distances (Axioms) [🔴]
<!-- Reason: The four metric axioms are core, exam-critical content for Unit 15. -->

### Core Idea
A **metric** on a non-empty set S is any function d : S × S → R that satisfies four axioms — non-negativity, identity of indiscernibles, symmetry, and the triangle inequality. These axioms are the abstract distillation of every reasonable notion of "distance."

> **In Simple Terms:** A function gets to be called a "distance" only if it (1) is never negative, (2) is zero exactly when both points coincide, (3) doesn't care which point you start from, and (4) doesn't reward you for taking a detour.

### Definitions
- **Metric on a set**: For a non-empty set S, a function d : S × S → R is called a **metric** if for all x, y, z in S it satisfies: ⭐
  - **(i) Non-negativity**: d(x, y) ≥ 0. (The cost of going from any point to any point is non-negative.)
  - **(ii) Identity of indiscernibles**: d(x, y) = 0 iff x = y. Equivalently:
    - (a) d(x, x) = 0 for any x in S (it does not cost to remain at the same point), and
    - (b) d(x, y) > 0 if x ≠ y (the cost of going to a different point is positive).
  - **(iii) Symmetry**: d(x, y) = d(y, x). (Cost of going from x to y equals cost of going back.)
  - **(iv) Triangle inequality** ("transitive property" in the source): d(x, z) ≤ d(x, y) + d(y, z). (Going directly from x to z does not exceed going from x via y to z.)

> **Quick Recall (the four axioms):**
> 1. d(x, y) ≥ 0
> 2. d(x, y) = 0 ⇔ x = y
> 3. d(x, y) = d(y, x)
> 4. d(x, z) ≤ d(x, y) + d(y, z)

### Connections
- Leads to: Definition of metric space (15.2.2)

---

## Section: 15.2.2 Metric Space — Definition & Examples [🔴]
<!-- Reason: Foundational definition plus two worked examples (Example 15.1 absolute-value metric on R, Example 15.2 discrete metric). -->

### Core Idea
A **metric space** is just an ordered pair (S, d) consisting of a non-empty set S and a metric d on it. Two key examples — both verified directly against the four axioms — are (R, d) with d(x, y) = |x − y| (the absolute-value/mod-induced metric on the real line) and the **discrete metric** on any non-empty set S (d(x, y) = 0 if x = y, else 1).

> **In Simple Terms:** Pair up any set with any rule that satisfies the four axioms, and you've made a metric space. It doesn't have to be R^n; you can metrify words, dates, family trees — anything.

### Definitions
- **Metric Space**: The ordered pair (S, d), where S ≠ ∅ and d is a metric on S, is called a **metric space**. ⭐

### Examples

**Example 15.1 — The mod / absolute-value metric on R.**
Recall Mod : R → R defined as
- Mod(x) = |x| = −x if x < 0, and = x if x ≥ 0.

So |x| ≥ 0. Define d : R × R → R by d(x, y) = |x − y|. Then (R, d) is a metric space. Verification of each axiom:

- (i) Non-negativity. Since x − y ∈ R, by definition of mod, d(x, y) = |x − y| ≥ 0.
- (ii) Identity. We know |x| = 0 iff x = 0. So d(x, y) = |x − y| = 0 iff x − y = 0 iff x = y.
- (iii) Symmetry. d(x, y) = |x − y| = |y − x| (by the mod function) = d(y, x).
- (iv) Triangle inequality. For x, y, z ∈ R:
  d(x, z) = |x − z| = |(x − y) + (y − z)| ≤ |x − y| + |y − z| (by triangular property of mod) = d(x, y) + d(y, z).

**Example 15.2 — The Discrete Metric.**
For any non-empty set S, define d : S × S → R by
- d(x, y) = 0 if x = y, and 1 if x ≠ y.

Then (S, d) is a metric space. Verification:

- (i) d(x, y) ∈ {0, 1}, hence d(x, y) ≥ 0.
- (ii) If d(x, y) = 0 then x = y (otherwise d would be 1).
- (iii) Symmetry. If d(x, y) = 0 then x = y, so d(x, y) = d(x, x) = d(y, x). If d(x, y) = 1 then y ≠ x, so d(y, x) = 1. Either way d(x, y) = d(y, x).
- (iv) Triangle inequality.
  - Case (a): if x = z, then d(x, z) = 0 = 0 + 0 ≤ d(x, y) + d(y, z).
  - Case (b): if x ≠ z, then d(x, z) = 1. For any y in S, y is unequal to at least one of x, z. Say x ≠ y; then d(x, y) = 1, so d(x, z) = 1 ≤ 1 + 0 ≤ d(x, y) + d(y, z) (since d(y, z) ≥ 0).

### Check Your Progress 1 (problems posed in this chunk)
1. Show (R^2, d_T) is a metric space, where R^2 = R × R, and the Taxicab distance is d_T(x, y) = |x_1 − y_1| + |x_2 − y_2|.
2. Show (R^2, d_E) is a metric space, where the Euclidean distance is d_E(x, y) = √[(x_1 − x_2)^2 + (y_1 − y_2)^2].

(Solutions appear in chunk 013/section 15.6 of the unit.)

### Connections
- Builds on: |·| function (Unit 1), Euclidean distance (Unit 14)
- Leads to: Open/closed sphere; open/closed sets (15.2.3)

---

## Section: 15.2.3 Open/Closed Interval, Ball, Sphere (Euclidean) [🟡]
<!-- Reason: Builds vocabulary toward open/closed spheres in metric spaces; supporting concept. -->

### Core Idea
The familiar open and closed intervals on R are the "1-dimensional" versions of more general open/closed balls (in R^2) and open/closed spheres (in R^3 and R^n). All of these can be written as the set of points whose Euclidean distance from a centre point is less than r (open) or at most r (closed).

> **In Simple Terms:** An open interval is a 1-D open ball around its midpoint. Move up a dimension, you get a disk; up another, a 3-D ball; further, an n-dimensional sphere — each time, the same idea: "all points within distance r of a centre."

### Key Concepts

#### Open / closed interval on R
For a real number a and ε > 0:
- **Open interval**: ]a − ε, a + ε[ = { x : |x − a| < ε }
- **Closed interval**: [a − ε, a + ε] = { x : |x − a| ≤ ε }

#### Open ball in R^2
For a = (a_1, a_2) ∈ R^2 and radius r > 0:
- B(a, r) = { x = (x_1, x_2) ∈ R^2 : d_E(x, a) < r }

The text describes its shape as a ball but **without boundary**.

#### Open sphere in R^3
For a = (a_1, a_2, a_3) ∈ R^3 and r > 0:
- S(a, r) = { x = (x_1, x_2, x_3) ∈ R^3 : d_E(x, a) < r }

Again, this is the sphere shape **without boundary**.

#### Open sphere in R^n
For a = (a_1, …, a_n) ∈ R^n and r > 0:
- S(a, r) = { x = (x_1, …, x_n) ∈ R^n : d_E(x, a) < r }

#### Closed ball / closed sphere
- B^c(a, r) = { x ∈ R^2 : d_E(x, a) ≤ r }
- S^c(a, r) = { x ∈ R^n : d_E(x, a) ≤ r }

### ⚠️ Common Mistakes
- ❌ Treating "ball" and "sphere" as different objects in this text. ✅ Here they're used interchangeably (the unit explicitly says the term "ball" is also used for "sphere").
- ❌ Thinking S^c is a standard notation. ✅ The text explicitly notes B^c and S^c are **not standard notations** for closed ball/sphere — they are local notation only.

### Edge Cases & Caveats
- An open ball/sphere is the strict-inequality version (`<`). The closed version uses `≤`.
- The boundary is excluded in the open version, included in the closed.

### Recap of Open Set / Closed Set in R / R^n (Euclidean) (from previous unit)
- **Open set (in R)**: A set S ⊆ R is **open** if for each a ∈ S, there exists ε > 0 such that ]a − ε, a + ε[ ⊆ S. So every member is "well inside" S; no member is a boundary point. Earlier results recalled: (i) every open interval ]a, b[ is an open set, (ii) union of open intervals is an open set.
- **Closed set (in R)**: S ⊆ R is **closed** if R − S = (−∞, +∞) − S is open in R. (R itself can be denoted (−∞, +∞).)

### Connections
- Builds on: Open/closed intervals (Unit 1)
- Leads to: Generalisation to arbitrary metric space (15.2.3.1)

---

## Section: 15.2.3.1.1 Open & Closed Sphere of an Arbitrary Metric Space [🔴]
<!-- Reason: Core abstract definition; everything later (open set, continuity, etc.) builds on this. -->

### Core Idea
Once we have a metric space (X, d), we can replicate the "ball around a point" construction *without* needing R^n. The open sphere of radius r around a is just everyone in X at distance strictly less than r from a; the closed sphere uses ≤ r.

> **In Simple Terms:** "Throw a circle of radius r around the point a" — but the geometry of the circle is dictated entirely by your chosen metric. Different metrics give differently shaped "spheres."

### Definitions
Let (X, d) be a metric space, X ≠ ∅, d a metric on X, a ∈ X, r > 0.
- **Open sphere with centre a and radius r** ⭐:
  S(a, r) = { x ∈ X : d(a, x) < r }.
- **Closed sphere with centre a and radius r** ⭐:
  S^c(a, r) = { x ∈ X : d(a, x) ≤ r }.

Notes (from the text): the term "ball" is also used for "sphere"; the notation S^c is **not standard** for closed sphere.

### Example (begins this chunk; continues into chunk 012)

**Example 15.3 — Open and closed spheres in (R, d), d(x, y) = |x − y|.**

Open sphere with centre a ∈ R and radius r > 0:
S(a, r) = { x ∈ R : d(x, a) = |x − a| < r } (i.e., the open interval ]a − r, a + r[)

Closed sphere with centre a ∈ R and radius r > 0:
S^c(a, r) = { x ∈ R : d(x, a) = |x − a| ≤ r } (i.e., the closed interval [a − r, a + r])

(The next chunk continues with Example 15.4, the same construction in (R^2, d_E).)

> **Quick Recall:**
> - Open sphere uses strict < ; closed uses ≤.
> - In (R, |·|), an open sphere is just an open interval centred at a.

### Connections
- Builds on: Metric space definition (15.2.2.2)
- Leads to: Open set in metric space (15.2.3.1.2, chunk 012)

### Open Questions
1. What does an "open sphere" look like under the **discrete metric** (Example 15.2)? — Pursued in chunk 012's Check Your Progress 2.
